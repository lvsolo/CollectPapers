# Tracking — 2024 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### JDT3D: Addressing the Gaps in LiDAR-Based Tracking-by-Attention.
- **链接**: [arXiv:2407.04926](https://arxiv.org/abs/2407.04926) · [代码](https://github.com/TRAILab/JDT3D) · 📚 被引 4
- **作者**: Brian Cheong, Jiachen Zhou, Steven Lake Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tracking-by-detection (TBD) methods achieve state-of-the-art performance on 3D tracking benchmarks for autonomous driving. On the other hand, tracking-by-attention (TBA) methods have the potential to outperform TBD methods, particularly for long occlusions and challenging detection settings. This work investigates why TBA methods continue to lag in performance behind TBD methods using a LiDAR-based joint detector and tracker called JDT3D. Based on this analysis, we propose two generalizable methods to bridge the gap between TBD and TBA methods: track sampling augmentation and confidence-based query propagation. JDT3D is trained and evaluated on the nuScenes dataset, achieving 0.574 on the AMOTA metric on the nuScenes test set, outperforming all existing LiDAR-based TBA approaches by over 6%. Based on our results, we further discuss some potential challenges with the existing TBA model formulation to explain the continued gap in performance with TBD methods. The implementation of JDT3D can be found at the following link: https://github.com/TRAILab/JDT3D.

</details>

### VETRA: A Dataset for Vehicle Tracking in Aerial Imagery - New Challenges for Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73013-9_4) · 📚 被引 6
- **作者**: Jens Hellekes, Manuel Muehlhaus, Reza Bahmanyar, Seyed Majid Azimi, Franz Kurz
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Beyond MOT: Semantic Multi-object Tracking.
- **链接**: [arXiv:2403.05021](https://arxiv.org/abs/2403.05021) · [代码](https://github.com/Nathan-Li123/SMOTer)
- **作者**: Yunhao Li, Qin Li, Hao Wang, Xue Ma, Jiali Yao, Shaohua Dong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current multi-object tracking (MOT) aims to predict trajectories of targets (i.e., ''where'') in videos. Yet, knowing merely ''where'' is insufficient in many crucial applications. In comparison, semantic understanding such as fine-grained behaviors, interactions, and overall summarized captions (i.e., ''what'') from videos, associated with ''where'', is highly-desired for comprehensive video analysis. Thus motivated, we introduce Semantic Multi-Object Tracking (SMOT), that aims to estimate object trajectories and meanwhile understand semantic details of associated trajectories including instance captions, instance interactions, and overall video captions, integrating ''where'' and ''what'' for tracking. In order to foster the exploration of SMOT, we propose BenSMOT, a large-scale Benchmark for Semantic MOT. Specifically, BenSMOT comprises 3,292 videos with 151K frames, covering various scenarios for semantic tracking of humans. BenSMOT provides annotations for the trajectories of targets, along with associated instance captions in natural language, instance interactions, and overall caption for each video sequence. To our best knowledge, BenSMOT is the first publicly available benchmark for SMOT. Besides, to encourage future research, we present a novel tracker named SMOTer, which is specially designed and end-to-end trained for SMOT, showing promising performance. By releasing BenSMOT, we expect to go beyond conventional MOT by predicting ''where'' and ''what'' for SMOT, opening up a new direction in tracking for video understanding. We will release BenSMOT and SMOTer at https://github.com/Nathan-Li123/SMOTer.

</details>

### PapMOT: Exploring Adversarial Patch Attack Against Multiple Object Tracking.
- **链接**: [arXiv:2504.09361](https://arxiv.org/abs/2504.09361) · 📚 被引 4
- **作者**: Jiahuan Long, Tingsong Jiang, Wen Yao, Shuai Jia, Weijia Zhang, Weien Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tracking multiple objects in a continuous video stream is crucial for many computer vision tasks. It involves detecting and associating objects with their respective identities across successive frames. Despite significant progress made in multiple object tracking (MOT), recent studies have revealed the vulnerability of existing MOT methods to adversarial attacks. Nevertheless, all of these attacks belong to digital attacks that inject pixel-level noise into input images, and are therefore ineffective in physical scenarios. To fill this gap, we propose PapMOT, which can generate physical adversarial patches against MOT for both digital and physical scenarios. Besides attacking the detection mechanism, PapMOT also optimizes a printable patch that can be detected as new targets to mislead the identity association process. Moreover, we introduce a patch enhancement strategy to further degrade the temporal consistency of tracking results across video frames, resulting in more aggressive attacks. We further develop new evaluation metrics to assess the robustness of MOT against such attacks. Extensive evaluations on multiple datasets demonstrate that our PapMOT can successfully attack various architectures of MOT trackers in digital scenarios. We also validate the effectiveness of PapMOT for physical attacks by deploying printed adversarial patches in the real world.

</details>

### Lost and Found: Overcoming Detector Failures in Online Multi-object Tracking.
- **链接**: [arXiv:2407.10151](https://arxiv.org/abs/2407.10151) · [代码](https://github.com/lorenzovaquero/BUSCA) · 📚 被引 20
- **作者**: Lorenzo Vaquero, Yihong Xu, Xavier Alameda-Pineda, Víctor M. Brea, Manuel Mucientes
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking (MOT) endeavors to precisely estimate the positions and identities of multiple objects over time. The prevailing approach, tracking-by-detection (TbD), first detects objects and then links detections, resulting in a simple yet effective method. However, contemporary detectors may occasionally miss some objects in certain frames, causing trackers to cease tracking prematurely. To tackle this issue, we propose BUSCA, meaning `to search', a versatile framework compatible with any online TbD system, enhancing its ability to persistently track those objects missed by the detector, primarily due to occlusions. Remarkably, this is accomplished without modifying past tracking results or accessing future frames, i.e., in a fully online manner. BUSCA generates proposals based on neighboring tracks, motion, and learned tokens. Utilizing a decision Transformer that integrates multimodal visual and spatiotemporal information, it addresses the object-proposal association as a multi-choice question-answering task. BUSCA is trained independently of the underlying tracker, solely on synthetic data, without requiring fine-tuning. Through BUSCA, we showcase consistent performance enhancements across five different trackers and establish a new state-of-the-art baseline across three different benchmarks. Code available at: https://github.com/lorenzovaquero/BUSCA.

</details>

### Boosting 3D Single Object Tracking with 2D Matching Distillation and 3D Pre-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73254-6_16) · 📚 被引 12
- **作者**: Qiangqiang Wu, Yan Xia, Jia Wan, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

## 跨领域论文（完整笔记在其他领域）

- Walker: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
