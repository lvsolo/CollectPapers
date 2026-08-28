# BEV — 2023 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Parametric Depth Based Feature Representation Learning for Object Detection and Segmentation in Bird's-Eye View.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00779) · 📚 被引 7
- **作者**: Jiayu Yang, Enze Xie, Miaomiao Liu, José M. Álvarez
- **🏷️ 机构**: Australian National University, The University of Hong Kong, NVIDIA
- **会议**: ICCV 2023

### BEVPlace: Learning LiDAR-based Place Recognition using Bird's Eye View Images.
- **链接**: [arXiv:2302.14325](https://arxiv.org/abs/2302.14325) · [代码](https://github.com/zjuluolun/BEVPlace) · 📚 被引 88
- **作者**: Lun Luo, Shuhang Zheng, Yixuan Li, Yongzhi Fan, Beinan Yu, Si-Yuan Cao et al.
- **🏷️ 机构**: Zhejiang University,Ningbo Innovation Center, Zhejiang University,College of Information Science and Electronic Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Place recognition is a key module for long-term SLAM systems. Current LiDAR-based place recognition methods usually use representations of point clouds such as unordered points or range images. These methods achieve high recall rates of retrieval, but their performance may degrade in the case of view variation or scene changes. In this work, we explore the potential of a different representation in place recognition, i.e. bird's eye view (BEV) images. We observe that the structural contents of BEV images are less influenced by rotations and translations of point clouds. We validate that, without any delicate design, a simple VGGNet trained on BEV images achieves comparable performance with the state-of-the-art place recognition methods in scenes of slight viewpoint changes. For more robust place recognition, we design a rotation-invariant network called BEVPlace. We use group convolution to extract rotation-equivariant local features from the images and NetVLAD for global feature aggregation. In addition, we observe that the distance between BEV features is correlated with the geometry distance of point clouds. Based on the observation, we develop a method to estimate the position of the query cloud, extending the usage of place recognition. The experiments conducted on large-scale public datasets show that our method 1) achieves state-of-the-art performance in terms of recall rates, 2) is robust to view changes, 3) shows strong generalization ability, and 4) can estimate the positions of query point clouds. Source codes are publicly available at https://github.com/zjuluolun/BEVPlace.

</details>

> Place recognition is a key module for long-term SLAM systems. Current LiDAR-based place recognition methods usually use representations of point clouds such as unordered points or range images. These methods achieve high recall rates of retrieval, but their performance may degrade in the case of view variation or scene changes. In this work, we explore the potential of a different representation in place recognition, i.e. bird's eye view (BEV) images. We observe that the structural contents of BEV images are less influenced by rotations and translations of point clouds. We validate that, without any delicate design, a simple VGGNet trained on BEV images achieves comparable performance with the state-of-the-art place recognition methods in scenes of slight viewpoint changes. For more robust place recognition, we design a rotation-invariant network called BEVPlace. We use group convolution to extract rotation-equivariant local features from the images and NetVLAD for global feature aggregation. In addition, we observe that the distance between BEV features is correlated with the geometry distance of point clouds. Based on the observation, we develop a method to estimate the position of the query cloud, extending the usage of place recognition. The experiments conducted on large-scale public datasets show that our method 1) achieves state-of-the-art performance in terms of recall rates, 2) is robust to view changes, 3) shows strong generalization ability, and 4) can estimate the positions of query point clouds. Source codes are publicly available at https://github.com/zjuluolun/BEVPlace.

</details>

### Towards Viewpoint Robustness in Bird's Eye View Segmentation.
- **链接**: [arXiv:2309.05192](https://arxiv.org/abs/2309.05192) · 📚 被引 17
- **作者**: Tzofi Klinghoffer, Jonah Philion, Wenzheng Chen, Or Litany, Zan Gojcic, Jungseock Joo et al.
- **🏷️ 机构**: MIT, NVIDIA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous vehicles (AV) require that neural networks used for perception be robust to different viewpoints if they are to be deployed across many types of vehicles without the repeated cost of data collection and labeling for each. AV companies typically focus on collecting data from diverse scenarios and locations, but not camera rig configurations, due to cost. As a result, only a small number of rig variations exist across most fleets. In this paper, we study how AV perception models are affected by changes in camera viewpoint and propose a way to scale them across vehicle types without repeated data collection and labeling. Using bird's eye view (BEV) segmentation as a motivating task, we find through extensive experiments that existing perception models are surprisingly sensitive to changes in camera viewpoint. When trained with data from one camera rig, small changes to pitch, yaw, depth, or height of the camera at inference time lead to large drops in performance. We introduce a technique for novel view synthesis and use it to transform collected data to the viewpoint of target rigs, allowing us to train BEV segmentation models for diverse target rigs without any additional data collection or labeling cost. To analyze the impact of viewpoint changes, we leverage synthetic data to mitigate other gaps (content, ISP, etc). Our approach is then trained on real data and evaluated on synthetic data, enabling evaluation on diverse target rigs. We release all data for use in future work. Our method is able to recover an average of 14.7% of the IoU that is otherwise lost when deploying to new rigs.

</details>

### MapPrior: Bird's-Eye View Map Layout Estimation with Generative Models.
- **链接**: [arXiv:2308.12963](https://arxiv.org/abs/2308.12963) · 📚 被引 14
- **作者**: Xiyue Zhu, Vlas Zyrianov, Zhijian Liu, Shenlong Wang
- **🏷️ 机构**: University of Illinois at Urbana-Champaign, MIT
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite tremendous advancements in bird's-eye view (BEV) perception, existing models fall short in generating realistic and coherent semantic map layouts, and they fail to account for uncertainties arising from partial sensor information (such as occlusion or limited coverage). In this work, we introduce MapPrior, a novel BEV perception framework that combines a traditional discriminative BEV perception model with a learned generative model for semantic map layouts. Our MapPrior delivers predictions with better accuracy, realism, and uncertainty awareness. We evaluate our model on the large-scale nuScenes benchmark. At the time of submission, MapPrior outperforms the strongest competing method, with significantly improved MMD and ECE scores in camera- and LiDAR-based BEV perception.

</details>

### BEV-DG: Cross-Modal Learning under Bird's-Eye View for Domain Generalization of 3D Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01068) · 📚 被引 19
- **作者**: Miaoyu Li, Yachao Zhang, Xu Ma, Yanyun Qu, Yun Fu
- **🏷️ 机构**: Xiamen University,School of Informatics, Tsinghua University,Tsinghua Shenzhen International Graduate School, Northeastern University,Department of ECE
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- Surround-View Vision-based 3D Detection for Autonomous Driving: A Survey. → [3d-detection](../3d-detection/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
