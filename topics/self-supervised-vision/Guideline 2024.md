# Self-supervised Vision — 2024 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 70 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### Towards Scalable 3D Anomaly Detection and Localization: A Benchmark via 3D Anomaly Synthesis and A Self-Supervised Learning Network. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2311.14897](https://arxiv.org/abs/2311.14897) · 📚 被引 50
- **作者**: Wenqiao Li, Xiaohao Xu, Yao Gu, Bozhong Zheng, Shenghua Gao, Yingna Wu
- **🏷️ 机构**: ShanghaiTech University, University of Michigan, Ann Arbor
- **会议**: CVPR 2024
- **摘要（中）**: 这篇论文针对3D异常检测中真实异常数据稀缺、限制模型可扩展性的问题。作者提出了一种3D异常合成流程，基于ShapeNet构建了包含40类1600个点云样本的Anomaly-ShapeNet数据集，并设计了一种自监督方法IMRNet，通过几何感知采样模块保留潜在异常区域，并利用掩码重建进行表示学习。相比现有方法，该方法提供了丰富多样的合成数据，增强了模型对工业场景的适应性。实验表明，该方法能有效训练模型并提升3D异常定位性能。
- **摘要（英）**: This paper addresses the scarcity of real 3D anomaly data that limits model scalability. It proposes a 3D anomaly synthesis pipeline to create Anomaly-ShapeNet with 1600 samples across 40 categories, and a self-supervised IMRNet with geometry-aware sampling and mask reconstruction. This approach provides rich training data and improves adaptability to industrial scenarios, with experiments showing effective anomaly localization.
- **核心贡献**: 提出了Anomaly-ShapeNet合成数据集和IMRNet自监督网络，用于可扩展的3D异常检测与定位。
- **创新点**: 利用几何感知采样和掩码重建实现自监督3D异常表示学习。
- **结果**: 在合成数据集上实现了有效的3D异常检测和定位，增强了模型泛化能力。

### SPU-PMD: Self-Supervised Point Cloud Upsampling via Progressive Mesh Deformation. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00496) · 📚 被引 16
- **作者**: Yanzhe Liu, Rong Chen, Yushi Li, Yixi Li, Xuehou Tan
- **🏷️ 机构**: Dalian Maritime University, Xi&#x0027;an Jiaotong-Liverpool University, Tokai University
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。根据标题推测，它可能针对点云上采样问题，提出了一种基于渐进网格变形的自监督方法。由于缺乏详细信息，无法评估其方法质量和效果。
- **摘要（英）**: The abstract is empty, so details are unavailable. Based on the title, it likely addresses point cloud upsampling via a self-supervised progressive mesh deformation approach. Quality and results cannot be assessed due to missing information.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Mitigating Object Dependencies: Improving Point Cloud Self-Supervised Learning Through Object Exchange. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2404.07504](https://arxiv.org/abs/2404.07504) · 📚 被引 5
- **作者**: Yanhao Wu, Tong Zhang, Wei Ke, Congpei Qiu, Sabine Süsstrunk, Mathieu Salzmann
- **🏷️ 机构**: School of Software Engineering, Xi&#x0027;an Jiaotong University,China, School of Computer and Communication Sciences, EPFL,Switzerland
- **会议**: CVPR 2024
- **摘要（中）**: 这篇论文针对室内点云场景中物体间强依赖关系导致网络忽略个体模式的问题。作者提出了一种新的自监督学习策略，通过物体交换策略在不同场景间交换相似大小的物体对，以解耦上下文依赖，并引入上下文感知特征学习，聚合跨场景物体特征以编码物体模式。相比现有SSL方法，该方法在特征鲁棒性和环境变化适应性上表现更优。实验表明，该方法在点云场景理解任务上超越了现有技术，并展示了良好的迁移能力。
- **摘要（英）**: This paper addresses the issue of strong inter-object dependencies in indoor point clouds that cause networks to bypass individual patterns. It proposes an SSL strategy with object exchange to disentangle context and context-aware feature learning to encode object patterns. The method outperforms existing SSL techniques in robustness and transferability, as shown in experiments.
- **核心贡献**: 提出了基于物体交换和上下文感知特征学习的自监督策略，提升点云特征鲁棒性。
- **创新点**: 通过物体交换解耦上下文依赖，并聚合跨场景特征学习物体模式。
- **结果**: 在点云场景理解任务上超越了现有SSL方法，并展现出更强的环境鲁棒性。

### Self-Supervised Multi-Object Tracking with Path Consistency. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2404.05136](https://arxiv.org/abs/2404.05136) · 📚 被引 15
- **作者**: Zijia Lu, Bing Shuai, Yanbei Chen, Zhenlin Xu, Davide Modolo
- **🏷️ 机构**: AWS AI Labs
- **会议**: CVPR 2024
- **摘要（中）**: 针对无监督多目标跟踪中缺乏身份监督导致目标匹配学习困难的问题，提出了路径一致性概念，通过让模型在不同帧跳过组合下生成多个关联结果，并强制这些结果一致来训练匹配模型。设计了路径一致性损失，仅用自监督信号训练，无需人工身份标注。在MOT17、PersonPath22和KITTI三个数据集上，该方法显著优于现有无监督方法，并接近监督方法的性能。
- **摘要（英）**: To learn robust object matching without identity supervision, this paper introduces path consistency, enforcing consistent association results across different frame-skipping observation paths. A path consistency loss trains the matching model purely self-supervised, outperforming existing unsupervised methods on MOT17, PersonPath22, and KITTI, approaching supervised performance.
- **核心贡献**: 提出路径一致性损失，实现无需身份标注的自监督多目标跟踪训练。
- **创新点**: 通过帧跳过生成多观测路径并强制关联一致性，创新性地利用观测不变性。
- **结果**: 在三个跟踪数据集上超越现有无监督方法，接近监督方法性能。

### Iterated Learning Improves Compositionality in Large Vision-Language Models. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2404.02145](https://arxiv.org/abs/2404.02145) · 📚 被引 3
- **作者**: Chenhao Zheng, Jieyu Zhang, Aniruddha Kembhavi, Ranjay Krishna
- **🏷️ 机构**: University of Michigan, University of Washington, Allen Institute for Artificial Intelligence
- **会议**: CVPR 2024
- **摘要（中）**: 针对大型视觉-语言模型在组合性理解上的不足，即难以区分细微差异的图像描述，提出了一种基于迭代学习的训练算法。该方法借鉴认知科学中的文化传播理论，将视觉-语言对比学习重构为Lewis信号博弈，并通过迭代重置一个智能体的权重来模拟文化传承，从而激励组合性语言的发展。相比仅增加模型规模或数据量，该方法在组合性任务上显著提升性能，但摘要未提供具体数值。
- **摘要（英）**: To address the compositional understanding deficiency in large vision-language models, we propose an iterated learning algorithm inspired by cultural transmission, reframing contrastive learning as a Lewis Signaling Game and iteratively resetting one agent's weights. This incentivizes the development of compositional representations, outperforming scale-based approaches, though specific metrics are not provided in the abstract.
- **核心贡献**: 提出迭代学习算法，通过文化传播机制提升VLM的组合性理解。
- **创新点**: 将对比学习重构为信号博弈，并引入迭代重置模拟文化传承。
- **结果**: 在组合性任务上显著提升，但具体数据未给出。

### Systematic comparison of semi-supervised and self-supervised learning for medical image classification. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02103) · 📚 被引 19
- **作者**: Zhe Huang, Ruijie Jiang, Shuchin Aeron, Michael C. Hughes
- **🏷️ 机构**: Tufts University, School of Engineering
- **会议**: CVPR 2024
- **摘要（中）**: ①针对医学图像分类中半监督和自监督学习方法的系统比较缺失问题。②对多种半监督和自监督方法在医学图像分类任务上进行了全面实验对比。③相比已有零散研究，提供了统一的评估框架和公平的比较基准。④实验揭示了不同方法在不同医学数据集上的性能差异，为实际应用提供了选择指导。
- **摘要（英）**: This paper provides a systematic comparison of semi-supervised and self-supervised learning methods for medical image classification. It evaluates multiple approaches under a unified framework, revealing performance variations across datasets. The study offers practical guidance for method selection in medical imaging.
- **核心贡献**: 提供医学图像分类中半监督与自监督方法的系统比较基准。
- **创新点**: 统一评估框架下的多方法对比分析。
- **结果**: 揭示了不同方法在医学数据集上的性能差异，提供选择建议。

### What, When, and Where? Self-Supervised Spatio- Temporal Grounding in Untrimmed Multi-Action Videos from Narrated Instructions.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01743) · 📚 被引 4
- **作者**: Brian Chen, Nina Shvetsova, Andrew Rouditchenko, Daniel Kondermann, Samuel Thomas, Shih-Fu Chang et al.
- **🏷️ 机构**: Columbia University, Goethe University,Frankfurt, MIT CSAIL
- **会议**: CVPR 2024

### Low-Res Leads the Way: Improving Generalization for Super-Resolution by Self-Supervised Learning.
- **链接**: [arXiv:2403.02601](https://arxiv.org/abs/2403.02601) · 📚 被引 26
- **作者**: Haoyu Chen, Wenbo Li, Jinjin Gu, Jingjing Ren, Haoze Sun, Xueyi Zou et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology (Guangzhou), Huawei Noah&#x0027;s Ark Lab, The University of Sydney
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > For image super-resolution (SR), bridging the gap between the performance on synthetic datasets and real-world degradation scenarios remains a challenge. This work introduces a novel "Low-Res Leads the Way" (LWay) training framework, merging Supervised Pre-training with Self-supervised Learning to enhance the adaptability of SR models to real-world images. Our approach utilizes a low-resolution (LR) reconstruction network to extract degradation embeddings from LR images, merging them with super-resolved outputs for LR reconstruction. Leveraging unseen LR images for self-supervised learning guides the model to adapt its modeling space to the target domain, facilitating fine-tuning of SR models without requiring paired high-resolution (HR) images. The integration of Discrete Wavelet Transform (DWT) further refines the focus on high-frequency details. Extensive evaluations show that our method significantly improves the generalization and detail restoration capabilities of SR models on unseen real-world datasets, outperforming existing methods. Our training regime is universally compatible, requiring no network architecture modifications, making it a practical solution for real-world SR applications.

### Self-Supervised Facial Representation Learning with Facial Region Awareness.
- **链接**: [arXiv:2403.02138](https://arxiv.org/abs/2403.02138) · 📚 被引 28
- **作者**: Zheng Gao, Ioannis Patras
- **🏷️ 机构**: Queen Mary University of London,London,El 4NS
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Self-supervised pre-training has been proved to be effective in learning transferable representations that benefit various visual tasks. This paper asks this question: can self-supervised pre-training learn general facial representations for various facial analysis tasks? Recent efforts toward this goal are limited to treating each face image as a whole, i.e., learning consistent facial representations at the image-level, which overlooks the consistency of local facial representations (i.e., facial regions like eyes, nose, etc). In this work, we make a first attempt to propose a novel self-supervised facial representation learning framework to learn consistent global and local facial representations, Facial Region Awareness (FRA). Specifically, we explicitly enforce the consistency of facial regions by matching the local facial representations across views, which are extracted with learned heatmaps highlighting the facial regions. Inspired by the mask prediction in supervised semantic segmentation, we obtain the heatmaps via cosine similarity between the per-pixel projection of feature maps and facial mask embeddings computed from learnable positional embeddings, which leverage the attention mechanism to globally look up the facial image for facial regions. To learn such heatmaps, we formulate the learning of facial mask embeddings as a deep clustering problem by assigning the pixel features from the feature maps to them. The transfer learning results on facial classification and regression tasks show that our FRA outperforms previous pre-trained models and more importantly, using ResNet as the unified backbone for various tasks, our FRA achieves comparable or even better performance compared with SOTA methods in facial analysis tasks.

### CuVLER: Enhanced Unsupervised Object Discoveries through Exhaustive Self-Supervised Transformers.
- **链接**: [arXiv:2403.07700](https://arxiv.org/abs/2403.07700) · 📚 被引 10
- **作者**: Shahaf Arica, Or Rubin, Sapir Gershov, Shlomi Laufer
- **🏷️ 机构**: Technion - Israel Institute of Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this paper, we introduce VoteCut, an innovative method for unsupervised object discovery that leverages feature representations from multiple self-supervised models. VoteCut employs normalized-cut based graph partitioning, clustering and a pixel voting approach. Additionally, We present CuVLER (Cut-Vote-and-LEaRn), a zero-shot model, trained using pseudo-labels, generated by VoteCut, and a novel soft target loss to refine segmentation accuracy. Through rigorous evaluations across multiple datasets and several unsupervised setups, our methods demonstrate significant improvements in comparison to previous state-of-the-art models. Our ablation studies further highlight the contributions of each component, revealing the robustness and efficacy of our approach. Collectively, VoteCut and CuVLER pave the way for future advancements in image segmentation.

### Prompt Augmentation for Self-supervised Text-guided Image Manipulation.
- **链接**: [arXiv:2412.13081](https://arxiv.org/abs/2412.13081) · 📚 被引 4
- **作者**: Rumeysa Bodur, Binod Bhattarai, Tae-Kyun Kim
- **🏷️ 机构**: Imperial College London,UK, University of Aberdeen,UK
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Text-guided image editing finds applications in various creative and practical fields. While recent studies in image generation have advanced the field, they often struggle with the dual challenges of coherent image transformation and context preservation. In response, our work introduces prompt augmentation, a method amplifying a single input prompt into several target prompts, strengthening textual context and enabling localised image editing. Specifically, we use the augmented prompts to delineate the intended manipulation area. We propose a Contrastive Loss tailored to driving effective image editing by displacing edited areas and drawing preserved regions closer. Acknowledging the continuous nature of image manipulations, we further refine our approach by incorporating the similarity concept, creating a Soft Contrastive Loss. The new losses are incorporated to the diffusion model, demonstrating improved or competitive image editing results on public datasets and generated images over state-of-the-art approaches.

### Exploring Efficient Asymmetric Blind-Spots for Self-Supervised Denoising in Real-World Scenarios.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00272) · 📚 被引 16
- **作者**: Shiyan Chen, Jiyuan Zhang, Zhaofei Yu, Tiejun Huang
- **🏷️ 机构**: School of Computer Science, Peking University
- **会议**: CVPR 2024

### ShapeMatcher: Self-Supervised Joint Shape Canonicalization, Segmentation, Retrieval and Deformation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01986) · 📚 被引 10
- **作者**: Yan Di, Chenyangguang Zhang, Chaowei Wang, Ruida Zhang, Guangyao Zhai, Yanyan Li et al.
- **🏷️ 机构**: Technical University of Munich, Tsinghua University, Northwestern Polytechnical University
- **会议**: CVPR 2024

### Learning to Predict Activity Progress by Self-Supervised Video Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01766) · 📚 被引 25
- **作者**: Gerard Donahue, Ehsan Elhamifar
- **🏷️ 机构**: Northeastern University Northeastern University,Boston,MA,USA
- **会议**: CVPR 2024

### Patch2Self2: Self-Supervised Denoising on Coresets via Matrix Sketching.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02610) · 📚 被引 2
- **作者**: Shreyas Fadnavis, Agniva Chowdhury, Joshua Batson, Petros Drineas, Eleftherios Garyfallidis
- **🏷️ 机构**: Johnson and Johnson R&#x0026;D,Cambridge,MA, Oak Ridge National Laboratory,Oak Ridge,TN, Anthropic,San Francisco,CA
- **会议**: CVPR 2024

### SD2Event: Self-Supervised Learning of Dynamic Detectors and Contextual Descriptors for Event Cameras.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00295) · 📚 被引 10
- **作者**: Yuan Gao, Yuqing Zhu, Xinjun Li, Yimin Du, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: CVPR 2024

### An Asymmetric Augmented Self-Supervised Learning Method for Unsupervised Fine-Grained Image Hashing.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01671) · 📚 被引 15
- **作者**: Feiran Hu, Chen-Lin Zhang, Jiangliang Guo, Xiu-Shen Wei, Lin Zhao, Anqi Xu et al.
- **🏷️ 机构**: School of Computer Science and Engineering, Nanjing University of Science and Technology, 4Paradigm Inc., A Innovation Technology Group Co., Ltd
- **会议**: CVPR 2024

### Self-Supervised Representation Learning from Arbitrary Scenarios.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02167) · 📚 被引 5
- **作者**: Zhaowen Li, Yousong Zhu, Zhiyang Chen, Zongxin Gao, Rui Zhao, Chaoyang Zhao et al.
- **🏷️ 机构**: Foundation Model Research Center, Institute of Automation, Chinese Academy of Science1, Independent Researcher, Qing Yuan Research Institute, Shanghai Jiao Tong University
- **会议**: CVPR 2024

### Self-Supervised Debiasing Using Low Rank Regularization.
- **链接**: [arXiv:2210.05248](https://arxiv.org/abs/2210.05248) · 📚 被引 2
- **作者**: Geon Yeong Park, Chanyong Jung, Sangmin Lee, Jong Chul Ye, Sang Wan Lee
- **🏷️ 机构**: Bio and Brain Engineering, Mathematical Sciences
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Spurious correlations can cause strong biases in deep neural networks, impairing generalization ability. While most existing debiasing methods require full supervision on either spurious attributes or target labels, training a debiased model from a limited amount of both annotations is still an open question. To address this issue, we investigate an interesting phenomenon using the spectral analysis of latent representations: spuriously correlated attributes make neural networks inductively biased towards encoding lower effective rank representations. We also show that a rank regularization can amplify this bias in a way that encourages highly correlated features. Leveraging these findings, we propose a self-supervised debiasing framework potentially compatible with unlabeled samples. Specifically, we first pretrain a biased encoder in a self-supervised manner with the rank regularization, serving as a semantic bottleneck to enforce the encoder to learn the spuriously correlated attributes. This biased encoder is then used to discover and upweight bias-conflicting samples in a downstream task, serving as a boosting to effectively debias the main model. Remarkably, the proposed debiasing framework significantly improves the generalization performance of self-supervised learning baselines and, in some cases, even outperforms state-of-the-art supervised debiasing approaches.

### Parameter Efficient Self-Supervised Geospatial Domain Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02630) · 📚 被引 21
- **作者**: Linus Scheibenreif, Michael Mommert, Damian Borth
- **🏷️ 机构**: University of St. Gallen,Switzerland
- **会议**: CVPR 2024

### LAFS: Landmark-Based Facial Self-Supervised Learning for Face Recognition.
- **链接**: [arXiv:2403.08161](https://arxiv.org/abs/2403.08161) · 📚 被引 26
- **作者**: Zhonglin Sun, Chen Feng, Ioannis Patras, Georgios Tzimiropoulos
- **🏷️ 机构**: Queen Mary University of London,London,UK
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this work we focus on learning facial representations that can be adapted to train effective face recognition models, particularly in the absence of labels. Firstly, compared with existing labelled face datasets, a vastly larger magnitude of unlabeled faces exists in the real world. We explore the learning strategy of these unlabeled facial images through self-supervised pretraining to transfer generalized face recognition performance. Moreover, motivated by one recent finding, that is, the face saliency area is critical for face recognition, in contrast to utilizing random cropped blocks of images for constructing augmentations in pretraining, we utilize patches localized by extracted facial landmarks. This enables our method - namely LAndmark-based Facial Self-supervised learning LAFS), to learn key representation that is more critical for face recognition. We also incorporate two landmark-specific augmentations which introduce more diversity of landmark information to further regularize the learning. With learned landmark-based facial representations, we further adapt the representation for face recognition with regularization mitigating variations in landmark positions. Our method achieves significant improvement over the state-of-the-art on multiple face recognition benchmarks, especially on more challenging few-shot scenarios.

### Self-Supervised Dual Contouring.
- **链接**: [arXiv:2405.18131](https://arxiv.org/abs/2405.18131)
- **作者**: Ramana Sundararaman, Roman Klokov, Maks Ovsjanikov
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Learning-based isosurface extraction methods have recently emerged as a robust and efficient alternative to axiomatic techniques. However, the vast majority of such approaches rely on supervised training with axiomatically computed ground truths, thus potentially inheriting biases and data artifacts of the corresponding axiomatic methods. Steering away from such dependencies, we propose a self-supervised training scheme for the Neural Dual Contouring meshing framework, resulting in our method: Self-Supervised Dual Contouring (SDC). Instead of optimizing predicted mesh vertices with supervised training, we use two novel self-supervised loss functions that encourage the consistency between distances to the generated mesh up to the first order. Meshes reconstructed by SDC surpass existing data-driven methods in capturing intricate details while being more robust to possible irregularities in the input. Furthermore, we use the same self-supervised training objective linking inferred mesh and input SDF, to regularize the training process of Deep Implicit Networks (DINs). We demonstrate that the resulting DINs produce higher-quality implicit functions, ultimately leading to more accurate and detail-preserving surfaces compared to prior baselines for different input modalities. Finally, we demonstrate that our self-supervised losses improve meshing performance in the single-view reconstruction task by enabling joint training of predicted SDF and resulting output mesh. We open-source our code at https://github.com/Sentient07/SDC

### PanoPose: Self-supervised Relative Pose Estimation for Panoramic Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01891) · 📚 被引 9
- **作者**: Diantao Tu, Hainan Cui, Xianwei Zheng, Shuhan Shen
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Wuhan University,The State Key Lab. LIESMARS
- **会议**: CVPR 2024

### GroupContrast: Semantic-Aware Self-Supervised Representation Learning for 3D Understanding.
- **链接**: [arXiv:2403.09639](https://arxiv.org/abs/2403.09639) · 📚 被引 28
- **作者**: Chengyao Wang, Li Jiang, Xiaoyang Wu, Zhuotao Tian, Bohao Peng, Hengshuang Zhao et al.
- **🏷️ 机构**: CUHK, CUHK(SZ), HKU
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Self-supervised 3D representation learning aims to learn effective representations from large-scale unlabeled point clouds. Most existing approaches adopt point discrimination as the pretext task, which assigns matched points in two distinct views as positive pairs and unmatched points as negative pairs. However, this approach often results in semantically identical points having dissimilar representations, leading to a high number of false negatives and introducing a "semantic conflict" problem. To address this issue, we propose GroupContrast, a novel approach that combines segment grouping and semantic-aware contrastive learning. Segment grouping partitions points into semantically meaningful regions, which enhances semantic coherence and provides semantic guidance for the subsequent contrastive representation learning. Semantic-aware contrastive learning augments the semantic information extracted from segment grouping and helps to alleviate the issue of "semantic conflict". We conducted extensive experiments on multiple 3D scene understanding tasks. The results demonstrate that GroupContrast learns semantically meaningful representations and achieves promising transfer learning performance.

### Neural Modes: Self-supervised Learning of Nonlinear Modal Subspaces.
- **链接**: [arXiv:2404.17620](https://arxiv.org/abs/2404.17620) · 📚 被引 6
- **作者**: Jiahong Wang, Yinwei Du, Stelian Coros, Bernhard Thomaszewski
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We propose a self-supervised approach for learning physics-based subspaces for real-time simulation. Existing learning-based methods construct subspaces by approximating pre-defined simulation data in a purely geometric way. However, this approach tends to produce high-energy configurations, leads to entangled latent space dimensions, and generalizes poorly beyond the training set. To overcome these limitations, we propose a self-supervised approach that directly minimizes the system's mechanical energy during training. We show that our method leads to learned subspaces that reflect physical equilibrium constraints, resolve overfitting issues of previous methods, and offer interpretable latent space parameters.

### CNC-Net: Self-Supervised Learning for CNC Machining Operations.
- **链接**: [arXiv:2312.09925](https://arxiv.org/abs/2312.09925) · 📚 被引 3
- **作者**: Mohsen Yavartanoo, Sangmin Hong, Reyhaneh Neshatavar, Kyoung Mu Lee
- **🏷️ 机构**: Dept. of ECE &#x0026; ASRI, Seoul National University,IPAI,Seoul,Korea
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > CNC manufacturing is a process that employs computer numerical control (CNC) machines to govern the movements of various industrial tools and machinery, encompassing equipment ranging from grinders and lathes to mills and CNC routers. However, the reliance on manual CNC programming has become a bottleneck, and the requirement for expert knowledge can result in significant costs. Therefore, we introduce a pioneering approach named CNC-Net, representing the use of deep neural networks (DNNs) to simulate CNC machines and grasp intricate operations when supplied with raw materials. CNC-Net constitutes a self-supervised framework that exclusively takes an input 3D model and subsequently generates the essential operation parameters required by the CNC machine to construct the object. Our method has the potential to transformative automation in manufacturing by offering a cost-effective alternative to the high costs of manual CNC programming while maintaining exceptional precision in 3D object production. Our experiments underscore the effectiveness of our CNC-Net in constructing the desired 3D objects through the utilization of CNC operations. Notably, it excels in preserving finer local details, exhibiting a marked enhancement in precision compared to the state-of-the-art 3D CAD reconstruction approaches.

### Unmixing Diffusion for Self-Supervised Hyperspectral Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02628) · 📚 被引 34
- **作者**: Haijin Zeng, Jiezhang Cao, Kai Zhang, Yongyong Chen, Hiep Luong, Wilfried Philips
- **🏷️ 机构**: IMEC-UGent, ETH Zurich, Nanjing University
- **会议**: CVPR 2024

### Imagine Before Go: Self-Supervised Generative Map for Object Goal Navigation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01553) · 📚 被引 21
- **作者**: Sixian Zhang, Xinyao Yu, Xinhang Song, Xiaohan Wang, Shuqiang Jiang
- **🏷️ 机构**: Institute of Computing Technology,Key Lab of Intelligent Information Processing Laboratory of the Chinese Academy of Sciences (CAS),Beijing
- **会议**: CVPR 2024

### SD-DiT: Unleashing the Power of Self-Supervised Discrimination in Diffusion Transformer*.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00806) · 📚 被引 18
- **作者**: Rui Zhu, Yingwei Pan, Yehao Li, Ting Yao, Zhenglong Sun, Tao Mei et al.
- **🏷️ 机构**: The Chinese University of HongKong,Shenzhen, HiDream.ai Inc, The Hong Kong Polytechnic University
- **会议**: CVPR 2024

### MaskCLR: Attention-Guided Contrastive Learning for Robust Action Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01767) · 📚 被引 23
- **作者**: Mohamed Abdelfattah, Mariam Hassan, Alexandre Alahi
- **🏷️ 机构**: &#x00C9;cole Poly technique F&#x00E9;d&#x00E9;rale de Lausanne (EPFL)
- **会议**: CVPR 2024

### Relaxed Contrastive Learning for Federated Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01167) · 📚 被引 40
- **作者**: Seonguk Seo, Jinkyu Kim, Geeho Kim, Bohyung Han
- **🏷️ 机构**: Seoul National University,ECE
- **会议**: CVPR 2024

### Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00347) · 📚 被引 31
- **作者**: Woo-Jin Ahn, Geun-Yeong Yang, Hyun Duck Choi, Myo-Taeg Lim
- **🏷️ 机构**: Korea University, Chonnam National University
- **会议**: CVPR 2024

### NoiseCLR: A Contrastive Learning Approach for Unsupervised Discovery of Interpretable Directions in Diffusion Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02285) · 📚 被引 18
- **作者**: Yusuf Dalva, Pinar Yanardag
- **🏷️ 机构**: Virginia Tech
- **会议**: CVPR 2024

### Instance-Aware Contrastive Learning for Occluded Human Mesh Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01004) · 📚 被引 4
- **作者**: Mi-Gyeong Gwon, Gi-Mun Um, Won-Sik Cheong, Wonjun Kim
- **🏷️ 机构**: Konkuk University, Electronics and Telecommunications Research Institute
- **会议**: CVPR 2024

### Contrastive Learning for DeepFake Classification and Localization via Multi-Label Ranking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01669) · 📚 被引 20
- **作者**: Cheng-Yao Hong, Yen-Chi Hsu, Tyng-Luh Liu
- **🏷️ 机构**: Institute of Information Science, Academia Sinica,Taiwan
- **会议**: CVPR 2024

### Universal Novelty Detection Through Adaptive Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02162) · 📚 被引 10
- **作者**: Hossein Mirzaei, Mojtaba Nafez, Mohammad Jafari, Mohammad Bagher Soltani, Mohammad Azizmalayeri, Jafar Habibi et al.
- **🏷️ 机构**: Sharif University of Technology,Iran, Okinawa Institute of Science and Technology,Japan
- **会议**: CVPR 2024

### Enhancing Post-Training Quantization Calibration Through Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01507) · 📚 被引 13
- **作者**: Yuzhang Shang, Gaowen Liu, Ramana Rao Kompella, Yan Yan
- **🏷️ 机构**: Illinois Institute of Technology, Cisco Research
- **会议**: CVPR 2024

### Contextrast: Contextual Contrastive Learning for Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00358) · 📚 被引 41
- **作者**: Changki Sung, Wanhee Kim, Jungho An, Wooju Lee, Hyungtae Lim, Hyun Myung
- **🏷️ 机构**: School of Electrical Engineering, KI-Robotics, Korea Advanced Institute of Science and Technology,Republic of Korea, Department of Automotive Engineering Kookmin University,Republic of Korea
- **会议**: CVPR 2024

### VoCo: A Simple-Yet-Effective Volume Contrastive Learning Framework for 3D Medical Image Analysis.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02158) · 📚 被引 83
- **作者**: Linshan Wu, Jiaxin Zhuang, Hao Chen
- **🏷️ 机构**: Hong Kong University of Science and Technology
- **会议**: CVPR 2024

### Data Poisoning Based Backdoor Attacks to Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02299) · 📚 被引 18
- **作者**: Jinghuai Zhang, Hongbin Liu, Jinyuan Jia, Neil Zhenqiang Gong
- **🏷️ 机构**: University of California,Los Angeles, Duke University, Penn State
- **会议**: CVPR 2024

### A Unified Framework for Microscopy Defocus Deblur with Multi-Pyramid Transformer and Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01058) · 📚 被引 26
- **作者**: Yuelin Zhang, Pengyu Zheng, Wanquan Yan, Chengyu Fang, Shing Shin Cheng
- **🏷️ 机构**: The Chinese University of Hong Kong,Department of Mechanical and Automation Engineering, Shenzhen International Graduate School, Tsinghua University
- **会议**: CVPR 2024

### Improving Graph Contrastive Learning via Adaptive Positive Sampling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02187) · 📚 被引 9
- **作者**: Jiaming Zhuo, Feiyang Qin, Can Cui, Kun Fu, Bingxin Niu, Mengzhu Wang et al.
- **🏷️ 机构**: School of Artificial Intelligence, Hebei University of Technology,Tianjin,China, School of Computer Science and Engineering, Beihang University,Beijing,China, Institute of Information Engineering Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. → [3d-detection](../3d-detection/Guideline%202024.md)
- VideoGrounding-DINO: Towards Open-Vocabulary Spatio- Temporal Video Grounding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- SCE-MAE: Selective Correspondence Enhancement with Masked Autoencoder for Self-Supervised Landmark Estimation. → [object-detection](../object-detection/Guideline%202024.md)
- PointOBB: Learning Oriented Object Detection via Single Point Supervision. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- DETRs Beat YOLOs on Real-time Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- SelfPose3d: Self-Supervised Multi-Person Multi-View 3d Pose Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Investigating and Mitigating the Side Effects of Noisy Views for Self-Supervised Clustering Algorithms in Practical Multi-View Scenarios. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- From-Ground-To-Objects: Coarse-to-Fine Self-supervised Monocular Depth Estimation of Dynamic Objects with Ground Contact Prior. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Mining Supervision for Dynamic Regions in Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Bootstrapping Autonomous Driving Radars with Self-Supervised Learning. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- UniPAD: A Universal Pre-Training Paradigm for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202024.md)
- SyncMask: Synchronized Attentional Masking for Fashion-centric Vision-Language Pretraining. → [multimodal](../multimodal/Guideline%202024.md)
- Hallucination Augmented Contrastive Learning for Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202024.md)
- BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Polos: Multimodal Metric Learning from Human Feedback for Image Captioning. → [multimodal](../multimodal/Guideline%202024.md)
- Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language. → [multimodal](../multimodal/Guideline%202024.md)
- Self-Supervised Class-Agnostic Motion Prediction with Spatial and Temporal Consistency Regularizations. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Continual Self-Supervised Learning: Towards Universal Multi-Modal Medical Data Representation Learning. → [continual-learning](../continual-learning/Guideline%202024.md)
- ES3: Evolving Self-Supervised Learning of Robust Audio-Visual Speech Representations. → [multimodal](../multimodal/Guideline%202024.md)
- Enhancing Visual Document Understanding with Contrastive Learning in Large Visual-Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MLIP: Enhancing Medical Visual Representation with Divergence Encoder and Knowledge-guided Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- OmniSeg3D: Omniversal 3D Segmentation via Hierarchical Contrastive Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything. → [object-detection](../object-detection/Guideline%202024.md)
- Adaptive VIO: Deep Visual-Inertial Odometry with Online Continual Learning. → [continual-learning](../continual-learning/Guideline%202024.md)
