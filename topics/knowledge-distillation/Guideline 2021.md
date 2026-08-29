# Knowledge Distillation — 2021 Guideline

> 领域: 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

## 跨领域论文（完整笔记在其他领域）

- Continual Learning in the Teacher-Student Setup: Impact of Task Similarity. → [continual-learning](../continual-learning/Guideline%202021.md)

## 🆕 增量新增

### EvDistill: Asynchronous Events To End-Task Learning via Bidirectional Reconstruction-Guided Cross-Modal Knowledge Distillation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2111.12341](https://arxiv.org/abs/2111.12341) · 📚 被引 76
- **作者**: Lin Wang, Yujeong Chae, Sung-Hoon Yoon, Tae-Kyun Kim, Kuk-Jin Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对事件相机数据缺乏标注、难以训练端到端模型的问题。②提出EvDistill方法，通过双向模态重建模块桥接事件数据和图像数据，并利用知识蒸馏从图像教师网络迁移知识到事件学生网络。③相比已有方法，无需配对数据即可进行跨模态蒸馏，且推理时无额外计算。④在多个事件数据任务上取得了优于现有方法的性能。
- **摘要（英）**: This paper addresses the lack of labeled event camera data for end-task training. It proposes EvDistill, which uses a bidirectional modality reconstruction module to bridge event and image data, enabling knowledge distillation from an image teacher to an event student without paired data. This approach adds no extra inference cost and outperforms existing methods on multiple event-based tasks.
- **核心贡献**: 提出无配对跨模态知识蒸馏框架，用于事件数据学习。
- **创新点**: 双向模态重建模块实现跨模态知识迁移。
- **结果**: 在事件数据任务上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Event cameras sense per-pixel intensity changes and produce asynchronous event streams with high dynamic range and less motion blur, showing advantages over conventional cameras. A hurdle of training event-based models is the lack of large qualitative labeled data. Prior works learning end-tasks mostly rely on labeled or pseudo-labeled datasets obtained from the active pixel sensor (APS) frames; however, such datasets' quality is far from rivaling those based on the canonical images. In this paper, we propose a novel approach, called \textbf{EvDistill}, to learn a student network on the unlabeled and unpaired event data (target modality) via knowledge distillation (KD) from a teacher network trained with large-scale, labeled image data (source modality). To enable KD across the unpaired modalities, we first propose a bidirectional modality reconstruction (BMR) module to bridge both modalities and simultaneously exploit them to distill knowledge via the crafted pairs, causing no extra computation in the inference. The BMR is improved by the end-tasks and KD losses in an end-to-end manner. Second, we leverage the structural similarities of both modalities and adapt the knowledge by matching their distributions. Moreover, as most prior feature KD methods are uni-modality and less applicable to our problem, we propose to leverage an affinity graph KD loss to boost the distillation. Our extensive experiments on semantic segmentation and object recognition demonstrate that EvDistill achieves significantly better results than the prior works and KD with only events and APS frames.

</details>

### Instance-Conditional Knowledge Distillation for Object Detection. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2110.12724](https://arxiv.org/abs/2110.12724)
- **作者**: Zijian Kang, Peizhen Zhang, Xiangyu Zhang, Jian Sun, Nanning Zheng
- **🏷️ 机构**: MEGVII, XJTU
- **会议**: NeurIPS 2021
- **摘要（中）**: 针对目标检测中知识蒸馏难以平衡不同位置表示对检测目标贡献的问题，提出了一种实例条件蒸馏框架，通过可学习的条件解码模块，以每个目标实例为查询检索教师表示中的相关信息，并利用定位-识别敏感辅助任务指导注意力权重。该方法在多种设置下显著提升性能，例如将ResNet-50的RetinaNet从37.4提升到40.7 mAP（+3.3），甚至超过使用ResNet-101的教师模型（40.4 mAP）。
- **摘要（英）**: This paper proposes an instance-conditional distillation framework for object detection, using a learnable decoding module to retrieve instance-specific knowledge from teacher representations, guided by a localization-recognition-sensitive task. It boosts RetinaNet with ResNet-50 from 37.4 to 40.7 mAP, surpassing the stronger teacher, demonstrating high efficacy.
- **核心贡献**: 提出了实例条件蒸馏框架，有效解决了检测中知识蒸馏的平衡问题。
- **创新点**: 创新性地引入条件解码模块和辅助任务，实现按实例自适应蒸馏。
- **结果**: 在多个检测器上实现显著提升，如RetinaNet +3.3 mAP并超越教师。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge distillation has shown great success in classification, however, it is still challenging for detection. In a typical image for detection, representations from different locations may have different contributions to detection targets, making the distillation hard to balance. In this paper, we propose a conditional distillation framework to distill the desired knowledge, namely knowledge that is beneficial in terms of both classification and localization for every instance. The framework introduces a learnable conditional decoding module, which retrieves information given each target instance as query. Specifically, we encode the condition information as query and use the teacher's representations as key. The attention between query and key is used to measure the contribution of different features, guided by a localization-recognition-sensitive auxiliary task. Extensive experiments demonstrate the efficacy of our method: we observe impressive improvements under various settings. Notably, we boost RetinaNet with ResNet-50 backbone from 37.4 to 40.7 mAP (+3.3) under 1x schedule, that even surpasses the teacher (40.4 mAP) with ResNet-101 backbone under 3x schedule. Code has been released on https://github.com/megvii-research/ICD.

</details>

## 跨领域论文（完整笔记在其他领域）

- 3DIoUMatch: Leveraging IoU Prediction for Semi-Supervised 3D Object Detection. → [object-detection](../object-detection/Guideline%202021.md)
- Humble Teachers Teach Better Students for Semi-Supervised Object Detection. → [object-detection](../object-detection/Guideline%202021.md)
- Towards Distraction-Robust Active Visual Tracking. → [tracking](../tracking/Guideline%202021.md)
- Continual Learning in the Teacher-Student Setup: Impact of Task Similarity. → [continual-learning](../continual-learning/Guideline%202021.md)
<!-- COMPLETE v1 papers=2 -->
