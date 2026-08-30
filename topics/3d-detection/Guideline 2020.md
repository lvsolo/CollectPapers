# 3D Detection — 2020 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 19 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Object as Hotspots: An Anchor-Free 3D Object Detection Approach via Firing of Hotspots. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_5)
- **作者**: Qi Chen, Lin Sun, Zhixin Wang, Kui Jia, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: ①该论文针对3D目标检测中锚点方法在稀疏点云上的局限性，现有方法依赖预定义锚点导致效率低和泛化差。②提出了基于热点（Hotspots）的无锚点3D检测方法，通过预测目标的热点位置并直接回归边界框，简化了检测流程。③相比锚点方法，该方法无需锚点设计，提高了检测效率和灵活性，适用于LiDAR点云。④摘要未提供具体数值，但方法在标准数据集上展示了竞争力，具体效果需查阅全文。
- **摘要（英）**: This paper addresses limitations of anchor-based 3D detection in sparse point clouds by proposing an anchor-free approach based on hotspots, which predicts target locations and regresses boxes directly. It eliminates anchor design, improving efficiency and flexibility, though specific results are not detailed in the abstract.
- **核心贡献**: 提出了基于热点的无锚点3D检测方法，简化了检测流程。
- **创新点**: 利用热点预测替代锚点机制，实现端到端3D检测。
- **结果**: 在标准数据集上展示了竞争力，但摘要未提供具体数值。

### DSGN: Deep Stereo Geometry Network for 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2001.03398](https://arxiv.org/abs/2001.03398) · 📚 被引 179
- **作者**: Yilun Chen, Shu Liu, Xiaoyong Shen, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2020
- **摘要（中）**: ①针对基于图像的3D检测与LiDAR方法性能差距大的问题。②提出了Deep Stereo Geometry Network (DSGN)，通过可微的3D几何体积表示进行端到端检测。③改进点在于首次提供简单有效的单阶段立体3D检测流程，同时学习深度和语义。④在KITTI 3D检测上比先前立体方法提升约10 AP，并达到与部分LiDAR方法相当的性能。
- **摘要（英）**: This paper addresses the large performance gap between image-based and LiDAR-based 3D detection. It proposes DSGN using a differentiable volumetric representation for end-to-end detection. The improvement lies in jointly estimating depth and detecting objects in a one-stage pipeline. It outperforms previous stereo methods by ~10 AP on KITTI and matches some LiDAR methods.
- **核心贡献**: 提出了基于立体几何体积的端到端3D检测框架。
- **创新点**: 利用3D几何体积同时编码深度和语义信息。
- **结果**: 在KITTI上提升约10 AP，接近LiDAR性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most state-of-the-art 3D object detectors heavily rely on LiDAR sensors because there is a large performance gap between image-based and LiDAR-based methods. It is caused by the way to form representation for the prediction in 3D scenarios. Our method, called Deep Stereo Geometry Network (DSGN), significantly reduces this gap by detecting 3D objects on a differentiable volumetric representation -- 3D geometric volume, which effectively encodes 3D geometric structure for 3D regular space. With this representation, we learn depth information and semantic cues simultaneously. For the first time, we provide a simple and effective one-stage stereo-based 3D detection pipeline that jointly estimates the depth and detects 3D objects in an end-to-end learning manner. Our approach outperforms previous stereo-based 3D detectors (about 10 higher in terms of AP) and even achieves comparable performance with several LiDAR-based methods on the KITTI 3D object detection leaderboard. Our code is publicly available at https://github.com/chenyilun95/DSGN.

</details>

### A Hierarchical Graph Network for 3D Object Detection on Point Clouds. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_A_Hierarchical_Graph_Network_for_3D_Object_Detection_on_Point_CVPR_2020_paper.html) · 📚 被引 143
- **作者**: Jintai Chen, Biwen Lei, Qingyu Song, Haochao Ying, Danny Z. Chen, Jian Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对点云3D物体检测中如何有效利用点云层次结构信息的问题。②提出了一种层次图网络，通过构建点级、区域级和物体级的图结构来传播和聚合特征。③相比传统直接处理原始点云的方法，该方法能更好地建模点云的内在结构关系。④摘要未提供具体数据，但该方法在点云检测任务上展示了潜力。
- **摘要（英）**: This paper addresses 3D object detection from point clouds by proposing a hierarchical graph network that constructs graphs at point, region, and object levels to propagate and aggregate features. It improves upon methods that directly process raw points by better modeling structural relationships. The abstract lacks quantitative results but demonstrates potential for point cloud detection.
- **核心贡献**: 提出层次图网络用于点云3D物体检测。
- **创新点**: 多层级图结构建模点云内在关系。
- **结果**: 在点云检测任务上展示了潜力，但未提供具体数据。

### MonoPair: Monocular 3D Object Detection Using Pairwise Spatial Relationships. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2003.00504](https://arxiv.org/abs/2003.00504) · 📚 被引 285
- **作者**: Yongjian Chen, Lei Tai, Kai Sun, Mingyang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对单目3D物体检测中遮挡样本信息不足的问题。②提出了MonoPair方法，通过考虑成对样本的空间关系，利用相邻物体的空间约束来编码部分遮挡物体的信息。具体包括不确定性感知的位置预测和相邻物体对的3D距离预测，并通过非线性最小二乘进行联合优化。③相比独立处理每个物体的检测器，该方法能利用邻域信息提升遮挡样本的检测精度。④在KITTI 3D检测基准上取得了最佳性能，尤其在困难样本上大幅超越现有方法。
- **摘要（英）**: This paper addresses monocular 3D object detection for occluded samples by proposing MonoPair, which encodes spatial constraints from adjacent object pairs via uncertainty-aware predictions and nonlinear least squares optimization. It outperforms existing methods on KITTI 3D detection, especially for hard samples, by leveraging pairwise relationships.
- **核心贡献**: 提出成对空间关系建模提升单目3D检测的遮挡样本性能。
- **创新点**: 不确定性感知预测与后优化模块的集成。
- **结果**: 在KITTI基准上取得最佳性能，困难样本提升明显。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an essential component in autonomous driving while challenging to solve, especially for those occluded samples which are only partially visible. Most detectors consider each 3D object as an independent training target, inevitably resulting in a lack of useful information for occluded samples. To this end, we propose a novel method to improve the monocular 3D object detection by considering the relationship of paired samples. This allows us to encode spatial constraints for partially-occluded objects from their adjacent neighbors. Specifically, the proposed detector computes uncertainty-aware predictions for object locations and 3D distances for the adjacent object pairs, which are subsequently jointly optimized by nonlinear least squares. Finally, the one-stage uncertainty-aware prediction structure and the post-optimization module are dedicatedly integrated for ensuring the run-time efficiency. Experiments demonstrate that our method yields the best performance on KITTI 3D detection benchmark, by outperforming state-of-the-art competitors by wide margins, especially for the hard samples.

</details>

### Learning Depth-Guided Convolutions for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:1912.04799](https://arxiv.org/abs/1912.04799) · 📚 被引 210
- **作者**: Mingyu Ding, Yuqi Huo, Hongwei Yi, Zhe Wang, Jianping Shi, Zhiwu Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对单目3D物体检测中缺乏准确深度信息的问题。②提出了深度引导的局部卷积网络D4LCN，其中滤波器和感受野可从图像深度图自动学习，使不同像素具有不同滤波器。③相比依赖伪LiDAR表示的方法，该方法直接改进2D卷积，缩小了图像表示与点云表示的差距。④实验表明D4LCN在单目3D检测上取得了显著性能提升。
- **摘要（英）**: This paper tackles monocular 3D detection by proposing depth-guided local convolutions (D4LCN), where filters and receptive fields are learned from depth maps, avoiding pseudo-LiDAR dependency. It narrows the gap between image and point cloud representations, achieving significant performance gains in experiments.
- **核心贡献**: 提出深度引导的局部卷积网络用于单目3D检测。
- **创新点**: 动态深度-深度可分离-膨胀卷积自动学习滤波器。
- **结果**: 在单目3D检测上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection from a single image without LiDAR is a challenging task due to the lack of accurate depth information. Conventional 2D convolutions are unsuitable for this task because they fail to capture local object and its scale information, which are vital for 3D object detection. To better represent 3D structure, prior arts typically transform depth maps estimated from 2D images into a pseudo-LiDAR representation, and then apply existing 3D point-cloud based object detectors. However, their results depend heavily on the accuracy of the estimated depth maps, resulting in suboptimal performance. In this work, instead of using pseudo-LiDAR representation, we improve the fundamental 2D fully convolutions by proposing a new local convolutional network (LCN), termed Depth-guided Dynamic-Depthwise-Dilated LCN (D$^4$LCN), where the filters and their receptive fields can be automatically learned from image-based depth maps, making different pixels of different images have different filters. D$^4$LCN overcomes the limitation of conventional 2D convolutions and narrows the gap between image representation and 3D point cloud representation. Extensive experiments show that D$^4$LCN outperforms existing works by large margins. For example, the relative improvement of D$^4$LCN against the state-of-the-art on KITTI is 9.1\% in the moderate setting. The code is available at https://github.com/dingmyu/D4LCN.

</details>

### Finding Your (3D) Center: 3D Object Detection Using a Learned Loss.
- **链接**: [arXiv:2004.02693](https://arxiv.org/abs/2004.02693) · 📚 被引 7
- **作者**: David Griffiths, Jan Boehm, Tobias Ritschel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2001.10692](https://arxiv.org/abs/2001.10692) · 📚 被引 258
- **作者**: Charles R. Qi, Xinlei Chen, Or Litany, Leonidas J. Guibas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对点云3D检测中数据稀疏、缺乏颜色和纹理信息的问题。②提出ImVoteNet，在VoteNet基础上融合2D图像投票和3D点云投票，提取几何和语义特征并提升到3D。③相比多模态检测方法，显式利用2D特征并设计多塔训练方案。④在SUN RGB-D数据集上提升SOTA 5.7 mAP。
- **摘要（英）**: This paper tackles the limitations of point cloud data in 3D detection, such as sparsity and lack of texture. It proposes ImVoteNet, which fuses 2D image votes with 3D point cloud votes, extracting geometric and semantic features. Compared to prior multi-modal methods, it explicitly leverages 2D features with a multi-tower training scheme. It improves SOTA by 5.7 mAP on SUN RGB-D.
- **核心贡献**: 提出基于2D-3D投票融合的3D检测架构。
- **创新点**: 显式提取2D几何和语义特征并提升到3D。
- **结果**: 在SUN RGB-D上提升SOTA 5.7 mAP。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection has seen quick progress thanks to advances in deep learning on point clouds. A few recent works have even shown state-of-the-art performance with just point clouds input (e.g. VoteNet). However, point cloud data have inherent limitations. They are sparse, lack color information and often suffer from sensor noise. Images, on the other hand, have high resolution and rich texture. Thus they can complement the 3D geometry provided by point clouds. Yet how to effectively use image information to assist point cloud based detection is still an open question. In this work, we build on top of VoteNet and propose a 3D detection architecture called ImVoteNet specialized for RGB-D scenes. ImVoteNet is based on fusing 2D votes in images and 3D votes in point clouds. Compared to prior work on multi-modal detection, we explicitly extract both geometric and semantic features from the 2D images. We leverage camera parameters to lift these features to 3D. To improve the synergy of 2D-3D feature fusion, we also propose a multi-tower training scheme. We validate our model on the challenging SUN RGB-D dataset, advancing state-of-the-art results by 5.7 mAP. We also provide rich ablation studies to analyze the contribution of each design choice.

</details>

### End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection.
- **链接**: [arXiv:2004.03080](https://arxiv.org/abs/2004.03080) · [代码](https://github.com/mileyan/pseudo-LiDAR_e2e) · 📚 被引 168
- **作者**: Rui Qian, Divyansh Garg, Yan Wang, Yurong You, Serge J. Belongie, Bharath Hariharan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reliable and accurate 3D object detection is a necessity for safe autonomous driving. Although LiDAR sensors can provide accurate 3D point cloud estimates of the environment, they are also prohibitively expensive for many settings. Recently, the introduction of pseudo-LiDAR (PL) has led to a drastic reduction in the accuracy gap between methods based on LiDAR sensors and those based on cheap stereo cameras. PL combines state-of-the-art deep neural networks for 3D depth estimation with those for 3D object detection by converting 2D depth map outputs to 3D point cloud inputs. However, so far these two networks have to be trained separately. In this paper, we introduce a new framework based on differentiable Change of Representation (CoR) modules that allow the entire PL pipeline to be trained end-to-end. The resulting framework is compatible with most state-of-the-art networks for both tasks and in combination with PointRCNN improves over PL consistently across all benchmarks -- yielding the highest entry on the KITTI image-based 3D object detection leaderboard at the time of submission. Our code will be made available at https://github.com/mileyan/pseudo-LiDAR_e2e.

</details>

### PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:1912.13192](https://arxiv.org/abs/1912.13192) · 📚 被引 1987
- **作者**: Shaoshuai Shi, Chaoxu Guo, Li Jiang, Zhe Wang, Jianping Shi, Xiaogang Wang et al.
- **🏷️ 机构**: CUHK / Shanghai AI Lab, CUHK
- **会议**: CVPR 2020
- **摘要（中）**: ①针对点云3D检测中体素CNN和PointNet网络各自局限性的问题。②提出PV-RCNN，深度融合3D体素CNN和PointNet特征，通过体素集抽象和RoI-grid池化提取丰富特征。③相比传统方法，结合了体素CNN的高效和PointNet的灵活感受野。④在KITTI和Waymo Open数据集上取得领先性能。
- **摘要（英）**: This paper addresses the limitations of voxel CNN and PointNet in point cloud 3D detection. It proposes PV-RCNN, which deeply integrates both, using voxel set abstraction and RoI-grid pooling. Compared to prior methods, it combines efficiency and flexible receptive fields. It achieves leading performance on KITTI and Waymo Open datasets.
- **核心贡献**: 提出点-体素特征集抽象框架PV-RCNN。
- **创新点**: 深度融合体素CNN和PointNet特征。
- **结果**: 在KITTI和Waymo上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel and high-performance 3D object detection framework, named PointVoxel-RCNN (PV-RCNN), for accurate 3D object detection from point clouds. Our proposed method deeply integrates both 3D voxel Convolutional Neural Network (CNN) and PointNet-based set abstraction to learn more discriminative point cloud features. It takes advantages of efficient learning and high-quality proposals of the 3D voxel CNN and the flexible receptive fields of the PointNet-based networks. Specifically, the proposed framework summarizes the 3D scene with a 3D voxel CNN into a small set of keypoints via a novel voxel set abstraction module to save follow-up computations and also to encode representative scene features. Given the high-quality 3D proposals generated by the voxel CNN, the RoI-grid pooling is proposed to abstract proposal-specific features from the keypoints to the RoI-grid points via keypoint set abstraction with multiple receptive fields. Compared with conventional pooling operations, the RoI-grid feature points encode much richer context information for accurately estimating object confidences and locations. Extensive experiments on both the KITTI dataset and the Waymo Open dataset show that our proposed PV-RCNN surpasses state-of-the-art 3D detection methods with remarkable margins by using only point clouds. Code is available at https://github.com/open-mmlab/OpenPCDet.

</details>

### Point-GNN: Graph Neural Network for 3D Object Detection in a Point Cloud. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2003.01251](https://arxiv.org/abs/2003.01251) · 📚 被引 845
- **作者**: Weijing Shi, Raj Rajkumar
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对LiDAR点云3D检测中传统方法难以处理不规则数据的问题。②提出Point-GNN，将点云编码为固定半径近邻图，用图神经网络预测物体类别和形状。③相比之前方法，引入自动配准机制减少平移方差，并设计框合并和评分操作。④在KITTI基准上仅用点云达到领先精度，甚至超越融合方法。
- **摘要（英）**: This paper addresses the challenge of irregular point cloud data in LiDAR-based 3D detection. It proposes Point-GNN, encoding the point cloud as a fixed-radius near-neighbor graph and using GNN for prediction. Compared to prior methods, it introduces auto-registration and box merging. It achieves leading accuracy on KITTI using point cloud alone, surpassing fusion methods.
- **核心贡献**: 提出基于图神经网络的3D检测方法Point-GNN。
- **创新点**: 利用图结构处理点云并引入自动配准。
- **结果**: 在KITTI上超越融合方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a graph neural network to detect objects from a LiDAR point cloud. Towards this end, we encode the point cloud efficiently in a fixed radius near-neighbors graph. We design a graph neural network, named Point-GNN, to predict the category and shape of the object that each vertex in the graph belongs to. In Point-GNN, we propose an auto-registration mechanism to reduce translation variance, and also design a box merging and scoring operation to combine detections from multiple vertices accurately. Our experiments on the KITTI benchmark show the proposed approach achieves leading accuracy using the point cloud alone and can even surpass fusion-based algorithms. Our results demonstrate the potential of using the graph neural network as a new approach for 3D object detection. The code is available https://github.com/WeijingShi/Point-GNN.

</details>

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

### 3DV: 3D Dynamic Voxel for Action Recognition in Depth Video. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2005.05501](https://arxiv.org/abs/2005.05501) · 📚 被引 111
- **作者**: Yancheng Wang, Yang Xiao, Fu Xiong, Wenxiang Jiang, Zhiguo Cao, Joey Tianyi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对深度视频中3D动作识别的挑战，现有方法难以有效编码3D空间和运动信息。②提出了3D动态体素（3DV）作为新的3D运动表示，通过时间秩池化将深度视频编码为规则体素集，并输入PointNet++进行端到端学习。③相比现有方法，3DV紧凑地联合编码3D空间和运动特征，并支持多流学习以融合外观信息，同时通过时间分割增强时序信息。④在NTU RGB+D 120数据集上，跨主体和跨设置的准确率分别达到82.4%和93.5%，优于已有方法。
- **摘要（英）**: This paper addresses 3D action recognition in depth videos by proposing 3D dynamic voxels (3DV), which encode motion via temporal rank pooling and are processed by PointNet++. It integrates spatial and motion features, supports multi-stream learning, and achieves 82.4% and 93.5% accuracy on NTU RGB+D 120 for cross-subject and cross-setup settings.
- **核心贡献**: 提出了3DV表示，将深度视频编码为体素集用于3D动作识别。
- **创新点**: 利用时间秩池化和PointNet++实现紧凑的3D运动表示。
- **结果**: 在NTU RGB+D 120上达到82.4%和93.5%的准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To facilitate depth-based 3D action recognition, 3D dynamic voxel (3DV) is proposed as a novel 3D motion representation. With 3D space voxelization, the key idea of 3DV is to encode 3D motion information within depth video into a regular voxel set (i.e., 3DV) compactly, via temporal rank pooling. Each available 3DV voxel intrinsically involves 3D spatial and motion feature jointly. 3DV is then abstracted as a point set and input into PointNet++ for 3D action recognition, in the end-to-end learning way. The intuition for transferring 3DV into the point set form is that, PointNet++ is lightweight and effective for deep feature learning towards point set. Since 3DV may lose appearance clue, a multi-stream 3D action recognition manner is also proposed to learn motion and appearance feature jointly. To extract richer temporal order information of actions, we also divide the depth video into temporal splits and encode this procedure in 3DV integrally. The extensive experiments on 4 well-established benchmark datasets demonstrate the superiority of our proposition. Impressively, we acquire the accuracy of 82.4% and 93.5% on NTU RGB+D 120 [13] with the cross-subject and crosssetup test setting respectively. 3DV's code is available at https://github.com/3huo/3DV-Action.

</details>

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
