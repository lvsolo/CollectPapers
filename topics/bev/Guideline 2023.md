# BEV — 2023 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

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

### BAEFormer: Bi-Directional and Early Interaction Transformers for Bird's Eye View Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00925) · 📚 被引 31
- **作者**: Cong Pan, Yonghao He, Junran Peng, Qian Zhang, Wei Sui, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,National Laboratory of Pattern Recognition, Horizon Robotics, Huawei Inc.
- **会议**: CVPR 2023

### BEV@DC: Bird's-Eye View Assisted Training for Depth Completion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00891) · 📚 被引 37
- **作者**: Wending Zhou, Xu Yan, Yinghong Liao, Yuankai Lin, Jin Huang, Gangming Zhao et al.
- **🏷️ 机构**: FNii, CUHK-Shenzhen, Huazhong University of Science and Technology, Cardiff University
- **会议**: CVPR 2023

### BEV-Guided Multi-Modality Fusion for Driving Perception.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02103) · 📚 被引 59
- **作者**: Yunze Man, Liang-Yan Gui, Yu-Xiong Wang
- **🏷️ 机构**: UIUC
- **会议**: CVPR 2023

### BEV-LaneDet: An Efficient 3D Lane Detection Based on Virtual Camera via Key-Points.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00103) · 📚 被引 70
- **作者**: Ruihao Wang, Jian Qin, Kaiying Li, Yaochen Li, Dong Cao, Jintao Xu
- **🏷️ 机构**: HAOMO.AI Technology Co., Ltd., Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2023

### FB-BEV: BEV Representation from Forward-Backward View Transformations.
- **链接**: [arXiv:2308.02236](https://arxiv.org/abs/2308.02236) · [代码](https://github.com/NVlabs/FB-BEV) · 📚 被引 139
- **作者**: Zhiqi Li, Zhiding Yu, Wenhai Wang, Anima Anandkumar, Tong Lu, José M. Álvarez
- **🏷️ 机构**: Nanjing University,National Key Lab for Novel Software Technology, NVIDIA, The Chinese University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> View Transformation Module (VTM), where transformations happen between multi-view image features and Bird-Eye-View (BEV) representation, is a crucial step in camera-based BEV perception systems. Currently, the two most prominent VTM paradigms are forward projection and backward projection. Forward projection, represented by Lift-Splat-Shoot, leads to sparsely projected BEV features without post-processing. Backward projection, with BEVFormer being an example, tends to generate false-positive BEV features from incorrect projections due to the lack of utilization on depth. To address the above limitations, we propose a novel forward-backward view transformation module. Our approach compensates for the deficiencies in both existing methods, allowing them to enhance each other to obtain higher quality BEV representations mutually. We instantiate the proposed module with FB-BEV, which achieves a new state-of-the-art result of 62.4% NDS on the nuScenes test set. Code and models are available at https://github.com/NVlabs/FB-BEV.

</details>

### MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception.
- **链接**: [arXiv:2211.10593](https://arxiv.org/abs/2211.10593) · 📚 被引 46
- **作者**: Hongyu Zhou, Zheng Ge, Zeming Li, Xiangyu Zhang
- **🏷️ 机构**: MEGVII Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes an efficient multi-camera to Bird's-Eye-View (BEV) view transformation method for 3D perception, dubbed MatrixVT. Existing view transformers either suffer from poor transformation efficiency or rely on device-specific operators, hindering the broad application of BEV models. In contrast, our method generates BEV features efficiently with only convolutions and matrix multiplications (MatMul). Specifically, we propose describing the BEV feature as the MatMul of image feature and a sparse Feature Transporting Matrix (FTM). A Prime Extraction module is then introduced to compress the dimension of image features and reduce FTM's sparsity. Moreover, we propose the Ring \& Ray Decomposition to replace the FTM with two matrices and reformulate our pipeline to reduce calculation further. Compared to existing methods, MatrixVT enjoys a faster speed and less memory footprint while remaining deploy-friendly. Extensive experiments on the nuScenes benchmark demonstrate that our method is highly efficient but obtains results on par with the SOTA method in object detection and map segmentation tasks

</details>

## 跨领域论文（完整笔记在其他领域）

- BEV-SAN: Accurate BEV 3D Object Detection via Slice Attention Networks. → [3d-detection](../3d-detection/Guideline%202023.md)
- UniDistill: A Universal Cross-Modality Knowledge Distillation Framework for 3D Object Detection in Bird's-Eye View. → [3d-detection](../3d-detection/Guideline%202023.md)
