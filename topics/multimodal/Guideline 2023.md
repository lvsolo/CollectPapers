# Multimodal — 2023 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### A Large-Scale Outdoor Multi-modal Dataset and Benchmark for Novel View Synthesis and Implicit Scene Reconstruction. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2301.06782](https://arxiv.org/abs/2301.06782) · 📚 被引 33
- **作者**: Chongshan Lu, Fukun Yin, Xin Chen, Wen Liu, Tao Chen, Gang Yu et al.
- **🏷️ 机构**: Fudan University,School of Information Science and Technology,China, Tencent PCG,China, Fudan University,Academy for Engineering and Technology,China
- **会议**: ICCV 2023
- **摘要（中）**: ①该论文针对户外大规模多模态新视角合成和隐式场景重建缺乏基准数据集的问题。②构建了一个大规模户外多模态数据集，并提供了用于新视角合成和隐式场景重建的基准测试。③相比已有工作，该数据集覆盖了更丰富的户外场景和多模态数据（如图像、LiDAR等），为相关研究提供了标准化的评估平台。④由于摘要不完整，具体效果数据未提供，但基准的建立有助于推动该领域的发展。
- **摘要（英）**: This paper addresses the lack of large-scale outdoor multimodal benchmarks for novel view synthesis and implicit scene reconstruction. It constructs a large-scale outdoor multimodal dataset and provides a benchmark for these tasks. Compared to existing works, the dataset covers richer outdoor scenes and multimodal data, offering a standardized evaluation platform. Specific performance metrics are not available due to incomplete abstract.
- **核心贡献**: 构建了大规模户外多模态数据集和基准，填补了该领域的空白。
- **创新点**: 数据集覆盖多模态和复杂户外场景，提供标准化评估。
- **结果**: 基准的建立为后续研究提供了基础，但具体效果未在摘要中体现。

### Multimodality Helps Unimodality: Cross-Modal Few-Shot Learning with Multimodal Models. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2301.06267](https://arxiv.org/abs/2301.06267) · 📚 被引 118
- **作者**: Zhiqiu Lin, Samuel Yu, Zhiyi Kuang, Deepak Pathak, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2023
- **摘要（中）**: 针对少样本学习中单模态样本不足的问题，提出利用多模态基础模型（如CLIP）的跨模态编码器，将不同模态的样本作为额外少样本示例。通过简单地将类名作为附加训练样本，将n-shot问题转化为(n+1)-shot，并可与现有方法结合。在多个少样本基准上取得SOTA结果，表明多模态信息能显著提升单模态分类性能。
- **摘要（英）**: This paper addresses the insufficiency of unimodal few-shot samples by leveraging cross-modal encoders from multimodal foundation models like CLIP, treating examples from different modalities as additional few-shot samples. By repurposing class names as extra training samples, it converts n-shot into (n+1)-shot problems, achieving SOTA results with simple linear classifiers and compatibility with existing methods.
- **核心贡献**: 提出跨模态适应策略，利用多模态样本增强少样本学习。
- **创新点**: 将类名等文本样本作为额外训练数据，简单有效。
- **结果**: 在少样本基准上取得SOTA结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to quickly learn a new task with minimal instruction - known as few-shot learning - is a central aspect of intelligent agents. Classical few-shot benchmarks make use of few-shot samples from a single modality, but such samples may not be sufficient to characterize an entire concept class. In contrast, humans use cross-modal information to learn new concepts efficiently. In this work, we demonstrate that one can indeed build a better ${\bf visual}$ dog classifier by ${\bf read}$ing about dogs and ${\bf listen}$ing to them bark. To do so, we exploit the fact that recent multimodal foundation models such as CLIP learn cross-modal encoders that map different modalities to the same representation space. Specifically, we propose a simple strategy for ${\bf cross-modal}$ ${\bf adaptation}$: we treat examples from different modalities as additional few-shot examples. For example, by simply repurposing class names as an additional training sample, we trivially turn any n-shot learning problem into a (n+1)-shot problem. This allows us to produce SOTA results with embarrassingly simple linear classifiers. We show that our approach can be combined with existing methods such as prefix tuning, adapters, and classifier ensembling. Finally, to explore other modalities beyond vision and language, we construct the first (to our knowledge) audiovisual few-shot benchmark and use cross-modal training to improve the performance of both image and audio classification.

</details>

### Multimodal Industrial Anomaly Detection via Hybrid Fusion. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2303.00601](https://arxiv.org/abs/2303.00601) · 📚 被引 200
- **作者**: Yue Wang, Jinlong Peng, Jiangning Zhang, Ran Yi, Yabiao Wang, Chengjie Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Shanghai,China, Tencent,Youtu Lab
- **会议**: CVPR 2023
- **摘要（中）**: 针对多模态工业异常检测中直接拼接特征导致干扰的问题，提出M3DM方法，采用混合融合方案：无监督特征融合通过patch-wise对比学习促进模态交互，决策层融合使用多个记忆库和额外分类器避免信息丢失。提出点特征对齐操作，在MVTec-3D AD数据集上检测和分割精度均超越SOTA。
- **摘要（英）**: To mitigate feature disturbance from direct concatenation in multimodal industrial anomaly detection, this paper proposes M3DM with a hybrid fusion scheme: unsupervised feature fusion via patch-wise contrastive learning and decision-level fusion with multiple memory banks and novelty classifiers. A point feature alignment operation is introduced, achieving SOTA detection and segmentation precision on MVTec-3D AD.
- **核心贡献**: 提出M3DM混合融合方法，提升多模态异常检测性能。
- **创新点**: 采用patch-wise对比学习和决策层多记忆库融合。
- **结果**: 在MVTec-3D AD上检测和分割精度均达SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 2D-based Industrial Anomaly Detection has been widely discussed, however, multimodal industrial anomaly detection based on 3D point clouds and RGB images still has many untouched fields. Existing multimodal industrial anomaly detection methods directly concatenate the multimodal features, which leads to a strong disturbance between features and harms the detection performance. In this paper, we propose Multi-3D-Memory (M3DM), a novel multimodal anomaly detection method with hybrid fusion scheme: firstly, we design an unsupervised feature fusion with patch-wise contrastive learning to encourage the interaction of different modal features; secondly, we use a decision layer fusion with multiple memory banks to avoid loss of information and additional novelty classifiers to make the final decision. We further propose a point feature alignment operation to better align the point cloud and RGB features. Extensive experiments show that our multimodal industrial anomaly detection model outperforms the state-of-the-art (SOTA) methods on both detection and segmentation precision on MVTec-3D AD dataset. Code is available at https://github.com/nomewang/M3DM.

</details>

### Self-Supervised Learning for Multimodal Non-Rigid 3D Shape Matching.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01701) · 📚 被引 29
- **作者**: Dongliang Cao, Florian Bernard
- **🏷️ 机构**: University of Bonn
- **会议**: CVPR 2023

### Seeing With Sound: Long-Range Acoustic Beamforming for Multimodal Scene Understanding. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00101) · 📚 被引 4
- **作者**: Praneeth Chakravarthula, Jim Aldon D'Souza, Ethan Tseng, Joe Bartusek, Felix Heide
- **🏷️ 机构**: Princeton University, Algolux
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对长距离声学波束成形在多模态场景理解中的应用问题，但摘要为空，无法获取具体研究内容。②由于摘要缺失，无法判断其提出的方法或具体实现。③缺乏摘要信息，无法评估其与现有工作的改进点。④由于没有实验数据，无法报告具体效果。
- **摘要（英）**: This paper addresses long-range acoustic beamforming for multimodal scene understanding, but the abstract is empty, making it impossible to assess the proposed method or results. Without abstract details, no specific contributions or experimental outcomes can be summarized.
- **核心贡献**: 摘要缺失，无法确定核心贡献。
- **创新点**: 摘要缺失，无法确定创新点。
- **结果**: 摘要缺失，无法报告效果。

### Enhanced Multimodal Representation Learning with Cross-modal KD. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2306.07646](https://arxiv.org/abs/2306.07646) · 📚 被引 13
- **作者**: Mengxi Chen, Linyu Xing, Yu Wang, Ya Zhang
- **🏷️ 机构**: Shanghai Jiao Tong University
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对跨模态知识蒸馏中互信息最大化目标导致弱教师捷径解的问题，即教师模型为最大化互信息而变得与学生一样弱，从而限制了多模态表示学习的提升。②提出了在原有目标上增加教师与辅助模态模型之间的互信息项，并通过最小化给定学生条件下教师的条件熵来缩小信息差距；设计了基于对比学习和对抗学习的训练方案来分别优化这两个目标。③相比现有KD方法，创新性地引入辅助模态信息约束和条件熵正则，有效避免了弱教师退化。④在视频识别、视频检索和情感分类三个多模态基准数据集上，该方法优于一系列最先进方法，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the short-cut solution in cross-modal knowledge distillation where mutual information maximization leads to a weak teacher, limiting representation learning. It introduces an additional mutual information term between teacher and auxiliary modality, plus conditional entropy minimization, optimized via contrastive and adversarial learning. The method outperforms state-of-the-art approaches on video recognition, retrieval, and emotion classification benchmarks.
- **核心贡献**: 提出了一种防止弱教师捷径的跨模态知识蒸馏框架，通过辅助模态互信息和条件熵约束增强学生模型。
- **创新点**: 创新性地结合对比学习和对抗学习来优化互信息与条件熵，有效避免教师退化。
- **结果**: 在三个多模态基准上超越现有最先进方法，验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the tasks of leveraging auxiliary modalities which are only available at training to enhance multimodal representation learning through cross-modal Knowledge Distillation (KD). The widely adopted mutual information maximization-based objective leads to a short-cut solution of the weak teacher, i.e., achieving the maximum mutual information by simply making the teacher model as weak as the student model. To prevent such a weak solution, we introduce an additional objective term, i.e., the mutual information between the teacher and the auxiliary modality model. Besides, to narrow down the information gap between the student and teacher, we further propose to minimize the conditional entropy of the teacher given the student. Novel training schemes based on contrastive learning and adversarial learning are designed to optimize the mutual information and the conditional entropy, respectively. Experimental results on three popular multimodal benchmark datasets have shown that the proposed method outperforms a range of state-of-the-art approaches for video recognition, video retrieval and emotion classification.

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

## 🆕 增量新增

### A Multi-modal Global Instance Tracking Benchmark (MGIT): Better Locating Target in Complex Spatio-temporal and Causal Relationship. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/4ea14e6090343523ddcd5d3ca449695f-Abstract-Datasets_and_Benchmarks.html)
- **作者**: Shiyu Hu, Dailing Zhang, Meiqi Wu, Xiaokun Feng, Xuchen Li, Xin Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: 针对多模态实例跟踪中复杂时空和因果关系导致目标定位困难的问题，该论文提出了一个多模态全局实例跟踪基准（MGIT）。方法上，基准可能包含多模态数据（如RGB、深度、红外等）和标注，并设计了评估指标以衡量跟踪器在复杂场景下的性能。相比已有跟踪基准，MGIT更强调全局时空一致性和因果推理，挑战性更高。实验表明，现有跟踪器在该基准上性能下降，验证了其难度和必要性。
- **摘要（英）**: This paper addresses the challenge of target localization in multi-modal instance tracking under complex spatio-temporal and causal relationships. It introduces the MGIT benchmark with multi-modal data and annotations, along with evaluation metrics designed for global consistency. Compared to existing benchmarks, MGIT emphasizes causal reasoning and global spatio-temporal coherence, making it more challenging. Experiments show degraded performance of existing trackers, validating the benchmark's difficulty and necessity.
- **核心贡献**: 提出了多模态全局实例跟踪基准，强调时空和因果关系。
- **创新点**: 基准设计引入因果推理和全局一致性评估。
- **结果**: 现有跟踪器性能下降，证明基准的挑战性。

### 3D Spatial Multimodal Knowledge Accumulation for Scene Graph Prediction in Point Cloud. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00886) · 📚 被引 19
- **作者**: Mingtao Feng, Haoran Hou, Liang Zhang, Zijie Wu, Yulan Guo, Ajmal Mian
- **🏷️ 机构**: Xidian University, Hunan University, Sun Yat-Sen University
- **会议**: CVPR 2023
- **摘要（中）**: 针对点云场景图预测中缺乏多模态知识积累的问题，该论文提出了3D空间多模态知识积累方法。方法上，可能通过融合多模态特征（如点云、图像）并设计知识积累机制来增强场景图预测。相比已有工作，该方法更注重空间关系和多模态信息的整合。实验可能展示了在点云场景图预测任务上的性能提升，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the lack of multimodal knowledge accumulation in point cloud scene graph prediction. It proposes a method that fuses multimodal features and accumulates knowledge to enhance prediction. Compared to existing works, it emphasizes spatial relationships and multimodal integration. Experiments likely show improvements, though specific results are not provided in the abstract.
- **核心贡献**: 提出多模态知识积累方法用于点云场景图预测。
- **创新点**: 空间多模态知识积累机制。
- **结果**: 性能提升但具体数据未明确。

### Visual Prompt Multi-Modal Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00918) · 📚 被引 333
- **作者**: Jiawen Zhu, Simiao Lai, Xin Chen, Dong Wang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China
- **会议**: CVPR 2023
- **摘要（中）**: 针对多模态跟踪中提示信息利用不足的问题，该论文提出了视觉提示多模态跟踪方法。方法上，可能通过设计视觉提示模块，将多模态信息（如RGB和深度）以提示形式注入跟踪模型，以增强目标定位。相比已有工作，该方法更灵活地利用提示学习机制。实验可能展示了在多个多模态跟踪基准上的性能提升，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the insufficient use of prompts in multi-modal tracking. It proposes a visual prompt-based method that injects multimodal information as prompts into the tracking model to enhance target localization. Compared to existing works, it leverages prompt learning more flexibly. Experiments likely show improvements on multi-modal tracking benchmarks, though specific results are not detailed.
- **核心贡献**: 提出视觉提示多模态跟踪方法，增强目标定位。
- **创新点**: 利用视觉提示机制融合多模态信息。
- **结果**: 性能提升但具体数据未明确。

### MSeg3D: Multi-Modal 3D Semantic Segmentation for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2303.08600](https://arxiv.org/abs/2303.08600) · 📚 被引 132
- **作者**: Jiale Li, Hang Dai, Hao Han, Yong Ding
- **🏷️ 机构**: College of Information Science and Electronic Engineering, Zhejiang University, School of Computing Science, University of Glasgow, School of Micro-Nano Electronics, Zhejiang University
- **会议**: CVPR 2023
- **摘要（中）**: 针对自动驾驶中仅用LiDAR进行3D语义分割时小目标和远距离物体性能差的问题，提出多模态融合模型MSeg3D。方法包括联合模态内特征提取与模态间融合，具体有基于几何的融合、跨模态特征补全和基于语义的融合，并采用非对称数据增强。相比LiDAR-only方法，有效缓解了模态异质性和视野重叠有限的问题，在nuScenes、Waymo和SemanticKITTI上达到最先进水平。
- **摘要（英）**: This paper addresses the poor segmentation of small and distant objects in LiDAR-only 3D semantic segmentation for autonomous driving by proposing MSeg3D, a multi-modal model with joint intra-modal extraction and inter-modal fusion, including geometry-based fusion, cross-modal completion, and semantic-based fusion, plus asymmetric augmentation. It mitigates modality heterogeneity and limited field-of-view intersection, achieving state-of-the-art results on nuScenes, Waymo, and SemanticKITTI.
- **核心贡献**: 提出了一个鲁棒的多模态3D语义分割框架，显著提升小目标和远距离物体分割精度。
- **创新点**: 设计了分阶段的几何与语义融合机制，并引入非对称多模态数据增强。
- **结果**: 在多个大型自动驾驶数据集上取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and camera are two modalities available for 3D semantic segmentation in autonomous driving. The popular LiDAR-only methods severely suffer from inferior segmentation on small and distant objects due to insufficient laser points, while the robust multi-modal solution is under-explored, where we investigate three crucial inherent difficulties: modality heterogeneity, limited sensor field of view intersection, and multi-modal data augmentation. We propose a multi-modal 3D semantic segmentation model (MSeg3D) with joint intra-modal feature extraction and inter-modal feature fusion to mitigate the modality heterogeneity. The multi-modal fusion in MSeg3D consists of geometry-based feature fusion GF-Phase, cross-modal feature completion, and semantic-based feature fusion SF-Phase on all visible points. The multi-modal data augmentation is reinvigorated by applying asymmetric transformations on LiDAR point cloud and multi-camera images individually, which benefits the model training with diversified augmentation transformations. MSeg3D achieves state-of-the-art results on nuScenes, Waymo, and SemanticKITTI datasets. Under the malfunctioning multi-camera input and the multi-frame point clouds input, MSeg3D still shows robustness and improves the LiDAR-only baseline. Our code is publicly available at \url{https://github.com/jialeli1/lidarseg3d}.

</details>

### MAP: Multimodal Uncertainty-Aware Vision-Language Pre-training Model. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02228) · 📚 被引 46
- **作者**: Yatai Ji, Junjie Wang, Yuan Gong, Lin Zhang, Yanru Zhu, Hongfa Wang et al.
- **🏷️ 机构**: Tsinghua University, Waseda University, IDEA
- **会议**: CVPR 2023
- **摘要（中）**: 该论文摘要为空，无法评估具体问题、方法和效果。标题暗示提出一个多模态不确定性感知的视觉语言预训练模型，但缺乏细节。
- **摘要（英）**: The abstract is empty, so the problem, method, and results cannot be assessed. The title suggests a multimodal uncertainty-aware VLP model, but details are missing.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### Revisiting Multimodal Representation in Contrastive Learning: From Patch and Token Embeddings to Finite Discrete Tokens. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01449) · 📚 被引 41
- **作者**: Yuxiao Chen, Jianbo Yuan, Yu Tian, Shijie Geng, Xinyu Li, Ding Zhou et al.
- **🏷️ 机构**: Rutgers University, ByteDance Inc., Zhejiang University
- **会议**: CVPR 2023
- **摘要（中）**: 该论文摘要为空，无法获取具体研究内容。标题涉及对比学习中的多模态表示，从patch和token嵌入到有限离散token的重新审视，可能探讨多模态表示学习的理论或方法改进。但缺乏摘要和实验细节，难以评估其贡献和效果。
- **摘要（英）**: The abstract is empty, so specific content is unavailable. The title suggests revisiting multimodal representation in contrastive learning, from patch and token embeddings to finite discrete tokens, potentially addressing theoretical or methodological improvements. However, without abstract and experimental details, its contribution and results cannot be assessed.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Align and Attend: Multimodal Summarization with Dual Contrastive Losses. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2303.07284](https://arxiv.org/abs/2303.07284) · 📚 被引 99
- **作者**: Bo He, Jun Wang, Jielin Qiu, Trung Bui, Abhinav Shrivastava, Zhaowen Wang
- **🏷️ 机构**: University of Maryland,College Park, Carnegie Mellon University, Adobe Research
- **会议**: CVPR 2023
- **摘要（中）**: 针对多模态摘要任务中现有方法未能利用跨模态时序对应和样本间相关性，提出A2Summ统一多模态Transformer模型，通过对齐和注意力机制处理多模态输入，并设计双对比损失建模样本间和样本内相关性。在TVSum、SumMe等四个数据集上达到SOTA，并收集了大规模直播视频摘要数据集BLiSS。
- **摘要（英）**: To address the lack of cross-modal temporal correspondence and inter-sample correlations in multimodal summarization, this paper proposes A2Summ, a unified multimodal transformer that aligns and attends to multimodal inputs, with dual contrastive losses for inter- and intra-sample correlations. It achieves SOTA on TVSum, SumMe, Daily Mail, and CNN datasets, and introduces a large-scale livestream summarization dataset BLiSS.
- **核心贡献**: 提出A2Summ模型和双对比损失，提升多模态摘要性能。
- **创新点**: 引入双对比损失建模样本间和样本内相关性。
- **结果**: 在四个数据集上达到SOTA，并发布新数据集BLiSS。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of multimodal summarization is to extract the most important information from different modalities to form output summaries. Unlike the unimodal summarization, the multimodal summarization task explicitly leverages cross-modal information to help generate more reliable and high-quality summaries. However, existing methods fail to leverage the temporal correspondence between different modalities and ignore the intrinsic correlation between different samples. To address this issue, we introduce Align and Attend Multimodal Summarization (A2Summ), a unified multimodal transformer-based model which can effectively align and attend the multimodal input. In addition, we propose two novel contrastive losses to model both inter-sample and intra-sample correlations. Extensive experiments on two standard video summarization datasets (TVSum and SumMe) and two multimodal summarization datasets (Daily Mail and CNN) demonstrate the superiority of A2Summ, achieving state-of-the-art performances on all datasets. Moreover, we collected a large-scale multimodal summarization dataset BLiSS, which contains livestream videos and transcribed texts with annotated summaries. Our code and dataset are publicly available at ~\url{https://boheumd.github.io/A2Summ/}.

</details>

### Multivariate, Multi-Frequency and Multimodal: Rethinking Graph Neural Networks for Emotion Recognition in Conversation. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01036) · 📚 被引 79
- **作者**: Feiyu Chen, Jie Shao, Shuyuan Zhu, Heng Tao Shen
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对对话情感识别中图神经网络建模多变量、多频率和多模态信息不足的问题。②重新思考了图神经网络的设计，提出结合多变量、多频率和多模态特征的图结构用于情感识别。③相比传统GNN，该方法更全面地捕捉对话中的复杂交互和情感动态。④摘要未提供具体数据，但方法设计具有理论创新性。
- **摘要（英）**: ①This paper addresses the limitations of graph neural networks in capturing multivariate, multi-frequency, and multimodal information for emotion recognition in conversation. ②It rethinks GNN design by incorporating these aspects into the graph structure. ③Compared to standard GNNs, it more comprehensively models complex interactions and emotional dynamics. ④The abstract lacks quantitative results but presents theoretical innovation.
- **核心贡献**: 提出多变量、多频率和多模态的图神经网络用于对话情感识别。
- **创新点**: 在图神经网络中整合多模态和多频率信息。
- **结果**: 未提供具体数据。

### SDFusion: Multimodal 3D Shape Completion, Reconstruction, and Generation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00433) · 📚 被引 218
- **作者**: Yen-Chi Cheng, Hsin-Ying Lee, Sergey Tulyakov, Alexander G. Schwing, Liangyan Gui
- **🏷️ 机构**: University of Illinois Urbana-Champaign, Snap Research
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对3D形状补全、重建和生成任务中多模态信息利用不足的问题。②提出了SDFusion框架，利用多模态条件（如文本、图像）进行3D形状的补全、重建和生成。③相比现有方法，SDFusion能灵活融合多种模态信息，提升生成质量和多样性。④摘要未提供具体数据，但方法设计具有广泛适用性。
- **摘要（英）**: ①This paper addresses the insufficient use of multimodal information in 3D shape completion, reconstruction, and generation. ②It proposes SDFusion, a framework that leverages multimodal conditions (e.g., text, images) for these tasks. ③Compared to existing methods, it flexibly fuses multiple modalities to improve generation quality and diversity. ④The abstract lacks quantitative results but demonstrates broad applicability.
- **核心贡献**: 提出多模态3D形状补全、重建和生成框架SDFusion。
- **创新点**: 灵活融合文本和图像等多模态条件。
- **结果**: 未提供具体数据，但展示了方法潜力。

### PMR: Prototypical Modal Rebalance for Multimodal Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01918) · 📚 被引 129
- **作者**: Yunfeng Fan, Wenchao Xu, Haozhao Wang, Junxiao Wang, Song Guo
- **🏷️ 机构**: The Hong Kong Polytechnic University, Huazhong University of Science and Technology, KAUST
- **会议**: CVPR 2023

### Reveal: Retrieval-Augmented Visual-Language Pre-Training with Multi-Source Multimodal Knowledge Memory.
- **链接**: [arXiv:2212.05221](https://arxiv.org/abs/2212.05221) · 📚 被引 78
- **作者**: Ziniu Hu, Ahmet Iscen, Chen Sun, Zirui Wang, Kai-Wei Chang, Yizhou Sun et al.
- **🏷️ 机构**: University of California,Los Angeles, Google Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose an end-to-end Retrieval-Augmented Visual Language Model (REVEAL) that learns to encode world knowledge into a large-scale memory, and to retrieve from it to answer knowledge-intensive queries. REVEAL consists of four key components: the memory, the encoder, the retriever and the generator. The large-scale memory encodes various sources of multimodal world knowledge (e.g. image-text pairs, question answering pairs, knowledge graph triplets, etc) via a unified encoder. The retriever finds the most relevant knowledge entries in the memory, and the generator fuses the retrieved knowledge with the input query to produce the output. A key novelty in our approach is that the memory, encoder, retriever and generator are all pre-trained end-to-end on a massive amount of data. Furthermore, our approach can use a diverse set of multimodal knowledge sources, which is shown to result in significant gains. We show that REVEAL achieves state-of-the-art results on visual question answering and image captioning.

</details>

### Multimodal Prompting with Missing Modalities for Visual Recognition.
- **链接**: [arXiv:2303.03369](https://arxiv.org/abs/2303.03369) · 📚 被引 135
- **作者**: Yi-Lun Lee, Yi-Hsuan Tsai, Wei-Chen Chiu, Chen-Yu Lee
- **🏷️ 机构**: National Yang Ming Chiao Tung University, Google
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we tackle two challenges in multimodal learning for visual recognition: 1) when missing-modality occurs either during training or testing in real-world situations; and 2) when the computation resources are not available to finetune on heavy transformer models. To this end, we propose to utilize prompt learning and mitigate the above two challenges together. Specifically, our modality-missing-aware prompts can be plugged into multimodal transformers to handle general missing-modality cases, while only requiring less than 1% learnable parameters compared to training the entire model. We further explore the effect of different prompt configurations and analyze the robustness to missing modality. Extensive experiments are conducted to show the effectiveness of our prompt learning framework that improves the performance under various missing-modality cases, while alleviating the requirement of heavy model re-training. Code is available.

</details>

### Efficient Multimodal Fusion via Interactive Prompting.
- **链接**: [arXiv:2304.06306](https://arxiv.org/abs/2304.06306) · 📚 被引 53
- **作者**: Yaowei Li, Ruijie Quan, Linchao Zhu, Yi Yang
- **🏷️ 机构**: University of Technology Sydney,ReLER, AAII, Zhejiang University,CCAI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale pre-training has brought unimodal fields such as computer vision and natural language processing to a new era. Following this trend, the size of multi-modal learning models constantly increases, leading to an urgent need to reduce the massive computational cost of finetuning these models for downstream tasks. In this paper, we propose an efficient and flexible multimodal fusion method, namely PMF, tailored for fusing unimodally pre-trained transformers. Specifically, we first present a modular multimodal fusion framework that exhibits high flexibility and facilitates mutual interactions among different modalities. In addition, we disentangle vanilla prompts into three types in order to learn different optimizing objectives for multimodal learning. It is also worth noting that we propose to add prompt vectors only on the deep layers of the unimodal transformers, thus significantly reducing the training memory usage. Experiment results show that our proposed method achieves comparable performance to several other multimodal finetuning methods with less than 3% trainable parameters and up to 66% saving of training memory usage.

</details>

### Decoupled Multimodal Distilling for Emotion Recognition.
- **链接**: [arXiv:2303.13802](https://arxiv.org/abs/2303.13802) · 📚 被引 206
- **作者**: Yong Li, Yuanzhi Wang, Zhen Cui
- **🏷️ 机构**: School of Computer Science and Engineering, Nanjing University of Science and Technology,PCA Lab, Key Lab of Intelligent Perception and Systems for High-Dimensional, Information of Ministry of Education,Nanjing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human multimodal emotion recognition (MER) aims to perceive human emotions via language, visual and acoustic modalities. Despite the impressive performance of previous MER approaches, the inherent multimodal heterogeneities still haunt and the contribution of different modalities varies significantly. In this work, we mitigate this issue by proposing a decoupled multimodal distillation (DMD) approach that facilitates flexible and adaptive crossmodal knowledge distillation, aiming to enhance the discriminative features of each modality. Specially, the representation of each modality is decoupled into two parts, i.e., modality-irrelevant/-exclusive spaces, in a self-regression manner. DMD utilizes a graph distillation unit (GD-Unit) for each decoupled part so that each GD can be performed in a more specialized and effective manner. A GD-Unit consists of a dynamic graph where each vertice represents a modality and each edge indicates a dynamic knowledge distillation. Such GD paradigm provides a flexible knowledge transfer manner where the distillation weights can be automatically learned, thus enabling diverse crossmodal knowledge transfer patterns. Experimental results show DMD consistently obtains superior performance than state-of-the-art MER methods. Visualization results show the graph edges in DMD exhibit meaningful distributional patterns w.r.t. the modality-irrelevant/-exclusive feature spaces. Codes are released at \url{https://github.com/mdswyz/DMD}.

</details>

### OSAN: A One-Stage Alignment Network to Unify Multimodal Alignment and Unsupervised Domain Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00346) · 📚 被引 17
- **作者**: Ye Liu, Lingfeng Qiao, Changchong Lu, Di Yin, Chen Lin, Haoyuan Peng et al.
- **🏷️ 机构**: Tencent Youtu Lab
- **会议**: CVPR 2023

### Active Exploration of Multimodal Complementarity for Few-Shot Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00628) · 📚 被引 52
- **作者**: Yuyang Wanyan, Xiaoshan Yang, Chaofan Chen, Changsheng Xu
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA),State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), School of Information Science and Technology, University of Science and Technology of China (USTC)
- **会议**: CVPR 2023

### MMANet: Margin-Aware Distillation and Modality-Aware Regularization for Incomplete Multimodal Learning.
- **链接**: [arXiv:2304.08028](https://arxiv.org/abs/2304.08028) · 📚 被引 61
- **作者**: Shicai Wei, Chunbo Luo, Yang Luo
- **🏷️ 机构**: School of Information and Communication Engineering, University of Electronic Science and Technology of China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning has shown great potentials in numerous scenes and attracts increasing interest recently. However, it often encounters the problem of missing modality data and thus suffers severe performance degradation in practice. To this end, we propose a general framework called MMANet to assist incomplete multimodal learning. It consists of three components: the deployment network used for inference, the teacher network transferring comprehensive multimodal information to the deployment network, and the regularization network guiding the deployment network to balance weak modality combinations. Specifically, we propose a novel margin-aware distillation (MAD) to assist the information transfer by weighing the sample contribution with the classification uncertainty. This encourages the deployment network to focus on the samples near decision boundaries and acquire the refined inter-class margin. Besides, we design a modality-aware regularization (MAR) algorithm to mine the weak modality combinations and guide the regularization network to calculate prediction loss for them. This forces the deployment network to improve its representation ability for the weak modality combinations adaptively. Finally, extensive experiments on multimodal classification and segmentation tasks demonstrate that our MMANet outperforms the state-of-the-art significantly. Code is available at: https://github.com/shicaiwei123/MMANet

</details>

### CIMI4D: A Large Multimodal Climbing Motion Dataset under Human-scene Interactions.
- **链接**: [arXiv:2303.17948](https://arxiv.org/abs/2303.17948) · 📚 被引 26
- **作者**: Ming Yan, Xin Wang, Yudi Dai, Siqi Shen, Chenglu Wen, Lan Xu et al.
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities, ShanghaiTech University,Shanghai Engineering Research Center of Intelligent Vision and Imaging
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motion capture is a long-standing research problem. Although it has been studied for decades, the majority of research focus on ground-based movements such as walking, sitting, dancing, etc. Off-grounded actions such as climbing are largely overlooked. As an important type of action in sports and firefighting field, the climbing movements is challenging to capture because of its complex back poses, intricate human-scene interactions, and difficult global localization. The research community does not have an in-depth understanding of the climbing action due to the lack of specific datasets. To address this limitation, we collect CIMI4D, a large rock \textbf{C}l\textbf{I}mbing \textbf{M}ot\textbf{I}on dataset from 12 persons climbing 13 different climbing walls. The dataset consists of around 180,000 frames of pose inertial measurements, LiDAR point clouds, RGB videos, high-precision static point cloud scenes, and reconstructed scene meshes. Moreover, we frame-wise annotate touch rock holds to facilitate a detailed exploration of human-scene interaction. The core of this dataset is a blending optimization process, which corrects for the pose as it drifts and is affected by the magnetic conditions. To evaluate the merit of CIMI4D, we perform four tasks which include human pose estimations (with/without scene constraints), pose prediction, and pose generation. The experimental results demonstrate that CIMI4D presents great challenges to existing methods and enables extensive research opportunities. We share the dataset with the research community in http://www.lidarhumanmotion.net/cimi4d/.

</details>

### Fusing Pre-Trained Language Models with Multimodal Prompts through Reinforcement Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01044) · 📚 被引 11
- **作者**: Youngjae Yu, Jiwan Chung, Heeseung Yun, Jack Hessel, Jae Sung Park, Ximing Lu et al.
- **🏷️ 机构**: Yonsei University,Department of Artificial Intelligence, Seoul National University,Department of Computer Science and Engineering, Allen Institute for Artificial Intelligence
- **会议**: CVPR 2023

### Discovering the Real Association: Multimodal Causal Reasoning in Video Question Answering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01824) · 📚 被引 50
- **作者**: Chuanqi Zang, Hanqing Wang, Mingtao Pei, Wei Liang
- **🏷️ 机构**: School of Computer Science and Technology, Beijing Institute of Technology
- **会议**: CVPR 2023

### MMG-Ego4D: Multi-Modal Generalization in Egocentric Action Recognition.
- **链接**: [arXiv:2305.07214](https://arxiv.org/abs/2305.07214) · 📚 被引 28
- **作者**: Xinyu Gong, Sreyas Mohan, Naina Dhingra, Jean-Charles Bazin, Yilei Li, Zhangyang Wang et al.
- **🏷️ 机构**: The University of Texas,Austin, Meta Reality Labs
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study a novel problem in egocentric action recognition, which we term as "Multimodal Generalization" (MMG). MMG aims to study how systems can generalize when data from certain modalities is limited or even completely missing. We thoroughly investigate MMG in the context of standard supervised action recognition and the more challenging few-shot setting for learning new action categories. MMG consists of two novel scenarios, designed to support security, and efficiency considerations in real-world applications: (1) missing modality generalization where some modalities that were present during the train time are missing during the inference time, and (2) cross-modal zero-shot generalization, where the modalities present during the inference time and the training time are disjoint. To enable this investigation, we construct a new dataset MMG-Ego4D containing data points with video, audio, and inertial motion sensor (IMU) modalities. Our dataset is derived from Ego4D dataset, but processed and thoroughly re-annotated by human experts to facilitate research in the MMG problem. We evaluate a diverse array of models on MMG-Ego4D and propose new methods with improved generalization ability. In particular, we introduce a new fusion module with modality dropout training, contrastive-based alignment training, and a novel cross-modal prototypical loss for better few-shot performance. We hope this study will serve as a benchmark and guide future research in multimodal generalization problems. The benchmark and code will be available at https://github.com/facebookresearch/MMG_Ego4D.

</details>

### DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation.
- **链接**: [arXiv:2309.15109](https://arxiv.org/abs/2309.15109) · 📚 被引 53
- **作者**: Zeyu Wang, Dingwen Li, Chenxu Luo, Cihang Xie, Xiaodong Yang
- **🏷️ 机构**: QCraft, UC Santa Cruz
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D perception based on the representations learned from multi-camera bird's-eye-view (BEV) is trending as cameras are cost-effective for mass production in autonomous driving industry. However, there exists a distinct performance gap between multi-camera BEV and LiDAR based 3D object detection. One key reason is that LiDAR captures accurate depth and other geometry measurements, while it is notoriously challenging to infer such 3D information from merely image input. In this work, we propose to boost the representation learning of a multi-camera BEV based student detector by training it to imitate the features of a well-trained LiDAR based teacher detector. We propose effective balancing strategy to enforce the student to focus on learning the crucial features from the teacher, and generalize knowledge transfer to multi-scale layers with temporal fusion. We conduct extensive evaluations on multiple representative models of multi-camera BEV. Experiments reveal that our approach renders significant improvement over the student models, leading to the state-of-the-art performance on the popular benchmark nuScenes.

</details>

### Tensor Factorization for Leveraging Cross-Modal Knowledge in Data-Constrained Infrared Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00099) · 📚 被引 1
- **作者**: Manish Sharma, Moitreya Chatterjee, Kuan-Chuan Peng, Suhas Lohit, Michael J. Jones
- **🏷️ 机构**: Rochester Institute of Technology,NY,USA,14623, Mitsubishi Electric Research Laboratories,Cambridge,MA,USA,02139
- **会议**: ICCV 2023

### UniSeg: A Unified Multi-Modal LiDAR Segmentation Network and the OpenPCSeg Codebase.
- **链接**: [arXiv:2309.05573](https://arxiv.org/abs/2309.05573) · 📚 被引 80
- **作者**: Youquan Liu, Runnan Chen, Xin Li, Lingdong Kong, Yuchen Yang, Zhaoyang Xia et al.
- **🏷️ 机构**: Shanghai AI Laboratory, The Chinese University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point-, voxel-, and range-views are three representative forms of point clouds. All of them have accurate 3D measurements but lack color and texture information. RGB images are a natural complement to these point cloud views and fully utilizing the comprehensive information of them benefits more robust perceptions. In this paper, we present a unified multi-modal LiDAR segmentation network, termed UniSeg, which leverages the information of RGB images and three views of the point cloud, and accomplishes semantic segmentation and panoptic segmentation simultaneously. Specifically, we first design the Learnable cross-Modal Association (LMA) module to automatically fuse voxel-view and range-view features with image features, which fully utilize the rich semantic information of images and are robust to calibration errors. Then, the enhanced voxel-view and range-view features are transformed to the point space,where three views of point cloud features are further fused adaptively by the Learnable cross-View Association module (LVA). Notably, UniSeg achieves promising results in three public benchmarks, i.e., SemanticKITTI, nuScenes, and Waymo Open Dataset (WOD); it ranks 1st on two challenges of two benchmarks, including the LiDAR semantic segmentation challenge of nuScenes and panoptic segmentation challenges of SemanticKITTI. Besides, we construct the OpenPCSeg codebase, which is the largest and most comprehensive outdoor LiDAR segmentation codebase. It contains most of the popular outdoor LiDAR segmentation algorithms and provides reproducible implementations. The OpenPCSeg codebase will be made publicly available at https://github.com/PJLab-ADG/PCSeg.

</details>

### Self-supervised Cross-view Representation Reconstruction for Change Captioning.
- **链接**: [arXiv:2309.16283](https://arxiv.org/abs/2309.16283) · 📚 被引 33
- **作者**: Yunbin Tu, Liang Li, Li Su, Zheng-Jun Zha, Chenggang Yan, Qingming Huang
- **🏷️ 机构**: University of Chinese Academy of Sciences,Beijing,China, ICT, CAS,Key Lab of Intelligent Information Processing,Beijing,China, University of Science and Technology of China,Hefei,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Change captioning aims to describe the difference between a pair of similar images. Its key challenge is how to learn a stable difference representation under pseudo changes caused by viewpoint change. In this paper, we address this by proposing a self-supervised cross-view representation reconstruction (SCORER) network. Concretely, we first design a multi-head token-wise matching to model relationships between cross-view features from similar/dissimilar images. Then, by maximizing cross-view contrastive alignment of two similar images, SCORER learns two view-invariant image representations in a self-supervised way. Based on these, we reconstruct the representations of unchanged objects by cross-attention, thus learning a stable difference representation for caption generation. Further, we devise a cross-modal backward reasoning to improve the quality of caption. This module reversely models a ``hallucination'' representation with the caption and ``before'' representation. By pushing it closer to the ``after'' representation, we enforce the caption to be informative about the difference in a self-supervised manner. Extensive experiments show our method achieves the state-of-the-art results on four datasets. The code is available at https://github.com/tuyunbin/SCORER.

</details>

### Multimodal Contrastive Learning and Tabular Attention for Automated Alzheimer's Disease Prediction.
- **链接**: [arXiv:2308.15469](https://arxiv.org/abs/2308.15469) · 📚 被引 23
- **作者**: Weichen Huang
- **🏷️ 机构**: St Andrew&#x2019;s College,Dublin,Ireland
- **会议**: ICCV 2023

### Lecture Presentations Multimodal Dataset: Towards Understanding Multimodality in Educational Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01838) · 📚 被引 22
- **作者**: Dong Won Lee, Chaitanya Ahuja, Paul Pu Liang, Sanika Natu, Louis-Philippe Morency
- **🏷️ 机构**: MIT, Carnegie Mellon University
- **会议**: ICCV 2023

### Cross-Modal Learning with 3D Deformable Attention for Action Recognition.
- **链接**: [arXiv:2212.05638](https://arxiv.org/abs/2212.05638) · 📚 被引 41
- **作者**: Sangwon Kim, Dasom Ahn, ByoungChul Ko
- **🏷️ 机构**: Keimyung University
- **会议**: ICCV 2023

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
- **链接**: [arXiv:2308.11185](https://arxiv.org/abs/2308.11185) · 📚 被引 4
- **作者**: Najmeh Sadoughi, Xinyu Li, Avijit Vajpayee, David Fan, Bing Shuai, Hector J. Santos-Villalobos et al.
- **🏷️ 机构**: Amazon Prime Video, AWS AI Labs
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous research has studied the task of segmenting cinematic videos into scenes and into narrative acts. However, these studies have overlooked the essential task of multimodal alignment and fusion for effectively and efficiently processing long-form videos (>60min). In this paper, we introduce Multimodal alignmEnt aGgregation and distillAtion (MEGA) for cinematic long-video segmentation. MEGA tackles the challenge by leveraging multiple media modalities. The method coarsely aligns inputs of variable lengths and different modalities with alignment positional encoding. To maintain temporal synchronization while reducing computation, we further introduce an enhanced bottleneck fusion layer which uses temporal alignment. Additionally, MEGA employs a novel contrastive loss to synchronize and transfer labels across modalities, enabling act segmentation from labeled synopsis sentences on video shots. Our experimental results show that MEGA outperforms state-of-the-art methods on MovieNet dataset for scene segmentation (with an Average Precision improvement of +1.19%) and on TRIPOD dataset for act segmentation (with a Total Agreement improvement of +5.51%)

</details>

### Dense 2D-3D Indoor Prediction with Sound via Aligned Cross-Modal Distillation.
- **链接**: [arXiv:2309.11081](https://arxiv.org/abs/2309.11081) · 📚 被引 6
- **作者**: Heeseung Yun, Joonil Na, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sound can convey significant information for spatial reasoning in our daily lives. To endow deep networks with such ability, we address the challenge of dense indoor prediction with sound in both 2D and 3D via cross-modal knowledge distillation. In this work, we propose a Spatial Alignment via Matching (SAM) distillation framework that elicits local correspondence between the two modalities in vision-to-audio knowledge transfer. SAM integrates audio features with visually coherent learnable spatial embeddings to resolve inconsistencies in multiple layers of a student model. Our approach does not rely on a specific input representation, allowing for flexibility in the input shapes or dimensions without performance degradation. With a newly curated benchmark named Dense Auditory Prediction of Surroundings (DAPS), we are the first to tackle dense indoor prediction of omnidirectional surroundings in both 2D and 3D with audio observations. Specifically, for audio-based depth estimation, semantic segmentation, and challenging 3D scene reconstruction, the proposed distillation framework consistently achieves state-of-the-art performance across various metrics and backbone architectures.

</details>

### BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=-2zfgNS917)
- **作者**: Zehui Chen, Zhenyu Li, Shiquan Zhang, Liangji Fang, Qinhong Jiang, Feng Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Multi-Modal Classifiers for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://proceedings.mlr.press/v202/kaul23a.html)
- **作者**: Prannay Kaul, Weidi Xie, Andrew Zisserman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Data Poisoning Attacks Against Multimodal Encoders.
- **链接**: [出版页](https://proceedings.mlr.press/v202/yang23f.html)
- **作者**: Ziqing Yang, Xinlei He, Zheng Li, Michael Backes, Mathias Humbert, Pascal Berrang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### PaLM-E: An Embodied Multimodal Language Model.
- **链接**: [出版页](https://proceedings.mlr.press/v202/driess23a.html)
- **作者**: Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Reparameterized Policy Learning for Multimodal Trajectory Optimization.
- **链接**: [出版页](https://proceedings.mlr.press/v202/huang23k.html)
- **作者**: Zhiao Huang, Litian Liang, Zhan Ling, Xuanlin Li, Chuang Gan, Hao Su
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### VIMA: Robot Manipulation with Multimodal Prompts.
- **链接**: [出版页](https://proceedings.mlr.press/v202/jiang23b.html)
- **作者**: Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### MEWL: Few-shot multimodal word learning with referential uncertainty.
- **链接**: [出版页](https://proceedings.mlr.press/v202/jiang23i.html)
- **作者**: Guangyuan Jiang, Manjie Xu, Shiji Xin, Wei Liang, Yujia Peng, Chi Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Calibrating Multimodal Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/ma23i.html)
- **作者**: Huan Ma, Qingyang Zhang, Changqing Zhang, Bingzhe Wu, Huazhu Fu, Joey Tianyi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Robustness in Multimodal Learning under Train-Test Modality Mismatch.
- **链接**: [出版页](https://proceedings.mlr.press/v202/mckinzie23a.html)
- **作者**: Brandon McKinzie, Vaishaal Shankar, Joseph Yitan Cheng, Yinfei Yang, Jonathon Shlens, Alexander T. Toshev
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### π-Tuning: Transferring Multimodal Foundation Models with Optimal Multi-task Interpolation.
- **链接**: [出版页](https://proceedings.mlr.press/v202/wu23t.html)
- **作者**: Chengyue Wu, Teng Wang, Yixiao Ge, Zeyu Lu, Ruisong Zhou, Ying Shan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Retrieval-Augmented Multimodal Language Modeling.
- **链接**: [出版页](https://proceedings.mlr.press/v202/yasunaga23a.html)
- **作者**: Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Richard James, Jure Leskovec, Percy Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Provable Dynamic Fusion for Low-Quality Multimodal Data.
- **链接**: [出版页](https://proceedings.mlr.press/v202/zhang23ar.html)
- **作者**: Qingyang Zhang, Haitao Wu, Changqing Zhang, Qinghua Hu, Huazhu Fu, Joey Tianyi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### On the Generalization of Multi-modal Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/zhang23an.html)
- **作者**: Qi Zhang, Yifei Wang, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICML 2023

### Multi-modal Queried Object Detection in the Wild.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/0e3af444e7d82d29871804de476d1fbe-Abstract-Conference.html)
- **作者**: Yifan Xu, Mengdan Zhang, Chaoyou Fu, Peixian Chen, Xiaoshan Yang, Ke Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Virtual Sparse Convolution for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [bev](../bev/Guideline%202023.md)
- CLIP2: Contrastive Language-Image-Point Pretraining from Real-World Point Cloud Data. → [vlm](../vlm/Guideline%202023.md)
- Q: How to Specialize Large Vision-Language Models to Data-Scarce VQA Tasks? A: Self-Train on Unlabeled Images! → [vlm](../vlm/Guideline%202023.md)
- FAME-ViL: Multi-Tasking Vision-Language Model for Heterogeneous Fashion Tasks. → [vlm](../vlm/Guideline%202023.md)
- VILA: Learning Image Aesthetics from User Comments with Vision-Language Pretraining. → [vlm](../vlm/Guideline%202023.md)
- CrowdCLIP: Unsupervised Crowd Counting via Vision-Language Model. → [vlm](../vlm/Guideline%202023.md)
- Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models. → [vlm](../vlm/Guideline%202023.md)
- Self-Supervised Learning for Multimodal Non-Rigid 3D Shape Matching. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Best of Both Worlds: Multimodal Contrastive Learning with Tabular and Imaging Data. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Vita-CLIP: Video and text adaptive CLIP via Multimodal Prompting. → [vlm](../vlm/Guideline%202023.md)
- Vision Transformers are Parameter-Efficient Audio-Visual Learners. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Class Prototypes based Contrastive Learning for Classifying Multi-Label and Fine-Grained Educational Videos. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- ObjectFusion: Multi-modal 3D Object Detection with Object-Centric Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- FocalFormer3D : Focusing on Hard Instance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- GraphAlign: Enhancing Accurate Feature Alignment by Graph matching for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- PointDC: Unsupervised Semantic Segmentation of 3D Point Clouds via Cross-modal Distillation and Super-Voxel Clustering. → [3d-detection](../3d-detection/Guideline%202023.md)
- BEV-DG: Cross-Modal Learning under Bird's-Eye View for Domain Generalization of 3D Semantic Segmentation. → [bev](../bev/Guideline%202023.md)
- AIDE: A Vision-Driven Multi-View, Multi-Modal, Multi-Tasking Dataset for Assistive Driving Perception. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Replay: Multi-modal Multi-view Acted Videos for Casual Holography. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- CLIP-FO3D: Learning Free Open-world 3D Scene Representations from 2D Dense CLIP. → [vlm](../vlm/Guideline%202023.md)
- Zenseact Open Dataset: A large-scale and diverse multimodal dataset for autonomous driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Unsupervised 3D Perception with 2D Vision-Language Distillation for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Hidden Biases of End-to-End Driving Models. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- SelfGraphVQA: A Self-Supervised Graph Neural Network for Scene-based Question Answering. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning. → [vlm](../vlm/Guideline%202023.md)
- Verbs in Action: Improving verb understanding in video-language models. → [video-understanding](../video-understanding/Guideline%202023.md)
- Video Action Recognition with Attentive Semantic Units. → [video-understanding](../video-understanding/Guideline%202023.md)
- Multimodal Distillation for Egocentric Action Recognition. → [video-understanding](../video-understanding/Guideline%202023.md)
- Class-Incremental Grouping Network for Continual Audio-Visual Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- Audio-Visual Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- Multimodal Parameter-Efficient Few-Shot Class Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- InstaTune: Instantaneous Neural Architecture Search During Fine-Tuning. → [neural-architecture-search](../neural-architecture-search/Guideline%202023.md)
- TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance. → [vlm](../vlm/Guideline%202023.md)
- CoDA: Collaborative Novel Box Discovery and Cross-modal Alignment for Open-vocabulary 3D Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Leveraging Vision-Centric Multi-Modal Expertise for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Unleash the Potential of Image Branch for Cross-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)

<!-- COMPLETE v1 papers=64 -->
