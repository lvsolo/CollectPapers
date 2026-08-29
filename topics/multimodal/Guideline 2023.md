# Multimodal — 2023 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 31 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A Large-Scale Outdoor Multi-modal Dataset and Benchmark for Novel View Synthesis and Implicit Scene Reconstruction.
- **链接**: [arXiv:2301.06782](https://arxiv.org/abs/2301.06782) · 📚 被引 33
- **作者**: Chongshan Lu, Fukun Yin, Xin Chen, Wen Liu, Tao Chen, Gang Yu et al.
- **🏷️ 机构**: Fudan University,School of Information Science and Technology,China, Tencent PCG,China, Fudan University,Academy for Engineering and Technology,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Radiance Fields (NeRF) has achieved impressive results in single object scene reconstruction and novel view synthesis, which have been demonstrated on many single modality and single object focused indoor scene datasets like DTU, BMVS, and NeRF Synthetic.However, the study of NeRF on large-scale outdoor scene reconstruction is still limited, as there is no unified outdoor scene dataset for large-scale NeRF evaluation due to expensive data acquisition and calibration costs. In this paper, we propose a large-scale outdoor multi-modal dataset, OMMO dataset, containing complex land objects and scenes with calibrated images, point clouds and prompt annotations. Meanwhile, a new benchmark for several outdoor NeRF-based tasks is established, such as novel view synthesis, surface reconstruction, and multi-modal NeRF. To create the dataset, we capture and collect a large number of real fly-view videos and select high-quality and high-resolution clips from them. Then we design a quality review module to refine images, remove low-quality frames and fail-to-calibrate scenes through a learning-based automatic evaluation plus manual review. Finally, a number of volunteers are employed to add the text descriptions for each scene and key-frame to meet the potential multi-modal requirements in the future. Compared with existing NeRF datasets, our dataset contains abundant real-world urban and natural scenes with various scales, camera trajectories, and lighting conditions. Experiments show that our dataset can benchmark most state-of-the-art NeRF methods on different tasks. We will release the dataset and model weights very soon.

</details>

### MMST-ViT: Climate Change-aware Crop Yield Prediction via Multi-Modal Spatial-Temporal Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00531)
- **作者**: Fudong Lin, Summer Crawford, Kaleb Guillot, Yihe Zhang, Yan Chen, Xu Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Tensor Factorization for Leveraging Cross-Modal Knowledge in Data-Constrained Infrared Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00099) · 📚 被引 1
- **作者**: Manish Sharma, Moitreya Chatterjee, Kuan-Chuan Peng, Suhas Lohit, Michael J. Jones
- **🏷️ 机构**: Rochester Institute of Technology,NY,USA,14623, Mitsubishi Electric Research Laboratories,Cambridge,MA,USA,02139
- **会议**: ICCV 2023

### UniSeg: A Unified Multi-Modal LiDAR Segmentation Network and the OpenPCSeg Codebase.
- **链接**: [arXiv:2309.05573](https://arxiv.org/abs/2309.05573) · [代码](https://github.com/PJLab-ADG/PCSeg) · 📚 被引 80
- **作者**: Youquan Liu, Runnan Chen, Xin Li, Lingdong Kong, Yuchen Yang, Zhaoyang Xia et al.
- **🏷️ 机构**: Shanghai AI Laboratory, The Chinese University of Hong Kong
- **会议**: ICCV 2023

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

### Task-Oriented Multi-Modal Mutual Learning for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02007)
- **作者**: Sifan Long, Zhen Zhao, Junkun Yuan, Zichang Tan, Jiangjiang Liu, Luping Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### ProVLA: Compositional Image Search with Progressive Vision-Language Alignment and Multimodal Fusion.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00293) · 📚 被引 4
- **作者**: Zhizhang Hu, Xinliang Zhu, Son Tran, René Vidal, Arnab Dhua
- **🏷️ 机构**: University of California, Merced, Amazon Visual Search &amp; AR, Amazon M5
- **会议**: ICCV 2023

### Lecture Presentations Multimodal Dataset: Towards Understanding Multimodality in Educational Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01838) · 📚 被引 22
- **作者**: Dong Won Lee, Chaitanya Ahuja, Paul Pu Liang, Sanika Natu, Louis-Philippe Morency
- **🏷️ 机构**: MIT, Carnegie Mellon University
- **会议**: ICCV 2023

### CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00017)
- **作者**: Hritik Bansal, Fan Yin, Nishad Singhi, Aditya Grover, Yu Yang, Kai-Wei Chang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Multimodal Contrastive Learning and Tabular Attention for Automated Alzheimer's Disease Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00261)
- **作者**: Weichen Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Cross-Modal Learning with 3D Deformable Attention for Action Recognition.
- **链接**: [arXiv:2212.05638](https://arxiv.org/abs/2212.05638) · 📚 被引 41
- **作者**: Sangwon Kim, Dasom Ahn, ByoungChul Ko
- **🏷️ 机构**: Keimyung University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An important challenge in vision-based action recognition is the embedding of spatiotemporal features with two or more heterogeneous modalities into a single feature. In this study, we propose a new 3D deformable transformer for action recognition with adaptive spatiotemporal receptive fields and a cross-modal learning scheme. The 3D deformable transformer consists of three attention modules: 3D deformability, local joint stride, and temporal stride attention. The two cross-modal tokens are input into the 3D deformable attention module to create a cross-attention token with a reflected spatiotemporal correlation. Local joint stride attention is applied to spatially combine attention and pose tokens. Temporal stride attention temporally reduces the number of input tokens in the attention module and supports temporal expression learning without the simultaneous use of all tokens. The deformable transformer iterates L-times and combines the last cross-modal token for classification. The proposed 3D deformable transformer was tested on the NTU60, NTU120, FineGYM, and PennAction datasets, and showed results better than or similar to pre-trained state-of-the-art methods even without a pre-training process. In addition, by visualizing important joints and correlations during action recognition through spatial joint and temporal stride attention, the possibility of achieving an explainable potential for action recognition is presented.

</details>

### Multimodal Distillation for Egocentric Action Recognition.
- **链接**: [arXiv:2307.07483](https://arxiv.org/abs/2307.07483) · [代码](https://github.com/gorjanradevski/multimodal-distillation) · 📚 被引 36
- **作者**: Gorjan Radevski, Dusan Grujicic, Matthew B. Blaschko, Marie-Francine Moens, Tinne Tuytelaars
- **🏷️ 机构**: KU Leuven University,Belgium
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The focal point of egocentric video understanding is modelling hand-object interactions. Standard models, e.g. CNNs or Vision Transformers, which receive RGB frames as input perform well. However, their performance improves further by employing additional input modalities that provide complementary cues, such as object detections, optical flow, audio, etc. The added complexity of the modality-specific modules, on the other hand, makes these models impractical for deployment. The goal of this work is to retain the performance of such a multimodal approach, while using only the RGB frames as input at inference time. We demonstrate that for egocentric action recognition on the Epic-Kitchens and the Something-Something datasets, students which are taught by multimodal teachers tend to be more accurate and better calibrated than architecturally equivalent models trained on ground truth labels in a unimodal or multimodal fashion. We further adopt a principled multimodal knowledge distillation framework, allowing us to deal with issues which occur when applying multimodal knowledge distillation in a naive manner. Lastly, we demonstrate the achieved reduction in computational complexity, and show that our approach maintains higher performance with the reduction of the number of input views. We release our code at https://github.com/gorjanradevski/multimodal-distillation.

</details>

### Actor-agnostic Multi-label Action Recognition with Multi-modal Query.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00086) · 📚 被引 19
- **作者**: Anindya Mondal, Sauradip Nag, Joaquin M. Prada, Xiatian Zhu, Anjan Dutta
- **🏷️ 机构**: University of Surrey
- **会议**: ICCV 2023

### Decouple Before Interact: Multi-Modal Prompt Learning for Continual Visual Question Answering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00276) · 📚 被引 19
- **作者**: Zi Qian, Xin Wang, Xuguang Duan, Pengda Qin, Yuhong Li, Wenwu Zhu
- **🏷️ 机构**: Tsinghua University,BNRist,Department of Computer Science and Technology, Alibaba Group
- **会议**: ICCV 2023

### MEGA: Multimodal Alignment Aggregation and Distillation For Cinematic Video Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02132)
- **作者**: Najmeh Sadoughi, Xinyu Li, Avijit Vajpayee, David Fan, Bing Shuai, Hector J. Santos-Villalobos et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Dense 2D-3D Indoor Prediction with Sound via Aligned Cross-Modal Distillation.
- **链接**: [arXiv:2309.11081](https://arxiv.org/abs/2309.11081) · 📚 被引 6
- **作者**: Heeseung Yun, Joonil Na, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sound can convey significant information for spatial reasoning in our daily lives. To endow deep networks with such ability, we address the challenge of dense indoor prediction with sound in both 2D and 3D via cross-modal knowledge distillation. In this work, we propose a Spatial Alignment via Matching (SAM) distillation framework that elicits local correspondence between the two modalities in vision-to-audio knowledge transfer. SAM integrates audio features with visually coherent learnable spatial embeddings to resolve inconsistencies in multiple layers of a student model. Our approach does not rely on a specific input representation, allowing for flexibility in the input shapes or dimensions without performance degradation. With a newly curated benchmark named Dense Auditory Prediction of Surroundings (DAPS), we are the first to tackle dense indoor prediction of omnidirectional surroundings in both 2D and 3D with audio observations. Specifically, for audio-based depth estimation, semantic segmentation, and challenging 3D scene reconstruction, the proposed distillation framework consistently achieves state-of-the-art performance across various metrics and backbone architectures.

</details>

## 跨领域论文（完整笔记在其他领域）

- ObjectFusion: Multi-modal 3D Object Detection with Object-Centric Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202023.md)
- GraphAlign: Enhancing Accurate Feature Alignment by Graph matching for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- PointDC: Unsupervised Semantic Segmentation of 3D Point Clouds via Cross-modal Distillation and Super-Voxel Clustering. → [3d-detection](../3d-detection/Guideline%202023.md)
- BEV-DG: Cross-Modal Learning under Bird's-Eye View for Domain Generalization of 3D Semantic Segmentation. → [bev](../bev/Guideline%202023.md)
- AIDE: A Vision-Driven Multi-View, Multi-Modal, Multi-Tasking Dataset for Assistive Driving Perception. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Replay: Multi-modal Multi-view Acted Videos for Casual Holography. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Zenseact Open Dataset: A large-scale and diverse multimodal dataset for autonomous driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Class-Incremental Grouping Network for Continual Audio-Visual Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- Audio-Visual Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- Multimodal Parameter-Efficient Few-Shot Class Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
