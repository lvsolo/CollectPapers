# Autonomous Driving — 2024 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications.
- **链接**: [arXiv:2311.17663](https://arxiv.org/abs/2311.17663) · [代码](https://github.com/haomo-ai/Cam4DOcc) · 📚 被引 35
- **作者**: Junyi Ma, Xieyuanli Chen, Jiawei Huang, Jingyi Xu, Zhen Luo, Jintao Xu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,IRMV Lab,Department of Automation, College of Intelligence Science and Technology, National University of Defense Technology, HAOMO.AI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Understanding how the surrounding environment changes is crucial for performing downstream tasks safely and reliably in autonomous driving applications. Recent occupancy estimation techniques using only camera images as input can provide dense occupancy representations of large-scale scenes based on the current observation. However, they are mostly limited to representing the current 3D space and do not consider the future state of surrounding objects along the time axis. To extend camera-only occupancy estimation into spatiotemporal prediction, we propose Cam4DOcc, a new benchmark for camera-only 4D occupancy forecasting, evaluating the surrounding scene changes in a near future. We build our benchmark based on multiple publicly available datasets, including nuScenes, nuScenes-Occupancy, and Lyft-Level5, which provides sequential occupancy states of general movable and static objects, as well as their 3D backward centripetal flow. To establish this benchmark for future research with comprehensive comparisons, we introduce four baseline types from diverse camera-based perception and prediction implementations, including a static-world occupancy model, voxelization of point cloud prediction, 2D-3D instance-based prediction, and our proposed novel end-to-end 4D occupancy forecasting network. Furthermore, the standardized evaluation protocol for preset multiple tasks is also provided to compare the performance of all the proposed baselines on present and future occupancy estimation with respect to objects of interest in autonomous driving scenarios. The dataset and our implementation of all four baselines in the proposed Cam4DOcc benchmark will be released here: https://github.com/haomo-ai/Cam4DOcc.

### LaMPilot: An Open Benchmark Dataset for Autonomous Driving with Language Model Programs.
- **链接**: [arXiv:2312.04372](https://arxiv.org/abs/2312.04372) · [代码](https://github.com/PurdueDigitalTwin/LaMPilot) · 📚 被引 53
- **作者**: Yunsheng Ma, Can Cui, Xu Cao, Wenqian Ye, Peiran Liu, Juanwu Lu et al.
- **🏷️ 机构**: Purdue University, University of Illinois Urbana-Champaign, University of Virginia
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Autonomous driving (AD) has made significant strides in recent years. However, existing frameworks struggle to interpret and execute spontaneous user instructions, such as "overtake the car ahead." Large Language Models (LLMs) have demonstrated impressive reasoning capabilities showing potential to bridge this gap. In this paper, we present LaMPilot, a novel framework that integrates LLMs into AD systems, enabling them to follow user instructions by generating code that leverages established functional primitives. We also introduce LaMPilot-Bench, the first benchmark dataset specifically designed to quantitatively evaluate the efficacy of language model programs in AD. Adopting the LaMPilot framework, we conduct extensive experiments to assess the performance of off-the-shelf LLMs on LaMPilot-Bench. Our results demonstrate the potential of LLMs in handling diverse driving scenarios and following user instructions in driving. To facilitate further research in this area, we release our code and data at https://github.com/PurdueDigitalTwin/LaMPilot.

### AIDE: An Automatic Data Engine for Object Detection in Autonomous Driving.
- **链接**: [arXiv:2403.17373](https://arxiv.org/abs/2403.17373) · 📚 被引 33
- **作者**: Mingfu Liang, Jong-Chyi Su, Samuel Schulter, Sparsh Garg, Shiyu Zhao, Ying Wu et al.
- **🏷️ 机构**: Northwestern University, NEC Laboratories America, Rutgers University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Autonomous vehicle (AV) systems rely on robust perception models as a cornerstone of safety assurance. However, objects encountered on the road exhibit a long-tailed distribution, with rare or unseen categories posing challenges to a deployed perception model. This necessitates an expensive process of continuously curating and annotating data with significant human effort. We propose to leverage recent advances in vision-language and large language models to design an Automatic Data Engine (AIDE) that automatically identifies issues, efficiently curates data, improves the model through auto-labeling, and verifies the model through generation of diverse scenarios. This process operates iteratively, allowing for continuous self-improvement of the model. We further establish a benchmark for open-world detection on AV datasets to comprehensively evaluate various learning paradigms, demonstrating our method's superior performance at a reduced cost.

### Visual Point Cloud Forecasting Enables Scalable Autonomous Driving.
- **链接**: [arXiv:2312.17655](https://arxiv.org/abs/2312.17655) · 📚 被引 58
- **作者**: Zetong Yang, Li Chen, Yanan Sun, Hongyang Li
- **🏷️ 机构**: OpenDriveLab and Shanghai AI Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In contrast to extensive studies on general vision, pre-training for scalable visual autonomous driving remains seldom explored. Visual autonomous driving applications require features encompassing semantics, 3D geometry, and temporal information simultaneously for joint perception, prediction, and planning, posing dramatic challenges for pre-training. To resolve this, we bring up a new pre-training task termed as visual point cloud forecasting - predicting future point clouds from historical visual input. The key merit of this task captures the synergic learning of semantics, 3D structures, and temporal dynamics. Hence it shows superiority in various downstream tasks. To cope with this new problem, we present ViDAR, a general model to pre-train downstream visual encoders. It first extracts historical embeddings by the encoder. These representations are then transformed to 3D geometric space via a novel Latent Rendering operator for future point cloud prediction. Experiments show significant gain in downstream tasks, e.g., 3.1% NDS on 3D detection, ~10% error reduction on motion forecasting, and ~15% less collision rate on planning.

### Adaptive Fusion of Single-View and Multi-View Depth for Autonomous Driving.
- **链接**: [arXiv:2403.07535](https://arxiv.org/abs/2403.07535) · [代码](https://github.com/Junda24/AFNet) · 📚 被引 43
- **作者**: Junda Cheng, Wei Yin, Kaixuan Wang, Xiaozhi Chen, Shijie Wang, Xin Yang
- **🏷️ 机构**: Huazhong University of Science and Technology, DJI Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multi-view depth estimation has achieved impressive performance over various benchmarks. However, almost all current multi-view systems rely on given ideal camera poses, which are unavailable in many real-world scenarios, such as autonomous driving. In this work, we propose a new robustness benchmark to evaluate the depth estimation system under various noisy pose settings. Surprisingly, we find current multi-view depth estimation methods or single-view and multi-view fusion methods will fail when given noisy pose settings. To address this challenge, we propose a single-view and multi-view fused depth estimation system, which adaptively integrates high-confident multi-view and single-view results for both robust and accurate depth estimations. The adaptive fusion module performs fusion by dynamically selecting high-confidence regions between two branches based on a wrapping confidence map. Thus, the system tends to choose the more reliable branch when facing textureless scenes, inaccurate calibration, dynamic objects, and other degradation or challenging conditions. Our method outperforms state-of-the-art multi-view and fusion methods under robustness testing. Furthermore, we achieve state-of-the-art performance on challenging benchmarks (KITTI and DDAD) when given accurate pose estimations. Project website: https://github.com/Junda24/AFNet/.

### Holistic Autonomous Driving Understanding by Bird'View Injected Multi-Modal Large Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01297) · 📚 被引 41
- **作者**: Xinpeng Ding, Jianhua Han, Hang Xu, Xiaodan Liang, Wei Zhang, Xiaomeng Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab, Sun Yat-Sen University
- **会议**: CVPR 2024

### Physical 3D Adversarial Attacks against Monocular Depth Estimation in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02308) · 📚 被引 57
- **作者**: Junhao Zheng, Chenhao Lin, Jiahao Sun, Zhengyu Zhao, Qian Li, Chao Shen
- **🏷️ 机构**: Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China,710049
- **会议**: CVPR 2024

### Driving Into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving.
- **链接**: [arXiv:2311.17918](https://arxiv.org/abs/2311.17918) · 📚 被引 116
- **作者**: Yuqi Wang, Jiawei He, Lue Fan, Hongxin Li, Yuntao Chen, Zhaoxiang Zhang
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences (UCAS), Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, MAIS, Centre for Artificial Intelligence and Robotics (HKISI_CAS)
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

### DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes.
- **链接**: [arXiv:2312.07920](https://arxiv.org/abs/2312.07920) · [代码](https://github.com/VDIGPKU/DrivingGaussian) · 📚 被引 280
- **作者**: Xiaoyu Zhou, Zhiwei Lin, Xiaojun Shan, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, Google Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present DrivingGaussian, an efficient and effective framework for surrounding dynamic autonomous driving scenes. For complex scenes with moving objects, we first sequentially and progressively model the static background of the entire scene with incremental static 3D Gaussians. We then leverage a composite dynamic Gaussian graph to handle multiple moving objects, individually reconstructing each object and restoring their accurate positions and occlusion relationships within the scene. We further use a LiDAR prior for Gaussian Splatting to reconstruct scenes with greater details and maintain panoramic consistency. DrivingGaussian outperforms existing methods in dynamic driving scene reconstruction and enables photorealistic surround-view synthesis with high-fidelity and multi-camera consistency. Our project page is at: https://github.com/VDIGPKU/DrivingGaussian.

### On the Road to Portability: Compressing End-to-End Motion Planner for Autonomous Driving.
- **链接**: [arXiv:2403.01238](https://arxiv.org/abs/2403.01238) · 📚 被引 14
- **作者**: Kaituo Feng, Changsheng Li, Dongchun Ren, Ye Yuan, Guoren Wang
- **🏷️ 机构**: Beijing Institute of Technology, ALLRIDE.AI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > End-to-end motion planning models equipped with deep neural networks have shown great potential for enabling full autonomous driving. However, the oversized neural networks render them impractical for deployment on resource-constrained systems, which unavoidably requires more computational time and resources during reference.To handle this, knowledge distillation offers a promising approach that compresses models by enabling a smaller student model to learn from a larger teacher model. Nevertheless, how to apply knowledge distillation to compress motion planners has not been explored so far. In this paper, we propose PlanKD, the first knowledge distillation framework tailored for compressing end-to-end motion planners. First, considering that driving scenes are inherently complex, often containing planning-irrelevant or even noisy information, transferring such information is not beneficial for the student planner. Thus, we design an information bottleneck based strategy to only distill planning-relevant information, rather than transfer all information indiscriminately. Second, different waypoints in an output planned trajectory may hold varying degrees of importance for motion planning, where a slight deviation in certain crucial waypoints might lead to a collision. Therefore, we devise a safety-aware waypoint-attentive distillation module that assigns adaptive weights to different waypoints based on the importance, to encourage the student to accurately mimic more crucial waypoints, thereby improving overall safety. Experiments demonstrate that our PlanKD can boost the performance of smaller planners by a large margin, and significantly reduce their reference time.

### Bootstrapping Autonomous Driving Radars with Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01422)
- **作者**: Yiduo Hao, Sohrab Madani, Junfeng Guan, Mohammed Alloulah, Saurabh Gupta, Haitham Hassanieh
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving.
- **链接**: [arXiv:2404.04804](https://arxiv.org/abs/2404.04804) · 📚 被引 74
- **作者**: Jinlong Li, Baolu Li, Zhengzhong Tu, Xinyu Liu, Qing Guo, Felix Juefei-Xu et al.
- **🏷️ 机构**: Cleveland State University, University of Texas at Austin, Centre for Frontier AI Research (CFAR), A&#x002A;STAR
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-centric perception systems for autonomous driving have gained considerable attention recently due to their cost-effectiveness and scalability, especially compared to LiDAR-based systems. However, these systems often struggle in low-light conditions, potentially compromising their performance and safety. To address this, our paper introduces LightDiff, a domain-tailored framework designed to enhance the low-light image quality for autonomous driving applications. Specifically, we employ a multi-condition controlled diffusion model. LightDiff works without any human-collected paired data, leveraging a dynamic data degradation process instead. It incorporates a novel multi-condition adapter that adaptively controls the input weights from different modalities, including depth maps, RGB images, and text captions, to effectively illuminate dark scenes while maintaining context consistency. Furthermore, to align the enhanced images with the detection model's knowledge, LightDiff employs perception-specific scores as rewards to guide the diffusion training process through reinforcement learning. Extensive experiments on the nuScenes datasets demonstrate that LightDiff can significantly improve the performance of several state-of-the-art 3D detectors in night-time conditions while achieving high visual quality scores, highlighting its potential to safeguard autonomous driving.

### Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving?
- **链接**: [arXiv:2312.03031](https://arxiv.org/abs/2312.03031) · [代码](https://github.com/NVlabs/BEV-Planner) · 📚 被引 86
- **作者**: Zhiqi Li, Zhiding Yu, Shiyi Lan, Jiahan Li, Jan Kautz, Tong Lu et al.
- **🏷️ 机构**: Nanjing University,National Key Lab for Novel Software Technology, NVIDIA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > End-to-end autonomous driving recently emerged as a promising research direction to target autonomy from a full-stack perspective. Along this line, many of the latest works follow an open-loop evaluation setting on nuScenes to study the planning behavior. In this paper, we delve deeper into the problem by conducting thorough analyses and demystifying more devils in the details. We initially observed that the nuScenes dataset, characterized by relatively simple driving scenarios, leads to an under-utilization of perception information in end-to-end models incorporating ego status, such as the ego vehicle's velocity. These models tend to rely predominantly on the ego vehicle's status for future path planning. Beyond the limitations of the dataset, we also note that current metrics do not comprehensively assess the planning quality, leading to potentially biased conclusions drawn from existing benchmarks. To address this issue, we introduce a new metric to evaluate whether the predicted trajectories adhere to the road. We further propose a simple baseline able to achieve competitive results without relying on perception annotations. Given the current limitations on the benchmark and metrics, we suggest the community reassess relevant prevailing research and be cautious whether the continued pursuit of state-of-the-art would yield convincing and universal conclusions. Code and models are available at \url{https://github.com/NVlabs/BEV-Planner}

### DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving.
- **链接**: [arXiv:2405.04390](https://arxiv.org/abs/2405.04390) · 📚 被引 33
- **作者**: Chen Min, Dawei Zhao, Liang Xiao, Jian Zhao, Xinli Xu, Zheng Zhu et al.
- **🏷️ 机构**: School of Computer Science, Peking University, Unmanned Systems Technology Research Center, Defense Innovation Institute, China Telecom Institute of AI &#x0026; NPU
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-centric autonomous driving has recently raised wide attention due to its lower cost. Pre-training is essential for extracting a universal representation. However, current vision-centric pre-training typically relies on either 2D or 3D pre-text tasks, overlooking the temporal characteristics of autonomous driving as a 4D scene understanding task. In this paper, we address this challenge by introducing a world model-based autonomous driving 4D representation learning framework, dubbed \emph{DriveWorld}, which is capable of pre-training from multi-camera driving videos in a spatio-temporal fashion. Specifically, we propose a Memory State-Space Model for spatio-temporal modelling, which consists of a Dynamic Memory Bank module for learning temporal-aware latent dynamics to predict future changes and a Static Scene Propagation module for learning spatial-aware latent statics to offer comprehensive scene contexts. We additionally introduce a Task Prompt to decouple task-aware features for various downstream tasks. The experiments demonstrate that DriveWorld delivers promising results on various autonomous driving tasks. When pre-trained with the OpenScene dataset, DriveWorld achieves a 7.5% increase in mAP for 3D object detection, a 3.0% increase in IoU for online mapping, a 5.0% increase in AMOTA for multi-object tracking, a 0.1m decrease in minADE for motion forecasting, a 3.0% increase in IoU for occupancy prediction, and a 0.34m reduction in average L2 error for planning.

### VLP: Vision Language Planning for Autonomous Driving.
- **链接**: [arXiv:2401.05577](https://arxiv.org/abs/2401.05577) · 📚 被引 85
- **作者**: Chenbin Pan, Burhaneddin Yaman, Tommaso Nesti, Abhirup Mallik, Alessandro Gabriele Allievi, Senem Velipasalar et al.
- **🏷️ 机构**: Syracuse University, Bosch Research North America &#x0026; Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Autonomous driving is a complex and challenging task that aims at safe motion planning through scene understanding and reasoning. While vision-only autonomous driving methods have recently achieved notable performance, through enhanced scene understanding, several key issues, including lack of reasoning, low generalization performance and long-tail scenarios, still need to be addressed. In this paper, we present VLP, a novel Vision-Language-Planning framework that exploits language models to bridge the gap between linguistic understanding and autonomous driving. VLP enhances autonomous driving systems by strengthening both the source memory foundation and the self-driving car's contextual understanding. VLP achieves state-of-the-art end-to-end planning performance on the challenging NuScenes dataset by achieving 35.9\% and 60.5\% reduction in terms of average L2 error and collision rates, respectively, compared to the previous best method. Moreover, VLP shows improved performance in challenging long-tail scenarios and strong generalization capabilities when faced with new urban environments.

### Adversarial Backdoor Attack by Naturalistic Data Poisoning on Trajectory Prediction in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01410) · 📚 被引 16
- **作者**: Mozhgan Pourkeshavarz, Mohammad Sabokrou, Amir Rasouli
- **🏷️ 机构**: Noah&#x0027;s Ark Lab,Huawei,Canada, Okinawa Institute of Science and Technology (OIST)
- **会议**: CVPR 2024

### CaDeT: A Causal Disentanglement Approach for Robust Trajectory Prediction in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01409) · 📚 被引 25
- **作者**: Mozhgan Pourkeshavarz, Junrui Zhang, Amir Rasouli
- **🏷️ 机构**: Noah&#x0027;s Ark Lab,Huawei,Canada
- **会议**: CVPR 2024

### NeuRAD: Neural Rendering for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01411) · 📚 被引 90
- **作者**: Adam Tonderski, Carl Lindström, Georg Hess, William Ljungbergh, Lennart Svensson, Christoffer Petersson
- **🏷️ 机构**: Zenseact, Chalmers University of Technology
- **会议**: CVPR 2024

### Editable Scene Simulation for Autonomous Driving via Collaborative LLM-Agents.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01428) · 📚 被引 78
- **作者**: Yuxi Wei, Zi Wang, Yifan Lu, Chenxin Xu, Changxing Liu, Hao Zhao et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Carnegie Mellon University, Tsinghua University
- **会议**: CVPR 2024

### Panacea: Panoramic and Controllable Video Generation for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00659) · 📚 被引 0
- **作者**: Yuqing Wen, Yucheng Zhao, Yingfei Liu, Fan Jia, Yanhui Wang, Chong Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### PARA-Drive: Parallelized Architecture for Real-Time Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01463) · 📚 被引 67
- **作者**: Xinshuo Weng, Boris Ivanovic, Yan Wang, Yue Wang, Marco Pavone
- **🏷️ 机构**: NVIDIA Research
- **会议**: CVPR 2024

### SynFog: A Photorealistic Synthetic Fog Dataset Based on End-to-End Imaging Simulation for Advancing Real-World Defogging in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02056) · 📚 被引 22
- **作者**: Yiming Xie, Henglu Wei, Zhenyi Liu, Xiaoyu Wang, Xiangyang Ji
- **🏷️ 机构**: Tsinghua University, Stanford University
- **会议**: CVPR 2024

### Generalized Predictive Model for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01389)
- **作者**: Jiazhi Yang, Shenyuan Gao, Yihang Qiu, Li Chen, Tianyu Li, Bo Dai et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2024

### UniPAD: A Universal Pre-Training Paradigm for Autonomous Driving.
- **链接**: [arXiv:2310.08370](https://arxiv.org/abs/2310.08370) · [代码](https://github.com/Nightmare-n/UniPAD) · 📚 被引 42
- **作者**: Honghui Yang, Sha Zhang, Di Huang, Xiaoyang Wu, Haoyi Zhu, Tong He et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, Shanghai Artificial Intelligence Laboratory, HongKong University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the context of autonomous driving, the significance of effective feature learning is widely acknowledged. While conventional 3D self-supervised pre-training methods have shown widespread success, most methods follow the ideas originally designed for 2D images. In this paper, we present UniPAD, a novel self-supervised learning paradigm applying 3D volumetric differentiable rendering. UniPAD implicitly encodes 3D space, facilitating the reconstruction of continuous 3D shape structures and the intricate appearance characteristics of their 2D projections. The flexibility of our method enables seamless integration into both 2D and 3D frameworks, enabling a more holistic comprehension of the scenes. We manifest the feasibility and effectiveness of UniPAD by conducting extensive experiments on various downstream 3D tasks. Our method significantly improves lidar-, camera-, and lidar-camera-based baseline by 9.1, 7.7, and 6.9 NDS, respectively. Notably, our pre-training pipeline achieves 73.2 NDS for 3D object detection and 79.4 mIoU for 3D semantic segmentation on the nuScenes validation set, achieving state-of-the-art results in comparison with previous methods. The code will be available at https://github.com/Nightmare-n/UniPAD.

### Feedback-Guided Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01421)
- **作者**: Jimuyang Zhang, Zanming Huang, Arijit Ray, Eshed Ohn-Bar
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### PACER+: On-Demand Pedestrian Animation Controller in Driving Scenarios.
- **链接**: [arXiv:2404.19722](https://arxiv.org/abs/2404.19722) · 📚 被引 12
- **作者**: Jingbo Wang, Zhengyi Luo, Ye Yuan, Yixuan Li, Bo Dai
- **🏷️ 机构**: Shanghai AI Lab, Carnegie Mellon University, NVIDIA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We address the challenge of content diversity and controllability in pedestrian simulation for driving scenarios. Recent pedestrian animation frameworks have a significant limitation wherein they primarily focus on either following trajectory [46] or the content of the reference video [57], consequently overlooking the potential diversity of human motion within such scenarios. This limitation restricts the ability to generate pedestrian behaviors that exhibit a wider range of variations and realistic motions and therefore restricts its usage to provide rich motion content for other components in the driving simulation system, e.g., suddenly changed motion to which the autonomous vehicle should respond. In our approach, we strive to surpass the limitation by showcasing diverse human motions obtained from various sources, such as generated human motions, in addition to following the given trajectory. The fundamental contribution of our framework lies in combining the motion tracking task with trajectory following, which enables the tracking of specific motion parts (e.g., upper body) while simultaneously following the given trajectory by a single policy. This way, we significantly enhance both the diversity of simulated human motion within the given scenario and the controllability of the content, including language-based control. Our framework facilitates the generation of a wide range of human motions, contributing to greater realism and adaptability in pedestrian simulations for driving scenarios. More information is on our project page https://wangjingbo1219.github.io/papers/CVPR2024_PACER_PLUS/PACERPLUSPage.html .

### Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset.
- **链接**: [arXiv:2406.09383](https://arxiv.org/abs/2406.09383) · 📚 被引 16
- **作者**: Yiming Li, Zhiheng Li, Nuo Chen, Moonjun Gong, Zonglin Lyu, Zehong Wang et al.
- **🏷️ 机构**: New York University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large-scale datasets have fueled recent advancements in AI-based autonomous vehicle research. However, these datasets are usually collected from a single vehicle's one-time pass of a certain location, lacking multiagent interactions or repeated traversals of the same place. Such information could lead to transformative enhancements in autonomous vehicles' perception, prediction, and planning capabilities. To bridge this gap, in collaboration with the self-driving company May Mobility, we present the MARS dataset which unifies scenarios that enable MultiAgent, multitraveRSal, and multimodal autonomous vehicle research. More specifically, MARS is collected with a fleet of autonomous vehicles driving within a certain geographical area. Each vehicle has its own route and different vehicles may appear at nearby locations. Each vehicle is equipped with a LiDAR and surround-view RGB cameras. We curate two subsets in MARS: one facilitates collaborative driving with multiple vehicles simultaneously present at the same location, and the other enables memory retrospection through asynchronous traversals of the same location by multiple vehicles. We conduct experiments in place recognition and neural reconstruction. More importantly, MARS introduces new research opportunities and challenges such as multitraversal 3D reconstruction, multiagent perception, and unsupervised object discovery. Our data and codes can be found at https://ai4ce.github.io/MARS/.

### Dualad: Disentangling the Dynamic and Static World for End-to-End Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01395) · 📚 被引 7
- **作者**: Simon Doll, Niklas Hanselmann, Lukas Schneider, Richard Schulz, Marius Cordts, Markus Enzweiler et al.
- **🏷️ 机构**: Mercedes-Benz AG, Esslingen University of Applied Sciences, University of T&#x00FC;bingen
- **会议**: CVPR 2024

### LMDrive: Closed-Loop End-to-End Driving with Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01432) · 📚 被引 178
- **作者**: Hao Shao, Yuxuan Hu, Letian Wang, Guanglu Song, Steven L. Waslander, Yu Liu et al.
- **🏷️ 机构**: CUHKMMLab, CPII under InnoHK, University of Toronto
- **会议**: CVPR 2024
