# 3D Detection — 2020 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MLCVNet: Multi-Level Context VoteNet for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Xie_MLCVNet_Multi-Level_Context_VoteNet_for_3D_Object_Detection_CVPR_2020_paper.html) · 📚 被引 172
- **作者**: Qian Xie, Yu-Kun Lai, Jing Wu, Zhoutao Wang, Yiming Zhang, Kai Xu et al.
- **🏷️ 机构**: Nanjing University of Aeronautics and Astronautics, Cardiff University, National University of Defense Technology
- **会议**: CVPR 2020

### Density-Based Clustering for 3D Object Detection in Point Clouds.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Ahmed_Density-Based_Clustering_for_3D_Object_Detection_in_Point_Clouds_CVPR_2020_paper.html) · 📚 被引 30
- **作者**: Syeda Mariam Ahmed, Chee-Meng Chew
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### DSGN: Deep Stereo Geometry Network for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_DSGN_Deep_Stereo_Geometry_Network_for_3D_Object_Detection_CVPR_2020_paper.html) · 📚 被引 179
- **作者**: Yilun Chen, Shu Liu, Xiaoyong Shen, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2020

### A Hierarchical Graph Network for 3D Object Detection on Point Clouds.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_A_Hierarchical_Graph_Network_for_3D_Object_Detection_on_Point_CVPR_2020_paper.html) · 📚 被引 143
- **作者**: Jintai Chen, Biwen Lei, Qingyu Song, Haochao Ying, Danny Z. Chen, Jian Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### MonoPair: Monocular 3D Object Detection Using Pairwise Spatial Relationships.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_MonoPair_Monocular_3D_Object_Detection_Using_Pairwise_Spatial_Relationships_CVPR_2020_paper.html) · 📚 被引 285
- **作者**: Yongjian Chen, Lei Tai, Kai Sun, Mingyang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Learning Depth-Guided Convolutions for Monocular 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Ding_Learning_Depth-Guided_Convolutions_for_Monocular_3D_Object_Detection_CVPR_2020_paper.html) · 📚 被引 210
- **作者**: Mingyu Ding, Yuqi Huo, Hongwei Yi, Zhe Wang, Jianping Shi, Zhiwu Lu et al.
- **🏷️ 机构**: The University of Hong Kong
- **会议**: CVPR 2020

### Structure Aware Single-Stage 3D Object Detection From Point Cloud.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/He_Structure_Aware_Single-Stage_3D_Object_Detection_From_Point_Cloud_CVPR_2020_paper.html) · 📚 被引 555
- **作者**: Chenhang He, Hui Zeng, Jianqiang Huang, Xian-Sheng Hua, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2020

### What You See is What You Get: Exploiting Visibility for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Hu_What_You_See_is_What_You_Get_Exploiting_Visibility_for_CVPR_2020_paper.html) · 📚 被引 108
- **作者**: Peiyun Hu, Jason Ziglar, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: CVPR 2020

### IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Peng_IDA-3D_Instance-Depth-Aware_3D_Object_Detection_From_Stereo_Vision_for_Autonomous_CVPR_2020_paper.html)
- **作者**: Wanli Peng, Hao Pan, He Liu, Yi Sun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes.
- **链接**: [arXiv:2001.10692](https://arxiv.org/abs/2001.10692) · [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Qi_ImVoteNet_Boosting_3D_Object_Detection_in_Point_Clouds_With_Image_CVPR_2020_paper.html) · 📚 被引 258
- **作者**: Charles R. Qi, Xinlei Chen, Or Litany, Leonidas J. Guibas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > 3D object detection has seen quick progress thanks to advances in deep learning on point clouds. A few recent works have even shown state-of-the-art performance with just point clouds input (e.g. VoteNet). However, point cloud data have inherent limitations. They are sparse, lack color information and often suffer from sensor noise. Images, on the other hand, have high resolution and rich texture. Thus they can complement the 3D geometry provided by point clouds. Yet how to effectively use image information to assist point cloud based detection is still an open question. In this work, we build on top of VoteNet and propose a 3D detection architecture called ImVoteNet specialized for RGB-D scenes. ImVoteNet is based on fusing 2D votes in images and 3D votes in point clouds. Compared to prior work on multi-modal detection, we explicitly extract both geometric and semantic features from the 2D images. We leverage camera parameters to lift these features to 3D. To improve the synergy of 2D-3D feature fusion, we also propose a multi-tower training scheme. We validate our model on the challenging SUN RGB-D dataset, advancing state-of-the-art results by 5.7 mAP. We also provide rich ablation studies to analyze the contribution of each design choice.

### End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection.
- **链接**: [arXiv:2004.03080](https://arxiv.org/abs/2004.03080) · [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Qian_End-to-End_Pseudo-LiDAR_for_Image-Based_3D_Object_Detection_CVPR_2020_paper.html) · [代码](https://github.com/mileyan/pseudo-LiDAR_e2e) · 📚 被引 168
- **作者**: Rui Qian, Divyansh Garg, Yan Wang, Yurong You, Serge J. Belongie, Bharath Hariharan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Reliable and accurate 3D object detection is a necessity for safe autonomous driving. Although LiDAR sensors can provide accurate 3D point cloud estimates of the environment, they are also prohibitively expensive for many settings. Recently, the introduction of pseudo-LiDAR (PL) has led to a drastic reduction in the accuracy gap between methods based on LiDAR sensors and those based on cheap stereo cameras. PL combines state-of-the-art deep neural networks for 3D depth estimation with those for 3D object detection by converting 2D depth map outputs to 3D point cloud inputs. However, so far these two networks have to be trained separately. In this paper, we introduce a new framework based on differentiable Change of Representation (CoR) modules that allow the entire PL pipeline to be trained end-to-end. The resulting framework is compatible with most state-of-the-art networks for both tasks and in combination with PointRCNN improves over PL consistently across all benchmarks -- yielding the highest entry on the KITTI image-based 3D object detection leaderboard at the time of submission. Our code will be made available at https://github.com/mileyan/pseudo-LiDAR_e2e.

### PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Shi_PV-RCNN_Point-Voxel_Feature_Set_Abstraction_for_3D_Object_Detection_CVPR_2020_paper.html) · 📚 被引 1983
- **作者**: Shaoshuai Shi, Chaoxu Guo, Li Jiang, Zhe Wang, Jianping Shi, Xiaogang Wang et al.
- **🏷️ 机构**: CUHK / Shanghai AI Lab, CUHK
- **会议**: CVPR 2020

### Point-GNN: Graph Neural Network for 3D Object Detection in a Point Cloud.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Shi_Point-GNN_Graph_Neural_Network_for_3D_Object_Detection_in_a_CVPR_2020_paper.html) · 📚 被引 843
- **作者**: Weijing Shi, Raj Rajkumar
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Disp R-CNN: Stereo 3D Object Detection via Shape Prior Guided Instance Disparity Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Sun_Disp_R-CNN_Stereo_3D_Object_Detection_via_Shape_Prior_Guided_CVPR_2020_paper.html) · 📚 被引 93
- **作者**: Jiaming Sun, Linghao Chen, Yiming Xie, Siyu Zhang, Qinhong Jiang, Xiaowei Zhou et al.
- **🏷️ 机构**: Image Derivative Inc.
- **会议**: CVPR 2020

### PointPainting: Sequential Fusion for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Vora_PointPainting_Sequential_Fusion_for_3D_Object_Detection_CVPR_2020_paper.html) · 📚 被引 1118
- **作者**: Sourabh Vora, Alex H. Lang, Bassam Helou, Oscar Beijbom
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### HVNet: Hybrid Voxel Network for LiDAR Based 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Ye_HVNet_Hybrid_Voxel_Network_for_LiDAR_Based_3D_Object_Detection_CVPR_2020_paper.html) · 📚 被引 210
- **作者**: Maosheng Ye, Shuangjie Xu, Tongyi Cao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### SESS: Self-Ensembling Semi-Supervised 3D Object Detection.
- **链接**: [arXiv:1912.11803](https://arxiv.org/abs/1912.11803) · [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhao_SESS_Self-Ensembling_Semi-Supervised_3D_Object_Detection_CVPR_2020_paper.html) · [代码](https://github.com/Na-Z/sess) · 📚 被引 124
- **作者**: Na Zhao, Tat-Seng Chua, Gim Hee Lee
- **🏷️ 机构**: NUS
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > The performance of existing point cloud-based 3D object detection methods heavily relies on large-scale high-quality 3D annotations. However, such annotations are often tedious and expensive to collect. Semi-supervised learning is a good alternative to mitigate the data annotation issue, but has remained largely unexplored in 3D object detection. Inspired by the recent success of self-ensembling technique in semi-supervised image classification task, we propose SESS, a self-ensembling semi-supervised 3D object detection framework. Specifically, we design a thorough perturbation scheme to enhance generalization of the network on unlabeled and new unseen data. Furthermore, we propose three consistency losses to enforce the consistency between two sets of predicted 3D object proposals, to facilitate the learning of structure and semantic invariances of objects. Extensive experiments conducted on SUN RGB-D and ScanNet datasets demonstrate the effectiveness of SESS in both inductive and transductive semi-supervised 3D object detection. Our SESS achieves competitive performance compared to the state-of-the-art fully-supervised method by using only 50% labeled data. Our code is available at https://github.com/Na-Z/sess.

### Joint 3D Instance Segmentation and Object Detection for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhou_Joint_3D_Instance_Segmentation_and_Object_Detection_for_Autonomous_Driving_CVPR_2020_paper.html)
- **作者**: Dingfu Zhou, Jin Fang, Xibin Song, Liu Liu, Junbo Yin, Yuchao Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
