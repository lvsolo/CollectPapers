# Multi-camera Perception — 2020 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Learning Multiview 3D Point Cloud Registration.
- **链接**: [arXiv:2001.05119](https://arxiv.org/abs/2001.05119) · [代码](https://github.com/zgojcic/3D_multiview_reg) · 📚 被引 160
- **作者**: Zan Gojcic, Caifa Zhou, Jan D. Wegner, Leonidas J. Guibas, Tolga Birdal
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel, end-to-end learnable, multiview 3D point cloud registration algorithm. Registration of multiple scans typically follows a two-stage pipeline: the initial pairwise alignment and the globally consistent refinement. The former is often ambiguous due to the low overlap of neighboring point clouds, symmetries and repetitive scene parts. Therefore, the latter global refinement aims at establishing the cyclic consistency across multiple scans and helps in resolving the ambiguous cases. In this paper we propose, to the best of our knowledge, the first end-to-end algorithm for joint learning of both parts of this two-stage problem. Experimental evaluation on well accepted benchmark datasets shows that our approach outperforms the state-of-the-art by a significant margin, while being end-to-end trainable and computationally less costly. Moreover, we present detailed analysis and an ablation study that validate the novel components of our approach. The source code and pretrained models are publicly available under https://github.com/zgojcic/3D_multiview_reg.

</details>

### End-to-End Learning Local Multi-View Descriptors for 3D Point Clouds.
- **链接**: [arXiv:2003.05855](https://arxiv.org/abs/2003.05855) · 📚 被引 102
- **作者**: Lei Li, Siyu Zhu, Hongbo Fu, Ping Tan, Chiew-Lan Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### 3D Packing for Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Guizilini_3D_Packing_for_Self-Supervised_Monocular_Depth_Estimation_CVPR_2020_paper.html)
- **作者**: Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raventos, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Exploit Clues From Views: Self-Supervised and Regularized Learning for Multiview Object Recognition.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Ho_Exploit_Clues_From_Views_Self-Supervised_and_Regularized_Learning_for_Multiview_CVPR_2020_paper.html)
- **作者**: Chih-Hui Ho, Bo Liu, Tz-Ying Wu, Nuno Vasconcelos
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### On the Uncertainty of Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Poggi_On_the_Uncertainty_of_Self-Supervised_Monocular_Depth_Estimation_CVPR_2020_paper.html)
- **作者**: Matteo Poggi, Filippo Aleotti, Fabio Tosi, Stefano Mattoccia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

## 🆕 增量新增

### GeoGraph: Graph-Based Multi-view Object Detection with Geometric Cues End-to-End. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58571-6_29)
- **作者**: Ahmed Samy Nassar, Stefano D'Aronco, Sébastien Lefèvre, Jan D. Wegner
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对多视角3D目标检测中几何信息利用不足和端到端训练困难的问题。②提出GeoGraph，利用图神经网络建模多视角几何关系，并引入几何线索实现端到端检测。③相比已有基于投影或Transformer的方法，显式编码相机间几何约束，提升跨视角一致性。④在nuScenes等数据集上达到领先的检测精度，尤其在小目标和遮挡场景中表现突出。
- **摘要（英）**: GeoGraph proposes a graph-based multi-view object detection framework that explicitly encodes geometric cues between cameras, enabling end-to-end training. It achieves leading detection accuracy on nuScenes, particularly for small and occluded objects.
- **核心贡献**: 提出基于图神经网络的多视角几何建模方法，提升端到端3D检测性能。
- **创新点**: 将相机间几何关系编码为图结构，实现几何感知的跨视角特征融合。
- **结果**: 在nuScenes上达到领先精度，显著改善小目标和遮挡场景检测。

### Multi-view Action Recognition Using Cross-View Video Prediction. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58583-9_26)
- **作者**: Shruti Vyas, Yogesh S. Rawat, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①针对多视角动作识别中视角差异导致的特征不对齐问题。②提出跨视角视频预测方法，通过预测其他视角的视频帧来学习视角不变表示。③相比直接融合多视角特征，该方法利用生成式预测增强跨视角一致性。④在多个动作识别基准上取得改进，但提升幅度有限。
- **摘要（英）**: This work addresses cross-view action recognition by predicting videos from other views, learning view-invariant representations. It improves recognition accuracy on benchmarks, though gains are moderate.
- **核心贡献**: 提出基于跨视角视频预测的视角不变表示学习方法。
- **创新点**: 利用生成式预测任务促进多视角特征对齐。
- **结果**: 在动作识别基准上取得一定精度提升。

### Contrastive Multi-View Representation Learning on Graphs. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/hassani20a.html)
- **作者**: Kaveh Hassani, Amir Hosein Khas Ahmadi
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对图数据上多视图表示学习中的对比学习效率问题。②提出对比多视图图表示学习方法，优化跨视图对比目标。③相比单视图图对比学习，利用多视图信息增强表示质量。④在多个图数据集上验证了有效性，但领域与视觉感知差异大。
- **摘要（英）**: This paper proposes contrastive multi-view representation learning for graphs, leveraging cross-view contrastive objectives to improve representation quality. It shows effectiveness on graph benchmarks.
- **核心贡献**: 提出面向图数据的多视图对比学习框架。
- **创新点**: 将多视图对比学习扩展到图结构数据。
- **结果**: 在图数据集上提升了表示学习性能。

### Forget About the LiDAR: Self-Supervised Depth Estimators with MED Probability Volumes. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/951124d4a093eeae83d9726a20295498-Abstract.html)
- **作者**: Juan Luis Gonzalez Bello, Munchurl Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020
- **摘要（中）**: ①针对自监督深度估计中依赖LiDAR监督或复杂后处理的问题，提出无需LiDAR的纯自监督方案。②提出MED概率体积（MED Probability Volumes）方法，通过概率建模深度分布，替代传统离散化深度表示。③相比已有自监督方法，MED体积更高效且精度更高，无需LiDAR标签。④在KITTI等基准上达到自监督深度估计的最优精度，且推理速度更快。
- **摘要（英）**: This paper introduces MED Probability Volumes for self-supervised depth estimation, replacing discrete depth representations with probabilistic volumes, eliminating LiDAR dependency. It achieves state-of-the-art accuracy among self-supervised methods on KITTI with faster inference.
- **核心贡献**: 提出MED概率体积，实现无需LiDAR的高精度自监督深度估计。
- **创新点**: 用概率体积建模深度分布，替代传统离散化表示，提升效率和精度。
- **结果**: 在KITTI上达到自监督最优精度，并加速推理。

## 跨领域论文（完整笔记在其他领域）

- From Image Collections to Point Clouds With Self-Supervised Shape and Pose Networks. → [self-supervised-vision](../self-supervised-vision/Guideline%202020.md)
- Self-Supervised Monocular Trained Depth Estimation Using Self-Attention and Discrete Disparity Volume. → [self-supervised-vision](../self-supervised-vision/Guideline%202020.md)
- Self-Supervised Monocular Scene Flow Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202020.md)
<!-- COMPLETE v1 papers=9 -->
