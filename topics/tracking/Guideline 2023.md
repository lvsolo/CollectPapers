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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00934) · 📚 被引 910
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

> 3D single object tracking has been a crucial problem for decades with numerous applications such as autonomous driving. Despite its wide-ranging use, this task remains challenging due to the significant appearance variation caused by occlusion and size differences among tracked targets. To address these issues, we present MBPTrack, which adopts a Memory mechanism to utilize past information and formulates localization in a coarse-to-fine scheme using Box Priors given in the first frame. Specifically, past frames with targetness masks serve as an external memory, and a transformer-based module propagates tracked target cues from the memory to the current frame. To precisely localize objects of all sizes, MBPTrack first predicts the target center via Hough voting. By leveraging box priors given in the first frame, we adaptively sample reference points around the target center that roughly cover the target of different sizes. Then, we obtain dense feature maps by aggregating point features into the reference points, where localization can be performed more effectively. Extensive experiments demonstrate that MBPTrack achieves state-of-the-art performance on KITTI, nuScenes and Waymo Open Dataset, while running at 50 FPS on a single RTX3090 GPU.

</details>

### Exploring Lightweight Hierarchical Vision Transformers for Efficient Visual Tracking.
- **链接**: [arXiv:2308.06904](https://arxiv.org/abs/2308.06904) · 📚 被引 127
- **作者**: Ben Kang, Xin Chen, Dong Wang, Houwen Peng, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,School of Information and Communication Engineering, Microsoft Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based visual trackers have demonstrated significant progress owing to their superior modeling capabilities. However, existing trackers are hampered by low speed, limiting their applicability on devices with limited computational power. To alleviate this problem, we propose HiT, a new family of efficient tracking models that can run at high speed on different devices while retaining high performance. The central idea of HiT is the Bridge Module, which bridges the gap between modern lightweight transformers and the tracking framework. The Bridge Module incorporates the high-level information of deep features into the shallow large-resolution features. In this way, it produces better features for the tracking head. We also propose a novel dual-image position encoding technique that simultaneously encodes the position information of both the search region and template images. The HiT model achieves promising speed with competitive performance. For instance, it runs at 61 frames per second (fps) on the Nvidia Jetson AGX edge device. Furthermore, HiT attains 64.6% AUC on the LaSOT benchmark, surpassing all previous efficient trackers.

</details>

### Tracking without Label: Unsupervised Multiple Object Tracking via Contrastive Similarity Learning.
- **链接**: [arXiv:2309.00942](https://arxiv.org/abs/2309.00942) · 📚 被引 14
- **作者**: Sha Meng, Dian Shao, Jiacheng Guo, Shan Gao
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x2019;an,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised learning is a challenging task due to the lack of labels. Multiple Object Tracking (MOT), which inevitably suffers from mutual object interference, occlusion, etc., is even more difficult without label supervision. In this paper, we explore the latent consistency of sample features across video frames and propose an Unsupervised Contrastive Similarity Learning method, named UCSL, including three contrast modules: self-contrast, cross-contrast, and ambiguity contrast. Specifically, i) self-contrast uses intra-frame direct and inter-frame indirect contrast to obtain discriminative representations by maximizing self-similarity. ii) Cross-contrast aligns cross- and continuous-frame matching results, mitigating the persistent negative effect caused by object occlusion. And iii) ambiguity contrast matches ambiguous objects with each other to further increase the certainty of subsequent object association through an implicit manner. On existing benchmarks, our method outperforms the existing unsupervised methods using only limited help from ReID head, and even provides higher accuracy than lots of fully supervised methods.

</details>

## 🆕 增量新增

### MBPTrack: Improving 3D Point Cloud Tracking with Memory networks and Box Priors. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2303.05071](https://arxiv.org/abs/2303.05071) · 📚 被引 25
- **作者**: Tian-Xing Xu, Yuan-Chen Guo, Yu-Kun Lai, Song-Hai Zhang
- **🏷️ 机构**: Tsinghua University,China, Cardiff University,United Kingdom
- **会议**: ICCV 2023
- **摘要（中）**: ①该论文针对3D单目标跟踪中外观变化和尺寸差异问题，提出MBPTrack，利用记忆网络和框先验进行粗到细定位。②方法上，采用外部记忆存储过去帧和目标掩码，通过transformer模块传播目标线索，并利用第一帧的框先验自适应采样参考点。③改进点在于结合记忆机制和框先验，提升不同尺寸目标的定位精度。④实验表明，MBPTrack在KITTI、nuScenes和Waymo数据集上达到最先进性能，显著优于现有方法。
- **摘要（英）**: This paper addresses appearance variation and size differences in 3D single object tracking by proposing MBPTrack, which uses memory networks and box priors for coarse-to-fine localization. It propagates target cues via transformer and adaptively samples reference points. Experiments show state-of-the-art performance on KITTI, nuScenes, and Waymo datasets.
- **核心贡献**: 提出MBPTrack，结合记忆网络和框先验提升3D跟踪性能。
- **创新点**: 记忆机制和自适应参考点采样。
- **结果**: 在多个数据集上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D single object tracking has been a crucial problem for decades with numerous applications such as autonomous driving. Despite its wide-ranging use, this task remains challenging due to the significant appearance variation caused by occlusion and size differences among tracked targets. To address these issues, we present MBPTrack, which adopts a Memory mechanism to utilize past information and formulates localization in a coarse-to-fine scheme using Box Priors given in the first frame. Specifically, past frames with targetness masks serve as an external memory, and a transformer-based module propagates tracked target cues from the memory to the current frame. To precisely localize objects of all sizes, MBPTrack first predicts the target center via Hough voting. By leveraging box priors given in the first frame, we adaptively sample reference points around the target center that roughly cover the target of different sizes. Then, we obtain dense feature maps by aggregating point features into the reference points, where localization can be performed more effectively. Extensive experiments demonstrate that MBPTrack achieves state-of-the-art performance on KITTI, nuScenes and Waymo Open Dataset, while running at 50 FPS on a single RTX3090 GPU.

</details>

### ZoomTrack: Target-aware Non-uniform Resizing for Efficient Visual Tracking. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/9fc291fef2f9607a46777d367f900a15-Abstract-Conference.html)
- **作者**: Yutong Kou, Jin Gao, Bing Li, Gang Wang, Weiming Hu, Yizheng Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: 该论文摘要缺失，无法提供具体内容。根据标题推测，可能针对视觉跟踪中的目标感知非均匀缩放问题，提出ZoomTrack方法，但缺乏详细信息。
- **摘要（英）**: The abstract is missing, so specific details are unavailable. Based on the title, it likely addresses target-aware non-uniform resizing for efficient visual tracking, but no concrete information is provided.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

## 跨领域论文（完整笔记在其他领域）

- GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Standing Between Past and Future: Spatio-Temporal Modeling for Multi-Camera 3D Multi-Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- OVTrack: Open-Vocabulary Multiple Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Unsupervised 3D Perception with 2D Vision-Language Distillation for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
<!-- COMPLETE v1 papers=14 -->
