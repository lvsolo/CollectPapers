# 3D Detection — 2022 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 22 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Bridged Transformer for Vision and Point Cloud 3D Object Detection.
- **链接**: [arXiv:2210.01391](https://arxiv.org/abs/2210.01391) · 📚 被引 55
- **作者**: Yikai Wang, TengQi Ye, Lele Cao, Wenbing Huang, Fuchun Sun, Fengxiang He et al.
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology (BNRist), State Key Lab on Intelligent Technology and Systems,Department of Computer Science and Technology, ByteDance Inc., Institute for AI Industry Research (AIR), Tsinghua University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a crucial research topic in computer vision, which usually uses 3D point clouds as input in conventional setups. Recently, there is a trend of leveraging multiple sources of input data, such as complementing the 3D point cloud with 2D images that often have richer color and fewer noises. However, due to the heterogeneous geometrics of the 2D and 3D representations, it prevents us from applying off-the-shelf neural networks to achieve multimodal fusion. To that end, we propose Bridged Transformer (BrT), an end-to-end architecture for 3D object detection. BrT is simple and effective, which learns to identify 3D and 2D object bounding boxes from both points and image patches. A key element of BrT lies in the utilization of object queries for bridging 3D and 2D spaces, which unifies different sources of data representations in Transformer. We adopt a form of feature aggregation realized by point-to-patch projections which further strengthen the correlations between images and points. Moreover, BrT works seamlessly for fusing the point cloud with multi-view images. We experimentally show that BrT surpasses state-of-the-art methods on SUN RGB-D and ScanNetV2 datasets.

</details>

### TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers.
- **链接**: [arXiv:2203.11496](https://arxiv.org/abs/2203.11496) · 📚 被引 906
- **作者**: Xuyang Bai, Zeyu Hu, Xinge Zhu, Qingqiu Huang, Yilun Chen, Hongbo Fu et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, ADS, IAS BU, Huawei, City University of Hong Kong
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and camera are two important sensors for 3D object detection in autonomous driving. Despite the increasing popularity of sensor fusion in this field, the robustness against inferior image conditions, e.g., bad illumination and sensor misalignment, is under-explored. Existing fusion methods are easily affected by such conditions, mainly due to a hard association of LiDAR points and image pixels, established by calibration matrices. We propose TransFusion, a robust solution to LiDAR-camera fusion with a soft-association mechanism to handle inferior image conditions. Specifically, our TransFusion consists of convolutional backbones and a detection head based on a transformer decoder. The first layer of the decoder predicts initial bounding boxes from a LiDAR point cloud using a sparse set of object queries, and its second decoder layer adaptively fuses the object queries with useful image features, leveraging both spatial and contextual relationships. The attention mechanism of the transformer enables our model to adaptively determine where and what information should be taken from the image, leading to a robust and effective fusion strategy. We additionally design an image-guided query initialization strategy to deal with objects that are difficult to detect in point clouds. TransFusion achieves state-of-the-art performance on large-scale datasets. We provide extensive experiments to demonstrate its robustness against degenerated image quality and calibration errors. We also extend the proposed method to the 3D tracking task and achieve the 1st place in the leaderboard of nuScenes tracking, showing its effectiveness and generalization capability.

</details>

### Pseudo-Stereo for Monocular 3D Object Detection in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00096)
- **作者**: Yi-Nan Chen, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Focal Sparse Convolutional Networks for 3D Object Detection.
- **链接**: [arXiv:2204.12463](https://arxiv.org/abs/2204.12463) · [代码](https://github.com/dvlab-research/FocalsConv) · 📚 被引 315
- **作者**: Yukang Chen, Yanwei Li, Xiangyu Zhang, Jian Sun, Jiaya Jia
- **🏷️ 机构**: The Chinese University of Hong Kong, MEGVII Technology
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-uniformed 3D sparse data, e.g., point clouds or voxels in different spatial positions, make contribution to the task of 3D object detection in different ways. Existing basic components in sparse convolutional networks (Sparse CNNs) process all sparse data, regardless of regular or submanifold sparse convolution. In this paper, we introduce two new modules to enhance the capability of Sparse CNNs, both are based on making feature sparsity learnable with position-wise importance prediction. They are focal sparse convolution (Focals Conv) and its multi-modal variant of focal sparse convolution with fusion, or Focals Conv-F for short. The new modules can readily substitute their plain counterparts in existing Sparse CNNs and be jointly trained in an end-to-end fashion. For the first time, we show that spatially learnable sparsity in sparse convolution is essential for sophisticated 3D object detection. Extensive experiments on the KITTI, nuScenes and Waymo benchmarks validate the effectiveness of our approach. Without bells and whistles, our results outperform all existing single-model entries on the nuScenes test benchmark at the paper submission time. Code and models are at https://github.com/dvlab-research/FocalsConv.

</details>

### VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention.
- **链接**: [arXiv:2203.09704](https://arxiv.org/abs/2203.09704) · [代码](https://github.com/Gorilla-Lab-SCUT/VISTA) · 📚 被引 92
- **作者**: Shengheng Deng, Zhihao Liang, Lin Sun, Kui Jia
- **🏷️ 机构**: South China University of Technology, Magic Leap,Sunnyvale,CA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects from LiDAR point clouds is of tremendous significance in autonomous driving. In spite of good progress, accurate and reliable 3D detection is yet to be achieved due to the sparsity and irregularity of LiDAR point clouds. Among existing strategies, multi-view methods have shown great promise by leveraging the more comprehensive information from both bird's eye view (BEV) and range view (RV). These multi-view methods either refine the proposals predicted from single view via fused features, or fuse the features without considering the global spatial context; their performance is limited consequently. In this paper, we propose to adaptively fuse multi-view features in a global spatial context via Dual Cross-VIew SpaTial Attention (VISTA). The proposed VISTA is a novel plug-and-play fusion module, wherein the multi-layer perceptron widely adopted in standard attention modules is replaced with a convolutional one. Thanks to the learned attention mechanism, VISTA can produce fused features of high quality for prediction of proposals. We decouple the classification and regression tasks in VISTA, and an additional constraint of attention variance is applied that enables the attention module to focus on specific targets instead of generic points. We conduct thorough experiments on the benchmarks of nuScenes and Waymo; results confirm the efficacy of our designs. At the time of submission, our method achieves 63.0% in overall mAP and 69.8% in NDS on the nuScenes benchmark, outperforming all published methods by up to 24% in safety-crucial categories such as cyclist. The source code in PyTorch is available at https://github.com/Gorilla-Lab-SCUT/VISTA

</details>

### A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01668)
- **作者**: Hamidreza Fazlali, Yixuan Xu, Yuan Ren, Bingbing Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Homography Loss for Monocular 3D Object Detection.
- **链接**: [arXiv:2204.00754](https://arxiv.org/abs/2204.00754) · 📚 被引 48
- **作者**: Jiaqi Gu, Bojian Wu, Lubin Fan, Jianqiang Huang, Shen Cao, Zhiyu Xiang et al.
- **🏷️ 机构**: Alibaba Cloud Computing Ltd., Zhejiang University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an essential task in autonomous driving. However, most current methods consider each 3D object in the scene as an independent training sample, while ignoring their inherent geometric relations, thus inevitably resulting in a lack of leveraging spatial constraints. In this paper, we propose a novel method that takes all the objects into consideration and explores their mutual relationships to help better estimate the 3D boxes. Moreover, since 2D detection is more reliable currently, we also investigate how to use the detected 2D boxes as guidance to globally constrain the optimization of the corresponding predicted 3D boxes. To this end, a differentiable loss function, termed as Homography Loss, is proposed to achieve the goal, which exploits both 2D and 3D information, aiming at balancing the positional relationships between different objects by global constraints, so as to obtain more accurately predicted 3D boxes. Thanks to the concise design, our loss function is universal and can be plugged into any mature monocular 3D detector, while significantly boosting the performance over their baseline. Experiments demonstrate that our method yields the best performance (Nov. 2021) compared with the other state-of-the-arts by a large margin on KITTI 3D datasets.

</details>

### LiDAR Snowfall Simulation for Robust 3D Object Detection.
- **链接**: [arXiv:2203.15118](https://arxiv.org/abs/2203.15118) · [代码](https://github.com/SysCV/LiDAR_snow_sim) · 📚 被引 168
- **作者**: Martin Hahner, Christos Sakaridis, Mario Bijelic, Felix Heide, Fisher Yu, Dengxin Dai et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, Princeton University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a central task for applications such as autonomous driving, in which the system needs to localize and classify surrounding traffic agents, even in the presence of adverse weather. In this paper, we address the problem of LiDAR-based 3D object detection under snowfall. Due to the difficulty of collecting and annotating training data in this setting, we propose a physically based method to simulate the effect of snowfall on real clear-weather LiDAR point clouds. Our method samples snow particles in 2D space for each LiDAR line and uses the induced geometry to modify the measurement for each LiDAR beam accordingly. Moreover, as snowfall often causes wetness on the ground, we also simulate ground wetness on LiDAR point clouds. We use our simulation to generate partially synthetic snowy LiDAR data and leverage these data for training 3D object detection models that are robust to snowfall. We conduct an extensive evaluation using several state-of-the-art 3D object detection methods and show that our simulation consistently yields significant performance gains on the real snowy STF dataset compared to clear-weather baselines and competing simulation approaches, while not sacrificing performance in clear weather. Our code is available at www.github.com/SysCV/LiDAR_snow_sim.

</details>

### Voxel Set Transformer: A Set-to-Set Approach to 3D Object Detection from Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00823) · 📚 被引 222
- **作者**: Chenhang He, Ruihuang Li, Shuai Li, Lei Zhang
- **🏷️ 机构**: The Hong Kong Polytechnic University
- **会议**: CVPR 2022

### Point Density-Aware Voxels for LiDAR 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00828) · 📚 被引 148
- **作者**: Jordan S. K. Hu, Tianshu Kuai, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute
- **会议**: CVPR 2022

### Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00258)
- **作者**: Hanjiang Hu, Zuxin Liu, Sharad Chitlangia, Akhil Agnihotri, Ding Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### MonoDTR: Monocular 3D Object Detection with Depth-Aware Transformer.
- **链接**: [arXiv:2203.10981](https://arxiv.org/abs/2203.10981) · [代码](https://github.com/kuanchihhuang/MonoDTR) · 📚 被引 225
- **作者**: Kuan-Chih Huang, Tsung-Han Wu, Hung-Ting Su, Winston H. Hsu
- **🏷️ 机构**: National Taiwan University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important yet challenging task in autonomous driving. Some existing methods leverage depth information from an off-the-shelf depth estimator to assist 3D detection, but suffer from the additional computational burden and achieve limited performance caused by inaccurate depth priors. To alleviate this, we propose MonoDTR, a novel end-to-end depth-aware transformer network for monocular 3D object detection. It mainly consists of two components: (1) the Depth-Aware Feature Enhancement (DFE) module that implicitly learns depth-aware features with auxiliary supervision without requiring extra computation, and (2) the Depth-Aware Transformer (DTR) module that globally integrates context- and depth-aware features. Moreover, different from conventional pixel-wise positional encodings, we introduce a novel depth positional encoding (DPE) to inject depth positional hints into transformers. Our proposed depth-aware modules can be easily plugged into existing image-only monocular 3D object detectors to improve the performance. Extensive experiments on the KITTI dataset demonstrate that our approach outperforms previous state-of-the-art monocular-based methods and achieves real-time detection. Code is available at https://github.com/kuanchihhuang/MonoDTR

</details>

### 3D-VField: Adversarial Augmentation of Point Clouds for Domain Generalization in 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01678) · 📚 被引 67
- **作者**: Alexander Lehner, Stefano Gasperini, Alvaro Marcos-Ramiro, Michael Schmidt, Mohammad-Ali Nikouei Mahani, Nassir Navab et al.
- **🏷️ 机构**: Technical University of Munich, BMW Group
- **会议**: CVPR 2022

### Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00386)
- **作者**: Peixuan Li, Jieyu Jin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Point-to-Voxel Knowledge Distillation for LiDAR Semantic Segmentation.
- **链接**: [arXiv:2206.02099](https://arxiv.org/abs/2206.02099) · [代码](https://github.com/cardwing/Codes-for-PVKD) · 📚 被引 200
- **作者**: Yuenan Hou, Xinge Zhu, Yuexin Ma, Chen Change Loy, Yikang Li
- **🏷️ 机构**: Shanghai AI Laboratory, The Chinese University of Hong Kong, ShanghaiTech University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This article addresses the problem of distilling knowledge from a large teacher model to a slim student network for LiDAR semantic segmentation. Directly employing previous distillation approaches yields inferior results due to the intrinsic challenges of point cloud, i.e., sparsity, randomness and varying density. To tackle the aforementioned problems, we propose the Point-to-Voxel Knowledge Distillation (PVD), which transfers the hidden knowledge from both point level and voxel level. Specifically, we first leverage both the pointwise and voxelwise output distillation to complement the sparse supervision signals. Then, to better exploit the structural information, we divide the whole point cloud into several supervoxels and design a difficulty-aware sampling strategy to more frequently sample supervoxels containing less-frequent classes and faraway objects. On these supervoxels, we propose inter-point and inter-voxel affinity distillation, where the similarity information between points and voxels can help the student model better capture the structural information of the surrounding environment. We conduct extensive experiments on two popular LiDAR segmentation benchmarks, i.e., nuScenes and SemanticKITTI. On both benchmarks, our PVD consistently outperforms previous distillation approaches by a large margin on three representative backbones, i.e., Cylinder3D, SPVNAS and MinkowskiNet. Notably, on the challenging nuScenes and SemanticKITTI datasets, our method can achieve roughly 75% MACs reduction and 2x speedup on the competitive Cylinder3D model and rank 1st on the SemanticKITTI leaderboard among all published algorithms. Our code is available at https://github.com/cardwing/Codes-for-PVKD.

</details>

### DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01667)
- **作者**: Yingwei Li, Adams Wei Yu, Tianjian Meng, Benjamin Caine, Jiquan Ngiam, Daiyi Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### LIFT: Learning 4D LiDAR Image Fusion Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01666) · 📚 被引 36
- **作者**: Yihan Zeng, Da Zhang, Chunwei Wang, Zhenwei Miao, Ting Liu, Xin Zhan et al.
- **🏷️ 机构**: AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Alibaba DAMO Academy
- **会议**: CVPR 2022

### SS3D: Sparsely-Supervised 3D Object Detection from Point Cloud.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00824) · 📚 被引 34
- **作者**: Chuandong Liu, Chenqiang Gao, Fangcen Liu, Jiang Liu, Deyu Meng, Xinbo Gao
- **🏷️ 机构**: School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications,Chongqing,China, Meta,Menlo Park,USA, Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China
- **会议**: CVPR 2022

### Boosting 3D Object Detection by Simulating Multimodality on Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01327) · 📚 被引 35
- **作者**: Wu Zheng, Mingxuan Hong, Li Jiang, Chi-Wing Fu
- **🏷️ 机构**: CUHK,Department of Computer Science and Engineering, Max Planck Institute
- **会议**: CVPR 2022

### Diversity Matters: Fully Exploiting Depth Clues for Reliable Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00281) · 📚 被引 87
- **作者**: Zhuoling Li, Zhan Qu, Yang Zhou, Jianzhuang Liu, Haoqian Wang, Lihui Jiang
- **🏷️ 机构**: Tsinghua University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022

### Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02065)
- **作者**: Xiaoqing Ye, Mao Shu, Hanyu Li, Yifeng Shi, Yingying Li, Guangjie Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00098)
- **作者**: Yanan Zhang, Jiaxin Chen, Di Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022
