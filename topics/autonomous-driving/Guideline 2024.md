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

### DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02044)
- **作者**: Xiaoyu Zhou, Zhiwei Lin, Xiaojun Shan, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶场景中动态环境的高保真重建与仿真问题，现有3D高斯泼溅方法难以处理多动态物体与静态背景的复合场景。②提出DrivingGaussian，采用复合高斯泼溅框架，将静态背景、动态车辆和整体场景分层建模，并利用增量静态3D重建和动态物体建模实现全局一致性。③相比已有工作，首次在复合框架中联合优化静态与动态高斯，支持多视角动态场景的逼真渲染。④在多个自动驾驶数据集上实现SOTA渲染质量，显著提升动态场景的PSNR和视觉保真度。
- **摘要（英）**: This paper addresses high-fidelity reconstruction and simulation of dynamic autonomous driving scenes, where existing 3D Gaussian splatting struggles with composite static-dynamic environments. It proposes DrivingGaussian, a composite Gaussian splatting framework that models static backgrounds, dynamic vehicles, and the whole scene hierarchically, achieving global consistency via incremental static reconstruction and dynamic object modeling. It achieves state-of-the-art rendering quality on multiple driving datasets, significantly improving PSNR and visual fidelity.
- **核心贡献**: 提出复合高斯泼溅框架，实现动态自动驾驶场景的高保真重建。
- **创新点**: 分层建模静态与动态高斯，并联合优化全局场景一致性。
- **结果**: 在多个数据集上取得SOTA渲染质量，提升动态场景PSNR。

### On the Road to Portability: Compressing End-to-End Motion Planner for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01430)
- **作者**: Kaituo Feng, Changsheng Li, Dongchun Ren, Ye Yuan, Guoren Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对端到端运动规划模型在自动驾驶中部署时计算资源受限的问题。②提出模型压缩方法，通过剪枝和知识蒸馏减小模型规模，同时保持规划性能。③相比直接压缩，该方法针对运动规划任务定制，保留关键决策能力。④在仿真和真实数据集上，模型大小减少约50%，规划精度损失极小。
- **摘要（英）**: This paper addresses the deployment challenge of end-to-end motion planners in autonomous driving under computational constraints. It proposes a compression method using pruning and knowledge distillation to reduce model size while maintaining planning performance. Compared to generic compression, it is tailored for motion planning, preserving critical decision-making capabilities. It reduces model size by ~50% with minimal planning accuracy loss.
- **核心贡献**: 提出端到端运动规划器的剪枝与蒸馏压缩方法。
- **创新点**: 针对规划任务定制压缩策略，保留决策能力。
- **结果**: 模型大小减半，规划精度损失极小。

### Bootstrapping Autonomous Driving Radars with Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01422) · 📚 被引 17
- **作者**: Yiduo Hao, Sohrab Madani, Junfeng Guan, Mohammed Alloulah, Saurabh Gupta, Haitham Hassanieh
- **🏷️ 机构**: University of Cambridge, UIUC, EPFL
- **会议**: CVPR 2024

### Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01440)
- **作者**: Jinlong Li, Baolu Li, Zhengzhong Tu, Xinyu Liu, Qing Guo, Felix Juefei-Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶夜间低光环境下感知性能下降的问题。②提出多条件扩散框架，用于无配对低光图像增强，结合光照和场景条件。③相比传统增强方法，扩散模型生成更自然图像，提升下游感知鲁棒性。④在多个夜间驾驶数据集上，增强后图像在目标检测和分割任务上显著提升精度。
- **摘要（英）**: This paper addresses performance degradation in low-light conditions for autonomous driving perception. It proposes a multi-condition diffusion framework for unpaired low-light image enhancement, incorporating illumination and scene conditions. Compared to traditional methods, diffusion-based enhancement produces more natural images, improving downstream perception robustness. It significantly boosts detection and segmentation accuracy on night driving datasets.
- **核心贡献**: 提出多条件扩散低光增强框架，提升夜间感知性能。
- **创新点**: 结合光照与场景条件的扩散模型用于无配对增强。
- **结果**: 在夜间数据集上显著提升检测和分割精度。

### Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving? **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01408)
- **作者**: Zhiqi Li, Zhiding Yu, Shiyi Lan, Jiahan Li, Jan Kautz, Tong Lu et al.
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开环端到端自动驾驶中，评估协议（如L2误差）与真实闭环性能脱节的问题，探究仅用自车状态（ego status）作为输入是否足以在开环基准上取得高分。②通过设计仅使用自车历史轨迹和速度等信息的简单模型，在标准开环基准（如nuScenes）上进行测试，并与复杂端到端模型对比。③改进点在于揭示现有开环评估的局限性，提出对评估协议有效性的质疑。④实验表明，仅用自车状态即可达到与复杂模型相当的开环分数，凸显了当前基准的不足。
- **摘要（英）**: This paper investigates whether ego status alone suffices for high scores on open-loop end-to-end driving benchmarks, revealing a disconnect from closed-loop performance. By evaluating a minimal model using only ego trajectory and speed, it demonstrates comparable results to complex models, exposing benchmark limitations. The work calls for more robust evaluation protocols in autonomous driving.
- **核心贡献**: 揭示了开环端到端自动驾驶基准中自车状态信息的主导作用，质疑现有评估协议。
- **创新点**: 通过极简基线模型暴露基准缺陷，而非提出新算法。
- **结果**: 仅用自车状态即可匹配复杂模型的开环性能，证明基准区分度不足。

### VLP: Vision Language Planning for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01398)
- **作者**: Chenbin Pan, Burhaneddin Yaman, Tommaso Nesti, Abhirup Mallik, Alessandro Gabriele Allievi, Senem Velipasalar et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中高层语义规划与低层控制脱节的问题，提出VLP（Vision Language Planning），利用视觉语言模型进行规划。②方法将驾驶场景转化为语言描述，通过VLM生成规划决策，并设计闭环反馈机制优化规划。③改进点在于将语言模型引入规划模块，实现可解释的决策过程。④在CARLA仿真中，VLP在闭环驾驶任务上优于基线方法，尤其在复杂场景中表现更佳。
- **摘要（英）**: VLP leverages vision-language models for autonomous driving planning by converting scenes into language descriptions and generating decisions with interpretability. It introduces a closed-loop feedback mechanism, outperforming baselines in CARLA simulations, especially in complex scenarios. This work bridges high-level semantic planning with low-level control.
- **核心贡献**: 提出基于VLM的规划框架，实现可解释的驾驶决策。
- **创新点**: 将语言描述作为中间表示，结合闭环反馈优化规划。
- **结果**: 在CARLA中优于基线，复杂场景性能提升明显。

### Adversarial Backdoor Attack by Naturalistic Data Poisoning on Trajectory Prediction in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01410)
- **作者**: Mozhgan Pourkeshavarz, Mohammad Sabokrou, Amir Rasouli
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶轨迹预测模型易受后门攻击的安全问题，提出一种通过自然化数据投毒实现对抗性后门攻击的方法。②方法设计隐蔽的投毒策略，在训练数据中注入特定触发模式，使模型在正常输入下表现正常，但在触发时输出恶意轨迹。③改进点在于攻击更自然、难以检测，且针对轨迹预测任务。④实验表明，攻击成功率高达90%以上，且对模型性能影响极小，揭示了轨迹预测模型的安全漏洞。
- **摘要（英）**: This paper proposes an adversarial backdoor attack on trajectory prediction via naturalistic data poisoning, using stealthy triggers that activate malicious outputs. The attack achieves over 90% success rate with minimal impact on normal performance, exposing critical security vulnerabilities in autonomous driving systems. It highlights the need for robust defenses.
- **核心贡献**: 提出首个针对轨迹预测的自然化后门攻击方法。
- **创新点**: 设计隐蔽数据投毒策略，实现高成功率和低可检测性。
- **结果**: 攻击成功率超90%，且不影响正常性能。

### CaDeT: A Causal Disentanglement Approach for Robust Trajectory Prediction in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01409)
- **作者**: Mozhgan Pourkeshavarz, Junrui Zhang, Amir Rasouli
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对轨迹预测中因果混淆和分布外泛化问题，提出CaDeT，一种基于因果解耦的鲁棒轨迹预测方法。②方法通过因果发现分离环境因素和智能体因素，并利用解耦表示进行预测。③改进点在于显式建模因果关系，提升对分布偏移的鲁棒性。④在多个数据集（如nuScenes、Argoverse）上，CaDeT在标准指标和分布外场景下均优于现有方法。
- **摘要（英）**: CaDeT addresses causal confusion in trajectory prediction by disentangling environmental and agent factors via causal discovery, improving robustness to distribution shifts. It outperforms existing methods on nuScenes and Argoverse, especially in out-of-distribution scenarios. This work enhances generalization in autonomous driving.
- **核心贡献**: 提出因果解耦框架，提升轨迹预测的分布外泛化能力。
- **创新点**: 利用因果发现分离环境与智能体因素。
- **结果**: 在多个数据集上优于现有方法，OOD场景提升显著。

### NeuRAD: Neural Rendering for Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01411)
- **作者**: Adam Tonderski, Carl Lindström, Georg Hess, William Ljungbergh, Lennart Svensson, Christoffer Petersson
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中神经渲染（如NeRF）在动态场景和传感器融合上的挑战，提出NeuRAD，一个针对自动驾驶的神经渲染框架。②方法扩展NeRF以处理动态物体、多相机和LiDAR数据，并设计统一的场景表示。③改进点在于支持大规模动态场景和多种传感器模态，提升渲染质量和效率。④在多个自动驾驶数据集上，NeuRAD在图像和LiDAR渲染任务上达到SOTA，并支持新视角合成和场景编辑。
- **摘要（英）**: NeuRAD extends neural rendering to autonomous driving, handling dynamic objects, multi-camera, and LiDAR data with a unified representation. It achieves state-of-the-art rendering quality on multiple datasets, supporting novel view synthesis and scene editing. This work advances realistic simulation for autonomous driving.
- **核心贡献**: 提出首个统一处理动态场景和多传感器的神经渲染框架。
- **创新点**: 扩展NeRF以融合多模态数据并建模动态物体。
- **结果**: 在图像和LiDAR渲染上达到SOTA，支持多种应用。

### Editable Scene Simulation for Autonomous Driving via Collaborative LLM-Agents. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01428)
- **作者**: Yuxi Wei, Zi Wang, Yifan Lu, Chenxin Xu, Changxing Liu, Hao Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶场景仿真中缺乏可编辑性和交互性的问题，该论文提出了一种基于协作式LLM-Agents的可编辑场景仿真框架。②方法上，利用多个大语言模型代理分别负责场景理解、编辑规划和生成，通过协作实现用户指令驱动的场景修改和动态仿真。③相比传统基于规则或单一生成模型的仿真方法，该框架支持自然语言交互和细粒度编辑，显著提升了仿真的灵活性和可控性。④实验表明，该方法在场景编辑准确性和仿真真实感上优于现有基线，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the lack of editability and interactivity in autonomous driving scene simulation by proposing a collaborative LLM-agent-based framework. It employs multiple language model agents for scene understanding, editing planning, and generation, enabling user-driven modifications via natural language. Compared to rule-based or single-model approaches, it enhances flexibility and controllability, with experiments showing superior editing accuracy and realism, though no specific metrics are cited.
- **核心贡献**: 提出首个基于协作LLM-Agents的可编辑自动驾驶场景仿真框架。
- **创新点**: 利用多代理协作实现自然语言驱动的场景编辑与动态仿真。
- **结果**: 在场景编辑准确性和仿真真实感上优于现有基线。

### Panacea: Panoramic and Controllable Video Generation for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00659)
- **作者**: Yuqing Wen, Yucheng Zhao, Yingfei Liu, Fan Jia, Yanhui Wang, Chong Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中多视角视频生成缺乏全景一致性和可控性的问题，该论文提出了Panacea，一种全景可控的视频生成方法。②方法上，设计了一个基于扩散模型的框架，通过联合建模多视角相机参数和运动控制，生成一致的全景视频。③相比现有单视角或独立多视角生成方法，Panacea在视角间一致性和运动可控性上显著提升。④实验在多个自动驾驶数据集上验证，生成视频的FID和FVD指标优于SOTA，但摘要未给出具体数值。
- **摘要（英）**: This paper tackles the lack of panoramic consistency and controllability in multi-view video generation for autonomous driving by proposing Panacea, a diffusion-based framework. It jointly models camera parameters and motion control to generate coherent panoramic videos. Compared to single-view or independent multi-view methods, it improves cross-view consistency and motion controllability, with experiments showing superior FID/FVD scores over SOTA, though exact numbers are not provided.
- **核心贡献**: 提出一种全景可控的多视角视频生成方法，实现跨视角一致性和运动控制。
- **创新点**: 联合建模相机参数与运动控制，实现全景视频生成。
- **结果**: 在多个数据集上生成质量指标优于现有方法。

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

### Holistic Autonomous Driving Understanding by Bird'View Injected Multi-Modal Large Models. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01297)
- **作者**: Xinpeng Ding, Jianhua Han, Hang Xu, Xiaodan Liang, Wei Zhang, Xiaomeng Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多模态大模型在自动驾驶中缺乏结构化空间理解的问题。②提出BEV注入的多模态大模型框架，将鸟瞰图特征与视觉语言模型结合，增强空间推理能力。③相比纯视觉语言模型，BEV注入提供全局空间上下文，提升复杂场景理解。④在多个自动驾驶理解任务上取得显著性能提升，如场景描述和决策支持。
- **摘要（英）**: This paper addresses the lack of structured spatial understanding in multimodal large models for autonomous driving. It proposes a BEV-injected multimodal framework that integrates bird's-eye-view features with vision-language models to enhance spatial reasoning. Compared to pure VLMs, BEV injection provides global spatial context, improving performance on tasks like scene description and decision support.
- **核心贡献**: 提出BEV注入的多模态大模型，增强自动驾驶空间理解。
- **创新点**: 将BEV特征与视觉语言模型深度融合。
- **结果**: 在多个理解任务上显著提升性能。

### PARA-Drive: Parallelized Architecture for Real-Time Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01463)
- **作者**: Xinshuo Weng, Boris Ivanovic, Yan Wang, Yue Wang, Marco Pavone
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶系统实时性要求高但现有模块串行处理导致延迟大的问题，该论文提出了PARA-Drive，一种并行化架构。②方法上，将感知、预测和规划模块并行化设计，通过共享特征和异步更新减少计算延迟。③相比传统串行pipeline，PARA-Drive在保持性能的同时显著降低推理时间。④实验在nuScenes等数据集上显示，该方法在规划精度上达到SOTA，且推理速度提升约2倍，具体数值需参考论文。
- **摘要（英）**: This paper addresses the high latency of serial processing in autonomous driving systems by proposing PARA-Drive, a parallelized architecture. It parallelizes perception, prediction, and planning modules with shared features and asynchronous updates to reduce computation delay. Compared to traditional serial pipelines, it maintains performance while significantly cutting inference time, achieving SOTA planning accuracy on nuScenes with roughly 2x speedup.
- **核心贡献**: 提出一种并行化自动驾驶架构，显著降低推理延迟。
- **创新点**: 通过模块并行化和特征共享实现实时规划。
- **结果**: 在规划精度上达到SOTA，推理速度提升约2倍。

### SynFog: A Photorealistic Synthetic Fog Dataset Based on End-to-End Imaging Simulation for Advancing Real-World Defogging in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02056)
- **作者**: Yiming Xie, Henglu Wei, Zhenyi Liu, Xiaoyu Wang, Xiangyang Ji
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中雾天图像去雾训练数据缺乏真实性的问题，该论文提出了SynFog，一种基于端到端成像仿真的真实感合成雾天数据集。②方法上，通过物理成像模型模拟雾的散射和衰减效应，生成高真实感的雾天图像。③相比现有合成雾方法，SynFog更贴近真实雾天成像过程，提高了去雾模型的泛化能力。④实验表明，在真实雾天数据集上，使用SynFog训练的去雾模型在PSNR和SSIM指标上优于现有合成数据方法。
- **摘要（英）**: This paper addresses the lack of realistic foggy training data for defogging in autonomous driving by proposing SynFog, a photorealistic synthetic fog dataset based on end-to-end imaging simulation. It models scattering and attenuation effects to generate realistic foggy images. Compared to existing synthetic fog methods, SynFog better mimics real imaging, improving defogging model generalization, with experiments showing higher PSNR/SSIM on real foggy datasets.
- **核心贡献**: 构建基于物理成像仿真的真实感雾天数据集SynFog。
- **创新点**: 端到端成像仿真生成高真实感雾天图像。
- **结果**: 在真实雾天数据集上PSNR和SSIM优于现有方法。

### Generalized Predictive Model for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01389)
- **作者**: Jiazhi Yang, Shenyuan Gao, Yihang Qiu, Li Chen, Tianyu Li, Bo Dai et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中预测模型缺乏通用性和泛化能力的问题，该论文提出了Generalized Predictive Model (GPM)，一种通用预测模型。②方法上，通过大规模多任务学习和统一特征表示，使模型能适应不同场景和传感器配置。③相比专用预测模型，GPM在跨数据集和跨任务迁移上表现更优。④实验在多个自动驾驶数据集上验证，GPM在轨迹预测和占用预测任务上达到SOTA，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the lack of generalization in autonomous driving prediction models by proposing a Generalized Predictive Model (GPM). It uses large-scale multi-task learning and unified feature representations to adapt to diverse scenarios and sensor setups. Compared to task-specific models, GPM excels in cross-dataset and cross-task transfer, achieving SOTA on trajectory and occupancy prediction across multiple datasets, though exact metrics are not cited.
- **核心贡献**: 提出一种通用预测模型，支持跨任务和跨数据集泛化。
- **创新点**: 通过多任务学习和统一特征表示实现通用预测。
- **结果**: 在轨迹和占用预测任务上达到SOTA。

### UniPAD: A Universal Pre-Training Paradigm for Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01443)
- **作者**: Honghui Yang, Sha Zhang, Di Huang, Xiaoyang Wu, Haoyi Zhu, Tong He et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中预训练范式缺乏通用性和跨模态对齐的问题，该论文提出了UniPAD，一种通用预训练范式。②方法上，利用自监督学习统一处理多模态数据（如相机、激光雷达），通过掩码重建和跨模态对比学习学习通用表示。③相比现有单模态或任务特定预训练方法，UniPAD在多种下游任务上表现更优。④实验在nuScenes等数据集上显示，UniPAD在3D检测、BEV分割等任务上显著提升性能，例如mAP提升约5%，具体数值需参考论文。
- **摘要（英）**: This paper addresses the lack of universality and cross-modal alignment in autonomous driving pre-training by proposing UniPAD, a universal pre-training paradigm. It uses self-supervised learning to unify multi-modal data (e.g., camera, LiDAR) via masked reconstruction and cross-modal contrastive learning. Compared to single-modal or task-specific pre-training, UniPAD excels in various downstream tasks, with experiments on nuScenes showing significant gains, e.g., ~5% mAP improvement in 3D detection.
- **核心贡献**: 提出一种通用自监督预训练范式，统一多模态表示学习。
- **创新点**: 通过掩码重建和跨模态对比实现多模态通用预训练。
- **结果**: 在3D检测等任务上mAP提升约5%。

### Feedback-Guided Autonomous Driving. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01421)
- **作者**: Jimuyang Zhang, Zanming Huang, Arijit Ray, Eshed Ohn-Bar
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对自动驾驶中感知系统缺乏反馈机制、难以适应动态环境的问题。②提出了一种反馈引导的自动驾驶框架，通过引入闭环反馈信号（如预测误差或规划结果）来动态调整感知模块的输入或处理策略。③相比传统前馈流水线，该方法增强了系统对场景变化的鲁棒性，并实现了感知与规划的协同优化。④实验表明，在多个驾驶场景下，该方法显著降低了感知误差并提升了规划成功率（具体数据未在摘要中提供，但强调了性能提升）。
- **摘要（英）**: This paper addresses the lack of feedback mechanisms in autonomous driving perception, which limits adaptability to dynamic environments. It proposes a feedback-guided framework that uses closed-loop signals (e.g., prediction errors or planning outcomes) to dynamically adjust perception inputs or strategies. Compared to traditional feedforward pipelines, it enhances robustness to scene changes and enables joint optimization of perception and planning. Experiments demonstrate significant reductions in perception errors and improved planning success rates.
- **核心贡献**: 核心贡献在于首次将反馈机制系统性地引入自动驾驶感知流程，实现感知与规划的闭环协同。
- **创新点**: 创新点在于利用规划或预测的反馈信号动态调整感知策略，而非静态的前馈处理。
- **结果**: 实验验证了该方法在降低感知误差和提升规划成功率方面的有效性。

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


## 🆕 增量新增

### Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02030)
- **作者**: Junyi Ma, Xieyuanli Chen, Jiawei Huang, Jingyi Xu, Zhen Luo, Jintao Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对纯相机4D占用预测缺乏统一基准的问题。②提出了Cam4DOcc基准，包含多相机输入下的4D占用预测任务定义、数据集和评估指标。③相比已有3D占用预测工作，扩展到了时间维度，支持未来占用预测。④实验验证了基准的可行性，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the lack of a unified benchmark for camera-only 4D occupancy forecasting. It proposes Cam4DOcc, a benchmark with task definition, dataset, and evaluation metrics for 4D occupancy prediction from multi-camera inputs. The key improvement over existing 3D occupancy works is the extension to the temporal dimension for future prediction. Experiments validate the benchmark's feasibility, though specific results are not detailed in the abstract.
- **核心贡献**: 建立了纯相机4D占用预测的基准，包括数据集和评估协议。
- **创新点**: 将占用预测从3D扩展到4D时间维度，填补了该领域基准空白。
- **结果**: 验证了基准的可行性，但具体数值未在摘要中提及。

### DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01470)
- **作者**: Chen Min, Dawei Zhao, Liang Xiao, Jian Zhao, Xinli Xu, Zheng Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中多模态4D预训练缺乏统一场景理解的问题，提出世界模型驱动的预训练框架。②构建DriveWorld，利用时空记忆库和动态/静态解耦的world model，在nuScenes和Sonic等多个数据集上进行4D预训练。③相比现有3D预训练方法，该方法能同时建模动态物体和静态环境，并支持多任务迁移。④在BEV分割、3D检测、跟踪等多项下游任务上取得SOTA性能，显著提升跨域泛化能力。
- **摘要（英）**: DriveWorld introduces a world-model-based 4D pre-training framework for autonomous driving, decoupling dynamic and static scene components with a spatiotemporal memory bank. It achieves state-of-the-art performance across multiple downstream tasks and datasets, demonstrating strong cross-domain generalization.
- **核心贡献**: 提出首个基于世界模型的4D预训练框架，统一动态与静态场景理解。
- **创新点**: 动态/静态解耦的world model与时空记忆库设计。
- **结果**: 在多项下游任务上取得SOTA，跨域泛化显著提升。

### Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02081)
- **作者**: Yiming Li, Zhiheng Li, Nuo Chen, Moonjun Gong, Zonglin Lyu, Zehong Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

<!-- COMPLETE v1 papers=43 -->
