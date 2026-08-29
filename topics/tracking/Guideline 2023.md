# Tracking — 2023 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### PVT++: A Simple End-to-End Latency-Aware Visual Tracking Framework.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00918) · 📚 被引 22
- **作者**: Bowen Li, Ziyuan Huang, Junjie Ye, Yiming Li, Sebastian A. Scherer, Hang Zhao et al.
- **🏷️ 机构**: Carnegie Mellon University, National University of Singapore, Tongji University
- **会议**: ICCV 2023

### MBPTrack: Improving 3D Point Cloud Tracking with Memory networks and Box Priors.
- **链接**: [arXiv:2303.05071](https://arxiv.org/abs/2303.05071) · 📚 被引 25
- **作者**: Tian-Xing Xu, Yuan-Chen Guo, Yu-Kun Lai, Song-Hai Zhang
- **🏷️ 机构**: Tsinghua University,China, Cardiff University,United Kingdom
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D single object tracking has been a crucial problem for decades with numerous applications such as autonomous driving. Despite its wide-ranging use, this task remains challenging due to the significant appearance variation caused by occlusion and size differences among tracked targets. To address these issues, we present MBPTrack, which adopts a Memory mechanism to utilize past information and formulates localization in a coarse-to-fine scheme using Box Priors given in the first frame. Specifically, past frames with targetness masks serve as an external memory, and a transformer-based module propagates tracked target cues from the memory to the current frame. To precisely localize objects of all sizes, MBPTrack first predicts the target center via Hough voting. By leveraging box priors given in the first frame, we adaptively sample reference points around the target center that roughly cover the target of different sizes. Then, we obtain dense feature maps by aggregating point features into the reference points, where localization can be performed more effectively. Extensive experiments demonstrate that MBPTrack achieves state-of-the-art performance on KITTI, nuScenes and Waymo Open Dataset, while running at 50 FPS on a single RTX3090 GPU.

</details>

### SportsMOT: A Large Multi-Object Tracking Dataset in Multiple Sports Scenes.
- **链接**: [arXiv:2304.05170](https://arxiv.org/abs/2304.05170) · 📚 被引 180
- **作者**: Yutao Cui, Chenkai Zeng, Xiaoyu Zhao, Yichun Yang, Gangshan Wu, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking in sports scenes plays a critical role in gathering players statistics, supporting further analysis, such as automatic tactical analysis. Yet existing MOT benchmarks cast little attention on the domain, limiting its development. In this work, we present a new large-scale multi-object tracking dataset in diverse sports scenes, coined as \emph{SportsMOT}, where all players on the court are supposed to be tracked. It consists of 240 video sequences, over 150K frames (almost 15\times MOT17) and over 1.6M bounding boxes (3\times MOT17) collected from 3 sports categories, including basketball, volleyball and football. Our dataset is characterized with two key properties: 1) fast and variable-speed motion and 2) similar yet distinguishable appearance. We expect SportsMOT to encourage the MOT trackers to promote in both motion-based association and appearance-based association. We benchmark several state-of-the-art trackers and reveal the key challenge of SportsMOT lies in object association. To alleviate the issue, we further propose a new multi-object tracking framework, termed as \emph{MixSort}, introducing a MixFormer-like structure as an auxiliary association model to prevailing tracking-by-detection trackers. By integrating the customized appearance-based association with the original motion-based association, MixSort achieves state-of-the-art performance on SportsMOT and MOT17. Based on MixSort, we give an in-depth analysis and provide some profound insights into SportsMOT. The dataset and code will be available at https://deeperaction.github.io/datasets/sportsmot.html.

</details>

### Collaborative Tracking Learning for Frame-Rate-Insensitive Multi-Object Tracking.
- **链接**: [arXiv:2308.05911](https://arxiv.org/abs/2308.05911) · [代码](https://github.com/yolomax/ColTrack) · 📚 被引 23
- **作者**: Yiheng Liu, Junta Wu, Yi Fu
- **🏷️ 机构**: ByteDance Inc.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-object tracking (MOT) at low frame rates can reduce computational, storage and power overhead to better meet the constraints of edge devices. Many existing MOT methods suffer from significant performance degradation in low-frame-rate videos due to significant location and appearance changes between adjacent frames. To this end, we propose to explore collaborative tracking learning (ColTrack) for frame-rate-insensitive MOT in a query-based end-to-end manner. Multiple historical queries of the same target jointly track it with richer temporal descriptions. Meanwhile, we insert an information refinement module between every two temporal blocking decoders to better fuse temporal clues and refine features. Moreover, a tracking object consistency loss is proposed to guide the interaction between historical queries. Extensive experimental results demonstrate that in high-frame-rate videos, ColTrack obtains higher performance than state-of-the-art methods on large-scale datasets Dancetrack and BDD100K, and outperforms the existing end-to-end methods on MOT17. More importantly, ColTrack has a significant advantage over state-of-the-art methods in low-frame-rate videos, which allows it to obtain faster processing speeds by reducing frame-rate requirements while maintaining higher performance. Code will be released at https://github.com/yolomax/ColTrack

</details>

### Tracking without Label: Unsupervised Multiple Object Tracking via Contrastive Similarity Learning.
- **链接**: [arXiv:2309.00942](https://arxiv.org/abs/2309.00942) · 📚 被引 14
- **作者**: Sha Meng, Dian Shao, Jiacheng Guo, Shan Gao
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x2019;an,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised learning is a challenging task due to the lack of labels. Multiple Object Tracking (MOT), which inevitably suffers from mutual object interference, occlusion, etc., is even more difficult without label supervision. In this paper, we explore the latent consistency of sample features across video frames and propose an Unsupervised Contrastive Similarity Learning method, named UCSL, including three contrast modules: self-contrast, cross-contrast, and ambiguity contrast. Specifically, i) self-contrast uses intra-frame direct and inter-frame indirect contrast to obtain discriminative representations by maximizing self-similarity. ii) Cross-contrast aligns cross- and continuous-frame matching results, mitigating the persistent negative effect caused by object occlusion. And iii) ambiguity contrast matches ambiguous objects with each other to further increase the certainty of subsequent object association through an implicit manner. On existing benchmarks, our method outperforms the existing unsupervised methods using only limited help from ReID head, and even provides higher accuracy than lots of fully supervised methods.

</details>

### Object-Centric Multiple Object Tracking.
- **链接**: [arXiv:2309.00233](https://arxiv.org/abs/2309.00233)
- **作者**: Zixu Zhao, Jiaze Wang, Max Horn, Yizhuo Ding, Tong He, Zechen Bai et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised object-centric learning methods allow the partitioning of scenes into entities without additional localization information and are excellent candidates for reducing the annotation burden of multiple-object tracking (MOT) pipelines. Unfortunately, they lack two key properties: objects are often split into parts and are not consistently tracked over time. In fact, state-of-the-art models achieve pixel-level accuracy and temporal consistency by relying on supervised object detection with additional ID labels for the association through time. This paper proposes a video object-centric model for MOT. It consists of an index-merge module that adapts the object-centric slots into detection outputs and an object memory module that builds complete object prototypes to handle occlusions. Benefited from object-centric learning, we only require sparse detection labels (0%-6.25%) for object localization and feature binding. Relying on our self-supervised Expectation-Maximization-inspired loss for object association, our approach requires no ID labels. Our experiments significantly narrow the gap between the existing object-centric model and the fully supervised state-of-the-art and outperform several unsupervised trackers.

</details>

### 3DMOTFormer: Graph Transformer for Online 3D Multi-Object Tracking.
- **链接**: [arXiv:2308.06635](https://arxiv.org/abs/2308.06635) · [代码](https://github.com/dsx0511/3DMOTFormer) · 📚 被引 56
- **作者**: Shuxiao Ding, Eike Rehder, Lukas Schneider, Marius Cordts, Juergen Gall
- **🏷️ 机构**: Mercedes-Benz AG,Sindelfingen,Germany, Robert Bosch GmbH,Stuttgart,Germany, University of Bonn,Bonn,Germany
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tracking 3D objects accurately and consistently is crucial for autonomous vehicles, enabling more reliable downstream tasks such as trajectory prediction and motion planning. Based on the substantial progress in object detection in recent years, the tracking-by-detection paradigm has become a popular choice due to its simplicity and efficiency. State-of-the-art 3D multi-object tracking (MOT) approaches typically rely on non-learned model-based algorithms such as Kalman Filter but require many manually tuned parameters. On the other hand, learning-based approaches face the problem of adapting the training to the online setting, leading to inevitable distribution mismatch between training and inference as well as suboptimal performance. In this work, we propose 3DMOTFormer, a learned geometry-based 3D MOT framework building upon the transformer architecture. We use an Edge-Augmented Graph Transformer to reason on the track-detection bipartite graph frame-by-frame and conduct data association via edge classification. To reduce the distribution mismatch between training and inference, we propose a novel online training strategy with an autoregressive and recurrent forward pass as well as sequential batch optimization. Using CenterPoint detections, our approach achieves 71.2% and 68.2% AMOTA on the nuScenes validation and test split, respectively. In addition, a trained 3DMOTFormer model generalizes well across different object detectors. Code is available at: https://github.com/dsx0511/3DMOTFormer.

</details>

### MeMOTR: Long-Term Memory-Augmented Transformer for Multi-Object Tracking.
- **链接**: [arXiv:2307.15700](https://arxiv.org/abs/2307.15700) · [代码](https://github.com/MCG-NJU/MeMOTR) · 📚 被引 150
- **作者**: Ruopeng Gao, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a video task, Multiple Object Tracking (MOT) is expected to capture temporal information of targets effectively. Unfortunately, most existing methods only explicitly exploit the object features between adjacent frames, while lacking the capacity to model long-term temporal information. In this paper, we propose MeMOTR, a long-term memory-augmented Transformer for multi-object tracking. Our method is able to make the same object's track embedding more stable and distinguishable by leveraging long-term memory injection with a customized memory-attention layer. This significantly improves the target association ability of our model. Experimental results on DanceTrack show that MeMOTR impressively surpasses the state-of-the-art method by 7.9% and 13.0% on HOTA and AssA metrics, respectively. Furthermore, our model also outperforms other Transformer-based methods on association performance on MOT17 and generalizes well on BDD100K. Code is available at https://github.com/MCG-NJU/MeMOTR.

</details>

### Heterogeneous Diversity Driven Active Learning for Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00911) · 📚 被引 11
- **作者**: Rui Li, Baopeng Zhang, Jun Liu, Wei Liu, Jian Zhao, Zhu Teng
- **🏷️ 机构**: Beijing Jiaotong University, Singapore University of Technology and Design, Institute of North Electronic Equipment
- **会议**: ICCV 2023

### Uncertainty-aware Unsupervised Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00917) · 📚 被引 24
- **作者**: Kai Liu, Sheng Jin, Zhihang Fu, Ze Chen, Rongxin Jiang, Jieping Ye
- **🏷️ 机构**: Zhejiang University, Alibaba DAMO Academy
- **会议**: ICCV 2023

### TrackFlow: Multi-Object Tracking with Normalizing Flows.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00874) · 📚 被引 20
- **作者**: Gianluca Mancusi, Aniello Panariello, Angelo Porrello, Matteo Fabbri, Simone Calderara, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy, GoatAI S.r.l.
- **会议**: ICCV 2023

### DARTH: Holistic Test-time Adaptation for Multiple Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00891) · 📚 被引 17
- **作者**: Mattia Segù, Bernt Schiele, Fisher Yu
- **🏷️ 机构**: ETH Zurich, Saarland Informatics Campus,Max Planck Institute for Informatics
- **会议**: ICCV 2023

### Integrating Boxes and Masks: A Multi-Object Framework for Unified Visual Tracking and Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00893) · 📚 被引 23
- **作者**: Yuanyou Xu, Zongxin Yang, Yi Yang
- **🏷️ 机构**: Zhejiang University,ReLER, CCAI,China
- **会议**: ICCV 2023

### Robust Object Modeling for Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00879)
- **作者**: Yidong Cai, Jie Liu, Jie Tang, Gangshan Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Exploring Lightweight Hierarchical Vision Transformers for Efficient Visual Tracking.
- **链接**: [arXiv:2308.06904](https://arxiv.org/abs/2308.06904) · 📚 被引 127
- **作者**: Ben Kang, Xin Chen, Dong Wang, Houwen Peng, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,School of Information and Communication Engineering, Microsoft Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based visual trackers have demonstrated significant progress owing to their superior modeling capabilities. However, existing trackers are hampered by low speed, limiting their applicability on devices with limited computational power. To alleviate this problem, we propose HiT, a new family of efficient tracking models that can run at high speed on different devices while retaining high performance. The central idea of HiT is the Bridge Module, which bridges the gap between modern lightweight transformers and the tracking framework. The Bridge Module incorporates the high-level information of deep features into the shallow large-resolution features. In this way, it produces better features for the tracking head. We also propose a novel dual-image position encoding technique that simultaneously encodes the position information of both the search region and template images. The HiT model achieves promising speed with competitive performance. For instance, it runs at 61 frames per second (fps) on the Nvidia Jetson AGX edge device. Furthermore, HiT attains 64.6% AUC on the LaSOT benchmark, surpassing all previous efficient trackers.

</details>

### CiteTracker: Correlating Image and Text for Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00915) · 📚 被引 80
- **作者**: Xin Li, Yuqing Huang, Zhenyu He, Yaowei Wang, Huchuan Lu, Ming-Hsuan Yang
- **🏷️ 机构**: Peng Cheng Laboratory, Harbin Institute of Technology,Shenzhen, Dalian University of Technology
- **会议**: ICCV 2023

### End-to-end 3D Tracking with Decoupled Queries.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01678) · 📚 被引 19
- **作者**: Yanwei Li, Zhiding Yu, Jonah Philion, Anima Anandkumar, Sanja Fidler, Jiaya Jia et al.
- **🏷️ 机构**: CUHK, NVIDIA
- **会议**: ICCV 2023

### MixCycle: Mixup Assisted Semi-Supervised 3D Single Object Tracking with Cycle Consistency.
- **链接**: [arXiv:2303.09219](https://arxiv.org/abs/2303.09219) · 📚 被引 9
- **作者**: Qiao Wu, Jiaqi Yang, Kun Sun, Chu'ai Zhang, Yanning Zhang, Mathieu Salzmann
- **🏷️ 机构**: Northwestern Polytechnical University, China University of Geosciences,Wuhan, &#x00C9;cole Polytechnique F&#x00E9;d&#x00E9;rale de Lausanne
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D single object tracking (SOT) is an indispensable part of automated driving. Existing approaches rely heavily on large, densely labeled datasets. However, annotating point clouds is both costly and time-consuming. Inspired by the great success of cycle tracking in unsupervised 2D SOT, we introduce the first semi-supervised approach to 3D SOT. Specifically, we introduce two cycle-consistency strategies for supervision: 1) Self tracking cycles, which leverage labels to help the model converge better in the early stages of training; 2) forward-backward cycles, which strengthen the tracker's robustness to motion variations and the template noise caused by the template update strategy. Furthermore, we propose a data augmentation strategy named SOTMixup to improve the tracker's robustness to point cloud diversity. SOTMixup generates training samples by sampling points in two point clouds with a mixing rate and assigns a reasonable loss weight for training according to the mixing rate. The resulting MixCycle approach generalizes to appearance matching-based trackers. On the KITTI benchmark, based on the P2B tracker, MixCycle trained with $\textbf{10\%}$ labels outperforms P2B trained with $\textbf{100\%}$ labels, and achieves a $\textbf{28.4\%}$ precision improvement when using $\textbf{1\%}$ labels. Our code will be released at \url{https://github.com/Mumuqiao/MixCycle}.

</details>

### Human from Blur: Human Pose Tracking from Blurry Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01369) · 📚 被引 6
- **作者**: Yiming Zhao, Denys Rozumnyi, Jie Song, Otmar Hilliges, Marc Pollefeys, Martin R. Oswald
- **🏷️ 机构**: ETH,Z&#x00FC;rich
- **会议**: ICCV 2023

### A Gated Attention Transformer for Multi-Person Pose Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00343) · 📚 被引 7
- **作者**: Andreas Doering, Juergen Gall
- **🏷️ 机构**: University of Bonn
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- ReST: A Reconfigurable Spatial-Temporal Graph Model for Multi-Camera Multi-Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
