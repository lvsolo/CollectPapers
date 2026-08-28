# Autonomous Driving — 2025 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Spotting the Unexpected (STU): A 3D LiDAR Dataset for Anomaly Segmentation in Autonomous Driving.
- **链接**: [arXiv:2505.02148](https://arxiv.org/abs/2505.02148) · 📚 被引 4
- **作者**: Alexey Nekrasov, Malcolm Burdorf, Stewart Worrall, Bastian Leibe, Julie Stephany Berrio Perez
- **🏷️ 机构**: RWTH Aachen University, The University of Sydney
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To operate safely, autonomous vehicles (AVs) need to detect and handle unexpected objects or anomalies on the road. While significant research exists for anomaly detection and segmentation in 2D, research progress in 3D is underexplored. Existing datasets lack high-quality multimodal data that are typically found in AVs. This paper presents a novel dataset for anomaly segmentation in driving scenarios. To the best of our knowledge, it is the first publicly available dataset focused on road anomaly segmentation with dense 3D semantic labeling, incorporating both LiDAR and camera data, as well as sequential information to enable anomaly detection across various ranges. This capability is critical for the safe navigation of autonomous vehicles. We adapted and evaluated several baseline models for 3D segmentation, highlighting the challenges of 3D anomaly detection in driving environments. Our dataset and evaluation code will be openly available, facilitating the testing and performance comparison of different approaches.

</details>

### SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving.
- **链接**: [arXiv:2411.16816](https://arxiv.org/abs/2411.16816) · 📚 被引 31
- **作者**: Georg Hess, Carl Lindström, Maryam Fatemi, Christoffer Petersson, Lennart Svensson
- **🏷️ 机构**: Zenseact, Chalmers University of Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ensuring the safety of autonomous robots, such as self-driving vehicles, requires extensive testing across diverse driving scenarios. Simulation is a key ingredient for conducting such testing in a cost-effective and scalable way. Neural rendering methods have gained popularity, as they can build simulation environments from collected logs in a data-driven manner. However, existing neural radiance field (NeRF) methods for sensor-realistic rendering of camera and lidar data suffer from low rendering speeds, limiting their applicability for large-scale testing. While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous driving. To address these limitations, we propose SplatAD, the first 3DGS-based method for realistic, real-time rendering of dynamic scenes for both camera and lidar data. SplatAD accurately models key sensor-specific phenomena such as rolling shutter effects, lidar intensity, and lidar ray dropouts, using purpose-built algorithms to optimize rendering efficiency. Evaluation across three autonomous driving datasets demonstrates that SplatAD achieves state-of-the-art rendering quality with up to +2 PSNR for NVS and +3 PSNR for reconstruction while increasing rendering speed over NeRF-based methods by an order of magnitude. See https://research.zenseact.com/publications/splatad/ for our project page.

</details>

### HiLoTs: High-Low Temporal Sensitive Representation Learning for Semi-Supervised LiDAR Segmentation in Autonomous Driving.
- **链接**: [arXiv:2503.17752](https://arxiv.org/abs/2503.17752) · [代码](https://github.com/rdlin118/HiLoTs) · 📚 被引 8
- **作者**: R. D. Lin, Pengcheng Weng, Yinqiao Wang, Han Ding, Jinsong Han, Fei Wang
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering,China, Xi&#x2019;an Jiaotong University,School of Computer Science and Technology,China, Zhejiang University,College of Computer Science and Technology,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR point cloud semantic segmentation plays a crucial role in autonomous driving. In recent years, semi-supervised methods have gained popularity due to their significant reduction in annotation labor and time costs. Current semi-supervised methods typically focus on point cloud spatial distribution or consider short-term temporal representations, e.g., only two adjacent frames, often overlooking the rich long-term temporal properties inherent in autonomous driving scenarios. In driving experience, we observe that nearby objects, such as roads and vehicles, remain stable while driving, whereas distant objects exhibit greater variability in category and shape. This natural phenomenon is also captured by LiDAR, which reflects lower temporal sensitivity for nearby objects and higher sensitivity for distant ones. To leverage these characteristics, we propose HiLoTs, which learns high-temporal sensitivity and low-temporal sensitivity representations from continuous LiDAR frames. These representations are further enhanced and fused using a cross-attention mechanism. Additionally, we employ a teacher-student framework to align the representations learned by the labeled and unlabeled branches, effectively utilizing the large amounts of unlabeled data. Experimental results on the SemanticKITTI and nuScenes datasets demonstrate that our proposed HiLoTs outperforms state-of-the-art semi-supervised methods, and achieves performance close to LiDAR+Camera multimodal approaches. Code is available on https://github.com/rdlin118/HiLoTs

</details>

### SOLVE: Synergy of Language-Vision and End-to-End Networks for Autonomous Driving.
- **链接**: [arXiv:2505.16805](https://arxiv.org/abs/2505.16805) · 📚 被引 6
- **作者**: Xuesong Chen, Linjiang Huang, Tao Ma, Rongyao Fang, Shaoshuai Shi, Hongsheng Li
- **🏷️ 机构**: MMLab,CUHK, Beihang University,Institute of Artificial Intelligence, Didi Chuxing,Voyager Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The integration of Vision-Language Models (VLMs) into autonomous driving systems has shown promise in addressing key challenges such as learning complexity, interpretability, and common-sense reasoning. However, existing approaches often struggle with efficient integration and realtime decision-making due to computational demands. In this paper, we introduce SOLVE, an innovative framework that synergizes VLMs with end-to-end (E2E) models to enhance autonomous vehicle planning. Our approach emphasizes knowledge sharing at the feature level through a shared visual encoder, enabling comprehensive interaction between VLM and E2E components. We propose a Trajectory Chain-of-Thought (T-CoT) paradigm, which progressively refines trajectory predictions, reducing uncertainty and improving accuracy. By employing a temporal decoupling strategy, SOLVE achieves efficient cooperation by aligning high-quality VLM outputs with E2E real-time performance. Evaluated on the nuScenes dataset, our method demonstrates significant improvements in trajectory prediction accuracy, paving the way for more robust and reliable autonomous driving systems.

</details>

### VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving.
- **链接**: [arXiv:2411.14716](https://arxiv.org/abs/2411.14716) · 📚 被引 6
- **作者**: Haiming Zhang, Wending Zhou, Yiyao Zhu, Xu Yan, Jiantao Gao, Dongfeng Bai et al.
- **🏷️ 机构**: FNii,Shenzhen, HKUST, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces VisionPAD, a novel self-supervised pre-training paradigm designed for vision-centric algorithms in autonomous driving. In contrast to previous approaches that employ neural rendering with explicit depth supervision, VisionPAD utilizes more efficient 3D Gaussian Splatting to reconstruct multi-view representations using only images as supervision. Specifically, we introduce a self-supervised method for voxel velocity estimation. By warping voxels to adjacent frames and supervising the rendered outputs, the model effectively learns motion cues in the sequential data. Furthermore, we adopt a multi-frame photometric consistency approach to enhance geometric perception. It projects adjacent frames to the current frame based on rendered depths and relative poses, boosting the 3D geometric representation through pure image supervision. Extensive experiments on autonomous driving datasets demonstrate that VisionPAD significantly improves performance in 3D object detection, occupancy prediction and map segmentation, surpassing state-of-the-art pre-training strategies by a considerable margin.

</details>

### JiSAM: Alleviate Labeling Burden and Corner Case Problems in Autonomous Driving via Minimal Real-World Data.
- **链接**: [arXiv:2503.08422](https://arxiv.org/abs/2503.08422) · 📚 被引 2
- **作者**: Runjian Chen, Wenqi Shao, Bo Zhang, Shaoshuai Shi, Li Jiang, Ping Luo
- **🏷️ 机构**: The University of Hong Kong, Shanghai AI Laboratory, Voyager Research, Didi Chuxing
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep-learning-based autonomous driving (AD) perception introduces a promising picture for safe and environment-friendly transportation. However, the over-reliance on real labeled data in LiDAR perception limits the scale of on-road attempts. 3D real world data is notoriously time-and-energy-consuming to annotate and lacks corner cases like rare traffic participants. On the contrary, in simulators like CARLA, generating labeled LiDAR point clouds with corner cases is a piece of cake. However, introducing synthetic point clouds to improve real perception is non-trivial. This stems from two challenges: 1) sample efficiency of simulation datasets 2) simulation-to-real gaps. To overcome both challenges, we propose a plug-and-play method called JiSAM , shorthand for Jittering augmentation, domain-aware backbone and memory-based Sectorized AlignMent. In extensive experiments conducted on the famous AD dataset NuScenes, we demonstrate that, with SOTA 3D object detector, JiSAM is able to utilize the simulation data and only labels on 2.5% available real data to achieve comparable performance to models trained on all real data. Additionally, JiSAM achieves more than 15 mAPs on the objects not labeled in the real training set.

</details>

### Distilling Multi-modal Large Language Models for Autonomous Driving.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hegde_Distilling_Multi-modal_Large_Language_Models_for_Autonomous_Driving_CVPR_2025_paper.html)
- **作者**: Deepti Hegde, Rajeev Yasarla, Hong Cai, Shizhong Han, Apratim Bhattacharyya, Shweta Mahajan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving.
- **链接**: [arXiv:2411.15139](https://arxiv.org/abs/2411.15139) · [代码](https://github.com/hustvl/DiffusionDrive) · 📚 被引 80
- **作者**: Bencheng Liao, Shaoyu Chen, Haoran Yin, Bo Jiang, Cheng Wang, Sixu Yan et al.
- **🏷️ 机构**: Huazhong University of Science &#x0026; Technology,Institute of Artificial Intelligence, Huazhong University of Science &#x0026; Technology,School of EIC, Horizon Robotics
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the diffusion model has emerged as a powerful generative technique for robotic policy learning, capable of modeling multi-mode action distributions. Leveraging its capability for end-to-end autonomous driving is a promising direction. However, the numerous denoising steps in the robotic diffusion policy and the more dynamic, open-world nature of traffic scenes pose substantial challenges for generating diverse driving actions at a real-time speed. To address these challenges, we propose a novel truncated diffusion policy that incorporates prior multi-mode anchors and truncates the diffusion schedule, enabling the model to learn denoising from anchored Gaussian distribution to the multi-mode driving action distribution. Additionally, we design an efficient cascade diffusion decoder for enhanced interaction with conditional scene context. The proposed model, DiffusionDrive, demonstrates 10$\times$ reduction in denoising steps compared to vanilla diffusion policy, delivering superior diversity and quality in just 2 steps. On the planning-oriented NAVSIM dataset, with the aligned ResNet-34 backbone, DiffusionDrive achieves 88.1 PDMS without bells and whistles, setting a new record, while running at a real-time speed of 45 FPS on an NVIDIA 4090. Qualitative results on challenging scenarios further confirm that DiffusionDrive can robustly generate diverse plausible driving actions. Code and model will be available at https://github.com/hustvl/DiffusionDrive.

</details>

### Temporal Logic-Based Multi-Vehicle Backdoor Attacks against Offline RL Agents in End-to-end Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/656c9f7c3a322e31ce56403cca3ca0f1-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xuan Chen, Shiwei Feng, Zikang Xiong, Shengwei An, Yunshu Mao, Lu Yan et al.
- **🏷️ 机构**: Purdue University, DeepRoute.ai, Virginia Polytechnic Institute and State University
- **会议**: NeurIPS 2025

### TopoPoint: Enhance Topology Reasoning via Endpoint Detection in Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/ab6022d3d669b5baafa24c91d7c407a6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yanping Fu, Xinyuan Liu, Tianyu Li, Yike Ma, Yucheng Zhang, Feng Dai
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences, University of Electronic Science and Technology of China, The Institute of Computing Technology of the Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### Prioritizing Perception-Guided Self-Supervision: A New Paradigm for Causal Modeling in End-to-End Autonomous Driving.
- **链接**: [arXiv:2511.08214](https://arxiv.org/abs/2511.08214) · 📚 被引 0
- **作者**: Yi Huang, Zhan Qu, Lihui Jiang, Bingbing Liu, Hongbo Zhang
- **🏷️ 机构**: The Chinese University of Hong Kong, Huawei Technologies Ltd., Huawei
- **会议**: NeurIPS 2025

### Model-Based Policy Adaptation for Closed-Loop End-to-end Autonomous Driving.
- **链接**: [arXiv:2511.21584](https://arxiv.org/abs/2511.21584) · 📚 被引 0
- **作者**: Haohong Lin, Yunzhi Zhang, Wenhao Ding, Jiajun Wu, Ding Zhao
- **🏷️ 机构**: CMU, Stanford University, Imperial College London
- **会议**: NeurIPS 2025

### GaussianFusion: Gaussian-Based Multi-Sensor Fusion for End-to-End Autonomous Driving.
- **链接**: [arXiv:2506.00034](https://arxiv.org/abs/2506.00034) · 📚 被引 1
- **作者**: Shuai Liu, Quanmin Liang, Zefeng Li, Boyang Li, Kai Huang
- **🏷️ 机构**: SUN YAT-SEN UNIVERSITY, Sun Yat-sen University, Nanyang Technological University
- **会议**: NeurIPS 2025

### Embodied Cognition Augmented End2End Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/3f28c4340f6172c94f28ad913e7c92a6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ling Niu, Xiaoji Zheng, Han Wang, Ziyuan Yang, Chen Zheng, Bokui Chen et al.
- **🏷️ 机构**: Tsinghua University, University of Washington, Tsinghua University, Tsinghua University
- **会议**: NeurIPS 2025

### DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/750337e1301941f81ae31a90e0a1c181-Abstract-Conference.html) · 📚 被引 0
- **作者**: Shuyao Shang, Yuntao Chen, Yuqi Wang, Yingyan Li, Zhao-Xiang Zhang
- **🏷️ 机构**: Institute of automation, Chinese academy of science, Centre for Artificial Intelligence and Robotics, HKISI, CAS, Petuum Inc.
- **会议**: NeurIPS 2025

### Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/36d1e8aa9ceec3b781682bf5e63c31bf-Abstract-Conference.html) · 📚 被引 2
- **作者**: Tianyi Tan, Yinan Zheng, Ruiming Liang, Zexu Wang, Kexin Zheng, Jinliang Zheng et al.
- **🏷️ 机构**: Tsinghua University, Institute of Automation, Chinese Academy of Sciences, The Chinese University of Hong Kong
- **会议**: NeurIPS 2025

### Towards Physics-informed Spatial Intelligence with Human Priors: An Autonomous Driving Pilot Study.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2e0d3c6ad1a4d85bef3cfe63af58bc76-Abstract-Conference.html) · 📚 被引 0
- **作者**: Guanlin Wu, Boyan Su, Yang Zhao, Pu Wang, Yichen Lin, Hao (Frank) Yang
- **🏷️ 机构**: Johns Hopkins University, University of Minnesota - Twin Cities, Mitsubishi Electric Research Labs
- **会议**: NeurIPS 2025

### RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/bb0f9af6a4881ccb6e14c11b8b4be710-Abstract-Conference.html) · 📚 被引 0
- **作者**: Tianyi Yan, Wencheng Han, Xia Zhou, Xueyang Zhang, Kun Zhan, Cheng-Zhong Xu et al.
- **🏷️ 机构**: University of Macau, Li Auto Inc., LiAuto
- **会议**: NeurIPS 2025

### ReSim: Reliable World Simulation for Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f502981cbe221d857ad409450a7917c3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jiazhi Yang, Kashyap Chitta, Shenyuan Gao, Long Chen, Yuqian Shao, Xiaosong Jia et al.
- **🏷️ 机构**: NVIDIA, Hong Kong University of Science and Technology, Shanghai Jiaotong University
- **会议**: NeurIPS 2025

### CodeMerge: Codebook-Guided Model Merging for Robust Test-Time Adaptation in Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/463a91da3c832bd28912cd0d1b8d9974-Abstract-Conference.html) · 📚 被引 0
- **作者**: Huitong Yang, Zhuoxiao Chen, Fengyi Zhang, Zi Huang, Yadan Luo
- **🏷️ 机构**: The University of Queensland, University of Queensland
- **会议**: NeurIPS 2025

### Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2).
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/c2915bc5961edb04e209a524ec167522-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhenjie Yang, Xiaosong Jia, Qifeng Li, Xue Yang, Maoqing Yao, Junchi Yan
- **🏷️ 机构**: Shanghai Jiao Tong University, University of California, Berkeley, Shanghai Jiaotong University
- **会议**: NeurIPS 2025

### FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/61466f2c7a87edfa5898665c70af0e90-Abstract-Conference.html) · 📚 被引 2
- **作者**: Shuang Zeng, Xinyuan Chang, Mengwei Xie, Xinran Liu, Yifan Bai, Zheng Pan et al.
- **🏷️ 机构**: Xi'an Jiaotong University, Alibaba Group, Tongji University
- **会议**: NeurIPS 2025

### CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/66d09284cfb6f125fe888f71dc14f35e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dapeng Zhang, Fei Shen, Rui Zhao, Yinda Chen, Peng Zhi, Chenyang Li et al.
- **🏷️ 机构**: Lanzhou University, Nanjing University of Science and Technology, University of science and technology of China
- **会议**: NeurIPS 2025

### SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving.
- **链接**: [arXiv:2509.16588](https://arxiv.org/abs/2509.16588) · 📚 被引 0
- **作者**: Haiming Zhang, Yiyao Zhu, Wending Zhou, Xu Yan, Yingjie Cai, Bingbing Liu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Shenzhen, Hong Kong University of Science and Technology, The Chinese University of Hongkong, Shenzhen
- **会议**: NeurIPS 2025

### AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning.
- **链接**: [arXiv:2506.13757](https://arxiv.org/abs/2506.13757) · 📚 被引 3
- **作者**: Zewei Zhou, Tianhui Cai, Seth Z. Zhao, Yun Zhang, Zhiyu Huang, Bolei Zhou et al.
- **🏷️ 机构**: University of California, Los Angeles, UCLA Computer Science Department, University of California, Los Angeles, UCLA
- **会议**: NeurIPS 2025

### VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting.
- **链接**: [arXiv:2510.23205](https://arxiv.org/abs/2510.23205) · 📚 被引 0
- **作者**: Hoonhee Cho, Jae-Young Kang, Giwon Lee, Hyemin Yang, Heejun Park, Seokwoo Jung et al.
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology, KAIST, Korea Advanced Institute of Science &amp; Technology
- **会议**: NeurIPS 2025

### RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2ed3a566a0af6dcec424b988f1880ecc-Abstract-Conference.html) · 📚 被引 2
- **作者**: Hao Gao, Shaoyu Chen, Bo Jiang, Bencheng Liao, Yiang Shi, Xiaoyang Guo et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Anhui University, Horizon Robotics
- **会议**: NeurIPS 2025

### SURDS: Benchmarking Spatial Understanding and Reasoning in Driving Scenarios with Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b80285c98ad292e378e31ae18d0fcc1b-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Xianda Guo, Ruijun Zhang, Yiqun Duan, Yuhang He, Dujun Nie, Wenke Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding the traffic scenes and then generating high-definition (HD) maps present significant challenges in autonomous driving. In this paper, we defined a novel Traffic Topology Scene Graph, a unified scene graph explicitly modeling the lane, controlled and guided by different road signals (e.g., right turn), and topology relationships among them, which is always ignored by previous high-definition (HD) mapping methods. For the generation of T2SG, we propose TopoFormer, a novel one-stage Topology Scene Graph TransFormer with two newly designed layers. Specifically, TopoFormer incorporates a Lane Aggregation Layer (LAL) that leverages the geometric distance among the centerline of lanes to guide the aggregation of global information. Furthermore, we proposed a Counterfactual Intervention Layer (CIL) to model the reasonable road structure ( e.g., intersection, straight) among lanes under counterfactual intervention. Then the generated T2SG can provide a more accurate and explainable description of the topological structure in traffic scenes. Experimental results demonstrate that TopoFormer outperforms existing methods on the T2SG generation task, and the generated T2SG significantly enhances traffic topology reasoning in downstream tasks, achieving a state-of-the-art performance of 46.3 OLS on the OpenLane-V2 benchmark. We will release our source code and model.

</details>

### Future-Aware End-to-End Driving: Bidirectional Modeling of Trajectory Planning and Scene Evolution.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/0ee633a6ade45eab4276352b3ee79c7a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Bozhou Zhang, Nan Song, Jingyu Li, Xiatian Zhu, Jiankang Deng, Li Zhang
- **🏷️ 机构**: Fudan University, University of Surrey, Imperial College London
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Integrating large language models (LLMs) into autonomous driving has attracted significant attention with the hope of improving generalization and explainability. However, existing methods often focus on either driving or vision-language understanding but achieving both high driving performance and extensive language understanding remains challenging. In addition, the dominant approach to tackle vision-language understanding is using visual question answering. However, for autonomous driving, this is only useful if it is aligned with the action space. Otherwise, the model's answers could be inconsistent with its behavior. Therefore, we propose a model that can handle three different tasks: (1) closed-loop driving, (2) vision-language understanding, and (3) language-action alignment. Our model SimLingo is based on a vision language model (VLM) and works using only camera, excluding expensive sensors like LiDAR. SimLingo obtains state-of-the-art performance on the widely used CARLA simulator on the Bench2Drive benchmark and is the winning entry at the CARLA challenge 2024. Additionally, we achieve strong results in a wide variety of language-related tasks while maintaining high driving performance.

</details>

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

> Trajectory planning is vital for autonomous driving, ensuring safe and efficient navigation in complex environments. While recent learning-based methods, particularly reinforcement learning (RL), have shown promise in specific scenarios, RL planners struggle with training inefficiencies and managing large-scale, real-world driving scenarios. In this paper, we introduce \textbf{CarPlanner}, a \textbf{C}onsistent \textbf{a}uto-\textbf{r}egressive \textbf{Planner} that uses RL to generate multi-modal trajectories. The auto-regressive structure enables efficient large-scale RL training, while the incorporation of consistency ensures stable policy learning by maintaining coherent temporal consistency across time steps. Moreover, CarPlanner employs a generation-selection framework with an expert-guided reward function and an invariant-view module, simplifying RL training and enhancing policy performance. Extensive analysis demonstrates that our proposed RL framework effectively addresses the challenges of training efficiency and performance enhancement, positioning CarPlanner as a promising solution for trajectory planning in autonomous driving. To the best of our knowledge, we are the first to demonstrate that the RL-based planner can surpass both IL- and rule-based state-of-the-arts (SOTAs) on the challenging large-scale real-world dataset nuPlan. Our proposed CarPlanner surpasses RL-, IL-, and rule-based SOTA approaches within this demanding dataset.

</details>

### MPDrive: Improving Spatial Understanding with Marker-Based Prompt Learning for Autonomous Driving.
- **链接**: [arXiv:2504.00379](https://arxiv.org/abs/2504.00379) · 📚 被引 9
- **作者**: Zhiyuan Zhang, Xiaofan Li, Zhihao Xu, Wenjie Peng, Zijian Zhou, Miaojing Shi et al.
- **🏷️ 机构**: South China University of Technology, Baidu Inc., King&#x2019;s College London
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving visual question answering (AD-VQA) aims to answer questions related to perception, prediction, and planning based on given driving scene images, heavily relying on the model's spatial understanding capabilities. Prior works typically express spatial information through textual representations of coordinates, resulting in semantic gaps between visual coordinate representations and textual descriptions. This oversight hinders the accurate transmission of spatial information and increases the expressive burden. To address this, we propose a novel Marker-based Prompt learning framework (MPDrive), which represents spatial coordinates by concise visual markers, ensuring linguistic expressive consistency and enhancing the accuracy of both visual perception and spatial expression in AD-VQA. Specifically, we create marker images by employing a detection expert to overlay object regions with numerical labels, converting complex textual coordinate generation into straightforward text-based visual marker predictions. Moreover, we fuse original and marker images as scene-level features and integrate them with detection priors to derive instance-level features. By combining these features, we construct dual-granularity visual prompts that stimulate the LLM's spatial perception capabilities. Extensive experiments on the DriveLM and CODA-LM datasets show that MPDrive achieves state-of-the-art performance, particularly in cases requiring sophisticated spatial understanding.

</details>

### Bridging Past and Future: End-to-End Autonomous Driving with Historical Prediction and Planning.
- **链接**: [arXiv:2503.14182](https://arxiv.org/abs/2503.14182) · 📚 被引 7
- **作者**: Bozhou Zhang, Nan Song, Xin Jin, Li Zhang
- **🏷️ 机构**: Fudan University,School of Data Science, Eastern Institute of Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving unifies tasks in a differentiable framework, enabling planning-oriented optimization and attracting growing attention. Current methods aggregate historical information either through dense historical bird's-eye-view (BEV) features or by querying a sparse memory bank, following paradigms inherited from detection. However, we argue that these paradigms either omit historical information in motion planning or fail to align with its multi-step nature, which requires predicting or planning multiple future time steps. In line with the philosophy of future is a continuation of past, we propose BridgeAD, which reformulates motion and planning queries as multi-step queries to differentiate the queries for each future time step. This design enables the effective use of historical prediction and planning by applying them to the appropriate parts of the end-to-end system based on the time steps, which improves both perception and motion planning. Specifically, historical queries for the current frame are combined with perception, while queries for future frames are integrated with motion planning. In this way, we bridge the gap between past and future by aggregating historical insights at every time step, enhancing the overall coherence and accuracy of the end-to-end autonomous driving pipeline. Extensive experiments on the nuScenes dataset in both open-loop and closed-loop settings demonstrate that BridgeAD achieves state-of-the-art performance.

</details>

## 跨领域论文（完整笔记在其他领域）

- OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202025.md)
- Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge. → [3d-detection](../3d-detection/Guideline%202025.md)
