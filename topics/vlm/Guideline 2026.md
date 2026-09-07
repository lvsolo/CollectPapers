# VLM — 2026 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Reinforcement Learning Framework for Embodied Exploration **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2601.10744](https://arxiv.org/abs/2601.10744)
- **作者**: Sen Wang, Bangwei Liu, Zhenkun Gao, Lizhuang Ma, Xuhong Wang, Yuan Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: 这篇论文针对具身智能体在长期复杂任务中缺乏持续学习和利用长期记忆进行决策的问题，提出了长期记忆具身探索（LMEE）任务，并构建了包含多目标导航和基于记忆问答的基准数据集LMEE-Bench。作者提出了MemoryExplorer方法，通过强化学习微调多模态大语言模型，鼓励主动查询记忆，并设计多任务奖励函数来提升探索和记忆利用能力。相比现有单次具身任务仅关注任务完成结果，该方法统一了探索认知和决策行为，促进了终身学习。实验在LMEE-Bench上验证了方法的有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the lack of lifelong learning and long-term memory utilization in embodied agents for long-horizon tasks, proposing the LMEE task and LMEE-Bench benchmark with multi-goal navigation and memory-based QA. It introduces MemoryExplorer, which fine-tunes a multimodal LLM via reinforcement learning to encourage active memory querying, with a multi-task reward function. Compared to one-shot tasks focusing only on outcomes, it unifies exploration cognition and decision-making for lifelong learning, with effectiveness demonstrated on the benchmark.
- **核心贡献**: 提出了LMEE任务和基准，以及基于多模态LLM强化学习的MemoryExplorer方法。
- **创新点**: 将长期记忆查询机制融入多模态LLM的强化学习框架。
- **结果**: 在LMEE-Bench上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An ideal embodied agent should possess lifelong learning capabilities to handle long-horizon and complex tasks, enabling continuous operation in general environments. This not only requires the agent to accurately accomplish given tasks but also to leverage long-term episodic memory to optimize decision-making. However, existing mainstream one-shot embodied tasks primarily focus on task completion results, neglecting the crucial process of exploration and memory utilization. To address this, we propose Long-term Memory Embodied Exploration (LMEE), which aims to unify the agent's exploratory cognition and decision-making behaviors to promote lifelong learning. We further construct a corresponding dataset and benchmark, LMEE-Bench, incorporating multi-goal navigation and memory-based question answering to comprehensively evaluate both the process and outcome of embodied exploration. To enhance the agent's memory recall and proactive exploration capabilities, we propose MemoryExplorer, a novel method that fine-tunes a multimodal large language model through reinforcement learning to encourage active memory querying. By incorporating a multi-task reward function that includes action prediction, frontier selection, and question answering, our model achieves proactive exploration. Extensive experiments against state-of-the-art embodied exploration models demonstrate that our approach achieves significant advantages in long-horizon embodied tasks. Our dataset and code will be released at https://wangsen99.github.io/papers/lmee/

</details>

### Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2601.09111](https://arxiv.org/abs/2601.09111)
- **作者**: Yang Li, Aming Wu, Zihao Zhang, Yahong Han
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①该论文针对视觉语言导航（VLN）在开放环境下的泛化问题，即训练与测试数据分布不一致导致传统闭集方法失效。②提出了slow4fast-VLN框架，包含快速推理模块（端到端策略网络实时输出动作并积累历史记录）和慢速推理模块（深度反思提取经验以增强泛化），两者动态交互。③相比已有工作，受人类快慢认知系统启发，首次将双系统推理引入VLN的开放场景适应任务（GSA-VLN），实现跨环境和指令的稳定策略。④摘要未提供具体数据，但声称通过动态交互推理显著提升导航泛化能力。
- **摘要（英）**: This paper addresses the generalization challenge of Vision-Language Navigation (VLN) in open environments, where training and test distributions differ. It proposes slow4fast-VLN, a dynamic interactive framework with a fast reasoning module for real-time action generation and a slow reasoning module for reflective experience extraction, inspired by human fast-slow cognition. The method introduces dual-system reasoning to the General Scene Adaptation task, aiming to improve policy stability and generalization across unseen environments and instructions, though no quantitative results are reported in the abstract.
- **核心贡献**: 提出slow4fast-VLN框架，通过快慢推理交互提升VLN在开放环境下的泛化能力。
- **创新点**: 首次将人类快慢认知系统建模为动态交互推理框架，用于开放场景VLN任务。
- **结果**: 摘要未提供具体数值，但声称能增强跨环境导航的适应能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation (VLN) aims to enable agents to navigate to a target location based on language instructions. Traditional VLN often follows a close-set assumption, i.e., training and test data share the same style of the input images and instructions. However, the real world is open and filled with various unseen environments, posing enormous difficulties for close-set methods. To this end, we focus on the General Scene Adaptation (GSA-VLN) task, aiming to learn generalized navigation ability by introducing diverse environments and inconsistent instructions.Recent research indicates that by means of fast and slow cognition systems, human beings could generate stable policies, which strengthen their adaptation for open world. Inspired by this idea, we propose the slow4fast-VLN, establishing a dynamic interactive fast-slow reasoning framework. The fast-reasoning module, an end-to-end strategy network, outputs actions via real-time input. It accumulates execution records in a history repository to build memory. The slow-reasoning module analyze the memories generated by the fast-reasoning module. Through deep reflection, it extracts experiences that enhance the generalization ability of decision-making. These experiences are structurally stored and used to continuously optimize the fast-reasoning module. Unlike traditional methods that treat fast-slow reasoning as independent mechanisms, our framework enables fast-slow interaction. By leveraging the experiences from slow reasoning, it continually improves the accuracy and generalization ability of fast decisions. This interaction allows the system to continuously adapt and efficiently execute navigation tasks when facing unseen scenarios. Extensive experiments demonstrate the superiorities of our method.

</details>

### Context Matters: Peer-Aware Student Behavioral Engagement Measurement via VLM Action Parsing and LLM Sequence Classification **⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2601.06394](https://arxiv.org/abs/2601.06394)
- **作者**: Ahmed Abdelkawy, Ahmed Elsayed, Asem Ali, Aly Farag, Thomas Tretter, Michael McIntyre
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①该论文针对课堂学生行为参与度测量中标注数据稀缺和忽略同伴上下文的问题。②提出了三阶段框架：首先用少样本适应微调视觉语言模型（VLM）进行学生动作识别；其次用滑动时间窗口将视频分段并生成动作序列；最后用大语言模型（LLM）结合课堂上下文分类整个序列为参与度等级。③相比已有方法，创新性地引入同伴动作作为上下文，并利用VLM和LLM的少样本能力减少标注需求。④摘要未提供具体性能数据，但强调框架在隐私受限场景下的适用性。
- **摘要（英）**: This paper tackles student engagement measurement in classrooms, addressing scarce annotations and ignored peer context. It proposes a three-stage framework: few-shot VLM adaptation for action recognition, sliding temporal windows to generate action sequences, and LLM-based sequence classification with classroom context. The novelty lies in incorporating peer actions and leveraging VLM/LLM few-shot capabilities, though no quantitative results are given in the abstract.
- **核心贡献**: 提出一个结合VLM和LLM的三阶段框架，利用同伴上下文进行少样本学生参与度测量。
- **创新点**: 将同伴动作作为上下文信息，并融合VLM动作解析与LLM序列分类。
- **结果**: 摘要未提供具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding student behavior in the classroom is essential to improve both pedagogical quality and student engagement. Existing methods for predicting student engagement typically require substantial annotated data to model the diversity of student behaviors, yet privacy concerns often restrict researchers to their own proprietary datasets. Moreover, the classroom context, represented in peers' actions, is ignored. To address the aforementioned limitation, we propose a novel three-stage framework for video-based student engagement measurement. First, we explore the few-shot adaptation of the vision-language model for student action recognition, which is fine-tuned to distinguish among action categories with a few training samples. Second, to handle continuous and unpredictable student actions, we utilize the sliding temporal window technique to divide each student's 2-minute-long video into non-overlapping segments. Each segment is assigned an action category via the fine-tuned VLM model, generating a sequence of action predictions. Finally, we leverage the large language model to classify this entire sequence of actions, together with the classroom context, as belonging to an engaged or disengaged student. The experimental results demonstrate the effectiveness of the proposed approach in identifying student engagement. The source code will be available at https://github.com/ahmed-nady/context_aware_student_engagement.

</details>

### Agentic Retoucher for Text-To-Image Generation **⭐⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2601.02046](https://arxiv.org/abs/2601.02046)
- **作者**: Shaocheng Shen, Jianfeng Liang, Chunlei Cai, Cong Geng, Huiyu Duan, Xiaoyun Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①该论文针对文本到图像（T2I）扩散模型生成图像中肢体、面部、文字等小尺度畸变问题，现有修复方法成本高或空间定位弱。②提出了Agentic Retoucher框架，将后生成修正重构为感知-推理-行动循环：感知代理学习上下文显著性进行细粒度畸变定位，推理代理通过渐进偏好对齐进行类人诊断，行动代理根据用户偏好规划局部修复。③相比已有方法，该框架整合感知证据、语言推理和可控修正到统一的自校正决策过程，并构建了GenBlemish-27K数据集（6K图像、27K畸变标注）用于细粒度监督和评估。④摘要未提供具体性能数据，但强调框架的层次化决策和数据集构建。
- **摘要（英）**: This paper addresses persistent small-scale distortions in T2I diffusion model outputs, where existing refinement methods are costly or lack spatial grounding. It proposes Agentic Retoucher, a hierarchical decision-driven framework reformulating correction as a perception-reasoning-action loop, with agents for contextual saliency-based localization, human-aligned diagnosis via preference alignment, and adaptive inpainting planning. The work also introduces GenBlemish-27K dataset for fine-grained supervision, though quantitative results are not reported in the abstract.
- **核心贡献**: 提出Agentic Retoucher框架和GenBlemish-27K数据集，用于T2I图像的细粒度畸变修复。
- **创新点**: 将后生成修正建模为感知-推理-行动的层次化决策循环，结合VLM和偏好对齐。
- **结果**: 摘要未提供具体数值，但框架和数据集有望提升修复精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-to-image (T2I) diffusion models such as SDXL and FLUX have achieved impressive photorealism, yet small-scale distortions remain pervasive in limbs, face, text and so on. Existing refinement approaches either perform costly iterative re-generation or rely on vision-language models (VLMs) with weak spatial grounding, leading to semantic drift and unreliable local edits. To close this gap, we propose Agentic Retoucher, a hierarchical decision-driven framework that reformulates post-generation correction as a human-like perception-reasoning-action loop. Specifically, we design (1) a perception agent that learns contextual saliency for fine-grained distortion localization under text-image consistency cues, (2) a reasoning agent that performs human-aligned inferential diagnosis via progressive preference alignment, and (3) an action agent that adaptively plans localized inpainting guided by user preference. This design integrates perceptual evidence, linguistic reasoning, and controllable correction into a unified, self-corrective decision process. To enable fine-grained supervision and quantitative evaluation, we further construct GenBlemish-27K, a dataset of 6K T2I images with 27K annotated artifact regions across 12 categories. Extensive experiments demonstrate that Agentic Retoucher consistently outperforms state-of-the-art methods in perceptual quality, distortion localization and human preference alignment, establishing a new paradigm for self-corrective and perceptually reliable T2I generation.

</details>

## 跨领域论文（完整笔记在其他领域）

- Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding → [multimodal](../multimodal/Guideline%202026.md)
- MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation → [multi-camera-perception](../multi-camera-perception/Guideline%202026.md)
- VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice → [multimodal](../multimodal/Guideline%202026.md)
- Purify then Guide: Rethinking Domain Generalization for Multimodal Face Anti-Spoofing → [multimodal](../multimodal/Guideline%202026.md)
- Privacy Beyond Pixels: Latent Anonymization for Privacy-Preserving Video Understanding → [video-understanding](../video-understanding/Guideline%202026.md)

<!-- COMPLETE v1 papers=4 -->
