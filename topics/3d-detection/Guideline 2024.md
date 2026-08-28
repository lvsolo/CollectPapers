# 3D Detection — 2024 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 27 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OPEN: Object-Wise Position Embedding for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73347-5_9)
- **作者**: Jinghua Hou, Tong Wang, Xiaoqing Ye, Zhe Liu, Shi Gong, Xiao Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### LISO: Lidar-Only Self-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73016-0_15)
- **作者**: Stefan Andreas Baur, Frank Moosmann, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: ECCV 2024

### LiDAR-Based All-Weather 3D Object Detection via Prompting and Distilling 4D Radar.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_21) · 📚 被引 8
- **作者**: Yujeong Chae, Hyeonseong Kim, Changgyoon Oh, Minseok Kim, Kuk-Jin Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learning High-Resolution Vector Representation from Multi-camera Images for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72761-0_22)
- **作者**: Zhili Chen, Shuangjie Xu, Maosheng Ye, Zian Qian, Xiaoyi Zou, Dit-Yan Yeung et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Diff3DETR: Agent-Based Diffusion Model for Semi-supervised 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72754-2_4) · 📚 被引 11
- **作者**: Jiacheng Deng, Jiahao Lu, Tianzhu Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CMD: A Cross Mechanism Domain Adaptation Dataset for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72998-0_13) · 📚 被引 8
- **作者**: Jinhao Deng, Wei Ye, Hai Wu, Xun Huang, Qiming Xia, Xin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73661-2_8) · 📚 被引 3
- **作者**: Djamahl Etchegaray, Zi Huang, Tatsuya Harada, Yadan Luo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Weakly Supervised 3D Object Detection via Multi-level Visual Guidance.
- **链接**: [arXiv:2312.07530](https://arxiv.org/abs/2312.07530) · [代码](https://github.com/kuanchihhuang/VG-W3D) · 📚 被引 6
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

### FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73242-3_7)
- **作者**: Zheng Jiang, Jinqing Zhang, Yanan Zhang, Qingjie Liu, Zhenghui Hu, Baohui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image.
- **链接**: [arXiv:2407.05256](https://arxiv.org/abs/2407.05256) · 📚 被引 7
- **作者**: Pengkun Jiao, Na Zhao, Jingjing Chen, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D object detection (OV-3DDet) aims to localize and recognize both seen and previously unseen object categories within any new 3D scene. While language and vision foundation models have achieved success in handling various open-vocabulary tasks with abundant training data, OV-3DDet faces a significant challenge due to the limited availability of training data. Although some pioneering efforts have integrated vision-language models (VLM) knowledge into OV-3DDet learning, the full potential of these foundational models has yet to be fully exploited. In this paper, we unlock the textual and visual wisdom to tackle the open-vocabulary 3D detection task by leveraging the language and vision foundation models. We leverage a vision foundation model to provide image-wise guidance for discovering novel classes in 3D scenes. Specifically, we utilize a object detection vision foundation model to enable the zero-shot discovery of objects in images, which serves as the initial seeds and filtering guidance to identify novel 3D objects. Additionally, to align the 3D space with the powerful vision-language space, we introduce a hierarchical alignment approach, where the 3D feature space is aligned with the vision-language feature space using a pre-trained VLM at the instance, category, and scene levels. Through extensive experimentation, we demonstrate significant improvements in accuracy and generalization, highlighting the potential of foundation models in advancing open-vocabulary 3D object detection in real-world scenarios.

</details>

### LabelDistill: Label-Guided Cross-Modal Knowledge Distillation for Camera-Based 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72992-8_2)
- **作者**: Sanmin Kim, Youngseok Kim, Sihwan Hwang, Hyeonjun Jeong, Dongsuk Kum
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Diffusion Model for Robust Multi-sensor Fusion in 3D Object Detection and BEV Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73113-6_14)
- **作者**: Duy-Tho Le, Hengcan Shi, Jianfei Cai, Hamid Rezatofighi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

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

### Ray Denoising: Depth-Aware Hard Negative Sampling for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72967-6_12)
- **作者**: Feng Liu, Tengteng Huang, Qianjing Zhang, Haotian Yao, Chi Zhang, Fang Wan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MonoWAD: Weather-Adaptive Diffusion Model for Robust Monocular 3D Object Detection.
- **链接**: [arXiv:2407.16448](https://arxiv.org/abs/2407.16448) · [代码](https://github.com/VisualAIKHU/MonoWAD) · 📚 被引 9
- **作者**: Youngmin Oh, Hyung-Il Kim, Seong Tae Kim, Jung Uk Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important challenging task in autonomous driving. Existing methods mainly focus on performing 3D detection in ideal weather conditions, characterized by scenarios with clear and optimal visibility. However, the challenge of autonomous driving requires the ability to handle changes in weather conditions, such as foggy weather, not just clear weather. We introduce MonoWAD, a novel weather-robust monocular 3D object detector with a weather-adaptive diffusion model. It contains two components: (1) the weather codebook to memorize the knowledge of the clear weather and generate a weather-reference feature for any input, and (2) the weather-adaptive diffusion model to enhance the feature representation of the input feature by incorporating a weather-reference feature. This serves an attention role in indicating how much improvement is needed for the input feature according to the weather conditions. To achieve this goal, we introduce a weather-adaptive enhancement loss to enhance the feature representation under both clear and foggy weather conditions. Extensive experiments under various weather conditions demonstrate that MonoWAD achieves weather-robust monocular 3D object detection. The code and dataset are released at https://github.com/VisualAIKHU/MonoWAD.

</details>

### SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73030-6_27)
- **作者**: Edoardo Palladin, Roland Dietze, Praveen Narayanan, Mario Bijelic, Felix Heide
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73347-5_20)
- **作者**: Ziying Song, Lei Yang, Shaoqing Xu, Lin Liu, Dongyang Xu, Caiyan Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SimPB: A Single Model for 2D and 3D Object Detection from Multiple Cameras.
- **链接**: [arXiv:2403.10353](https://arxiv.org/abs/2403.10353) · [代码](https://github.com/nullmax-vision/SimPB) · 📚 被引 5
- **作者**: Yingqi Tang, Zhaotie Meng, Guoliang Chen, Erkang Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

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
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72761-0_7) · 📚 被引 24
- **作者**: Hongcheng Zhang, Liu Liang, Pengxin Zeng, Xiao Song, Zhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene.
- **链接**: [arXiv:2407.08569](https://arxiv.org/abs/2407.08569) · 📚 被引 9
- **作者**: Ruiyang Zhang, Hu Zhang, Hang Yu, Zhedong Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The unsupervised 3D object detection is to accurately detect objects in unstructured environments with no explicit supervisory signals. This task, given sparse LiDAR point clouds, often results in compromised performance for detecting distant or small objects due to the inherent sparsity and limited spatial resolution. In this paper, we are among the early attempts to integrate LiDAR data with 2D images for unsupervised 3D detection and introduce a new method, dubbed LiDAR-2D Self-paced Learning (LiSe). We argue that RGB images serve as a valuable complement to LiDAR data, offering precise 2D localization cues, particularly when scarce LiDAR points are available for certain objects. Considering the unique characteristics of both modalities, our framework devises a self-paced learning pipeline that incorporates adaptive sampling and weak model aggregation strategies. The adaptive sampling strategy dynamically tunes the distribution of pseudo labels during training, countering the tendency of models to overfit easily detected samples, such as nearby and large-sized objects. By doing so, it ensures a balanced learning trajectory across varying object scales and distances. The weak model aggregation component consolidates the strengths of models trained under different pseudo label distributions, culminating in a robust and powerful final model. Experimental evaluations validate the efficacy of our proposed LiSe method, manifesting significant improvements of +7.1% AP$_{BEV}$ and +3.4% AP$_{3D}$ on nuScenes, and +8.3% AP$_{BEV}$ and +7.4% AP$_{3D}$ on Lyft compared to existing techniques.

</details>
