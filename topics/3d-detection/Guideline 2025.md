# 3D Detection — 2025 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00749)
- **作者**: Adrian Chow, Evelien Riddell, Yimu Wang, Sean Sedwards, Krzysztof Czarnecki
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D sensors provide point clouds, a canonical 3D representation used in various scene understanding tasks. Modern LiDARs face key challenges in several real-world scenarios, such as long-distance or low-albedo objects, producing sparse or erroneous point clouds. These errors, which are rooted in the noisy raw LiDAR measurements, get propagated to downstream perception models, resulting in potentially severe loss of accuracy. This is because conventional 3D processing pipelines do not retain any uncertainty information from the raw measurements when constructing point clouds. We propose Probabilistic Point Clouds (PPC), a novel 3D scene representation where each point is augmented with a probability attribute that encapsulates the measurement uncertainty (or confidence) in the raw data. We further introduce inference approaches that leverage PPC for robust 3D object detection; these methods are versatile and can be used as computationally lightweight drop-in modules in 3D inference pipelines. We demonstrate, via both simulations and real captures, that PPC-based 3D inference methods outperform several baselines using LiDAR as well as camera-LiDAR fusion models, across challenging indoor and outdoor scenarios involving small, distant, and low-albedo objects, as well as strong ambient light. Our project webpage is at https://bhavyagoyal.github.io/ppc .

</details>

### Robust 3D Object Detection Using Probabilistic Point Clouds From Single-Photon Lidars.
- **链接**: [arXiv:2508.00169](https://arxiv.org/abs/2508.00169) · 📚 被引 0
- **作者**: Bhavya Goyal, Felipe Gutierrez-Barragan, Wei Lin, Andreas Velten, Yin Li, Mohit Gupta
- **🏷️ 机构**: University of Wisconsin-Madison
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D sensors provide point clouds, a canonical 3D representation used in various scene understanding tasks. Modern LiDARs face key challenges in several real-world scenarios, such as long-distance or low-albedo objects, producing sparse or erroneous point clouds. These errors, which are rooted in the noisy raw LiDAR measurements, get propagated to downstream perception models, resulting in potentially severe loss of accuracy. This is because conventional 3D processing pipelines do not retain any uncertainty information from the raw measurements when constructing point clouds. We propose Probabilistic Point Clouds (PPC), a novel 3D scene representation where each point is augmented with a probability attribute that encapsulates the measurement uncertainty (or confidence) in the raw data. We further introduce inference approaches that leverage PPC for robust 3D object detection; these methods are versatile and can be used as computationally lightweight drop-in modules in 3D inference pipelines. We demonstrate, via both simulations and real captures, that PPC-based 3D inference methods outperform several baselines using LiDAR as well as camera-LiDAR fusion models, across challenging indoor and outdoor scenarios involving small, distant, and low-albedo objects, as well as strong ambient light. Our project webpage is at https://bhavyagoyal.github.io/ppc .

</details>

### OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00813)
- **作者**: Peng-Hao Hsu, Ke Zhang, Fu-En Wang, Tao Tu, Ming-Feng Li, Yu-Lun Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts.
- **链接**: [arXiv:2508.20488](https://arxiv.org/abs/2508.20488) · 📚 被引 0
- **作者**: Zixuan Hu, Dongxiao Li, Xinzhu Ma, Shixiang Tang, Xiaotong Li, Wenhan Yang et al.
- **🏷️ 机构**: School of Computer Science, Peking University,Beijing,China, The Chinese University of Hong Kong,Hongkong,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate monocular 3D object detection (M3OD) is pivotal for safety-critical applications like autonomous driving, yet its reliability deteriorates significantly under real-world domain shifts caused by environmental or sensor variations. To address these shifts, Test-Time Adaptation (TTA) methods have emerged, enabling models to adapt to target distributions during inference. While prior TTA approaches recognize the positive correlation between low uncertainty and high generalization ability, they fail to address the dual uncertainty inherent to M3OD: semantic uncertainty (ambiguous class predictions) and geometric uncertainty (unstable spatial localization). To bridge this gap, we propose Dual Uncertainty Optimization (DUO), the first TTA framework designed to jointly minimize both uncertainties for robust M3OD. Through a convex optimization lens, we introduce an innovative convex structure of the focal loss and further derive a novel unsupervised version, enabling label-agnostic uncertainty weighting and balanced learning for high-uncertainty objects. In parallel, we design a semantic-aware normal field constraint that preserves geometric coherence in regions with clear semantic cues, reducing uncertainty from the unstable 3D representation. This dual-branch mechanism forms a complementary loop: enhanced spatial perception improves semantic classification, and robust semantic predictions further refine spatial understanding. Extensive experiments demonstrate the superiority of DUO over existing methods across various datasets and domain shift types.

</details>

### GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-Based Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02495) · 📚 被引 1
- **作者**: Xin Jin, Haisheng Su, Cong Ma, Kai Liu, Wei Wu, Fei Hui et al.
- **🏷️ 机构**: Chang&#x0027; an University, Shanghai Jiao Tong University, SenseAuto Research
- **会议**: ICCV 2025

### Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection.
- **链接**: [arXiv:2508.02288](https://arxiv.org/abs/2508.02288) · [代码](https://github.com/mickeykang16/Ev-Stereo3D) · 📚 被引 2
- **作者**: Jae-Young Kang, Hoonhee Cho, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is essential for autonomous systems, enabling precise localization and dimension estimation. While LiDAR and RGB cameras are widely used, their fixed frame rates create perception gaps in high-speed scenarios. Event cameras, with their asynchronous nature and high temporal resolution, offer a solution by capturing motion continuously. The recent approach, which integrates event cameras with conventional sensors for continuous-time detection, struggles in fast-motion scenarios due to its dependency on synchronized sensors. We propose a novel stereo 3D object detection framework that relies solely on event cameras, eliminating the need for conventional 3D sensors. To compensate for the lack of semantic and geometric information in event data, we introduce a dual filter mechanism that extracts both. Additionally, we enhance regression by aligning bounding boxes with object-centric information. Experiments show that our method outperforms prior approaches in dynamic environments, demonstrating the potential of event cameras for robust, continuous-time 3D perception. The code is available at https://github.com/mickeykang16/Ev-Stereo3D.

</details>

### MemDistill: Distilling LiDAR Knowledge into Memory for Camera-Only 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00642)
- **作者**: Donghyeon Kwon, Youngseok Yoon, Hyeongseok Son, Suha Kwak
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### EVT: Efficient View Transformation for Multi-Modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02472)
- **作者**: Yongjin Lee, Hyeon Mun Jeong, Yurim Jeon, Sanghyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Perspective-Invariant 3D Object Detection.
- **链接**: [arXiv:2507.17665](https://arxiv.org/abs/2507.17665) · 📚 被引 1
- **作者**: Ao Liang, Lingdong Kong, Dongyue Lu, Youquan Liu, Jian Fang, Huaici Zhao et al.
- **🏷️ 机构**: National University of Singapore, Fudan University, Shenyang Institute of Automation, Chinese Academy of Sciences
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rise of robotics, LiDAR-based 3D object detection has garnered significant attention in both academia and industry. However, existing datasets and methods predominantly focus on vehicle-mounted platforms, leaving other autonomous platforms underexplored. To bridge this gap, we introduce Pi3DET, the first benchmark featuring LiDAR data and 3D bounding box annotations collected from multiple platforms: vehicle, quadruped, and drone, thereby facilitating research in 3D object detection for non-vehicle platforms as well as cross-platform 3D detection. Based on Pi3DET, we propose a novel cross-platform adaptation framework that transfers knowledge from the well-studied vehicle platform to other platforms. This framework achieves perspective-invariant 3D detection through robust alignment at both geometric and feature levels. Additionally, we establish a benchmark to evaluate the resilience and robustness of current 3D detectors in cross-platform scenarios, providing valuable insights for developing adaptive 3D perception systems. Extensive experiments validate the effectiveness of our approach on challenging cross-platform tasks, demonstrating substantial gains over existing adaptation methods. We hope this work paves the way for generalizable and unified 3D perception systems across diverse and complex environments. Our Pi3DET dataset, cross-platform benchmark suite, and annotation toolkit have been made publicly available.

</details>

### Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02403)
- **作者**: Linshen Liu, Boyan Su, Junyue Jiang, Guanlin Wu, Cong Guo, Ceyu Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02613)
- **作者**: Haisheng Su, Junjie Zhang, Feixiang Song, Sanping Zhou, Wei Wu, Junchi Yan et al.
- **🏷️ 机构**: XJTU
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider indoor 3D object detection with respect to a single RGB(-D) frame acquired from a commodity handheld device. We seek to significantly advance the status quo with respect to both data and modeling. First, we establish that existing datasets have significant limitations to scale, accuracy, and diversity of objects. As a result, we introduce the Cubify-Anything 1M (CA-1M) dataset, which exhaustively labels over 400K 3D objects on over 1K highly accurate laser-scanned scenes with near-perfect registration to over 3.5K handheld, egocentric captures. Next, we establish Cubify Transformer (CuTR), a fully Transformer 3D object detection baseline which rather than operating in 3D on point or voxel-based representations, predicts 3D boxes directly from 2D features derived from RGB(-D) inputs. While this approach lacks any 3D inductive biases, we show that paired with CA-1M, CuTR outperforms point-based methods - accurately recalling over 62% of objects in 3D, and is significantly more capable at handling noise and uncertainty present in commodity LiDAR-derived depth maps while also providing promising RGB only performance without architecture changes. Furthermore, by pre-training on CA-1M, CuTR can outperform point-based methods on a more diverse variant of SUN RGB-D - supporting the notion that while inductive biases in 3D are useful at the smaller sizes of existing datasets, they fail to scale to the data-rich regime of CA-1M. Overall, this dataset and baseline model provide strong evidence that we are moving towards models which can effectively Cubify Anything.

</details>

### FSHNet: Fully Sparse Hybrid Network for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_FSHNet_Fully_Sparse_Hybrid_Network_for_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Shuai Liu, Mingyue Cui, Boyang Li, Quanmin Liang, Tinghe Hong, Yunxiao Shan et al.
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering, Sun Yat-sen University,School of Artificial Intelligence
- **会议**: CVPR 2025

### MonoTAKD: Teaching Assistant Knowledge Distillation for Monocular 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_MonoTAKD_Teaching_Assistant_Knowledge_Distillation_for_Monocular_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Hou-I Liu, Christine Wu, Jen-Hao Cheng, Wenhao Chai, Shian-Yun Wang, Gaowen Liu et al.
- **🏷️ 机构**: National Yang Ming Chiao Tung University, University of Washington, University of Southern California
- **会议**: CVPR 2025

### RICCARDO: Radar Hit Prediction and Convolution for Camera-Radar 3D Object Detection.
- **链接**: [arXiv:2504.09086](https://arxiv.org/abs/2504.09086) · [代码](https://github.com/longyunf/riccardo) · 📚 被引 5
- **作者**: Yunfei Long, Abhinav Kumar, Xiaoming Liu, Daniel D. Morris
- **🏷️ 机构**: Michigan State University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Radar hits reflect from points on both the boundary and internal to object outlines. This results in a complex distribution of radar hits that depends on factors including object category, size, and orientation. Current radar-camera fusion methods implicitly account for this with a black-box neural network. In this paper, we explicitly utilize a radar hit distribution model to assist fusion. First, we build a model to predict radar hit distributions conditioned on object properties obtained from a monocular detector. Second, we use the predicted distribution as a kernel to match actual measured radar points in the neighborhood of the monocular detections, generating matching scores at nearby positions. Finally, a fusion stage combines context with the kernel detector to refine the matching scores. Our method achieves the state-of-the-art radar-camera detection performance on nuScenes. Our source code is available at https://github.com/longyunf/riccardo.

</details>

### GBlobs: Explicit Local Structure via Gaussian Blobs for Improved Cross-Domain LiDAR-based 3D Object Detection.
- **链接**: [arXiv:2503.08639](https://arxiv.org/abs/2503.08639) · 📚 被引 2
- **作者**: Dusan Malic, Christian Fruhwirth-Reisinger, Samuel Schulter, Horst Possegger
- **🏷️ 机构**: Christian Doppler Laboratory for Embedded Machine Learning, Amazon
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D detectors need large datasets for training, yet they struggle to generalize to novel domains. Domain Generalization (DG) aims to mitigate this by training detectors that are invariant to such domain shifts. Current DG approaches exclusively rely on global geometric features (point cloud Cartesian coordinates) as input features. Over-reliance on these global geometric features can, however, cause 3D detectors to prioritize object location and absolute position, resulting in poor cross-domain performance. To mitigate this, we propose to exploit explicit local point cloud structure for DG, in particular by encoding point cloud neighborhoods with Gaussian blobs, GBlobs. Our proposed formulation is highly efficient and requires no additional parameters. Without any bells and whistles, simply by integrating GBlobs in existing detectors, we beat the current state-of-the-art in challenging single-source DG benchmarks by over 21 mAP (Waymo->KITTI), 13 mAP (KITTI->Waymo), and 12 mAP (nuScenes->KITTI), without sacrificing in-domain performance. Additionally, GBlobs demonstrate exceptional performance in multi-source DG, surpassing the current state-of-the-art by 17, 12, and 5 mAP on Waymo, KITTI, and ONCE, respectively.

</details>

### Leveraging Temporal Cues for Semi-Supervised Multi-View 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Park_Leveraging_Temporal_Cues_for_Semi-Supervised_Multi-View_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Jinhyung Park, Navyata Sanghvi, Hiroki Adachi, Yoshihisa Shibata, Shawn Hunt, Shinya Tanaka et al.
- **🏷️ 机构**: Carnegie Mellon University, DENSO Corporation, DENSO International America, Inc.
- **会议**: CVPR 2025

### MonoDGP: Monocular 3D Object Detection with Decoupled-Query and Geometry-Error Priors.
- **链接**: [arXiv:2410.19590](https://arxiv.org/abs/2410.19590) · [代码](https://github.com/PuFanqi23/MonoDGP) · 📚 被引 25
- **作者**: Fanqi Pu, Yifan Wang, Jiru Deng, Wenming Yang
- **🏷️ 机构**: Tsinghua University,Shenzhen International Graduate School
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perspective projection has been extensively utilized in monocular 3D object detection methods. It introduces geometric priors from 2D bounding boxes and 3D object dimensions to reduce the uncertainty of depth estimation. However, due to depth errors originating from the object's visual surface, the height of the bounding box often fails to represent the actual projected central height, which undermines the effectiveness of geometric depth. Direct prediction for the projected height unavoidably results in a loss of 2D priors, while multi-depth prediction with complex branches does not fully leverage geometric depth. This paper presents a Transformer-based monocular 3D object detection method called MonoDGP, which adopts perspective-invariant geometry errors to modify the projection formula. We also try to systematically discuss and explain the mechanisms and efficacy behind geometry errors, which serve as a simple but effective alternative to multi-depth prediction. Additionally, MonoDGP decouples the depth-guided decoder and constructs a 2D decoder only dependent on visual features, providing 2D priors and initializing object queries without the disturbance of 3D detection. To further optimize and fine-tune input tokens of the transformer decoder, we also introduce a Region Segment Head (RSH) that generates enhanced features and segment embeddings. Our monocular method demonstrates state-of-the-art performance on the KITTI benchmark without extra data. Code is available at https://github.com/PuFanqi23/MonoDGP.

</details>

### Uncertainty Meets Diversity: A Comprehensive Active Learning Framework for Indoor 3D Object Detection.
- **链接**: [arXiv:2503.16125](https://arxiv.org/abs/2503.16125) · 📚 被引 3
- **作者**: Jiangyi Wang, Na Zhao
- **🏷️ 机构**: Singapore University of Technology and Design (SUTD)
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Active learning has emerged as a promising approach to reduce the substantial annotation burden in 3D object detection tasks, spurring several initiatives in outdoor environments. However, its application in indoor environments remains unexplored. Compared to outdoor 3D datasets, indoor datasets face significant challenges, including fewer training samples per class, a greater number of classes, more severe class imbalance, and more diverse scene types and intra-class variances. This paper presents the first study on active learning for indoor 3D object detection, where we propose a novel framework tailored for this task. Our method incorporates two key criteria - uncertainty and diversity - to actively select the most ambiguous and informative unlabeled samples for annotation. The uncertainty criterion accounts for both inaccurate detections and undetected objects, ensuring that the most ambiguous samples are prioritized. Meanwhile, the diversity criterion is formulated as a joint optimization problem that maximizes the diversity of both object class distributions and scene types, using a new Class-aware Adaptive Prototype (CAP) bank. The CAP bank dynamically allocates representative prototypes to each class, helping to capture varying intra-class diversity across different categories. We evaluate our method on SUN RGB-D and ScanNetV2, where it outperforms baselines by a significant margin, achieving over 85% of fully-supervised performance with just 10% of the annotation budget.

</details>

### CorrBEV: Multi-View 3D Object Detection by Correlation Learning with Multi-modal Prototypes.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xue_CorrBEV_Multi-View_3D_Object_Detection_by_Correlation_Learning_with_Multi-modal_CVPR_2025_paper.html)
- **作者**: Ziteng Xue, Mingzhe Guo, Heng Fan, Shihui Zhang, Zhipeng Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Perspective-Invariant 3D Object Detection.
- **链接**: [arXiv:2507.17665](https://arxiv.org/abs/2507.17665) · 📚 被引 1
- **作者**: Ao Liang, Lingdong Kong, Dongyue Lu, Youquan Liu, Jian Fang, Huaici Zhao et al.
- **🏷️ 机构**: National University of Singapore, Fudan University, Shenyang Institute of Automation, Chinese Academy of Sciences
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rise of robotics, LiDAR-based 3D object detection has garnered significant attention in both academia and industry. However, existing datasets and methods predominantly focus on vehicle-mounted platforms, leaving other autonomous platforms underexplored. To bridge this gap, we introduce Pi3DET, the first benchmark featuring LiDAR data and 3D bounding box annotations collected from multiple platforms: vehicle, quadruped, and drone, thereby facilitating research in 3D object detection for non-vehicle platforms as well as cross-platform 3D detection. Based on Pi3DET, we propose a novel cross-platform adaptation framework that transfers knowledge from the well-studied vehicle platform to other platforms. This framework achieves perspective-invariant 3D detection through robust alignment at both geometric and feature levels. Additionally, we establish a benchmark to evaluate the resilience and robustness of current 3D detectors in cross-platform scenarios, providing valuable insights for developing adaptive 3D perception systems. Extensive experiments validate the effectiveness of our approach on challenging cross-platform tasks, demonstrating substantial gains over existing adaptation methods. We hope this work paves the way for generalizable and unified 3D perception systems across diverse and complex environments. Our Pi3DET dataset, cross-platform benchmark suite, and annotation toolkit have been made publicly available.

</details>

### Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02403)
- **作者**: Linshen Liu, Boyan Su, Junyue Jiang, Guanlin Wu, Cong Guo, Ceyu Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02613)
- **作者**: Haisheng Su, Junjie Zhang, Feixiang Song, Sanping Zhou, Wei Wu, Junchi Yan et al.
- **🏷️ 机构**: XJTU
- **会议**: ICCV 2025

</details>

### Gaussian-Det: Learning Closed-Surface Gaussians for 3D Object Detection.
- **链接**: [arXiv:2410.01404](https://arxiv.org/abs/2410.01404)
- **作者**: Hongru Yan, Yu Zheng, Yueqi Duan
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Motal: Unsupervised 3D Object Detection by Modality and Task-Specific Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00593) · 📚 被引 0
- **作者**: Hai Wu, Hongwei Lin, Xusheng Guo, Xin Li, Mingming Wang, Cheng Wang et al.
- **🏷️ 机构**: Xiamen University, Texas A&#x0026;M University, Tsinghua University
- **会议**: ICCV 2025

### Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02143)
- **作者**: Lizhen Xu, Xiuxiu Bai, Xiaojun Jia, Jianwu Fang, Shanmin Pang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Boosting Multi-View Indoor 3D Object Detection Via Adaptive 3D Volume Construction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00565)
- **作者**: Runmin Zhang, Zhu Yu, Si-Yuan Cao, Lingyu Zhu, Guangyi Zhang, Xiaokai Bai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Harnessing Uncertainty-Aware Bounding Boxes for Unsupervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00862) · 📚 被引 1
- **作者**: Ruiyang Zhang, Hu Zhang, Zhedong Zheng
- **🏷️ 机构**: FST and ICI, University of Macau,China, CSIRO Data61,Australia
- **会议**: ICCV 2025

### CVFusion: Cross-View Fusion of 4D Radar and Camera for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02617) · 📚 被引 4
- **作者**: Hanzhi Zhong, Zhiyu Xiang, Ruoyu Xu, Jingyun Fu, Peng Xu, Shaohong Wang et al.
- **🏷️ 机构**: Zhejiang University,China
- **会议**: ICCV 2025

### Doppler-Aware LiDAR-RADAR Fusion for Weather-Robust 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02525) · 📚 被引 2
- **作者**: Yujeong Chae, Heejun Park, Hyeonseong Kim, Kuk-Jin Yoon
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology
- **会议**: ICCV 2025

### VoxelKP: A Voxel-Based Network Architecture for Human Keypoint Estimation in LiDAR Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02626) · 📚 被引 0
- **作者**: Jian Shi, Peter Wonka
- **🏷️ 机构**: KAUST
- **会议**: ICCV 2025

### SDFormer: Vision-Based 3D Semantic Scene Completion via SAM-Assisted Dual-Channel Voxel Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02491) · 📚 被引 0
- **作者**: Yujie Xue, Huilong Pi, Jiapeng Zhang, Yunchuan Qin, Zhuo Tang, Kenli Li et al.
- **🏷️ 机构**: College of Computer Science and Electronic Engineering, Hunan University
- **会议**: ICCV 2025
