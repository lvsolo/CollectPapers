# Network Pruning — 2025 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 23 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### General Compression Framework for Efficient Transformer Object Tracking.
- **链接**: [arXiv:2409.17564](https://arxiv.org/abs/2409.17564) · [代码](https://github.com/LingyiHongfd/CompressTracker) · 📚 被引 3
- **作者**: Lingyi Hong, Jinglun Li, Xinyu Zhou, Shilin Yan, Pinxue Guo, Kaixun Jiang et al.
- **🏷️ 机构**: College of Computer Science and Artificial Intelligence, Fudan University,Shanghai Key Lab of Intelligent Information Processing,China, College of Intelligent Robotics and Advanced Manufacturing, Fudan University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous works have attempted to improve tracking efficiency through lightweight architecture design or knowledge distillation from teacher models to compact student trackers. However, these solutions often sacrifice accuracy for speed to a great extent, and also have the problems of complex training process and structural limitations. Thus, we propose a general model compression framework for efficient transformer object tracking, named CompressTracker, to reduce model size while preserving tracking accuracy. Our approach features a novel stage division strategy that segments the transformer layers of the teacher model into distinct stages to break the limitation of model structure. Additionally, we also design a unique replacement training technique that randomly substitutes specific stages in the student model with those from the teacher model, as opposed to training the student model in isolation. Replacement training enhances the student model's ability to replicate the teacher model's behavior and simplifies the training process. To further forcing student model to emulate teacher model, we incorporate prediction guidance and stage-wise feature mimicking to provide additional supervision during the teacher model's compression process. CompressTracker is structurally agnostic, making it compatible with any transformer architecture. We conduct a series of experiment to verify the effectiveness and generalizability of our CompressTracker. Our CompressTracker-SUTrack, compressed from SUTrack, retains about 99 performance on LaSOT (72.2 AUC) while achieves 2.42x speed up. Code is available at https://github.com/LingyiHongfd/CompressTracker.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the substantial advancements demonstrated by learning-based neural models in the LiDAR Point Cloud Compression (LPCC) task, realizing real-time compression - an indispensable criterion for numerous industrial applications - remains a formidable challenge. This paper proposes RENO, the first real-time neural codec for 3D LiDAR point clouds, achieving superior performance with a lightweight model. RENO skips the octree construction and directly builds upon the multiscale sparse tensor representation. Instead of the multi-stage inferring, RENO devises sparse occupancy codes, which exploit cross-scale correlation and derive voxels' occupancy in a one-shot manner, greatly saving processing time. Experimental results demonstrate that the proposed RENO achieves real-time coding speed, 10 fps at 14-bit depth on a desktop platform (e.g., one RTX 3090 GPU) for both encoding and decoding processes, while providing 12.25% and 48.34% bit-rate savings compared to G-PCCv23 and Draco, respectively, at a similar quality. RENO model size is merely 1MB, making it attractive for practical applications. The source code is available at https://github.com/NJUVISION/RENO.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Gaussian and Laplacian entropy models are proved effective in learned point cloud attribute compression, as they assist in arithmetic coding of latents. However, we demonstrate through experiments that there is still unutilized information in entropy parameters estimated by neural networks in current methods, which can be used for more accurate probability estimation. Thus we introduce generalized Gaussian entropy model, which controls the tail shape through shape parameter to more accurately estimate the probability of latents. Meanwhile, to the best of our knowledge, existing methods use fixed likelihood intervals for each integer during arithmetic coding, which limits model performance. We propose Mean Error Discriminator (MED) to determine whether the entropy parameter estimation is accurate and then dynamically adjust likelihood intervals. Experiments show that our method significantly improves rate-distortion (RD) performance on three VAE-based models for point cloud attribute compression, and our method can be applied to other compression tasks, such as image and video compression.

</details>

### Cross-Granularity Online Optimization with Masked Compensated Information for Learned Image Compression.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01533) · 📚 被引 1
- **作者**: Haowei Kuang, Wenhan Yang, Zongming Guo, Jiaying Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China, Pengcheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

### PUP 3D-GS: Principled Uncertainty Pruning for 3D Gaussian Splatting.
- **链接**: [arXiv:2406.10219](https://arxiv.org/abs/2406.10219) · 📚 被引 37
- **作者**: Alex Hanson, Allen Tu, Vasu Singla, Mayuka Jayawardhana, Matthias Zwicker, Tom Goldstein
- **🏷️ 机构**: University of Maryland,College Park
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in novel view synthesis have enabled real-time rendering speeds with high reconstruction accuracy. 3D Gaussian Splatting (3D-GS), a foundational point-based parametric 3D scene representation, models scenes as large sets of 3D Gaussians. However, complex scenes can consist of millions of Gaussians, resulting in high storage and memory requirements that limit the viability of 3D-GS on devices with limited resources. Current techniques for compressing these pretrained models by pruning Gaussians rely on combining heuristics to determine which Gaussians to remove. At high compression ratios, these pruned scenes suffer from heavy degradation of visual fidelity and loss of foreground details. In this paper, we propose a principled sensitivity pruning score that preserves visual fidelity and foreground details at significantly higher compression ratios than existing approaches. It is computed as a second-order approximation of the reconstruction error on the training views with respect to the spatial parameters of each Gaussian. Additionally, we propose a multi-round prune-refine pipeline that can be applied to any pretrained 3D-GS model without changing its training pipeline. After pruning 90% of Gaussians, a substantially higher percentage than previous methods, our PUP 3D-GS pipeline increases average rendering speed by 3.56$\times$ while retaining more salient foreground information and achieving higher image quality metrics than existing techniques on scenes from the Mip-NeRF 360, Tanks & Temples, and Deep Blending datasets.

</details>

### ATP: Adaptive Threshold Pruning for Efficient Data Encoding in Quantum Neural Networks.
- **链接**: [arXiv:2503.21815](https://arxiv.org/abs/2503.21815) · 📚 被引 3
- **作者**: Mohamed Afane, Gabrielle Ebbrecht, Ying Wang, Juntao Chen, Junaid Farooq
- **🏷️ 机构**: Fordham University, Stevens Institute of Technology, University of Michigan-Dearborn
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Quantum Neural Networks (QNNs) offer promising capabilities for complex data tasks, but are often constrained by limited qubit resources and high entanglement, which can hinder scalability and efficiency. In this paper, we introduce Adaptive Threshold Pruning (ATP), an encoding method that reduces entanglement and optimizes data complexity for efficient computations in QNNs. ATP dynamically prunes non-essential features in the data based on adaptive thresholds, effectively reducing quantum circuit requirements while preserving high performance. Extensive experiments across multiple datasets demonstrate that ATP reduces entanglement entropy and improves adversarial robustness when combined with adversarial training methods like FGSM. Our results highlight ATPs ability to balance computational efficiency and model resilience, achieving significant performance improvements with fewer resources, which will help make QNNs more feasible in practical, resource-constrained settings.

</details>

### PACT: Pruning and Clustering-Based Token Reduction for Faster Visual Language Models.
- **链接**: [arXiv:2504.08966](https://arxiv.org/abs/2504.08966) · 📚 被引 2
- **作者**: Mohamed Dhouib, Davide Buscaldi, Sonia Vanier, Aymen Shabou
- **🏷️ 机构**: LIX, &#x00C9;cole Polytechnique, IP,Paris,France, LIPN, Universit&#x00E9; Sorbonne Paris Nord,France, DataLab Groupe, Cr&#x00E9;dit Agricole S.A,France
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual Language Models require substantial computational resources for inference due to the additional input tokens needed to represent visual information. However, these visual tokens often contain redundant and unimportant information, resulting in an unnecessarily high number of tokens. To address this, we introduce PACT, a method that reduces inference time and memory usage by pruning irrelevant tokens and merging visually redundant ones at an early layer of the language model. Our approach uses a novel importance metric to identify unimportant tokens without relying on attention scores, making it compatible with FlashAttention. We also propose a novel clustering algorithm, called Distance Bounded Density Peak Clustering, which efficiently clusters visual tokens while constraining the distances between elements within a cluster by a predefined threshold. We demonstrate the effectiveness of PACT through extensive experiments.

</details>

### EfficientLLaVA: Generalizable Auto-Pruning for Large Vision-language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_EfficientLLaVA_Generalizable_Auto-Pruning_for_Large_Vision-language_Models_CVPR_2025_paper.html)
- **作者**: Yinan Liang, Ziwei Wang, Xiuwei Xu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### ICP: Immediate Compensation Pruning for Mid-to-high Sparsity.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Luo_ICP_Immediate_Compensation_Pruning_for_Mid-to-high_Sparsity_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Xin Luo, Xueming Fu, Zihang Jiang, S. Kevin Zhou
- **🏷️ 机构**: USTC,School of Biomedical Engineering, Division of Life Sciences and Medicine
- **会议**: CVPR 2025

### Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression.
- **链接**: [arXiv:2502.16638](https://arxiv.org/abs/2502.16638) · 📚 被引 21
- **作者**: Xiaoyi Qu, David Aponte, Colby R. Banbury, Daniel P. Robinson, Tianyu Ding, Kazuhito Koishida et al.
- **🏷️ 机构**: Lehigh University, Microsoft
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning and quantization are fundamental techniques used to reduce the size of deep neural networks (DNNs) and typically are applied independently. Applying these techniques jointly via co-optimization has the potential to produce smaller, high-quality models. However, existing joint schemes are not widely used because of (1) engineering difficulties (complicated multi-stage processes), (2) black-box optimization (extensive hyperparameter tuning to control the overall compression), and (3) insufficient architecture generalization. To address these limitations, we present the framework GETA, which automatically and efficiently performs joint structured pruning and quantization-aware training on any DNNs. GETA introduces three key innovations: (i) a quantization-aware dependency graph (QADG) that constructs a pruning search space for generic quantization-aware DNN, (ii) a partially projected stochastic gradient method that guarantees layerwise bit constraints are satisfied, and (iii) a new joint learning strategy that incorporates interpretable relationships between pruning and quantization. We present numerical experiments on both convolutional neural networks and transformer architectures that show that our approach achieves competitive (often superior) performance compared to existing joint pruning and quantization methods.

</details>

### MDP: Multidimensional Vision Model Pruning with Latency Constraint.
- **链接**: [arXiv:2504.02168](https://arxiv.org/abs/2504.02168) · 📚 被引 3
- **作者**: Xinglong Sun, Barath Lakshmanan, Maying Shen, Shiyi Lan, Jingde Chen, José M. Álvarez
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current structural pruning methods face two significant limitations: (i) they often limit pruning to finer-grained levels like channels, making aggressive parameter reduction challenging, and (ii) they focus heavily on parameter and FLOP reduction, with existing latency-aware methods frequently relying on simplistic, suboptimal linear models that fail to generalize well to transformers, where multiple interacting dimensions impact latency. In this paper, we address both limitations by introducing Multi-Dimensional Pruning (MDP), a novel paradigm that jointly optimizes across a variety of pruning granularities-including channels, query, key, heads, embeddings, and blocks. MDP employs an advanced latency modeling technique to accurately capture latency variations across all prunable dimensions, achieving an optimal balance between latency and accuracy. By reformulating pruning as a Mixed-Integer Nonlinear Program (MINLP), MDP efficiently identifies the optimal pruned structure across all prunable dimensions while respecting latency constraints. This versatile framework supports both CNNs and transformers. Extensive experiments demonstrate that MDP significantly outperforms previous methods, especially at high pruning ratios. On ImageNet, MDP achieves a 28% speed increase with a +1.4 Top-1 accuracy improvement over prior work like HALP for ResNet50 pruning. Against the latest transformer pruning method, Isomorphic, MDP delivers an additional 37% acceleration with a +0.7 Top-1 accuracy improvement.

</details>

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
- **链接**: [arXiv:2503.19576](https://arxiv.org/abs/2503.19576) · 📚 被引 1
- **作者**: Dhananjaya Jayasundara, Sudarshan Rajagopalan, Yasiru Ranasinghe, Trac D. Tran, Vishal M. Patel
- **🏷️ 机构**: Johns Hopkins University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Implicit Neural Representations (INRs) are increasingly recognized as a versatile data modality for representing discretized signals, offering benefits such as infinite query resolution and reduced storage requirements. Existing signal compression approaches for INRs typically employ one of two strategies: 1. direct quantization with entropy coding of the trained INR; 2. deriving a latent code on top of the INR through a learnable transformation. Thus, their performance is heavily dependent on the quantization and entropy coding schemes employed. In this paper, we introduce SINR, an innovative compression algorithm that leverages the patterns in the vector spaces formed by weights of INRs. We compress these vector spaces using a high-dimensional sparse code within a dictionary. Further analysis reveals that the atoms of the dictionary used to generate the sparse code do not need to be learned or transmitted to successfully recover the INR weights. We demonstrate that the proposed approach can be integrated with any existing INR-based signal compression technique. Our results indicate that SINR achieves substantial reductions in storage requirements for INRs across various configurations, outperforming conventional INR-based compression baselines. Furthermore, SINR maintains high-quality decoding across diverse data modalities, including images, occupancy fields, and Neural Radiance Fields.

</details>

### SURGEON: Memory-Adaptive Fully Test-Time Adaptation via Dynamic Activation Sparsity.
- **链接**: [arXiv:2503.20354](https://arxiv.org/abs/2503.20354) · 📚 被引 3
- **作者**: Ke Ma, Jiaqi Tang, Bin Guo, Fan Dang, Sicong Liu, Zhui Zhu et al.
- **🏷️ 机构**: Northwestern Polytechnical University, The Hong Kong University of Science and Technology, Beijing Jiaotong University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the growing integration of deep models into mobile terminals, the accuracy of these models declines significantly due to various deployment interferences. Test-time adaptation (TTA) has emerged to improve the performance of deep models by adapting them to unlabeled target data online. Yet, the significant memory cost, particularly in resource-constrained terminals, impedes the effective deployment of most backward-propagation-based TTA methods. To tackle memory constraints, we introduce SURGEON, a method that substantially reduces memory cost while preserving comparable accuracy improvements during fully test-time adaptation (FTTA) without relying on specific network architectures or modifications to the original training procedure. Specifically, we propose a novel dynamic activation sparsity strategy that directly prunes activations at layer-specific dynamic ratios during adaptation, allowing for flexible control of learning ability and memory cost in a data-sensitive manner. Among this, two metrics, Gradient Importance and Layer Activation Memory, are considered to determine the layer-wise pruning ratios, reflecting accuracy contribution and memory efficiency, respectively. Experimentally, our method surpasses the baselines by not only reducing memory usage but also achieving superior accuracy, delivering SOTA performance across diverse datasets, architectures, and tasks.

</details>

### Random Conditioning for Diffusion Model Compression with Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kim_Random_Conditioning_for_Diffusion_Model_Compression_with_Distillation_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Dohyun Kim, Sehwan Park, Geonhee Han, Seung Wook Kim, Paul Hongsuck Seo
- **🏷️ 机构**: Korea University,Dept. of CSE, NVIDIA
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models. → [multimodal](../multimodal/Guideline%202025.md)
- CASP: Compression of Large Multimodal Models Based on Attention Sparsity. → [multimodal](../multimodal/Guideline%202025.md)
- FlashSloth : Lightning Multimodal Large Language Models via Embedded Visual Compression. → [multimodal](../multimodal/Guideline%202025.md)
- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding. → [3d-detection](../3d-detection/Guideline%202025.md)
