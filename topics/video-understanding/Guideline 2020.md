# Video Understanding — 2020 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Screencast Tutorial Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Screencast_Tutorial_Video_Understanding_CVPR_2020_paper.html)
- **作者**: Kunpeng Li, Chen Fang, Zhaowen Wang, Seokhwan Kim, Hailin Jin, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Gate-Shift Networks for Video Action Recognition.
- **链接**: [arXiv:1912.00381](https://arxiv.org/abs/1912.00381) · 📚 被引 155
- **作者**: Swathikiran Sudhakaran, Sergio Escalera, Oswald Lanz
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep 3D CNNs for video action recognition are designed to learn powerful representations in the joint spatio-temporal feature space. In practice however, because of the large number of parameters and computations involved, they may under-perform in the lack of sufficiently large datasets for training them at scale. In this paper we introduce spatial gating in spatial-temporal decomposition of 3D kernels. We implement this concept with Gate-Shift Module (GSM). GSM is lightweight and turns a 2D-CNN into a highly efficient spatio-temporal feature extractor. With GSM plugged in, a 2D-CNN learns to adaptively route features through time and combine them, at almost no additional parameters and computational overhead. We perform an extensive evaluation of the proposed module to study its effectiveness in video action recognition, achieving state-of-the-art results on Something Something-V1 and Diving48 datasets, and obtaining competitive results on EPIC-Kitchens with far less model complexity.

</details>

### Spatio-Temporal Graph for Video Captioning With Knowledge Distillation.
- **链接**: [arXiv:2003.13942](https://arxiv.org/abs/2003.13942) · 📚 被引 213
- **作者**: Boxiao Pan, Haoye Cai, De-An Huang, Kuan-Hui Lee, Adrien Gaidon, Ehsan Adeli et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video captioning is a challenging task that requires a deep understanding of visual scenes. State-of-the-art methods generate captions using either scene-level or object-level information but without explicitly modeling object interactions. Thus, they often fail to make visually grounded predictions, and are sensitive to spurious correlations. In this paper, we propose a novel spatio-temporal graph model for video captioning that exploits object interactions in space and time. Our model builds interpretable links and is able to provide explicit visual grounding. To avoid unstable performance caused by the variable number of objects, we further propose an object-aware knowledge distillation mechanism, in which local object information is used to regularize global scene features. We demonstrate the efficacy of our approach through extensive experiments on two benchmarks, showing our approach yields competitive performance with interpretable predictions.

</details>

## 跨领域论文（完整笔记在其他领域）

- Video Playback Rate Perception for Self-Supervised Spatio-Temporal Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202020.md)
- 3DV: 3D Dynamic Voxel for Action Recognition in Depth Video. → [3d-detection](../3d-detection/Guideline%202020.md)

## 🆕 增量新增

### RubiksNet: Learnable 3D-Shift for Efficient Video Action Recognition. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58529-7_30)
- **作者**: Linxi Fan, Shyamal Buch, Guanzhi Wang, Ryan Cao, Yuke Zhu, Juan Carlos Niebles et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①该论文针对视频动作识别中3D卷积计算成本高的问题。②提出了RubiksNet，利用可学习的3D移位操作替代传统卷积，实现高效时空特征提取。③相比固定移位模式，该方法通过可学习参数自适应调整移位策略，提升了模型灵活性。④由于摘要缺失，具体效果数据未知，但该方向在效率与性能平衡上有潜力。
- **摘要（英）**: This paper addresses the high computational cost of 3D convolutions in video action recognition. It proposes RubiksNet, which uses learnable 3D shifts to replace standard convolutions for efficient spatio-temporal modeling. The learnable shifts offer adaptive routing compared to fixed patterns. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出可学习3D移位机制用于高效视频识别。
- **创新点**: 将移位操作参数化，实现数据驱动的时空特征重组。
- **结果**: 效果未知，因摘要缺失。

## 跨领域论文（完整笔记在其他领域）

- Video Playback Rate Perception for Self-Supervised Spatio-Temporal Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202020.md)
- Multi-Modal Domain Adaptation for Fine-Grained Action Recognition. → [multimodal](../multimodal/Guideline%202020.md)
- Speech2Action: Cross-Modal Supervision for Action Recognition. → [multimodal](../multimodal/Guideline%202020.md)
- 3DV: 3D Dynamic Voxel for Action Recognition in Depth Video. → [3d-detection](../3d-detection/Guideline%202020.md)
- Multi-view Action Recognition Using Cross-View Video Prediction. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
<!-- COMPLETE v1 papers=4 -->
