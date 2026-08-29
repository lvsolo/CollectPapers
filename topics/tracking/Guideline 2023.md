# Tracking — 2023 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CXTrack: Improving 3D Point Cloud Tracking with Contextual Information.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00111) · 📚 被引 39
- **作者**: Tian-Xing Xu, Yuan-Chen Guo, Yu-Kun Lai, Song-Hai Zhang
- **🏷️ 机构**: Tsinghua University,China, Cardiff University,United Kingdom
- **会议**: CVPR 2023

### MOTRv2: Bootstrapping End-to-End Multi-Object Tracking by Pretrained Object Detectors.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02112) · 📚 被引 246
- **作者**: Yuang Zhang, Tiancai Wang, Xiangyu Zhang
- **🏷️ 机构**: Shanghai Jiao Tong University, MEGVII Technology
- **会议**: CVPR 2023

### Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking.
- **链接**: [arXiv:2203.14360](https://arxiv.org/abs/2203.14360) · [代码](https://github.com/noahcao/OC_SORT) · 📚 被引 910
- **作者**: Jinkun Cao, Jiangmiao Pang, Xinshuo Weng, Rawal Khirodkar, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University, Shanghai AI Laboratory, Nvidia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Kalman filter (KF) based methods for multi-object tracking (MOT) make an assumption that objects move linearly. While this assumption is acceptable for very short periods of occlusion, linear estimates of motion for prolonged time can be highly inaccurate. Moreover, when there is no measurement available to update Kalman filter parameters, the standard convention is to trust the priori state estimations for posteriori update. This leads to the accumulation of errors during a period of occlusion. The error causes significant motion direction variance in practice. In this work, we show that a basic Kalman filter can still obtain state-of-the-art tracking performance if proper care is taken to fix the noise accumulated during occlusion. Instead of relying only on the linear state estimate (i.e., estimation-centric approach), we use object observations (i.e., the measurements by object detector) to compute a virtual trajectory over the occlusion period to fix the error accumulation of filter parameters during the occlusion period. This allows more time steps to correct errors accumulated during occlusion. We name our method Observation-Centric SORT (OC-SORT). It remains Simple, Online, and Real-Time but improves robustness during occlusion and non-linear motion. Given off-the-shelf detections as input, OC-SORT runs at 700+ FPS on a single CPU. It achieves state-of-the-art on multiple datasets, including MOT17, MOT20, KITTI, head tracking, and especially DanceTrack where the object motion is highly non-linear. The code and models are available at \url{https://github.com/noahcao/OC_SORT}.

</details>

### MotionTrack: Learning Robust Short-Term and Long-Term Motions for Multi-Object Tracking.
- **链接**: [arXiv:2303.10404](https://arxiv.org/abs/2303.10404) · 📚 被引 167
- **作者**: Zheng Qin, Sanping Zhou, Le Wang, Jinghai Duan, Gang Hua, Wei Tang
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, School of Software Engineering, Xi&#x0027;an Jiaotong University, Wormpex AI Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The main challenge of Multi-Object Tracking~(MOT) lies in maintaining a continuous trajectory for each target. Existing methods often learn reliable motion patterns to match the same target between adjacent frames and discriminative appearance features to re-identify the lost targets after a long period. However, the reliability of motion prediction and the discriminability of appearances can be easily hurt by dense crowds and extreme occlusions in the tracking process. In this paper, we propose a simple yet effective multi-object tracker, i.e., MotionTrack, which learns robust short-term and long-term motions in a unified framework to associate trajectories from a short to long range. For dense crowds, we design a novel Interaction Module to learn interaction-aware motions from short-term trajectories, which can estimate the complex movement of each target. For extreme occlusions, we build a novel Refind Module to learn reliable long-term motions from the target's history trajectory, which can link the interrupted trajectory with its corresponding detection. Our Interaction Module and Refind Module are embedded in the well-known tracking-by-detection paradigm, which can work in tandem to maintain superior performance. Extensive experimental results on MOT17 and MOT20 datasets demonstrate the superiority of our approach in challenging scenarios, and it achieves state-of-the-art performances at various MOT metrics.

</details>

### Focus On Details: Online Multi-Object Tracking with Diverse Fine-Grained Representation.
- **链接**: [arXiv:2302.14589](https://arxiv.org/abs/2302.14589) · 📚 被引 85
- **作者**: Hao Ren, Shoudong Han, Huilin Ding, Ziwen Zhang, Hongwei Wang, Faquan Wang
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,National Key Laboratory of Science and Technology on Multispectral Information Processing
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Discriminative representation is essential to keep a unique identifier for each target in Multiple object tracking (MOT). Some recent MOT methods extract features of the bounding box region or the center point as identity embeddings. However, when targets are occluded, these coarse-grained global representations become unreliable. To this end, we propose exploring diverse fine-grained representation, which describes appearance comprehensively from global and local perspectives. This fine-grained representation requires high feature resolution and precise semantic information. To effectively alleviate the semantic misalignment caused by indiscriminate contextual information aggregation, Flow Alignment FPN (FAFPN) is proposed for multi-scale feature alignment aggregation. It generates semantic flow among feature maps from different resolutions to transform their pixel positions. Furthermore, we present a Multi-head Part Mask Generator (MPMG) to extract fine-grained representation based on the aligned feature maps. Multiple parallel branches of MPMG allow it to focus on different parts of targets to generate local masks without label supervision. The diverse details in target masks facilitate fine-grained representation. Eventually, benefiting from a Shuffle-Group Sampling (SGS) training strategy with positive and negative samples balanced, we achieve state-of-the-art performance on MOT17 and MOT20 test sets. Even on DanceTrack, where the appearance of targets is extremely similar, our method significantly outperforms ByteTrack by 5.0% on HOTA and 5.6% on IDF1. Extensive experiments have proved that diverse fine-grained representation makes Re-ID great again in MOT.

</details>

### Referring Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01406)
- **作者**: Dongming Wu, Wencheng Han, Tiancai Wang, Xingping Dong, Xiangyu Zhang, Jianbing Shen
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2023

### UTM: A Unified Multiple Object Tracking Model with Identity-Aware Feature Enhancement.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02095) · 📚 被引 87
- **作者**: Sisi You, Hantao Yao, Bing-Kun Bao, Changsheng Xu
- **🏷️ 机构**: Nanjing University of Posts and Telecommunications, Institute of Automation, Chinese Academy of Sciences (CASIA),State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2023

### 3D-POP - An Automated Annotation Approach to Facilitate Markerless 2D-3D Tracking of Freely Moving Birds with Marker-Based Motion Capture.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02038) · 📚 被引 27
- **作者**: Hemal Naik, Alex Hoi Hang Chan, Junran Yang, Mathilde Delacoux, Iain D. Couzin, Fumihiro Kano et al.
- **🏷️ 机构**: Max Planck Institute of Animal Behavior,Dept. of Collective Behavior and Dept. of Ecology of Animal Societies, University of Konstanz,Dept. of Biology
- **会议**: CVPR 2023

### Autoregressive Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00935)
- **作者**: Xing Wei, Yifan Bai, Yongchao Zheng, Dahu Shi, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### GarmentTracking: Category-Level Garment Pose Tracking.
- **链接**: [arXiv:2303.13913](https://arxiv.org/abs/2303.13913) · 📚 被引 11
- **作者**: Han Xue, Wenqiang Xu, Jieyi Zhang, Tutian Tang, Yutong Li, Wenxin Du et al.
- **🏷️ 机构**: Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Cornell University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Garments are important to humans. A visual system that can estimate and track the complete garment pose can be useful for many downstream tasks and real-world applications. In this work, we present a complete package to address the category-level garment pose tracking task: (1) A recording system VR-Garment, with which users can manipulate virtual garment models in simulation through a VR interface. (2) A large-scale dataset VR-Folding, with complex garment pose configurations in manipulation like flattening and folding. (3) An end-to-end online tracking framework GarmentTracking, which predicts complete garment pose both in canonical space and task space given a point cloud sequence. Extensive experiments demonstrate that the proposed GarmentTracking achieves great performance even when the garment has large non-rigid deformation. It outperforms the baseline approach on both speed and accuracy. We hope our proposed solution can serve as a platform for future research. Codes and datasets are available in https://garment-tracking.robotflow.ai.

</details>

## 跨领域论文（完整笔记在其他领域）

- Standing Between Past and Future: Spatio-Temporal Modeling for Multi-Camera 3D Multi-Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- OVTrack: Open-Vocabulary Multiple Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202023.md)
