# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### RIDDLE: Lidar Data Compression with Range Image Deep Delta Encoding.
- **链接**: [arXiv:2206.01738](https://arxiv.org/abs/2206.01738) · 📚 被引 32
- **作者**: Xuanyu Zhou, Charles R. Qi, Yin Zhou, Dragomir Anguelov
- **🏷️ 机构**: Waymo LLC
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Lidars are depth measuring sensors widely used in autonomous driving and augmented reality. However, the large volume of data produced by lidars can lead to high costs in data storage and transmission. While lidar data can be represented as two interchangeable representations: 3D point clouds and range images, most previous work focus on compressing the generic 3D point clouds. In this work, we show that directly compressing the range images can leverage the lidar scanning pattern, compared to compressing the unprojected point clouds. We propose a novel data-driven range image compression algorithm, named RIDDLE (Range Image Deep DeLta Encoding). At its core is a deep model that predicts the next pixel value in a raster scanning order, based on contextual laser shots from both the current and past scans (represented as a 4D point cloud of spherical coordinates and time). The deltas between predictions and original values can then be compressed by entropy encoding. Evaluated on the Waymo Open Dataset and KITTI, our method demonstrates significant improvement in the compression rate (under the same distortion) compared to widely used point cloud and range image compression algorithms as well as recent deep methods.

### 3DAC: Learning Attribute Compression for Point Clouds.
- **链接**: [arXiv:2203.09931](https://arxiv.org/abs/2203.09931) · 📚 被引 50
- **作者**: Guangchi Fang, Qingyong Hu, Hanyun Wang, Yiling Xu, Yulan Guo
- **🏷️ 机构**: Sun Yat-sen University, University of Oxford, Information Engineering University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We study the problem of attribute compression for large-scale unstructured 3D point clouds. Through an in-depth exploration of the relationships between different encoding steps and different attribute channels, we introduce a deep compression network, termed 3DAC, to explicitly compress the attributes of 3D point clouds and reduce storage usage in this paper. Specifically, the point cloud attributes such as color and reflectance are firstly converted to transform coefficients. We then propose a deep entropy model to model the probabilities of these coefficients by considering information hidden in attribute transforms and previous encoded attributes. Finally, the estimated probabilities are used to further compress these transform coefficients to a final attributes bitstream. Extensive experiments conducted on both indoor and outdoor large-scale open point cloud datasets, including ScanNet and SemanticKITTI, demonstrated the superior compression rates and reconstruction quality of the proposed 3DAC.

### Density-preserving Deep Point Cloud Compression.
- **链接**: [arXiv:2204.12684](https://arxiv.org/abs/2204.12684) · 📚 被引 80
- **作者**: Yun He, Xinlin Ren, Danhang Tang, Yinda Zhang, Xiangyang Xue, Yanwei Fu
- **🏷️ 机构**: Fudan University, Google
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Local density of point clouds is crucial for representing local details, but has been overlooked by existing point cloud compression methods. To address this, we propose a novel deep point cloud compression method that preserves local density information. Our method works in an auto-encoder fashion: the encoder downsamples the points and learns point-wise features, while the decoder upsamples the points using these features. Specifically, we propose to encode local geometry and density with three embeddings: density embedding, local position embedding and ancestor embedding. During the decoding, we explicitly predict the upsampling factor for each point, and the directions and scales of the upsampled points. To mitigate the clustered points issue in existing methods, we design a novel sub-point convolution layer, and an upsampling block with adaptive scale. Furthermore, our method can also compress point-wise attributes, such as normal. Extensive qualitative and quantitative results on SemanticKITTI and ShapeNet demonstrate that our method achieves the state-of-the-art rate-distortion trade-off.

### Fire Together Wire Together: A Dynamic Pruning Approach with Self-Supervised Mask Prediction.
- **链接**: [arXiv:2110.08232](https://arxiv.org/abs/2110.08232) · 📚 被引 43
- **作者**: Sara Elkerdawy, Mostafa Elhoushi, Hong Zhang, Nilanjan Ray
- **🏷️ 机构**: University of Alberta,Huawei, Toronto Heterogeneous Compilers Lab,Huawei
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Dynamic model pruning is a recent direction that allows for the inference of a different sub-network for each input sample during deployment. However, current dynamic methods rely on learning a continuous channel gating through regularization by inducing sparsity loss. This formulation introduces complexity in balancing different losses (e.g task loss, regularization loss). In addition, regularization based methods lack transparent tradeoff hyperparameter selection to realize a computational budget. Our contribution is two-fold: 1) decoupled task and pruning losses. 2) Simple hyperparameter selection that enables FLOPs reduction estimation before training. Inspired by the Hebbian theory in Neuroscience: "neurons that fire together wire together", we propose to predict a mask to process k filters in a layer based on the activation of its previous layer. We pose the problem as a self-supervised binary classification problem. Each mask predictor module is trained to predict if the log-likelihood for each filter in the current layer belongs to the top-k activated filters. The value k is dynamically estimated for each input based on a novel criterion using the mass of heatmaps. We show experiments on several neural architectures, such as VGG, ResNet and MobileNet on CIFAR and ImageNet datasets. On CIFAR, we reach similar accuracy to SOTA methods with 15% and 24% higher FLOPs reduction. Similarly in ImageNet, we achieve lower drop in accuracy with up to 13% improvement in FLOPs reduction.

### Revisiting Random Channel Pruning for Neural Network Compression.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00029) · 📚 被引 110
- **作者**: Yawei Li, Kamil Adamczewski, Wen Li, Shuhang Gu, Radu Timofte, Luc Van Gool
- **🏷️ 机构**: Computer Vision Lab, ETH Zurich, MPI-IS, UESTC
- **会议**: CVPR 2022

### When to Prune? A Policy towards Early Structural Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01193) · 📚 被引 49
- **作者**: Maying Shen, Pavlo Molchanov, Hongxu Yin, José M. Álvarez
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2022

### Interspace Pruning: Using Adaptive Filter Representations to Improve Training of Sparse CNNs.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01220) · 📚 被引 29
- **作者**: Paul Wimmer, Jens Mehnert, Alexandru Condurache
- **🏷️ 机构**: Automated Driving Research, Robert Bosch GmbH,Stuttgart,Germany,70469
- **会议**: CVPR 2022

### Quarantine: Sparsity Can Uncover the Trojan Attack Trigger for Free.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00068) · 📚 被引 13
- **作者**: Tianlong Chen, Zhenyu Zhang, Yihua Zhang, Shiyu Chang, Sijia Liu, Zhangyang Wang
- **🏷️ 机构**: University of Texas at Austin, Michigan State University, University of California,Santa Barbara
- **会议**: CVPR 2022

### Attentive Fine-Grained Structured Sparsity for Image Restoration.
- **链接**: [arXiv:2204.12266](https://arxiv.org/abs/2204.12266) · [代码](https://github.com/JungHunOh/SLS_CVPR2022) · 📚 被引 12
- **作者**: Junghun Oh, Heewon Kim, Seungjun Nah, Cheeun Hong, Jonghyun Choi, Kyoung Mu Lee
- **🏷️ 机构**: ASRI,Dept. of ECE, Yonsei University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Image restoration tasks have witnessed great performance improvement in recent years by developing large deep models. Despite the outstanding performance, the heavy computation demanded by the deep models has restricted the application of image restoration. To lift the restriction, it is required to reduce the size of the networks while maintaining accuracy. Recently, N:M structured pruning has appeared as one of the effective and practical pruning approaches for making the model efficient with the accuracy constraint. However, it fails to account for different computational complexities and performance requirements for different layers of an image restoration network. To further optimize the trade-off between the efficiency and the restoration accuracy, we propose a novel pruning method that determines the pruning ratio for N:M structured sparsity at each layer. Extensive experimental results on super-resolution and deblurring tasks demonstrate the efficacy of our method which outperforms previous pruning methods significantly. PyTorch implementation for the proposed methods is available at https://github.com/JungHunOh/SLS_CVPR2022.
