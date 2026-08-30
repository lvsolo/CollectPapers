# Multimodal — 2022 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 37 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Self-supervised object detection from audio-visual correspondence.
- **链接**: [arXiv:2104.06401](https://arxiv.org/abs/2104.06401) · 📚 被引 40
- **作者**: Triantafyllos Afouras, Yuki M. Asano, Francois Fagan, Andrea Vedaldi, Florian Metze
- **🏷️ 机构**: University of Oxford, University of Amsterdam, Meta AI
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the problem of learning object detectors without supervision. Differently from weakly-supervised object detection, we do not assume image-level class labels. Instead, we extract a supervisory signal from audio-visual data, using the audio component to "teach" the object detector. While this problem is related to sound source localisation, it is considerably harder because the detector must classify the objects by type, enumerate each instance of the object, and do so even when the object is silent. We tackle this problem by first designing a self-supervised framework with a contrastive objective that jointly learns to classify and localise objects. Then, without using any supervision, we simply use these self-supervised labels and boxes to train an image-based object detector. With this, we outperform previous unsupervised and weakly-supervised detectors for the task of object detection and sound source localization. We also show that we can align this detector to ground-truth classes with as little as one label per pseudo-class, and show how our method can learn to detect generic objects that go beyond instruments, such as airplanes and cats.

</details>

### CrossPoint: Self-Supervised Cross-Modal Contrastive Learning for 3D Point Cloud Understanding.
- **链接**: [arXiv:2203.00680](https://arxiv.org/abs/2203.00680) · [代码](https://github.com/MohamedAfham/CrossPoint) · 📚 被引 274
- **作者**: Mohamed Afham, Isuru Dissanayake, Dinithi Dissanayake, Amaya Dharmasiri, Kanchana Thilakarathna, Ranga Rodrigo
- **🏷️ 机构**: Univeristy of Moratuwa,Dept. of Electronic and Telecommunication Engineering,Sri Lanka, The University of Sydney
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Manual annotation of large-scale point cloud dataset for varying tasks such as 3D object classification, segmentation and detection is often laborious owing to the irregular structure of point clouds. Self-supervised learning, which operates without any human labeling, is a promising approach to address this issue. We observe in the real world that humans are capable of mapping the visual concepts learnt from 2D images to understand the 3D world. Encouraged by this insight, we propose CrossPoint, a simple cross-modal contrastive learning approach to learn transferable 3D point cloud representations. It enables a 3D-2D correspondence of objects by maximizing agreement between point clouds and the corresponding rendered 2D image in the invariant space, while encouraging invariance to transformations in the point cloud modality. Our joint training objective combines the feature correspondences within and across modalities, thus ensembles a rich learning signal from both 3D point cloud and 2D image modalities in a self-supervised fashion. Experimental results show that our approach outperforms the previous unsupervised learning methods on a diverse range of downstream tasks including 3D object classification and segmentation. Further, the ablation studies validate the potency of our approach for a better point cloud understanding. Code and pretrained models are available at http://github.com/MohamedAfham/CrossPoint.

</details>

### Text2Pos: Text-to-Point-Cloud Cross-Modal Localization. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.15125](https://arxiv.org/abs/2203.15125) · 📚 被引 26
- **作者**: Manuel Kolmet, Qunjie Zhou, Aljosa Osep, Laura Leal-Taixé
- **🏷️ 机构**: Technical University of Munich,Germany
- **会议**: CVPR 2022
- **摘要（中）**: ①针对自然语言描述与3D点云环境之间的跨模态定位问题，旨在通过文本指定车辆接驳或货物配送位置。②提出了Text2Pos，一个跨模态定位模块，采用从粗到细的方式对齐文本描述与点云中的定位线索。③构建了KITTI360Pose数据集，这是该任务的首个基准。④实验显示，在top-10检索中，65%的文本查询能在15米内定位到目标位置。
- **摘要（英）**: This paper addresses text-to-point-cloud localization by proposing Text2Pos, a cross-modal module that aligns textual descriptions with point cloud cues in a coarse-to-fine manner. It introduces the KITTI360Pose dataset and achieves 65% localization accuracy within 15m for top-10 retrievals.
- **核心贡献**: 首次提出文本到点云定位任务并构建基准数据集。
- **创新点**: 采用粗到细的跨模态对齐策略。
- **结果**: 在KITTI360Pose上实现65%的top-10定位精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Natural language-based communication with mobile devices and home appliances is becoming increasingly popular and has the potential to become natural for communicating with mobile robots in the future. Towards this goal, we investigate cross-modal text-to-point-cloud localization that will allow us to specify, for example, a vehicle pick-up or goods delivery location. In particular, we propose Text2Pos, a cross-modal localization module that learns to align textual descriptions with localization cues in a coarse- to-fine manner. Given a point cloud of the environment, Text2Pos locates a position that is specified via a natural language-based description of the immediate surroundings. To train Text2Pos and study its performance, we construct KITTI360Pose, the first dataset for this task based on the recently introduced KITTI360 dataset. Our experiments show that we can localize 65% of textual queries within 15m distance to query locations for top-10 retrieved locations. This is a starting point that we hope will spark future developments towards language-based navigation.

</details>

### Multimodal Colored Point Cloud to Image Alignment. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00654) · 📚 被引 4
- **作者**: Noam Rotstein, Amit Bracha, Ron Kimmel
- **🏷️ 机构**: Technion - Israel Institute of Technology
- **会议**: CVPR 2022
- **摘要（中）**: ①针对彩色点云与图像对齐问题，可能涉及多模态数据配准。②摘要缺失，无法详细评估方法。③缺乏具体信息，难以判断创新点。④效果未知。
- **摘要（英）**: This paper addresses multimodal colored point cloud to image alignment, but the abstract is missing, limiting detailed assessment. No specific methods or results are available.
- **核心贡献**: 未知，摘要缺失。
- **创新点**: 未知。
- **结果**: 未知。

### Open-Vocabulary Instance Segmentation via Robust Cross-Modal Pseudo-Labeling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00689)
- **作者**: Dat Huynh, Jason Kuen, Zhe Lin, Jiuxiang Gu, Ehsan Elhamifar
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Cross-modal Map Learning for Vision and Language Navigation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01502) · 📚 被引 73
- **作者**: Georgios Georgakis, Karl Schmeckpeper, Karan Wanchoo, Soham Dan, Eleni Miltsakaki, Dan Roth et al.
- **🏷️ 机构**: University of Pennsylvania
- **会议**: CVPR 2022

### COTS: Collaborative Two-Stream Vision-Language Pre-Training Model for Cross-Modal Retrieval.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01524) · 📚 被引 68
- **作者**: Haoyu Lu, Nanyi Fei, Yuqi Huo, Yizhao Gao, Zhiwu Lu, Ji-Rong Wen
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China
- **会议**: CVPR 2022

### Multimodal Dynamics: Dynamical Fusion for Trustworthy Multimodal Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02005) · 📚 被引 172
- **作者**: Zongbo Han, Fan Yang, Junzhou Huang, Changqing Zhang, Jianhua Yao
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University, Tencent AI Lab
- **会议**: CVPR 2022

### Expanding Large Pre-trained Unimodal Models with Multimodal Information Injection for Image-Text Multimodal Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01505)
- **作者**: Tao Liang, Guosheng Lin, Mingyang Wan, Tianrui Li, Guojun Ma, Fengmao Lv
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Multimodal Token Fusion for Vision Transformers.
- **链接**: [arXiv:2204.08721](https://arxiv.org/abs/2204.08721) · [代码](https://github.com/yikaiw/TokenFusion) · 📚 被引 237
- **作者**: Yikai Wang, Xinghao Chen, Lele Cao, Wenbing Huang, Fuchun Sun, Yunhe Wang
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology (BNRist), State Key Lab on Intelligent Technology and Systems,Department of Computer Science and Technology, Huawei Noah&#x0027;s Ark Lab, Institute for AI Industry Research (AIR), Tsinghua University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many adaptations of transformers have emerged to address the single-modal vision tasks, where self-attention modules are stacked to handle input sources like images. Intuitively, feeding multiple modalities of data to vision transformers could improve the performance, yet the inner-modal attentive weights may also be diluted, which could thus undermine the final performance. In this paper, we propose a multimodal token fusion method (TokenFusion), tailored for transformer-based vision tasks. To effectively fuse multiple modalities, TokenFusion dynamically detects uninformative tokens and substitutes these tokens with projected and aggregated inter-modal features. Residual positional alignment is also adopted to enable explicit utilization of the inter-modal alignments after fusion. The design of TokenFusion allows the transformer to learn correlations among multimodal features, while the single-modal transformer architecture remains largely intact. Extensive experiments are conducted on a variety of homogeneous and heterogeneous modalities and demonstrate that TokenFusion surpasses state-of-the-art methods in three typical vision tasks: multimodal image-to-image translation, RGB-depth semantic segmentation, and 3D object detection with point cloud and images. Our code is available at https://github.com/yikaiw/TokenFusion.

</details>

### Are Multimodal Transformers Robust to Missing Modality?
- **链接**: [arXiv:2204.05454](https://arxiv.org/abs/2204.05454) · 📚 被引 163
- **作者**: Mengmeng Ma, Jian Ren, Long Zhao, Davide Testuggine, Xi Peng
- **🏷️ 机构**: University of Delaware, Snap Inc., Google Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal data collected from the real world are often imperfect due to missing modalities. Therefore multimodal models that are robust against modal-incomplete data are highly preferred. Recently, Transformer models have shown great success in processing multimodal data. However, existing work has been limited to either architecture designs or pre-training strategies; whether Transformer models are naturally robust against missing-modal data has rarely been investigated. In this paper, we present the first-of-its-kind work to comprehensively investigate the behavior of Transformers in the presence of modal-incomplete data. Unsurprising, we find Transformer models are sensitive to missing modalities while different modal fusion strategies will significantly affect the robustness. What surprised us is that the optimal fusion strategy is dataset dependent even for the same Transformer model; there does not exist a universal strategy that works in general cases. Based on these findings, we propose a principle method to improve the robustness of Transformer models by automatically searching for an optimal fusion strategy regarding input data. Experimental validations on three benchmarks support the superior performance of the proposed method.

</details>

### Learnable Irrelevant Modality Dropout for Multimodal Action Recognition on Modality-Specific Annotated Videos. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01957) · 📚 被引 30
- **作者**: Saghir Alfasly, Jian Lu, Chen Xu, Yuru Zou
- **🏷️ 机构**: Shenzhen University,Shenzhen Key Laboratory of Advanced Machine Learning and Applications,China
- **会议**: CVPR 2022
- **摘要（中）**: ①针对多模态动作识别中，模态特定标注视频导致模态缺失或噪声的问题。②提出了可学习的无关模态丢弃方法，在训练中动态丢弃不相关模态，增强模型鲁棒性。③相比固定丢弃策略，可学习机制适应不同样本。④在动作识别任务上提升了性能，但具体数据未提供。
- **摘要（英）**: This paper addresses multimodal action recognition with modality-specific annotated videos by proposing a learnable irrelevant modality dropout method. It dynamically drops irrelevant modalities during training, improving robustness and performance, though specific results are not detailed.
- **核心贡献**: 提出可学习的模态丢弃策略，处理模态缺失问题。
- **创新点**: 动态学习丢弃不相关模态，提升泛化性。
- **结果**: 在动作识别任务上性能提升，但未提供具体数值。

### End-to-End Referring Video Object Segmentation with Multimodal Transformers.
- **链接**: [arXiv:2111.14821](https://arxiv.org/abs/2111.14821) · [代码](https://github.com/mttr2021/MTTR) · 📚 被引 163
- **作者**: Adam Botach, Evgenii Zheltonozhskii, Chaim Baskin
- **🏷️ 机构**: Technion -Israel Institute of Technology
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The referring video object segmentation task (RVOS) involves segmentation of a text-referred object instance in the frames of a given video. Due to the complex nature of this multimodal task, which combines text reasoning, video understanding, instance segmentation and tracking, existing approaches typically rely on sophisticated pipelines in order to tackle it. In this paper, we propose a simple Transformer-based approach to RVOS. Our framework, termed Multimodal Tracking Transformer (MTTR), models the RVOS task as a sequence prediction problem. Following recent advancements in computer vision and natural language processing, MTTR is based on the realization that video and text can be processed together effectively and elegantly by a single multimodal Transformer model. MTTR is end-to-end trainable, free of text-related inductive bias components and requires no additional mask-refinement post-processing steps. As such, it simplifies the RVOS pipeline considerably compared to existing methods. Evaluation on standard benchmarks reveals that MTTR significantly outperforms previous art across multiple metrics. In particular, MTTR shows impressive +5.7 and +5.0 mAP gains on the A2D-Sentences and JHMDB-Sentences datasets respectively, while processing 76 frames per second. In addition, we report strong results on the public validation set of Refer-YouTube-VOS, a more challenging RVOS dataset that has yet to receive the attention of researchers. The code to reproduce our experiments is available at https://github.com/mttr2021/MTTR

</details>

### WebQA: Multihop and Multimodal QA.
- **链接**: [arXiv:2109.00590](https://arxiv.org/abs/2109.00590) · 📚 被引 58
- **作者**: Yingshan Chang, Guihong Cao, Mridu Narang, Jianfeng Gao, Hisami Suzuki, Yonatan Bisk
- **🏷️ 机构**: Carnegie Mellon University, Microsoft, Bing Search, Microsoft Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling Visual Question Answering (VQA) to the open-domain and multi-hop nature of web searches, requires fundamental advances in visual representation learning, knowledge aggregation, and language generation. In this work, we introduce WebQA, a challenging new benchmark that proves difficult for large-scale state-of-the-art models which lack language groundable visual representations for novel objects and the ability to reason, yet trivial for humans. WebQA mirrors the way humans use the web: 1) Ask a question, 2) Choose sources to aggregate, and 3) Produce a fluent language response. This is the behavior we should be expecting from IoT devices and digital assistants. Existing work prefers to assume that a model can either reason about knowledge in images or in text. WebQA includes a secondary text-only QA task to ensure improved visual performance does not come at the cost of language understanding. Our challenge for the community is to create unified multimodal reasoning models that answer questions regardless of the source modality, moving us closer to digital assistants that not only query language knowledge, but also the richer visual online world.

</details>

### STCrowd: A Multimodal Dataset for Pedestrian Perception in Crowded Scenes.
- **链接**: [arXiv:2204.01026](https://arxiv.org/abs/2204.01026) · 📚 被引 45
- **作者**: Peishan Cong, Xinge Zhu, Feng Qiao, Yiming Ren, Xidong Peng, Yuenan Hou et al.
- **🏷️ 机构**: ShanghaiTech University, The Chinese University of Hong Kong, RWTH Aachen University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately detecting and tracking pedestrians in 3D space is challenging due to large variations in rotations, poses and scales. The situation becomes even worse for dense crowds with severe occlusions. However, existing benchmarks either only provide 2D annotations, or have limited 3D annotations with low-density pedestrian distribution, making it difficult to build a reliable pedestrian perception system especially in crowded scenes. To better evaluate pedestrian perception algorithms in crowded scenarios, we introduce a large-scale multimodal dataset,STCrowd. Specifically, in STCrowd, there are a total of 219 K pedestrian instances and 20 persons per frame on average, with various levels of occlusion. We provide synchronized LiDAR point clouds and camera images as well as their corresponding 3D labels and joint IDs. STCrowd can be used for various tasks, including LiDAR-only, image-only, and sensor-fusion based pedestrian detection and tracking. We provide baselines for most of the tasks. In addition, considering the property of sparse global distribution and density-varying local distribution of pedestrians, we further propose a novel method, Density-aware Hierarchical heatmap Aggregation (DHA), to enhance pedestrian perception in crowded scenes. Extensive experiments show that our new method achieves state-of-the-art performance for pedestrian detection on various datasets.

</details>

### MuKEA: Multimodal Knowledge Extraction and Accumulation for Knowledge-based Visual Question Answering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00503) · 📚 被引 112
- **作者**: Yang Ding, Jing Yu, Bang Liu, Yue Hu, Mingxin Cui, Qi Wu
- **🏷️ 机构**: Institute of Information Engineering, Chinese Academy of Sciences,Beijing,China, Universit&#x00E9; de Montr&#x00E9;al,Canada, University of Adelaide,Australia
- **会议**: CVPR 2022

### Egocentric Scene Understanding via Multimodal Spatial Rectifier.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00285) · 📚 被引 4
- **作者**: Tien Do, Khiem Vuong, Hyun Soo Park
- **🏷️ 机构**: University of Minnesota, Carnegie Mellon University
- **会议**: CVPR 2022

### XYLayoutLM: Towards Layout-Aware Multimodal Networks For Visually-Rich Document Understanding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00454) · 📚 被引 70
- **作者**: Zhangxuan Gu, Changhua Meng, Ke Wang, Jun Lan, Weiqiang Wang, Ming Gu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence,Department of Computer Science and Engineering, Ant Group
- **会议**: CVPR 2022

### 3MASSIV: Multilingual, Multimodal and Multi-Aspect dataset of Social Media Short Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02039) · 📚 被引 13
- **作者**: Vikram Gupta, Trisha Mittal, Puneet Mathur, Vaibhav Mishra, Mayank Maheshwari, Aniket Bera et al.
- **🏷️ 机构**: ShareChat,India, University of Maryland, College Park,USA
- **会议**: CVPR 2022

### Show Me What and Tell Me How: Video Synthesis via Multimodal Conditioning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00360) · 📚 被引 37
- **作者**: Ligong Han, Jian Ren, Hsin-Ying Lee, Francesco Barbieri, Kyle Olszewski, Shervin Minaee et al.
- **🏷️ 机构**: Snap Inc., Rutgers University
- **会议**: CVPR 2022

### Towards Multimodal Depth Estimation from Light Fields.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01261) · 📚 被引 15
- **作者**: Titus Leistner, Radek Mackowiak, Lynton Ardizzone, Ullrich Köthe, Carsten Rother
- **🏷️ 机构**: Heidelberg University,Visual Learning Lab
- **会议**: CVPR 2022

### Multimodal Material Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01918)
- **作者**: Yupeng Liang, Ryosuke Wakaki, Shohei Nobuhara, Ko Nishino
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Balanced Multimodal Learning via On-the-fly Gradient Modulation.
- **链接**: [arXiv:2203.15332](https://arxiv.org/abs/2203.15332) · [代码](https://github.com/GeWu-Lab/OGM-GE_CVPR2022) · 📚 被引 324
- **作者**: Xiaokang Peng, Yake Wei, Andong Deng, Dong Wang, Di Hu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing, Beijing Key Laboratory of Big Data Management and Analysis Methods,Beijing, Shanghai Jiao Tong University,Shanghai
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning helps to comprehensively understand the world, by integrating different senses. Accordingly, multiple input modalities are expected to boost model performance, but we actually find that they are not fully exploited even when the multimodal model outperforms its uni-modal counterpart. Specifically, in this paper we point out that existing multimodal discriminative models, in which uniform objective is designed for all modalities, could remain under-optimized uni-modal representations, caused by another dominated modality in some scenarios, e.g., sound in blowing wind event, vision in drawing picture event, etc. To alleviate this optimization imbalance, we propose on-the-fly gradient modulation to adaptively control the optimization of each modality, via monitoring the discrepancy of their contribution towards the learning objective. Further, an extra Gaussian noise that changes dynamically is introduced to avoid possible generalization drop caused by gradient modulation. As a result, we achieve considerable improvement over common fusion methods on different multimodal tasks, and this simple strategy can also boost existing multimodal methods, which illustrates its efficacy and versatility. The source code is available at \url{https://github.com/GeWu-Lab/OGM-GE_CVPR2022}.

</details>

### Motron: Multimodal Probabilistic Human Motion Forecasting.
- **链接**: [arXiv:2203.04132](https://arxiv.org/abs/2203.04132) · 📚 被引 39
- **作者**: Tim Salzmann, Marco Pavone, Markus Ryll
- **🏷️ 机构**: Technical University of Munich, Stanford University
- **会议**: CVPR 2022

### Can Push-forward Generative Models Fit Multimodal Distributions?
- **链接**: [arXiv:2206.14476](https://arxiv.org/abs/2206.14476) · 📚 被引 4
- **作者**: Antoine Salmona, Valentin De Bortoli, Julie Delon, Agnès Desolneux
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

> Autonomous systems and humans are increasingly sharing the same space. Robots work side by side or even hand in hand with humans to balance each other's limitations. Such cooperative interactions are ever more sophisticated. Thus, the ability to reason not just about a human's center of gravity position, but also its granular motion is an important prerequisite for human-robot interaction. Though, many algorithms ignore the multimodal nature of humans or neglect uncertainty in their motion forecasts. We present Motron, a multimodal, probabilistic, graph-structured model, that captures human's multimodality using probabilistic methods while being able to output deterministic maximum-likelihood motions and corresponding confidence values for each mode. Our model aims to be tightly integrated with the robotic planning-control-interaction loop; outputting physically feasible human motions and being computationally efficient. We demonstrate the performance of our model on several challenging real-world motion forecasting datasets, outperforming a wide array of generative/variational methods while providing state-of-the-art single-output motions if required. Both using significantly less computational power than state-of-the art algorithms.

</details>

### End-to-end Generative Pretraining for Multimodal Video Captioning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01743) · 📚 被引 133
- **作者**: Paul Hongsuck Seo, Arsha Nagrani, Anurag Arnab, Cordelia Schmid
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2022

### Dual-Key Multimodal Backdoors for Visual Question Answering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01494) · 📚 被引 28
- **作者**: Matthew Walmer, Karan Sikka, Indranil Sur, Abhinav Shrivastava, Susmit Jha
- **🏷️ 机构**: University of Maryland,College Park, SRI International
- **会议**: CVPR 2022

### MNSRNet: Multimodal Transformer Network for 3D Surface Super-Resolution.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01237) · 📚 被引 5
- **作者**: Wuyuan Xie, Tengcong Huang, Miaohui Wang
- **🏷️ 机构**: College of Computer Science and Software Engineering, Shenzhen University, Shenzhen University,Guangdong Key Laboratory of Intelligent Information Processing
- **会议**: CVPR 2022

### CrossLoc: Scalable Aerial Localization Assisted by Multimodal Synthetic Data.
- **链接**: [arXiv:2112.09081](https://arxiv.org/abs/2112.09081) · 📚 被引 20
- **作者**: Qi Yan, Jianhao Zheng, Simon Reding, Shanci Li, Iordan Doytchinov
- **🏷️ 机构**: Ecole Polytechnique F&#x00E9;d&#x00E9;rale de Lausanne (EPFL),TOPO laboratory
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a visual localization system that learns to estimate camera poses in the real world with the help of synthetic data. Despite significant progress in recent years, most learning-based approaches to visual localization target at a single domain and require a dense database of geo-tagged images to function well. To mitigate the data scarcity issue and improve the scalability of the neural localization models, we introduce TOPO-DataGen, a versatile synthetic data generation tool that traverses smoothly between the real and virtual world, hinged on the geographic camera viewpoint. New large-scale sim-to-real benchmark datasets are proposed to showcase and evaluate the utility of the said synthetic data. Our experiments reveal that synthetic data generically enhances the neural network performance on real data. Furthermore, we introduce CrossLoc, a cross-modal visual representation learning approach to pose estimation that makes full use of the scene coordinate ground truth via self-supervision. Without any extra data, CrossLoc significantly outperforms the state-of-the-art methods and achieves substantially higher real-data sample efficiency. Our code and datasets are all available at https://crossloc.github.io/.

</details>

### VisualHow: Multimodal Problem Solving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01518) · 📚 被引 5
- **作者**: Jinhui Yang, Xianyu Chen, Ming Jiang, Shi Chen, Louis Wang, Qi Zhao
- **🏷️ 机构**: University of Minnesota
- **会议**: CVPR 2022

### M5Product: Self-harmonized Contrastive Learning for E-commercial Multi-modal Pretraining.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02057) · 📚 被引 25
- **作者**: Xiao Dong, Xunlin Zhan, Yangxin Wu, Yunchao Wei, Michael C. Kampffmeyer, Xiaoyong Wei et al.
- **🏷️ 机构**: Sun Yat-sen University, Beijing Jiaotong University, UiT The Arctic University of Norway
- **会议**: CVPR 2022

### EI-CLIP: Entity-aware Interventional Contrastive Learning for E-commerce Cross-modal Retrieval.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01752)
- **作者**: Haoyu Ma, Handong Zhao, Zhe Lin, Ajinkya Kale, Zhangyang Wang, Tong Yu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Interact before Align: Leveraging Cross-Modal Knowledge for Domain Adaptive Action Recognition. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01431) · 📚 被引 32
- **作者**: Lijin Yang, Yifei Huang, Yusuke Sugano, Yoichi Sato
- **🏷️ 机构**: Institute of Industrial Science, The University of Tokyo
- **会议**: CVPR 2022
- **摘要（中）**: ①针对无监督域适应动作识别中，跨模态对齐前缺乏有效交互导致域偏移问题。②提出在特征对齐前先进行跨模态知识交互的方法，利用多模态信息增强域适应能力。③相比直接对齐方法，强调交互阶段对模态互补性的利用。④摘要缺失，无法提供具体数据，但方法设计具有合理性。
- **摘要（英）**: This paper addresses the problem of unsupervised domain adaptation in action recognition by proposing a cross-modal interaction step before alignment. It leverages multimodal knowledge to improve domain adaptation, though specific results are unavailable due to missing abstract details.
- **核心贡献**: 提出交互-对齐两阶段框架用于域适应动作识别。
- **创新点**: 在域适应中引入跨模态交互前置阶段。
- **结果**: 摘要未提供具体数据。

### Robust Cross-Modal Representation Learning with Progressive Self-Distillation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2204.04588](https://arxiv.org/abs/2204.04588) · 📚 被引 46
- **作者**: Alex Andonian, Shixing Chen, Raffay Hamid
- **🏷️ 机构**: MIT CSAIL, Amazon Prime Video
- **会议**: CVPR 2022
- **摘要（中）**: ①针对CLIP在噪声图文数据上训练效率低、表示鲁棒性不足的问题。②提出渐进自蒸馏框架，通过模型自身生成软对齐目标，动态调整图像-文本匹配。③相比CLIP，无需额外计算成本，通过软对齐缓解噪声对应关系。④在14个基准数据集上，零样本分类、线性探测和图文检索均优于CLIP，且对自然分布偏移具有更好的有效鲁棒性。
- **摘要（英）**: This paper tackles the inefficiency of CLIP training on noisy web data by introducing progressive self-distillation with soft image-text alignments. The method dynamically generates soft targets from the model itself, improving robustness without extra compute. It outperforms CLIP across 14 benchmarks in zero-shot, linear probe, and retrieval, with better effective robustness to distribution shifts.
- **核心贡献**: 提出渐进自蒸馏的跨模态对比学习框架，提升噪声数据下的表示质量。
- **创新点**: 利用模型自身知识生成软对齐目标，替代硬标签。
- **结果**: 在14个数据集上全面超越CLIP，且鲁棒性更优。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The learning objective of vision-language approach of CLIP does not effectively account for the noisy many-to-many correspondences found in web-harvested image captioning datasets, which contributes to its compute and data inefficiency. To address this challenge, we introduce a novel training framework based on cross-modal contrastive learning that uses progressive self-distillation and soft image-text alignments to more efficiently learn robust representations from noisy data. Our model distills its own knowledge to dynamically generate soft-alignment targets for a subset of images and captions in every minibatch, which are then used to update its parameters. Extensive evaluation across 14 benchmark datasets shows that our method consistently outperforms its CLIP counterpart in multiple settings, including: (a) zero-shot classification, (b) linear probe transfer, and (c) image-text retrieval, without incurring added computational cost. Analysis using an ImageNet-based robustness test-bed reveals that our method offers better effective robustness to natural distribution shifts compared to both ImageNet-trained models and CLIP itself. Lastly, pretraining with datasets spanning two orders of magnitude in size shows that our improvements over CLIP tend to scale with number of training examples.

</details>

### Scaling Multimodal Pre-Training via Cross-Modality Gradient Harmonization.
- **链接**: [arXiv:2211.02077](https://arxiv.org/abs/2211.02077) · 📚 被引 2
- **作者**: Junru Wu, Yi Liang, Feng Han, Hassan Akbari, Zhangyang Wang, Cong Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Multi-Lingual Acquisition on Multimodal Pre-training for Cross-modal Retrieval.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/bfadef437ed27372648714c930c3a77a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Liang Zhang, Anwen Hu, Qin Jin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

- DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CroMo: Cross-Modal Learning for Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)

## 🆕 增量新增

### Multimodal Object Detection via Probabilistic Ensembling. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_9) · 📚 被引 201
- **作者**: Yi-Ting Chen, Jinghao Shi, Zelin Ye, Christoph Mertz, Deva Ramanan, Shu Kong
- **🏷️ 机构**: CMU
- **会议**: ECCV 2022
- **摘要（中）**: 针对多模态目标检测中不同模态预测不一致的问题，论文提出了一种概率集成方法，通过建模各模态预测的不确定性来加权融合结果。该方法利用概率分布表示每个模态的检测输出，并基于贝叶斯规则进行集成，从而减少冲突并提高整体可靠性。相比传统确定性融合，该方法能更好地处理噪声和缺失模态。实验显示，在多个多模态数据集上，该方法显著提升了检测精度和鲁棒性。
- **摘要（英）**: This paper tackles inconsistent predictions in multimodal object detection by proposing a probabilistic ensembling method that weights fusion based on uncertainty. It models each modality's output as a probability distribution and integrates them via Bayesian rules, improving robustness against noise and missing modalities, with significant accuracy gains on multimodal datasets.
- **核心贡献**: 提出概率集成框架，利用不确定性加权提升多模态检测性能。
- **创新点**: 将概率建模引入多模态检测集成，处理预测冲突。
- **结果**: 在多个数据集上提升精度和鲁棒性。

### Multimodal Transformer for Automatic 3D Annotation and Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2207.09805](https://arxiv.org/abs/2207.09805)
- **作者**: Chang Liu, Xiaoyan Qian, Binxiao Huang, Xiaojuan Qi, Edmund Y. Lam, Siew-Chong Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对LiDAR扫描中3D框标注成本高的问题，本文提出端到端多模态Transformer自动标注器MTrans，利用LiDAR和图像从弱2D框生成精确3D框。方法通过图像信息生成新3D点来缓解点云稀疏性，并多任务同时进行前景分割、点云稠密化和3D框回归。在KITTI上，相比最先进自动标注器，moderate和hard样本的3D AP分别提升4.48%和4.03%，并扩展到3D检测达到89.45% AP。
- **摘要（英）**: This paper proposes MTrans, an end-to-end multimodal transformer autolabeler that generates precise 3D boxes from weak 2D boxes using LiDAR and images, densifying sparse point clouds with image-derived points. It improves 3D AP by 4.48% and 4.03% on KITTI moderate and hard samples versus SOTA autolabeler, and extends to detection with 89.45% AP.
- **核心贡献**: 提出多模态Transformer自动标注器，从弱2D框生成精确3D框。
- **创新点**: 通过图像生成3D点稠密化点云，缓解稀疏性问题。
- **结果**: 在KITTI上显著提升标注质量和检测精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite a growing number of datasets being collected for training 3D object detection models, significant human effort is still required to annotate 3D boxes on LiDAR scans. To automate the annotation and facilitate the production of various customized datasets, we propose an end-to-end multimodal transformer (MTrans) autolabeler, which leverages both LiDAR scans and images to generate precise 3D box annotations from weak 2D bounding boxes. To alleviate the pervasive sparsity problem that hinders existing autolabelers, MTrans densifies the sparse point clouds by generating new 3D points based on 2D image information. With a multi-task design, MTrans segments the foreground/background, densifies LiDAR point clouds, and regresses 3D boxes simultaneously. Experimental results verify the effectiveness of the MTrans for improving the quality of the generated labels. By enriching the sparse point clouds, our method achieves 4.48\% and 4.03\% better 3D AP on KITTI moderate and hard samples, respectively, versus the state-of-the-art autolabeler. MTrans can also be extended to improve the accuracy for 3D object detection, resulting in a remarkable 89.45\% AP on KITTI hard samples. Codes are at \url{https://github.com/Cliu2/MTrans}.

</details>

### Class-Agnostic Object Detection with Multi-modal Transformer. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_30) · 📚 被引 68
- **作者**: Muhammad Maaz, Hanoona Abdul Rasheed, Salman Khan, Fahad Shahbaz Khan, Rao Muhammad Anwer, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对类别无关目标检测问题，提出一种基于多模态Transformer的检测框架。方法利用多模态信息（如文本或音频）增强目标提议的生成与分类，从而实现对任意类别目标的检测。通过跨模态注意力机制，模型能够更好地捕捉目标的语义特征。实验在多个数据集上验证了方法的有效性，但具体细节和量化结果在摘要中未给出。
- **摘要（英）**: This paper addresses class-agnostic object detection by proposing a multi-modal Transformer framework. The method leverages multi-modal information to enhance proposal generation and classification, enabling detection of arbitrary categories. Cross-modal attention helps capture semantic features, with effectiveness demonstrated across datasets, though specific quantitative results are not detailed in the abstract.
- **核心贡献**: 提出多模态Transformer用于类别无关目标检测。
- **创新点**: 利用跨模态注意力融合多源信息。
- **结果**: 在多个数据集上验证了有效性。

### Multi-modal Masked Pre-training for Monocular Panoramic Depth Completion. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.09855](https://arxiv.org/abs/2203.09855) · 📚 被引 28
- **作者**: Zhiqiang Yan, Xiang Li, Kun Wang, Zhenyu Zhang, Jun Li, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对全景深度补全（PDC）任务中，360°深度传感器在复杂场景下产生稀疏深度数据，需要结合RGB图像恢复密集深度的问题。②提出多模态掩码预训练方法M^3PT，在预训练阶段用共享随机掩码同时遮盖全景RGB图像和稀疏深度图的块，并重建掩码区域的稀疏深度。③相比MAE仅处理单模态，首次将掩码预训练扩展到多模态视觉任务，且预训练与微调架构一致，无需丢弃解码器。④实验表明该方法有效提升密集全景深度恢复性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses monocular panoramic depth completion by proposing M^3PT, a multi-modal masked pre-training approach that jointly masks and reconstructs patches of RGB images and sparse depth. It extends masked autoencoding to multi-modal tasks with no architectural gap between pre-training and fine-tuning. Experiments demonstrate improved dense depth recovery, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出首个多模态掩码预训练框架用于全景深度补全。
- **创新点**: 将MAE的掩码重建思想扩展到RGB和深度双模态输入。
- **结果**: 在PDC任务上验证了预训练方法的有效性，但未给出具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we formulate a potentially valuable panoramic depth completion (PDC) task as panoramic 3D cameras often produce 360° depth with missing data in complex scenes. Its goal is to recover dense panoramic depths from raw sparse ones and panoramic RGB images. To deal with the PDC task, we train a deep network that takes both depth and image as inputs for the dense panoramic depth recovery. However, it needs to face a challenging optimization problem of the network parameters due to its non-convex objective function. To address this problem, we propose a simple yet effective approach termed M{^3}PT: multi-modal masked pre-training. Specifically, during pre-training, we simultaneously cover up patches of the panoramic RGB image and sparse depth by shared random mask, then reconstruct the sparse depth in the masked regions. To our best knowledge, it is the first time that we show the effectiveness of masked pre-training in a multi-modal vision task, instead of the single-modal task resolved by masked autoencoders (MAE). Different from MAE where fine-tuning completely discards the decoder part of pre-training, there is no architectural difference between the pre-training and fine-tuning stages in our M$^{3}$PT as they only differ in the prediction density, which potentially makes the transfer learning more convenient and effective. Extensive experiments verify the effectiveness of M{^3}PT on three panoramic datasets. Notably, we improve the state-of-the-art baselines by averagely 26.2% in RMSE, 51.7% in MRE, 49.7% in MAE, and 37.5% in RMSElog on three benchmark datasets.

</details>

### Multimodal Transformer with Variable-Length Memory for Vision-and-Language Navigation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2111.05759](https://arxiv.org/abs/2111.05759) · 📚 被引 29
- **作者**: Chuang Lin, Yi Jiang, Jianfei Cai, Lizhen Qu, Gholamreza Haffari, Zehuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视觉-语言导航（VLN）中，现有Transformer方法用固定长度向量表示时间上下文，难以捕捉长期依赖的问题。②提出带可变长度记忆的多模态Transformer（MTVM），通过记忆库直接存储历史激活，并引入记忆感知一致性损失，增强时间上下文表示。③相比LSTM解码器或固定隐藏状态，可变长度记忆更灵活，能保留更多轨迹信息。④实验表明MTVM在VLN基准上优于现有方法，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the limitation of fixed-length temporal context in Transformer-based VLN by introducing MTVM, which stores previous activations in a variable-length memory bank and uses a memory-aware consistency loss. This enables better long-term context modeling compared to LSTM or fixed hidden states. Experiments show improved navigation performance, though specific metrics are not given.
- **核心贡献**: 提出可变长度记忆的多模态Transformer用于视觉-语言导航。
- **创新点**: 用记忆库替代固定长度向量以增强时间上下文。
- **结果**: 在VLN任务上取得优于现有方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-Language Navigation (VLN) is a task that an agent is required to follow a language instruction to navigate to the goal position, which relies on the ongoing interactions with the environment during moving. Recent Transformer-based VLN methods have made great progress benefiting from the direct connections between visual observations and the language instruction via the multimodal cross-attention mechanism. However, these methods usually represent temporal context as a fixed-length vector by using an LSTM decoder or using manually designed hidden states to build a recurrent Transformer. Considering a single fixed-length vector is often insufficient to capture long-term temporal context, in this paper, we introduce Multimodal Transformer with Variable-length Memory (MTVM) for visually-grounded natural language navigation by modelling the temporal context explicitly. Specifically, MTVM enables the agent to keep track of the navigation trajectory by directly storing previous activations in a memory bank. To further boost the performance, we propose a memory-aware consistency loss to help learn a better joint representation of temporal context with random masked instructions. We evaluate MTVM on popular R2R and CVDN datasets, and our model improves Success Rate on R2R unseen validation and test set by 2% each, and reduce Goal Process by 1.6m on CVDN test set.

</details>

### Switch-BERT: Learning to Model Multimodal Interactions by Switching Attention and Input. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2306.14182](https://arxiv.org/abs/2306.14182) · 📚 被引 6
- **作者**: Qingpei Guo, Kaisheng Yao, Wei Chu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多模态模型中固定结构难以适应不同模态输入组合的模态不匹配问题。②提出Switch-BERT，扩展BERT架构，引入可学习的层内和跨层交互，从一组注意力模式中优化选择，并学习关注不同深度的输出。③相比ViLBERT和UNITER等固定结构模型，Switch-BERT能动态调整注意力，缓解模态不匹配。④在VQA、图像-文本检索和指代表达理解任务上，Switch-BERT一致优于或媲美现有模型，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses modality mismatch in fixed-structure multimodal models by proposing Switch-BERT, which learns layer-wise and cross-layer attention modes and attends to outputs from various depths. This dynamic adaptation mitigates mismatch issues compared to ViLBERT and UNITER. Experiments on VQA, retrieval, and referring expression tasks show consistent improvements or comparable performance, though specific metrics are omitted.
- **核心贡献**: 提出可学习注意力模式的Switch-BERT用于多模态表示学习。
- **创新点**: 通过切换注意力模式适应不同模态输入。
- **结果**: 在多个多模态任务上取得优于或媲美现有模型的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to model intra-modal and inter-modal interactions is fundamental in multimodal machine learning. The current state-of-the-art models usually adopt deep learning models with fixed structures. They can achieve exceptional performances on specific tasks, but face a particularly challenging problem of modality mismatch because of diversity of input modalities and their fixed structures. In this paper, we present \textbf{Switch-BERT} for joint vision and language representation learning to address this problem. Switch-BERT extends BERT architecture by introducing learnable layer-wise and cross-layer interactions. It learns to optimize attention from a set of attention modes representing these interactions. One specific property of the model is that it learns to attend outputs from various depths, therefore mitigates the modality mismatch problem. We present extensive experiments on visual question answering, image-text retrieval and referring expression comprehension experiments. Results confirm that, whereas alternative architectures including ViLBERT and UNITER may excel in particular tasks, Switch-BERT can consistently achieve better or comparable performances than the current state-of-the-art models in these tasks. Ablation studies indicate that the proposed model achieves superior performances due to its ability in learning task-specific multimodal interactions.

</details>

### MUGEN: A Playground for Video-Audio-Text Multimodal Understanding and GENeration. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2204.08058](https://arxiv.org/abs/2204.08058) · 📚 被引 19
- **作者**: Thomas Hayes, Songyang Zhang, Xi Yin, Guan Pang, Sasha Sheng, Harry Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多模态视频-音频-文本理解与生成缺乏丰富且可控数据集的问题。②构建MUGEN数据集，基于游戏平台CoinRun修改，引入音频和新交互，训练RL代理生成375K个视频片段，并收集人工文本描述和自动语义标注。③相比现有数据集，MUGEN提供窄而丰富的任务环境，支持检索和生成基准测试。④基准实验显示该数据集能有效评估多模态方法，但摘要未提供具体性能数据。
- **摘要（英）**: This paper introduces MUGEN, a large-scale video-audio-text dataset built on a modified CoinRun game, with 375K clips, human annotations, and automatic semantic maps. It provides a controlled environment for multimodal understanding and generation tasks. Benchmarks demonstrate its utility for evaluating retrieval and generation methods, though specific results are not detailed.
- **核心贡献**: 构建了大规模视频-音频-文本数据集MUGEN及基准。
- **创新点**: 利用游戏引擎生成可控且丰富的多模态数据。
- **结果**: 为多模态理解与生成提供有效基准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal video-audio-text understanding and generation can benefit from datasets that are narrow but rich. The narrowness allows bite-sized challenges that the research community can make progress on. The richness ensures we are making progress along the core challenges. To this end, we present a large-scale video-audio-text dataset MUGEN, collected using the open-sourced platform game CoinRun [11]. We made substantial modifications to make the game richer by introducing audio and enabling new interactions. We trained RL agents with different objectives to navigate the game and interact with 13 objects and characters. This allows us to automatically extract a large collection of diverse videos and associated audio. We sample 375K video clips (3.2s each) and collect text descriptions from human annotators. Each video has additional annotations that are extracted automatically from the game engine, such as accurate semantic maps for each frame and templated textual descriptions. Altogether, MUGEN can help progress research in many tasks in multimodal understanding and generation. We benchmark representative approaches on tasks involving video-audio-text retrieval and generation. Our dataset and code are released at: https://mugen-org.github.io/.

</details>

### Multimodal Conditional Image Synthesis with Product-of-Experts GANs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19787-1_6) · 📚 被引 54
- **作者**: Xun Huang, Arun Mallya, Ting-Chun Wang, Ming-Yu Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Learning Mutual Modulation for Self-supervised Cross-Modal Super-Resolution.
- **链接**: [arXiv:2207.09156](https://arxiv.org/abs/2207.09156) · 📚 被引 15
- **作者**: Xiaoyu Dong, Naoto Yokoya, Longguang Wang, Tatsumi Uezato
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised cross-modal super-resolution (SR) can overcome the difficulty of acquiring paired training data, but is challenging because only low-resolution (LR) source and high-resolution (HR) guide images from different modalities are available. Existing methods utilize pseudo or weak supervision in LR space and thus deliver results that are blurry or not faithful to the source modality. To address this issue, we present a mutual modulation SR (MMSR) model, which tackles the task by a mutual modulation strategy, including a source-to-guide modulation and a guide-to-source modulation. In these modulations, we develop cross-domain adaptive filters to fully exploit cross-modal spatial dependency and help induce the source to emulate the resolution of the guide and induce the guide to mimic the modality characteristics of the source. Moreover, we adopt a cycle consistency constraint to train MMSR in a fully self-supervised manner. Experiments on various tasks demonstrate the state-of-the-art performance of our MMSR.

</details>

### CMD: Self-supervised 3D Action Representation Learning with Cross-Modal Mutual Distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20062-5_42) · 📚 被引 62
- **作者**: Yunyao Mao, Wengang Zhou, Zhenbo Lu, Jiajun Deng, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Drive&Segment: Unsupervised Semantic Segmentation of Urban Scenes via Cross-Modal Distillation.
- **链接**: [arXiv:2203.11160](https://arxiv.org/abs/2203.11160)
- **作者**: Antonín Vobecký, David Hurych, Oriane Siméoni, Spyros Gidaris, Andrei Bursuc, Patrick Pérez et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work investigates learning pixel-wise semantic image segmentation in urban scenes without any manual annotation, just from the raw non-curated data collected by cars which, equipped with cameras and LiDAR sensors, drive around a city. Our contributions are threefold. First, we propose a novel method for cross-modal unsupervised learning of semantic image segmentation by leveraging synchronized LiDAR and image data. The key ingredient of our method is the use of an object proposal module that analyzes the LiDAR point cloud to obtain proposals for spatially consistent objects. Second, we show that these 3D object proposals can be aligned with the input images and reliably clustered into semantically meaningful pseudo-classes. Finally, we develop a cross-modal distillation approach that leverages image data partially annotated with the resulting pseudo-classes to train a transformer-based model for image semantic segmentation. We show the generalization capabilities of our method by testing on four different testing datasets (Cityscapes, Dark Zurich, Nighttime Driving and ACDC) without any finetuning, and demonstrate significant improvements compared to the current state of the art on this problem. See project webpage https://vobecant.github.io/DriveAndSegment/ for the code and more.

</details>

### On the Limitations of Multimodal VAEs.
- **链接**: [arXiv:2110.04121](https://arxiv.org/abs/2110.04121)
- **作者**: Imant Daunhawer, Thomas M. Sutter, Kieran Chin-Cheong, Emanuele Palumbo, Julia E. Vogt
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal variational autoencoders (VAEs) have shown promise as efficient generative models for weakly-supervised data. Yet, despite their advantage of weak supervision, they exhibit a gap in generative quality compared to unimodal VAEs, which are completely unsupervised. In an attempt to explain this gap, we uncover a fundamental limitation that applies to a large family of mixture-based multimodal VAEs. We prove that the sub-sampling of modalities enforces an undesirable upper bound on the multimodal ELBO and thereby limits the generative quality of the respective models. Empirically, we showcase the generative quality gap on both synthetic and real data and present the tradeoffs between different variants of multimodal VAEs. We find that none of the existing approaches fulfills all desired criteria of an effective multimodal generative model when applied on more complex datasets than those used in previous benchmarks. In summary, we identify, formalize, and validate fundamental limitations of VAE-based approaches for modeling weakly-supervised data and discuss implications for real-world applications.

</details>

### Learning Multimodal VAEs through Mutual Supervision.
- **链接**: [arXiv:2106.12570](https://arxiv.org/abs/2106.12570)
- **作者**: Tom Joy, Yuge Shi, Philip H. S. Torr, Tom Rainforth, Sebastian M. Schmon, Siddharth Narayanaswamy
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal VAEs seek to model the joint distribution over heterogeneous data (e.g.\ vision, language), whilst also capturing a shared representation across such modalities. Prior work has typically combined information from the modalities by reconciling idiosyncratic representations directly in the recognition model through explicit products, mixtures, or other such factorisations. Here we introduce a novel alternative, the MEME, that avoids such explicit combinations by repurposing semi-supervised VAEs to combine information between modalities implicitly through mutual supervision. This formulation naturally allows learning from partially-observed data where some modalities can be entirely missing -- something that most existing approaches either cannot handle, or do so to a limited extent. We demonstrate that MEME outperforms baselines on standard metrics across both partial and complete observation schemes on the MNIST-SVHN (image-image) and CUB (image-text) datasets. We also contrast the quality of the representations learnt by mutual supervision against standard approaches and observe interesting trends in its ability to capture relatedness between data.

</details>

### Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction.
- **链接**: [arXiv:2201.02184](https://arxiv.org/abs/2201.02184)
- **作者**: Bowen Shi, Wei-Ning Hsu, Kushal Lakhotia, Abdelrahman Mohamed
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video recordings of speech contain correlated audio and visual information, providing a strong signal for speech representation learning from the speaker's lip movements and the produced sound. We introduce Audio-Visual Hidden Unit BERT (AV-HuBERT), a self-supervised representation learning framework for audio-visual speech, which masks multi-stream video input and predicts automatically discovered and iteratively refined multimodal hidden units. AV-HuBERT learns powerful audio-visual speech representation benefiting both lip-reading and automatic speech recognition. On the largest public lip-reading benchmark LRS3 (433 hours), AV-HuBERT achieves 32.5% WER with only 30 hours of labeled data, outperforming the former state-of-the-art approach (33.6%) trained with a thousand times more transcribed video data (31K hours). The lip-reading WER is further reduced to 26.9% when using all 433 hours of labeled data from LRS3 and combined with self-training. Using our audio-visual representation on the same benchmark for audio-only speech recognition leads to a 40% relative WER reduction over the state-of-the-art performance (1.3% vs 2.3%). Our code and models are available at https://github.com/facebookresearch/av_hubert

</details>

### Learning Vision-Guided Quadrupedal Locomotion End-to-End with Cross-Modal Transformers.
- **链接**: [arXiv:2107.03996](https://arxiv.org/abs/2107.03996)
- **作者**: Ruihan Yang, Minghao Zhang, Nicklas Hansen, Huazhe Xu, Xiaolong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose to address quadrupedal locomotion tasks using Reinforcement Learning (RL) with a Transformer-based model that learns to combine proprioceptive information and high-dimensional depth sensor inputs. While learning-based locomotion has made great advances using RL, most methods still rely on domain randomization for training blind agents that generalize to challenging terrains. Our key insight is that proprioceptive states only offer contact measurements for immediate reaction, whereas an agent equipped with visual sensory observations can learn to proactively maneuver environments with obstacles and uneven terrain by anticipating changes in the environment many steps ahead. In this paper, we introduce LocoTransformer, an end-to-end RL method that leverages both proprioceptive states and visual observations for locomotion control. We evaluate our method in challenging simulated environments with different obstacles and uneven terrain. We transfer our learned policy from simulation to a real robot by running it indoors and in the wild with unseen obstacles and terrain. Our method not only significantly improves over baselines, but also achieves far better generalization performance, especially when transferred to the real robot. Our project page with videos is at https://rchalyang.github.io/LocoTransformer/ .

</details>

### Poisoning and Backdooring Contrastive Learning.
- **链接**: [arXiv:2106.09667](https://arxiv.org/abs/2106.09667)
- **作者**: Nicholas Carlini, Andreas Terzis
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal contrastive learning methods like CLIP train on noisy and uncurated training datasets. This is cheaper than labeling datasets manually, and even improves out-of-distribution robustness. We show that this practice makes backdoor and poisoning attacks a significant threat. By poisoning just 0.01% of a dataset (e.g., just 300 images of the 3 million-example Conceptual Captions dataset), we can cause the model to misclassify test images by overlaying a small patch. Targeted poisoning attacks, whereby the model misclassifies a particular test input with an adversarially-desired label, are even easier requiring control of 0.0001% of the dataset (e.g., just three out of the 3 million images). Our attacks call into question whether training on noisy and uncurated Internet scrapes is desirable.

</details>

### Gaussian Mixture Variational Autoencoder with Contrastive Learning for Multi-Label Classification.
- **链接**: [arXiv:2112.00976](https://arxiv.org/abs/2112.00976)
- **作者**: Junwen Bai, Shufeng Kong, Carla P. Gomes
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-label classification (MLC) is a prediction task where each sample can have more than one label. We propose a novel contrastive learning boosted multi-label prediction model based on a Gaussian mixture variational autoencoder (C-GMVAE), which learns a multimodal prior space and employs a contrastive loss. Many existing methods introduce extra complex neural modules like graph neural networks to capture the label correlations, in addition to the prediction modules. We find that by using contrastive learning in the supervised setting, we can exploit label information effectively in a data-driven manner, and learn meaningful feature and label embeddings which capture the label correlations and enhance the predictive power. Our method also adopts the idea of learning and aligning latent spaces for both features and labels. In contrast to previous works based on a unimodal prior, C-GMVAE imposes a Gaussian mixture structure on the latent space, to alleviate the posterior collapse and over-regularization issues. C-GMVAE outperforms existing methods on multiple public datasets and can often match other models' full performance with only 50% of the training data. Furthermore, we show that the learnt embeddings provide insights into the interpretation of label-label interactions.

</details>

### Geometric Multimodal Contrastive Representation Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v162/poklukar22a.html)
- **作者**: Petra Poklukar, Miguel Vasco, Hang Yin, Francisco S. Melo, Ana Paiva, Danica Kragic
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Cross-modal Learning for Image-Guided Point Cloud Shape Completion.
- **链接**: [arXiv:2209.09552](https://arxiv.org/abs/2209.09552) · 📚 被引 15
- **作者**: Emanuele Aiello, Diego Valsesia, Enrico Magli
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper we explore the recent topic of point cloud completion, guided by an auxiliary image. We show how it is possible to effectively combine the information from the two modalities in a localized latent space, thus avoiding the need for complex point cloud reconstruction methods from single views used by the state-of-the-art. We also investigate a novel weakly-supervised setting where the auxiliary image provides a supervisory signal to the training process by using a differentiable renderer on the completed point cloud to measure fidelity in the image space. Experiments show significant improvements over state-of-the-art supervised methods for both unimodal and multimodal completion. We also show the effectiveness of the weakly-supervised approach which outperforms a number of supervised methods and is competitive with the latest supervised models only exploiting point cloud information.

</details>

## 跨领域论文（完整笔记在其他领域）

- Bridged Transformer for Vision and Point Cloud 3D Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Self-supervised object detection from audio-visual correspondence. → [object-detection](../object-detection/Guideline%202022.md)
- Focal Sparse Convolutional Networks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CrossPoint: Self-Supervised Cross-Modal Contrastive Learning for 3D Point Cloud Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Revisiting the "Video" in Video-Language Understanding. → [video-understanding](../video-understanding/Guideline%202022.md)
- Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Single-Stream Multi-level Alignment for Vision-Language Pretraining. → [vlm](../vlm/Guideline%202022.md)
- Generative Negative Text Replay for Continual Vision-Language Pretraining. → [vlm](../vlm/Guideline%202022.md)
- Sound Localization by Self-supervised Time Delay Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- PreTraM: Self-supervised Pre-training via Connecting Trajectory and Map. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- CODER: Coupled Diversity-Sensitive Momentum Contrastive Learning for Image-Text Retrieval. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Learning Visual Representation from Modality-Shared Contrastive Language-Image Pre-training. → [vlm](../vlm/Guideline%202022.md)
- DeepInteraction: 3D Object Detection via Modality Interaction. → [3d-detection](../3d-detection/Guideline%202022.md)
- Let Images Give You More: Point Cloud Cross-Modal Training for Shape Analysis. → [knowledge-distillation](../knowledge-distillation/Guideline%202022.md)

<!-- COMPLETE v1 papers=55 -->
