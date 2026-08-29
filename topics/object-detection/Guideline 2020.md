# Object Detection — 2020 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Computation Reallocation for Object Detection.
- **链接**: [arXiv:1912.11234](https://arxiv.org/abs/1912.11234)
- **作者**: Feng Liang, Chen Lin, Ronghao Guo, Ming Sun, Wei Wu, Junjie Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The allocation of computation resources in the backbone is a crucial issue in object detection. However, classification allocation pattern is usually adopted directly to object detector, which is proved to be sub-optimal. In order to reallocate the engaged computation resources in a more efficient way, we present CR-NAS (Computation Reallocation Neural Architecture Search) that can learn computation reallocation strategies across different feature resolution and spatial position diectly on the target detection dataset. A two-level reallocation space is proposed for both stage and spatial reallocation. A novel hierarchical search procedure is adopted to cope with the complex search space. We apply CR-NAS to multiple backbones and achieve consistent improvements. Our CR-ResNet50 and CR-MobileNetV2 outperforms the baseline by 1.9% and 1.7% COCO AP respectively without any additional computation budget. The models discovered by CR-NAS can be equiped to other powerful detection neck/head and be easily transferred to other dataset, e.g. PASCAL VOC, and other vision tasks, e.g. instance segmentation. Our CR-NAS can be used as a plugin to improve the performance of various networks, which is demanding.

</details>

## 跨领域论文（完整笔记在其他领域）

- Pseudo-LiDAR++: Accurate Depth for 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
