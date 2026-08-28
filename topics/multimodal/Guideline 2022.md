# Multimodal — 2022 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

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

### Text2Pos: Text-to-Point-Cloud Cross-Modal Localization.
- **链接**: [arXiv:2203.15125](https://arxiv.org/abs/2203.15125) · 📚 被引 26
- **作者**: Manuel Kolmet, Qunjie Zhou, Aljosa Osep, Laura Leal-Taixé
- **🏷️ 机构**: Technical University of Munich,Germany
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Natural language-based communication with mobile devices and home appliances is becoming increasingly popular and has the potential to become natural for communicating with mobile robots in the future. Towards this goal, we investigate cross-modal text-to-point-cloud localization that will allow us to specify, for example, a vehicle pick-up or goods delivery location. In particular, we propose Text2Pos, a cross-modal localization module that learns to align textual descriptions with localization cues in a coarse- to-fine manner. Given a point cloud of the environment, Text2Pos locates a position that is specified via a natural language-based description of the immediate surroundings. To train Text2Pos and study its performance, we construct KITTI360Pose, the first dataset for this task based on the recently introduced KITTI360 dataset. Our experiments show that we can localize 65% of textual queries within 15m distance to query locations for top-10 retrieved locations. This is a starting point that we hope will spark future developments towards language-based navigation.

</details>

### Multimodal Colored Point Cloud to Image Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00654) · 📚 被引 4
- **作者**: Noam Rotstein, Amit Bracha, Ron Kimmel
- **🏷️ 机构**: Technion - Israel Institute of Technology
- **会议**: CVPR 2022

### Open-Vocabulary Instance Segmentation via Robust Cross-Modal Pseudo-Labeling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00689)
- **作者**: Dat Huynh, Jason Kuen, Zhe Lin, Jiuxiang Gu, Ehsan Elhamifar
- **🏷️ 机构**: （机构待查）
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

### Learnable Irrelevant Modality Dropout for Multimodal Action Recognition on Modality-Specific Annotated Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01957) · 📚 被引 30
- **作者**: Saghir Alfasly, Jian Lu, Chen Xu, Yuru Zou
- **🏷️ 机构**: Shenzhen University,Shenzhen Key Laboratory of Advanced Machine Learning and Applications,China
- **会议**: CVPR 2022

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
- **链接**: [arXiv:2203.15332](https://arxiv.org/abs/2203.15332) · [代码](https://github.com/GeWu-Lab/OGM-GE_CVPR2022) · 📚 被引 323
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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous systems and humans are increasingly sharing the same space. Robots work side by side or even hand in hand with humans to balance each other's limitations. Such cooperative interactions are ever more sophisticated. Thus, the ability to reason not just about a human's center of gravity position, but also its granular motion is an important prerequisite for human-robot interaction. Though, many algorithms ignore the multimodal nature of humans or neglect uncertainty in their motion forecasts. We present Motron, a multimodal, probabilistic, graph-structured model, that captures human's multimodality using probabilistic methods while being able to output deterministic maximum-likelihood motions and corresponding confidence values for each mode. Our model aims to be tightly integrated with the robotic planning-control-interaction loop; outputting physically feasible human motions and being computationally efficient. We demonstrate the performance of our model on several challenging real-world motion forecasting datasets, outperforming a wide array of generative/variational methods while providing state-of-the-art single-output motions if required. Both using significantly less computational power than state-of-the art algorithms.

</details>

### End-to-end Generative Pretraining for Multimodal Video Captioning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01743) · 📚 被引 133
- **作者**: Paul Hongsuck Seo, Arsha Nagrani, Anurag Arnab, Cordelia Schmid
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2022

### ContIG: Self-supervised Multimodal Contrastive Learning for Medical Imaging with Genetics.
- **链接**: [arXiv:2111.13424](https://arxiv.org/abs/2111.13424) · 📚 被引 64
- **作者**: Aiham Taleb, Matthias Kirchler, Remo Monti, Christoph Lippert
- **🏷️ 机构**: Hasso Plattner Institute for Digital Engineering, University of Potsdam,Germany
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High annotation costs are a substantial bottleneck in applying modern deep learning architectures to clinically relevant medical use cases, substantiating the need for novel algorithms to learn from unlabeled data. In this work, we propose ContIG, a self-supervised method that can learn from large datasets of unlabeled medical images and genetic data. Our approach aligns images and several genetic modalities in the feature space using a contrastive loss. We design our method to integrate multiple modalities of each individual person in the same model end-to-end, even when the available modalities vary across individuals. Our procedure outperforms state-of-the-art self-supervised methods on all evaluated downstream benchmark tasks. We also adapt gradient-based explainability algorithms to better understand the learned cross-modal associations between the images and genetic modalities. Finally, we perform genome-wide association studies on the features learned by our models, uncovering interesting relationships between images and genetic data.

</details>

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01684) · 📚 被引 20
- **作者**: Qi Yan, Jianhao Zheng, Simon Reding, Shanci Li, Iordan Doytchinov
- **🏷️ 机构**: Ecole Polytechnique F&#x00E9;d&#x00E9;rale de Lausanne (EPFL),TOPO laboratory
- **会议**: CVPR 2022

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

### Interact before Align: Leveraging Cross-Modal Knowledge for Domain Adaptive Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01431) · 📚 被引 32
- **作者**: Lijin Yang, Yifei Huang, Yusuke Sugano, Yoichi Sato
- **🏷️ 机构**: Institute of Industrial Science, The University of Tokyo
- **会议**: CVPR 2022

### Robust Cross-Modal Representation Learning with Progressive Self-Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01594) · 📚 被引 46
- **作者**: Alex Andonian, Shixing Chen, Raffay Hamid
- **🏷️ 机构**: MIT CSAIL, Amazon Prime Video
- **会议**: CVPR 2022

## 跨领域论文（完整笔记在其他领域）

- DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CroMo: Cross-Modal Learning for Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
