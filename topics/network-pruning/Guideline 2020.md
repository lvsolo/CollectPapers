# Network Pruning — 2020 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DA-NAS: Data Adapted Pruning for Efficient Neural Architecture Search.
- **链接**: [arXiv:2003.12563](https://arxiv.org/abs/2003.12563) · 📚 被引 10
- **作者**: Xiyang Dai, Dongdong Chen, Mengchen Liu, Yinpeng Chen, Lu Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient search is a core issue in Neural Architecture Search (NAS). It is difficult for conventional NAS algorithms to directly search the architectures on large-scale tasks like ImageNet. In general, the cost of GPU hours for NAS grows with regard to training dataset size and candidate set size. One common way is searching on a smaller proxy dataset (e.g., CIFAR-10) and then transferring to the target task (e.g., ImageNet). These architectures optimized on proxy data are not guaranteed to be optimal on the target task. Another common way is learning with a smaller candidate set, which may require expert knowledge and indeed betrays the essence of NAS. In this paper, we present DA-NAS that can directly search the architecture for large-scale target tasks while allowing a large candidate set in a more efficient manner. Our method is based on an interesting observation that the learning speed for blocks in deep neural networks is related to the difficulty of recognizing distinct categories. We carefully design a progressive data adapted pruning strategy for efficient architecture search. It will quickly trim low performed blocks on a subset of target dataset (e.g., easy classes), and then gradually find the best blocks on the whole target dataset. At this time, the original candidate set becomes as compact as possible, providing a faster search in the target task. Experiments on ImageNet verify the effectiveness of our approach. It is 2x faster than previous methods while the accuracy is currently state-of-the-art, at 76.2% under small FLOPs constraint. It supports an argument search space (i.e., more candidate blocks) to efficiently search the best-performing architecture.

</details>

### DHP: Differentiable Meta Pruning via HyperNetworks.
- **链接**: [arXiv:2003.13683](https://arxiv.org/abs/2003.13683) · 📚 被引 91
- **作者**: Yawei Li, Shuhang Gu, Kai Zhang, Luc Van Gool, Radu Timofte
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Network pruning has been the driving force for the acceleration of neural networks and the alleviation of model storage/transmission burden. With the advent of AutoML and neural architecture search (NAS), pruning has become topical with automatic mechanism and searching based architecture optimization. Yet, current automatic designs rely on either reinforcement learning or evolutionary algorithm. Due to the non-differentiability of those algorithms, the pruning algorithm needs a long searching stage before reaching the convergence. To circumvent this problem, this paper introduces a differentiable pruning method via hypernetworks for automatic network pruning. The specifically designed hypernetworks take latent vectors as input and generate the weight parameters of the backbone network. The latent vectors control the output channels of the convolutional layers in the backbone network and act as a handle for the pruning of the layers. By enforcing $\ell_1$ sparsity regularization to the latent vectors and utilizing proximal gradient solver, sparse latent vectors can be obtained. Passing the sparsified latent vectors through the hypernetworks, the corresponding slices of the generated weight parameters can be removed, achieving the effect of network pruning. The latent vectors of all the layers are pruned together, resulting in an automatic layer configuration. Extensive experiments are conducted on various networks for image classification, single image super-resolution, and denoising. And the experimental results validate the proposed method.

</details>

### EagleEye: Fast Sub-net Evaluation for Efficient Neural Network Pruning.
- **链接**: [arXiv:2007.02491](https://arxiv.org/abs/2007.02491) · [代码](https://github.com/anonymous47823493/EagleEye) · 📚 被引 133
- **作者**: Bailin Li, Bowen Wu, Jiang Su, Guangrun Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Finding out the computational redundant part of a trained Deep Neural Network (DNN) is the key question that pruning algorithms target on. Many algorithms try to predict model performance of the pruned sub-nets by introducing various evaluation methods. But they are either inaccurate or very complicated for general application. In this work, we present a pruning method called EagleEye, in which a simple yet efficient evaluation component based on adaptive batch normalization is applied to unveil a strong correlation between different pruned DNN structures and their final settled accuracy. This strong correlation allows us to fast spot the pruned candidates with highest potential accuracy without actually fine-tuning them. This module is also general to plug-in and improve some existing pruning algorithms. EagleEye achieves better pruning performance than all of the studied pruning algorithms in our experiments. Concretely, to prune MobileNet V1 and ResNet-50, EagleEye outperforms all compared methods by up to 3.8%. Even in the more challenging experiments of pruning the compact model of MobileNet V1, EagleEye achieves the highest accuracy of 70.9% with an overall 50% operations (FLOPs) pruned. All accuracy results are Top-1 ImageNet classification accuracy. Source code and models are accessible to open-source community https://github.com/anonymous47823493/EagleEye .

</details>

### DSA: More Efficient Budgeted Pruning via Differentiable Sparsity Allocation.
- **链接**: [arXiv:2004.02164](https://arxiv.org/abs/2004.02164) · 📚 被引 69
- **作者**: Xuefei Ning, Tianchen Zhao, Wenshuo Li, Peng Lei, Yu Wang, Huazhong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Budgeted pruning is the problem of pruning under resource constraints. In budgeted pruning, how to distribute the resources across layers (i.e., sparsity allocation) is the key problem. Traditional methods solve it by discretely searching for the layer-wise pruning ratios, which lacks efficiency. In this paper, we propose Differentiable Sparsity Allocation (DSA), an efficient end-to-end budgeted pruning flow. Utilizing a novel differentiable pruning process, DSA finds the layer-wise pruning ratios with gradient-based optimization. It allocates sparsity in continuous space, which is more efficient than methods based on discrete evaluation and search. Furthermore, DSA could work in a pruning-from-scratch manner, whereas traditional budgeted pruning methods are applied to pre-trained models. Experimental results on CIFAR-10 and ImageNet show that DSA could achieve superior performance than current iterative budgeted pruning methods, and shorten the time cost of the overall pruning process by at least 1.5x in the meantime.

</details>

### Meta-learning with Network Pruning.
- **链接**: [arXiv:2007.03219](https://arxiv.org/abs/2007.03219)
- **作者**: Hongduan Tian, Bo Liu, Xiao-Tong Yuan, Qingshan Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Meta-learning is a powerful paradigm for few-shot learning. Although with remarkable success witnessed in many applications, the existing optimization based meta-learning models with over-parameterized neural networks have been evidenced to ovetfit on training tasks. To remedy this deficiency, we propose a network pruning based meta-learning approach for overfitting reduction via explicitly controlling the capacity of network. A uniform concentration analysis reveals the benefit of network capacity constraint for reducing generalization gap of the proposed meta-learner. We have implemented our approach on top of Reptile assembled with two network pruning routines: Dense-Sparse-Dense (DSD) and Iterative Hard Thresholding (IHT). Extensive experimental results on benchmark datasets with different over-parameterized deep networks demonstrate that our method not only effectively alleviates meta-overfitting but also in many cases improves the overall generalization performance when applied to few-shot classification tasks.

</details>

### Differentiable Joint Pruning and Quantization for Hardware Efficiency.
- **链接**: [arXiv:2007.10463](https://arxiv.org/abs/2007.10463) · 📚 被引 62
- **作者**: Ying Wang, Yadong Lu, Tijmen Blankevoort
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a differentiable joint pruning and quantization (DJPQ) scheme. We frame neural network compression as a joint gradient-based optimization problem, trading off between model pruning and quantization automatically for hardware efficiency. DJPQ incorporates variational information bottleneck based structured pruning and mixed-bit precision quantization into a single differentiable loss function. In contrast to previous works which consider pruning and quantization separately, our method enables users to find the optimal trade-off between both in a single training procedure. To utilize the method for more efficient hardware inference, we extend DJPQ to integrate structured pruning with power-of-two bit-restricted quantization. We show that DJPQ significantly reduces the number of Bit-Operations (BOPs) for several networks while maintaining the top-1 accuracy of original floating-point models (e.g., 53x BOPs reduction in ResNet18 on ImageNet, 43x in MobileNetV2). Compared to the conventional two-stage approach, which optimizes pruning and quantization independently, our scheme outperforms in terms of both accuracy and BOPs. Even when considering bit-restricted quantization, DJPQ achieves larger compression ratios and better accuracy than the two-stage approach.

</details>

### Accelerating CNN Training by Pruning Activation Gradients.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58595-2_20) · 📚 被引 22
- **作者**: Xucheng Ye, Pengcheng Dai, Junyu Luo, Xin Guo, Yingjie Qi, Jianlei Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### An Image Enhancing Pattern-Based Sparsity for Real-Time Inference on Mobile Devices.
- **链接**: [arXiv:2001.07710](https://arxiv.org/abs/2001.07710) · 📚 被引 15
- **作者**: Xiaolong Ma, Wei Niu, Tianyun Zhang, Sijia Liu, Sheng Lin, Hongjia Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weight pruning has been widely acknowledged as a straightforward and effective method to eliminate redundancy in Deep Neural Networks (DNN), thereby achieving acceleration on various platforms. However, most of the pruning techniques are essentially trade-offs between model accuracy and regularity which lead to impaired inference accuracy and limited on-device acceleration performance. To solve the problem, we introduce a new sparsity dimension, namely pattern-based sparsity that comprises pattern and connectivity sparsity, and becoming both highly accurate and hardware friendly. With carefully designed patterns, the proposed pruning unprecedentedly and consistently achieves accuracy enhancement and better feature extraction ability on different DNN structures and datasets, and our pattern-aware pruning framework also achieves pattern library extraction, pattern selection, pattern and connectivity pruning and weight training simultaneously. Our approach on the new pattern-based sparsity naturally fits into compiler optimization for highly efficient DNN execution on mobile platforms. To the best of our knowledge, it is the first time that mobile devices achieve real-time inference for the large-scale DNN models thanks to the unique spatial property of pattern-based sparsity and the help of the code generation capability of compilers.

</details>

### Online Ensemble Model Compression Using Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58529-7_2) · 📚 被引 42
- **作者**: Devesh Walawalkar, Zhiqiang Shen, Marios Savvides
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
