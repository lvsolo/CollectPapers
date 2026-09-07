# Video Understanding — 2026 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Mind the Generative Details: Direct Localized Detail Preference Optimization for Video Diffusion Models
- **链接**: [arXiv:2601.04068](https://arxiv.org/abs/2601.04068) · [代码](https://github.com/1170300714/Local-DPO)
- **作者**: Zitong Huang, Kaidong Zhang, Yukang Ding, Chao Gao, Rui Ding, Ying Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aligning text-to-video diffusion models with human preferences is crucial for generating high-quality videos. Existing Direct Preference Otimization (DPO) methods rely on multi-sample ranking and task-specific critic models, which is inefficient and often yields ambiguous global supervision. To address these limitations, we propose LocalDPO, a novel post-training framework that constructs localized preference pairs from real videos and optimizes alignment at the spatio-temporal region level. We design an automated pipeline to efficiently collect preference pair data that generates preference pairs with a single inference per prompt, eliminating the need for external critic models or manual annotation. Specifically, we treat high-quality real videos as positive samples and generate corresponding negatives by locally corrupting them with random spatio-temporal masks and restoring only the masked regions using the frozen base model. During training, we introduce a region-aware DPO loss that restricts preference learning to corrupted areas for rapid convergence. Experiments on Wan2.1 and CogVideoX demonstrate that LocalDPO consistently improves video fidelity, temporal coherence and human preference scores over other post-training approaches, establishing a more efficient and fine-grained paradigm for video generator alignment.The code is available at https://github.com/1170300714/Local-DPO.

</details>

## 跨领域论文（完整笔记在其他领域）

- Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding → [multimodal](../multimodal/Guideline%202026.md)
- Context Matters: Peer-Aware Student Behavioral Engagement Measurement via VLM Action Parsing and LLM Sequence Classification → [vlm](../vlm/Guideline%202026.md)
- VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice → [multimodal](../multimodal/Guideline%202026.md)
<!-- COMPLETE v1 papers=4 -->
