# Video Understanding — 2026 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Mind the Generative Details: Direct Localized Detail Preference Optimization for Video Diffusion Models **⭐⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2601.04068](https://arxiv.org/abs/2601.04068)
- **作者**: Zitong Huang, Kaidong Zhang, Yukang Ding, Chao Gao, Rui Ding, Ying Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2026
- **摘要（中）**: ①这篇论文针对文本到视频扩散模型与人类偏好对齐中现有DPO方法依赖多样本排序和任务特定批评模型、效率低且全局监督模糊的问题。②提出了LocalDPO框架，通过从真实视频构建局部偏好对，在时空区域级别优化对齐，利用随机时空掩码和冻结基础模型生成负样本，并引入区域感知DPO损失。③相比已有工作，改进在于单次推理生成偏好对，无需外部批评模型或手动标注，并将偏好学习限制在损坏区域以加速收敛。④在Wan2.1和CogVideoX上的实验表明，LocalDPO持续提升视频保真度、时间连贯性和人类偏好，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the inefficiency and ambiguous global supervision of existing DPO methods for aligning text-to-video diffusion models with human preferences. It proposes LocalDPO, a post-training framework that constructs localized preference pairs from real videos via random spatio-temporal masking and restoration, using a region-aware DPO loss for rapid convergence. Experiments on Wan2.1 and CogVideoX show consistent improvements in video fidelity, temporal coherence, and human preference.
- **核心贡献**: 提出LocalDPO，一种无需外部批评模型的局部偏好优化框架，用于视频扩散模型对齐。
- **创新点**: 通过局部时空损坏和区域感知损失实现高效偏好学习。
- **结果**: 在多个视频模型上提升生成质量与时间连贯性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aligning text-to-video diffusion models with human preferences is crucial for generating high-quality videos. Existing Direct Preference Otimization (DPO) methods rely on multi-sample ranking and task-specific critic models, which is inefficient and often yields ambiguous global supervision. To address these limitations, we propose LocalDPO, a novel post-training framework that constructs localized preference pairs from real videos and optimizes alignment at the spatio-temporal region level. We design an automated pipeline to efficiently collect preference pair data that generates preference pairs with a single inference per prompt, eliminating the need for external critic models or manual annotation. Specifically, we treat high-quality real videos as positive samples and generate corresponding negatives by locally corrupting them with random spatio-temporal masks and restoring only the masked regions using the frozen base model. During training, we introduce a region-aware DPO loss that restricts preference learning to corrupted areas for rapid convergence. Experiments on Wan2.1 and CogVideoX demonstrate that LocalDPO consistently improves video fidelity, temporal coherence and human preference scores over other post-training approaches, establishing a more efficient and fine-grained paradigm for video generator alignment.The code is available at https://github.com/1170300714/Local-DPO.

</details>

### Privacy Beyond Pixels: Latent Anonymization for Privacy-Preserving Video Understanding **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2511.08666](https://arxiv.org/abs/2511.08666)
- **作者**: Joseph Fioresi, Ishan Rajendrakumar Dave, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2026
- **摘要（中）**: ①该论文针对视频基础模型在特征提取和存储过程中泄露敏感个人信息（如肤色、性别、服装）的隐私问题，现有像素级匿名化方法需重训整个模型且任务特定，不适用于视频基础模型。②提出了一种轻量级匿名化适配模块（AAM），在潜在空间中操作，以即插即用方式应用于冻结的视频编码器，去除视频特征中的私有信息同时保留通用任务效用。③设计了三个训练目标：基于片段的自监督隐私目标以减少静态片段间的互信息、协同训练目标以保留效用，以及另一个未完整提及的目标。④摘要未提供具体数据，但方法旨在最小化微调和特征重提取的计算负担，适用于视频基础模型。
- **摘要（英）**: This paper addresses privacy leakage in video foundation models by proposing a latent-space Anonymizing Adapter Module (AAM) that removes sensitive information from video features while preserving task utility. It operates plug-and-play on frozen encoders, avoiding retraining, and uses novel training objectives including clip-level self-supervised privacy and co-training for utility retention. The approach targets computational efficiency and generalizability across downstream tasks.
- **核心贡献**: 提出了一种在潜在空间中操作的轻量级匿名化适配模块，用于视频基础模型的隐私保护。
- **创新点**: 将隐私匿名化从像素级转移到潜在特征级，并采用即插即用设计适配冻结的视频编码器。
- **结果**: 摘要未提供具体量化结果，但声称能有效去除私有信息并保留任务效用，同时降低计算开销。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel formulation of visual privacy preservation for video foundation models that operates entirely in the latent space. While spatio-temporal features learned by foundation models have deepened general understanding of video content, sharing or storing these extracted visual features for downstream tasks inadvertently reveals sensitive personal information like skin color, gender, or clothing. Current privacy preservation methods focus on input-pixel-level anonymization, which requires retraining the entire utility video model and results in task-specific anonymization, making them unsuitable for recent video foundational models. To address these challenges, we introduce a lightweight Anonymizing Adapter Module (AAM) that removes private information from video features while retaining general task utility. AAM can be applied in a plug-and-play fashion to frozen video encoders, minimizing the computational burden of finetuning and re-extracting features. Our framework employs three newly designed training objectives: (1) a clip-level self-supervised privacy objective to reduce mutual information between static clips, (2) a co-training objective to retain utility across seen tasks, and (3) a latent consistency loss for generalization on unseen tasks. Our extensive evaluations demonstrate a significant 35% reduction in privacy leakage while maintaining near-baseline utility performance across various downstream tasks: Action Recognition (Kinetics400, UCF101, HMDB51), Temporal Action Detection (THUMOS14), and Anomaly Detection (UCF-Crime). We also provide an analysis on anonymization for sensitive temporal attribute recognition. Additionally, we propose new protocols for assessing gender bias in action recognition models, showing that our method effectively mitigates such biases and promotes more equitable video understanding. https://joefioresi718.github.io/SPLAVU_webpage/

</details>

## 跨领域论文（完整笔记在其他领域）

- Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding → [multimodal](../multimodal/Guideline%202026.md)
- Context Matters: Peer-Aware Student Behavioral Engagement Measurement via VLM Action Parsing and LLM Sequence Classification → [vlm](../vlm/Guideline%202026.md)
- VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice → [multimodal](../multimodal/Guideline%202026.md)

<!-- COMPLETE v1 papers=2 -->
