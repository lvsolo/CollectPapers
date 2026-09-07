# Multimodal — 2026 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding **⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:2601.07298](https://arxiv.org/abs/2601.07298)
- **作者**: Jianghao Yin, Qingbin Li, Kun Sun, Cheng Ding, Jie Wang, Qin Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: 这篇论文针对多模态大语言模型在多图像推理任务中性能下降的问题，提出了一种认知启发的元动作框架CINEMA，将多图像推理分解为全局、聚焦、提示、思考和回答五个结构化元动作，模拟人类认知步骤。作者设计了基于检索的树采样策略生成高质量元动作轨迹用于冷启动训练，并在强化学习阶段采用两阶段范式，包括多样性保持策略和退火利用阶段。构建了包含56k冷启动和58k强化学习实例的数据集，覆盖多图像、多帧和单图像任务。实验表明该方法提升了多图像推理性能，但摘要未提供具体数据。
- **摘要（英）**: This paper tackles the degraded performance of MLLMs in multi-image reasoning by proposing CINEMA, a cognition-inspired meta-action framework that decomposes reasoning into five structured actions. It uses retrieval-based tree sampling for cold-start training and a two-stage RL paradigm with diversity preservation and annealing. A dataset of 56k cold-start and 58k RL instances is constructed, and experiments show improved multi-image reasoning performance.
- **核心贡献**: 提出了CINEMA框架和元动作分解策略，以及配套的训练数据集。
- **创新点**: 将人类认知步骤显式建模为元动作，并用于多图像推理。
- **结果**: 在多图像推理任务上取得了性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Multimodal Large Language Models (MLLMs) excel at single-image understanding, they exhibit significantly degraded performance in multi-image reasoning scenarios. Multi-image reasoning presents fundamental challenges including complex inter-relationships between images and scattered critical information across image sets. Inspired by human cognitive processes, we propose a Cognition-Inspired Meta-Action Framework (CINEMA), which decomposes multi-image reasoning into five structured meta-actions: Global, Focus, Hint, Think, and Answer, explicitly modeling the sequential cognitive steps humans naturally employ. For cold-start training, we introduce a Retrieval-Based Tree Sampling strategy that generates high-quality meta-action trajectories to bootstrap the model with reasoning patterns. During reinforcement learning, we adopt a two-stage paradigm: an exploration phase with Diversity-Preserving Strategy to avoid entropy collapse, followed by an annealed exploitation phase with DAPO to gradually strengthen exploitation. To train our model, we construct a dataset of 56k cold-start and 58k reinforcement learning instances spanning multi-image, multi-frame, and single-image tasks. We conduct extensive evaluations on multi-image reasoning benchmarks, video understanding benchmarks, and single-image benchmarks, achieving competitive state-of-the-art performance on several key benchmarks. Our model surpasses GPT-4o on the MUIR and MVMath benchmarks and notably outperforms specialized video reasoning models on video understanding benchmarks, demonstrating the effectiveness and generalizability of our human cognition-inspired reasoning framework.

</details>

### VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2601.05175](https://arxiv.org/abs/2601.05175)
- **作者**: Shuming Liu, Mingchen Zhuge, Changsheng Zhao, Jun Chen, Lemeng Wu, Zechun Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: 这篇论文针对视频理解中链式思维（CoT）推理的必要性和效率问题，发现强化学习训练的视频模型在直接回答时往往能达到或超过CoT性能，但CoT计算成本更高。作者提出了VideoAuto-R1框架，采用“思考一次，回答两次”的训练范式，模型首先生成初始答案，然后进行推理，最后输出审查答案，并通过可验证奖励监督。在推理时，模型根据初始答案的置信度决定是否进行推理。在视频问答和接地基准上，VideoAuto-R1实现了最先进的准确率，同时将平均响应长度从149个token减少到44个，效率提升约3.3倍。
- **摘要（英）**: This paper questions the necessity of CoT in video understanding, showing that direct answering can match or surpass CoT for RL-trained models. It proposes VideoAuto-R1 with a 'Thinking Once, Answering Twice' paradigm and confidence-based adaptive reasoning. It achieves SOTA accuracy on video QA and grounding benchmarks while reducing response length by ~3.3x.
- **核心贡献**: 提出了VideoAuto-R1框架，实现按需推理以提升视频理解效率。
- **创新点**: 基于置信度动态决定是否进行推理，减少不必要的计算。
- **结果**: 在视频QA和接地任务上达到SOTA，响应长度减少3.3倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Chain-of-thought (CoT) reasoning has emerged as a powerful tool for multimodal large language models on video understanding tasks. However, its necessity and advantages over direct answering remain underexplored. In this paper, we first demonstrate that for RL-trained video models, direct answering often matches or even surpasses CoT performance, despite CoT producing step-by-step analyses at a higher computational cost. Motivated by this, we propose VideoAuto-R1, a video understanding framework that adopts a reason-when-necessary strategy. During training, our approach follows a Thinking Once, Answering Twice paradigm: the model first generates an initial answer, then performs reasoning, and finally outputs a reviewed answer. Both answers are supervised via verifiable rewards. During inference, the model uses the confidence score of the initial answer to determine whether to proceed with reasoning. Across video QA and grounding benchmarks, VideoAuto-R1 achieves state-of-the-art accuracy with significantly improved efficiency, reducing the average response length by ~3.3x, e.g., from 149 to just 44 tokens. Moreover, we observe a low rate of thinking-mode activation on perception-oriented tasks, but a higher rate on reasoning-intensive tasks. This suggests that explicit language-based reasoning is generally beneficial but not always necessary.

</details>

### Beyond Patches: Global-aware Autoregressive Model for Multimodal Few-Shot Font Generation **⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2601.01593](https://arxiv.org/abs/2601.01593)
- **作者**: Haonan Cai, Yuxuan Luo, Zhouhui Lian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: 这篇论文针对少样本字体生成（FFG）中结构完整性和风格保真度难以平衡的问题，以及现有自回归模型受限于补丁级标记化而忽略全局依赖的缺陷。作者提出了GAR-Font框架，引入全局感知标记器以捕获局部结构和全局风格模式，并设计了多模态风格编码器，通过轻量级语言风格适配器实现灵活的风格控制，无需密集的多模态预训练。此外，还包含后精炼流程以增强结构保真度。实验验证了方法的有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the challenges in few-shot font generation, including structural integrity and stylistic fidelity, and the limitations of patch-level tokenization in AR models. It proposes GAR-Font with a global-aware tokenizer, a multimodal style encoder with a lightweight language adapter, and a post-refinement pipeline. Experiments demonstrate effectiveness.
- **核心贡献**: 提出了GAR-Font框架，用于多模态少样本字体生成。
- **创新点**: 引入全局感知标记器和语言风格适配器。
- **结果**: 在字体生成任务上验证了有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Manual font design is an intricate process that transforms a stylistic visual concept into a coherent glyph set. This challenge persists in automated Few-shot Font Generation (FFG), where models often struggle to preserve both the structural integrity and stylistic fidelity from limited references. While autoregressive (AR) models have demonstrated impressive generative capabilities, their application to FFG is constrained by conventional patch-level tokenization, which neglects global dependencies crucial for coherent font synthesis. Moreover, existing FFG methods remain within the image-to-image paradigm, relying solely on visual references and overlooking the role of language in conveying stylistic intent during font design. To address these limitations, we propose GAR-Font, a novel AR framework for multimodal few-shot font generation. GAR-Font introduces a global-aware tokenizer that effectively captures both local structures and global stylistic patterns, a multimodal style encoder offering flexible style control through a lightweight language-style adapter without requiring intensive multimodal pretraining, and a post-refinement pipeline that further enhances structural fidelity and style coherence. Extensive experiments show that GAR-Font outperforms existing FFG methods, excelling in maintaining global style faithfulness and achieving higher-quality results with textual stylistic guidance.

</details>

### Purify then Guide: Rethinking Domain Generalization for Multimodal Face Anti-Spoofing **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2505.09484](https://arxiv.org/abs/2505.09484)
- **作者**: Yingjie Ma, Xun Lin, Zitong Yu, Haonan Wang, Ruixin Zhang, Shouhong Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2026
- **摘要（中）**: 这篇论文针对多模态人脸防伪（FAS）方法在泛化能力上的不足，主要源于模态特定偏差和域偏移。作者提出了多模态去噪与对齐（MMDA）框架，利用CLIP的零样本泛化能力，通过去噪和对齐机制抑制多模态数据中的噪声，增强跨模态对齐的泛化性能。其中，模态-域联合差分注意力（MD2A）模块通过提取公共噪声特征来细化注意力机制，同时减轻域和模态噪声的影响。表示空间软对齐（RS2）策略利用预训练CLIP将多域多模态数据灵活对齐到泛化表示空间。实验验证了方法的有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the generalization issues in multimodal face anti-spoofing caused by modality-specific biases and domain shifts. It proposes the MMDA framework, leveraging CLIP's zero-shot capability for denoising and alignment, with MD2A attention and RS2 alignment strategies. Experiments demonstrate improved cross-modal generalization.
- **核心贡献**: 提出了MMDA框架，用于增强多模态人脸防伪的泛化能力。
- **创新点**: 结合CLIP和联合差分注意力进行模态-域去噪与对齐。
- **结果**: 在跨模态泛化上取得了性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Face Anti-Spoofing (FAS) is essential for the security of facial recognition systems in diverse scenarios such as payment processing and surveillance. Current multimodal FAS methods often struggle with effective generalization, mainly due to modality-specific biases and domain shifts. To address these challenges, we introduce the \textbf{M}ulti\textbf{m}odal \textbf{D}enoising and \textbf{A}lignment (\textbf{MMDA}) framework. By leveraging the zero-shot generalization capability of CLIP, the MMDA framework effectively suppresses noise in multimodal data through denoising and alignment mechanisms, thereby significantly enhancing the generalization performance of cross-modal alignment. The \textbf{M}odality-\textbf{D}omain Joint \textbf{D}ifferential \textbf{A}ttention (\textbf{MD2A}) module in MMDA concurrently mitigates the impacts of domain and modality noise by refining the attention mechanism based on extracted common noise features. Furthermore, the \textbf{R}epresentation \textbf{S}pace \textbf{S}oft (\textbf{RS2}) Alignment strategy utilizes the pre-trained CLIP model to align multi-domain multimodal data into a generalized representation space in a flexible manner, preserving intricate representations and enhancing the model's adaptability to various unseen conditions. We also design a \textbf{U}-shaped \textbf{D}ual \textbf{S}pace \textbf{A}daptation (\textbf{U-DSA}) module to enhance the adaptability of representations while maintaining generalization performance. These improvements not only enhance the framework's generalization capabilities but also boost its ability to represent complex representations. Our experimental results on four benchmark datasets under different evaluation protocols demonstrate that the MMDA framework outperforms existing state-of-the-art methods in terms of cross-domain generalization and multimodal detection accuracy. The code will be released soon.

</details>

### DeepEyesV2: Toward Agentic Multimodal Model **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2511.05271](https://arxiv.org/abs/2511.05271)
- **作者**: Jack Hong, Chenxiao Zhao, ChengLin Zhu, Weiheng Lu, Guohai Xu, Xing Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2026
- **摘要（中）**: ①针对智能体多模态模型在工具调用和推理集成上的不足，直接强化学习无法有效诱导工具使用行为。②提出DeepEyesV2，采用两阶段训练流程：冷启动阶段建立工具使用模式，强化学习阶段优化工具调用；并构建多样化训练数据集和RealX-Bench基准。③相比现有方法，通过冷启动和RL结合，解决了工具使用行为不稳定的问题。④在RealX-Bench和其他基准上验证了有效性，在真实世界理解、数学推理和搜索密集型任务上表现优异。
- **摘要（英）**: This paper tackles the challenge of enabling agentic multimodal models to invoke external tools effectively, proposing DeepEyesV2 with a two-stage pipeline (cold-start and reinforcement learning) to establish and refine tool-use behavior. It introduces RealX-Bench for evaluating real-world multimodal reasoning, demonstrating strong performance across understanding, math, and search tasks.
- **核心贡献**: 提出DeepEyesV2及两阶段训练方法，解决工具使用行为诱导问题。
- **创新点**: 冷启动加强化学习的训练策略，稳定提升工具调用能力。
- **结果**: 在RealX-Bench等基准上表现优异，验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Agentic multimodal models should not only comprehend text and images, but also actively invoke external tools, such as code execution environments and web search, and integrate these operations into reasoning. In this work, we introduce DeepEyesV2 and explore how to build an agentic multimodal model from the perspectives of data construction, training methods, and model evaluation. We observe that direct reinforcement learning alone fails to induce robust tool-use behavior. This phenomenon motivates a two-stage training pipeline: a cold-start stage to establish tool-use patterns, and reinforcement learning stage to further refine tool invocation. We curate a diverse, moderately challenging training dataset, specifically including examples where tool use is beneficial. We further introduce RealX-Bench, a comprehensive benchmark designed to evaluate real-world multimodal reasoning, which inherently requires the integration of multiple capabilities, including perception, search, and reasoning. We evaluate DeepEyesV2 on RealX-Bench and other representative benchmarks, demonstrating its effectiveness across real-world understanding, mathematical reasoning, and search-intensive tasks. Moreover, DeepEyesV2 exhibits task-adaptive tool invocation, tending to use image operations for perception tasks and numerical computations for reasoning tasks. Reinforcement learning further enables complex tool combinations and allows model to selectively invoke tools based on context. We hope our study can provide guidance for community in developing agentic multimodal models.

</details>

## 跨领域论文（完整笔记在其他领域）

- Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Reinforcement Learning Framework for Embodied Exploration → [vlm](../vlm/Guideline%202026.md)
- MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation → [multi-camera-perception](../multi-camera-perception/Guideline%202026.md)
- Omni-View: Unlocking How Generation Facilitates Understanding in Unified 3D Model based on Multiview images → [multi-camera-perception](../multi-camera-perception/Guideline%202026.md)

<!-- COMPLETE v1 papers=5 -->
