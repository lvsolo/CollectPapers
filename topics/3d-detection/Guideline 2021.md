# 3D Detection — 2021 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### RangeDet: In Defense of Range View for LiDAR-based 3D Object Detection.
- **链接**: [arXiv:2103.10039](https://arxiv.org/abs/2103.10039) · 📚 被引 245
- **作者**: Lue Fan, Xuan Xiong, Feng Wang, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA), TuSimple
- **会议**: ICCV 2021

### Fog Simulation on Real LiDAR Point Clouds for 3D Object Detection in Adverse Weather.
- **链接**: [arXiv:2108.05249](https://arxiv.org/abs/2108.05249) · 📚 被引 205
- **作者**: Martin Hahner, Christos Sakaridis, Dengxin Dai, Luc Van Gool
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: ICCV 2021

### Gated3D: Monocular 3D Object Detection From Temporal Illumination Cues.
- **链接**: [arXiv:2102.03602](https://arxiv.org/abs/2102.03602) · 📚 被引 10
- **作者**: Frank D. Julca-Aguilar, Jason Taylor, Mario Bijelic, Fahim Mannan, Ethan Tseng, Felix Heide
- **🏷️ 机构**: Algolux, Mercedes-Benz AG, Princeton University
- **会议**: ICCV 2021

</details>

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
- **链接**: [arXiv:2104.00678](https://arxiv.org/abs/2104.00678) · 📚 被引 297
- **作者**: Ze Liu, Zheng Zhang, Yue Cao, Han Hu, Xin Tong
- **🏷️ 机构**: University of Science and Technology of China, Microsoft Research Asia
- **会议**: ICCV 2021

### AutoShape: Real-Time Shape-Aware Monocular 3D Object Detection.
- **链接**: [arXiv:2108.11127](https://arxiv.org/abs/2108.11127) · 📚 被引 140
- **作者**: Zongdai Liu, Dingfu Zhou, Feixiang Lu, Jin Fang, Liangjun Zhang
- **🏷️ 机构**: National Engineering Laboratory of Deep Learning Technology and Application,Robotics and Autonomous Driving Laboratory, Baidu Research,China
- **会议**: ICCV 2021

</details>

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

### Multi-Echo LiDAR for 3D Object Detection.
- **链接**: [arXiv:2107.11470](https://arxiv.org/abs/2107.11470) · 📚 被引 10
- **作者**: Yunze Man, Xinshuo Weng, Prasanna Kumar Sivakumar, Matthew O'Toole, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University, DENSO
- **会议**: ICCV 2021

### Pyramid R-CNN: Towards Better Performance and Adaptability for 3D Object Detection.
- **链接**: [arXiv:2109.02499](https://arxiv.org/abs/2109.02499) · 📚 被引 172
- **作者**: Jiageng Mao, Minzhe Niu, Haoyue Bai, Xiaodan Liang, Hang Xu, Chunjing Xu
- **🏷️ 机构**: The Chinese University of Hong Kong, Huawei Noah&#x2019;s Ark Lab, HKUST
- **会议**: ICCV 2021

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a key module for safety-critical robotics applications such as autonomous driving. For these applications, we care most about how the detections affect the ego-agent's behavior and safety (the egocentric perspective). Intuitively, we seek more accurate descriptions of object geometry when it's more likely to interfere with the ego-agent's motion trajectory. However, current detection metrics, based on box Intersection-over-Union (IoU), are object-centric and aren't designed to capture the spatio-temporal relationship between objects and the ego-agent. To address this issue, we propose a new egocentric measure to evaluate 3D object detection, namely Support Distance Error (SDE). Our analysis based on SDE reveals that the egocentric detection quality is bounded by the coarse geometry of the bounding boxes. Given the insight that SDE would benefit from more accurate geometry descriptions, we propose to represent objects as amodal contours, specifically amodal star-shaped polygons, and devise a simple model, StarPoly, to predict such contours. Our experiments on the large-scale Waymo Open Dataset show that SDE better reflects the impact of detection quality on the ego-agent's safety compared to IoU; and the estimated contours from StarPoly consistently improve the egocentric detection quality over recent 3D object detectors.

</details>

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
- **链接**: [arXiv:2109.08141](https://arxiv.org/abs/2109.08141) · 📚 被引 481
- **作者**: Ishan Misra, Rohit Girdhar, Armand Joulin
- **🏷️ 机构**: Facebook AI Research
- **会议**: ICCV 2021

### Is Pseudo-Lidar needed for Monocular 3D Object detection?
- **链接**: [arXiv:2108.06417](https://arxiv.org/abs/2108.06417) · 📚 被引 315
- **作者**: Dennis Park, Rares Ambrus, Vitor Guizilini, Jie Li, Adrien Gaidon
- **🏷️ 机构**: Toyota Research Institute
- **会议**: ICCV 2021

### RandomRooms: Unsupervised Pre-training from Synthetic Shapes and Randomized Layouts for 3D Object Detection.
- **链接**: [arXiv:2108.07794](https://arxiv.org/abs/2108.07794) · 📚 被引 45
- **作者**: Yongming Rao, Benlin Liu, Yi Wei, Jiwen Lu, Cho-Jui Hsieh, Jie Zhou
- **🏷️ 机构**: Tsinghua University, UCLA
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00317) · 📚 被引 11
- **作者**: Jiaming Sun, Yiming Xie, Siyu Zhang, Linghao Chen, Guofeng Zhang, Hujun Bao et al.
- **🏷️ 机构**: Zhejiang University, SenseTime Research
- **会议**: ICCV 2021

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While current 3D object recognition research mostly focuses on the real-time, onboard scenario, there are many offboard use cases of perception that are largely under-explored, such as using machines to automatically generate high-quality 3D labels. Existing 3D object detectors fail to satisfy the high-quality requirement for offboard uses due to the limited input and speed constraints. In this paper, we propose a novel offboard 3D object detection pipeline using point cloud sequence data. Observing that different frames capture complementary views of objects, we design the offboard detector to make use of the temporal points through both multi-frame object detection and novel object-centric refinement models. Evaluated on the Waymo Open Dataset, our pipeline named 3D Auto Labeling shows significant gains compared to the state-of-the-art onboard detectors and our offboard baselines. Its performance is even on par with human labels verified through a human label study. Further experiments demonstrate the application of auto labels for semi-supervised learning and provide extensive analysis to validate various design choices.

</details>

### Categorical Depth Distribution Network for Monocular 3D Object Detection.
- **链接**: [arXiv:2103.01100](https://arxiv.org/abs/2103.01100) · 📚 被引 517
- **作者**: Cody Reading, Ali Harakeh, Julia Chae, Steven L. Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is a key problem for autonomous vehicles, as it provides a solution with simple configuration compared to typical multi-sensor systems. The main challenge in monocular 3D detection lies in accurately predicting object depth, which must be inferred from object and scene cues due to the lack of direct range measurement. Many methods attempt to directly estimate depth to assist in 3D detection, but show limited performance as a result of depth inaccuracy. Our proposed solution, Categorical Depth Distribution Network (CaDDN), uses a predicted categorical depth distribution for each pixel to project rich contextual feature information to the appropriate depth interval in 3D space. We then use the computationally efficient bird's-eye-view projection and single-stage detector to produce the final output bounding boxes. We design CaDDN as a fully differentiable end-to-end approach for joint depth estimation and object detection. We validate our approach on the KITTI 3D object detection benchmark, where we rank 1st among published monocular methods. We also provide the first monocular 3D detection results on the newly released Waymo Open Dataset. We provide a code release for CaDDN which is made available.

</details>

### The Devil is in the Task: Exploiting Reciprocal Appearance-Localization Features for Monocular 3D Object Detection.
- **链接**: [arXiv:2112.14023](https://arxiv.org/abs/2112.14023) · 📚 被引 52
- **作者**: Zhikang Zou, Xiaoqing Ye, Liang Du, Xianhui Cheng, Xiao Tan, Li Zhang et al.
- **🏷️ 机构**: Baidu Inc.,China, Fudan University, MOE Key Laboratory of Computational Neuroscience and Brain-Inspired Intelligence, Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, Fudan University,School of Computer Science
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Low-cost monocular 3D object detection plays a fundamental role in autonomous driving, whereas its accuracy is still far from satisfactory. In this paper, we dig into the 3D object detection task and reformulate it as the sub-tasks of object localization and appearance perception, which benefits to a deep excavation of reciprocal information underlying the entire task. We introduce a Dynamic Feature Reflecting Network, named DFR-Net, which contains two novel standalone modules: (i) the Appearance-Localization Feature Reflecting module (ALFR) that first separates taskspecific features and then self-mutually reflects the reciprocal features; (ii) the Dynamic Intra-Trading module (DIT) that adaptively realigns the training processes of various sub-tasks via a self-learning manner. Extensive experiments on the challenging KITTI dataset demonstrate the effectiveness and generalization of DFR-Net. We rank 1st among all the monocular 3D object detectors in the KITTI test set (till March 16th, 2021). The proposed method is also easy to be plug-and-play in many cutting-edge 3D detection frameworks at negligible cost to boost performance. The code will be made publicly available.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The objective of this paper is to learn context- and depth-aware feature representation to solve the problem of monocular 3D object detection. We make following contributions: (i) rather than appealing to the complicated pseudo-LiDAR based approach, we propose a depth-conditioned dynamic message propagation (DDMP) network to effectively integrate the multi-scale depth information with the image context;(ii) this is achieved by first adaptively sampling context-aware nodes in the image context and then dynamically predicting hybrid depth-dependent filter weights and affinity matrices for propagating information; (iii) by augmenting a center-aware depth encoding (CDE) task, our method successfully alleviates the inaccurate depth prior; (iv) we thoroughly demonstrate the effectiveness of our proposed approach and show state-of-the-art results among the monocular-based approaches on the KITTI benchmark dataset. Particularly, we rank $1^{st}$ in the highly competitive KITTI monocular 3D object detection track on the submission day (November 16th, 2020). Code and models are released at \url{https://github.com/fudan-zvg/DDMP}

</details>

### ST3D: Self-Training for Unsupervised Domain Adaptation on 3D Object Detection.
- **链接**: [arXiv:2103.05346](https://arxiv.org/abs/2103.05346) · [代码](https://github.com/CVMI-Lab/ST3D) · 📚 被引 182
- **作者**: Jihan Yang, Shaoshuai Shi, Zhe Wang, Hongsheng Li, Xiaojuan Qi
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new domain adaptive self-training pipeline, named ST3D, for unsupervised domain adaptation on 3D object detection from point clouds. First, we pre-train the 3D detector on the source domain with our proposed random object scaling strategy for mitigating the negative effects of source domain bias. Then, the detector is iteratively improved on the target domain by alternatively conducting two steps, which are the pseudo label updating with the developed quality-aware triplet memory bank and the model training with curriculum data augmentation. These specific designs for 3D object detection enable the detector to be trained with consistent and high-quality pseudo labels and to avoid overfitting to the large number of easy examples in pseudo labeled data. Our ST3D achieves state-of-the-art performance on all evaluated datasets and even surpasses fully supervised results on KITTI 3D object detection benchmark. Code will be available at https://github.com/CVMI-Lab/ST3D.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important task in autonomous driving. It can be easily intractable where there exists ego-car pose change w.r.t. ground plane. This is common due to the slight fluctuation of road smoothness and slope. Due to the lack of insight in industrial application, existing methods on open datasets neglect the camera pose information, which inevitably results in the detector being susceptible to camera extrinsic parameters. The perturbation of objects is very popular in most autonomous driving cases for industrial products. To this end, we propose a novel method to capture camera pose to formulate the detector free from extrinsic perturbation. Specifically, the proposed framework predicts camera extrinsic parameters by detecting vanishing point and horizon change. A converter is designed to rectify perturbative features in the latent space. By doing so, our 3D detector works independent of the extrinsic parameter variations and produces accurate results in realistic cases, e.g., potholed and uneven roads, where almost all existing monocular detectors fail to handle. Experiments demonstrate our method yields the best performance compared with the other state-of-the-arts by a large margin on both KITTI 3D and nuScenes datasets.

</details>

### VoxelContext-Net: An Octree Based Framework for Point Cloud Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Que_VoxelContext-Net_An_Octree_Based_Framework_for_Point_Cloud_Compression_CVPR_2021_paper.html)
- **作者**: Zizheng Que, Guo Lu, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
