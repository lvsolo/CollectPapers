# Tracking — 2020 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Online Decision Based Visual Tracking via Reinforcement Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/885b2c7a6deb4fea10f319c4ce993e02-Abstract.html)
- **作者**: Ke Song, Wei Zhang, Ran Song, Yibin Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Deep Graph Pose: a semi-supervised deep graphical model for improved animal pose tracking.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/4379cf00e1a95a97a33dac10ce454ca4-Abstract.html) · 📚 被引 24
- **作者**: Anqi Wu, Estefany Kelly Buchanan, Matthew R. Whiteway, Michael Schartner, Guido Meijer, Jean-Paul Noel et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Segment as Points for Efficient Online Multi-Object Tracking and Segmentation.
- **链接**: [arXiv:2007.01550](https://arxiv.org/abs/2007.01550) · [代码](https://github.com/detectRecog/PointTrack)
- **作者**: Zhenbo Xu, Wei Zhang, Xiao Tan, Wei Yang, Huan Huang, Shilei Wen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current multi-object tracking and segmentation (MOTS) methods follow the tracking-by-detection paradigm and adopt convolutions for feature extraction. However, as affected by the inherent receptive field, convolution based feature extraction inevitably mixes up the foreground features and the background features, resulting in ambiguities in the subsequent instance association. In this paper, we propose a highly effective method for learning instance embeddings based on segments by converting the compact image representation to un-ordered 2D point cloud representation. Our method generates a new tracking-by-points paradigm where discriminative instance embeddings are learned from randomly selected points rather than images. Furthermore, multiple informative data modalities are converted into point-wise representations to enrich point-wise features. The resulting online MOTS framework, named PointTrack, surpasses all the state-of-the-art methods including 3D tracking methods by large margins (5.4% higher MOTSA and 18 times faster over MOTSFusion) with the near real-time speed (22 FPS). Evaluations across three datasets demonstrate both the effectiveness and efficiency of our method. Moreover, based on the observation that current MOTS datasets lack crowded scenes, we build a more challenging MOTS dataset named APOLLO MOTS with higher instance density. Both APOLLO MOTS and our codes are publicly available at https://github.com/detectRecog/PointTrack.

</details>

### SPARK: Spatial-Aware Online Incremental Attack Against Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58595-2_13) · 📚 被引 62
- **作者**: Qing Guo, Xiaofei Xie, Felix Juefei-Xu, Lei Ma, Zhongguo Li, Wanli Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### PG-Net: Pixel to Global Matching Network for Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58542-6_26) · 📚 被引 73
- **作者**: Bingyan Liao, Chenye Wang, Yayun Wang, Yaonong Wang, Jun Yin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

## 🆕 增量新增

### Simultaneous Detection and Tracking with Motion Modelling for Multiple Object Tracking. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58586-0_37)
- **作者**: ShiJie Sun, Naveed Akhtar, Xiangyu Song, HuanSheng Song, Ajmal Mian, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对多目标跟踪中检测与跟踪分离导致误差累积、运动模型简单的问题。②提出一种同时进行检测与跟踪的框架，将运动建模集成到检测过程中，实现端到端的联合优化。③相比传统两步法，该方法通过共享特征和联合推理减少误差传播，并引入更复杂的运动模型以适应目标动态变化。④摘要未提供具体数据，但理论上可提升跟踪鲁棒性和准确性。
- **摘要（英）**: This paper addresses the error accumulation and simplistic motion modeling in separate detection-tracking pipelines for multi-object tracking. It proposes a simultaneous detection and tracking framework that integrates motion modeling into the detection process for end-to-end joint optimization. Compared to two-step methods, it reduces error propagation via shared features and joint inference, with a more sophisticated motion model. Specific quantitative results are not provided in the abstract.
- **核心贡献**: 提出联合检测与运动建模的跟踪框架，减少误差累积。
- **创新点**: 将运动模型嵌入检测网络实现端到端联合优化。
- **结果**: 理论上提升跟踪性能，但无具体数据验证。

### Fooling Detection Alone is Not Enough: Adversarial Attack against Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openreview.net/forum?id=rJl31TNYPr)
- **作者**: Yunhan Jia, Yantao Lu, Junjie Shen, Qi Alfred Chen, Hao Chan, Zhenyu Zhong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020
- **摘要（中）**: ①针对多目标跟踪系统在对抗攻击下的脆弱性，现有攻击仅关注检测而忽略跟踪关联。②提出一种针对多目标跟踪的对抗攻击方法，通过同时干扰检测和关联模块，使跟踪性能显著下降。③相比仅攻击检测的方法，该攻击更全面，能有效破坏跟踪的时空一致性。④摘要未提供具体数值，但强调攻击效果优于单一检测攻击。
- **摘要（英）**: This paper addresses the vulnerability of multi-object tracking systems to adversarial attacks, noting that existing attacks focus only on detection. It proposes an adversarial attack method targeting both detection and association modules, significantly degrading tracking performance. Compared to detection-only attacks, it more comprehensively disrupts spatio-temporal consistency. Specific metrics are not given in the abstract.
- **核心贡献**: 提出首个针对多目标跟踪的联合攻击方法。
- **创新点**: 同时攻击检测与关联模块，破坏跟踪一致性。
- **结果**: 攻击效果优于仅检测攻击，但具体数据未披露。

### Lifted Disjoint Paths with Application in Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/hornakova20a.html)
- **作者**: Andrea Hornáková, Roberto Henschel, Bodo Rosenhahn, Paul Swoboda
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对多目标跟踪中数据关联的全局最优求解问题，传统方法计算复杂度高。②提出一种基于提升不相交路径（Lifted Disjoint Paths）的优化方法，将跟踪问题建模为图上的路径选择，并引入高阶约束提升关联准确性。③相比经典不相交路径方法，该方法通过提升边（lifted edges）捕获长时依赖，提高全局一致性。④摘要未提供具体数据，但理论上在复杂场景下具有更优的关联性能。
- **摘要（英）**: This paper tackles the global optimal data association problem in multi-object tracking, where traditional methods suffer from high computational complexity. It proposes a lifted disjoint paths approach, modeling tracking as path selection on a graph with higher-order constraints. Compared to classic disjoint paths, lifted edges capture long-term dependencies, improving global consistency. Specific results are not provided in the abstract.
- **核心贡献**: 提出提升不相交路径方法，增强跟踪关联的全局最优性。
- **创新点**: 引入提升边捕获长时依赖，突破传统路径约束。
- **结果**: 理论上提升关联性能，但缺乏实验数据。
<!-- COMPLETE v1 papers=8 -->
