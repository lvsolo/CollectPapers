# Multimodal — 2022 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multimodal Object Detection via Probabilistic Ensembling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_9) · 📚 被引 201
- **作者**: Yi-Ting Chen, Jinghao Shi, Zelin Ye, Christoph Mertz, Deva Ramanan, Shu Kong
- **🏷️ 机构**: CMU
- **会议**: ECCV 2022

### Multimodal Transformer for Automatic 3D Annotation and Object Detection.
- **链接**: [arXiv:2207.09805](https://arxiv.org/abs/2207.09805) · [代码](https://github.com/Cliu2/MTrans)
- **作者**: Chang Liu, Xiaoyan Qian, Binxiao Huang, Xiaojuan Qi, Edmund Y. Lam, Siew-Chong Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Despite a growing number of datasets being collected for training 3D object detection models, significant human effort is still required to annotate 3D boxes on LiDAR scans. To automate the annotation and facilitate the production of various customized datasets, we propose an end-to-end multimodal transformer (MTrans) autolabeler, which leverages both LiDAR scans and images to generate precise 3D box annotations from weak 2D bounding boxes. To alleviate the pervasive sparsity problem that hinders existing autolabelers, MTrans densifies the sparse point clouds by generating new 3D points based on 2D image information. With a multi-task design, MTrans segments the foreground/background, densifies LiDAR point clouds, and regresses 3D boxes simultaneously. Experimental results verify the effectiveness of the MTrans for improving the quality of the generated labels. By enriching the sparse point clouds, our method achieves 4.48\% and 4.03\% better 3D AP on KITTI moderate and hard samples, respectively, versus the state-of-the-art autolabeler. MTrans can also be extended to improve the accuracy for 3D object detection, resulting in a remarkable 89.45\% AP on KITTI hard samples. Codes are at \url{https://github.com/Cliu2/MTrans}.

### Class-Agnostic Object Detection with Multi-modal Transformer.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_30)
- **作者**: Muhammad Maaz, Hanoona Abdul Rasheed, Salman Khan, Fahad Shahbaz Khan, Rao Muhammad Anwer, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2022

### Multi-modal Masked Pre-training for Monocular Panoramic Depth Completion.
- **链接**: [arXiv:2203.09855](https://arxiv.org/abs/2203.09855) · 📚 被引 28
- **作者**: Zhiqiang Yan, Xiang Li, Kun Wang, Zhenyu Zhang, Jun Li, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > In this paper, we formulate a potentially valuable panoramic depth completion (PDC) task as panoramic 3D cameras often produce 360° depth with missing data in complex scenes. Its goal is to recover dense panoramic depths from raw sparse ones and panoramic RGB images. To deal with the PDC task, we train a deep network that takes both depth and image as inputs for the dense panoramic depth recovery. However, it needs to face a challenging optimization problem of the network parameters due to its non-convex objective function. To address this problem, we propose a simple yet effective approach termed M{^3}PT: multi-modal masked pre-training. Specifically, during pre-training, we simultaneously cover up patches of the panoramic RGB image and sparse depth by shared random mask, then reconstruct the sparse depth in the masked regions. To our best knowledge, it is the first time that we show the effectiveness of masked pre-training in a multi-modal vision task, instead of the single-modal task resolved by masked autoencoders (MAE). Different from MAE where fine-tuning completely discards the decoder part of pre-training, there is no architectural difference between the pre-training and fine-tuning stages in our M$^{3}$PT as they only differ in the prediction density, which potentially makes the transfer learning more convenient and effective. Extensive experiments verify the effectiveness of M{^3}PT on three panoramic datasets. Notably, we improve the state-of-the-art baselines by averagely 26.2% in RMSE, 51.7% in MRE, 49.7% in MAE, and 37.5% in RMSElog on three benchmark datasets.

### Multimodal Transformer with Variable-Length Memory for Vision-and-Language Navigation.
- **链接**: [arXiv:2111.05759](https://arxiv.org/abs/2111.05759) · 📚 被引 29
- **作者**: Chuang Lin, Yi Jiang, Jianfei Cai, Lizhen Qu, Gholamreza Haffari, Zehuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Vision-and-Language Navigation (VLN) is a task that an agent is required to follow a language instruction to navigate to the goal position, which relies on the ongoing interactions with the environment during moving. Recent Transformer-based VLN methods have made great progress benefiting from the direct connections between visual observations and the language instruction via the multimodal cross-attention mechanism. However, these methods usually represent temporal context as a fixed-length vector by using an LSTM decoder or using manually designed hidden states to build a recurrent Transformer. Considering a single fixed-length vector is often insufficient to capture long-term temporal context, in this paper, we introduce Multimodal Transformer with Variable-length Memory (MTVM) for visually-grounded natural language navigation by modelling the temporal context explicitly. Specifically, MTVM enables the agent to keep track of the navigation trajectory by directly storing previous activations in a memory bank. To further boost the performance, we propose a memory-aware consistency loss to help learn a better joint representation of temporal context with random masked instructions. We evaluate MTVM on popular R2R and CVDN datasets, and our model improves Success Rate on R2R unseen validation and test set by 2% each, and reduce Goal Process by 1.6m on CVDN test set.

### Learning Mutual Modulation for Self-supervised Cross-Modal Super-Resolution.
- **链接**: [arXiv:2207.09156](https://arxiv.org/abs/2207.09156) · 📚 被引 15
- **作者**: Xiaoyu Dong, Naoto Yokoya, Longguang Wang, Tatsumi Uezato
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Self-supervised cross-modal super-resolution (SR) can overcome the difficulty of acquiring paired training data, but is challenging because only low-resolution (LR) source and high-resolution (HR) guide images from different modalities are available. Existing methods utilize pseudo or weak supervision in LR space and thus deliver results that are blurry or not faithful to the source modality. To address this issue, we present a mutual modulation SR (MMSR) model, which tackles the task by a mutual modulation strategy, including a source-to-guide modulation and a guide-to-source modulation. In these modulations, we develop cross-domain adaptive filters to fully exploit cross-modal spatial dependency and help induce the source to emulate the resolution of the guide and induce the guide to mimic the modality characteristics of the source. Moreover, we adopt a cycle consistency constraint to train MMSR in a fully self-supervised manner. Experiments on various tasks demonstrate the state-of-the-art performance of our MMSR.

### CMD: Self-supervised 3D Action Representation Learning with Cross-Modal Mutual Distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20062-5_42) · 📚 被引 62
- **作者**: Yunyao Mao, Wengang Zhou, Zhenbo Lu, Jiajun Deng, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Drive&Segment: Unsupervised Semantic Segmentation of Urban Scenes via Cross-Modal Distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_28)
- **作者**: Antonín Vobecký, David Hurych, Oriane Siméoni, Spyros Gidaris, Andrei Bursuc, Patrick Pérez et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

## 跨领域论文（完整笔记在其他领域）

- Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
