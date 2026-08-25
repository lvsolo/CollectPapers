# Tracking — 2021 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GMOT-40: A Benchmark for Generic Multiple Object Tracking.
- **链接**: [arXiv:2011.11858](https://arxiv.org/abs/2011.11858) · 📚 被引 38
- **作者**: Hexin Bai, Wensheng Cheng, Peng Chu, Juehuan Liu, Kai Zhang, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Multiple Object Tracking (MOT) has witnessed remarkable advances in recent years. However, existing studies dominantly request prior knowledge of the tracking target, and hence may not generalize well to unseen categories. In contrast, Generic Multiple Object Tracking (GMOT), which requires little prior information about the target, is largely under-explored. In this paper, we make contributions to boost the study of GMOT in three aspects. First, we construct the first public GMOT dataset, dubbed GMOT-40, which contains 40 carefully annotated sequences evenly distributed among 10 object categories. In addition, two tracking protocols are adopted to evaluate different characteristics of tracking algorithms. Second, by noting the lack of devoted tracking algorithms, we have designed a series of baseline GMOT algorithms. Third, we perform a thorough evaluation on GMOT-40, involving popular MOT algorithms (with necessary modifications) and the proposed baselines. We will release the GMOT-40 benchmark, the evaluation results, as well as the baseline algorithm to the public upon the publication of the paper.

### Improving Multiple Object Tracking With Single Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zheng_Improving_Multiple_Object_Tracking_With_Single_Object_Tracking_CVPR_2021_paper.html)
- **作者**: Linyu Zheng, Ming Tang, Yingying Chen, Guibo Zhu, Jinqiao Wang, Hanqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Discriminative Appearance Modeling With Multi-Track Pooling for Real-Time Multi-Object Tracking.
- **链接**: [arXiv:2101.12159](https://arxiv.org/abs/2101.12159) · 📚 被引 73
- **作者**: Chanho Kim, Fuxin Li, Mazen Alotaibi, James M. Rehg
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > In multi-object tracking, the tracker maintains in its memory the appearance and motion information for each object in the scene. This memory is utilized for finding matches between tracks and detections and is updated based on the matching result. Many approaches model each target in isolation and lack the ability to use all the targets in the scene to jointly update the memory. This can be problematic when there are similar looking objects in the scene. In this paper, we solve the problem of simultaneously considering all tracks during memory updating, with only a small spatial overhead, via a novel multi-track pooling module. We additionally propose a training strategy adapted to multi-track pooling which generates hard tracking episodes online. We show that the combination of these innovations results in a strong discriminative appearance model, enabling the use of greedy data association to achieve online tracking performance. Our experiments demonstrate real-time, state-of-the-art performance on public multi-object tracking (MOT) datasets.

### Seeing Behind Objects for 3D Multi-Object Tracking in RGB-D Sequences.
- **链接**: [arXiv:2012.08197](https://arxiv.org/abs/2012.08197) · 📚 被引 18
- **作者**: Norman Müller, Yu-Shiang Wong, Niloy J. Mitra, Angela Dai, Matthias Nießner
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Multi-object tracking from RGB-D video sequences is a challenging problem due to the combination of changing viewpoints, motion, and occlusions over time. We observe that having the complete geometry of objects aids in their tracking, and thus propose to jointly infer the complete geometry of objects as well as track them, for rigidly moving objects over time. Our key insight is that inferring the complete geometry of the objects significantly helps in tracking. By hallucinating unseen regions of objects, we can obtain additional correspondences between the same instance, thus providing robust tracking even under strong change of appearance. From a sequence of RGB-D frames, we detect objects in each frame and learn to predict their complete object geometry as well as a dense correspondence mapping into a canonical space. This allows us to derive 6DoF poses for the objects in each frame, along with their correspondence between frames, providing robust object tracking across the RGB-D sequence. Experiments on both synthetic and real-world RGB-D data demonstrate that we achieve state-of-the-art performance on dynamic object tracking. Furthermore, we show that our object completion significantly helps tracking, providing an improvement of $6.5\%$ in mean MOTA.

### Learning a Proposal Classifier for Multiple Object Tracking.
- **链接**: [arXiv:2103.07889](https://arxiv.org/abs/2103.07889) · [代码](https://github.com/daip13/LPC_MOT.git)
- **作者**: Peng Dai, Renliang Weng, Wongun Choi, Changshui Zhang, Zhangping He, Wei Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > The recent trend in multiple object tracking (MOT) is heading towards leveraging deep learning to boost the tracking performance. However, it is not trivial to solve the data-association problem in an end-to-end fashion. In this paper, we propose a novel proposal-based learnable framework, which models MOT as a proposal generation, proposal scoring and trajectory inference paradigm on an affinity graph. This framework is similar to the two-stage object detector Faster RCNN, and can solve the MOT problem in a data-driven way. For proposal generation, we propose an iterative graph clustering method to reduce the computational cost while maintaining the quality of the generated proposals. For proposal scoring, we deploy a trainable graph-convolutional-network (GCN) to learn the structural patterns of the generated proposals and rank them according to the estimated quality scores. For trajectory inference, a simple deoverlapping strategy is adopted to generate tracking output while complying with the constraints that no detection can be assigned to more than one track. We experimentally demonstrate that the proposed method achieves a clear performance improvement in both MOTA and IDF1 with respect to previous state-of-the-art on two public benchmarks. Our code is available at https://github.com/daip13/LPC_MOT.git.

### Online Multiple Object Tracking With Cross-Task Synergy.
- **链接**: [arXiv:2104.00380](https://arxiv.org/abs/2104.00380) · [代码](https://github.com/songguocode/TADAM) · 📚 被引 70
- **作者**: Song Guo, Jingya Wang, Xinchao Wang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Modern online multiple object tracking (MOT) methods usually focus on two directions to improve tracking performance. One is to predict new positions in an incoming frame based on tracking information from previous frames, and the other is to enhance data association by generating more discriminative identity embeddings. Some works combined both directions within one framework but handled them as two individual tasks, thus gaining little mutual benefits. In this paper, we propose a novel unified model with synergy between position prediction and embedding association. The two tasks are linked by temporal-aware target attention and distractor attention, as well as identity-aware memory aggregation model. Specifically, the attention modules can make the prediction focus more on targets and less on distractors, therefore more reliable embeddings can be extracted accordingly for association. On the other hand, such reliable embeddings can boost identity-awareness through memory aggregation, hence strengthen attention modules and suppress drifts. In this way, the synergy between position prediction and embedding association is achieved, which leads to strong robustness to occlusions. Extensive experiments demonstrate the superiority of our proposed model over a wide range of existing methods on MOTChallenge benchmarks. Our code and models are publicly available at https://github.com/songguocode/TADAM.

### Learnable Graph Matching: Incorporating Graph Partitioning With Deep Feature Learning for Multiple Object Tracking.
- **链接**: [arXiv:2103.16178](https://arxiv.org/abs/2103.16178) · [代码](https://github.com/jiaweihe1996/GMTracker)
- **作者**: Jiawei He, Zehao Huang, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

- **摘要（英，原文）**:

  > Data association across frames is at the core of Multiple Object Tracking (MOT) task. This problem is usually solved by a traditional graph-based optimization or directly learned via deep learning. Despite their popularity, we find some points worth studying in current paradigm: 1) Existing methods mostly ignore the context information among tracklets and intra-frame detections, which makes the tracker hard to survive in challenging cases like severe occlusion. 2) The end-to-end association methods solely rely on the data fitting power of deep neural networks, while they hardly utilize the advantage of optimization-based assignment methods. 3) The graph-based optimization methods mostly utilize a separate neural network to extract features, which brings the inconsistency between training and inference. Therefore, in this paper we propose a novel learnable graph matching method to address these issues. Briefly speaking, we model the relationships between tracklets and the intra-frame detections as a general undirected graph. Then the association problem turns into a general graph matching between tracklet graph and detection graph. Furthermore, to make the optimization end-to-end differentiable, we relax the original graph matching into continuous quadratic programming and then incorporate the training of it into a deep graph network with the help of the implicit function theorem. Lastly, our method GMTracker, achieves state-of-the-art performance on several standard MOT datasets. Our code will be available at https://github.com/jiaweihe1996/GMTracker .

### Quasi-Dense Similarity Learning for Multiple Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Pang_Quasi-Dense_Similarity_Learning_for_Multiple_Object_Tracking_CVPR_2021_paper.html) · 📚 被引 425
- **作者**: Jiangmiao Pang, Linlu Qiu, Xia Li, Haofeng Chen, Qi Li, Trevor Darrell et al.
- **🏷️ 机构**: Zhejiang University, Georgia Institute of Technology, ETH Z&#x00FC;rich
- **会议**: CVPR 2021

### Probabilistic Tracklet Scoring and Inpainting for Multiple Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Saleh_Probabilistic_Tracklet_Scoring_and_Inpainting_for_Multiple_Object_Tracking_CVPR_2021_paper.html) · 📚 被引 87
- **作者**: Fatemeh Sadat Saleh, Sadegh Aliakbarian, Hamid Rezatofighi, Mathieu Salzmann, Stephen Gould
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### SiamMOT: Siamese Multi-Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Shuai_SiamMOT_Siamese_Multi-Object_Tracking_CVPR_2021_paper.html)
- **作者**: Bing Shuai, Andrew G. Berneshawi, Xinyu Li, Davide Modolo, Joseph Tighe
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Multiple Object Tracking With Correlation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Multiple_Object_Tracking_With_Correlation_Learning_CVPR_2021_paper.html)
- **作者**: Qiang Wang, Yun Zheng, Pan Pan, Yinghui Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Transformer Meets Tracker: Exploiting Temporal Context for Robust Visual Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Transformer_Meets_Tracker_Exploiting_Temporal_Context_for_Robust_Visual_Tracking_CVPR_2021_paper.html) · 📚 被引 805
- **作者**: Ning Wang, Wengang Zhou, Jie Wang, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### STMTrack: Template-Free Visual Tracking With Space-Time Memory Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Fu_STMTrack_Template-Free_Visual_Tracking_With_Space-Time_Memory_Networks_CVPR_2021_paper.html) · 📚 被引 350
- **作者**: Zhihong Fu, Qingjie Liu, Zehua Fu, Yunhong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### TesseTrack: End-to-End Learnable Multi-Person Articulated 3D Pose Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Reddy_TesseTrack_End-to-End_Learnable_Multi-Person_Articulated_3D_Pose_Tracking_CVPR_2021_paper.html) · 📚 被引 104
- **作者**: N. Dinesh Reddy, Laurent Guigues, Leonid Pishchulin, Jayan Eledath, Srinivasa G. Narasimhan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

## 跨领域论文（完整笔记在其他领域）

- DyGLIP: A Dynamic Graph Model With Link Prediction for Accurate Multi-Camera Multiple Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
