# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GD-MAE: Generative Decoder for MAE Pre-Training on LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00907) · 📚 被引 71
- **作者**: Honghui Yang, Tong He, Jiaheng Liu, Hua Chen, Boxi Wu, Binbin Lin et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab
- **会议**: CVPR 2023

### DeepMapping2: Self-Supervised Large-Scale LiDAR Map Optimization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00898) · 📚 被引 13
- **作者**: Chao Chen, Xinhao Liu, Yiming Li, Li Ding, Chen Feng
- **🏷️ 机构**: New York University, University of Rochester
- **会议**: CVPR 2023

### Distilling Self-Supervised Vision Transformers for Weakly-Supervised Few-Shot Classification & Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01880) · 📚 被引 42
- **作者**: Dahyun Kang, Piotr Koniusz, Minsu Cho, Naila Murray
- **🏷️ 机构**: Meta AI, Data61 &#x2665; CSIRO, POSTECH
- **会议**: CVPR 2023

### MixMAE: Mixed and Masked Autoencoder for Efficient Pretraining of Hierarchical Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00605) · 📚 被引 69
- **作者**: Jihao Liu, Xin Huang, Jinliang Zheng, Yu Liu, Hongsheng Li
- **🏷️ 机构**: SenseTime, CUHK
- **会议**: CVPR 2023

### Self-Supervised Image-to-Point Distillation via Semantically Tolerant Contrastive Loss.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00686) · 📚 被引 29
- **作者**: Anas Mahmoud, Jordan S. K. Hu, Tianshu Kuai, Ali Harakeh, Liam Paull, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute, Mila, Universit&#x00E9; de Montr&#x00E9;al
- **会议**: CVPR 2023

### MobileVOS: Real-Time Video Object Segmentation Contrastive Learning meets Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01010) · 📚 被引 36
- **作者**: Roy Miles, Mehmet Kerim Yucel, Bruno Manganelli, Albert Saà-Garriga
- **🏷️ 机构**: Samsung Research,UK
- **会议**: CVPR 2023

### Multi-Mode Online Knowledge Distillation for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2304.06461](https://arxiv.org/abs/2304.06461) · [出版页](https://doi.org/10.1109/CVPR52729.2023.01140) · 📚 被引 38
- **作者**: Kaiyou Song, Jin Xie, Shan Zhang, Zimeng Luo
- **🏷️ 机构**: Megvii Technology
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Self-supervised learning (SSL) has made remarkable progress in visual representation learning. Some studies combine SSL with knowledge distillation (SSL-KD) to boost the representation learning performance of small models. In this study, we propose a Multi-mode Online Knowledge Distillation method (MOKD) to boost self-supervised visual representation learning. Different from existing SSL-KD methods that transfer knowledge from a static pre-trained teacher to a student, in MOKD, two different models learn collaboratively in a self-supervised manner. Specifically, MOKD consists of two distillation modes: self-distillation and cross-distillation modes. Among them, self-distillation performs self-supervised learning for each model independently, while cross-distillation realizes knowledge interaction between different models. In cross-distillation, a cross-attention feature search strategy is proposed to enhance the semantic feature alignment between different models. As a result, the two models can absorb knowledge from each other to boost their representation learning performance. Extensive experimental results on different backbones and datasets demonstrate that two heterogeneous models can benefit from MOKD and outperform their independently trained baseline. In addition, MOKD also outperforms existing SSL-KD methods for both the student and teacher models.

### Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00611)
- **作者**: Rui Wang, Dongdong Chen, Zuxuan Wu, Yinpeng Chen, Xiyang Dai, Mengchen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Complete-to-Partial 4D Distillation for Self-Supervised Point Cloud Sequence Representation Learning.
- **链接**: [arXiv:2212.05330](https://arxiv.org/abs/2212.05330) · [出版页](https://doi.org/10.1109/CVPR52729.2023.01694) · 📚 被引 22
- **作者**: Zhuoyang Zhang, Yuhao Dong, Yunze Liu, Li Yi
- **🏷️ 机构**: IIIS, Tsinghua University
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Recent work on 4D point cloud sequences has attracted a lot of attention. However, obtaining exhaustively labeled 4D datasets is often very expensive and laborious, so it is especially important to investigate how to utilize raw unlabeled data. However, most existing self-supervised point cloud representation learning methods only consider geometry from a static snapshot omitting the fact that sequential observations of dynamic scenes could reveal more comprehensive geometric details. And the video representation learning frameworks mostly model motion as image space flows, let alone being 3D-geometric-aware. To overcome such issues, this paper proposes a new 4D self-supervised pre-training method called Complete-to-Partial 4D Distillation. Our key idea is to formulate 4D self-supervised representation learning as a teacher-student knowledge distillation framework and let the student learn useful 4D representations with the guidance of the teacher. Experiments show that this approach significantly outperforms previous pre-training approaches on a wide range of 4D point cloud sequence understanding tasks including indoor and outdoor scenarios.

## 跨领域论文（完整笔记在其他领域）

- Mask DINO: Towards A Unified Transformer-based Framework for Object Detection and Segmentation. → [object-detection](../object-detection/Guideline%202023.md)
- Object Detection with Self-Supervised Scene Adaptation. → [object-detection](../object-detection/Guideline%202023.md)
- MV-JAR: Masked Voxel Jigsaw and Reconstruction for LiDAR-Based Self-Supervised Pre-Training. → [3d-detection](../3d-detection/Guideline%202023.md)
- Lite-Mono: A Lightweight CNN and Transformer Architecture for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Open Vocabulary Semantic Segmentation with Patch Aligned Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Revisiting Multimodal Representation in Contrastive Learning: From Patch and Token Embeddings to Finite Discrete Tokens. → [multimodal](../multimodal/Guideline%202023.md)
- Self-Supervised Learning for Multimodal Non-Rigid 3D Shape Matching. → [multimodal](../multimodal/Guideline%202023.md)
- Best of Both Worlds: Multimodal Contrastive Learning with Tabular and Imaging Data. → [multimodal](../multimodal/Guideline%202023.md)
- Hunting Sparsity: Density-Guided Contrastive Learning for Semi-Supervised Semantic Segmentation. → [network-pruning](../network-pruning/Guideline%202023.md)
