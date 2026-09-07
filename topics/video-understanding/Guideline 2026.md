# Video Understanding — 2026 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Privacy Beyond Pixels: Latent Anonymization for Privacy-Preserving Video Understanding
- **链接**: [arXiv:2511.08666](https://arxiv.org/abs/2511.08666)
- **作者**: Joseph Fioresi, Ishan Rajendrakumar Dave, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2026

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel formulation of visual privacy preservation for video foundation models that operates entirely in the latent space. While spatio-temporal features learned by foundation models have deepened general understanding of video content, sharing or storing these extracted visual features for downstream tasks inadvertently reveals sensitive personal information like skin color, gender, or clothing. Current privacy preservation methods focus on input-pixel-level anonymization, which requires retraining the entire utility video model and results in task-specific anonymization, making them unsuitable for recent video foundational models. To address these challenges, we introduce a lightweight Anonymizing Adapter Module (AAM) that removes private information from video features while retaining general task utility. AAM can be applied in a plug-and-play fashion to frozen video encoders, minimizing the computational burden of finetuning and re-extracting features. Our framework employs three newly designed training objectives: (1) a clip-level self-supervised privacy objective to reduce mutual information between static clips, (2) a co-training objective to retain utility across seen tasks, and (3) a latent consistency loss for generalization on unseen tasks. Our extensive evaluations demonstrate a significant 35% reduction in privacy leakage while maintaining near-baseline utility performance across various downstream tasks: Action Recognition (Kinetics400, UCF101, HMDB51), Temporal Action Detection (THUMOS14), and Anomaly Detection (UCF-Crime). We also provide an analysis on anonymization for sensitive temporal attribute recognition. Additionally, we propose new protocols for assessing gender bias in action recognition models, showing that our method effectively mitigates such biases and promotes more equitable video understanding. https://joefioresi718.github.io/SPLAVU_webpage/

</details>
<!-- COMPLETE v1 papers=1 -->
