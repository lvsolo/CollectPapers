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
