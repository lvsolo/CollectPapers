# Autonomous Driving — 2025 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 22 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Driving by the Rules: A Benchmark for Integrating Traffic Sign Regulations into Vectorized HD Map. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2410.23780](https://arxiv.org/abs/2410.23780) · 📚 被引 3
- **作者**: Xinyuan Chang, Maixuan Xue, Xinran Liu, Zheng Pan, Xing Wei
- **🏷️ 机构**: Alibaba Group,Amap, Xi&#x2019;an Jiaotong University
- **会议**: CVPR 2025
- **摘要（中）**: 针对在线高精地图构建中忽略交通规则层的问题，本文提出MapDR数据集，包含超过10000个标注视频片段，用于从交通标志中提取驾驶规则并与局部感知的矢量化高精地图关联。基于该基准，作者定义了将交通规则集成到在线高精地图的新任务，并提供了模块化（VLE-MEE）和端到端（RuleVLM）的基线解决方案。相比现有工作，该研究填补了交通标志规则集成方面的关键空白，为可靠自动驾驶系统的发展做出贡献。
- **摘要（英）**: Addressing the neglect of traffic regulation layers in online HD mapping, this paper introduces MapDR, a dataset with over 10,000 annotated video clips for extracting driving rules from traffic signs and associating them with vectorized local HD maps. It defines a new task of integrating traffic regulations into online maps and provides modular (VLE-MEE) and end-to-end (RuleVLM) baselines, filling a critical gap and advancing reliable autonomous driving.
- **核心贡献**: 提出了MapDR数据集和交通规则集成任务，并提供了两种基线解决方案。
- **创新点**: 首次将交通标志规则提取与在线矢量化高精地图关联，定义了新任务。
- **结果**: MapDR包含超过10000个标注视频片段，基线方法展示了有效性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ensuring adherence to traffic sign regulations is essential for both human and autonomous vehicle navigation. While current online mapping solutions often prioritize the construction of the geometric and connectivity layers of HD maps, overlooking the construction of the traffic regulation layer within HD maps. Addressing this gap, we introduce MapDR, a novel dataset designed for the extraction of Driving Rules from traffic signs and their association with vectorized, locally perceived HD Maps. MapDR features over $10,000$ annotated video clips that capture the intricate correlation between traffic sign regulations and lanes. Built upon this benchmark and the newly defined task of integrating traffic regulations into online HD maps, we provide modular and end-to-end solutions: VLE-MEE and RuleVLM, offering a strong baseline for advancing autonomous driving technology. It fills a critical gap in the integration of traffic sign rules, contributing to the development of reliable autonomous driving systems. Code is available at https://github.com/MIV-XJTU/MapDR.

</details>

### Spotting the Unexpected (STU): A 3D LiDAR Dataset for Anomaly Segmentation in Autonomous Driving.
- **链接**: [arXiv:2505.02148](https://arxiv.org/abs/2505.02148) · 📚 被引 4
- **作者**: Alexey Nekrasov, Malcolm Burdorf, Stewart Worrall, Bastian Leibe, Julie Stephany Berrio Perez
- **🏷️ 机构**: RWTH Aachen University, The University of Sydney
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vehicle-to-everything (V2X) collaborative perception has emerged as a promising solution to address the limitations of single-vehicle perception systems. However, existing V2X datasets are limited in scope, diversity, and quality. To address these gaps, we present Mixed Signals, a comprehensive V2X dataset featuring 45.1k point clouds and 240.6k bounding boxes collected from three connected autonomous vehicles (CAVs) equipped with two different configurations of LiDAR sensors, plus a roadside unit with dual LiDARs. Our dataset provides point clouds and bounding box annotations across 10 classes, ensuring reliable data for perception training. We provide detailed statistical analysis on the quality of our dataset and extensively benchmark existing V2X methods on it. The Mixed Signals dataset is ready-to-use, with precise alignment and consistent annotations across time and viewpoints. Dataset website is available at https://mixedsignalsdataset.cs.cornell.edu/.

</details>

### RoboTron-Drive: All-in-One Large Multimodal Model for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00751)
- **作者**: Zhijian Huang, Chengjian Feng, Feng Yan, Baihui Xiao, Zequn Jie, Yujie Zhong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### T-norm Selection for Object Detection in Autonomous Driving with Logical Constraints.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7dbdf006424e7749c8a35913d3574c4e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Thomas Eiter, Katsumi Inoue, Nelson Higuera, Sota Moriyama
- **🏷️ 机构**: Technische Universität Wien, NII, TU Wien
- **会议**: NeurIPS 2025

### DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving.
- **链接**: [arXiv:2412.09043](https://arxiv.org/abs/2412.09043) · [代码](https://github.com/EnVision-Research/DriveRecon) · 📚 被引 0
- **作者**: Hao Lu, Tianshuo Xu, Wenzhao Zheng, Yunpeng Zhang, Wei Zhan, Dalong Du et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, University of California, Berkeley, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Photorealistic 4D reconstruction of street scenes is essential for developing real-world simulators in autonomous driving. However, most existing methods perform this task offline and rely on time-consuming iterative processes, limiting their practical applications. To this end, we introduce the Large 4D Gaussian Reconstruction Model (DrivingRecon), a generalizable driving scene reconstruction model, which directly predicts 4D Gaussian from surround view videos. To better integrate the surround-view images, the Prune and Dilate Block (PD-Block) is proposed to eliminate overlapping Gaussian points between adjacent views and remove redundant background points. To enhance cross-temporal information, dynamic and static decoupling is tailored to better learn geometry and motion features. Experimental results demonstrate that DrivingRecon significantly improves scene reconstruction quality and novel view synthesis compared to existing methods. Furthermore, we explore applications of DrivingRecon in model pre-training, vehicle adaptation, and scene editing. Our code is available at https://github.com/EnVision-Research/DriveRecon.

</details>

### JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration.
- **链接**: [arXiv:2504.04158](https://arxiv.org/abs/2504.04158) · 📚 被引 21
- **作者**: Yunlong Lin, Zixu Lin, Haoyu Chen, Panwang Pan, Chenxin Li, Sixiang Chen et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,Xiamen,China, The Hong Kong University of Science and Technology (Guangzhou), Bytedance&#x2019;s Pico
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-centric perception systems struggle with unpredictable and coupled weather degradations in the wild. Current solutions are often limited, as they either depend on specific degradation priors or suffer from significant domain gaps. To enable robust and autonomous operation in real-world conditions, we propose JarvisIR, a VLM-powered agent that leverages the VLM as a controller to manage multiple expert restoration models. To further enhance system robustness, reduce hallucinations, and improve generalizability in real-world adverse weather, JarvisIR employs a novel two-stage framework consisting of supervised fine-tuning and human feedback alignment. Specifically, to address the lack of paired data in real-world scenarios, the human feedback alignment enables the VLM to be fine-tuned effectively on large-scale real-world data in an unsupervised manner. To support the training and evaluation of JarvisIR, we introduce CleanBench, a comprehensive dataset consisting of high-quality and large-scale instruction-responses pairs, including 150K synthetic entries and 80K real entries. Extensive experiments demonstrate that JarvisIR exhibits superior decision-making and restoration capabilities. Compared with existing methods, it achieves a 50% improvement in the average of all perception metrics on CleanBench-Real. Project page: https://cvpr2025-jarvisir.github.io/.

</details>

### T2SG: Traffic Topology Scene Graph for Topology Reasoning in Autonomous Driving.
- **链接**: [arXiv:2411.18894](https://arxiv.org/abs/2411.18894)
- **作者**: Changsheng Lv, Mengshi Qi, Liang Liu, Huadong Ma
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### AGC-Drive: A Large-Scale Dataset for Real-World Aerial-Ground Collaboration in Driving Scenarios.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/910ac01a3e5c5e7e67d64f23c0e1a740-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Yunhao Hou, Bochao Zou, Min Zhang, Ran Chen, Shangdong Yang, Yanmei Zhang et al.
- **🏷️ 机构**: University of Science and Technology Beijing, Xiamen NEVC, 北京科技大学
- **会议**: NeurIPS 2025

### A Driving-Style-Adaptive Framework for Vehicle Trajectory Prediction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/734615a8060a8e0c331bb4f87bf310f4-Abstract-Conference.html) · 📚 被引 0
- **作者**: Di Wen, Yu Wang, Zhigang Wu, Zhaocheng He, Zhe Wu, Qingfang Zheng
- **🏷️ 机构**: Sun Yat-Sen University, Tsinghua University, SUN YAT-SEN UNIVERSITY
- **会议**: NeurIPS 2025

### Future-Aware End-to-End Driving: Bidirectional Modeling of Trajectory Planning and Scene Evolution.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/0ee633a6ade45eab4276352b3ee79c7a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Bozhou Zhang, Nan Song, Jingyu Li, Xiatian Zhu, Jiankang Deng, Li Zhang
- **🏷️ 机构**: Fudan University, University of Surrey, Imperial College London
- **会议**: NeurIPS 2025

### SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment.
- **链接**: [arXiv:2503.09594](https://arxiv.org/abs/2503.09594) · 📚 被引 19
- **作者**: Katrin Renz, Long Chen, Elahe Arani, Oleg Sinavski
- **🏷️ 机构**: Wayve
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

## 跨领域论文（完整笔记在其他领域）

</details>

### Don't Shake the Wheel: Momentum-Aware Planning in End-to-End Autonomous Driving.
- **链接**: [arXiv:2503.03125](https://arxiv.org/abs/2503.03125)
- **作者**: Ziying Song, Caiyan Jia, Lin Liu, Hongyu Pan, Yongchang Zhang, Junming Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving frameworks enable seamless integration of perception and planning but often rely on one-shot trajectory prediction, which may lead to unstable control and vulnerability to occlusions in single-frame perception. To address this, we propose the Momentum-Aware Driving (MomAD) framework, which introduces trajectory momentum and perception momentum to stabilize and refine trajectory predictions. MomAD comprises two core components: (1) Topological Trajectory Matching (TTM) employs Hausdorff Distance to select the optimal planning query that aligns with prior paths to ensure coherence;(2) Momentum Planning Interactor (MPI) cross-attends the selected planning query with historical queries to expand static and dynamic perception files. This enriched query, in turn, helps regenerate long-horizon trajectory and reduce collision risks. To mitigate noise arising from dynamic environments and detection errors, we introduce robust instance denoising during training, enabling the planning model to focus on critical signals and improve its robustness. We also propose a novel Trajectory Prediction Consistency (TPC) metric to quantitatively assess planning stability. Experiments on the nuScenes dataset demonstrate that MomAD achieves superior long-term consistency (>=3s) compared to SOTA methods. Moreover, evaluations on the curated Turning-nuScenes shows that MomAD reduces the collision rate by 26% and improves TPC by 0.97m (33.45%) over a 6s prediction horizon, while closedloop on Bench2Drive demonstrates an up to 16.3% improvement in success rate.

</details>

### SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_SplatFlow_Self-Supervised_Dynamic_Gaussian_Splatting_in_Neural_Motion_Flow_Field_CVPR_2025_paper.html)
- **作者**: Su Sun, Cheng Zhao, Zhuoyang Sun, Yingjie Victor Chen, Mei Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### OmniDrive: A Holistic Vision-Language Dataset for Autonomous Driving with Counterfactual Reasoning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_OmniDrive_A_Holistic_Vision-Language_Dataset_for_Autonomous_Driving_with_Counterfactual_CVPR_2025_paper.html) · 📚 被引 27
- **作者**: Shihao Wang, Zhiding Yu, Xiaohui Jiang, Shiyi Lan, Min Shi, Nadine Chang et al.
- **🏷️ 机构**: NVIDIA, Beijing Institute of Technology
- **会议**: CVPR 2025

### GoalFlow: Goal-Driven Flow Matching for Multimodal Trajectories Generation in End-to-End Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xing_GoalFlow_Goal-Driven_Flow_Matching_for_Multimodal_Trajectories_Generation_in_End-to-End_CVPR_2025_paper.html)
- **作者**: Zebin Xing, Xingyu Zhang, Yang Hu, Bo Jiang, Tong He, Qian Zhang et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab
- **会议**: CVPR 2025

### DriveGPT4-V2: Harnessing Large Language Model Capabilities for Enhanced Closed-Loop Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_DriveGPT4-V2_Harnessing_Large_Language_Model_Capabilities_for_Enhanced_Closed-Loop_Autonomous_CVPR_2025_paper.html) · 📚 被引 14
- **作者**: Zhenhua Xu, Yan Bai, Yujia Zhang, Zhuoling Li, Fei Xia, Kwan-Yee K. Wong et al.
- **🏷️ 机构**: The University of Hong Kong, Meituan, Tsinghua University
- **会议**: CVPR 2025

### Enduring, Efficient and Robust Trajectory Prediction Attack in Autonomous Driving via Optimization-Driven Multi-Frame Perturbation Framework.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Enduring_Efficient_and_Robust_Trajectory_Prediction_Attack_in_Autonomous_Driving_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Yi Yu, Weizhen Han, Libing Wu, Bingyi Liu, Enshu Wang, Zhuangzhuang Zhang
- **🏷️ 机构**: Wuhan University,Key Laboratory of Aerospace Information Security and Trusted Computing, Ministry of Education, School of Cyber Science and Engineering, Wuhan University of Technology,School of Computer Science and Artificial Intelligence, City University of Hong Kong,Department of Computer Science
- **会议**: CVPR 2025

### CarPlanner: Consistent Auto-regressive Trajectory Planning for Large-Scale Reinforcement Learning in Autonomous Driving.
- **链接**: [arXiv:2502.19908](https://arxiv.org/abs/2502.19908) · 📚 被引 14
- **作者**: Dongkun Zhang, Jiaming Liang, Ke Guo, Sha Lu, Qi Wang, Rong Xiong et al.
- **🏷️ 机构**: Zhejiang University, Cainiao Network
- **会议**: CVPR 2025

### Orion: A Holistic End-To-End Autonomous Driving Framework by Vision-Language Instructed Action Generation.
- **链接**: [arXiv:2503.19755](https://arxiv.org/abs/2503.19755) · 📚 被引 8
- **作者**: Haoyu Fu, Diankun Zhang, Zongchuang Zhao, Jianfeng Cui, Dingkang Liang, Chong Zhang et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Xiaomi EV
- **会议**: ICCV 2025

### MagicDrive-V2: High-Resolution Long Video Generation for Autonomous Driving with Adaptive Control.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02612) · 📚 被引 2
- **作者**: Ruiyuan Gao, Kai Chen, Bo Xiao, Lanqing Hong, Zhenguo Li, Qiang Xu
- **🏷️ 机构**: CUHK, HKUST, Huawei Cloud
- **会议**: ICCV 2025

### Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving.
- **链接**: [arXiv:2503.18108](https://arxiv.org/abs/2503.18108) · 📚 被引 1
- **作者**: Junhao Ge, Zuhong Liu, Longteng Fan, Yifan Jiang, Jiaqi Su, Yiming Li et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, New York University, ETH Zurich
- **会议**: ICCV 2025

### MPDrive: Improving Spatial Understanding with Marker-Based Prompt Learning for Autonomous Driving.
- **链接**: [arXiv:2504.00379](https://arxiv.org/abs/2504.00379) · 📚 被引 9
- **作者**: Zhiyuan Zhang, Xiaofan Li, Zhihao Xu, Wenjie Peng, Zijian Zhou, Miaojing Shi et al.
- **🏷️ 机构**: South China University of Technology, Baidu Inc., King&#x2019;s College London
- **会议**: CVPR 2025

### CARIM: Caption-Based Autonomous Driving Scene Retrieval via Inclusive Text Matching.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02046) · 📚 被引 0
- **作者**: Minjoo Ki, Daejung Kim, Kisung Kim, Seon Joo Kim, Jinhan Lee
- **🏷️ 机构**: Yonsei University,Korea, Naver Labs,Korea
- **会议**: ICCV 2025

> The generation and simulation of diverse real-world scenes have significant application value in the field of autonomous driving, especially for the corner cases. Recently, researchers have explored employing neural radiance fields or diffusion models to generate novel views or synthetic data under driving scenes. However, these approaches suffer from unseen scenes or restricted video length, thus lacking sufficient adaptability for data generation and simulation. To address these issues, we propose a simple yet effective framework, named Glad, to generate video data in a frame-by-frame style. To ensure the temporal consistency of synthetic video, we introduce a latent variable propagation module, which views the latent features of previous frame as noise prior and injects it into the latent features of current frame. In addition, we design a streaming data sampler to orderly sample the original image in a video clip at continuous iterations. Given the reference frame, our Glad can be viewed as a streaming simulator by generating the videos for specific scenes. Extensive experiments are performed on the widely-used nuScenes dataset. Experimental results demonstrate that our proposed Glad achieves promising performance, serving as a strong baseline for online video generation. We will release the source code and models publicly.

</details>

### Bridging Past and Future: End-to-End Autonomous Driving with Historical Prediction and Planning.
- **链接**: [arXiv:2503.14182](https://arxiv.org/abs/2503.14182) · 📚 被引 7
- **作者**: Bozhou Zhang, Nan Song, Xin Jin, Li Zhang
- **🏷️ 机构**: Fudan University,School of Data Science, Eastern Institute of Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Achieving human-like driving behaviors in complex open-world environments is a critical challenge in autonomous driving. Contemporary learning-based planning approaches such as imitation learning methods often struggle to balance competing objectives and lack of safety assurance,due to limited adaptability and inadequacy in learning complex multi-modal behaviors commonly exhibited in human planning, not to mention their strong reliance on the fallback strategy with predefined rules. We propose a novel transformer-based Diffusion Planner for closed-loop planning, which can effectively model multi-modal driving behavior and ensure trajectory quality without any rule-based refinement. Our model supports joint modeling of both prediction and planning tasks under the same architecture, enabling cooperative behaviors between vehicles. Moreover, by learning the gradient of the trajectory score function and employing a flexible classifier guidance mechanism, Diffusion Planner effectively achieves safe and adaptable planning behaviors. Evaluations on the large-scale real-world autonomous planning benchmark nuPlan and our newly collected 200-hour delivery-vehicle driving dataset demonstrate that Diffusion Planner achieves state-of-the-art closed-loop performance with robust transferability in diverse driving styles.

</details>

## 跨领域论文（完整笔记在其他领域）

- V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)

## 🆕 增量新增

### SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2411.16816](https://arxiv.org/abs/2411.16816) · 📚 被引 31
- **作者**: Georg Hess, Carl Lindström, Maryam Fatemi, Christoffer Petersson, Lennart Svensson
- **🏷️ 机构**: Zenseact, Chalmers University of Technology
- **会议**: CVPR 2025
- **摘要（中）**: 针对现有神经渲染方法（如NeRF）在自动驾驶传感器仿真中渲染速度慢、且3DGS方法仅支持相机数据的问题，本文提出了SplatAD，首个基于3D高斯泼溅的方法，实现动态场景中相机和LiDAR数据的实时逼真渲染。该方法精确建模了滚动快门效应、LiDAR强度和射线丢失等传感器特性，并设计了专用算法优化渲染效率。在三个自动驾驶数据集上的评估表明，SplatAD达到了最先进的性能。
- **摘要（英）**: To overcome the slow rendering of NeRF methods and the camera-only limitation of 3DGS in autonomous driving simulation, this paper proposes SplatAD, the first 3DGS-based method for real-time, realistic rendering of dynamic scenes for both camera and LiDAR. It models rolling shutter, lidar intensity, and dropouts with optimized algorithms, achieving state-of-the-art results on three datasets.
- **核心贡献**: 提出了SplatAD，首个支持相机和LiDAR实时渲染的3DGS方法。
- **创新点**: 建模传感器特定现象并优化渲染效率，扩展3DGS至LiDAR。
- **结果**: 在三个数据集上达到SOTA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ensuring the safety of autonomous robots, such as self-driving vehicles, requires extensive testing across diverse driving scenarios. Simulation is a key ingredient for conducting such testing in a cost-effective and scalable way. Neural rendering methods have gained popularity, as they can build simulation environments from collected logs in a data-driven manner. However, existing neural radiance field (NeRF) methods for sensor-realistic rendering of camera and lidar data suffer from low rendering speeds, limiting their applicability for large-scale testing. While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous driving. To address these limitations, we propose SplatAD, the first 3DGS-based method for realistic, real-time rendering of dynamic scenes for both camera and lidar data. SplatAD accurately models key sensor-specific phenomena such as rolling shutter effects, lidar intensity, and lidar ray dropouts, using purpose-built algorithms to optimize rendering efficiency. Evaluation across three autonomous driving datasets demonstrates that SplatAD achieves state-of-the-art rendering quality with up to +2 PSNR for NVS and +3 PSNR for reconstruction while increasing rendering speed over NeRF-based methods by an order of magnitude. See https://research.zenseact.com/publications/splatad/ for our project page.

</details>

### HiLoTs: High-Low Temporal Sensitive Representation Learning for Semi-Supervised LiDAR Segmentation in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2503.17752](https://arxiv.org/abs/2503.17752) · 📚 被引 8
- **作者**: R. D. Lin, Pengcheng Weng, Yinqiao Wang, Han Ding, Jinsong Han, Fei Wang
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering,China, Xi&#x2019;an Jiaotong University,School of Computer Science and Technology,China, Zhejiang University,College of Computer Science and Technology,China
- **会议**: CVPR 2025
- **摘要（中）**: 针对半监督LiDAR分割中忽略长期时间信息的问题，提出HiLoTs方法，从连续LiDAR帧中学习高/低时间敏感性表示，利用交叉注意力融合，并在教师-学生框架中对齐标注与未标注分支。相比仅利用相邻帧的方法，该方法利用了驾驶场景中近处物体稳定、远处物体变化大的自然特性。实验表明，该方法在多个数据集上显著提升分割性能。
- **摘要（英）**: To address the neglect of long-term temporal information in semi-supervised LiDAR segmentation, HiLoTs learns high- and low-temporal-sensitivity representations from continuous frames, fuses them via cross-attention, and aligns labeled/unlabeled branches in a teacher-student framework. It leverages the natural property that nearby objects are stable while distant ones vary. Experiments show significant performance gains on multiple datasets.
- **核心贡献**: 提出利用高-低时间敏感性表示学习提升半监督LiDAR分割性能。
- **创新点**: 首次将时间敏感性差异引入半监督LiDAR分割表示学习。
- **结果**: 在多个数据集上显著提升分割精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR point cloud semantic segmentation plays a crucial role in autonomous driving. In recent years, semi-supervised methods have gained popularity due to their significant reduction in annotation labor and time costs. Current semi-supervised methods typically focus on point cloud spatial distribution or consider short-term temporal representations, e.g., only two adjacent frames, often overlooking the rich long-term temporal properties inherent in autonomous driving scenarios. In driving experience, we observe that nearby objects, such as roads and vehicles, remain stable while driving, whereas distant objects exhibit greater variability in category and shape. This natural phenomenon is also captured by LiDAR, which reflects lower temporal sensitivity for nearby objects and higher sensitivity for distant ones. To leverage these characteristics, we propose HiLoTs, which learns high-temporal sensitivity and low-temporal sensitivity representations from continuous LiDAR frames. These representations are further enhanced and fused using a cross-attention mechanism. Additionally, we employ a teacher-student framework to align the representations learned by the labeled and unlabeled branches, effectively utilizing the large amounts of unlabeled data. Experimental results on the SemanticKITTI and nuScenes datasets demonstrate that our proposed HiLoTs outperforms state-of-the-art semi-supervised methods, and achieves performance close to LiDAR+Camera multimodal approaches. Code is available on https://github.com/rdlin118/HiLoTs

</details>

### SOLVE: Synergy of Language-Vision and End-to-End Networks for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2505.16805](https://arxiv.org/abs/2505.16805) · 📚 被引 6
- **作者**: Xuesong Chen, Linjiang Huang, Tao Ma, Rongyao Fang, Shaoshuai Shi, Hongsheng Li
- **🏷️ 机构**: MMLab,CUHK, Beihang University,Institute of Artificial Intelligence, Didi Chuxing,Voyager Research
- **会议**: CVPR 2025
- **摘要（中）**: ①针对VLM与端到端自动驾驶模型集成时计算开销大、实时决策难的问题。②提出SOLVE框架，通过共享视觉编码器在特征层面实现VLM与E2E模型的知识共享，并设计轨迹链式思维（T-CoT）范式逐步细化轨迹预测，同时采用时间解耦策略协调VLM高质量输出与E2E实时性能。③相比现有方法，创新性地在特征级融合而非仅输出级集成，并通过T-CoT减少预测不确定性。④在nuScenes数据集上显著提升了轨迹预测精度，为更鲁棒的自动驾驶系统铺路。
- **摘要（英）**: This paper addresses the challenge of efficiently integrating Vision-Language Models (VLMs) into end-to-end autonomous driving systems for real-time decision-making. SOLVE proposes a shared visual encoder for feature-level knowledge sharing, a Trajectory Chain-of-Thought (T-CoT) paradigm to refine trajectory predictions, and a temporal decoupling strategy to balance VLM quality with E2E speed. Evaluated on nuScenes, it achieves significant improvements in trajectory prediction accuracy.
- **核心贡献**: 提出SOLVE框架，实现VLM与端到端模型在特征层面的高效协同，并引入T-CoT提升轨迹预测精度。
- **创新点**: 特征级知识共享与时间解耦策略，结合轨迹链式思维，突破传统输出级集成的性能瓶颈。
- **结果**: 在nuScenes上轨迹预测精度显著提升，验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The integration of Vision-Language Models (VLMs) into autonomous driving systems has shown promise in addressing key challenges such as learning complexity, interpretability, and common-sense reasoning. However, existing approaches often struggle with efficient integration and realtime decision-making due to computational demands. In this paper, we introduce SOLVE, an innovative framework that synergizes VLMs with end-to-end (E2E) models to enhance autonomous vehicle planning. Our approach emphasizes knowledge sharing at the feature level through a shared visual encoder, enabling comprehensive interaction between VLM and E2E components. We propose a Trajectory Chain-of-Thought (T-CoT) paradigm, which progressively refines trajectory predictions, reducing uncertainty and improving accuracy. By employing a temporal decoupling strategy, SOLVE achieves efficient cooperation by aligning high-quality VLM outputs with E2E real-time performance. Evaluated on the nuScenes dataset, our method demonstrates significant improvements in trajectory prediction accuracy, paving the way for more robust and reliable autonomous driving systems.

</details>

### JiSAM: Alleviate Labeling Burden and Corner Case Problems in Autonomous Driving via Minimal Real-World Data. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2503.08422](https://arxiv.org/abs/2503.08422) · 📚 被引 2
- **作者**: Runjian Chen, Wenqi Shao, Bo Zhang, Shaoshuai Shi, Li Jiang, Ping Luo
- **🏷️ 机构**: The University of Hong Kong, Shanghai AI Laboratory, Voyager Research, Didi Chuxing
- **会议**: CVPR 2025
- **摘要（中）**: ①针对LiDAR感知中真实标注成本高且缺乏罕见交通参与者（corner cases）的问题。②提出即插即用方法JiSAM，包含抖动增强（Jittering augmentation）、域感知骨干网络（domain-aware backbone）和基于记忆的分区对齐（memory-based Sectorized AlignMent），以高效利用仿真数据并缩小sim-to-real差距。③相比现有域适应方法，JiSAM同时解决仿真数据采样效率和域间隙，且无需修改检测器结构。④在nuScenes上，使用SOTA 3D检测器，仅用2.5%真实标注数据即可达到全量数据训练的性能，并在未见物体上提升超过15 mAP。
- **摘要（英）**: This paper tackles the high annotation cost and lack of corner cases in real LiDAR perception by leveraging simulation data. JiSAM, a plug-and-play method, combines jittering augmentation, a domain-aware backbone, and memory-based sectorized alignment to improve sample efficiency and bridge the sim-to-real gap. On nuScenes, it achieves performance comparable to full-data training using only 2.5% real labels and gains over 15 mAP on unseen objects.
- **核心贡献**: 提出JiSAM方法，通过仿真数据高效利用和域对齐，实现极少真实标注下的高性能3D检测。
- **创新点**: 结合抖动增强、域感知骨干和记忆分区对齐，同时解决仿真数据效率与域间隙问题。
- **结果**: 仅用2.5%真实数据达到全量训练性能，未见物体mAP提升超15点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep-learning-based autonomous driving (AD) perception introduces a promising picture for safe and environment-friendly transportation. However, the over-reliance on real labeled data in LiDAR perception limits the scale of on-road attempts. 3D real world data is notoriously time-and-energy-consuming to annotate and lacks corner cases like rare traffic participants. On the contrary, in simulators like CARLA, generating labeled LiDAR point clouds with corner cases is a piece of cake. However, introducing synthetic point clouds to improve real perception is non-trivial. This stems from two challenges: 1) sample efficiency of simulation datasets 2) simulation-to-real gaps. To overcome both challenges, we propose a plug-and-play method called JiSAM , shorthand for Jittering augmentation, domain-aware backbone and memory-based Sectorized AlignMent. In extensive experiments conducted on the famous AD dataset NuScenes, we demonstrate that, with SOTA 3D object detector, JiSAM is able to utilize the simulation data and only labels on 2.5% available real data to achieve comparable performance to models trained on all real data. Additionally, JiSAM achieves more than 15 mAPs on the objects not labeled in the real training set.

</details>

### Distilling Multi-modal Large Language Models for Autonomous Driving.
- **链接**: [arXiv:2501.09757](https://arxiv.org/abs/2501.09757) · 📚 被引 18
- **作者**: Deepti Hegde, Rajeev Yasarla, Hong Cai, Shizhong Han, Apratim Bhattacharyya, Shweta Mahajan et al.
- **🏷️ 机构**: Johns Hopkins University, Qualcomm AI Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving demands safe motion planning, especially in critical "long-tail" scenarios. Recent end-to-end autonomous driving systems leverage large language models (LLMs) as planners to improve generalizability to rare events. However, using LLMs at test time introduces high computational costs. To address this, we propose DiMA, an end-to-end autonomous driving system that maintains the efficiency of an LLM-free (or vision-based) planner while leveraging the world knowledge of an LLM. DiMA distills the information from a multi-modal LLM to a vision-based end-to-end planner through a set of specially designed surrogate tasks. Under a joint training strategy, a scene encoder common to both networks produces structured representations that are semantically grounded as well as aligned to the final planning objective. Notably, the LLM is optional at inference, enabling robust planning without compromising on efficiency. Training with DiMA results in a 37% reduction in the L2 trajectory error and an 80% reduction in the collision rate of the vision-based planner, as well as a 44% trajectory error reduction in longtail scenarios. DiMA also achieves state-of-the-art performance on the nuScenes planning benchmark.

</details>

### DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving.
- **链接**: [arXiv:2411.15139](https://arxiv.org/abs/2411.15139) · 📚 被引 80
- **作者**: Bencheng Liao, Shaoyu Chen, Haoran Yin, Bo Jiang, Cheng Wang, Sixu Yan et al.
- **🏷️ 机构**: Huazhong University of Science &#x0026; Technology,Institute of Artificial Intelligence, Huazhong University of Science &#x0026; Technology,School of EIC, Horizon Robotics
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the diffusion model has emerged as a powerful generative technique for robotic policy learning, capable of modeling multi-mode action distributions. Leveraging its capability for end-to-end autonomous driving is a promising direction. However, the numerous denoising steps in the robotic diffusion policy and the more dynamic, open-world nature of traffic scenes pose substantial challenges for generating diverse driving actions at a real-time speed. To address these challenges, we propose a novel truncated diffusion policy that incorporates prior multi-mode anchors and truncates the diffusion schedule, enabling the model to learn denoising from anchored Gaussian distribution to the multi-mode driving action distribution. Additionally, we design an efficient cascade diffusion decoder for enhanced interaction with conditional scene context. The proposed model, DiffusionDrive, demonstrates 10$\times$ reduction in denoising steps compared to vanilla diffusion policy, delivering superior diversity and quality in just 2 steps. On the planning-oriented NAVSIM dataset, with the aligned ResNet-34 backbone, DiffusionDrive achieves 88.1 PDMS without bells and whistles, setting a new record, while running at a real-time speed of 45 FPS on an NVIDIA 4090. Qualitative results on challenging scenarios further confirm that DiffusionDrive can robustly generate diverse plausible driving actions. Code and model will be available at https://github.com/hustvl/DiffusionDrive.

</details>

### Critic-V: VLM Critics Help Catch VLM Errors in Multimodal Reasoning.
- **链接**: [arXiv:2411.18203](https://arxiv.org/abs/2411.18203) · 📚 被引 6
- **作者**: Di Zhang, Jingdi Lei, Junxian Li, Xunzhi Wang, Yujie Liu, Zonglin Yang et al.
- **🏷️ 机构**: Fudan University, Shanghai Artificial Intelligence Laboratory, Shanghai Jiaotong University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have shown remarkable advancements in multimodal reasoning tasks. However, they still often generate inaccurate or irrelevant responses due to issues like hallucinated image understandings or unrefined reasoning paths. To address these challenges, we introduce Critic-V, a novel framework inspired by the Actor-Critic paradigm to boost the reasoning capability of VLMs. This framework decouples the reasoning process and critic process by integrating two independent components: the Reasoner, which generates reasoning paths based on visual and textual inputs, and the Critic, which provides constructive critique to refine these paths. In this approach, the Reasoner generates reasoning responses according to text prompts, which can evolve iteratively as a policy based on feedback from the Critic. This interaction process was theoretically driven by a reinforcement learning framework where the Critic offers natural language critiques instead of scalar rewards, enabling more nuanced feedback to boost the Reasoner's capability on complex reasoning tasks. The Critic model is trained using Direct Preference Optimization (DPO), leveraging a preference dataset of critiques ranked by Rule-based Reward~(RBR) to enhance its critic capabilities. Evaluation results show that the Critic-V framework significantly outperforms existing methods, including GPT-4V, on 5 out of 8 benchmarks, especially regarding reasoning accuracy and efficiency. Combining a dynamic text-based policy for the Reasoner and constructive feedback from the preference-optimized Critic enables a more reliable and context-sensitive multimodal reasoning process. Our approach provides a promising solution to enhance the reliability of VLMs, improving their performance in real-world reasoning-heavy multimodal applications such as autonomous driving and embodied intelligence.

</details>

### ModeSeq: Taming Sparse Multimodal Motion Prediction with Sequential Mode Modeling.
- **链接**: [arXiv:2411.11911](https://arxiv.org/abs/2411.11911) · 📚 被引 8
- **作者**: Zikang Zhou, Hengjian Zhou, Haibo Hu, Zihao Wen, Jianping Wang, Yung-Hui Li et al.
- **🏷️ 机构**: City University of Hong Kong, Zhejiang University, Hon Hai Research Institute
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anticipating the multimodality of future events lays the foundation for safe autonomous driving. However, multimodal motion prediction for traffic agents has been clouded by the lack of multimodal ground truth. Existing works predominantly adopt the winner-take-all training strategy to tackle this challenge, yet still suffer from limited trajectory diversity and uncalibrated mode confidence. While some approaches address these limitations by generating excessive trajectory candidates, they necessitate a post-processing stage to identify the most representative modes, a process lacking universal principles and compromising trajectory accuracy. We are thus motivated to introduce ModeSeq, a new multimodal prediction paradigm that models modes as sequences. Unlike the common practice of decoding multiple plausible trajectories in one shot, ModeSeq requires motion decoders to infer the next mode step by step, thereby more explicitly capturing the correlation between modes and significantly enhancing the ability to reason about multimodality. Leveraging the inductive bias of sequential mode prediction, we also propose the Early-Match-Take-All (EMTA) training strategy to diversify the trajectories further. Without relying on dense mode prediction or heuristic post-processing, ModeSeq considerably improves the diversity of multimodal output while attaining satisfactory trajectory accuracy, resulting in balanced performance on motion prediction benchmarks. Moreover, ModeSeq naturally emerges with the capability of mode extrapolation, which supports forecasting more behavior modes when the future is highly uncertain.

</details>

### VoteFlow: Enforcing Local Rigidity in Self-Supervised Scene Flow.
- **链接**: [arXiv:2503.22328](https://arxiv.org/abs/2503.22328) · 📚 被引 5
- **作者**: Yancong Lin, Shiming Wang, Liangliang Nan, Julian F. P. Kooij, Holger Caesar
- **🏷️ 机构**: TU Delft
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene flow estimation aims to recover per-point motion from two adjacent LiDAR scans. However, in real-world applications such as autonomous driving, points rarely move independently of others, especially for nearby points belonging to the same object, which often share the same motion. Incorporating this locally rigid motion constraint has been a key challenge in self-supervised scene flow estimation, which is often addressed by post-processing or appending extra regularization. While these approaches are able to improve the rigidity of predicted flows, they lack an architectural inductive bias for local rigidity within the model structure, leading to suboptimal learning efficiency and inferior performance. In contrast, we enforce local rigidity with a lightweight add-on module in neural network design, enabling end-to-end learning. We design a discretized voting space that accommodates all possible translations and then identify the one shared by nearby points by differentiable voting. Additionally, to ensure computational efficiency, we operate on pillars rather than points and learn representative features for voting per pillar. We plug the Voting Module into popular model designs and evaluate its benefit on Argoverse 2 and Waymo datasets. We outperform baseline works with only marginal compute overhead. Code is available at https://github.com/tudelft-iv/VoteFlow.

</details>

### Mixed Signals: A Diverse Point Cloud Dataset for Heterogeneous LiDAR V2X Collaboration.
- **链接**: [arXiv:2502.14156](https://arxiv.org/abs/2502.14156)
- **作者**: Katie Z. Luo, Minh-Quan Dao, Zhenzhen Liu, Mark E. Campbell, Wei-Lun Chao, Kilian Q. Weinberger et al.
- **🏷️ 机构**: Cornell University, Inria, The Ohio State University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vehicle-to-everything (V2X) collaborative perception has emerged as a promising solution to address the limitations of single-vehicle perception systems. However, existing V2X datasets are limited in scope, diversity, and quality. To address these gaps, we present Mixed Signals, a comprehensive V2X dataset featuring 45.1k point clouds and 240.6k bounding boxes collected from three connected autonomous vehicles (CAVs) equipped with two different configurations of LiDAR sensors, plus a roadside unit with dual LiDARs. Our dataset provides point clouds and bounding box annotations across 10 classes, ensuring reliable data for perception training. We provide detailed statistical analysis on the quality of our dataset and extensively benchmark existing V2X methods on it. The Mixed Signals dataset is ready-to-use, with precise alignment and consistent annotations across time and viewpoints. Dataset website is available at https://mixedsignalsdataset.cs.cornell.edu/.

</details>

### Hints of Prompt: Enhancing Visual Representation for Multimodal LLMs in Autonomous Driving.
- **链接**: [arXiv:2411.13076](https://arxiv.org/abs/2411.13076)
- **作者**: Hao Zhou, Zhanning Gao, Zhili Chen, Maosheng Ye, Qifeng Chen, Tongyi Cao et al.
- **🏷️ 机构**: University of Chinese Academy of Sciences,Beijing,China, DeepRoute.AI,Shenzhen,China, The Hong Kong University of Science and Technology,Hong Kong,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In light of the dynamic nature of autonomous driving environments and stringent safety requirements, general MLLMs combined with CLIP alone often struggle to accurately represent driving-specific scenarios, particularly in complex interactions and long-tail cases. To address this, we propose the Hints of Prompt (HoP) framework, which introduces three key enhancements: Affinity hint to emphasize instance-level structure by strengthening token-wise connections, Semantic hint to incorporate high-level information relevant to driving-specific cases, such as complex interactions among vehicles and traffic signs, and Question hint to align visual features with the query context, focusing on question-relevant regions. These hints are fused through a Hint Fusion module, enriching visual representations by capturing driving-related representations with limited domain data, ensuring faster adaptation to driving scenarios. Extensive experiments confirm the effectiveness of the HoP framework, showing that it significantly outperforms previous state-of-the-art methods in all key metrics.

</details>

### AD-GS: Object-Aware B-Spline Gaussian Splatting for Self-Supervised Autonomous Driving.
- **链接**: [arXiv:2507.12137](https://arxiv.org/abs/2507.12137) · 📚 被引 1
- **作者**: Jiawei Xu, Kai Deng, Zexin Fan, Shenlong Wang, Jin Xie, Jian Yang
- **🏷️ 机构**: College of Computer Science, Nankai University, University of Illinois Urbana-Champaign, School of Intelligence Science and Technology, Nanjing University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modeling and rendering dynamic urban driving scenes is crucial for self-driving simulation. Current high-quality methods typically rely on costly manual object tracklet annotations, while self-supervised approaches fail to capture dynamic object motions accurately and decompose scenes properly, resulting in rendering artifacts. We introduce AD-GS, a novel self-supervised framework for high-quality free-viewpoint rendering of driving scenes from a single log. At its core is a novel learnable motion model that integrates locality-aware B-spline curves with global-aware trigonometric functions, enabling flexible yet precise dynamic object modeling. Rather than requiring comprehensive semantic labeling, AD-GS automatically segments scenes into objects and background with the simplified pseudo 2D segmentation, representing objects using dynamic Gaussians and bidirectional temporal visibility masks. Further, our model incorporates visibility reasoning and physically rigid regularization to enhance robustness. Extensive evaluations demonstrate that our annotation-free model significantly outperforms current state-of-the-art annotation-free methods and is competitive with annotation-dependent approaches.

</details>

### AMD: Adaptive Momentum and Decoupled Contrastive Learning Framework for Robust Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2507.01801](https://arxiv.org/abs/2507.01801) · 📚 被引 1
- **作者**: Bin Rao, Haicheng Liao, Yanchen Guan, Chengyue Wang, Bonan Wang, Jiaxun Zhang et al.
- **🏷️ 机构**: University of Macau,State Key Laboratory of Internet of Things for Smart City
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately predicting the future trajectories of traffic agents is essential in autonomous driving. However, due to the inherent imbalance in trajectory distributions, tail data in natural datasets often represents more complex and hazardous scenarios. Existing studies typically rely solely on a base model's prediction error, without considering the diversity and uncertainty of long-tail trajectory patterns. We propose an adaptive momentum and decoupled contrastive learning framework (AMD), which integrates unsupervised and supervised contrastive learning strategies. By leveraging an improved momentum contrast learning (MoCo-DT) and decoupled contrastive learning (DCL) module, our framework enhances the model's ability to recognize rare and complex trajectories. Additionally, we design four types of trajectory random augmentation methods and introduce an online iterative clustering strategy, allowing the model to dynamically update pseudo-labels and better adapt to the distributional shifts in long-tail data. We propose three different criteria to define long-tail trajectories and conduct extensive comparative experiments on the nuScenes and ETH$/$UCY datasets. The results show that AMD not only achieves optimal performance in long-tail trajectory prediction but also demonstrates outstanding overall prediction accuracy.

</details>

### Navigation-Guided Sparse Scene Representation for End-to-End Autonomous Driving.
- **链接**: [出版页](https://openreview.net/forum?id=Vv76fCYffN)
- **作者**: Peidong Li, Dixiao Cui
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Enhancing End-to-End Autonomous Driving with Latent World Model.
- **链接**: [arXiv:2406.08481](https://arxiv.org/abs/2406.08481)
- **作者**: Yingyan Li, Lue Fan, Jiawei He, Yuqi Wang, Yuntao Chen, Zhaoxiang Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, end-to-end planners directly utilize raw sensor data, enabling them to extract richer scene features and reduce information loss compared to traditional planners. This raises a crucial research question: how can we develop better scene feature representations to fully leverage sensor data in end-to-end driving? Self-supervised learning methods show great success in learning rich feature representations in NLP and computer vision. Inspired by this, we propose a novel self-supervised learning approach using the LAtent World model (LAW) for end-to-end driving. LAW predicts future scene features based on current features and ego trajectories. This self-supervised task can be seamlessly integrated into perception-free and perception-based frameworks, improving scene feature learning and optimizing trajectory prediction. LAW achieves state-of-the-art performance across multiple benchmarks, including real-world open-loop benchmark nuScenes, NAVSIM, and simulator-based closed-loop benchmark CARLA. The code is released at https://github.com/BraveGroup/LAW.

</details>

### AdaWM: Adaptive World Model based Planning for Autonomous Driving.
- **链接**: [出版页](https://openreview.net/forum?id=NEu8wgPctU)
- **作者**: Hang Wang, Xin Ye, Feng Tao, Chenbin Pan, Abhirup Mallik, Burhaneddin Yaman et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Glad: A Streaming Scene Generator for Autonomous Driving.
- **链接**: [arXiv:2503.00045](https://arxiv.org/abs/2503.00045)
- **作者**: Bin Xie, Yingfei Liu, Tiancai Wang, Jiale Cao, Xiangyu Zhang
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The generation and simulation of diverse real-world scenes have significant application value in the field of autonomous driving, especially for the corner cases. Recently, researchers have explored employing neural radiance fields or diffusion models to generate novel views or synthetic data under driving scenes. However, these approaches suffer from unseen scenes or restricted video length, thus lacking sufficient adaptability for data generation and simulation. To address these issues, we propose a simple yet effective framework, named Glad, to generate video data in a frame-by-frame style. To ensure the temporal consistency of synthetic video, we introduce a latent variable propagation module, which views the latent features of previous frame as noise prior and injects it into the latent features of current frame. In addition, we design a streaming data sampler to orderly sample the original image in a video clip at continuous iterations. Given the reference frame, our Glad can be viewed as a streaming simulator by generating the videos for specific scenes. Extensive experiments are performed on the widely-used nuScenes dataset. Experimental results demonstrate that our proposed Glad achieves promising performance, serving as a strong baseline for online video generation. We will release the source code and models publicly.

</details>

### Trajectory-LLM: A Language-based Data Generator for Trajectory Prediction in Autonomous Driving.
- **链接**: [出版页](https://openreview.net/forum?id=UapxTvxB3N)
- **作者**: Kairui Yang, Zihao Guo, Gengjie Lin, Haotian Dong, Zhao Huang, Yipeng Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Diffusion-Based Planning for Autonomous Driving with Flexible Guidance.
- **链接**: [arXiv:2501.15564](https://arxiv.org/abs/2501.15564)
- **作者**: Yinan Zheng, Ruiming Liang, Kexin Zheng, Jinliang Zheng, Liyuan Mao, Jianxiong Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Achieving human-like driving behaviors in complex open-world environments is a critical challenge in autonomous driving. Contemporary learning-based planning approaches such as imitation learning methods often struggle to balance competing objectives and lack of safety assurance,due to limited adaptability and inadequacy in learning complex multi-modal behaviors commonly exhibited in human planning, not to mention their strong reliance on the fallback strategy with predefined rules. We propose a novel transformer-based Diffusion Planner for closed-loop planning, which can effectively model multi-modal driving behavior and ensure trajectory quality without any rule-based refinement. Our model supports joint modeling of both prediction and planning tasks under the same architecture, enabling cooperative behaviors between vehicles. Moreover, by learning the gradient of the trajectory score function and employing a flexible classifier guidance mechanism, Diffusion Planner effectively achieves safe and adaptable planning behaviors. Evaluations on the large-scale real-world autonomous planning benchmark nuPlan and our newly collected 200-hour delivery-vehicle driving dataset demonstrate that Diffusion Planner achieves state-of-the-art closed-loop performance with robust transferability in diverse driving styles.

</details>

### Hierarchically Encapsulated Representation for Protocol Design in Self-Driving Labs.
- **链接**: [arXiv:2504.03810](https://arxiv.org/abs/2504.03810)
- **作者**: Yu-Zhe Shi, Mingchen Liu, Fanxu Meng, Qiao Xu, Zhangqian Bi, Kun He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-driving laboratories have begun to replace human experimenters in performing single experimental skills or predetermined experimental protocols. However, as the pace of idea iteration in scientific research has been intensified by Artificial Intelligence, the demand for rapid design of new protocols for new discoveries become evident. Efforts to automate protocol design have been initiated, but the capabilities of knowledge-based machine designers, such as Large Language Models, have not been fully elicited, probably for the absence of a systematic representation of experimental knowledge, as opposed to isolated, flatten pieces of information. To tackle this issue, we propose a multi-faceted, multi-scale representation, where instance actions, generalized operations, and product flow models are hierarchically encapsulated using Domain-Specific Languages. We further develop a data-driven algorithm based on non-parametric modeling that autonomously customizes these representations for specific domains. The proposed representation is equipped with various machine designers to manage protocol design tasks, including planning, modification, and adjustment. The results demonstrate that the proposed method could effectively complement Large Language Models in the protocol design process, serving as an auxiliary module in the realm of machine-assisted scientific exploration.

</details>

### MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models.
- **链接**: [arXiv:2503.14827](https://arxiv.org/abs/2503.14827)
- **作者**: Chejian Xu, Jiawei Zhang, Zhaorun Chen, Chulin Xie, Mintong Kang, Yujin Potter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal foundation models (MMFMs) play a crucial role in various applications, including autonomous driving, healthcare, and virtual assistants. However, several studies have revealed vulnerabilities in these models, such as generating unsafe content by text-to-image models. Existing benchmarks on multimodal models either predominantly assess the helpfulness of these models, or only focus on limited perspectives such as fairness and privacy. In this paper, we present the first unified platform, MMDT (Multimodal DecodingTrust), designed to provide a comprehensive safety and trustworthiness evaluation for MMFMs. Our platform assesses models from multiple perspectives, including safety, hallucination, fairness/bias, privacy, adversarial robustness, and out-of-distribution (OOD) generalization. We have designed various evaluation scenarios and red teaming algorithms under different tasks for each perspective to generate challenging data, forming a high-quality benchmark. We evaluate a range of multimodal models using MMDT, and our findings reveal a series of vulnerabilities and areas for improvement across these perspectives. This work introduces the first comprehensive and unique safety and trustworthiness evaluation platform for MMFMs, paving the way for developing safer and more reliable MMFMs and systems. Our platform and benchmark are available at https://mmdecodingtrust.github.io/.

</details>

### SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25cm.html)
- **作者**: Jiawei Zhang, Xuan Yang, Taiqi Wang, Yu Yao, Aleksandr Petiushko, Bo Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### HCRMP: An LLM-Hinted Contextual Reinforcement Learning Framework for Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9851fb4a60b303319c66d86c36c3a0ef-Abstract-Conference.html)
- **作者**: Zhiwen Chen, Hanming Deng, Zhuoren Li, Huanxi Wen, Guizhe Jin, Ran Yu et al.
- **🏷️ 机构**: Tongji University, Sensetime
- **会议**: NeurIPS 2025

### Temporal Logic-Based Multi-Vehicle Backdoor Attacks against Offline RL Agents in End-to-end Autonomous Driving.
- **链接**: [arXiv:2509.16950](https://arxiv.org/abs/2509.16950)
- **作者**: Xuan Chen, Shiwei Feng, Zikang Xiong, Shengwei An, Yunshu Mao, Lu Yan et al.
- **🏷️ 机构**: Purdue University, DeepRoute.ai, Virginia Polytechnic Institute and State University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Assessing the safety of autonomous driving (AD) systems against security threats, particularly backdoor attacks, is a stepping stone for real-world deployment. However, existing works mainly focus on pixel-level triggers that are impractical to deploy in the real world. We address this gap by introducing a novel backdoor attack against the end-to-end AD systems that leverage one or more other vehicles' trajectories as triggers. To generate precise trigger trajectories, we first use temporal logic (TL) specifications to define the behaviors of attacker vehicles. Configurable behavior models are then used to generate these trajectories, which are quantitatively evaluated and iteratively refined based on the TL specifications. We further develop a negative training strategy by incorporating patch trajectories that are similar to triggers but are designated not to activate the backdoor. It enhances the stealthiness of the attack and refines the system's responses to trigger scenarios. Through extensive experiments on 5 offline reinforcement learning (RL) driving agents with 6 trigger patterns and target action combinations, we demonstrate the flexibility and effectiveness of our proposed attack, showing the under-exploration of existing end-to-end AD systems' vulnerabilities to such trajectory-based backdoor attacks.

</details>

### TopoPoint: Enhance Topology Reasoning via Endpoint Detection in Autonomous Driving.
- **链接**: [arXiv:2505.17771](https://arxiv.org/abs/2505.17771)
- **作者**: Yanping Fu, Xinyuan Liu, Tianyu Li, Yike Ma, Yucheng Zhang, Feng Dai
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences, University of Electronic Science and Technology of China, The Institute of Computing Technology of the Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Topology reasoning, which unifies perception and structured reasoning, plays a vital role in understanding intersections for autonomous driving. However, its performance heavily relies on the accuracy of lane detection, particularly at connected lane endpoints. Existing methods often suffer from lane endpoints deviation, leading to incorrect topology construction. To address this issue, we propose TopoPoint, a novel framework that explicitly detects lane endpoints and jointly reasons over endpoints and lanes for robust topology reasoning. During training, we independently initialize point and lane query, and proposed Point-Lane Merge Self-Attention to enhance global context sharing through incorporating geometric distances between points and lanes as an attention mask . We further design Point-Lane Graph Convolutional Network to enable mutual feature aggregation between point and lane query. During inference, we introduce Point-Lane Geometry Matching algorithm that computes distances between detected points and lanes to refine lane endpoints, effectively mitigating endpoint deviation. Extensive experiments on the OpenLane-V2 benchmark demonstrate that TopoPoint achieves state-of-the-art performance in topology reasoning (48.8 on OLS). Additionally, we propose DET$_p$ to evaluate endpoint detection, under which our method significantly outperforms existing approaches (52.6 v.s. 45.2 on DET$_p$). The code is released at https://github.com/Franpin/TopoPoint.

</details>

### Prioritizing Perception-Guided Self-Supervision: A New Paradigm for Causal Modeling in End-to-End Autonomous Driving.
- **链接**: [arXiv:2511.08214](https://arxiv.org/abs/2511.08214)
- **作者**: Yi Huang, Zhan Qu, Lihui Jiang, Bingbing Liu, Hongbo Zhang
- **🏷️ 机构**: The Chinese University of Hong Kong, Huawei Technologies Ltd., Huawei
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving systems, predominantly trained through imitation learning, have demonstrated considerable effectiveness in leveraging large-scale expert driving data. Despite their success in open-loop evaluations, these systems often exhibit significant performance degradation in closed-loop scenarios due to causal confusion. This confusion is fundamentally exacerbated by the overreliance of the imitation learning paradigm on expert trajectories, which often contain unattributable noise and interfere with the modeling of causal relationships between environmental contexts and appropriate driving actions. To address this fundamental limitation, we propose Perception-Guided Self-Supervision (PGS) - a simple yet effective training paradigm that leverages perception outputs as the primary supervisory signals, explicitly modeling causal relationships in decision-making. The proposed framework aligns both the inputs and outputs of the decision-making module with perception results, such as lane centerlines and the predicted motions of surrounding agents, by introducing positive and negative self-supervision for the ego trajectory. This alignment is specifically designed to mitigate causal confusion arising from the inherent noise in expert trajectories. Equipped with perception-driven supervision, our method, built on a standard end-to-end architecture, achieves a Driving Score of 78.08 and a mean success rate of 48.64% on the challenging closed-loop Bench2Drive benchmark, significantly outperforming existing state-of-the-art methods, including those employing more complex network architectures and inference pipelines. These results underscore the effectiveness and robustness of the proposed PGS framework and point to a promising direction for addressing causal confusion and enhancing real-world generalization in autonomous driving.

</details>

### Model-Based Policy Adaptation for Closed-Loop End-to-end Autonomous Driving.
- **链接**: [arXiv:2511.21584](https://arxiv.org/abs/2511.21584)
- **作者**: Haohong Lin, Yunzhi Zhang, Wenhao Ding, Jiajun Wu, Ding Zhao
- **🏷️ 机构**: CMU, Stanford University, Imperial College London
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end (E2E) autonomous driving models have demonstrated strong performance in open-loop evaluations but often suffer from cascading errors and poor generalization in closed-loop settings. To address this gap, we propose Model-based Policy Adaptation (MPA), a general framework that enhances the robustness and safety of pretrained E2E driving agents during deployment. MPA first generates diverse counterfactual trajectories using a geometry-consistent simulation engine, exposing the agent to scenarios beyond the original dataset. Based on this generated data, MPA trains a diffusion-based policy adapter to refine the base policy's predictions and a multi-step Q value model to evaluate long-term outcomes. At inference time, the adapter proposes multiple trajectory candidates, and the Q value model selects the one with the highest expected utility. Experiments on the nuScenes benchmark using a photorealistic closed-loop simulator demonstrate that MPA significantly improves performance across in-domain, out-of-domain, and safety-critical scenarios. We further investigate how the scale of counterfactual data and inference-time guidance strategies affect overall effectiveness.

</details>

### Embodied Cognition Augmented End2End Autonomous Driving.
- **链接**: [arXiv:2511.01334](https://arxiv.org/abs/2511.01334)
- **作者**: Ling Niu, Xiaoji Zheng, Han Wang, Ziyuan Yang, Chen Zheng, Bokui Chen et al.
- **🏷️ 机构**: Tsinghua University, University of Washington, Tsinghua University, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, vision-based end-to-end autonomous driving has emerged as a new paradigm. However, popular end-to-end approaches typically rely on visual feature extraction networks trained under label supervision. This limited supervision framework restricts the generality and applicability of driving models. In this paper, we propose a novel paradigm termed $E^{3}AD$, which advocates for comparative learning between visual feature extraction networks and the general EEG large model, in order to learn latent human driving cognition for enhancing end-to-end planning. In this work, we collected a cognitive dataset for the mentioned contrastive learning process. Subsequently, we investigated the methods and potential mechanisms for enhancing end-to-end planning with human driving cognition, using popular driving models as baselines on publicly available autonomous driving datasets. Both open-loop and closed-loop tests are conducted for a comprehensive evaluation of planning performance. Experimental results demonstrate that the $E^{3}AD$ paradigm significantly enhances the end-to-end planning performance of baseline models. Ablation studies further validate the contribution of driving cognition and the effectiveness of comparative learning process. To the best of our knowledge, this is the first work to integrate human driving cognition for improving end-to-end autonomous driving planning. It represents an initial attempt to incorporate embodied cognitive data into end-to-end autonomous driving, providing valuable insights for future brain-inspired autonomous driving systems. Our code will be made available at Github

</details>

### DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving.
- **链接**: [arXiv:2509.17940](https://arxiv.org/abs/2509.17940)
- **作者**: Shuyao Shang, Yuntao Chen, Yuqi Wang, Yingyan Li, Zhao-Xiang Zhang
- **🏷️ 机构**: Institute of automation, Chinese academy of science, Centre for Artificial Intelligence and Robotics, HKISI, CAS, Petuum Inc.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving has substantially progressed by directly predicting future trajectories from raw perception inputs, which bypasses traditional modular pipelines. However, mainstream methods trained via imitation learning suffer from critical safety limitations, as they fail to distinguish between trajectories that appear human-like but are potentially unsafe. Some recent approaches attempt to address this by regressing multiple rule-driven scores but decoupling supervision from policy optimization, resulting in suboptimal performance. To tackle these challenges, we propose DriveDPO, a Safety Direct Preference Optimization Policy Learning framework. First, we distill a unified policy distribution from human imitation similarity and rule-based safety scores for direct policy optimization. Further, we introduce an iterative Direct Preference Optimization stage formulated as trajectory-level preference alignment. Extensive experiments on the NAVSIM benchmark demonstrate that DriveDPO achieves a new state-of-the-art PDMS of 90.0. Furthermore, qualitative results across diverse challenging scenarios highlight DriveDPO's ability to produce safer and more reliable driving behaviors.

</details>

### Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling.
- **链接**: [arXiv:2510.11083](https://arxiv.org/abs/2510.11083) · 📚 被引 2
- **作者**: Tianyi Tan, Yinan Zheng, Ruiming Liang, Zexu Wang, Kexin Zheng, Jinliang Zheng et al.
- **🏷️ 机构**: Tsinghua University, Institute of Automation, Chinese Academy of Sciences, The Chinese University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modeling interactive driving behaviors in complex scenarios remains a fundamental challenge for autonomous driving planning. Learning-based approaches attempt to address this challenge with advanced generative models, removing the dependency on over-engineered architectures for representation fusion. However, brute-force implementation by simply stacking transformer blocks lacks a dedicated mechanism for modeling interactive behaviors that are common in real driving scenarios. The scarcity of interactive driving data further exacerbates this problem, leaving conventional imitation learning methods ill-equipped to capture high-value interactive behaviors. We propose Flow Planner, which tackles these problems through coordinated innovations in data modeling, model architecture, and learning scheme. Specifically, we first introduce fine-grained trajectory tokenization, which decomposes the trajectory into overlapping segments to decrease the complexity of whole trajectory modeling. With a sophisticatedly designed architecture, we achieve efficient temporal and spatial fusion of planning and scene information, to better capture interactive behaviors. In addition, the framework incorporates flow matching with classifier-free guidance for multi-modal behavior generation, which dynamically reweights agent interactions during inference to maintain coherent response strategies, providing a critical boost for interactive scenario understanding. Experimental results on the large-scale nuPlan dataset and challenging interactive interPlan dataset demonstrate that Flow Planner achieves state-of-the-art performance among learning-based approaches while effectively modeling interactive behaviors in complex driving scenarios.

</details>

### Towards Physics-informed Spatial Intelligence with Human Priors: An Autonomous Driving Pilot Study.
- **链接**: [arXiv:2510.21160](https://arxiv.org/abs/2510.21160)
- **作者**: Guanlin Wu, Boyan Su, Yang Zhao, Pu Wang, Yichen Lin, Hao (Frank) Yang
- **🏷️ 机构**: Johns Hopkins University, University of Minnesota - Twin Cities, Mitsubishi Electric Research Labs
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How to integrate and verify spatial intelligence in foundation models remains an open challenge. Current practice often proxies Visual-Spatial Intelligence (VSI) with purely textual prompts and VQA-style scoring, which obscures geometry, invites linguistic shortcuts, and weakens attribution to genuinely spatial skills. We introduce Spatial Intelligence Grid (SIG): a structured, grid-based schema that explicitly encodes object layouts, inter-object relations, and physically grounded priors. As a complementary channel to text, SIG provides a faithful, compositional representation of scene structure for foundation-model reasoning. Building on SIG, we derive SIG-informed evaluation metrics that quantify a model's intrinsic VSI, which separates spatial capability from language priors. In few-shot in-context learning with state-of-the-art multimodal LLMs (e.g. GPT- and Gemini-family models), SIG yields consistently larger, more stable, and more comprehensive gains across all VSI metrics compared to VQA-only representations, indicating its promise as a data-labeling and training schema for learning VSI. We also release SIGBench, a benchmark of 1.4K driving frames annotated with ground-truth SIG labels and human gaze traces, supporting both grid-based machine VSI tasks and attention-driven, human-like VSI tasks in autonomous-driving scenarios.

</details>

### ReSim: Reliable World Simulation for Autonomous Driving.
- **链接**: [arXiv:2506.09981](https://arxiv.org/abs/2506.09981)
- **作者**: Jiazhi Yang, Kashyap Chitta, Shenyuan Gao, Long Chen, Yuqian Shao, Xiaosong Jia et al.
- **🏷️ 机构**: NVIDIA, Hong Kong University of Science and Technology, Shanghai Jiaotong University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How can we reliably simulate future driving scenarios under a wide range of ego driving behaviors? Recent driving world models, developed exclusively on real-world driving data composed mainly of safe expert trajectories, struggle to follow hazardous or non-expert behaviors, which are rare in such data. This limitation restricts their applicability to tasks such as policy evaluation. In this work, we address this challenge by enriching real-world human demonstrations with diverse non-expert data collected from a driving simulator (e.g., CARLA), and building a controllable world model trained on this heterogeneous corpus. Starting with a video generator featuring a diffusion transformer architecture, we devise several strategies to effectively integrate conditioning signals and improve prediction controllability and fidelity. The resulting model, ReSim, enables Reliable Simulation of diverse open-world driving scenarios under various actions, including hazardous non-expert ones. To close the gap between high-fidelity simulation and applications that require reward signals to judge different actions, we introduce a Video2Reward module that estimates a reward from ReSim's simulated future. Our ReSim paradigm achieves up to 44% higher visual fidelity, improves controllability for both expert and non-expert actions by over 50%, and boosts planning and policy selection performance on NAVSIM by 2% and 25%, respectively.

</details>

### CodeMerge: Codebook-Guided Model Merging for Robust Test-Time Adaptation in Autonomous Driving.
- **链接**: [arXiv:2505.16524](https://arxiv.org/abs/2505.16524)
- **作者**: Huitong Yang, Zhuoxiao Chen, Fengyi Zhang, Zi Huang, Yadan Luo
- **🏷️ 机构**: The University of Queensland, University of Queensland
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Maintaining robust 3D perception under dynamic and unpredictable test-time conditions remains a critical challenge for autonomous driving systems. Existing test-time adaptation (TTA) methods often fail in high-variance tasks like 3D object detection due to unstable optimization and sharp minima. While recent model merging strategies based on linear mode connectivity (LMC) offer improved stability by interpolating between fine-tuned checkpoints, they are computationally expensive, requiring repeated checkpoint access and multiple forward passes. In this paper, we introduce CodeMerge, a lightweight and scalable model merging framework that bypasses these limitations by operating in a compact latent space. Instead of loading full models, CodeMerge represents each checkpoint with a low-dimensional fingerprint derived from the source model's penultimate features and constructs a key-value codebook. We compute merging coefficients using ridge leverage scores on these fingerprints, enabling efficient model composition without compromising adaptation quality. Our method achieves strong performance across challenging benchmarks, improving end-to-end 3D detection 14.9% NDS on nuScenes-C and LiDAR-based detection by over 7.6% mAP on nuScenes-to-KITTI, while benefiting downstream tasks such as online mapping, motion prediction and planning even without training. Code and pretrained models are released in the supplementary material.

</details>

### Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2).
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/c2915bc5961edb04e209a524ec167522-Abstract-Conference.html)
- **作者**: Zhenjie Yang, Xiaosong Jia, Qifeng Li, Xue Yang, Maoqing Yao, Junchi Yan
- **🏷️ 机构**: Shanghai Jiao Tong University, University of California, Berkeley, Shanghai Jiaotong University
- **会议**: NeurIPS 2025

### FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/61466f2c7a87edfa5898665c70af0e90-Abstract-Conference.html) · 📚 被引 2
- **作者**: Shuang Zeng, Xinyuan Chang, Mengwei Xie, Xinran Liu, Yifan Bai, Zheng Pan et al.
- **🏷️ 机构**: Xi'an Jiaotong University, Alibaba Group, Tongji University
- **会议**: NeurIPS 2025

### CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/66d09284cfb6f125fe888f71dc14f35e-Abstract-Conference.html)
- **作者**: Dapeng Zhang, Fei Shen, Rui Zhao, Yinda Chen, Peng Zhi, Chenyang Li et al.
- **🏷️ 机构**: Lanzhou University, Nanjing University of Science and Technology, University of science and technology of China
- **会议**: NeurIPS 2025

### SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving.
- **链接**: [arXiv:2509.16588](https://arxiv.org/abs/2509.16588)
- **作者**: Haiming Zhang, Yiyao Zhu, Wending Zhou, Xu Yan, Yingjie Cai, Bingbing Liu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Shenzhen, Hong Kong University of Science and Technology, The Chinese University of Hongkong, Shenzhen
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse Perception Models (SPMs) adopt a query-driven paradigm that forgoes explicit dense BEV or volumetric construction, enabling highly efficient computation and accelerated inference. In this paper, we introduce SQS, a novel query-based splatting pre-training specifically designed to advance SPMs in autonomous driving. SQS introduces a plug-in module that predicts 3D Gaussian representations from sparse queries during pre-training, leveraging self-supervised splatting to learn fine-grained contextual features through the reconstruction of multi-view images and depth maps. During fine-tuning, the pre-trained Gaussian queries are seamlessly integrated into downstream networks via query interaction mechanisms that explicitly connect pre-trained queries with task-specific queries, effectively accommodating the diverse requirements of occupancy prediction and 3D object detection. Extensive experiments on autonomous driving benchmarks demonstrate that SQS delivers considerable performance gains across multiple query-based 3D perception tasks, notably in occupancy prediction and 3D object detection, outperforming prior state-of-the-art pre-training approaches by a significant margin (i.e., +1.3 mIoU on occupancy prediction and +1.0 NDS on 3D detection).

</details>

### AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning.
- **链接**: [arXiv:2506.13757](https://arxiv.org/abs/2506.13757) · 📚 被引 3
- **作者**: Zewei Zhou, Tianhui Cai, Seth Z. Zhao, Yun Zhang, Zhiyu Huang, Bolei Zhou et al.
- **🏷️ 机构**: University of California, Los Angeles, UCLA Computer Science Department, University of California, Los Angeles, UCLA
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in Vision-Language-Action (VLA) models have shown promise for end-to-end autonomous driving by leveraging world knowledge and reasoning capabilities. However, current VLA models often struggle with physically infeasible action outputs, complex model structures, or unnecessarily long reasoning. In this paper, we propose AutoVLA, a novel VLA model that unifies reasoning and action generation within a single autoregressive generation model for end-to-end autonomous driving. AutoVLA performs semantic reasoning and trajectory planning directly from raw visual inputs and language instructions. We tokenize continuous trajectories into discrete, feasible actions, enabling direct integration into the language model. For training, we employ supervised fine-tuning to equip the model with dual thinking modes: fast thinking (trajectory-only) and slow thinking (enhanced with chain-of-thought reasoning). To further enhance planning performance and efficiency, we introduce a reinforcement fine-tuning method based on Group Relative Policy Optimization (GRPO), reducing unnecessary reasoning in straightforward scenarios. Extensive experiments across real-world and simulated datasets and benchmarks, including nuPlan, nuScenes, Waymo, and CARLA, demonstrate the competitive performance of AutoVLA in both open-loop and closed-loop settings. Qualitative results showcase the adaptive reasoning and accurate planning capabilities of AutoVLA in diverse scenarios.

</details>

### VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting.
- **链接**: [arXiv:2510.23205](https://arxiv.org/abs/2510.23205)
- **作者**: Hoonhee Cho, Jae-Young Kang, Giwon Lee, Hyemin Yang, Heejun Park, Seokwoo Jung et al.
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology, KAIST, Korea Advanced Institute of Science &amp; Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving (E2E-AD) has emerged as a promising paradigm that unifies perception, prediction, and planning into a holistic, data-driven framework. However, achieving robustness to varying camera viewpoints, a common real-world challenge due to diverse vehicle configurations, remains an open problem. In this work, we propose VR-Drive, a novel E2E-AD framework that addresses viewpoint generalization by jointly learning 3D scene reconstruction as an auxiliary task to enable planning-aware view synthesis. Unlike prior scene-specific synthesis approaches, VR-Drive adopts a feed-forward inference strategy that supports online training-time augmentation from sparse views without additional annotations. To further improve viewpoint consistency, we introduce a viewpoint-mixed memory bank that facilitates temporal interaction across multiple viewpoints and a viewpoint-consistent distillation strategy that transfers knowledge from original to synthesized views. Trained in a fully end-to-end manner, VR-Drive effectively mitigates synthesis-induced noise and improves planning under viewpoint shifts. In addition, we release a new benchmark dataset to evaluate E2E-AD performance under novel camera viewpoints, enabling comprehensive analysis. Our results demonstrate that VR-Drive is a scalable and robust solution for the real-world deployment of end-to-end autonomous driving systems.

</details>

### RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2ed3a566a0af6dcec424b988f1880ecc-Abstract-Conference.html) · 📚 被引 2
- **作者**: Hao Gao, Shaoyu Chen, Bo Jiang, Bencheng Liao, Yiang Shi, Xiaoyang Guo et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Anhui University, Horizon Robotics
- **会议**: NeurIPS 2025

### SURDS: Benchmarking Spatial Understanding and Reasoning in Driving Scenarios with Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b80285c98ad292e378e31ae18d0fcc1b-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Xianda Guo, Ruijun Zhang, Yiqun Duan, Yuhang He, Dujun Nie, Wenke Huang et al.
- **🏷️ 机构**: Meta, State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences; School of Artificial Intelligence, University of Chinese Academy of Sciences, University of Technology Sydney
- **会议**: NeurIPS 2025

### DiffE2E: Rethinking End-to-End Driving with a Hybrid Diffusion-Regression-Classification Policy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/61162d94822d468ee6e92803340f2040-Abstract-Conference.html)
- **作者**: Rui Zhao, Yuze Fan, Ziguo Chen, Fei Gao, Zhenhai Gao
- **🏷️ 机构**: Lanzhou University, Jilin University
- **会议**: NeurIPS 2025

### Approximate Domain Unlearning for Vision-Language Models.
- **链接**: [arXiv:2510.08132](https://arxiv.org/abs/2510.08132)
- **作者**: Kodai Kawamura, Yuta Goto, Rintaro Yanagi, Hirokatsu Kataoka, Go Irie
- **🏷️ 机构**: National University of Singapore, Tokyo University of Science, AIST, National Institute of Advanced Industrial Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained Vision-Language Models (VLMs) exhibit strong generalization capabilities, enabling them to recognize a wide range of objects across diverse domains without additional training. However, they often retain irrelevant information beyond the requirements of specific downstream tasks, raising concerns about computational efficiency and potential information leakage. This has motivated growing interest in approximate unlearning, which aims to selectively remove unnecessary knowledge while preserving overall model performance. Existing approaches to approximate unlearning have primarily focused on class unlearning, where a VLM is retrained to fail to recognize specified object classes while maintaining accuracy for others. However, merely forgetting object classes is often insufficient in practical applications. For instance, an autonomous driving system should accurately recognize real cars while avoiding misrecognition of illustrated cars depicted in roadside advertisements as real cars, which could be hazardous. In this paper, we introduce Approximate Domain Unlearning (ADU), a novel problem setting that requires reducing recognition accuracy for images from specified domains (e.g., illustration) while preserving accuracy for other domains (e.g., real). ADU presents new technical challenges: due to the strong domain generalization capability of pre-trained VLMs, domain distributions are highly entangled in the feature space, making naive approaches based on penalizing target domains ineffective. To tackle this limitation, we propose a novel approach that explicitly disentangles domain distributions and adaptively captures instance-specific domain information. Extensive experiments show that our approach outperforms baselines built upon VLM tuning techniques, paving the way for practical and fine-grained unlearning in VLMs. Code: https://kodaikawamura.github.io/Domain_Unlearning/.

</details>

### Extremely Simple Multimodal Outlier Synthesis for Out-of-Distribution Detection and Segmentation.
- **链接**: [arXiv:2505.16985](https://arxiv.org/abs/2505.16985) · 📚 被引 2
- **作者**: Moru Liu, Hao Dong, Jessica Kelly, Olga Fink, Mario Trapp
- **🏷️ 机构**: Technische Universität München, Peking University, Fraunhofer IKS
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection and segmentation are crucial for deploying machine learning models in safety-critical applications such as autonomous driving and robot-assisted surgery. While prior research has primarily focused on unimodal image data, real-world applications are inherently multimodal, requiring the integration of multiple modalities for improved OOD detection. A key challenge is the lack of supervision signals from unknown data, leading to overconfident predictions on OOD samples. To address this challenge, we propose Feature Mixing, an extremely simple and fast method for multimodal outlier synthesis with theoretical support, which can be further optimized to help the model better distinguish between in-distribution (ID) and OOD data. Feature Mixing is modality-agnostic and applicable to various modality combinations. Additionally, we introduce CARLA-OOD, a novel multimodal dataset for OOD segmentation, featuring synthetic OOD objects across diverse scenes and weather conditions. Extensive experiments on SemanticKITTI, nuScenes, CARLA-OOD datasets, and the MultiOOD benchmark demonstrate that Feature Mixing achieves state-of-the-art performance with a $10 \times$ to $370 \times$ speedup. Our source code and dataset will be available at https://github.com/mona4399/FeatureMixing.

</details>

### PhysDrive: A Multimodal Remote Physiological Measurement Dataset for In-vehicle Driver Monitoring.
- **链接**: [arXiv:2507.19172](https://arxiv.org/abs/2507.19172)
- **作者**: Jiyao Wang, Xiao Yang, Qingyong Hu, Jack Tang, Can Liu, Dengbo He et al.
- **🏷️ 机构**: Research, Microsoft, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robust and unobtrusive in-vehicle physiological monitoring is crucial for ensuring driving safety and user experience. While remote physiological measurement (RPM) offers a promising non-invasive solution, its translation to real-world driving scenarios is critically constrained by the scarcity of comprehensive datasets. Existing resources are often limited in scale, modality diversity, the breadth of biometric annotations, and the range of captured conditions, thereby omitting inherent real-world challenges in driving. Here, we present PhysDrive, the first large-scale multimodal dataset for contactless in-vehicle physiological sensing with dedicated consideration on various modality settings and driving factors. PhysDrive collects data from 48 drivers, including synchronized RGB, near-infrared camera, and raw mmWave radar data, accompanied with six synchronized ground truths (ECG, BVP, Respiration, HR, RR, and SpO2). It covers a wide spectrum of naturalistic driving conditions, including driver motions, dynamic natural light, vehicle types, and road conditions. We extensively evaluate both signal-processing and deep-learning methods on PhysDrive, establishing a comprehensive benchmark across all modalities, and release full open-source code with compatibility for mainstream public toolboxes. We envision PhysDrive will serve as a foundational resource and accelerate research on multimodal driver monitoring and smart-cockpit systems.

</details>

### MuSLR: Multimodal Symbolic Logical Reasoning.
- **链接**: [arXiv:2509.25851](https://arxiv.org/abs/2509.25851)
- **作者**: Jundong Xu, Hao Fei, Yuhui Zhang, Liangming Pan, Qijun Huang, Qian Liu et al.
- **🏷️ 机构**: National University of Singapore, Stanford University, Peking University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal symbolic logical reasoning, which aims to deduce new facts from multimodal input via formal logic, is critical in high-stakes applications such as autonomous driving and medical diagnosis, as its rigorous, deterministic reasoning helps prevent serious consequences. To evaluate such capabilities of current state-of-the-art vision language models (VLMs), we introduce the first benchmark MuSLR for multimodal symbolic logical reasoning grounded in formal logical rules. MuSLR comprises 1,093 instances across 7 domains, including 35 atomic symbolic logic and 976 logical combinations, with reasoning depths ranging from 2 to 9. We evaluate 7 state-of-the-art VLMs on MuSLR and find that they all struggle with multimodal symbolic reasoning, with the best model, GPT-4.1, achieving only 46.8%. Thus, we propose LogiCAM, a modular framework that applies formal logical rules to multimodal inputs, boosting GPT-4.1's Chain-of-Thought performance by 14.13%, and delivering even larger gains on complex logics such as first-order logic. We also conduct a comprehensive error analysis, showing that around 70% of failures stem from logical misalignment between modalities, offering key insights to guide future improvements. All data and code are publicly available at https://llm-symbol.github.io/MuSLR.

</details>

## 跨领域论文（完整笔记在其他领域）

- OpenAD: Open-World Autonomous Driving Benchmark for 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- STSBench: A Spatio-temporal Scenario Benchmark for Multi-modal Large Language Models in Autonomous Driving. → [vlm](../vlm/Guideline%202025.md)
- UniMamba: Unified Spatial-Channel Representation Learning with Group-Efficient Mamba for LiDAR-based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras. → [3d-detection](../3d-detection/Guideline%202025.md)
- RaCFormer: Towards High-Quality 3D Object Detection via Query-based Radar-Camera Fusion. → [object-detection](../object-detection/Guideline%202025.md)
- Track Any Anomalous Object: A Granular Video Anomaly Detection Pipeline. → [video-understanding](../video-understanding/Guideline%202025.md)
- V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- RICCARDO: Radar Hit Prediction and Convolution for Camera-Radar 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- GBlobs: Explicit Local Structure via Gaussian Blobs for Improved Cross-Domain LiDAR-based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- SparseAlign: a Fully Sparse Framework for Cooperative Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- SP3D: Boosting Sparsely-Supervised 3D Object Detection via Accurate Cross-Modal Semantic Prompts. → [3d-detection](../3d-detection/Guideline%202025.md)
- Spotting the Unexpected (STU): A 3D LiDAR Dataset for Anomaly Segmentation in Autonomous Driving. → [fod-detection](../fod-detection/Guideline%202025.md)
- Multi-Scale Neighborhood Occupancy Masked Autoencoder for Self-Supervised Learning in LiDAR Point Clouds. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- PSA-SSL: Pose and Size-aware Self-Supervised Learning on LiDAR Point Clouds. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- SDGOCC: Semantic and Depth-Guided Bird's-Eye View Transformation for 3D Multimodal Occupancy Prediction. → [multimodal](../multimodal/Guideline%202025.md)
- Toward Real-world BEV Perception: Depth Uncertainty Estimation via Gaussian Splatting. → [bev](../bev/Guideline%202025.md)
- Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction. → [occupancy](../occupancy/Guideline%202025.md)
- GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction. → [occupancy](../occupancy/Guideline%202025.md)
- Improved Monocular Depth Prediction Using Distance Transform Over Pre-semantic Contours with Self-supervised Neural Networks. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving. → [object-detection](../object-detection/Guideline%202025.md)
- JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Bridging Past and Future: End-to-End Autonomous Driving with Historical Prediction and Planning. → [bev](../bev/Guideline%202025.md)
- DriveGEN: Generalized and Robust 3D Detection in Driving via Controllable Text-to-Image Diffusion Generation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- MMTL-UniAD: A Unified Framework for Multimodal and Multi-Task Learning in Assistive Driving Perception. → [multimodal](../multimodal/Guideline%202025.md)
- Generating Multimodal Driving Scenes via Next-Scene Prediction. → [multimodal](../multimodal/Guideline%202025.md)
- Embodied Scene Understanding for Vision Language Models via MetaVQA. → [vlm](../vlm/Guideline%202025.md)
- GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Synthetic-to-Real Self-supervised Robust Depth Estimation via Learning with Motion and Structure Priors. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Multi-modal Knowledge Distillation-based Human Trajectory Forecasting. → [knowledge-distillation](../knowledge-distillation/Guideline%202025.md)
- OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving. → [object-detection](../object-detection/Guideline%202025.md)
- RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion. → [object-detection](../object-detection/Guideline%202025.md)
- DoppDrive: Doppler-Driven Temporal Aggregation for Improved Radar Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts. → [3d-detection](../3d-detection/Guideline%202025.md)
- EVT: Efficient View Transformation for Multi-Modal 3D Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge. → [3d-detection](../3d-detection/Guideline%202025.md)
- DuET: Dual Incremental Object Detection via Exemplar-Free Task Arithmetic. → [object-detection](../object-detection/Guideline%202025.md)
- ForeSight: Multi-View Streaming Joint Object Detection and Trajectory Forecasting. → [object-detection](../object-detection/Guideline%202025.md)
- FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- 3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Temporal Overlapping Prediction: A Self-Supervised Pre-Training Method for LiDAR Moving Object Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- MCAM: Multimodal Causal Analysis Model for Ego-Vehicle-Level Driving Video Understanding. → [video-understanding](../video-understanding/Guideline%202025.md)
- RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [bev](../bev/Guideline%202025.md)
- DriveTransformer: Unified Transformer for Scalable End-to-End Autonomous Driving. → [bev](../bev/Guideline%202025.md)
- Semi-Supervised Vision-Centric 3D Occupancy World Model for Autonomous Driving. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- X-Drive: Cross-modality Consistent Multi-Sensor Data Synthesis for Driving Scenarios. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction. → [occupancy](../occupancy/Guideline%202025.md)
- Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving. → [bev](../bev/Guideline%202025.md)
- GaussianFusion: Gaussian-Based Multi-Sensor Fusion for End-to-End Autonomous Driving. → [bev](../bev/Guideline%202025.md)
- RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation. → [occupancy](../occupancy/Guideline%202025.md)
- Genesis: Multimodal Driving Scene Generation with Spatio-Temporal and Cross-Modal Consistency. → [video-understanding](../video-understanding/Guideline%202025.md)
- MVU-Eval: Towards Multi-Video Understanding Evaluation for Multimodal LLMs. → [video-understanding](../video-understanding/Guideline%202025.md)

<!-- COMPLETE v1 papers=70 -->
