# 3D Detection — 2021 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Objects Are Different: Flexible Monocular 3D Object Detection.
- **链接**: [arXiv:2104.02323](https://arxiv.org/abs/2104.02323) · [代码](https://github.com/zhangyp15/MonoFlex)
- **作者**: Yunpeng Zhang, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology,China Department of Automation,China
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > The precise localization of 3D objects from a single image without depth information is a highly challenging problem. Most existing methods adopt the same approach for all objects regardless of their diverse distributions, leading to limited performance for truncated objects. In this paper, we propose a flexible framework for monocular 3D object detection which explicitly decouples the truncated objects and adaptively combines multiple approaches for object depth estimation. Specifically, we decouple the edge of the feature map for predicting long-tail truncated objects so that the optimization of normal objects is not influenced. Furthermore, we formulate the object depth estimation as an uncertainty-guided ensemble of directly regressed object depth and solved depths from different groups of keypoints. Experiments demonstrate that our method outperforms the state-of-the-art method by relatively 27\% for the moderate level and 30\% for the hard level in the test set of KITTI benchmark while maintaining real-time efficiency. Code will be available at \url{https://github.com/zhangyp15/MonoFlex}.

### GrooMeD-NMS: Grouped Mathematically Differentiable NMS for Monocular 3D Object Detection.
- **链接**: [arXiv:2103.17202](https://arxiv.org/abs/2103.17202) · [代码](https://github.com/abhi1kumar/groomed_nms)
- **作者**: Abhinav Kumar, Garrick Brazil, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Modern 3D object detectors have immensely benefited from the end-to-end learning idea. However, most of them use a post-processing algorithm called Non-Maximal Suppression (NMS) only during inference. While there were attempts to include NMS in the training pipeline for tasks such as 2D object detection, they have been less widely adopted due to a non-mathematical expression of the NMS. In this paper, we present and integrate GrooMeD-NMS -- a novel Grouped Mathematically Differentiable NMS for monocular 3D object detection, such that the network is trained end-to-end with a loss on the boxes after NMS. We first formulate NMS as a matrix operation and then group and mask the boxes in an unsupervised manner to obtain a simple closed-form expression of the NMS. GrooMeD-NMS addresses the mismatch between training and inference pipelines and, therefore, forces the network to select the best 3D box in a differentiable manner. As a result, GrooMeD-NMS achieves state-of-the-art monocular 3D object detection results on the KITTI benchmark dataset performing comparably to monocular video-based methods. Code and models at https://github.com/abhi1kumar/groomed_nms

### 3DIoUMatch: Leveraging IoU Prediction for Semi-Supervised 3D Object Detection.
- **链接**: [arXiv:2012.04355](https://arxiv.org/abs/2012.04355) · 📚 被引 121
- **作者**: He Wang, Yezhen Cong, Or Litany, Yue Gao, Leonidas J. Guibas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > 3D object detection is an important yet demanding task that heavily relies on difficult to obtain 3D annotations. To reduce the required amount of supervision, we propose 3DIoUMatch, a novel semi-supervised method for 3D object detection applicable to both indoor and outdoor scenes. We leverage a teacher-student mutual learning framework to propagate information from the labeled to the unlabeled train set in the form of pseudo-labels. However, due to the high task complexity, we observe that the pseudo-labels suffer from significant noise and are thus not directly usable. To that end, we introduce a confidence-based filtering mechanism, inspired by FixMatch. We set confidence thresholds based upon the predicted objectness and class probability to filter low-quality pseudo-labels. While effective, we observe that these two measures do not sufficiently capture localization quality. We therefore propose to use the estimated 3D IoU as a localization metric and set category-aware self-adjusted thresholds to filter poorly localized proposals. We adopt VoteNet as our backbone detector on indoor datasets while we use PV-RCNN on the autonomous driving dataset, KITTI. Our method consistently improves state-of-the-art methods on both ScanNet and SUN-RGBD benchmarks by significant margins under all label ratios (including fully labeled setting). For example, when training using only 10\% labeled data on ScanNet, 3DIoUMatch achieves 7.7% absolute improvement on mAP@0.25 and 8.5% absolute improvement on mAP@0.5 upon the prior art. On KITTI, we are the first to demonstrate semi-supervised 3D object detection and our method surpasses a fully supervised baseline from 1.8% to 7.6% under different label ratios and categories.

### To the Point: Efficient 3D Object Detection in the Range Image With Graph Convolution Kernels.
- **链接**: [arXiv:2106.13381](https://arxiv.org/abs/2106.13381) · 📚 被引 68
- **作者**: Yuning Chai, Pei Sun, Jiquan Ngiam, Weiyue Wang, Benjamin Caine, Vijay Vasudevan et al.
- **🏷️ 机构**: Waymo
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > 3D object detection is vital for many robotics applications. For tasks where a 2D perspective range image exists, we propose to learn a 3D representation directly from this range image view. To this end, we designed a 2D convolutional network architecture that carries the 3D spherical coordinates of each pixel throughout the network. Its layers can consume any arbitrary convolution kernel in place of the default inner product kernel and exploit the underlying local geometry around each pixel. We outline four such kernels: a dense kernel according to the bag-of-words paradigm, and three graph kernels inspired by recent graph neural network advances: the Transformer, the PointNet, and the Edge Convolution. We also explore cross-modality fusion with the camera image, facilitated by operating in the perspective range image view. Our method performs competitively on the Waymo Open Dataset and improves the state-of-the-art AP for pedestrian detection from 69.7% to 75.5%. It is also efficient in that our smallest model, which still outperforms the popular PointPillars in quality, requires 180 times fewer FLOPS and model parameters

### MonoRUn: Monocular 3D Object Detection by Reconstruction and Uncertainty Propagation.
- **链接**: [arXiv:2103.12605](https://arxiv.org/abs/2103.12605) · 📚 被引 131
- **作者**: Hansheng Chen, Yuyao Huang, Wei Tian, Zhong Gao, Lu Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Object localization in 3D space is a challenging aspect in monocular 3D object detection. Recent advances in 6DoF pose estimation have shown that predicting dense 2D-3D correspondence maps between image and object 3D model and then estimating object pose via Perspective-n-Point (PnP) algorithm can achieve remarkable localization accuracy. Yet these methods rely on training with ground truth of object geometry, which is difficult to acquire in real outdoor scenes. To address this issue, we propose MonoRUn, a novel detection framework that learns dense correspondences and geometry in a self-supervised manner, with simple 3D bounding box annotations. To regress the pixel-related 3D object coordinates, we employ a regional reconstruction network with uncertainty awareness. For self-supervised training, the predicted 3D coordinates are projected back to the image plane. A Robust KL loss is proposed to minimize the uncertainty-weighted reprojection error. During testing phase, we exploit the network uncertainty by propagating it through all downstream modules. More specifically, the uncertainty-driven PnP algorithm is leveraged to estimate object pose and its covariance. Extensive experiments demonstrate that our proposed approach outperforms current state-of-the-art methods on KITTI benchmark.

### Back-Tracing Representative Points for Voting-Based 3D Object Detection in Point Clouds.
- **链接**: [arXiv:2104.06114](https://arxiv.org/abs/2104.06114) · [代码](https://github.com/cheng052/BRNet) · 📚 被引 114
- **作者**: Bowen Cheng, Lu Sheng, Shaoshuai Shi, Ming Yang, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > 3D object detection in point clouds is a challenging vision task that benefits various applications for understanding the 3D visual world. Lots of recent research focuses on how to exploit end-to-end trainable Hough voting for generating object proposals. However, the current voting strategy can only receive partial votes from the surfaces of potential objects together with severe outlier votes from the cluttered backgrounds, which hampers full utilization of the information from the input point clouds. Inspired by the back-tracing strategy in the conventional Hough voting methods, in this work, we introduce a new 3D object detection method, named as Back-tracing Representative Points Network (BRNet), which generatively back-traces the representative points from the vote centers and also revisits complementary seed points around these generated points, so as to better capture the fine local structural features surrounding the potential objects from the raw point clouds. Therefore, this bottom-up and then top-down strategy in our BRNet enforces mutual consistency between the predicted vote centers and the raw surface points and thus achieves more reliable and flexible object localization and class prediction results. Our BRNet is simple but effective, which significantly outperforms the state-of-the-art methods on two large-scale point cloud datasets, ScanNet V2 (+7.5% in terms of mAP@0.50) and SUN RGB-D (+4.7% in terms of mAP@0.50), while it is still lightweight and efficient. Code will be available at https://github.com/cheng052/BRNet.

### LiDAR-Aug: A General Rendering-Based Augmentation Framework for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Fang_LiDAR-Aug_A_General_Rendering-Based_Augmentation_Framework_for_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 51
- **作者**: Jin Fang, Xinxin Zuo, Dingfu Zhou, Shengze Jin, Sen Wang, Liangjun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Delving Into Localization Errors for Monocular 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ma_Delving_Into_Localization_Errors_for_Monocular_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 242
- **作者**: Xinzhu Ma, Yinmin Zhang, Dan Xu, Dongzhan Zhou, Shuai Yi, Haojie Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### HVPR: Hybrid Voxel-Point Representation for Single-Stage 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Noh_HVPR_Hybrid_Voxel-Point_Representation_for_Single-Stage_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 153
- **作者**: Jongyoun Noh, Sanghoon Lee, Bumsub Ham
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### 3D Object Detection With Pointformer.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Pan_3D_Object_Detection_With_Pointformer_CVPR_2021_paper.html)
- **作者**: Xuran Pan, Zhuofan Xia, Shiji Song, Li Erran Li, Gao Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Offboard 3D Object Detection From Point Cloud Sequences.
- **链接**: [arXiv:2103.05073](https://arxiv.org/abs/2103.05073) · 📚 被引 161
- **作者**: Charles R. Qi, Yin Zhou, Mahyar Najibi, Pei Sun, Khoa Vo, Boyang Deng et al.
- **🏷️ 机构**: Waymo LLC
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > While current 3D object recognition research mostly focuses on the real-time, onboard scenario, there are many offboard use cases of perception that are largely under-explored, such as using machines to automatically generate high-quality 3D labels. Existing 3D object detectors fail to satisfy the high-quality requirement for offboard uses due to the limited input and speed constraints. In this paper, we propose a novel offboard 3D object detection pipeline using point cloud sequence data. Observing that different frames capture complementary views of objects, we design the offboard detector to make use of the temporal points through both multi-frame object detection and novel object-centric refinement models. Evaluated on the Waymo Open Dataset, our pipeline named 3D Auto Labeling shows significant gains compared to the state-of-the-art onboard detectors and our offboard baselines. Its performance is even on par with human labels verified through a human label study. Further experiments demonstrate the application of auto labels for semi-supervised learning and provide extensive analysis to validate various design choices.

### Categorical Depth Distribution Network for Monocular 3D Object Detection.
- **链接**: [arXiv:2103.01100](https://arxiv.org/abs/2103.01100) · 📚 被引 516
- **作者**: Cody Reading, Ali Harakeh, Julia Chae, Steven L. Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Monocular 3D object detection is a key problem for autonomous vehicles, as it provides a solution with simple configuration compared to typical multi-sensor systems. The main challenge in monocular 3D detection lies in accurately predicting object depth, which must be inferred from object and scene cues due to the lack of direct range measurement. Many methods attempt to directly estimate depth to assist in 3D detection, but show limited performance as a result of depth inaccuracy. Our proposed solution, Categorical Depth Distribution Network (CaDDN), uses a predicted categorical depth distribution for each pixel to project rich contextual feature information to the appropriate depth interval in 3D space. We then use the computationally efficient bird's-eye-view projection and single-stage detector to produce the final output bounding boxes. We design CaDDN as a fully differentiable end-to-end approach for joint depth estimation and object detection. We validate our approach on the KITTI 3D object detection benchmark, where we rank 1st among published monocular methods. We also provide the first monocular 3D detection results on the newly released Waymo Open Dataset. We provide a code release for CaDDN which is made available.

### RSN: Range Sparse Net for Efficient, Accurate LiDAR 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_RSN_Range_Sparse_Net_for_Efficient_Accurate_LiDAR_3D_Object_CVPR_2021_paper.html) · 📚 被引 155
- **作者**: Pei Sun, Weiyue Wang, Yuning Chai, Gamaleldin Elsayed, Alex Bewley, Xiao Zhang et al.
- **🏷️ 机构**: Waymo LLC, Google
- **会议**: CVPR 2021

### PointAugmenting: Cross-Modal Augmentation for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_PointAugmenting_Cross-Modal_Augmentation_for_3D_Object_Detection_CVPR_2021_paper.html)
- **作者**: Chunwei Wang, Chao Ma, Ming Zhu, Xiaokang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Depth-Conditioned Dynamic Message Propagation for Monocular 3D Object Detection.
- **链接**: [arXiv:2103.16470](https://arxiv.org/abs/2103.16470) · [代码](https://github.com/fudan-zvg/DDMP)
- **作者**: Li Wang, Liang Du, Xiaoqing Ye, Yanwei Fu, Guodong Guo, Xiangyang Xue et al.
- **🏷️ 机构**: Fudan University,School of Computer Science, Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, Baidu Inc.
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > The objective of this paper is to learn context- and depth-aware feature representation to solve the problem of monocular 3D object detection. We make following contributions: (i) rather than appealing to the complicated pseudo-LiDAR based approach, we propose a depth-conditioned dynamic message propagation (DDMP) network to effectively integrate the multi-scale depth information with the image context;(ii) this is achieved by first adaptively sampling context-aware nodes in the image context and then dynamically predicting hybrid depth-dependent filter weights and affinity matrices for propagating information; (iii) by augmenting a center-aware depth encoding (CDE) task, our method successfully alleviates the inaccurate depth prior; (iv) we thoroughly demonstrate the effectiveness of our proposed approach and show state-of-the-art results among the monocular-based approaches on the KITTI benchmark dataset. Particularly, we rank $1^{st}$ in the highly competitive KITTI monocular 3D object detection track on the submission day (November 16th, 2020). Code and models are released at \url{https://github.com/fudan-zvg/DDMP}

### ST3D: Self-Training for Unsupervised Domain Adaptation on 3D Object Detection.
- **链接**: [arXiv:2103.05346](https://arxiv.org/abs/2103.05346) · [代码](https://github.com/CVMI-Lab/ST3D) · 📚 被引 181
- **作者**: Jihan Yang, Shaoshuai Shi, Zhe Wang, Hongsheng Li, Xiaojuan Qi
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > We present a new domain adaptive self-training pipeline, named ST3D, for unsupervised domain adaptation on 3D object detection from point clouds. First, we pre-train the 3D detector on the source domain with our proposed random object scaling strategy for mitigating the negative effects of source domain bias. Then, the detector is iteratively improved on the target domain by alternatively conducting two steps, which are the pseudo label updating with the developed quality-aware triplet memory bank and the model training with curriculum data augmentation. These specific designs for 3D object detection enable the detector to be trained with consistent and high-quality pseudo labels and to avoid overfitting to the large number of easy examples in pseudo labeled data. Our ST3D achieves state-of-the-art performance on all evaluated datasets and even surpasses fully supervised results on KITTI 3D object detection benchmark. Code will be available at https://github.com/CVMI-Lab/ST3D.

### Center-Based 3D Object Detection and Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.html)
- **作者**: Tianwei Yin, Xingyi Zhou, Philipp Krähenbühl
- **🏷️ 机构**: UT Austin
- **会议**: CVPR 2021

### SRDAN: Scale-Aware and Range-Aware Domain Adaptation Network for Cross-Dataset 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_SRDAN_Scale-Aware_and_Range-Aware_Domain_Adaptation_Network_for_Cross-Dataset_3D_CVPR_2021_paper.html) · 📚 被引 49
- **作者**: Weichen Zhang, Wen Li, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Monocular 3D Object Detection: An Extrinsic Parameter Free Approach.
- **链接**: [arXiv:2106.15796](https://arxiv.org/abs/2106.15796) · 📚 被引 86
- **作者**: Yunsong Zhou, Yuan He, Hongzi Zhu, Cheng Wang, Hongyang Li, Qinhong Jiang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Monocular 3D object detection is an important task in autonomous driving. It can be easily intractable where there exists ego-car pose change w.r.t. ground plane. This is common due to the slight fluctuation of road smoothness and slope. Due to the lack of insight in industrial application, existing methods on open datasets neglect the camera pose information, which inevitably results in the detector being susceptible to camera extrinsic parameters. The perturbation of objects is very popular in most autonomous driving cases for industrial products. To this end, we propose a novel method to capture camera pose to formulate the detector free from extrinsic perturbation. Specifically, the proposed framework predicts camera extrinsic parameters by detecting vanishing point and horizon change. A converter is designed to rectify perturbative features in the latent space. By doing so, our 3D detector works independent of the extrinsic parameter variations and produces accurate results in realistic cases, e.g., potholed and uneven roads, where almost all existing monocular detectors fail to handle. Experiments demonstrate our method yields the best performance compared with the other state-of-the-arts by a large margin on both KITTI 3D and nuScenes datasets.

### VoxelContext-Net: An Octree Based Framework for Point Cloud Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Que_VoxelContext-Net_An_Octree_Based_Framework_for_Point_Cloud_Compression_CVPR_2021_paper.html)
- **作者**: Zizheng Que, Guo Lu, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### CanonPose: Self-Supervised Monocular 3D Human Pose Estimation in the Wild.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wandt_CanonPose_Self-Supervised_Monocular_3D_Human_Pose_Estimation_in_the_Wild_CVPR_2021_paper.html)
- **作者**: Bastian Wandt, Marco Rudolph, Petrissa Zell, Helge Rhodin, Bodo Rosenhahn
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
