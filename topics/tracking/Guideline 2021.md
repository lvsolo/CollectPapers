# Tracking — 2021 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### GMOT-40: A Benchmark for Generic Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2011.11858](https://arxiv.org/abs/2011.11858) · 📚 被引 38
- **作者**: Hexin Bai, Wensheng Cheng, Peng Chu, Juehuan Liu, Kai Zhang, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对通用多目标跟踪（GMOT）领域缺乏公开基准和专用算法的问题，现有MOT方法依赖目标先验知识，难以泛化到未见类别。②构建了首个GMOT数据集GMOT-40，包含10个类别、40个精心标注的序列，并设计了两种跟踪协议以评估算法特性；同时提出了一系列基线GMOT算法。③相比现有MOT基准，GMOT-40强调无需目标先验的通用跟踪，填补了该方向空白。④对GMOT-40进行了全面评估，涵盖主流MOT算法（经必要修改）和所提基线，结果将公开。
- **摘要（英）**: This paper addresses the lack of benchmarks and dedicated algorithms for Generic Multiple Object Tracking (GMOT), where prior knowledge of targets is unavailable. It introduces GMOT-40, the first public GMOT dataset with 40 sequences across 10 categories, along with two evaluation protocols and baseline algorithms. The work fills a gap by enabling evaluation of tracking methods on unseen categories, with comprehensive results to be released.
- **核心贡献**: 构建了首个通用多目标跟踪基准GMOT-40及配套评估协议和基线算法。
- **创新点**: 首次系统性地定义和评估无需目标先验的通用多目标跟踪任务。
- **结果**: 提供了全面的基准评估结果，并公开数据集和基线以促进后续研究。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multiple Object Tracking (MOT) has witnessed remarkable advances in recent years. However, existing studies dominantly request prior knowledge of the tracking target, and hence may not generalize well to unseen categories. In contrast, Generic Multiple Object Tracking (GMOT), which requires little prior information about the target, is largely under-explored. In this paper, we make contributions to boost the study of GMOT in three aspects. First, we construct the first public GMOT dataset, dubbed GMOT-40, which contains 40 carefully annotated sequences evenly distributed among 10 object categories. In addition, two tracking protocols are adopted to evaluate different characteristics of tracking algorithms. Second, by noting the lack of devoted tracking algorithms, we have designed a series of baseline GMOT algorithms. Third, we perform a thorough evaluation on GMOT-40, involving popular MOT algorithms (with necessary modifications) and the proposed baselines. We will release the GMOT-40 benchmark, the evaluation results, as well as the baseline algorithm to the public upon the publication of the paper.

</details>

### Improving Multiple Object Tracking With Single Object Tracking. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zheng_Improving_Multiple_Object_Tracking_With_Single_Object_Tracking_CVPR_2021_paper.html)
- **作者**: Linyu Zheng, Ming Tang, Yingying Chen, Guibo Zhu, Jinqiao Wang, Hanqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多目标跟踪（MOT）中数据关联的鲁棒性问题，现有方法在遮挡和外观变化下性能受限。②提出利用单目标跟踪（SOT）来改进MOT，通过整合SOT的时序信息增强目标定位和关联。③相比纯MOT方法，该方法结合了SOT的长期跟踪能力，提高了跟踪稳定性。④摘要不完整，未提供具体数据，但方法思路具有潜力。
- **摘要（英）**: This paper proposes improving multiple object tracking by leveraging single object tracking techniques to enhance temporal consistency and association robustness. The integration aims to address challenges like occlusion and appearance changes. Specific results are not available due to incomplete abstract.
- **核心贡献**: 提出将单目标跟踪能力融入多目标跟踪框架以提升性能。
- **创新点**: 利用SOT的时序建模增强MOT的数据关联。
- **结果**: 未提供具体实验数据，效果待验证。

### Discriminative Appearance Modeling With Multi-Track Pooling for Real-Time Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2101.12159](https://arxiv.org/abs/2101.12159) · 📚 被引 73
- **作者**: Chanho Kim, Fuxin Li, Mazen Alotaibi, James M. Rehg
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多目标跟踪中外观模型孤立建模的问题，现有方法忽略场景中所有目标间的相互影响，导致相似外观目标易混淆。②提出多轨迹池化模块，在更新记忆时同时考虑所有轨迹，并设计适配的在线训练策略生成困难跟踪片段。③相比逐目标独立建模，该方法以极小空间开销实现联合外观建模，支持贪心数据关联。④在公开MOT数据集上达到实时、最先进的性能。
- **摘要（英）**: This paper tackles the issue of isolated appearance modeling in multi-object tracking by introducing a multi-track pooling module that jointly updates memory across all tracks with minimal spatial overhead. A tailored training strategy generates hard episodes online. The method achieves real-time state-of-the-art performance on public MOT benchmarks.
- **核心贡献**: 提出多轨迹池化模块和配套训练策略，实现实时高精度多目标跟踪。
- **创新点**: 在记忆更新中同时考虑所有轨迹，增强外观判别能力。
- **结果**: 在公开MOT数据集上达到实时最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In multi-object tracking, the tracker maintains in its memory the appearance and motion information for each object in the scene. This memory is utilized for finding matches between tracks and detections and is updated based on the matching result. Many approaches model each target in isolation and lack the ability to use all the targets in the scene to jointly update the memory. This can be problematic when there are similar looking objects in the scene. In this paper, we solve the problem of simultaneously considering all tracks during memory updating, with only a small spatial overhead, via a novel multi-track pooling module. We additionally propose a training strategy adapted to multi-track pooling which generates hard tracking episodes online. We show that the combination of these innovations results in a strong discriminative appearance model, enabling the use of greedy data association to achieve online tracking performance. Our experiments demonstrate real-time, state-of-the-art performance on public multi-object tracking (MOT) datasets.

</details>

### Seeing Behind Objects for 3D Multi-Object Tracking in RGB-D Sequences. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2012.08197](https://arxiv.org/abs/2012.08197) · 📚 被引 18
- **作者**: Norman Müller, Yu-Shiang Wong, Niloy J. Mitra, Angela Dai, Matthias Nießner
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对RGB-D序列中多目标跟踪因视角变化、运动和遮挡导致的挑战，现有方法缺乏对物体完整几何的利用。②提出联合推断物体完整几何和跟踪，通过预测未见区域和密集对应映射到规范空间，从而获得6DoF姿态和帧间对应。③相比仅依赖可见部分的方法，完整几何补全提供了更多对应关系，增强遮挡下的鲁棒性。④在合成和真实RGB-D数据上达到动态物体跟踪的最先进性能。
- **摘要（英）**: This paper addresses RGB-D multi-object tracking by jointly inferring complete object geometry and tracking, using hallucinated regions to obtain additional correspondences. This enables robust 6DoF pose estimation and tracking under strong appearance changes. Experiments on synthetic and real data show state-of-the-art performance.
- **核心贡献**: 提出联合物体几何补全与跟踪的框架，提升RGB-D序列中动态物体跟踪鲁棒性。
- **创新点**: 利用完整几何推断增强帧间对应，克服外观变化。
- **结果**: 在合成和真实数据上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking from RGB-D video sequences is a challenging problem due to the combination of changing viewpoints, motion, and occlusions over time. We observe that having the complete geometry of objects aids in their tracking, and thus propose to jointly infer the complete geometry of objects as well as track them, for rigidly moving objects over time. Our key insight is that inferring the complete geometry of the objects significantly helps in tracking. By hallucinating unseen regions of objects, we can obtain additional correspondences between the same instance, thus providing robust tracking even under strong change of appearance. From a sequence of RGB-D frames, we detect objects in each frame and learn to predict their complete object geometry as well as a dense correspondence mapping into a canonical space. This allows us to derive 6DoF poses for the objects in each frame, along with their correspondence between frames, providing robust object tracking across the RGB-D sequence. Experiments on both synthetic and real-world RGB-D data demonstrate that we achieve state-of-the-art performance on dynamic object tracking. Furthermore, we show that our object completion significantly helps tracking, providing an improvement of $6.5\%$ in mean MOTA.

</details>

### Learning a Proposal Classifier for Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2103.07889](https://arxiv.org/abs/2103.07889) · 📚 被引 115
- **作者**: Peng Dai, Renliang Weng, Wongun Choi, Changshui Zhang, Zhangping He, Wei Ding
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多目标跟踪中数据关联难以端到端学习的问题，现有方法多依赖手工设计或分步优化。②提出基于提议的可学习框架，将MOT建模为提议生成、评分和轨迹推断，类似Faster RCNN的两阶段范式；使用迭代图聚类生成提议，图卷积网络学习结构模式并评分。③相比传统关联方法，该框架以数据驱动方式解决关联问题，降低计算成本。④在MOTA和IDF1指标上均取得明显性能提升。
- **摘要（英）**: This paper proposes a proposal-based learnable framework for MOT, modeling it as proposal generation, scoring, and trajectory inference on an affinity graph, akin to Faster R-CNN. It uses iterative graph clustering and graph convolutional networks for efficient and effective association. The method achieves clear improvements in MOTA and IDF1.
- **核心贡献**: 提出基于提议和图卷积的MOT框架，实现数据驱动的数据关联。
- **创新点**: 借鉴两阶段检测器设计，将关联问题转化为提议评分问题。
- **结果**: 在MOTA和IDF1上均显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent trend in multiple object tracking (MOT) is heading towards leveraging deep learning to boost the tracking performance. However, it is not trivial to solve the data-association problem in an end-to-end fashion. In this paper, we propose a novel proposal-based learnable framework, which models MOT as a proposal generation, proposal scoring and trajectory inference paradigm on an affinity graph. This framework is similar to the two-stage object detector Faster RCNN, and can solve the MOT problem in a data-driven way. For proposal generation, we propose an iterative graph clustering method to reduce the computational cost while maintaining the quality of the generated proposals. For proposal scoring, we deploy a trainable graph-convolutional-network (GCN) to learn the structural patterns of the generated proposals and rank them according to the estimated quality scores. For trajectory inference, a simple deoverlapping strategy is adopted to generate tracking output while complying with the constraints that no detection can be assigned to more than one track. We experimentally demonstrate that the proposed method achieves a clear performance improvement in both MOTA and IDF1 with respect to previous state-of-the-art on two public benchmarks. Our code is available at https://github.com/daip13/LPC_MOT.git.

</details>

### Online Multiple Object Tracking With Cross-Task Synergy. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2104.00380](https://arxiv.org/abs/2104.00380) · 📚 被引 70
- **作者**: Song Guo, Jingya Wang, Xinchao Wang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对在线多目标跟踪中位置预测和嵌入关联两个任务独立处理、缺乏协同的问题，现有方法难以从相互增强中获益。②提出统一模型，通过时间感知的目标注意力和干扰物注意力连接两个任务，并利用身份感知记忆聚合模型增强身份意识。③相比分别处理两任务的方法，该协同机制使预测更聚焦目标，嵌入更可靠，从而提升关联鲁棒性。④实验表明对遮挡具有强鲁棒性，性能优于现有方法。
- **摘要（英）**: This paper addresses the lack of synergy between position prediction and embedding association in online MOT by proposing a unified model with temporal-aware target and distractor attention, plus identity-aware memory aggregation. This synergy enhances prediction focus and embedding reliability, improving robustness to occlusions. Experiments demonstrate superior performance.
- **核心贡献**: 提出位置预测与嵌入关联协同的统一MOT模型，增强遮挡鲁棒性。
- **创新点**: 利用注意力机制和记忆聚合实现任务间互惠增强。
- **结果**: 在遮挡场景下表现强鲁棒性，性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern online multiple object tracking (MOT) methods usually focus on two directions to improve tracking performance. One is to predict new positions in an incoming frame based on tracking information from previous frames, and the other is to enhance data association by generating more discriminative identity embeddings. Some works combined both directions within one framework but handled them as two individual tasks, thus gaining little mutual benefits. In this paper, we propose a novel unified model with synergy between position prediction and embedding association. The two tasks are linked by temporal-aware target attention and distractor attention, as well as identity-aware memory aggregation model. Specifically, the attention modules can make the prediction focus more on targets and less on distractors, therefore more reliable embeddings can be extracted accordingly for association. On the other hand, such reliable embeddings can boost identity-awareness through memory aggregation, hence strengthen attention modules and suppress drifts. In this way, the synergy between position prediction and embedding association is achieved, which leads to strong robustness to occlusions. Extensive experiments demonstrate the superiority of our proposed model over a wide range of existing methods on MOTChallenge benchmarks. Our code and models are publicly available at https://github.com/songguocode/TADAM.

</details>

### Learnable Graph Matching: Incorporating Graph Partitioning With Deep Feature Learning for Multiple Object Tracking. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2103.16178](https://arxiv.org/abs/2103.16178) · 📚 被引 124
- **作者**: Jiawei He, Zehao Huang, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对多目标跟踪中数据关联忽略轨迹间和帧内检测的上下文信息、端到端方法缺乏优化分配优势、图优化方法特征提取与推理不一致的问题，提出了一种可学习的图匹配方法。该方法将轨迹与检测建模为无向图，将关联问题转化为图匹配问题，并实现端到端优化。相比已有工作，它结合了深度特征学习与图划分优化，缓解了训练与推理的不一致性。实验表明该方法在MOT基准上具有竞争力。
- **摘要（英）**: This paper addresses data association in multi-object tracking by proposing a learnable graph matching method that models tracklets and detections as graphs and solves association via graph matching. It integrates deep feature learning with graph partitioning to handle context information and reduce train-inference inconsistency. Experiments show competitive performance on MOT benchmarks.
- **核心贡献**: 提出了一种可学习的图匹配框架，统一了特征提取与关联优化。
- **创新点**: 将轨迹-检测关联建模为图匹配问题，并实现端到端训练。
- **结果**: 在MOT基准上取得有竞争力的跟踪性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data association across frames is at the core of Multiple Object Tracking (MOT) task. This problem is usually solved by a traditional graph-based optimization or directly learned via deep learning. Despite their popularity, we find some points worth studying in current paradigm: 1) Existing methods mostly ignore the context information among tracklets and intra-frame detections, which makes the tracker hard to survive in challenging cases like severe occlusion. 2) The end-to-end association methods solely rely on the data fitting power of deep neural networks, while they hardly utilize the advantage of optimization-based assignment methods. 3) The graph-based optimization methods mostly utilize a separate neural network to extract features, which brings the inconsistency between training and inference. Therefore, in this paper we propose a novel learnable graph matching method to address these issues. Briefly speaking, we model the relationships between tracklets and the intra-frame detections as a general undirected graph. Then the association problem turns into a general graph matching between tracklet graph and detection graph. Furthermore, to make the optimization end-to-end differentiable, we relax the original graph matching into continuous quadratic programming and then incorporate the training of it into a deep graph network with the help of the implicit function theorem. Lastly, our method GMTracker, achieves state-of-the-art performance on several standard MOT datasets. Our code will be available at https://github.com/jiaweihe1996/GMTracker .

</details>

### Quasi-Dense Similarity Learning for Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Pang_Quasi-Dense_Similarity_Learning_for_Multiple_Object_Tracking_CVPR_2021_paper.html) · 📚 被引 426
- **作者**: Jiangmiao Pang, Linlu Qiu, Xia Li, Haofeng Chen, Qi Li, Trevor Darrell et al.
- **🏷️ 机构**: Zhejiang University, Georgia Institute of Technology, ETH Z&#x00FC;rich
- **会议**: CVPR 2021
- **摘要（中）**: 针对多目标跟踪中相似度学习效率低、难以处理密集场景的问题，提出了准密集相似度学习方法。该方法通过密集采样实例对进行对比学习，增强特征判别力，并利用准密集匹配实现高效关联。相比稀疏匹配方法，它充分利用了空间上下文，提升了跟踪鲁棒性。在MOT17、MOT20等基准上取得了领先性能。
- **摘要（英）**: This paper introduces quasi-dense similarity learning for multi-object tracking, which densely samples instance pairs for contrastive learning and uses quasi-dense matching for association. It improves feature discrimination and robustness in crowded scenes. The method achieves state-of-the-art results on MOT17 and MOT20.
- **核心贡献**: 提出了准密集相似度学习框架，增强了MOT中的特征匹配能力。
- **创新点**: 利用密集对比学习与准密集匹配替代稀疏关联。
- **结果**: 在多个MOT基准上达到领先性能。

### Probabilistic Tracklet Scoring and Inpainting for Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2012.02337](https://arxiv.org/abs/2012.02337) · 📚 被引 87
- **作者**: Fatemeh Sadat Saleh, Sadegh Aliakbarian, Hamid Rezatofighi, Mathieu Salzmann, Stephen Gould
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对多目标跟踪中长期遮挡导致轨迹丢失的问题，提出了概率自回归运动模型来评分轨迹提议。该方法通过学习自然轨迹的分布，直接测量轨迹似然，既能分配新检测，也能通过采样修复丢失轨迹。相比现有方法，它显式建模长期运动信息，提升了遮挡场景下的跟踪鲁棒性。在MOT16、MOT17和MOT20上超越了多数现有方法。
- **摘要（英）**: This paper proposes a probabilistic autoregressive motion model for tracklet scoring and inpainting in MOT, learning the distribution of natural tracklets to handle long occlusions. It enables both detection assignment and tracklet gap filling via sampling. The method outperforms state-of-the-art on MOT16, MOT17, and MOT20.
- **核心贡献**: 提出了基于概率自回归模型的轨迹评分与修复方法。
- **创新点**: 将轨迹似然建模用于遮挡恢复。
- **结果**: 在多个MOT数据集上取得最优性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent advances in multiple object tracking (MOT), achieved by joint detection and tracking, dealing with long occlusions remains a challenge. This is due to the fact that such techniques tend to ignore the long-term motion information. In this paper, we introduce a probabilistic autoregressive motion model to score tracklet proposals by directly measuring their likelihood. This is achieved by training our model to learn the underlying distribution of natural tracklets. As such, our model allows us not only to assign new detections to existing tracklets, but also to inpaint a tracklet when an object has been lost for a long time, e.g., due to occlusion, by sampling tracklets so as to fill the gap caused by misdetections. Our experiments demonstrate the superiority of our approach at tracking objects in challenging sequences; it outperforms the state of the art in most standard MOT metrics on multiple MOT benchmark datasets, including MOT16, MOT17, and MOT20.

</details>

### SiamMOT: Siamese Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2105.11595](https://arxiv.org/abs/2105.11595) · 📚 被引 143
- **作者**: Bing Shuai, Andrew G. Berneshawi, Xinyu Li, Davide Modolo, Joseph Tighe
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对在线多目标跟踪中运动建模不足的问题，提出了基于区域的Siamese多目标跟踪网络SiamMOT。该方法包含运动模型估计实例帧间移动，并设计了隐式和显式两种运动建模变体。相比现有方法，它显著提升了运动建模能力，在MOT17、TAO-person和Caltech数据集上超越现有技术。SiamMOT运行效率高，在720P视频上达到17 FPS。
- **摘要（英）**: This paper introduces SiamMOT, a region-based Siamese network for online MOT with an explicit motion model for instance association. It explores implicit and explicit motion modeling variants, showing significant improvements over state-of-the-art on MOT17, TAO-person, and Caltech. The method runs at 17 FPS on 720P videos.
- **核心贡献**: 提出了SiamMOT，将Siamese网络与运动模型结合用于在线跟踪。
- **创新点**: 显式运动建模与区域级Siamese匹配的集成。
- **结果**: 在多个数据集上超越现有方法，且保持实时性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we focus on improving online multi-object tracking (MOT). In particular, we introduce a region-based Siamese Multi-Object Tracking network, which we name SiamMOT. SiamMOT includes a motion model that estimates the instance's movement between two frames such that detected instances are associated. To explore how the motion modelling affects its tracking capability, we present two variants of Siamese tracker, one that implicitly models motion and one that models it explicitly. We carry out extensive quantitative experiments on three different MOT datasets: MOT17, TAO-person and Caltech Roadside Pedestrians, showing the importance of motion modelling for MOT and the ability of SiamMOT to substantially outperform the state-of-the-art. Finally, SiamMOT also outperforms the winners of ACM MM'20 HiEve Grand Challenge on HiEve dataset. Moreover, SiamMOT is efficient, and it runs at 17 FPS for 720P videos on a single modern GPU. Codes are available in \url{https://github.com/amazon-research/siam-mot}.

</details>

### Multiple Object Tracking With Correlation Learning. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2104.03541](https://arxiv.org/abs/2104.03541)
- **作者**: Qiang Wang, Yun Zheng, Pan Pan, Yinghui Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对多目标跟踪中卷积网络难以捕获长距离时空依赖的问题，提出利用局部相关模块建模目标与周围环境的拓扑关系，并通过自监督学习约束相关体积。同时提出可学习的相关算子，在不同层特征图上建立帧间匹配以对齐和传播时序上下文。相比仅依赖相邻帧特征增强的方法，该方法在拥挤场景下显著提升了判别能力，在MOT基准上取得了领先性能。
- **摘要（英）**: This paper addresses the limitation of CNNs in capturing long-range spatio-temporal dependencies for multi-object tracking by introducing local correlation modules for topological modeling and learnable correlation operators for frame-to-frame matching. It achieves state-of-the-art performance on MOT benchmarks, especially in crowded scenes.
- **核心贡献**: 提出基于相关学习的多目标跟踪框架，增强时空上下文建模。
- **创新点**: 利用局部相关模块和可学习相关算子实现长距离依赖捕获。
- **结果**: 在多个MOT基准上取得领先的跟踪精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works have shown that convolutional networks have substantially improved the performance of multiple object tracking by simultaneously learning detection and appearance features. However, due to the local perception of the convolutional network structure itself, the long-range dependencies in both the spatial and temporal cannot be obtained efficiently. To incorporate the spatial layout, we propose to exploit the local correlation module to model the topological relationship between targets and their surrounding environment, which can enhance the discriminative power of our model in crowded scenes. Specifically, we establish dense correspondences of each spatial location and its context, and explicitly constrain the correlation volumes through self-supervised learning. To exploit the temporal context, existing approaches generally utilize two or more adjacent frames to construct an enhanced feature representation, but the dynamic motion scene is inherently difficult to depict via CNNs. Instead, our paper proposes a learnable correlation operator to establish frame-to-frame matches over convolutional feature maps in the different layers to align and propagate temporal context. With extensive experimental results on the MOT datasets, our approach demonstrates the effectiveness of correlation learning with the superior performance and obtains state-of-the-art MOTA of 76.5% and IDF1 of 73.6% on MOT17.

</details>

### Transformer Meets Tracker: Exploiting Temporal Context for Robust Visual Tracking. **⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2103.11681](https://arxiv.org/abs/2103.11681) · 📚 被引 805
- **作者**: Ning Wang, Wengang Zhou, Jie Wang, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对视频目标跟踪中时间上下文利用不足的问题，提出了基于Transformer的跟踪框架。该方法将编码器和解码器分离为并行分支，编码器增强目标模板特征，解码器传播跟踪线索。相比传统Siamese跟踪器，它有效利用了帧间时间信息，提升了跟踪鲁棒性。在多个基准上超越了当前顶尖跟踪器。
- **摘要（英）**: This paper proposes a transformer-based tracking framework that exploits temporal context by separating encoder and decoder branches for template enhancement and cue propagation. It improves tracking robustness compared to Siamese trackers. The method achieves state-of-the-art results on prevalent benchmarks.
- **核心贡献**: 提出了并行编码器-解码器Transformer结构用于视觉跟踪。
- **创新点**: 将Transformer的编码器和解码器分别用于模板增强和线索传播。
- **结果**: 在多个跟踪基准上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In video object tracking, there exist rich temporal contexts among successive frames, which have been largely overlooked in existing trackers. In this work, we bridge the individual video frames and explore the temporal contexts across them via a transformer architecture for robust object tracking. Different from classic usage of the transformer in natural language processing tasks, we separate its encoder and decoder into two parallel branches and carefully design them within the Siamese-like tracking pipelines. The transformer encoder promotes the target templates via attention-based feature reinforcement, which benefits the high-quality tracking model generation. The transformer decoder propagates the tracking cues from previous templates to the current frame, which facilitates the object searching process. Our transformer-assisted tracking framework is neat and trained in an end-to-end manner. With the proposed transformer, a simple Siamese matching approach is able to outperform the current top-performing trackers. By combining our transformer with the recent discriminative tracking pipeline, our method sets several new state-of-the-art records on prevalent tracking benchmarks.

</details>

### STMTrack: Template-Free Visual Tracking With Space-Time Memory Networks. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2104.00324](https://arxiv.org/abs/2104.00324) · 📚 被引 350
- **作者**: Zhihong Fu, Qingjie Liu, Zehua Fu, Yunhong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对Siamese跟踪器固定模板难以适应目标外观变化的问题，提出了基于时空记忆网络的模板无关跟踪框架STMTrack。该方法利用记忆机制存储历史目标信息，引导跟踪器关注当前帧的显著区域，并通过像素级相似度计算生成精确边界框。相比模板更新方法，它避免了复杂优化和手工策略。在OTB等基准上展现了竞争力。
- **摘要（英）**: This paper proposes STMTrack, a template-free tracking framework using space-time memory networks to store historical target information and guide attention. It avoids complex template updating strategies and generates accurate bounding boxes via pixel-level similarity. The method shows competitive performance on large-scale benchmarks.
- **核心贡献**: 提出了基于时空记忆网络的模板无关跟踪方法。
- **创新点**: 利用记忆机制替代固定模板更新。
- **结果**: 在OTB等基准上取得有竞争力的结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Boosting performance of the offline trained siamese trackers is getting harder nowadays since the fixed information of the template cropped from the first frame has been almost thoroughly mined, but they are poorly capable of resisting target appearance changes. Existing trackers with template updating mechanisms rely on time-consuming numerical optimization and complex hand-designed strategies to achieve competitive performance, hindering them from real-time tracking and practical applications. In this paper, we propose a novel tracking framework built on top of a space-time memory network that is competent to make full use of historical information related to the target for better adapting to appearance variations during tracking. Specifically, a novel memory mechanism is introduced, which stores the historical information of the target to guide the tracker to focus on the most informative regions in the current frame. Furthermore, the pixel-level similarity computation of the memory network enables our tracker to generate much more accurate bounding boxes of the target. Extensive experiments and comparisons with many competitive trackers on challenging large-scale benchmarks, OTB-2015, TrackingNet, GOT-10k, LaSOT, UAV123, and VOT2018, show that, without bells and whistles, our tracker outperforms all previous state-of-the-art real-time methods while running at 37 FPS. The code is available at https://github.com/fzh0917/STMTrack.

</details>

### TesseTrack: End-to-End Learnable Multi-Person Articulated 3D Pose Tracking. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Reddy_TesseTrack_End-to-End_Learnable_Multi-Person_Articulated_3D_Pose_Tracking_CVPR_2021_paper.html) · 📚 被引 104
- **作者**: N. Dinesh Reddy, Laurent Guigues, Leonid Pishchulin, Jayan Eledath, Srinivasa G. Narasimhan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①这篇论文针对多人体关节3D姿态跟踪问题，旨在从视频中端到端地学习人体姿态序列。②提出了一个可学习的端到端框架，直接输出多人的关节3D姿态轨迹，可能结合了检测与关联模块。③相比传统分步方法，该方法统一了检测和跟踪，减少了误差累积。④摘要未提供具体数据，效果未知，但作为端到端方法具有探索意义。
- **摘要（英）**: This paper addresses multi-person articulated 3D pose tracking in videos, proposing an end-to-end learnable framework that directly outputs pose trajectories. It unifies detection and association to reduce error accumulation, though no quantitative results are reported in the abstract.
- **核心贡献**: 提出端到端的多人体3D姿态跟踪框架。
- **创新点**: 将检测与关联集成于单一可学习网络。
- **结果**: 未报告具体效果数据。

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
