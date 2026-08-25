# Autonomous Driving — 2025 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 22 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Driving by the Rules: A Benchmark for Integrating Traffic Sign Regulations into Vectorized HD Map.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chang_Driving_by_the_Rules_A_Benchmark_for_Integrating_Traffic_Sign_CVPR_2025_paper.html)
- **作者**: Xinyuan Chang, Maixuan Xue, Xinran Liu, Zheng Pan, Xing Wei
- **🏷️ 机构**: Alibaba Group,Amap, Xi&#x2019;an Jiaotong University
- **会议**: CVPR 2025

### Spotting the Unexpected (STU): A 3D LiDAR Dataset for Anomaly Segmentation in Autonomous Driving.
- **链接**: [arXiv:2505.02148](https://arxiv.org/abs/2505.02148)
- **作者**: Alexey Nekrasov, Malcolm Burdorf, Stewart Worrall, Bastian Leibe, Julie Stephany Berrio Perez
- **🏷️ 机构**: RWTH Aachen University, The University of Sydney
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > To operate safely, autonomous vehicles (AVs) need to detect and handle unexpected objects or anomalies on the road. While significant research exists for anomaly detection and segmentation in 2D, research progress in 3D is underexplored. Existing datasets lack high-quality multimodal data that are typically found in AVs. This paper presents a novel dataset for anomaly segmentation in driving scenarios. To the best of our knowledge, it is the first publicly available dataset focused on road anomaly segmentation with dense 3D semantic labeling, incorporating both LiDAR and camera data, as well as sequential information to enable anomaly detection across various ranges. This capability is critical for the safe navigation of autonomous vehicles. We adapted and evaluated several baseline models for 3D segmentation, highlighting the challenges of 3D anomaly detection in driving environments. Our dataset and evaluation code will be openly available, facilitating the testing and performance comparison of different approaches.

### SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving.
- **链接**: [arXiv:2411.16816](https://arxiv.org/abs/2411.16816)
- **作者**: Georg Hess, Carl Lindström, Maryam Fatemi, Christoffer Petersson, Lennart Svensson
- **🏷️ 机构**: Zenseact, Chalmers University of Technology
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Ensuring the safety of autonomous robots, such as self-driving vehicles, requires extensive testing across diverse driving scenarios. Simulation is a key ingredient for conducting such testing in a cost-effective and scalable way. Neural rendering methods have gained popularity, as they can build simulation environments from collected logs in a data-driven manner. However, existing neural radiance field (NeRF) methods for sensor-realistic rendering of camera and lidar data suffer from low rendering speeds, limiting their applicability for large-scale testing. While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous driving. To address these limitations, we propose SplatAD, the first 3DGS-based method for realistic, real-time rendering of dynamic scenes for both camera and lidar data. SplatAD accurately models key sensor-specific phenomena such as rolling shutter effects, lidar intensity, and lidar ray dropouts, using purpose-built algorithms to optimize rendering efficiency. Evaluation across three autonomous driving datasets demonstrates that SplatAD achieves state-of-the-art rendering quality with up to +2 PSNR for NVS and +3 PSNR for reconstruction while increasing rendering speed over NeRF-based methods by an order of magnitude. See https://research.zenseact.com/publications/splatad/ for our project page.

### HiLoTs: High-Low Temporal Sensitive Representation Learning for Semi-Supervised LiDAR Segmentation in Autonomous Driving.
- **链接**: [arXiv:2503.17752](https://arxiv.org/abs/2503.17752) · [代码](https://github.com/rdlin118/HiLoTs)
- **作者**: R. D. Lin, Pengcheng Weng, Yinqiao Wang, Han Ding, Jinsong Han, Fei Wang
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering,China, Xi&#x2019;an Jiaotong University,School of Computer Science and Technology,China, Zhejiang University,College of Computer Science and Technology,China
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > LiDAR point cloud semantic segmentation plays a crucial role in autonomous driving. In recent years, semi-supervised methods have gained popularity due to their significant reduction in annotation labor and time costs. Current semi-supervised methods typically focus on point cloud spatial distribution or consider short-term temporal representations, e.g., only two adjacent frames, often overlooking the rich long-term temporal properties inherent in autonomous driving scenarios. In driving experience, we observe that nearby objects, such as roads and vehicles, remain stable while driving, whereas distant objects exhibit greater variability in category and shape. This natural phenomenon is also captured by LiDAR, which reflects lower temporal sensitivity for nearby objects and higher sensitivity for distant ones. To leverage these characteristics, we propose HiLoTs, which learns high-temporal sensitivity and low-temporal sensitivity representations from continuous LiDAR frames. These representations are further enhanced and fused using a cross-attention mechanism. Additionally, we employ a teacher-student framework to align the representations learned by the labeled and unlabeled branches, effectively utilizing the large amounts of unlabeled data. Experimental results on the SemanticKITTI and nuScenes datasets demonstrate that our proposed HiLoTs outperforms state-of-the-art semi-supervised methods, and achieves performance close to LiDAR+Camera multimodal approaches. Code is available on https://github.com/rdlin118/HiLoTs

### SOLVE: Synergy of Language-Vision and End-to-End Networks for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SOLVE_Synergy_of_Language-Vision_and_End-to-End_Networks_for_Autonomous_Driving_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Xuesong Chen, Linjiang Huang, Tao Ma, Rongyao Fang, Shaoshuai Shi, Hongsheng Li
- **🏷️ 机构**: MMLab,CUHK, Beihang University,Institute of Artificial Intelligence, Didi Chuxing,Voyager Research
- **会议**: CVPR 2025

### VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_VisionPAD_A_Vision-Centric_Pre-training_Paradigm_for_Autonomous_Driving_CVPR_2025_paper.html)
- **作者**: Haiming Zhang, Wending Zhou, Yiyao Zhu, Xu Yan, Jiantao Gao, Dongfeng Bai et al.
- **🏷️ 机构**: FNii,Shenzhen, HKUST, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2025

### JiSAM: Alleviate Labeling Burden and Corner Case Problems in Autonomous Driving via Minimal Real-World Data.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_JiSAM_Alleviate_Labeling_Burden_and_Corner_Case_Problems_in_Autonomous_CVPR_2025_paper.html)
- **作者**: Runjian Chen, Wenqi Shao, Bo Zhang, Shaoshuai Shi, Li Jiang, Ping Luo
- **🏷️ 机构**: The University of Hong Kong, Shanghai AI Laboratory, Voyager Research, Didi Chuxing
- **会议**: CVPR 2025

### Distilling Multi-modal Large Language Models for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hegde_Distilling_Multi-modal_Large_Language_Models_for_Autonomous_Driving_CVPR_2025_paper.html)
- **作者**: Deepti Hegde, Rajeev Yasarla, Hong Cai, Shizhong Han, Apratim Bhattacharyya, Shweta Mahajan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_DiffusionDrive_Truncated_Diffusion_Model_for_End-to-End_Autonomous_Driving_CVPR_2025_paper.html)
- **作者**: Bencheng Liao, Shaoyu Chen, Haoran Yin, Bo Jiang, Cheng Wang, Sixu Yan et al.
- **🏷️ 机构**: Huazhong University of Science &#x0026; Technology,Institute of Artificial Intelligence, Huazhong University of Science &#x0026; Technology,School of EIC, Horizon Robotics
- **会议**: CVPR 2025

### JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.html)
- **作者**: Yunlong Lin, Zixu Lin, Haoyu Chen, Panwang Pan, Chenxin Li, Sixiang Chen et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,Xiamen,China, The Hong Kong University of Science and Technology (Guangzhou), Bytedance&#x2019;s Pico
- **会议**: CVPR 2025

### T2SG: Traffic Topology Scene Graph for Topology Reasoning in Autonomous Driving.
- **链接**: [arXiv:2411.18894](https://arxiv.org/abs/2411.18894)
- **作者**: Changsheng Lv, Mengshi Qi, Liang Liu, Huadong Ma
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Understanding the traffic scenes and then generating high-definition (HD) maps present significant challenges in autonomous driving. In this paper, we defined a novel Traffic Topology Scene Graph, a unified scene graph explicitly modeling the lane, controlled and guided by different road signals (e.g., right turn), and topology relationships among them, which is always ignored by previous high-definition (HD) mapping methods. For the generation of T2SG, we propose TopoFormer, a novel one-stage Topology Scene Graph TransFormer with two newly designed layers. Specifically, TopoFormer incorporates a Lane Aggregation Layer (LAL) that leverages the geometric distance among the centerline of lanes to guide the aggregation of global information. Furthermore, we proposed a Counterfactual Intervention Layer (CIL) to model the reasonable road structure ( e.g., intersection, straight) among lanes under counterfactual intervention. Then the generated T2SG can provide a more accurate and explainable description of the topological structure in traffic scenes. Experimental results demonstrate that TopoFormer outperforms existing methods on the T2SG generation task, and the generated T2SG significantly enhances traffic topology reasoning in downstream tasks, achieving a state-of-the-art performance of 46.3 OLS on the OpenLane-V2 benchmark. We will release our source code and model.

### SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment.
- **链接**: [arXiv:2503.09594](https://arxiv.org/abs/2503.09594)
- **作者**: Katrin Renz, Long Chen, Elahe Arani, Oleg Sinavski
- **🏷️ 机构**: Wayve
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Integrating large language models (LLMs) into autonomous driving has attracted significant attention with the hope of improving generalization and explainability. However, existing methods often focus on either driving or vision-language understanding but achieving both high driving performance and extensive language understanding remains challenging. In addition, the dominant approach to tackle vision-language understanding is using visual question answering. However, for autonomous driving, this is only useful if it is aligned with the action space. Otherwise, the model's answers could be inconsistent with its behavior. Therefore, we propose a model that can handle three different tasks: (1) closed-loop driving, (2) vision-language understanding, and (3) language-action alignment. Our model SimLingo is based on a vision language model (VLM) and works using only camera, excluding expensive sensors like LiDAR. SimLingo obtains state-of-the-art performance on the widely used CARLA simulator on the Bench2Drive benchmark and is the winning entry at the CARLA challenge 2024. Additionally, we achieve strong results in a wide variety of language-related tasks while maintaining high driving performance.

### Don't Shake the Wheel: Momentum-Aware Planning in End-to-End Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Song_Dont_Shake_the_Wheel_Momentum-Aware_Planning_in_End-to-End_Autonomous_Driving_CVPR_2025_paper.html)
- **作者**: Ziying Song, Caiyan Jia, Lin Liu, Hongyu Pan, Yongchang Zhang, Junming Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

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
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_DriveGPT4-V2_Harnessing_Large_Language_Model_Capabilities_for_Enhanced_Closed-Loop_Autonomous_CVPR_2025_paper.html)
- **作者**: Zhenhua Xu, Yan Bai, Yujia Zhang, Zhuoling Li, Fei Xia, Kwan-Yee K. Wong et al.
- **🏷️ 机构**: The University of Hong Kong, Meituan, Tsinghua University
- **会议**: CVPR 2025

### Enduring, Efficient and Robust Trajectory Prediction Attack in Autonomous Driving via Optimization-Driven Multi-Frame Perturbation Framework.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Enduring_Efficient_and_Robust_Trajectory_Prediction_Attack_in_Autonomous_Driving_CVPR_2025_paper.html)
- **作者**: Yi Yu, Weizhen Han, Libing Wu, Bingyi Liu, Enshu Wang, Zhuangzhuang Zhang
- **🏷️ 机构**: Wuhan University,Key Laboratory of Aerospace Information Security and Trusted Computing, Ministry of Education, School of Cyber Science and Engineering, Wuhan University of Technology,School of Computer Science and Artificial Intelligence, City University of Hong Kong,Department of Computer Science
- **会议**: CVPR 2025

### CarPlanner: Consistent Auto-regressive Trajectory Planning for Large-Scale Reinforcement Learning in Autonomous Driving.
- **链接**: [arXiv:2502.19908](https://arxiv.org/abs/2502.19908)
- **作者**: Dongkun Zhang, Jiaming Liang, Ke Guo, Sha Lu, Qi Wang, Rong Xiong et al.
- **🏷️ 机构**: Zhejiang University, Cainiao Network
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Trajectory planning is vital for autonomous driving, ensuring safe and efficient navigation in complex environments. While recent learning-based methods, particularly reinforcement learning (RL), have shown promise in specific scenarios, RL planners struggle with training inefficiencies and managing large-scale, real-world driving scenarios. In this paper, we introduce \textbf{CarPlanner}, a \textbf{C}onsistent \textbf{a}uto-\textbf{r}egressive \textbf{Planner} that uses RL to generate multi-modal trajectories. The auto-regressive structure enables efficient large-scale RL training, while the incorporation of consistency ensures stable policy learning by maintaining coherent temporal consistency across time steps. Moreover, CarPlanner employs a generation-selection framework with an expert-guided reward function and an invariant-view module, simplifying RL training and enhancing policy performance. Extensive analysis demonstrates that our proposed RL framework effectively addresses the challenges of training efficiency and performance enhancement, positioning CarPlanner as a promising solution for trajectory planning in autonomous driving. To the best of our knowledge, we are the first to demonstrate that the RL-based planner can surpass both IL- and rule-based state-of-the-arts (SOTAs) on the challenging large-scale real-world dataset nuPlan. Our proposed CarPlanner surpasses RL-, IL-, and rule-based SOTA approaches within this demanding dataset.

### MPDrive: Improving Spatial Understanding with Marker-Based Prompt Learning for Autonomous Driving.
- **链接**: [arXiv:2504.00379](https://arxiv.org/abs/2504.00379)
- **作者**: Zhiyuan Zhang, Xiaofan Li, Zhihao Xu, Wenjie Peng, Zijian Zhou, Miaojing Shi et al.
- **🏷️ 机构**: South China University of Technology, Baidu Inc., King&#x2019;s College London
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Autonomous driving visual question answering (AD-VQA) aims to answer questions related to perception, prediction, and planning based on given driving scene images, heavily relying on the model's spatial understanding capabilities. Prior works typically express spatial information through textual representations of coordinates, resulting in semantic gaps between visual coordinate representations and textual descriptions. This oversight hinders the accurate transmission of spatial information and increases the expressive burden. To address this, we propose a novel Marker-based Prompt learning framework (MPDrive), which represents spatial coordinates by concise visual markers, ensuring linguistic expressive consistency and enhancing the accuracy of both visual perception and spatial expression in AD-VQA. Specifically, we create marker images by employing a detection expert to overlay object regions with numerical labels, converting complex textual coordinate generation into straightforward text-based visual marker predictions. Moreover, we fuse original and marker images as scene-level features and integrate them with detection priors to derive instance-level features. By combining these features, we construct dual-granularity visual prompts that stimulate the LLM's spatial perception capabilities. Extensive experiments on the DriveLM and CODA-LM datasets show that MPDrive achieves state-of-the-art performance, particularly in cases requiring sophisticated spatial understanding.

### Bridging Past and Future: End-to-End Autonomous Driving with Historical Prediction and Planning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Bridging_Past_and_Future_End-to-End_Autonomous_Driving_with_Historical_Prediction_CVPR_2025_paper.html)
- **作者**: Bozhou Zhang, Nan Song, Xin Jin, Li Zhang
- **🏷️ 机构**: Fudan University,School of Data Science, Eastern Institute of Technology
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
