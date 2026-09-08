# Mono 3D Detection — 2026 Guideline

> 领域: 单目 3D 检测（Monocular 3D Object Detection，含单目深度支撑的 3D 感知）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2025](Guideline%202025.md), [2024](Guideline%202024.md), [2023](Guideline%202023.md), [2022](Guideline%202022.md), [2021](Guideline%202021.md)

### Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2601.07298](https://arxiv.org/abs/2601.07298)
- **作者**: Jianghao Yin, Qingbin Li, Kun Sun, Cheng Ding, Jie Wang, Qin Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: 这篇论文针对多模态大语言模型（MLLMs）在多图像推理任务中性能显著下降的问题，提出了一种受人类认知过程启发的元动作框架（CINEMA），将多图像推理分解为五个结构化元动作：全局、聚焦、提示、思考和回答，以显式建模人类自然的认知步骤。为冷启动训练，引入了基于检索的树采样策略生成高质量元动作轨迹；在强化学习阶段，采用两阶段范式，先用多样性保持策略避免熵坍缩，再用DAPO退火利用阶段逐步增强利用。构建了包含56k冷启动和58k强化学习实例的数据集，覆盖多图像、多帧和单图像任务，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the degraded performance of Multimodal Large Language Models (MLLMs) in multi-image reasoning by proposing a Cognition-Inspired Meta-Action Framework (CINEMA) that decomposes reasoning into five meta-actions: Global, Focus, Hint, Think, and Answer. It introduces a Retrieval-Based Tree Sampling strategy for cold-start training and a two-stage reinforcement learning paradigm with diversity preservation and annealed exploitation. A dataset of 56k cold-start and 58k RL instances is constructed, though no specific performance metrics are reported in the abstract.
- **核心贡献**: 提出了CINEMA元动作框架，将多图像推理分解为可学习的认知步骤，并配套了训练策略和数据集。
- **创新点**: 将人类认知过程建模为结构化元动作，结合检索式树采样和两阶段强化学习优化推理。
- **结果**: 构建了大规模训练数据，但摘要未给出具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Multimodal Large Language Models (MLLMs) excel at single-image understanding, they exhibit significantly degraded performance in multi-image reasoning scenarios. Multi-image reasoning presents fundamental challenges including complex inter-relationships between images and scattered critical information across image sets. Inspired by human cognitive processes, we propose a Cognition-Inspired Meta-Action Framework (CINEMA), which decomposes multi-image reasoning into five structured meta-actions: Global, Focus, Hint, Think, and Answer, explicitly modeling the sequential cognitive steps humans naturally employ. For cold-start training, we introduce a Retrieval-Based Tree Sampling strategy that generates high-quality meta-action trajectories to bootstrap the model with reasoning patterns. During reinforcement learning, we adopt a two-stage paradigm: an exploration phase with Diversity-Preserving Strategy to avoid entropy collapse, followed by an annealed exploitation phase with DAPO to gradually strengthen exploitation. To train our model, we construct a dataset of 56k cold-start and 58k reinforcement learning instances spanning multi-image, multi-frame, and single-image tasks. We conduct extensive evaluations on multi-image reasoning benchmarks, video understanding benchmarks, and single-image benchmarks, achieving competitive state-of-the-art performance on several key benchmarks. Our model surpasses GPT-4o on the MUIR and MVMath benchmarks and notably outperforms specialized video reasoning models on video understanding benchmarks, demonstrating the effectiveness and generalizability of our human cognition-inspired reasoning framework.

</details>
<!-- COMPLETE v1 papers=1 -->
