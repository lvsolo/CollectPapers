# Neural Architecture Search — 2020 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 24 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Hit-Detector: Hierarchical Trinity Architecture Search for Object Detection. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2003.11818](https://arxiv.org/abs/2003.11818) · 📚 被引 81
- **作者**: Jianyuan Guo, Kai Han, Yunhe Wang, Chao Zhang, Zhaohui Yang, Han Wu et al.
- **🏷️ 机构**: Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University; Noah's Ark Lab, Huawei Technologies, Noah's Ark Lab, Huawei Technologies, Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University
- **会议**: CVPR 2020
- **摘要（中）**: ①针对现有NAS方法仅搜索检测器单一组件（如骨干或特征融合层），导致搜索组件与手工设计组件不一致的问题。②提出层次化三体搜索框架，端到端同时搜索检测器的骨干、颈部和头部架构。③发现不同组件偏好不同算子，采用自动筛选子搜索空间的方法，提高搜索效率。④搜索得到的Hit-Detector在COCO minival集上达到41.4% mAP，仅27M参数。
- **摘要（英）**: This paper addresses the inconsistency in NAS methods that search only one component of an object detector, leaving others manually designed. It proposes a hierarchical trinity search framework to jointly discover backbone, neck, and head architectures end-to-end, with automatic sub-search-space screening. The resulting Hit-Detector achieves 41.4% mAP on COCO minival with 27M parameters.
- **核心贡献**: 提出层次化三体搜索框架，端到端搜索检测器所有组件。
- **创新点**: 自动筛选不同组件的子搜索空间，实现高效联合搜索。
- **结果**: 在COCO上达到41.4% mAP，参数仅27M。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) has achieved great success in image classification task. Some recent works have managed to explore the automatic design of efficient backbone or feature fusion layer for object detection. However, these methods focus on searching only one certain component of object detector while leaving others manually designed. We identify the inconsistency between searched component and manually designed ones would withhold the detector of stronger performance. To this end, we propose a hierarchical trinity search framework to simultaneously discover efficient architectures for all components (i.e. backbone, neck, and head) of object detector in an end-to-end manner. In addition, we empirically reveal that different parts of the detector prefer different operators. Motivated by this, we employ a novel scheme to automatically screen different sub search spaces for different components so as to perform the end-to-end search for each component on the corresponding sub search space efficiently. Without bells and whistles, our searched architecture, namely Hit-Detector, achieves 41.4\% mAP on COCO minival set with 27M parameters. Our implementation is available at https://github.com/ggjy/HitDet.pytorch.

</details>

### SP-NAS: Serial-to-Parallel Backbone Search for Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Jiang_SP-NAS_Serial-to-Parallel_Backbone_Search_for_Object_Detection_CVPR_2020_paper.html) · 📚 被引 56
- **作者**: Chenhan Jiang, Hang Xu, Wei Zhang, Xiaodan Liang, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对目标检测中骨干网络设计依赖人工且搜索效率低的问题。②提出SP-NAS，通过串行到并行的搜索策略，自动设计检测专用骨干网络。③相比传统NAS方法，考虑了检测任务的多尺度特征需求，优化了搜索空间和搜索算法。④在COCO数据集上取得了优于手工设计网络的检测精度，同时保持了较高的搜索效率。
- **摘要（英）**: This paper addresses the inefficiency of manual backbone design for object detection by proposing SP-NAS, a serial-to-parallel search strategy that automatically discovers detection-specific backbones. It improves upon prior NAS by incorporating multi-scale feature requirements into the search space and algorithm. The method achieves superior detection accuracy on COCO with efficient search.
- **核心贡献**: 提出面向目标检测的串行到并行骨干网络搜索方法。
- **创新点**: 设计检测感知的搜索空间和串并行搜索策略。
- **结果**: 在COCO上取得优于手工网络的检测精度。

### NAS-FCOS: Fast Neural Architecture Search for Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:1906.04423](https://arxiv.org/abs/1906.04423) · 📚 被引 200
- **作者**: Ning Wang, Yang Gao, Hao Chen, Peng Wang, Zhi Tian, Chunhua Shen et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020
- **摘要（中）**: ①针对目标检测中解码器结构（FPN和预测头）依赖人工设计且NAS搜索成本高的问题。②提出NAS-FCOS，在无锚检测器FCOS上，利用强化学习高效搜索FPN和预测头结构。③通过精心设计搜索空间、搜索算法和评估策略，显著降低搜索成本。④在8块V100 GPU上4天内完成搜索，发现的架构在AP上超越Faster R-CNN、RetinaNet和FCOS 1.5至3.5个点。
- **摘要（英）**: This paper tackles the manual design of decoder structures in object detection by proposing NAS-FCOS, which efficiently searches FPN and prediction head architectures using reinforcement learning on the anchor-free FCOS detector. It reduces search cost through carefully designed search space and evaluation strategies. The discovered architecture surpasses state-of-the-art detectors by 1.5-3.5 AP within 4 GPU-days.
- **核心贡献**: 提出高效搜索检测解码器结构的NAS方法。
- **创新点**: 将NAS应用于无锚检测器的FPN和预测头搜索。
- **结果**: 搜索架构在AP上超越多个SOTA检测器1.5-3.5点。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of deep neural networks relies on significant architecture engineering. Recently neural architecture search (NAS) has emerged as a promise to greatly reduce manual effort in network design by automatically searching for optimal architectures, although typically such algorithms need an excessive amount of computational resources, e.g., a few thousand GPU-days. To date, on challenging vision tasks such as object detection, NAS, especially fast versions of NAS, is less studied. Here we propose to search for the decoder structure of object detectors with search efficiency being taken into consideration. To be more specific, we aim to efficiently search for the feature pyramid network (FPN) as well as the prediction head of a simple anchor-free object detector, namely FCOS, using a tailored reinforcement learning paradigm. With carefully designed search space, search algorithms and strategies for evaluating network quality, we are able to efficiently search a top-performing detection architecture within 4 days using 8 V100 GPUs. The discovered architecture surpasses state-of-the-art object detection models (such as Faster R-CNN, RetinaNet and FCOS) by 1.5 to 3.5 points in AP on the COCO dataset, with comparable computation complexity and memory footprint, demonstrating the efficacy of the proposed NAS for object detection.

</details>

### Densely Connected Search Space for More Flexible Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:1906.09607](https://arxiv.org/abs/1906.09607) · 📚 被引 98
- **作者**: Jiemin Fang, Yuzhu Sun, Qian Zhang, Yuan Li, Wenyu Liu, Xinggang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对NAS中块数量和宽度需手动设置，限制网络尺度搜索的问题。②提出DenseNAS，设计密集连接的搜索空间，通过路由块实现块数和宽度的联合搜索。③引入链式成本估计算法，在搜索中同时优化精度和模型成本。④在ImageNet上，DenseNAS达到75.3% top-1精度，FLOPs仅361MB，延迟17.9ms；更大模型达到76.1%精度。
- **摘要（英）**: This paper addresses the manual setting of block counts and widths in NAS by proposing DenseNAS, a densely connected search space with routing blocks for joint search. It introduces a chained cost estimation algorithm to optimize both accuracy and model cost. DenseNAS achieves 75.3% top-1 accuracy on ImageNet with 361MB FLOPs and 17.9ms latency.
- **核心贡献**: 提出密集连接搜索空间实现块数和宽度联合搜索。
- **创新点**: 设计路由块和链式成本估计优化搜索。
- **结果**: 在ImageNet上以低FLOPs取得高精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has dramatically advanced the development of neural network design. We revisit the search space design in most previous NAS methods and find the number and widths of blocks are set manually. However, block counts and block widths determine the network scale (depth and width) and make a great influence on both the accuracy and the model cost (FLOPs/latency). In this paper, we propose to search block counts and block widths by designing a densely connected search space, i.e., DenseNAS. The new search space is represented as a dense super network, which is built upon our designed routing blocks. In the super network, routing blocks are densely connected and we search for the best path between them to derive the final architecture. We further propose a chained cost estimation algorithm to approximate the model cost during the search. Both the accuracy and model cost are optimized in DenseNAS. For experiments on the MobileNetV2-based search space, DenseNAS achieves 75.3% top-1 accuracy on ImageNet with only 361MB FLOPs and 17.9ms latency on a single TITAN-XP. The larger model searched by DenseNAS achieves 76.1% accuracy with only 479M FLOPs. DenseNAS further promotes the ImageNet classification accuracies of ResNet-18, -34 and -50-B by 1.5%, 0.5% and 0.3% with 200M, 600M and 680M FLOPs reduction respectively. The related code is available at https://github.com/JaminFong/DenseNAS.

</details>

### Can Weight Sharing Outperform Random Architecture Search? An Investigation With TuNAS. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2008.06120](https://arxiv.org/abs/2008.06120) · 📚 被引 72
- **作者**: Gabriel Bender, Hanxiao Liu, Bo Chen, Grace Chu, Shuyang Cheng, Pieter-Jan Kindermans et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对权重共享NAS是否优于随机搜索的争议问题。②通过TuNAS方法，在多个规模和难度递增的搜索空间上，对图像分类和检测任务进行系统比较。③提出改进技术提升搜索架构质量并减少手动调参。④实验表明，在大型现实任务中，高效搜索方法相比随机搜索有显著优势。
- **摘要（英）**: This paper investigates whether weight-sharing NAS outperforms random search by conducting thorough comparisons on image classification and detection tasks. It proposes techniques to improve searched architecture quality and reduce manual tuning. Results show efficient search provides substantial gains over random search on large realistic tasks.
- **核心贡献**: 系统比较权重共享NAS与随机搜索的性能。
- **创新点**: 提出改进搜索质量和减少调参的技术。
- **结果**: 证明高效搜索在大型任务上优于随机搜索。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient Neural Architecture Search methods based on weight sharing have shown good promise in democratizing Neural Architecture Search for computer vision models. There is, however, an ongoing debate whether these efficient methods are significantly better than random search. Here we perform a thorough comparison between efficient and random search methods on a family of progressively larger and more challenging search spaces for image classification and detection on ImageNet and COCO. While the efficacies of both methods are problem-dependent, our experiments demonstrate that there are large, realistic tasks where efficient search methods can provide substantial gains over random search. In addition, we propose and evaluate techniques which improve the quality of searched architectures and reduce the need for manual hyper-parameter tuning. Source code and experiment data are available at https://github.com/google-research/google-research/tree/master/tunas

</details>

### MTL-NAS: Task-Agnostic Neural Architecture Search Towards General-Purpose Multi-Task Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2003.14058](https://arxiv.org/abs/2003.14058) · 📚 被引 66
- **作者**: Yuan Gao, Haoping Bai, Zequn Jie, Jiayi Ma, Kui Jia, Wei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对通用多任务学习中NAS搜索空间任务特定、无法适应不同任务组合的问题。②提出MTL-NAS，将多任务网络分解为单任务骨干，并设计任务无关的搜索空间，插入跨任务特征融合边。③提出单次梯度搜索算法，通过最小熵正则化使架构权重收敛到近离散值，实现搜索后直接评估。④实验表明，搜索模型无需重新训练即可使用，性能优于现有方法。
- **摘要（英）**: This paper addresses the task-specific search spaces in multi-task NAS by proposing MTL-NAS, which disentangles networks into single-task backbones and designs a task-agnostic search space with cross-task edges. It introduces a single-shot gradient search with minimum entropy regularization for direct evaluation. The searched model achieves superior performance without retraining.
- **核心贡献**: 提出任务无关的NAS方法用于通用多任务学习。
- **创新点**: 设计层次化特征共享搜索空间和单次搜索算法。
- **结果**: 搜索模型可直接评估，性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose to incorporate neural architecture search (NAS) into general-purpose multi-task learning (GP-MTL). Existing NAS methods typically define different search spaces according to different tasks. In order to adapt to different task combinations (i.e., task sets), we disentangle the GP-MTL networks into single-task backbones (optionally encode the task priors), and a hierarchical and layerwise features sharing/fusing scheme across them. This enables us to design a novel and general task-agnostic search space, which inserts cross-task edges (i.e., feature fusion connections) into fixed single-task network backbones. Moreover, we also propose a novel single-shot gradient-based search algorithm that closes the performance gap between the searched architectures and the final evaluation architecture. This is realized with a minimum entropy regularization on the architecture weights during the search phase, which makes the architecture weights converge to near-discrete values and therefore achieves a single model. As a result, our searched model can be directly used for evaluation without (re-)training from scratch. We perform extensive experiments using different single-task backbones on various task sets, demonstrating the promising performance obtained by exploiting the hierarchical and layerwise features, as well as the desirable generalizability to different i) task sets and ii) single-task backbones. The code of our paper is available at https://github.com/bhpfelix/MTLNAS.

</details>

### AdversarialNAS: Adversarial Neural Architecture Search for GANs. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:1912.02037](https://arxiv.org/abs/1912.02037) · 📚 被引 77
- **作者**: Chen Gao, Yunpeng Chen, Si Liu, Zhenxiong Tan, Shuicheng Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对GAN架构设计依赖人工且现有NAS方法无法同时搜索生成器和判别器的问题。②提出AdversarialNAS，首次以可微分方式同时搜索生成器和判别器架构。③设计对抗搜索算法，无需额外评估指标，考虑两个网络的相关性和平衡。④在CIFAR-10上，搜索仅需1 GPU天，FID达到10.87，IS达到8.74，刷新SOTA。
- **摘要（英）**: This paper addresses manual GAN architecture design by proposing AdversarialNAS, the first method to simultaneously search generator and discriminator architectures in a differentiable manner. It uses an adversarial search algorithm without extra metrics, considering network relevance and balance. The method achieves SOTA FID of 10.87 and IS of 8.74 on CIFAR-10 in 1 GPU day.
- **核心贡献**: 提出可微分对抗NAS方法同时搜索GAN生成器和判别器。
- **创新点**: 设计对抗搜索算法，无需额外评估指标。
- **结果**: 在CIFAR-10上刷新FID和IS记录。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) that aims to automate the procedure of architecture design has achieved promising results in many computer vision fields. In this paper, we propose an AdversarialNAS method specially tailored for Generative Adversarial Networks (GANs) to search for a superior generative model on the task of unconditional image generation. The AdversarialNAS is the first method that can search the architectures of generator and discriminator simultaneously in a differentiable manner. During searching, the designed adversarial search algorithm does not need to comput any extra metric to evaluate the performance of the searched architecture, and the search paradigm considers the relevance between the two network architectures and improves their mutual balance. Therefore, AdversarialNAS is very efficient and only takes 1 GPU day to search for a superior generative model in the proposed large search space ($10^{38}$). Experiments demonstrate the effectiveness and superiority of our method. The discovered generative model sets a new state-of-the-art FID score of $10.87$ and highly competitive Inception Score of $8.74$ on CIFAR-10. Its transferability is also proven by setting new state-of-the-art FID score of $26.98$ and Inception score of $9.63$ on STL-10. Code is at: \url{https://github.com/chengaopro/AdversarialNAS}.

</details>

### When NAS Meets Robustness: In Search of Robust Architectures Against Adversarial Attacks. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:1911.10695](https://arxiv.org/abs/1911.10695) · 📚 被引 107
- **作者**: Minghao Guo, Yuzhe Yang, Rui Xu, Ziwei Liu, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对神经网络架构搜索（NAS）中忽视鲁棒性的问题，即搜索到的架构在对抗攻击下性能脆弱。②提出在NAS搜索过程中引入对抗鲁棒性作为优化目标，寻找兼顾精度与鲁棒性的架构。③相比传统NAS仅关注标准精度，该方法将鲁棒性纳入搜索空间和优化策略。④摘要缺失，无法提供具体数据，但主题具有前瞻性。
- **摘要（英）**: This paper addresses the issue of neural architecture search (NAS) neglecting robustness, proposing to incorporate adversarial robustness into the search objective. It aims to find architectures that balance accuracy and robustness, a novel direction compared to standard NAS. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出将对抗鲁棒性纳入NAS搜索目标的新框架。
- **创新点**: 在NAS中联合优化精度与鲁棒性。
- **结果**: 具体效果未在摘要中给出。

### MiLeNAS: Efficient Neural Architecture Search via Mixed-Level Reformulation. **⭐⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2003.12238](https://arxiv.org/abs/2003.12238) · 📚 被引 85
- **作者**: Chaoyang He, Haishan Ye, Li Shen, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对NAS中双层优化近似导致的梯度误差和次优解问题。②提出混合层级重构（Mixed-Level Reformulation）方法，将NAS转化为可高效优化的单层问题，并引入模型大小搜索和早停策略。③相比DARTS等双层优化方法，该方法使用简单一阶优化即可获得更低验证误差。④在卷积搜索空间实验中，搜索过程约5小时完成，架构精度一致优于双层优化方法。
- **摘要（英）**: This paper tackles the suboptimality caused by gradient errors in bilevel optimization for NAS. It proposes a mixed-level reformulation enabling efficient first-order optimization, with model size-based search and early stopping. The method achieves lower validation errors and completes search in ~5 hours, outperforming bilevel approaches.
- **核心贡献**: 提出混合层级重构以解决NAS双层优化的近似误差问题。
- **创新点**: 将NAS转化为混合层级优化，简化训练过程。
- **结果**: 搜索时间约5小时，精度优于双层优化方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many recently proposed methods for Neural Architecture Search (NAS) can be formulated as bilevel optimization. For efficient implementation, its solution requires approximations of second-order methods. In this paper, we demonstrate that gradient errors caused by such approximations lead to suboptimality, in the sense that the optimization procedure fails to converge to a (locally) optimal solution. To remedy this, this paper proposes \mldas, a mixed-level reformulation for NAS that can be optimized efficiently and reliably. It is shown that even when using a simple first-order method on the mixed-level formulation, \mldas\ can achieve a lower validation error for NAS problems. Consequently, architectures obtained by our method achieve consistently higher accuracies than those obtained from bilevel optimization. Moreover, \mldas\ proposes a framework beyond DARTS. It is upgraded via model size-based search and early stopping strategies to complete the search process in around 5 hours. Extensive experiments within the convolutional architecture search space validate the effectiveness of our approach.

</details>

### DSNAS: Direct Neural Architecture Search Without Parameter Retraining. **⭐⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:2002.09128](https://arxiv.org/abs/2002.09128) · 📚 被引 85
- **作者**: Shoukang Hu, Sirui Xie, Hehui Zheng, Chunxiao Liu, Jianping Shi, Xunying Liu et al.
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文指出传统NAS两阶段参数优化导致架构性能相关性差的问题。②提出DSNAS，一种端到端可微NAS框架，通过低偏差蒙特卡洛估计同时优化架构和参数，无需重新训练。③相比两阶段方法，DSNAS直接部署子网络，减少总计算消耗。④在ImageNet上达到74.4%精度，仅需420 GPU小时，总时间减少34%以上。
- **摘要（英）**: This paper addresses the poor correlation between two-stage NAS optimization. It proposes DSNAS, an end-to-end differentiable framework using low-biased Monte Carlo estimation for simultaneous architecture and parameter optimization, enabling direct deployment. DSNAS achieves 74.4% accuracy on ImageNet in 420 GPU hours, reducing total time by over 34%.
- **核心贡献**: 提出任务特定端到端的NAS问题定义和DSNAS框架。
- **创新点**: 无需参数重训练的可微NAS方法。
- **结果**: ImageNet精度74.4%，时间减少34%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> If NAS methods are solutions, what is the problem? Most existing NAS methods require two-stage parameter optimization. However, performance of the same architecture in the two stages correlates poorly. In this work, we propose a new problem definition for NAS, task-specific end-to-end, based on this observation. We argue that given a computer vision task for which a NAS method is expected, this definition can reduce the vaguely-defined NAS evaluation to i) accuracy of this task and ii) the total computation consumed to finally obtain a model with satisfying accuracy. Seeing that most existing methods do not solve this problem directly, we propose DSNAS, an efficient differentiable NAS framework that simultaneously optimizes architecture and parameters with a low-biased Monte Carlo estimate. Child networks derived from DSNAS can be deployed directly without parameter retraining. Comparing with two-stage methods, DSNAS successfully discovers networks with comparable accuracy (74.4%) on ImageNet in 420 GPU hours, reducing the total time by more than 34%. Our implementation is available at https://github.com/SNAS-Series/SNAS-Series.

</details>

### Neural Architecture Search for Lightweight Non-Local Networks. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2004.01961](https://arxiv.org/abs/2004.01961) · 📚 被引 35
- **作者**: Yingwei Li, Xiaojie Jin, Jieru Mei, Xiaochen Lian, Linjie Yang, Cihang Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对非局部（NL）块计算成本高且难以嵌入移动网络的问题。②提出LightNL块，通过压缩变换和紧凑特征，计算成本降低400倍，并设计AutoNL算法端到端搜索最优配置。③相比传统NL块，LightNL在保持性能的同时大幅降低计算量。④在ImageNet上，AutoNL模型在350M FLOPs下达到77.7% top-1精度，搜索仅需32 GPU小时。
- **摘要（英）**: This paper addresses the high computational cost of Non-Local blocks for mobile networks. It proposes LightNL blocks with 400x lower cost and an AutoNL search algorithm for optimal embedding. The searched model achieves 77.7% top-1 accuracy on ImageNet at 350M FLOPs, with search taking only 32 GPU hours.
- **核心贡献**: 提出轻量级非局部块和自动搜索算法AutoNL。
- **创新点**: 将NL块轻量化并集成到NAS中。
- **结果**: ImageNet 77.7%精度，计算成本大幅降低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-Local (NL) blocks have been widely studied in various vision tasks. However, it has been rarely explored to embed the NL blocks in mobile neural networks, mainly due to the following challenges: 1) NL blocks generally have heavy computation cost which makes it difficult to be applied in applications where computational resources are limited, and 2) it is an open problem to discover an optimal configuration to embed NL blocks into mobile neural networks. We propose AutoNL to overcome the above two obstacles. Firstly, we propose a Lightweight Non-Local (LightNL) block by squeezing the transformation operations and incorporating compact features. With the novel design choices, the proposed LightNL block is 400x computationally cheaper} than its conventional counterpart without sacrificing the performance. Secondly, by relaxing the structure of the LightNL block to be differentiable during training, we propose an efficient neural architecture search algorithm to learn an optimal configuration of LightNL blocks in an end-to-end manner. Notably, using only 32 GPU hours, the searched AutoNL model achieves 77.7% top-1 accuracy on ImageNet under a typical mobile setting (350M FLOPs), significantly outperforming previous mobile models including MobileNetV2 (+5.7%), FBNet (+2.8%) and MnasNet (+2.1%). Code and models are available at https://github.com/LiYingwei/AutoNL.

</details>

### Block-Wisely Supervised Neural Architecture Search With Knowledge Distillation. **⭐⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Block-Wisely_Supervised_Neural_Architecture_Search_With_Knowledge_Distillation_CVPR_2020_paper.html) · 📚 被引 119
- **作者**: Changlin Li, Jiefeng Peng, Liuchun Yuan, Guangrun Wang, Xiaodan Liang, Liang Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对NAS中监督信息利用不足的问题。②提出块级监督的NAS方法，结合知识蒸馏提升搜索效率。③相比传统NAS，通过块级监督和蒸馏增强训练信号。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses insufficient supervision in NAS, proposing block-wise supervision with knowledge distillation to enhance search. It aims to improve training signals compared to standard NAS. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出块级监督和知识蒸馏结合的NAS方法。
- **创新点**: 在NAS中引入块级蒸馏监督。
- **结果**: 具体效果未在摘要中给出。

### SGAS: Sequential Greedy Architecture Search. **⭐⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:1912.00195](https://arxiv.org/abs/1912.00195) · 📚 被引 143
- **作者**: Guohao Li, Guocheng Qian, Itzel C. Delgadillo, Matthias Müller, Ali K. Thabet, Bernard Ghanem
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对NAS搜索阶段验证精度与最终评估性能不一致的问题。②提出SGAS，将搜索过程分解为子问题，通过贪心策略选择和剪枝候选操作。③相比传统NAS，SGAS通过顺序贪心搜索提高泛化能力。④在图像分类、点云分类和蛋白质交互图节点分类任务上，SGAS以最小计算成本找到最先进架构。
- **摘要（英）**: This paper addresses the generalization gap in NAS between search and evaluation. It proposes SGAS, a sequential greedy search that divides the procedure into subproblems and prunes operations greedily. SGAS achieves state-of-the-art architectures on image classification, point cloud classification, and node classification with minimal computational cost.
- **核心贡献**: 提出顺序贪心架构搜索方法SGAS。
- **创新点**: 将NAS分解为贪心子问题以提升泛化。
- **结果**: 多任务上达到最先进性能，计算成本低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Architecture design has become a crucial component of successful deep learning. Recent progress in automatic neural architecture search (NAS) shows a lot of promise. However, discovered architectures often fail to generalize in the final evaluation. Architectures with a higher validation accuracy during the search phase may perform worse in the evaluation. Aiming to alleviate this common issue, we introduce sequential greedy architecture search (SGAS), an efficient method for neural architecture search. By dividing the search procedure into sub-problems, SGAS chooses and prunes candidate operations in a greedy fashion. We apply SGAS to search architectures for Convolutional Neural Networks (CNN) and Graph Convolutional Networks (GCN). Extensive experiments show that SGAS is able to find state-of-the-art architectures for tasks such as image classification, point cloud classification and node classification in protein-protein interaction graphs with minimal computational cost. Please visit https://www.deepgcns.org/auto/sgas for more information about SGAS.

</details>

### GP-NAS: Gaussian Process Based Neural Architecture Search. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_GP-NAS_Gaussian_Process_Based_Neural_Architecture_Search_CVPR_2020_paper.html) · 📚 被引 46
- **作者**: Zhihang Li, Teng Xi, Jiankang Deng, Gang Zhang, Shengzhao Wen, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对神经网络架构搜索中高斯过程建模的问题，但摘要缺失，无法获取具体研究内容。②由于摘要为空，无法判断其提出的方法或所做的具体工作。③同样无法评估其相比已有工作的改进点。④由于缺乏摘要信息，无法报告具体效果或数据。
- **摘要（英）**: The paper addresses Gaussian process-based neural architecture search, but the abstract is missing, preventing assessment of its contributions and results.
- **核心贡献**: 无法确定核心贡献。
- **创新点**: 无法确定创新点。
- **结果**: 无法确定取得的效果。

### Graph-Guided Architecture Search for Real-Time Semantic Segmentation. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:1909.06793](https://arxiv.org/abs/1909.06793) · 📚 被引 87
- **作者**: Peiwen Lin, Peng Sun, Guangliang Cheng, Sirui Xie, Xi Li, Jianping Shi
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对实时语义分割网络设计中性能与速度权衡依赖人工经验的问题。②提出了图引导架构搜索（GAS）方法，引入新的搜索空间，通过细胞独立方式消除细胞共享约束，并集成图卷积网络（GCN）作为细胞间通信机制，同时加入延迟导向约束。③相比以往工作，GAS支持细胞级多样性，并通过GCN增强细胞间信息交互，更有效地平衡速度与性能。④在Cityscapes和CamVid数据集上，GAS实现了精度与速度的新最先进权衡。
- **摘要（英）**: This paper addresses the empirical trade-off between performance and speed in designing lightweight semantic segmentation networks. It proposes Graph-guided Architecture Search (GAS) with a novel search space, cell-independent design, and GCN-based communication, achieving state-of-the-art accuracy-speed trade-offs on Cityscapes and CamVid.
- **核心贡献**: 提出GAS方法，通过图引导搜索实现实时语义分割网络的自动设计。
- **创新点**: 引入细胞独立搜索空间和GCN通信机制，增强搜索多样性。
- **结果**: 在Cityscapes和CamVid上取得精度与速度的新最先进权衡。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Designing a lightweight semantic segmentation network often requires researchers to find a trade-off between performance and speed, which is always empirical due to the limited interpretability of neural networks. In order to release researchers from these tedious mechanical trials, we propose a Graph-guided Architecture Search (GAS) pipeline to automatically search real-time semantic segmentation networks. Unlike previous works that use a simplified search space and stack a repeatable cell to form a network, we introduce a novel search mechanism with new search space where a lightweight model can be effectively explored through the cell-level diversity and latencyoriented constraint. Specifically, to produce the cell-level diversity, the cell-sharing constraint is eliminated through the cell-independent manner. Then a graph convolution network (GCN) is seamlessly integrated as a communication mechanism between cells. Finally, a latency-oriented constraint is endowed into the search process to balance the speed and performance. Extensive experiments on Cityscapes and CamVid datasets demonstrate that GAS achieves the new state-of-the-art trade-off between accuracy and speed. In particular, on Cityscapes dataset, GAS achieves the new best performance of 73.5% mIoU with speed of 108.4 FPS on Titan Xp.

</details>

### MemNAS: Memory-Efficient Neural Architecture Search With Grow-Trim Learning. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_MemNAS_Memory-Efficient_Neural_Architecture_Search_With_Grow-Trim_Learning_CVPR_2020_paper.html) · 📚 被引 12
- **作者**: Peiye Liu, Bo Wu, Huadong Ma, Mingoo Seok
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对内存高效的神经网络架构搜索问题，但摘要缺失，无法获取具体研究内容。②由于摘要为空，无法判断其提出的方法或所做的具体工作。③同样无法评估其相比已有工作的改进点。④由于缺乏摘要信息，无法报告具体效果或数据。
- **摘要（英）**: The paper addresses memory-efficient NAS with grow-trim learning, but the abstract is missing, preventing assessment of its contributions and results.
- **核心贡献**: 无法确定核心贡献。
- **创新点**: 无法确定创新点。
- **结果**: 无法确定取得的效果。

### UNAS: Differentiable Architecture Search Meets Reinforcement Learning. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:1912.07651](https://arxiv.org/abs/1912.07651) · 📚 被引 24
- **作者**: Arash Vahdat, Arun Mallya, Ming-Yu Liu, Jan Kautz
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对可微分NAS（DNAS）只能优化可微损失函数且需要准确近似非可微标准的问题。②提出了UNAS统一框架，结合DNAS和强化学习（RL）方法，支持在统一框架中搜索可微和非可微标准，并引入基于泛化差距的新目标函数防止过拟合。③相比已有工作，UNAS兼具DNAS的低搜索成本和RL的灵活性。④在CIFAR-10、CIFAR-100和ImageNet上，UNAS在所有数据集上取得最先进平均精度。
- **摘要（英）**: This paper addresses the limitation of differentiable NAS in handling non-differentiable criteria. It proposes UNAS, a unified framework combining DNAS and RL, with a generalization-gap objective, achieving state-of-the-art average accuracy on CIFAR-10, CIFAR-100, and ImageNet.
- **核心贡献**: 提出UNAS统一框架，整合DNAS和RL，支持混合标准搜索。
- **创新点**: 引入泛化差距目标函数，防止过拟合架构选择。
- **结果**: 在多个数据集上取得最先进平均精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) aims to discover network architectures with desired properties such as high accuracy or low latency. Recently, differentiable NAS (DNAS) has demonstrated promising results while maintaining a search cost orders of magnitude lower than reinforcement learning (RL) based NAS. However, DNAS models can only optimize differentiable loss functions in search, and they require an accurate differentiable approximation of non-differentiable criteria. In this work, we present UNAS, a unified framework for NAS, that encapsulates recent DNAS and RL-based approaches under one framework. Our framework brings the best of both worlds, and it enables us to search for architectures with both differentiable and non-differentiable criteria in one unified framework while maintaining a low search cost. Further, we introduce a new objective function for search based on the generalization gap that prevents the selection of architectures prone to overfitting. We present extensive experiments on the CIFAR-10, CIFAR-100, and ImageNet datasets and we perform search in two fundamentally different search spaces. We show that UNAS obtains the state-of-the-art average accuracy on all three datasets when compared to the architectures searched in the DARTS space. Moreover, we show that UNAS can find an efficient and accurate architecture in the ProxylessNAS search space, that outperforms existing MobileNetV2 based architectures. The source code is available at https://github.com/NVlabs/unas .

</details>

### FBNetV2: Differentiable Neural Architecture Search for Spatial and Channel Dimensions. **⭐⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2004.05565](https://arxiv.org/abs/2004.05565) · 📚 被引 238
- **作者**: Alvin Wan, Xiaoliang Dai, Peizhao Zhang, Zijian He, Yuandong Tian, Saining Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对DNAS搜索空间小、内存和计算开销大的瓶颈。②提出了DMaskingNAS算法，通过掩码机制实现特征图重用，扩展搜索空间至传统DNAS的10^14倍，支持输入分辨率和滤波器数量的搜索，并采用形状传播最大化每FLOP或每参数精度。③相比已有工作，DMaskingNAS在保持内存和计算成本几乎不变的情况下大幅扩展搜索空间。④搜索的FBNetV2模型在精度和效率上超越先前架构，搜索成本降低421倍，精度提高0.9%，FLOPs减少15%（相比MobileNetV3-Small），或精度相似但FLOPs减少20%（相比Efficient-B0）。
- **摘要（英）**: This paper addresses the limited search space and high memory cost of DNAS. It proposes DMaskingNAS with a masking mechanism for feature reuse, expanding the search space by 10^14x, achieving state-of-the-art performance with up to 421x less search cost and improved accuracy-efficiency trade-offs.
- **核心贡献**: 提出DMaskingNAS，通过掩码机制大幅扩展DNAS搜索空间。
- **创新点**: 利用特征图重用掩码，保持计算成本恒定。
- **结果**: FBNetV2在精度和效率上超越先前架构，搜索成本大幅降低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable Neural Architecture Search (DNAS) has demonstrated great success in designing state-of-the-art, efficient neural networks. However, DARTS-based DNAS's search space is small when compared to other search methods', since all candidate network layers must be explicitly instantiated in memory. To address this bottleneck, we propose a memory and computationally efficient DNAS variant: DMaskingNAS. This algorithm expands the search space by up to $10^{14}\times$ over conventional DNAS, supporting searches over spatial and channel dimensions that are otherwise prohibitively expensive: input resolution and number of filters. We propose a masking mechanism for feature map reuse, so that memory and computational costs stay nearly constant as the search space expands. Furthermore, we employ effective shape propagation to maximize per-FLOP or per-parameter accuracy. The searched FBNetV2s yield state-of-the-art performance when compared with all previous architectures. With up to 421$\times$ less search cost, DMaskingNAS finds models with 0.9% higher accuracy, 15% fewer FLOPs than MobileNetV3-Small; and with similar accuracy but 20% fewer FLOPs than Efficient-B0. Furthermore, our FBNetV2 outperforms MobileNetV3 by 2.6% in accuracy, with equivalent model size. FBNetV2 models are open-sourced at https://github.com/facebookresearch/mobile-vision.

</details>

### CARS: Continuous Evolution for Efficient Neural Architecture Search. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:1909.04977](https://arxiv.org/abs/1909.04977) · 📚 被引 215
- **作者**: Zhaohui Yang, Yunhe Wang, Xinghao Chen, Boxin Shi, Chao Xu, Chunjing Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对现有NAS算法主要依赖可微分方法的问题。②提出了CARS，一种高效的连续进化方法，通过共享参数的SuperNet和种群继承加速搜索，并采用非支配排序保留Pareto前沿结果。③相比已有工作，CARS结合进化算法和参数共享，仅需0.4 GPU天即可完成搜索。④在ImageNet上，CARS生成的网络（参数3.7M-5.1M）超越了最先进方法。
- **摘要（英）**: This paper addresses the dominance of differentiable NAS methods. It proposes CARS, a continuous evolutionary approach with SuperNet parameter sharing and Pareto-based sorting, achieving efficient search in 0.4 GPU days and outperforming state-of-the-art on ImageNet.
- **核心贡献**: 提出CARS连续进化搜索方法，结合SuperNet和Pareto优化。
- **创新点**: 通过种群继承和非支配排序加速搜索。
- **结果**: 在ImageNet上以0.4 GPU天搜索出超越最先进方法的网络。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Searching techniques in most of existing neural architecture search (NAS) algorithms are mainly dominated by differentiable methods for the efficiency reason. In contrast, we develop an efficient continuous evolutionary approach for searching neural networks. Architectures in the population that share parameters within one SuperNet in the latest generation will be tuned over the training dataset with a few epochs. The searching in the next evolution generation will directly inherit both the SuperNet and the population, which accelerates the optimal network generation. The non-dominated sorting strategy is further applied to preserve only results on the Pareto front for accurately updating the SuperNet. Several neural networks with different model sizes and performances will be produced after the continuous search with only 0.4 GPU days. As a result, our framework provides a series of networks with the number of parameters ranging from 3.7M to 5.1M under mobile settings. These networks surpass those produced by the state-of-the-art methods on the benchmark ImageNet dataset.

</details>

### Memory-Efficient Hierarchical Neural Architecture Search for Image Denoising. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhang_Memory-Efficient_Hierarchical_Neural_Architecture_Search_for_Image_Denoising_CVPR_2020_paper.html) · 📚 被引 57
- **作者**: Haokui Zhang, Ying Li, Hao Chen, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对图像去噪任务中的神经网络架构搜索（NAS）内存效率低的问题。②提出了一种内存高效的层次化NAS方法，通过层次化搜索策略和内存优化技术来降低搜索过程中的内存消耗。③相比传统NAS方法，该方法在保持去噪性能的同时显著减少了内存占用。④由于摘要不完整，无法提供具体数据，但该方法旨在实现内存高效与性能的平衡。
- **摘要（英）**: This paper addresses the memory inefficiency in neural architecture search (NAS) for image denoising. It proposes a memory-efficient hierarchical NAS method that reduces memory consumption during search while maintaining denoising performance. The approach improves upon traditional NAS by optimizing memory usage, though specific results are unavailable due to incomplete abstract.
- **核心贡献**: 提出内存高效的层次化NAS方法用于图像去噪。
- **创新点**: 层次化搜索与内存优化结合。
- **结果**: 具体效果未在摘要中给出。

### Rethinking Performance Estimation in Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2005.09917](https://arxiv.org/abs/2005.09917) · 📚 被引 24
- **作者**: Xiawu Zheng, Rongrong Ji, Qiang Wang, Qixiang Ye, Zhenguo Li, Yonghong Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对NAS中性能评估（PE）耗时且不可或缺的问题，提出在资源受限条件下的预算化性能评估（BPE）框架。②提出了最小重要性剪枝（MIP）方法，利用随机森林估计超参数重要性并迭代剪枝，以高效探索BPE搜索空间。③相比已有工作，MIP通过剪枝不重要的超参数，将计算资源分配给更重要的超参数，实现了更有效的探索。④结合多种搜索算法（如强化学习、进化算法、随机搜索和可微架构搜索），实现了1000倍的NAS加速，且性能下降可忽略不计。
- **摘要（英）**: This paper addresses the time-consuming performance estimation (PE) in NAS by proposing a budgeted PE (BPE) framework under resource constraints. It introduces Minimum Importance Pruning (MIP) to estimate hyperparameter importance via random forest and prune less important ones iteratively, enabling efficient exploration. Combined with various search algorithms, it achieves 1000x NAS speedup with negligible performance drop compared to SOTA.
- **核心贡献**: 提出预算化性能评估框架和最小重要性剪枝方法，实现高效NAS。
- **创新点**: 将性能评估视为可搜索组件，并用随机森林引导剪枝。
- **结果**: 实现1000倍加速，性能损失可忽略。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) remains a challenging problem, which is attributed to the indispensable and time-consuming component of performance estimation (PE). In this paper, we provide a novel yet systematic rethinking of PE in a resource constrained regime, termed budgeted PE (BPE), which precisely and effectively estimates the performance of an architecture sampled from an architecture space. Since searching an optimal BPE is extremely time-consuming as it requires to train a large number of networks for evaluation, we propose a Minimum Importance Pruning (MIP) approach. Given a dataset and a BPE search space, MIP estimates the importance of hyper-parameters using random forest and subsequently prunes the minimum one from the next iteration. In this way, MIP effectively prunes less important hyper-parameters to allocate more computational resource on more important ones, thus achieving an effective exploration. By combining BPE with various search algorithms including reinforcement learning, evolution algorithm, random search, and differentiable architecture search, we achieve 1, 000x of NAS speed up with a negligible performance drop comparing to the SOTA

</details>

### EcoNAS: Finding Proxies for Economical Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2001.01233](https://arxiv.org/abs/2001.01233) · 📚 被引 93
- **作者**: Dongzhan Zhou, Xinchi Zhou, Wenwei Zhang, Chen Change Loy, Shuai Yi, Xuesen Zhang et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对NAS中训练和评估候选架构耗时的问题，提出使用代理（proxy）来降低计算成本。②系统研究了不同代理在保持候选网络排名一致性方面的行为，并提出了层次化代理策略，对潜在更准确的候选网络分配更多计算，早期用快速代理丢弃无望的候选。③相比已有代理方法，该策略更可靠且经济。④基于此提出了经济型进化NAS（EcoNAS），实现了400倍的加速（具体性能数据未完整给出）。
- **摘要（英）**: This paper addresses the time-consuming training and evaluation in NAS by investigating proxies under reduced settings. It systematically studies proxy behaviors in rank consistency and proposes a hierarchical proxy strategy that allocates more computation to promising candidates and discards unpromising ones early. This leads to EcoNAS, achieving 400x speedup with reliable performance.
- **核心贡献**: 提出层次化代理策略，实现经济型NAS。
- **创新点**: 基于代理可靠性分析，动态分配计算资源。
- **结果**: 实现400倍加速。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) achieves significant progress in many computer vision tasks. While many methods have been proposed to improve the efficiency of NAS, the search progress is still laborious because training and evaluating plausible architectures over large search space is time-consuming. Assessing network candidates under a proxy (i.e., computationally reduced setting) thus becomes inevitable. In this paper, we observe that most existing proxies exhibit different behaviors in maintaining the rank consistency among network candidates. In particular, some proxies can be more reliable -- the rank of candidates does not differ much comparing their reduced setting performance and final performance. In this paper, we systematically investigate some widely adopted reduction factors and report our observations. Inspired by these observations, we present a reliable proxy and further formulate a hierarchical proxy strategy. The strategy spends more computations on candidate networks that are potentially more accurate, while discards unpromising ones in early stage with a fast proxy. This leads to an economical evolutionary-based NAS (EcoNAS), which achieves an impressive 400x search time reduction in comparison to the evolutionary-based state of the art (8 vs. 3150 GPU days). Some new proxies led by our observations can also be applied to accelerate other NAS methods while still able to discover good candidate networks with performance matching those found by previous proxy strategies.

</details>

### MnasFPN: Learning Latency-Aware Pyramid Architecture for Object Detection on Mobile Devices. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:1912.01106](https://arxiv.org/abs/1912.01106) · 📚 被引 40
- **作者**: Bo Chen, Golnaz Ghiasi, Hanxiao Liu, Tsung-Yi Lin, Dmitry Kalenichenko, Hartwig Adam et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对移动设备上目标检测架构设计依赖手工且缺乏延迟感知的问题。②提出了MnasFPN，一个移动友好的检测头搜索空间，结合延迟感知架构搜索。③改进点在于搜索空间设计创新，并考虑设备延迟。④MnasFPN+MobileNetV2在Pixel上比MobileNetV3+SSDLite提升1.8 mAP，且比NAS-FPNLite更准更快。
- **摘要（英）**: This paper proposes MnasFPN, a mobile-friendly search space for detection heads with latency-aware NAS. It outperforms MobileNetV3+SSDLite by 1.8 mAP and is faster than NAS-FPNLite.
- **核心贡献**: 设计了移动友好的检测头搜索空间和延迟感知搜索方法。
- **创新点**: 将延迟纳入搜索目标并创新搜索空间。
- **结果**: 在移动设备上实现精度和速度的显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the blooming success of architecture search for vision tasks in resource-constrained environments, the design of on-device object detection architectures have mostly been manual. The few automated search efforts are either centered around non-mobile-friendly search spaces or not guided by on-device latency. We propose MnasFPN, a mobile-friendly search space for the detection head, and combine it with latency-aware architecture search to produce efficient object detection models. The learned MnasFPN head, when paired with MobileNetV2 body, outperforms MobileNetV3+SSDLite by 1.8 mAP at similar latency on Pixel. It is also both 1.0 mAP more accurate and 10% faster than NAS-FPNLite. Ablation studies show that the majority of the performance gain comes from innovations in the search space. Further explorations reveal an interesting coupling between the search space design and the search algorithm, and that the complexity of MnasFPN search space may be at a local optimum.

</details>

### Stabilizing Differentiable Architecture Search via Perturbation-based Regularization. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/chen20f.html)
- **作者**: Xiangning Chen, Cho-Jui Hsieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①该论文针对可微架构搜索（DARTS）稳定性差的问题。②提出基于扰动的正则化方法来稳定DARTS的搜索过程。③相比已有DARTS变体，该方法通过扰动正则化增强了搜索的鲁棒性。④由于摘要缺失，无法提供具体数据，但该方法旨在提升搜索稳定性。
- **摘要（英）**: This paper addresses the instability in differentiable architecture search (DARTS). It proposes a perturbation-based regularization method to stabilize the search process. Compared to existing DARTS variants, it enhances robustness via perturbation regularization. Specific results are unavailable due to missing abstract details.
- **核心贡献**: 提出了基于扰动的正则化方法，用于稳定DARTS搜索。
- **创新点**: 通过扰动正则化增强搜索鲁棒性。
- **结果**: 旨在提升DARTS的搜索稳定性。

### Neural Architecture Search in A Proxy Validation Loss Landscape. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/li20c.html)
- **作者**: Yanxi Li, Minjing Dong, Yunhe Wang, Chang Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①该论文针对NAS中代理验证损失景观与真实性能不一致的问题。②提出在代理验证损失景观中进行架构搜索的方法，以更准确地评估候选架构。③相比已有代理方法，该方法利用损失景观信息提高搜索的可靠性。④由于摘要缺失，无法提供具体数据，但该方法旨在提升NAS的搜索效率与准确性。
- **摘要（英）**: This paper addresses the inconsistency between proxy validation loss landscapes and true performance in NAS. It proposes searching within a proxy validation loss landscape to better evaluate candidate architectures. Compared to existing proxy methods, it leverages landscape information for improved reliability. Specific results are unavailable due to missing abstract details.
- **核心贡献**: 提出了在代理验证损失景观中进行架构搜索的方法。
- **创新点**: 利用损失景观信息提升NAS搜索的可靠性。
- **结果**: 旨在提升NAS的搜索效率与准确性。

### Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data.
- **链接**: [出版页](http://proceedings.mlr.press/v119/such20a.html)
- **作者**: Felipe Petroski Such, Aditya Rawal, Joel Lehman, Kenneth O. Stanley, Jeffrey Clune
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Does Unsupervised Architecture Representation Learning Help Neural Architecture Search?
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/937936029af671cf479fa893db91cbdd-Abstract.html)
- **作者**: Shen Yan, Yu Zheng, Wei Ao, Xiao Zeng, Mi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Hierarchical Neural Architecture Search for Deep Stereo Matching.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/fc146be0b230d7e0a92e66a6114b840d-Abstract.html)
- **作者**: Xuelian Cheng, Yiran Zhong, Mehrtash Harandi, Yuchao Dai, Xiaojun Chang, Hongdong Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### CLEARER: Multi-Scale Neural Architecture Search for Image Restoration.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/c6e81542b125c36346d9167691b8bd09-Abstract.html)
- **作者**: Yuanbiao Gou, Boyun Li, Zitao Liu, Songfan Yang, Xi Peng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Semi-Supervised Neural Architecture Search.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/77305c2f862ad1d353f55bf38e5a5183-Abstract.html)
- **作者**: Renqian Luo, Xu Tan, Rui Wang, Tao Qin, Enhong Chen, Tie-Yan Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Bridging the Gap between Sample-based and One-shot Neural Architecture Search with BONAS.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/13d4635deccc230c944e4ff6e03404b5-Abstract.html)
- **作者**: Han Shi, Renjie Pi, Hang Xu, Zhenguo Li, James T. Kwok, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### A Study on Encodings for Neural Architecture Search.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/ea4eb49329550caaa1d2044105223721-Abstract.html)
- **作者**: Colin White, Willie Neiswanger, Sam Nolen, Yash Savani
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Auto-Panoptic: Cooperative Multi-Component Architecture Search for Panoptic Segmentation.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/ec1f764517b7ffb52057af6df18142b7-Abstract.html)
- **作者**: Yangxin Wu, Gengwei Zhang, Hang Xu, Xiaodan Liang, Liang Lin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### ISTA-NAS: Efficient and Consistent Neural Architecture Search by Sparse Coding.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/76cf99d3614e23eabab16fb27e944bf9-Abstract.html)
- **作者**: Yibo Yang, Hongyang Li, Shan You, Fei Wang, Chen Qian, Zhouchen Lin
- **🏷️ 机构**: Shanghai AI Lab, Peking University
- **会议**: NeurIPS 2020

### Differentiable Neural Architecture Search in Equivalent Space with Exploration Enhancement.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/9a96a2c73c0d477ff2a6da3bf538f4f4-Abstract.html)
- **作者**: Miao Zhang, Huiqi Li, Shirui Pan, Xiaojun Chang, Zongyuan Ge, Steven W. Su
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Theory-Inspired Path-Regularized Differential Network Architecture Search.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/5e1b18c4c6a6d31695acbae3fd70ecc6-Abstract.html)
- **作者**: Pan Zhou, Caiming Xiong, Richard Socher, Steven Chu-Hong Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<!-- COMPLETE v1 papers=36 -->
