# 3D Detection — 2020 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 19 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Object as Hotspots: An Anchor-Free 3D Object Detection Approach via Firing of Hotspots.
- **链接**: [arXiv:1912.12791](https://arxiv.org/abs/1912.12791) · 📚 被引 132
- **作者**: Qi Chen, Lin Sun, Zhixin Wang, Kui Jia, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### DSGN: Deep Stereo Geometry Network for 3D Object Detection.
- **链接**: [arXiv:2001.03398](https://arxiv.org/abs/2001.03398) · [代码](https://github.com/chenyilun95/DSGN) · 📚 被引 179
- **作者**: Yilun Chen, Shu Liu, Xiaoyong Shen, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2020

> Accurate 3D object detection in LiDAR based point clouds suffers from the challenges of data sparsity and irregularities. Existing methods strive to organize the points regularly, e.g. voxelize, pass them through a designed 2D/3D neural network, and then define object-level anchors that predict offsets of 3D bounding boxes using collective evidences from all the points on the objects of interest. Contrary to the state-of-the-art anchor-based methods, based on the very nature of data sparsity, we observe that even points on an individual object part are informative about semantic information of the object. We thus argue in this paper for an approach opposite to existing methods using object-level anchors. Inspired by compositional models, which represent an object as parts and their spatial relations, we propose to represent an object as composition of its interior non-empty voxels, termed hotspots, and the spatial relations of hotspots. This gives rise to the representation of Object as Hotspots (OHS). Based on OHS, we further propose an anchor-free detection head with a novel ground truth assignment strategy that deals with inter-object point-sparsity imbalance to prevent the network from biasing towards objects with more points. Experimental results show that our proposed method works remarkably well on objects with a small number of points. Notably, our approach ranked 1st on KITTI 3D Detection Benchmark for cyclist and pedestrian detection, and achieved state-of-the-art performance on NuScenes 3D Detection Benchmark.

</details>

### A Hierarchical Graph Network for 3D Object Detection on Point Clouds.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_A_Hierarchical_Graph_Network_for_3D_Object_Detection_on_Point_CVPR_2020_paper.html) · 📚 被引 143
- **作者**: Jintai Chen, Biwen Lei, Qingyu Song, Haochao Ying, Danny Z. Chen, Jian Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### MonoPair: Monocular 3D Object Detection Using Pairwise Spatial Relationships.
- **链接**: [arXiv:2003.00504](https://arxiv.org/abs/2003.00504) · 📚 被引 285
- **作者**: Yongjian Chen, Lei Tai, Kai Sun, Mingyang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perceiving the physical world in 3D is fundamental for self-driving applications. Although temporal motion is an invaluable resource to human vision for detection, tracking, and depth perception, such features have not been thoroughly utilized in modern 3D object detectors. In this work, we propose a novel method for monocular video-based 3D object detection which carefully leverages kinematic motion to improve precision of 3D localization. Specifically, we first propose a novel decomposition of object orientation as well as a self-balancing 3D confidence. We show that both components are critical to enable our kinematic model to work effectively. Collectively, using only a single model, we efficiently leverage 3D kinematics from monocular videos to improve the overall localization precision in 3D object detection while also producing useful by-products of scene dynamics (ego-motion and per-object velocity). We achieve state-of-the-art performance on monocular 3D object detection and the Bird's Eye View tasks within the KITTI self-driving dataset.

### Learning Depth-Guided Convolutions for Monocular 3D Object Detection.
- **链接**: [arXiv:1912.04799](https://arxiv.org/abs/1912.04799) · [代码](https://github.com/dingmyu/D4LCN) · 📚 被引 210
- **作者**: Mingyu Ding, Yuqi Huo, Hongwei Yi, Zhe Wang, Jianping Shi, Zhiwu Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data augmentation has been widely adopted for object detection in 3D point clouds. However, all previous related efforts have focused on manually designing specific data augmentation methods for individual architectures. In this work, we present the first attempt to automate the design of data augmentation policies for 3D object detection. We introduce the Progressive Population Based Augmentation (PPBA) algorithm, which learns to optimize augmentation strategies by narrowing down the search space and adopting the best parameters discovered in previous iterations. On the KITTI 3D detection test set, PPBA improves the StarNet detector by substantial margins on the moderate difficulty category of cars, pedestrians, and cyclists, outperforming all current state-of-the-art single-stage detection models. Additional experiments on the Waymo Open Dataset indicate that PPBA continues to effectively improve the StarNet and PointPillars detectors on a 20x larger dataset compared to KITTI. The magnitude of the improvements may be comparable to advances in 3D perception architectures and the gains come without an incurred cost at inference time. In subsequent experiments, we find that PPBA may be up to 10x more data efficient than baseline 3D detection models without augmentation, highlighting that 3D detection models may achieve competitive accuracy with far fewer labeled examples.

</details>

### Finding Your (3D) Center: 3D Object Detection Using a Learned Loss.
- **链接**: [arXiv:2004.02693](https://arxiv.org/abs/2004.02693) · 📚 被引 7
- **作者**: David Griffiths, Jan Boehm, Tobias Ritschel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes.
- **链接**: [arXiv:2001.10692](https://arxiv.org/abs/2001.10692) · 📚 被引 258
- **作者**: Charles R. Qi, Xinlei Chen, Or Litany, Leonidas J. Guibas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects in 3D LiDAR data is a core technology for autonomous driving and other robotics applications. Although LiDAR data is acquired over time, most of the 3D object detection algorithms propose object bounding boxes independently for each frame and neglect the useful information available in the temporal domain. To address this problem, in this paper we propose a sparse LSTM-based multi-frame 3d object detection algorithm. We use a U-Net style 3D sparse convolution network to extract features for each frame's LiDAR point-cloud. These features are fed to the LSTM module together with the hidden and memory features from last frame to predict the 3d objects in the current frame as well as hidden and memory features that are passed to the next frame. Experiments on the Waymo Open Dataset show that our algorithm outperforms the traditional frame by frame approach by 7.5% mAP@0.7 and other multi-frame approaches by 1.2% while using less memory and computation per frame. To the best of our knowledge, this is the first work to use an LSTM for 3D object detection in sparse point clouds.

### End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection.
- **链接**: [arXiv:2004.03080](https://arxiv.org/abs/2004.03080) · [代码](https://github.com/mileyan/pseudo-LiDAR_e2e) · 📚 被引 168
- **作者**: Rui Qian, Divyansh Garg, Yan Wang, Yurong You, Serge J. Belongie, Bharath Hariharan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reliable and accurate 3D object detection is a necessity for safe autonomous driving. Although LiDAR sensors can provide accurate 3D point cloud estimates of the environment, they are also prohibitively expensive for many settings. Recently, the introduction of pseudo-LiDAR (PL) has led to a drastic reduction in the accuracy gap between methods based on LiDAR sensors and those based on cheap stereo cameras. PL combines state-of-the-art deep neural networks for 3D depth estimation with those for 3D object detection by converting 2D depth map outputs to 3D point cloud inputs. However, so far these two networks have to be trained separately. In this paper, we introduce a new framework based on differentiable Change of Representation (CoR) modules that allow the entire PL pipeline to be trained end-to-end. The resulting framework is compatible with most state-of-the-art networks for both tasks and in combination with PointRCNN improves over PL consistently across all benchmarks -- yielding the highest entry on the KITTI image-based 3D object detection leaderboard at the time of submission. Our code will be made available at https://github.com/mileyan/pseudo-LiDAR_e2e.

</details>

### PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection.
- **链接**: [arXiv:1912.13192](https://arxiv.org/abs/1912.13192) · [代码](https://github.com/open-mmlab/OpenPCDet) · 📚 被引 1987
- **作者**: Shaoshuai Shi, Chaoxu Guo, Li Jiang, Zhe Wang, Jianping Shi, Xiaogang Wang et al.
- **🏷️ 机构**: CUHK / Shanghai AI Lab, CUHK
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel and high-performance 3D object detection framework, named PointVoxel-RCNN (PV-RCNN), for accurate 3D object detection from point clouds. Our proposed method deeply integrates both 3D voxel Convolutional Neural Network (CNN) and PointNet-based set abstraction to learn more discriminative point cloud features. It takes advantages of efficient learning and high-quality proposals of the 3D voxel CNN and the flexible receptive fields of the PointNet-based networks. Specifically, the proposed framework summarizes the 3D scene with a 3D voxel CNN into a small set of keypoints via a novel voxel set abstraction module to save follow-up computations and also to encode representative scene features. Given the high-quality 3D proposals generated by the voxel CNN, the RoI-grid pooling is proposed to abstract proposal-specific features from the keypoints to the RoI-grid points via keypoint set abstraction with multiple receptive fields. Compared with conventional pooling operations, the RoI-grid feature points encode much richer context information for accurately estimating object confidences and locations. Extensive experiments on both the KITTI dataset and the Waymo Open dataset show that our proposed PV-RCNN surpasses state-of-the-art 3D detection methods with remarkable margins by using only point clouds. Code is available at https://github.com/open-mmlab/OpenPCDet.

</details>

### Point-GNN: Graph Neural Network for 3D Object Detection in a Point Cloud.
- **链接**: [arXiv:2003.01251](https://arxiv.org/abs/2003.01251) · [代码](https://github.com/WeijingShi/Point-GNN) · 📚 被引 845
- **作者**: Weijing Shi, Raj Rajkumar
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Weakly Supervised 3D Object Detection from Lidar Point Cloud.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58601-0_31)
- **作者**: Qinghao Meng, Wenguan Wang, Tianfei Zhou, Jianbing Shen, Luc Van Gool, Dengxin Dai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Distance-Normalized Unified Representation for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58526-6_6) · 📚 被引 41
- **作者**: Xuepeng Shi, Zhixiang Chen, Tae-Kyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Towards Generalization Across Depth for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58542-6_46) · 📚 被引 49
- **作者**: Andrea Simonelli, Samuel Rota Bulò, Lorenzo Porzi, Elisa Ricci, Peter Kontschieder
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### InfoFocus: 3D Object Detection for Autonomous Driving with Dynamic Information Modeling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58607-2_24)
- **作者**: Jun Wang, Shiyi Lan, Mingfei Gao, Larry S. Davis
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### 3DV: 3D Dynamic Voxel for Action Recognition in Depth Video.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wang_3DV_3D_Dynamic_Voxel_for_Action_Recognition_in_Depth_Video_CVPR_2020_paper.html)
- **作者**: Yancheng Wang, Yang Xiao, Fu Xiong, Wenxiang Jiang, Zhiguo Cao, Joey Tianyi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
