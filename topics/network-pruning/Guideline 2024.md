# Network Pruning — 2024 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 26 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Sparsest Models Elude Pruning: An Exposé of Pruning's Current Capabilities.
- **链接**: [arXiv:2407.04075](https://arxiv.org/abs/2407.04075)
- **作者**: Stephen Zhang, Vardan Papyan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning has emerged as a promising approach for compressing large-scale models, yet its effectiveness in recovering the sparsest of models has not yet been explored. We conducted an extensive series of 485,838 experiments, applying a range of state-of-the-art pruning algorithms to a synthetic dataset we created, named the Cubist Spiral. Our findings reveal a significant gap in performance compared to ideal sparse networks, which we identified through a novel combinatorial search algorithm. We attribute this performance gap to current pruning algorithms' poor behaviour under overparameterization, their tendency to induce disconnected paths throughout the network, and their propensity to get stuck at suboptimal solutions, even when given the optimal width and initialization. This gap is concerning, given the simplicity of the network architectures and datasets used in our study. We hope that our research encourages further investigation into new pruning techniques that strive for true network sparsity.

</details>

### Junk DNA Hypothesis: Pruning Small Pre-Trained Weights Irreversibly and Monotonically Impairs "Difficult" Downstream Tasks in LLMs.
- **链接**: [出版页](https://proceedings.mlr.press/v235/yin24b.html)
- **作者**: Lu Yin, Ajay Kumar Jaiswal, Shiwei Liu, Souvik Kundu, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity.
- **链接**: [出版页](https://proceedings.mlr.press/v235/yin24e.html)
- **作者**: Lu Yin, You Wu, Zhenyu Zhang, Cheng-Yu Hsieh, Yaqing Wang, Yiling Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### BWS: Best Window Selection Based on Sample Scores for Data Pruning across Broad Ranges.
- **链接**: [arXiv:2406.03057](https://arxiv.org/abs/2406.03057)
- **作者**: Hoyong Choi, Nohyun Ki, Hye Won Chung
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data subset selection aims to find a smaller yet informative subset of a large dataset that can approximate the full-dataset training, addressing challenges associated with training neural networks on large-scale datasets. However, existing methods tend to specialize in either high or low selection ratio regimes, lacking a universal approach that consistently achieves competitive performance across a broad range of selection ratios. We introduce a universal and efficient data subset selection method, Best Window Selection (BWS), by proposing a method to choose the best window subset from samples ordered based on their difficulty scores. This approach offers flexibility by allowing the choice of window intervals that span from easy to difficult samples. Furthermore, we provide an efficient mechanism for selecting the best window subset by evaluating its quality using kernel ridge regression. Our experimental results demonstrate the superior performance of BWS compared to other baselines across a broad range of selection ratios over datasets, including CIFAR-10/100 and ImageNet, and the scenarios involving training from random initialization or fine-tuning of pre-trained models.

</details>

### A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts.
- **链接**: [arXiv:2405.16646](https://arxiv.org/abs/2405.16646)
- **作者**: Mohammed Nowaz Rabbani Chowdhury, Meng Wang, Kaoutar El Maghraoui, Naigang Wang, Pin-Yu Chen, Christopher D. Carothers
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The sparsely gated mixture of experts (MoE) architecture sends different inputs to different subnetworks, i.e., experts, through trainable routers. MoE reduces the training computation significantly for large models, but its deployment can be still memory or computation expensive for some downstream tasks. Model pruning is a popular approach to reduce inference computation, but its application in MoE architecture is largely unexplored. To the best of our knowledge, this paper provides the first provably efficient technique for pruning experts in finetuned MoE models. We theoretically prove that prioritizing the pruning of the experts with a smaller change of the routers l2 norm from the pretrained model guarantees the preservation of test accuracy, while significantly reducing the model size and the computational requirements. Although our theoretical analysis is centered on binary classification tasks on simplified MoE architecture, our expert pruning method is verified on large vision MoE models such as VMoE and E3MoE finetuned on benchmark datasets such as CIFAR10, CIFAR100, and ImageNet.

</details>

### Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models.
- **链接**: [arXiv:2406.02924](https://arxiv.org/abs/2406.02924) · [代码](https://github.com/pprp/Pruner-Zero)
- **作者**: Peijie Dong, Lujun Li, Zhenheng Tang, Xiang Liu, Xinglin Pan, Qiang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the remarkable capabilities, Large Language Models (LLMs) face deployment challenges due to their extensive size. Pruning methods drop a subset of weights to accelerate, but many of them require retraining, which is prohibitively expensive and computationally demanding. Recently, post-training pruning approaches introduced novel metrics, enabling the pruning of LLMs without retraining. However, these metrics require the involvement of human experts and tedious trial and error. To efficiently identify superior pruning metrics, we develop an automatic framework for searching symbolic pruning metrics using genetic programming. In particular, we devise an elaborate search space encompassing the existing pruning metrics to discover the potential symbolic pruning metric. We propose an opposing operation simplification strategy to increase the diversity of the population. In this way, Pruner-Zero allows auto-generation of symbolic pruning metrics. Based on the searched results, we explore the correlation between pruning metrics and performance after pruning and summarize some principles. Extensive experiments on LLaMA and LLaMA-2 on language modeling and zero-shot tasks demonstrate that our Pruner-Zero obtains superior performance than SOTA post-training pruning methods. Code at: \url{https://github.com/pprp/Pruner-Zero}.

</details>

### A New Branch-and-Bound Pruning Framework for ℓ0-Regularized Problems.
- **链接**: [arXiv:2406.03504](https://arxiv.org/abs/2406.03504)
- **作者**: Théo Guyard, Cédric Herzet, Clément Elvira, Ayse-Nur Arslan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the resolution of learning problems involving $\ell_0$-regularization via Branch-and-Bound (BnB) algorithms. These methods explore regions of the feasible space of the problem and check whether they do not contain solutions through "pruning tests". In standard implementations, evaluating a pruning test requires to solve a convex optimization problem, which may result in computational bottlenecks. In this paper, we present an alternative to implement pruning tests for some generic family of $\ell_0$-regularized problems. Our proposed procedure allows the simultaneous assessment of several regions and can be embedded in standard BnB implementations with a negligible computational overhead. We show through numerical simulations that our pruning strategy can improve the solving time of BnB procedures by several orders of magnitude for typical problems encountered in machine-learning applications.

</details>

### PruNeRF: Segment-Centric Dataset Pruning via 3D Spatial Consistency.
- **链接**: [arXiv:2406.00798](https://arxiv.org/abs/2406.00798)
- **作者**: Yeonsung Jung, Heecheol Yun, Joonhyung Park, Jin-Hwa Kim, Eunho Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Radiance Fields (NeRF) have shown remarkable performance in learning 3D scenes. However, NeRF exhibits vulnerability when confronted with distractors in the training images -- unexpected objects are present only within specific views, such as moving entities like pedestrians or birds. Excluding distractors during dataset construction is a straightforward solution, but without prior knowledge of their types and quantities, it becomes prohibitively expensive. In this paper, we propose PruNeRF, a segment-centric dataset pruning framework via 3D spatial consistency, that effectively identifies and prunes the distractors. We first examine existing metrics for measuring pixel-wise distraction and introduce Influence Functions for more accurate measurements. Then, we assess 3D spatial consistency using a depth-based reprojection technique to obtain 3D-aware distraction. Furthermore, we incorporate segmentation for pixel-to-segment refinement, enabling more precise identification. Our experiments on benchmark datasets demonstrate that PruNeRF consistently outperforms state-of-the-art methods in robustness against distractors.

</details>

### LayerMerge: Neural Network Depth Compression through Layer Pruning and Merging.
- **链接**: [arXiv:2406.12837](https://arxiv.org/abs/2406.12837) · [代码](https://github.com/snu-mllab/LayerMerge)
- **作者**: Jinuk Kim, Marwa El Halabi, Mingi Ji, Hyun Oh Song
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works show that reducing the number of layers in a convolutional neural network can enhance efficiency while maintaining the performance of the network. Existing depth compression methods remove redundant non-linear activation functions and merge the consecutive convolution layers into a single layer. However, these methods suffer from a critical drawback; the kernel size of the merged layers becomes larger, significantly undermining the latency reduction gained from reducing the depth of the network. We show that this problem can be addressed by jointly pruning convolution layers and activation functions. To this end, we propose LayerMerge, a novel depth compression method that selects which activation layers and convolution layers to remove, to achieve a desired inference speed-up while minimizing performance loss. Since the corresponding selection problem involves an exponential search space, we formulate a novel surrogate optimization problem and efficiently solve it via dynamic programming. Empirical results demonstrate that our method consistently outperforms existing depth compression and layer pruning methods on various network architectures, both on image classification and generation tasks. We release the code at https://github.com/snu-mllab/LayerMerge.

</details>

### No Free Prune: Information-Theoretic Barriers to Pruning at Initialization.
- **链接**: [arXiv:2402.01089](https://arxiv.org/abs/2402.01089)
- **作者**: Tanishq Kumar, Kevin Luo, Mark Sellke
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The existence of "lottery tickets" arXiv:1803.03635 at or near initialization raises the tantalizing question of whether large models are necessary in deep learning, or whether sparse networks can be quickly identified and trained without ever training the dense models that contain them. However, efforts to find these sparse subnetworks without training the dense model ("pruning at initialization") have been broadly unsuccessful arXiv:2009.08576. We put forward a theoretical explanation for this, based on the model's effective parameter count, $p_\text{eff}$, given by the sum of the number of non-zero weights in the final network and the mutual information between the sparsity mask and the data. We show the Law of Robustness of arXiv:2105.12806 extends to sparse networks with the usual parameter count replaced by $p_\text{eff}$, meaning a sparse neural network which robustly interpolates noisy data requires a heavily data-dependent mask. We posit that pruning during and after training outputs masks with higher mutual information than those produced by pruning at initialization. Thus two networks may have the same sparsities, but differ in effective parameter count based on how they were trained. This suggests that pruning near initialization may be infeasible and explains why lottery tickets exist, but cannot be found fast (i.e. without training the full network). Experiments on neural networks confirm that information gained during training may indeed affect model capacity.

</details>

### Towards efficient deep spiking neural networks construction with spiking activity based pruning.
- **链接**: [arXiv:2406.01072](https://arxiv.org/abs/2406.01072)
- **作者**: Yaxin Li, Qi Xu, Jiangrong Shen, Hongming Xu, Long Chen, Gang Pan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of deep and large-scale spiking neural networks (SNNs) exhibiting high performance across diverse complex datasets has led to a need for compressing network models due to the presence of a significant number of redundant structural units, aiming to more effectively leverage their low-power consumption and biological interpretability advantages. Currently, most model compression techniques for SNNs are based on unstructured pruning of individual connections, which requires specific hardware support. Hence, we propose a structured pruning approach based on the activity levels of convolutional kernels named Spiking Channel Activity-based (SCA) network pruning framework. Inspired by synaptic plasticity mechanisms, our method dynamically adjusts the network's structure by pruning and regenerating convolutional kernels during training, enhancing the model's adaptation to the current target task. While maintaining model performance, this approach refines the network architecture, ultimately reducing computational load and accelerating the inference process. This indicates that structured dynamic sparse learning methods can better facilitate the application of deep SNNs in low-power and high-efficiency scenarios.

</details>

### COPAL: Continual Pruning in Large Language Generative Models.
- **链接**: [arXiv:2405.02347](https://arxiv.org/abs/2405.02347)
- **作者**: Srikanth Malla, Joon Hee Choi, Chiho Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adapting pre-trained large language models to different domains in natural language processing requires two key considerations: high computational demands and model's inability to continual adaptation. To simultaneously address both issues, this paper presents COPAL (COntinual Pruning in Adaptive Language settings), an algorithm developed for pruning large language generative models under a continual model adaptation setting. While avoiding resource-heavy finetuning or retraining, our pruning process is guided by the proposed sensitivity analysis. The sensitivity effectively measures model's ability to withstand perturbations introduced by the new dataset and finds model's weights that are relevant for all encountered datasets. As a result, COPAL allows seamless model adaptation to new domains while enhancing the resource efficiency. Our empirical evaluation on a various size of LLMs show that COPAL outperforms baseline models, demonstrating its efficacy in efficiency and adaptability.

</details>

### OSSCAR: One-Shot Structured Pruning in Vision and Language Models with Combinatorial Optimization.
- **链接**: [arXiv:2403.12983](https://arxiv.org/abs/2403.12983)
- **作者**: Xiang Meng, Shibal Ibrahim, Kayhan Behdin, Hussein Hazimeh, Natalia Ponomareva, Rahul Mazumder
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning is a promising approach for reducing the inference costs of large vision and language models. By removing carefully chosen structures, e.g., neurons or attention heads, the improvements from this approach can be realized on standard deep learning hardware. In this work, we focus on structured pruning in the one-shot (post-training) setting, which does not require model retraining after pruning. We propose a novel combinatorial optimization framework for this problem, based on a layer-wise reconstruction objective and a careful reformulation that allows for scalable optimization. Moreover, we design a new local combinatorial optimization algorithm, which exploits low-rank updates for efficient local search. Our framework is time and memory-efficient and considerably improves upon state-of-the-art one-shot methods on vision models (e.g., ResNet50, MobileNet) and language models (e.g., OPT-1.3B -- OPT-30B). For language models, e.g., OPT-2.7B, OSSCAR can lead to $125\times$ lower test perplexity on WikiText with $2\times$ inference time speedup in comparison to the state-of-the-art ZipLM approach. Our framework is also $6\times$ -- $8\times$ faster. Notably, our work considers models with tens of billions of parameters, which is up to $100\times$ larger than what has been previously considered in the structured pruning literature.

</details>

### Ensemble Pruning for Out-of-distribution Generalization.
- **链接**: [出版页](https://proceedings.mlr.press/v235/qiao24a.html)
- **作者**: Fengchun Qiao, Xi Peng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Exploring Intrinsic Dimension for Vision-Language Model Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wang24cp.html)
- **作者**: Hanzhang Wang, Jiawen Zhang, Qingyuan Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications.
- **链接**: [arXiv:2402.05162](https://arxiv.org/abs/2402.05162)
- **作者**: Boyi Wei, Kaixuan Huang, Yangsibo Huang, Tinghao Xie, Xiangyu Qi, Mengzhou Xia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) show inherent brittleness in their safety mechanisms, as evidenced by their susceptibility to jailbreaking and even non-malicious fine-tuning. This study explores this brittleness of safety alignment by leveraging pruning and low-rank modifications. We develop methods to identify critical regions that are vital for safety guardrails, and that are disentangled from utility-relevant regions at both the neuron and rank levels. Surprisingly, the isolated regions we find are sparse, comprising about $3\%$ at the parameter level and $2.5\%$ at the rank level. Removing these regions compromises safety without significantly impacting utility, corroborating the inherent brittleness of the model's safety mechanisms. Moreover, we show that LLMs remain vulnerable to low-cost fine-tuning attacks even when modifications to the safety-critical regions are restricted. These findings underscore the urgent need for more robust safety strategies in LLMs.

</details>

### Lightweight Image Super-Resolution via Flexible Meta Pruning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24cc.html)
- **作者**: Yulun Zhang, Kai Zhang, Luc Van Gool, Martin Danelljan, Fisher Yu
- **🏷️ 机构**: ETH Zurich
- **会议**: ICML 2024

### APT: Adaptive Pruning and Tuning Pretrained Language Models for Efficient Training and Inference.
- **链接**: [arXiv:2401.12200](https://arxiv.org/abs/2401.12200)
- **作者**: Bowen Zhao, Hannaneh Hajishirzi, Qingqing Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-tuning and inference with large Language Models (LM) are generally known to be expensive. Parameter-efficient fine-tuning over pretrained LMs reduces training memory by updating a small number of LM parameters but does not improve inference efficiency. Structured pruning improves LM inference efficiency by removing consistent parameter blocks, yet often increases training memory and time. To improve both training and inference efficiency, we introduce APT that adaptively prunes and tunes parameters for the LMs. At the early stage of fine-tuning, APT dynamically adds salient tuning parameters for fast and accurate convergence while discarding unimportant parameters for efficiency. Compared to baselines, our experiments show that APT maintains up to 98% task performance when pruning RoBERTa and T5 models with 40% parameters left while keeping 86.4% LLaMA models' performance with 70% parameters remained. Furthermore, APT speeds up LMs fine-tuning by up to 8x and reduces large LMs memory training footprint by up to 70%.

</details>

### Defense against Backdoor Attack on Pre-trained Language Models via Head Pruning and Attention Normalization.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhao24r.html)
- **作者**: Xingyi Zhao, Depeng Xu, Shuhan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Accelerating Transformer Pre-training with 2: 4 Sparsity.
- **链接**: [arXiv:2404.01847](https://arxiv.org/abs/2404.01847) · [代码](https://github.com/huyz2023/2by4-pretrain)
- **作者**: Yuezhou Hu, Kang Zhao, Weiyu Huang, Jianfei Chen, Jun Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training large transformers is slow, but recent innovations on GPU architecture give us an advantage. NVIDIA Ampere GPUs can execute a fine-grained 2:4 sparse matrix multiplication twice as fast as its dense equivalent. In the light of this property, we comprehensively investigate the feasibility of accelerating feed-forward networks (FFNs) of transformers in pre-training. First, we define a ``flip rate'' to monitor the stability of a 2:4 training process. Utilizing this metric, we propose three techniques to preserve accuracy: to modify the sparse-refined straight-through estimator by applying the masked decay term on gradients, to determine a feasible decay factor in warm-up stage, and to enhance the model's quality by a dense fine-tuning procedure near the end of pre-training. Besides, we devise two techniques to practically accelerate training: to calculate transposable 2:4 masks by convolution, and to accelerate gated activation functions by reducing GPU L2 cache miss. Experiments show that our 2:4 sparse training algorithm achieves similar convergence to dense training algorithms on several transformer pre-training tasks, while actual acceleration can be observed on different shapes of transformer block apparently. Our toolkit is available at https://github.com/huyz2023/2by4-pretrain.

</details>

### SPP: Sparsity-Preserved Parameter-Efficient Fine-Tuning for Large Language Models.
- **链接**: [arXiv:2405.16057](https://arxiv.org/abs/2405.16057) · [代码](https://github.com/Lucky-Lance/SPP)
- **作者**: Xudong Lu, Aojun Zhou, Yuhui Xu, Renrui Zhang, Peng Gao, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) have become pivotal in advancing the field of artificial intelligence, yet their immense sizes pose significant challenges for both fine-tuning and deployment. Current post-training pruning methods, while reducing the sizes of LLMs, often fail to maintain their original performance. To address these challenges, this paper introduces SPP, a Sparsity-Preserved Parameter-efficient fine-tuning method. Different from existing post-training pruning approaches that struggle with performance retention, SPP proposes to employ lightweight learnable column and row matrices to optimize sparse LLM weights, keeping the structure and sparsity of pruned pre-trained models intact. By element-wise multiplication and residual addition, SPP ensures the consistency of model sparsity pattern and ratio during both training and weight-merging processes. We demonstrate the effectiveness of SPP by applying it to the LLaMA and LLaMA-2 model families with recent post-training pruning methods. Our results show that SPP significantly enhances the performance of models with different sparsity patterns (i.e. unstructured and N:M sparsity), especially for those with high sparsity ratios (e.g. 75%), making it a promising solution for the efficient fine-tuning of sparse LLMs. Code will be made available at https://github.com/Lucky-Lance/SPP.

</details>

### SPADE: Sparsity-Guided Debugging for Deep Neural Networks.
- **链接**: [arXiv:2310.04519](https://arxiv.org/abs/2310.04519) · [代码](https://github.com/IST-DASLab/SPADE)
- **作者**: Arshia Soltani Moakhar, Eugenia Iofinova, Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It is known that sparsity can improve interpretability for deep neural networks. However, existing methods in the area either require networks that are pre-trained with sparsity constraints, or impose sparsity after the fact, altering the network's general behavior. In this paper, we demonstrate, for the first time, that sparsity can instead be incorporated into the interpretation process itself, as a sample-specific preprocessing step. Unlike previous work, this approach, which we call SPADE, does not place constraints on the trained model and does not affect its behavior during inference on the sample. Given a trained model and a target sample, SPADE uses sample-targeted pruning to provide a "trace" of the network's execution on the sample, reducing the network to the most important connections prior to computing an interpretation. We demonstrate that preprocessing with SPADE significantly increases the accuracy of image saliency maps across several interpretability methods. Additionally, SPADE improves the usefulness of neuron visualizations, aiding humans in reasoning about network behavior. Our code is available at https://github.com/IST-DASLab/SPADE.

</details>

### QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference.
- **链接**: [arXiv:2406.10774](https://arxiv.org/abs/2406.10774) · [代码](https://github.com/mit-han-lab/Quest)
- **作者**: Jiaming Tang, Yilong Zhao, Kan Zhu, Guangxuan Xiao, Baris Kasikci, Song Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As the demand for long-context large language models (LLMs) increases, models with context windows of up to 128K or 1M tokens are becoming increasingly prevalent. However, long-context LLM inference is challenging since the inference speed decreases significantly as the sequence length grows. This slowdown is primarily caused by loading a large KV cache during self-attention. Previous works have shown that a small portion of critical tokens will dominate the attention outcomes. However, we observe the criticality of a token highly depends on the query. To this end, we propose Quest, a query-aware KV cache selection algorithm. Quest keeps track of the minimal and maximal Key values in KV cache pages and estimates the criticality of a given page using Query vectors. By only loading the Top-K critical KV cache pages for attention, Quest significantly speeds up self-attention without sacrificing accuracy. We show that Quest can achieve up to 2.23x self-attention speedup, which reduces inference latency by 7.03x while performing well on tasks with long dependencies with negligible accuracy loss. Code is available at http://github.com/mit-han-lab/Quest .

</details>

### A Sparsity Principle for Partially Observable Causal Representation Learning.
- **链接**: [arXiv:2403.08335](https://arxiv.org/abs/2403.08335)
- **作者**: Danru Xu, Dingling Yao, Sébastien Lachapelle, Perouz Taslakian, Julius von Kügelgen, Francesco Locatello et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Causal representation learning aims at identifying high-level causal variables from perceptual data. Most methods assume that all latent causal variables are captured in the high-dimensional observations. We instead consider a partially observed setting, in which each measurement only provides information about a subset of the underlying causal state. Prior work has studied this setting with multiple domains or views, each depending on a fixed subset of latents. Here, we focus on learning from unpaired observations from a dataset with an instance-dependent partial observability pattern. Our main contribution is to establish two identifiability results for this setting: one for linear mixing functions without parametric assumptions on the underlying causal model, and one for piecewise linear mixing functions with Gaussian latent causal variables. Based on these insights, we propose two methods for estimating the underlying causal variables by enforcing sparsity in the inferred representation. Experiments on different simulated datasets and established benchmarks highlight the effectiveness of our approach in recovering the ground-truth latents.

</details>

### Smoothing Proximal Gradient Methods for Nonsmooth Sparsity Constrained Optimization: Optimality Conditions and Global Convergence.
- **链接**: [出版页](https://proceedings.mlr.press/v235/yuan24a.html)
- **作者**: Ganzhao Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Exploring the Benefit of Activation Sparsity in Pre-training.
- **链接**: [arXiv:2410.03440](https://arxiv.org/abs/2410.03440) · [代码](https://github.com/thunlp/moefication)
- **作者**: Zhengyan Zhang, Chaojun Xiao, Qiujieli Qin, Yankai Lin, Zhiyuan Zeng, Xu Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained Transformers inherently possess the characteristic of sparse activation, where only a small fraction of the neurons are activated for each token. While sparse activation has been explored through post-training methods, its potential in pre-training remains untapped. In this work, we first study how activation properties change during pre-training. Our examination reveals that Transformers exhibit sparse activation throughout the majority of the pre-training process while the activation correlation keeps evolving as training progresses. Leveraging this observation, we propose Switchable Sparse-Dense Learning (SSD). SSD adaptively switches between the Mixtures-of-Experts (MoE) based sparse training and the conventional dense training during the pre-training process, leveraging the efficiency of sparse training and avoiding the static activation correlation of sparse training. Compared to dense training, SSD achieves comparable performance with identical model size and reduces pre-training costs. Moreover, the models trained with SSD can be directly used as MoE models for sparse inference and achieve the same performance as dense models with up to $2\times$ faster inference speed. Codes are available at https://github.com/thunlp/moefication.

</details>
