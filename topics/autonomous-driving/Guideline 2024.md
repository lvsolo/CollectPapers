# Autonomous Driving — 2024 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Image-to-Lidar Relational Distillation for Autonomous Driving Data.
- **链接**: [arXiv:2409.00845](https://arxiv.org/abs/2409.00845) · 📚 被引 5
- **作者**: Anas Mahmoud, Ali Harakeh, Steven L. Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained on extensive and diverse multi-modal datasets, 2D foundation models excel at addressing 2D tasks with little or no downstream supervision, owing to their robust representations. The emergence of 2D-to-3D distillation frameworks has extended these capabilities to 3D models. However, distilling 3D representations for autonomous driving datasets presents challenges like self-similarity, class imbalance, and point cloud sparsity, hindering the effectiveness of contrastive distillation, especially in zero-shot learning contexts. Whereas other methodologies, such as similarity-based distillation, enhance zero-shot performance, they tend to yield less discriminative representations, diminishing few-shot performance. We investigate the gap in structure between the 2D and the 3D representations that result from state-of-the-art distillation frameworks and reveal a significant mismatch between the two. Additionally, we demonstrate that the observed structural gap is negatively correlated with the efficacy of the distilled representations on zero-shot and few-shot 3D semantic segmentation. To bridge this gap, we propose a relational distillation framework enforcing intra-modal and cross-modal constraints, resulting in distilled 3D representations that closely capture the structure of the 2D representation. This alignment significantly enhances 3D representation performance over those learned through contrastive distillation in zero-shot segmentation tasks. Furthermore, our relational loss consistently improves the quality of 3D representations in both in-distribution and out-of-distribution few-shot segmentation tasks, outperforming approaches that rely on the similarity loss.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a lightweight and scalable Regional Point-Language Contrastive learning framework, namely \textbf{RegionPLC}, for open-world 3D scene understanding, aiming to identify and recognize open-set objects and categories. Specifically, based on our empirical studies, we introduce a 3D-aware SFusion strategy that fuses 3D vision-language pairs derived from multiple 2D foundation models, yielding high-quality, dense region-level language descriptions without human 3D annotations. Subsequently, we devise a region-aware point-discriminative contrastive learning objective to enable robust and effective 3D learning from dense regional language supervision. We carry out extensive experiments on ScanNet, ScanNet200, and nuScenes datasets, and our model outperforms prior 3D open-world scene understanding approaches by an average of 17.2\% and 9.1\% for semantic and instance segmentation, respectively, while maintaining greater scalability and lower resource demands. Furthermore, our method has the flexibility to be effortlessly integrated with language models to enable open-ended grounded 3D reasoning without extra task-specific training. Code is available at https://github.com/CVMI-Lab/PLA.

</details>

### Driving Into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving.
- **链接**: [arXiv:2311.17918](https://arxiv.org/abs/2311.17918) · 📚 被引 116
- **作者**: Yuqi Wang, Jiawei He, Lue Fan, Hongxin Li, Yuntao Chen, Zhaoxiang Zhang
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences (UCAS), Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, MAIS, Centre for Artificial Intelligence and Robotics (HKISI_CAS)
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

</details>

### DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes.
- **链接**: [arXiv:2312.07920](https://arxiv.org/abs/2312.07920) · 📚 被引 280
- **作者**: Xiaoyu Zhou, Zhiwei Lin, Xiaojun Shan, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, Google Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present DrivingGaussian, an efficient and effective framework for surrounding dynamic autonomous driving scenes. For complex scenes with moving objects, we first sequentially and progressively model the static background of the entire scene with incremental static 3D Gaussians. We then leverage a composite dynamic Gaussian graph to handle multiple moving objects, individually reconstructing each object and restoring their accurate positions and occlusion relationships within the scene. We further use a LiDAR prior for Gaussian Splatting to reconstruct scenes with greater details and maintain panoramic consistency. DrivingGaussian outperforms existing methods in dynamic driving scene reconstruction and enables photorealistic surround-view synthesis with high-fidelity and multi-camera consistency. Our project page is at: https://github.com/VDIGPKU/DrivingGaussian.

</details>

### On the Road to Portability: Compressing End-to-End Motion Planner for Autonomous Driving.
- **链接**: [arXiv:2403.01238](https://arxiv.org/abs/2403.01238) · 📚 被引 14
- **作者**: Kaituo Feng, Changsheng Li, Dongchun Ren, Ye Yuan, Guoren Wang
- **🏷️ 机构**: Beijing Institute of Technology, ALLRIDE.AI
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end motion planning models equipped with deep neural networks have shown great potential for enabling full autonomous driving. However, the oversized neural networks render them impractical for deployment on resource-constrained systems, which unavoidably requires more computational time and resources during reference.To handle this, knowledge distillation offers a promising approach that compresses models by enabling a smaller student model to learn from a larger teacher model. Nevertheless, how to apply knowledge distillation to compress motion planners has not been explored so far. In this paper, we propose PlanKD, the first knowledge distillation framework tailored for compressing end-to-end motion planners. First, considering that driving scenes are inherently complex, often containing planning-irrelevant or even noisy information, transferring such information is not beneficial for the student planner. Thus, we design an information bottleneck based strategy to only distill planning-relevant information, rather than transfer all information indiscriminately. Second, different waypoints in an output planned trajectory may hold varying degrees of importance for motion planning, where a slight deviation in certain crucial waypoints might lead to a collision. Therefore, we devise a safety-aware waypoint-attentive distillation module that assigns adaptive weights to different waypoints based on the importance, to encourage the student to accurately mimic more crucial waypoints, thereby improving overall safety. Experiments demonstrate that our PlanKD can boost the performance of smaller planners by a large margin, and significantly reduce their reference time.

</details>

### Bootstrapping Autonomous Driving Radars with Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01422) · 📚 被引 17
- **作者**: Yiduo Hao, Sohrab Madani, Junfeng Guan, Mohammed Alloulah, Saurabh Gupta, Haitham Hassanieh
- **🏷️ 机构**: University of Cambridge, UIUC, EPFL
- **会议**: CVPR 2024

### Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving.
- **链接**: [arXiv:2404.04804](https://arxiv.org/abs/2404.04804) · 📚 被引 74
- **作者**: Jinlong Li, Baolu Li, Zhengzhong Tu, Xinyu Liu, Qing Guo, Felix Juefei-Xu et al.
- **🏷️ 机构**: Cleveland State University, University of Texas at Austin, Centre for Frontier AI Research (CFAR), A&#x002A;STAR
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-centric perception systems for autonomous driving have gained considerable attention recently due to their cost-effectiveness and scalability, especially compared to LiDAR-based systems. However, these systems often struggle in low-light conditions, potentially compromising their performance and safety. To address this, our paper introduces LightDiff, a domain-tailored framework designed to enhance the low-light image quality for autonomous driving applications. Specifically, we employ a multi-condition controlled diffusion model. LightDiff works without any human-collected paired data, leveraging a dynamic data degradation process instead. It incorporates a novel multi-condition adapter that adaptively controls the input weights from different modalities, including depth maps, RGB images, and text captions, to effectively illuminate dark scenes while maintaining context consistency. Furthermore, to align the enhanced images with the detection model's knowledge, LightDiff employs perception-specific scores as rewards to guide the diffusion training process through reinforcement learning. Extensive experiments on the nuScenes datasets demonstrate that LightDiff can significantly improve the performance of several state-of-the-art 3D detectors in night-time conditions while achieving high visual quality scores, highlighting its potential to safeguard autonomous driving.

</details>

### Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving?
- **链接**: [arXiv:2312.03031](https://arxiv.org/abs/2312.03031) · 📚 被引 86
- **作者**: Zhiqi Li, Zhiding Yu, Shiyi Lan, Jiahan Li, Jan Kautz, Tong Lu et al.
- **🏷️ 机构**: Nanjing University,National Key Lab for Novel Software Technology, NVIDIA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving recently emerged as a promising research direction to target autonomy from a full-stack perspective. Along this line, many of the latest works follow an open-loop evaluation setting on nuScenes to study the planning behavior. In this paper, we delve deeper into the problem by conducting thorough analyses and demystifying more devils in the details. We initially observed that the nuScenes dataset, characterized by relatively simple driving scenarios, leads to an under-utilization of perception information in end-to-end models incorporating ego status, such as the ego vehicle's velocity. These models tend to rely predominantly on the ego vehicle's status for future path planning. Beyond the limitations of the dataset, we also note that current metrics do not comprehensively assess the planning quality, leading to potentially biased conclusions drawn from existing benchmarks. To address this issue, we introduce a new metric to evaluate whether the predicted trajectories adhere to the road. We further propose a simple baseline able to achieve competitive results without relying on perception annotations. Given the current limitations on the benchmark and metrics, we suggest the community reassess relevant prevailing research and be cautious whether the continued pursuit of state-of-the-art would yield convincing and universal conclusions. Code and models are available at \url{https://github.com/NVlabs/BEV-Planner}

</details>

### VLP: Vision Language Planning for Autonomous Driving.
- **链接**: [arXiv:2401.05577](https://arxiv.org/abs/2401.05577) · 📚 被引 85
- **作者**: Chenbin Pan, Burhaneddin Yaman, Tommaso Nesti, Abhirup Mallik, Alessandro Gabriele Allievi, Senem Velipasalar et al.
- **🏷️ 机构**: Syracuse University, Bosch Research North America &#x0026; Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving is a complex and challenging task that aims at safe motion planning through scene understanding and reasoning. While vision-only autonomous driving methods have recently achieved notable performance, through enhanced scene understanding, several key issues, including lack of reasoning, low generalization performance and long-tail scenarios, still need to be addressed. In this paper, we present VLP, a novel Vision-Language-Planning framework that exploits language models to bridge the gap between linguistic understanding and autonomous driving. VLP enhances autonomous driving systems by strengthening both the source memory foundation and the self-driving car's contextual understanding. VLP achieves state-of-the-art end-to-end planning performance on the challenging NuScenes dataset by achieving 35.9\% and 60.5\% reduction in terms of average L2 error and collision rates, respectively, compared to the previous best method. Moreover, VLP shows improved performance in challenging long-tail scenarios and strong generalization capabilities when faced with new urban environments.

</details>

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00659)
- **作者**: Yuqing Wen, Yucheng Zhao, Yingfei Liu, Fan Jia, Yanhui Wang, Chong Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SeFlow: A Self-supervised Scene Flow Method in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73232-4_20) · 📚 被引 21
- **作者**: Qingwen Zhang, Yi Yang, Peizheng Li, Olov Andersson, Patric Jensfelt
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting a potential collision with leading vehicles is an essential functionality of any autonomous/assisted driving system. One bottleneck of existing vision-based solutions is that their updating rate is limited to the frame rate of standard cameras used. In this paper, we present a novel method that estimates the time to collision using a neuromorphic event-based camera, a biologically inspired visual sensor that can sense at exactly the same rate as scene dynamics. The core of the proposed algorithm consists of a two-step approach for efficient and accurate geometric model fitting on event data in a coarse-to-fine manner. The first step is a robust linear solver based on a novel geometric measurement that overcomes the partial observability of event-based normal flow. The second step further refines the resulting model via a spatio-temporal registration process formulated as a nonlinear optimization problem. Experiments on both synthetic and real data demonstrate the effectiveness of the proposed method, outperforming other alternative methods in terms of efficiency and accuracy.

</details>

### Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving.
- **链接**: [arXiv:2406.03877](https://arxiv.org/abs/2406.03877) · 📚 被引 75
- **作者**: Xiaosong Jia, Zhenjie Yang, Qifeng Li, Zhiyuan Zhang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene flow estimation predicts the 3D motion at each point in successive LiDAR scans. This detailed, point-level, information can help autonomous vehicles to accurately predict and understand dynamic changes in their surroundings. Current state-of-the-art methods require annotated data to train scene flow networks and the expense of labeling inherently limits their scalability. Self-supervised approaches can overcome the above limitations, yet face two principal challenges that hinder optimal performance: point distribution imbalance and disregard for object-level motion constraints. In this paper, we propose SeFlow, a self-supervised method that integrates efficient dynamic classification into a learning-based scene flow pipeline. We demonstrate that classifying static and dynamic points helps design targeted objective functions for different motion patterns. We also emphasize the importance of internal cluster consistency and correct object point association to refine the scene flow estimation, in particular on object details. Our real-time capable method achieves state-of-the-art performance on the self-supervised scene flow task on Argoverse 2 and Waymo datasets. The code is open-sourced at https://github.com/KTH-RPL/SeFlow along with trained model weights.

</details>

</details>

### Reasoning Multi-Agent Behavioral Topology for Interactive Autonomous Driving.
- **链接**: [arXiv:2409.18031](https://arxiv.org/abs/2409.18031) · 📚 被引 11
- **作者**: Haochen Liu, Li Chen, Yu Qiao, Chen Lv, Hongyang Li
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Directly producing planning results from raw sensors has been a long-desired solution for autonomous driving and has attracted increasing attention recently. Most existing end-to-end autonomous driving methods factorize this problem into perception, motion prediction, and planning. However, we argue that the conventional progressive pipeline still cannot comprehensively model the entire traffic evolution process, e.g., the future interaction between the ego car and other traffic participants and the structural trajectory prior. In this paper, we explore a new paradigm for end-to-end autonomous driving, where the key is to predict how the ego car and the surroundings evolve given past scenes. We propose GenAD, a generative framework that casts autonomous driving into a generative modeling problem. We propose an instance-centric scene tokenizer that first transforms the surrounding scenes into map-aware instance tokens. We then employ a variational autoencoder to learn the future trajectory distribution in a structural latent space for trajectory prior modeling. We further adopt a temporal model to capture the agent and ego movements in the latent space to generate more effective future trajectories. GenAD finally simultaneously performs motion prediction and planning by sampling distributions in the learned structural latent space conditioned on the instance tokens and using the learned temporal model to generate futures. Extensive experiments on the widely used nuScenes benchmark show that the proposed GenAD achieves state-of-the-art performance on vision-centric end-to-end autonomous driving with high efficiency. Code: https://github.com/wzzheng/GenAD.

</details>

### Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving.
- **链接**: [arXiv:2405.15324](https://arxiv.org/abs/2405.15324) · 📚 被引 11
- **作者**: Jianbiao Mei, Yukai Ma, Xuemeng Yang, Licheng Wen, Xinyu Cai, Xin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving has advanced significantly due to sensors, machine learning, and artificial intelligence improvements. However, prevailing methods struggle with intricate scenarios and causal relationships, hindering adaptability and interpretability in varied environments. To address the above problems, we introduce LeapAD, a novel paradigm for autonomous driving inspired by the human cognitive process. Specifically, LeapAD emulates human attention by selecting critical objects relevant to driving decisions, simplifying environmental interpretation, and mitigating decision-making complexities. Additionally, LeapAD incorporates an innovative dual-process decision-making module, which consists of an Analytic Process (System-II) for thorough analysis and reasoning, along with a Heuristic Process (System-I) for swift and empirical processing. The Analytic Process leverages its logical reasoning to accumulate linguistic driving experience, which is then transferred to the Heuristic Process by supervised fine-tuning. Through reflection mechanisms and a growing memory bank, LeapAD continuously improves itself from past mistakes in a closed-loop environment. Closed-loop testing in CARLA shows that LeapAD outperforms all methods relying solely on camera input, requiring 1-2 orders of magnitude less labeled data. Experiments also demonstrate that as the memory bank expands, the Heuristic Process with only 1.8B parameters can inherit the knowledge from a GPT-4 powered Analytic Process and achieve continuous performance improvement. Project page: https://pjlab-adg.github.io/LeapAD.

</details>

### BehaviorGPT: Smart Agent Simulation for Autonomous Driving with Next-Patch Prediction.
- **链接**: [arXiv:2405.17372](https://arxiv.org/abs/2405.17372) · 📚 被引 8
- **作者**: Zikang Zhou, Haibo Hu, Xinhong Chen, Jianping Wang, Nan Guan, Kui Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Simulating realistic behaviors of traffic agents is pivotal for efficiently validating the safety of autonomous driving systems. Existing data-driven simulators primarily use an encoder-decoder architecture to encode the historical trajectories before decoding the future. However, the heterogeneity between encoders and decoders complicates the models, and the manual separation of historical and future trajectories leads to low data utilization. Given these limitations, we propose BehaviorGPT, a homogeneous and fully autoregressive Transformer designed to simulate the sequential behavior of multiple agents. Crucially, our approach discards the traditional separation between "history" and "future" by modeling each time step as the "current" one for motion generation, leading to a simpler, more parameter- and data-efficient agent simulator. We further introduce the Next-Patch Prediction Paradigm (NP3) to mitigate the negative effects of autoregressive modeling, in which models are trained to reason at the patch level of trajectories and capture long-range spatial-temporal interactions. Despite having merely 3M model parameters, BehaviorGPT won first place in the 2024 Waymo Open Sim Agents Challenge with a realism score of 0.7473 and a minADE score of 1.4147, demonstrating its exceptional performance in traffic agent simulation.

</details>

### Expert-level protocol translation for self-driving labs.
- **链接**: [arXiv:2411.00444](https://arxiv.org/abs/2411.00444) · 📚 被引 1
- **作者**: Yu-Zhe Shi, Fanxu Meng, Haofei Hou, Zhangqian Bi, Qiao Xu, Lecheng Ruan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent development in Artificial Intelligence (AI) models has propelled their application in scientific discovery, but the validation and exploration of these discoveries require subsequent empirical experimentation. The concept of self-driving laboratories promises to automate and thus boost the experimental process following AI-driven discoveries. However, the transition of experimental protocols, originally crafted for human comprehension, into formats interpretable by machines presents significant challenges, which, within the context of specific expert domain, encompass the necessity for structured as opposed to natural language, the imperative for explicit rather than tacit knowledge, and the preservation of causality and consistency throughout protocol steps. Presently, the task of protocol translation predominantly requires the manual and labor-intensive involvement of domain experts and information technology specialists, rendering the process time-intensive. To address these issues, we propose a framework that automates the protocol translation process through a three-stage workflow, which incrementally constructs Protocol Dependence Graphs (PDGs) that approach structured on the syntax level, completed on the semantics level, and linked on the execution level. Quantitative and qualitative evaluations have demonstrated its performance at par with that of human experts, underscoring its potential to significantly expedite and democratize the process of scientific discovery by elevating the automation capabilities within self-driving laboratories.

</details>

## 🆕 增量新增

### LaMPilot: An Open Benchmark Dataset for Autonomous Driving with Language Model Programs. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2312.04372](https://arxiv.org/abs/2312.04372) · 📚 被引 53
- **作者**: Yunsheng Ma, Can Cui, Xu Cao, Wenqian Ye, Peiran Liu, Juanwu Lu et al.
- **🏷️ 机构**: Purdue University, University of Illinois Urbana-Champaign, University of Virginia
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有自动驾驶框架难以理解和执行自发用户指令（如“超车”）的问题，提出了LaMPilot框架，将大语言模型（LLM）集成到自动驾驶系统中，通过生成代码调用功能原语来遵循用户指令。同时引入了LaMPilot-Bench，首个专门用于定量评估语言模型程序在自动驾驶中效能的基准数据集。实验表明，现成LLM在处理多样驾驶场景和遵循用户指令方面具有潜力。
- **摘要（英）**: To address the challenge of interpreting and executing spontaneous user instructions in autonomous driving, this paper proposes LaMPilot, a framework integrating LLMs into AD systems to generate code that leverages functional primitives. It also introduces LaMPilot-Bench, the first benchmark for quantitatively evaluating language model programs in AD. Experiments demonstrate the potential of off-the-shelf LLMs in handling diverse driving scenarios and following user instructions.
- **核心贡献**: 提出了LaMPilot框架和LaMPilot-Bench基准，实现LLM驱动的自动驾驶指令执行。
- **创新点**: 利用LLM生成代码来桥接用户指令与驾驶功能。
- **结果**: 实验验证了LLM在驾驶场景中的潜力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving (AD) has made significant strides in recent years. However, existing frameworks struggle to interpret and execute spontaneous user instructions, such as "overtake the car ahead." Large Language Models (LLMs) have demonstrated impressive reasoning capabilities showing potential to bridge this gap. In this paper, we present LaMPilot, a novel framework that integrates LLMs into AD systems, enabling them to follow user instructions by generating code that leverages established functional primitives. We also introduce LaMPilot-Bench, the first benchmark dataset specifically designed to quantitatively evaluate the efficacy of language model programs in AD. Adopting the LaMPilot framework, we conduct extensive experiments to assess the performance of off-the-shelf LLMs on LaMPilot-Bench. Our results demonstrate the potential of LLMs in handling diverse driving scenarios and following user instructions in driving. To facilitate further research in this area, we release our code and data at https://github.com/PurdueDigitalTwin/LaMPilot.

</details>

### AIDE: An Automatic Data Engine for Object Detection in Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2403.17373](https://arxiv.org/abs/2403.17373) · 📚 被引 33
- **作者**: Mingfu Liang, Jong-Chyi Su, Samuel Schulter, Sparsh Garg, Shiyu Zhao, Ying Wu et al.
- **🏷️ 机构**: Northwestern University, NEC Laboratories America, Rutgers University
- **会议**: CVPR 2024
- **摘要（中）**: 针对自动驾驶中长尾分布和罕见类别导致的感知模型性能下降问题，提出AIDE自动数据引擎，利用视觉-语言模型和大语言模型自动识别问题、高效筛选数据、自动标注并生成多样化场景验证模型，实现迭代式自我改进。相比传统人工数据标注流程，该方法显著降低了成本并提升了开放世界检测性能。在自动驾驶数据集上的基准测试表明，AIDE在减少成本的同时取得了更优的检测效果。
- **摘要（英）**: To address the long-tailed distribution and rare categories in autonomous driving perception, AIDE leverages vision-language and large language models to automatically identify issues, curate data, auto-label, and verify via scenario generation, enabling iterative self-improvement. It reduces human annotation cost while achieving superior open-world detection performance on AV benchmarks.
- **核心贡献**: 提出首个基于大模型的自动数据引擎，实现开放世界检测的闭环自改进。
- **创新点**: 利用VLM和LLM实现数据筛选、标注和验证的全自动化流程。
- **结果**: 在自动驾驶数据集上以更低成本取得更优的开放世界检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous vehicle (AV) systems rely on robust perception models as a cornerstone of safety assurance. However, objects encountered on the road exhibit a long-tailed distribution, with rare or unseen categories posing challenges to a deployed perception model. This necessitates an expensive process of continuously curating and annotating data with significant human effort. We propose to leverage recent advances in vision-language and large language models to design an Automatic Data Engine (AIDE) that automatically identifies issues, efficiently curates data, improves the model through auto-labeling, and verifies the model through generation of diverse scenarios. This process operates iteratively, allowing for continuous self-improvement of the model. We further establish a benchmark for open-world detection on AV datasets to comprehensively evaluate various learning paradigms, demonstrating our method's superior performance at a reduced cost.

</details>

### Visual Point Cloud Forecasting Enables Scalable Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2312.17655](https://arxiv.org/abs/2312.17655) · 📚 被引 58
- **作者**: Zetong Yang, Li Chen, Yanan Sun, Hongyang Li
- **🏷️ 机构**: OpenDriveLab and Shanghai AI Lab
- **会议**: CVPR 2024
- **摘要（中）**: 针对视觉自动驾驶预训练缺乏同时涵盖语义、3D几何和时间信息的方法，提出视觉点云预测作为新预训练任务，并设计ViDAR模型。通过潜在渲染算子将历史嵌入转换到3D几何空间预测未来点云，实现语义、结构和时间动态的协同学习。在3D检测、运动预测和规划等下游任务上取得显著提升，如NDS提升3.1%、碰撞率降低约15%。
- **摘要（英）**: To address the lack of pre-training methods that simultaneously capture semantics, 3D geometry, and temporal dynamics for visual autonomous driving, this paper proposes visual point cloud forecasting as a new pre-training task and presents ViDAR. It uses a Latent Rendering operator to transform historical embeddings into 3D space for future point cloud prediction. Experiments show significant gains in downstream tasks, including 3.1% NDS improvement in 3D detection and ~15% collision rate reduction.
- **核心贡献**: 提出视觉点云预测预训练任务和ViDAR模型，实现语义、几何与时间协同学习。
- **创新点**: 设计潜在渲染算子，将视觉特征转换至3D空间进行未来预测。
- **结果**: 在多个下游任务上显著提升性能，验证了预训练的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrast to extensive studies on general vision, pre-training for scalable visual autonomous driving remains seldom explored. Visual autonomous driving applications require features encompassing semantics, 3D geometry, and temporal information simultaneously for joint perception, prediction, and planning, posing dramatic challenges for pre-training. To resolve this, we bring up a new pre-training task termed as visual point cloud forecasting - predicting future point clouds from historical visual input. The key merit of this task captures the synergic learning of semantics, 3D structures, and temporal dynamics. Hence it shows superiority in various downstream tasks. To cope with this new problem, we present ViDAR, a general model to pre-train downstream visual encoders. It first extracts historical embeddings by the encoder. These representations are then transformed to 3D geometric space via a novel Latent Rendering operator for future point cloud prediction. Experiments show significant gain in downstream tasks, e.g., 3.1% NDS on 3D detection, ~10% error reduction on motion forecasting, and ~15% less collision rate on planning.

</details>

### Holistic Autonomous Driving Understanding by Bird'View Injected Multi-Modal Large Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01297) · 📚 被引 41
- **作者**: Xinpeng Ding, Jianhua Han, Hang Xu, Xiaodan Liang, Wei Zhang, Xiaomeng Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab, Sun Yat-Sen University
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
- **链接**: [arXiv:2310.08370](https://arxiv.org/abs/2310.08370) · 📚 被引 42
- **作者**: Honghui Yang, Sha Zhang, Di Huang, Xiaoyang Wu, Haoyi Zhu, Tong He et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, Shanghai Artificial Intelligence Laboratory, HongKong University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the context of autonomous driving, the significance of effective feature learning is widely acknowledged. While conventional 3D self-supervised pre-training methods have shown widespread success, most methods follow the ideas originally designed for 2D images. In this paper, we present UniPAD, a novel self-supervised learning paradigm applying 3D volumetric differentiable rendering. UniPAD implicitly encodes 3D space, facilitating the reconstruction of continuous 3D shape structures and the intricate appearance characteristics of their 2D projections. The flexibility of our method enables seamless integration into both 2D and 3D frameworks, enabling a more holistic comprehension of the scenes. We manifest the feasibility and effectiveness of UniPAD by conducting extensive experiments on various downstream 3D tasks. Our method significantly improves lidar-, camera-, and lidar-camera-based baseline by 9.1, 7.7, and 6.9 NDS, respectively. Notably, our pre-training pipeline achieves 73.2 NDS for 3D object detection and 79.4 mIoU for 3D semantic segmentation on the nuScenes validation set, achieving state-of-the-art results in comparison with previous methods. The code will be available at https://github.com/Nightmare-n/UniPAD.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the challenge of content diversity and controllability in pedestrian simulation for driving scenarios. Recent pedestrian animation frameworks have a significant limitation wherein they primarily focus on either following trajectory [46] or the content of the reference video [57], consequently overlooking the potential diversity of human motion within such scenarios. This limitation restricts the ability to generate pedestrian behaviors that exhibit a wider range of variations and realistic motions and therefore restricts its usage to provide rich motion content for other components in the driving simulation system, e.g., suddenly changed motion to which the autonomous vehicle should respond. In our approach, we strive to surpass the limitation by showcasing diverse human motions obtained from various sources, such as generated human motions, in addition to following the given trajectory. The fundamental contribution of our framework lies in combining the motion tracking task with trajectory following, which enables the tracking of specific motion parts (e.g., upper body) while simultaneously following the given trajectory by a single policy. This way, we significantly enhance both the diversity of simulated human motion within the given scenario and the controllability of the content, including language-based control. Our framework facilitates the generation of a wide range of human motions, contributing to greater realism and adaptability in pedestrian simulations for driving scenarios. More information is on our project page https://wangjingbo1219.github.io/papers/CVPR2024_PACER_PLUS/PACERPLUSPage.html .

</details>

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

### TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving: Supplementary Materials.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73036-8_6) · 📚 被引 9
- **作者**: Cheng Zhao, Su Sun, Ruoyu Wang, Yuliang Guo, Jun-Jun Wan, Zhou Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Dolphins: Multimodal Language Model for Driving.
- **链接**: [arXiv:2312.00438](https://arxiv.org/abs/2312.00438) · 📚 被引 46
- **作者**: Yingzi Ma, Yulong Cao, Jiachen Sun, Marco Pavone, Chaowei Xiao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The quest for fully autonomous vehicles (AVs) capable of navigating complex real-world scenarios with human-like understanding and responsiveness. In this paper, we introduce Dolphins, a novel vision-language model architected to imbibe human-like abilities as a conversational driving assistant. Dolphins is adept at processing multimodal inputs comprising video (or image) data, text instructions, and historical control signals to generate informed outputs corresponding to the provided instructions. Building upon the open-sourced pretrained Vision-Language Model, OpenFlamingo, we first enhance Dolphins's reasoning capabilities through an innovative Grounded Chain of Thought (GCoT) process. Then we tailored Dolphins to the driving domain by constructing driving-specific instruction data and conducting instruction tuning. Through the utilization of the BDD-X dataset, we designed and consolidated four distinct AV tasks into Dolphins to foster a holistic understanding of intricate driving scenarios. As a result, the distinctive features of Dolphins are characterized into two dimensions: (1) the ability to provide a comprehensive understanding of complex and long-tailed open-world driving scenarios and solve a spectrum of AV tasks, and (2) the emergence of human-like capabilities including gradient-free instant adaptation via in-context learning and error recovery via reflection.

</details>

### ReSimAD: Zero-Shot 3D Domain Transfer for Autonomous Driving with Source Reconstruction and Target Simulation.
- **链接**: [arXiv:2309.05527](https://arxiv.org/abs/2309.05527)
- **作者**: Bo Zhang, Xinyu Cai, Jiakang Yuan, Donglin Yang, Jianfei Guo, Xiangchao Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain shifts such as sensor type changes and geographical situation variations are prevalent in Autonomous Driving (AD), which poses a challenge since AD model relying on the previous domain knowledge can be hardly directly deployed to a new domain without additional costs. In this paper, we provide a new perspective and approach of alleviating the domain shifts, by proposing a Reconstruction-Simulation-Perception (ReSimAD) scheme. Specifically, the implicit reconstruction process is based on the knowledge from the previous old domain, aiming to convert the domain-related knowledge into domain-invariant representations, e.g., 3D scene-level meshes. Besides, the point clouds simulation process of multiple new domains is conditioned on the above reconstructed 3D meshes, where the target-domain-like simulation samples can be obtained, thus reducing the cost of collecting and annotating new-domain data for the subsequent perception process. For experiments, we consider different cross-domain situations such as Waymo-to-KITTI, Waymo-to-nuScenes, Waymo-to-ONCE, etc, to verify the zero-shot target-domain perception using ReSimAD. Results demonstrate that our method is beneficial to boost the domain generalization ability, even promising for 3D pre-training.

</details>

### LaneSegNet: Map Learning with Lane Segment Perception for Autonomous Driving.
- **链接**: [arXiv:2312.16108](https://arxiv.org/abs/2312.16108)
- **作者**: Tianyu Li, Peijin Jia, Bangjun Wang, Li Chen, Kun Jiang, Junchi Yan et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A map, as crucial information for downstream applications of an autonomous driving system, is usually represented in lanelines or centerlines. However, existing literature on map learning primarily focuses on either detecting geometry-based lanelines or perceiving topology relationships of centerlines. Both of these methods ignore the intrinsic relationship of lanelines and centerlines, that lanelines bind centerlines. While simply predicting both types of lane in one model is mutually excluded in learning objective, we advocate lane segment as a new representation that seamlessly incorporates both geometry and topology information. Thus, we introduce LaneSegNet, the first end-to-end mapping network generating lane segments to obtain a complete representation of the road structure. Our algorithm features two key modifications. One is a lane attention module to capture pivotal region details within the long-range feature space. Another is an identical initialization strategy for reference points, which enhances the learning of positional priors for lane attention. On the OpenLane-V2 dataset, LaneSegNet outperforms previous counterparts by a substantial gain across three tasks, \textit{i.e.}, map element detection (+4.8 mAP), centerline perception (+6.9 DET$_l$), and the newly defined one, lane segment perception (+5.6 mAP). Furthermore, it obtains a real-time inference speed of 14.7 FPS. Code is accessible at https://github.com/OpenDriveLab/LaneSegNet.

</details>

### DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models.
- **链接**: [arXiv:2309.16292](https://arxiv.org/abs/2309.16292)
- **作者**: Licheng Wen, Daocheng Fu, Xin Li, Xinyu Cai, Tao Ma, Pinlong Cai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in autonomous driving have relied on data-driven approaches, which are widely adopted but face challenges including dataset bias, overfitting, and uninterpretability. Drawing inspiration from the knowledge-driven nature of human driving, we explore the question of how to instill similar capabilities into autonomous driving systems and summarize a paradigm that integrates an interactive environment, a driver agent, as well as a memory component to address this question. Leveraging large language models (LLMs) with emergent abilities, we propose the DiLu framework, which combines a Reasoning and a Reflection module to enable the system to perform decision-making based on common-sense knowledge and evolve continuously. Extensive experiments prove DiLu's capability to accumulate experience and demonstrate a significant advantage in generalization ability over reinforcement learning-based methods. Moreover, DiLu is able to directly acquire experiences from real-world datasets which highlights its potential to be deployed on practical autonomous driving systems. To the best of our knowledge, we are the first to leverage knowledge-driven capability in decision-making for autonomous vehicles. Through the proposed DiLu framework, LLM is strengthened to apply knowledge and to reason causally in the autonomous driving domain. Project page: https://pjlab-adg.github.io/DiLu/

</details>

### Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion.
- **链接**: [出版页](https://openreview.net/forum?id=Psl75UCoZM)
- **作者**: Lunjun Zhang, Yuwen Xiong, Ze Yang, Sergio Casas, Rui Hu, Raquel Urtasun
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: ICLR 2024

### Revisiting Few-Shot Object Detection with Vision-Language Models.
- **链接**: [arXiv:2312.14494](https://arxiv.org/abs/2312.14494) · 📚 被引 13
- **作者**: Anish Madan, Neehar Peri, Shu Kong, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The era of vision-language models (VLMs) trained on web-scale datasets challenges conventional formulations of "open-world" perception. In this work, we revisit the task of few-shot object detection (FSOD) in the context of recent foundational VLMs. First, we point out that zero-shot predictions from VLMs such as GroundingDINO significantly outperform state-of-the-art few-shot detectors (48 vs. 33 AP) on COCO. Despite their strong zero-shot performance, such foundation models may still be sub-optimal. For example, trucks on the web may be defined differently from trucks for a target application such as autonomous vehicle perception. We argue that the task of few-shot recognition can be reformulated as aligning foundation models to target concepts using a few examples. Interestingly, such examples can be multi-modal, using both text and visual cues, mimicking instructions that are often given to human annotators when defining a target concept of interest. Concretely, we propose Foundational FSOD, a new benchmark protocol that evaluates detectors pre-trained on any external data and fine-tuned on multi-modal (text and visual) K-shot examples per target class. We repurpose nuImages for Foundational FSOD, benchmark several popular open-source VLMs, and provide an empirical analysis of state-of-the-art methods. Lastly, we discuss our recent CVPR 2024 Foundational FSOD competition and share insights from the community. Notably, the winning team significantly outperforms our baseline by 23.3 mAP! Our code and dataset splits are available at https://github.com/anishmadan23/foundational_fsod

</details>

### ZOPP: A Framework of Zero-shot Offboard Panoptic Perception for Autonomous Driving.
- **链接**: [arXiv:2411.05311](https://arxiv.org/abs/2411.05311)
- **作者**: Tao Ma, Hongbin Zhou, Qiusheng Huang, Xuemeng Yang, Jianfei Guo, Bo Zhang et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Offboard perception aims to automatically generate high-quality 3D labels for autonomous driving (AD) scenes. Existing offboard methods focus on 3D object detection with closed-set taxonomy and fail to match human-level recognition capability on the rapidly evolving perception tasks. Due to heavy reliance on human labels and the prevalence of data imbalance and sparsity, a unified framework for offboard auto-labeling various elements in AD scenes that meets the distinct needs of perception tasks is not being fully explored. In this paper, we propose a novel multi-modal Zero-shot Offboard Panoptic Perception (ZOPP) framework for autonomous driving scenes. ZOPP integrates the powerful zero-shot recognition capabilities of vision foundation models and 3D representations derived from point clouds. To the best of our knowledge, ZOPP represents a pioneering effort in the domain of multi-modal panoptic perception and auto labeling for autonomous driving scenes. We conduct comprehensive empirical studies and evaluations on Waymo open dataset to validate the proposed ZOPP on various perception tasks. To further explore the usability and extensibility of our proposed ZOPP, we also conduct experiments in downstream applications. The results further demonstrate the great potential of our ZOPP for real-world scenarios.

</details>

### Autonomous Driving with Spiking Neural Networks.
- **链接**: [arXiv:2405.19687](https://arxiv.org/abs/2405.19687) · 📚 被引 5
- **作者**: Ruijie Zhu, Ziqing Wang, Leilani Gilpin, Jason Eshraghian
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving demands an integrated approach that encompasses perception, prediction, and planning, all while operating under strict energy constraints to enhance scalability and environmental sustainability. We present Spiking Autonomous Driving (SAD), the first unified Spiking Neural Network (SNN) to address the energy challenges faced by autonomous driving systems through its event-driven and energy-efficient nature. SAD is trained end-to-end and consists of three main modules: perception, which processes inputs from multi-view cameras to construct a spatiotemporal bird's eye view; prediction, which utilizes a novel dual-pathway with spiking neurons to forecast future states; and planning, which generates safe trajectories considering predicted occupancy, traffic rules, and ride comfort. Evaluated on the nuScenes dataset, SAD achieves competitive performance in perception, prediction, and planning tasks, while drawing upon the energy efficiency of SNNs. This work highlights the potential of neuromorphic computing to be applied to energy-efficient autonomous driving, a critical step toward sustainable and safety-critical automotive technology. Our code is available at \url{https://github.com/ridgerchu/SAD}.

</details>
<!-- COMPLETE v1 papers=40 -->
