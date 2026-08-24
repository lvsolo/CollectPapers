# 📚 arXiv 每日论文报告（我的领域）

**报告日期**: 2026-08-24  
**论文来源**: [arXiv cs.CV Recent](https://arxiv.org/list/cs.CV/recent)  
**关注论文数**: 14 篇（关键词匹配模式，未配置 LLM）

> 匹配领域: 3D Detection、BEV、Occupancy、Multi-camera Perception、Tracking、Open Vocabulary Detection、FOD Detection、VLM、Vision Transformer、Self-supervised Vision、Video Understanding、Multimodal、Continual Learning、Neural Architecture Search、Network Pruning、Knowledge Distillation

## 📑 目录

- [VLM](#vlm) (8篇)
- [Multimodal](#multimodal) (6篇)

## VLM

### 1. ArtiMo: Agent-Driven Articulated Mesh Animation

- **arXiv ID**: [2608.20699](https://arxiv.org/abs/2608.20699)  · [📄 PDF](https://arxiv.org/pdf/2608.20699)
- **作者**: Chunyu Zou, Peng Dai, Yi-Hua Huang et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Animating articulated 3D meshes via text requires satisfying strict kinematic constraints, modeling causal interactions between parts, and achieving instruction fidelity. Due to the absence of task-specific training data and explicit articulation supervision, existing data-driven mesh animation methods are largely inapplicable to this setting.

### 2. Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs

- **arXiv ID**: [2608.20999](https://arxiv.org/abs/2608.20999)  · [📄 PDF](https://arxiv.org/pdf/2608.20999)
- **作者**: Haiming Li, Yingsheng Liu, Jingmin Zhu et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Multimodal LLMs apply the language model interface to visual inputs, where ordinal regression tasks such as age estimation, image quality assessment, and disease grading require autoregressive decisions over ordered class labels. We ask whether MLLMs reliably convert internal ordinal evidence into ordered digit-token outputs.

### 3. Identify, Locate, Link: End-to-End Key-Value Extraction from Document Images

- **arXiv ID**: [2608.20868](https://arxiv.org/abs/2608.20868)  · [📄 PDF](https://arxiv.org/pdf/2608.20868)
- **作者**: A. Said Gurbuz, Ahmed Nassar, Christoph Auer et al. (11 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CL
- **摘要摘录**: Document processing pipelines traditionally cascade optical character recognition (OCR) engines with downstream models for structured information extraction, leading to multi-stage error propagation. We fine-tune SmolDocling, a compact 256M-parameter vision-language model (VLM), to perform end-to-end key-value extraction directly from document images, jointly solving identification, localization, and association in a single pass without OCR preprocessing.

### 4. When Generated Images Look Right and Retrieve Wrong: Coverage-Guided Cross-Scale Re-Indexing for Knowledge-Faithful Generative Perception

- **arXiv ID**: [2608.20810](https://arxiv.org/abs/2608.20810)  · [📄 PDF](https://arxiv.org/pdf/2608.20810)
- **作者**: Guangyuan Dong, Chuang Liu, Yangchen Zeng et al. (9 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.MM, cs.AI, cs.CV
- **摘要摘录**: Multimodal information systems increasingly route generated visual content back through the same vision-language index that informed its production, so the output must remain retrievable by the queries it was meant to serve. When the scene contains entities at vastly different scales, existing language-guided generators condition on a single, globally pooled text embedding and quietly drop scale-specific concepts, breaking concept-query retrieval even when pixel fidelity is high.

### 5. AffordAny: Open-World 3D Affordance Grounding from Monocular RGB Images via Vision-Language-Guided Geometric Reasoning

- **arXiv ID**: [2608.20720](https://arxiv.org/abs/2608.20720)  · [📄 PDF](https://arxiv.org/pdf/2608.20720)
- **作者**: Junqi Wu, Kaihua Tang, Xuanwen Chen et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Open-world 3D affordance grounding requires localizing functional object parts in 3D given free-form language queries. Existing methods typically assume pre-built object-centric 3D geometry and closed affordance ontologies, limiting deployment from raw RGB observations.

### 6. ES-VP : Energy-Shaped Dynamic Visual Prompting for Efficient Model Adaptation

- **arXiv ID**: [2608.21194](https://arxiv.org/abs/2608.21194)  · [📄 PDF](https://arxiv.org/pdf/2608.21194)
- **作者**: Can Jin, Ying Li, Jingchen Sun et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Visual prompting (VP) has emerged as a parameter-efficient method for adapting pre-trained models to downstream tasks. However, existing approaches encounter a trade-off between flexibility and efficiency.

### 7. TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming

- **arXiv ID**: [2608.20958](https://arxiv.org/abs/2608.20958)  · [📄 PDF](https://arxiv.org/pdf/2608.20958)
- **作者**: Yibo Hu, Yu Qian, Mao Gu et al. (9 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.AI, cs.CV
- **摘要摘录**: E-commerce live streaming requires omni-modal understanding of noisy, temporally extended streams, where product facts are distributed across speech, video frames, product images, overlaid text, and user queries. We present TLive-Omni, an omni-modal understanding model tailored to live-commerce scenarios.

### 8. OccluRank: Controllable Occlusion-Aware Layout-to-Image Generation by Adding Just an Ordinal Rank

- **arXiv ID**: [2608.20932](https://arxiv.org/abs/2608.20932)  · [📄 PDF](https://arxiv.org/pdf/2608.20932)
- **作者**: Wenyang Hong, Yuan Wang, Yanbin Hao et al. (8 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV
- **摘要摘录**: Layout-to-image generation enables explicit spatial control through bounding-box layouts, yet bounding boxes specify only instance locations and cannot represent their occlusion order. Existing methods may rely on additional geometric conditions, employ complex inference procedures, or aggregate independently constructed instance representations without explicitly modeling their occlusion-dependent interactions.

---

## Multimodal

### 1. EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking

- **arXiv ID**: [2608.20886](https://arxiv.org/abs/2608.20886)  · [📄 PDF](https://arxiv.org/pdf/2608.20886)
- **作者**: Enjun Du, Siyi Liu, Zirong Chen et al. (11 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.LG
- **摘要摘录**: Real-world image search queries are multimodal and compositional: ``find this shirt in pink'' specifies an entity to retain, an attribute to modify, and context to ignore. Yet existing re-rankers either compress such multifaceted relevance into an opaque embedding or rely on free-form chain-of-thought that easily omits or hallucinates fine-grained constraints.

### 2. Multi-Modal Traffic Sign Detection with Semantic Attributes for Autonomous Driving

- **arXiv ID**: [2608.20874](https://arxiv.org/abs/2608.20874)  · [📄 PDF](https://arxiv.org/pdf/2608.20874)
- **作者**: Meda Lazar, Sourab Sridhar, Shashwata Gupta et al. (6 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.RO
- **摘要摘录**: Reliable traffic sign detection is a prerequisite for the global deployment of autonomous driving systems, where regulatory compliance and road safety depend on perceiving signs correctly across regions, ranges, and weather conditions. Despite recent progress, vision-based methods continue to face three fundamental limitations: poor cross-regional generalization due to high diversity across countries, degraded performance on small-object detection at long ranges (traffic signs occupy as little a

### 3. Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation

- **arXiv ID**: [2608.20756](https://arxiv.org/abs/2608.20756)  · [📄 PDF](https://arxiv.org/pdf/2608.20756)
- **作者**: Rujin Liang, Zhongpu Chen, Yuhao Lei et al. (4 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other as

### 4. MigrationNarrate: A Dataset for Detection of Migration Narratives in YouTube Videos

- **arXiv ID**: [2608.20984](https://arxiv.org/abs/2608.20984)  · [📄 PDF](https://arxiv.org/pdf/2608.20984)
- **作者**: Fatima Haouari, Carolina Scarton, Kalina Bontcheva
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.CL, cs.CY
- **摘要摘录**: Narratives are central to how social communication is framed, making their detection critical for understanding and analysing public discourse. Prior work has explored narrative detection and extraction across diverse domains; however, migration narratives remain significantly understudied, primarily due to the absence of dedicated annotated datasets.

### 5. KoViDoRe: Korean Visual Document Retrieval

- **arXiv ID**: [2608.20840](https://arxiv.org/abs/2608.20840)  · [📄 PDF](https://arxiv.org/pdf/2608.20840)
- **作者**: Yongbin Choi, Yongwoo Song, Mujeen Sung
- **提交日期**: 2026-08-21 · **分类**: cs.IR, cs.CV
- **摘要摘录**: Recent advances in multimodal retrieval have improved the ability to retrieve information from visually rich documents such as PDFs and reports. However, existing benchmarks remain largely centered on English and provide limited coverage of Korean visual documents with complex structures.

### 6. TRACE: Training-time Report-guided and Clinically Ordered Concept Editing

- **arXiv ID**: [2608.20809](https://arxiv.org/abs/2608.20809)  · [📄 PDF](https://arxiv.org/pdf/2608.20809)
- **作者**: Wentao Yue, Tianyou Lai, Jiayu Luo et al. (7 authors)
- **提交日期**: 2026-08-21 · **分类**: cs.CV, cs.AI
- **摘要摘录**: Breast ultrasound diagnosis relies on clinically meaningful semantic concepts, yet most deep learning methods adopt end-to-end image-to-label paradigms that lack interpretability and robustness. While concept-based approaches offer a promising alternative, they often assume complete annotations or require multimodal inputs at inference, which significantly limits their real-world applicability.

---

## 📊 统计

| 领域 | 论文数 |
|------|--------|
| VLM | 8 |
| Multimodal | 6 |
| **总计** | **14** |