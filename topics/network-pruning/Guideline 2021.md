# Network Pruning — 2021 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### NPAS: A Compiler-Aware Framework of Unified Network Pruning and Architecture Search for Beyond Real-Time Mobile Acceleration.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_NPAS_A_Compiler-Aware_Framework_of_Unified_Network_Pruning_and_Architecture_CVPR_2021_paper.html) · 📚 被引 25
- **作者**: Zhengang Li, Geng Yuan, Wei Niu, Pu Zhao, Yanyu Li, Yuxuan Cai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Network Pruning via Performance Maximization.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Gao_Network_Pruning_via_Performance_Maximization_CVPR_2021_paper.html) · 📚 被引 110
- **作者**: Shangqian Gao, Feihu Huang, Weidong Cai, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Learnable Motion Coherence for Correspondence Pruning.
- **链接**: [arXiv:2011.14563](https://arxiv.org/abs/2011.14563) · 📚 被引 62
- **作者**: Yuan Liu, Lingjie Liu, Cheng Lin, Zhen Dong, Wenping Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Achieving on-Mobile Real-Time Super-Resolution with Neural Architecture and Pruning Search.
- **链接**: [arXiv:2108.08910](https://arxiv.org/abs/2108.08910) · 📚 被引 52
- **作者**: Zheng Zhan, Yifan Gong, Pu Zhao, Geng Yuan, Wei Niu, Yushu Wu et al.
- **🏷️ 机构**: Northeastern University, College of William &#x0026; Mary, Cleveland State University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motion coherence is an important clue for distinguishing true correspondences from false ones. Modeling motion coherence on sparse putative correspondences is challenging due to their sparsity and uneven distributions. Existing works on motion coherence are sensitive to parameter settings and have difficulty in dealing with complex motion patterns. In this paper, we introduce a network called Laplacian Motion Coherence Network (LMCNet) to learn motion coherence property for correspondence pruning. We propose a novel formulation of fitting coherent motions with a smooth function on a graph of correspondences and show that this formulation allows a closed-form solution by graph Laplacian. This closed-form solution enables us to design a differentiable layer in a learning framework to capture global motion coherence from putative correspondences. The global motion coherence is further combined with local coherence extracted by another local layer to robustly detect inlier correspondences. Experiments demonstrate that LMCNet has superior performances to the state of the art in relative camera pose estimation and correspondences pruning of dynamic scenes.

</details>

### Manifold Regularized Dynamic Network Pruning.
- **链接**: [arXiv:2103.05861](https://arxiv.org/abs/2103.05861) · 📚 被引 87
- **作者**: Yehui Tang, Yunhe Wang, Yixing Xu, Yiping Deng, Chao Xu, Dacheng Tao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural network pruning is an essential approach for reducing the computational complexity of deep models so that they can be well deployed on resource-limited devices. Compared with conventional methods, the recently developed dynamic pruning methods determine redundant filters variant to each input instance which achieves higher acceleration. Most of the existing methods discover effective sub-networks for each instance independently and do not utilize the relationship between different inputs. To maximally excavate redundancy in the given network architecture, this paper proposes a new paradigm that dynamically removes redundant filters by embedding the manifold information of all instances into the space of pruned networks (dubbed as ManiDP). We first investigate the recognition complexity and feature similarity between images in the training set. Then, the manifold relationship between instances and the pruned sub-networks will be aligned in the training procedure. The effectiveness of the proposed method is verified on several benchmarks, which shows better performance in terms of both accuracy and computational cost compared to the state-of-the-art methods. For example, our method can reduce 55.3% FLOPs of ResNet-34 with only 0.57% top-1 accuracy degradation on ImageNet.

</details>

### Convolutional Neural Network Pruning With Structural Redundancy Reduction.
- **链接**: [arXiv:2104.03438](https://arxiv.org/abs/2104.03438) · 📚 被引 175
- **作者**: Zi Wang, Chengcheng Li, Xiangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolutional neural network (CNN) pruning has become one of the most successful network compression approaches in recent years. Existing works on network pruning usually focus on removing the least important filters in the network to achieve compact architectures. In this study, we claim that identifying structural redundancy plays a more essential role than finding unimportant filters, theoretically and empirically. We first statistically model the network pruning problem in a redundancy reduction perspective and find that pruning in the layer(s) with the most structural redundancy outperforms pruning the least important filters across all layers. Based on this finding, we then propose a network pruning approach that identifies structural redundancy of a CNN and prunes filters in the selected layer(s) with the most redundancy. Experiments on various benchmark network architectures and datasets show that our proposed approach significantly outperforms the previous state-of-the-art.

</details>

### Joint-DetNAS: Upgrade Your Detector With NAS, Pruning and Dynamic Distillation.
- **链接**: [arXiv:2105.12971](https://arxiv.org/abs/2105.12971) · 📚 被引 25
- **作者**: Lewei Yao, Renjie Pi, Hang Xu, Wei Zhang, Zhenguo Li, Tong Zhang
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Joint-DetNAS, a unified NAS framework for object detection, which integrates 3 key components: Neural Architecture Search, pruning, and Knowledge Distillation. Instead of naively pipelining these techniques, our Joint-DetNAS optimizes them jointly. The algorithm consists of two core processes: student morphism optimizes the student's architecture and removes the redundant parameters, while dynamic distillation aims to find the optimal matching teacher. For student morphism, weight inheritance strategy is adopted, allowing the student to flexibly update its architecture while fully utilize the predecessor's weights, which considerably accelerates the search; To facilitate dynamic distillation, an elastic teacher pool is trained via integrated progressive shrinking strategy, from which teacher detectors can be sampled without additional cost in subsequent searches. Given a base detector as the input, our algorithm directly outputs the derived student detector with high performance without additional training. Experiments demonstrate that our Joint-DetNAS outperforms the naive pipelining approach by a great margin. Given a classic R101-FPN as the base detector, Joint-DetNAS is able to boost its mAP from 41.4 to 43.9 on MS COCO and reduce the latency by 47%, which is on par with the SOTA EfficientDet while requiring less search cost. We hope our proposed method can provide the community with a new way of jointly optimizing NAS, KD and pruning.

</details>

### Multi-Decoding Deraining Network and Quasi-Sparsity Based Training.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Multi-Decoding_Deraining_Network_and_Quasi-Sparsity_Based_Training_CVPR_2021_paper.html) · 📚 被引 33
- **作者**: Yinglong Wang, Chao Ma, Bing Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Exploring Sparsity in Image Super-Resolution for Efficient Inference.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Exploring_Sparsity_in_Image_Super-Resolution_for_Efficient_Inference_CVPR_2021_paper.html) · 📚 被引 291
- **作者**: Longguang Wang, Xiaoyu Dong, Yingqian Wang, Xinyi Ying, Zaiping Lin, Wei An et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Effective Sparsification of Neural Networks With Global Sparsity Constraint.
- **链接**: [arXiv:2105.01571](https://arxiv.org/abs/2105.01571) · 📚 被引 32
- **作者**: Xiao Zhou, Weizhong Zhang, Hang Xu, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weight pruning is an effective technique to reduce the model size and inference time for deep neural networks in real-world deployments. However, since magnitudes and relative importance of weights are very different for different layers of a neural network, existing methods rely on either manual tuning or handcrafted heuristic rules to find appropriate pruning rates individually for each layer. This approach generally leads to suboptimal performance. In this paper, by directly working on the probability space, we propose an effective network sparsification method called {\it probabilistic masking} (ProbMask), which solves a natural sparsification formulation under global sparsity constraint. The key idea is to use probability as a global criterion for all layers to measure the weight importance. An appealing feature of ProbMask is that the amounts of weight redundancy can be learned automatically via our constraint and thus we avoid the problem of tuning pruning rates individually for different layers in a network. Extensive experimental results on CIFAR-10/100 and ImageNet demonstrate that our method is highly effective, and can outperform previous state-of-the-art methods by a significant margin, especially in the high pruning rate situation. Notably, the gap of Top-1 accuracy between our ProbMask and existing methods can be up to 10\%. As a by-product, we show ProbMask is also highly effective in identifying supermasks, which are subnetworks with high performance in a randomly weighted dense neural network.

</details>

## 跨领域论文（完整笔记在其他领域）

- VoxelContext-Net: An Octree Based Framework for Point Cloud Compression. → [3d-detection](../3d-detection/Guideline%202021.md)
