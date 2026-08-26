# Network Pruning — 2020 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OctSqueeze: Octree-Structured Entropy Model for LiDAR Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Huang_OctSqueeze_Octree-Structured_Entropy_Model_for_LiDAR_Compression_CVPR_2020_paper.html) · 📚 被引 200
- **作者**: Lila Huang, Shenlong Wang, Kelvin Wong, Jerry Liu, Raquel Urtasun
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2020

### APQ: Joint Search for Network Architecture, Pruning and Quantization Policy.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wang_APQ_Joint_Search_for_Network_Architecture_Pruning_and_Quantization_Policy_CVPR_2020_paper.html) · 📚 被引 159
- **作者**: Tianzhe Wang, Kuan Wang, Han Cai, Ji Lin, Zhijian Liu, Hanrui Wang et al.
- **🏷️ 机构**: Massachusetts Institute of Technology; Shanghai Jiao Tong University, Massachusetts Institute of Technology
- **会议**: CVPR 2020

### Multi-Dimensional Pruning: A Unified Framework for Model Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Guo_Multi-Dimensional_Pruning_A_Unified_Framework_for_Model_Compression_CVPR_2020_paper.html) · 📚 被引 65
- **作者**: Jinyang Guo, Wanli Ouyang, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### DMCP: Differentiable Markov Channel Pruning for Neural Networks.
- **链接**: [arXiv:2005.03354](https://arxiv.org/abs/2005.03354) · [代码](https://github.com/zx55/dmcp) · 📚 被引 142
- **作者**: Shaopeng Guo, Yujie Wang, Quanquan Li, Junjie Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Recent works imply that the channel pruning can be regarded as searching optimal sub-structure from unpruned networks. However, existing works based on this observation require training and evaluating a large number of structures, which limits their application. In this paper, we propose a novel differentiable method for channel pruning, named Differentiable Markov Channel Pruning (DMCP), to efficiently search the optimal sub-structure. Our method is differentiable and can be directly optimized by gradient descent with respect to standard task loss and budget regularization (e.g. FLOPs constraint). In DMCP, we model the channel pruning as a Markov process, in which each state represents for retaining the corresponding channel during pruning, and transitions between states denote the pruning process. In the end, our method is able to implicitly select the proper number of channels in each layer by the Markov process with optimized transitions. To validate the effectiveness of our method, we perform extensive experiments on Imagenet with ResNet and MobilenetV2. Results show our method can achieve consistent improvement than state-of-the-art pruning methods in various FLOPs settings. The code is available at https://github.com/zx55/dmcp

### Learning Filter Pruning Criteria for Deep Convolutional Neural Networks Acceleration.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/He_Learning_Filter_Pruning_Criteria_for_Deep_Convolutional_Neural_Networks_Acceleration_CVPR_2020_paper.html) · 📚 被引 201
- **作者**: Yang He, Yuhang Ding, Ping Liu, Linchao Zhu, Hanwang Zhang, Yi Yang
- **🏷️ 机构**: NUS
- **会议**: CVPR 2020

### Structured Compression by Weight Encryption for Unstructured Pruning and Quantization.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kwon_Structured_Compression_by_Weight_Encryption_for_Unstructured_Pruning_and_Quantization_CVPR_2020_paper.html) · 📚 被引 41
- **作者**: Se Jung Kwon, Dongsoo Lee, Byeongwook Kim, Parichay Kapoor, Baeseong Park, Gu-Yeon Wei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Group Sparsity: The Hinge Between Filter Pruning and Decomposition for Network Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Group_Sparsity_The_Hinge_Between_Filter_Pruning_and_Decomposition_for_CVPR_2020_paper.html) · 📚 被引 170
- **作者**: Yawei Li, Shuhang Gu, Christoph Mayer, Luc Van Gool, Radu Timofte
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### HRank: Filter Pruning Using High-Rank Feature Map.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Lin_HRank_Filter_Pruning_Using_High-Rank_Feature_Map_CVPR_2020_paper.html) · 📚 被引 737
- **作者**: Mingbao Lin, Rongrong Ji, Yan Wang, Yichen Zhang, Baochang Zhang, Yonghong Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Neural Network Pruning With Residual-Connections and Limited-Data.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Luo_Neural_Network_Pruning_With_Residual-Connections_and_Limited-Data_CVPR_2020_paper.html) · 📚 被引 113
- **作者**: Jian-Hao Luo, Jianxin Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Dynamic Convolutions: Exploiting Spatial Sparsity for Faster Inference.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Verelst_Dynamic_Convolutions_Exploiting_Spatial_Sparsity_for_Faster_Inference_CVPR_2020_paper.html) · 📚 被引 157
- **作者**: Thomas Verelst, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Efficient and Robust Shape Correspondence via Sparsity-Enforced Quadratic Assignment.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_Efficient_and_Robust_Shape_Correspondence_via_Sparsity-Enforced_Quadratic_Assignment_CVPR_2020_paper.html) · 📚 被引 7
- **作者**: Rui Xiang, Rongjie Lai, Hongkai Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Automatic Neural Network Compression by Sparsity-Quantization Joint Learning: A Constrained Optimization-Based Approach.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Yang_Automatic_Neural_Network_Compression_by_Sparsity-Quantization_Joint_Learning_A_Constrained_CVPR_2020_paper.html) · 📚 被引 63
- **作者**: Haichuan Yang, Shupeng Gui, Yuhao Zhu, Ji Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Few Sample Knowledge Distillation for Efficient Network Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Few_Sample_Knowledge_Distillation_for_Efficient_Network_Compression_CVPR_2020_paper.html) · 📚 被引 107
- **作者**: Tianhong Li, Jianguo Li, Zhuang Liu, Changshui Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
