# Knowledge Distillation — 2022 Guideline

> 领域: 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

## 跨领域论文（完整笔记在其他领域）

- Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)

## 🆕 增量新增

### Towards Efficient 3D Object Detection with Knowledge Distillation. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2205.15156](https://arxiv.org/abs/2205.15156) · 📚 被引 10
- **作者**: Jihan Yang, Shaoshuai Shi, Runyu Ding, Zhe Wang, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
- **摘要（中）**: ①该论文针对3D目标检测中先进模型计算开销大、知识蒸馏在3D领域缺乏系统研究的问题。②首先从模型压缩和输入分辨率降低两个角度构建了六组教师-学生对，并评估了2D领域的KD方法在3D检测上的适用性；随后提出了改进的KD流程，包括基于教师分类响应的关键位置logit蒸馏和教师引导的学生模型初始化。③相比现有KD方法，该工作专门针对3D检测设计，通过权重继承和选择性蒸馏提升了知识迁移效率。④在Waymo数据集上，最佳模型达到65.75%的LEVEL 2 mAPH，超越教师模型且仅需44%的计算量。
- **摘要（英）**: This paper addresses the heavy computation of advanced 3D detectors by systematically exploring knowledge distillation for pillar- and voxel-based detectors, constructing six teacher-student pairs and proposing an enhanced KD pipeline with pivotal-position logit distillation and teacher-guided initialization. It outperforms existing KD methods on Waymo, achieving 65.75% LEVEL 2 mAPH with only 44% of the teacher's computation. The work provides practical insights for efficient 3D detection.
- **核心贡献**: 构建了3D检测KD基准并提出了改进的蒸馏方法，实现高效准确的3D目标检测。
- **创新点**: 结合关键位置logit蒸馏和权重继承初始化，提升KD在3D检测中的迁移效率。
- **结果**: 在Waymo上以44%计算量超越教师模型，达到65.75% mAPH。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite substantial progress in 3D object detection, advanced 3D detectors often suffer from heavy computation overheads. To this end, we explore the potential of knowledge distillation (KD) for developing efficient 3D object detectors, focusing on popular pillar- and voxel-based detectors.In the absence of well-developed teacher-student pairs, we first study how to obtain student models with good trade offs between accuracy and efficiency from the perspectives of model compression and input resolution reduction. Then, we build a benchmark to assess existing KD methods developed in the 2D domain for 3D object detection upon six well-constructed teacher-student pairs. Further, we propose an improved KD pipeline incorporating an enhanced logit KD method that performs KD on only a few pivotal positions determined by teacher classification response, and a teacher-guided student model initialization to facilitate transferring teacher model's feature extraction ability to students through weight inheritance. Finally, we conduct extensive experiments on the Waymo dataset. Our best performing model achieves $65.75\%$ LEVEL 2 mAPH, surpassing its teacher model and requiring only $44\%$ of teacher flops. Our most efficient model runs 51 FPS on an NVIDIA A100, which is $2.2\times$ faster than PointPillar with even higher accuracy. Code is available at \url{https://github.com/CVMI-Lab/SparseKD}.

</details>

### Let Images Give You More: Point Cloud Cross-Modal Training for Shape Analysis. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2210.04208](https://arxiv.org/abs/2210.04208)
- **作者**: Xu Yan, Heshen Zhan, Chaoda Zheng, Jiantao Gao, Ruimao Zhang, Shuguang Cui et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
- **摘要（中）**: ①该论文针对点云分析中单模态表示学习性能瓶颈的问题。②提出了PointCMT跨模态训练策略，利用渲染或投影的2D视图图像通过教师-学生框架进行知识蒸馏，并设计了特征和分类器增强准则以消除模态分布差异。③相比现有跨模态方法，PointCMT无需修改点云网络架构，仅通过训练阶段引入图像信息提升点云表示判别力，并避免负迁移。④在多个数据集和骨干网络上取得了显著性能提升，验证了方法的有效性。
- **摘要（英）**: This paper tackles the bottleneck of single-modality representation learning in point cloud analysis by proposing PointCMT, a cross-modal training strategy that distills knowledge from 2D view images into point cloud networks via a teacher-student framework with feature and classifier enhancement. It improves point-only representations without architecture changes and avoids negative transfer, achieving significant gains across datasets and backbones. The method is simple yet effective for 3D shape analysis.
- **核心贡献**: 提出了一种无需架构修改的点云跨模态训练方法，利用图像知识提升点云表示质量。
- **创新点**: 通过特征和分类器增强准则消除模态差异，实现有效的跨模态知识迁移。
- **结果**: 在多个点云数据集上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although recent point cloud analysis achieves impressive progress, the paradigm of representation learning from a single modality gradually meets its bottleneck. In this work, we take a step towards more discriminative 3D point cloud representation by fully taking advantages of images which inherently contain richer appearance information, e.g., texture, color, and shade. Specifically, this paper introduces a simple but effective point cloud cross-modality training (PointCMT) strategy, which utilizes view-images, i.e., rendered or projected 2D images of the 3D object, to boost point cloud analysis. In practice, to effectively acquire auxiliary knowledge from view images, we develop a teacher-student framework and formulate the cross modal learning as a knowledge distillation problem. PointCMT eliminates the distribution discrepancy between different modalities through novel feature and classifier enhancement criteria and avoids potential negative transfer effectively. Note that PointCMT effectively improves the point-only representation without architecture modification. Sufficient experiments verify significant gains on various datasets using appealing backbones, i.e., equipped with PointCMT, PointNet++ and PointMLP achieve state-of-the-art performance on two benchmarks, i.e., 94.4% and 86.7% accuracy on ModelNet40 and ScanObjectNN, respectively. Code will be made available at https://github.com/ZhanHeshen/PointCMT.

</details>

## 跨领域论文（完整笔记在其他领域）

- Label Matching Semi-Supervised Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SPIRAL: Self-supervised Perturbation-Invariant Representation Learning for Speech Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
<!-- COMPLETE v1 papers=2 -->
