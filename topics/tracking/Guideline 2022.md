# Tracking — 2022 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Beyond 3D Siamese Tracking: A Motion-Centric Paradigm for 3D Single Object Tracking in Point Clouds.
- **链接**: [arXiv:2203.01730](https://arxiv.org/abs/2203.01730) · 📚 被引 103
- **作者**: Chaoda Zheng, Xu Yan, Haiming Zhang, Baoyuan Wang, Shenghui Cheng, Shuguang Cui et al.
- **🏷️ 机构**: The Chinese University of Hong Kong (Shenzhen), Xiaobing.AI, Westlake University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > 3D single object tracking (3D SOT) in LiDAR point clouds plays a crucial role in autonomous driving. Current approaches all follow the Siamese paradigm based on appearance matching. However, LiDAR point clouds are usually textureless and incomplete, which hinders effective appearance matching. Besides, previous methods greatly overlook the critical motion clues among targets. In this work, beyond 3D Siamese tracking, we introduce a motion-centric paradigm to handle 3D SOT from a new perspective. Following this paradigm, we propose a matching-free two-stage tracker M^2-Track. At the 1^st-stage, M^2-Track localizes the target within successive frames via motion transformation. Then it refines the target box through motion-assisted shape completion at the 2^nd-stage. Extensive experiments confirm that M^2-Track significantly outperforms previous state-of-the-arts on three large-scale datasets while running at 57FPS (~8%, ~17%, and ~22%) precision gains on KITTI, NuScenes, and Waymo Open Dataset respectively). Further analysis verifies each component's effectiveness and shows the motion-centric paradigm's promising potential when combined with appearance matching.

### PoseTrack21: A Dataset for Person Search, Multi-Object Tracking and Multi-Person Pose Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02029) · 📚 被引 49
- **作者**: Andreas Doering, Di Chen, Shanshan Zhang, Bernt Schiele, Juergen Gall
- **🏷️ 机构**: University of Bonn, Nanjing University of Science and Technology, MPI for Informatics
- **会议**: CVPR 2022

### Learning of Global Objective for Network Flow in Multi-Object Tracking.
- **链接**: [arXiv:2203.16210](https://arxiv.org/abs/2203.16210) · 📚 被引 24
- **作者**: Shuai Li, Yu Kong, Hamid Rezatofighi
- **🏷️ 机构**: Rochester Institute of Technology, Monash University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > This paper concerns the problem of multi-object tracking based on the min-cost flow (MCF) formulation, which is conventionally studied as an instance of linear program. Given its computationally tractable inference, the success of MCF tracking largely relies on the learned cost function of underlying linear program. Most previous studies focus on learning the cost function by only taking into account two frames during training, therefore the learned cost function is sub-optimal for MCF where a multi-frame data association must be considered during inference. In order to address this problem, in this paper we propose a novel differentiable framework that ties training and inference together during learning by solving a bi-level optimization problem, where the lower-level solves a linear program and the upper-level contains a loss function that incorporates global tracking result. By back-propagating the loss through differentiable layers via gradient descent, the globally parameterized cost function is explicitly learned and regularized. With this approach, we are able to learn a better objective for global MCF tracking. As a result, we achieve competitive performances compared to the current state-of-the-art methods on the popular multi-object tracking benchmarks such as MOT16, MOT17 and MOT20.

### MeMOT: Multi-Object Tracking with Memory.
- **链接**: [arXiv:2203.16761](https://arxiv.org/abs/2203.16761) · 📚 被引 231
- **作者**: Jiarui Cai, Mingze Xu, Wei Li, Yuanjun Xiong, Wei Xia, Zhuowen Tu et al.
- **🏷️ 机构**: University of Washington, AWS AI Labs
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We propose an online tracking algorithm that performs the object detection and data association under a common framework, capable of linking objects after a long time span. This is realized by preserving a large spatio-temporal memory to store the identity embeddings of the tracked objects, and by adaptively referencing and aggregating useful information from the memory as needed. Our model, called MeMOT, consists of three main modules that are all Transformer-based: 1) Hypothesis Generation that produce object proposals in the current video frame; 2) Memory Encoding that extracts the core information from the memory for each tracked object; and 3) Memory Decoding that solves the object detection and data association tasks simultaneously for multi-object tracking. When evaluated on widely adopted MOT benchmark datasets, MeMOT observes very competitive performance.

### Multi-Object Tracking Meets Moving UAV.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00867) · 📚 被引 119
- **作者**: Shuai Liu, Xin Li, Huchuan Lu, You He
- **🏷️ 机构**: Dalian University of Technology,Dalian, Peng Cheng Laboratory,Shenzhen, Naval Aeronautical University,Yantai,China
- **会议**: CVPR 2022

### TrackFormer: Multi-Object Tracking with Transformers.
- **链接**: [arXiv:2101.02702](https://arxiv.org/abs/2101.02702) · [代码](https://github.com/timmeinhardt/trackformer) · 📚 被引 875
- **作者**: Tim Meinhardt, Alexander Kirillov, Laura Leal-Taixé, Christoph Feichtenhofer
- **🏷️ 机构**: Technical University of Munich, Facebook AI Research (FAIR)
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > The challenging task of multi-object tracking (MOT) requires simultaneous reasoning about track initialization, identity, and spatio-temporal trajectories. We formulate this task as a frame-to-frame set prediction problem and introduce TrackFormer, an end-to-end trainable MOT approach based on an encoder-decoder Transformer architecture. Our model achieves data association between frames via attention by evolving a set of track predictions through a video sequence. The Transformer decoder initializes new tracks from static object queries and autoregressively follows existing tracks in space and time with the conceptually new and identity preserving track queries. Both query types benefit from self- and encoder-decoder attention on global frame-level features, thereby omitting any additional graph optimization or modeling of motion and/or appearance. TrackFormer introduces a new tracking-by-attention paradigm and while simple in its design is able to achieve state-of-the-art performance on the task of multi-object tracking (MOT17 and MOT20) and segmentation (MOTS20). The code is available at https://github.com/timmeinhardt/trackformer .

### DanceTrack: Multi-Object Tracking in Uniform Appearance and Diverse Motion.
- **链接**: [arXiv:2111.14690](https://arxiv.org/abs/2111.14690) · 📚 被引 338
- **作者**: Peize Sun, Jinkun Cao, Yi Jiang, Zehuan Yuan, Song Bai, Kris Kitani et al.
- **🏷️ 机构**: The University of Hong Kong, Carnegie Mellon University, ByteDance Inc
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > A typical pipeline for multi-object tracking (MOT) is to use a detector for object localization, and following re-identification (re-ID) for object association. This pipeline is partially motivated by recent progress in both object detection and re-ID, and partially motivated by biases in existing tracking datasets, where most objects tend to have distinguishing appearance and re-ID models are sufficient for establishing associations. In response to such bias, we would like to re-emphasize that methods for multi-object tracking should also work when object appearance is not sufficiently discriminative. To this end, we propose a large-scale dataset for multi-human tracking, where humans have similar appearance, diverse motion and extreme articulation. As the dataset contains mostly group dancing videos, we name it "DanceTrack". We expect DanceTrack to provide a better platform to develop more MOT algorithms that rely less on visual discrimination and depend more on motion analysis. We benchmark several state-of-the-art trackers on our dataset and observe a significant performance drop on DanceTrack when compared against existing benchmarks. The dataset, project code and competition server are released at: \url{https://github.com/DanceTrack}.

### Iterative Corresponding Geometry: Fusing Region and Depth for Highly Efficient 3D Tracking of Textureless Objects.
- **链接**: [arXiv:2203.05334](https://arxiv.org/abs/2203.05334) · 📚 被引 49
- **作者**: Manuel Stoiber, Martin Sundermeyer, Rudolph Triebel
- **🏷️ 机构**: German Aerospace Center (DLR)
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Tracking objects in 3D space and predicting their 6DoF pose is an essential task in computer vision. State-of-the-art approaches often rely on object texture to tackle this problem. However, while they achieve impressive results, many objects do not contain sufficient texture, violating the main underlying assumption. In the following, we thus propose ICG, a novel probabilistic tracker that fuses region and depth information and only requires the object geometry. Our method deploys correspondence lines and points to iteratively refine the pose. We also implement robust occlusion handling to improve performance in real-world settings. Experiments on the YCB-Video, OPT, and Choi datasets demonstrate that, even for textured objects, our approach outperforms the current state of the art with respect to accuracy and robustness. At the same time, ICG shows fast convergence and outstanding efficiency, requiring only 1.3 ms per frame on a single CPU core. Finally, we analyze the influence of individual components and discuss our performance compared to deep learning-based methods. The source code of our tracker is publicly available.

### Ranking-Based Siamese Visual Tracking.
- **链接**: [arXiv:2205.11761](https://arxiv.org/abs/2205.11761) · [代码](https://github.com/sansanfree/RBO) · 📚 被引 87
- **作者**: Feng Tang, Qiang Ling
- **🏷️ 机构**: University of Science and Technology of China,Department of Automation,China
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Current Siamese-based trackers mainly formulate the visual tracking into two independent subtasks, including classification and localization. They learn the classification subnetwork by processing each sample separately and neglect the relationship among positive and negative samples. Moreover, such tracking paradigm takes only the classification confidence of proposals for the final prediction, which may yield the misalignment between classification and localization. To resolve these issues, this paper proposes a ranking-based optimization algorithm to explore the relationship among different proposals. To this end, we introduce two ranking losses, including the classification one and the IoU-guided one, as optimization constraints. The classification ranking loss can ensure that positive samples rank higher than hard negative ones, i.e., distractors, so that the trackers can select the foreground samples successfully without being fooled by the distractors. The IoU-guided ranking loss aims to align classification confidence scores with the Intersection over Union(IoU) of the corresponding localization prediction for positive samples, enabling the well-localized prediction to be represented by high classification confidence. Specifically, the proposed two ranking losses are compatible with most Siamese trackers and incur no additional computation for inference. Extensive experiments on seven tracking benchmarks, including OTB100, UAV123, TC128, VOT2016, NFS30, GOT-10k and LaSOT, demonstrate the effectiveness of the proposed ranking-based optimization algorithm. The code and raw results are available at https://github.com/sansanfree/RBO.

### Spiking Transformers for Event-based Single Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00860) · 📚 被引 174
- **作者**: Jiqing Zhang, Bo Dong, Haiwei Zhang, Jianchuan Ding, Felix Heide, Baocai Yin et al.
- **🏷️ 机构**: Dalian University of Technology, Princeton University
- **会议**: CVPR 2022

## 跨领域论文（完整笔记在其他领域）

- Towards Discriminative Representation: Multi-view Trajectory Contrastive Learning for Online Multi-object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- LMGP: Lifted Multicut Meets Geometry Projections for Multi-Camera Multi-Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
