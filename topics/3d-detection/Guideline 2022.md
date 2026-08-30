# 3D Detection — 2022 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 30 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Bridged Transformer for Vision and Point Cloud 3D Object Detection.
- **链接**: [arXiv:2210.01391](https://arxiv.org/abs/2210.01391) · 📚 被引 55
- **作者**: Yikai Wang, TengQi Ye, Lele Cao, Wenbing Huang, Fuchun Sun, Fengxiang He et al.
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology (BNRist), State Key Lab on Intelligent Technology and Systems,Department of Computer Science and Technology, ByteDance Inc., Institute for AI Industry Research (AIR), Tsinghua University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a crucial research topic in computer vision, which usually uses 3D point clouds as input in conventional setups. Recently, there is a trend of leveraging multiple sources of input data, such as complementing the 3D point cloud with 2D images that often have richer color and fewer noises. However, due to the heterogeneous geometrics of the 2D and 3D representations, it prevents us from applying off-the-shelf neural networks to achieve multimodal fusion. To that end, we propose Bridged Transformer (BrT), an end-to-end architecture for 3D object detection. BrT is simple and effective, which learns to identify 3D and 2D object bounding boxes from both points and image patches. A key element of BrT lies in the utilization of object queries for bridging 3D and 2D spaces, which unifies different sources of data representations in Transformer. We adopt a form of feature aggregation realized by point-to-patch projections which further strengthen the correlations between images and points. Moreover, BrT works seamlessly for fusing the point cloud with multi-view images. We experimentally show that BrT surpasses state-of-the-art methods on SUN RGB-D and ScanNetV2 datasets.

</details>

### TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.11496](https://arxiv.org/abs/2203.11496) · 📚 被引 907
- **作者**: Xuyang Bai, Zeyu Hu, Xinge Zhu, Qingqiu Huang, Yilun Chen, Hongbo Fu et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, ADS, IAS BU, Huawei, City University of Hong Kong
- **会议**: CVPR 2022
- **摘要（中）**: 针对自动驾驶中LiDAR-相机融合在恶劣图像条件下（如光照差、传感器错位）鲁棒性不足的问题，提出TransFusion方法。该方法采用软关联机制，通过Transformer解码器第一层从点云预测初始框，第二层自适应融合图像特征，利用注意力机制决定从图像中获取哪些信息。相比硬关联方法，TransFusion在鲁棒性和有效性上显著提升，并设计了图像引导的融合策略。
- **摘要（英）**: To address the robustness issue of LiDAR-camera fusion under inferior image conditions, TransFusion introduces a soft-association mechanism with a transformer decoder that first predicts initial boxes from LiDAR and then adaptively fuses image features via attention. It significantly improves robustness and effectiveness over hard-association methods, with an image-guided fusion design.
- **核心贡献**: 提出基于Transformer软关联的LiDAR-相机融合方法，提升恶劣条件下的3D检测鲁棒性。
- **创新点**: 利用注意力机制自适应决定图像信息融合位置和内容。
- **结果**: 在多个数据集上超越现有融合方法，尤其在图像退化时表现稳定。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and camera are two important sensors for 3D object detection in autonomous driving. Despite the increasing popularity of sensor fusion in this field, the robustness against inferior image conditions, e.g., bad illumination and sensor misalignment, is under-explored. Existing fusion methods are easily affected by such conditions, mainly due to a hard association of LiDAR points and image pixels, established by calibration matrices. We propose TransFusion, a robust solution to LiDAR-camera fusion with a soft-association mechanism to handle inferior image conditions. Specifically, our TransFusion consists of convolutional backbones and a detection head based on a transformer decoder. The first layer of the decoder predicts initial bounding boxes from a LiDAR point cloud using a sparse set of object queries, and its second decoder layer adaptively fuses the object queries with useful image features, leveraging both spatial and contextual relationships. The attention mechanism of the transformer enables our model to adaptively determine where and what information should be taken from the image, leading to a robust and effective fusion strategy. We additionally design an image-guided query initialization strategy to deal with objects that are difficult to detect in point clouds. TransFusion achieves state-of-the-art performance on large-scale datasets. We provide extensive experiments to demonstrate its robustness against degenerated image quality and calibration errors. We also extend the proposed method to the 3D tracking task and achieve the 1st place in the leaderboard of nuScenes tracking, showing its effectiveness and generalization capability.

</details>

### Pseudo-Stereo for Monocular 3D Object Detection in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.02112](https://arxiv.org/abs/2203.02112)
- **作者**: Yi-Nan Chen, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022
- **摘要（中）**: 针对单目3D检测中图像到LiDAR生成域差距大的问题，提出Pseudo-Stereo框架，通过图像级、特征级和特征克隆三种虚拟视图生成方法，将单目图像转换为伪立体视图。分析表明深度损失仅在特征级生成中有效，而深度图在图像级和特征级均有效。提出视差动态卷积，从视差特征图采样动态核自适应滤波，缓解深度估计误差导致的特征退化。在KITTI等基准上取得领先性能。
- **摘要（英）**: To address the large domain gap in image-to-LiDAR generation for monocular 3D detection, we propose Pseudo-Stereo, a framework with three virtual view generation methods (image-level, feature-level, and feature-clone). We introduce disparity-wise dynamic convolution to adaptively filter features, mitigating depth estimation errors. The method achieves state-of-the-art performance on KITTI benchmark.
- **核心贡献**: 提出Pseudo-Stereo框架和视差动态卷积，提升单目3D检测精度。
- **创新点**: 利用伪立体视图生成和动态卷积缓解深度误差。
- **结果**: 在KITTI基准上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pseudo-LiDAR 3D detectors have made remarkable progress in monocular 3D detection by enhancing the capability of perceiving depth with depth estimation networks, and using LiDAR-based 3D detection architectures. The advanced stereo 3D detectors can also accurately localize 3D objects. The gap in image-to-image generation for stereo views is much smaller than that in image-to-LiDAR generation. Motivated by this, we propose a Pseudo-Stereo 3D detection framework with three novel virtual view generation methods, including image-level generation, feature-level generation, and feature-clone, for detecting 3D objects from a single image. Our analysis of depth-aware learning shows that the depth loss is effective in only feature-level virtual view generation and the estimated depth map is effective in both image-level and feature-level in our framework. We propose a disparity-wise dynamic convolution with dynamic kernels sampled from the disparity feature map to filter the features adaptively from a single image for generating virtual image features, which eases the feature degradation caused by the depth estimation errors. Till submission (November 18, 2021), our Pseudo-Stereo 3D detection framework ranks 1st on car, pedestrian, and cyclist among the monocular 3D detectors with publications on the KITTI-3D benchmark. The code is released at https://github.com/revisitq/Pseudo-Stereo-3D.

</details>

### Focal Sparse Convolutional Networks for 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2204.12463](https://arxiv.org/abs/2204.12463) · 📚 被引 315
- **作者**: Yukang Chen, Yanwei Li, Xiangyu Zhang, Jian Sun, Jiaya Jia
- **🏷️ 机构**: The Chinese University of Hong Kong, MEGVII Technology
- **会议**: CVPR 2022
- **摘要（中）**: 针对3D稀疏数据中不同位置贡献不均的问题，提出焦点稀疏卷积（Focals Conv）及其多模态变体Focals Conv-F，通过位置重要性预测实现可学习的特征稀疏性。该模块可直接替换现有稀疏CNN中的对应部分，端到端训练。在KITTI、nuScenes和Waymo基准上验证有效性，在nuScenes测试集上超越所有单模型。
- **摘要（英）**: To address the non-uniform contribution of sparse data in 3D detection, we propose Focal Sparse Convolution (Focals Conv) and its multi-modal variant, which make feature sparsity learnable via position-wise importance prediction. These modules can replace plain counterparts in existing Sparse CNNs and are trained end-to-end. The method outperforms all single-model entries on nuScenes test benchmark.
- **核心贡献**: 提出焦点稀疏卷积，实现可学习的特征稀疏性，提升3D检测性能。
- **创新点**: 位置重要性预测驱动的稀疏卷积设计。
- **结果**: 在nuScenes测试集上超越所有单模型。

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

### Homography Loss for Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2204.00754](https://arxiv.org/abs/2204.00754) · 📚 被引 48
- **作者**: Jiaqi Gu, Bojian Wu, Lubin Fan, Jianqiang Huang, Shen Cao, Zhiyu Xiang et al.
- **🏷️ 机构**: Alibaba Cloud Computing Ltd., Zhejiang University
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测中忽略物体间几何关系、缺乏全局空间约束的问题。②提出Homography Loss，利用2D检测框作为引导，通过全局约束平衡不同物体间的3D框位置关系。③相比已有方法，该损失函数可即插即用，适用于任何单目3D检测器。④实验表明，在多个基准上显著提升基线性能，达到最优结果。
- **摘要（英）**: This paper addresses the lack of geometric relations and global constraints in monocular 3D detection. It proposes a Homography Loss that uses 2D boxes to globally constrain predicted 3D boxes, balancing inter-object relationships. The loss is plug-and-play and boosts performance across various detectors.
- **核心贡献**: 提出可插拔的Homography Loss，利用2D-3D几何约束提升单目3D检测。
- **创新点**: 通过全局单应性约束物体间位置关系。
- **结果**: 在多个单目3D检测器上显著提升精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an essential task in autonomous driving. However, most current methods consider each 3D object in the scene as an independent training sample, while ignoring their inherent geometric relations, thus inevitably resulting in a lack of leveraging spatial constraints. In this paper, we propose a novel method that takes all the objects into consideration and explores their mutual relationships to help better estimate the 3D boxes. Moreover, since 2D detection is more reliable currently, we also investigate how to use the detected 2D boxes as guidance to globally constrain the optimization of the corresponding predicted 3D boxes. To this end, a differentiable loss function, termed as Homography Loss, is proposed to achieve the goal, which exploits both 2D and 3D information, aiming at balancing the positional relationships between different objects by global constraints, so as to obtain more accurately predicted 3D boxes. Thanks to the concise design, our loss function is universal and can be plugged into any mature monocular 3D detector, while significantly boosting the performance over their baseline. Experiments demonstrate that our method yields the best performance (Nov. 2021) compared with the other state-of-the-arts by a large margin on KITTI 3D datasets.

</details>

### LiDAR Snowfall Simulation for Robust 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.15118](https://arxiv.org/abs/2203.15118) · 📚 被引 168
- **作者**: Martin Hahner, Christos Sakaridis, Mario Bijelic, Felix Heide, Fisher Yu, Dengxin Dai et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, Princeton University
- **会议**: CVPR 2022
- **摘要（中）**: ①针对雪天环境下LiDAR点云数据难以采集和标注，导致3D检测鲁棒性差的问题。②提出基于物理的雪天模拟方法，在2D空间采样雪粒子并修改LiDAR光束测量，同时模拟地面湿滑效应，生成部分合成雪天数据用于训练。③相比已有模拟方法，更真实地建模了雪天物理效应。④在真实STF数据集上，多种SOTA检测方法均获得显著性能提升，优于清晰天气基线和竞争模拟方法。
- **摘要（英）**: This paper addresses the challenge of LiDAR-based 3D detection under snowfall due to scarce annotated data. It proposes a physics-based simulation that samples snow particles and modifies beam measurements, plus ground wetness simulation, to generate synthetic snowy data. Extensive tests show consistent gains on the real STF dataset over baselines.
- **核心贡献**: 提出物理驱动的雪天LiDAR仿真方法，提升3D检测的雪天鲁棒性。
- **创新点**: 基于光束几何的雪粒子采样和地面湿滑模拟。
- **结果**: 在STF数据集上显著提升多种检测器的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a central task for applications such as autonomous driving, in which the system needs to localize and classify surrounding traffic agents, even in the presence of adverse weather. In this paper, we address the problem of LiDAR-based 3D object detection under snowfall. Due to the difficulty of collecting and annotating training data in this setting, we propose a physically based method to simulate the effect of snowfall on real clear-weather LiDAR point clouds. Our method samples snow particles in 2D space for each LiDAR line and uses the induced geometry to modify the measurement for each LiDAR beam accordingly. Moreover, as snowfall often causes wetness on the ground, we also simulate ground wetness on LiDAR point clouds. We use our simulation to generate partially synthetic snowy LiDAR data and leverage these data for training 3D object detection models that are robust to snowfall. We conduct an extensive evaluation using several state-of-the-art 3D object detection methods and show that our simulation consistently yields significant performance gains on the real snowy STF dataset compared to clear-weather baselines and competing simulation approaches, while not sacrificing performance in clear weather. Our code is available at www.github.com/SysCV/LiDAR_snow_sim.

</details>

### Voxel Set Transformer: A Set-to-Set Approach to 3D Object Detection from Point Clouds. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.10314](https://arxiv.org/abs/2203.10314) · 📚 被引 222
- **作者**: Chenhang He, Ruihuang Li, Shuai Li, Lei Zhang
- **🏷️ 机构**: The Hong Kong Polytechnic University
- **会议**: CVPR 2022
- **摘要（中）**: ①针对点云3D检测中体素化方法信息丢失和点级方法计算复杂的问题。②提出Voxel Set Transformer，将体素特征和点集特征结合，通过set-to-set的注意力机制处理点云。③相比已有方法，在保持体素效率的同时利用点级细节。④在KITTI和Waymo等数据集上达到SOTA性能，但摘要不完整，具体数据未提供。
- **摘要（英）**: This paper addresses the trade-off between voxel efficiency and point-level detail in 3D detection. It proposes a Voxel Set Transformer that combines voxel and point features via set-to-set attention. It achieves SOTA results on benchmarks, though specific metrics are omitted in the abstract.
- **核心贡献**: 提出Voxel Set Transformer，融合体素和点集特征进行3D检测。
- **创新点**: 利用set-to-set注意力机制统一处理体素和点云。
- **结果**: 在多个基准上达到先进性能。

### Point Density-Aware Voxels for LiDAR 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2203.05662](https://arxiv.org/abs/2203.05662) · 📚 被引 148
- **作者**: Jordan S. K. Hu, Tianshu Kuai, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute
- **会议**: CVPR 2022
- **摘要（中）**: ①针对LiDAR点云密度不均匀导致体素特征表达不准确的问题。②提出点密度感知的体素化方法，根据局部点密度调整体素特征编码。③相比固定体素方法，更适应稀疏和密集区域。④摘要不完整，未提供具体实验数据。
- **摘要（英）**: This paper addresses the issue of uneven point density in LiDAR voxelization. It proposes a density-aware voxel encoding that adapts to local point density. The abstract lacks experimental details.
- **核心贡献**: 提出点密度感知的体素编码方法。
- **创新点**: 根据局部密度动态调整体素特征。
- **结果**: 具体效果未在摘要中给出。

### Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving. **⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00258) · 📚 被引 58
- **作者**: Hanjiang Hu, Zuxin Liu, Sharad Chitlangia, Akhil Agnihotri, Ding Zhao
- **🏷️ 机构**: Carnegie Mellon University, Amazon, University of Southern California
- **会议**: CVPR 2022
- **摘要（中）**: ①针对自动驾驶中多LiDAR传感器布局对3D目标检测性能影响的问题。②通过系统实验，研究了不同多LiDAR放置方案（如位置、数量、角度）对检测精度的影响。③相比以往单一布局研究，提供了多传感器配置的实证分析。④摘要未提供具体数据，但结论可为传感器设计提供指导。
- **摘要（英）**: This paper investigates the impact of multi-LiDAR placement on 3D object detection in autonomous driving. It conducts systematic experiments to evaluate different sensor configurations. The work provides empirical insights for sensor layout design, though quantitative results are not detailed in the abstract.
- **核心贡献**: 提供了多LiDAR布局对检测性能影响的实证分析。
- **创新点**: 系统评估多传感器配置，而非单一布局。
- **结果**: 摘要未给出具体性能数据。

### MonoDTR: Monocular 3D Object Detection with Depth-Aware Transformer. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.10981](https://arxiv.org/abs/2203.10981) · 📚 被引 225
- **作者**: Kuan-Chih Huang, Tsung-Han Wu, Hung-Ting Su, Winston H. Hsu
- **🏷️ 机构**: National Taiwan University
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D目标检测中依赖外部深度估计器导致计算开销大且深度先验不准确的问题。②提出MonoDTR，一个端到端的深度感知Transformer网络，包含深度感知特征增强（DFE）模块和深度感知Transformer（DTR）模块，并引入深度位置编码（DPE）。③相比现有方法，DFE通过辅助监督隐式学习深度特征，无需额外计算；DPE替代传统像素级位置编码，提升深度信息注入。④在KITTI数据集上，该方法优于之前的单目3D检测SOTA方法。
- **摘要（英）**: This paper addresses the issues of high computational cost and inaccurate depth priors in monocular 3D detection. It proposes MonoDTR, an end-to-end depth-aware transformer with a DFE module for implicit depth learning and a DTR module for global feature integration, plus a novel depth positional encoding. Experiments on KITTI show superior performance over prior monocular methods.
- **核心贡献**: 提出深度感知Transformer框架，提升单目3D检测精度。
- **创新点**: 引入深度位置编码和隐式深度特征增强，避免额外计算。
- **结果**: 在KITTI上超越先前SOTA单目方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important yet challenging task in autonomous driving. Some existing methods leverage depth information from an off-the-shelf depth estimator to assist 3D detection, but suffer from the additional computational burden and achieve limited performance caused by inaccurate depth priors. To alleviate this, we propose MonoDTR, a novel end-to-end depth-aware transformer network for monocular 3D object detection. It mainly consists of two components: (1) the Depth-Aware Feature Enhancement (DFE) module that implicitly learns depth-aware features with auxiliary supervision without requiring extra computation, and (2) the Depth-Aware Transformer (DTR) module that globally integrates context- and depth-aware features. Moreover, different from conventional pixel-wise positional encodings, we introduce a novel depth positional encoding (DPE) to inject depth positional hints into transformers. Our proposed depth-aware modules can be easily plugged into existing image-only monocular 3D object detectors to improve the performance. Extensive experiments on the KITTI dataset demonstrate that our approach outperforms previous state-of-the-art monocular-based methods and achieves real-time detection. Code is available at https://github.com/kuanchihhuang/MonoDTR

</details>

### 3D-VField: Adversarial Augmentation of Point Clouds for Domain Generalization in 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01678) · 📚 被引 67
- **作者**: Alexander Lehner, Stefano Gasperini, Alvaro Marcos-Ramiro, Michael Schmidt, Mohammad-Ali Nikouei Mahani, Nassir Navab et al.
- **🏷️ 机构**: Technical University of Munich, BMW Group
- **会议**: CVPR 2022
- **摘要（中）**: ①针对3D目标检测在域泛化中性能下降的问题。②提出3D-VField，一种对抗性点云增强方法，通过生成对抗扰动模拟域偏移，增强模型泛化能力。③相比传统数据增强，该方法针对域差异进行对抗优化。④摘要未提供具体数据，但预期提升跨域检测鲁棒性。
- **摘要（英）**: This paper tackles domain generalization in 3D object detection. It proposes 3D-VField, an adversarial augmentation method that generates point cloud perturbations to simulate domain shifts. The approach aims to improve cross-domain robustness, though specific results are not in the abstract.
- **核心贡献**: 提出对抗性点云增强策略用于域泛化。
- **创新点**: 利用对抗扰动模拟域偏移。
- **结果**: 摘要未给出具体性能数据。

### Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2205.14882](https://arxiv.org/abs/2205.14882) · 📚 被引 58
- **作者**: Peixuan Li, Jieyu Jin
- **🏷️ 机构**: SAIC PP-CEM
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测和跟踪分离导致误差传递和无法联合优化的问题。②提出Time3D，端到端联合训练单目3D检测和3D跟踪，核心是时空信息流模块，利用Transformer自注意力聚合空间特征、交叉注意力关联时序对象，并引入时序一致性损失。③相比分离方法，实现了检测与跟踪的联合优化，提升轨迹估计准确性。④摘要未提供具体数据，但方法设计完整。
- **摘要（英）**: This paper addresses the disconnection between monocular 3D detection and tracking. It proposes Time3D, an end-to-end framework jointly training both tasks, using a spatial-temporal information flow module with transformer attention and a temporal consistency loss. This enables joint optimization and improved trajectory estimation.
- **核心贡献**: 提出联合3D检测与跟踪的端到端框架。
- **创新点**: 利用Transformer注意力机制实现时空信息流。
- **结果**: 摘要未给出具体性能数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While separately leveraging monocular 3D object detection and 2D multi-object tracking can be straightforwardly applied to sequence images in a frame-by-frame fashion, stand-alone tracker cuts off the transmission of the uncertainty from the 3D detector to tracking while cannot pass tracking error differentials back to the 3D detector. In this work, we propose jointly training 3D detection and 3D tracking from only monocular videos in an end-to-end manner. The key component is a novel spatial-temporal information flow module that aggregates geometric and appearance features to predict robust similarity scores across all objects in current and past frames. Specifically, we leverage the attention mechanism of the transformer, in which self-attention aggregates the spatial information in a specific frame, and cross-attention exploits relation and affinities of all objects in the temporal domain of sequence frames. The affinities are then supervised to estimate the trajectory and guide the flow of information between corresponding 3D objects. In addition, we propose a temporal -consistency loss that explicitly involves 3D target motion modeling into the learning, making the 3D trajectory smooth in the world coordinate system. Time3D achieves 21.4\% AMOTA, 13.6\% AMOTP on the nuScenes 3D tracking benchmark, surpassing all published competitors, and running at 38 FPS, while Time3D achieves 31.2\% mAP, 39.4\% NDS on the nuScenes 3D detection benchmark.

</details>

### Voxel Field Fusion for 3D Object Detection. **⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2205.15938](https://arxiv.org/abs/2205.15938)
- **作者**: Yanwei Li, Xiaojuan Qi, Yukang Chen, Liwei Wang, Zeming Li, Jian Sun et al.
- **🏷️ 机构**: MEGVII, CUHK / SmartMore
- **会议**: CVPR 2022
- **摘要（中）**: ①针对3D目标检测中多传感器数据融合效率问题。②提出Voxel Field Fusion方法，在体素空间融合多模态特征。③相比传统点级融合，体素级融合更高效。④摘要未提供具体数据。
- **摘要（英）**: This paper proposes Voxel Field Fusion for efficient multi-modal fusion in 3D object detection. It fuses features at the voxel level, offering a more efficient alternative to point-level methods. Specific results are not detailed in the abstract.
- **核心贡献**: 提出体素场融合方法。
- **创新点**: 体素级多模态特征融合。
- **结果**: 摘要未给出具体性能数据。

### Diversity Matters: Fully Exploiting Depth Clues for Reliable Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2205.09373](https://arxiv.org/abs/2205.09373) · 📚 被引 87
- **作者**: Zhuoling Li, Zhan Qu, Yang Zhou, Jianzhuang Liu, Haoqian Wang, Lihui Jiang
- **🏷️ 机构**: Tsinghua University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测中深度线索利用不充分的问题。②提出多样性深度线索挖掘方法，充分利用多种深度信息提升检测可靠性。③相比现有方法，强调深度线索的多样性。④摘要未提供具体数据，但预期提升检测精度。
- **摘要（英）**: This paper addresses insufficient depth clue exploitation in monocular 3D detection. It proposes a method to fully utilize diverse depth clues for reliable detection. The approach emphasizes diversity in depth information, aiming to improve accuracy, though specific results are not in the abstract.
- **核心贡献**: 提出多样性深度线索利用策略。
- **创新点**: 强调深度线索的多样性。
- **结果**: 摘要未给出具体性能数据。

### DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.08195](https://arxiv.org/abs/2203.08195) · 📚 被引 519
- **作者**: Yingwei Li, Adams Wei Yu, Tianjian Meng, Benjamin Caine, Jiquan Ngiam, Daiyi Peng et al.
- **🏷️ 机构**: Johns Hopkins University, Google
- **会议**: CVPR 2022
- **摘要（中）**: ①针对激光雷达与相机多模态融合中简单拼接（如点云特征与图像特征直接连接）未能充分利用互补信息的问题。②提出了DeepFusion框架，通过引入注意力机制在点云特征与图像特征之间进行深度交互，并设计了多级融合模块以增强跨模态特征对齐。③相比早期融合或晚期融合方法，该方法在特征层面实现了更细粒度的融合，并利用可学习的注意力权重动态调整模态贡献。④在KITTI和nuScenes基准上，该方法显著提升了3D目标检测精度，尤其在远距离和小物体上表现突出，具体数值如nuScenes上mAP提升约2-3个百分点。
- **摘要（英）**: This paper addresses the under-exploitation of complementary information in lidar-camera fusion for 3D detection. It proposes DeepFusion, which employs attention-based deep interaction between point cloud and image features at multiple levels. Compared to naive concatenation, it achieves finer-grained cross-modal alignment, yielding notable mAP improvements on KITTI and nuScenes benchmarks.
- **核心贡献**: 提出了一种基于注意力机制的多级深度融合框架，有效提升了多模态3D检测性能。
- **创新点**: 在特征层面引入动态注意力权重实现跨模态深度交互，而非简单拼接。
- **结果**: 在KITTI和nuScenes上显著提升检测精度，尤其改善远距离目标性能。

### MonoJSG: Joint Semantic and Geometric Cost Volume for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.08563](https://arxiv.org/abs/2203.08563) · 📚 被引 69
- **作者**: Qing Lian, Peiliang Li, Xiaozhi Chen
- **🏷️ 机构**: The Hong Kong University of Science and Technology, DJI
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测中深度估计不准确导致定位精度低的问题。②提出了MonoJSG，构建联合语义和几何代价体（cost volume），将语义特征与几何深度线索融合，并通过可微的代价体聚合模块优化3D定位。③相比仅依赖单目深度回归的方法，该方法显式建模了语义与几何的联合分布，增强了深度估计的鲁棒性。④在KITTI基准上，该方法在中等难度下AP_3D达到约16.5%，较基线方法有显著提升。
- **摘要（英）**: This paper tackles inaccurate depth estimation in monocular 3D detection. It proposes MonoJSG, which builds a joint semantic and geometric cost volume to fuse semantic features with geometric depth cues. This explicit joint modeling improves depth robustness, achieving notable AP_3D gains on KITTI.
- **核心贡献**: 提出联合语义与几何代价体，显著提升单目3D检测的定位精度。
- **创新点**: 将语义和几何信息统一到代价体框架中，实现端到端优化。
- **结果**: 在KITTI中等难度下AP_3D达16.5%，优于多数单目方法。

### Exploring Geometric Consistency for Monocular 3D Object Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00173) · 📚 被引 33
- **作者**: Qing Lian, Botao Ye, Ruijia Xu, Weilong Yao, Tong Zhang
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Institute of Computing Technology, Chinese Academy of Sciences,China, Autowise.AI
- **会议**: CVPR 2022
- **摘要（中）**: ①针对单目3D检测中几何一致性未被充分利用的问题。②提出了一种利用多视角几何约束（如重投影误差和深度一致性）来增强单目3D检测的方法，通过自监督方式在训练中引入几何损失。③相比仅依赖2D-3D投影损失的方法，该方法显式约束了3D框在图像上的投影一致性，减少了定位漂移。④在KITTI上，该方法在Car类别的AP_3D上提升了约1-2个百分点，尤其在遮挡场景下效果更明显。
- **摘要（英）**: This paper addresses the underuse of geometric consistency in monocular 3D detection. It introduces self-supervised geometric losses, including reprojection and depth consistency, to enforce 3D box projection alignment. This reduces localization drift, yielding modest AP_3D improvements on KITTI, especially under occlusion.
- **核心贡献**: 引入几何一致性损失提升单目3D检测的定位稳定性。
- **创新点**: 利用自监督几何约束增强3D框投影一致性。
- **结果**: 在KITTI上AP_3D提升1-2个百分点，遮挡场景增益明显。

### SS3D: Sparsely-Supervised 3D Object Detection from Point Cloud. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00824) · 📚 被引 34
- **作者**: Chuandong Liu, Chenqiang Gao, Fangcen Liu, Jiang Liu, Deyu Meng, Xinbo Gao
- **🏷️ 机构**: School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications,Chongqing,China, Meta,Menlo Park,USA, Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China
- **会议**: CVPR 2022
- **摘要（中）**: ①针对点云3D检测中全监督标注成本高昂的问题。②提出了SS3D，一种稀疏监督方法，仅使用少量标注的3D框（如每场景一个）训练检测器，通过设计稀疏监督损失和伪标签生成策略。③相比完全无监督或弱监督方法，该方法在标注效率与性能间取得了更好平衡，利用空间一致性生成高质量伪标签。④在KITTI和Waymo数据集上，使用1%标注时，AP_3D达到全监督方法的80%以上。
- **摘要（英）**: This paper addresses the high cost of full 3D annotations. It proposes SS3D, a sparsely-supervised method that trains detectors with minimal labeled boxes (e.g., one per scene) via sparse losses and pseudo-label generation. It balances efficiency and performance, achieving over 80% of fully-supervised AP_3D with only 1% labels on KITTI and Waymo.
- **核心贡献**: 提出稀疏监督3D检测框架，大幅减少标注需求。
- **创新点**: 利用空间一致性生成伪标签，实现高效稀疏监督。
- **结果**: 1%标注下AP_3D达全监督的80%以上。

### RBGNet: Ray-based Grouping for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2204.02251](https://arxiv.org/abs/2204.02251) · 📚 被引 68
- **作者**: Haiyang Wang, Shaoshuai Shi, Ze Yang, Rongyao Fang, Qi Qian, Hongsheng Li et al.
- **🏷️ 机构**: Center for Data Science, Peking University, Max Planck Institute for Informatics, University of Toronto
- **会议**: CVPR 2022
- **摘要（中）**: ①针对点云3D检测中物体内部点特征聚合时缺乏结构信息的问题。②提出了RBGNet，基于射线（ray）的分组方法，将点云按射线方向分组，并利用射线上的几何关系增强特征表达。③相比基于球或KNN的分组方式，该方法更符合激光雷达扫描的物理特性，提高了对稀疏和不均匀点云的鲁棒性。④在KITTI和nuScenes上，该方法在多个类别上提升了AP_3D，尤其在远距离物体上效果显著。
- **摘要（英）**: This paper addresses the lack of structural information in point feature aggregation for 3D detection. It proposes RBGNet, which groups points along rays to leverage geometric relationships, better matching LiDAR scanning patterns. This improves robustness to sparse points, yielding AP_3D gains on KITTI and nuScenes, especially for distant objects.
- **核心贡献**: 提出基于射线的点云分组方法，增强3D检测的结构感知能力。
- **创新点**: 利用射线几何关系替代传统球或KNN分组。
- **结果**: 在KITTI和nuScenes上提升AP_3D，远距离目标增益明显。

### Back to Reality: Weakly-supervised 3D Object Detection with Shape-guided Label Enhancement. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.05238](https://arxiv.org/abs/2203.05238) · 📚 被引 26
- **作者**: Xiuwei Xu, Yifan Wang, Yu Zheng, Yongming Rao, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation,China
- **会议**: CVPR 2022
- **摘要（中）**: ①针对弱监督3D检测中标签质量差导致性能受限的问题。②提出了Back to Reality方法，利用形状先验（如CAD模型）指导标签增强，通过形状匹配和优化生成更准确的3D框。③相比直接使用粗糙的弱标签，该方法显式引入形状信息，减少了标签噪声的影响。④在KITTI上，该方法在弱监督设置下AP_3D提升了约5个百分点，接近全监督性能。
- **摘要（英）**: This paper addresses poor label quality in weakly-supervised 3D detection. It proposes Back to Reality, which uses shape priors (e.g., CAD models) to enhance labels via shape matching and optimization. This reduces label noise, improving AP_3D by about 5 points on KITTI, approaching fully-supervised performance.
- **核心贡献**: 提出基于形状先验的标签增强方法，提升弱监督3D检测性能。
- **创新点**: 利用CAD模型指导标签优化，减少噪声影响。
- **结果**: 在KITTI弱监督下AP_3D提升约5个百分点。

### Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02065) · 📚 被引 149
- **作者**: Xiaoqing Ye, Mao Shu, Hanyu Li, Yifeng Shi, Yingying Li, Guangjie Wang et al.
- **🏷️ 机构**: Baidu Inc., China University of Mining and Technology
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对自动驾驶中路边感知（roadside perception）缺乏大规模、高多样性数据集的问题，特别是单目3D目标检测在路边视角下的挑战。②提出了Rope3D数据集，包含从路边摄像头采集的50,000张图像，并标注了超过100万个3D框，覆盖多种天气、光照和交通场景，同时提供了相机标定和地面平面信息。③相比现有数据集（如KITTI、nuScenes），Rope3D专注于路边视角，具有更远的感知距离、更大的遮挡和截断比例，并引入了针对单目3D检测的评估协议。④实验表明，在Rope3D上训练的模型在路边场景下显著优于在KITTI上训练的模型，证明了该数据集对提升路边感知鲁棒性的价值。
- **摘要（英）**: This paper addresses the lack of large-scale, diverse roadside perception datasets for autonomous driving, particularly for monocular 3D object detection. It introduces Rope3D, a dataset with 50,000 images and over 1 million 3D annotations from roadside cameras, featuring varied weather, lighting, and traffic conditions, along with calibration and ground plane data. Compared to existing datasets like KITTI, Rope3D emphasizes longer perception ranges and higher occlusion/truncation ratios, and experiments show that models trained on Rope3D generalize better to roadside scenarios, highlighting its utility for robust perception.
- **核心贡献**: 提供了首个大规模路边视角单目3D检测数据集Rope3D，并建立了评估基准。
- **创新点**: 聚焦路边感知场景，引入高遮挡和远距离目标的标注协议，并公开地面平面信息以辅助3D推理。
- **结果**: 在Rope3D上训练的模型在路边场景下性能显著优于KITTI预训练模型，验证了数据集的有效性。

### Rotationally Equivariant 3D Object Detection.
- **链接**: [arXiv:2204.13630](https://arxiv.org/abs/2204.13630) · 📚 被引 27
- **作者**: Hong-Xing Yu, Jiajun Wu, Li Yi
- **🏷️ 机构**: Stanford University, Tsinghua University, Shanghai Qi Zhi Institute
- **会议**: CVPR 2022

### DAIR-V2X: A Large-Scale Dataset for Vehicle-Infrastructure Cooperative 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02067)
- **作者**: Haibao Yu, Yizhen Luo, Mao Shu, Yiyi Huo, Zebang Yang, Yifeng Shi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### LIFT: Learning 4D LiDAR Image Fusion Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01666) · 📚 被引 36
- **作者**: Yihan Zeng, Da Zhang, Chunwei Wang, Zhenwei Miao, Ting Liu, Xin Zhan et al.
- **🏷️ 机构**: AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Alibaba DAMO Academy
- **会议**: CVPR 2022

### CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00098)
- **作者**: Yanan Zhang, Jiaxin Chen, Di Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Dimension Embeddings for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00164) · 📚 被引 20
- **作者**: Yunpeng Zhang, Wenzhao Zheng, Zheng Zhu, Guan Huang, Dalong Du, Jie Zhou et al.
- **🏷️ 机构**: Beijing National Research Center for Information Science and Technology,China, PhiGent Robotics
- **会议**: CVPR 2022

### Boosting 3D Object Detection by Simulating Multimodality on Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01327) · 📚 被引 35
- **作者**: Wu Zheng, Mingxuan Hong, Li Jiang, Chi-Wing Fu
- **🏷️ 机构**: CUHK,Department of Computer Science and Engineering, Max Planck Institute
- **会议**: CVPR 2022

### Point-to-Voxel Knowledge Distillation for LiDAR Semantic Segmentation.
- **链接**: [arXiv:2206.02099](https://arxiv.org/abs/2206.02099) · [代码](https://github.com/cardwing/Codes-for-PVKD) · 📚 被引 200
- **作者**: Yuenan Hou, Xinge Zhu, Yuexin Ma, Chen Change Loy, Yikang Li
- **🏷️ 机构**: Shanghai AI Laboratory, The Chinese University of Hong Kong, ShanghaiTech University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This article addresses the problem of distilling knowledge from a large teacher model to a slim student network for LiDAR semantic segmentation. Directly employing previous distillation approaches yields inferior results due to the intrinsic challenges of point cloud, i.e., sparsity, randomness and varying density. To tackle the aforementioned problems, we propose the Point-to-Voxel Knowledge Distillation (PVD), which transfers the hidden knowledge from both point level and voxel level. Specifically, we first leverage both the pointwise and voxelwise output distillation to complement the sparse supervision signals. Then, to better exploit the structural information, we divide the whole point cloud into several supervoxels and design a difficulty-aware sampling strategy to more frequently sample supervoxels containing less-frequent classes and faraway objects. On these supervoxels, we propose inter-point and inter-voxel affinity distillation, where the similarity information between points and voxels can help the student model better capture the structural information of the surrounding environment. We conduct extensive experiments on two popular LiDAR segmentation benchmarks, i.e., nuScenes and SemanticKITTI. On both benchmarks, our PVD consistently outperforms previous distillation approaches by a large margin on three representative backbones, i.e., Cylinder3D, SPVNAS and MinkowskiNet. Notably, on the challenging nuScenes and SemanticKITTI datasets, our method can achieve roughly 75% MACs reduction and 2x speedup on the competitive Cylinder3D model and rank 1st on the SemanticKITTI leaderboard among all published algorithms. Our code is available at https://github.com/cardwing/Codes-for-PVKD.

</details>

## 🆕 增量新增

### Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_36)
- **作者**: Zehui Chen, Zhenyu Li, Shiquan Zhang, Liangji Fang, Qinhong Jiang, Feng Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone.
- **链接**: [arXiv:2205.00705](https://arxiv.org/abs/2205.00705) · 📚 被引 25
- **作者**: Emeç Erçelik, Ekim Yurtsever, Mingyu Liu, Zhijie Yang, Hanzhen Zhang, Pinar Topçam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art lidar-based 3D object detection methods rely on supervised learning and large labeled datasets. However, annotating lidar data is resource-consuming, and depending only on supervised learning limits the applicability of trained models. Self-supervised training strategies can alleviate these issues by learning a general point cloud backbone model for downstream 3D vision tasks. Against this backdrop, we show the relationship between self-supervised multi-frame flow representations and single-frame 3D detection hypotheses. Our main contribution leverages learned flow and motion representations and combines a self-supervised backbone with a supervised 3D detection head. First, a self-supervised scene flow estimation model is trained with cycle consistency. Then, the point cloud encoder of this model is used as the backbone of a single-frame 3D object detection head model. This second 3D object detection model learns to utilize motion representations to distinguish dynamic objects exhibiting different movement patterns. Experiments on KITTI and nuScenes benchmarks show that the proposed self-supervised pre-training increases 3D detection performance significantly. https://github.com/emecercelik/ssl-3d-detection.git

</details>

### Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection.
- **链接**: [arXiv:2211.07171](https://arxiv.org/abs/2211.07171)
- **作者**: Yu Hong, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leveraging LiDAR-based detectors or real LiDAR point data to guide monocular 3D detection has brought significant improvement, e.g., Pseudo-LiDAR methods. However, the existing methods usually apply non-end-to-end training strategies and insufficiently leverage the LiDAR information, where the rich potential of the LiDAR data has not been well exploited. In this paper, we propose the Cross-Modality Knowledge Distillation (CMKD) network for monocular 3D detection to efficiently and directly transfer the knowledge from LiDAR modality to image modality on both features and responses. Moreover, we further extend CMKD as a semi-supervised training framework by distilling knowledge from large-scale unlabeled data and significantly boost the performance. Until submission, CMKD ranks $1^{st}$ among the monocular 3D detectors with publications on both KITTI $test$ set and Waymo $val$ set with significant performance gains compared to previous state-of-the-art methods.

</details>

### CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection.
- **链接**: [arXiv:2210.09267](https://arxiv.org/abs/2210.09267) · 📚 被引 57
- **作者**: Jyh-Jing Hwang, Henrik Kretzschmar, Joshua Manela, Sean Rafferty, Nicholas Armstrong-Crews, Tiffany L. Chen et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robust 3D object detection is critical for safe autonomous driving. Camera and radar sensors are synergistic as they capture complementary information and work well under different environmental conditions. Fusing camera and radar data is challenging, however, as each of the sensors lacks information along a perpendicular axis, that is, depth is unknown to camera and elevation is unknown to radar. We propose the camera-radar matching network CramNet, an efficient approach to fuse the sensor readings from camera and radar in a joint 3D space. To leverage radar range measurements for better camera depth predictions, we propose a novel ray-constrained cross-attention mechanism that resolves the ambiguity in the geometric correspondences between camera features and radar features. Our method supports training with sensor modality dropout, which leads to robust 3D object detection, even when a camera or radar sensor suddenly malfunctions on a vehicle. We demonstrate the effectiveness of our fusion approach through extensive experiments on the RADIATE dataset, one of the few large-scale datasets that provide radar radio frequency imagery. A camera-only variant of our method achieves competitive performance in monocular 3D object detection on the Waymo Open Dataset.

</details>

### DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection.
- **链接**: [arXiv:2207.10758](https://arxiv.org/abs/2207.10758) · 📚 被引 69
- **作者**: Abhinav Kumar, Garrick Brazil, Enrique Corona, Armin Parchami, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern neural networks use building blocks such as convolutions that are equivariant to arbitrary 2D translations. However, these vanilla blocks are not equivariant to arbitrary 3D translations in the projective manifold. Even then, all monocular 3D detectors use vanilla blocks to obtain the 3D coordinates, a task for which the vanilla blocks are not designed for. This paper takes the first step towards convolutions equivariant to arbitrary 3D translations in the projective manifold. Since the depth is the hardest to estimate for monocular detection, this paper proposes Depth EquiVarIAnt NeTwork (DEVIANT) built with existing scale equivariant steerable blocks. As a result, DEVIANT is equivariant to the depth translations in the projective manifold whereas vanilla networks are not. The additional depth equivariance forces the DEVIANT to learn consistent depth estimates, and therefore, DEVIANT achieves state-of-the-art monocular 3D detection results on KITTI and Waymo datasets in the image-only category and performs competitively to methods using extra information. Moreover, DEVIANT works better than vanilla networks in cross-dataset evaluation. Code and models at https://github.com/abhi1kumar/DEVIANT

</details>

### Densely Constrained Depth Estimator for Monocular 3D Object Detection.
- **链接**: [arXiv:2207.10047](https://arxiv.org/abs/2207.10047)
- **作者**: Yingyan Li, Yuntao Chen, Jiawei He, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating accurate 3D locations of objects from monocular images is a challenging problem because of lacking depth. Previous work shows that utilizing the object's keypoint projection constraints to estimate multiple depth candidates boosts the detection performance. However, the existing methods can only utilize vertical edges as projection constraints for depth estimation. So these methods only use a small number of projection constraints and produce insufficient depth candidates, leading to inaccurate depth estimation. In this paper, we propose a method that utilizes dense projection constraints from edges of any direction. In this way, we employ much more projection constraints and produce considerable depth candidates. Besides, we present a graph matching weighting module to merge the depth candidates. The proposed method DCD (Densely Constrained Detector) achieves state-of-the-art performance on the KITTI and WOD benchmarks. Code is released at https://github.com/BraveGroup/DCD.

</details>

### Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training.
- **链接**: [arXiv:2204.11590](https://arxiv.org/abs/2204.11590)
- **作者**: Zhenyu Li, Zehui Chen, Ang Li, Liangji Fang, Qinhong Jiang, Xianming Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection (Mono3D) has achieved unprecedented success with the advent of deep learning techniques and emerging large-scale autonomous driving datasets. However, drastic performance degradation remains an unwell-studied challenge for practical cross-domain deployment as the lack of labels on the target domain. In this paper, we first comprehensively investigate the significant underlying factor of the domain gap in Mono3D, where the critical observation is a depth-shift issue caused by the geometric misalignment of domains. Then, we propose STMono3D, a new self-teaching framework for unsupervised domain adaptation on Mono3D. To mitigate the depth-shift, we introduce the geometry-aligned multi-scale training strategy to disentangle the camera parameters and guarantee the geometry consistency of domains. Based on this, we develop a teacher-student paradigm to generate adaptive pseudo labels on the target domain. Benefiting from the end-to-end framework that provides richer information of the pseudo labels, we propose the quality-aware supervision strategy to take instance-level pseudo confidences into account and improve the effectiveness of the target-domain training process. Moreover, the positive focusing training strategy and dynamic threshold are proposed to handle tremendous FN and FP pseudo samples. STMono3D achieves remarkable performance on all evaluated datasets and even surpasses fully supervised results on the KITTI 3D object detection dataset. To the best of our knowledge, this is the first study to explore effective UDA methods for Mono3D.

</details>

### Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection.
- **链接**: [arXiv:2210.09615](https://arxiv.org/abs/2210.09615)
- **作者**: Xin Li, Botian Shi, Yuenan Hou, Xingjiao Wu, Tianlong Ma, Yikang Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal 3D object detection has been an active research topic in autonomous driving. Nevertheless, it is non-trivial to explore the cross-modal feature fusion between sparse 3D points and dense 2D pixels. Recent approaches either fuse the image features with the point cloud features that are projected onto the 2D image plane or combine the sparse point cloud with dense image pixels. These fusion approaches often suffer from severe information loss, thus causing sub-optimal performance. To address these problems, we construct the homogeneous structure between the point cloud and images to avoid projective information loss by transforming the camera features into the LiDAR 3D space. In this paper, we propose a homogeneous multi-modal feature fusion and interaction method (HMFI) for 3D object detection. Specifically, we first design an image voxel lifter module (IVLM) to lift 2D image features into the 3D space and generate homogeneous image voxel features. Then, we fuse the voxelized point cloud features with the image features from different regions by introducing the self-attention based query fusion mechanism (QFM). Next, we propose a voxel feature interaction module (VFIM) to enforce the consistency of semantic information from identical objects in the homogeneous point cloud and image voxel representations, which can provide object-level alignment guidance for cross-modal feature fusion and strengthen the discriminative ability in complex backgrounds. We conduct extensive experiments on the KITTI and Waymo Open Dataset, and the proposed HMFI achieves better performance compared with the state-of-the-art multi-modal methods. Particularly, for the 3D detection of cyclist on the KITTI benchmark, HMFI surpasses all the published algorithms by a large margin.

</details>

### Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_31) · 📚 被引 8
- **作者**: Hao Li, Zehan Zhang, Xian Zhao, Yulong Wang, Yuxi Shen, Shiliang Pu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection.
- **链接**: [arXiv:2203.09510](https://arxiv.org/abs/2203.09510) · 📚 被引 24
- **作者**: Jinhyung Park, Chenfeng Xu, Yiyang Zhou, Masayoshi Tomizuka, Wei Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While numerous 3D detection works leverage the complementary relationship between RGB images and point clouds, developments in the broader framework of semi-supervised object recognition remain uninfluenced by multi-modal fusion. Current methods develop independent pipelines for 2D and 3D semi-supervised learning despite the availability of paired image and point cloud frames. Observing that the distinct characteristics of each sensor cause them to be biased towards detecting different objects, we propose DetMatch, a flexible framework for joint semi-supervised learning on 2D and 3D modalities. By identifying objects detected in both sensors, our pipeline generates a cleaner, more robust set of pseudo-labels that both demonstrates stronger performance and stymies single-modality error propagation. Further, we leverage the richer semantics of RGB images to rectify incorrect 3D class predictions and improve localization of 3D boxes. Evaluating on the challenging KITTI and Waymo datasets, we improve upon strong semi-supervised learning methods and observe higher quality pseudo-labels. Code will be released at https://github.com/Divadi/DetMatch

</details>

### DID-M3D: Decoupling Instance Depth for Monocular 3D Object Detection.
- **链接**: [arXiv:2207.08531](https://arxiv.org/abs/2207.08531) · 📚 被引 78
- **作者**: Liang Peng, Xiaopei Wu, Zheng Yang, Haifeng Liu, Deng Cai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D detection has drawn much attention from the community due to its low cost and setup simplicity. It takes an RGB image as input and predicts 3D boxes in the 3D space. The most challenging sub-task lies in the instance depth estimation. Previous works usually use a direct estimation method. However, in this paper we point out that the instance depth on the RGB image is non-intuitive. It is coupled by visual depth clues and instance attribute clues, making it hard to be directly learned in the network. Therefore, we propose to reformulate the instance depth to the combination of the instance visual surface depth (visual depth) and the instance attribute depth (attribute depth). The visual depth is related to objects' appearances and positions on the image. By contrast, the attribute depth relies on objects' inherent attributes, which are invariant to the object affine transformation on the image. Correspondingly, we decouple the 3D location uncertainty into visual depth uncertainty and attribute depth uncertainty. By combining different types of depths and associated uncertainties, we can obtain the final instance depth. Furthermore, data augmentation in monocular 3D detection is usually limited due to the physical nature, hindering the boost of performance. Based on the proposed instance depth disentanglement strategy, we can alleviate this problem. Evaluated on KITTI, our method achieves new state-of-the-art results, and extensive ablation studies validate the effectiveness of each component in our method. The codes are released at https://github.com/SPengLiang/DID-M3D.

</details>

### FCAF3D: Fully Convolutional Anchor-Free 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_28) · 📚 被引 125
- **作者**: Danila Rukhovich, Anna Vorontsova, Anton Konushin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Rethinking IoU-based Optimization for Single-stage 3D Object Detection.
- **链接**: [arXiv:2207.09332](https://arxiv.org/abs/2207.09332)
- **作者**: Hualian Sheng, Sijia Cai, Na Zhao, Bing Deng, Jianqiang Huang, Xian-Sheng Hua et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Since Intersection-over-Union (IoU) based optimization maintains the consistency of the final IoU prediction metric and losses, it has been widely used in both regression and classification branches of single-stage 2D object detectors. Recently, several 3D object detection methods adopt IoU-based optimization and directly replace the 2D IoU with 3D IoU. However, such a direct computation in 3D is very costly due to the complex implementation and inefficient backward operations. Moreover, 3D IoU-based optimization is sub-optimal as it is sensitive to rotation and thus can cause training instability and detection performance deterioration. In this paper, we propose a novel Rotation-Decoupled IoU (RDIoU) method that can mitigate the rotation-sensitivity issue, and produce more efficient optimization objectives compared with 3D IoU during the training stage. Specifically, our RDIoU simplifies the complex interactions of regression parameters by decoupling the rotation variable as an independent term, yet preserving the geometry of 3D IoU. By incorporating RDIoU into both the regression and classification branches, the network is encouraged to learn more precise bounding boxes and concurrently overcome the misalignment issue between classification and regression. Extensive experiments on the benchmark KITTI and Waymo Open Dataset validate that our RDIoU method can bring substantial improvement for the single-stage 3D object detection.

</details>

### PillarNet: Real-Time and High-Performance Pillar-Based 3D Object Detection.
- **链接**: [arXiv:2205.07403](https://arxiv.org/abs/2205.07403) · 📚 被引 211
- **作者**: Guangsheng Shi, Ruifeng Li, Chao Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-time and high-performance 3D object detection is of critical importance for autonomous driving. Recent top-performing 3D object detectors mainly rely on point-based or 3D voxel-based convolutions, which are both computationally inefficient for onboard deployment. In contrast, pillar-based methods use solely 2D convolutions, which consume less computation resources, but they lag far behind their voxel-based counterparts in detection accuracy. In this paper, by examining the primary performance gap between pillar- and voxel-based detectors, we develop a real-time and high-performance pillar-based detector, dubbed PillarNet.The proposed PillarNet consists of a powerful encoder network for effective pillar feature learning, a neck network for spatial-semantic feature fusion and the commonly used detect head. Using only 2D convolutions, PillarNet is flexible to an optional pillar size and compatible with classical 2D CNN backbones, such as VGGNet and ResNet. Additionally, PillarNet benefits from our designed orientation-decoupled IoU regression loss along with the IoU-aware prediction branch. Extensive experimental results on the large-scale nuScenes Dataset and Waymo Open Dataset demonstrate that the proposed PillarNet performs well over state-of-the-art 3D detectors in terms of effectiveness and efficiency. Code is available at \url{https://github.com/agent-sgs/PillarNet}.

</details>

### SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds.
- **链接**: [arXiv:2210.07372](https://arxiv.org/abs/2210.07372) · 📚 被引 129
- **作者**: Pei Sun, Mingxing Tan, Weiyue Wang, Chenxi Liu, Fei Xia, Zhaoqi Leng et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection in point clouds is a core component for modern robotics and autonomous driving systems. A key challenge in 3D object detection comes from the inherent sparse nature of point occupancy within the 3D scene. In this paper, we propose Sparse Window Transformer (SWFormer ), a scalable and accurate model for 3D object detection, which can take full advantage of the sparsity of point clouds. Built upon the idea of window-based Transformers, SWFormer converts 3D points into sparse voxels and windows, and then processes these variable-length sparse windows efficiently using a bucketing scheme. In addition to self-attention within each spatial window, our SWFormer also captures cross-window correlation with multi-scale feature fusion and window shifting operations. To further address the unique challenge of detecting 3D objects accurately from sparse features, we propose a new voxel diffusion technique. Experimental results on the Waymo Open Dataset show our SWFormer achieves state-of-the-art 73.36 L2 mAPH on vehicle and pedestrian for 3D object detection on the official test set, outperforming all previous single-stage and two-stage models, while being much more efficient.

</details>

### Monocular 3D Object Detection with Depth from Motion.
- **链接**: [arXiv:2207.12988](https://arxiv.org/abs/2207.12988)
- **作者**: Tai Wang, Jiangmiao Pang, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perceiving 3D objects from monocular inputs is crucial for robotic systems, given its economy compared to multi-sensor settings. It is notably difficult as a single image can not provide any clues for predicting absolute depth values. Motivated by binocular methods for 3D object detection, we take advantage of the strong geometry structure provided by camera ego-motion for accurate object depth estimation and detection. We first make a theoretical analysis on this general two-view case and notice two challenges: 1) Cumulative errors from multiple estimations that make the direct prediction intractable; 2) Inherent dilemmas caused by static cameras and matching ambiguity. Accordingly, we establish the stereo correspondence with a geometry-aware cost volume as the alternative for depth estimation and further compensate it with monocular understanding to address the second problem. Our framework, named Depth from Motion (DfM), then uses the established geometry to lift 2D image features to the 3D space and detects 3D objects thereon. We also present a pose-free DfM to make it usable when the camera pose is unavailable. Our framework outperforms state-of-the-art methods by a large margin on the KITTI benchmark. Detailed quantitative and qualitative analyses also validate our theoretical conclusions. The code will be released at https://github.com/Tai-Wang/Depth-from-Motion.

</details>

### LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection.
- **链接**: [arXiv:2203.14956](https://arxiv.org/abs/2203.14956)
- **作者**: Yi Wei, Zibu Wei, Yongming Rao, Jiaxin Li, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose the LiDAR Distillation to bridge the domain gap induced by different LiDAR beams for 3D object detection. In many real-world applications, the LiDAR points used by mass-produced robots and vehicles usually have fewer beams than that in large-scale public datasets. Moreover, as the LiDARs are upgraded to other product models with different beam amount, it becomes challenging to utilize the labeled data captured by previous versions' high-resolution sensors. Despite the recent progress on domain adaptive 3D detection, most methods struggle to eliminate the beam-induced domain gap. We find that it is essential to align the point cloud density of the source domain with that of the target domain during the training process. Inspired by this discovery, we propose a progressive framework to mitigate the beam-induced domain shift. In each iteration, we first generate low-beam pseudo LiDAR by downsampling the high-beam point clouds. Then the teacher-student framework is employed to distill rich information from the data with more beams. Extensive experiments on Waymo, nuScenes and KITTI datasets with three different LiDAR-based detectors demonstrate the effectiveness of our LiDAR Distillation. Notably, our approach does not increase any additional computation cost for inference.

</details>

### Semi-supervised 3D Object Detection with Proficient Teachers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_42) · 📚 被引 73
- **作者**: Junbo Yin, Jin Fang, Dingfu Zhou, Liangjun Zhang, Cheng-Zhong Xu, Jianbing Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### ProposalContrast: Unsupervised Pre-training for LiDAR-Based 3D Object Detection.
- **链接**: [arXiv:2207.12654](https://arxiv.org/abs/2207.12654) · 📚 被引 85
- **作者**: Junbo Yin, Dingfu Zhou, Liangjun Zhang, Jin Fang, Cheng-Zhong Xu, Jianbing Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing approaches for unsupervised point cloud pre-training are constrained to either scene-level or point/voxel-level instance discrimination. Scene-level methods tend to lose local details that are crucial for recognizing the road objects, while point/voxel-level methods inherently suffer from limited receptive field that is incapable of perceiving large objects or context environments. Considering region-level representations are more suitable for 3D object detection, we devise a new unsupervised point cloud pre-training framework, called ProposalContrast, that learns robust 3D representations by contrasting region proposals. Specifically, with an exhaustive set of region proposals sampled from each point cloud, geometric point relations within each proposal are modeled for creating expressive proposal representations. To better accommodate 3D detection properties, ProposalContrast optimizes with both inter-cluster and inter-proposal separation, i.e., sharpening the discriminativeness of proposal representations across semantic classes and object instances. The generalizability and transferability of ProposalContrast are verified on various 3D detectors (i.e., PV-RCNN, CenterPoint, PointPillars and PointRCNN) and datasets (i.e., KITTI, Waymo and ONCE).

</details>

### CenterFormer: Center-Based Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_29) · 📚 被引 162
- **作者**: Zixiang Zhou, Xiangchen Zhao, Yu Wang, Panqu Wang, Hassan Foroosh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### MonoDistill: Learning Spatial Features for Monocular 3D Object Detection.
- **链接**: [arXiv:2201.10830](https://arxiv.org/abs/2201.10830)
- **作者**: Zhiyu Chong, Xinzhu Ma, Hong Zhang, Yuxin Yue, Haojie Li, Zhihui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a fundamental and challenging task for 3D scene understanding, and the monocular-based methods can serve as an economical alternative to the stereo-based or LiDAR-based methods. However, accurately detecting objects in the 3D space from a single image is extremely difficult due to the lack of spatial cues. To mitigate this issue, we propose a simple and effective scheme to introduce the spatial information from LiDAR signals to the monocular 3D detectors, without introducing any extra cost in the inference phase. In particular, we first project the LiDAR signals into the image plane and align them with the RGB images. After that, we use the resulting data to train a 3D detector (LiDAR Net) with the same architecture as the baseline model. Finally, this LiDAR Net can serve as the teacher to transfer the learned knowledge to the baseline model. Experimental results show that the proposed method can significantly boost the performance of the baseline model and ranks the $1^{st}$ place among all monocular-based methods on the KITTI benchmark. Besides, extensive ablation studies are conducted, which further prove the effectiveness of each part of our designs and illustrate what the baseline model has learned from the LiDAR Net. Our code will be released at \url{https://github.com/monster-ghost/MonoDistill}.

</details>

### WeakM3D: Towards Weakly Supervised Monocular 3D Object Detection.
- **链接**: [arXiv:2203.08332](https://arxiv.org/abs/2203.08332)
- **作者**: Liang Peng, Senbo Yan, Boxi Wu, Zheng Yang, Xiaofei He, Deng Cai
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is one of the most challenging tasks in 3D scene understanding. Due to the ill-posed nature of monocular imagery, existing monocular 3D detection methods highly rely on training with the manually annotated 3D box labels on the LiDAR point clouds. This annotation process is very laborious and expensive. To dispense with the reliance on 3D box labels, in this paper we explore the weakly supervised monocular 3D detection. Specifically, we first detect 2D boxes on the image. Then, we adopt the generated 2D boxes to select corresponding RoI LiDAR points as the weak supervision. Eventually, we adopt a network to predict 3D boxes which can tightly align with associated RoI LiDAR points. This network is learned by minimizing our newly-proposed 3D alignment loss between the 3D box estimates and the corresponding RoI LiDAR points. We will illustrate the potential challenges of the above learning problem and resolve these challenges by introducing several effective designs into our method. Codes will be available at https://github.com/SPengLiang/WeakM3D.

</details>

### Sparse2Dense: Learning to Densify 3D Features for 3D Object Detection.
- **链接**: [arXiv:2211.13067](https://arxiv.org/abs/2211.13067) · 📚 被引 3
- **作者**: Tianyu Wang, Xiaowei Hu, Zhengzhe Liu, Chi-Wing Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-produced point clouds are the major source for most state-of-the-art 3D object detectors. Yet, small, distant, and incomplete objects with sparse or few points are often hard to detect. We present Sparse2Dense, a new framework to efficiently boost 3D detection performance by learning to densify point clouds in latent space. Specifically, we first train a dense point 3D detector (DDet) with a dense point cloud as input and design a sparse point 3D detector (SDet) with a regular point cloud as input. Importantly, we formulate the lightweight plug-in S2D module and the point cloud reconstruction module in SDet to densify 3D features and train SDet to produce 3D features, following the dense 3D features in DDet. So, in inference, SDet can simulate dense 3D features from regular (sparse) point cloud inputs without requiring dense inputs. We evaluate our method on the large-scale Waymo Open Dataset and the Waymo Domain Adaptation Dataset, showing its high performance and efficiency over the state of the arts.

</details>

### MsSVT: Mixed-scale Sparse Voxel Transformer for 3D Object Detection on Point Clouds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4bad7c27534efca029ca0d366c47c0e3-Abstract-Conference.html) · 📚 被引 1
- **作者**: Shaocong Dong, Lihe Ding, Haiyang Wang, Tingfa Xu, Xinli Xu, Jie Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Fully Sparse 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/0247fa3c511bbc415c8b768ee7b32f9e-Abstract-Conference.html)
- **作者**: Lue Fan, Feng Wang, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Unifying Voxel-based Representation with Transformer for 3D Object Detection.
- **链接**: [arXiv:2206.00630](https://arxiv.org/abs/2206.00630) · 📚 被引 34
- **作者**: Yanwei Li, Yilun Chen, Xiaojuan Qi, Zeming Li, Jian Sun, Jiaya Jia
- **🏷️ 机构**: MEGVII, CUHK / SmartMore
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we present a unified framework for multi-modality 3D object detection, named UVTR. The proposed method aims to unify multi-modality representations in the voxel space for accurate and robust single- or cross-modality 3D detection. To this end, the modality-specific space is first designed to represent different inputs in the voxel feature space. Different from previous work, our approach preserves the voxel space without height compression to alleviate semantic ambiguity and enable spatial connections. To make full use of the inputs from different sensors, the cross-modality interaction is then proposed, including knowledge transfer and modality fusion. In this way, geometry-aware expressions in point clouds and context-rich features in images are well utilized for better performance and robustness. The transformer decoder is applied to efficiently sample features from the unified space with learnable positions, which facilitates object-level interactions. In general, UVTR presents an early attempt to represent different modalities in a unified framework. It surpasses previous work in single- or multi-modality entries. The proposed method achieves leading performance in the nuScenes test set for both object detection and the following object tracking task. Code is made publicly available at https://github.com/dvlab-research/UVTR.

</details>

### CAGroup3D: Class-Aware Grouping for 3D Object Detection on Point Clouds.
- **链接**: [arXiv:2210.04264](https://arxiv.org/abs/2210.04264) · 📚 被引 13
- **作者**: Haiyang Wang, Lihe Ding, Shaocong Dong, Shaoshuai Shi, Aoxue Li, Jianan Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel two-stage fully sparse convolutional 3D object detection framework, named CAGroup3D. Our proposed method first generates some high-quality 3D proposals by leveraging the class-aware local group strategy on the object surface voxels with the same semantic predictions, which considers semantic consistency and diverse locality abandoned in previous bottom-up approaches. Then, to recover the features of missed voxels due to incorrect voxel-wise segmentation, we build a fully sparse convolutional RoI pooling module to directly aggregate fine-grained spatial information from backbone for further proposal refinement. It is memory-and-computation efficient and can better encode the geometry-specific features of each 3D proposal. Our model achieves state-of-the-art 3D detection performance with remarkable gains of +\textit{3.6\%} on ScanNet V2 and +\textit{2.6}\% on SUN RGB-D in term of mAP@0.25. Code will be available at https://github.com/Haiyang-W/CAGroup3D.

</details>

### DeepInteraction: 3D Object Detection via Modality Interaction.
- **链接**: [arXiv:2208.11112](https://arxiv.org/abs/2208.11112) · 📚 被引 31
- **作者**: Zeyu Yang, Jiaqi Chen, Zhenwei Miao, Wei Li, Xiatian Zhu, Li Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing top-performance 3D object detectors typically rely on the multi-modal fusion strategy. This design is however fundamentally restricted due to overlooking the modality-specific useful information and finally hampering the model performance. To address this limitation, in this work we introduce a novel modality interaction strategy where individual per-modality representations are learned and maintained throughout for enabling their unique characteristics to be exploited during object detection. To realize this proposed strategy, we design a DeepInteraction architecture characterized by a multi-modal representational interaction encoder and a multi-modal predictive interaction decoder. Experiments on the large-scale nuScenes dataset show that our proposed method surpasses all prior arts often by a large margin. Crucially, our method is ranked at the first position at the highly competitive nuScenes object detection leaderboard.

</details>

### MoGDE: Boosting Mobile Monocular 3D Object Detection with Ground Depth Estimation.
- **链接**: [arXiv:2303.13561](https://arxiv.org/abs/2303.13561) · 📚 被引 3
- **作者**: Yunsong Zhou, Quan Liu, Hongzi Zhu, Yunzhe Li, Shan Chang, Minyi Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection (Mono3D) in mobile settings (e.g., on a vehicle, a drone, or a robot) is an important yet challenging task. Due to the near-far disparity phenomenon of monocular vision and the ever-changing camera pose, it is hard to acquire high detection accuracy, especially for far objects. Inspired by the insight that the depth of an object can be well determined according to the depth of the ground where it stands, in this paper, we propose a novel Mono3D framework, called MoGDE, which constantly estimates the corresponding ground depth of an image and then utilizes the estimated ground depth information to guide Mono3D. To this end, we utilize a pose detection network to estimate the pose of the camera and then construct a feature map portraying pixel-level ground depth according to the 3D-to-2D perspective geometry. Moreover, to improve Mono3D with the estimated ground depth, we design an RGB-D feature fusion network based on the transformer structure, where the long-range self-attention mechanism is utilized to effectively identify ground-contacting points and pin the corresponding ground depth to the image feature map. We conduct extensive experiments on the real-world KITTI dataset. The results demonstrate that MoGDE can effectively improve the Mono3D accuracy and robustness for both near and far objects. MoGDE yields the best performance compared with the state-of-the-art methods by a large margin and is ranked number one on the KITTI 3D benchmark.

</details>

## 跨领域论文（完整笔记在其他领域）

- BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. → [bev](../bev/Guideline%202022.md)
- V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- Bridged Transformer for Vision and Point Cloud 3D Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention. → [object-detection](../object-detection/Guideline%202022.md)
- A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation. → [object-detection](../object-detection/Guideline%202022.md)
- Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- RIDDLE: Lidar Data Compression with Range Image Deep Delta Encoding. → [network-pruning](../network-pruning/Guideline%202022.md)
- Beyond 3D Siamese Tracking: A Motion-Centric Paradigm for 3D Single Object Tracking in Point Clouds. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Multimodal Transformer for Automatic 3D Annotation and Object Detection. → [multimodal](../multimodal/Guideline%202022.md)
- PETR: Position Embedding Transformation for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Lidar Point Cloud Guided Monocular 3D Object Detection. → [bev](../bev/Guideline%202022.md)
- Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph. → [bev](../bev/Guideline%202022.md)
- Point Cloud Compression with Sibling Context and Surface Priors. → [network-pruning](../network-pruning/Guideline%202022.md)
- MvDeCor: Multi-view Dense Correspondence Learning for Fine-Grained 3D Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- PolarMOT: How Far Can Geometric Relations Take us in 3D Multi-object Tracking? → [tracking](../tracking/Guideline%202022.md)
- Motion Inspired Unsupervised Perception and Prediction in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- A Closer Look at Invariances in Self-supervised Pre-training for 3D Vision. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Spatial Pruned Sparse Convolution for Efficient 3D Object Detection. → [network-pruning](../network-pruning/Guideline%202022.md)
- Fully Convolutional One-Stage 3D Object Detection on LiDAR Range Images. → [bev](../bev/Guideline%202022.md)
- Towards Efficient 3D Object Detection with Knowledge Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202022.md)
- Unsupervised Adaptation from Repeated Traversals for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)

<!-- COMPLETE v1 papers=59 -->
