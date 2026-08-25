# 3D Detection — 2024 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 26 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors.
- **链接**: [arXiv:2403.06093](https://arxiv.org/abs/2403.06093) · [代码](https://github.com/nullmax-vision/QAF2D)
- **作者**: Haoxuanye Ji, Pengpeng Liang, Erkang Cheng
- **🏷️ 机构**: Nullmax, School of Computer and Artificial Intelligence, Zhengzhou University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multi-camera-based 3D object detection has made notable progress in the past several years. However, we observe that there are cases (e.g. faraway regions) in which popular 2D object detectors are more reliable than state-of-the-art 3D detectors. In this paper, to improve the performance of query-based 3D object detectors, we present a novel query generating approach termed QAF2D, which infers 3D query anchors from 2D detection results. A 2D bounding box of an object in an image is lifted to a set of 3D anchors by associating each sampled point within the box with depth, yaw angle, and size candidates. Then, the validity of each 3D anchor is verified by comparing its projection in the image with its corresponding 2D box, and only valid anchors are kept and used to construct queries. The class information of the 2D bounding box associated with each query is also utilized to match the predicted boxes with ground truth for the set-based loss. The image feature extraction backbone is shared between the 3D detector and 2D detector by adding a small number of prompt parameters. We integrate QAF2D into three popular query-based 3D object detectors and carry out comprehensive evaluations on the nuScenes dataset. The largest improvement that QAF2D can bring about on the nuScenes validation subset is $2.3\%$ NDS and $2.7\%$ mAP. Code is available at https://github.com/nullmax-vision/QAF2D.

### SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00978)
- **作者**: Abhinav Kumar, Yuliang Guo, Xinyu Huang, Liu Ren, Xiaoming Liu
- **🏷️ 机构**: Michigan State University, Bosch Research North America, Bosch Center for AI
- **会议**: CVPR 2024

### Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01436)
- **作者**: Yujeong Chae, Hyeonseong Kim, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2024

### Weak-to-Strong 3D Object Detection with X-Ray Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01426)
- **作者**: Alexander Gambashidze, Aleksandr Dadukin, Maksim Golyadkin, Maria Razzhivina, Ilya Makarov
- **🏷️ 机构**: Artificial Intelligence Research Institute, HSE University
- **会议**: CVPR 2024

### PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01415) · 📚 被引 23
- **作者**: Kuan-Chih Huang, Weijie Lyu, Ming-Hsuan Yang, Yi-Hsuan Tsai
- **🏷️ 机构**: University of California,Merced, Google
- **会议**: CVPR 2024

### GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection.
- **链接**: [arXiv:2411.00340](https://arxiv.org/abs/2411.00340)
- **作者**: Xiaotian Li, Baojie Fan, Jiandong Tian, Huijie Fan
- **🏷️ 机构**: Nanjing University of Posts and Telecommunications, Shenyang Institute of Automation Chinese Academy of Science
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent years have witnessed the remarkable progress of 3D multi-modality object detection methods based on the Bird's-Eye-View (BEV) perspective. However, most of them overlook the complementary interaction and guidance between LiDAR and camera. In this work, we propose a novel multi-modality 3D objection detection method, named GAFusion, with LiDAR-guided global interaction and adaptive fusion. Specifically, we introduce sparse depth guidance (SDG) and LiDAR occupancy guidance (LOG) to generate 3D features with sufficient depth information. In the following, LiDAR-guided adaptive fusion transformer (LGAFT) is developed to adaptively enhance the interaction of different modal BEV features from a global perspective. Meanwhile, additional downsampling with sparse height compression and multi-scale dual-path transformer (MSDPT) are designed to enlarge the receptive fields of different modal features. Finally, a temporal fusion module is introduced to aggregate features from previous frames. GAFusion achieves state-of-the-art 3D object detection results with 73.6$\%$ mAP and 74.9$\%$ NDS on the nuScenes test set.

### BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01901)
- **作者**: Zhenxin Li, Shiyi Lan, José M. Álvarez, Zuxuan Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### UniMODE: Unified Monocular 3D Object Detection.
- **链接**: [arXiv:2402.18573](https://arxiv.org/abs/2402.18573)
- **作者**: Zhuoling Li, Xiaogang Xu, Ser-Nam Lim, Hengshuang Zhao
- **🏷️ 机构**: IHKU, CUHK, UCF
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Realizing unified 3D object detection, including both indoor and outdoor scenes, holds great importance in applications like robot navigation. However, involving various scenarios of data to train models poses challenges due to their significantly distinct characteristics, \eg, diverse geometry properties and heterogeneous domain distributions. In this work, we propose to address the challenges from two perspectives, the algorithm perspective and data perspective. In terms of the algorithm perspective, we first build a monocular 3D object detector based on the bird's-eye-view (BEV) detection paradigm, where the explicit feature projection is beneficial to addressing the geometry learning ambiguity. In this detector, we split the classical BEV detection architecture into two stages and propose an uneven BEV grid design to handle the convergence instability caused by geometry difference between scenarios. Besides, we develop a sparse BEV feature projection strategy to reduce the computational cost and a unified domain alignment method to handle heterogeneous domains. From the data perspective, we propose to incorporate depth information to improve training robustness. Specifically, we build the first unified multi-modal 3D object detection benchmark MM-Omni3D and extend the aforementioned monocular detector to its multi-modal version, which is the first unified multi-modal 3D object detector. We name the designed monocular and multi-modal detectors as UniMODE and MM-UniMODE, respectively. The experimental results reveal several insightful findings highlighting the benefits of multi-modal data and confirm the effectiveness of all the proposed strategies.

### RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01414)
- **作者**: Zhiwei Lin, Zhe Liu, Zhongyu Xia, Xinhao Wang, Yongtao Wang, Shengxiang Qi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01643)
- **作者**: Zihua Liu, Hiroki Sakuma, Masatoshi Okutomi
- **🏷️ 机构**: Tokyo Institute of Technology, T2 Inc.
- **会议**: CVPR 2024

### Multi-View Attentive Contextualization for Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01579)
- **作者**: Xianpeng Liu, Ce Zheng, Ming Qian, Nan Xue, Chen Chen, Zhebin Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Learning Occupancy for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00979)
- **作者**: Liang Peng, Junkai Xu, Haoran Cheng, Zheng Yang, Xiaopei Wu, Wei Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### MonoDiff: Monocular 3D Object Detection and Pose Estimation with Diffusion Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01014)
- **作者**: Yasiru Ranasinghe, Deepti Hegde, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University,Baltimore,USA
- **会议**: CVPR 2024

### BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01394)
- **作者**: Wenjie Wang, Yehao Lu, Guangcong Zheng, Shuigen Zhan, Xiaoqing Ye, Zichang Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Commonsense Prototype for Outdoor Unsupervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01418)
- **作者**: Hai Wu, Shijia Zhao, Xun Huang, Chenglu Wen, Xin Li, Cheng Wang
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities, Texas A&#x0026;M University,Section of Visual Computing and Interactive Media
- **会议**: CVPR 2024

### HINTED: Hard Instance Enhanced Detector with Mixed-Density Feature Fusion for Sparsely-Supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01451)
- **作者**: Qiming Xia, Wei Ye, Hai Wu, Shijia Zhao, Leyuan Xing, Xun Huang et al.
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities,Xiamen,China, Texas A&#x0026;M University,Section of Visual Computing and Interactive Media,Texas,USA
- **会议**: CVPR 2024

### 3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features.
- **链接**: [arXiv:2311.04391](https://arxiv.org/abs/2311.04391) · 📚 被引 19
- **作者**: Chenfeng Xu, Huan Ling, Sanja Fidler, Or Litany
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present 3DiffTection, a state-of-the-art method for 3D object detection from single images, leveraging features from a 3D-aware diffusion model. Annotating large-scale image data for 3D detection is resource-intensive and time-consuming. Recently, pretrained large image diffusion models have become prominent as effective feature extractors for 2D perception tasks. However, these features are initially trained on paired text and image data, which are not optimized for 3D tasks, and often exhibit a domain gap when applied to the target data. Our approach bridges these gaps through two specialized tuning strategies: geometric and semantic. For geometric tuning, we fine-tune a diffusion model to perform novel view synthesis conditioned on a single image, by introducing a novel epipolar warp operator. This task meets two essential criteria: the necessity for 3D awareness and reliance solely on posed image data, which are readily available (e.g., from videos) and does not require manual annotation. For semantic refinement, we further train the model on target data with detection supervision. Both tuning phases employ ControlNet to preserve the integrity of the original feature capabilities. In the final step, we harness these enhanced capabilities to conduct a test-time prediction ensemble across multiple virtual viewpoints. Through our methodology, we obtain 3D-aware features that are tailored for 3D detection and excel in identifying cross-view point correspondences. Consequently, our model emerges as a powerful 3D detector, substantially surpassing previous benchmarks, e.g., Cube-RCNN, a precedent in single-view 3D detection by 9.43\% in AP3D on the Omni3D-ARkitscene dataset. Furthermore, 3DiffTection showcases robust data efficiency and generalization to cross-domain data.

### MonoCD: Monocular 3D Object Detection with Complementary Depths.
- **链接**: [arXiv:2404.03181](https://arxiv.org/abs/2404.03181) · [代码](https://github.com/elvintanhust/MonoCD)
- **作者**: Longfei Yan, Pei Yan, Shengzhou Xiong, Xuanyu Xiang, Yihua Tan
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,Hubei Engineering Research Center of Machine Vision and Intelligent Systems,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Monocular 3D object detection has attracted widespread attention due to its potential to accurately obtain object 3D localization from a single image at a low cost. Depth estimation is an essential but challenging subtask of monocular 3D object detection due to the ill-posedness of 2D to 3D mapping. Many methods explore multiple local depth clues such as object heights and keypoints and then formulate the object depth estimation as an ensemble of multiple depth predictions to mitigate the insufficiency of single-depth information. However, the errors of existing multiple depths tend to have the same sign, which hinders them from neutralizing each other and limits the overall accuracy of combined depth. To alleviate this problem, we propose to increase the complementarity of depths with two novel designs. First, we add a new depth prediction branch named complementary depth that utilizes global and efficient depth clues from the entire image rather than the local clues to reduce the correlation of depth predictions. Second, we propose to fully exploit the geometric relations between multiple depth clues to achieve complementarity in form. Benefiting from these designs, our method achieves higher complementarity. Experiments on the KITTI benchmark demonstrate that our method achieves state-of-the-art performance without introducing extra data. In addition, complementary depth can also be a lightweight and plug-and-play module to boost multiple existing monocular 3d object detectors. Code is available at https://github.com/elvintanhust/MonoCD.

### Improving Distant 3D Object Detection Using 2D Box Supervision.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01407) · 📚 被引 9
- **作者**: Zetong Yang, Zhiding Yu, Christopher B. Choy, Renhao Wang, Anima Anandkumar, José M. Álvarez
- **🏷️ 机构**: CUHK, NVIDIA, UC Berkeley
- **会议**: CVPR 2024

### IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01412)
- **作者**: Junbo Yin, Jianbing Shen, Runnan Chen, Wei Li, Ruigang Yang, Pascal Frossard et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Pseudo Label Refinery for Unsupervised Domain Adaptation on Cross-Dataset 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01448)
- **作者**: Zhanwei Zhang, Minghao Chen, Shuai Xiao, Liang Peng, Hengjia Li, Binbin Lin et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, School of Computer Sciene and Technology, Hangzhou Dianzi University, Alibaba Group
- **会议**: CVPR 2024

### SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection.
- **链接**: [arXiv:2403.05817](https://arxiv.org/abs/2403.05817) · [代码](https://github.com/zhanggang001/HEDNet) · 📚 被引 78
- **作者**: Gang Zhang, Junnan Chen, Guohuan Gao, Jianmin Li, Si Liu, Xiaolin Hu
- **🏷️ 机构**: Institute for AI, BNRist, Tsinghua University,Department of Computer Science and Technology, Huazhong University of Science and Technology, Beijing Institute of Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > LiDAR-based 3D object detection plays an essential role in autonomous driving. Existing high-performing 3D object detectors usually build dense feature maps in the backbone network and prediction head. However, the computational costs introduced by the dense feature maps grow quadratically as the perception range increases, making these models hard to scale up to long-range detection. Some recent works have attempted to construct fully sparse detectors to solve this issue; nevertheless, the resulting models either rely on a complex multi-stage pipeline or exhibit inferior performance. In this work, we propose SAFDNet, a straightforward yet highly effective architecture, tailored for fully sparse 3D object detection. In SAFDNet, an adaptive feature diffusion strategy is designed to address the center feature missing problem. We conducted extensive experiments on Waymo Open, nuScenes, and Argoverse2 datasets. SAFDNet performed slightly better than the previous SOTA on the first two datasets but much better on the last dataset, which features long-range detection, verifying the efficacy of SAFDNet in scenarios where long-range detection is required. Notably, on Argoverse2, SAFDNet surpassed the previous best hybrid detector HEDNet by 2.6% mAP while being 2.1x faster, and yielded 2.1% mAP gains over the previous best sparse detector FSDv2 while being 1.3x faster. The code will be available at https://github.com/zhanggang001/HEDNet.

### CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01452)
- **作者**: Haonan Zhang, Longjun Liu, Yuqi Huang, Zhao Yang, Xinyu Lei, Bihan Wen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Decoupled Pseudo-Labeling for Semi-Supervised Monocular 3D Object Detection.
- **链接**: [arXiv:2403.17387](https://arxiv.org/abs/2403.17387)
- **作者**: Jiacheng Zhang, Jiaming Li, Xiangru Lin, Wei Zhang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University,Guangzhou,China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We delve into pseudo-labeling for semi-supervised monocular 3D object detection (SSM3OD) and discover two primary issues: a misalignment between the prediction quality of 3D and 2D attributes and the tendency of depth supervision derived from pseudo-labels to be noisy, leading to significant optimization conflicts with other reliable forms of supervision. We introduce a novel decoupled pseudo-labeling (DPL) approach for SSM3OD. Our approach features a Decoupled Pseudo-label Generation (DPG) module, designed to efficiently generate pseudo-labels by separately processing 2D and 3D attributes. This module incorporates a unique homography-based method for identifying dependable pseudo-labels in BEV space, specifically for 3D attributes. Additionally, we present a DepthGradient Projection (DGP) module to mitigate optimization conflicts caused by noisy depth supervision of pseudo-labels, effectively decoupling the depth gradient and removing conflicting gradients. This dual decoupling strategy-at both the pseudo-label generation and gradient levels-significantly improves the utilization of pseudo-labels in SSM3OD. Our comprehensive experiments on the KITTI benchmark demonstrate the superiority of our method over existing approaches.

### Prompt3D: Random Prompt Assisted Weakly-Supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02649)
- **作者**: Xiaohong Zhang, Huisheng Ye, Jingwen Li, Qinyu Tang, Yuanqi Li, Yanwen Guo et al.
- **🏷️ 机构**: Nanjing University
- **会议**: CVPR 2024

### Three Pillars Improving Vision Foundation Model Distillation for Lidar.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02033)
- **作者**: Gilles Puy, Spyros Gidaris, Alexandre Boulch, Oriane Siméoni, Corentin Sautier, Patrick Pérez et al.
- **🏷️ 机构**: valeo.ai,Paris,France, Kyutai,Paris,France
- **会议**: CVPR 2024
