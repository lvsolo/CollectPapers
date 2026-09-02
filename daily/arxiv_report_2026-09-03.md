# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-09-03  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 55 篇（其中 55 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (10篇)
- [Multimodal](#multimodal) (10篇)
- [Vision Transformer](#vision-transformer) (7篇)
- [Network Pruning](#network-pruning) (6篇)
- [Self-supervised Vision](#self-supervised-vision) (5篇)
- [Video Understanding](#video-understanding) (4篇)
- [Multi-camera Perception](#multi-camera-perception) (4篇)
- [Open-set Detection](#open-set-detection) (2篇)
- [BEV](#bev) (2篇)
- [Autonomous Driving](#autonomous-driving) (2篇)
- [Tracking](#tracking) (1篇)
- [3D Detection](#3d-detection) (1篇)
- [Object Detection](#object-detection) (1篇)

## VLM

### 1. IntroConformal: Conformal Factuality Guarantees for Large Vision-Language Models via Introspective Signals **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.01375](https://arxiv.org/abs/2609.01375)  · [📄 PDF](https://arxiv.org/pdf/2609.01375)
- **作者**: Md. Atabuzzaman, Christian Alexander, Chris Thomas
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.CL
- **摘要（中）**: ①针对大型视觉语言模型（LVLMs）生成内容的事实性缺乏统计保证的问题，现有方法依赖外部验证器或生成时置信度信号，存在辅助依赖或对自信但错误输出失效的缺陷。②提出了IntroConformal，一个无需训练的共形风险控制（CRC）框架，利用模型自身的内部信号（如层间语义稳定性和验证概率）提供有限样本、分布无关的事实性保证。③相比现有工作，创新性地使用内省信号替代外部验证器，减少了辅助依赖并提高了对错误输出的鲁棒性。④在多个LVLM架构上，IntroConformal满足共形风险保证，同时显著减少弃权，并在声明级判别上达到或超过基于外部验证器的基线。
- **摘要（英）**: This paper addresses the lack of statistical factuality guarantees in LVLMs by proposing IntroConformal, a training-free Conformal Risk Control framework that leverages introspective signals like layer-wise semantic stability and verification probability. It eliminates reliance on external verifiers, achieving finite-sample guarantees with reduced abstention and competitive claim-level discrimination across multiple architectures.
- **评估**: 该论文为LVLM事实性控制提供了新颖的统计框架，内省信号的设计具有理论深度，对可靠性敏感的自动驾驶场景有潜在参考价值。
- **核心贡献**: 提出了首个基于内省信号的共形风险控制框架，为LVLM事实性提供统计保证。
- **创新点**: 利用模型内部隐藏状态信号替代外部验证器，实现无需训练的事实性控制。
- **结果**: 在多个LVLM上满足共形保证，弃权率显著降低，判别性能优于或持平外部验证器基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) have achieved strong multimodal performance, yet ensuring the factual correctness of generated content remains challenging. Existing methods that provide statistical guarantees on factuality typically rely on external verifiers or generation-time confidence signals, which introduce auxiliary dependencies or often fail for confident but incorrect outputs. We argue that reliable factuality control can instead be achieved through introspective signals derived from the model itself. We introduce IntroConformal, a training-free Conformal Risk Control (CRC) framework that provides finite-sample, distribution-free factuality guarantees. We first instantiate it with layer-wise semantic stability, a conformity score derived from hidden-state representations, and then propose verification probability, a stronger score capturing the model's self-administered judgment on claim factuality. Across multiple LVLM architectures, IntroConformal satisfies the conformal risk guarantee while substantially reducing abstention and achieving competitive or superior claim-level discrimination relative to external verifier-based baselines.

</details>

### 2. Reliability Challenges in Diffusion Vision-Language Models **⭐⭐⭐** (相关度: 50%, 质量: 0.65)

- **arXiv ID**: [2609.01318](https://arxiv.org/abs/2609.01318)  · [📄 PDF](https://arxiv.org/pdf/2609.01318)
- **作者**: Md. Atabuzzaman, Chris Thomas
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.CL
- **摘要（中）**: ①针对扩散式大型视觉语言模型（dLVLMs）的可靠性（如幻觉和偏见）尚未被系统评估的问题。②首次对六种扩散模型和自回归基线在四个维度上进行可靠性基准测试，涵盖幻觉率、偏见、多项选择准确率等。③发现dLVLMs反转了AR模型的yes-bias，幻觉率相当但语言质量下降，在少数族裔群体上准确率崩溃且性别偏见极性相反，并存在长度先验导致的多项选择准确率崩溃。④这些模式在不同模型家族中变化，揭示了扩散生成特有的机制信号。
- **摘要（英）**: This paper presents the first systematic reliability evaluation of diffusion-based LVLMs, benchmarking six models against autoregressive baselines across hallucination, bias, and accuracy dimensions. Key findings include reversed yes-bias, degraded linguistic quality, and accuracy collapse on underrepresented groups, highlighting unique mechanistic signals in diffusion generation.
- **评估**: 该论文填补了dLVLMs可靠性研究的空白，发现对多模态模型设计有重要警示，但相关性较弱。
- **核心贡献**: 首次系统评估了扩散式LVLMs的幻觉和偏见可靠性。
- **创新点**: 揭示了扩散模型特有的长度先验和去噪步骤相关的幻觉机制。
- **结果**: 发现dLVLMs在偏见和多项选择上存在严重可靠性问题，准确率可崩溃至近零。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our key findings are: (1) dLVLMs reverse the yes-bias of AR models in binary visual queries; (2) they achieve competitive hallucination rates yet exhibit degraded linguistic quality; (3) they collapse to near-zero accuracy on underrepresented racial groups with opposite-polarity gender bias; and (4) they exhibit accuracy collapse in multiple-choice settings when the correct option is shorter than its distractors, associated with a length prior that emerges at the first denoising step. Tokens committed at late denoising steps with low confidence further correlate with hallucinated content, pointing to a mechanistic signal unique to diffusion generation. These patterns vary across model families, suggesting reliability is shaped by the generative paradigm together with training data.

</details>

### 3. Dyn-3D: Unveiling and Resolving Ego-Motion Ambiguity in Vision-Language Models **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.01059](https://arxiv.org/abs/2609.01059)  · [📄 PDF](https://arxiv.org/pdf/2609.01059)
- **作者**: Jiayu Ding, Zhuodong Liu, Lei Zhang et al. (9 authors)
- **🏷️ 机构**: PolyU / OPPO
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对视觉语言模型（VLMs）在动态3D空间推理中因自我运动感知不足导致尺度模糊和运动估计退化的问题，尤其在较大位移下出现运动崩溃。②提出了Dyn-3D基准，使用反事实3D渲染解耦视觉变化与真实运动属性，并设计了TempoVista框架，包含Kinematic-GSPO算法，将度量物理真值嵌入策略优化中。③相比现有方法，显式地将视觉表示锚定在3D空间，利用相机动力学作为几何校准信号。④实验表明，该方法显著提升了运动估计和鲁棒空间推理能力。
- **摘要（英）**: This paper tackles ego-motion ambiguity in VLMs for dynamic 3D reasoning by introducing the Dyn-3D benchmark with counterfactual rendering and the TempoVista framework with Kinematic-GSPO, which embeds metric physical ground truth into policy optimization. It improves motion estimation and spatial reasoning by grounding visual representations in 3D space, addressing kinematic collapse under large displacements.
- **评估**: 该论文直接针对自动驾驶中的运动感知问题，反事实基准和物理监督方法具有高实用价值。
- **核心贡献**: 提出了Dyn-3D基准和TempoVista框架，解决VLM在动态3D推理中的自我运动歧义。
- **创新点**: 利用反事实渲染和物理真值策略优化，显式校准视觉运动表示。
- **结果**: 显著提升运动估计和空间推理鲁棒性，尤其在较大位移场景。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As Vision-Language Models (VLMs) tackle dynamic 3D spatial reasoning, ego-motion perception becomes essential to resolve monocular scale ambiguity. However, current models often overfit to smooth trajectory priors rather than genuinely understanding physical motion. Consequently, their spatial reasoning degrades severely under large displacements, a phenomenon we term Kinematic Collapse. This failure stems from spurious visual-motion correlations in natural videos and a lack of explicit physical supervision. To evaluate this, we introduce Dyn-3D, a benchmark using counterfactual 3D rendering to rigorously decouple visual changes from true kinematic properties. Furthermore, we propose the TempoVista framework, featuring the Kinematic-GSPO algorithm. By embedding metric physical ground truth into policy optimization, TempoVista explicitly grounds visual representations in 3D space. Experiments demonstrate that our approach significantly improves both motion estimation and robust spatial reasoning by utilizing camera dynamics as an effective geometric calibration signal.

</details>

### 4. The Visual Insensitivity Gap: Diagnosing When Vision-Language Models Fail to Use Visual Evidence **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.85)

- **arXiv ID**: [2609.00868](https://arxiv.org/abs/2609.00868)  · [📄 PDF](https://arxiv.org/pdf/2609.00868)
- **作者**: Genpei Zhang
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.CL, cs.LG
- **摘要（中）**: ①针对视觉语言模型在多模态基准测试中可能未真正使用视觉输入的问题，现有评估仅依赖聚合准确率，忽略了视觉证据利用的失败。②提出了视觉不敏感间隙现象，并通过逐样本视觉敏感指数（VSI）量化，发现模糊问题相关区域后，40%-97%样本的下一词分布几乎不变。③该间隙是样本属性而非模型属性，VSI排名跨模型相关，且编码器-LLM间隙在每模型上超过0.65。④VSI在强模型的多选推理上具有高诊断效用（AUROC=0.85-0.87），但在弱模型上表现有限。
- **摘要（英）**: This paper identifies the Visual Insensitivity Gap, where VLMs fail to use visual evidence on 40%-97% of samples, quantified by a per-sample Visual Sensitivity Index (VSI). The gap is sample-specific and consistent across models, with a significant encoder-LLM gap, and VSI shows diagnostic utility in multi-choice reasoning tasks.
- **评估**: 该论文揭示了VLM评估中的关键盲点，对多模态感知系统的可靠性诊断有重要启示。
- **核心贡献**: 首次系统量化了VLM的视觉不敏感间隙，并提出了VSI诊断指标。
- **创新点**: 通过扰动视觉区域和线性探测，揭示了编码器-LLM间的信息传递断裂。
- **结果**: 发现VLM在大量样本上忽略视觉输入，VSI在特定任务上AUROC达0.85-0.87。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models are evaluated by aggregate accuracy on multimodal benchmarks, a practice that implicitly assumes the model uses its visual input. We show this assumption fails on 40%--97% of samples across six VLMs and three perceptual benchmarks: blurring the question-relevant visual region leaves the next-token distribution nearly unchanged. We name this phenomenon the Visual Insensitivity Gap and quantify it with a per-sample Visual Sensitivity Index (VSI). The gap is a property of samples, not of models: VSI ranks correlate across models (grand-mean Spearman rho=+0.40, permutation p<10^-3), so the same samples are flagged insensitive by VLMs sharing no architectural detail beyond a contrastively pretrained vision tower. The mechanism is concrete: on the insensitive samples, a linear probe on each model's own vision tower distinguishes perturbed from clean images at 0.72--0.79 accuracy, yet the model's argmax token changes on only 2%--11% of the same samples, an encoder--LLM gap above 0.65 on every model. Mapping VSI's diagnostic utility cell by cell surfaces a strong regime (multi-choice reasoning on capable VLMs: AUROC=0.85--0.87) and a weak regime (well-calibrated factuality, where softmax confidence already leads). VSI is not a universal best abstention signal; it is a sample-intrinsic indicator of vision-ignoring failure, best used as a conditional ensemble component.

</details>

### 5. Visual Attention Faithfulness in Vision-Language Models is Heterogeneous **⭐⭐⭐** (相关度: 65%, 质量: 0.75)

- **arXiv ID**: [2609.00830](https://arxiv.org/abs/2609.00830)  · [📄 PDF](https://arxiv.org/pdf/2609.00830)
- **作者**: Xurui Song, Weishi Wang, Zhongqi Yue et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对视觉语言模型中注意力权重是否忠实反映模型推理的问题，在NLP中已有研究，但在视觉模态中尚未探索。②通过因果扰动分析，评估了注意力排序视觉标记的完整性和充分性间隙，发现视觉注意力忠实性是异质的，表现为三种模式：忠实-充分、忠实-分布和非焦点。③人类标注的真实区域仅在约60%情况下满足完整性，与模型注意力排序存在系统性分歧。④在VQAv2和文档任务上验证了这些模式，表明视觉注意力忠实性受任务和模型影响。
- **摘要（英）**: This paper investigates visual attention faithfulness in VLMs through causal perturbation analysis, identifying three heterogeneous modes: Faithful-Sufficient, Faithful-Distributed, and Non-Focal. It reveals systematic divergence between model attention and human intuition, with human regions satisfying comprehensiveness in only ~60% of cases.
- **评估**: 该论文深化了对VLM注意力机制的理解，对可解释性和鲁棒性设计有参考价值。
- **核心贡献**: 首次系统分析了VLM中视觉注意力忠实性的异质性模式。
- **创新点**: 通过因果扰动和人类标注对比，揭示了注意力与推理的复杂关系。
- **结果**: 发现注意力忠实性因样本和任务而异，人类区域与模型注意力存在分歧。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Whether attention weights faithfully reflect model reasoning has been actively debated in NLP, yet this question remains largely unexplored for the visual modality in Vision-Language Models (VLMs). We address this gap through causal perturbation analysis on current VLMs, evaluating both the comprehensiveness and sufficiency gap of attention-ranked visual tokens. Our analysis reveals that visual attention faithfulness is heterogeneous, manifesting in three distinct processing modes: Faithful-Sufficient, where top-$k$ attention tokens are both necessary and sufficient for prediction; Faithful-Distributed, where they are necessary but broader visual context remains required; and Non-Focal, where no localized attention region is individually necessary while visual information remains an essential trigger for prediction. Furthermore, human-annotated ground-truth regions satisfy comprehensiveness in only $\sim 60$% of cases compared with model attention rankings, revealing systematic divergence between model visual reliance and human intuition. We demonstrate these patterns across both general VQA on VQAv2 and document tasks on VRDU and ChartQA, showing that visual attention faithfulness varies systematically with processing demands and model architectures rather than being uniformly faithful or unfaithful.

</details>

### 6. Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.00355](https://arxiv.org/abs/2609.00355)  · [📄 PDF](https://arxiv.org/pdf/2609.00355)
- **作者**: Jungseob Lee, Seongtae Hong, Dongyub Jude Lee et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/js-lee-AI/GLANCE](https://github.com/js-lee-AI/GLANCE)
- **提交日期**: 2026-08-31 · **分类**: cs.AI, cs.CL, cs.CV
- **摘要（中）**: ①针对视觉语言模型中投机解码的效率问题，现有起草器因自回归特性而必须保持小规模，导致视觉信息被压缩或忽略，在图像可预测文本时可靠性下降。②提出了GLANCE，首个一次性块起草器，对未修改的VLM目标无损，通过块扩散头读取目标已融合的视觉语言状态，一次前向填充整个块。③相比现有方法，视觉成本为零，深度不增加顺序步骤，宽候选树在一次目标验证中完成。④在相同引擎和预算下，GLANCE解码速度比自回归快2.93倍，且精确复现贪婪解码。
- **摘要（英）**: This paper introduces GLANCE, the first one-pass block drafter for lossless speculative decoding in VLMs, using a block-diffusion head to read fused vision-language states and fill blocks in one forward pass. It achieves up to 2.93x speedup over autoregression while exactly reproducing greedy decoding, overcoming the self-defeating cycle of small drafters.
- **评估**: 该论文解决了VLM推理效率的关键瓶颈，方法创新且实验充分，对实时感知系统有直接价值。
- **核心贡献**: 提出了GLANCE，首个无损块起草器，显著加速VLM解码。
- **创新点**: 利用块扩散头读取融合状态，消除视觉开销并实现并行块生成。
- **结果**: 解码速度提升至2.93倍，且保持输出无损。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Speculative decoding accelerates generation without changing its output, yet on vision-language models (VLMs) it has been caught in a self-defeating cycle. The drafter stays autoregressive, so it must stay small. A small drafter cannot afford the image at every step, so vision is compressed, pruned, or hidden. A drafter cut off from the image is then least reliable exactly where the image makes text predictable. We present GLANCE, the first one-pass block drafter that is lossless on an unmodified VLM target, and it breaks the cycle at both ends. A block-diffusion head reads the target's already-fused vision-language state, so vision costs the drafter nothing, and fills a whole block in one forward pass, so depth costs no sequential steps. A wide candidate tree is verified in one target pass, and every audited prompt reproduces greedy decoding exactly. Grounded workloads reward this most, entering a verbatim-copy regime whose long runs cost an autoregressive drafter a pass for every token and a block drafter one in total. Under one engine and one round budget, GLANCE decodes up to 2.93x faster than autoregression, from one draft pass a round where the production EAGLE3-VL head takes eight, and accepts 2.7x longer blocks than an EAGLE-3 head trained on the same corpus. One law organizes these results. Accepted length is set by the target's next-token entropy, with a fitted slope that steepens with grounding across all five tasks. The law transfers across targets and modalities and names its own boundary, since free-running text still favors a chain. Our code is available at https://github.com/js-lee-AI/GLANCE.

</details>

### 7. From Saliency to Discriminability: Rank-Preserving Visual Token Pruning for VLM Rerankers **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2609.00667](https://arxiv.org/abs/2609.00667)  · [📄 PDF](https://arxiv.org/pdf/2609.00667)
- **作者**: Siyi Liu, Hanjun Yang, Chenchen Zhang et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.IR, cs.CV
- **摘要（中）**: ①针对VLM重排序器处理多候选图像时视觉token过多、现有剪枝方法基于注意力显著性但与排序贡献不一致的问题。②提出RaDiCal框架，利用归一化注意力熵判断显著性何时可信，融合无注意力的排序判别先验，并选择剪枝层。③相比现有方法，首次系统诊断了显著性-排序贡献错位，并利用注意力熵作为可靠性指标。④在Flickr30K和MSCOCO上以20% token预算匹配或超越Dense MRR@10，在FashionIQ上排名第一，FLOPs降低39-45%。
- **摘要（英）**: This paper addresses the misalignment between attention saliency and ranking contribution in token pruning for VLM rerankers. It proposes RaDiCal, a training-free framework that uses normalized attention entropy to decide when saliency is trustworthy and fuses it with a rank-discriminative prior. RaDiCal matches or surpasses dense performance at 20% token budget on retrieval benchmarks and cuts FLOPs by 39-45%.
- **评估**: 该工作对token剪枝与排序任务的关系提供了新见解，方法简洁有效，对多模态检索系统部署有实际价值。
- **核心贡献**: 提出了基于注意力熵的排序判别性token剪枝框架RaDiCal。
- **创新点**: 首次利用归一化注意力熵诊断显著性-排序贡献错位并指导剪枝。
- **结果**: 在多个检索基准上以低token预算达到或超越密集性能，显著降低计算量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models used as listwise rerankers must jointly process visual tokens from tens of candidates per query, making token pruning essential for practical deployment. Existing pruning methods retain tokens by attention saliency, yet we show that saliency is systematically misaligned with ranking contribution: visually prominent tokens often capture order-neutral patterns shared across candidates. This mismatch is layer-dependent: saliency becomes informative only where attention is concentrated, and normalized attention entropy diagnoses the reliability shift (Pearson r=0.87). We propose RaDiCal (Rank-Discriminative Calibration), a training-free framework that uses normalized attention entropy to decide when saliency can be trusted, fusing it with an attention-free rank-discriminative prior and selecting pruning layers from the same trust landscape. Across three retrieval benchmarks and multiple VLM architectures, RaDiCal matches Dense MRR@10 on Flickr30K and surpasses it on MSCOCO at a 20% token budget, ranks first among all pruning methods on FashionIQ, and holds within 1.2 pp on Flickr30K and MSCOCO at 10% retention. It cuts FLOPs by 39--45% and delivers 1.28--1.45$\times$ measured speedups across two VLM architectures without dataset-specific retuning.

</details>

### 8. Beyond Language Priors: Diagnosing and Fixing Visual-Origin Hallucinations in Multimodal LLM **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.82)

- **arXiv ID**: [2609.00231](https://arxiv.org/abs/2609.00231)  · [📄 PDF](https://arxiv.org/pdf/2609.00231)
- **作者**: Peiyang Xu, Xiaopei Zhu, Jun Zhu et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/zxp555/ACFT_MM](https://github.com/zxp555/ACFT_MM)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对多模态大语言模型中的对象幻觉问题，现有研究主要归因于语言先验，忽略了视觉特征提取错误和图文对齐不当导致的视觉来源幻觉。②通过余弦相似度和Smooth Grad-CAM熵分析，证明幻觉样本具有更低的图文相似度和反转的注意力模式，并提出对抗对比微调（ACFT）方法。③ACFT通过对抗性幻觉属性翻转（AHAF）构造完美对齐的正负样本对进行对比微调。④该方法能有效减少幻觉，并同时作为诊断探针揭示幻觉的视觉根源。
- **摘要（英）**: This paper identifies visual-origin hallucination in MLLMs, caused by incorrect visual feature extraction and misalignment, distinct from language priors. It proposes Adversarial Contrastive Fine-Tuning (ACFT) with AHAF to construct aligned positive-negative pairs for contrastive learning. The method reduces hallucinations and serves as a diagnostic probe for visual causes.
- **评估**: 该研究挑战了主流观点，提供了视觉来源幻觉的定量证据，并提出了有效的微调策略，对多模态模型可靠性有重要意义。
- **核心贡献**: 揭示了视觉来源幻觉的机制并提出ACFT微调方法。
- **创新点**: 利用对抗性扰动翻转幻觉属性来构造对比学习样本。
- **结果**: 有效降低对象幻觉，并提供了新的诊断工具。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing research on object hallucination in multimodal large language models (MLLMs) predominantly attributes the problem to language priors such as over-reliance on textual co-occurrence statistics. We challenge this view by presenting quantitative evidence for a complementary, under-explored cause: visual-origin hallucination, where hallucinations arise from incorrect visual feature extraction and misalignment between image and text embeddings. Through cosine similarity analysis and Smooth Grad-CAM entropy measurements, we show that hallucinated samples exhibit systematically lower image-text similarity (average 0.158 vs. -0.122) and inverted attention patterns, where attention is dispersed when the target object is present but wrongly concentrated when it is absent. Guided by this diagnosis, we propose Adversarial Contrastive Fine-Tuning (ACFT). ACFT uses an Adversarial Hallucination Attribute Flipping (AHAF) procedure, involving minimal, targeted adversarial perturbations that flip an image's hallucination attribute, to construct perfectly aligned positive-negative pairs, which are then used for contrastive fine-tuning. AHAF simultaneously serves as a diagnostic probe, revealing that MLLM visual representations lie dangerously close to hallucination decision boundaries. Requiring only 0.9% of the COCO dataset and adding zero inference overhead, ACFT achieves state-of-the-art performance on POPE, MME, and four description-level hallucination benchmarks across LLaVA, MiniGPT-4, and Qwen2.5-VL. Code is available at https://github.com/zxp555/ACFT_MM

</details>

### 9. Separating perception from reasoning in vision-language models: a model-free render ceiling for crystal structures **⭐⭐⭐** (相关度: 60%, 质量: 0.75)

- **arXiv ID**: [2609.00663](https://arxiv.org/abs/2609.00663)  · [📄 PDF](https://arxiv.org/pdf/2609.00663)
- **作者**: Can Polat, Mustafa Kurban, Erchin Serpedin et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cond-mat.mtrl-sci, physics.chem-ph
- **摘要（中）**: ①针对多模态评估无法区分模型是误读图像还是错误推理的问题。②提出render ceiling，一种无模型参考基准，通过反转相机参数和重解跨视角对应关系来恢复图像支持的答案。③在2160个晶体结构上验证了ceiling的可靠性，并证明模型缺陷完全归因于模型自身。④实验显示，提供精确几何文本能提升所有模型，但监督视觉模型（0.8952）仍超过所有VLM，揭示了提取阶段的伪造问题。
- **摘要（英）**: This paper introduces the render ceiling, a model-free reference for separating perception from reasoning in VLM benchmarks. By inverting cameras and re-solving correspondences, it recovers the exact answer supported by images. Experiments show that even with exact geometry, VLMs underperform supervised vision models, exposing extraction-stage issues.
- **评估**: 该工作为多模态评估提供了新工具，有助于精确定位模型缺陷来源，但对自动驾驶领域直接相关性较低。
- **核心贡献**: 提出了render ceiling方法以分离感知与推理缺陷。
- **创新点**: 利用可逆渲染构建无模型基准参考。
- **结果**: 证明了VLM在视觉提取上的不足，并提供了基准构建规则。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal evaluations cannot say whether a vision-language model misread an image or misreasoned about it, because every existing method for separating the two places a second model in the loop. We introduce the render ceiling, a model-free reference for benchmarks built by rendering known objects: inverting the frozen cameras and re-solving cross-view correspondence recovers exactly the answer the images support. We prove the ceiling fails only through an enumerable set of projection coincidences and certify that set empty on 2,160 rendered crystal structures, so every point of a model's deficit belongs to the model. Across fourteen vision-language models, supplying exact geometry as text lifts every model yet closes under half the gap for thirteen, while a supervised vision model with no language component reads the same images at 0.8952, above every vision-language model. The instrument exposes extraction-stage fabrication that downstream accuracy would misattribute to reasoning, yields camera-placement rules for benchmark builders, and transfers to any benchmark with an invertible forward rendering.

</details>

### 10. Teaching Vision-Language Models to Use the Scale They Are Given: Label-Free Equivariance Training for Metric Physical Reasoning **⭐⭐⭐** (相关度: 70%, 质量: 0.78)

- **arXiv ID**: [2609.00658](https://arxiv.org/abs/2609.00658)  · [📄 PDF](https://arxiv.org/pdf/2609.00658)
- **作者**: Kaizhen Tan, Yang Feng, Heqing Du et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对VLM在度量物理推理中未能充分利用提供的尺度信息，预测对尺度变化响应不足的问题。②提出EquiSD，利用尺度等变性约束，在无度量标注下通过重缩放世界空间量来生成训练目标。③相比现有方法，无需额外标注，直接利用物理规律作为监督。④实验显示，该方法能改善模型对尺度变化的响应，但摘要中未提供具体数值。
- **摘要（英）**: This paper addresses the under-response of VLMs to scale changes in metric physical reasoning. It proposes EquiSD, which uses scale-equivariance constraints to generate training targets without metric annotations. The method improves scale grounding, though specific performance numbers are not detailed in the abstract.
- **评估**: 该工作提出了一种新颖的无标注训练策略，对视频物理推理有潜在价值，但效果数据不充分。
- **核心贡献**: 提出了基于尺度等变性的无标注训练方法EquiSD。
- **创新点**: 利用物理尺度变换作为自监督信号。
- **结果**: 改善了VLM的度量接地能力，但具体效果待验证。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Metric questions about video require vision-language models to use supplied real-world references to convert visual measurements into physical units. Yet we find that current models use this scale information only partially. When every world-space quantity in a prompt is rescaled by a common factor, the video remains equally valid and the correct answer changes by exactly that factor, but model predictions move only part of the way and accuracy remains concentrated near the familiar scale of the depicted objects. Across eight vision-language models, this under-response persists over four orders of magnitude. The same models recover the correct closed-form scaling laws when the identical physics is asked in a scale-free form, indicating that the main deficit lies in metric grounding rather than physical mechanism knowledge. We use this exact scaling relation as supervision without requiring metric annotations. Under a common rescaling of the supplied world-space quantities, the correct metric answer must change by the same factor. EquiSD exploits this constraint by projecting a model's own prediction onto the scale-equivariant family and fine-tuning the model on the resulting targets. It requires no ground-truth answers and only one model query per training video. On held-out simulated videos, EquiSD increases a 3B model's median response slope from 0.66 to 0.94 and improves mean relative accuracy by 9.2 points across scales. The learned relation generalizes to unseen world scales and transfers without adaptation to real QuantiPhy videos, where accuracy increases by 6.4 points. These results show that an exact physical symmetry can provide label-free supervision for improving metric grounding in vision-language models.

</details>

---

## Multimodal

### 1. Multimodal RGB-Infrared Combination for UAV-Based Wildfire Segmentation: A Comparative Study on FLAME3 **⭐⭐** (相关度: 50%, 质量: 0.65)

- **arXiv ID**: [2609.01390](https://arxiv.org/abs/2609.01390)  · [📄 PDF](https://arxiv.org/pdf/2609.01390)
- **作者**: Matheus F. Kovaleski, Luís Garrote, Cristiano Premebida et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对无人机野火分割中RGB和红外模态融合策略和架构影响不明确的问题。②在FLAME3数据集上比较RGB和红外基线，以及三种融合策略在U-Net、DeepLabV3+和SegFormer上的表现。③相比单一模态，该研究系统分析模态贡献、融合时机和架构差异。④发现热红外信息在分割中占主导，特征级融合结合Transformer架构最有前景。
- **摘要（英）**: This paper investigates RGB-infrared fusion for UAV-based wildfire segmentation on FLAME3, comparing baselines and fusion strategies across three architectures. It finds thermal information dominates and feature-level fusion with transformer architectures is most promising.
- **评估**: 该工作为多模态分割提供实证比较，但领域与自动驾驶相关性较低，方法创新有限。
- **核心贡献**: 系统比较了RGB-红外融合策略和架构对野火分割的影响。
- **创新点**: 分析模态贡献和融合时机在不同架构下的效果。
- **结果**: 热红外信息主导分割性能，特征级融合结合Transformer最优。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unmanned Aerial Vehicles (UAVs) have emerged as a promising platform for firefighting operations due to their flexibility, low operational cost, and ability to acquire high-resolution imagery in locations that may be difficult or dangerous to access using conventional methods. Recent advances in deep learning have significantly improved the capabilities of UAV-based wildfire monitoring systems. The present work investigates RGB-infrared fusion for binary wildfire segmentation on the FLAME3 dataset. In this Study, RGB and Infrared baselines are compared with three representative fusion strategies across three segmentation architectures, including U-Net, DeepLabV3+, and SegFormer. The key motivation of this work is to analyze the contribution of each modality, evaluate the impact of fusion timing, and examine how different network architectures exploit multimodal information for UAV wildfire delineation. The findings indicate that thermal information plays a dominant role in UAV segmentation and that feature-level multimodal fusion combined with transformer-based architectures offers the most promising direction for future research.

</details>

### 2. Differentially Private Paired Table-Image Multimodal Synthesis **⭐⭐⭐** (相关度: 40%, 质量: 0.72)

- **arXiv ID**: [2609.00708](https://arxiv.org/abs/2609.00708)  · [📄 PDF](https://arxiv.org/pdf/2609.00708)
- **作者**: Kai Chen, Josephine Lamp, Somesh Jha et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/KaiChen9909/TabImage_Syn](https://github.com/KaiChen9909/TabImage_Syn)
- **提交日期**: 2026-09-01 · **分类**: cs.CR, cs.AI, cs.CV
- **摘要（中）**: ①针对差分隐私下成对表格-图像数据合成中两种模态偏好不同学习机制且需保持依赖的挑战。②提出DP-TabImage框架，利用概率图模型生成表格分布，并用DP-SGD训练的表格条件扩散模型生成图像分布，通过私有原型预训练促进条件学习。③相比单独合成表格或图像的方法，该框架显式建模跨模态依赖，且原型预训练不增加隐私成本。④在三个真实数据集上，DP-TabImage在表格保真度、图像保真度和跨模态对齐间取得良好平衡。
- **摘要（英）**: This paper addresses differentially private synthesis of paired table-image data, proposing DP-TabImage with a private graphical model and a table-conditioned diffusion model. It achieves a strong balance among tabular fidelity, image fidelity, and cross-modal alignment on three datasets.
- **评估**: 该工作解决隐私保护下多模态数据合成的独特问题，方法设计合理，但领域相关性较低。
- **核心贡献**: 提出DP-TabImage框架，实现差分隐私下的成对表格-图像合成。
- **创新点**: 结合概率图模型和条件扩散模型，利用原型预训练降低隐私成本。
- **结果**: 在三个数据集上实现多模态保真度的平衡。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentially private (DP) synthesis has been extensively studied for tabular and image data separately, yet many real-world datasets contain images paired with multivariate tabular records. Synthesizing such data is particularly challenging under DP, as the two modalities favor different private learning mechanisms while their dependence must also be preserved. To address this challenge, we propose DP-TabImage, a modality-specialized framework for private paired synthesis. DP-TabImage instantiates the factorization $p(x,y)=p_T(y)p_I(x\;|\;y)$ using a private Probabilistic Graphical Model for the multivariate table distribution and a table-conditioned diffusion model trained with DP-SGD for the conditional image distribution. To facilitate conditional learning under clipped and noisy gradients, we further pretrain the model on private table-image prototypes, pairing privately constructed attribute-conditioned images with tabular vectors derived from the already private tabular model at no additional privacy cost. Experiments on three real-world datasets show that DP-TabImage achieves a strong balance among tabular fidelity, image fidelity, and cross-modal alignment. Our analysis further reveals that visual warm-up primarily improves marginal image fidelity, whereas aligned table-image warm-up is critical for improving cross-modal correspondence. Our source code is available in the GitHub repository, https://github.com/KaiChen9909/TabImage_Syn.

</details>

### 3. Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.00206](https://arxiv.org/abs/2609.00206)  · [📄 PDF](https://arxiv.org/pdf/2609.00206)
- **作者**: Ruotong Wang, Zihao Zhu, Siwei Lyu et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对多模态大模型在视频审核中忽略组合性安全盲区的问题。②定义分布式隐害（DIH），指视频中多个良性组件组合产生有害含义，并研究时间分布和跨模态两种情形。③开发多智能体合成框架生成9000多个视频，带推理标注，用于基准测试。④实验表明现有MLLM在DIH检测上存在显著缺陷，该数据集和框架促进安全对齐研究。
- **摘要（英）**: This paper identifies a compositional safety blind spot in MLLM-based video moderation, termed Distributed Implicit Harm (DIH), where benign components collectively convey harm. A multi-agent synthesis framework generates over 9,000 DIH videos with reasoning annotations, benchmarking reveals significant deficiencies in current MLLMs, highlighting the need for improved safety alignment.
- **评估**: 对多模态安全与视频理解有重要贡献，与自动驾驶中场景理解相关。
- **核心贡献**: 定义并系统研究多模态视频中的组合性安全盲区。
- **创新点**: 多智能体合成框架生成带推理标注的DIH视频数据集。
- **结果**: 揭示现有MLLM在DIH检测上的不足。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite their growing use in video moderation, multimodal large language models (MLLMs) exhibit a compositional safety blind spot: videos composed of seemingly benign components can convey harmful meaning when interpreted as a whole. We refer to this phenomenon as Distributed Implicit Harm (DIH), where harm arises from relations among components distributed along a decomposition axis of the video, rather than from any single explicit cue. Among many possible axes, we study two representative cases: temporally distributed harm across visual segments (DIH-T) and cross-modal harm between audio and visual streams (DIH-M). Studying and mitigating DIH at scale requires data that is difficult to collect: such videos lack compositional harm annotations, evade retrieval based on local visual cues, keywords, or single-modality signals, and are consequently absent from existing safety datasets. To bridge this gap, we develop a multi-agent synthesis framework that composes individually benign components into harmful scenarios and generates diverse DIH videos with explicit reasoning annotations, yielding a dataset of over 9,000 videos spanning visual-only and audio-visual settings. Benchmarking over 30 MLLMs spanning frontier proprietary models and leading open-source systems reveals substantial and consistent deficits in detecting both DIH-T and DIH-M. Notably, this failure persists even among the strongest frontier models: they often correctly assess individual components in isolation but fail to recognize the harmful meaning that emerges from their composition. We further evaluate these models on a manually collected set of real-world DIH videos from social media and observe the same failure mode, highlighting DIH as a practical and underexplored challenge for video moderation.

</details>

### 4. Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.01607](https://arxiv.org/abs/2609.01607)  · [📄 PDF](https://arxiv.org/pdf/2609.01607)
- **作者**: Penghao Wu, Haiwen Diao, Weichen Fan et al. (6 authors)
- **🏷️ 机构**: CUHK
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对统一多模态模型（UMMs）中视觉理解与生成功能虽统一但未必协同的问题，在表示、任务和系统三个层面进行受控研究。方法上，在无预训练视觉先验的架构中，通过任务解耦架构分离冲突的视觉计算并保留语义交互，避免目标间的不对称退化。相比已有工作，揭示了生成目标丰富理解特征、理解目标增强生成对齐的正向交互，但共享计算路径会导致一方主导。实验表明，端到端UMM在复杂任务上优于匹配的规划器-执行器流水线，验证了协同学习的优势。
- **摘要（英）**: This paper investigates whether unified multimodal models achieve learning synergy between visual understanding and generation, finding that generation enriches understanding features while understanding strengthens alignment, but shared computation paths cause asymmetric dominance. A task-decoupled architecture that separates conflicting visual computations while preserving semantic interaction mitigates this issue, and end-to-end UMMs outperform planner-executor pipelines on complex tasks.
- **评估**: 该研究系统性地剖析了多模态统一模型的内在协同机制，对设计高效的多模态架构具有重要指导意义。
- **核心贡献**: 揭示了统一多模态模型中理解与生成目标在表示、任务和系统层面的协同与竞争关系。
- **创新点**: 提出任务解耦架构以缓解共享计算路径导致的目标主导问题。
- **结果**: 端到端UMM在复杂任务上优于规划器-执行器流水线，验证了协同学习的优势。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretrained vision priors. At the representation level, we find that each objective provides useful signal to the other: generation enriches the visual features learned for understanding, while understanding strengthens vision--language alignment for generation. However, when both objectives are forced through the same computation path, one tends to dominate. A task-decoupled architecture that specializes conflicting visual computation while preserving semantic interaction avoids this asymmetric degradation. At the task level, through three case studies, we find positive bidirectional transfer when understanding and generation tasks rely on shared knowledge. At the system level, we show that an end-to-end UMM outperforms a matched planner--executor pipeline on complex tasks that explicitly require both image understanding and generation. Together, these results show that the value of UMMs extends beyond a unified interface: appropriate specialization, shared task knowledge, and end-to-end optimization can turn coexistence into synergy.

</details>

### 5. MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2609.01316](https://arxiv.org/abs/2609.01316)  · [📄 PDF](https://arxiv.org/pdf/2609.01316)
- **作者**: Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.IR, cs.AI, cs.CL
- **摘要（中）**: 这篇论文针对视觉丰富文档检索中OCR线性化导致表格、图表等关键内容丢失的问题，提出MIDR框架，在索引阶段利用多模态大模型将页面转换为验证过的文本字段，并用BM25F索引，可选与稠密检索融合。相比ColPali等基于补丁的视觉检索器，MIDR将多模态推理移至索引时间，实现文本为中心的检索。在ViDoRe V3上，MIDR Hybrid平均nDCG达0.6219，相对BM25提升23%，在法语文档域中显著提升跨语言检索性能，且索引内存小约9倍。
- **摘要（英）**: This paper addresses the representation problem in visually rich document retrieval, where OCR linearization corrupts or omits content in tables and charts. MIDR shifts multimodal reasoning to index time by using a multimodal LLM to generate verified textual fields indexed with BM25F, achieving 0.6219 average nDCG on ViDoRe V3, a 23% relative gain over BM25, while using 9x smaller index memory than ColQwen2.5.
- **评估**: 该工作为文档检索提供了一种高效的训练无关方案，在跨语言和资源效率上具有实际价值。
- **核心贡献**: 提出MIDR框架，通过索引时多模态增强实现高效且跨语言的文档检索。
- **创新点**: 利用多模态LLM在索引阶段生成验证文本，避免查询时视觉推理开销。
- **结果**: 在ViDoRe V3上平均nDCG达0.6219，相对BM25提升23%，并优于ColQwen2.5在多数域上的表现。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Retrieval over visually rich documents has a representation problem: important content often lives in tables, charts, figures, and layout relations that plain OCR linearizes, corrupts, or omits. ColPali-family visual retrievers address this with patch-level multi-vector indexes and late-interaction scoring, keeping image-derived retrieval on the query-time serving path. We introduce MIDR (Multimodal Indexing for Document Retrieval), a training-free framework for enrichment-augmented indexing that shifts multimodal reasoning to index time. During ingestion, a multimodal LLM converts rendered pages into verified textual fields that are indexed with BM25F and optionally fused with dense retrieval, enabling text-centric serving over multimodally grounded evidence. On ViDoRe V3, MIDR Hybrid achieves 0.6219 average nDCG across five English domains, a 23.0% relative gain over BM25, remaining competitive with ColQwen2.5. On two French-document domains, enrichment bridges English queries and French page text, lifting BM25 from 0.1532 to 0.5448 nDCG and outperforming ColQwen2.5. Across all seven domains, MIDR leads ColQwen2.5 on four while using approximately 9x smaller index memory and approximately 2x lower query latency. These results establish index-time multimodal reasoning as a compelling accuracy-deployment alternative to serving-time visual late interaction.

</details>

### 6. TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.01277](https://arxiv.org/abs/2609.01277)  · [📄 PDF](https://arxiv.org/pdf/2609.01277)
- **作者**: Chao Zhou, Yiling Chen, Qi Chu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI, cs.MM
- **摘要（中）**: 这篇论文针对预训练联合音视频扩散模型缺乏对语音发生时间显式控制的问题，提出推理时语音调度任务，在无需微调的情况下将语音和视觉发音放置在用户指定的起止区间。方法上，利用去噪过程中时序敏感的文本到音频交叉注意力头定位源跨度，并通过区域感知潜在重映射转移内容。相比已有工作，TimeSteer无需训练即可实现时间编辑，并引入SpeechShift基准。实验表明，该方法能有效调度语音，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the lack of explicit temporal control in joint audio-visual diffusion models by introducing inference-time speech scheduling, which places coupled speech and visual articulation within user-specified intervals without finetuning. TimeSteer leverages timing-sensitive cross-attention heads for source span localization and region-aware latent remapping for content transfer, introducing the SpeechShift benchmark for evaluation.
- **评估**: 该工作探索了生成模型中的新任务，具有创新性，但应用领域与自动驾驶感知相关性较低。
- **核心贡献**: 提出推理时语音调度任务及训练无关的TimeSteer框架。
- **创新点**: 利用去噪过程的固有属性实现无需微调的时间编辑。
- **结果**: 在SpeechShift基准上验证了有效性，但具体性能数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although pretrained joint audio-visual diffusion models offer rich control over \emph{what} to generate, they provide no explicit control over \emph{when} an utterance should occur. To address this, we study \emph{inference-time speech scheduling}, a novel task that places coupled speech and visual articulation within user-specified begin--end intervals without finetuning the backbone model. We uncover two intrinsic properties of the denoising process that enable this task. First, a timing-sensitive text-to-audio cross-attention head exposes each utterance's model-implied source span along the latent timeline. Second, the predicted clean latent already organizes coupled speech and visual articulation, allowing their temporal placement to be edited without regenerating the content. Building on these discoveries, we propose \textbf{TimeSteer}, a training-free framework that localizes each utterance's source span through \textbf{Source Span Localization} and transfers the associated audio-visual latent content from the source interval to the specified target interval through \textbf{Region-Aware Latent Remapping}. We further introduce \textbf{SpeechShift}, the first benchmark for interval-level speech scheduling in joint audio-visual generation. Experiments across two representative backbones show that TimeSteer substantially improves interval controllability over training-free baselines while maintaining competitive overall generation quality.

</details>

### 7. ViTAL-X: Video-Text Alignment with Cross-Modal Temporal Edits **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.85)

- **arXiv ID**: [2609.00505](https://arxiv.org/abs/2609.00505)  · [📄 PDF](https://arxiv.org/pdf/2609.00505)
- **作者**: Sethuraman T, Savya Khosla, Onkar Kishor Susladkar et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对视频-文本模型（如CLIP）的时间盲区问题，即无法感知顺序、方向和运动动态，提出XTE-Bench诊断基准，揭示大规模模型仍存在此缺陷。方法上，提出跨模态时间编辑（XTE）自监督框架，通过同步视频-文本变换生成硬负样本，无需人工标注。ViTAL-X实例化该框架，仅用0.4B参数和1M训练片段，在六个时间基准上达到最先进性能，超越7B参数模型和基于600倍数据训练的基线。
- **摘要（英）**: This paper addresses temporal blindness in video-text models by introducing XTE-Bench, a diagnostic probe showing that even large-scale models struggle with temporal reasoning. The proposed Cross-Modal Temporal Edits (XTE) framework generates hard temporal negatives via synchronized video-text transformations, and ViTAL-X achieves state-of-the-art performance on six temporal benchmarks with only 0.4B parameters and 1M clips, outperforming 7B-parameter models.
- **评估**: 该工作有效解决了视频理解中的关键时间推理缺陷，方法轻量且高效，对多模态感知有借鉴意义。
- **核心贡献**: 提出XTE自监督框架和ViTAL-X模型，显著提升视频-文本模型的时间感知能力。
- **创新点**: 通过同步变换生成硬负样本，无需标注即可注入精确时间监督。
- **结果**: ViTAL-X在六个时间基准上达到SOTA，超越7B参数模型和600倍数据训练的基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video-text models adapted from image-text architectures (e.g., CLIP) frequently exhibit temporal blindness, the inability to perceive fundamental cues like order, direction, and motion dynamics. Standard datasets mask this limitation by enabling models to exploit static spatial shortcuts. To systematically evaluate this, we introduce XTE-Bench, a diagnostic probe revealing that even large-scale video-language models struggle with basic temporal reasoning, indicating that parameter scaling alone is insufficient to resolve this flaw. To address this, we propose Cross-Modal Temporal Edits (XTE), a self-supervised framework that injects precise temporal supervision. By performing synchronized video-text transformations, XTE generates hard temporal negatives without manual annotation. We instantiate this with ViTAL-X, a lightweight model that equips frozen image-text backbones with temporal awareness while preserving their foundational spatial knowledge. Across six temporal benchmarks, ViTAL-X achieves state-of-the-art performance. Utilizing only 0.4B parameters and 1M training clips, ViTAL-X outperforms 7B-parameter models and surpasses baselines trained on 600x more data. These results demonstrate that targeted, high-quality temporal alignment provides a highly efficient alternative to pure scaling.

</details>

### 8. SlideMix: Enhancing Whole Slide Image Analysis via Multimodal Shuffling **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2609.00396](https://arxiv.org/abs/2609.00396)  · [📄 PDF](https://arxiv.org/pdf/2609.00396)
- **作者**: Chad Wong, Sicheng Chen, Tianyi Zhang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Xia-Research-Lab/SlideMix](https://github.com/Xia-Research-Lab/SlideMix)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对全切片图像（WSI）分析中组织异质性、弱监督和多尺度证据等挑战，提出SlideMix，一种基于多模态洗牌的模型无关增强框架。方法上，使用检索增强VLM选择诊断相关区域，进行原位瓦片洗牌以混合特征，并通过VLM软标签和课程学习机制控制洗牌粒度。相比已有MIL增强方法，SlideMix保留诊断相关性和跨尺度结构。摘要未提供具体性能数据，但声称在多个数据集上有效。
- **摘要（英）**: This paper addresses challenges in whole slide image analysis, such as tissue heterogeneity and weak supervision, by proposing SlideMix, a model-agnostic multimodal augmentation framework. It uses a retrieval-augmented VLM for region selection, in-place tile shuffling for feature mixing, and curriculum learning for adaptive control, but no specific performance metrics are provided in the abstract.
- **评估**: 该工作针对医学图像分析提出创新增强方法，但与自动驾驶感知领域相关性较低。
- **核心贡献**: 提出SlideMix框架，通过多模态洗牌增强MIL-based WSI分析。
- **创新点**: 结合VLM区域选择和课程学习实现诊断相关的增强。
- **结果**: 摘要未提供具体数据，声称在多个数据集上有效。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Histopathological whole slide images (WSIs) are central to cancer diagnosis, but their gigapixel scale, tissue heterogeneity, weak slide-level supervision, sparse diagnostic regions, and multi-scale evidence make robust automated analysis challenging. Multiple instance learning (MIL) is widely used to aggregate tile-level features into slide-level predictions, yet existing augmentation strategies often perturb tissue regions without preserving diagnostic relevance, slide context, or cross-scale structure. We propose SlideMix, a model-agnostic multimodal augmentation framework for MIL-based WSI analysis. SlideMix uses a retrieval-augmented vision-language model (VLM)-based Visual-Language Adaptive Region selector to identify diagnostically relevant regions and reduce weak-label noise. It then performs In-place Tile Shuffling within meaningful tissue regions to mix feature embeddings while preserving slide-level context. A VLM-based soft-labeling module supervises mixed samples, while a multi-factor, loss-driven online Curriculum-Learning Feedback scheme adaptively controls shuffle granularity, feature similarity, and shuffle ratio to promote cross-scale representation learning. Across 11 WSI datasets comprising 20,523 slides, 8 diagnostic tasks, and 10 WSI backbones, SlideMix improves accuracy and generalization in most settings and compares favorably with established augmentation baselines, providing a simple plug-and-play approach for more robust and scalable digital pathology models. Source code: https://github.com/Xia-Research-Lab/SlideMix

</details>

### 9. CrossFeat: Bridging Imaging Modalities in Feature Descriptor Space **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.00272](https://arxiv.org/abs/2609.00272)  · [📄 PDF](https://arxiv.org/pdf/2609.00272)
- **作者**: Paul Schneider, Nazim Haouchine
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对跨模态图像匹配中，现有描述子需针对每对模态重新训练或使用大模型导致计算开销大的问题。②提出CrossFeat框架，学习一个跨模态映射函数，将现有单模态描述子的特征映射到另一模态的兼容表示，并引入几何-外观解耦以保持结构信息。③相比逐对训练或大模型方法，CrossFeat无需重新训练即可适配新模态，且保持原始描述子的几何属性。④在多个跨域数据集上实验，多模态匹配性能显著提升。
- **摘要（英）**: This paper addresses the high cost of retraining descriptors for each modality pair in cross-modal matching. CrossFeat learns a crossing function in descriptor space to map features across modalities while preserving geometric properties via geometry-appearance disentanglement. It improves multimodal matching performance across multiple domains without per-pair retraining.
- **评估**: 该工作为跨模态描述子提供了一种轻量级通用方案，对多模态感知任务有参考价值，但实验规模有限。
- **核心贡献**: 提出一种无需重新训练的跨模态描述子适配框架。
- **创新点**: 在描述子空间学习跨模态映射并解耦几何与外观。
- **结果**: 在多个跨域数据集上提升了多模态匹配性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most advances in keypoint descriptions address monomodal settings, where image variations arise from viewpoint, illumination, or contrast changes. Multimodal scenarios involve images produced by fundamentally different sensing processes, such as multispectral imaging, RGB-depth, satellite imagery, or medical imaging, causing the same structures to appear differently. A common solution to cross-modal description is to train descriptors for each modality pair, which requires retraining whenever the modalities change, or to train large models, which incur a significant increase in runtime. Instead, we propose CrossFeat, a framework that enables an existing monomodal descriptor to operate across modalities. Our method learns a crossing function in descriptor space that maps features from one modality to a representation compatible with another. To preserve the structural information captured by the original descriptor, CrossFeat introduces a geometry-appearance disentanglement such that only appearance is altered while the geometric properties are preserved. Experiments across multiple domains and datasets demonstrate improved performance in multimodal matching.

</details>

### 10. ExBind: A Controlled Diagnostic Benchmark for Visual-to-Executable Correspondence **⭐⭐⭐** (相关度: 45%, 质量: 0.7)

- **arXiv ID**: [2609.01344](https://arxiv.org/abs/2609.01344)  · [📄 PDF](https://arxiv.org/pdf/2609.01344)
- **作者**: Ziqian Wang, Yuxiao Cheng, Tingxiong Xiao et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Daerwang2020/Exbind](https://github.com/Daerwang2020/Exbind)
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对多模态编码与编辑系统中，视觉或语义指代到可执行对象的精确映射问题。②构建了ExBind诊断基准，隔离视觉到可执行对应层，包含SVG、DOM、canvas等案例，并评估模型输出严格引用。③相比现有基准，ExBind提供受控的潜在绑定实例和确定性映射，无需推理轨迹。④Qwen3-VL-4B达到100%有效性和98.8%精确准确率，而Qwen2.5-VL-3B在表格套件中表现出系统性错误。
- **摘要（英）**: This paper introduces ExBind, a controlled diagnostic benchmark for visual-to-executable correspondence, isolating the binding layer with deterministic mappings. It reveals performance gaps in VLMs, with Qwen3-VL-4B achieving near-perfect accuracy.
- **评估**: 该基准对多模态系统评估有价值，但主题与自动驾驶感知核心领域相距较远。
- **核心贡献**: 提出了ExBind基准，用于诊断视觉到可执行对应关系。
- **创新点**: 设计了表示无关的潜在绑定实例和严格评估协议。
- **结果**: 揭示了不同VLM在精确映射上的显著性能差异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal coding and editing systems must map a visible or semantic referent to the exact executable object that can be edited. A wrong reference may select a valid but incorrect DOM node, SVG element, graph endpoint, hierarchy member, or table cell, while final execution success alone does not reveal the source of the failure. ExBind isolates this visual-to-executable correspondence layer as a controlled diagnostic benchmark between semantic localization and action execution. It samples representation-independent latent binding instances and compiles them into SVG, DOM, canvas, tree, graph, and table cases with deterministic mappings to executable references. Models output only a strict reference; the evaluator maps predictions back to latent structure and scores structural constraints without requiring reasoning traces. The release contains a 250-case broad suite, a disjoint 240-case targeted suite, and 50 paired latent groups. Qwen2.5-VL-3B achieves 98.4% candidate validity but 76.4% exact accuracy, while Qwen3-VL-4B achieves 100.0% validity and 98.8% exact accuracy. In the targeted table suite, all Qwen2.5-VL-3B residual errors are valid correct-row/wrong-column selections. Candidate-order perturbations change case-level outcomes while preserving this error pattern. ExBind is designed for controlled diagnosis rather than population-scale ranking or end-to-end editing evaluation. Code and benchmark records are available at https://github.com/Daerwang2020/Exbind and https://huggingface.co/datasets/Ziqianwwww/ExBind.

</details>

---

## Vision Transformer

### 1. ViTAMINS: An Empirical Study of Training Self-Supervised Vision Transformers with Synthetic Hard Negatives **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.86)

- **arXiv ID**: [2609.01041](https://arxiv.org/abs/2609.01041)  · [📄 PDF](https://arxiv.org/pdf/2609.01041)
- **作者**: Nikos Giakoumoglou, Andreas Floros, Kleanthis-Marios Papadopoulos et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI, cs.LG
- **摘要（中）**: ①针对自监督视觉Transformer预训练中负样本质量不足的问题。②提出ViTAMINS，将合成硬负样本集成到无监督对比预训练中。③相比现有方法，ViTAMINS通过简单修改对比框架即可提升表示质量，并产生涌现属性，如语义分类能力（+11.3%）。④在ImageNet和多个下游任务上超越竞争方法，且资源效率更高，ViT-B超越V-JEPA的ViT-L。
- **摘要（英）**: This paper addresses the lack of hard negatives in self-supervised ViT pretraining. It proposes ViTAMINS, which integrates synthetic hard negatives into contrastive learning. The method improves representation quality, yields emergent semantic classification abilities (+11.3%), and outperforms competing methods with better resource efficiency.
- **评估**: 该工作展示了合成硬负样本在自监督学习中的潜力，实验全面，对视觉表示学习有重要贡献。
- **核心贡献**: 提出了集成合成硬负样本的自监督ViT训练方法ViTAMINS。
- **创新点**: 利用合成硬负样本激发表示中的语义信息。
- **结果**: 在多个基准上超越现有方法，并显著提升分类性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce ViTAMINS, a method that integrates synthetic hard negatives into unsupervised vision transformer pretraining to improve representation quality. Our approach is thoroughly benchmarked on ImageNet and transfer learning, image retrieval, copy detection, and image, video segmentation tasks. Notably, our proposed negatives give rise to emergent properties, where learned representations contain explicit information about the semantic content of an image and serve as excellent classifiers (up to +11.3% over baselines). ViTAMINS achieves these benefits through simple modifications to existing contrastive frameworks and outperforms competing methods while being more resource efficient, e.g., our ViT-B surpasses V-JEPA with ViT-L. Our findings motivate reconsidering contrastive learning as a simpler yet powerful alternative to dominant generative and self-distillation approaches.

</details>

### 2. Semantic-Guided Multimodal Preprocessing for Vision Transformer-Based Clear Cell Renal Cell Carcinoma Grading **⭐⭐** (相关度: 10%, 质量: 0.6)

- **arXiv ID**: [2609.01426](https://arxiv.org/abs/2609.01426)  · [📄 PDF](https://arxiv.org/pdf/2609.01426)
- **作者**: Fatemeh Javadian, Zhu Chen, Zahra Aminparast et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI, cs.LG
- **摘要（中）**: ①针对透明细胞肾细胞癌分级中现有方法未将细胞核分类与最终肿瘤分级关联的问题。②提出语义引导的多模态预处理方法，将预训练模型的细胞核分类图与RGB病理图像结合，通过通道拼接和乘法调制输入ViT。③相比仅用RGB或最大投票聚合，利用核分级信息同时保留纹理特征。④平衡准确率达0.916，优于RGB基线0.707和最大投票0.427，且在扰动下仍保持21个百分点的提升。
- **摘要（英）**: This paper addresses clear cell renal cell carcinoma grading by integrating nuclei classification maps with RGB histopathology images for ViT-based grading. The proposed semantic-guided preprocessing uses channel concatenation and multiplicative modulation, achieving 0.916 balanced accuracy, outperforming RGB-only baseline (0.707) and max-voting (0.427). The method shows robustness under perturbation, maintaining a 21-point improvement.
- **评估**: 医学影像领域应用，与自动驾驶感知方向相关性极低，但方法有一定通用性。
- **核心贡献**: 提出语义引导的多模态预处理策略，提升ViT在病理分级中的性能。
- **创新点**: 将核分类语义图与RGB特征融合，通过调制机制增强ViT表征。
- **结果**: 平衡准确率提升至0.916，显著优于基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Clear cell renal cell carcinoma (CCRCC) grading is essential for treatment planning, yet existing approaches either analyze patch-level images directly or focus solely on nuclei-level classification, without linking to final tumor grading. We propose a semantic-guided multimodal preprocessing method that integrates nuclei classification maps from existing pre-trained models with RGB histopathology images for Vision Transformer (ViT)-based CCRCC grading. Our approach employs classification map channel concatenation and multiplicative modulation, with optimized overlays to leverage nuclei grading information, while preserving RGB textural features. Evaluation of multiple preprocessing strategies demonstrates that semantic-guided enhancement achieves 0.916 balanced accuracy, outperforming RGB-only baseline (0.707) and max-voting aggregation from prior studies (0.427). Sensitivity analysis reveals that this 21 percentage point improvement over baseline persists even under simulated perturbation at rates matching current state-of-the-art nuclei classification model error thresholds, suggesting both effective semantic utilization and practical robustness. These findings show that preprocessing-based multimodal fusion can leverage the diagnostic potential of existing imperfect nuclei classifiers, effectively bridging previously isolated fine-grained nuclear-level analysis with coarse-grained ViT-based patch classification. Per-class recall was consistent across grades (0.93, 0.91, 0.91), indicating that gains are not concentrated in the majority class. Because the sensitivity analysis perturbs ground-truth maps rather than predictions from an actual nuclei model, this result characterizes robustness under simulated error rather than deployment with a real upstream model, which remains for future work.

</details>

### 3. HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.01282](https://arxiv.org/abs/2609.01282)  · [📄 PDF](https://arxiv.org/pdf/2609.01282)
- **作者**: Sathiyamohan Nishankar, Pubudu Sanjeewani, Asanka Perera et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对ViT架构多样性导致现有归因方法（如Grad-CAM、attention rollout、LRP）无法统一适用的问题。②提出HiLRP框架，将ViT中的注意力和分辨率降低算子分解为四种操作类型，每种操作定义满足守恒的相关性规则。③相比现有方法，HiLRP无需架构特定推导即可支持新骨干，且归因图分解预测而非依赖启发式假设。④实验表明该方法在多种ViT变体上提供守恒有效的解释，提升可解释性。
- **摘要（英）**: This paper addresses the lack of unified attribution methods across diverse ViT architectures by decomposing attention and resolution-reduction operators into four operation types with conservation-valid relevance rules. HiLRP supports new backbones by construction, avoiding architecture-specific derivation, and produces attribution maps that decompose predictions. The method demonstrates effectiveness across various ViT variants.
- **评估**: 对ViT可解释性有重要贡献，可迁移至自动驾驶感知模型解释，但非直接应用。
- **核心贡献**: 提出统一的守恒归因框架HiLRP，适用于多种ViT架构。
- **创新点**: 基于操作类型分解的通用相关性规则，实现架构无关的归因。
- **结果**: 在多种ViT变体上提供守恒有效的解释。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformer (ViT) design has become increasingly diverse, with backbones combining convolutional stems, windowed, linear, or multi-axis attention, patch merging, and spatial reduction in various configurations. This diversity poses challenges for existing attribution methods, whose assumptions often do not hold across ViT variants: Grad-CAM requires a terminal spatial feature map, attention rollout assumes global softmax attention, and layer-wise relevance propagation (LRP) requires module-specific rules. To the best of our knowledge, no existing method provides a unified attribution framework across this architectural space. We show that this architectural diversity can be captured by a simpler underlying structure. The attention and resolution-reduction operators in current ViTs can be decomposed into four operation types: linear maps, bilinear mixing, normalization or gating, and reindexing. Each operation admits a relevance rule that satisfies conservation. Based on these rules, HiLRP supports new backbones by construction rather than by architecture-specific derivation, and its attribution maps decompose the prediction rather than relying on heuristic assumptions. We prove conservation and conditional equivariance and verify both to machine precision. Across 14 attribution methods and 10 architectures, we find that no prior method remains reliable across ViT families, while Faithfulness Correlation becomes uninformative for backbones robust to spatial masking. HiLRP alone preserves conservation across windowed, spatial-reduction, multi-axis, and linear-attention models, where naive extensions can produce zero or inflated relevance. It also localizes attribution failures in class activation mapping, achieving 0.97 Pointing compared with 0.55 for competing methods on EfficientViT.

</details>

### 4. Where Should Experience Live? Hierarchical Hebbian Memory for Continual Vision Transformers **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.75)

- **arXiv ID**: [2609.00358](https://arxiv.org/abs/2609.00358)  · [📄 PDF](https://arxiv.org/pdf/2609.00358)
- **作者**: Mohammed Yusuf Mujawar, Noorbakhsh Amiri Golilarz
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.NE
- **摘要（中）**: ①针对ViT在持续学习场景中难以组织新信息的问题。②提出层次Hebbian记忆架构，包含工作记忆、路由情景记忆和语义记忆三级，由学习控制器调节读写和巩固。③相比单一记忆库，多库检索和因果读写生命周期提升持续学习性能。④在Omniglot上达97.39%准确率，CORe50上95.37%，延迟关联准确率47.50%优于基线24.17%。
- **摘要（英）**: This paper addresses the limitation of ViTs in organizing new information during continual learning by proposing a Hierarchical Hebbian Memory with three levels: working, episodic, and semantic memory. A learned controller regulates routing and consolidation, achieving 97.39% on Omniglot and 95.37% on CORe50, with improved delayed-association accuracy.
- **评估**: 持续学习与记忆机制设计新颖，对自动驾驶在线适应有参考价值。
- **核心贡献**: 提出层次Hebbian记忆架构，增强ViT的持续学习能力。
- **创新点**: 三级记忆与因果读写生命周期结合，实现多时间尺度信息组织。
- **结果**: 在多个基准上显著提升持续学习准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers provide strong visual representations but typically rely on slowly updated parameters, limiting their ability to organize newly acquired information across different memory timescales. This work proposes \textit{Hierarchical Hebbian Memory}, a three-level memory architecture composed of rapid Working Memory, persistent Routed Episodic Memory, and slower Semantic Memory. A learned controller regulates memory contribution, read and write routing, plasticity, retention, and consolidation. A causal read-before-write lifecycle ensures that the current outcome cannot influence the prediction it supervises. The architecture is evaluated on Omniglot 5-way 1-shot recognition and CORe50 continual object recognition. With Swin-Tiny, the hierarchical model reaches 97.39\% accuracy on Omniglot and 95.37\% final accuracy on CORe50 when combined with experience replay. Learned multi-bank retrieval reaches 47.50\% delayed-association accuracy, compared with 24.17\% for a single persistent bank and 25.00\% without memory. After intervening distractors, Episodic Memory retains approximately 0.96 cosine similarity with stored associations, while Working Memory falls to approximately 0.05. These results show that Hebbian association and learned memory routing can jointly organize online visual experience across rapid, persistent, and consolidated memory timescales within Vision Transformers.

</details>

### 5. A Benchmark for Vehicle Attribute Classification in Cross-Domain Surveillance Scenarios **⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.01584](https://arxiv.org/abs/2609.01584)  · [📄 PDF](https://arxiv.org/pdf/2609.01584)
- **作者**: Sergio M. Silva, Otavio T. Remer, Gabriel E. Lima et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/UFPR-IPASP-PR/uvib-vehicle-attributes](https://github.com/UFPR-IPASP-PR/uvib-vehicle-attributes)
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对车辆属性分析模型在真实监控场景中因视角、遮挡、光照等变化导致的性能退化问题。②引入了UVIB基准，包含84,835张来自七个巴西公开数据集的车辆图像，统一标注了前/后朝向、遮挡相关VMMR适用性和颜色清晰度。③评估了四种代表性架构在混合域、跨域和跨数据集协议下的表现。④结果表明域偏移对性能的影响大于架构选择，尤其在跨域设置中VMMR适用性显著下降。
- **摘要（英）**: This paper introduces UVIB, a benchmark for vehicle attribute classification across domains, with unified annotations and multi-protocol evaluation. Results show domain shift impacts performance more than architecture choice, highlighting cross-domain challenges.
- **评估**: 该基准对智能交通和自动驾驶中的车辆感知有参考价值，但更偏向监控场景。
- **核心贡献**: 提出了UVIB基准，用于跨域车辆属性分类评估。
- **创新点**: 统一了多源数据集的属性标注并设计了跨域评估协议。
- **结果**: 揭示了域偏移对车辆属性分析的显著影响。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vehicle attribute analysis is a key component of Intelligent Transportation Systems (ITS), supporting applications such as vehicle identification, traffic monitoring, and forensic investigation. However, models trained under controlled conditions often degrade in real surveillance scenarios due to changes in viewpoint, occlusion, illumination, and sensor characteristics. This paper introduces Unconstrained Vehicle Identification Benchmark (UVIB), a benchmark for evaluating three operational vehicle-analysis tasks: front/rear orientation, occlusion-related suitability for Vehicle Make and Model Recognition (VMMR), and color clarity. The benchmark contains 84,835 vehicle images from seven public Brazilian datasets, grouped into surveillance and general acquisition domains, with unified binary annotations that were not jointly available in the original sources. Four representative architectures, EfficientNetV2-S, ResNet-50, ViT/B-16, and YOLO11s-cls, are evaluated under mixed-domain, cross-domain, and cross-dataset protocols. The results show that domain shift has a stronger impact than architecture choice, with substantial degradation in cross-domain settings, especially for VMMR suitability and color clarity. While orientation generalizes more reliably, VMMR suitability remains affected by class imbalance and ambiguous occlusions, and color clarity is highly sensitive to illumination and sensor modality. These findings highlight the need for benchmarks and evaluation protocols that explicitly measure operational robustness beyond standard in-domain accuracy. The proposed benchmark is publicly available at https://github.com/UFPR-IPASP-PR/uvib-vehicle-attributes/.

</details>

### 6. Can Scene Text Recognition Read Rare Compositions? **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.85)

- **arXiv ID**: [2609.00816](https://arxiv.org/abs/2609.00816)  · [📄 PDF](https://arxiv.org/pdf/2609.00816)
- **作者**: Genpei Zhang
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对场景文本识别在标准基准上看似饱和，但在稀有词和字符n-gram组合上性能显著下降的问题。②通过联合分层测试图像，发现稀有词×稀有三元组角落的准确率比中心低10-18个百分点，并跨四种书写系统验证。③通过多种探针定位失败源于自回归解码器的词汇先验，而非容量瓶颈。④测试了16种非架构缓解方法，部分能恢复差距，但问题仍存在。
- **摘要（英）**: This paper reveals that scene text recognition performance drops significantly on rare word and n-gram compositions, despite high aggregate accuracy. It localizes the failure to the autoregressive decoder's lexical prior and evaluates mitigations.
- **评估**: 该论文对视觉识别模型的鲁棒性分析深入，对自动驾驶中的文本理解有间接启示。
- **核心贡献**: 揭示了场景文本识别在稀有组合上的系统性失败。
- **创新点**: 通过分层和探针方法定位失败根源。
- **结果**: 证明了性能下降非容量问题，而是词汇先验导致。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene text recognition is reported as 89--97% accurate on the six standard benchmarks, and the problem is widely treated as saturated. We present an alternative reading. When the same test images are stratified jointly by ground-truth word rarity and character n-gram novelty against a reference corpus, accuracy at the rare-word x rare-trigram corner of the resulting 5x5 grid drops 10--18 pt below the q3/q3 centre across nine English specialised recognisers, and the same direction (corner below centre) holds on all 13 of 13 (language, model) pairs we test across four writing systems (Latin, Han, Han+kana, Arabic). The drop is not a capacity bottleneck. A 6x vision-backbone scale-up (CLIP4STR-Base 158M -> CLIP4STR-Huge 1.0B, OpenCLIP ViT-H/14 LAION-2B) leads every benchmark in aggregate accuracy yet leaves the stress corner unchanged (86.9 -> 86.5, within paired-bootstrap noise). Four converging probes--layer-wise probing, confidence-when-wrong, attention re-balancing, and a cross-script commit-vs-abstain error split--localise the failure to the autoregressive decoder's lexical prior. We then ask how much of the gap existing techniques recover. Of 16 non-architectural mitigations, the largest mean q5/q5 gain is +1.3 pt and none clears the paired-bootstrap noise floor; the only intervention that does is the architectural shift from autoregressive to CTC decoding (SVTRv2, +2.5 pt, p=0.02, n=474). A confidence-routed AR-CTC ensemble adds a directionally consistent +0.6 pt that stays within noise, and its dominant learned coefficient is each model's own minimum-softmax confidence--independently echoing the mechanism above. No configuration we test improves both the compositional corner and aggregate accuracy. The rare-input long tail thus points to architectural change rather than added capacity.

</details>

### 7. Mind the Rift: Cross-Scale Coupling Mismatch for AI-Generated Video Detection **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.00742](https://arxiv.org/abs/2609.00742)  · [📄 PDF](https://arxiv.org/pdf/2609.00742)
- **作者**: Siyu Li, Jin Yang, Weiheng Liang
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Litsay/RIFT](https://github.com/Litsay/RIFT)
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.MM
- **摘要（中）**: ①针对AI生成视频检测中，现有方法忽略跨尺度耦合失配这一新取证信号的问题。②提出了RIFT框架，包含宏观流（通过微分几何和持续同源性构建动态基线）、微观流（通过隐写分析和时间建模）以及耦合发散量化。③相比现有检测器，RIFT利用自然视频中宏观动态与微观残差的固有耦合，而AI生成器违反此耦合。④该框架作为正交方法，有望提升检测鲁棒性。
- **摘要（英）**: This paper identifies cross-scale coupling mismatch as a new forensic signal for AI-generated video detection, proposing the RIFT framework with macro and micro streams. It leverages the intrinsic coupling in natural videos to detect generated content.
- **评估**: 该论文提出新颖的取证信号和框架，对视频真实性验证有重要意义，与自动驾驶感知中的异常检测相关。
- **核心贡献**: 提出了基于跨尺度耦合失配的AI视频检测框架RIFT。
- **创新点**: 利用自然视频的物理耦合作为检测信号。
- **结果**: 提供了正交的检测方法，增强鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As AI video generators achieve cinematic realism, reliable detection becomes essential for safeguarding digital trust. We identify cross-scale coupling mismatch as a new forensic signal, where scale refers to the level of abstraction (semantic dynamics vs. pixel-level residuals): in natural videos, macro-level temporal dynamics and micro-level residual patterns are intrinsically coupled by the unified imaging physics pipeline, whereas AI generators, whose training objectives do not explicitly preserve this joint distribution, systematically violate this coupling. Detecting such mismatch is challenging because it requires independently extracting information at both scales while simultaneously quantifying their cross-scale relationship. We propose RIFT (Representation Inconsistency Forensics on Trajectories), an orthogonal forensic framework that addresses this through three interlocking components: a macro stream that builds a dynamic baseline of expected temporal evolution via differential geometry and persistent homology on learned manifold trajectories, a micro stream that acts as a sensitive forensic probe via steganalytic filtering and temporal modeling, and a coupling divergence module that measures the conditional dependency between the two streams. Gram-Schmidt orthogonality guarantees the information-theoretic validity of this measurement. Experiments on two benchmarks (VidProM, 120K videos, 7 generators; GenVidBench, 68K videos, 4 generators) demonstrate that RIFT achieves 99.33% and 99.72% F1-score respectively, with 97.87% unseen-generator detection rate in leave-one-out evaluation, while exhibiting encoder agnosticism: scaling from ViT-S/14 (22M) to ViT-L/14 (300M) changes F1 by less than 0.1%, and switching to a different encoder family (DINOv1) reduces F1 by only 0.73 pp. Code is available at https://github.com/Litsay/RIFT

</details>

---

## Network Pruning

### 1. S$^2$Prune: Spatially Structured Visual Token Pruning for Multimodal Large Language Models **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2609.01224](https://arxiv.org/abs/2609.01224)  · [📄 PDF](https://arxiv.org/pdf/2609.01224)
- **作者**: Yuanyuan Jia, Shunpu Tang, Qianqian Yang
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/yuanyuanjia71-spec/S2Prune](https://github.com/yuanyuanjia71-spec/S2Prune)
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对多模态大语言模型（MLLM）中视觉token冗余导致推理开销大的问题，现有剪枝方法基于重要性或冗余度选择token，但忽略了空间覆盖的稳定性。②提出S²Prune，一种无需训练的剪枝方法，先按区域划分图像并保证每区域至少保留一个token以维持空间覆盖，再根据拉普拉斯方差分配剩余预算，最后利用首个解码器块的早期表示变化（ERC）选择代表性token。③相比现有方法，S²Prune显式结合空间覆盖与局部结构自适应，克服了纯重要性/冗余度标准的空间偏差。④在Qwen2.5-VL-7B-Instruct上，S²Prune在无训练剪枝方法中平均准确率最高，仅用原始576个token中的32个仍保持良好性能。
- **摘要（英）**: This paper addresses the high inference cost of visual tokens in multimodal large language models by proposing S²Prune, a training-free pruning method that preserves spatial coverage via region-based token allocation and selects representative tokens using early representation change. It outperforms existing training-free pruning methods on Qwen2.5-VL-7B-Instruct, achieving the highest average accuracy with only 32 of 576 tokens.
- **评估**: 该工作为MLLM视觉token剪枝提供了新视角，强调空间覆盖的重要性，方法简单有效，对高效多模态推理有实际价值。
- **核心贡献**: 提出一种结合空间覆盖与局部结构自适应的无训练视觉token剪枝方法。
- **创新点**: 利用区域划分和拉普拉斯方差分配token预算，并引入早期表示变化选择代表性token。
- **结果**: 在Qwen2.5-VL-7B-Instruct上达到无训练剪枝方法中的最高平均准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual token pruning reduces the inference overhead of multimodal large language models (MLLMs) by retaining only a subset of visual tokens. Existing methods usually select tokens based on importance or redundancy. However, we observe that these criteria produce stable spatial biases across inputs and do not always outperform simple Uniform Grid sampling, highlighting the value of broad spatial coverage. Motivated by this, we propose S$^2$Prune, a training-free pruning method that preserves spatial coverage while adapting token density to local image structure. We first divide the image into regions and assign at least one token to each region to preserve coverage. The remaining token budget is then distributed according to Laplacian variation, giving more tokens to regions with richer structure. We then use Early Representation Change (ERC), computed from the first decoder block, to select representative tokens within each region. We evaluate S$^2$Prune across diverse settings and two MLLM architectures. On Qwen2.5-VL-7B-Instruct, it achieves the highest average accuracy among the evaluated training-free pruning methods. With only 32 of the original 576 visual tokens, it still retains 79.3% of the full-model performance. Code is available at https://github.com/yuanyuanjia71-spec/S2Prune.

</details>

### 2. SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.82)

- **arXiv ID**: [2609.01004](https://arxiv.org/abs/2609.01004)  · [📄 PDF](https://arxiv.org/pdf/2609.01004)
- **作者**: Shiyu Li, Zi-Yuan Hu, Shijia Huang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/LaVi-Lab/SinkPruner](https://github.com/LaVi-Lab/SinkPruner)
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI, cs.CL
- **摘要（中）**: ①针对多模态大语言模型视觉token剪枝中忽略高范数异常token的问题，这些token在特征和空间上高度冗余但常被误认为信息丰富。②提出SinkPruner，一种无训练剪枝框架，包含视觉清洗器（过滤高范数冗余并缓解注意力汇聚和分散）和文本引导剪枝器（保留与文本查询语义对齐的token）。③相比现有方法，SinkPruner显式处理高范数异常token，结合视觉和文本信息进行粗到细的剪枝。④在12个图像-语言和4个视频-语言基准上验证了有效性、效率和泛化性。
- **摘要（英）**: This paper tackles the issue of high-norm outlier tokens in visual token pruning for MLLMs, proposing SinkPruner, a training-free framework with a visual sanitizer and a text-guided pruner. It demonstrates effectiveness and efficiency across 12 image-language and 4 video-language benchmarks.
- **评估**: 该工作揭示了高范数token的冗余性，提出针对性解决方案，对提升MLLM推理效率有重要参考意义。
- **核心贡献**: 提出SinkPruner框架，通过视觉清洗和文本引导实现高效视觉token剪枝。
- **创新点**: 识别并利用高范数异常token的冗余性，结合注意力汇聚缓解和文本语义对齐。
- **结果**: 在多个图像和视频语言基准上验证了有效性和泛化性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences. To reduce inference costs, recent studies have explored visual token pruning through vision-centric or text-guided strategies. However, these methods often overlook high-norm outlier tokens, i.e., tokens with abnormally large feature norms, leading to suboptimal pruning decisions. In this work, we show that such high-norm outlier tokens are highly redundant in both feature and spatial dimensions, yet are often mistakenly preserved as informative cues by existing methods. Motivated by this observation, we propose SinkPruner, a training-free visual token pruning framework for efficient MLLM inference. SinkPruner follows a coarse-to-fine design with two key modules: a visual sanitizer that filters high-norm redundancies and alleviates attention sink and attention dispersion, and a text-guided pruner that further retains tokens semantically aligned with the text query. Extensive experiments on twelve image-language and four video-language benchmarks demonstrate the effectiveness, efficiency, and generalizability of our framework. Notably, SinkPruner preserves 96.5% (91.8%) of the original performance of LLaVA-1.5 (Qwen2.5-VL) under an 89% token reduction. Experiments further indicate that our visual sanitizer exhibits promising transferability in enhancing the performance of existing pruning methods. Our code is available at https://github.com/LaVi-Lab/SinkPruner.

</details>

### 3. A Closed-Loop Evaluation of Capability Loss and Recovery in Compressed Driving Policies **⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2609.00718](https://arxiv.org/abs/2609.00718)  · [📄 PDF](https://arxiv.org/pdf/2609.00718)
- **作者**: Ahmad Alfan Alfian Irfan, Nur Ahmad Khatim, Mansur Arief
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.AI, cs.CV
- **摘要（中）**: ①针对压缩驾驶策略时仅用聚合数值评分评估可能无法反映实际驾驶安全性的问题。②提出一种阶段式闭环评估方法，在Gym-Duckietown中训练信念状态策略，逐步压缩actor并在五个驾驶课程上评估。③相比传统评估，该方法通过闭环交互测试压缩各阶段的能力损失和恢复。④发现结构化剪枝是驾驶能力首次丧失的阶段，蒸馏可改善但受限于重放数据，整数量化导致部分需要停车再启动的课程失效。
- **摘要（英）**: This paper proposes a stage-wise closed-loop evaluation approach for compressed driving policies, training a belief-state policy in Gym-Duckietown and compressing it stage by stage. It finds that structured pruning first causes capability loss, distillation improves but is limited by rehearsal data, and integer quantization loses stop-and-resume curricula.
- **评估**: 该工作强调闭环评估在压缩驾驶策略中的重要性，为自动驾驶模型压缩提供了更可靠的验证方法。
- **核心贡献**: 提出一种阶段式闭环评估框架，用于分析压缩驾驶策略的能力损失与恢复。
- **创新点**: 将压缩过程分解为阶段，并在闭环驾驶环境中逐阶段评估。
- **结果**: 识别出结构化剪枝为能力损失关键阶段，量化影响特定驾驶行为。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many automobile and mobility companies deploy learned driving policies on embedded computers with limited memory and power. Pruning, knowledge distillation, and quantization are the standard methods to reduce the size and the inference cost of these policies. However, these methods are commonly assessed by aggregate numerical scores, and such scores may not reflect the ability of the policy to drive safely when interacting with other road users. In this study, we propose a stage-wise closed-loop evaluation approach to follow a driving policy through a compression pipeline. We formulate the driving task as a partially observable Markov decision process (POMDP) and train a belief-state policy with proximal policy optimization (PPO) in Gym-Duckietown. We then extract the actor, compress it one stage at a time, and evaluate it on five driving curricula. We show that structured pruning is the stage at which the driving capability is first lost. Meanwhile, distillation improves the pruned actor, but the improvement is limited by its rehearsal data. Integer quantization of the improved actor loses some of the curricula that require the vehicle to stop and then resume. Interestingly, the same procedure on the unpruned actor preserves all five curricula. Our study thus provides an empirical analysis aiming to answer the currently active discussions on how to accept a compressed driving policy, so as to achieve a safe and statistically reliable deployment of automated driving functions.

</details>

### 4. One Prompt Is Enough: Watermark Laundering Through Foundation Image Models **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.85)

- **arXiv ID**: [2609.01249](https://arxiv.org/abs/2609.01249)  · [📄 PDF](https://arxiv.org/pdf/2609.01249)
- **作者**: Jidong Yang, Qi Li, Wei Zong et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI, cs.CR
- **摘要（中）**: ①针对不可见水印在基础图像模型下易被去除的安全威胁。②形式化水印清洗问题，评估六个OpenAI和Google图像编辑模型、三种水印方案和1800个重建输出，发现OpenAI模型产生最强载荷破坏，而Nano Banana 2显示DwtDct在高保真重建下仍脆弱。③提示词消融表明无需显式去除指令即可破坏水印，效果主要由重建路径引起。④与常规攻击比较显示基础模型构成独特威胁。
- **摘要（英）**: This paper formalizes watermark laundering via foundation image models, showing that a single reconstruction prompt can remove invisible watermarks. Evaluation across six models and three schemes reveals OpenAI models cause strongest disruption, with effects primarily from reconstruction rather than attack wording.
- **评估**: 对多模态模型安全性有重要启示，但非自动驾驶核心领域，相关性一般。
- **核心贡献**: 形式化水印清洗问题并系统评估基础模型威胁。
- **创新点**: 揭示重建路径本身即可破坏水印，无需显式攻击指令。
- **结果**: 识别出OpenAI模型的高破坏性和DwtDct的脆弱性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Invisible watermarks are typically evaluated against predefined perturbations such as compression, blur, noise, cropping, and denoising. Public foundation image models expose a distinct threat: an attacker can submit a watermarked image with a single reconstruction prompt and obtain a visually faithful output from which the invisible watermark can no longer be decoded reliably. We formalize this failure mode as watermark laundering and evaluate it using a joint payload-fidelity profile that combines bit error rate (BER) with visual and semantic preservation. Across six OpenAI and Google image editing models, three representative watermarking schemes, and 1,800 reconstructed outputs, we identify two complementary laundering regimes: OpenAI models produce the strongest payload disruption across the evaluated schemes, whereas Nano Banana 2 shows that DwtDct remains vulnerable under high-fidelity reconstruction. Prompt ablations show that no single removal-oriented instruction is necessary for payload disruption, indicating that the effect is primarily induced by the reconstruction pathway rather than by explicit attack wording. Comparisons with conventional attacks further show that prompt-conditioned reconstruction constitutes a distinct operational attack interface. These findings motivate foundation-model reconstruction as a missing robustness condition in invisible watermark evaluation.

</details>

### 5. Stochastic Optimization of Tree Tensor Networks **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.00870](https://arxiv.org/abs/2609.00870)  · [📄 PDF](https://arxiv.org/pdf/2609.00870)
- **作者**: Marius Willner, Maximilian Scharf, André Uschmajew et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: math.OC, cs.CV, physics.comp-ph
- **摘要（中）**: ①针对树张量网络（TTNs）在机器学习中优化困难的问题。②推导了TTNs在参数流形和商流形上的随机黎曼优化器，包括自适应和无学习率方案，适用于小批量训练，并采用混合CNN-TTN架构评估。③相比无约束优化，所提优化器在预测性能相当的同时实现数值稳定的下游压缩。④在Fashion-MNIST、CIFAR10和Imagenette上验证，但摘要未提供具体数值。
- **摘要（英）**: This paper derives stochastic Riemannian optimizers for tree tensor networks, including adaptive and learning-rate-free schemes. Using a hybrid CNN-TTN architecture, the optimizers achieve comparable performance to unconstrained optimization while enabling stable compression.
- **评估**: 与自动驾驶感知相关性低，主要面向机器学习基础优化，但方法有理论价值。
- **核心贡献**: 提出TTNs的随机黎曼优化器。
- **创新点**: 在参数和商流形上推导自适应优化方案。
- **结果**: 在多个数据集上实现可比性能并支持稳定压缩。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tensor networks, originally developed for quantum many-body physics, are promising models for machine learning. We derive stochastic Riemannian optimizers for tree tensor networks (TTNs) on both their parameter and quotient manifolds, including adaptive and learning-rate-free schemes suitable for minibatch training. Using a hybrid CNN-TTN architecture, we evaluate the methods on Fashion-MNIST, CIFAR10, and Imagenette. The proposed optimizers achieve predictive performance comparable to unconstrained optimization while enabling numerically stable downstream compression.

</details>

### 6. Potential-Guided Particle Steering for Negation-Constrained Dexterous Grasping **⭐⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2609.00555](https://arxiv.org/abs/2609.00555)  · [📄 PDF](https://arxiv.org/pdf/2609.00555)
- **作者**: Geonho Kim, SooGon Kim, Jongmin Lee
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.RO, cs.CV
- **摘要（中）**: ①论文针对语言驱动的灵巧抓取模型（如DextER）在指令包含否定约束（如“抓把手但避开主体”）时系统性失败的问题，现有训练语料（如DexGYSNet）几乎不含回避指令，且收集所有约束样本不切实际。②提出一种推理时框架，结合序贯蒙特卡洛与无分类器引导，在采样过程中引导向指定部位并剪除朝向禁止区域的候选，无需否定特定训练样本；利用冻结的3D部件定位模型从语言指令中定位禁止区域。③相比已有工作，创新在于无需否定示例训练即可处理否定约束，避免了模型将禁止部位误解为抓取目标。④构建了NegGrasp基准，包含配对的正/负指令和约束感知指标，实验表明该方法在否定约束场景下显著提升抓取成功率，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the systematic failure of language-driven dexterous grasping models under negation constraints, proposing an inference-time framework combining Sequential Monte Carlo with classifier-free guidance to steer sampling toward instructed parts while pruning forbidden regions, without negation-specific training. A frozen 3D part-grounding model localizes forbidden areas, and a new benchmark NegGrasp with constraint-aware metrics is introduced, showing improved performance in constrained scenarios.
- **评估**: 该论文聚焦于机器人抓取中的否定约束问题，方法具有推理时通用性，但领域与自动驾驶感知相关性较低，质量中等。
- **核心贡献**: 提出无需否定训练样本的推理时框架，解决语言驱动灵巧抓取中的否定约束问题。
- **创新点**: 结合序贯蒙特卡洛与无分类器引导，在采样中动态剪除禁止区域候选。
- **结果**: 在NegGrasp基准上验证了有效性，但具体数值未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Language-driven dexterous grasp models, such as DextER, perform well when instructions specify where to grasp, but we find they fail systematically when an instruction also specifies where not to grasp (e.g., "grasp the handle but avoid the body"). Existing training corpora, DexGYSNet among them, contain virtually no avoidance instructions, and collecting examples for every possible constraint is impractical. Moreover, because every part mentioned during training denotes a contact target, models may interpret a forbidden part as another region to grasp rather than one to avoid. We therefore introduce an inference-time framework for negation-constrained dexterous grasping that requires no negation-specific training examples. Combining Sequential Monte Carlo with classifier-free guidance, our method guides sampling toward the instructed part while pruning candidates headed for the forbidden region, without any negation examples during training. A frozen 3D part-grounding model localizes the forbidden region from the language instruction. To evaluate this setting, we construct NegGrasp, a benchmark of paired positive/negative instructions with constraint-aware metrics that credit a grasp only if it both accomplishes the task and respects the stated constraint. On NegGrasp, our method reduces the violation rate of the strongest baseline from 57.9% to 17.2% while improving both constraint-aware and physical success.

</details>

---

## Self-supervised Vision

### 1. What, Where, and How: Probing Spatiotemporal Representations in Video Foundation Models **⭐⭐⭐** (相关度: 60%, 质量: 0.78)

- **arXiv ID**: [2609.01551](https://arxiv.org/abs/2609.01551)  · [📄 PDF](https://arxiv.org/pdf/2609.01551)
- **作者**: Sharon S. Musa, Fereshteh Forghani, Harrish Thasarathan et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对自监督视频基础模型表示中视觉概念编码位置和几何组织不明确的问题。②通过系统逐层分析V-JEPA 2和VideoMAE-v2，训练轻量探针发现相机运动理解、直观物理和异常检测三种时间属性。③相比已有工作，该研究提供了层级的表示分析，并发现相机运动在60-70%网络深度达到最佳性能（>90 ROC AUC），异常检测中等（>60），直观物理接近随机。④此外，发现时间特征形成平滑低维轨迹，并应用样条插值实现相机运动插值。
- **摘要（英）**: This paper systematically analyzes spatiotemporal representations in video foundation models, probing camera motion, intuitive physics, and anomaly detection across layers. It finds camera motion emerges at 60-70% depth with high accuracy, while physics reasoning is limited, and demonstrates geometric organization via spline-based steering.
- **评估**: 该工作为视频基础模型的可解释性提供了深入分析，有助于理解表示学习机制。
- **核心贡献**: 揭示了视频基础模型中时间属性的层级编码和几何组织。
- **创新点**: 结合轻量探针和几何分析，系统研究层间表示。
- **结果**: 相机运动理解达到高ROC AUC，并实现潜在空间插值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised video foundation models learn rich spatiotemporal representations, yet it remains unclear what visual concepts these representations encode, where they emerge across transformer layers, and how they are geometrically organized. In this work, we tackle these three questions through a systematic layer-wise analysis of V-JEPA 2 and VideoMAE-v2. We leverage lightweight probes trained to discover three temporally grounded properties: (i) camera motion understanding, (ii) intuitive physics, and (iii) anomaly detection. Both models encode camera motion, with best results ($>90$ ROC AUC) emerging at 60-70% of network depth, and achieve moderate anomaly detection performance ($>60$ ROC AUC), but remain near chance on intuitive-physics tasks, suggesting a limited encoding of deeper physical reasoning. Beyond classification, we find that temporal features from individual videos form smooth low-dimensional trajectories in representation space, suggesting that camera motion is not only linearly decodable but also geometrically organized. Based on these results, we apply geometry-aware spline-based steering in the model's latent representations to interpolate camera motion, yielding steered videos with smoother trajectories and more coherent temporal progression than linear interpolation.

</details>

### 2. Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.01511](https://arxiv.org/abs/2609.01511)  · [📄 PDF](https://arxiv.org/pdf/2609.01511)
- **作者**: Lucas Cunha, Lucas Sotomaior, Lucas Gasperin et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/lucasdocunha/FaceForgery-Benchmark](https://github.com/lucasdocunha/FaceForgery-Benchmark)
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对人脸伪造检测在真实退化条件下鲁棒性不足的问题。②构建标准化基准，在MFFI数据集上评估六种模型家族，包括CNN、Transformer和冻结DINOv3，覆盖空间、频谱和混合输入。③发现干净集性能不能反映退化鲁棒性，DINOv3在退化集上表现最佳。④Xception在干净集达0.884 AUC，但退化集下降；DINOv3在退化集达0.726 AUC，仅训练线性头。
- **摘要（英）**: This paper addresses face forgery detection robustness under realistic degradation by benchmarking six model families on the MFFI dataset. Results show clean-set performance is not indicative of robustness; frozen DINOv3 achieves the best degraded-set AUC of 0.726, while Xception excels on clean sets (0.884). Fourier cues are useful only when combined with RGB.
- **评估**: 对伪造检测鲁棒性有系统分析，但领域与自动驾驶感知关联有限。
- **核心贡献**: 提供人脸伪造检测在退化条件下的标准化基准和鲁棒性分析。
- **创新点**: 系统比较空间、频谱和自监督特征在退化下的表现。
- **结果**: 揭示DINOv3在退化条件下的优越鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Face forgery detectors often achieve strong results on controlled benchmarks, but their reliability under realistic image degradations remains limited. This paper presents a standardized benchmark for face forgery detection using the Multi-Dimensional Face Forgery Image (MFFI) dataset and evaluates performance on both clean and degraded test partitions. We compare six model families, including convolutional networks, transformer-based models, and a frozen self-supervised DINOv3 backbone, across spatial, spectral, and hybrid input representations. The results show that clean-set performance is not a reliable indicator of robustness under compression, resizing, and blurring. Xception with RGB obtains the best clean performance, reaching 0.884 mean ROC-AUC, but degrades substantially on the harder partition. In contrast, frozen DINOv3 achieves the strongest degraded-set result, with 0.726 mean ROC-AUC, while training only a linear classification head. The representation analysis indicates that Fourier-domain cues are most useful when combined with RGB information, whereas purely spectral inputs consistently underperform spatial representations. Qualitative attribution maps further suggest that convolutional detectors focus on localized artifacts, while DINOv3 relies on broader facial structure. These findings reinforce the need for degraded evaluation protocols and highlight self-supervised visual representations as a promising direction for robust face forgery detection. Our source code is publicly available at https://github.com/lucasdocunha/FaceForgery-Benchmark/.

</details>

### 3. CMRVision: A Foundation Model for Cardiac MR Image Analysis **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.01308](https://arxiv.org/abs/2609.01308)  · [📄 PDF](https://arxiv.org/pdf/2609.01308)
- **作者**: Athira J. Jacob, Puneet Sharma, Daniel Rueckert
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对心脏磁共振成像缺乏专用基础模型的问题。②提出CMRVision，使用DINOv3风格自监督学习在3600万CMR图像上预训练，系统评估架构和训练选择。③相比自然图像和医学图像基础模型，CMR特定预训练、小patch和patch级目标提升下游性能。④在多任务分割基准上表现最佳，LV Dice 0.940-0.967，心肌0.855-0.905。
- **摘要（英）**: This paper introduces CMRVision, a CMR-specific foundation model pretrained with DINOv3-style self-supervised learning on 36 million images. Domain-specific pretraining with smaller patches improves downstream segmentation and classification, outperforming prior baselines with Dice scores up to 0.967 for LV.
- **评估**: 医学影像基础模型研究，方法可借鉴至自动驾驶多传感器预训练。
- **核心贡献**: 构建CMR专用基础模型并验证领域特定预训练优势。
- **创新点**: 大规模CMR自监督预训练与patch级目标设计。
- **结果**: 在多任务分割上超越现有基础模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cardiac magnetic resonance (CMR) imaging provides complementary information on cardiac anatomy, function, and tissue characterization across multiple sequences and views. In this work, we investigate foundation model pretraining for 2D CMR and introduce CMRVision, a CMR-specific foundation model trained using DINOv3-style self-supervised learning on a multi-center, multi-sequence cohort of 36 million CMR images. We systematically evaluate architectural and training design choices for domain-specific pretraining. CMRVision is evaluated on two downstream tasks: multi-task segmentation across cine, late gadolinium enhancement (LGE), and mapping sequences, and cine view classification. Our experiments show that CMR-specific pretraining, smaller patch sizes, and patch-level objectives consistently improve downstream performance. Across a multi-task segmentation benchmark, CMRVision achieved the strongest overall performance, outperforming prior natural-image (NI), medical-image, supervised, and CMR foundation model baselines. Improvements were modest but consistent across structures and sequences, with Dice scores ranging from 0.940-0.967 for LV and 0.855-0.905 for myocardium, and reaching 0.929 for RV, 0.920 for LA, and 0.931 for RA. The largest gains were observed for myocardium segmentation in LGE and mapping images. In a zero-shot segmentation task on unseen LGE long-axis views, the model achieved an average Dice score of 0.692, demonstrating cross-view generalization. For cine view classification, CMRVision achieved the highest average accuracy (0.906), compared to prior methods reported in the literature. These results highlight the potential of CMRVision to support robust and generalizable cardiac MRI analysis across multiple sequences and views.

</details>

### 4. Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison **⭐⭐⭐⭐⭐** (相关度: 90%, 质量: 0.9)

- **arXiv ID**: [2609.01530](https://arxiv.org/abs/2609.01530)  · [📄 PDF](https://arxiv.org/pdf/2609.01530)
- **作者**: Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对跨视图补全自监督预训练中参考视图对非共视区域提供单目信号的问题，提出Gekko网络，将重建误差的相对改进作为共视性的自监督代理。方法上，Gekko联合执行跨视图补全、掩码自编码和逐像素相对改进预测，为所有掩码区域提供双目信号，无需3D标注。相比CroCo，Gekko在零样本对应估计、相对位姿估计和点图回归上持续提升，在严格相对位姿阈值下精度高6倍，ETH3D端点误差降低22%。
- **摘要（英）**: This paper addresses the limitation of cross-view completion pre-training, where non-co-visible regions receive only monocular signals, by introducing Gekko, which predicts the relative improvement of cross-view reconstruction error over masked autoencoding as a co-visibility proxy. Gekko jointly performs cross-view completion, masked autoencoding, and per-pixel prediction, providing binocular signals for all regions, and consistently outperforms CroCo on zero-shot correspondence, relative pose estimation, and pointmap regression, with up to 6x higher accuracy and a 22% drop in endpoint error on ETH3D.
- **评估**: 该工作为3D视觉自监督预训练提供了重要改进，显著提升下游任务性能，与自动驾驶感知高度相关。
- **核心贡献**: 提出Gekko网络，利用重建误差比较增强跨视图补全预训练。
- **创新点**: 将重建误差的相对改进作为共视性代理，提供额外双目信号。
- **结果**: 在零样本任务上优于CroCo，严格阈值下精度高6倍，ETH3D端点误差降低22%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstructing non-co-visible patches, implicitly yielding a monocular training signal in these regions. We introduce Gekko, which turns this limitation into a useful signal. The relative improvement of the cross-view reconstruction error over a masked-autoencoder error is a self-supervised proxy for co-visibility: large improvements indicate co-visible regions, negligible ones non-co-visible areas. Gekko is a network, trained from scratch, that jointly performs cross-view completion, masked autoencoding, and per-pixel prediction of this relative improvement, providing an additional binocular signal for all masked regions without any ground-truth 3D annotation. Under identical architectures and training data, Gekko consistently outperforms CroCo on zero-shot correspondence estimation, relative pose estimation, and pointmap regression, with up to 6 times higher accuracy at the strictest relative-pose threshold and a 22% drop in end-point error on ETH3D. The extra channel it learns is itself a strong co-visibility detector on unseen scenes, and Gekko's frozen features outperform released cross-view backbones of comparable or larger size. It can also be trained directly from raw videos with a simple stride-based curriculum, removing the cumbersome 3D preprocessing prior methods require while matching models trained on curated data. Code and pre-trained models are publicly available.

</details>

### 5. PredErase: Training-Free Object-and-Effect Removal with Predictive Latent Guidance **⭐⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2609.00956](https://arxiv.org/abs/2609.00956)  · [📄 PDF](https://arxiv.org/pdf/2609.00956)
- **作者**: Waikit Xiu, Qiang Lu, Junbiao Chen et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对图像编辑中，仅移除目标掩膜无法处理阴影和接触着色等残留效应的问题。②提出PredErase，一种无需训练的后处理流程，基于FLUX.2和I-JEPA，通过接触带扩展和预测潜在引导来分离可编辑区域与目标结构。③相比现有训练无关方法，PredErase利用I-JEPA的掩码预测能力提供上下文条件目标，并锁定非支持区域。④在RemovalBench等基准上，PredErase优于原生FLUX.2基线。
- **摘要（英）**: This paper tackles the issue of residual photometric effects when removing objects with only instance masks. PredErase is a training-free method on FLUX.2 and I-JEPA that separates editable regions and predicts hole structure via latent guidance. It outperforms the native backbone on removal benchmarks.
- **评估**: 该工作对图像编辑中的对象移除有实际意义，但相关性较低，且效果数据不完整。
- **核心贡献**: 提出一种无需训练的对象与效应移除方法。
- **创新点**: 结合I-JEPA预测引导与接触带扩展。
- **结果**: 在多个基准上优于原生FLUX.2。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Removing an object is not the same as filling its mask. Cast shadows and contact shading usually lie outside the user-provided instance mask M_obj, so a frozen Fill model that edits only that mask leaves the object's photometric footprint on nearby surfaces. Supervised removers learn this joint erasure from paired clean plates. Training-free editors freeze pretrained weights, yet most still treat M_obj as the entire editable support and steer sampling with CLIP or DINO energies that do not predict the occluded scene. We present PredErase, a training-free inference procedure on frozen FLUX.2 and I-JEPA. The method separates where Fill may rewrite pixels from what structure should occupy the hole. A contact-band expansion M_flux of M_obj exposes local residuals on the supporting plane. I-JEPA, pretrained for masked token prediction, supplies a context-conditioned hole target in representation space; sparse projected gradients align decoded Fill completions with that target inside the instance, while coordinates outside the packed support stay locked. Under instance-only masks on RemovalBench, RORD-Val, and DEFACTO-Val, PredErase improves the native FLUX.2 backbone. Supervised removers remain stronger on several full-image appearance metrics; the supported claim is training-free object-and-effect editing of frozen Fill, not replacement of paired-data erasers.

</details>

---

## Video Understanding

### 1. Seeing the World and the Self from Egocentric Video **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2609.01276](https://arxiv.org/abs/2609.01276)  · [📄 PDF](https://arxiv.org/pdf/2609.01276)
- **作者**: Kai Guan, Minchao Jiang, Ruichen WangLi et al. (5 authors)
- **🏷️ 机构**: PolyU / OPPO
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对第一视角视频中完整3D感知的难题，即同时恢复周围场景和穿戴者全身运动，并统一到同一度量坐标系。现有方法通常将场景重建和运动估计分开处理，忽略了二者间的相互依赖。作者提出RESELF框架，将确定性度量几何重建与几何条件运动生成相结合，利用大规模外部视角数据预训练的几何基础模型，通过帧级尺度和相对位姿一致性目标适应第一视角视频，并用扩散模型恢复穿戴者运动。相比已有工作，该方法首次在统一框架中解决场景与自身重建的不对称可见性和不同预测范式问题，实验表明其在场景重建和运动估计上均取得显著提升。
- **摘要（英）**: This paper addresses complete 3D perception from egocentric video, jointly recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. The proposed RESELF framework couples deterministic metric geometry reconstruction with geometry-conditioned motion generation, adapting a geometry foundation model via frame-wise scale and relative-pose consistency, and using a diffusion model for motion recovery. It outperforms separate scene reconstruction and motion estimation methods, demonstrating the benefit of unified joint recovery.
- **评估**: 该论文提出了一种新颖的统一框架，解决了第一视角感知中场景与自身重建的耦合难题，对自动驾驶和可穿戴设备应用具有重要参考价值。
- **核心贡献**: 提出RESELF，首个统一重建场景与穿戴者全身运动的第一视角3D感知框架。
- **创新点**: 将确定性几何重建与生成式运动推断结合，利用几何基础模型适应第一视角数据。
- **结果**: 在场景重建和运动估计任务上均优于现有分离方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Complete 3D perception from egocentric video requires recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. Existing methods typically address scene reconstruction and motion estimation separately: scene reconstruction methods ignore the wearer, whereas motion estimation methods lack explicit scene geometry and often depend on external trajectories. Joint recovery is challenging because the two tasks exhibit asymmetric visibility and require different prediction paradigms. The largely visible scene supports deterministic geometric regression, whereas the severely occluded body requires generative motion inference. We therefore propose RESELF (REconstructing the Scene and the sELF), a unified framework that couples deterministic metric geometry reconstruction with geometry-conditioned motion generation. RESELF adapts a geometry foundation model pre-trained on large-scale exocentric data to egocentric video using frame-wise scale and relative-pose consistency objectives. The resulting camera trajectory and latent geometric features condition a diffusion model that recovers the wearer's motion. A subsequent closed-loop kinematic feedback stage further refines the camera head while preserving the reconstructed scene geometry. To support training and evaluation, we curate EE4D-JSM from EgoExo4D by aligning egocentric video, sparse metric scene geometry, camera trajectories, and full-body motion annotations. Experiments show that RESELF outperforms state-of-the-art methods designed for the individual tasks across depth estimation, camera tracking, and full-body motion estimation. Code, models, and datasets will be available at https://ka1guan.github.io/RESELF/.

</details>

### 2. StreamScout: Learning When to Look Deeper for Streaming Video Understanding **⭐⭐⭐** (相关度: 50%, 质量: 0.65)

- **arXiv ID**: [2609.00291](https://arxiv.org/abs/2609.00291)  · [📄 PDF](https://arxiv.org/pdf/2609.00291)
- **作者**: Ce Zhang, Jing Bi, Jinxi He et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对流式视频理解中查询到达任意时刻、需在无界视频流上回答问题的挑战，指出现有系统对所有查询使用固定成本的记忆访问，忽略了证据需求的差异。作者提出StreamScout，一种自适应推理框架，在流中仅维护轻量级文本时间线，查询时逐步用三种视觉视图增强时间线，并在每阶段根据证据充分性决定立即回答或升级。通过辅助集上的级联探测和知识蒸馏，优化停止或升级策略，并进一步细化策略。相比已有工作，该方法首次将记忆访问深度作为可学习决策，实验表明在保持准确率的同时显著降低计算成本。
- **摘要（英）**: This paper tackles streaming video understanding where queries arrive at arbitrary moments, proposing StreamScout, an adaptive inference framework that progressively augments a lightweight textual timeline with visual views and decides when to answer or escalate. It distills the model's competence boundary into a LoRA adaptation to improve the stop-or-escalate policy. Experiments show reduced computational cost while maintaining accuracy.
- **评估**: 该论文聚焦流式视频理解的推理效率，提出自适应深度访问机制，对实时视频分析系统有启发意义。
- **核心贡献**: 提出StreamScout，首个在流式视频理解中自适应决定记忆访问深度的框架。
- **创新点**: 将记忆访问深度建模为可学习策略，并通过知识蒸馏优化决策。
- **结果**: 在保持准确率的同时显著降低计算开销。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Streaming video understanding requires answering questions that arrive at arbitrary moments over an unbounded video stream. Existing systems primarily focus on what to retain in a bounded memory, yet access that memory using the same fixed-cost procedure for every query, despite substantial variation in the evidence required. We argue that deciding how deeply to access memory for each query is as important as deciding what the memory should store. To this end, we introduce StreamScout, an adaptive inference framework that maintains only a lightweight textual timeline in context as the stream unfolds. At query time, StreamScout progressively augments the timeline with up to three increasingly informative visual views: a glance at recent frames, a uniform look-back over the past stream, and query-salient retrieval. At each stage, the model answers immediately if the available evidence is sufficient; otherwise, it escalates to the next view. To improve this stop-or-escalate policy, we probe the cascade on an auxiliary set and distill the model's empirical competence boundary into supervision for a lightweight LoRA adaptation, yielding StreamScout-S. We further refine the policy through reinforcement learning, allowing the model to explore stopping behaviors beyond imitation of the distilled decisions, yielding StreamScout-R. Across three backbones and three streaming benchmarks, StreamScout and its variants consistently outperform prior streaming methods while substantially reducing inference cost and token consumption; on OVO-Bench, for instance, StreamScout-S improves Qwen3-VL-8B by 14.65 points while using 59% fewer tokens than uniform sampling and answering in 1.04 s on average.

</details>

### 3. TempCloze: Can Video-LLMs Identify the Missing Middle? **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.85)

- **arXiv ID**: [2609.01515](https://arxiv.org/abs/2609.01515)  · [📄 PDF](https://arxiv.org/pdf/2609.01515)
- **作者**: Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对视频大模型（Video-LLMs）在时间推理任务中依赖语言捷径（如选项措辞、答案相关性）而忽视真实视觉时间理解的问题。②提出了TempCloze基准，给定视频开头和结尾片段，模型需从四个候选中识别真实缺失的中间片段，包含1521个来自长镜头和第一人称视频的样本，并沿语义、对齐和进展三个维度构造干扰项。③相比现有基准，通过同源干扰项和共享场景/物体减少外观线索，更纯粹地评估视觉时间推理。④评估10个专有和21个开源Video-LLMs发现对齐是主要瓶颈，模型常能识别语义内容和局部进展但难以处理时间对齐。
- **摘要（英）**: This paper addresses the issue of language shortcuts in temporal reasoning benchmarks for Video-LLMs. It introduces TempCloze, a video cloze benchmark requiring models to identify the true missing middle from candidates, with same-source distractors along semantic, alignment, and progression dimensions. Evaluation of 31 models reveals alignment as the primary bottleneck, highlighting limitations in visual temporal reasoning.
- **评估**: 该基准设计严谨，有效隔离语言先验，对视频理解领域有重要参考价值，但相关性略偏视频理解而非自动驾驶核心。
- **核心贡献**: 提出了TempCloze基准，系统评估Video-LLMs的视觉时间推理能力。
- **创新点**: 通过同源干扰项和缺失中间片段设计，减少语言捷径干扰。
- **结果**: 发现对齐是Video-LLMs时间推理的主要瓶颈。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly long-take and egocentric videos. We construct same-source distractors along three dimensions: Semantic asks what event should happen, Alignment probes when it should occur, and Progression tests how it should unfold, while shared scenes and objects reduce appearance cues. Our evaluation of 10 proprietary and 21 open-source Video-LLMs reveals Alignment as the primary bottleneck: models often recognize plausible semantic content and local event progression but struggle with temporal alignment. We further conduct error pattern and behavioral sensitivity analyses on TempCloze-Mixed and TempCloze-Hard with four representative models to examine where errors arise and how candidate order, context direction, visible span, frame density, and test-time scaling influence model choices.

</details>

### 4. ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.00188](https://arxiv.org/abs/2609.00188)  · [📄 PDF](https://arxiv.org/pdf/2609.00188)
- **作者**: Xionghao Wu, Yijun Yang, Shiyang Zhou et al. (20 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对机器人操作泛化中动作标注数据稀缺且多样性有限的问题。②提出ZimaBlue框架，通过大规模视频预训练学习世界动作模型（WAMs），采用三阶段训练课程：因果具身视频预训练、视频-动作中间训练（统一动作表示）、目标机器人微调，并采用异步慢-快双系统架构实现实时控制。③相比现有方法，利用无动作的自我中心视频作为可扩展经验来源，并通过统一动作表示桥接异构机器人数据。④实验显示在多种机器人操作任务上提升泛化能力，但摘要未提供具体数值。
- **摘要（英）**: This paper tackles the scaling challenge in robotic manipulation by leveraging egocentric videos. ZimaBlue introduces a three-stage curriculum for learning World Action Models, with an asynchronous Slow-Fast architecture for real-time control. It demonstrates improved generalization across robot tasks, though specific metrics are not detailed in the abstract.
- **评估**: 视频预训练思路对自动驾驶感知有启发，但主要面向机器人操作，相关性中等。
- **核心贡献**: 提出ZimaBlue框架，从大规模视频中学习可泛化的世界动作模型。
- **创新点**: 三阶段训练课程和异步慢-快双系统架构。
- **结果**: 在机器人操作任务上提升泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robotic manipulation faces a fundamental scaling challenge: robust generalization demands broad physical experience, yet action-labeled robot trajectories are expensive to collect and inherently limited in diversity. Egocentric videos offer a far more scalable source of embodied experience, capturing object interactions, contact dynamics, tool use, and long-horizon behaviors across diverse environments. The central challenge is how to convert this abundant but action-free experience into effective robot control. We introduce ZimaBlue, a scalable framework for learning generalizable World Action Models (WAMs) from large-scale video. ZimaBlue follows a three-stage training curriculum: it first performs causal embodied video pre-training on large-scale human and robot egocentric videos, then grounds the learned visual dynamics in heterogeneous robot trajectories through video-action mid-training with a unified action representation, and finally specializes the model to a target robot for deployment. To make generative WAMs practical for real-time control, ZimaBluefurther adopts an asynchronous Slow-Fast dual-system architecture, where a high-capacity Slow world model provides generalizable spatiotemporal representations and a lightweight Fast branch enables 30 Hz action prediction on NVIDIA RTX 4090. On real-robot zero-shot evaluations, scaling from target-robot data alone to over 120,000 hours of embodied video improves success from 36.1% to 77.8%. ZimaBlue further delivers strong performance across multiple benchmarks, with particularly pronounced gains on unseen tasks.

</details>

---

## Multi-camera Perception

### 1. Monocular Depth Estimation from a Single Image: Progress and Opportunities **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.01172](https://arxiv.org/abs/2609.01172)  · [📄 PDF](https://arxiv.org/pdf/2609.01172)
- **作者**: Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 这篇综述论文系统回顾了单目深度估计领域的发展，从早期基于学习的方法到基础模型的兴起，涵盖问题定义、相对与度量深度估计的区别、关键挑战、常用数据集（室内、室外、合成）以及基础模型时代前的重大进展。作者重点分析了基于判别式和生成式范式的基础模型方法，强调大规模预训练（如DINOv3）和合成数据的关键作用，并比较了代表性模型的定量和定性表现。相比已有综述，该文提供了更全面的分类和最新进展总结，为自动驾驶等应用提供指导。
- **摘要（英）**: This survey traces the evolution of monocular depth estimation from early learning-based methods to foundation models, covering problem formulations, datasets, and key advances. It categorizes foundation-model approaches into discriminative and generative paradigms, highlighting the roles of large-scale pretraining and synthetic data. It provides a comprehensive comparison of representative models, offering guidance for applications like autonomous driving.
- **评估**: 该综述系统全面，对单目深度估计领域的研究者具有较高参考价值，但创新性相对有限。
- **核心贡献**: 提供单目深度估计从传统方法到基础模型的全面综述和分类。
- **创新点**: 将基础模型方法分为判别式和生成式范式，并强调预训练和合成数据的作用。
- **结果**: 总结了领域进展并比较了代表性模型性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing the problem, distinguishing between relative and metric depth estimation, and highlighting the key challenges that have shaped a decade of research. We then present common problem formulations and introduce the most widely used datasets, covering indoor, outdoor, and synthetic data. Following this, we review major advances prior to the foundation model era, distilling core insights from influential methods that contributed to improvements in accuracy, efficiency, and robustness. The survey then turns to the recent surge of foundation-model-based approaches, categorizing them into discriminative and generative paradigms and emphasizing the critical roles of large-scale pretraining (e.g., DINOv3) and synthetic data. We compare representative models using both quantitative benchmarks and qualitative examples, and discuss natural extensions to video-based depth estimation. Further, to illustrate real-world impact, we highlight the integration of depth estimation into applications such as visual SLAM, content generation, and robot perception. Finally, we outline open challenges and promising research directions as the field advances further into the era of foundation models.

</details>

### 2. Feed-Forward Multi-view Multi-person Reconstruction with Contrastive Human-Aware 3D Representation **⭐⭐⭐⭐** (相关度: 65%, 质量: 0.8)

- **arXiv ID**: [2609.00745](https://arxiv.org/abs/2609.00745)  · [📄 PDF](https://arxiv.org/pdf/2609.00745)
- **作者**: Yuanwang Yang, Buzhen Huang, Zongxuan Ren et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对非约束环境下多视角多人重建的鲁棒性和效率问题，指出现有自底向上方法依赖精确相机标定和显式跨视角匹配，难以应对严重遮挡和歧义。作者提出新的自顶向下范式，维护统一的实例中心人体感知3D空间，通过跨模态对比学习同时实现相机标定、跨视角关联和人体重建。多视角观测被提升并融合到共享3D空间，在实例级别联合编码几何结构、视觉外观和人体语义线索，并引入空间对比学习策略对齐同一实例的3D特征。相比已有工作，该方法在3D空间中原生执行对应推理、语义聚合和实例判别，实验表明在严重遮挡下显著提升跨视角一致性和鲁棒性。
- **摘要（英）**: This paper addresses robust multi-person reconstruction in unconstrained environments, proposing a top-down paradigm with a unified instance-centric human-aware 3D space for simultaneous camera calibration, cross-view association, and reconstruction via cross-modal contrastive learning. Spatial contrastive learning aligns 3D features of the same instance across views and modalities. Experiments show improved cross-view consistency and robustness under severe occlusions.
- **评估**: 该论文提出创新的自顶向下多视角重建框架，有效解决遮挡和标定问题，对3D人体感知研究有重要贡献。
- **核心贡献**: 提出统一实例中心3D空间的自顶向下多视角多人重建方法。
- **创新点**: 利用跨模态对比学习在3D空间原生实现跨视角关联和实例判别。
- **结果**: 在严重遮挡场景下显著提升重建鲁棒性和跨视角一致性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view human reconstruction has been extensively studied under simplified settings, yet robust and efficient multi-person reconstruction in unconstrained environments remains challenging. Existing bottom-up methods often rely on accurate camera calibration and explicit cross-view matching, and therefore struggle with severe occlusions and ambiguities. We propose a new top-down paradigm that maintains a unified, instance-centric human-aware 3D space, enabling simultaneous camera calibration, cross-view association, and human reconstruction via cross-modal contrastive learning. Observations from multiple views are lifted and fused into this shared 3D space, where geometric structure, visual appearance, and human-centric semantic cues are jointly encoded at the instance level. We further introduce a spatial contrastive learning strategy that aligns 3D features corresponding to the same human instance across different views and modalities while separating different instances. This enables correspondence reasoning, semantic aggregation, and instance discrimination to be performed natively in 3D, improving cross-view consistency and robustness under severe occlusions. Finally, structured human body models are recovered in a feed-forward manner by regressing SMPL parameters from instance-level 3D human tokens. Extensive experiments demonstrate robust, accurate, and efficient multi-view human reconstruction in challenging real-world scenarios.

</details>

### 3. Inverse Rendering for Modeling with Line Primitives **⭐⭐⭐** (相关度: 30%, 质量: 0.75)

- **arXiv ID**: [2609.00625](https://arxiv.org/abs/2609.00625)  · [📄 PDF](https://arxiv.org/pdf/2609.00625)
- **作者**: Kenji Tojo, Ariel Shamir, Nobuyuki Umetani et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.GR, cs.CV
- **摘要（中）**: ①针对毛发、纤维等模糊各向异性结构的真实物体重建和实时可视化难题。②提出基于显式线段基元的逆渲染方法，通过亚像素网格光栅化实现抗锯齿，并引入随机可微光栅器优化线段位置、属性和连接性。③相比基于表面的方法，能更好地捕捉模糊结构，且兼容标准深度测试光栅化、反射建模和物理仿真。④在合成和真实数据集上优于表面方法，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses reconstruction of fuzzy anisotropic structures like hair and fur. It proposes an inverse rendering method using explicit line primitives with a stochastic differentiable rasterizer. Experiments show superiority over surface-based approaches, though quantitative details are limited.
- **评估**: 与自动驾驶感知相关性低，主要面向图形学重建，但方法创新性尚可。
- **核心贡献**: 提出基于线段基元的逆渲染方法，用于模糊几何重建。
- **创新点**: 随机可微光栅器优化线段基元。
- **结果**: 在模糊结构重建上优于表面方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Faithfully capturing diverse real-world objects with fuzzy, anisotropic structures, such as hair, fur, fibers, and textiles, for efficient real-time visualization remains challenging. Recent radiance field reconstruction methods capture these structures from multi-view images using translucent volumetric primitives such as 3D Gaussians rather than opaque low-dimensional primitives (e.g., triangles, line segments, and polylines), thereby limiting compatibility with standard depth-tested rasterization, reflection modeling, and physical simulation. We present an inverse rendering method for reconstructing fuzzy geometry using explicit line segments, which are rasterized on a subpixel grid for anti-aliasing to reproduce a semi-transparent appearance. While straightforward to render, optimizing numerous line primitives to match target images poses a significant challenge. We address this by introducing a stochastic differentiable rasterizer for line segments that produces informative gradients with respect to vertex positions, attributes, and discrete connectivity. Experiments on synthetic and real-world datasets show that our method outperforms surface-based approaches in capturing fuzzy boundaries and achieves quality comparable to volumetric representations while relying entirely on explicit geometry. The resulting representation integrates seamlessly with standard graphics pipelines, enabling cross-platform rendering, various shading models, and physical simulation.

</details>

### 4. Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2609.00610](https://arxiv.org/abs/2609.00610)  · [📄 PDF](https://arxiv.org/pdf/2609.00610)
- **作者**: Xiaoyan Liu, Jiaxin Liu, Kangrui Li et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对当前4D生成范式因视频生成和3D重建顺序解耦导致交互延迟高的问题。②提出Streaming4D，将块式自回归视频生成与增量3D重建紧密耦合，生成视频块后立即触发重建，实现合成与几何更新的并行执行。③相比传统逐帧生成和延迟几何恢复，降低反馈延迟并保持几何保真度。④在RTX 4090上实现1.24倍加速，同时保持高质量4D几何和多视角一致性。
- **摘要（英）**: This paper addresses high latency in 4D generation by proposing Streaming4D, a synchronous pipeline integrating block-wise video generation with incremental reconstruction. It enables parallel execution, achieving 1.24x speedup on RTX 4090 while maintaining geometric fidelity.
- **评估**: 对自动驾驶在线重建和世界模型有启发，但主要面向4D内容生成，相关性中等。
- **核心贡献**: 提出Streaming4D，实现视频生成与3D重建的同步流水线。
- **创新点**: 块式视频生成与增量重建的紧耦合设计。
- **结果**: 在RTX 4090上实现1.24倍加速并保持高质量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current 4D generation paradigms are often bottlenecked by a sequential decoupling design: video is generated first, followed by 3D reconstruction, leading to high interaction latency. This limits applications in interactive real-time scenarios. To this end, we propose \textbf{Streaming4D}, a tightly coupled synchronous pipeline that integrates block-wise autoregressive video generation with incremental 3D reconstruction. Unlike traditional frame-by-frame emission and delayed geometry recovery, Streaming4D generates temporal video blocks and immediately triggers reconstruction for each completed block, enabling parallel execution between synthesis and geometric updates. This approach allows the world representation to evolve online with the video stream, reducing feedback latency while preserving geometric fidelity. We instantiate \textbf{Streaming4D} using a Self-Forcing-style autoregressive generator and an incremental reconstruction backend. Experiments show consistent runtime improvements across resolutions on a single RTX 4090 (1.24$\times$ speedup), while maintaining high-quality 4D geometry and multi-view consistency.

</details>

---

## Open-set Detection

### 1. VOIM: Training-Free Open-Vocabulary 3D Instance Mapping for RGB-D and Monocular SLAM **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.88)

- **arXiv ID**: [2609.00775](https://arxiv.org/abs/2609.00775)  · [📄 PDF](https://arxiv.org/pdf/2609.00775)
- **作者**: Sangmin Song, Sarath Kodagoda, Marc G. Carmichael et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对在线开放词汇3D实例映射系统在首次检测时即提交标签和实例决策，导致证据不足时错误累积的问题。②提出VOIM，一种无需训练的体素接地实例管理器，通过跨视图累积软证据来延迟决策。③相比现有系统，VOIM在ScanNet++上以多种感知配置超越OVO-SLAM 4.8-11.7 mIoU，并在同等协议下达到44.07 vs 32.37 mIoU。④该方法支持RGB-D和单目RGB输入，扩展了应用范围。
- **摘要（英）**: This paper addresses premature commitment in online open-vocabulary 3D instance mapping. It proposes VOIM, a training-free voxel-grounded manager that accumulates soft evidence across views before making decisions. VOIM outperforms OVO-SLAM by 4.8-11.7 mIoU on ScanNet++ and supports both RGB-D and monocular inputs.
- **评估**: 该工作对在线3D映射的决策时机提供了新思路，实验充分，对自动驾驶场景理解有直接参考价值。
- **核心贡献**: 提出了延迟决策的体素接地实例管理器VOIM。
- **创新点**: 利用跨视图累积软证据避免早期错误提交。
- **结果**: 在ScanNet++上显著超越现有方法，并支持单目输入。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Voxel-Grounded Online Instance Manager (VOIM), a training-free voxel-grounded instance manager that builds open-vocabulary 3D instance maps from RGB-D or from monocular RGB alone, a regime no prior training-free system addresses. Online systems typically segment object instances and label them at first detection, committing when evidence is weakest. VOIM instead defers label and instance decisions until soft evidence from unmodified, off-the-shelf perception has accumulated per voxel across views. We show that the mapping stage, rather than the particular perception models, carries the result: across four perception configurations on ScanNet++, varying the region descriptor, the detector label prior and the mask source, the map exceeds the strongest online RGB-D system, OVO-SLAM, by between 4.8 and 11.7 mIoU. Perception is not neutral, and substituting that baseline's own descriptor family costs 4.1 of the margin, yet the baseline carries the marginally better 2D descriptor (33.7 vs. 31.5 mIoU over three scenes) and still realizes the weaker map. Under a like-for-like protocol VOIM reaches 44.07 mIoU on ScanNet++ against 32.37, winning all ten scenes and both aggregations (pooled 33.31 vs. 25.97), and the same system runs unchanged to fully monocular RGB, matching that baseline pooled on Replica (27.80 vs. 27.50). The advantage is regime-specific: under Replica's all-classes scoring, matched inputs give a split result, 28.60 vs. 27.50 pooled against 24.59 vs. 30.11 on the per-scene mean. Room scale is label-limited and building scale drift-limited. Labeling does not run in real time, dominated by per-class detection over the full vocabulary. The maps export occupancy grids and resolve free-form queries to object instances.

</details>

### 2. SAM3-LoRA: Parameter-Efficient Adaptation of a Concept-Promptable Foundation Model for Multi-Class Structural Defect Segmentation **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2609.00469](https://arxiv.org/abs/2609.00469)  · [📄 PDF](https://arxiv.org/pdf/2609.00469)
- **作者**: P. Malaisree, S. Youwai, S. Janrungautai et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对SAM3等提示分割基础模型在专业领域（如结构缺陷分割）全量微调计算成本过高的问题。②应用低秩适配（LoRA）适配SAM3进行多类结构缺陷分割，并提出一种监督流程，直接使用类别名称作为提示训练概念可提示模型，无需模板或同义词扩展。③识别并缓解了仅正提示导致的模型存在预测与文本条件解耦的退化模式。④该方法在保持高效性的同时，实现了有效的多类分割，并跨数据集验证了效率提升的迁移性。
- **摘要（英）**: This paper applies LoRA to adapt SAM3 for multi-class structural defect segmentation, introducing a supervision procedure using category names as prompts and addressing a collapse mode from positive-only prompts. It achieves efficient adaptation with transferable gains across datasets.
- **评估**: 该论文对基础模型高效适配有贡献，但结构缺陷分割与自动驾驶感知领域关联度有限。
- **核心贡献**: 提出了基于LoRA的SAM3高效适配方法及监督流程。
- **创新点**: 识别并缓解了概念可提示模型的正提示退化问题。
- **结果**: 实现了高效且有效的多类结构缺陷分割。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Promptable segmentation foundation models such as SAM3 accept an open-vocabulary text concept and return every instance matching it, but adapting them to a specialized domain by full fine-tuning is computationally prohibitive for the organizations that would benefit most. This study applies Low-Rank Adaptation (LoRA) to SAM3 for multi-class structural defect segmentation and examines both how such a model can be supervised from conventional annotation and whether the resulting efficiency gain transfers across datasets. Two contributions are methodological. First, we describe a supervision procedure that trains a concept-promptable model directly from COCO-style class-labeled instance segmentation by using the category name itself as the prompt, requiring no prompt templates, no synonym expansion, and no learned class embeddings. Second, we identify and mitigate a failure mode specific to this setting: because a conventional annotation file yields positive prompts exclusively, the model's presence prediction decouples from the text condition and degenerates into responding to any prompt, a collapse that is invisible to every metric computed on positive prompts alone. Exhaustive hard-negative prompting, in which every dataset category absent from an image is issued as a zero-detection query, addresses this at no annotation cost. Two adapter placements were compared under an identical protocol, updating 0.121% and 1.341% of model parameters. On a purpose-built tunnel lining dataset, pixel intersection-over-union improved from 0.017 to 0.338 and instance-level recall from 0.375 to 0.672; on the independent public Structural Defects Dataset, from 0.017 to 0.855 and from 0.574 to 1.000. Improvements were directionally consistent across ten metrics on both datasets, and the largest per-category gains occurred precisely where zero-shot competence was absent.

</details>

---

## BEV

### 1. CERF: Communication-Efficient and Retraining-Free Collaborative Perception **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2609.00951](https://arxiv.org/abs/2609.00951)  · [📄 PDF](https://arxiv.org/pdf/2609.00951)
- **作者**: Jiuwu Hao, Ziyi Ni, Liguo Sun et al. (8 authors)
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Artificial Intelligence, Chinese Academy of Sciences,Institute of Automation
- **💻 代码**: [github.com/uestchjw/CERF](https://github.com/uestchjw/CERF)
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对协同感知中密集特征图传输导致的通信开销和异构性挑战，提出CERF，一种通信高效且无需重训练的开放异构协同感知框架。作者引入新的虚拟模态Poture，由其他智能体的感知输出生成，用于增强自车的BEV特征，并通过卡尔曼滤波跟踪器和运动预测模型从历史感知结果推导当前预测以缓解传输延迟。相比主流中间协同方法，CERF在多种下游任务上实现相当性能，同时将通信开销降低95%，并支持未知异构智能体的无缝集成。
- **摘要（英）**: This paper addresses communication overhead and heterogeneity in collaborative perception, proposing CERF, a communication-efficient and retraining-free framework that uses a virtual modality (Poture) generated from other agents' perception outputs to augment ego BEV features. Kalman-filter tracking and motion forecasting mitigate transmission delays. CERF achieves performance comparable to intermediate-collaboration methods while reducing communication overhead by 95% and enabling seamless integration of heterogeneous agents.
- **评估**: 该论文针对协同感知的实际部署瓶颈，提出高效且通用的解决方案，对自动驾驶多车协同具有重要工程价值。
- **核心贡献**: 提出CERF，首个通信高效且无需重训练的开放异构协同感知框架。
- **创新点**: 引入虚拟模态Poture增强BEV特征，并利用预测补偿传输延迟。
- **结果**: 通信开销降低95%，性能与主流方法相当，支持异构智能体集成。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Collaborative perception shares information among multiple agents to obtain a comprehensive scene representation, enhancing the perceptual capability of individual agents. However, most existing methods rely on transmitting and fusing dense feature maps for collaboration, which incurs inevitable communication overhead and heterogeneity challenges, limiting their practicality for real-world deployment. To address these challenges, we propose CERF, a novel Communication-Efficient and Retraining-Free framework for open heterogeneous collaborative perception. In CERF, we introduce a new virtual modality (termed Poture), which is generated from the perception outputs of other agents, to augment the extracted Bird's Eye View (BEV) features of the ego agent. To mitigate transmission delays, we employ a Kalman-filter based tracker and a motion forecasting model to derive the current predictions from historical perception results. Extensive experiments demonstrate that CERF achieves performance comparable to mainstream intermediate-collaboration methods while reducing communication overhead by 95% across various downstream tasks. Furthermore, CERF enables seamless integration of unknown heterogeneous agents into the existing collaborative framework without additional retraining costs. Code is available at https://github.com/uestchjw/CERF.

</details>

### 2. PyDoseRT Proton: A GPU Pencil-Beam Engine with a Convolutional Residual-Correction Network for Fast Proton Dose Calculation **⭐⭐** (相关度: 10%, 质量: 0.5)

- **arXiv ID**: [2609.01018](https://arxiv.org/abs/2609.01018)  · [📄 PDF](https://arxiv.org/pdf/2609.01018)
- **作者**: Lukas Zimmermann, Hermann Fuchs, Attila Simkó et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: physics.med-ph, cs.CV
- **摘要（中）**: ①针对质子剂量计算中，物理引擎精度与速度的权衡问题。②提出PyDoseRT Proton，结合GPU铅笔束引擎和卷积残差校正网络，通过双高斯核校准和残差U-Net预测修正。③相比纯物理或纯学习模型，混合方法在保持速度的同时提升精度。④在DoseRAD2026任务中，该方法达到接近蒙特卡洛的精度。
- **摘要（英）**: This paper addresses the speed-accuracy trade-off in proton dose calculation. PyDoseRT Proton combines a GPU pencil-beam engine with a residual correction network for fast and accurate prediction. It achieves near-Monte Carlo accuracy on the DoseRAD2026 task.
- **评估**: 该工作与自动驾驶感知领域无关，但方法在医学物理中有一定价值。
- **核心贡献**: 提出混合物理-学习质子剂量计算引擎。
- **创新点**: 可微物理引擎与残差网络结合。
- **结果**: 在剂量预测任务中达到高精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Architecture category. Hybrid method: a physics-based analytical pencil-beam (PB) dose engine followed by a 3-D convolutional residual-correction network (RepVGG-U-Net). We addressed the DoseRAD2026 proton dose-prediction task with PyDoseRT Proton, a GPU-accelerated engine implemented in PyTorch and augmented by a learned residual toward Monte Carlo (MC) accuracy. A double-Gaussian PB kernel was calibrated to GATE/Geant4 integrated depth doses in water in two stages: a classical per-energy curve fit, then a gradient-based fit of the full 3-D dose through the PyTorch physics engine as it retains a differentiable execution path for gradient-based optimization of dose-dependent objectives. The engine computes each beamlet on a beam's-eye-view (BEV) lattice with variance-preserving Gaussian splitting, an analytic nuclear halo, and a Fermi-Eyges heterogeneity term, then rotates the result into the patient frame. Additionally, a compact residual U-Net predicts an additive correction in BEV space. It is conditioned on voxelwise material-label embeddings, a discrete energy embedding and spot size. The same model was used for all anatomical sites (thoracic and abdominal). It was trained with a patient-space L1 objective emphasizing the scored high-dose region and multi-scale BEV deep supervision. The submitted CT configuration obtained preliminary-test beamlet MAE 0.0066, image-z IDD distance 0.0025, plan MAE 0.0049, 98.30\% gamma pass rate (1\%/1 mm), and DVH error 0.460.

</details>

---

## Autonomous Driving

### 1. MeRoPE: Metric Rotary Position Embedding for Camera-Controlled Video Generation **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2609.01252](https://arxiv.org/abs/2609.01252)  · [📄 PDF](https://arxiv.org/pdf/2609.01252)
- **作者**: Zhijian Qiao, Xinjiang Wang, Jiajie Chen et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.RO
- **摘要（中）**: ①针对相机控制视频生成中，现有位置编码在真实尺度相机轨迹下导致注意力对数无界增长的问题。②提出MeRoPE，一种保范数的相对相机编码，通过正交旋转块编码射线方向，将度量位移映射为多频旋转相位，并添加视差锚定对应先验。③相比齐次投影编码，MeRoPE严格保持特征范数，限制注意力对数，并对全局刚体变换不变。④在nuScenes和PanShot上，MeRoPE在相机控制上优于先前编码，生成运动与姿态一致性最佳。
- **摘要（英）**: This paper addresses the scale-dependent failure of positional encodings in camera-controlled video generation. MeRoPE is a norm-preserving relative camera encoding that encodes ray orientations and metric displacements with rotation blocks and multi-frequency phases. It achieves stronger camera control and consistency on nuScenes and PanShot.
- **评估**: 该工作对自动驾驶场景生成和感知有重要价值，方法设计严谨，实验充分。
- **核心贡献**: 提出一种保范数的度量旋转位置编码。
- **创新点**: 结合正交旋转块与视差锚定先验。
- **结果**: 在多个数据集上优于先前编码。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In camera-controlled video generation, geometry-aware positional encodings condition tokens on camera extrinsics and per-token viewing rays. Existing schemes, however, have a scale-dependent failure mode on real-world metric camera trajectories: homogeneous projective encodings cause attention logits and feature norms to grow unbounded with physical translation baselines. We propose MeRoPE (Metric Rotary Position Embedding), a norm-preserving relative camera encoding for attention. MeRoPE encodes relative orientations between calibrated viewing rays with orthogonal rotation blocks, maps raw metric displacements into multi-frequency rotary phases, and adds a disparity-anchored correspondence prior along the epipolar arc. This design strictly preserves feature norms, bounds pre-softmax attention logits regardless of the physical translation scale, and maintains exact invariance to global rigid coordinate changes. Across nuScenes and PanShot, which cover large-baseline trajectories and diverse camera optics, respectively, MeRoPE achieves stronger camera control than prior encodings, with the best consistency between generated camera motion and conditioning poses in both rotation and translation. Code will be made publicly available.

</details>

### 2. CoLT-Drive: Counterfactual Long-Tail Benchmarking and Knowledge-Preserving Adaptation for Driving Affordance Prediction **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.75)

- **arXiv ID**: [2609.00242](https://arxiv.org/abs/2609.00242)  · [📄 PDF](https://arxiv.org/pdf/2609.00242)
- **作者**: Zhengxu Tang, Guofeng Cui, Ziyu Gong et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/tangzhengxu/CoLT-Drive](https://github.com/tangzhengxu/CoLT-Drive)
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI, cs.CL
- **摘要（中）**: ①针对自动驾驶长尾场景中，仅识别罕见对象不足以决策，需推断其对可行动作的影响的问题。②提出CoLT-Drive基准和KPA适配框架，KPA结合结构化提示、SLERP专家合并和RegMoE模块，保留开放世界知识并分配轻量适配能力。③相比传统微调，KPA在保持预训练知识的同时提升决策级预测。④在CoLT-Drive上，KPA显著提升小VLM的驾驶决策性能。
- **摘要（英）**: This paper addresses the limitation of rare-object recognition in long-tail driving by formalizing decision-level affordance prediction. CoLT-Drive is a counterfactual benchmark, and KPA is a knowledge-preserving adaptation framework with prompting and RegMoE. KPA improves small VLM performance on driving decisions.
- **评估**: 该工作对自动驾驶安全决策有重要贡献，基准和框架设计新颖，实验有说服力。
- **核心贡献**: 提出长尾驾驶决策基准和知识保留适配框架。
- **创新点**: 结合反事实基准与RegMoE模块。
- **结果**: 在CoLT-Drive上显著提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-tail autonomous driving failures are often framed as rare-object recognition errors. We argue that this view is incomplete: the decision-critical question is not only whether a model recognizes an unusual object, but whether it infers how that object changes the ego vehicle's feasible high-level actions. We formalize this problem as decision-level driving affordance prediction, where a model maps a front-view image, ego-motion history, and navigation command to a structured longitudinal--lateral meta-action. To evaluate this capability, we introduce CoLT-Drive, a 3,536-sample counterfactual long-tail benchmark that inserts rare objects into otherwise fixed driving scenes and measures whether models predict acceptable action pairs. To improve deployable small VLMs, we propose KPA, a knowledge-preserving adaptation framework that combines structured perception-to-decision prompting, SLERP-based expert merging, and RegMoE, a regime-aware LoRA mixture-of-experts module. KPA preserves the pretrained model's open-world knowledge while allocating lightweight adaptation capacity to different driving decision regimes. Experiments on an in-domain driving split and CoLT-Drive show that KPA achieves 60.8\% pair accuracy on CoLT-Drive, outperforming the pretrained Qwen3-VL-2B baseline (50.3\%) and LoRA SFT (32.4\%) while maintaining competitive in-domain accuracy. Our benchmark and code are available at https://huggingface.co/datasets/tangzx2024/CoLT-Drive and https://github.com/tangzhengxu/CoLT-Drive.

</details>

---

## Tracking

### 1. Beyond the Image Plane: World-Grounded Queries for Multi-Object Tracking **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2609.00924](https://arxiv.org/abs/2609.00924)  · [📄 PDF](https://arxiv.org/pdf/2609.00924)
- **作者**: Orcun Cetintas, Guillem Brasó, Tim Meinhardt et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 这篇论文针对单目视频多目标跟踪中仅依赖图像平面外观和几何导致的深度和空间关系歧义问题，提出PLANET，一种端到端多目标跟踪器，旨在超越图像平面。作者先将现有2D跟踪数据集提升到3D，然后在查询形成时嵌入重建的3D场景几何到特征和位置编码中，形成世界接地查询，并通过辅助3D位置预测任务鼓励查询编码物体位置。互补的双分辨率时间记忆在更长的时间间隔内保留证据。相比已有工作，该方法首次将3D场景几何显式集成到跟踪查询中，实验表明在三个不同基准上达到最先进性能。
- **摘要（英）**: This paper addresses ambiguities in multi-object tracking from monocular videos by introducing PLANET, an end-to-end tracker that forms world-grounded queries by embedding reconstructed 3D scene geometry into features and positional encodings. An auxiliary 3D location prediction task and dual-resolution temporal memory enhance query encoding and evidence preservation. PLANET achieves state-of-the-art performance on three benchmarks.
- **评估**: 该论文创新性地将3D场景几何融入跟踪查询，显著提升多目标跟踪性能，对自动驾驶感知有直接应用价值。
- **核心贡献**: 提出PLANET，首个利用世界接地查询进行端到端多目标跟踪的方法。
- **创新点**: 将重建的3D场景几何嵌入查询形成过程，并引入辅助3D位置预测。
- **结果**: 在三个基准上取得最先进跟踪性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular videos record 3D scenes as sequences of 2D image-plane projections, obscuring depth and spatial relationships. Multi-object trackers localize and associate objects primarily using appearance and geometry observed only in the image plane, inheriting these ambiguities. To address this limitation, we introduce PLANET, an end-to-end multi-object tracker designed to move beyond the image plane. As an enabling step, we lift existing 2D tracking datasets into 3D. We then form world-grounded queries by embedding reconstructed 3D scene geometry into the features and positional encodings used during query formation. An auxiliary 3D location prediction task further encourages the queries to encode object positions during training. A complementary dual-resolution temporal memory preserves this evidence across longer temporal gaps. As a result, PLANET achieves state-of-the-art performance across three diverse benchmarks.

</details>

---

## 3D Detection

### 1. Instance-Guided Report Anchoring for Text-Free 3D Abnormality Segmentation in Chest CT **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2609.00447](https://arxiv.org/abs/2609.00447)  · [📄 PDF](https://arxiv.org/pdf/2609.00447)
- **作者**: Zhenyu Bu, Haoyan Ding, Chushu Shen et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对胸部CT异常分割中，专家体素级标注成本高，而放射报告可提供实例级指导的问题。②提出IGRA模块，将每个异常实例表示锚定到对应报告发现嵌入，训练后丢弃文本组件，实现纯图像推理。③相比现有视觉-语言方法，IGRA无需推理时文本输入，并支持多类别同时预测。④在ReXGroundingCT上，IGRA将Dice从25.25提升至30.93，相对提升22.5%。
- **摘要（英）**: This paper addresses the high cost of voxel-level labels in chest CT segmentation by leveraging radiology reports. IGRA anchors instance representations to report findings during training and discards text at inference. It improves Dice by 22.5% over image-only baselines.
- **评估**: 该工作对医学影像分析有贡献，方法可迁移至其他多模态任务，但相关性一般。
- **核心贡献**: 提出实例引导的报告锚定模块。
- **创新点**: 训练时锚定文本，推理时纯图像。
- **结果**: Dice提升22.5%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D abnormality segmentation in chest CT requires dense spatial supervision, but obtaining expert voxel-level labels is costly. Radiology reports, however, are routinely generated during clinical interpretation and contain instance-specific descriptions that can provide additional guidance without new dense annotation. Existing vision-language grounding methods typically require report-derived findings at inference, making localization dependent on paired text and limiting each forward pass to a queried finding. We propose Instance-Guided Report Anchoring (IGRA), a model-agnostic module that preserves the correspondence between each annotated abnormality instance and the report finding that describes it. IGRA pools each instance representation and anchors it to the corresponding finding embedding during training; all text-related components are discarded at inference. We further reformulate free-text grounding on ReXGroundingCT as multi-label volumetric segmentation by merging same-category instances, allowing all abnormality categories to be predicted in one image-only forward pass. IGRA improves Dice by 22.5% over the strongest image-only baseline (30.93 vs. 25.25) and is comparable to VoxTell on the single-finding subset (30.29 vs. 30.43). Applied unchanged to four standard 3D segmentation backbones, IGRA improves Dice and hit rate across all architectures. Zero-shot evaluation on LIDC-IDRI, PleThora, and a private in-house dataset further shows consistent gains over image-only baselines.

</details>

---

## Object Detection

### 1. Does This Moment Justify the Recommendation? Counterfactual Behavior-Grounded Evidence Retrieval for Personalized Video Recommendation **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.00996](https://arxiv.org/abs/2609.00996)  · [📄 PDF](https://arxiv.org/pdf/2609.00996)
- **作者**: Xin Liu
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-01 · **分类**: cs.CV
- **摘要（中）**: ①针对个性化视频推荐中，时间定位检索到的片段是否构成对特定用户的有效推荐证据这一问题。②提出了反事实行为证据检索任务，并构建了CBGER-10K数据集，包含5000对受控事实-反事实样本；同时提出CBGER框架，解耦片段级定位与视频级证据估计，并通过结构化反事实监督学习。③相比现有工作，首次将反事实推理引入个性化视频推荐与时间定位的结合，并严格分离证据位置与证据存在性。④CBGER在五个基线上达到0.4432 MRR、0.6977配对准确率和0.6987干预一致性，优于QD-DETR。
- **摘要（英）**: This paper addresses whether a retrieved moment constitutes valid evidence for recommending a video to a specific user, proposing counterfactual behavior-grounded evidence retrieval with the CBGER-10K dataset and a framework that decouples localization from evidence estimation. It achieves superior MRR and consistency over baselines, highlighting the importance of counterfactual supervision.
- **评估**: 该论文创新性地将反事实推理应用于视频推荐与时间定位的交叉领域，但研究主题与自动驾驶感知相关性较低。
- **核心贡献**: 提出了反事实行为证据检索任务及CBGER-10K基准和CBGER框架。
- **创新点**: 将反事实推理引入个性化视频推荐证据验证。
- **结果**: 在多个基线上显著提升证据检索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Personalized video recommendation predicts user preference at the video level, while temporal video grounding localizes query-relevant moments. However, strong localization does not establish whether the retrieved moment constitutes valid evidence for recommending the video to a particular user. We study counterfactual behavior-grounded evidence retrieval, which separates where personalized evidence occurs from whether such evidence exists and evaluates whether model predictions respond consistently when that evidence is replaced. We introduce CBGER-10K, containing 5,000 controlled factual--counterfactual pairs for 3,026 users, where each pair replaces only the focal behavior-supported segment while preserving the user, temporal position, and hard distractors. We further propose CBGER, a compact framework that decouples segment-level localization from video-level evidence estimation and learns both through structured counterfactual supervision. CBGER achieves $0.4432$ MRR, $0.6977$ Pair Accuracy, and $0.6987$ Intervention Consistency across five adapted personalized-highlight and temporal-grounding baselines. Notably, compared with QD-DETR, its MRR improvement is not statistically significant, while Pair Accuracy improves by $11.03$ points. These results show that accurate temporal localization does not necessarily imply reliable personalized evidence existence, motivating explicit evaluation of Whether alongside Where.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 10 |
| Multimodal | 10 |
| Vision Transformer | 7 |
| Network Pruning | 6 |
| Self-supervised Vision | 5 |
| Video Understanding | 4 |
| Multi-camera Perception | 4 |
| Open-set Detection | 2 |
| BEV | 2 |
| Autonomous Driving | 2 |
| Tracking | 1 |
| 3D Detection | 1 |
| Object Detection | 1 |
| **总计** | **55** |