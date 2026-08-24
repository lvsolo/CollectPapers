# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-08-24  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 14 篇（其中 14 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (9篇)
- [Multimodal](#multimodal) (4篇)
- [Object Detection](#object-detection) (1篇)

## VLM

### 1. Identify, Locate, Link: End-to-End Key-Value Extraction from Document Images **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2608.20868](https://arxiv.org/abs/2608.20868)  · [📄 PDF](https://arxiv.org/pdf/2608.20868)
- **作者**: A. Said Gurbuz, Ahmed Nassar, Christoph Auer et al. (11 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CL
- **摘要（中）**: 针对文档处理流水线中OCR与下游模型级联导致的错误传播问题，本文微调紧凑的256M参数视觉语言模型SmolDocling，直接从文档图像端到端提取键值对，无需OCR预处理。通过扩展DocTags加入键、值、区域和链接标签，支持多对多关系，并设计合成表单填充和图裁剪增强流水线，以及布局感知评估框架。在FUNSD、XFUND和大型私有数据集上，模型优于更大的零样本VLM基线，比Qwen2.5-VL（7B）小27倍，推理快5倍以上。
- **摘要（英）**: This paper addresses error propagation in cascaded OCR-based document processing by fine-tuning SmolDocling, a 256M-parameter VLM, for end-to-end key-value extraction from document images without OCR. It extends DocTags with key, value, region, and link tags, and introduces augmentation and layout-aware evaluation, outperforming larger zero-shot VLMs while being 27x smaller and 5x faster.
- **评估**: 该工作展示了紧凑VLM在文档理解任务上的高效性，但领域相关性较低，对自动驾驶感知参考价值有限。
- **核心贡献**: 提出端到端键值提取方法，利用紧凑VLM消除OCR级联错误。
- **创新点**: 扩展DocTags支持多对多关系，并设计布局感知评估框架。
- **结果**: 在多个基准上优于大模型基线，且模型尺寸和推理速度显著优化。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Document processing pipelines traditionally cascade optical character recognition (OCR) engines with downstream models for structured information extraction, leading to multi-stage error propagation. We fine-tune SmolDocling, a compact 256M-parameter vision-language model (VLM), to perform end-to-end key-value extraction directly from document images, jointly solving identification, localization, and association in a single pass without OCR preprocessing. We extend DocTags with specialized key, value, region, and link tags, enabling many-to-many relationships in a unified output sequence. To address data limitations, we design an augmentation pipeline combining synthetic form filling and graph-based crops that preserve complete key-value subgraphs. We further introduce a layout-aware evaluation framework extending text matching with spatial bounding box verification. On FUNSD, XFUND, and a large-scale private dataset, our model outperforms larger zero-shot VLM baselines under layout-aware evaluation, while being 27 times smaller than Qwen2.5-VL (7B) and over 5 times faster at inference. The model weights will be released publicly after publication.

</details>

### 2. When Generated Images Look Right and Retrieve Wrong: Coverage-Guided Cross-Scale Re-Indexing for Knowledge-Faithful Generative Perception **⭐⭐⭐** (相关度: 60%, 质量: 0.65)

- **arXiv ID**: [2608.20810](https://arxiv.org/abs/2608.20810)  · [📄 PDF](https://arxiv.org/pdf/2608.20810)
- **作者**: Guangyuan Dong, Chuang Liu, Yangchen Zeng et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.MM, cs.AI, cs.CV
- **摘要（中）**: 针对生成图像在跨尺度场景中语义坍缩导致检索失败的问题，本文提出CERES框架，构建三级语义金字塔，通过共现感知路由器挖掘隐式概念，并采用尺度路由交叉注意力到轻量U-Net生成器，用冻结VLM重索引验证覆盖。引入可微软Jaccard覆盖目标，在非退化条件下提供密集梯度，并用独立DINOv2线性探针验证。在四个全色锐化基准的七个设置上，CERES在保持像素保真度的同时提升了概念查询检索性能。
- **摘要（英）**: This paper addresses semantic collapse in generated images with multi-scale entities, where single pooled embeddings drop scale-specific concepts, breaking retrieval. It proposes CERES, a closed-loop indexing framework with a semantic pyramid, co-occurrence-aware routing, scale-routed cross-attention, and soft-Jaccard coverage verification, improving retrieval on pansharpening benchmarks.
- **评估**: 该研究聚焦生成式感知的检索一致性，方法有创新性，但应用场景与自动驾驶核心任务关联度中等。
- **核心贡献**: 提出CERES框架，通过覆盖引导的跨尺度重索引解决生成图像的语义坍缩问题。
- **创新点**: 引入三级语义金字塔和软Jaccard覆盖目标，实现生成与检索的闭环验证。
- **结果**: 在多个全色锐化基准上提升检索性能，同时保持高像素保真度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal information systems increasingly route generated visual content back through the same vision-language index that informed its production, so the output must remain retrievable by the queries it was meant to serve. When the scene contains entities at vastly different scales, existing language-guided generators condition on a single, globally pooled text embedding and quietly drop scale-specific concepts, breaking concept-query retrieval even when pixel fidelity is high. We formalise this failure as semantic collapse and propose CERES, a closed-loop multimodal indexing framework that builds a three-level semantic pyramid, mines implicit concepts via a co-occurrence-aware router, performs scale-routed cross-attention into a lightweight U-Net generator, and verifies coverage by re-indexing the generated image with the same frozen VLM. A continuously differentiable soft-Jaccard coverage objective returns dense gradients to the 0.39M-parameter generator under explicit non-degeneracy conditions, and coverage is verified by an independent DINOv2 linear probe trained only on external scene and object labels. On four pansharpening benchmarks across seven settings, CERES delivers the new state of the art with the largest gains where scale variation is most extreme. It also improves concept-query retrieval Recall@5 by +14.0 points and image-text mean reciprocal rank by 0.19 over the strongest baseline, showing that the closed loop preserves queryable content rather than self-referential feature consistency.

</details>

### 3. AffordAny: Open-World 3D Affordance Grounding from Monocular RGB Images via Vision-Language-Guided Geometric Reasoning **⭐⭐⭐⭐** (相关度: 75%, 质量: 0.75)

- **arXiv ID**: [2608.20720](https://arxiv.org/abs/2608.20720)  · [📄 PDF](https://arxiv.org/pdf/2608.20720)
- **作者**: Junqi Wu, Kaihua Tang, Xuanwen Chen et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: 针对开放世界3D功能接地依赖预构建几何和封闭本体的问题，本文提出AffordAny，利用单目RGB图像端到端构建大规模文本条件3D部分监督，通过冻结VLM引导解码器接地功能，并用伪标签自训练提升开放世界泛化。自动化流水线生成5,334个对象和10,633个部分级样本，覆盖473个类别，类别多样性比先前工作高一个数量级。在系统化泛化协议下，对未见对象、未见类别和未见指令改写均取得显著性能提升。
- **摘要（英）**: This paper addresses open-world 3D affordance grounding from raw RGB images, where existing methods assume pre-built geometry and closed ontologies. AffordAny constructs large-scale text-conditioned 3D supervision, uses a frozen VLM-guided decoder, and improves generalization via pseudo-label self-training, achieving an order-of-magnitude increase in categorical diversity and strong performance under systematic generalization protocols.
- **评估**: 该工作将3D功能接地扩展到开放世界，方法自动化程度高，对自动驾驶场景理解有潜在参考价值。
- **核心贡献**: 提出AffordAny，实现从单目RGB图像到开放世界3D功能接地的端到端框架。
- **创新点**: 利用冻结VLM和伪标签自训练，无需人工标注即可扩展新对象类别。
- **结果**: 生成大规模基准并显著提升未见对象和类别的泛化性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-world 3D affordance grounding requires localizing functional object parts in 3D given free-form language queries. Existing methods typically assume pre-built object-centric 3D geometry and closed affordance ontologies, limiting deployment from raw RGB observations. We present AffordAny, an end-to-end framework that uses one monocular RGB image to construct large-scale text-conditioned 3D part supervision, ground affordances with a frozen vision-language model (VLM) guided decoder, and improve open-world generalization through pseudo-label self-training. Our automated pipeline produces a benchmark of 5,334 objects and 10,633 part-level samples spanning 473 categories, an order-of-magnitude increase in categorical diversity over prior work. The decoder progressively fuses frozen Cosmos-2B features with 3D geometry through spatial projection, instruction-conditioned semantic compression, and bidirectional geometry-semantics interaction. Minimal-perturbation pseudo-label self-training further adds new objects without human annotation. Under a systematic generalization protocol evaluating unseen objects, unseen categories, and unseen instruction paraphrases, our approach achieves 0.428 IoU on unseen objects and 0.315 IoU on unseen categories after self-training, with unseen-category mIoU improving by 6.3% relative (p<0.01) and an instruction sensitivity gap of only 0.105, demonstrating effectiveness and robustness of our method.

</details>

### 4. ES-VP : Energy-Shaped Dynamic Visual Prompting for Efficient Model Adaptation **⭐⭐⭐⭐** (相关度: 80%, 质量: 0.8)

- **arXiv ID**: [2608.21194](https://arxiv.org/abs/2608.21194)  · [📄 PDF](https://arxiv.org/pdf/2608.21194)
- **作者**: Can Jin, Ying Li, Jingchen Sun et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: 针对视觉提示（VP）在灵活性和效率之间的权衡问题，现有固定提示忽略图像特性，而辅助网络生成提示增加参数和过拟合风险。本文提出能量形状视觉提示（ES-VP），利用低秩初始化和能量引导动态适应生成图像特定提示，直接使用预训练模型进行自适应提示生成，确保参数效率和泛化性。在五个架构和十五个数据集上的大量实验表明，ES-VP在参数更少的情况下优于当前单提示方法。
- **摘要（英）**: This paper addresses the trade-off between flexibility and efficiency in visual prompting, where fixed prompts ignore image characteristics and auxiliary networks increase parameters. ES-VP generates image-specific prompts via low-rank initialization and energy-guided dynamic adaptation, directly using the pre-trained model, achieving superior performance with fewer parameters across five architectures and fifteen datasets.
- **评估**: 该工作提出高效的视觉提示方法，参数效率高且泛化性强，对自动驾驶中预训练模型适配有实用价值。
- **核心贡献**: 提出ES-VP，实现图像特定提示生成，兼顾参数效率和性能。
- **创新点**: 利用能量引导动态适应和低秩初始化，无需辅助网络即可生成多样化提示。
- **结果**: 在多个架构和数据集上优于现有方法，且参数更少。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual prompting (VP) has emerged as a parameter-efficient method for adapting pre-trained models to downstream tasks. However, existing approaches encounter a trade-off between flexibility and efficiency. Some methods apply a fixed prompt to all images, ignoring individual image characteristics, while others introduce auxiliary networks to generate diverse prompts. Although the latter can improve performance, it also significantly increases parameter usage and the potential for overfitting to specific datasets. Furthermore, the auxiliary networks, combined with inherent biases in pre-trained models, limit scalability and generalization. In this paper, we propose Energy-Shaped Visual Prompting (ES-VP), a novel approach that generates image-specific prompts using low-rank initialization and energy-guided dynamic adaptation, achieving superior performance with fewer parameters compared to single-prompt methods. ES-VP directly utilizes the pre-trained model for adaptive prompt generation, ensuring both parameter efficiency and improved generalization. Extensive experiments conducted on five architectures across fifteen datasets demonstrate that ES-VP consistently outperforms current state-of-the-art (SOTA) single and diverse VP methods. For instance, using the CLIP architecture across four datasets, ES-VP outperforms the SOTA method DAM-VP by an average of 2.6\% in accuracy while utilizing 590$\times$ fewer VP parameters, thereby establishing a new benchmark for efficient and generalizable model adaptation.

</details>

### 5. TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming **⭐⭐** (相关度: 10%, 质量: 0.5)

- **arXiv ID**: [2608.20958](https://arxiv.org/abs/2608.20958)  · [📄 PDF](https://arxiv.org/pdf/2608.20958)
- **作者**: Yibo Hu, Yu Qian, Mao Gu et al. (9 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.AI, cs.CV
- **摘要（中）**: ①针对电商直播中多模态、长时序、噪声大的流式内容理解问题，产品信息分散在语音、视频帧、商品图、叠加文本和用户查询中。②提出TLive-Omni，将图像、视频、音频和文本映射到统一表示空间，引入Per-vGrid时间戳令牌组织以对齐视频网格与音频，设计三阶段监督训练流程和Faithful-RFT强化微调阶段。③相比现有方法，通过显式时间对齐和任务可验证反馈直接评分最终响应，而非优化推理式探索，提升忠实度和表达质量。④在电商直播场景中实现实时响应，但摘要未提供具体量化数据。
- **摘要（英）**: This paper addresses omni-modal understanding in noisy, long-form e-commerce live streams by proposing TLive-Omni, which unifies image, video, audio, and text inputs via Per-vGrid timestamped token organization and a three-stage training recipe with Faithful-RFT reinforcement fine-tuning. It improves answer faithfulness and expression quality through task-verifiable feedback, though no specific quantitative results are reported in the abstract.
- **评估**: 该论文针对电商直播这一垂直场景，但领域相关性极低，且缺乏具体实验数据，创新性有限。
- **核心贡献**: 提出面向电商直播的 omni-modal 理解模型及时间对齐和强化微调方法。
- **创新点**: 引入 Per-vGrid 时间戳令牌组织和 Faithful-RFT 直接评分机制。
- **结果**: 在电商直播场景中提升响应忠实度和实时性，但无量化数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> E-commerce live streaming requires omni-modal understanding of noisy, temporally extended streams, where product facts are distributed across speech, video frames, product images, overlaid text, and user queries. We present TLive-Omni, an omni-modal understanding model tailored to live-commerce scenarios. It maps image, video, audio, and text inputs into a unified representation space. For long-form live streaming analysis, we introduce Per-vGrid, a timestamped token organization that groups each video grid with its temporally corresponding audio within explicit boundary tokens to facilitate temporal alignment. We design a three-stage supervised training recipe that progressively develops live-commerce understanding, from omni-modal perception to instruction-following responses. We then propose Faithful-RFT, a reinforcement fine-tuning stage that further improves answer faithfulness and expression quality while meeting real-time demands, scoring final responses directly with task-verifiable feedback rather than optimizing for reasoning-style exploration during rollout. Moreover, TLive-Omni is supported by a scenario-oriented atomic capability taxonomy and a compact data production engine that converts live-commerce audio, image, and video streams into training signals for speech recognition, speaker analysis, product visual grounding, text recognition, temporal grounding, video dense caption, and omni-modal QA, etc. For scalable training, a synchronized length-grouped sampler reduces padding while preserving comparable workloads across workers, while a lightweight dynamic sampling strategy regenerates rollout groups with near-zero reward variance to maintain meaningful relative advantages for GRPO. Experiments on e-commerce live streaming benchmarks demonstrate strong performance across live-commerce domain tasks, together with excellent generalization on general benchmarks.

</details>

### 6. OccluRank: Controllable Occlusion-Aware Layout-to-Image Generation by Adding Just an Ordinal Rank **⭐⭐** (相关度: 15%, 质量: 0.6)

- **arXiv ID**: [2608.20932](https://arxiv.org/abs/2608.20932)  · [📄 PDF](https://arxiv.org/pdf/2608.20932)
- **作者**: Wenyang Hong, Yuan Wang, Yanbin Hao et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对布局到图像生成中边界框无法表示遮挡顺序的问题，现有方法依赖额外几何条件或复杂推理。②提出OccluRank，仅给每个边界框增加一个序数秩，通过轻量级秩条件编码和Order-aware Instance Interaction模块联合更新实例表示。③相比已有工作，无需额外几何输入或推理时优化，显式建模遮挡依赖交互。④构建OccluLayout合成数据集，但摘要未提供生成质量的量化对比数据。
- **摘要（英）**: This paper tackles occlusion order modeling in layout-to-image generation by augmenting bounding boxes with an ordinal rank and introducing an Order-aware Instance Interaction module for joint representation updates. It avoids extra geometric inputs and inference-time optimization, with a synthetic dataset OccluLayout, though quantitative results are not detailed in the abstract.
- **评估**: 与自动驾驶感知领域相关性低，主要面向图像生成，但遮挡建模思路有一定参考价值。
- **核心贡献**: 提出仅用序数秩实现可控遮挡感知的布局到图像生成框架。
- **创新点**: 通过秩条件编码和顺序感知交互模块显式建模遮挡顺序。
- **结果**: 构建合成数据集并实现可控生成，但缺乏具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Layout-to-image generation enables explicit spatial control through bounding-box layouts, yet bounding boxes specify only instance locations and cannot represent their occlusion order. Existing methods may rely on additional geometric conditions, employ complex inference procedures, or aggregate independently constructed instance representations without explicitly modeling their occlusion-dependent interactions. We propose OccluRank, a simple and controllable occlusion-aware layout-to-image framework that augments each bounding box with only one ordinal rank. OccluRank encodes the user-specified occlusion order through lightweight rank-based conditioning and introduces an Order-aware Instance Interaction (OII) module to jointly update rank-conditioned instance representations before aggregation. This allows the specified order to guide information exchange among occluding instances without additional geometric inputs or specialized inference-time optimization. We further construct OccluLayout, a synthetic training dataset whose occlusion order and amodal annotations are derived directly from known scene geometry rather than estimated from partially occluded images using auxiliary prediction models. For comprehensive evaluation, we introduce OccluLayout-Bench, which uses multiple multimodal large language model evaluators to assess instance presence, spatial layout, attributes, and occlusion order, together with FID for overall image quality. Experiments show that OccluRank more reliably preserves target instances, follows specified layouts, and realizes desired occlusion relationships while maintaining comparable attribute consistency and overall image quality.

</details>

### 7. InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.20910](https://arxiv.org/abs/2608.20910)  · [📄 PDF](https://arxiv.org/pdf/2608.20910)
- **作者**: Yunze Tong, Mushui Liu, Canyu Zhao et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对现有指令式视频编辑依赖固定时间跨度逐帧对齐的假设，无法处理开放流式视频编辑任务。②提出无限视频编辑任务，并设计数据收集管道和InfinityEdit轻量级编辑适配器，使流式视频生成器具备无界编辑能力。③相比现有方法，支持连续编辑指令序列，确保编辑是忠实延续而非逐帧重写。④摘要未提供具体量化结果，但强调生成质量在编辑累积时保持稳定。
- **摘要（英）**: This paper introduces infinite video editing for open-ended streams, proposing a data-collection pipeline and InfinityEdit, a lightweight adapter that equips streaming generators with unbounded editing ability. It addresses faithful continuation and stability under accumulated edits, though no quantitative results are provided in the abstract.
- **评估**: 视频编辑领域创新，但与自动驾驶感知相关性低，且缺乏实验数据。
- **核心贡献**: 提出无限视频编辑任务及轻量级适配器解决方案。
- **创新点**: 将编辑从固定片段扩展到无界流式场景。
- **结果**: 实现流式视频编辑，但未报告具体性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With large pretrained models, existing methods have effectively improved instruction-based video editing. However, most of them rely on an in-place editing assumption. They align the edited video with the given source clip frame by frame over a fixed time span. This pattern fails for open-ended streams, e.g., restyling a live game or applying a camera move to an ongoing shot. In such cases, edits must extend to future frames as they arrive, rather than be applied to a static input clip. In this paper, we study this setting and name it infinite video editing: given a preceding segment and an edit request, a model must generate the next segment that continues the stream while applying the requested edit. This process repeats as an unbounded sequence of edit instructions arrives. This task brings two challenges: the edit must be a faithful continuation rather than a frame-wise rewrite, and generation quality must remain stable as edits accumulate. To address them, we first design a data-collection pipeline for infinite video editing. Based on the collected data, we propose InfinityEdit, a lightweight edit adapter that equips a streaming video generator with unbounded editing ability. The adapter contains three attention modules. History cross-attention guides the denoising frames using the input frames. Temporal causal self-attention keeps temporal cues flowing only from earlier frames to later ones. Edit cross-attention injects the edit request into generation. During inference, the adapter is activated only in the chunk where an edit request arrives. Subsequent chunks are generated by the original model with a reset anchor frame. This scheme applies the edit while preserving the original model's infinite generation ability. Extensive experiments show that InfinityEdit faithfully continues the stream under each edit, and stays stable over unbounded edit sequences.

</details>

### 8. Identity-Preserving Text-to-Video Generation via Agentic Enhancement and Semantic Repair **⭐⭐** (相关度: 15%, 质量: 0.6)

- **arXiv ID**: [2608.20749](https://arxiv.org/abs/2608.20749)  · [📄 PDF](https://arxiv.org/pdf/2608.20749)
- **作者**: Jiayi Gao, Changcheng Hua, Jiaqi Tang et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/oceanflowlab/AESR](https://github.com/oceanflowlab/AESR)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对身份保持视频生成中身份漂移、指令遵循不完整和细节缺失问题，且商业模型为闭源黑盒。②提出AESR框架，包含全局智能体提示增强模块和样本级视觉语义修复模块，通过从官方文档、人机交互数据和测试域经验构建可复用剧本。③相比直接参数优化，采用轻量级增强框架，无需访问模型内部。④摘要未提供具体量化结果，但强调提升身份保持和指令遵循能力。
- **摘要（英）**: This paper addresses identity drift and incomplete instruction following in identity-preserving video generation by proposing AESR, a lightweight enhancement framework with global agentic prompt enhancement and sample-level semantic repair. It learns prompting formats and accumulates experience without parameter optimization, though quantitative results are not reported in the abstract.
- **评估**: 视频生成增强方法，与自动驾驶感知相关性低，创新性一般。
- **核心贡献**: 提出基于智能体增强和语义修复的身份保持视频生成框架。
- **创新点**: 利用智能体循环积累测试域经验并修复生成错误。
- **结果**: 提升身份保持和指令遵循，但无具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Identity-preserving video generation aims to synthesize videos that follow natural-language instructions while maintaining the visual identity of a given subject. Recent commercial video generation models have achieved strong visual quality and motion realism, but they still suffer from identity drift, incomplete instruction following, and missing visual details under complex prompts. Since these models are usually closed-source black boxes, directly improving them through parameter optimization is often infeasible. We therefore propose Agentic Enhancement and Semantic Repair (AESR), a lightweight enhancement framework for identity-preserving video generation. To improve prompt construction before generation and mitigate the above failures, AESR introduces a global agentic prompt enhancement module. This module learns model-specific prompting formats from official documentation, acquires human-centered video generation priors from human-interaction data, and accumulates test-domain identity-preserving generation experience into a reusable playbook through an agentic loop. To further repair errors in videos generated with enhanced prompts, AESR introduces a sample-level visual semantic repair module, which uses a VLM to locate erroneous video segments and design repair instructions, edits selected frames into explicit visual references, and guides a video editing model to fix local semantic or identity-related errors. We also adopt a lightweight Mixture-of-Experts selection strategy to choose reliable outputs from different generation and refinement paths. Under the official evaluation protocol of the ACM MM 2026 Identity-Preserving Video Generation Challenge, our system MIPL\_Video ranked first in Track 1, demonstrating the effectiveness of AESR for practical identity-preserving video generation. The code is available at https://github.com/oceanflowlab/AESR.

</details>

### 9. AGIDefect-4K: A Richly Annotated Dataset for AI-Generated Image Defect Detection, Localization and Explanation **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.20713](https://arxiv.org/abs/2608.20713)  · [📄 PDF](https://arxiv.org/pdf/2608.20713)
- **作者**: Xiangfei Sheng, Weidong Zou, Tianjiao Gu et al. (6 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/sxfly99/AGIDefect-4K](https://github.com/sxfly99/AGIDefect-4K)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要（中）**: ①针对AI生成图像中细微但关键缺陷的检测、定位和解释问题，现有基准缺乏全面诊断。②提出AGIDefect-4K数据集，包含4000张来自15个生成模型的图像，具有分层注释：检测标签、像素级分割掩码和文本解释，并构建AGIDA基线框架基于多模态大语言模型进行联合任务。③相比现有基准，提供更丰富的注释和解释能力。④基准测试显示AGI缺陷理解仍具挑战性，但摘要未提供具体性能数据。
- **摘要（英）**: This paper introduces AGIDefect-4K, a richly annotated dataset of 4,000 images from 15 generative models with hierarchical annotations for defect detection, localization, and explanation, along with AGIDA, a baseline framework using MLLMs. It addresses the gap in comprehensive AGI defect diagnosis, though benchmark results are not quantified in the abstract.
- **评估**: 数据集构建有实用价值，但领域相关性中等，方法创新性一般。
- **核心贡献**: 提供首个带分层注释的AI生成图像缺陷检测数据集和基线框架。
- **创新点**: 结合检测、分割和文本解释的多层次注释设计。
- **结果**: 揭示AGI缺陷理解挑战，但无具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative AI can now produce highly realistic images, yet current models still exhibit subtle but critical defects that undermine their reliability. While existing AI-generated image (AGI) evaluation benchmarks have made notable progress, comprehensive AGI defect diagnosis remains underexplored. To bridge this gap, we introduce AGIDefect-4K, a richly annotated dataset of 4,000 images from 15 state-of-the-art generative models spanning both open-source and closed-source systems. AGIDefect-4K features hierarchical defect annotations: (1) detection labels identifying whether defects exist, (2) pixel-level segmentation masks localizing defective regions, and (3) detailed textual explanations characterizing defect types and their perceptual impact. Each image is further annotated with an overall quality score. Building on this, we present AGIDA (AGI Defect Assistant), a baseline framework leveraging Multimodal Large Language Models (MLLMs) for joint defect detection, localization, explanation, and quality prediction. Comprehensive benchmarking on AGIDefect-4K reveals that AGI defect understanding remains challenging, underscoring the value of this dataset. The dataset is publicly available at https://github.com/sxfly99/AGIDefect-4K.

</details>

---

## Multimodal

### 1. Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2608.20756](https://arxiv.org/abs/2608.20756)  · [📄 PDF](https://arxiv.org/pdf/2608.20756)
- **作者**: Rujin Liang, Zhongpu Chen, Yuhao Lei et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/SWUFE-DB-Group/Vis-Poison](https://github.com/SWUFE-DB-Group/Vis-Poison)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对多模态检索增强生成（RAG）系统中视觉知识被投毒的安全问题，现有攻击依赖修改文本元数据，而本文提出Vis-Poison，以图像本身作为攻击载荷，无需操纵任何文本。方法采用自动化多智能体流程构造视觉上合理的投毒图像，并在两个代表性RAG流水线、四个嵌入模型和六个生成模型上评估。在黑盒设置下，对3万条多模态知识库实现40.16%至65.40%的端到端攻击成功率，且对依赖参数知识正确回答的MLLM平均成功率超60%。
- **摘要（英）**: This paper addresses the vulnerability of multimodal retrieval-augmented generation (RAG) systems to visual knowledge poisoning, where prior attacks rely on altering text metadata. It proposes Vis-Poison, a novel attack using the poisoned image itself as the payload via an automated multi-agent method, achieving 40.16%-65.40% end-to-end success rates on 30k-entry knowledge bases in black-box settings and over 60% average success against various MLLMs.
- **评估**: 该研究揭示了多模态RAG系统在视觉知识层面的安全盲区，攻击方法新颖且实验充分，对自动驾驶等依赖多模态感知的系统具有警示意义。
- **核心贡献**: 提出首个以图像为载荷的视觉知识投毒攻击方法Vis-Poison，无需修改文本元数据。
- **创新点**: 利用多智能体自动化生成视觉上合理的投毒图像，实现黑盒条件下的高效攻击。
- **结果**: 在多个多模态RAG流水线上实现40.16%-65.40%的攻击成功率，且对多种MLLM有效。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other associated text. Specifically, this attack is instantiated through an automated multi-agent method that constructs visually plausible poisoned images. To assess its impact, we evaluate Vis-Poison across two representative multimodal RAG pipelines, four embedding models, and six generation models. Empirically, Vis-Poison achieves an end-to-end attack success rate of 40.16\% to 65.40\% against 30k-entry multimodal knowledge bases in \emph{black-box} settings. Moreover, Vis-Poison remains effective against various MLLMs that can answer correctly from parametric knowledge alone, with an average success rate above 60\%. Code and data are available at https://github.com/SWUFE-DB-Group/Vis-Poison.

</details>

### 2. MigrationNarrate: A Dataset for Detection of Migration Narratives in YouTube Videos **⭐⭐** (相关度: 10%, 质量: 0.5)

- **arXiv ID**: [2608.20984](https://arxiv.org/abs/2608.20984)  · [📄 PDF](https://arxiv.org/pdf/2608.20984)
- **作者**: Fatima Haouari, Carolina Scarton, Kalina Bontcheva
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CL, cs.CY
- **摘要（中）**: ①针对YouTube视频中迁移叙事检测缺乏多模态数据集的问题，现有研究主要基于文本。②提出MigrationNarrate数据集，包含1115个YouTube视频转录文本，采用两级分类体系（12个超级叙事和53个叙事标签），并报告基于预训练编码器和LLM的基准结果。③相比已有工作，首次提供迁移叙事的多模态视频数据集。④摘要未提供具体性能数据，但包含错误分析。
- **摘要（英）**: This paper introduces MigrationNarrate, the first multimodal dataset for migration narrative detection in YouTube videos, with 1,115 transcripts annotated using a two-level taxonomy. It provides benchmarks with encoder models and LLMs, though no quantitative results are detailed in the abstract.
- **评估**: 社会媒体分析领域数据集，与自动驾驶感知相关性极低。
- **核心贡献**: 构建首个迁移叙事多模态视频检测数据集。
- **创新点**: 提出两级叙事分类体系并应用于视频转录。
- **结果**: 提供基准和错误分析，但无具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Narratives are central to how social communication is framed, making their detection critical for understanding and analysing public discourse. Prior work has explored narrative detection and extraction across diverse domains; however, migration narratives remain significantly understudied, primarily due to the absence of dedicated annotated datasets. Furthermore, public communication has recently shifted towards video-centric platforms, where narratives are conveyed through multimodal signals and consumed at scale. Despite this shift, narratives in videos remain largely unexplored. To bridge these gaps, we introduce MigrationNarrate, the first multimodal dataset for detection of migration narratives in the UK, consisting of 1,115 YouTube video transcripts annotated using a two-level taxonomy of 12 migration super-narratives and 53 narrative labels. This paper details the dataset design, collection, and annotations; together with benchmark results using a combination of pre-trained encoder models and both open- and closed-source Large Language Models. Finally, a thorough error analysis offers insights for future work.

</details>

### 3. KoViDoRe: Korean Visual Document Retrieval **⭐⭐** (相关度: 20%, 质量: 0.6)

- **arXiv ID**: [2608.20840](https://arxiv.org/abs/2608.20840)  · [📄 PDF](https://arxiv.org/pdf/2608.20840)
- **作者**: Yongbin Choi, Yongwoo Song, Mujeen Sung
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.IR, cs.CV
- **摘要（中）**: ①这篇论文针对韩语视觉文档检索中缺乏复杂结构、多页证据聚合的基准问题。②提出了KoViDoRe基准，包含多样布局的韩语文档，并开发了多阶段数据构建流程，包括结构化解析、基于摘要和上下文的合成查询生成及人工验证的相关性映射。③相比现有以英语为主、单页检索的基准，该工作覆盖了韩语多页场景和结构化内容。④评估显示当前多模态检索模型在韩语视觉文档检索上表现不佳，尤其在结构化内容和多样查询类型下。
- **摘要（英）**: This paper addresses the lack of benchmarks for Korean visual document retrieval with complex structures and multi-page evidence aggregation. It introduces KoViDoRe, a benchmark built via a multi-stage pipeline including structured parsing, synthetic query generation, and human-verified relevance mapping. Evaluations show current multimodal retrieval models struggle with Korean visual documents, especially structured content and diverse queries.
- **评估**: 该论文为韩语视觉文档检索提供了新基准，但领域相关性较低，且方法创新性有限，主要贡献在于数据集构建。
- **核心贡献**: 提出了KoViDoRe，一个覆盖韩语多页视觉文档检索的基准数据集。
- **创新点**: 设计了多阶段数据构建流程，结合摘要和上下文策略生成合成查询。
- **结果**: 当前模型在KoViDoRe上表现不佳，凸显了韩语视觉文档检索的挑战。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in multimodal retrieval have improved the ability to retrieve information from visually rich documents such as PDFs and reports. However, existing benchmarks remain largely centered on English and provide limited coverage of Korean visual documents with complex structures. Furthermore, most existing Korean resources primarily evaluate single-page retrieval, failing to capture realistic scenarios that require evidence aggregation across multiple pages. To address these gaps, we introduce KoViDoRe, a benchmark for Korean visual document retrieval. The dataset is constructed from publicly available Korean documents with diverse layouts, including tables, figures, and multi-column structures. We develop a multi-stage data curation pipeline consisting of structured document parsing, synthetic query generation using both summary-based and context-based strategies, and relevance mapping with human verification. Using KoViDoRe, we evaluate a wide range of multimodal retrieval models and observe that current models struggle to effectively handle Korean visual document retrieval, particularly in settings involving structured content and diverse query types. Motivated by this finding, we further curate a large-scale training dataset, Ko-VDR Train Public, to support the development of retrieval models tailored to Korean visual documents. Together, KoViDoRe and Ko-VDR Train Public provide a unified benchmark and training resource for Korean visual document retrieval.

</details>

### 4. TRACE: Training-time Report-guided and Clinically Ordered Concept Editing **⭐⭐⭐** (相关度: 30%, 质量: 0.7)

- **arXiv ID**: [2608.20809](https://arxiv.org/abs/2608.20809)  · [📄 PDF](https://arxiv.org/pdf/2608.20809)
- **作者**: Wentao Yue, Tianyou Lai, Jiayu Luo et al. (7 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①这篇论文针对乳腺超声诊断中概念模型依赖完整标注或推理时多模态输入、缺乏可解释性和鲁棒性的问题。②提出了TRACE框架，利用结构化放射报告作为特权概念监督，在训练时进行概念编辑，测试时仅需图像输入；包括教师引导编辑机制、战略概念缺失训练和编辑蒸馏。③相比现有概念方法，TRACE在训练时利用报告，测试时无需额外模态，并处理不完整标注。④在多个数据集上实验显示TRACE性能优越，并提升了可解释性。
- **摘要（英）**: This paper tackles the issues of concept-based models in breast ultrasound diagnosis requiring complete annotations or multimodal inputs at inference. It proposes TRACE, a training-time framework using structured reports as privileged supervision, with teacher-guided editing and edit distillation for image-only inference. Experiments show superior performance and improved interpretability across multiple datasets.
- **评估**: 该论文在医学影像领域有应用价值，但与本用户关注的自动驾驶感知方向相关性较低，方法设计有一定创新性。
- **核心贡献**: 提出了TRACE框架，利用训练时报告监督实现图像-only推理的概念编辑。
- **创新点**: 引入战略概念缺失训练和编辑蒸馏，处理不完整标注并实现自主概念细化。
- **结果**: TRACE在多个数据集上取得优越性能，并增强了模型可解释性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Breast ultrasound diagnosis relies on clinically meaningful semantic concepts, yet most deep learning methods adopt end-to-end image-to-label paradigms that lack interpretability and robustness. While concept-based approaches offer a promising alternative, they often assume complete annotations or require multimodal inputs at inference, which significantly limits their real-world applicability. To tackle these issues, we propose Training-time Report-guided and Clinically Ordered Concept Editing (TRACE), a training-time report-guided framework that leverages structured radiology reports as privileged concept supervision while enabling image-only diagnosis at test time. TRACE refines image-derived concepts through a teacher-guided editing mechanism within a malignancy-aware ordered concept space. To address incomplete annotations, we introduce Strategic Concept Missing Training (SCMT) and train an image-only self-editor via edit distillation for autonomous concept refinement. Besides, we introduce BUSC, a concept-enriched benchmark linking images, labels, and structured attributes. Experiments across multiple datasets demonstrate that TRACE achieves superior performance and improved cross-domain robustness compared to existing methods.

</details>

---

## Object Detection

### 1. On the Transferability of Agricultural Weed Detection Under Cross-Field Distribution Shift **⭐⭐⭐** (相关度: 65%, 质量: 0.7)

- **arXiv ID**: [2608.21254](https://arxiv.org/abs/2608.21254)  · [📄 PDF](https://arxiv.org/pdf/2608.21254)
- **作者**: Nikhilesh Prabhakar, Pranuthi Tenali, Wilfredo Abudeye Fernandez et al. (8 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.LG
- **摘要（中）**: 针对农业杂草检测在跨田地分布偏移下泛化性能未知的问题，本文引入新采集的棉花田UAV图像数据集，并与现有大豆数据集结合，评估跨作物检测器迁移策略。比较无监督域自适应检测（DAOD）与域邻近源预训练加少样本微调，分析目标域标签预算从零到有限的情况。结果表明，DAOD在零标签下有效，而少样本微调在少量标签下恢复性能，为减少重新标注需求提供指导。
- **摘要（英）**: This paper addresses the lack of evidence on cross-field generalization for agricultural weed detection, introducing a new cotton UAV dataset and evaluating transfer strategies against a soybean dataset. It compares unsupervised domain adaptive detection (DAOD) with pretraining plus few-shot fine-tuning, showing DAOD works with zero labels and fine-tuning recovers performance with few labels.
- **评估**: 该研究聚焦农业检测的域迁移问题，实验设计扎实，但对自动驾驶感知的直接相关性一般。
- **核心贡献**: 提供跨作物杂草检测的迁移性能分析，并引入新数据集。
- **创新点**: 系统比较DAOD与少样本微调在跨田地分布偏移下的效果。
- **结果**: 揭示不同标签预算下的最优迁移策略，减少部署时重新标注需求。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate agricultural weed detection in real-world field conditions is essential for precision agriculture, enabling targeted intervention and reducing yield loss. Recent work has reported strong detection performance from UAV-based imagery across a range of crops, yet existing approaches evaluate within a single crop and field, leaving practitioners with little evidence that a model trained on one crop will generalize to a new field or crop type. In this work, we characterize where cross-dataset weed-localization performance degrades and which modeling choices recover it, reducing the need to relabel every new deployment field. We introduce a newly collected and annotated UAV image dataset for agricultural weed detection in cotton fields and use it alongside an existing soybean dataset collected under a similar protocol. Using these datasets, we evaluate the performance of several strategies for transferring a detector trained on one crop to another, comparing unsupervised domain adaptive object detection (DAOD) against pretraining on a domain-adjacent source dataset followed by few-shot fine-tuning on the target dataset. Our analysis spans target-domain label budgets from zero to the full target dataset, characterizing the trade-off between adaptation strategy and annotation effort. We find that few-shot fine-tuning with as few as 25 labeled target examples outperforms unsupervised DAOD in our cross-crop comparison, suggesting that source domain selection combined with modest target supervision is more productive than algorithmic sophistication in adaptation.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 9 |
| Multimodal | 4 |
| Object Detection | 1 |
| **总计** | **14** |