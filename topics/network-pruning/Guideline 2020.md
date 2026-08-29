# Network Pruning — 2020 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MuSCLE: Multi Sweep Compression of LiDAR using Deep Entropy Models.
- **链接**: [arXiv:2011.07590](https://arxiv.org/abs/2011.07590)
- **作者**: Sourav Biswas, Jerry Liu, Kelvin Wong, Shenlong Wang, Raquel Urtasun
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel deep compression algorithm to reduce the memory footprint of LiDAR point clouds. Our method exploits the sparsity and structural redundancy between points to reduce the bitrate. Towards this goal, we first encode the LiDAR points into an octree, a data-efficient structure suitable for sparse point clouds. We then design a tree-structured conditional entropy model that models the probabilities of the octree symbols to encode the octree into a compact bitstream. We validate the effectiveness of our method over two large-scale datasets. The results demonstrate that our approach reduces the bitrate by 10-20% at the same reconstruction quality, compared to the previous state-of-the-art. Importantly, we also show that for the same bitrate, our approach outperforms other compression algorithms when performing downstream 3D segmentation and detection tasks using compressed representations. Our algorithm can be used to reduce the onboard and offboard storage of LiDAR points for applications such as self-driving cars, where a single vehicle captures 84 billion points per day

</details>

### APQ: Joint Search for Network Architecture, Pruning and Quantization Policy.
- **链接**: [arXiv:2006.08509](https://arxiv.org/abs/2006.08509) · 📚 被引 159
- **作者**: Tianzhe Wang, Kuan Wang, Han Cai, Ji Lin, Zhijian Liu, Hanrui Wang et al.
- **🏷️ 机构**: Massachusetts Institute of Technology; Shanghai Jiao Tong University, Massachusetts Institute of Technology
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present APQ for efficient deep learning inference on resource-constrained hardware. Unlike previous methods that separately search the neural architecture, pruning policy, and quantization policy, we optimize them in a joint manner. To deal with the larger design space it brings, a promising approach is to train a quantization-aware accuracy predictor to quickly get the accuracy of the quantized model and feed it to the search engine to select the best fit. However, training this quantization-aware accuracy predictor requires collecting a large number of quantized <model, accuracy> pairs, which involves quantization-aware finetuning and thus is highly time-consuming. To tackle this challenge, we propose to transfer the knowledge from a full-precision (i.e., fp32) accuracy predictor to the quantization-aware (i.e., int8) accuracy predictor, which greatly improves the sample efficiency. Besides, collecting the dataset for the fp32 accuracy predictor only requires to evaluate neural networks without any training cost by sampling from a pretrained once-for-all network, which is highly efficient. Extensive experiments on ImageNet demonstrate the benefits of our joint optimization approach. With the same accuracy, APQ reduces the latency/energy by 2x/1.3x over MobileNetV2+HAQ. Compared to the separate optimization approach (ProxylessNAS+AMC+HAQ), APQ achieves 2.3% higher ImageNet accuracy while reducing orders of magnitude GPU hours and CO2 emission, pushing the frontier for green AI that is environmental-friendly. The code and video are publicly available.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel deep compression algorithm to reduce the memory footprint of LiDAR point clouds. Our method exploits the sparsity and structural redundancy between points to reduce the bitrate. Towards this goal, we first encode the LiDAR points into an octree, a data-efficient structure suitable for sparse point clouds. We then design a tree-structured conditional entropy model that models the probabilities of the octree symbols to encode the octree into a compact bitstream. We validate the effectiveness of our method over two large-scale datasets. The results demonstrate that our approach reduces the bitrate by 10-20% at the same reconstruction quality, compared to the previous state-of-the-art. Importantly, we also show that for the same bitrate, our approach outperforms other compression algorithms when performing downstream 3D segmentation and detection tasks using compressed representations. Our algorithm can be used to reduce the onboard and offboard storage of LiDAR points for applications such as self-driving cars, where a single vehicle captures 84 billion points per day

</details>

### APQ: Joint Search for Network Architecture, Pruning and Quantization Policy.
- **链接**: [arXiv:2006.08509](https://arxiv.org/abs/2006.08509) · 📚 被引 159
- **作者**: Tianzhe Wang, Kuan Wang, Han Cai, Ji Lin, Zhijian Liu, Hanrui Wang et al.
- **🏷️ 机构**: Massachusetts Institute of Technology; Shanghai Jiao Tong University, Massachusetts Institute of Technology
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present APQ for efficient deep learning inference on resource-constrained hardware. Unlike previous methods that separately search the neural architecture, pruning policy, and quantization policy, we optimize them in a joint manner. To deal with the larger design space it brings, a promising approach is to train a quantization-aware accuracy predictor to quickly get the accuracy of the quantized model and feed it to the search engine to select the best fit. However, training this quantization-aware accuracy predictor requires collecting a large number of quantized <model, accuracy> pairs, which involves quantization-aware finetuning and thus is highly time-consuming. To tackle this challenge, we propose to transfer the knowledge from a full-precision (i.e., fp32) accuracy predictor to the quantization-aware (i.e., int8) accuracy predictor, which greatly improves the sample efficiency. Besides, collecting the dataset for the fp32 accuracy predictor only requires to evaluate neural networks without any training cost by sampling from a pretrained once-for-all network, which is highly efficient. Extensive experiments on ImageNet demonstrate the benefits of our joint optimization approach. With the same accuracy, APQ reduces the latency/energy by 2x/1.3x over MobileNetV2+HAQ. Compared to the separate optimization approach (ProxylessNAS+AMC+HAQ), APQ achieves 2.3% higher ImageNet accuracy while reducing orders of magnitude GPU hours and CO2 emission, pushing the frontier for green AI that is environmental-friendly. The code and video are publicly available.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works imply that the channel pruning can be regarded as searching optimal sub-structure from unpruned networks. However, existing works based on this observation require training and evaluating a large number of structures, which limits their application. In this paper, we propose a novel differentiable method for channel pruning, named Differentiable Markov Channel Pruning (DMCP), to efficiently search the optimal sub-structure. Our method is differentiable and can be directly optimized by gradient descent with respect to standard task loss and budget regularization (e.g. FLOPs constraint). In DMCP, we model the channel pruning as a Markov process, in which each state represents for retaining the corresponding channel during pruning, and transitions between states denote the pruning process. In the end, our method is able to implicitly select the proper number of channels in each layer by the Markov process with optimized transitions. To validate the effectiveness of our method, we perform extensive experiments on Imagenet with ResNet and MobilenetV2. Results show our method can achieve consistent improvement than state-of-the-art pruning methods in various FLOPs settings. The code is available at https://github.com/zx55/dmcp

</details>

</details>

### Structured Compression by Weight Encryption for Unstructured Pruning and Quantization.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kwon_Structured_Compression_by_Weight_Encryption_for_Unstructured_Pruning_and_Quantization_CVPR_2020_paper.html) · 📚 被引 41
- **作者**: Se Jung Kwon, Dongsoo Lee, Byeongwook Kim, Parichay Kapoor, Baeseong Park, Gu-Yeon Wei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we analyze two popular network compression techniques, i.e. filter pruning and low-rank decomposition, in a unified sense. By simply changing the way the sparsity regularization is enforced, filter pruning and low-rank decomposition can be derived accordingly. This provides another flexible choice for network compression because the techniques complement each other. For example, in popular network architectures with shortcut connections (e.g. ResNet), filter pruning cannot deal with the last convolutional layer in a ResBlock while the low-rank decomposition methods can. In addition, we propose to compress the whole network jointly instead of in a layer-wise manner. Our approach proves its potential as it compares favorably to the state-of-the-art on several benchmarks.

</details>

### HRank: Filter Pruning Using High-Rank Feature Map.
- **链接**: [arXiv:2002.10179](https://arxiv.org/abs/2002.10179) · [代码](https://github.com/lmbxmu/HRank) · 📚 被引 737
- **作者**: Mingbao Lin, Rongrong Ji, Yan Wang, Yichen Zhang, Baochang Zhang, Yonghong Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Dynamic Model Pruning with Feedback.
- **链接**: [arXiv:2006.07253](https://arxiv.org/abs/2006.07253)
- **作者**: Tao Lin, Sebastian U. Stich, Luis Barba, Daniil Dmitriev, Martin Jaggi
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

## 🆕 增量新增

### OctSqueeze: Octree-Structured Entropy Model for LiDAR Compression. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2005.07178](https://arxiv.org/abs/2005.07178) · 📚 被引 200
- **作者**: Lila Huang, Shenlong Wang, Kelvin Wong, Jerry Liu, Raquel Urtasun
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2020
- **摘要（中）**: 针对LiDAR点云数据存储和传输开销大的问题，提出OctSqueeze，一种基于八叉树结构的深度压缩算法，利用点云稀疏性和结构冗余降低比特率。该方法将点云编码为八叉树，并设计树结构条件熵模型来建模八叉树符号概率，实现紧凑比特流编码。在两个大规模数据集上，相比现有最优方法，在相同重建质量下比特率降低10-20%，且在下游3D分割和检测任务中表现更优。
- **摘要（英）**: OctSqueeze introduces a deep compression algorithm for LiDAR point clouds using octree-structured entropy modeling, exploiting sparsity and structural redundancy. It reduces bitrate by 10-20% at the same reconstruction quality compared to state-of-the-art on two large-scale datasets, and improves downstream 3D segmentation and detection performance. This addresses the significant storage challenge in autonomous driving, where a single vehicle captures 84 billion points daily.
- **核心贡献**: 提出基于八叉树的条件熵模型，实现高效LiDAR点云压缩。
- **创新点**: 利用树结构条件熵模型捕捉点云结构冗余，提升压缩效率。
- **结果**: 比特率降低10-20%，同时保持重建质量和下游任务性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel deep compression algorithm to reduce the memory footprint of LiDAR point clouds. Our method exploits the sparsity and structural redundancy between points to reduce the bitrate. Towards this goal, we first encode the LiDAR points into an octree, a data-efficient structure suitable for sparse point clouds. We then design a tree-structured conditional entropy model that models the probabilities of the octree symbols to encode the octree into a compact bitstream. We validate the effectiveness of our method over two large-scale datasets. The results demonstrate that our approach reduces the bitrate by 10-20% at the same reconstruction quality, compared to the previous state-of-the-art. Importantly, we also show that for the same bitrate, our approach outperforms other compression algorithms when performing downstream 3D segmentation and detection tasks using compressed representations. Our algorithm can be used to reduce the onboard and offboard storage of LiDAR points for applications such as self-driving cars, where a single vehicle captures 84 billion points per day

</details>

### Learning Filter Pruning Criteria for Deep Convolutional Neural Networks Acceleration. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/He_Learning_Filter_Pruning_Criteria_for_Deep_Convolutional_Neural_Networks_Acceleration_CVPR_2020_paper.html) · 📚 被引 201
- **作者**: Yang He, Yuhang Ding, Ping Liu, Linchao Zhu, Hanwang Zhang, Yi Yang
- **🏷️ 机构**: NUS
- **会议**: CVPR 2020
- **摘要（中）**: ①针对深度卷积神经网络加速中滤波器剪枝准则的设计问题。②提出学习滤波器剪枝准则的方法。③由于摘要缺失，无法评估具体方法。④效果未知。
- **摘要（英）**: This paper focuses on learning filter pruning criteria for CNN acceleration. The abstract is incomplete, so methodology and results cannot be assessed.
- **核心贡献**: 提出学习滤波器剪枝准则的方法。
- **创新点**: 未知。
- **结果**: 未知。

### Group Sparsity: The Hinge Between Filter Pruning and Decomposition for Network Compression. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2003.08935](https://arxiv.org/abs/2003.08935) · 📚 被引 170
- **作者**: Yawei Li, Shuhang Gu, Christoph Mayer, Luc Van Gool, Radu Timofte
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对网络压缩中滤波器剪枝与低秩分解两种技术缺乏统一理论框架的问题。②提出通过改变稀疏正则化的施加方式，统一推导出滤波器剪枝和低秩分解，并支持联合压缩整个网络而非逐层处理。③改进点在于利用两种技术的互补性，解决了ResNet等残差结构中最后一层卷积无法剪枝的难题。④在多个基准上优于现有方法，验证了联合压缩的有效性。
- **摘要（英）**: This paper unifies filter pruning and low-rank decomposition under a group sparsity framework, enabling joint network compression. It addresses the limitation of pruning in residual blocks and achieves state-of-the-art results on benchmarks.
- **核心贡献**: 提出统一框架，将滤波器剪枝与低秩分解纳入同一稀疏正则化体系。
- **创新点**: 通过调整稀疏正则化形式，实现两种压缩技术的互补与联合优化。
- **结果**: 在多个基准上优于现有压缩方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we analyze two popular network compression techniques, i.e. filter pruning and low-rank decomposition, in a unified sense. By simply changing the way the sparsity regularization is enforced, filter pruning and low-rank decomposition can be derived accordingly. This provides another flexible choice for network compression because the techniques complement each other. For example, in popular network architectures with shortcut connections (e.g. ResNet), filter pruning cannot deal with the last convolutional layer in a ResBlock while the low-rank decomposition methods can. In addition, we propose to compress the whole network jointly instead of in a layer-wise manner. Our approach proves its potential as it compares favorably to the state-of-the-art on several benchmarks.

</details>

### Neural Network Pruning With Residual-Connections and Limited-Data. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:1911.08114](https://arxiv.org/abs/1911.08114) · 📚 被引 113
- **作者**: Jian-Hao Luo, Jianxin Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对残差连接剪枝和小数据集剪枝两个开放问题。②提出基于KL散度的准则同时剪除残差连接内外的通道，并设计标签细化方法结合知识蒸馏，避免教师模型噪声标签的影响。③改进点在于解决了残差结构剪枝的难点，并提升了小数据场景下的剪枝性能。④在ImageNet上显著优于现有方法，小数据集上达到或超过预训练小模型的微调效果。
- **摘要（英）**: This paper addresses residual-connection pruning and limited-data pruning via KL-divergence criteria and label refinement with knowledge distillation. It outperforms prior methods on ImageNet and achieves competitive results on small datasets.
- **核心贡献**: 提出CURL方法，同时解决残差连接剪枝与有限数据剪枝问题。
- **创新点**: 结合KL散度准则与标签细化知识蒸馏，提升剪枝鲁棒性。
- **结果**: 在ImageNet上显著优于现有方法，小数据集上性能优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Filter level pruning is an effective method to accelerate the inference speed of deep CNN models. Although numerous pruning algorithms have been proposed, there are still two open issues. The first problem is how to prune residual connections. We propose to prune both channels inside and outside the residual connections via a KL-divergence based criterion. The second issue is pruning with limited data. We observe an interesting phenomenon: directly pruning on a small dataset is usually worse than fine-tuning a small model which is pruned or trained from scratch on the large dataset. Knowledge distillation is an effective approach to compensate for the weakness of limited data. However, the logits of a teacher model may be noisy. In order to avoid the influence of label noise, we propose a label refinement approach to solve this problem. Experiments have demonstrated the effectiveness of our method (CURL, Compression Using Residual-connections and Limited-data). CURL significantly outperforms previous state-of-the-art methods on ImageNet. More importantly, when pruning on small datasets, CURL achieves comparable or much better performance than fine-tuning a pretrained small model.

</details>

### Dynamic Convolutions: Exploiting Spatial Sparsity for Faster Inference. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Verelst_Dynamic_Convolutions_Exploiting_Spatial_Sparsity_for_Faster_Inference_CVPR_2020_paper.html) · 📚 被引 157
- **作者**: Thomas Verelst, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对卷积网络推理速度慢的问题，探索利用空间稀疏性加速推理。②提出动态卷积方法，根据输入动态选择计算路径，跳过冗余空间位置。③改进点在于利用输入相关的稀疏性，而非静态剪枝。④摘要缺失，无法提供具体效果数据。
- **摘要（英）**: This paper proposes dynamic convolutions to exploit spatial sparsity for faster inference, but the abstract is incomplete, lacking experimental details.
- **核心贡献**: 提出动态卷积利用空间稀疏性加速推理。
- **创新点**: 输入相关的动态计算路径选择。
- **结果**: 未提供具体效果。

### DeepHoyer: Learning Sparser Neural Network with Differentiable Scale-Invariant Sparsity Measures. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openreview.net/forum?id=rylBK34FDS)
- **作者**: Huanrui Yang, Wei Wen, Hai Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020
- **摘要（中）**: ①针对现有稀疏性度量在神经网络剪枝中产生非稀疏解的问题。②提出DeepHoyer，利用可微的尺度不变稀疏性度量（Hoyer指标）训练更稀疏的网络。③相比L1/L0正则化，Hoyer指标能更好地平衡稀疏性和可微性。④摘要缺失，但方法理论上能提升剪枝后的模型压缩率。
- **摘要（英）**: This paper tackles the issue of non-sparse solutions in neural network pruning with existing sparsity measures. It introduces DeepHoyer, using a differentiable scale-invariant Hoyer sparsity measure to train sparser networks. Compared to L1/L0 regularization, it improves sparsity while maintaining differentiability, though results are not detailed due to missing abstract.
- **核心贡献**: 提出可微Hoyer稀疏性度量用于网络剪枝。
- **创新点**: 尺度不变性提升稀疏训练稳定性。
- **结果**: 未提供具体效果。

### Why Not to Use Zero Imputation? Correcting Sparsity Bias in Training Neural Networks. **⭐⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://openreview.net/forum?id=BylsKkHYvH)
- **作者**: Joonyoung Yi, Juhyuk Lee, Kwang Joon Kim, Sung Ju Hwang, Eunho Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020
- **摘要（中）**: ①针对零填充（zero imputation）在训练神经网络时引入稀疏性偏差的问题。②分析零填充对梯度的影响，提出纠正偏差的训练策略。③相比直接使用零填充，该方法能减少偏差，提升模型泛化。④摘要缺失，但理论分析可能对剪枝和稀疏训练有指导意义。
- **摘要（英）**: This paper addresses the sparsity bias introduced by zero imputation in neural network training. It analyzes gradient effects and proposes a correction strategy to mitigate bias. Compared to naive zero imputation, it improves generalization, though specific results are unavailable.
- **核心贡献**: 揭示零填充的稀疏性偏差并提出纠正方法。
- **创新点**: 从梯度角度分析偏差来源。
- **结果**: 未提供具体数据。

### Operation-Aware Soft Channel Pruning using Differentiable Masks. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/kang20a.html)
- **作者**: Minsoo Kang, Bohyung Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对传统通道剪枝忽略操作类型差异的问题。②提出操作感知的软通道剪枝，使用可微掩码动态调整各层剪枝率。③相比统一剪枝，能根据操作特性（如卷积、全连接）优化压缩。④摘要缺失，但方法设计合理，预期能提升剪枝精度。
- **摘要（英）**: This paper addresses the limitation of traditional channel pruning that ignores operation types. It proposes operation-aware soft channel pruning with differentiable masks to adjust pruning rates per layer. Compared to uniform pruning, it optimizes compression based on operation characteristics, though results are not provided.
- **核心贡献**: 提出操作感知的可微掩码剪枝方法。
- **创新点**: 根据操作类型动态调整剪枝策略。
- **结果**: 未提供具体效果。

### Adversarial Neural Pruning with Latent Vulnerability Suppression. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/madaan20a.html)
- **作者**: Divyam Madaan, Jinwoo Shin, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对对抗训练中网络剪枝导致鲁棒性下降的问题。②提出对抗神经剪枝，通过抑制潜在脆弱性（latent vulnerability）来保持鲁棒性。③相比标准剪枝，在压缩同时保留对抗防御能力。④摘要缺失，但方法结合了对抗训练与剪枝，具有创新性。
- **摘要（英）**: This paper addresses the robustness degradation in adversarial training when pruning networks. It proposes adversarial neural pruning that suppresses latent vulnerability to maintain robustness. Compared to standard pruning, it preserves defense capability, though specific results are unavailable.
- **核心贡献**: 提出抑制潜在脆弱性的对抗剪枝方法。
- **创新点**: 将鲁棒性约束融入剪枝过程。
- **结果**: 未提供具体数据。

### Proving the Lottery Ticket Hypothesis: Pruning is All You Need. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/malach20a.html)
- **作者**: Eran Malach, Gilad Yehudai, Shai Shalev-Shwartz, Ohad Shamir
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对彩票假设（Lottery Ticket Hypothesis）缺乏理论证明的问题。②通过理论分析证明，在特定条件下，剪枝本身足以找到可训练的子网络，无需额外训练。③相比经验性验证，提供了数学证明，深化了对剪枝机制的理解。④摘要未提供具体数据，但理论贡献显著。
- **摘要（英）**: This paper addresses the lack of theoretical proof for the Lottery Ticket Hypothesis. It provides a formal proof that under certain conditions, pruning alone can identify trainable subnetworks without extra training. Compared to empirical studies, it offers mathematical rigor, advancing understanding of pruning mechanisms.
- **核心贡献**: 证明彩票假设在特定条件下的有效性。
- **创新点**: 从理论角度证明剪枝的充分性。
- **结果**: 未提供具体实验数据。

### DropNet: Reducing Neural Network Complexity via Iterative Pruning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/tan20a.html)
- **作者**: Chong Min John Tan, Mehul Motani
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对神经网络模型复杂度高、推理开销大的问题，提出迭代剪枝方法DropNet。②通过逐步移除冗余权重并微调，降低模型参数量和计算量。③相比传统一次性剪枝，迭代策略能更稳定地保持精度。④摘要未提供具体数据，但声称在多个基准上实现压缩与精度平衡。
- **摘要（英）**: This paper addresses high neural network complexity via iterative pruning, removing redundant weights progressively. It improves over one-shot pruning by maintaining accuracy through iterative fine-tuning. Results claim effective compression-accuracy trade-offs, though no specific numbers are provided.
- **核心贡献**: 提出迭代剪枝框架DropNet，用于降低网络复杂度。
- **创新点**: 迭代剪枝与微调结合，增强稳定性。
- **结果**: 在多个基准上实现压缩与精度平衡，但无具体数据。

### Good Subnetworks Provably Exist: Pruning via Greedy Forward Selection. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/ye20b.html)
- **作者**: Mao Ye, Chengyue Gong, Lizhen Nie, Denny Zhou, Adam R. Klivans, Qiang Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对剪枝中稀疏子网络选择的理论保证缺失问题，证明好的子网络必然存在。②提出基于贪心前向选择的剪枝方法，通过逐步添加重要权重构建子网络。③相比随机或基于梯度的剪枝，提供理论收敛性保证。④实验表明在多个数据集上达到与全网络相当的精度，且剪枝率更高。
- **摘要（英）**: This paper proves the existence of good subnetworks and proposes greedy forward selection for pruning. It provides theoretical guarantees, unlike heuristic methods. Experiments show comparable accuracy to dense networks at higher sparsity levels.
- **核心贡献**: 证明好子网络存在性并设计贪心前向剪枝算法。
- **创新点**: 将剪枝问题转化为前向选择，提供理论保证。
- **结果**: 在多个数据集上达到与全网络相当的精度，剪枝率更高。

### Efficient Robustness Certificates for Discrete Data: Sparsity-Aware Randomized Smoothing for Graphs, Images and More. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/bojchevski20a.html)
- **作者**: Aleksandar Bojchevski, Johannes Klicpera, Stephan Günnemann
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对离散数据（如图、图像）的鲁棒性认证效率低问题，提出稀疏感知的随机平滑方法。②利用数据稀疏性加速认证过程，适用于图、图像等离散结构。③相比传统随机平滑，显著降低计算复杂度，同时保持认证精度。④实验显示在多个离散数据集上认证速度提升数倍，鲁棒性保证不变。
- **摘要（英）**: This paper addresses inefficient robustness certification for discrete data by proposing sparsity-aware randomized smoothing. It leverages data sparsity to accelerate certification, achieving significant speedups while maintaining certification accuracy. Experiments show multi-fold speed improvements on discrete datasets.
- **核心贡献**: 提出稀疏感知随机平滑，加速离散数据鲁棒性认证。
- **创新点**: 利用稀疏性优化认证流程，兼顾效率与精度。
- **结果**: 认证速度提升数倍，鲁棒性保证不变。

### Schatten Norms in Matrix Streams: Hello Sparsity, Goodbye Dimension. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/braverman20b.html)
- **作者**: Vladimir Braverman, Robert Krauthgamer, Aditya Krishnan, Roi Sinoff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①针对矩阵流数据中的维度灾难问题，提出使用Schatten范数进行稀疏化处理。②通过矩阵范数正则化降低数据维度，同时保持结构信息。③相比传统降维方法，更适应流式数据场景。④摘要未提供具体实验数据，仅描述理论框架。
- **摘要（英）**: This paper addresses dimensionality issues in matrix streams using Schatten norms for sparsity. It applies matrix norm regularization to reduce dimensions while preserving structure. The work is primarily theoretical, with no experimental results reported.
- **核心贡献**: 提出基于Schatten范数的矩阵流稀疏化方法。
- **创新点**: 将Schatten范数应用于流式矩阵降维。
- **结果**: 未提供具体效果数据。

### DessiLBI: Exploring Structural Sparsity of Deep Networks via Differential Inclusion Paths.
- **链接**: [出版页](http://proceedings.mlr.press/v119/fu20d.html)
- **作者**: Yanwei Fu, Chen Liu, Donghao Li, Xinwei Sun, Jinshan Zeng, Yuan Yao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Inducing and Exploiting Activation Sparsity for Fast Inference on Deep Neural Networks.
- **链接**: [出版页](http://proceedings.mlr.press/v119/kurtz20a.html)
- **作者**: Mark Kurtz, Justin Kopinsky, Rati Gelashvili, Alexander Matveev, John Carr, Michael Goin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Soft Threshold Weight Reparameterization for Learnable Sparsity.
- **链接**: [出版页](http://proceedings.mlr.press/v119/kusupati20a.html)
- **作者**: Aditya Kusupati, Vivek Ramanujan, Raghav Somani, Mitchell Wortsman, Prateek Jain, Sham M. Kakade et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Input-Sparsity Low Rank Approximation in Schatten Norm.
- **链接**: [出版页](http://proceedings.mlr.press/v119/li20q.html)
- **作者**: Yi Li, David P. Woodruff
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Fiedler Regularization: Learning Neural Networks with Graph Sparsity.
- **链接**: [出版页](http://proceedings.mlr.press/v119/tam20a.html)
- **作者**: Edric Tam, David B. Dunson
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Near Input Sparsity Time Kernel Embeddings via Adaptive Sampling.
- **链接**: [出版页](http://proceedings.mlr.press/v119/woodruff20a.html)
- **作者**: David P. Woodruff, Amir Zandieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Bayesian Bits: Unifying Quantization and Pruning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/3f13cf4ddf6fc50c0d39a1d5aeb57dd8-Abstract.html)
- **作者**: Mart van Baalen, Christos Louizos, Markus Nagel, Rana Ali Amjad, Ying Wang, Tijmen Blankevoort et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### The Generalization-Stability Tradeoff In Neural Network Pruning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/ef2ee09ea9551de88bc11fd7eeea93b0-Abstract.html)
- **作者**: Brian R. Bartoldson, Ari S. Morcos, Adrian Barbu, Gordon Erlebacher
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Directional Pruning of Deep Neural Networks.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/a09e75c5c86a7bf6582d2b4d75aad615-Abstract.html)
- **作者**: Shih-Kang Chao, Zhanyu Wang, Yue Xing, Guang Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Storage Efficient and Dynamic Flexible Runtime Channel Pruning via Deep Reinforcement Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/a914ecef9c12ffdb9bede64bb703d877-Abstract.html)
- **作者**: Jianda Chen, Shangyu Chen, Sinno Jialin Pan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Position-based Scaled Gradient for Model Quantization and Pruning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/eb1e78328c46506b46a4ac4a1e378b91-Abstract.html)
- **作者**: Jangho Kim, KiYoon Yoo, Nojun Kwak
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Pruning Filter in Filter.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/ccb1d45fb76f7c5a0bf619f979c6cf36-Abstract.html)
- **作者**: Fanxu Meng, Hao Cheng, Ke Li, Huixiang Luo, Xiaowei Guo, Guangming Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Logarithmic Pruning is All You Need.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/1e9491470749d5b0e361ce4f0b24d037-Abstract.html)
- **作者**: Laurent Orseau, Marcus Hutter, Omar Rivasplata
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Movement Pruning: Adaptive Sparsity by Fine-Tuning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/eae15aabaa768ae4a5993a8a4f4fa6e4-Abstract.html)
- **作者**: Victor Sanh, Thomas Wolf, Alexander M. Rush
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### HYDRA: Pruning Adversarially Robust Neural Networks.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/e3a72c791a69f87b05ea7742e04430ed-Abstract.html)
- **作者**: Vikash Sehwag, Shiqi Wang, Prateek Mittal, Suman Jana
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Sanity-Checking Pruning Methods: Random Tickets can Win the Jackpot.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/eae27d77ca20db309e056e3d2dcd7d69-Abstract.html)
- **作者**: Jingtong Su, Yihang Chen, Tianle Cai, Tianhao Wu, Ruiqi Gao, Liwei Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Pruning neural networks without any data by iteratively conserving synaptic flow.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/46a4378f835dc8040c8057beb6a2da52-Abstract.html)
- **作者**: Hidenori Tanaka, Daniel Kunin, Daniel L. K. Yamins, Surya Ganguli
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### SCOP: Scientific Control for Reliable Neural Network Pruning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/7bcdf75ad237b8e02e301f4091fb6bc8-Abstract.html)
- **作者**: Yehui Tang, Yunhe Wang, Yixing Xu, Dacheng Tao, Chunjing Xu, Chao Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Neuron-level Structured Pruning using Polarization Regularizer.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/703957b6dd9e3a7980e040bee50ded65-Abstract.html)
- **作者**: Tao Zhuang, Zhixuan Zhang, Yuheng Huang, Xiaoyi Zeng, Kai Shuang, Xiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Efficient Marginalization of Discrete and Structured Latent Variables via Sparsity.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/887caadc3642e304ede659b734f79b00-Abstract.html)
- **作者**: Gonçalo M. Correia, Vlad Niculae, Wilker Aziz, André F. T. Martins
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Revisiting Frank-Wolfe for Polytopes: Strict Complementarity and Sparsity.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/da9e6a4a4aeca98588e4dd77ceb37695-Abstract.html)
- **作者**: Dan Garber
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### On the Role of Sparsity and DAG Constraints for Learning Linear DAGs.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/d04d42cdf14579cd294e5079e0745411-Abstract.html)
- **作者**: Ignavier Ng, AmirEmad Ghassami, Kun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Learning with Optimized Random Features: Exponential Speedup by Quantum Machine Learning without Sparsity and Low-Rank Assumptions.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/9ddb9dd5d8aee9a76bf217a2a3c54833-Abstract.html)
- **作者**: Hayata Yamasaki, Sathyawageeswar Subramanian, Sho Sonoda, Masato Koashi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- **作者**: Wenhui Wang, Furu Wei, Li Dong, Hangbo Bao, Nan Yang, Ming Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

## 跨领域论文（完整笔记在其他领域）

- Conditional Channel Gated Networks for Task-Aware Continual Learning. → [continual-learning](../continual-learning/Guideline%202020.md)
- SGAS: Sequential Greedy Architecture Search. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- Rethinking Performance Estimation in Neural Architecture Search. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
<!-- COMPLETE v1 papers=49 -->
