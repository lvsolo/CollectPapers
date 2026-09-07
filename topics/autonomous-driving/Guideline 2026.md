# Autonomous Driving — 2026 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2512.20563](https://arxiv.org/abs/2512.20563)
- **作者**: Long Nguyen, Micha Fauth, Bernhard Jaeger, Daniel Dauner, Maximilian Igl, Andreas Geiger et al.
- **🏷️ 机构**: University of Tübingen
- **会议**: CVPR 2026
- **摘要（中）**: ①针对端到端驾驶中模仿学习因专家与学生在可见性、不确定性和导航意图上的不对称性导致闭环性能不佳的问题。②提出LEAD框架，通过实证分析这些不对称性，并采取实际干预措施（如增强学生感知、明确意图表示）来缩小差距，最终训练出TransFuser v6（TFv6）策略。③相比已有工作，系统性地识别并解决了专家-学生不对称问题，而非仅依赖数据量或模型容量。④在CARLA基准上取得新SOTA，Bench2Drive上DS达95，Longest6 v2和Town13上性能翻倍以上。
- **摘要（英）**: This paper addresses the learner-expert asymmetry in end-to-end driving, where privileged experts outperform sensor-based students due to visibility, uncertainty, and intent gaps. It proposes LEAD with practical interventions to narrow these gaps, yielding TransFuser v6 that achieves state-of-the-art results on CARLA benchmarks, including 95 DS on Bench2Drive and doubled performance on Longest6 v2 and Town13.
- **核心贡献**: 核心贡献是识别并缓解专家-学生不对称性，提出可操作的干预措施，推动端到端驾驶性能达到新高度。
- **创新点**: 创新点在于从实证角度量化不对称性影响，并设计多维度干预策略而非单一架构改进。
- **结果**: 在CARLA多个基准上刷新SOTA，DS达95，Longest6 v2和Town13性能翻倍。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Simulators can generate virtually unlimited driving data, yet imitation learning policies in simulation still struggle to achieve robust closed-loop performance. Motivated by this gap, we empirically study how misalignment between privileged expert demonstrations and sensor-based student observations can limit the effectiveness of imitation learning. More precisely, experts have significantly higher visibility (e.g., ignoring occlusions) and far lower uncertainty (e.g., knowing other vehicles' actions), making them difficult to imitate reliably. Furthermore, navigational intent (i.e., the route to follow) is under-specified in student models at test time via only a single target point. We demonstrate that these asymmetries can measurably limit driving performance in CARLA and offer practical interventions to address them. After careful modifications to narrow the gaps between expert and student, our TransFuser v6 (TFv6) student policy achieves a new state of the art on all major publicly available CARLA closed-loop benchmarks, reaching 95 DS on Bench2Drive and more than doubling prior performances on Longest6~v2 and Town13. Additionally, by integrating perception supervision from our dataset into a shared sim-to-real pipeline, we show consistent gains on the NAVSIM and Waymo Vision-Based End-to-End driving benchmarks. Our code, data, and models are publicly available at https://github.com/autonomousvision/lead.

</details>

### KnowVal: A Knowledge-Augmented and Value-Guided Autonomous Driving System **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2512.20299](https://arxiv.org/abs/2512.20299)
- **作者**: Zhongyu Xia, Wenhao Chen, Yongtao Wang, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2026
- **摘要（中）**: ①针对现有自动驾驶系统依赖数据驱动学习，难以捕捉决策背后的复杂逻辑和价值观对齐问题。②提出KnowVal系统，构建包含交通法规、防御性驾驶原则和伦理规范的综合驾驶知识图谱，并设计基于LLM的高效检索机制，同时开发人类偏好数据集训练价值模型以指导轨迹评估。③相比已有工作，将知识增强与价值对齐结合，提升可解释性和安全性。④在nuScenes上实现最低碰撞率，在Bench2Drive和NVISIM上取得SOTA结果。
- **摘要（英）**: This paper tackles the challenge of capturing complex decision logic and value alignment in autonomous driving, which data-driven methods often miss. It proposes KnowVal, integrating a comprehensive driving knowledge graph with LLM-based retrieval and a value model trained on human preferences, achieving the lowest collision rate on nuScenes and SOTA results on Bench2Drive and NVISIM.
- **核心贡献**: 核心贡献是提出知识增强与价值引导的自动驾驶框架，提升规划性能与安全性。
- **创新点**: 创新点在于将显式驾驶知识与人类价值偏好结合，实现可解释的轨迹评估。
- **结果**: 在nuScenes上碰撞率最低，Bench2Drive和NVISIM上达到SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual-language reasoning, driving knowledge, and value alignment are essential for advanced autonomous driving systems. However, existing approaches largely rely on data-driven learning, making it difficult to capture the complex logic underlying decision-making through imitation or limited reinforcement rewards. To address this, we propose KnowVal, a new autonomous driving system that enables visual-language reasoning through the synergistic integration of open-world perception and knowledge retrieval. Specifically, we construct a comprehensive driving knowledge graph that encodes traffic laws, defensive driving principles, and ethical norms, complemented by an efficient LLM-based retrieval mechanism tailored for driving scenarios. Furthermore, we develop a human-preference dataset and train a Value Model to guide interpretable, value-aligned trajectory assessment. Experimental results show that our method substantially improves planning performance while remaining compatible with existing architectures. Notably, KnowVal achieves the lowest collision rate on nuScenes and state-of-the-art results on Bench2Drive and NVISIM.

</details>

### Latent Chain-of-Thought World Modeling for End-to-End Driving **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2512.10226](https://arxiv.org/abs/2512.10226)
- **作者**: Shuhan Tan, Kashyap Chitta, Yuxiao Chen, Ran Tian, Yurong You, Yan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①针对VLA模型在自动驾驶中使用自然语言进行链式思考推理效率低的问题。②提出Latent-CoT-Drive（LCDrive），在潜在空间中表达链式思考，通过动作提议令牌和世界模型令牌交错推理，并利用真实未来轨迹冷启动训练，再通过闭环强化学习增强推理能力。③相比已有工作，用潜在语言替代自然语言，统一推理与决策表示，提升效率。④在大规模端到端驾驶任务上验证了有效性，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the inefficiency of natural language chain-of-thought reasoning in VLA models for driving. It proposes LCDrive, which performs reasoning in a latent space using action-proposal and world model tokens, trained with cold start on ground-truth rollouts and closed-loop RL, improving reasoning efficiency and driving performance.
- **核心贡献**: 核心贡献是提出潜在空间链式思考世界模型，统一推理与决策。
- **创新点**: 创新点在于用动作对齐的潜在语言替代自然语言进行推理。
- **结果**: 在大规模端到端驾驶任务上验证有效性，具体数值未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

</details>

### SPACeR: Self-Play Anchoring with Centralized Reference Models **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2510.18060](https://arxiv.org/abs/2510.18060)
- **作者**: Wei-Jer Chang, Akshay Rangesh, Kevin Joseph, Matthew Strong, Masayoshi Tomizuka, Yihan Hu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2026
- **摘要（中）**: ①针对自动驾驶模拟中智能体策略需兼具拟人性和可扩展性，但模仿学习模型推理慢且难以适应闭环，而自博弈RL易偏离人类行为的问题。②提出SPACeR框架，利用预训练的令牌化自回归运动模型作为集中参考策略，指导分散自博弈RL，通过似然奖励和KL散度锚定策略到人类驾驶分布。③相比已有工作，结合模仿学习的拟人性和RL的可扩展性，无需复杂奖励塑形。④在Waymo Sim Agents Challenge上取得优异成绩，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the trade-off between human-like behavior and scalability in AV sim agents, where imitation models are slow and RL diverges from human norms. It proposes SPACeR, using a pretrained tokenized motion model as a centralized reference to guide self-play RL via likelihood rewards and KL divergence, achieving strong results on the Waymo Sim Agents Challenge.
- **核心贡献**: 核心贡献是提出集中参考模型引导的自博弈框架，平衡拟人性与可扩展性。
- **创新点**: 创新点在于利用预训练运动模型作为参考策略，通过KL散度锚定RL训练。
- **结果**: 在Waymo Sim Agents Challenge上取得优异成绩，具体数值未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Developing autonomous vehicles (AVs) requires not only safety and efficiency, but also realistic, human-like behaviors that are socially aware and predictable. Achieving this requires sim agent policies that are human-like, fast, and scalable in multi-agent settings. Recent progress in imitation learning with large diffusion-based or tokenized models has shown that behaviors can be captured directly from human driving data, producing realistic policies. However, these models are computationally expensive, slow during inference, and struggle to adapt in reactive, closed-loop scenarios. In contrast, self-play reinforcement learning (RL) scales efficiently and naturally captures multi-agent interactions, but it often relies on heuristics and reward shaping, and the resulting policies can diverge from human norms. We propose SPACeR, a framework that leverages a pretrained tokenized autoregressive motion model as a centralized reference policy to guide decentralized self-play. The reference model provides likelihood rewards and KL divergence, anchoring policies to the human driving distribution while preserving RL scalability. Evaluated on the Waymo Sim Agents Challenge, our method achieves competitive performance with imitation-learned policies while being up to 10x faster at inference and 50x smaller in parameter size than large generative models. In addition, we demonstrate in closed-loop ego planning evaluation tasks that our sim agents can effectively measure planner quality with fast and scalable traffic simulation, establishing a new paradigm for testing autonomous driving policies.

</details>

<!-- COMPLETE v1 papers=4 -->
