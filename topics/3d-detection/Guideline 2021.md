# 3D Detection — 2021 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### RangeDet: In Defense of Range View for LiDAR-based 3D Object Detection.
- **链接**: [arXiv:2103.10039](https://arxiv.org/abs/2103.10039)
- **作者**: Lue Fan, Xuan Xiong, Feng Wang, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA), TuSimple
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose an anchor-free single-stage LiDAR-based 3D object detector -- RangeDet. The most notable difference with previous works is that our method is purely based on the range view representation. Compared with the commonly used voxelized or Bird's Eye View (BEV) representations, the range view representation is more compact and without quantization error. Although there are works adopting it for semantic segmentation, its performance in object detection is largely behind voxelized or BEV counterparts. We first analyze the existing range-view-based methods and find two issues overlooked by previous works: 1) the scale variation between nearby and far away objects; 2) the inconsistency between the 2D range image coordinates used in feature extraction and the 3D Cartesian coordinates used in output. Then we deliberately design three components to address these issues in our RangeDet. We test our RangeDet in the large-scale Waymo Open Dataset (WOD). Our best model achieves 72.9/75.9/65.8 3D AP on vehicle/pedestrian/cyclist. These results outperform other range-view-based methods by a large margin (~20 3D AP in vehicle detection), and are overall comparable with the state-of-the-art multi-view-based methods. Codes will be public.

</details>

### Fog Simulation on Real LiDAR Point Clouds for 3D Object Detection in Adverse Weather.
- **链接**: [arXiv:2108.05249](https://arxiv.org/abs/2108.05249)
- **作者**: Martin Hahner, Christos Sakaridis, Dengxin Dai, Luc Van Gool
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work addresses the challenging task of LiDAR-based 3D object detection in foggy weather. Collecting and annotating data in such a scenario is very time, labor and cost intensive. In this paper, we tackle this problem by simulating physically accurate fog into clear-weather scenes, so that the abundant existing real datasets captured in clear weather can be repurposed for our task. Our contributions are twofold: 1) We develop a physically valid fog simulation method that is applicable to any LiDAR dataset. This unleashes the acquisition of large-scale foggy training data at no extra cost. These partially synthetic data can be used to improve the robustness of several perception methods, such as 3D object detection and tracking or simultaneous localization and mapping, on real foggy data. 2) Through extensive experiments with several state-of-the-art detection approaches, we show that our fog simulation can be leveraged to significantly improve the performance for 3D object detection in the presence of fog. Thus, we are the first to provide strong 3D object detection baselines on the Seeing Through Fog dataset. Our code is available at www.trace.ethz.ch/lidar_fog_simulation.

</details>

### Gated3D: Monocular 3D Object Detection From Temporal Illumination Cues.
- **链接**: [arXiv:2102.03602](https://arxiv.org/abs/2102.03602) · 📚 被引 10
- **作者**: Frank D. Julca-Aguilar, Jason Taylor, Mario Bijelic, Fahim Mannan, Ethan Tseng, Felix Heide
- **🏷️ 机构**: Algolux, Mercedes-Benz AG, Princeton University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Today's state-of-the-art methods for 3D object detection are based on lidar, stereo, or monocular cameras. Lidar-based methods achieve the best accuracy, but have a large footprint, high cost, and mechanically-limited angular sampling rates, resulting in low spatial resolution at long ranges. Recent approaches based on low-cost monocular or stereo cameras promise to overcome these limitations but struggle in low-light or low-contrast regions as they rely on passive CMOS sensors. In this work, we propose a novel 3D object detection modality that exploits temporal illumination cues from a low-cost monocular gated imager. We propose a novel deep detector architecture, Gated3D, that is tailored to temporal illumination cues from three gated images. Gated images allow us to exploit mature 2D object feature extractors that guide the 3D predictions through a frustum segment estimation. We assess the proposed method on a novel 3D detection dataset that includes gated imagery captured in over 10,000 km of driving data. We validate that our method outperforms state-of-the-art monocular and stereo approaches at long distances. We will release our code and dataset, opening up a new sensor modality as an avenue to replace lidar in autonomous driving.

</details>

### Exploring Geometry-aware Contrast and Clustering Harmonization for Self-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00328)
- **作者**: Hanxue Liang, Chenhan Jiang, Dapeng Feng, Xin Chen, Hang Xu, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Group-Free 3D Object Detection via Transformers.
- **链接**: [arXiv:2104.00678](https://arxiv.org/abs/2104.00678) · [代码](https://github.com/zeliu98/Group-Free-3D)
- **作者**: Ze Liu, Zheng Zhang, Yue Cao, Han Hu, Xin Tong
- **🏷️ 机构**: University of Science and Technology of China, Microsoft Research Asia
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, directly detecting 3D objects from 3D point clouds has received increasing attention. To extract object representation from an irregular point cloud, existing methods usually take a point grouping step to assign the points to an object candidate so that a PointNet-like network could be used to derive object features from the grouped points. However, the inaccurate point assignments caused by the hand-crafted grouping scheme decrease the performance of 3D object detection. In this paper, we present a simple yet effective method for directly detecting 3D objects from the 3D point cloud. Instead of grouping local points to each object candidate, our method computes the feature of an object from all the points in the point cloud with the help of an attention mechanism in the Transformers \cite{vaswani2017attention}, where the contribution of each point is automatically learned in the network training. With an improved attention stacking scheme, our method fuses object features in different stages and generates more accurate object detection results. With few bells and whistles, the proposed method achieves state-of-the-art 3D object detection performance on two widely used benchmarks, ScanNet V2 and SUN RGB-D. The code and models are publicly available at \url{https://github.com/zeliu98/Group-Free-3D}

</details>

### AutoShape: Real-Time Shape-Aware Monocular 3D Object Detection.
- **链接**: [arXiv:2108.11127](https://arxiv.org/abs/2108.11127) · [代码](https://github.com/zongdai/AutoShape) · 📚 被引 140
- **作者**: Zongdai Liu, Dingfu Zhou, Feixiang Lu, Jin Fang, Liangjun Zhang
- **🏷️ 机构**: National Engineering Laboratory of Deep Learning Technology and Application,Robotics and Autonomous Driving Laboratory, Baidu Research,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing deep learning-based approaches for monocular 3D object detection in autonomous driving often model the object as a rotated 3D cuboid while the object's geometric shape has been ignored. In this work, we propose an approach for incorporating the shape-aware 2D/3D constraints into the 3D detection framework. Specifically, we employ the deep neural network to learn distinguished 2D keypoints in the 2D image domain and regress their corresponding 3D coordinates in the local 3D object coordinate first. Then the 2D/3D geometric constraints are built by these correspondences for each object to boost the detection performance. For generating the ground truth of 2D/3D keypoints, an automatic model-fitting approach has been proposed by fitting the deformed 3D object model and the object mask in the 2D image. The proposed framework has been verified on the public KITTI dataset and the experimental results demonstrate that by using additional geometrical constraints the detection performance has been significantly improved as compared to the baseline method. More importantly, the proposed framework achieves state-of-the-art performance with real time. Data and code will be available at https://github.com/zongdai/AutoShape

</details>

### Geometry Uncertainty Projection Network for Monocular 3D Object Detection.
- **链接**: [arXiv:2107.13774](https://arxiv.org/abs/2107.13774)
- **作者**: Yan Lu, Xinzhu Ma, Lei Yang, Tianzhu Zhang, Yating Liu, Qi Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Geometry Projection is a powerful depth estimation method in monocular 3D object detection. It estimates depth dependent on heights, which introduces mathematical priors into the deep model. But projection process also introduces the error amplification problem, in which the error of the estimated height will be amplified and reflected greatly at the output depth. This property leads to uncontrollable depth inferences and also damages the training efficiency. In this paper, we propose a Geometry Uncertainty Projection Network (GUP Net) to tackle the error amplification problem at both inference and training stages. Specifically, a GUP module is proposed to obtains the geometry-guided uncertainty of the inferred depth, which not only provides high reliable confidence for each depth but also benefits depth learning. Furthermore, at the training stage, we propose a Hierarchical Task Learning strategy to reduce the instability caused by error amplification. This learning algorithm monitors the learning situation of each task by a proposed indicator and adaptively assigns the proper loss weights for different tasks according to their pre-tasks situation. Based on that, each task starts learning only when its pre-tasks are learned well, which can significantly improve the stability and efficiency of the training process. Extensive experiments demonstrate the effectiveness of the proposed method. The overall model can infer more reliable object depth than existing methods and outperforms the state-of-the-art image-based monocular 3D detectors by 3.74% and 4.7% AP40 of the car and pedestrian categories on the KITTI benchmark.

</details>

### Multi-Echo LiDAR for 3D Object Detection.
- **链接**: [arXiv:2107.11470](https://arxiv.org/abs/2107.11470)
- **作者**: Yunze Man, Xinshuo Weng, Prasanna Kumar Sivakumar, Matthew O'Toole, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University, DENSO
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR sensors can be used to obtain a wide range of measurement signals other than a simple 3D point cloud, and those signals can be leveraged to improve perception tasks like 3D object detection. A single laser pulse can be partially reflected by multiple objects along its path, resulting in multiple measurements called echoes. Multi-echo measurement can provide information about object contours and semi-transparent surfaces which can be used to better identify and locate objects. LiDAR can also measure surface reflectance (intensity of laser pulse return), as well as ambient light of the scene (sunlight reflected by objects). These signals are already available in commercial LiDAR devices but have not been used in most LiDAR-based detection models. We present a 3D object detection model which leverages the full spectrum of measurement signals provided by LiDAR. First, we propose a multi-signal fusion (MSF) module to combine (1) the reflectance and ambient features extracted with a 2D CNN, and (2) point cloud features extracted using a 3D graph neural network (GNN). Second, we propose a multi-echo aggregation (MEA) module to combine the information encoded in different set of echo points. Compared with traditional single echo point cloud methods, our proposed Multi-Signal LiDAR Detector (MSLiD) extracts richer context information from a wider range of sensing measurements and achieves more accurate 3D object detection. Experiments show that by incorporating the multi-modality of LiDAR, our method outperforms the state-of-the-art by up to 9.1%.

</details>

### Pyramid R-CNN: Towards Better Performance and Adaptability for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00272) · 📚 被引 172
- **作者**: Jiageng Mao, Minzhe Niu, Haoyue Bai, Xiaodan Liang, Hang Xu, Chunjing Xu
- **🏷️ 机构**: The Chinese University of Hong Kong, Huawei Noah&#x2019;s Ark Lab, HKUST
- **会议**: ICCV 2021

### Voxel Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00315)
- **作者**: Jiageng Mao, Yujing Xue, Minzhe Niu, Haoyue Bai, Jiashi Feng, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### An End-to-End Transformer Model for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00290) · 📚 被引 481
- **作者**: Ishan Misra, Rohit Girdhar, Armand Joulin
- **🏷️ 机构**: Facebook AI Research
- **会议**: ICCV 2021

### Is Pseudo-Lidar needed for Monocular 3D Object detection?
- **链接**: [arXiv:2108.06417](https://arxiv.org/abs/2108.06417)
- **作者**: Dennis Park, Rares Ambrus, Vitor Guizilini, Jie Li, Adrien Gaidon
- **🏷️ 机构**: Toyota Research Institute
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in 3D object detection from single images leverages monocular depth estimation as a way to produce 3D pointclouds, turning cameras into pseudo-lidar sensors. These two-stage detectors improve with the accuracy of the intermediate depth estimation network, which can itself be improved without manual labels via large-scale self-supervised learning. However, they tend to suffer from overfitting more than end-to-end methods, are more complex, and the gap with similar lidar-based detectors remains significant. In this work, we propose an end-to-end, single stage, monocular 3D object detector, DD3D, that can benefit from depth pre-training like pseudo-lidar methods, but without their limitations. Our architecture is designed for effective information transfer between depth estimation and 3D detection, allowing us to scale with the amount of unlabeled pre-training data. Our method achieves state-of-the-art results on two challenging benchmarks, with 16.34% and 9.28% AP for Cars and Pedestrians (respectively) on the KITTI-3D benchmark, and 41.5% mAP on NuScenes.

</details>

### RandomRooms: Unsupervised Pre-training from Synthetic Shapes and Randomized Layouts for 3D Object Detection.
- **链接**: [arXiv:2108.07794](https://arxiv.org/abs/2108.07794)
- **作者**: Yongming Rao, Benlin Liu, Yi Wei, Jiwen Lu, Cho-Jui Hsieh, Jie Zhou
- **🏷️ 机构**: Tsinghua University, UCLA
- **会议**: ICCV 2021

### Improving 3D Object Detection with Channel-wise Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00274) · 📚 被引 278
- **作者**: Hualian Sheng, Sijia Cai, Yuan Liu, Bing Deng, Jianqiang Huang, Xian-Sheng Hua et al.
- **🏷️ 机构**: Zhejiang University,College of Information Science and Electronic Engineering, Alibaba Group,DAMO Academy
- **会议**: ICCV 2021

### Geometry-based Distance Decomposition for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01489) · 📚 被引 147
- **作者**: Xuepeng Shi, Qi Ye, Xiaozhi Chen, Chuangrong Chen, Zhixiang Chen, Tae-Kyun Kim
- **🏷️ 机构**: Imperial College London, Zhejiang University, DJI
- **会议**: ICCV 2021

### Are we Missing Confidence in Pseudo-LiDAR Methods for Monocular 3D Object Detection?
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00321) · 📚 被引 35
- **作者**: Andrea Simonelli, Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder, Elisa Ricci
- **🏷️ 机构**: University of Trento,Fondazione Bruno Kessler, Facebook Reality Labs
- **会议**: ICCV 2021

### You Don't Only Look Once: Constructing Spatial-Temporal Memory for Integrated 3D Object Detection and Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00317)
- **作者**: Jiaming Sun, Yiming Xie, Siyu Zhang, Linghao Chen, Guofeng Zhang, Hujun Bao et al.
- **🏷️ 机构**: Zhejiang University, SenseTime Research
- **会议**: ICCV 2021

### VENet: Voting Enhancement Network for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00369) · 📚 被引 59
- **作者**: Qian Xie, Yu-Kun Lai, Jing Wu, Zhoutao Wang, Dening Lu, Mingqiang Wei et al.
- **🏷️ 机构**: Nanjing University of Aeronautics and Astronautics, Cardiff University
- **会议**: ICCV 2021

### SPG: Unsupervised Domain Adaptation for 3D Object Detection via Semantic Point Generation.
- **链接**: [arXiv:2108.06709](https://arxiv.org/abs/2108.06709) · 📚 被引 144
- **作者**: Qiangeng Xu, Yin Zhou, Weiyue Wang, Charles R. Qi, Dragomir Anguelov
- **🏷️ 机构**: University of Southern California, Waymo, LLC
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, a LiDAR-based object detector should perform reliably at different geographic locations and under various weather conditions. While recent 3D detection research focuses on improving performance within a single domain, our study reveals that the performance of modern detectors can drop drastically cross-domain. In this paper, we investigate unsupervised domain adaptation (UDA) for LiDAR-based 3D object detection. On the Waymo Domain Adaptation dataset, we identify the deteriorating point cloud quality as the root cause of the performance drop. To address this issue, we present Semantic Point Generation (SPG), a general approach to enhance the reliability of LiDAR detectors against domain shifts. Specifically, SPG generates semantic points at the predicted foreground regions and faithfully recovers missing parts of the foreground objects, which are caused by phenomena such as occlusions, low reflectance or weather interference. By merging the semantic points with the original points, we obtain an augmented point cloud, which can be directly consumed by modern LiDAR-based detectors. To validate the wide applicability of SPG, we experiment with two representative detectors, PointPillars and PV-RCNN. On the UDA task, SPG significantly improves both detectors across all object categories of interest and at all difficulty levels. SPG can also benefit object detection in the original domain. On the Waymo Open Dataset and KITTI, SPG improves 3D detection results of these two methods across all categories. Combined with PV-RCNN, SPG achieves state-of-the-art 3D detection results on KITTI.

</details>

### The Devil is in the Task: Exploiting Reciprocal Appearance-Localization Features for Monocular 3D Object Detection.
- **链接**: [arXiv:2112.14023](https://arxiv.org/abs/2112.14023) · 📚 被引 52
- **作者**: Zhikang Zou, Xiaoqing Ye, Liang Du, Xianhui Cheng, Xiao Tan, Li Zhang et al.
- **🏷️ 机构**: Baidu Inc.,China, Fudan University, MOE Key Laboratory of Computational Neuroscience and Brain-Inspired Intelligence, Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, Fudan University,School of Computer Science
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Low-cost monocular 3D object detection plays a fundamental role in autonomous driving, whereas its accuracy is still far from satisfactory. In this paper, we dig into the 3D object detection task and reformulate it as the sub-tasks of object localization and appearance perception, which benefits to a deep excavation of reciprocal information underlying the entire task. We introduce a Dynamic Feature Reflecting Network, named DFR-Net, which contains two novel standalone modules: (i) the Appearance-Localization Feature Reflecting module (ALFR) that first separates taskspecific features and then self-mutually reflects the reciprocal features; (ii) the Dynamic Intra-Trading module (DIT) that adaptively realigns the training processes of various sub-tasks via a self-learning manner. Extensive experiments on the challenging KITTI dataset demonstrate the effectiveness and generalization of DFR-Net. We rank 1st among all the monocular 3D object detectors in the KITTI test set (till March 16th, 2021). The proposed method is also easy to be plug-and-play in many cutting-edge 3D detection frameworks at negligible cost to boost performance. The code will be made publicly available.

</details>

### RPVNet: A Deep and Efficient Range-Point-Voxel Fusion Network for LiDAR Point Cloud Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01572) · 📚 被引 321
- **作者**: Jianyun Xu, Ruixiang Zhang, Jian Dou, Yushi Zhu, Jie Sun, Shiliang Pu
- **🏷️ 机构**: Hikvision Research Institute
- **会议**: ICCV 2021
