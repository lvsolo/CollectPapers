# Occupancy — 2024 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73383-3_22) · 📚 被引 56
- **作者**: Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Fully Sparse 3D Occupancy Prediction.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72698-9_4)
- **作者**: Haisong Liu, Yang Chen, Haiguang Wang, Zetong Yang, Tianyu Li, Jia Zeng et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2024

### CVT-Occ: Cost Volume Temporal Fusion for 3D Occupancy Prediction.
- **链接**: [arXiv:2409.13430](https://arxiv.org/abs/2409.13430) · [代码](https://github.com/Tsinghua-MARS-Lab/CVT-Occ) · 📚 被引 11
- **作者**: Zhangchen Ye, Tao Jiang, Chenfeng Xu, Yiming Li, Hang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-based 3D occupancy prediction is significantly challenged by the inherent limitations of monocular vision in depth estimation. This paper introduces CVT-Occ, a novel approach that leverages temporal fusion through the geometric correspondence of voxels over time to improve the accuracy of 3D occupancy predictions. By sampling points along the line of sight of each voxel and integrating the features of these points from historical frames, we construct a cost volume feature map that refines current volume features for improved prediction outcomes. Our method takes advantage of parallax cues from historical observations and employs a data-driven approach to learn the cost volume. We validate the effectiveness of CVT-Occ through rigorous experiments on the Occ3D-Waymo dataset, where it outperforms state-of-the-art methods in 3D occupancy prediction with minimal additional computational cost. The code is released at \url{https://github.com/Tsinghua-MARS-Lab/CVT-Occ}.

</details>

### Monocular Occupancy Prediction for Scalable Indoor Scenes.
- **链接**: [arXiv:2407.11730](https://arxiv.org/abs/2407.11730) · [代码](https://github.com/hongxiaoy/ISO.git) · 📚 被引 5
- **作者**: Hongxiao Yu, Yuqi Wang, Yuntao Chen, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-based 3D occupancy prediction has recently garnered increasing attention in outdoor driving scenes. However, research in indoor scenes remains relatively unexplored. The core differences in indoor scenes lie in the complexity of scene scale and the variance in object size. In this paper, we propose a novel method, named ISO, for predicting indoor scene occupancy using monocular images. ISO harnesses the advantages of a pretrained depth model to achieve accurate depth predictions. Furthermore, we introduce the Dual Feature Line of Sight Projection (D-FLoSP) module within ISO, which enhances the learning of 3D voxel features. To foster further research in this domain, we introduce Occ-ScanNet, a large-scale occupancy benchmark for indoor scenes. With a dataset size 40 times larger than the NYUv2 dataset, it facilitates future scalable research in indoor scene analysis. Experimental results on both NYUv2 and Occ-ScanNet demonstrate that our method achieves state-of-the-art performance. The dataset and code are made publicly at https://github.com/hongxiaoy/ISO.git.

</details>

### VEON: Vocabulary-Enhanced Occupancy Prediction.
- **链接**: [arXiv:2407.12294](https://arxiv.org/abs/2407.12294) · 📚 被引 8
- **作者**: Jilai Zheng, Pin Tang, Zhongdao Wang, Guoqing Wang, Xiangxuan Ren, Bailan Feng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perceiving the world as 3D occupancy supports embodied agents to avoid collision with any types of obstacle. While open-vocabulary image understanding has prospered recently, how to bind the predicted 3D occupancy grids with open-world semantics still remains under-explored due to limited open-world annotations. Hence, instead of building our model from scratch, we try to blend 2D foundation models, specifically a depth model MiDaS and a semantic model CLIP, to lift the semantics to 3D space, thus fulfilling 3D occupancy. However, building upon these foundation models is not trivial. First, the MiDaS faces the depth ambiguity problem, i.e., it only produces relative depth but fails to estimate bin depth for feature lifting. Second, the CLIP image features lack high-resolution pixel-level information, which limits the 3D occupancy accuracy. Third, open vocabulary is often trapped by the long-tail problem. To address these issues, we propose VEON for Vocabulary-Enhanced Occupancy predictioN by not only assembling but also adapting these foundation models. We first equip MiDaS with a Zoedepth head and low-rank adaptation (LoRA) for relative-metric-bin depth transformation while reserving beneficial depth prior. Then, a lightweight side adaptor network is attached to the CLIP vision encoder to generate high-resolution features for fine-grained 3D occupancy prediction. Moreover, we design a class reweighting strategy to give priority to the tail classes. With only 46M trainable parameters and zero manual semantic labels, VEON achieves 15.14 mIoU on Occ3D-nuScenes, and shows the capability of recognizing objects with open-vocabulary categories, meaning that our VEON is label-efficient, parameter-efficient, and precise enough.

</details>

### nuCraft: Crafting High Resolution 3D Semantic Occupancy for Unified 3D Scene Understanding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72652-1_8) · 📚 被引 5
- **作者**: Benjin Zhu, Zhe Wang, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2024

> 3D occupancy-based perception pipeline has significantly advanced autonomous driving by capturing detailed scene descriptions and demonstrating strong generalizability across various object categories and shapes. Current methods predominantly rely on LiDAR or camera inputs for 3D occupancy prediction. These methods are susceptible to adverse weather conditions, limiting the all-weather deployment of self-driving cars. To improve perception robustness, we leverage the recent advances in automotive radars and introduce a novel approach that utilizes 4D imaging radar sensors for 3D occupancy prediction. Our method, RadarOcc, circumvents the limitations of sparse radar point clouds by directly processing the 4D radar tensor, thus preserving essential scene details. RadarOcc innovatively addresses the challenges associated with the voluminous and noisy 4D radar data by employing Doppler bins descriptors, sidelobe-aware spatial sparsification, and range-wise self-attention mechanisms. To minimize the interpolation errors associated with direct coordinate transformations, we also devise a spherical-based feature encoding followed by spherical-to-Cartesian feature aggregation. We benchmark various baseline methods based on distinct modalities on the public K-Radar dataset. The results demonstrate RadarOcc's state-of-the-art performance in radar-based 3D occupancy prediction and promising results even when compared with LiDAR- or camera-based methods. Additionally, we present qualitative evidence of the superior performance of 4D radar in adverse weather conditions and explore the impact of key pipeline components through ablation studies.

- ViewFormer: Exploring Spatiotemporal Modeling for Multi-view 3D Occupancy Perception via View-Guided Transformers. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- OccGen: Generative Multi-modal 3D Occupancy Prediction for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
