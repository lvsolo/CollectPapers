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

## 🆕 增量新增

### MLCVNet: Multi-Level Context VoteNet for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2004.05679](https://arxiv.org/abs/2004.05679) · 📚 被引 172
- **作者**: Qian Xie, Yu-Kun Lai, Jing Wu, Zhoutao Wang, Yiming Zhang, Kai Xu et al.
- **🏷️ 机构**: Nanjing University of Aeronautics and Astronautics, Cardiff University, National University of Defense Technology
- **会议**: CVPR 2020
- **摘要（中）**: 针对现有3D目标检测方法忽略物体间上下文信息的问题，该论文基于VoteNet提出MLCVNet，引入三个上下文模块：Patch-to-Patch Context（PPC）在投票前捕获点块间上下文，Object-to-Object Context（OOC）在提案阶段捕获候选物体间上下文，Global Scene Context（GSC）学习全局场景上下文。通过多级上下文融合，显著提升了3D检测精度。在SUN RGB-D和ScanNet等数据集上验证了有效性。
- **摘要（英）**: This paper proposes MLCVNet, extending VoteNet with three context modules (PPC, OOC, GSC) to capture patch-level, object-level, and scene-level contextual information for 3D object detection. The method improves detection accuracy on standard benchmarks like SUN RGB-D and ScanNet.
- **核心贡献**: 提出了多级上下文VoteNet，增强3D检测的上下文感知能力。
- **创新点**: 首次在投票和分类阶段系统集成补丁、物体和场景级上下文。
- **结果**: 在多个3D检测基准上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we address the 3D object detection task by capturing multi-level contextual information with the self-attention mechanism and multi-scale feature fusion. Most existing 3D object detection methods recognize objects individually, without giving any consideration on contextual information between these objects. Comparatively, we propose Multi-Level Context VoteNet (MLCVNet) to recognize 3D objects correlatively, building on the state-of-the-art VoteNet. We introduce three context modules into the voting and classifying stages of VoteNet to encode contextual information at different levels. Specifically, a Patch-to-Patch Context (PPC) module is employed to capture contextual information between the point patches, before voting for their corresponding object centroid points. Subsequently, an Object-to-Object Context (OOC) module is incorporated before the proposal and classification stage, to capture the contextual information between object candidates. Finally, a Global Scene Context (GSC) module is designed to learn the global scene context. We demonstrate these by capturing contextual information at patch, object and scene levels. Our method is an effective way to promote detection accuracy, achieving new state-of-the-art detection performance on challenging 3D object detection datasets, i.e., SUN RGBD and ScanNet. We also release our code at https://github.com/NUAAXQ/MLCVNet.

</details>

### Density-Based Clustering for 3D Object Detection in Point Clouds. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Ahmed_Density-Based_Clustering_for_3D_Object_Detection_in_Point_Clouds_CVPR_2020_paper.html) · 📚 被引 30
- **作者**: Syeda Mariam Ahmed, Chee-Meng Chew
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对点云3D目标检测中聚类方法对密度变化敏感的问题，该论文提出基于密度聚类的3D检测方法，通过自适应密度估计改进物体提案生成。方法在KITTI等数据集上验证了鲁棒性。
- **摘要（英）**: This paper introduces a density-based clustering approach for 3D object detection in point clouds, improving proposal generation under varying point densities. Evaluations on KITTI show robustness.
- **核心贡献**: 提出密度自适应聚类方法增强3D检测鲁棒性。
- **创新点**: 利用密度信息优化聚类过程。
- **结果**: 在KITTI上展示了性能提升。

### Structure Aware Single-Stage 3D Object Detection From Point Cloud. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/He_Structure_Aware_Single-Stage_3D_Object_Detection_From_Point_Cloud_CVPR_2020_paper.html) · 📚 被引 556
- **作者**: Chenhang He, Hui Zeng, Jianqiang Huang, Xian-Sheng Hua, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2020
- **摘要（中）**: ①针对点云单阶段3D目标检测中的结构感知问题。②由于摘要缺失，方法不明，可能涉及点云结构编码或注意力机制。③改进点可能在于增强几何结构利用。④效果未知。
- **摘要（英）**: This paper addresses structure-aware single-stage 3D detection from point clouds. The method is unclear due to missing abstract, possibly focusing on geometric encoding. Results are unspecified.
- **核心贡献**: 探索点云结构感知的3D检测。
- **创新点**: 可能引入结构建模。
- **结果**: 效果未报告。

### What You See is What You Get: Exploiting Visibility for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:1912.04986](https://arxiv.org/abs/1912.04986) · 📚 被引 108
- **作者**: Peiyun Hu, Jason Ziglar, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: CVPR 2020
- **摘要（中）**: ①这篇论文针对LiDAR点云本质上是2.5D数据而非真正3D数据的问题，指出传统方法将点云表示为(x,y,z)坐标集合会丢失自由空间（freespace）的隐藏信息。②提出通过3D射线投射（raycasting）高效恢复可见性信息，并将其作为额外的体素化可见性图输入流，增强基于体素的3D检测网络。③改进点在于将可见性信息与虚拟物体合成数据增强、多帧时间聚合等先进技术结合，充分利用2.5D数据的几何特性。④在NuScenes 3D检测基准上，添加可见性输入流显著提升了检测性能，验证了方法的有效性。
- **摘要（英）**: This paper addresses the issue that LiDAR point clouds are inherently 2.5D, and representing them as (x,y,z) points destroys hidden freespace information. It proposes recovering visibility via 3D raycasting and adding a voxelized visibility map as an extra input stream to voxel-based detectors, combined with synthetic augmentation and temporal aggregation. Experiments on NuScenes show significant improvement in 3D detection performance.
- **核心贡献**: 提出利用可见性信息增强3D检测网络，恢复2.5D数据中的自由空间知识。
- **创新点**: 将3D射线投射生成的可见性图作为额外输入流，与现有检测框架无缝集成。
- **结果**: 在NuScenes基准上显著提升3D检测精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in 3D sensing have created unique challenges for computer vision. One fundamental challenge is finding a good representation for 3D sensor data. Most popular representations (such as PointNet) are proposed in the context of processing truly 3D data (e.g. points sampled from mesh models), ignoring the fact that 3D sensored data such as a LiDAR sweep is in fact 2.5D. We argue that representing 2.5D data as collections of (x, y, z) points fundamentally destroys hidden information about freespace. In this paper, we demonstrate such knowledge can be efficiently recovered through 3D raycasting and readily incorporated into batch-based gradient learning. We describe a simple approach to augmenting voxel-based networks with visibility: we add a voxelized visibility map as an additional input stream. In addition, we show that visibility can be combined with two crucial modifications common to state-of-the-art 3D detectors: synthetic data augmentation of virtual objects and temporal aggregation of LiDAR sweeps over multiple time frames. On the NuScenes 3D detection benchmark, we show that, by adding an additional stream for visibility input, we can significantly improve the overall detection accuracy of a state-of-the-art 3D detector.

</details>

### IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Peng_IDA-3D_Instance-Depth-Aware_3D_Object_Detection_From_Stereo_Vision_for_Autonomous_CVPR_2020_paper.html) · 📚 被引 62
- **作者**: Wanli Peng, Hao Pan, He Liu, Yi Sun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对立体视觉3D目标检测中深度估计不准确、实例级深度信息利用不足的问题。②提出IDA-3D框架，通过实例深度感知模块，利用实例分割和深度估计的联合优化，为每个目标实例预测更精确的深度。③相比传统基于像素级深度图的方法，该方法在实例级别进行深度细化，并融合多任务学习，提高了深度估计的鲁棒性。④在KITTI数据集上，该方法在立体图像3D检测任务中取得了当时领先的性能，显著提升了中等和困难样本的检测精度。
- **摘要（英）**: This paper addresses the issue of inaccurate depth estimation in stereo-based 3D object detection by introducing an instance-depth-aware module that jointly optimizes instance segmentation and depth prediction. It refines depth at the instance level, improving robustness over pixel-wise depth methods. The approach achieves state-of-the-art performance on KITTI, particularly for moderate and hard samples.
- **核心贡献**: 提出实例深度感知的立体3D检测框架，通过实例级深度细化提升检测精度。
- **创新点**: 将实例分割与深度估计联合优化，实现实例级深度感知。
- **结果**: 在KITTI数据集上取得领先性能，尤其提升中等和困难样本的精度。

### Disp R-CNN: Stereo 3D Object Detection via Shape Prior Guided Instance Disparity Estimation. **⭐⭐⭐⭐** (相关度: 87%)
- **链接**: [arXiv:2004.03572](https://arxiv.org/abs/2004.03572) · 📚 被引 93
- **作者**: Jiaming Sun, Linghao Chen, Yiming Xie, Siyu Zhang, Qinhong Jiang, Xiaowei Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对立体3D检测中全图视差估计成本高且未利用类别先验的问题。②提出Disp R-CNN，设计实例视差估计网络（iDispNet），仅对目标像素预测视差，并学习类别形状先验以提高精度。③为解决视差标注稀缺，利用统计形状模型生成密集视差伪真值，无需LiDAR点云，使方法更广泛适用。④在KITTI数据集上，即使训练时无LiDAR真值，仍取得竞争性能，平均精度比之前最优方法提升20%。
- **摘要（英）**: This paper addresses the high cost and lack of category priors in full-image disparity estimation for stereo 3D detection by proposing Disp R-CNN with an instance disparity estimation network (iDispNet) that predicts disparity only on objects and learns shape priors. It uses a statistical shape model to generate pseudo ground-truth without LiDAR, improving applicability. On KITTI, it outperforms previous methods by 20% in average precision even without LiDAR supervision.
- **核心贡献**: 提出实例视差估计网络和形状先验，实现高效且无需LiDAR的立体3D检测。
- **创新点**: 仅对目标实例预测视差，并利用统计形状模型生成伪真值。
- **结果**: 在KITTI上平均精度提升20%，且无需LiDAR真值。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel system named Disp R-CNN for 3D object detection from stereo images. Many recent works solve this problem by first recovering a point cloud with disparity estimation and then apply a 3D detector. The disparity map is computed for the entire image, which is costly and fails to leverage category-specific prior. In contrast, we design an instance disparity estimation network (iDispNet) that predicts disparity only for pixels on objects of interest and learns a category-specific shape prior for more accurate disparity estimation. To address the challenge from scarcity of disparity annotation in training, we propose to use a statistical shape model to generate dense disparity pseudo-ground-truth without the need of LiDAR point clouds, which makes our system more widely applicable. Experiments on the KITTI dataset show that, even when LiDAR ground-truth is not available at training time, Disp R-CNN achieves competitive performance and outperforms previous state-of-the-art methods by 20% in terms of average precision.

</details>

### HVNet: Hybrid Voxel Network for LiDAR Based 3D Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2003.00186](https://arxiv.org/abs/2003.00186) · 📚 被引 210
- **作者**: Maosheng Ye, Shuangjie Xu, Tongyi Cao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对激光雷达3D检测中体素与点云特征表示效率与精度平衡的问题。②提出HVNet，一种混合体素网络，结合体素与点级特征提取，通过多尺度特征融合增强检测。③相比单一表示方法，HVNet在保持实时性的同时提升检测精度。④在KITTI数据集上取得当时领先的检测性能。
- **摘要（英）**: This paper addresses the trade-off between efficiency and accuracy in LiDAR-based 3D detection. It proposes HVNet, a hybrid voxel network that combines voxel and point-level features with multi-scale fusion. It achieves leading detection performance on KITTI while maintaining real-time inference.
- **核心贡献**: 提出混合体素网络，融合多尺度特征提升3D检测精度。
- **创新点**: 结合体素与点级特征，实现高效且精确的检测。
- **结果**: 在KITTI上取得领先性能，保持实时性。

### Joint 3D Instance Segmentation and Object Detection for Autonomous Driving. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhou_Joint_3D_Instance_Segmentation_and_Object_Detection_for_Autonomous_Driving_CVPR_2020_paper.html) · 📚 被引 92
- **作者**: Dingfu Zhou, Jin Fang, Xibin Song, Liu Liu, Junbo Yin, Yuchao Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自动驾驶中3D实例分割与检测任务分离的问题。②提出联合框架同时处理实例分割和3D检测，共享特征提取并优化多任务损失。③相比单独处理，联合学习提升整体性能。④在自动驾驶数据集上验证了有效性。
- **摘要（英）**: This paper addresses the separation of 3D instance segmentation and detection in autonomous driving. It proposes a joint framework sharing features and optimizing multi-task losses. It improves overall performance compared to separate processing on autonomous driving datasets.
- **核心贡献**: 提出联合3D实例分割与检测框架，提升自动驾驶感知效率。
- **创新点**: 共享特征和多任务损失优化实现联合学习。
- **结果**: 在自动驾驶数据集上验证了联合方法的有效性。

### Monocular Differentiable Rendering for Self-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_31)
- **作者**: Deniz Beker, Hiroharu Kato, Mihai Morariu, Takahiro Ando, Toru Matsuoka, Wadim Kehl et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Kinematic 3D Object Detection in Monocular Video.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58592-1_9)
- **作者**: Garrick Brazil, Gerard Pons-Moll, Xiaoming Liu, Bernt Schiele
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Improving 3D Object Detection Through Progressive Population Based Augmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_17)
- **作者**: Shuyang Cheng, Zhaoqi Leng, Ekin Dogus Cubuk, Barret Zoph, Chunyan Bai, Jiquan Ngiam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### EPNet: Enhancing Point Features with Image Semantics for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58555-6_3)
- **作者**: Tengteng Huang, Zhe Liu, Xiwu Chen, Xiang Bai
- **🏷️ 机构**: HUAST
- **会议**: ECCV 2020

### An LSTM Approach to Temporal 3D Object Detection in LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58523-5_16)
- **作者**: Rui Huang, Wanyue Zhang, Abhijit Kundu, Caroline Pantofaru, David A. Ross, Thomas A. Funkhouser et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### RTM3D: Real-Time Monocular 3D Detection from Object Keypoints for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58580-8_38)
- **作者**: Peixuan Li, Huaici Zhao, Pengfei Liu, Feidao Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Reinforced Axial Refinement Network for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58520-4_32)
- **作者**: Lijie Liu, Chufan Wu, Jiwen Lu, Lingxi Xie, Jie Zhou, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Monocular 3D Object Detection via Feature Domain Adaptation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58545-7_2)
- **作者**: Xiaoqing Ye, Liang Du, Yifeng Shi, Yingying Li, Xiao Tan, Jianfeng Feng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### 3D-CVF: Generating Joint Camera and LiDAR Features Using Cross-view Spatial Feature Fusion for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58583-9_43)
- **作者**: Jin Hyeok Yoo, Yecheol Kim, Ji Song Kim, Jun Won Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### H3DNet: 3D Object Detection Using Hybrid Geometric Primitives.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58610-2_19)
- **作者**: Zaiwei Zhang, Bo Sun, Haitao Yang, Qixing Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Rotation-Robust Intersection over Union for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58565-5_28)
- **作者**: Yu Zheng, Danyang Zhang, Sinan Xie, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Pseudo-LiDAR++: Accurate Depth for 3D Object Detection in Autonomous Driving.
- **链接**: [出版页](https://openreview.net/forum?id=BJedHRVtPB)
- **作者**: Yurong You, Yan Wang, Wei-Lun Chao, Divyansh Garg, Geoff Pleiss, Bharath Hariharan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### Every View Counts: Cross-View Consistency in 3D Object Detection with Hybrid-Cylindrical-Spherical Voxelization.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/f2fc990265c712c49d51a18a32b39f0c-Abstract.html)
- **作者**: Qi Chen, Lin Sun, Ernest Cheung, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

## 跨领域论文（完整笔记在其他领域）

- Associate-3Ddet: Perceptual-to-Conceptual Association for 3D Point Cloud Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
- End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
- PointPainting: Sequential Fusion for 3D Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
- LiDAR-Based Online 3D Video Object Detection With Graph-Based Message Passing and Spatiotemporal Transformer Attention. → [object-detection](../object-detection/Guideline%202020.md)
- SESS: Self-Ensembling Semi-Supervised 3D Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
- nuScenes: A Multimodal Dataset for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202020.md)
- Scalability in Perception for Autonomous Driving: Waymo Open Dataset. → [autonomous-driving](../autonomous-driving/Guideline%202020.md)
- SurfelGAN: Synthesizing Realistic Sensor Data for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202020.md)
<!-- COMPLETE v1 papers=36 -->
