# Autonomous Driving — 2025 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### STSBench: A Spatio-temporal Scenario Benchmark for Multi-modal Large Language Models in Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d7b7c2ff14a479d574b971fd8a36f3e4-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Christian Fruhwirth-Reisinger, Dusan Malic, Wei Lin, David Schinagl, Samuel Schulter, Horst Possegger
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

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

### HCRMP: An LLM-Hinted Contextual Reinforcement Learning Framework for Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9851fb4a60b303319c66d86c36c3a0ef-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhiwen Chen, Hanming Deng, Zhuoren Li, Huanxi Wen, Guizhe Jin, Ran Yu et al.
- **🏷️ 机构**: Tongji University, Sensetime
- **会议**: NeurIPS 2025

### Temporal Logic-Based Multi-Vehicle Backdoor Attacks against Offline RL Agents in End-to-end Autonomous Driving.
- **链接**: [arXiv:2509.16950](https://arxiv.org/abs/2509.16950) · 📚 被引 0
- **作者**: Xuan Chen, Shiwei Feng, Zikang Xiong, Shengwei An, Yunshu Mao, Lu Yan et al.
- **🏷️ 机构**: Purdue University, DeepRoute.ai, Virginia Polytechnic Institute and State University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Assessing the safety of autonomous driving (AD) systems against security threats, particularly backdoor attacks, is a stepping stone for real-world deployment. However, existing works mainly focus on pixel-level triggers that are impractical to deploy in the real world. We address this gap by introducing a novel backdoor attack against the end-to-end AD systems that leverage one or more other vehicles' trajectories as triggers. To generate precise trigger trajectories, we first use temporal logic (TL) specifications to define the behaviors of attacker vehicles. Configurable behavior models are then used to generate these trajectories, which are quantitatively evaluated and iteratively refined based on the TL specifications. We further develop a negative training strategy by incorporating patch trajectories that are similar to triggers but are designated not to activate the backdoor. It enhances the stealthiness of the attack and refines the system's responses to trigger scenarios. Through extensive experiments on 5 offline reinforcement learning (RL) driving agents with 6 trigger patterns and target action combinations, we demonstrate the flexibility and effectiveness of our proposed attack, showing the under-exploration of existing end-to-end AD systems' vulnerabilities to such trajectory-based backdoor attacks.

</details>

### TopoPoint: Enhance Topology Reasoning via Endpoint Detection in Autonomous Driving.
- **链接**: [arXiv:2505.17771](https://arxiv.org/abs/2505.17771) · [代码](https://github.com/Franpin/TopoPoint) · 📚 被引 0
- **作者**: Yanping Fu, Xinyuan Liu, Tianyu Li, Yike Ma, Yucheng Zhang, Feng Dai
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences, University of Electronic Science and Technology of China, The Institute of Computing Technology of the Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Topology reasoning, which unifies perception and structured reasoning, plays a vital role in understanding intersections for autonomous driving. However, its performance heavily relies on the accuracy of lane detection, particularly at connected lane endpoints. Existing methods often suffer from lane endpoints deviation, leading to incorrect topology construction. To address this issue, we propose TopoPoint, a novel framework that explicitly detects lane endpoints and jointly reasons over endpoints and lanes for robust topology reasoning. During training, we independently initialize point and lane query, and proposed Point-Lane Merge Self-Attention to enhance global context sharing through incorporating geometric distances between points and lanes as an attention mask . We further design Point-Lane Graph Convolutional Network to enable mutual feature aggregation between point and lane query. During inference, we introduce Point-Lane Geometry Matching algorithm that computes distances between detected points and lanes to refine lane endpoints, effectively mitigating endpoint deviation. Extensive experiments on the OpenLane-V2 benchmark demonstrate that TopoPoint achieves state-of-the-art performance in topology reasoning (48.8 on OLS). Additionally, we propose DET$_p$ to evaluate endpoint detection, under which our method significantly outperforms existing approaches (52.6 v.s. 45.2 on DET$_p$). The code is released at https://github.com/Franpin/TopoPoint.

</details>

### Prioritizing Perception-Guided Self-Supervision: A New Paradigm for Causal Modeling in End-to-End Autonomous Driving.
- **链接**: [arXiv:2511.08214](https://arxiv.org/abs/2511.08214) · 📚 被引 0
- **作者**: Yi Huang, Zhan Qu, Lihui Jiang, Bingbing Liu, Hongbo Zhang
- **🏷️ 机构**: The Chinese University of Hong Kong, Huawei Technologies Ltd., Huawei
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving systems, predominantly trained through imitation learning, have demonstrated considerable effectiveness in leveraging large-scale expert driving data. Despite their success in open-loop evaluations, these systems often exhibit significant performance degradation in closed-loop scenarios due to causal confusion. This confusion is fundamentally exacerbated by the overreliance of the imitation learning paradigm on expert trajectories, which often contain unattributable noise and interfere with the modeling of causal relationships between environmental contexts and appropriate driving actions. To address this fundamental limitation, we propose Perception-Guided Self-Supervision (PGS) - a simple yet effective training paradigm that leverages perception outputs as the primary supervisory signals, explicitly modeling causal relationships in decision-making. The proposed framework aligns both the inputs and outputs of the decision-making module with perception results, such as lane centerlines and the predicted motions of surrounding agents, by introducing positive and negative self-supervision for the ego trajectory. This alignment is specifically designed to mitigate causal confusion arising from the inherent noise in expert trajectories. Equipped with perception-driven supervision, our method, built on a standard end-to-end architecture, achieves a Driving Score of 78.08 and a mean success rate of 48.64% on the challenging closed-loop Bench2Drive benchmark, significantly outperforming existing state-of-the-art methods, including those employing more complex network architectures and inference pipelines. These results underscore the effectiveness and robustness of the proposed PGS framework and point to a promising direction for addressing causal confusion and enhancing real-world generalization in autonomous driving.

</details>

### Model-Based Policy Adaptation for Closed-Loop End-to-end Autonomous Driving.
- **链接**: [arXiv:2511.21584](https://arxiv.org/abs/2511.21584) · 📚 被引 0
- **作者**: Haohong Lin, Yunzhi Zhang, Wenhao Ding, Jiajun Wu, Ding Zhao
- **🏷️ 机构**: CMU, Stanford University, Imperial College London
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end (E2E) autonomous driving models have demonstrated strong performance in open-loop evaluations but often suffer from cascading errors and poor generalization in closed-loop settings. To address this gap, we propose Model-based Policy Adaptation (MPA), a general framework that enhances the robustness and safety of pretrained E2E driving agents during deployment. MPA first generates diverse counterfactual trajectories using a geometry-consistent simulation engine, exposing the agent to scenarios beyond the original dataset. Based on this generated data, MPA trains a diffusion-based policy adapter to refine the base policy's predictions and a multi-step Q value model to evaluate long-term outcomes. At inference time, the adapter proposes multiple trajectory candidates, and the Q value model selects the one with the highest expected utility. Experiments on the nuScenes benchmark using a photorealistic closed-loop simulator demonstrate that MPA significantly improves performance across in-domain, out-of-domain, and safety-critical scenarios. We further investigate how the scale of counterfactual data and inference-time guidance strategies affect overall effectiveness.

</details>

### GaussianFusion: Gaussian-Based Multi-Sensor Fusion for End-to-End Autonomous Driving.
- **链接**: [arXiv:2506.00034](https://arxiv.org/abs/2506.00034) · [代码](https://github.com/Say2L/GaussianFusion) · 📚 被引 1
- **作者**: Shuai Liu, Quanmin Liang, Zefeng Li, Boyang Li, Kai Huang
- **🏷️ 机构**: SUN YAT-SEN UNIVERSITY, Sun Yat-sen University, Nanyang Technological University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-sensor fusion is crucial for improving the performance and robustness of end-to-end autonomous driving systems. Existing methods predominantly adopt either attention-based flatten fusion or bird's eye view fusion through geometric transformations. However, these approaches often suffer from limited interpretability or dense computational overhead. In this paper, we introduce GaussianFusion, a Gaussian-based multi-sensor fusion framework for end-to-end autonomous driving. Our method employs intuitive and compact Gaussian representations as intermediate carriers to aggregate information from diverse sensors. Specifically, we initialize a set of 2D Gaussians uniformly across the driving scene, where each Gaussian is parameterized by physical attributes and equipped with explicit and implicit features. These Gaussians are progressively refined by integrating multi-modal features. The explicit features capture rich semantic and spatial information about the traffic scene, while the implicit features provide complementary cues beneficial for trajectory planning. To fully exploit rich spatial and semantic information in Gaussians, we design a cascade planning head that iteratively refines trajectory predictions through interactions with Gaussians. Extensive experiments on the NAVSIM and Bench2Drive benchmarks demonstrate the effectiveness and robustness of the proposed GaussianFusion framework. The source code will be released at https://github.com/Say2L/GaussianFusion.

</details>

### Embodied Cognition Augmented End2End Autonomous Driving.
- **链接**: [arXiv:2511.01334](https://arxiv.org/abs/2511.01334) · 📚 被引 0
- **作者**: Ling Niu, Xiaoji Zheng, Han Wang, Ziyuan Yang, Chen Zheng, Bokui Chen et al.
- **🏷️ 机构**: Tsinghua University, University of Washington, Tsinghua University, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, vision-based end-to-end autonomous driving has emerged as a new paradigm. However, popular end-to-end approaches typically rely on visual feature extraction networks trained under label supervision. This limited supervision framework restricts the generality and applicability of driving models. In this paper, we propose a novel paradigm termed $E^{3}AD$, which advocates for comparative learning between visual feature extraction networks and the general EEG large model, in order to learn latent human driving cognition for enhancing end-to-end planning. In this work, we collected a cognitive dataset for the mentioned contrastive learning process. Subsequently, we investigated the methods and potential mechanisms for enhancing end-to-end planning with human driving cognition, using popular driving models as baselines on publicly available autonomous driving datasets. Both open-loop and closed-loop tests are conducted for a comprehensive evaluation of planning performance. Experimental results demonstrate that the $E^{3}AD$ paradigm significantly enhances the end-to-end planning performance of baseline models. Ablation studies further validate the contribution of driving cognition and the effectiveness of comparative learning process. To the best of our knowledge, this is the first work to integrate human driving cognition for improving end-to-end autonomous driving planning. It represents an initial attempt to incorporate embodied cognitive data into end-to-end autonomous driving, providing valuable insights for future brain-inspired autonomous driving systems. Our code will be made available at Github

</details>

### DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving.
- **链接**: [arXiv:2509.17940](https://arxiv.org/abs/2509.17940) · 📚 被引 0
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
- **链接**: [arXiv:2510.21160](https://arxiv.org/abs/2510.21160) · 📚 被引 0
- **作者**: Guanlin Wu, Boyan Su, Yang Zhao, Pu Wang, Yichen Lin, Hao (Frank) Yang
- **🏷️ 机构**: Johns Hopkins University, University of Minnesota - Twin Cities, Mitsubishi Electric Research Labs
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How to integrate and verify spatial intelligence in foundation models remains an open challenge. Current practice often proxies Visual-Spatial Intelligence (VSI) with purely textual prompts and VQA-style scoring, which obscures geometry, invites linguistic shortcuts, and weakens attribution to genuinely spatial skills. We introduce Spatial Intelligence Grid (SIG): a structured, grid-based schema that explicitly encodes object layouts, inter-object relations, and physically grounded priors. As a complementary channel to text, SIG provides a faithful, compositional representation of scene structure for foundation-model reasoning. Building on SIG, we derive SIG-informed evaluation metrics that quantify a model's intrinsic VSI, which separates spatial capability from language priors. In few-shot in-context learning with state-of-the-art multimodal LLMs (e.g. GPT- and Gemini-family models), SIG yields consistently larger, more stable, and more comprehensive gains across all VSI metrics compared to VQA-only representations, indicating its promise as a data-labeling and training schema for learning VSI. We also release SIGBench, a benchmark of 1.4K driving frames annotated with ground-truth SIG labels and human gaze traces, supporting both grid-based machine VSI tasks and attention-driven, human-like VSI tasks in autonomous-driving scenarios.

</details>

### RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation.
- **链接**: [arXiv:2509.16500](https://arxiv.org/abs/2509.16500) · 📚 被引 0
- **作者**: Tianyi Yan, Wencheng Han, Xia Zhou, Xueyang Zhang, Kun Zhan, Cheng-Zhong Xu et al.
- **🏷️ 机构**: University of Macau, Li Auto Inc., LiAuto
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Synthetic data is crucial for advancing autonomous driving (AD) systems, yet current state-of-the-art video generation models, despite their visual realism, suffer from subtle geometric distortions that limit their utility for downstream perception tasks. We identify and quantify this critical issue, demonstrating a significant performance gap in 3D object detection when using synthetic versus real data. To address this, we introduce Reinforcement Learning with Geometric Feedback (RLGF), RLGF uniquely refines video diffusion models by incorporating rewards from specialized latent-space AD perception models. Its core components include an efficient Latent-Space Windowing Optimization technique for targeted feedback during diffusion, and a Hierarchical Geometric Reward (HGR) system providing multi-level rewards for point-line-plane alignment, and scene occupancy coherence. To quantify these distortions, we propose GeoScores. Applied to models like DiVE on nuScenes, RLGF substantially reduces geometric errors (e.g., VP error by 21\%, Depth error by 57\%) and dramatically improves 3D object detection mAP by 12.7\%, narrowing the gap to real-data performance. RLGF offers a plug-and-play solution for generating geometrically sound and reliable synthetic videos for AD development.

</details>

### ReSim: Reliable World Simulation for Autonomous Driving.
- **链接**: [arXiv:2506.09981](https://arxiv.org/abs/2506.09981) · 📚 被引 0
- **作者**: Jiazhi Yang, Kashyap Chitta, Shenyuan Gao, Long Chen, Yuqian Shao, Xiaosong Jia et al.
- **🏷️ 机构**: NVIDIA, Hong Kong University of Science and Technology, Shanghai Jiaotong University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How can we reliably simulate future driving scenarios under a wide range of ego driving behaviors? Recent driving world models, developed exclusively on real-world driving data composed mainly of safe expert trajectories, struggle to follow hazardous or non-expert behaviors, which are rare in such data. This limitation restricts their applicability to tasks such as policy evaluation. In this work, we address this challenge by enriching real-world human demonstrations with diverse non-expert data collected from a driving simulator (e.g., CARLA), and building a controllable world model trained on this heterogeneous corpus. Starting with a video generator featuring a diffusion transformer architecture, we devise several strategies to effectively integrate conditioning signals and improve prediction controllability and fidelity. The resulting model, ReSim, enables Reliable Simulation of diverse open-world driving scenarios under various actions, including hazardous non-expert ones. To close the gap between high-fidelity simulation and applications that require reward signals to judge different actions, we introduce a Video2Reward module that estimates a reward from ReSim's simulated future. Our ReSim paradigm achieves up to 44% higher visual fidelity, improves controllability for both expert and non-expert actions by over 50%, and boosts planning and policy selection performance on NAVSIM by 2% and 25%, respectively.

</details>

### CodeMerge: Codebook-Guided Model Merging for Robust Test-Time Adaptation in Autonomous Driving.
- **链接**: [arXiv:2505.16524](https://arxiv.org/abs/2505.16524) · 📚 被引 0
- **作者**: Huitong Yang, Zhuoxiao Chen, Fengyi Zhang, Zi Huang, Yadan Luo
- **🏷️ 机构**: The University of Queensland, University of Queensland
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Maintaining robust 3D perception under dynamic and unpredictable test-time conditions remains a critical challenge for autonomous driving systems. Existing test-time adaptation (TTA) methods often fail in high-variance tasks like 3D object detection due to unstable optimization and sharp minima. While recent model merging strategies based on linear mode connectivity (LMC) offer improved stability by interpolating between fine-tuned checkpoints, they are computationally expensive, requiring repeated checkpoint access and multiple forward passes. In this paper, we introduce CodeMerge, a lightweight and scalable model merging framework that bypasses these limitations by operating in a compact latent space. Instead of loading full models, CodeMerge represents each checkpoint with a low-dimensional fingerprint derived from the source model's penultimate features and constructs a key-value codebook. We compute merging coefficients using ridge leverage scores on these fingerprints, enabling efficient model composition without compromising adaptation quality. Our method achieves strong performance across challenging benchmarks, improving end-to-end 3D detection 14.9% NDS on nuScenes-C and LiDAR-based detection by over 7.6% mAP on nuScenes-to-KITTI, while benefiting downstream tasks such as online mapping, motion prediction and planning even without training. Code and pretrained models are released in the supplementary material.

</details>

### Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2).
- **链接**: [arXiv:2505.16394](https://arxiv.org/abs/2505.16394) · 📚 被引 0
- **作者**: Zhenjie Yang, Xiaosong Jia, Qifeng Li, Xue Yang, Maoqing Yao, Junchi Yan
- **🏷️ 机构**: Shanghai Jiao Tong University, University of California, Berkeley, Shanghai Jiaotong University
- **会议**: NeurIPS 2025

### FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving.
- **链接**: [arXiv:2505.17685](https://arxiv.org/abs/2505.17685) · 📚 被引 2
- **作者**: Shuang Zeng, Xinyuan Chang, Mengwei Xie, Xinran Liu, Yifan Bai, Zheng Pan et al.
- **🏷️ 机构**: Xi'an Jiaotong University, Alibaba Group, Tongji University
- **会议**: NeurIPS 2025

### CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action Model.
- **链接**: [arXiv:2511.19914](https://arxiv.org/abs/2511.19914) · 📚 被引 0
- **作者**: Dapeng Zhang, Fei Shen, Rui Zhao, Yinda Chen, Peng Zhi, Chenyang Li et al.
- **🏷️ 机构**: Lanzhou University, Nanjing University of Science and Technology, University of science and technology of China
- **会议**: NeurIPS 2025

### SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving.
- **链接**: [arXiv:2509.16588](https://arxiv.org/abs/2509.16588) · 📚 被引 0
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
- **链接**: [arXiv:2510.23205](https://arxiv.org/abs/2510.23205) · 📚 被引 0
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
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

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

### DiffE2E: Rethinking End-to-End Driving with a Hybrid Diffusion-Regression-Classification Policy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/61162d94822d468ee6e92803340f2040-Abstract-Conference.html) · 📚 被引 0
- **作者**: Rui Zhao, Yuze Fan, Ziguo Chen, Fei Gao, Zhenhai Gao
- **🏷️ 机构**: Lanzhou University, Jilin University
- **会议**: NeurIPS 2025

## 跨领域论文（完整笔记在其他领域）

- OpenAD: Open-World Autonomous Driving Benchmark for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
