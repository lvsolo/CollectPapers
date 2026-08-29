# 3D Detection — 2021 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Object DGCNN: 3D Object Detection using Dynamic Graphs.
- **链接**: [arXiv:2110.06923](https://arxiv.org/abs/2110.06923)
- **作者**: Yue Wang, Justin M. Solomon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection often involves complicated training and testing pipelines, which require substantial domain knowledge about individual datasets. Inspired by recent non-maximum suppression-free 2D object detection models, we propose a 3D object detection architecture on point clouds. Our method models 3D object detection as message passing on a dynamic graph, generalizing the DGCNN framework to predict a set of objects. In our construction, we remove the necessity of post-processing via object confidence aggregation or non-maximum suppression. To facilitate object detection from sparse point clouds, we also propose a set-to-set distillation approach customized to 3D detection. This approach aligns the outputs of the teacher model and the student model in a permutation-invariant fashion, significantly simplifying knowledge distillation for the 3D detection task. Our method achieves state-of-the-art performance on autonomous driving benchmarks. We also provide abundant analysis of the detection model and distillation framework.

</details>

### Revisiting 3D Object Detection From an Egocentric Perspective.
- **链接**: [arXiv:2112.07787](https://arxiv.org/abs/2112.07787)
- **作者**: Boyang Deng, Charles R. Qi, Mahyar Najibi, Thomas A. Funkhouser, Yin Zhou, Dragomir Anguelov
- **🏷️ 机构**: Waymo
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a key module for safety-critical robotics applications such as autonomous driving. For these applications, we care most about how the detections affect the ego-agent's behavior and safety (the egocentric perspective). Intuitively, we seek more accurate descriptions of object geometry when it's more likely to interfere with the ego-agent's motion trajectory. However, current detection metrics, based on box Intersection-over-Union (IoU), are object-centric and aren't designed to capture the spatio-temporal relationship between objects and the ego-agent. To address this issue, we propose a new egocentric measure to evaluate 3D object detection, namely Support Distance Error (SDE). Our analysis based on SDE reveals that the egocentric detection quality is bounded by the coarse geometry of the bounding boxes. Given the insight that SDE would benefit from more accurate geometry descriptions, we propose to represent objects as amodal contours, specifically amodal star-shaped polygons, and devise a simple model, StarPoly, to predict such contours. Our experiments on the large-scale Waymo Open Dataset show that SDE better reflects the impact of detection quality on the ego-agent's safety compared to IoU; and the estimated contours from StarPoly consistently improve the egocentric detection quality over recent 3D object detectors.

</details>

### Voxel-based 3D Detection and Reconstruction of Multiple Objects from a Single Image.
- **链接**: [arXiv:2111.03098](https://arxiv.org/abs/2111.03098)
- **作者**: Feng Liu, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inferring 3D locations and shapes of multiple objects from a single 2D image is a long-standing objective of computer vision. Most of the existing works either predict one of these 3D properties or focus on solving both for a single object. One fundamental challenge lies in how to learn an effective representation of the image that is well-suited for 3D detection and reconstruction. In this work, we propose to learn a regular grid of 3D voxel features from the input image which is aligned with 3D scene space via a 3D feature lifting operator. Based on the 3D voxel features, our novel CenterNet-3D detection head formulates the 3D detection as keypoint detection in the 3D space. Moreover, we devise an efficient coarse-to-fine reconstruction module, including coarse-level voxelization and a novel local PCA-SDF shape representation, which enables fine detail reconstruction and one order of magnitude faster inference than prior methods. With complementary supervision from both 3D detection and reconstruction, one enables the 3D voxel features to be geometry and context preserving, benefiting both tasks.The effectiveness of our approach is demonstrated through 3D detection and reconstruction in single object and multiple object scenarios.

</details>

### Progressive Coordinate Transforms for Monocular 3D Object Detection.
- **链接**: [arXiv:2108.05793](https://arxiv.org/abs/2108.05793) · [代码](https://github.com/amazon-research/progressive-coordinate-transforms)
- **作者**: Li Wang, Li Zhang, Yi Zhu, Zhi Zhang, Tong He, Mu Li et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab, AWS / CMU
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recognizing and localizing objects in the 3D space is a crucial ability for an AI agent to perceive its surrounding environment. While significant progress has been achieved with expensive LiDAR point clouds, it poses a great challenge for 3D object detection given only a monocular image. While there exist different alternatives for tackling this problem, it is found that they are either equipped with heavy networks to fuse RGB and depth information or empirically ineffective to process millions of pseudo-LiDAR points. With in-depth examination, we realize that these limitations are rooted in inaccurate object localization. In this paper, we propose a novel and lightweight approach, dubbed {\em Progressive Coordinate Transforms} (PCT) to facilitate learning coordinate representations. Specifically, a localization boosting mechanism with confidence-aware loss is introduced to progressively refine the localization prediction. In addition, semantic image representation is also exploited to compensate for the usage of patch proposals. Despite being lightweight and simple, our strategy leads to superior improvements on the KITTI and Waymo Open Dataset monocular 3D detection benchmarks. At the same time, our proposed PCT shows great generalization to most coordinate-based 3D detection frameworks. The code is available at: https://github.com/amazon-research/progressive-coordinate-transforms .

</details>

### 3D Siamese Voxel-to-BEV Tracker for Sparse Point Clouds.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/f0fcf351df4eb6786e9bb6fc4e2dee02-Abstract.html)
- **作者**: Le Hui, Lingpeng Wang, Mingmei Cheng, Jin Xie, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Learning Transferable Features for Point Cloud Detection via 3D Contrastive Co-training.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b3b25a26a0828ea5d48d8f8aa0d6f9af-Abstract.html)
- **作者**: Yihan Zeng, Chunwei Wang, Yunbo Wang, Hang Xu, Chaoqiang Ye, Zhen Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Multimodal Virtual Point 3D Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/895daa408f494ad58006c47a30f51c1f-Abstract.html)
- **作者**: Tianwei Yin, Xingyi Zhou, Philipp Krähenbühl
- **🏷️ 机构**: UT Austin
- **会议**: NeurIPS 2021
