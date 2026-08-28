# Autonomous Driving — 2022 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 34 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

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

### CODA: A Real-World Road Corner Case Dataset for Object Detection in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.07724](https://arxiv.org/abs/2203.07724)
- **作者**: Kaican Li, Kai Chen, Haoyu Wang, Lanqing Hong, Chaoqiang Ye, Jianhua Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对自动驾驶中现有检测器无法识别罕见物体和边缘案例（如过街的狗）的问题，该论文提出了CODA数据集，包含1500个真实驾驶场景，每个场景平均有4个物体级边缘案例，涵盖30多个类别。相比现有数据集，CODA专门用于评估检测器在边缘案例上的性能。实验表明，标准检测器在CODA上的mAR不超过12.8%，即使是最先进的开集检测器也难以可靠识别新物体，凸显了该问题的严峻性。
- **摘要（英）**: This paper addresses the issue that current detectors fail on rare objects and corner cases in autonomous driving by introducing CODA, a dataset with 1500 real-world scenes averaging four object-level corner cases across 30+ categories. Standard detectors achieve mAR below 12.8%, and even state-of-the-art open-world detectors struggle, highlighting the critical gap.
- **核心贡献**: 构建了首个大规模真实世界自动驾驶边缘案例检测数据集CODA。
- **创新点**: 聚焦于物体级边缘案例，提供多类别罕见物体标注。
- **结果**: 标准检测器mAR降至12.8%以下，验证了现有方法的不足。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contemporary deep-learning object detection methods for autonomous driving usually assume prefixed categories of common traffic participants, such as pedestrians and cars. Most existing detectors are unable to detect uncommon objects and corner cases (e.g., a dog crossing a street), which may lead to severe accidents in some situations, making the timeline for the real-world application of reliable autonomous driving uncertain. One main reason that impedes the development of truly reliably self-driving systems is the lack of public datasets for evaluating the performance of object detectors on corner cases. Hence, we introduce a challenging dataset named CODA that exposes this critical problem of vision-based detectors. The dataset consists of 1500 carefully selected real-world driving scenes, each containing four object-level corner cases (on average), spanning more than 30 object categories. On CODA, the performance of standard object detectors trained on large-scale autonomous driving datasets significantly drops to no more than 12.8% in mAR. Moreover, we experiment with the state-of-the-art open-world object detector and find that it also fails to reliably identify the novel objects in CODA, suggesting that a robust perception system for autonomous driving is probably still far from reach. We expect our CODA dataset to facilitate further research in reliable detection for real-world autonomous driving. Our dataset will be released at https://coda-dataset.github.io.

</details>

### Self-Distillation for Robust LiDAR Semantic Segmentation in Autonomous Driving. **⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19815-1_38) · 📚 被引 33
- **作者**: Jiale Li, Hang Dai, Yong Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对自动驾驶中LiDAR语义分割的鲁棒性问题，但摘要不完整，无法获取具体方法细节。②论文标题表明使用自蒸馏技术，可能通过教师-学生框架提升分割鲁棒性。③由于摘要缺失，无法评估具体改进点和效果。④建议查阅完整论文以获取实验数据。
- **摘要（英）**: This paper addresses robust LiDAR semantic segmentation in autonomous driving using self-distillation, but the abstract is incomplete, lacking method details and results. Further reading is needed for evaluation.
- **核心贡献**: 提出了基于自蒸馏的LiDAR语义分割方法（待确认）。
- **创新点**: 自蒸馏技术用于提升分割鲁棒性（待确认）。
- **结果**: 效果未知，需查阅完整论文。

### 3D Siamese Transformer Network for Single Object Tracking on Point Clouds. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.11995](https://arxiv.org/abs/2207.11995)
- **作者**: Le Hui, Lingpeng Wang, Linghua Tang, Kaihao Lan, Jin Xie, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对3D单目标跟踪中模板与搜索区域间外观差异大、跨相关学习困难的问题。②提出3D Siamese Transformer网络，使用自注意力捕获点云非局部信息以表征形状，解码器用交叉注意力上采样判别性特征，并设计迭代粗到细相关网络增强跨相关。③相比传统Siamese方法，显式利用Transformer建模长距离依赖和跨相关，提升鲁棒性。④实验表明在KITTI和nuScenes等基准上达到先进性能，但摘要未提供具体数值。
- **摘要（英）**: This paper tackles the challenge of robust cross-correlation learning in 3D single object tracking by introducing a Siamese Transformer network with self-attention for shape encoding and cross-attention for feature upsampling, plus an iterative coarse-to-fine correlation module. It achieves state-of-the-art performance on KITTI and nuScenes benchmarks, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出首个基于Siamese Transformer的3D单目标跟踪框架，有效学习模板与搜索区域的鲁棒跨相关。
- **创新点**: 结合自注意力与交叉注意力，并设计迭代粗到细相关网络，提升点云跟踪的判别能力。
- **结果**: 在多个基准上达到先进性能，具体数值未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Siamese network based trackers formulate 3D single object tracking as cross-correlation learning between point features of a template and a search area. Due to the large appearance variation between the template and search area during tracking, how to learn the robust cross correlation between them for identifying the potential target in the search area is still a challenging problem. In this paper, we explicitly use Transformer to form a 3D Siamese Transformer network for learning robust cross correlation between the template and the search area of point clouds. Specifically, we develop a Siamese point Transformer network to learn shape context information of the target. Its encoder uses self-attention to capture non-local information of point clouds to characterize the shape information of the object, and the decoder utilizes cross-attention to upsample discriminative point features. After that, we develop an iterative coarse-to-fine correlation network to learn the robust cross correlation between the template and the search area. It formulates the cross-feature augmentation to associate the template with the potential target in the search area via cross attention. To further enhance the potential target, it employs the ego-feature augmentation that applies self-attention to the local k-NN graph of the feature space to aggregate target features. Experiments on the KITTI, nuScenes, and Waymo datasets show that our method achieves state-of-the-art performance on the 3D single object tracking task.

</details>

### Point Cloud Compression with Range Image-Based Entropy Model for Autonomous Driving. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_19) · 📚 被引 15
- **作者**: Sukai Wang, Ming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对自动驾驶场景中点云压缩的熵模型设计问题。②论文标题表明提出基于距离图像的熵模型，但摘要为空，无法获取具体方法细节。③由于缺乏摘要，无法评估与现有工作的改进点。④效果未知。
- **摘要（英）**: This paper proposes a range image-based entropy model for point cloud compression in autonomous driving, but the abstract is empty, so no details on methodology, improvements, or results are available.
- **核心贡献**: 提出基于距离图像的熵模型用于自动驾驶点云压缩。
- **创新点**: 利用距离图像结构进行熵编码。
- **结果**: 未知。

### Differentiable Raycasting for Self-Supervised Occupancy Forecasting. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2210.01917](https://arxiv.org/abs/2210.01917) · 📚 被引 58
- **作者**: Tarasha Khurana, Peiyun Hu, Achal Dave, Jason Ziglar, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: ECCV 2022
- **摘要（中）**: ①针对自监督占用预测中，以自我为中心的freespace表示混淆了环境运动和自车运动，难以用于下游规划的问题。②提出使用几何占用作为替代表示，并通过可微光线投射将未来占用预测渲染为未来LiDAR扫描，与真实扫描对比进行自监督学习。③相比freespace，占用自然解耦环境与自车运动，且可微光线投射使占用作为内部表示涌现。④实验表明该方法在多个数据集上有效提升占用预测和规划性能，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the issue that ego-centric freespace representations confound environment and ego motion, hindering downstream planning, by proposing geometric occupancy as a disentangled alternative and using differentiable raycasting to render future occupancy into LiDAR sweeps for self-supervised learning. This approach enables occupancy to emerge as an internal representation, improving forecasting and planning performance on multiple datasets, though specific metrics are not detailed.
- **核心贡献**: 提出基于可微光线投射的自监督占用预测框架，实现环境与自车运动解耦。
- **创新点**: 利用可微光线投射将占用渲染为LiDAR扫描，实现无需标注的占用学习。
- **结果**: 在多个数据集上提升占用预测和规划性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motion planning for safe autonomous driving requires learning how the environment around an ego-vehicle evolves with time. Ego-centric perception of driveable regions in a scene not only changes with the motion of actors in the environment, but also with the movement of the ego-vehicle itself. Self-supervised representations proposed for large-scale planning, such as ego-centric freespace, confound these two motions, making the representation difficult to use for downstream motion planners. In this paper, we use geometric occupancy as a natural alternative to view-dependent representations such as freespace. Occupancy maps naturally disentangle the motion of the environment from the motion of the ego-vehicle. However, one cannot directly observe the full 3D occupancy of a scene (due to occlusion), making it difficult to use as a signal for learning. Our key insight is to use differentiable raycasting to "render" future occupancy predictions into future LiDAR sweep predictions, which can be compared with ground-truth sweeps for self-supervised learning. The use of differentiable raycasting allows occupancy to emerge as an internal representation within the forecasting network. In the absence of groundtruth occupancy, we quantitatively evaluate the forecasting of raycasted LiDAR sweeps and show improvements of upto 15 F1 points. For downstream motion planners, where emergent occupancy can be directly used to guide non-driveable regions, this representation relatively reduces the number of collisions with objects by up to 17% as compared to freespace-centric motion planners.

</details>

### ST-P3: End-to-End Vision-Based Autonomous Driving via Spatial-Temporal Feature Learning.
- **链接**: [arXiv:2207.07601](https://arxiv.org/abs/2207.07601) · 📚 被引 258
- **作者**: Shengchao Hu, Li Chen, Penghao Wu, Hongyang Li, Junchi Yan, Dacheng Tao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many existing autonomous driving paradigms involve a multi-stage discrete pipeline of tasks. To better predict the control signals and enhance user safety, an end-to-end approach that benefits from joint spatial-temporal feature learning is desirable. While there are some pioneering works on LiDAR-based input or implicit design, in this paper we formulate the problem in an interpretable vision-based setting. In particular, we propose a spatial-temporal feature learning scheme towards a set of more representative features for perception, prediction and planning tasks simultaneously, which is called ST-P3. Specifically, an egocentric-aligned accumulation technique is proposed to preserve geometry information in 3D space before the bird's eye view transformation for perception; a dual pathway modeling is devised to take past motion variations into account for future prediction; a temporal-based refinement unit is introduced to compensate for recognizing vision-based elements for planning. To the best of our knowledge, we are the first to systematically investigate each part of an interpretable end-to-end vision-based autonomous driving system. We benchmark our approach against previous state-of-the-arts on both open-loop nuScenes dataset as well as closed-loop CARLA simulation. The results show the effectiveness of our method. Source code, model and protocol details are made publicly available at https://github.com/OpenPerceptionX/ST-P3.

</details>

### InAction: Interpretable Action Decision Making for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_22) · 📚 被引 32
- **作者**: Taotao Jing, Haifeng Xia, Renran Tian, Haoran Ding, Xiao Luo, Joshua E. Domeyer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

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

### PreTraM: Self-supervised Pre-training via Connecting Trajectory and Map.
- **链接**: [arXiv:2204.10435](https://arxiv.org/abs/2204.10435)
- **作者**: Chenfeng Xu, Tian Li, Chen Tang, Lingfeng Sun, Kurt Keutzer, Masayoshi Tomizuka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has recently achieved significant progress in trajectory forecasting. However, the scarcity of trajectory data inhibits the data-hungry deep-learning models from learning good representations. While mature representation learning methods exist in computer vision and natural language processing, these pre-training methods require large-scale data. It is hard to replicate these approaches in trajectory forecasting due to the lack of adequate trajectory data (e.g., 34K samples in the nuScenes dataset). To work around the scarcity of trajectory data, we resort to another data modality closely related to trajectories-HD-maps, which is abundantly provided in existing datasets. In this paper, we propose PreTraM, a self-supervised pre-training scheme via connecting trajectories and maps for trajectory forecasting. Specifically, PreTraM consists of two parts: 1) Trajectory-Map Contrastive Learning, where we project trajectories and maps to a shared embedding space with cross-modal contrastive learning, and 2) Map Contrastive Learning, where we enhance map representation with contrastive learning on large quantities of HD-maps. On top of popular baselines such as AgentFormer and Trajectron++, PreTraM boosts their performance by 5.5% and 6.9% relatively in FDE-10 on the challenging nuScenes dataset. We show that PreTraM improves data efficiency and scales well with model size.

</details>

### Action-Based Contrastive Learning for Trajectory Prediction.
- **链接**: [arXiv:2207.08664](https://arxiv.org/abs/2207.08664)
- **作者**: Marah Halawa, Olaf Hellwich, Pia Bideau
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Trajectory prediction is an essential task for successful human robot interaction, such as in autonomous driving. In this work, we address the problem of predicting future pedestrian trajectories in a first person view setting with a moving camera. To that end, we propose a novel action-based contrastive learning loss, that utilizes pedestrian action information to improve the learned trajectory embeddings. The fundamental idea behind this new loss is that trajectories of pedestrians performing the same action should be closer to each other in the feature space than the trajectories of pedestrians with significantly different actions. In other words, we argue that behavioral information about pedestrian action influences their future trajectory. Furthermore, we introduce a novel sampling strategy for trajectories that is able to effectively increase negative and positive contrastive samples. Additional synthetic trajectory samples are generated using a trained Conditional Variational Autoencoder (CVAE), which is at the core of several models developed for trajectory prediction. Results show that our proposed contrastive framework employs contextual information about pedestrian behavior, i.e. action, effectively, and it learns a better trajectory representation. Thus, integrating the proposed contrastive framework within a trajectory prediction model improves its results and outperforms state-of-the-art methods on three trajectory prediction benchmarks [31, 32, 26].

</details>

## 跨领域论文（完整笔记在其他领域）

- BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. → [3d-detection](../3d-detection/Guideline%202022.md)
- V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. → [3d-detection](../3d-detection/Guideline%202022.md)
- MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone. → [3d-detection](../3d-detection/Guideline%202022.md)
- Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. → [3d-detection](../3d-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- PETR: Position Embedding Transformation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Lidar Point Cloud Guided Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rethinking IoU-based Optimization for Single-stage 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- PillarNet: Real-Time and High-Performance Pillar-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph. → [3d-detection](../3d-detection/Guideline%202022.md)
- ProposalContrast: Unsupervised Pre-training for LiDAR-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Point Cloud Compression with Sibling Context and Surface Priors. → [3d-detection](../3d-detection/Guideline%202022.md)
- Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches. → [3d-detection](../3d-detection/Guideline%202022.md)
- PolarMOT: How Far Can Geometric Relations Take us in 3D Multi-object Tracking? → [3d-detection](../3d-detection/Guideline%202022.md)
- Motion Inspired Unsupervised Perception and Prediction in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
