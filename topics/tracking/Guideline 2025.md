# Tracking — 2025 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### TrackAny3D: Transferring Pretrained 3D Models for Category-Unified 3D Point Cloud Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02623) · 📚 被引 1
- **作者**: Mengmeng Wang, Haonan Wang, Yulong Li, Xiangjie Kong, Jiaxin Du, Guojiang Shen et al.
- **🏷️ 机构**: Zhejiang University of Technology, RMIT University
- **会议**: ICCV 2025

### GRAE-3DMOT: Geometry Relation-Aware Encoder for Online 3D Multi-Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kim_GRAE-3DMOT_Geometry_Relation-Aware_Encoder_for_Online_3D_Multi-Object_Tracking_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Hyunseop Kim, Hyo-Jun Lee, Yonguk Lee, Jinu Lee, Hanul Kim, Yeong Jun Koh
- **🏷️ 机构**: Chungnam National University, Kangwon National University, 42Dot Inc.
- **会议**: CVPR 2025

### Omnidirectional Multi-Object Tracking.
- **链接**: [arXiv:2503.04565](https://arxiv.org/abs/2503.04565)
- **作者**: Kai Luo, Hao Shi, Sheng Wu, Fei Teng, Mengfei Duan, Chang Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present a novel benchmark, GSOT3D, that aims at facilitating development of generic 3D single object tracking (SOT) in the wild. Specifically, GSOT3D offers 620 sequences with 123K frames, and covers a wide selection of 54 object categories. Each sequence is offered with multiple modalities, including the point cloud (PC), RGB image, and depth. This allows GSOT3D to support various 3D tracking tasks, such as single-modal 3D SOT on PC and multi-modal 3D SOT on RGB-PC or RGB-D, and thus greatly broadens research directions for 3D object tracking. To provide highquality per-frame 3D annotations, all sequences are labeled manually with multiple rounds of meticulous inspection and refinement. To our best knowledge, GSOT3D is the largest benchmark dedicated to various generic 3D object tracking tasks. To understand how existing 3D trackers perform and to provide comparisons for future research on GSOT3D, we assess eight representative point cloud-based tracking models. Our evaluation results exhibit that these models heavily degrade on GSOT3D, and more efforts are required for robust and generic 3D object tracking. Besides, to encourage future research, we present a simple yet effective generic 3D tracker, named PROT3D, that localizes the target object via a progressive spatial-temporal network and outperforms all current solutions by a large margin. By releasing GSOT3D, we expect to advance further 3D tracking in future research and applications. Our benchmark and model as well as the evaluation results will be publicly released at our webpage https://github.com/ailovejinx/GSOT3D.

</details>

### MUST: The First Dataset and Unified Framework for Multispectral UAV Single Object Tracking.
- **链接**: [arXiv:2503.17699](https://arxiv.org/abs/2503.17699) · 📚 被引 12
- **作者**: Haolin Qin, Tingfa Xu, Tianhao Li, Zhenxiang Chen, Tao Feng, Jianan Li
- **🏷️ 机构**: Beijing Institute of Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a data capture system and a new dataset, HO-Cap, for 3D reconstruction and pose tracking of hands and objects in videos. The system leverages multiple RGBD cameras and a HoloLens headset for data collection, avoiding the use of expensive 3D scanners or mocap systems. We propose a semi-automatic method for annotating the shape and pose of hands and objects in the collected videos, significantly reducing the annotation time compared to manual labeling. With this system, we captured a video dataset of humans interacting with objects to perform various tasks, including simple pick-and-place actions, handovers between hands, and using objects according to their affordance, which can serve as human demonstrations for research in embodied AI and robot manipulation. Our data capture setup and annotation framework will be available for the community to use in reconstructing 3D shapes of objects and human hands and tracking their poses in videos.

</details>

### Focusing on Tracks for Online Multi-Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shim_Focusing_on_Tracks_for_Online_Multi-Object_Tracking_CVPR_2025_paper.html) · 📚 被引 20
- **作者**: Kyujin Shim, Kangwook Ko, Yujin Yang, Changick Kim
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST)
- **会议**: CVPR 2025

### SPMTrack: Spatio-Temporal Parameter-Efficient Fine-Tuning with Mixture of Experts for Scalable Visual Tracking.
- **链接**: [arXiv:2503.18338](https://arxiv.org/abs/2503.18338) · 📚 被引 13
- **作者**: Wenrui Cai, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,Beijing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most state-of-the-art trackers adopt one-stream paradigm, using a single Vision Transformer for joint feature extraction and relation modeling of template and search region images. However, relation modeling between different image patches exhibits significant variations. For instance, background regions dominated by target-irrelevant information require reduced attention allocation, while foreground, particularly boundary areas, need to be be emphasized. A single model may not effectively handle all kinds of relation modeling simultaneously. In this paper, we propose a novel tracker called SPMTrack based on mixture-of-experts tailored for visual tracking task (TMoE), combining the capability of multiple experts to handle diverse relation modeling more flexibly. Benefiting from TMoE, we extend relation modeling from image pairs to spatio-temporal context, further improving tracking accuracy with minimal increase in model parameters. Moreover, we employ TMoE as a parameter-efficient fine-tuning method, substantially reducing trainable parameters, which enables us to train SPMTrack of varying scales efficiently and preserve the generalization ability of pretrained models to achieve superior performance. We conduct experiments on seven datasets, and experimental results demonstrate that our method significantly outperforms current state-of-the-art trackers. The source code is available at https://github.com/WenRuiCai/SPMTrack.

</details>

### Autoregressive Sequential Pretraining for Visual Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Autoregressive_Sequential_Pretraining_for_Visual_Tracking_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Shiyi Liang, Yifan Bai, Yihong Gong, Xing Wei
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering
- **会议**: CVPR 2025

### Exploring Historical Information for RGBE Visual Tracking with Mamba.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_Exploring_Historical_Information_for_RGBE_Visual_Tracking_with_Mamba_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Chuanyu Sun, Jiqing Zhang, Yang Wang, Huilin Ge, Qianchen Xia, Baocai Yin et al.
- **🏷️ 机构**: Dalian University of Technology,Key Laboratory of Social Computing and Cognitive Intelligence, Dalian Maritime University, Jiangsu University of Science and Technology
- **会议**: CVPR 2025

### GaPT-DAR: Category-level Garments Pose Tracking via Integrated 2D Deformation and 3D Reconstruction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_GaPT-DAR_Category-level_Garments_Pose_Tracking_via_Integrated_2D_Deformation_and_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Li Zhang, Mingliang Xu, Jianan Wang, Qiaojun Yu, Lixin Yang, Yonglu Li et al.
- **🏷️ 机构**: University of Science and Technology of China,Hefei,China, Astribot,Shenzhen,China, Shanghai Jiao Tong University,Shanghai,China
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- All-Day Multi-Camera Multi-Target Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
