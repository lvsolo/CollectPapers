# Network Pruning — 2024 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### AlterMOMA: Fusion Redundancy Pruning for Camera-LiDAR Fusion Models with Alternative Modality Masking.
- **链接**: [arXiv:2409.17728](https://arxiv.org/abs/2409.17728) · 📚 被引 0
- **作者**: Shiqi Sun, Yantao Lu, Ning Liu, Bo Jiang, Jinchao Chen, Ying Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-LiDAR fusion models significantly enhance perception performance in autonomous driving. The fusion mechanism leverages the strengths of each modality while minimizing their weaknesses. Moreover, in practice, camera-LiDAR fusion models utilize pre-trained backbones for efficient training. However, we argue that directly loading single-modal pre-trained camera and LiDAR backbones into camera-LiDAR fusion models introduces similar feature redundancy across modalities due to the nature of the fusion mechanism. Unfortunately, existing pruning methods are developed explicitly for single-modal models, and thus, they struggle to effectively identify these specific redundant parameters in camera-LiDAR fusion models. In this paper, to address the issue above on camera-LiDAR fusion models, we propose a novelty pruning framework Alternative Modality Masking Pruning (AlterMOMA), which employs alternative masking on each modality and identifies the redundant parameters. Specifically, when one modality parameters are masked (deactivated), the absence of features from the masked backbone compels the model to reactivate previous redundant features of the other modality backbone. Therefore, these redundant features and relevant redundant parameters can be identified via the reactivation process. The redundant parameters can be pruned by our proposed importance score evaluation function, Alternative Evaluation (AlterEva), which is based on the observation of the loss changes when certain modality parameters are activated and deactivated. Extensive experiments on the nuScene and KITTI datasets encompassing diverse tasks, baseline models, and pruning algorithms showcase that AlterMOMA outperforms existing pruning methods, attaining state-of-the-art performance.

</details>

### BMRS: Bayesian Model Reduction for Structured Pruning.
- **链接**: [arXiv:2406.01345](https://arxiv.org/abs/2406.01345) · 📚 被引 2
- **作者**: Dustin Wright, Christian Igel, Raghavendra Selvan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern neural networks are often massively overparameterized leading to high compute costs during training and at inference. One effective method to improve both the compute and energy efficiency of neural networks while maintaining good performance is structured pruning, where full network structures (e.g.~neurons or convolutional filters) that have limited impact on the model output are removed. In this work, we propose Bayesian Model Reduction for Structured pruning (BMRS), a fully end-to-end Bayesian method of structured pruning. BMRS is based on two recent methods: Bayesian structured pruning with multiplicative noise, and Bayesian model reduction (BMR), a method which allows efficient comparison of Bayesian models under a change in prior. We present two realizations of BMRS derived from different priors which yield different structured pruning characteristics: 1) BMRS_N with the truncated log-normal prior, which offers reliable compression rates and accuracy without the need for tuning any thresholds and 2) BMRS_U with the truncated log-uniform prior that can achieve more aggressive compression based on the boundaries of truncation. Overall, we find that BMRS offers a theoretically grounded approach to structured pruning of neural networks yielding both high compression rates and accuracy. Experiments on multiple datasets and neural networks of varying complexity showed that the two BMRS methods offer a competitive performance-efficiency trade-off compared to other pruning methods.

</details>

### Exploring Token Pruning in Vision State Space Models.
- **链接**: [arXiv:2409.18962](https://arxiv.org/abs/2409.18962) · 📚 被引 2
- **作者**: Zheng Zhan, Zhenglun Kong, Yifan Gong, Yushu Wu, Zichong Meng, Hangyu Zheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State Space Models (SSMs) have the advantage of keeping linear computational complexity compared to attention modules in transformers, and have been applied to vision tasks as a new type of powerful vision foundation model. Inspired by the observations that the final prediction in vision transformers (ViTs) is only based on a subset of most informative tokens, we take the novel step of enhancing the efficiency of SSM-based vision models through token-based pruning. However, direct applications of existing token pruning techniques designed for ViTs fail to deliver good performance, even with extensive fine-tuning. To address this issue, we revisit the unique computational characteristics of SSMs and discover that naive application disrupts the sequential token positions. This insight motivates us to design a novel and general token pruning method specifically for SSM-based vision models. We first introduce a pruning-aware hidden state alignment method to stabilize the neighborhood of remaining tokens for performance enhancement. Besides, based on our detailed analysis, we propose a token importance evaluation method adapted for SSM models, to guide the token pruning. With efficient implementation and practical acceleration methods, our method brings actual speedup. Extensive experiments demonstrate that our approach can achieve significant computation reduction with minimal impact on performance across different tasks. Notably, we achieve 81.7\% accuracy on ImageNet with a 41.6\% reduction in the FLOPs for pruned PlainMamba-L3. Furthermore, our work provides deeper insights into understanding the behavior of SSM-based vision models for future research.

</details>

### SequentialAttention++ for Block Sparsification: Differentiable Pruning Meets Combinatorial Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8735e0793cfd43327eceaacf39466a01-Abstract-Conference.html) · 📚 被引 0
- **作者**: Taisuke Yasuda, Kyriakos Axiotis, Gang Fu, Mohammad Hossein Bateni, Vahab Mirrokni
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### S2HPruner: Soft-to-Hard Distillation Bridges the Discretization Gap in Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d368aba36f74776cc7a1079332a31973-Abstract-Conference.html) · 📚 被引 1
- **作者**: Weihao Lin, Shengji Tang, Chong Yu, Peng Ye, Tao Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### SparseLLM: Towards Global Pruning of Pre-trained Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/522134ee1c52c7a2b929bc87cfe1781c-Abstract-Conference.html) · 📚 被引 13
- **作者**: Guangji Bai, Yijiang Li, Chen Ling, Kibaek Kim, Liang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Finding Transformer Circuits With Edge Pruning.
- **链接**: [arXiv:2406.16778](https://arxiv.org/abs/2406.16778) · 📚 被引 6
- **作者**: Adithya Bhaskar, Alexander Wettig, Dan Friedman, Danqi Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The path to interpreting a language model often proceeds via analysis of circuits -- sparse computational subgraphs of the model that capture specific aspects of its behavior. Recent work has automated the task of discovering circuits. Yet, these methods have practical limitations, as they rely either on inefficient search algorithms or inaccurate approximations. In this paper, we frame automated circuit discovery as an optimization problem and propose *Edge Pruning* as an effective and scalable solution. Edge Pruning leverages gradient-based pruning techniques, but instead of removing neurons or components, it prunes the \emph{edges} between components. Our method finds circuits in GPT-2 that use less than half the number of edges compared to circuits found by previous methods while being equally faithful to the full model predictions on standard circuit-finding tasks. Edge Pruning is efficient even with as many as 100K examples, outperforming previous methods in speed and producing substantially better circuits. It also perfectly recovers the ground-truth circuits in two models compiled with Tracr. Thanks to its efficiency, we scale Edge Pruning to CodeLlama-13B, a model over 100x the scale that prior methods operate on. We use this setting for a case study comparing the mechanisms behind instruction prompting and in-context learning. We find two circuits with more than 99.96% sparsity that match the performance of the full model and reveal that the mechanisms in the two settings overlap substantially. Our case study shows that Edge Pruning is a practical and scalable tool for interpretability and sheds light on behaviors that only emerge in large models.

</details>

### Beyond Efficiency: Molecular Data Pruning for Enhanced Generalization.
- **链接**: [arXiv:2409.01081](https://arxiv.org/abs/2409.01081) · 📚 被引 1
- **作者**: Dingshuo Chen, Zhixun Li, Yuyan Ni, Guibin Zhang, Ding Wang, Qiang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the emergence of various molecular tasks and massive datasets, how to perform efficient training has become an urgent yet under-explored issue in the area. Data pruning (DP), as an oft-stated approach to saving training burdens, filters out less influential samples to form a coreset for training. However, the increasing reliance on pretrained models for molecular tasks renders traditional in-domain DP methods incompatible. Therefore, we propose a Molecular data Pruning framework for enhanced Generalization (MolPeg), which focuses on the source-free data pruning scenario, where data pruning is applied with pretrained models. By maintaining two models with different updating paces during training, we introduce a novel scoring function to measure the informativeness of samples based on the loss discrepancy. As a plug-and-play framework, MolPeg realizes the perception of both source and target domain and consistently outperforms existing DP methods across four downstream tasks. Remarkably, it can surpass the performance obtained from full-dataset training, even when pruning up to 60-70% of the data on HIV and PCBA dataset. Our work suggests that the discovery of effective data-pruning metrics could provide a viable path to both enhanced efficiency and superior generalization in transfer learning.

</details>

### DISP-LLM: Dimension-Independent Structural Pruning for Large Language Models.
- **链接**: [arXiv:2410.11988](https://arxiv.org/abs/2410.11988) · 📚 被引 14
- **作者**: Shangqian Gao, Chi-Heng Lin, Ting Hua, Zheng Tang, Yilin Shen, Hongxia Jin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) have achieved remarkable success in various natural language processing tasks, including language modeling, understanding, and generation. However, the increased memory and computational costs associated with these models pose significant challenges for deployment on resource-limited devices. Structural pruning has emerged as a promising solution to reduce the costs of LLMs without requiring post-processing steps. Prior structural pruning methods either follow the dependence of structures at the cost of limiting flexibility, or introduce non-trivial additional parameters by incorporating different projection matrices. In this work, we propose a novel approach that relaxes the constraint imposed by regular structural pruning methods and eliminates the structural dependence along the embedding dimension. Our dimension-independent structural pruning method offers several benefits. Firstly, our method enables different blocks to utilize different subsets of the feature maps. Secondly, by removing structural dependence, we facilitate each block to possess varying widths along its input and output dimensions, thereby significantly enhancing the flexibility of structural pruning. We evaluate our method on various LLMs, including OPT, LLaMA, LLaMA-2, Phi-1.5, and Phi-2. Experimental results demonstrate that our approach outperforms other state-of-the-art methods, showing for the first time that structural pruning can achieve an accuracy similar to semi-structural pruning.

</details>

### Layer-Adaptive State Pruning for Deep State Space Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/14730e0dd6ac1c4a5765310909fd51b1-Abstract-Conference.html) · 📚 被引 2
- **作者**: Minseon Gwak, Seongrok Moon, Joohwan Ko, PooGyeon Park
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Pruning neural network models for gene regulatory dynamics using data and domain knowledge.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d52d2281babd36913643392a09a56832-Abstract-Conference.html) · 📚 被引 0
- **作者**: Intekhab Hossain, Jonas Fischer, Rebekka Burkholz, John Quackenbush
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### S-STE: Continuous Pruning Function for Efficient 2: 4 Sparse Pre-training.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/3b576711b12ab036b45130fc8eb78504-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yuezhou Hu, Jun Zhu, Jianfei Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Fast Iterative Hard Thresholding Methods with Pruning Gradient Computations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5eaa54503005d9125ad6aa3044e912d8-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yasutoshi Ida, Sekitoshi Kanai, Atsutoshi Kumagai, Tomoharu Iwata, Yasuhiro Fujiwara
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Spectral Graph Pruning Against Over-Squashing and Over-Smoothing.
- **链接**: [arXiv:2404.04612](https://arxiv.org/abs/2404.04612) · 📚 被引 4
- **作者**: Adarsh Jamadandi, Celia Rubio-Madrigal, Rebekka Burkholz
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Message Passing Graph Neural Networks are known to suffer from two problems that are sometimes believed to be diametrically opposed: over-squashing and over-smoothing. The former results from topological bottlenecks that hamper the information flow from distant nodes and are mitigated by spectral gap maximization, primarily, by means of edge additions. However, such additions often promote over-smoothing that renders nodes of different classes less distinguishable. Inspired by the Braess phenomenon, we argue that deleting edges can address over-squashing and over-smoothing simultaneously. This insight explains how edge deletions can improve generalization, thus connecting spectral gap optimization to a seemingly disconnected objective of reducing computational resources by pruning graphs for lottery tickets. To this end, we propose a more effective spectral gap optimization framework to add or delete edges and demonstrate its effectiveness on large heterophilic datasets.

</details>

### DapperFL: Domain Adaptive Federated Learning with Model Fusion Pruning for Edge Devices.
- **链接**: [arXiv:2412.05823](https://arxiv.org/abs/2412.05823) · [代码](https://github.com/jyzgh/DapperFL) · 📚 被引 5
- **作者**: Yongzhe Jia, Xuyun Zhang, Hongsheng Hu, Kim-Kwang Raymond Choo, Lianyong Qi, Xiaolong Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated learning (FL) has emerged as a prominent machine learning paradigm in edge computing environments, enabling edge devices to collaboratively optimize a global model without sharing their private data. However, existing FL frameworks suffer from efficacy deterioration due to the system heterogeneity inherent in edge computing, especially in the presence of domain shifts across local data. In this paper, we propose a heterogeneous FL framework DapperFL, to enhance model performance across multiple domains. In DapperFL, we introduce a dedicated Model Fusion Pruning (MFP) module to produce personalized compact local models for clients to address the system heterogeneity challenges. The MFP module prunes local models with fused knowledge obtained from both local and remaining domains, ensuring robustness to domain shifts. Additionally, we design a Domain Adaptive Regularization (DAR) module to further improve the overall performance of DapperFL. The DAR module employs regularization generated by the pruned model, aiming to learn robust representations across domains. Furthermore, we introduce a specific aggregation algorithm for aggregating heterogeneous local models with tailored architectures and weights. We implement DapperFL on a realworld FL platform with heterogeneous clients. Experimental results on benchmark datasets with multiple domains demonstrate that DapperFL outperforms several state-of-the-art FL frameworks by up to 2.28%, while significantly achieving model volume reductions ranging from 20% to 80%. Our code is available at: https://github.com/jyzgh/DapperFL.

</details>

### Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ff997469ac66cf893c4183efeb22212a-Abstract-Conference.html) · 📚 被引 7
- **作者**: Lujun Li, Peijie Dong, Zhenheng Tang, Xiang Liu, Qiang Wang, Wenhan Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### SlimGPT: Layer-wise Structured Pruning for Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c1c44e46358e0fb94dc94ec495a7fb1a-Abstract-Conference.html) · 📚 被引 12
- **作者**: Gui Ling, Ziyang Wang, Yuliang Yan, Qingwen Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models.
- **链接**: [arXiv:2410.10912](https://arxiv.org/abs/2410.10912) · [代码](https://github.com/haiquanlu/AlphaPruning) · 📚 被引 8
- **作者**: Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work on pruning large language models (LLMs) has shown that one can eliminate a large number of parameters without compromising performance, making pruning a promising strategy to reduce LLM model size. Existing LLM pruning strategies typically assign uniform pruning ratios across layers, limiting overall pruning ability; and recent work on layerwise pruning of LLMs is often based on heuristics that can easily lead to suboptimal performance. In this paper, we leverage Heavy-Tailed Self-Regularization (HT-SR) Theory, in particular the shape of empirical spectral densities (ESDs) of weight matrices, to design improved layerwise pruning ratios for LLMs. Our analysis reveals a wide variability in how well-trained, and thus relatedly how prunable, different layers of an LLM are. Based on this, we propose AlphaPruning, which uses shape metrics to allocate layerwise sparsity ratios in a more theoretically principled manner. AlphaPruning can be used in conjunction with multiple existing LLM pruning methods. Our empirical results show that AlphaPruning prunes LLaMA-7B to 80% sparsity while maintaining reasonable perplexity, marking a first in the literature on LLMs. We have open-sourced our code at https://github.com/haiquanlu/AlphaPruning.

</details>

### ALPS: Improved Optimization for Highly Sparse One-Shot Pruning for Large Language Models.
- **链接**: [arXiv:2406.07831](https://arxiv.org/abs/2406.07831) · 📚 被引 0
- **作者**: Xiang Meng, Kayhan Behdin, Haoyue Wang, Rahul Mazumder
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The impressive performance of Large Language Models (LLMs) across various natural language processing tasks comes at the cost of vast computational resources and storage requirements. One-shot pruning techniques offer a way to alleviate these burdens by removing redundant weights without the need for retraining. Yet, the massive scale of LLMs often forces current pruning approaches to rely on heuristics instead of optimization-based techniques, potentially resulting in suboptimal compression. In this paper, we introduce ALPS, an optimization-based framework that tackles the pruning problem using the operator splitting technique and a preconditioned conjugate gradient-based post-processing step. Our approach incorporates novel techniques to accelerate and theoretically guarantee convergence while leveraging vectorization and GPU parallelism for efficiency. ALPS substantially outperforms state-of-the-art methods in terms of the pruning objective and perplexity reduction, particularly for highly sparse models. On the OPT-30B model with 70% sparsity, ALPS achieves a 13% reduction in test perplexity on the WikiText dataset and a 19% improvement in zero-shot benchmark performance compared to existing methods.

</details>

### Compact Language Models via Pruning and Knowledge Distillation.
- **链接**: [arXiv:2407.14679](https://arxiv.org/abs/2407.14679) · 📚 被引 21
- **作者**: Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi et al.
- **🏷️ 机构**: NVIDIA
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) targeting different deployment scales and sizes are currently produced by training each variant from scratch; this is extremely compute-intensive. In this paper, we investigate if pruning an existing LLM and then re-training it with a fraction (<3%) of the original training data can be a suitable alternative to repeated, full retraining. To this end, we develop a set of practical and effective compression best practices for LLMs that combine depth, width, attention and MLP pruning with knowledge distillation-based retraining; we arrive at these best practices through a detailed empirical exploration of pruning strategies for each axis, methods to combine axes, distillation strategies, and search techniques for arriving at optimal compressed architectures. We use this guide to compress the Nemotron-4 family of LLMs by a factor of 2-4x, and compare their performance to similarly-sized models on a variety of language modeling tasks. Deriving 8B and 4B models from an already pretrained 15B model using our approach requires up to 40x fewer training tokens per model compared to training from scratch; this results in compute cost savings of 1.8x for training the full model family (15B, 8B, and 4B). Minitron models exhibit up to a 16% improvement in MMLU scores compared to training from scratch, perform comparably to other community models such as Mistral 7B, Gemma 7B and Llama-3 8B, and outperform state-of-the-art compression techniques from the literature. We have open-sourced Minitron model weights on Huggingface, with corresponding supplementary material including example code available on GitHub.

</details>

### DEPrune: Depth-wise Separable Convolution Pruning for Maximizing GPU Parallelism.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c16a99558b0b4f6b10966ca9bdb98ade-Abstract-Conference.html) · 📚 被引 5
- **作者**: Cheonjun Park, Mincheol Park, Hyunchan Moon, Myung Kuk Yoon, Seokjin Go, Suhyun Kim et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Faster Differentially Private Top-k Selection: A Joint Exponential Mechanism with Pruning.
- **链接**: [arXiv:2411.09552](https://arxiv.org/abs/2411.09552) · 📚 被引 1
- **作者**: Hao Wu, Hanwen Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the differentially private top-$k$ selection problem, aiming to identify a sequence of $k$ items with approximately the highest scores from $d$ items. Recent work by Gillenwater et al. (ICML '22) employs a direct sampling approach from the vast collection of $d^{\,Θ(k)}$ possible length-$k$ sequences, showing superior empirical accuracy compared to previous pure or approximate differentially private methods. Their algorithm has a time and space complexity of $\tilde{O}(dk)$. In this paper, we present an improved algorithm with time and space complexity $O(d + k^2 / ε\cdot \ln d)$, where $ε$ denotes the privacy parameter. Experimental results show that our algorithm runs orders of magnitude faster than their approach, while achieving similar empirical accuracy.

</details>

### Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/448444518637da106d978ae7409d9789-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xinhao Yao, Xiaolin Hu, Shenzhi Yang, Yong Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### 3D Gaussian Rendering Can Be Sparser: Efficient Rendering via Learned Fragment Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/0b2de71212384ffcaf80ad9fd1a21fe3-Abstract-Conference.html) · 📚 被引 5
- **作者**: Zhifan Ye, Chenxi Wan, Chaojian Li, Jihoon Hong, Sixu Li, Leshu Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### GDeR: Safeguarding Efficiency, Balancing, and Robustness via Prototypical Graph Pruning.
- **链接**: [arXiv:2410.13761](https://arxiv.org/abs/2410.13761) · 📚 被引 0
- **作者**: Guibin Zhang, Haonan Dong, Yuchen Zhang, Zhixun Li, Dingshuo Chen, Kai Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training high-quality deep models necessitates vast amounts of data, resulting in overwhelming computational and memory demands. Recently, data pruning, distillation, and coreset selection have been developed to streamline data volume by retaining, synthesizing, or selecting a small yet informative subset from the full set. Among these methods, data pruning incurs the least additional training cost and offers the most practical acceleration benefits. However, it is the most vulnerable, often suffering significant performance degradation with imbalanced or biased data schema, thus raising concerns about its accuracy and reliability in on-device deployment. Therefore, there is a looming need for a new data pruning paradigm that maintains the efficiency of previous practices while ensuring balance and robustness. Unlike the fields of computer vision and natural language processing, where mature solutions have been developed to address these issues, graph neural networks (GNNs) continue to struggle with increasingly large-scale, imbalanced, and noisy datasets, lacking a unified dataset pruning solution. To achieve this, we introduce a novel dynamic soft-pruning method, GDeR, designed to update the training ``basket'' during the process using trainable prototypes. GDeR first constructs a well-modeled graph embedding hypersphere and then samples \textit{representative, balanced, and unbiased subsets} from this embedding space, which achieves the goal we called Graph Training Debugging. Extensive experiments on five datasets across three GNN backbones, demonstrate that GDeR (I) achieves or surpasses the performance of the full dataset with 30%~50% fewer training samples, (II) attains up to a 2.81x lossless training speedup, and (III) outperforms state-of-the-art pruning methods in imbalanced training and noisy training scenarios by 0.3%~4.3% and 3.6%~7.8%, respectively.

</details>

### HEPrune: Fast Private Training of Deep Neural Networks With Encrypted Data Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5b26b9e634ba10f6c51c6db7365c4c28-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yancheng Zhang, Mengxin Zheng, Yuzhang Shang, Xun Chen, Qian Lou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models.
- **链接**: [arXiv:2409.17481](https://arxiv.org/abs/2409.17481) · [代码](https://github.com/NVlabs/MaskLLM) · 📚 被引 14
- **作者**: Gongfan Fang, Hongxu Yin, Saurav Muralidharan, Greg Heinrich, Jeff Pool, Jan Kautz et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) are distinguished by their massive parameter counts, which typically result in significant redundancy. This work introduces MaskLLM, a learnable pruning method that establishes Semi-structured (or ``N:M'') Sparsity in LLMs, aimed at reducing computational overhead during inference. Instead of developing a new importance criterion, MaskLLM explicitly models N:M patterns as a learnable distribution through Gumbel Softmax sampling. This approach facilitates end-to-end training on large-scale datasets and offers two notable advantages: 1) High-quality Masks - our method effectively scales to large datasets and learns accurate masks; 2) Transferability - the probabilistic modeling of mask distribution enables the transfer learning of sparsity across domains or tasks. We assessed MaskLLM using 2:4 sparsity on various LLMs, including LLaMA-2, Nemotron-4, and GPT-3, with sizes ranging from 843M to 15B parameters, and our empirical results show substantial improvements over state-of-the-art methods. For instance, leading approaches achieve a perplexity (PPL) of 10 or greater on Wikitext compared to the dense model's 5.12 PPL, but MaskLLM achieves a significantly lower 6.72 PPL solely by learning the masks with frozen weights. Furthermore, MaskLLM's learnable nature allows customized masks for lossless application of 2:4 sparsity to downstream tasks or domains. Code is available at https://github.com/NVlabs/MaskLLM.

</details>

### Sparsity-Agnostic Linear Bandits with Adaptive Adversaries.
- **链接**: [arXiv:2406.01192](https://arxiv.org/abs/2406.01192) · 📚 被引 0
- **作者**: Tianyuan Jin, Kyoungseok Jang, Nicolò Cesa-Bianchi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study stochastic linear bandits where, in each round, the learner receives a set of actions (i.e., feature vectors), from which it chooses an element and obtains a stochastic reward. The expected reward is a fixed but unknown linear function of the chosen action. We study sparse regret bounds, that depend on the number $S$ of non-zero coefficients in the linear reward function. Previous works focused on the case where $S$ is known, or the action sets satisfy additional assumptions. In this work, we obtain the first sparse regret bounds that hold when $S$ is unknown and the action sets are adversarially generated. Our techniques combine online to confidence set conversions with a novel randomized model selection approach over a hierarchy of nested confidence sets. When $S$ is known, our analysis recovers state-of-the-art bounds for adversarial action sets. We also show that a variant of our approach, using Exp3 to dynamically select the confidence sets, can be used to improve the empirical performance of stochastic linear bandits while enjoying a regret bound with optimal dependence on the time horizon.

</details>

### Adaptive Layer Sparsity for Large Language Models via Activation Correlation Assessment.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c573258c38d0a3919d8c1364053c45df-Abstract-Conference.html) · 📚 被引 2
- **作者**: Wei Li, Lujun Li, Mark G. Lee, Shengjie Sun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Navigating Extremes: Dynamic Sparsity in Large Output Spaces.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d4bdeed749a437de2cbe2e2c7e5a6a8a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Nasibullah Nasibullah, Erik Schultheis, Mike Lasby, Yani Ioannou, Rohit Babbar
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### On the Sparsity of the Strong Lottery Ticket Hypothesis.
- **链接**: [arXiv:2410.14754](https://arxiv.org/abs/2410.14754) · 📚 被引 0
- **作者**: Emanuele Natale, Davide Ferré, Giordano Giambartolomei, Frédéric Giroire, Frederik Mallmann-Trenn
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Considerable research efforts have recently been made to show that a random neural network $N$ contains subnetworks capable of accurately approximating any given neural network that is sufficiently smaller than $N$, without any training. This line of research, known as the Strong Lottery Ticket Hypothesis (SLTH), was originally motivated by the weaker Lottery Ticket Hypothesis, which states that a sufficiently large random neural network $N$ contains \emph{sparse} subnetworks that can be trained efficiently to achieve performance comparable to that of training the entire network $N$. Despite its original motivation, results on the SLTH have so far not provided any guarantee on the size of subnetworks. Such limitation is due to the nature of the main technical tool leveraged by these results, the Random Subset Sum (RSS) Problem. Informally, the RSS Problem asks how large a random i.i.d. sample $Ω$ should be so that we are able to approximate any number in $[-1,1]$, up to an error of $ ε$, as the sum of a suitable subset of $Ω$. We provide the first proof of the SLTH in classical settings, such as dense and equivariant networks, with guarantees on the sparsity of the subnetworks. Central to our results, is the proof of an essentially tight bound on the Random Fixed-Size Subset Sum Problem (RFSS), a variant of the RSS Problem in which we only ask for subsets of a given size, which is of independent interest.

</details>

### Improving Decision Sparsity.
- **链接**: [arXiv:2410.20483](https://arxiv.org/abs/2410.20483)
- **作者**: Yiyang Sun, Tong Wang, Cynthia Rudin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparsity is a central aspect of interpretability in machine learning. Typically, sparsity is measured in terms of the size of a model globally, such as the number of variables it uses. However, this notion of sparsity is not particularly relevant for decision-making; someone subjected to a decision does not care about variables that do not contribute to the decision. In this work, we dramatically expand a notion of decision sparsity called the Sparse Explanation Value(SEV) so that its explanations are more meaningful. SEV considers movement along a hypercube towards a reference point. By allowing flexibility in that reference and by considering how distances along the hypercube translate to distances in feature space, we can derive sparser and more meaningful explanations for various types of function classes. We present cluster-based SEV and its variant tree-based SEV, introduce a method that improves credibility of explanations, and propose algorithms that optimize decision sparsity in machine learning models.

</details>

### Exploiting Activation Sparsity with Dense to Dynamic-k Mixture-of-Experts Conversion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/4c2092ec0b1370cce3fb5965ab255fae-Abstract-Conference.html) · 📚 被引 1
- **作者**: Filip Szatkowski, Bartosz Wójcik, Mikolaj Piórczynski, Simone Scardapane
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### S2FT: Efficient, Scalable and Generalizable LLM Fine-tuning by Structured Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6e3b9fb0c0c56cf6e1ee61e6a068fca4-Abstract-Conference.html) · 📚 被引 1
- **作者**: Xinyu Yang, Jixuan Leng, Geyang Guo, Jiawei Zhao, Ryumei Nakada, Linjun Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Learn To be Efficient: Build Structured Sparsity in Large Language Models.
- **链接**: [arXiv:2402.06126](https://arxiv.org/abs/2402.06126) · 📚 被引 3
- **作者**: Haizhong Zheng, Xiaoyan Bai, Xueshen Liu, Zhuoqing Morley Mao, Beidi Chen, Fan Lai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) have achieved remarkable success with their billion-level parameters, yet they incur high inference overheads. The emergence of activation sparsity in LLMs provides a natural approach to reduce this cost by involving only parts of the parameters for inference. However, existing methods only focus on utilizing this naturally formed activation sparsity in a post-training setting, overlooking the potential for further amplifying this inherent sparsity. In this paper, we hypothesize that LLMs can learn to be efficient by achieving more structured activation sparsity. To achieve this, we introduce a novel training algorithm, Learn-To-be-Efficient (LTE), designed to train efficiency-aware LLMs to learn to activate fewer neurons and achieve a better trade-off between sparsity and performance. Furthermore, unlike SOTA MoEfication methods, which mainly focus on ReLU-based models, LTE can also be applied to LLMs like LLaMA using non-ReLU activations. Extensive evaluation on language understanding, language generation, and instruction tuning tasks show that LTE consistently outperforms SOTA baselines. Along with our hardware-aware custom kernel implementation, LTE reduces LLaMA2-7B inference latency by 25% at 50% sparsity.

</details>
