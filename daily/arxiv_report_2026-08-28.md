# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-08-28  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 91 篇（其中 91 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (10篇)
- [Self-supervised Vision](#self-supervised-vision) (10篇)
- [Video Understanding](#video-understanding) (10篇)
- [Object Detection](#object-detection) (10篇)
- [Multimodal](#multimodal) (10篇)
- [Vision Transformer](#vision-transformer) (10篇)
- [Multi-camera Perception](#multi-camera-perception) (10篇)
- [Network Pruning](#network-pruning) (7篇)
- [Autonomous Driving](#autonomous-driving) (4篇)
- [Open-set Detection](#open-set-detection) (4篇)
- [3D Detection](#3d-detection) (3篇)
- [Continual Learning](#continual-learning) (2篇)
- [BEV](#bev) (1篇)

## VLM

### 1. When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.23978](https://arxiv.org/abs/2608.23978)  · [📄 PDF](https://arxiv.org/pdf/2608.23978)
- **作者**: Zhengxiang Wang, Owen Rambow
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.AI, cs.CV
- **摘要（中）**: ①针对现有视觉定位评估仅关注单次映射，忽略了真实世界中目标信息不完整、模糊且需通过交互建立的问题。②提出了一个受控的交互式视觉定位评估框架，在四种人类视觉上下文和四种交互协议下，系统性地改变初始目标信息量和需通过对话获取的信息量，评估大型视觉语言模型（LVLM）的表现。③相比已有工作，首次系统性地将交互引入视觉定位评估，并分析了交互对定位性能的影响。④实验发现，当前LVLM在交互式视觉定位任务上显著低于人类基线，且当无初始描述时性能最差，模型置信度校准不佳，过度自信。
- **摘要（英）**: This paper addresses the limitation of conventional visual grounding evaluation that overlooks interactive and incomplete target information. It introduces a controlled benchmark with four human-grounded contexts and four interaction protocols, revealing that current LVLMs significantly underperform human baselines, especially when no initial description is given. The study also highlights poor confidence calibration in LVLMs, suggesting that proactive question-driven grounding remains a major challenge.
- **评估**: 该论文为交互式视觉定位提供了首个系统性基准，揭示了LVLM在真实交互场景中的不足，对多模态感知研究具有重要参考价值。
- **核心贡献**: 提出了交互式视觉定位的受控评估框架，并系统分析了LVLM在交互场景下的性能与校准问题。
- **创新点**: 将交互引入视觉定位评估，设计了多协议和多上下文的基准测试。
- **结果**: LVLM在交互式视觉定位上显著低于人类基线，且置信度校准差。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual grounding is typically evaluated as a one-shot mapping from an informative referring expression to a visual target. This formulation misses a central property of real-world reference: target information is often incomplete, ambiguous, and established through interaction. We introduce a controlled evaluation framework for interactive visual grounding in large vision-language models (LVLMs), varying how much target information is provided upfront and how much must be acquired through dialogue. Across four human-grounded visual contexts and four interaction protocols, current LVLMs perform significantly below task-level human baselines. Interaction can help when follow-up questions refine or repair an initial target description. Performance is lowest when no initial description is provided and target information must be acquired through questions, indicating that proactive question-driven grounding remains difficult. LVLMs are also poorly calibrated, often reporting confidence that exceeds their empirical accuracy. Follow-up studies confirm these patterns across varied description sources (human versus AI), reasoning efforts, repeated interactions, description providers, and visual contexts. Overall, interactive visual grounding remains an important challenge, requiring visual matching, information seeking and synthesis.

</details>

### 2. Semi-Supervised Adaptation of Vision-Language Models for Image Classification **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.25485](https://arxiv.org/abs/2608.25485)  · [📄 PDF](https://arxiv.org/pdf/2608.25485)
- **作者**: Mohamed L. Mekhalfi, Mohamad M. Al Rahhal, Yakoub Bazi et al. (7 authors)
- **🏷️ 机构**: Fondazione Bruno Kessler, Via Sommarive 18, King Saud University, Tarim University
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: ①针对视觉语言模型（如CLIP）在卫星图像分类中性能受限且标注样本稀缺的问题。②提出了Self-Evolutionary CLIP（SE-CLIP），一个半监督框架，通过初始热身和递归发现阶段，从无标签池中迭代挖掘高置信度样本，并采用类平衡选择策略防止模型偏向易学类别。③相比现有参数高效微调方法，SE-CLIP在极少标注下实现了递归标签挖掘，减少了人工干预。④在UCM和NWPU基准上，SE-CLIP显著优于现有半监督方法，为遥感领域VLM适配提供了可行方案。
- **摘要（英）**: This paper addresses the performance degradation of CLIP on satellite imagery due to domain gap and annotation scarcity. It proposes SE-CLIP, a semi-supervised framework with a warm-up phase and recursive label mining, using class-balanced selection to maintain support set integrity. Results on UCM and NWPU benchmarks show significant improvements over existing semi-supervised methods, enabling efficient VLM adaptation with minimal human effort.
- **评估**: 该论文针对遥感场景的VLM适配问题提出了实用的半监督方案，虽领域相关度一般，但方法具有通用性。
- **核心贡献**: 提出了SE-CLIP半监督框架，通过递归标签挖掘和类平衡策略提升卫星图像分类性能。
- **创新点**: 将自进化思想引入CLIP适配，实现无标注数据的递归利用。
- **结果**: 在UCM和NWPU上显著优于现有半监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models like CLIP have shown sig- nificant potential in handling natural images, yet their perfor- mance is often limited by the distinct characteristics of satellite imagery. While parameter-efficient adaptation techniques exist, their efficacy is frequently limited by the scarcity of annotated samples. In this letter, we propose Self-Evolutionary CLIP (SE- CLIP), a semi-supervised framework designed for recursive label mining in scene classification. The approach follows a dual-phase pipeline, where an initial warm-up on a few annotated seeds is followed by a recursive discovery phase that iteratively identifies high-confidence samples from unlabeled pools. To maintain the integrity of the evolving support set, we employ a class-balanced selection strategy that prevents the model from being dominated by easily learned categories. Results on the UCM and NWPU benchmarks indicate that SE-CLIP significantly outperforms existing semi-supervised approaches. The framework provides a viable solution for adapting VLMs to the remote sensing domain with minimal human intervention.

</details>

### 3. GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models **⭐⭐⭐** (相关度: 40%, 质量: 0.75)

- **arXiv ID**: [2608.25375](https://arxiv.org/abs/2608.25375)  · [📄 PDF](https://arxiv.org/pdf/2608.25375)
- **作者**: Yiqun Sun, Junyu Chen, Pengfei Wei et al. (4 authors)
- **🏷️ 机构**: Magellan Technology Research Institute (MTRI)
- **💻 代码**: [github.com/dukesun99/GGSS](https://github.com/dukesun99/GGSS)
- **提交日期**: 2026-08-26 · **分类**: cs.CY, cs.CL, cs.CV
- **摘要（中）**: ①针对生成式视觉语言模型在人口统计属性上产生有偏输出，而现有推理时去偏方法主要针对静态嵌入或CLIP模型的问题。②提出了GGSS（Geodesic-Gated Spherical Steering），一种保范干预方法，在单位超球面上发现反事实偏置子空间，沿测地线弧引导视觉令牌，并使用自适应门控聚焦于携带强人口统计信号的令牌。③相比现有推理时去偏基线，GGSS专门针对生成式VLM设计，并采用单操作点协议进行评估。④在四个生成式VLM上，GGSS在分类、成对和职业-性别偏置测试中取得最低平均偏置，同时在MMStar准确率上保持±0.6个百分点内的稳定性。
- **摘要（英）**: This paper addresses demographic bias in generative VLMs, which existing inference-time debiasers fail to handle effectively. It proposes GGSS, a norm-preserving intervention that discovers a counterfactual bias subspace and steers visual tokens along geodesic arcs with adaptive gating. Evaluations on four generative VLMs show the lowest average bias across multiple tests while preserving general capability within 0.6 p.p. on MMStar.
- **评估**: 该论文针对生成式VLM的偏置问题提出了创新的推理时干预方法，实验充分，对公平性研究有贡献。
- **核心贡献**: 提出了GGSS方法，通过测地线门控球面引导实现生成式VLM的推理时去偏。
- **创新点**: 首次将测地线干预和自适应门控应用于生成式VLM的偏置修正。
- **结果**: 在四个模型上取得最低平均偏置，且保持视觉语言能力稳定。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative vision-language models (VLMs) are increasingly used in human-centered settings, yet they can produce demographically biased outputs even when images differ only in controlled attributes such as perceived race or gender. However, existing inference-time debiasers were largely designed for static embeddings or CLIP-like models rather than generative VLMs. We propose GGSS---Geodesic-Gated Spherical Steering---a norm-preserving intervention that discovers a counterfactual bias subspace on the unit hypersphere, steers visual tokens along geodesic arcs, and uses an adaptive gate to focus correction on tokens that carry stronger demographic signal. We evaluate four generative VLMs against ten adapted inference-time debiasing baselines and prompt-based mitigation under a single operating-point protocol across categorical, pairwise, and occupation-gender bias tests, while also measuring general visual-language capability. GGSS achieves the lowest average bias on all four models, significant on three of four backbones under paired permutation tests, while preserving MMStar accuracy within +/- 0.6 p.p. of the unsteered baseline. Code is available at https://github.com/dukesun99/GGSS.

</details>

### 4. MLLMCLIP: Feature-Level Distillation of MLLM for Robust Vision-Language Representations **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.85)

- **arXiv ID**: [2608.25575](https://arxiv.org/abs/2608.25575)  · [📄 PDF](https://arxiv.org/pdf/2608.25575)
- **作者**: Jongsuk Kim, Qiyu Wu, Zhuoyuan Mao et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对CLIP等预训练视觉语言模型在组合性（属性-对象和关系结构）上表现不佳，而现有方法依赖合成硬负例导致巨大流水线开销的问题。②提出了MLLMCLIP，一个异构蒸馏框架，直接从生成式多模态大语言模型（MLLM）教师中转移多模态知识到判别式CLIP学生，完全绕过合成数据。③为弥合架构差异，引入了基于注意力的逐层令牌选择和CKA蒸馏损失。④相比现有CLIP增强方法，MLLMCLIP在组合准确率上达到最先进水平，并在零样本分类和图像文本检索上持续提升，表明特征级蒸馏增强了组合和通用视觉语言表示能力。
- **摘要（英）**: This paper tackles the compositional weakness of CLIP without relying on synthetic hard negatives. It proposes MLLMCLIP, a heterogeneous distillation framework that transfers knowledge from a generative MLLM teacher to a CLIP student via attention-based token selection and CKA loss. The method achieves state-of-the-art compositional accuracy and consistent gains on zero-shot classification and retrieval, demonstrating the power of feature-level distillation.
- **评估**: 该论文提出了一种新颖的异构蒸馏方法，有效提升了CLIP的组合性，方法创新且实验扎实，对多模态学习有重要价值。
- **核心贡献**: 提出了MLLMCLIP框架，通过特征级蒸馏从MLLM向CLIP转移多模态知识，提升组合表示能力。
- **创新点**: 引入注意力令牌选择和CKA损失解决异构架构蒸馏问题。
- **结果**: 在组合准确率上达到SOTA，并提升零样本分类和检索性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained vision-language models such as CLIP excel at zero-shot recognition but often fail at compositionality, particularly attribute-object and relational structures. Recent studies mitigate this issue by augmenting training with synthetic hard negatives generated by a cascade of large language models and text-to-image models, which incurs substantial pipeline overhead. We instead propose MLLMCLIP, a heterogeneous distillation framework that transfers multimodal knowledge directly from a generative Multimodal Large Language Model (MLLM) teacher into a discriminative CLIP student, bypassing synthetic data entirely. To bridge the architectural mismatch between the two paradigms, we introduce an attention-based per-layer token selection and a CKA-based distillation loss. Compared to prior CLIP-enhancement methods, MLLMCLIP achieves state-of-the-art compositional accuracy while delivering consistent gains on standard zero-shot classification and image-text retrieval, showing that feature-level distillation strengthens both compositional and general vision-language representation capability.

</details>

### 5. MVC-Bench: Benchmarking Calibration of Medical Vision-Language Models **⭐⭐** (相关度: 25%, 质量: 0.6)

- **arXiv ID**: [2608.27004](https://arxiv.org/abs/2608.27004)  · [📄 PDF](https://arxiv.org/pdf/2608.27004)
- **作者**: Ashshak Sharifdeen, Shihab Aaqil Ahamed, Ufaq Khan et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对医学视觉语言模型校准不足的问题，提出校准基准MVC-Bench。②评估三个维度：对模态/骨干/域偏移的鲁棒性、校准策略和提示调优的有效性、对提示模板和随机种子的稳定性。③覆盖8种骨干、3种模态（眼底、病理、胸片），比较多种校准和提示方法。④通过1638+受控实验，报告准确率和期望校准误差（ECE）等指标。
- **摘要（英）**: This paper introduces MVC-Bench, a calibration-centric benchmark for medical VLMs, assessing robustness to shifts, calibration strategies, and stability. It covers eight backbones and three modalities with 1638+ experiments, reporting accuracy and ECE. The work highlights calibration gaps in medical VLMs under realistic conditions.
- **评估**: 该论文关注医学VLM校准，与自动驾驶多模态感知有一定方法关联，但领域差异大，实用性有限。
- **核心贡献**: 提出首个医学VLM校准基准MVC-Bench。
- **创新点**: 系统评估校准鲁棒性和稳定性。
- **结果**: 揭示现有VLM校准不足，提供基准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reliable evaluation of vision-language models (VLMs) and medical vision-language models (Medical-VLMs) requires calibrated confidence, particularly under realistic clinical conditions. However, existing efforts mainly focused on improving accuracy, leaving calibration in the medical domain underexplored. To this end, we propose MVC-Bench, a calibration-centric benchmark for medical image classification with VLMs and Medical-VLMs. MVC-Bench assesses the calibration across three axes: (i) robustness to modality, backbone, and domain shift (ii) effectiveness of calibration strategies and prompt-tuning methods (iii) stability under prompt-template and random-seed variations. The benchmark covers eight different backbones, three medical modalities, including fundus imaging, histopathology, and chest X-ray under in-domain and domain shift settings. It compares post-hoc calibration, train-time calibration, and zero-shot inference methods, together with six prompt-tuning methods. Across more than 1638 controlled experiments, we report accuracy and Expected Calibration Error (ECE) as primary metrics, and further report results with complementary calibration measures, including Maximum Calibration Error (MCE) and Adaptive Calibration Error (ACE). We further investigate the underlying causes of miscalibration in VLMs and Medical-VLMs and propose a simple train-time calibration method, Multi-Class Margin (MCM) regularization, which achieves lowest ECE on 10 out of 12 settings in in-domain and remains competitive under domain shifts. Collectively, MVC-Bench provides a structured evaluation framework and actionable guidance for improving calibration in safety-critical medical workflows.

</details>

### 6. Beyond Atomic Layouts: Compositional Design Understanding with Vision-Language Models **⭐⭐⭐** (相关度: 30%, 质量: 0.65)

- **arXiv ID**: [2608.26716](https://arxiv.org/abs/2608.26716)  · [📄 PDF](https://arxiv.org/pdf/2608.26716)
- **作者**: Yiyang Huang, Zhaowen Wang, Simon Jenni et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对VLM在组合布局理解上的不足，提出新任务和数据集CoDeLayout。②构建约20K真实多层布局VQA数据集，标注组合元素对和设计意图，并提出MASON后训练范式。③MASON包含多模态对齐（MA）和结构感知（SP），分别缓解语义漂移和层级关系模糊。④实验表明现有VLM在组合布局上表现差，MASON显著提升理解能力。
- **摘要（英）**: This paper introduces compositional layout understanding and the CoDeLayout dataset (~20K samples) to address VLM limitations. It proposes MASON with multimodal alignment and structural perception to mitigate semantic drift and structural ambiguity. Experiments show MASON improves compositional layout reasoning over existing VLMs.
- **评估**: 该论文涉及VLM和视觉理解，与自动驾驶场景理解有间接关联，但目标领域为文档/UI设计，相关性中等。
- **核心贡献**: 提出组合布局理解任务和MASON方法。
- **创新点**: 结合多模态对齐和结构感知处理层级布局。
- **结果**: 显著提升组合布局理解性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Layout understanding, or the interpretation of element organization, is essential for document analysis, user interface (UI) creation, and graphic design. While recent vision-language models (VLMs) excel at interpreting atomic layouts composed of independent elements, they struggle with compositional layouts that require reasoning over visually entangled elements within hierarchical multi-layer structures. In this paper, we introduce a new task, compositional layout understanding, and present CoDeLayout, a VQA dataset of ~20K real-world multi-layer layouts annotated with compositional element pairs and design intent. Through empirical analysis on CoDeLayout, we identify two key challenges for existing VLMs: semantic drift between textual metadata and visual content, and structural ambiguity in hierarchical inter-element relationships. To address these challenges, we propose MASON, a post-training paradigm that integrates multimodal alignment (MA) and structural perception (SP). MA enhances element interpretation by grounding metadata-defined elements to their visual counterparts, mitigating semantic drift, while SP models layer-aware inter-element spatial relationships to improve hierarchical understanding and reduce structural ambiguity. Experiments reveal substantial gaps in existing VLMs: even the strongest baseline, GPT-o3, achieves only 79.68% accuracy, whereas Qwen2.5-VL 7B with MASON reaches 91.66%. Notably, MASON surpasses full-data Direct Finetune using only 30% of the training data and scales better with additional data.

</details>

### 7. Do Vision-Language Models Agree on the Affective Qualities of Shape? A Cross-Model Audit for Generative Design Interfaces **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2608.25876](https://arxiv.org/abs/2608.25876)  · [📄 PDF](https://arxiv.org/pdf/2608.25876)
- **作者**: Luca Bux, Thiago Rios, Ingo Scholtes et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.HC, cs.CV
- **摘要（中）**: ①针对生成设计界面中，不同视觉语言模型（VLM）在表示对象情感品质（如“优雅”、“极简”）时是否一致的问题。②审计了6个VLM，通过沿Kansei形容词对（情感印象）对无纹理3D对象进行排序，以文本表示差异定义轴，并使用几何对作为正对照，无关形容词对建立经验零假设。③相比已有工作，首次系统评估了VLM在情感品质上的跨模型一致性。④在ShapeNet的10个类别中，情感轴的一致性高于零假设（平均秩相关0.36 vs 0.14），但低于几何上限（0.44），且一致性高度不均匀，取决于类别表示变化与语义方向的匹配程度。
- **摘要（英）**: This paper investigates whether different VLMs consistently represent affective qualities of 3D objects in generative design interfaces. It audits six VLMs by ranking objects along Kansei adjective pairs, finding that affective axes converge above the null but below geometric controls, with high variability across categories. The study reveals that consistency depends on alignment between category variation and semantic direction, rather than overall shape variance.
- **评估**: 该论文关注VLM在情感语义上的一致性，但领域相关度较低，实验规模有限，对自动驾驶感知参考价值不大。
- **核心贡献**: 首次审计了多个VLM在3D对象情感品质表示上的一致性。
- **创新点**: 将Kansei工程引入VLM评估，建立跨模型一致性审计框架。
- **结果**: 情感轴一致性部分高于零假设，但低于几何控制，且类别间差异大。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative design interfaces increasingly expose semantic controls that let users steer output with concepts such as "more elegant" or "more minimalist," typically encoded by a vision-language model (VLM). A practical question is whether state-of-the-art VLMs represent objects consistently in terms of the same concept. We audit 6 VLMs by ranking untextured 3D objects along Kansei adjective pairs, where Kansei describes affective impressions of product form, with each axis defined as the difference between the text representations of its two poles. Geometric pairs serve as positive controls, and pairs of unrelated adjectives establish an empirical null. Across 10 categories of ShapeNet database, affective axes converge above the null (mean pairwise rank correlation 0.36 vs. 0.14) but below the geometric ceiling (0.44). The agreement between models is partial and highly uneven: on the three axes shared by all categories, mean convergence ranges from 0.21 for bookshelves to 0.51 for jars. Convergence depends primarily on whether a category's representational variation aligns with the semantic direction being evaluated, rather than simply on how much the objects vary in shape overall. Cross-model convergence does not imply agreement with human judgments. Based on our findings, we implement a UI prototype that shows how the audit can inform which Kansei descriptors to expose as controls for a given object class and which to withhold.

</details>

### 8. What Do Medical Vision-Language Models Learn in Radiology? Transfer, Alignment, and Source-Proxy Leakage Under Distribution Shift **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.25251](https://arxiv.org/abs/2608.25251)  · [📄 PDF](https://arxiv.org/pdf/2608.25251)
- **作者**: Ayoub Louaye Bouaziz, Lokmane Chebouba, Yassine Himeur
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对医学视觉语言模型在分布偏移下表现不可靠的问题，研究了其表示层面的盲点。利用NIH ChestXray14和CheXpert等数据集，通过跨数据集视觉迁移和对抗适应诊断，评估了多模态对齐和源代理信息泄漏。发现自监督视觉初始化优于监督ImageNet初始化，而对抗适应仅在窄范围内有效，且多模态精确配对检索在外部压力测试下表现低。定性分析显示临床合理的跨数据集结构和胸部注意力。
- **摘要（英）**: This paper investigates representation-level blind spots in medical VLMs under distribution shift, using cross-dataset transfer and adversarial adaptation diagnostics. Self-supervised visual initialization improves transfer over supervised initialization, while adversarial adaptation is unstable and multimodal exact-pair retrieval remains low under external stress testing. Qualitative analyses reveal clinically plausible cross-dataset structure.
- **评估**: 该论文对医学VLM的鲁棒性提供了深入分析，但领域相关性较低，主要面向医学影像而非自动驾驶感知。
- **核心贡献**: 系统分析了医学VLM在分布偏移下的表示级盲点和源代理泄漏。
- **创新点**: 结合跨数据集迁移和对抗适应诊断，量化多模态对齐和源代理信息。
- **结果**: 自监督初始化提升迁移，对抗适应不稳定，精确配对检索率低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Medical vision-language models (VLMs) can appear reliable in-domain while failing when acquisition domain, paired supervision, or evaluation protocol changes. We study this failure mode as a representation-level blind spot relevant to epistemic intelligence, without claiming a formal estimator of epistemic uncertainty. Using NIH ChestXray14 and CheXpert, we first isolate source-only cross-dataset visual transfer from unsupervised domain-adaptation diagnostics. Using PadChest and OpenI, we then evaluate multimodal alignment under strict pair-index retrieval and quantify metadata-derived source-proxy information retained in frozen embeddings. Self-supervised visual initialization improves NIH-to-CheXpert transfer over supervised ImageNet initialization in matched ResNet-18 comparisons, whereas adversarial adaptation is useful only in a narrow regime and becomes unstable as adversarial pressure increases. Multimodal exact-pair retrieval remains low under external OpenI stress testing, and source-proxy information remains recoverable from learned representations. Qualitative nearest-neighbor and Grad-CAM analyses show clinically plausible cross-dataset structure and thoracic attention patterns in many cases, while device-heavy and false-positive cases remain ambiguous. Auxiliary architecture checks are task-dependent and do not support a universal backbone ranking. Overall, the study shows that apparent competence under a single protocol can conceal transfer, alignment, and shortcut-related failure modes, motivating stress-tested evaluation of medical VLMs under distribution shift.

</details>

### 9. DoublesEval: Diagnosing Multi-Agent Tactical Reasoning in Vision-Language Models via Professional Doubles Badminton **⭐⭐⭐** (相关度: 50%, 质量: 0.65)

- **arXiv ID**: [2608.24439](https://arxiv.org/abs/2608.24439)  · [📄 PDF](https://arxiv.org/pdf/2608.24439)
- **作者**: Jintao Cheng, Weibin Li
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Chengjt1999/DoublesEval](https://github.com/Chengjt1999/DoublesEval)
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: 针对视觉语言模型在动态多智能体交互推理上的不足，提出了多智能体战术推理能力并构建了DoublesEval诊断框架，利用职业双打羽毛球作为测试平台。该框架通过关键时刻协议分解回合，从原子识别、段内复合理解、跨段因果推理和高层战术抽象四个维度评估模型。提出了TacticCheck，一种轻量级约束引导的测试时一致性检查器，无需参数更新或标签即可重排候选答案。在60个精选回合上评估了四个开源VLM，揭示了推理失败的具体位置。
- **摘要（英）**: This paper formalizes multi-agent tactical reasoning and introduces DoublesEval, a diagnostic framework using professional doubles badminton to evaluate VLMs across four interpretable dimensions. TacticCheck, a constraint-guided test-time consistency checker, reranks answers without parameter updates. Evaluation on four VLMs reveals specific reasoning failure modes.
- **评估**: 该论文提出了新颖的评估框架，但领域相关性一般，主要关注体育场景而非自动驾驶。
- **核心贡献**: 形式化多智能体战术推理并提供结构化诊断框架。
- **创新点**: 利用职业羽毛球作为测试平台，结合测试时一致性检查。
- **结果**: 揭示了VLM在动态交互推理中的具体失败模式。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual Language Models (VLMs) excel at describing visible scene content but struggle to reason about dynamic multi-agent interactions, where action semantics depend on coordinated roles and spatial-temporal dependencies. We formalize this capability as \textbf{multi-agent tactical reasoning} and introduce \textbf{DoublesEval}, a diagnostic evaluation framework that leverages professional doubles badminton as a structurally tractable testbed. DoublesEval employs a key-moment-based protocol that decomposes rallies into tactically salient instants and probes models across four interpretable dimensions: atomic recognition, intra-segment composite understanding, cross-segment causal reasoning, and high-level tactical abstraction. This design isolates \emph{where} reasoning fails, rather than merely measuring answer correctness. To address observed failure modes, we propose \textbf{TacticCheck}, a lightweight constraint-guided test-time consistency checker that reranks candidate answers using the model's own lower-level tactical predictions, requiring no parameter updates or ground-truth labels at inference time. Evaluating four representative open-source VLMs on 60 curated rallies (yielding $\sim$9.6K structured instances) via a zero-shot protocol, we find that models remain weak across all diagnostic levels, with especially clear bottlenecks in spatial state, interaction binding, and terminal evidence. TacticCheck delivers consistent gains across all evaluated models, while still leaving a substantial gap to robust tactical reasoning. These results highlight the need for structured, interaction-aware evaluation paradigms for next-generation VLMs. The source code is available in \href{https://github.com/Chengjt1999/DoublesEval}{\textcolor{blue}{our GitHub repository}}.

</details>

### 10. What Does Prompt Learning Change? -A Natural-Language Concept Analysis of Vision-Language Models **⭐⭐⭐** (相关度: 45%, 质量: 0.7)

- **arXiv ID**: [2608.24142](https://arxiv.org/abs/2608.24142)  · [📄 PDF](https://arxiv.org/pdf/2608.24142)
- **作者**: Ryo Kamiya, Hiroshi Kera, Kazuhiko Kawamoto
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: 针对提示学习优化连续提示向量但难以解释的问题，提出了PromptSpLiCE方法，将类条件文本嵌入表示为固定自然语言字典中概念的稀疏组合。通过比较提示学习前后的概念轮廓，评估了CoOp在11个图像分类数据集上的变化。发现概念轮廓变化显著，平均仅1.6个初始前10概念保留，且轮廓变化与准确率提升正相关。推导了局部梯度表达式，提供了几何直觉。
- **摘要（英）**: This paper introduces PromptSpLiCE to interpret prompt learning by expressing text embeddings as sparse concept combinations. Evaluation on CoOp across 11 datasets shows significant concept profile changes, positively associated with accuracy gains. A local gradient expression provides geometric intuition for loss sensitivity.
- **评估**: 该论文提供了提示学习的可解释性分析，但相关性较低，主要面向图像分类而非自动驾驶。
- **核心贡献**: 提出后验方法解释提示学习的概念变化。
- **创新点**: 利用稀疏概念字典比较提示学习前后的轮廓。
- **结果**: 概念轮廓变化与准确率提升正相关。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning adapts vision-language models such as CLIP by optimizing continuous prompt vectors, but the learned prompts are difficult to interpret in natural language. We present PromptSpLiCE, a post-hoc method that expresses each class-conditioned text embedding as a sparse combination of concepts from a fixed natural-language dictionary. Using the same dictionary before and after prompt learning allows us to compare changes in their concept profiles. We evaluate PromptSpLiCE on CoOp, a representative prompt-learning method, across 11 image-classification datasets. The concept profiles change substantially: on average, only 1.6 of the initial top-10 concepts remain in the top 10 after learning. Across datasets, profile change is positively associated with accuracy gain. We also derive a local gradient expression that provides geometric intuition for why image-aligned concept directions distinct from the current prompt can have greater loss sensitivity.

</details>

---

## Self-supervised Vision

### 1. Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2608.24093](https://arxiv.org/abs/2608.24093)  · [📄 PDF](https://arxiv.org/pdf/2608.24093)
- **作者**: Jheng-Ling Lee, Shang-Tse Chen
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对4D点云视频自监督学习中标注成本高和基于重建的预训练过度强调低层几何细节的问题。②提出了一个JEPA风格的框架，通过掩码点管预测在特征空间中进行潜在表示学习，并引入Sketched Isotropic Gaussian Regularization来稳定潜在预测，避免嵌入坍塌。③相比重建式预训练，该方法在预训练目标上更贴合下游语义识别，同时捕捉空间结构和时间动态。④在动作和手势识别基准上，该方法提升了微调、少标签学习和跨数据集迁移的性能，表明JEPA式潜在预测是重建式预训练的有效替代方案。
- **摘要（英）**: This paper tackles the challenges of costly annotations and overemphasis on low-level geometry in 4D point cloud video self-supervised learning. It proposes a JEPA-style framework that predicts masked point-tube representations in latent space with a sketched isotropic Gaussian regularizer, avoiding explicit reconstruction. Experiments on action and gesture recognition show improved fine-tuning, limited-label learning, and cross-dataset transfer, validating the effectiveness of latent prediction over reconstruction-based pretraining.
- **评估**: 该论文将JEPA思想成功应用于4D点云视频，为自监督学习提供了新方向，对自动驾驶中的动态场景理解有潜在价值。
- **核心贡献**: 提出了基于JEPA的4D点云视频自监督预训练方法，通过潜在点管预测提升语义表示质量。
- **创新点**: 引入Sketched Isotropic Gaussian Regularization稳定潜在预测，避免嵌入坍塌。
- **结果**: 在动作和手势识别上显著提升下游任务性能，包括少标签和跨数据集场景。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised representation learning for 4D point cloud videos is challenging because annotations are costly and reconstruction-based pretraining can overemphasize low-level geometric details. We propose a JEPA-style framework that learns from unlabeled spatiotemporal point clouds through latent point-tube prediction. Instead of reconstructing raw coordinates, the model masks spatiotemporal regions and predicts their target representations from visible context representations in feature space. To stabilize latent prediction, we incorporate Sketched Isotropic Gaussian Regularization, which encourages non-collapsed embeddings without relying on explicit reconstruction targets. This formulation aims to capture both spatial structure and temporal dynamics while keeping the pretraining objective aligned with downstream semantic recognition. Experiments on action and gesture recognition benchmarks show that the learned representations improve downstream fine-tuning, limited-label learning, and cross-dataset transfer. These results suggest that JEPA-style latent prediction is a promising alternative to reconstruction-centered pretraining for 4D point cloud videos.

</details>

### 2. Domain-Specific Self-Supervised Representation Learning for Retinal Fundus Classification **⭐⭐** (相关度: 20%, 质量: 0.5)

- **arXiv ID**: [2608.26686](https://arxiv.org/abs/2608.26686)  · [📄 PDF](https://arxiv.org/pdf/2608.26686)
- **作者**: Bekzat Nurlanbekova, Fung Fung Ting
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对医学图像标注稀缺、监督学习成本高的问题，探索对比自监督学习在视网膜眼底图像分类中的应用。②研究了SimSiam和SimCLR两种SSL框架，结合视网膜特定增强策略，在资源受限条件下用小批量训练。③通过线性评估和微调评估多疾病分类和糖网分级任务，强调增强策略需适配数据特性。④结果表明定制增强策略能提升表示质量，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the scarcity of annotated medical images by investigating contrastive self-supervised learning (SimSiam and SimCLR) for retinal fundus classification. It explores augmentation strategies and training parameters under resource-constrained settings, evaluating via linear probing and fine-tuning. Results suggest tailored augmentations improve representation quality, though specific metrics are omitted.
- **评估**: 该论文聚焦医学图像SSL，与自动驾驶感知领域相关性低，方法常规，实验规模有限，创新性一般。
- **核心贡献**: 探索了视网膜特定增强策略在资源受限SSL中的可行性。
- **创新点**: 将领域特定增强融入小批量SSL训练。
- **结果**: 定制增强提升下游分类性能，但无具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the growing number of public datasets, annotated medical images remain scarce. Supervised learning methods achieve strong performance on many benchmarks, however require large amounts of labeled data, which are costly and time-consuming to obtain in the medical domain. To address this limitation, contrastive self-supervised learning (SSL) has emerged as a promising alternative for learning useful representations from unlabeled data. In this work, we investigate two SSL frameworks, SimSiam and SimCLR, for retinal disease classification from fundus images. We focus on understanding how augmentation strategies and training parameters influence representation learning under resource-constrained settings. Given limited data and computational capacity, we explore the feasibility of training SSL models with small batch sizes incorporated with retinal-specific augmentation techniques. Through a series of experiments, we assess the quality of learned representations via linear evaluation and fine-tuning across downstream tasks, including multi-disease classification and diabetic retinopathy grading. Our results show that tailoring augmentation strategies to the characteristics of retinal images plays a critical role in improving performance. Even under constrained settings, lightweight SSL frameworks can learn transferable representations that reduce dependence on large annotated datasets and achieve competitive results.

</details>

### 3. B-MIM: Biased Masked Image Modeling for Generalizable Segmentation of Fine-Grained Anatomical Structures **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.24364](https://arxiv.org/abs/2608.24364)  · [📄 PDF](https://arxiv.org/pdf/2608.24364)
- **作者**: Sebastián González, Karen Sanchez, José M. Saavedra et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: ①针对医学CT图像中自监督预训练编码器偏向粗粒度语义理解，对血管、小肿瘤等精细解剖结构不敏感的问题。②提出偏置掩码图像建模（B-MIM），通过随机降低全局语义对齐、优先局部块重建，使编码器捕获高频形态细节和结构连续性，并在17个公开来源的9955例CT腹部数据上预训练3D Swin Transformer。③相比标准iBOT目标，B-MIM通过减少全局语义压力增强对复杂结构的泛化能力。④在肝脏血管分割任务上提升了拓扑保真度（clDice），在肿瘤分割中取得有竞争力的Dice分数，且仅更新少量参数。
- **摘要（英）**: This paper addresses the insensitivity of CT encoders to fine-grained anatomical structures by proposing Biased Masked Image Modeling (B-MIM), which stochastically reduces global semantic alignment to prioritize local patch reconstruction. Pretrained on 9,955 CT studies, the 3D Swin Transformer backbone improves topological fidelity in liver vessel segmentation and achieves competitive tumor segmentation Dice scores with minimal parameter updates.
- **评估**: 该论文针对医学图像精细结构分割的预训练偏差问题，提出简单有效的B-MIM方法，对医学影像自监督学习有参考价值，但与自动驾驶感知领域相关性较低。
- **核心贡献**: 提出B-MIM自监督预训练策略，通过偏置全局语义对齐提升精细解剖结构的分割泛化能力。
- **创新点**: 在iBOT目标中引入随机全局语义对齐降低机制，优先局部重建以捕获高频细节。
- **结果**: 在肝脏血管分割中提升clDice，肿瘤分割中达到有竞争力的Dice分数。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pretraining enables transferable representations for medical imaging, yet most CT encoders remain biased toward coarse semantic understanding, limiting their sensitivity to fine-grained anatomical structures such as vessels or small tumors. In this paper, we introduce Biased Masked Image Modeling (B-MIM), a modification of the iBOT objective that stochastically reduces global semantic alignment to prioritize local patch reconstruction. This bias encourages the encoder to capture high-frequency morphological details and structural continuity. We curate a multi-institutional CT abdominal dataset of 9,955 filtered studies from 17 public sources and pretrain a 3D Swin Transformer backbone using B-MIM. Across inter-dataset experiments on liver vessel segmentation, the proposed encoder improves topological fidelity (clDice) and achieves competitive Dice scores in tumor segmentation, compared to fully fine-tuned baselines, despite updating only a fraction of the parameters. Our results suggest that reducing global semantic pressure during pretraining enhances generalization to intricate anatomical structures.

</details>

### 4. DINOcular: Self-Supervised Visuospatial Representations **⭐⭐⭐** (相关度: 60%, 质量: 0.6)

- **arXiv ID**: [2608.27226](https://arxiv.org/abs/2608.27226)  · [📄 PDF](https://arxiv.org/pdf/2608.27226)
- **作者**: Farkhat Almukhamedov, Sami Azirar, Hermann Blum
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对视觉基础模型仅用RGB训练、缺乏几何信息的问题，提出RGB-D自监督框架DINOcular。②通过深度导出的几何先验与视觉骨干结合，采用块间和块内融合，编码外观和空间结构。③在3D几何基准上优于同类方法，同时保持语义迁移能力。④在RGB-D语义分割任务上表现有竞争力。
- **摘要（英）**: This paper presents DINOcular, a self-supervised framework for joint visuospatial representations from RGB-D data. It integrates depth-derived geometric priors via inter/intra-patch fusion, improving 3D awareness while preserving semantic transfer. It outperforms comparable methods on 3D benchmarks and remains competitive on RGB-D segmentation.
- **评估**: 该论文与自动驾驶3D感知相关，但实验规模较小，方法创新性中等，实用性待验证。
- **核心贡献**: 提出RGB-D自监督表示学习框架。
- **创新点**: 深度几何先验与视觉骨干融合。
- **结果**: 3D基准上优于同类方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a self-supervised framework for learning joint visuospatial representations from RGB-D observations. While modern vision foundation models are trained almost exclusively on RGB images, many embodied systems have access to explicit depth sensing, which provides geometric information that monocular inputs cannot recover. Our method integrates depth-derived geometric priors with a visual backbone through inter-patch and intra-patch fusion, enabling the model to encode both appearance and spatial structure efficiently. The resulting representation shows promising improvements on 3D awareness while preserving semantic transfer: it outperforms prior methods of comparable scale on multiple 3D geometry benchmarks, and remains competitive when probed for standard RGB-D semantic segmentation tasks.

</details>

### 5. LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics **⭐⭐⭐⭐** (相关度: 65%, 质量: 0.8)

- **arXiv ID**: [2608.27395](https://arxiv.org/abs/2608.27395)  · [📄 PDF](https://arxiv.org/pdf/2608.27395)
- **作者**: Lukas Kuhn, Lucas Maes, Giuseppe Serra et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对视频自监督预训练计算昂贵、依赖复杂启发式（如EMA、stop-gradient）的问题，提出LeVJEPA。②基于LeJEPA的无崩溃目标，仅用编码器和投影器，单一超参数，通过SIGReg正则化保证不崩溃。③采用均匀随机token丢弃降低计算成本，同时提升下游精度。④在相同数据和epoch下，匹配或超越V-JEPA 2，预训练计算减少5.6至20.8倍。
- **摘要（英）**: This paper introduces LeVJEPA, a video encoder trained with LeJEPA's collapse-free objective, eliminating EMA and stop-gradient heuristics. It uses a single encoder-projector architecture with SIGReg regularization and random token dropping, reducing compute significantly. At matched epochs, it matches or surpasses V-JEPA 2 with 5.6-20.8x less pretraining compute.
- **评估**: 该论文在视频自监督学习上具有高效率和可扩展性，与自动驾驶视频感知相关，方法简洁且实验扎实。
- **核心贡献**: 提出无启发式的视频预训练方法LeVJEPA。
- **创新点**: 利用SIGReg和token dropping实现高效无崩溃训练。
- **结果**: 计算减少5.6-20.8倍，性能匹配或超越V-JEPA 2。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video carries the temporal structure of the physical world, yet learning representations from it has remained computationally expensive: prevailing self-supervised methods either prevent representation collapse through architectural asymmetries, coupling an exponential-moving-average target encoder, a stop-gradient, and a capacity-limited predictor, or circumvent it by reconstructing masked content in pixel space. We introduce LeVJEPA, the first video encoder trained under LeJEPA's collapse-free objective, which dispenses with both. A single encoder is trained with an invariance loss over global and local views of a clip, regularized by SIGReg, which excludes collapse with a provable guarantee. The architecture reduces to an encoder and a projector, and the objective to a single hyperparameter. This formulation admits two properties. First, the cost of pretraining is governed by the number of tokens the encoder observes; uniform random token dropping renders this number small while simultaneously improving downstream accuracy. At matched epochs on identical data, LeVJEPA matches or surpasses V-JEPA 2 across ViT-S/B/L at 5.6 to 20.8x less pretraining compute, and at matched total FLOPs it exceeds the strongest video baseline by 7.6 points on ImageNet-1K while remaining competitive on motion-centric benchmarks. Second, since no asymmetry between branches is required, the encoder can be trained with block-causal attention at no measurable accuracy cost: temporal ordering becomes a property of the encoder itself. Against a compute-matched DINOv2 trained on frames of the same videos, LeVJEPA approaches the image-pretrained encoder on appearance-centric evaluation while nearly doubling its motion-centric accuracy. These results indicate that, once its computational overhead is removed, video becomes a viable and in several respects preferable substrate for general-purpose visual pretraining.

</details>

### 6. FIDA: Feature Instability-Driven Attack on Self-Supervised Facial Representation **⭐⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2608.26861](https://arxiv.org/abs/2608.26861)  · [📄 PDF](https://arxiv.org/pdf/2608.26861)
- **作者**: Zhiyang Chen, Changchun Yin, Huiqin Yang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.CR
- **摘要（中）**: 针对自监督学习模型在后门攻击下的脆弱性，特别是面部表示中身份特征纠缠带来的攻击隐蔽性挑战，提出了FIDA（特征不稳定性驱动攻击）框架。该方法使用微妙语义触发器进行注入，核心创新是特征不稳定性损失，训练编码器增加触发特征沿扰动方向的敏感性，从而避免刚性特征模式以逃避基于扰动的防御。实验表明FIDA实现了高攻击成功率并保持良性效用，对依赖面部分析的多媒体应用构成威胁。
- **摘要（英）**: FIDA introduces a backdoor attack framework for self-supervised facial representations, using subtle semantic triggers and a Feature Instability Loss to increase sensitivity along perturbation directions. This prevents rigid feature patterns, evading perturbation-based defenses. Experiments show high attack success rates while preserving benign utility, posing risks to facial analysis applications.
- **评估**: 该论文揭示了自监督面部表示的安全漏洞，攻击方法有创新性，但领域相关性较低。
- **核心贡献**: 提出FIDA，一种基于特征不稳定性的后门攻击框架。
- **创新点**: 利用特征不稳定性损失增强攻击隐蔽性，逃避防御。
- **结果**: 实现高攻击成功率并保持良性效用。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) models are vulnerable to backdoor attacks. However, the systemic risks they pose in face representation have received little attention. The entanglement of identity features in self-supervised face learning presents unique challenges for attack stealthiness. To address this gap, we propose FIDA (Feature Instability-Driven Attack), a novel backdoor attack framework. FIDA uses subtle semantic triggers for injection, but its key innovation is a novel objective called Feature Instability Loss. It trains the encoder to increase the sensitivity of triggered features along perturbation directions sampled during attack optimization . By preventing the backdoor from exhibiting the rigid feature patterns typical of previous attacks, FIDA effectively evades the evaluated perturbation-based defenses. Experiments show that FIDA achieves a high attack success rate and generally preserves benign utility across the evaluated settings , posing a significant threat to real-world multimedia applications relying on facial analysis.

</details>

### 7. Embedding NDRE Trajectories into Contrastive Learning for Label-Free, Physiology-Aware Crop-Stress Staging and DSS Outputs **⭐⭐** (相关度: 10%, 质量: 0.6)

- **arXiv ID**: [2608.25888](https://arxiv.org/abs/2608.25888)  · [📄 PDF](https://arxiv.org/pdf/2608.25888)
- **作者**: Shafqaat Ahmad
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对作物胁迫检测中传统植被指数阈值或图像聚类无法捕捉胁迫进展的问题，提出EigenCL框架，利用生理引导的对比学习对Sentinel-2 NDRE轨迹进行胁迫分期。该模型在10,000个玉米NDRE块上训练，无需重训练即可迁移到其他地区，产生四个生理一致的胁迫簇，显著优于基线（Silhouette=0.748, DBI=0.35, CHI=49,624），并与玉米生长阶段对齐。
- **摘要（英）**: This paper proposes EigenCL, a physiology-guided contrastive learning framework for crop stress staging from NDRE trajectories, trained on maize patches and tested across regions without retraining. It produces four coherent stress clusters, outperforming baselines with Silhouette=0.748, DBI=0.35, CHI=49,624, and aligning with growth stages.
- **评估**: 该论文专注于农业遥感，与自动驾驶感知领域相关性极低，但对比学习方法有一定通用性。
- **核心贡献**: 提出了EigenCL，一种生理引导的对比学习框架用于作物胁迫分期。
- **创新点**: 利用NDRE轨迹和生理知识引导对比学习，实现可迁移的胁迫诊断。
- **结果**: 在跨区域测试中显著优于基线，并产生生理一致的胁迫簇。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Timely detection of crop stress is critical for sustaining yields under increasing drought frequency, yet conventional vegetation index thresholds or image-based clustering often fail to capture stress progression, limiting their value for farm decision-making. To address this gap, we present EigenCL, a physiology-guided contrastive learning framework that stages crop stress from Sentinel-2 NDRE trajectories, with the goal of providing interpretable and transferable stress diagnostics for decision support systems (DSS). EigenCL was trained on 10,000 maize NDRE patches from drought-affected Iowa fields in 2020 and tested on Nebraska fields in 2023 without retraining, with validation incorporating soil-moisture records, U.S. Drought Monitor maps, and county-level yield statistics. The model produced four physiologically coherent stress clusters (Healthy, Mild, Moderate, Severe), significantly outperforming baselines including K-Means, SimCLR, ProtoCLR, and an ablation model (Silhouette = 0.748, DBI = 0.35, CHI = 49,624). Clusters aligned with maize growth stages, with severe stress peaking around tasseling-silking (VT-R1), a stage known to drive yield loss; moreover, EigenCL clusters correlated with soil moisture at 0-14-day lags (rho up to 0.72) and matched yield anomalies in drought-affected counties. By embedding NDRE trajectory dynamics into contrastive learning, EigenCL enables early stress alerts and interpretable DSS outputs (e.g., heatmaps, scouting priorities, regional risk indices), extending beyond single-date NDRE thresholds and supporting scalable monitoring for climate-smart agronomy.

</details>

### 8. DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.25851](https://arxiv.org/abs/2608.25851)  · [📄 PDF](https://arxiv.org/pdf/2608.25851)
- **作者**: Tuo Chen, Jie Gui, Minjing Dong et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/jsrdcht/DEFUSE](https://github.com/jsrdcht/DEFUSE)
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对自监督学习编码器易受后门攻击且现有防御方法依赖严格假设的问题，提出DEFUSE框架，将后门检测重新表述为表示条件下的图像似然估计问题，由条件扩散生成模型参数化。未感染的表示产生语义一致的重建，而后门表示映射到目标类或无意义图像，从而暴露后门。由于精确似然不可解，该框架将目标放宽为语义重建，无需重训练或OOD暴露，适用于视觉和视觉-语言编码器。
- **摘要（英）**: This paper proposes DEFUSE, a generalizable backdoor defense for SSL encoders, reformulating detection as representation-conditioned likelihood estimation with a conditional diffusion model. It exposes backdoors via semantic inconsistency in reconstructions, relaxing the objective due to intractability, and works across visual and vision-language encoders without restrictive assumptions.
- **评估**: 该论文针对SSL后门防御提出通用框架，方法创新且实验充分，对自动驾驶中自监督模型的安全性有重要参考价值。
- **核心贡献**: 提出了DEFUSE，一种基于生成先验的通用后门检测框架。
- **创新点**: 将后门检测转化为似然估计问题，利用扩散模型的重建语义一致性。
- **结果**: 在多种SSL编码器上有效检测后门，无需重训练或数据访问。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) encoders are vulnerable to backdoor attacks, posing threats to both visual SSL encoders and vision-language encoders. Existing defenses are typically designed for only one of these paradigms and rely on restrictive assumptions such as access to uninfected in-distribution data or precomputed pseudo-labels, which are difficult to satisfy in practice. To address these limitations, we propose DEFUSE, a generalizable backdoor detection framework for SSL encoders. Inspired by Bayesian posterior inference, we reformulate backdoor detection as a representation-conditioned image likelihood estimation problem parameterized by a conditional diffusion generative model. Uninfected representations tend to yield semantically consistent reconstructions, whereas backdoored ones are more likely to be mapped to the attacker's target class or semantically meaningless images, deviating from the original semantics and thereby exposing the backdoor. However, we find that the exact likelihood is intractable, because highly abstracted representations discard the low-level information necessary for pixel-faithful reconstruction. We therefore relax the objective to semantic reconstruction and evaluate it in a well-separated representation space provided by a reference encoder. Rather than training from scratch, we fine-tune a pretrained diffusion model, leveraging its generative prior to map data onto the natural image manifold while preserving semantic content. Extensive experiments demonstrate that DEFUSE substantially outperforms existing detectors across diverse attack settings, generalizing to both visual SSL and vision-language encoders. Notably, our method greatly reduces the reliance on prior knowledge about the victim encoder or the attack strategy. The source code is available at https://github.com/jsrdcht/DEFUSE .

</details>

### 9. ConsensusTAS: Self-Supervised Temporal Action Segmentation for Long-Horizon Construction Videos **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.24043](https://arxiv.org/abs/2608.24043)  · [📄 PDF](https://arxiv.org/pdf/2608.24043)
- **作者**: Xiaoshan Zhou, Yafei Sun
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: 针对长时程施工视频中细粒度活动阶段分割标注耗时的问题，提出无标签自监督方法ConsensusTAS，通过利用候选分割的内部一致性将连续视频流分割为不同活动阶段。在GTEA、Breakfast和Assembly101三个公开数据集上，F1@10分别达到73.08、64.33，F1@50达到33.50，优于现有方法，并在真实施工视频上验证了有效性。
- **摘要（英）**: To address the costly annotation of fine-grained activity boundaries in long construction videos, this paper proposes ConsensusTAS, a label-free self-supervised method that segments continuous streams by exploiting internal consensus of candidate segmentations. It outperforms state-of-the-art on GTEA (F1@10 73.08), Breakfast (F1@10 64.33), and Assembly101 (F1@50 33.50), with validation on real-world construction videos.
- **评估**: 自监督时序分割在特定领域有应用价值，但与自动驾驶感知核心方向关联度有限。
- **核心贡献**: 提出无标签自监督时序动作分割方法，适用于长时程施工视频。
- **创新点**: 利用候选分割内部一致性实现无监督分割。
- **结果**: 在多个公开数据集上超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recognizing sequential construction activities is important for collaborative human-robot work; for example, robots are able to understand workers' current and upcoming actions and provide timely tool delivery or physical support. However, despite extensive research on construction worker activity recognition, existing studies have been limited to classifying activity categories, such as climbing, lifting, and walking, instead of recognizing fine-grained activity transitions from long-horizon sequences. Addressing this problem is challenging because annotating action temporal boundaries in long construction videos is time-consuming. In this study, we propose ConsensusTAS, a label-free, self-supervised learning approach to segment continuous video streams into distinct activity phases by exploiting the internal consensus of candidate segmentations. We evaluated our algorithm on three public datasets, where it outperformed state-of-the-art methods, achieving an F1@10 of 73.08 on GTEA, an F1@10 of 64.33 on Breakfast, and an F1@50 of 33.50 on static-camera videos from Assembly101. We also tested it on real-world construction videos, where post-hoc evaluation showed that the model successfully recognized and segmented actions within the composite activity of bricklaying, such as spreading mortar on a brick, placing the brick, pressing, and aligning. Compared with other temporal action segmentation models that require computationally intensive large vision-language models, our method can run on a CPU, which provides practical value for video surveillance and human-robot collaboration on mobile robotic platforms.

</details>

### 10. SSMB: Self-Supervised Local Feature Detection under Motion Blur **⭐⭐⭐** (相关度: 50%, 质量: 0.65)

- **arXiv ID**: [2608.27181](https://arxiv.org/abs/2608.27181)  · [📄 PDF](https://arxiv.org/pdf/2608.27181)
- **作者**: Zhenjun Zhao, Fabio Bellavia, Wenting Wang et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对运动模糊下关键点检测的挑战，现有方法依赖去模糊或手工关键点，可能引入伪影或假设。②提出了SSMB，一个无需去模糊的自监督关键点检测器，引入局部判别增强（LDE）模块，并通过两阶段训练：几何预训练和模糊感知训练。③相比已有工作，该方法无需手工检测器或外部伪标签，直接从渲染几何和真实模糊对中学习。④在模糊图像上提升了关键点检测的重复性和鲁棒性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses keypoint detection under motion blur by proposing SSMB, a deblur-free self-supervised detector with a Local Discriminability Enhancement module. It uses two-stage training on synthetic shapes and real sharp-blur pairs to learn blur-invariant detection without handcrafted detectors. The method improves repeatability and robustness, though quantitative results are not detailed.
- **评估**: 该论文对鲁棒视觉感知有贡献，与自动驾驶中的低质量图像处理相关。
- **核心贡献**: 提出了SSMB，一个无需去模糊的自监督关键点检测器。
- **创新点**: 通过LDE模块和两阶段训练，实现无外部监督的模糊不变检测。
- **结果**: 在模糊图像上提升了关键点检测的重复性，但具体效果未量化。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Keypoint detection under motion blur remains a significant challenge, as blur distorts local image structure and degrades the repeatability of feature localization. Existing approaches either rely on computationally expensive deblur-then-detect pipelines that may introduce restoration artifacts, or learn to regress the image positions of handcrafted keypoints extracted on sharp images, which reflects the assumptions of the handcrafted detector rather than what is truly repeatable under blur. We present SSMB, a deblur-free, self-supervised keypoint detector for motion-blurred images that requires neither handcrafted detectors nor external pseudo-labels. SSMB introduces the Local Discriminability Enhancement (LDE) module, which restores fine-grained local discriminability after global feature mixing. Training is performed in two stages. First, geometric pretraining on synthetic shapes bootstraps spatially discriminative keypoint detection without any external detector, just from the rendered geometry. Second, blur-aware training on real sharp-blur image pairs learns blur-invariant detection through a multi-component self-supervised objective that enforces cross-domain consistency, geometric alignment, and spatial coverage. Extensive evaluations on keypoint detection, image matching, relative pose estimation, and visual localization under motion blur demonstrate that SSMB establishes a new state-of-the-art among sparse keypoint detectors, consistently outperforming both supervised and self-supervised baselines across all tasks. Code, models, and datasets will be publicly available upon paper acceptance.

</details>

---

## Video Understanding

### 1. LongVU-TTT: Causal Test-Time Training for Visual Resampling in Long Video Understanding **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.25729](https://arxiv.org/abs/2608.25729)  · [📄 PDF](https://arxiv.org/pdf/2608.25729)
- **作者**: Mahmoud Ahmed, Sameh Abdulah, Olatunji Ruwase et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: ①针对长视频多模态大模型在有限视觉token预算下难以建模时间变化的问题。②提出LongVU-TTT，在视觉编码器和LLM之间插入卷积测试时训练（TTT）重采样器，使用因果快速权重更新适应每个视频并上下文化帧特征，同时采用混合均匀和变化感知选择器保留视觉证据。③相比TTT-MLP和双向Mamba2，TTT-Conv在MLVU上分别提升+2.12和+3.04，且优于注意力和固定状态循环重采样器。④处理多达512帧并缩减至128个LLM帧，在五个视频理解基准上取得竞争性能。
- **摘要（英）**: This paper addresses temporal modeling in long-video MLLMs under limited visual-token budgets by inserting a convolutional Test-Time Training resampler with causal fast-weight updates. TTT-Conv improves over TTT-MLP by +2.12 and bidirectional Mamba2 by +3.04 on MLVU, and achieves competitive performance across five benchmarks while processing up to 512 frames.
- **评估**: 该论文创新性地将测试时训练用于视频重采样，提升长视频理解效率，对自动驾驶多相机视频感知有潜在应用。
- **核心贡献**: 提出LongVU-TTT，通过因果TTT重采样器增强长视频理解中的时间建模。
- **创新点**: 在视觉编码器和LLM间插入卷积TTT重采样器，使用快速权重适应视频。
- **结果**: 在MLVU上提升+2.12至+3.04，五个基准上竞争性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-video MLLMs must model temporal change before a limited visual-token budget removes most frame evidence. We introduce LongVU-TTT, which inserts a convolutional Test-Time Training (TTT) resampler with causal fast-weight updates between the vision encoder and the LLM. Its grouped 2D fast weights adapt to each video and contextualize frame features before compression, while a hybrid uniform-and-change-aware selector retains explicit visual evidence for downstream reasoning. Under controlled conditions, TTT-Conv improves over TTT-MLP by up to +2.12 and bidirectional Mamba2 by up to +3.04 on MLVU, and it is stronger than attention- and fixed-state recurrent resamplers across three benchmarks. Analysis shows that the fast weights behave as a temporal aggregation state rather than a reliable long-horizon episodic memory: their benefit attenuates as evidence becomes more distant, motivating explicit frame retention. LongVU-TTT processes up to 512 frames before reducing them to 128 LLM frames and achieves competitive performance across five video understanding benchmarks.

</details>

### 2. Skeleton-based Zero-Shot Spatio-Temporal Action Localization via Weakly-Supervised Pretraining **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.25701](https://arxiv.org/abs/2608.25701)  · [📄 PDF](https://arxiv.org/pdf/2608.25701)
- **作者**: Koshiro Nagano, Fumiaki Sato, Ryo Hachiuma et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: ①针对骨架零样本时空动作定位中，新目标动作训练标注成本高的问题。②提出Skeleton-Language特征池化切换，通过弱监督视觉-语言预训练，从视频级特征聚合切换到推理时的实例级特征计算，无需目标动作训练。③引入场景混合判别对比学习，在MIL框架下区分场景内实例级动作。④在四个公开时空动作定位和分类数据集上验证，有效解决标注限制。
- **摘要（英）**: This paper proposes a weakly-supervised vision-language pretraining strategy for skeleton-based zero-shot spatio-temporal action localization, using pooling kernel switching from video-level to instance-level features. Scene-Mixed Discriminative Contrastive Learning distinguishes actions within scenes, and experiments on four datasets show effectiveness in overcoming annotation limitations.
- **评估**: 该论文解决零样本动作定位的标注问题，方法有创新性，但与自动驾驶感知核心任务相关性一般。
- **核心贡献**: 提出骨架语言特征池化切换和场景混合对比学习，实现零样本时空动作定位。
- **创新点**: 通过弱监督预训练和池化切换，避免目标动作训练。
- **结果**: 在四个数据集上有效解决标注限制。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel pretraining strategy for skeleton-based zero-shot spatio-temporal action localization to estimate unseen actions for person instances while overcoming high annotation costs for training via new target actions and pretraining using large-scale action scenery datasets. Specifically, our approach, termed Skeleton-Language feature Pooling Switching, introduces a weakly-supervised vision-language pretraining mechanism. This mechanism transitions pooling kernels from pretraining, which aggregates skeleton features at the video level and aligns them with each video's known action text embeddings, to the inference phase that computes instance-level features without training via target actions. Furthermore, we propose Scene-Mixed Discriminative Contrastive Learning to distinguish actions at the instance level within the combined scene through the MIL framework. Our experiments on four public spatio-temporal action localization and classification datasets demonstrate that the proposed method effectively addresses annotation limitations.

</details>

### 3. MoTE: Mixture of Task Experts for Multi-Task Video Understanding **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.85)

- **arXiv ID**: [2608.24763](https://arxiv.org/abs/2608.24763)  · [📄 PDF](https://arxiv.org/pdf/2608.24763)
- **作者**: Muhammad Asad Ali, Umar Khan, Nadia Robertini et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对程序性视频语言模型中，密集Transformer解码器共享前馈网络导致任务行为纠缠和扩展困难的问题。②提出了MoTE（Mixture of Task Experts），一种解码器架构，将大语言模型的前馈网络转换为任务特定专家，同时保持多模态骨干共享，每个样本遵循单一样本级任务路由。③相比稀疏MoE的token级路由，MoTE采用任务级路由，更符合程序性目标，且活动专家计算量与存储专家数无关。④在五个COIN基准上，五专家模型激活约2B参数，平均top-1准确率高于近期VideoLLM基线，并优于密集全专家激活和稀疏路由控制。
- **摘要（英）**: This paper addresses the issue of shared feed-forward networks in dense transformer decoders entangling task behavior in procedural video-language models. It proposes MoTE, a decoder architecture that converts LLM feed-forward networks into task-specific experts while keeping the multimodal backbone shared, with each sample following a sample-level task route. Compared to token-level sparse MoE, MoTE aligns with task-level objectives and keeps active computation independent of expert count, achieving higher average top-1 accuracy on five COIN benchmarks with ~2B activated parameters.
- **评估**: 该工作提出了一种任务级专家混合架构，有效解决了多任务视频理解中的任务纠缠问题，性能提升显著，具有较高的研究价值。
- **核心贡献**: 提出MoTE架构，通过任务特定专家转换实现多任务视频理解的高效解耦。
- **创新点**: 采用样本级任务路由，将前馈网络转换为任务专家，保持计算效率。
- **结果**: 在COIN基准上平均top-1准确率优于现有VideoLLM基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Procedural video-language models must solve heterogeneous tasks from the same visual evidence, including action recognition, forecasting, and procedure prediction. Dense transformer decoders share the same feed-forward networks across tasks, which can entangle task behavior and make controlled capability expansion difficult. Sparse Mixture-of-Experts (MoE) decoders provide conditional computation, but token-level learned routing is not naturally aligned with task-level procedural objectives. We propose MoTE (Mixture of Task Experts), a decoder architecture that converts large language model feed-forward networks into task-specific experts while keeping the multimodal backbone shared. Each example follows one sample-level task route, so active task-expert computation remains independent of the number of stored task experts. We instantiate this design as VideoLLM-MoTE and evaluate it on five COIN benchmarks using explicit task routes. The five-expert model activates ~2B LLM parameters per sample and achieves higher average top-1 accuracy than recent VideoLLM baselines. Under the same expert topology, it improves over dense all-expert activation and learned sparse-routing controls. These results show that task-structured routing provides an interpretable and compute-efficient decoder alternative for multi-task video-language learning.

</details>

### 4. Video-OPSD: Exploiting Privileged Visual Evidence for On-Policy Self-Distillation in Video Large Language Models **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2608.27065](https://arxiv.org/abs/2608.27065)  · [📄 PDF](https://arxiv.org/pdf/2608.27065)
- **作者**: Ziyue Wang, Shiqi Huang, Weiwen Xu et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对视频大语言模型（Video-LLMs）中on-policy自蒸馏（OPSD）未被充分探索的问题，现有方法通常通过增加上下文信息来构建特权教师，但忽略了视频本身的时间冗余性。②提出了Video-OPSD框架，利用证据帧作为特权视觉证据，构建证据引导的自教师，并用于知识迁移。③相比已有工作，该方法从主输入中提取特权监督，而非依赖外部信息，使教师提供更聚焦的监督。④在视频推理任务上，该方法通过证据引导提升了监督质量，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the underexplored on-policy self-distillation for Video-LLMs by exploiting privileged visual evidence from long videos. It proposes Video-OPSD, which conditions the teacher on annotated evidence frames while the student reasons over the full video, enabling more informative supervision. The approach improves policy optimization through dense token-level supervision, though specific performance gains are not detailed in the abstract.
- **评估**: 该论文对视频理解领域有重要贡献，方法创新性强，但与自动驾驶感知的直接相关性中等。
- **核心贡献**: 提出了Video-OPSD框架，利用证据帧进行特权自蒸馏，提升Video-LLMs的推理能力。
- **创新点**: 从视频主输入中提取特权视觉证据，而非依赖外部信息，构建更有效的自教师。
- **结果**: 在视频推理任务上提升了监督质量，但具体效果未在摘要中量化。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> On-policy self-distillation (OPSD) has recently emerged as an effective post-training paradigm that improves policy optimization through dense token-level supervision from a privileged self-teacher. Despite its promise, OPSD remains largely underexplored for Video Large Language Models (Video-LLMs). Existing methods typically construct privileged teachers by augmenting their context with additional information while keeping the primary input unchanged for both teacher and student. Video reasoning, however, offers a distinct source of privileged supervision within the primary input itself: long videos contain substantial temporal redundancy, and only a small subset of frames provides the evidence necessary to answer a question. Building on this observation, we present $\textbf{Video-OPSD}$, an OPSD framework that exploits privileged visual evidence for both self-teacher construction and knowledge transfer. First, our Evidence-Grounded Self-Teacher conditions the teacher exclusively on annotated evidence frames while the student continues to reason over the complete video. This focused visual input enables the teacher to provide more informative supervision. Second, our Evidence-Guided Token Optimization adaptively weights token-level distillation according to each reasoning token's reliance on privileged visual evidence, thereby emphasizing perceptually grounded reasoning. Experiments across video understanding and reasoning benchmarks show that $\textbf{Video-OPSD}$ consistently improves upon Standard OPSD across multiple backbones and achieves performance comparable to GRPO while requiring substantially less training time, establishing an effective and efficient post-training approach for Video-LLMs.

</details>

### 5. Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.24293](https://arxiv.org/abs/2608.24293)  · [📄 PDF](https://arxiv.org/pdf/2608.24293)
- **作者**: Yeonkyeong Lee, Hyunsung Go, Jongmin Kim et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: 针对传统VAE在视频数据上固定压缩比无法适应时空内容复杂度的问题，提出KATok，一种基于Transformer的VAE，集成自适应token选择器，根据内容丰富度丢弃无信息token，实现数据依赖压缩。为缓解token丢弃导致的空间错位，提出级联和联合生成两种位置预测策略，在重建和生成质量上达到先进水平。
- **摘要（英）**: To address fixed compression ratios in conventional VAEs for video, KATok introduces a transformer-based VAE with an adaptive token selector that discards uninformative tokens based on content richness, enabling data-dependent compression. It proposes cascaded and joint position-prediction strategies to maintain spatial consistency, achieving strong reconstruction and generation quality.
- **评估**: 视频压缩与生成方向创新，但与自动驾驶感知核心任务关联较弱。
- **核心贡献**: 提出自适应tokenizer的视频VAE，实现紧凑表示。
- **创新点**: 联合学习token选择与位置预测。
- **结果**: 重建和生成质量达到先进水平。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Latent diffusion models have emerged as a dominant framework for high-fidelity image and video synthesis, operating in compact latent spaces with variational autoencoders (VAEs) to enhance computational efficiency without compromising visual quality. However, conventional VAEs are suboptimal for video data as they employ fixed compression ratios that cannot adapt to the varying complexity of spatio-temporal content. We present KATok (Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation), a transformer-based VAE that incorporates an adaptive token selector which is jointly learned with latent tokens. By evaluating each token's content-richness as keep-or-drop probability, the token selector effectively discards uninformative tokens, naturally allowing data-dependent compression. Applying adaptive tokenization to diffusion models may cause spatial misalignment, as token dropping can disturb the original spatio-temporal structure. To alleviate this issue, we propose two position-prediction strategies: cascaded and joint generation, to ensure spatial consistency. We empirically show that our model achieves strong reconstruction and generation quality at a state-of-the-art compression ratio. Further analysis on video data reveals that this improvement is primarily achieved by reducing spatio-temporal redundancy and removing uninformative tokens, as supported by both quantitative and qualitative results.

</details>

### 6. ReGround-Surg: Reliability-Guided Anchor Grounding for Referring Surgical Video Segmentation **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.24671](https://arxiv.org/abs/2608.24671)  · [📄 PDF](https://arxiv.org/pdf/2608.24671)
- **作者**: Jiaxin Wen, Ming Yin, Lu Liu et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/JiaxinWen1/ReGround-Surg](https://github.com/JiaxinWen1/ReGround-Surg)
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: ①针对手术视频中参照分割任务，SAM2两阶段方法对初始锚点质量敏感，错误锚点导致跟踪误差传播。②提出ReGround-Surg，一个轻量级可靠性引导锚点定位框架，预测文本条件空间可靠性图，并用于门控侧适配器和可靠性加权视觉到文本注意力模块。③相比ReSurgSAM2，通过可靠性图增强相关视觉区域并抑制无关信息，提高锚点定位准确性。④实验表明在手术视频分割上性能提升，尤其处理相似器械和遮挡场景。
- **摘要（英）**: This paper proposes ReGround-Surg, a reliability-guided anchor grounding framework for SAM2-based referring surgical video segmentation, using a text-conditioned spatial reliability map to enhance relevant regions and suppress noise. It improves anchor quality and reduces error propagation, showing gains in challenging surgical scenarios.
- **评估**: 该工作针对手术视频分割，与自动驾驶视频理解有一定方法借鉴，但领域差异大。
- **核心贡献**: 提出可靠性引导锚点定位框架，提升SAM2在手术视频参照分割中的鲁棒性。
- **创新点**: 利用空间可靠性图双重增强视觉和文本融合。
- **结果**: 在手术视频分割上取得性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Referring surgical video segmentation requires segmenting a target instrument or tissue region across video frames according to a natural language expression. Recent Segment Anything Model 2 (SAM2) based two-stage methods (e.g., ReSurgSAM2) first ground the referred target in an initial or selected frame, then propagate the selected mask via tracking. Although effective, their performance is highly sensitive to the quality of the initial grounded mask: once an incorrect anchor is selected, subsequent tracking tends to propagate the error. This issue is especially challenging in surgical videos due to visually similar instruments, occlusion, and complex tissue-tool interactions. To address this issue, we propose ReGround-Surg, a lightweight reliability-guided anchor grounding framework to improve SAM2-based referring surgical video segmentation. It first predicts a text-conditioned spatial reliability map from the referring expression and current-frame visual features. The map is then reused in two complementary branches: a Gated Side Adapter enhances expression-relevant visual regions before text-to-vision fusion, while a Reliability-Weighted Vision-to-Text Attention module suppresses off-target visual evidence during prompt-token aggregation. Experiments on Ref-EndoVis17 and Ref-EndoVis18 show consistent improvements over state-of-the-art methods across three evaluation splits with negligible speed reduction. Code is publicly available at https://github.com/JiaxinWen1/ReGround-Surg.

</details>

### 7. RefineRank: Joint Box Refinement and Ranking for Surgical Spatio-Temporal Grounding **⭐⭐⭐** (相关度: 25%, 质量: 0.7)

- **arXiv ID**: [2608.23928](https://arxiv.org/abs/2608.23928)  · [📄 PDF](https://arxiv.org/pdf/2608.23928)
- **作者**: Linzhe Jiang, Jiayuan Huang, Changhao Zhang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/linzhe001/RefineRank](https://github.com/linzhe001/RefineRank)
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对手术时空定位中视觉语言模型坐标不精确和开放集检测器置信度不反映问题答案的问题。②提出RefineRank，结合冻结医学视觉语言模型和开放集检测器，通过紧凑可训练模块RefineNet预测坐标修正和质量分数，固定解码规则选择最高分框。③相比现有方法，在候选框级别融合语言和区域特征，同时进行框修正和排序。④在MedVidBench上取得0.421 STG mIoU，为最高显示分数，全局多指标排名第11，坐标修正提升候选oracle上界。
- **摘要（英）**: This paper introduces RefineRank for surgical spatio-temporal grounding, combining a frozen medical VLM and open-set detector via a compact RefineNet to refine coordinates and rank candidate boxes. It achieves 0.421 STG mIoU on MedVidBench, the highest displayed score, demonstrating effective box-level fusion.
- **评估**: 该工作聚焦手术视频定位，方法结合VLM和检测器有创新，但与自动驾驶感知相关性较低。
- **核心贡献**: 提出RefineRank，在候选框级别融合VLM和开放集检测器，实现框修正与排序。
- **创新点**: 联合预测坐标修正和质量分数，固定解码规则选择最优框。
- **结果**: 在MedVidBench上取得最高STG mIoU。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Surgical spatio-temporal grounding (STG) requires locating, at each video time specified by a procedural question, the object that the question asks about. Existing approaches face a trade-off: vision language models understand the question context but produce imprecise coordinates, whereas open-set detectors provide localized candidate boxes whose confidence does not reflect which box answers the question. We introduce RefineRank, which closes this gap at the candidate-box level. A compact trainable module, RefineNet, combines the language and regional features of a frozen medical vision language model with the proposals of a frozen open-set detector: it predicts a bounded coordinate correction and a quality score for every candidate box, and a fixed decoding rule returns the original or refined box with the highest score. On the MedVidBench Official Rankings (Verified), RefineRank records 0.421 STG mIoU, the highest displayed STG score, while its global multi-metric rank is 11. In a controlled evaluation on separate training and evaluation videos, coordinate correction raises the candidate oracle upper bound from 0.6772 to 0.7302, and ranking the joint pool of original and refined candidates by their RefineNet scores improves STG mIoU from 0.2719 to 0.4534, whereas separately trained selectors over the same pool reach at most 0.4186. These results show that a small box-level module can reconcile question understanding with precise localization without retraining either backbone. Code is available at [https://github.com/linzhe001/RefineRank](https://github.com/linzhe001/RefineRank).

</details>

### 8. Bootstrapping a 4D LiDAR Annotation Tool from Video Foundation Models **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2608.25418](https://arxiv.org/abs/2608.25418)  · [📄 PDF](https://arxiv.org/pdf/2608.25418)
- **作者**: Jihun Kim, Hyun-Kurl Jang, Hyemin Yang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对4D LiDAR分割标注成本高、难以扩展的问题，提出LiDAR-SAM2框架，利用2D视频基础模型SAM2自动生成时间一致的LiDAR级标签，无需人工标注。通过多视角投影和时空聚合生成伪标签，并设计模态接口和两阶段学习目标适配SAM2到LiDAR时空结构。在SemanticKITTI上，仅需少量点即可生成接近人工标注质量的语义和全景标签，训练模型性能接近全标注结果。
- **摘要（英）**: To address the high cost of 4D LiDAR segmentation annotation, LiDAR-SAM2 leverages the video foundation model SAM2 to automatically generate temporally coherent LiDAR labels without human labeling. It uses multi-view projection and spatio-temporal aggregation, with a tailored modality interface and two-stage learning objective. On SemanticKITTI, it achieves near-human annotation quality from few points, with trained models approaching full-supervision performance.
- **评估**: 该工作将视频基础模型成功迁移到4D LiDAR领域，显著降低标注成本，对自动驾驶感知数据生产具有重要价值。
- **核心贡献**: 提出首个无需人工标注即可生成高质量4D LiDAR分割标签的框架。
- **创新点**: 利用视频基础模型SAM2的时空一致性能力，通过多视角投影和两阶段学习适配LiDAR数据。
- **结果**: 在SemanticKITTI上，自动生成的标签接近人工标注质量，训练模型性能接近全监督结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Progress in 4D LiDAR segmentation is bottlenecked by data. Assigning temporally consistent labels across sparse point cloud sequences is costly and hard to scale, and every new task or domain tends to demand fresh dense annotation. This motivates a simple question of whether high-quality LiDAR training data can be produced automatically, without any human labeling. To this end, we introduce LiDAR-SAM2, a framework that turns a 2D video foundation model, SAM2, into a scalable source of supervision for the 4D LiDAR domain. On the data side, it automatically generates temporally coherent LiDAR-level labels from SAM2 video masks through multi-view projection and spatio-temporal aggregation. On the modeling side, a tailored modality interface and a two-stage learning objective adapt SAM2's video segmentation kernel to spatio-temporal LiDAR structure, so that a single click per object yields a consistent mask track across the sequence. Trained with no human LiDAR annotation, LiDAR-SAM2 produces semantic and panoptic labels on SemanticKITTI that approach the quality of full human annotation from only a few points, and models trained on these labels approach the performance of full ground-truth supervision. This positions LiDAR-SAM2 as a scalable labeling tool that substantially reduces the annotation burden for 3D and 4D scene understanding.

</details>

### 9. AdaVDR: Adaptive Tool Use and Reflection for Video Deep Research **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.25559](https://arxiv.org/abs/2608.25559)  · [📄 PDF](https://arxiv.org/pdf/2608.25559)
- **作者**: Xintong Zhang, Xiaomeng Fan, Shilin Yan et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 该论文针对视频深度研究中工具使用策略不当和检索成本高的问题，提出了AdaVDR，一个自适应视频深度研究代理，具备自适应工具调用和反思能力。方法根据任务和能力选择工具，仅在不可靠中间结果时回溯，并开发了数据构建管道，通过事件发现和外部检索生成高质量QA对和工具使用轨迹。该工作提升了视频问答的准确性和效率，但主要面向开放域视频理解，与自动驾驶感知的关联有限。
- **摘要（英）**: This paper addresses inefficient tool use in video deep research, proposing AdaVDR, an adaptive agent with tool invocation and reflection. It selects tools based on task needs and backtracks only when necessary, using a data pipeline to construct QA pairs and trajectories. The method improves accuracy and reduces latency, though its focus on open-domain video limits direct relevance to autonomous driving.
- **评估**: 该论文在视频理解和多模态代理方面有实用贡献，但主题偏离自动驾驶核心感知任务。
- **核心贡献**: 提出了自适应工具调用和反思的视频深度研究代理。
- **创新点**: 基于任务能力选择工具并动态回溯，减少无效交互。
- **结果**: 提升了视频问答的准确性和效率，降低推理错误。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video deep research answers complex questions by jointly understanding video content and retrieving external knowledge from the open Web. However, diverse questions and videos require different tool-use strategies, and inappropriate tool calls can produce incorrect results. Uncertain grounding and retrieval also make unnecessary interactions costly and error-prone, increasing latency and reasoning errors. To address these challenges, we propose AdaVDR, an adaptive video deep research agent with adaptive tool invocation and reflection. AdaVDR selects tools according to the task and its capabilities, and backtracks only when unreliable intermediate results require correction. To enable these capabilities, we develop a video deep research data construction pipeline. We first discover retrieval-relevant events and entities in diverse videos and acquire detailed information through grounding and external retrieval to construct high-quality QA pairs. For each QA, task-specific prompts organize the information acquisition process into a tool-use trajectory, allowing different question and video types to follow different grounding and retrieval strategies. We further introduce model-conditioned tool necessity filtering, which evaluates tool calls against the target model's video understanding and internal knowledge, removing tools or tool chains the model can bypass. This yields trajectories tailored to the target model's video understanding capability and knowledge. Using this pipeline, we construct training data and VDR-EE, a benchmark covering entity-centric and event-centric questions. We perform supervised fine-tuning followed by reinforcement learning with a redundancy-aware reward to strengthen adaptive tool invocation and reflection. Experiments show that our method performs best among the evaluated open-source models on VDR-EE and substantially improves over its base models on VideoDR.

</details>

### 10. Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2608.24885](https://arxiv.org/abs/2608.24885)  · [📄 PDF](https://arxiv.org/pdf/2608.24885)
- **作者**: Sixiang Chen, Jiaming Liu, Jixian Wu et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.RO, cs.CV
- **摘要（中）**: 该论文针对机器人世界模型在动作条件生成中未验证动作跟随假设的问题，提出了WorldEcho诊断基准，覆盖更广动作分布，使用视觉完整性和SE(3)轨迹对齐评估。诊断发现现有世界模型能执行专家动作但难以处理离专家轨迹，要么忽略命令动作要么生成无效视觉结果。进一步提出WorldSync，通过分布覆盖、表征基础和干预效果对齐三个轴增强动作跟随，拓宽训练分布并引入Action-Forcing Expert。该工作对自动驾驶中的世界模型和策略学习有直接价值。
- **摘要（英）**: This paper addresses the unverified action-following assumption in robotic world models, introducing WorldEcho to probe over broader action distributions with visual and trajectory alignment. Diagnosis shows models struggle with off-expert actions, leading to WorldSync, which enhances action following via distribution coverage, grounding, and intervention alignment. The work is directly relevant to autonomous driving world models and policy learning.
- **评估**: 该论文诊断并改进了世界模型的动作跟随能力，对自动驾驶仿真和策略学习有重要启示，实验设计严谨。
- **核心贡献**: 提出了WorldEcho诊断基准和WorldSync对齐方法，提升世界模型动作跟随。
- **创新点**: 从三个互补轴增强动作条件生成，包括分布覆盖和干预对齐。
- **结果**: 诊断显示现有模型在离专家动作上失败，WorldSync显著改善。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Action-conditioned world models are increasingly used as learned simulators for policy evaluation and improvement, yet their effectiveness rests on an unverified assumption: generated futures faithfully reflect arbitrary valid actions. Existing benchmarks are typically confined to expert demonstrations, leaving off-expert action following inadequately evaluated. To address this gap, we introduce WorldEcho, which probes action following over a broader action distribution using visual integrity and SE(3) trajectory alignment. Our diagnosis shows that current world models reasonably execute expert actions but struggle with diverse off-expert trajectories, either ignoring the commanded actions or producing visually invalid rollouts. We further propose WorldSync, which strengthens action following along three complementary axes: distributional coverage, representational grounding, and intervention-effect alignment. It broadens the training distribution over action consequences, grounds intermediate video representations in action-induced robot dynamics through an Action-Forcing Expert, and aligns predicted changes under action interventions with the corresponding changes in ground-truth futures. Experiments on RoboTwin benchmarks and real-robot tasks show that WorldSync improves WorldEcho metrics and serves as a more reliable simulator for iterative policy improvement, enabling policies to achieve higher success rates.

</details>

---

## Object Detection

### 1. Example-based Robust Abnormality Detection with Minimal Annotations using Exemplar Med-DETR **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.24281](https://arxiv.org/abs/2608.24281)  · [📄 PDF](https://arxiv.org/pdf/2608.24281)
- **作者**: Sheethal Bhat, Bogdan Georgescu, Awais Mansoor et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: ①针对医学目标检测中标注需求高、视觉-语言方法因缺乏接地数据难以迁移的问题。②扩展EM-DETR框架，提出可扩展的少样本检测方法，用于胸片异常检测，采用基于示例的特征生成和域感知对比优化。③相比传统少样本学习，无需大量重训练即可适应新疾病发现。④在最小监督下实现高效异常检测，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses annotation reduction in medical object detection by extending EM-DETR with exemplar-based feature generation and domain-aware contrastive optimization for few-shot Chest X-Ray abnormality detection. The method adapts to novel findings without exhaustive retraining, overcoming limitations of vision-language and few-shot learning approaches.
- **评估**: 该论文针对医学检测的少样本问题提出实用方案，但缺乏具体实验结果，与自动驾驶领域相关性较低。
- **核心贡献**: 提出基于示例的少样本医学检测方法，减少标注需求。
- **创新点**: 结合示例特征生成和域感知对比优化，适应新发现。
- **结果**: 在最小监督下实现高效异常检测，但未提供具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reducing annotation requirements remains a key challenge in developing robust medical object detectors. To address this, Vision-Language (VL) object detection methods leverage grounding text information to enable powerful zero-shot and few-shot object detectors in the natural image domain [1, 2, 3, 4]. However, transferring these methods to the medical domain is challenging due to the absence of comparable quality and quantity of the grounding data. Regardless, significant contextual and non-imaging information exists in medical images that remains underutilized. Few-shot learning (FSL) techniques partially address this limitation but struggle to general ize to unseen medical findings and require extensive retraining when new findings are introduced [5, 6]. To overcome these challenges, we extend our prior EM-DETR framework [7] and introduce a scalable FS detection approach designed for efficient abnormality detection in Chest X-Ray (CXR) images under minimal supervision. The proposed architecture incorporates exemplar-based feature generation and domain-aware contrastive optimization, enabling effective adaptation to novel disease findings without exhaustive retraining. Our method achieves near state-of-the-art (SOTA) detection performance using less than 10% of the annotated data, demonstrating its potential for practical, annotation-efficient clinical deployment across both proprietary and public CXR datasets.

</details>

### 2. TADP: Task-Aware Deformable Prediction for Single-Stage 3D Object Detection **⭐⭐⭐** (相关度: 85%, 质量: 0.7)

- **arXiv ID**: [2608.27282](https://arxiv.org/abs/2608.27282)  · [📄 PDF](https://arxiv.org/pdf/2608.27282)
- **作者**: Su Wang, Yaochen Li, Min Yang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AI, cs.RO
- **摘要（中）**: 针对单阶段3D检测器使用相同特征完成不同任务导致特征空间不适配的问题，提出了任务感知形变预测（TADP）方法。该方法设计了三重特征细化聚合模块提取三级特征，多尺度特征聚合块以尺度感知方式融合特征，并引入即插即用的任务感知形变头，感知各任务的重点和交互。相比现有方法，TADP通过形变预测适应任务差异，在KITTI数据集上汽车mAP达到80.91%，超越许多先进方法。
- **摘要（英）**: TADP addresses the feature mismatch in single-stage 3D detection by introducing a task-aware deformable prediction method with triple feature refinement and multi-scale aggregation. The plug-and-play deformation head adapts predictions to task-specific emphasis and interaction. On KITTI, it achieves 80.91% car mAP, surpassing many state-of-the-art methods.
- **评估**: 该论文针对单阶段3D检测的任务适配问题提出了有效方案，实验结果有竞争力。
- **核心贡献**: 提出TADP，通过任务感知形变预测提升单阶段3D检测性能。
- **创新点**: 设计即插即用的任务感知形变头，动态调整预测以适应任务差异。
- **结果**: 在KITTI上汽车mAP达80.91%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most single-stage 3D object detectors complete different tasks with the same extracted features. Nevertheless, it is impossible to project features into a common space that is adaptive for all the tasks. We present a novel task-aware deformable prediction (TADP) method for single-stage 3D object detection to solve this problem. Firstly, a triple feature refinement aggregation module is designed to extract three-level features adaptively. Additionally, we design the multi-scale feature aggregation block to fuse multi-scale features in a scale-aware manner. Finally, the prediction of each task is deformed with the designed plug-and-play task-aware deformation head. It can percept the emphasis and interaction of each task. We also designed three different deformation modules. The experimental results demonstrate that the proposed deformation head shows good results on other detection methods. The experimental results on the KITTI dataset demonstrate that the car mAP is 80.91%, surpassing many state-of-the-art methods on the KITTI benchmark.

</details>

### 3. Socialized Detector Learning: Trajectory-Guided and Reciprocal Distillation for Heterogeneous Object Detectors **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2608.25836](https://arxiv.org/abs/2608.25836)  · [📄 PDF](https://arxiv.org/pdf/2608.25836)
- **作者**: Weihao Li, Yunqi Zhu, Zhihe Fan et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对异构目标检测器知识碎片化、聚合式社会化学习缺乏迁移顺序规划的问题，提出社会化检测器学习（SDL）和轨迹引导互蒸馏（TGRD）。TGRD通过特征对齐残差估计检测器间迁移难度，预计算分数表并贪心构建载体轨迹，沿轨迹将知识逐步整合到联合类别载体，再通过互蒸馏回传专家。条件代理证书分析表明渐进式证书不大于聚合目标，在MS COCO上验证了有效性。
- **摘要（英）**: To address fragmented knowledge across heterogeneous detectors and lack of transfer order planning in aggregation-based socialization, SDL and TGRD estimate inter-detector transfer difficulty from feature-alignment residuals, construct a carrier trajectory greedily, and progressively consolidate knowledge into a union-category carrier with reciprocal transfer. Conditional proxy-certificate analysis shows the progressive certificate is no larger than aggregated targets, with validation on MS COCO.
- **评估**: 该工作为异构检测器知识融合提供了有序迁移的新范式，理论分析与实验结合紧密。
- **核心贡献**: 提出轨迹引导的互蒸馏方法，实现异构检测器知识有序整合。
- **创新点**: 用迁移难度估计和贪心轨迹构建替代单向蒸馏。
- **结果**: 在MS COCO上验证了渐进式蒸馏的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection knowledge is fragmented across independently trained, heterogeneous detectors with complementary category supports. In socialized learning, this knowledge resides in a society, and learning aims to evolve the society collectively through exchange. However, aggregation-based socialization does not explicitly plan transfer order, whereas progressive multi-teacher distillation considers order but remains a one-way student enhancement in a shared category space. Building on Socialized Learning, we formulate Socialized Detector Learning (SDL) for heterogeneous, category-specialized object detectors and propose Trajectory-Guided and Reciprocal Distillation (TGRD).TGRD estimates directed operational Inter-Detector Transfer Difficulty (IDTD) from held-out feature-alignment residuals, precomputes a fixed score table, and greedily constructs a carrier trajectory. Along the trajectory, knowledge is progressively consolidated into a union-category carrier and then returned to experts through reciprocal transfer. A conditional proxy-certificate analysis shows that, under stated assumptions, the progressive certificate is no larger than an aggregated-target counterpart. On MS COCO with four heterogeneous experts and two carrier initializations, final carriers outperform epoch-matched simultaneous aggregation controls by 2.6 AP in both settings. Reciprocal detectors attain 20.8--28.4 AP on previously unsupported categories while remaining within 1.3 AP of original expert-specific performance. These results support order-aware progressive consolidation followed by reciprocal transfer as a viable mechanism for detector-society evolution.

</details>

### 4. Rethinking Pre-Training and Augmentation for Zero-Shot Cross-City Object Detection **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.24154](https://arxiv.org/abs/2608.24154)  · [📄 PDF](https://arxiv.org/pdf/2608.24154)
- **作者**: Long Hoang Pham, Quoc Pham-Nam Ho, Huy-Hung Nguyen et al. (13 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/SKKUAutoLab/aic26_cross_city](https://github.com/SKKUAutoLab/aic26_cross_city)
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对跨城市目标检测中地理域偏移和隐私限制下无法使用目标域数据的问题，提出模块化训练流水线，包含多数据集预训练策略（类无关目标性蒸馏解耦车辆几何与语义）和域鲁棒增强流（Grayworld变换去除颜色捷径，强化形状先验）。在RF-DETR上评估，桥接跨城市分布差距且仅需16GB GPU内存，优化变体进一步提升了性能。
- **摘要（英）**: To address geographic domain shift in cross-city detection under privacy constraints, a modular pipeline is proposed with multi-dataset pre-training using class-agnostic objectness distillation and a domain-resilient augmentation stream with Grayworld transformation. Evaluated on RF-DETR, it bridges cross-city gaps with limited GPU memory, and optimized variants improve performance.
- **评估**: 该工作针对隐私敏感场景的零样本跨城市检测提供了实用且高效的解决方案。
- **核心贡献**: 提出模块化训练流水线，结合预训练和增强解决跨城市域偏移。
- **创新点**: Grayworld变换和类无关蒸馏解耦几何与语义。
- **结果**: 在RF-DETR上桥接分布差距，仅需16GB内存。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world deployment of traffic surveillance systems is bottlenecked by geographic domain shift, in which models trained in one city underperform when applied to an unseen target city. Conventional domain adaptation relies on hyperparameter-sensitive architectures or direct profiling of target data. Both are fundamentally precluded in privacy-conscious ecosystems that require completely blind training and evaluation loops. In this setting, we explore the effects of pre-training and augmentation in addressing the domain shift problem. Specifically, we propose a new modular training pipeline for object detection structured around two core orthogonal pillars: (1) a multi-dataset pre-training strategy featuring a class-agnostic objectness distillation to decouple structural vehicle geometry from semantic taxonomies, and (2) a domain-resilient augmentation stream featuring a novel Grayworld transformation that forces global attention heads to strip volatile chromatic shortcuts in favor of robust shape priors. When evaluated with the real-time transformer-based detector RF-DETR, our framework bridges cross-city distribution gaps while using limited GPU memory (16GB). Our optimized variants, RF-DETR-HR and RF-DETR-Grayworld, deliver a substantial empirical gain of +24.29 over the baseline, achieving 1st place (47.53 mAP) on the AI City Challenge Track 6 leaderboard. Code and data are available at: \href{https://github.com/SKKUAutoLab/aic26_cross_city}{SKKUAutoLab/aic26\_cross\_city}.

</details>

### 5. ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection **⭐⭐** (相关度: 75%, 质量: 0.6)

- **arXiv ID**: [2608.23923](https://arxiv.org/abs/2608.23923)  · [📄 PDF](https://arxiv.org/pdf/2608.23923)
- **作者**: Rashid Riyadh, Abd Ullah Khan, Imad Gohar et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: 针对SAHI在背景块上计算浪费的问题，提出ROI-Gated SAHI，引入轻量级提议器定位前景区域并限制切片细化。在COCO128上静态门控平均速度比Full SAHI慢（0.88x），mAP@0.5更低（0.6602 vs 0.7569）；自适应路由策略（τ=0.4）降低延迟，速度提升1.02x。在三图像稀疏场景中，加速比0.96x至6.90x，平均3.41x，表明ROI门控在稀疏场景最有效。
- **摘要（英）**: To reduce compute waste on background tiles in SAHI, ROI-Gated SAHI introduces a lightweight proposer to restrict sliced refinement. On COCO128, static gating is slower with lower mAP, while adaptive routing achieves slight speedup; in sparse scenes, speedups range from 0.96x to 6.90x, showing effectiveness in sparse scenarios.
- **评估**: 该工作针对小目标检测推理优化有实用价值，但性能提升有限且依赖场景稀疏度。
- **核心贡献**: 提出ROI门控的SAHI推理框架，减少背景计算。
- **创新点**: 用轻量级提议器实现内容自适应切片。
- **结果**: 在稀疏场景平均加速3.41x，但密集场景无优势。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Slicing-Aided Hyper Inference (SAHI) improves small object detection in high-resolution images but often spends substantial compute on background tiles. We propose region-of-interest (ROI)-Gated SAHI, an inference-time framework that introduces a lightweight proposer to localize foreground regions and restrict sliced refinement to informative areas. We evaluate the framework in two settings. On the COCO128 full split dataset comprising 128 images, static ROI-gating is slower on average than Full SAHI, achieving a speed ratio of 0.88, and yields a lower mAP@0.5 of 0.6602 compared with 0.7569 for Full SAHI. A simple adaptive routing policy with $τ=$ 0.4 educes the mean latency, achieving a slight gain of 1.02$\times$ over Full SAHI. On a three-image sparse-to-dense case study, ROI-gating achieves speedups ranging from 0.96$\times$ to 6.90$\times$ with a mean speedup of 3.41$\times$. These results show that ROI-gating is most beneficial in sparse scenes and requires policy-based routing for robust average behavior.

</details>

### 6. TDFNet: Tri-projection Deformable Fusion Network for Panoramic Salient Object Detection **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.25808](https://arxiv.org/abs/2608.25808)  · [📄 PDF](https://arxiv.org/pdf/2608.25808)
- **作者**: Qiangqiang Zhou, Jiacong Yu, Jiawei Xu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对全景显著目标检测中球面投影到2D平面引入几何畸变的问题，提出TDFNet，首个三投影可变形融合网络，利用互补投影表示缓解畸变。设计跨投影可变形注意力模块，利用投影间空间对应构造几何感知采样位置，增强跨投影上下文聚合和抗畸变能力。
- **摘要（英）**: To address geometric distortions in panoramic salient object detection, TDFNet is the first tri-projection deformable fusion network, using complementary projections to alleviate distortions. A cross-projection deformable attention module leverages spatial correspondences for geometry-aware sampling, enhancing robustness.
- **评估**: 全景检测方向有创新，但与自动驾驶核心感知任务相关性一般。
- **核心贡献**: 提出三投影可变形融合网络用于全景显著目标检测。
- **创新点**: 跨投影可变形注意力机制。
- **结果**: 缓解投影畸变，提升检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed the growing potential of panoramic salient object detection in robotic vision, virtual reality, and related applications. However, projecting spherical scenes onto 2D planes inevitably introduces geometric distortions, which fundamentally limit the effectiveness of existing projection-based methods. Specifically, Equirectangular Projection (ERP) suffers from severe polar stretching distortions, while cube map projection introduces discontinuities across cube-face boundaries, resulting in degraded feature discriminability and compromised geometric consistency. To address these limitations, we propose TDFNet, the first Tri-projection Deformable Fusion Network for panoramic salient object detection, exploiting complementary projection representations to alleviate geometric distortions and improve detection performance.Specifically, we design a cross-projection deformable attention (CDA) module that leverages spatial correspondences between different projections to construct geometry-aware sampling locations, guiding deformable attention for cross-projection contextual aggregation and enhancing robustness against projection-induced deformations. Furthermore, we introduce a latitude-guided fusion module, which utilizes spherical latitude priors to construct geometric confidence weights for adaptively balancing ERP and CMP features. Meanwhile, LGF incorporates distortion-reduced semantic references from Tangent Projection to achieve cross-projection feature refinement and spatial alignment.By constructing a three-branch encoding architecture based on ERP, CMP, and Tangent Projection, TDFNet simultaneously preserves global spatial continuity, local geometric details, and fine-grained boundary information.

</details>

### 7. MIMONet: Multi-scale Input and Multi-scale Output Network for Salient Object Detection **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.25733](https://arxiv.org/abs/2608.25733)  · [📄 PDF](https://arxiv.org/pdf/2608.25733)
- **作者**: Zhaojian Yao, Wei Gao, Tiesong Zhao et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对现有显著目标检测方法输入单尺寸图像难以学习目标尺寸变化知识的问题，提出MIMONet，采用多尺度输入和多尺度输出网络，通过图像金字塔提取三个不同分辨率图像的多级特征形成三个编码器分支并交换信息，使分支学习尺寸变化知识。设计多尺度感知模块，将输入特征层分为不同分辨率子层，增强多尺度目标检测能力。
- **摘要（英）**: To address the difficulty of learning object-scale variations with single-size inputs, MIMONet proposes a multi-scale input and multi-scale output network, using an image pyramid with three encoder branches exchanging information. A multi-scale perception module divides feature layers into sub-layers of different resolutions, improving multi-scale object detection.
- **评估**: 多尺度检测方法有通用价值，但创新性一般，与自动驾驶关联度中等。
- **核心贡献**: 提出多尺度输入输出网络用于显著目标检测。
- **创新点**: 多分支信息交换学习尺寸变化。
- **结果**: 提升多尺度目标识别能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The existing methods for saliency detection task focus on the application of multi-level features, aiming to take advantage of the respective strengths of high- and low-level features. However, because the inputs of these models are single-size images, their multi-level features have difficulty in learning the knowledge of size variations of salient objects. Object-scale variation learning has great potential for detecting multi-scale objects, which has not been fully explored by existing methods. To improve the recognition ability of a model for objects with different sizes, we are inspired by the image pyramid to propose a Multi-scale Input and Multi-scale Output Network (MIMONet). In MIMONet, we extract multi-level features for three images with different resolutions to form three encoder branches, and information will be exchanged between the branches. The advantage of this approach is that the features of one branch can learn the knowledge of target size variation from the features of the other two branches. In addition, we design a Multi-scale Perception (MSP) module, in which the input feature layer is divided into several sub-layers with different resolutions. Capturing the multi-level structure information of the objects in these sub-layers can make the objects more fully perceived. For network training, we propose a Joint Saliency Loss (JSL), which can constrain multiple saliency maps output by the network to identify the same foreground objects, and induce their boundaries to be preserved clearly. Experimental results show that MIMONet has stronger detection capabilities and harvests better evaluation scores on multiple datasets compared to existing models. The code of our model will be released.

</details>

### 8. Automatic weld seam segmentation for industrial quality control: a comparison of RGB and polarimetric imaging with CNN and transformer architectures **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2608.25465](https://arxiv.org/abs/2608.25465)  · [📄 PDF](https://arxiv.org/pdf/2608.25465)
- **作者**: Simone Garbin, Leonardo Venturoso, Marco Todescato
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对工业质量控制中焊缝分割自动化程度低、依赖人工且存在操作员间差异的问题。②评估基于RGB和偏振成像的自动焊缝分割，比较CNN和Transformer架构，在受控实验室和真实非受控条件下，采用统一阈值无关协议，每个CNN用三个随机种子训练。③发现采集设置是系统的一阶组件：受控RGB下CNN mAP50达0.87，非受控下降至0.22-0.48；偏振成像配合对齐保持几何增强可定位未见焊缝，mAP50达0.93。④偏振成像性能与最佳控制相当，但未超越。
- **摘要（英）**: This paper evaluates automatic weld seam segmentation from RGB and polarimetric imagery in industrial quality control, comparing CNN and transformer architectures under controlled and uncontrolled conditions. It finds that acquisition setup is a first-order factor: CNN mAP50 drops from 0.87 in controlled RGB to 0.22-0.48 uncontrolled, while polarimetric imaging with alignment-preserving augmentation reaches mAP50 0.93, on par with the best control. The study highlights the importance of imaging conditions over architecture choice.
- **评估**: 工业应用导向的实证比较，与自动驾驶感知关联度低，但方法对比有参考价值。
- **核心贡献**: 系统比较RGB和偏振成像在焊缝分割中的性能，揭示采集条件的关键作用。
- **创新点**: 引入偏振成像和几何增强提升非受控条件下的分割鲁棒性。
- **结果**: 偏振成像在非受控条件下mAP50达0.93，与最佳控制相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual inspection of welded assemblies remains one of the least automated stages in many industrial production processes, still depending largely on the experience of human operators and thus subject to inter-operator variability; the manufacturing of special-purpose machinery cabins, the setting of this study, is one representative case. This work evaluates the feasibility of automatic weld seam segmentation from RGB and polarimetric imagery, comparing controlled laboratory acquisitions with images captured under real, uncontrolled conditions. Convolutional neural network (CNN) architectures and transformer-based architectures are benchmarked under a unified, threshold-independent protocol, training each CNN with three random seeds to separate genuine effects from seed noise. In controlled RGB conditions, CNN models reach a mean mask mAP50 of up to 0.87, but drop to 0.22-0.48 under uncontrolled acquisition, showing that the acquisition setup is a first-order component of the inspection system. Polarimetric imaging with alignment-preserving geometric augmentation localizes previously unseen welds with a mean mask mAP50 up to 0.93: on par with, rather than ahead of, the best controlled-RGB result, but reaching that accuracy on uncontrolled RGB without requiring acquisition control. The clearest architectural finding concerns viewpoint robustness. In-distribution, transformers and CNNs are broadly comparable; but under a test-time viewpoint shift, the transformer models, and RF-DETR in particular, retain high accuracy while every CNN collapses. The gap holds across three seeds and a resolution-matched control, pointing to architecture rather than training resolution. Within the CNN family, capacity brings no reliable in-distribution gain once seed variance is accounted for: small CNNs suffice for fixed viewpoints, transformers for variable ones.

</details>

### 9. Lowering the Barrier to AI-Driven Inspection: A No-Code Workflow for Automated Structural Defect Detection **⭐⭐** (相关度: 30%, 质量: 0.5)

- **arXiv ID**: [2608.25176](https://arxiv.org/abs/2608.25176)  · [📄 PDF](https://arxiv.org/pdf/2608.25176)
- **作者**: Michael Holm, Tanner McElroy, Xinghang Zhang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.LG, eess.IV
- **摘要（中）**: ①针对结构缺陷检测中传统视觉方法对噪声敏感、深度学习应用需要编程技能导致采用率低的问题。②提出了YOLOEZ，一个基于GUI的无代码工具，集成数据标注、训练和推理于一体，支持YOLO模型的端到端应用。③相比现有软件，降低了技术门槛，使非专家也能开发高性能模型，并支持可复现的工作流。④评估显示其性能优于现有软件，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the technical barriers in adopting deep learning for structural defect detection by introducing YOLOEZ, a GUI-based no-code tool that integrates data labeling, training, and inference. It lowers the entry barrier for non-experts while supporting reproducible workflows. Evaluation shows improved performance over existing software, though specific metrics are not provided in the abstract.
- **评估**: 该工具对工程应用有实用价值，但创新性和技术深度有限，与自动驾驶感知领域相关性较低。
- **核心贡献**: 提出了一个无代码的YOLO模型应用工具，简化了结构缺陷检测流程。
- **创新点**: 将数据标注、训练和推理集成到单一GUI界面，无需编程。
- **结果**: 在结构缺陷检测中性能优于现有软件。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structural health monitoring (SHM) is essential in modern engineering, providing data for condition-based maintenance, lifecycle assessment, and predictive decision-making. Traditionally, SHM relied on visual inspection to detect defects such as cracks and deformations. Early computer vision (CV) methods, including thresholding, edge detection, and handcrafted features, aimed to automate this process but were highly sensitive to noise, imaging variations, and multiscale defects, limiting their reliability. Recent advances in machine learning, particularly convolutional neural networks (CNNs) and You Only Look Once (YOLO), have improved defect detection accuracy and enabled real-time analysis. However, adoption in SHM remains limited due to technical barriers such as data labeling, model training, and deployment, which typically require programming expertise. To address this gap, we introduce YOLOEZ, an open-source, GUI-based tool for end-to-end YOLO model application. YOLOEZ integrates data labeling, training, and inference into a single interface, enabling high-performance model development without code while supporting reproducible workflows. Evaluation against existing software and classical image processing demonstrates that YOLOEZ not only outperforms traditional methods across most detection metrics, but also lowers adoption barriers present in other modern CV tools. By combining accuracy with accessibility, YOLOEZ facilitates wider use of AI-driven monitoring for predictive maintenance, digital twins, and intelligent structural systems.

</details>

### 10. Decoupling candidate dual AGN from chance superpositions in the GOTHIC survey via a deep-learning framework **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.24164](https://arxiv.org/abs/2608.24164)  · [📄 PDF](https://arxiv.org/pdf/2608.24164)
- **作者**: Bhavesh Mukheja, Snehanshu Saha, Anwesh Bhattacharya et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: astro-ph.GA, cs.CV, cs.LG
- **摘要（中）**: ①针对双活动星系核（DAGN）候选体在成像巡天中因投影效应和空间分辨率限制难以与前景恒星等偶然叠加区分的问题。②使用基于YOLOv11定向边界框架构的监督深度学习框架，在标注的SDSS图像上训练，以分离真实双核与前景恒星污染。③相比传统方法，利用深度学习自动识别，提高了检测精度和效率。④最终模型对双核类别的验证精度为0.919，召回率0.905，F1为0.912，识别出29,605个双核候选体，其中54.5%-62%与真实双核一致。
- **摘要（英）**: This paper addresses the challenge of distinguishing dual active galactic nuclei from chance superpositions in imaging surveys using a YOLOv11-based oriented-bounding-box deep learning framework. It achieves high precision and recall for the dual-nuclei class, identifying thousands of candidates. The method significantly improves automated detection efficiency compared to traditional approaches.
- **评估**: 该研究在天文学领域有应用价值，但方法基于现有YOLO架构，创新性一般，与自动驾驶感知相关性低。
- **核心贡献**: 将YOLOv11应用于天文图像中的双核星系检测，有效分离真实双核与偶然叠加。
- **创新点**: 采用定向边界框的YOLOv11架构处理天文图像中的目标检测。
- **结果**: 验证精度0.919，召回率0.905，F1为0.912。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dual active galactic nuclei (DAGN) mark a critical phase in the evolution of merging galaxies and the pairing of supermassive black holes, yet they remain difficult to identify in large imaging surveys because of projection effects and limited spatial resolution. Compact foreground stars and unresolved substructure can mimic dual nuclei through chance superposition, complicating automated detection. We revisit the 46,061 galaxies flagged but rejected as DAGN candidates by the GOTHIC pipeline, primarily because the two nuclei fell within the SDSS fibre aperture or exceeded its separation threshold. We train a supervised deep-learning framework based on the YOLOv11 oriented-bounding-box architecture on annotated SDSS imaging to separate genuine dual nuclei from foreground stellar contaminants and other spurious alignments. The final model attains a validation precision of 0.919, recall of 0.905, and $F_1$ of 0.912 for the dual-nuclei class, and yields 29,605 dual-nucleus candidates after removing star-dominated and blended detections. Structured visual inspection indicates that $54.5$--$62\%$ are consistent with genuine dual nuclei, implying $\sim(1.4$--$1.8)\times10^{4}$ plausible systems. Cross-calibrating the YOLO separation against the deterministic GOTHIC centroid measurement and restricting to the compact regime ($d \le 6.87''$) gives a conservative subset of $\sim 13{,}672$ candidates, reaching calibrated separations of $\sim 0.56''$. Spectroscopy of the most compact ($\le 1$~kpc) systems shows they are dominated by passive, absorption-line galaxies with no resolved double-peaked emission, so confirmation requires higher-resolution follow-up. The catalogue is a statistically refined list of candidates, not confirmed DAGN. Nonetheless, deep-learning detection substantially reduces contamination and expands the plausible DAGN census.

</details>

---

## Multimodal

### 1. UniGeo: A Multi-modal Large Language Model for Text-Guided Cross-View Geo-Localization **⭐⭐⭐** (相关度: 60%, 质量: 0.6)

- **arXiv ID**: [2608.26722](https://arxiv.org/abs/2608.26722)  · [📄 PDF](https://arxiv.org/pdf/2608.26722)
- **作者**: Jiahao Wen, Hang Yu, Zhedong Zheng
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 针对文本引导的无人机地理定位中，不完整查询和高度相似候选图像导致全局跨模态匹配不足的问题，提出了UniGeo，一个统一的多模态大语言模型。该方法通过地理语义学习建立局部场景元素、空间关系与语言描述之间的稳定对应，并通过跨视角生成建模无人机与卫星视角间的语义映射，最后利用即插即用的验证模块对高混淆候选进行细粒度判别。相比现有直接匹配方法，UniGeo联合支持地理语义理解、跨视角生成和候选级验证，并采用多阶段训练策略。摘要未提供具体定量结果，但展示了在跨视角定位任务上的潜力。
- **摘要（英）**: UniGeo addresses text-guided drone geo-localization by proposing a unified multimodal LLM that jointly performs geo-semantic understanding, cross-view generation, and candidate-level verification. It establishes stable correspondences between scene elements and language, and models drone-satellite semantic mappings, improving fine-grained localization over direct matching. The multi-stage training strategy progressively enhances these capabilities, though specific quantitative results are not detailed in the abstract.
- **评估**: 该论文将多模态大语言模型引入跨视角地理定位，方法新颖，但摘要缺乏实验数据，实际效果待验证。
- **核心贡献**: 提出UniGeo，首个统一MLLM框架联合支持地理语义理解、跨视角生成和候选验证。
- **创新点**: 通过多任务联合学习和多阶段训练实现跨视角语义映射与细粒度判别。
- **结果**: 摘要未提供具体数据，但展示了在文本引导地理定位上的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-guided drone geo-localization aims to identify a target region in a large-scale image gallery from a natural-language description. Existing methods mainly formulate this task as direct matching between an open-ended text query and candidate images. However, incomplete queries and highly similar candidates often make global cross-modal matching insufficient for reliable fine-grained localization. We propose UniGeo, a unified multimodal large language model (MLLM) for text-guided drone geo-localization. Built on a shared vision-language framework, UniGeo jointly supports geo-semantic understanding, cross-view semantic generation, and candidate-level verification. Specifically, it establishes stable correspondences among local scene elements, spatial relations, and language descriptions through geo-semantic learning, and further models semantic mappings between drone and satellite views through cross-view generation. Based on these capabilities, a plug-and-play verification module performs fine-grained discrimination among highly confusable candidates. We further introduce a multi-stage training strategy that progressively learns geo-semantic understanding, cross-view generation, and candidate verification, improving adaptation to text-guided geo-localization. Experiments demonstrate consistent improvements across multiple retrieval backbones. On GeoText-1652, UniGeo improves R@10 and mAP by 13.59 and 2.83 percentage points, respectively, validating its effectiveness for fine-grained text-guided drone geo-localization.

</details>

### 2. CODE: Cross-Modal Calibration and Dynamic Suppression for Open World Object Detection **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2608.27214](https://arxiv.org/abs/2608.27214)  · [📄 PDF](https://arxiv.org/pdf/2608.27214)
- **作者**: Hao Xu, Zhaoning Shi, Hehe Jin et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 针对开放世界目标检测中多模态基础模型因单向文本到视觉匹配导致的语义模糊，以及刚性异常惩罚过度抑制已知类边界附近未知对象的问题，提出了CODE框架。该方法包含三个互补组件：跨模态联合置信度校准注入全局视觉原型校准文本驱动的已知类预测，不确定性引导的通用目标性增强利用局部视觉响应强化潜在未知对象，动态异常抑制通过置信度边际调整保留模糊分布外实例。在Real-World Detection基准上，使用OWL-ViT L/14骨干，CODE在任务1中达到21.7 U-mAP和40.8 K-mAP，分别超过先前最先进方法2.6和2.3点。
- **摘要（英）**: CODE addresses open-world object detection by proposing a unified inference-time framework with cross-modal calibration, uncertainty-guided objectness enhancement, and dynamic outlier suppression. It injects global visual prototypes to calibrate text-driven predictions and uses confidence margins to preserve ambiguous unknown objects. On the Real-World Detection benchmark with OWL-ViT L/14, CODE achieves 21.7 U-mAP and 40.8 K-mAP in Task 1, surpassing prior SOTA by 2.6 and 2.3 points.
- **评估**: 该论文针对开放世界检测的语义模糊和过度抑制问题提出了有效解决方案，实验提升显著。
- **核心贡献**: 提出CODE，通过跨模态校准和动态抑制提升开放世界检测性能。
- **创新点**: 结合全局原型校准和置信度边际调整，平衡已知与未知类检测。
- **结果**: 在Real-World Detection上U-mAP和K-mAP分别提升2.6和2.3点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open World Object Detection (OWOD) built on multimodal foundation models often suffers from semantic ambiguity caused by unidirectional text-to-vision matching, while rigid outlier penalties may over-suppress unknown objects near known-class decision boundaries. We propose CODE (Cross-Modal Calibration and Dynamic Suppression), a unified inference-time framework with three complementary components. Cross-Modal Joint Confidence Calibration injects global visual prototypes to calibrate text-driven known-class predictions. Uncertainty-Guided Universal Objectness Enhancement measures classification hesitation from local visual responses to strengthen potential unknown objects. Dynamic Outlier Suppression via Confidence Margin replaces rigid suppression with a margin-aware adjustment that preserves ambiguous out-of-distribution instances. Experiments on the Real-World Detection benchmark demonstrate that, with the OWL-ViT L/14 backbone, CODE achieves 21.7 U-mAP and 40.8 K-mAP in Task 1, surpassing the previous state of the art by 2.6 and 2.3 points, respectively.

</details>

### 3. How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space **⭐⭐** (相关度: 20%, 质量: 0.4)

- **arXiv ID**: [2608.27121](https://arxiv.org/abs/2608.27121)  · [📄 PDF](https://arxiv.org/pdf/2608.27121)
- **作者**: Corey D. C. Heath
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.MM, cs.CV, cs.LG
- **摘要（中）**: ①针对AI模型如何在没有显式标签或跨模态监督的情况下，自主形成对艺术作品的审美分类这一问题。②提出了一个自监督框架，将文本、音频、图像和视频四种模态投影到共享的256维嵌入空间，并应用迭代聚类来发现审美结构。③相比已有工作，该工作探索了AI与人类情感标签的差异，而非依赖人工标注。④在弱监督多模态数据集上，展示了AI聚类与人类情感标签的差异，但未提供定量性能数据。
- **摘要（英）**: This paper addresses how AI models autonomously form aesthetic categorizations of artistic media without explicit labels or cross-modal supervision. It proposes a self-supervised framework projecting four modalities into a shared embedding space with iterative clustering to discover aesthetic structure. The work diverges from human affective labels and has applications in organizing media collections, though quantitative results are limited.
- **评估**: 该论文与自动驾驶感知领域相关性极低，主要关注艺术审美，但自监督多模态嵌入方法有一定参考价值。
- **核心贡献**: 提出了一个自监督多模态框架，用于发现AI对艺术的审美结构。
- **创新点**: 利用迭代聚类在共享嵌入空间中无监督地发现跨模态审美结构。
- **结果**: 展示了AI聚类与人类情感标签的差异，但缺乏定量评估。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aesthetics are an important part of the symbolism of artistic works. Although subjective, humans categorize art based on the emotion evoked regardless of modality. What remains under-explored is how AI models form their own aesthetic categorization of human-produced media without explicit labels or cross-modal supervision. We present a self-supervised framework that projects four modalities (text, audio, image and video) into a shared 256-dimensional embedding space and applies iterative clustering to discover aesthetic structure. We discuss the divergence between AI-generated cluster assignments and human affective register labels on a weakly supervised multimodal dataset. This work has applications in understanding how AI structures cross-modal similarity, organizing heterogeneous media collections for Retrieval-Augmented Generation (RAG), and automated data labeling.

</details>

### 4. A Visual Dependence-Aware Framework for Multimodal Unsupervised Continual Post-Training **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.85)

- **arXiv ID**: [2608.26095](https://arxiv.org/abs/2608.26095)  · [📄 PDF](https://arxiv.org/pdf/2608.26095)
- **作者**: Kaichen Li, Zhilin Zhu, Jianhao Huang et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对多模态无监督持续后训练中目标令牌均匀优化而忽视视觉依赖异质性的问题，提出视觉依赖感知（VDA）框架。VC-OT将旧任务视觉依赖的结构失真建模为最优传输问题，通过区域感知地面代价和依赖分层传输惩罚缓解跨模态遗忘；VMA利用视觉依赖异质性强调视觉接地的新任务学习。实验表明该方法有效缓解跨模态遗忘并提升新任务性能。
- **摘要（英）**: To address uniform token optimization in multimodal unsupervised continual post-training, VDA framework uses VC-OT to model structural distortion of old-task visual dependence as optimal transport, mitigating cross-modal forgetting, and VMA exploits heterogeneity to emphasize visually grounded learning. Experiments show effectiveness in reducing forgetting and improving new-task performance.
- **评估**: 该工作深入挖掘视觉依赖特性，为多模态持续学习提供了新视角和有效方法。
- **核心贡献**: 提出视觉依赖感知框架，解决多模态持续后训练中的遗忘问题。
- **创新点**: 将视觉依赖结构失真建模为最优传输问题。
- **结果**: 有效缓解跨模态遗忘并提升新任务学习。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we explore a novel task of Multimodal Unsupervised Continual Post-Training (MU-CPT), enabling deployed MLLMs to continually evolve from streaming unlabeled data. Existing unsupervised post-training methods for MLLMs typically optimize target tokens uniformly, overlooking their heterogeneous visual dependence (VD). However, we reveal that token-level VD is crucial for MU-CPT. Specifically, its structural distortion serves as an indicator of cross-modal catastrophic forgetting, and its inherent heterogeneity acts as a compass to guide new-task learning. Leveraging this property, we propose a Visual Dependence-Aware (VDA) framework with two main components. First, Visually Constrained Optimal Transport (VC-OT) formulates the VD structural distortion of old-task VD during new-task learning as an optimal transport problem to mitigate cross-modal forgetting. By designing a region-aware ground cost and a dependence-stratified transport penalty, it prevents global shifts in visual focus while strictly prohibiting visual reliance from degenerating into language bias. Second, Visually Modulated Adaptation (VMA) exploits VD heterogeneity to emphasize visually grounded new-task learning, promoting new-task plasticity. Together, our method simultaneously maintains old-task stability and new-task plasticity during challenging MU-CPT. Extensive experiments under our MU-CPT setting validate the effectiveness of VDA.

</details>

### 5. StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models **⭐⭐⭐** (相关度: 65%, 质量: 0.75)

- **arXiv ID**: [2608.26067](https://arxiv.org/abs/2608.26067)  · [📄 PDF](https://arxiv.org/pdf/2608.26067)
- **作者**: Zhe Liu, Jinghua Hou, Yuxiang Lu et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对VLA模型如pi0.5的单帧范式限制时间推理和空间感知的问题，提出StreamPI流式多模态时间建模框架，不增加参数。指令锚定时间建模将（视觉观察，语言指令）作为原子时间单元，对内双向注意力融合，跨对因果注意力保持自回归推理。随机间隔流式训练策略（如每3帧）实现更快更平滑的动作执行，并增强对帧时序扰动的鲁棒性。
- **摘要（英）**: To address single-frame limitations in VLA models, StreamPI introduces streaming temporal modeling with instruction-anchored attention, treating each observation-instruction pair as an atomic unit with bidirectional intra-pair and causal inter-pair attention. Random-interval streaming training enables faster and smoother action execution and robustness to frame-timing perturbations.
- **评估**: 该工作为VLA模型提供轻量级时间建模方案，对机器人操作有实际应用价值。
- **核心贡献**: 提出StreamPI流式时间建模，增强单帧VLA的时间推理能力。
- **创新点**: 指令锚定的原子时间单元设计，无需额外参数。
- **结果**: 实现更快更平滑的动作执行，提升鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored temporal modeling. It treats each (visual observation, language instruction) pair as an atomic temporal unit: bidirectional attention within each pair enables cross-modal fusion, while causal attention across pairs preserves autoregressive streaming inference. This ensures the language instruction serves as a persistent semantic anchor throughout task execution. To bridge the gap between synchronous training and asynchronous real-robot deployment, we introduce a andom-interval streaming training strategy: a proper inter-frame interval (e.g., every 3 frames) enables faster and smoother action execution. Beyond this, randomizing the interval further improves robustness to frame-timing perturbations, supporting asynchronous deployment in practice. Furthermore, by leveraging the length extrapolation capability of the LLM backbone, StreamPI seamlessly inherits pretrained single-frame weights and supports flexible single-frame and multi-frame inference. Experiments on real-robot tasks spanning memory-dependent and precise perception scenarios, as well as the simulation benchmark LIBERO, demonstrate that StreamPI outperforms pi0.5 across diverse tasks.

</details>

### 6. Asymmetric Cross-Modal Fine-Grained Visual Categorization: ACF-Net and the BirdPro Benchmark **⭐⭐⭐** (相关度: 40%, 质量: 0.6)

- **arXiv ID**: [2608.25520](https://arxiv.org/abs/2608.25520)  · [📄 PDF](https://arxiv.org/pdf/2608.25520)
- **作者**: Bohan Deng, Shuo Ye, Zitong Yu
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对非对称跨模态细粒度视觉分类中音视频不同步、不对应的问题，提出ACF-Net框架，包含光流引导运动模块（OFGM）和不对称跨模态自适应融合模块（ACAF），分别增强动态视觉表征和进行不确定性感知融合。相比现有方法，该工作首次系统研究非对称跨模态场景，并构建了BirdPro基准数据集。实验表明该方法在细粒度分类任务上有效，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses asymmetric cross-modal fine-grained visual categorization where audio and video are weakly synchronized. It proposes ACF-Net with optical flow-guided motion and asymmetric adaptive fusion modules, along with the BirdPro benchmark. The method improves robustness in category-level recognition under weak cross-modal correspondence.
- **评估**: 该工作填补了非对称跨模态FGVC研究的空白，但领域相关性较低，且实验细节不足。
- **核心贡献**: 提出ACF-Net和BirdPro基准，首次探索非对称跨模态细粒度分类。
- **创新点**: 利用光流引导运动模块和不确定性感知融合处理弱对应关系。
- **结果**: 在BirdPro上验证了有效性，但未报告具体指标。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Audio-visual cross-modal Fine-Grained Visual Categorization (FGVC) aims to identify fine-grained categories by jointly leveraging visual and auditory information. However, FGVC under asymmetric cross-modal scenarios has received limited attention, where paired video and audio are not strictly synchronized and may not even correspond to the same individual or moment. Such weak and ambiguous cross-modal correspondence poses substantial challenges to effective representation learning and modality alignment. To address these issues, we propose ACF-Net, a novel optical flow-guided framework for asymmetric audio-visual fine-grained learning. ACF-Net consists of two key modules: Optical Flow-Guided Motion (OFGM) and Asymmetric CrossModal Adaptive Fusion (ACAF). OFGM captures motion-sensitive visual cues and suppresses irrelevant background interference, thereby enhancing discriminative dynamic representations in videos. ACAF estimates modality reliability under weakly matched audio-video pairs and performs uncertainty-aware adaptive fusion to improve category-level recognition robustness. To support research on asymmetric cross-modal FGVC, we further construct BirdPro, a new bird-oriented audio-visual benchmark, since existing datasets often lack large-scale category-level audio-video associations under non-strict temporal and instance correspondence. BirdPro contains 1,919 audio recordings and 11,965 videos covering 194 bird species. Extensive experiments show that ACF-Net achieves the best results compared with representative baseline methods, outperforming the strongest baselines by 2.97% and 1.92% in the fused and mismatched settings, respectively.

</details>

### 7. AdaptiveEmbed: Sample-Adaptive Multi-Vector Representation for Multimodal Retrieval **⭐⭐⭐** (相关度: 30%, 质量: 0.55)

- **arXiv ID**: [2608.25412](https://arxiv.org/abs/2608.25412)  · [📄 PDF](https://arxiv.org/pdf/2608.25412)
- **作者**: Xinze Liu, Lei Yang, Dayan Wu et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对多向量表示中固定容量分配忽略样本差异的问题，提出样本自适应多向量表示（SAMVR）新问题设置，并设计AdaptiveEmbed框架，通过多组学习实现内容自适应嵌入集（CAES）。相比固定容量方法，该方法根据样本检索效用动态分配向量数量，提升检索效率。实验表明在多个多模态检索基准上取得改进，但摘要未给出具体数值。
- **摘要（英）**: This paper introduces sample-adaptive multi-vector representation (SAMVR) for multimodal retrieval, where each sample's embedding capacity is determined by its retrieval utility. The proposed AdaptiveEmbed framework learns content-adaptive embedding sets via multi-group learning, outperforming fixed-capacity baselines.
- **评估**: 问题设定新颖，但与应用领域（自动驾驶感知）相关性低，且实验细节有限。
- **核心贡献**: 提出SAMVR问题设定和AdaptiveEmbed框架，实现样本级自适应表示容量。
- **创新点**: 根据样本检索效用动态分配向量数量，突破固定容量限制。
- **结果**: 在检索基准上优于固定容量方法，但未报告具体数值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-vector representations have emerged as an effective paradigm for multimodal retrieval, representing each sample with multiple complementary embeddings to capture fine-grained cross-modal information. However, existing approaches typically employ a fixed representation capacity, assigning the same number of vectors to all samples regardless of their individual retrieval demands. Such a fixed-capacity formulation overlooks the fact that different samples may require different amounts of representation capacity for effective retrieval. In this work, we introduce \emph{Sample-Adaptive Multi-Vector Representation} (SAMVR), a new problem setting for multimodal retrieval that studies how multi-vector representation capacity can be allocated at the sample level. Under SAMVR, each sample is represented by a \emph{content-adaptive embedding set} (CAES), whose capacity is determined according to the sample-specific retrieval utility of additional representation vectors. To instantiate SAMVR, we propose \emph{AdaptiveEmbed}, a unified framework for learning sample-adaptive multi-vector representations. AdaptiveEmbed learns structured multi-vector representations through \emph{Multi-Group Contrastive Learning} (MGCL) with the symmetric \emph{set-to-set similarity} (SetSim), and further employs \emph{Utility Policy Optimization} (UPO) to determine sample-specific representation capacity via \emph{Marginal Utility Allocation} (MUA). Experiments across multimodal retrieval benchmarks involving image, text, video, and audio show that sample-adaptive capacity allocation achieves overall better retrieval performance than fixed-capacity multi-vector representations, validating the effectiveness of SAMVR for multimodal retrieval. These results establish SAMVR as a viable formulation for adaptive capacity allocation in multi-vector multimodal retrieval.

</details>

### 8. RSFusionDet: Underwater RGB-Sonar Multimodal Object Detection **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.75)

- **arXiv ID**: [2608.25367](https://arxiv.org/abs/2608.25367)  · [📄 PDF](https://arxiv.org/pdf/2608.25367)
- **作者**: Zhuoyan Liu, Yihan Wang, Bo Wang et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/LEFTeyex/RSFusionDet](https://github.com/LEFTeyex/RSFusionDet)
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对水下单模态目标检测中光学图像受噪声和距离限制、声呐图像缺乏结构信息的问题，构建了RGB-Sonar多模态目标检测数据集RSFusion，并提出RSFusionDet检测器，包含跨注意力融合模块（CAFusion）和对象匹配头（OMHead）及损失（OMLoss），以融合空间错位的RGB和声呐特征并匹配同一目标。相比单模态方法，该方法充分利用互补信息，在RSFusion数据集上取得76.4/48.6 AP（RGB/Sonar）和83.4的检测性能。
- **摘要（英）**: This paper addresses underwater object detection by fusing RGB and sonar modalities, which have complementary strengths. It introduces the RSFusion dataset and RSFusionDet detector with cross-attention fusion and object matching head, achieving 76.4/48.6 AP on RGB/Sonar modalities.
- **评估**: 该工作对多模态融合检测有贡献，且与自动驾驶感知中的多传感器融合相关，但领域为水下场景。
- **核心贡献**: 构建RGB-Sonar多模态检测数据集并提出融合检测器。
- **创新点**: 设计跨注意力融合和对象匹配头处理空间错位。
- **结果**: 在RSFusion上取得76.4/48.6 AP，优于单模态方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Underwater unimodal object detection faces many challenges in sensor imaging, such as optical images limited by underwater noise and visible distance, and sonar images limited by less object structural information. While, optical images have rich object structural information, and sonar images are less affected by underwater noise and have a longer visible distance. Optical (RGB modality) and sonar (Sonar modality) images have complementary information underwater. In this paper, we create an RGB-Sonar multimodal object detection dataset, \textbf{R}GB-\textbf{S}onar \textbf{Fusion} (RSFusion) and propose evaluation metrics for the benchmark. And we propose the \textbf{R}GB-\textbf{S}onar \textbf{Fusion} \textbf{Det}ector (RSFusionDet) with a new RGB-Sonar multimodal object detection result expression for RGB-Sonar multimodal object detection. We analyze the features of RGB and Sonar modal information, and design a Cross-Attention Fusion (CAFusion) module to fuse RGB-Sonar spatial misalignment features and Object Matching Head (OMHead) with Loss (OMLoss) to match identical objects in RGB-Sonar modalities. Our RSFusionDet achieves 76.4/48.6 AP (RGB/Sonar) for object detection and 83.4 \(\text{F1-Score}_{match}\) for object matching, on RSFusion, which outperforms other object detection models. Compared with the DINO baseline, our method improves by 0.7/1.4 AP (RGB/Sonar) while simultaneously providing reliable cross-modal object matching. The code and datasets are publicly available at https://github.com/LEFTeyex/RSFusionDet.

</details>

### 9. Hierarchical MoE for Multi-Modal ILD Diagnosis **⭐⭐⭐** (相关度: 25%, 质量: 0.65)

- **arXiv ID**: [2608.25261](https://arxiv.org/abs/2608.25261)  · [📄 PDF](https://arxiv.org/pdf/2608.25261)
- **作者**: Alec K. Peltekian, Gorkem Durak, Halil Ertugrul Aktas et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.AI, cs.CV
- **摘要（中）**: 针对间质性肺病分类中多模态数据异质性问题，提出分层多模态MoE模型，结合冻结的预训练影像专家和结构化EHR数据，通过两阶段门控（模态级和子门控）实现患者特定权重和临床特征组分解。相比单一影像模型，该方法在严格患者级交叉验证下取得最高平均AUC（0.8750），优于影像-only REN（0.8646）和SwinUNETR（0.7685）。
- **摘要（英）**: This paper presents a hierarchical multimodal MoE for ILD classification, integrating frozen imaging expert and EHR via two-stage gating. It achieves the highest mean AUC of 0.8750, outperforming imaging-only baselines, with interpretability across modalities and clinical groups.
- **评估**: 医学影像领域应用，与自动驾驶感知相关性低，但MoE架构设计有一定参考价值。
- **核心贡献**: 提出分层MoE框架融合影像和EHR数据，提升ILD分类性能。
- **创新点**: 两阶段门控实现模态级和特征组级自适应加权。
- **结果**: AUC达0.8750，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixture-of-experts (MoE) models combine specialized predictors under learned routing, offering a principled mechanism for leveraging heterogeneity in medical data. We present a hierarchical multimodal MoE for interstitial lung disease (ILD) classification that integrates a frozen, pre-trained imaging expert with structured electronic health records (EHR) via two-stage gating. A modality-level gate assigns patient-specific weights to imaging and EHR predictions, while a sub-gating module decomposes the EHR branch into clinically defined feature groups with learned, group-specific contributions. This design preserves stable imaging representations while enabling input-dependent clinical weighting and explicit EHR specialization. Under strict patient-level cross-validation, the model achieved the highest mean AUC among the evaluated methods (0.8750 +- 0.0443), compared with 0.8646 for imaging-only REN and 0.7685 for SwinUNETR. The framework extends interpretability across anatomical regions, imaging--EHR utilization, and clinically defined EHR feature groups.

</details>

### 10. WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report **⭐⭐⭐⭐** (相关度: 50%, 质量: 0.8)

- **arXiv ID**: [2608.24053](https://arxiv.org/abs/2608.24053)  · [📄 PDF](https://arxiv.org/pdf/2608.24053)
- **作者**: Junjie Zhou, Ke Mei, Lei Li et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding)
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.CL, cs.IR
- **摘要（中）**: 针对通用多模态嵌入模型的需求，提出WeMM-Embedding系列模型，支持文本、图像、视频、文档和交错输入，包含2B、4B、9B三个变体，采用两阶段训练（大规模对齐和精炼）。相比现有开源基线，2B变体已超越8B基线，9B变体在MMEB-v2上取得80.6的新SOTA，并在微信26任务内部基准和14个在线A/B测试中表现优异。
- **摘要（英）**: This technical report presents WeMM-Embedding, a family of universal multimodal embedding models supporting diverse inputs with flexible output dimensions. The 2B variant surpasses an 8B baseline on MMEB-v2, and the 9B variant achieves a new SOTA score of 80.6, with strong practical gains in WeChat applications.
- **评估**: 工业级多模态嵌入模型，性能强大，但与应用领域相关性一般，且为技术报告。
- **核心贡献**: 发布WeMM-Embedding系列模型，实现多模态嵌入的SOTA性能。
- **创新点**: 两阶段训练和跨尺度知识迁移提升嵌入质量。
- **结果**: 9B模型在MMEB-v2上取得80.6，超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Universal multimodal embeddings are becoming a core component of modern AI systems, enabling heterogeneous content to be represented in a shared space for applications such as retrieval, recommendation, classification, and agentic systems. In this report, we present WeMM-Embedding, a family of universal multimodal embedding models supporting text, images, videos, visual documents, and arbitrarily interleaved multimodal inputs with flexible output dimensions. The family comprises 2B, 4B, and 9B variants and is trained in two stages: a large-scale multimodal alignment stage, followed by a refinement stage using curated data, fine-grained relevance supervision, and cross-scale knowledge transfer. Across extensive evaluations, WeMM-Embedding achieves leading performance on multiple public benchmarks. Notably, the 2B variant already surpasses the previously leading 8B open-source baseline on MMEB-v2, while the 9B variant further achieves a new state-of-the-art overall score of 80.6. WeMM-Embedding also demonstrates strong practical performance across WeChat applications, with substantial gains on a 26-task in-house benchmark and consistent improvements across 14 online A/B tests. It has been deployed at scale across recommendation and search applications, including WeChat Channels, Official Accounts, Moments, and e-commerce services. We have released the model weights and code to facilitate future research at https://github.com/Tencent/WeMM-Embedding.

</details>

---

## Vision Transformer

### 1. Token-Oriented Semantic Communication with Pretrained Vision Transformers **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.25410](https://arxiv.org/abs/2608.25410)  · [📄 PDF](https://arxiv.org/pdf/2608.25410)
- **作者**: Jiwoong Im, Minwoo Kim, Jaeho Lee et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: eess.SP, cs.AI, cs.CV
- **摘要（中）**: 针对边缘系统中客户端-服务器协同推理的通信成本和模型间互操作性问题，提出了一种面向token的语义通信框架，利用token级任务相关性决定传输哪些压缩图像潜变量，无需直接传输token嵌入。该框架协调轻量级ViT、学习图像压缩模型和大规模服务器ViT，无需端到端训练，通过ViT patch token和LIC潜变量的空间对齐实现选择性传输。
- **摘要（英）**: This paper proposes a token-oriented semantic communication framework for edge inference, using token-level task relevance to select compressed latents for transmission, avoiding direct token embedding transfer. It coordinates pretrained ViTs and LIC without end-to-end training, leveraging spatial alignment for efficiency.
- **评估**: 该论文关注通信效率，与自动驾驶感知核心任务相关性低，但token级选择性传输思想有一定创新性。
- **核心贡献**: 提出了一种基于token相关性的语义通信框架，降低通信成本并提升互操作性。
- **创新点**: 利用ViT patch token与LIC潜变量的空间对齐，实现token粒度传输。
- **结果**: 在资源受限场景下实现高效协同推理，但未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Token communications realize the semantic communication principle at the granularity of transformer tokens, providing a promising direction for client--server collaborative inference in resource-constrained edge systems. However, directly transmitting token embeddings presents two practical challenges: substantial communication cost and limited interoperability across model-specific token embedding spaces. To address these challenges, we propose a \emph{token-oriented} semantic communication framework. In this framework, token-level task relevance determines which compressed image latents are transmitted, enabling token-granular transmission without directly transmitting token embeddings. The framework is modular, coordinating three pretrained components---a lightweight client-side vision transformer (ViT), a learned image compression (LIC) model, and a large server-side ViT---without end-to-end training. The key enabler is the one-to-one spatial alignment between ViT patch tokens and the LIC latent vectors, which allows token-level task relevance to directly determine which latent vectors are transmitted. Building on this alignment, token-aligned LIC selectively transmits task-relevant latents, layer-selective attention rollout estimates token relevance from a selected range of attention layers in a single forward pass, and surrogate token substitution adapts the frozen server model by optimizing a single learnable token. Experiments on ImageNet show that the proposed framework achieves a more favorable rate--accuracy trade-off than recent semantic communication schemes, hand-crafted codecs, and task-agnostic LIC models.

</details>

### 2. Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2608.27367](https://arxiv.org/abs/2608.27367)  · [📄 PDF](https://arxiv.org/pdf/2608.27367)
- **作者**: Frederik Berenz
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对JEPA世界模型中固定大小ViT编码器在简单任务上过参数化、复杂任务上欠参数化的问题。②提出了连续容量增长（SCG）方法，从最小编码器开始，根据任务复杂度通过测试-验证机制增量扩展宽度或深度，并引入SIGReg正则化防止崩溃。③相比已有工作，该方法实现了参数效率的显著提升，并动态适应任务需求。④在60维多目标动力学任务上，深度扩展将预测损失降低20.3%，参数效率比固定大模型高56倍。
- **摘要（英）**: This paper addresses the inefficiency of fixed-size ViT encoders in JEPA world models by proposing Successive Capacity Growth (SCG), which starts from a minimal encoder and incrementally expands width or depth based on task complexity. It uses function-preserving expansion and SIGReg regularization to prevent collapse. SCG improves prediction loss by 20.3% with 56x parameter efficiency over fixed large models.
- **评估**: 该论文对自适应视觉Transformer有重要贡献，与自动驾驶中的高效感知模型相关。
- **核心贡献**: 提出了SCG方法，实现任务驱动的ViT编码器动态扩展。
- **创新点**: 通过测试-验证机制和SIGReg，实现参数高效的容量增长。
- **结果**: 预测损失降低20.3%，参数效率提升56倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transformer blocks for higher-order semantic abstraction), driven by a task-agnostic test-and-verify mechanism that exploits function-preserving expansion to safely trial architectural changes and roll back if they do not improve prediction loss. The Sketched Isotropic Gaussian Regularizer (SIGReg) ensures that all learned semantic dimensions remain statistically independent and aligned with the predictive objective, preventing collapse even as the architecture grows. On a 60-dimensional multi-object dynamics task, SCG naturally triggers depth expansion, improving prediction loss by 20.3% over the fixed small baseline with 56 times greater parameter efficiency than scaling to the fixed large model; on a 2D navigation task, a single width expansion yields even an 23% improvement over the fixed large model. Across all three tested environments of increasing complexity, the adaptive encoder matches or exceeds the fixed small baseline, with zero false-positive expansions and bit-exact function preservation (ratio = 1.0, absolute difference = 0.0). The take-away is that JEPA world model encoders need not be pre-allocated at maximum capacity - they can grow successively as the task demands, achieving significant compute and data efficiency while maintaining representation quality.

</details>

### 3. Less Contouring, More Accuracy: Lesion-Guided ROI Deep Learning for Ovarian Ultrasound Classification **⭐⭐** (相关度: 15%, 质量: 0.65)

- **arXiv ID**: [2608.25965](https://arxiv.org/abs/2608.25965)  · [📄 PDF](https://arxiv.org/pdf/2608.25965)
- **作者**: Mehran Ahmad, Ali Abbasian Ardakani, Afshin Mohammadi et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对卵巢超声分类中像素级分割标注负担重的问题，研究了病变引导的感兴趣区域（ROI）深度学习能否在减少标注负担的同时保持诊断性能。在MMOTU和OUD两个数据集上比较了全局图像、病变引导ROI、病变轮廓和轮廓放射组学四种策略，并评估了四种深度学习架构。结果表明病变引导ROI策略在减少标注需求的同时取得了有竞争力的诊断性能。
- **摘要（英）**: This paper investigates whether lesion-guided ROI deep learning can achieve competitive diagnostic performance while reducing annotation burden in ovarian ultrasound classification. It compares four strategies across two datasets and four architectures, showing that lesion-guided ROI achieves competitive performance with less annotation effort.
- **评估**: 该论文属于医学影像分类领域，与自动驾驶感知方向无关，但ROI引导方法有一定通用性。
- **核心贡献**: 验证了病变引导ROI深度学习在减少标注负担下的有效性。
- **创新点**: 系统比较多种ROI策略并统一框架评估。
- **结果**: 病变引导ROI策略在减少标注需求下保持竞争力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ovarian lesion classification using transvaginal ultrasound remains challenging due to overlapping imaging characteristics and the dependence on expert interpretation. This study investigates whether lesion-guided region-of-interest (ROI) deep learning can achieve competitive diagnostic performance while reducing the annotation burden associated with pixel-level lesion segmentation. Two publicly available ovarian ultrasound datasets were evaluated: the Multi-Modality Ovarian Tumor Ultrasound (MMOTU) dataset for eight-class classification and the Ovarian Ultrasound Dataset (OUD) for binary classification. Four strategies were compared under a unified framework: global image-based deep learning, lesion-guided ROI-based deep learning, lesion contour-based deep learning, and contour-based radiomics with machine learning classifiers. Four deep learning architectures, MaxViT-Tiny, Swin Transformer, EfficientNet-B7, and ResNet18, were evaluated. Radiomics models were developed using support vector machine, k-nearest neighbors, and artificial neural network classifiers, with ANOVA-based feature selection applied for the lower-sample OUD dataset. The lesion-guided ROI strategy achieved the strongest overall performance, with MaxViT-Tiny obtaining 93.10% accuracy and an AUC of 0.99 on MMOTU and 97.56% accuracy and an AUC of 0.99 on OUD. The contour-based approach achieved comparable accuracy but required substantially higher annotation effort. These findings demonstrate that lesion-guided ROI deep learning provides an effective balance between diagnostic performance and annotation efficiency, offering a practical approach for scalable AI-assisted ovarian ultrasound analysis

</details>

### 4. Capacity Overflow: A Blind Spot for Backdoor Attacks in Vision MoE **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.25371](https://arxiv.org/abs/2608.25371)  · [📄 PDF](https://arxiv.org/pdf/2608.25371)
- **作者**: Xiaocheng Zou, Tiancheng Zheng, Xiaolin Xu et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.CR
- **摘要（中）**: 针对视觉混合专家（MoE）架构中容量受限的令牌调度机制，识别了批次依赖行为作为被忽视的攻击面，并提出了一种隐蔽的供应链后门攻击。通过三阶段框架：在早期MoE层注入后门，在深层训练中和器抑制后门，并配置批次自适应容量因子，使大批次部署时通过令牌溢出禁用中和器。在V-MoE和Swin-MoE上的ImageNet-100和GTSRB实验中，激活模式攻击成功率76-87%，休眠模式低于9%，并规避了现有检测。
- **摘要（英）**: This paper identifies batch-dependent capacity dispatch in Vision MoE as an overlooked attack surface and proposes a stealthy supply-chain backdoor attack via a three-phase framework. It achieves activation-mode attack success rates of 76-87% with dormant-mode ASR below 9% on V-MoE and Swin-MoE, evading existing defenses.
- **评估**: 该论文揭示了视觉MoE架构的安全漏洞，对自动驾驶中大规模Transformer部署的安全性有重要警示意义。
- **核心贡献**: 首次提出利用MoE容量机制的批次自适应后门攻击。
- **创新点**: 通过容量因子配置实现攻击的休眠与激活状态切换。
- **结果**: 激活模式攻击成功率76-87%，休眠模式低于9%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixture-of-Experts (MoE) has become a prevalent paradigm for scaling Vision Transformers efficiently. To ensure computational scalability and prevent expert overload, Vision MoE architectures employ a capacity-bounded token dispatch mechanism, where each expert's processing budget depends on the inference batch size. This work identifies this batch-dependent behavior as an overlooked attack surface, and proposes a stealthy supply-chain backdoor attack that exploits this property through a three-phase framework. First, we inject a backdoor into an early MoE layer. Second, we train a neutralizer in a deeper MoE layer that suppresses the backdoor under normal capacity. Third, we configure a batch-adaptive capacity factor that preserves high capacity for small batches while reducing it for large batches, naturally disabling the neutralizer via token overflow at deployment-scale batch sizes. The attack remains in dormant mode during small-batch security audits and enters activation mode during large-batch deployment. Experiments on V-MoE and Swin-MoE across ImageNet-100 and GTSRB demonstrate activation-mode attack success rates of 76-87% with dormant-mode ASR below 9%, while evading Neural Cleanse, STRIP, Fine-Pruning, and Activation Clustering. Our findings reveal a fundamental security risk arising from batch-dependent execution in scalable Vision MoE architectures.

</details>

### 5. Unsupervised Adaptation of 3D CT Foundation Models for 3D CBCT Segmentation **⭐⭐⭐⭐** (相关度: 50%, 质量: 0.8)

- **arXiv ID**: [2608.27190](https://arxiv.org/abs/2608.27190)  · [📄 PDF](https://arxiv.org/pdf/2608.27190)
- **作者**: Gauthier Miralles, Loic Le Folgoc, Vincent Jugnon et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①这篇论文针对CBCT分割中标注数据稀缺和与诊断CT域差异大的问题。②提出了基于冗余减少特征对齐的无监督域适应（UDA）框架，无需目标域标注或推理时适应，且架构无关，适用于CNN和ViT基础模型。③相比现有预训练基础模型和UDA方法，该方法通过显式特征空间桥接有效解决了跨模态泛化问题。④在两个CT-CBCT肝脏分割基准上（介入血管和放射治疗）一致优于现有方法。
- **摘要（英）**: This paper addresses CBCT segmentation challenges with scarce annotations and domain shift from CT. A redundancy-reducing feature alignment UDA framework is proposed, architecture-agnostic for CNN and ViT models. It consistently outperforms existing foundation models and UDA methods on two liver segmentation benchmarks.
- **评估**: 该论文在医学影像域适应方面有较强创新，但与应用领域（自动驾驶）相关性较低。
- **核心贡献**: 提出了无需目标域标注的架构无关UDA框架。
- **创新点**: 利用冗余减少特征对齐实现跨模态泛化。
- **结果**: 在CT-CBCT分割基准上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D segmentation of cone-beam CT (CBCT) is critical for interventional and radiation therapy applications, yet it remains limited by two compounding challenges: the scarcity of annotated CBCT data and the large domain shift from diagnostic CT. Interventional CBCT exhibits fundamental modality differences from conventional CT, driven by acquisition and physics effects as well as contrast-specific vascular content, thereby limiting effective cross-modality model transfer. We propose a novel unsupervised domain adaptation (UDA) framework based on redundancy-reducing feature alignment, enabling 3D CBCT segmentation with no target-domain annotations or inference-time adaptation. Our framework is architecture-agnostic, seamlessly adapting both CNN-based and ViT-based foundation models. We evaluate our method on two challenging CT-CBCT liver segmentation benchmarks: one for interventional vascular procedures and one for radiation therapy, demonstrating that even large-scale pretrained segmentation networks require explicit feature-space bridging to generalize across acquisition modalities, and that our approach consistently outperforms existing pretrained foundation model and UDA strategies. To support reproducibility and benchmarking, we release the liver segmentations for a public CBCT dataset, along with the code, trained models, and weights.

</details>

### 6. Parameter-Efficient pretrained-CT-to-MRI Transfer for Rectal Cancer Segmentation: Performance-Calibration Trade-offs **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.27178](https://arxiv.org/abs/2608.27178)  · [📄 PDF](https://arxiv.org/pdf/2608.27178)
- **作者**: Aneesh Rangnekar, Jorge Tapias Gomez, Joseph O Deasy et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①这篇论文针对直肠癌MRI分割中计算效率与校准不确定性之间的权衡问题。②提出了SWIFT框架，使用在10,444个CT体积上预训练的Swin V2编码器，通过四种配置（全微调、解码器压缩、低秩适应和LoRA解码器集成）适应T2加权MRI。③相比全微调，SWIFTe将参数减少70.1%，肿瘤检测率从89.9%提升至93.9%，同时保持几何精度。④在247例测试集上，SWIFTe实现了更优的检测率和放射组学一致性，但表面DSC略有下降。
- **摘要（英）**: This paper addresses efficiency and calibration trade-offs in rectal cancer MRI segmentation. SWIFT adapts a CT-pretrained Swin encoder via parameter-efficient configurations, reducing parameters by 70.1% and improving detection rate to 93.9%. It demonstrates effective performance-calibration balance.
- **评估**: 该论文在医学影像分割的效率优化上有价值，但与应用领域（自动驾驶）相关性低。
- **核心贡献**: 提出了参数高效的CT到MRI迁移分割框架。
- **创新点**: 结合LoRA和集成实现性能与校准的平衡。
- **结果**: 参数减少70.1%，检测率提升至93.9%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate rectal cancer segmentation from magnetic resonance imaging (MRI) is essential for adaptive radiotherapy and tumor response assessment, but deployment also requires computational efficiency and informative, calibrated uncertainty estimates. We therefore introduce SWIFT, a SWin pretrained model wIth parameter-eFficient and Tumor-aware fine-tuning for rectal cancer segmentation. A Swin V2 encoder pretrained on 10,444 public 3D CT volumes using a DINOv2-style objective was adapted to T2-weighted MRI through four cumulative configurations: full fine-tuning (SWIFT), decoder compression (SWIFTe), low-rank adaptation (SWIFTe-LoRA), and a four-member LoRA-decoder ensemble (SWIFTe-LDE4). Geometric accuracy, tumor detection, radiomic agreement, and probability calibration were evaluated on a held-out 247-case test set from a single-institution cohort acquired using 1.5 or 3 Tesla GE scanners. Compared with SWIFT, SWIFTe reduced total parameters by 70.1% (from 72.8M to 21.8M) and increased tumor detection rate from 89.9% to 93.9%, while achieving a slightly lower median surface DSC (0.61 versus 0.62) and improved radiomic agreement. In a separate SWIFTe ablation, removing tumor-aware augmentation reduced detection from 93.9% to 89.9% but increased surface DSC from 0.61 to 0.64, demonstrating a detection-boundary-agreement trade-off. SWIFTe-LoRA used 14.6% of SWIFTe's trainable parameters while retaining similar segmentation performance. SWIFTe-LDE4 achieved the lowest calibration errors among the four configurations after temperature scaling (expected calibration error, 0.217; Brier score, 0.222), although the absolute expected calibration error indicates residual miscalibration. Similar efficiency-calibration patterns were observed using the public VoCo checkpoint, supporting robustness across pretrained initializations rather than external clinical generalizability.

</details>

### 7. MoE-based Feature Adapter for Prompt-free Binary Coronary Artery Segmentation in X-ray Angiography **⭐⭐⭐** (相关度: 35%, 质量: 0.7)

- **arXiv ID**: [2608.24783](https://arxiv.org/abs/2608.24783)  · [📄 PDF](https://arxiv.org/pdf/2608.24783)
- **作者**: Lin Xi, Yingliang Ma
- **🏷️ 机构**: University of East Anglia
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: ①针对X射线血管造影中冠状动脉分割因血管细、对比度低和背景干扰而困难的问题。②提出了基于混合专家（MoE）的特征适配器，构建在参数高效的ViT适配器上，使用多个轻量级专家和输入相关的top-k路由，自适应细化血管相关特征。③相比U-Net和Transformer基线，该方法能更好地适应异质血管造影外观，且计算成本受限。④在MOSXAV和外部XACV数据集上优于代表性基线，提高了跨数据集泛化能力。
- **摘要（英）**: This paper addresses coronary artery segmentation challenges in X-ray angiography by proposing a prompt-free mixture-of-experts feature adapter built on parameter-efficient ViT adapters. It uses multiple lightweight experts with input-dependent routing to refine vessel features while limiting computational cost. Experiments show improved performance and cross-dataset generalization over baselines.
- **评估**: 该工作将MoE适配器应用于医学图像分割，方法有创新性，但与自动驾驶感知领域相关性较低。
- **核心贡献**: 提出了基于MoE的特征适配器，用于冠状动脉分割，提升泛化能力。
- **创新点**: 在ViT适配器中引入MoE和top-k路由，实现自适应特征细化。
- **结果**: 在MOSXAV和XACV数据集上优于基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate segmentation of coronary arteries in X-ray angiography videos is essential for quantitative coronary analysis and image-guided interventions. However, accurate segmentation remains challenging because coronary vessels are thin and exhibit low contrast, while the presence of catheters, guidewires, and complex anatomical background structures can further interfere with vessel delineation. Existing U-Net- and Transformer-based models provide strong baselines, but their shared feature-adaptation pathways may be insufficient for heterogeneous angiographic appearances. In this paper, we propose a prompt-free mixture-of-experts (MoE) feature adapter for binary coronary artery segmentation. Built upon parameter-efficient Vision Transformer adapters, the proposed method uses multiple lightweight experts with input-dependent top-$k$ routing to adaptively refine vessel-related features while limiting active computational cost. Experiments on MOSXAV and external evaluation on XACV show that the proposed method outperforms representative baselines and improves cross-dataset generalisation. These results suggest that MoE-based adapter learning is effective for robust coronary artery segmentation in X-ray angiography videos.

</details>

### 8. Weakly Supervised Seafloor Segmentation for Seagrass Habitat Mapping in Side-Scan Sonar Imagery **⭐⭐⭐** (相关度: 45%, 质量: 0.7)

- **arXiv ID**: [2608.24756](https://arxiv.org/abs/2608.24756)  · [📄 PDF](https://arxiv.org/pdf/2608.24756)
- **作者**: Hayat Rajani, Nuno Gracias, Rafael Garcia
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.LG
- **摘要（中）**: ①针对侧扫声纳图像中海草栖息地制图依赖密集人工标注、成本高的问题。②采用弱监督语义分割框架，仅用图像级标签学习像素级地图，结合ViT编码器-解码器和分类分支，提取类激活图，并用密集条件随机场细化伪标签，采用迭代自训练和采样策略处理类别不平衡。③相比全监督方法，降低了标注成本，并针对声学图像噪声和弱边界调整了CRF。④在保留测试剖面上，细化伪标签的mIoU达到89.3%。
- **摘要（英）**: This paper addresses the high cost of manual annotation in seagrass habitat mapping from side-scan sonar imagery by adapting a weakly supervised semantic segmentation framework. It uses image-level labels, class activation maps, and refined pseudo-labels with a tuned CRF, achieving an mIoU of 89.3% on a held-out transect. This approach significantly reduces annotation effort while maintaining high accuracy.
- **评估**: 该工作展示了弱监督方法在声纳图像分割中的有效性，对水下感知有参考价值，但与自动驾驶核心领域相关性中等。
- **核心贡献**: 将弱监督语义分割应用于侧扫声纳海草制图，减少标注成本。
- **创新点**: 结合ViT和CRF细化伪标签，并针对声学图像特性调整。
- **结果**: 细化伪标签mIoU达89.3%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Seagrass meadows are crucial blue-carbon habitats, and mapping their extent is a prerequisite for coastal management and carbon inventory. Optical satellite sensors cover large areas but cannot reach deep or turbid water, whereas side-scan sonar (SSS) images the seabed at high resolution and at any depth. Interpreting SSS, however, still relies on dense manual annotation, which is slow and costly. We address this by adapting a weakly supervised semantic segmentation framework to SSS benthic habitat mapping, so that pixel-level maps are learned from image-level labels alone. The framework couples a ViT-based encoder-decoder with a classification branch, extracts class activation maps, and refines them into pseudo-labels with a dense conditional random field that we tune for the noise and weak boundaries of acoustic imagery. It follows an iterative self-training scheme, together with a sampling strategy to cope with the strong class imbalance of the data. We also study the effect of different loss functions on segmentation quality, finding Lovász-Softmax loss the most effective. On a held-out transect, the refined pseudo-labels reached an mIoU of 89.3\% against the ground truth, and the segmentation branch, trained without any pixel-level labels, reached 87.6\%. Self-supervised pretraining on unlabelled SSS added a further 3\% in mean intersection-over-union. Field trials further demonstrate the generalizability of the trained model. These results show that accurate and label-efficient benthic habitat mapping from side-scan sonar is feasible at the scale needed for coast-wide seagrass monitoring.

</details>

### 9. Interpretable Fundus Image Classification via Ring-Based Retinal Vasculature Features **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.24723](https://arxiv.org/abs/2608.24723)  · [📄 PDF](https://arxiv.org/pdf/2608.24723)
- **作者**: Xiaoyan Li, Shixin Xu, Arvind Gupta et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, stat.ML
- **摘要（中）**: 该论文针对眼底图像分类中深度学习模型缺乏可解释性的问题，提出了一种基于视盘周围环形视网膜血管结构的可解释分类框架。方法量化了血管几何、颜色、氧合相关外观及血管-背景熵等生理学描述符，并跨环形区域聚合以捕捉空间变化。相比依赖深度潜在表示的黑盒模型，该方法仅使用定量血管描述符，在HRF数据集上达到91.1%的准确率，与大规模预训练的视觉Transformer RETFound相当。该工作为医学图像分析提供了可解释的替代方案，但与自动驾驶感知领域相关性较低。
- **摘要（英）**: This paper addresses the lack of interpretability in deep learning-based fundus image classification by proposing a ring-structured representation of retinal vasculature. It quantifies vessel geometry, color, oxygenation-related appearance, and entropy within concentric regions, achieving 91.1% accuracy on HRF, matching RETFound. The method offers a physiologically motivated, interpretable alternative to black-box models, though its relevance to autonomous driving is limited.
- **评估**: 该论文在医学图像可解释性方面有贡献，但主题与自动驾驶感知领域相距较远，创新性和影响力有限。
- **核心贡献**: 提出了一种基于环形血管特征的可解释眼底图像分类方法。
- **创新点**: 利用生理学启发的环形血管描述符替代深度潜在表示。
- **结果**: 在HRF数据集上达到91.1%准确率，与RETFound相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Retinal fundus photography is widely used for screening and monitoring ocular diseases, but many modern classification pipelines rely on deep latent representations and provide limited interpretability. This study develops an interpretable fundus image classification framework based on a ring-structured representation of the retinal vasculature centered on the optic disc. The method quantifies vessel geometry, color appearance, oxygenation-related vascular appearance, and vessel--background entropy within concentric retinal regions. These physiologically motivated descriptors are derived from vessel masks, image intensities, and optical-density measurements and aggregated across rings to capture spatial variation in vascular properties. Using only quantitative vascular descriptors, the proposed method achieved strong classification performance across three public fundus datasets. On HRF, it achieved 91.1\% accuracy using automatically generated vessel masks, matching RETFound, a vision transformer pretrained on large-scale retinal fundus image data, under the same evaluation setting. Additional analyses suggest that pretrained image models are sensitive to acquisition-related spatial cues, including fundus scale and retinal position within the field of view, as well as broader non-vessel image characteristics. This framework may support interpretable disease classification, quantitative retinal phenotyping, and retinal biomarker discovery without requiring large task-specific training datasets.

</details>

### 10. Low-Rank Ternary Adaptation for Fine-Tuning Transformers **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.24469](https://arxiv.org/abs/2608.24469)  · [📄 PDF](https://arxiv.org/pdf/2608.24469)
- **作者**: Alexandru-Dragos Manolache, Yunqiang Li, Jan van Gemert
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/alexmanoo/ternary_adaptation](https://github.com/alexmanoo/ternary_adaptation)
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.LG
- **摘要（中）**: 该论文针对三元Transformer无法直接使用低秩LoRA方法微调的问题，提出了三元乘法适配（ternary multiplicative adaptation），通过低秩Kronecker分解将三元权重的离散更新（如符号翻转或置零）表示为两个小三元矩阵的元素级乘积。该方法保持三元域，支持无需反量化的直接合并，在六个模型（包括三元化的LLaMA-3 1B/3B和ViT-B/16）上实验，恢复了大量量化损失的性能，并优于强低比特和三元基线。该工作对高效模型微调有贡献，但与自动驾驶感知的直接相关性中等。
- **摘要（英）**: This paper tackles the challenge of fine-tuning ternary transformers with low-rank adaptation methods, proposing ternary multiplicative adaptation via low-rank Kronecker factorization. It preserves the ternary domain and enables direct merging without dequantization, recovering performance on six models including LLaMA-3 and ViT-B/16. The method outperforms strong low-bit baselines, offering efficient fine-tuning for resource-constrained settings.
- **评估**: 该论文在模型压缩和高效微调方面有创新，但主题更偏向通用机器学习，对自动驾驶感知的针对性不强。
- **核心贡献**: 提出了一种保持三元域的低秩适配方法，支持直接合并。
- **创新点**: 利用Kronecker分解实现三元权重的离散更新表示。
- **结果**: 在多个模型上恢复量化损失，优于现有低比特基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ternary transformers offer extreme memory and compute efficiency, but existing low-bit LoRA-based methods cannot directly fine-tune ternary weights. Current approaches either require dequantization, restoring low-bit base weights to higher precision to merge with adaptation weight, or update only quantization parameters, preventing a merged model that remains ternary. We propose ternary multiplicative adaptation, which represents discrete updates of ternary weights such as sign flips or zeroing through a low-rank Kronecker factorization into two small ternary matrices applied element-wise to ternary weights. This design is parameter-efficient and expressive, preserves the ternary domain, and supports direct merging without dequantization. Experiments on six models across language and vision, including ternarized LLaMA-3 1B and 3B and a ternary ViT-B/16, demonstrate that our method recovers much of the performance lost to quantization and outperforms strong low-bit and ternary baselines. Code is available at https://github.com/alexmanoo/ternary_adaptation.

</details>

---

## Multi-camera Perception

### 1. A Dual-Transformer for Multi-Camera View Recommendation **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2608.25601](https://arxiv.org/abs/2608.25601)  · [📄 PDF](https://arxiv.org/pdf/2608.25601)
- **作者**: Josep Cabacas-Maso, Carles Ventura, Ismael Benito-Altamirano
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对多摄像机编辑中如何选择最佳视角的问题，提出了一种双Transformer架构，包含时间编码器和交叉注意力模块，使候选视角能独立查询历史上下文。在TVMCE数据集上，该方法显著优于现有SOTA，Precision@0.5从37.16%提升至56.60%，使用SwinV2骨干网络时达到69.65%。
- **摘要（英）**: This paper addresses multi-camera view recommendation by proposing a Dual-Transformer with cross-attention, where a temporal encoder builds memory and candidate views query it. It achieves 56.60% Precision@0.5 on TVMCE, improving over the prior 37.16%, and 69.65% with SwinV2 backbone.
- **评估**: 该论文聚焦于媒体制作中的视角选择，与自动驾驶多相机感知相关性较低，但方法设计有一定参考价值。
- **核心贡献**: 提出了一种双Transformer架构用于多相机视角推荐，显著提升编辑精度。
- **创新点**: 将视角选择解耦为时间编码和交叉注意力查询，增强候选视角的独立评估能力。
- **结果**: 在TVMCE数据集上Precision@0.5提升至56.60%，最佳配置达69.65%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-camera systems are foundational to modern media production, and multi-camera editing is a critical task. This involves the proper selection of the appropriate camera view at each moment. In this paper, we propose a novel Dual-Transformer architecture with Cross-Attention that heavily outperformed the current SOTA models over the TVMCE dataset (TV Shows Multicamera Editing dataset). Our model decouples these tasks: (1) a dedicated temporal encoder first processes the sequence of past frames to build a rich memory of the recent history, and (2) the candidate camera views then act as queries to this memory via a cross-attention module, allowing each candidate to independently interrogate the historical context and find the most relevant information for its own evaluation. Our approach achieved 56.60% Precision@0.5, representing a substantial improvement over the prior best result of 37.16%. We further conducted an ablation study exploring the use of lightweight backbone architectures, where the SwinV2 backbone yielded the best performance, achieving 69.65% Precision@0.5. Using this best-performing configuration, we then investigated the feasibility of adapting the model to replicate the editing style of a specific human editor. To this end, we fine-tuned the model using varying proportions of the initial segment of a target video. Our results demonstrate that even with only 20% of the video used for fine-tuning, the model exhibited measurable improvements in Precision@0.5, indicating strong potential for data-efficient personalization of editing style adapted to each individual TV show or producer.

</details>

### 2. Syn2RealTrack: Bridging the Gap Between Synthetic and Real-World Datasets for Online Multi-View Multi-Target Tracking **⭐⭐⭐** (相关度: 75%, 质量: 0.7)

- **arXiv ID**: [2608.24130](https://arxiv.org/abs/2608.24130)  · [📄 PDF](https://arxiv.org/pdf/2608.24130)
- **作者**: Duong Nguyen-Ngoc Tran, Ngoc Doan-Minh Huynh, Cu Quoc Le et al. (13 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/SKKUAutoLab/aic26_mc3dp](https://github.com/SKKUAutoLab/aic26_mc3dp)
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对仓库场景多相机3D感知中合成数据到真实数据的域差距问题，提出Syn2RealTrack在线管线，将域差距分解为相机标定、物体形状先验和物体数量假设三个可分离点，并分别采用图像自标定、可见性加权部件描述符和因果滤波器等局部补救措施。该方法无需重新训练特征提取器，通过重新分配几何和外观之间的信任实现自适应。在A数据集上验证了有效性。
- **摘要（英）**: This paper tackles the synthetic-to-real gap in multi-camera 3D perception for warehouse scenes by decomposing it into calibration, shape prior, and cardinality prior issues, each addressed with local remedies like image-only calibration and visibility-weighted descriptors. The online pipeline adapts without retraining, improving ground-plane localization and cross-camera association.
- **评估**: 该论文针对多相机3D跟踪中的域适应问题，分解问题并设计针对性解决方案，对自动驾驶多相机感知有借鉴意义。
- **核心贡献**: 提出了Syn2RealTrack，一种分解合成到真实域差距的多相机跟踪管线。
- **创新点**: 将域差距分解为三个可分离点并分别处理，避免单一域适应模块的负担。
- **结果**: 在仓库场景数据集上有效提升跨相机身份关联和地面定位精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-camera 3D perception systems for warehouse scenes are trained largely on synthetic data and evaluated on physically captured environments. The resulting synthetic-to-real gap, which corrupts ground-plane localization and cross-camera identity association, is usually treated as one deficiency for a single domain-adaptation module to absorb; we argue instead that it enters the pipeline at three separable points: the camera calibration, the object shape prior, and the assumption that the object census is known, each admitting a different local remedy. Our online pipeline, Syn2RealTrack, follows this decomposition: lens distortion is recovered from images alone under a calibration that provides none, detections are fused across views by a visibility-weighted part-based descriptor that abstains on occluded parts rather than guessing, person height is measured in closed form from calibration instead of copied from a synthetic prior, and a closed-world cardinality prior is paired with a causal filter that removes the phantom boxes the prior manufactures. The system therefore adapts by reallocating trust between geometry and appearance without retraining a feature extractor. On the AI City Challenge 2026 Track~1 evaluation server it reaches a 3D Higher Order Tracking Accuracy (HOTA) of 52.0118%. The code will be released at https://github.com/SKKUAutoLab/aic26_mc3dp

</details>

### 3. Vision-centric generative AI models: A software-hardware perspective **⭐⭐⭐** (相关度: 60%, 质量: 0.6)

- **arXiv ID**: [2608.27199](https://arxiv.org/abs/2608.27199)  · [📄 PDF](https://arxiv.org/pdf/2608.27199)
- **作者**: Eleni Tselepi, Cristian Sestito, Shady Agwa et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AR
- **摘要（中）**: ①这篇论文针对视觉生成式AI模型在边缘设备（如自动驾驶车辆）上的部署面临硬件资源受限的问题。②作者从软件-硬件协同设计的视角，量化了多种生成模型在各类加速器平台上的参数成本和能效，并将四种生成模型家族映射到七个实际应用领域。③相比以往仅关注输出质量的研究，本文强调了部署约束应从设计之初就纳入考虑，以实现“正确的模型”在“正确的硬件”上运行。④论文倡导软硬件协同设计，使生成式AI部署在更广泛的平台上可持续且可访问。
- **摘要（英）**: This paper addresses the deployment challenges of vision generative AI models on edge devices with strict hardware constraints, such as autonomous vehicles. It quantifies parameter cost and energy efficiency across accelerator platforms and maps generative model families to real-world applications. The authors advocate for software-hardware co-design to ensure sustainable and accessible deployment.
- **评估**: 该论文提供了有价值的视角，但偏重综述性分析，缺乏具体算法创新，对自动驾驶感知研究者的直接参考价值有限。
- **核心贡献**: 提出了视觉生成式AI软硬件协同设计的系统性分析框架。
- **创新点**: 从软硬件协同角度重新审视生成式AI部署问题。
- **结果**: 量化了模型参数成本与能效，并提出了部署原则。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision generative artificial intelligence (AI) has emerged as one of the most rapidly advancing areas of deep learning. The explosion of multimodal models has made them widely associated with text-to-image applications running on large datacentres. However, vision generative models are equally needed in applications that operate under strict hardware constraints at the edge, including autonomous vehicles, agricultural sensors, and mobile devices. In this Perspective, we argue that progress in vision generative AI has been driven by output quality, with hardware evolving reactively to accommodate growing model demands. We quantify the parameter cost and energy efficiency of these models across a range of accelerator platforms, and map four generative model families against seven real-world application domains. Finally, we advocate a software-hardware co-design approach, where deployment constraints are considered from the start of the design process, ensuring that the "right model" runs on the "right hardware" to serve the "right application", making generative AI deployment sustainable and accessible across a much broader range of platforms.

</details>

### 4. GeoMAD: Geometry-Aware Multi-View Anomaly Detection via Deformable Fusion and Distributional Alignment **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.75)

- **arXiv ID**: [2608.26724](https://arxiv.org/abs/2608.26724)  · [📄 PDF](https://arxiv.org/pdf/2608.26724)
- **作者**: Shang-Fu Chen, Jhih-Ciang Wu, Kuan-Chuan Peng et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①这篇论文针对多视角异常检测中几何对应不足和分布不一致的问题。②提出了GeoMAD框架，包含跨视角可变形融合模块（CDFM）和分布视角对齐（DVA），CDFM直接在2D特征图上学习内容自适应采样偏移，无需相机标定或3D重建。③相比基于体素的方法，GeoMAD避免了昂贵的3D构建和类别特定假设；相比轻量级补丁融合，它提供了连续的跨视角对应。④实验表明GeoMAD在多类别工业场景中实现了统一的异常检测，性能优于现有方法。
- **摘要（英）**: This paper tackles geometric correspondence deficiency and distributional inconsistency in multi-view anomaly detection. GeoMAD introduces a Cross-view Deformable Fusion Module and Distributional View Alignment, enabling content-adaptive sampling without camera calibration or 3D construction. It outperforms existing methods in multi-class industrial settings.
- **评估**: 该方法在多视角感知领域具有创新性，可变形融合机制对多相机系统有借鉴意义，但应用场景偏向工业检测。
- **核心贡献**: 提出了无需3D监督的多视角异常检测统一框架。
- **创新点**: 利用可变形融合实现连续跨视角对应。
- **结果**: 在多类别工业异常检测基准上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view anomaly detection (MvAD) detects defects by exploiting complementary observations from multiple camera viewpoints. The central challenge is to fuse views with sufficient geometric awareness while remaining scalable to multi-class industrial settings. Existing methods typically fall into two extremes: voxel-based fusion provides explicit geometric alignment but requires costly 3D construction and class-specific assumptions, whereas lightweight patch-based fusion is efficient but relies on discrete candidate matching and lacks continuous cross-view correspondence. In this paper, we propose GeoMAD, a unified multi-view, multi-class AD framework that addresses both geometric correspondence deficiency and distributional inconsistency. Our \textit{Cross-view Deformable Fusion Module} (CDFM) learns content-adaptive, view-pair-specific sampling offsets directly on 2D feature maps and arranges them across a multi-scale window pyramid with image-global reference sampling, enabling hierarchical cross-view correspondence without camera calibration, voxel construction, or class-specific 3D supervision. We further introduce \textit{Distributional View Alignment} (DVA), a self-supervised cross-view regularization loss that aligns each view's bottleneck distribution against a per-instance view-centric target, enforcing global consistency without pixel-level correspondence. Together, CDFM and DVA bridge local geometric correspondence and global distributional consistency, providing geometry-aware and distribution-consistent fusion while preserving the efficiency of 2D feature-space learning. Extensive experiments on Real-IAD and MANTA-Tiny show that GeoMAD achieves strong detection and localization performance in unified MvAD.

</details>

### 5. See More, Detect Less? Taming Information Leakage in Multi-View Anomaly Detection **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.25168](https://arxiv.org/abs/2608.25168)  · [📄 PDF](https://arxiv.org/pdf/2608.25168)
- **作者**: Shang-Fu Chen, Kuan-Chuan Peng, Jhih-Ciang Wu et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.MM
- **摘要（中）**: ①针对多视角异常检测中，朴素融合多视角信息会导致正常线索传播到解码器，从而重建异常区域并破坏检测依赖的重建差距，即跨视角信息泄漏问题。②提出GLAD框架，首次结合视觉基础模型特征与局部和全局跨视角融合，包含多视角合并注意力（MMA）模块和对象引导注意力（OGA）模块。③MMA以线性复杂度进行局部跨视角融合，使用可学习的视角重要性权重和令牌级门控；OGA通过聚合所有视角的类令牌到对象级表示并广播回补丁令牌来捕获全局上下文。④实验表明，GLAD在多个基准上优于现有方法，有效缓解信息泄漏并提升异常检测性能。
- **摘要（英）**: This paper identifies cross-view information leakage in multi-view anomaly detection, where naive fusion causes normal cues to reconstruct anomalies, collapsing the detection gap. GLAD is proposed as the first framework combining vision foundation features with local and global cross-view fusion, using Multi-view Merging Attention (MMA) for linear-complexity local fusion and Object-Guided Attention (OGA) for global context. Experiments show GLAD outperforms existing methods, effectively mitigating leakage and improving detection accuracy.
- **评估**: 该论文深入分析了多视角融合的失败模式，并提出创新框架，对多相机感知和异常检测有重要启示，与自动驾驶感知高度相关。
- **核心贡献**: 首次提出并解决多视角异常检测中的跨视角信息泄漏问题，设计GLAD框架实现有效融合。
- **创新点**: 通过限制解码器信息流和结合局部-全局注意力机制，实现线性复杂度的多视角融合。
- **结果**: 在多个基准上优于现有方法，显著提升异常检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In multi-view anomaly detection, more cross-view information can actually hurt. When multiple inspection views are naively fused in a reconstruction-based pipeline, normal cues from intact views propagate to the decoder, which faithfully reconstructs anomalous regions, collapsing the reconstruction gap the detector depends on. We call this failure mode \emph{cross-view information leakage} and show that effective multi-view fusion must explicitly restrict the information reaching the decoder. Building on this insight, we present GLAD(Global-Local Attention Driven framework), the first framework combining vision foundation model features with local and global cross-view fusion for multi-view anomaly detection. The Multi-view Merging Attention (MMA) module performs local cross-view fusion at linear complexity with learnable view importance weighting and token-wise gating, letting each view selectively incorporate fine-grained evidence from other views at $\mathcal{O}(N)$ cost. The Object-Guided Attention (OGA) module captures global context by aggregating class tokens from all views into a single object-level representation and broadcasting it back to patch tokens via temperature-scaled sigmoid gating, replacing the original patch representations rather than adding a residual to preserve the reconstruction gap. Experiments on Real-IAD and MANTA-Tiny show that GLAD outperforms state-of-the-art methods across sample-, image-, and pixel-level metrics, confirming that principled information restriction is key to multi-view anomaly reasoning.

</details>

### 6. ExMesh++: From Multi-View Images to Relightable UV-PBR Mesh Assets via Topology-Adaptive Reconstruction and Decomposition **⭐⭐⭐** (相关度: 50%, 质量: 0.75)

- **arXiv ID**: [2608.24109](https://arxiv.org/abs/2608.24109)  · [📄 PDF](https://arxiv.org/pdf/2608.24109)
- **作者**: Chuanjin Fan, Lifan Wu, Wenjie Chang et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.GR, cs.CV
- **摘要（中）**: ①针对多视角重建生成可编辑和可重光照网格资产时，现有方法在拓扑、UV参数化和PBR材质图方面存在不足，且联合优化几何、材质和光照可能导致歧义分解。②提出ExMesh++，一个分阶段框架，第一阶段通过自适应顶点分裂和合并优化显式网格几何和拓扑，同时保持UV一致性；第二阶段固定网格-UV载体，优化UV空间PBR贴图和环境光照。③与现有隐式场或高斯基元方法不同，ExMesh++直接操作显式网格，避免表面提取和纹理烘焙。④实验表明，ExMesh++在重建质量和材质分解上优于现有方法，生成可直接用于渲染的资产。
- **摘要（英）**: This paper addresses the challenge of reconstructing relightable UV-PBR mesh assets from multi-view images, where existing methods struggle with topology, UV parameterization, and material decomposition. ExMesh++ is a staged framework that first refines mesh geometry and topology with adaptive vertex splitting/merging while maintaining UV consistency, then optimizes UV-space PBR maps and lighting. It outperforms existing methods in reconstruction quality and material decomposition, producing directly renderable assets.
- **评估**: 该论文在三维重建和材质估计方面有创新，对自动驾驶中的场景重建和仿真有潜在应用，但直接相关性中等。
- **核心贡献**: 提出了ExMesh++，一个分阶段的多视角重建框架，生成具有良好拓扑和PBR材质的可重光照网格。
- **创新点**: 通过自适应拓扑调整和分阶段优化，避免几何、材质和光照的歧义分解。
- **结果**: 在重建质量和材质分解上优于现有方法，生成可直接渲染的资产。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view reconstruction extends beyond surface recovery to editable and relightable mesh assets. Such assets require well-formed topology, valid UV parameterization, and explicit PBR material maps. Existing surface reconstruction approaches optimize implicit fields, Gaussian primitives, or other intermediate representations. Converting them into such assets often requires surface extraction and texture baking. Inverse-rendering methods estimate materials and illumination, yet these components often remain tied to neural fields or point-based primitives rather than the final mesh. Joint optimization of geometry, materials, and lighting may also allow these variables to compensate for one another, leading to ambiguous decomposition. To address these limitations, we present ExMesh++, a staged framework for reconstructing relightable UV-PBR mesh assets from multi-view images. The first stage refines explicit mesh geometry and topology through adaptive vertex splitting and merging, while maintaining UV consistency as the topology changes. The second stage fixes the resulting mesh-UV carrier and optimizes UV-space PBR maps together with environment lighting. Building on this stable carrier, ExMesh++ models one-bounce diffuse indirect illumination through secondary-ray tracing with shared UV-PBR materials. Experiments demonstrate competitive geometry accuracy, strong relighting performance, and direct usability of the exported assets in standard DCC workflows.

</details>

### 7. CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.85)

- **arXiv ID**: [2608.26656](https://arxiv.org/abs/2608.26656)  · [📄 PDF](https://arxiv.org/pdf/2608.26656)
- **作者**: Yuanxiang Ni, Xianliang Huang, Chenhang Ma et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对3D场景中多物体移除面临的严重遮挡、语义纠缠以及几何和多视角一致性问题。②提出CoGeo-GS框架，为高斯分配概念感知语义标签，实现灵活物体选择和单阶段优化，并引入结合单目深度先验、扩散细化与边界对齐混合的几何补全流程，以及几何正则化细化策略。③相比现有3DGS方法，能处理多物体场景，减少前景与背景干扰，稳定重建移除区域几何。④实验表明在视觉质量和重建保真度上优于现有方法。
- **摘要（英）**: This paper addresses multi-object removal in 3D scenes, hindered by occlusion and semantic entanglement. CoGeo-GS assigns concept-aware tags to Gaussians for flexible selection and introduces a geometry-aware completion pipeline with depth priors and diffusion refinement. It outperforms existing methods in visual quality and reconstruction fidelity.
- **评估**: 该论文针对3D编辑中的多物体移除难题，提出概念驱动与几何感知的联合方案，对自动驾驶场景中的动态物体编辑具有参考价值。
- **核心贡献**: 提出CoGeo-GS，实现概念驱动、几何感知的多物体3D场景移除。
- **创新点**: 结合语义标签与几何补全流程，实现单阶段多物体移除。
- **结果**: 在视觉质量和重建保真度上超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object removal in 3D scenes is challenging due to severe occlusions, semantic entanglement, and the difficulty of maintaining geometric and multi-view consistency. Existing 3D Gaussian Splatting (3DGS) methods perform well for single-object editing but scale poorly to multi-object scenarios, often requiring repetitive optimization and yielding unstable geometry in removed regions. We propose CoGeo-GS, a concept-driven framework for controllable multi-object removal in 3D scenes. CoGeo-GS assigns concept-aware semantic tags to Gaussians, enabling flexible object selection and reducing interference between foreground objects and background structures within a single optimization stage. To recover plausible geometry, we introduce a geometry-aware completion pipeline that combines monocular depth priors with diffusion-based refinement and boundary-aligned blending. A geometry-regularized refinement strategy further stabilizes reconstruction and preserves multi-view consistency. Experiments demonstrate that CoGeo-GS outperforms existing methods in visual quality and reconstruction fidelity.

</details>

### 8. NeuDonatello: Uncertainty-Aware Framework for Accurate Neural SDF Learning **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.88)

- **arXiv ID**: [2608.26504](https://arxiv.org/abs/2608.26504)  · [📄 PDF](https://arxiv.org/pdf/2608.26504)
- **作者**: Alvin Jinsung Choi, Wanhee Kim, Taeyun Kim et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对从RGB图像恢复3D表面时，纹理缺失、遮挡和场景歧义导致的SDF估计不准确问题。②提出NeuDonatello框架，用蒙特卡洛采样建模空间变化的不确定性，开发自适应正则化以在RGB监督不可靠处加强几何约束，并引入不确定性感知的SDF到密度转换尺度参数。③相比现有方法，显式建模不确定性并利用其指导重建，提高复杂场景的准确性。④实验表明在多种场景下达到最先进的重建精度。
- **摘要（英）**: This paper tackles inaccurate SDF estimation from RGB images due to textureless regions and ambiguities. NeuDonatello models spatially varying uncertainty via Monte Carlo sampling, enabling adaptive regularization and uncertainty-aware density conversion. It achieves state-of-the-art reconstruction accuracy across diverse scenes.
- **评估**: 该论文将不确定性建模引入神经表面重建，方法新颖且实验充分，对3D感知中的几何恢复有借鉴意义。
- **核心贡献**: 提出NeuDonatello，利用SDF不确定性提升神经表面重建精度。
- **创新点**: 蒙特卡洛采样建模不确定性并自适应调整几何约束。
- **结果**: 在多种场景下达到最先进的重建精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural surface reconstruction has emerged as a powerful paradigm for recovering high-quality 3D surfaces from multi-view images. However, recovering accurate geometry solely from RGB images remains challenging due to uncertainties arising from textureless regions, occlusions, and inherent scene ambiguities. Existing methods often overlook such uncertainties, leading to inaccurate estimates of the signed distance function (SDF). We introduce NeuDonatello, a novel framework that models and leverages SDF uncertainty to improve surface reconstruction. Central to our approach is to model spatially varying uncertainty using a Monte Carlo sampling strategy. Using this uncertainty, we develop an adaptive regularization that selectively strengthens geometric constraints where RGB supervision is unreliable, avoiding incorrect surface reconstruction. We further introduce an uncertainty-aware scale parameter for the SDF-to-density conversion. Conditioned on uncertainty, this design enables more accurate modeling of spatially varying densities. Extensive experiments demonstrate that NeuDonatello achieves state-of-the-art reconstruction accuracy, with robust performance across diverse scenes using only posed RGB images.

</details>

### 9. MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding and Coaching **⭐⭐⭐⭐** (相关度: 40%, 质量: 0.8)

- **arXiv ID**: [2608.26094](https://arxiv.org/abs/2608.26094)  · [📄 PDF](https://arxiv.org/pdf/2608.26094)
- **作者**: Hao Yin, Paritosh Parmar, Lijun Gu et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI, cs.ET
- **摘要（中）**: ①针对现有动作质量评估（AQA）数据集和方法仅依赖视觉输入，忽略肌肉力学等生理动态，且将动作建模为整体模式，难以提供细粒度、生物力学基础的反馈的问题。②提出了MyoMechanix，一个多模态生态系统，包含7,500+样本、20种动作、38个受试者，同步多视角RGB视频、3D姿态、sEMG等信号，并构建了Fitness Knowledge Graph（FKG）和CUBIST推理引擎，实现组合评分和可解释评估。③相比现有AQA基准，整合了生理信号和结构化知识，支持细粒度错误归因和反馈生成。④实验建立了MyoMechanix-AQA、VideoQA和Video2EMG任务，但摘要未提供具体性能数据。
- **摘要（英）**: This paper introduces MyoMechanix, a multimodal ecosystem for weight-loaded action quality assessment that aligns motion with muscle activity, featuring a large benchmark with synchronized video, pose, and sEMG data. It constructs a Fitness Knowledge Graph and a compositional reasoning engine for interpretable feedback. This work advances AQA by integrating physiological dynamics and structured knowledge, though specific performance metrics are not detailed in the abstract.
- **评估**: 该工作构建了大规模多模态AQA基准，具有数据价值和创新性，但与自动驾驶感知领域相关性有限。
- **核心贡献**: 提出了包含生理信号和知识图谱的多模态动作质量评估生态系统。
- **创新点**: 将肌肉力学信号与视觉数据结合，并利用知识图谱实现组合推理。
- **结果**: 建立了最大的多模态AQA基准，但具体性能未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing action quality assessment (AQA) datasets and methods rely primarily on visual inputs such as RGB and pose, overlooking physiological dynamics such as muscle mechanics and often modeling actions as monolithic patterns. These limitations hinder fine-grained, biomechanically grounded feedback. We introduce MyoMechanix, a multimodal ecosystem for weight-loaded actions that aligns motion with muscle activity. Expert-annotated, it contains 7,500+ samples of 20 actions from 38 subjects, with synchronized multiview RGB video, 3D pose, sEMG, and additional physiological signals, forming the largest multimodal AQA benchmark to date. We further construct the Fitness Knowledge Graph (FKG), which organizes expert annotations into structured relationships among actions, phases, key steps, errors, and corrective feedback, enabling compositional scoring and interpretable assessment. Building on these representations, we develop CUBIST (Compositional Ontological Reasoning Engine), which performs decomposition-analysis-recomposition for fine-grained error attribution and feedback generation. We also establish MyoMechanix-AQA, MyoMechanix-VideoQA, and a novel MyoMechanix-Video2EMG task. Experiments show that multimodal sensing and structured representations improve performance, interpretability, and error attribution, with CUBIST achieving state-of-the-art results; VideoQA enhances language-grounded action understanding; and Video2EMG suggests video-based alternatives to costly EMG sensing. MyoMechanix advances skilled activity understanding toward biomechanically grounded, multimodal, and compositional reasoning for Physical AI applications in fitness, rehabilitation, healthcare, and machine learning. Project page: https://haoyin116.github.io/MyoMechanix/

</details>

### 10. Moving Beyond More Views: Redundancy-Aware Ego-Exo Fusion for Proficiency Estimation **⭐⭐⭐⭐** (相关度: 50%, 质量: 0.8)

- **arXiv ID**: [2608.25736](https://arxiv.org/abs/2608.25736)  · [📄 PDF](https://arxiv.org/pdf/2608.25736)
- **作者**: Xu Dong, Wanqing Li, Anthony Adeyemi-Ejeye et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/dx199771/AdaMVS](https://github.com/dx199771/AdaMVS)
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: ①针对EgoExo熟练度估计中，增加更多外部视角反而降低性能的问题，原因是多视角冗余和过拟合。②提出了两个互补模块：AdaMVS从数据角度自适应选择信息量最大的视角令牌进行融合，VIB-GB从特征角度结合梯度混合和变分信息瓶颈正则化，压缩冗余信号并抑制过拟合。③相比简单融合所有视角，该方法能学习哪些视角有用，提高泛化能力。④在EgoExo-4D和EgoExo-Fitness上的实验表明，该方法有效，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the degradation of EgoExo proficiency estimation with more exocentric views by proposing AdaMVS for adaptive view selection and VIB-GB for feature regularization. These modules mitigate multiview redundancy and overfitting, improving generalization. Experiments on EgoExo-4D and EgoExo-Fitness demonstrate effectiveness, though specific metrics are not provided.
- **评估**: 该工作针对多视角融合中的冗余问题提出了有效解决方案，对多模态感知有参考价值，但与自动驾驶核心领域相关性中等。
- **核心贡献**: 提出了自适应视角选择和特征正则化模块，解决多视角融合中的冗余和过拟合问题。
- **创新点**: 结合弱监督视角选择和变分信息瓶颈正则化，提升多模态融合的鲁棒性。
- **结果**: 在EgoExo基准上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> EgoExo proficiency estimation aims to assess action quality by integrating fine-grained motion cues from egocentric (1st-person) views with spatial context from multiple exocentric (3rd-person) views. Simply adding more exocentric views degrades EgoExo performance, as redundant or noisy perspectives dilute useful motion cues. Our analysis identifies two key causes: (1) Multiview redundancy - From the data perspective, certain views provide limited or noisy information, diluting discriminative cues; (2) Overfitting - From the feature perspective, conventional fusion increases representational complexity, causing the model to memorise view-specific patterns rather than learn generalisable representations. To address these issues, we propose two complementary modules: AdaMVS, which adaptively identifies and fuses the most informative view tokens under weak supervision from the data perspective, and VIB-GB, which combines Gradient Blending and Variational Information Bottleneck regularisation from the feature perspective to compress redundant signals and suppress overfitting during training. Experiments on EgoExo-4D and EgoExo-Fitness demonstrate that our method learns both which view to look at and how to fuse them, achieving new state-of-the-art results. Our source code is available at https://github.com/dx199771/AdaMVS

</details>

---

## Network Pruning

### 1. SHIFT-LLM: Distribution Shift Correction in Depth-Pruned LLMs **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.25068](https://arxiv.org/abs/2608.25068)  · [📄 PDF](https://arxiv.org/pdf/2608.25068)
- **作者**: Ali Bahri, Hang Li, Hongliang Li et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: 针对深度剪枝移除Transformer块导致隐藏状态分布破坏和准确率下降的问题，提出了SHIFT-LLM，一种无需训练的剪枝后校正框架，在每个剪枝位置插入线性残差适配器。LRA保留原始残差块的恒等路径并添加轻量仿射残差校正，通过闭式最小二乘回归校准，无需梯度计算。支持低秩分解和跨层合并，可与参数高效微调结合。
- **摘要（英）**: This paper introduces SHIFT-LLM, a training-free post-pruning correction framework that inserts Linear Residual Adapters to mitigate distributional mismatch in depth-pruned LLMs. LRAs are calibrated via closed-form least-squares regression and support low-rank factorization. It combines with parameter-efficient fine-tuning for further recovery.
- **评估**: 该论文针对LLM剪枝，与自动驾驶感知领域相关性低，但方法在模型压缩上有一定通用性。
- **核心贡献**: 提出无需训练的深度剪枝校正框架。
- **创新点**: 利用线性残差适配器近似缺失残差更新。
- **结果**: 缓解分布偏移并支持额外压缩。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Depth pruning removes entire Transformer blocks to reduce the inference cost of large language models, but disrupts the hidden-state distributions expected by downstream layers, leading to significant accuracy loss. We introduce SHIFT-LLM, a training-free post-pruning correction framework that inserts a Linear Residual Adapter (LRA) at each pruning site. Each LRA preserves the identity pathway of the original residual block and adds a lightweight affine residual correction. This correction is calibrated via closed-form least-squares regression on a small held-out set, without gradient computation, to approximate the missing residual update produced by the pruned block. Together with the preserved identity pathway, the resulting LRA output approximates the hidden state produced by the original block, thereby mitigating the distributional mismatch introduced by layer removal while avoiding the expensive attention and feed-forward computations of the removed blocks. The resulting LRAs support low-rank factorization and exact merging across consecutive pruned layers for additional compression, and combine naturally with parameter-efficient fine-tuning for further recovery beyond fine-tuning the pruned model alone. Experiments on five model families, six layer-selection criteria, and seven zero-shot benchmarks show that SHIFT-LLM consistently recovers accuracy lost to depth pruning across most configurations, achieving gains up to +15.7 points on Llama-3.1-8B-Instruct while requiring only a few hundred calibration samples and no gradient computation.

</details>

### 2. VisCache: Visual KV Cache Pruning for Efficient Vision Large Language Model Inference **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.85)

- **arXiv ID**: [2608.24063](https://arxiv.org/abs/2608.24063)  · [📄 PDF](https://arxiv.org/pdf/2608.24063)
- **作者**: Lyuke Wang, Zhuo Li, Guangxu Zhu
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/Wlklk/VisCache](https://github.com/Wlklk/VisCache)
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对视觉大语言模型（VLLM）在长上下文推理中，视觉KV缓存导致的计算和内存开销过大的问题。②提出了VisCache，一个无需训练的即插即用框架，包含两个阶段：轻量级VLM选择性转发信息关键帧以过滤时间冗余；以及PruneKV算法，采用抛物线层间预算分配和非对称更新机制（选择性剪枝键、融合值）来压缩视觉KV缓存。③相比现有均匀剪枝方法，VisCache考虑了VLLM的注意力动态，实现了粗到细的剪枝，减少了信息损失。④实验表明，VisCache显著提升推理效率，最高可实现2.35倍加速。
- **摘要（英）**: This paper addresses the high computational and memory costs of visual KV caches in Vision Large Language Models (VLLMs) during long-context inference. It proposes VisCache, a training-free plug-and-play framework with two stages: a lightweight VLM filters keyframes to reduce temporal redundancy, and a PruneKV algorithm applies parabolic layer-wise budget allocation with asymmetric key pruning and value fusion. Compared to uniform pruning, VisCache preserves critical information and achieves up to 2.35x speedup in inference.
- **评估**: 该工作针对VLLM推理效率瓶颈，提出了一种无需训练的视觉KV缓存剪枝方法，具有实用性和创新性，对多模态感知系统的高效部署有重要参考价值。
- **核心贡献**: 提出VisCache框架，通过关键帧过滤和注意力感知的KV剪枝，显著提升VLLM推理效率。
- **创新点**: 引入抛物线层间预算分配和非对称键值更新机制，实现粗到细的视觉KV缓存剪枝。
- **结果**: 推理速度最高提升2.35倍，同时保持性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Vision Large Language Models (VLLMs) have achieved remarkable success in multimodal reasoning, their long-context inference remains prohibitively expensive due to the massive computation and memory overhead of visual Key-Value (KV) caches. Existing KV compression methods often apply uniform pruning across visual tokens and layers, leading to substantial information loss and degraded performance.To address this challenge, we propose \textbf{VisCache}, a plug-and-play framework for coarse-to-fine \textbf{Vis}ual KV \textbf{Cache} pruning without training, which consists of two synergistic stages. First, a lightweight VLM filters temporal redundancy by selectively forwarding semantically informative keyframes. Second, we introduce {PruneKV}, a surgical KV compression algorithm tailored to the attention dynamics of VLLMs. Unlike rigid pruning strategies, PruneKV adopts a parabolic layer-wise budget allocation together with an asymmetric update mechanism that selectively prunes keys while fusing values, thereby preserving critical contextual information. Extensive experiments demonstrate that VisCache substantially improves inference efficiency, achieving up to {2.35$\times$ speedup} and significant memory reduction while maintaining competitive performance with only {19--28\%} KV cache retention. VisCache consistently outperforms existing baselines, establishing a new Pareto frontier between efficiency and performance for long-context VLLM inference. Code is available at https://github.com/Wlklk/VisCache

</details>

### 3. KISS-GS: 3D Gaussian Splatting Compression Kept Simple **⭐⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2608.26948](https://arxiv.org/abs/2608.26948)  · [📄 PDF](https://arxiv.org/pdf/2608.26948)
- **作者**: Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对3D高斯泼溅（3DGS）场景重建后文件体积过大的问题，现有压缩系统组合多种策略，导致增益来源不透明且组件复用受限。②提出了KISS-GS，一个模块化压缩流水线，将压缩与训练完全解耦，通过剪枝方案实现15.7倍压缩，并编码为图像格式。③相比已有工作，该方法简化了压缩流程，提出了自组织2D码本和并行代表分配平滑（PRAS）技术。④在编码阶段进一步减少6.6倍场景大小，并通过可选编码感知微调提升性能。
- **摘要（英）**: This paper addresses the massive file sizes of 3D Gaussian Splatting scenes by proposing KISS-GS, a modular compression pipeline decoupled from training. It achieves 15.7x compaction via pruning and 6.6x encoding reduction using novel self-organizing 2D codebooks and PRAS. The approach simplifies compression and improves transparency, with optional encoding-aware fine-tuning for further gains.
- **评估**: 该论文在3D场景压缩方面有实用价值，但与自动驾驶感知领域相关性较低。
- **核心贡献**: 提出了KISS-GS，一个解耦训练的模块化3DGS压缩流水线。
- **创新点**: 通过自组织2D码本和PRAS技术，实现高效且透明的压缩。
- **结果**: 实现了15.7倍压缩和6.6倍编码缩减，显著减小场景文件大小。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene reconstruction with 3D Gaussian Splatting (3DGS) has become common, however deployment remains painful as the uncompressed file sizes can be massive. Current 3DGS compression systems combine multiple strategies for file size reduction, which can obscure where gains come from and limit component reuse across training pipelines. To make the gains more transparent, we propose KISS-GS, a modular compression pipeline named after the principle of keeping things simple, designed to decouple compression entirely from training. Given a 3DGS scene reconstructed with vanilla 3DGS, we are able to reduce it through compaction by 15.7x using a combination of state-of-the-art pruning schemes. Then we encode it into an image-based format designed for simple, ubiquitous decoding. With the SOG-XT format, we propose a novel extension to Self-Organizing Gaussians with two main contributions: (i) Self-organizing 2D Codebooks and (ii) Parallel Representative Assignment Smoothing (PRAS), which leverages the symmetry of quaternion and scale parameterizations to produce 2D attribute grids more amenable to encoding. This encoding reduces scene size by 6.6x. We show that optional encoding-aware fine-tuning yields a further 2.2x. Across standard 3DGS benchmarks, our simple and modular approach thus achieves a total of 85x to 319x reductions in the size of the scene over uncompressed vanilla 3DGS, setting new benchmarks for real-world scenes and surpassing tightly integrated methods in rate-distortion. Decoding relies solely on web-native image formats, and the modular design makes each stage easy to combine with future advances in reconstruction and compaction. Code and project page: https://fraunhoferhhi.github.io/KISS-GS/

</details>

### 4. CrossMambaTuning: Synergistic Spatial and Cross-Layer Adaptation for Machine Vision Compression **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2608.25568](https://arxiv.org/abs/2608.25568)  · [📄 PDF](https://arxiv.org/pdf/2608.25568)
- **作者**: Haobo Xiong, Shaobo Liu, Kai Liu et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/rsr1123/CrossMambaTuning](https://github.com/rsr1123/CrossMambaTuning)
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对预训练学习图像压缩模型在下游机器视觉任务中微调时缺乏跨层协调机制的问题，提出了CrossMambaTuning框架，集成状态空间模型与跨层交互机制进行参数高效微调。设计了带任务特定提示和多尺度分支的高效Mamba适配器，以及利用参数共享策略的尺度不变跨层适配器（SICA）来融合不同尺度的任务信息并减少冗余。相比现有方法，参数开销减少了72%，在多个机器视觉任务上取得了最先进性能。
- **摘要（英）**: To address the lack of cross-layer coordination in fine-tuning pretrained learned image compression models for downstream vision tasks, this paper proposes CrossMambaTuning, integrating state space models with cross-layer interaction for parameter-efficient fine-tuning. It introduces an efficient Mamba adapter with task-specific prompts and multi-scale branching, plus a Scale-Invariant Cross-Layer Adapter (SICA) using parameter sharing to fuse multi-scale information and reduce redundancy. The method achieves SOTA performance on multiple vision tasks with 72% parameter reduction compared to SOTA methods.
- **评估**: 该论文在图像压缩与视觉任务适配的交叉领域提出了新颖的跨层交互微调方法，对参数效率优化有显著贡献，但与自动驾驶感知核心方向关联较弱。
- **核心贡献**: 提出了CrossMambaTuning框架，通过跨层交互和参数共享实现图像压缩模型的高效任务适配。
- **创新点**: 将Mamba架构与跨层适配器结合，实现局部特征与全局依赖的协同捕获。
- **结果**: 在多个机器视觉任务上达到SOTA，参数开销降低72%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To reduce deployment cost and retraining overhead, adapting pretrained learned image compression (LIC) models to downstream machine vision tasks has attracted growing attention. However, existing methods typically insert fine-tuning modules independently into frozen backbones, lacking explicit mechanisms for cross-layer coordination. To address this limitation, we propose a novel framework named CrossMambaTuning, which integrates State Space Models with cross-layer interaction mechanisms for parameter-efficient fine-tuning. Specifically, we design an efficient Mamba adapter equipped with task-specific prompts and multi-scale branching to precisely capture both local features and global dependencies. Furthermore, we introduce a Scale-Invariant Cross-Layer Adapter (SICA) utilizing a parameter-sharing strategy to fuse task information across different scales and reduce redundancy. Extensive experiments demonstrate that CrossMambaTuning achieves state-of-the-art (SOTA) performance on multiple machine vision tasks, reducing parameter overhead by 72\% compared to SOTA methods. Code is available at https://github.com/rsr1123/CrossMambaTuning.

</details>

### 5. MaST: Motion-aware Sparse Pipeline for Lightweight Object Tracking **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2608.24365](https://arxiv.org/abs/2608.24365)  · [📄 PDF](https://arxiv.org/pdf/2608.24365)
- **作者**: Qingmao Wei, Fagui Liu, Dengke Zhang et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/TsingWei/MaST](https://github.com/TsingWei/MaST)
- **提交日期**: 2026-08-25 · **分类**: cs.CV
- **摘要（中）**: 针对Transformer跟踪器密集token处理导致计算开销大的问题，提出MaST稀疏跟踪框架，从token到box实现端到端稀疏化。通过注入轻量级运动先验细化注意力重要性分数，实现早期稳定的token剪枝，并设计原生稀疏预测头直接处理非结构化token。在多个基准上，MaST-tiny达到63.8 AUC，刷新轻量级跟踪器SOTA。
- **摘要（英）**: To reduce computational cost in Transformer trackers, MaST introduces a motion-aware sparse pipeline with early token pruning and a natively sparse prediction head. It injects a motion prior to refine importance scores and avoids dense reshaping. On benchmarks, MaST-tiny achieves 63.8 AUC, setting a new SOTA among lightweight trackers.
- **评估**: 该工作有效解决了稀疏跟踪中早期剪枝不稳定和预测头密集化的问题，对实时边缘部署有重要价值。
- **核心贡献**: 提出首个从token到box的端到端稀疏跟踪框架。
- **创新点**: 运动先验引导的早期token剪枝和原生稀疏预测头设计。
- **结果**: 在多个基准上刷新轻量级跟踪器SOTA，MaST-tiny AUC达63.8。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based object trackers are renowned for their strong performance, yet dense token processing often leads to prohibitive computational cost, limiting real-time deployment on edge devices. While recent works explore token pruning to reduce computation, they often stop short of an end-to-end sparse pipeline, as early-layer token scores can be noisy without a motion prior, and many trackers ultimately fall back to dense reshaping to feed the dense prediction head that partially negates the savings. We introduce Motion-aware Sparse Tracker (MaST), a sparse tracking framework that makes sparsity effective from tokens to boxes. First, MaST injects a lightweight motion prior to refine cross-attention-based importance scores, enabling earlier and more stable token reduction in the search region. Second, we introduce a natively sparse prediction head that operates directly on the retained unstructured tokens with a score-first, regress-once design, eliminating dense padding/reshaping and reducing redundant computation. Extensive experiments on multiple benchmarks demonstrate that MaST establishes new state of the art among lightweight trackers, where MaST-tiny attains 63.8 AUC on LaSOT and 80.1 SUC on TrackingNet, surpassing the prior best AsymTrack-S by +1.0 AUC and +2.2 SUC while running at 152 FPS on Jetson Nano, nearly twice as fast as AsymTrack-S at 88 FPS. Code is available at https://github.com/TsingWei/MaST.

</details>

### 6. Ring Forcing: Towards Precise Long-Term Memory for Autoregressive Video Diffusion **⭐⭐⭐⭐** (相关度: 60%, 质量: 0.82)

- **arXiv ID**: [2608.26794](https://arxiv.org/abs/2608.26794)  · [📄 PDF](https://arxiv.org/pdf/2608.26794)
- **作者**: Bowen Xue, Brandon Y. Feng, Chenguo Lin et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对自回归视频扩散模型在长时生成中缺乏鲁棒长期记忆，导致物体永久性和记忆容量不足的问题。②提出Ring Forcing框架，采用环形结构训练策略强制从远历史检索，并引入压缩和时间步组合策略扩展有效历史跨度至分钟级。③相比现有方法，平衡了历史严格遵循与生成多样性，并扩大记忆容量。④实验表明在长时视频生成中有效提升物体身份保持和上下文利用能力。
- **摘要（英）**: This paper addresses long-term memory deficiency in autoregressive video diffusion, focusing on object permanence and memory capacity. Ring Forcing uses a ring-structured training strategy for distant history retrieval and a compression-timestep composition to extend historical span. It improves identity preservation and context utilization in long video generation.
- **评估**: 该论文针对视频生成中的长期记忆瓶颈提出创新训练策略，对自动驾驶中的视频预测和场景理解有潜在启发。
- **核心贡献**: 提出Ring Forcing，增强自回归视频扩散的长期记忆能力。
- **创新点**: 环形训练策略与压缩组合扩展历史跨度。
- **结果**: 在长时视频生成中提升物体身份保持和上下文利用。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling video generation to long durations reveals a critical bottleneck: current models lack robust long-term memory. This deficiency can be studied along two critical aspects: object permanence, the ability to precisely reproduce the appearance of objects upon re-entry; and memory capacity, the ability to process ultra-long context and use information from distant history. Robust long-term memory requires both: object permanence without sufficient context handling limits the temporal scope, while long context length without permanence fails to maintain identity. To address this, we present Ring Forcing, an autoregressive video diffusion framework designed to robustly construct and precisely utilize long-term memory. Our ring-structured training strategy enforces retrieval from distant history, effectively reconciling the trade-off between strict historical adherence and generative diversity. To expand memory capacity, we introduce a compression and timestep composition strategy. Under fixed sequence length constraints, this method extends the effective historical span to minutes-long durations and achieves a comprehensive receptive field over the entire history. Furthermore, we present a sparse RoPE mechanism to enable flexible, scalable memory adaptation while fully exploiting pre-trained priors. Extensive experiments demonstrate that Ring Forcing achieves superior minutes-long coherence and object permanence, significantly outperforming state-of-the-art methods.

</details>

### 7. Efficient Training with Foresight: Multi-Token Auxiliary Supervision for Autoregressive Image Generation **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.25386](https://arxiv.org/abs/2608.25386)  · [📄 PDF](https://arxiv.org/pdf/2608.25386)
- **作者**: Guo Niu, Xiongfei Yao, Teng Wang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 该论文针对自回归图像生成中传统下一词预测的稀疏和短视监督、表征区分度不足及训练成本高的问题，提出了多令牌自回归（MTAR）统一训练框架。方法引入多令牌预测（MTP）缓解监督稀疏性，采用令牌级对比正则化（TCR）增强表征可分性，并加入语义丢弃（SD）加速训练，减少低信息令牌的冗余计算。该框架从预测目标、表征正则化和训练效率三方面改进，但主要面向图像生成，与自动驾驶感知的相关性较低。
- **摘要（英）**: This paper addresses sparse supervision and high training costs in autoregressive image generation, proposing MTAR with multi-token prediction, token-level contrastive regularization, and semantic dropping. These components improve prediction objectives, representation discriminability, and training efficiency. The framework enhances generation quality but has limited direct relevance to autonomous driving perception.
- **评估**: 该论文在图像生成训练效率上有创新，但主题与自动驾驶感知领域关联较弱。
- **核心贡献**: 提出了MTAR框架，统一改进自回归图像生成的监督、表征和效率。
- **创新点**: 结合多令牌预测、对比正则化和语义丢弃。
- **结果**: 提升了生成质量和训练效率，但未提供具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autoregressive (AR) image generation has shown strong potential for scalable high-fidelity synthesis by modeling images as discrete token sequences. However, traditional next token prediction (NTP) continues to suffer from sparse and myopic supervision, insufficiently discriminative representations, and high training cost caused by dense computation over the full token sequence. To address these issues, we propose multi-token autoregressive (MTAR), a unified training framework that improves autoregressive image generation from three aspects: prediction objectives, representation regularization, and training efficiency. Specifically, MTAR introduces multi-token prediction (MTP) to alleviate the sparsity and myopia of traditional NTP by imposing joint supervision on multiple future tokens; employs token-level contrastive regularization (TCR) to explicitly enhance the separability of sampled token representations and thereby improve representation discriminability; and incorporates semantic dropping (SD) as a semantics-aware training acceleration strategy to reduce redundant computation on low-information tokens while preserving informative learning signals. All three components are applied only during training and introduce no additional overhead during autoregressive inference. On ImageNet, MTAR achieves a better balance between generation quality and training efficiency. Compared with LlamaGen, MTAR achieves up to 0.95 lower FID and 39\% faster training. Moreover, even with only 1/3 of the training iterations, it still attains performance comparable to or better than the baseline, substantially reducing training time.

</details>

---

## Autonomous Driving

### 1. DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.26589](https://arxiv.org/abs/2608.26589)  · [📄 PDF](https://arxiv.org/pdf/2608.26589)
- **作者**: Wenxin Zhang, Hang Li, Zhiwei Xu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 针对图像与稀疏LiDAR点云之间模态差异导致跨模态对应学习困难的问题，提出了DPA-I2P，一种深度引导的投影对齐方法用于图像到点云配准。该方法通过射线条件度量深度编码（RMDE）和投影一致视觉提升（PVL）以结构化、几何感知方式利用深度和视觉线索，并采用跨模态查询剪枝（CQP）抑制不可靠查询以提高匹配稳定性。相比现有隐式对应学习方法，DPA-I2P在KITTI上分别将RTE和RRE降低了45.0%和55.6%，在nuScenes上也验证了有效性。
- **摘要（英）**: DPA-I2P tackles image-to-point-cloud registration in autonomous driving by introducing depth-guided projective alignment with Ray-Conditioned Metric Depth Encoding and Projection-Consistent Vision Lifting. It also employs Cross-Modal Query Pruning to suppress unreliable queries, improving matching stability. On KITTI, it reduces RTE and RRE by 45.0% and 55.6% over the strongest implicit baseline, demonstrating significant gains.
- **评估**: 该论文针对自动驾驶定位任务提出了有效的深度引导对齐方法，实验改进显著，实用性强。
- **核心贡献**: 提出DPA-I2P，通过深度引导投影对齐提升图像-点云配准精度。
- **创新点**: 利用射线条件深度编码和投影一致提升实现几何感知的跨模态对齐。
- **结果**: 在KITTI上RTE和RRE分别降低45.0%和55.6%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-to-Point Cloud Registration aims to estimate the camera pose of a given image within a 3D scene point cloud, which is a fundamental task in autonomous driving and large-scale outdoor localization. Recent implicit correspondence learning methods have improved registration performance by learning cross-modal alignment in an end-to-end framework, leading to more accurate camera pose estimation. However, due to the inherent modality discrepancy between images and sparse LiDAR point clouds, reliable cross-modal correspondence learning remains challenging. To address this issue, we propose Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration (DPA-I2P). Unlike naive depth or feature concatenation, Ray-Conditioned Metric Depth Encoding (RMDE) and Projection-Consistent Vision Lifting (PVL) exploit depth and visual cues in a structured, geometry-aware manner. In addition, Cross-Modal Query Pruning (CQP) suppresses unreliable queries during early refinement to improve matching stability. Experiments on KITTI and nuScenes demonstrate the effectiveness of the proposed method. On KITTI, DPA-I2P reduces RTE and RRE by 45.0% and 55.6% over the strongest implicit baseline, respectively. On nuScenes, DPA-I2P also improves registration accuracy over the evaluated baselines, suggesting better transferability to different driving scenes.

</details>

### 2. Variance-Guided Spatial Attention Fusion for Robust End-to-End Driving under Asymmetric Sensor Degradation **⭐⭐⭐⭐** (相关度: 90%, 质量: 0.8)

- **arXiv ID**: [2608.24366](https://arxiv.org/abs/2608.24366)  · [📄 PDF](https://arxiv.org/pdf/2608.24366)
- **作者**: Weizhi Tao, Zengwang Jin, Xiao Wang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.RO
- **摘要（中）**: 针对端到端多模态驾驶在非对称传感器退化（如单模态或局部区域损坏）下脆弱的问题，提出Variance-Guided Spatial Attention Fusion (VG-SAF)，通过密集异方差可靠性估计作为可解释空间门控。框架包含物理增强器模拟传感器故障并提供密集监督、模态专家通过跨分支蒸馏预测逐像素可靠性、以及混合注意力机制抑制不可靠单元并仲裁模态，提升鲁棒性。
- **摘要（英）**: To address fragility under asymmetric sensor degradation in end-to-end multimodal driving, VG-SAF uses dense heteroscedastic reliability estimates as interpretable spatial gates. It couples a physically grounded augmentor for dense supervision, modality-specific experts with cross-branch distillation for per-pixel reliability, and hybrid attention to suppress unreliable cells, enhancing robustness.
- **评估**: 针对自动驾驶多模态融合的鲁棒性问题，方法新颖且实用，与用户领域高度相关。
- **核心贡献**: 提出方差引导的空间注意力融合，应对非对称传感器退化。
- **创新点**: 利用密集可靠性监督和物理故障模拟。
- **结果**: 提升端到端驾驶在传感器退化下的鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end multimodal driving has progressed rapidly by fusing camera and LiDAR streams. Existing pipelines remain fragile under asymmetric sensor degradation, where either an entire modality or only a localized region is corrupted while other regions remain useful. The key difficulty is not simply to add an uncertainty head, but to obtain dense reliability supervision, calibrate this reliability against physical fault severity, and use it before unreliable features bias the planner. We propose Variance-Guided Spatial Attention Fusion (VG-SAF), in which dense heteroscedastic reliability estimates act as interpretable spatial gates. The framework couples three components. First, a physically grounded augmentor simulates representative camera and LiDAR failures and emits a continuous spatial mask, providing dense supervision without additional annotation. Second, modality-specific experts predict per-pixel reliability scales through cross-branch dense distillation in log space, enforcing a monotone severity-to-scale response. Third, calibrated reliability maps drive a hybrid attention mechanism that suppresses unreliable cells with a local spatial gate and arbitrates between modalities through a cross-modal trust softmax. A Laplace uncertainty head emits a systemic waypoint uncertainty scale that signals severe or combined sensor degradation, including severities outside the training ranges. On the CARLA Longest6 benchmark, VG-SAF consistently improves closed-loop robustness over the baselines across camera-only, LiDAR-only, and joint degradation regimes, as measured by driving score, route completion, and infraction score.

</details>

### 3. CARE: Camera-Residual Reserves for First Sightings in Adaptive LiDAR Sensing **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.8)

- **arXiv ID**: [2608.24282](https://arxiv.org/abs/2608.24282)  · [📄 PDF](https://arxiv.org/pdf/2608.24282)
- **作者**: Jiachen Gong, Yun Li, Ehsan Javanmardi et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.RO
- **摘要（中）**: ①针对自适应LiDAR扫描中历史驱动策略无法及时检测新物体、随机采样无感知、相机引导策略浪费预算的问题。②提出CARE，一种无训练分配规则，为当前相机检测中轨迹预测无法解释的方向预留部分射线预算，其余遵循历史策略，未用储备返回随机底限。③相比现有方法，CARE无需训练，结合相机检测和轨迹预测，提高新物体首次发现率。④在nuScenes上150场景、4148事件评估，测量历史驱动扫描的首次发现损失，并引入严格因果变体，结果表明CARE有效降低新物体漏检。
- **摘要（英）**: This paper proposes CARE, a training-free allocation rule for adaptive LiDAR scanning that reserves ray budget for camera detections unexplained by track forecasts, improving first-sighting of new objects. Evaluated on nuScenes, it reduces detection loss compared to history-driven policies, enhancing efficiency in autonomous driving.
- **评估**: 该工作针对自适应LiDAR感知，与自动驾驶高度相关，方法简洁有效，实验设计严谨。
- **核心贡献**: 提出CARE分配规则，结合相机检测和轨迹预测，提升新物体首次发现率。
- **创新点**: 无训练预算预留机制，利用相机残差信息。
- **结果**: 在nuScenes上降低首次发现损失，提高检测效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adaptive LiDAR scanning concentrates a limited sensing budget on regions of interest predicted from past object tracks, lowering data volume in autonomous driving while maintaining detection accuracy. However, existing scanning policies face three challenges. First, history-driven approaches depend on past tracks, so unseen objects are detected late or missed. Second, random or uniform sampling outside the predicted regions has no awareness of where new objects appear. Third, camera-guided alternatives spend budget on all camera detections, resampling objects already covered, costing recall in crowded scenes and range when budgets are scarce. This paper introduces the CAmera-REsidual reserve (CARE), a training-free allocation rule that reserves part of a fixed ray budget for the directions of current camera detections that the track forecasts cannot explain; the rest follows the base history policy, and unused reserve returns to a random floor. The paper makes three contributions. First, a leakage-free ray-budget evaluation on nuScenes (150 scenes, 4,148 events) measuring the first-sighting loss of history-driven scanning, with a strict-causal variant using the preceding keyframe. Second, CARE raises first-sighting recall by 5.2, 5.2, and 4.3 points at 10%, 20%, and 35% budgets over the history policy, with paired intervals excluding zero; the camera cue drives this gain, and the first-sighting versus overall trade-off is a budget-dependent Pareto choice. Third, a safety-bounded forgetting module that releases budget from receding or static tracks beyond a speed-dependent guard distance; at tight budgets, forgetting without the guard significantly harms near-field recall, so the guard is what keeps it safe. The pipeline runs end to end on a real vehicle and, in closed-loop simulation, detects an occluded pedestrian earlier and brakes more reliably than history-driven scanning.

</details>

### 4. Beyond the Proving Ground: Independent Public-Road Testing of Assisted Lane Change Systems using LiDAR **⭐⭐⭐** (相关度: 70%, 质量: 0.65)

- **arXiv ID**: [2608.26669](https://arxiv.org/abs/2608.26669)  · [📄 PDF](https://arxiv.org/pdf/2608.26669)
- **作者**: Marcello Cellina, Akos Kriston, Antonio Migneco et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.RO, cs.CV
- **摘要（中）**: ①这篇论文针对辅助车道变更系统在公共道路上独立测试的挑战，因为试验场场景可能无法反映真实驾驶复杂性。②提出了一种使用LiDAR检测和跟踪系统的独立测试方法，在法国A31高速公路上进行了测试，覆盖不同车距和速度组合。③相比依赖制造商合作的测试，该方法无需地理围栏，确保了评估独立性。④在27个预定义车道变更操作中，18个完成，9个被抑制，其中6个系统允许的操作未满足UNECE法规最低距离要求。
- **摘要（英）**: This paper addresses the challenge of independently testing assisted lane change systems on public roads. A LiDAR-based methodology was deployed on a French motorway, assessing system compliance with UNECE regulations. Results showed 6 of 27 maneuvers violated minimum distance requirements, highlighting safety gaps.
- **评估**: 该论文提供了实用的独立测试方法，对自动驾驶系统安全评估有参考价值，但技术深度一般。
- **核心贡献**: 提出了基于LiDAR的公共道路辅助车道变更系统独立测试方法。
- **创新点**: 利用实时动态GNSS和LiDAR实现无制造商协作的合规性评估。
- **结果**: 发现部分系统操作不符合法规要求。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Testing of commercial Advanced Driver Assistance Systems is essential to ensure safety and compliance during type approval and in service operation. However, proving ground scenarios may not reflect real world driving complexity, while geo fencing can require manufacturer collaboration and limit assessment independence. This work presents a methodology for independently testing Assisted Lane Change systems on public roads. A campaign on the A31 French motorway used a test vehicle equipped with a LiDAR based vehicle detection and tracking system. Tests covered combinations of inter vehicle distance and speed between the test vehicle and the take over vehicle. Real time kinematic global navigation satellite system receivers assessed detection and tracking performance. Recorded lane change trajectories were compared with the lane change suppression requirements of UNECE Regulation Number 79. Of 27 predefined lane change manoeuvres, 18 were completed and 9 suppressed. In 6 cases, the system allowed manoeuvres that did not meet regulatory minimum distance requirements. In 3 cases, the deviation remained statistically significant after accounting for measurement uncertainty. To the authors knowledge, this is the first public road campaign designed to assess Assisted Lane Change compliance with Regulation Number 79 safety distance requirements. The results demonstrate the suitability of LiDAR based sensing for this purpose. The methodology can support market surveillance and future regulatory revisions by revealing real world behaviours not covered by approval procedures.

</details>

---

## Open-set Detection

### 1. Text-to-seed generation: Training-free open-vocabulary seeded semantic segmentation via re-purposing diffusion as text-guided seed generator **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2608.26624](https://arxiv.org/abs/2608.26624)  · [📄 PDF](https://arxiv.org/pdf/2608.26624)
- **作者**: Kumju Jo, Heesun Jung, Sungyong Baik
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对开放词汇语义分割（OVSS）中SAM独立性能有限，且依赖粗掩码细化不可靠的问题。②提出了Text-to-Seed（T2S），一个无需训练的框架，利用Stable Diffusion的文本-区域对应生成注意力种子点，再作为SAM的点提示生成完整掩码。③相比已有工作，该方法将OVSS重构为种子定位和区域扩展，避免了粗掩码误差的传播。④在标准OVSS基准上取得了强性能，无需任务特定训练或额外标注。
- **摘要（英）**: This paper addresses the limited performance of SAM in open-vocabulary semantic segmentation by proposing Text-to-Seed (T2S), a training-free framework that uses Stable Diffusion to generate seed points from text queries. These seeds serve as point prompts for SAM, enabling reliable region expansion without coarse mask refinement. T2S achieves strong performance on standard benchmarks without task-specific training.
- **评估**: 该论文对开放集分割有重要贡献，方法简洁有效，与自动驾驶中的开放世界感知相关。
- **核心贡献**: 提出了T2S框架，利用扩散模型生成种子点，提升SAM的开放词汇分割能力。
- **创新点**: 将OVSS重构为文本引导的种子定位和区域扩展，无需训练。
- **结果**: 在标准OVSS基准上取得强性能，无需额外标注。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation (OVSS) aims to segment image regions corresponding to arbitrary text queries. Although the Segment Anything Model (SAM) is a powerful foundation model for segmentation, its standalone performance on OVSS remains limited. Existing methods therefore often use SAM to refine coarse masks predicted by other models, but this strategy is unreliable when the initial masks are inaccurate. In this work, we argue that more reliable segmentation can be achieved by exploiting SAM as a region expansion module guided by accurate object points (i.e., seeds) rather than inaccurate coarse masks. Inspired by classical seeded segmentation, we reformulate OVSS as text-guided seed localization followed by seed-based region expansion. To realize this idea, we propose Text-to-Seed (T2S), a training-free framework that leverages the text-to-region correspondence of Stable Diffusion to generate attention-based seed points for target categories described by text. These sparse seeds are then used as point prompts for SAM to produce full object masks. Without task-specific training or additional annotations, T2S achieves strong performance on standard OVSS benchmarks, demonstrating the effectiveness of combining semantic grounding with seed-driven spatial segmentation.

</details>

### 2. OpenVeinNet: Robust Open-Set Finger Vein Verification with Dynamic Snake Convolution and Graph Learning **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.25515](https://arxiv.org/abs/2608.25515)  · [📄 PDF](https://arxiv.org/pdf/2608.25515)
- **作者**: Sushrut Patwardhan, Raghavendra Ramachandra
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对指静脉验证在开放集场景下测试身份未见且需拒绝未注册样本的挑战，提出OpenVeinNet，结合动态蛇形卷积提取局部曲线结构，图卷积建模长程拓扑关系，并引入质心角度混合损失增强嵌入空间的类内紧凑性和类间角度分离。在五个公开数据集上采用留一数据集训练评估，验证跨数据集鲁棒性。
- **摘要（英）**: To address open-set finger vein verification where test identities are unseen, OpenVeinNet combines dynamic snake convolution for local curvilinear features and graph convolution for long-range topology, with a centroid angular hybrid loss for discriminative embeddings. It is evaluated via leave-one-dataset-out training on five public datasets.
- **评估**: 开放集验证方法有借鉴意义，但生物识别领域与自动驾驶感知关联度中等。
- **核心贡献**: 提出开放集指静脉验证框架，结合动态卷积和图学习。
- **创新点**: 质心角度混合损失提升嵌入判别力。
- **结果**: 在跨数据集评估中表现鲁棒。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Finger vein verification is a promising biometric modality for secure authentication because vascular patterns are internal, difficult to observe externally, and relatively resistant to presentation attacks. However, reliable verification remains challenging in open-set settings, where test identities are unseen during training and non-enrolled probes must be rejected at inference. This paper presents OpenVeinNet, a finger vein verification framework designed for cross-dataset and open-set evaluation. The proposed model combines Dynamic Snake Convolution with graph-based feature modelling. Dynamic Snake Convolution extracts local curvilinear and tubular vein structures using adaptive sampling, while the graph convolutional backbone models long-range topological relationships between vein regions. To improve the discriminative quality of the embedding space, we introduce a Centroid Angular Hybrid Loss, which jointly encourages intra-class compactness and inter-class angular separation for cosinesimilaritybased verification. Experiments are conducted on five public finger vein datasets: FV-300, MMCBNU, FV-USM, PolyU, and VERA. The method is evaluated using leaveonedatasetout training under both enrolmentbased unknownrejection and fullsubject verification protocols, and is compared with handcrafted and recent deep learning-based baselines. The results show that OpenVeinNet achieves strong cross-dataset generalisation, consistently low equal error rates, and competitive true accept rates at fixed false accept rate operating points. Ablation studies further confirm the individual and combined contributions of adaptive tubular feature extraction, graph-based relational modelling, and the proposed loss function. These findings indicate that explicitly modelling local vein geometry, global vascular relationships, and angularly compact embeddings is effective for openset finger vein verification.

</details>

### 3. TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.75)

- **arXiv ID**: [2608.25935](https://arxiv.org/abs/2608.25935)  · [📄 PDF](https://arxiv.org/pdf/2608.25935)
- **作者**: Yuqiang Lin, Yan Shi, Sam Lockyer et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/siri-rouser/TAU-Agent](https://github.com/siri-rouser/TAU-Agent)
- **提交日期**: 2026-08-26 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对交通异常理解（TAU）中检测、推理和解释异常事件的需求，提出了TAU-Agent，一个基于智能体检索增强的框架。中央检索智能体协调视频字幕工具和开放词汇跟踪工具，检索与查询相关的证据，包括字幕、时间间隔和物体轨迹，然后提供给微调后的视觉语言模型进行推理和答案生成。在AI City Challenge 2026的域内和域外基准上，分别取得Track 3得分0.6779、Track 7得分0.3998和Track 8得分67.9275，排名第二、第十二和第五。
- **摘要（英）**: To address traffic anomaly understanding, this paper proposes TAU-Agent, an agentic retrieval-augmented framework that orchestrates video captioning and open-vocabulary tracking tools to retrieve evidence for a fine-tuned VLM. It achieves scores of 0.6779 on Track 3, 0.3998 on Track 7, and 67.9275 on Track 8 in the AI City Challenge 2026, ranking second, twelfth, and fifth respectively.
- **评估**: 该论文将智能体检索增强与视觉语言模型结合用于交通异常理解，对自动驾驶场景的视频感知有较高参考价值。
- **核心贡献**: 提出了TAU-Agent框架，通过检索增强实现交通异常视频的检测与解释。
- **创新点**: 利用多工具协同的检索智能体动态选择证据，提升VLM推理准确性。
- **结果**: 在AI City Challenge 2026多个赛道取得领先排名。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traffic Anomaly Understanding (TAU) requires models and systems to detect, reason about, and explain anomalous events in transportation videos. To address this challenge, we propose TAU-Agent, an agentic retrieval-augmented framework for traffic anomaly understanding. Given a task query, a central retrieval agent orchestrates two visual perception tools, namely a Video Captioning Tool and an Open-Vocabulary Tracking Tool, to retrieve and select query-relevant evidence, including captions, temporal intervals, and object trajectories. The selected evidence, together with sampled video frames and the input query, is provided to a supervised fine-tuned vision-language model for final reasoning and answer generation. We evaluate TAU-Agent on both the in-domain and the out-of-domain benchmarks from the AI City Challenge 2026. TAU-Agent achieves scores of 0.6779 on Track 3, 0.3998 on Track 7, and 67.9275 on Track 8, ranking second, twelfth, and fifth, respectively. Code is available at: https://github.com/siri-rouser/TAU-Agent.

</details>

### 4. CloSeR: Unified Relational Distillation from Closed-Set Teachers for Category Discovery **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.8)

- **arXiv ID**: [2608.25692](https://arxiv.org/abs/2608.25692)  · [📄 PDF](https://arxiv.org/pdf/2608.25692)
- **作者**: Yuanpei Liu, Zhenqi He, Jialu Tang et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: ①针对广义类别发现（GCD）中闭集识别与开集发现耦合训练导致目标冲突、预测偏差以及预训练表示语义几何被扰动的问题。②提出CloSeR框架，通过注入闭集关系知识到GCD训练中：先构建领域自适应闭集教师（冻结基础模型骨干，仅微调轻量块级适配器），再通过统一关系蒸馏（URD）将教师知识转移到下游GCD，蒸馏互补的全局和局部关系。③相比现有GCD方法，解耦闭集与开集目标，保留预训练先验，降低训练成本。④摘要未提供具体数值，但方法设计合理。
- **摘要（英）**: This paper addresses the objective conflict and biased predictions in Generalized Category Discovery (GCD) caused by coupled closed-set recognition and open-set discovery training. It proposes CloSeR, a plug-and-play framework that injects closed-set relational knowledge via a domain-adapted teacher with lightweight adapters and Unified Relational Distillation (URD). This decouples objectives and preserves pretrained priors, improving GCD training, though specific metrics are not reported in the abstract.
- **评估**: 针对GCD中关键耦合问题提出解耦方案，方法简洁且具有通用性，对开放世界感知有参考价值。
- **核心贡献**: 提出CloSeR框架，通过闭集关系蒸馏解耦GCD中的闭集与开集学习。
- **创新点**: 利用冻结骨干的轻量适配器教师和统一关系蒸馏，避免目标冲突。
- **结果**: 摘要未给出具体数据，但方法设计具有潜力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalized Category Discovery (GCD) is an intriguing open-world problem that has garnered increasing attention: given partially labelled data, the goal is to correctly recognize known classes while discovering coherent novel categories from unlabelled samples. Recent GCD methods typically adapt foundation models by jointly optimizing supervised classification and unsupervised discovery objectives on mixed labelled and unlabelled data. While effective, this coupled training can entangle closed-set recognition and open-set discovery, leading to objective conflict and biased predictions, and may disturb the semantic geometry of pretrained representations under limited labels and noisy pseudo-labels. We propose CloSeR, a simple plug-and-play framework that injects Closed-Set Relational knowledge into GCD training. CloSeR first builds a domain-adapted closed-set teacher by tuning lightweight block-wise adapters on labelled known-class data while keeping the foundation model backbone frozen, thereby preserving pretrained priors at low training cost. It then transfers the teacher's knowledge to downstream GCD via Unified Relational Distillation (URD), which distills complementary global sample-to-prototype relations to anchor known-class semantics and local sample-to-sample relations to preserve neighborhood structure, using separate feature pathways to reduce optimization interference. CloSeR is head-agnostic and readily integrates with both parametric and non-parametric GCD methods. Extensive experiments with DINO and DINOv2 backbones on six benchmarks (CIFAR-10/100, ImageNet-100, CUB, Stanford-Cars, and FGVC-Aircraft) show consistent gains over GCD baselines, achieving state-of-the-art performance. Project page: https://visual-ai.github.io/closer/

</details>

---

## 3D Detection

### 1. Generative Semantic Scene Completion **⭐⭐⭐⭐⭐** (相关度: 95%, 质量: 0.9)

- **arXiv ID**: [2608.26737](https://arxiv.org/abs/2608.26737)  · [📄 PDF](https://arxiv.org/pdf/2608.26737)
- **作者**: Shi Chen, Weifeng Ge
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV, cs.LG, cs.RO
- **摘要（中）**: ①这篇论文针对户外LiDAR语义场景补全（SSC）中目标体积仅1%被观测和类别不平衡超过7000倍的问题。②将SSC重构为生成式语义场景补全（GSSC），采用单一离散扩散公式，包含配对稀疏-稠密场景合成（PS³）、语义引导生成场景补全（SGSC）和结构化源离散扩散（S²D²）三种角色。③相比现有SSC方法，GSSC通过生成方式从源头解决长尾分布，且S²D²无需重新训练即可提升外部SSC基线的性能。④在SemanticKITTI隐藏测试集上，单步无测试时增强达到38.8% mIoU，据作者称是最佳结果。
- **摘要（英）**: This paper addresses outdoor LiDAR semantic scene completion with sparse observations and extreme class imbalance. GSSC recasts SSC as a generative problem using discrete diffusion, with paired synthesis and refinement roles. It achieves 38.8% mIoU on SemanticKITTI hidden test, surpassing existing baselines without retraining.
- **评估**: 该论文在Occupancy和SSC领域具有突破性，生成式方法有效解决了数据稀疏和长尾问题，对自动驾驶感知有重要价值。
- **核心贡献**: 提出了生成式语义场景补全框架，统一了合成、生成和细化。
- **创新点**: 将离散扩散应用于SSC，实现无需重训练的外部基线提升。
- **结果**: 在SemanticKITTI上达到38.8% mIoU，为当前最优。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Outdoor LiDAR semantic scene completion (SSC) recovers a dense semantic voxel grid from a scan observing 1% of the target volume, under class imbalance beyond 7,000x. We recast SSC as generative semantic scene completion (GSSC): a single discrete-diffusion formulation in three roles. First, paired sparse-dense scene synthesis (PS$^3$) generates matched sparse LiDAR observations with their dense semantic completions, addressing the long tail at its source and yielding the PS$^3$-SemanticKITTI corpus we train on alongside SemanticKITTI. Second, semantic-guided generative scene completion (SGSC) generates the scene from noise with multinomial discrete diffusion, conditioned on the sparse scan through a bird's-eye-view semantic map and a sparse 3D feature stream. Third, the same framework instead refines an existing completion in one flow-matching step: structured source discrete diffusion (S$^2$D$^2$). S$^2$D$^2$ improves the mIoU of SGSC's own output and every external SSC base tested, without base retraining or test-time adaptation. On the strongest base, one step without test-time augmentation reaches 38.8% mIoU on the SemanticKITTI hidden test. To our knowledge that is the best causal, single-sweep, single-sample result on that leaderboard, +2.1 pp over the previous best published score under the same restriction. Four correction steps with eight-view test-time augmentation reach 39.2%, outside that restriction.

</details>

### 2. Steer the Sampling, Not the Kernel Grid: Geometry-Guided Sampling Operator for Volumetric Segmentation **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.25819](https://arxiv.org/abs/2608.25819)  · [📄 PDF](https://arxiv.org/pdf/2608.25819)
- **作者**: Sizhe Wang, Himashi Peiris, Zhaolin Chen
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-26 · **分类**: cs.CV
- **摘要（中）**: 针对3D分割中细长结构（如血管）因下采样和固定网格卷积导致模糊或断裂的问题，提出几何引导的采样算子，在特征细化和分辨率降低时预测局部方向和步长，沿方向对称采样并生成几何边界线索。跨尺度一致性对齐编码器-解码器特征。在BraTS和MSD Hepatic Ves等数据集上，替换U-Net中所有步长1和2算子带来一致改进。
- **摘要（英）**: To address blurring and disconnection of thin structures in 3D segmentation, a geometry-guided sampling operator predicts local orientation and step sizes, sampling symmetrically along directions. Cross-scale consensus aligns features at skip connections. Replacing all stride operators in 3D U-Net yields consistent improvements on BraTS and MSD datasets.
- **评估**: 该工作对医学图像细结构分割有改进，但自动驾驶领域相关性有限。
- **核心贡献**: 提出几何引导的采样算子替代固定网格卷积，改善细长结构分割。
- **创新点**: 通过预测采样方向和步长，而非变形卷积核，实现特征细化和降采样。
- **结果**: 在BraTS和MSD等数据集上一致提升分割性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D segmentation is central to quantitative lesion assessment and anatomy mapping for clinical planning and follow-up. Thin, elongated, and fine anatomical/pathological structures (e.g., vessels) are a particularly challenging case: a one-voxel boundary error can disconnect a branch and change clinically relevant topology. In encoder-decoder networks (e.g., U-Net), repeated downsampling and fixed-grid convolution blur or alias fine structures and weaken orientation cues, so early mistakes propagate across scales. We propose a geometry-guided local operator that steers where features are sampled, rather than deforming convolutional kernels, under a single formulation for both feature refinement (stride 1) and resolution reduction (stride > 1). At each voxel, it predicts a local orientation and bounded step sizes, samples symmetrically along these directions, and transforms paired samples into compact geometric and boundary cues with lightweight mixing; a cross-scale consensus aligns encoder and decoder features at skip connections to reduce geometric mismatch. Replacing all stride 1 and stride 2 operators in a 3D U-Net yields consistent improvements on BraTS, MSD Hepatic Vessel, and TDSC-ABUS, with notably better boundary metrics (e.g., BraTS Dice 86.1 to 88.9, HD95 7.1 to 6.2; TDSC-ABUS HD95 39.1 to 27.8) while reducing parameters from 2.3M to 0.8M. We further demonstrate that the operator can be integrated into other backbones (e.g., nnU-Net, Swin-UNETR, and MedNeXt) without changing their macro-architectures while providing consistent performance gains.

</details>

### 3. Luce: Relightable Gaussians for 3D Asset Generation **⭐⭐⭐** (相关度: 40%, 质量: 0.75)

- **arXiv ID**: [2608.23943](https://arxiv.org/abs/2608.23943)  · [📄 PDF](https://arxiv.org/pdf/2608.23943)
- **作者**: Mayank Singh, Michele Stoppa, Alvise Memo et al. (10 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.AI, cs.GR
- **摘要（中）**: 针对图像到3D生成中需要同时捕捉几何和外观并支持重光照的问题，提出Luce表示，在体素化多模态高斯云中统一几何和PBR材质，每种模态使用专用高斯原语。变分自编码器压缩到材质感知潜空间，整流流Transformer从单图生成潜码。在Toys4K上，FID比最强基线提升28%，在AI生成图像基准上CLIP对齐分数达0.8519。
- **摘要（英）**: For image-to-3D generation with relighting support, Luce unifies geometry and PBR materials in a voxelized multimodal Gaussian cloud with dedicated primitives per modality. A VAE compresses to a material-aware latent, and a rectified-flow transformer generates it from a single image. On Toys4K, FID improves by 28% over the strongest baseline, with CLIP alignment of 0.8519 on AI-generated images.
- **评估**: 该工作在3D资产生成领域有创新，但与自动驾驶感知核心方向相关性较低。
- **核心贡献**: 提出统一几何和PBR材质的可重光照3D表示。
- **创新点**: 多模态高斯云和材质感知潜空间设计。
- **结果**: 在Toys4K上FID提升28%，CLIP对齐分数优于基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-fidelity image-to-3D generation requires a 3D representation that captures both geometry and appearance. To support relighting and integration into standard rendering pipelines, the representation should include physically based rendering (PBR) modalities such as albedo, metallic-roughness, and surface normals. We propose Luce, a 3D representation that unifies geometry and PBR materials within a voxelized multimodal Gaussian cloud, using dedicated Gaussian primitives for each modality. A variational autoencoder compresses this representation into a unified material-aware latent space. A rectified-flow transformer generates this latent from a single image, conditioned on multi-layer features from a pretrained image encoder that preserve both semantic context and fine spatial detail. The latent then decodes into relightable PBR Gaussians and an optional textured mesh with a tangent-space normal map. On Toys4K, Luce achieves state-of-the-art single-image-to-3D generation, improving FID by 28% over the strongest baseline. We further introduce a benchmark of AI-generated images, on which Luce improves the CLIP image-alignment score over the best baseline (0.8519 vs. 0.8299). Luce generates relightable, geometrically accurate, and materially faithful assets that preserve fine details such as text, logos, and inscriptions.

</details>

---

## Continual Learning

### 1. Parameter Efficient Continual Learning for Sparse Event-Based Transformers **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.75)

- **arXiv ID**: [2608.26720](https://arxiv.org/abs/2608.26720)  · [📄 PDF](https://arxiv.org/pdf/2608.26720)
- **作者**: Vaishnavi Nagabhushana, Kartikay Agrawal, Ayon Borthakur
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: ①针对稀疏事件驱动Transformer在持续学习中的参数效率和性能问题，提出sLoTh框架。②冻结骨干，仅更新低秩注意力更新（seLoRA）和共享神经元阈值，参数更新少于1%，无需回放缓冲区。③在CIFAR-100、Tiny-ImageNet、ImageNet-100和ImageNet-R上，最多100任务，实现无回放的类增量学习。④性能与有回放方法竞争，计算开销降低约6倍。
- **摘要（英）**: This paper introduces sLoTh, a parameter-efficient continual learning framework for sparse event-based vision transformers. It freezes the backbone and updates less than 1% parameters via low-rank attention and threshold modulation, without replay buffers. Experiments on multiple benchmarks with up to 100 tasks show competitive rehearsal-free performance and ~6x compute reduction.
- **评估**: 该论文结合持续学习、稀疏Transformer和事件驱动，与自动驾驶边缘部署和增量感知高度相关，方法创新且实验充分。
- **核心贡献**: 提出稀疏事件Transformer的持续学习框架sLoTh。
- **创新点**: 利用低秩注意力和阈值调制实现超低参数更新。
- **结果**: 无回放性能竞争，计算开销降低6倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robotic and edge intelligence systems operate in dynamic environments where data arrives continuously, requiring models to adapt while preserving previously learned knowledge under strict memory and energy constraints. While parameter-efficient fine-tuning has shown promise for continual learning with vision transformers, conventional architectures rely on dense computation and remain costly for real-world deployment. Sparse event-based vision transformers provide energy-efficient event-driven computation, yet their continual learning capabilities remain largely unexplored. We here introduce sLoTh, a parameter-efficient continual learning framework for pretrained sparse event-based (spiking) vision transformers. sLoTh freezes the backbone and restricts plasticity to scalable-efficient low-rank attention updates (seLoRA) and shared neuronal threshold modulation, enabling adaptation without replay buffers by updating less than 1% of model parameters. Experiments across CIFAR-100, Tiny-ImageNet, ImageNet-100, and ImageNet-R with up to 100 tasks demonstrate competitive rehearsal-free performance in class-incremental learning and online continual learning, while enabling approximately 6.5x lower energy consumption than conventional dense vision transformers.

</details>

### 2. Geo-LoRA: Geometry-Aware Subspace Evolution for Low-Rank Adaptation in Continual Learning **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.7)

- **arXiv ID**: [2608.26960](https://arxiv.org/abs/2608.26960)  · [📄 PDF](https://arxiv.org/pdf/2608.26960)
- **作者**: Yibo Feng
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-27 · **分类**: cs.CV
- **摘要（中）**: 针对无重放类增量学习中LoRA适配器低秩子空间缺乏几何控制导致共享表示不稳定和任务特定更新重复占用旧方向的问题，提出了Geo-LoRA框架。该方法通过子空间投影保持（SPP）约束共享分支在Grassmann流形上的平滑轨迹，自适应核心-松弛对齐（ACSA）分解主残差成分，以及中位数校准块重叠（MCBO）惩罚任务特定分支的过度复用，从而调节所有LoRA子空间的演化。相比现有LoRA方法，Geo-LoRA在不引入额外适配器类型的情况下，从几何角度系统性地平衡稳定性和可塑性。摘要未提供具体实验数据，但提供了理论上的几何约束框架。
- **摘要（英）**: Geo-LoRA addresses rehearsal-free class-incremental learning by introducing geometry-aware constraints on LoRA subspace evolution. It uses Subspace Projection Preservation and Adaptive Core-Slack Alignment for shared branches, and Median-Calibrated Block Overlap for task-specific branches, ensuring smooth trajectories and preventing subspace crowding. This principled approach balances stability and plasticity without extra adapter types, though quantitative results are not specified in the abstract.
- **评估**: 该论文从几何角度为LoRA持续学习提供了新视角，理论框架扎实，但缺乏实验验证。
- **核心贡献**: 提出Geo-LoRA，通过几何约束调节LoRA子空间演化以提升持续学习性能。
- **创新点**: 利用Grassmann流形和统计约束实现子空间演化的几何控制。
- **结果**: 摘要未提供具体数据，但理论上提升了稳定性与可塑性平衡。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rehearsal-free class-incremental learning (CIL) with LoRA adapters remains challenging because the low-rank subspaces updated across tasks evolve without geometric control, causing unstable shared representations and repetitive collapse of task-specific updates into previously occupied directions. We introduce Geo-LoRA, a geometry-aware framework that explicitly regulates how low-rank subspaces, both shared and task-specific, evolve during continual learning. For the shared branch, Subspace Projection Preservation (SPP) constrains consecutive updates to follow smooth trajectories on the Grassmann manifold, and Adaptive Core-Slack Alignment (ACSA) decomposes transitions into principal and residual components, aligning the former while modulating the latter to balance stability and plasticity. For the task-specific branch, Median-Calibrated Block Overlap (MCBO) imposes a statistical constraint via normalized projection overlap, penalizing excessive reuse to mitigate subspace crowding. These constraints jointly regulate the evolution of all LoRA subspaces across layers and tasks without introducing additional adapter types beyond standard LoRA. Geo-LoRA provides a principled geometric formulation for continual low-rank adaptation and consistently achieves state-of-the-art performance across multiple benchmark datasets and different task lengths.

</details>

---

## BEV

### 1. Lightweight Machine Learning-Driven Monocular Sidewalk Path Extraction for Embedded Micromobility Navigation **⭐⭐⭐** (相关度: 60%, 质量: 0.75)

- **arXiv ID**: [2608.25178](https://arxiv.org/abs/2608.25178)  · [📄 PDF](https://arxiv.org/pdf/2608.25178)
- **作者**: Lkhanaajav Mijiddorj, Yang Yan, Tyler Beringer et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-25 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对微移动导航中在紧凑低功耗硬件上、杂乱且地图稀疏环境下进行人行道级路径提取的感知与规划问题。②提出单目视觉流水线，经过三次设计迭代（骨架图基线、距离变换走廊规划、轻量图像空间架构），并系统比较了BEV和图像空间域的五种路径规划方法；使用OneFormer Swin-L伪标签的半监督教师-学生框架训练紧凑SegFormer-B0学生模型。③相比基线，轻量模型在速度和精度上均有提升，图像空间规划相比BEV距离变换规划大幅加速。④SegFormer-B0达到手标注IoU 0.946，每帧11.7ms，优于基线（IoU 0.758，18.9ms）；图像空间中点规划横向中心误差14.3px，耗时2.2ms，比BEV距离变换规划快421倍。
- **摘要（英）**: This paper tackles sidewalk path extraction for micromobility navigation on low-power hardware in cluttered, map-sparse environments. It presents a monocular pipeline with three design iterations and compares five planning methods across BEV and image-space domains, using a semi-supervised teacher-student framework with a compact SegFormer-B0 student. The student achieves IoU 0.946 at 11.7ms/frame, and image-space midpoint planning reduces center error to 14.3px at 2.2ms, a 421x speedup over BEV distance-transform planning.
- **评估**: 面向嵌入式微移动导航的轻量化感知方案，与自动驾驶边缘计算场景相关，但规模较小。
- **核心贡献**: 提出并系统比较了轻量级单目人行道提取与规划方法，实现高效嵌入式导航。
- **创新点**: 结合半监督蒸馏和图像空间规划，显著提升速度并保持精度。
- **结果**: 轻量模型IoU达0.946，规划速度提升421倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sidewalk-scale path extraction demands perception and planning that run reliably on compact, low-power hardware in cluttered, map-sparse environments. We present a monocular vision pipeline for sidewalk path extraction in micromobility systems that progresses through three design iterations, from a skeleton-graph baseline through distance-transform corridor planning to a lightweight image-space architecture, and provides a systematic comparison of five path-planning methods across both bird's-eye-view (BEV) and image-space domains. A compact SegFormer-B0 student model, trained with a semi-supervised teacher-student framework using OneFormer Swin-L pseudo-labels, achieves a hand-annotated IoU of 0.946 at 11.7 ms per frame, improving over the baseline checkpoint (IoU 0.758, 18.9 ms). In a controlled planner comparison on 32 hand-labeled frames, image-space midpoint planning achieves the lowest lateral center error (14.3 px) at 2.2 ms, a 421x speedup over BEV distance-transform planning (926.8 ms, 65.0 px center error), while maintaining comparable mask-path alignment (98.5% versus 98.6%). A full-video replay across six campus sequences (22,679 frames) confirms that the improved segmentation reduces temporal instability from 1.46% to 0.33% and increases template-path availability from 73.7% to 79.3%. We further show that BEV-only path extraction is fragile in monocular settings: in one profiled run, 99.3% of frames produced no valid BEV path. The final recommended architecture, image-space midpoint primary, image-space distance-transform fallback, and BEV reserved for visualization, runs the full perception-to-path stack in under 50 ms per frame on CPU, making it suitable for embedded pedestrian-speed micromobility systems.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 10 |
| Self-supervised Vision | 10 |
| Video Understanding | 10 |
| Object Detection | 10 |
| Multimodal | 10 |
| Vision Transformer | 10 |
| Multi-camera Perception | 10 |
| Network Pruning | 7 |
| Autonomous Driving | 4 |
| Open-set Detection | 4 |
| 3D Detection | 3 |
| Continual Learning | 2 |
| BEV | 1 |
| **总计** | **91** |