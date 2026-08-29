# Neural Architecture Search — 2020 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 24 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Hit-Detector: Hierarchical Trinity Architecture Search for Object Detection.
- **链接**: [arXiv:2003.11818](https://arxiv.org/abs/2003.11818) · [代码](https://github.com/ggjy/HitDet.pytorch) · 📚 被引 81
- **作者**: Jianyuan Guo, Kai Han, Yunhe Wang, Chao Zhang, Zhaohui Yang, Han Wu et al.
- **🏷️ 机构**: Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University; Noah's Ark Lab, Huawei Technologies, Noah's Ark Lab, Huawei Technologies, Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) has achieved great success in image classification task. Some recent works have managed to explore the automatic design of efficient backbone or feature fusion layer for object detection. However, these methods focus on searching only one certain component of object detector while leaving others manually designed. We identify the inconsistency between searched component and manually designed ones would withhold the detector of stronger performance. To this end, we propose a hierarchical trinity search framework to simultaneously discover efficient architectures for all components (i.e. backbone, neck, and head) of object detector in an end-to-end manner. In addition, we empirically reveal that different parts of the detector prefer different operators. Motivated by this, we employ a novel scheme to automatically screen different sub search spaces for different components so as to perform the end-to-end search for each component on the corresponding sub search space efficiently. Without bells and whistles, our searched architecture, namely Hit-Detector, achieves 41.4\% mAP on COCO minival set with 27M parameters. Our implementation is available at https://github.com/ggjy/HitDet.pytorch.

</details>

### SP-NAS: Serial-to-Parallel Backbone Search for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Jiang_SP-NAS_Serial-to-Parallel_Backbone_Search_for_Object_Detection_CVPR_2020_paper.html) · 📚 被引 56
- **作者**: Chenhan Jiang, Hang Xu, Wei Zhang, Xiaodan Liang, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### NAS-FCOS: Fast Neural Architecture Search for Object Detection.
- **链接**: [arXiv:1906.04423](https://arxiv.org/abs/1906.04423) · 📚 被引 200
- **作者**: Ning Wang, Yang Gao, Hao Chen, Peng Wang, Zhi Tian, Chunhua Shen et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of deep neural networks relies on significant architecture engineering. Recently neural architecture search (NAS) has emerged as a promise to greatly reduce manual effort in network design by automatically searching for optimal architectures, although typically such algorithms need an excessive amount of computational resources, e.g., a few thousand GPU-days. To date, on challenging vision tasks such as object detection, NAS, especially fast versions of NAS, is less studied. Here we propose to search for the decoder structure of object detectors with search efficiency being taken into consideration. To be more specific, we aim to efficiently search for the feature pyramid network (FPN) as well as the prediction head of a simple anchor-free object detector, namely FCOS, using a tailored reinforcement learning paradigm. With carefully designed search space, search algorithms and strategies for evaluating network quality, we are able to efficiently search a top-performing detection architecture within 4 days using 8 V100 GPUs. The discovered architecture surpasses state-of-the-art object detection models (such as Faster R-CNN, RetinaNet and FCOS) by 1.5 to 3.5 points in AP on the COCO dataset, with comparable computation complexity and memory footprint, demonstrating the efficacy of the proposed NAS for object detection.

</details>

### Densely Connected Search Space for More Flexible Neural Architecture Search.
- **链接**: [arXiv:1906.09607](https://arxiv.org/abs/1906.09607) · [代码](https://github.com/JaminFong/DenseNAS) · 📚 被引 98
- **作者**: Jiemin Fang, Yuzhu Sun, Qian Zhang, Yuan Li, Wenyu Liu, Xinggang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has dramatically advanced the development of neural network design. We revisit the search space design in most previous NAS methods and find the number and widths of blocks are set manually. However, block counts and block widths determine the network scale (depth and width) and make a great influence on both the accuracy and the model cost (FLOPs/latency). In this paper, we propose to search block counts and block widths by designing a densely connected search space, i.e., DenseNAS. The new search space is represented as a dense super network, which is built upon our designed routing blocks. In the super network, routing blocks are densely connected and we search for the best path between them to derive the final architecture. We further propose a chained cost estimation algorithm to approximate the model cost during the search. Both the accuracy and model cost are optimized in DenseNAS. For experiments on the MobileNetV2-based search space, DenseNAS achieves 75.3% top-1 accuracy on ImageNet with only 361MB FLOPs and 17.9ms latency on a single TITAN-XP. The larger model searched by DenseNAS achieves 76.1% accuracy with only 479M FLOPs. DenseNAS further promotes the ImageNet classification accuracies of ResNet-18, -34 and -50-B by 1.5%, 0.5% and 0.3% with 200M, 600M and 680M FLOPs reduction respectively. The related code is available at https://github.com/JaminFong/DenseNAS.

</details>

### Can Weight Sharing Outperform Random Architecture Search? An Investigation With TuNAS.
- **链接**: [arXiv:2008.06120](https://arxiv.org/abs/2008.06120) · [代码](https://github.com/google-research/google-research) · 📚 被引 72
- **作者**: Gabriel Bender, Hanxiao Liu, Bo Chen, Grace Chu, Shuyang Cheng, Pieter-Jan Kindermans et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient Neural Architecture Search methods based on weight sharing have shown good promise in democratizing Neural Architecture Search for computer vision models. There is, however, an ongoing debate whether these efficient methods are significantly better than random search. Here we perform a thorough comparison between efficient and random search methods on a family of progressively larger and more challenging search spaces for image classification and detection on ImageNet and COCO. While the efficacies of both methods are problem-dependent, our experiments demonstrate that there are large, realistic tasks where efficient search methods can provide substantial gains over random search. In addition, we propose and evaluate techniques which improve the quality of searched architectures and reduce the need for manual hyper-parameter tuning. Source code and experiment data are available at https://github.com/google-research/google-research/tree/master/tunas

</details>

### MTL-NAS: Task-Agnostic Neural Architecture Search Towards General-Purpose Multi-Task Learning.
- **链接**: [arXiv:2003.14058](https://arxiv.org/abs/2003.14058) · [代码](https://github.com/bhpfelix/MTLNAS) · 📚 被引 67
- **作者**: Yuan Gao, Haoping Bai, Zequn Jie, Jiayi Ma, Kui Jia, Wei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose to incorporate neural architecture search (NAS) into general-purpose multi-task learning (GP-MTL). Existing NAS methods typically define different search spaces according to different tasks. In order to adapt to different task combinations (i.e., task sets), we disentangle the GP-MTL networks into single-task backbones (optionally encode the task priors), and a hierarchical and layerwise features sharing/fusing scheme across them. This enables us to design a novel and general task-agnostic search space, which inserts cross-task edges (i.e., feature fusion connections) into fixed single-task network backbones. Moreover, we also propose a novel single-shot gradient-based search algorithm that closes the performance gap between the searched architectures and the final evaluation architecture. This is realized with a minimum entropy regularization on the architecture weights during the search phase, which makes the architecture weights converge to near-discrete values and therefore achieves a single model. As a result, our searched model can be directly used for evaluation without (re-)training from scratch. We perform extensive experiments using different single-task backbones on various task sets, demonstrating the promising performance obtained by exploiting the hierarchical and layerwise features, as well as the desirable generalizability to different i) task sets and ii) single-task backbones. The code of our paper is available at https://github.com/bhpfelix/MTLNAS.

</details>

### AdversarialNAS: Adversarial Neural Architecture Search for GANs.
- **链接**: [arXiv:1912.02037](https://arxiv.org/abs/1912.02037) · [代码](https://github.com/chengaopro/AdversarialNAS) · 📚 被引 77
- **作者**: Chen Gao, Yunpeng Chen, Si Liu, Zhenxiong Tan, Shuicheng Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) that aims to automate the procedure of architecture design has achieved promising results in many computer vision fields. In this paper, we propose an AdversarialNAS method specially tailored for Generative Adversarial Networks (GANs) to search for a superior generative model on the task of unconditional image generation. The AdversarialNAS is the first method that can search the architectures of generator and discriminator simultaneously in a differentiable manner. During searching, the designed adversarial search algorithm does not need to comput any extra metric to evaluate the performance of the searched architecture, and the search paradigm considers the relevance between the two network architectures and improves their mutual balance. Therefore, AdversarialNAS is very efficient and only takes 1 GPU day to search for a superior generative model in the proposed large search space ($10^{38}$). Experiments demonstrate the effectiveness and superiority of our method. The discovered generative model sets a new state-of-the-art FID score of $10.87$ and highly competitive Inception Score of $8.74$ on CIFAR-10. Its transferability is also proven by setting new state-of-the-art FID score of $26.98$ and Inception score of $9.63$ on STL-10. Code is at: \url{https://github.com/chengaopro/AdversarialNAS}.

</details>

### Organ at Risk Segmentation for Head and Neck Cancer Using Stratified Learning and Neural Architecture Search.
- **链接**: [arXiv:2004.08426](https://arxiv.org/abs/2004.08426) · 📚 被引 47
- **作者**: Dazhou Guo, Dakai Jin, Zhuotun Zhu, Tsung-Ying Ho, Adam P. Harrison, Chun-Hung Chao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> OAR segmentation is a critical step in radiotherapy of head and neck (H&N) cancer, where inconsistencies across radiation oncologists and prohibitive labor costs motivate automated approaches. However, leading methods using standard fully convolutional network workflows that are challenged when the number of OARs becomes large, e.g. > 40. For such scenarios, insights can be gained from the stratification approaches seen in manual clinical OAR delineation. This is the goal of our work, where we introduce stratified organ at risk segmentation (SOARS), an approach that stratifies OARs into anchor, mid-level, and small & hard (S&H) categories. SOARS stratifies across two dimensions. The first dimension is that distinct processing pipelines are used for each OAR category. In particular, inspired by clinical practices, anchor OARs are used to guide the mid-level and S&H categories. The second dimension is that distinct network architectures are used to manage the significant contrast, size, and anatomy variations between different OARs. We use differentiable neural architecture search (NAS), allowing the network to choose among 2D, 3D or Pseudo-3D convolutions. Extensive 4-fold cross-validation on 142 H&N cancer patients with 42 manually labeled OARs, the most comprehensive OAR dataset to date, demonstrates that both pipeline- and NAS-stratification significantly improves quantitative performance over the state-of-the-art (from 69.52% to 73.68% in absolute Dice scores). Thus, SOARS provides a powerful and principled means to manage the highly complex segmentation space of OARs.

</details>

### When NAS Meets Robustness: In Search of Robust Architectures Against Adversarial Attacks.
- **链接**: [arXiv:1911.10695](https://arxiv.org/abs/1911.10695) · 📚 被引 107
- **作者**: Minghao Guo, Yuzhe Yang, Rui Xu, Ziwei Liu, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2020

### MiLeNAS: Efficient Neural Architecture Search via Mixed-Level Reformulation.
- **链接**: [arXiv:2003.12238](https://arxiv.org/abs/2003.12238) · 📚 被引 85
- **作者**: Chaoyang He, Haishan Ye, Li Shen, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many recently proposed methods for Neural Architecture Search (NAS) can be formulated as bilevel optimization. For efficient implementation, its solution requires approximations of second-order methods. In this paper, we demonstrate that gradient errors caused by such approximations lead to suboptimality, in the sense that the optimization procedure fails to converge to a (locally) optimal solution. To remedy this, this paper proposes \mldas, a mixed-level reformulation for NAS that can be optimized efficiently and reliably. It is shown that even when using a simple first-order method on the mixed-level formulation, \mldas\ can achieve a lower validation error for NAS problems. Consequently, architectures obtained by our method achieve consistently higher accuracies than those obtained from bilevel optimization. Moreover, \mldas\ proposes a framework beyond DARTS. It is upgraded via model size-based search and early stopping strategies to complete the search process in around 5 hours. Extensive experiments within the convolutional architecture search space validate the effectiveness of our approach.

</details>

### DSNAS: Direct Neural Architecture Search Without Parameter Retraining.
- **链接**: [arXiv:2002.09128](https://arxiv.org/abs/2002.09128) · [代码](https://github.com/SNAS-Series/SNAS-Series) · 📚 被引 85
- **作者**: Shoukang Hu, Sirui Xie, Hehui Zheng, Chunxiao Liu, Jianping Shi, Xunying Liu et al.
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> If NAS methods are solutions, what is the problem? Most existing NAS methods require two-stage parameter optimization. However, performance of the same architecture in the two stages correlates poorly. In this work, we propose a new problem definition for NAS, task-specific end-to-end, based on this observation. We argue that given a computer vision task for which a NAS method is expected, this definition can reduce the vaguely-defined NAS evaluation to i) accuracy of this task and ii) the total computation consumed to finally obtain a model with satisfying accuracy. Seeing that most existing methods do not solve this problem directly, we propose DSNAS, an efficient differentiable NAS framework that simultaneously optimizes architecture and parameters with a low-biased Monte Carlo estimate. Child networks derived from DSNAS can be deployed directly without parameter retraining. Comparing with two-stage methods, DSNAS successfully discovers networks with comparable accuracy (74.4%) on ImageNet in 420 GPU hours, reducing the total time by more than 34%. Our implementation is available at https://github.com/SNAS-Series/SNAS-Series.

</details>

### Neural Architecture Search for Lightweight Non-Local Networks.
- **链接**: [arXiv:2004.01961](https://arxiv.org/abs/2004.01961) · [代码](https://github.com/LiYingwei/AutoNL) · 📚 被引 35
- **作者**: Yingwei Li, Xiaojie Jin, Jieru Mei, Xiaochen Lian, Linjie Yang, Cihang Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-Local (NL) blocks have been widely studied in various vision tasks. However, it has been rarely explored to embed the NL blocks in mobile neural networks, mainly due to the following challenges: 1) NL blocks generally have heavy computation cost which makes it difficult to be applied in applications where computational resources are limited, and 2) it is an open problem to discover an optimal configuration to embed NL blocks into mobile neural networks. We propose AutoNL to overcome the above two obstacles. Firstly, we propose a Lightweight Non-Local (LightNL) block by squeezing the transformation operations and incorporating compact features. With the novel design choices, the proposed LightNL block is 400x computationally cheaper} than its conventional counterpart without sacrificing the performance. Secondly, by relaxing the structure of the LightNL block to be differentiable during training, we propose an efficient neural architecture search algorithm to learn an optimal configuration of LightNL blocks in an end-to-end manner. Notably, using only 32 GPU hours, the searched AutoNL model achieves 77.7% top-1 accuracy on ImageNet under a typical mobile setting (350M FLOPs), significantly outperforming previous mobile models including MobileNetV2 (+5.7%), FBNet (+2.8%) and MnasNet (+2.1%). Code and models are available at https://github.com/LiYingwei/AutoNL.

</details>

### Block-Wisely Supervised Neural Architecture Search With Knowledge Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Block-Wisely_Supervised_Neural_Architecture_Search_With_Knowledge_Distillation_CVPR_2020_paper.html) · 📚 被引 119
- **作者**: Changlin Li, Jiefeng Peng, Liuchun Yuan, Guangrun Wang, Xiaodan Liang, Liang Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### SGAS: Sequential Greedy Architecture Search.
- **链接**: [arXiv:1912.00195](https://arxiv.org/abs/1912.00195) · 📚 被引 143
- **作者**: Guohao Li, Guocheng Qian, Itzel C. Delgadillo, Matthias Müller, Ali K. Thabet, Bernard Ghanem
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Architecture design has become a crucial component of successful deep learning. Recent progress in automatic neural architecture search (NAS) shows a lot of promise. However, discovered architectures often fail to generalize in the final evaluation. Architectures with a higher validation accuracy during the search phase may perform worse in the evaluation. Aiming to alleviate this common issue, we introduce sequential greedy architecture search (SGAS), an efficient method for neural architecture search. By dividing the search procedure into sub-problems, SGAS chooses and prunes candidate operations in a greedy fashion. We apply SGAS to search architectures for Convolutional Neural Networks (CNN) and Graph Convolutional Networks (GCN). Extensive experiments show that SGAS is able to find state-of-the-art architectures for tasks such as image classification, point cloud classification and node classification in protein-protein interaction graphs with minimal computational cost. Please visit https://www.deepgcns.org/auto/sgas for more information about SGAS.

</details>

### GP-NAS: Gaussian Process Based Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_GP-NAS_Gaussian_Process_Based_Neural_Architecture_Search_CVPR_2020_paper.html) · 📚 被引 46
- **作者**: Zhihang Li, Teng Xi, Jiankang Deng, Gang Zhang, Shengzhao Wen, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Graph-Guided Architecture Search for Real-Time Semantic Segmentation.
- **链接**: [arXiv:1909.06793](https://arxiv.org/abs/1909.06793) · 📚 被引 87
- **作者**: Peiwen Lin, Peng Sun, Guangliang Cheng, Sirui Xie, Xi Li, Jianping Shi
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Designing a lightweight semantic segmentation network often requires researchers to find a trade-off between performance and speed, which is always empirical due to the limited interpretability of neural networks. In order to release researchers from these tedious mechanical trials, we propose a Graph-guided Architecture Search (GAS) pipeline to automatically search real-time semantic segmentation networks. Unlike previous works that use a simplified search space and stack a repeatable cell to form a network, we introduce a novel search mechanism with new search space where a lightweight model can be effectively explored through the cell-level diversity and latencyoriented constraint. Specifically, to produce the cell-level diversity, the cell-sharing constraint is eliminated through the cell-independent manner. Then a graph convolution network (GCN) is seamlessly integrated as a communication mechanism between cells. Finally, a latency-oriented constraint is endowed into the search process to balance the speed and performance. Extensive experiments on Cityscapes and CamVid datasets demonstrate that GAS achieves the new state-of-the-art trade-off between accuracy and speed. In particular, on Cityscapes dataset, GAS achieves the new best performance of 73.5% mIoU with speed of 108.4 FPS on Titan Xp.

</details>

### MemNAS: Memory-Efficient Neural Architecture Search With Grow-Trim Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_MemNAS_Memory-Efficient_Neural_Architecture_Search_With_Grow-Trim_Learning_CVPR_2020_paper.html) · 📚 被引 12
- **作者**: Peiye Liu, Bo Wu, Huadong Ma, Mingoo Seok
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### UNAS: Differentiable Architecture Search Meets Reinforcement Learning.
- **链接**: [arXiv:1912.07651](https://arxiv.org/abs/1912.07651) · [代码](https://github.com/NVlabs/unas) · 📚 被引 24
- **作者**: Arash Vahdat, Arun Mallya, Ming-Yu Liu, Jan Kautz
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) aims to discover network architectures with desired properties such as high accuracy or low latency. Recently, differentiable NAS (DNAS) has demonstrated promising results while maintaining a search cost orders of magnitude lower than reinforcement learning (RL) based NAS. However, DNAS models can only optimize differentiable loss functions in search, and they require an accurate differentiable approximation of non-differentiable criteria. In this work, we present UNAS, a unified framework for NAS, that encapsulates recent DNAS and RL-based approaches under one framework. Our framework brings the best of both worlds, and it enables us to search for architectures with both differentiable and non-differentiable criteria in one unified framework while maintaining a low search cost. Further, we introduce a new objective function for search based on the generalization gap that prevents the selection of architectures prone to overfitting. We present extensive experiments on the CIFAR-10, CIFAR-100, and ImageNet datasets and we perform search in two fundamentally different search spaces. We show that UNAS obtains the state-of-the-art average accuracy on all three datasets when compared to the architectures searched in the DARTS space. Moreover, we show that UNAS can find an efficient and accurate architecture in the ProxylessNAS search space, that outperforms existing MobileNetV2 based architectures. The source code is available at https://github.com/NVlabs/unas .

</details>

### FBNetV2: Differentiable Neural Architecture Search for Spatial and Channel Dimensions.
- **链接**: [arXiv:2004.05565](https://arxiv.org/abs/2004.05565) · [代码](https://github.com/facebookresearch/mobile-vision) · 📚 被引 238
- **作者**: Alvin Wan, Xiaoliang Dai, Peizhao Zhang, Zijian He, Yuandong Tian, Saining Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable Neural Architecture Search (DNAS) has demonstrated great success in designing state-of-the-art, efficient neural networks. However, DARTS-based DNAS's search space is small when compared to other search methods', since all candidate network layers must be explicitly instantiated in memory. To address this bottleneck, we propose a memory and computationally efficient DNAS variant: DMaskingNAS. This algorithm expands the search space by up to $10^{14}\times$ over conventional DNAS, supporting searches over spatial and channel dimensions that are otherwise prohibitively expensive: input resolution and number of filters. We propose a masking mechanism for feature map reuse, so that memory and computational costs stay nearly constant as the search space expands. Furthermore, we employ effective shape propagation to maximize per-FLOP or per-parameter accuracy. The searched FBNetV2s yield state-of-the-art performance when compared with all previous architectures. With up to 421$\times$ less search cost, DMaskingNAS finds models with 0.9% higher accuracy, 15% fewer FLOPs than MobileNetV3-Small; and with similar accuracy but 20% fewer FLOPs than Efficient-B0. Furthermore, our FBNetV2 outperforms MobileNetV3 by 2.6% in accuracy, with equivalent model size. FBNetV2 models are open-sourced at https://github.com/facebookresearch/mobile-vision.

</details>

### CARS: Continuous Evolution for Efficient Neural Architecture Search.
- **链接**: [arXiv:1909.04977](https://arxiv.org/abs/1909.04977) · 📚 被引 215
- **作者**: Zhaohui Yang, Yunhe Wang, Xinghao Chen, Boxin Shi, Chao Xu, Chunjing Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Searching techniques in most of existing neural architecture search (NAS) algorithms are mainly dominated by differentiable methods for the efficiency reason. In contrast, we develop an efficient continuous evolutionary approach for searching neural networks. Architectures in the population that share parameters within one SuperNet in the latest generation will be tuned over the training dataset with a few epochs. The searching in the next evolution generation will directly inherit both the SuperNet and the population, which accelerates the optimal network generation. The non-dominated sorting strategy is further applied to preserve only results on the Pareto front for accurately updating the SuperNet. Several neural networks with different model sizes and performances will be produced after the continuous search with only 0.4 GPU days. As a result, our framework provides a series of networks with the number of parameters ranging from 3.7M to 5.1M under mobile settings. These networks surpass those produced by the state-of-the-art methods on the benchmark ImageNet dataset.

</details>

### C2FNAS: Coarse-to-Fine Neural Architecture Search for 3D Medical Image Segmentation.
- **链接**: [arXiv:1912.09628](https://arxiv.org/abs/1912.09628) · 📚 被引 121
- **作者**: Qihang Yu, Dong Yang, Holger Roth, Yutong Bai, Yixiao Zhang, Alan L. Yuille et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D convolution neural networks (CNN) have been proved very successful in parsing organs or tumours in 3D medical images, but it remains sophisticated and time-consuming to choose or design proper 3D networks given different task contexts. Recently, Neural Architecture Search (NAS) is proposed to solve this problem by searching for the best network architecture automatically. However, the inconsistency between search stage and deployment stage often exists in NAS algorithms due to memory constraints and large search space, which could become more serious when applying NAS to some memory and time consuming tasks, such as 3D medical image segmentation. In this paper, we propose coarse-to-fine neural architecture search (C2FNAS) to automatically search a 3D segmentation network from scratch without inconsistency on network size or input size. Specifically, we divide the search procedure into two stages: 1) the coarse stage, where we search the macro-level topology of the network, i.e. how each convolution module is connected to other modules; 2) the fine stage, where we search at micro-level for operations in each cell based on previous searched macro-level topology. The coarse-to-fine manner divides the search procedure into two consecutive stages and meanwhile resolves the inconsistency. We evaluate our method on 10 public datasets from Medical Segmentation Decalthon (MSD) challenge, and achieve state-of-the-art performance with the network searched using one dataset, which demonstrates the effectiveness and generalization of our searched models.

</details>

### Memory-Efficient Hierarchical Neural Architecture Search for Image Denoising.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhang_Memory-Efficient_Hierarchical_Neural_Architecture_Search_for_Image_Denoising_CVPR_2020_paper.html) · 📚 被引 57
- **作者**: Haokui Zhang, Ying Li, Hao Chen, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020

### Rethinking Performance Estimation in Neural Architecture Search.
- **链接**: [arXiv:2005.09917](https://arxiv.org/abs/2005.09917) · 📚 被引 24
- **作者**: Xiawu Zheng, Rongrong Ji, Qiang Wang, Qixiang Ye, Zhenguo Li, Yonghong Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) remains a challenging problem, which is attributed to the indispensable and time-consuming component of performance estimation (PE). In this paper, we provide a novel yet systematic rethinking of PE in a resource constrained regime, termed budgeted PE (BPE), which precisely and effectively estimates the performance of an architecture sampled from an architecture space. Since searching an optimal BPE is extremely time-consuming as it requires to train a large number of networks for evaluation, we propose a Minimum Importance Pruning (MIP) approach. Given a dataset and a BPE search space, MIP estimates the importance of hyper-parameters using random forest and subsequently prunes the minimum one from the next iteration. In this way, MIP effectively prunes less important hyper-parameters to allocate more computational resource on more important ones, thus achieving an effective exploration. By combining BPE with various search algorithms including reinforcement learning, evolution algorithm, random search, and differentiable architecture search, we achieve 1, 000x of NAS speed up with a negligible performance drop comparing to the SOTA

</details>

### EcoNAS: Finding Proxies for Economical Neural Architecture Search.
- **链接**: [arXiv:2001.01233](https://arxiv.org/abs/2001.01233) · 📚 被引 93
- **作者**: Dongzhan Zhou, Xinchi Zhou, Wenwei Zhang, Chen Change Loy, Shuai Yi, Xuesen Zhang et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) achieves significant progress in many computer vision tasks. While many methods have been proposed to improve the efficiency of NAS, the search progress is still laborious because training and evaluating plausible architectures over large search space is time-consuming. Assessing network candidates under a proxy (i.e., computationally reduced setting) thus becomes inevitable. In this paper, we observe that most existing proxies exhibit different behaviors in maintaining the rank consistency among network candidates. In particular, some proxies can be more reliable -- the rank of candidates does not differ much comparing their reduced setting performance and final performance. In this paper, we systematically investigate some widely adopted reduction factors and report our observations. Inspired by these observations, we present a reliable proxy and further formulate a hierarchical proxy strategy. The strategy spends more computations on candidate networks that are potentially more accurate, while discards unpromising ones in early stage with a fast proxy. This leads to an economical evolutionary-based NAS (EcoNAS), which achieves an impressive 400x search time reduction in comparison to the evolutionary-based state of the art (8 vs. 3150 GPU days). Some new proxies led by our observations can also be applied to accelerate other NAS methods while still able to discover good candidate networks with performance matching those found by previous proxy strategies.

</details>
