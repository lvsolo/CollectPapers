# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-09-02  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 73 篇（其中 73 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (10篇)
- [Multimodal](#multimodal) (10篇)
- [Object Detection](#object-detection) (9篇)
- [Multi-camera Perception](#multi-camera-perception) (9篇)
- [Video Understanding](#video-understanding) (7篇)
- [Self-supervised Vision](#self-supervised-vision) (6篇)
- [Vision Transformer](#vision-transformer) (5篇)
- [Continual Learning](#continual-learning) (4篇)
- [Open-set Detection](#open-set-detection) (3篇)
- [3D Detection](#3d-detection) (3篇)
- [Autonomous Driving](#autonomous-driving) (3篇)
- [Neural Architecture Search](#neural-architecture-search) (1篇)
- [Knowledge Distillation](#knowledge-distillation) (1篇)
- [Occupancy](#occupancy) (1篇)
- [Network Pruning](#network-pruning) (1篇)

## VLM

### 1. Partition-Aware Unlearning for Removing Spurious Correlations in Large Vision-Language Models **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2608.29996](https://arxiv.org/abs/2608.29996)  · [📄 PDF](https://arxiv.org/pdf/2608.29996)
- **作者**: Aditi Sarker, Nazreen Shah, Rafi Ibn Sultan et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.AI, cs.LG
- **摘要（中）**: 这篇论文针对大型视觉语言模型（LVLMs）中利用虚假物体-背景相关性进行预测的问题，即模型依赖上下文捷径而非物体相关视觉证据。作者提出了PURGE框架，包含结构化数据集构建策略和分区感知遗忘方法，通过分区数据选择性移除虚假关联，同时保留物体基础能力。相比现有基准，该方法提供了对捷径依赖的受控诊断和缓解手段。实验表明该框架能有效减少虚假相关性引起的错误，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the issue of LVLMs exploiting spurious object-background correlations, leading to shortcut-based predictions. The authors propose PURGE, a framework with structured dataset construction and partition-aware unlearning to selectively remove spurious associations while preserving object-based capabilities. It offers controlled diagnosis and mitigation beyond existing benchmarks, though specific quantitative results are not detailed in the abstract.
- **评估**: 该论文针对LVLM鲁棒性中的关键问题，提出了系统性的构建和缓解框架，对理解模型决策机制有重要价值。
- **核心贡献**: 提出了PURGE框架，用于构建、基准测试和缓解LVLMs中的虚假相关性失败。
- **创新点**: 引入分区感知遗忘机制，利用结构化数据分区选择性去除虚假关联。
- **结果**: 有效减少虚假相关性引起的错误，但具体性能数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) achieve strong performance across many multimodal tasks; however, they often exploit spurious object-background correlations, resulting in predictions driven by contextual shortcuts rather than object-relevant visual evidence. Despite growing interest in hallucination and robustness evaluation, existing benchmarks provide limited control over whether model predictions are grounded in the target object or induced by correlated background cues. In this work, we introduce PURGE (\underline{P}artition-aware \underline{U}nlearning for \underline{R}emoving spurious-correlation \underline{G}enerated \underline{E}rrors), a framework for constructing, benchmarking, and mitigating spurious-correlation-induced failures in LVLMs. The framework consists of: -- (1) Structured dataset construction wherein we develop three complementary structured data construction strategies that partition examples by object-relevant evidence and spurious background cues, enabling controlled diagnosis of shortcut reliance; and -- (2) Partition-aware unlearning, which uses these partitions to selectively remove spurious object-background associations while preserving object-based reasoning. We evaluate the \algo~framework across multiple LVLMs, including LLaVA-1.6-7B, Qwen3-VL-8B-Instruct, and Qwen3.5-9B, together with CLIP as a vision-language encoder, on a diverse suite of benchmarks, including CHAIR, POPE, Causal-HalBench, MM-SpuBench, AMBER, MMHal, and Waterbirds. Our results show that PURGE consistently reduces hallucinations and spurious-correlation-driven errors while maintaining or improving overall performance in most evaluated settings, providing both a reusable evaluation protocol and an effective mitigation framework for more reliable LVLMs.

</details>

### 2. Hallucination Mitigation for Large Vision-Language Models via Implicit Feature Stabilization **⭐⭐⭐⭐** (相关度: 65%, 质量: 0.8)

- **arXiv ID**: [2608.29924](https://arxiv.org/abs/2608.29924)  · [📄 PDF](https://arxiv.org/pdf/2608.29924)
- **作者**: Aditi Sarker, Rafi Ibn Sultan, Hui Zhu et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.AI, cs.LG
- **摘要（中）**: 这篇论文针对LVLMs中的幻觉问题，将其归因于特征不稳定性，即输入轻微扰动导致嵌入大幅变化。作者提出INFUSE框架，通过微调将扰动不变性融入模型权重，无需推理时干预，并利用双向对比目标对齐跨模态表示。相比显式稳定方法，该方法在部署时无额外开销。理论上证明了锚点偏差随视图数K以1/√K速率缩小，并在Lipschitz解码器下约束输出变化。实验显示幻觉率随特征稳定性提升而下降。
- **摘要（英）**: This paper addresses hallucination in LVLMs by linking it to feature instability under input perturbations. The INFUSE framework builds perturbation-invariance into model weights during fine-tuning, avoiding inference-time interventions, and aligns representations across modalities with bidirectional contrastive objectives. Theoretical results show anchor deviation shrinks at 1/√K rate, and experiments demonstrate reduced hallucination rates with improved stability.
- **评估**: 该论文提供了幻觉问题的理论解释和实用解决方案，具有较高的学术和实际价值。
- **核心贡献**: 提出INFUSE框架，通过隐式特征稳定化缓解LVLM幻觉。
- **创新点**: 将扰动不变性融入权重，实现部署时零额外开销的稳定化。
- **结果**: 幻觉率随特征稳定性提升而下降，理论保证锚点偏差收敛。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) are prone to hallucinations: they fluently describe objects, attributes, and scenes that are not in the image. We connect part of this failure to a measurable property of their representations, feature instability, where mild semantics-preserving perturbations of the input cause large changes in the learned embeddings; hallucination rates rise together with this variability. Existing stability-motivated remedies are explicit, in the sense that they intervene at inference time through latent steering or constrained decoding, and pay for it on every query. We propose implicit stabilization instead: perturbation-invariance is built into the model weights during fine-tuning, and nothing extra runs at deployment. Our framework, INFUSE, first stabilizes visual and textual representations around perturbation-averaged and ground-truth anchors, then aligns the stabilized representations across modalities with bidirectional contrastive objectives. We prove that the anchor's root-mean-square deviation from the perturbation-mean representation shrinks at rate $1/\sqrt{K}$ in the number of views, and that under a Lipschitz decoder, this bounds how much any perturbation can change the model's hallucination behavior. On LLaVA-1.5, LLaVA-1.6, and Qwen3-VL-8B-Instruct, INFUSE reduces AMBER CHAIR by 46-63% relative to each base model, improves ObjHal, MMHal, HallusionBench, and POPE, and preserves VQA-v2 and TextVQA, all with no inference-time overhead.

</details>

### 3. SpanCalib-VLM: Calibrated Hallucination Span Detection in Vision-Language Models **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.29974](https://arxiv.org/abs/2608.29974)  · [📄 PDF](https://arxiv.org/pdf/2608.29974)
- **作者**: Amanuel Gizachew Abebe, Yasmin Moslem
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.CL
- **摘要（中）**: 这篇论文针对LVLMs中幻觉跨度检测的准确性和校准问题，提出SpanCalib-VLM混合双系统，结合判别式序列标注器（XLM-RoBERTa-Large与SigLIP融合）和生成式VLM（Qwen3.5-4B-SHROOM-SFT）。通过Union-Calibrated Fusion策略，用序列标注器的校准概率重新评分生成模型的候选跨度。在SHROOM-Visions英语评估集上，集成达到Pearson校准相关0.41、整体IoU 0.39、干净响应IoU 0.91和检测准确率70.7%。相比单一模型，该方法平衡了召回率和校准性。
- **摘要（英）**: This paper addresses hallucination span detection in LVLMs with a hybrid dual-system, SpanCalib-VLM, combining a discriminative sequence tagger and a generative VLM via Union-Calibrated Fusion. It achieves Pearson calibration correlation of 0.41, overall IoU of 0.39, clean-response IoU of 0.91, and 70.7% accuracy on SHROOM-Visions. The approach balances recall and calibration better than single models.
- **评估**: 该论文针对共享任务提供了有效的混合方案，在检测和校准上表现均衡，但创新性有限。
- **核心贡献**: 提出SpanCalib-VLM混合系统，结合判别式和生成式模型提升幻觉跨度检测与校准。
- **创新点**: 采用Union-Calibrated Fusion策略，用判别式模型校准生成式模型的候选跨度。
- **结果**: 在SHROOM-Visions上达到0.41校准相关和0.39 IoU，准确率70.7%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting hallucinations in Large Vision-Language Models (LVLMs) requires both accurate span localization and well-calibrated confidence scores. Fine-tuned generative VLMs excel at identifying hallucinated text spans but suffer from overconfidence and high inference latency. Discriminative sequence taggers offer deterministic speed and superior calibration but exhibit conservative span recall. We present SpanCalib-VLM, a hybrid dual-system for the SHROOM-Visions Shared Task that combines a multimodal sequence tagger, consisting of XLM-RoBERTa-Large fused with a SigLIP vision encoder via cross-attention, with our fine-tuned generative VLM (Qwen3.5-4B-SHROOM-SFT). Through a Union-Calibrated Fusion strategy, candidate spans from the generative model are re-scored with calibrated probabilities from the sequence tagger. On the SHROOM-Visions English evaluation split, our ensemble achieves a Pearson calibration correlation of 0.41 and an overall IoU of 0.39, with a clean-response IoU of 0.91} and overall detection accuracy of 70.7%. We make our model weights and code publicly available.

</details>

### 4. Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models **⭐⭐⭐** (相关度: 55%, 质量: 0.65)

- **arXiv ID**: [2608.29590](https://arxiv.org/abs/2608.29590)  · [📄 PDF](https://arxiv.org/pdf/2608.29590)
- **作者**: Yusuke Hirota, Michael Ross Boone, Arun George Zachariah et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对强安全护栏下LVLMs的社会偏见评估问题，现有基准因模型拒绝回答而失效。作者改变评估范式，将任务与人物解耦，使用不涉及人物的提示（如写虚构故事）并附加图像作为临时用户信息，隐式提供人口统计线索，比较不同人口统计下的输出。在故事生成、术语解释和考试式QA三个任务上，对20个LVLMs评估发现所有模型都非预期地使用人口统计信息。该方法避免了护栏模型的拒绝，实现可靠偏见测量。
- **摘要（英）**: This paper addresses societal bias evaluation in LVLMs with strong guardrails, where existing benchmarks fail due to refusals. The proposed method decouples tasks from depicted persons, using person-irrelevant prompts with images as implicit demographic cues, enabling reliable bias measurement. Across 20 LVLMs, all models undesirably use demographic information, demonstrating the method's effectiveness.
- **评估**: 该论文提出了创新的偏见评估范式，解决了护栏模型的评估难题，但领域相关性较低。
- **核心贡献**: 提出护栏无关的社会偏见评估方法，通过任务解耦实现可靠测量。
- **创新点**: 将任务与人物解耦，利用隐式人口统计线索避免模型拒绝。
- **结果**: 在20个LVLMs上发现所有模型均使用人口统计信息，验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a societal bias evaluation method for large vision-language models (LVLMs) in the era of strong safety guardrails. Existing benchmarks rely on prompts that ask models to infer attributes of people in images (e.g., "Is this person a CEO or a secretary?"). However, we find that LVLMs with strong guardrails, such as GPT and Claude, often refuse these prompts, making evaluations unreliable. To address this, we change the prior evaluation paradigm by decoupling the task from the depicted person: instead of inferring person's attributes, we use prompts that do not ask about the person (e.g., "Write a fictional story about an imaginary person.") and attach the image as provisional user information to implicitly provide demographic cues, then compare outputs across user demographics. Instantiated across three tasks --- story generation, term explanation, and exam-style QA --- our method avoids refusals even in guardrailed LVLMs, enabling reliable bias measurement. Applying it to 20 recent LVLMs, both open-source and proprietary, we find that all models undesirably use user demographic information in person-irrelevant tasks; for instance, characters in stories are often portrayed as mechanic for male users and nurse for female users. Although still biased, proprietary models like GPT-5 show lower bias than open-source ones. We analyze potential factors behind this gap, discussing continuous model monitoring and improvement as a possible contributor for reducing bias.

</details>

### 5. VisER: Visual Evidence and Reliance for Object Hallucination Detection in LVLMs **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2608.30480](https://arxiv.org/abs/2608.30480)  · [📄 PDF](https://arxiv.org/pdf/2608.30480)
- **作者**: Afsaneh Hasanebrahimi, Hanxun Huang, Christopher Leckie et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.LG
- **摘要（中）**: 这篇论文针对LVLMs中物体幻觉检测问题，指出现有训练无关检测器使用内部信号时存在源混淆，无法区分支持来自物体视觉证据还是文本前缀。作者提出VisER，一种训练无关的双侧度量，从视觉证据（物体-上下文兼容性是否由图像token支持）和视觉依赖（物体支持是否更多来自图像而非前缀）两个互补视角评估。相比现有方法，VisER在困难案例中能更好区分幻觉物体。实验显示结合这些视角提高了检测性能，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses object hallucination detection in LVLMs, noting that existing training-free detectors suffer from source confounding. VisER proposes a two-sided metric evaluating visual evidence and visual reliance to distinguish hallucinated objects. It improves detection in difficult cases by separating image-based support from prefix-based support, though specific results are not detailed.
- **评估**: 该论文针对幻觉检测中的关键缺陷提出了创新度量，对提升模型可靠性有实际意义。
- **核心贡献**: 提出VisER，一种训练无关的双侧度量，用于物体级幻觉检测。
- **创新点**: 区分视觉证据和视觉依赖，解决内部信号的源混淆问题。
- **结果**: 结合两个视角提升幻觉检测性能，具体数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object hallucination remains a persistent reliability issue in large vision-language models, where generated object mentions may sound plausible but lack visual grounding. Recent training-free detectors use internal signals such as token likelihood, attention, visual confidence, or image-text similarity to identify hallucinated objects. These signals are useful, but they are often source-confounded. They measure how strongly an object is supported inside the model without distinguishing whether that support comes from object-specific visual evidence or the generated text prefix. In difficult cases, a hallucinated object can still receive high internal support because it fits the scene, is associated with nearby visual cues, or follows naturally from the generated text prefix. We propose VisER, a training-free two-sided metric for object-level hallucination detection. VisER evaluates each generated object mention from two complementary views. Visual Evidence measures whether object-context compatibility is backed by object-specific evidence from image tokens. Visual Reliance measures whether the object is supported more by the image than by the generated prefix. Combining these views gives a more source-aware grounding score, while avoiding additional object-level verification generations. Across multiple LVLMs and benchmarks, VisER improves AUROC and AUPR over a range of baselines.

</details>

### 6. Frontier vision-language models have overtaken young adults at detecting AI-generated portraits -- but not their calibration **⭐⭐⭐** (相关度: 50%, 质量: 0.6)

- **arXiv ID**: [2608.30210](https://arxiv.org/abs/2608.30210)  · [📄 PDF](https://arxiv.org/pdf/2608.30210)
- **作者**: Sunwhi Kim, Sunyul Kim, Meounggun Jo et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.HC, cs.CV
- **摘要（中）**: 这篇论文评估了19个VLM在检测AI生成人脸肖像方面的性能，与1667名成年人（85%准确率）对比。2026年6月的14个模型仅匹配20-30岁成年人，而7月的5个新模型中gpt-5.6-sol达到92.8%平衡准确率，超过20岁成年人（88.5%），claude-fable-5检测所有AI图像且平均91.9%。模型灵敏度显著超过年轻人（d'达3.4 vs 2.4），但校准不佳，标准偏差从-1.10到+1.45，而人类接近零。该研究揭示了VLM在检测能力上的超越和校准缺陷。
- **摘要（英）**: This paper benchmarks 19 VLMs on AI-generated portrait detection, finding that July-2026 models like gpt-5.6-sol (92.8% accuracy) surpass young adults (88.5%), with sensitivity d' up to 3.4. However, model calibration is poor, with criteria spread from -1.10 to +1.45, unlike humans near zero. The study highlights VLMs' superior detection but inadequate calibration.
- **评估**: 该论文提供了VLM检测能力的实证评估，但领域相关性较低，且未来日期设定影响可信度。
- **核心贡献**: 系统评估了VLM在AI生成人脸检测中的性能和校准，与人类对比。
- **创新点**: 使用身份匹配的肖像数据集和统一协议进行跨模型人类对比。
- **结果**: 最新VLM检测准确率超过年轻人，但校准偏差显著。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> AI image generators now create face portraits that are hard to tell from real photographs. Vision-language models (VLMs) are increasingly proposed to flag such images. We benchmarked 19 VLMs on the same 198 face portraits -- real photographs and identity-matched ChatGPT-4o and Imagen 3 versions -- under the same task as our earlier study of 1,667 adults (85% correct overall; accuracy fell steeply with age). The June-2026 cohort of 14 models only matched adults in their 20s-30s. Four weeks later the ceiling broke. Among five July-2026 releases under the identical protocol, gpt-5.6-sol reached 92.8% balanced accuracy (five-draw mean 92.1%), clearly above adults in their 20s (88.5%), and claude-fable-5 detected every AI image while averaging 91.9%. Model sensitivity now exceeds young adults decisively (d' up to 3.4 versus ~ 2.4). What has not been overtaken is human calibration. Model criteria spread from c = -1.10 to +1.45 while humans sit near zero at every age; both new leaders are biased (+0.44, -0.97), and only a few mid-ranked models approach the human balance. Changing the labelled examples still flipped about one answer in four. The best machines now out-see young adults here, without matching the human balance between suspicion and trust.

</details>

### 7. Centering before Pruning: Lightweight Geometry Correction for Diversity-Based Visual Token Pruning in LVLMs **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.30263](https://arxiv.org/abs/2608.30263)  · [📄 PDF](https://arxiv.org/pdf/2608.30263)
- **作者**: Shunjie Wen, Jaeyeon Lee, Dong-Wan Choi
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对大型视觉语言模型（LVLMs）中视觉token序列冗长且高度冗余导致推理成本高的问题，以及基于多样性的剪枝方法中原始token特征余弦相似度集中在正值区间、难以区分非冗余token的缺陷。②提出Cen-Prune方法，在计算余弦相似度前对token特征进行中心化处理，以揭示更丰富的成对结构，并结合原始几何中隐含的全局显著性偏好来平衡多样性与显著性。③改进点在于揭示了多样性与显著性在原始几何中的纠缠关系，并通过中心化与原始几何的互补使用来提升剪枝性能。④实验表明，中心化单独使用会降低剪枝性能，但Cen-Prune通过结合两者，在保持多样性的同时保留了语义信息，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the high inference cost of LVLMs due to redundant visual token sequences and the limited discriminability of cosine similarity in diversity-based pruning. It proposes Cen-Prune, which centers token features before similarity computation and integrates global distinctiveness to balance diversity and semantic informativeness. The method reveals the entanglement of diversity and distinctiveness, improving pruning performance over raw geometry alone.
- **评估**: 该论文对视觉token剪枝中的几何特性进行了深入分析，提出了简单有效的改进方案，对LVLMs效率优化有参考价值。
- **核心贡献**: 提出了Cen-Prune框架，通过中心化几何与显著性偏好结合，提升了多样性剪枝的性能。
- **创新点**: 首次揭示了多样性与显著性在原始token几何中的纠缠，并设计互补策略。
- **结果**: 中心化单独使用性能下降，但Cen-Prune结合两者后剪枝性能提升，具体数值未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (LVLMs) incur substantial inference costs due to their long and highly redundant visual-token sequences. Diversity-based pruning mitigates this cost by selecting token subsets based on pairwise cosine similarity. We find, however, that similarities between raw visual tokens are strongly concentrated in the positive range, limiting their ability to distinguish non-redundant tokens. A natural way to improve this resolution is to center token features before computing cosine similarity. Centering indeed reveals a substantially richer pairwise structure, yet unexpectedly degrades pruning performance when used alone. We show that this apparent contradiction arises because the raw geometry does more than represent pairwise diversity: it also implicitly favors globally distinctive tokens, which tend to contain semantically informative content. Centering better resolves subset diversity but loses this useful token-wise preference, revealing that diversity and distinctiveness are entangled in the raw geometry. Based on this analysis, we propose the \textbf{Cen}tered Geometry \textbf{Prune}r (Cen-Prune), which measures subset diversity using centered cosine similarity while retaining raw-space distinctiveness as a complementary token-wise preference. This lightweight, plug-and-play correction leaves the underlying selection mechanism unchanged and incurs negligible computational overhead. Extensive experiments across multiple image- and video-understanding benchmarks and LVLM architectures demonstrate that Cen-Prune provides robust improvements in overall performance across existing diversity-based pruners.

</details>

### 8. DICS: Exploring Data Intrinsic Consistency for Visual Instruction Selection **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.30209](https://arxiv.org/abs/2608.30209)  · [📄 PDF](https://arxiv.org/pdf/2608.30209)
- **作者**: Yuyang Hong, Jinhui Guo, Jiaqi Gu et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/cqu-student/DICS](https://github.com/cqu-student/DICS)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对视觉指令微调中在固定比例下选择最优数据子集的问题，现有方法忽略样本内部一致性。②提出数据内在一致性（DIC）指标，包括视觉信息一致性（VIC）和响应信息一致性（RIC），并构建DICS自适应选择方法，平衡高内部一致性和全局多样性。③改进点在于从样本级一致性角度筛选数据，优于仅依赖分布多样性或启发式过滤的方法。④实验表明DICS在多种数据规模下优于SOTA方法，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses optimal subset selection in visual instruction tuning by proposing Data Intrinsic Consistency (DIC), a self-scoring metric for sample-level inter-component consistency. DICS adaptively selects data balancing high consistency and global diversity. It consistently outperforms SOTA methods across diverse dataset scales.
- **评估**: 该论文对多模态数据选择有贡献，但与自动驾驶核心领域相关性一般。
- **核心贡献**: 提出了DIC指标和DICS选择方法，提升视觉指令微调数据效率。
- **创新点**: 首次引入样本级内部一致性用于数据选择。
- **结果**: 在多种数据规模下优于SOTA，具体数值未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual instruction tuning is crucial for advancing the vision-language alignment and instruction-following capabilities of Vision-Language Models (VLMs). However, identifying optimal subsets under a fixed ratio constraint from rapidly expanding datasets remains a significant bottleneck. While existing methods largely depend on distribution diversity or heuristic filtering, they often overlook the internal coherence within individual samples. To bridge this gap, we propose Data Intrinsic Consistency (DIC), a self-scoring metric designed to quantify the sample-level inter-component consistency. DIC consists of two modules: Visual Information Consistency (VIC), evaluating the alignment between visual content and instructions, and Response Information Consistency (RIC), assessing response coherence relative to the instruction. Building upon DIC, we introduce Data Intrinsic Consistency Selection (DICS), an adaptive data selection method that optimizes the trade-off between high intra-sample consistency and global distributional diversity under varying data budgets. Extensive experiments demonstrate that DICS consistently outperforms state-of-the-art methods across diverse dataset scales and model architectures, surpassing full-dataset fine-tuning while using only 25% of the LLaVA-1.5-665K data. We further curate DICS-6M, a 6M-sample multi-modal instruction corpus that enables the largest-scale visual instruction selection study to date; remarkably, DICS reaches 94.52\% of the official InternVL3-8B-Instruct performance using less than 25\% of its reported training data. Code can be seen at https://github.com/cqu-student/DICS

</details>

### 9. Towards Continual Test-Time Adaptation of Vision-Language Models in Open-Vocabulary Semantic Segmentation **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.29923](https://arxiv.org/abs/2608.29923)  · [📄 PDF](https://arxiv.org/pdf/2608.29923)
- **作者**: Chandler Timm C. Doloriel, Yunbei Zhang, Sarthak Kumar Maharana et al. (8 authors)
- **🏷️ 机构**: ETS Montreal, École de Technologie Supérieure, Montreal, École de technologie supérieure, Université du Québec
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.LG · **📚 被引**: 1
- **摘要（中）**: ①针对开放词汇语义分割（OVSS）在持续测试时分布偏移下视觉-语言对齐脆弱的问题，包括熵最小化导致类崩溃、持续更新侵蚀对齐、冗余梯度浪费计算。②提出DAF框架，包含边际多样性损失、跨模态锚点一致性损失和特征显著性过滤，以稳定熵基适应。③改进点在于通过锚点约束和过滤机制，防止崩溃并减少计算开销。④在五个数据集（包括自动驾驶场景）上，DAF相比源模型在Pascal VOC20-C上mIoU提升超8点，LoveDA上超9点，Foggy Cityscapes上超3点，且保持稳定。
- **摘要（英）**: This paper addresses fragility of vision-language alignment in OVSS under continual test-time shifts. DAF stabilizes entropy-based adaptation with marginal diversity loss, cross-modal anchor consistency, and feature salience filtering. It improves mIoU by over 8 points on Pascal VOC20-C, 9 on LoveDA, and 3 on Foggy Cityscapes, remaining robust.
- **评估**: 该论文直接针对自动驾驶场景的分布偏移问题，方法有效且实验充分，高度相关。
- **核心贡献**: 提出了DAF框架，稳定OVSS在持续测试时适应中的性能。
- **创新点**: 结合多样性损失、锚点一致性和显著性过滤。
- **结果**: 在多个数据集上mIoU提升显著，如Foggy Cityscapes超3点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation (OVSS) relies on vision-language alignment to recognize arbitrary text-defined categories, yet this alignment is fragile under continual test-time distribution shift. Our diagnostic analysis reveals that entropy minimization drives patch-level class collapse, continual updates erode vision-language alignment, and redundant gradients from low-shift samples waste computation. We propose Diversify, Anchor, and Filter (DAF), a stabilization framework that augments entropy-based adaptation with a marginal diversity loss that resists collapse, a cross-modal anchor consistency loss that constrains feature drift relative to a frozen source model, and feature salience filtering that skips low-value backward passes to offset part of the source-anchor overhead. We evaluate on five datasets spanning natural scenes, autonomous driving, underwater imagery, and remote sensing with their corrupted variants. Across the evaluated continual shifts, DAF remains stable where entropy minimization collapses, improving mIoU by over 8 points on Pascal VOC20-C, over 9 points on LoveDA, and over 3 points on Foggy Cityscapes compared to the source model, and is robust to aggressive adaptation and learning rate choices.

</details>

### 10. InspectorGPT: A Comparative Reasoning Enhanced VLM for Comprehensive Industrial Anomaly Detection **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.29783](https://arxiv.org/abs/2608.29783)  · [📄 PDF](https://arxiv.org/pdf/2608.29783)
- **作者**: Weifei Chen, Honghao Zhang, Zhiyuan You et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 针对工业异常检测中传统无监督方法泛化性差和VLM微调后判别能力崩溃的问题，提出了InspectorGPT，一个基于比较推理的VLM框架。通过将查询图像与无缺陷参考图像比较来识别差异，并执行多种检测任务，利用思维链微调和组相对策略优化（GRPO）内化比较推理能力。该方法提供像素级分割，优于仅文本或粗框的现有方法。
- **摘要（英）**: To address poor generalization in industrial anomaly detection and reasoning collapse in fine-tuned VLMs, this paper proposes InspectorGPT, a VLM framework centered on comparative reasoning between query and reference images. It uses CoT fine-tuning and GRPO with verifiable rewards, enabling pixel-level segmentation.
- **评估**: 该工作将比较推理引入工业异常检测，解决了VLM微调中的关键问题，具有实际应用价值。
- **核心贡献**: 提出了一个基于比较推理的VLM框架，实现全面工业异常检测。
- **创新点**: 利用GRPO和CoT内化比较推理，支持像素级分割。
- **结果**: 摘要未提供具体数值，但声称优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Industrial anomaly detection is a critical component of modern manufacturing. Most traditional unsupervised methods rely on modelling normal feature distributions, inherently limiting generalization to unknown categories. To improve generalizability, some recent methods incorporate vision-language models (VLMs) for zero-shot detection via text prompts. However, we observe that reasoning-oriented post-training can cause anomaly discrimination to collapse, with some fine-tuned models performing worse than their base VLMs. Existing methods also provide only textual decisions or coarse boxes, without pixel-level segmentation. A more explicit detection principle comes from human inspection: anomalies are identified by comparing a query image with a defect-free reference. Inspired by this, we propose InspectorGPT, a VLM framework centered on comparative reasoning. Given a normal reference and a query image, InspectorGPT compares them to identify discrepancies and perform multiple inspection tasks with detailed reasoning. We internalize this capability through Chain-of-Thought (CoT) fine-tuning and Group Relative Policy Optimization (GRPO) with tailored, verifiable rewards. We further introduce InspectorGPT-Seg for pixel-level anomaly masks. Segmentation supervision improves anomaly discrimination but weakens semantic reasoning, while joint training fails to balance them. We therefore train the two branches separately and combine them through task-vector fusion. Extensive experiments demonstrate superior multi-dimensional performance and generalization to unseen benchmarks, validating comparative reasoning for comprehensive industrial inspection.

</details>

---

## Multimodal

### 1. TAMI: Temporally Aligned, Missingness-Aware, and Interpretable Multimodal Fusion for Mental Health Assessment in Older Adults with Mild Cognitive Impairment **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2608.30857](https://arxiv.org/abs/2608.30857)  · [📄 PDF](https://arxiv.org/pdf/2608.30857)
- **作者**: Merna Bibars, Bolaji Omofojoye, Allan I. Levey et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对老年MCI患者抑郁和焦虑筛查中多模态融合的时序错位、模态缺失和可解释性不足问题。②提出TAMI框架，在问答段内对齐语音、语言、面部和生理特征，编码模态缺失模式，并基于问题上下文进行融合。③改进点在于联合处理时序对齐、缺失感知和细粒度归因，优于零填充和忽略缺失的方法。④在49名MCI老年人的访谈中，TAMI在抑郁和焦虑检测上取得AUROC 0.68和0.65（摘要未完整给出焦虑值），展示了有效性。
- **摘要（英）**: This paper tackles temporal misalignment, modality dropout, and interpretability in multimodal fusion for mental health screening in older adults with MCI. TAMI aligns features on a shared timeline, encodes missingness, and conditions fusion on question context. It achieves AUROC 0.68 for depression and 0.65 for anxiety in a 49-participant study.
- **评估**: 该论文针对特定医疗场景提出多模态融合方案，但领域相关性较低，方法创新性一般。
- **核心贡献**: 提出了TAMI框架，整合时序对齐、缺失感知和可解释融合。
- **创新点**: 在融合中显式建模模态缺失和问题上下文。
- **结果**: 在MCI老年人数据集上AUROC达0.68（抑郁）和0.65（焦虑）。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Depression and anxiety in older adults with Mild Cognitive Impairment (MCI) are frequently underdiagnosed due to limited access to care. Multimodal analysis of remote clinical interviews is a scalable screening approach, but existing methods have three limitations. First, they do not correct temporal misalignment across multimodal features extracted at different resolutions, inducing spurious cross-modal associations. Second, remote recordings exhibit uneven modality dropout, but missing values are often zero-filled, making them indistinguishable from valid near-zero measurements. Finally, they do not jointly attribute predictions to modalities, questions, and interview moments, limiting fine-grained clinical interpretation. We propose a Temporally-Aligned, Missingness-Aware, Interpretable (TAMI) multimodal fusion framework. TAMI aligns speech, language, facial, and physiological features within question-answer segments on a shared timeline, encodes modality-level missingness over time, and conditions fusion on question context. In interviews with 49 older adults with MCI, TAMI achieved area under the receiver operating characteristic curve (AUROC) scores of 0.68 (depression) and 0.69 (anxiety). Fine-grained temporal alignment of multimodal features produced the largest performance gain ($Δ{\geq}0.1$). Multi-level interpretability analysis revealed that depression classification relied on eyegaze and open-ended questions, while anxiety classification depended on eyegaze and head pose, with attribution uniformly distributed across questions. Using only responses to the open-ended questions (5.1min), the depression model achieved an AUROC score of 0.67, which was not significantly different from using the full interview (19min) ($p>0.05$). Our findings support designing interview protocols centered on open-ended questions for depression screening in older adults with MCI.

</details>

### 2. Modality Disentangled Learning for Incomplete Multimodal Emotion Recognition: A Primitive Memory Distillation Perspective **⭐⭐** (相关度: 10%, 质量: 0.6)

- **arXiv ID**: [2608.30563](https://arxiv.org/abs/2608.30563)  · [📄 PDF](https://arxiv.org/pdf/2608.30563)
- **作者**: Jiaqi Zhang, Zheng Pang, Mengting Li et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/JiaqiZhang-Sengoku/PriMD](https://github.com/JiaqiZhang-Sengoku/PriMD)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对多模态情感识别中模态缺失导致表示不稳定的问题。现有方法将缺失模态整体生成或对齐，忽略了模态内信息的异质性。作者提出Primitive Memory Distillation (PriMD)框架，从模态内视角解耦跨模态共享语义与模态特有细节，并将后者离散化为可学习的语义基元构建记忆库。在模态缺失时，学生模型利用可用模态的共享语义作为查询动态检索基元以补偿缺失信息。该方法在情感识别任务上提升了鲁棒性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the instability of multimodal emotion recognition under missing modalities. Existing methods treat missing modalities holistically, ignoring intra-modal heterogeneity. The authors propose PriMD, which disentangles shared semantics from modality-specific details and discretizes the latter into learnable primitives for memory-based retrieval. It improves robustness but no quantitative results are reported in the abstract.
- **评估**: 该论文与自动驾驶感知领域相关性极低，主要面向情感识别，方法虽有新意但缺乏实验数据支撑，整体重要性有限。
- **核心贡献**: 提出PriMD框架，通过模态内解耦和基元记忆检索应对模态缺失问题。
- **创新点**: 从模态内视角区分共享语义与特有细节，并利用记忆库动态补偿缺失模态。
- **结果**: 摘要未提供具体性能数据，仅声称提升鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Emotion Recognition (MER) systems often suffer from missing modalities in real-world scenarios. Existing methods usually generate, align, or distill missing modalities as a whole, overlooking the heterogeneous nature of the information carried by each modality. Such holistic treatment mixes inferable shared semantics with uncertain modality-specific details, yielding unstable representations and degrading robustness. To address this issue, we propose the Primitive Memory Distillation (PriMD) framework. Unlike existing methods, PriMD takes an intra-modal perspective and focuses on how different types of information within a modality differ in recoverability within each modality. PriMD first disentangles cross-modal shared semantics from modality-specific representations, and then discretizes the latter into learnable semantic primitives to construct modality-specific memory banks. When modalities are missing, PriMD is a teacher-student framework that the student model uses the shared semantics of available modalities as queries to dynamically retrieve primitives. It compensates for missing modality-specific information within a constrained memory space and aligns with the teacher model. Extensive experiments on IEMOCAP, CMU-MOSI, and CMU-MOSEI demonstrate that PriMD achieves state-of-the-art performance and consistently stronger robustness across a wide range of missing-modality settings, while mitigating the instability caused by holistic feature inference. Our code and project website are available at https://github.com/JiaqiZhang-Sengoku/PriMD and https://jiaqizhang-sengoku.github.io/PriMD/, respectively.

</details>

### 3. SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions **⭐⭐** (相关度: 15%, 质量: 0.7)

- **arXiv ID**: [2608.29607](https://arxiv.org/abs/2608.29607)  · [📄 PDF](https://arxiv.org/pdf/2608.29607)
- **作者**: Zirong Chen, Fuda Ye, Kuan Zhang et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.IR
- **摘要（中）**: 这篇论文针对移动端拍照问答（snap-and-ask）检索在模糊图像和错误文本下的鲁棒性问题。现有基准仅测试干净输入或未隔离配对鲁棒性。作者提出SnapBench基准，包含1145个查询、9085个图库项和53种受控损坏条件，并评估16种多模态检索器。结果显示图像损坏显著降低检索性能，而文本损坏影响有限；还提出MOOR方法进行模态锚定和异常感知重加权。该工作为多模态检索鲁棒性提供了测试平台，但与自动驾驶感知领域关联较弱。
- **摘要（英）**: This paper addresses robustness in snap-and-ask multimodal retrieval under blurry images and noisy text. Existing benchmarks lack paired corruption testing. The authors introduce SnapBench with 1,145 queries and 53 corruption conditions, evaluating 16 retrievers, and propose MOOR for modality-anchored reweighting. It provides a testbed but has limited relevance to autonomous driving.
- **评估**: 该论文聚焦移动端检索，与自动驾驶感知领域相关性低，但基准构建和鲁棒性分析有一定参考价值。
- **核心贡献**: 提出SnapBench基准和MOOR方法，系统评估多模态检索在损坏输入下的鲁棒性。
- **创新点**: 首次提供配对损坏条件下的多模态检索基准，并引入异常感知重加权策略。
- **结果**: 发现图像损坏严重降低检索性能，MOOR方法在鲁棒性上有所提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mobile AI acts as a visual oracle, empowering users to snap a picture of something and ask for information. Snap-and-ask retrieval is now one of the most common entry points for mobile AI, yet photos are often blurry, while text questions may be short or mistyped. Existing benchmarks only test on clean inputs or do not isolate paired robustness in snap-and-ask retrieval. Therefore, we introduce SnapBench, the first paired benchmark for robust snap-and-ask multimodal retrieval, spanning 1,145 queries, 9,085 gallery items under 53 controlled corruption conditions with human annotations. We evaluate 16 multimodal retrievers, covering dual-tower encoders and embedding-based VLMs. Results show that image corruptions substantially degrade retrieval, while text corruptions mainly affect text-only retrieval and have limited impact on joint retrieval. Clean image-only retrieval often outperforms joint retrieval, indicating the coarse-text drag and the lack of cross-modal fallback under noisy inputs. SnapBench provides a controlled testbed for evaluating robust retrieval in snap-and-ask scenarios. We further propose MOOR (Modality-anchored, Outlier-aware, Optimal Reweighting), a simple adaptive fusion approach, highlighting the need for reliability-aware modality calibration in snap-and-ask retrieval.

</details>

### 4. VIBE: Video Instruction-aligned Background music gEneration **⭐⭐** (相关度: 10%, 质量: 0.65)

- **arXiv ID**: [2608.30125](https://arxiv.org/abs/2608.30125)  · [📄 PDF](https://arxiv.org/pdf/2608.30125)
- **作者**: Aryan Vijay Bhosale, Vaibhavi Lokegaonkar, Vishnu Raj et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.SD, cs.AI, cs.CL
- **摘要（中）**: 这篇论文针对视频到音乐生成中缺乏语义控制和指令违反惩罚的问题。现有V2M模型依赖重建目标和静态跨模态条件，导致控制力不足。作者提出VIBE模型，包含深度跨层条件连接机制和全面的奖励建模分类，优化硬约束（如节奏、调性）和软质量（如音乐性、多模态对齐），并采用5阶段训练课程。实验显示VIBE在可控性和指令遵循上增强，但生成保真度与基线相当。该工作与自动驾驶感知领域无关。
- **摘要（英）**: This paper addresses lack of semantic control in video-to-music generation. Existing models rely on reconstruction objectives and static conditioning. The authors propose VIBE with depth-wise cross-layer conditioning and a reward modeling taxonomy with a 5-stage curriculum. It improves controllability but performs comparably on fidelity.
- **评估**: 该论文面向音乐生成，与自动驾驶感知领域完全无关，但方法设计有一定创新性。
- **核心贡献**: 提出VIBE模型，通过动态条件连接和奖励建模提升视频到音乐生成的指令遵循。
- **创新点**: 引入深度跨层条件连接和结构化奖励建模训练课程。
- **结果**: 在可控性和指令遵循上增强，生成保真度与基线相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current video-to-music (V2M) models lack semantic control and fail to penalize instruction violations, largely due to their reliance on reconstruction objectives and the representational bottleneck of static cross-modal conditioning in Diffusion Autoregressive (DAR) architectures. To resolve this, we introduce VIBE, a novel text-and-video-to-music (T+V2M) generation model that leverages: (1) Conditioning Connection, a depth-wise cross-layer conditioning mechanism that dynamically bridges the planning and diffusion refinement heads and (2) a comprehensive reward modeling taxonomy, optimizing for both hard, verifiable constraints (e.g., tempo, key) and soft, subjective qualities (e.g., musicality, multimodal alignment) with a structured 5-stage training curriculum. Upon evaluation using audio-visual alignment, instruction following, and audio quality metrics, along with a subjective human evaluation study, we observe that VIBE demonstrates enhanced controllability and instruction adherence while performing comparably to most evaluated baselines on generation fidelity and multimodal alignment.

</details>

### 5. GarmentWeaver: Schema-Aware Structured Synthesis for Multimodal Sewing Patterns **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.30550](https://arxiv.org/abs/2608.30550)  · [📄 PDF](https://arxiv.org/pdf/2608.30550)
- **作者**: Yinwen Lu, Weihao Luo, Yueqi Zhong
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.AI, cs.CV
- **摘要（中）**: 针对多模态缝纫图案生成中现有方法将服装规格建模为扁平长序列导致结构纠缠和模拟兼容性差的问题，该论文提出GarmentWeaver框架，通过激活服装相关结构分支构建紧凑层次目标，并以结构化方式预测可执行缝纫图案。该框架基于预训练视觉语言模型进行多模态服装理解，并引入可行性感知正则化以鼓励结构有效和模拟兼容的输出。实验表明，GarmentWeaver在准确性和可执行性上优于强基线方法。
- **摘要（英）**: This paper tackles the issue of flat long-sequence modeling in multimodal sewing pattern generation, which entangles structure and parameters, by proposing GarmentWeaver, a schema-aware framework that constructs compact hierarchical targets and predicts executable patterns structurally. It leverages a pretrained vision-language model for multimodal understanding and applies feasibility-aware regularization for valid outputs. Experiments show superior accuracy and executability over strong baselines.
- **评估**: 该论文在服装生成领域有创新，但与自动驾驶感知研究方向无关。
- **核心贡献**: 提出了模式感知的结构化多模态缝纫图案生成框架。
- **创新点**: 通过层次化目标构建和可行性正则化提升图案可执行性。
- **结果**: 在准确性和可执行性上优于强基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Sewing pattern generation aims to infer executable sewing patterns from design cues such as sketches and textual descriptions. As an interpretable and simulation-compatible representation, sewing patterns are particularly valuable for digital garment creation. However, existing methods often model garment specifications as flat long sequences, which entangles garment structure with detailed parameters and leads to redundant components, inaccurate local details, and poor simulation compatibility. In this paper, we present GarmentWeaver, a schema-aware framework for multimodal Sewing pattern generation. GarmentWeaver constructs compact hierarchical targets by activating garment-relevant structural branches and predicts executable Sewing patterns in a structured manner. Specifically, we introduce a schema-aware target construction strategy, build the generator on top of a pretrained vision-language model for multimodal garment understanding, and impose feasibility-aware regularization to encourage structurally valid and simulation-compatible outputs. Extensive experiments show that GarmentWeaver produces more accurate and more executable sewing patterns than strong baselines, while also yielding better simulation results. These findings demonstrate the effectiveness of schema-aware structured generation for reliable multimodal Sewing pattern prediction.

</details>

### 6. Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation **⭐⭐⭐** (相关度: 40%, 质量: 0.75)

- **arXiv ID**: [2608.30163](https://arxiv.org/abs/2608.30163)  · [📄 PDF](https://arxiv.org/pdf/2608.30163)
- **作者**: Ruofan Hu, Shengyang Xu, Minjie Hong et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Collab-Gen/Doc-REFRAG](https://github.com/Collab-Gen/Doc-REFRAG)
- **提交日期**: 2026-08-31 · **分类**: cs.IR, cs.CV
- **摘要（中）**: 针对现有多模态RAG模型在真实多图像场景中准确率有限且处理大量检索图像计算开销大的问题，该论文引入DocLongRAG数据集（含34.3万问答对，平均每对关联37.4张检索图像），并提出Doc-REFRAG框架，通过问题引导的视觉令牌压缩和基于轻量强化学习的选择器选择性扩展相关部分。在六个基准上，Doc-REFRAG优于十一个强基线，达到最先进准确率并显著降低推理延迟。
- **摘要（英）**: This paper addresses limited accuracy and high computational overhead in multimodal RAG for multi-image scenarios by introducing DocLongRAG, a large-scale dataset with 343K QA pairs and 37.4 retrieved images on average, and proposing Doc-REFRAG, which compresses visual tokens and selectively expands relevant ones via a lightweight RL-based selector. Experiments on six benchmarks show state-of-the-art accuracy with lower inference latency than eleven baselines.
- **评估**: 该论文在多模态文档检索增强生成方面有贡献，但与应用领域（自动驾驶感知）相关性一般。
- **核心贡献**: 提出了大规模多图像RAG数据集和高效的Doc-REFRAG框架。
- **创新点**: 问题引导的视觉令牌压缩和RL选择器。
- **结果**: 在六个基准上达到最先进准确率并降低延迟。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world knowledge resides in multimodal documents, necessitating retrieval-augmented generation (RAG) for accurate question answering. However, existing multimodal RAG models are primarily designed for single-image or closed-document settings and exhibit limited accuracy in realistic multi-image scenarios. Moreover, processing numerous retrieved images incurs substantial computational overhead from irrelevant visual tokens. To address these challenges, we introduce DocLongRAG, a large-scale dataset of 343K question--answer pairs, each associated with an average of 37.4 retrieved images to reflect authentic RAG workflows. Building on this dataset, we propose Doc-REFRAG, a question-guided framework that compresses visual tokens into coarse chunks and selectively expands question-relevant ones via a lightweight RL-based selector. Experiments on six benchmarks show that Doc-REFRAG outperforms eleven strong baselines, achieving state-of-the-art accuracy with significantly lower inference latency. Our resources are available at https://github.com/Collab-Gen/Doc-REFRAG.

</details>

### 7. DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution **⭐⭐** (相关度: 10%, 质量: 0.6)

- **arXiv ID**: [2608.31106](https://arxiv.org/abs/2608.31106)  · [📄 PDF](https://arxiv.org/pdf/2608.31106)
- **作者**: Jiashu Zhu, Yanhao Zheng, Ruitian Tian et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.SD
- **摘要（中）**: 针对现有视频生成器常忽略音频或分阶段合成，限制视觉动态与声学事件交互建模的问题，本文提出DreamX-Creator 1.0，一个紧凑的原生联合音视频生成系统，核心为7B生成器，基于首帧和文本提示联合去噪音频和视频流。系统通过门控跨模态注意力耦合流，并采用渐进式联合训练和音视频强化学习，以及自回归1步2K细化流程实现高分辨率输出。该方法在联合生成质量上有所提升，但主题与自动驾驶感知领域完全无关。
- **摘要（英）**: This paper addresses the limitation of video generators that omit audio or synthesize it separately, proposing DreamX-Creator 1.0, a compact native joint audio-video generation system with a 7B generator that jointly denoises audio and video streams conditioned on a first frame and text prompt. It uses gated cross-modal attention, progressive joint training, and audio-video reinforcement learning, with an autoregressive 1-step 2K refinement pipeline for high resolution. The method improves joint generation quality, but the topic is unrelated to autonomous driving perception.
- **评估**: 该论文在音视频生成领域有技术价值，但与自动驾驶感知研究方向完全无关，不建议关注。
- **核心贡献**: 提出了原生联合音视频生成系统DreamX-Creator 1.0。
- **创新点**: 通过门控跨模态注意力和联合训练实现音视频原生协同生成。
- **结果**: 在联合生成质量上取得提升，支持2K分辨率输出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent video generators often omit audio or synthesize it in a separate stage, limiting reciprocal modeling of visual dynamics and acoustic events. We present DreamX-Creator 1.0, a compact native joint audio-video generation system centered on a 7B generator. Conditioned on a first frame and a text prompt, the generator jointly denoises modality-specialized audio and video streams. The streams are processed independently in the first half of the network and coupled in the latter half through Gated Cross-Modal Attention, whose token- and head-wise output gates modulate each active cross-modal attention-head output. A unified Audio-Video Data System constructs and filters temporally coherent clips, produces structured multimodal annotations, and organizes clips into capability-oriented data pools. Progressive Joint Training comprises two audio-video pre-training stages followed by High-Quality Finetuning. Audio-Video Reinforcement Learning further post-trains the generator with Modality-Aware Multimodal Feedback that routes video-, audio-, and cross-modal feedback to the corresponding streams. For high-resolution output, our Autoregressive 1-Step 2K Refinement pipeline adapts a bidirectional multi-step teacher into an autoregressive multi-step refiner and distills it into a student requiring one denoising evaluation per temporal chunk. Overall, DreamX-Creator 1.0 achieves native, synchronized audio-video generation with performance competitive with state-of-the-art open-source systems. By releasing our compact 7B generator and 2K Refiner, we seek to democratize native audio-video generation and provide an accessible foundation for future research in unified audio-video generative modeling.

</details>

### 8. MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents **⭐⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2608.31022](https://arxiv.org/abs/2608.31022)  · [📄 PDF](https://arxiv.org/pdf/2608.31022)
- **作者**: Vernon Toh, Navonil Majumder, Zhengyuan Liu et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.AI, cs.CV
- **摘要（中）**: ①针对部分可观测环境中AI代理的感知状态构建与解释能力难以评估的问题。②提出了MNIST-PRO基准，将MNIST数字识别转化为带回溯约束的序列化瞥视搜索任务，并评估了十种多模态模型在四种记忆表示下的表现。③相比现有基准，MNIST-PRO隔离了物理和控制复杂性，专注于感知状态构建能力。④实验发现模型在完全可观测下表现良好，但在部分可观测下性能显著下降，并识别出三个瓶颈：感知状态构建困难、过早停止探索、难以修正早期错误信念。
- **摘要（英）**: This paper addresses the challenge of evaluating AI agents' perceptual-state construction in partially observable environments. It introduces MNIST-PRO, a benchmark converting MNIST recognition into a sequential glimpse-based search task with lookback constraints, evaluating ten multimodal models across four memory representations. Results reveal a clear performance gap under partial observability, identifying bottlenecks in state integration, premature exploration stopping, and failure to revise incorrect beliefs.
- **评估**: 该基准为研究代理感知与记忆交互提供了简洁的测试平台，但领域相关性较低，主要面向通用AI代理而非自动驾驶感知。
- **核心贡献**: 提出了MNIST-PRO基准，用于隔离和评估部分可观测环境中的感知状态构建能力。
- **创新点**: 将MNIST识别转化为带回溯约束的序列化瞥视搜索任务，简化了物理复杂性。
- **结果**: 揭示了部分可观测下多模态模型的性能瓶颈，包括感知集成和信念修正失败。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas. While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks. First, perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses. Second, agents often stop exploring before they see the full sequence. Third, models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence. These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.

</details>

### 9. From Intent to Evidence: Policy-Steered Multi-Strategy Retrieval for Long-Video Agents **⭐⭐⭐** (相关度: 35%, 质量: 0.65)

- **arXiv ID**: [2608.31005](https://arxiv.org/abs/2608.31005)  · [📄 PDF](https://arxiv.org/pdf/2608.31005)
- **作者**: Can Zhang, Baofeng Zhang, Xiaotian Han et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对长视频代理在证据获取时采用单一行为，忽略证据集中性、覆盖范围或竞争假设区分需求的问题。②提出了VESTA，一种无需训练的长视频代理，采用路由条件化的获取-验证-整合循环，通过意图路由器推断证据获取策略（聚焦、回忆或对比检索）和证据记账策略。③相比现有方法，VESTA允许自主探索，同时通过策略引导检索提高证据获取效率。④实验表明，VESTA在长视频问答任务中通过策略化检索和证据账本整合，提升了证据获取的准确性和推理效率。
- **摘要（英）**: This paper addresses the issue of long-video agents using uniform evidence acquisition behaviors, ignoring varying evidence requirements. It proposes VESTA, a training-free agent with a route-conditioned acquire-verify-consolidate loop, using an intent router to infer evidence-acquisition policies. VESTA enhances autonomous exploration and evidence integration, improving performance in long-video tasks.
- **评估**: 该方法对视频理解中的证据获取策略有创新，但主要面向通用视频代理，与自动驾驶感知的直接关联有限。
- **核心贡献**: 提出了VESTA，一种策略引导的多策略检索长视频代理，无需训练即可适应不同证据需求。
- **创新点**: 引入意图路由器动态选择检索策略，并维护时间证据账本以整合观测。
- **结果**: 在长视频任务中通过策略化检索提升了证据获取和推理的准确性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing long-video agents acquire evidence through one uniform behavior, ignoring whether the required evidence is concentrated, requires broad occurrence coverage, or must discriminate competing hypotheses---which can cause failure before substantive reasoning begins. Prescribing a fine-grained solution procedure for every question is not a satisfactory remedy, as it restricts autonomous exploration. We propose VESTA, a training-free long-video agent organized as a route-conditioned acquire--verify--consolidate loop. Before exploration, an intent router infers an evidence-acquisition policy---focused, recall, or contrastive retrieval over a shared visual--speech scene index---together with an evidence-accounting policy that configures the evidence view maintained during exploration. Policy-steered retrieval yields provisional references that multimodal evidence operations convert into observations, while the Reasoner remains free to verify them, re-query using intermediate findings, or inspect regions outside the retrieved set. A temporal evidence ledger consolidates observations into an adaptive, compressed view of temporal location, provenance, coverage, conflicts, verification outcomes, and hypothesis support, exposing missing and unresolved evidence to guide subsequent acquisition; finalization prioritizes verified observations. On Video-MME-v2, VESTA improves average accuracy by 2.7 points over VideoARM and gains across all six reported metrics. On LongVideoBench, EgoSchema, and LVBench under shared query-time models, it improves by 6.9 points on the LongVideoBench long subset and 1.5 on LVBench, and matches VideoARM on EgoSchema.

</details>

### 10. Pretrained, Curriculum-Tuned, and Ensembled: A Tracer-Aware Interactive Segmentation Pipeline for AutoPET V **⭐⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2608.30844](https://arxiv.org/abs/2608.30844)  · [📄 PDF](https://arxiv.org/pdf/2608.30844)
- **作者**: Xinglong Liang, Chunyao Lu, Tianyu Zhang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Liiiii2101/AUTOPET2026-MEDAI](https://github.com/Liiiii2101/AUTOPET2026-MEDAI)
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对全身PET/CT中交互式病灶分割需要强初始预测和高效响应稀疏修正笔划的问题，且FDG和PSMA示踪剂分布差异大。②提出了TRIAGE，一种示踪剂感知的交互式分割流程，核心是3D STU-Net，通过掩码自编码预训练和异步掩码策略学习跨模态表示，并辅以器官分割模型提供解剖上下文，示踪剂分类器路由到特定分支。③相比现有方法，TRIAGE利用示踪剂特定分支和器官上下文区分生理摄取与恶性病灶。④在AutoPET V挑战中，TRIAGE通过预训练和课程调优，提升了初始预测和交互修正的准确性。
- **摘要（英）**: This paper addresses interactive lesion segmentation in whole-body PET/CT, where tracer distributions differ between FDG and PSMA studies. It proposes TRIAGE, a tracer-aware pipeline using a 3D STU-Net with masked autoencoding pre-training and an auxiliary organ segmentation model for anatomical context. TRIAGE improves initial predictions and interactive refinement, showing strong performance in the AutoPET V challenge.
- **评估**: 该方法在医学影像分割中具有创新性，但领域与自动驾驶感知相关性中等，可借鉴其预训练和交互策略。
- **核心贡献**: 提出了TRIAGE，一种示踪剂感知的交互式分割流程，结合预训练和器官上下文。
- **创新点**: 利用异步掩码自编码预训练和示踪剂分类路由，适应不同示踪剂分布。
- **结果**: 在AutoPET V中通过预训练和课程调优提升了分割性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Interactive lesion segmentation in whole-body PET/CT requires a model to provide a strong initial prediction while also responding efficiently to sparse corrective scribbles during inference. This setting is particularly challenging because tracer distributions, physiological uptake patterns, lesion appearance, and acquisition characteristics differ substantially between FDG and PSMA studies. We present TRIAGE, Tracer-aware Refinement via Interactive Anatomy-Guided sEgmentation. The core backbone is a 3D STU-Net initialized through masked autoencoding pre-training with an asynchronous masking strategy, aiming to learn transferable anatomical and cross-modal representations before task-specific fine-tuning. In parallel, we train an auxiliary organ segmentation model whose predictions provide explicit anatomical context and help distinguish physiological uptake from malignant lesions. A dedicated tracer classifier first routes each study to an FDG- or PSMA-specific branch. Within each branch, a first-stage segmentation model consumes CT, PET, and organ context to generate an initial lesion mask. The initial prediction is then combined with cumulative foreground/background scribbles and refined by a second interactive segmentation network. The FDG and PSMA branches share the same overall processing pipeline but are trained independently to account for tracer-specific appearance and error modes. We additionally employ curriculum-style training and model ensembling to improve robustness across interaction steps and heterogeneous cohorts. Experiments are conducted using the official AutoPET V data and ten-fold split; quantitative results, ablations, and final test-set performance are left as placeholders to be completed after the challenge evaluation. Code: https://github.com/Liiiii2101/AUTOPET2026-MEDAI.

</details>

---

## Object Detection

### 1. ARMOR: Manifold-Oriented Training for Adversarially Robust Aerial Object Detection under Data Scarcity **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.85)

- **arXiv ID**: [2608.29510](https://arxiv.org/abs/2608.29510)  · [📄 PDF](https://arxiv.org/pdf/2608.29510)
- **作者**: Haoran Wang, Matthew Lau, Alec Helbling et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.CR, cs.LG
- **摘要（中）**: 针对航空目标检测在数据稀缺下对物理对抗补丁的脆弱性问题，提出了ARMOR，一种基于流形导向训练的防御方法。该方法通过掩蔽图像背景保留目标相关特征，并注入随机化补丁，在低数据场景下实现对抗鲁棒性。相比依赖大规模生成模型的OMAT，ARMOR复用检测任务标签，数据高效。
- **摘要（英）**: To address vulnerability to adversarial patches in aerial object detection under data scarcity, this paper proposes ARMOR, a manifold-oriented training defense that masks backgrounds and injects randomized patches. It is data-efficient by reusing detection labels, unlike OMAT.
- **评估**: 该工作针对实际部署中的对抗鲁棒性和数据稀缺问题，方法实用且与自动驾驶感知高度相关。
- **核心贡献**: 提出了一个数据高效的流形导向对抗训练方法，用于航空目标检测。
- **创新点**: 通过背景掩蔽和随机补丁注入实现低数据下的对抗鲁棒性。
- **结果**: 摘要未提供具体数值，但声称有效提升鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aerial object detection is increasingly deployed in real-world applications, but models remain vulnerable to physical, universal adversarial patches that cause them to miss objects. Furthermore, defenders face the practical constraint of training data scarcity: aerial imagery is costly to collect and label, so a deployment site typically yields hundreds of images rather than the tens of thousands that adversarial robustness benchmarks assume. To tackle model vulnerability and training data scarcity, we propose Adversarial Robustness with Manifold-Oriented Training (ARMOR), a novel defense that realizes the core insights of on-manifold adversarial training (OMAT) in low-data regimes. ARMOR builds on the insight of OMAT to model the data manifold - the compact structure capturing the data's relevant features - to learn and robustify these features during training. While OMAT relies on the data-intensive operations of training large generative models and adversarial training to achieve this, ARMOR adopts a data-efficient approach that reuses labels the detection task already supplies: ARMOR (i) masks image backgrounds to retain object-relevant features, and (ii) injects randomized patches on objects to improve feature robustness. Our low-data experiments with physically-realizable adversarial patches evaluate both query-free transfer attacks and defense-aware attacks. ARMOR maintains strong clean performance of over 0.90 model confidence, while improving adversarial robustness by up to 0.32 in model confidence over state-of-the-art defenses. Physical experiments with printed patches confirm that these gains survive deployment. Overall, ARMOR translates insights from manifold-based training to defend object detectors amidst training data scarcity.

</details>

### 2. SynCrash: A Multi-Stage Pipeline for Zero-Shot Accident Detection and Localization in Traffic Surveillance Video **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.29759](https://arxiv.org/abs/2608.29759)  · [📄 PDF](https://arxiv.org/pdf/2608.29759)
- **作者**: Arkya Jyoti Bagchi, Ritul Jangir, Varun Raskar
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 这篇论文针对固定视角CCTV监控视频中的零样本事故检测、空间定位和碰撞类型分类问题，面向CVPR 2026 ACCIDENT挑战赛。作者提出SynCrash多阶段流水线：首先用VideoMAEv2-giant在CARLA合成数据上微调进行时间定位，其次用YOLO检测物体并结合物理启发式规则预测碰撞点，最后用基于车辆数量和配置的规则分类碰撞类型。核心洞察是时间理解适合合成数据监督微调，而空间理解依赖预训练检测器和物理先验。该方法在零样本设置下有效，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses zero-shot accident detection, localization, and classification in CCTV surveillance video. The authors propose SynCrash, a multi-stage pipeline using VideoMAEv2 fine-tuned on synthetic CARLA data for temporal localization, YOLO with physics-informed heuristics for spatial localization, and rule-based collision classification. It leverages synthetic training and pretrained detectors, but no quantitative results are reported.
- **评估**: 该论文与自动驾驶感知高度相关，特别是事故检测和零样本泛化，方法设计合理，但缺乏具体实验结果。
- **核心贡献**: 提出SynCrash多阶段流水线，实现零样本事故检测、定位和分类。
- **创新点**: 结合合成数据微调与物理启发式规则，解耦时间与空间理解。
- **结果**: 在零样本设置下有效，但具体性能未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present SynCrash, a multi-stage pipeline for zero-shot accident detection, spatial localization, and collision-type classification in fixed-view CCTV surveillance video. Our approach addresses the ACCIDENT at CVPR 2026 Challenge, which requires predicting when an accident occurs, where in the frame the impact happens, and what type of collision it is, all without access to labeled real-world training data. The pipeline operates in three decoupled stages: (1) Temporal localization via a VideoMAEv2-giant backbone fine-tuned on CARLA-based synthetic clips with metadata-aware embeddings and dense sliding-window inference; (2) Spatial localization using YOLO for object detection combined with a physics-informed hybrid heuristic that leverages bounding-box overlap and trajectory-based reasoning to predict the impact point; and (3) Collision-type classification using a lightweight rule-based strategy derived from the number and configuration of detected vehicles. The key insight is that temporal understanding benefits from supervised fine-tuning on synthetic data, whereas spatial understanding is better served by pretrained object detectors and physics priors that transfer naturally across domains.

</details>

### 3. Real-Time Video Anomaly Detection Using YOLO Pose Estimation and CLIP-Based Semantic Scoring **⭐⭐⭐** (相关度: 55%, 质量: 0.6)

- **arXiv ID**: [2608.31074](https://arxiv.org/abs/2608.31074)  · [📄 PDF](https://arxiv.org/pdf/2608.31074)
- **作者**: Vanodhya G. Warnasooriya, Amir Hajian, Watchara Ruangsang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI, eess.IV
- **摘要（中）**: ①针对实时视频异常检测中光流和独立姿态估计计算开销大的问题。②提出了两阶段轻量框架，第一阶段用YOLO v11n-pose提取人体关键点，第二阶段用CLIP ViT-B/32对裁剪区域进行语义评分。③消除了光流、独立姿态估计器和密度评分模块的需求。④在CUHK Avenue、ShanghaiTech和自定义数据集上达到约51 FPS，AUROC分别为89.26%、70.26%和84.13%，比多特征基线快3.36倍。
- **摘要（英）**: This paper addresses computational overhead in real-time video anomaly detection by proposing a lightweight two-stage framework using YOLO pose estimation and CLIP-based semantic scoring. It eliminates optical flow and standalone pose estimators, achieving 51 FPS with AUROC values of 89.26%, 70.26%, and 84.13% on three datasets.
- **评估**: 该论文方法简洁高效，适合实时监控场景，但与自动驾驶感知核心任务关联度一般。
- **核心贡献**: 提出基于YOLO姿态和CLIP语义评分的实时视频异常检测框架。
- **创新点**: 融合姿态关键点与CLIP文本语义，去除传统光流依赖。
- **结果**: 实现51 FPS吞吐量，AUROC最高达89.26%，速度提升3.36倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a lightweight two-stage framework for real-time video anomaly detection. The first stage employs YOLO v11n-pose to detect persons and extract seventeen skeletal keypoints in a single forward pass. The second stage encodes each cropped person region through CLIP ViT-B/32 and computes cosine similarity against predefined textual descriptions of anomalous behaviors. This architecture eliminates the need for optical flow, standalone pose estimators, and density-based scoring modules. Experiments on CUHK Avenue, ShanghaiTech Campus, and a custom indoor dataset collected at Chulalongkorn University demonstrate an end-to-end throughput of approximately 51 FPS on an NVIDIA Titan XP GPU, a 3.36x speedup over the multi-feature baseline, while maintaining frame-level AUROC values of 89.26%, 70.26%, and 84.13%, respectively.

</details>

### 4. RailSyn: Diagnosis-Guided Image Generation for Traceable Data Completion in Railway Foreign Object Detection **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.75)

- **arXiv ID**: [2608.30709](https://arxiv.org/abs/2608.30709)  · [📄 PDF](https://arxiv.org/pdf/2608.30709)
- **作者**: Quan Hao, Chenxi Zhang, Ziyang Tao et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对铁路异物检测中真实正样本稀缺、生成数据缺乏任务相关缺陷显式补偿的问题。②提出了RailSyn诊断引导框架，包含真实参考的Inspector和需求对齐的Generator；Inspector构建变半径经验覆盖定位补全区域，Generator通过域适应、智能体规划放置和条件细化生成数据。③通过审计识别铁路上下文、入侵语义和视觉一致性需求，并追踪表示空间变化。④完整系统达到局部壳覆盖C_gap至13.64%，显著提升生成数据对真实分布的覆盖。
- **摘要（英）**: This paper addresses scarce real positive samples in railway foreign object detection by proposing RailSyn, a diagnosis-guided framework with an Inspector and Generator. The Inspector localizes completion regions via empirical cover, while the Generator uses domain adaptation and agent-planned placement. The system achieves local-shell occupation of C_gap to 13.64%, improving data coverage.
- **评估**: 该论文针对FOD检测的数据稀缺问题提出创新性生成框架，与自动驾驶中罕见障碍物检测高度相关，值得关注。
- **核心贡献**: 提出诊断引导的铁路异物检测数据补全框架RailSyn。
- **创新点**: 通过Inspector审计和Generator需求对齐，实现可追踪的生成数据补全。
- **结果**: 局部壳覆盖达到13.64%，有效提升生成数据对真实分布的覆盖。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Railway foreign object detection (RFOD) is critical to safe railway operation, yet scarce real positive samples incompletely represent task-relevant variations in object scale, intrusion relation, railway scene, illumination, and adverse weather. Existing synthetic augmentation can improve RFOD detection, but its gains lack an explicit account of the task-relevant deficiencies complemented by the generated data. We therefore introduce RailSyn, a diagnosis-guided framework comprising a real-referenced Inspector and a requirement-aligned Generator. The Inspector constructs a variable-radius empirical cover from finite real observations to localize candidate completion regions and profile synthetic pools. The resulting audit identifies railway-context, intrusion-semantic, and visual-consistency requirements; the Generator addresses them through domain adaptation, agent-planned placement and physical contact relations, and plan-consistent conditional refinement. Using the Inspector, we further trace representation-space changes across generation variants; the complete system attains a local-shell occupation of $C_{gap}$ to 13.64%, which measures generated coverage of real-derived completion regions. Extensive experiments show AP50--95 gains of up to 4.9 points and consistent improvements across nine mainstream detectors, demonstrating broad cross-architecture utility.

</details>

### 5. Real-Time Scene-Adaptive Tone Mapping for High-Dynamic Range Object Detection **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.30400](https://arxiv.org/abs/2608.30400)  · [📄 PDF](https://arxiv.org/pdf/2608.30400)
- **作者**: Gongzhe Li, Linwei Qiu, Peibei Cao et al. (6 authors)
- **🏷️ 机构**: The Chinese University of Hong Kong, Shenzhen, Beihang University, Nanjing University of Information Science and Technology
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对HDR图像输入导致LDR训练的目标检测网络性能严重下降的问题。②提出了场景自适应色调映射方法，引入神经光度校准和尺度不变局部色调映射模型，实现与下游任务的端到端优化。③支持性能迁移微调，从LDR sRGB高效适应HDR RAW。④在挑战性汽车HDR场景中优于传统色调映射和先进AI-ISP方法，并支持高效迁移。
- **摘要（英）**: This paper addresses performance degradation of LDR-trained detection networks on HDR inputs by proposing a scene-adaptive tone mapping method with neural photometric calibration and scaling-invariant local mapping. It enables end-to-end optimization with downstream tasks and efficient transfer finetuning. The method outperforms traditional and AI-ISP methods in automotive HDR scenes.
- **评估**: 该论文直接解决自动驾驶中HDR感知的实际问题，方法创新且实用，与目标检测和自动驾驶高度相关。
- **核心贡献**: 提出面向HDR目标检测的场景自适应色调映射方法。
- **创新点**: 引入神经光度校准和尺度不变局部映射，实现端到端优化。
- **结果**: 在汽车HDR场景中优于传统和AI-ISP方法，支持高效迁移。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-dynamic-range (HDR) images, with their rich tone and detail reproduction, hold significant potential to enhance computer vision systems, particularly in autonomous driving. However, most neural networks for embedded systems are trained on low-dynamic-range (LDR) inputs and suffer substantial performance degradation when handling high-bit-depth HDR images due to the challenges posed by extreme dynamic ranges. In this paper, we propose a novel tone mapping method that not only bridges the gap between HDR RAW inputs and the LDR sRGB requirements of detection networks but also achieves end-to-end optimization with downstream tasks. Instead of relying on the traditional image signal processing (ISP) pipeline, we introduce neural photometric calibration to regularize dynamic ranges and a scaling-invariant local tone mapping model to preserve image details. In addition, our architecture also supports performance transfer finetuning, enabling efficient adaptation from the LDR sRGB images to the HDR RAW images with minimal cost. The proposed method outperforms traditional tone mapping algorithms and advanced AI-ISP methods in challenging automotive HDR scenes. Moreover, our pipeline achieves real-time processing of 4K high-bit-depth HDR inputs on NVIDIA Jetson platforms.

</details>

### 6. Seeing the Unseen: Camouflaged Object Detection Beyond the Visible Spectrum **⭐⭐⭐** (相关度: 70%, 质量: 0.7)

- **arXiv ID**: [2608.30355](https://arxiv.org/abs/2608.30355)  · [📄 PDF](https://arxiv.org/pdf/2608.30355)
- **作者**: Avi Gupta, Trasha Gupta
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对传统伪装目标检测仅依赖RGB图像、光谱信息受限的问题。②提出了MSFormer端到端框架，利用多光谱图像进行伪装目标检测，预测二值掩码。③提供了多光谱波段整合的实证依据。④实验表明方法优于现有RGB-based方法，验证了多光谱信息的有效性。
- **摘要（英）**: This paper addresses limited spectral information in camouflaged object detection by proposing MSFormer, an end-to-end framework leveraging multispectral images for binary mask prediction. It provides empirical justification for integrating multispectral bands. Extensive experiments show superiority over existing RGB-based methods.
- **评估**: 该论文拓展了伪装检测的光谱维度，对自动驾驶中低可见性目标感知有参考价值，但应用场景较窄。
- **核心贡献**: 提出多光谱伪装目标检测框架MSFormer。
- **创新点**: 利用多光谱图像丰富光谱信息，提升低可见性目标检测能力。
- **结果**: 在多个数据集上优于现有RGB-based方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in camouflaged object detection (COD) have led to substantial progress in challenging low-visibility scenarios, with pioneering studies demonstrating notable success in localizing objects in camouflaged scenes. Despite these achievements, existing approaches predominantly rely on conventional three-channel RGB imagery, thereby constraining the available visual information to a limited spectral range. Multispectral images offer a wide range of information about a scene by capturing fine-grained spectral signatures. Hence, by leveraging multispectral images for COD, we introduce a novel approach to detect camouflaged objects from the corresponding multispectral inputs. In particular, we propose an end-to-end framework, \textbf{\textit{MSFormer}}, that takes a multispectral camouflaged image as input and predicts a binary mask for it. Additionally, we also provide empirical justification for integrating multispectral bands for this complex low-vision task. Our extensive experiments demonstrate the effectiveness of our method, which outperforms existing methods.

</details>

### 7. RailGen: Improving Railway Intrusion Detection via Agent-Guided Small-Scale Foreign Object Generation **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.30727](https://arxiv.org/abs/2608.30727)  · [📄 PDF](https://arxiv.org/pdf/2608.30727)
- **作者**: Quan Hao, Ziyang Tao, Chenxi Zhang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对铁路异物检测（RFOD）中小目标检测在长尾分布下样本稀缺和类间模糊的问题，提出生成增强检测范式。构建RailGen多模态图像生成智能体，基于大模型在语义约束下自动调用工具生成铁路场景、校准入侵位置、提取异物并融合成逼真入侵效果，生成高质量合成样本以稠密化尾类特征。提出FocalDEIM检测框架，采用Focal Modulation增强密集匹配以改善小目标判别，并采用Focal Loss强调难样本，缓解复杂铁路场景中的类间模糊。
- **摘要（英）**: This paper addresses small-object detection in railway foreign object detection (RFOD) under long-tailed distributions by proposing a generative-augmented paradigm. RailGen, a multimodal generation agent, automatically creates realistic intrusion samples to densify tail-class features. FocalDEIM, a detection framework, uses Focal Modulation and Focal Loss to improve small-object discrimination and handle hard samples, alleviating inter-class blur.
- **评估**: 该工作针对铁路异物检测这一实际应用场景，结合生成式增强和检测优化，具有较高的应用价值和针对性。
- **核心贡献**: 提出了RailGen生成智能体和FocalDEIM检测框架，解决长尾小目标检测问题。
- **创新点**: 利用大模型驱动的多模态生成智能体自动合成逼真异物样本。
- **结果**: 有效稠密化尾类特征空间，提升小目标检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Small-object detection under long-tailed data distributions is a fundamental yet challenging problem in multimedia. Railway Foreign Object Detection (RFOD) epitomizes this challenge with easily confused small intrusions and scarce samples. To address these issues, we propose a generative-augmented detection paradigm that leverages multimodal image generation to enrich the feature space of rare and small objects. We first construct RailGen, a multimodal image generation agent based on large models. Under semantic constraints, RailGen automatically invokes tools to generate railway scenes, calibrate intrusion positions, extract foreign objects, and fuse them into realistic intrusion effects. This process produces high-quality synthetic samples that effectively densify the feature representations of tail classes and complete the small-object feature space. Within this paradigm, we further propose FocalDEIM, a detection framework designed to enhance training with generated data. FocalDEIM improves dense matching with Focal Modulation for better small-object discrimination and adopts Focal Loss to emphasize hard samples, thereby alleviating blurred inter-class boundaries in complex railway scenes. Experimental results demonstrate that RailGen can generate high-quality small-scale foreign objects, reducing the object pixel area by up to 58x and 13.85x on average. Equipped with these challenging samples, our paradigm surpasses the baseline DEIM by 5.6% and 7.5% in mAP@50 and mAP@(50-95), respectively, and outperforms existing state-of-the-art methods. Ablation studies verify RailGen's feature-space enrichment and FocalDEIM's boundary discrimination. The paradigm provides an effective multimodal generative solution for long-tailed small-object detection in safety-critical applications.

</details>

### 8. A Composition-Aware Pretraining Framework for Geospatial Foundation Models **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.30817](https://arxiv.org/abs/2608.30817)  · [📄 PDF](https://arxiv.org/pdf/2608.30817)
- **作者**: Aryan Kashyap Naveen, Abhishek Srinivas, Pranav Moothedath et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/05kashyap/GFM_Composition_Pretraining](https://github.com/05kashyap/GFM_Composition_Pretraining)
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对地理空间基础模型预训练忽略卫星场景组合性的问题，提出组合感知预训练框架，将每个图像单元映射到土地覆盖分数直方图作为预测目标，并用推土机距离蒸馏到骨干网络。相比现有方法，该框架显式编码分数土地覆盖混合，提升了区域级语义理解任务性能。在36.8M参数下，在多数检索和场景分类设置中优于303M参数的SatMAE和600M参数的Prithvi-EO-2.0。
- **摘要（英）**: To address the lack of compositional modeling in geospatial pretraining, this framework maps each image cell to a fractional land-cover histogram as a prediction target, distilled via Earth Mover's Distance. It explicitly encodes land-cover mixtures, improving region-level tasks like retrieval and classification. With 36.8M parameters, it outperforms larger SatMAE and Prithvi-EO-2.0 in most settings.
- **评估**: 该工作对遥感基础模型有显著改进，但与应用领域（自动驾驶）相关性一般。
- **核心贡献**: 提出组合感知预训练框架，显式编码土地覆盖分数。
- **创新点**: 使用分数土地覆盖直方图作为预训练目标。
- **结果**: 在检索和分类任务上超越更大规模模型。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Geospatial foundation models have emerged as state-of-the-art methods for downstream Earth observation tasks. However, existing pretraining methodologies process imagery through a single-concept lens, failing to capture the highly compositional nature of complex satellite scenes. We propose a composition-aware pretraining framework that explicitly encodes fractional land-cover mixtures. Each satellite image cell is mapped to a histogram representing its fractional land-cover distribution, which we term the "composition target". These targets serve as the primary prediction objective and are distilled into the backbone using Earth Mover's Distance. Experimental evaluation shows that composition-aware pretraining yields substantial gains on region-level understanding tasks requiring semantic similarity judgment, including zero-shot image retrieval and scene classification, while remaining competitive on tasks requiring fine-grained spatial precision, such as segmentation and object detection. With a 36.8M-parameter backbone, our framework outperforms SatMAE and Prithvi-EO-2.0, which contain 303M and 600M parameters, respectively, in most retrieval and scene classification settings. On the fine-grained ForestNet-12 dataset, a rigorous testbed for compositional discrimination, our method boosts baseline mAP@10 from 0.279 to 0.434, a 55.6% relative improvement, providing direct evidence for the effectiveness of explicit composition modeling. The code implementation can be found at https://github.com/05kashyap/GFM_Composition_Pretraining

</details>

### 9. ChessQueries: Toward Better Chess Board Recognition **⭐⭐⭐⭐** (相关度: 50%, 质量: 0.8)

- **arXiv ID**: [2608.30762](https://arxiv.org/abs/2608.30762)  · [📄 PDF](https://arxiv.org/pdf/2608.30762)
- **作者**: Joël Seytre
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对国际象棋棋盘识别任务中现有基准的局限性，提出ChessQueries方法，结合ViT编码器和DETR风格解码器，在ChessReD基准上将SOTA从15.3%提升至99.2%，并在分布外数据集上表现强劲。该方法在两个数据集上饱和，平均每棋盘错误方块数仅0.01（对比SOTA的3.4和0.15），并发布了更难的广播比赛数据集。
- **摘要（英）**: To improve chess board recognition, ChessQueries combines a ViT encoder with a DETR-style decoder, boosting ChessReD accuracy from 15.3% to 99.2% and showing strong out-of-distribution performance. It saturates existing benchmarks with 0.01 wrong squares per board, and introduces a harder dataset from broadcast tournaments.
- **评估**: 该方法在特定任务上表现卓越，但领域相关性有限，不过其技术可迁移至一般目标检测。
- **核心贡献**: 提出高精度棋盘识别方法并发布更难数据集。
- **创新点**: 结合ViT和DETR解码器实现端到端棋盘识别。
- **结果**: 在ChessReD上达到99.2%准确率，错误率极低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Chess board recognition is the task of mapping the image of a chess board to the information of which piece is on which square. So far this task has two established benchmarks: ChessCog is synthetic, and ChessReD comes from smartphone pictures of a single chess board setup. We introduce ChessQueries, a new method combining a ViT encoder with a DETR-style decoder, which outperforms existing methods. On the ChessReD benchmark, we improve the state of the art from 15.3% to 99.2%, and demonstrate strong capabilities on out-of-distribution datasets. Our method saturates the task on the two datasets, with an average 0.01 wrong squares per board (vs. SotA: 3.4 / 0.15 respectively). We also share a new, harder public dataset, parsed from broadcasted top-level chess tournaments. Code, model weights and the SLCC data will be released.

</details>

---

## Multi-camera Perception

### 1. DARP: A Calibrated Dual-Arm RGB-D-IR Dataset for Multi-View Robotic Perception **⭐⭐** (相关度: 25%, 质量: 0.65)

- **arXiv ID**: [2608.31002](https://arxiv.org/abs/2608.31002)  · [📄 PDF](https://arxiv.org/pdf/2608.31002)
- **作者**: Manish Kansana, Mohammed Yusuf Mujawar, Sudip Mittal et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.RO, cs.CV
- **摘要（中）**: 针对机器人感知中单视角受自遮挡和表面可见性限制的问题，该论文提出DARP数据集，包含双机械臂RGB-D-IR多模态数据，使用两个独立移动的眼在手式机械臂在共享桌面工作区进行对象中心感知。每个机械臂携带Intel RealSense传感器记录RGB、深度和立体红外数据，并同步记录机器人关节状态用于姿态恢复。数据集包含十个桌面对象，保留原始传感器记录和标定信息，并实现了确定性多视图融合管道以评估几何一致性。
- **摘要（英）**: This paper addresses limitations of single-view robotic perception by introducing DARP, a calibrated dual-arm RGB-D-IR dataset with two independently moving eye-in-hand manipulators for object-centered perception. Each arm records RGB, depth, and stereo infrared data with synchronized robot states, and the dataset includes ten objects with calibration for trajectory reconstruction. A deterministic multi-view fusion pipeline evaluates geometric consistency.
- **评估**: 该论文提供了多视角感知数据集，但主要面向机器人操作，与自动驾驶感知相关性较低。
- **核心贡献**: 发布了双机械臂多模态感知数据集DARP。
- **创新点**: 双机械臂自动定位和跨臂确认的采集流程。
- **结果**: 提供了可用于多视角融合评估的数据集。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robotic perception from a single viewpoint is often limited by self-occlusion and incomplete surface visibility. This paper presents DARP(Dual-Arm Robotic Perception) https://doi.org/10.21227/rmv3-be47, a calibrated dual-arm RGB-D-IR dataset for object-centered robotic perception using two independently moving eye-in-hand manipulators positioned on opposite sides of a shared tabletop workspace. Each arm carries an Intel RealSense sensor that continuously records RGB, depth, and stereo infrared data while synchronized robot joint states are logged for pose recovery. Objects are placed without fixed poses or marked locations, and the acquisition procedure performs automatic localization, cross-arm confirmation, adaptive viewpoint generation, and continuous multimodal recording. DARP contains ten unique tabletop objects and preserves the original sensor recordings, robot-state logs, object-level metadata, and calibration information required to reconstruct camera trajectories in a shared metric frame. To evaluate the geometric consistency of the acquisition, we implement a deterministic multi-view fusion pipeline that converts calibrated RGB-D observations into complementary partial point clouds and measured surface meshes without using learned or generative completion methods. Evaluation on 224 held-out RGB-D keyframes comprising 1,563,466 three-dimensional query points yields a median point-to-mesh distance of 2.13~mm and an RMSE of 4.04~mm, with 96.56\% of points within 10~mm of the measured-surface mesh. DARP is intended as a reusable resource for multi-view reconstruction, collaborative robotic perception, multimodal fusion, active perception, and future learning-based reasoning over partial object observations.

</details>

### 2. Multi-View Reflective Surface Inspection via Semantic-Saliency Cross-Verification **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.30997](https://arxiv.org/abs/2608.30997)  · [📄 PDF](https://arxiv.org/pdf/2608.30997)
- **作者**: Van-Giang Nguyen, Thanh-Tuan Tran, Xuan-Hieu Phan et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对反光智能手机盖板玻璃从单一固定视角检测缺陷时可见性变化和空间模糊的问题，该论文提出多视角检测框架，每个RGB观测由共享的每视角专家处理，视觉语言模型生成类别感知语义框，法线参考重建分支提供类别无关显著性，通过空间一致性对语义提议进行重排序。在282张生产线图像上，语义-显著性关联将AP50从52.6%提升至62.6%，跨视角证据召回率从最佳单视角的75.5%提升至88.3%。
- **摘要（英）**: This paper addresses defect visibility variation and spatial ambiguity in reflective surface inspection by proposing a multi-view framework where a VLM generates semantic boxes and a normal-reference branch provides saliency, with spatial agreement used to re-rank proposals. On 282 production images, AP50 improves from 52.6% to 62.6%, and cross-view recall increases from 75.5% to 88.3%.
- **评估**: 该论文在多视角感知和VLM应用上有一定参考价值，但面向工业检测，与自动驾驶感知相关性中等。
- **核心贡献**: 提出了语义-显著性交叉验证的多视角缺陷检测框架。
- **创新点**: 利用VLM语义框和显著性空间一致性进行重排序。
- **结果**: 显著提升了检测精度和跨视角召回率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reflective smartphone cover glass is challenging to inspect from a single fixed viewpoint because defect visibility varies with viewing geometry and specular reflections. This gives rise to two practical challenges: defects may be weakly observable from certain viewpoints, while the available visual evidence may remain spatially ambiguous. To address these issues, we propose a multi-view inspection framework in which each RGB observation is processed by a shared per-view expert. A vision-language model (VLM) produces class-aware semantic boxes, while a normal-reference reconstruction branch provides class-agnostic saliency. Their spatial agreement is used as supporting evidence to rank semantic proposals without modifying their coordinates or treating saliency as ground truth. The resulting evidence records are combined at product level without cross-view registration. On 282 production-line images, semantic-saliency association improves $AP_{50}$ from 52.6% to 62.6% by re-ranking fixed semantic proposals. Across 94 products, cross-view evidence recall $R_{\rm prod}@0.5$ increases from 75.5% for the best single view to 88.3% using all three views. These results support the complementary roles of semantic-saliency cross-verification and additional optical observations in reflective-surface inspection.

</details>

### 3. MEOM: Multi-View Expected-OKS Maximization for Human Pose Triangulation **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.30521](https://arxiv.org/abs/2608.30521)  · [📄 PDF](https://arxiv.org/pdf/2608.30521)
- **作者**: Ziliang Xiong, Henglin Shi, Per-Erik Forssen
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对传统代数三角化从多视角2D关键点估计3D人体姿态时，热图多模态和单峰解码丢失空间分布的问题，该论文提出多视角期望OKS最大化（MEOM）目标，定位各视角概率质量一致的3D关节点，并采用最高密度区域校准评估热图可靠性。该框架支持有无3D监督两种设置，无监督时通过最大化MEOM优化3D姿态，在模糊的Human3.6M和遮挡的CMU Panoptic帧上优于依赖更大骨干和时间融合的方法。
- **摘要（英）**: This paper addresses unreliable heatmap decoding in multi-view 3D human pose estimation by proposing Multi-view Expected-OKS Maximization (MEOM), which locates 3D joints where views agree in probability mass, and uses highest-density-region calibration for reliability. The framework works with and without 3D supervision, achieving comparable or better performance on ambiguous and occluded benchmarks than methods with larger backbones and temporal fusion.
- **评估**: 该论文在多视角3D姿态估计上有创新，与自动驾驶中的3D检测和BEV感知有方法上的相关性，值得关注。
- **核心贡献**: 提出了基于概率质量融合的多视角3D姿态估计目标MEOM。
- **创新点**: 利用整个热图分布和HDR校准进行鲁棒三角化。
- **结果**: 在模糊和遮挡场景中达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional algebraic triangulation solves 3D human pose estimation (HPE) from multi-view 2D keypoints. The typical approach, decoding 2D keypoints from predicted heatmaps, is unreliable as heatmaps can be multimodal under occlusion, and collapsing them into single peaks discards their spatial distribution. We seek to use the entire heatmap to estimate 3D poses more accurately, which requires solving two problems: how to robustly fuse heatmaps across views, and how to assess the reliability of heatmaps. For the former, we introduce a novel objective, Multi-viewExpected-OKS Maximization (MEOM), that locates a 3D joint where the views agree in probability mass. For the latter, we adopt highest-density-region (HDR) calibration as a diagnostic of that mass, independently of distance-based metrics. The proposed framework covers two settings, with and without 3D supervision. Without 3D supervision, we optimize 3D poses from pretrained heatmap predictors by maximizing MEOM, achieving comparable performance with state-of-the-art methods that rely on larger backbones, temporal fusion, and simulated 3D data. On ambiguous Human3.6M (H36MA) and occluded CMU Panoptic frames, the advantage is substantial. When 3D labels are available, we train the model end-to-end with a combined MEOM and MSE loss, achieving 19.11 mm absolute MPJPE on Human3.6M outperforming the state-of-the-art volumetric approach on absolute MPJPE at half the inference cost.

</details>

### 4. FaceSnap: Real-Time Personalized Lightstage Facial Performance Capture **⭐⭐** (相关度: 15%, 质量: 0.7)

- **arXiv ID**: [2608.31033](https://arxiv.org/abs/2608.31033)  · [📄 PDF](https://arxiv.org/pdf/2608.31033)
- **作者**: Rukhshanda Hussain, Noé Artru, Emeline Got et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对Lightstage面部捕捉资源密集、计算量大和数据存储瓶颈的问题，本文提出FaceSnap，一个端到端框架，通过两阶段方法简化捕捉流程。第一阶段从运动范围序列进行一次性多视角优化，构建个性化模型编码几何和表情相关外观；第二阶段利用该模型从单目Lightstage相机实现实时高保真面部性能捕捉，联合估计几何和动态4K纹理，速度达83 fps。FaceSnap在几何精度上与全帧多视角优化相当，优于基于生产质量3D数据训练的feed-forward方法，并引入Multi4D基准。该工作专注于数字人领域，与自动驾驶感知无关。
- **摘要（英）**: This paper addresses the resource-intensive and labor-heavy nature of Lightstage facial capture, proposing FaceSnap, an end-to-end framework with a two-stage approach: one-time multi-view optimization for a personalized model, then real-time monocular capture with joint geometry and 4K texture estimation at 83 fps. FaceSnap achieves geometric accuracy competitive with full multi-view optimization and outperforms feed-forward methods, introducing the Multi4D benchmark. The work focuses on digital humans and is unrelated to autonomous driving perception.
- **评估**: 该论文在数字人捕捉领域有创新性，但主题与自动驾驶感知完全无关，不具参考价值。
- **核心贡献**: 提出了FaceSnap框架，实现单目实时高保真面部捕捉。
- **创新点**: 通过个性化模型和残差上采样器实现单目4K纹理恢复。
- **结果**: 83 fps下实现几何精度与多视角优化相当，优于feed-forward方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Lightstage facial capture produces production-quality digital humans, but it is resource and labor-intensive. Multi-camera setups, hours of computation, and massive data storage create bottlenecks that hinder iterative workflows. This paper introduces FaceSnap, an end-to-end framework that streamlines capture via a two-stage approach. First, a one-time multi-view optimization from a range-of-motion sequence builds a personalized model encoding both geometry and expression-dependent appearance. This model then enables high-fidelity real-time facial performance capture from a single monocular lightstage camera, with no further multi-view capture required. FaceSnap jointly estimates geometry and dynamic 4K texture at 83 fps. The 4K texture is produced by a novel personalized residual upscaler that recovers subject-specific high-frequency detail, which generic upscalers fail to capture. FaceSnap achieves geometric accuracy competitive with full per-frame multi-view optimization while outperforming feed-forward methods trained on production-quality 3D data, all from a single camera view. Finally, we introduce Multi4D, a public benchmark for evaluating 4D facial reconstruction methods in lightstage environments, enabling topology-invariant geometric comparison across methods.

</details>

### 5. OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2608.29881](https://arxiv.org/abs/2608.29881)  · [📄 PDF](https://arxiv.org/pdf/2608.29881)
- **作者**: Muxin Liu, Tianbo Liu, Jing Xia et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 针对单目深度估计在透明、反射和镜面等光学挑战场景中可靠性差，现有方法依赖场景特定预处理或后处理导致架构冗余和过专业化的问题，本文识别出传感器诱导的监督偏差为关键瓶颈，即模型从有偏的真实深度监督中继承传感器失效模式。为此提出OptiGeo，一个偏差感知训练框架，利用干净几何教师和残差修剪对齐来修复有偏真实监督，并将透明目标渲染重新定义为紧凑的干净光学几何源。仅用小型目标渲染集，OptiGeo即可学习透明物体的几何结构，提升光学挑战场景下的深度估计鲁棒性，对自动驾驶感知具有直接应用价值。
- **摘要（英）**: This paper addresses the reliability issue of monocular depth estimation in optically challenging scenes like transparent and reflective environments, identifying sensor-induced supervision bias as a key bottleneck where models inherit sensor failure patterns from biased real-depth supervision. It proposes OptiGeo, a bias-aware training framework that rehabilitates biased supervision using a clean-geometry teacher and residual-trimmed alignment, redefining transparency-targeted rendering as a compact clean optical geometry source. With a small targeted rendering set, OptiGeo learns transparent object geometry, improving depth estimation robustness, with direct application to autonomous driving perception.
- **评估**: 该论文针对自动驾驶中的光学挑战场景提出了有效解决方案，偏差感知训练思路新颖，实用性强，值得关注。
- **核心贡献**: 提出了OptiGeo偏差感知训练框架，修复光学挑战场景中的深度监督偏差。
- **创新点**: 将透明目标渲染作为干净几何源，结合残差修剪对齐提升鲁棒性。
- **结果**: 仅用小型渲染集即可学习透明物体几何，显著提升深度估计性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation has achieved strong open-domain generalization, yet reliable robotic deployment remains difficult in transparent, reflective, and specular environments, where depth sensors often produce missing or biased depth. Existing methods often handle such optical failures with scene-specific preprocessing, auxiliary modules, or post-hoc fine-tuning. While effective in constrained settings, these designs increase architectural redundancy and can over-specialize general geometry models to narrow optical scenarios. We revisit this problem as a localized failure mode within base-model training and identify sensor-induced supervision bias as a key bottleneck: models inherit sensor failure patterns from biased real-depth supervision in optically challenging regions. We then introduce OptiGeo, a bias-aware training framework that rehabilitates biased real supervision using a clean-geometry teacher and residual-trimmed alignment. We redefine transparency-targeted rendering as a compact source of clean optical geometry, rather than a large domain-specific fine-tuning set. With only a small targeted rendering set, OptiGeo learns the geometric structure of transparent objects and regions, correcting local geometry distortions that real sensors cannot reliably supervise. Despite only 30M parameters, OptiGeo outperforms substantially larger 300M-scale monocular models and billion-scale multi-view baselines on transparent-scene benchmarks, while remaining competitive on general zero-shot depth and boundary sharpness. Real-world navigation cases further validate its practicality as an efficient perception module in optically challenging scenes.

</details>

### 6. SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.31023](https://arxiv.org/abs/2608.31023)  · [📄 PDF](https://arxiv.org/pdf/2608.31023)
- **作者**: Haozheng Yu, Xinyu Yang, Rundong Luo et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对单目视频动态高斯泼溅中，模型容易过拟合训练视图，在遮挡或复杂运动下缺乏正则化信号的问题。②提出了语义运动图（SMG），将高斯运动建模为低秩语义运动，利用语义一致性先验，由可靠图节点引导不可靠节点。③相比现有动态高斯泼溅方法，SMG通过语义结构约束运动，减少过拟合。④在自建的多视角数据集上，SMG在动态场景建模中表现出更好的泛化能力。
- **摘要（英）**: This paper addresses overfitting in dynamic Gaussian splatting from monocular videos under occlusion or complex motion. It proposes Semantic Motion Graph (SMG), modeling Gaussian motion as low-rank semantic motion driven by graph nodes, using semantic coherence priors. SMG improves generalization in dynamic scenes, validated on a new multiview dataset.
- **评估**: 该方法对动态场景建模有创新，与自动驾驶中的动态物体感知相关，但实验数据集为自建，泛化性待验证。
- **核心贡献**: 提出了SMG，利用语义运动图建模动态高斯泼溅中的结构化运动。
- **创新点**: 通过语义一致性先验和可靠节点引导，减少欠约束区域的运动不确定性。
- **结果**: 在自建数据集上提升了动态场景建模的泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study dynamic Gaussian Splatting from monocular videos. While recent advancements in dynamic Gaussian splatting offer a promising foundation for modeling dynamic scenes, they often overfit to the training views and fail under occlusion or complex scene motion due to the lack of reliable regularization signals in under-constrained regions. We propose Semantic Motion Graph (SMG), a novel approach models the Gaussian motion as the low-rank semantic motion. Our key insight is that the real-world scene motion is often structured by semantic coherence: regions that are spatially close and semantically related tend to exhibit consistent dynamics. To leverage this prior, we construct SMG to model structured motion of the scene. The Gaussian motion is driven by the motion of SMG nodes. We further observe that the uncertainty of Gaussian motion arises from both unreliable off-the-shelf priors and weakly constrained regions during optimization. SMG addresses this by using reliable graph nodes to guide the motion of nearby unreliable nodes. To evaluate dynamic Gaussian splatting under challenging real-world scenarios, we introduce a new multiview dataset collected under an ego-exo setup. Extensive experiments demonstrate that SMG achieves state-of-the-art performance on monocular dynamic Gaussian splatting across challenging real-world benchmarks. Project page: https://smg-gaussian.github.io/.

</details>

### 7. VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement **⭐⭐⭐⭐** (相关度: 65%, 质量: 0.75)

- **arXiv ID**: [2608.30870](https://arxiv.org/abs/2608.30870)  · [📄 PDF](https://arxiv.org/pdf/2608.30870)
- **作者**: Kun Cao, Di Wang, Haibin Zhu et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/DDKK0526/VCAR](https://github.com/DDKK0526/VCAR)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对3D高斯泼溅语义分割中，特征蒸馏方法训练开销大且边界模糊的问题。②提出了VCAR，一种无需训练的粗到细分割策略，基于视图完整性和轴感知边界细化，包括可见性加权多视图投票和球面螺旋采样生成补充视角。③相比现有方法，VCAR通过轴感知边界细化抑制各向异性高斯原语的边界溢出。④实验表明，VCAR在分割精度和边界质量上优于现有方法，同时无需训练开销。
- **摘要（英）**: This paper addresses high training overhead and blurred boundaries in 3DGS semantic segmentation. It proposes VCAR, a training-free coarse-to-fine strategy using visibility-weighted voting and axis-aware boundary refinement. VCAR improves segmentation accuracy and boundary quality without per-scene training.
- **评估**: 该方法在3D场景理解中具有实用价值，与自动驾驶中的3D感知相关，创新点明确且实验充分。
- **核心贡献**: 提出了VCAR，一种无需训练的3DGS分割方法，结合视图完整性和轴感知细化。
- **创新点**: 引入轴感知边界细化，分解2D协方差以抑制各向异性原语伪影。
- **结果**: 在分割精度和边界质量上优于现有方法，且无需训练开销。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semantic segmentation in 3D Gaussian Splatting (3DGS) is crucial for advancing 3D scene understanding. Existing methods predominantly rely on feature distillation, which incurs substantial per-scene training overhead and often yields blurred segmentation boundaries. We identify that these boundary artifacts are driven in part by insufficient viewpoint coverage and boundary overflow of anisotropic Gaussian primitives. To address these challenges, we propose VCAR, a training-free coarse-to-fine segmentation strategy based on View Completeness and Axis-aware Boundary Refinement. In the coarse stage, a visibility-based weighted multi-view voting scheme rapidly localizes the target. In the fine stage, an object-centric sphere derived from the coarse result generates supplementary viewpoints via Spherical Spiral Sampling (SSS), allowing multi-view voting on the augmented views to precisely refine object boundaries and suppress irrelevant 3D Gaussians. Moreover, we introduce Axis-aware Boundary Refinement (ABR) to mitigate artifacts from anisotropic primitives. By decomposing the projected 2D covariance into per-axis contributions, ABR identifies the dominant axis responsible for boundary leakage and applies targeted anisotropic compression exclusively along that axis. Extensive experiments on NVOS and LERF demonstrate that VCAR achieves state-of-the-art segmentation accuracy and efficiency without training. Our code is available at https://github.com/DDKK0526/VCAR.

</details>

### 8. Proximity3D: Shape from Capacitive Proximity on Sensing Manifold **⭐⭐** (相关度: 10%, 质量: 0.5)

- **arXiv ID**: [2608.30344](https://arxiv.org/abs/2608.30344)  · [📄 PDF](https://arxiv.org/pdf/2608.30344)
- **作者**: Hao Chen, Chenming Wu, Chun Ping Lam et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.CG, cs.GR
- **摘要（中）**: ①针对传统形状重建方法假设测量域为平面（如RGB图像或深度图）的问题，该论文提出利用曲面电容纺织物作为形状传感器，将其表面视为非平面感知流形。②方法上，每个扫描表示为该流形上的电容邻近场，由曲面电极布局与附近物体几何的交互产生，并引入多视图前馈重建模型聚合已知传感器视图的场并恢复物体形状。③相比平面域方法，创新在于处理非平面感知域，利用嵌入式传感实现机器人近场几何感知。④模拟和物理实验表明，该方法能从曲面传感表面的电容邻近信号中稳健重建形状，为机器人近场感知开辟新途径。
- **摘要（英）**: This paper addresses shape reconstruction from capacitive proximity signals on curved sensing surfaces, proposing a multi-view feedforward model that aggregates proximity fields on a non-planar manifold. It demonstrates robust reconstruction in simulated and physical experiments, offering a new route to robotic near-field geometric awareness via embodied sensing.
- **评估**: 该论文与自动驾驶感知领域关联度较低，主要面向机器人触觉/近场感知，但方法上对非平面感知流形的处理有一定新颖性。
- **核心贡献**: 提出首个利用曲面电容传感流形进行形状重建的多视图框架。
- **创新点**: 将非平面感知流形引入形状重建，替代传统平面域假设。
- **结果**: 模拟和物理实验验证了曲面电容信号下的稳健形状重建。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most shape reconstruction methods assume measurements defined over planar sensing domains, such as RGB images or depth maps. In this paper, we use a curved capacitive textile as a shape sensor, treating its surface as a non-planar sensing manifold. Each scan is represented as a capacitive proximity field on this manifold, induced by the interaction between the curved electrode layout and nearby object geometry. We introduce a multi-view feedforward reconstruction model that aggregates these fields across known sensor views and recovers the observed object shape. Simulated and physical experiments demonstrate robust reconstruction from capacitive proximity signals acquired on curved sensing surfaces, pointing toward a new route to robotic near-field geometric awareness via embodied sensing.

</details>

### 9. Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.30129](https://arxiv.org/abs/2608.30129)  · [📄 PDF](https://arxiv.org/pdf/2608.30129)
- **作者**: Bingde Liu, Wu Ran, Jinglei Zhang et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对生成式单目深度估计中标准注意力O(N^2)复杂度和多步去噪导致的高计算成本问题，该论文提出Lapis框架，实现一步扩散的高效高保真深度估计。②方法上，采用线性注意力机制和像素空间生成框架，通过粗到细层级结构：Patch级一致性模块整合语义和空间先验恢复结构连贯性，像素级细化模块利用跳跃连接恢复锐利几何边界。③相比直接应用线性注意力和一步预测，Lapis解决了结构一致性差、细节丢失和噪声问题，并采用x-预测策略直接目标干净数据流形以减少采样噪声。④实验表明，Lapis在保持高保真细节的同时显著提升效率，适用于高分辨率图像应用。
- **摘要（英）**: This paper introduces Lapis, a linear-attention-based pixel-space generative framework for efficient one-step diffusion depth estimation, addressing the computational bottlenecks of standard attention and multi-step denoising. It employs a coarse-to-fine hierarchy with patch-level consistency and pixel-level refinement modules, achieving high-fidelity depth with reduced noise and improved structural consistency.
- **评估**: 该论文在深度估计领域具有较高创新性和实用性，对自动驾驶感知中的单目深度估计有直接参考价值，但主题更偏向生成式方法而非传统检测。
- **核心贡献**: 提出线性注意力像素空间生成框架，实现高效一步扩散深度估计。
- **创新点**: 粗到细层级结构结合语义先验和跳跃连接，解决一步扩散中的结构一致性问题。
- **结果**: 在保持高保真细节的同时显著降低计算成本，适用于高分辨率场景。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work presents $\textbf{Lapis}$, a $\textbf{l}$inear-$\textbf{a}$ttention-based $\textbf{pi}$xel-$\textbf{s}$pace generative framework that achieves efficient and high-fidelity depth estimation with one-step diffusion. While generative frameworks have significantly advanced monocular depth estimation with superior detail fidelity, the $\mathcal{O}(N^2)$ complexity of standard attention and the multi-step denoising process introduce prohibitive computational costs when scaling them to high-resolution image applications. Although linear attention and one-step prediction are intuitively viable, directly applying them leads to poor structural consistency, detail loss, and noise. Lapis rectifies these limitations through a coarse-to-fine hierarchy. Specifically, a Patch-level Consistency Module restores structural coherence by integrating semantic and spatial priors. Subsequently, a Pixel-level Refinement Module recovers sharp geometric boundaries via skip-connection-based pixel correspondence. Furthermore, to mitigate sampling noise inherent in one-step diffusion, we leverage the manifold assumption and adopt a direct $\mathbf{x}$-prediction strategy to target the clean data manifold. Extensive evaluations on multiple benchmarks demonstrate that Lapis consistently achieves state-of-the-art (SOTA) accuracy and boundary sharpness across various resolutions, reducing inference latency by up to 7.6$\times$ at 1080P and 10.9$\times$ at 1440P resolution compared to previous SOTA generative models.

</details>

---

## Video Understanding

### 1. Motion-Saliency Complementary Masked Modeling for Point Cloud Video Understanding **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2608.30279](https://arxiv.org/abs/2608.30279)  · [📄 PDF](https://arxiv.org/pdf/2608.30279)
- **作者**: Wei Wang, Yiding Sun, Yuyan Wang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对点云视频自监督表示学习中运动信息捕获不足的问题，提出了MoSaiC框架，包含课程运动显著性掩码（CMSM）、法向流运动建模（NFM）和跨视图令牌一致性预测（CTCP）三个组件。相比现有掩码建模方法，该方法显式建模局部刚体旋转和运动显著性，增强了外观与运动动态的联合学习。在动作识别、时间动作分割和点级语义分割等下游任务上验证了有效性。
- **摘要（英）**: To address insufficient motion capture in self-supervised point cloud video representation learning, this paper proposes MoSaiC, integrating curriculum motion-saliency masking, normal-flow motion modeling, and cross-view token consistency prediction. It explicitly models local rigid rotations and motion saliency, improving joint appearance-motion learning. Experiments on action recognition, temporal segmentation, and semantic segmentation demonstrate effectiveness.
- **评估**: 该工作为点云视频自监督学习提供了新思路，运动显著性掩码和几何运动建模具有创新性，对3D动态场景理解有重要参考价值。
- **核心贡献**: 提出了一种结合运动显著性和几何建模的自监督点云视频表示学习框架。
- **创新点**: 将法向流运动建模和课程掩码策略引入点云视频掩码建模。
- **结果**: 在多个下游任务上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point cloud video representation learning is crucial for 3D dynamic scene understanding. In this paper, we propose MoSaiC, a novel Motion-Saliency Complementary masked modeling framework for self-supervised point cloud video representation learning. MoSaiC couples three components: Curriculum Motion-Saliency Masking (CMSM), which guides the masking process toward motion-salient tokens under a curriculum schedule; Normal-Flow Motion (NFM) modeling, which supervises the local rigid rotation of each token in the Lie algebra so(3) as an explicit geometric motion target; and Cross-view Token Consistency Prediction (CTCP), which enforces consistency between two complementary masked views at the token level. Together, these components allow MoSaiC to effectively capture both appearance and motion dynamics. Extensive experiments on multiple downstream tasks, including action recognition, temporal action segmentation, and point-level semantic segmentation, demonstrate the effectiveness of our approach.

</details>

### 2. RIDGE: Region-Informed Derivative-Guided Evidence Selection for Long Video Understanding **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2608.29958](https://arxiv.org/abs/2608.29958)  · [📄 PDF](https://arxiv.org/pdf/2608.29958)
- **作者**: Shanqing Xu, Meng Luo, Mengchen Qian et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 针对长视频理解中帧选择仅依赖相似度值排序而忽略时间结构的问题，提出了RIDGE框架，将帧-查询相似度曲线视为时间信号，利用局部变化和曲率划分时间线为结构区域，并应用区域特定选择以保留事件核心、过渡、铺垫、余波和上下文帧。该方法作为预计算分数的轻量级后处理步骤，无需训练或迭代LVLM调用。
- **摘要（英）**: To address frame selection in long video understanding that ignores temporal structure, this paper proposes RIDGE, which treats frame-query similarity as a temporal signal, partitions timeline into structural regions using curvature, and applies region-specific selection. It is a lightweight post-processing step requiring no training.
- **评估**: 该工作从信号处理角度重新审视帧选择问题，具有新颖性，但效果数据未在摘要中给出，需进一步验证。
- **核心贡献**: 提出了一个基于相似度曲线形状的帧选择框架，用于长视频理解。
- **创新点**: 将帧选择问题转化为时间信号的结构区域分析。
- **结果**: 摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long videos contain far more visual content than Large Vision-Language Models (LVLMs) can process under a fixed visual-token budget, making frame selection essential. Existing query-aware selectors usually estimate frame-query relevance and build a compact subset from high-scoring frames. Although their mechanisms differ, the similarity sequence is still often treated primarily as values to rank or sample from, rather than as an ordered signal whose shape reflects how query-relevant evidence emerges, peaks, and fades over time. This can obscure frames that explain, contextualize, or follow an event, because such evidence may lie on the rising or falling sides of a nearby relevance peak and receive lower absolute scores. We propose RIDGE, a frame selection framework that reads the frame-query similarity curve as a temporal signal. By using local changes and curvature, RIDGE partitions the timeline into structural regions and applies region-specific selection to preserve event cores, transitions, buildup, aftermath, and contextual frames under a fixed budget. It is a lightweight post-processing step on precomputed frame-query scores and requires neither training nor iterative LVLM calls. Across four long-video benchmarks and three backbones, RIDGE achieves the best performance in most settings and remains competitive in the others.

</details>

### 3. Learning Compositional Spatio-Temporal Video Grounding with Synthetic Curriculum **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.30584](https://arxiv.org/abs/2608.30584)  · [📄 PDF](https://arxiv.org/pdf/2608.30584)
- **作者**: Xingjian Wang, Shijian Wang, Yibo Wang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对现有时空视频定位（STVG）方法在处理真实场景中组合查询（需联合推理属性和关系）时表现不佳的问题，提出了CompSTVG任务。构建了一个合成数据引擎，利用时空场景图作为难度度量，将难度控制的查询合成建模为约束规划问题，生成分级难度的训练和评估数据。基于该引擎构建了STVG-CompBench基准，按显式难度级别分层。对11个代表性STVG模型的评估显示，现有模型在组合查询上表现较差，揭示了该任务的挑战性。
- **摘要（英）**: This paper addresses the poor performance of existing spatio-temporal video grounding (STVG) methods on compositional queries requiring joint reasoning about attributes and relations. It proposes CompSTVG, a new task, and builds a synthetic data engine using spatio-temporal scene graphs as difficulty measures, casting query synthesis as constraint programming. A benchmark, STVG-CompBench, is introduced, and evaluation of 11 models reveals significant limitations on compositional queries.
- **评估**: 该论文提出了一个新颖且具有挑战性的任务，并提供了系统化的数据生成和评估框架，对推动视频理解领域向复杂查询发展有重要价值。
- **核心贡献**: 提出了CompSTVG任务和STVG-CompBench基准，并构建了基于约束规划的合成数据引擎。
- **创新点**: 利用时空场景图作为难度度量，将组合查询合成形式化为约束规划问题。
- **结果**: 揭示了现有STVG模型在组合查询上的显著不足，为后续研究提供了基准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the impressive progress of recent MLLMs on spatio-temporal video grounding (STVG), existing evaluations and training data focus primarily on simple queries. They largely overlook the compositional queries prevalent in real-world scenarios, where a target must be disambiguated by jointly reasoning about its attributes and relations to other entities. To bridge this gap, we propose Compositional Spatio-Temporal Video Grounding (CompSTVG), a task that requires models to process complex textual queries where every intertwined attribute and relational cue is essential for disambiguation. To facilitate this task at scale, we build a synthetic data engine that leverages a spatio-temporal scene graph as a difficulty measure and casts difficulty-controlled query synthesis as a constraint programming problem, producing difficulty-graded data for both evaluation and training. Built on this engine, we introduce STVG-CompBench, a benchmark stratified by explicit difficulty levels that jointly capture temporal complexity and spatial interference. Evaluating 11 representative STVG models on STVG-CompBench reveals that current models perform poorly on compositional queries, exhibiting a sharp performance drop that is typically obscured by overall dataset-level averages. We further construct synthetic training data and propose CurrSTVG, a curriculum reinforcement learning framework that delivers consistent gains, with the largest improvements observed on the most challenging compositional queries.

</details>

### 4. PRISM: Predictive Recomposition via Semantic Latent Decomposition for View-invariant Video Representation Learning **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.85)

- **arXiv ID**: [2608.30388](https://arxiv.org/abs/2608.30388)  · [📄 PDF](https://arxiv.org/pdf/2608.30388)
- **作者**: Youngchae Chee, Hosu Lee, Sungjune Park et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/litcoderr/prism](https://github.com/litcoderr/prism)
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对跨视角视频表示学习中，视角不变和视角变化语义在统一嵌入中纠缠的问题，提出PRISM方法。核心思想是，当视角不变特征能与任意视角变化特征充分重组且保持独立语义时，才实现真正解耦。PRISM将视频分解为视角不变和视角变化潜变量，并在语言监督下重组，鼓励两流清晰分离。在EgoExo4D、EgoExoLearn和AE2上取得最先进结果，零样本设置下甚至超越领域内模型。
- **摘要（英）**: This paper tackles the entanglement of view-invariant and view-variant semantics in cross-view video representation learning. PRISM decomposes videos into view-invariant and view-variant latents and recomposes them under language supervision for clean separation. It achieves state-of-the-art results on EgoExo4D, EgoExoLearn, and AE2, surpassing in-domain models in zero-shot settings.
- **评估**: 提出了一种新颖的解耦视角不变表示方法，通过重组机制和语言监督，显著提升了跨视角视频理解的泛化能力。
- **核心贡献**: 提出了PRISM框架，通过语义潜变量分解和重组实现视角不变视频表示学习。
- **创新点**: 将解耦条件定义为与任意视角变化特征的可重组性，并利用语言监督促进分离。
- **结果**: 在多个跨视角基准上取得最先进性能，零样本设置下表现优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-view video representation learning aims to capture viewpoint-invariant action semantics despite substantial appearance changes across egocentric and exocentric videos. However, existing methods encode each video as a unified embedding, where view-invariant and view-variant semantics inevitably entangle under co-occurrences - a failure mode we show persists even in cross-view methods explicitly trained for view-invariance. Our key insight is that a view-invariant feature is truly disentangled when it can be sufficiently recomposed with an arbitrary view-variant feature while preserving their independent semantics. Building on this, we propose PRISM, that decomposes video into view-invariant and view-variant latents and recompose them under language supervision encouraging clean decomposition of the two streams. PRISM achieves state-of-the-art results on EgoExo4D, EgoExoLearn, AE2, even surpassing in-domain models under zero-shot setting. Code is available at https://github.com/litcoderr/prism.

</details>

### 5. Dynamic Hub-and-Spoke Memory for Streaming Video Understanding **⭐⭐⭐⭐** (相关度: 65%, 质量: 0.8)

- **arXiv ID**: [2608.30294](https://arxiv.org/abs/2608.30294)  · [📄 PDF](https://arxiv.org/pdf/2608.30294)
- **作者**: Xinru Jiang, Lin Zhao, Xi Xiao et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对流式视频理解中需在任意时刻回答关于持续增长视觉流的问题，且需紧凑记忆长历史并有效检索相关证据的挑战，提出动态枢纽-辐条记忆（D-HSM）框架。该框架无需训练，将远处历史表示为结构化文本记忆，保留近期帧为视觉令牌。D-HSM将历史视频块转为类型化文本观察，存储在实体中心的枢纽-辐条记忆中，回答问题时动态检索紧凑子集并扩展。在流式和长视频基准上，D-HSM一致且显著提升VLM骨干性能，并超越其他在线和离线基线。
- **摘要（英）**: This paper addresses streaming video understanding by proposing Dynamic Hub-and-Spoke Memory (D-HSM), a training-free framework that stores distant history as structured textual memory while keeping recent frames as visual tokens. It dynamically retrieves question-aware memory subsets and combines them with the recent visual window for frozen-VLM inference. D-HSM consistently improves VLM backbones and outperforms state-of-the-art baselines on streaming and long video benchmarks.
- **评估**: 该工作提供了一种高效且无需训练的流式视频理解方案，通过结构化记忆和动态检索显著增强了VLM的长期建模能力。
- **核心贡献**: 提出了D-HSM框架，利用实体中心的枢纽-辐条记忆实现流式视频理解。
- **创新点**: 将历史视频转为类型化文本记忆，并采用动态检索和扩展机制。
- **结果**: 在多个基准上显著提升VLM性能，超越现有在线和离线方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Streaming video understanding requires answering questions at arbitrary times over a continuously growing visual stream. The central challenge is to compactly remember long-range history while effectively retrieving question-relevant evidence. We propose Dynamic Hub-and-Spoke Memory (D-HSM), a training-free framework that represents distant history as structured textual memory while preserving the recent frames as visual tokens for fine-grained perception. Specifically, D-HSM turns selected historical video chunks into typed textual observations and stores them in an entity-centered hub-and-spoke memory, with entities as hubs and related evidence as spokes. When answering a question, D-HSM dynamically retrieves a compact question-aware memory subset, expands it through hub-and-spoke links, and combines it with the recent visual window for frozen-VLM answer prediction. Extensive experiments on both streaming and long video benchmarks show that D-HSM consistently and substantially improves VLM backbones and outperforms other state-of-the-art online and offline video understanding baselines.

</details>

### 6. ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2608.30184](https://arxiv.org/abs/2608.30184)  · [📄 PDF](https://arxiv.org/pdf/2608.30184)
- **作者**: Jiahao Wu, Jie Liang, Die Hu et al. (9 authors)
- **🏷️ 机构**: Peking University, shenzhen, China, Pengcheng Laboratory, shenzhen, China
- **💻 代码**: [github.com/WuJH2001/ATGS](https://github.com/WuJH2001/ATGS)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对体积视频表示中长序列和复杂运动导致的时间不稳定和视觉伪影问题，提出ATGS（锚定时间高斯泼溅）框架。核心思想是，用单个高斯原语显式跟踪长期复杂运动本质不稳定，因此将高斯组织在时间条件锚点周围，局部化其时空支持，降低长程运动复杂度。引入时间窗口策略仅激活查询时间相关的锚点，提升可扩展性和时间连贯性。设计紧凑的多级锚点特征编码全局、局部空间和局部时间特征，约束高斯生成。实验表明，ATGS在长序列复杂运动体积视频上持续优于先前方法。
- **摘要（英）**: This paper addresses temporal instability and artifacts in long volumetric videos with complex motions by proposing ATGS, a Gaussian splatting framework. It organizes Gaussians around time-conditioned anchors to reduce long-range motion complexity and uses a temporal windowing strategy for scalability. Multi-level anchor features encode global, spatial, and temporal information, and experiments show consistent improvements over prior methods.
- **评估**: 该工作针对体积视频表示中的长序列和复杂运动问题提出了有效的锚定策略，具有较好的实用价值，但创新性相对常规。
- **核心贡献**: 提出了ATGS框架，通过时间条件锚点和多级特征实现稳定的长体积视频表示。
- **创新点**: 利用时间条件锚点局部化高斯支持，降低长程运动复杂度。
- **结果**: 在长序列复杂运动体积视频上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Volumetric video enables immersive free viewpoint rendering of dynamic real world scenes, yet existing methods struggle with long sequences and complex motions, often leading to temporal instability and visual artifacts. To address these challenges, we propose \ourname, a Gaussian splatting based framework for volumetric video reconstruction. Our key insight is that explicitly tracking long term complex motion with individual Gaussian primitives is inherently unstable. Instead, we organize Gaussians around time conditioned anchors that localize their spatial and temporal support, thereby reducing long range motion complexity. We further introduce a temporal windowing strategy to activate only anchors relevant to the queried time, which improves scalability and temporal coherence. In addition, to ensure spatial and temporal stability, we design a compact set of multi level anchor features that encode global features, local spatial features, and local temporal features, jointly constraining Gaussian generation. Extensive experiments demonstrate that \ourname \ consistently outperforms prior methods on long sequence volumetric videos with complex motions. Project page: https://github.com/WuJH2001/ATGS.

</details>

### 7. Everybody Tracking Every Body **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.29927](https://arxiv.org/abs/2608.29927)  · [📄 PDF](https://arxiv.org/pdf/2608.29927)
- **作者**: Daeyun Shin, Yunhan Zhao, Shu Kong et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: ①针对多人在自我中心视角下的3D姿态估计问题，该论文提出集中协调的扩散方法。②方法上，每个个体佩戴相机记录自我中心视频和IMU数据，通过VIO SLAM跟踪相机运动，融合基于头部运动的姿态估计和外部视角姿态观测，并基于观测内容和可靠性进行条件化。③相比仅运动或仅视觉基线，创新在于扩散模型融合多模态数据流，学习身体运动轨迹和视频观测可靠性的丰富先验。④在挑战性多人物数据集上的评估表明，融合方法在绝对和相对姿态精度上均优于基线。
- **摘要（英）**: This paper addresses multi-person 3D pose estimation from egocentric views with centralized coordination, proposing a diffusion-based fusion of head-motion-derived poses and exocentric observations conditioned on reliability. It learns rich priors from motion capture and multi-person video, improving both absolute and relative pose accuracy over motion-only and vision-only baselines.
- **评估**: 该论文在多人姿态估计和跟踪领域具有较高创新性，对自动驾驶中的行人感知和交互场景有参考价值，但更偏向可穿戴设备应用。
- **核心贡献**: 提出扩散模型融合自我中心多模态数据，实现多人3D姿态估计。
- **创新点**: 基于观测可靠性的条件化融合，结合运动先验和视频观测。
- **结果**: 在多人数据集上优于运动仅和视觉仅基线，提升姿态精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the problem of 3D body pose estimation of multiple interacting people from their egocentric views with centralized coordination. Each individual wears a camera recording egocentric video and IMU data. Processing this video with VIO SLAM provides high-quality tracking of each egocentric camera through space. The first-person view from one individual provides third-person observations of other people, although these exocentric observations are sparse, intermittent, and of highly variable reliability as both cameras and subjects move. To integrate these synchronized data streams, we propose a diffusion-based approach that fuses estimates of pose based on head motion derived from egocentric camera motion with exocentric pose observations, conditioning on both observation content and reliability. Our model is trained on a mixture of single-person motion-capture data and multi-person video in order to learn rich priors for body motion trajectories and video observation reliability. Evaluation on challenging multi-person datasets suggests our fusion approach improves over motion-only and vision-only baselines in terms of both absolute and relative pose accuracy.

</details>

---

## Self-supervised Vision

### 1. MCSeg: Pre-training and Fine-tuning Volumetric Pyramid Transformer for Multi-modal Cardiac Image Segmentation **⭐⭐** (相关度: 20%, 质量: 0.7)

- **arXiv ID**: [2608.30371](https://arxiv.org/abs/2608.30371)  · [📄 PDF](https://arxiv.org/pdf/2608.30371)
- **作者**: Zhiyu Ye, Hairong Zheng, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对多模态心脏图像分割中混合网络架构不匹配的问题。现有混合网络难以有效桥接单尺度3D ViT编码器和多尺度CNN解码器。作者提出MCSeg，包含缩放特征金字塔（SFP）将ViT输出转换为层次特征金字塔，并采用掩码图像建模自监督预训练和区域互信息损失提升边界分割。在四个数据集上（ImageCHD、MM-WHS、HVSMR-2.0、MSD Heart）一致优于11种SOTA方法。该工作主要面向医学影像，与自动驾驶感知领域相关性低。
- **摘要（英）**: This paper addresses architectural mismatch in hybrid networks for multi-modal cardiac segmentation. The authors propose MCSeg with a Scaling Feature Pyramid to bridge ViT and CNN decoders, plus masked image modeling pre-training and regional mutual information loss. It outperforms 11 SOTA methods on four datasets, but is focused on medical imaging.
- **评估**: 该论文方法有通用性，但面向医学影像，与自动驾驶感知领域相关性低。
- **核心贡献**: 提出MCSeg网络和缩放特征金字塔，解决ViT-CNN混合架构的尺度不匹配。
- **创新点**: 通过SFP将单尺度ViT输出转换为多尺度特征金字塔，并集成RMI损失。
- **结果**: 在四个心脏分割数据集上优于11种SOTA方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Automatic cardiac image segmentation is pivotal for diagnosing and treating cardiac diseases. In this work, we introduce MCSeg, a volumetric transformer-based network tailored for multi-modal cardiac segmentation. To overcome the architectural mismatch inherent in existing hybrid networks, we propose a novel Scaling Feature Pyramid (SFP). Unlike conventional skip connections, the SFP effectively bridges the single-scale 3D Vision Transformer (ViT) encoder and the multi-scale CNN decoder by transforming the ViT's output into a hierarchical feature pyramid, ensuring that global contextual information is effectively leveraged. For the training paradigm, the ViT encoder first undergoes self-supervised pre-training via masked image modeling. Subsequently, the network is fine-tuned on downstream tasks, during which a regional mutual information (RMI) loss is integrated to improve boundary segmentation accuracy. In experiments, MCSeg consistently outperforms eleven SOTA methods on CT dataset ImageCHD, multi-modal dataset MM-WHS, MRI dataset HVSMR-2.0 and MSD Heart, highlighting the effectiveness of our MCSeg for multi-modal cardiac segmentation tasks. Furthermore, MCSeg's superior performance in few-shot experiment showcases its significant potential in adapting to limited data scenarios. Codes and pre-trained ViT-B weights are open-sourced at https://openi.pcl.ac.cn/OpenMedIA/MCSeg

</details>

### 2. Biomechanical 3D Body: Self-Supervised Distillation of Biomechanical Pose from a 3D Body Foundation Model **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.29928](https://arxiv.org/abs/2608.29928)  · [📄 PDF](https://arxiv.org/pdf/2608.29928)
- **作者**: R. James Cotton, J. D. Peiffer, Lucinda Williamson et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 针对单目人体恢复方法输出缺乏生物力学定义关节角的问题，该论文在SAM-3D-Body基础模型上扩展了一个生物力学预测头，从单张RGB图像回归生物力学模型的关节角度和尺度。通过Levenberg-Marquardt求解器对网格预测标记进行逆运动学拟合，生成优化目标来监督生物力学输出，实现从网格头到生物力学头的自监督蒸馏，无需配对图像-生物力学数据。模型在JAX和Equinox中实现，并在SAM-3D-Body数据集上训练，在MoVi和BioCV数据集上验证，展示了良好的泛化能力。
- **摘要（英）**: This paper addresses the lack of biomechanically defined joint angles in monocular body recovery by extending the SAM-3D-Body foundation model with a biomechanical prediction head that regresses joint angles and scales from a single RGB image. It uses in-loop optimized targets from a Levenberg-Marquardt solver for inverse kinematics fits against mesh markers, enabling self-supervised distillation from unlabeled images. The model, implemented in JAX with Equinox, is trained on SAM-3D-Body and validated on MoVi and BioCV, showing effective generalization.
- **评估**: 该论文将基础模型扩展到生物力学领域，自监督蒸馏策略具有创新性，但与应用领域（自动驾驶感知）相关性较低。
- **核心贡献**: 提出了一种从3D身体基础模型自监督蒸馏生物力学姿态的方法。
- **创新点**: 利用逆运动学求解器生成优化目标，实现无配对数据的生物力学头蒸馏。
- **结果**: 在MoVi和BioCV数据集上验证了模型的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art monocular body recovery methods predict mesh vertices and angles on the corresponding kinematic tree, but their outputs lack biomechanically defined joint angles that downstream applications like clinical and biomechanical analyses require. We extend an existing foundation model, SAM-3D-Body, with an additional biomechanical prediction head that, from a single RGB image, regresses the joint angles and scales of a biomechanical model. Training this model presents a challenge, as there are limited datasets of paired images and biomechanical fits. To overcome this, we supervise biomechanical outputs with in-loop optimized targets from a Levenberg-Marquardt solver performing inverse kinematics fits against markers from the mesh predictions. This allows distilling the biomechanical head from the mesh head, even from unlabeled images. To make this work with GPU-optimized biomechanical models in MuJoCo, the entire model was implemented in JAX using Equinox. We trained this distilled output head on the publicly released SAM-3D-Body dataset. We then validated this model on biomechanical fits to two publicly available marker-based datasets, MoVi and BioCV, as well as movements from a clinical cohort captured with multiview markerless motion capture. The resulting model outperforms existing models for direct regression of biomechanics from images while only slightly underperforming the state-of-the-art monocular biomechanics method that performs more costly inference-time optimization of entire trajectories.

</details>

### 3. Vision Models Predict Urban Scene Appraisal with Limited Neural Alignment **⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.30964](https://arxiv.org/abs/2608.30964)  · [📄 PDF](https://arxiv.org/pdf/2608.30964)
- **作者**: Kaizhen Tan, Yuantao Deng
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对预训练视觉嵌入在预测城市场景人类评分时，高预测精度并不代表其组织场景方式与人类感知一致的问题，本文利用63名成年人观看56个柏林街景的EEG数据，估计了场景的表征几何及其与17种特征空间（包括语言监督、自监督、类别监督和密集预测训练）的对应关系。结果显示，最佳表征DINOv2 ViT-B仅达到噪声下限的29.6%，所有模型跨度从11.0%到29.6%，且Gabor能量描述符与最佳模型无显著差异，表明视觉模型与人类神经响应的对齐度普遍较低。该研究揭示了视觉模型在场景理解上的局限性，但主题与自动驾驶感知关联较弱。
- **摘要（英）**: This paper investigates whether pretrained vision embeddings organize urban scenes as human perception does, beyond predictive accuracy, using EEG data from 63 adults viewing 56 Berlin street scenes. It finds that the best representation, DINOv2 ViT-B, reaches only 29.6% of the noise ceiling lower bound, with all models spanning 11.0% to 29.6%, and a Gabor energy descriptor matching the best model, indicating low neural alignment. The study highlights limitations of vision models in scene understanding, but its relevance to autonomous driving perception is limited.
- **评估**: 该研究对视觉表征与人类感知对齐的评估具有科学价值，但主题偏向认知神经科学，与自动驾驶感知领域相关性较低。
- **核心贡献**: 系统评估了17种视觉特征空间与人类脑电响应的对应关系，揭示低对齐度。
- **创新点**: 结合EEG数据与表征几何分析，分离预测精度与感知一致性。
- **结果**: 最佳模型DINOv2仅达噪声下限的29.6%，Gabor描述符与最佳模型相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained vision embeddings are increasingly used as general-purpose representations for modelling how people appraise urban scenes, and are validated almost entirely by how well they predict human ratings. High predictive accuracy does not establish that these embeddings organise scenes as human perception does. We test the two properties separately against brain data. Using openly released EEG from 63 adults who viewed and rated 56 Berlin street scenes, we estimate the representational geometry of the scenes over time, the proportion of that geometry that is explainable at all, and its correspondence with seventeen feature spaces spanning language-supervised, self-supervised, category-supervised and dense-prediction training, two orders of magnitude of scale, and interpretable controls. Correspondence is low throughout: the best representation, DINOv2 ViT-B, reaches 29.6% of the lower bound of the noise ceiling, the panel spans 11.0% to 29.6%, and a Gabor energy descriptor is indistinguishable from the best model while outperforming every language-supervised model tested. Within a model, deeper layers still match later neural responses, so the hierarchical correspondence found for object recognition survives even at this low overall level. The same embeddings predict held-out appraisal ratings well, up to r = 0.87, and the two measures do not track each other across models; reweighting features towards the neural geometry lowers appraisal prediction for every model tested, against a control of matched dimensionality. Predicting how a street is appraised is therefore weak evidence that a model represents the street as the brain does. The benchmark uses only public data and requires no training, so evaluating a new representation needs only its embeddings for 55 images.

</details>

### 4. Evaluating 2D and 3D-Aware Vision Foundation Models for Vehicle Attribute Recognition **⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.29929](https://arxiv.org/abs/2608.29929)  · [📄 PDF](https://arxiv.org/pdf/2608.29929)
- **作者**: Alexandre V. Delazeri, Gabriel E. Lima, Eduil Nascimento et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/UFPR-IPASPPR/3D-Vision-Benchmark](https://github.com/UFPR-IPASPPR/3D-Vision-Benchmark)
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 针对车辆属性识别中，视觉基础模型在细粒度分类上的有效性未充分探索，以及3D感知模型是否优于2D架构的问题，本文对14种先进的2D和3D感知视觉基础模型进行了实证基准测试。使用UFPR-VeSV数据集，通过线性探测评估冻结特征提取器在车辆类型、品牌和型号识别上的性能，并在少样本和OOD域偏移下进行压力测试。结果显示，标准2D自监督模型（特别是DINOv3）在细粒度任务上大幅优于3D感知模型，宏准确率超过93%，而3D感知的Depth Anything v2在不变性上表现更强。该研究为车辆识别中的模型选择提供了实用指导。
- **摘要（英）**: This paper addresses the underexplored effectiveness of vision foundation models for fine-grained vehicle attribute recognition and whether 3D-aware models outperform 2D architectures. It benchmarks 14 state-of-the-art 2D and 3D-aware models on the UFPR-VeSV dataset via linear probing, with few-shot and OOD stress tests. Results show that 2D self-supervised models, especially DINOv3, outperform 3D-aware models, achieving over 93% Macro-Accuracy for make and model recognition, while 3D-aware Depth Anything v2 shows stronger invariance. The study provides practical guidance for model selection in vehicle recognition.
- **评估**: 该论文对车辆属性识别中的模型选择有直接参考价值，但方法创新性一般，主要贡献在于实证评估。
- **核心贡献**: 系统评估了14种2D和3D感知基础模型在车辆属性识别上的性能。
- **创新点**: 首次对比2D和3D感知基础模型在细粒度车辆识别中的优劣。
- **结果**: DINOv3在品牌和型号识别上宏准确率超93%，3D模型在不变性上更强。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vehicle attribute recognition is an important task in intelligent transportation systems, particularly when Automatic License Plate Recognition (ALPR) is unavailable or unreliable. Although vision foundation models have shown strong transferability across domains, their effectiveness for fine-grained vehicle classification remains underexplored. Moreover, given the inherently three-dimensional structure of vehicles, it is unclear whether emerging 3D-aware foundation models offer advantages over standard 2D architectures. This paper presents an empirical benchmark of 14 state-of-the-art 2D and 3D-aware vision foundation models. Using the challenging real-world UFPR-VeSV dataset, we evaluate these models as frozen feature extractors via linear probing for vehicle type, make, and model recognition. We further stress-test the best-performing models under few-shot learning and Out-of-Distribution (OOD) domain shifts. Our results show that standard 2D self-supervised models, particularly DINOv3, substantially outperform 3D-aware models in fine-grained tasks, achieving over 93% Macro-Accuracy for make and model recognition. However, the 3D-aware Depth Anything v2 exhibits stronger invariance to viewing angles in vehicle type classification. These findings motivate hybrid approaches that combine 2D and 3D priors for robust vehicle recognition. Our code is publicly available at https://github.com/UFPR-IPASPPR/3D-Vision-Benchmark/.

</details>

### 5. BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.31113](https://arxiv.org/abs/2608.31113)  · [📄 PDF](https://arxiv.org/pdf/2608.31113)
- **作者**: Pradyumn Goyal, Yizhak Ben-Shabat, Hsueh-Ti Derek Liu et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对视频驱动3D网格动画中依赖显式骨架或高维顶点回归的问题，提出BLARM方法，通过学习紧凑的时变刚性运动组件和时不变顶点蒙皮权重来表示动画，无需骨架或绑定。该方法使用分解时空注意力将几何变形潜码与视频特征融合，并通过轨迹重建、熵正则化和运动感知对比学习训练。BLARM生成准确且时间稳定的动画，同时恢复紧凑可解释的运动结构。
- **摘要（英）**: To avoid explicit rigs or high-dimensional vertex regression in video-driven animation, BLARM represents motion via compact rigid components and skinning weights, decoded with factorized spatial-temporal attention. Trained with trajectory reconstruction and contrastive learning, it produces accurate, temporally stable animations with interpretable motion structure.
- **评估**: 该工作在3D动画领域有创新，但与自动驾驶感知相关性较低。
- **核心贡献**: 提出无需骨架的视频驱动3D动画方法。
- **创新点**: 使用刚性运动基元和蒙皮权重表示动画。
- **结果**: 生成准确且时间稳定的动画。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce BLARM, a feed-forward method for video-driven 3D mesh animation. Given a monocular video and a static object mesh, BLARM predicts a temporally coherent animated mesh whose motion follows the video. Rather than relying on explicit rigs or directly regressing high-dimensional vertex motion, we represent animation using a compact set of learned, time-varying rigid motion components and time-invariant vertex-to-component skinning weights. This yields a low-dimensional deformation space without requiring skeletons, cages, skinning weights, or rig annotations. Our architecture conditions geometry-derived deformation latents on video features through factorized spatial-temporal attention, then decodes rigid transformations blended by predicted skinning weights. Trained with trajectory reconstruction, entropy regularization, and motion-aware contrastive learning, BLARM produces accurate and temporally stable animations while recovering compact, interpretable motion structure from monocular video.

</details>

### 6. A Hybrid State-Space Approach for Census-Tract Population Estimation **⭐⭐⭐** (相关度: 50%, 质量: 0.6)

- **arXiv ID**: [2608.30094](https://arxiv.org/abs/2608.30094)  · [📄 PDF](https://arxiv.org/pdf/2608.30094)
- **作者**: Jackson R. Ye, Alexandre V. Morozov
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.LG
- **摘要（中）**: 针对人口估计中均匀栅格分解导致空间偏差的问题，提出MambaPop方法，将每个行政单元作为多边形掩膜卫星图像，将人口估计视为序列建模问题，直接配对图像和人口标签，消除分解步骤。基于混合状态空间-注意力MambaVision骨干，该方法首次将序列模型应用于人口估计，避免了传统方法的系统性偏差。
- **摘要（英）**: To address spatial bias from uniform raster disaggregation in population estimation, MambaPop treats each administrative unit as a polygon-masked image and formulates estimation as sequence modeling, eliminating disaggregation. Built on MambaVision, it directly pairs images with labels, reducing systematic bias.
- **评估**: 该工作对遥感应用有贡献，但自动驾驶领域相关性一般。
- **核心贡献**: 提出基于序列模型的人口估计方法，消除分解步骤。
- **创新点**: 将行政单元图像作为序列建模输入。
- **结果**: 避免了传统方法的空间偏差。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sequence models---the architecture family behind large language models and, increasingly, state-of-the-art image recognition---have redefined how machines learn from high-dimensional data. Yet population estimation from satellite imagery, a task that underpins infrastructure planning, public health, and disaster response, has scarcely benefited: leading systems still bind population to a uniform raster, disaggregating census counts onto grid cells through weighting surfaces built from ancillary data (e.g., in WorldPop and LandScan), which can introduce systematic spatial bias, and predicting population per grid cell with convolutional neural networks. In this approach, the administrative-unit structure in which the census was actually collected is discarded. We close this gap with MambaPop, which renders each administrative unit as a single polygon-masked satellite image and treats tract-level population estimation as a sequence-modeling problem over its image patches, pairing each tract image directly with its population label and eliminating the disaggregation step entirely. Built on the hybrid state-space--attention MambaVision backbone, MambaPop is, to our knowledge, the first method to learn population directly from an administrative unit's own image as well as the first to apply a state-space based (Mamba) hybrid architecture to the population estimation task. Across all $\sim$84{,}000 contiguous-US census tracts of the 2020 census, MambaPop attains a mean absolute error (MAE) of $1{,}141$ persons per tract, matching the strongest convolutional baseline (YOLOv11, MAE $1{,}122$).

</details>

---

## Vision Transformer

### 1. Seeing Through Extreme Visual Sparsity: Surface Understanding from a Single Random Visual Patch **⭐⭐** (相关度: 30%, 质量: 0.5)

- **arXiv ID**: [2608.29475](https://arxiv.org/abs/2608.29475)  · [📄 PDF](https://arxiv.org/pdf/2608.29475)
- **作者**: Sindhuja Penchala, Sudip Mittal, Noorbakhsh Amiri Golilarz
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: ①针对从极端稀疏视觉观测（仅10%可见像素）中同时进行表面重建和材料分类的问题。②提出了SSUF统一双任务学习框架，将ConvAE、ViT、Swin Transformer和MAE四种预训练架构扩展为同时具备重建和分类能力的模型。③通过为重建模型添加分类头、为分类模型添加重建解码器，实现了公平比较。④实验表明Swin Transformer在分类上最优，准确率89.21%，F1分数0.8922，但重建质量与效率因模型而异。
- **摘要（英）**: This paper addresses surface reconstruction and material classification from extremely sparse visual observations with only 10% visible pixels. It proposes SSUF, a unified dual-task framework adapting four pretrained architectures with added heads or decoders for fair comparison. Swin Transformer achieves the best classification accuracy of 89.21% and F1-score of 0.8922.
- **评估**: 该论文针对稀疏观测下的表面理解问题，但应用场景偏向机器人感知，与自动驾驶核心方向关联较弱，方法创新有限。
- **核心贡献**: 提出统一双任务框架SSUF，用于稀疏视觉下的表面重建与材料分类。
- **创新点**: 将多种预训练架构统一扩展为双任务模型，实现重建与分类的联合评估。
- **结果**: Swin Transformer在分类任务上达到89.21%准确率，验证了不同架构的适用性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Surface material recognition from incomplete visual observations remains a challenging problem in robotic perception and environmental understanding. This paper discusses Sparse Surface Understanding Framework (SSUF), a unified dual-task learning framework that adapts four pretrained architectures-Convolutional Autoencoder (ConvAE), Vision Transformer (ViT), Swin Transformer, and Masked Autoencoder (MAE) for si-multaneous surface reconstruction and material classification. Experiments were conducted on the Touch-and-Go dataset using a sparse observation protocol in which only 10% of the original image remained visible while the remaining regions were masked. To enable a fair comparison, reconstruction-oriented models were extended with classification heads, whereas classification- oriented models were augmented with reconstruction decoders. The resulting architectures were assessed using reconstruction quality, classification performance, model complexity, and in-ference efficiency metrics. Experimental results revealed distinct strengths across the models. Swin Transformer achieved the best classification performance with an accuracy of 89.21%, an F1-score of 0.8922, and a ROC-AUC of 0.9813. In contrast, MAE produced the highest reconstruction scores among evaluated models, with a PSNR of 16.06 dB and an SSIM of 0.4501, while ViT provided the best overall balance between reconstruction and classification performance. Furthermore, all models achieved real-time inference, requiring less than 5 ms per image. Over-all, the results show that pretrained architectures can support material recognition under severe visual sparsity, while accurate image reconstruction remains challenging.

</details>

### 2. Conducting Stylistic Analysis of Paintings through an Art-History Agent **⭐⭐** (相关度: 10%, 质量: 0.6)

- **arXiv ID**: [2608.29644](https://arxiv.org/abs/2608.29644)  · [📄 PDF](https://arxiv.org/pdf/2608.29644)
- **作者**: Marc S. Walton, Astrid Harth
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.AI, cs.CL
- **摘要（中）**: 该论文针对艺术史中绘画风格分析依赖人工观察、而现有AI模型仅提供不可解释概率分类的问题，提出一个自动化风格分析框架。方法上，用Vision Transformer在大规模绘画语料上训练编码嵌入，通过稀疏字典学习分解为共享特征，再由大语言模型解释特征并合成风格描述，最后用ReAct框架整合特征。相比已有工作，该框架弥合了艺术史方法论与AI之间的鸿沟，提供可解释的风格分析。摘要未给出定量结果，但框架在证据收集、发现和验证方面有潜力。
- **摘要（英）**: This paper addresses the gap between traditional art-historical stylistic analysis and unexplainable AI classifications by proposing an automated framework. It trains a ViT on paintings, factorizes embeddings via sparse dictionary learning, and uses LLMs to interpret features and synthesize descriptions with a ReAct coordinator. The approach enhances evidence collection and verification, though no quantitative results are reported.
- **评估**: 该论文与自动驾驶感知领域相关性极低，但提出了一种结合视觉Transformer和LLM的可解释分析框架，对跨领域方法有参考价值。
- **核心贡献**: 提出一个结合ViT、稀疏字典学习和LLM的自动化绘画风格分析框架。
- **创新点**: 将艺术史风格分析流程转化为可解释的AI框架，利用LLM合成特征描述。
- **结果**: 摘要未提供具体效果数据，但框架在风格分析任务上展示了可行性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Attributing an artwork to an artist has traditionally relied on detailed visual observations and descriptions, known as stylistic analysis in art history. By contrast, current artificial intelligence (AI) models used in the field offer only unexplained probabilistic classifications. To bridge this methodological gap, we present an AI framework that automates stylistic analysis of paintings, providing a foundation for enhancing evidence collection, discovery, and verification. By training a vision transformer (ViT) on a large corpus of paintings with metadata, our system encodes this art history-specific data as embeddings. These representations are factorized via sparse dictionary learning into a shared set of features that recur across the training set. A large language model (LLM) then interprets each feature by retrieving associated artworks and their accompanying curator-written texts, and synthesizes them into descriptions that reflect their stylistic attributes. Finally, an autonomous coordinator LLM applies a reasoning-and-action (ReAct) framework to weight, test, and refine these features into cohesive descriptions of an artwork, or comparisons of artworks. This approach converts detailed visual features into descriptive terms, addressing a key challenge in art history. It thus connects the use of images as data with the semantic concerns of humanists, establishing vision-based computational art history as an area for future growth.

</details>

### 3. A Controlled Evaluation of Model Rankings and Input Reliance in Surface Water Segmentation **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.30895](https://arxiv.org/abs/2608.30895)  · [📄 PDF](https://arxiv.org/pdf/2608.30895)
- **作者**: Kittipat Phunjanna, Kristóf Karacs, Chayut Ngamkhanong
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对地表水分割中仅用全局IoU排名模型配置无法解释性能差异和输入依赖性的问题，该论文进行受控评估。②方法上，通过重复配置比较、配对测试芯片分析、固定检查点输入压力测试和地理重加权，在Sen1Floods11数据集上系统评估，并在GEOID-Flood上二次验证。③相比仅用聚合指标，该研究揭示了排名在不同种子和地理加权下的不稳定性，以及辅助输入依赖性的架构差异。④结果表明，跨模态学生模型在Sen1Floods11上取得最高平均IoU，但排名不稳定；固定检查点测试显示对地形和WorldCover的依赖，但无干净输入性能提升。
- **摘要（英）**: This paper conducts a controlled evaluation of surface water segmentation models, using repeated comparisons and stress tests to analyze ranking stability and input reliance beyond aggregate IoU. It finds that rankings vary across seeds and geographic weighting, and that ancillary-input effects differ between architectures, highlighting the need for more nuanced evaluation.
- **评估**: 该论文对评估方法论有贡献，但主题与自动驾驶感知关联度一般，更偏向遥感应用。
- **核心贡献**: 系统评估了地表水分割模型排名的稳定性和输入依赖性。
- **创新点**: 引入固定检查点输入压力测试和地理重加权分析排名稳定性。
- **结果**: 揭示了跨模态学生模型的高性能但排名不稳定，以及辅助输入的架构依赖性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Performance evaluation for surface-water segmentation commonly uses an aggregate metric such as global intersection-over-union (IoU) to rank model configurations. However, a configuration ranking does not by itself establish why one system performs better, whether a close ordering is stable, or how strongly predictions rely on individual inputs. We examine these distinctions primarily on Sen1Floods11 through repeated configuration comparisons, paired test-chip analysis, fixed-checkpoint input stress tests, and geographic reweighting, with a targeted secondary evaluation of supervised input configurations on GEOID-Flood. The cross-modal student achieves the highest three-seed mean IoU on Sen1Floods11, but close orderings vary across seeds and geographic weighting, while ancillary-input rankings differ between Swin-UNet and U-Net. The GEOID-Flood evaluation shows substantial agreement in supervised ancillary-input effects, although the exact architecture ordering remains configuration dependent. Fixed-checkpoint tests further establish reliance on terrain and WorldCover without establishing a clean-input performance benefit, while target semantics and the later WorldCover prior restrict the evaluation to retrospective all-water segmentation. These results show that aggregate metrics remain useful for ranking complete configurations, but ranking stability, component attribution, input reliance, and deployment scope require distinct evidence. Performance evaluation should therefore match the evidence reported to the claim being made.

</details>

### 4. Quantum-Grassmann-Plucker Token Mixing for Deep Learning-Based Post-Disaster Damage Assessment **⭐⭐** (相关度: 20%, 质量: 0.5)

- **arXiv ID**: [2608.30633](https://arxiv.org/abs/2608.30633)  · [📄 PDF](https://arxiv.org/pdf/2608.30633)
- **作者**: Kooroush Farahkhah, Umut Lagap, Taha Rezaei et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对灾后建筑损伤评估中类别不平衡、中间损伤状态模糊和跨事件迁移性有限的问题，该论文首次将Grassmann-Plucker (GP) token mixing应用于计算机视觉。②方法上，提出量子启发GP头（QGP）和混合量子机器学习GP头（HQML-GP），通过编码token对形成的子空间和Plucker坐标表示多尺度关系，并融合振幅概率特征和模拟量子电路期望值。③相比MLP和Transformer基线，GP-based头在相同训练条件下进行比较，利用冻结的六通道Vision Transformer编码器处理配对前后事件图像。④在xBD龙卷风数据集上的实验表明，GP-based头在损伤分类中表现出潜力，但具体性能数据未在摘要中给出。
- **摘要（英）**: This paper applies Grassmann-Plucker token mixing to post-disaster damage assessment, introducing quantum-inspired and hybrid quantum machine learning heads that encode geometric token relationships. It compares these heads against MLP and Transformer baselines on xBD tornado data, showing potential for improved classification despite class imbalance and ambiguity.
- **评估**: 该论文创新性较强但应用领域与自动驾驶感知无关，且实验细节有限，整体重要性较低。
- **核心贡献**: 首次将Grassmann-Plucker token mixing引入视觉任务，用于灾后损伤评估。
- **创新点**: 量子启发GP头融合几何和量子特征，增强token表示。
- **结果**: 在xBD数据集上展示了GP-based头的分类潜力，但未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Timely post-disaster building damage assessment from satellite imagery is a critical engineering decision support task, yet it remains constrained by class imbalance, ambiguous intermediate damage states, and limited cross-event transferability. This study presents, to our knowledge, the first application of Grassmann-Plucker (GP) token mixing to computer vision and introduces two extensions for image classification: the Quantum-inspired Grassmann-Plucker (QGP) head and the Hybrid Quantum Machine Learning Grassmann-Plucker (HQML-GP) head. The GP head represents multiscale relationships among image patch tokens by encoding subspaces formed by token pairs with Plucker coordinates; QGP enriches these coordinates with amplitude-derived probability features, whereas HQML-GP incorporates expectation values generated by a simulated quantum circuit into the geometric token representation. Paired pre- and post-event image patches from the xBD tornado dataset were processed using a frozen six-channel Vision Transformer base encoder with 16 x 16-pixel patches. The three GP-based heads were compared with multilayer perceptron and Transformer baselines under identical training, checkpoint selection, and evaluation protocols. Joplin and Moore tornado samples were used for model development and seen-event testing, while Tuscaloosa was reserved for unseen-event evaluation. QGP led both test sets in accuracy and macro-F1: 83.46% and 64.50% for the seen events, and 66.45% and 52.70% for the unseen event. Although HQML-GP obtained the highest validation macro-F1 of 65.63%, it did not surpass QGP on either test set and required substantially more training time per epoch. These results establish GP token mixing as a competitive attention-free alternative to conventional Transformer-based token mixing for paired satellite image damage classification.

</details>

### 5. SVI2LoD3: Agent-Driven Reconstruction of LoD3 Facade Openings in Semantic 3D City Models from Volunteered Street View Imagery using Large Language and Visual Models **⭐⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2608.29992](https://arxiv.org/abs/2608.29992)  · [📄 PDF](https://arxiv.org/pdf/2608.29992)
- **作者**: Elmehdi Kanna, Lukas Arzoumanidis, Huynh Duc An Son Nguyen et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/hcu-cml/citydb-SVI2LoD3-ai](https://github.com/hcu-cml/citydb-SVI2LoD3-ai)
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: ①针对3D城市模型中立面开口LoD3重建依赖大量人工标注和语义分割的问题，该论文提出端到端代理驱动管线。②方法上，利用大型语言和视觉模型进行零样本分割，减少标注工作量，并强制正确的部分层级结构以生成CityGML兼容的LoD3模型。③相比监督方法，创新在于零样本策略和新的评估指标Facade Feature Distance (FFD)，该指标基于视觉Transformer的高层特征空间测量距离，同时捕捉语义正确性和建筑布局。④在eTRIMS数据集上的基准测试表明，该方法在减少标注的同时保持强性能，FFD提供了比mIoU或FRDS更合适的立面重建质量评估。
- **摘要（英）**: This paper presents an agent-driven pipeline for LoD3 facade opening reconstruction using zero-shot segmentation with large language and visual models, reducing annotation effort while ensuring CityGML conformity. It introduces a novel Facade Feature Distance metric based on vision transformer features, which better captures semantic and architectural quality than traditional overlap metrics.
- **评估**: 该论文在3D城市建模领域有贡献，但主题与自动驾驶感知关联度较低，主要面向地理信息应用。
- **核心贡献**: 提出零样本LoD3立面重建管线和新评估指标FFD。
- **创新点**: 利用VLM进行零样本分割并强制部分层级结构，确保CityGML兼容。
- **结果**: 在eTRIMS数据集上实现强性能，同时减少标注需求。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents an end-to-end, agent-driven pipeline for the LoD3 reconstruction of facade openings in 3D city models, producing directly usable CityGML-conform outputs. In contrast to existing approaches that rely on supervised semantic segmentation and therefore require large amounts of manually annotated training data, the proposed method employs a zero-shot segmentation strategy. This substantially reduces the annotation effort while still achieving strong performance in our benchmark on the eTRIMS dataset. A further key contribution is the enforcement of correct partonomic hierarchies, thereby producing CityGML-conform LoD3 building models. Beyond the reconstruction pipeline itself, this work also introduces a novel evaluation metric for facade reconstruction, termed Facade Feature Distance (FFD). Unlike conventional metrics such as mIoU or FRDS, which assess similarity primarily through pixel-wise overlap, FFD measures distance in a high-level feature space derived from a vision transformer. In doing so, it captures both semantic correctness and architectural layout, providing a more suitable assessment of facade reconstruction quality. The proposed pipeline and evaluation strategy together offer a practical and scalable contribution toward the automated generation and analysis of semantically enriched 3D city models. The developed code is published at: https://github.com/hcu-cml/citydb-SVI2LoD3-ai.

</details>

---

## Continual Learning

### 1. One Adapter, Many Tasks: Task-Conditioned Feature Transformations for Continual Learning **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.31096](https://arxiv.org/abs/2608.31096)  · [📄 PDF](https://arxiv.org/pdf/2608.31096)
- **作者**: Yunxiang Fu, Meng Lou, Yizhou Yu
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对类增量学习（CIL）中任务特定适配器参数效率低和LoRA合并导致表示干扰的问题。②提出FACET方法，学习单一共享适配器，采用动态任务条件特征变换，将特征分布塑造成重叠减少的任务混合体，并引入条件特征一致性。③改进点在于在推理时动态调整特征，避免静态权重干扰，同时保持参数效率。④实验表明FACET在多个CIL基准上优于现有方法，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses parameter inefficiency and representation interference in class-incremental learning. FACET uses a single shared adapter with dynamic task-conditioned feature transformation, shaping features into a mixture of reduced-overlap tasks. It achieves excellent parameter efficiency and discriminative features, outperforming baselines on CIL benchmarks.
- **评估**: 该论文在持续学习领域有创新，但与自动驾驶感知相关性较低。
- **核心贡献**: 提出了FACET，一种任务条件特征变换方法，提升CIL参数效率和特征判别性。
- **创新点**: 动态任务条件变换避免静态权重干扰。
- **结果**: 在CIL基准上优于现有方法，具体数值未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) requires a model to incrementally learn tasks that contain new classes without accessing earlier training data while preserving the ability to recognize all seen classes. Recently, pretrained-model-based approaches have become prevalent by adapting a frozen backbone with additional lightweight trainable modules. Existing methods, however, exhibit limitations: task-specific adapters learn explicit per-task representations but are parameter- and computation-inefficient, while LoRA-based merging methods combine per-task LoRA parameters into a single model whose static aggregated weights cause representation interference during inference. To address these problems, we present \textbf{FACET}: task-conditioned \textbf{F}e\textbf{A}ture transformation with \textbf{C}ondition\textbf{E}d feature consis\textbf{T}ency, achieving excellent parameter efficiency while producing highly discriminative features during inference. When continually trained on a task sequence, FACET learns a single shared adapter that employs a dynamic task-conditioned feature transformation, shaping the overall feature distribution of the adapter into a mixture of overlap-reduced task-specific components. On the other hand, we propose an efficient replay-free task-conditioned feature consistency loss, aiming to mitigate catastrophic forgetting of the learned mixture distribution in the adapter's feature space. Even when maintaining only a single adapter, FACET demonstrates robust scalability. On both very long task sequences (e.g., 200 tasks) and standard short task sequences (e.g., 20 tasks), our method achieves superior performance while using significantly fewer trainable parameters and GFLOPs. The code will be made open source upon acceptance.

</details>

### 2. Knowing Beyond the Known: Reinforced Knowledge Specification for Multi-Label Class-Incremental Learning **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.30316](https://arxiv.org/abs/2608.30316)  · [📄 PDF](https://arxiv.org/pdf/2608.30316)
- **作者**: Aoting Zhang, Dongbao Yang, Chang Liu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对多标签类增量学习（MLCIL）中已知与未知知识边界模糊的问题，提出了KBK框架，通过显式建模已知和未知知识来统一历史、当前和未来学习。具体包括层次特征净化模块和不确定性感知回忆增强策略，前者从全局特征中分离细粒度类特定特征，后者抑制不可靠预测。利用语义相关性合成未知特征，以保留嵌入空间结构。
- **摘要（英）**: To address ambiguous known-unknown boundaries in multi-label class-incremental learning, this paper proposes KBK, which explicitly models known and unknown knowledge via hierarchical feature purification and uncertainty-aware recall enhancement. It synthesizes unknown features using semantic correlations to preserve embedding structure.
- **评估**: 该工作对多标签增量学习中的知识边界问题提供了系统解决方案，但实验细节和效果数据未在摘要中充分展示。
- **核心贡献**: 提出了一个强化知识规范框架，统一处理多标签增量学习中的历史、当前和未来知识。
- **创新点**: 利用不确定性感知和语义相关性合成未知特征。
- **结果**: 摘要未提供具体数值，但声称改善历史保留和当前学习。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing class-incremental learning methods struggle in multi-label scenarios (MLCIL) due to the inherent contradiction of learning objectives arising from co-occurring and incomplete labels. We argue that the core obstacle is the model's ambiguous boundary between known and unknown knowledge, which undermines historical knowledge retention, complicates current task learning, and limits adaptability to future concepts. To address this, we propose KBK (Knowing Beyond the Known), a reinforced knowledge specification framework that explicitly models what is known or not to unify historical, current, and prospective learning. Specifically, to clarify known knowledge, we develop a hierarchical feature purification module that disentangles fine-grained class-specific features from global features, where high-level semantic abstraction is reinforced with low-level visual features. Additionally, an uncertainty-aware recall enhancement strategy suppresses unreliable predictions based on distribution priors, improving the quality of historical recall. For probing the unknown, KBK leverages semantic correlations to synthesize informative unknown features under co-occurring, preserving embedding space for future learning. Furthermore, to mitigate heterogeneous forgetting, we design a category-balanced gradient compensation loss that dynamically reweights gradient backpropagation according to forgetting speeds. Experiments on multiple benchmarks validate the effectiveness and robustness of KBK, which surpasses prior best methods by 2.7% in Avg. Acc on MS-COCO B0-C10 setting even without any replay buffers.

</details>

### 3. SELECT: SELEctive Context Transfer for Class-Incremental Semantic Segmentation **⭐⭐⭐** (相关度: 30%, 质量: 0.75)

- **arXiv ID**: [2608.30281](https://arxiv.org/abs/2608.30281)  · [📄 PDF](https://arxiv.org/pdf/2608.30281)
- **作者**: Avi Gupta, Saurabh Yadav, Koteswar Rao Jerripothula et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/avigupta2798/SELECT](https://github.com/avigupta2798/SELECT)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 这篇论文针对类增量语义分割（CISS）中的灾难性遗忘和背景偏移问题。现有方法依赖无差别知识迁移或模糊初始化，导致语义信息稀释。作者提出SELECT方法，通过上下文迁移注意力机制将新类锚定到少量语义相似的旧类，并加入噪声扰动和基于边界的迁移损失以保持类间分离。在Pascal VOC和ADE20K上实验，SELECT持续优于先前方法，但摘要未给出具体数值。该方法与自动驾驶中的增量场景理解相关，但主要面向通用语义分割。
- **摘要（英）**: This paper addresses catastrophic forgetting and background shift in class-incremental semantic segmentation. Existing methods use indiscriminate knowledge transfer. The authors propose SELECT with a context transfer attention mechanism that grounds new classes in similar past classes, plus noise perturbation and margin-based loss. It outperforms prior work on Pascal VOC and ADE20K, though no exact numbers are given.
- **评估**: 该论文对自动驾驶中的持续学习场景有一定参考价值，但方法针对通用分割，相关性中等。
- **核心贡献**: 提出SELECT方法，通过选择性上下文迁移实现类增量语义分割。
- **创新点**: 利用上下文迁移注意力机制将新类锚定到语义相似的旧类，并引入边界损失。
- **结果**: 在Pascal VOC和ADE20K上优于先前方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-Incremental Semantic Segmentation (CISS) is fundamentally challenged by catastrophic forgetting and background shift, where learning new concepts degrades performance on previously seen classes. While existing methods attempt to balance stability (retaining old knowledge) and plasticity (learning new knowledge), they often fail to leverage prior knowledge effectively. These approaches typically rely on indiscriminate knowledge transfer or ambiguous initializations, which can dilute crucial semantic information. To overcome this limitation, we propose SELECT, a novel approach for Selective Context Transfer, which instead grounds each new class in a small set of semantically similar past classes. Its core is a Context Transfer Attention mechanism that aggregates the learned tokens from similar classes into a structured initialization for the new class. To ensure this transfer does not corrupt the borrowed representations, we add a controlled noise perturbation and a margin-based context-transfer loss that enforces separation between the new class token and its source tokens. Extensive experiments on Pascal VOC and ADE20K show that SELECT consistently outperforms prior work, achieving mIoU of 2.2% on VOC and 2.8% on ADE, providing an effective handle on the stability-plasticity dilemma. Code is available at https://github.com/avigupta2798/SELECT.

</details>

### 4. Continual Test-Time Adaptation via Entropy Sensitivity-Guidance in Strict Online Setting **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.29920](https://arxiv.org/abs/2608.29920)  · [📄 PDF](https://arxiv.org/pdf/2608.29920)
- **作者**: Chandler Timm C. Doloriel, Yunbei Zhang, Muhammad Salman Siddiqui et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对严格在线测试时适应（TTA）中，批量大小为1且无源数据时模型容易漂移或崩溃的问题。②提出了SEGA，一种基于熵敏感性引导的擦除适应方法，通过结构化擦除探测预测熵变化，利用敏感性轨迹协调恢复和样本选择。③相比依赖原始熵或批量统计的方法，SEGA提供了实用的反馈信号，无需周期性重置或模型储备。④在ImageNet-C、CIFAR10/100-C和水产养殖流上，SEGA相比强CTTA基线在鲁棒性和稳定性上取得一致提升，同时减少反向传播次数。
- **摘要（英）**: This paper addresses drift and collapse in strict online test-time adaptation with batch size one. It proposes SEGA, which uses structured erasures to probe entropy changes and coordinates recovery via sensitivity trajectories. SEGA achieves consistent robustness gains over strong CTTA baselines on corruption streams while reducing backward passes.
- **评估**: 该方法对自动驾驶中的分布漂移适应具有重要参考价值，尤其在在线学习场景下，创新性强且实验充分。
- **核心贡献**: 提出了SEGA，一种基于熵敏感性引导的严格在线TTA方法，无需重置或储备。
- **创新点**: 利用结构化擦除的敏感性轨迹作为反馈信号，替代原始熵或批量统计。
- **结果**: 在多个基准上提升鲁棒性和稳定性，同时降低计算开销。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation (TTA) promises robustness under distribution shift by updating a pretrained model on unlabeled test data, but strict online TTA with batch size one and no access to source data is especially prone to drift or collapse. We introduce Sensitivity-Guided Erasing Adaptation (SEGA), a method for strict online continual TTA (CTTA) on corruption-style streams. SEGA uses a small number of structured erasures to probe how predictive entropy changes as information is removed, and uses the resulting per-sample sensitivity trajectories to coordinate recovery and sample selection rather than relying on raw entropy or batch statistics. This yields a practical feedback signal for long-horizon batch-size-one adaptation without periodic resets or model reservoirs. In experiments on ImageNet-C, CIFAR10/100-C, and corruption-generated aquaculture streams treated as controlled corruption-style proxies, SEGA yields consistent robustness and stability gains over strong CTTA baselines while reducing backward passes through sensitivity-based gating.

</details>

---

## Open-set Detection

### 1. OPUS: A Simple yet Effective Unified Framework for Open-Vocabulary Detection **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.30247](https://arxiv.org/abs/2608.30247)  · [📄 PDF](https://arxiv.org/pdf/2608.30247)
- **作者**: Xiaoyan Wei, Zhimin Yao, Ruilin Yang et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对统一开放词汇检测（OVD）中复杂设计（如重跨模态融合、分阶段训练）在强基础模型时代是否必要的问题。②提出OPUS框架，采用DINOv3-ConvNeXt-B视觉编码器、提示感知解码器和单阶段文本-视觉训练策略，支持文本、交互式视觉、通用视觉和混合提示。③改进点在于简化架构，利用语义丰富的视觉表示和可扩展的接地监督，避免提示特定分支。④实验表明OPUS在多个OVD基准上达到SOTA性能，具体数据未在摘要中给出。
- **摘要（英）**: This paper questions the necessity of complex designs in unified open-vocabulary detection with stronger foundation models. OPUS simplifies the framework using a semantic-rich visual encoder and prompt-aware decoder, trained with one-stage text-visual strategy. It supports multiple prompt types and achieves state-of-the-art results on OVD benchmarks.
- **评估**: 该论文简化了统一OVD框架，与开放集检测和自动驾驶感知高度相关，具有实用价值。
- **核心贡献**: 提出了OPUS，一个简单统一的开放词汇检测框架，支持多种提示类型。
- **创新点**: 利用强基础模型简化架构，无需复杂跨模态融合。
- **结果**: 在OVD基准上达到SOTA，具体数值未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent unified open-vocabulary detection (OVD) supports heterogeneous prompts, including text queries, visual exemplars, and their combinations, but often rely on increasingly complex designs such as heavy cross-modal fusion, staged training, and iterative annotation pipelines. We revisit whether such complexity is necessary in the era of stronger foundation models. Our finding is that unified OVD can be made substantially simpler with semantic-rich visual representations and scalable grounding supervision. We present OPUS (\textbf{O}pen-vocabulary, \textbf{P}rompt-\textbf{U}nified, \textbf{S}imple), a unified detector supporting text, interactive visual, generic visual, and mixed prompting within one framework. OPUS adopts a simple three-part design. Its model architecture combines a semantic-rich visual encoder, built on a DINOv3-ConvNeXt-B backbone with efficient hybrid encoding, with a prompt-aware decoder that avoids prompt-specific branches for unified prompt reasoning. OPUS is trained with a one-stage text-visual training strategy with Instance-level Contrastive Alignment (ICA), and is supported by a SAM3-based single-pass data engine for heterogeneous grounding supervision. Experiments on COCO, LVIS-minival, and ODinW35 show that OPUS achieves state-of-the-art Visual-I performance, reaching 68.1/69.2/54.7 AP, while maintaining balanced Text and Visual-G accuracy. OPUS also turns mixed prompting from interference into complementarity, improving over text or visual prompt alone. These results show that simplicity and strong unified prompting capability can be achieved together.

</details>

### 2. VeriCam: A Verification Baseline for the Classification of Unknown Data **⭐⭐⭐** (相关度: 70%, 质量: 0.6)

- **arXiv ID**: [2608.31107](https://arxiv.org/abs/2608.31107)  · [📄 PDF](https://arxiv.org/pdf/2608.31107)
- **作者**: Lucas Wojcik, Gabriel E. Lima, Sergio M. Silva et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/lmlwojcik/VeriCam](https://github.com/lmlwojcik/VeriCam)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对基础模型在细粒度未知类分类中表征能力不足的问题，提出VeriCam流水线，利用验证任务训练的图像模型构建关系图，并通过Leiden图聚类算法对未知数据进行分类。相比直接使用零样本分类，该方法通过成对判别学习细粒度特征，增强了未知类的区分能力。在LPLCv2交通数据集上验证了有效性，但摘要未提供具体性能数据。
- **摘要（英）**: To address the limited fine-grained representation of foundation models for unknown class classification, VeriCam leverages verification-trained image models to construct a relational graph and applies Leiden clustering for unknown data classification. It improves over zero-shot methods by learning discriminative minutiae features via pairwise discrimination. Validation on the LPLCv2 traffic dataset demonstrates its potential, though specific metrics are not detailed.
- **评估**: 该工作为开放集分类提供了新思路，但实验充分性一般，且与自动驾驶核心任务关联度中等。
- **核心贡献**: 提出了一种基于验证任务和关系图聚类的未知类分类流水线。
- **创新点**: 利用验证模型构建关系图并采用Leiden聚类实现未知类分类。
- **结果**: 在LPLCv2数据集上验证了有效性，但未报告具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of foundation models have enabled a new era in zero-shot classification. Yet, key challenges persist. Despite their impressive generalization power that leverages the immense pre-training knowledge, both foundation models for image and text as well as vision-text hybrids lack the representational power needed for fine-grained, minutiae-based class separation that some real-world tasks require. To address the current gaps in the literature, we propose VeriCam, a pipeline designed to learn highly specialized features that enable classification of unknown classes in unseen data. VeriCam works by leveraging the representation power of image models trained for the verification task, where the model develops an intricate feature space that incorporates fine-grained details. By training a model to discriminate between pairs of images from the same and different classes, a relational graph is constructed, representing the class relationships between data points. We then present two approaches for graph clustering: a naive algorithm and a specific setup for the Leiden graph clustering algorithm. The pipeline is validated on the LPLCv2 dataset, which comprises real-world traffic surveillance images. We show that the dataset carries an inherent capture device bias that is posed as a generalization challenge for downstream License Plate recognition tasks such as OCR. As such, we dynamically identify capture devices with a label-agnostic approach, enabling the construction of a fair and unbiased benchmark. In the cross-device scenario, our pipeline reaches an F1-Score of 93.45 in the verification baseline and a V-Measure score of 80.13 in the clustering step. All code is publicly available at https://github.com/lmlwojcik/VeriCam

</details>

### 3. UFPR-PEs: A Brazilian Face Recognition Benchmark with Self-Declared Race/Color Labels **⭐⭐** (相关度: 30%, 质量: 0.5)

- **arXiv ID**: [2608.30688](https://arxiv.org/abs/2608.30688)  · [📄 PDF](https://arxiv.org/pdf/2608.30688)
- **作者**: Alexandre Diano, Bernardo Biesseck, Gabriel Polo et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对人脸识别系统在不同种族/肤色群体上的偏差评估问题，构建了UFPR-PEs基准，使用巴西政客公开视频和自报种族/肤色标签，包含巴西特有的parda类别。该基准保留了困难样本以分析现实条件下的性能，并评估了验证和开闭集识别任务中的子群差异。结果显示识别性能随图像质量变化显著，子群差距需结合视觉难度解释。
- **摘要（英）**: To evaluate demographic bias in face recognition, UFPR-PEs provides a benchmark using Brazilian politicians' videos with self-declared race/color labels, including the parda category. It preserves difficult samples for realistic analysis and evaluates verification and identification tasks, showing performance varies with image quality and subgroup gaps depend on visual difficulty.
- **评估**: 该工作对公平性研究有贡献，但与自动驾驶感知领域相关性较低。
- **核心贡献**: 构建了包含巴西种族分类的人脸识别偏差评估基准。
- **创新点**: 引入巴西人口普查种族分类和困难样本保留策略。
- **结果**: 揭示了识别性能与图像质量和子群差异的关联。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While face recognition systems are widely deployed, ensuring their demographic reliability and robustness under uncontrolled visual conditions remains a critical challenge. To bridge this gap, we present UFPR-PEs, a benchmark for face recognition bias evaluation using public videos of elected Brazilian politicians annotated with official self-declared race/color categories. The dataset adopts the Brazilian census taxonomy, including the parda category, which has no direct equivalent in the U.S.- or Europe-centric schemas commonly used in prior benchmarks. Our benchmark is built from compressed public video and preserves difficult samples so that performance can be analyzed under realistic conditions. We describe the construction pipeline, report dataset statistics, and evaluate face recognition performance across verification and (closed- and open-set) identification settings, including subgroup analysis by race/color and difficulty level. The results show that recognition performance varies substantially with image quality, and that subgroup gaps must be interpreted jointly with visual difficulty rather than in isolation. Overall, UFPR-PEs provides a reproducible and demographically grounded setting for studying face recognition bias under challenging public video conditions.

</details>

---

## 3D Detection

### 1. SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding **⭐⭐⭐** (相关度: 60%, 质量: 0.65)

- **arXiv ID**: [2608.30451](https://arxiv.org/abs/2608.30451)  · [📄 PDF](https://arxiv.org/pdf/2608.30451)
- **作者**: Yi Zhang, Yi Wang, Yueting Wu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①针对图像-based 3D视觉定位中文本与观测对齐松散、忽略时间顺序的问题。②提出了SeqAlign3DVG基准，包含9,622个单视图和14,493个序列样本，所有表达均经人工验证并严格对齐RGB观测；并提出了基于体素的ROVM和PLVF模块。③ROVM通过保守记忆动态排序和聚合多视图证据，PLVF进行由粗到细的空间-语言推理。④在无深度协议下达到最先进性能，显著提升复杂关系目标的定位精度。
- **摘要（英）**: This paper tackles loose text-observation alignment and neglected temporal ordering in image-based 3D visual grounding. It introduces SeqAlign3DVG benchmark with human-verified expressions and a voxel-based pipeline using ROVM and PLVF for robust multi-view aggregation and coarse-to-fine reasoning. The method achieves state-of-the-art performance under depth-free protocol.
- **评估**: 该论文为3D视觉定位提供了严格对齐的基准和有效推理框架，对自动驾驶多相机感知有参考价值，但偏重语言交互场景。
- **核心贡献**: 提出时序对齐的3D视觉定位基准SeqAlign3DVG及体素推理框架。
- **创新点**: 引入ROVM和PLVF实现动态证据排序与渐进式语言-体素融合。
- **结果**: 在无深度协议下取得最先进性能，显著改善复杂目标定位。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-based 3D visual grounding is critical for embodied agents, yet existing benchmarks suffer from loose text-observation alignment and neglect temporal ordering. We introduce SeqAlign3DVG, a novel benchmark dedicated to temporally ordered and strictly observation-aligned image-based 3D visual grounding. Unlike prior works using order-agnostic views or global point clouds, SeqAlign3DVG ensures all expressions are human-verified and strictly grounded in the provided RGB observations (single frames or ordered observation sequences). It comprises 9,622 single-view and 14,493 sequence samples featuring rich descriptions, complex relations, and multi-instance ambiguities. To tackle this benchmark, we propose a unified voxel-based pipeline featuring Relevance-Ordered Voxel Memory (ROVM) and Progressive Language-Voxel Fusion (PLVF). ROVM dynamically ranks and aggregates multi-view evidence via a conservative memory to mitigate noisy observations, while PLVF performs coarse-to-fine spatial-linguistic reasoning for precise disambiguation. Our approach achieves state-of-the-art performance under the depth-free protocol, significantly improving localization for targets defined by complex relations and appearance cues.

</details>

### 2. Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.30821](https://arxiv.org/abs/2608.30821)  · [📄 PDF](https://arxiv.org/pdf/2608.30821)
- **作者**: Minghan Qin, Yuang Wang, Xiuyu Yang et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 该论文针对可组合场景建模中解析、生成和放置步骤对输入要求过高的问题，提出Lucida框架，重新分配各步骤需求。方法上，解析视频为场景图，为每个实例生成完整资产，并用GizmoAct（VLM策略）通过多轮GUI交互放置资产。相比现有流水线，Lucida只依赖真实捕获可靠提供的信息，精度在流水线末端达成。在场景级3D目标检测等任务上展示了效果，但摘要未给出具体数据。
- **摘要（英）**: This paper addresses composable scene modeling challenges by proposing Lucida, which redistributes requirements across parse, generate, and place steps. It parses video into a scene graph, generates assets, and uses a VLM policy for placement. The approach handles cluttered captures better than existing pipelines, though quantitative results are not detailed.
- **评估**: 该论文对机器人仿真和具身AI有参考价值，但自动驾驶相关性一般，方法有创新性。
- **核心贡献**: 提出Lucida框架，实现从真实视频到可编辑3D场景的可组合建模。
- **创新点**: 用VLM策略将放置任务转化为多轮GUI交互，降低对输入精度的要求。
- **结果**: 在场景级3D目标检测等任务上展示了有效性，但具体数据未给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Composable scene modeling aims to recover a real indoor scene as complete, editable object assets arranged as observed, giving robot simulation and embodied AI a simulation-ready replica of the real environment whose objects can be manipulated individually. Existing pipelines decompose the task into three steps---parse the observations into instances, generate an asset for each, and place each asset back---but every step presumes an input that a cluttered capture rarely provides: accurate instance geometry, unoccluded views, and assets that accurately match the observations. We propose Lucida, which keeps this order but redistributes the requirements, so each step consumes only what a real capture reliably provides and precision is reached at the end of the pipeline rather than demanded at its start. Lucida parses the video into a scene graph whose nodes carry per-instance multi-view evidence, generates a complete asset for each instance from its evidence, and places assets with GizmoAct, a VLM policy that casts placement as multi-turn GUI interaction, manipulating the object's gizmo in a closed loop and deciding itself when alignment is reached. Across scene-level 3D object detection, object pose estimation, and scene reconstruction, Lucida improves mAP over Boxer by 69% on R2S-Scene, raises ADD-SB@0.05 from 57.8% to 83.4% on CA-1M, and increases scene F-Score from 0.794 for SAM3D to 0.924.

</details>

### 3. OrnaStyler: Ornament-Aware Latent Editing for Content-Preserving 3D Stylization **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.29905](https://arxiv.org/abs/2608.29905)  · [📄 PDF](https://arxiv.org/pdf/2608.29905)
- **作者**: Tomohiro Aizawa, Shigeru Kuriyama, Chunzhi Gu
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/tomohiro0427/OrnaStyler](https://github.com/tomohiro0427/OrnaStyler)
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 该论文针对文本引导的3D资产风格编辑中保留精细结构装饰的挑战，提出OrnaStyler框架，基于整流流生成模型，引入反演引导的编辑策略，在几何和外观层面恢复内容感知的潜在表示。核心思想是显式建模风格元素的空间配置，缓解内容保留与风格表达之间的张力。在几何层面，通过流反演操作体素表示，合成装饰增强结构。摘要未提供定量结果，但框架旨在实现零样本风格化。
- **摘要（英）**: This paper addresses text-guided 3D stylization with fine-grained ornamentation by proposing OrnaStyler, a zero-shot framework based on rectified flow. It uses inversion-guided editing to recover content-aware latents and models spatial configuration of style elements. The approach preserves source geometry while integrating new details, though no quantitative results are reported.
- **评估**: 该论文与自动驾驶感知领域相关性低，但3D编辑方法对视觉生成有参考价值。
- **核心贡献**: 提出OrnaStyler框架，实现保留内容的文本引导3D风格化。
- **创新点**: 通过流反演和显式空间配置建模，平衡内容保留与风格表达。
- **结果**: 摘要未提供具体效果数据，但框架展示了零样本风格化的潜力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-guided style editing of 3D assets is essential for adapting existing objects to diverse visual aesthetics in digital content creation. Despite rapid progress in 3D shape modeling, faithfully stylizing an existing asset remains challenging when the desired stylization involves fine-grained structural ornamentation, which requires the model to preserve the source geometry and object identity, while coherently integrating new style-specific details. We propose \textbf{OrnaStyler}, a zero-shot framework for text-guided ornament-aware 3D stylization. Built upon rectified flow-based generative modeling, OrnaStyler introduces an inversion-guided editing strategy that recovers content-aware latent representations at both geometry and appearance levels in a staged manner to facilitate faithful editing. Our core idea is to explicitly model the spatial configuration of stylistic elements, thereby mitigating the fundamental tension between content preservation and style expression in the voxel space. Specifically, at the geometry level, we manipulate voxel representations through flow inversion to synthesize ornament-enhanced structures while preserving the spatial identity of the source asset. Then, at the appearance level, we introduce an adjacency-aware feature inpainting mechanism to harmonize newly generated ornaments with the original content, yielding coherent geometry-appearance integration. Our approach operates solely in the inference phase and enables selective editing over geometric augmentation or appearance stylization. Extensive experiments on both generated and real-world 3D assets against prior methods demonstrate that OrnaStyler achieves state-of-the-art editing performance in terms of content preservation, style fidelity, and overall visual realism. Code is available at: https://github.com/tomohiro0427/OrnaStyler

</details>

---

## Autonomous Driving

### 1. Driving on Memory **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.31029](https://arxiv.org/abs/2608.31029)  · [📄 PDF](https://arxiv.org/pdf/2608.31029)
- **作者**: Christian Löwens, Thorben Funke, Alexandru Paul Condurache
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/boschresearch/MemoryDrivoR](https://github.com/boschresearch/MemoryDrivoR)
- **提交日期**: 2026-08-31 · **分类**: cs.CV, cs.LG, cs.RO
- **摘要（中）**: 该论文针对端到端自动驾驶规划模型在NAVSIM等基准上得分高但可能未真正理解动态场景的问题，提出用记忆替换相机输入来探测模型对动态信息的依赖。方法上，移除相机输入，用同一位置的先前驾驶记忆替代，提供静态场景信息但不含当前交通状态。结果显示，在NAVSIM上，仅靠记忆就能达到甚至超过领先端到端方法的性能，表明高得分不要求模型对当前交通做出反应。该发现对基准评估的有效性提出警示，且效应依赖具体基准。
- **摘要（英）**: This paper probes how much end-to-end driving benchmark scores depend on reacting to dynamic scenes by replacing camera input with memory from prior drives. On NAVSIM, memory alone nearly matches or exceeds leading methods, indicating high scores do not require reacting to current traffic. The effect is benchmark-dependent, cautioning against over-reliance on such metrics.
- **评估**: 该论文对自动驾驶规划基准的有效性提出重要质疑，对评估方法有深远影响，值得高度关注。
- **核心贡献**: 揭示NAVSIM基准中记忆信息足以达到高得分，质疑其评估动态感知能力。
- **创新点**: 通过记忆替换输入来隔离动态信息贡献，提供基准评估的探针方法。
- **结果**: 在NAVSIM上，记忆驱动达到或超过领先方法性能，但效果依赖基准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving models plan future trajectories from raw sensor input. While earlier driving benchmarks often measured deviation from the human trajectory, current benchmarks such as NAVSIM and Bench2Drive evaluate models with richer simulation-based metrics intended to capture safe and compliant driving. A high benchmark score should reflect that a model can understand the scene in front of it and act accordingly. But how much of that score specifically comes from reacting to the dynamic part of that scene? To probe this, we remove a model's camera input and replace it with memories from prior drives at the same location. The retrieved memories can provide persistent scene information, including road layout and location-conditioned regularities, but not the current traffic state. Surprisingly, memory is nearly sufficient on NAVSIM, reaching or even exceeding the performance of leading end-to-end methods without actually observing the evaluated scene. Our results suggest that a high NAVSIM score does not require a planner to react to the current traffic scene and should be treated with caution. This effect is benchmark-dependent: driving from memory causes substantially larger performance drops on Bench2Drive and RealEngine. We provide our code at https://github.com/boschresearch/MemoryDrivoR .

</details>

### 2. Physical Adversarial Examples for Person Detectors in Thermal Images Based on 3D Modeling **⭐⭐⭐** (相关度: 70%, 质量: 0.7)

- **arXiv ID**: [2608.30839](https://arxiv.org/abs/2608.30839)  · [📄 PDF](https://arxiv.org/pdf/2608.30839)
- **作者**: Xiaopei Zhu, Siyuan Huang, Zhanhao Hu et al. (6 authors)
- **🏷️ 机构**: Tsinghua
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 该论文针对热红外人体检测器在真实场景中的安全性问题，提出基于3D建模的对抗服装设计。方法上，利用3D建模模拟多角度场景，优化服装上的黑色补丁布局，并用气凝胶制作物理对抗服装。相比2D建模，3D建模更贴近真实世界。物理攻击中，对YOLOv9的室内攻击成功率达80.11%，室外76.85%，而随机补丁仅26.53%和23.03%。该工作展示了热红外检测的脆弱性。
- **摘要（英）**: This paper addresses security vulnerabilities in thermal person detectors by proposing 3D-modeled adversarial clothing. It optimizes patch layouts and fabricates physical clothing with aerogel, achieving attack success rates of 80.11% indoors and 76.85% outdoors against YOLOv9. The 3D modeling enhances realism compared to 2D approaches.
- **评估**: 该论文对自动驾驶中热红外感知的安全性有实际意义，攻击成功率数据充分，但领域相关性中等。
- **核心贡献**: 提出基于3D建模的物理对抗服装，有效攻击热红外人体检测器。
- **创新点**: 利用3D建模和真实红外照片构建纹理图，优化补丁布局以增强攻击效果。
- **结果**: 室内外攻击成功率分别达80.11%和76.85%，显著高于随机补丁。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Thermal Infrared detection is widely used in autonomous driving, medical AI, etc., but its security has only attracted attention recently. We propose infrared adversarial clothing designed to evade thermal person detectors in real-world scenarios. The design of the adversarial clothing is based on 3D modeling, which makes it easier to simulate multiangle scenes near the real world compared to 2D modeling. We optimized the black patch layout pattern of 3D clothing based on the adversarial example technique and made physical adversarial clothing using the aerogel. The idea is to paste a set of square aerogel patches, which display black squares in thermal images, in the inner side of clothing at specific locations with specific orientations. To enhance realism, we propose a method to build infrared 3D models with real infrared photos and develop texture maps for 3D models to simulate varied infrared characteristics over time and location. In physical attacks, we achieved an attack success rate of 80.11\% indoors and 76.85\% outdoors against YOLOv9. In contrast, randomly placed patches yielded much lower success rates (26.53\% indoors and 23.03\% outdoors). The adversarial clothing also showed good transferability to unknown detectors with an ensemble attack method, demonstrating the effectiveness of our approach.

</details>

### 3. MotionSync: Non-Causal Refinement of Causal Tracker for Label-Efficient 3D Perception **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.29567](https://arxiv.org/abs/2608.29567)  · [📄 PDF](https://arxiv.org/pdf/2608.29567)
- **作者**: Rahul Ahuja, Bala Murali Manoghar Sai Sudhakar, Shashwata Gupta et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 该论文针对自动驾驶数据引擎中3D框和轨迹标注成本高、且在线和离线系统分离的问题，提出MotionSync框架，将因果/非因果边界作为架构接缝。方法上，因果跟踪器扩展了强基线，加入不确定性校准、帧率不变关联门和多假设运动；非因果通道用RTS平滑、物理验证补全和语义剪枝修正轨迹，但不回写。作为自动标注器，用25%人工标签加MotionSync伪标签训练的3D检测器达到全监督mAP的96.9%，在10%预算下非因果通道贡献显著。
- **摘要（英）**: This paper addresses high annotation costs in autonomous driving by proposing MotionSync, which integrates causal and non-causal tracking in one system. A causal tracker emits online results, refined by a non-causal pass with RTS smoothing and semantic pruning. As an auto-labeller, it achieves 96.9% of full-supervision mAP with 25% human labels on Waymo.
- **评估**: 该论文对自动驾驶数据引擎和3D感知有重要价值，方法创新且实验充分，值得关注。
- **核心贡献**: 提出统一因果/非因果的跟踪框架，作为高效自动标注器降低标注成本。
- **创新点**: 将因果/非因果边界作为架构接缝，非因果修正不回写，保持在线一致性。
- **结果**: 25%人工标签下达到全监督mAP的96.9%，10%预算下非因果通道贡献显著。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Three-dimensional box-and-track annotation is the cost bottleneck in autonomous-driving data engines, and the offline systems built to relieve it replace the online perception stack outright, so a team needing both regimes maintains and reconciles two. MotionSync makes the causal/non-causal boundary an explicit architectural seam instead. A strictly causal tracker, built on a strong published baseline and extended with innovation-driven uncertainty calibration, frame-rate-invariant kinematic association gates, and multi-hypothesis motion with learned mode selection, emits a valid online result. A non-causal pass then revises the buffered trajectories with Rauch--Tung--Striebel smoothing applied separately to pose, extent and yaw, physics-validated gap completion, and semantic pruning of ghost tracks against LiDAR point labels. The refiner never writes back, so one system serves both regimes and refinement's effect is a delta over an unaltered causal estimate. Used as an auto-labeller, a fixed 3D detector trained on 25% human labels plus MotionSync pseudo-labels reaches 96.9% of its full-supervision mean average precision (mAP) on Waymo, and at a 10% budget the non-causal pass accounts for +3.3 mAP/L2 over pseudo-labels from the same tracker's causal stage. Re-fitting the online tracker on its own refined output recovers 73% of the benefit of human supervision, while its causal output is worse supervision than no re-fitting at all. As a tracker MotionSync is at parity with the leading published offline entries on the headline metric and ahead of them on error composition, which is where a refinement pass can act at all: it reduces misses and fragmentations together, the signature of gap completion rather than of a tuned detector.

</details>

---

## Neural Architecture Search

### 1. NepScript Genesis: Neural Architecture Search for Handwritten Devanagari Digit Synthesis **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.29540](https://arxiv.org/abs/2608.29540)  · [📄 PDF](https://arxiv.org/pdf/2608.29540)
- **作者**: Mausam Gurung, Prabin Neupane, Sajjan Acharya
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-30 · **分类**: cs.CV
- **摘要（中）**: 针对手写梵文数字生成中GAN架构设计依赖人工的问题，提出了NepScript Genesis，一个基于NAS的GAN自动发现框架，应用于条件式梵文数字合成。比较了五种NAS策略，并引入领域感知评估指标Enhanced Score，其中自适应探索策略在不到1 GPU小时内达到FID 79.12，相比DCGAN基线提升76.19%。在低资源场景下，用生成数据增强训练可将CNN分类准确率从91.0%提升至96.5%。
- **摘要（英）**: To automate GAN architecture design for Devanagari digit synthesis, this paper proposes NepScript Genesis, a NAS framework with a domain-aware metric. Adaptive exploration achieves FID 79.12, a 76.19% improvement over baseline, and boosts CNN accuracy from 91.0% to 96.5% in low-resource settings.
- **评估**: 该工作针对特定手写字符生成任务，NAS策略比较有一定价值，但领域相关性较低，方法通用性有限。
- **核心贡献**: 提出了一个针对手写数字合成的NAS-GAN框架和领域感知评估指标。
- **创新点**: 将脚本特定结构启发式融入NAS搜索以防止模式崩溃。
- **结果**: FID大幅降低，下游分类准确率提升5.5个百分点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces NepScript Genesis, a Neural Architecture Search (NAS) framework for automated Generative Adversarial Network (GAN) discovery, applied to conditional Devanagari handwritten digit synthesis. We compare five NAS strategies against a carefully constructed Deep Convolutional GAN (DCGAN) baseline (FID=332.28). Architecture selection utilizes a two-stage pipeline guided by a novel domain-aware evaluation metric (Enhanced Score). Results demonstrate that Adaptive Exploration achieves the optimal quality-efficiency trade-off, attaining an FID of 79.12 -- a 76.19% improvement over the baseline -- and the highest mode coverage among the NAS strategies (Recall=0.531) in under one GPU-hour. Furthermore, we demonstrate that incorporating script-specific structural heuristics into the search phase prevents early-stage mode collapse. In a downstream low-resource evaluation, augmenting 250 real training samples per class with GAN-generated digits from the best NAS model improves CNN classification accuracy from 91.0% to 96.5% (+5.5 percentage points), demonstrating that NAS-optimized synthesis produces digits of sufficient quality to benefit practical recognition pipelines when real data is scarce.

</details>

---

## Knowledge Distillation

### 1. Identity-Conditioned Latent Consistency Distillation for Face Synthesis **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.31053](https://arxiv.org/abs/2608.31053)  · [📄 PDF](https://arxiv.org/pdf/2608.31053)
- **作者**: Tiago Kienen Chaves, Bernardo Biesseck, David Menotti
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/UFPR-IPASP-PR/FaceRec-IdentityConsistency](https://github.com/UFPR-IPASP-PR/FaceRec-IdentityConsistency)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对扩散模型迭代采样导致大规模人脸合成计算成本高的问题，提出身份条件潜在一致性蒸馏方法。从基础扩散模型Arc2Face中蒸馏知识，将原始文本到图像流程适配为嵌入到人脸设置，用ArcFace身份嵌入替换文本提示。蒸馏模型平均推理时间0.4819秒/图，相比Arc2Face的2.102秒，加速4.36倍。基于FID的定量结果显示，蒸馏模型在所有评估协议上与Arc2Face保持竞争力。
- **摘要（英）**: This paper addresses the high computational cost of diffusion models for large-scale face synthesis by proposing identity-conditioned latent consistency distillation. It distills knowledge from Arc2Face, adapting text-to-image to embedding-to-face with ArcFace embeddings. The distilled model achieves 4.36x speed-up (0.4819s vs 2.102s per image) while maintaining competitive FID scores.
- **评估**: 该工作有效降低了身份条件人脸合成的计算成本，但应用范围较窄，创新性有限。
- **核心贡献**: 提出了身份条件潜在一致性蒸馏方法，实现快速且高质量的人脸合成。
- **创新点**: 将文本到图像蒸馏适配为嵌入到人脸，利用一致性模型减少迭代次数。
- **结果**: 推理速度提升4.36倍，图像质量与教师模型相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models have achieved strong results in high-fidelity image synthesis, but their iterative sampling process makes large-scale generation computationally expensive. This limitation is especially relevant when generating synthetic face datasets for face recognition, where a large number of subjects with many samples in different poses, expressions, ages, etc., are required. In this work, we show that identity-conditioned face synthesis can be performed at a substantially lower computational cost by a latent Consistency Model with few iterations, without compromising image quality. For training, we distill knowledge from the foundation Diffusion Model Arc2Face (teacher) by adapting its original text-to-image pipeline to an embedding-to-face setting, replacing textual prompts with ArcFace identity embeddings. Our distilled model (student) generates identity-conditioned face images with an average inference time of 0.4819 seconds per image, compared with 2.102 seconds for Arc2Face, resulting in a 4.36$\times$ speed-up. Quantitative results, based on FID scores, show that the distilled model remains competitive with Arc2Face across all evaluation protocols. On 100k generated images, it achieves near-parity on CelebA (13.921 vs. 12.928) and outperforms the teacher on WebFace42M (9.317 vs. 9.802). Further evaluations on Synth-500 and AgeDB show a moderate performance gap for the former but comparable results for the latter. These results indicate that Arc2Face can be accelerated through task-specific latent consistency distillation while preserving high image quality for large-scale synthetic face generation. Our proposal is publicly available at https://github.com/UFPR-IPASP-PR/FaceRec-IdentityConsistency.

</details>

---

## Occupancy

### 1. InfraOcc: An Infrastructure Occupancy Benchmark with Static-to-Dynamic Reasoning **⭐⭐⭐⭐⭐** (相关度: 95%, 质量: 0.9)

- **arXiv ID**: [2608.30657](https://arxiv.org/abs/2608.30657)  · [📄 PDF](https://arxiv.org/pdf/2608.30657)
- **作者**: Lei Yang, Xiaokai Bai, Boqi Li et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/yanglei18/InfraOcc](https://github.com/yanglei18/InfraOcc)
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: 针对现有占用网络基准和方法主要面向移动自车感知，忽略了路侧固定视角下静态骨架近乎持久、动态事件稀疏短暂的结构特性这一问题，本文构建了首个真实世界路侧语义占用基准InfraOcc，包含290个多模态序列的密集体素标注，并设计了静态-动态解耦的标注流程和统一的多模态评估。进一步提出ProSD-Occ方法，将占用预测重构为静态-动态推理问题，利用静态占用占97.3%且跨帧持久、动态参与者中位占用帧率仅1.8%的结构性不对称，显著提升了动态占用预测的准确性。该工作为路侧感知和车路协同提供了新的基准和方法，具有重要的实际应用价值。
- **摘要（英）**: This paper addresses the gap in occupancy benchmarks for fixed-viewpoint infrastructure sensors, which observe persistent static scaffolds and sparse dynamic events, unlike ego-vehicle perception. It introduces InfraOcc, the first real-world infrastructure-side semantic occupancy benchmark with 290 multi-modal sequences and a static-dynamic decoupled annotation pipeline, and proposes ProSD-Occ, which reformulates occupancy prediction as static-to-dynamic reasoning to exploit the structural asymmetry where static occupancy fills 97.3% of voxels and dynamic participants have a median occupied-frame ratio of only 1.8%. The method significantly improves dynamic occupancy prediction, offering a new benchmark and approach for roadside perception and vehicle-infrastructure cooperation.
- **评估**: 该论文填补了路侧占用感知领域的空白，提出的基准和方法对自动驾驶车路协同具有重要参考价值，静态-动态解耦的思路新颖且实用。
- **核心贡献**: 构建了首个真实世界路侧语义占用基准InfraOcc，并提出静态-动态推理方法ProSD-Occ。
- **创新点**: 将占用预测重构为静态-动态推理，利用路侧场景的结构性不对称提升动态预测。
- **结果**: 静态占用占97.3%，动态参与者中位占用帧率仅1.8%，ProSD-Occ显著提升动态占用预测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fixed-viewpoint infrastructure sensors repeatedly observe the same traffic space, making roadside 3D occupancy structurally different from ego-vehicle perception: a near-persistent static scaffold is overlaid with sparse, short-lived dynamic events. Existing occupancy benchmarks and methods, however, are built around moving ego vehicles and neither measure nor exploit this structure, instead treating occupancy as flat one-shot voxel classification. We address this gap from both data and model perspectives. We build InfraOcc, to our knowledge, the first real-world infrastructure-side semantic occupancy benchmark, with dense voxel annotations for 290 multi-modal sequences in a fixed roadside frame, a static-dynamic decoupled annotation pipeline, unified camera-only, LiDAR-only, and multi-modal evaluation, and diagnostics for static and dynamic occupancy. InfraOcc shows that static infrastructure fills 97.3% of occupied voxels and persists across frames, whereas dynamic participants have a median occupied-frame ratio of only 1.8% per location, revealing a structural static-dynamic asymmetry beyond semantic long-tailedness. We further propose ProSD-Occ, which reformulates occupancy as progressive static-to-dynamic evidence reasoning: it explains persistent layout, exposes residual dynamic evidence under static-confidence guidance, and recomposes static, dynamic, and free-space evidence into a unified field. ProSD-Occ ranks first in overall, dynamic, static, and geometric occupancy on every track, e.g., a 23.5% relative camera-only dynamic-mIoU gain over the strongest baseline and 65.87 multi-modal overall mIoU, establishing fixed-viewpoint roadside occupancy as a distinct problem with its own reasoning paradigm. The benchmark and code will be publicly available at https://github.com/yanglei18/InfraOcc

</details>

---

## Network Pruning

### 1. Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.30218](https://arxiv.org/abs/2608.30218)  · [📄 PDF](https://arxiv.org/pdf/2608.30218)
- **作者**: Jingong Chen, Qingwen Zhang, Sanghyeon Jun et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-31 · **分类**: cs.CV
- **摘要（中）**: ①这篇论文针对连续时间4D重建在独立XR头显上不可行的问题，即逐场景优化计算量大且低预算下会崩溃，前馈预测虽快但缺乏场景细节。②提出了摊销锚点细化方法，使用冻结骨干网络预测初始高斯表示，并在固定计算预算下进行短优化以特化场景，同时通过容量下限保持表示密度；训练后阶段应用持久同调约束剪枝不稳定高斯，保留拓扑持久结构，并将轨迹直接作为场景流。③相比已有工作，该方法结合了前馈预测的速度和逐场景优化的细节恢复能力，并引入了拓扑约束实现稳定剪枝。④在Stage-Capture基准上达到24.31±2.22dB，在单个消费级GPU上实现目标预算内的重建，并在独立XR头显上播放。
- **摘要（英）**: This paper addresses the impracticality of continuous-time 4D reconstruction on standalone XR headsets, where per-scene optimization is computationally infeasible and feed-forward prediction lacks scene-specific detail. It proposes Amortized Anchor Refinement, combining a frozen backbone for initial Gaussian prediction with short optimization under a fixed budget, and a training-free persistent-homology constraint to prune unstable Gaussians while preserving topological structures. The method achieves 24.31±2.22dB on Stage-Capture and enables reconstruction on a single consumer GPU with playback on a standalone headset.
- **评估**: 该论文聚焦XR设备上的4D重建，与自动驾驶感知领域相关性较低，但方法中的摊销优化和拓扑剪枝思想可能对高效3D表示学习有参考价值。
- **核心贡献**: 提出了一种结合前馈预测和短优化的摊销锚点细化框架，并引入持久同调约束实现稳定高斯剪枝。
- **创新点**: 将拓扑持久性分析应用于高斯剪枝，并设计容量下限防止低预算下的表示崩溃。
- **结果**: 在Stage-Capture基准上达到24.31dB，并在消费级GPU上实现目标预算内重建。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continuous-time 4D reconstruction remains impractical on standalone XR headsets. Per-scene optimization demands deployment-infeasible compute, and lower budgets cause collapse rather than degrade gradually. Feed-forward prediction is fast, but struggle to recover scene-specific detail. We present Amortized Anchor Refinement, which uses a frozen backbone to predict an initial Gaussian representation and a short optimization to specialize it under a fixed compute budget, with a capacity floor preserving representational density. A training-free stage then applies a persistent-homology constraint to prune unstable Gaussians while preserving topologically persistent structures, and streams the resulting trajectories directly as scene flow. On the Stage-Capture benchmark, Amortized Anchor Refinement achieves 24.31$\pm$2.22dB, while our deployment experiments demonstrate reconstruction within the target budget on a single consumer GPU and playback on a standalone XR headset.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 10 |
| Multimodal | 10 |
| Object Detection | 9 |
| Multi-camera Perception | 9 |
| Video Understanding | 7 |
| Self-supervised Vision | 6 |
| Vision Transformer | 5 |
| Continual Learning | 4 |
| Open-set Detection | 3 |
| 3D Detection | 3 |
| Autonomous Driving | 3 |
| Neural Architecture Search | 1 |
| Knowledge Distillation | 1 |
| Occupancy | 1 |
| Network Pruning | 1 |
| **总计** | **73** |