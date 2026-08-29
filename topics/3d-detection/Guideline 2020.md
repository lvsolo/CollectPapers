# 3D Detection — 2020 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 19 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Object as Hotspots: An Anchor-Free 3D Object Detection Approach via Firing of Hotspots.
- **链接**: [arXiv:1912.12791](https://arxiv.org/abs/1912.12791) · 📚 被引 132
- **作者**: Qi Chen, Lin Sun, Zhixin Wang, Kui Jia, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D object detection in LiDAR based point clouds suffers from the challenges of data sparsity and irregularities. Existing methods strive to organize the points regularly, e.g. voxelize, pass them through a designed 2D/3D neural network, and then define object-level anchors that predict offsets of 3D bounding boxes using collective evidences from all the points on the objects of interest. Contrary to the state-of-the-art anchor-based methods, based on the very nature of data sparsity, we observe that even points on an individual object part are informative about semantic information of the object. We thus argue in this paper for an approach opposite to existing methods using object-level anchors. Inspired by compositional models, which represent an object as parts and their spatial relations, we propose to represent an object as composition of its interior non-empty voxels, termed hotspots, and the spatial relations of hotspots. This gives rise to the representation of Object as Hotspots (OHS). Based on OHS, we further propose an anchor-free detection head with a novel ground truth assignment strategy that deals with inter-object point-sparsity imbalance to prevent the network from biasing towards objects with more points. Experimental results show that our proposed method works remarkably well on objects with a small number of points. Notably, our approach ranked 1st on KITTI 3D Detection Benchmark for cyclist and pedestrian detection, and achieved state-of-the-art performance on NuScenes 3D Detection Benchmark.

</details>

### Monocular Differentiable Rendering for Self-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_31)
- **作者**: Deniz Beker, Hiroharu Kato, Mihai Morariu, Takahiro Ando, Toru Matsuoka, Wadim Kehl et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Kinematic 3D Object Detection in Monocular Video.
- **链接**: [arXiv:2007.09548](https://arxiv.org/abs/2007.09548)
- **作者**: Garrick Brazil, Gerard Pons-Moll, Xiaoming Liu, Bernt Schiele
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perceiving the physical world in 3D is fundamental for self-driving applications. Although temporal motion is an invaluable resource to human vision for detection, tracking, and depth perception, such features have not been thoroughly utilized in modern 3D object detectors. In this work, we propose a novel method for monocular video-based 3D object detection which carefully leverages kinematic motion to improve precision of 3D localization. Specifically, we first propose a novel decomposition of object orientation as well as a self-balancing 3D confidence. We show that both components are critical to enable our kinematic model to work effectively. Collectively, using only a single model, we efficiently leverage 3D kinematics from monocular videos to improve the overall localization precision in 3D object detection while also producing useful by-products of scene dynamics (ego-motion and per-object velocity). We achieve state-of-the-art performance on monocular 3D object detection and the Bird's Eye View tasks within the KITTI self-driving dataset.

</details>

### Improving 3D Object Detection Through Progressive Population Based Augmentation.
- **链接**: [arXiv:2004.00831](https://arxiv.org/abs/2004.00831)
- **作者**: Shuyang Cheng, Zhaoqi Leng, Ekin Dogus Cubuk, Barret Zoph, Chunyan Bai, Jiquan Ngiam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data augmentation has been widely adopted for object detection in 3D point clouds. However, all previous related efforts have focused on manually designing specific data augmentation methods for individual architectures. In this work, we present the first attempt to automate the design of data augmentation policies for 3D object detection. We introduce the Progressive Population Based Augmentation (PPBA) algorithm, which learns to optimize augmentation strategies by narrowing down the search space and adopting the best parameters discovered in previous iterations. On the KITTI 3D detection test set, PPBA improves the StarNet detector by substantial margins on the moderate difficulty category of cars, pedestrians, and cyclists, outperforming all current state-of-the-art single-stage detection models. Additional experiments on the Waymo Open Dataset indicate that PPBA continues to effectively improve the StarNet and PointPillars detectors on a 20x larger dataset compared to KITTI. The magnitude of the improvements may be comparable to advances in 3D perception architectures and the gains come without an incurred cost at inference time. In subsequent experiments, we find that PPBA may be up to 10x more data efficient than baseline 3D detection models without augmentation, highlighting that 3D detection models may achieve competitive accuracy with far fewer labeled examples.

</details>

### Finding Your (3D) Center: 3D Object Detection Using a Learned Loss.
- **链接**: [arXiv:2004.02693](https://arxiv.org/abs/2004.02693) · 📚 被引 7
- **作者**: David Griffiths, Jan Boehm, Tobias Ritschel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Massive semantically labeled datasets are readily available for 2D images, however, are much harder to achieve for 3D scenes. Objects in 3D repositories like ShapeNet are labeled, but regrettably only in isolation, so without context. 3D scenes can be acquired by range scanners on city-level scale, but much fewer with semantic labels. Addressing this disparity, we introduce a new optimization procedure, which allows training for 3D detection with raw 3D scans while using as little as 5% of the object labels and still achieve comparable performance. Our optimization uses two networks. A scene network maps an entire 3D scene to a set of 3D object centers. As we assume the scene not to be labeled by centers, no classic loss, such as Chamfer can be used to train it. Instead, we use another network to emulate the loss. This loss network is trained on a small labeled subset and maps a non centered 3D object in the presence of distractions to its own center. This function is very similar - and hence can be used instead of - the gradient the supervised loss would provide. Our evaluation documents competitive fidelity at a much lower level of supervision, respectively higher quality at comparable supervision. Supplementary material can be found at: https://dgriffiths3.github.io.

</details>

### EPNet: Enhancing Point Features with Image Semantics for 3D Object Detection.
- **链接**: [arXiv:2007.08856](https://arxiv.org/abs/2007.08856) · [代码](https://github.com/happinesslz/EPNet) · 📚 被引 437
- **作者**: Tengteng Huang, Zhe Liu, Xiwu Chen, Xiang Bai
- **🏷️ 机构**: HUAST
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we aim at addressing two critical issues in the 3D detection task, including the exploitation of multiple sensors~(namely LiDAR point cloud and camera image), as well as the inconsistency between the localization and classification confidence. To this end, we propose a novel fusion module to enhance the point features with semantic image features in a point-wise manner without any image annotations. Besides, a consistency enforcing loss is employed to explicitly encourage the consistency of both the localization and classification confidence. We design an end-to-end learnable framework named EPNet to integrate these two components. Extensive experiments on the KITTI and SUN-RGBD datasets demonstrate the superiority of EPNet over the state-of-the-art methods. Codes and models are available at: \url{https://github.com/happinesslz/EPNet}.

</details>

### An LSTM Approach to Temporal 3D Object Detection in LiDAR Point Clouds.
- **链接**: [arXiv:2007.12392](https://arxiv.org/abs/2007.12392) · 📚 被引 74
- **作者**: Rui Huang, Wanyue Zhang, Abhijit Kundu, Caroline Pantofaru, David A. Ross, Thomas A. Funkhouser et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects in 3D LiDAR data is a core technology for autonomous driving and other robotics applications. Although LiDAR data is acquired over time, most of the 3D object detection algorithms propose object bounding boxes independently for each frame and neglect the useful information available in the temporal domain. To address this problem, in this paper we propose a sparse LSTM-based multi-frame 3d object detection algorithm. We use a U-Net style 3D sparse convolution network to extract features for each frame's LiDAR point-cloud. These features are fed to the LSTM module together with the hidden and memory features from last frame to predict the 3d objects in the current frame as well as hidden and memory features that are passed to the next frame. Experiments on the Waymo Open Dataset show that our algorithm outperforms the traditional frame by frame approach by 7.5% mAP@0.7 and other multi-frame approaches by 1.2% while using less memory and computation per frame. To the best of our knowledge, this is the first work to use an LSTM for 3D object detection in sparse point clouds.

</details>

### RTM3D: Real-Time Monocular 3D Detection from Object Keypoints for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58580-8_38)
- **作者**: Peixuan Li, Huaici Zhao, Pengfei Liu, Feidao Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Reinforced Axial Refinement Network for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58520-4_32) · 📚 被引 17
- **作者**: Lijie Liu, Chufan Wu, Jiwen Lu, Lingxi Xie, Jie Zhou, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Weakly Supervised 3D Object Detection from Lidar Point Cloud.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58601-0_31)
- **作者**: Qinghao Meng, Wenguan Wang, Tianfei Zhou, Jianbing Shen, Luc Van Gool, Dengxin Dai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Distance-Normalized Unified Representation for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58526-6_6) · 📚 被引 41
- **作者**: Xuepeng Shi, Zhixiang Chen, Tae-Kyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Towards Generalization Across Depth for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58542-6_46) · 📚 被引 49
- **作者**: Andrea Simonelli, Samuel Rota Bulò, Lorenzo Porzi, Elisa Ricci, Peter Kontschieder
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### InfoFocus: 3D Object Detection for Autonomous Driving with Dynamic Information Modeling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58607-2_24)
- **作者**: Jun Wang, Shiyi Lan, Mingfei Gao, Larry S. Davis
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Monocular 3D Object Detection via Feature Domain Adaptation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58545-7_2) · 📚 被引 29
- **作者**: Xiaoqing Ye, Liang Du, Yifeng Shi, Yingying Li, Xiao Tan, Jianfeng Feng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### 3D-CVF: Generating Joint Camera and LiDAR Features Using Cross-view Spatial Feature Fusion for 3D Object Detection.
- **链接**: [arXiv:2004.12636](https://arxiv.org/abs/2004.12636) · 📚 被引 425
- **作者**: Jin Hyeok Yoo, Yecheol Kim, Ji Song Kim, Jun Won Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a new deep architecture for fusing camera and LiDAR sensors for 3D object detection. Because the camera and LiDAR sensor signals have different characteristics and distributions, fusing these two modalities is expected to improve both the accuracy and robustness of 3D object detection. One of the challenges presented by the fusion of cameras and LiDAR is that the spatial feature maps obtained from each modality are represented by significantly different views in the camera and world coordinates; hence, it is not an easy task to combine two heterogeneous feature maps without loss of information. To address this problem, we propose a method called 3D-CVF that combines the camera and LiDAR features using the cross-view spatial feature fusion strategy. First, the method employs auto-calibrated projection, to transform the 2D camera features to a smooth spatial feature map with the highest correspondence to the LiDAR features in the bird's eye view (BEV) domain. Then, a gated feature fusion network is applied to use the spatial attention maps to mix the camera and LiDAR features appropriately according to the region. Next, camera-LiDAR feature fusion is also achieved in the subsequent proposal refinement stage. The camera feature is used from the 2D camera-view domain via 3D RoI grid pooling and fused with the BEV feature for proposal refinement. Our evaluations, conducted on the KITTI and nuScenes 3D object detection datasets demonstrate that the camera-LiDAR fusion offers significant performance gain over single modality and that the proposed 3D-CVF achieves state-of-the-art performance in the KITTI benchmark.

</details>

### H3DNet: 3D Object Detection Using Hybrid Geometric Primitives.
- **链接**: [arXiv:2006.05682](https://arxiv.org/abs/2006.05682) · 📚 被引 151
- **作者**: Zaiwei Zhang, Bo Sun, Haitao Yang, Qixing Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce H3DNet, which takes a colorless 3D point cloud as input and outputs a collection of oriented object bounding boxes (or BB) and their semantic labels. The critical idea of H3DNet is to predict a hybrid set of geometric primitives, i.e., BB centers, BB face centers, and BB edge centers. We show how to convert the predicted geometric primitives into object proposals by defining a distance function between an object and the geometric primitives. This distance function enables continuous optimization of object proposals, and its local minimums provide high-fidelity object proposals. H3DNet then utilizes a matching and refinement module to classify object proposals into detected objects and fine-tune the geometric parameters of the detected objects. The hybrid set of geometric primitives not only provides more accurate signals for object detection than using a single type of geometric primitives, but it also provides an overcomplete set of constraints on the resulting 3D layout. Therefore, H3DNet can tolerate outliers in predicted geometric primitives. Our model achieves state-of-the-art 3D detection results on two large datasets with real 3D scans, ScanNet and SUN RGB-D.

</details>

### Rotation-Robust Intersection over Union for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58565-5_28) · 📚 被引 37
- **作者**: Yu Zheng, Danyang Zhang, Sinan Xie, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Self-Supervised Monocular 3D Face Reconstruction by Occlusion-Aware Multi-view Geometry Consistency.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58555-6_4)
- **作者**: Jiaxiang Shang, Tianwei Shen, Shiwei Li, Lei Zhou, Mingmin Zhen, Tian Fang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### VoxelPose: Towards Multi-camera 3D Human Pose Estimation in Wild Environment.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58452-8_12)
- **作者**: Hanyue Tu, Chunyu Wang, Wenjun Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
