# BEV — 2024 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks.
- **链接**: [arXiv:2407.13517](https://arxiv.org/abs/2407.13517) · [代码](https://github.com/SehwanChoi0307/Mask2Map) · 📚 被引 18
- **作者**: Sehwan Choi, Jungho Kim, Hongjae Shin, Jun Won Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce Mask2Map, a novel end-to-end online HD map construction method designed for autonomous driving applications. Our approach focuses on predicting the class and ordered point set of map instances within a scene, represented in the bird's eye view (BEV). Mask2Map consists of two primary components: the Instance-Level Mask Prediction Network (IMPNet) and the Mask-Driven Map Prediction Network (MMPNet). IMPNet generates Mask-Aware Queries and BEV Segmentation Masks to capture comprehensive semantic information globally. Subsequently, MMPNet enhances these query features using local contextual information through two submodules: the Positional Query Generator (PQG) and the Geometric Feature Extractor (GFE). PQG extracts instance-level positional queries by embedding BEV positional information into Mask-Aware Queries, while GFE utilizes BEV Segmentation Masks to generate point-level geometric features. However, we observed limited performance in Mask2Map due to inter-network inconsistency stemming from different predictions to Ground Truth (GT) matching between IMPNet and MMPNet. To tackle this challenge, we propose the Inter-network Denoising Training method, which guides the model to denoise the output affected by both noisy GT queries and perturbed GT Segmentation Masks. Our evaluation conducted on nuScenes and Argoverse2 benchmarks demonstrates that Mask2Map achieves remarkable performance improvements over previous state-of-the-art methods, with gains of 10.1% mAP and 4.1 mAP, respectively. Our code can be found at https://github.com/SehwanChoi0307/Mask2Map.

</details>

### DA-BEV: Unsupervised Domain Adaptation for Bird's Eye View Perception.
- **链接**: [arXiv:2401.08687](https://arxiv.org/abs/2401.08687) · 📚 被引 2
- **作者**: Kai Jiang, Jiaxing Huang, Weiying Xie, Jie Lei, Yunsong Li, Ling Shao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-only Bird's Eye View (BEV) has demonstrated great potential in environment perception in a 3D space. However, most existing studies were conducted under a supervised setup which cannot scale well while handling various new data. Unsupervised domain adaptive BEV, which effective learning from various unlabelled target data, is far under-explored. In this work, we design DA-BEV, the first domain adaptive camera-only BEV framework that addresses domain adaptive BEV challenges by exploiting the complementary nature of image-view features and BEV features. DA-BEV introduces the idea of query into the domain adaptation framework to derive useful information from image-view and BEV features. It consists of two query-based designs, namely, query-based adversarial learning (QAL) and query-based self-training (QST), which exploits image-view features or BEV features to regularize the adaptation of the other. Extensive experiments show that DA-BEV achieves superior domain adaptive BEV perception performance consistently across multiple datasets and tasks such as 3D object detection and 3D scene segmentation.

</details>

## 跨领域论文（完整笔记在其他领域）

- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Diffusion Model for Robust Multi-sensor Fusion in 3D Object Detection and BEV Segmentation. → [3d-detection](../3d-detection/Guideline%202024.md)
- GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
