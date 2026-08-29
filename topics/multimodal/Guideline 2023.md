# Multimodal — 2023 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A Large-Scale Outdoor Multi-modal Dataset and Benchmark for Novel View Synthesis and Implicit Scene Reconstruction.
- **链接**: [arXiv:2301.06782](https://arxiv.org/abs/2301.06782) · 📚 被引 33
- **作者**: Chongshan Lu, Fukun Yin, Xin Chen, Wen Liu, Tao Chen, Gang Yu et al.
- **🏷️ 机构**: Fudan University,School of Information Science and Technology,China, Tencent PCG,China, Fudan University,Academy for Engineering and Technology,China
- **会议**: ICCV 2023

### MMST-ViT: Climate Change-aware Crop Yield Prediction via Multi-Modal Spatial-Temporal Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00531)
- **作者**: Fudong Lin, Summer Crawford, Kaleb Guillot, Yihe Zhang, Yan Chen, Xu Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Multimodality Helps Unimodality: Cross-Modal Few-Shot Learning with Multimodal Models.
- **链接**: [arXiv:2301.06267](https://arxiv.org/abs/2301.06267) · 📚 被引 118
- **作者**: Zhiqiu Lin, Samuel Yu, Zhiyi Kuang, Deepak Pathak, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of multimodal summarization is to extract the most important information from different modalities to form output summaries. Unlike the unimodal summarization, the multimodal summarization task explicitly leverages cross-modal information to help generate more reliable and high-quality summaries. However, existing methods fail to leverage the temporal correspondence between different modalities and ignore the intrinsic correlation between different samples. To address this issue, we introduce Align and Attend Multimodal Summarization (A2Summ), a unified multimodal transformer-based model which can effectively align and attend the multimodal input. In addition, we propose two novel contrastive losses to model both inter-sample and intra-sample correlations. Extensive experiments on two standard video summarization datasets (TVSum and SumMe) and two multimodal summarization datasets (Daily Mail and CNN) demonstrate the superiority of A2Summ, achieving state-of-the-art performances on all datasets. Moreover, we collected a large-scale multimodal summarization dataset BLiSS, which contains livestream videos and transcribed texts with annotated summaries. Our code and dataset are publicly available at ~\url{https://boheumd.github.io/A2Summ/}.

</details>

### Multimodal Industrial Anomaly Detection via Hybrid Fusion.
- **链接**: [arXiv:2303.00601](https://arxiv.org/abs/2303.00601) · [代码](https://github.com/nomewang/M3DM) · 📚 被引 200
- **作者**: Yue Wang, Jinlong Peng, Jiangning Zhang, Ran Yi, Yabiao Wang, Chengjie Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Shanghai,China, Tencent,Youtu Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 2D-based Industrial Anomaly Detection has been widely discussed, however, multimodal industrial anomaly detection based on 3D point clouds and RGB images still has many untouched fields. Existing multimodal industrial anomaly detection methods directly concatenate the multimodal features, which leads to a strong disturbance between features and harms the detection performance. In this paper, we propose Multi-3D-Memory (M3DM), a novel multimodal anomaly detection method with hybrid fusion scheme: firstly, we design an unsupervised feature fusion with patch-wise contrastive learning to encourage the interaction of different modal features; secondly, we use a decision layer fusion with multiple memory banks to avoid loss of information and additional novelty classifiers to make the final decision. We further propose a point feature alignment operation to better align the point cloud and RGB features. Extensive experiments show that our multimodal industrial anomaly detection model outperforms the state-of-the-art (SOTA) methods on both detection and segmentation precision on MVTec-3D AD dataset. Code is available at https://github.com/nomewang/M3DM.

</details>

### Self-Supervised Learning for Multimodal Non-Rigid 3D Shape Matching.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01701) · 📚 被引 29
- **作者**: Dongliang Cao, Florian Bernard
- **🏷️ 机构**: University of Bonn
- **会议**: CVPR 2023

### Seeing With Sound: Long-Range Acoustic Beamforming for Multimodal Scene Understanding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00101) · 📚 被引 4
- **作者**: Praneeth Chakravarthula, Jim Aldon D'Souza, Ethan Tseng, Joe Bartusek, Felix Heide
- **🏷️ 机构**: Princeton University, Algolux
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Enhanced Multimodal Representation Learning with Cross-modal KD.
- **链接**: [arXiv:2306.07646](https://arxiv.org/abs/2306.07646) · 📚 被引 13
- **作者**: Mengxi Chen, Linyu Xing, Yu Wang, Ya Zhang
- **🏷️ 机构**: Shanghai Jiao Tong University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the tasks of leveraging auxiliary modalities which are only available at training to enhance multimodal representation learning through cross-modal Knowledge Distillation (KD). The widely adopted mutual information maximization-based objective leads to a short-cut solution of the weak teacher, i.e., achieving the maximum mutual information by simply making the teacher model as weak as the student model. To prevent such a weak solution, we introduce an additional objective term, i.e., the mutual information between the teacher and the auxiliary modality model. Besides, to narrow down the information gap between the student and teacher, we further propose to minimize the conditional entropy of the teacher given the student. Novel training schemes based on contrastive learning and adversarial learning are designed to optimize the mutual information and the conditional entropy, respectively. Experimental results on three popular multimodal benchmark datasets have shown that the proposed method outperforms a range of state-of-the-art approaches for video recognition, video retrieval and emotion classification.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the tasks of leveraging auxiliary modalities which are only available at training to enhance multimodal representation learning through cross-modal Knowledge Distillation (KD). The widely adopted mutual information maximization-based objective leads to a short-cut solution of the weak teacher, i.e., achieving the maximum mutual information by simply making the teacher model as weak as the student model. To prevent such a weak solution, we introduce an additional objective term, i.e., the mutual information between the teacher and the auxiliary modality model. Besides, to narrow down the information gap between the student and teacher, we further propose to minimize the conditional entropy of the teacher given the student. Novel training schemes based on contrastive learning and adversarial learning are designed to optimize the mutual information and the conditional entropy, respectively. Experimental results on three popular multimodal benchmark datasets have shown that the proposed method outperforms a range of state-of-the-art approaches for video recognition, video retrieval and emotion classification.

</details>

</details>

### ProtoTransfer: Cross-Modal Prototype Transfer for Point Cloud Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00309) · 📚 被引 15
- **作者**: Pin Tang, Hai-Ming Xu, Chao Ma
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, AI Institute, University of Adelaide,Australian Institute for Machine Learning
- **会议**: ICCV 2023

### Tell Me What Happened: Unifying Text-guided Video Completion via Multimodal Masked Video Generation.
- **链接**: [arXiv:2211.12824](https://arxiv.org/abs/2211.12824) · 📚 被引 18
- **作者**: Tsu-Jui Fu, Licheng Yu, Ning Zhang, Cheng-Yang Fu, Jong-Chyi Su, William Yang Wang et al.
- **🏷️ 机构**: UC Santa Barbara, Meta, NEC Laboratories America
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point-, voxel-, and range-views are three representative forms of point clouds. All of them have accurate 3D measurements but lack color and texture information. RGB images are a natural complement to these point cloud views and fully utilizing the comprehensive information of them benefits more robust perceptions. In this paper, we present a unified multi-modal LiDAR segmentation network, termed UniSeg, which leverages the information of RGB images and three views of the point cloud, and accomplishes semantic segmentation and panoptic segmentation simultaneously. Specifically, we first design the Learnable cross-Modal Association (LMA) module to automatically fuse voxel-view and range-view features with image features, which fully utilize the rich semantic information of images and are robust to calibration errors. Then, the enhanced voxel-view and range-view features are transformed to the point space,where three views of point cloud features are further fused adaptively by the Learnable cross-View Association module (LVA). Notably, UniSeg achieves promising results in three public benchmarks, i.e., SemanticKITTI, nuScenes, and Waymo Open Dataset (WOD); it ranks 1st on two challenges of two benchmarks, including the LiDAR semantic segmentation challenge of nuScenes and panoptic segmentation challenges of SemanticKITTI. Besides, we construct the OpenPCSeg codebase, which is the largest and most comprehensive outdoor LiDAR segmentation codebase. It contains most of the popular outdoor LiDAR segmentation algorithms and provides reproducible implementations. The OpenPCSeg codebase will be made publicly available at https://github.com/PJLab-ADG/PCSeg.

</details>

### See More and Know More: Zero-shot Point Cloud Segmentation via Multi-modal Visual Data.
- **链接**: [arXiv:2307.10782](https://arxiv.org/abs/2307.10782) · 📚 被引 27
- **作者**: Yuhang Lu, Qi Jiang, Runnan Chen, Yuenan Hou, Xinge Zhu, Yuexin Ma
- **🏷️ 机构**: ShanghaiTech University, The University of Hong Kong, Shanghai AI Laboratory
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot point cloud segmentation aims to make deep models capable of recognizing novel objects in point cloud that are unseen in the training phase. Recent trends favor the pipeline which transfers knowledge from seen classes with labels to unseen classes without labels. They typically align visual features with semantic features obtained from word embedding by the supervision of seen classes' annotations. However, point cloud contains limited information to fully match with semantic features. In fact, the rich appearance information of images is a natural complement to the textureless point cloud, which is not well explored in previous literature. Motivated by this, we propose a novel multi-modal zero-shot learning method to better utilize the complementary information of point clouds and images for more accurate visual-semantic alignment. Extensive experiments are performed in two popular benchmarks, i.e., SemanticKITTI and nuScenes, and our method outperforms current SOTA methods with 52% and 49% improvement on average for unseen class mIoU, respectively.

</details>

### ProtoTransfer: Cross-Modal Prototype Transfer for Point Cloud Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00309) · 📚 被引 15
- **作者**: Pin Tang, Hai-Ming Xu, Chao Ma
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, AI Institute, University of Adelaide,Australian Institute for Machine Learning
- **会议**: ICCV 2023

### UniTR: A Unified and Efficient Multi-Modal Transformer for Bird's-Eye-View Representation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00625) · 📚 被引 95
- **作者**: Haiyang Wang, Hao Tang, Shaoshuai Shi, Aoxue Li, Zhenguo Li, Bernt Schiele et al.
- **🏷️ 机构**: Peking University, Max Planck Institute for Informatics, Huawei,China
- **会议**: ICCV 2023

### MixReorg: Cross-Modal Mixed Patch Reorganization is a Good Mask Learner for Open-World Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00116) · 📚 被引 16
- **作者**: Kaixin Cai, Pengzhen Ren, Yi Zhu, Hang Xu, Jianzhuang Liu, Changlin Li et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, Huawei Noah&#x2019;s Ark Lab, University of Technology Sydney
- **会议**: ICCV 2023

### CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00017)
- **作者**: Hritik Bansal, Fan Yin, Nishad Singhi, Aditya Grover, Yu Yang, Kai-Wei Chang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Vision Transformers are Parameter-Efficient Audio-Visual Learners.
- **链接**: [arXiv:2212.07983](https://arxiv.org/abs/2212.07983) · 📚 被引 90
- **作者**: Yan-Bo Lin, Yi-Lin Sung, Jie Lei, Mohit Bansal, Gedas Bertasius
- **🏷️ 机构**: UNC Chapel Hill,Department of Computer Science
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The focal point of egocentric video understanding is modelling hand-object interactions. Standard models, e.g. CNNs or Vision Transformers, which receive RGB frames as input perform well. However, their performance improves further by employing additional input modalities that provide complementary cues, such as object detections, optical flow, audio, etc. The added complexity of the modality-specific modules, on the other hand, makes these models impractical for deployment. The goal of this work is to retain the performance of such a multimodal approach, while using only the RGB frames as input at inference time. We demonstrate that for egocentric action recognition on the Epic-Kitchens and the Something-Something datasets, students which are taught by multimodal teachers tend to be more accurate and better calibrated than architecturally equivalent models trained on ground truth labels in a unimodal or multimodal fashion. We further adopt a principled multimodal knowledge distillation framework, allowing us to deal with issues which occur when applying multimodal knowledge distillation in a naive manner. Lastly, we demonstrate the achieved reduction in computational complexity, and show that our approach maintains higher performance with the reduction of the number of input views. We release our code at https://github.com/gorjanradevski/multimodal-distillation.

</details>

### Self-Supervised Video Forensics by Audio-Visual Anomaly Detection.
- **链接**: [arXiv:2301.01767](https://arxiv.org/abs/2301.01767) · 📚 被引 92
- **作者**: Chao Feng, Ziyang Chen, Andrew Owens
- **🏷️ 机构**: University of Michigan
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sound can convey significant information for spatial reasoning in our daily lives. To endow deep networks with such ability, we address the challenge of dense indoor prediction with sound in both 2D and 3D via cross-modal knowledge distillation. In this work, we propose a Spatial Alignment via Matching (SAM) distillation framework that elicits local correspondence between the two modalities in vision-to-audio knowledge transfer. SAM integrates audio features with visually coherent learnable spatial embeddings to resolve inconsistencies in multiple layers of a student model. Our approach does not rely on a specific input representation, allowing for flexibility in the input shapes or dimensions without performance degradation. With a newly curated benchmark named Dense Auditory Prediction of Surroundings (DAPS), we are the first to tackle dense indoor prediction of omnidirectional surroundings in both 2D and 3D with audio observations. Specifically, for audio-based depth estimation, semantic segmentation, and challenging 3D scene reconstruction, the proposed distillation framework consistently achieves state-of-the-art performance across various metrics and backbone architectures.

</details>

### Decomposed Cross-Modal Distillation for RGB-based Temporal Action Detection.
- **链接**: [arXiv:2303.17285](https://arxiv.org/abs/2303.17285) · 📚 被引 21
- **作者**: Pilhyeon Lee, Taeoh Kim, Minho Shim, Dongyoon Wee, Hyeran Byun
- **🏷️ 机构**: Yonsei University, Naver Cloud, AI Tech.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Temporal action detection aims to predict the time intervals and the classes of action instances in the video. Despite the promising performance, existing two-stream models exhibit slow inference speed due to their reliance on computationally expensive optical flow. In this paper, we introduce a decomposed cross-modal distillation framework to build a strong RGB-based detector by transferring knowledge of the motion modality. Specifically, instead of direct distillation, we propose to separately learn RGB and motion representations, which are in turn combined to perform action localization. The dual-branch design and the asymmetric training objectives enable effective motion knowledge transfer while preserving RGB information intact. In addition, we introduce a local attentive fusion to better exploit the multimodal complementarity. It is designed to preserve the local discriminability of the features that is important for action localization. Extensive experiments on the benchmarks verify the effectiveness of the proposed method in enhancing RGB-based action detectors. Notably, our framework is agnostic to backbones and detection heads, bringing consistent gains across different model combinations.

</details>

### Decomposed Cross-Modal Distillation for RGB-based Temporal Action Detection.
- **链接**: [arXiv:2303.17285](https://arxiv.org/abs/2303.17285) · 📚 被引 21
- **作者**: Pilhyeon Lee, Taeoh Kim, Minho Shim, Dongyoon Wee, Hyeran Byun
- **🏷️ 机构**: Yonsei University, Naver Cloud, AI Tech.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Temporal action detection aims to predict the time intervals and the classes of action instances in the video. Despite the promising performance, existing two-stream models exhibit slow inference speed due to their reliance on computationally expensive optical flow. In this paper, we introduce a decomposed cross-modal distillation framework to build a strong RGB-based detector by transferring knowledge of the motion modality. Specifically, instead of direct distillation, we propose to separately learn RGB and motion representations, which are in turn combined to perform action localization. The dual-branch design and the asymmetric training objectives enable effective motion knowledge transfer while preserving RGB information intact. In addition, we introduce a local attentive fusion to better exploit the multimodal complementarity. It is designed to preserve the local discriminability of the features that is important for action localization. Extensive experiments on the benchmarks verify the effectiveness of the proposed method in enhancing RGB-based action detectors. Notably, our framework is agnostic to backbones and detection heads, bringing consistent gains across different model combinations.

</details>

### Grounding Language Models to Images for Multimodal Inputs and Outputs.
- **链接**: [出版页](https://proceedings.mlr.press/v202/koh23a.html)
- **作者**: Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

- Virtual Sparse Convolution for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MSeg3D: Multi-Modal 3D Semantic Segmentation for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
