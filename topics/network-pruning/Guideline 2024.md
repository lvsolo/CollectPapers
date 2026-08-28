# Network Pruning — 2024 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DSPDet3D: 3D Small Object Detection with Dynamic Spatial Pruning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73390-1_21) · 📚 被引 10
- **作者**: Xiuwei Xu, Zhihao Sun, Ziwei Wang, Hongmin Liu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### LPViT: Low-Power Semi-structured Pruning for Vision Transformers.
- **链接**: [arXiv:2407.02068](https://arxiv.org/abs/2407.02068) · [代码](https://github.com/Akimoto-Cris/LPViT) · 📚 被引 7
- **作者**: Kaixin Xu, Zhe Wang, Chunyun Chen, Xue Geng, Jie Lin, Xulei Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have emerged as a promising alternative to convolutional neural networks for various image analysis tasks, offering comparable or superior performance. However, one significant drawback of ViTs is their resource-intensive nature, leading to increased memory footprint, computation complexity, and power consumption. To democratize this high-performance technology and make it more environmentally friendly, it is essential to compress ViT models, reducing their resource requirements while maintaining high performance. In this paper, we introduce a new block-structured pruning to address the resource-intensive issue for ViTs, offering a balanced trade-off between accuracy and hardware acceleration. Unlike unstructured pruning or channel-wise structured pruning, block pruning leverages the block-wise structure of linear layers, resulting in more efficient matrix multiplications. To optimize this pruning scheme, our paper proposes a novel hardware-aware learning objective that simultaneously maximizes speedup and minimizes power consumption during inference, tailored to the block sparsity structure. This objective eliminates the need for empirical look-up tables and focuses solely on reducing parametrized layer connections. Moreover, our paper provides a lightweight algorithm to achieve post-training pruning for ViTs, utilizing second-order Taylor approximation and empirical optimization to solve the proposed hardware-aware objective. Extensive experiments on ImageNet are conducted across various ViT architectures, including DeiT-B and DeiT-S, demonstrating competitive performance with other pruning methods and achieving a remarkable balance between accuracy preservation and power savings. Especially, we achieve 3.93x speedup on dedicated hardware and GPUs respectively for DeiT-B, and a power reduction by 1.4x on GPUs. Code released to https://github.com/Akimoto-Cris/LPViT.

</details>

### Non-transferable Pruning.
- **链接**: [arXiv:2410.08015](https://arxiv.org/abs/2410.08015)
- **作者**: Ruyi Ding, Lili Su, Aidong Adam Ding, Yunsi Fei
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained Deep Neural Networks (DNNs), developed from extensive datasets to integrate multifaceted knowledge, are increasingly recognized as valuable intellectual property (IP). To safeguard these models against IP infringement, strategies for ownership verification and usage authorization have emerged. Unlike most existing IP protection strategies that concentrate on restricting direct access to the model, our study addresses an extended DNN IP issue: applicability authorization, aiming to prevent the misuse of learned knowledge, particularly in unauthorized transfer learning scenarios. We propose Non-Transferable Pruning (NTP), a novel IP protection method that leverages model pruning to control a pretrained DNN's transferability to unauthorized data domains. Selective pruning can deliberately diminish a model's suitability on unauthorized domains, even with full fine-tuning. Specifically, our framework employs the alternating direction method of multipliers (ADMM) for optimizing both the model sparsity and an innovative non-transferable learning loss, augmented with Fisher space discriminative regularization, to constrain the model's generalizability to the target dataset. We also propose a novel effective metric to measure the model non-transferability: Area Under the Sample-wise Learning Curve (SLC-AUC). This metric facilitates consideration of full fine-tuning across various sample sizes. Experimental results demonstrate that NTP significantly surpasses the state-of-the-art non-transferable learning methods, with an average SLC-AUC at $-0.54$ across diverse pairs of source and target domains, indicating that models trained with NTP do not suit for transfer learning to unauthorized target domains. The efficacy of NTP is validated in both supervised and self-supervised learning contexts, confirming its applicability in real-world scenarios.

</details>

### Isomorphic Pruning for Vision Models.
- **链接**: [arXiv:2407.04616](https://arxiv.org/abs/2407.04616) · [代码](https://github.com/VainF/Isomorphic-Pruning) · 📚 被引 19
- **作者**: Gongfan Fang, Xinyin Ma, Michael Bi Mi, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning reduces the computational overhead of deep neural networks by removing redundant sub-structures. However, assessing the relative importance of different sub-structures remains a significant challenge, particularly in advanced vision models featuring novel mechanisms and architectures like self-attention, depth-wise convolutions, or residual connections. These heterogeneous substructures usually exhibit diverged parameter scales, weight distributions, and computational topology, introducing considerable difficulty to importance comparison. To overcome this, we present Isomorphic Pruning, a simple approach that demonstrates effectiveness across a range of network architectures such as Vision Transformers and CNNs, and delivers competitive performance across different model sizes. Isomorphic Pruning originates from an observation that, when evaluated under a pre-defined importance criterion, heterogeneous sub-structures demonstrate significant divergence in their importance distribution, as opposed to isomorphic structures that present similar importance patterns. This inspires us to perform isolated ranking and comparison on different types of sub-structures for more reliable pruning. Our empirical results on ImageNet-1K demonstrate that Isomorphic Pruning surpasses several pruning baselines dedicatedly designed for Transformers or CNNs. For instance, we improve the accuracy of DeiT-Tiny from 74.52% to 77.50% by pruning an off-the-shelf DeiT-Base model. And for ConvNext-Tiny, we enhanced performance from 82.06% to 82.18%, while reducing the number of parameters and memory usage. Code is available at \url{https://github.com/VainF/Isomorphic-Pruning}.

</details>

### Straightforward Layer-Wise Pruning for More Efficient Visual Adaptation.
- **链接**: [arXiv:2407.14330](https://arxiv.org/abs/2407.14330) · 📚 被引 4
- **作者**: Ruizi Han, Jinglei Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Parameter-efficient transfer learning (PETL) aims to adapt large pre-trained models using limited parameters. While most PETL approaches update the added parameters and freeze pre-trained weights during training, the minimal impact of task-specific deep layers on cross-domain data poses a challenge as PETL cannot modify them, resulting in redundant model structures. Structural pruning effectively reduces model redundancy; however, common pruning methods often lead to an excessive increase in stored parameters due to varying pruning structures based on pruning rates and data. Recognizing the storage parameter volume issue, we propose a Straightforward layer-wise pruning method, called SLS, for pruning PETL-transferred models. By evaluating parameters from a feature perspective of each layer and utilizing clustering metrics to assess current parameters based on clustering phenomena in low-dimensional space obtained through t-SNE, SLS facilitates informed pruning decisions. Our study reveals that layer-wise pruning, with a focus on storing pruning indices, addresses storage volume concerns. Notably, mainstream Layer-wise pruning methods may not be suitable for assessing layer importance in PETL-transferred models, where the majority of parameters are pre-trained and have limited relevance to downstream datasets. Comparative analysis against state-of-the-art PETL methods demonstrates that the pruned model achieved a notable balance between model throughput and accuracy. Moreover, SLS effectively reduces storage overhead arising from varying pruned structures while enhancing the accuracy and speed of pruned models compared to conventional pruning methods.

</details>

### IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72643-9_13) · 📚 被引 8
- **作者**: Kai Huang, Hao Zou, Ye Xi, Bochen Wang, Zhen Xie, Liang Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### PaPr: Training-Free One-Step Patch Pruning with Lightweight ConvNets for Faster Inference.
- **链接**: [arXiv:2403.16020](https://arxiv.org/abs/2403.16020) · [代码](https://github.com/tanvir-utexas/PaPr) · 📚 被引 4
- **作者**: Tanvir Mahmud, Burhaneddin Yaman, Chun-Hao Liu, Diana Marculescu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As deep neural networks evolve from convolutional neural networks (ConvNets) to advanced vision transformers (ViTs), there is an increased need to eliminate redundant data for faster processing without compromising accuracy. Previous methods are often architecture-specific or necessitate re-training, restricting their applicability with frequent model updates. To solve this, we first introduce a novel property of lightweight ConvNets: their ability to identify key discriminative patch regions in images, irrespective of model's final accuracy or size. We demonstrate that fully-connected layers are the primary bottleneck for ConvNets performance, and their suppression with simple weight recalibration markedly enhances discriminative patch localization performance. Using this insight, we introduce PaPr, a method for substantially pruning redundant patches with minimal accuracy loss using lightweight ConvNets across a variety of deep learning architectures, including ViTs, ConvNets, and hybrid transformers, without any re-training. Moreover, the simple early-stage one-step patch pruning with PaPr enhances existing patch reduction methods. Through extensive testing on diverse architectures, PaPr achieves significantly higher accuracy over state-of-the-art patch reduction methods with similar FLOP count reduction. More specifically, PaPr reduces about 70% of redundant patches in videos with less than 0.8% drop in accuracy, and up to 3.7x FLOPs reduction, which is a 15% more reduction with 2.5% higher accuracy. Code is released at https://github.com/tanvir-utexas/PaPr.

</details>

### SNP: Structured Neuron-Level Pruning to Preserve Attention Scores.
- **链接**: [arXiv:2404.11630](https://arxiv.org/abs/2404.11630) · 📚 被引 3
- **作者**: Kyunghwan Shim, Jaewoong Yun, Shinkook Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-head self-attention (MSA) is a key component of Vision Transformers (ViTs), which have achieved great success in various vision tasks. However, their high computational cost and memory footprint hinder their deployment on resource-constrained devices. Conventional pruning approaches can only compress and accelerate the MSA module using head pruning, although the head is not an atomic unit. To address this issue, we propose a novel graph-aware neuron-level pruning method, Structured Neuron-level Pruning (SNP). SNP prunes neurons with less informative attention scores and eliminates redundancy among heads. Specifically, it prunes graphically connected query and key layers having the least informative attention scores while preserving the overall attention scores. Value layers, which can be pruned independently, are pruned to eliminate inter-head redundancy. Our proposed method effectively compresses and accelerates Transformer-based models for both edge devices and server processors. For instance, the DeiT-Small with SNP runs 3.1$\times$ faster than the original model and achieves performance that is 21.94\% faster and 1.12\% higher than the DeiT-Tiny. Additionally, SNP combine successfully with conventional head or block pruning approaches. SNP with head pruning could compress the DeiT-Base by 80\% of the parameters and computational costs and achieve 3.85$\times$ faster inference speed on RTX3090 and 4.93$\times$ on Jetson Nano.

</details>

### GTPT: Group-Based Token Pruning Transformer for Efficient Human Pose Estimation.
- **链接**: [arXiv:2407.10756](https://arxiv.org/abs/2407.10756) · 📚 被引 6
- **作者**: Haonan Wang, Jie Liu, Jie Tang, Gangshan Wu, Bo Xu, Yanbing Chou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, 2D human pose estimation has made significant progress on public benchmarks. However, many of these approaches face challenges of less applicability in the industrial community due to the large number of parametric quantities and computational overhead. Efficient human pose estimation remains a hurdle, especially for whole-body pose estimation with numerous keypoints. While most current methods for efficient human pose estimation primarily rely on CNNs, we propose the Group-based Token Pruning Transformer (GTPT) that fully harnesses the advantages of the Transformer. GTPT alleviates the computational burden by gradually introducing keypoints in a coarse-to-fine manner. It minimizes the computation overhead while ensuring high performance. Besides, GTPT groups keypoint tokens and prunes visual tokens to improve model performance while reducing redundancy. We propose the Multi-Head Group Attention (MHGA) between different groups to achieve global interaction with little computational overhead. We conducted experiments on COCO and COCO-WholeBody. Compared to other methods, the experimental results show that GTPT can achieve higher performance with less computation, especially in whole-body with numerous keypoints.

</details>

### ELSE: Efficient Deep Neural Network Inference Through Line-Based Sparsity Exploration.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73247-8_24) · 📚 被引 0
- **作者**: Zeqi Zhu, Alberto García-Ortiz, Luc Waeijen, Egor Bondarev, Arash Pourtaherian, Orlando Moreira
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

## 跨领域论文（完整笔记在其他领域）

- Make Your ViT-Based Multi-view 3D Detectors Faster via Token Compression. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Distill Gold from Massive Ores: Bi-level Data Pruning Towards Efficient Dataset Distillation. → [knowledge-distillation](../knowledge-distillation/Guideline%202024.md)
