# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### RIDDLE: Lidar Data Compression with Range Image Deep Delta Encoding.
- **链接**: [arXiv:2206.01738](https://arxiv.org/abs/2206.01738) · 📚 被引 32
- **作者**: Xuanyu Zhou, Charles R. Qi, Yin Zhou, Dragomir Anguelov
- **🏷️ 机构**: Waymo LLC
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Lidars are depth measuring sensors widely used in autonomous driving and augmented reality. However, the large volume of data produced by lidars can lead to high costs in data storage and transmission. While lidar data can be represented as two interchangeable representations: 3D point clouds and range images, most previous work focus on compressing the generic 3D point clouds. In this work, we show that directly compressing the range images can leverage the lidar scanning pattern, compared to compressing the unprojected point clouds. We propose a novel data-driven range image compression algorithm, named RIDDLE (Range Image Deep DeLta Encoding). At its core is a deep model that predicts the next pixel value in a raster scanning order, based on contextual laser shots from both the current and past scans (represented as a 4D point cloud of spherical coordinates and time). The deltas between predictions and original values can then be compressed by entropy encoding. Evaluated on the Waymo Open Dataset and KITTI, our method demonstrates significant improvement in the compression rate (under the same distortion) compared to widely used point cloud and range image compression algorithms as well as recent deep methods.

</details>

### 3DAC: Learning Attribute Compression for Point Clouds.
- **链接**: [arXiv:2203.09931](https://arxiv.org/abs/2203.09931) · 📚 被引 51
- **作者**: Guangchi Fang, Qingyong Hu, Hanyun Wang, Yiling Xu, Yulan Guo
- **🏷️ 机构**: Sun Yat-sen University, University of Oxford, Information Engineering University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the problem of attribute compression for large-scale unstructured 3D point clouds. Through an in-depth exploration of the relationships between different encoding steps and different attribute channels, we introduce a deep compression network, termed 3DAC, to explicitly compress the attributes of 3D point clouds and reduce storage usage in this paper. Specifically, the point cloud attributes such as color and reflectance are firstly converted to transform coefficients. We then propose a deep entropy model to model the probabilities of these coefficients by considering information hidden in attribute transforms and previous encoded attributes. Finally, the estimated probabilities are used to further compress these transform coefficients to a final attributes bitstream. Extensive experiments conducted on both indoor and outdoor large-scale open point cloud datasets, including ScanNet and SemanticKITTI, demonstrated the superior compression rates and reconstruction quality of the proposed 3DAC.

</details>

### Density-preserving Deep Point Cloud Compression.
- **链接**: [arXiv:2204.12684](https://arxiv.org/abs/2204.12684) · 📚 被引 80
- **作者**: Yun He, Xinlin Ren, Danhang Tang, Yinda Zhang, Xiangyang Xue, Yanwei Fu
- **🏷️ 机构**: Fudan University, Google
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Local density of point clouds is crucial for representing local details, but has been overlooked by existing point cloud compression methods. To address this, we propose a novel deep point cloud compression method that preserves local density information. Our method works in an auto-encoder fashion: the encoder downsamples the points and learns point-wise features, while the decoder upsamples the points using these features. Specifically, we propose to encode local geometry and density with three embeddings: density embedding, local position embedding and ancestor embedding. During the decoding, we explicitly predict the upsampling factor for each point, and the directions and scales of the upsampled points. To mitigate the clustered points issue in existing methods, we design a novel sub-point convolution layer, and an upsampling block with adaptive scale. Furthermore, our method can also compress point-wise attributes, such as normal. Extensive qualitative and quantitative results on SemanticKITTI and ShapeNet demonstrate that our method achieves the state-of-the-art rate-distortion trade-off.

</details>

### Fire Together Wire Together: A Dynamic Pruning Approach with Self-Supervised Mask Prediction.
- **链接**: [arXiv:2110.08232](https://arxiv.org/abs/2110.08232) · 📚 被引 43
- **作者**: Sara Elkerdawy, Mostafa Elhoushi, Hong Zhang, Nilanjan Ray
- **🏷️ 机构**: University of Alberta,Huawei, Toronto Heterogeneous Compilers Lab,Huawei
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dynamic model pruning is a recent direction that allows for the inference of a different sub-network for each input sample during deployment. However, current dynamic methods rely on learning a continuous channel gating through regularization by inducing sparsity loss. This formulation introduces complexity in balancing different losses (e.g task loss, regularization loss). In addition, regularization based methods lack transparent tradeoff hyperparameter selection to realize a computational budget. Our contribution is two-fold: 1) decoupled task and pruning losses. 2) Simple hyperparameter selection that enables FLOPs reduction estimation before training. Inspired by the Hebbian theory in Neuroscience: "neurons that fire together wire together", we propose to predict a mask to process k filters in a layer based on the activation of its previous layer. We pose the problem as a self-supervised binary classification problem. Each mask predictor module is trained to predict if the log-likelihood for each filter in the current layer belongs to the top-k activated filters. The value k is dynamically estimated for each input based on a novel criterion using the mass of heatmaps. We show experiments on several neural architectures, such as VGG, ResNet and MobileNet on CIFAR and ImageNet datasets. On CIFAR, we reach similar accuracy to SOTA methods with 15% and 24% higher FLOPs reduction. Similarly in ImageNet, we achieve lower drop in accuracy with up to 13% improvement in FLOPs reduction.

</details>

### Revisiting Random Channel Pruning for Neural Network Compression.
- **链接**: [arXiv:2205.05676](https://arxiv.org/abs/2205.05676) · 📚 被引 110
- **作者**: Yawei Li, Kamil Adamczewski, Wen Li, Shuhang Gu, Radu Timofte, Luc Van Gool
- **🏷️ 机构**: Computer Vision Lab, ETH Zurich, MPI-IS, UESTC
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Channel (or 3D filter) pruning serves as an effective way to accelerate the inference of neural networks. There has been a flurry of algorithms that try to solve this practical problem, each being claimed effective in some ways. Yet, a benchmark to compare those algorithms directly is lacking, mainly due to the complexity of the algorithms and some custom settings such as the particular network configuration or training procedure. A fair benchmark is important for the further development of channel pruning. Meanwhile, recent investigations reveal that the channel configurations discovered by pruning algorithms are at least as important as the pre-trained weights. This gives channel pruning a new role, namely searching the optimal channel configuration. In this paper, we try to determine the channel configuration of the pruned models by random search. The proposed approach provides a new way to compare different methods, namely how well they behave compared with random pruning. We show that this simple strategy works quite well compared with other channel pruning methods. We also show that under this setting, there are surprisingly no clear winners among different channel importance evaluation methods, which then may tilt the research efforts into advanced channel configuration searching methods.

</details>

### When to Prune? A Policy towards Early Structural Pruning.
- **链接**: [arXiv:2110.12007](https://arxiv.org/abs/2110.12007) · 📚 被引 49
- **作者**: Maying Shen, Pavlo Molchanov, Hongxu Yin, José M. Álvarez
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning enables appealing reductions in network memory footprint and time complexity. Conventional post-training pruning techniques lean towards efficient inference while overlooking the heavy computation for training. Recent exploration of pre-training pruning at initialization hints on training cost reduction via pruning, but suffers noticeable performance degradation. We attempt to combine the benefits of both directions and propose a policy that prunes as early as possible during training without hurting performance. Instead of pruning at initialization, our method exploits initial dense training for few epochs to quickly guide the architecture, while constantly evaluating dominant sub-networks via neuron importance ranking. This unveils dominant sub-networks whose structures turn stable, allowing conventional pruning to be pushed earlier into the training. To do this early, we further introduce an Early Pruning Indicator (EPI) that relies on sub-network architectural similarity and quickly triggers pruning when the sub-network's architecture stabilizes. Through extensive experiments on ImageNet, we show that EPI empowers a quick tracking of early training epochs suitable for pruning, offering same efficacy as an otherwise ``oracle'' grid-search that scans through epochs and requires orders of magnitude more compute. Our method yields $1.4\%$ top-1 accuracy boost over state-of-the-art pruning counterparts, cuts down training cost on GPU by $2.4\times$, hence offers a new efficiency-accuracy boundary for network pruning during training.

</details>

### Interspace Pruning: Using Adaptive Filter Representations to Improve Training of Sparse CNNs.
- **链接**: [arXiv:2203.07808](https://arxiv.org/abs/2203.07808) · 📚 被引 29
- **作者**: Paul Wimmer, Jens Mehnert, Alexandru Condurache
- **🏷️ 机构**: Automated Driving Research, Robert Bosch GmbH,Stuttgart,Germany,70469
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unstructured pruning is well suited to reduce the memory footprint of convolutional neural networks (CNNs), both at training and inference time. CNNs contain parameters arranged in $K \times K$ filters. Standard unstructured pruning (SP) reduces the memory footprint of CNNs by setting filter elements to zero, thereby specifying a fixed subspace that constrains the filter. Especially if pruning is applied before or during training, this induces a strong bias. To overcome this, we introduce interspace pruning (IP), a general tool to improve existing pruning methods. It uses filters represented in a dynamic interspace by linear combinations of an underlying adaptive filter basis (FB). For IP, FB coefficients are set to zero while un-pruned coefficients and FBs are trained jointly. In this work, we provide mathematical evidence for IP's superior performance and demonstrate that IP outperforms SP on all tested state-of-the-art unstructured pruning methods. Especially in challenging situations, like pruning for ImageNet or pruning to high sparsity, IP greatly exceeds SP with equal runtime and parameter costs. Finally, we show that advances of IP are due to improved trainability and superior generalization ability.

</details>

### Quarantine: Sparsity Can Uncover the Trojan Attack Trigger for Free.
- **链接**: [arXiv:2205.11819](https://arxiv.org/abs/2205.11819) · [代码](https://github.com/VITA-Group/Backdoor-LTH) · 📚 被引 13
- **作者**: Tianlong Chen, Zhenyu Zhang, Yihua Zhang, Shiyu Chang, Sijia Liu, Zhangyang Wang
- **🏷️ 机构**: University of Texas at Austin, Michigan State University, University of California,Santa Barbara
- **会议**: CVPR 2022

### Learning Extremely Lightweight and Robust Model with Differentiable Constraints on Sparsity and Condition Number.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19772-7_40) · 📚 被引 1
- **作者**: Xian Wei, Yangyu Xu, Yanhui Huang, Hairong Lv, Hai Lan, Mingsong Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

> Trojan attacks threaten deep neural networks (DNNs) by poisoning them to behave normally on most samples, yet to produce manipulated results for inputs attached with a particular trigger. Several works attempt to detect whether a given DNN has been injected with a specific trigger during the training. In a parallel line of research, the lottery ticket hypothesis reveals the existence of sparse subnetworks which are capable of reaching competitive performance as the dense network after independent training. Connecting these two dots, we investigate the problem of Trojan DNN detection from the brand new lens of sparsity, even when no clean training data is available. Our crucial observation is that the Trojan features are significantly more stable to network pruning than benign features. Leveraging that, we propose a novel Trojan network detection regime: first locating a "winning Trojan lottery ticket" which preserves nearly full Trojan information yet only chance-level performance on clean inputs; then recovering the trigger embedded in this already isolated subnetwork. Extensive experiments on various datasets, i.e., CIFAR-10, CIFAR-100, and ImageNet, with different network architectures, i.e., VGG-16, ResNet-18, ResNet-20s, and DenseNet-100 demonstrate the effectiveness of our proposal. Codes are available at https://github.com/VITA-Group/Backdoor-LTH.

</details>

### Attentive Fine-Grained Structured Sparsity for Image Restoration.
- **链接**: [arXiv:2204.12266](https://arxiv.org/abs/2204.12266) · [代码](https://github.com/JungHunOh/SLS_CVPR2022) · 📚 被引 12
- **作者**: Junghun Oh, Heewon Kim, Seungjun Nah, Cheeun Hong, Jonghyun Choi, Kyoung Mu Lee
- **🏷️ 机构**: ASRI,Dept. of ECE, Yonsei University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image restoration tasks have witnessed great performance improvement in recent years by developing large deep models. Despite the outstanding performance, the heavy computation demanded by the deep models has restricted the application of image restoration. To lift the restriction, it is required to reduce the size of the networks while maintaining accuracy. Recently, N:M structured pruning has appeared as one of the effective and practical pruning approaches for making the model efficient with the accuracy constraint. However, it fails to account for different computational complexities and performance requirements for different layers of an image restoration network. To further optimize the trade-off between the efficiency and the restoration accuracy, we propose a novel pruning method that determines the pruning ratio for N:M structured sparsity at each layer. Extensive experimental results on super-resolution and deblurring tasks demonstrate the efficacy of our method which outperforms previous pruning methods significantly. PyTorch implementation for the proposed methods is available at https://github.com/JungHunOh/SLS_CVPR2022.

</details>

## 🆕 增量新增

### Point Cloud Compression with Sibling Context and Surface Priors. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2205.00760](https://arxiv.org/abs/2205.00760)
- **作者**: Zhili Chen, Zian Qian, Sukai Wang, Qifeng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对大规模点云压缩中熵编码未能充分利用八叉树层级依赖和几何先验的问题。②提出一种基于八叉树的多级框架，利用兄弟节点子代、祖先和邻居上下文构建熵模型，并通过体素几何感知模块局部拟合二次曲面提供几何先验。③相比现有方法，增强了层级依赖建模和几何信息利用，解码时采用两步启发式策略提升重建质量。④在KITTI Odometry和nuScenes数据集上，比特率分别降低11-16%和12-14%，优于现有基线。
- **摘要（英）**: This paper addresses the problem of large-scale point cloud compression by proposing an octree-based multi-level framework with a novel entropy model that leverages sibling, ancestor, and neighbor contexts, along with locally fitted quadratic surfaces for geometric priors. It improves compression efficiency by 11-16% on KITTI Odometry and 12-14% on nuScenes, outperforming state-of-the-art baselines.
- **核心贡献**: 提出了一种结合层级上下文和几何先验的八叉树熵模型，显著提升点云压缩率。
- **创新点**: 利用兄弟节点子代上下文和局部二次曲面拟合作为几何先验，增强熵编码的预测能力。
- **结果**: 在KITTI和nuScenes上实现11-16%和12-14%的比特率降低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel octree-based multi-level framework for large-scale point cloud compression, which can organize sparse and unstructured point clouds in a memory-efficient way. In this framework, we propose a new entropy model that explores the hierarchical dependency in an octree using the context of siblings' children, ancestors, and neighbors to encode the occupancy information of each non-leaf octree node into a bitstream. Moreover, we locally fit quadratic surfaces with a voxel-based geometry-aware module to provide geometric priors in entropy encoding. These strong priors empower our entropy framework to encode the octree into a more compact bitstream. In the decoding stage, we apply a two-step heuristic strategy to restore point clouds with better reconstruction quality. The quantitative evaluation shows that our method outperforms state-of-the-art baselines with a bitrate improvement of 11-16% and 12-14% on the KITTI Odometry and nuScenes datasets, respectively.

</details>

### PPT: Token-Pruned Pose Transformer for Monocular and Multi-view Human Pose Estimation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2209.08194](https://arxiv.org/abs/2209.08194) · 📚 被引 76
- **作者**: Haoyu Ma, Zhe Wang, Yifei Chen, Deying Kong, Liangjian Chen, Xingwei Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对视觉Transformer在人体姿态估计中全局注意力计算开销大的问题，提出Token剪枝姿态Transformer（PPT），通过定位粗略人体掩膜并仅对选定token进行自注意力，降低计算量。进一步扩展到多视角姿态估计，提出人体区域融合策略，将所有人前景像素作为对应候选。在COCO和MPII上，PPT在保持精度的同时减少计算，在多视角数据集上实现高效融合并达到新最先进水平。
- **摘要（英）**: To reduce computational cost of global attention in vision transformers for pose estimation, this paper proposes token-Pruned Pose Transformer (PPT), which locates a rough human mask and performs self-attention only on selected tokens. Extended to multi-view with human area fusion, PPT matches accuracy of previous methods while reducing computation on COCO and MPII, and achieves state-of-the-art on multi-view datasets.
- **核心贡献**: 提出token剪枝机制和跨视角融合策略，提升姿态估计效率。
- **创新点**: 基于人体掩膜的token剪枝和人体区域融合。
- **结果**: 在COCO和MPII上精度匹配且计算减少，多视角数据集上达到新最先进水平。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the vision transformer and its variants have played an increasingly important role in both monocular and multi-view human pose estimation. Considering image patches as tokens, transformers can model the global dependencies within the entire image or across images from other views. However, global attention is computationally expensive. As a consequence, it is difficult to scale up these transformer-based methods to high-resolution features and many views. In this paper, we propose the token-Pruned Pose Transformer (PPT) for 2D human pose estimation, which can locate a rough human mask and performs self-attention only within selected tokens. Furthermore, we extend our PPT to multi-view human pose estimation. Built upon PPT, we propose a new cross-view fusion strategy, called human area fusion, which considers all human foreground pixels as corresponding candidates. Experimental results on COCO and MPII demonstrate that our PPT can match the accuracy of previous pose transformer methods while reducing the computation. Moreover, experiments on Human 3.6M and Ski-Pose demonstrate that our Multi-view PPT can efficiently fuse cues from multiple views and achieve new state-of-the-art results.

</details>

### SPViT: Enabling Faster Vision Transformers via Latency-Aware Soft Token Pruning. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_37) · 📚 被引 160
- **作者**: Zhenglun Kong, Peiyan Dong, Xiaolong Ma, Xin Meng, Wei Niu, Mengshu Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对视觉Transformer推理延迟高的问题，提出了延迟感知的软令牌剪枝方法SPViT。该方法通过评估每个令牌对最终预测的贡献，并考虑硬件延迟，动态剪枝不重要的令牌，从而在保持精度的同时加速推理。实验表明，SPViT在图像分类和检测任务上实现了显著的加速比，同时精度损失极小。
- **摘要（英）**: To reduce the inference latency of Vision Transformers, this paper proposes SPViT, a latency-aware soft token pruning method. It dynamically prunes unimportant tokens based on their contribution to predictions and hardware latency, achieving significant speedup with minimal accuracy drop on classification and detection tasks.
- **核心贡献**: 提出延迟感知的软令牌剪枝方法，有效加速ViT推理。
- **创新点**: 将硬件延迟纳入令牌剪枝决策，实现精度与速度的更好权衡。
- **结果**: 在多个任务上实现显著加速，精度损失极小。

### SuperTickets: Drawing Task-Agnostic Lottery Tickets from Supernets via Jointly Architecture Searching and Parameter Pruning.
- **链接**: [arXiv:2207.03677](https://arxiv.org/abs/2207.03677) · 📚 被引 8
- **作者**: Haoran You, Baopu Li, Zhanyi Sun, Xu Ouyang, Yingyan Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has demonstrated amazing success in searching for efficient deep neural networks (DNNs) from a given supernet. In parallel, the lottery ticket hypothesis has shown that DNNs contain small subnetworks that can be trained from scratch to achieve a comparable or higher accuracy than original DNNs. As such, it is currently a common practice to develop efficient DNNs via a pipeline of first search and then prune. Nevertheless, doing so often requires a search-train-prune-retrain process and thus prohibitive computational cost. In this paper, we discover for the first time that both efficient DNNs and their lottery subnetworks (i.e., lottery tickets) can be directly identified from a supernet, which we term as SuperTickets, via a two-in-one training scheme with jointly architecture searching and parameter pruning. Moreover, we develop a progressive and unified SuperTickets identification strategy that allows the connectivity of subnetworks to change during supernet training, achieving better accuracy and efficiency trade-offs than conventional sparse training. Finally, we evaluate whether such identified SuperTickets drawn from one task can transfer well to other tasks, validating their potential of handling multiple tasks simultaneously. Extensive experiments and ablation studies on three tasks and four benchmark datasets validate that our proposed SuperTickets achieve boosted accuracy and efficiency trade-offs than both typical NAS and pruning pipelines, regardless of having retraining or not. Codes and pretrained models are available at https://github.com/RICE-EIC/SuperTickets.

</details>

### Towards Ultra Low Latency Spiking Neural Networks for Vision and Sequential Tasks Using Temporal Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_42) · 📚 被引 30
- **作者**: Sayeed Shafayet Chowdhury, Nitin Rathi, Kaushik Roy
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Bayesian Optimization with Clustering and Rollback for CNN Auto Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20050-2_29)
- **作者**: Hanwei Fan, Jiandong Mu, Wei Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Interpretations Steered Network Pruning via Amortized Inferred Saliency Maps.
- **链接**: [arXiv:2209.02869](https://arxiv.org/abs/2209.02869) · 📚 被引 13
- **作者**: Alireza Ganjdanesh, Shangqian Gao, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolutional Neural Networks (CNNs) compression is crucial to deploying these models in edge devices with limited resources. Existing channel pruning algorithms for CNNs have achieved plenty of success on complex models. They approach the pruning problem from various perspectives and use different metrics to guide the pruning process. However, these metrics mainly focus on the model's `outputs' or `weights' and neglect its `interpretations' information. To fill in this gap, we propose to address the channel pruning problem from a novel perspective by leveraging the interpretations of a model to steer the pruning process, thereby utilizing information from both inputs and outputs of the model. However, existing interpretation methods cannot get deployed to achieve our goal as either they are inefficient for pruning or may predict non-coherent explanations. We tackle this challenge by introducing a selector model that predicts real-time smooth saliency masks for pruned models. We parameterize the distribution of explanatory masks by Radial Basis Function (RBF)-like functions to incorporate geometric prior of natural images in our selector model's inductive bias. Thus, we can obtain compact representations of explanations to reduce the computational costs of our pruning method. We leverage our selector model to steer the network pruning by maximizing the similarity of explanatory representations for the pruned and original models. Extensive experiments on CIFAR-10 and ImageNet benchmark datasets demonstrate the efficacy of our proposed method. Our implementations are available at \url{https://github.com/Alii-Ganjj/InterpretationsSteeredPruning}

</details>

### Disentangled Differentiable Network Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_20) · 📚 被引 14
- **作者**: Shangqian Gao, Feihu Huang, Yanfu Zhang, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Filter Pruning via Feature Discrimination in Deep Neural Networks.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_15)
- **作者**: Zhiqiang He, Yaguan Qian, Yuqi Wang, Bin Wang, Xiaohui Guan, Zhaoquan Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Soft Masking for Cost-Constrained Channel Pruning.
- **链接**: [arXiv:2211.02206](https://arxiv.org/abs/2211.02206) · 📚 被引 15
- **作者**: Ryan Humble, Maying Shen, Jorge Albericio Latorre, Eric Darve, José M. Álvarez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured channel pruning has been shown to significantly accelerate inference time for convolution neural networks (CNNs) on modern hardware, with a relatively minor loss of network accuracy. Recent works permanently zero these channels during training, which we observe to significantly hamper final accuracy, particularly as the fraction of the network being pruned increases. We propose Soft Masking for cost-constrained Channel Pruning (SMCP) to allow pruned channels to adaptively return to the network while simultaneously pruning towards a target cost constraint. By adding a soft mask re-parameterization of the weights and channel pruning from the perspective of removing input channels, we allow gradient updates to previously pruned channels and the opportunity for the channels to later return to the network. We then formulate input channel pruning as a global resource allocation problem. Our method outperforms prior works on both the ImageNet classification and PASCAL VOC detection datasets.

</details>

### CPrune: Compiler-Informed Model Pruning for Efficient Target-Aware DNN Execution.
- **链接**: [arXiv:2207.01260](https://arxiv.org/abs/2207.01260) · 📚 被引 5
- **作者**: Taeho Kim, Yongin Kwon, Jemin Lee, Taeho Kim, Sangtae Ha
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mobile devices run deep learning models for various purposes, such as image classification and speech recognition. Due to the resource constraints of mobile devices, researchers have focused on either making a lightweight deep neural network (DNN) model using model pruning or generating an efficient code using compiler optimization. Surprisingly, we found that the straightforward integration between model compression and compiler auto-tuning often does not produce the most efficient model for a target device. We propose CPrune, a compiler-informed model pruning for efficient target-aware DNN execution to support an application with a required target accuracy. CPrune makes a lightweight DNN model through informed pruning based on the structural information of subgraphs built during the compiler tuning process. Our experimental results show that CPrune increases the DNN execution speed up to 2.73x compared to the state-of-the-art TVM auto-tune while satisfying the accuracy requirement.

</details>

### Ensemble Knowledge Guided Sub-network Search and Fine-Tuning for Filter Pruning.
- **链接**: [arXiv:2203.02651](https://arxiv.org/abs/2203.02651)
- **作者**: Seunghyun Lee, Byung Cheol Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional NAS-based pruning algorithms aim to find the sub-network with the best validation performance. However, validation performance does not successfully represent test performance, i.e., potential performance. Also, although fine-tuning the pruned network to restore the performance drop is an inevitable process, few studies have handled this issue. This paper provides a novel Ensemble Knowledge Guidance (EKG) to solve both problems at once. First, we experimentally prove that the fluctuation of loss landscape can be an effective metric to evaluate the potential performance. In order to search a sub-network with the smoothest loss landscape at a low cost, we employ EKG as a search reward. EKG utilized for the following search iteration is composed of the ensemble knowledge of interim sub-networks, i.e., the by-products of the sub-network evaluation. Next, we reuse EKG to provide a gentle and informative guidance to the pruned network while fine-tuning the pruned network. Since EKG is implemented as a memory bank in both phases, it requires a negligible cost. For example, when pruning and training ResNet-50, just 315 GPU hours are required to remove around 45.04% of FLOPS without any performance degradation, which can operate even on a low-spec workstation. the implemented code is available at https://github.com/sseung0703/EKG.

</details>

### FairGRAPE: Fairness-Aware GRAdient Pruning mEthod for Face Attribute Classification.
- **链接**: [arXiv:2207.10888](https://arxiv.org/abs/2207.10888) · 📚 被引 29
- **作者**: Xiaofeng Lin, Seungbae Kim, Jungseock Joo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing pruning techniques preserve deep neural networks' overall ability to make correct predictions but may also amplify hidden biases during the compression process. We propose a novel pruning method, Fairness-aware GRAdient Pruning mEthod (FairGRAPE), that minimizes the disproportionate impacts of pruning on different sub-groups. Our method calculates the per-group importance of each model weight and selects a subset of weights that maintain the relative between-group total importance in pruning. The proposed method then prunes network edges with small importance values and repeats the procedure by updating importance values. We demonstrate the effectiveness of our method on four different datasets, FairFace, UTKFace, CelebA, and ImageNet, for the tasks of face attribute classification where our method reduces the disparity in performance degradation by up to 90% compared to the state-of-the-art pruning algorithms. Our method is substantially more effective in a setting with a high pruning rate (99%). The code and dataset used in the experiments are available at https://github.com/Bernardo1998/FairGRAPE

</details>

### Multi-granularity Pruning for Model Acceleration on Mobile Devices.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_29) · 📚 被引 5
- **作者**: Tianli Zhao, Xi Sheryl Zhang, Wentao Zhu, Jiaxing Wang, Sen Yang, Ji Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Prospect Pruning: Finding Trainable Weights at Initialization using Meta-Gradients.
- **链接**: [arXiv:2202.08132](https://arxiv.org/abs/2202.08132)
- **作者**: Milad Alizadeh, Shyam A. Tailor, Luisa M. Zintgraf, Joost van Amersfoort, Sebastian Farquhar, Nicholas Donald Lane et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning neural networks at initialization would enable us to find sparse models that retain the accuracy of the original network while consuming fewer computational resources for training and inference. However, current methods are insufficient to enable this optimization and lead to a large degradation in model performance. In this paper, we identify a fundamental limitation in the formulation of current methods, namely that their saliency criteria look at a single step at the start of training without taking into account the trainability of the network. While pruning iteratively and gradually has been shown to improve pruning performance, explicit consideration of the training stage that will immediately follow pruning has so far been absent from the computation of the saliency criterion. To overcome the short-sightedness of existing methods, we propose Prospect Pruning (ProsPr), which uses meta-gradients through the first few steps of optimization to determine which weights to prune. ProsPr combines an estimate of the higher-order effects of pruning on the loss and the optimization trajectory to identify the trainable sub-network. Our method achieves state-of-the-art pruning performance on a variety of vision classification tasks, with less data and in a single shot compared to existing pruning-at-initialization methods.

</details>

### The Unreasonable Effectiveness of Random Pruning: Return of the Most Naive Baseline for Sparse Training.
- **链接**: [arXiv:2202.02643](https://arxiv.org/abs/2202.02643)
- **作者**: Shiwei Liu, Tianlong Chen, Xiaohan Chen, Li Shen, Decebal Constantin Mocanu, Zhangyang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Random pruning is arguably the most naive way to attain sparsity in neural networks, but has been deemed uncompetitive by either post-training pruning or sparse training. In this paper, we focus on sparse training and highlight a perhaps counter-intuitive finding, that random pruning at initialization can be quite powerful for the sparse training of modern neural networks. Without any delicate pruning criteria or carefully pursued sparsity structures, we empirically demonstrate that sparsely training a randomly pruned network from scratch can match the performance of its dense equivalent. There are two key factors that contribute to this revival: (i) the network sizes matter: as the original dense networks grow wider and deeper, the performance of training a randomly pruned sparse network will quickly grow to matching that of its dense equivalent, even at high sparsity ratios; (ii) appropriate layer-wise sparsity ratios can be pre-chosen for sparse training, which shows to be another important performance booster. Simple as it looks, a randomly pruned subnetwork of Wide ResNet-50 can be sparsely trained to outperforming a dense Wide ResNet-50, on ImageNet. We also observed such randomly pruned networks outperform dense counterparts in other favorable aspects, such as out-of-distribution detection, uncertainty estimation, and adversarial robustness. Overall, our results strongly suggest there is larger-than-expected room for sparse training at scale, and the benefits of sparsity might be more universal beyond carefully designed pruning. Our source code can be found at https://github.com/VITA-Group/Random_Pruning.

</details>

### Learning Pruning-Friendly Networks via Frank-Wolfe: One-Shot, Any-Sparsity, And No Retraining.
- **链接**: [出版页](https://openreview.net/forum?id=O1DEtITim__)
- **作者**: Lu Miao, Xiaolong Luo, Tianlong Chen, Wuyang Chen, Dong Liu, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### SOSP: Efficiently Capturing Global Correlations by Second-Order Structured Pruning.
- **链接**: [arXiv:2110.11395](https://arxiv.org/abs/2110.11395)
- **作者**: Manuel Nonnenmacher, Thomas Pfeil, Ingo Steinwart, David Reeb
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning neural networks reduces inference time and memory costs. On standard hardware, these benefits will be especially prominent if coarse-grained structures, like feature maps, are pruned. We devise two novel saliency-based methods for second-order structured pruning (SOSP) which include correlations among all structures and layers. Our main method SOSP-H employs an innovative second-order approximation, which enables saliency evaluations by fast Hessian-vector products. SOSP-H thereby scales like a first-order method despite taking into account the full Hessian. We validate SOSP-H by comparing it to our second method SOSP-I that uses a well-established Hessian approximation, and to numerous state-of-the-art methods. While SOSP-H performs on par or better in terms of accuracy, it has clear advantages in terms of scalability and efficiency. This allowed us to scale SOSP-H to large-scale vision tasks, even though it captures correlations across all layers of the network. To underscore the global nature of our pruning methods, we evaluate their performance not only by removing structures from a pretrained network, but also by detecting architectural bottlenecks. We show that our algorithms allow to systematically reveal architectural bottlenecks, which we then remove to further increase the accuracy of the networks.

</details>

### An Operator Theoretic View On Pruning Deep Neural Networks.
- **链接**: [出版页](https://openreview.net/forum?id=pWBNOgdeURp)
- **作者**: William T. Redman, Maria Fonoberova, Ryan Mohr, Yannis G. Kevrekidis, Igor Mezic
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Learning Efficient Image Super-Resolution Networks via Structure-Regularized Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=AjGC97Aofee)
- **作者**: Yulun Zhang, Huan Wang, Can Qin, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Revisit Kernel Pruning with Lottery Regulated Grouped Convolutions.
- **链接**: [出版页](https://openreview.net/forum?id=LdEhiMG9WLO)
- **作者**: Shaochen (Henry) Zhong, Guanqun Zhang, Ningjia Huang, Shuai Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Sparsity Winning Twice: Better Robust Generalization from More Efficient Training.
- **链接**: [arXiv:2202.09844](https://arxiv.org/abs/2202.09844)
- **作者**: Tianlong Chen, Zhenyu Zhang, Pengjun Wang, Santosh Balachandra, Haoyu Ma, Zehao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies demonstrate that deep networks, even robustified by the state-of-the-art adversarial training (AT), still suffer from large robust generalization gaps, in addition to the much more expensive training costs than standard training. In this paper, we investigate this intriguing problem from a new perspective, i.e., injecting appropriate forms of sparsity during adversarial training. We introduce two alternatives for sparse adversarial training: (i) static sparsity, by leveraging recent results from the lottery ticket hypothesis to identify critical sparse subnetworks arising from the early training; (ii) dynamic sparsity, by allowing the sparse subnetwork to adaptively adjust its connectivity pattern (while sticking to the same sparsity ratio) throughout training. We find both static and dynamic sparse methods to yield win-win: substantially shrinking the robust generalization gap and alleviating the robust overfitting, meanwhile significantly saving training and inference FLOPs. Extensive experiments validate our proposals with multiple network architectures on diverse datasets, including CIFAR-10/100 and Tiny-ImageNet. For example, our methods reduce robust generalization gap and overfitting by 34.44% and 4.02%, with comparable robust/standard accuracy boosts and 87.83%/87.82% training/inference FLOPs savings on CIFAR-100 with ResNet-18. Besides, our approaches can be organically combined with existing regularizers, establishing new state-of-the-art results in AT. Codes are available in https://github.com/VITA-Group/Sparsity-Win-Robust-Generalization.

</details>

### Deep Ensembling with No Overhead for either Training or Testing: The All-Round Blessings of Dynamic Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=RLtqs6pzj1-)
- **作者**: Shiwei Liu, Tianlong Chen, Zahra Atashgahi, Xiaohan Chen, Ghada Sokar, Elena Mocanu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Encoding Weights of Irregular Sparsity for Fixed-to-Fixed Model Compression.
- **链接**: [出版页](https://openreview.net/forum?id=Vs5NK44aP9P)
- **作者**: Baeseong Park, Se Jung Kwon, Daehwan Oh, Byeongwook Kim, Dongsoo Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### ZeroFL: Efficient On-Device Training for Federated Learning with Local Sparsity.
- **链接**: [arXiv:2208.02507](https://arxiv.org/abs/2208.02507)
- **作者**: Xinchi Qiu, Javier Fernández-Marqués, Pedro P. B. de Gusmao, Yan Gao, Titouan Parcollet, Nicholas Donald Lane
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> When the available hardware cannot meet the memory and compute requirements to efficiently train high performing machine learning models, a compromise in either the training quality or the model complexity is needed. In Federated Learning (FL), nodes are orders of magnitude more constrained than traditional server-grade hardware and are often battery powered, severely limiting the sophistication of models that can be trained under this paradigm. While most research has focused on designing better aggregation strategies to improve convergence rates and in alleviating the communication costs of FL, fewer efforts have been devoted to accelerating on-device training. Such stage, which repeats hundreds of times (i.e. every round) and can involve thousands of devices, accounts for the majority of the time required to train federated models and, the totality of the energy consumption at the client side. In this work, we present the first study on the unique aspects that arise when introducing sparsity at training time in FL workloads. We then propose ZeroFL, a framework that relies on highly sparse operations to accelerate on-device training. Models trained with ZeroFL and 95% sparsity achieve up to 2.3% higher accuracy compared to competitive baselines obtained from adapting a state-of-the-art sparse training framework to the FL setting.

</details>

### The Combinatorial Brain Surgeon: Pruning Weights That Cancel One Another in Neural Networks.
- **链接**: [arXiv:2203.04466](https://arxiv.org/abs/2203.04466)
- **作者**: Xin Yu, Thiago Serra, Srikumar Ramalingam, Shandian Zhe
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Linearity Grafting: Relaxed Neuron Pruning Helps Certifiable Robustness.
- **链接**: [arXiv:2206.07839](https://arxiv.org/abs/2206.07839)
- **作者**: Tianlong Chen, Huan Zhang, Zhenyu Zhang, Shiyu Chang, Sijia Liu, Pin-Yu Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### SPDY: Accurate Pruning with Speedup Guarantees.
- **链接**: [arXiv:2201.13096](https://arxiv.org/abs/2201.13096)
- **作者**: Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Sparse Double Descent: Where Network Pruning Aggravates Overfitting.
- **链接**: [arXiv:2206.08684](https://arxiv.org/abs/2206.08684)
- **作者**: Zheng He, Zeke Xie, Quanzhi Zhu, Zengchang Qin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### PAC-Net: A Model Pruning Approach to Inductive Transfer Learning.
- **链接**: [arXiv:2206.05703](https://arxiv.org/abs/2206.05703)
- **作者**: Sanghoon Myung, In Huh, Wonik Jang, Jae Myung Choe, Jisu Ryu, Daesin Kim et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Neural Network Pruning Denoises the Features and Makes Local Connectivity Emerge in Visual Tasks.
- **链接**: [出版页](https://proceedings.mlr.press/v162/pellegrini22a.html)
- **作者**: Franco Pellegrini, Giulio Biroli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Winning the Lottery Ahead of Time: Efficient Early Network Pruning.
- **链接**: [arXiv:2206.10451](https://arxiv.org/abs/2206.10451)
- **作者**: John Rachwan, Daniel Zügner, Bertrand Charpentier, Simon Geisler, Morgane Ayle, Stephan Günnemann
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Topology-Aware Network Pruning using Multi-stage Graph Embedding and Reinforcement Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v162/yu22e.html)
- **作者**: Sixing Yu, Arya Mazaheri, Ali Jannesari
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### PLATON: Pruning Large Transformer Models with Upper Confidence Bound of Weight Importance.
- **链接**: [arXiv:2206.12562](https://arxiv.org/abs/2206.12562)
- **作者**: Qingru Zhang, Simiao Zuo, Chen Liang, Alexander Bukharin, Pengcheng He, Weizhu Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### SpeqNets: Sparsity-aware permutation-equivariant graph networks.
- **链接**: [arXiv:2203.13913](https://arxiv.org/abs/2203.13913)
- **作者**: Christopher Morris, Gaurav Rattan, Sandra Kiefer, Siamak Ravanbakhsh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While (message-passing) graph neural networks have clear limitations in approximating permutation-equivariant functions over graphs or general relational data, more expressive, higher-order graph neural networks do not scale to large graphs. They either operate on $k$-order tensors or consider all $k$-node subgraphs, implying an exponential dependence on $k$ in memory requirements, and do not adapt to the sparsity of the graph. By introducing new heuristics for the graph isomorphism problem, we devise a class of universal, permutation-equivariant graph networks, which, unlike previous architectures, offer a fine-grained control between expressivity and scalability and adapt to the sparsity of the graph. These architectures lead to vastly reduced computation times compared to standard higher-order graph networks in the supervised node- and graph-level classification and regression regime while significantly improving over standard graph neural network and graph kernel architectures in terms of predictive performance.

</details>

### Sparsity in Partially Controllable Linear Systems.
- **链接**: [arXiv:2110.06150](https://arxiv.org/abs/2110.06150)
- **作者**: Yonathan Efroni, Sham M. Kakade, Akshay Krishnamurthy, Cyril Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A fundamental concept in control theory is that of controllability, where any system state can be reached through an appropriate choice of control inputs. Indeed, a large body of classical and modern approaches are designed for controllable linear dynamical systems. However, in practice, we often encounter systems in which a large set of state variables evolve exogenously and independently of the control inputs; such systems are only partially controllable. The focus of this work is on a large class of partially controllable linear dynamical systems, specified by an underlying sparsity pattern. Our main results establish structural conditions and finite-sample guarantees for learning to control such systems. In particular, our structural results characterize those state variables which are irrelevant for optimal control, an analysis which departs from classical control techniques. Our algorithmic results adapt techniques from high-dimensional statistics -- specifically soft-thresholding and semiparametric least-squares -- to exploit the underlying sparsity pattern in order to obtain finite-sample guarantees that significantly improve over those based on certainty-equivalence. We also corroborate these theoretical improvements over certainty-equivalent control through a simulation study.

</details>

### Leverage Score Sampling for Tensor Product Matrices in Input Sparsity Time.
- **链接**: [arXiv:2202.04515](https://arxiv.org/abs/2202.04515)
- **作者**: David P. Woodruff, Amir Zandieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an input sparsity time sampling algorithm that can spectrally approximate the Gram matrix corresponding to the $q$-fold column-wise tensor product of $q$ matrices using a nearly optimal number of samples, improving upon all previously known methods by poly$(q)$ factors. Furthermore, for the important special case of the $q$-fold self-tensoring of a dataset, which is the feature matrix of the degree-$q$ polynomial kernel, the leading term of our method's runtime is proportional to the size of the input dataset and has no dependence on $q$. Previous techniques either incur poly$(q)$ slowdowns in their runtime or remove the dependence on $q$ at the expense of having sub-optimal target dimension, and depend quadratically on the number of data-points in their runtime. Our sampling technique relies on a collection of $q$ partially correlated random projections which can be simultaneously applied to a dataset $X$ in total time that only depends on the size of $X$, and at the same time their $q$-fold Kronecker product acts as a near-isometry for any fixed vector in the column span of $X^{\otimes q}$. We also show that our sampling methods generalize to other classes of kernels beyond polynomial, such as Gaussian and Neural Tangent kernels.

</details>

### Spatial Pruned Sparse Convolution for Efficient 3D Object Detection.
- **链接**: [arXiv:2209.14201](https://arxiv.org/abs/2209.14201) · 📚 被引 3
- **作者**: Jianhui Liu, Yukang Chen, Xiaoqing Ye, Zhuotao Tian, Xiao Tan, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D scenes are dominated by a large number of background points, which is redundant for the detection task that mainly needs to focus on foreground objects. In this paper, we analyze major components of existing sparse 3D CNNs and find that 3D CNNs ignore the redundancy of data and further amplify it in the down-sampling process, which brings a huge amount of extra and unnecessary computational overhead. Inspired by this, we propose a new convolution operator named spatial pruned sparse convolution (SPS-Conv), which includes two variants, spatial pruned submanifold sparse convolution (SPSS-Conv) and spatial pruned regular sparse convolution (SPRS-Conv), both of which are based on the idea of dynamically determining crucial areas for redundancy reduction. We validate that the magnitude can serve as important cues to determine crucial areas which get rid of the extra computations of learning-based methods. The proposed modules can easily be incorporated into existing sparse 3D CNNs without extra architectural modifications. Extensive experiments on the KITTI, Waymo and nuScenes datasets demonstrate that our method can achieve more than 50% reduction in GFLOPs without compromising the performance.

</details>

### VTC-LFC: Vision Transformer Compression with Low-Frequency Components.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5a8177df23bdcc15a02a6739f5b9dd4a-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zhenyu Wang, Hao Luo, Pichao Wang, Feng Ding, Fan Wang, Hao Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Recall Distortion in Neural Network Pruning and the Undecayed Pruning Algorithm.
- **链接**: [arXiv:2206.02976](https://arxiv.org/abs/2206.02976) · 📚 被引 2
- **作者**: Aidan Good, Jiaqi Lin, Xin Yu, Hannah Sieg, Mikey Ferguson, Shandian Zhe et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning techniques have been successfully used in neural networks to trade accuracy for sparsity. However, the impact of network pruning is not uniform: prior work has shown that the recall for underrepresented classes in a dataset may be more negatively affected. In this work, we study such relative distortions in recall by hypothesizing an intensification effect that is inherent to the model. Namely, that pruning makes recall relatively worse for a class with recall below accuracy and, conversely, that it makes recall relatively better for a class with recall above accuracy. In addition, we propose a new pruning algorithm aimed at attenuating such effect. Through statistical analysis, we have observed that intensification is less severe with our algorithm but nevertheless more pronounced with relatively more difficult tasks, less complex models, and higher pruning ratios. More surprisingly, we conversely observe a de-intensification effect with lower pruning ratios, which indicates that moderate pruning may have a corrective effect to such distortions.

</details>

### Pruning has a disparate impact on model accuracy.
- **链接**: [arXiv:2205.13574](https://arxiv.org/abs/2205.13574) · 📚 被引 6
- **作者**: Cuong Tran, Ferdinando Fioretto, Jung-Eun Kim, Rakshit Naidu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Network pruning is a widely-used compression technique that is able to significantly scale down overparameterized models with minimal loss of accuracy. This paper shows that pruning may create or exacerbate disparate impacts. The paper sheds light on the factors to cause such disparities, suggesting differences in gradient norms and distance to decision boundary across groups to be responsible for this critical issue. It analyzes these factors in detail, providing both theoretical and empirical support, and proposes a simple, yet effective, solution that mitigates the disparate impacts caused by pruning.

</details>

### Sparse Probabilistic Circuits via Pruning and Growing.
- **链接**: [arXiv:2211.12551](https://arxiv.org/abs/2211.12551) · 📚 被引 5
- **作者**: Meihua Dang, Anji Liu, Guy Van den Broeck
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Probabilistic circuits (PCs) are a tractable representation of probability distributions allowing for exact and efficient computation of likelihoods and marginals. There has been significant recent progress on improving the scale and expressiveness of PCs. However, PC training performance plateaus as model size increases. We discover that most capacity in existing large PC structures is wasted: fully-connected parameter layers are only sparsely used. We propose two operations: pruning and growing, that exploit the sparsity of PC structures. Specifically, the pruning operation removes unimportant sub-networks of the PC for model compression and comes with theoretical guarantees. The growing operation increases model capacity by increasing the size of the latent space. By alternatingly applying pruning and growing, we increase the capacity that is meaningfully used, allowing us to significantly scale up PC learning. Empirically, our learner achieves state-of-the-art likelihoods on MNIST-family image datasets and on Penn Tree Bank language data compared to other PC learners and less tractable deep generative models such as flow-based models and variational autoencoders (VAEs).

</details>

### Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning.
- **链接**: [arXiv:2208.11580](https://arxiv.org/abs/2208.11580) · 📚 被引 22
- **作者**: Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of model compression for deep neural networks (DNNs) in the challenging one-shot/post-training setting, in which we are given an accurate trained model, and must compress it without any retraining, based only on a small amount of calibration input data. This problem has become popular in view of the emerging software and hardware support for executing models compressed via pruning and/or quantization with speedup, and well-performing solutions have been proposed independently for both compression approaches. In this paper, we introduce a new compression framework which covers both weight pruning and quantization in a unified setting, is time- and space-efficient, and considerably improves upon the practical performance of existing post-training methods. At the technical level, our approach is based on an exact and efficient realization of the classical Optimal Brain Surgeon (OBS) framework of [LeCun, Denker, and Solla, 1990] extended to also cover weight quantization at the scale of modern DNNs. From the practical perspective, our experimental results show that it can improve significantly upon the compression-accuracy trade-offs of existing post-training methods, and that it can enable the accurate compound application of both pruning and quantization in a post-training setting.

</details>

### Data-Efficient Structured Pruning via Submodular Optimization.
- **链接**: [arXiv:2203.04940](https://arxiv.org/abs/2203.04940) · 📚 被引 2
- **作者**: Marwa El Halabi, Suraj Srinivas, Simon Lacoste-Julien
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning is an effective approach for compressing large pre-trained neural networks without significantly affecting their performance. However, most current structured pruning methods do not provide any performance guarantees, and often require fine-tuning, which makes them inapplicable in the limited-data regime. We propose a principled data-efficient structured pruning method based on submodular optimization. In particular, for a given layer, we select neurons/channels to prune and corresponding new weights for the next layer, that minimize the change in the next layer's input induced by pruning. We show that this selection problem is a weakly submodular maximization problem, thus it can be provably approximated using an efficient greedy algorithm. Our method is guaranteed to have an exponentially decreasing error between the original model and the pruned model outputs w.r.t the pruned size, under reasonable assumptions. It is also one of the few methods in the literature that uses only a limited-number of training data and no labels. Our experimental results demonstrate that our method outperforms state-of-the-art methods in the limited-data regime.

</details>

### Pruning's Effect on Generalization Through the Lens of Training and Regularization.
- **链接**: [arXiv:2210.13738](https://arxiv.org/abs/2210.13738) · 📚 被引 3
- **作者**: Tian Jin, Michael Carbin, Daniel M. Roy, Jonathan Frankle, Gintare Karolina Dziugaite
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Practitioners frequently observe that pruning improves model generalization. A long-standing hypothesis based on bias-variance trade-off attributes this generalization improvement to model size reduction. However, recent studies on over-parameterization characterize a new model size regime, in which larger models achieve better generalization. Pruning models in this over-parameterized regime leads to a contradiction -- while theory predicts that reducing model size harms generalization, pruning to a range of sparsities nonetheless improves it. Motivated by this contradiction, we re-examine pruning's effect on generalization empirically. We show that size reduction cannot fully account for the generalization-improving effect of standard pruning algorithms. Instead, we find that pruning leads to better training at specific sparsities, improving the training loss over the dense model. We find that pruning also leads to additional regularization at other sparsities, reducing the accuracy degradation due to noisy examples over the dense model. Pruning extends model training time and reduces model size. These two factors improve training and add regularization respectively. We empirically demonstrate that both factors are essential to fully explaining pruning's impact on generalization.

</details>

### A Fast Post-Training Pruning Framework for Transformers.
- **链接**: [arXiv:2204.09656](https://arxiv.org/abs/2204.09656) · 📚 被引 6
- **作者**: Woosuk Kwon, Sehoon Kim, Michael W. Mahoney, Joseph Hassoun, Kurt Keutzer, Amir Gholami
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning is an effective way to reduce the huge inference cost of Transformer models. However, prior work on pruning Transformers requires retraining the models. This can add high training cost and high complexity to model deployment, making it difficult to use in many practical situations. To address this, we propose a fast post-training pruning framework for Transformers that does not require any retraining. Given a resource constraint and a sample dataset, our framework automatically prunes the Transformer model using structured sparsity methods. To retain high accuracy without retraining, we introduce three novel techniques: (i) a lightweight mask search algorithm that finds which heads and filters to prune based on the Fisher information; (ii) mask rearrangement that complements the search algorithm; and (iii) mask tuning that reconstructs the output activations for each layer. We apply our method to BERT-base and DistilBERT, and we evaluate its effectiveness on GLUE and SQuAD benchmarks. Our framework achieves up to 2.0x reduction in FLOPs and 1.56x speedup in inference latency, while maintaining < 1% loss in accuracy. Importantly, our framework prunes Transformers in less than 3 minutes on a single GPU, which is over two orders of magnitude faster than existing pruning approaches that retrain the models.

</details>

### Robust Binary Models by Pruning Randomly-initialized Networks.
- **链接**: [arXiv:2202.01341](https://arxiv.org/abs/2202.01341) · 📚 被引 1
- **作者**: Chen Liu, Ziqi Zhao, Sabine Süsstrunk, Mathieu Salzmann
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robustness to adversarial attacks was shown to require a larger model capacity, and thus a larger memory footprint. In this paper, we introduce an approach to obtain robust yet compact models by pruning randomly-initialized binary networks. Unlike adversarial training, which learns the model parameters, we initialize the model parameters as either +1 or -1, keep them fixed, and find a subnetwork structure that is robust to attacks. Our method confirms the Strong Lottery Ticket Hypothesis in the presence of adversarial attacks, and extends this to binary networks. Furthermore, it yields more compact networks with competitive performance than existing works by 1) adaptively pruning different network layers; 2) exploiting an effective binary initialization scheme; 3) incorporating a last batch normalization layer to improve training stability. Our experiments demonstrate that our approach not only always outperforms the state-of-the-art robust binary networks, but also can achieve accuracy better than full-precision ones on some datasets. Finally, we show the structured patterns of our pruned binary networks.

</details>

### Structural Pruning via Latency-Saliency Knapsack.
- **链接**: [arXiv:2210.06659](https://arxiv.org/abs/2210.06659) · 📚 被引 2
- **作者**: Maying Shen, Hongxu Yin, Pavlo Molchanov, Lei Mao, Jianna Liu, José M. Álvarez
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structural pruning can simplify network architecture and improve inference speed. We propose Hardware-Aware Latency Pruning (HALP) that formulates structural pruning as a global resource allocation optimization problem, aiming at maximizing the accuracy while constraining latency under a predefined budget on targeting device. For filter importance ranking, HALP leverages latency lookup table to track latency reduction potential and global saliency score to gauge accuracy drop. Both metrics can be evaluated very efficiently during pruning, allowing us to reformulate global structural pruning under a reward maximization problem given target constraint. This makes the problem solvable via our augmented knapsack solver, enabling HALP to surpass prior work in pruning efficacy and accuracy-efficiency trade-off. We examine HALP on both classification and detection tasks, over varying networks, on ImageNet and VOC datasets, on different platforms. In particular, for ResNet-50/-101 pruning on ImageNet, HALP improves network throughput by $1.60\times$/$1.90\times$ with $+0.3\%$/$-0.2\%$ top-1 accuracy changes, respectively. For SSD pruning on VOC, HALP improves throughput by $1.94\times$ with only a $0.56$ mAP drop. HALP consistently outperforms prior art, sometimes by large margins. Project page at https://halp-neurips.github.io/.

</details>

### Beyond neural scaling laws: beating power law scaling via data pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7b75da9b61eda40fa35453ee5d077df6-Abstract-Conference.html) · 📚 被引 31
- **作者**: Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, Ari Morcos
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Pruning Neural Networks via Coresets and Convex Geometry: Towards No Assumptions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/f7fc38fdd95fd146a471791b93ff9f12-Abstract-Conference.html) · 📚 被引 1
- **作者**: Murad Tukan, Loay Mualem, Alaa Maalouf
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Advancing Model Pruning via Bi-level Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/749252feedd44f7f10d47ec1d674a2f8-Abstract-Conference.html) · 📚 被引 5
- **作者**: Yihua Zhang, Yuguang Yao, Parikshit Ram, Pu Zhao, Tianlong Chen, Mingyi Hong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Learning Best Combination for Efficient N: M Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/06589ec9d86876508600a678f9c8f51d-Abstract-Conference.html)
- **作者**: Yuxin Zhang, Mingbao Lin, Zhihang Lin, Yiting Luo, Ke Li, Fei Chao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Accelerated Projected Gradient Algorithms for Sparsity Constrained Optimization Problems.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/aab3003c922e0fcd2fd2c951fa3c03ad-Abstract-Conference.html) · 📚 被引 1
- **作者**: Jan Harold Alcantara, Ching-pei Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Sparsity in Continuous-Depth Neural Networks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/0626822954674a06ccd9c234e3f0d572-Abstract-Conference.html) · 📚 被引 2
- **作者**: Hananeh Aliee, Till Richter, Mikhail Solonin, Ignacio Ibarra, Fabian J. Theis, Niki Kilbertus
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Transformers meet Stochastic Block Models: Attention with Data-Adaptive Sparsity and Cost.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9c93b3cd3bc60c0fe7b0c2d74a2da966-Abstract-Conference.html) · 📚 被引 2
- **作者**: Sungjun Cho, Seonwoo Min, Jinwoo Kim, Moontae Lee, Honglak Lee, Seunghoon Hong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Controlled Sparsity via Constrained Optimization or: How I Learned to Stop Tuning Penalties and Love Constraints.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/089b592cccfafdca8e0178e85b609f19-Abstract-Conference.html) · 📚 被引 5
- **作者**: Jose Gallego-Posada, Juan Ramirez, Akram Erraqabi, Yoshua Bengio, Simon Lacoste-Julien
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Feature Learning in $L_2$-regularized DNNs: Attraction/Repulsion and Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/2d2f85c0f93e69cf71f58eebaebb5e8d-Abstract-Conference.html) · 📚 被引 2
- **作者**: Arthur Jacot, Eugene A. Golikov, Clément Hongler, Franck Gabriel
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Spartan: Differentiable Sparsity via Regularized Transportation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/1afb9ca4adf1d9cb3c87ff3e22a29049-Abstract-Conference.html)
- **作者**: Kai Sheng Tai, Tai-Peng Tian, Ser Nam Lim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Accelerating Sparse Convolution with Column Vector-Wise Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/c383e44d9a878d1982d9abb838bd5d8a-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yijun Tan, Kai Han, Kang Zhao, Xianzhi Yu, Zidong Du, Yunji Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### SInGE: Sparsity via Integrated Gradients Estimation of Neuron Relevance.
- **链接**: [arXiv:2207.04089](https://arxiv.org/abs/2207.04089)
- **作者**: Edouard Yvinec, Arnaud Dapogny, Matthieu Cord, Kevin Bailly
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The leap in performance in state-of-the-art computer vision methods is attributed to the development of deep neural networks. However it often comes at a computational price which may hinder their deployment. To alleviate this limitation, structured pruning is a well known technique which consists in removing channels, neurons or filters, and is commonly applied in order to produce more compact models. In most cases, the computations to remove are selected based on a relative importance criterion. At the same time, the need for explainable predictive models has risen tremendously and motivated the development of robust attribution methods that highlight the relative importance of pixels of an input image or feature map. In this work, we discuss the limitations of existing pruning heuristics, among which magnitude and gradient-based methods. We draw inspiration from attribution methods to design a novel integrated gradient pruning criterion, in which the relevance of each neuron is defined as the integral of the gradient variation on a path towards this neuron removal. Furthermore, we propose an entwined DNN pruning and fine-tuning flowchart to better preserve DNN accuracy while removing parameters. We show through extensive validation on several datasets, architectures as well as pruning scenarios that the proposed method, dubbed SInGE, significantly outperforms existing state-of-the-art DNN pruning methods.

</details>

### On the Identifiability of Nonlinear ICA: Sparsity and Beyond.
- **链接**: [arXiv:2206.07751](https://arxiv.org/abs/2206.07751) · 📚 被引 2
- **作者**: Yujia Zheng, Ignavier Ng, Kun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Nonlinear independent component analysis (ICA) aims to recover the underlying independent latent sources from their observable nonlinear mixtures. How to make the nonlinear ICA model identifiable up to certain trivial indeterminacies is a long-standing problem in unsupervised learning. Recent breakthroughs reformulate the standard independence assumption of sources as conditional independence given some auxiliary variables (e.g., class labels and/or domain/time indexes) as weak supervision or inductive bias. However, nonlinear ICA with unconditional priors cannot benefit from such developments. We explore an alternative path and consider only assumptions on the mixing process, such as Structural Sparsity. We show that under specific instantiations of such constraints, the independent latent sources can be identified from their nonlinear mixtures up to a permutation and a component-wise transformation, thus achieving nontrivial identifiability of nonlinear ICA without auxiliary variables. We provide estimation methods and validate the theoretical results experimentally. The results on image data suggest that our conditions may hold in a number of practical data generating processes.

</details>

### Geometric Knowledge Distillation: Topology Compression for Graph Neural Networks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/c06f788963f0ce069f5b2dbf83fe7822-Abstract-Conference.html) · 📚 被引 6
- **作者**: Chenxiao Yang, Qitian Wu, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Sparse DETR: Efficient End-to-End Object Detection with Learnable Sparsity. → [object-detection](../object-detection/Guideline%202022.md)
- Q-ViT: Accurate and Fully Quantized Low-bit Vision Transformer. → [vision-transformer](../vision-transformer/Guideline%202022.md)
- Focal Sparse Convolutional Networks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention. → [object-detection](../object-detection/Guideline%202022.md)
- Point-to-Voxel Knowledge Distillation for LiDAR Semantic Segmentation. → [3d-detection](../3d-detection/Guideline%202022.md)
- Learning Bayesian Sparse Networks with Full Experience Replay for Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Constrained Few-shot Class-incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Multimodal Transformer for Automatic 3D Annotation and Object Detection. → [multimodal](../multimodal/Guideline%202022.md)
- SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- PointCLM: A Contrastive Learning-based Framework for Multi-instance Point Cloud Registration. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Point Cloud Compression with Range Image-Based Entropy Model for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- FOSTER: Feature Boosting and Compression for Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Neural Architecture Search for Spiking Neural Networks. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- Memory Replay with Data Compression for Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Unifying Voxel-based Representation with Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Towards Efficient 3D Object Detection with Knowledge Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202022.md)
- SAViT: Structure-Aware Vision Transformer Pruning via Collaborative Optimization. → [vision-transformer](../vision-transformer/Guideline%202022.md)
<!-- COMPLETE v1 papers=72 -->
