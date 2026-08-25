# Network Pruning — 2025 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Efficient Test-time Adaptive Object Detection via Sensitivity-Guided Pruning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Efficient_Test-time_Adaptive_Object_Detection_via_Sensitivity-Guided_Pruning_CVPR_2025_paper.html)
- **作者**: Kunyu Wang, Xueyang Fu, Xin Lu, Chengjie Ge, Chengzhi Cao, Wei Zhai et al.
- **🏷️ 机构**: University of Science and Technology of China,School of Information Science and Technology and MoE Key Laboratory of Brain-Inspired Intelligent Perception and Cognition,Hefei,China,230026
- **会议**: CVPR 2025

### RENO: Real-Time Neural Compression for 3D LiDAR Point Clouds.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/You_RENO_Real-Time_Neural_Compression_for_3D_LiDAR_Point_Clouds_CVPR_2025_paper.html)
- **作者**: Kang You, Tong Chen, Dandan Ding, M. Salman Asif, Zhan Ma
- **🏷️ 机构**: Nanjing University, Hangzhou Normal University, University of California Riverside
- **会议**: CVPR 2025

### Generalized Gaussian Entropy Model for Point Cloud Attribute Compression with Dynamic Likelihood Intervals.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Generalized_Gaussian_Entropy_Model_for_Point_Cloud_Attribute_Compression_with_CVPR_2025_paper.html)
- **作者**: Changhao Peng
- **🏷️ 机构**: Peking University
- **会议**: CVPR 2025

### TopNet: Transformer-Efficient Occupancy Prediction Network for Octree-Structured Point Cloud Geometry Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_TopNet_Transformer-Efficient_Occupancy_Prediction_Network_for_Octree-Structured_Point_Cloud_Geometry_CVPR_2025_paper.html)
- **作者**: Xinjie Wang, Yifan Zhang, Ting Liu, Xinpu Liu, Ke Xu, Jianwei Wan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### EfficientLLaVA: Generalizable Auto-Pruning for Large Vision-language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_EfficientLLaVA_Generalizable_Auto-Pruning_for_Large_Vision-language_Models_CVPR_2025_paper.html)
- **作者**: Yinan Liang, Ziwei Wang, Xiuwei Xu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### PUP 3D-GS: Principled Uncertainty Pruning for 3D Gaussian Splatting.
- **链接**: [arXiv:2406.10219](https://arxiv.org/abs/2406.10219) · 📚 被引 37
- **作者**: Alex Hanson, Allen Tu, Vasu Singla, Mayuka Jayawardhana, Matthias Zwicker, Tom Goldstein
- **🏷️ 机构**: University of Maryland,College Park
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Recent advances in novel view synthesis have enabled real-time rendering speeds with high reconstruction accuracy. 3D Gaussian Splatting (3D-GS), a foundational point-based parametric 3D scene representation, models scenes as large sets of 3D Gaussians. However, complex scenes can consist of millions of Gaussians, resulting in high storage and memory requirements that limit the viability of 3D-GS on devices with limited resources. Current techniques for compressing these pretrained models by pruning Gaussians rely on combining heuristics to determine which Gaussians to remove. At high compression ratios, these pruned scenes suffer from heavy degradation of visual fidelity and loss of foreground details. In this paper, we propose a principled sensitivity pruning score that preserves visual fidelity and foreground details at significantly higher compression ratios than existing approaches. It is computed as a second-order approximation of the reconstruction error on the training views with respect to the spatial parameters of each Gaussian. Additionally, we propose a multi-round prune-refine pipeline that can be applied to any pretrained 3D-GS model without changing its training pipeline. After pruning 90% of Gaussians, a substantially higher percentage than previous methods, our PUP 3D-GS pipeline increases average rendering speed by 3.56$\times$ while retaining more salient foreground information and achieving higher image quality metrics than existing techniques on scenes from the Mip-NeRF 360, Tanks & Temples, and Deep Blending datasets.

### ATP: Adaptive Threshold Pruning for Efficient Data Encoding in Quantum Neural Networks.
- **链接**: [arXiv:2503.21815](https://arxiv.org/abs/2503.21815) · 📚 被引 3
- **作者**: Mohamed Afane, Gabrielle Ebbrecht, Ying Wang, Juntao Chen, Junaid Farooq
- **🏷️ 机构**: Fordham University, Stevens Institute of Technology, University of Michigan-Dearborn
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Quantum Neural Networks (QNNs) offer promising capabilities for complex data tasks, but are often constrained by limited qubit resources and high entanglement, which can hinder scalability and efficiency. In this paper, we introduce Adaptive Threshold Pruning (ATP), an encoding method that reduces entanglement and optimizes data complexity for efficient computations in QNNs. ATP dynamically prunes non-essential features in the data based on adaptive thresholds, effectively reducing quantum circuit requirements while preserving high performance. Extensive experiments across multiple datasets demonstrate that ATP reduces entanglement entropy and improves adversarial robustness when combined with adversarial training methods like FGSM. Our results highlight ATPs ability to balance computational efficiency and model resilience, achieving significant performance improvements with fewer resources, which will help make QNNs more feasible in practical, resource-constrained settings.

### PACT: Pruning and Clustering-Based Token Reduction for Faster Visual Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Dhouib_PACT_Pruning_and_Clustering-Based_Token_Reduction_for_Faster_Visual_Language_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Mohamed Dhouib, Davide Buscaldi, Sonia Vanier, Aymen Shabou
- **🏷️ 机构**: LIX, &#x00C9;cole Polytechnique, IP,Paris,France, LIPN, Universit&#x00E9; Sorbonne Paris Nord,France, DataLab Groupe, Cr&#x00E9;dit Agricole S.A,France
- **会议**: CVPR 2025

### ICP: Immediate Compensation Pruning for Mid-to-high Sparsity.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Luo_ICP_Immediate_Compensation_Pruning_for_Mid-to-high_Sparsity_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Xin Luo, Xueming Fu, Zihang Jiang, S. Kevin Zhou
- **🏷️ 机构**: USTC,School of Biomedical Engineering, Division of Life Sciences and Medicine
- **会议**: CVPR 2025

### Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Qu_Automatic_Joint_Structured_Pruning_and_Quantization_for_Efficient_Neural_Network_CVPR_2025_paper.html) · 📚 被引 20
- **作者**: Xiaoyi Qu, David Aponte, Colby R. Banbury, Daniel P. Robinson, Tianyu Ding, Kazuhito Koishida et al.
- **🏷️ 机构**: Lehigh University, Microsoft
- **会议**: CVPR 2025

### MDP: Multidimensional Vision Model Pruning with Latency Constraint.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_MDP_Multidimensional_Vision_Model_Pruning_with_Latency_Constraint_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Xinglong Sun, Barath Lakshmanan, Maying Shen, Shiyi Lan, Jingde Chen, José M. Álvarez
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2025

### Libra-Merging: Importance-redundancy and Pruning-merging Trade-off for Acceleration Plug-in in Large Vision-Language Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Libra-Merging_Importance-redundancy_and_Pruning-merging_Trade-off_for_Acceleration_Plug-in_in_Large_CVPR_2025_paper.html)
- **作者**: Longrong Yang, Dong Shen, Chaoxiang Cai, Kaibing Chen, Fan Yang, Tingting Gao et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2025

### ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.html)
- **作者**: Xubing Ye, Yukang Gan, Yixiao Ge, Xiao-Ping Zhang, Yansong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Flexible Group Count Enables Hassle-Free Structured Pruning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Flexible_Group_Count_Enables_Hassle-Free_Structured_Pruning_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Jiamu Zhang, Shaochen Zhong, Andrew Ye, Zirui Liu, Sebastian Zhao, Kaixiong Zhou et al.
- **🏷️ 机构**: Rice University,USA, Stanford University,USA, University of Minnesota-Twin Cities,USA
- **会议**: CVPR 2025

### SINR: Sparsity Driven Compressed Implicit Neural Representations.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jayasundara_SINR_Sparsity_Driven_Compressed_Implicit_Neural_Representations_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Dhananjaya Jayasundara, Sudarshan Rajagopalan, Yasiru Ranasinghe, Trac D. Tran, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University
- **会议**: CVPR 2025

### SURGEON: Memory-Adaptive Fully Test-Time Adaptation via Dynamic Activation Sparsity.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SURGEON_Memory-Adaptive_Fully_Test-Time_Adaptation_via_Dynamic_Activation_Sparsity_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Ke Ma, Jiaqi Tang, Bin Guo, Fan Dang, Sicong Liu, Zhui Zhu et al.
- **🏷️ 机构**: Northwestern Polytechnical University, The Hong Kong University of Science and Technology, Beijing Jiaotong University
- **会议**: CVPR 2025

### Random Conditioning for Diffusion Model Compression with Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kim_Random_Conditioning_for_Diffusion_Model_Compression_with_Distillation_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Dohyun Kim, Sehwan Park, Geonhee Han, Seung Wook Kim, Paul Hongsuck Seo
- **🏷️ 机构**: Korea University,Dept. of CSE, NVIDIA
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models. → [multimodal](../multimodal/Guideline%202025.md)
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding. → [3d-detection](../3d-detection/Guideline%202025.md)
- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- CASP: Compression of Large Multimodal Models Based on Attention Sparsity. → [multimodal](../multimodal/Guideline%202025.md)
