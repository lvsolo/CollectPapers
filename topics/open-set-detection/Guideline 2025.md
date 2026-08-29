# Open-set Detection — 2025 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OVTR: End-to-End Open-Vocabulary Multiple Object Tracking with Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=GDS5eN65QY)
- **作者**: Jinyang Li, En Yu, Sijia Chen, Wenbing Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Revisit the Open Nature of Open Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openreview.net/forum?id=2vHIHrJAcI)
- **作者**: Qiming Huang, Han Hu, Jianbo Jiao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds.
- **链接**: [arXiv:2502.20041](https://arxiv.org/abs/2502.20041)
- **作者**: Hengshuo Chu, Xiang Deng, Qi Lv, Xiaoyang Chen, Yinchuan Li, Jianye Hao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D Affordance detection is a challenging problem with broad applications on various robotic tasks. Existing methods typically formulate the detection paradigm as a label-based semantic segmentation task. This paradigm relies on predefined labels and lacks the ability to comprehend complex natural language, resulting in limited generalization in open-world scene. To address these limitations, we reformulate the traditional affordance detection paradigm into \textit{Instruction Reasoning Affordance Segmentation} (IRAS) task. This task is designed to output a affordance mask region given a query reasoning text, which avoids fixed categories of input labels. We accordingly propose the \textit{3D-AffordanceLLM} (3D-ADLLM), a framework designed for reasoning affordance detection in 3D open-scene. Specifically, 3D-ADLLM introduces large language models (LLMs) to 3D affordance perception with a custom-designed decoder for generating affordance masks, thus achieving open-world reasoning affordance detection. In addition, given the scarcity of 3D affordance datasets for training large models, we seek to extract knowledge from general segmentation data and transfer it to affordance detection. Thus, we propose a multi-stage training strategy that begins with a novel pre-training task, i.e., \textit{Referring Object Part Segmentation}~(ROPS). This stage is designed to equip the model with general recognition and segmentation capabilities at the object-part level. Then followed by fine-tuning with the IRAS task, 3D-ADLLM obtains the reasoning ability for affordance detection. In summary, 3D-ADLLM leverages the rich world knowledge and human-object interaction reasoning ability of LLMs, achieving approximately an 8\% improvement in mIoU on open-vocabulary affordance detection tasks.

</details>

### Class Distribution-induced Attention Map for Open-vocabulary Semantic Segmentations.
- **链接**: [出版页](https://openreview.net/forum?id=CMqOfvD3tO)
- **作者**: Dong Un Kang, Hayeon Kim, Se Young Chun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### A Simple Framework for Open-Vocabulary Zero-Shot Segmentation.
- **链接**: [arXiv:2406.16085](https://arxiv.org/abs/2406.16085)
- **作者**: Thomas Stegmüller, Tim Lebailly, Nikola Dukic, Behzad Bozorgtabar, Tinne Tuytelaars, Jean-Philippe Thiran
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot classification capabilities naturally arise in models trained within a vision-language contrastive framework. Despite their classification prowess, these models struggle in dense tasks like zero-shot open-vocabulary segmentation. This deficiency is often attributed to the absence of localization cues in captions and the intertwined nature of the learning process, which encompasses both image representation learning and cross-modality alignment. To tackle these issues, we propose SimZSS, a Simple framework for open-vocabulary Zero-Shot Segmentation. The method is founded on two key principles: i) leveraging frozen vision-only models that exhibit spatial awareness while exclusively aligning the text encoder and ii) exploiting the discrete nature of text and linguistic knowledge to pinpoint local concepts within captions. By capitalizing on the quality of the visual representations, our method requires only image-caption pairs datasets and adapts to both small curated and large-scale noisy datasets. When trained on COCO Captions across 8 GPUs, SimZSS achieves state-of-the-art results on 7 out of 8 benchmark datasets in less than 15 minutes.

</details>

### Open-Vocabulary Customization from CLIP via Data-Free Knowledge Distillation.
- **链接**: [出版页](https://openreview.net/forum?id=1aF2D2CPHi)
- **作者**: Yongxian Wei, Zixuan Hu, Li Shen, Zhenyi Wang, Chun Yuan, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

## 跨领域论文（完整笔记在其他领域）

- Cyclic Contrastive Knowledge Transfer for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Open-YOLO 3D: Towards Fast and Accurate Open-Vocabulary 3D Instance Segmentation. → [object-detection](../object-detection/Guideline%202025.md)
- Towards Robust Multimodal Open-set Test-time Adaptation via Adaptive Entropy-aware Optimization. → [multimodal](../multimodal/Guideline%202025.md)
