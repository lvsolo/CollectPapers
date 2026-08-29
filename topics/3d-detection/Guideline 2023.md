# 3D Detection — 2023 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=-2zfgNS917)
- **作者**: Zehui Chen, Zhenyu Li, Shiquan Zhang, Liangji Fang, Qinhong Jiang, Feng Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Exploring Active 3D Object Detection from a Generalization Perspective.
- **链接**: [arXiv:2301.09249](https://arxiv.org/abs/2301.09249) · [代码](https://github.com/Luoyadan/CRB-active-3Ddet)
- **作者**: Yadan Luo, Zhuoxiao Chen, Zijian Wang, Xin Yu, Zi Huang, Mahsa Baktashmotlagh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To alleviate the high annotation cost in LiDAR-based 3D object detection, active learning is a promising solution that learns to select only a small portion of unlabeled data to annotate, without compromising model performance. Our empirical study, however, suggests that mainstream uncertainty-based and diversity-based active learning policies are not effective when applied in the 3D detection task, as they fail to balance the trade-off between point cloud informativeness and box-level annotation costs. To overcome this limitation, we jointly investigate three novel criteria in our framework Crb for point cloud acquisition - label conciseness}, feature representativeness and geometric balance, which hierarchically filters out the point clouds of redundant 3D bounding box labels, latent features and geometric characteristics (e.g., point cloud density) from the unlabeled sample pool and greedily selects informative ones with fewer objects to annotate. Our theoretical analysis demonstrates that the proposed criteria align the marginal distributions of the selected subset and the prior distributions of the unseen test set, and minimizes the upper bound of the generalization error. To validate the effectiveness and applicability of Crb, we conduct extensive experiments on the two benchmark 3D object detection datasets of KITTI and Waymo and examine both one-stage (i.e., Second) and two-stage 3D detectors (i.e., Pv-rcnn). Experiments evidence that the proposed approach outperforms existing active learning strategies and achieves fully supervised performance requiring $1\%$ and $8\%$ annotations of bounding boxes and point clouds, respectively. Source code: https://github.com/Luoyadan/CRB-active-3Ddet.

</details>

### Time Will Tell: New Outlooks and A Baseline for Temporal Multi-View 3D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=H3HcEJA2Um)
- **作者**: Jinhyung Park, Chenfeng Xu, Shijia Yang, Kurt Keutzer, Kris M. Kitani, Masayoshi Tomizuka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### DBQ-SSD: Dynamic Ball Query for Efficient 3D Object Detection.
- **链接**: [arXiv:2207.10909](https://arxiv.org/abs/2207.10909) · [代码](https://github.com/yancie-yjr/DBQ-SSD)
- **作者**: Jinrong Yang, Lin Song, Songtao Liu, Weixin Mao, Zeming Li, Xiaoping Li et al.
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many point-based 3D detectors adopt point-feature sampling strategies to drop some points for efficient inference. These strategies are typically based on fixed and handcrafted rules, making it difficult to handle complicated scenes. Different from them, we propose a Dynamic Ball Query (DBQ) network to adaptively select a subset of input points according to the input features, and assign the feature transform with a suitable receptive field for each selected point. It can be embedded into some state-of-the-art 3D detectors and trained in an end-to-end manner, which significantly reduces the computational cost. Extensive experiments demonstrate that our method can increase the inference speed by 30%-100% on KITTI, Waymo, and ONCE datasets. Specifically, the inference speed of our detector can reach 162 FPS on KITTI scene, and 30 FPS on Waymo and ONCE scenes without performance degradation. Due to skipping the redundant points, some evaluation metrics show significant improvements. Codes will be released at https://github.com/yancie-yjr/DBQ-SSD.

</details>
