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

### Time Will Tell: New Outlooks and A Baseline for Temporal Multi-View 3D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=H3HcEJA2Um)
- **作者**: Jinhyung Park, Chenfeng Xu, Shijia Yang, Kurt Keutzer, Kris M. Kitani, Masayoshi Tomizuka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### DBQ-SSD: Dynamic Ball Query for Efficient 3D Object Detection.
- **链接**: [arXiv:2207.10909](https://arxiv.org/abs/2207.10909) · [代码](https://github.com/yancie-yjr/DBQ-SSD)
- **作者**: Jinrong Yang, Lin Song, Songtao Liu, Weixin Mao, Zeming Li, Xiaoping Li et al.
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many point-based 3D detectors adopt point-feature sampling strategies to drop some points for efficient inference. These strategies are typically based on fixed and handcrafted rules, making it difficult to handle complicated scenes. Different from them, we propose a Dynamic Ball Query (DBQ) network to adaptively select a subset of input points according to the input features, and assign the feature transform with a suitable receptive field for each selected point. It can be embedded into some state-of-the-art 3D detectors and trained in an end-to-end manner, which significantly reduces the computational cost. Extensive experiments demonstrate that our method can increase the inference speed by 30%-100% on KITTI, Waymo, and ONCE datasets. Specifically, the inference speed of our detector can reach 162 FPS on KITTI scene, and 30 FPS on Waymo and ONCE scenes without performance degradation. Due to skipping the redundant points, some evaluation metrics show significant improvements. Codes will be released at https://github.com/yancie-yjr/DBQ-SSD.

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

## 🆕 增量新增

### Omni3D: A Large Benchmark and Model for 3D Object Detection in the Wild. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01264) · 📚 被引 106
- **作者**: Garrick Brazil, Abhinav Kumar, Julian Straub, Nikhila Ravi, Justin Johnson, Georgia Gkioxari
- **🏷️ 机构**: Meta AI, Michigan State University, Caltech
- **会议**: CVPR 2023
- **摘要（中）**: 针对现有3D目标检测数据集局限于特定场景（如室内或自动驾驶）的问题，提出了Omni3D，一个大规模野外3D目标检测基准，包含多样化的真实世界图像和3D标注。同时提出了一种新的模型，利用全局场景理解和局部几何推理，在跨域场景中实现鲁棒的3D检测。相比已有工作，该基准和模型显著提升了野外3D检测的泛化能力，在多个数据集上取得了领先性能。
- **摘要（英）**: This paper addresses the limitation of existing 3D object detection datasets confined to specific domains like indoor or autonomous driving. It introduces Omni3D, a large-scale benchmark for in-the-wild 3D detection with diverse real-world images and 3D annotations, and a novel model combining global scene understanding with local geometric reasoning. This approach enhances generalization across domains, achieving state-of-the-art performance on multiple datasets.
- **核心贡献**: 构建了Omni3D基准并提出了跨域3D检测模型。
- **创新点**: 结合全局和局部信息处理野外场景的3D检测。
- **结果**: 在多个数据集上取得领先性能。

### AShapeFormer : Semantics-Guided Object-Level Active Shape Encoding for 3D Object Detection via Transformers. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00104) · 📚 被引 19
- **作者**: Zechuan Li, Hongshan Yu, Zhengeng Yang, Tom Tongjia Chen, Naveed Akhtar
- **🏷️ 机构**: Hunan University, The University of Western Australia
- **会议**: CVPR 2023
- **摘要（中）**: ①针对3D点云目标检测中形状信息利用不充分的问题。②提出AShapeFormer，通过语义引导的主动形状编码，利用Transformer架构增强形状特征表达。③相比现有方法，更有效地结合语义信息与几何形状，提升检测精度。④在标准数据集上验证了有效性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses insufficient shape information utilization in 3D point cloud object detection. It proposes AShapeFormer with semantics-guided active shape encoding via Transformers to enhance shape features. The method improves detection accuracy by effectively integrating semantic and geometric information, though specific numerical results are not provided in the abstract.
- **核心贡献**: 提出语义引导的主动形状编码Transformer用于3D目标检测。
- **创新点**: 将语义信息与主动形状编码结合，增强形状特征表达。
- **结果**: 在3D检测任务上验证了有效性，但未提供具体性能数据。

### VoxelNeXt: Fully Sparse VoxelNet for 3D Object Detection and Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02076) · 📚 被引 449
- **作者**: Yukang Chen, Jianhui Liu, Xiangyu Zhang, Xiaojuan Qi, Jiaya Jia
- **🏷️ 机构**: The Chinese University of Hong Kong, The University of Hong Kong, MEGVII
- **会议**: CVPR 2023
- **摘要（中）**: 针对现有3D检测方法依赖密集特征或后处理的问题，提出了VoxelNeXt，一种全稀疏的VoxelNet用于3D检测和跟踪。方法上，完全基于稀疏卷积和稀疏特征，直接预测3D框，无需密集特征或特定后处理。相比已有工作，该方法简化了检测流程，提高了效率。摘要未提供具体数据，但全稀疏设计在效率和性能上具有潜力。
- **摘要（英）**: This paper addresses the inefficiency of dense features in 3D detection. It proposes VoxelNeXt, a fully sparse voxel network that directly predicts 3D boxes without dense features or post-processing. This simplifies the pipeline and improves efficiency, though specific results are not provided in the abstract.
- **核心贡献**: 提出了全稀疏VoxelNet，简化3D检测和跟踪流程。
- **创新点**: 完全基于稀疏卷积，无需密集特征和后处理。
- **结果**: 摘要未提供具体数据，但展示了高效检测的潜力。

### MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2306.03206](https://arxiv.org/abs/2306.03206) · 📚 被引 17
- **作者**: Yingwei Li, Charles R. Qi, Yin Zhou, Chenxi Liu, Dragomir Anguelov
- **🏷️ 机构**: Waymo LLC
- **会议**: CVPR 2023
- **摘要（中）**: ①针对点云序列中遮挡和远距离目标检测困难的问题。②提出了MoDAR，利用运动预测输出生成虚拟点云模态，将时序上下文中的目标信息传播到当前帧，增强原始点云。③相比直接编码长序列的方法，MoDAR以虚拟点形式高效利用超长序列信息，且兼容任意点云检测器。④在Waymo数据集上，使用18秒序列显著提升检测性能，达到新最先进水平，计算开销小。
- **摘要（英）**: This paper addresses occluded and long-range object detection in point cloud sequences. MoDAR generates virtual points from motion forecasting to augment LiDAR data, effectively encoding long-term context. It achieves new state-of-the-art results on Waymo with minimal overhead.
- **核心贡献**: 提出基于运动预测的虚拟模态增强3D检测。
- **创新点**: 将运动预测输出转化为虚拟点云。
- **结果**: 在Waymo上显著提升检测性能并保持低开销。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Occluded and long-range objects are ubiquitous and challenging for 3D object detection. Point cloud sequence data provide unique opportunities to improve such cases, as an occluded or distant object can be observed from different viewpoints or gets better visibility over time. However, the efficiency and effectiveness in encoding long-term sequence data can still be improved. In this work, we propose MoDAR, using motion forecasting outputs as a type of virtual modality, to augment LiDAR point clouds. The MoDAR modality propagates object information from temporal contexts to a target frame, represented as a set of virtual points, one for each object from a waypoint on a forecasted trajectory. A fused point cloud of both raw sensor points and the virtual points can then be fed to any off-the-shelf point-cloud based 3D object detector. Evaluated on the Waymo Open Dataset, our method significantly improves prior art detectors by using motion forecasting from extra-long sequences (e.g. 18 seconds), achieving new state of the arts, while not adding much computation overhead.

</details>

### Deep Dive into Gradients: Better Optimization for 3D Object Detection with Gradient-Corrected IoU Supervision. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00497) · 📚 被引 15
- **作者**: Qi Ming, Lingjuan Miao, Zhe Ma, Lin Zhao, Zhiqiang Zhou, Xuhui Huang et al.
- **🏷️ 机构**: School of Automation, Beijing Institute of Technology,China
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对3D目标检测中IoU监督与梯度优化不匹配的问题，即传统IoU损失在梯度传播时可能不准确或导致优化不稳定。②提出了梯度校正的IoU监督方法，通过分析梯度并修正IoU损失的梯度方向，以改善训练过程。③相比已有工作，该方法直接优化梯度而非仅调整损失函数形式，更细粒度地提升优化效率。④实验表明，该方法在3D检测基准上提升了检测精度，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the mismatch between IoU supervision and gradient optimization in 3D object detection, where traditional IoU losses may yield inaccurate gradients. It proposes a gradient-corrected IoU supervision method that adjusts gradient directions during training. Compared to existing works, it directly refines gradients rather than loss formulations, improving optimization efficiency. Experiments show improved detection accuracy on 3D benchmarks, though specific numbers are not provided in the abstract.
- **核心贡献**: 提出梯度校正的IoU监督机制，提升3D检测训练的优化质量。
- **创新点**: 从梯度角度修正IoU损失，而非仅调整损失函数形式。
- **结果**: 在3D检测基准上提升了精度，但具体数值未在摘要中给出。

### Bi3D: Bi-Domain Active Learning for Cross-Domain 3D Object Detection.
- **链接**: [arXiv:2303.05886](https://arxiv.org/abs/2303.05886)
- **作者**: Jiakang Yuan, Bo Zhang, Xiangchao Yan, Tao Chen, Botian Shi, Yikang Li et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Domain Adaptation (UDA) technique has been explored in 3D cross-domain tasks recently. Though preliminary progress has been made, the performance gap between the UDA-based 3D model and the supervised one trained with fully annotated target domain is still large. This motivates us to consider selecting partial-yet-important target data and labeling them at a minimum cost, to achieve a good trade-off between high performance and low annotation cost. To this end, we propose a Bi-domain active learning approach, namely Bi3D, to solve the cross-domain 3D object detection task. The Bi3D first develops a domainness-aware source sampling strategy, which identifies target-domain-like samples from the source domain to avoid the model being interfered by irrelevant source data. Then a diversity-based target sampling strategy is developed, which selects the most informative subset of target domain to improve the model adaptability to the target domain using as little annotation budget as possible. Experiments are conducted on typical cross-domain adaptation scenarios including cross-LiDAR-beam, cross-country, and cross-sensor, where Bi3D achieves a promising target-domain detection accuracy (89.63% on KITTI) compared with UDAbased work (84.29%), even surpassing the detector trained on the full set of the labeled target domain (88.98%). Our code is available at: https://github.com/PJLabADG/3DTrans.

</details>

### MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer.
- **链接**: [arXiv:2303.13018](https://arxiv.org/abs/2303.13018) · 📚 被引 46
- **作者**: Yunsong Zhou, Hongzi Zhu, Quan Liu, Shan Chang, Minyi Guo
- **🏷️ 机构**: Shanghai Jiao Tong University, Donghua University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mobile monocular 3D object detection (Mono3D) (e.g., on a vehicle, a drone, or a robot) is an important yet challenging task. Existing transformer-based offline Mono3D models adopt grid-based vision tokens, which is suboptimal when using coarse tokens due to the limited available computational power. In this paper, we propose an online Mono3D framework, called MonoATT, which leverages a novel vision transformer with heterogeneous tokens of varying shapes and sizes to facilitate mobile Mono3D. The core idea of MonoATT is to adaptively assign finer tokens to areas of more significance before utilizing a transformer to enhance Mono3D. To this end, we first use prior knowledge to design a scoring network for selecting the most important areas of the image, and then propose a token clustering and merging network with an attention mechanism to gradually merge tokens around the selected areas in multiple stages. Finally, a pixel-level feature map is reconstructed from heterogeneous tokens before employing a SOTA Mono3D detector as the underlying detection core. Experiment results on the real-world KITTI dataset demonstrate that MonoATT can effectively improve the Mono3D accuracy for both near and far objects and guarantee low latency. MonoATT yields the best performance compared with the state-of-the-art methods by a large margin and is ranked number one on the KITTI 3D benchmark.

</details>

### MV-JAR: Masked Voxel Jigsaw and Reconstruction for LiDAR-Based Self-Supervised Pre-Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01292) · 📚 被引 23
- **作者**: Runsen Xu, Tai Wang, Wenwei Zhang, Runjian Chen, Jinkun Cao, Jiangmiao Pang et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, NTU,S-Lab, The University of Hong Kong
- **会议**: CVPR 2023

### GraVoS: Voxel Selection for 3D Point-Cloud Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02077) · 📚 被引 15
- **作者**: Oren Shrout, Yizhak Ben-Shabat, Ayellet Tal
- **🏷️ 机构**: Technion,Israel
- **会议**: CVPR 2023

### Revisiting Domain-Adaptive 3D Object Detection by Reliable, Diverse and Class-balanced Pseudo-Labeling.
- **链接**: [arXiv:2307.07944](https://arxiv.org/abs/2307.07944) · 📚 被引 26
- **作者**: Zhuoxiao Chen, Yadan Luo, Zheng Wang, Mahsa Baktashmotlagh, Zi Huang
- **🏷️ 机构**: The University of Queensland, University of Electronic Science and Technology of China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised domain adaptation (DA) with the aid of pseudo labeling techniques has emerged as a crucial approach for domain-adaptive 3D object detection. While effective, existing DA methods suffer from a substantial drop in performance when applied to a multi-class training setting, due to the co-existence of low-quality pseudo labels and class imbalance issues. In this paper, we address this challenge by proposing a novel ReDB framework tailored for learning to detect all classes at once. Our approach produces Reliable, Diverse, and class-Balanced pseudo 3D boxes to iteratively guide the self-training on a distributionally different target domain. To alleviate disruptions caused by the environmental discrepancy (e.g., beam numbers), the proposed cross-domain examination (CDE) assesses the correctness of pseudo labels by copy-pasting target instances into a source environment and measuring the prediction consistency. To reduce computational overhead and mitigate the object shift (e.g., scales and point densities), we design an overlapped boxes counting (OBC) metric that allows to uniformly downsample pseudo-labeled objects across different geometric characteristics. To confront the issue of inter-class imbalance, we progressively augment the target point clouds with a class-balanced set of pseudo-labeled target instances and source objects, which boosts recognition accuracies on both frequently appearing and rare classes. Experimental results on three benchmark datasets using both voxel-based (i.e., SECOND) and point-based 3D detectors (i.e., PointRCNN) demonstrate that our proposed ReDB approach outperforms existing 3D domain adaptation methods by a large margin, improving 23.15% mAP on the nuScenes $\rightarrow$ KITTI task. The code is available at https://github.com/zhuoxiao-chen/ReDB-DA-3Ddet.

</details>

### Learning with Noisy Data for Semi-Supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00638) · 📚 被引 15
- **作者**: Zehui Chen, Zhenyu Li, Shuo Wang, Dengpan Fu, Feng Zhao
- **🏷️ 机构**: University of Science and Technology of China, Harbin Institute of Technology, NIO
- **会议**: ICCV 2023

### FocalFormer3D : Focusing on Hard Instance for 3D Object Detection.
- **链接**: [arXiv:2308.04556](https://arxiv.org/abs/2308.04556) · 📚 被引 112
- **作者**: Yilun Chen, Zhiding Yu, Yukang Chen, Shiyi Lan, Anima Anandkumar, Jiaya Jia et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, NVIDIA, Caltech
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> False negatives (FN) in 3D object detection, {\em e.g.}, missing predictions of pedestrians, vehicles, or other obstacles, can lead to potentially dangerous situations in autonomous driving. While being fatal, this issue is understudied in many current 3D detection methods. In this work, we propose Hard Instance Probing (HIP), a general pipeline that identifies \textit{FN} in a multi-stage manner and guides the models to focus on excavating difficult instances. For 3D object detection, we instantiate this method as FocalFormer3D, a simple yet effective detector that excels at excavating difficult objects and improving prediction recall. FocalFormer3D features a multi-stage query generation to discover hard objects and a box-level transformer decoder to efficiently distinguish objects from massive object candidates. Experimental results on the nuScenes and Waymo datasets validate the superior performance of FocalFormer3D. The advantage leads to strong performance on both detection and tracking, in both LiDAR and multi-modal settings. Notably, FocalFormer3D achieves a 70.5 mAP and 73.9 NDS on nuScenes detection benchmark, while the nuScenes tracking benchmark shows 72.1 AMOTA, both ranking 1st place on the nuScenes LiDAR leaderboard. Our code is available at \url{https://github.com/NVlabs/FocalFormer3D}.

</details>

### Once Detected, Never Lost: Surpassing Human Performance in Offline LiDAR based 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01815) · 📚 被引 28
- **作者**: Lue Fan, Yuxue Yang, Yiming Mao, Feng Wang, Yuntao Chen, Naiyan Wang et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Automation, Hunan University, TuSimple
- **会议**: ICCV 2023

### A Fast Unified System for 3D Object Detection and Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01563) · 📚 被引 3
- **作者**: Thomas Heitzinger, Martin Kampel
- **🏷️ 机构**: TU Wien,Computer Vision Lab,Vienna,Austria
- **会议**: ICCV 2023

### UpCycling: Semi-supervised 3D Object Detection without Sharing Raw-level Unlabeled Scenes.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02134) · 📚 被引 4
- **作者**: Sunwook Hwang, Youngseok Kim, Seongwon Kim, Saewoong Bahk, Hyung-Sin Kim
- **🏷️ 机构**: Seoul National University,Department of Electrical and Computer Engineering, SK Telecom,Seoul,Korea, Seoul National University,Graduate School of Data Science
- **会议**: ICCV 2023

### PG-RCNN: Semantic Surface Point Generation for 3D Object Detection.
- **链接**: [arXiv:2307.12637](https://arxiv.org/abs/2307.12637) · 📚 被引 49
- **作者**: Inyong Koo, Inyoung Lee, Se-Ho Kim, Hee-Seon Kim, Woo-Jin Jeon, Changick Kim
- **🏷️ 机构**: KAIST Daejeon,South Korea
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One of the main challenges in LiDAR-based 3D object detection is that the sensors often fail to capture the complete spatial information about the objects due to long distance and occlusion. Two-stage detectors with point cloud completion approaches tackle this problem by adding more points to the regions of interest (RoIs) with a pre-trained network. However, these methods generate dense point clouds of objects for all region proposals, assuming that objects always exist in the RoIs. This leads to the indiscriminate point generation for incorrect proposals as well. Motivated by this, we propose Point Generation R-CNN (PG-RCNN), a novel end-to-end detector that generates semantic surface points of foreground objects for accurate detection. Our method uses a jointly trained RoI point generation module to process the contextual information of RoIs and estimate the complete shape and displacement of foreground objects. For every generated point, PG-RCNN assigns a semantic feature that indicates the estimated foreground probability. Extensive experiments show that the point clouds generated by our method provide geometrically and semantically rich information for refining false positive and misaligned proposals. PG-RCNN achieves competitive performance on the KITTI benchmark, with significantly fewer parameters than state-of-the-art models. The code is available at https://github.com/quotation2520/PG-RCNN.

</details>

### Monocular 3D Object Detection with Bounding Box Denoising in 3D by Perceiver.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00592) · 📚 被引 16
- **作者**: Xianpeng Liu, Ce Zheng, Kelvin Cheng, Nan Xue, Guo-Jun Qi, Tianfu Wu
- **🏷️ 机构**: North Carolina State University, University of Central Florida, Ant Group
- **会议**: ICCV 2023

### Kecor: Kernel Coding Rate Maximization for Active 3D Object Detection.
- **链接**: [arXiv:2307.07942](https://arxiv.org/abs/2307.07942) · 📚 被引 15
- **作者**: Yadan Luo, Zhuoxiao Chen, Zhen Fang, Zheng Zhang, Mahsa Baktashmotlagh, Zi Huang
- **🏷️ 机构**: The University of Queensland, University of Technology Sydney, Harbin Institute of Technology,Shenzhen
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Achieving a reliable LiDAR-based object detector in autonomous driving is paramount, but its success hinges on obtaining large amounts of precise 3D annotations. Active learning (AL) seeks to mitigate the annotation burden through algorithms that use fewer labels and can attain performance comparable to fully supervised learning. Although AL has shown promise, current approaches prioritize the selection of unlabeled point clouds with high uncertainty and/or diversity, leading to the selection of more instances for labeling and reduced computational efficiency. In this paper, we resort to a novel kernel coding rate maximization (KECOR) strategy which aims to identify the most informative point clouds to acquire labels through the lens of information theory. Greedy search is applied to seek desired point clouds that can maximize the minimal number of bits required to encode the latent features. To determine the uniqueness and informativeness of the selected samples from the model perspective, we construct a proxy network of the 3D detector head and compute the outer product of Jacobians from all proxy layers to form the empirical neural tangent kernel (NTK) matrix. To accommodate both one-stage (i.e., SECOND) and two-stage detectors (i.e., PVRCNN), we further incorporate the classification entropy maximization and well trade-off between detection performance and the total number of bounding boxes selected for annotation. Extensive experiments conducted on two 3D benchmarks and a 2D detection dataset evidence the superiority and versatility of the proposed approach. Our results show that approximately 44% box-level annotation costs and 26% computational time are reduced compared to the state-of-the-art AL method, without compromising detection performance.

</details>

### Towards Fair and Comprehensive Comparisons for Image-Based 3D Object Detection.
- **链接**: [arXiv:2310.05447](https://arxiv.org/abs/2310.05447) · 📚 被引 2
- **作者**: Xinzhu Ma, Yongtao Wang, Yinmin Zhang, Zhiyi Xia, Yuan Meng, Zhihui Wang et al.
- **🏷️ 机构**: Shanghai AI Lab, Dalian University of Technology, Tsinghua University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we build a modular-designed codebase, formulate strong training recipes, design an error diagnosis toolbox, and discuss current methods for image-based 3D object detection. In particular, different from other highly mature tasks, e.g., 2D object detection, the community of image-based 3D object detection is still evolving, where methods often adopt different training recipes and tricks resulting in unfair evaluations and comparisons. What is worse, these tricks may overwhelm their proposed designs in performance, even leading to wrong conclusions. To address this issue, we build a module-designed codebase and formulate unified training standards for the community. Furthermore, we also design an error diagnosis toolbox to measure the detailed characterization of detection models. Using these tools, we analyze current methods in-depth under varying settings and provide discussions for some open questions, e.g., discrepancies in conclusions on KITTI-3D and nuScenes datasets, which have led to different dominant methods for these datasets. We hope that this work will facilitate future research in image-based 3D object detection. Our codes will be released at \url{https://github.com/OpenGVLab/3dodi}

</details>

### DetZero: Rethinking Offboard 3D Object Detection with Long-term Sequential Point Clouds.
- **链接**: [arXiv:2306.06023](https://arxiv.org/abs/2306.06023) · 📚 被引 42
- **作者**: Tao Ma, Xuemeng Yang, Hongbin Zhou, Xin Li, Botian Shi, Junjie Liu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong,Multimedia Laboratory, Shanghai Artificial Intelligence Laboratory, East China Normal University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing offboard 3D detectors always follow a modular pipeline design to take advantage of unlimited sequential point clouds. We have found that the full potential of offboard 3D detectors is not explored mainly due to two reasons: (1) the onboard multi-object tracker cannot generate sufficient complete object trajectories, and (2) the motion state of objects poses an inevitable challenge for the object-centric refining stage in leveraging the long-term temporal context representation. To tackle these problems, we propose a novel paradigm of offboard 3D object detection, named DetZero. Concretely, an offline tracker coupled with a multi-frame detector is proposed to focus on the completeness of generated object tracks. An attention-mechanism refining module is proposed to strengthen contextual information interaction across long-term sequential point clouds for object refining with decomposed regression methods. Extensive experiments on Waymo Open Dataset show our DetZero outperforms all state-of-the-art onboard and offboard 3D detection methods. Notably, DetZero ranks 1st place on Waymo 3D object detection leaderboard with 85.15 mAPH (L2) detection performance. Further experiments validate the application of taking the place of human labels with such high-quality results. Our empirical study leads to rethinking conventions and interesting findings that can guide future research on offboard 3D object detection.

</details>

### PARTNER: Level up the Polar Representation for LiDAR 3D Object Detection.
- **链接**: [arXiv:2308.03982](https://arxiv.org/abs/2308.03982) · 📚 被引 20
- **作者**: Ming Nie, Yujing Xue, Chunwei Wang, Chaoqiang Ye, Hang Xu, Xinge Zhu et al.
- **🏷️ 机构**: Fudan University,School of Data Science, National University of Singapore, Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, polar-based representation has shown promising properties in perceptual tasks. In addition to Cartesian-based approaches, which separate point clouds unevenly, representing point clouds as polar grids has been recognized as an alternative due to (1) its advantage in robust performance under different resolutions and (2) its superiority in streaming-based approaches. However, state-of-the-art polar-based detection methods inevitably suffer from the feature distortion problem because of the non-uniform division of polar representation, resulting in a non-negligible performance gap compared to Cartesian-based approaches. To tackle this issue, we present PARTNER, a novel 3D object detector in the polar coordinate. PARTNER alleviates the dilemma of feature distortion with global representation re-alignment and facilitates the regression by introducing instance-level geometric information into the detection head. Extensive experiments show overwhelming advantages in streaming-based detection and different resolutions. Furthermore, our method outperforms the previous polar-based works with remarkable margins of 3.68% and 9.15% on Waymo and ONCE validation set, thus achieving competitive results over the state-of-the-art methods.

</details>

### Clusterformer: Cluster-based Transformer for 3D Object Detection in Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00613) · 📚 被引 14
- **作者**: Yu Pei, Xian Zhao, Hao Li, Jingyuan Ma, Jingwei Zhang, Shiliang Pu
- **🏷️ 机构**: HikVision Research Institute
- **会议**: ICCV 2023

### SupFusion: Supervised LiDAR-Camera Fusion for 3D Object Detection.
- **链接**: [arXiv:2309.07084](https://arxiv.org/abs/2309.07084) · 📚 被引 34
- **作者**: Yiran Qin, Chaoqun Wang, Zijian Kang, Ningning Ma, Zhen Li, Ruimao Zhang
- **🏷️ 机构**: The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen),School of Data Science, Shenzhen Research Institute of Big Data,China, NIO, The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen),School of Science and Engineering, Future Intelligent Network Research Institute,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel training strategy called SupFusion, which provides an auxiliary feature level supervision for effective LiDAR-Camera fusion and significantly boosts detection performance. Our strategy involves a data enhancement method named Polar Sampling, which densifies sparse objects and trains an assistant model to generate high-quality features as the supervision. These features are then used to train the LiDAR-Camera fusion model, where the fusion feature is optimized to simulate the generated high-quality features. Furthermore, we propose a simple yet effective deep fusion module, which contiguously gains superior performance compared with previous fusion methods with SupFusion strategy. In such a manner, our proposal shares the following advantages. Firstly, SupFusion introduces auxiliary feature-level supervision which could boost LiDAR-Camera detection performance without introducing extra inference costs. Secondly, the proposed deep fusion could continuously improve the detector's abilities. Our proposed SupFusion and deep fusion module is plug-and-play, we make extensive experiments to demonstrate its effectiveness. Specifically, we gain around 2% 3D mAP improvements on KITTI benchmark based on multiple LiDAR-Camera 3D detectors.

</details>

### GraphAlign: Enhancing Accurate Feature Alignment by Graph matching for Multi-Modal 3D Object Detection.
- **链接**: [arXiv:2310.08261](https://arxiv.org/abs/2310.08261) · 📚 被引 68
- **作者**: Ziying Song, Haiyue Wei, Lin Bai, Lei Yang, Caiyan Jia
- **🏷️ 机构**: Beijing Jiaotong University,School of Computer and Information Technology, Hebei University of Science and Technology,School of Information Science and Engineering, Tsinghua University,State Key Laboratory of Automotive Safety and Energy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR and cameras are complementary sensors for 3D object detection in autonomous driving. However, it is challenging to explore the unnatural interaction between point clouds and images, and the critical factor is how to conduct feature alignment of heterogeneous modalities. Currently, many methods achieve feature alignment by projection calibration only, without considering the problem of coordinate conversion accuracy errors between sensors, leading to sub-optimal performance. In this paper, we present GraphAlign, a more accurate feature alignment strategy for 3D object detection by graph matching. Specifically, we fuse image features from a semantic segmentation encoder in the image branch and point cloud features from a 3D Sparse CNN in the LiDAR branch. To save computation, we construct the nearest neighbor relationship by calculating Euclidean distance within the subspaces that are divided into the point cloud features. Through the projection calibration between the image and point cloud, we project the nearest neighbors of point cloud features onto the image features. Then by matching the nearest neighbors with a single point cloud to multiple images, we search for a more appropriate feature alignment. In addition, we provide a self-attention module to enhance the weights of significant relations to fine-tune the feature alignment between heterogeneous modalities. Extensive experiments on nuScenes benchmark demonstrate the effectiveness and efficiency of our GraphAlign.

</details>

### Not Every Side Is Equal: Localization Uncertainty Estimation for Semi-Supervised 3D Object Detection.
- **链接**: [arXiv:2312.10390](https://arxiv.org/abs/2312.10390) · 📚 被引 10
- **作者**: Chuxin Wang, Wenfei Yang, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised 3D object detection from point cloud aims to train a detector with a small number of labeled data and a large number of unlabeled data. The core of existing methods lies in how to select high-quality pseudo-labels using the designed quality evaluation criterion. However, these methods treat each pseudo bounding box as a whole and assign equal importance to each side during training, which is detrimental to model performance due to many sides having poor localization quality. Besides, existing methods filter out a large number of low-quality pseudo-labels, which also contain some correct regression values that can help with model training. To address the above issues, we propose a side-aware framework for semi-supervised 3D object detection consisting of three key designs: a 3D bounding box parameterization method, an uncertainty estimation module, and a pseudo-label selection strategy. These modules work together to explicitly estimate the localization quality of each side and assign different levels of importance during the training phase. Extensive experiment results demonstrate that the proposed method can consistently outperform baseline models under different scenes and evaluation criteria. Moreover, our method achieves state-of-the-art performance on three datasets with different labeled ratios.

</details>

### Towards Universal LiDAR-Based 3D Object Detection by Multi-Domain Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00796) · 📚 被引 9
- **作者**: Guile Wu, Tongtong Cao, Bingbing Liu, Xingxin Chen, Yuan Ren
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab
- **会议**: ICCV 2023

### CoIn: Contrastive Instance Feature Mining for Outdoor 3D Object Detection with Very Limited Annotations.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00575) · 📚 被引 31
- **作者**: Qiming Xia, Jinhao Deng, Chenglu Wen, Hai Wu, Shaoshuai Shi, Xin Li et al.
- **🏷️ 机构**: Xiamen University, Max-Planck Institute, Texas A&#x0026;M University
- **会议**: ICCV 2023

### SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection.
- **链接**: [arXiv:2304.14340](https://arxiv.org/abs/2304.14340) · 📚 被引 132
- **作者**: Yichen Xie, Chenfeng Xu, Marie-Julie Rakotosaona, Patrick Rim, Federico Tombari, Kurt Keutzer et al.
- **🏷️ 机构**: University of California,Berkeley, Google, California Institute of Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> By identifying four important components of existing LiDAR-camera 3D object detection methods (LiDAR and camera candidates, transformation, and fusion outputs), we observe that all existing methods either find dense candidates or yield dense representations of scenes. However, given that objects occupy only a small part of a scene, finding dense candidates and generating dense representations is noisy and inefficient. We propose SparseFusion, a novel multi-sensor 3D detection method that exclusively uses sparse candidates and sparse representations. Specifically, SparseFusion utilizes the outputs of parallel detectors in the LiDAR and camera modalities as sparse candidates for fusion. We transform the camera candidates into the LiDAR coordinate space by disentangling the object representations. Then, we can fuse the multi-modality candidates in a unified 3D space by a lightweight self-attention module. To mitigate negative transfer between modalities, we propose novel semantic and geometric cross-modality transfer modules that are applied prior to the modality-specific detectors. SparseFusion achieves state-of-the-art performance on the nuScenes benchmark while also running at the fastest speed, even outperforming methods with stronger backbones. We perform extensive experiments to demonstrate the effectiveness and efficiency of our modules and overall method pipeline. Our code will be made publicly available at https://github.com/yichen928/SparseFusion.

</details>

### MonoNeRD: NeRF-like Representations for Monocular 3D Object Detection.
- **链接**: [arXiv:2308.09421](https://arxiv.org/abs/2308.09421) · 📚 被引 40
- **作者**: Junkai Xu, Liang Peng, Haoran Chen, Hao Li, Wei Qian, Ke Li et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD &#x0026; CG, FABU Inc, Fullong Inc
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the field of monocular 3D detection, it is common practice to utilize scene geometric clues to enhance the detector's performance. However, many existing works adopt these clues explicitly such as estimating a depth map and back-projecting it into 3D space. This explicit methodology induces sparsity in 3D representations due to the increased dimensionality from 2D to 3D, and leads to substantial information loss, especially for distant and occluded objects. To alleviate this issue, we propose MonoNeRD, a novel detection framework that can infer dense 3D geometry and occupancy. Specifically, we model scenes with Signed Distance Functions (SDF), facilitating the production of dense 3D representations. We treat these representations as Neural Radiance Fields (NeRF) and then employ volume rendering to recover RGB images and depth maps. To the best of our knowledge, this work is the first to introduce volume rendering for M3D, and demonstrates the potential of implicit reconstruction for image-based 3D perception. Extensive experiments conducted on the KITTI-3D benchmark and Waymo Open Dataset demonstrate the effectiveness of MonoNeRD. Codes are available at https://github.com/cskkxjk/MonoNeRD.

</details>

### Cross Modal Transformer: Towards Fast and Robust 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01675) · 📚 被引 173
- **作者**: Junjie Yan, Yingfei Liu, Jianjian Sun, Fan Jia, Shuailin Li, Tiancai Wang et al.
- **🏷️ 机构**: MEGVII Technology
- **会议**: ICCV 2023

### MonoDETR: Depth-guided Transformer for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00840) · 📚 被引 190
- **作者**: Renrui Zhang, Han Qiu, Tai Wang, Ziyu Guo, Ziteng Cui, Yu Qiao et al.
- **🏷️ 机构**: CUHK MMLab, Shanghai Artificial Intelligence Laboratory
- **会议**: ICCV 2023

### A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00769) · 📚 被引 24
- **作者**: Dingyuan Zhang, Dingkang Liang, Zhikang Zou, Jingyu Li, Xiaoqing Ye, Zhe Liu et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Baidu Inc.,China
- **会议**: ICCV 2023

### An Empirical Analysis of Range for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00440) · 📚 被引 10
- **作者**: Neehar Peri, Mengtian Li, Benjamin Wilson, Yu-Xiong Wang, James Hays, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University, Georgia Institute of Technology, University of Illinois Urbana-Champaign
- **会议**: ICCV 2023

### SceneRF: Self-Supervised Monocular 3D Scene Reconstruction with Radiance Fields.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00861) · 📚 被引 50
- **作者**: Anh-Quan Cao, Raoul de Charette
- **🏷️ 机构**: Inria
- **会议**: ICCV 2023

### JOTR: 3D Joint Contrastive Learning with Transformers for Occluded Human Mesh Recovery.
- **链接**: [arXiv:2307.16377](https://arxiv.org/abs/2307.16377) · 📚 被引 27
- **作者**: Jiahao Li, Zongxin Yang, Xiaohan Wang, Jianxin Ma, Chang Zhou, Yi Yang
- **🏷️ 机构**: Zhejiang University,ReLER, CCAI, Alibaba Group,DAMO Academy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we focus on the problem of 3D human mesh recovery from a single image under obscured conditions. Most state-of-the-art methods aim to improve 2D alignment technologies, such as spatial averaging and 2D joint sampling. However, they tend to neglect the crucial aspect of 3D alignment by improving 3D representations. Furthermore, recent methods struggle to separate the target human from occlusion or background in crowded scenes as they optimize the 3D space of target human with 3D joint coordinates as local supervision. To address these issues, a desirable method would involve a framework for fusing 2D and 3D features and a strategy for optimizing the 3D space globally. Therefore, this paper presents 3D JOint contrastive learning with TRansformers (JOTR) framework for handling occluded 3D human mesh recovery. Our method includes an encoder-decoder transformer architecture to fuse 2D and 3D representations for achieving 2D$\&$3D aligned results in a coarse-to-fine manner and a novel 3D joint contrastive learning approach for adding explicitly global supervision for the 3D feature space. The contrastive learning approach includes two contrastive losses: joint-to-joint contrast for enhancing the similarity of semantically similar voxels (i.e., human joints), and joint-to-non-joint contrast for ensuring discrimination from others (e.g., occlusions and background). Qualitative and quantitative analyses demonstrate that our method outperforms state-of-the-art competitors on both occlusion-specific and standard benchmarks, significantly improving the reconstruction of occluded humans.

</details>

### Beyond the limitation of monocular 3D detector via knowledge distillation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00833) · 📚 被引 5
- **作者**: Yiran Yang, Dongshuo Yin, Xuee Rong, Xian Sun, Wenhui Diao, Xinming Li
- **🏷️ 机构**: Chinese Academy of Sciences,Key Laboratory of Network Information System Technology, Aerospace Information Research Institute
- **会议**: ICCV 2023

### Exploring Active 3D Object Detection from a Generalization Perspective.
- **链接**: [出版页](https://openreview.net/forum?id=2RwXVje1rAh)
- **作者**: Yadan Luo, Zhuoxiao Chen, Zijian Wang, Xin Yu, Zi Huang, Mahsa Baktashmotlagh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### RangePerception: Taming LiDAR Range View for Efficient and Accurate 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fb8e52adcd9b59bad73f109c53afc43a-Abstract-Conference.html)
- **作者**: Yeqi Bai, Ben Fei, Youquan Liu, Tao Ma, Yuenan Hou, Botian Shi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Depth-discriminative Metric Learning for Monocular 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fda257e65f46e21dbc117b20fd0aba3c-Abstract-Conference.html)
- **作者**: Wonhyeok Choi, Mingyu Shin, Sunghoon Im
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### 3D Copy-Paste: Physically Plausible Object Insertion for Monocular 3D Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/370fa2e691f57eb319bc263a07dad4a5-Abstract-Conference.html)
- **作者**: Yunhao Ge, Hong-Xing Yu, Cheng Zhao, Yuliang Guo, Xinyu Huang, Liu Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Diffusion-SS3D: Diffusion Model for Semi-supervised 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/99786eed5e16920f908572fb00e151c3-Abstract-Conference.html)
- **作者**: Cheng-Ju Ho, Chen-Hsuan Tai, Yen-Yu Lin, Ming-Hsuan Yang, Yi-Hsuan Tsai
- **🏷️ 机构**: UC Merced
- **会议**: NeurIPS 2023

### Query-based Temporal Fusion with Explicit Motion for 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/ef0dcb44a47185f5bacac62571f6e920-Abstract-Conference.html)
- **作者**: Jinghua Hou, Zhe Liu, Dingkang Liang, Zhikang Zou, Xiaoqing Ye, Xiang Bai
- **🏷️ 机构**: HUAST
- **会议**: NeurIPS 2023

### STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5d8c01de2dc698c54201c1c7d0b86974-Abstract-Conference.html)
- **作者**: Sujin Jang, Dae Ung Jo, Sung Ju Hwang, Dongwook Lee, Daehyun Ji
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### MonoUNI: A Unified Vehicle and Infrastructure-side Monocular 3D Object Detection Network with Sufficient Depth Clues.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2703a0e3c2b33506295a77762338cf24-Abstract-Conference.html)
- **作者**: Jinrang Jia, Zhenjia Li, Yifeng Shi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Flow-Based Feature Fusion for Vehicle-Infrastructure Cooperative 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6ca5d2665de83394f437dad0c3746907-Abstract-Conference.html)
- **作者**: Haibao Yu, Yingjuan Tang, Enze Xie, Jilei Mao, Ping Luo, Zaiqing Nie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### HEDNet: A Hierarchical Encoder-Decoder Network for 3D Object Detection in Point Clouds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a64e641fa00a7eb9500cb7e1835d0495-Abstract-Conference.html)
- **作者**: Gang Zhang, Junnan Chen, Guohuan Gao, Jianmin Li, Xiaolin Hu
- **🏷️ 机构**: Tsinghua
- **会议**: NeurIPS 2023

### Unleash the Potential of Image Branch for Cross-modal 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a1f0c0cd6caaa4863af5f12608edf63e-Abstract-Conference.html)
- **作者**: Yifan Zhang, Qijian Zhang, Junhui Hou, Yixuan Yuan, Guoliang Xing
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Differentiable Registration of Images and LiDAR Point Clouds with VoxelPoint-to-Pixel Matching.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a0a53fefef4c2ad72d5ab79703ba70cb-Abstract-Conference.html)
- **作者**: Junsheng Zhou, Baorui Ma, Wenyuan Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- ConQueR: Query Contrast Voxel-DETR for 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Are We Ready for Vision-Centric Driving Streaming Perception? The ASAP Benchmark. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Surround-View Vision-based 3D Detection for Autonomous Driving: A Survey. → [bev](../bev/Guideline%202023.md)
- 3D Video Object Detection with Learnable Object-Centric Global Optimization. → [object-detection](../object-detection/Guideline%202023.md)
- Curricular Object Manipulation in LiDAR-based Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Viewpoint Equivariance for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Dynamic Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- PiMAE: Point Cloud and Image Interactive Masked Autoencoders for 3D Object Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [object-detection](../object-detection/Guideline%202023.md)
- Benchmarking Robustness of 3D Object Detection to Common Corruptions in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- NeRF-RPN: A general framework for object detection in NeRFs. → [object-detection](../object-detection/Guideline%202023.md)
- X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [object-detection](../object-detection/Guideline%202023.md)
- CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [bev](../bev/Guideline%202023.md)
- Collaboration Helps Camera Overtake LiDAR in 3D Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- FrustumFormer: Adaptive Instance-aware Resampling for Multi-view 3D Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [multimodal](../multimodal/Guideline%202023.md)
- Predict to Detect: Prediction-guided 3D Object Detection using Sequential Images. → [bev](../bev/Guideline%202023.md)
- GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds. → [bev](../bev/Guideline%202023.md)
- SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. → [bev](../bev/Guideline%202023.md)
- 3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- ImGeoNet: Image-induced Geometry-aware Voxel Representation for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Pixel-Aligned Recurrent Queries for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- NeRF-Det: Learning Geometry-Aware Volumetric Representation for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [network-pruning](../network-pruning/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection. → [bev](../bev/Guideline%202023.md)
- UniSeg: A Unified Multi-Modal LiDAR Segmentation Network and the OpenPCSeg Codebase. → [multimodal](../multimodal/Guideline%202023.md)
- MBPTrack: Improving 3D Point Cloud Tracking with Memory networks and Box Priors. → [tracking](../tracking/Guideline%202023.md)
- Bird's-Eye-View Scene Graph for Vision-Language Navigation. → [vlm](../vlm/Guideline%202023.md)
- OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction. → [network-pruning](../network-pruning/Guideline%202023.md)
- Unsupervised 3D Perception with 2D Vision-Language Distillation for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Unsupervised Domain Adaptation for Self-Driving from Past Traversal Features. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection. → [multimodal](../multimodal/Guideline%202023.md)
- Time Will Tell: New Outlooks and A Baseline for Temporal Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- CoDA: Collaborative Novel Box Discovery and Cross-modal Alignment for Open-vocabulary 3D Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- CluB: Cluster Meets BEV for LiDAR-Based 3D Object Detection. → [bev](../bev/Guideline%202023.md)
<!-- COMPLETE v1 papers=82 -->
