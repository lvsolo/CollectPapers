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

> In this paper, we present a new tracking architecture with an encoder-decoder transformer as the key component. The encoder models the global spatio-temporal feature dependencies between target objects and search regions, while the decoder learns a query embedding to predict the spatial positions of the target objects. Our method casts object tracking as a direct bounding box prediction problem, without using any proposals or predefined anchors. With the encoder-decoder transformer, the prediction of objects just uses a simple fully-convolutional network, which estimates the corners of objects directly. The whole method is end-to-end, does not need any postprocessing steps such as cosine window and bounding box smoothing, thus largely simplifying existing tracking pipelines. The proposed tracker achieves state-of-the-art performance on five challenging short-term and long-term benchmarks, while running at real-time speed, being 6x faster than Siam R-CNN. Code and models are open-sourced at https://github.com/researchmm/Stark.

</details>

### Video Annotation for Visual Tracking via Selection and Refinement.
- **链接**: [arXiv:2108.03821](https://arxiv.org/abs/2108.03821) · 📚 被引 9
- **作者**: Kenan Dai, Jie Zhao, Lijun Wang, Dong Wang, Jianhua Li, Huchuan Lu et al.
- **🏷️ 机构**: Dalian University of Technology,China, CSA Intellicloud Ltd, Remark Holdings
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning based visual trackers entail offline pre-training on large volumes of video datasets with accurate bounding box annotations that are labor-expensive to achieve. We present a new framework to facilitate bounding box annotations for video sequences, which investigates a selection-and-refinement strategy to automatically improve the preliminary annotations generated by tracking algorithms. A temporal assessment network (T-Assess Net) is proposed which is able to capture the temporal coherence of target locations and select reliable tracking results by measuring their quality. Meanwhile, a visual-geometry refinement network (VG-Refine Net) is also designed to further enhance the selected tracking results by considering both target appearance and temporal geometry constraints, allowing inaccurate tracking results to be corrected. The combination of the above two networks provides a principled approach to ensure the quality of automatic video annotation. Experiments on large scale tracking benchmarks demonstrate that our method can deliver highly accurate bounding box annotations and significantly reduce human labor by 94.0%, yielding an effective means to further boost tracking performance with augmented training data.

</details>

### Track without Appearance: Learn Box and Tracklet Embedding with Local and Global Motion Patterns for Vehicle Tracking.
- **链接**: [arXiv:2108.06029](https://arxiv.org/abs/2108.06029) · [代码](https://github.com/GaoangW/LGMTracker) · 📚 被引 73
- **作者**: Gaoang Wang, Renshu Gu, Zuozhu Liu, Weijie Hu, Mingli Song, Jenq-Neng Hwang
- **🏷️ 机构**: Zhejiang University, Hangzhou Dianzi University, Guangdong University of Petrochemical Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vehicle tracking is an essential task in the multi-object tracking (MOT) field. A distinct characteristic in vehicle tracking is that the trajectories of vehicles are fairly smooth in both the world coordinate and the image coordinate. Hence, models that capture motion consistencies are of high necessity. However, tracking with the standalone motion-based trackers is quite challenging because targets could get lost easily due to limited information, detection error and occlusion. Leveraging appearance information to assist object re-identification could resolve this challenge to some extent. However, doing so requires extra computation while appearance information is sensitive to occlusion as well. In this paper, we try to explore the significance of motion patterns for vehicle tracking without appearance information. We propose a novel approach that tackles the association issue for long-term tracking with the exclusive fully-exploited motion information. We address the tracklet embedding issue with the proposed reconstruct-to-embed strategy based on deep graph convolutional neural networks (GCN). Comprehensive experiments on the KITTI-car tracking dataset and UA-Detrac dataset show that the proposed method, though without appearance information, could achieve competitive performance with the state-of-the-art (SOTA) trackers. The source code will be available at https://github.com/GaoangW/LGMTracker.

</details>

### MLVSNet: Multi-level Voting Siamese Network for 3D Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00309) · 📚 被引 58
- **作者**: Zhoutao Wang, Qian Xie, Yu-Kun Lai, Jing Wu, Kun Long, Jun Wang
- **🏷️ 机构**: Nanjing University of Aeronautics and Astronautics, Cardiff University
- **会议**: ICCV 2021

### Learn to Match: Automatic Matching Network Design for Visual Tracking.
- **链接**: [arXiv:2108.00803](https://arxiv.org/abs/2108.00803) · [代码](https://github.com/JudasDie/SOTS) · 📚 被引 241
- **作者**: Zhipeng Zhang, Yihao Liu, Xiao Wang, Bing Li, Weiming Hu
- **🏷️ 机构**: Chinese Academy of Sciences,National Laboratory of Pattern Recognition, Institute of Automation, University of Chinese Academy of Sciences,School of AI, Peng Cheng Laboratory
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Siamese tracking has achieved groundbreaking performance in recent years, where the essence is the efficient matching operator cross-correlation and its variants. Besides the remarkable success, it is important to note that the heuristic matching network design relies heavily on expert experience. Moreover, we experimentally find that one sole matching operator is difficult to guarantee stable tracking in all challenging environments. Thus, in this work, we introduce six novel matching operators from the perspective of feature fusion instead of explicit similarity learning, namely Concatenation, Pointwise-Addition, Pairwise-Relation, FiLM, Simple-Transformer and Transductive-Guidance, to explore more feasibility on matching operator selection. The analyses reveal these operators' selective adaptability on different environment degradation types, which inspires us to combine them to explore complementary features. To this end, we propose binary channel manipulation (BCM) to search for the optimal combination of these operators. BCM determines to retrain or discard one operator by learning its contribution to other tracking steps. By inserting the learned matching networks to a strong baseline tracker Ocean, our model achieves favorable gains by $67.2 \rightarrow 71.4$, $52.6 \rightarrow 58.3$, $70.3 \rightarrow 76.0$ success on OTB100, LaSOT, and TrackingNet, respectively. Notably, Our tracker, dubbed AutoMatch, uses less than half of training data/time than the baseline tracker, and runs at 50 FPS using PyTorch. Code and model will be released at https://github.com/JudasDie/SOTS.

</details>

## 跨领域论文（完整笔记在其他领域）

- Exploring Simple 3D Multi-Object Tracking for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
