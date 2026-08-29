# Network Pruning — 2025 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 25 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DeepCompress-ViT: Rethinking Model Compression to Enhance Efficiency of Vision Transformers at the Edge.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ahmed_DeepCompress-ViT_Rethinking_Model_Compression_to_Enhance_Efficiency_of_Vision_Transformers_CVPR_2025_paper.html)
- **作者**: Sabbir Ahmed, Abdullah Al Arafat, Deniz Najafi, Akhlak Mahmood, Mamshad Nayeem Rizve, Mohaiminul Al Nahian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Efficient Test-time Adaptive Object Detection via Sensitivity-Guided Pruning.
- **链接**: [arXiv:2506.02462](https://arxiv.org/abs/2506.02462) · 📚 被引 4
- **作者**: Kunyu Wang, Xueyang Fu, Xin Lu, Chengjie Ge, Chengzhi Cao, Wei Zhai et al.
- **🏷️ 机构**: University of Science and Technology of China,School of Information Science and Technology and MoE Key Laboratory of Brain-Inspired Intelligent Perception and Cognition,Hefei,China,230026
- **会议**: CVPR 2025

### ConceptPrune: Concept Editing in Diffusion Models via Skilled Neuron Pruning.
- **链接**: [arXiv:2405.19237](https://arxiv.org/abs/2405.19237)
- **作者**: Ruchika Chavhan, Da Li, Timothy M. Hospedales
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual test-time adaptive object detection (CTTA-OD) aims to online adapt a source pre-trained detector to ever-changing environments during inference under continuous domain shifts. Most existing CTTA-OD methods prioritize effectiveness while overlooking computational efficiency, which is crucial for resource-constrained scenarios. In this paper, we propose an efficient CTTA-OD method via pruning. Our motivation stems from the observation that not all learned source features are beneficial; certain domain-sensitive feature channels can adversely affect target domain performance. Inspired by this, we introduce a sensitivity-guided channel pruning strategy that quantifies each channel based on its sensitivity to domain discrepancies at both image and instance levels. We apply weighted sparsity regularization to selectively suppress and prune these sensitive channels, focusing adaptation efforts on invariant ones. Additionally, we introduce a stochastic channel reactivation mechanism to restore pruned channels, enabling recovery of potentially useful features and mitigating the risks of early pruning. Extensive experiments on three benchmarks show that our method achieves superior adaptation performance while reducing computational overhead by 12% in FLOPs compared to the recent SOTA method.

</details>

### RENO: Real-Time Neural Compression for 3D LiDAR Point Clouds.
- **链接**: [arXiv:2503.12382](https://arxiv.org/abs/2503.12382) · [代码](https://github.com/NJUVISION/RENO) · 📚 被引 20
- **作者**: Kang You, Tong Chen, Dandan Ding, M. Salman Asif, Zhan Ma
- **🏷️ 机构**: Nanjing University, Hangzhou Normal University, University of California Riverside
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing AI-based point cloud compression methods struggle with dependence on specific training data distributions, which limits their real-world deployment. Implicit Neural Representation (INR) methods solve the above problem by encoding overfitted network parameters to the bitstream, resulting in more distribution-agnostic results. However, due to the limitation of encoding time and decoder size, current INR based methods only consider lossy geometry compression. In this paper, we propose the first INR based lossless point cloud geometry compression method called Lossless Implicit Neural Representations for Point Cloud Geometry Compression (LINR-PCGC). To accelerate encoding speed, we design a group of point clouds level coding framework with an effective network initialization strategy, which can reduce around 60% encoding time. A lightweight coding network based on multiscale SparseConv, consisting of scale context extraction, child node prediction, and model compression modules, is proposed to realize fast inference and compact decoder size. Experimental results show that our method consistently outperforms traditional and AI-based methods: for example, with the convergence time in the MVUB dataset, our method reduces the bitstream by approximately 21.21% compared to G-PCC TMC13v23 and 21.95% compared to SparsePCGC. Our project can be seen on https://huangwenjie2023.github.io/LINR-PCGC/.

</details>

### Generalized Gaussian Entropy Model for Point Cloud Attribute Compression with Dynamic Likelihood Intervals.
- **链接**: [arXiv:2506.09510](https://arxiv.org/abs/2506.09510) · 📚 被引 0
- **作者**: Changhao Peng
- **🏷️ 机构**: Peking University
- **会议**: CVPR 2025

### Keyframe-Oriented Vision Token Pruning: Enhancing Efficiency of Large Vision Language Models on Long-form Video Processing.
- **链接**: [arXiv:2503.10742](https://arxiv.org/abs/2503.10742) · 📚 被引 2
- **作者**: Yudong Liu, Jingwei Sun, Yueqian Lin, Jianyi Zhang, Jingyang Zhang, Ming Yin et al.
- **🏷️ 机构**: Duke University
- **会议**: ICCV 2025

### Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration.
- **链接**: [arXiv:2412.13180](https://arxiv.org/abs/2412.13180) · 📚 被引 1
- **作者**: Mark Endo, Xiaohan Wang, Serena Yeung-Levy
- **🏷️ 机构**: Stanford University,USA
- **会议**: ICCV 2025

</details>

### TopNet: Transformer-Efficient Occupancy Prediction Network for Octree-Structured Point Cloud Geometry Compression.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_TopNet_Transformer-Efficient_Occupancy_Prediction_Network_for_Octree-Structured_Point_Cloud_Geometry_CVPR_2025_paper.html)
- **作者**: Xinjie Wang, Yifan Zhang, Ting Liu, Xinpu Liu, Ke Xu, Jianwei Wan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

> In this paper, we propose MixA-Q, a mixed-precision activation quantization framework that leverages intra-layer activation sparsity (a concept widely explored in activation pruning methods) for efficient inference of quantized window-based vision transformers. For a given uniform-bit quantization configuration, MixA-Q separates the batched window computations within Swin blocks and assigns a lower bit width to the activations of less important windows, improving the trade-off between model performance and efficiency. We introduce a Two-Branch Swin Block that processes activations separately in high- and low-bit precision, enabling seamless integration of our method with most quantization-aware training (QAT) and post-training quantization (PTQ) methods, or with simple modifications. Our experimental evaluations over the COCO dataset demonstrate that MixA-Q achieves a training-free 1.35x computational speedup without accuracy loss in PTQ configuration. With QAT, MixA-Q achieves a lossless 1.25x speedup and a 1.53x speedup with only a 1% mAP drop by incorporating activation pruning. Notably, by reducing the quantization error in important regions, our sparsity-aware quantization adaptation improves the mAP of the quantized W4A4 model (with both weights and activations in 4-bit precision) by 0.7%, reducing quantization degradation by 24%.

</details>

### HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder.
- **链接**: [arXiv:2505.01938](https://arxiv.org/abs/2505.01938) · [代码](https://github.com/Qi-Yangsjtu/HybridGS)
- **作者**: Qi Yang, Le Yang, Geert Van der Auwera, Zhu Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce DC-AR, a novel masked autoregressive (AR) text-to-image generation framework that delivers superior image generation quality with exceptional computational efficiency. Due to the tokenizers' limitations, prior masked AR models have lagged behind diffusion models in terms of quality or efficiency. We overcome this limitation by introducing DC-HT - a deep compression hybrid tokenizer for AR models that achieves a 32x spatial compression ratio while maintaining high reconstruction fidelity and cross-resolution generalization ability. Building upon DC-HT, we extend MaskGIT and create a new hybrid masked autoregressive image generation framework that first produces the structural elements through discrete tokens and then applies refinements via residual tokens. DC-AR achieves state-of-the-art results with a gFID of 5.49 on MJHQ-30K and an overall score of 0.69 on GenEval, while offering 1.5-7.9x higher throughput and 2.0-3.5x lower latency compared to prior leading diffusion and autoregressive models.

</details>

### Privacy-Shielded Image Compression: Defending Against Exploitation from Vision-Language Pretrained Models.
- **链接**: [arXiv:2506.15201](https://arxiv.org/abs/2506.15201)
- **作者**: Xuelin Shen, Jiayin Xu, Kangsheng Yin, Wenhan Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Increasingly expensive training of ever larger models such as Vision Transfomers motivate reusing the vast library of already trained state-of-the-art networks. However, their latency, high computational costs and memory demands pose significant challenges for deployment, especially on resource-constrained hardware. While structured pruning methods can reduce these factors, they often require costly retraining, sometimes for up to hundreds of epochs, or even training from scratch to recover the lost accuracy resulting from the structural modifications. Maintaining the provided performance of trained models after structured pruning and thereby avoiding extensive retraining remains a challenge. To solve this, we introduce Variance-Based Pruning, a simple and structured one-shot pruning technique for efficiently compressing networks, with minimal finetuning. Our approach first gathers activation statistics, which are used to select neurons for pruning. Simultaneously the mean activations are integrated back into the model to preserve a high degree of performance. On ImageNet-1k recognition tasks, we demonstrate that directly after pruning DeiT-Base retains over 70% of its original performance and requires only 10 epochs of fine-tuning to regain 99% of the original accuracy while simultaneously reducing MACs by 35% and model size by 36%, thus speeding up the model by 1.44x. The code is available at: https://github.com/boschresearch/variance-based-pruning

</details>

### CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wang25eb.html)
- **作者**: Qinsi Wang, Hancheng Ye, Ming-Yu Chung, Yudong Liu, Yueqian Lin, Martin Kuo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Contradiction Retrieval via Contrastive Learning with Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xu25s.html)
- **作者**: Haike Xu, Zongyu Lin, Kai-Wei Chang, Yizhou Sun, Piotr Indyk
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding.
- **链接**: [出版页](https://proceedings.mlr.press/v267/shen25j.html)
- **作者**: Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Lemeng Wu, Jun Chen, Chenchen Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning.
- **链接**: [arXiv:2509.16105](https://arxiv.org/abs/2509.16105) · 📚 被引 0
- **作者**: Sikai Bai, Haoxi Li, Jie Zhang, Zicong Hong, Song Guo
- **🏷️ 机构**: The Hong Kong University of Science and Technology, EPFL
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the significant breakthrough of Mixture-of-Experts (MoE), the increasing scale of these MoE models presents huge memory and storage challenges. Existing MoE pruning methods, which involve reducing parameter size with a uniform sparsity across all layers, often lead to suboptimal outcomes and performance degradation due to varying expert redundancy in different MoE layers. To address this, we propose a non-uniform pruning strategy, dubbed \textbf{Di}fferentiable \textbf{E}xpert \textbf{P}runing (\textbf{DiEP}), which adaptively adjusts pruning rates at the layer level while jointly learning inter-layer importance, effectively capturing the varying redundancy across different MoE layers. By transforming the global discrete search space into a continuous one, our method handles exponentially growing non-uniform expert combinations, enabling adaptive gradient-based pruning. Extensive experiments on five advanced MoE models demonstrate the efficacy of our method across various NLP tasks. Notably, \textbf{DiEP} retains around 92\% of original performance on Mixtral 8$\times$7B with only half the experts, outperforming other pruning methods by up to 7.1\% on the challenging MMLU dataset.

</details>

### Activity Pruning for Efficient Spiking Neural Networks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/fa12d67b5939c37ea8a4659c31a08d2c-Abstract-Conference.html) · 📚 被引 0
- **作者**: Tong Bu, Xinyu Shi, Zhaofei Yu
- **🏷️ 机构**: Peking University
- **会议**: NeurIPS 2025

### Multi-Objective One-Shot Pruning for Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/84b5ca5e88590b07e277a77e88b68291-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weiyu Chen, Hansi Yang, Yunhao Gou, Han Shi, Enliang Hu, Zhenguo Li et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Hong Kong University of Science and Technology
- **会议**: NeurIPS 2025

### SCOPE: Saliency-Coverage Oriented Token Pruning for Efficient Multimodel LLMs.
- **链接**: [arXiv:2510.24214](https://arxiv.org/abs/2510.24214) · 📚 被引 0
- **作者**: Jinhong Deng, Wen Li, Joey Tianyi Zhou, Yang He
- **🏷️ 机构**: University of Electronic Science and Technology of China, Shanghai University of International Business and Economics, CFAR, A*STAR
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) typically process a large number of visual tokens, leading to considerable computational overhead, even though many of these tokens are redundant. Existing visual token pruning methods primarily focus on selecting the most salient tokens based on attention scores, resulting in the semantic incompleteness of the selected tokens. In this paper, we propose a novel visual token pruning strategy, called \textbf{S}aliency-\textbf{C}overage \textbf{O}riented token \textbf{P}runing for \textbf{E}fficient MLLMs (SCOPE), to jointly model both the saliency and coverage of the selected visual tokens to better preserve semantic completeness. Specifically, we introduce a set-coverage for a given set of selected tokens, computed based on the token relationships. We then define a token-coverage gain for each unselected token, quantifying how much additional coverage would be obtained by including it. By integrating the saliency score into the token-coverage gain, we propose our SCOPE score and iteratively select the token with the highest SCOPE score. We conduct extensive experiments on multiple vision-language understanding benchmarks using the LLaVA-1.5 and LLaVA-Next models. Experimental results demonstrate that our method consistently outperforms prior approaches. Our code is available at \href{https://github.com/kinredon/SCOPE}{https://github.com/kinredon/SCOPE}.

</details>

### Domain-Specific Pruning of Large Mixture-of-Experts Models with Few-shot Demonstrations.
- **链接**: [arXiv:2504.06792](https://arxiv.org/abs/2504.06792) · 📚 被引 0
- **作者**: Zican Dong, Han Peng, Peiyu Liu, Xin Zhao, Dong Wu, Feng Xiao et al.
- **🏷️ 机构**: Renmin University of China, University of International Business and Economics, Institute of Information Engineering, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixture-of-Experts (MoE) models achieve a favorable trade-off between performance and inference efficiency by activating only a subset of experts. However, the memory overhead of storing all experts remains a major limitation, especially in large-scale MoE models such as DeepSeek-R1(671B). In this study, we investigate domain specialization and expert redundancy in large-scale MoE models and uncover a consistent behavior we term few-shot expert localization, with only a few in-domain demonstrations, the model consistently activates a sparse and stable subset of experts on tasks within the same domain. Building on this observation, we propose a simple yet effective pruning framework, EASY-EP, that leverages a few domain-specific demonstrations to identify and retain only the most relevant experts. EASY-EP comprises two key components: output-aware expert importance assessment and expert-level token contribution estimation. The former evaluates the importance of each expert for the current token by considering the gating scores and L2 norm of the outputs of activated experts, while the latter assesses the contribution of tokens based on representation similarities before and after routed experts. Experiments on DeepSeek-R1 and DeepSeek-V3-0324 show that our method can achieve comparable performances and $2.99\times$ throughput under the same memory budget with full model with only half the experts.

</details>

### Backdoor Mitigation via Invertible Pruning Masks.
- **链接**: [arXiv:2509.15497](https://arxiv.org/abs/2509.15497) · 📚 被引 1
- **作者**: Kealan Dunnett, Reza Arablouei, Volkan Dedeoglu, Dimity Miller, Raja Jurdak
- **🏷️ 机构**: Queensland University of Technology and CSIRO Data61, CSIRO, Queensland University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model pruning has gained traction as a promising defense strategy against backdoor attacks in deep learning. However, existing pruning-based approaches often fall short in accurately identifying and removing the specific parameters responsible for inducing backdoor behaviors. Despite the dominance of fine-tuning-based defenses in recent literature, largely due to their superior performance, pruning remains a compelling alternative, offering greater interpretability and improved robustness in low-data regimes. In this paper, we propose a novel pruning approach featuring a learned \emph{selection} mechanism to identify parameters critical to both main and backdoor tasks, along with an \emph{invertible} pruning mask designed to simultaneously achieve two complementary goals: eliminating the backdoor task while preserving it through the inverse mask. We formulate this as a bi-level optimization problem that jointly learns selection variables, a sparse invertible mask, and sample-specific backdoor perturbations derived from clean data. The inner problem synthesizes candidate triggers using the inverse mask, while the outer problem refines the mask to suppress backdoor behavior without impairing clean-task accuracy. Extensive experiments demonstrate that our approach outperforms existing pruning-based backdoor mitigation approaches, maintains strong performance under limited data conditions, and achieves competitive results compared to state-of-the-art fine-tuning approaches. Notably, the proposed approach is particularly effective in restoring correct predictions for compromised samples after successful backdoor mitigation.

</details>

### DenoiseRotator: Enhance Pruning Robustness for LLMs via Importance Concentration.
- **链接**: [arXiv:2505.23049](https://arxiv.org/abs/2505.23049) · 📚 被引 0
- **作者**: Tianteng Gu, Bei Liu, Bo Xiao, Ke Zeng, Jiacheng Liu, Yanmin Qian
- **🏷️ 机构**: Shanghai Jiaotong University, Hong Kong University of Science and Technology, Meituan
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning is a widely used technique to compress large language models (LLMs) by removing unimportant weights, but it often suffers from significant performance degradation - especially under semi-structured sparsity constraints. Existing pruning methods primarily focus on estimating the importance of individual weights, which limits their ability to preserve critical capabilities of the model. In this work, we propose a new perspective: rather than merely selecting which weights to prune, we first redistribute parameter importance to make the model inherently more amenable to pruning. By minimizing the information entropy of normalized importance scores, our approach concentrates importance onto a smaller subset of weights, thereby enhancing pruning robustness. We instantiate this idea through DenoiseRotator, which applies learnable orthogonal transformations to the model's weight matrices. Our method can be seamlessly integrated with existing pruning techniques such as Magnitude, SparseGPT, and Wanda. Evaluated on LLaMA3, Qwen2.5, and Mistral models under 50% unstructured and 2:4 semi-structured sparsity, DenoiseRotator consistently improves perplexity and zero-shot accuracy. For instance, on LLaMA3-70B pruned with SparseGPT at 2:4 semi-structured sparsity, DenoiseRotator reduces the perplexity gap to the dense model by 58%, narrowing the degradation from 8.1 to 3.4 points. Codes are available at https://github.com/Axel-gu/DenoiseRotator.

</details>

### Learning to Focus: Causal Attention Distillation via Gradient-Guided Token Pruning.
- **链接**: [arXiv:2506.07851](https://arxiv.org/abs/2506.07851) · 📚 被引 0
- **作者**: Yiju Guo, Wenkai Yang, Zexu Sun, Ning Ding, Zhiyuan Liu, Yankai Lin
- **🏷️ 机构**: Renmin University of China, Tsinghua University, Tsinghua University, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have demonstrated significant improvements in contextual understanding. However, their ability to attend to truly critical information during long-context reasoning and generation still falls behind the pace. Specifically, our preliminary experiments reveal that certain distracting patterns can misdirect the model's attention during inference, and removing these patterns substantially improves reasoning accuracy and generation quality. We attribute this phenomenon to spurious correlations in the training data, which obstruct the model's capacity to infer authentic causal instruction-response relationships. This phenomenon may induce redundant reasoning processes, potentially resulting in significant inference overhead and, more critically, the generation of erroneous or suboptimal responses. To mitigate this, we introduce a two-stage framework called Learning to Focus (LeaF) leveraging intervention-based inference to disentangle confounding factors. In the first stage, LeaF employs gradient-based comparisons with an advanced teacher to automatically identify confounding tokens based on causal relationships in the training corpus. Then, in the second stage, it prunes these tokens during distillation to enact intervention, aligning the student's attention with the teacher's focus distribution on truly critical context tokens. Experimental results demonstrate that LeaF not only achieves an absolute improvement in various mathematical reasoning, code generation and multi-hop question answering benchmarks but also effectively suppresses attention to confounding tokens during inference, yielding a more interpretable and reliable reasoning model.

</details>

### FedRTS: Federated Robust Pruning via Combinatorial Thompson Sampling.
- **链接**: [arXiv:2501.19122](https://arxiv.org/abs/2501.19122) · 📚 被引 0
- **作者**: Hong Huang, Jinhai Yang, Yuan Chen, Jiaxun Ye, Dapeng Wu
- **🏷️ 机构**: City University of Hong Kong, University of Florida
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated Learning (FL) enables collaborative model training across distributed clients without data sharing, but its high computational and communication demands strain resource-constrained devices. While existing methods use dynamic pruning to improve efficiency by periodically adjusting sparse model topologies while maintaining sparsity, these approaches suffer from issues such as greedy adjustments, unstable topologies, and communication inefficiency, resulting in less robust models and suboptimal performance under data heterogeneity and partial client availability. To address these challenges, we propose Federated Robust pruning via combinatorial Thompson Sampling (FedRTS), a novel framework designed to develop robust sparse models. FedRTS enhances robustness and performance through its Thompson Sampling-based Adjustment (TSAdj) mechanism, which uses probabilistic decisions informed by stable, farsighted information instead of deterministic decisions reliant on unstable and myopic information in previous methods. Extensive experiments demonstrate that FedRTS achieves state-of-the-art performance in computer vision and natural language processing tasks while reducing communication costs, particularly excelling in scenarios with heterogeneous data distributions and partial client participation. Our codes are available at: https://github.com/Little0o0/FedRTS

</details>

### Discovering Important Experts for Mixture-of-Experts Models Pruning Through a Theoretical Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/c66a9db149261435664284a20b6f1d42-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weizhong Huang, Yuxin Zhang, Xiawu Zheng, Fei Chao, Rongrong Ji, Liujuan Cao
- **🏷️ 机构**: Xiamen University, Aberystwyth University, Xiamen University, China
- **会议**: NeurIPS 2025

### MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference.
- **链接**: [arXiv:2505.22913](https://arxiv.org/abs/2505.22913) · 📚 被引 1
- **作者**: Donghyeon Joo, Helya Hosseini, Ramyad Hadidi, Bahar Asgari
- **🏷️ 机构**: University of Maryland, College Park, Department of Computer Science, University of Maryland, College Park, d-Matrix
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We demonstrate that unstructured sparsity significantly improves KV cache compression for LLMs, enabling sparsity levels up to 70% without compromising accuracy or requiring fine-tuning. We conduct a systematic exploration of pruning strategies and find per-token magnitude-based pruning as highly effective for both Key and Value caches under unstructured sparsity, surpassing prior structured pruning schemes. The Key cache benefits from prominent outlier elements, while the Value cache surprisingly benefits from a simple magnitude-based pruning despite its uniform distribution. KV cache size is the major bottleneck in decode performance due to high memory overhead for large context lengths. To address this, we use a bitmap-based sparse format and a custom attention kernel capable of compressing and directly computing over compressed caches pruned to arbitrary sparsity patterns, significantly accelerating memory-bound operations in decode computations and thereby compensating for the overhead of runtime pruning and compression. Our custom attention kernel coupled with the bitmap-based format delivers substantial compression of KV cache upto 45% of dense inference and thereby enables longer context length and increased tokens/sec throughput of upto 2.23x compared to dense inference. Our pruning mechanism and sparse attention kernel is available at https://github.com/dhjoo98/mustafar.

</details>

### Týr-the-Pruner: Structural Pruning LLMs via Global Sparsity Distribution Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/db2cbf43a349bc866111e791b58c7bf4-Abstract-Conference.html) · 📚 被引 0
- **作者**: Guanchen Li, Yixing Xu, Zeping Li, Ji Liu, Xuanwu Yin, Dong Li et al.
- **🏷️ 机构**: Advanced Micro Devices, AMD, University of Science and Technology of China
- **会议**: NeurIPS 2025

### Why 1 + 1 < 1 in Visual Token Pruning: Beyond Naive Integration via Multi-Objective Balanced Covering.
- **链接**: [arXiv:2505.10118](https://arxiv.org/abs/2505.10118) · 📚 被引 0
- **作者**: Yangfu Li, Hongjian Zhan, Tianyi Chen, Qi Liu, Yu-Jie Xiong, Yue Lu
- **🏷️ 机构**: East China Normal University, Shanghai Jiaotong University, Peking University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing visual token pruning methods target prompt alignment and visual preservation with static strategies, overlooking the varying relative importance of these objectives across tasks, which leads to inconsistent performance. To address this, we derive the first closed-form error bound for visual token pruning based on the Hausdorff distance, uniformly characterizing the contributions of both objectives. Moreover, leveraging $ε$-covering theory, we reveal an intrinsic trade-off between these objectives and quantify their optimal attainment levels under a fixed budget. To practically handle this trade-off, we propose Multi-Objective Balanced Covering (MoB), which reformulates visual token pruning as a bi-objective covering problem. In this framework, the attainment trade-off reduces to budget allocation via greedy radius trading. MoB offers a provable performance bound and linear scalability with respect to the number of input visual tokens, enabling adaptation to challenging pruning scenarios. Extensive experiments show that MoB preserves 96.4% of performance for LLaVA-1.5-7B using only 11.1% of the original visual tokens and accelerates LLaVA-Next-7B by 1.3-1.5$\times$ with negligible performance loss. Additionally, evaluations on Qwen2-VL and Video-LLaVA confirm that MoB integrates seamlessly into advanced MLLMs and diverse vision-language tasks.

</details>

### Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/ad2f57116d62a9d8dcfaba6a168715e4-Abstract-Conference.html) · 📚 被引 1
- **作者**: Chaofan Lin, Jiaming Tang, Shuo Yang, Hanshuo Wang, Tian Tang, Boyu Tian et al.
- **🏷️ 机构**: Tsinghua University, Massachusetts Institute of Technology, Harbin Institute of Technology (Shenzhen)
- **会议**: NeurIPS 2025

### Pruning-Robust Mamba with Asymmetric Multi-Scale Scanning Paths.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a5e7816971fa6fee513b4980edbf254e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jindi Lv, Yuhao Zhou, Mingjia Shi, Zhiyuan Liang, Panpan Zhang, Xiaojiang Peng et al.
- **🏷️ 机构**: sichuan university, Sichuan University, University of Virginia
- **会议**: NeurIPS 2025

### The Graphon Limit Hypothesis: Understanding Neural Network Pruning via Infinite Width Analysis.
- **链接**: [arXiv:2510.17515](https://arxiv.org/abs/2510.17515) · 📚 被引 0
- **作者**: Hoang Pham, The Anh Ta, Tom Jacobs, Rebekka Burkholz, Long Tran-Thanh
- **🏷️ 机构**: University of Warwick, CSIRO's Data61, CISPA Helmholtz Center
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse neural networks promise efficiency, yet training them effectively remains a fundamental challenge. Despite advances in pruning methods that create sparse architectures, understanding why some sparse structures are better trainable than others with the same level of sparsity remains poorly understood. Aiming to develop a systematic approach to this fundamental problem, we propose a novel theoretical framework based on the theory of graph limits, particularly graphons, that characterizes sparse neural networks in the infinite-width regime. Our key insight is that connectivity patterns of sparse neural networks induced by pruning methods converge to specific graphons as networks' width tends to infinity, which encodes implicit structural biases of different pruning methods. We postulate the Graphon Limit Hypothesis and provide empirical evidence to support it. Leveraging this graphon representation, we derive a Graphon Neural Tangent Kernel (Graphon NTK) to study the training dynamics of sparse networks in the infinite width limit. Graphon NTK provides a general framework for the theoretical analysis of sparse networks. We empirically show that the spectral analysis of Graphon NTK correlates with observed training dynamics of sparse networks, explaining the varying convergence behaviours of different pruning methods. Our framework provides theoretical insights into the impact of connectivity patterns on the trainability of various sparse network architectures.

</details>

### FastVID: Dynamic Density Pruning for Fast Video Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b2e63e36c57e153b9015fece2352a9f9-Abstract-Conference.html)
- **作者**: Leqi Shen, Guoqiang Gong, Tao He, Yifeng Zhang, Pengzhang Liu, Sicheng Zhao et al.
- **🏷️ 机构**: NUS
- **会议**: NeurIPS 2025

### ReplaceMe: Network Simplification via Depth Pruning and Transformer Block Linearization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1c10d0c087c14689628124bbc8fa69f6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dmitriy Shopkhoev, Ammar Ali, Magauiya Zhussip, Valentin Malykh, Stamatios Lefkimmiatis, Nikos Komodakis et al.
- **🏷️ 机构**: MTS AI, Moscow Institute of Physics and Technology, Ecole des Ponts ParisTech
- **会议**: NeurIPS 2025

### Efficient Hybrid Language Model Compression through Group-Aware SSM Pruning.
- **链接**: [arXiv:2504.11409](https://arxiv.org/abs/2504.11409) · 📚 被引 0
- **作者**: Ali Taghibakhshi, Sharath Turuvekere Sreenivas, Saurav Muralidharan, Marcin Chochowski, Yashaswi Karnati, Raviraj Joshi et al.
- **🏷️ 机构**: NVIDIA, Department of Computer Science, Indian Institute of Technology, Madras, Indian Institute of Technology, Madras
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hybrid LLM architectures that combine Attention and State Space Models (SSMs) achieve state-of-the-art accuracy and runtime performance. Recent work has demonstrated that applying compression and distillation to Attention-only models yields smaller, more accurate models at a fraction of the training cost. In this work, we explore the effectiveness of compressing Hybrid architectures. We introduce a novel group-aware pruning strategy that preserves the structural integrity of SSM blocks and their sequence modeling capabilities. Furthermore, we demonstrate the necessity of such SSM pruning to achieve improved accuracy and inference speed compared to traditional approaches. Our compression recipe combines SSM, FFN, embedding dimension, and layer pruning, followed by knowledge distillation-based retraining, similar to the MINITRON technique. Using this approach, we compress the Nemotron-H 8B Hybrid model down to 4B parameters with up to 40x fewer training tokens. The resulting model surpasses the accuracy of similarly-sized models while achieving 2x faster inference, significantly advancing the Pareto frontier.

</details>

### Each Complexity Deserves a Pruning Policy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/ab4ccdc1fd3d09c5841bda2a7e6bd783-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hanshi Wang, Yuhao Xu, Zekun Xu, Jin Gao, Yufan Liu, Weiming Hu et al.
- **🏷️ 机构**: Institute of automation, Chinese academy of science, Sichuan University, Institute of automation, Chinese academy of science, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### FlowPrune: Accelerating Attention Flow Calculation by Pruning Flow Network.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/c2cd7fa98591516c025d7632b2586ca1-Abstract-Conference.html) · 📚 被引 0
- **作者**: Shuo Xu, Yu Chen, Shuxia Lin, Xin Geng, Xu Yang
- **🏷️ 机构**: University of Maryland, College Park, Shanghai Jiaotong University, Southeast University
- **会议**: NeurIPS 2025

### Attribution-Driven Adaptive Token Pruning for Transformers.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4b9d42d1105cd1e4fb64ab96a1f4b8b6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yaoyao Yan, Hui Yu, Weizhi Xu
- **🏷️ 机构**: Shandong Normal University
- **会议**: NeurIPS 2025

### ALTER: All-in-One Layer Pruning and Temporal Expert Routing for Efficient Diffusion Generation.
- **链接**: [arXiv:2505.21817](https://arxiv.org/abs/2505.21817) · 📚 被引 0
- **作者**: Xiaomeng Yang, Lei Lu, Qihui Fan, Changdi Yang, Juyi Lin, Yanzhi Wang et al.
- **🏷️ 机构**: Northeastern University, Carnegie Mellon University, Florida State University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models have demonstrated exceptional capabilities in generating high-fidelity images. However, their iterative denoising process results in significant computational overhead during inference, limiting their practical deployment in resource-constrained environments. Existing acceleration methods often adopt uniform strategies that fail to capture the temporal variations during diffusion generation, while the commonly adopted sequential pruning-then-fine-tuning strategy suffers from sub-optimality due to the misalignment between pruning decisions made on pretrained weights and the model's final parameters. To address these limitations, we introduce ALTER: All-in-One Layer Pruning and Temporal Expert Routing, a unified framework that transforms diffusion models into a mixture of efficient temporal experts. ALTER achieves a single-stage optimization that unifies layer pruning, expert routing, and model fine-tuning by employing a trainable hypernetwork, which dynamically generates layer pruning decisions and manages timestep routing to specialized, pruned expert sub-networks throughout the ongoing fine-tuning of the UNet. This unified co-optimization strategy enables significant efficiency gains while preserving high generative quality. Specifically, ALTER achieves same-level visual fidelity to the original 50-step Stable Diffusion v2.1 model while utilizing only 25.9% of its total MACs with just 20 inference steps and delivering a 3.64x speedup through 35% sparsity.

</details>

### Pruning Spurious Subgraphs for Graph Out-of-Distribution Generalization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/336825d7395fd78f081c124be6ace2e0-Abstract-Conference.html) · 📚 被引 0
- **作者**: Tianjun Yao, Haoxuan Li, Yongqiang Chen, Tongliang Liu, Le Song, Eric P. Xing et al.
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence, Peking University, MBZUAI/CMU
- **会议**: NeurIPS 2025

### DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs.
- **链接**: [arXiv:2506.20194](https://arxiv.org/abs/2506.20194) · 📚 被引 0
- **作者**: Ruokai Yin, Yuhang Li, Donghyun Lee, Priyadarshini Panda
- **🏷️ 机构**: Yale University, University of Southern California
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) deliver strong performance but are difficult to deploy due to high memory and compute costs. While pruning reduces these demands, most methods ignore activation sparsity observed at runtime. We reinterpret activation sparsity as dynamic structured weight sparsity and propose DuoGPT, a unified framework that constructs dual-sparse (spMspV) workloads by combining unstructured weight pruning with activation sparsity. To preserve accuracy, we extend the Optimal Brain Compression (OBC) framework with activation-aware calibration and introduce output residuals from the dense model as correction terms. We further optimize the solution for efficient GPU execution, enabling scalability to billion-parameter LLMs. Evaluations on LLaMA-2 and LLaMA-3 show that DuoGPT outperforms state-of-the-art structured pruning methods by up to 9.17% accuracy at an iso-speedup of 1.39$\times$ compared to the baseline dense model. Code is available at Github.

</details>

### Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs.
- **链接**: [arXiv:2506.10967](https://arxiv.org/abs/2506.10967) · 📚 被引 0
- **作者**: Qizhe Zhang, Mengzhen Liu, Lichen Li, Ming Lu, Yuan Zhang, Junwen Pan et al.
- **🏷️ 机构**: Peking University, Intel Labs China, Communication University of China
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In multimodal large language models (MLLMs), the length of input visual tokens is often significantly greater than that of their textual counterparts, leading to a high inference cost. Many works aim to address this issue by removing redundant visual tokens. However, current approaches either rely on attention-based pruning, which retains numerous duplicate tokens, or use similarity-based pruning, overlooking the instruction relevance, consequently causing suboptimal performance. In this paper, we go beyond attention or similarity by proposing a novel visual token pruning method named CDPruner, which maximizes the conditional diversity of retained tokens. We first define the conditional similarity between visual tokens conditioned on the instruction, and then reformulate the token pruning problem with determinantal point process (DPP) to maximize the conditional diversity of the selected subset. The proposed CDPruner is training-free and model-agnostic, allowing easy application to various MLLMs. Extensive experiments across diverse MLLMs show that CDPruner establishes new state-of-the-art on various vision-language benchmarks. By maximizing conditional diversity through DPP, the selected subset better represents the input images while closely adhering to user instructions, thereby preserving strong performance even with high reduction ratios. When applied to LLaVA, CDPruner reduces FLOPs by 95\% and CUDA latency by 78\%, while maintaining 94\% of the original accuracy. Our code is available at https://github.com/Theia-4869/CDPruner.

</details>

### Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning.
- **链接**: [arXiv:2505.23195](https://arxiv.org/abs/2505.23195) · 📚 被引 1
- **作者**: Lifan Zhao, Yanyan Shen, Zhaoyang Liu, Xue Wang, Jiaji Deng
- **🏷️ 机构**: Shanghai Jiao Tong University, meituan, Alibaba Group
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling laws motivate the development of Time Series Foundation Models (TSFMs) that pre-train vast parameters and achieve remarkable zero-shot forecasting performance. Surprisingly, even after fine-tuning, TSFMs cannot consistently outperform smaller, specialized models trained on full-shot downstream data. A key question is how to realize effective adaptation of TSFMs for a target forecasting task. Through empirical studies on various TSFMs, the pre-trained models often exhibit inherent sparsity and redundancy in computation, suggesting that TSFMs have learned to activate task-relevant network substructures to accommodate diverse forecasting tasks. To preserve this valuable prior knowledge, we propose a structured pruning method to regularize the subsequent fine-tuning process by focusing it on a more relevant and compact parameter space. Extensive experiments on seven TSFMs and six benchmarks demonstrate that fine-tuning a smaller, pruned TSFM significantly improves forecasting performance compared to fine-tuning original models. This prune-then-finetune paradigm often enables TSFMs to achieve state-of-the-art performance and surpass strong specialized baselines. Source code is made publicly available at https://github.com/SJTU-DMTai/Prune-then-Finetune.

</details>

### Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity.
- **链接**: [arXiv:2505.14884](https://arxiv.org/abs/2505.14884) · 📚 被引 0
- **作者**: Susav Shrestha, Bradley W. Settlemyer, Nikoli Dryden, Narasimha Reddy
- **🏷️ 机构**: Texas A&amp;M University - College Station, NVIDIA, Lawrence Livermore National Labs
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accelerating large language model (LLM) inference is critical for real-world deployments requiring high throughput and low latency. Contextual sparsity, where each token dynamically activates only a small subset of the model parameters, shows promise but does not scale to large batch sizes due to union of active neurons quickly approaching dense computation. We introduce Polar Sparsity, highlighting a key shift in sparsity importance from MLP to Attention layers as we scale batch size and sequence length. While MLP layers become more compute-efficient under batching, their sparsity vanishes. In contrast, attention becomes increasingly more expensive at scale, while their head sparsity remains stable and batch-invariant. We develop Selective Head Attention with hardware-efficient, sparsity-aware GPU kernels, delivering up to \(2.2\times\) end-to-end speedups for models like OPT, LLaMA-2 \& 3, Qwen, Mistral across various batch sizes and sequence lengths without compromising accuracy. To our knowledge, this is the first work to demonstrate that contextual sparsity can scale effectively to large batch sizes, delivering substantial inference acceleration with minimal changes, making Polar Sparsity practical for large-scale, high-throughput LLM deployment systems. Our code is available at: https://github.com/susavlsh10/Polar-Sparsity.

</details>

### Bivariate Matrix-valued Linear Regression (BMLR): Finite-sample performance under Identifiability and Sparsity Assumptions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1403d0b949e4dab6fb3aec92ee8bbc9b-Abstract-Conference.html) · 📚 被引 0
- **作者**: Nayel Bettache
- **🏷️ 机构**: Capital Fund Management
- **会议**: NeurIPS 2025

### The Price of Sparsity: Sufficient Conditions for Sparse Recovery using Sparse and Sparsified Measurements.
- **链接**: [arXiv:2509.01809](https://arxiv.org/abs/2509.01809) · 📚 被引 0
- **作者**: Youssef Chaabouni, David Gamarnik
- **🏷️ 机构**: Massachusetts Institute of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of recovering the support of a sparse signal using noisy projections. While extensive work has been done on the dense measurement matrix setting, the sparse setting remains less explored. In this work, we establish sufficient conditions on the sample size for successful sparse recovery using sparse measurement matrices. Bringing together our result with previously known necessary conditions, we discover that, in the regime where $ds/p \rightarrow +\infty$, sparse recovery in the sparse setting exhibits a phase transition at an information-theoretic threshold of $n_{\text{INF}}^{\text{SP}} = Θ\left(s\log\left(p/s\right)/\log\left(ds/p\right)\right)$, where $p$ denotes the signal dimension, $s$ the number of non-zero components of the signal, and $d$ the expected number of non-zero components per row of measurement. This expression makes the price of sparsity explicit: restricting each measurement to $d$ non-zeros inflates the required sample size by a factor of $\log{s}/\log\left(ds/p\right)$, revealing a precise trade-off between sampling complexity and measurement sparsity. Additionally, we examine the effect of sparsifying an originally dense measurement matrix on sparse signal recovery. We prove in the regime of $s = αp$ and $d = ψp$ with $α, ψ\in \left(0,1\right)$ and $ψ$ small that a sample of size $n^{\text{Sp-ified}}_{\text{INF}} = Θ\left(p / ψ^2\right)$ is sufficient for recovery, subject to a certain uniform integrability conjecture, the proof of which is work in progress.

</details>

### Bilevel Network Learning via Hierarchically Structured Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7b8fecab2dfd40e80c51c3fcf6675914-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jiayi Fan, Jingyuan Yang, Shuangge Ma, Mengyun Wu
- **🏷️ 机构**: Shanghai University of Finance and Economics, Yale University
- **会议**: NeurIPS 2025

### Price of Parsimony: Complexity of Fourier Sparsity Testing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f17376c941d5882050e2e366bb74dffa-Abstract-Conference.html) · 📚 被引 0
- **作者**: Arijit Ghosh, Manmatha Roy
- **🏷️ 机构**: Indian Statistical Institute, Indian Statistical Institute, Kolkata
- **会议**: NeurIPS 2025

### Differentiable Sparsity via $D$-Gating: Simple and Versatile Structured Penalization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/dea9b4b6f55ae611c54065d6fc750755-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chris Kolb, Laetitia Frost, Bernd Bischl, David Rügamer
- **🏷️ 机构**: LMU Munich (Germany), University of Munich, Ludwig-Maximilians-Universität München, LMU
- **会议**: NeurIPS 2025

### FPSAttention: Training-Aware FP8 and Sparsity Co-Design for Fast Video Diffusion.
- **链接**: [arXiv:2506.04648](https://arxiv.org/abs/2506.04648) · 📚 被引 0
- **作者**: Akide Liu, Zeyu Zhang, Zhexin Li, Xuehai Bai, Yuanjie Xing, Yizeng Han et al.
- **🏷️ 机构**: Monash University, Renmin University of China, Alibaba Group
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion generative models have become the standard for producing high-quality, coherent video content, yet their slow inference speeds and high computational demands hinder practical deployment. Although both quantization and sparsity can independently accelerate inference while maintaining generation quality, naively combining these techniques in existing training-free approaches leads to significant performance degradation due to the lack of joint optimization. We introduce FPSAttention, a novel training-aware co-design of FP8 quantization and sparsity for video generation, with a focus on the 3D bi-directional attention mechanism. Our approach features three key innovations: 1) A unified 3D tile-wise granularity that simultaneously supports both quantization and sparsity; 2) A denoising step-aware strategy that adapts to the noise schedule, addressing the strong correlation between quantization/sparsity errors and denoising steps; 3) A native, hardware-friendly kernel that leverages FlashAttention and is implemented with optimized Hopper architecture features for highly efficient execution. Trained on Wan2.1's 1.3B and 14B models and evaluated on the VBench benchmark, FPSAttention achieves a 7.09x kernel speedup for attention operations and a 4.96x end-to-end speedup for video generation compared to the BF16 baseline at 720p resolution-without sacrificing generation quality.

</details>

### Lua-LLM: Learning Unstructured-Sparsity Allocation for Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b2c39fe6ce838440faf03a0f780e7a63-Abstract-Conference.html) · 📚 被引 0
- **作者**: Mingge Lu, Jingwei Sun, Junqing Lin, Zechun Zhou, Guangzhong Sun
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: NeurIPS 2025

### Overcoming Sparsity Artifacts in Crosscoders to Interpret Chat-Tuning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9902a53031ebbbab73898028073d4790-Abstract-Conference.html) · 📚 被引 1
- **作者**: Julian Minder, Clément Dumas, Caden Juang, Bilal Chughtai, Neel Nanda
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free.
- **链接**: [arXiv:2505.06708](https://arxiv.org/abs/2505.06708) · 📚 被引 7
- **作者**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang et al.
- **🏷️ 机构**: Qwen Team, Georgia Institute of Technology, Alibaba Inc.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual Autoregressive (VAR) modeling has gained popularity for its shift towards next-scale prediction. However, existing VAR paradigms process the entire token map at each scale step, leading to the complexity and runtime scaling dramatically with image resolution. To address this challenge, we propose FastVAR, a post-training acceleration method for efficient resolution scaling with VARs. Our key finding is that the majority of latency arises from the large-scale step where most tokens have already converged. Leveraging this observation, we develop the cached token pruning strategy that only forwards pivotal tokens for scale-specific modeling while using cached tokens from previous scale steps to restore the pruned slots. This significantly reduces the number of forwarded tokens and improves the efficiency at larger resolutions. Experiments show the proposed FastVAR can further speedup FlashAttention-accelerated VAR by 2.7$\times$ with negligible performance drop of <1%. We further extend FastVAR to zero-shot generation of higher resolution images. In particular, FastVAR can generate one 2K image with 15GB memory footprints in 1.5s on a single NVIDIA 3090 GPU. Code is available at https://github.com/csguoh/FastVAR.

</details>

### Exploiting Dynamic Sparsity in Einsum.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7feb98f84ee34f697944333d4faec0bd-Abstract-Conference.html) · 📚 被引 0
- **作者**: Christoph Staudt, Mark Blacher, Tim Hoffmann, Lea Kasche, Olaf Beyersdorff, Joachim Giesen
- **🏷️ 机构**: Friedrich-Schiller Universität Jena, University of Jena, Friedrich-Schiller-Universitat Jena
- **会议**: NeurIPS 2025

### Spark Transformer: Reactivating Sparsity in Transformer FFN and Attention.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/220d26c7fb478c2a397bd3fef0fe1d6f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chong You, Kan Wu, Zhipeng Jia, Lin Chen, Srinadh Bhojanapalli, Jiaxian Guo et al.
- **🏷️ 机构**: Google, SystemsResearch@Google, University of Science and Technology of China
- **会议**: NeurIPS 2025

### FlashMo: Geometric Interpolants and Frequency-Aware Sparsity for Scalable Efficient Motion Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/306264db5698839230be3642aafc849c-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zeyu Zhang, Yiran Wang, Danning Li, Dong Gong, Ian Reid, Richard Hartley
- **🏷️ 机构**: Renmin University of China, University of Sydney, University of Sydney, McGill University
- **会议**: NeurIPS 2025

### One-Step Diffusion-Based Image Compression with Semantic Distillation.
- **链接**: [arXiv:2505.16687](https://arxiv.org/abs/2505.16687) · 📚 被引 1
- **作者**: Naifu Xue, Zhaoyang Jia, Jiahao Li, Bin Li, Yuan Zhang, Yan Lu
- **🏷️ 机构**: Communication University of China, University of Science and Technology of China, Microsoft Research Asia
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models are renowned for their generative capabilities, yet their pretraining processes exhibit distinct phases of learning speed that have been entirely overlooked in prior post-training acceleration efforts in the community. In this study, we introduce a novel framework called MosaicDiff that aligns diffusion pretraining dynamics with post-training sampling acceleration via trajectory-aware structural pruning. Our approach leverages the observation that the middle, fast-learning stage of diffusion pretraining requires more conservative pruning to preserve critical model features, while the early and later, slow-learning stages benefit from a more aggressive pruning strategy. This adaptive pruning mechanism is the first to explicitly mirror the inherent learning speed variations of diffusion pretraining, thereby harmonizing the model's inner training dynamics with its accelerated sampling process. Extensive experiments on DiT and SDXL demonstrate that our method achieves significant speed-ups in sampling without compromising output quality, outperforming previous state-of-the-art methods by large margins, also providing a new viewpoint for more efficient and robust training-free diffusion acceleration.

</details>

## 跨领域论文（完整笔记在其他领域）

### ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.html)
- **作者**: Xubing Ye, Yukang Gan, Yixiao Ge, Xiao-Ping Zhang, Yansong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### VoCo-LLaMA: Towards Vision Compression with Large Language Models.
- **链接**: [arXiv:2406.12275](https://arxiv.org/abs/2406.12275) · 📚 被引 20
- **作者**: Xubing Ye, Yukang Gan, Xiaoke Huang, Yixiao Ge, Yansong Tang
- **🏷️ 机构**: Tsinghua University,Tsinghua Shenzhen International Graduate School, Tencent PCG,ARC Lab, UC Santa Cruz
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have achieved remarkable success in various multi-modal tasks, but they are often bottlenecked by the limited context window and high computational cost of processing high-resolution image inputs and videos. Vision compression can alleviate this problem by reducing the vision token count. Previous approaches compress vision tokens with external modules and force LLMs to understand the compressed ones, leading to visual information loss. However, the LLMs' understanding paradigm of vision tokens is not fully utilised in the compression learning process. We propose VoCo-LLaMA, the first approach to compress vision tokens using LLMs. By introducing Vision Compression tokens during the vision instruction tuning phase and leveraging attention distillation, our method distill how LLMs comprehend vision tokens into their processing of VoCo tokens. VoCo-LLaMA facilitates effective vision compression and improves the computational efficiency during the inference stage. Specifically, our method achieves minimal performance loss with a compression ratio of 576$\times$, resulting in up to 94.8$\%$ fewer FLOPs and 69.6$\%$ acceleration in inference time. Furthermore, through continuous training using time-series compressed token sequences of video frames, VoCo-LLaMA demonstrates the ability to understand temporal correlations, outperforming previous methods on popular video question-answering benchmarks. Our approach presents a promising way to unlock the full potential of VLMs' contextual window, enabling more scalable multi-modal applications. The project page, along with the associated code, can be accessed via https://yxxxb.github.io/VoCo-LLaMA-page/.

</details>

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

> Vision language models (VLMs) demonstrate strong capabilities in jointly processing visual and textual data. However, they often incur substantial computational overhead due to redundant visual information, particularly in long-form video scenarios. Existing approaches predominantly focus on either vision token pruning, which may overlook spatio-temporal dependencies, or keyframe selection, which identifies informative frames but discards others, thus disrupting contextual continuity. In this work, we propose KVTP (Keyframe-oriented Vision Token Pruning), a novel framework that overcomes the drawbacks of token pruning and keyframe selection. By adaptively assigning pruning rates based on frame relevance to the query, KVTP effectively retains essential contextual information while significantly reducing redundant computation. To thoroughly evaluate the long-form video understanding capacities of VLMs, we curated and reorganized subsets from VideoMME, EgoSchema, and NextQA into a unified benchmark named SparseKV-QA that highlights real-world scenarios with sparse but crucial events. Our experiments with VLMs of various scales show that KVTP can reduce token usage by 80% without compromising spatiotemporal and contextual consistency, significantly cutting computation while maintaining the performance. These results demonstrate our approach's effectiveness in efficient long-video processing, facilitating more scalable VLM deployment.

</details>

### SURGEON: Memory-Adaptive Fully Test-Time Adaptation via Dynamic Activation Sparsity.
- **链接**: [arXiv:2503.20354](https://arxiv.org/abs/2503.20354) · 📚 被引 3
- **作者**: Ke Ma, Jiaqi Tang, Bin Guo, Fan Dang, Sicong Liu, Zhui Zhu et al.
- **🏷️ 机构**: Northwestern Polytechnical University, The Hong Kong University of Science and Technology, Beijing Jiaotong University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision encoders serve as the cornerstone of multimodal understanding. Single-encoder architectures like CLIP exhibit inherent constraints in generalizing across diverse multimodal tasks, while recent multi-encoder fusion methods introduce prohibitive computational overhead to achieve superior performance using complementary visual representations from multiple vision encoders. To address this, we propose a progressive pruning framework, namely Multi-Encoder collaboraTivE tOken pRuning (METEOR), that eliminates redundant visual tokens across the encoding, fusion, and decoding stages for multi-encoder MLLMs. For multi-vision encoding, we discard redundant tokens within each encoder via a rank guided collaborative token assignment strategy. Subsequently, for multi-vision fusion, we combine the visual features from different encoders while reducing cross-encoder redundancy with cooperative pruning. Finally, we propose an adaptive token pruning method in the LLM decoding stage to further discard irrelevant tokens based on the text prompts with dynamically adjusting pruning ratios for specific task demands. To our best knowledge, this is the first successful attempt that achieves an efficient multi-encoder based vision language model with multi-stage pruning strategies. Extensive experiments on 11 benchmarks demonstrate the effectiveness of our proposed approach. Compared with EAGLE, a typical multi-encoder MLLMs, METEOR reduces 76% visual tokens with only 0.3% performance drop in average. The code is available at https://github.com/YuchenLiu98/METEOR.

</details>

### Random Conditioning for Diffusion Model Compression with Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kim_Random_Conditioning_for_Diffusion_Model_Compression_with_Distillation_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Dohyun Kim, Sehwan Park, Geonhee Han, Seung Wook Kim, Paul Hongsuck Seo
- **🏷️ 机构**: Korea University,Dept. of CSE, NVIDIA
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models. → [multimodal](../multimodal/Guideline%202025.md)
- CASP: Compression of Large Multimodal Models Based on Attention Sparsity. → [multimodal](../multimodal/Guideline%202025.md)
- FlashSloth : Lightning Multimodal Large Language Models via Embedded Visual Compression. → [multimodal](../multimodal/Guideline%202025.md)
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding. → [3d-detection](../3d-detection/Guideline%202025.md)

## 🆕 增量新增

### PVC: Progressive Visual Token Compression for Unified Image and Video Processing in Large Vision-Language Models. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2412.09613](https://arxiv.org/abs/2412.09613) · 📚 被引 3
- **作者**: Chenyu Yang, Xuan Dong, Xizhou Zhu, Weijie Su, Jiahao Wang, Hao Tian et al.
- **🏷️ 机构**: Tsinghua University, Shanghai AI Laboratory,OpenGVLab, SenseTime Research
- **会议**: CVPR 2025
- **摘要（中）**: 针对图像和视频处理中视觉token压缩策略不统一的问题，本文提出渐进式视觉token压缩（PVC）方法，将图像扩展为静态视频，并采用统一压缩策略，逐帧渐进编码和自适应压缩，利用时间冗余高效压缩视频token。图像通过重复帧补充空间细节，PVC以每帧64个token的有限数量保留空间和时间信息。实验表明，该模型在多种视频理解任务上达到最先进性能，统一了图像和视频处理。
- **摘要（英）**: This paper proposes Progressive Visual Token Compression (PVC) to unify image and video processing in VLMs, extending images as static videos and progressively compressing tokens. It exploits temporal redundancy for videos and spatial details for images, with limited tokens per frame. Experiments show state-of-the-art performance across video understanding tasks, unifying token compression.
- **核心贡献**: 提出PVC方法，统一图像和视频的视觉token压缩。
- **创新点**: 通过渐进编码和自适应压缩，在有限token下保留时空细节。
- **结果**: 在视频理解任务上取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (VLMs) have been extended to understand both images and videos. Visual token compression is leveraged to reduce the considerable token length of visual inputs. To meet the needs of different tasks, existing high-performance models usually process images and videos separately with different token compression strategies, limiting the capabilities of combining images and videos. To this end, we extend each image into a "static" video and introduce a unified token compression strategy called Progressive Visual Token Compression (PVC), where the tokens of each frame are progressively encoded and adaptively compressed to supplement the information not extracted from previous frames. Video tokens are efficiently compressed with exploiting the inherent temporal redundancy. Images are repeated as static videos, and the spatial details can be gradually supplemented in multiple frames. PVC unifies the token compressing of images and videos. With a limited number of tokens per frame (64 tokens by default), spatial details and temporal changes can still be preserved. Experiments show that our model achieves state-of-the-art performance across various video understanding benchmarks, including long video tasks and fine-grained short video tasks. Meanwhile, our unified token compression strategy incurs no performance loss on image benchmarks, particularly in detail-sensitive tasks.

</details>

### Libra-Merging: Importance-redundancy and Pruning-merging Trade-off for Acceleration Plug-in in Large Vision-Language Model. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Libra-Merging_Importance-redundancy_and_Pruning-merging_Trade-off_for_Acceleration_Plug-in_in_Large_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Longrong Yang, Dong Shen, Chaoxiang Cai, Kaibing Chen, Fan Yang, Tingting Gao et al.
- **🏷️ 机构**: Zhejiang University,College of Computer Science and Technology, Kuaishou Technology, Zhejiang University,School of Software Technology
- **会议**: CVPR 2025
- **摘要（中）**: ①针对大型视觉语言模型（LVLM）推理加速问题，现有token剪枝方法未充分考虑重要性-冗余度权衡及剪枝与合并的协同。②提出Libra-Merging方法，作为加速插件，结合重要性评估、冗余度分析与剪枝-合并策略，动态减少视觉token。③相比已有工作，创新性地将剪枝与合并统一优化，平衡信息保留与计算效率。④实验表明在保持性能的同时显著降低计算开销，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses inference acceleration for large vision-language models by proposing Libra-Merging, a plug-in method that integrates importance-redundancy analysis with pruning-merging trade-offs. It dynamically reduces visual tokens while balancing information retention and efficiency, outperforming prior token pruning approaches. Experimental results show notable computational savings with minimal performance loss, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出剪枝与合并协同的加速插件，优化视觉token处理。
- **创新点**: 将重要性-冗余度权衡与剪枝-合并策略结合。
- **结果**: 在保持性能的同时降低计算开销。

### DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2503.02175](https://arxiv.org/abs/2503.02175) · 📚 被引 14
- **作者**: Saeed Ranjbar Alvar, Gursimran Singh, Mohammad Akbari, Yong Zhang
- **🏷️ 机构**: Huawei Technologies Canada Co., Ltd.
- **会议**: CVPR 2025
- **摘要（中）**: ①针对大型多模态模型（LMM）中视觉token数量庞大导致推理延迟高的问题，现有剪枝方法依赖次优重要性指标或需大量校准。②提出DivPrune，将token剪枝形式化为最大最小多样性问题（MMDP），选择多样性最高的子集。③相比已有工作，直接最大化所选token的多样性，减少冗余。④实验表明在保持性能的同时降低冗余，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses high inference latency in LMMs by proposing DivPrune, which formulates token pruning as a Max-Min Diversity Problem to select a diverse subset. It reduces redundancy among retained tokens without extensive calibration. Results show improved diversity and efficiency, though specific metrics are not detailed.
- **核心贡献**: 提出基于多样性最大化的视觉token剪枝方法。
- **创新点**: 将token剪枝建模为MMDP问题。
- **结果**: 降低冗余并保持性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) have emerged as powerful models capable of understanding various data modalities, including text, images, and videos. LMMs encode both text and visual data into tokens that are then combined and processed by an integrated Large Language Model (LLM). Including visual tokens substantially increases the total token count, often by thousands. The increased input length for LLM significantly raises the complexity of inference, resulting in high latency in LMMs. To address this issue, token pruning methods, which remove part of the visual tokens, are proposed. The existing token pruning methods either require extensive calibration and fine-tuning or rely on suboptimal importance metrics which results in increased redundancy among the retained tokens. In this paper, we first formulate token pruning as Max-Min Diversity Problem (MMDP) where the goal is to select a subset such that the diversity among the selected {tokens} is maximized. Then, we solve the MMDP to obtain the selected subset and prune the rest. The proposed method, DivPrune, reduces redundancy and achieves the highest diversity of the selected tokens. By ensuring high diversity, the selected tokens better represent the original tokens, enabling effective performance even at high pruning ratios without requiring fine-tuning. Extensive experiments with various LMMs show that DivPrune achieves state-of-the-art accuracy over 16 image- and video-language datasets. Additionally, DivPrune reduces both the end-to-end latency and GPU memory usage for the tested models. The code is available $\href{https://github.com/vbdi/divprune}{\text{here}}$.

</details>

### CASP: Compression of Large Multimodal Models Based on Attention Sparsity. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2503.05936](https://arxiv.org/abs/2503.05936) · 📚 被引 2
- **作者**: Mohsen Gholami, Mohammad Akbari, Kevin Cannons, Yong Zhang
- **🏷️ 机构**: Huawei Technologies Canada Co., Ltd.
- **会议**: CVPR 2025
- **摘要（中）**: 针对大型多模态模型（LMMs）低比特压缩未被充分探索的问题，论文提出CASP压缩技术。该方法基于注意力矩阵稀疏性，对Query和Key权重矩阵进行数据感知的低秩分解，并通过最优比特分配进行全层量化。相比已有量化方法，CASP可兼容任意量化技术，并在2-bit量化方法（AQLM和QuIP#）基础上平均提升21%的图像和视频语言基准性能。
- **摘要（英）**: Addressing the under-explored low-bit compression for Large Multimodal Models (LMMs), this paper proposes CASP, which leverages attention sparsity to perform data-aware low-rank decomposition on Query and Key matrices followed by optimal bit allocation quantization. It enhances state-of-the-art 2-bit quantization methods by an average of 21% on image- and video-language benchmarks.
- **核心贡献**: 提出基于注意力稀疏性的LMMs压缩方法CASP。
- **创新点**: 利用注意力矩阵稀疏性约束压缩误差，实现低秩分解与量化结合。
- **结果**: 在2-bit量化方法上平均提升21%基准性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we propose an extreme compression technique for Large Multimodal Models (LMMs). While previous studies have explored quantization as an efficient post-training compression method for Large Language Models (LLMs), low-bit compression for multimodal models remains under-explored. The redundant nature of inputs in multimodal models results in a highly sparse attention matrix. We theoretically and experimentally demonstrate that the attention matrix's sparsity bounds the compression error of the Query and Key weight matrices. Based on this, we introduce CASP, a model compression technique for LMMs. Our approach performs a data-aware low-rank decomposition on the Query and Key weight matrix, followed by quantization across all layers based on an optimal bit allocation process. CASP is compatible with any quantization technique and enhances state-of-the-art 2-bit quantization methods (AQLM and QuIP#) by an average of 21% on image- and video-language benchmarks.

</details>

### LLaVA-ST: A Multimodal Large Language Model for Fine-Grained Spatial-Temporal Understanding. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2501.08282](https://arxiv.org/abs/2501.08282) · 📚 被引 15
- **作者**: Hongyu Li, Jinyu Chen, Ziyu Wei, Shaofei Huang, Tianrui Hui, Jialin Gao et al.
- **🏷️ 机构**: Beihang University,School of Artificial Intelligence, Hefei University of Technology,School of Computer Science and Information Engineering, Meituan
- **会议**: CVPR 2025
- **摘要（中）**: 针对多模态大语言模型难以同时处理时空定位的问题，论文提出LLaVA-ST。该方法引入语言对齐位置嵌入，将文本坐标特殊标记嵌入视觉空间，简化细粒度时空对应关系对齐；并设计时空打包器，将时空分辨率特征压缩解耦为两个点-区域注意力流。此外，构建了包含430万训练样本的ST-Align数据集。该方法有效提升了细粒度时空多模态理解能力。
- **摘要（英）**: To address the challenge of simultaneous temporal and spatial localization in MLLMs, this paper proposes LLaVA-ST with Language-Aligned Positional Embedding and Spatial-Temporal Packer, decoupling feature compression into two attention streams. It also introduces the ST-Align dataset with 4.3M samples, improving fine-grained spatial-temporal understanding.
- **核心贡献**: 提出LLaVA-ST模型及ST-Align数据集，解决细粒度时空理解问题。
- **创新点**: 语言对齐位置嵌入和时空解耦压缩机制。
- **结果**: 在细粒度时空理解任务上取得显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in multimodal large language models (MLLMs) have shown promising results, yet existing approaches struggle to effectively handle both temporal and spatial localization simultaneously. This challenge stems from two key issues: first, incorporating spatial-temporal localization introduces a vast number of coordinate combinations, complicating the alignment of linguistic and visual coordinate representations; second, encoding fine-grained temporal and spatial information during video feature compression is inherently difficult. To address these issues, we propose LLaVA-ST, a MLLM for fine-grained spatial-temporal multimodal understanding. In LLaVA-ST, we propose Language-Aligned Positional Embedding, which embeds the textual coordinate special token into the visual space, simplifying the alignment of fine-grained spatial-temporal correspondences. Additionally, we design the Spatial-Temporal Packer, which decouples the feature compression of temporal and spatial resolutions into two distinct point-to-region attention processing streams. Furthermore, we propose ST-Align dataset with 4.3M training samples for fine-grained spatial-temporal multimodal understanding. With ST-align, we present a progressive training pipeline that aligns the visual and textual feature through sequential coarse-to-fine stages.Additionally, we introduce an ST-Align benchmark to evaluate spatial-temporal interleaved fine-grained understanding tasks, which include Spatial-Temporal Video Grounding (STVG) , Event Localization and Captioning (ELC) and Spatial Video Grounding (SVG). LLaVA-ST achieves outstanding performance on 11 benchmarks requiring fine-grained temporal, spatial, or spatial-temporal interleaving multimodal understanding. Our code, data and benchmark will be released at Our code, data and benchmark will be released at https://github.com/appletea233/LLaVA-ST .

</details>

### FlashSloth : Lightning Multimodal Large Language Models via Embedded Visual Compression. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tong_FlashSloth__Lightning_Multimodal_Large_Language_Models_via_Embedded_Visual_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Bo Tong, Bokai Lai, Yiyi Zhou, Gen Luo, Yunhang Shen, Ke Li et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,P.R. China,361005, Shanghai AI Laboratory,OpenGVLab, Tencent,Youtu Lab,P.R. China
- **会议**: CVPR 2025
- **摘要（中）**: 论文标题为FlashSloth，旨在通过嵌入式视觉压缩实现闪电般快速的多模态大语言模型。但摘要为空，无法获取具体方法、改进点和效果信息。
- **摘要（英）**: The paper proposes FlashSloth for lightning-fast MLLMs via embedded visual compression, but the abstract is empty, lacking details on methodology and results.
- **核心贡献**: 提出嵌入式视觉压缩方法加速多模态模型。
- **创新点**: 嵌入式视觉压缩技术。
- **结果**: 未知。

### Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding.
- **链接**: [arXiv:2502.10392](https://arxiv.org/abs/2502.10392) · 📚 被引 5
- **作者**: Wenxuan Guo, Xiuwei Xu, Ziwei Wang, Jianjiang Feng, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University, Nanyang Technological University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose an efficient multi-level convolution architecture for 3D visual grounding. Conventional methods are difficult to meet the requirements of real-time inference due to the two-stage or point-based architecture. Inspired by the success of multi-level fully sparse convolutional architecture in 3D object detection, we aim to build a new 3D visual grounding framework following this technical route. However, as in 3D visual grounding task the 3D scene representation should be deeply interacted with text features, sparse convolution-based architecture is inefficient for this interaction due to the large amount of voxel features. To this end, we propose text-guided pruning (TGP) and completion-based addition (CBA) to deeply fuse 3D scene representation and text features in an efficient way by gradual region pruning and target completion. Specifically, TGP iteratively sparsifies the 3D scene representation and thus efficiently interacts the voxel features with text features by cross-attention. To mitigate the affect of pruning on delicate geometric information, CBA adaptively fixes the over-pruned region by voxel completion with negligible computational overhead. Compared with previous single-stage methods, our method achieves top inference speed and surpasses previous fastest method by 100\% FPS. Our method also achieves state-of-the-art accuracy even compared with two-stage methods, with $+1.13$ lead of Acc@0.5 on ScanRefer, and $+2.6$ and $+3.2$ leads on NR3D and SR3D respectively. The code is available at \href{https://github.com/GWxuan/TSP3D}{https://github.com/GWxuan/TSP3D}.

</details>

### Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning.
- **链接**: [arXiv:2503.08101](https://arxiv.org/abs/2503.08101) · 📚 被引 1
- **作者**: Lizhen Xu, Xiuxiu Bai, Xiaojun Jia, Jianwu Fang, Shanmin Pang
- **🏷️ 机构**: Xi&#x0027;an Jiaotong University,China, Nanyang Technological University,Singapore
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Query-based methods with dense features have demonstrated remarkable success in 3D object detection tasks. However, the computational demands of these models, particularly with large image sizes and multiple transformer layers, pose significant challenges for efficient running on edge devices. Existing pruning and distillation methods either need retraining or are designed for ViT models, which are hard to migrate to 3D detectors. To address this issue, we propose a zero-shot runtime pruning method for transformer decoders in 3D object detection models. The method, termed tgGBC (trim keys gradually Guided By Classification scores), systematically trims keys in transformer modules based on their importance. We expand the classification score to multiply it with the attention map to get the importance score of each key and then prune certain keys after each transformer layer according to their importance scores. Our method achieves a 1.99x speedup in the transformer decoder of the latest ToC3D model, with only a minimal performance loss of less than 1%. Interestingly, for certain models, our method even enhances their performance. Moreover, we deploy 3D detectors with tgGBC on an edge device, further validating the effectiveness of our method. The code can be found at https://github.com/iseri27/tg_gbc.

</details>

### LINR-PCGC: Lossless Implicit Neural Representations for Point Cloud Geometry Compression.
- **链接**: [arXiv:2507.15686](https://arxiv.org/abs/2507.15686) · 📚 被引 1
- **作者**: Wenjie Huang, Qi Yang, Shuting Xia, He Huang, Yiling Xu, Zhu Li
- **🏷️ 机构**: Shanghai Jiao Tong University, University of Missouri-Kansas City
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing AI-based point cloud compression methods struggle with dependence on specific training data distributions, which limits their real-world deployment. Implicit Neural Representation (INR) methods solve the above problem by encoding overfitted network parameters to the bitstream, resulting in more distribution-agnostic results. However, due to the limitation of encoding time and decoder size, current INR based methods only consider lossy geometry compression. In this paper, we propose the first INR based lossless point cloud geometry compression method called Lossless Implicit Neural Representations for Point Cloud Geometry Compression (LINR-PCGC). To accelerate encoding speed, we design a group of point clouds level coding framework with an effective network initialization strategy, which can reduce around 60% encoding time. A lightweight coding network based on multiscale SparseConv, consisting of scale context extraction, child node prediction, and model compression modules, is proposed to realize fast inference and compact decoder size. Experimental results show that our method consistently outperforms traditional and AI-based methods: for example, with the convergence time in the MVUB dataset, our method reduces the bitstream by approximately 21.21% compared to G-PCC TMC13v23 and 21.95% compared to SparsePCGC. Our project can be seen on https://huangwenjie2023.github.io/LINR-PCGC/.

</details>

### General Compression Framework for Efficient Transformer Object Tracking.
- **链接**: [arXiv:2409.17564](https://arxiv.org/abs/2409.17564) · 📚 被引 3
- **作者**: Lingyi Hong, Jinglun Li, Xinyu Zhou, Shilin Yan, Pinxue Guo, Kaixun Jiang et al.
- **🏷️ 机构**: College of Computer Science and Artificial Intelligence, Fudan University,Shanghai Key Lab of Intelligent Information Processing,China, College of Intelligent Robotics and Advanced Manufacturing, Fudan University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous works have attempted to improve tracking efficiency through lightweight architecture design or knowledge distillation from teacher models to compact student trackers. However, these solutions often sacrifice accuracy for speed to a great extent, and also have the problems of complex training process and structural limitations. Thus, we propose a general model compression framework for efficient transformer object tracking, named CompressTracker, to reduce model size while preserving tracking accuracy. Our approach features a novel stage division strategy that segments the transformer layers of the teacher model into distinct stages to break the limitation of model structure. Additionally, we also design a unique replacement training technique that randomly substitutes specific stages in the student model with those from the teacher model, as opposed to training the student model in isolation. Replacement training enhances the student model's ability to replicate the teacher model's behavior and simplifies the training process. To further forcing student model to emulate teacher model, we incorporate prediction guidance and stage-wise feature mimicking to provide additional supervision during the teacher model's compression process. CompressTracker is structurally agnostic, making it compatible with any transformer architecture. We conduct a series of experiment to verify the effectiveness and generalizability of our CompressTracker. Our CompressTracker-SUTrack, compressed from SUTrack, retains about 99 performance on LaSOT (72.2 AUC) while achieves 2.42x speed up. Code is available at https://github.com/LingyiHongfd/CompressTracker.

</details>

### LLaVA-Prumerge: Adaptive Token Reduction for Efficient Large Multimodal Models.
- **链接**: [arXiv:2403.15388](https://arxiv.org/abs/2403.15388) · 📚 被引 19
- **作者**: Yuzhang Shang, Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan
- **🏷️ 机构**: UCF, UW-Madison, Illinois Tech
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) have shown significant visual reasoning capabilities by connecting a visual encoder and a large language model. LMMs typically take in a fixed and large amount of visual tokens, such as the penultimate layer features in the CLIP visual encoder, as the prefix content. Recent LMMs incorporate more complex visual inputs, such as high-resolution images and videos, which further increases the number of visual tokens significantly. However, due to the inherent design of the Transformer architecture, the computational costs of these models tend to increase quadratically with the number of input tokens. To tackle this problem, we explore a token reduction mechanism that identifies significant spatial redundancy among visual tokens. In response, we propose PruMerge, a novel adaptive visual token reduction strategy that significantly reduces the number of visual tokens without compromising the performance of LMMs. Specifically, to metric the importance of each token, we exploit the sparsity observed in the visual encoder, characterized by the sparse distribution of attention scores between the class token and visual tokens. This sparsity enables us to dynamically select the most crucial visual tokens to retain. Subsequently, we cluster the selected (unpruned) tokens based on their key similarity and merge them with the unpruned tokens, effectively supplementing and enhancing their informational content. Empirically, when applied to LLaVA-1.5, our approach can compress the visual tokens by 14 times on average, and achieve comparable performance across diverse visual question-answering and reasoning tasks. Code and checkpoints are at https://llava-prumerge.github.io/.

</details>

### Mixa-Q: Revisiting Activation Sparsity for Vision Transformers From a Mixed-Precision Quantization Perspective.
- **链接**: [arXiv:2507.19131](https://arxiv.org/abs/2507.19131) · 📚 被引 2
- **作者**: Weitian Wang, Shubham Rai, Cecilia De la Parra, Akash Kumar
- **🏷️ 机构**: Robert Bosch GmbH,Renningen,Germany
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose MixA-Q, a mixed-precision activation quantization framework that leverages intra-layer activation sparsity (a concept widely explored in activation pruning methods) for efficient inference of quantized window-based vision transformers. For a given uniform-bit quantization configuration, MixA-Q separates the batched window computations within Swin blocks and assigns a lower bit width to the activations of less important windows, improving the trade-off between model performance and efficiency. We introduce a Two-Branch Swin Block that processes activations separately in high- and low-bit precision, enabling seamless integration of our method with most quantization-aware training (QAT) and post-training quantization (PTQ) methods, or with simple modifications. Our experimental evaluations over the COCO dataset demonstrate that MixA-Q achieves a training-free 1.35x computational speedup without accuracy loss in PTQ configuration. With QAT, MixA-Q achieves a lossless 1.25x speedup and a 1.53x speedup with only a 1% mAP drop by incorporating activation pruning. Notably, by reducing the quantization error in important regions, our sparsity-aware quantization adaptation improves the mAP of the quantized W4A4 model (with both weights and activations in 4-bit precision) by 0.7%, reducing quantization degradation by 24%.

</details>

### Cross-Granularity Online Optimization with Masked Compensated Information for Learned Image Compression.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01533) · 📚 被引 1
- **作者**: Haowei Kuang, Wenhan Yang, Zongming Guo, Jiaying Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China, Pengcheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

### DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer.
- **链接**: [arXiv:2507.04947](https://arxiv.org/abs/2507.04947) · 📚 被引 1
- **作者**: Yecheng Wu, Junyu Chen, Zhuoyang Zhang, Enze Xie, Jincheng Yu, Junsong Chen et al.
- **🏷️ 机构**: MIT NVIDIA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce DC-AR, a novel masked autoregressive (AR) text-to-image generation framework that delivers superior image generation quality with exceptional computational efficiency. Due to the tokenizers' limitations, prior masked AR models have lagged behind diffusion models in terms of quality or efficiency. We overcome this limitation by introducing DC-HT - a deep compression hybrid tokenizer for AR models that achieves a 32x spatial compression ratio while maintaining high reconstruction fidelity and cross-resolution generalization ability. Building upon DC-HT, we extend MaskGIT and create a new hybrid masked autoregressive image generation framework that first produces the structural elements through discrete tokens and then applies refinements via residual tokens. DC-AR achieves state-of-the-art results with a gFID of 5.49 on MJHQ-30K and an overall score of 0.69 on GenEval, while offering 1.5-7.9x higher throughput and 2.0-3.5x lower latency compared to prior leading diffusion and autoregressive models.

</details>

### Variance-Based Pruning for Accelerating and Compressing Trained Networks.
- **链接**: [arXiv:2507.12988](https://arxiv.org/abs/2507.12988) · 📚 被引 2
- **作者**: Uranik Berisha, Jens Mehnert, Alexandru Paul Condurache
- **🏷️ 机构**: GmbH,Automated Driving Research, Robert Bosch,Stuttgart,Germany,70469
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Increasingly expensive training of ever larger models such as Vision Transfomers motivate reusing the vast library of already trained state-of-the-art networks. However, their latency, high computational costs and memory demands pose significant challenges for deployment, especially on resource-constrained hardware. While structured pruning methods can reduce these factors, they often require costly retraining, sometimes for up to hundreds of epochs, or even training from scratch to recover the lost accuracy resulting from the structural modifications. Maintaining the provided performance of trained models after structured pruning and thereby avoiding extensive retraining remains a challenge. To solve this, we introduce Variance-Based Pruning, a simple and structured one-shot pruning technique for efficiently compressing networks, with minimal finetuning. Our approach first gathers activation statistics, which are used to select neurons for pruning. Simultaneously the mean activations are integrated back into the model to preserve a high degree of performance. On ImageNet-1k recognition tasks, we demonstrate that directly after pruning DeiT-Base retains over 70% of its original performance and requires only 10 epochs of fine-tuning to regain 99% of the original accuracy while simultaneously reducing MACs by 35% and model size by 36%, thus speeding up the model by 1.44x. The code is available at: https://github.com/boschresearch/variance-based-pruning

</details>

### FastVAR: Linear Visual Autoregressive Modeling Via Cached Token Pruning.
- **链接**: [arXiv:2503.23367](https://arxiv.org/abs/2503.23367) · 📚 被引 2
- **作者**: Hang Guo, Yawei Li, Taolin Zhang, Jiangshan Wang, Tao Dai, Shu-Tao Xia et al.
- **🏷️ 机构**: Tsinghua University, ETH Zurich, Shenzhen University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual Autoregressive (VAR) modeling has gained popularity for its shift towards next-scale prediction. However, existing VAR paradigms process the entire token map at each scale step, leading to the complexity and runtime scaling dramatically with image resolution. To address this challenge, we propose FastVAR, a post-training acceleration method for efficient resolution scaling with VARs. Our key finding is that the majority of latency arises from the large-scale step where most tokens have already converged. Leveraging this observation, we develop the cached token pruning strategy that only forwards pivotal tokens for scale-specific modeling while using cached tokens from previous scale steps to restore the pruned slots. This significantly reduces the number of forwarded tokens and improves the efficiency at larger resolutions. Experiments show the proposed FastVAR can further speedup FlashAttention-accelerated VAR by 2.7$\times$ with negligible performance drop of <1%. We further extend FastVAR to zero-shot generation of higher resolution images. In particular, FastVAR can generate one 2K image with 15GB memory footprints in 1.5s on a single NVIDIA 3090 GPU. Code is available at https://github.com/csguoh/FastVAR.

</details>

### MosaicDiff: Training-free Structural Pruning for Diffusion Model Acceleration Reflecting Pretraining Dynamics.
- **链接**: [arXiv:2510.11962](https://arxiv.org/abs/2510.11962) · 📚 被引 1
- **作者**: Bowei Guo, Shengkun Tang, Cong Zeng, Zhiqiang Shen
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models are renowned for their generative capabilities, yet their pretraining processes exhibit distinct phases of learning speed that have been entirely overlooked in prior post-training acceleration efforts in the community. In this study, we introduce a novel framework called MosaicDiff that aligns diffusion pretraining dynamics with post-training sampling acceleration via trajectory-aware structural pruning. Our approach leverages the observation that the middle, fast-learning stage of diffusion pretraining requires more conservative pruning to preserve critical model features, while the early and later, slow-learning stages benefit from a more aggressive pruning strategy. This adaptive pruning mechanism is the first to explicitly mirror the inherent learning speed variations of diffusion pretraining, thereby harmonizing the model's inner training dynamics with its accelerated sampling process. Extensive experiments on DiT and SDXL demonstrate that our method achieves significant speed-ups in sampling without compromising output quality, outperforming previous state-of-the-art methods by large margins, also providing a new viewpoint for more efficient and robust training-free diffusion acceleration.

</details>

### METEOR: Multi-Encoder Collaborative Token Pruning for Efficient Vision Language Models.
- **链接**: [arXiv:2507.20842](https://arxiv.org/abs/2507.20842)
- **作者**: Yuchen Liu, Yaoming Wang, Bowen Shi, Xiaopeng Zhang, Wenrui Dai, Chenglin Li et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,China, Meituan Inc.,China, Huawei Inc.,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision encoders serve as the cornerstone of multimodal understanding. Single-encoder architectures like CLIP exhibit inherent constraints in generalizing across diverse multimodal tasks, while recent multi-encoder fusion methods introduce prohibitive computational overhead to achieve superior performance using complementary visual representations from multiple vision encoders. To address this, we propose a progressive pruning framework, namely Multi-Encoder collaboraTivE tOken pRuning (METEOR), that eliminates redundant visual tokens across the encoding, fusion, and decoding stages for multi-encoder MLLMs. For multi-vision encoding, we discard redundant tokens within each encoder via a rank guided collaborative token assignment strategy. Subsequently, for multi-vision fusion, we combine the visual features from different encoders while reducing cross-encoder redundancy with cooperative pruning. Finally, we propose an adaptive token pruning method in the LLM decoding stage to further discard irrelevant tokens based on the text prompts with dynamically adjusting pruning ratios for specific task demands. To our best knowledge, this is the first successful attempt that achieves an efficient multi-encoder based vision language model with multi-stage pruning strategies. Extensive experiments on 11 benchmarks demonstrate the effectiveness of our proposed approach. Compared with EAGLE, a typical multi-encoder MLLMs, METEOR reduces 76% visual tokens with only 0.3% performance drop in average. The code is available at https://github.com/YuchenLiu98/METEOR.

</details>

### WINS: Winograd Structured Pruning for Fast Winograd Convolution.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02087)
- **作者**: Cheonjun Park, Hyun Jae Oh, Mincheol Park, Hyunchan Moon, Minsik Kim, Suhyun Kim et al.
- **🏷️ 机构**: Hankuk University of Foreign Studies, Yonsei University, Samsung Advanced Institute of Technology
- **会议**: ICCV 2025

### MOBIUS: Big-to-Mobile Universal Instance Segmentation via Multi-modal Bottleneck Fusion and Calibrated Decoder Pruning.
- **链接**: [arXiv:2510.15026](https://arxiv.org/abs/2510.15026)
- **作者**: Mattia Segù, Marta Tintore Gazulla, Yongqin Xian, Luc Van Gool, Federico Tombari
- **🏷️ 机构**: Google, Sofia University,INSAIT
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling up model size and training data has advanced foundation models for instance-level perception, achieving state-of-the-art in-domain and zero-shot performance across object detection and segmentation. However, their high computational cost limits adoption on resource-constrained platforms. We first examine the limitations of existing architectures in enabling efficient edge deployment without compromising performance. We then introduce MOBIUS, a family of foundation models for universal instance segmentation, designed for Pareto-optimal downscaling to support deployment across devices ranging from high-end accelerators to mobile hardware. To reduce training and inference demands, we propose: (i) a bottleneck pixel decoder for efficient multi-scale and multi-modal fusion, (ii) a language-guided uncertainty calibration loss for adaptive decoder pruning, and (iii) a streamlined, unified training strategy. Unlike efficient baselines that trade accuracy for reduced complexity, MOBIUS reduces pixel and transformer decoder FLOPs by up to 55% and 75%, respectively, while maintaining state-of-the-art performance in just a third of the training iterations. MOBIUS establishes a new benchmark for efficient segmentation on both high-performance computing platforms and mobile devices.

</details>

### Pruning All-Rounder: Rethinking and Improving Inference Efficiency for Large Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01883)
- **作者**: Wei Suo, Ji Ma, Mengyang Sun, Lin Yuanbo Wu, Peng Wang, Yanning Zhang
- **🏷️ 机构**: Northwestern Polytechnical University,China, Swansea University,United Kingdom
- **会议**: ICCV 2025

### Partial Forward Blocking: A Novel Data Pruning Paradigm for Lossless Training Acceleration.
- **链接**: [arXiv:2506.23674](https://arxiv.org/abs/2506.23674) · 📚 被引 1
- **作者**: Dongyue Wu, Zilin Guo, Jialong Zuo, Nong Sang, Changxin Gao
- **🏷️ 机构**: School of Artifcial Intelligence and Automation, Huazhong University of Science and Technology,National Key Laboratory of Multispectral Information Intelligent Processing Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ever-growing size of training datasets enhances the generalization capability of modern machine learning models but also incurs exorbitant computational costs. Existing data pruning approaches aim to accelerate training by removing those less important samples. However, they often rely on gradients or proxy models, leading to prohibitive additional costs of gradient back-propagation and proxy model training. In this paper, we propose Partial Forward Blocking (PFB), a novel framework for lossless training acceleration. The efficiency of PFB stems from its unique adaptive pruning pipeline: sample importance is assessed based on features extracted from the shallow layers of the target model. Less important samples are then pruned, allowing only the retained ones to proceed with the subsequent forward pass and loss back-propagation. This mechanism significantly reduces the computational overhead of deep-layer forward passes and back-propagation for pruned samples, while also eliminating the need for auxiliary backward computations and proxy model training. Moreover, PFB introduces probability density as an indicator of sample importance. Combined with an adaptive distribution estimation module, our method dynamically prioritizes relatively rare samples, aligning with the constantly evolving training state. Extensive experiments demonstrate the significant superiority of PFB in performance and speed. On ImageNet, PFB achieves a 0.5% accuracy improvement and 33% training time reduction with 40% data pruned.

</details>

### VFLowOpt: A Token Pruning Framework for LMMs with Visual Information Flow-Guided Optimization.
- **链接**: [arXiv:2508.05211](https://arxiv.org/abs/2508.05211) · 📚 被引 1
- **作者**: Sihan Yang, Runsen Xu, Chenhang Cui, Tai Wang, Dahua Lin, Jiangmiao Pang
- **🏷️ 机构**: Shanghai AI Laboratory, National University of Singapore
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) excel in visual-language tasks by leveraging numerous visual tokens for fine-grained visual information, but this token redundancy results in significant computational costs. Previous research aimed at reducing visual tokens during inference typically leverages importance maps derived from attention scores among vision-only tokens or vision-language tokens to prune tokens across one or multiple pruning stages. Despite this progress, pruning frameworks and strategies remain simplistic and insufficiently explored, often resulting in substantial performance degradation. In this paper, we propose VFlowOpt, a token pruning framework that introduces an importance map derivation process and a progressive pruning module with a recycling mechanism. The hyperparameters of its pruning strategy are further optimized by a visual information flow-guided method. Specifically, we compute an importance map for image tokens based on their attention-derived context relevance and patch-level information entropy. We then decide which tokens to retain or prune and aggregate the pruned ones as recycled tokens to avoid potential information loss. Finally, we apply a visual information flow-guided method that regards the last token in the LMM as the most representative signal of text-visual interactions. This method minimizes the discrepancy between token representations in LMMs with and without pruning, thereby enabling superior pruning strategies tailored to different LMMs. Experiments demonstrate that VFlowOpt can prune 90% of visual tokens while maintaining comparable performance, leading to an 89% reduction in KV-Cache memory and 3.8 times faster inference.

</details>

### Beyond Text-Visual Attention: Exploiting Visual Cues for Effective Token Pruning in VLMs.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01939) · 📚 被引 6
- **作者**: Qizhe Zhang, Aosong Cheng, Ming Lu, Renrui Zhang, Zhiyong Zhuo, Jiajun Cao et al.
- **🏷️ 机构**: School of Computer Science, Peking University,State Key Laboratory for Multimedia Information Processing, CUHK MMLab, ByteDance
- **会议**: ICCV 2025

### AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning.
- **链接**: [arXiv:2412.03248](https://arxiv.org/abs/2412.03248) · 📚 被引 2
- **作者**: Yiwu Zhong, Zhuoming Liu, Yin Li, Liwei Wang
- **🏷️ 机构**: The Chinese University of Hong Kong, University of Wisconsin-Madison
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have enabled the creation of multi-modal LLMs that exhibit strong comprehension of visual data such as images and videos. However, these models usually rely on extensive visual tokens from visual encoders, leading to high computational demands, which limits their applicability in resource-constrained environments and for long-context tasks. In this work, we propose a training-free adaptive inference method for multi-modal LLMs that can accommodate a broad range of efficiency requirements with a minimum performance drop. Our method consists of a) iterative token merging based on embedding similarity before LLMs, and b) progressive token pruning within LLM layers based on multi-modal importance. With a minimalist design, our method can be applied to both video and image LLMs. Extensive experiments on diverse video and image benchmarks demonstrate that our method substantially reduces computation load (e.g., a $\textbf{7-fold}$ reduction in FLOPs) while preserving the performance of video and image LLMs. Further, at a similar computational cost, our method outperforms the state-of-the-art methods in long video understanding (e.g., $\textbf{+4.6}$ on MLVU). Additionally, our in-depth analysis provides insights into token redundancy and LLM layer behaviors, offering guidance for future research in designing efficient multi-modal LLMs. Our code is available at https://github.com/LaVi-Lab/AIM.

</details>

### ZipVL: Accelerating Vision-Language Models Through Dynamic Token Sparsity.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01904)
- **作者**: Yefei He, Feng Chen, Jing Liu, Wenqi Shao, Hong Zhou, Kaipeng Zhang et al.
- **🏷️ 机构**: Zhejiang University,China, The University of Adelaide,Australia, Monash University,ZIP Lab,Australia
- **会议**: ICCV 2025

### SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02208)
- **作者**: Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis et al.
- **🏷️ 机构**: NVIDIA, MIT, University of Toronto
- **会议**: ICCV 2025

### PLADIS: Pushing the Limits of Attention in Diffusion Models at Inference Time by Leveraging Sparsity.
- **链接**: [arXiv:2503.07677](https://arxiv.org/abs/2503.07677)
- **作者**: Kwanyoung Kim, Byeongsu Sim
- **🏷️ 机构**: Samsung Research
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models have shown impressive results in generating high-quality conditional samples using guidance techniques such as Classifier-Free Guidance (CFG). However, existing methods often require additional training or neural function evaluations (NFEs), making them incompatible with guidance-distilled models. Also, they rely on heuristic approaches that need identifying target layers. In this work, we propose a novel and efficient method, termed PLADIS, which boosts pre-trained models (U-Net/Transformer) by leveraging sparse attention. Specifically, we extrapolate query-key correlations using softmax and its sparse counterpart in the cross-attention layer during inference, without requiring extra training or NFEs. By leveraging the noise robustness of sparse attention, our PLADIS unleashes the latent potential of text-to-image diffusion models, enabling them to excel in areas where they once struggled with newfound effectiveness. It integrates seamlessly with guidance techniques, including guidance-distilled models. Extensive experiments show notable improvements in text alignment and human preference, offering a highly efficient and universally applicable solution. See Our project page : https://cubeyoung.github.io/pladis-proejct/

</details>

### Sparsity Outperforms Low-Rank Projections in Few-Shot Adaptation.
- **链接**: [arXiv:2504.12436](https://arxiv.org/abs/2504.12436)
- **作者**: Nairouz Mrabah, Nicolas Richet, Ismail Ben Ayed, Eric Granger
- **🏷️ 机构**: LIVIA, ETS Montreal,ILLS Department of Systems Engineering,Canada
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adapting Vision-Language Models (VLMs) to new domains with few labeled samples remains a significant challenge due to severe overfitting and computational constraints. State-of-the-art solutions, such as low-rank reparameterization, mitigate these issues but often struggle with generalization and require extensive hyperparameter tuning. In this paper, a novel Sparse Optimization (SO) framework is proposed. Unlike low-rank approaches that typically constrain updates to a fixed subspace, our SO method leverages high sparsity to dynamically adjust very few parameters. We introduce two key paradigms. First, we advocate for \textit{local sparsity and global density}, which updates a minimal subset of parameters per iteration while maintaining overall model expressiveness. As a second paradigm, we advocate for \textit{local randomness and global importance}, which sparsifies the gradient using random selection while pruning the first moment based on importance. This combination significantly mitigates overfitting and ensures stable adaptation in low-data regimes. Extensive experiments on 11 diverse datasets show that SO achieves state-of-the-art few-shot adaptation performance while reducing memory overhead.

</details>

### SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs.
- **链接**: [arXiv:2506.05344](https://arxiv.org/abs/2506.05344)
- **作者**: Jiahui Wang, Zuyan Liu, Yongming Rao, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) are commonly derived by extending pre-trained Large Language Models (LLMs) with visual capabilities. In this work, we investigate how MLLMs process visual inputs by analyzing their attention mechanisms. We reveal a surprising sparsity phenomenon: only a small subset (approximately less than 5%) of attention heads in LLMs actively contribute to visual understanding, termed visual heads. To identify these heads efficiently, we design a training-free framework that quantifies head-level visual relevance through targeted response analysis. Building on this discovery, we introduce SparseMM, a KV-Cache optimization strategy that allocates asymmetric computation budgets to heads in LLMs based on their visual scores, leveraging the sparity of visual heads for accelerating the inference of MLLMs. Compared with prior KV-Cache acceleration methods that ignore the particularity of visual, SparseMM prioritizes stress and retaining visual semantics during decoding. Extensive evaluations across mainstream multimodal benchmarks demonstrate that SparseMM achieves superior accuracy-efficiency trade-offs. Notably, SparseMM delivers 1.38x real-time acceleration and 52% memory reduction during generation while maintaining performance parity on efficiency test. Our project is open sourced at https://github.com/CR400AF-A/SparseMM.

</details>

### VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration.
- **链接**: [arXiv:2410.23317](https://arxiv.org/abs/2410.23317)
- **作者**: Dezhan Tu, Danylo Vashchilenko, Yuzhe Lu, Panpan Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have demonstrated impressive performance across a versatile set of tasks. A key challenge in accelerating VLMs is storing and accessing the large Key-Value (KV) cache that encodes long visual contexts, such as images or videos. While existing KV cache compression methods are effective for Large Language Models (LLMs), directly migrating them to VLMs yields suboptimal accuracy and speedup. To bridge the gap, we propose VL-Cache, a novel KV cache compression recipe tailored for accelerating VLM inference. In this paper, we first investigate the unique sparsity pattern of VLM attention by distinguishing visual and text tokens in prefill and decoding phases. Based on these observations, we introduce a layer-adaptive sparsity-aware cache budget allocation method that effectively distributes the limited cache budget across different layers, further reducing KV cache size without compromising accuracy. Additionally, we develop a modality-aware token scoring policy to better evaluate the token importance. Empirical results on multiple benchmark datasets demonstrate that retaining only 10% of KV cache achieves accuracy comparable to that with full cache. In a speed benchmark, our method accelerates end-to-end latency of generating 100 tokens by up to 2.33x and speeds up decoding by up to 7.08x, while reducing the memory footprint of KV cache in GPU by 90%.

</details>

### Matryoshka Multimodal Models.
- **链接**: [arXiv:2405.17430](https://arxiv.org/abs/2405.17430)
- **作者**: Mu Cai, Jianwei Yang, Jianfeng Gao, Yong Jae Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) such as LLaVA have shown strong performance in visual-linguistic reasoning. These models first embed images into a fixed large number of visual tokens and then feed them into a Large Language Model (LLM). However, this design causes an excessive number of tokens for dense visual scenarios such as high-resolution images and videos, leading to great inefficiency. While token pruning/merging methods do exist, they produce a single length output for each image and do not afford flexibility in trading off information density v.s. efficiency. Inspired by the concept of Matryoshka Dolls, we propose M3: Matryoshka Multimodal Models, which learns to represent visual content as nested sets of visual tokens that capture information across multiple coarse-to-fine granularities. Our approach offers several unique benefits for LMMs: (1) One can explicitly control the visual granularity per test instance during inference, e.g. , adjusting the number of tokens used to represent an image based on the anticipated complexity or simplicity of the content; (2) M3 provides a framework for analyzing the granularity needed for existing datasets, where we find that COCO-style benchmarks only need around ~9 visual tokens to obtain accuracy similar to that of using all 576 tokens; (3) Our approach provides a foundation to explore the best trade-off between performance and visual token length at sample level, where our investigation reveals that a large gap exists between the oracle upper bound and current fixed-scale representations.

</details>

### γ-MoD: Exploring Mixture-of-Depth Adaptation for Multimodal Large Language Models.
- **链接**: [arXiv:2410.13859](https://arxiv.org/abs/2410.13859)
- **作者**: Yaxin Luo, Gen Luo, Jiayi Ji, Yiyi Zhou, Xiaoshuai Sun, Zhiqiang Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the significant progress in multimodal large language models (MLLMs), their high computational cost remains a barrier to real-world deployment. Inspired by the mixture of depths (MoDs) in natural language processing, we aim to address this limitation from the perspective of ``activated tokens''. Our key insight is that if most tokens are redundant for the layer computation, then can be skipped directly via the MoD layer. However, directly converting the dense layers of MLLMs to MoD layers leads to substantial performance degradation. To address this issue, we propose an innovative MoD adaptation strategy for existing MLLMs called $γ$-MoD. In $γ$-MoD, a novel metric is proposed to guide the deployment of MoDs in the MLLM, namely rank of attention maps (ARank). Through ARank, we can effectively identify which layer is redundant and should be replaced with the MoD layer. Based on ARank, we further propose two novel designs to maximize the computational sparsity of MLLM while maintaining its performance, namely shared vision-language router and masked routing learning. With these designs, more than 90% dense layers of the MLLM can be effectively converted to the MoD ones. To validate our method, we apply it to three popular MLLMs, and conduct extensive experiments on 9 benchmark datasets. Experimental results not only validate the significant efficiency benefit of $γ$-MoD to existing MLLMs but also confirm its generalization ability on various MLLMs. For example, with a minor performance drop, i.e., -1.5%, $γ$-MoD can reduce the training and inference time of LLaVA-HR by 31.0% and 53.2%, respectively.

</details>

### LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token.
- **链接**: [arXiv:2501.03895](https://arxiv.org/abs/2501.03895)
- **作者**: Shaolei Zhang, Qingkai Fang, Zhe Yang, Yang Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of real-time large multimodal models (LMMs) like GPT-4o has sparked considerable interest in efficient LMMs. LMM frameworks typically encode visual inputs into vision tokens (continuous representations) and integrate them and textual instructions into the context of large language models (LLMs), where large-scale parameters and numerous context tokens (predominantly vision tokens) result in substantial computational overhead. Previous efforts towards efficient LMMs always focus on replacing the LLM backbone with smaller models, while neglecting the crucial issue of token quantity. In this paper, we introduce LLaVA-Mini, an efficient LMM with minimal vision tokens. To achieve a high compression ratio of vision tokens while preserving visual information, we first analyze how LMMs understand vision tokens and find that most vision tokens only play a crucial role in the early layers of LLM backbone, where they mainly fuse visual information into text tokens. Building on this finding, LLaVA-Mini introduces modality pre-fusion to fuse visual information into text tokens in advance, thereby facilitating the extreme compression of vision tokens fed to LLM backbone into one token. LLaVA-Mini is a unified large multimodal model that can support the understanding of images, high-resolution images, and videos in an efficient manner. Experiments across 11 image-based and 7 video-based benchmarks demonstrate that LLaVA-Mini outperforms LLaVA-v1.5 with just 1 vision token instead of 576. Efficiency analyses reveal that LLaVA-Mini can reduce FLOPs by 77%, deliver low-latency responses within 40 milliseconds, and process over 10,000 frames of video on the GPU hardware with 24GB of memory.

</details>

### Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=GTcEe5fayC)
- **作者**: Sheng Li, Qitao Tan, Yue Dai, Zhenglun Kong, Tianyu Wang, Jun Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Probe Pruning: Accelerating LLMs through Dynamic Pruning via Model-Probing.
- **链接**: [出版页](https://openreview.net/forum?id=WOt1owGfuN)
- **作者**: Qi Le, Enmao Diao, Ziyan Wang, Xinran Wang, Jie Ding, Li Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models.
- **链接**: [arXiv:2405.20541](https://arxiv.org/abs/2405.20541)
- **作者**: Zachary Ankner, Cody Blakeney, Kartik Sreenivasan, Max Marion, Matthew L. Leavitt, Mansheej Paul
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we investigate whether small language models can determine high-quality subsets of large-scale text datasets that improve the performance of larger language models. While existing work has shown that pruning based on the perplexity of a larger model can yield high-quality data, we investigate whether smaller models can be used for perplexity-based pruning and how pruning is affected by the domain composition of the data being pruned. We demonstrate that for multiple dataset compositions, perplexity-based pruning of pretraining data can \emph{significantly} improve downstream task performance: pruning based on perplexities computed with a 125 million parameter model improves the average performance on downstream tasks of a 3 billion parameter model by up to 2.04 and achieves up to a $1.45\times$ reduction in pretraining steps to reach commensurate baseline performance. Furthermore, we demonstrate that such perplexity-based data pruning also yields downstream performance gains in the over-trained and data-constrained regimes.

</details>

### LLaMaFlex: Many-in-one LLMs via Generalized Pruning and Weight Sharing.
- **链接**: [出版页](https://openreview.net/forum?id=AyC4uxx2HW)
- **作者**: Ruisi Cai, Saurav Muralidharan, Hongxu Yin, Zhangyang Wang, Jan Kautz, Pavlo Molchanov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Provence: efficient and robust context pruning for retrieval-augmented generation.
- **链接**: [arXiv:2501.16214](https://arxiv.org/abs/2501.16214)
- **作者**: Nadezhda Chirkova, Thibault Formal, Vassilina Nikoulina, Stéphane Clinchant
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Retrieval-augmented generation improves various aspects of large language models (LLMs) generation, but suffers from computational overhead caused by long contexts as well as the propagation of irrelevant retrieved information into generated responses. Context pruning deals with both aspects, by removing irrelevant parts of retrieved contexts before LLM generation. Existing context pruning approaches are however limited, and do not provide a universal model that would be both efficient and robust in a wide range of scenarios, e.g., when contexts contain a variable amount of relevant information or vary in length, or when evaluated on various domains. In this work, we close this gap and introduce Provence (Pruning and Reranking Of retrieVEd relevaNt ContExts), an efficient and robust context pruner for Question Answering, which dynamically detects the needed amount of pruning for a given context and can be used out-of-the-box for various domains. The three key ingredients of Provence are formulating the context pruning task as sequence labeling, unifying context pruning capabilities with context reranking, and training on diverse data. Our experimental results show that Provence enables context pruning with negligible to no drop in performance, in various domains and settings, at almost no cost in a standard RAG pipeline. We also conduct a deeper analysis alongside various ablations to provide insights into training context pruners for future work.

</details>

### Training-Free Dataset Pruning for Instance Segmentation.
- **链接**: [arXiv:2503.00828](https://arxiv.org/abs/2503.00828)
- **作者**: Yalun Dai, Lingao Xiao, Ivor W. Tsang, Yang He
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing dataset pruning techniques primarily focus on classification tasks, limiting their applicability to more complex and practical tasks like instance segmentation. Instance segmentation presents three key challenges: pixel-level annotations, instance area variations, and class imbalances, which significantly complicate dataset pruning efforts. Directly adapting existing classification-based pruning methods proves ineffective due to their reliance on time-consuming model training process. To address this, we propose a novel Training-Free Dataset Pruning (TFDP) method for instance segmentation. Specifically, we leverage shape and class information from image annotations to design a Shape Complexity Score (SCS), refining it into a Scale-Invariant (SI-SCS) and Class-Balanced (CB-SCS) versions to address instance area variations and class imbalances, all without requiring model training. We achieve state-of-the-art results on VOC 2012, Cityscapes, and COCO datasets, generalizing well across CNN and Transformer architectures. Remarkably, our approach accelerates the pruning process by an average of 1349$\times$ on COCO compared to the adapted baselines. Source code is available at: https://github.com/he-y/dataset-pruning-for-instance-segmentation

</details>

### DARE the Extreme: Revisiting Delta-Parameter Pruning For Fine-Tuned Models.
- **链接**: [arXiv:2410.09344](https://arxiv.org/abs/2410.09344)
- **作者**: Wenlong Deng, Yize Zhao, Vala Vakilian, Minghui Chen, Xiaoxiao Li, Christos Thrampoulidis
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Storing open-source fine-tuned models separately introduces redundancy and increases response times in applications utilizing multiple models. Delta-parameter pruning (DPP), particularly the random drop and rescale (DARE) method proposed by Yu et al., addresses this by pruning the majority of delta parameters--the differences between fine-tuned and pre-trained model weights--while typically maintaining minimal performance loss. However, DARE fails when either the pruning rate or the magnitude of the delta parameters is large. We highlight two key reasons for this failure: (1) an excessively large rescaling factor as pruning rates increase, and (2) high mean and variance in the delta parameters. To push DARE's limits, we introduce DAREx (DARE the eXtreme), which features two algorithmic improvements: (1) DAREx-q, a rescaling factor modification that significantly boosts performance at high pruning rates (e.g., >30 % on COLA and SST2 for encoder models, with even greater gains in decoder models), and (2) DAREx-L2, which combines DARE with AdamR, an in-training method that applies appropriate delta regularization before DPP. We also demonstrate that DAREx-q can be seamlessly combined with vanilla parameter-efficient fine-tuning techniques like LoRA and can facilitate structural DPP. Additionally, we revisit the application of importance-based pruning techniques within DPP, demonstrating that they outperform random-based methods when delta parameters are large. Through this comprehensive study, we develop a pipeline for selecting the most appropriate DPP method under various practical scenarios.

</details>

### Adaptive Pruning of Pretrained Transformer via Differential Inclusions.
- **链接**: [arXiv:2501.03289](https://arxiv.org/abs/2501.03289)
- **作者**: Yizhuo Ding, Ke Fan, Yikai Wang, Xinwei Sun, Yanwei Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large transformers have demonstrated remarkable success, making it necessary to compress these models to reduce inference costs while preserving their perfor-mance. Current compression algorithms prune transformers at fixed compression ratios, requiring a unique pruning process for each ratio, which results in high computational costs. In contrast, we propose pruning of pretrained transformers at any desired ratio within a single pruning stage, based on a differential inclusion for a mask parameter. This dynamic can generate the whole regularization solution path of the mask parameter, whose support set identifies the network structure. Therefore, the solution path identifies a Transformer weight family with various sparsity levels, offering greater flexibility and customization. In this paper, we introduce such an effective pruning method, termed SPP (Solution Path Pruning). To achieve effective pruning, we segment the transformers into paired modules, including query-key pairs, value-projection pairs, and sequential linear layers, and apply low-rank compression to these pairs, maintaining the output structure while enabling structural compression within the inner states. Extensive experiments conducted on various well-known transformer backbones have demonstrated the efficacy of SPP.

</details>

### Not All Prompts Are Made Equal: Prompt-based Pruning of Text-to-Image Diffusion Models.
- **链接**: [arXiv:2406.12042](https://arxiv.org/abs/2406.12042)
- **作者**: Alireza Ganjdanesh, Reza Shirkavand, Shangqian Gao, Heng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-to-image (T2I) diffusion models have demonstrated impressive image generation capabilities. Still, their computational intensity prohibits resource-constrained organizations from deploying T2I models after fine-tuning them on their internal target data. While pruning techniques offer a potential solution to reduce the computational burden of T2I models, static pruning methods use the same pruned model for all input prompts, overlooking the varying capacity requirements of different prompts. Dynamic pruning addresses this issue by utilizing a separate sub-network for each prompt, but it prevents batch parallelism on GPUs. To overcome these limitations, we introduce Adaptive Prompt-Tailored Pruning (APTP), a novel prompt-based pruning method designed for T2I diffusion models. Central to our approach is a prompt router model, which learns to determine the required capacity for an input text prompt and routes it to an architecture code, given a total desired compute budget for prompts. Each architecture code represents a specialized model tailored to the prompts assigned to it, and the number of codes is a hyperparameter. We train the prompt router and architecture codes using contrastive learning, ensuring that similar prompts are mapped to nearby codes. Further, we employ optimal transport to prevent the codes from collapsing into a single one. We demonstrate APTP's effectiveness by pruning Stable Diffusion (SD) V2.1 using CC3M and COCO as target datasets. APTP outperforms the single-model pruning baselines in terms of FID, CLIP, and CMMD scores. Our analysis of the clusters learned by APTP reveals they are semantically meaningful. We also show that APTP can automatically discover previously empirically found challenging prompts for SD, e.g. prompts for generating text images, assigning them to higher capacity codes.

</details>

### Beware of Calibration Data for Pruning Large Language Models.
- **链接**: [arXiv:2410.17711](https://arxiv.org/abs/2410.17711)
- **作者**: Yixin Ji, Yang Xiang, Juntao Li, Qingrong Xia, Ping Li, Xinyu Duan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As large language models (LLMs) are widely applied across various fields, model compression has become increasingly crucial for reducing costs and improving inference efficiency. Post-training pruning is a promising method that does not require resource-intensive iterative training and only needs a small amount of calibration data to assess the importance of parameters. Recent research has enhanced post-training pruning from different aspects but few of them systematically explore the effects of calibration data, and it is unclear if there exist better calibration data construction strategies. We fill this blank and surprisingly observe that calibration data is also crucial to post-training pruning, especially for high sparsity. Through controlled experiments on important influence factors of calibration data, including the pruning settings, the amount of data, and its similarity with pre-training data, we observe that a small size of data is adequate, and more similar data to its pre-training stage can yield better performance. As pre-training data is usually inaccessible for advanced LLMs, we further provide a self-generating calibration data synthesis strategy to construct feasible calibration data. Experimental results on recent strong open-source LLMs (e.g., DCLM, and LLaMA-3) show that the proposed strategy can enhance the performance of strong pruning methods (e.g., Wanda, DSnoT, OWL) by a large margin (up to $2.68\%$). Code is available at https://github.com/Dereck0602/calibration_data.

</details>

### Exploring Learning Complexity for Efficient Downstream Dataset Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=FN7n7JRjsk)
- **作者**: Wenyu Jiang, Zhenlong Liu, Zejian Xie, Songxin Zhang, Bingyi Jing, Hongxin Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Efficient Online Pruning and Abstraction for Imperfect Information Extensive-Form Games.
- **链接**: [出版页](https://openreview.net/forum?id=MTcgsz1SHr)
- **作者**: Boning Li, Longbo Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Beyond Linear Approximations: A Novel Pruning Approach for Attention Matrix.
- **链接**: [arXiv:2410.11261](https://arxiv.org/abs/2410.11261)
- **作者**: Yingyu Liang, Jiangxuan Long, Zhenmei Shi, Zhao Song, Yufa Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) have shown immense potential in enhancing various aspects of our daily lives, from conversational AI to search and AI assistants. However, their growing capabilities come at the cost of extremely large model sizes, making deployment on edge devices challenging due to memory and computational constraints. This paper introduces a novel approach to LLM weight pruning that directly optimizes for approximating the attention matrix, a core component of transformer architectures. Unlike existing methods that focus on linear approximations, our approach accounts for the non-linear nature of the Softmax attention mechanism. We provide theoretical guarantees for the convergence of our Gradient Descent-based optimization method to a near-optimal pruning mask solution. Our empirical results demonstrate the effectiveness of our non-linear pruning approach in maintaining model performance while significantly reducing computational costs, which is beyond the current state-of-the-art methods, i.e., SparseGPT and Wanda, by a large margin. This work establishes a new theoretical foundation for pruning algorithm design in LLMs, potentially paving the way for more efficient LLM inference on resource-constrained devices.

</details>

### Preserving Deep Representations in One-Shot Pruning: A Hessian-Free Second-Order Optimization Framework.
- **链接**: [arXiv:2411.18376](https://arxiv.org/abs/2411.18376)
- **作者**: Ryan Lucas, Rahul Mazumder
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present SNOWS, a one-shot post-training pruning framework aimed at reducing the cost of vision network inference without retraining. Current leading one-shot pruning methods minimize layer-wise least squares reconstruction error which does not take into account deeper network representations. We propose to optimize a more global reconstruction objective. This objective accounts for nonlinear activations deep in the network to obtain a better proxy for the network loss. This nonlinear objective leads to a more challenging optimization problem -- we demonstrate it can be solved efficiently using a specialized second-order optimization framework. A key innovation of our framework is the use of Hessian-free optimization to compute exact Newton descent steps without needing to compute or store the full Hessian matrix. A distinct advantage of SNOWS is that it can be readily applied on top of any sparse mask derived from prior methods, readjusting their weights to exploit nonlinearities in deep feature representations. SNOWS obtains state-of-the-art results on various one-shot pruning benchmarks including residual networks and Vision Transformers (ViT/B-16 and ViT/L-16, 86m and 304m parameters respectively).

</details>

### Probabilistic Neural Pruning via Sparsity Evolutionary Fokker-Planck-Kolmogorov Equation.
- **链接**: [出版页](https://openreview.net/forum?id=hJ1BaJ5ELp)
- **作者**: Zhanfeng Mo, Haosen Shi, Sinno Jialin Pan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Severing Spurious Correlations with Data Pruning.
- **链接**: [arXiv:2503.18258](https://arxiv.org/abs/2503.18258)
- **作者**: Varun Mulchandani, Jung-Eun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks have been shown to learn and rely on spurious correlations present in the data that they are trained on. Reliance on such correlations can cause these networks to malfunction when deployed in the real world, where these correlations may no longer hold. To overcome the learning of and reliance on such correlations, recent studies propose approaches that yield promising results. These works, however, study settings where the strength of the spurious signal is significantly greater than that of the core, invariant signal, making it easier to detect the presence of spurious features in individual training samples and allow for further processing. In this paper, we identify new settings where the strength of the spurious signal is relatively weaker, making it difficult to detect any spurious information while continuing to have catastrophic consequences. We also discover that spurious correlations are learned primarily due to only a handful of all the samples containing the spurious feature and develop a novel data pruning technique that identifies and prunes small subsets of the training data that contain these samples. Our proposed technique does not require inferred domain knowledge, information regarding the sample-wise presence or nature of spurious information, or human intervention. Finally, we show that such data pruning attains state-of-the-art performance on previously studied settings where spurious information is identifiable.

</details>

### Context-aware Dynamic Pruning for Speech Foundation Models.
- **链接**: [出版页](https://openreview.net/forum?id=u2QdCiOgwA)
- **作者**: Masao Someki, Yifan Peng, Siddhant Arora, Markus Müller, Athanasios Mouchtaris, Grant P. Strimel et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Data Pruning by Information Maximization.
- **链接**: [arXiv:2506.01701](https://arxiv.org/abs/2506.01701)
- **作者**: Haoru Tan, Sitong Wu, Wei Huang, Shizhen Zhao, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present InfoMax, a novel data pruning method, also known as coreset selection, designed to maximize the information content of selected samples while minimizing redundancy. By doing so, InfoMax enhances the overall informativeness of the coreset. The information of individual samples is measured by importance scores, which capture their influence or difficulty in model learning. To quantify redundancy, we use pairwise sample similarities, based on the premise that similar samples contribute similarly to the learning process. We formalize the coreset selection problem as a discrete quadratic programming (DQP) task, with the objective of maximizing the total information content, represented as the sum of individual sample contributions minus the redundancies introduced by similar samples within the coreset. To ensure practical scalability, we introduce an efficient gradient-based solver, complemented by sparsification techniques applied to the similarity matrix and dataset partitioning strategies. This enables InfoMax to seamlessly scale to datasets with millions of samples. Extensive experiments demonstrate the superior performance of InfoMax in various data pruning tasks, including image classification, vision-language pre-training, and instruction tuning for large language models. Code is available at https://github.com/hrtan/InfoMax.

</details>

### DRoP: Distributionally Robust Data Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=fxv0FfmDAg)
- **作者**: Artem M. Vysogorets, Kartik Ahuja, Julia Kempe
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Revisit Micro-batch Clipping: Adaptive Data Pruning via Gradient Manipulation.
- **链接**: [arXiv:2408.16204](https://arxiv.org/abs/2408.16204)
- **作者**: Lun Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Micro-batch clipping, a gradient clipping method, has recently shown potential in enhancing auto-speech recognition (ASR) model performance. However, the underlying mechanism behind this improvement remains mysterious, particularly the observation that only certain micro-batch sizes are beneficial. In this paper, we make the first attempt to explain this phenomenon. Inspired by recent data pruning research, we assume that specific training samples may impede model convergence during certain training phases. Under this assumption, the convergence analysis shows that micro-batch clipping can improve the convergence rate asymptotically at the cost of an additional constant bias that does not diminish with more training iterations. The bias is dependent on a few factors and can be minimized at specific micro-batch size, thereby elucidating the existence of the sweet-spot micro-batch size observed previously. We also verify the effectiveness of micro-batch clipping beyond speech models on vision and language models, and show promising performance gains in these domains. An exploration of potential limitations shows that micro-batch clipping is less effective when training data originates from multiple distinct domains.

</details>

### DPaI: Differentiable Pruning at Initialization with Node-Path Balance Principle.
- **链接**: [出版页](https://openreview.net/forum?id=hvLBTpiDt3)
- **作者**: Lichuan Xiang, Quan Nguyen-Tri, Lan-Cuong Nguyen, Hoang Pham, Khoat Than, Long Tran-Thanh et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### ThinK: Thinner Key Cache by Query-Driven Pruning.
- **链接**: [arXiv:2407.21018](https://arxiv.org/abs/2407.21018)
- **作者**: Yuhui Xu, Zhanming Jie, Hanze Dong, Lei Wang, Xudong Lu, Aojun Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) have revolutionized the field of natural language processing, achieving unprecedented performance across a variety of applications. However, their increased computational and memory demands present significant challenges, especially when handling long sequences. This paper focuses on the long-context scenario, addressing the inefficiencies in KV cache memory consumption during inference. Unlike existing approaches that optimize the memory based on the sequence length, we identify substantial redundancy in the channel dimension of the KV cache, as indicated by an uneven magnitude distribution and a low-rank structure in the attention weights. In response, we propose ThinK, a novel query-dependent KV cache pruning method designed to minimize attention weight loss while selectively pruning the least significant channels. Our approach not only maintains or enhances model accuracy but also achieves a reduction in KV cache memory costs by over 20% compared with vanilla KV cache eviction and quantization methods. For instance, ThinK integrated with KIVI can achieve a 2.8x reduction in peak memory usage while maintaining nearly the same quality, enabling up to a 5x increase in batch size when using a single GPU. Extensive evaluations on the LLaMA and Mistral models across various long-sequence datasets verified the efficiency of ThinK, establishing a new baseline algorithm for efficient LLM deployment without compromising performance. Our code has been made available at https://github.com/SalesforceAIResearch/ThinK.

</details>

### OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition.
- **链接**: [arXiv:2409.13652](https://arxiv.org/abs/2409.13652)
- **作者**: Stephen Zhang, Vardan Papyan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent paradigm shift to large-scale foundation models has brought about a new era for deep learning that, while has found great success in practice, has also been plagued by prohibitively expensive costs in terms of high memory consumption and compute. To mitigate these issues, there has been a concerted effort in post-hoc neural network pruning techniques that do not require costly retraining. Despite the considerable progress being made, existing methods often exhibit a steady drop in model performance as the compression increases. In this paper, we present a novel approach to compressing large transformers, coined OATS, that utilizes the second moment information in the input embeddings to decompose the model weights into a sum of sparse and low-rank matrices. Without any retraining, OATS achieves state-of-the-art performance when compressing models by up to $60\%$ on large language models such as Llama-3 and Phi-3 and vision transformers such as ViT and DINOv2 while delivering up to $1.37\times$ the CPU acceleration versus a model that was comparably pruned.

</details>

### R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference.
- **链接**: [arXiv:2504.19449](https://arxiv.org/abs/2504.19449)
- **作者**: Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs), while demonstrating remarkable capabilities across various applications, present significant challenges during inference due to their substantial model size, especially when deployed on edge devices. Activation sparsity offers a promising solution to reduce computation and memory movement, enabling more efficient inference, particularly for small-batch on-device applications. However, current approaches face limitations with non-ReLU activation function, which are foundational to most advanced LLMs, or require heavy continual training. Additionally, the difficulty in predicting active channels and limited achievable sparsity ratios constrain the effectiveness of activation sparsity-based methods. In this paper, we introduce R-Sparse, a training-free activation sparsity approach capable of achieving high sparsity levels in advanced LLMs. We conducted two preliminary investigations into how different components contribute to the output within a single linear layer and found two key observations: (i) the non-sparse components of the input function can be regarded as a few bias terms, and (ii) The full computation can be effectively approximated by an appropriate combination of input channels and weight singular values. Building on this, we replace the linear layers in LLMs with a rank-aware sparse inference method that leverages the sparsity of input channels and singular value components, eliminating the need for active channel prediction like the output sparsity based approaches. Experiments on Llama-2/3 and Mistral models across ten diverse tasks demonstrate that R-Sparse achieves comparable performance at 50% model-level sparsity, resulting in a significant 43% end-to-end efficient improvements with customized kernels.

</details>

### Zeroth-Order Fine-Tuning of LLMs with Transferable Static Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=myYzr50xBh)
- **作者**: Wentao Guo, Jikai Long, Yimeng Zeng, Zirui Liu, Xinyu Yang, Yide Ran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Effective Interplay between Sparsity and Quantization: From Theory to Practice.
- **链接**: [arXiv:2405.20935](https://arxiv.org/abs/2405.20935)
- **作者**: Simla Burcu Harma, Ayan Chakraborty, Elizaveta Kostenok, Danila Mishin, Dongho Ha, Babak Falsafi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The increasing size of deep neural networks (DNNs) necessitates effective model compression to reduce their computational and memory footprints. Sparsity and quantization are two prominent compression methods that have been shown to reduce DNNs' computational and memory footprints significantly while preserving model accuracy. However, how these two methods interact when combined together remains a key question for developers, as many tacitly assume that they are orthogonal, meaning that their combined use does not introduce additional errors beyond those introduced by each method independently. In this paper, we provide the first mathematical proof that sparsity and quantization are non-orthogonal. We corroborate these results with experiments spanning a range of large language models, including the OPT and LLaMA model families (with 125M to 8B parameters), and vision models like ViT and ResNet. We show that the order in which we apply these methods matters because applying quantization before sparsity may disrupt the relative importance of tensor elements, which may inadvertently remove significant elements from a tensor. More importantly, we show that even if applied in the correct order, the compounded errors from sparsity and quantization can significantly harm accuracy. Our findings extend to the efficient deployment of large models in resource-constrained compute platforms to reduce serving cost, offering insights into best practices for applying these compression methods to maximize hardware resource efficiency without compromising accuracy.

</details>

### Leveraging Variable Sparsity to Refine Pareto Stationarity in Multi-Objective Optimization.
- **链接**: [出版页](https://openreview.net/forum?id=Bl3e8HV9xW)
- **作者**: Zeou Hu, Yaoliang Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Improved Algorithms for Kernel Matrix-Vector Multiplication Under Sparsity Assumptions.
- **链接**: [arXiv:2507.23539](https://arxiv.org/abs/2507.23539)
- **作者**: Piotr Indyk, Michael Kapralov, Kshiteej Sheth, Tal Wagner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motivated by the problem of fast processing of attention matrices, we study fast algorithms for computing matrix-vector products for asymmetric Gaussian Kernel matrices $K\in \mathbb{R}^{n\times n}$. $K$'s columns are indexed by a set of $n$ keys $k_1,k_2\ldots, k_n\in \mathbb{R}^d$, rows by a set of $n$ queries $q_1,q_2,\ldots,q_n\in \mathbb{R}^d $, and its $i,j$ entry is $K_{ij} = e^{-\|q_i-k_j\|_2^2/2σ^2}$ for some bandwidth parameter $σ>0$. Given a vector $x\in \mathbb{R}^n$ and error parameter $ε>0$, our task is to output a $y\in \mathbb{R}^n$ such that $\|Kx-y\|_2\leq ε\|x\|_2$ in time subquadratic in $n$ and linear in $d$. Our algorithms rely on the following modelling assumption about the matrices $K$: the sum of the entries of $K$ scales linearly in $n$, as opposed to worst case quadratic growth. We validate this assumption experimentally, for Gaussian kernel matrices encountered in various settings such as fast attention computation in LLMs. We obtain the first subquadratic-time algorithm that works under this assumption, for unrestricted vectors.

</details>

### Training-Free Activation Sparsity in Large Language Models.
- **链接**: [arXiv:2408.14690](https://arxiv.org/abs/2408.14690)
- **作者**: James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Activation sparsity can enable practical inference speedups in large language models (LLMs) by reducing the compute and memory-movement required for matrix multiplications during the forward pass. However, existing methods face limitations that inhibit widespread adoption. Some approaches are tailored towards older models with ReLU-based sparsity, while others require extensive continued pre-training on up to hundreds of billions of tokens. This paper describes TEAL, a simple training-free method that applies magnitude-based activation sparsity to hidden states throughout the entire model. TEAL achieves 40-50% model-wide sparsity with minimal performance degradation across Llama-2, Llama-3, and Mistral families, with sizes varying from 7B to 70B. We improve existing sparse kernels and demonstrate wall-clock decoding speed-ups of up to 1.53$\times$ and 1.8$\times$ at 40% and 50% model-wide sparsity. TEAL is compatible with weight quantization, enabling further efficiency gains.

</details>

### Wasserstein Distances, Neuronal Entanglement, and Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=cnKhHxN3xj)
- **作者**: Shashata Sawmya, Linghao Kong, Ilia Markov, Dan Alistarh, Nir Shavit
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Medium-Difficulty Samples Constitute Smoothed Decision Boundary for Knowledge Distillation on Pruned Datasets.
- **链接**: [出版页](https://openreview.net/forum?id=Rz4UkJziFe)
- **作者**: Yudong Chen, Xuwei Xu, Frank de Hoog, Jiajun Liu, Sen Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Efficient LiDAR Reflectance Compression via Scanning Serialization.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhu25aa.html)
- **作者**: Jiahao Zhu, Kang You, Dandan Ding, Zhan Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Compression via Pre-trained Transformers: A Study on Byte-Level Multimodal Data.
- **链接**: [出版页](https://proceedings.mlr.press/v267/heurtel-depeiges25a.html)
- **作者**: David Heurtel-Depeiges, Anian Ruoss, Joel Veness, Tim Genewein
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### DLP: Dynamic Layerwise Pruning in Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/chen25l.html)
- **作者**: Yuli Chen, Bo Cheng, Jiale Han, Yingying Zhang, Yingting Li, Shuhao Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Distilling the Knowledge in Data Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/ben-baruch25a.html)
- **作者**: Emanuel Ben Baruch, Adam Botach, Igor Kviatkovsky, Manoj Aggarwal, Gérard G. Medioni
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### A Dynamical Systems-Inspired Pruning Strategy for Addressing Oversmoothing in Graph Attention Networks.
- **链接**: [出版页](https://proceedings.mlr.press/v267/chakraborty25a.html)
- **作者**: Biswadeep Chakraborty, Harshit Kumar, Saibal Mukhopadhyay
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Lightweight Dataset Pruning without Full Training via Example Difficulty and Prediction Uncertainty.
- **链接**: [出版页](https://proceedings.mlr.press/v267/cho25e.html)
- **作者**: Yeseul Cho, Baekrok Shin, Changmin Kang, Chulhee Yun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Compressing tree ensembles through Level-wise Optimization and Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/devos25a.html)
- **作者**: Laurens Devos, Timo Martens, Deniz Can Oruc, Wannes Meert, Hendrik Blockeel, Jesse Davis
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SlimLLM: Accurate Structured Pruning for Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/guo25a.html)
- **作者**: Jialong Guo, Xinghao Chen, Yehui Tang, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Optimal Decision Tree Pruning Revisited: Algorithms and Complexity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/harviainen25a.html)
- **作者**: Juha Harviainen, Frank Sommer, Manuel Sorge, Stefan Szeider
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Olica: Efficient Structured Pruning of Large Language Models without Retraining.
- **链接**: [出版页](https://proceedings.mlr.press/v267/he25m.html)
- **作者**: Jiujun He, Huazhen Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Instruction-Following Pruning for Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/hou25b.html)
- **作者**: Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SAFE: Finding Sparse and Flat Minima to Improve Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lee25s.html)
- **作者**: Dongyeop Lee, Kwanhee Lee, Jinseok Chung, Namhoon Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### BaWA: Automatic Optimizing Pruning Metric for Large Language Models with Balanced Weight and Activation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/liu25cs.html)
- **作者**: Lian Liu, Xiandong Zhao, Guanchen Li, Dong Li, Mengdi Wang, Yinhe Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Pruning for GNNs: Lower Complexity with Comparable Expressiveness.
- **链接**: [出版页](https://proceedings.mlr.press/v267/ma25e.html)
- **作者**: Dun Ma, Jianguo Chen, Wenguo Yang, Suixiang Gao, Shengminjie Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### CLOVER: Cross-Layer Orthogonal Vectors Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/meng25d.html)
- **作者**: Fanxu Meng, Pingzhi Tang, Fan Jiang, Muhan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### On the Dynamic Regret of Following the Regularized Leader: Optimism with History Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/mhaisen25a.html)
- **作者**: Naram Mhaisen, George Iosifidis
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

## 跨领域论文（完整笔记在其他领域）

- DeepCompress-ViT: Rethinking Model Compression to Enhance Efficiency of Vision Transformers at the Edge. → [vision-transformer](../vision-transformer/Guideline%202025.md)
- Towards RAW Object Detection in Diverse Conditions. → [object-detection](../object-detection/Guideline%202025.md)
- SparseAlign: a Fully Sparse Framework for Cooperative Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- EditSplat: Multi-View Fusion and Attention-Guided Optimization for View-Consistent 3D Scene Editing with 3D Gaussian Splatting. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- FastVLM: Efficient Vision Encoding for Vision Language Models. → [vlm](../vlm/Guideline%202025.md)
- Not Only Text: Exploring Compositionality of Visual Representations in Vision-Language Models. → [vlm](../vlm/Guideline%202025.md)
- MotionBench: Benchmarking and Improving Fine-grained Video Motion Understanding for Vision Language Models. → [vlm](../vlm/Guideline%202025.md)
- EfficientLLaVA: Generalizable Auto-Pruning for Large Vision-language Models. → [vlm](../vlm/Guideline%202025.md)
- Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding. → [video-understanding](../video-understanding/Guideline%202025.md)
- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- LoRASculpt: Sculpting LoRA for Harmonizing General and Specialized Knowledge in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- LibraGrad: Balancing Gradient Flow for Universally Better Vision Transformer Attributions. → [vision-transformer](../vision-transformer/Guideline%202025.md)
- DoppDrive: Doppler-Driven Temporal Aggregation for Improved Radar Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Plug-in Feedback Self-Adaptive Attention in CLIP for Training-Free Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- 3D-LMVIC: Learning-based Multi-View Image Compression with 3D Gaussian Geometric Priors. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
<!-- COMPLETE v1 papers=147 -->
