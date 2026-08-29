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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object tracking has achieved significant progress over the past few years. However, state-of-the-art trackers become increasingly heavy and expensive, which limits their deployments in resource-constrained applications. In this work, we present LightTrack, which uses neural architecture search (NAS) to design more lightweight and efficient object trackers. Comprehensive experiments show that our LightTrack is effective. It can find trackers that achieve superior performance compared to handcrafted SOTA trackers, such as SiamRPN++ and Ocean, while using much fewer model Flops and parameters. Moreover, when deployed on resource-constrained mobile chipsets, the discovered trackers run much faster. For example, on Snapdragon 845 Adreno GPU, LightTrack runs $12\times$ faster than Ocean, while using $13\times$ fewer parameters and $38\times$ fewer Flops. Such improvements might narrow the gap between academic models and industrial deployments in object tracking task. LightTrack is released at https://github.com/researchmm/LightTrack.

</details>

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

### TransNAS-Bench-101: Improving Transferability and Generalizability of Cross-Task Neural Architecture Search.
- **链接**: [arXiv:2105.11871](https://arxiv.org/abs/2105.11871) · 📚 被引 50
- **作者**: Yawen Duan, Xin Chen, Hang Xu, Zewei Chen, Xiaodan Liang, Tong Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### DOTS: Decoupling Operation and Topology in Differentiable Architecture Search.
- **链接**: [arXiv:2010.00969](https://arxiv.org/abs/2010.00969) · 📚 被引 41
- **作者**: Yuchao Gu, Lijuan Wang, Yun Liu, Yi Yang, Yu-Huan Wu, Shao-Ping Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

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

> Low-light image enhancement plays very important roles in low-level vision field. Recent works have built a large variety of deep learning models to address this task. However, these approaches mostly rely on significant architecture engineering and suffer from high computational burden. In this paper, we propose a new method, named Retinex-inspired Unrolling with Architecture Search (RUAS), to construct lightweight yet effective enhancement network for low-light images in real-world scenario. Specifically, building upon Retinex rule, RUAS first establishes models to characterize the intrinsic underexposed structure of low-light images and unroll their optimization processes to construct our holistic propagation structure. Then by designing a cooperative reference-free learning strategy to discover low-light prior architectures from a compact search space, RUAS is able to obtain a top-performing image enhancement network, which is with fast speed and requires few computational resources. Extensive experiments verify the superiority of our RUAS framework against recently proposed state-of-the-art methods.

</details>

### AttentiveNAS: Improving Neural Architecture Search via Attentive Sampling.
- **链接**: [arXiv:2011.09011](https://arxiv.org/abs/2011.09011) · [代码](https://github.com/facebookresearch/AttentiveNAS) · 📚 被引 80
- **作者**: Dilin Wang, Meng Li, Chengyue Gong, Vikas Chandra
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has shown great promise in designing state-of-the-art (SOTA) models that are both accurate and efficient. Recently, two-stage NAS, e.g. BigNAS, decouples the model training and searching process and achieves remarkable search efficiency and accuracy. Two-stage NAS requires sampling from the search space during training, which directly impacts the accuracy of the final searched models. While uniform sampling has been widely used for its simplicity, it is agnostic of the model performance Pareto front, which is the main focus in the search process, and thus, misses opportunities to further improve the model accuracy. In this work, we propose AttentiveNAS that focuses on improving the sampling strategy to achieve better performance Pareto. We also propose algorithms to efficiently and effectively identify the networks on the Pareto during training. Without extra re-training or post-processing, we can simultaneously obtain a large number of networks across a wide range of FLOPs. Our discovered model family, AttentiveNAS models, achieves top-1 accuracy from 77.3% to 80.7% on ImageNet, and outperforms SOTA models, including BigNAS and Once-for-All networks. We also achieve ImageNet accuracy of 80.1% with only 491 MFLOPs. Our training code and pretrained models are available at https://github.com/facebookresearch/AttentiveNAS.

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

### FP-NAS: Fast Probabilistic Neural Architecture Search.
- **链接**: [arXiv:2011.10949](https://arxiv.org/abs/2011.10949) · 📚 被引 18
- **作者**: Zhicheng Yan, Xiaoliang Dai, Peizhao Zhang, Yuandong Tian, Bichen Wu, Matt Feiszli
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differential Neural Architecture Search (NAS) requires all layer choices to be held in memory simultaneously; this limits the size of both search space and final architecture. In contrast, Probabilistic NAS, such as PARSEC, learns a distribution over high-performing architectures, and uses only as much memory as needed to train a single model. Nevertheless, it needs to sample many architectures, making it computationally expensive for searching in an extensive space. To solve these problems, we propose a sampling method adaptive to the distribution entropy, drawing more samples to encourage explorations at the beginning, and reducing samples as learning proceeds. Furthermore, to search fast in the multi-variate space, we propose a coarse-to-fine strategy by using a factorized distribution at the beginning which can reduce the number of architecture parameters by over an order of magnitude. We call this method Fast Probabilistic NAS (FP-NAS). Compared with PARSEC, it can sample 64% fewer architectures and search 2.1x faster. Compared with FBNetV2, FP-NAS is 1.9x - 3.5x faster, and the searched models outperform FBNetV2 models on ImageNet. FP-NAS allows us to expand the giant FBNetV2 space to be wider (i.e. larger channel choices) and deeper (i.e. more blocks), while adding Split-Attention block and enabling the search over the number of splits. When searching a model of size 0.4G FLOPS, FP-NAS is 132x faster than EfficientNet, and the searched FP-NAS-L0 model outperforms EfficientNet-B0 by 0.7% accuracy. Without using any architecture surrogate or scaling tricks, we directly search large models up to 1.0G FLOPS. Our FP-NAS-L2 model with simple distillation outperforms BigNAS-XL with advanced in-place distillation by 0.7% accuracy using similar FLOPS.

</details>

### HourNAS: Extremely Fast Neural Architecture Search Through an Hourglass Lens.
- **链接**: [arXiv:2005.14446](https://arxiv.org/abs/2005.14446) · 📚 被引 11
- **作者**: Zhaohui Yang, Yunhe Wang, Xinghao Chen, Jianyuan Guo, Wei Zhang, Chao Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) refers to automatically design the architecture. We propose an hourglass-inspired approach (HourNAS) for this problem that is motivated by the fact that the effects of the architecture often proceed from the vital few blocks. Acting like the narrow neck of an hourglass, vital blocks in the guaranteed path from the input to the output of a deep neural network restrict the information flow and influence the network accuracy. The other blocks occupy the major volume of the network and determine the overall network complexity, corresponding to the bulbs of an hourglass. To achieve an extremely fast NAS while preserving the high accuracy, we propose to identify the vital blocks and make them the priority in the architecture search. The search space of those non-vital blocks is further shrunk to only cover the candidates that are affordable under the computational resource constraints. Experimental results on the ImageNet show that only using 3 hours (0.1 days) with one GPU, our HourNAS can search an architecture that achieves a 77.0% Top-1 accuracy, which outperforms the state-of-the-art methods.

</details>

### Towards Improving the Consistency, Efficiency, and Flexibility of Differentiable Neural Architecture Search.
- **链接**: [arXiv:2101.11342](https://arxiv.org/abs/2101.11342) · 📚 被引 37
- **作者**: Yibo Yang, Shan You, Hongyang Li, Fei Wang, Chen Qian, Zhouchen Lin
- **🏷️ 机构**: Shanghai AI Lab, Peking University
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most differentiable neural architecture search methods construct a super-net for search and derive a target-net as its sub-graph for evaluation. There exists a significant gap between the architectures in search and evaluation. As a result, current methods suffer from an inconsistent, inefficient, and inflexible search process. In this paper, we introduce EnTranNAS that is composed of Engine-cells and Transit-cells. The Engine-cell is differentiable for architecture search, while the Transit-cell only transits a sub-graph by architecture derivation. Consequently, the gap between the architectures in search and evaluation is significantly reduced. Our method also spares much memory and computation cost, which speeds up the search process. A feature sharing strategy is introduced for more balanced optimization and more efficient search. Furthermore, we develop an architecture derivation method to replace the traditional one that is based on a hand-crafted rule. Our method enables differentiable sparsification, and keeps the derived architecture equivalent to that of Engine-cell, which further improves the consistency between search and evaluation. Besides, it supports the search for topology where a node can be connected to prior nodes with any number of connections, so that the searched architectures could be more flexible. For experiments on CIFAR-10, our search on the standard space requires only 0.06 GPU-day. We further have an error rate of 2.22% with 0.07 GPU-day for the search on an extended space. We can also directly perform the search on ImageNet with topology learnable and achieve a top-1 error rate of 23.8% in 2.1 GPU-day.

</details>

### Landmark Regularization: Ranking Guided Super-Net Training in Neural Architecture Search.
- **链接**: [arXiv:2104.05309](https://arxiv.org/abs/2104.05309) · 📚 被引 13
- **作者**: Kaicheng Yu, René Ranftl, Mathieu Salzmann
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weight sharing has become a de facto standard in neural architecture search because it enables the search to be done on commodity hardware. However, recent works have empirically shown a ranking disorder between the performance of stand-alone architectures and that of the corresponding shared-weight networks. This violates the main assumption of weight-sharing NAS algorithms, thus limiting their effectiveness. We tackle this issue by proposing a regularization term that aims to maximize the correlation between the performance rankings of the shared-weight network and that of the standalone architectures using a small set of landmark architectures. We incorporate our regularization term into three different NAS algorithms and show that it consistently improves performance across algorithms, search-spaces, and tasks.

</details>

### Neural Architecture Search With Random Labels.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_Neural_Architecture_Search_With_Random_Labels_CVPR_2021_paper.html) · 📚 被引 46
- **作者**: Xuanyang Zhang, Pengfei Hou, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### DCNAS: Densely Connected Neural Architecture Search for Semantic Image Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_DCNAS_Densely_Connected_Neural_Architecture_Search_for_Semantic_Image_Segmentation_CVPR_2021_paper.html) · 📚 被引 92
- **作者**: Xiong Zhang, Hongmin Xu, Hong Mo, Jianchao Tan, Cheng Yang, Lei Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

## 跨领域论文（完整笔记在其他领域）

- NPAS: A Compiler-Aware Framework of Unified Network Pruning and Architecture Search for Beyond Real-Time Mobile Acceleration. → [network-pruning](../network-pruning/Guideline%202021.md)
- Joint-DetNAS: Upgrade Your Detector With NAS, Pruning and Dynamic Distillation. → [network-pruning](../network-pruning/Guideline%202021.md)
