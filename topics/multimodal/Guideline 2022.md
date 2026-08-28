# Multimodal — 2022 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite a growing number of datasets being collected for training 3D object detection models, significant human effort is still required to annotate 3D boxes on LiDAR scans. To automate the annotation and facilitate the production of various customized datasets, we propose an end-to-end multimodal transformer (MTrans) autolabeler, which leverages both LiDAR scans and images to generate precise 3D box annotations from weak 2D bounding boxes. To alleviate the pervasive sparsity problem that hinders existing autolabelers, MTrans densifies the sparse point clouds by generating new 3D points based on 2D image information. With a multi-task design, MTrans segments the foreground/background, densifies LiDAR point clouds, and regresses 3D boxes simultaneously. Experimental results verify the effectiveness of the MTrans for improving the quality of the generated labels. By enriching the sparse point clouds, our method achieves 4.48\% and 4.03\% better 3D AP on KITTI moderate and hard samples, respectively, versus the state-of-the-art autolabeler. MTrans can also be extended to improve the accuracy for 3D object detection, resulting in a remarkable 89.45\% AP on KITTI hard samples. Codes are at \url{https://github.com/Cliu2/MTrans}.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we formulate a potentially valuable panoramic depth completion (PDC) task as panoramic 3D cameras often produce 360° depth with missing data in complex scenes. Its goal is to recover dense panoramic depths from raw sparse ones and panoramic RGB images. To deal with the PDC task, we train a deep network that takes both depth and image as inputs for the dense panoramic depth recovery. However, it needs to face a challenging optimization problem of the network parameters due to its non-convex objective function. To address this problem, we propose a simple yet effective approach termed M{^3}PT: multi-modal masked pre-training. Specifically, during pre-training, we simultaneously cover up patches of the panoramic RGB image and sparse depth by shared random mask, then reconstruct the sparse depth in the masked regions. To our best knowledge, it is the first time that we show the effectiveness of masked pre-training in a multi-modal vision task, instead of the single-modal task resolved by masked autoencoders (MAE). Different from MAE where fine-tuning completely discards the decoder part of pre-training, there is no architectural difference between the pre-training and fine-tuning stages in our M$^{3}$PT as they only differ in the prediction density, which potentially makes the transfer learning more convenient and effective. Extensive experiments verify the effectiveness of M{^3}PT on three panoramic datasets. Notably, we improve the state-of-the-art baselines by averagely 26.2% in RMSE, 51.7% in MRE, 49.7% in MAE, and 37.5% in RMSElog on three benchmark datasets.

</details>

### Multimodal Transformer with Variable-Length Memory for Vision-and-Language Navigation.
- **链接**: [arXiv:2111.05759](https://arxiv.org/abs/2111.05759) · 📚 被引 29
- **作者**: Chuang Lin, Yi Jiang, Jianfei Cai, Lizhen Qu, Gholamreza Haffari, Zehuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-Language Navigation (VLN) is a task that an agent is required to follow a language instruction to navigate to the goal position, which relies on the ongoing interactions with the environment during moving. Recent Transformer-based VLN methods have made great progress benefiting from the direct connections between visual observations and the language instruction via the multimodal cross-attention mechanism. However, these methods usually represent temporal context as a fixed-length vector by using an LSTM decoder or using manually designed hidden states to build a recurrent Transformer. Considering a single fixed-length vector is often insufficient to capture long-term temporal context, in this paper, we introduce Multimodal Transformer with Variable-length Memory (MTVM) for visually-grounded natural language navigation by modelling the temporal context explicitly. Specifically, MTVM enables the agent to keep track of the navigation trajectory by directly storing previous activations in a memory bank. To further boost the performance, we propose a memory-aware consistency loss to help learn a better joint representation of temporal context with random masked instructions. We evaluate MTVM on popular R2R and CVDN datasets, and our model improves Success Rate on R2R unseen validation and test set by 2% each, and reduce Goal Process by 1.6m on CVDN test set.

</details>

### Switch-BERT: Learning to Model Multimodal Interactions by Switching Attention and Input.
- **链接**: [arXiv:2306.14182](https://arxiv.org/abs/2306.14182) · 📚 被引 6
- **作者**: Qingpei Guo, Kaisheng Yao, Wei Chu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to model intra-modal and inter-modal interactions is fundamental in multimodal machine learning. The current state-of-the-art models usually adopt deep learning models with fixed structures. They can achieve exceptional performances on specific tasks, but face a particularly challenging problem of modality mismatch because of diversity of input modalities and their fixed structures. In this paper, we present \textbf{Switch-BERT} for joint vision and language representation learning to address this problem. Switch-BERT extends BERT architecture by introducing learnable layer-wise and cross-layer interactions. It learns to optimize attention from a set of attention modes representing these interactions. One specific property of the model is that it learns to attend outputs from various depths, therefore mitigates the modality mismatch problem. We present extensive experiments on visual question answering, image-text retrieval and referring expression comprehension experiments. Results confirm that, whereas alternative architectures including ViLBERT and UNITER may excel in particular tasks, Switch-BERT can consistently achieve better or comparable performances than the current state-of-the-art models in these tasks. Ablation studies indicate that the proposed model achieves superior performances due to its ability in learning task-specific multimodal interactions.

</details>

### MUGEN: A Playground for Video-Audio-Text Multimodal Understanding and GENeration.
- **链接**: [arXiv:2204.08058](https://arxiv.org/abs/2204.08058) · 📚 被引 19
- **作者**: Thomas Hayes, Songyang Zhang, Xi Yin, Guan Pang, Sasha Sheng, Harry Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal video-audio-text understanding and generation can benefit from datasets that are narrow but rich. The narrowness allows bite-sized challenges that the research community can make progress on. The richness ensures we are making progress along the core challenges. To this end, we present a large-scale video-audio-text dataset MUGEN, collected using the open-sourced platform game CoinRun [11]. We made substantial modifications to make the game richer by introducing audio and enabling new interactions. We trained RL agents with different objectives to navigate the game and interact with 13 objects and characters. This allows us to automatically extract a large collection of diverse videos and associated audio. We sample 375K video clips (3.2s each) and collect text descriptions from human annotators. Each video has additional annotations that are extracted automatically from the game engine, such as accurate semantic maps for each frame and templated textual descriptions. Altogether, MUGEN can help progress research in many tasks in multimodal understanding and generation. We benchmark representative approaches on tasks involving video-audio-text retrieval and generation. Our dataset and code are released at: https://mugen-org.github.io/.

</details>

### Multimodal Conditional Image Synthesis with Product-of-Experts GANs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19787-1_6) · 📚 被引 54
- **作者**: Xun Huang, Arun Mallya, Ting-Chun Wang, Ming-Yu Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Learning Mutual Modulation for Self-supervised Cross-Modal Super-Resolution.
- **链接**: [arXiv:2207.09156](https://arxiv.org/abs/2207.09156) · 📚 被引 15
- **作者**: Xiaoyu Dong, Naoto Yokoya, Longguang Wang, Tatsumi Uezato
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised cross-modal super-resolution (SR) can overcome the difficulty of acquiring paired training data, but is challenging because only low-resolution (LR) source and high-resolution (HR) guide images from different modalities are available. Existing methods utilize pseudo or weak supervision in LR space and thus deliver results that are blurry or not faithful to the source modality. To address this issue, we present a mutual modulation SR (MMSR) model, which tackles the task by a mutual modulation strategy, including a source-to-guide modulation and a guide-to-source modulation. In these modulations, we develop cross-domain adaptive filters to fully exploit cross-modal spatial dependency and help induce the source to emulate the resolution of the guide and induce the guide to mimic the modality characteristics of the source. Moreover, we adopt a cycle consistency constraint to train MMSR in a fully self-supervised manner. Experiments on various tasks demonstrate the state-of-the-art performance of our MMSR.

</details>

### CMD: Self-supervised 3D Action Representation Learning with Cross-Modal Mutual Distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20062-5_42) · 📚 被引 62
- **作者**: Yunyao Mao, Wengang Zhou, Zhenbo Lu, Jiajun Deng, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Drive&Segment: Unsupervised Semantic Segmentation of Urban Scenes via Cross-Modal Distillation.
- **链接**: [arXiv:2203.11160](https://arxiv.org/abs/2203.11160)
- **作者**: Antonín Vobecký, David Hurych, Oriane Siméoni, Spyros Gidaris, Andrei Bursuc, Patrick Pérez et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work investigates learning pixel-wise semantic image segmentation in urban scenes without any manual annotation, just from the raw non-curated data collected by cars which, equipped with cameras and LiDAR sensors, drive around a city. Our contributions are threefold. First, we propose a novel method for cross-modal unsupervised learning of semantic image segmentation by leveraging synchronized LiDAR and image data. The key ingredient of our method is the use of an object proposal module that analyzes the LiDAR point cloud to obtain proposals for spatially consistent objects. Second, we show that these 3D object proposals can be aligned with the input images and reliably clustered into semantically meaningful pseudo-classes. Finally, we develop a cross-modal distillation approach that leverages image data partially annotated with the resulting pseudo-classes to train a transformer-based model for image semantic segmentation. We show the generalization capabilities of our method by testing on four different testing datasets (Cityscapes, Dark Zurich, Nighttime Driving and ACDC) without any finetuning, and demonstrate significant improvements compared to the current state of the art on this problem. See project webpage https://vobecant.github.io/DriveAndSegment/ for the code and more.

</details>

## 跨领域论文（完整笔记在其他领域）

- Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
