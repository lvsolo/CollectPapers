# Object Detection — 2025 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Union-over-Intersections: Object Detection beyond Winner-Takes-All.
- **链接**: [出版页](https://openreview.net/forum?id=HqLHY4TzGj)
- **作者**: Aritra Bhowmik, Pascal Mettes, Martin R. Oswald, Cees G. M. Snoek
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Pursuing Better Decision Boundaries for Long-Tailed Object Detection via Category Information Amount.
- **链接**: [arXiv:2502.03852](https://arxiv.org/abs/2502.03852)
- **作者**: Yanbiao Ma, Wei Dai, Jiayi Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In object detection, the instance count is typically used to define whether a dataset exhibits a long-tail distribution, implicitly assuming that models will underperform on categories with fewer instances. This assumption has led to extensive research on category bias in datasets with imbalanced instance counts. However, models still exhibit category bias even in datasets where instance counts are relatively balanced, clearly indicating that instance count alone cannot explain this phenomenon. In this work, we first introduce the concept and measurement of category information amount. We observe a significant negative correlation between category information amount and accuracy, suggesting that category information amount more accurately reflects the learning difficulty of a category. Based on this observation, we propose Information Amount-Guided Angular Margin (IGAM) Loss. The core idea of IGAM is to dynamically adjust the decision space of each category based on its information amount, thereby reducing category bias in long-tail datasets. IGAM Loss not only performs well on long-tailed benchmark datasets such as LVIS v1.0 and COCO-LT but also shows significant improvement for underrepresented categories in the non-long-tailed dataset Pascal VOC. Comprehensive experiments demonstrate the potential of category information amount as a tool and the generality of our proposed method.

</details>

### PointOBB-v2: Towards Simpler, Faster, and Stronger Single Point Supervised Oriented Object Detection.
- **链接**: [arXiv:2410.08210](https://arxiv.org/abs/2410.08210)
- **作者**: Botao Ren, Xue Yang, Yi Yu, Junwei Luo, Zhidong Deng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Single point supervised oriented object detection has gained attention and made initial progress within the community. Diverse from those approaches relying on one-shot samples or powerful pretrained models (e.g. SAM), PointOBB has shown promise due to its prior-free feature. In this paper, we propose PointOBB-v2, a simpler, faster, and stronger method to generate pseudo rotated boxes from points without relying on any other prior. Specifically, we first generate a Class Probability Map (CPM) by training the network with non-uniform positive and negative sampling. We show that the CPM is able to learn the approximate object regions and their contours. Then, Principal Component Analysis (PCA) is applied to accurately estimate the orientation and the boundary of objects. By further incorporating a separation mechanism, we resolve the confusion caused by the overlapping on the CPM, enabling its operation in high-density scenarios. Extensive comparisons demonstrate that our method achieves a training speed 15.58x faster and an accuracy improvement of 11.60%/25.15%/21.19% on the DOTA-v1.0/v1.5/v2.0 datasets compared to the previous state-of-the-art, PointOBB. This significantly advances the cutting edge of single point supervised oriented detection in the modular track.

</details>

### Multi-Perspective Data Augmentation for Few-shot Object Detection.
- **链接**: [arXiv:2502.18195](https://arxiv.org/abs/2502.18195) · [代码](https://github.com/nvakhoa/MPAD)
- **作者**: Anh-Khoa Nguyen Vu, Quoc-Truong Truong, Vinh-Tiep Nguyen, Thanh Duc Ngo, Thanh-Toan Do, Tam V. Nguyen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent few-shot object detection (FSOD) methods have focused on augmenting synthetic samples for novel classes, show promising results to the rise of diffusion models. However, the diversity of such datasets is often limited in representativeness because they lack awareness of typical and hard samples, especially in the context of foreground and background relationships. To tackle this issue, we propose a Multi-Perspective Data Augmentation (MPAD) framework. In terms of foreground-foreground relationships, we propose in-context learning for object synthesis (ICOS) with bounding box adjustments to enhance the detail and spatial information of synthetic samples. Inspired by the large margin principle, support samples play a vital role in defining class boundaries. Therefore, we design a Harmonic Prompt Aggregation Scheduler (HPAS) to mix prompt embeddings at each time step of the generation process in diffusion models, producing hard novel samples. For foreground-background relationships, we introduce a Background Proposal method (BAP) to sample typical and hard backgrounds. Extensive experiments on multiple FSOD benchmarks demonstrate the effectiveness of our approach. Our framework significantly outperforms traditional methods, achieving an average increase of $17.5\%$ in nAP50 over the baseline on PASCAL VOC. Code is available at https://github.com/nvakhoa/MPAD.

</details>

### High-dimension Prototype is a Better Incremental Object Detection Learner.
- **链接**: [出版页](https://openreview.net/forum?id=6T8czSBWce)
- **作者**: Yanjie Wang, Liqun Chen, Tianming Zhao, Tao Zhang, Guodong Wang, Luxin Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### PseDet: Revisiting the Power of Pseudo Label in Incremental Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=Iu8FVcUmVp)
- **作者**: Qiuchen Wang, Zehui Chen, Chenhongyi Yang, Jiaming Liu, Zhenyu Li, Feng Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### R2Det: Exploring Relaxed Rotation Equivariance in 2D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=EUeNr3e8AV)
- **作者**: Zhiqiang Wu, Yingjie Liu, Hanlin Dong, Xuan Tang, Jian Yang, Bo Jin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Cyclic Contrastive Knowledge Transfer for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=JU9oHs7ivN)
- **作者**: Chuhan Zhang, Chaoyang Zhu, Pingcheng Dong, Long Chen, Dong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Open-YOLO 3D: Towards Fast and Accurate Open-Vocabulary 3D Instance Segmentation.
- **链接**: [出版页](https://openreview.net/forum?id=CRmiX0v16e)
- **作者**: Mohamed El Amine Boudjoghra, Angela Dai, Jean Lahoud, Hisham Cholakkal, Rao Muhammad Anwer, Salman H. Khan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

## 跨领域论文（完整笔记在其他领域）

- MOS: Model Synergy for Test-Time Adaptation on LiDAR-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Intent3D: 3D Object Detection in RGB-D Scans Based on Human Intention. → [3d-detection](../3d-detection/Guideline%202025.md)
- State Space Model Meets Transformer: A New Paradigm for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Gaussian-Det: Learning Closed-Surface Gaussians for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
