# 3D Detection — 2021 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

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

### GrooMeD-NMS: Grouped Mathematically Differentiable NMS for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2103.17202](https://arxiv.org/abs/2103.17202) · 📚 被引 88
- **作者**: Abhinav Kumar, Garrick Brazil, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目3D检测中NMS后处理与训练推理不一致的问题，提出GrooMeD-NMS，一种分组数学可微NMS方法，将NMS表示为矩阵操作并通过无监督分组和掩码获得闭式解。该方法使网络能够以端到端方式训练，并在NMS后计算损失，强制网络以可微方式选择最佳3D框。在KITTI基准上达到单目3D检测的最先进性能，与基于视频的方法相当。
- **摘要（英）**: This paper addresses the mismatch between training and inference in monocular 3D detection by proposing GrooMeD-NMS, a grouped mathematically differentiable NMS formulated as matrix operations with a closed-form solution. It enables end-to-end training with loss computed after NMS, forcing the network to select the best 3D box differentiably. It achieves state-of-the-art results on KITTI, comparable to video-based methods.
- **核心贡献**: 提出首个数学可微的NMS方法并集成到单目3D检测训练中。
- **创新点**: 将NMS转化为矩阵操作并实现闭式可微表达。
- **结果**: 在KITTI上达到SOTA，与视频方法性能相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern 3D object detectors have immensely benefited from the end-to-end learning idea. However, most of them use a post-processing algorithm called Non-Maximal Suppression (NMS) only during inference. While there were attempts to include NMS in the training pipeline for tasks such as 2D object detection, they have been less widely adopted due to a non-mathematical expression of the NMS. In this paper, we present and integrate GrooMeD-NMS -- a novel Grouped Mathematically Differentiable NMS for monocular 3D object detection, such that the network is trained end-to-end with a loss on the boxes after NMS. We first formulate NMS as a matrix operation and then group and mask the boxes in an unsupervised manner to obtain a simple closed-form expression of the NMS. GrooMeD-NMS addresses the mismatch between training and inference pipelines and, therefore, forces the network to select the best 3D box in a differentiable manner. As a result, GrooMeD-NMS achieves state-of-the-art monocular 3D object detection results on the KITTI benchmark dataset performing comparably to monocular video-based methods. Code and models at https://github.com/abhi1kumar/groomed_nms

</details>

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

### 3DIoUMatch: Leveraging IoU Prediction for Semi-Supervised 3D Object Detection.
- **链接**: [arXiv:2012.04355](https://arxiv.org/abs/2012.04355) · 📚 被引 121
- **作者**: He Wang, Yezhen Cong, Or Litany, Yue Gao, Leonidas J. Guibas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

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

### To the Point: Efficient 3D Object Detection in the Range Image With Graph Convolution Kernels. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2106.13381](https://arxiv.org/abs/2106.13381) · 📚 被引 68
- **作者**: Yuning Chai, Pei Sun, Jiquan Ngiam, Weiyue Wang, Benjamin Caine, Vijay Vasudevan et al.
- **🏷️ 机构**: Waymo
- **会议**: CVPR 2021
- **摘要（中）**: 针对基于距离图像的3D检测中几何信息利用不足问题，提出一种2D卷积网络架构，在整个网络中携带每个像素的3D球坐标，并允许层使用任意卷积核以利用局部几何。设计了四种核：密集核和三种图核（Transformer、PointNet、Edge Convolution），并探索与相机图像的跨模态融合。在Waymo数据集上，行人检测AP从69.7%提升至75.5%，最小模型比PointPillars质量更高且计算量减少180倍。
- **摘要（英）**: This paper addresses the underutilization of geometry in range-image-based 3D detection by proposing a 2D CNN that carries 3D spherical coordinates throughout the network and supports arbitrary convolution kernels. It designs four kernels including graph-based ones and explores cross-modal fusion. On Waymo, it improves pedestrian AP from 69.7% to 75.5%, with a minimal model 180x more efficient than PointPillars.
- **核心贡献**: 提出携带3D坐标的2D卷积网络用于距离图像3D检测。
- **创新点**: 在2D网络中嵌入3D几何并支持多种卷积核。
- **结果**: 在Waymo上显著提升行人检测AP并大幅降低计算量。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is vital for many robotics applications. For tasks where a 2D perspective range image exists, we propose to learn a 3D representation directly from this range image view. To this end, we designed a 2D convolutional network architecture that carries the 3D spherical coordinates of each pixel throughout the network. Its layers can consume any arbitrary convolution kernel in place of the default inner product kernel and exploit the underlying local geometry around each pixel. We outline four such kernels: a dense kernel according to the bag-of-words paradigm, and three graph kernels inspired by recent graph neural network advances: the Transformer, the PointNet, and the Edge Convolution. We also explore cross-modality fusion with the camera image, facilitated by operating in the perspective range image view. Our method performs competitively on the Waymo Open Dataset and improves the state-of-the-art AP for pedestrian detection from 69.7% to 75.5%. It is also efficient in that our smallest model, which still outperforms the popular PointPillars in quality, requires 180 times fewer FLOPS and model parameters

</details>

### MonoRUn: Monocular 3D Object Detection by Reconstruction and Uncertainty Propagation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2103.12605](https://arxiv.org/abs/2103.12605) · 📚 被引 131
- **作者**: Hansheng Chen, Yuyao Huang, Wei Tian, Zhong Gao, Lu Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目3D检测中依赖真实几何标注的问题，提出MonoRUn，一种自监督学习密集对应和几何的检测框架，仅需3D框标注。采用区域重建网络和不确定性感知，通过将预测3D坐标投影回图像平面，使用Robust KL损失最小化不确定性加权重投影误差。测试时传播不确定性，利用不确定性驱动的PnP算法估计姿态和协方差。实验表明方法有效。
- **摘要（英）**: This paper addresses the reliance on ground-truth geometry in monocular 3D detection by proposing MonoRUn, a self-supervised framework that learns dense correspondences and geometry with only 3D box annotations. It uses a regional reconstruction network with uncertainty awareness and a Robust KL loss for reprojection error. During testing, uncertainty is propagated through an uncertainty-driven PnP algorithm for pose estimation.
- **核心贡献**: 提出自监督的单目3D检测框架MonoRUn。
- **创新点**: 利用不确定性传播和Robust KL损失实现自监督几何学习。
- **结果**: 在实验中验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object localization in 3D space is a challenging aspect in monocular 3D object detection. Recent advances in 6DoF pose estimation have shown that predicting dense 2D-3D correspondence maps between image and object 3D model and then estimating object pose via Perspective-n-Point (PnP) algorithm can achieve remarkable localization accuracy. Yet these methods rely on training with ground truth of object geometry, which is difficult to acquire in real outdoor scenes. To address this issue, we propose MonoRUn, a novel detection framework that learns dense correspondences and geometry in a self-supervised manner, with simple 3D bounding box annotations. To regress the pixel-related 3D object coordinates, we employ a regional reconstruction network with uncertainty awareness. For self-supervised training, the predicted 3D coordinates are projected back to the image plane. A Robust KL loss is proposed to minimize the uncertainty-weighted reprojection error. During testing phase, we exploit the network uncertainty by propagating it through all downstream modules. More specifically, the uncertainty-driven PnP algorithm is leveraged to estimate object pose and its covariance. Extensive experiments demonstrate that our proposed approach outperforms current state-of-the-art methods on KITTI benchmark.

</details>

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

### Back-Tracing Representative Points for Voting-Based 3D Object Detection in Point Clouds. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2104.06114](https://arxiv.org/abs/2104.06114) · 📚 被引 114
- **作者**: Bowen Cheng, Lu Sheng, Shaoshuai Shi, Ming Yang, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①这篇论文针对点云3D目标检测中Hough投票策略只能接收部分表面投票且受背景离群点干扰的问题。②提出了Back-tracing Representative Points Network (BRNet)，从投票中心回溯代表性点，并重新访问互补种子点，以捕捉局部结构特征。③相比现有投票方法，通过自底向上和自顶向下策略增强投票中心与原始表面点的一致性。④摘要未提供具体数据，但预期在标准3D检测基准上提升定位精度和可靠性。
- **摘要（英）**: This paper addresses limitations in Hough voting for 3D object detection by proposing BRNet, which back-traces representative points from vote centers and revisits seed points. This improves local feature capture and consistency, likely enhancing localization accuracy, though specific results are not detailed.
- **核心贡献**: 提出回溯代表性点网络改进3D投票检测。
- **创新点**: 自底向上和自顶向下结合的回溯策略。
- **结果**: 预期提升3D检测定位精度和可靠性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection in point clouds is a challenging vision task that benefits various applications for understanding the 3D visual world. Lots of recent research focuses on how to exploit end-to-end trainable Hough voting for generating object proposals. However, the current voting strategy can only receive partial votes from the surfaces of potential objects together with severe outlier votes from the cluttered backgrounds, which hampers full utilization of the information from the input point clouds. Inspired by the back-tracing strategy in the conventional Hough voting methods, in this work, we introduce a new 3D object detection method, named as Back-tracing Representative Points Network (BRNet), which generatively back-traces the representative points from the vote centers and also revisits complementary seed points around these generated points, so as to better capture the fine local structural features surrounding the potential objects from the raw point clouds. Therefore, this bottom-up and then top-down strategy in our BRNet enforces mutual consistency between the predicted vote centers and the raw surface points and thus achieves more reliable and flexible object localization and class prediction results. Our BRNet is simple but effective, which significantly outperforms the state-of-the-art methods on two large-scale point cloud datasets, ScanNet V2 (+7.5% in terms of mAP@0.50) and SUN RGB-D (+4.7% in terms of mAP@0.50), while it is still lightweight and efficient. Code will be available at https://github.com/cheng052/BRNet.

</details>

### Geometry-based Distance Decomposition for Monocular 3D Object Detection.
- **链接**: [arXiv:2104.03775](https://arxiv.org/abs/2104.03775) · 📚 被引 147
- **作者**: Xuepeng Shi, Qi Ye, Xiaozhi Chen, Chuangrong Chen, Zhixiang Chen, Tae-Kyun Kim
- **🏷️ 机构**: Imperial College London, Zhejiang University, DJI
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is of great significance for autonomous driving but remains challenging. The core challenge is to predict the distance of objects in the absence of explicit depth information. Unlike regressing the distance as a single variable in most existing methods, we propose a novel geometry-based distance decomposition to recover the distance by its factors. The decomposition factors the distance of objects into the most representative and stable variables, i.e. the physical height and the projected visual height in the image plane. Moreover, the decomposition maintains the self-consistency between the two heights, leading to robust distance prediction when both predicted heights are inaccurate. The decomposition also enables us to trace the causes of the distance uncertainty for different scenarios. Such decomposition makes the distance prediction interpretable, accurate, and robust. Our method directly predicts 3D bounding boxes from RGB images with a compact architecture, making the training and inference simple and efficient. The experimental results show that our method achieves the state-of-the-art performance on the monocular 3D Object Detection and Birds Eye View tasks of the KITTI dataset, and can generalize to images with different camera intrinsics.

</details>

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

### LiDAR-Aug: A General Rendering-Based Augmentation Framework for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Fang_LiDAR-Aug_A_General_Rendering-Based_Augmentation_Framework_for_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 52
- **作者**: Jin Fang, Xinxin Zuo, Dingfu Zhou, Shengze Jin, Sen Wang, Liangjun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对3D目标检测中数据增强方法缺乏通用性和真实感的问题，提出基于渲染的通用增强框架LiDAR-Aug，通过渲染技术生成多样化的点云增强样本。该方法适用于多种3D检测框架，在KITTI等基准上验证了有效性，但摘要未提供具体数据。
- **摘要（英）**: To address the lack of general and realistic augmentation in 3D object detection, this paper proposes LiDAR-Aug, a rendering-based framework that generates diverse point cloud augmentations. It is applicable to various detectors and shows effectiveness on benchmarks like KITTI, though specific results are not detailed.
- **核心贡献**: 提出基于渲染的通用增强框架LiDAR-Aug。
- **创新点**: 利用渲染技术生成真实感点云增强样本。
- **结果**: 在3D检测基准上验证了有效性。

### Delving Into Localization Errors for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ma_Delving_Into_Localization_Errors_for_Monocular_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 242
- **作者**: Xinzhu Ma, Yinmin Zhang, Dan Xu, Dongzhan Zhou, Shuai Yi, Haojie Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对单目3D目标检测中定位误差导致检测精度低的问题。②提出了一种深入分析定位误差来源的方法，并设计了相应的损失函数和网络结构来优化定位精度。③相比已有工作，更系统地分解了定位误差，并针对性地改进。④在KITTI基准上显著提升了3D检测性能，尤其在定位精度方面。
- **摘要（英）**: This paper addresses localization errors in monocular 3D object detection. It proposes a systematic analysis of error sources and designs tailored loss functions and network modifications to improve localization accuracy. Compared to prior work, it offers a more granular decomposition of errors, leading to significant performance gains on KITTI.
- **核心贡献**: 系统分析了单目3D检测中的定位误差并提出了针对性优化方法。
- **创新点**: 将定位误差分解为多个维度并设计专用损失函数。
- **结果**: 在KITTI基准上显著提升了定位精度和整体检测性能。

### HVPR: Hybrid Voxel-Point Representation for Single-Stage 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Noh_HVPR_Hybrid_Voxel-Point_Representation_for_Single-Stage_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 153
- **作者**: Jongyoun Noh, Sanghoon Lee, Bumsub Ham
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对单阶段3D目标检测中体素和点表示各自局限性的问题。②提出了混合体素-点表示（HVPR），结合体素的高效性和点的精确性，通过特征融合模块增强检测性能。③相比纯体素或纯点方法，HVPR在保持速度的同时提高了精度。④在KITTI和Waymo数据集上取得了优于现有单阶段方法的性能。
- **摘要（英）**: This paper tackles the limitations of voxel and point representations in single-stage 3D detection. It introduces a hybrid voxel-point representation (HVPR) that combines efficiency and precision via feature fusion. Compared to pure voxel or point methods, HVPR improves accuracy while maintaining speed, achieving superior results on KITTI and Waymo.
- **核心贡献**: 提出混合体素-点表示用于单阶段3D检测。
- **创新点**: 设计特征融合模块有效结合体素和点信息。
- **结果**: 在多个基准上超越现有单阶段方法。

### 3D Object Detection With Pointformer. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Pan_3D_Object_Detection_With_Pointformer_CVPR_2021_paper.html)
- **作者**: Xuran Pan, Zhuofan Xia, Shiji Song, Li Erran Li, Gao Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对3D目标检测中Transformer架构对点云特征提取不足的问题。②提出了Pointformer，将Transformer应用于点云处理，通过自注意力机制捕捉点间关系。③相比传统卷积方法，Pointformer能更好地建模全局上下文。④在标准3D检测基准上展示了竞争力，但性能提升有限。
- **摘要（英）**: This paper addresses the underutilization of Transformer architectures in point cloud-based 3D detection. It proposes Pointformer, applying self-attention to capture inter-point relationships. Compared to convolutional methods, it better models global context, showing competitive results on standard benchmarks.
- **核心贡献**: 将Transformer架构引入点云3D检测。
- **创新点**: 利用自注意力机制增强点云特征提取。
- **结果**: 在基准上取得有竞争力的性能。

### Offboard 3D Object Detection From Point Cloud Sequences. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2103.05073](https://arxiv.org/abs/2103.05073) · 📚 被引 161
- **作者**: Charles R. Qi, Yin Zhou, Mahyar Najibi, Pei Sun, Khoa Vo, Boyang Deng et al.
- **🏷️ 机构**: Waymo LLC
- **会议**: CVPR 2021
- **摘要（中）**: ①针对离线3D目标检测场景（如自动生成高质量3D标签）未被充分探索的问题。②提出了3D Auto Labeling流水线，利用点云序列数据，通过多帧检测和对象中心细化模型提升检测质量。③相比在线检测器，离线方法不受实时性限制，能利用更多时序信息。④在Waymo Open Dataset上显著优于现有在线检测器，性能与人工标签相当，并展示了在半监督学习中的应用。
- **摘要（英）**: This paper addresses the under-explored offboard 3D detection scenario for high-quality label generation. It proposes a 3D Auto Labeling pipeline using point cloud sequences, combining multi-frame detection and object-centric refinement. Compared to onboard detectors, it leverages temporal information without real-time constraints, achieving performance on par with human labels on Waymo and enabling semi-supervised learning.
- **核心贡献**: 提出首个高效的离线3D检测流水线用于自动标签生成。
- **创新点**: 利用时序点云和对象中心细化模型提升检测精度。
- **结果**: 性能与人工标签相当，并支持半监督学习。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While current 3D object recognition research mostly focuses on the real-time, onboard scenario, there are many offboard use cases of perception that are largely under-explored, such as using machines to automatically generate high-quality 3D labels. Existing 3D object detectors fail to satisfy the high-quality requirement for offboard uses due to the limited input and speed constraints. In this paper, we propose a novel offboard 3D object detection pipeline using point cloud sequence data. Observing that different frames capture complementary views of objects, we design the offboard detector to make use of the temporal points through both multi-frame object detection and novel object-centric refinement models. Evaluated on the Waymo Open Dataset, our pipeline named 3D Auto Labeling shows significant gains compared to the state-of-the-art onboard detectors and our offboard baselines. Its performance is even on par with human labels verified through a human label study. Further experiments demonstrate the application of auto labels for semi-supervised learning and provide extensive analysis to validate various design choices.

</details>

### SPG: Unsupervised Domain Adaptation for 3D Object Detection via Semantic Point Generation.
- **链接**: [arXiv:2108.06709](https://arxiv.org/abs/2108.06709) · 📚 被引 144
- **作者**: Qiangeng Xu, Yin Zhou, Weiyue Wang, Charles R. Qi, Dragomir Anguelov
- **🏷️ 机构**: University of Southern California, Waymo, LLC
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, a LiDAR-based object detector should perform reliably at different geographic locations and under various weather conditions. While recent 3D detection research focuses on improving performance within a single domain, our study reveals that the performance of modern detectors can drop drastically cross-domain. In this paper, we investigate unsupervised domain adaptation (UDA) for LiDAR-based 3D object detection. On the Waymo Domain Adaptation dataset, we identify the deteriorating point cloud quality as the root cause of the performance drop. To address this issue, we present Semantic Point Generation (SPG), a general approach to enhance the reliability of LiDAR detectors against domain shifts. Specifically, SPG generates semantic points at the predicted foreground regions and faithfully recovers missing parts of the foreground objects, which are caused by phenomena such as occlusions, low reflectance or weather interference. By merging the semantic points with the original points, we obtain an augmented point cloud, which can be directly consumed by modern LiDAR-based detectors. To validate the wide applicability of SPG, we experiment with two representative detectors, PointPillars and PV-RCNN. On the UDA task, SPG significantly improves both detectors across all object categories of interest and at all difficulty levels. SPG can also benefit object detection in the original domain. On the Waymo Open Dataset and KITTI, SPG improves 3D detection results of these two methods across all categories. Combined with PV-RCNN, SPG achieves state-of-the-art 3D detection results on KITTI.

</details>

### RSN: Range Sparse Net for Efficient, Accurate LiDAR 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_RSN_Range_Sparse_Net_for_Efficient_Accurate_LiDAR_3D_Object_CVPR_2021_paper.html) · 📚 被引 155
- **作者**: Pei Sun, Weiyue Wang, Yuning Chai, Gamaleldin Elsayed, Alex Bewley, Xiao Zhang et al.
- **🏷️ 机构**: Waymo LLC, Google
- **会议**: CVPR 2021
- **摘要（中）**: ①针对LiDAR 3D检测中计算效率和精度平衡的问题。②提出了Range Sparse Net（RSN），利用稀疏卷积和范围感知设计，在保持精度的同时提高效率。③相比密集处理方法，RSN通过稀疏化计算减少了资源消耗。④在多个基准上实现了高效且准确的检测性能。
- **摘要（英）**: This paper addresses the efficiency-accuracy trade-off in LiDAR 3D detection. It proposes Range Sparse Net (RSN), using sparse convolution and range-aware design to improve efficiency without sacrificing accuracy. Compared to dense methods, it reduces computational cost, achieving efficient and accurate detection on benchmarks.
- **核心贡献**: 提出范围稀疏网络用于高效LiDAR 3D检测。
- **创新点**: 利用稀疏卷积和范围信息优化计算。
- **结果**: 在保持精度的同时显著提升效率。

### PointAugmenting: Cross-Modal Augmentation for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_PointAugmenting_Cross-Modal_Augmentation_for_3D_Object_Detection_CVPR_2021_paper.html) · 📚 被引 459
- **作者**: Chunwei Wang, Chao Ma, Ming Zhu, Xiaokang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对3D目标检测中跨模态特征融合不足的问题，提出PointAugmenting方法，通过将点云特征增强到图像特征中，实现跨模态增强。方法利用点云提供的几何信息来增强2D图像特征，提升3D检测精度。相比已有工作，该方法简单有效，直接融合点云和图像特征，避免了复杂的伪LiDAR流程。实验在KITTI等数据集上验证了有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper introduces PointAugmenting, a cross-modal augmentation method that enhances image features with point cloud features for 3D object detection. It directly fuses geometric information from LiDAR into 2D features, avoiding complex pseudo-LiDAR pipelines. The approach demonstrates effectiveness on benchmarks like KITTI, though specific metrics are not provided in the abstract.
- **核心贡献**: 提出点云特征增强图像特征的跨模态融合方法。
- **创新点**: 直接利用点云几何信息增强图像特征，简化融合流程。
- **结果**: 在3D检测基准上验证有效性，但摘要未给出具体数据。

### Depth-Conditioned Dynamic Message Propagation for Monocular 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2103.16470](https://arxiv.org/abs/2103.16470) · 📚 被引 137
- **作者**: Li Wang, Liang Du, Xiaoqing Ye, Yanwei Fu, Guodong Guo, Xiangyang Xue et al.
- **🏷️ 机构**: Fudan University,School of Computer Science, Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, Baidu Inc.
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目3D目标检测中深度信息不准确和上下文建模不足的问题，提出深度条件动态消息传播（DDMP）网络。方法通过自适应采样上下文节点，动态预测深度相关的滤波权重和亲和矩阵来传播信息，并引入中心感知深度编码（CDE）任务缓解深度先验不准确。相比已有伪LiDAR方法，该方法直接集成多尺度深度信息与图像上下文，更高效。在KITTI基准上取得单目3D检测SOTA结果，排名第一（2020年11月16日）。
- **摘要（英）**: This paper proposes a depth-conditioned dynamic message propagation (DDMP) network for monocular 3D object detection, integrating multi-scale depth with image context via adaptive node sampling and dynamic filter weights. It introduces a center-aware depth encoding task to mitigate depth inaccuracies, avoiding complex pseudo-LiDAR pipelines. The method achieves state-of-the-art results on KITTI, ranking 1st on the monocular 3D detection track.
- **核心贡献**: 提出深度条件动态消息传播网络，有效融合深度和上下文信息。
- **创新点**: 动态预测深度相关滤波权重和亲和矩阵，结合中心感知深度编码。
- **结果**: 在KITTI单目3D检测上排名第一，达到SOTA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The objective of this paper is to learn context- and depth-aware feature representation to solve the problem of monocular 3D object detection. We make following contributions: (i) rather than appealing to the complicated pseudo-LiDAR based approach, we propose a depth-conditioned dynamic message propagation (DDMP) network to effectively integrate the multi-scale depth information with the image context;(ii) this is achieved by first adaptively sampling context-aware nodes in the image context and then dynamically predicting hybrid depth-dependent filter weights and affinity matrices for propagating information; (iii) by augmenting a center-aware depth encoding (CDE) task, our method successfully alleviates the inaccurate depth prior; (iv) we thoroughly demonstrate the effectiveness of our proposed approach and show state-of-the-art results among the monocular-based approaches on the KITTI benchmark dataset. Particularly, we rank $1^{st}$ in the highly competitive KITTI monocular 3D object detection track on the submission day (November 16th, 2020). Code and models are released at \url{https://github.com/fudan-zvg/DDMP}

</details>

### ST3D: Self-Training for Unsupervised Domain Adaptation on 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 92%)
- **链接**: [arXiv:2103.05346](https://arxiv.org/abs/2103.05346) · 📚 被引 182
- **作者**: Jihan Yang, Shaoshuai Shi, Zhe Wang, Hongsheng Li, Xiaojuan Qi
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2021
- **摘要（中）**: 针对3D目标检测中无监督域适应问题，提出ST3D自训练管道。方法首先在源域用随机对象缩放策略预训练检测器以缓解源域偏差，然后在目标域通过伪标签更新（使用质量感知三元组记忆库）和课程数据增强交替迭代优化。相比已有域适应方法，该设计确保伪标签一致性和高质量，避免过拟合简单样本。在多个数据集上达到SOTA，甚至超过KITTI上的全监督结果。
- **摘要（英）**: This paper presents ST3D, a self-training pipeline for unsupervised domain adaptation in 3D object detection, using random object scaling pre-training and iterative pseudo-label updating with a quality-aware triplet memory bank. It incorporates curriculum data augmentation to handle easy examples, achieving consistent high-quality pseudo-labels. ST3D achieves state-of-the-art results on multiple datasets, surpassing fully supervised performance on KITTI.
- **核心贡献**: 提出ST3D自训练管道，实现3D检测的无监督域适应。
- **创新点**: 随机对象缩放预训练和质量感知三元组记忆库。
- **结果**: 在多个数据集上达到SOTA，超过KITTI全监督结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new domain adaptive self-training pipeline, named ST3D, for unsupervised domain adaptation on 3D object detection from point clouds. First, we pre-train the 3D detector on the source domain with our proposed random object scaling strategy for mitigating the negative effects of source domain bias. Then, the detector is iteratively improved on the target domain by alternatively conducting two steps, which are the pseudo label updating with the developed quality-aware triplet memory bank and the model training with curriculum data augmentation. These specific designs for 3D object detection enable the detector to be trained with consistent and high-quality pseudo labels and to avoid overfitting to the large number of easy examples in pseudo labeled data. Our ST3D achieves state-of-the-art performance on all evaluated datasets and even surpasses fully supervised results on KITTI 3D object detection benchmark. Code will be available at https://github.com/CVMI-Lab/ST3D.

</details>

### Center-Based 3D Object Detection and Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.html)
- **作者**: Tianwei Yin, Xingyi Zhou, Philipp Krähenbühl
- **🏷️ 机构**: UT Austin
- **会议**: CVPR 2021
- **摘要（中）**: 针对3D目标检测和跟踪中中心点表示的有效性问题，提出基于中心的3D检测和跟踪方法。方法利用中心点作为关键表示，简化检测流程并联合跟踪。相比基于锚框的方法，中心点方法更简洁高效。实验在多个数据集上验证了有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper proposes a center-based approach for 3D object detection and tracking, using center points as key representations to simplify the pipeline and enable joint tracking. It offers a more efficient alternative to anchor-based methods. The effectiveness is demonstrated on multiple datasets, though specific metrics are not provided in the abstract.
- **核心贡献**: 提出基于中心的3D检测和跟踪方法。
- **创新点**: 利用中心点简化检测流程并联合跟踪。
- **结果**: 在多个数据集上验证有效性，但摘要未给出具体数据。

### SRDAN: Scale-Aware and Range-Aware Domain Adaptation Network for Cross-Dataset 3D Object Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_SRDAN_Scale-Aware_and_Range-Aware_Domain_Adaptation_Network_for_Cross-Dataset_3D_CVPR_2021_paper.html) · 📚 被引 49
- **作者**: Weichen Zhang, Wen Li, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对跨数据集3D目标检测中因传感器配置、场景分布差异导致的域偏移问题。②提出尺度感知和距离感知的域适应网络（SRDAN），通过对齐不同尺度和距离下的特征分布来提升泛化能力。③相比现有域适应方法，显式建模了尺度与距离对域偏移的影响，增强了特征对齐的针对性。④在跨数据集基准上取得了显著的性能提升，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses domain shift in cross-dataset 3D object detection caused by sensor and scene differences. It proposes a scale-aware and range-aware domain adaptation network (SRDAN) that aligns feature distributions across scales and ranges. The method improves generalization over existing approaches, though specific quantitative gains are not detailed in the abstract.
- **核心贡献**: 提出尺度与距离感知的域适应网络，用于跨数据集3D检测。
- **创新点**: 显式建模尺度与距离对域偏移的影响。
- **结果**: 在跨数据集基准上性能提升，具体数值未给出。

### Monocular 3D Object Detection: An Extrinsic Parameter Free Approach. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2106.15796](https://arxiv.org/abs/2106.15796) · 📚 被引 86
- **作者**: Yunsong Zhou, Yuan He, Hongzi Zhu, Cheng Wang, Hongyang Li, Qinhong Jiang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2021
- **摘要（中）**: ①针对单目3D检测中相机外参变化（如路面颠簸）导致检测性能下降的问题。②提出一种无需外参的方法，通过检测消失点和水平线变化预测相机外参，并在潜在空间设计转换器矫正扰动特征。③相比现有方法忽略相机位姿信息，本方法显式建模外参扰动，提升实际场景鲁棒性。④在颠簸和不平路面等真实场景中，性能优于现有单目检测器。
- **摘要（英）**: This work tackles the sensitivity of monocular 3D detection to camera extrinsic variations caused by road unevenness. It predicts extrinsics via vanishing point and horizon detection, and rectifies perturbed features in latent space. The method outperforms existing detectors in realistic challenging scenarios like potholed roads.
- **核心贡献**: 提出免外参的单目3D检测框架，提升实际场景鲁棒性。
- **创新点**: 通过消失点和水平线预测外参并矫正特征。
- **结果**: 在真实颠簸场景中性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important task in autonomous driving. It can be easily intractable where there exists ego-car pose change w.r.t. ground plane. This is common due to the slight fluctuation of road smoothness and slope. Due to the lack of insight in industrial application, existing methods on open datasets neglect the camera pose information, which inevitably results in the detector being susceptible to camera extrinsic parameters. The perturbation of objects is very popular in most autonomous driving cases for industrial products. To this end, we propose a novel method to capture camera pose to formulate the detector free from extrinsic perturbation. Specifically, the proposed framework predicts camera extrinsic parameters by detecting vanishing point and horizon change. A converter is designed to rectify perturbative features in the latent space. By doing so, our 3D detector works independent of the extrinsic parameter variations and produces accurate results in realistic cases, e.g., potholed and uneven roads, where almost all existing monocular detectors fail to handle. Experiments demonstrate our method yields the best performance compared with the other state-of-the-arts by a large margin on both KITTI 3D and nuScenes datasets.

</details>

### VoxelContext-Net: An Octree Based Framework for Point Cloud Compression. **⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2105.02158](https://arxiv.org/abs/2105.02158) · 📚 被引 177
- **作者**: Zizheng Que, Guo Lu, Dong Xu
- **🏷️ 机构**: Beihang University, Beijing Institute of Technology, University of Sydney
- **会议**: CVPR 2021
- **摘要（中）**: ①针对点云压缩问题，提出基于八叉树的框架VoxelContext-Net。②利用八叉树结构进行上下文建模，实现高效点云压缩。③相比传统方法，结合深度学习与八叉树提升压缩率。④摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses point cloud compression using an octree-based framework, VoxelContext-Net. It leverages octree structure for context modeling to achieve efficient compression. The abstract lacks specific performance metrics.
- **核心贡献**: 提出基于八叉树的点云压缩框架。
- **创新点**: 结合八叉树与深度学习进行压缩。
- **结果**: 未提供具体数据。

### Objects Are Different: Flexible Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2104.02323](https://arxiv.org/abs/2104.02323) · 📚 被引 296
- **作者**: Yunpeng Zhang, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology,China Department of Automation,China
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目3D检测中截断物体性能受限的问题，提出MonoFlex，一种灵活框架，显式解耦截断物体并自适应组合深度估计方法。该方法通过特征图边缘解耦预测长尾截断物体，并将深度估计建模为直接回归和关键点求解的不确定性引导集成。在KITTI测试集上，中等难度相对提升27%，困难难度提升30%，同时保持实时效率。
- **摘要（英）**: MonoFlex addresses limited performance on truncated objects in monocular 3D detection by decoupling edge features and adaptively ensembling depth estimation methods. It uses uncertainty-guided combination of direct regression and keypoint-based solutions, achieving 27% and 30% relative improvements on moderate and hard KITTI levels with real-time efficiency.
- **核心贡献**: 提出解耦截断物体和自适应深度集成的单目3D检测框架。
- **创新点**: 不确定性引导的深度估计集成与边缘特征解耦。
- **结果**: 在KITTI上中等和困难难度分别提升27%和30%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The precise localization of 3D objects from a single image without depth information is a highly challenging problem. Most existing methods adopt the same approach for all objects regardless of their diverse distributions, leading to limited performance for truncated objects. In this paper, we propose a flexible framework for monocular 3D object detection which explicitly decouples the truncated objects and adaptively combines multiple approaches for object depth estimation. Specifically, we decouple the edge of the feature map for predicting long-tail truncated objects so that the optimization of normal objects is not influenced. Furthermore, we formulate the object depth estimation as an uncertainty-guided ensemble of directly regressed object depth and solved depths from different groups of keypoints. Experiments demonstrate that our method outperforms the state-of-the-art method by relatively 27\% for the moderate level and 30\% for the hard level in the test set of KITTI benchmark while maintaining real-time efficiency. Code will be available at \url{https://github.com/zhangyp15/MonoFlex}.

</details>

### Categorical Depth Distribution Network for Monocular 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2103.01100](https://arxiv.org/abs/2103.01100) · 📚 被引 517
- **作者**: Cody Reading, Ali Harakeh, Julia Chae, Steven L. Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对单目3D检测中深度估计不准确导致检测性能受限的问题。②提出CaDDN，通过预测每个像素的类别深度分布，将上下文特征投影到3D空间，并结合BEV投影和单阶段检测器。③相比直接估计深度的方法，CaDDN利用分布建模提高了深度精度。④在KITTI基准上排名第一，并首次在Waymo上提供单目3D检测结果。
- **摘要（英）**: This paper addresses the depth inaccuracy issue in monocular 3D detection. It proposes CaDDN, which predicts categorical depth distributions per pixel to project features into 3D space, combined with BEV projection and a single-stage detector. Compared to direct depth estimation, CaDDN improves depth accuracy via distribution modeling. It ranks 1st on KITTI and provides the first monocular 3D detection results on Waymo.
- **核心贡献**: 提出类别深度分布网络，实现端到端的单目3D检测。
- **创新点**: 利用深度分布而非点估计来投影特征。
- **结果**: 在KITTI上排名第一，并首次在Waymo上取得结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is a key problem for autonomous vehicles, as it provides a solution with simple configuration compared to typical multi-sensor systems. The main challenge in monocular 3D detection lies in accurately predicting object depth, which must be inferred from object and scene cues due to the lack of direct range measurement. Many methods attempt to directly estimate depth to assist in 3D detection, but show limited performance as a result of depth inaccuracy. Our proposed solution, Categorical Depth Distribution Network (CaDDN), uses a predicted categorical depth distribution for each pixel to project rich contextual feature information to the appropriate depth interval in 3D space. We then use the computationally efficient bird's-eye-view projection and single-stage detector to produce the final output bounding boxes. We design CaDDN as a fully differentiable end-to-end approach for joint depth estimation and object detection. We validate our approach on the KITTI 3D object detection benchmark, where we rank 1st among published monocular methods. We also provide the first monocular 3D detection results on the newly released Waymo Open Dataset. We provide a code release for CaDDN which is made available.

</details>

### LiDAR R-CNN: An Efficient and Universal 3D Object Detector. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2103.15297](https://arxiv.org/abs/2103.15297) · 📚 被引 223
- **作者**: Zhichao Li, Feng Wang, Naiyan Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对现有3D检测器第二阶段细化中直接应用PointNet导致特征忽略提议框尺寸的问题，提出LiDAR R-CNN通用第二阶段检测器。该方法分析问题根源，提出多种补救措施（如点云池化、尺寸感知特征），显著提升性能。在Waymo和KITTI数据集上基于PointPillars变体实现新SOTA，且计算开销小。
- **摘要（英）**: This paper addresses the overlooked issue in second-stage 3D detection where naively applying PointNet makes features ignore proposal sizes. It proposes LiDAR R-CNN, a universal second-stage detector with several remedies (e.g., point cloud pooling, size-aware features), significantly improving performance. On Waymo and KITTI, it achieves new state-of-the-art results based on a PointPillars variant with minor computational cost.
- **核心贡献**: 提出LiDAR R-CNN通用第二阶段检测器，解决PointNet特征忽略提议尺寸问题。
- **创新点**: 设计尺寸感知的点云特征提取方法，提升细化精度。
- **结果**: 在Waymo和KITTI上取得SOTA结果，且开销小。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D detection in point cloud is essential in the perception system of autonomous driving. In this paper, we present LiDAR R-CNN, a second stage detector that can generally improve any existing 3D detector. To fulfill the real-time and high precision requirement in practice, we resort to point-based approach other than the popular voxel-based approach. However, we find an overlooked issue in previous work: Naively applying point-based methods like PointNet could make the learned features ignore the size of proposals. To this end, we analyze this problem in detail and propose several methods to remedy it, which bring significant performance improvement. Comprehensive experimental results on real-world datasets like Waymo Open Dataset (WOD) and KITTI dataset with various popular detectors demonstrate the universality and superiority of our LiDAR R-CNN. In particular, based on one variant of PointPillars, our method could achieve new state-of-the-art results with minor cost. Codes will be released at https://github.com/tusimple/LiDAR_RCNN .

</details>

### Exploring Geometry-aware Contrast and Clustering Harmonization for Self-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00328)
- **作者**: Hanxue Liang, Chenhan Jiang, Dapeng Feng, Xin Chen, Hang Xu, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Geometry Uncertainty Projection Network for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00310)
- **作者**: Yan Lu, Xinzhu Ma, Lei Yang, Tianzhu Zhang, Yating Liu, Qi Chu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Voxel Transformer for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00315)
- **作者**: Jiageng Mao, Yujing Xue, Minzhe Niu, Haoyue Bai, Jiashi Feng, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Improving 3D Object Detection with Channel-wise Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00274)
- **作者**: Hualian Sheng, Sijia Cai, Yuan Liu, Bing Deng, Jianqiang Huang, Xian-Sheng Hua et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### VENet: Voting Enhancement Network for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00369)
- **作者**: Qian Xie, Yu-Kun Lai, Jing Wu, Zhoutao Wang, Dening Lu, Mingqiang Wei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### The Devil is in the Task: Exploiting Reciprocal Appearance-Localization Features for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00271)
- **作者**: Zhikang Zou, Xiaoqing Ye, Liang Du, Xianhui Cheng, Xiao Tan, Li Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### RPVNet: A Deep and Efficient Range-Point-Voxel Fusion Network for LiDAR Point Cloud Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01572)
- **作者**: Jianyun Xu, Ruixiang Zhang, Jian Dou, Yushi Zhu, Jie Sun, Shiliang Pu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Object DGCNN: 3D Object Detection using Dynamic Graphs.
- **链接**: [arXiv:2110.06923](https://arxiv.org/abs/2110.06923)
- **作者**: Yue Wang, Justin M. Solomon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection often involves complicated training and testing pipelines, which require substantial domain knowledge about individual datasets. Inspired by recent non-maximum suppression-free 2D object detection models, we propose a 3D object detection architecture on point clouds. Our method models 3D object detection as message passing on a dynamic graph, generalizing the DGCNN framework to predict a set of objects. In our construction, we remove the necessity of post-processing via object confidence aggregation or non-maximum suppression. To facilitate object detection from sparse point clouds, we also propose a set-to-set distillation approach customized to 3D detection. This approach aligns the outputs of the teacher model and the student model in a permutation-invariant fashion, significantly simplifying knowledge distillation for the 3D detection task. Our method achieves state-of-the-art performance on autonomous driving benchmarks. We also provide abundant analysis of the detection model and distillation framework.

</details>

### Revisiting 3D Object Detection From an Egocentric Perspective.
- **链接**: [arXiv:2112.07787](https://arxiv.org/abs/2112.07787)
- **作者**: Boyang Deng, Charles R. Qi, Mahyar Najibi, Thomas A. Funkhouser, Yin Zhou, Dragomir Anguelov
- **🏷️ 机构**: Waymo
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a key module for safety-critical robotics applications such as autonomous driving. For these applications, we care most about how the detections affect the ego-agent's behavior and safety (the egocentric perspective). Intuitively, we seek more accurate descriptions of object geometry when it's more likely to interfere with the ego-agent's motion trajectory. However, current detection metrics, based on box Intersection-over-Union (IoU), are object-centric and aren't designed to capture the spatio-temporal relationship between objects and the ego-agent. To address this issue, we propose a new egocentric measure to evaluate 3D object detection, namely Support Distance Error (SDE). Our analysis based on SDE reveals that the egocentric detection quality is bounded by the coarse geometry of the bounding boxes. Given the insight that SDE would benefit from more accurate geometry descriptions, we propose to represent objects as amodal contours, specifically amodal star-shaped polygons, and devise a simple model, StarPoly, to predict such contours. Our experiments on the large-scale Waymo Open Dataset show that SDE better reflects the impact of detection quality on the ego-agent's safety compared to IoU; and the estimated contours from StarPoly consistently improve the egocentric detection quality over recent 3D object detectors.

</details>

### Voxel-based 3D Detection and Reconstruction of Multiple Objects from a Single Image.
- **链接**: [arXiv:2111.03098](https://arxiv.org/abs/2111.03098)
- **作者**: Feng Liu, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inferring 3D locations and shapes of multiple objects from a single 2D image is a long-standing objective of computer vision. Most of the existing works either predict one of these 3D properties or focus on solving both for a single object. One fundamental challenge lies in how to learn an effective representation of the image that is well-suited for 3D detection and reconstruction. In this work, we propose to learn a regular grid of 3D voxel features from the input image which is aligned with 3D scene space via a 3D feature lifting operator. Based on the 3D voxel features, our novel CenterNet-3D detection head formulates the 3D detection as keypoint detection in the 3D space. Moreover, we devise an efficient coarse-to-fine reconstruction module, including coarse-level voxelization and a novel local PCA-SDF shape representation, which enables fine detail reconstruction and one order of magnitude faster inference than prior methods. With complementary supervision from both 3D detection and reconstruction, one enables the 3D voxel features to be geometry and context preserving, benefiting both tasks.The effectiveness of our approach is demonstrated through 3D detection and reconstruction in single object and multiple object scenarios.

</details>

### Progressive Coordinate Transforms for Monocular 3D Object Detection.
- **链接**: [arXiv:2108.05793](https://arxiv.org/abs/2108.05793)
- **作者**: Li Wang, Li Zhang, Yi Zhu, Zhi Zhang, Tong He, Mu Li et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab, AWS / CMU
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recognizing and localizing objects in the 3D space is a crucial ability for an AI agent to perceive its surrounding environment. While significant progress has been achieved with expensive LiDAR point clouds, it poses a great challenge for 3D object detection given only a monocular image. While there exist different alternatives for tackling this problem, it is found that they are either equipped with heavy networks to fuse RGB and depth information or empirically ineffective to process millions of pseudo-LiDAR points. With in-depth examination, we realize that these limitations are rooted in inaccurate object localization. In this paper, we propose a novel and lightweight approach, dubbed {\em Progressive Coordinate Transforms} (PCT) to facilitate learning coordinate representations. Specifically, a localization boosting mechanism with confidence-aware loss is introduced to progressively refine the localization prediction. In addition, semantic image representation is also exploited to compensate for the usage of patch proposals. Despite being lightweight and simple, our strategy leads to superior improvements on the KITTI and Waymo Open Dataset monocular 3D detection benchmarks. At the same time, our proposed PCT shows great generalization to most coordinate-based 3D detection frameworks. The code is available at: https://github.com/amazon-research/progressive-coordinate-transforms .

</details>

### Learning Transferable Features for Point Cloud Detection via 3D Contrastive Co-training.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b3b25a26a0828ea5d48d8f8aa0d6f9af-Abstract.html)
- **作者**: Yihan Zeng, Chunwei Wang, Yunbo Wang, Hang Xu, Chaoqiang Ye, Zhen Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Multimodal Virtual Point 3D Detection.
- **链接**: [arXiv:2111.06881](https://arxiv.org/abs/2111.06881)
- **作者**: Tianwei Yin, Xingyi Zhou, Philipp Krähenbühl
- **🏷️ 机构**: UT Austin
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Lidar-based sensing drives current autonomous vehicles. Despite rapid progress, current Lidar sensors still lag two decades behind traditional color cameras in terms of resolution and cost. For autonomous driving, this means that large objects close to the sensors are easily visible, but far-away or small objects comprise only one measurement or two. This is an issue, especially when these objects turn out to be driving hazards. On the other hand, these same objects are clearly visible in onboard RGB sensors. In this work, we present an approach to seamlessly fuse RGB sensors into Lidar-based 3D recognition. Our approach takes a set of 2D detections to generate dense 3D virtual points to augment an otherwise sparse 3D point cloud. These virtual points naturally integrate into any standard Lidar-based 3D detectors along with regular Lidar measurements. The resulting multi-modal detector is simple and effective. Experimental results on the large-scale nuScenes dataset show that our framework improves a strong CenterPoint baseline by a significant 6.6 mAP, and outperforms competing fusion approaches. Code and more visualizations are available at https://tianweiy.github.io/mvp/

</details>

## 跨领域论文（完整笔记在其他领域）

- 3DIoUMatch: Leveraging IoU Prediction for Semi-Supervised 3D Object Detection. → [object-detection](../object-detection/Guideline%202021.md)
- Unsupervised Object Detection With LIDAR Clues. → [object-detection](../object-detection/Guideline%202021.md)
- 3D-MAN: 3D Multi-Frame Attention Network for Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- SE-SSD: Self-Ensembling Single-Stage Object Detector From Point Cloud. → [bev](../bev/Guideline%202021.md)
- Self-Supervised Pillar Motion Learning for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
- 3D Siamese Voxel-to-BEV Tracker for Sparse Point Clouds. → [bev](../bev/Guideline%202021.md)

<!-- COMPLETE v1 papers=48 -->
