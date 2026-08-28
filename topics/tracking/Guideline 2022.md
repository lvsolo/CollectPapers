# Tracking — 2022 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Towards Generic 3D Tracking in RGBD Videos: Benchmark and Baseline.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_7) · 📚 被引 4
- **作者**: Jinyu Yang, Zhongqun Zhang, Zhe Li, Hyung Jin Chang, Ales Leonardis, Feng Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### ByteTrack: Multi-object Tracking by Associating Every Detection Box.
- **链接**: [arXiv:2110.06864](https://arxiv.org/abs/2110.06864) · [代码](https://github.com/ifzhang/ByteTrack) · 📚 被引 2137
- **作者**: Yifu Zhang, Peize Sun, Yi Jiang, Dongdong Yu, Fucheng Weng, Zehuan Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking (MOT) aims at estimating bounding boxes and identities of objects in videos. Most methods obtain identities by associating detection boxes whose scores are higher than a threshold. The objects with low detection scores, e.g. occluded objects, are simply thrown away, which brings non-negligible true object missing and fragmented trajectories. To solve this problem, we present a simple, effective and generic association method, tracking by associating almost every detection box instead of only the high score ones. For the low score detection boxes, we utilize their similarities with tracklets to recover true objects and filter out the background detections. When applied to 9 different state-of-the-art trackers, our method achieves consistent improvement on IDF1 score ranging from 1 to 10 points. To put forwards the state-of-the-art performance of MOT, we design a simple and strong tracker, named ByteTrack. For the first time, we achieve 80.3 MOTA, 77.3 IDF1 and 63.1 HOTA on the test set of MOT17 with 30 FPS running speed on a single V100 GPU. ByteTrack also achieves state-of-the-art performance on MOT20, HiEve and BDD100K tracking benchmarks. The source code, pre-trained models with deploy versions and tutorials of applying to other trackers are released at https://github.com/ifzhang/ByteTrack.

</details>

### CMT: Context-Matching-Guided Transformer for 3D Tracking in Point Clouds.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_6) · 📚 被引 17
- **作者**: Zhiyang Guo, Yunyao Mao, Wengang Zhou, Min Wang, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### 3D Siamese Transformer Network for Single Object Tracking on Point Clouds.
- **链接**: [arXiv:2207.11995](https://arxiv.org/abs/2207.11995)
- **作者**: Le Hui, Lingpeng Wang, Linghua Tang, Kaihao Lan, Jin Xie, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Siamese network based trackers formulate 3D single object tracking as cross-correlation learning between point features of a template and a search area. Due to the large appearance variation between the template and search area during tracking, how to learn the robust cross correlation between them for identifying the potential target in the search area is still a challenging problem. In this paper, we explicitly use Transformer to form a 3D Siamese Transformer network for learning robust cross correlation between the template and the search area of point clouds. Specifically, we develop a Siamese point Transformer network to learn shape context information of the target. Its encoder uses self-attention to capture non-local information of point clouds to characterize the shape information of the object, and the decoder utilizes cross-attention to upsample discriminative point features. After that, we develop an iterative coarse-to-fine correlation network to learn the robust cross correlation between the template and the search area. It formulates the cross-feature augmentation to associate the template with the potential target in the search area via cross attention. To further enhance the potential target, it employs the ego-feature augmentation that applies self-attention to the local k-NN graph of the feature space to aggregate target features. Experiments on the KITTI, nuScenes, and Waymo datasets show that our method achieves state-of-the-art performance on the 3D single object tracking task.

</details>

### PolarMOT: How Far Can Geometric Relations Take us in 3D Multi-object Tracking?
- **链接**: [arXiv:2208.01957](https://arxiv.org/abs/2208.01957) · 📚 被引 46
- **作者**: Aleksandr Kim, Guillem Brasó, Aljosa Osep, Laura Leal-Taixé
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most (3D) multi-object tracking methods rely on appearance-based cues for data association. By contrast, we investigate how far we can get by only encoding geometric relationships between objects in 3D space as cues for data-driven data association. We encode 3D detections as nodes in a graph, where spatial and temporal pairwise relations among objects are encoded via localized polar coordinates on graph edges. This representation makes our geometric relations invariant to global transformations and smooth trajectory changes, especially under non-holonomic motion. This allows our graph neural network to learn to effectively encode temporal and spatial interactions and fully leverage contextual and motion cues to obtain final scene interpretation by posing data association as edge classification. We establish a new state-of-the-art on nuScenes dataset and, more importantly, show that our method, PolarMOT, generalizes remarkably well across different locations (Boston, Singapore, Karlsruhe) and datasets (nuScenes and KITTI).

</details>

### MOTCOM: The Multi-Object Tracking Dataset Complexity Metric.
- **链接**: [arXiv:2207.10031](https://arxiv.org/abs/2207.10031) · 📚 被引 4
- **作者**: Malte Pedersen, Joakim Bruslund Haurum, Patrick Dendorfer, Thomas B. Moeslund
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There exists no comprehensive metric for describing the complexity of Multi-Object Tracking (MOT) sequences. This lack of metrics decreases explainability, complicates comparison of datasets, and reduces the conversation on tracker performance to a matter of leader board position. As a remedy, we present the novel MOT dataset complexity metric (MOTCOM), which is a combination of three sub-metrics inspired by key problems in MOT: occlusion, erratic motion, and visual similarity. The insights of MOTCOM can open nuanced discussions on tracker performance and may lead to a wider acknowledgement of novel contributions developed for either less known datasets or those aimed at solving sub-problems. We evaluate MOTCOM on the comprehensive MOT17, MOT20, and MOTSynth datasets and show that MOTCOM is far better at describing the complexity of MOT sequences compared to the conventional density and number of tracks. Project page at https://vap.aau.dk/motcom

</details>

### Robust Multi-object Tracking by Marginal Inference.
- **链接**: [arXiv:2208.03727](https://arxiv.org/abs/2208.03727)
- **作者**: Yifu Zhang, Chunyu Wang, Xinggang Wang, Wenjun Zeng, Wenyu Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking in videos requires to solve a fundamental problem of one-to-one assignment between objects in adjacent frames. Most methods address the problem by first discarding impossible pairs whose feature distances are larger than a threshold, followed by linking objects using Hungarian algorithm to minimize the overall distance. However, we find that the distribution of the distances computed from Re-ID features may vary significantly for different videos. So there isn't a single optimal threshold which allows us to safely discard impossible pairs. To address the problem, we present an efficient approach to compute a marginal probability for each pair of objects in real time. The marginal probability can be regarded as a normalized distance which is significantly more stable than the original feature distance. As a result, we can use a single threshold for all videos. The approach is general and can be applied to the existing trackers to obtain about one point improvement in terms of IDF1 metric. It achieves competitive results on MOT17 and MOT20 benchmarks. In addition, the computed probability is more interpretable which facilitates subsequent post-processing operations.

</details>

### AiATrack: Attention in Attention for Transformer Visual Tracking.
- **链接**: [arXiv:2207.09603](https://arxiv.org/abs/2207.09603) · 📚 被引 333
- **作者**: Shenyuan Gao, Chunluan Zhou, Chao Ma, Xinggang Wang, Junsong Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer trackers have achieved impressive advancements recently, where the attention mechanism plays an important role. However, the independent correlation computation in the attention mechanism could result in noisy and ambiguous attention weights, which inhibits further performance improvement. To address this issue, we propose an attention in attention (AiA) module, which enhances appropriate correlations and suppresses erroneous ones by seeking consensus among all correlation vectors. Our AiA module can be readily applied to both self-attention blocks and cross-attention blocks to facilitate feature aggregation and information propagation for visual tracking. Moreover, we propose a streamlined Transformer tracking framework, dubbed AiATrack, by introducing efficient feature reuse and target-background embeddings to make full use of temporal references. Experiments show that our tracker achieves state-of-the-art performance on six tracking benchmarks while running at a real-time speed.

</details>

### AvatarPoser: Articulated Full-Body Pose Tracking from Sparse Motion Sensing.
- **链接**: [arXiv:2207.13784](https://arxiv.org/abs/2207.13784) · 📚 被引 117
- **作者**: Jiaxi Jiang, Paul Streli, Huajian Qiu, Andreas Fender, Larissa Laich, Patrick Snape et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Today's Mixed Reality head-mounted displays track the user's head pose in world space as well as the user's hands for interaction in both Augmented Reality and Virtual Reality scenarios. While this is adequate to support user input, it unfortunately limits users' virtual representations to just their upper bodies. Current systems thus resort to floating avatars, whose limitation is particularly evident in collaborative settings. To estimate full-body poses from the sparse input sources, prior work has incorporated additional trackers and sensors at the pelvis or lower body, which increases setup complexity and limits practical application in mobile settings. In this paper, we present AvatarPoser, the first learning-based method that predicts full-body poses in world coordinates using only motion input from the user's head and hands. Our method builds on a Transformer encoder to extract deep features from the input signals and decouples global motion from the learned local joint orientations to guide pose estimation. To obtain accurate full-body motions that resemble motion capture animations, we refine the arm joints' positions using an optimization routine with inverse kinematics to match the original tracking input. In our evaluation, AvatarPoser achieved new state-of-the-art results in evaluations on large motion capture datasets (AMASS). At the same time, our method's inference speed supports real-time operation, providing a practical interface to support holistic avatar control and representation for Metaverse applications.

</details>

### Towards Sequence-Level Training for Visual Tracking.
- **链接**: [arXiv:2208.05810](https://arxiv.org/abs/2208.05810) · 📚 被引 42
- **作者**: Minji Kim, Seungkwan Lee, Jungseul Ok, Bohyung Han, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the extensive adoption of machine learning on the task of visual object tracking, recent learning-based approaches have largely overlooked the fact that visual tracking is a sequence-level task in its nature; they rely heavily on frame-level training, which inevitably induces inconsistency between training and testing in terms of both data distributions and task objectives. This work introduces a sequence-level training strategy for visual tracking based on reinforcement learning and discusses how a sequence-level design of data sampling, learning objectives, and data augmentation can improve the accuracy and robustness of tracking algorithms. Our experiments on standard benchmarks including LaSOT, TrackingNet, and GOT-10k demonstrate that four representative tracking models, SiamRPN++, SiamAttn, TransT, and TrDiMP, consistently improve by incorporating the proposed methods in training without modifying architectures.

</details>

### Robust Visual Tracking by Segmentation.
- **链接**: [arXiv:2203.11191](https://arxiv.org/abs/2203.11191)
- **作者**: Matthieu Paul, Martin Danelljan, Christoph Mayer, Luc Van Gool
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating the target extent poses a fundamental challenge in visual object tracking. Typically, trackers are box-centric and fully rely on a bounding box to define the target in the scene. In practice, objects often have complex shapes and are not aligned with the image axis. In these cases, bounding boxes do not provide an accurate description of the target and often contain a majority of background pixels. We propose a segmentation-centric tracking pipeline that not only produces a highly accurate segmentation mask, but also internally works with segmentation masks instead of bounding boxes. Thus, our tracker is able to better learn a target representation that clearly differentiates the target in the scene from background content. In order to achieve the necessary robustness for the challenging tracking scenario, we propose a separate instance localization component that is used to condition the segmentation decoder when producing the output mask. We infer a bounding box from the segmentation mask, validate our tracker on challenging tracking datasets and achieve the new state of the art on LaSOT with a success AUC score of 69.7%. Since most tracking datasets do not contain mask annotations, we cannot use them to evaluate predicted segmentation masks. Instead, we validate our segmentation quality on two popular video object segmentation datasets.

</details>

### Hierarchical Feature Embedding for Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_25)
- **作者**: Zhixiong Pi, Weitao Wan, Chong Sun, Changxin Gao, Nong Sang, Chen Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
