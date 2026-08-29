# Multi-camera Perception — 2025 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Trusted Multi-View Classification via Evolutionary Multi-View Fusion.
- **链接**: [出版页](https://openreview.net/forum?id=M3kBtqpys5)
- **作者**: Xinyan Liang, Pinhan Fu, Yuhua Qian, Qian Guo, Guoqing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Enhance Multi-View Classification Through Multi-Scale Alignment and Expanded Boundary.
- **链接**: [出版页](https://openreview.net/forum?id=t1J2CnDFwj)
- **作者**: Yuena Lin, Yiyuan Wang, Gengyu Lyu, Yongjian Deng, Haichun Cai, Huibin Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency.
- **链接**: [arXiv:2407.17470](https://arxiv.org/abs/2407.17470)
- **作者**: Yiming Xie, Chun-Han Yao, Vikram Voleti, Huaizu Jiang, Varun Jampani
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Stable Video 4D (SV4D), a latent video diffusion model for multi-frame and multi-view consistent dynamic 3D content generation. Unlike previous methods that rely on separately trained generative models for video generation and novel view synthesis, we design a unified diffusion model to generate novel view videos of dynamic 3D objects. Specifically, given a monocular reference video, SV4D generates novel views for each video frame that are temporally consistent. We then use the generated novel view videos to optimize an implicit 4D representation (dynamic NeRF) efficiently, without the need for cumbersome SDS-based optimization used in most prior works. To train our unified novel view video generation model, we curate a dynamic 3D object dataset from the existing Objaverse dataset. Extensive experimental results on multiple datasets and user studies demonstrate SV4D's state-of-the-art performance on novel-view video synthesis as well as 4D generation compared to prior works.

</details>

### Simple yet Effective Incomplete Multi-view Clustering: Similarity-level Imputation and Intra-view Hybrid-group Prototype Construction.
- **链接**: [出版页](https://openreview.net/forum?id=KijslFbfOL)
- **作者**: Shengju Yu, Zhibin Dong, Siwei Wang, Pei Zhang, Yi Zhang, Xinwang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians.
- **链接**: [arXiv:2504.06003](https://arxiv.org/abs/2504.06003)
- **作者**: Can Zhang, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The primary focus of most recent works on open-vocabulary neural fields is extracting precise semantic features from the VLMs and then consolidating them efficiently into a multi-view consistent 3D neural fields representation. However, most existing works over-trusted SAM to regularize image-level CLIP without any further refinement. Moreover, several existing works improved efficiency by dimensionality reduction of semantic features from 2D VLMs before fusing with 3DGS semantic fields, which inevitably leads to multi-view inconsistency. In this work, we propose econSG for open-vocabulary semantic segmentation with 3DGS. Our econSG consists of: 1) A Confidence-region Guided Regularization (CRR) that mutually refines SAM and CLIP to get the best of both worlds for precise semantic features with complete and precise boundaries. 2) A low dimensional contextual space to enforce 3D multi-view consistency while improving computational efficiency by fusing backprojected multi-view 2D features and follow by dimensional reduction directly on the fused 3D features instead of operating on each 2D view separately. Our econSG shows state-of-the-art performance on four benchmark datasets compared to the existing methods. Furthermore, we are also the most efficient training among all the methods.

</details>

### SynCamMaster: Synchronizing Multi-Camera Video Generation from Diverse Viewpoints.
- **链接**: [arXiv:2412.07760](https://arxiv.org/abs/2412.07760)
- **作者**: Jianhong Bai, Menghan Xia, Xintao Wang, Ziyang Yuan, Zuozhu Liu, Haoji Hu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in video diffusion models have shown exceptional abilities in simulating real-world dynamics and maintaining 3D consistency. This progress inspires us to investigate the potential of these models to ensure dynamic consistency across various viewpoints, a highly desirable feature for applications such as virtual filming. Unlike existing methods focused on multi-view generation of single objects for 4D reconstruction, our interest lies in generating open-world videos from arbitrary viewpoints, incorporating 6 DoF camera poses. To achieve this, we propose a plug-and-play module that enhances a pre-trained text-to-video model for multi-camera video generation, ensuring consistent content across different viewpoints. Specifically, we introduce a multi-view synchronization module to maintain appearance and geometry consistency across these viewpoints. Given the scarcity of high-quality training data, we design a hybrid training scheme that leverages multi-camera images and monocular videos to supplement Unreal Engine-rendered multi-camera videos. Furthermore, our method enables intriguing extensions, such as re-rendering a video from novel viewpoints. We also release a multi-view synchronized video dataset, named SynCamVideo-Dataset. Project page: https://jianhongbai.github.io/SynCamMaster/.

</details>

### COPER: Correlation-based Permutations for Multi-View Clustering.
- **链接**: [出版页](https://openreview.net/forum?id=5ZEbpBYGwH)
- **作者**: Ran Eisenberg, Jonathan Svirsky, Ofir Lindenbaum
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Deep Incomplete Multi-view Learning via Cyclic Permutation of VAEs.
- **链接**: [arXiv:2502.11037](https://arxiv.org/abs/2502.11037)
- **作者**: Xin Gao, Jian Pu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-View Representation Learning (MVRL) aims to derive a unified representation from multi-view data by leveraging shared and complementary information across views. However, when views are irregularly missing, the incomplete data can lead to representations that lack sufficiency and consistency. To address this, we propose Multi-View Permutation of Variational Auto-Encoders (MVP), which excavates invariant relationships between views in incomplete data. MVP establishes inter-view correspondences in the latent space of Variational Auto-Encoders, enabling the inference of missing views and the aggregation of more sufficient information. To derive a valid Evidence Lower Bound (ELBO) for learning, we apply permutations to randomly reorder variables for cross-view generation and then partition them by views to maintain invariant meanings under permutations. Additionally, we enhance consistency by introducing an informational prior with cyclic permutations of posteriors, which turns the regularization term into a similarity measure across distributions. We demonstrate the effectiveness of our approach on seven diverse datasets with varying missing ratios, achieving superior performance in multi-view clustering and generation tasks.

</details>

### Duoduo CLIP: Efficient 3D Understanding with Multi-View Images.
- **链接**: [出版页](https://openreview.net/forum?id=iGbuc9ekKK)
- **作者**: Han-Hung Lee, Yiming Zhang, Angel X. Chang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### CREIMBO: Cross-Regional Ensemble Interactions in Multi-view Brain Observations.
- **链接**: [出版页](https://openreview.net/forum?id=28abpUEICJ)
- **作者**: Noga Mudrik, Ryan Ly, Oliver Rübel, Adam Shabti Charles
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Diffusion2: Dynamic 3D Content Generation via Score Composition of Video and Multi-view Diffusion Models.
- **链接**: [出版页](https://openreview.net/forum?id=fectsEG2GU)
- **作者**: Zeyu Yang, Zijie Pan, Chun Gu, Li Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Self-supervised Monocular Depth Estimation Robust to Reflective Surface Leveraged by Triplet Mining.
- **链接**: [出版页](https://openreview.net/forum?id=XdRIno98gG)
- **作者**: Wonhyeok Choi, Kyumin Hwang, Wei Peng, Minwoo Choi, Sunghoon Im
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### MRAG-Bench: Vision-Centric Evaluation for Retrieval-Augmented Multimodal Models.
- **链接**: [出版页](https://openreview.net/forum?id=Usklli4gMc)
- **作者**: Wenbo Hu, Jia-Chen Gu, Zi-Yi Dou, Mohsen Fayyaz, Pan Lu, Kai-Wei Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

## 跨领域论文（完整笔记在其他领域）

- Semi-Supervised Vision-Centric 3D Occupancy World Model for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
