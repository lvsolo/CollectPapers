# Autonomous Driving — 2023 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Transformer-Based Sensor Fusion for Autonomous Driving: A Survey.
- **链接**: [arXiv:2302.11481](https://arxiv.org/abs/2302.11481) · [代码](https://github.com/ApoorvRoboticist/Transformers-Sensor-Fusion) · 📚 被引 34
- **作者**: Apoorv Singh
- **🏷️ 机构**: Motional Carnegie Mellon University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sensor fusion is an essential topic in many perception systems, such as autonomous driving and robotics. Transformers-based detection head and CNN-based feature encoder to extract features from raw sensor-data has emerged as one of the best performing sensor-fusion 3D-detection-framework, according to the dataset leaderboards. In this work we provide an in-depth literature survey of transformer based 3D-object detection task in the recent past, primarily focusing on the sensor fusion. We also briefly go through the Vision transformers (ViT) basics, so that readers can easily follow through the paper. Moreover, we also briefly go through few of the non-transformer based less-dominant methods for sensor fusion for autonomous driving. In conclusion we summarize with sensor-fusion trends to follow and provoke future research. More updated summary can be found at: https://github.com/ApoorvRoboticist/Transformers-Sensor-Fusion

</details>

### Optimizing the Placement of Roadside LiDARs for Autonomous Driving.
- **链接**: [arXiv:2310.07247](https://arxiv.org/abs/2310.07247) · 📚 被引 19
- **作者**: Wentao Jiang, Hao Xiang, Xinyu Cai, Runsheng Xu, Jiaqi Ma, Yikang Li et al.
- **🏷️ 机构**: Beihang University, UCLA, Shanghai AI Laboratory
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-agent cooperative perception is an increasingly popular topic in the field of autonomous driving, where roadside LiDARs play an essential role. However, how to optimize the placement of roadside LiDARs is a crucial but often overlooked problem. This paper proposes an approach to optimize the placement of roadside LiDARs by selecting optimized positions within the scene for better perception performance. To efficiently obtain the best combination of locations, a greedy algorithm based on perceptual gain is proposed, which selects the location that can maximize the perceptual gain sequentially. We define perceptual gain as the increased perceptual capability when a new LiDAR is placed. To obtain the perception capability, we propose a perception predictor that learns to evaluate LiDAR placement using only a single point cloud frame. A dataset named Roadside-Opt is created using the CARLA simulator to facilitate research on the roadside LiDAR placement problem.

</details>

### MV-DeepSDF: Implicit Modeling with Multi-Sweep Point Clouds for 3D Vehicle Reconstruction in Autonomous Driving.
- **链接**: [arXiv:2309.16715](https://arxiv.org/abs/2309.16715) · 📚 被引 15
- **作者**: Yibo Liu, Kelly Zhu, Guile Wu, Yuan Ren, Bingbing Liu, Yang Liu et al.
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab, York University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing 3D vehicles from noisy and sparse partial point clouds is of great significance to autonomous driving. Most existing 3D reconstruction methods cannot be directly applied to this problem because they are elaborately designed to deal with dense inputs with trivial noise. In this work, we propose a novel framework, dubbed MV-DeepSDF, which estimates the optimal Signed Distance Function (SDF) shape representation from multi-sweep point clouds to reconstruct vehicles in the wild. Although there have been some SDF-based implicit modeling methods, they only focus on single-view-based reconstruction, resulting in low fidelity. In contrast, we first analyze multi-sweep consistency and complementarity in the latent feature space and propose to transform the implicit space shape estimation problem into an element-to-set feature extraction problem. Then, we devise a new architecture to extract individual element-level representations and aggregate them to generate a set-level predicted latent code. This set-level latent code is an expression of the optimal 3D shape in the implicit space, and can be subsequently decoded to a continuous SDF of the vehicle. In this way, our approach learns consistent and complementary information among multi-sweeps for 3D vehicle reconstruction. We conduct thorough experiments on two real-world autonomous driving datasets (Waymo and KITTI) to demonstrate the superiority of our approach over state-of-the-art alternative methods both qualitatively and quantitatively.

</details>

### SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01986)
- **作者**: Yi Wei, Linqing Zhao, Wenzhao Zheng, Zheng Zhu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Zenseact Open Dataset: A large-scale and diverse multimodal dataset for autonomous driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01846) · 📚 被引 70
- **作者**: Mina Alibeigi, William Ljungbergh, Adam Tonderski, Georg Hess, Adam Lilja, Carl Lindström et al.
- **🏷️ 机构**: Zenseact
- **会议**: ICCV 2023

### Video Task Decathlon: Unifying Image and Video Tasks in Autonomous Driving.
- **链接**: [arXiv:2309.04422](https://arxiv.org/abs/2309.04422) · 📚 被引 11
- **作者**: Thomas E. Huang, Yifan Liu, Luc Van Gool, Fisher Yu
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Performing multiple heterogeneous visual tasks in dynamic scenes is a hallmark of human perception capability. Despite remarkable progress in image and video recognition via representation learning, current research still focuses on designing specialized networks for singular, homogeneous, or simple combination of tasks. We instead explore the construction of a unified model for major image and video recognition tasks in autonomous driving with diverse input and output structures. To enable such an investigation, we design a new challenge, Video Task Decathlon (VTD), which includes ten representative image and video tasks spanning classification, segmentation, localization, and association of objects and pixels. On VTD, we develop our unified network, VTDNet, that uses a single structure and a single set of weights for all ten tasks. VTDNet groups similar tasks and employs task interaction stages to exchange information within and between task groups. Given the impracticality of labeling all tasks on all frames, and the performance degradation associated with joint training of many tasks, we design a Curriculum training, Pseudo-labeling, and Fine-tuning (CPF) scheme to successfully train VTDNet on all tasks and mitigate performance loss. Armed with CPF, VTDNet significantly outperforms its single-task counterparts on most tasks with only 20% overall computations. VTD is a promising new direction for exploring the unification of perception tasks in autonomous driving.

</details>

### GameFormer: Game-theoretic Modeling and Learning of Transformer-based Interactive Prediction and Planning for Autonomous Driving.
- **链接**: [arXiv:2303.05760](https://arxiv.org/abs/2303.05760) · 📚 被引 145
- **作者**: Zhiyu Huang, Haochen Liu, Chen Lv
- **🏷️ 机构**: Nanyang Technological University,Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous vehicles operating in complex real-world environments require accurate predictions of interactive behaviors between traffic participants. This paper tackles the interaction prediction problem by formulating it with hierarchical game theory and proposing the GameFormer model for its implementation. The model incorporates a Transformer encoder, which effectively models the relationships between scene elements, alongside a novel hierarchical Transformer decoder structure. At each decoding level, the decoder utilizes the prediction outcomes from the previous level, in addition to the shared environmental context, to iteratively refine the interaction process. Moreover, we propose a learning process that regulates an agent's behavior at the current level to respond to other agents' behaviors from the preceding level. Through comprehensive experiments on large-scale real-world driving datasets, we demonstrate the state-of-the-art accuracy of our model on the Waymo interaction prediction task. Additionally, we validate the model's capacity to jointly reason about the motion plan of the ego agent and the behaviors of multiple agents in both open-loop and closed-loop planning tests, outperforming various baseline methods. Furthermore, we evaluate the efficacy of our model on the nuPlan planning benchmark, where it achieves leading performance.

</details>

### DriveAdapter: Breaking the Coupling Barrier of Perception and Planning in End-to-End Autonomous Driving.
- **链接**: [arXiv:2308.00398](https://arxiv.org/abs/2308.00398) · 📚 被引 76
- **作者**: Xiaosong Jia, Yulu Gao, Li Chen, Junchi Yan, Patrick Langechuan Liu, Hongyang Li
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Shanghai AI Lab,OpenDriveLab, Anker Innovations
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving aims to build a fully differentiable system that takes raw sensor data as inputs and directly outputs the planned trajectory or control signals of the ego vehicle. State-of-the-art methods usually follow the `Teacher-Student' paradigm. The Teacher model uses privileged information (ground-truth states of surrounding agents and map elements) to learn the driving strategy. The student model only has access to raw sensor data and conducts behavior cloning on the data collected by the teacher model. By eliminating the noise of the perception part during planning learning, state-of-the-art works could achieve better performance with significantly less data compared to those coupled ones. However, under the current Teacher-Student paradigm, the student model still needs to learn a planning head from scratch, which could be challenging due to the redundant and noisy nature of raw sensor inputs and the casual confusion issue of behavior cloning. In this work, we aim to explore the possibility of directly adopting the strong teacher model to conduct planning while letting the student model focus more on the perception part. We find that even equipped with a SOTA perception model, directly letting the student model learn the required inputs of the teacher model leads to poor driving performance, which comes from the large distribution gap between predicted privileged inputs and the ground-truth. To this end, we propose DriveAdapter, which employs adapters with the feature alignment objective function between the student (perception) and teacher (planning) modules. Additionally, since the pure learning-based teacher model itself is imperfect and occasionally breaks safety rules, we propose a method of action-guided feature learning with a mask for those imperfect teacher features to further inject the priors of hand-crafted rules into the learning process.

</details>

### VAD: Vectorized Scene Representation for Efficient Autonomous Driving.
- **链接**: [arXiv:2303.12077](https://arxiv.org/abs/2303.12077) · [代码](https://github.com/hustvl/VAD) · 📚 被引 319
- **作者**: Bo Jiang, Shaoyu Chen, Qing Xu, Bencheng Liao, Jiajie Chen, Helong Zhou et al.
- **🏷️ 机构**: Huazhong University of Science &amp; Technology, Horizon Robotics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving requires a comprehensive understanding of the surrounding environment for reliable trajectory planning. Previous works rely on dense rasterized scene representation (e.g., agent occupancy and semantic map) to perform planning, which is computationally intensive and misses the instance-level structure information. In this paper, we propose VAD, an end-to-end vectorized paradigm for autonomous driving, which models the driving scene as a fully vectorized representation. The proposed vectorized paradigm has two significant advantages. On one hand, VAD exploits the vectorized agent motion and map elements as explicit instance-level planning constraints which effectively improves planning safety. On the other hand, VAD runs much faster than previous end-to-end planning methods by getting rid of computation-intensive rasterized representation and hand-designed post-processing steps. VAD achieves state-of-the-art end-to-end planning performance on the nuScenes dataset, outperforming the previous best method by a large margin. Our base model, VAD-Base, greatly reduces the average collision rate by 29.0% and runs 2.5x faster. Besides, a lightweight variant, VAD-Tiny, greatly improves the inference speed (up to 9.3x) while achieving comparable planning performance. We believe the excellent performance and the high efficiency of VAD are critical for the real-world deployment of an autonomous driving system. Code and models are available at https://github.com/hustvl/VAD for facilitating future research.

</details>

### Unsupervised 3D Perception with 2D Vision-Language Distillation for Autonomous Driving.
- **链接**: [arXiv:2309.14491](https://arxiv.org/abs/2309.14491) · 📚 被引 27
- **作者**: Mahyar Najibi, Jingwei Ji, Yin Zhou, Charles R. Qi, Xinchen Yan, Scott Ettinger et al.
- **🏷️ 机构**: Waymo LLC
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Closed-set 3D perception models trained on only a pre-defined set of object categories can be inadequate for safety critical applications such as autonomous driving where new object types can be encountered after deployment. In this paper, we present a multi-modal auto labeling pipeline capable of generating amodal 3D bounding boxes and tracklets for training models on open-set categories without 3D human labels. Our pipeline exploits motion cues inherent in point cloud sequences in combination with the freely available 2D image-text pairs to identify and track all traffic participants. Compared to the recent studies in this domain, which can only provide class-agnostic auto labels limited to moving objects, our method can handle both static and moving objects in the unsupervised manner and is able to output open-vocabulary semantic labels thanks to the proposed vision-language knowledge distillation. Experiments on the Waymo Open Dataset show that our approach outperforms the prior work by significant margins on various unsupervised 3D perception tasks.

</details>

### Domain generalization of 3D semantic segmentation in autonomous driving.
- **链接**: [arXiv:2212.04245](https://arxiv.org/abs/2212.04245) · [代码](https://github.com/JulesSanchez/3DLabelProp) · 📚 被引 34
- **作者**: Jules Sanchez, Jean-Emmanuel Deschaud, François Goulette
- **🏷️ 机构**: Mines Paris - PSL, PSL University,Centre for Robotics,Paris,France,75006
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Using deep learning, 3D autonomous driving semantic segmentation has become a well-studied subject, with methods that can reach very high performance. Nonetheless, because of the limited size of the training datasets, these models cannot see every type of object and scene found in real-world applications. The ability to be reliable in these various unknown environments is called \textup{domain generalization}. Despite its importance, domain generalization is relatively unexplored in the case of 3D autonomous driving semantic segmentation. To fill this gap, this paper presents the first benchmark for this application by testing state-of-the-art methods and discussing the difficulty of tackling Laser Imaging Detection and Ranging (LiDAR) domain shifts. We also propose the first method designed to address this domain generalization, which we call 3DLabelProp. This method relies on leveraging the geometry and sequentiality of the LiDAR data to enhance its generalization performances by working on partially accumulated point clouds. It reaches a mean Intersection over Union (mIoU) of 50.4% on SemanticPOSS and of 55.2% on PandaSet solid-state LiDAR while being trained only on SemanticKITTI, making it the state-of-the-art method for generalization (+5% and +33% better, respectively, than the second best method). The code for this method is available on GitHub: https://github.com/JulesSanchez/3DLabelProp.

</details>

### Does Physical Adversarial Example Really Matter to Autonomous Driving? Towards System-Level Effect of Adversarial Object Evasion Attack.
- **链接**: [arXiv:2308.11894](https://arxiv.org/abs/2308.11894) · 📚 被引 7
- **作者**: Ningfei Wang, Yunpeng Luo, Takami Sato, Kaidi Xu, Qi Alfred Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving (AD), accurate perception is indispensable to achieving safe and secure driving. Due to its safety-criticality, the security of AD perception has been widely studied. Among different attacks on AD perception, the physical adversarial object evasion attacks are especially severe. However, we find that all existing literature only evaluates their attack effect at the targeted AI component level but not at the system level, i.e., with the entire system semantics and context such as the full AD pipeline. Thereby, this raises a critical research question: can these existing researches effectively achieve system-level attack effects (e.g., traffic rule violations) in the real-world AD context? In this work, we conduct the first measurement study on whether and how effectively the existing designs can lead to system-level effects, especially for the STOP sign-evasion attacks due to their popularity and severity. Our evaluation results show that all the representative prior works cannot achieve any system-level effects. We observe two design limitations in the prior works: 1) physical model-inconsistent object size distribution in pixel sampling and 2) lack of vehicle plant model and AD system model consideration. Then, we propose SysAdv, a novel system-driven attack design in the AD context and our evaluation results show that the system-level effects can be significantly improved, i.e., the violation rate increases by around 70%.

</details>

### Learning Human Dynamics in Autonomous Driving Scenarios.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01901) · 📚 被引 23
- **作者**: Jingbo Wang, Ye Yuan, Zhengyi Luo, Kevin Xie, Dahua Lin, Umar Iqbal et al.
- **🏷️ 机构**: NVIDIA, The Chinese University of Hong Kong
- **会议**: ICCV 2023

### SemARFlow: Injecting Semantics into Unsupervised Optical Flow Estimation for Autonomous Driving.
- **链接**: [arXiv:2303.06209](https://arxiv.org/abs/2303.06209) · [代码](https://github.com/duke-vision/semantic-unsup-flow-release) · 📚 被引 8
- **作者**: Shuai Yuan, Shuzhi Yu, Hannah Kim, Carlo Tomasi
- **🏷️ 机构**: Duke University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised optical flow estimation is especially hard near occlusions and motion boundaries and in low-texture regions. We show that additional information such as semantics and domain knowledge can help better constrain this problem. We introduce SemARFlow, an unsupervised optical flow network designed for autonomous driving data that takes estimated semantic segmentation masks as additional inputs. This additional information is injected into the encoder and into a learned upsampler that refines the flow output. In addition, a simple yet effective semantic augmentation module provides self-supervision when learning flow and its boundaries for vehicles, poles, and sky. Together, these injections of semantic information improve the KITTI-2015 optical flow test error rate from 11.80% to 8.38%. We also show visible improvements around object boundaries as well as a greater ability to generalize across datasets. Code is available at https://github.com/duke-vision/semantic-unsup-flow-release.

</details>

### Exploring the Road Graph in Trajectory Forecasting for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00014) · 📚 被引 6
- **作者**: Rémy Sun, Diane Lingrand, Frédéric Precioso
- **🏷️ 机构**: Universit&#x00E9; C&#x00F4;te d&#x2019;Azur,Inria, CNRS, I3S,Maasai,Nice,France
- **会议**: ICCV 2023

### Sensitivity analysis of AI-based algorithms for autonomous driving on optical wavefront aberrations induced by the windshield.
- **链接**: [arXiv:2308.11711](https://arxiv.org/abs/2308.11711) · 📚 被引 1
- **作者**: Dominik Werner Wolf, Markus Ulrich, Nikhil Kapoor
- **🏷️ 机构**: Volkswagen Group, Karlsruhe Institute of Technology, CARIAD SE
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving perception techniques are typically based on supervised machine learning models that are trained on real-world street data. A typical training process involves capturing images with a single car model and windshield configuration. However, deploying these trained models on different car types can lead to a domain shift, which can potentially hurt the neural networks performance and violate working ADAS requirements. To address this issue, this paper investigates the domain shift problem further by evaluating the sensitivity of two perception models to different windshield configurations. This is done by evaluating the dependencies between neural network benchmark metrics and optical merit functions by applying a Fourier optics based threat model. Our results show that there is a performance gap introduced by windshields and existing optical metrics used for posing requirements might not be sufficient.

</details>

### Hidden Biases of End-to-End Driving Models.
- **链接**: [arXiv:2306.07957](https://arxiv.org/abs/2306.07957) · 📚 被引 72
- **作者**: Bernhard Jaeger, Kashyap Chitta, Andreas Geiger
- **🏷️ 机构**: University of T&#x00FC;bingen,T&#x00FC;bingen AI Center
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end driving systems have recently made rapid progress, in particular on CARLA. Independent of their major contribution, they introduce changes to minor system components. Consequently, the source of improvements is unclear. We identify two biases that recur in nearly all state-of-the-art methods and are critical for the observed progress on CARLA: (1) lateral recovery via a strong inductive bias towards target point following, and (2) longitudinal averaging of multimodal waypoint predictions for slowing down. We investigate the drawbacks of these biases and identify principled alternatives. By incorporating our insights, we develop TF++, a simple end-to-end method that ranks first on the Longest6 and LAV benchmarks, gaining 11 driving score over the best prior work on Longest6.

</details>

### Unsupervised Self-Driving Attention Prediction via Uncertainty Mining and Knowledge Embedding.
- **链接**: [arXiv:2303.09706](https://arxiv.org/abs/2303.09706) · 📚 被引 14
- **作者**: Pengfei Zhu, Mengshi Qi, Xia Li, Weijian Li, Huadong Ma
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,Beijing Key Laboratory of Intelligent Telecommunications Software and Multimedia,Beijing,100876, University of Rochester,Department of Computer Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting attention regions of interest is an important yet challenging task for self-driving systems. Existing methodologies rely on large-scale labeled traffic datasets that are labor-intensive to obtain. Besides, the huge domain gap between natural scenes and traffic scenes in current datasets also limits the potential for model training. To address these challenges, we are the first to introduce an unsupervised way to predict self-driving attention by uncertainty modeling and driving knowledge integration. Our approach's Uncertainty Mining Branch (UMB) discovers commonalities and differences from multiple generated pseudo-labels achieved from models pre-trained on natural scenes by actively measuring the uncertainty. Meanwhile, our Knowledge Embedding Block (KEB) bridges the domain gap by incorporating driving knowledge to adaptively refine the generated pseudo-labels. Quantitative and qualitative results with equivalent or even more impressive performance compared to fully-supervised state-of-the-art approaches across all three public datasets demonstrate the effectiveness of the proposed method and the potential of this direction. The code will be made publicly available.

</details>

### Unsupervised Domain Adaptation for Self-Driving from Past Traversal Features.
- **链接**: [arXiv:2309.12140](https://arxiv.org/abs/2309.12140) · [代码](https://github.com/zhangtravis/Hist-DA) · 📚 被引 2
- **作者**: Travis Zhang, Katie Luo, Cheng Perng Phoo, Yurong You, Wei-Lun Chao, Bharath Hariharan et al.
- **🏷️ 机构**: Cornell University, The Ohio State University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid development of 3D object detection systems for self-driving cars has significantly improved accuracy. However, these systems struggle to generalize across diverse driving environments, which can lead to safety-critical failures in detecting traffic participants. To address this, we propose a method that utilizes unlabeled repeated traversals of multiple locations to adapt object detectors to new driving environments. By incorporating statistics computed from repeated LiDAR scans, we guide the adaptation process effectively. Our approach enhances LiDAR-based detection models using spatial quantized historical features and introduces a lightweight regression head to leverage the statistics for feature regularization. Additionally, we leverage the statistics for a novel self-training process to stabilize the training. The framework is detector model-agnostic and experiments on real-world datasets demonstrate significant improvements, achieving up to a 20-point performance gain, especially in detecting pedestrians and distant objects. Code is available at https://github.com/zhangtravis/Hist-DA.

</details>

## 跨领域论文（完整笔记在其他领域）

- Surround-View Vision-based 3D Detection for Autonomous Driving: A Survey. → [3d-detection](../3d-detection/Guideline%202023.md)
- On Offline Evaluation of 3D Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
