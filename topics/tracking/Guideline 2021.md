# Tracking — 2021 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GMOT-40: A Benchmark for Generic Multiple Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Bai_GMOT-40_A_Benchmark_for_Generic_Multiple_Object_Tracking_CVPR_2021_paper.html) · 📚 被引 38
- **作者**: Hexin Bai, Wensheng Cheng, Peng Chu, Juehuan Liu, Kai Zhang, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Improving Multiple Object Tracking With Single Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zheng_Improving_Multiple_Object_Tracking_With_Single_Object_Tracking_CVPR_2021_paper.html)
- **作者**: Linyu Zheng, Ming Tang, Yingying Chen, Guibo Zhu, Jinqiao Wang, Hanqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Discriminative Appearance Modeling With Multi-Track Pooling for Real-Time Multi-Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Kim_Discriminative_Appearance_Modeling_With_Multi-Track_Pooling_for_Real-Time_Multi-Object_Tracking_CVPR_2021_paper.html) · 📚 被引 73
- **作者**: Chanho Kim, Fuxin Li, Mazen Alotaibi, James M. Rehg
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Seeing Behind Objects for 3D Multi-Object Tracking in RGB-D Sequences.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Muller_Seeing_Behind_Objects_for_3D_Multi-Object_Tracking_in_RGB-D_Sequences_CVPR_2021_paper.html) · 📚 被引 18
- **作者**: Norman Müller, Yu-Shiang Wong, Niloy J. Mitra, Angela Dai, Matthias Nießner
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Learning a Proposal Classifier for Multiple Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Dai_Learning_a_Proposal_Classifier_for_Multiple_Object_Tracking_CVPR_2021_paper.html)
- **作者**: Peng Dai, Renliang Weng, Wongun Choi, Changshui Zhang, Zhangping He, Wei Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

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

## 跨领域论文（完整笔记在其他领域）

- DyGLIP: A Dynamic Graph Model With Link Prediction for Accurate Multi-Camera Multiple Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
