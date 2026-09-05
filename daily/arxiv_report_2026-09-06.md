# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-09-06  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 9 篇（其中 9 篇经大模型中文评估）

> 匹配领域: Object Detection、Autonomous Driving、3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open-set Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (9篇)

## VLM

### 1. Temporal Self-Distillation: Learning Visual State Tracking in Videos Without Supervision **⭐⭐⭐⭐** (相关度: 70%, 质量: 0.8)

- **arXiv ID**: [2609.04203](https://arxiv.org/abs/2609.04203)  · [📄 PDF](https://arxiv.org/pdf/2609.04203)
- **作者**: Shravan Venkatraman, Wenshuai Zhao, Mohammad Hassan Vali et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对视频连续状态跟踪缺乏无监督训练方法的问题，现有方法依赖标签或外部教师。②提出S³T框架，将时间采样密度作为特权信息，密集视图作为教师，稀疏视图学生通过自蒸馏匹配下一token分布，无需标签或额外推理成本。③相比自进化方法，首次实现完全自包含的连续状态跟踪，利用自蒸馏机制有效传递时间动态信息。④在LLaVA-OneVision-2-8B上，VSTAT准确率提升+1.74，集成后+2.38，适配视觉编码器后+2.70；从合成视频学到的能力迁移到真实视频，VSTAT-YouTube提升+7.95，MVBench Action Count提升+4.50。
- **摘要（英）**: This paper addresses the lack of unsupervised methods for continuous video state tracking by introducing S3T, which treats temporal sampling density as privileged information and uses self-distillation from dense to sparse views. It achieves significant improvements on VSTAT and transfers learned capabilities to real videos, with gains of +7.95 on VSTAT-YouTube and +4.50 on MVBench Action Count.
- **评估**: 该工作为视频状态跟踪提供了首个完全自监督框架，方法简洁且效果显著，对视频理解领域具有重要参考价值。
- **核心贡献**: 提出首个完全自包含的连续视频状态跟踪自监督框架S³T。
- **创新点**: 利用时间采样密度作为特权信息，通过自蒸馏实现无监督训练。
- **结果**: 在VSTAT和真实视频基准上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce S$^3$T (Self-Supervised Self-Distillation over Time), which, to the best of our knowledge, is the first fully self-contained framework for continuous video state tracking. Our method treats temporal sampling density as privileged information, based on the hypothesis that a denser view of the same clip recovers the running state more accurately. This view serves as the teacher, while a sparse-view student with the same weights learns to match its next-token distribution. The model generates its own target, so training requires no labels, separate teacher, or reward signal, and adds no inference cost. On LLaVA-OneVision-2-8B, S$^3$T improves VSTAT accuracy by $+1.74$ as a single model, $+2.38$ with souping, and $+2.70$ with additional vision-encoder adaptation, while prior self-evolving methods leave state tracking largely unchanged. The capability learned from unlabeled synthetic clips transfers to real videos, improving performance by $+7.95$ on VSTAT-YouTube state-tracking questions and $+4.50$ on MVBench Action Count.

</details>

### 2. Principia: Relational Physics Tests for Video Models **⭐⭐⭐** (相关度: 60%, 质量: 0.7)

- **arXiv ID**: [2609.04200](https://arxiv.org/abs/2609.04200)  · [📄 PDF](https://arxiv.org/pdf/2609.04200)
- **作者**: Varun Varma Thozhiyoor, Shivam Tripathi, Venkatesh Babu Radhakrishnan et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对视频模型物理推理评估中绝对运动测量受帧率、尺度和相机标定影响的问题。②提出Principia基准，通过成对物体的关系一致性评估牛顿物理，涵盖八种现象，并引入与标定无关的一致性分数。③相比现有基准，利用关系一致性避免标定依赖，更直接地量化物理违背。④在六个SOTA视频生成器上，所有模型得分不超过0.42，尽管VBench得分约0.8，显示现有模型物理推理能力严重不足。
- **摘要（英）**: This paper introduces Principia, a benchmark for evaluating Newtonian physics in video models through relational consistency between paired objects, avoiding calibration dependencies. Results show all six state-of-the-art video generators score below 0.42, highlighting significant deficiencies in physical reasoning despite high VBench scores.
- **评估**: 该基准为视频物理推理评估提供了新视角，揭示了现有生成模型的重大缺陷，对视频理解研究有启示作用。
- **核心贡献**: 提出基于关系一致性的物理推理基准Principia。
- **创新点**: 利用标定无关的关系一致性分数评估物理违背。
- **结果**: 发现现有视频生成器物理推理能力极低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Evaluating physical reasoning in video models is difficult because absolute motion measurements depend on frame rate, object scale, and camera calibration, all of which are often ambiguous or unavailable in generated video. We propose a different approach. When two objects in the same scene obey the same physical law, their motions must satisfy predictable relationships, and these relationships hold independent of calibration. We introduce Principia, a benchmark that evaluates Newtonian physics through relational consistency between paired objects. Principia spans eight phenomena - gravity, restitution, friction, rotational inertia, projectile motion, momentum, pendulum, and mass-spring oscillation - across translational, rotational, collisional, and oscillatory dynamics, using real-world scenes recorded under controlled protocols. We also introduce a calibration-independent consistency score that quantifies physical violation directly in image space. Across thousands of generations from six state-of-the-art video generators, no model exceeds 0.42 on Principia despite all scoring around 0.8 on VBench. Vision-language models are evaluated on their ability to detect relational physics violations, with the best model achieving only 67% accuracy and most performing near chance level.

</details>

### 3. WorldReward: Reward Modeling for Camera-Conditioned World Models **⭐⭐⭐** (相关度: 50%, 质量: 0.7)

- **arXiv ID**: [2609.03952](https://arxiv.org/abs/2609.03952)  · [📄 PDF](https://arxiv.org/pdf/2609.03952)
- **作者**: Yibin Wang, Zehan Wang, Junshu Tang et al. (16 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ①针对相机条件世界模型评估中动作一致性和视觉质量分离评估的问题。②提出WorldReward，基于VLM的成对偏好奖励模型，将视频分解为动作对齐块，组织结构化视觉证据，并通过投票聚合块级决策。③相比现有奖励，统一了动作一致性和视觉质量评估，避免长视频上下文噪声。④在训练中构建大规模数据集，但摘要未提供具体性能数据。
- **摘要（英）**: This paper presents WorldReward, a VLM-based pairwise preference reward model that unifies action-consistency and visual-quality evaluation for camera-conditioned world models by decomposing videos into action-aligned chunks and aggregating decisions. It addresses limitations of existing rewards that assess these aspects separately, though specific performance metrics are not detailed in the abstract.
- **评估**: 该工作为世界模型评估提供了统一框架，方法设计合理，但缺乏具体实验数据，影响力待验证。
- **核心贡献**: 提出统一动作一致性和视觉质量的VLM奖励模型WorldReward。
- **创新点**: 通过块级分解和投票聚合处理长视频评估。
- **结果**: 摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-conditioned world models generate interactive videos in which commanded actions should induce the expected scene changes while appearance, geometry, and temporal dynamics remain coherent. Existing rewards assess these requirements separately: geometry-based rewards estimate trajectory execution but cannot judge the visual quality of the executed motion, whereas image-based rewards measure frame quality without capturing action execution or temporal dynamics. We posit that a vision-language model (VLM) offers a shared reasoning space for relating actions to their visual outcomes. However, judging a complete long video against its full action sequence creates a lengthy, noisy context in which short-lived local action evidence can be missed or diluted. We present WorldReward, a VLM-based pairwise preference reward model that unifies action-consistency and visual-quality evaluation for camera-conditioned world models. WorldReward decomposes paired videos into action-aligned chunks, organizes each chunk into structured visual evidence, and aggregates chunk-level decisions by voting into separate video-level action and visual-quality preferences. To train it, we construct a large-scale reasoning-augmented preference dataset using structured judgments generated by a frontier VLM and refined through tool-based agent auditing and targeted human review. We further introduce WorldReward-Bench, a human-annotated benchmark measuring reward-model agreement with human preferences across action consistency, appearance quality, and motion quality. WorldReward achieves the highest agreement on all three dimensions, exceeding GPT-5.5 by 3.42, 1.45, and 3.56 percentage points, respectively. When used for RL post-training of HY-WorldPlay 1.5, it consistently improves both action execution and visual quality across short- to long-term horizons.

</details>

### 4. When Vision Meets Graphs: A Survey on Graph Reasoning and Learning **⭐⭐** (相关度: 30%, 质量: 0.6)

- **arXiv ID**: [2609.03816](https://arxiv.org/abs/2609.03816)  · [📄 PDF](https://arxiv.org/pdf/2609.03816)
- **作者**: Xinjian Zhao, Wei Pang, Zhixuan Yu et al. (11 authors)
- **🏷️ 机构**: The Chinese University of Hong Kong, University of Waterloo, CASIA
- **提交日期**: 2026-09-03 · **分类**: cs.SI, cs.CV, cs.LG · **📚 被引**: 1
- **摘要（中）**: ①针对图学习管线忽略图视觉形式的问题，传统GNN仅处理符号结构。②提供首个系统综述，涵盖视觉图推理和学习的三个方向。③相比现有综述，强调视觉模型在图理解中的潜力。④作为综述，无实验数据，但为跨领域研究提供框架。
- **摘要（英）**: This survey systematically reviews the emerging area of vision meets graphs, where visual depictions of graphs are used as first-class inputs for reasoning and learning. It organizes existing work into three threads and argues for renewed attention in the era of powerful vision models, though no experimental results are provided.
- **评估**: 该综述为图学习与视觉结合提供了新视角，但相关性较低，对自动驾驶领域贡献有限。
- **核心贡献**: 首次系统综述视觉图推理与学习领域。
- **创新点**: 将图视觉形式作为一等输入。
- **结果**: 无实验数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graphs are a fundamental data structure underlying many problems in the natural and social sciences. Over the past decade, Graph Neural Networks (GNNs) have dominated graph machine learning, supported by solid theoretical foundations. Yet scientists often understand graph structure through vision: chemists read molecular diagrams and social scientists inspect network visualizations. Despite decades of work on graph visualization, most graph learning pipelines still treat graphs purely as symbolic structures, rarely leveraging the visual form of graphs. We argue that this gap deserves renewed attention in the era of powerful vision and vision-language models. This survey provides a first systematic overview of the emerging area we term vision meets graphs, which treats visual depictions of graphs as first-class inputs for reasoning and learning. We organize existing work into three threads. Vision for Graph Reasoning studies how models can use visual depictions of graphs to understand structure and carry out multi-step reasoning. Vision for Graph Learning explores how visual features can complement or augment graph encoders beyond known limitations of message passing. Scientific Graphs examines domains where standardized depiction conventions support both reasoning and learning. Our goal is to clarify what current methods can and cannot do, and to outline a path toward foundation models that perceive and reason about graphs as scientists do.

</details>

### 5. Editable Visual Design **⭐⭐** (相关度: 20%, 质量: 0.5)

- **arXiv ID**: [2609.04034](https://arxiv.org/abs/2609.04034)  · [📄 PDF](https://arxiv.org/pdf/2609.04034)
- **作者**: Junyan Ye, Wei Liu, Dongzhi Jiang et al. (12 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.CL
- **摘要（中）**: ①针对扩散模型生成扁平位图无法分层编辑和代码生成缺乏美学直觉的问题。②提出可编辑视觉设计范式，由编码代理驱动，VLM作为创意大脑，图像生成模型作为视觉模拟器，采用先想象后行动的工作流。③相比现有方法，结合了扩散模型的表达力和代码生成的精确控制。④摘要未提供具体性能数据。
- **摘要（英）**: This paper proposes Editable Visual Design, a coding-agent-driven paradigm that combines VLM as a creative brain and image generation as a visual simulator to produce editable artifacts with decoupled layers. It addresses limitations of diffusion models and code-based generation, though no specific performance metrics are provided.
- **评估**: 该工作面向设计应用，与自动驾驶感知相关性低，创新性一般。
- **核心贡献**: 提出可编辑视觉设计的新范式。
- **创新点**: 结合VLM和图像生成模型实现分层编辑。
- **结果**: 摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets. To address this, we propose Editable Visual Design, a new paradigm driven by a Coding Agent. We designate the VLM as the ``creative brain'' for requirement comprehension, task planning, and aesthetic judgment, while utilizing the image generation model as an on-demand ``visual world simulator'' to synthesize standalone visual assets. Operating under an ``imagine first, then act'' closed-loop workflow, the agent generates isolated assets, writes native HTML/CSS, and iteratively refines the design against visual rendering feedback. Furthermore, Agent Design Replay faithfully reproduces the creative and reasoning trajectory akin to that of professional human designers. Ultimately, the system delivers editable artifacts with decoupled layers and real text, enabling users to perform intuitive mouse dragging and layout adjustments on a graphical user interface. Validations on posters, infographics, and other scenarios show that this paradigm successfully achieves both refined aesthetics and production-grade editability.

</details>

### 6. LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes **⭐⭐⭐** (相关度: 40%, 质量: 0.8)

- **arXiv ID**: [2609.03796](https://arxiv.org/abs/2609.03796)  · [📄 PDF](https://arxiv.org/pdf/2609.03796)
- **作者**: Chuyan Chen, Haoxing Chen, Kun Chen et al. (30 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI
- **摘要（中）**: ①针对图像生成模型依赖配对图文数据和训练细节不透明的问题。②提出LLaDA-Image，结合6B DiT和冻结的视觉语言模块，先通过图像预训练建立生成先验，使用RMSNorm和Muon优化器。③相比现有模型，提供完全开放的训练配方，减少配对数据依赖。④在Qwen-Image-Bench上，英文和中文轨道分别得分53.53和53.38，创开源模型SOTA。
- **摘要（英）**: This paper introduces LLaDA-Image, a unified framework with a 6B DiT and frozen vision-language module, trained with image-only pre-training and open recipes. It achieves state-of-the-art scores of 53.53 and 53.38 on Qwen-Image-Bench English and Chinese tracks, respectively, among open-source models.
- **评估**: 该工作提供完全开放的训练配方，对生成模型研究有贡献，但与自动驾驶感知相关性较低。
- **核心贡献**: 提出LLaDA-Image并开放完整训练配方。
- **创新点**: 通过图像预训练和Muon优化器减少配对数据依赖。
- **结果**: 在Qwen-Image-Bench上创开源SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce LLaDA-Image, a unified framework that pairs a 6B Diffusion Transformer (DiT) trained from scratch with a frozen vision-language understanding module built on the LLaDA2.0-Mini diffusion language model backbone. Instead of relying heavily on paired image-text data from the beginning, we first build a strong visual generative prior through image-only pre-training and mid-training. The generation pipeline comprises 220M samples, 98 of which are real images. For efficient and scalable optimization, we use parameter-free RMSNorm throughout the DiT together with the Muon optimizer. The resulting unified model produces highly photorealistic images while accurately following fine-grained editing instructions. We further distill LLaDA-Image into LLaDA-Image-Turbo, enabling fast inference in 2-4 sampling steps. On Qwen-Image-Bench, LLaDA-Image achieves overall scores of 53.53 and 53.38 on the English and Chinese tracks, respectively, setting a new state-of-the-art among open-source models on both tracks. To support further research on capable and efficient generative models, we release our model weights, training code, and detailed recipes.

</details>

### 7. ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation **⭐⭐⭐⭐** (相关度: 85%, 质量: 0.75)

- **arXiv ID**: [2609.03756](https://arxiv.org/abs/2609.03756)  · [📄 PDF](https://arxiv.org/pdf/2609.03756)
- **作者**: Javier del Pino, Salvador Rodríguez, Alejandro Garabito et al. (5 authors)
- **🏷️ 机构**: （机构待查）
- **💻 代码**: [github.com/speridlabs/eneas](https://github.com/speridlabs/eneas)
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI
- **摘要（中）**: 针对文本提示分割模型（如SAM 3）在实例跟踪中出现的时序幻觉、空间碎片化和语义误分类问题（如目标消失时无法报告缺失、极端特写时分割局部纹理、将雕像等视觉相似物误判为目标），提出ENEAS统一方法，支持精确跟踪和开放概念发现。方法上，在几何鲁棒的SeC架构上添加文本提示适配器，利用时序记忆保持目标在消失时不漂移；发现模式通过语义验证层结合高速视觉特征实现。相比已有工作，首次将文本提示与几何跟踪结合，并引入语义验证层解决视觉与本体论冲突。实验表明在跟踪和分割质量上优于基线，但摘要未提供具体数值。
- **摘要（英）**: ENEAS addresses temporal hallucinations, spatial fragmentation, and semantic misclassification in text-promptable segmentation models by extending the SeC architecture with a text-prompting adapter and temporal memory for robust instance tracking, plus a semantic verification layer for open-concept discovery. It improves over prior methods by unifying precise tracking and semantic discovery in a single framework, though quantitative results are not detailed in the abstract.
- **评估**: 该论文针对多模态分割模型的时序一致性和语义可靠性问题，提出统一跟踪与发现框架，对自动驾驶中的动态目标跟踪和开放集感知有重要参考价值。
- **核心贡献**: 提出ENEAS，一个统一的文本提示方法，同时实现精确实例跟踪和开放概念语义发现。
- **创新点**: 将文本提示适配器集成到几何鲁棒的SeC架构，并引入语义验证层解决视觉相似物误判。
- **结果**: 在跟踪和分割任务上优于基线，但摘要未提供具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present ENEAS, a unified, text-promptable method for instance tracking and semantic discovery. Text-promptable segmentation models, including the latest foundation models such as SAM 3, still suffer from temporal hallucinations, spatial fragmentation, and semantic misclassification: they fail to report target absence when an object leaves the field of view, segment local textures instead of the complete object during extreme close-ups, and prioritize visual features over ontological reality, so that visually similar artifacts such as statues, paintings, or reflections are segmented as target entities. ENEAS works two ways from a single method: precise tracking and high-quality segmentation of a unique instance, and open-concept discovery of every instance a text query names, resolved by a semantic verification layer. For tracking, we extend the geometrically robust SeC architecture, previously limited to point interactions, with a text-prompting adapter and leverage its temporal memory, so that the target is held through disappearance without drifting to distractors and kept whole even when it fills the entire view. For discovery, the verification layer combines high-speed visual embedding matching with conditional VLM refinement, invoking semantic reasoning only for ambiguous candidates, which filters out the ontological errors that visual-only models cannot distinguish while keeping latency low. Designed with 3D reconstruction in mind, where a single misclassified distractor corrupts the asset, ENEAS unlocks high-quality semantic tracking and segmentation of video, of broad libraries, and of collections of temporally or spatially unordered data, together with the discrimination to tell true instances from their doppelgangers: things that look alike but are not the same. The code and models are available at https://github.com/speridlabs/eneas

</details>

### 8. ToPO: Token-Conditioned Preference Routing for Attention-Based Latent Diffusion Models **⭐⭐⭐** (相关度: 40%, 质量: 0.7)

- **arXiv ID**: [2609.03688](https://arxiv.org/abs/2609.03688)  · [📄 PDF](https://arxiv.org/pdf/2609.03688)
- **作者**: Juntao Xu, Shihong Li, Hoi Fan Au et al. (4 authors)
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV
- **摘要（中）**: ToPO针对Diffusion-DPO在注意力潜在扩散模型中偏好优化效率低的问题，提出基于token条件路由的分离时空路径，通过交叉注意力调制和辅助排序项提升对齐质量。在SD-1.5和SDXL上均优于Diffusion-DPO，但实验范围限于等更新步数协议。
- **摘要（英）**: ToPO addresses the inefficiency of Diffusion-DPO in applying preference labels across spatial and temporal coordinates by constructing a detached, separable spatial-temporal route from branchwise residual contrast, using cross-attention to modulate spatial factors. It outperforms Diffusion-DPO on all five SD-1.5 metrics and SDXL benchmarks, though results are scoped to equal-update protocols.
- **评估**: 该论文对扩散模型偏好优化有方法论创新，但与自动驾驶感知领域关联较弱，主要面向图像生成。
- **核心贡献**: 提出Token-Oriented Preference Optimization方法，提升注意力潜在扩散模型的偏好对齐性能。
- **创新点**: 利用冻结参考去噪器的分支残差构建分离时空路由，并引入像素中点排序辅助项。
- **结果**: 在SD-1.5和SDXL上全面优于Diffusion-DPO，盲测中胜率更高。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pairwise preference labels rank complete images, yet Diffusion-DPO applies their effect over many spatial and denoising-time coordinates. For attention-based, noise-prediction latent diffusion, ToPO (Token-Oriented Preference Optimization) constructs a per-minibatch, detached, separable spatial-temporal route from branchwise squared-residual contrast in a frozen reference denoiser. Preferred-branch cross-attention uses content tokens to modulate the spatial factor, and an auxiliary pixel-midpoint ordering term is added without local labels or a learned reward model. In matched three-seed retrainings with a shared update schedule, ToPO has higher endpoint estimates than Diffusion-DPO on all five reported SD-1.5 metrics and on HPSv2, ImageReward, and CLIP for SDXL. It also receives larger raw win shares in an aggregate blind SDXL A/B study. These findings are scoped to the reported equal-update U-Net protocols rather than an equal-compute comparison.

</details>

### 9. Cross-Dataset Transfer and Reliability of Explainable Artificial Intelligence for RhythmFormer Remote Photoplethysmography **⭐⭐** (相关度: 60%, 质量: 0.6)

- **arXiv ID**: [2609.03663](https://arxiv.org/abs/2609.03663)  · [📄 PDF](https://arxiv.org/pdf/2609.03663)
- **作者**: Louis Chen, Torbjörn E. M. Nordling
- **🏷️ 机构**: （机构待查）
- **提交日期**: 2026-09-03 · **分类**: cs.CV, cs.AI, eess.IV
- **摘要（中）**: 针对远程光电容积描记（rPPG）可解释性研究缺乏定量证据的问题，该论文量化了RhythmFormer模型的解释，并评估跨数据集迁移性和与性能的关系。方法上，训练了八个条件特定模型，使用皮肤覆盖率和Salience-guided Faithfulness Coefficient评估四种解释方法。结果显示Beyond Intuition在两个数据集上排名最高，但解释与单样本心率误差等无显著相关，多数相关系数低于0.10，表明解释可靠性有限。
- **摘要（英）**: This paper quantifies explanations for RhythmFormer rPPG models and evaluates their cross-dataset transfer and relation to performance. Beyond Intuition ranks highest on both datasets, but explanations show weak correlation with per-clip errors, indicating limited reliability.
- **评估**: 该论文对rPPG可解释性有贡献，但与自动驾驶感知核心方向关联度一般，且结果揭示解释方法可靠性不足。
- **核心贡献**: 首次定量评估rPPG模型解释的跨数据集迁移性和可靠性。
- **创新点**: 应用多种解释方法并引入皮肤覆盖率和SaCo指标进行量化分析。
- **结果**: Beyond Intuition表现最佳，但解释与性能相关性弱，可靠性存疑。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Background. Remote photoplethysmography estimates the cardiovascular pulse from facial video, and its explanations have rested on inspecting heatmaps rather than on quantitative evidence about where a model reads it. We quantified the explanations and asked whether such explanations transfer between datasets and track model performance. Method. We trained eight condition-specific RhythmFormer models on NCKU-rPPG, recorded under three illumination levels, speaking, rotation, and cycling, estimated one heart rate per 5.12-second clip, and set them beside a UBFC-rPPG reproduction. Raw attention, rollout, attention flow, and Beyond Intuition were assessed by skin coverage and the Salience-guided Faithfulness Coefficient (SaCo). Results. Beyond Intuition ranked highest on both datasets, at median coverage 0.789 and SaCo 0.837 on Static level 3 against 0.826 and 0.917 on UBFC-rPPG; lower ranks differed. Within one participant of one condition, neither measure was related to a clip's heart-rate error, waveform correlation, or signal-to-noise ratio on either dataset: 186 of the 252 coefficients fell below $|ρ|=0.10$ and 28 reached $p<0.05$ against the 13 expected by chance. Across the eight scenarios only Beyond Intuition's coverage followed the three performance measures, at $ρ=-0.43$, $+0.57$, and $+0.43$, while the attention-only methods' SaCo ran opposite to each. It failed at 40 lux alone, its median coverage falling to 0.180 and its median SaCo to $-0.178$, whereas motion degraded the estimates far more without such a drop. Conclusions. Skin coverage and SaCo carry information complementary to the performance measures rather than a proxy for them: attributing to the skin does not guarantee an accurate estimate. What an attribution reveals about a condition is where the model looks rather than how faithfully its map is ordered.

</details>

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 9 |
| **总计** | **9** |