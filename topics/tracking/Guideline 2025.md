# Tracking — 2025 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multiple Object Tracking as ID Prediction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_Multiple_Object_Tracking_as_ID_Prediction_CVPR_2025_paper.html) · 📚 被引 52
- **作者**: Ruopeng Gao, Ji Qi, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology, China Mobile (Suzhou) Software Technology Co., Ltd.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Omnidirectional Multi-Object Tracking.
- **链接**: [arXiv:2503.04565](https://arxiv.org/abs/2503.04565)
- **作者**: Kai Luo, Hao Shi, Sheng Wu, Fei Teng, Mengfei Duan, Chang Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Panoramic imagery, with its 360° field of view, offers comprehensive information to support Multi-Object Tracking (MOT) in capturing spatial and temporal relationships of surrounding objects. However, most MOT algorithms are tailored for pinhole images with limited views, impairing their effectiveness in panoramic settings. Additionally, panoramic image distortions, such as resolution loss, geometric deformation, and uneven lighting, hinder direct adaptation of existing MOT methods, leading to significant performance degradation. To address these challenges, we propose OmniTrack, an omnidirectional MOT framework that incorporates Tracklet Management to introduce temporal cues, FlexiTrack Instances for object localization and association, and the CircularStatE Module to alleviate image and geometric distortions. This integration enables tracking in panoramic field-of-view scenarios, even under rapid sensor motion. To mitigate the lack of panoramic MOT datasets, we introduce the QuadTrack dataset--a comprehensive panoramic dataset collected by a quadruped robot, featuring diverse challenges such as panoramic fields of view, intense motion, and complex environments. Extensive experiments on the public JRDB dataset and the newly introduced QuadTrack benchmark demonstrate the state-of-the-art performance of the proposed framework. OmniTrack achieves a HOTA score of 26.92% on JRDB, representing an improvement of 3.43%, and further achieves 23.45% on QuadTrack, surpassing the baseline by 6.81%. The established dataset and source code are available at https://github.com/xifen523/OmniTrack.

</details>

### MUST: The First Dataset and Unified Framework for Multispectral UAV Single Object Tracking.
- **链接**: [arXiv:2503.17699](https://arxiv.org/abs/2503.17699) · 📚 被引 12
- **作者**: Haolin Qin, Tingfa Xu, Tianhao Li, Zhenxiang Chen, Tao Feng, Jianan Li
- **🏷️ 机构**: Beijing Institute of Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> UAV tracking faces significant challenges in real-world scenarios, such as small-size targets and occlusions, which limit the performance of RGB-based trackers. Multispectral images (MSI), which capture additional spectral information, offer a promising solution to these challenges. However, progress in this field has been hindered by the lack of relevant datasets. To address this gap, we introduce the first large-scale Multispectral UAV Single Object Tracking dataset (MUST), which includes 250 video sequences spanning diverse environments and challenges, providing a comprehensive data foundation for multispectral UAV tracking. We also propose a novel tracking framework, UNTrack, which encodes unified spectral, spatial, and temporal features from spectrum prompts, initial templates, and sequential searches. UNTrack employs an asymmetric transformer with a spectral background eliminate mechanism for optimal relationship modeling and an encoder that continuously updates the spectrum prompt to refine tracking, improving both accuracy and efficiency. Extensive experiments show that our proposed UNTrack outperforms state-of-the-art UAV trackers. We believe our dataset and framework will drive future research in this area. The dataset is available on https://github.com/q2479036243/MUST-Multispectral-UAV-Single-Object-Tracking.

</details>

> We seek to extract a temporally consistent 6D pose trajectory of a manipulated object from an Internet instructional video. This is a challenging set-up for current 6D pose estimation methods due to uncontrolled capturing conditions, subtle but dynamic object motions, and the fact that the exact mesh of the manipulated object is not known. To address these challenges, we present the following contributions. First, we develop a new method that estimates the 6D pose of any object in the input image without prior knowledge of the object itself. The method proceeds by (i) retrieving a CAD model similar to the depicted object from a large-scale model database, (ii) 6D aligning the retrieved CAD model with the input image, and (iii) grounding the absolute scale of the object with respect to the scene. Second, we extract smooth 6D object trajectories from Internet videos by carefully tracking the detected objects across video frames. The extracted object trajectories are then retargeted via trajectory optimization into the configuration space of a robotic manipulator. Third, we thoroughly evaluate and ablate our 6D pose estimation method on YCB-V and HOPE-Video datasets as well as a new dataset of instructional videos manually annotated with approximate 6D object trajectories. We demonstrate significant improvements over existing state-of-the-art RGB 6D pose estimation methods. Finally, we show that the 6D object motion estimated from Internet videos can be transferred to a 7-axis robotic manipulator both in a virtual simulator as well as in a real world set-up. We also successfully apply our method to egocentric videos taken from the EPIC-KITCHENS dataset, demonstrating potential for Embodied AI applications.

</details>

### Samba: Synchronized Set-of-Sequences Modeling for Multiple Object Tracking.
- **链接**: [arXiv:2410.01806](https://arxiv.org/abs/2410.01806)
- **作者**: Mattia Segù, Luigi Piccinelli, Siyuan Li, Yung-Hsu Yang, Luc Van Gool, Bernt Schiele
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multiple object tracking in complex scenarios - such as coordinated dance performances, team sports, or dynamic animal groups - presents unique challenges. In these settings, objects frequently move in coordinated patterns, occlude each other, and exhibit long-term dependencies in their trajectories. However, it remains a key open research question on how to model long-range dependencies within tracklets, interdependencies among tracklets, and the associated temporal occlusions. To this end, we introduce Samba, a novel linear-time set-of-sequences model designed to jointly process multiple tracklets by synchronizing the multiple selective state-spaces used to model each tracklet. Samba autoregressively predicts the future track query for each sequence while maintaining synchronized long-term memory representations across tracklets. By integrating Samba into a tracking-by-propagation framework, we propose SambaMOTR, the first tracker effectively addressing the aforementioned issues, including long-range dependencies, tracklet interdependencies, and temporal occlusions. Additionally, we introduce an effective technique for dealing with uncertain observations (MaskObs) and an efficient training recipe to scale SambaMOTR to longer sequences. By modeling long-range dependencies and interactions among tracked objects, SambaMOTR implicitly learns to track objects accurately through occlusions without any hand-crafted heuristics. Our approach significantly surpasses prior state-of-the-art on the DanceTrack, BFT, and SportsMOT datasets.

</details>

### CO-MOT: Boosting End-to-end Transformer-based Multi-Object Tracking via Coopetition Label Assignment and Shadow Sets.
- **链接**: [出版页](https://openreview.net/forum?id=0ov0dMQ3mN)
- **作者**: Feng Yan, Weixin Luo, Yujie Zhong, Yiyang Gan, Lin Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

## 跨领域论文（完整笔记在其他领域）

- VOVTrack: Exploring the Potentiality in Raw Videos for Open-Vocabulary Multi-Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202025.md)
