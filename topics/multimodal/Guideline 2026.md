# Multimodal — 2026 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DeepEyesV2: Toward Agentic Multimodal Model
- **链接**: [arXiv:2511.05271](https://arxiv.org/abs/2511.05271)
- **作者**: Jack Hong, Chenxiao Zhao, ChengLin Zhu, Weiheng Lu, Guohai Xu, Xing Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2026

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Agentic multimodal models should not only comprehend text and images, but also actively invoke external tools, such as code execution environments and web search, and integrate these operations into reasoning. In this work, we introduce DeepEyesV2 and explore how to build an agentic multimodal model from the perspectives of data construction, training methods, and model evaluation. We observe that direct reinforcement learning alone fails to induce robust tool-use behavior. This phenomenon motivates a two-stage training pipeline: a cold-start stage to establish tool-use patterns, and reinforcement learning stage to further refine tool invocation. We curate a diverse, moderately challenging training dataset, specifically including examples where tool use is beneficial. We further introduce RealX-Bench, a comprehensive benchmark designed to evaluate real-world multimodal reasoning, which inherently requires the integration of multiple capabilities, including perception, search, and reasoning. We evaluate DeepEyesV2 on RealX-Bench and other representative benchmarks, demonstrating its effectiveness across real-world understanding, mathematical reasoning, and search-intensive tasks. Moreover, DeepEyesV2 exhibits task-adaptive tool invocation, tending to use image operations for perception tasks and numerical computations for reasoning tasks. Reinforcement learning further enables complex tool combinations and allows model to selectively invoke tools based on context. We hope our study can provide guidance for community in developing agentic multimodal models.

</details>

## 跨领域论文（完整笔记在其他领域）

- Omni-View: Unlocking How Generation Facilitates Understanding in Unified 3D Model based on Multiview images → [multi-camera-perception](../multi-camera-perception/Guideline%202026.md)
<!-- COMPLETE v1 papers=2 -->
