# 3D Detection — 2020 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

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
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most state-of-the-art 3D object detectors heavily rely on LiDAR sensors because there is a large performance gap between image-based and LiDAR-based methods. It is caused by the way to form representation for the prediction in 3D scenarios. Our method, called Deep Stereo Geometry Network (DSGN), significantly reduces this gap by detecting 3D objects on a differentiable volumetric representation -- 3D geometric volume, which effectively encodes 3D geometric structure for 3D regular space. With this representation, we learn depth information and semantic cues simultaneously. For the first time, we provide a simple and effective one-stage stereo-based 3D detection pipeline that jointly estimates the depth and detects 3D objects in an end-to-end learning manner. Our approach outperforms previous stereo-based 3D detectors (about 10 higher in terms of AP) and even achieves comparable performance with several LiDAR-based methods on the KITTI 3D object detection leaderboard. Our code is publicly available at https://github.com/chenyilun95/DSGN.

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

> Monocular 3D object detection is an essential component in autonomous driving while challenging to solve, especially for those occluded samples which are only partially visible. Most detectors consider each 3D object as an independent training target, inevitably resulting in a lack of useful information for occluded samples. To this end, we propose a novel method to improve the monocular 3D object detection by considering the relationship of paired samples. This allows us to encode spatial constraints for partially-occluded objects from their adjacent neighbors. Specifically, the proposed detector computes uncertainty-aware predictions for object locations and 3D distances for the adjacent object pairs, which are subsequently jointly optimized by nonlinear least squares. Finally, the one-stage uncertainty-aware prediction structure and the post-optimization module are dedicatedly integrated for ensuring the run-time efficiency. Experiments demonstrate that our method yields the best performance on KITTI 3D detection benchmark, by outperforming state-of-the-art competitors by wide margins, especially for the hard samples.

</details>

</details>

### Improving 3D Object Detection Through Progressive Population Based Augmentation.
- **链接**: [arXiv:2004.00831](https://arxiv.org/abs/2004.00831)
- **作者**: Shuyang Cheng, Zhaoqi Leng, Ekin Dogus Cubuk, Barret Zoph, Chunyan Bai, Jiquan Ngiam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

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

> 3D object detection has seen quick progress thanks to advances in deep learning on point clouds. A few recent works have even shown state-of-the-art performance with just point clouds input (e.g. VoteNet). However, point cloud data have inherent limitations. They are sparse, lack color information and often suffer from sensor noise. Images, on the other hand, have high resolution and rich texture. Thus they can complement the 3D geometry provided by point clouds. Yet how to effectively use image information to assist point cloud based detection is still an open question. In this work, we build on top of VoteNet and propose a 3D detection architecture called ImVoteNet specialized for RGB-D scenes. ImVoteNet is based on fusing 2D votes in images and 3D votes in point clouds. Compared to prior work on multi-modal detection, we explicitly extract both geometric and semantic features from the 2D images. We leverage camera parameters to lift these features to 3D. To improve the synergy of 2D-3D feature fusion, we also propose a multi-tower training scheme. We validate our model on the challenging SUN RGB-D dataset, advancing state-of-the-art results by 5.7 mAP. We also provide rich ablation studies to analyze the contribution of each design choice.

</details>

</details>

### RTM3D: Real-Time Monocular 3D Detection from Object Keypoints for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58580-8_38)
- **作者**: Peixuan Li, Huaici Zhao, Pengfei Liu, Feidao Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

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
- **链接**: [arXiv:2003.01251](https://arxiv.org/abs/2003.01251) · [代码](https://github.com/WeijingShi/Point-GNN) · 📚 被引 844
- **作者**: Weijing Shi, Raj Rajkumar
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a graph neural network to detect objects from a LiDAR point cloud. Towards this end, we encode the point cloud efficiently in a fixed radius near-neighbors graph. We design a graph neural network, named Point-GNN, to predict the category and shape of the object that each vertex in the graph belongs to. In Point-GNN, we propose an auto-registration mechanism to reduce translation variance, and also design a box merging and scoring operation to combine detections from multiple vertices accurately. Our experiments on the KITTI benchmark show the proposed approach achieves leading accuracy using the point cloud alone and can even surpass fusion-based algorithms. Our results demonstrate the potential of using the graph neural network as a new approach for 3D object detection. The code is available https://github.com/WeijingShi/Point-GNN.

</details>

### Disp R-CNN: Stereo 3D Object Detection via Shape Prior Guided Instance Disparity Estimation.
- **链接**: [arXiv:2004.03572](https://arxiv.org/abs/2004.03572) · 📚 被引 93
- **作者**: Jiaming Sun, Linghao Chen, Yiming Xie, Siyu Zhang, Qinhong Jiang, Xiaowei Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel system named Disp R-CNN for 3D object detection from stereo images. Many recent works solve this problem by first recovering a point cloud with disparity estimation and then apply a 3D detector. The disparity map is computed for the entire image, which is costly and fails to leverage category-specific prior. In contrast, we design an instance disparity estimation network (iDispNet) that predicts disparity only for pixels on objects of interest and learns a category-specific shape prior for more accurate disparity estimation. To address the challenge from scarcity of disparity annotation in training, we propose to use a statistical shape model to generate dense disparity pseudo-ground-truth without the need of LiDAR point clouds, which makes our system more widely applicable. Experiments on the KITTI dataset show that, even when LiDAR ground-truth is not available at training time, Disp R-CNN achieves competitive performance and outperforms previous state-of-the-art methods by 20% in terms of average precision.

</details>

### PointPainting: Sequential Fusion for 3D Object Detection.
- **链接**: [arXiv:1911.10150](https://arxiv.org/abs/1911.10150) · 📚 被引 1122
- **作者**: Sourabh Vora, Alex H. Lang, Bassam Helou, Oscar Beijbom
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera and lidar are important sensor modalities for robotics in general and self-driving cars in particular. The sensors provide complementary information offering an opportunity for tight sensor-fusion. Surprisingly, lidar-only methods outperform fusion methods on the main benchmark datasets, suggesting a gap in the literature. In this work, we propose PointPainting: a sequential fusion method to fill this gap. PointPainting works by projecting lidar points into the output of an image-only semantic segmentation network and appending the class scores to each point. The appended (painted) point cloud can then be fed to any lidar-only method. Experiments show large improvements on three different state-of-the art methods, Point-RCNN, VoxelNet and PointPillars on the KITTI and nuScenes datasets. The painted version of PointRCNN represents a new state of the art on the KITTI leaderboard for the bird's-eye view detection task. In ablation, we study how the effects of Painting depends on the quality and format of the semantic segmentation output, and demonstrate how latency can be minimized through pipelining.

</details>

### HVNet: Hybrid Voxel Network for LiDAR Based 3D Object Detection.
- **链接**: [arXiv:2003.00186](https://arxiv.org/abs/2003.00186) · 📚 被引 210
- **作者**: Maosheng Ye, Shuangjie Xu, Tongyi Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

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
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58565-5_28)
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

### Towards Part-Aware Monocular 3D Human Pose Estimation: An Architecture Search Approach.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58580-8_42)
- **作者**: Zerui Chen, Yan Huang, Hongyuan Yu, Bin Xue, Ke Han, Yiru Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Searching Efficient 3D Architectures with Sparse Point-Voxel Convolution.
- **链接**: [arXiv:2007.16100](https://arxiv.org/abs/2007.16100) · 📚 被引 609
- **作者**: Haotian Tang, Zhijian Liu, Shengyu Zhao, Yujun Lin, Ji Lin, Hanrui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-driving cars need to understand 3D scenes efficiently and accurately in order to drive safely. Given the limited hardware resources, existing 3D perception models are not able to recognize small instances (e.g., pedestrians, cyclists) very well due to the low-resolution voxelization and aggressive downsampling. To this end, we propose Sparse Point-Voxel Convolution (SPVConv), a lightweight 3D module that equips the vanilla Sparse Convolution with the high-resolution point-based branch. With negligible overhead, this point-based branch is able to preserve the fine details even from large outdoor scenes. To explore the spectrum of efficient 3D models, we first define a flexible architecture design space based on SPVConv, and we then present 3D Neural Architecture Search (3D-NAS) to search the optimal network architecture over this diverse design space efficiently and effectively. Experimental results validate that the resulting SPVNAS model is fast and accurate: it outperforms the state-of-the-art MinkowskiNet by 3.3%, ranking 1st on the competitive SemanticKITTI leaderboard. It also achieves 8x computation reduction and 3x measured speedup over MinkowskiNet with higher accuracy. Finally, we transfer our method to 3D object detection, and it achieves consistent improvements over the one-stage detection baseline on KITTI.

</details>
