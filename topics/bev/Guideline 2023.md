# BEV — 2023 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Parametric Depth Based Feature Representation Learning for Object Detection and Segmentation in Bird's-Eye View.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00779) · 📚 被引 7
- **作者**: Jiayu Yang, Enze Xie, Miaomiao Liu, José M. Álvarez
- **🏷️ 机构**: Australian National University, The University of Hong Kong, NVIDIA
- **会议**: ICCV 2023

### BEVPlace: Learning LiDAR-based Place Recognition using Bird's Eye View Images.
- **链接**: [arXiv:2302.14325](https://arxiv.org/abs/2302.14325) · [代码](https://github.com/zjuluolun/BEVPlace) · 📚 被引 88
- **作者**: Lun Luo, Shuhang Zheng, Yixuan Li, Yongzhi Fan, Beinan Yu, Si-Yuan Cao et al.
- **🏷️ 机构**: Zhejiang University,Ningbo Innovation Center, Zhejiang University,College of Information Science and Electronic Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Place recognition is a key module for long-term SLAM systems. Current LiDAR-based place recognition methods usually use representations of point clouds such as unordered points or range images. These methods achieve high recall rates of retrieval, but their performance may degrade in the case of view variation or scene changes. In this work, we explore the potential of a different representation in place recognition, i.e. bird's eye view (BEV) images. We observe that the structural contents of BEV images are less influenced by rotations and translations of point clouds. We validate that, without any delicate design, a simple VGGNet trained on BEV images achieves comparable performance with the state-of-the-art place recognition methods in scenes of slight viewpoint changes. For more robust place recognition, we design a rotation-invariant network called BEVPlace. We use group convolution to extract rotation-equivariant local features from the images and NetVLAD for global feature aggregation. In addition, we observe that the distance between BEV features is correlated with the geometry distance of point clouds. Based on the observation, we develop a method to estimate the position of the query cloud, extending the usage of place recognition. The experiments conducted on large-scale public datasets show that our method 1) achieves state-of-the-art performance in terms of recall rates, 2) is robust to view changes, 3) shows strong generalization ability, and 4) can estimate the positions of query point clouds. Source codes are publicly available at https://github.com/zjuluolun/BEVPlace.

</details>

### BAEFormer: Bi-Directional and Early Interaction Transformers for Bird's Eye View Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00925) · 📚 被引 31
- **作者**: Cong Pan, Yonghao He, Junran Peng, Qian Zhang, Wei Sui, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,National Laboratory of Pattern Recognition, Horizon Robotics, Huawei Inc.
- **会议**: CVPR 2023

### BEV@DC: Bird's-Eye View Assisted Training for Depth Completion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00891) · 📚 被引 37
- **作者**: Wending Zhou, Xu Yan, Yinghong Liao, Yuankai Lin, Jin Huang, Gangming Zhao et al.
- **🏷️ 机构**: FNii, CUHK-Shenzhen, Huazhong University of Science and Technology, Cardiff University
- **会议**: CVPR 2023

### BEV-Guided Multi-Modality Fusion for Driving Perception.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02103) · 📚 被引 59
- **作者**: Yunze Man, Liang-Yan Gui, Yu-Xiong Wang
- **🏷️ 机构**: UIUC
- **会议**: CVPR 2023

### BEV-LaneDet: An Efficient 3D Lane Detection Based on Virtual Camera via Key-Points.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00103) · 📚 被引 70
- **作者**: Ruihao Wang, Jian Qin, Kaiying Li, Yaochen Li, Dong Cao, Jintao Xu
- **🏷️ 机构**: HAOMO.AI Technology Co., Ltd., Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2023

### FB-BEV: BEV Representation from Forward-Backward View Transformations.
- **链接**: [arXiv:2308.02236](https://arxiv.org/abs/2308.02236) · [代码](https://github.com/NVlabs/FB-BEV) · 📚 被引 139
- **作者**: Zhiqi Li, Zhiding Yu, Wenhai Wang, Anima Anandkumar, Tong Lu, José M. Álvarez
- **🏷️ 机构**: Nanjing University,National Key Lab for Novel Software Technology, NVIDIA, The Chinese University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> View Transformation Module (VTM), where transformations happen between multi-view image features and Bird-Eye-View (BEV) representation, is a crucial step in camera-based BEV perception systems. Currently, the two most prominent VTM paradigms are forward projection and backward projection. Forward projection, represented by Lift-Splat-Shoot, leads to sparsely projected BEV features without post-processing. Backward projection, with BEVFormer being an example, tends to generate false-positive BEV features from incorrect projections due to the lack of utilization on depth. To address the above limitations, we propose a novel forward-backward view transformation module. Our approach compensates for the deficiencies in both existing methods, allowing them to enhance each other to obtain higher quality BEV representations mutually. We instantiate the proposed module with FB-BEV, which achieves a new state-of-the-art result of 62.4% NDS on the nuScenes test set. Code and models are available at https://github.com/NVlabs/FB-BEV.

</details>

### MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception.
- **链接**: [arXiv:2211.10593](https://arxiv.org/abs/2211.10593) · 📚 被引 46
- **作者**: Hongyu Zhou, Zheng Ge, Zeming Li, Xiangyu Zhang
- **🏷️ 机构**: MEGVII Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes an efficient multi-camera to Bird's-Eye-View (BEV) view transformation method for 3D perception, dubbed MatrixVT. Existing view transformers either suffer from poor transformation efficiency or rely on device-specific operators, hindering the broad application of BEV models. In contrast, our method generates BEV features efficiently with only convolutions and matrix multiplications (MatMul). Specifically, we propose describing the BEV feature as the MatMul of image feature and a sparse Feature Transporting Matrix (FTM). A Prime Extraction module is then introduced to compress the dimension of image features and reduce FTM's sparsity. Moreover, we propose the Ring \& Ray Decomposition to replace the FTM with two matrices and reformulate our pipeline to reduce calculation further. Compared to existing methods, MatrixVT enjoys a faster speed and less memory footprint while remaining deploy-friendly. Extensive experiments on the nuScenes benchmark demonstrate that our method is highly efficient but obtains results on par with the SOTA method in object detection and map segmentation tasks

</details>

## 跨领域论文（完整笔记在其他领域）

- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [3d-detection](../3d-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [3d-detection](../3d-detection/Guideline%202023.md)

## 🆕 增量新增

### BEVFormer v2: Adapting Modern Image Backbones to Bird's-Eye-View Recognition via Perspective Supervision. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2211.10439](https://arxiv.org/abs/2211.10439) · 📚 被引 320
- **作者**: Chenyu Yang, Yuntao Chen, Hao Tian, Chenxin Tao, Xizhou Zhu, Zhaoxiang Zhang et al.
- **🏷️ 机构**: Tsinghua University, Centre for Artificial Intelligence and Robotics, HKISI&#x005F;CAS, Sense Time Research
- **会议**: CVPR 2023
- **摘要（中）**: 针对现有BEV检测器与新兴图像骨干网络（如ViT）结合时优化困难、收敛慢的问题，提出BEVFormer v2，通过引入透视空间监督来缓解优化难度。方法采用两阶段检测器，先由透视头生成提议，再送入BEV头进行最终预测。相比已有工作，该方法不依赖特定深度预训练骨干，能适配多种现代骨干网络，并在nuScenes上取得新的SoTA结果。
- **摘要（英）**: To address the optimization difficulty and slow convergence when integrating modern image backbones with BEV detectors, we propose BEVFormer v2 with perspective supervision. It uses a two-stage design where proposals from a perspective head are fed into the BEV head, enabling compatibility with various backbones and achieving new state-of-the-art on nuScenes.
- **核心贡献**: 提出透视监督的两阶段BEV检测框架，提升与现代骨干的兼容性。
- **创新点**: 引入透视空间监督以简化BEV检测器的优化。
- **结果**: 在nuScenes上取得新的SoTA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel bird's-eye-view (BEV) detector with perspective supervision, which converges faster and better suits modern image backbones. Existing state-of-the-art BEV detectors are often tied to certain depth pre-trained backbones like VoVNet, hindering the synergy between booming image backbones and BEV detectors. To address this limitation, we prioritize easing the optimization of BEV detectors by introducing perspective space supervision. To this end, we propose a two-stage BEV detector, where proposals from the perspective head are fed into the bird's-eye-view head for final predictions. To evaluate the effectiveness of our model, we conduct extensive ablation studies focusing on the form of supervision and the generality of the proposed detector. The proposed method is verified with a wide spectrum of traditional and modern image backbones and achieves new SoTA results on the large-scale nuScenes dataset. The code shall be released soon.

</details>

### Surround-View Vision-based 3D Detection for Autonomous Driving: A Survey. **⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00348) · 📚 被引 24
- **作者**: Apoorv Singh
- **🏷️ 机构**: Motional Carnegie Mellon University
- **会议**: ICCV 2023
- **摘要（中）**: 针对环视视觉3D检测在自动驾驶中的快速发展，该综述系统梳理了相关方法、数据集和评估指标。方法上，对现有基于相机的3D检测方法进行分类，涵盖单目、双目和多相机方法，并讨论了BEV表示、时序融合等关键技术。相比已有综述，该工作聚焦于环视视觉这一特定方向，提供了更全面的技术总结和未来方向展望。摘要未提供具体数据，但综述性论文为研究者提供了系统参考。
- **摘要（英）**: This survey addresses the rapid progress in surround-view vision-based 3D detection for autonomous driving. It systematically categorizes existing methods, datasets, and evaluation metrics, focusing on camera-based approaches with BEV representations and temporal fusion. It provides a comprehensive reference for researchers, though specific quantitative results are not included.
- **核心贡献**: 系统综述了环视视觉3D检测的方法、数据集和评估指标。
- **创新点**: 聚焦环视视觉方向，提供分类和未来展望。
- **结果**: 提供了全面的技术总结，但无具体实验数据。

### UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2303.15083](https://arxiv.org/abs/2303.15083) · 📚 被引 69
- **作者**: Shengchao Zhou, Weizhou Liu, Chen Hu, Shuchang Zhou, Chao Ma
- **🏷️ 机构**: MEGVII Technology, AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence
- **会议**: CVPR 2023
- **摘要（中）**: ①针对自动驾驶中多模态传感器系统复杂但单模态检测精度较低的问题，旨在通过知识蒸馏提升单模态检测器性能。②提出了UniDistill框架，在训练时将教师和学生检测器的特征投影到BEV空间，计算三种蒸馏损失以稀疏对齐前景特征，支持LiDAR-to-camera、camera-to-LiDAR、fusion-to-LiDAR和fusion-to-camera等多种蒸馏路径。③利用不同检测器在BEV中的相似检测范式，实现了跨模态通用蒸馏，且推理时无额外成本。④三种蒸馏损失能过滤背景信息错位影响，并平衡不同大小物体，显著提升了单模态检测器的精度。
- **摘要（英）**: This paper addresses the trade-off between complex multi-modal systems and lower-accuracy single-modal detectors in autonomous driving by proposing UniDistill, a universal cross-modality knowledge distillation framework. It projects teacher and student features into BEV space and applies three distillation losses for sparse foreground alignment, supporting multiple distillation paths like LiDAR-to-camera and fusion-to-LiDAR. The method improves single-modal detector accuracy without inference overhead, effectively filtering background misalignment and balancing object size variations.
- **核心贡献**: 提出了UniDistill，一个支持多种跨模态蒸馏路径的BEV空间知识蒸馏框架，显著提升单模态3D检测性能。
- **创新点**: 在BEV空间统一特征表示，并通过稀疏前景对齐损失实现跨模态高效蒸馏。
- **结果**: 在多种蒸馏路径下均显著提升了单模态检测器的精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the field of 3D object detection for autonomous driving, the sensor portfolio including multi-modality and single-modality is diverse and complex. Since the multi-modal methods have system complexity while the accuracy of single-modal ones is relatively low, how to make a tradeoff between them is difficult. In this work, we propose a universal cross-modality knowledge distillation framework (UniDistill) to improve the performance of single-modality detectors. Specifically, during training, UniDistill projects the features of both the teacher and the student detector into Bird's-Eye-View (BEV), which is a friendly representation for different modalities. Then, three distillation losses are calculated to sparsely align the foreground features, helping the student learn from the teacher without introducing additional cost during inference. Taking advantage of the similar detection paradigm of different detectors in BEV, UniDistill easily supports LiDAR-to-camera, camera-to-LiDAR, fusion-to-LiDAR and fusion-to-camera distillation paths. Furthermore, the three distillation losses can filter the effect of misaligned background information and balance between objects of different sizes, improving the distillation effectiveness. Extensive experiments on nuScenes demonstrate that UniDistill effectively improves the mAP and NDS of student detectors by 2.0%~3.2%.

</details>

### Predict to Detect: Prediction-guided 3D Object Detection using Sequential Images. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2306.08528](https://arxiv.org/abs/2306.08528) · 📚 被引 13
- **作者**: Sanmin Kim, Youngseok Kim, In-Jae Lee, Dongsuk Kum
- **🏷️ 机构**: KAIST
- **会议**: ICCV 2023
- **摘要（中）**: ①针对基于序列图像的3D检测中运动信息利用不足的问题。②提出P2D模型，通过预测当前帧信息来显式提取时序运动特征，并基于预测结果进行BEV特征聚合。③相比简单拼接或静态立体，更充分利用运动线索。④实验显示相比序列基线，mAP和NDS分别提升3.0%和3.7%。
- **摘要（英）**: This paper addresses insufficient motion cue exploitation in sequential image-based 3D detection. It proposes P2D, which predicts current frame info from past frames to extract motion features and aggregates BEV features attentively. The method improves mAP by 3.0% and NDS by 3.7% over baselines.
- **核心贡献**: 提出预测引导的时序特征聚合方法用于3D检测。
- **创新点**: 利用预测模块显式建模运动特征。
- **结果**: mAP和NDS分别提升3.0%和3.7%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent camera-based 3D object detection methods have introduced sequential frames to improve the detection performance hoping that multiple frames would mitigate the large depth estimation error. Despite improved detection performance, prior works rely on naive fusion methods (e.g., concatenation) or are limited to static scenes (e.g., temporal stereo), neglecting the importance of the motion cue of objects. These approaches do not fully exploit the potential of sequential images and show limited performance improvements. To address this limitation, we propose a novel 3D object detection model, P2D (Predict to Detect), that integrates a prediction scheme into a detection framework to explicitly extract and leverage motion features. P2D predicts object information in the current frame using solely past frames to learn temporal motion features. We then introduce a novel temporal feature aggregation method that attentively exploits Bird's-Eye-View (BEV) features based on predicted object information, resulting in accurate 3D object detection. Experimental results demonstrate that P2D improves mAP and NDS by 3.0% and 3.7% compared to the sequential image-based baseline, illustrating that incorporating a prediction scheme can significantly improve detection accuracy.

</details>

### GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2308.08140](https://arxiv.org/abs/2308.08140) · 📚 被引 14
- **作者**: Ziyu Li, Jingming Guo, Tongtong Cao, Bingbing Liu, Wankou Yang
- **🏷️ 机构**: School of Automation, Southeast University, Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2023
- **摘要（中）**: ①针对LiDAR-based 3D检测器在跨域场景下因域差距导致的性能下降问题。②提出GPA-3D框架，利用点云物体的几何结构分配可学习的原型，对齐源域和目标域的BEV特征，减少特征分布差异。③相比现有方法，显式利用几何关系进行原型对齐，而非仅依赖特征统计匹配。④在Waymo、nuScenes和KITTI等基准上验证了有效性，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the domain gap issue in LiDAR-based 3D detection by proposing GPA-3D, which assigns learnable geometry-aware prototypes to align BEV features across domains. It explicitly leverages geometric structures to reduce feature distribution discrepancy, improving cross-domain generalization. Evaluations on Waymo, nuScenes, and KITTI demonstrate its effectiveness, though specific metrics are not provided in the abstract.
- **核心贡献**: 提出几何感知原型对齐框架，显式利用点云几何结构减少跨域特征差异。
- **创新点**: 将可学习原型与点云几何结构绑定，实现源域和目标域BEV特征的细粒度对齐。
- **结果**: 在多个基准上验证了跨域检测性能的提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D detection has made great progress in recent years. However, the performance of 3D detectors is considerably limited when deployed in unseen environments, owing to the severe domain gap problem. Existing domain adaptive 3D detection methods do not adequately consider the problem of the distributional discrepancy in feature space, thereby hindering generalization of detectors across domains. In this work, we propose a novel unsupervised domain adaptive \textbf{3D} detection framework, namely \textbf{G}eometry-aware \textbf{P}rototype \textbf{A}lignment (\textbf{GPA-3D}), which explicitly leverages the intrinsic geometric relationship from point cloud objects to reduce the feature discrepancy, thus facilitating cross-domain transferring. Specifically, GPA-3D assigns a series of tailored and learnable prototypes to point cloud objects with distinct geometric structures. Each prototype aligns BEV (bird's-eye-view) features derived from corresponding point cloud objects on source and target domains, reducing the distributional discrepancy and achieving better adaptation. The evaluation results obtained on various benchmarks, including Waymo, nuScenes and KITTI, demonstrate the superiority of our GPA-3D over the state-of-the-art approaches for different adaptation scenarios. The MindSpore version code will be publicly available at \url{https://github.com/Liz66666/GPA3D}.

</details>

### SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2308.09244](https://arxiv.org/abs/2308.09244) · 📚 被引 151
- **作者**: Haisong Liu, Yao Teng, Tao Lu, Haiguang Wang, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology
- **会议**: ICCV 2023
- **摘要（中）**: ①针对基于相机的3D检测中，稀疏检测器性能不如稠密检测器的问题。②提出SparseBEV，一种全稀疏3D检测器，包含尺度自适应自注意力、自适应时空采样和自适应混合三个关键设计。③相比现有稀疏方法，通过增强BEV和图像空间的适应性，缩小了与稠密方法的性能差距。④在nuScenes测试集上达到67.5 NDS，实现了最先进性能。
- **摘要（英）**: This paper tackles the performance gap between sparse and dense camera-based 3D detectors by proposing SparseBEV, a fully sparse detector with scale-adaptive self-attention, adaptive spatio-temporal sampling, and adaptive mixing. These designs enhance adaptability in both BEV and image spaces, achieving state-of-the-art 67.5 NDS on nuScenes test split.
- **核心贡献**: 提出全稀疏3D检测器SparseBEV，通过自适应特征聚合和采样达到最先进性能。
- **创新点**: 在稀疏检测中引入尺度自适应和查询引导的时空采样，提升特征适应性。
- **结果**: 在nuScenes上以67.5 NDS超越稠密检测器。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-based 3D object detection in BEV (Bird's Eye View) space has drawn great attention over the past few years. Dense detectors typically follow a two-stage pipeline by first constructing a dense BEV feature and then performing object detection in BEV space, which suffers from complex view transformations and high computation cost. On the other side, sparse detectors follow a query-based paradigm without explicit dense BEV feature construction, but achieve worse performance than the dense counterparts. In this paper, we find that the key to mitigate this performance gap is the adaptability of the detector in both BEV and image space. To achieve this goal, we propose SparseBEV, a fully sparse 3D object detector that outperforms the dense counterparts. SparseBEV contains three key designs, which are (1) scale-adaptive self attention to aggregate features with adaptive receptive field in BEV space, (2) adaptive spatio-temporal sampling to generate sampling locations under the guidance of queries, and (3) adaptive mixing to decode the sampled features with dynamic weights from the queries. On the test split of nuScenes, SparseBEV achieves the state-of-the-art performance of 67.5 NDS. On the val split, SparseBEV achieves 55.8 NDS while maintaining a real-time inference speed of 23.5 FPS. Code is available at https://github.com/MCG-NJU/SparseBEV.

</details>

### Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection. **⭐⭐⭐⭐** (相关度: 82%)
- **链接**: [arXiv:2307.08209](https://arxiv.org/abs/2307.08209) · 📚 被引 29
- **作者**: Tianchen Zhao, Xuefei Ning, Ke Hong, Zhongyuan Qiu, Pu Lu, Yali Zhao et al.
- **🏷️ 机构**: Tsinghua University, Novauto, Meituan
- **会议**: ICCV 2023
- **摘要（中）**: ①针对体素法3D检测在资源受限车辆上计算和内存开销大的问题。②提出Ada3D自适应推理框架，利用轻量级重要性预测器过滤冗余输入，并引入稀疏保持批归一化利用BEV特征稀疏性。③相比现有方法，从输入层面减少空间冗余，而非仅优化模型结构。④实现40%体素减少和BEV密度从100%降至20%而不损失精度，计算和内存成本降低5倍，GPU延迟优化1.52倍/1.45倍。
- **摘要（英）**: This paper addresses the high computational and memory costs of voxel-based 3D detection by proposing Ada3D, an adaptive inference framework that filters redundant inputs via a lightweight importance predictor and exploits BEV sparsity with Sparsity Preserving Batch Normalization. It reduces voxels by 40% and BEV density to 20% without accuracy loss, achieving 5x cost reduction and 1.52x/1.45x latency improvement.
- **核心贡献**: 提出自适应推理框架，利用输入稀疏性显著降低3D检测的计算和内存开销。
- **创新点**: 结合重要性预测和稀疏保持批归一化，实现输入级冗余过滤。
- **结果**: 在保持精度的同时，实现5倍计算和内存成本降低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Voxel-based methods have achieved state-of-the-art performance for 3D object detection in autonomous driving. However, their significant computational and memory costs pose a challenge for their application to resource-constrained vehicles. One reason for this high resource consumption is the presence of a large number of redundant background points in Lidar point clouds, resulting in spatial redundancy in both 3D voxel and dense BEV map representations. To address this issue, we propose an adaptive inference framework called Ada3D, which focuses on exploiting the input-level spatial redundancy. Ada3D adaptively filters the redundant input, guided by a lightweight importance predictor and the unique properties of the Lidar point cloud. Additionally, we utilize the BEV features' intrinsic sparsity by introducing the Sparsity Preserving Batch Normalization. With Ada3D, we achieve 40% reduction for 3D voxels and decrease the density of 2D BEV feature maps from 100% to 20% without sacrificing accuracy. Ada3D reduces the model computational and memory cost by 5x, and achieves 1.52x/1.45x end-to-end GPU latency and 1.5x/4.5x GPU peak memory optimization for the 3D and 2D backbone respectively.

</details>

### Towards Viewpoint Robustness in Bird's Eye View Segmentation. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2309.05192](https://arxiv.org/abs/2309.05192) · 📚 被引 17
- **作者**: Tzofi Klinghoffer, Jonah Philion, Wenzheng Chen, Or Litany, Zan Gojcic, Jungseock Joo et al.
- **🏷️ 机构**: MIT, NVIDIA
- **会议**: ICCV 2023
- **摘要（中）**: 针对自动驾驶中相机视点变化导致BEV分割性能大幅下降的问题，本文系统研究了视点变化的影响，并提出一种新颖的视图合成技术，将采集数据转换到目标相机配置的视点，从而无需额外数据采集和标注即可训练多种车型的BEV分割模型。实验表明，现有模型对相机俯仰角、偏航角、深度和高度的微小变化非常敏感，而所提方法有效缓解了这一问题。
- **摘要（英）**: This paper investigates the sensitivity of BEV segmentation models to camera viewpoint changes and proposes a novel view synthesis technique to transform collected data to target rig viewpoints, enabling training for diverse vehicle types without additional data collection. Experiments reveal that existing models are highly sensitive to small changes in pitch, yaw, depth, or height, and the proposed method effectively mitigates this issue.
- **核心贡献**: 提出一种基于视图合成的数据增强方法，提升BEV分割模型对视点变化的鲁棒性。
- **创新点**: 利用新颖视图合成技术将数据转换到目标视点，避免重复数据采集。
- **结果**: 显著降低了视点变化带来的性能下降，支持多车型部署。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous vehicles (AV) require that neural networks used for perception be robust to different viewpoints if they are to be deployed across many types of vehicles without the repeated cost of data collection and labeling for each. AV companies typically focus on collecting data from diverse scenarios and locations, but not camera rig configurations, due to cost. As a result, only a small number of rig variations exist across most fleets. In this paper, we study how AV perception models are affected by changes in camera viewpoint and propose a way to scale them across vehicle types without repeated data collection and labeling. Using bird's eye view (BEV) segmentation as a motivating task, we find through extensive experiments that existing perception models are surprisingly sensitive to changes in camera viewpoint. When trained with data from one camera rig, small changes to pitch, yaw, depth, or height of the camera at inference time lead to large drops in performance. We introduce a technique for novel view synthesis and use it to transform collected data to the viewpoint of target rigs, allowing us to train BEV segmentation models for diverse target rigs without any additional data collection or labeling cost. To analyze the impact of viewpoint changes, we leverage synthetic data to mitigate other gaps (content, ISP, etc). Our approach is then trained on real data and evaluated on synthetic data, enabling evaluation on diverse target rigs. We release all data for use in future work. Our method is able to recover an average of 14.7% of the IoU that is otherwise lost when deploying to new rigs.

</details>

### MapPrior: Bird's-Eye View Map Layout Estimation with Generative Models. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2308.12963](https://arxiv.org/abs/2308.12963) · 📚 被引 14
- **作者**: Xiyue Zhu, Vlas Zyrianov, Zhijian Liu, Shenlong Wang
- **🏷️ 机构**: University of Illinois at Urbana-Champaign, MIT
- **会议**: ICCV 2023
- **摘要（中）**: 针对BEV感知模型生成语义地图布局不真实且无法处理部分传感器信息不确定性的问题，本文提出MapPrior框架，结合传统判别式BEV模型与生成式模型，提升预测的准确性、真实性和不确定性感知。在nuScenes基准上，MapPrior在相机和LiDAR的BEV感知任务中，显著优于最强基线，MMD和ECE分数大幅改善。
- **摘要（英）**: This paper introduces MapPrior, a BEV perception framework combining a discriminative model with a generative model for semantic map layouts, addressing issues of unrealistic layouts and uncertainty from partial sensor information. On nuScenes, MapPrior outperforms the strongest baseline with significantly improved MMD and ECE scores in both camera- and LiDAR-based BEV perception.
- **核心贡献**: 提出MapPrior，融合生成模型与判别模型，提升BEV地图布局估计的准确性和不确定性感知。
- **创新点**: 将生成式先验引入BEV感知，实现更真实和一致的布局预测。
- **结果**: 在nuScenes上大幅提升MMD和ECE指标，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite tremendous advancements in bird's-eye view (BEV) perception, existing models fall short in generating realistic and coherent semantic map layouts, and they fail to account for uncertainties arising from partial sensor information (such as occlusion or limited coverage). In this work, we introduce MapPrior, a novel BEV perception framework that combines a traditional discriminative BEV perception model with a learned generative model for semantic map layouts. Our MapPrior delivers predictions with better accuracy, realism, and uncertainty awareness. We evaluate our model on the large-scale nuScenes benchmark. At the time of submission, MapPrior outperforms the strongest competing method, with significantly improved MMD and ECE scores in camera- and LiDAR-based BEV perception.

</details>

### BEV-DG: Cross-Modal Learning under Bird's-Eye View for Domain Generalization of 3D Semantic Segmentation. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01068) · 📚 被引 19
- **作者**: Miaoyu Li, Yachao Zhang, Xu Ma, Yanyun Qu, Yun Fu
- **🏷️ 机构**: Xiamen University,School of Informatics, Tsinghua University,Tsinghua Shenzhen International Graduate School, Northeastern University,Department of ECE
- **会议**: ICCV 2023
- **摘要（中）**: 针对3D语义分割在跨域场景下泛化能力不足的问题，本文提出BEV-DG方法，利用BEV表示进行跨模态学习，以增强域泛化性能。通过融合多模态信息并利用BEV的视角不变性，提升模型在不同域间的鲁棒性。实验表明，该方法在多个域泛化基准上取得了改进。
- **摘要（英）**: This paper addresses the limited generalization of 3D semantic segmentation across domains by proposing BEV-DG, which leverages BEV representations for cross-modal learning. By fusing multimodal information and exploiting BEV's viewpoint invariance, the method enhances robustness across domains, with experiments showing improvements on multiple benchmarks.
- **核心贡献**: 提出BEV-DG，利用BEV跨模态学习提升3D语义分割的域泛化能力。
- **创新点**: 将BEV表示与跨模态学习结合，增强域不变特征提取。
- **结果**: 在多个域泛化基准上取得性能提升。

### CluB: Cluster Meets BEV for LiDAR-Based 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/7f2fc4053a66edfa430bcdf9a6ff3b17-Abstract-Conference.html)
- **作者**: Yingjie Wang, Jiajun Deng, Yuenan Hou, Yao Li, Yu Zhang, Jianmin Ji et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Asynchrony-Robust Collaborative Perception via Bird's Eye View Flow.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5a829e299ebc1c1615ddb09e98fb6ce8-Abstract-Conference.html)
- **作者**: Sizhe Wei, Yuxi Wei, Yue Hu, Yifan Lu, Yiqi Zhong, Siheng Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### HotBEV: Hardware-oriented Transformer-based Multi-View 3D Detector for BEV Perception.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/081b08068e4733ae3e7ad019fe8d172f-Abstract-Conference.html)
- **作者**: Peiyan Dong, Zhenglun Kong, Xin Meng, Pinrui Yu, Yifan Gong, Geng Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [object-detection](../object-detection/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [object-detection](../object-detection/Guideline%202023.md)
- BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [multimodal](../multimodal/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [network-pruning](../network-pruning/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Bird's-Eye-View Scene Graph for Vision-Language Navigation. → [vlm](../vlm/Guideline%202023.md)
- MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception. → [network-pruning](../network-pruning/Guideline%202023.md)
- OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction. → [network-pruning](../network-pruning/Guideline%202023.md)
- BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection. → [multimodal](../multimodal/Guideline%202023.md)
<!-- COMPLETE v1 papers=21 -->
