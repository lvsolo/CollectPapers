# Network Pruning — 2021 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multi-Prize Lottery Ticket Hypothesis: Finding Accurate Binary Neural Networks by Pruning A Randomly Weighted Network.
- **链接**: [arXiv:2103.09377](https://arxiv.org/abs/2103.09377) · [代码](https://github.com/chrundle/biprop)
- **作者**: James Diffenderfer, Bhavya Kailkhura
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, Frankle & Carbin (2019) demonstrated that randomly-initialized dense networks contain subnetworks that once found can be trained to reach test accuracy comparable to the trained dense network. However, finding these high performing trainable subnetworks is expensive, requiring iterative process of training and pruning weights. In this paper, we propose (and prove) a stronger Multi-Prize Lottery Ticket Hypothesis: A sufficiently over-parameterized neural network with random weights contains several subnetworks (winning tickets) that (a) have comparable accuracy to a dense target network with learned weights (prize 1), (b) do not require any further training to achieve prize 1 (prize 2), and (c) is robust to extreme forms of quantization (i.e., binary weights and/or activation) (prize 3). This provides a new paradigm for learning compact yet highly accurate binary neural networks simply by pruning and quantizing randomly weighted full precision neural networks. We also propose an algorithm for finding multi-prize tickets (MPTs) and test it by performing a series of experiments on CIFAR-10 and ImageNet datasets. Empirical results indicate that as models grow deeper and wider, multi-prize tickets start to reach similar (and sometimes even higher) test accuracy compared to their significantly larger and full-precision counterparts that have been weight-trained. Without ever updating the weight values, our MPTs-1/32 not only set new binary weight network state-of-the-art (SOTA) Top-1 accuracy -- 94.8% on CIFAR-10 and 74.03% on ImageNet -- but also outperform their full-precision counterparts by 1.78% and 0.76%, respectively. Further, our MPT-1/1 achieves SOTA Top-1 accuracy (91.9%) for binary neural networks on CIFAR-10. Code and pre-trained models are available at: https://github.com/chrundle/biprop.

</details>

### Pruning Neural Networks at Initialization: Why Are We Missing the Mark?
- **链接**: [arXiv:2009.08576](https://arxiv.org/abs/2009.08576)
- **作者**: Jonathan Frankle, Gintare Karolina Dziugaite, Daniel M. Roy, Michael Carbin
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work has explored the possibility of pruning neural networks at initialization. We assess proposals for doing so: SNIP (Lee et al., 2019), GraSP (Wang et al., 2020), SynFlow (Tanaka et al., 2020), and magnitude pruning. Although these methods surpass the trivial baseline of random pruning, they remain below the accuracy of magnitude pruning after training, and we endeavor to understand why. We show that, unlike pruning after training, randomly shuffling the weights these methods prune within each layer or sampling new initial values preserves or improves accuracy. As such, the per-weight pruning decisions made by these methods can be replaced by a per-layer choice of the fraction of weights to prune. This property suggests broader challenges with the underlying pruning heuristics, the desire to prune at initialization, or both.

</details>

### Robust Pruning at Initialization.
- **链接**: [出版页](https://openreview.net/forum?id=vXj_ucZQ4hA)
- **作者**: Soufiane Hayou, Jean-Francois Ton, Arnaud Doucet, Yee Whye Teh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Network Pruning That Matters: A Case Study on Retraining Variants.
- **链接**: [arXiv:2105.03193](https://arxiv.org/abs/2105.03193)
- **作者**: Duong H. Le, Binh-Son Hua
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Network pruning is an effective method to reduce the computational expense of over-parameterized neural networks for deployment on low-resource systems. Recent state-of-the-art techniques for retraining pruned networks such as weight rewinding and learning rate rewinding have been shown to outperform the traditional fine-tuning technique in recovering the lost accuracy (Renda et al., 2020), but so far it is unclear what accounts for such performance. In this work, we conduct extensive experiments to verify and analyze the uncanny effectiveness of learning rate rewinding. We find that the reason behind the success of learning rate rewinding is the usage of a large learning rate. Similar phenomenon can be observed in other learning rate schedules that involve large learning rates, e.g., the 1-cycle learning rate schedule (Smith et al., 2019). By leveraging the right learning rate schedule in retraining, we demonstrate a counter-intuitive phenomenon in that randomly pruned networks could even achieve better performance than methodically pruned networks (fine-tuned with the conventional approach). Our results emphasize the cruciality of the learning rate schedule in pruned network retraining - a detail often overlooked by practitioners during the implementation of network pruning. One-sentence Summary: We study the effective of different retraining mechanisms while doing pruning

</details>

### Layer-adaptive Sparsity for the Magnitude-based Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=H6ATjJ0TKdf)
- **作者**: Jaeho Lee, Sejun Park, Sangwoo Mo, Sungsoo Ahn, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### A Gradient Flow Framework For Analyzing Network Pruning.
- **链接**: [arXiv:2009.11839](https://arxiv.org/abs/2009.11839) · [代码](https://github.com/EkdeepSLubana/flowandprune)
- **作者**: Ekdeep Singh Lubana, Robert P. Dick
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent network pruning methods focus on pruning models early-on in training. To estimate the impact of removing a parameter, these methods use importance measures that were originally designed to prune trained models. Despite lacking justification for their use early-on in training, such measures result in surprisingly low accuracy loss. To better explain this behavior, we develop a general framework that uses gradient flow to unify state-of-the-art importance measures through the norm of model parameters. We use this framework to determine the relationship between pruning measures and evolution of model parameters, establishing several results related to pruning models early-on in training: (i) magnitude-based pruning removes parameters that contribute least to reduction in loss, resulting in models that converge faster than magnitude-agnostic methods; (ii) loss-preservation based pruning preserves first-order model evolution dynamics and is therefore appropriate for pruning minimally trained models; and (iii) gradient-norm based pruning affects second-order model evolution dynamics, such that increasing gradient norm via pruning can produce poorly performing models. We validate our claims on several VGG-13, MobileNet-V1, and ResNet-56 models trained on CIFAR-10/CIFAR-100. Code available at https://github.com/EkdeepSLubana/flowandprune.

</details>

### ChipNet: Budget-Aware Pruning with Heaviside Continuous Approximations.
- **链接**: [arXiv:2102.07156](https://arxiv.org/abs/2102.07156)
- **作者**: Rishabh Tiwari, Udbhav Bamba, Arnav Chavan, Deepak K. Gupta
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structured pruning methods are among the effective strategies for extracting small resource-efficient convolutional neural networks from their dense counterparts with minimal loss in accuracy. However, most existing methods still suffer from one or more limitations, that include 1) the need for training the dense model from scratch with pruning-related parameters embedded in the architecture, 2) requiring model-specific hyperparameter settings, 3) inability to include budget-related constraint in the training process, and 4) instability under scenarios of extreme pruning. In this paper, we present ChipNet, a deterministic pruning strategy that employs continuous Heaviside function and a novel crispness loss to identify a highly sparse network out of an existing dense network. Our choice of continuous Heaviside function is inspired by the field of design optimization, where the material distribution task is posed as a continuous optimization problem, but only discrete values (0 or 1) are practically feasible and expected as final outcomes. Our approach's flexible design facilitates its use with different choices of budget constraints while maintaining stability for very low target budgets. Experimental results show that ChipNet outperforms state-of-the-art structured pruning methods by remarkable margins of up to 16.1% in terms of accuracy. Further, we show that the masks obtained with ChipNet are transferable across datasets. For certain cases, it was observed that masks transferred from a model trained on feature-rich teacher dataset provide better performance on the student dataset than those obtained by directly pruning on the student data itself.

</details>

### Neural Pruning via Growing Regularization.
- **链接**: [arXiv:2012.09243](https://arxiv.org/abs/2012.09243) · [代码](https://github.com/mingsuntse/regularization-pruning)
- **作者**: Huan Wang, Can Qin, Yulun Zhang, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Regularization has long been utilized to learn sparsity in deep neural network pruning. However, its role is mainly explored in the small penalty strength regime. In this work, we extend its application to a new scenario where the regularization grows large gradually to tackle two central problems of pruning: pruning schedule and weight importance scoring. (1) The former topic is newly brought up in this work, which we find critical to the pruning performance while receives little research attention. Specifically, we propose an L2 regularization variant with rising penalty factors and show it can bring significant accuracy gains compared with its one-shot counterpart, even when the same weights are removed. (2) The growing penalty scheme also brings us an approach to exploit the Hessian information for more accurate pruning without knowing their specific values, thus not bothered by the common Hessian approximation problems. Empirically, the proposed algorithms are easy to implement and scalable to large datasets and networks in both structured and unstructured pruning. Their effectiveness is demonstrated with modern deep neural networks on the CIFAR and ImageNet datasets, achieving competitive results compared to many state-of-the-art algorithms. Our code and trained models are publicly available at https://github.com/mingsuntse/regularization-pruning.

</details>

### Learning a Latent Simplex in Input Sparsity Time.
- **链接**: [出版页](https://openreview.net/forum?id=04LZCAxMSco)
- **作者**: Ainesh Bakshi, Chiranjib Bhattacharyya, Ravi Kannan, David P. Woodruff, Samson Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### A Discriminative Gaussian Mixture Model with Sparsity.
- **链接**: [出版页](https://openreview.net/forum?id=-_Zp7r2-cGK)
- **作者**: Hideaki Hayashi, Seiichi Uchida
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Understanding the effects of data parallelism and sparsity on neural network training.
- **链接**: [出版页](https://openreview.net/forum?id=rsogjAnYs4z)
- **作者**: Namhoon Lee, Thalaiyasingam Ajanthan, Philip H. S. Torr, Martin Jaggi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### BSQ: Exploring Bit-Level Sparsity for Mixed-Precision Neural Network Quantization.
- **链接**: [arXiv:2102.10462](https://arxiv.org/abs/2102.10462)
- **作者**: Huanrui Yang, Lin Duan, Yiran Chen, Hai Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixed-precision quantization can potentially achieve the optimal tradeoff between performance and compression rate of deep neural networks, and thus, have been widely investigated. However, it lacks a systematic method to determine the exact quantization scheme. Previous methods either examine only a small manually-designed search space or utilize a cumbersome neural architecture search to explore the vast search space. These approaches cannot lead to an optimal quantization scheme efficiently. This work proposes bit-level sparsity quantization (BSQ) to tackle the mixed-precision quantization from a new angle of inducing bit-level sparsity. We consider each bit of quantized weights as an independent trainable variable and introduce a differentiable bit-sparsity regularizer. BSQ can induce all-zero bits across a group of weight elements and realize the dynamic precision reduction, leading to a mixed-precision quantization scheme of the original model. Our method enables the exploration of the full mixed-precision space with a single gradient-based optimization process, with only one hyperparameter to tradeoff the performance and compression. BSQ achieves both higher accuracy and higher bit reduction on various model architectures on the CIFAR-10 and ImageNet datasets comparing to previous methods.

</details>
