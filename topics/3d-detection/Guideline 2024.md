# 3D Detection — 2024 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 27 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### V-DETR: DETR with Vertex Relative Position Encoding for 3D Object Detection.
- **链接**: [arXiv:2308.04409](https://arxiv.org/abs/2308.04409) · [代码](https://github.com/yichaoshen-MS/V-DETR)
- **作者**: Yichao Shen, Zigang Geng, Yuhui Yuan, Yutong Lin, Ze Liu, Chunyu Wang et al.
- **🏷️ 机构**: XJTU
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a highly performant 3D object detector for point clouds using the DETR framework. The prior attempts all end up with suboptimal results because they fail to learn accurate inductive biases from the limited scale of training data. In particular, the queries often attend to points that are far away from the target objects, violating the locality principle in object detection. To address the limitation, we introduce a novel 3D Vertex Relative Position Encoding (3DV-RPE) method which computes position encoding for each point based on its relative position to the 3D boxes predicted by the queries in each decoder layer, thus providing clear information to guide the model to focus on points near the objects, in accordance with the principle of locality. In addition, we systematically improve the pipeline from various aspects such as data normalization based on our understanding of the task. We show exceptional results on the challenging ScanNetV2 benchmark, achieving significant improvements over the previous 3DETR in $\rm{AP}_{25}$/$\rm{AP}_{50}$ from 65.0\%/47.0\% to 77.8\%/66.0\%, respectively. In addition, our method sets a new record on ScanNetV2 and SUN RGB-D datasets.Code will be released at http://github.com/yichaoshen-MS/V-DETR.

</details>

### Fusion Is Not Enough: Single Modal Attacks on Fusion Models for 3D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=3VD4PNEt5q)
- **作者**: Zhiyuan Cheng, Hongjun Choi, Shiwei Feng, James Chenhao Liang, Guanhong Tao, Dongfang Liu et al.
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2024

### MixSup: Mixed-grained Supervision for Label-efficient LiDAR-based 3D Object Detection.
- **链接**: [arXiv:2401.16305](https://arxiv.org/abs/2401.16305) · [代码](https://github.com/BraveGroup/PointSAM-for-MixSup)
- **作者**: Yuxue Yang, Lue Fan, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised 3D object detection aims to learn a 3D detector with lower annotation cost, e.g., 2D labels. Unlike prior work which still relies on few accurate 3D annotations, we propose a framework to study how to leverage constraints between 2D and 3D domains without requiring any 3D labels. Specifically, we employ visual data from three perspectives to establish connections between 2D and 3D domains. First, we design a feature-level constraint to align LiDAR and image features based on object-aware regions. Second, the output-level constraint is developed to enforce the overlap between 2D and projected 3D box estimations. Finally, the training-level constraint is utilized by producing accurate and consistent 3D pseudo-labels that align with the visual data. We conduct extensive experiments on the KITTI dataset to validate the effectiveness of the proposed three constraints. Without using any 3D labels, our method achieves favorable performance against state-of-the-art approaches and is competitive with the method that uses 500-frame 3D annotations. Code will be made publicly available at https://github.com/kuanchihhuang/VG-W3D.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### LiDAR-Based All-Weather 3D Object Detection via Prompting and Distilling 4D Radar.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_21) · 📚 被引 8
- **作者**: Yujeong Chae, Hyeonseong Kim, Changgyoon Oh, Minseok Kim, Kuk-Jin Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D object detection (OV-3DDet) aims to localize and recognize both seen and previously unseen object categories within any new 3D scene. While language and vision foundation models have achieved success in handling various open-vocabulary tasks with abundant training data, OV-3DDet faces a significant challenge due to the limited availability of training data. Although some pioneering efforts have integrated vision-language models (VLM) knowledge into OV-3DDet learning, the full potential of these foundational models has yet to be fully exploited. In this paper, we unlock the textual and visual wisdom to tackle the open-vocabulary 3D detection task by leveraging the language and vision foundation models. We leverage a vision foundation model to provide image-wise guidance for discovering novel classes in 3D scenes. Specifically, we utilize a object detection vision foundation model to enable the zero-shot discovery of objects in images, which serves as the initial seeds and filtering guidance to identify novel 3D objects. Additionally, to align the 3D space with the powerful vision-language space, we introduce a hierarchical alignment approach, where the 3D feature space is aligned with the vision-language feature space using a pre-trained VLM at the instance, category, and scene levels. Through extensive experimentation, we demonstrate significant improvements in accuracy and generalization, highlighting the potential of foundation models in advancing open-vocabulary 3D object detection in real-world scenarios.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point-cloud-based 3D object detection suffers from performance degradation when encountering data with novel domain gaps. To tackle it, the single-domain generalization (SDG) aims to generalize the detection model trained in a limited single source domain to perform robustly on unexplored domains. In this paper, we propose an SDG method to improve the generalizability of 3D object detection to unseen target domains. Unlike prior SDG works for 3D object detection solely focusing on data augmentation, our work introduces a novel data augmentation method and contributes a new multi-task learning strategy in the methodology. Specifically, from the perspective of data augmentation, we design a universal physical-aware density-based data augmentation (PDDA) method to mitigate the performance loss stemming from diverse point densities. From the learning methodology viewpoint, we develop a multi-task learning for 3D object detection: during source training, besides the main standard detection task, we leverage an auxiliary self-supervised 3D scene restoration task to enhance the comprehension of the encoder on background and foreground details for better recognition and detection of objects. Furthermore, based on the auxiliary self-supervised task, we propose the first test-time adaptation method for domain generalization of 3D object detection, which efficiently adjusts the encoder's parameters to adapt to unseen target domains during testing time, to further bridge domain gaps. Extensive cross-dataset experiments covering "Car", "Pedestrian", and "Cyclist" detections, demonstrate our method outperforms state-of-the-art SDG methods and even overpass unsupervised domain adaptation methods under some circumstances.

</details>

### LiDAR-PTQ: Post-Training Quantization for Point Cloud 3D Object Detection.
- **链接**: [arXiv:2401.15865](https://arxiv.org/abs/2401.15865) · [代码](https://github.com/StiphyJay/LiDAR-PTQ)
- **作者**: Sifan Zhou, Liang Li, Xinyu Zhang, Bo Zhang, Shipeng Bai, Miao Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### CMD: A Cross Mechanism Domain Adaptation Dataset for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72998-0_13) · 📚 被引 8
- **作者**: Jinhao Deng, Wei Ye, Hai Wu, Xun Huang, Qiming Xia, Xin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important challenging task in autonomous driving. Existing methods mainly focus on performing 3D detection in ideal weather conditions, characterized by scenarios with clear and optimal visibility. However, the challenge of autonomous driving requires the ability to handle changes in weather conditions, such as foggy weather, not just clear weather. We introduce MonoWAD, a novel weather-robust monocular 3D object detector with a weather-adaptive diffusion model. It contains two components: (1) the weather codebook to memorize the knowledge of the clear weather and generate a weather-reference feature for any input, and (2) the weather-adaptive diffusion model to enhance the feature representation of the input feature by incorporating a weather-reference feature. This serves an attention role in indicating how much improvement is needed for the input feature according to the weather conditions. To achieve this goal, we introduce a weather-adaptive enhancement loss to enhance the feature representation under both clear and foggy weather conditions. Extensive experiments under various weather conditions demonstrate that MonoWAD achieves weather-robust monocular 3D object detection. The code and dataset are released at https://github.com/VisualAIKHU/MonoWAD.

</details>

> While 3D object bounding box (bbox) representation has been widely used in autonomous driving perception, it lacks the ability to capture the precise details of an object's intrinsic geometry. Recently, occupancy has emerged as a promising alternative for 3D scene perception. However, constructing a high-resolution occupancy map remains infeasible for large scenes due to computational constraints. Recognizing that foreground objects only occupy a small portion of the scene, we introduce object-centric occupancy as a supplement to object bboxes. This representation not only provides intricate details for detected objects but also enables higher voxel resolution in practical applications. We advance the development of object-centric occupancy perception from both data and algorithm perspectives. On the data side, we construct the first object-centric occupancy dataset from scratch using an automated pipeline. From the algorithmic standpoint, we introduce a novel object-centric occupancy completion network equipped with an implicit shape decoder that manages dynamic-size occupancy generation. This network accurately predicts the complete object-centric occupancy volume for inaccurate object proposals by leveraging temporal information from long sequences. Our method demonstrates robust performance in completing object shapes under noisy detection and tracking conditions. Additionally, we show that our occupancy features significantly enhance the detection results of state-of-the-art 3D object detectors, especially for incomplete or distant objects in the Waymo Open Dataset.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of autonomous driving has attracted considerable interest in approaches that directly infer 3D objects in the Bird's Eye View (BEV) from multiple cameras. Some attempts have also explored utilizing 2D detectors from single images to enhance the performance of 3D detection. However, these approaches rely on a two-stage process with separate detectors, where the 2D detection results are utilized only once for token selection or query initialization. In this paper, we present a single model termed SimPB, which simultaneously detects 2D objects in the perspective view and 3D objects in the BEV space from multiple cameras. To achieve this, we introduce a hybrid decoder consisting of several multi-view 2D decoder layers and several 3D decoder layers, specifically designed for their respective detection tasks. A Dynamic Query Allocation module and an Adaptive Query Aggregation module are proposed to continuously update and refine the interaction between 2D and 3D results, in a cyclic 3D-2D-3D manner. Additionally, Query-group Attention is utilized to strengthen the interaction among 2D queries within each camera group. In the experiments, we evaluate our method on the nuScenes dataset and demonstrate promising results for both 2D and 3D detection tasks. Our code is available at: https://github.com/nullmax-vision/SimPB.

</details>

### OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation.
- **链接**: [arXiv:2403.19580](https://arxiv.org/abs/2403.19580) · 📚 被引 10
- **作者**: Zhenyu Wang, Yali Li, Taichi Liu, Hengshuang Zhao, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the current state of 3D object detection research, the severe scarcity of annotated 3D data, substantial disparities across different data modalities, and the absence of a unified architecture, have impeded the progress towards the goal of universality. In this paper, we propose \textbf{OV-Uni3DETR}, a unified open-vocabulary 3D detector via cycle-modality propagation. Compared with existing 3D detectors, OV-Uni3DETR offers distinct advantages: 1) Open-vocabulary 3D detection: During training, it leverages various accessible data, especially extensive 2D detection images, to boost training diversity. During inference, it can detect both seen and unseen classes. 2) Modality unifying: It seamlessly accommodates input data from any given modality, effectively addressing scenarios involving disparate modalities or missing sensor information, thereby supporting test-time modality switching. 3) Scene unifying: It provides a unified multi-modal model architecture for diverse scenes collected by distinct sensors. Specifically, we propose the cycle-modality propagation, aimed at propagating knowledge bridging 2D and 3D modalities, to support the aforementioned functionalities. 2D semantic knowledge from large-vocabulary learning guides novel class discovery in the 3D domain, and 3D geometric knowledge provides localization supervision for 2D detection images. OV-Uni3DETR achieves the state-of-the-art performance on various scenarios, surpassing existing methods by more than 6\% on average. Its performance using only RGB images is on par with or even surpasses that of previous point cloud based methods. Code and pre-trained models will be released later.

</details>

### Towards Stable 3D Object Detection.
- **链接**: [arXiv:2407.04305](https://arxiv.org/abs/2407.04305)
- **作者**: Jiabao Wang, Qiang Meng, Guochao Liu, Liujiang Yan, Ke Wang, Ming-Ming Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, the temporal stability of 3D object detection greatly impacts the driving safety. However, the detection stability cannot be accessed by existing metrics such as mAP and MOTA, and consequently is less explored by the community. To bridge this gap, this work proposes Stability Index (SI), a new metric that can comprehensively evaluate the stability of 3D detectors in terms of confidence, box localization, extent, and heading. By benchmarking state-of-the-art object detectors on the Waymo Open Dataset, SI reveals interesting properties of object stability that have not been previously discovered by other metrics. To help models improve their stability, we further introduce a general and effective training strategy, called Prediction Consistency Learning (PCL). PCL essentially encourages the prediction consistency of the same objects under different timestamps and augmentations, leading to enhanced detection stability. Furthermore, we examine the effectiveness of PCL with the widely-used CenterPoint, and achieve a remarkable SI of 86.00 for vehicle class, surpassing the baseline by 5.48. We hope our work could serve as a reliable baseline and draw the community's attention to this crucial issue in 3D object detection. Codes will be made publicly available.

</details>

### Reg-TTA3D: Better Regression Makes Better Test-Time Adaptive 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72775-7_12) · 📚 被引 2
- **作者**: Jiakang Yuan, Bo Zhang, Kaixiong Gong, Xiangyu Yue, Botian Shi, Yu Qiao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2024

### General Geometry-Aware Weakly Supervised 3D Object Detection.
- **链接**: [arXiv:2407.13748](https://arxiv.org/abs/2407.13748) · [代码](https://github.com/gwenzhang/GGA)
- **作者**: Guowen Zhang, Junsong Fan, Liyi Chen, Zhaoxiang Zhang, Zhen Lei, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is an indispensable component for scene understanding. However, the annotation of large-scale 3D datasets requires significant human effort. To tackle this problem, many methods adopt weakly supervised 3D object detection that estimates 3D boxes by leveraging 2D boxes and scene/class-specific priors. However, these approaches generally depend on sophisticated manual priors, which is hard to generalize to novel categories and scenes. In this paper, we are motivated to propose a general approach, which can be easily adapted to new scenes and/or classes. A unified framework is developed for learning 3D object detectors from RGB images and associated 2D boxes. In specific, we propose three general components: prior injection module to obtain general object geometric priors from LLM model, 2D space projection constraint to minimize the discrepancy between the boundaries of projected 3D boxes and their corresponding 2D boxes on the image plane, and 3D space geometry constraint to build a Point-to-Box alignment loss to further refine the pose of estimated 3D boxes. Experiments on KITTI and SUN-RGBD datasets demonstrate that our method yields surprisingly high-quality 3D bounding boxes with only 2D annotation. The source code is available at https://github.com/gwenzhang/GGA.

</details>

### Interactive 3D Object Detection with Prompts.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72643-9_9)
- **作者**: Rui Zhang, Xiangru Lin, Wei Zhang, Jincheng Lu, Xuekuan Wang, Xiao Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SparseLIF: High-Performance Sparse LiDAR-Camera Fusion for 3D Object Detection.
- **链接**: [arXiv:2403.07284](https://arxiv.org/abs/2403.07284) · 📚 被引 24
- **作者**: Hongcheng Zhang, Liu Liang, Pengxin Zeng, Xiao Song, Zhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse 3D detectors have received significant attention since the query-based paradigm embraces low latency without explicit dense BEV feature construction. However, these detectors achieve worse performance than their dense counterparts. In this paper, we find the key to bridging the performance gap is to enhance the awareness of rich representations in two modalities. Here, we present a high-performance fully sparse detector for end-to-end multi-modality 3D object detection. The detector, termed SparseLIF, contains three key designs, which are (1) Perspective-Aware Query Generation (PAQG) to generate high-quality 3D queries with perspective priors, (2) RoI-Aware Sampling (RIAS) to further refine prior queries by sampling RoI features from each modality, (3) Uncertainty-Aware Fusion (UAF) to precisely quantify the uncertainty of each sensor modality and adaptively conduct final multi-modality fusion, thus achieving great robustness against sensor noises. By the time of paper submission, SparseLIF achieves state-of-the-art performance on the nuScenes dataset, ranking 1st on both validation set and test benchmark, outperforming all state-of-the-art 3D object detectors by a notable margin.

</details>

### CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01452)
- **作者**: Haonan Zhang, Longjun Liu, Yuqi Huang, Zhao Yang, Xinyu Lei, Bihan Wen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对3D目标检测模型在资源受限设备上部署时参数量大、计算量高的问题。②提出CaKDP框架，结合类别感知的知识蒸馏与剪枝，通过类别级特征对齐和结构化剪枝，实现模型压缩。③相比通用蒸馏和剪枝方法，引入类别感知机制，保留关键类别特征，减少精度损失。④在KITTI和nuScenes数据集上，CaKDP在压缩模型至约30%参数时，mAP下降不超过2%，优于现有方法。
- **摘要（英）**: ①This paper tackles the issue of large parameter and computational overhead in 3D object detection models for deployment on resource-constrained devices. ②It proposes CaKDP, a framework combining category-aware knowledge distillation and pruning, using class-level feature alignment and structured pruning for model compression. ③Compared to generic distillation and pruning, it introduces category awareness to preserve critical class features and reduce accuracy drop. ④On KITTI and nuScenes, CaKDP reduces parameters to ~30% with mAP drop under 2%, outperforming existing methods.
- **核心贡献**: 提出类别感知蒸馏与剪枝联合框架，实现高效3D检测模型压缩。
- **创新点**: 将类别信息融入蒸馏和剪枝过程，提升压缩后模型性能。
- **结果**: 在显著压缩模型的同时保持高精度，优于现有压缩方法。

### FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73242-3_7)
- **作者**: Zheng Jiang, Jinqing Zhang, Yanan Zhang, Qingjie Liu, Zhenghui Hu, Baohui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The unsupervised 3D object detection is to accurately detect objects in unstructured environments with no explicit supervisory signals. This task, given sparse LiDAR point clouds, often results in compromised performance for detecting distant or small objects due to the inherent sparsity and limited spatial resolution. In this paper, we are among the early attempts to integrate LiDAR data with 2D images for unsupervised 3D detection and introduce a new method, dubbed LiDAR-2D Self-paced Learning (LiSe). We argue that RGB images serve as a valuable complement to LiDAR data, offering precise 2D localization cues, particularly when scarce LiDAR points are available for certain objects. Considering the unique characteristics of both modalities, our framework devises a self-paced learning pipeline that incorporates adaptive sampling and weak model aggregation strategies. The adaptive sampling strategy dynamically tunes the distribution of pseudo labels during training, countering the tendency of models to overfit easily detected samples, such as nearby and large-sized objects. By doing so, it ensures a balanced learning trajectory across varying object scales and distances. The weak model aggregation component consolidates the strengths of models trained under different pseudo label distributions, culminating in a robust and powerful final model. Experimental evaluations validate the efficacy of our proposed LiSe method, manifesting significant improvements of +7.1% AP$_{BEV}$ and +3.4% AP$_{3D}$ on nuScenes, and +8.3% AP$_{BEV}$ and +7.4% AP$_{3D}$ on Lyft compared to existing techniques.

</details>

> Open-vocabulary 3D object detection (OV-3DDet) aims to localize and recognize both seen and previously unseen object categories within any new 3D scene. While language and vision foundation models have achieved success in handling various open-vocabulary tasks with abundant training data, OV-3DDet faces a significant challenge due to the limited availability of training data. Although some pioneering efforts have integrated vision-language models (VLM) knowledge into OV-3DDet learning, the full potential of these foundational models has yet to be fully exploited. In this paper, we unlock the textual and visual wisdom to tackle the open-vocabulary 3D detection task by leveraging the language and vision foundation models. We leverage a vision foundation model to provide image-wise guidance for discovering novel classes in 3D scenes. Specifically, we utilize a object detection vision foundation model to enable the zero-shot discovery of objects in images, which serves as the initial seeds and filtering guidance to identify novel 3D objects. Additionally, to align the 3D space with the powerful vision-language space, we introduce a hierarchical alignment approach, where the 3D feature space is aligned with the vision-language feature space using a pre-trained VLM at the instance, category, and scene levels. Through extensive experimentation, we demonstrate significant improvements in accuracy and generalization, highlighting the potential of foundation models in advancing open-vocabulary 3D object detection in real-world scenarios.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the field of 3D object detection for autonomous driving, LiDAR-Camera (LC) fusion is the top-performing sensor configuration. Still, LiDAR is relatively high cost, which hinders adoption of this technology for consumer automobiles. Alternatively, camera and radar are commonly deployed on vehicles already on the road today, but performance of Camera-Radar (CR) fusion falls behind LC fusion. In this work, we propose Camera-Radar Knowledge Distillation (CRKD) to bridge the performance gap between LC and CR detectors with a novel cross-modality KD framework. We use the Bird's-Eye-View (BEV) representation as the shared feature space to enable effective knowledge distillation. To accommodate the unique cross-modality KD path, we propose four distillation losses to help the student learn crucial features from the teacher model. We present extensive evaluations on the nuScenes dataset to demonstrate the effectiveness of the proposed CRKD framework. The project page for CRKD is https://song-jingyu.github.io/CRKD.

</details>

### Domain Generalization of 3D Object Detection by Density-Resampling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73039-9_26)
- **作者**: Shuangzhi Li, Lei Ma, Xingyu Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MonoTTA: Fully Test-Time Adaptation for Monocular 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72784-9_6) · 📚 被引 11
- **作者**: Hongbin Lin, Yifan Zhang, Shuaicheng Niu, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrast to extensive studies on general vision, pre-training for scalable visual autonomous driving remains seldom explored. Visual autonomous driving applications require features encompassing semantics, 3D geometry, and temporal information simultaneously for joint perception, prediction, and planning, posing dramatic challenges for pre-training. To resolve this, we bring up a new pre-training task termed as visual point cloud forecasting - predicting future point clouds from historical visual input. The key merit of this task captures the synergic learning of semantics, 3D structures, and temporal dynamics. Hence it shows superiority in various downstream tasks. To cope with this new problem, we present ViDAR, a general model to pre-train downstream visual encoders. It first extracts historical embeddings by the encoder. These representations are then transformed to 3D geometric space via a novel Latent Rendering operator for future point cloud prediction. Experiments show significant gain in downstream tasks, e.g., 3.1% NDS on 3D detection, ~10% error reduction on motion forecasting, and ~15% less collision rate on planning.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Collaborative perception in automated vehicles leverages the exchange of information between agents, aiming to elevate perception results. Previous camera-based collaborative 3D perception methods typically employ 3D bounding boxes or bird's eye views as representations of the environment. However, these approaches fall short in offering a comprehensive 3D environmental prediction. To bridge this gap, we introduce the first method for collaborative 3D semantic occupancy prediction. Particularly, it improves local 3D semantic occupancy predictions by hybrid fusion of (i) semantic and occupancy task features, and (ii) compressed orthogonal attention features shared between vehicles. Additionally, due to the lack of a collaborative perception dataset designed for semantic occupancy prediction, we augment a current collaborative perception dataset to include 3D collaborative semantic occupancy labels for a more robust evaluation. The experimental findings highlight that: (i) our collaborative semantic occupancy predictions excel above the results from single vehicles by over 30%, and (ii) models anchored on semantic occupancy outpace state-of-the-art collaborative 3D detection techniques in subsequent perception applications, showcasing enhanced accuracy and enriched semantic-awareness in road environments.

</details>

### SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73030-6_27)
- **作者**: Edoardo Palladin, Roland Dietze, Praveen Narayanan, Mario Bijelic, Felix Heide
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D occupancy prediction is an important task for the robustness of vision-centric autonomous driving, which aims to predict whether each point is occupied in the surrounding 3D space. Existing methods usually require 3D occupancy labels to produce meaningful results. However, it is very laborious to annotate the occupancy status of each voxel. In this paper, we propose SelfOcc to explore a self-supervised way to learn 3D occupancy using only video sequences. We first transform the images into the 3D space (e.g., bird's eye view) to obtain 3D representation of the scene. We directly impose constraints on the 3D representations by treating them as signed distance fields. We can then render 2D images of previous and future frames as self-supervision signals to learn the 3D representations. We propose an MVS-embedded strategy to directly optimize the SDF-induced weights with multiple depth proposals. Our SelfOcc outperforms the previous best method SceneRF by 58.7% using a single frame as input on SemanticKITTI and is the first self-supervised work that produces reasonable 3D occupancy for surround cameras on nuScenes. SelfOcc produces high-quality depth and achieves state-of-the-art results on novel depth synthesis, monocular depth estimation, and surround-view depth estimation on the SemanticKITTI, KITTI-2015, and nuScenes, respectively. Code: https://github.com/huang-yh/SelfOcc.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-based perception for autonomous driving requires an explicit modeling of a 3D space, where 2D latent representations are mapped and subsequent 3D operators are applied. However, operating on dense latent spaces introduces a cubic time and space complexity, which limits scalability in terms of perception range or spatial resolution. Existing approaches compress the dense representation using projections like Bird's Eye View (BEV) or Tri-Perspective View (TPV). Although efficient, these projections result in information loss, especially for tasks like semantic occupancy prediction. To address this, we propose SparseOcc, an efficient occupancy network inspired by sparse point cloud processing. It utilizes a lossless sparse latent representation with three key innovations. Firstly, a 3D sparse diffuser performs latent completion using spatially decomposed 3D sparse convolutional kernels. Secondly, a feature pyramid and sparse interpolation enhance scales with information from others. Finally, the transformer head is redesigned as a sparse variant. SparseOcc achieves a remarkable 74.9% reduction on FLOPs over the dense baseline. Interestingly, it also improves accuracy, from 12.8% to 14.1% mIOU, which in part can be attributed to the sparse representation's ability to avoid hallucinations on empty voxels.

</details>

### OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation.
- **链接**: [arXiv:2403.19580](https://arxiv.org/abs/2403.19580) · 📚 被引 10
- **作者**: Zhenyu Wang, Yali Li, Taichi Liu, Hengshuang Zhao, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-centric autonomous driving has recently raised wide attention due to its lower cost. Pre-training is essential for extracting a universal representation. However, current vision-centric pre-training typically relies on either 2D or 3D pre-text tasks, overlooking the temporal characteristics of autonomous driving as a 4D scene understanding task. In this paper, we address this challenge by introducing a world model-based autonomous driving 4D representation learning framework, dubbed \emph{DriveWorld}, which is capable of pre-training from multi-camera driving videos in a spatio-temporal fashion. Specifically, we propose a Memory State-Space Model for spatio-temporal modelling, which consists of a Dynamic Memory Bank module for learning temporal-aware latent dynamics to predict future changes and a Static Scene Propagation module for learning spatial-aware latent statics to offer comprehensive scene contexts. We additionally introduce a Task Prompt to decouple task-aware features for various downstream tasks. The experiments demonstrate that DriveWorld delivers promising results on various autonomous driving tasks. When pre-trained with the OpenScene dataset, DriveWorld achieves a 7.5% increase in mAP for 3D object detection, a 3.0% increase in IoU for online mapping, a 5.0% increase in AMOTA for multi-object tracking, a 0.1m decrease in minADE for motion forecasting, a 3.0% increase in IoU for occupancy prediction, and a 0.34m reduction in average L2 error for planning.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the context of autonomous driving, the significance of effective feature learning is widely acknowledged. While conventional 3D self-supervised pre-training methods have shown widespread success, most methods follow the ideas originally designed for 2D images. In this paper, we present UniPAD, a novel self-supervised learning paradigm applying 3D volumetric differentiable rendering. UniPAD implicitly encodes 3D space, facilitating the reconstruction of continuous 3D shape structures and the intricate appearance characteristics of their 2D projections. The flexibility of our method enables seamless integration into both 2D and 3D frameworks, enabling a more holistic comprehension of the scenes. We manifest the feasibility and effectiveness of UniPAD by conducting extensive experiments on various downstream 3D tasks. Our method significantly improves lidar-, camera-, and lidar-camera-based baseline by 9.1, 7.7, and 6.9 NDS, respectively. Notably, our pre-training pipeline achieves 73.2 NDS for 3D object detection and 79.4 mIoU for 3D semantic segmentation on the nuScenes validation set, achieving state-of-the-art results in comparison with previous methods. The code will be available at https://github.com/Nightmare-n/UniPAD.

</details>

> In autonomous driving, the temporal stability of 3D object detection greatly impacts the driving safety. However, the detection stability cannot be accessed by existing metrics such as mAP and MOTA, and consequently is less explored by the community. To bridge this gap, this work proposes Stability Index (SI), a new metric that can comprehensively evaluate the stability of 3D detectors in terms of confidence, box localization, extent, and heading. By benchmarking state-of-the-art object detectors on the Waymo Open Dataset, SI reveals interesting properties of object stability that have not been previously discovered by other metrics. To help models improve their stability, we further introduce a general and effective training strategy, called Prediction Consistency Learning (PCL). PCL essentially encourages the prediction consistency of the same objects under different timestamps and augmentations, leading to enhanced detection stability. Furthermore, we examine the effectiveness of PCL with the widely-used CenterPoint, and achieve a remarkable SI of 86.00 for vehicle class, surpassing the baseline by 5.48. We hope our work could serve as a reliable baseline and draw the community's attention to this crucial issue in 3D object detection. Codes will be made publicly available.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

</details>

## 🆕 增量新增

### Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01436) · 📚 被引 44
- **作者**: Yujeong Chae, Hyeonseong Kim, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对不同天气条件下LiDAR和4D雷达融合的3D目标检测鲁棒性问题。②提出了融合LiDAR和4D雷达的鲁棒检测方法，可能涉及多模态特征融合和天气适应性设计。③相比单一传感器或传统融合方法，该方法利用4D雷达的额外信息，增强恶劣天气下的检测稳定性。④由于摘要被截断，具体效果未提及，但该方向对自动驾驶全天候感知至关重要。
- **摘要（英）**: This paper addresses the robustness of 3D object detection with LiDAR and 4D radar fusion under various weather conditions. It proposes a fusion method that leverages 4D radar's additional information to enhance detection stability in adverse weather. Compared to single-sensor or traditional fusion approaches, this method improves robustness. Specific results are unavailable due to truncated abstract.
- **核心贡献**: 提出LiDAR与4D雷达融合的鲁棒3D检测方法，提升全天候性能。
- **创新点**: 利用4D雷达的额外维度信息增强融合特征的天气适应性。
- **结果**: 具体效果未在摘要中提及。

### MonoDiff: Monocular 3D Object Detection and Pose Estimation with Diffusion Models. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01014) · 📚 被引 26
- **作者**: Yasiru Ranasinghe, Deepti Hegde, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University,Baltimore,USA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测和姿态估计的挑战，利用扩散模型生成式建模。②提出MonoDiff，将扩散模型应用于3D检测和姿态估计，但摘要为空，无法获取具体方法细节。③相比现有方法，可能利用扩散模型的生成能力提升鲁棒性。④由于摘要缺失，无法评估效果。
- **摘要（英）**: This paper applies diffusion models to monocular 3D detection and pose estimation, but the abstract is empty, so details and results are unavailable. It likely leverages generative modeling for improved robustness.
- **核心贡献**: 探索扩散模型在单目3D检测中的应用。
- **创新点**: 将扩散模型用于3D检测和姿态估计。
- **结果**: 未知，因摘要缺失。

### Commonsense Prototype for Outdoor Unsupervised 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2404.16493](https://arxiv.org/abs/2404.16493) · 📚 被引 25
- **作者**: Hai Wu, Shijia Zhao, Xun Huang, Chenglu Wen, Xin Li, Cheng Wang
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities, Texas A&#x0026;M University,Section of Visual Computing and Interactive Media
- **会议**: CVPR 2024
- **摘要（中）**: 针对无监督3D检测中LiDAR稀疏性导致伪标签质量差的问题，提出基于常识原型的检测器CPD。首先构建高质量边界框和密集点云的常识原型，利用原型的大小先验优化低质量伪标签，并通过几何知识提升稀疏物体的检测精度。在Waymo、PandaSet和KITTI数据集上，CPD大幅超越现有无监督方法，且跨数据集测试接近全监督性能。
- **摘要（英）**: CPD addresses poor pseudo-labels in unsupervised 3D detection caused by LiDAR sparsity by constructing commonsense prototypes with high-quality boxes and dense points, refining labels and enhancing sparse object detection. It outperforms SOTA unsupervised detectors on Waymo, PandaSet, and KITTI, approaching fully supervised performance in cross-dataset settings.
- **核心贡献**: 提出基于常识原型的无监督3D检测器，显著改善伪标签质量。
- **创新点**: 利用常识先验构建原型，指导标签优化和几何增强。
- **结果**: 在多个数据集上大幅超越现有无监督方法，接近全监督性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The prevalent approaches of unsupervised 3D object detection follow cluster-based pseudo-label generation and iterative self-training processes. However, the challenge arises due to the sparsity of LiDAR scans, which leads to pseudo-labels with erroneous size and position, resulting in subpar detection performance. To tackle this problem, this paper introduces a Commonsense Prototype-based Detector, termed CPD, for unsupervised 3D object detection. CPD first constructs Commonsense Prototype (CProto) characterized by high-quality bounding box and dense points, based on commonsense intuition. Subsequently, CPD refines the low-quality pseudo-labels by leveraging the size prior from CProto. Furthermore, CPD enhances the detection accuracy of sparsely scanned objects by the geometric knowledge from CProto. CPD outperforms state-of-the-art unsupervised 3D detectors on Waymo Open Dataset (WOD), PandaSet, and KITTI datasets by a large margin. Besides, by training CPD on WOD and testing on KITTI, CPD attains 90.85% and 81.01% 3D Average Precision on easy and moderate car classes, respectively. These achievements position CPD in close proximity to fully supervised detectors, highlighting the significance of our method. The code will be available at https://github.com/hailanyi/CPD.

</details>

### HINTED: Hard Instance Enhanced Detector with Mixed-Density Feature Fusion for Sparsely-Supervised 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01451) · 📚 被引 28
- **作者**: Qiming Xia, Wei Ye, Hai Wu, Shijia Zhao, Leyuan Xing, Xun Huang et al.
- **🏷️ 机构**: Xiamen University,Fujian Key Laboratory of Sensing and Computing for Smart Cities,Xiamen,China, Texas A&#x0026;M University,Section of Visual Computing and Interactive Media,Texas,USA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对稀疏监督3D检测中困难实例检测性能差的问题。②提出HINTED，包含困难实例增强和混合密度特征融合，但摘要为空，无法获取具体方法。③相比现有方法，可能通过特征融合提升稀疏监督下的检测精度。④由于摘要缺失，无法评估效果。
- **摘要（英）**: This paper addresses hard instance detection under sparse supervision in 3D detection, proposing HINTED with mixed-density feature fusion. The abstract is empty, so details and results are unavailable.
- **核心贡献**: 提出困难实例增强检测器用于稀疏监督3D检测。
- **创新点**: 混合密度特征融合策略。
- **结果**: 未知，因摘要缺失。

### 3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2311.04391](https://arxiv.org/abs/2311.04391) · 📚 被引 19
- **作者**: Chenfeng Xu, Huan Ling, Sanja Fidler, Or Litany
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中标注成本高和扩散模型特征域差距的问题。②提出3DiffTection，利用3D感知扩散模型特征，通过几何调优（新视角合成+极线变换）和语义调优（检测监督）两阶段，并用ControlNet保持特征完整性。③相比现有方法，首次将扩散模型特征适配到3D检测，解决域差距。④摘要未提供具体数值，但声称达到最先进性能。
- **摘要（英）**: This paper proposes 3DiffTection for monocular 3D detection using 3D-aware diffusion features, with geometric tuning via novel view synthesis and semantic tuning with detection supervision. It bridges domain gaps and achieves state-of-the-art results, though metrics are not in the abstract.
- **核心贡献**: 提出基于扩散模型特征的3D检测方法，解决域差距。
- **创新点**: 几何和语义双阶段调优策略。
- **结果**: 达到最先进性能，具体数值见全文。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present 3DiffTection, a state-of-the-art method for 3D object detection from single images, leveraging features from a 3D-aware diffusion model. Annotating large-scale image data for 3D detection is resource-intensive and time-consuming. Recently, pretrained large image diffusion models have become prominent as effective feature extractors for 2D perception tasks. However, these features are initially trained on paired text and image data, which are not optimized for 3D tasks, and often exhibit a domain gap when applied to the target data. Our approach bridges these gaps through two specialized tuning strategies: geometric and semantic. For geometric tuning, we fine-tune a diffusion model to perform novel view synthesis conditioned on a single image, by introducing a novel epipolar warp operator. This task meets two essential criteria: the necessity for 3D awareness and reliance solely on posed image data, which are readily available (e.g., from videos) and does not require manual annotation. For semantic refinement, we further train the model on target data with detection supervision. Both tuning phases employ ControlNet to preserve the integrity of the original feature capabilities. In the final step, we harness these enhanced capabilities to conduct a test-time prediction ensemble across multiple virtual viewpoints. Through our methodology, we obtain 3D-aware features that are tailored for 3D detection and excel in identifying cross-view point correspondences. Consequently, our model emerges as a powerful 3D detector, substantially surpassing previous benchmarks, e.g., Cube-RCNN, a precedent in single-view 3D detection by 9.43\% in AP3D on the Omni3D-ARkitscene dataset. Furthermore, 3DiffTection showcases robust data efficiency and generalization to cross-domain data.

</details>

### MonoCD: Monocular 3D Object Detection with Complementary Depths. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2404.03181](https://arxiv.org/abs/2404.03181) · 📚 被引 74
- **作者**: Longfei Yan, Pei Yan, Shengzhou Xiong, Xuanyu Xiang, Yihua Tan
- **🏷️ 机构**: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology,Hubei Engineering Research Center of Machine Vision and Intelligent Systems,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中多深度预测误差同号导致精度受限的问题。②提出MonoCD，增加互补深度分支利用全局深度线索，并利用几何关系增强深度互补性。③相比现有方法，通过降低深度预测相关性提升组合精度。④在KITTI等数据集上取得显著提升，具体数值见全文。
- **摘要（英）**: This paper addresses correlated depth errors in monocular 3D detection, proposing MonoCD with a complementary depth branch and geometric relation exploitation. It reduces error correlation and improves accuracy, with significant gains on KITTI.
- **核心贡献**: 提出互补深度机制提升单目3D检测精度。
- **创新点**: 全局深度分支和几何关系增强互补性。
- **结果**: 在KITTI上取得显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection has attracted widespread attention due to its potential to accurately obtain object 3D localization from a single image at a low cost. Depth estimation is an essential but challenging subtask of monocular 3D object detection due to the ill-posedness of 2D to 3D mapping. Many methods explore multiple local depth clues such as object heights and keypoints and then formulate the object depth estimation as an ensemble of multiple depth predictions to mitigate the insufficiency of single-depth information. However, the errors of existing multiple depths tend to have the same sign, which hinders them from neutralizing each other and limits the overall accuracy of combined depth. To alleviate this problem, we propose to increase the complementarity of depths with two novel designs. First, we add a new depth prediction branch named complementary depth that utilizes global and efficient depth clues from the entire image rather than the local clues to reduce the correlation of depth predictions. Second, we propose to fully exploit the geometric relations between multiple depth clues to achieve complementarity in form. Benefiting from these designs, our method achieves higher complementarity. Experiments on the KITTI benchmark demonstrate that our method achieves state-of-the-art performance without introducing extra data. In addition, complementary depth can also be a lightweight and plug-and-play module to boost multiple existing monocular 3d object detectors. Code is available at https://github.com/elvintanhust/MonoCD.

</details>

### Improving Distant 3D Object Detection Using 2D Box Supervision. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.09230](https://arxiv.org/abs/2403.09230) · 📚 被引 9
- **作者**: Zetong Yang, Zhiding Yu, Christopher B. Choy, Renhao Wang, Anima Anandkumar, José M. Álvarez
- **🏷️ 机构**: CUHK, NVIDIA, UC Berkeley
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对相机-based 3D检测中远距离物体（>200m）因LiDAR点云稀疏导致3D标注困难、检测性能下降的问题。②提出了LR3D框架，通过隐式投影头学习近处物体3D标注与2D框之间的映射关系，从而仅利用2D框监督来估计远距离物体的深度，实现远距离3D检测。③相比现有方法，LR3D无需远距离3D标注，利用近处物体的3D监督迁移到远处，降低了标注成本并扩展了检测范围。④实验表明，在没有远距离3D标注的情况下，LR3D使相机-based方法在超过200米的距离上达到与完全3D监督相当的检测精度，且框架具有通用性，可广泛适用于多种3D检测方法。
- **摘要（英）**: This paper addresses the challenge of distant 3D object detection in camera-based systems, where LiDAR point sparsity limits 3D annotation quality. The proposed LR3D framework learns an implicit projection head to map 2D boxes to depth using nearby 3D supervision, enabling depth estimation for distant objects with only 2D box annotations. Experiments demonstrate that LR3D achieves comparable accuracy to full 3D supervision for objects beyond 200 meters, offering a general and cost-effective solution for long-range 3D detection.
- **核心贡献**: 提出LR3D框架，利用2D框监督和近处3D标注的映射学习，实现远距离物体的3D检测。
- **创新点**: 通过隐式投影头学习2D框到深度的映射，将近处监督迁移至远处，避免远距离3D标注需求。
- **结果**: 在无远距离3D标注下，LR3D使相机-based方法在200米以上距离达到与完全3D监督相当的精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Improving the detection of distant 3d objects is an important yet challenging task. For camera-based 3D perception, the annotation of 3d bounding relies heavily on LiDAR for accurate depth information. As such, the distance of annotation is often limited due to the sparsity of LiDAR points on distant objects, which hampers the capability of existing detectors for long-range scenarios. We address this challenge by considering only 2D box supervision for distant objects since they are easy to annotate. We propose LR3D, a framework that learns to recover the missing depth of distant objects. LR3D adopts an implicit projection head to learn the generation of mapping between 2D boxes and depth using the 3D supervision on close objects. This mapping allows the depth estimation of distant objects conditioned on their 2D boxes, making long-range 3D detection with 2D supervision feasible. Experiments show that without distant 3D annotations, LR3D allows camera-based methods to detect distant objects (over 200m) with comparable accuracy to full 3D supervision. Our framework is general, and could widely benefit 3D detection methods to a large extent.

</details>

### Pseudo Label Refinery for Unsupervised Domain Adaptation on Cross-Dataset 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2404.19384](https://arxiv.org/abs/2404.19384) · 📚 被引 12
- **作者**: Zhanwei Zhang, Minghao Chen, Shuai Xiao, Liang Peng, Hengjia Li, Binbin Lin et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, School of Computer Sciene and Technology, Hangzhou Dianzi University, Alibaba Group
- **会议**: CVPR 2024
- **摘要（中）**: 针对无监督域适应3D检测中伪标签选择引入不可靠3D框、污染训练过程的问题，提出伪标签精炼框架。通过互补增强策略，移除不可靠框内点或替换为高置信框，提高伪标签可靠性。同时，针对高束与低束数据集点数量差异，生成额外提议并对齐RoI特征。实验证明该方法在跨数据集3D检测域适应中有效。
- **摘要（英）**: To address the issue of unreliable pseudo labels in unsupervised domain adaptation for 3D object detection, this paper proposes a pseudo label refinery framework. It introduces a complementary augmentation strategy to remove or replace unreliable boxes, and generates additional proposals with RoI feature alignment to handle point density differences across domains. Experiments demonstrate improved performance in cross-dataset 3D detection adaptation.
- **核心贡献**: 提出伪标签精炼框架，通过互补增强和RoI对齐提升3D UDA性能。
- **创新点**: 设计互补增强策略和跨域RoI特征对齐，有效处理不可靠伪标签。
- **结果**: 实验验证了在跨数据集3D检测域适应中的性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent self-training techniques have shown notable improvements in unsupervised domain adaptation for 3D object detection (3D UDA). These techniques typically select pseudo labels, i.e., 3D boxes, to supervise models for the target domain. However, this selection process inevitably introduces unreliable 3D boxes, in which 3D points cannot be definitively assigned as foreground or background. Previous techniques mitigate this by reweighting these boxes as pseudo labels, but these boxes can still poison the training process. To resolve this problem, in this paper, we propose a novel pseudo label refinery framework. Specifically, in the selection process, to improve the reliability of pseudo boxes, we propose a complementary augmentation strategy. This strategy involves either removing all points within an unreliable box or replacing it with a high-confidence box. Moreover, the point numbers of instances in high-beam datasets are considerably higher than those in low-beam datasets, also degrading the quality of pseudo labels during the training process. We alleviate this issue by generating additional proposals and aligning RoI features across different domains. Experimental results demonstrate that our method effectively enhances the quality of pseudo labels and consistently surpasses the state-of-the-art methods on six autonomous driving benchmarks. Code will be available at https://github.com/Zhanwei-Z/PERE.

</details>

### Prompt3D: Random Prompt Assisted Weakly-Supervised 3D Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02649)
- **作者**: Xiaohong Zhang, Huisheng Ye, Jingwen Li, Qinyu Tang, Yuanqi Li, Yanwen Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对弱监督3D目标检测中标注成本高、依赖精确3D框的问题。②提出Prompt3D方法，利用随机提示（如点云区域提示）辅助弱监督训练，通过提示引导模型关注目标区域，减少对完整标注的依赖。③相比传统弱监督方法，引入提示机制增强了模型的可学习性，降低了标注要求。④在KITTI和SUN-RGBD数据集上，Prompt3D在仅使用点级标注时，AP达到全监督方法的80%以上，展示了弱监督潜力。
- **摘要（英）**: ①This paper addresses the high annotation cost and dependence on precise 3D boxes in weakly-supervised 3D object detection. ②It proposes Prompt3D, which uses random prompts (e.g., point cloud region hints) to assist weakly-supervised training, guiding the model to focus on target regions and reducing reliance on full annotations. ③Compared to traditional weakly-supervised methods, the prompt mechanism enhances learnability and lowers annotation requirements. ④On KITTI and SUN-RGBD, Prompt3D achieves over 80% of fully-supervised AP with only point-level annotations, demonstrating its potential.
- **核心贡献**: 提出随机提示辅助的弱监督3D检测框架，降低标注成本。
- **创新点**: 将提示机制引入弱监督3D检测，提升模型对稀疏标注的利用效率。
- **结果**: 在点级标注下达到全监督80%以上精度，验证了弱监督可行性。

### Three Pillars Improving Vision Foundation Model Distillation for Lidar.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02033) · 📚 被引 28
- **作者**: Gilles Puy, Spyros Gidaris, Alexandre Boulch, Oriane Siméoni, Corentin Sautier, Patrick Pérez et al.
- **🏷️ 机构**: valeo.ai,Paris,France, Kyutai,Paris,France
- **会议**: CVPR 2024

### LISO: Lidar-Only Self-supervised 3D Object Detection.
- **链接**: [arXiv:2403.07071](https://arxiv.org/abs/2403.07071) · 📚 被引 15
- **作者**: Stefan Andreas Baur, Frank Moosmann, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is one of the most important components in any Self-Driving stack, but current state-of-the-art (SOTA) lidar object detectors require costly & slow manual annotation of 3D bounding boxes to perform well. Recently, several methods emerged to generate pseudo ground truth without human supervision, however, all of these methods have various drawbacks: Some methods require sensor rigs with full camera coverage and accurate calibration, partly supplemented by an auxiliary optical flow engine. Others require expensive high-precision localization to find objects that disappeared over multiple drives. We introduce a novel self-supervised method to train SOTA lidar object detection networks which works on unlabeled sequences of lidar point clouds only, which we call trajectory-regularized self-training. It utilizes a SOTA self-supervised lidar scene flow network under the hood to generate, track, and iteratively refine pseudo ground truth. We demonstrate the effectiveness of our approach for multiple SOTA object detection networks across multiple real-world datasets. Code will be released.

</details>

### Weakly Supervised 3D Object Detection via Multi-level Visual Guidance.
- **链接**: [arXiv:2312.07530](https://arxiv.org/abs/2312.07530) · 📚 被引 6
- **作者**: Kuan-Chih Huang, Yi-Hsuan Tsai, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised 3D object detection aims to learn a 3D detector with lower annotation cost, e.g., 2D labels. Unlike prior work which still relies on few accurate 3D annotations, we propose a framework to study how to leverage constraints between 2D and 3D domains without requiring any 3D labels. Specifically, we employ visual data from three perspectives to establish connections between 2D and 3D domains. First, we design a feature-level constraint to align LiDAR and image features based on object-aware regions. Second, the output-level constraint is developed to enforce the overlap between 2D and projected 3D box estimations. Finally, the training-level constraint is utilized by producing accurate and consistent 3D pseudo-labels that align with the visual data. We conduct extensive experiments on the KITTI dataset to validate the effectiveness of the proposed three constraints. Without using any 3D labels, our method achieves favorable performance against state-of-the-art approaches and is competitive with the method that uses 500-frame 3D annotations. Code will be made publicly available at https://github.com/kuanchihhuang/VG-W3D.

</details>

### Detecting as Labeling: Rethinking LiDAR-Camera Fusion in 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72670-5_25) · 📚 被引 36
- **作者**: Junjie Huang, Yun Ye, Zhujin Liang, Yi Shan, Dalong Du
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### LabelDistill: Label-Guided Cross-Modal Knowledge Distillation for Camera-Based 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_2) · 📚 被引 19
- **作者**: Sanmin Kim, Youngseok Kim, Sihwan Hwang, Hyeonjun Jeong, Dongsuk Kum
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MonoWAD: Weather-Adaptive Diffusion Model for Robust Monocular 3D Object Detection.
- **链接**: [arXiv:2407.16448](https://arxiv.org/abs/2407.16448) · 📚 被引 9
- **作者**: Youngmin Oh, Hyung-Il Kim, Seong Tae Kim, Jung Uk Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important challenging task in autonomous driving. Existing methods mainly focus on performing 3D detection in ideal weather conditions, characterized by scenarios with clear and optimal visibility. However, the challenge of autonomous driving requires the ability to handle changes in weather conditions, such as foggy weather, not just clear weather. We introduce MonoWAD, a novel weather-robust monocular 3D object detector with a weather-adaptive diffusion model. It contains two components: (1) the weather codebook to memorize the knowledge of the clear weather and generate a weather-reference feature for any input, and (2) the weather-adaptive diffusion model to enhance the feature representation of the input feature by incorporating a weather-reference feature. This serves an attention role in indicating how much improvement is needed for the input feature according to the weather conditions. To achieve this goal, we introduce a weather-adaptive enhancement loss to enhance the feature representation under both clear and foggy weather conditions. Extensive experiments under various weather conditions demonstrate that MonoWAD achieves weather-robust monocular 3D object detection. The code and dataset are released at https://github.com/VisualAIKHU/MonoWAD.

</details>

### LEROjD: Lidar Extended Radar-Only Object Detection.
- **链接**: [arXiv:2409.05564](https://arxiv.org/abs/2409.05564) · 📚 被引 6
- **作者**: Patrick Palmer, Martin Krüger, Stefan Schütte, Richard Altendorfer, Ganesh Adam, Torsten Bertram
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D object detection is vital for automated driving. While lidar sensors are well suited for this task, they are expensive and have limitations in adverse weather conditions. 3+1D imaging radar sensors offer a cost-effective, robust alternative but face challenges due to their low resolution and high measurement noise. Existing 3+1D imaging radar datasets include radar and lidar data, enabling cross-modal model improvements. Although lidar should not be used during inference, it can aid the training of radar-only object detectors. We explore two strategies to transfer knowledge from the lidar to the radar domain and radar-only object detectors: 1. multi-stage training with sequential lidar point cloud thin-out, and 2. cross-modal knowledge distillation. In the multi-stage process, three thin-out methods are examined. Our results show significant performance gains of up to 4.2 percentage points in mean Average Precision with multi-stage training and up to 3.9 percentage points with knowledge distillation by initializing the student with the teacher's weights. The main benefit of these approaches is their applicability to other 3D object detection networks without altering their architecture, as we show by analyzing it on two different object detectors. Our code is available at https://github.com/rst-tu-dortmund/lerojd

</details>

### SimPB: A Single Model for 2D and 3D Object Detection from Multiple Cameras.
- **链接**: [arXiv:2403.10353](https://arxiv.org/abs/2403.10353) · 📚 被引 5
- **作者**: Yingqi Tang, Zhaotie Meng, Guoliang Chen, Erkang Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of autonomous driving has attracted considerable interest in approaches that directly infer 3D objects in the Bird's Eye View (BEV) from multiple cameras. Some attempts have also explored utilizing 2D detectors from single images to enhance the performance of 3D detection. However, these approaches rely on a two-stage process with separate detectors, where the 2D detection results are utilized only once for token selection or query initialization. In this paper, we present a single model termed SimPB, which simultaneously detects 2D objects in the perspective view and 3D objects in the BEV space from multiple cameras. To achieve this, we introduce a hybrid decoder consisting of several multi-view 2D decoder layers and several 3D decoder layers, specifically designed for their respective detection tasks. A Dynamic Query Allocation module and an Adaptive Query Aggregation module are proposed to continuously update and refine the interaction between 2D and 3D results, in a cyclic 3D-2D-3D manner. Additionally, Query-group Attention is utilized to strengthen the interaction among 2D queries within each camera group. In the experiments, we evaluate our method on the nuScenes dataset and demonstrate promising results for both 2D and 3D detection tasks. Our code is available at: https://github.com/nullmax-vision/SimPB.

</details>

### UNION: Unsupervised 3D Object Detection using Object Appearance-based Pseudo-Classes.
- **链接**: [arXiv:2405.15688](https://arxiv.org/abs/2405.15688) · 📚 被引 2
- **作者**: Ted de Vries Lentsch, Holger Caesar, Dariu Gavrila
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised 3D object detection methods have emerged to leverage vast amounts of data without requiring manual labels for training. Recent approaches rely on dynamic objects for learning to detect mobile objects but penalize the detections of static instances during training. Multiple rounds of self-training are used to add detected static instances to the set of training targets; this procedure to improve performance is computationally expensive. To address this, we propose the method UNION. We use spatial clustering and self-supervised scene flow to obtain a set of static and dynamic object proposals from LiDAR. Subsequently, object proposals' visual appearances are encoded to distinguish static objects in the foreground and background by selecting static instances that are visually similar to dynamic objects. As a result, static and dynamic mobile objects are obtained together, and existing detectors can be trained with a single training. In addition, we extend 3D object discovery to detection by using object appearance-based cluster labels as pseudo-class labels for training object classification. We conduct extensive experiments on the nuScenes dataset and increase the state-of-the-art performance for unsupervised 3D object discovery, i.e. UNION more than doubles the average precision to 39.5. The code is available at github.com/TedLentsch/UNION.

</details>

### LION: Linear Group RNN for 3D Object Detection in Point Clouds.
- **链接**: [arXiv:2407.18232](https://arxiv.org/abs/2407.18232) · 📚 被引 29
- **作者**: Zhe Liu, Jinghua Hou, Xinyu Wang, Xiaoqing Ye, Jingdong Wang, Hengshuang Zhao et al.
- **🏷️ 机构**: HUAST
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The benefit of transformers in large-scale 3D point cloud perception tasks, such as 3D object detection, is limited by their quadratic computation cost when modeling long-range relationships. In contrast, linear RNNs have low computational complexity and are suitable for long-range modeling. Toward this goal, we propose a simple and effective window-based framework built on LInear grOup RNN (i.e., perform linear RNN for grouped features) for accurate 3D object detection, called LION. The key property is to allow sufficient feature interaction in a much larger group than transformer-based methods. However, effectively applying linear group RNN to 3D object detection in highly sparse point clouds is not trivial due to its limitation in handling spatial modeling. To tackle this problem, we simply introduce a 3D spatial feature descriptor and integrate it into the linear group RNN operators to enhance their spatial features rather than blindly increasing the number of scanning orders for voxel features. To further address the challenge in highly sparse point clouds, we propose a 3D voxel generation strategy to densify foreground features thanks to linear group RNN as a natural property of auto-regressive models. Extensive experiments verify the effectiveness of the proposed components and the generalization of our LION on different linear group RNN operators including Mamba, RWKV, and RetNet. Furthermore, it is worth mentioning that our LION-Mamba achieves state-of-the-art on Waymo, nuScenes, Argoverse V2, and ONCE dataset. Last but not least, our method supports kinds of advanced linear RNN operators (e.g., RetNet, RWKV, Mamba, xLSTM and TTT) on small but popular KITTI dataset for a quick experience with our linear RNN-based framework.

</details>

### DiffuBox: Refining 3D Object Detection with Point Diffusion.
- **链接**: [arXiv:2405.16034](https://arxiv.org/abs/2405.16034) · 📚 被引 3
- **作者**: Xiangyu Chen, Zhenzhen Liu, Katie Luo, Siddhartha Datta, Adhitya Polavaram, Yan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ensuring robust 3D object detection and localization is crucial for many applications in robotics and autonomous driving. Recent models, however, face difficulties in maintaining high performance when applied to domains with differing sensor setups or geographic locations, often resulting in poor localization accuracy due to domain shift. To overcome this challenge, we introduce a novel diffusion-based box refinement approach. This method employs a domain-agnostic diffusion model, conditioned on the LiDAR points surrounding a coarse bounding box, to simultaneously refine the box's location, size, and orientation. We evaluate this approach under various domain adaptation settings, and our results reveal significant improvements across different datasets, object classes and detectors. Our PyTorch implementation is available at \href{https://github.com/cxy1997/DiffuBox}{https://github.com/cxy1997/DiffuBox}.

</details>

### CRT-Fusion: Camera, Radar, Temporal Fusion Using Motion Information for 3D Object Detection.
- **链接**: [arXiv:2411.03013](https://arxiv.org/abs/2411.03013) · 📚 被引 4
- **作者**: Jisong Kim, Minjae Seong, Jun Won Choi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate and robust 3D object detection is a critical component in autonomous vehicles and robotics. While recent radar-camera fusion methods have made significant progress by fusing information in the bird's-eye view (BEV) representation, they often struggle to effectively capture the motion of dynamic objects, leading to limited performance in real-world scenarios. In this paper, we introduce CRT-Fusion, a novel framework that integrates temporal information into radar-camera fusion to address this challenge. Our approach comprises three key modules: Multi-View Fusion (MVF), Motion Feature Estimator (MFE), and Motion Guided Temporal Fusion (MGTF). The MVF module fuses radar and image features within both the camera view and bird's-eye view, thereby generating a more precise unified BEV representation. The MFE module conducts two simultaneous tasks: estimation of pixel-wise velocity information and BEV segmentation. Based on the velocity and the occupancy score map obtained from the MFE module, the MGTF module aligns and fuses feature maps across multiple timestamps in a recurrent manner. By considering the motion of dynamic objects, CRT-Fusion can produce robust BEV feature maps, thereby improving detection accuracy and robustness. Extensive evaluations on the challenging nuScenes dataset demonstrate that CRT-Fusion achieves state-of-the-art performance for radar-camera-based 3D object detection. Our approach outperforms the previous best method in terms of NDS by +1.7%, while also surpassing the leading approach in mAP by +1.4%. These significant improvements in both metrics showcase the effectiveness of our proposed fusion strategy in enhancing the reliability and accuracy of 3D object detection.

</details>

### Real-time Stereo-based 3D Object Detection for Streaming Perception.
- **链接**: [arXiv:2410.12394](https://arxiv.org/abs/2410.12394)
- **作者**: Changcai Li, Zonghua Gu, Gang Chen, Libo Huang, Wei Zhang, Huihui Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to promptly respond to environmental changes is crucial for the perception system of autonomous driving. Recently, a new task called streaming perception was proposed. It jointly evaluate the latency and accuracy into a single metric for video online perception. In this work, we introduce StreamDSGN, the first real-time stereo-based 3D object detection framework designed for streaming perception. StreamDSGN is an end-to-end framework that directly predicts the 3D properties of objects in the next moment by leveraging historical information, thereby alleviating the accuracy degradation of streaming perception. Further, StreamDSGN applies three strategies to enhance the perception accuracy: (1) A feature-flow-based fusion method, which generates a pseudo-next feature at the current moment to address the misalignment issue between feature and ground truth. (2) An extra regression loss for explicit supervision of object motion consistency in consecutive frames. (3) A large kernel backbone with a large receptive field for effectively capturing long-range spatial contextual features caused by changes in object positions. Experiments on the KITTI Tracking dataset show that, compared with the strong baseline, StreamDSGN significantly improves the streaming average precision by up to 4.33%. Our code is available at https://github.com/weiyangdaren/streamDSGN-pytorch.

</details>

### 3DET-Mamba: Causal Sequence Modelling for End-to-End 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/547108084f0c2af39b956f8eadb75d1b-Abstract-Conference.html) · 📚 被引 3
- **作者**: Mingsheng Li, Jiakang Yuan, Sijin Chen, Lin Zhang, Anyu Zhu, Xin Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### STONE: A Submodular Optimization Framework for Active 3D Object Detection.
- **链接**: [arXiv:2410.03918](https://arxiv.org/abs/2410.03918)
- **作者**: Ruiyu Mao, Sarthak Kumar Maharana, Rishabh K. Iyer, Yunhui Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is fundamentally important for various emerging applications, including autonomous driving and robotics. A key requirement for training an accurate 3D object detector is the availability of a large amount of LiDAR-based point cloud data. Unfortunately, labeling point cloud data is extremely challenging, as accurate 3D bounding boxes and semantic labels are required for each potential object. This paper proposes a unified active 3D object detection framework, for greatly reducing the labeling cost of training 3D object detectors. Our framework is based on a novel formulation of submodular optimization, specifically tailored to the problem of active 3D object detection. In particular, we address two fundamental challenges associated with active 3D object detection: data imbalance and the need to cover the distribution of the data, including LiDAR-based point cloud data of varying difficulty levels. Extensive experiments demonstrate that our method achieves state-of-the-art performance with high computational efficiency compared to existing active learning methods. The code is available at https://github.com/RuiyuM/STONE.

</details>

### One for All: Multi-Domain Joint Training for Point Cloud Based 3D Object Detection.
- **链接**: [arXiv:2411.01584](https://arxiv.org/abs/2411.01584) · 📚 被引 3
- **作者**: Zhenyu Wang, Yali Li, Hengshuang Zhao, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The current trend in computer vision is to utilize one universal model to address all various tasks. Achieving such a universal model inevitably requires incorporating multi-domain data for joint training to learn across multiple problem scenarios. In point cloud based 3D object detection, however, such multi-domain joint training is highly challenging, because large domain gaps among point clouds from different datasets lead to the severe domain-interference problem. In this paper, we propose \textbf{OneDet3D}, a universal one-for-all model that addresses 3D detection across different domains, including diverse indoor and outdoor scenes, within the \emph{same} framework and only \emph{one} set of parameters. We propose the domain-aware partitioning in scatter and context, guided by a routing mechanism, to address the data interference issue, and further incorporate the text modality for a language-guided classification to unify the multi-dataset label spaces and mitigate the category interference issue. The fully sparse structure and anchor-free head further accommodate point clouds with significant scale disparities. Extensive experiments demonstrate the strong universal ability of OneDet3D to utilize only one trained model for addressing almost all 3D object detection tasks.

</details>

### ImOV3D: Learning Open Vocabulary Point Clouds 3D Object Detection from Only 2D Images.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ff9783ec29688387d44779d67d06ef66-Abstract-Conference.html)
- **作者**: Timing Yang, Yuanliang Ju, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Voxel Mamba: Group-Free State Space Models for Point Cloud based 3D Object Detection.
- **链接**: [arXiv:2406.10700](https://arxiv.org/abs/2406.10700) · 📚 被引 29
- **作者**: Guowen Zhang, Lue Fan, Chenhang He, Zhen Lei, Zhaoxiang Zhang, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Serialization-based methods, which serialize the 3D voxels and group them into multiple sequences before inputting to Transformers, have demonstrated their effectiveness in 3D object detection. However, serializing 3D voxels into 1D sequences will inevitably sacrifice the voxel spatial proximity. Such an issue is hard to be addressed by enlarging the group size with existing serialization-based methods due to the quadratic complexity of Transformers with feature sizes. Inspired by the recent advances of state space models (SSMs), we present a Voxel SSM, termed as Voxel Mamba, which employs a group-free strategy to serialize the whole space of voxels into a single sequence. The linear complexity of SSMs encourages our group-free design, alleviating the loss of spatial proximity of voxels. To further enhance the spatial proximity, we propose a Dual-scale SSM Block to establish a hierarchical structure, enabling a larger receptive field in the 1D serialization curve, as well as more complete local regions in 3D space. Moreover, we implicitly apply window partition under the group-free framework by positional encoding, which further enhances spatial proximity by encoding voxel positional information. Our experiments on Waymo Open Dataset and nuScenes dataset show that Voxel Mamba not only achieves higher accuracy than state-of-the-art methods, but also demonstrates significant advantages in computational efficiency.

</details>

### MonoMAE: Enhancing Monocular 3D Detection through Depth-Aware Masked Autoencoders.
- **链接**: [arXiv:2405.07696](https://arxiv.org/abs/2405.07696) · 📚 被引 11
- **作者**: Xueying Jiang, Sheng Jin, Xiaoqin Zhang, Ling Shao, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection aims for precise 3D localization and identification of objects from a single-view image. Despite its recent progress, it often struggles while handling pervasive object occlusions that tend to complicate and degrade the prediction of object dimensions, depths, and orientations. We design MonoMAE, a monocular 3D detector inspired by Masked Autoencoders that addresses the object occlusion issue by masking and reconstructing objects in the feature space. MonoMAE consists of two novel designs. The first is depth-aware masking that selectively masks certain parts of non-occluded object queries in the feature space for simulating occluded object queries for network training. It masks non-occluded object queries by balancing the masked and preserved query portions adaptively according to the depth information. The second is lightweight query completion that works with the depth-aware masking to learn to reconstruct and complete the masked object queries. With the proposed object occlusion and completion, MonoMAE learns enriched 3D representations that achieve superior monocular 3D detection performance qualitatively and quantitatively for both occluded and non-occluded objects. Additionally, MonoMAE learns generalizable representations that can work well in new domains.

</details>

### Training an Open-Vocabulary Monocular 3D Detection Model without 3D Data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8492211e9176b8abdaeb1f7aa4c223ea-Abstract-Conference.html) · 📚 被引 12
- **作者**: Rui Huang, Henry Zheng, Yan Wang, Zhuofan Xia, Marco Pavone, Gao Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MAN TruckScenes: A multimodal dataset for autonomous trucking in diverse conditions.
- **链接**: [arXiv:2407.07462](https://arxiv.org/abs/2407.07462) · 📚 被引 19
- **作者**: Felix Fent, Fabian Kuttenreich, Florian Ruch, Farija Rizwin, Stefan Juergens, Lorenz Lechermann et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous trucking is a promising technology that can greatly impact modern logistics and the environment. Ensuring its safety on public roads is one of the main duties that requires an accurate perception of the environment. To achieve this, machine learning methods rely on large datasets, but to this day, no such datasets are available for autonomous trucks. In this work, we present MAN TruckScenes, the first multimodal dataset for autonomous trucking. MAN TruckScenes allows the research community to come into contact with truck-specific challenges, such as trailer occlusions, novel sensor perspectives, and terminal environments for the first time. It comprises more than 740 scenes of 20s each within a multitude of different environmental conditions. The sensor set includes 4 cameras, 6 lidar, 6 radar sensors, 2 IMUs, and a high-precision GNSS. The dataset's 3D bounding boxes were manually annotated and carefully reviewed to achieve a high quality standard. Bounding boxes are available for 27 object classes, 15 attributes, and a range of more than 230m. The scenes are tagged according to 34 distinct scene tags, and all objects are tracked throughout the scene to promote a wide range of applications. Additionally, MAN TruckScenes is the first dataset to provide 4D radar data with 360° coverage and is thereby the largest radar dataset with annotated 3D bounding boxes. Finally, we provide extensive dataset analysis and baseline results. The dataset, development kit, and more are available online.

</details>

## 跨领域论文（完整笔记在其他领域）

- CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. → [vlm](../vlm/Guideline%202024.md)
- Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- V-DETR: DETR with Vertex Relative Position Encoding for 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors. → [object-detection](../object-detection/Guideline%202024.md)
- SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects. → [bev](../bev/Guideline%202024.md)
- RadarDistill: Boosting Radar-Based Object Detection Performance via Knowledge Distillation from LiDAR Features. → [object-detection](../object-detection/Guideline%202024.md)
- PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. → [bev](../bev/Guideline%202024.md)
- UniMODE: Unified Monocular 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Multi-View Attentive Contextualization for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Learning Occupancy for Monocular 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. → [bev](../bev/Guideline%202024.md)
- IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. → [multimodal](../multimodal/Guideline%202024.md)
- SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Decoupled Pseudo-Labeling for Semi-Supervised Monocular 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- CRKD: Enhanced Camera-Radar Object Detection with Cross-Modality Knowledge Distillation. → [object-detection](../object-detection/Guideline%202024.md)
- Visual Point Cloud Forecasting Enables Scalable Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Collaborative Semantic Occupancy Prediction with Hybrid Feature Fusion in Connected Automated Vehicles. → [occupancy](../occupancy/Guideline%202024.md)
- SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- SparseOcc: Rethinking Sparse Latent Representation for Vision-Based Semantic Occupancy Prediction. → [occupancy](../occupancy/Guideline%202024.md)
- DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving. → [object-detection](../object-detection/Guideline%202024.md)
- UniPAD: A Universal Pre-Training Paradigm for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Volumetric Environment Representation for Vision-Language Navigation. → [vlm](../vlm/Guideline%202024.md)
- OPEN: Object-Wise Position Embedding for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- DeTra: A Unified Model for Object Detection and Trajectory Forecasting. → [object-detection](../object-detection/Guideline%202024.md)
- Learning High-Resolution Vector Representation from Multi-camera Images for 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Diff3DETR: Agent-Based Diffusion Model for Semi-supervised 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Diffusion Model for Robust Multi-sensor Fusion in 3D Object Detection and BEV Segmentation. → [bev](../bev/Guideline%202024.md)
- Ray Denoising: Depth-Aware Hard Negative Sampling for Multi-view 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather. → [multimodal](../multimodal/Guideline%202024.md)
- GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection. → [bev](../bev/Guideline%202024.md)
- OV-Uni3DETR: Towards Unified Open-Vocabulary 3D Object Detection via Cycle-Modality Propagation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene. → [bev](../bev/Guideline%202024.md)
- Fast Point Cloud Geometry Compression with Context-Based Residual Coding and INR-Based Refinement. → [network-pruning](../network-pruning/Guideline%202024.md)
- DA-BEV: Unsupervised Domain Adaptation for Bird's Eye View Perception. → [bev](../bev/Guideline%202024.md)
- 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- CALICO: Self-Supervised Camera-LiDAR Contrastive Pre-training for BEV Perception. → [bev](../bev/Guideline%202024.md)
- GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer. → [vision-transformer](../vision-transformer/Guideline%202024.md)
- Towards Flexible 3D Perception: Object-Centric Occupancy Completion Augments 3D Object Detection. → [occupancy](../occupancy/Guideline%202024.md)
- Unified Domain Generalization and Adaptation for Multi-View 3D Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- MVSDet: Multi-View Indoor 3D Object Detection via Efficient Plane Sweeps. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- OPUS: Occupancy Prediction Using a Sparse Set. → [occupancy](../occupancy/Guideline%202024.md)
- ZOPP: A Framework of Zero-shot Offboard Panoptic Perception for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)


## 🆕 增量新增

### Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors. **⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02001)
- **作者**: Haoxuanye Ji, Pengpeng Liang, Erkang Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对3D目标检测中查询锚点初始化不准确、影响检测性能的问题。②提出利用2D检测结果引导3D查询锚点的生成，通过2D-3D几何对应关系为3D检测器提供更优的初始锚点。③相比传统随机或数据驱动锚点，该方法利用了成熟的2D检测器先验，提升锚点质量。④摘要未提供具体实验数据，需查看全文验证效果。
- **摘要（英）**: This paper addresses the issue of inaccurate query anchor initialization in 3D object detection. It proposes using 2D detection results to guide the generation of 3D query anchors via 2D-3D geometric correspondence, leveraging mature 2D detectors for better priors. The abstract lacks experimental details, requiring full-text review.
- **核心贡献**: 提出2D检测引导的3D查询锚点生成方法，提升3D检测初始化质量。
- **创新点**: 利用2D检测先验改善3D查询锚点，跨模态信息融合。
- **结果**: 具体效果未在摘要中报告。

### SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.20318](https://arxiv.org/abs/2403.20318)
- **作者**: Abhinav Kumar, Yuliang Guo, Xinyu Huang, Liu Ren, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中大型物体（如卡车、公交车）因截断和遮挡导致定位精度差的问题。②提出SeaBird方法，在鸟瞰图（BEV）分割任务中使用Dice损失，并设计专门的网络结构来优化大型物体的中心点预测。③相比传统L1损失或交叉熵损失，Dice损失能更好地处理类别不平衡和形状不规则，提升大型物体的分割质量。④在KITTI和nuScenes数据集上，对大型物体的3D检测精度显著提升，尤其在IoU阈值较高时表现突出。
- **摘要（英）**: This paper addresses the challenge of monocular 3D detection for large objects, which suffer from truncation and occlusion. It proposes SeaBird, a method that applies Dice loss to bird's eye view segmentation, improving center point prediction for large objects. Compared to L1 or cross-entropy losses, Dice loss better handles class imbalance and irregular shapes, leading to significant accuracy gains on KITTI and nuScenes, especially at high IoU thresholds.
- **核心贡献**: 提出将Dice损失应用于BEV分割，显著提升单目3D检测中大型物体的精度。
- **创新点**: 利用Dice损失对形状和尺度的鲁棒性，优化BEV分割中的中心点预测。
- **结果**: 在KITTI和nuScenes上大型物体检测精度显著提升。

### PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01415)
- **作者**: Kuan-Chih Huang, Weijie Lyu, Ming-Hsuan Yang, Yi-Hsuan Tsai
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2024
- **摘要（中）**: ①针对时序3D目标检测中计算开销大和长程依赖建模不足的问题。②提出PTT（Point-Trajectory Transformer），利用点轨迹（point trajectories）作为时序特征，通过Transformer高效聚合多帧信息。③相比基于体素或BEV的时序融合方法，PTT直接操作原始点云轨迹，减少信息丢失并降低计算复杂度。④在nuScenes数据集上，PTT在保持高精度的同时，推理速度显著提升，尤其在长时序场景下表现优异。
- **摘要（英）**: This paper tackles the high computational cost and insufficient long-range dependency modeling in temporal 3D object detection. It proposes PTT, a point-trajectory transformer that aggregates multi-frame information via point trajectories, reducing information loss and computation compared to voxel or BEV-based fusion. On nuScenes, PTT achieves high accuracy with significantly improved inference speed, especially in long-sequence scenarios.
- **核心贡献**: 提出基于点轨迹的Transformer架构，实现高效时序3D检测。
- **创新点**: 利用点轨迹而非体素或BEV进行时序特征聚合，降低计算并增强长程依赖。
- **结果**: 在nuScenes上实现高精度和快速推理。

### GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02004)
- **作者**: Xiaotian Li, Baojie Fan, Jiandong Tian, Huijie Fan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对LiDAR和相机融合中模态对齐和特征互补不足的问题。②提出GAFusion，通过多种引导机制（如深度引导、语义引导）自适应融合LiDAR和相机特征。③相比简单拼接或注意力融合，GAFusion利用多级引导信息，增强跨模态特征的对齐和互补。④在nuScenes和Waymo数据集上，GAFusion在3D检测精度上达到SOTA，尤其在远距离和小物体场景下提升明显。
- **摘要（英）**: This paper addresses the insufficient modality alignment and complementarity in LiDAR-camera fusion. It proposes GAFusion, which adaptively fuses LiDAR and camera features using multiple guidance mechanisms (e.g., depth and semantic guidance). Compared to simple concatenation or attention fusion, GAFusion enhances cross-modal alignment and complementarity, achieving SOTA 3D detection accuracy on nuScenes and Waymo, especially for distant and small objects.
- **核心贡献**: 提出多引导自适应融合框架，显著提升LiDAR-相机3D检测精度。
- **创新点**: 引入深度和语义等多级引导，实现更有效的跨模态特征融合。
- **结果**: 在nuScenes和Waymo上达到SOTA精度。

### UniMODE: Unified Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01567)
- **作者**: Zhuoling Li, Xiaogang Xu, Ser-Nam Lim, Hengshuang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中不同物体尺度差异大和深度估计不准的问题。②提出UniMODE，统一处理单目3D检测任务，通过多尺度特征和自适应深度预测模块提升泛化能力。③相比专用模型，UniMODE在多种数据集上无需微调即可适应，减少领域差距。④在KITTI和nuScenes上，UniMODE在单目3D检测精度上达到SOTA，尤其在跨数据集迁移时表现稳健。
- **摘要（英）**: This paper addresses the challenges of scale variation and inaccurate depth estimation in monocular 3D detection. It proposes UniMODE, which unifies the task with multi-scale features and adaptive depth prediction, improving generalization. Compared to specialized models, UniMODE adapts across datasets without fine-tuning, achieving SOTA accuracy on KITTI and nuScenes, with robust cross-dataset performance.
- **核心贡献**: 提出统一单目3D检测框架，提升跨数据集泛化能力。
- **创新点**: 结合多尺度特征和自适应深度预测，实现任务统一。
- **结果**: 在KITTI和nuScenes上达到SOTA并稳健迁移。

### VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01643)
- **作者**: Zihua Liu, Hiroki Sakuma, Masatoshi Okutomi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: 针对弱监督3D物体检测中依赖昂贵3D标注的问题，提出VSRD方法，利用实例感知的体积轮廓渲染技术，仅需2D框标注即可训练3D检测器。该方法通过可微渲染将3D提案投影为体积轮廓，并与2D实例分割掩码对齐，从而提供监督信号。相比现有弱监督方法，VSRD更精确地利用实例级几何信息，减少了对3D标注的依赖。实验表明，在KITTI等数据集上，该方法显著提升了弱监督3D检测的精度。
- **摘要（英）**: Addressing the high cost of 3D annotations in weakly supervised 3D object detection, VSRD introduces instance-aware volumetric silhouette rendering to train detectors using only 2D box labels. It aligns rendered volumetric silhouettes with 2D instance masks via differentiable rendering, providing richer geometric supervision. Compared to prior weakly supervised methods, VSRD leverages instance-level cues more effectively, achieving notable accuracy improvements on KITTI and other benchmarks.
- **核心贡献**: 提出基于体积轮廓渲染的弱监督3D检测框架，仅需2D标注。
- **创新点**: 将实例感知的体积渲染引入弱监督3D检测，实现几何级监督。
- **结果**: 在KITTI等数据集上显著提升弱监督3D检测精度。

### Learning Occupancy for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00979)
- **作者**: Liang Peng, Junkai Xu, Haoran Cheng, Zheng Yang, Xiaopei Wu, Wei Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: 针对单目3D物体检测中深度估计不准确导致定位精度低的问题，提出学习占用场作为中间表示的方法。该方法将3D空间划分为占用网格，并预测每个网格的占用概率，从而提供更丰富的几何先验。相比直接回归3D框，占用学习能更好地处理遮挡和截断。在KITTI和nuScenes数据集上，该方法显著提升了单目3D检测的定位精度和召回率。
- **摘要（英）**: Addressing inaccurate depth estimation in monocular 3D detection, this method learns an occupancy field as an intermediate representation, predicting occupancy probabilities for 3D voxels to provide richer geometric priors. Compared to direct 3D box regression, occupancy learning better handles occlusion and truncation. It achieves significant improvements in localization accuracy and recall on KITTI and nuScenes.
- **核心贡献**: 提出基于占用场学习的单目3D检测框架。
- **创新点**: 利用3D占用预测作为中间监督，增强几何理解。
- **结果**: 在KITTI和nuScenes上定位精度和召回率显著提升。

### IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 100%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01412)
- **作者**: Junbo Yin, Jianbing Shen, Runnan Chen, Wei Li, Ruigang Yang, Pascal Frossard et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多模态3D检测中相机与LiDAR特征融合不充分、实例级信息丢失的问题。②提出IS-Fusion，通过实例-场景协同融合模块，在实例级别和场景级别同时融合图像与点云特征，并设计跨模态注意力机制。③相比现有融合方法（如点级或体素级），首次显式建模实例级交互，提升对遮挡和稀疏区域的感知。④在KITTI和nuScenes上达到SOTA，尤其在困难类别和远距离目标上优势明显。
- **摘要（英）**: This paper addresses insufficient camera-LiDAR fusion in multimodal 3D detection by proposing IS-Fusion, which collaboratively fuses instance-level and scene-level features with cross-modal attention. Unlike point- or voxel-level methods, it explicitly models instance interactions. Achieves SOTA on KITTI and nuScenes, especially for hard and distant objects.
- **核心贡献**: 提出实例-场景协同融合的多模态3D检测框架。
- **创新点**: 实例级与场景级跨模态注意力协同融合。
- **结果**: 在KITTI和nuScenes上达到SOTA。

### SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01372)
- **作者**: Gang Zhang, Junnan Chen, Guohuan Gao, Jianmin Li, Si Liu, Xiaolin Hu
- **🏷️ 机构**: Tsinghua
- **会议**: CVPR 2024
- **摘要（中）**: ①针对全稀疏3D目标检测中特征提取效率低、感受野受限的问题。②提出SAFDNet，一种简单有效的全稀疏网络，通过设计稀疏卷积模块和特征融合策略来增强稀疏点云的特征表达。③相比现有全稀疏方法，在保持稀疏性的同时提升了检测精度和速度。④在nuScenes和Waymo数据集上取得了领先的检测性能，验证了其有效性。
- **摘要（英）**: This paper addresses the inefficiency and limited receptive field in fully sparse 3D object detection. It proposes SAFDNet, a simple yet effective network with sparse convolution modules and feature fusion to enhance feature representation. Compared to existing fully sparse methods, it improves detection accuracy and speed, achieving state-of-the-art results on nuScenes and Waymo.
- **核心贡献**: 提出了一种简单有效的全稀疏3D检测网络SAFDNet，平衡了精度与效率。
- **创新点**: 设计了针对稀疏点云的高效特征提取与融合机制。
- **结果**: 在nuScenes和Waymo上取得领先的检测性能。

### Decoupled Pseudo-Labeling for Semi-Supervised Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01601)
- **作者**: Jiacheng Zhang, Jiaming Li, Xiangru Lin, Wei Zhang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对半监督单目3D目标检测中伪标签噪声大、训练不稳定的问题。②提出解耦伪标签方法，分别处理分类和回归任务的伪标签生成，减少噪声传播。③通过独立优化分类和回归的置信度阈值，提高了伪标签质量。④在KITTI和nuScenes基准上，使用少量标注数据时显著提升了检测精度，优于现有半监督方法。
- **摘要（英）**: This paper addresses the noisy pseudo-labels and unstable training in semi-supervised monocular 3D object detection. It proposes a decoupled pseudo-labeling method that separately handles classification and regression tasks to reduce noise propagation. By independently optimizing confidence thresholds, it improves pseudo-label quality, achieving significant accuracy gains over existing methods on KITTI and nuScenes with limited labeled data.
- **核心贡献**: 提出了解耦伪标签框架，提升半监督单目3D检测的精度和稳定性。
- **创新点**: 将分类和回归伪标签生成解耦，独立优化阈值。
- **结果**: 在KITTI和nuScenes上以少量标注数据取得显著性能提升。

<!-- COMPLETE v1 papers=58 -->
