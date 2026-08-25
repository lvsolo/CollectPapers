# Network Pruning — 2024 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 25 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MULTIFLOW: Shifting Towards Task-Agnostic Vision-Language Pruning.
- **链接**: [arXiv:2404.05621](https://arxiv.org/abs/2404.05621) · [代码](https://github.com/FarinaMatteo/multiflow)
- **作者**: Matteo Farina, Massimiliano Mancini, Elia Cunegatti, Gaowen Liu, Giovanni Iacca, Elisa Ricci
- **🏷️ 机构**: University of Trento, Cisco Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > While excellent in transfer learning, Vision-Language models (VLMs) come with high computational costs due to their large number of parameters. To address this issue, removing parameters via model pruning is a viable solution. However, existing techniques for VLMs are task-specific, and thus require pruning the network from scratch for each new task of interest. In this work, we explore a new direction: Task-Agnostic Vision-Language Pruning (TA-VLP). Given a pretrained VLM, the goal is to find a unique pruned counterpart transferable to multiple unknown downstream tasks. In this challenging setting, the transferable representations already encoded in the pretrained model are a key aspect to preserve. Thus, we propose Multimodal Flow Pruning (MULTIFLOW), a first, gradient-free, pruning framework for TA-VLP where: (i) the importance of a parameter is expressed in terms of its magnitude and its information flow, by incorporating the saliency of the neurons it connects; and (ii) pruning is driven by the emergent (multimodal) distribution of the VLM parameters after pretraining. We benchmark eight state-of-the-art pruning algorithms in the context of TA-VLP, experimenting with two VLMs, three vision-language tasks, and three pruning ratios. Our experimental results show that MULTIFLOW outperforms recent sophisticated, combinatorial competitors in the vast majority of the cases, paving the way towards addressing TA-VLP. The code is publicly available at https://github.com/FarinaMatteo/multiflow.

### MoPE-CLIP: Structured Pruning for Efficient Vision-Language Models with Module-Wise Pruning Error Metric.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02584)
- **作者**: Haokun Lin, Haoli Bai, Zhili Liu, Lu Hou, Muyi Sun, Linqi Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Once for Both: Single Stage of Importance and Sparsity Search for Vision Transformer Compression.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00533)
- **作者**: Hancheng Ye, Chong Yu, Peng Ye, Renqiu Xia, Yansong Tang, Jiwen Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Dense Vision Transformer Compression with Few Samples.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01498)
- **作者**: Hanxiao Zhang, Yifan Zhou, Guo-Hua Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Diversity-Aware Channel Pruning for StyleGAN Compression.
- **链接**: [arXiv:2403.13548](https://arxiv.org/abs/2403.13548)
- **作者**: Jiwoo Chung, Sangeek Hyun, Sang-Heon Shim, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > StyleGAN has shown remarkable performance in unconditional image generation. However, its high computational cost poses a significant challenge for practical applications. Although recent efforts have been made to compress StyleGAN while preserving its performance, existing compressed models still lag behind the original model, particularly in terms of sample diversity. To overcome this, we propose a novel channel pruning method that leverages varying sensitivities of channels to latent vectors, which is a key factor in sample diversity. Specifically, by assessing channel importance based on their sensitivities to latent vector perturbations, our method enhances the diversity of samples in the compressed model. Since our method solely focuses on the channel pruning stage, it has complementary benefits with prior training schemes without additional training cost. Extensive experiments demonstrate that our method significantly enhances sample diversity across various datasets. Moreover, in terms of FID scores, our method not only surpasses state-of-the-art by a large margin but also achieves comparable scores with only half training iterations.

### Jointly Training and Pruning CNNs via Learnable Agent Guidance and Alignment.
- **链接**: [arXiv:2403.19490](https://arxiv.org/abs/2403.19490)
- **作者**: Alireza Ganjdanesh, Shangqian Gao, Heng Huang
- **🏷️ 机构**: University of Maryland College Park,Department of Computer Science, University of Pittsburgh,Department of Electrical and Computer Engineering
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Structural model pruning is a prominent approach used for reducing the computational cost of Convolutional Neural Networks (CNNs) before their deployment on resource-constrained devices. Yet, the majority of proposed ideas require a pretrained model before pruning, which is costly to secure. In this paper, we propose a novel structural pruning approach to jointly learn the weights and structurally prune architectures of CNN models. The core element of our method is a Reinforcement Learning (RL) agent whose actions determine the pruning ratios of the CNN model's layers, and the resulting model's accuracy serves as its reward. We conduct the joint training and pruning by iteratively training the model's weights and the agent's policy, and we regularize the model's weights to align with the selected structure by the agent. The evolving model's weights result in a dynamic reward function for the agent, which prevents using prominent episodic RL methods with stationary environment assumption for our purpose. We address this challenge by designing a mechanism to model the complex changing dynamics of the reward function and provide a representation of it to the RL agent. To do so, we take a learnable embedding for each training epoch and employ a recurrent model to calculate a representation of the changing environment. We train the recurrent model and embeddings using a decoder model to reconstruct observed rewards. Such a design empowers our agent to effectively leverage episodic observations along with the environment representations to learn a proper policy to determine performant sub-networks of the CNN model. Our extensive experiments on CIFAR-10 and ImageNet using ResNets and MobileNets demonstrate the effectiveness of our method.

### Device-Wise Federated Network Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01173)
- **作者**: Shangqian Gao, Junyi Li, Zeyu Zhang, Yanfu Zhang, Weidong Cai, Heng Huang
- **🏷️ 机构**: University of Pittsburgh,Electrical and Computer Engineering, University of Maryland College Park,Computer Science, University of Arizona,Information
- **会议**: CVPR 2024

### BilevelPruning: Unified Dynamic and Static Channel Pruning for Convolutional Neural Networks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01523)
- **作者**: Shangqian Gao, Yanfu Zhang, Feihu Huang, Heng Huang
- **🏷️ 机构**: University of Pittsburgh,Electrical and Computer Engineering, College of William and Mary,Computer Science, University of Maryland College Park,Computer Science
- **会议**: CVPR 2024

### OrthCaps: An Orthogonal CapsNet with Sparse Attention Routing and Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00577)
- **作者**: Xinyu Geng, Jiaming Wang, Jiawei Gong, Yuerong Xue, Jun Xu, Fanglin Chen et al.
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, Shanghai Jiao Tong University
- **会议**: CVPR 2024

### FedMef: Towards Memory-Efficient Federated Dynamic Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02601)
- **作者**: Hong Huang, Weiming Zhuang, Chen Chen, Lingjuan Lyu
- **🏷️ 机构**: City University of Hong Kong, Sony AI
- **会议**: CVPR 2024

### Resource- Efficient Transformer Pruning for Finetuning of Large Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01534)
- **作者**: Fatih Ilhan, Gong Su, Selim Furkan Tekin, Tiansheng Huang, Sihao Hu, Ling Liu
- **🏷️ 机构**: Georgia Institute of Technology,Atlanta,GA, IBM Research,Yorktown Heights,NY
- **会议**: CVPR 2024

### Finding Lottery Tickets in Vision Models via Data-Driven Spectral Foresight Pruning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01528)
- **作者**: Leonardo Iurada, Marco Ciccone, Tatiana Tommasi
- **🏷️ 机构**: Politecnico di Torino,Italy
- **会议**: CVPR 2024

### HiPose: Hierarchical Binary Surface Encoding and Correspondence Pruning for RGB-D 6DoF Object Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00967)
- **作者**: Yongliang Lin, Yongzhi Su, Praveen Nathan, Sandeep Inuganti, Yan Di, Martin Sundermeyer et al.
- **🏷️ 机构**: Zhejiang University, German Research Center for Artificial Intelligence (DFKI), Technische Universit&#x00E4;t M&#x00FC;nchen
- **会议**: CVPR 2024

### MAP: MAsk-Pruning for Source-Free Model Intellectual Property Protection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02226)
- **作者**: Boyang Peng, Sanqing Qu, Yong Wu, Tianpei Zou, Lianghua He, Alois Knoll et al.
- **🏷️ 机构**: Tongji University, Technical University of Munich
- **会议**: CVPR 2024

### Zero-TPrune: Zero-Shot Token Pruning Through Leveraging of the Attention Graph in Pre-Trained Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01521)
- **作者**: Hongjie Wang, Bhishma Dedhia, Niraj K. Jha
- **🏷️ 机构**: Princeton University,Princeton,NJ,USA,08540
- **会议**: CVPR 2024

### Auto- Train-Once: Controller Network Guided Automatic Network Pruning from Scratch.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01530)
- **作者**: Xidong Wu, Shangqian Gao, Zeyu Zhang, Zhenzhen Li, Runxue Bao, Yanfu Zhang et al.
- **🏷️ 机构**: University of Pittsburgh, University of Arizona, Bosch Center for AI
- **会议**: CVPR 2024

### Spanning Training Progress: Temporal Dual-Depth Scoring (TDDS) for Enhanced Dataset Pruning.
- **链接**: [arXiv:2311.13613](https://arxiv.org/abs/2311.13613)
- **作者**: Xin Zhang, Jiawei Du, Yunsong Li, Weiying Xie, Joey Tianyi Zhou
- **🏷️ 机构**: XiDian University,Xi&#x0027;an,China, Agency for Science, Technology and Research (A*STAR),Centre for Frontier AI Research (CFAR),Singapore
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Dataset pruning aims to construct a coreset capable of achieving performance comparable to the original, full dataset. Most existing dataset pruning methods rely on snapshot-based criteria to identify representative samples, often resulting in poor generalization across various pruning and cross-architecture scenarios. Recent studies have addressed this issue by expanding the scope of training dynamics considered, including factors such as forgetting event and probability change, typically using an averaging approach. However, these works struggle to integrate a broader range of training dynamics without overlooking well-generalized samples, which may not be sufficiently highlighted in an averaging manner. In this study, we propose a novel dataset pruning method termed as Temporal Dual-Depth Scoring (TDDS), to tackle this problem. TDDS utilizes a dual-depth strategy to achieve a balance between incorporating extensive training dynamics and identifying representative samples for dataset pruning. In the first depth, we estimate the series of each sample's individual contributions spanning the training progress, ensuring comprehensive integration of training dynamics. In the second depth, we focus on the variability of the sample-wise contributions identified in the first depth to highlight well-generalized samples. Extensive experiments conducted on CIFAR and ImageNet datasets verify the superiority of TDDS over previous SOTA methods. Specifically on CIFAR-100, our method achieves 54.51% accuracy with only 10% training data, surpassing random selection by 7.83% and other comparison methods by at least 12.69%.

### Masked Spatial Propagation Network for Sparsity-Adaptive Depth Refinement.
- **链接**: [arXiv:2404.19294](https://arxiv.org/abs/2404.19294)
- **作者**: Jinyoung Jun, Jae-Han Lee, Chang-Su Kim
- **🏷️ 机构**: Korea University, Gauss Labs Inc
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The main function of depth completion is to compensate for an insufficient and unpredictable number of sparse depth measurements of hardware sensors. However, existing research on depth completion assumes that the sparsity -- the number of points or LiDAR lines -- is fixed for training and testing. Hence, the completion performance drops severely when the number of sparse depths changes significantly. To address this issue, we propose the sparsity-adaptive depth refinement (SDR) framework, which refines monocular depth estimates using sparse depth points. For SDR, we propose the masked spatial propagation network (MSPN) to perform SDR with a varying number of sparse depths effectively by gradually propagating sparse depth information throughout the entire depth map. Experimental results demonstrate that MPSN achieves state-of-the-art performance on both SDR and conventional depth completion scenarios.

### Transferable Structural Sparse Adversarial Attack Via Exact Group Sparsity Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02332)
- **作者**: Di Ming, Peng Ren, Yunlong Wang, Xin Feng
- **🏷️ 机构**: School of Computer Science and Engineering, Chongqing University of Technology,Chongqing,China
- **会议**: CVPR 2024

### MaxQ: Multi-Axis Query for N: m Sparsity Network.
- **链接**: [arXiv:2312.07061](https://arxiv.org/abs/2312.07061) · [代码](https://github.com/JingyangXiang/MaxQ)
- **作者**: Jingyang Xiang, Siqi Li, Junhao Chen, Zhuangzhi Chen, Tianxin Huang, Linpeng Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > N:M sparsity has received increasing attention due to its remarkable performance and latency trade-off compared with structured and unstructured sparsity. However, existing N:M sparsity methods do not differentiate the relative importance of weights among blocks and leave important weights underappreciated. Besides, they directly apply N:M sparsity to the whole network, which will cause severe information loss. Thus, they are still sub-optimal. In this paper, we propose an efficient and effective Multi-Axis Query methodology, dubbed as MaxQ, to rectify these problems. During the training, MaxQ employs a dynamic approach to generate soft N:M masks, considering the weight importance across multiple axes. This method enhances the weights with more importance and ensures more effective updates. Meanwhile, a sparsity strategy that gradually increases the percentage of N:M weight blocks is applied, which allows the network to heal from the pruning-induced damage progressively. During the runtime, the N:M soft masks can be precomputed as constants and folded into weights without causing any distortion to the sparse pattern and incurring additional computational overhead. Comprehensive experiments demonstrate that MaxQ achieves consistent improvements across diverse CNN architectures in various computer vision tasks, including image classification, object detection and instance segmentation. For ResNet50 with 1:16 sparse pattern, MaxQ can achieve 74.6\% top-1 accuracy on ImageNet and improve by over 2.8\% over the state-of-the-art. Codes and checkpoints are available at \url{https://github.com/JingyangXiang/MaxQ}.

### UniPTS: A Unified Framework for Proficient Post-Training Sparsity.
- **链接**: [arXiv:2405.18810](https://arxiv.org/abs/2405.18810) · [代码](https://github.com/xjjxmu/UniPTS)
- **作者**: Jingjing Xie, Yuxin Zhang, Mingbao Lin, Zhihang Lin, Liujuan Cao, Rongrong Ji
- **🏷️ 机构**: Efficient Computing, Ministry of Education of China, School of Informatics, Xiamen University,Key Laboratory of Multimedia Trusted Perception, Tencent Youtu Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Post-training Sparsity (PTS) is a recently emerged avenue that chases efficient network sparsity with limited data in need. Existing PTS methods, however, undergo significant performance degradation compared with traditional methods that retrain the sparse networks via the whole dataset, especially at high sparsity ratios. In this paper, we attempt to reconcile this disparity by transposing three cardinal factors that profoundly alter the performance of conventional sparsity into the context of PTS. Our endeavors particularly comprise (1) A base-decayed sparsity objective that promotes efficient knowledge transferring from dense network to the sparse counterpart. (2) A reducing-regrowing search algorithm designed to ascertain the optimal sparsity distribution while circumventing overfitting to the small calibration set in PTS. (3) The employment of dynamic sparse training predicated on the preceding aspects, aimed at comprehensively optimizing the sparsity structure while ensuring training stability. Our proposed framework, termed UniPTS, is validated to be much superior to existing PTS methods across extensive benchmarks. As an illustration, it amplifies the performance of POT, a recently proposed recipe, from 3.9% to 68.6% when pruning ResNet-50 at 90% sparsity ratio on ImageNet. We release the code of our paper at https://github.com/xjjxmu/UniPTS.

## 跨领域论文（完整笔记在其他领域）

- CaKDP: Category-Aware Knowledge Distillation and Pruning Framework for Lightweight 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer. → [multimodal](../multimodal/Guideline%202024.md)
- Sieve: Multimodal Dataset Pruning Using Image Captioning Models. → [multimodal](../multimodal/Guideline%202024.md)
- Towards Backward-Compatible Continual Learning of Image Compression. → [continual-learning](../continual-learning/Guideline%202024.md)
