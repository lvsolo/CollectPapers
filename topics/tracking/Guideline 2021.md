# Tracking — 2021 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CAPTRA: CAtegory-level Pose Tracking for Rigid and Articulated Objects from Point Clouds.
- **链接**: [arXiv:2104.03437](https://arxiv.org/abs/2104.03437) · 📚 被引 95
- **作者**: Yijia Weng, He Wang, Qiang Zhou, Yuzhe Qin, Yueqi Duan, Qingnan Fan et al.
- **🏷️ 机构**: Peking University,CFCS, Shandong University, UCSD
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we tackle the problem of category-level online pose tracking of objects from point cloud sequences. For the first time, we propose a unified framework that can handle 9DoF pose tracking for novel rigid object instances as well as per-part pose tracking for articulated objects from known categories. Here the 9DoF pose, comprising 6D pose and 3D size, is equivalent to a 3D amodal bounding box representation with free 6D pose. Given the depth point cloud at the current frame and the estimated pose from the last frame, our novel end-to-end pipeline learns to accurately update the pose. Our pipeline is composed of three modules: 1) a pose canonicalization module that normalizes the pose of the input depth point cloud; 2) RotationNet, a module that directly regresses small interframe delta rotations; and 3) CoordinateNet, a module that predicts the normalized coordinates and segmentation, enabling analytical computation of the 3D size and translation. Leveraging the small pose regime in the pose-canonicalized point clouds, our method integrates the best of both worlds by combining dense coordinate prediction and direct rotation regression, thus yielding an end-to-end differentiable pipeline optimized for 9DoF pose accuracy (without using non-differentiable RANSAC). Our extensive experiments demonstrate that our method achieves new state-of-the-art performance on category-level rigid object pose (NOCS-REAL275) and articulated object pose benchmarks (SAPIEN, BMVC) at the fastest FPS ~12.

</details>

### Box-Aware Feature Enhancement for Single Object Tracking on Point Clouds.
- **链接**: [arXiv:2108.04728](https://arxiv.org/abs/2108.04728) · 📚 被引 110
- **作者**: Chaoda Zheng, Xu Yan, Jiantao Gao, Weibing Zhao, Wei Zhang, Zhen Li et al.
- **🏷️ 机构**: The Chinese University of Hong Kong (Shenzhen),Shenzhen Research Institute of Big Data, Shanghai University,Research Institute of USV Engineering, Baidu Inc
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current 3D single object tracking approaches track the target based on a feature comparison between the target template and the search area. However, due to the common occlusion in LiDAR scans, it is non-trivial to conduct accurate feature comparisons on severe sparse and incomplete shapes. In this work, we exploit the ground truth bounding box given in the first frame as a strong cue to enhance the feature description of the target object, enabling a more accurate feature comparison in a simple yet effective way. In particular, we first propose the BoxCloud, an informative and robust representation, to depict an object using the point-to-box relation. We further design an efficient box-aware feature fusion module, which leverages the aforementioned BoxCloud for reliable feature matching and embedding. Integrating the proposed general components into an existing model P2B, we construct a superior box-aware tracker (BAT). Experiments confirm that our proposed BAT outperforms the previous state-of-the-art by a large margin on both KITTI and NuScenes benchmarks, achieving a 15.2% improvement in terms of precision while running ~20% faster.

</details>

### Assignment-Space-based Multi-Object Tracking and Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01334) · 📚 被引 9
- **作者**: Anwesa Choudhuri, Girish Chowdhary, Alexander G. Schwing
- **🏷️ 机构**: University of Illinois at Urbana-Champaign
- **会议**: ICCV 2021

### Continuous Copy-Paste for One-stage Multi-object Tracking and Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01504) · 📚 被引 19
- **作者**: Zhenbo Xu, Ajin Meng, Zhenbo Shi, Wei Yang, Zhi Chen, Liusheng Huang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2021

### Learning Spatio-Temporal Transformer for Visual Tracking.
- **链接**: [arXiv:2103.17154](https://arxiv.org/abs/2103.17154) · [代码](https://github.com/researchmm/Stark)
- **作者**: Bin Yan, Houwen Peng, Jianlong Fu, Dong Wang, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multiple Object Tracking (MOT) has witnessed remarkable advances in recent years. However, existing studies dominantly request prior knowledge of the tracking target, and hence may not generalize well to unseen categories. In contrast, Generic Multiple Object Tracking (GMOT), which requires little prior information about the target, is largely under-explored. In this paper, we make contributions to boost the study of GMOT in three aspects. First, we construct the first public GMOT dataset, dubbed GMOT-40, which contains 40 carefully annotated sequences evenly distributed among 10 object categories. In addition, two tracking protocols are adopted to evaluate different characteristics of tracking algorithms. Second, by noting the lack of devoted tracking algorithms, we have designed a series of baseline GMOT algorithms. Third, we perform a thorough evaluation on GMOT-40, involving popular MOT algorithms (with necessary modifications) and the proposed baselines. We will release the GMOT-40 benchmark, the evaluation results, as well as the baseline algorithm to the public upon the publication of the paper.

</details>

</details>

### Video Annotation for Visual Tracking via Selection and Refinement.
- **链接**: [arXiv:2108.03821](https://arxiv.org/abs/2108.03821) · 📚 被引 9
- **作者**: Kenan Dai, Jie Zhao, Lijun Wang, Dong Wang, Jianhua Li, Huchuan Lu et al.
- **🏷️ 机构**: Dalian University of Technology,China, CSA Intellicloud Ltd, Remark Holdings
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In multi-object tracking, the tracker maintains in its memory the appearance and motion information for each object in the scene. This memory is utilized for finding matches between tracks and detections and is updated based on the matching result. Many approaches model each target in isolation and lack the ability to use all the targets in the scene to jointly update the memory. This can be problematic when there are similar looking objects in the scene. In this paper, we solve the problem of simultaneously considering all tracks during memory updating, with only a small spatial overhead, via a novel multi-track pooling module. We additionally propose a training strategy adapted to multi-track pooling which generates hard tracking episodes online. We show that the combination of these innovations results in a strong discriminative appearance model, enabling the use of greedy data association to achieve online tracking performance. Our experiments demonstrate real-time, state-of-the-art performance on public multi-object tracking (MOT) datasets.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking from RGB-D video sequences is a challenging problem due to the combination of changing viewpoints, motion, and occlusions over time. We observe that having the complete geometry of objects aids in their tracking, and thus propose to jointly infer the complete geometry of objects as well as track them, for rigidly moving objects over time. Our key insight is that inferring the complete geometry of the objects significantly helps in tracking. By hallucinating unseen regions of objects, we can obtain additional correspondences between the same instance, thus providing robust tracking even under strong change of appearance. From a sequence of RGB-D frames, we detect objects in each frame and learn to predict their complete object geometry as well as a dense correspondence mapping into a canonical space. This allows us to derive 6DoF poses for the objects in each frame, along with their correspondence between frames, providing robust object tracking across the RGB-D sequence. Experiments on both synthetic and real-world RGB-D data demonstrate that we achieve state-of-the-art performance on dynamic object tracking. Furthermore, we show that our object completion significantly helps tracking, providing an improvement of $6.5\%$ in mean MOTA.

</details>

> Vehicle tracking is an essential task in the multi-object tracking (MOT) field. A distinct characteristic in vehicle tracking is that the trajectories of vehicles are fairly smooth in both the world coordinate and the image coordinate. Hence, models that capture motion consistencies are of high necessity. However, tracking with the standalone motion-based trackers is quite challenging because targets could get lost easily due to limited information, detection error and occlusion. Leveraging appearance information to assist object re-identification could resolve this challenge to some extent. However, doing so requires extra computation while appearance information is sensitive to occlusion as well. In this paper, we try to explore the significance of motion patterns for vehicle tracking without appearance information. We propose a novel approach that tackles the association issue for long-term tracking with the exclusive fully-exploited motion information. We address the tracklet embedding issue with the proposed reconstruct-to-embed strategy based on deep graph convolutional neural networks (GCN). Comprehensive experiments on the KITTI-car tracking dataset and UA-Detrac dataset show that the proposed method, though without appearance information, could achieve competitive performance with the state-of-the-art (SOTA) trackers. The source code will be available at https://github.com/GaoangW/LGMTracker.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent trend in multiple object tracking (MOT) is heading towards leveraging deep learning to boost the tracking performance. However, it is not trivial to solve the data-association problem in an end-to-end fashion. In this paper, we propose a novel proposal-based learnable framework, which models MOT as a proposal generation, proposal scoring and trajectory inference paradigm on an affinity graph. This framework is similar to the two-stage object detector Faster RCNN, and can solve the MOT problem in a data-driven way. For proposal generation, we propose an iterative graph clustering method to reduce the computational cost while maintaining the quality of the generated proposals. For proposal scoring, we deploy a trainable graph-convolutional-network (GCN) to learn the structural patterns of the generated proposals and rank them according to the estimated quality scores. For trajectory inference, a simple deoverlapping strategy is adopted to generate tracking output while complying with the constraints that no detection can be assigned to more than one track. We experimentally demonstrate that the proposed method achieves a clear performance improvement in both MOTA and IDF1 with respect to previous state-of-the-art on two public benchmarks. Our code is available at https://github.com/daip13/LPC_MOT.git.

</details>

### Learn to Match: Automatic Matching Network Design for Visual Tracking.
- **链接**: [arXiv:2108.00803](https://arxiv.org/abs/2108.00803) · [代码](https://github.com/JudasDie/SOTS) · 📚 被引 241
- **作者**: Zhipeng Zhang, Yihao Liu, Xiao Wang, Bing Li, Weiming Hu
- **🏷️ 机构**: Chinese Academy of Sciences,National Laboratory of Pattern Recognition, Institute of Automation, University of Chinese Academy of Sciences,School of AI, Peng Cheng Laboratory
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern online multiple object tracking (MOT) methods usually focus on two directions to improve tracking performance. One is to predict new positions in an incoming frame based on tracking information from previous frames, and the other is to enhance data association by generating more discriminative identity embeddings. Some works combined both directions within one framework but handled them as two individual tasks, thus gaining little mutual benefits. In this paper, we propose a novel unified model with synergy between position prediction and embedding association. The two tasks are linked by temporal-aware target attention and distractor attention, as well as identity-aware memory aggregation model. Specifically, the attention modules can make the prediction focus more on targets and less on distractors, therefore more reliable embeddings can be extracted accordingly for association. On the other hand, such reliable embeddings can boost identity-awareness through memory aggregation, hence strengthen attention modules and suppress drifts. In this way, the synergy between position prediction and embedding association is achieved, which leads to strong robustness to occlusions. Extensive experiments demonstrate the superiority of our proposed model over a wide range of existing methods on MOTChallenge benchmarks. Our code and models are publicly available at https://github.com/songguocode/TADAM.

</details>

### Learnable Graph Matching: Incorporating Graph Partitioning With Deep Feature Learning for Multiple Object Tracking.
- **链接**: [arXiv:2103.16178](https://arxiv.org/abs/2103.16178) · [代码](https://github.com/jiaweihe1996/GMTracker) · 📚 被引 124
- **作者**: Jiawei He, Zehao Huang, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data association across frames is at the core of Multiple Object Tracking (MOT) task. This problem is usually solved by a traditional graph-based optimization or directly learned via deep learning. Despite their popularity, we find some points worth studying in current paradigm: 1) Existing methods mostly ignore the context information among tracklets and intra-frame detections, which makes the tracker hard to survive in challenging cases like severe occlusion. 2) The end-to-end association methods solely rely on the data fitting power of deep neural networks, while they hardly utilize the advantage of optimization-based assignment methods. 3) The graph-based optimization methods mostly utilize a separate neural network to extract features, which brings the inconsistency between training and inference. Therefore, in this paper we propose a novel learnable graph matching method to address these issues. Briefly speaking, we model the relationships between tracklets and the intra-frame detections as a general undirected graph. Then the association problem turns into a general graph matching between tracklet graph and detection graph. Furthermore, to make the optimization end-to-end differentiable, we relax the original graph matching into continuous quadratic programming and then incorporate the training of it into a deep graph network with the help of the implicit function theorem. Lastly, our method GMTracker, achieves state-of-the-art performance on several standard MOT datasets. Our code will be available at https://github.com/jiaweihe1996/GMTracker .

</details>

### Quasi-Dense Similarity Learning for Multiple Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Pang_Quasi-Dense_Similarity_Learning_for_Multiple_Object_Tracking_CVPR_2021_paper.html) · 📚 被引 426
- **作者**: Jiangmiao Pang, Linlu Qiu, Xia Li, Haofeng Chen, Qi Li, Trevor Darrell et al.
- **🏷️ 机构**: Zhejiang University, Georgia Institute of Technology, ETH Z&#x00FC;rich
- **会议**: CVPR 2021

### Probabilistic Tracklet Scoring and Inpainting for Multiple Object Tracking.
- **链接**: [arXiv:2012.02337](https://arxiv.org/abs/2012.02337) · 📚 被引 87
- **作者**: Fatemeh Sadat Saleh, Sadegh Aliakbarian, Hamid Rezatofighi, Mathieu Salzmann, Stephen Gould
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent advances in multiple object tracking (MOT), achieved by joint detection and tracking, dealing with long occlusions remains a challenge. This is due to the fact that such techniques tend to ignore the long-term motion information. In this paper, we introduce a probabilistic autoregressive motion model to score tracklet proposals by directly measuring their likelihood. This is achieved by training our model to learn the underlying distribution of natural tracklets. As such, our model allows us not only to assign new detections to existing tracklets, but also to inpaint a tracklet when an object has been lost for a long time, e.g., due to occlusion, by sampling tracklets so as to fill the gap caused by misdetections. Our experiments demonstrate the superiority of our approach at tracking objects in challenging sequences; it outperforms the state of the art in most standard MOT metrics on multiple MOT benchmark datasets, including MOT16, MOT17, and MOT20.

</details>

### SiamMOT: Siamese Multi-Object Tracking.
- **链接**: [arXiv:2105.11595](https://arxiv.org/abs/2105.11595) · [代码](https://github.com/amazon-research/siam-mot) · 📚 被引 143
- **作者**: Bing Shuai, Andrew G. Berneshawi, Xinyu Li, Davide Modolo, Joseph Tighe
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we focus on improving online multi-object tracking (MOT). In particular, we introduce a region-based Siamese Multi-Object Tracking network, which we name SiamMOT. SiamMOT includes a motion model that estimates the instance's movement between two frames such that detected instances are associated. To explore how the motion modelling affects its tracking capability, we present two variants of Siamese tracker, one that implicitly models motion and one that models it explicitly. We carry out extensive quantitative experiments on three different MOT datasets: MOT17, TAO-person and Caltech Roadside Pedestrians, showing the importance of motion modelling for MOT and the ability of SiamMOT to substantially outperform the state-of-the-art. Finally, SiamMOT also outperforms the winners of ACM MM'20 HiEve Grand Challenge on HiEve dataset. Moreover, SiamMOT is efficient, and it runs at 17 FPS for 720P videos on a single modern GPU. Codes are available in \url{https://github.com/amazon-research/siam-mot}.

</details>

### Multiple Object Tracking With Correlation Learning.
- **链接**: [arXiv:2104.03541](https://arxiv.org/abs/2104.03541)
- **作者**: Qiang Wang, Yun Zheng, Pan Pan, Yinghui Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works have shown that convolutional networks have substantially improved the performance of multiple object tracking by simultaneously learning detection and appearance features. However, due to the local perception of the convolutional network structure itself, the long-range dependencies in both the spatial and temporal cannot be obtained efficiently. To incorporate the spatial layout, we propose to exploit the local correlation module to model the topological relationship between targets and their surrounding environment, which can enhance the discriminative power of our model in crowded scenes. Specifically, we establish dense correspondences of each spatial location and its context, and explicitly constrain the correlation volumes through self-supervised learning. To exploit the temporal context, existing approaches generally utilize two or more adjacent frames to construct an enhanced feature representation, but the dynamic motion scene is inherently difficult to depict via CNNs. Instead, our paper proposes a learnable correlation operator to establish frame-to-frame matches over convolutional feature maps in the different layers to align and propagate temporal context. With extensive experimental results on the MOT datasets, our approach demonstrates the effectiveness of correlation learning with the superior performance and obtains state-of-the-art MOTA of 76.5% and IDF1 of 73.6% on MOT17.

</details>

### Transformer Meets Tracker: Exploiting Temporal Context for Robust Visual Tracking.
- **链接**: [arXiv:2103.11681](https://arxiv.org/abs/2103.11681) · 📚 被引 805
- **作者**: Ning Wang, Wengang Zhou, Jie Wang, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In video object tracking, there exist rich temporal contexts among successive frames, which have been largely overlooked in existing trackers. In this work, we bridge the individual video frames and explore the temporal contexts across them via a transformer architecture for robust object tracking. Different from classic usage of the transformer in natural language processing tasks, we separate its encoder and decoder into two parallel branches and carefully design them within the Siamese-like tracking pipelines. The transformer encoder promotes the target templates via attention-based feature reinforcement, which benefits the high-quality tracking model generation. The transformer decoder propagates the tracking cues from previous templates to the current frame, which facilitates the object searching process. Our transformer-assisted tracking framework is neat and trained in an end-to-end manner. With the proposed transformer, a simple Siamese matching approach is able to outperform the current top-performing trackers. By combining our transformer with the recent discriminative tracking pipeline, our method sets several new state-of-the-art records on prevalent tracking benchmarks.

</details>

### STMTrack: Template-Free Visual Tracking With Space-Time Memory Networks.
- **链接**: [arXiv:2104.00324](https://arxiv.org/abs/2104.00324) · [代码](https://github.com/fzh0917/STMTrack) · 📚 被引 350
- **作者**: Zhihong Fu, Qingjie Liu, Zehua Fu, Yunhong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Boosting performance of the offline trained siamese trackers is getting harder nowadays since the fixed information of the template cropped from the first frame has been almost thoroughly mined, but they are poorly capable of resisting target appearance changes. Existing trackers with template updating mechanisms rely on time-consuming numerical optimization and complex hand-designed strategies to achieve competitive performance, hindering them from real-time tracking and practical applications. In this paper, we propose a novel tracking framework built on top of a space-time memory network that is competent to make full use of historical information related to the target for better adapting to appearance variations during tracking. Specifically, a novel memory mechanism is introduced, which stores the historical information of the target to guide the tracker to focus on the most informative regions in the current frame. Furthermore, the pixel-level similarity computation of the memory network enables our tracker to generate much more accurate bounding boxes of the target. Extensive experiments and comparisons with many competitive trackers on challenging large-scale benchmarks, OTB-2015, TrackingNet, GOT-10k, LaSOT, UAV123, and VOT2018, show that, without bells and whistles, our tracker outperforms all previous state-of-the-art real-time methods while running at 37 FPS. The code is available at https://github.com/fzh0917/STMTrack.

</details>

### TesseTrack: End-to-End Learnable Multi-Person Articulated 3D Pose Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Reddy_TesseTrack_End-to-End_Learnable_Multi-Person_Articulated_3D_Pose_Tracking_CVPR_2021_paper.html) · 📚 被引 104
- **作者**: N. Dinesh Reddy, Laurent Guigues, Leonid Pishchulin, Jayan Eledath, Srinivasa G. Narasimhan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

## 跨领域论文（完整笔记在其他领域）

- Exploring Simple 3D Multi-Object Tracking for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
