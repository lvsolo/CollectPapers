# Network Pruning — 2022 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 26 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### VTC-LFC: Vision Transformer Compression with Low-Frequency Components.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5a8177df23bdcc15a02a6739f5b9dd4a-Abstract-Conference.html)
- **作者**: Zhenyu Wang, Hao Luo, Pichao Wang, Feng Ding, Fan Wang, Hao Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### SAViT: Structure-Aware Vision Transformer Pruning via Collaborative Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/3b11c5cc84b6da2838db348b37dbd1a2-Abstract-Conference.html)
- **作者**: Chuanyang Zheng, Zheyang Li, Kai Zhang, Zhi Yang, Wenming Tan, Jun Xiao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Recall Distortion in Neural Network Pruning and the Undecayed Pruning Algorithm.
- **链接**: [arXiv:2206.02976](https://arxiv.org/abs/2206.02976) · 📚 被引 2
- **作者**: Aidan Good, Jiaqi Lin, Xin Yu, Hannah Sieg, Mikey Ferguson, Shandian Zhe et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning techniques have been successfully used in neural networks to trade accuracy for sparsity. However, the impact of network pruning is not uniform: prior work has shown that the recall for underrepresented classes in a dataset may be more negatively affected. In this work, we study such relative distortions in recall by hypothesizing an intensification effect that is inherent to the model. Namely, that pruning makes recall relatively worse for a class with recall below accuracy and, conversely, that it makes recall relatively better for a class with recall above accuracy. In addition, we propose a new pruning algorithm aimed at attenuating such effect. Through statistical analysis, we have observed that intensification is less severe with our algorithm but nevertheless more pronounced with relatively more difficult tasks, less complex models, and higher pruning ratios. More surprisingly, we conversely observe a de-intensification effect with lower pruning ratios, which indicates that moderate pruning may have a corrective effect to such distortions.

</details>

### Pruning has a disparate impact on model accuracy.
- **链接**: [arXiv:2205.13574](https://arxiv.org/abs/2205.13574) · 📚 被引 6
- **作者**: Cuong Tran, Ferdinando Fioretto, Jung-Eun Kim, Rakshit Naidu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Network pruning is a widely-used compression technique that is able to significantly scale down overparameterized models with minimal loss of accuracy. This paper shows that pruning may create or exacerbate disparate impacts. The paper sheds light on the factors to cause such disparities, suggesting differences in gradient norms and distance to decision boundary across groups to be responsible for this critical issue. It analyzes these factors in detail, providing both theoretical and empirical support, and proposes a simple, yet effective, solution that mitigates the disparate impacts caused by pruning.

</details>

### Sparse Probabilistic Circuits via Pruning and Growing.
- **链接**: [arXiv:2211.12551](https://arxiv.org/abs/2211.12551) · 📚 被引 5
- **作者**: Meihua Dang, Anji Liu, Guy Van den Broeck
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Probabilistic circuits (PCs) are a tractable representation of probability distributions allowing for exact and efficient computation of likelihoods and marginals. There has been significant recent progress on improving the scale and expressiveness of PCs. However, PC training performance plateaus as model size increases. We discover that most capacity in existing large PC structures is wasted: fully-connected parameter layers are only sparsely used. We propose two operations: pruning and growing, that exploit the sparsity of PC structures. Specifically, the pruning operation removes unimportant sub-networks of the PC for model compression and comes with theoretical guarantees. The growing operation increases model capacity by increasing the size of the latent space. By alternatingly applying pruning and growing, we increase the capacity that is meaningfully used, allowing us to significantly scale up PC learning. Empirically, our learner achieves state-of-the-art likelihoods on MNIST-family image datasets and on Penn Tree Bank language data compared to other PC learners and less tractable deep generative models such as flow-based models and variational autoencoders (VAEs).

</details>

### Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning.
- **链接**: [arXiv:2208.11580](https://arxiv.org/abs/2208.11580) · 📚 被引 23
- **作者**: Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of model compression for deep neural networks (DNNs) in the challenging one-shot/post-training setting, in which we are given an accurate trained model, and must compress it without any retraining, based only on a small amount of calibration input data. This problem has become popular in view of the emerging software and hardware support for executing models compressed via pruning and/or quantization with speedup, and well-performing solutions have been proposed independently for both compression approaches. In this paper, we introduce a new compression framework which covers both weight pruning and quantization in a unified setting, is time- and space-efficient, and considerably improves upon the practical performance of existing post-training methods. At the technical level, our approach is based on an exact and efficient realization of the classical Optimal Brain Surgeon (OBS) framework of [LeCun, Denker, and Solla, 1990] extended to also cover weight quantization at the scale of modern DNNs. From the practical perspective, our experimental results show that it can improve significantly upon the compression-accuracy trade-offs of existing post-training methods, and that it can enable the accurate compound application of both pruning and quantization in a post-training setting.

</details>

### Data-Efficient Structured Pruning via Submodular Optimization.
- **链接**: [arXiv:2203.04940](https://arxiv.org/abs/2203.04940) · 📚 被引 2
- **作者**: Marwa El Halabi, Suraj Srinivas, Simon Lacoste-Julien
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning is an effective approach for compressing large pre-trained neural networks without significantly affecting their performance. However, most current structured pruning methods do not provide any performance guarantees, and often require fine-tuning, which makes them inapplicable in the limited-data regime. We propose a principled data-efficient structured pruning method based on submodular optimization. In particular, for a given layer, we select neurons/channels to prune and corresponding new weights for the next layer, that minimize the change in the next layer's input induced by pruning. We show that this selection problem is a weakly submodular maximization problem, thus it can be provably approximated using an efficient greedy algorithm. Our method is guaranteed to have an exponentially decreasing error between the original model and the pruned model outputs w.r.t the pruned size, under reasonable assumptions. It is also one of the few methods in the literature that uses only a limited-number of training data and no labels. Our experimental results demonstrate that our method outperforms state-of-the-art methods in the limited-data regime.

</details>

### Pruning's Effect on Generalization Through the Lens of Training and Regularization.
- **链接**: [arXiv:2210.13738](https://arxiv.org/abs/2210.13738) · 📚 被引 3
- **作者**: Tian Jin, Michael Carbin, Daniel M. Roy, Jonathan Frankle, Gintare Karolina Dziugaite
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Practitioners frequently observe that pruning improves model generalization. A long-standing hypothesis based on bias-variance trade-off attributes this generalization improvement to model size reduction. However, recent studies on over-parameterization characterize a new model size regime, in which larger models achieve better generalization. Pruning models in this over-parameterized regime leads to a contradiction -- while theory predicts that reducing model size harms generalization, pruning to a range of sparsities nonetheless improves it. Motivated by this contradiction, we re-examine pruning's effect on generalization empirically. We show that size reduction cannot fully account for the generalization-improving effect of standard pruning algorithms. Instead, we find that pruning leads to better training at specific sparsities, improving the training loss over the dense model. We find that pruning also leads to additional regularization at other sparsities, reducing the accuracy degradation due to noisy examples over the dense model. Pruning extends model training time and reduces model size. These two factors improve training and add regularization respectively. We empirically demonstrate that both factors are essential to fully explaining pruning's impact on generalization.

</details>

### A Fast Post-Training Pruning Framework for Transformers.
- **链接**: [arXiv:2204.09656](https://arxiv.org/abs/2204.09656) · 📚 被引 6
- **作者**: Woosuk Kwon, Sehoon Kim, Michael W. Mahoney, Joseph Hassoun, Kurt Keutzer, Amir Gholami
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pruning is an effective way to reduce the huge inference cost of Transformer models. However, prior work on pruning Transformers requires retraining the models. This can add high training cost and high complexity to model deployment, making it difficult to use in many practical situations. To address this, we propose a fast post-training pruning framework for Transformers that does not require any retraining. Given a resource constraint and a sample dataset, our framework automatically prunes the Transformer model using structured sparsity methods. To retain high accuracy without retraining, we introduce three novel techniques: (i) a lightweight mask search algorithm that finds which heads and filters to prune based on the Fisher information; (ii) mask rearrangement that complements the search algorithm; and (iii) mask tuning that reconstructs the output activations for each layer. We apply our method to BERT-base and DistilBERT, and we evaluate its effectiveness on GLUE and SQuAD benchmarks. Our framework achieves up to 2.0x reduction in FLOPs and 1.56x speedup in inference latency, while maintaining < 1% loss in accuracy. Importantly, our framework prunes Transformers in less than 3 minutes on a single GPU, which is over two orders of magnitude faster than existing pruning approaches that retrain the models.

</details>

### Robust Binary Models by Pruning Randomly-initialized Networks.
- **链接**: [arXiv:2202.01341](https://arxiv.org/abs/2202.01341) · 📚 被引 1
- **作者**: Chen Liu, Ziqi Zhao, Sabine Süsstrunk, Mathieu Salzmann
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robustness to adversarial attacks was shown to require a larger model capacity, and thus a larger memory footprint. In this paper, we introduce an approach to obtain robust yet compact models by pruning randomly-initialized binary networks. Unlike adversarial training, which learns the model parameters, we initialize the model parameters as either +1 or -1, keep them fixed, and find a subnetwork structure that is robust to attacks. Our method confirms the Strong Lottery Ticket Hypothesis in the presence of adversarial attacks, and extends this to binary networks. Furthermore, it yields more compact networks with competitive performance than existing works by 1) adaptively pruning different network layers; 2) exploiting an effective binary initialization scheme; 3) incorporating a last batch normalization layer to improve training stability. Our experiments demonstrate that our approach not only always outperforms the state-of-the-art robust binary networks, but also can achieve accuracy better than full-precision ones on some datasets. Finally, we show the structured patterns of our pruned binary networks.

</details>

### Structural Pruning via Latency-Saliency Knapsack.
- **链接**: [arXiv:2210.06659](https://arxiv.org/abs/2210.06659) · 📚 被引 2
- **作者**: Maying Shen, Hongxu Yin, Pavlo Molchanov, Lei Mao, Jianna Liu, José M. Álvarez
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structural pruning can simplify network architecture and improve inference speed. We propose Hardware-Aware Latency Pruning (HALP) that formulates structural pruning as a global resource allocation optimization problem, aiming at maximizing the accuracy while constraining latency under a predefined budget on targeting device. For filter importance ranking, HALP leverages latency lookup table to track latency reduction potential and global saliency score to gauge accuracy drop. Both metrics can be evaluated very efficiently during pruning, allowing us to reformulate global structural pruning under a reward maximization problem given target constraint. This makes the problem solvable via our augmented knapsack solver, enabling HALP to surpass prior work in pruning efficacy and accuracy-efficiency trade-off. We examine HALP on both classification and detection tasks, over varying networks, on ImageNet and VOC datasets, on different platforms. In particular, for ResNet-50/-101 pruning on ImageNet, HALP improves network throughput by $1.60\times$/$1.90\times$ with $+0.3\%$/$-0.2\%$ top-1 accuracy changes, respectively. For SSD pruning on VOC, HALP improves throughput by $1.94\times$ with only a $0.56$ mAP drop. HALP consistently outperforms prior art, sometimes by large margins. Project page at https://halp-neurips.github.io/.

</details>

### Beyond neural scaling laws: beating power law scaling via data pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7b75da9b61eda40fa35453ee5d077df6-Abstract-Conference.html) · 📚 被引 31
- **作者**: Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, Ari Morcos
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Pruning Neural Networks via Coresets and Convex Geometry: Towards No Assumptions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/f7fc38fdd95fd146a471791b93ff9f12-Abstract-Conference.html) · 📚 被引 1
- **作者**: Murad Tukan, Loay Mualem, Alaa Maalouf
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Advancing Model Pruning via Bi-level Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/749252feedd44f7f10d47ec1d674a2f8-Abstract-Conference.html) · 📚 被引 5
- **作者**: Yihua Zhang, Yuguang Yao, Parikshit Ram, Pu Zhao, Tianlong Chen, Mingyi Hong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Learning Best Combination for Efficient N: M Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/06589ec9d86876508600a678f9c8f51d-Abstract-Conference.html)
- **作者**: Yuxin Zhang, Mingbao Lin, Zhihang Lin, Yiting Luo, Ke Li, Fei Chao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Accelerated Projected Gradient Algorithms for Sparsity Constrained Optimization Problems.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/aab3003c922e0fcd2fd2c951fa3c03ad-Abstract-Conference.html) · 📚 被引 1
- **作者**: Jan Harold Alcantara, Ching-pei Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Sparsity in Continuous-Depth Neural Networks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/0626822954674a06ccd9c234e3f0d572-Abstract-Conference.html) · 📚 被引 2
- **作者**: Hananeh Aliee, Till Richter, Mikhail Solonin, Ignacio Ibarra, Fabian J. Theis, Niki Kilbertus
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Transformers meet Stochastic Block Models: Attention with Data-Adaptive Sparsity and Cost.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9c93b3cd3bc60c0fe7b0c2d74a2da966-Abstract-Conference.html) · 📚 被引 2
- **作者**: Sungjun Cho, Seonwoo Min, Jinwoo Kim, Moontae Lee, Honglak Lee, Seunghoon Hong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Controlled Sparsity via Constrained Optimization or: How I Learned to Stop Tuning Penalties and Love Constraints.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/089b592cccfafdca8e0178e85b609f19-Abstract-Conference.html) · 📚 被引 5
- **作者**: Jose Gallego-Posada, Juan Ramirez, Akram Erraqabi, Yoshua Bengio, Simon Lacoste-Julien
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Feature Learning in $L_2$-regularized DNNs: Attraction/Repulsion and Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/2d2f85c0f93e69cf71f58eebaebb5e8d-Abstract-Conference.html) · 📚 被引 2
- **作者**: Arthur Jacot, Eugene A. Golikov, Clément Hongler, Franck Gabriel
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Spartan: Differentiable Sparsity via Regularized Transportation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/1afb9ca4adf1d9cb3c87ff3e22a29049-Abstract-Conference.html) · 📚 被引 0
- **作者**: Kai Sheng Tai, Tai-Peng Tian, Ser Nam Lim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Accelerating Sparse Convolution with Column Vector-Wise Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/c383e44d9a878d1982d9abb838bd5d8a-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yijun Tan, Kai Han, Kang Zhao, Xianzhi Yu, Zidong Du, Yunji Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### SInGE: Sparsity via Integrated Gradients Estimation of Neuron Relevance.
- **链接**: [arXiv:2207.04089](https://arxiv.org/abs/2207.04089) · 📚 被引 0
- **作者**: Edouard Yvinec, Arnaud Dapogny, Matthieu Cord, Kevin Bailly
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The leap in performance in state-of-the-art computer vision methods is attributed to the development of deep neural networks. However it often comes at a computational price which may hinder their deployment. To alleviate this limitation, structured pruning is a well known technique which consists in removing channels, neurons or filters, and is commonly applied in order to produce more compact models. In most cases, the computations to remove are selected based on a relative importance criterion. At the same time, the need for explainable predictive models has risen tremendously and motivated the development of robust attribution methods that highlight the relative importance of pixels of an input image or feature map. In this work, we discuss the limitations of existing pruning heuristics, among which magnitude and gradient-based methods. We draw inspiration from attribution methods to design a novel integrated gradient pruning criterion, in which the relevance of each neuron is defined as the integral of the gradient variation on a path towards this neuron removal. Furthermore, we propose an entwined DNN pruning and fine-tuning flowchart to better preserve DNN accuracy while removing parameters. We show through extensive validation on several datasets, architectures as well as pruning scenarios that the proposed method, dubbed SInGE, significantly outperforms existing state-of-the-art DNN pruning methods.

</details>

### On the Identifiability of Nonlinear ICA: Sparsity and Beyond.
- **链接**: [arXiv:2206.07751](https://arxiv.org/abs/2206.07751) · 📚 被引 2
- **作者**: Yujia Zheng, Ignavier Ng, Kun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Nonlinear independent component analysis (ICA) aims to recover the underlying independent latent sources from their observable nonlinear mixtures. How to make the nonlinear ICA model identifiable up to certain trivial indeterminacies is a long-standing problem in unsupervised learning. Recent breakthroughs reformulate the standard independence assumption of sources as conditional independence given some auxiliary variables (e.g., class labels and/or domain/time indexes) as weak supervision or inductive bias. However, nonlinear ICA with unconditional priors cannot benefit from such developments. We explore an alternative path and consider only assumptions on the mixing process, such as Structural Sparsity. We show that under specific instantiations of such constraints, the independent latent sources can be identified from their nonlinear mixtures up to a permutation and a component-wise transformation, thus achieving nontrivial identifiability of nonlinear ICA without auxiliary variables. We provide estimation methods and validate the theoretical results experimentally. The results on image data suggest that our conditions may hold in a number of practical data generating processes.

</details>

### Geometric Knowledge Distillation: Topology Compression for Graph Neural Networks.
- **链接**: [arXiv:2210.13014](https://arxiv.org/abs/2210.13014) · 📚 被引 6
- **作者**: Chenxiao Yang, Qitian Wu, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Spatial Pruned Sparse Convolution for Efficient 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
