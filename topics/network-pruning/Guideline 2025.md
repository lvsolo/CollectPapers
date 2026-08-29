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
