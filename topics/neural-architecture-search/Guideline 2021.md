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
