# Object Detection — 2024 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### SARDet-100K: Towards Open-Source Benchmark and ToolKit for Large-Scale SAR Object Detection.
- **链接**: [arXiv:2403.06534](https://arxiv.org/abs/2403.06534) · [代码](https://github.com/zcablii/SARDet_100K) · 📚 被引 27
- **作者**: Yuxuan Li, Xiang Li, Weijie Li, Qibin Hou, Li Liu, Ming-Ming Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Synthetic Aperture Radar (SAR) object detection has gained significant attention recently due to its irreplaceable all-weather imaging capabilities. However, this research field suffers from both limited public datasets (mostly comprising <2K images with only mono-category objects) and inaccessible source code. To tackle these challenges, we establish a new benchmark dataset and an open-source method for large-scale SAR object detection. Our dataset, SARDet-100K, is a result of intense surveying, collecting, and standardizing 10 existing SAR detection datasets, providing a large-scale and diverse dataset for research purposes. To the best of our knowledge, SARDet-100K is the first COCO-level large-scale multi-class SAR object detection dataset ever created. With this high-quality dataset, we conducted comprehensive experiments and uncovered a crucial challenge in SAR object detection: the substantial disparities between the pretraining on RGB datasets and finetuning on SAR datasets in terms of both data domain and model structure. To bridge these gaps, we propose a novel Multi-Stage with Filter Augmentation (MSFA) pretraining framework that tackles the problems from the perspective of data input, domain transition, and model migration. The proposed MSFA method significantly enhances the performance of SAR object detection models while demonstrating exceptional generalizability and flexibility across diverse models. This work aims to pave the way for further advancements in SAR object detection. The dataset and code is available at https://github.com/zcablii/SARDet_100K.

</details>

### Long-tailed Object Detection Pretraining: Dynamic Rebalancing Contrastive Learning with Dual Reconstruction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/470629a47e2d65ce0606c40055df5d26-Abstract-Conference.html)
- **作者**: Chen-Long Duan, Yong Li, Xiu-Shen Wei, Lin Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### You Only Look Around: Learning Illumination-Invariant Feature for Low-light Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/9e74900c3f6100c56add4bf417547848-Abstract-Conference.html) · 📚 被引 27
- **作者**: Mingbo Hong, Shen Cheng, Haibin Huang, Haoqiang Fan, Shuaicheng Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Open-Vocabulary Object Detection via Language Hierarchy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/e1fcd183ab33714a8464e4e9a20ac710-Abstract-Conference.html)
- **作者**: Jiaxing Huang, Jingyi Zhang, Kai Jiang, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### DA-Ada: Learning Domain-Aware Adapter for Domain Adaptive Object Detection.
- **链接**: [arXiv:2410.09004](https://arxiv.org/abs/2410.09004) · [代码](https://github.com/Therock90421/DA-Ada) · 📚 被引 6
- **作者**: Haochen Li, Rui Zhang, Hantao Yao, Xin Zhang, Yifan Hao, Xinkai Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain adaptive object detection (DAOD) aims to generalize detectors trained on an annotated source domain to an unlabelled target domain. As the visual-language models (VLMs) can provide essential general knowledge on unseen images, freezing the visual encoder and inserting a domain-agnostic adapter can learn domain-invariant knowledge for DAOD. However, the domain-agnostic adapter is inevitably biased to the source domain. It discards some beneficial knowledge discriminative on the unlabelled domain, i.e., domain-specific knowledge of the target domain. To solve the issue, we propose a novel Domain-Aware Adapter (DA-Ada) tailored for the DAOD task. The key point is exploiting domain-specific knowledge between the essential general knowledge and domain-invariant knowledge. DA-Ada consists of the Domain-Invariant Adapter (DIA) for learning domain-invariant knowledge and the Domain-Specific Adapter (DSA) for injecting the domain-specific knowledge from the information discarded by the visual encoder. Comprehensive experiments over multiple DAOD tasks show that DA-Ada can efficiently infer a domain-aware visual encoder for boosting domain adaptive object detection. Our code is available at https://github.com/Therock90421/DA-Ada.

</details>

### DiPEx: Dispersing Prompt Expansion for Class-Agnostic Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/2c2e95b75a10adbd2359f8ed5c0a38cd-Abstract-Conference.html)
- **作者**: Jia Syuen Lim, Zhuoxiao Chen, Zhi Chen, Mahsa Baktashmotlagh, Xin Yu, Zi Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/80f48ffa8022773973a4a5cec7cce19c-Abstract-Conference.html) · 📚 被引 7
- **作者**: Zhiwei Lin, Yongtao Wang, Zhi Tang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Unsupervised Object Detection with Theoretical Guarantees.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b9b1d29de259b82c944b03b7322eae45-Abstract-Conference.html) · 📚 被引 0
- **作者**: Marian Longa, João F. Henriques
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Progressive Exploration-Conformal Learning for Sparsely Annotated Object Detection in Aerial Images.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/47a287298e7887d1c25d4aabb918bd54-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zihan Lu, Chenxu Wang, Chunyan Xu, Xiangwei Zheng, Zhen Cui
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Revisiting Few-Shot Object Detection with Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/22b2067b8f680812624032025864c5a1-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Anish Madan, Neehar Peri, Shu Kong, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: NeurIPS 2024

### DI-MaskDINO: A Joint Object Detection and Instance Segmentation Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6f1346bac8b02f76a631400e2799b24b-Abstract-Conference.html) · 📚 被引 4
- **作者**: Zhixiong Nan, Xianghong Li, Tao Xiang, Jifeng Dai
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: NeurIPS 2024

### Fetch and Forge: Efficient Dataset Condensation for Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d7b351608d824a4680344a02b180a947-Abstract-Conference.html) · 📚 被引 2
- **作者**: Ding Qi, Jian Li, Jinlong Peng, Bo Zhao, Shuguang Dou, Jialin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Amnesia as a Catalyst for Enhancing Black Box Pixel Attacks in Image Classification and Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/9e770fcdb456400325c11d58b3a04d08-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dongsu Song, Daehwa Ko, Jay Hoon Jung
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### YOLOv10: Real-Time End-to-End Object Detection.
- **链接**: [arXiv:2405.14458](https://arxiv.org/abs/2405.14458) · 📚 被引 1603
- **作者**: Ao Wang, Hui Chen, Lihao Liu, Kai Chen, Zijia Lin, Jungong Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Over the past years, YOLOs have emerged as the predominant paradigm in the field of real-time object detection owing to their effective balance between computational cost and detection performance. Researchers have explored the architectural designs, optimization objectives, data augmentation strategies, and others for YOLOs, achieving notable progress. However, the reliance on the non-maximum suppression (NMS) for post-processing hampers the end-to-end deployment of YOLOs and adversely impacts the inference latency. Besides, the design of various components in YOLOs lacks the comprehensive and thorough inspection, resulting in noticeable computational redundancy and limiting the model's capability. It renders the suboptimal efficiency, along with considerable potential for performance improvements. In this work, we aim to further advance the performance-efficiency boundary of YOLOs from both the post-processing and model architecture. To this end, we first present the consistent dual assignments for NMS-free training of YOLOs, which brings competitive performance and low inference latency simultaneously. Moreover, we introduce the holistic efficiency-accuracy driven model design strategy for YOLOs. We comprehensively optimize various components of YOLOs from both efficiency and accuracy perspectives, which greatly reduces the computational overhead and enhances the capability. The outcome of our effort is a new generation of YOLO series for real-time end-to-end object detection, dubbed YOLOv10. Extensive experiments show that YOLOv10 achieves state-of-the-art performance and efficiency across various model scales. For example, our YOLOv10-S is 1.8$\times$ faster than RT-DETR-R18 under the similar AP on COCO, meanwhile enjoying 2.8$\times$ smaller number of parameters and FLOPs. Compared with YOLOv9-C, YOLOv10-B has 46\% less latency and 25\% fewer parameters for the same performance.

</details>

### Adaptive Important Region Selection with Reinforced Hierarchical Search for Dense Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/510950c4e75d8bbe430dbe01c8ad2426-Abstract-Conference.html) · 📚 被引 2
- **作者**: Dingrong Wang, Hitesh Sapkota, Qi Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### AdaptiveISP: Learning an Adaptive Image Signal Processor for Object Detection.
- **链接**: [arXiv:2410.22939](https://arxiv.org/abs/2410.22939) · 📚 被引 6
- **作者**: Yujin Wang, Tianyi Xu, Zhang Fan, Tianfan Xue, Jinwei Gu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image Signal Processors (ISPs) convert raw sensor signals into digital images, which significantly influence the image quality and the performance of downstream computer vision tasks. Designing ISP pipeline and tuning ISP parameters are two key steps for building an imaging and vision system. To find optimal ISP configurations, recent works use deep neural networks as a proxy to search for ISP parameters or ISP pipelines. However, these methods are primarily designed to maximize the image quality, which are sub-optimal in the performance of high-level computer vision tasks such as detection, recognition, and tracking. Moreover, after training, the learned ISP pipelines are mostly fixed at the inference time, whose performance degrades in dynamic scenes. To jointly optimize ISP structures and parameters, we propose AdaptiveISP, a task-driven and scene-adaptive ISP. One key observation is that for the majority of input images, only a few processing modules are needed to improve the performance of downstream recognition tasks, and only a few inputs require more processing. Based on this, AdaptiveISP utilizes deep reinforcement learning to automatically generate an optimal ISP pipeline and the associated ISP parameters to maximize the detection performance. Experimental results show that AdaptiveISP not only surpasses the prior state-of-the-art methods for object detection but also dynamically manages the trade-off between detection performance and computational cost, especially suitable for scenes with large dynamic range variations. Project website: https://openimaginglab.github.io/AdaptiveISP/.

</details>

### EGSST: Event-based Graph Spatiotemporal Sensitive Transformer for Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/da733d44e4be3902d952d6c1ffcb7db6-Abstract-Conference.html) · 📚 被引 1
- **作者**: Sheng Wu, Hang Sheng, Hui Feng, Bo Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### UMB: Understanding Model Behavior for Open-World Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8766fbc68e1ed1cdef712ce273e0a363-Abstract-Conference.html)
- **作者**: Xing Xi, Yangyang Huang, Zhijie Zhong, Ronghua Luo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Towards Unsupervised Model Selection for Domain Adaptive Object Detection.
- **链接**: [arXiv:2412.17284](https://arxiv.org/abs/2412.17284) · 📚 被引 0
- **作者**: Hengfu Yu, Jinhong Deng, Wen Li, Lixin Duan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Evaluating the performance of deep models in new scenarios has drawn increasing attention in recent years. However, while it is possible to collect data from new scenarios, the annotations are not always available. Existing DAOD methods often rely on validation or test sets on the target domain for model selection, which is impractical in real-world applications. In this paper, we propose a novel unsupervised model selection approach for domain adaptive object detection, which is able to select almost the optimal model for the target domain without using any target labels. Our approach is based on the flat minima principle, i,e., models located in the flat minima region in the parameter space usually exhibit excellent generalization ability. However, traditional methods require labeled data to evaluate how well a model is located in the flat minima region, which is unrealistic for the DAOD task. Therefore, we design a Detection Adaptation Score (DAS) approach to approximately measure the flat minima without using target labels. We show via a generalization bound that the flatness can be deemed as model variance, while the minima depend on the domain distribution distance for the DAOD task. Accordingly, we propose a Flatness Index Score (FIS) to assess the flatness by measuring the classification and localization fluctuation before and after perturbations of model parameters and a Prototypical Distance Ratio (PDR) score to seek the minima by measuring the transferability and discriminability of the models. In this way, the proposed DAS approach can effectively evaluate the model generalization ability on the target domain. We have conducted extensive experiments on various DAOD benchmarks and approaches, and the experimental results show that the proposed DAS correlates well with the performance of DAOD models and can be used as an effective tool for model selection after training.

</details>

### ODGEN: Domain-specific Object Detection Data Generation with Diffusion Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/743771397cef2aa0ef497c428c3a46b7-Abstract-Conference.html) · 📚 被引 4
- **作者**: Jingyuan Zhu, Shiyu Li, Yuxuan Liu, Jian Yuan, Ping Huang, Jiulong Shan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- UNION: Unsupervised 3D Object Detection using Object Appearance-based Pseudo-Classes. → [3d-detection](../3d-detection/Guideline%202024.md)
- Towards Flexible 3D Perception: Object-Centric Occupancy Completion Augments 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- LION: Linear Group RNN for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202024.md)
- Unified Domain Generalization and Adaptation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- DiffuBox: Refining 3D Object Detection with Point Diffusion. → [3d-detection](../3d-detection/Guideline%202024.md)
- Zero-shot Generalizable Incremental Learning for Vision-Language Object Detection. → [continual-learning](../continual-learning/Guideline%202024.md)
- CRT-Fusion: Camera, Radar, Temporal Fusion Using Motion Information for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Real-time Stereo-based 3D Object Detection for Streaming Perception. → [3d-detection](../3d-detection/Guideline%202024.md)
- 3DET-Mamba: Causal Sequence Modelling for End-to-End 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- STONE: A Submodular Optimization Framework for Active 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- One for All: Multi-Domain Joint Training for Point Cloud Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- MVSDet: Multi-View Indoor 3D Object Detection via Efficient Plane Sweeps. → [3d-detection](../3d-detection/Guideline%202024.md)
- ImOV3D: Learning Open Vocabulary Point Clouds 3D Object Detection from Only 2D Images. → [3d-detection](../3d-detection/Guideline%202024.md)
- Voxel Mamba: Group-Free State Space Models for Point Cloud based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- RETR: Multi-View Radar Detection Transformer for Indoor Perception. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
