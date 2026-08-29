# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Rethinking Rotated Object Detection with Gaussian Wasserstein Distance Loss.
- **链接**: [arXiv:2101.11952](https://arxiv.org/abs/2101.11952) · [代码](https://github.com/yangxue0827/RotationDetection)
- **作者**: Xue Yang, Junchi Yan, Qi Ming, Wentao Wang, Xiaopeng Zhang, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Boundary discontinuity and its inconsistency to the final detection metric have been the bottleneck for rotating detection regression loss design. In this paper, we propose a novel regression loss based on Gaussian Wasserstein distance as a fundamental approach to solve the problem. Specifically, the rotated bounding box is converted to a 2-D Gaussian distribution, which enables to approximate the indifferentiable rotational IoU induced loss by the Gaussian Wasserstein distance (GWD) which can be learned efficiently by gradient back-propagation. GWD can still be informative for learning even there is no overlapping between two rotating bounding boxes which is often the case for small object detection. Thanks to its three unique properties, GWD can also elegantly solve the boundary discontinuity and square-like problem regardless how the bounding box is defined. Experiments on five datasets using different detectors show the effectiveness of our approach. Codes are available at https://github.com/yangxue0827/RotationDetection and https://github.com/open-mmlab/mmrotate.

</details>

### What Makes for End-to-End Object Detection?
- **链接**: [出版页](http://proceedings.mlr.press/v139/sun21b.html)
- **作者**: Peize Sun, Yi Jiang, Enze Xie, Wenqi Shao, Zehuan Yuan, Changhu Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021
