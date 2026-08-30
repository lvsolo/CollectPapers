# Multi-camera Perception — 2023 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 58 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Are We Ready for Vision-Centric Driving Streaming Perception? The ASAP Benchmark. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2212.08914](https://arxiv.org/abs/2212.08914) · 📚 被引 21
- **作者**: Xiaofeng Wang, Zheng Zhu, Yunpeng Zhang, Guan Huang, Yun Ye, Wenbo Xu et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, PhiGent Robotics, Southeast University
- **会议**: CVPR 2023
- **摘要（中）**: 针对视觉中心感知方法在实际部署中延迟过高（如多数相机3D检测器运行时间超过300ms）而现有基准仅进行离线评估、忽略推理延迟的问题，提出了ASAP基准，这是首个评估自动驾驶视觉中心感知在线性能的基准。基于2Hz标注的nuScenes数据集，提出标注扩展流程生成12Hz高帧率标签，并构建了SPUR评估协议，利用12Hz输入进行流式评估。相比已有工作，首次量化了性能与效率的权衡，为实际部署提供了更真实的评估标准。
- **摘要（英）**: To address the high latency of vision-centric perception in real-world deployment and the lack of online evaluation in existing benchmarks, this paper proposes the ASAP benchmark, the first to evaluate online performance of vision-centric perception in autonomous driving. It introduces an annotation-extending pipeline to generate 12Hz labels from 2Hz annotated nuScenes data and a SPUR evaluation protocol for streaming assessment, quantifying the performance-efficiency trade-off.
- **核心贡献**: 提出首个面向自动驾驶视觉中心感知的在线流式感知基准ASAP及SPUR评估协议。
- **创新点**: 通过标注扩展和高帧率评估协议，首次将推理延迟纳入感知性能评估。
- **结果**: 提供了12Hz高帧率标签和流式评估协议，量化了性能与效率的权衡。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, vision-centric perception has flourished in various autonomous driving tasks, including 3D detection, semantic map construction, motion forecasting, and depth estimation. Nevertheless, the latency of vision-centric approaches is too high for practical deployment (e.g., most camera-based 3D detectors have a runtime greater than 300ms). To bridge the gap between ideal research and real-world applications, it is necessary to quantify the trade-off between performance and efficiency. Traditionally, autonomous-driving perception benchmarks perform the offline evaluation, neglecting the inference time delay. To mitigate the problem, we propose the Autonomous-driving StreAming Perception (ASAP) benchmark, which is the first benchmark to evaluate the online performance of vision-centric perception in autonomous driving. On the basis of the 2Hz annotated nuScenes dataset, we first propose an annotation-extending pipeline to generate high-frame-rate labels for the 12Hz raw images. Referring to the practical deployment, the Streaming Perception Under constRained-computation (SPUR) evaluation protocol is further constructed, where the 12Hz inputs are utilized for streaming evaluation under the constraints of different computational resources. In the ASAP benchmark, comprehensive experiment results reveal that the model rank alters under different constraints, suggesting that the model latency and computation budget should be considered as design choices to optimize the practical deployment. To facilitate further research, we establish baselines for camera-based streaming 3D detection, which consistently enhance the streaming performance across various hardware. ASAP project page: https://github.com/JeffWang987/ASAP.

</details>

### Multi-view Adversarial Discriminator: Mine the Non-causal Factors for Object Detection in Unseen Domains. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2304.02950](https://arxiv.org/abs/2304.02950) · 📚 被引 56
- **作者**: Mingjun Xu, Lingyun Qin, Weijie Chen, Shiliang Pu, Lei Zhang
- **🏷️ 机构**: School of Microelectronics and Communication Engineering, Chongqing University, China Hikvision Research Institute,Hangzhou,China
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对目标检测在未知域中因域偏移导致性能下降的问题，现有域泛化方法忽略了公共特征中隐含的非因果因素。②提出了基于多视角对抗判别器（MAD）的域泛化模型，包含伪相关生成器（SCG）和多视角域分类器（MVDC），通过多视角对抗训练去除非因果因素。③相比传统单视角域对抗学习，创新在于利用数据多模态结构，在多个潜在空间中识别并移除非因果因素。④摘要不完整，具体效果未提及，但理论上可提升跨域检测鲁棒性。
- **摘要（英）**: This paper addresses domain shift in object detection by removing non-causal factors from common features. It proposes a Multi-view Adversarial Discriminator (MAD) model with a Spurious Correlations Generator and Multi-View Domain Classifier. The innovation is using multi-view adversarial training to purify domain-invariant features. Specific results are not provided in the incomplete abstract, but the approach aims to improve cross-domain robustness.
- **核心贡献**: 提出多视角对抗判别器以去除目标检测中的非因果因素。
- **创新点**: 利用多视角潜在空间识别并移除非因果特征。
- **结果**: 具体效果未在摘要中提及。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain shift degrades the performance of object detection models in practical applications. To alleviate the influence of domain shift, plenty of previous work try to decouple and learn the domain-invariant (common) features from source domains via domain adversarial learning (DAL). However, inspired by causal mechanisms, we find that previous methods ignore the implicit insignificant non-causal factors hidden in the common features. This is mainly due to the single-view nature of DAL. In this work, we present an idea to remove non-causal factors from common features by multi-view adversarial training on source domains, because we observe that such insignificant non-causal factors may still be significant in other latent spaces (views) due to the multi-mode structure of data. To summarize, we propose a Multi-view Adversarial Discriminator (MAD) based domain generalization model, consisting of a Spurious Correlations Generator (SCG) that increases the diversity of source domain by random augmentation and a Multi-View Domain Classifier (MVDC) that maps features to multiple latent spaces, such that the non-causal factors are removed and the domain-invariant features are purified. Extensive experiments on six benchmarks show our MAD obtains state-of-the-art performance.

</details>

### AIDE: A Vision-Driven Multi-View, Multi-Modal, Multi-Tasking Dataset for Assistive Driving Perception.
- **链接**: [arXiv:2307.13933](https://arxiv.org/abs/2307.13933) · 📚 被引 67
- **作者**: Dingkang Yang, Shuai Huang, Zhi Xu, Zhenpeng Li, Shunli Wang, Mingcheng Li et al.
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University
- **会议**: ICCV 2023

### Cross-view Topology Based Consistent and Complementary Information for Deep Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01781) · 📚 被引 32
- **作者**: Zhibin Dong, Siwei Wang, Jiaqi Jin, Xinwang Liu, En Zhu
- **🏷️ 机构**: National University of Defense Technology,School of Computer,Changsha,China, Intelligent Game and Decision Lab,Beijing,China
- **会议**: ICCV 2023

</details>

### Cross-view Topology Based Consistent and Complementary Information for Deep Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01781) · 📚 被引 32
- **作者**: Zhibin Dong, Siwei Wang, Jiaqi Jin, Xinwang Liu, En Zhu
- **🏷️ 机构**: National University of Defense Technology,School of Computer,Changsha,China, Intelligent Game and Decision Lab,Beijing,China
- **会议**: ICCV 2023

### Neural Pixel Composition for 3D-4D View Synthesis from Multi-Views. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00036) · 📚 被引 8
- **作者**: Aayush Bansal, Michael Zollhöfer
- **🏷️ 机构**: Reality Labs Research,Pittsburgh,USA
- **会议**: CVPR 2023
- **摘要（中）**: ①针对多视图3D-4D视图合成中的神经像素合成问题。②提出了一个基于神经像素合成的框架，用于从多视图图像生成3D-4D表示。③相比现有方法，可能改进了视图合成的质量和一致性。④由于摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper addresses neural pixel composition for 3D-4D view synthesis from multi-views. It proposes a framework for generating 3D-4D representations from multi-view images. The improvement over existing work is unclear due to incomplete abstract. Specific results are not available.
- **核心贡献**: 提出了一个多视图3D-4D视图合成的神经像素组合方法。
- **创新点**: 利用神经像素组合进行3D-4D表示。
- **结果**: 未提供具体效果数据。

### Deep Incomplete Multi-View Clustering with Cross-View Partial Sample and Prototype Alignment. **⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2303.15689](https://arxiv.org/abs/2303.15689) · 📚 被引 102
- **作者**: Jiaqi Jin, Siwei Wang, Zhibin Dong, Xinwang Liu, En Zhu
- **🏷️ 机构**: School of Computer, National University of Defense Technology,Changsha,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对不完整多视图聚类中样本缺失和原型对齐问题。②提出了跨视图部分样本和原型对齐网络（CPSPAN），利用成对观测数据对齐作为代理监督信号，并改进原型对齐。③相比现有对比学习方法，避免了强制视图表示完全一致，保留了视图差异。④摘要不完整，未提供具体效果数据。
- **摘要（英）**: This paper addresses incomplete multi-view clustering with cross-view partial sample and prototype alignment. It proposes CPSPAN, which uses pair-observed data alignment as proxy supervision and improves prototype alignment. The improvement over existing contrastive methods is avoiding exact representation consistency. Specific results are not provided.
- **核心贡献**: 提出了CPSPAN网络用于不完整多视图聚类。
- **创新点**: 利用代理监督信号和原型对齐处理不完整视图。
- **结果**: 未提供具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of existing multi-view clustering relies on the assumption of sample integrity across multiple views. However, in real-world scenarios, samples of multi-view are partially available due to data corruption or sensor failure, which leads to incomplete multi-view clustering study (IMVC). Although several attempts have been proposed to address IMVC, they suffer from the following drawbacks: i) Existing methods mainly adopt cross-view contrastive learning forcing the representations of each sample across views to be exactly the same, which might ignore view discrepancy and flexibility in representations; ii) Due to the absence of non-observed samples across multiple views, the obtained prototypes of clusters might be unaligned and biased, leading to incorrect fusion. To address the above issues, we propose a Cross-view Partial Sample and Prototype Alignment Network (CPSPAN) for Deep Incomplete Multi-view Clustering. Firstly, unlike existing contrastive-based methods, we adopt pair-observed data alignment as 'proxy supervised signals' to guide instance-to-instance correspondence construction among views. Then, regarding of the shifted prototypes in IMVC, we further propose a prototype alignment module to achieve incomplete distribution calibration across views. Extensive experimental results showcase the effectiveness of our proposed modules, attaining noteworthy performance improvements when compared to existing IMVC competitors on benchmark datasets.

</details>

### Learning to Fuse Monocular and Multi-view Cues for Multi-frame Depth Estimation in Dynamic Scenes. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2304.08993](https://arxiv.org/abs/2304.08993) · 📚 被引 41
- **作者**: Rui Li, Dong Gong, Wei Yin, Hao Chen, Yu Zhu, Kaixuan Wang et al.
- **🏷️ 机构**: Northwestern Polytechnical University, The University of New South Wales, DJI
- **会议**: CVPR 2023
- **摘要（中）**: ①针对动态场景中多帧深度估计因多视图几何一致性被破坏而性能下降的问题。②提出了一种学习融合单目和多视图线索的方法，无需启发式掩码，通过跨线索融合（CCF）模块传播静态区域的几何信息到动态区域的单目表示。③相比现有方法，避免了掩码质量不可控和线索融合不充分的问题。④摘要不完整，未提供具体效果数据，但方法在动态场景中具有潜力。
- **摘要（英）**: This paper addresses multi-frame depth estimation in dynamic scenes where multi-view geometric consistency is violated. It proposes a method to learn fusion of monocular and multi-view cues without heuristic masks, using a cross-cue fusion module. The improvement is avoiding mask quality issues and better utilizing both cues. Specific results are not provided.
- **核心贡献**: 提出了动态场景中多帧深度估计的跨线索融合方法。
- **创新点**: 无需掩码的跨线索融合模块。
- **结果**: 未提供具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-frame depth estimation generally achieves high accuracy relying on the multi-view geometric consistency. When applied in dynamic scenes, e.g., autonomous driving, this consistency is usually violated in the dynamic areas, leading to corrupted estimations. Many multi-frame methods handle dynamic areas by identifying them with explicit masks and compensating the multi-view cues with monocular cues represented as local monocular depth or features. The improvements are limited due to the uncontrolled quality of the masks and the underutilized benefits of the fusion of the two types of cues. In this paper, we propose a novel method to learn to fuse the multi-view and monocular cues encoded as volumes without needing the heuristically crafted masks. As unveiled in our analyses, the multi-view cues capture more accurate geometric information in static areas, and the monocular cues capture more useful contexts in dynamic areas. To let the geometric perception learned from multi-view cues in static areas propagate to the monocular representation in dynamic areas and let monocular cues enhance the representation of multi-view cost volume, we propose a cross-cue fusion (CCF) module, which includes the cross-cue attention (CCA) to encode the spatially non-local relative intra-relations from each source to enhance the representation of the other. Experiments on real-world datasets prove the significant effectiveness and generalization ability of the proposed method.

</details>

### OmniCity: Omnipotent City Understanding with Multi-Level and Multi-View Images. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2208.00928](https://arxiv.org/abs/2208.00928) · 📚 被引 30
- **作者**: Weijia Li, Yawen Lai, Linning Xu, Yuanbo Xiangli, Jinhua Yu, Conghui He et al.
- **🏷️ 机构**: Sun Yat-Sen University, SenseTime Research, The Chinese University of Hong Kong
- **会议**: CVPR 2023
- **摘要（中）**: ①针对城市理解中多级别和多视图图像数据集缺乏的问题。②提出了OmniCity数据集，包含多视图卫星图像和街景全景/单视图图像，超过10万张像素级标注图像，来自纽约市2.5万个地理位置。③相比现有基准，图像数量更多、标注类型更丰富、视图更多，并引入了街景全景图像上的细粒度建筑实例分割新任务。④提供了多种任务的基准结果，包括建筑足迹提取、高度估计和分割。
- **摘要（英）**: This paper addresses the lack of multi-level and multi-view datasets for city understanding. It introduces OmniCity, a dataset with over 100K pixel-wise annotated images from satellite and street-level views in NYC. It offers more images, richer annotations, and a new fine-grained building instance segmentation task. Benchmarks for multiple tasks are provided.
- **核心贡献**: 构建了OmniCity多级别多视图城市理解数据集。
- **创新点**: 引入街景全景图像上的细粒度建筑实例分割任务。
- **结果**: 提供了多种任务的基准结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents OmniCity, a new dataset for omnipotent city understanding from multi-level and multi-view images. More precisely, the OmniCity contains multi-view satellite images as well as street-level panorama and mono-view images, constituting over 100K pixel-wise annotated images that are well-aligned and collected from 25K geo-locations in New York City. To alleviate the substantial pixel-wise annotation efforts, we propose an efficient street-view image annotation pipeline that leverages the existing label maps of satellite view and the transformation relations between different views (satellite, panorama, and mono-view). With the new OmniCity dataset, we provide benchmarks for a variety of tasks including building footprint extraction, height estimation, and building plane/instance/fine-grained segmentation. Compared with the existing multi-level and multi-view benchmarks, OmniCity contains a larger number of images with richer annotation types and more views, provides more benchmark results of state-of-the-art models, and introduces a novel task for fine-grained building instance segmentation on street-level panorama images. Moreover, OmniCity provides new problem settings for existing tasks, such as cross-view image matching, synthesis, segmentation, detection, etc., and facilitates the developing of new methods for large-scale city understanding, reconstruction, and simulation. The OmniCity dataset as well as the benchmarks will be available at https://city-super.github.io/omnicity.

</details>

### Multi-Sensor Large-Scale Dataset for Multi-View 3D Reconstruction. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2203.06111](https://arxiv.org/abs/2203.06111) · 📚 被引 14
- **作者**: Oleg Voynov, Gleb Bobrovskikh, Pavel A. Karpyshev, Saveliy Galochkin, Andrei-Timotei Ardelean, Arseniy Bozhenko et al.
- **🏷️ 机构**: Skolkovo Institute of Science and Technology
- **会议**: CVPR 2023
- **摘要（中）**: ①针对多视图3D表面重建中多传感器数据缺乏的问题。②提出了一个新的多传感器数据集，包含来自不同分辨率和模态的RGB和深度数据，如智能手机、RealSense、Kinect等。③相比现有数据集，场景多样且材料属性丰富，对算法具有挑战性。④提供了约140万张图像，覆盖107个场景、100个视角和14种光照条件。
- **摘要（英）**: This paper addresses the lack of multi-sensor data for multi-view 3D reconstruction. It presents a dataset with registered RGB and depth data from various sensors. The scenes are diverse and challenging for existing algorithms. It includes around 1.4 million images of 107 scenes under 14 lighting conditions.
- **核心贡献**: 构建了多传感器多视图3D重建数据集。
- **创新点**: 包含多种传感器和挑战性材料属性。
- **结果**: 提供了大规模图像数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new multi-sensor dataset for multi-view 3D surface reconstruction. It includes registered RGB and depth data from sensors of different resolutions and modalities: smartphones, Intel RealSense, Microsoft Kinect, industrial cameras, and structured-light scanner. The scenes are selected to emphasize a diverse set of material properties challenging for existing algorithms. We provide around 1.4 million images of 107 different scenes acquired from 100 viewing directions under 14 lighting conditions. We expect our dataset will be useful for evaluation and training of 3D reconstruction algorithms and for related tasks. The dataset is available at skoltech3d.appliedai.tech.

</details>

### GCFAgg: Global and Cross-View Feature Aggregation for Multi-View Clustering. **⭐⭐** (相关度: 15%)
- **链接**: [arXiv:2305.06799](https://arxiv.org/abs/2305.06799) · 📚 被引 186
- **作者**: Weiqing Yan, Yuanyang Zhang, Chenlei Lv, Chang Tang, Guanghui Yue, Liang Liao et al.
- **🏷️ 机构**: School of Computer and Control Engineering, Yantai University,Yantai,China,264005, College of Computer Science and Software Engineering, Shenzhen University,Shenzhen,China,518060, School of Computer, China University of Geosciences,Wuhan,China,430074
- **会议**: CVPR 2023
- **摘要（中）**: ①针对多视图聚类中忽略样本结构关系的问题。②提出了全局和跨视图特征聚合网络（GCFAggMVC），通过跨样本和跨视图特征聚合获得共识表示，并用结构引导对比学习对齐。③相比现有视图级聚合方法，充分探索了相似样本的互补性。④摘要不完整，未提供具体效果数据。
- **摘要（英）**: This paper addresses the issue of ignoring sample structure relationships in multi-view clustering. It proposes GCFAggMVC, which uses cross-sample and cross-view feature aggregation and structure-guided contrastive learning. The improvement is exploring complementarity of similar samples. Specific results are not provided.
- **核心贡献**: 提出了GCFAggMVC网络用于多视图聚类。
- **创新点**: 跨样本和跨视图特征聚合。
- **结果**: 未提供具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view clustering can partition data samples into their categories by learning a consensus representation in unsupervised way and has received more and more attention in recent years. However, most existing deep clustering methods learn consensus representation or view-specific representations from multiple views via view-wise aggregation way, where they ignore structure relationship of all samples. In this paper, we propose a novel multi-view clustering network to address these problems, called Global and Cross-view Feature Aggregation for Multi-View Clustering (GCFAggMVC). Specifically, the consensus data presentation from multiple views is obtained via cross-sample and cross-view feature aggregation, which fully explores the complementary ofsimilar samples. Moreover, we align the consensus representation and the view-specific representation by the structure-guided contrastive learning module, which makes the view-specific representations from different samples with high structure relationship similar. The proposed module is a flexible multi-view data representation module, which can be also embedded to the incomplete multi-view data clustering task via plugging our module into other frameworks. Extensive experiments show that the proposed method achieves excellent performance in both complete multi-view data clustering tasks and incomplete multi-view data clustering tasks.

</details>

### Cross-Guided Optimization of Radiance Fields with Multi-View Image Super-Resolution for High-Resolution Novel View Synthesis. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01196) · 📚 被引 14
- **作者**: Youngho Yoon, Kuk-Jin Yoon
- **🏷️ 机构**: Visual Intelligence Lab., KAIST,Korea
- **会议**: CVPR 2023
- **摘要（中）**: 该论文针对高分辨率新视角合成中辐射场优化与多视图图像超分辨率结合的问题，提出了一种交叉引导优化方法。方法通过联合优化辐射场和超分辨率网络，利用多视图一致性约束提升重建质量。相比已有工作，该方法在跨视图信息融合上有所改进。摘要未提供具体数据，效果未知。
- **摘要（英）**: This paper addresses high-resolution novel view synthesis by proposing a cross-guided optimization of radiance fields with multi-view image super-resolution. It jointly optimizes the radiance field and super-resolution network with multi-view consistency constraints. The improvement over prior work lies in cross-view information fusion, but no quantitative results are reported in the abstract.
- **核心贡献**: 提出辐射场与多视图超分辨率的交叉引导优化框架。
- **创新点**: 交叉引导机制联合优化辐射场和超分辨率。
- **结果**: 未提供具体效果数据。

### POEM: Reconstructing Hand in a Point Embedded Multi-view Stereo. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2304.04038](https://arxiv.org/abs/2304.04038) · 📚 被引 14
- **作者**: Lixin Yang, Jian Xu, Licheng Zhong, Xinyu Zhan, Zhicheng Wang, Kejian Wu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Nreal
- **会议**: CVPR 2023
- **摘要（中）**: 该论文针对多视图立体中手部网格重建时3D几何感知特征捕获不足的问题，提出POEM方法，直接在嵌入多视图立体的3D点上操作。方法利用点作为跨视图特征融合的媒介，设计基于点的特征融合和跨集点注意力机制。相比已有工作，POEM直接处理3D点而非将3D信息编码到2D特征，在三个多视图数据集上优于现有最先进方法。
- **摘要（英）**: This paper addresses the challenge of capturing 3D geometrical-aware features in multi-view hand mesh reconstruction by proposing POEM, which directly operates on 3D points embedded in multi-view stereo. It uses points as a medium for cross-view feature fusion and designs point-based feature fusion and cross-set point attention. Compared to prior methods that encode 3D info into 2D features, POEM outperforms state-of-the-art on three multi-view datasets.
- **核心贡献**: 提出基于3D点嵌入的多视图手部重建方法POEM。
- **创新点**: 直接在3D点上进行跨视图特征融合和注意力机制。
- **结果**: 在三个多视图数据集上优于现有最先进方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Enable neural networks to capture 3D geometrical-aware features is essential in multi-view based vision tasks. Previous methods usually encode the 3D information of multi-view stereo into the 2D features. In contrast, we present a novel method, named POEM, that directly operates on the 3D POints Embedded in the Multi-view stereo for reconstructing hand mesh in it. Point is a natural form of 3D information and an ideal medium for fusing features across views, as it has different projections on different views. Our method is thus in light of a simple yet effective idea, that a complex 3D hand mesh can be represented by a set of 3D points that 1) are embedded in the multi-view stereo, 2) carry features from the multi-view images, and 3) encircle the hand. To leverage the power of points, we design two operations: point-based feature fusion and cross-set point attention mechanism. Evaluation on three challenging multi-view datasets shows that POEM outperforms the state-of-the-art in hand mesh reconstruction. Code and models are available for research at https://github.com/lixiny/POEM.

</details>

### Adaptive Patch Deformation for Textureless-Resilient Multi-View Stereo. **⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00162) · 📚 被引 35
- **作者**: Yuesong Wang, Zhaojie Zeng, Tao Guan, Wei Yang, Zhuo Chen, Wenkai Liu et al.
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Huazhong University of Science &#x0026; Technology, School of Computer Science &#x0026; Technology, Zhejiang University
- **会议**: CVPR 2023
- **摘要（中）**: 该论文针对多视图立体中无纹理区域重建鲁棒性问题，提出自适应补丁变形方法。方法通过动态调整匹配补丁的形状以适应无纹理区域，提升重建精度。相比已有工作，该方法在无纹理场景下具有更好的适应性。摘要未提供具体实验数据，效果未知。
- **摘要（英）**: This paper addresses the robustness of multi-view stereo in textureless regions by proposing adaptive patch deformation. It dynamically adjusts the shape of matching patches to handle textureless areas, improving reconstruction accuracy. The improvement over prior work lies in adaptability to textureless scenes, but no quantitative results are provided in the abstract.
- **核心贡献**: 提出自适应补丁变形以增强无纹理区域的多视图立体重建。
- **创新点**: 动态调整补丁形状以适应无纹理区域。
- **结果**: 未提供具体效果数据。

### MetaViewer: Towards A Unified Multi-View Representation.
- **链接**: [arXiv:2303.06329](https://arxiv.org/abs/2303.06329) · 📚 被引 14
- **作者**: Ren Wang, Haoliang Sun, Yuling Ma, Xiaoming Xi, Yilong Yin
- **🏷️ 机构**: Shandong University, Shandong Jianzhu University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing multi-view representation learning methods typically follow a specific-to-uniform pipeline, extracting latent features from each view and then fusing or aligning them to obtain the unified object representation. However, the manually pre-specify fusion functions and view-private redundant information mixed in features potentially degrade the quality of the derived representation. To overcome them, we propose a novel bi-level-optimization-based multi-view learning framework, where the representation is learned in a uniform-to-specific manner. Specifically, we train a meta-learner, namely MetaViewer, to learn fusion and model the view-shared meta representation in outer-level optimization. Start with this meta representation, view-specific base-learners are then required to rapidly reconstruct the corresponding view in inner-level. MetaViewer eventually updates by observing reconstruction processes from uniform to specific over all views, and learns an optimal fusion scheme that separates and filters out view-private information. Extensive experimental results in downstream tasks such as classification and clustering demonstrate the effectiveness of our method.

</details>

### A Light Touch Approach to Teaching Transformers Multi-view Geometry.
- **链接**: [arXiv:2211.15107](https://arxiv.org/abs/2211.15107) · 📚 被引 10
- **作者**: Yash Bhalgat, João F. Henriques, Andrew Zisserman
- **🏷️ 机构**: University of Oxford,Visual Geometry Group
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers are powerful visual learners, in large part due to their conspicuous lack of manually-specified priors. This flexibility can be problematic in tasks that involve multiple-view geometry, due to the near-infinite possible variations in 3D shapes and viewpoints (requiring flexibility), and the precise nature of projective geometry (obeying rigid laws). To resolve this conundrum, we propose a "light touch" approach, guiding visual Transformers to learn multiple-view geometry but allowing them to break free when needed. We achieve this by using epipolar lines to guide the Transformer's cross-attention maps, penalizing attention values outside the epipolar lines and encouraging higher attention along these lines since they contain geometrically plausible matches. Unlike previous methods, our proposal does not require any camera pose information at test-time. We focus on pose-invariant object instance retrieval, where standard Transformer networks struggle, due to the large differences in viewpoint between query and retrieved images. Experimentally, our method outperforms state-of-the-art approaches at object retrieval, without needing pose information at test-time.

</details>

### Instant Multi-View Head Capture through Learnable Registration.
- **链接**: [arXiv:2306.07437](https://arxiv.org/abs/2306.07437) · 📚 被引 25
- **作者**: Timo Bolkart, Tianye Li, Michael J. Black
- **🏷️ 机构**: MPI for Intelligent Systems,T&#x00FC;bingen, University of Southern California
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing methods for capturing datasets of 3D heads in dense semantic correspondence are slow, and commonly address the problem in two separate steps; multi-view stereo (MVS) reconstruction followed by non-rigid registration. To simplify this process, we introduce TEMPEH (Towards Estimation of 3D Meshes from Performances of Expressive Heads) to directly infer 3D heads in dense correspondence from calibrated multi-view images. Registering datasets of 3D scans typically requires manual parameter tuning to find the right balance between accurately fitting the scans surfaces and being robust to scanning noise and outliers. Instead, we propose to jointly register a 3D head dataset while training TEMPEH. Specifically, during training we minimize a geometric loss commonly used for surface registration, effectively leveraging TEMPEH as a regularizer. Our multi-view head inference builds on a volumetric feature representation that samples and fuses features from each view using camera calibration information. To account for partial occlusions and a large capture volume that enables head movements, we use view- and surface-aware feature fusion, and a spatial transformer-based head localization module, respectively. We use raw MVS scans as supervision during training, but, once trained, TEMPEH directly predicts 3D heads in dense correspondence without requiring scans. Predicting one head takes about 0.3 seconds with a median reconstruction error of 0.26 mm, 64% lower than the current state-of-the-art. This enables the efficient capture of large datasets containing multiple people and diverse facial motions. Code, model, and data are publicly available at https://tempeh.is.tue.mpg.de.

</details>

### RIAV-MVS: Recurrent-Indexing an Asymmetric Volume for Multi-View Stereo.
- **链接**: [arXiv:2205.14320](https://arxiv.org/abs/2205.14320) · [代码](https://github.com/oppo-us-research/riav-mvs) · 📚 被引 12
- **作者**: Changjiang Cai, Pan Ji, Qingan Yan, Yi Xu
- **🏷️ 机构**: OPPO US Research Center, InnoPeak Technology, Inc.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a learning-based method for multi-view depth estimation from posed images. Our core idea is a "learning-to-optimize" paradigm that iteratively indexes a plane-sweeping cost volume and regresses the depth map via a convolutional Gated Recurrent Unit (GRU). Since the cost volume plays a paramount role in encoding the multi-view geometry, we aim to improve its construction both at pixel- and frame- levels. At the pixel level, we propose to break the symmetry of the Siamese network (which is typically used in MVS to extract image features) by introducing a transformer block to the reference image (but not to the source images). Such an asymmetric volume allows the network to extract global features from the reference image to predict its depth map. Given potential inaccuracies in the poses between reference and source images, we propose to incorporate a residual pose network to correct the relative poses. This essentially rectifies the cost volume at the frame level. We conduct extensive experiments on real-world MVS datasets and show that our method achieves state-of-the-art performance in terms of both within-dataset evaluation and cross-dataset generalization. Code available: https://github.com/oppo-us-research/riav-mvs.

</details>

### Multi-View Azimuth Stereo via Tangent Space Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00086) · 📚 被引 14
- **作者**: Xu Cao, Hiroaki Santo, Fumio Okura, Yasuyuki Matsushita
- **🏷️ 机构**: Osaka University
- **会议**: CVPR 2023

### GM-NeRF: Learning Generalizable Model-Based Neural Radiance Fields from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01978) · 📚 被引 33
- **作者**: Jianchuan Chen, Wentao Yi, Liqian Ma, Xu Jia, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, ZMO AI Inc.
- **会议**: CVPR 2023

### MAIR: Multi-View Attention Inverse Rendering with 3D Spatially-Varying Lighting Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00811) · 📚 被引 12
- **作者**: Junyong Choi, SeokYeong Lee, Haesol Park, Seung-Won Jung, Ig-Jae Kim, Junghyun Cho
- **🏷️ 机构**: Korea Institute of Science and Technology(KIST), Korea University
- **会议**: CVPR 2023

### 3D Concept Learning and Reasoning from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00888) · 📚 被引 42
- **作者**: Yining Hong, Chunru Lin, Yilun Du, Zhenfang Chen, Joshua B. Tenenbaum, Chuang Gan
- **🏷️ 机构**: UCLA, Shanghai Jiaotong University, MIT CSAIL
- **会议**: CVPR 2023

### StyleGAN Salon: Multi-View Latent Optimization for Pose-Invariant Hairstyle Transfer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00832) · 📚 被引 10
- **作者**: Sasikarn Khwanmuang, Pakkapon Phongthawee, Patsorn Sangkloy, Supasorn Suwajanakorn
- **🏷️ 机构**: VISTEC,Thailand, Phranakhon Rajabhat University,Thailand
- **会议**: CVPR 2023

### Multi-view Inverse Rendering for Large-scale Real-world Indoor Scenes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01203) · 📚 被引 25
- **作者**: Zhen Li, Lingli Wang, Mofang Cheng, Cihui Pan, Jiaqi Yang
- **🏷️ 机构**: Realsee, Northwestern Polytechnical University
- **会议**: CVPR 2023

### NeuralUDF: Learning Unsigned Distance Fields for Multi-View Reconstruction of Surfaces with Arbitrary Topologies.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01996) · 📚 被引 67
- **作者**: Xiaoxiao Long, Cheng Lin, Lingjie Liu, Yuan Liu, Peng Wang, Christian Theobalt et al.
- **🏷️ 机构**: The University of Hong Kong, Tencent Games, Max Planck Institute for Informatics
- **会议**: CVPR 2023

### NeAT: Learning Neural Implicit Surfaces with Arbitrary Topologies from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00032) · 📚 被引 42
- **作者**: Xiaoxu Meng, Weikai Chen, Bo Yang
- **🏷️ 机构**: Digital Content Technology Center, Tencent Games
- **会议**: CVPR 2023

### I2MVFormer: Large Language Model Generated Multi-View Document Supervision for Zero-Shot Image Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01456) · 📚 被引 77
- **作者**: Muhammad Ferjad Naeem, Muhammad Gul Zain Ali Khan, Yongqin Xian, Muhammad Zeshan Afzal, Didier Stricker, Luc Van Gool et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, TUKL, Google
- **会议**: CVPR 2023

### VolRecon: Volume Rendering of Signed Ray Distance Functions for Generalizable Multi-View Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01601) · 📚 被引 52
- **作者**: Yufan Ren, Fangjinhua Wang, Tong Zhang, Marc Pollefeys, Sabine Süsstrunk
- **🏷️ 机构**: IVRL IC EPFL, ETH Zurich,Department of Computer Science
- **会议**: CVPR 2023

### PermutoSDF: Fast Multi-View Reconstruction with Implicit Surfaces Using Permutohedral Lattices.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00818) · 📚 被引 72
- **作者**: Radu Alexandru Rosu, Sven Behnke
- **🏷️ 机构**: University of Bonn,Germany
- **会议**: CVPR 2023

### BKinD-3D: Self-Supervised 3D Keypoint Discovery from Multi-View Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00869)
- **作者**: Jennifer J. Sun, Lili Karashchuk, Amil Dravid, Serim Ryou, Sonia Fereidooni, John C. Tuthill et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Replay: Multi-modal Multi-view Acted Videos for Casual Holography.
- **链接**: [arXiv:2307.12067](https://arxiv.org/abs/2307.12067) · 📚 被引 7
- **作者**: Roman Shapovalov, Yanir Kleiman, Ignacio Rocco, David Novotný, Andrea Vedaldi, Changan Chen et al.
- **🏷️ 机构**: Meta
- **会议**: ICCV 2023

### On the Effects of Self-supervision and Contrastive Alignment in Deep Multi-view Clustering.
- **链接**: [arXiv:2303.09877](https://arxiv.org/abs/2303.09877) · 📚 被引 57
- **作者**: Daniel J. Trosten, Sigurd Løkse, Robert Jenssen, Michael C. Kampffmeyer
- **🏷️ 机构**: UiT The Arctic University of Norway,Department of Physics and Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view image generation attracts particular attention these days due to its promising 3D-related applications, e.g., image viewpoint editing. Most existing methods follow a paradigm where a 3D representation is first synthesized, and then rendered into 2D images to ensure photo-consistency across viewpoints. However, such explicit bias for photo-consistency sacrifices photo-realism, causing geometry artifacts and loss of fine-scale details when these methods are applied to edit real images. To address this issue, we propose ray conditioning, a geometry-free alternative that relaxes the photo-consistency constraint. Our method generates multi-view images by conditioning a 2D GAN on a light field prior. With explicit viewpoint control, state-of-the-art photo-realism and identity consistency, our method is particularly suited for the viewpoint editing task.

</details>

### Multi-view Self-supervised Disentanglement for General Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01128)
- **作者**: Hao Chen, Chenyuan Qu, Yu Zhang, Chen Chen, Jianbo Jiao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Trap Attention: Monocular Depth Estimation with Manual Traps.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00487) · 📚 被引 21
- **作者**: Chao Ning, Hongping Gan
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x0027;an,China,710072
- **会议**: CVPR 2023

### iDisc: Internal Discretization for Monocular Depth Estimation.
- **链接**: [arXiv:2304.06334](https://arxiv.org/abs/2304.06334) · 📚 被引 120
- **作者**: Luigi Piccinelli, Christos Sakaridis, Fisher Yu
- **🏷️ 机构**: ETH Z&#x00FC;rich,Computer Vision Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation is fundamental for 3D scene understanding and downstream applications. However, even under the supervised setup, it is still challenging and ill-posed due to the lack of full geometric constraints. Although a scene can consist of millions of pixels, there are fewer high-level patterns. We propose iDisc to learn those patterns with internal discretized representations. The method implicitly partitions the scene into a set of high-level patterns. In particular, our new module, Internal Discretization (ID), implements a continuous-discrete-continuous bottleneck to learn those concepts without supervision. In contrast to state-of-the-art methods, the proposed model does not enforce any explicit constraints or priors on the depth output. The whole network with the ID module can be trained end-to-end, thanks to the bottleneck module based on attention. Our method sets the new state of the art with significant improvements on NYU-Depth v2 and KITTI, outperforming all published methods on the official KITTI benchmark. iDisc can also achieve state-of-the-art results on surface normal estimation. Further, we explore the model generalization capability via zero-shot testing. We observe the compelling need to promote diversification in the outdoor scenario. Hence, we introduce splits of two autonomous driving datasets, DDAD and Argoverse. Code is available at http://vis.xyz/pub/idisc .

</details>

### Lite-Mono: A Lightweight CNN and Transformer Architecture for Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01778)
- **作者**: Ning Zhang, Francesco Nex, George Vosselman, Norman Kerle
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### PlaneDepth: Self-Supervised Depth Estimation via Orthogonal Planes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02052)
- **作者**: Ruoyu Wang, Zehao Yu, Shenghua Gao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### DualRefine: Self-Supervised Depth and Pose Estimation Through Iterative Epipolar Sampling and Refinement Toward Equilibrium.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00077)
- **作者**: Antyanta Bangunharcana, Ahmed Magd, Kyung-Soo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Fully Self-Supervised Depth Estimation from Defocus Clue.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00882)
- **作者**: Haozhe Si, Bin Zhao, Dong Wang, Yunpeng Gao, Mulin Chen, Zhigang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- Viewpoint Equivariance for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [3d-detection](../3d-detection/Guideline%202023.md)
- CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- FrustumFormer: Adaptive Instance-aware Resampling for Multi-view 3D Detection. → [3d-detection](../3d-detection/Guideline%202023.md)

## 🆕 增量新增

### MUVA: A New Large-Scale Benchmark for Multi-view Amodal Instance Segmentation in the Shopping Scenario. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02148) · 📚 被引 14
- **作者**: Zhixuan Li, Weining Ye, Juan R. Terven, Zachary Bennett, Ying Zheng, Tingting Jiang et al.
- **🏷️ 机构**: Peking University,National Engineering Research Center of Visual Technology, National Key Laboratory for Multimedia Information Processing, School of Computer Science,Beijing,China,100871, AiFi Inc.,California,United States,94010
- **会议**: ICCV 2023
- **摘要（中）**: ①针对购物场景中多视角图像的无遮挡实例分割缺乏大规模基准的问题。②提出了MUVA，一个大规模多视角无遮挡实例分割基准，包含丰富的标注和场景。③相比现有基准，MUVA专门针对购物场景，提供了多视角一致性和遮挡处理的评估标准。④该基准为相关研究提供了标准化的测试平台，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the lack of large-scale benchmarks for multi-view amodal instance segmentation in shopping scenarios. It introduces MUVA, a new benchmark with comprehensive annotations, providing a standardized evaluation platform. The work fills a gap in domain-specific benchmarks, though no quantitative results are reported in the abstract.
- **核心贡献**: 提出了购物场景的多视角无遮挡实例分割基准MUVA。
- **创新点**: 首个针对购物场景的多视角无遮挡实例分割基准。
- **结果**: 提供了标准化评估平台，但未报告具体性能数据。

### Viewpoint Equivariance for Multi-View 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2303.14548](https://arxiv.org/abs/2303.14548) · 📚 被引 33
- **作者**: Dian Chen, Jie Li, Vitor Guizilini, Rares Ambrus, Adrien Gaidon
- **🏷️ 机构**: Toyota Research Institute (TRI),Los Altos,CA
- **会议**: CVPR 2023
- **摘要（中）**: 针对多视图3D检测中缺乏多视图一致性利用的问题，提出了VEDet框架，通过视角等变性和多视图几何提升定位精度。方法上，采用基于查询的Transformer架构，在输入层用3D透视几何的位置编码增强图像特征，并在输出层设计视角条件查询，通过多视图一致性学习视角等变性。相比已有工作，该方法在输入和损失层面注入多视图几何，提供了丰富的几何线索。在nuScenes基准上取得了最先进性能，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the underutilization of multi-view consistency in 3D object detection. It introduces VEDet, a query-based transformer framework that injects 3D geometry as positional encodings and enforces viewpoint equivariance via view-conditioned queries. This achieves state-of-the-art performance on nuScenes, demonstrating the benefit of multi-view geometry.
- **核心贡献**: 提出了VEDet框架，利用视角等变性和多视图几何提升3D检测精度。
- **创新点**: 在输入和损失层面引入多视图几何，实现视角等变学习。
- **结果**: 在nuScenes基准上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection from visual sensors is a cornerstone capability of robotic systems. State-of-the-art methods focus on reasoning and decoding object bounding boxes from multi-view camera input. In this work we gain intuition from the integral role of multi-view consistency in 3D scene understanding and geometric learning. To this end, we introduce VEDet, a novel 3D object detection framework that exploits 3D multi-view geometry to improve localization through viewpoint awareness and equivariance. VEDet leverages a query-based transformer architecture and encodes the 3D scene by augmenting image features with positional encodings from their 3D perspective geometry. We design view-conditioned queries at the output level, which enables the generation of multiple virtual frames during training to learn viewpoint equivariance by enforcing multi-view consistency. The multi-view geometry injected at the input level as positional encodings and regularized at the loss level provides rich geometric cues for 3D object detection, leading to state-of-the-art performance on the nuScenes benchmark. The code and model are made available at https://github.com/TRI-ML/VEDet.

</details>

### X3KD: Knowledge Distillation Across Modalities, Tasks and Stages for Multi-Camera 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01282) · 📚 被引 44
- **作者**: Marvin Klingner, Shubhankar Borse, Varun Ravi Kumar, Behnaz Rezaei, Venkatraman Narayanan, Senthil Kumar Yogamani et al.
- **🏷️ 机构**: Automated Driving, Qualcomm Technologies, Inc., Qualcomm AI Research, an initiative of Qualcomm Technologies, Inc., Automated Driving, QT Technologies Ireland Limited
- **会议**: CVPR 2023
- **摘要（中）**: ①针对多相机3D检测中跨模态、跨任务和跨阶段知识迁移不足的问题。②提出了X3KD框架，通过知识蒸馏在模态（LiDAR到相机）、任务（检测到分割）和训练阶段之间传递信息，增强相机模型的感知能力。③相比单一模态或单任务蒸馏，该方法实现了更全面的知识迁移，提升了多相机检测的精度和鲁棒性。④在nuScenes等数据集上验证了有效性，显著提升了多相机3D检测性能。
- **摘要（英）**: This paper addresses the lack of comprehensive knowledge transfer in multi-camera 3D detection. X3KD performs distillation across modalities, tasks, and training stages, improving camera-based detection accuracy. Experiments on nuScenes demonstrate significant performance gains.
- **核心贡献**: 提出跨模态、任务和阶段的统一知识蒸馏框架。
- **创新点**: 多维度知识蒸馏策略结合多相机3D检测。
- **结果**: 显著提升多相机3D检测精度。

### Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2303.08686](https://arxiv.org/abs/2303.08686) · 📚 被引 23
- **作者**: Runzhou Tao, Wencheng Han, Zhongying Qiu, Cheng-Zhong Xu, Jianbing Shen
- **🏷️ 机构**: Beijing Institute of Technology, SKL-IOTSC, CIS, University of Macau, QCraft
- **会议**: CVPR 2023
- **摘要（中）**: ①这篇论文针对单目3D目标检测依赖LiDAR点云标注、训练与推理不一致且数据成本高的问题。②提出了仅需2D图像标签的弱监督方法，利用投影一致性、多视图一致性和方向一致性三种约束，并设计了基于这些一致性的弱监督架构，同时提出新的2D方向标注方法以指导旋转方向预测。③相比已有工作，该方法消除了训练阶段对3D标注的依赖，降低了数据收集成本，并增强了方向预测的准确性。④实验表明，该方法性能与部分全监督方法相当，且作为预训练方法时显著优于对应的全监督基线。
- **摘要（英）**: This paper tackles the issue that monocular 3D object detection relies on LiDAR point cloud annotations for training, causing inconsistency with inference and high data costs. It proposes a weakly supervised method using only 2D image labels, leveraging projection, multi-view, and direction consistency, along with a new 2D direction labeling scheme. Compared to existing works, it removes the need for 3D annotations during training and improves rotation prediction. Experiments show comparable performance to some fully supervised methods, and as a pretraining approach, it significantly outperforms the fully supervised baseline.
- **核心贡献**: 提出仅用2D标签的弱监督单目3D检测方法，利用多视图和方向一致性训练。
- **创新点**: 引入方向一致性约束和2D方向标注方法，提升旋转预测精度。
- **结果**: 性能与部分全监督方法相当，预训练时显著优于全监督基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection has become a mainstream approach in automatic driving for its easy application. A prominent advantage is that it does not need LiDAR point clouds during the inference. However, most current methods still rely on 3D point cloud data for labeling the ground truths used in the training phase. This inconsistency between the training and inference makes it hard to utilize the large-scale feedback data and increases the data collection expenses. To bridge this gap, we propose a new weakly supervised monocular 3D objection detection method, which can train the model with only 2D labels marked on images. To be specific, we explore three types of consistency in this task, i.e. the projection, multi-view and direction consistency, and design a weakly-supervised architecture based on these consistencies. Moreover, we propose a new 2D direction labeling method in this task to guide the model for accurate rotation direction prediction. Experiments show that our weakly-supervised method achieves comparable performance with some fully supervised methods. When used as a pre-training method, our model can significantly outperform the corresponding fully-supervised baseline with only 1/3 3D labels. https://github.com/weakmono3d/weakmono3d

</details>

### CAPE: Camera View Position Embedding for Multi-View 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2303.10209](https://arxiv.org/abs/2303.10209) · 📚 被引 53
- **作者**: Kaixin Xiong, Shi Gong, Xiaoqing Ye, Xiao Tan, Ji Wan, Errui Ding et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Baidu Inc.
- **会议**: CVPR 2023
- **摘要（中）**: 针对基于查询的多视角3D检测中全局3D位置编码导致视图变换学习困难的问题，提出CAPE，在相机视图局部坐标系下构建3D位置嵌入，避免编码相机外参。并扩展至时间建模，利用历史查询和自运动编码提升检测。在nuScenes上达到61.0% NDS和52.5% mAP，为无激光雷达方法中的最优。
- **摘要（英）**: To ease view transformation learning, we propose CAPE, which uses camera-view local 3D position embeddings, avoiding extrinsic encoding. Extended to temporal modeling with ego-motion, it achieves state-of-the-art 61.0% NDS and 52.5% mAP on nuScenes among LiDAR-free methods.
- **核心贡献**: 提出相机视角位置嵌入，改进多视角3D检测。
- **创新点**: 局部坐标系下的位置编码，简化视图变换。
- **结果**: 在nuScenes上取得SoTA性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we address the problem of detecting 3D objects from multi-view images. Current query-based methods rely on global 3D position embeddings (PE) to learn the geometric correspondence between images and 3D space. We claim that directly interacting 2D image features with global 3D PE could increase the difficulty of learning view transformation due to the variation of camera extrinsics. Thus we propose a novel method based on CAmera view Position Embedding, called CAPE. We form the 3D position embeddings under the local camera-view coordinate system instead of the global coordinate system, such that 3D position embedding is free of encoding camera extrinsic parameters. Furthermore, we extend our CAPE to temporal modeling by exploiting the object queries of previous frames and encoding the ego-motion for boosting 3D object detection. CAPE achieves state-of-the-art performance (61.0% NDS and 52.5% mAP) among all LiDAR-free methods on nuScenes dataset. Codes and models are available on \href{https://github.com/PaddlePaddle/Paddle3D}{Paddle3D} and \href{https://github.com/kaixinbear/CAPE}{PyTorch Implementation}.

</details>

### Collaboration Helps Camera Overtake LiDAR in 3D Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2303.13560](https://arxiv.org/abs/2303.13560) · 📚 被引 108
- **作者**: Yue Hu, Yifan Lu, Runsheng Xu, Weidi Xie, Siheng Chen, Yanfeng Wang
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center, University of California,Los Angeles, Shanghai AI Laboratory
- **会议**: CVPR 2023
- **摘要（中）**: ①针对纯相机3D检测中深度估计不准的问题，提出通过多智能体协作来改进。②提出了CoCa3D，一种协作式纯相机3D检测方法，使智能体共享互补信息，并优化通信效率选择最有信息量的线索。③相比单智能体方法，多视角共享信息消除了深度估计的歧义，并补充了遮挡和远距离区域。④在DAIR-V2X、OPV2V+和CoPerception-UAVs+上，AP@70分别提升了44.21%、30.60%和12.59%，显著优于SOTA。
- **摘要（英）**: This paper addresses depth estimation challenges in camera-only 3D detection by introducing multi-agent collaboration. CoCa3D enables agents to share complementary information, optimizing communication efficiency, and disambiguates depth from multiple viewpoints. It achieves significant improvements of 44.21%, 30.60%, and 12.59% on DAIR-V2X, OPV2V+, and CoPerception-UAVs+ for AP@70, respectively.
- **核心贡献**: 提出协作式纯相机3D检测方法CoCa3D。
- **创新点**: 利用多智能体协作和通信优化改进深度估计。
- **结果**: 在多个数据集上显著提升AP@70。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-only 3D detection provides an economical solution with a simple configuration for localizing objects in 3D space compared to LiDAR-based detection systems. However, a major challenge lies in precise depth estimation due to the lack of direct 3D measurements in the input. Many previous methods attempt to improve depth estimation through network designs, e.g., deformable layers and larger receptive fields. This work proposes an orthogonal direction, improving the camera-only 3D detection by introducing multi-agent collaborations. Our proposed collaborative camera-only 3D detection (CoCa3D) enables agents to share complementary information with each other through communication. Meanwhile, we optimize communication efficiency by selecting the most informative cues. The shared messages from multiple viewpoints disambiguate the single-agent estimated depth and complement the occluded and long-range regions in the single-agent view. We evaluate CoCa3D in one real-world dataset and two new simulation datasets. Results show that CoCa3D improves previous SOTA performances by 44.21% on DAIR-V2X, 30.60% on OPV2V+, 12.59% on CoPerception-UAVs+ for AP@70. Our preliminary results show a potential that with sufficient collaboration, the camera might overtake LiDAR in some practical scenarios. We released the dataset and code at https://siheng-chen.github.io/dataset/CoPerception+ and https://github.com/MediaBrain-SJTU/CoCa3D.

</details>

### Robust Multiview Point Cloud Registration with Reliable Pose Graph Initialization and History Reweighting. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00917) · 📚 被引 45
- **作者**: Haiping Wang, Yuan Liu, Zhen Dong, Yulan Guo, Yu-Shen Liu, Wenping Wang et al.
- **🏷️ 机构**: Wuhan University, The University of Hong Kong, Sun Yat-sen University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对多视角点云配准中位姿图初始化和历史信息利用不足的问题。②提出了鲁棒的多视角点云配准方法，包括可靠的位姿图初始化和历史重加权策略。③相比现有方法，改进了初始化和优化过程，提高了配准鲁棒性。④摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses robust multiview point cloud registration by improving pose graph initialization and history reweighting. The proposed method enhances robustness in registration, but no quantitative results are provided in the abstract.
- **核心贡献**: 提出鲁棒的多视角点云配准方法。
- **创新点**: 改进位姿图初始化和历史重加权。
- **结果**: 摘要未提供具体性能数据。

### TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00138) · 📚 被引 35
- **作者**: Shaoheng Fang, Zi Wang, Yiqi Zhong, Junhao Ge, Siheng Chen
- **🏷️ 机构**: Shanghai Jiao Tong University,Cooperative Medianet Innovation Center, University of Southern California,Department of Computer Science
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视觉中心自动驾驶中联合感知和预测的时序BEV表示学习问题。②提出了TBP-Former，学习时序BEV金字塔，用于联合3D目标检测和运动预测。③相比现有BEV方法，TBP-Former通过金字塔结构捕获多尺度时序信息，提升感知和预测的协同性。④摘要未提供具体性能数据，但方法在架构上具有创新性。
- **摘要（英）**: This paper addresses joint perception and prediction in vision-centric autonomous driving by learning temporal BEV pyramids. TBP-Former captures multi-scale temporal information for improved 3D detection and motion prediction. The approach offers architectural innovation, though quantitative results are not detailed in the abstract.
- **核心贡献**: 提出时序BEV金字塔学习框架TBP-Former。
- **创新点**: 利用金字塔结构捕获多尺度时序信息。
- **结果**: 摘要未提供具体性能数据。

### Sample-level Multi-view Graph Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02295) · 📚 被引 48
- **作者**: Yuze Tan, Yixi Liu, Shudong Huang, Wentao Feng, Jiancheng Lv
- **🏷️ 机构**: Sichuan University
- **会议**: CVPR 2023

### FrustumFormer: Adaptive Instance-aware Resampling for Multi-view 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00493) · 📚 被引 27
- **作者**: Yuqi Wang, Yuntao Chen, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, HKISI&#x005F;CAS,Centre for Artificial Intelligence and Robotics
- **会议**: CVPR 2023

### Highly Confident Local Structure Based Consensus Graph Learning for Incomplete Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01508) · 📚 被引 51
- **作者**: Jie Wen, Chengliang Liu, Gehui Xu, Zhihao Wu, Chao Huang, Lunke Fei et al.
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen Key Laboratory of Visual Object Detection and Recognition,Shenzhen,China, School of Cyber Science and Technology, Shenzhen Campus of Sun Yat-sen University,Shenzhen,China, School of Computer Science and Technology, Guangdong University of Technology,Guangzhou,China
- **会议**: CVPR 2023

### CutMIB: Boosting Light Field Super-Resolution via Multi-View Image Blending.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00167) · 📚 被引 51
- **作者**: Zeyu Xiao, Yutong Liu, Ruisheng Gao, Zhiwei Xiong
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2023

### Exploring and Exploiting Uncertainty for Incomplete Multi-View Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01903) · 📚 被引 44
- **作者**: Mengyao Xie, Zongbo Han, Changqing Zhang, Yichen Bai, Qinghua Hu
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University
- **会议**: CVPR 2023

### High-fidelity 3D GAN Inversion by Pseudo-multi-view Optimization.
- **链接**: [arXiv:2211.15662](https://arxiv.org/abs/2211.15662) · 📚 被引 51
- **作者**: Jiaxin Xie, Hao Ouyang, Jingtan Piao, Chenyang Lei, Qifeng Chen
- **🏷️ 机构**: HKUST, CUHK,MMLab, CAIR, HKISI-CAS
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a high-fidelity 3D generative adversarial network (GAN) inversion framework that can synthesize photo-realistic novel views while preserving specific details of the input image. High-fidelity 3D GAN inversion is inherently challenging due to the geometry-texture trade-off in 3D inversion, where overfitting to a single view input image often damages the estimated geometry during the latent optimization. To solve this challenge, we propose a novel pipeline that builds on the pseudo-multi-view estimation with visibility analysis. We keep the original textures for the visible parts and utilize generative priors for the occluded parts. Extensive experiments show that our approach achieves advantageous reconstruction and novel view synthesis quality over state-of-the-art methods, even for images with out-of-distribution textures. The proposed pipeline also enables image attribute editing with the inverted latent code and 3D-aware texture modification. Our approach enables high-fidelity 3D rendering from a single image, which is promising for various applications of AI-generated 3D content.

</details>

### NEF: Neural Edge Fields for 3D Parametric Curve Reconstruction from Multi-View Images.
- **链接**: [arXiv:2303.07653](https://arxiv.org/abs/2303.07653) · 📚 被引 35
- **作者**: Yunfan Ye, Renjiao Yi, Zhirui Gao, Chenyang Zhu, Zhiping Cai, Kai Xu
- **🏷️ 机构**: National University of Defense Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the problem of reconstructing 3D feature curves of an object from a set of calibrated multi-view images. To do so, we learn a neural implicit field representing the density distribution of 3D edges which we refer to as Neural Edge Field (NEF). Inspired by NeRF, NEF is optimized with a view-based rendering loss where a 2D edge map is rendered at a given view and is compared to the ground-truth edge map extracted from the image of that view. The rendering-based differentiable optimization of NEF fully exploits 2D edge detection, without needing a supervision of 3D edges, a 3D geometric operator or cross-view edge correspondence. Several technical designs are devised to ensure learning a range-limited and view-independent NEF for robust edge extraction. The final parametric 3D curves are extracted from NEF with an iterative optimization method. On our benchmark with synthetic data, we demonstrate that NEF outperforms existing state-of-the-art methods on all metrics. Project page: https://yunfan1202.github.io/NEF/.

</details>

### MVImgNet: A Large-scale Dataset of Multi-view Images.
- **链接**: [arXiv:2303.06042](https://arxiv.org/abs/2303.06042) · 📚 被引 131
- **作者**: Xianggang Yu, Mutian Xu, Yidan Zhang, Haolin Liu, Chongjie Ye, Yushuang Wu et al.
- **🏷️ 机构**: FNii, CUHKSZ, SSE, CUHKSZ
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Being data-driven is one of the most iconic properties of deep learning algorithms. The birth of ImageNet drives a remarkable trend of "learning from large-scale data" in computer vision. Pretraining on ImageNet to obtain rich universal representations has been manifested to benefit various 2D visual tasks, and becomes a standard in 2D vision. However, due to the laborious collection of real-world 3D data, there is yet no generic dataset serving as a counterpart of ImageNet in 3D vision, thus how such a dataset can impact the 3D community is unraveled. To remedy this defect, we introduce MVImgNet, a large-scale dataset of multi-view images, which is highly convenient to gain by shooting videos of real-world objects in human daily life. It contains 6.5 million frames from 219,188 videos crossing objects from 238 classes, with rich annotations of object masks, camera parameters, and point clouds. The multi-view attribute endows our dataset with 3D-aware signals, making it a soft bridge between 2D and 3D vision. We conduct pilot studies for probing the potential of MVImgNet on a variety of 3D and 2D visual tasks, including radiance field reconstruction, multi-view stereo, and view-consistent image understanding, where MVImgNet demonstrates promising performance, remaining lots of possibilities for future explorations. Besides, via dense reconstruction on MVImgNet, a 3D object point cloud dataset is derived, called MVPNet, covering 87,200 samples from 150 categories, with the class label on each point cloud. Experiments show that MVPNet can benefit the real-world 3D object classification while posing new challenges to point cloud understanding. MVImgNet and MVPNet will be publicly available, hoping to inspire the broader vision community.

</details>

### 3D-aware Facial Landmark Detection via Multi-view Consistent Training on Synthetic Data.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01226) · 📚 被引 17
- **作者**: Libing Zeng, Lele Chen, Wentao Bao, Zhong Li, Yi Xu, Junsong Yuan et al.
- **🏷️ 机构**: Texas A&#x0026;M University, InnoPeak Technology, Inc,OPPO US Research Center, Michigan State University
- **会议**: CVPR 2023

### NeuralDome: A Neural Modeling Pipeline on Multi-View Human-Object Interactions.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00853) · 📚 被引 33
- **作者**: Juze Zhang, Haimin Luo, Hongdi Yang, Xinru Xu, Qianyang Wu, Ye Shi et al.
- **🏷️ 机构**: ShanghaiTech University
- **会议**: CVPR 2023

### GeoMVSNet: Learning Multi-View Stereo with Geometry Perception.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02060) · 📚 被引 119
- **作者**: Zhe Zhang, Rui Peng, Yuxi Hu, Ronggang Wang
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University,China, School of Science and Engineering, The Chinese University of Hong Kong,Shenzhen,China
- **会议**: CVPR 2023

### Multi-View Stereo Representation Revist: Region-Aware MVSNet.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01667) · 📚 被引 28
- **作者**: Yisu Zhang, Jianke Zhu, Lixiang Lin
- **🏷️ 机构**: Zhejiang University
- **会议**: CVPR 2023

### NeuFace: Realistic 3D Neural Face Rendering from Multi-View Images.
- **链接**: [arXiv:2303.14092](https://arxiv.org/abs/2303.14092) · 📚 被引 18
- **作者**: Mingwu Zheng, Haiyu Zhang, Hongyu Yang, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, Institute of Artificial Intelligence, Beihang University,Beijing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Realistic face rendering from multi-view images is beneficial to various computer vision and graphics applications. Due to the complex spatially-varying reflectance properties and geometry characteristics of faces, however, it remains challenging to recover 3D facial representations both faithfully and efficiently in the current studies. This paper presents a novel 3D face rendering model, namely NeuFace, to learn accurate and physically-meaningful underlying 3D representations by neural rendering techniques. It naturally incorporates the neural BRDFs into physically based rendering, capturing sophisticated facial geometry and appearance clues in a collaborative manner. Specifically, we introduce an approximated BRDF integration and a simple yet new low-rank prior, which effectively lower the ambiguities and boost the performance of the facial BRDFs. Extensive experiments demonstrate the superiority of NeuFace in human face rendering, along with a decent generalization ability to common objects.

</details>

### Relightable Neural Human Assets from Multi-view Gradient Illuminations.
- **链接**: [arXiv:2212.07648](https://arxiv.org/abs/2212.07648) · 📚 被引 24
- **作者**: Taotao Zhou, Kai He, Di Wu, Teng Xu, Qixuan Zhang, Kuixiang Shao et al.
- **🏷️ 机构**: ShanghaiTech University, University of Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human modeling and relighting are two fundamental problems in computer vision and graphics, where high-quality datasets can largely facilitate related research. However, most existing human datasets only provide multi-view human images captured under the same illumination. Although valuable for modeling tasks, they are not readily used in relighting problems. To promote research in both fields, in this paper, we present UltraStage, a new 3D human dataset that contains more than 2,000 high-quality human assets captured under both multi-view and multi-illumination settings. Specifically, for each example, we provide 32 surrounding views illuminated with one white light and two gradient illuminations. In addition to regular multi-view images, gradient illuminations help recover detailed surface normal and spatially-varying material maps, enabling various relighting applications. Inspired by recent advances in neural representation, we further interpret each example into a neural human asset which allows novel view synthesis under arbitrary lighting conditions. We show our neural human assets can achieve extremely high capture performance and are capable of representing fine details such as facial wrinkles and cloth folds. We also validate UltraStage in single image relighting tasks, training neural networks with virtual relighted data from neural assets and demonstrating realistic rendering improvements over prior arts. UltraStage will be publicly available to the community to stimulate significant future developments in various human modeling and rendering tasks. The dataset is available at https://miaoing.github.io/RNHA.

</details>

### Multi-View Reconstruction Using Signed Ray Distance Functions (SRDF).
- **链接**: [arXiv:2209.00082](https://arxiv.org/abs/2209.00082) · 📚 被引 11
- **作者**: Pierre Zins, Yuanlu Xu, Edmond Boyer, Stefanie Wuhrer, Tony Tung
- **🏷️ 机构**: Inria centre at the University Grenoble Alpes, Meta Reality Labs,Sausalito,USA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we investigate a new optimization framework for multi-view 3D shape reconstructions. Recent differentiable rendering approaches have provided breakthrough performances with implicit shape representations though they can still lack precision in the estimated geometries. On the other hand multi-view stereo methods can yield pixel wise geometric accuracy with local depth predictions along viewing rays. Our approach bridges the gap between the two strategies with a novel volumetric shape representation that is implicit but parameterized with pixel depths to better materialize the shape surface with consistent signed distances along viewing rays. The approach retains pixel-accuracy while benefiting from volumetric integration in the optimization. To this aim, depths are optimized by evaluating, at each 3D location within the volumetric discretization, the agreement between the depth prediction consistency and the photometric consistency for the corresponding pixels. The optimization is agnostic to the associated photo-consistency term which can vary from a median-based baseline to more elaborate criteria learned functions. Our experiments demonstrate the benefit of the volumetric integration with depth predictions. They also show that our approach outperforms existing approaches over standard 3D benchmarks with better geometry estimations.

</details>

### Standing Between Past and Future: Spatio-Temporal Modeling for Multi-Camera 3D Multi-Object Tracking.
- **链接**: [arXiv:2302.03802](https://arxiv.org/abs/2302.03802) · 📚 被引 65
- **作者**: Ziqi Pang, Jie Li, Pavel Tokmakov, Dian Chen, Sergey Zagoruyko, Yu-Xiong Wang
- **🏷️ 机构**: University of Illinois Urbana-Champaign, Toyota Research Institute, Woven Planet Level-5
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work proposes an end-to-end multi-camera 3D multi-object tracking (MOT) framework. It emphasizes spatio-temporal continuity and integrates both past and future reasoning for tracked objects. Thus, we name it "Past-and-Future reasoning for Tracking" (PF-Track). Specifically, our method adapts the "tracking by attention" framework and represents tracked instances coherently over time with object queries. To explicitly use historical cues, our "Past Reasoning" module learns to refine the tracks and enhance the object features by cross-attending to queries from previous frames and other objects. The "Future Reasoning" module digests historical information and predicts robust future trajectories. In the case of long-term occlusions, our method maintains the object positions and enables re-association by integrating motion predictions. On the nuScenes dataset, our method improves AMOTA by a large margin and remarkably reduces ID-Switches by 90% compared to prior approaches, which is an order of magnitude less. The code and models are made available at https://github.com/TRI-ML/PF-Track.

</details>

### Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection.
- **链接**: [arXiv:2303.11926](https://arxiv.org/abs/2303.11926) · 📚 被引 277
- **作者**: Shihao Wang, Yingfei Liu, Tiancai Wang, Ying Li, Xiangyu Zhang
- **🏷️ 机构**: Beijing Institute of Technology, MEGVII Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a long-sequence modeling framework, named StreamPETR, for multi-view 3D object detection. Built upon the sparse query design in the PETR series, we systematically develop an object-centric temporal mechanism. The model is performed in an online manner and the long-term historical information is propagated through object queries frame by frame. Besides, we introduce a motion-aware layer normalization to model the movement of the objects. StreamPETR achieves significant performance improvements only with negligible computation cost, compared to the single-frame baseline. On the standard nuScenes benchmark, it is the first online multi-view method that achieves comparable performance (67.6% NDS & 65.3% AMOTA) with lidar-based methods. The lightweight version realizes 45.0% mAP and 31.7 FPS, outperforming the state-of-the-art method (SOLOFusion) by 2.3% mAP and 1.8x faster FPS. Code has been available at https://github.com/exiawsh/StreamPETR.git.

</details>

### 3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00331) · 📚 被引 37
- **作者**: Changyong Shu, Jiajun Deng, Fisher Yu, Yifan Liu
- **🏷️ 机构**: Houmo AI, University of Sydney, ETH Z&#x00FC;rich
- **会议**: ICCV 2023

### ImGeoNet: Image-induced Geometry-aware Voxel Representation for Multi-view 3D Object Detection.
- **链接**: [arXiv:2308.09098](https://arxiv.org/abs/2308.09098) · 📚 被引 16
- **作者**: Tao Tu, Shun-Po Chuang, Yu-Lun Liu, Cheng Sun, Ke Zhang, Donna Roy et al.
- **🏷️ 机构**: National Tsing Hua University, National Taiwan University, National Yang Ming Chiao Tung University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose ImGeoNet, a multi-view image-based 3D object detection framework that models a 3D space by an image-induced geometry-aware voxel representation. Unlike previous methods which aggregate 2D features into 3D voxels without considering geometry, ImGeoNet learns to induce geometry from multi-view images to alleviate the confusion arising from voxels of free space, and during the inference phase, only images from multiple views are required. Besides, a powerful pre-trained 2D feature extractor can be leveraged by our representation, leading to a more robust performance. To evaluate the effectiveness of ImGeoNet, we conduct quantitative and qualitative experiments on three indoor datasets, namely ARKitScenes, ScanNetV2, and ScanNet200. The results demonstrate that ImGeoNet outperforms the current state-of-the-art multi-view image-based method, ImVoxelNet, on all three datasets in terms of detection accuracy. In addition, ImGeoNet shows great data efficiency by achieving results comparable to ImVoxelNet with 100 views while utilizing only 40 views. Furthermore, our studies indicate that our proposed image-induced geometry-aware representation can enable image-based methods to attain superior detection accuracy than the seminal point cloud-based method, VoteNet, in two practical scenarios: (1) scenarios where point clouds are sparse and noisy, such as in ARKitScenes, and (2) scenarios involve diverse object classes, particularly classes of small objects, as in the case in ScanNet200.

</details>

### Pixel-Aligned Recurrent Queries for Multi-View 3D Object Detection.
- **链接**: [arXiv:2310.01401](https://arxiv.org/abs/2310.01401) · 📚 被引 9
- **作者**: Yiming Xie, Huaizu Jiang, Georgia Gkioxari, Julian Straub
- **🏷️ 机构**: Northeastern University, California Institute of Technology, Meta Reality Labs Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present PARQ - a multi-view 3D object detector with transformer and pixel-aligned recurrent queries. Unlike previous works that use learnable features or only encode 3D point positions as queries in the decoder, PARQ leverages appearance-enhanced queries initialized from reference points in 3D space and updates their 3D location with recurrent cross-attention operations. Incorporating pixel-aligned features and cross attention enables the model to encode the necessary 3D-to-2D correspondences and capture global contextual information of the input images. PARQ outperforms prior best methods on the ScanNet and ARKitScenes datasets, learns and detects faster, is more robust to distribution shifts in reference points, can leverage additional input views without retraining, and can adapt inference compute by changing the number of recurrent iterations.

</details>

### NeRF-Det: Learning Geometry-Aware Volumetric Representation for Multi-View 3D Object Detection.
- **链接**: [arXiv:2307.14620](https://arxiv.org/abs/2307.14620) · 📚 被引 56
- **作者**: Chenfeng Xu, Bichen Wu, Ji Hou, Sam S. Tsai, Ruilong Li, Jialiang Wang et al.
- **🏷️ 机构**: University of California,Berkeley, Meta AI
- **会议**: ICCV 2023

### SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection.
- **链接**: [arXiv:2307.11477](https://arxiv.org/abs/2307.11477) · 📚 被引 42
- **作者**: Jinqing Zhang, Yanan Zhang, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,Beijing,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the pure camera-based Bird's-Eye-View (BEV) perception provides a feasible solution for economical autonomous driving. However, the existing BEV-based multi-view 3D detectors generally transform all image features into BEV features, without considering the problem that the large proportion of background information may submerge the object information. In this paper, we propose Semantic-Aware BEV Pooling (SA-BEVPool), which can filter out background information according to the semantic segmentation of image features and transform image features into semantic-aware BEV features. Accordingly, we propose BEV-Paste, an effective data augmentation strategy that closely matches with semantic-aware BEV feature. In addition, we design a Multi-Scale Cross-Task (MSCT) head, which combines task-specific and cross-task information to predict depth distribution and semantic segmentation more accurately, further improving the quality of semantic-aware BEV feature. Finally, we integrate the above modules into a novel multi-view 3D object detection framework, namely SA-BEV. Experiments on nuScenes show that SA-BEV achieves state-of-the-art performance. Code has been available at https://github.com/mengtan00/SA-BEV.git.

</details>

### UniFusion: Unified Multi-view Fusion Transformer for Spatial-Temporal Representation in Bird's-Eye-View.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00798) · 📚 被引 50
- **作者**: Zequn Qin, Jingyu Chen, Chao Chen, Xiaozhi Chen, Xi Li
- **🏷️ 机构**: Zhejiang University,College of Computer Science &amp; Technology, DJI
- **会议**: ICCV 2023

### ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01410) · 📚 被引 47
- **作者**: Zoey Guo, Yiwen Tang, Ray Zhang, Dong Wang, Zhigang Wang, Bin Zhao et al.
- **🏷️ 机构**: Shanghai Artificial Intelligence Laboratory
- **会议**: ICCV 2023

### Ray Conditioning: Trading Photo-consistency for Photo-realism in Multi-view Image Generation.
- **链接**: [arXiv:2304.13681](https://arxiv.org/abs/2304.13681) · 📚 被引 7
- **作者**: Eric Ming Chen, Sidhanth Holalkere, Ruyu Yan, Kai Zhang, Abe Davis
- **🏷️ 机构**: Cornell University, Adobe Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view image generation attracts particular attention these days due to its promising 3D-related applications, e.g., image viewpoint editing. Most existing methods follow a paradigm where a 3D representation is first synthesized, and then rendered into 2D images to ensure photo-consistency across viewpoints. However, such explicit bias for photo-consistency sacrifices photo-realism, causing geometry artifacts and loss of fine-scale details when these methods are applied to edit real images. To address this issue, we propose ray conditioning, a geometry-free alternative that relaxes the photo-consistency constraint. Our method generates multi-view images by conditioning a 2D GAN on a light field prior. With explicit viewpoint control, state-of-the-art photo-realism and identity consistency, our method is particularly suited for the viewpoint editing task.

</details>

### TEMPO: Efficient Multi-View Pose Estimation, Tracking, and Forecasting.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01355) · 📚 被引 27
- **作者**: Rohan Choudhury, Kris M. Kitani, László A. Jeni
- **🏷️ 机构**: Carnegie Mellon University,Robotics Institute
- **会议**: ICCV 2023

### Multi-View Active Fine-Grained Visual Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00151) · 📚 被引 13
- **作者**: Ruoyi Du, Wenqing Yu, Heqing Wang, Ting-En Lin, Dongliang Chang, Zhanyu Ma
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,China
- **会议**: ICCV 2023

### Ref-NeuS: Ambiguity-Reduced Neural Implicit Surface Learning for Multi-View Reconstruction with Reflection.
- **链接**: [arXiv:2303.10840](https://arxiv.org/abs/2303.10840) · 📚 被引 54
- **作者**: Wenhang Ge, Tao Hu, Haoyu Zhao, Shu Liu, Ying-Cong Chen
- **🏷️ 机构**: HKUST(GZ), CUHK, SmartMore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural implicit surface learning has shown significant progress in multi-view 3D reconstruction, where an object is represented by multilayer perceptrons that provide continuous implicit surface representation and view-dependent radiance. However, current methods often fail to accurately reconstruct reflective surfaces, leading to severe ambiguity. To overcome this issue, we propose Ref-NeuS, which aims to reduce ambiguity by attenuating the effect of reflective surfaces. Specifically, we utilize an anomaly detector to estimate an explicit reflection score with the guidance of multi-view context to localize reflective surfaces. Afterward, we design a reflection-aware photometric loss that adaptively reduces ambiguity by modeling rendered color as a Gaussian distribution, with the reflection score representing the variance. We show that together with a reflection direction-dependent radiance, our model achieves high-quality surface reconstruction on reflective surfaces and outperforms the state-of-the-arts by a large margin. Besides, our model is also comparable on general surfaces.

</details>

### Anchor Structure Regularization Induced Multi-view Subspace Clustering via Enhanced Tensor Rank Minimization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01772) · 📚 被引 37
- **作者**: Jintian Ji, Songhe Feng
- **🏷️ 机构**: Beijing Jiaotong University,Key Laboratory of Big Data &amp; Artificial Intelligence in Transportation, Ministry of Education,Beijing,China,100044
- **会议**: ICCV 2023

### Coordinate Quantized Neural Implicit Representations for Multi-view Reconstruction.
- **链接**: [arXiv:2308.11025](https://arxiv.org/abs/2308.11025) · 📚 被引 4
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **🏷️ 机构**: Wayne State University,Department of Computer Science,Detroit,USA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, huge progress has been made on learning neural implicit representations from multi-view images for 3D reconstruction. As an additional input complementing coordinates, using sinusoidal functions as positional encodings plays a key role in revealing high frequency details with coordinate-based neural networks. However, high frequency positional encodings make the optimization unstable, which results in noisy reconstructions and artifacts in empty space. To resolve this issue in a general sense, we introduce to learn neural implicit representations with quantized coordinates, which reduces the uncertainty and ambiguity in the field during optimization. Instead of continuous coordinates, we discretize continuous coordinates into discrete coordinates using nearest interpolation among quantized coordinates which are obtained by discretizing the field in an extremely high resolution. We use discrete coordinates and their positional encodings to learn implicit functions through volume rendering. This significantly reduces the variations in the sample space, and triggers more multi-view consistency constraints on intersections of rays from different views, which enables to infer implicit function in a more effective way. Our quantized coordinates do not bring any computational burden, and can seamlessly work upon the latest methods. Our evaluations under the widely used benchmarks show our superiority over the state-of-the-art. Our code is available at https://github.com/MachinePerceptionLab/CQ-NIR.

</details>

### Probabilistic Triangulation for Uncalibrated Multi-View 3D Human Pose Estimation.
- **链接**: [arXiv:2309.04756](https://arxiv.org/abs/2309.04756) · 📚 被引 21
- **作者**: Boyuan Jiang, Lei Hu, Shihong Xia
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Computing Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D human pose estimation has been a long-standing challenge in computer vision and graphics, where multi-view methods have significantly progressed but are limited by the tedious calibration processes. Existing multi-view methods are restricted to fixed camera pose and therefore lack generalization ability. This paper presents a novel Probabilistic Triangulation module that can be embedded in a calibrated 3D human pose estimation method, generalizing it to uncalibration scenes. The key idea is to use a probability distribution to model the camera pose and iteratively update the distribution from 2D features instead of using camera pose. Specifically, We maintain a camera pose distribution and then iteratively update this distribution by computing the posterior probability of the camera pose through Monte Carlo sampling. This way, the gradients can be directly back-propagated from the 3D pose estimation to the 2D heatmap, enabling end-to-end training. Extensive experiments on Human3.6M and CMU Panoptic demonstrate that our method outperforms other uncalibration methods and achieves comparable results with state-of-the-art calibration methods. Thus, our method achieves a trade-off between estimation accuracy and generalizability. Our code is in https://github.com/bymaths/probabilistic_triangulation

</details>

### MHCN: A Hyperbolic Neural Network Model for Multi-view Hierarchical Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01515) · 📚 被引 12
- **作者**: Fangfei Lin, Bing Bai, Yiwen Guo, Hao Chen, Yazhou Ren, Zenglin Xu
- **🏷️ 机构**: University of Electronic Science and Technology of China,China, Tencent Security Big Data Lab,China, Independent Researcher
- **会议**: ICCV 2023

### GeoMIM: Towards Better 3D Knowledge Transfer via Masked Image Modeling for Multi-view 3D Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01635) · 📚 被引 9
- **作者**: Jihao Liu, Tai Wang, Boxiao Liu, Qihang Zhang, Yu Liu, Hongsheng Li
- **🏷️ 机构**: CUHK MMLab, SenseTime Research
- **会议**: ICCV 2023

### When Epipolar Constraint Meets Non-local Operators in Multi-View Stereo.
- **链接**: [arXiv:2309.17218](https://arxiv.org/abs/2309.17218) · 📚 被引 54
- **作者**: Tianqi Liu, Xinyi Ye, Weiyue Zhao, Zhiyu Pan, Min Shi, Zhiguo Cao
- **🏷️ 机构**: Huazhong University of Science and Technology,Key Laboratory of Image Processing and Intelligent Control,Ministry of Education; School of Artificial Intelligence and Automation,Wuhan,China,430074
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning-based multi-view stereo (MVS) method heavily relies on feature matching, which requires distinctive and descriptive representations. An effective solution is to apply non-local feature aggregation, e.g., Transformer. Albeit useful, these techniques introduce heavy computation overheads for MVS. Each pixel densely attends to the whole image. In contrast, we propose to constrain non-local feature augmentation within a pair of lines: each point only attends the corresponding pair of epipolar lines. Our idea takes inspiration from the classic epipolar geometry, which shows that one point with different depth hypotheses will be projected to the epipolar line on the other view. This constraint reduces the 2D search space into the epipolar line in stereo matching. Similarly, this suggests that the matching of MVS is to distinguish a series of points lying on the same line. Inspired by this point-to-line search, we devise a line-to-point non-local augmentation strategy. We first devise an optimized searching algorithm to split the 2D feature maps into epipolar line pairs. Then, an Epipolar Transformer (ET) performs non-local feature augmentation among epipolar line pairs. We incorporate the ET into a learning-based MVS baseline, named ET-MVSNet. ET-MVSNet achieves state-of-the-art reconstruction performance on both the DTU and Tanks-and-Temples benchmark with high efficiency. Code is available at https://github.com/TQTQliu/ET-MVSNet.

</details>

### Multi-view Spectral Polarization Propagation for Video Glass Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02122) · 📚 被引 7
- **作者**: Yu Qiao, Bo Dong, Ao Jin, Yu Fu, Seung-Hwan Baek, Felix Heide et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICCV 2023

### Hierarchical Prior Mining for Non-local Multi-View Stereo.
- **链接**: [arXiv:2303.09758](https://arxiv.org/abs/2303.09758)
- **作者**: Chunlin Ren, Qingshan Xu, Shikun Zhang, Jiaqi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a fundamental problem in computer vision, multi-view stereo (MVS) aims at recovering the 3D geometry of a target from a set of 2D images. Recent advances in MVS have shown that it is important to perceive non-local structured information for recovering geometry in low-textured areas. In this work, we propose a Hierarchical Prior Mining for Non-local Multi-View Stereo (HPM-MVS). The key characteristics are the following techniques that exploit non-local information to assist MVS: 1) A Non-local Extensible Sampling Pattern (NESP), which is able to adaptively change the size of sampled areas without becoming snared in locally optimal solutions. 2) A new approach to leverage non-local reliable points and construct a planar prior model based on K-Nearest Neighbor (KNN), to obtain potential hypotheses for the regions where prior construction is challenging. 3) A Hierarchical Prior Mining (HPM) framework, which is used to mine extensive non-local prior information at different scales to assist 3D model recovery, this strategy can achieve a considerable balance between the reconstruction of details and low-textured areas. Experimental results on the ETH3D and Tanks \& Temples have verified the superior performance and strong generalization capability of our method. Our code will be released.

</details>

### End2End Multi-View Feature Matching with Differentiable Pose Optimization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00050) · 📚 被引 23
- **作者**: Barbara Roessle, Matthias Nießner
- **🏷️ 机构**: Technical University of Munich
- **会议**: ICCV 2023

### Spectral Graphormer: Spectral Graph-based Transformer for Egocentric Two-Hand Reconstruction using Multi-View Color Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01348) · 📚 被引 6
- **作者**: Tze Ho Elden Tse, Franziska Mueller, Zhengyang Shen, Danhang Tang, Thabo Beeler, Mingsong Dou et al.
- **🏷️ 机构**: Google
- **会议**: ICCV 2023

### NeuS2: Fast Learning of Neural Implicit Surfaces for Multi-view Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00305) · 📚 被引 291
- **作者**: Yiming Wang, Qin Han, Marc Habermann, Kostas Daniilidis, Christian Theobalt, Lingjie Liu
- **🏷️ 机构**: University of Pennsylvania, Peking University, Peking University, Max Planck Institute for Informatics
- **会议**: ICCV 2023

### Mixed Neural Voxels for Fast Multi-view Video Synthesis.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01805) · 📚 被引 87
- **作者**: Feng Wang, Sinan Tan, Xinghang Li, Zeyue Tian, Yafei Song, Huaping Liu
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology(BNRist),Department of Computer Science and Technology, Hong Kong University of Science and Technology, Alibaba Group,XR Lab, DAMO Academy
- **会议**: ICCV 2023

### S-VolSDF: Sparse Multi-View Stereo Regularization of Neural Implicit Surfaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00329) · 📚 被引 18
- **作者**: Haoyu Wu, Alexandros Graikos, Dimitris Samaras
- **🏷️ 机构**: Stony Brook University
- **会议**: ICCV 2023

### MV-Map: Offboard HD Map Generation with Multi-view Consistency.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00795) · 📚 被引 25
- **作者**: Ziyang Xie, Ziqi Pang, Yu-Xiong Wang
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: ICCV 2023

### CL-MVSNet: Unsupervised Multi-view Stereo with Dual-level Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00349) · 📚 被引 28
- **作者**: Kaiqiang Xiong, Rui Peng, Zhe Zhang, Tianxing Feng, Jianbo Jiao, Feng Gao et al.
- **🏷️ 机构**: Peking University,School of Electronic and Computer Engineering, University of Birmingham,School of Computer Science, Peking University,School of Arts
- **会议**: ICCV 2023

### Long-Range Grouping Transformer for Multi-View 3D Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01674) · 📚 被引 20
- **作者**: Liying Yang, Zhenwei Zhu, Xuxin Lin, Jian Nong, Yanyan Liang
- **🏷️ 机构**: Macau University of Science and Technology
- **会议**: ICCV 2023

### DeLiRa: Self-Supervised Depth, Light, and Radiance Fields.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01644) · 📚 被引 4
- **作者**: Vitor Guizilini, Igor Vasiljevic, Jiading Fang, Rares Ambrus, Sergey Zakharov, Vincent Sitzmann et al.
- **🏷️ 机构**: Toyota Research Institute (TRI),Los Altos,CA, Toyota Technological Institute of Chicago (TTIC),Chicago,IL, Massachusetts Institute of Technology (MIT),Cambridge,MA
- **会议**: ICCV 2023

### Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative Convolution Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00791) · 📚 被引 32
- **作者**: Wencheng Han, Junbo Yin, Jianbing Shen
- **🏷️ 机构**: University of Macau,SKL-IOTSC, CIS, Beijing Institute of Technology
- **会议**: ICCV 2023

### Self-supervised Monocular Depth Estimation: Let's Talk About The Weather.
- **链接**: [arXiv:2307.08357](https://arxiv.org/abs/2307.08357) · 📚 被引 46
- **作者**: Kieran Saunders, George Vogiatzis, Luis J. Manso
- **🏷️ 机构**: Aston University,Birmingham,UK, Loughborough University,Leicestershire,UK
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current, self-supervised depth estimation architectures rely on clear and sunny weather scenes to train deep neural networks. However, in many locations, this assumption is too strong. For example in the UK (2021), 149 days consisted of rain. For these architectures to be effective in real-world applications, we must create models that can generalise to all weather conditions, times of the day and image qualities. Using a combination of computer graphics and generative models, one can augment existing sunny-weather data in a variety of ways that simulate adverse weather effects. While it is tempting to use such data augmentations for self-supervised depth, in the past this was shown to degrade performance instead of improving it. In this paper, we put forward a method that uses augmentations to remedy this problem. By exploiting the correspondence between unaugmented and augmented data we introduce a pseudo-supervised loss for both depth and pose estimation. This brings back some of the benefits of supervised learning while still not requiring any labels. We also make a series of practical recommendations which collectively offer a reliable, efficient framework for weather-related augmentation of self-supervised depth from monocular video. We present extensive testing to show that our method, Robust-Depth, achieves SotA performance on the KITTI dataset while significantly surpassing SotA on challenging, adverse condition data such as DrivingStereo, Foggy CityScape and NuScenes-Night. The project website can be found here https://kieran514.github.io/Robust-Depth-Project/.

</details>

### 3D Distillation: Improving Self-Supervised Monocular Depth Estimation on Reflective Surfaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00838) · 📚 被引 12
- **作者**: Xuepeng Shi, Georgi Dikov, Gerhard Reitmayr, Tae-Kyun Kim, Mohsen Ghafoorian
- **🏷️ 机构**: Imperial College London, Qualcomm
- **会议**: ICCV 2023

### GasMono: Geometry-Aided Self-Supervised Monocular Depth Estimation for Indoor Scenes.
- **链接**: [arXiv:2309.16019](https://arxiv.org/abs/2309.16019) · 📚 被引 28
- **作者**: Chaoqiang Zhao, Matteo Poggi, Fabio Tosi, Lei Zhou, Qiyu Sun, Yang Tang et al.
- **🏷️ 机构**: East China University of Science and Technology, University of Bologna
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper tackles the challenges of self-supervised monocular depth estimation in indoor scenes caused by large rotation between frames and low texture. We ease the learning process by obtaining coarse camera poses from monocular sequences through multi-view geometry to deal with the former. However, we found that limited by the scale ambiguity across different scenes in the training dataset, a naïve introduction of geometric coarse poses cannot play a positive role in performance improvement, which is counter-intuitive. To address this problem, we propose to refine those poses during training through rotation and translation/scale optimization. To soften the effect of the low texture, we combine the global reasoning of vision transformers with an overfitting-aware, iterative self-distillation mechanism, providing more accurate depth guidance coming from the network itself. Experiments on NYUv2, ScanNet, 7scenes, and KITTI datasets support the effectiveness of each component in our framework, which sets a new state-of-the-art for indoor self-supervised monocular depth estimation, as well as outstanding generalization ability. Code and models are available at https://github.com/zxcqlf/GasMono

</details>

### HaMuCo: Hand Pose Estimation via Multiview Collaborative Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01898) · 📚 被引 24
- **作者**: Xiaozheng Zheng, Chao Wen, Zhou Xue, Pengfei Ren, Jingyu Wang
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,State Key Laboratory of Networking and Switching Technology, ByteDance,PICO IDL,Beijing
- **会议**: ICCV 2023

### Two-in-One Depth: Bridging the Gap Between Monocular and Binocular Self-supervised Depth Estimation.
- **链接**: [arXiv:2309.00933](https://arxiv.org/abs/2309.00933) · 📚 被引 18
- **作者**: Zhengming Zhou, Qiulei Dong
- **🏷️ 机构**: CASIA School of Artificial Intelligence, UCAS,State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular and binocular self-supervised depth estimations are two important and related tasks in computer vision, which aim to predict scene depths from single images and stereo image pairs respectively. In literature, the two tasks are usually tackled separately by two different kinds of models, and binocular models generally fail to predict depth from single images, while the prediction accuracy of monocular models is generally inferior to binocular models. In this paper, we propose a Two-in-One self-supervised depth estimation network, called TiO-Depth, which could not only compatibly handle the two tasks, but also improve the prediction accuracy. TiO-Depth employs a Siamese architecture and each sub-network of it could be used as a monocular depth estimation model. For binocular depth estimation, a Monocular Feature Matching module is proposed for incorporating the stereo knowledge between the two images, and the full TiO-Depth is used to predict depths. We also design a multi-stage joint-training strategy for improving the performances of TiO-Depth in both two tasks by combining the relative advantages of them. Experimental results on the KITTI, Cityscapes, and DDAD datasets demonstrate that TiO-Depth outperforms both the monocular and binocular state-of-the-art methods in most cases, and further verify the feasibility of a two-in-one network for monocular and binocular depth estimation. The code is available at https://github.com/ZM-Zhou/TiO-Depth_pytorch.

</details>

### Time Will Tell: New Outlooks and A Baseline for Temporal Multi-View 3D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=H3HcEJA2Um)
- **作者**: Jinhyung Park, Chenfeng Xu, Shijia Yang, Kurt Keutzer, Kris M. Kitani, Masayoshi Tomizuka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Voint Cloud: Multi-View Point Cloud Representation for 3D Understanding.
- **链接**: [出版页](https://openreview.net/forum?id=IpGgfpMucHj)
- **作者**: Abdullah Hamdi, Silvio Giancola, Bernard Ghanem
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### ViewCo: Discovering Text-Supervised Segmentation Masks via Multi-View Semantic Consistency.
- **链接**: [出版页](https://openreview.net/forum?id=2XLRBjY46O6)
- **作者**: Pengzhen Ren, Changlin Li, Hang Xu, Yi Zhu, Guangrun Wang, Jianzhuang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### LDMIC: Learning-based Distributed Multi-view Image Coding.
- **链接**: [出版页](https://openreview.net/forum?id=ILQVw4cA5F9)
- **作者**: Xinjie Zhang, Jiawei Shao, Jun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Proactive Multi-Camera Collaboration for 3D Human Pose Estimation.
- **链接**: [出版页](https://openreview.net/forum?id=CPIy9TWFYBG)
- **作者**: Hai Ci, Mickel Liu, Xuehai Pan, Fangwei Zhong, Yizhou Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Adversarial Training of Self-supervised Monocular Depth Estimation against Physical-World Attacks.
- **链接**: [出版页](https://openreview.net/forum?id=LfdEuhjR5GV)
- **作者**: Zhiyuan Cheng, James Liang, Guanhong Tao, Dongfang Liu, Xiangyu Zhang
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2023

### Provably Learning Diverse Features in Multi-View Data with Midpoint Mixup.
- **链接**: [出版页](https://proceedings.mlr.press/v202/chidambaram23a.html)
- **作者**: Muthu Chidambaram, Xiang Wang, Chenwei Wu, Rong Ge
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### The Role of Entropy and Reconstruction in Multi-View Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/rodri-guez-galvez23a.html)
- **作者**: Borja Rodríguez Gálvez, Arno Blaas, Pau Rodríguez, Adam Golinski, Xavier Suau, Jason Ramapuram et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Information-Theoretic State Space Model for Multi-View Reinforcement Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/hwang23c.html)
- **作者**: HyeongJoo Hwang, Seokin Seo, Youngsoo Jang, Sungyoon Kim, Geon-Hyeong Kim, Seunghoon Hong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

## 跨领域论文（完整笔记在其他领域）

- HM-ViT: Hetero-modal Vehicle-to-Vehicle Cooperative Perception with Vision Transformer. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- 3D Video Object Detection with Learnable Object-Centric Global Optimization. → [object-detection](../object-detection/Guideline%202023.md)
- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [object-detection](../object-detection/Guideline%202023.md)
- AeDet: Azimuth-Invariant Multi-View 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Towards Domain Generalization for Multi-view 3D Object Detection in Bird-Eye-View. → [object-detection](../object-detection/Guideline%202023.md)
- BEVHeight: A Robust Framework for Vision-based Roadside 3D Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- On the Effects of Self-supervision and Contrastive Alignment in Deep Multi-view Clustering. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- MSeg3D: Multi-Modal 3D Semantic Segmentation for Autonomous Driving. → [multimodal](../multimodal/Guideline%202023.md)
- ContraNeRF: Generalizable Neural Radiance Fields for Synthetic-to-real Novel View Synthesis via Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Local 3D Editing via 3D Distillation of CLIP Knowledge. → [vlm](../vlm/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [multimodal](../multimodal/Guideline%202023.md)
- SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. → [bev](../bev/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [network-pruning](../network-pruning/Guideline%202023.md)
- CLIP2Point: Transfer CLIP to Point Cloud Classification with Image-Depth Pre-Training. → [vlm](../vlm/Guideline%202023.md)
- MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception. → [network-pruning](../network-pruning/Guideline%202023.md)
- SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving. → [occupancy](../occupancy/Guideline%202023.md)
- Multi-view Self-supervised Disentanglement for General Image Denoising. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- CLIP-FO3D: Learning Free Open-world 3D Scene Representations from 2D Dense CLIP. → [vlm](../vlm/Guideline%202023.md)
- BEVDistill: Cross-Modal BEV Distillation for Multi-View 3D Object Detection. → [multimodal](../multimodal/Guideline%202023.md)

<!-- COMPLETE v1 papers=107 -->
