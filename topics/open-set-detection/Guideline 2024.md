# Open-set Detection — 2024 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 20 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection.
- **链接**: [arXiv:2407.08931](https://arxiv.org/abs/2407.08931) · [代码](https://github.com/GradiusTwinbee/GLIS) · 📚 被引 4
- **作者**: Xingyu Peng, Yan Bai, Chen Gao, Lirong Yang, Fei Xia, Beipeng Mu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Detection (OVD) is the task of detecting all interesting objects in a given scene without predefined object classes. Extensive work has been done to deal with the OVD for 2D RGB images, but the exploration of 3D OVD is still limited. Intuitively, lidar point clouds provide 3D information, both object level and scene level, to generate trustful detection results. However, previous lidar-based OVD methods only focus on the usage of object-level features, ignoring the essence of scene-level information. In this paper, we propose a Global-Local Collaborative Scheme (GLIS) for the lidar-based OVD task, which contains a local branch to generate object-level detection result and a global branch to obtain scene-level global feature. With the global-local information, a Large Language Model (LLM) is applied for chain-of-thought inference, and the detection result can be refined accordingly. We further propose Reflected Pseudo Labels Generation (RPLG) to generate high-quality pseudo labels for supervision and Background-Aware Object Localization (BAOL) to select precise object proposals. Extensive experiments on ScanNetV2 and SUN RGB-D demonstrate the superiority of our methods. Code is released at https://github.com/GradiusTwinbee/GLIS.

</details>

### Dual-Level Adaptive Self-labeling for Novel Class Discovery in Point Cloud Segmentation.
- **链接**: [arXiv:2407.12489](https://arxiv.org/abs/2407.12489) · 📚 被引 4
- **作者**: Ruijie Xu, Chuyu Zhang, Hui Ren, Xuming He
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the novel class discovery in point cloud segmentation, which discovers novel classes based on the semantic knowledge of seen classes. Existing work proposes an online point-wise clustering method with a simplified equal class-size constraint on the novel classes to avoid degenerate solutions. However, the inherent imbalanced distribution of novel classes in point clouds typically violates the equal class-size constraint. Moreover, point-wise clustering ignores the rich spatial context information of objects, which results in less expressive representation for semantic segmentation. To address the above challenges, we propose a novel self-labeling strategy that adaptively generates high-quality pseudo-labels for imbalanced classes during model training. In addition, we develop a dual-level representation that incorporates regional consistency into the point-level classifier learning, reducing noise in generated segmentation. Finally, we conduct extensive experiments on two widely used datasets, SemanticKITTI and SemanticPOSS, and the results show our method outperforms the state of the art by a large margin.

</details>

### Zero-Shot Detection of AI-Generated Images.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72649-1_4)
- **作者**: Davide Cozzolino, Giovanni Poggi, Matthias Nießner, Luisa Verdoliva
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Self-cooperation Knowledge Distillation for Novel Class Discovery.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72897-6_26) · 📚 被引 4
- **作者**: Yuzheng Wang, Zhaoyu Chen, Dingkang Yang, Yunquan Sun, Lizhe Qi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Open Vocabulary 3D Scene Understanding via Geometry Guided Self-Distillation.
- **链接**: [arXiv:2407.13362](https://arxiv.org/abs/2407.13362) · 📚 被引 5
- **作者**: Pengfei Wang, Yuxi Wang, Shuai Li, Zhaoxiang Zhang, Zhen Lei, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The scarcity of large-scale 3D-text paired data poses a great challenge on open vocabulary 3D scene understanding, and hence it is popular to leverage internet-scale 2D data and transfer their open vocabulary capabilities to 3D models through knowledge distillation. However, the existing distillation-based 3D scene understanding approaches rely on the representation capacity of 2D models, disregarding the exploration of geometric priors and inherent representational advantages offered by 3D data. In this paper, we propose an effective approach, namely Geometry Guided Self-Distillation (GGSD), to learn superior 3D representations from 2D pre-trained models. Specifically, we first design a geometry guided distillation module to distill knowledge from 2D models, and then leverage the 3D geometric priors to alleviate the inherent noise in 2D models and enhance the representation learning process. Due to the advantages of 3D representation, the performance of the distilled 3D student model can significantly surpass that of the 2D teacher model. This motivates us to further leverage the representation advantages of 3D data through self-distillation. As a result, our proposed GGSD approach outperforms the existing open vocabulary 3D scene understanding methods by a large margin, as demonstrated by our experiments on both indoor and outdoor benchmark datasets.

</details>

### 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation.
- **链接**: [arXiv:2401.02402](https://arxiv.org/abs/2401.02402) · 📚 被引 5
- **作者**: Zihao Xiao, Longlong Jing, Shangxuan Wu, Alex Zihao Zhu, Jingwei Ji, Chiyu Max Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D panoptic segmentation is a challenging perception task, especially in autonomous driving. It aims to predict both semantic and instance annotations for 3D points in a scene. Although prior 3D panoptic segmentation approaches have achieved great performance on closed-set benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem. For unseen object categories, 2D open-vocabulary segmentation has achieved promising results that solely rely on frozen CLIP backbones and ensembling multiple classification outputs. However, we find that simply extending these 2D models to 3D does not guarantee good performance due to poor per-mask classification quality, especially for novel stuff categories. In this paper, we propose the first method to tackle 3D open-vocabulary panoptic segmentation. Our model takes advantage of the fusion between learnable LiDAR features and dense frozen vision CLIP features, using a single classification head to make predictions for both base and novel classes. To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: object-level distillation loss and voxel-level distillation loss. Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.

</details>

## 跨领域论文（完整笔记在其他领域）

- Grounding DINO: Marrying DINO with Grounded Pre-training for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Cross-Domain Few-Shot Object Detection via Enhanced Open-Set Object Detector. → [object-detection](../object-detection/Guideline%202024.md)
- MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments. → [3d-detection](../3d-detection/Guideline%202024.md)
- Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image. → [3d-detection](../3d-detection/Guideline%202024.md)
- Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning. → [object-detection](../object-detection/Guideline%202024.md)
- CLIFF: Continual Latent Diffusion for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation. → [3d-detection](../3d-detection/Guideline%202024.md)
- OpenSight: A Simple Open-Vocabulary Framework for LiDAR-Based Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Towards Multimodal Open-Set Domain Generalization and Adaptation Through Self-supervision. → [multimodal](../multimodal/Guideline%202024.md)
- Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- OpenPSG: Open-Set Panoptic Scene Graph Generation via Large Multimodal Models. → [multimodal](../multimodal/Guideline%202024.md)
- Continual Learning and Unknown Object Discovery in 3D Scenes via Self-distillation. → [continual-learning](../continual-learning/Guideline%202024.md)
- Anytime Continual Learning for Open Vocabulary Classification. → [continual-learning](../continual-learning/Guideline%202024.md)
