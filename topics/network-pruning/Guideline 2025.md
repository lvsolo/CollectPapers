# Network Pruning — 2025 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 40 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Efficient LiDAR Reflectance Compression via Scanning Serialization.
- **链接**: [arXiv:2505.09433](https://arxiv.org/abs/2505.09433)
- **作者**: Jiahao Zhu, Kang You, Dandan Ding, Zhan Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reflectance attributes in LiDAR point clouds provide essential information for downstream tasks but remain underexplored in neural compression methods. To address this, we introduce SerLiC, a serialization-based neural compression framework to fully exploit the intrinsic characteristics of LiDAR reflectance. SerLiC first transforms 3D LiDAR point clouds into 1D sequences via scan-order serialization, offering a device-centric perspective for reflectance analysis. Each point is then tokenized into a contextual representation comprising its sensor scanning index, radial distance, and prior reflectance, for effective dependencies exploration. For efficient sequential modeling, Mamba is incorporated with a dual parallelization scheme, enabling simultaneous autoregressive dependency capture and fast processing. Extensive experiments demonstrate that SerLiC attains over 2x volume reduction against the original reflectance data, outperforming the state-of-the-art method by up to 22% reduction of compressed bits while using only 2% of its parameters. Moreover, a lightweight version of SerLiC achieves > 10 fps (frames per second) with just 111K parameters, which is attractive for real-world applications.

</details>

### Contradiction Retrieval via Contrastive Learning with Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xu25s.html)
- **作者**: Haike Xu, Zongyu Lin, Kai-Wei Chang, Yizhou Sun, Piotr Indyk
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding.
- **链接**: [出版页](https://proceedings.mlr.press/v267/shen25j.html)
- **作者**: Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Lemeng Wu, Jun Chen, Chenchen Zhu et al.
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
- **链接**: [arXiv:2506.06866](https://arxiv.org/abs/2506.06866)
- **作者**: Dongyeop Lee, Kwanhee Lee, Jinseok Chung, Namhoon Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparsifying neural networks often suffers from seemingly inevitable performance degradation, and it remains challenging to restore the original performance despite much recent progress. Motivated by recent studies in robust optimization, we aim to tackle this problem by finding subnetworks that are both sparse and flat at the same time. Specifically, we formulate pruning as a sparsity-constrained optimization problem where flatness is encouraged as an objective. We solve it explicitly via an augmented Lagrange dual approach and extend it further by proposing a generalized projection operation, resulting in novel pruning methods called SAFE and its extension, SAFE$^+$. Extensive evaluations on standard image classification and language modeling tasks reveal that SAFE consistently yields sparse networks with improved generalization performance, which compares competitively to well-established baselines. In addition, SAFE demonstrates resilience to noisy data, making it well-suited for real-world conditions.

</details>

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

### Earley-Driven Dynamic Pruning for Efficient Structured Decoding.
- **链接**: [出版页](https://proceedings.mlr.press/v267/sun25v.html)
- **作者**: Xintong Sun, Chi Wei, Minghao Tian, Shiwen Ni
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wang25eb.html)
- **作者**: Qinsi Wang, Hancheng Ye, Ming-Yu Chung, Yudong Liu, Yueqian Lin, Martin Kuo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Prompt-based Depth Pruning of Large Language Models.
- **链接**: [arXiv:2502.04348](https://arxiv.org/abs/2502.04348)
- **作者**: Juyun Wee, Minjae Park, Jaeho Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Depth pruning aims to reduce the inference cost of a large language model without any hardware-specific complications, by simply removing several less important transformer blocks. However, our empirical findings suggest that the importance of a transformer block may be highly task-dependent -- a block that is crucial for a task can be removed without degrading the accuracy on another task. Based on this observation, we develop a dynamic depth pruning algorithm, coined PuDDing (Prompt-routed Dynamic Depth Pruning), which determines which blocks to omit from the model based on the input prompt. PuDDing operates by training a lightweight router to predict the best omission set among a set of options, where this option set has also been constructed in a data-driven manner. Empirical results on commonsense reasoning benchmarks demonstrate that PuDDing effectively accelerates the inference language models, and achieves better on-task performance than static depth pruning baselines.

</details>

### Discrepancy Minimization in Input-Sparsity Time.
- **链接**: [arXiv:2210.12468](https://arxiv.org/abs/2210.12468)
- **作者**: Yichuan Deng, Xiaoyu Li, Zhao Song, Omri Weinstein
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A recent work by [Larsen, SODA 2023] introduced a faster combinatorial alternative to Bansal's SDP algorithm for finding a coloring $x \in \{-1, 1\}^n$ that approximately minimizes the discrepancy $\mathrm{disc}(A, x) := | A x |_{\infty}$ of a real-valued $m \times n$ matrix $A$. Larsen's algorithm runs in $\widetilde{O}(mn^2)$ time compared to Bansal's $\widetilde{O}(mn^{4.5})$-time algorithm, with a slightly weaker logarithmic approximation ratio in terms of the hereditary discrepancy of $A$ [Bansal, FOCS 2010]. We present a combinatorial $\widetilde{O}(\mathrm{nnz}(A) + n^3)$-time algorithm with the same approximation guarantee as Larsen's, optimal for tall matrices where $m = \mathrm{poly}(n)$. Using a more intricate analysis and fast matrix multiplication, we further achieve a runtime of $\widetilde{O}(\mathrm{nnz}(A) + n^{2.53})$, breaking the cubic barrier for square matrices and surpassing the limitations of linear-programming approaches [Eldan and Singh, RS&A 2018]. Our algorithm relies on two key ideas: (i) a new sketching technique for finding a projection matrix with a short $\ell_2$-basis using implicit leverage-score sampling, and (ii) a data structure for efficiently implementing the iterative Edge-Walk partial-coloring algorithm [Lovett and Meka, SICOMP 2015], and using an alternative analysis to enable ''lazy'' batch updates with low-rank corrections. Our results nearly close the computational gap between real-valued and binary matrices, for which input-sparsity time coloring was recently obtained by [Jain, Sah and Sawhney, SODA 2023].

</details>

### Pivoting Factorization: A Compact Meta Low-Rank Representation of Sparsity for Efficient Inference in Large Language Models.
- **链接**: [arXiv:2501.19090](https://arxiv.org/abs/2501.19090) · [代码](https://github.com/biomedical-cybernetics/pivoting-factorization)
- **作者**: Jialin Zhao, Yingtao Zhang, Carlo Vittorio Cannistraci
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid growth of Large Language Models has driven demand for effective model compression techniques to reduce memory and computation costs. Low-rank pruning has gained attention for its GPU compatibility across all densities. However, low-rank pruning struggles to match the performance of semi-structured pruning, often doubling perplexity at similar densities. In this paper, we propose Pivoting Factorization (PIFA), a novel lossless meta low-rank representation that unsupervisedly learns a compact form of any low-rank representation, effectively eliminating redundant information. PIFA identifies pivot rows (linearly independent rows) and expresses non-pivot rows as linear combinations, achieving 24.2% additional memory savings and 24.6% faster inference over low-rank layers at rank = 50% of dimension. To mitigate the performance degradation caused by low-rank pruning, we introduce a novel, retraining-free reconstruction method that minimizes error accumulation (M). MPIFA, combining M and PIFA into an end-to-end framework, significantly outperforms existing low-rank pruning methods, and achieves performance comparable to semi-structured pruning, while surpassing it in GPU efficiency and compatibility. Our code is available at https://github.com/biomedical-cybernetics/pivoting-factorization.

</details>

### Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/abnar25a.html)
- **作者**: Samira Abnar, Harshay Shah, Dan Busbridge, Alaaeldin El-Nouby, Joshua M. Susskind, Vimal Thilak
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Position: A Theory of Deep Learning Must Include Compositional Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/danhofer25a.html)
- **作者**: David A. Danhofer, Davide D'Ascenzo, Rafael Dubach, Tomaso A. Poggio
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### HashAttention: Semantic Sparsity for Faster Inference.
- **链接**: [出版页](https://proceedings.mlr.press/v267/desai25a.html)
- **作者**: Aditya Desai, Shuo Yang, Alejandro Cuadron, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SHIELD: Multi-task Multi-distribution Vehicle Routing Solver with Sparsity and Hierarchy.
- **链接**: [出版页](https://proceedings.mlr.press/v267/goh25a.html)
- **作者**: Yong Liang Goh, Zhiguang Cao, Yining Ma, Jianan Zhou, Mohammed Haroon Dupty, Wee Sun Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### The Role of Sparsity for Length Generalization in LLMs.
- **链接**: [出版页](https://proceedings.mlr.press/v267/golowich25a.html)
- **作者**: Noah Golowich, Samy Jelassi, David Brandfonbrener, Sham M. Kakade, Eran Malach
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective.
- **链接**: [出版页](https://proceedings.mlr.press/v267/huang25ax.html)
- **作者**: Weizhong Huang, Yuxin Zhang, Xiawu Zheng, Fei Chao, Rongrong Ji
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/khaki25a.html)
- **作者**: Samir Khaki, Xiuyu Li, Junxian Guo, Ligeng Zhu, Konstantinos N. Plataniotis, Amir Yazdanbakhsh et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### FlashTP: Fused, Sparsity-Aware Tensor Product for Machine Learning Interatomic Potentials.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lee25l.html)
- **作者**: Seung Yul Lee, Hojoon Kim, Yutack Park, Dawoon Jeong, Seungwu Han, Yeonhong Park et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Proxsparse: Regularized Learning of Semi-Structured Sparsity masks for Pretrained LLMS.
- **链接**: [出版页](https://proceedings.mlr.press/v267/liu25bi.html)
- **作者**: Hongyi Liu, Rajarshi Saha, Zhen Jia, Youngsuk Park, Jiaji Huang, Shoham Sabach et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Sparsing Law: Towards Large Language Models with Greater Activation Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/luo25i.html)
- **作者**: Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Efficient and Scalable Density Functional Theory Hamiltonian Prediction through Adaptive Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/luo25l.html)
- **作者**: Erpai Luo, Xinran Wei, Lin Huang, Yunyang Li, Han Yang, Zaishuo Xia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Network Sparsity Unlocks the Scaling Potential of Deep Reinforcement Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/ma25l.html)
- **作者**: Guozheng Ma, Lu Li, Zilin Wang, Li Shen, Pierre-Luc Bacon, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SecEmb: Sparsity-Aware Secure Federated Learning of On-Device Recommender System with Large Embedding.
- **链接**: [出版页](https://proceedings.mlr.press/v267/mai25a.html)
- **作者**: Peihua Mai, Youlong Ding, Ziyan Lyu, Minxin Du, Yan Pang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression.
- **链接**: [出版页](https://proceedings.mlr.press/v267/mozaffari25a.html)
- **作者**: Mohammad Mozaffari, Amir Yazdanbakhsh, Maryam Mehri Dehnavi
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Beyond Minimax Rates in Group Distributionally Robust Optimization via a Novel Notion of Sparsity.
- **链接**: [arXiv:2410.00690](https://arxiv.org/abs/2410.00690)
- **作者**: Quan M. Nguyen, Nishant A. Mehta, Cristóbal Guzmán
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The minimax sample complexity of group distributionally robust optimization (GDRO) has been determined up to a $\log(K)$ factor, where $K$ is the number of groups. In this work, we venture beyond the minimax perspective via a novel notion of sparsity that we dub $(λ, β)$-sparsity. In short, this condition means that at any parameter $θ$, there is a set of at most $β$ groups whose risks at $θ$ all are at least $λ$ larger than the risks of the other groups. To find an $ε$-optimal $θ$, we show via a novel algorithm and analysis that the $ε$-dependent term in the sample complexity can swap a linear dependence on $K$ for a linear dependence on the potentially much smaller $β$. This improvement leverages recent progress in sleeping bandits, showing a fundamental connection between the two-player zero-sum game optimization framework for GDRO and per-action regret bounds in sleeping bandits. We next show an adaptive algorithm which, up to log factors, gets a sample complexity bound that adapts to the best $(λ, β)$-sparsity condition that holds. We also show how to get a dimension-free semi-adaptive sample complexity bound with a computationally efficient method. Finally, we demonstrate the practicality of the $(λ, β)$-sparsity condition and the improved sample efficiency of our algorithms on both synthetic and real-life datasets.

</details>

### Accelerating Linear Recurrent Neural Networks for the Edge with Unstructured Sparsity.
- **链接**: [arXiv:2502.01330](https://arxiv.org/abs/2502.01330)
- **作者**: Alessandro Pierro, Steven Abreu, Jonathan Timcheck, Philipp Stratmann, Andreas Wild, Sumit Bam Shrestha
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Linear recurrent neural networks enable powerful long-range sequence modeling with constant memory usage and time-per-token during inference. These architectures hold promise for streaming applications at the edge, but deployment in resource-constrained environments requires hardware-aware optimizations to minimize latency and energy consumption. Unstructured sparsity offers a compelling solution, enabling substantial reductions in compute and memory requirements--when accelerated by compatible hardware platforms. In this paper, we conduct a scaling study to investigate the Pareto front of performance and efficiency across inference compute budgets. We find that highly sparse linear RNNs consistently achieve better efficiency-performance trade-offs than dense baselines, with 2x less compute and 36% less memory at iso-accuracy. Our models achieve state-of-the-art results on a real-time streaming task for audio denoising. By quantizing our sparse models to fixed-point arithmetic and deploying them on the Intel Loihi 2 neuromorphic chip for real-time processing, we translate model compression into tangible gains of 42x lower latency and 149x lower energy consumption compared to a dense model on an edge GPU. Our findings showcase the transformative potential of unstructured sparsity, paving the way for highly efficient recurrent neural networks in real-world, resource-constrained environments.

</details>

### Sparse Video-Gen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xi25c.html)
- **作者**: Haocheng Xi, Shuo Yang, Yilong Zhao, Chenfeng Xu, Muyang Li, Xiuyu Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Leveraging Sparsity for Sample-Efficient Preference Learning: A Theoretical Perspective.
- **链接**: [arXiv:2501.18282](https://arxiv.org/abs/2501.18282)
- **作者**: Yunzhen Yao, Lie He, Michael Gastpar
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper considers the sample-efficiency of preference learning, which models and predicts human choices based on comparative judgments. The minimax optimal estimation error rate $Θ(d/n)$ in classical estimation theory requires that the number of samples $n$ scales linearly with the dimensionality of the feature space $d$. However, the high dimensionality of the feature space and the high cost of collecting human-annotated data challenge the efficiency of traditional estimation methods. To remedy this, we leverage sparsity in the preference model and establish sharp error rates. We show that under the sparse random utility model, where the parameter of the reward function is $k$-sparse, the minimax optimal rate can be reduced to $Θ(k/n \log(d/k))$. Furthermore, we analyze the $\ell_{1}$-regularized estimator and show that it achieves near-optimal rate under mild assumptions on the Gram matrix. Experiments on synthetic data and LLM alignment data validate our theoretical findings, showing that sparsity-aware methods significantly reduce sample complexity and improve prediction accuracy.

</details>
