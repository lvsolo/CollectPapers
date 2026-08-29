# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Arch-Graph: Acyclic Architecture Relation Predictor for Task-Transferable Neural Architecture Search.
- **链接**: [arXiv:2204.05941](https://arxiv.org/abs/2204.05941) · 📚 被引 21
- **作者**: Minbin Huang, Zhijian Huang, Changlin Li, Xin Chen, Hang Xu, Zhenguo Li et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, ReLER AAII, UTS, The University of Hong Kong
- **会议**: CVPR 2022

### Large-Scale Graph Neural Architecture Search.
- **链接**: [出版页](https://proceedings.mlr.press/v162/guan22d.html)
- **作者**: Chaoyu Guan, Xin Wang, Hong Chen, Ziwei Zhang, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

> Neural Architecture Search (NAS) aims to find efficient models for multiple tasks. Beyond seeking solutions for a single task, there are surging interests in transferring network design knowledge across multiple tasks. In this line of research, effectively modeling task correlations is vital yet highly neglected. Therefore, we propose \textbf{Arch-Graph}, a transferable NAS method that predicts task-specific optimal architectures with respect to given task embeddings. It leverages correlations across multiple tasks by using their embeddings as a part of the predictor's input for fast adaptation. We also formulate NAS as an architecture relation graph prediction problem, with the relational graph constructed by treating candidate architectures as nodes and their pairwise relations as edges. To enforce some basic properties such as acyclicity in the relational graph, we add additional constraints to the optimization process, converting NAS into the problem of finding a Maximal Weighted Acyclic Subgraph (MWAS). Our algorithm then strives to eliminate cycles and only establish edges in the graph if the rank results can be trusted. Through MWAS, Arch-Graph can effectively rank candidate models for each task with only a small budget to finetune the predictor. With extensive experiments on TransNAS-Bench-101, we show Arch-Graph's transferability and high sample efficiency across numerous tasks, beating many NAS methods designed for both single-task and multi-task search. It is able to find top 0.16\% and 0.29\% architectures on average on two search spaces under the budget of only 50 models.

### AGNAS: Attention-Guided Micro and Macro-Architecture Search.
- **链接**: [出版页](https://proceedings.mlr.press/v162/sun22a.html)
- **作者**: Zihao Sun, Yu Hu, Shun Lu, Longxing Yang, Jilin Mei, Yinhe Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### ISNAS-DIP: Image-Specific Neural Architecture Search for Deep Image Prior.
- **链接**: [arXiv:2111.15362](https://arxiv.org/abs/2111.15362) · [代码](https://github.com/ozgurkara99/ISNAS-DIP) · 📚 被引 18
- **作者**: Metin Ersin Arican, Ozgur Kara, Gustav Bredell, Ender Konukoglu
- **🏷️ 机构**: Bogazici University,Department of Electrical and Electronics Engineering,Istanbul,Turkey, ETH-Zurich,Department of Information Technology and Electrical Engineering,Zurich,Switzerland
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works show that convolutional neural network (CNN) architectures have a spectral bias towards lower frequencies, which has been leveraged for various image restoration tasks in the Deep Image Prior (DIP) framework. The benefit of the inductive bias the network imposes in the DIP framework depends on the architecture. Therefore, researchers have studied how to automate the search to determine the best-performing model. However, common neural architecture search (NAS) techniques are resource and time-intensive. Moreover, best-performing models are determined for a whole dataset of images instead of for each image independently, which would be prohibitively expensive. In this work, we first show that optimal neural architectures in the DIP framework are image-dependent. Leveraging this insight, we then propose an image-specific NAS strategy for the DIP framework that requires substantially less training than typical NAS approaches, effectively enabling image-specific NAS. We justify the proposed strategy's effectiveness by (1) demonstrating its performance on a NAS Dataset for DIP that includes 522 models from a particular search space (2) conducting extensive experiments on image denoising, inpainting, and super-resolution tasks. Our experiments show that image-specific metrics can reduce the search space to a small cohort of models, of which the best model outperforms current NAS approaches for image restoration. Codes and datasets are available at https://github.com/ozgurkara99/ISNAS-DIP.

</details>

### Demystifying the Neural Tangent Kernel from a Practical Perspective: Can it be trusted for Neural Architecture Search without training?
- **链接**: [arXiv:2203.14577](https://arxiv.org/abs/2203.14577) · [代码](https://github.com/nutellamok/DemystifyingNTK) · 📚 被引 17
- **作者**: Jisoo Mok, Byunggook Na, Ji-Hoon Kim, Dongyoon Han, Sungroh Yoon
- **🏷️ 机构**: Seoul National University,Department of ECE, NAVER AI Lab
- **会议**: CVPR 2022

### TabNAS: Rejection Sampling for Neural Architecture Search on Tabular Datasets.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4e392aa9bc70ed731d3c9c32810f92fb-Abstract-Conference.html) · 📚 被引 1
- **作者**: Chengrun Yang, Gabriel Bender, Hanxiao Liu, Pieter-Jan Kindermans, Madeleine Udell, Yifeng Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

> In Neural Architecture Search (NAS), reducing the cost of architecture evaluation remains one of the most crucial challenges. Among a plethora of efforts to bypass training of each candidate architecture to convergence for evaluation, the Neural Tangent Kernel (NTK) is emerging as a promising theoretical framework that can be utilized to estimate the performance of a neural architecture at initialization. In this work, we revisit several at-initialization metrics that can be derived from the NTK and reveal their key shortcomings. Then, through the empirical analysis of the time evolution of NTK, we deduce that modern neural architectures exhibit highly non-linear characteristics, making the NTK-based metrics incapable of reliably estimating the performance of an architecture without some amount of training. To take such non-linear characteristics into account, we introduce Label-Gradient Alignment (LGA), a novel NTK-based metric whose inherent formulation allows it to capture the large amount of non-linear advantage present in modern neural architectures. With minimal amount of training, LGA obtains a meaningful level of rank correlation with the post-training test accuracy of an architecture. Lastly, we demonstrate that LGA, complemented with few epochs of training, successfully guides existing search algorithms to achieve competitive search performances with significantly less search cost. The code is available at: https://github.com/nutellamok/DemystifyingNTK.

</details>

### Distribution Consistent Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01061) · 📚 被引 7
- **作者**: Junyi Pan, Chong Sun, Yizhou Zhou, Ying Zhang, Chen Li
- **🏷️ 机构**: WeChat, Tencent Inc
- **会议**: CVPR 2022

### HyperSegNAS: Bridging One-Shot Neural Architecture Search with 3D Medical Image Segmentation using HyperNet.
- **链接**: [arXiv:2112.10652](https://arxiv.org/abs/2112.10652) · 📚 被引 32
- **作者**: Cheng Peng, Andriy Myronenko, Ali Hatamizadeh, Vishwesh Nath, Md Mahfuzur Rahman Siddiquee, Yufan He et al.
- **🏷️ 机构**: Johns Hopkins University, NVIDIA, Arizona State University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semantic segmentation of 3D medical images is a challenging task due to the high variability of the shape and pattern of objects (such as organs or tumors). Given the recent success of deep learning in medical image segmentation, Neural Architecture Search (NAS) has been introduced to find high-performance 3D segmentation network architectures. However, because of the massive computational requirements of 3D data and the discrete optimization nature of architecture search, previous NAS methods require a long search time or necessary continuous relaxation, and commonly lead to sub-optimal network architectures. While one-shot NAS can potentially address these disadvantages, its application in the segmentation domain has not been well studied in the expansive multi-scale multi-path search space. To enable one-shot NAS for medical image segmentation, our method, named HyperSegNAS, introduces a HyperNet to assist super-net training by incorporating architecture topology information. Such a HyperNet can be removed once the super-net is trained and introduces no overhead during architecture search. We show that HyperSegNAS yields better performing and more intuitive architectures compared to the previous state-of-the-art (SOTA) segmentation networks; furthermore, it can quickly and accurately find good architecture candidates under different computing constraints. Our method is evaluated on public datasets from the Medical Segmentation Decathlon (MSD) challenge, and achieves SOTA performances.

</details>

### Global Convergence of MAML and Theory-Inspired Neural Architecture Search for Few-Shot Learning.
- **链接**: [arXiv:2203.09137](https://arxiv.org/abs/2203.09137) · 📚 被引 34
- **作者**: Haoxiang Wang, Yite Wang, Ruoyu Sun, Bo Li
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model-agnostic meta-learning (MAML) and its variants have become popular approaches for few-shot learning. However, due to the non-convexity of deep neural nets (DNNs) and the bi-level formulation of MAML, the theoretical properties of MAML with DNNs remain largely unknown. In this paper, we first prove that MAML with over-parameterized DNNs is guaranteed to converge to global optima at a linear rate. Our convergence analysis indicates that MAML with over-parameterized DNNs is equivalent to kernel regression with a novel class of kernels, which we name as Meta Neural Tangent Kernels (MetaNTK). Then, we propose MetaNTK-NAS, a new training-free neural architecture search (NAS) method for few-shot learning that uses MetaNTK to rank and select architectures. Empirically, we compare our MetaNTK-NAS with previous NAS methods on two popular few-shot learning benchmarks, miniImageNet, and tieredImageNet. We show that the performance of MetaNTK-NAS is comparable or better than the state-of-the-art NAS method designed for few-shot learning while enjoying more than 100x speedup. We believe the efficiency of MetaNTK-NAS makes itself more practical for many real-world tasks.

</details>

### Shapley-NAS: Discovering Operation Contribution for Neural Architecture Search.
- **链接**: [arXiv:2206.09811](https://arxiv.org/abs/2206.09811) · [代码](https://github.com/Euphoria16/Shapley-NAS.git) · 📚 被引 55
- **作者**: Han Xiao, Ziwei Wang, Zheng Zhu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation,China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a Shapley value based method to evaluate operation contribution (Shapley-NAS) for neural architecture search. Differentiable architecture search (DARTS) acquires the optimal architectures by optimizing the architecture parameters with gradient descent, which significantly reduces the search cost. However, the magnitude of architecture parameters updated by gradient descent fails to reveal the actual operation importance to the task performance and therefore harms the effectiveness of obtained architectures. By contrast, we propose to evaluate the direct influence of operations on validation accuracy. To deal with the complex relationships between supernet components, we leverage Shapley value to quantify their marginal contributions by considering all possible combinations. Specifically, we iteratively optimize the supernet weights and update the architecture parameters by evaluating operation contributions via Shapley value, so that the optimal architectures are derived by selecting the operations that contribute significantly to the tasks. Since the exact computation of Shapley value is NP-hard, the Monte-Carlo sampling based algorithm with early truncation is employed for efficient approximation, and the momentum update mechanism is adopted to alleviate fluctuation of the sampling process. Extensive experiments on various datasets and various search spaces show that our Shapley-NAS outperforms the state-of-the-art methods by a considerable margin with light search cost. The code is available at https://github.com/Euphoria16/Shapley-NAS.git

</details>

### Performance-Aware Mutual Knowledge Distillation for Improving Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01162) · 📚 被引 13
- **作者**: Pengtao Xie, Xuefeng Du
- **🏷️ 机构**: University of California, San Diego,La Jolla,CA,United States, University of Wisconsin-Madison,Madison,WI,United States
- **会议**: CVPR 2022

### β-DARTS: Beta-Decay Regularization for Differentiable Architecture Search.
- **链接**: [arXiv:2203.01665](https://arxiv.org/abs/2203.01665) · 📚 被引 111
- **作者**: Peng Ye, Baopu Li, Yikang Li, Tao Chen, Jiayuan Fan, Wanli Ouyang
- **🏷️ 机构**: Fudan University, BAIDU USA LLC, Shanghai AI Laboratory
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search~(NAS) has attracted increasingly more attention in recent years because of its capability to design deep neural networks automatically. Among them, differential NAS approaches such as DARTS, have gained popularity for the search efficiency. However, they suffer from two main issues, the weak robustness to the performance collapse and the poor generalization ability of the searched architectures. To solve these two problems, a simple-but-efficient regularization method, termed as Beta-Decay, is proposed to regularize the DARTS-based NAS searching process. Specifically, Beta-Decay regularization can impose constraints to keep the value and variance of activated architecture parameters from too large. Furthermore, we provide in-depth theoretical analysis on how it works and why it works. Experimental results on NAS-Bench-201 show that our proposed method can help to stabilize the searching process and makes the searched network more transferable across different datasets. In addition, our search scheme shows an outstanding property of being less dependent on training time and data. Comprehensive experiments on a variety of search spaces and datasets validate the effectiveness of the proposed method.

</details>

### BaLeNAS: Differentiable Architecture Search via the Bayesian Learning Rule.
- **链接**: [arXiv:2111.13204](https://arxiv.org/abs/2111.13204) · 📚 被引 15
- **作者**: Miao Zhang, Shirui Pan, Xiaojun Chang, Steven Su, Jilin Hu, Gholamreza Haffari et al.
- **🏷️ 机构**: Aalborg University, Monash University, ReLER, AAII, UTS
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable Architecture Search (DARTS) has received massive attention in recent years, mainly because it significantly reduces the computational cost through weight sharing and continuous relaxation. However, more recent works find that existing differentiable NAS techniques struggle to outperform naive baselines, yielding deteriorative architectures as the search proceeds. Rather than directly optimizing the architecture parameters, this paper formulates the neural architecture search as a distribution learning problem through relaxing the architecture weights into Gaussian distributions. By leveraging the natural-gradient variational inference (NGVI), the architecture distribution can be easily optimized based on existing codebases without incurring more memory and computational consumption. We demonstrate how the differentiable NAS benefits from Bayesian principles, enhancing exploration and improving stability. The experimental results on NAS-Bench-201 and NAS-Bench-1shot1 benchmark datasets confirm the significant improvements the proposed framework can make. In addition, instead of simply applying the argmax on the learned parameters, we further leverage the recently-proposed training-free proxies in NAS to select the optimal architecture from a group architectures drawn from the optimized distribution, where we achieve state-of-the-art results on the NAS-Bench-201 and NAS-Bench-1shot1 benchmarks. Our best architecture in the DARTS search space also obtains competitive test errors with 2.37\%, 15.72\%, and 24.2\% on CIFAR-10, CIFAR-100, and ImageNet datasets, respectively.

</details>

### Neural Architecture Search with Representation Mutual Information.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01161)
- **作者**: Xiawu Zheng, Xiang Fei, Lei Zhang, Chenglin Wu, Fei Chao, Jianzhuang Liu et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2022

### Training-free Transformer Architecture Search.
- **链接**: [arXiv:2203.12217](https://arxiv.org/abs/2203.12217) · 📚 被引 56
- **作者**: Qinqin Zhou, Kekai Sheng, Xiawu Zheng, Ke Li, Xing Sun, Yonghong Tian et al.
- **🏷️ 机构**: School of Informatics, Xiamen University,Media Analytics and Computing Lab, Tencent Youtu Lab, Peng Cheng Laboratory
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, Vision Transformer (ViT) has achieved remarkable success in several computer vision tasks. The progresses are highly relevant to the architecture design, then it is worthwhile to propose Transformer Architecture Search (TAS) to search for better ViTs automatically. However, current TAS methods are time-consuming and existing zero-cost proxies in CNN do not generalize well to the ViT search space according to our experimental observations. In this paper, for the first time, we investigate how to conduct TAS in a training-free manner and devise an effective training-free TAS (TF-TAS) scheme. Firstly, we observe that the properties of multi-head self-attention (MSA) and multi-layer perceptron (MLP) in ViTs are quite different and that the synaptic diversity of MSA affects the performance notably. Secondly, based on the observation, we devise a modular strategy in TF-TAS that evaluates and ranks ViT architectures from two theoretical perspectives: synaptic diversity and synaptic saliency, termed as DSS-indicator. With DSS-indicator, evaluation results are strongly correlated with the test accuracies of ViT models. Experimental results demonstrate that our TF-TAS achieves a competitive performance against the state-of-the-art manually or automatically design ViT architectures, and it promotes the searching efficiency in ViT search space greatly: from about $24$ GPU days to less than $0.5$ GPU days. Moreover, the proposed DSS-indicator outperforms the existing cutting-edge zero-cost approaches (e.g., TE-score and NASWOT).

</details>

## 🆕 增量新增

### MAE-DET: Revisiting Maximum Entropy Principle in Zero-Shot NAS for Efficient Object Detection. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://proceedings.mlr.press/v162/sun22c.html)
- **作者**: Zhenhong Sun, Ming Lin, Xiuyu Sun, Zhiyu Tan, Hao Li, Rong Jin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022
- **摘要（中）**: 针对零样本神经架构搜索在目标检测中应用不足的问题，本文重新审视最大熵原理，提出MAE-DET方法。方法利用最大熵原理设计搜索策略，无需训练即可高效评估架构性能。相比传统NAS方法，该方法大幅降低了搜索成本。实验表明在目标检测任务上搜索到的架构性能优异。
- **摘要（英）**: This paper revisits the maximum entropy principle for zero-shot NAS in object detection, proposing MAE-DET. It designs a search strategy based on maximum entropy to evaluate architectures without training, significantly reducing search cost. The searched architectures achieve competitive detection performance.
- **核心贡献**: 提出基于最大熵的零样本NAS方法用于目标检测。
- **创新点**: 将最大熵原理引入零样本架构搜索，免训练评估。
- **结果**: 搜索到的架构在检测任务上性能优异。

### BLOX: Macro Neural Architecture Search Benchmark and Algorithms. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/c7589a96e8adfcf5a006c452b3758fd5-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 1
- **作者**: Thomas Chau, Lukasz Dudziak, Hongkai Wen, Nicholas D. Lane, Mohamed S. Abdelfattah
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
- **摘要（中）**: ①该论文针对宏观神经网络架构搜索（NAS）中缺乏标准化基准和高效算法的问题。②提出了BLOX，一个宏观NAS基准测试套件，并配套了相应的搜索算法。③相比已有工作，BLOX提供了更系统化的宏观搜索空间定义和评估协议。④由于摘要不完整，具体效果数据未提供，但基准的建立有助于推动该领域研究。
- **摘要（英）**: This paper addresses the lack of standardized benchmarks and efficient algorithms in macro neural architecture search. It introduces BLOX, a benchmark suite with associated search algorithms. The contribution lies in providing a systematic search space and evaluation protocol, though specific performance results are not detailed in the abstract.
- **核心贡献**: 提出了宏观NAS基准BLOX及配套算法。
- **创新点**: 系统化定义宏观搜索空间和评估协议。
- **结果**: 基准的建立，具体效果未明确。

### EAutoDet: Efficient Architecture Search for Object Detection. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.10747](https://arxiv.org/abs/2203.10747) · 📚 被引 24
- **作者**: Xiaoxing Wang, Jiale Lin, Juanping Zhao, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对目标检测中CNN训练耗时、直接在检测数据集上搜索架构成本极高（通常需数十甚至数百GPU天）的问题。②提出了高效框架EAutoDet，构建覆盖backbone和FPN的超级网络，采用可微搜索方法，并提出内核复用技术（共享候选操作权重并合并为单一卷积）以降低GPU内存和计算成本，同时引入动态通道细化策略搜索通道数。③相比现有检测NAS方法，显著提升了搜索效率，将搜索成本降至1.4 GPU天。④在COCO test-dev上，发现的架构达到40.1 mAP（120 FPS）和49.2 mAP（41.3 FPS），超越SOTA检测NAS方法，并成功迁移至旋转检测任务（DOTA上77.05 mAP50）。
- **摘要（英）**: This paper addresses the high computational cost of neural architecture search for object detection by proposing EAutoDet, an efficient framework that searches backbone and FPN architectures in 1.4 GPU-days via a differentiable supernet with kernel reusing and dynamic channel refinement. The discovered architectures achieve 40.1 mAP at 120 FPS and 49.2 mAP at 41.3 FPS on COCO test-dev, surpassing prior detection NAS methods, and transfer well to rotation detection.
- **核心贡献**: 提出了一种高效的检测NAS框架，在极低搜索成本下发现高性能backbone和FPN架构。
- **创新点**: 内核复用技术和动态通道细化策略，实现了可微搜索中的高效计算。
- **结果**: 在COCO上以1.4 GPU天搜索成本达到SOTA检测性能，并成功迁移至旋转检测。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training CNN for detection is time-consuming due to the large dataset and complex network modules, making it hard to search architectures on detection datasets directly, which usually requires vast search costs (usually tens and even hundreds of GPU-days). In contrast, this paper introduces an efficient framework, named EAutoDet, that can discover practical backbone and FPN architectures for object detection in 1.4 GPU-days. Specifically, we construct a supernet for both backbone and FPN modules and adopt the differentiable method. To reduce the GPU memory requirement and computational cost, we propose a kernel reusing technique by sharing the weights of candidate operations on one edge and consolidating them into one convolution. A dynamic channel refinement strategy is also introduced to search channel numbers. Extensive experiments show significant efficacy and efficiency of our method. In particular, the discovered architectures surpass state-of-the-art object detection NAS methods and achieve 40.1 mAP with 120 FPS and 49.2 mAP with 41.3 FPS on COCO test-dev set. We also transfer the discovered architectures to rotation detection task, which achieve 77.05 mAP$_{\text{50}}$ on DOTA-v1.0 test set with 21.1M parameters.

</details>

### Neural Architecture Search for Spiking Neural Networks. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2201.10355](https://arxiv.org/abs/2201.10355)
- **作者**: Youngeun Kim, Yuhang Li, Hyoungseob Park, Yeshwanth Venkatesha, Priyadarshini Panda
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对脉冲神经网络（SNN）使用类ANN架构导致性能次优的问题，提出了专门为SNN设计的神经架构搜索方法。该方法基于初始化时的激活模式选择能代表多样脉冲激活的架构，无需训练，并搜索前馈和反馈连接以利用时间信息。搜索得到的SNASNet在多个任务上取得更高性能，证明了反馈连接的重要性。
- **摘要（英）**: To address sub-optimal performance of SNNs using ANN-like architectures, this paper introduces a NAS approach for SNNs. It selects architectures based on activation patterns at initialization without training, and searches feedforward and feedback connections to leverage temporal information. The found SNASNet achieves higher performance, highlighting the importance of feedback connections.
- **核心贡献**: 提出首个针对SNN的NAS方法，并发现反馈连接对性能提升的关键作用。
- **创新点**: 利用初始化激活模式进行无训练架构搜索，并引入时间反馈连接。
- **结果**: SNASNet在多个任务上性能优于现有SNN架构。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spiking Neural Networks (SNNs) have gained huge attention as a potential energy-efficient alternative to conventional Artificial Neural Networks (ANNs) due to their inherent high-sparsity activation. However, most prior SNN methods use ANN-like architectures (e.g., VGG-Net or ResNet), which could provide sub-optimal performance for temporal sequence processing of binary information in SNNs. To address this, in this paper, we introduce a novel Neural Architecture Search (NAS) approach for finding better SNN architectures. Inspired by recent NAS approaches that find the optimal architecture from activation patterns at initialization, we select the architecture that can represent diverse spike activation patterns across different data samples without training. Moreover, to further leverage the temporal information among the spikes, we search for feed forward connections as well as backward connections (i.e., temporal feedback connections) between layers. Interestingly, SNASNet found by our search algorithm achieves higher performance with backward connections, demonstrating the importance of designing SNN architecture for suitably using temporal information. We conduct extensive experiments on three image recognition benchmarks where we show that SNASNet achieves state-of-the-art performance with significantly lower timesteps (5 timesteps). Code is available at Github.

</details>

### UniNet: Unified Architecture Search with Convolution, Transformer, and MLP. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2207.05420](https://arxiv.org/abs/2207.05420) · 📚 被引 21
- **作者**: Jihao Liu, Xin Huang, Guanglu Song, Hongsheng Li, Yu Liu
- **🏷️ 机构**: CUHK, SenseTime
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对如何有效组合卷积、Transformer和MLP算子以形成高性能混合视觉架构的问题。②提出了统一架构搜索方法UniNet，包含两个关键设计：将不同搜索算子统一建模，用相同配置参数表征，减少搜索空间大小；提出上下文感知下采样模块（DSMs）以缓解不同算子间的差距。③相比现有方法，统一建模降低了搜索成本，DSMs增强了特征适应性，有助于识别高性能混合架构。④摘要未提供具体数据，但通过强化学习搜索，预期在视觉任务上达到先进性能。
- **摘要（英）**: This paper addresses the challenge of effectively combining convolution, Transformer, and MLP operators for high-performance hybrid architectures. It proposes UniNet, a unified architecture search approach with unified operator modeling to reduce search space and context-aware downsampling modules (DSMs) to bridge operator gaps. This enables affordable search and better feature adaptation, with expected SOTA performance via RL-based search. Specific results are not provided.
- **核心贡献**: 提出统一架构搜索方法UniNet，结合卷积、Transformer和MLP，降低搜索成本。
- **创新点**: 统一算子建模和上下文感知下采样模块设计。
- **结果**: 摘要未提供具体数据，预期在视觉任务上表现优异。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, transformer and multi-layer perceptron (MLP) architectures have achieved impressive results on various vision tasks. However, how to effectively combine those operators to form high-performance hybrid visual architectures still remains a challenge. In this work, we study the learnable combination of convolution, transformer, and MLP by proposing a novel unified architecture search approach. Our approach contains two key designs to achieve the search for high-performance networks. First, we model the very different searchable operators in a unified form, and thus enable the operators to be characterized with the same set of configuration parameters. In this way, the overall search space size is significantly reduced, and the total search cost becomes affordable. Second, we propose context-aware downsampling modules (DSMs) to mitigate the gap between the different types of operators. Our proposed DSMs are able to better adapt features from different types of operators, which is important for identifying high-performance hybrid architectures. Finally, we integrate configurable operators and DSMs into a unified search space and search with a Reinforcement Learning-based search algorithm to fully explore the optimal combination of the operators. To this end, we search a baseline network and scale it up to obtain a family of models, named UniNets, which achieve much better accuracy and efficiency than previous ConvNets and Transformers. In particular, our UniNet-B5 achieves 84.9% top-1 accuracy on ImageNet, outperforming EfficientNet-B7 and BoTNet-T7 with 44% and 55% fewer FLOPs respectively. By pretraining on the ImageNet-21K, our UniNet-B6 achieves 87.4%, outperforming Swin-L with 51% fewer FLOPs and 41% fewer parameters. Code is available at https://github.com/Sense-X/UniNet.

</details>

### Data-Free Neural Architecture Search via Recursive Label Calibration. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2112.02086](https://arxiv.org/abs/2112.02086) · 📚 被引 5
- **作者**: Zechun Liu, Zhiqiang Shen, Yun Long, Eric P. Xing, Kwang-Ting Cheng, Chas Leichner
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对隐私保护和偏差避免等场景中，仅给定预训练模型而无原始训练数据时进行NAS的可行性问题。②提出通过递归标签校准合成可用数据，并采用区域更新策略生成多样且语义丰富的合成数据，同时使用输入和特征级正则化减少与自然图像的域差距，然后基于合成数据指导NAS。③相比现有数据-free NAS方法，增强了合成数据的语义、多样性和域一致性。④在DARTS、ProxylessNAS和SPOS三种NAS算法上验证，搜索到的架构性能与使用原始数据搜索的相当，证明了方法的有效性。
- **摘要（英）**: This paper explores data-free NAS by synthesizing data from a pre-trained model using recursive label calibration, regional update for diversity, and input/feature-level regularization to minimize domain gap. The approach is validated with DARTS, ProxylessNAS, and SPOS, achieving competitive architecture performance without original training data, addressing privacy and bias concerns.
- **核心贡献**: 提出了数据-free NAS框架，通过递归标签校准合成高质量数据以指导架构搜索。
- **创新点**: 递归标签校准和区域更新策略，提升合成数据的语义和多样性。
- **结果**: 在多种NAS算法上验证，性能与原始数据搜索相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper aims to explore the feasibility of neural architecture search (NAS) given only a pre-trained model without using any original training data. This is an important circumstance for privacy protection, bias avoidance, etc., in real-world scenarios. To achieve this, we start by synthesizing usable data through recovering the knowledge from a pre-trained deep neural network. Then we use the synthesized data and their predicted soft-labels to guide neural architecture search. We identify that the NAS task requires the synthesized data (we target at image domain here) with enough semantics, diversity, and a minimal domain gap from the natural images. For semantics, we propose recursive label calibration to produce more informative outputs. For diversity, we propose a regional update strategy to generate more diverse and semantically-enriched synthetic data. For minimal domain gap, we use input and feature-level regularization to mimic the original data distribution in latent space. We instantiate our proposed framework with three popular NAS algorithms: DARTS, ProxylessNAS and SPOS. Surprisingly, our results demonstrate that the architectures discovered by searching with our synthetic data achieve accuracy that is comparable to, or even higher than, architectures discovered by searching from the original ones, for the first time, deriving the conclusion that NAS can be done effectively with no need of access to the original or called natural data if the synthesis method is well designed.

</details>

### Robust Network Architecture Search via Feature Distortion Restraining. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20065-6_8) · 📚 被引 6
- **作者**: Yaguan Qian, Shenghui Huang, Bin Wang, Xiang Ling, Xiaohui Guan, Zhaoquan Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对NAS搜索过程中特征失真导致架构性能下降的问题。②提出了通过特征失真抑制的鲁棒NAS方法，但摘要内容缺失，无法详细描述具体技术。③改进点可能在于增强搜索过程的稳定性。④由于摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper proposes a robust NAS method via feature distortion restraining, but the abstract is incomplete, preventing detailed evaluation. It likely aims to improve search stability by mitigating feature distortion, though no quantitative results are provided.
- **核心贡献**: 提出特征失真抑制的鲁棒NAS方法。
- **创新点**: 特征失真抑制机制。
- **结果**: 未提供具体效果数据。

### Compiler-Aware Neural Architecture Search for On-Mobile Real-time Super-Resolution. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2207.12577](https://arxiv.org/abs/2207.12577) · 📚 被引 25
- **作者**: Yushu Wu, Yifan Gong, Pu Zhao, Yanyu Li, Zheng Zhan, Wei Niu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对移动设备上超分辨率（SR）推理的实时性需求，现有方法计算量大、功耗高。②提出了编译器感知的SR NAS框架，进行深度和每层宽度搜索，并采用自适应SR块，将推理速度直接纳入优化目标，同时使用集成编译器优化的速度模型预测延迟以加速收敛。③相比传统方法，直接考虑编译器优化和移动平台约束，实现了实时推理。④在移动平台GPU/DSP上实现720p分辨率的实时SR推理，PSNR和SSIM性能具有竞争力。
- **摘要（英）**: This paper proposes a compiler-aware NAS framework for real-time super-resolution on mobile devices, conducting depth and width search with adaptive blocks and incorporating a compiler-optimized speed model for latency prediction. It achieves real-time 720p SR inference on mobile GPU/DSP with competitive PSNR and SSIM, addressing computational and power constraints.
- **核心贡献**: 提出了编译器感知的NAS框架，实现移动端实时SR推理。
- **创新点**: 将编译器优化集成到速度模型中，联合优化图像质量和延迟。
- **结果**: 在移动平台上实现实时720p SR，性能具有竞争力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning-based super-resolution (SR) has gained tremendous popularity in recent years because of its high image quality performance and wide application scenarios. However, prior methods typically suffer from large amounts of computations and huge power consumption, causing difficulties for real-time inference, especially on resource-limited platforms such as mobile devices. To mitigate this, we propose a compiler-aware SR neural architecture search (NAS) framework that conducts depth search and per-layer width search with adaptive SR blocks. The inference speed is directly taken into the optimization along with the SR loss to derive SR models with high image quality while satisfying the real-time inference requirement. Instead of measuring the speed on mobile devices at each iteration during the search process, a speed model incorporated with compiler optimizations is leveraged to predict the inference latency of the SR block with various width configurations for faster convergence. With the proposed framework, we achieve real-time SR inference for implementing 720p resolution with competitive SR performance (in terms of PSNR and SSIM) on GPU/DSP of mobile platforms (Samsung Galaxy S21).

</details>

### A Max-Flow Based Approach for Neural Architecture Search. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_39)
- **作者**: Chao Xue, Xiaoxing Wang, Junchi Yan, Chun-Guang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对NAS中架构搜索的优化问题。②提出了基于最大流（Max-Flow）的NAS方法，但摘要内容缺失，无法详细描述具体算法。③改进点可能在于利用图论方法提升搜索效率。④由于摘要不完整，无法提供具体效果数据。
- **摘要（英）**: This paper proposes a max-flow based approach for neural architecture search, but the abstract is incomplete, limiting detailed assessment. It likely leverages graph theory for efficient search, though no quantitative results are available.
- **核心贡献**: 提出基于最大流的NAS优化方法。
- **创新点**: 将最大流理论应用于架构搜索。
- **结果**: 未提供具体效果数据。

### EAGAN: Efficient Two-Stage Evolutionary Architecture Search for GANs. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2111.15097](https://arxiv.org/abs/2111.15097) · 📚 被引 22
- **作者**: Guohao Ying, Xin He, Bin Gao, Bo Han, Xiaowen Chu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对GAN训练不稳定且手动设计架构需要专业知识的问题，提出自动搜索GAN架构的NAS方法。②提出了EAGAN，一种高效的两阶段进化算法NAS框架，将生成器（G）和判别器（D）的搜索解耦为两个阶段：阶段1用固定D搜索G并采用多对一训练策略，阶段2用最优G搜索D并采用一对一训练和权重重置策略。③相比早期仅搜索G的方法，EAGAN同时优化G和D，避免次优解；相比联合搜索方法，通过两阶段解耦和稳定性策略缓解了GAN训练不稳定性。④实验表明，EAGAN在多个数据集上取得了有竞争力的IS和FID分数，同时模型尺寸更小，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the instability of GAN training and the expertise required for manual architecture design by proposing EAGAN, an efficient two-stage evolutionary NAS framework that decouples generator and discriminator search. Stage-1 searches G with a fixed D using many-to-one training, while stage-2 searches D with the optimal G using one-to-one training and weight resetting, enhancing training stability. Compared to prior works, it jointly optimizes both G and D while mitigating instability, achieving competitive IS and FID scores with smaller model sizes, though specific numbers are not detailed in the abstract.
- **核心贡献**: 提出了一种两阶段进化NAS框架EAGAN，通过解耦G和D的搜索并引入稳定性策略，实现了高效且稳定的GAN架构自动搜索。
- **创新点**: 创新性地将GAN的G和D搜索解耦为两阶段，并采用多对一/一对一训练和权重重置策略来平衡搜索效率与训练稳定性。
- **结果**: 在图像生成任务上取得了有竞争力的IS和FID分数，同时降低了模型尺寸。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative adversarial networks (GANs) have proven successful in image generation tasks. However, GAN training is inherently unstable. Although many works try to stabilize it by manually modifying GAN architecture, it requires much expertise. Neural architecture search (NAS) has become an attractive solution to search GANs automatically. The early NAS-GANs search only generators to reduce search complexity but lead to a sub-optimal GAN. Some recent works try to search both generator (G) and discriminator (D), but they suffer from the instability of GAN training. To alleviate the instability, we propose an efficient two-stage evolutionary algorithm-based NAS framework to search GANs, namely EAGAN. We decouple the search of G and D into two stages, where stage-1 searches G with a fixed D and adopts the many-to-one training strategy, and stage-2 searches D with the optimal G found in stage-1 and adopts the one-to-one training and weight-resetting strategies to enhance the stability of GAN training. Both stages use the non-dominated sorting method to produce Pareto-front architectures under multiple objectives (e.g., model size, Inception Score (IS), and Fréchet Inception Distance (FID)). EAGAN is applied to the unconditional image generation task and can efficiently finish the search on the CIFAR-10 dataset in 1.2 GPU days. Our searched GANs achieve competitive results (IS=8.81$\pm$0.10, FID=9.91) on the CIFAR-10 dataset and surpass prior NAS-GANs on the STL-10 dataset (IS=10.44$\pm$0.087, FID=22.18). Source code: https://github.com/marsggbo/EAGAN.

</details>

### U-Boost NAS: Utilization-Boosted Differentiable Neural Architecture Search. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19775-8_11) · 📚 被引 3
- **作者**: Ahmet Caner Yüzügüler, Nikolaos Dimitriadis, Pascal Frossard
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对可微分神经网络架构搜索（DARTS）中架构利用率低的问题，即搜索过程中许多候选操作未被充分训练，导致搜索到的架构性能不佳。②提出了U-Boost NAS，一种利用率增强的可微分NAS方法，通过改进训练策略来提升候选操作的利用效率，但摘要内容不完整，具体方法细节未提供。③相比标准DARTS，U-Boost NAS旨在提高架构搜索的稳定性和最终性能，但缺乏详细对比信息。④由于摘要截断，无法获取具体实验效果和数据。
- **摘要（英）**: This paper addresses the low utilization of candidate operations in differentiable neural architecture search (DARTS), which leads to suboptimal searched architectures. It proposes U-Boost NAS, a utilization-boosted differentiable NAS method that enhances training efficiency of candidates, though the abstract is incomplete and lacks method details. Compared to standard DARTS, it aims to improve search stability and final performance, but no specific experimental results are available due to truncation.
- **核心贡献**: 提出了U-Boost NAS，一种通过提升候选操作利用率来改进可微分NAS的方法。
- **创新点**: 创新点在于通过利用率增强策略优化DARTS的训练过程，但具体机制未在摘要中阐明。
- **结果**: 由于摘要不完整，无法评估具体效果。

### NASViT: Neural Architecture Search for Efficient Vision Transformers with Gradient Conflict aware Supernet Training.
- **链接**: [出版页](https://openreview.net/forum?id=Qaw16njk6L)
- **作者**: Chengyue Gong, Dilin Wang, Meng Li, Xinlei Chen, Zhicheng Yan, Yuandong Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### SUMNAS: Supernet with Unbiased Meta-Features for Neural Architecture Search.
- **链接**: [出版页](https://openreview.net/forum?id=Z8FzvVU6_Kj)
- **作者**: Hyeonmin Ha, Ji-Hoon Kim, Semin Park, Byung-Gon Chun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### NASI: Label- and Data-agnostic Neural Architecture Search at Initialization.
- **链接**: [arXiv:2109.00817](https://arxiv.org/abs/2109.00817)
- **作者**: Yao Shu, Shaofeng Cai, Zhongxiang Dai, Beng Chin Ooi, Bryan Kian Hsiang Low
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed a surging interest in Neural Architecture Search (NAS). Various algorithms have been proposed to improve the search efficiency and effectiveness of NAS, i.e., to reduce the search cost and improve the generalization performance of the selected architectures, respectively. However, the search efficiency of these algorithms is severely limited by the need for model training during the search process. To overcome this limitation, we propose a novel NAS algorithm called NAS at Initialization (NASI) that exploits the capability of a Neural Tangent Kernel in being able to characterize the converged performance of candidate architectures at initialization, hence allowing model training to be completely avoided to boost the search efficiency. Besides the improved search efficiency, NASI also achieves competitive search effectiveness on various datasets like CIFAR-10/100 and ImageNet. Further, NASI is shown to be label- and data-agnostic under mild conditions, which guarantees the transferability of architectures selected by our NASI over different datasets.

</details>

### On Redundancy and Diversity in Cell-based Neural Architecture Search.
- **链接**: [arXiv:2203.08887](https://arxiv.org/abs/2203.08887)
- **作者**: Xingchen Wan, Binxin Ru, Pedro M. Esperança, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Searching for the architecture cells is a dominant paradigm in NAS. However, little attention has been devoted to the analysis of the cell-based search spaces even though it is highly important for the continual development of NAS. In this work, we conduct an empirical post-hoc analysis of architectures from the popular cell-based search spaces and find that the existing search spaces contain a high degree of redundancy: the architecture performance is minimally sensitive to changes at large parts of the cells, and universally adopted designs, like the explicit search for a reduction cell, significantly increase the complexities but have very limited impact on the performance. Across architectures found by a diverse set of search strategies, we consistently find that the parts of the cells that do matter for architecture performance often follow similar and simple patterns. By explicitly constraining cells to include these patterns, randomly sampled architectures can match or even outperform the state of the art. These findings cast doubts into our ability to discover truly novel architectures in the existing cell-based search spaces, and inspire our suggestions for improvement to guide future NAS research. Code is available at https://github.com/xingchenwan/cell-based-NAS-analysis.

</details>

### Graph Neural Architecture Search Under Distribution Shifts.
- **链接**: [出版页](https://proceedings.mlr.press/v162/qin22b.html)
- **作者**: Yijian Qin, Xin Wang, Ziwei Zhang, Pengtao Xie, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Analyzing and Mitigating Interference in Neural Architecture Search.
- **链接**: [arXiv:2108.12821](https://arxiv.org/abs/2108.12821)
- **作者**: Jin Xu, Xu Tan, Kaitao Song, Renqian Luo, Yichong Leng, Tao Qin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Deep and Flexible Graph Neural Architecture Search.
- **链接**: [出版页](https://proceedings.mlr.press/v162/zhang22s.html)
- **作者**: Wentao Zhang, Zheyu Lin, Yu Shen, Yang Li, Zhi Yang, Bin Cui
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Saliency-Aware Neural Architecture Search.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5e84e4413268b713f0d4a1b23a9dae57-Abstract-Conference.html) · 📚 被引 1
- **作者**: Ramtin Hosseini, Pengtao Xie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### LiteTransformerSearch: Training-free Neural Architecture Search for Efficient Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9949e6906be6448230cdba9a4cb2d564-Abstract-Conference.html) · 📚 被引 3
- **作者**: Mojan Javaheripi, Gustavo de Rosa, Subhabrata Mukherjee, Shital Shah, Tomasz Religa, Caio César Teodoro Mendes et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### NAS-Bench-Graph: Benchmarking Graph Neural Architecture Search.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/004bed4e186fdd7ebb73aad6e97c2332-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 5
- **作者**: Yijian Qin, Ziwei Zhang, Xin Wang, Zeyang Zhang, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Efficient Architecture Search for Diverse Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/6724eae98f3917968d54c193ac0b45f1-Abstract-Conference.html) · 📚 被引 5
- **作者**: Junhong Shen, Mikhail Khodak, Ameet Talwalkar
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Unifying and Boosting Gradient-Based Training-Free Neural Architecture Search.
- **链接**: [arXiv:2201.09785](https://arxiv.org/abs/2201.09785) · 📚 被引 1
- **作者**: Yao Shu, Zhongxiang Dai, Zhaoxuan Wu, Bryan Kian Hsiang Low
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has gained immense popularity owing to its ability to automate neural architecture design. A number of training-free metrics are recently proposed to realize NAS without training, hence making NAS more scalable. Despite their competitive empirical performances, a unified theoretical understanding of these training-free metrics is lacking. As a consequence, (a) the relationships among these metrics are unclear, (b) there is no theoretical interpretation for their empirical performances, and (c) there may exist untapped potential in existing training-free NAS, which probably can be unveiled through a unified theoretical understanding. To this end, this paper presents a unified theoretical analysis of gradient-based training-free NAS, which allows us to (a) theoretically study their relationships, (b) theoretically guarantee their generalization performances, and (c) exploit our unified theoretical understanding to develop a novel framework named hybrid NAS (HNAS) which consistently boosts training-free NAS in a principled way. Remarkably, HNAS can enjoy the advantages of both training-free (i.e., the superior search efficiency) and training-based (i.e., the remarkable search effectiveness) NAS, which we have demonstrated through extensive experiments.

</details>

### NAS-Bench-360: Benchmarking Neural Architecture Search on Diverse Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/506630e4a43bb9d64a49f98b9ba934e9-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 4
- **作者**: Renbo Tu, Nicholas Roberts, Mikhail Khodak, Junhong Shen, Frederic Sala, Ameet Talwalkar
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### ZARTS: On Zero-order Optimization for Neural Architecture Search.
- **链接**: [arXiv:2110.04743](https://arxiv.org/abs/2110.04743) · 📚 被引 3
- **作者**: Xiaoxing Wang, Wenxuan Guo, Jianlin Su, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable architecture search (DARTS) has been a popular one-shot paradigm for NAS due to its high efficiency. It introduces trainable architecture parameters to represent the importance of candidate operations and proposes first/second-order approximation to estimate their gradients, making it possible to solve NAS by gradient descent algorithm. However, our in-depth empirical results show that the approximation will often distort the loss landscape, leading to the biased objective to optimize and in turn inaccurate gradient estimation for architecture parameters. This work turns to zero-order optimization and proposes a novel NAS scheme, called ZARTS, to search without enforcing the above approximation. Specifically, three representative zero-order optimization methods are introduced: RS, MGS, and GLD, among which MGS performs best by balancing the accuracy and speed. Moreover, we explore the connections between RS/MGS and gradient descent algorithm and show that our ZARTS can be seen as a robust gradient-free counterpart to DARTS. Extensive experiments on multiple datasets and search spaces show the remarkable performance of our method. In particular, results on 12 benchmarks verify the outstanding robustness of ZARTS, where the performance of DARTS collapses due to its known instability issue. Also, we search on the search space of DARTS to compare with peer methods, and our discovered architecture achieves 97.54% accuracy on CIFAR-10 and 75.7% top-1 accuracy on ImageNet, which are state-of-the-art performance.

</details>

### Few-shot Task-agnostic Neural Architecture Search for Distilling Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/b7c12689a89e98a61bcaa65285a41b7c-Abstract-Conference.html) · 📚 被引 1
- **作者**: Dongkuan Xu, Subhabrata Mukherjee, Xiaodong Liu, Debadeepta Dey, Wenhui Wang, Xiang Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Interpreting Operation Selection in Differentiable Architecture Search: A Perspective from Influence-Directed Explanations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/cf1129594f603fde9e1913d10b7dbf77-Abstract-Conference.html) · 📚 被引 1
- **作者**: Miao Zhang, Wei Huang, Bin Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- ViTAS: Vision Transformer Architecture Search. → [vision-transformer](../vision-transformer/Guideline%202022.md)
- SuperTickets: Drawing Task-Agnostic Lottery Tickets from Supernets via Jointly Architecture Searching and Parameter Pruning. → [network-pruning](../network-pruning/Guideline%202022.md)
- Ensemble Knowledge Guided Sub-network Search and Fine-Tuning for Filter Pruning. → [network-pruning](../network-pruning/Guideline%202022.md)
<!-- COMPLETE v1 papers=42 -->
