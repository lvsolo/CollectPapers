# 3D Detection — 2023 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 36 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Surround-View Vision-based 3D Detection for Autonomous Driving: A Survey.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00348)
- **作者**: Apoorv Singh
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### ObjectFusion: Multi-modal 3D Object Detection with Object-Centric Fusion.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01656)
- **作者**: Qi Cai, Yingwei Pan, Ting Yao, Chong-Wah Ngo, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Object as Query: Lifting any 2D Object Detector to 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00351) · 📚 被引 47
- **作者**: Zitian Wang, Zehao Huang, Jiahui Fu, Naiyan Wang, Si Liu
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, TuSimple
- **会议**: ICCV 2023

### Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00335)
- **作者**: Shihao Wang, Yingfei Liu, Tiancai Wang, Ying Li, Xiangyu Zhang
- **🏷️ 机构**: MEGVII
- **会议**: ICCV 2023

### Efficient Transformer-based 3D Object Detection with Dynamic Token Halting.
- **链接**: [arXiv:2303.05078](https://arxiv.org/abs/2303.05078) · 📚 被引 10
- **作者**: Mao Ye, Gregory P. Meyer, Yuning Chai, Qiang Liu
- **🏷️ 机构**: The University of Texas at Austin, Cruise LLC
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Balancing efficiency and accuracy is a long-standing problem for deploying deep learning models. The trade-off is even more important for real-time safety-critical systems like autonomous vehicles. In this paper, we propose an effective approach for accelerating transformer-based 3D object detectors by dynamically halting tokens at different layers depending on their contribution to the detection task. Although halting a token is a non-differentiable operation, our method allows for differentiable end-to-end learning by leveraging an equivalent differentiable forward-pass. Furthermore, our framework allows halted tokens to be reused to inform the model's predictions through a straightforward token recycling mechanism. Our method significantly improves the Pareto frontier of efficiency versus accuracy when compared with the existing approaches. By halting tokens and increasing model capacity, we are able to improve the baseline model's performance without increasing the model's latency on the Waymo Open Dataset.

</details>

### DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00793)
- **作者**: Zeyu Wang, Dingwen Li, Chenxu Luo, Cihang Xie, Xiaodong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Revisiting Domain-Adaptive 3D Object Detection by Reliable, Diverse and Class-balanced Pseudo-Labeling.
- **链接**: [arXiv:2307.07944](https://arxiv.org/abs/2307.07944) · [代码](https://github.com/zhuoxiao-chen/ReDB-DA-3Ddet) · 📚 被引 26
- **作者**: Zhuoxiao Chen, Yadan Luo, Zheng Wang, Mahsa Baktashmotlagh, Zi Huang
- **🏷️ 机构**: The University of Queensland, University of Electronic Science and Technology of China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised domain adaptation (DA) with the aid of pseudo labeling techniques has emerged as a crucial approach for domain-adaptive 3D object detection. While effective, existing DA methods suffer from a substantial drop in performance when applied to a multi-class training setting, due to the co-existence of low-quality pseudo labels and class imbalance issues. In this paper, we address this challenge by proposing a novel ReDB framework tailored for learning to detect all classes at once. Our approach produces Reliable, Diverse, and class-Balanced pseudo 3D boxes to iteratively guide the self-training on a distributionally different target domain. To alleviate disruptions caused by the environmental discrepancy (e.g., beam numbers), the proposed cross-domain examination (CDE) assesses the correctness of pseudo labels by copy-pasting target instances into a source environment and measuring the prediction consistency. To reduce computational overhead and mitigate the object shift (e.g., scales and point densities), we design an overlapped boxes counting (OBC) metric that allows to uniformly downsample pseudo-labeled objects across different geometric characteristics. To confront the issue of inter-class imbalance, we progressively augment the target point clouds with a class-balanced set of pseudo-labeled target instances and source objects, which boosts recognition accuracies on both frequently appearing and rare classes. Experimental results on three benchmark datasets using both voxel-based (i.e., SECOND) and point-based 3D detectors (i.e., PointRCNN) demonstrate that our proposed ReDB approach outperforms existing 3D domain adaptation methods by a large margin, improving 23.15% mAP on the nuScenes $\rightarrow$ KITTI task. The code is available at https://github.com/zhuoxiao-chen/ReDB-DA-3Ddet.

</details>

### BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01675)
- **作者**: Xiaowei Chi, Jiaming Liu, Ming Lu, Rongyu Zhang, Zhaoqing Wang, Yandong Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### itKD: Interchange Transfer-based Knowledge Distillation for 3D Object Detection.
- **链接**: [arXiv:2205.15531](https://arxiv.org/abs/2205.15531) · 📚 被引 34
- **作者**: Hyeon Cho, Junyong Choi, Geonwoo Baek, Wonjun Hwang
- **🏷️ 机构**: Ajou University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> False negatives (FN) in 3D object detection, {\em e.g.}, missing predictions of pedestrians, vehicles, or other obstacles, can lead to potentially dangerous situations in autonomous driving. While being fatal, this issue is understudied in many current 3D detection methods. In this work, we propose Hard Instance Probing (HIP), a general pipeline that identifies \textit{FN} in a multi-stage manner and guides the models to focus on excavating difficult instances. For 3D object detection, we instantiate this method as FocalFormer3D, a simple yet effective detector that excels at excavating difficult objects and improving prediction recall. FocalFormer3D features a multi-stage query generation to discover hard objects and a box-level transformer decoder to efficiently distinguish objects from massive object candidates. Experimental results on the nuScenes and Waymo datasets validate the superior performance of FocalFormer3D. The advantage leads to strong performance on both detection and tracking, in both LiDAR and multi-modal settings. Notably, FocalFormer3D achieves a 70.5 mAP and 73.9 NDS on nuScenes detection benchmark, while the nuScenes tracking benchmark shows 72.1 AMOTA, both ranking 1st place on the nuScenes LiDAR leaderboard. Our code is available at \url{https://github.com/NVlabs/FocalFormer3D}.

</details>

### Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00105)
- **作者**: Yinpeng Dong, Caixin Kang, Jinlai Zhang, Zijian Zhu, Yikai Wang, Xiao Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### AeDet: Azimuth-Invariant Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02067)
- **作者**: Chengjian Feng, Zequn Jie, Yujie Zhong, Xiangxiang Chu, Lin Ma
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### MSF: Motion-guided Sequential Fusion for Efficient 3D Object Detection from Point Cloud Sequences.
- **链接**: [arXiv:2303.08316](https://arxiv.org/abs/2303.08316) · [代码](https://github.com/skyhehe123/MSF) · 📚 被引 33
- **作者**: Chenhang He, Ruihuang Li, Yabin Zhang, Shuai Li, Lei Zhang
- **🏷️ 机构**: The Hong Kong Polytechnic University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent camera-based 3D object detection methods have introduced sequential frames to improve the detection performance hoping that multiple frames would mitigate the large depth estimation error. Despite improved detection performance, prior works rely on naive fusion methods (e.g., concatenation) or are limited to static scenes (e.g., temporal stereo), neglecting the importance of the motion cue of objects. These approaches do not fully exploit the potential of sequential images and show limited performance improvements. To address this limitation, we propose a novel 3D object detection model, P2D (Predict to Detect), that integrates a prediction scheme into a detection framework to explicitly extract and leverage motion features. P2D predicts object information in the current frame using solely past frames to learn temporal motion features. We then introduce a novel temporal feature aggregation method that attentively exploits Bird's-Eye-View (BEV) features based on predicted object information, resulting in accurate 3D object detection. Experimental results demonstrate that P2D improves mAP and NDS by 3.0% and 3.7% compared to the sequential image-based baseline, illustrating that incorporating a prediction scheme can significantly improve detection accuracy.

</details>

### Density-Insensitive Unsupervised Domain Adaption on 3D Object Detection.
- **链接**: [arXiv:2304.09446](https://arxiv.org/abs/2304.09446) · 📚 被引 40
- **作者**: Qianjiang Hu, Daizong Liu, Wei Hu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China
- **会议**: CVPR 2023

### MSMDFusion: Fusing LiDAR and Camera at Multiple Scales with Multi-Depth Seeds for 3D Object Detection.
- **链接**: [arXiv:2209.03102](https://arxiv.org/abs/2209.03102) · [代码](https://github.com/SxJyJay/MSMDFusion) · 📚 被引 144
- **作者**: Yang Jiao, Zequn Jie, Shaoxiang Chen, Jingjing Chen, Lin Ma, Yu-Gang Jiang
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Meituan
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One of the main challenges in LiDAR-based 3D object detection is that the sensors often fail to capture the complete spatial information about the objects due to long distance and occlusion. Two-stage detectors with point cloud completion approaches tackle this problem by adding more points to the regions of interest (RoIs) with a pre-trained network. However, these methods generate dense point clouds of objects for all region proposals, assuming that objects always exist in the RoIs. This leads to the indiscriminate point generation for incorrect proposals as well. Motivated by this, we propose Point Generation R-CNN (PG-RCNN), a novel end-to-end detector that generates semantic surface points of foreground objects for accurate detection. Our method uses a jointly trained RoI point generation module to process the contextual information of RoIs and estimate the complete shape and displacement of foreground objects. For every generated point, PG-RCNN assigns a semantic feature that indicates the estimated foreground probability. Extensive experiments show that the point clouds generated by our method provide geometrically and semantically rich information for refining false positive and misaligned proposals. PG-RCNN achieves competitive performance on the KITTI benchmark, with significantly fewer parameters than state-of-the-art models. The code is available at https://github.com/quotation2520/PG-RCNN.

</details>

### X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01282)
- **作者**: Marvin Klingner, Shubhankar Borse, Varun Ravi Kumar, Behnaz Rezaei, Venkatraman Narayanan, Senthil Kumar Yogamani et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### LoGoNet: Towards Accurate 3D Object Detection with Local-to-Global Cross- Modal Fusion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01681) · 📚 被引 181
- **作者**: Xin Li, Tao Ma, Yuenan Hou, Botian Shi, Yuchen Yang, Youquan Liu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Shanghai AI Laboratory, Fudan University
- **会议**: CVPR 2023

### PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds.
- **链接**: [arXiv:2305.04925](https://arxiv.org/abs/2305.04925) · 📚 被引 182
- **作者**: Jinyu Li, Chenxu Luo, Xiaodong Yang
- **🏷️ 机构**: QCraft
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D detection has made great progress in recent years. However, the performance of 3D detectors is considerably limited when deployed in unseen environments, owing to the severe domain gap problem. Existing domain adaptive 3D detection methods do not adequately consider the problem of the distributional discrepancy in feature space, thereby hindering generalization of detectors across domains. In this work, we propose a novel unsupervised domain adaptive \textbf{3D} detection framework, namely \textbf{G}eometry-aware \textbf{P}rototype \textbf{A}lignment (\textbf{GPA-3D}), which explicitly leverages the intrinsic geometric relationship from point cloud objects to reduce the feature discrepancy, thus facilitating cross-domain transferring. Specifically, GPA-3D assigns a series of tailored and learnable prototypes to point cloud objects with distinct geometric structures. Each prototype aligns BEV (bird's-eye-view) features derived from corresponding point cloud objects on source and target domains, reducing the distributional discrepancy and achieving better adaptation. The evaluation results obtained on various benchmarks, including Waymo, nuScenes and KITTI, demonstrate the superiority of our GPA-3D over the state-of-the-art approaches for different adaptation scenarios. The MindSpore version code will be publicly available at \url{https://github.com/Liz66666/GPA3D}.

</details>

### Representation Disparity-aware Distillation for 3D Object Detection.
- **链接**: [arXiv:2308.10308](https://arxiv.org/abs/2308.10308) · 📚 被引 7
- **作者**: Yanjing Li, Sheng Xu, Mingbao Lin, Jihao Yin, Baochang Zhang, Xianbin Cao
- **🏷️ 机构**: Beihang University, Tencent
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we focus on developing knowledge distillation (KD) for compact 3D detectors. We observe that off-the-shelf KD methods manifest their efficacy only when the teacher model and student counterpart share similar intermediate feature representations. This might explain why they are less effective in building extreme-compact 3D detectors where significant representation disparity arises due primarily to the intrinsic sparsity and irregularity in 3D point clouds. This paper presents a novel representation disparity-aware distillation (RDD) method to address the representation disparity issue and reduce performance gap between compact students and over-parameterized teachers. This is accomplished by building our RDD from an innovative perspective of information bottleneck (IB), which can effectively minimize the disparity of proposal region pairs from student and teacher in features and logits. Extensive experiments are performed to demonstrate the superiority of our RDD over existing KD methods. For example, our RDD increases mAP of CP-Voxel-S to 57.1% on nuScenes dataset, which even surpasses teacher performance while taking up only 42% FLOPs.

</details>

### SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01703)
- **作者**: Haisong Liu, Yao Teng, Tao Lu, Haiguang Wang, Limin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01281)
- **作者**: Shuo Wang, Xinhai Zhao, Hai-Ming Xu, Zehui Chen, Dameng Yu, Jiahao Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Semi-Supervised Stereo-Based 3D Object Detection via Cross-View Consensus.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01676) · 📚 被引 5
- **作者**: Wenhao Wu, Hau-San Wong, Si Wu
- **🏷️ 机构**: City University of Hong Kong,Department of Computer Science, School of Computer Science and Engineering, South China University of Technology
- **会议**: CVPR 2023

### Virtual Sparse Convolution for Multimodal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02074)
- **作者**: Hai Wu, Chenglu Wen, Shaoshuai Shi, Xin Li, Cheng Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### CAPE: Camera View Position Embedding for Multi-View 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02066)
- **作者**: Kaixin Xiong, Shi Gong, Xiaoqing Ye, Xiao Tan, Ji Wan, Errui Ding et al.
- **🏷️ 机构**: HUAST
- **会议**: CVPR 2023

### Leveraging Vision-Centric Multi-Modal Expertise for 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/79206ac5b7e88eeeed74997f3b6f4c7f-Abstract-Conference.html)
- **作者**: Linyan Huang, Zhiqi Li, Chonghao Sima, Wenhai Wang, Jingdong Wang, Yu Qiao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cooperatively utilizing both ego-vehicle and infrastructure sensor data can significantly enhance autonomous driving perception abilities. However, the uncertain temporal asynchrony and limited communication conditions can lead to fusion misalignment and constrain the exploitation of infrastructure data. To address these issues in vehicle-infrastructure cooperative 3D (VIC3D) object detection, we propose the Feature Flow Net (FFNet), a novel cooperative detection framework. FFNet is a flow-based feature fusion framework that uses a feature flow prediction module to predict future features and compensate for asynchrony. Instead of transmitting feature maps extracted from still-images, FFNet transmits feature flow, leveraging the temporal coherence of sequential infrastructure frames. Furthermore, we introduce a self-supervised training approach that enables FFNet to generate feature flow with feature prediction ability from raw infrastructure sequences. Experimental results demonstrate that our proposed method outperforms existing cooperative detection methods while only requiring about 1/100 of the transmission cost of raw data and covers all latency in one model on the DAIR-V2X dataset. The code is available at \href{https://github.com/haibao-yu/FFNet-VIC3D}{https://github.com/haibao-yu/FFNet-VIC3D}.

</details>

### Distilling Focal Knowledge from Imperfect Expert for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00102) · 📚 被引 13
- **作者**: Jia Zeng, Li Chen, Hanming Deng, Lewei Lu, Junchi Yan, Yu Qiao et al.
- **🏷️ 机构**: OpenDrivel.ab, Shanghai AI Lab, SenseTime Research
- **会议**: CVPR 2023

### Uni3D: A Unified Baseline for Multi-Dataset 3D Object Detection.
- **链接**: [arXiv:2303.06880](https://arxiv.org/abs/2303.06880) · 📚 被引 43
- **作者**: Bo Zhang, Jiakang Yuan, Botian Shi, Tao Chen, Yikang Li, Yu Qiao
- **🏷️ 机构**: Shanghai AI Laboratory, School of Information Science and Technology, Fudan University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current 3D object detection models follow a single dataset-specific training and testing paradigm, which often faces a serious detection accuracy drop when they are directly deployed in another dataset. In this paper, we study the task of training a unified 3D detector from multiple datasets. We observe that this appears to be a challenging task, which is mainly due to that these datasets present substantial data-level differences and taxonomy-level variations caused by different LiDAR types and data acquisition standards. Inspired by such observation, we present a Uni3D which leverages a simple data-level correction operation and a designed semantic-level coupling-and-recoupling module to alleviate the unavoidable data-level and taxonomy-level differences, respectively. Our method is simple and easily combined with many 3D object detection baselines such as PV-RCNN and Voxel-RCNN, enabling them to effectively learn from multiple off-the-shelf 3D datasets to obtain more discriminative and generalizable representations. Experiments are conducted on many dataset consolidation settings including Waymo-nuScenes, nuScenes-KITTI, Waymo-KITTI, and Waymo-nuScenes-KITTI consolidations. Their results demonstrate that Uni3D exceeds a series of individual detectors trained on a single dataset, with a 1.04x parameter increase over a selected baseline detector. We expect this work will inspire the research of 3D generalization since it will push the limits of perceptual performance.

</details>

### OcTr: Octree-Based Transformer for 3D Object Detection.
- **链接**: [arXiv:2303.12621](https://arxiv.org/abs/2303.12621) · 📚 被引 79
- **作者**: Chao Zhou, Yanan Zhang, Jiaxin Chen, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A key challenge for LiDAR-based 3D object detection is to capture sufficient features from large scale 3D scenes especially for distant or/and occluded objects. Albeit recent efforts made by Transformers with the long sequence modeling capability, they fail to properly balance the accuracy and efficiency, suffering from inadequate receptive fields or coarse-grained holistic correlations. In this paper, we propose an Octree-based Transformer, named OcTr, to address this issue. It first constructs a dynamic octree on the hierarchical feature pyramid through conducting self-attention on the top level and then recursively propagates to the level below restricted by the octants, which captures rich global context in a coarse-to-fine manner while maintaining the computational complexity under control. Furthermore, for enhanced foreground perception, we propose a hybrid positional embedding, composed of the semantic-aware positional embedding and attention mask, to fully exploit semantic and geometry clues. Extensive experiments are conducted on the Waymo Open Dataset and KITTI Dataset, and OcTr reaches newly state-of-the-art results.

</details>

### UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00495)
- **作者**: Shengchao Zhou, Weizhou Liu, Chen Hu, Shuchang Zhou, Chao Ma
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection.
- **链接**: [arXiv:2307.08209](https://arxiv.org/abs/2307.08209) · 📚 被引 29
- **作者**: Tianchen Zhao, Xuefei Ning, Ke Hong, Zhongyuan Qiu, Pu Lu, Yali Zhao et al.
- **🏷️ 机构**: Tsinghua University, Novauto, Meituan
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Voxel-based methods have achieved state-of-the-art performance for 3D object detection in autonomous driving. However, their significant computational and memory costs pose a challenge for their application to resource-constrained vehicles. One reason for this high resource consumption is the presence of a large number of redundant background points in Lidar point clouds, resulting in spatial redundancy in both 3D voxel and dense BEV map representations. To address this issue, we propose an adaptive inference framework called Ada3D, which focuses on exploiting the input-level spatial redundancy. Ada3D adaptively filters the redundant input, guided by a lightweight importance predictor and the unique properties of the Lidar point cloud. Additionally, we utilize the BEV features' intrinsic sparsity by introducing the Sparsity Preserving Batch Normalization. With Ada3D, we achieve 40% reduction for 3D voxels and decrease the density of 2D BEV feature maps from 100% to 20% without sacrificing accuracy. Ada3D reduces the model computational and memory cost by 5x, and achieves 1.52x/1.45x end-to-end GPU latency and 1.5x/4.5x GPU peak memory optimization for the 3D and 2D backbone respectively.

</details>

### Understanding the Robustness of 3D Object Detection with Bird'View Representations in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02069)
- **作者**: Zijian Zhu, Yichi Zhang, Hai Chen, Yinpeng Dong, Shu Zhao, Wenbo Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### On Offline Evaluation of 3D Object Detection for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00441)
- **作者**: Tim Schreier, Katrin Renz, Andreas Geiger, Kashyap Chitta
- **🏷️ 机构**: University of Tübingen
- **会议**: ICCV 2023

### SVQNet: Sparse Voxel-Adjacent Query Network for 4D Spatio-Temporal LiDAR Semantic Segmentation.
- **链接**: [arXiv:2308.13323](https://arxiv.org/abs/2308.13323) · 📚 被引 10
- **作者**: Xuechao Chen, Shuangjie Xu, Xiaoyi Zou, Tongyi Cao, Dit-Yan Yeung, Lu Fang
- **🏷️ 机构**: Tsinghua University, Hong Kong University of Science and Technology, Deeproute.ai
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised object detection is crucial for 3D scene understanding, efficiently addressing the limitation of acquiring large-scale 3D bounding box annotations. Existing methods typically employ a teacher-student framework with pseudo-labeling to leverage unlabeled point clouds. However, producing reliable pseudo-labels in a diverse 3D space still remains challenging. In this work, we propose Diffusion-SS3D, a new perspective of enhancing the quality of pseudo-labels via the diffusion model for semi-supervised 3D object detection. Specifically, we include noises to produce corrupted 3D object size and class label distributions, and then utilize the diffusion model as a denoising process to obtain bounding box outputs. Moreover, we integrate the diffusion model into the teacher-student framework, so that the denoised bounding boxes can be used to improve pseudo-label generation, as well as the entire semi-supervised learning process. We conduct experiments on the ScanNet and SUN RGB-D benchmark datasets to demonstrate that our approach achieves state-of-the-art performance against existing methods. We also present extensive analysis to understand how our diffusion model design affects performance in semi-supervised learning.

</details>

### PointDC: Unsupervised Semantic Segmentation of 3D Point Clouds via Cross-modal Distillation and Super-Voxel Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01314)
- **作者**: Zisheng Chen, Hongbin Xu, Weitao Chen, Zhipeng Zhou, Haihong Xiao, Baigui Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### PointDistiller: Structured Knowledge Distillation Towards Efficient and Compact 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02087) · 📚 被引 59
- **作者**: Linfeng Zhang, Runpei Dong, Hung-Shuo Tai, Kaisheng Ma
- **🏷️ 机构**: Tsinghua University, Xi&#x0027;an Jiaotong University, DIDI
- **会议**: CVPR 2023
