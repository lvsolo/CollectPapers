# Tracking — 2021 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GMOT-40: A Benchmark for Generic Multiple Object Tracking.
- **链接**: [arXiv:2011.11858](https://arxiv.org/abs/2011.11858) · 📚 被引 38
- **作者**: Hexin Bai, Wensheng Cheng, Peng Chu, Juehuan Liu, Kai Zhang, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multiple object tracking and segmentation requires detecting, tracking, and segmenting objects belonging to a set of given classes. Most approaches only exploit the temporal dimension to address the association problem, while relying on single frame predictions for the segmentation mask itself. We propose Prototypical Cross-Attention Network (PCAN), capable of leveraging rich spatio-temporal information for online multiple object tracking and segmentation. PCAN first distills a space-time memory into a set of prototypes and then employs cross-attention to retrieve rich information from the past frames. To segment each object, PCAN adopts a prototypical appearance module to learn a set of contrastive foreground and background prototypes, which are then propagated over time. Extensive experiments demonstrate that PCAN outperforms current video instance tracking and segmentation competition winners on both Youtube-VIS and BDD100K datasets, and shows efficacy to both one-stage and two-stage segmentation frameworks. Code and video resources are available at http://vis.xyz/pub/pcan.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current 3D single object tracking approaches track the target based on a feature comparison between the target template and the search area. However, due to the common occlusion in LiDAR scans, it is non-trivial to conduct accurate feature comparisons on severe sparse and incomplete shapes. In this work, we exploit the ground truth bounding box given in the first frame as a strong cue to enhance the feature description of the target object, enabling a more accurate feature comparison in a simple yet effective way. In particular, we first propose the BoxCloud, an informative and robust representation, to depict an object using the point-to-box relation. We further design an efficient box-aware feature fusion module, which leverages the aforementioned BoxCloud for reliable feature matching and embedding. Integrating the proposed general components into an existing model P2B, we construct a superior box-aware tracker (BAT). Experiments confirm that our proposed BAT outperforms the previous state-of-the-art by a large margin on both KITTI and NuScenes benchmarks, achieving a 15.2% improvement in terms of precision while running ~20% faster.

</details>

### Seeing Behind Objects for 3D Multi-Object Tracking in RGB-D Sequences.
- **链接**: [arXiv:2012.08197](https://arxiv.org/abs/2012.08197) · 📚 被引 18
- **作者**: Norman Müller, Yu-Shiang Wong, Niloy J. Mitra, Angela Dai, Matthias Nießner
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking from RGB-D video sequences is a challenging problem due to the combination of changing viewpoints, motion, and occlusions over time. We observe that having the complete geometry of objects aids in their tracking, and thus propose to jointly infer the complete geometry of objects as well as track them, for rigidly moving objects over time. Our key insight is that inferring the complete geometry of the objects significantly helps in tracking. By hallucinating unseen regions of objects, we can obtain additional correspondences between the same instance, thus providing robust tracking even under strong change of appearance. From a sequence of RGB-D frames, we detect objects in each frame and learn to predict their complete object geometry as well as a dense correspondence mapping into a canonical space. This allows us to derive 6DoF poses for the objects in each frame, along with their correspondence between frames, providing robust object tracking across the RGB-D sequence. Experiments on both synthetic and real-world RGB-D data demonstrate that we achieve state-of-the-art performance on dynamic object tracking. Furthermore, we show that our object completion significantly helps tracking, providing an improvement of $6.5\%$ in mean MOTA.

</details>

### Learning a Proposal Classifier for Multiple Object Tracking.
- **链接**: [arXiv:2103.07889](https://arxiv.org/abs/2103.07889) · [代码](https://github.com/daip13/LPC_MOT.git) · 📚 被引 115
- **作者**: Peng Dai, Renliang Weng, Wongun Choi, Changshui Zhang, Zhangping He, Wei Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

</details>

### Online Multiple Object Tracking With Cross-Task Synergy.
- **链接**: [arXiv:2104.00380](https://arxiv.org/abs/2104.00380) · [代码](https://github.com/songguocode/TADAM) · 📚 被引 70
- **作者**: Song Guo, Jingya Wang, Xinchao Wang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Siamese tracking has achieved groundbreaking performance in recent years, where the essence is the efficient matching operator cross-correlation and its variants. Besides the remarkable success, it is important to note that the heuristic matching network design relies heavily on expert experience. Moreover, we experimentally find that one sole matching operator is difficult to guarantee stable tracking in all challenging environments. Thus, in this work, we introduce six novel matching operators from the perspective of feature fusion instead of explicit similarity learning, namely Concatenation, Pointwise-Addition, Pairwise-Relation, FiLM, Simple-Transformer and Transductive-Guidance, to explore more feasibility on matching operator selection. The analyses reveal these operators' selective adaptability on different environment degradation types, which inspires us to combine them to explore complementary features. To this end, we propose binary channel manipulation (BCM) to search for the optimal combination of these operators. BCM determines to retrain or discard one operator by learning its contribution to other tracking steps. By inserting the learned matching networks to a strong baseline tracker Ocean, our model achieves favorable gains by $67.2 \rightarrow 71.4$, $52.6 \rightarrow 58.3$, $70.3 \rightarrow 76.0$ success on OTB100, LaSOT, and TrackingNet, respectively. Notably, Our tracker, dubbed AutoMatch, uses less than half of training data/time than the baseline tracker, and runs at 50 FPS using PyTorch. Code and model will be released at https://github.com/JudasDie/SOTS.

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

- DyGLIP: A Dynamic Graph Model With Link Prediction for Accurate Multi-Camera Multiple Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)

## 🆕 增量新增

### CAPTRA: CAtegory-level Pose Tracking for Rigid and Articulated Objects from Point Clouds. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01296)
- **作者**: Yijia Weng, He Wang, Qiang Zhou, Yuzhe Qin, Yueqi Duan, Qingnan Fan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①该论文针对点云中刚体和关节物体的类别级姿态跟踪问题。②提出CAPTRA方法，利用点云输入进行类别级姿态估计与跟踪，支持刚体和关节物体。③相比实例级方法，泛化到未见过的同类物体，且统一处理两类物体。④摘要未提供具体数据，但强调类别级泛化能力。
- **摘要（英）**: This paper tackles category-level pose tracking for rigid and articulated objects from point clouds. CAPTRA performs pose estimation and tracking at category level, generalizing to unseen instances and handling both object types uniformly. The abstract highlights generalization but lacks quantitative results.
- **核心贡献**: 提出点云类别级刚体和关节物体姿态跟踪方法。
- **创新点**: 统一处理刚体和关节物体的类别级姿态跟踪。
- **结果**: 摘要未提供具体效果数据。

### Box-Aware Feature Enhancement for Single Object Tracking on Point Clouds. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01295)
- **作者**: Chaoda Zheng, Xu Yan, Jiantao Gao, Weibing Zhao, Wei Zhang, Zhen Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①该论文针对点云单目标跟踪中特征判别性不足的问题。②提出Box-Aware特征增强方法，利用目标框信息增强点云特征，提升跟踪鲁棒性。③相比仅依赖点云特征的方法，显式引入框先验，增强目标响应。④摘要未提供具体数据，但强调特征增强的有效性。
- **摘要（英）**: This paper addresses insufficient feature discrimination in single object tracking on point clouds. It proposes box-aware feature enhancement that leverages target box information to improve tracking robustness. Compared to point-only methods, it explicitly incorporates box priors to strengthen target response. The abstract lacks quantitative results.
- **核心贡献**: 提出框感知特征增强用于点云单目标跟踪。
- **创新点**: 显式利用目标框信息增强点云特征。
- **结果**: 摘要未提供具体效果数据。

### Towards Distraction-Robust Active Visual Tracking. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2106.10110](https://arxiv.org/abs/2106.10110)
- **作者**: Fangwei Zhong, Peng Sun, Wenhan Luo, Tingyun Yan, Yizhou Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021
- **摘要（中）**: ①针对主动视觉跟踪中干扰物（distractors）导致跟踪失败的问题。②提出混合合作-竞争多智能体博弈，目标与多个干扰物组成团队对抗跟踪器，通过博弈学习自然涌现多样的干扰行为，暴露跟踪器弱点。③提出干扰物奖励函数、跨模态师生学习策略和跟踪器的循环注意力机制。④实验表明跟踪器在干扰环境下表现鲁棒，并能泛化到未见环境，博弈还可用于对抗性测试跟踪器鲁棒性。
- **摘要（英）**: This paper addresses distraction-robustness in active visual tracking by proposing a mixed cooperative-competitive multi-agent game where target and distractors collaborate against a tracker. It introduces practical methods including distractor rewards, cross-modal teacher-student learning, and recurrent attention, achieving robust tracking and generalization, with the game serving for adversarial testing.
- **核心贡献**: 提出多智能体博弈框架增强主动跟踪的干扰鲁棒性。
- **创新点**: 合作-竞争博弈机制和跨模态师生学习。
- **结果**: 在干扰环境下实现鲁棒跟踪，并泛化到新环境。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In active visual tracking, it is notoriously difficult when distracting objects appear, as distractors often mislead the tracker by occluding the target or bringing a confusing appearance. To address this issue, we propose a mixed cooperative-competitive multi-agent game, where a target and multiple distractors form a collaborative team to play against a tracker and make it fail to follow. Through learning in our game, diverse distracting behaviors of the distractors naturally emerge, thereby exposing the tracker's weakness, which helps enhance the distraction-robustness of the tracker. For effective learning, we then present a bunch of practical methods, including a reward function for distractors, a cross-modal teacher-student learning strategy, and a recurrent attention mechanism for the tracker. The experimental results show that our tracker performs desired distraction-robust active visual tracking and can be well generalized to unseen environments. We also show that the multi-agent game can be used to adversarially test the robustness of trackers.

</details>

### Prototypical Cross-Attention Networks for Multiple Object Tracking and Segmentation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2106.11958](https://arxiv.org/abs/2106.11958)
- **作者**: Lei Ke, Xia Li, Martin Danelljan, Yu-Wing Tai, Chi-Keung Tang, Fisher Yu
- **🏷️ 机构**: ETH Zurich
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对多目标跟踪与分割中仅利用时间维度解决关联问题、分割依赖单帧预测的局限，提出原型交叉注意力网络PCAN。②方法将时空记忆蒸馏为原型集，通过交叉注意力从过去帧检索丰富信息，并采用原型外观模块学习对比性前景/背景原型，随时间传播。③相比现有方法，能充分利用时空信息，适用于在线多目标跟踪与分割。④在YouTube-VIS和BDD100K数据集上超越当前视频实例跟踪与分割竞赛冠军，且适用于单阶段和双阶段分割框架。
- **摘要（英）**: This paper addresses multiple object tracking and segmentation by proposing Prototypical Cross-Attention Network (PCAN), which distills spatio-temporal memory into prototypes and uses cross-attention to retrieve past information. It also learns contrastive foreground/background prototypes for segmentation. PCAN outperforms competition winners on YouTube-VIS and BDD100K, and works with both one-stage and two-stage frameworks.
- **核心贡献**: 提出原型交叉注意力网络用于在线多目标跟踪与分割。
- **创新点**: 利用原型蒸馏时空记忆并跨注意力检索。
- **结果**: 在YouTube-VIS和BDD100K上超越SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multiple object tracking and segmentation requires detecting, tracking, and segmenting objects belonging to a set of given classes. Most approaches only exploit the temporal dimension to address the association problem, while relying on single frame predictions for the segmentation mask itself. We propose Prototypical Cross-Attention Network (PCAN), capable of leveraging rich spatio-temporal information for online multiple object tracking and segmentation. PCAN first distills a space-time memory into a set of prototypes and then employs cross-attention to retrieve rich information from the past frames. To segment each object, PCAN adopts a prototypical appearance module to learn a set of contrastive foreground and background prototypes, which are then propagated over time. Extensive experiments demonstrate that PCAN outperforms current video instance tracking and segmentation competition winners on both Youtube-VIS and BDD100K datasets, and shows efficacy to both one-stage and two-stage segmentation frameworks. Code and video resources are available at http://vis.xyz/pub/pcan.

</details>

## 跨领域论文（完整笔记在其他领域）

- DyGLIP: A Dynamic Graph Model With Link Prediction for Accurate Multi-Camera Multiple Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-Supervised Multi-Object Tracking with Cross-input Consistency. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
<!-- COMPLETE v1 papers=18 -->
