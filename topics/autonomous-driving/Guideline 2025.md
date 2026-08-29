# Autonomous Driving — 2025 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 22 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Driving by the Rules: A Benchmark for Integrating Traffic Sign Regulations into Vectorized HD Map.
- **链接**: [arXiv:2410.23780](https://arxiv.org/abs/2410.23780) · [代码](https://github.com/MIV-XJTU/MapDR) · 📚 被引 3
- **作者**: Xinyuan Chang, Maixuan Xue, Xinran Liu, Zheng Pan, Xing Wei
- **🏷️ 机构**: Alibaba Group,Amap, Xi&#x2019;an Jiaotong University
- **会议**: CVPR 2025

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

> Integrating large language models (LLMs) into autonomous driving has attracted significant attention with the hope of improving generalization and explainability. However, existing methods often focus on either driving or vision-language understanding but achieving both high driving performance and extensive language understanding remains challenging. In addition, the dominant approach to tackle vision-language understanding is using visual question answering. However, for autonomous driving, this is only useful if it is aligned with the action space. Otherwise, the model's answers could be inconsistent with its behavior. Therefore, we propose a model that can handle three different tasks: (1) closed-loop driving, (2) vision-language understanding, and (3) language-action alignment. Our model SimLingo is based on a vision language model (VLM) and works using only camera, excluding expensive sensors like LiDAR. SimLingo obtains state-of-the-art performance on the widely used CARLA simulator on the Bench2Drive benchmark and is the winning entry at the CARLA challenge 2024. Additionally, we achieve strong results in a wide variety of language-related tasks while maintaining high driving performance.

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, end-to-end planners directly utilize raw sensor data, enabling them to extract richer scene features and reduce information loss compared to traditional planners. This raises a crucial research question: how can we develop better scene feature representations to fully leverage sensor data in end-to-end driving? Self-supervised learning methods show great success in learning rich feature representations in NLP and computer vision. Inspired by this, we propose a novel self-supervised learning approach using the LAtent World model (LAW) for end-to-end driving. LAW predicts future scene features based on current features and ego trajectories. This self-supervised task can be seamlessly integrated into perception-free and perception-based frameworks, improving scene feature learning and optimizing trajectory prediction. LAW achieves state-of-the-art performance across multiple benchmarks, including real-world open-loop benchmark nuScenes, NAVSIM, and simulator-based closed-loop benchmark CARLA. The code is released at https://github.com/BraveGroup/LAW.

</details>

### MPDrive: Improving Spatial Understanding with Marker-Based Prompt Learning for Autonomous Driving.
- **链接**: [arXiv:2504.00379](https://arxiv.org/abs/2504.00379) · 📚 被引 9
- **作者**: Zhiyuan Zhang, Xiaofan Li, Zhihao Xu, Wenjie Peng, Zijian Zhou, Miaojing Shi et al.
- **🏷️ 机构**: South China University of Technology, Baidu Inc., King&#x2019;s College London
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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
