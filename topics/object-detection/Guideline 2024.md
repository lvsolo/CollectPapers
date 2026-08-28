# Object Detection — 2024 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Size-invariance Matters: Rethinking Metrics and Losses for Imbalanced Multi-object Salient Object Detection.
- **链接**: [arXiv:2405.09782](https://arxiv.org/abs/2405.09782) · [代码](https://github.com/Ferry-Li/SI-SOD)
- **作者**: Feiran Li, Qianqian Xu, Shilong Bao, Zhiyong Yang, Runmin Cong, Xiaochun Cao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the size-invariance of evaluation metrics in Salient Object Detection (SOD), especially when multiple targets of diverse sizes co-exist in the same image. We observe that current metrics are size-sensitive, where larger objects are focused, and smaller ones tend to be ignored. We argue that the evaluation should be size-invariant because bias based on size is unjustified without additional semantic information. In pursuit of this, we propose a generic approach that evaluates each salient object separately and then combines the results, effectively alleviating the imbalance. We further develop an optimization framework tailored to this goal, achieving considerable improvements in detecting objects of different sizes. Theoretically, we provide evidence supporting the validity of our new metrics and present the generalization analysis of SOD. Extensive experiments demonstrate the effectiveness of our method. The code is available at https://github.com/Ferry-Li/SI-SOD.

</details>

### ESNet: Evolution and Succession Network for High-Resolution Salient Object Detection.
- **链接**: [出版页](https://proceedings.mlr.press/v235/liu24l.html)
- **作者**: Hongyu Liu, Runmin Cong, Hua Li, Qianqian Xu, Qingming Huang, Wei Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### DSD-DA: Distillation-based Source Debiasing for Domain Adaptive Object Detection.
- **链接**: [出版页](https://proceedings.mlr.press/v235/feng24d.html)
- **作者**: Yongchao Feng, Shiwei Li, Yingjie Gao, Ziyue Huang, Yanan Zhang, Qingjie Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024
