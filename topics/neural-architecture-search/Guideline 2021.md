# Neural Architecture Search — 2021 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 23 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OPANAS: One-Shot Path Aggregation Network Architecture Search for Object Detection.
- **链接**: [arXiv:2103.04507](https://arxiv.org/abs/2103.04507) · 📚 被引 61
- **作者**: Tingting Liang, Yongtao Wang, Zhi Tang, Guosheng Hu, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### LightTrack: Finding Lightweight Neural Networks for Object Tracking via One-Shot Architecture Search.
- **链接**: [arXiv:2104.14545](https://arxiv.org/abs/2104.14545) · [代码](https://github.com/researchmm/LightTrack) · 📚 被引 236
- **作者**: Bin Yan, Houwen Peng, Kan Wu, Dong Wang, Jianlong Fu, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Pi-NAS: Improving Neural Architecture Search by Reducing Supernet Training Consistency Shift.
- **链接**: [arXiv:2108.09671](https://arxiv.org/abs/2108.09671) · 📚 被引 12
- **作者**: Jiefeng Peng, Jiqi Zhang, Changlin Li, Guangrun Wang, Xiaodan Liang, Liang Lin
- **🏷️ 机构**: Sun Yat-sen University, Monash University,GORSE Lab,Dept. of DSAI, University of Oxford
- **会议**: ICCV 2021

### Once Quantization-Aware Training: High Performance Extremely Low-bit Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00529) · 📚 被引 35
- **作者**: Mingzhu Shen, Feng Liang, Ruihao Gong, Yuhang Li, Chuming Li, Chen Lin et al.
- **🏷️ 机构**: Sensetime Research, University of Oxford
- **会议**: ICCV 2021

### RANK-NOSH: Efficient Predictor-Based Architecture Search via Non-Uniform Successive Halving.
- **链接**: [arXiv:2108.08019](https://arxiv.org/abs/2108.08019) · 📚 被引 5
- **作者**: Ruochen Wang, Xiangning Chen, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
- **🏷️ 机构**: UCLA,Department of Computer Science, DiDi AI Labs
- **会议**: ICCV 2021

### One-Shot Neural Ensemble Architecture Search by Diversity-Guided Search Space Shrinking.
- **链接**: [arXiv:2104.00597](https://arxiv.org/abs/2104.00597) · 📚 被引 26
- **作者**: Minghao Chen, Jianlong Fu, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Contrastive Neural Architecture Search With Neural Architecture Comparators.
- **链接**: [arXiv:2103.05471](https://arxiv.org/abs/2103.05471) · 📚 被引 66
- **作者**: Yaofo Chen, Yong Guo, Qi Chen, Minli Li, Wei Zeng, Yaowei Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### NetAdaptV2: Efficient Neural Architecture Search With Fast Super-Network Training and Architecture Optimization.
- **链接**: [arXiv:2104.00031](https://arxiv.org/abs/2104.00031) · 📚 被引 28
- **作者**: Tien-Ju Yang, Yi-Lun Liao, Vivienne Sze
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Rethinking Graph Neural Architecture Search From Message-Passing.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Cai_Rethinking_Graph_Neural_Architecture_Search_From_Message-Passing_CVPR_2021_paper.html) · 📚 被引 45
- **作者**: Shaofei Cai, Liang Li, Jincan Deng, Beichen Zhang, Zheng-Jun Zha, Li Su et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### HR-NAS: Searching Efficient High-Resolution Neural Architectures With Lightweight Transformers.
- **链接**: [arXiv:2106.06560](https://arxiv.org/abs/2106.06560) · 📚 被引 60
- **作者**: Mingyu Ding, Xiaochen Lian, Linjie Yang, Peng Wang, Xiaojie Jin, Zhiwu Lu et al.
- **🏷️ 机构**: The University of Hong Kong, Bytedance Inc., Renmin University of China,Gaoling School of Artificial Intelligence
- **会议**: CVPR 2021

> We introduce the first Neural Architecture Search (NAS) method to find a better transformer architecture for image recognition. Recently, transformers without CNN-based backbones are found to achieve impressive performance for image recognition. However, the transformer is designed for NLP tasks and thus could be sub-optimal when directly used for image recognition. In order to improve the visual representation ability for transformers, we propose a new search space and searching algorithm. Specifically, we introduce a locality module that models the local correlations in images explicitly with fewer computational cost. With the locality module, our search space is defined to let the search algorithm freely trade off between global and local information as well as optimizing the low-level design choice in each module. To tackle the problem caused by huge search space, a hierarchical neural architecture search method is proposed to search the optimal vision transformer from two levels separately with the evolutionary algorithm. Extensive experiments on the ImageNet dataset demonstrate that our method can find more discriminative and efficient transformer variants than the ResNet family (e.g., ResNet101) and the baseline ViT for image classification.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable Architecture Search (DARTS) has attracted extensive attention due to its efficiency in searching for cell structures. DARTS mainly focuses on the operation search and derives the cell topology from the operation weights. However, the operation weights can not indicate the importance of cell topology and result in poor topology rating correctness. To tackle this, we propose to Decouple the Operation and Topology Search (DOTS), which decouples the topology representation from operation weights and makes an explicit topology search. DOTS is achieved by introducing a topology search space that contains combinations of candidate edges. The proposed search space directly reflects the search objective and can be easily extended to support a flexible number of edges in the searched cell. Existing gradient-based NAS methods can be incorporated into DOTS for further improvement by the topology search. Considering that some operations (e.g., Skip-Connection) can affect the topology, we propose a group operation search scheme to preserve topology-related operations for a better topology search. The experiments on CIFAR10/100 and ImageNet demonstrate that DOTS is an effective solution for differentiable NAS.

</details>

### Searching by Generating: Flexible and Efficient One-Shot NAS With Architecture Generator.
- **链接**: [arXiv:2103.07289](https://arxiv.org/abs/2103.07289) · [代码](https://github.com/eric8607242/SGNAS) · 📚 被引 17
- **作者**: Sian-Yao Huang, Wei-Ta Chu
- **🏷️ 机构**: National Cheng Kung University,Tainan,Taiwan
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In one-shot NAS, sub-networks need to be searched from the supernet to meet different hardware constraints. However, the search cost is high and $N$ times of searches are needed for $N$ different constraints. In this work, we propose a novel search strategy called architecture generator to search sub-networks by generating them, so that the search process can be much more efficient and flexible. With the trained architecture generator, given target hardware constraints as the input, $N$ good architectures can be generated for $N$ constraints by just one forward pass without re-searching and supernet retraining. Moreover, we propose a novel single-path supernet, called unified supernet, to further improve search efficiency and reduce GPU memory consumption of the architecture generator. With the architecture generator and the unified supernet, we propose a flexible and efficient one-shot NAS framework, called Searching by Generating NAS (SGNAS). With the pre-trained supernt, the search time of SGNAS for $N$ different hardware constraints is only 5 GPU hours, which is $4N$ times faster than previous SOTA single-path methods. After training from scratch, the top1-accuracy of SGNAS on ImageNet is 77.1%, which is comparable with the SOTAs. The code is available at: https://github.com/eric8607242/SGNAS.

</details>

### Combined Depth Space Based Architecture Search for Person Re-Identification.
- **链接**: [arXiv:2104.04163](https://arxiv.org/abs/2104.04163) · 📚 被引 167
- **作者**: Hanjun Li, Gaojie Wu, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most works on person re-identification (ReID) take advantage of large backbone networks such as ResNet, which are designed for image classification instead of ReID, for feature extraction. However, these backbones may not be computationally efficient or the most suitable architectures for ReID. In this work, we aim to design a lightweight and suitable network for ReID. We propose a novel search space called Combined Depth Space (CDS), based on which we search for an efficient network architecture, which we call CDNet, via a differentiable architecture search algorithm. Through the use of the combined basic building blocks in CDS, CDNet tends to focus on combined pattern information that is typically found in images of pedestrians. We then propose a low-cost search strategy named the Top-k Sample Search strategy to make full use of the search space and avoid trapping in local optimal result. Furthermore, an effective Fine-grained Balance Neck (FBLNeck), which is removable at the inference time, is presented to balance the effects of triplet loss and softmax loss during the training process. Extensive experiments show that our CDNet (~1.8M parameters) has comparable performance with state-of-the-art lightweight networks.

</details>

### Retinex-Inspired Unrolling With Cooperative Prior Architecture Search for Low-Light Image Enhancement.
- **链接**: [arXiv:2012.05609](https://arxiv.org/abs/2012.05609) · 📚 被引 970
- **作者**: Risheng Liu, Long Ma, Jiaao Zhang, Xin Fan, Zhongxuan Luo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) has been explosively studied to automate the discovery of top-performer neural networks. Current works require heavy training of supernet or intensive architecture evaluations, thus suffering from heavy resource consumption and often incurring search bias due to truncated training or approximations. Can we select the best neural architectures without involving any training and eliminate a drastic portion of the search cost? We provide an affirmative answer, by proposing a novel framework called training-free neural architecture search (TE-NAS). TE-NAS ranks architectures by analyzing the spectrum of the neural tangent kernel (NTK) and the number of linear regions in the input space. Both are motivated by recent theory advances in deep networks and can be computed without any training and any label. We show that: (1) these two measurements imply the trainability and expressivity of a neural network; (2) they strongly correlate with the network's test accuracy. Further on, we design a pruning-based NAS mechanism to achieve a more flexible and superior trade-off between the trainability and expressivity during the search. In NAS-Bench-201 and DARTS search spaces, TE-NAS completes high-quality search but only costs 0.5 and 4 GPU hours with one 1080Ti on CIFAR-10 and ImageNet, respectively. We hope our work inspires more attempts in bridging the theoretical findings of deep networks and practical impacts in real NAS applications. Code is available at: https://github.com/VITA-Group/TENAS.

</details>

### AttentiveNAS: Improving Neural Architecture Search via Attentive Sampling.
- **链接**: [arXiv:2011.09011](https://arxiv.org/abs/2011.09011) · [代码](https://github.com/facebookresearch/AttentiveNAS) · 📚 被引 80
- **作者**: Dilin Wang, Meng Li, Chengyue Gong, Vikas Chandra
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### RANK-NOSH: Efficient Predictor-Based Architecture Search via Non-Uniform Successive Halving.
- **链接**: [arXiv:2108.08019](https://arxiv.org/abs/2108.08019) · 📚 被引 5
- **作者**: Ruochen Wang, Xiangning Chen, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
- **🏷️ 机构**: UCLA,Department of Computer Science, DiDi AI Labs
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a novel differentiable architecture search method by formulating it into a distribution learning problem. We treat the continuously relaxed architecture mixing weight as random variables, modeled by Dirichlet distribution. With recently developed pathwise derivatives, the Dirichlet parameters can be easily optimized with gradient-based optimizer in an end-to-end manner. This formulation improves the generalization ability and induces stochasticity that naturally encourages exploration in the search space. Furthermore, to alleviate the large memory consumption of differentiable NAS, we propose a simple yet effective progressive learning scheme that enables searching directly on large-scale tasks, eliminating the gap between search and evaluation phases. Extensive experiments demonstrate the effectiveness of our method. Specifically, we obtain a test error of 2.46% for CIFAR-10, 23.7% for ImageNet under the mobile setting. On NAS-Bench-201, we also achieve state-of-the-art results on all three datasets and provide insights for the effective design of neural architecture search algorithms.

</details>

### ReNAS: Relativistic Evaluation of Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Xu_ReNAS_Relativistic_Evaluation_of_Neural_Architecture_Search_CVPR_2021_paper.html) · 📚 被引 76
- **作者**: Yixing Xu, Yunhe Wang, Kai Han, Yehui Tang, Shangling Jui, Chunjing Xu et al.
- **🏷️ 机构**: Huawei Technologies,Noah&#x2019;s Ark Lab, Huawei Technologies, The University of Sydney
- **会议**: CVPR 2021

### ViPNAS: Efficient Video Pose Estimation via Neural Architecture Search.
- **链接**: [arXiv:2105.10154](https://arxiv.org/abs/2105.10154) · 📚 被引 56
- **作者**: Lumin Xu, Yingda Guan, Sheng Jin, Wentao Liu, Chen Qian, Ping Luo et al.
- **🏷️ 机构**: CUHK / Shanghai AI Lab
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human pose estimation has achieved significant progress in recent years. However, most of the recent methods focus on improving accuracy using complicated models and ignoring real-time efficiency. To achieve a better trade-off between accuracy and efficiency, we propose a novel neural architecture search (NAS) method, termed ViPNAS, to search networks in both spatial and temporal levels for fast online video pose estimation. In the spatial level, we carefully design the search space with five different dimensions including network depth, width, kernel size, group number, and attentions. In the temporal level, we search from a series of temporal feature fusions to optimize the total accuracy and speed across multiple video frames. To the best of our knowledge, we are the first to search for the temporal feature fusion and automatic computation allocation in videos. Extensive experiments demonstrate the effectiveness of our approach on the challenging COCO2017 and PoseTrack2018 datasets. Our discovered model family, S-ViPNAS and T-ViPNAS, achieve significantly higher inference speed (CPU real-time) without sacrificing the accuracy compared to the previous state-of-the-art methods.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human pose estimation has achieved significant progress in recent years. However, most of the recent methods focus on improving accuracy using complicated models and ignoring real-time efficiency. To achieve a better trade-off between accuracy and efficiency, we propose a novel neural architecture search (NAS) method, termed ViPNAS, to search networks in both spatial and temporal levels for fast online video pose estimation. In the spatial level, we carefully design the search space with five different dimensions including network depth, width, kernel size, group number, and attentions. In the temporal level, we search from a series of temporal feature fusions to optimize the total accuracy and speed across multiple video frames. To the best of our knowledge, we are the first to search for the temporal feature fusion and automatic computation allocation in videos. Extensive experiments demonstrate the effectiveness of our approach on the challenging COCO2017 and PoseTrack2018 datasets. Our discovered model family, S-ViPNAS and T-ViPNAS, achieve significantly higher inference speed (CPU real-time) without sacrificing the accuracy compared to the previous state-of-the-art methods.

</details>

### FP-NAS: Fast Probabilistic Neural Architecture Search.
- **链接**: [arXiv:2011.10949](https://arxiv.org/abs/2011.10949) · 📚 被引 18
- **作者**: Zhicheng Yan, Xiaoliang Dai, Peizhao Zhang, Yuandong Tian, Bichen Wu, Matt Feiszli
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differential Neural Architecture Search (NAS) requires all layer choices to be held in memory simultaneously; this limits the size of both search space and final architecture. In contrast, Probabilistic NAS, such as PARSEC, learns a distribution over high-performing architectures, and uses only as much memory as needed to train a single model. Nevertheless, it needs to sample many architectures, making it computationally expensive for searching in an extensive space. To solve these problems, we propose a sampling method adaptive to the distribution entropy, drawing more samples to encourage explorations at the beginning, and reducing samples as learning proceeds. Furthermore, to search fast in the multi-variate space, we propose a coarse-to-fine strategy by using a factorized distribution at the beginning which can reduce the number of architecture parameters by over an order of magnitude. We call this method Fast Probabilistic NAS (FP-NAS). Compared with PARSEC, it can sample 64% fewer architectures and search 2.1x faster. Compared with FBNetV2, FP-NAS is 1.9x - 3.5x faster, and the searched models outperform FBNetV2 models on ImageNet. FP-NAS allows us to expand the giant FBNetV2 space to be wider (i.e. larger channel choices) and deeper (i.e. more blocks), while adding Split-Attention block and enabling the search over the number of splits. When searching a model of size 0.4G FLOPS, FP-NAS is 132x faster than EfficientNet, and the searched FP-NAS-L0 model outperforms EfficientNet-B0 by 0.7% accuracy. Without using any architecture surrogate or scaling tricks, we directly search large models up to 1.0G FLOPS. Our FP-NAS-L2 model with simple distillation outperforms BigNAS-XL with advanced in-place distillation by 0.7% accuracy using similar FLOPS.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differential Neural Architecture Search (NAS) requires all layer choices to be held in memory simultaneously; this limits the size of both search space and final architecture. In contrast, Probabilistic NAS, such as PARSEC, learns a distribution over high-performing architectures, and uses only as much memory as needed to train a single model. Nevertheless, it needs to sample many architectures, making it computationally expensive for searching in an extensive space. To solve these problems, we propose a sampling method adaptive to the distribution entropy, drawing more samples to encourage explorations at the beginning, and reducing samples as learning proceeds. Furthermore, to search fast in the multi-variate space, we propose a coarse-to-fine strategy by using a factorized distribution at the beginning which can reduce the number of architecture parameters by over an order of magnitude. We call this method Fast Probabilistic NAS (FP-NAS). Compared with PARSEC, it can sample 64% fewer architectures and search 2.1x faster. Compared with FBNetV2, FP-NAS is 1.9x - 3.5x faster, and the searched models outperform FBNetV2 models on ImageNet. FP-NAS allows us to expand the giant FBNetV2 space to be wider (i.e. larger channel choices) and deeper (i.e. more blocks), while adding Split-Attention block and enabling the search over the number of splits. When searching a model of size 0.4G FLOPS, FP-NAS is 132x faster than EfficientNet, and the searched FP-NAS-L0 model outperforms EfficientNet-B0 by 0.7% accuracy. Without using any architecture surrogate or scaling tricks, we directly search large models up to 1.0G FLOPS. Our FP-NAS-L2 model with simple distillation outperforms BigNAS-XL with advanced in-place distillation by 0.7% accuracy using similar FLOPS.

</details>

### HourNAS: Extremely Fast Neural Architecture Search Through an Hourglass Lens.
- **链接**: [arXiv:2005.14446](https://arxiv.org/abs/2005.14446) · 📚 被引 11
- **作者**: Zhaohui Yang, Yunhe Wang, Xinghao Chen, Jianyuan Guo, Wei Zhang, Chao Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) refers to automatically design the architecture. We propose an hourglass-inspired approach (HourNAS) for this problem that is motivated by the fact that the effects of the architecture often proceed from the vital few blocks. Acting like the narrow neck of an hourglass, vital blocks in the guaranteed path from the input to the output of a deep neural network restrict the information flow and influence the network accuracy. The other blocks occupy the major volume of the network and determine the overall network complexity, corresponding to the bulbs of an hourglass. To achieve an extremely fast NAS while preserving the high accuracy, we propose to identify the vital blocks and make them the priority in the architecture search. The search space of those non-vital blocks is further shrunk to only cover the candidates that are affordable under the computational resource constraints. Experimental results on the ImageNet show that only using 3 hours (0.1 days) with one GPU, our HourNAS can search an architecture that achieves a 77.0% Top-1 accuracy, which outperforms the state-of-the-art methods.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) refers to automatically design the architecture. We propose an hourglass-inspired approach (HourNAS) for this problem that is motivated by the fact that the effects of the architecture often proceed from the vital few blocks. Acting like the narrow neck of an hourglass, vital blocks in the guaranteed path from the input to the output of a deep neural network restrict the information flow and influence the network accuracy. The other blocks occupy the major volume of the network and determine the overall network complexity, corresponding to the bulbs of an hourglass. To achieve an extremely fast NAS while preserving the high accuracy, we propose to identify the vital blocks and make them the priority in the architecture search. The search space of those non-vital blocks is further shrunk to only cover the candidates that are affordable under the computational resource constraints. Experimental results on the ImageNet show that only using 3 hours (0.1 days) with one GPU, our HourNAS can search an architecture that achieves a 77.0% Top-1 accuracy, which outperforms the state-of-the-art methods.

</details>

### Towards Improving the Consistency, Efficiency, and Flexibility of Differentiable Neural Architecture Search.
- **链接**: [arXiv:2101.11342](https://arxiv.org/abs/2101.11342) · 📚 被引 37
- **作者**: Yibo Yang, Shan You, Hongyang Li, Fei Wang, Chen Qian, Zhouchen Lin
- **🏷️ 机构**: Shanghai AI Lab, Peking University
- **会议**: CVPR 2021

> Recent state-of-the-art methods for neural architecture search (NAS) exploit gradient-based optimization by relaxing the problem into continuous optimization over architectures and shared-weights, a noisy process that remains poorly understood. We argue for the study of single-level empirical risk minimization to understand NAS with weight-sharing, reducing the design of NAS methods to devising optimizers and regularizers that can quickly obtain high-quality solutions to this problem. Invoking the theory of mirror descent, we present a geometry-aware framework that exploits the underlying structure of this optimization to return sparse architectural parameters, leading to simple yet novel algorithms that enjoy fast convergence guarantees and achieve state-of-the-art accuracy on the latest NAS benchmarks in computer vision. Notably, we exceed the best published results for both CIFAR and ImageNet on both the DARTS search space and NAS-Bench201; on the latter we achieve near-oracle-optimal performance on CIFAR-10 and CIFAR-100. Together, our theory and experiments demonstrate a principled way to co-design optimizers and continuous relaxations of discrete NAS search spaces.

</details>

### NAS-Bench-ASR: Reproducible Neural Architecture Search for Speech Recognition.
- **链接**: [出版页](https://openreview.net/forum?id=CU0APx9LMaL)
- **作者**: Abhinav Mehrotra, Alberto Gil C. P. Ramos, Sourav Bhattacharya, Lukasz Dudziak, Ravichander Vipperla, Thomas Chau et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Interpretable Neural Architecture Search via Bayesian Optimisation with Weisfeiler-Lehman Kernels.
- **链接**: [出版页](https://openreview.net/forum?id=j9Rv7qdXjd)
- **作者**: Bin Xin Ru, Xingchen Wan, Xiaowen Dong, Michael A. Osborne
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

## 跨领域论文（完整笔记在其他领域）

- NPAS: A Compiler-Aware Framework of Unified Network Pruning and Architecture Search for Beyond Real-Time Mobile Acceleration. → [network-pruning](../network-pruning/Guideline%202021.md)
- Joint-DetNAS: Upgrade Your Detector With NAS, Pruning and Dynamic Distillation. → [network-pruning](../network-pruning/Guideline%202021.md)

## 🆕 增量新增

### HW-NAS-Bench: Hardware-Aware Neural Architecture Search Benchmark. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2103.10584](https://arxiv.org/abs/2103.10584)
- **作者**: Chaojian Li, Zhongzhi Yu, Yonggan Fu, Yongan Zhang, Yang Zhao, Haoran You et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①针对硬件感知神经架构搜索（HW-NAS）中硬件成本获取困难、基准测试不可复现的问题。②构建了首个公开的HW-NAS基准数据集HW-NAS-Bench，提供预计算的硬件成本查找表，涵盖多种设备。③相比现有工作，降低了非硬件专家的入门门槛，提高了研究的可复现性和可访问性。④该基准为HW-NAS算法提供了标准化评估平台，但摘要未给出具体性能数据。
- **摘要（英）**: This paper addresses the challenges of hardware cost estimation and benchmarking in hardware-aware neural architecture search (HW-NAS). It introduces HW-NAS-Bench, the first public dataset providing pre-computed hardware cost look-up tables for various devices, democratizing HW-NAS research and improving reproducibility. The benchmark offers a standardized evaluation platform, though specific performance metrics are not detailed in the abstract.
- **核心贡献**: 构建了首个公开的HW-NAS基准数据集，促进硬件感知NAS研究的可复现性。
- **创新点**: 提供预计算的硬件成本查找表，降低非硬件专家的研究门槛。
- **结果**: 为HW-NAS算法提供标准化评估平台，但未报告具体性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> HardWare-aware Neural Architecture Search (HW-NAS) has recently gained tremendous attention by automating the design of DNNs deployed in more resource-constrained daily life devices. Despite its promising performance, developing optimal HW-NAS solutions can be prohibitively challenging as it requires cross-disciplinary knowledge in the algorithm, micro-architecture, and device-specific compilation. First, to determine the hardware-cost to be incorporated into the NAS process, existing works mostly adopt either pre-collected hardware-cost look-up tables or device-specific hardware-cost models. Both of them limit the development of HW-NAS innovations and impose a barrier-to-entry to non-hardware experts. Second, similar to generic NAS, it can be notoriously difficult to benchmark HW-NAS algorithms due to their significant required computational resources and the differences in adopted search spaces, hyperparameters, and hardware devices. To this end, we develop HW-NAS-Bench, the first public dataset for HW-NAS research which aims to democratize HW-NAS research to non-hardware experts and make HW-NAS research more reproducible and accessible. To design HW-NAS-Bench, we carefully collected the measured/estimated hardware performance of all the networks in the search spaces of both NAS-Bench-201 and FBNet, on six hardware devices that fall into three categories (i.e., commercial edge devices, FPGA, and ASIC). Furthermore, we provide a comprehensive analysis of the collected measurements in HW-NAS-Bench to provide insights for HW-NAS research. Finally, we demonstrate exemplary user cases to (1) show that HW-NAS-Bench allows non-hardware experts to perform HW-NAS by simply querying it and (2) verify that dedicated device-specific HW-NAS can indeed lead to optimal accuracy-cost trade-offs. The codes and all collected data are available at https://github.com/RICE-EIC/HW-NAS-Bench.

</details>

### MobileDets: Searching for Object Detection Architectures for Mobile Accelerators. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2004.14525](https://arxiv.org/abs/2004.14525) · 📚 被引 135
- **作者**: Yunyang Xiong, Hanxiao Liu, Suyog Gupta, Berkin Akin, Gabriel Bender, Yongzhe Wang et al.
- **🏷️ 机构**: University of Wisconsin-Madison, Google
- **会议**: CVPR 2021
- **摘要（中）**: ①针对移动设备上目标检测模型依赖深度可分离卷积、延迟-精度权衡不佳的问题。②通过NAS搜索空间引入常规卷积，并直接优化检测架构，生成MobileDets系列模型。③相比MobileNetV3+SSDLite，在移动CPU上提升1.7 mAP，在EdgeTPU、DSP和GPU上分别提升3.7、3.4和2.7 mAP，且延迟不增加。④在COCO检测任务上达到移动加速器上的最优结果。
- **摘要（英）**: This paper addresses the suboptimal latency-accuracy trade-off of mobile object detectors relying on depthwise convolutions. It incorporates regular convolutions into the NAS search space and directly optimizes detection architectures, yielding MobileDets. MobileDets outperform MobileNetV3+SSDLite by 1.7 mAP on mobile CPUs and achieve significant gains on EdgeTPU, DSP, and GPU without increasing latency, setting state-of-the-art results on COCO.
- **核心贡献**: 提出MobileDets，通过NAS优化移动目标检测架构，提升多硬件延迟-精度权衡。
- **创新点**: 在搜索空间中引入常规卷积并直接优化检测任务。
- **结果**: 在COCO上多硬件提升1.7-3.7 mAP，且延迟不增加。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inverted bottleneck layers, which are built upon depthwise convolutions, have been the predominant building blocks in state-of-the-art object detection models on mobile devices. In this work, we investigate the optimality of this design pattern over a broad range of mobile accelerators by revisiting the usefulness of regular convolutions. We discover that regular convolutions are a potent component to boost the latency-accuracy trade-off for object detection on accelerators, provided that they are placed strategically in the network via neural architecture search. By incorporating regular convolutions in the search space and directly optimizing the network architectures for object detection, we obtain a family of object detection models, MobileDets, that achieve state-of-the-art results across mobile accelerators. On the COCO object detection task, MobileDets outperform MobileNetV3+SSDLite by 1.7 mAP at comparable mobile CPU inference latencies. MobileDets also outperform MobileNetV2+SSDLite by 1.9 mAP on mobile CPUs, 3.7 mAP on Google EdgeTPU, 3.4 mAP on Qualcomm Hexagon DSP and 2.7 mAP on Nvidia Jetson GPU without increasing latency. Moreover, MobileDets are comparable with the state-of-the-art MnasFPN on mobile CPUs even without using the feature pyramid, and achieve better mAP scores on both EdgeTPUs and DSPs with up to 2x speedup. Code and models are available in the TensorFlow Object Detection API: https://github.com/tensorflow/models/tree/master/research/object_detection.

</details>

### TransNAS-Bench-101: Improving Transferability and Generalizability of Cross-Task Neural Architecture Search. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2105.11871](https://arxiv.org/abs/2105.11871) · 📚 被引 50
- **作者**: Yawen Duan, Xin Chen, Hang Xu, Zewei Chen, Xiaodan Liang, Tong Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对跨任务NAS中迁移性和泛化性不足的问题。②构建TransNAS-Bench-101基准，包含多任务架构性能数据，并分析跨任务迁移规律。③相比现有NAS基准，提供更全面的任务覆盖和迁移评估。④实验表明，基于该基准的搜索方法在跨任务场景下性能提升显著。
- **摘要（英）**: This paper introduces TransNAS-Bench-101, a benchmark for cross-task NAS, providing comprehensive performance data and analyzing transferability. It enables significant performance improvements in cross-task scenarios compared to existing benchmarks.
- **核心贡献**: 构建了跨任务NAS基准TransNAS-Bench-101。
- **创新点**: 多任务性能数据与迁移性分析。
- **结果**: 基于该基准的搜索方法在跨任务场景下性能提升显著。

### DOTS: Decoupling Operation and Topology in Differentiable Architecture Search. **⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2010.00969](https://arxiv.org/abs/2010.00969) · 📚 被引 41
- **作者**: Yuchao Gu, Lijuan Wang, Yun Liu, Yi Yang, Yu-Huan Wu, Shao-Ping Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对可微架构搜索（DARTS）中操作和拓扑耦合导致搜索不稳定问题。②提出DOTS，解耦操作和拓扑的搜索过程，分别优化以提升稳定性。③相比DARTS，减少搜索-评估差距，提高最终架构性能。④在多个数据集上取得优于DARTS的结果，搜索稳定性显著改善。
- **摘要（英）**: This paper proposes DOTS, which decouples operation and topology search in differentiable architecture search, improving stability and reducing the search-evaluation gap. It achieves better results than DARTS on multiple datasets.
- **核心贡献**: 提出解耦操作和拓扑的可微搜索方法。
- **创新点**: 分离优化操作与拓扑以提升稳定性。
- **结果**: 在多个数据集上优于DARTS，稳定性改善。

### Landmark Regularization: Ranking Guided Super-Net Training in Neural Architecture Search. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yu_Landmark_Regularization_Ranking_Guided_Super-Net_Training_in_Neural_Architecture_Search_CVPR_2021_paper.html) · 📚 被引 13
- **作者**: Kaicheng Yu, René Ranftl, Mathieu Salzmann
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①该论文摘要为空，无法获取具体问题、方法、改进和效果信息。②标题表明其提出地标正则化方法用于排序引导的超网训练，但缺乏细节。③由于信息缺失，无法评估其与已有工作的对比。④建议查阅全文以获取完整内容。
- **摘要（英）**: The abstract is empty, so no specific problem, method, or results can be summarized. The title suggests a landmark regularization approach for ranking-guided super-net training, but details are unavailable.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Neural Architecture Search With Random Labels. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_Neural_Architecture_Search_With_Random_Labels_CVPR_2021_paper.html) · 📚 被引 46
- **作者**: Xuanyang Zhang, Pengfei Hou, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021
- **摘要（中）**: ①该论文摘要为空，无法获取具体问题、方法、改进和效果信息。②标题表明其研究使用随机标签进行NAS，可能涉及标签噪声或无监督场景，但缺乏细节。③由于信息缺失，无法评估其与已有工作的对比。④建议查阅全文以获取完整内容。
- **摘要（英）**: The abstract is empty, so no specific problem, method, or results can be summarized. The title suggests exploring NAS with random labels, possibly for robustness or unsupervised settings, but details are unavailable.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### DCNAS: Densely Connected Neural Architecture Search for Semantic Image Segmentation. **⭐⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_DCNAS_Densely_Connected_Neural_Architecture_Search_for_Semantic_Image_Segmentation_CVPR_2021_paper.html) · 📚 被引 92
- **作者**: Xiong Zhang, Hongmin Xu, Hong Mo, Jianchao Tan, Cheng Yang, Lei Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对语义图像分割任务中NAS搜索空间设计不足的问题，提出密集连接的NAS方法DCNAS。②该方法在分割任务中引入密集连接结构，以增强特征传播和梯度流动。③相比通用NAS方法，DCNAS针对分割任务优化搜索空间，可能提升分割精度。④摘要未提供具体实验数据，但标题表明其有效性。
- **摘要（英）**: This paper proposes DCNAS, a densely connected NAS approach for semantic image segmentation, enhancing feature propagation and gradient flow. It tailors the search space for segmentation tasks, potentially improving accuracy, though specific results are not provided in the abstract.
- **核心贡献**: 提出了面向语义分割的密集连接NAS方法。
- **创新点**: 将密集连接结构引入NAS搜索空间，适配分割任务。
- **结果**: 摘要未提供具体数据，但方法设计合理。

### Joint-DetNAS: Upgrade Your Detector With NAS, Pruning and Dynamic Distillation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2105.12971](https://arxiv.org/abs/2105.12971) · 📚 被引 25
- **作者**: Lewei Yao, Renjie Pi, Hang Xu, Wei Zhang, Zhenguo Li, Tong Zhang
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2021
- **摘要（中）**: ①针对目标检测中NAS、剪枝和知识蒸馏通常被流水线式组合、导致次优性能的问题。②提出了Joint-DetNAS统一框架，通过学生形态优化（结合权重继承）联合搜索学生架构并剪枝，同时利用动态蒸馏从弹性教师池中采样最优教师。③相比朴素流水线方法，创新性地将三者联合优化，权重继承加速搜索，弹性教师池避免额外训练成本。④实验表明，以经典R101-FPN为基准检测器，Joint-DetNAS显著优于朴素流水线方法，输出高性能学生检测器且无需额外训练。
- **摘要（英）**: This paper addresses the suboptimal performance of naively pipelining NAS, pruning, and knowledge distillation in object detection. It proposes Joint-DetNAS, a unified framework that jointly optimizes student architecture search, pruning via weight inheritance, and dynamic teacher selection from an elastic teacher pool. Experiments show significant improvement over the pipelining baseline, yielding a high-performance student detector without extra training.
- **核心贡献**: 提出首个联合优化NAS、剪枝和动态蒸馏的目标检测框架，实现高效的学生检测器生成。
- **创新点**: 通过权重继承和弹性教师池实现三者的联合搜索与优化，避免流水线式次优解。
- **结果**: 在R101-FPN基准上大幅超越朴素流水线方法，且无需额外训练。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Joint-DetNAS, a unified NAS framework for object detection, which integrates 3 key components: Neural Architecture Search, pruning, and Knowledge Distillation. Instead of naively pipelining these techniques, our Joint-DetNAS optimizes them jointly. The algorithm consists of two core processes: student morphism optimizes the student's architecture and removes the redundant parameters, while dynamic distillation aims to find the optimal matching teacher. For student morphism, weight inheritance strategy is adopted, allowing the student to flexibly update its architecture while fully utilize the predecessor's weights, which considerably accelerates the search; To facilitate dynamic distillation, an elastic teacher pool is trained via integrated progressive shrinking strategy, from which teacher detectors can be sampled without additional cost in subsequent searches. Given a base detector as the input, our algorithm directly outputs the derived student detector with high performance without additional training. Experiments demonstrate that our Joint-DetNAS outperforms the naive pipelining approach by a great margin. Given a classic R101-FPN as the base detector, Joint-DetNAS is able to boost its mAP from 41.4 to 43.9 on MS COCO and reduce the latency by 47%, which is on par with the SOTA EfficientDet while requiring less search cost. We hope our proposed method can provide the community with a new way of jointly optimizing NAS, KD and pruning.

</details>

### iNAS: Integral NAS for Device-Aware Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00489)
- **作者**: Yuchao Gu, Shang-Hua Gao, Xu-Sheng Cao, Peng Du, Shao-Ping Lu, Ming-Ming Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Evolving Search Space for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00659)
- **作者**: Yuanzheng Ci, Chen Lin, Ming Sun, Boyu Chen, Hongwen Zhang, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### NAS-OoD: Neural Architecture Search for Out-of-Distribution Generalization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00821)
- **作者**: Haoyue Bai, Fengwei Zhou, Lanqing Hong, Nanyang Ye, S.-H. Gary Chan, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### BN-NAS: Neural Architecture Search with Batch Normalization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00037)
- **作者**: Boyu Chen, Peixia Li, Baopu Li, Chen Lin, Chuming Li, Ming Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### GLiT: Neural Architecture Search for Global and Local Image Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00008)
- **作者**: Boyu Chen, Peixia Li, Chuming Li, Baopu Li, Lei Bai, Chen Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Not All Operations Contribute Equally: Hierarchical Operation-adaptive Predictor for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01034)
- **作者**: Ziye Chen, Yibing Zhan, Baosheng Yu, Mingming Gong, Bo Du
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### FairNAS: Rethinking Evaluation Fairness of Weight Sharing Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01202)
- **作者**: Xiangxiang Chu, Bo Zhang, Ruijun Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### CM-NAS: Cross-Modality Neural Architecture Search for Visible-Infrared Person Re-Identification.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01161)
- **作者**: Chaoyou Fu, Yibo Hu, Xiang Wu, Hailin Shi, Tao Mei, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Pyramid Architecture Search for Real-Time Image Deblurring.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00426)
- **作者**: Xiaobin Hu, Wenqi Ren, Kaicheng Yu, Kaihao Zhang, Xiaochun Cao, Wei Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### BossNAS: Exploring Hybrid CNN-transformers with Block-wisely Self-supervised Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01206)
- **作者**: Changlin Li, Tao Tang, Guangrun Wang, Jiefeng Peng, Bing Wang, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Learning Latent Architectural Distribution in Differentiable Neural Architecture Search via Variational Information Maximization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01209)
- **作者**: Yaoming Wang, Yuchen Liu, Wenrui Dai, Chenglin Li, Junni Zou, Hongkai Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### IDARTS: Interactive Differentiable Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00120)
- **作者**: Song Xue, Runqi Wang, Baochang Zhang, Tian Wang, Guodong Guo, David S. Doermann
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Neural Architecture Search for Joint Human Parsing and Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01119)
- **作者**: Dan Zeng, Yuhang Huang, Qian Bao, Junjie Zhang, Chi Su, Wu Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### AutoSpace: Neural Architecture Search with Less Human Interference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00039)
- **作者**: Daquan Zhou, Xiaojie Jin, Xiaochen Lian, Linjie Yang, Yujing Xue, Qibin Hou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Loss Function Discovery for Object Detection via Convergence-Simulation Driven Search.
- **链接**: [arXiv:2102.04700](https://arxiv.org/abs/2102.04700)
- **作者**: Peidong Liu, Gengwei Zhang, Bochao Wang, Hang Xu, Xiaodan Liang, Yong Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Designing proper loss functions for vision tasks has been a long-standing research direction to advance the capability of existing models. For object detection, the well-established classification and regression loss functions have been carefully designed by considering diverse learning challenges. Inspired by the recent progress in network architecture search, it is interesting to explore the possibility of discovering new loss function formulations via directly searching the primitive operation combinations. So that the learned losses not only fit for diverse object detection challenges to alleviate huge human efforts, but also have better alignment with evaluation metric and good mathematical convergence property. Beyond the previous auto-loss works on face recognition and image classification, our work makes the first attempt to discover new loss functions for the challenging object detection from primitive operation levels. We propose an effective convergence-simulation driven evolutionary search algorithm, called CSE-Autoloss, for speeding up the search progress by regularizing the mathematical rationality of loss candidates via convergence property verification and model optimization simulation. CSE-Autoloss involves the search space that cover a wide range of the possible variants of existing losses and discovers best-searched loss function combination within a short time (around 1.5 wall-clock days). We conduct extensive evaluations of loss function search on popular detectors and validate the good generalization capability of searched losses across diverse architectures and datasets. Our experiments show that the best-discovered loss function combinations outperform default combinations by 1.1% and 0.8% in terms of mAP for two-stage and one-stage detectors on COCO respectively. Our searched losses are available at https://github.com/PerdonLiu/CSE-Autoloss.

</details>

### Neural Architecture Search on ImageNet in Four GPU Hours: A Theoretically Inspired Perspective.
- **链接**: [arXiv:2102.11535](https://arxiv.org/abs/2102.11535)
- **作者**: Wuyang Chen, Xinyu Gong, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) has been explosively studied to automate the discovery of top-performer neural networks. Current works require heavy training of supernet or intensive architecture evaluations, thus suffering from heavy resource consumption and often incurring search bias due to truncated training or approximations. Can we select the best neural architectures without involving any training and eliminate a drastic portion of the search cost? We provide an affirmative answer, by proposing a novel framework called training-free neural architecture search (TE-NAS). TE-NAS ranks architectures by analyzing the spectrum of the neural tangent kernel (NTK) and the number of linear regions in the input space. Both are motivated by recent theory advances in deep networks and can be computed without any training and any label. We show that: (1) these two measurements imply the trainability and expressivity of a neural network; (2) they strongly correlate with the network's test accuracy. Further on, we design a pruning-based NAS mechanism to achieve a more flexible and superior trade-off between the trainability and expressivity during the search. In NAS-Bench-201 and DARTS search spaces, TE-NAS completes high-quality search but only costs 0.5 and 4 GPU hours with one 1080Ti on CIFAR-10 and ImageNet, respectively. We hope our work inspires more attempts in bridging the theoretical findings of deep networks and practical impacts in real NAS applications. Code is available at: https://github.com/VITA-Group/TENAS.

</details>

### DrNAS: Dirichlet Neural Architecture Search.
- **链接**: [arXiv:2006.10355](https://arxiv.org/abs/2006.10355)
- **作者**: Xiangning Chen, Ruochen Wang, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a novel differentiable architecture search method by formulating it into a distribution learning problem. We treat the continuously relaxed architecture mixing weight as random variables, modeled by Dirichlet distribution. With recently developed pathwise derivatives, the Dirichlet parameters can be easily optimized with gradient-based optimizer in an end-to-end manner. This formulation improves the generalization ability and induces stochasticity that naturally encourages exploration in the search space. Furthermore, to alleviate the large memory consumption of differentiable NAS, we propose a simple yet effective progressive learning scheme that enables searching directly on large-scale tasks, eliminating the gap between search and evaluation phases. Extensive experiments demonstrate the effectiveness of our method. Specifically, we obtain a test error of 2.46% for CIFAR-10, 23.7% for ImageNet under the mobile setting. On NAS-Bench-201, we also achieve state-of-the-art results on all three datasets and provide insights for the effective design of neural architecture search algorithms.

</details>

### Rapid Neural Architecture Search by Learning to Generate Graphs from Datasets.
- **链接**: [arXiv:2107.00860](https://arxiv.org/abs/2107.00860)
- **作者**: Hayeon Lee, Eunyoung Hyung, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the success of recent Neural Architecture Search (NAS) methods on various tasks which have shown to output networks that largely outperform human-designed networks, conventional NAS methods have mostly tackled the optimization of searching for the network architecture for a single task (dataset), which does not generalize well across multiple tasks (datasets). Moreover, since such task-specific methods search for a neural architecture from scratch for every given task, they incur a large computational cost, which is problematic when the time and monetary budget are limited. In this paper, we propose an efficient NAS framework that is trained once on a database consisting of datasets and pretrained networks and can rapidly search for a neural architecture for a novel dataset. The proposed MetaD2A (Meta Dataset-to-Architecture) model can stochastically generate graphs (architectures) from a given set (dataset) via a cross-modal latent space learned with amortized meta-learning. Moreover, we also propose a meta-performance predictor to estimate and select the best architecture without direct training on target datasets. The experimental results demonstrate that our model meta-learned on subsets of ImageNet-1K and architectures from NAS-Bench 201 search space successfully generalizes to multiple unseen datasets including CIFAR-10 and CIFAR-100, with an average search time of 33 GPU seconds. Even under MobileNetV3 search space, MetaD2A is 5.5K times faster than NSGANetV2, a transferable NAS method, with comparable performance. We believe that the MetaD2A proposes a new research direction for rapid NAS as well as ways to utilize the knowledge from rich databases of datasets and architectures accumulated over the past years. Code is available at https://github.com/HayeonLee/MetaD2A.

</details>

### Geometry-Aware Gradient Algorithms for Neural Architecture Search.
- **链接**: [arXiv:2004.07802](https://arxiv.org/abs/2004.07802)
- **作者**: Liam Li, Mikhail Khodak, Nina Balcan, Ameet Talwalkar
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent state-of-the-art methods for neural architecture search (NAS) exploit gradient-based optimization by relaxing the problem into continuous optimization over architectures and shared-weights, a noisy process that remains poorly understood. We argue for the study of single-level empirical risk minimization to understand NAS with weight-sharing, reducing the design of NAS methods to devising optimizers and regularizers that can quickly obtain high-quality solutions to this problem. Invoking the theory of mirror descent, we present a geometry-aware framework that exploits the underlying structure of this optimization to return sparse architectural parameters, leading to simple yet novel algorithms that enjoy fast convergence guarantees and achieve state-of-the-art accuracy on the latest NAS benchmarks in computer vision. Notably, we exceed the best published results for both CIFAR and ImageNet on both the DARTS search space and NAS-Bench201; on the latter we achieve near-oracle-optimal performance on CIFAR-10 and CIFAR-100. Together, our theory and experiments demonstrate a principled way to co-design optimizers and continuous relaxations of discrete NAS search spaces.

</details>
<!-- COMPLETE v1 papers=49 -->
