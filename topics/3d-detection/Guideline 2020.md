# 3D Detection — 2020 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 19 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MLCVNet: Multi-Level Context VoteNet for 3D Object Detection.
- **链接**: [arXiv:2004.05679](https://arxiv.org/abs/2004.05679) · [代码](https://github.com/NUAAXQ/MLCVNet) · 📚 被引 172
- **作者**: Qian Xie, Yu-Kun Lai, Jing Wu, Zhoutao Wang, Yiming Zhang, Kai Xu et al.
- **🏷️ 机构**: Nanjing University of Aeronautics and Astronautics, Cardiff University, National University of Defense Technology
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we address the 3D object detection task by capturing multi-level contextual information with the self-attention mechanism and multi-scale feature fusion. Most existing 3D object detection methods recognize objects individually, without giving any consideration on contextual information between these objects. Comparatively, we propose Multi-Level Context VoteNet (MLCVNet) to recognize 3D objects correlatively, building on the state-of-the-art VoteNet. We introduce three context modules into the voting and classifying stages of VoteNet to encode contextual information at different levels. Specifically, a Patch-to-Patch Context (PPC) module is employed to capture contextual information between the point patches, before voting for their corresponding object centroid points. Subsequently, an Object-to-Object Context (OOC) module is incorporated before the proposal and classification stage, to capture the contextual information between object candidates. Finally, a Global Scene Context (GSC) module is designed to learn the global scene context. We demonstrate these by capturing contextual information at patch, object and scene levels. Our method is an effective way to promote detection accuracy, achieving new state-of-the-art detection performance on challenging 3D object detection datasets, i.e., SUN RGBD and ScanNet. We also release our code at https://github.com/NUAAXQ/MLCVNet.

</details>

### Density-Based Clustering for 3D Object Detection in Point Clouds.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Ahmed_Density-Based_Clustering_for_3D_Object_Detection_in_Point_Clouds_CVPR_2020_paper.html) · 📚 被引 30
- **作者**: Syeda Mariam Ahmed, Chee-Meng Chew
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### DSGN: Deep Stereo Geometry Network for 3D Object Detection.
- **链接**: [arXiv:2001.03398](https://arxiv.org/abs/2001.03398) · [代码](https://github.com/chenyilun95/DSGN) · 📚 被引 179
- **作者**: Yilun Chen, Shu Liu, Xiaoyong Shen, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most state-of-the-art 3D object detectors heavily rely on LiDAR sensors because there is a large performance gap between image-based and LiDAR-based methods. It is caused by the way to form representation for the prediction in 3D scenarios. Our method, called Deep Stereo Geometry Network (DSGN), significantly reduces this gap by detecting 3D objects on a differentiable volumetric representation -- 3D geometric volume, which effectively encodes 3D geometric structure for 3D regular space. With this representation, we learn depth information and semantic cues simultaneously. For the first time, we provide a simple and effective one-stage stereo-based 3D detection pipeline that jointly estimates the depth and detects 3D objects in an end-to-end learning manner. Our approach outperforms previous stereo-based 3D detectors (about 10 higher in terms of AP) and even achieves comparable performance with several LiDAR-based methods on the KITTI 3D object detection leaderboard. Our code is publicly available at https://github.com/chenyilun95/DSGN.

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

> Monocular 3D object detection is an essential component in autonomous driving while challenging to solve, especially for those occluded samples which are only partially visible. Most detectors consider each 3D object as an independent training target, inevitably resulting in a lack of useful information for occluded samples. To this end, we propose a novel method to improve the monocular 3D object detection by considering the relationship of paired samples. This allows us to encode spatial constraints for partially-occluded objects from their adjacent neighbors. Specifically, the proposed detector computes uncertainty-aware predictions for object locations and 3D distances for the adjacent object pairs, which are subsequently jointly optimized by nonlinear least squares. Finally, the one-stage uncertainty-aware prediction structure and the post-optimization module are dedicatedly integrated for ensuring the run-time efficiency. Experiments demonstrate that our method yields the best performance on KITTI 3D detection benchmark, by outperforming state-of-the-art competitors by wide margins, especially for the hard samples.

</details>

### Learning Depth-Guided Convolutions for Monocular 3D Object Detection.
- **链接**: [arXiv:1912.04799](https://arxiv.org/abs/1912.04799) · [代码](https://github.com/dingmyu/D4LCN) · 📚 被引 210
- **作者**: Mingyu Ding, Yuqi Huo, Hongwei Yi, Zhe Wang, Jianping Shi, Zhiwu Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection from a single image without LiDAR is a challenging task due to the lack of accurate depth information. Conventional 2D convolutions are unsuitable for this task because they fail to capture local object and its scale information, which are vital for 3D object detection. To better represent 3D structure, prior arts typically transform depth maps estimated from 2D images into a pseudo-LiDAR representation, and then apply existing 3D point-cloud based object detectors. However, their results depend heavily on the accuracy of the estimated depth maps, resulting in suboptimal performance. In this work, instead of using pseudo-LiDAR representation, we improve the fundamental 2D fully convolutions by proposing a new local convolutional network (LCN), termed Depth-guided Dynamic-Depthwise-Dilated LCN (D$^4$LCN), where the filters and their receptive fields can be automatically learned from image-based depth maps, making different pixels of different images have different filters. D$^4$LCN overcomes the limitation of conventional 2D convolutions and narrows the gap between image representation and 3D point cloud representation. Extensive experiments show that D$^4$LCN outperforms existing works by large margins. For example, the relative improvement of D$^4$LCN against the state-of-the-art on KITTI is 9.1\% in the moderate setting. The code is available at https://github.com/dingmyu/D4LCN.

</details>

### Structure Aware Single-Stage 3D Object Detection From Point Cloud.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/He_Structure_Aware_Single-Stage_3D_Object_Detection_From_Point_Cloud_CVPR_2020_paper.html) · 📚 被引 556
- **作者**: Chenhang He, Hui Zeng, Jianqiang Huang, Xian-Sheng Hua, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2020

### What You See is What You Get: Exploiting Visibility for 3D Object Detection.
- **链接**: [arXiv:1912.04986](https://arxiv.org/abs/1912.04986) · 📚 被引 108
- **作者**: Peiyun Hu, Jason Ziglar, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in 3D sensing have created unique challenges for computer vision. One fundamental challenge is finding a good representation for 3D sensor data. Most popular representations (such as PointNet) are proposed in the context of processing truly 3D data (e.g. points sampled from mesh models), ignoring the fact that 3D sensored data such as a LiDAR sweep is in fact 2.5D. We argue that representing 2.5D data as collections of (x, y, z) points fundamentally destroys hidden information about freespace. In this paper, we demonstrate such knowledge can be efficiently recovered through 3D raycasting and readily incorporated into batch-based gradient learning. We describe a simple approach to augmenting voxel-based networks with visibility: we add a voxelized visibility map as an additional input stream. In addition, we show that visibility can be combined with two crucial modifications common to state-of-the-art 3D detectors: synthetic data augmentation of virtual objects and temporal aggregation of LiDAR sweeps over multiple time frames. On the NuScenes 3D detection benchmark, we show that, by adding an additional stream for visibility input, we can significantly improve the overall detection accuracy of a state-of-the-art 3D detector.

</details>

### IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Peng_IDA-3D_Instance-Depth-Aware_3D_Object_Detection_From_Stereo_Vision_for_Autonomous_CVPR_2020_paper.html)
- **作者**: Wanli Peng, Hao Pan, He Liu, Yi Sun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes.
- **链接**: [arXiv:2001.10692](https://arxiv.org/abs/2001.10692) · 📚 被引 258
- **作者**: Charles R. Qi, Xinlei Chen, Or Litany, Leonidas J. Guibas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a graph neural network to detect objects from a LiDAR point cloud. Towards this end, we encode the point cloud efficiently in a fixed radius near-neighbors graph. We design a graph neural network, named Point-GNN, to predict the category and shape of the object that each vertex in the graph belongs to. In Point-GNN, we propose an auto-registration mechanism to reduce translation variance, and also design a box merging and scoring operation to combine detections from multiple vertices accurately. Our experiments on the KITTI benchmark show the proposed approach achieves leading accuracy using the point cloud alone and can even surpass fusion-based algorithms. Our results demonstrate the potential of using the graph neural network as a new approach for 3D object detection. The code is available https://github.com/WeijingShi/Point-GNN.

</details>

### Disp R-CNN: Stereo 3D Object Detection via Shape Prior Guided Instance Disparity Estimation.
- **链接**: [arXiv:2004.03572](https://arxiv.org/abs/2004.03572) · 📚 被引 93
- **作者**: Jiaming Sun, Linghao Chen, Yiming Xie, Siyu Zhang, Qinhong Jiang, Xiaowei Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel system named Disp R-CNN for 3D object detection from stereo images. Many recent works solve this problem by first recovering a point cloud with disparity estimation and then apply a 3D detector. The disparity map is computed for the entire image, which is costly and fails to leverage category-specific prior. In contrast, we design an instance disparity estimation network (iDispNet) that predicts disparity only for pixels on objects of interest and learns a category-specific shape prior for more accurate disparity estimation. To address the challenge from scarcity of disparity annotation in training, we propose to use a statistical shape model to generate dense disparity pseudo-ground-truth without the need of LiDAR point clouds, which makes our system more widely applicable. Experiments on the KITTI dataset show that, even when LiDAR ground-truth is not available at training time, Disp R-CNN achieves competitive performance and outperforms previous state-of-the-art methods by 20% in terms of average precision.

</details>

### PointPainting: Sequential Fusion for 3D Object Detection.
- **链接**: [arXiv:1911.10150](https://arxiv.org/abs/1911.10150) · 📚 被引 1122
- **作者**: Sourabh Vora, Alex H. Lang, Bassam Helou, Oscar Beijbom
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera and lidar are important sensor modalities for robotics in general and self-driving cars in particular. The sensors provide complementary information offering an opportunity for tight sensor-fusion. Surprisingly, lidar-only methods outperform fusion methods on the main benchmark datasets, suggesting a gap in the literature. In this work, we propose PointPainting: a sequential fusion method to fill this gap. PointPainting works by projecting lidar points into the output of an image-only semantic segmentation network and appending the class scores to each point. The appended (painted) point cloud can then be fed to any lidar-only method. Experiments show large improvements on three different state-of-the art methods, Point-RCNN, VoxelNet and PointPillars on the KITTI and nuScenes datasets. The painted version of PointRCNN represents a new state of the art on the KITTI leaderboard for the bird's-eye view detection task. In ablation, we study how the effects of Painting depends on the quality and format of the semantic segmentation output, and demonstrate how latency can be minimized through pipelining.

</details>

### HVNet: Hybrid Voxel Network for LiDAR Based 3D Object Detection.
- **链接**: [arXiv:2003.00186](https://arxiv.org/abs/2003.00186) · 📚 被引 210
- **作者**: Maosheng Ye, Shuangjie Xu, Tongyi Cao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### SESS: Self-Ensembling Semi-Supervised 3D Object Detection.
- **链接**: [arXiv:1912.11803](https://arxiv.org/abs/1912.11803) · [代码](https://github.com/Na-Z/sess) · 📚 被引 125
- **作者**: Na Zhao, Tat-Seng Chua, Gim Hee Lee
- **🏷️ 机构**: Deaprtment of Computer Science, National University of Singapore
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The performance of existing point cloud-based 3D object detection methods heavily relies on large-scale high-quality 3D annotations. However, such annotations are often tedious and expensive to collect. Semi-supervised learning is a good alternative to mitigate the data annotation issue, but has remained largely unexplored in 3D object detection. Inspired by the recent success of self-ensembling technique in semi-supervised image classification task, we propose SESS, a self-ensembling semi-supervised 3D object detection framework. Specifically, we design a thorough perturbation scheme to enhance generalization of the network on unlabeled and new unseen data. Furthermore, we propose three consistency losses to enforce the consistency between two sets of predicted 3D object proposals, to facilitate the learning of structure and semantic invariances of objects. Extensive experiments conducted on SUN RGB-D and ScanNet datasets demonstrate the effectiveness of SESS in both inductive and transductive semi-supervised 3D object detection. Our SESS achieves competitive performance compared to the state-of-the-art fully-supervised method by using only 50% labeled data. Our code is available at https://github.com/Na-Z/sess.

</details>

### Joint 3D Instance Segmentation and Object Detection for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhou_Joint_3D_Instance_Segmentation_and_Object_Detection_for_Autonomous_Driving_CVPR_2020_paper.html)
- **作者**: Dingfu Zhou, Jin Fang, Xibin Song, Liu Liu, Junbo Yin, Yuchao Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### 3DV: 3D Dynamic Voxel for Action Recognition in Depth Video.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wang_3DV_3D_Dynamic_Voxel_for_Action_Recognition_in_Depth_Video_CVPR_2020_paper.html)
- **作者**: Yancheng Wang, Yang Xiao, Fu Xiong, Wenxiang Jiang, Zhiguo Cao, Joey Tianyi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
