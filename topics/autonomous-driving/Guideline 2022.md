# Autonomous Driving — 2022 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.16258](https://arxiv.org/abs/2203.16258) · 📚 被引 112
- **作者**: Corentin Sautier, Gilles Puy, Spyros Gidaris, Alexandre Boulch, Andrei Bursuc, Renaud Marlet
- **🏷️ 机构**: valeo.ai,Paris,France
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对自动驾驶中3D感知模型依赖大量标注数据的问题，提出自监督预训练方法。②利用同步校准的图像和LiDAR数据，通过超像素池化点云和图像特征，训练3D网络匹配跨模态特征，无需任何标注。③相比已有自监督方法，创新在于使用超像素进行区域对比，适应自动驾驶数据的视觉一致性。④实验表明，该方法在3D分割和检测任务上有效提升预训练模型性能。
- **摘要（英）**: This paper addresses the heavy annotation requirement for 3D perception models in autonomous driving by proposing a self-supervised pre-training method. It leverages synchronized image and LiDAR data, using superpixels to pool features and train a 3D network to match cross-modal representations without labels. Compared to prior work, it uniquely employs superpixel-based region contrast for driving data. Experiments show improved performance on downstream 3D tasks.
- **核心贡献**: 提出基于超像素的图像到LiDAR自监督蒸馏预训练方法。
- **创新点**: 利用超像素实现跨模态特征匹配，无需标注。
- **结果**: 在3D分割和检测任务上提升预训练效果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Segmenting or detecting objects in sparse Lidar point clouds are two important tasks in autonomous driving to allow a vehicle to act safely in its 3D environment. The best performing methods in 3D semantic segmentation or object detection rely on a large amount of annotated data. Yet annotating 3D Lidar data for these tasks is tedious and costly. In this context, we propose a self-supervised pre-training method for 3D perception models that is tailored to autonomous driving data. Specifically, we leverage the availability of synchronized and calibrated image and Lidar sensors in autonomous driving setups for distilling self-supervised pre-trained image representations into 3D models. Hence, our method does not require any point cloud nor image annotations. The key ingredient of our method is the use of superpixels which are used to pool 3D point features and 2D pixel features in visually similar regions. We then train a 3D network on the self-supervised task of matching these pooled point features with the corresponding pooled image pixel features. The advantages of contrasting regions obtained by superpixels are that: (1) grouping together pixels and points of visually coherent regions leads to a more meaningful contrastive task that produces features well adapted to 3D semantic segmentation and 3D object detection; (2) all the different regions have the same weight in the contrastive loss regardless of the number of 3D points sampled in these regions; (3) it mitigates the noise produced by incorrect matching of points and pixels due to occlusions between the different sensors. Extensive experiments on autonomous driving datasets demonstrate the ability of our image-to-Lidar distillation strategy to produce 3D representations that transfer well on semantic segmentation and object detection tasks.

</details>

### Exploiting Temporal Relations on Radar Perception for Autonomous Driving.
- **链接**: [arXiv:2204.01184](https://arxiv.org/abs/2204.01184) · 📚 被引 56
- **作者**: Peizhao Li, Pu Wang, Karl Berntorp, Hongfu Liu
- **🏷️ 机构**: Brandeis University, Mitsubishi Electric Research Laboratories
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the object recognition problem in autonomous driving using automotive radar sensors. Comparing to Lidar sensors, radar is cost-effective and robust in all-weather conditions for perception in autonomous driving. However, radar signals suffer from low angular resolution and precision in recognizing surrounding objects. To enhance the capacity of automotive radar, in this work, we exploit the temporal information from successive ego-centric bird-eye-view radar image frames for radar object recognition. We leverage the consistency of an object's existence and attributes (size, orientation, etc.), and propose a temporal relational layer to explicitly model the relations between objects within successive radar images. In both object detection and multiple object tracking, we show the superiority of our method compared to several baseline approaches.

</details>

### LTP: Lane-based Trajectory Prediction for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01662) · 📚 被引 83
- **作者**: Jingke Wang, Tengju Ye, Ziqing Gu, Junbo Chen
- **🏷️ 机构**: Alibaba Group
- **会议**: CVPR 2022

### Unifying Panoptic Segmentation for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02066) · 📚 被引 47
- **作者**: Oliver Zendel, Matthias Schörghuber, Bernhard Rainer, Markus Murschitz, Csaba Beleznai
- **🏷️ 机构**: AIT Austrian Institute of Technology
- **会议**: CVPR 2022

### Coopernaut: End-to-End Driving with Cooperative Perception for Networked Vehicles.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01674) · 📚 被引 129
- **作者**: Jiaxun Cui, Hang Qiu, Dian Chen, Peter Stone, Yuke Zhu
- **🏷️ 机构**: The University of Texas at Austin, Stanford University
- **会议**: CVPR 2022

### Generating Useful Accident-Prone Driving Scenarios via a Learned Traffic Prior.
- **链接**: [arXiv:2112.05077](https://arxiv.org/abs/2112.05077) · 📚 被引 135
- **作者**: Davis Rempe, Jonah Philion, Leonidas J. Guibas, Sanja Fidler, Or Litany
- **🏷️ 机构**: Stanford University, NVIDIA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Evaluating and improving planning for autonomous vehicles requires scalable generation of long-tail traffic scenarios. To be useful, these scenarios must be realistic and challenging, but not impossible to drive through safely. In this work, we introduce STRIVE, a method to automatically generate challenging scenarios that cause a given planner to produce undesirable behavior, like collisions. To maintain scenario plausibility, the key idea is to leverage a learned model of traffic motion in the form of a graph-based conditional VAE. Scenario generation is formulated as an optimization in the latent space of this traffic model, perturbing an initial real-world scene to produce trajectories that collide with a given planner. A subsequent optimization is used to find a "solution" to the scenario, ensuring it is useful to improve the given planner. Further analysis clusters generated scenarios based on collision type. We attack two planners and show that STRIVE successfully generates realistic, challenging scenarios in both cases. We additionally "close the loop" and use these scenarios to optimize hyperparameters of a rule-based planner.

</details>

### Towards Driving-Oriented Metric for Lane Detection Models.
- **链接**: [arXiv:2203.16851](https://arxiv.org/abs/2203.16851) · 📚 被引 15
- **作者**: Takami Sato, Qi Alfred Chen
- **🏷️ 机构**: University of California,Irvine
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> After the 2017 TuSimple Lane Detection Challenge, its dataset and evaluation based on accuracy and F1 score have become the de facto standard to measure the performance of lane detection methods. While they have played a major role in improving the performance of lane detection methods, the validity of this evaluation method in downstream tasks has not been adequately researched. In this study, we design 2 new driving-oriented metrics for lane detection: End-to-End Lateral Deviation metric (E2E-LD) is directly formulated based on the requirements of autonomous driving, a core downstream task of lane detection; Per-frame Simulated Lateral Deviation metric (PSLD) is a lightweight surrogate metric of E2E-LD. To evaluate the validity of the metrics, we conduct a large-scale empirical study with 4 major types of lane detection approaches on the TuSimple dataset and our newly constructed dataset Comma2k19-LD. Our results show that the conventional metrics have strongly negative correlations ($\leq$-0.55) with E2E-LD, meaning that some recent improvements purely targeting the conventional metrics may not have led to meaningful improvements in autonomous driving, but rather may actually have made it worse by overfitting to the conventional metrics. As autonomous driving is a security/safety-critical system, the underestimation of robustness hinders the sound development of practical lane detection models. We hope that our study will help the community achieve more downstream task-aware evaluations for lane detection.

</details>

### ST-P3: End-to-End Vision-Based Autonomous Driving via Spatial-Temporal Feature Learning.
- **链接**: [arXiv:2207.07601](https://arxiv.org/abs/2207.07601) · [代码](https://github.com/OpenPerceptionX/ST-P3) · 📚 被引 258
- **作者**: Shengchao Hu, Li Chen, Penghao Wu, Hongyang Li, Junchi Yan, Dacheng Tao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2022

- Pseudo-Stereo for Monocular 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. → [3d-detection](../3d-detection/Guideline%202022.md)
- DAIR-V2X: A Large-Scale Dataset for Vehicle-Infrastructure Cooperative 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)

## 🆕 增量新增

### V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.10638](https://arxiv.org/abs/2203.10638) · 📚 被引 520
- **作者**: Runsheng Xu, Hao Xiang, Zhengzhong Tu, Xin Xia, Ming-Hsuan Yang, Jiaqi Ma
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2022
- **摘要（中）**: 针对自动驾驶中单车感知的局限，该论文提出V2X-ViT，利用车联网（V2X）通信和视觉Transformer实现多智能体协同感知。通过异构多智能体自注意力和多尺度窗口自注意力交替层，有效融合车辆和基础设施信息，并处理异步、位姿误差和异构性挑战。在CARLA和OpenCDA构建的大规模数据集上，V2X-ViT在3D目标检测上达到SOTA，且在噪声环境下表现鲁棒。
- **摘要（英）**: This paper proposes V2X-ViT, a vision Transformer-based cooperative perception framework for V2X communication, using alternating heterogeneous multi-agent self-attention and multi-scale window self-attention to fuse information across vehicles and infrastructure. It achieves SOTA 3D detection on a large-scale CARLA/OpenCDA dataset and remains robust under noisy conditions.
- **核心贡献**: 提出了基于视觉Transformer的V2X协同感知框架V2X-ViT。
- **创新点**: 设计异构多智能体自注意力与多尺度窗口自注意力的统一架构。
- **结果**: 在3D目标检测上达到SOTA，并在噪声环境下保持鲁棒性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we investigate the application of Vehicle-to-Everything (V2X) communication to improve the perception performance of autonomous vehicles. We present a robust cooperative perception framework with V2X communication using a novel vision Transformer. Specifically, we build a holistic attention model, namely V2X-ViT, to effectively fuse information across on-road agents (i.e., vehicles and infrastructure). V2X-ViT consists of alternating layers of heterogeneous multi-agent self-attention and multi-scale window self-attention, which captures inter-agent interaction and per-agent spatial relationships. These key modules are designed in a unified Transformer architecture to handle common V2X challenges, including asynchronous information sharing, pose errors, and heterogeneity of V2X components. To validate our approach, we create a large-scale V2X perception dataset using CARLA and OpenCDA. Extensive experimental results demonstrate that V2X-ViT sets new state-of-the-art performance for 3D object detection and achieves robust performance even under harsh, noisy environments. The code is available at https://github.com/DerrickXuNu/v2x-vit.

</details>

### Beyond 3D Siamese Tracking: A Motion-Centric Paradigm for 3D Single Object Tracking in Point Clouds. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.01730](https://arxiv.org/abs/2203.01730) · 📚 被引 103
- **作者**: Chaoda Zheng, Xu Yan, Haiming Zhang, Baoyuan Wang, Shenghui Cheng, Shuguang Cui et al.
- **🏷️ 机构**: The Chinese University of Hong Kong (Shenzhen), Xiaobing.AI, Westlake University
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对3D单目标跟踪中基于Siamese外观匹配方法在LiDAR点云上效果不佳的问题，因为点云纹理少且不完整。②提出了运动中心范式，并设计了M^2-Track两阶段跟踪器，先通过运动变换定位目标，再通过运动辅助形状补全细化。③相比已有Siamese方法，该范式利用目标运动线索，避免外观匹配的局限。④在KITTI、NuScenes和Waymo上分别提升约8%、17%和22%的精度，运行速度达57FPS。
- **摘要（英）**: This paper addresses the limitations of Siamese appearance matching in 3D single object tracking due to textureless and incomplete LiDAR point clouds. It introduces a motion-centric paradigm with M^2-Track, a two-stage tracker that localizes via motion transformation and refines via motion-assisted shape completion. Compared to prior methods, it leverages motion clues, avoiding appearance matching issues. Experiments show significant precision gains on KITTI, NuScenes, and Waymo, running at 57FPS.
- **核心贡献**: 提出了运动中心的3D单目标跟踪范式及M^2-Track。
- **创新点**: 从运动视角而非外观匹配处理3D跟踪。
- **结果**: 在多个数据集上大幅提升精度并保持实时速度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D single object tracking (3D SOT) in LiDAR point clouds plays a crucial role in autonomous driving. Current approaches all follow the Siamese paradigm based on appearance matching. However, LiDAR point clouds are usually textureless and incomplete, which hinders effective appearance matching. Besides, previous methods greatly overlook the critical motion clues among targets. In this work, beyond 3D Siamese tracking, we introduce a motion-centric paradigm to handle 3D SOT from a new perspective. Following this paradigm, we propose a matching-free two-stage tracker M^2-Track. At the 1^st-stage, M^2-Track localizes the target within successive frames via motion transformation. Then it refines the target box through motion-assisted shape completion at the 2^nd-stage. Extensive experiments confirm that M^2-Track significantly outperforms previous state-of-the-arts on three large-scale datasets while running at 57FPS (~8%, ~17%, and ~22%) precision gains on KITTI, NuScenes, and Waymo Open Dataset respectively). Further analysis verifies each component's effectiveness and shows the motion-centric paradigm's promising potential when combined with appearance matching.

</details>

### Talisman: Targeted Active Learning for Object Detection with Rare Classes and Slices Using Submodular Mutual Information. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2112.00166](https://arxiv.org/abs/2112.00166) · 📚 被引 18
- **作者**: Suraj Kothawade, Saikat Ghosh, Sumit Shekhar, Yu Xiang, Rishabh K. Iyer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对目标检测中稀有类别和数据切片（如夜间摩托车）性能差的问题。②提出了TALISMAN框架，利用子模互信息函数基于RoI特征进行目标主动学习，选择信息量大的样本。③相比基于不确定性或全局描述符的方法，TALISMAN更适应稀有切片场景。④在实验中显著提升了稀有类别的检测性能。
- **摘要（英）**: This paper addresses poor performance on rare classes and slices in object detection. It proposes TALISMAN, a targeted active learning framework using submodular mutual information on RoI features. It outperforms uncertainty-based methods, improving rare slice detection.
- **核心贡献**: 提出了基于子模互信息的目标主动学习框架，提升稀有类别检测。
- **创新点**: 利用RoI特征和子模函数进行样本选择。
- **结果**: 在稀有切片上显著提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks based object detectors have shown great success in a variety of domains like autonomous vehicles, biomedical imaging, etc. It is known that their success depends on a large amount of data from the domain of interest. While deep models often perform well in terms of overall accuracy, they often struggle in performance on rare yet critical data slices. For example, data slices like "motorcycle at night" or "bicycle at night" are often rare but very critical slices for self-driving applications and false negatives on such rare slices could result in ill-fated failures and accidents. Active learning (AL) is a well-known paradigm to incrementally and adaptively build training datasets with a human in the loop. However, current AL based acquisition functions are not well-equipped to tackle real-world datasets with rare slices, since they are based on uncertainty scores or global descriptors of the image. We propose TALISMAN, a novel framework for Targeted Active Learning or object detectIon with rare slices using Submodular MutuAl iNformation. Our method uses the submodular mutual information functions instantiated using features of the region of interest (RoI) to efficiently target and acquire data points with rare slices. We evaluate our framework on the standard PASCAL VOC07+12 and BDD100K, a real-world self-driving dataset. We observe that TALISMAN outperforms other methods by in terms of average precision on rare slices, and in terms of mAP.

</details>

### CODA: A Real-World Road Corner Case Dataset for Object Detection in Autonomous Driving.
- **链接**: [arXiv:2203.07724](https://arxiv.org/abs/2203.07724)
- **作者**: Kaican Li, Kai Chen, Haoyu Wang, Lanqing Hong, Chaoqiang Ye, Jianhua Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contemporary deep-learning object detection methods for autonomous driving usually assume prefixed categories of common traffic participants, such as pedestrians and cars. Most existing detectors are unable to detect uncommon objects and corner cases (e.g., a dog crossing a street), which may lead to severe accidents in some situations, making the timeline for the real-world application of reliable autonomous driving uncertain. One main reason that impedes the development of truly reliably self-driving systems is the lack of public datasets for evaluating the performance of object detectors on corner cases. Hence, we introduce a challenging dataset named CODA that exposes this critical problem of vision-based detectors. The dataset consists of 1500 carefully selected real-world driving scenes, each containing four object-level corner cases (on average), spanning more than 30 object categories. On CODA, the performance of standard object detectors trained on large-scale autonomous driving datasets significantly drops to no more than 12.8% in mAR. Moreover, we experiment with the state-of-the-art open-world object detector and find that it also fails to reliably identify the novel objects in CODA, suggesting that a robust perception system for autonomous driving is probably still far from reach. We expect our CODA dataset to facilitate further research in reliable detection for real-world autonomous driving. Our dataset will be released at https://coda-dataset.github.io.

</details>

### Self-Distillation for Robust LiDAR Semantic Segmentation in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19815-1_38) · 📚 被引 33
- **作者**: Jiale Li, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Point Cloud Compression with Range Image-Based Entropy Model for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_19) · 📚 被引 15
- **作者**: Sukai Wang, Ming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### InAction: Interpretable Action Decision Making for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_22) · 📚 被引 32
- **作者**: Taotao Jing, Haifeng Xia, Renran Tian, Haoran Ding, Xiao Luo, Joshua E. Domeyer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Motion Inspired Unsupervised Perception and Prediction in Autonomous Driving.
- **链接**: [arXiv:2210.08061](https://arxiv.org/abs/2210.08061)
- **作者**: Mahyar Najibi, Jingwei Ji, Yin Zhou, Charles R. Qi, Xinchen Yan, Scott Ettinger et al.
- **🏷️ 机构**: Waymo
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning-based perception and prediction modules in modern autonomous driving systems typically rely on expensive human annotation and are designed to perceive only a handful of predefined object categories. This closed-set paradigm is insufficient for the safety-critical autonomous driving task, where the autonomous vehicle needs to process arbitrarily many types of traffic participants and their motion behaviors in a highly dynamic world. To address this difficulty, this paper pioneers a novel and challenging direction, i.e., training perception and prediction models to understand open-set moving objects, with no human supervision. Our proposed framework uses self-learned flow to trigger an automated meta labeling pipeline to achieve automatic supervision. 3D detection experiments on the Waymo Open Dataset show that our method significantly outperforms classical unsupervised approaches and is even competitive to the counterpart with supervised scene flow. We further show that our approach generates highly promising results in open-set 3D detection and trajectory prediction, confirming its potential in closing the safety gap of fully supervised systems.

</details>

### Rethinking Closed-Loop Training for Autonomous Driving.
- **链接**: [arXiv:2306.15713](https://arxiv.org/abs/2306.15713)
- **作者**: Chris Zhang, Runsheng Guo, Wenyuan Zeng, Yuwen Xiong, Binbin Dai, Rui Hu et al.
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in high-fidelity simulators have enabled closed-loop training of autonomous driving agents, potentially solving the distribution shift in training v.s. deployment and allowing training to be scaled both safely and cheaply. However, there is a lack of understanding of how to build effective training benchmarks for closed-loop training. In this work, we present the first empirical study which analyzes the effects of different training benchmark designs on the success of learning agents, such as how to design traffic scenarios and scale training environments. Furthermore, we show that many popular RL algorithms cannot achieve satisfactory performance in the context of autonomous driving, as they lack long-term planning and take an extremely long time to train. To address these issues, we propose trajectory value learning (TRAVL), an RL-based driving agent that performs planning with multistep look-ahead and exploits cheaply generated imagined data for efficient learning. Our experiments show that TRAVL can learn much faster and produce safer maneuvers compared to all the baselines. For more information, visit the project website: https://waabi.ai/research/travl

</details>

### KING: Generating Safety-Critical Driving Scenarios for Robust Imitation via Kinematics Gradients.
- **链接**: [arXiv:2204.13683](https://arxiv.org/abs/2204.13683) · 📚 被引 92
- **作者**: Niklas Hanselmann, Katrin Renz, Kashyap Chitta, Apratim Bhattacharyya, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Simulators offer the possibility of safe, low-cost development of self-driving systems. However, current driving simulators exhibit naïve behavior models for background traffic. Hand-tuned scenarios are typically added during simulation to induce safety-critical situations. An alternative approach is to adversarially perturb the background traffic trajectories. In this paper, we study this approach to safety-critical driving scenario generation using the CARLA simulator. We use a kinematic bicycle model as a proxy to the simulator's true dynamics and observe that gradients through this proxy model are sufficient for optimizing the background traffic trajectories. Based on this finding, we propose KING, which generates safety-critical driving scenarios with a 20% higher success rate than black-box optimization. By solving the scenarios generated by KING using a privileged rule-based expert algorithm, we obtain training data for an imitation learning policy. After fine-tuning on this new data, we show that the policy becomes better at avoiding collisions. Importantly, our generated data leads to reduced collisions on both held-out scenarios generated via KING as well as traditional hand-crafted scenarios, demonstrating improved robustness.

</details>

### Action-Based Contrastive Learning for Trajectory Prediction.
- **链接**: [arXiv:2207.08664](https://arxiv.org/abs/2207.08664)
- **作者**: Marah Halawa, Olaf Hellwich, Pia Bideau
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Trajectory prediction is an essential task for successful human robot interaction, such as in autonomous driving. In this work, we address the problem of predicting future pedestrian trajectories in a first person view setting with a moving camera. To that end, we propose a novel action-based contrastive learning loss, that utilizes pedestrian action information to improve the learned trajectory embeddings. The fundamental idea behind this new loss is that trajectories of pedestrians performing the same action should be closer to each other in the feature space than the trajectories of pedestrians with significantly different actions. In other words, we argue that behavioral information about pedestrian action influences their future trajectory. Furthermore, we introduce a novel sampling strategy for trajectories that is able to effectively increase negative and positive contrastive samples. Additional synthetic trajectory samples are generated using a trained Conditional Variational Autoencoder (CVAE), which is at the core of several models developed for trajectory prediction. Results show that our proposed contrastive framework employs contextual information about pedestrian behavior, i.e. action, effectively, and it learns a better trajectory representation. Thus, integrating the proposed contrastive framework within a trajectory prediction model improves its results and outperforms state-of-the-art methods on three trajectory prediction benchmarks [31, 32, 26].

</details>

### K-Radar: 4D Radar Object Detection for Autonomous Driving in Various Weather Conditions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/185fdf627eaae2abab36205dcd19b817-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 33
- **作者**: Dong-Hee Paek, Seung-Hyun Kong, Kevin Tirta Wijaya
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Effective Adaptation in Multi-Task Co-Training for Unified Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7c319b62e2257b34cb0e1040ced2e007-Abstract-Conference.html) · 📚 被引 4
- **作者**: Xiwen Liang, Yangxin Wu, Jianhua Han, Hang Xu, Chunjing Xu, Xiaodan Liang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Trajectory-guided Control Prediction for End-to-end Autonomous Driving: A Simple yet Strong Baseline.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/286a371d8a0a559281f682f8fbf89834-Abstract-Conference.html) · 📚 被引 45
- **作者**: Penghao Wu, Xiaosong Jia, Li Chen, Junchi Yan, Hongyang Li, Yu Qiao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2022

### Unsupervised Adaptation from Repeated Traversals for Autonomous Driving.
- **链接**: [arXiv:2303.15286](https://arxiv.org/abs/2303.15286)
- **作者**: Yurong You, Cheng Perng Phoo, Katie Luo, Travis Zhang, Wei-Lun Chao, Bharath Hariharan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> For a self-driving car to operate reliably, its perceptual system must generalize to the end-user's environment -- ideally without additional annotation efforts. One potential solution is to leverage unlabeled data (e.g., unlabeled LiDAR point clouds) collected from the end-users' environments (i.e. target domain) to adapt the system to the difference between training and testing environments. While extensive research has been done on such an unsupervised domain adaptation problem, one fundamental problem lingers: there is no reliable signal in the target domain to supervise the adaptation process. To overcome this issue we observe that it is easy to collect unsupervised data from multiple traversals of repeated routes. While different from conventional unsupervised domain adaptation, this assumption is extremely realistic since many drivers share the same roads. We show that this simple additional assumption is sufficient to obtain a potent signal that allows us to perform iterative self-training of 3D object detectors on the target domain. Concretely, we generate pseudo-labels with the out-of-domain detector but reduce false positives by removing detections of supposedly mobile objects that are persistent across traversals. Further, we reduce false negatives by encouraging predictions in regions that are not persistent. We experiment with our approach on two large-scale driving datasets and show remarkable improvement in 3D object detection of cars, pedestrians, and cyclists, bringing us a step closer to generalizable autonomous driving.

</details>

## 跨领域论文（完整笔记在其他领域）

- BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. → [bev](../bev/Guideline%202022.md)
- TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers. → [3d-detection](../3d-detection/Guideline%202022.md)
- Pseudo-Stereo for Monocular 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Focal Sparse Convolutional Networks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention. → [object-detection](../object-detection/Guideline%202022.md)
- A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation. → [object-detection](../object-detection/Guideline%202022.md)
- Homography Loss for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Snowfall Simulation for Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- MonoDTR: Monocular 3D Object Detection with Depth-Aware Transformer. → [3d-detection](../3d-detection/Guideline%202022.md)
- Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. → [3d-detection](../3d-detection/Guideline%202022.md)
- DAIR-V2X: A Large-Scale Dataset for Vehicle-Infrastructure Cooperative 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Point-to-Voxel Knowledge Distillation for LiDAR Semantic Segmentation. → [3d-detection](../3d-detection/Guideline%202022.md)
- RIDDLE: Lidar Data Compression with Range Image Deep Delta Encoding. → [network-pruning](../network-pruning/Guideline%202022.md)
- MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone. → [3d-detection](../3d-detection/Guideline%202022.md)
- Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. → [3d-detection](../3d-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- PETR: Position Embedding Transformation for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Lidar Point Cloud Guided Monocular 3D Object Detection. → [bev](../bev/Guideline%202022.md)
- Rethinking IoU-based Optimization for Single-stage 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- PillarNet: Real-Time and High-Performance Pillar-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph. → [bev](../bev/Guideline%202022.md)
- ProposalContrast: Unsupervised Pre-training for LiDAR-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Point Cloud Compression with Sibling Context and Surface Priors. → [network-pruning](../network-pruning/Guideline%202022.md)
- 3D Siamese Transformer Network for Single Object Tracking on Point Clouds. → [tracking](../tracking/Guideline%202022.md)
- Differentiable Raycasting for Self-Supervised Occupancy Forecasting. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- PolarMOT: How Far Can Geometric Relations Take us in 3D Multi-object Tracking? → [tracking](../tracking/Guideline%202022.md)
- ST-P3: End-to-End Vision-Based Autonomous Driving via Spatial-Temporal Feature Learning. → [bev](../bev/Guideline%202022.md)
- PreTraM: Self-supervised Pre-training via Connecting Trajectory and Map. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Memory Replay with Data Compression for Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Sparse2Dense: Learning to Densify 3D Features for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Unifying Voxel-based Representation with Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Spatial Pruned Sparse Convolution for Efficient 3D Object Detection. → [network-pruning](../network-pruning/Guideline%202022.md)
- Fully Convolutional One-Stage 3D Object Detection on LiDAR Range Images. → [bev](../bev/Guideline%202022.md)
- DeepInteraction: 3D Object Detection via Modality Interaction. → [3d-detection](../3d-detection/Guideline%202022.md)
- Towards Efficient 3D Object Detection with Knowledge Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202022.md)


## 🆕 增量新增

### Semi-supervised 3D Object Detection with Proficient Teachers.
- **链接**: [arXiv:2207.12655](https://arxiv.org/abs/2207.12655) · 📚 被引 73
- **作者**: Junbo Yin, Jin Fang, Dingfu Zhou, Liangjun Zhang, Cheng-Zhong Xu, Jianbing Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dominated point cloud-based 3D object detectors in autonomous driving scenarios rely heavily on the huge amount of accurately labeled samples, however, 3D annotation in the point cloud is extremely tedious, expensive and time-consuming. To reduce the dependence on large supervision, semi-supervised learning (SSL) based approaches have been proposed. The Pseudo-Labeling methodology is commonly used for SSL frameworks, however, the low-quality predictions from the teacher model have seriously limited its performance. In this work, we propose a new Pseudo-Labeling framework for semi-supervised 3D object detection, by enhancing the teacher model to a proficient one with several necessary designs. First, to improve the recall of pseudo labels, a Spatialtemporal Ensemble (STE) module is proposed to generate sufficient seed boxes. Second, to improve the precision of recalled boxes, a Clusteringbased Box Voting (CBV) module is designed to get aggregated votes from the clustered seed boxes. This also eliminates the necessity of sophisticated thresholds to select pseudo labels. Furthermore, to reduce the negative influence of wrongly pseudo-labeled samples during the training, a soft supervision signal is proposed by considering Box-wise Contrastive Learning (BCL). The effectiveness of our model is verified on both ONCE and Waymo datasets. For example, on ONCE, our approach significantly improves the baseline by 9.51 mAP. Moreover, with half annotations, our model outperforms the oracle model with full annotations on Waymo.

</details>

<!-- COMPLETE v1 papers=24 -->
