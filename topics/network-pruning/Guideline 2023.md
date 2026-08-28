# Network Pruning — 2023 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Dynamic Token Pruning in Plain Vision Transformers for Semantic Segmentation.
- **链接**: [arXiv:2308.01045](https://arxiv.org/abs/2308.01045) · 📚 被引 50
- **作者**: Quan Tang, Bowen Zhang, Jiajun Liu, Fagui Liu, Yifan Liu
- **🏷️ 机构**: South China University of Technology, The University of Adelaide, CSIRO
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have achieved leading performance on various visual tasks yet still suffer from high computational complexity. The situation deteriorates in dense prediction tasks like semantic segmentation, as high-resolution inputs and outputs usually imply more tokens involved in computations. Directly removing the less attentive tokens has been discussed for the image classification task but can not be extended to semantic segmentation since a dense prediction is required for every patch. To this end, this work introduces a Dynamic Token Pruning (DToP) method based on the early exit of tokens for semantic segmentation. Motivated by the coarse-to-fine segmentation process by humans, we naturally split the widely adopted auxiliary-loss-based network architecture into several stages, where each auxiliary block grades every token's difficulty level. We can finalize the prediction of easy tokens in advance without completing the entire forward pass. Moreover, we keep $k$ highest confidence tokens for each semantic category to uphold the representative context information. Thus, computational complexity will change with the difficulty of the input, akin to the way humans do segmentation. Experiments suggest that the proposed DToP architecture reduces on average $20\% - 35\%$ of computational cost for current semantic segmentation methods based on plain vision transformers without accuracy degradation.

</details>

### DiffRate : Differentiable Compression Rate for Efficient Vision Transformers.
- **链接**: [arXiv:2305.17997](https://arxiv.org/abs/2305.17997) · [代码](https://github.com/OpenGVLab/DiffRate) · 📚 被引 38
- **作者**: Mengzhao Chen, Wenqi Shao, Peng Xu, Mingbao Lin, Kaipeng Zhang, Fei Chao et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China, School of Informatics, Shanghai AI Laboratory,OpenGVLab, Tencent Holdings Ltd
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Token compression aims to speed up large-scale vision transformers (e.g. ViTs) by pruning (dropping) or merging tokens. It is an important but challenging task. Although recent advanced approaches achieved great success, they need to carefully handcraft a compression rate (i.e. number of tokens to remove), which is tedious and leads to sub-optimal performance. To tackle this problem, we propose Differentiable Compression Rate (DiffRate), a novel token compression method that has several appealing properties prior arts do not have. First, DiffRate enables propagating the loss function's gradient onto the compression ratio, which is considered as a non-differentiable hyperparameter in previous work. In this case, different layers can automatically learn different compression rates layer-wisely without extra overhead. Second, token pruning and merging can be naturally performed simultaneously in DiffRate, while they were isolated in previous works. Third, extensive experiments demonstrate that DiffRate achieves state-of-the-art performance. For example, by applying the learned layer-wise compression rates to an off-the-shelf ViT-H (MAE) model, we achieve a 40% FLOPs reduction and a 1.5x throughput improvement, with a minor accuracy drop of 0.16% on ImageNet without fine-tuning, even outperforming previous methods with fine-tuning. Codes and models are available at https://github.com/OpenGVLab/DiffRate.

</details>

### Single-Shot Pruning for Pre-trained Models: Rethinking the Importance of Magnitude Pruning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00155) · 📚 被引 13
- **作者**: Hirokazu Kohama, Hiroaki Minoura, Tsubasa Hirakawa, Takayoshi Yamashita, Hironobu Fujiyoshi
- **🏷️ 机构**: Chubu University
- **会议**: ICCV 2023

### Automatic Network Pruning via Hilbert-Schmidt Independence Criterion Lasso under Information Bottleneck Principle.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01601) · 📚 被引 22
- **作者**: Song Guo, Lei Zhang, Xiawu Zheng, Yan Wang, Yuchao Li, Fei Chao et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,Department of Artificial Intelligence, School of Informatics, Samsara Inc, Alibaba Group
- **会议**: ICCV 2023

### Unified Data-Free Compression: Pruning and Quantization without Fine-Tuning.
- **链接**: [arXiv:2308.07209](https://arxiv.org/abs/2308.07209) · 📚 被引 22
- **作者**: Shipeng Bai, Jun Chen, Xintian Shen, Yixuan Qian, Yong Liu
- **🏷️ 机构**: Zhejiang University,College of Control Science and Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning and quantization are promising approaches for reducing the inference time and memory footprint of neural networks. However, most existing methods require the original training dataset to fine-tune the model. This not only brings heavy resource consumption but also is not possible for applications with sensitive or proprietary data due to privacy and security concerns. Therefore, a few data-free methods are proposed to address this problem, but they perform data-free pruning and quantization separately, which does not explore the complementarity of pruning and quantization. In this paper, we propose a novel framework named Unified Data-Free Compression(UDFC), which performs pruning and quantization simultaneously without any data and fine-tuning process. Specifically, UDFC starts with the assumption that the partial information of a damaged(e.g., pruned or quantized) channel can be preserved by a linear combination of other channels, and then derives the reconstruction form from the assumption to restore the information loss due to compression. Finally, we formulate the reconstruction error between the original network and its compressed network, and theoretically deduce the closed-form solution. We evaluate the UDFC on the large-scale image classification task and obtain significant improvements over various network architectures and compression methods. For example, we achieve a 20.54% accuracy improvement on ImageNet dataset compared to SOTA method with 30% pruning ratio and 6-bit quantization on ResNet-34.

</details>

### Structural Alignment for Network Pruning through Partial Regularization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01596) · 📚 被引 23
- **作者**: Shangqian Gao, Zeyu Zhang, Yanfu Zhang, Feihu Huang, Heng Huang
- **🏷️ 机构**: University of Pittsburgh,Department of Electrical and Computer Engineering, University of Arizona,School of Information, University of Maryland at College Park,Department of Computer Science
- **会议**: ICCV 2023

### Differentiable Transportation Pruning.
- **链接**: [arXiv:2307.08483](https://arxiv.org/abs/2307.08483)
- **作者**: Yunqiang Li, Jan C. van Gemert, Torsten Hoefler, Bert Moons, Evangelos Eleftheriou, Bram-Ernst Verhoef
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning algorithms are increasingly employed at the edge. However, edge devices are resource constrained and thus require efficient deployment of deep neural networks. Pruning methods are a key tool for edge deployment as they can improve storage, compute, memory bandwidth, and energy usage. In this paper we propose a novel accurate pruning technique that allows precise control over the output network size. Our method uses an efficient optimal transportation scheme which we make end-to-end differentiable and which automatically tunes the exploration-exploitation behavior of the algorithm to find accurate sparse sub-networks. We show that our method achieves state-of-the-art performance compared to previous pruning methods on 3 different datasets, using 5 different models, across a wide range of pruning ratios, and with two types of sparsity budgets and pruning granularities.

</details>

### HollowNeRF: Pruning Hashgrid-Based NeRFs with Trainable Collision Mitigation.
- **链接**: [arXiv:2308.10122](https://arxiv.org/abs/2308.10122) · 📚 被引 15
- **作者**: Xiufeng Xie, Riccardo Gherardi, Zhihong Pan, Stephen Huang
- **🏷️ 机构**: Oppo Mobile Telecommunications Corp.,Palo Alto,CA,USA,94303
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural radiance fields (NeRF) have garnered significant attention, with recent works such as Instant-NGP accelerating NeRF training and evaluation through a combination of hashgrid-based positional encoding and neural networks. However, effectively leveraging the spatial sparsity of 3D scenes remains a challenge. To cull away unnecessary regions of the feature grid, existing solutions rely on prior knowledge of object shape or periodically estimate object shape during training by repeated model evaluations, which are costly and wasteful. To address this issue, we propose HollowNeRF, a novel compression solution for hashgrid-based NeRF which automatically sparsifies the feature grid during the training phase. Instead of directly compressing dense features, HollowNeRF trains a coarse 3D saliency mask that guides efficient feature pruning, and employs an alternating direction method of multipliers (ADMM) pruner to sparsify the 3D saliency mask during training. By exploiting the sparsity in the 3D scene to redistribute hash collisions, HollowNeRF improves rendering quality while using a fraction of the parameters of comparable state-of-the-art solutions, leading to a better cost-accuracy trade-off. Our method delivers comparable rendering quality to Instant-NGP, while utilizing just 31% of the parameters. In addition, our solution can achieve a PSNR accuracy gain of up to 1dB using only 56% of the parameters.

</details>

### Efficient Joint Optimization of Layer-Adaptive Weight Pruning in Deep Neural Networks.
- **链接**: [arXiv:2308.10438](https://arxiv.org/abs/2308.10438) · [代码](https://github.com/Akimoto-Cris/RD_VIT_PRUNE) · 📚 被引 29
- **作者**: Kaixin Xu, Zhe Wang, Xue Geng, Min Wu, Xiaoli Li, Weisi Lin
- **🏷️ 机构**: Technology and Research (A*STAR),Institute for Infocomm Research (I2R), Agency for Science,Singapore,138632, Nanyang Technological University,Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel layer-adaptive weight-pruning approach for Deep Neural Networks (DNNs) that addresses the challenge of optimizing the output distortion minimization while adhering to a target pruning ratio constraint. Our approach takes into account the collective influence of all layers to design a layer-adaptive pruning scheme. We discover and utilize a very important additivity property of output distortion caused by pruning weights on multiple layers. This property enables us to formulate the pruning as a combinatorial optimization problem and efficiently solve it through dynamic programming. By decomposing the problem into sub-problems, we achieve linear time complexity, making our optimization algorithm fast and feasible to run on CPUs. Our extensive experiments demonstrate the superiority of our approach over existing methods on the ImageNet and CIFAR-10 datasets. On CIFAR-10, our method achieves remarkable improvements, outperforming others by up to 1.0% for ResNet-32, 0.5% for VGG-16, and 0.7% for DenseNet-121 in terms of top-1 accuracy. On ImageNet, we achieve up to 4.7% and 4.6% higher top-1 accuracy compared to other methods for VGG-16 and ResNet-50, respectively. These results highlight the effectiveness and practicality of our approach for enhancing DNN performance through layer-adaptive weight pruning. Code will be available on https://github.com/Akimoto-Cris/RD_VIT_PRUNE.

</details>

### Towards Fairness-aware Adversarial Network Pruning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00477) · 📚 被引 6
- **作者**: Lei Zhang, Zhibo Wang, Xiaowei Dong, Yunhe Feng, Xiaoyi Pang, Zhifei Zhang et al.
- **🏷️ 机构**: Zhejiang University, Wuhan University, University of North Texas
- **会议**: ICCV 2023

### CoroNetGAN: Controlled Pruning of GANs via Hypernetworks.
- **链接**: [arXiv:2403.08261](https://arxiv.org/abs/2403.08261) · 📚 被引 3
- **作者**: Aman Kumar, Khushboo Anand, Shubham Mandloi, Ashutosh Mishra, Avinash Thakur, Neeraj Kasera et al.
- **🏷️ 机构**: OPPO Mobiles R &#x0026; D Center,Hyderabad,India, Indian Institute of Science,Bangalore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative Adversarial Networks (GANs) have proven to exhibit remarkable performance and are widely used across many generative computer vision applications. However, the unprecedented demand for the deployment of GANs on resource-constrained edge devices still poses a challenge due to huge number of parameters involved in the generation process. This has led to focused attention on the area of compressing GANs. Most of the existing works use knowledge distillation with the overhead of teacher dependency. Moreover, there is no ability to control the degree of compression in these methods. Hence, we propose CoroNet-GAN for compressing GAN using the combined strength of differentiable pruning method via hypernetworks. The proposed method provides the advantage of performing controllable compression while training along with reducing training time by a substantial factor. Experiments have been done on various conditional GAN architectures (Pix2Pix and CycleGAN) to signify the effectiveness of our approach on multiple benchmark datasets such as Edges-to-Shoes, Horse-to-Zebra and Summer-to-Winter. The results obtained illustrate that our approach succeeds to outperform the baselines on Zebra-to-Horse and Summer-to-Winter achieving the best FID score of 32.3 and 72.3 respectively, yielding high-fidelity images across all the datasets. Additionally, our approach also outperforms the state-of-the-art methods in achieving better inference time on various smart-phone chipsets and data-types making it a feasible solution for deployment on edge devices.

</details>

### Can Unstructured Pruning Reduce the Depth in Deep Neural Networks?
- **链接**: [arXiv:2308.06619](https://arxiv.org/abs/2308.06619) · 📚 被引 29
- **作者**: Zhu Liao, Victor Quétu, Van-Tam Nguyen, Enzo Tartaglione
- **🏷️ 机构**: Institut Polytechnique de Paris,LTCI, T&#x00E9;l&#x00E9;com Paris,France
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning is a widely used technique for reducing the size of deep neural networks while maintaining their performance. However, such a technique, despite being able to massively compress deep models, is hardly able to remove entire layers from a model (even when structured): is this an addressable task? In this study, we introduce EGP, an innovative Entropy Guided Pruning algorithm aimed at reducing the size of deep neural networks while preserving their performance. The key focus of EGP is to prioritize pruning connections in layers with low entropy, ultimately leading to their complete removal. Through extensive experiments conducted on popular models like ResNet-18 and Swin-T, our findings demonstrate that EGP effectively compresses deep neural networks while maintaining competitive performance levels. Our results not only shed light on the underlying mechanism behind the advantages of unstructured pruning, but also pave the way for further investigations into the intricate relationship between entropy, pruning techniques, and deep learning performance. The EGP algorithm and its insights hold great promise for advancing the field of network compression and optimization. The source code for EGP is released open-source.

</details>

### Shannon Strikes Again! Entropy-based Pruning in Deep Neural Networks for Transfer Learning under Extreme Memory and Computation Budgets.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00165) · 📚 被引 6
- **作者**: Gabriele Spadaro, Riccardo Renzulli, Andrea Bragagnolo, Jhony H. Giraldo, Attilio Fiandrotti, Marco Grangetto et al.
- **🏷️ 机构**: University of Turin,Computer Science Department,Italy, Independent Researcher, T&#x00E9;l&#x00E9;com Paris - Institut Polytechnique de Paris,LTCI,France
- **会议**: ICCV 2023

### Accelerating Deep Neural Networks via Semi-Structured Activation Sparsity.
- **链接**: [arXiv:2309.06626](https://arxiv.org/abs/2309.06626) · 📚 被引 2
- **作者**: Matteo Grimaldi, Darshan C. Ganji, Ivan Lazarevich, Sudhakar Sah Deeplite
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The demand for efficient processing of deep neural networks (DNNs) on embedded devices is a significant challenge limiting their deployment. Exploiting sparsity in the network's feature maps is one of the ways to reduce its inference latency. It is known that unstructured sparsity results in lower accuracy degradation with respect to structured sparsity but the former needs extensive inference engine changes to get latency benefits. To tackle this challenge, we propose a solution to induce semi-structured activation sparsity exploitable through minor runtime modifications. To attain high speedup levels at inference time, we design a sparse training procedure with awareness of the final position of the activations while computing the General Matrix Multiplication (GEMM). We extensively evaluate the proposed solution across various models for image classification and object detection tasks. Remarkably, our approach yields a speed improvement of $1.25 \times$ with a minimal accuracy drop of $1.1\%$ for the ResNet18 model on the ImageNet dataset. Furthermore, when combined with a state-of-the-art structured pruning method, the resulting models provide a good latency-accuracy trade-off, outperforming models that solely employ structured pruning techniques.

</details>

### Accumulation Knowledge Distillation for Conditional GAN Compression.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00140) · 📚 被引 1
- **作者**: Tingwei Gao, Rujiao Long
- **🏷️ 机构**: Alibaba Group
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- Growing a Brain with Sparsity-Inducing Generation for Continual Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
