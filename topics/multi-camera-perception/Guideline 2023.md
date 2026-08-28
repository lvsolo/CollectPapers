# Multi-camera Perception — 2023 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 45 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MUVA: A New Large-Scale Benchmark for Multi-view Amodal Instance Segmentation in the Shopping Scenario.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02148) · 📚 被引 14
- **作者**: Zhixuan Li, Weining Ye, Juan R. Terven, Zachary Bennett, Ying Zheng, Tingting Jiang et al.
- **🏷️ 机构**: Peking University,National Engineering Research Center of Visual Technology, National Key Laboratory for Multimedia Information Processing, School of Computer Science,Beijing,China,100871, AiFi Inc.,California,United States,94010
- **会议**: ICCV 2023

### UniFusion: Unified Multi-view Fusion Transformer for Spatial-Temporal Representation in Bird's-Eye-View.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00798) · 📚 被引 50
- **作者**: Zequn Qin, Jingyu Chen, Chao Chen, Xiaozhi Chen, Xi Li
- **🏷️ 机构**: Zhejiang University,College of Computer Science &amp; Technology, DJI
- **会议**: ICCV 2023

### AIDE: A Vision-Driven Multi-View, Multi-Modal, Multi-Tasking Dataset for Assistive Driving Perception.
- **链接**: [arXiv:2307.13933](https://arxiv.org/abs/2307.13933) · 📚 被引 67
- **作者**: Dingkang Yang, Shuai Huang, Zhi Xu, Zhenpeng Li, Shunli Wang, Mingcheng Li et al.
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University
- **会议**: ICCV 2023

### Cross-view Topology Based Consistent and Complementary Information for Deep Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01781) · 📚 被引 32
- **作者**: Zhibin Dong, Siwei Wang, Jiaqi Jin, Xinwang Liu, En Zhu
- **🏷️ 机构**: National University of Defense Technology,School of Computer,Changsha,China, Intelligent Game and Decision Lab,Beijing,China
- **会议**: ICCV 2023

### ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01410)
- **作者**: Zoey Guo, Yiwen Tang, Ray Zhang, Dong Wang, Zhigang Wang, Bin Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Replay: Multi-modal Multi-view Acted Videos for Casual Holography.
- **链接**: [arXiv:2307.12067](https://arxiv.org/abs/2307.12067) · 📚 被引 7
- **作者**: Roman Shapovalov, Yanir Kleiman, Ignacio Rocco, David Novotný, Andrea Vedaldi, Changan Chen et al.
- **🏷️ 机构**: Meta
- **会议**: ICCV 2023

### Ray Conditioning: Trading Photo-consistency for Photo-realism in Multi-view Image Generation.
- **链接**: [arXiv:2304.13681](https://arxiv.org/abs/2304.13681) · 📚 被引 7
- **作者**: Eric Ming Chen, Sidhanth Holalkere, Ruyu Yan, Kai Zhang, Abe Davis
- **🏷️ 机构**: Cornell University, Adobe Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view image generation attracts particular attention these days due to its promising 3D-related applications, e.g., image viewpoint editing. Most existing methods follow a paradigm where a 3D representation is first synthesized, and then rendered into 2D images to ensure photo-consistency across viewpoints. However, such explicit bias for photo-consistency sacrifices photo-realism, causing geometry artifacts and loss of fine-scale details when these methods are applied to edit real images. To address this issue, we propose ray conditioning, a geometry-free alternative that relaxes the photo-consistency constraint. Our method generates multi-view images by conditioning a 2D GAN on a light field prior. With explicit viewpoint control, state-of-the-art photo-realism and identity consistency, our method is particularly suited for the viewpoint editing task.

</details>

### Multi-view Self-supervised Disentanglement for General Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01128)
- **作者**: Hao Chen, Chenyuan Qu, Yu Zhang, Chen Chen, Jianbo Jiao
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### TEMPO: Efficient Multi-View Pose Estimation, Tracking, and Forecasting.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01355) · 📚 被引 27
- **作者**: Rohan Choudhury, Kris M. Kitani, László A. Jeni
- **🏷️ 机构**: Carnegie Mellon University,Robotics Institute
- **会议**: ICCV 2023

### Multi-View Active Fine-Grained Visual Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00151) · 📚 被引 13
- **作者**: Ruoyi Du, Wenqing Yu, Heqing Wang, Ting-En Lin, Dongliang Chang, Zhanyu Ma
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,China
- **会议**: ICCV 2023

### Ref-NeuS: Ambiguity-Reduced Neural Implicit Surface Learning for Multi-View Reconstruction with Reflection.
- **链接**: [arXiv:2303.10840](https://arxiv.org/abs/2303.10840) · 📚 被引 54
- **作者**: Wenhang Ge, Tao Hu, Haoyu Zhao, Shu Liu, Ying-Cong Chen
- **🏷️ 机构**: HKUST(GZ), CUHK, SmartMore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural implicit surface learning has shown significant progress in multi-view 3D reconstruction, where an object is represented by multilayer perceptrons that provide continuous implicit surface representation and view-dependent radiance. However, current methods often fail to accurately reconstruct reflective surfaces, leading to severe ambiguity. To overcome this issue, we propose Ref-NeuS, which aims to reduce ambiguity by attenuating the effect of reflective surfaces. Specifically, we utilize an anomaly detector to estimate an explicit reflection score with the guidance of multi-view context to localize reflective surfaces. Afterward, we design a reflection-aware photometric loss that adaptively reduces ambiguity by modeling rendered color as a Gaussian distribution, with the reflection score representing the variance. We show that together with a reflection direction-dependent radiance, our model achieves high-quality surface reconstruction on reflective surfaces and outperforms the state-of-the-arts by a large margin. Besides, our model is also comparable on general surfaces.

</details>

### Anchor Structure Regularization Induced Multi-view Subspace Clustering via Enhanced Tensor Rank Minimization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01772) · 📚 被引 37
- **作者**: Jintian Ji, Songhe Feng
- **🏷️ 机构**: Beijing Jiaotong University,Key Laboratory of Big Data &amp; Artificial Intelligence in Transportation, Ministry of Education,Beijing,China,100044
- **会议**: ICCV 2023

### Coordinate Quantized Neural Implicit Representations for Multi-view Reconstruction.
- **链接**: [arXiv:2308.11025](https://arxiv.org/abs/2308.11025) · [代码](https://github.com/MachinePerceptionLab/CQ-NIR) · 📚 被引 4
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **🏷️ 机构**: Wayne State University,Department of Computer Science,Detroit,USA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, huge progress has been made on learning neural implicit representations from multi-view images for 3D reconstruction. As an additional input complementing coordinates, using sinusoidal functions as positional encodings plays a key role in revealing high frequency details with coordinate-based neural networks. However, high frequency positional encodings make the optimization unstable, which results in noisy reconstructions and artifacts in empty space. To resolve this issue in a general sense, we introduce to learn neural implicit representations with quantized coordinates, which reduces the uncertainty and ambiguity in the field during optimization. Instead of continuous coordinates, we discretize continuous coordinates into discrete coordinates using nearest interpolation among quantized coordinates which are obtained by discretizing the field in an extremely high resolution. We use discrete coordinates and their positional encodings to learn implicit functions through volume rendering. This significantly reduces the variations in the sample space, and triggers more multi-view consistency constraints on intersections of rays from different views, which enables to infer implicit function in a more effective way. Our quantized coordinates do not bring any computational burden, and can seamlessly work upon the latest methods. Our evaluations under the widely used benchmarks show our superiority over the state-of-the-art. Our code is available at https://github.com/MachinePerceptionLab/CQ-NIR.

</details>

### Probabilistic Triangulation for Uncalibrated Multi-View 3D Human Pose Estimation.
- **链接**: [arXiv:2309.04756](https://arxiv.org/abs/2309.04756) · [代码](https://github.com/bymaths/probabilistic_triangulation) · 📚 被引 21
- **作者**: Boyuan Jiang, Lei Hu, Shihong Xia
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Computing Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D human pose estimation has been a long-standing challenge in computer vision and graphics, where multi-view methods have significantly progressed but are limited by the tedious calibration processes. Existing multi-view methods are restricted to fixed camera pose and therefore lack generalization ability. This paper presents a novel Probabilistic Triangulation module that can be embedded in a calibrated 3D human pose estimation method, generalizing it to uncalibration scenes. The key idea is to use a probability distribution to model the camera pose and iteratively update the distribution from 2D features instead of using camera pose. Specifically, We maintain a camera pose distribution and then iteratively update this distribution by computing the posterior probability of the camera pose through Monte Carlo sampling. This way, the gradients can be directly back-propagated from the 3D pose estimation to the 2D heatmap, enabling end-to-end training. Extensive experiments on Human3.6M and CMU Panoptic demonstrate that our method outperforms other uncalibration methods and achieves comparable results with state-of-the-art calibration methods. Thus, our method achieves a trade-off between estimation accuracy and generalizability. Our code is in https://github.com/bymaths/probabilistic_triangulation

</details>

### MHCN: A Hyperbolic Neural Network Model for Multi-view Hierarchical Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01515) · 📚 被引 12
- **作者**: Fangfei Lin, Bing Bai, Yiwen Guo, Hao Chen, Yazhou Ren, Zenglin Xu
- **🏷️ 机构**: University of Electronic Science and Technology of China,China, Tencent Security Big Data Lab,China, Independent Researcher
- **会议**: ICCV 2023

### GeoMIM: Towards Better 3D Knowledge Transfer via Masked Image Modeling for Multi-view 3D Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01635)
- **作者**: Jihao Liu, Tai Wang, Boxiao Liu, Qihang Zhang, Yu Liu, Hongsheng Li
- **🏷️ 机构**: SenseTime, CUHK
- **会议**: ICCV 2023

### When Epipolar Constraint Meets Non-local Operators in Multi-View Stereo.
- **链接**: [arXiv:2309.17218](https://arxiv.org/abs/2309.17218) · [代码](https://github.com/TQTQliu/ET-MVSNet) · 📚 被引 54
- **作者**: Tianqi Liu, Xinyi Ye, Weiyue Zhao, Zhiyu Pan, Min Shi, Zhiguo Cao
- **🏷️ 机构**: Huazhong University of Science and Technology,Key Laboratory of Image Processing and Intelligent Control,Ministry of Education; School of Artificial Intelligence and Automation,Wuhan,China,430074
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning-based multi-view stereo (MVS) method heavily relies on feature matching, which requires distinctive and descriptive representations. An effective solution is to apply non-local feature aggregation, e.g., Transformer. Albeit useful, these techniques introduce heavy computation overheads for MVS. Each pixel densely attends to the whole image. In contrast, we propose to constrain non-local feature augmentation within a pair of lines: each point only attends the corresponding pair of epipolar lines. Our idea takes inspiration from the classic epipolar geometry, which shows that one point with different depth hypotheses will be projected to the epipolar line on the other view. This constraint reduces the 2D search space into the epipolar line in stereo matching. Similarly, this suggests that the matching of MVS is to distinguish a series of points lying on the same line. Inspired by this point-to-line search, we devise a line-to-point non-local augmentation strategy. We first devise an optimized searching algorithm to split the 2D feature maps into epipolar line pairs. Then, an Epipolar Transformer (ET) performs non-local feature augmentation among epipolar line pairs. We incorporate the ET into a learning-based MVS baseline, named ET-MVSNet. ET-MVSNet achieves state-of-the-art reconstruction performance on both the DTU and Tanks-and-Temples benchmark with high efficiency. Code is available at https://github.com/TQTQliu/ET-MVSNet.

</details>

### Multi-view Spectral Polarization Propagation for Video Glass Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02122) · 📚 被引 7
- **作者**: Yu Qiao, Bo Dong, Ao Jin, Yu Fu, Seung-Hwan Baek, Felix Heide et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICCV 2023

### Hierarchical Prior Mining for Non-local Multi-View Stereo.
- **链接**: [arXiv:2303.09758](https://arxiv.org/abs/2303.09758)
- **作者**: Chunlin Ren, Qingshan Xu, Shikun Zhang, Jiaqi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a fundamental problem in computer vision, multi-view stereo (MVS) aims at recovering the 3D geometry of a target from a set of 2D images. Recent advances in MVS have shown that it is important to perceive non-local structured information for recovering geometry in low-textured areas. In this work, we propose a Hierarchical Prior Mining for Non-local Multi-View Stereo (HPM-MVS). The key characteristics are the following techniques that exploit non-local information to assist MVS: 1) A Non-local Extensible Sampling Pattern (NESP), which is able to adaptively change the size of sampled areas without becoming snared in locally optimal solutions. 2) A new approach to leverage non-local reliable points and construct a planar prior model based on K-Nearest Neighbor (KNN), to obtain potential hypotheses for the regions where prior construction is challenging. 3) A Hierarchical Prior Mining (HPM) framework, which is used to mine extensive non-local prior information at different scales to assist 3D model recovery, this strategy can achieve a considerable balance between the reconstruction of details and low-textured areas. Experimental results on the ETH3D and Tanks \& Temples have verified the superior performance and strong generalization capability of our method. Our code will be released.

</details>

### End2End Multi-View Feature Matching with Differentiable Pose Optimization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00050) · 📚 被引 23
- **作者**: Barbara Roessle, Matthias Nießner
- **🏷️ 机构**: Technical University of Munich
- **会议**: ICCV 2023

### Spectral Graphormer: Spectral Graph-based Transformer for Egocentric Two-Hand Reconstruction using Multi-View Color Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01348) · 📚 被引 6
- **作者**: Tze Ho Elden Tse, Franziska Mueller, Zhengyang Shen, Danhang Tang, Thabo Beeler, Mingsong Dou et al.
- **🏷️ 机构**: Google
- **会议**: ICCV 2023

### NeuS2: Fast Learning of Neural Implicit Surfaces for Multi-view Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00305) · 📚 被引 291
- **作者**: Yiming Wang, Qin Han, Marc Habermann, Kostas Daniilidis, Christian Theobalt, Lingjie Liu
- **🏷️ 机构**: University of Pennsylvania, Peking University, Peking University, Max Planck Institute for Informatics
- **会议**: ICCV 2023

### Mixed Neural Voxels for Fast Multi-view Video Synthesis.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01805) · 📚 被引 87
- **作者**: Feng Wang, Sinan Tan, Xinghang Li, Zeyue Tian, Yafei Song, Huaping Liu
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology(BNRist),Department of Computer Science and Technology, Hong Kong University of Science and Technology, Alibaba Group,XR Lab, DAMO Academy
- **会议**: ICCV 2023

### S-VolSDF: Sparse Multi-View Stereo Regularization of Neural Implicit Surfaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00329) · 📚 被引 18
- **作者**: Haoyu Wu, Alexandros Graikos, Dimitris Samaras
- **🏷️ 机构**: Stony Brook University
- **会议**: ICCV 2023

### MV-Map: Offboard HD Map Generation with Multi-view Consistency.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00795) · 📚 被引 25
- **作者**: Ziyang Xie, Ziqi Pang, Yu-Xiong Wang
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: ICCV 2023

### CL-MVSNet: Unsupervised Multi-view Stereo with Dual-level Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00349)
- **作者**: Kaiqiang Xiong, Rui Peng, Zhe Zhang, Tianxing Feng, Jianbo Jiao, Feng Gao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Long-Range Grouping Transformer for Multi-View 3D Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01674) · 📚 被引 20
- **作者**: Liying Yang, Zhenwei Zhu, Xuxin Lin, Jian Nong, Yanyan Liang
- **🏷️ 机构**: Macau University of Science and Technology
- **会议**: ICCV 2023

### DeLiRa: Self-Supervised Depth, Light, and Radiance Fields.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01644)
- **作者**: Vitor Guizilini, Igor Vasiljevic, Jiading Fang, Rares Ambrus, Sergey Zakharov, Vincent Sitzmann et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative Convolution Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00791)
- **作者**: Wencheng Han, Junbo Yin, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Self-supervised Monocular Depth Estimation: Let's Talk About The Weather.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00818)
- **作者**: Kieran Saunders, George Vogiatzis, Luis J. Manso
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### 3D Distillation: Improving Self-Supervised Monocular Depth Estimation on Reflective Surfaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00838)
- **作者**: Xuepeng Shi, Georgi Dikov, Gerhard Reitmayr, Tae-Kyun Kim, Mohsen Ghafoorian
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### GasMono: Geometry-Aided Self-Supervised Monocular Depth Estimation for Indoor Scenes.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01485)
- **作者**: Chaoqiang Zhao, Matteo Poggi, Fabio Tosi, Lei Zhou, Qiyu Sun, Yang Tang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### HaMuCo: Hand Pose Estimation via Multiview Collaborative Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01898)
- **作者**: Xiaozheng Zheng, Chao Wen, Zhou Xue, Pengfei Ren, Jingyu Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Two-in-One Depth: Bridging the Gap Between Monocular and Binocular Self-supervised Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00863)
- **作者**: Zhengming Zhou, Qiulei Dong
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. → [3d-detection](../3d-detection/Guideline%202023.md)
- 3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- ImGeoNet: Image-induced Geometry-aware Voxel Representation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Pixel-Aligned Recurrent Queries for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- NeRF-Det: Learning Geometry-Aware Volumetric Representation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception. → [bev](../bev/Guideline%202023.md)
- SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
