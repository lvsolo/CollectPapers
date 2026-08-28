# Network Pruning — 2023 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### One Less Reason for Filter Pruning: Gaining Free Adversarial Robustness with Structured Grouped Kernel Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/c3aba4234afd1c8116d879ba183f4835-Abstract-Conference.html) · 📚 被引 0
- **作者**: Shaochen (Henry) Zhong, Zaichuan You, Jiamu Zhang, Sebastian Zhao, Zachary LeClaire, Zirui Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Dynamic Context Pruning for Efficient and Interpretable Autoregressive Transformers.
- **链接**: [arXiv:2305.15805](https://arxiv.org/abs/2305.15805) · 📚 被引 9
- **作者**: Sotiris Anagnostidis, Dario Pavllo, Luca Biggio, Lorenzo Noci, Aurélien Lucchi, Thomas Hofmann
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autoregressive Transformers adopted in Large Language Models (LLMs) are hard to scale to long sequences. Despite several works trying to reduce their computational cost, most of LLMs still adopt attention layers between all pairs of tokens in the sequence, thus incurring a quadratic cost. In this study, we present a novel approach that dynamically prunes contextual information while preserving the model's expressiveness, resulting in reduced memory and computational requirements during inference. Our method employs a learnable mechanism that determines which uninformative tokens can be dropped from the context at any point across the generation process. By doing so, our approach not only addresses performance concerns but also enhances interpretability, providing valuable insight into the model's decision-making process. Our technique can be applied to existing pre-trained models through a straightforward fine-tuning process, and the pruning strength can be specified by a sparsity parameter. Notably, our empirical findings demonstrate that we can effectively prune up to 80\% of the context without significant performance degradation on downstream tasks, offering a valuable tool for mitigating inference costs. Our reference implementation achieves up to $2\times$ increase in inference throughput and even greater memory savings.

</details>

### Optimal Parameter and Neuron Pruning for Out-of-Distribution Detection.
- **链接**: [arXiv:2402.10062](https://arxiv.org/abs/2402.10062) · 📚 被引 1
- **作者**: Chao Chen, Zhihang Fu, Kai Liu, Ze Chen, Mingyuan Tao, Jieping Ye
- **🏷️ 机构**:  Alibaba / Zhejiang Lab
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> For a machine learning model deployed in real world scenarios, the ability of detecting out-of-distribution (OOD) samples is indispensable and challenging. Most existing OOD detection methods focused on exploring advanced training skills or training-free tricks to prevent the model from yielding overconfident confidence score for unknown samples. The training-based methods require expensive training cost and rely on OOD samples which are not always available, while most training-free methods can not efficiently utilize the prior information from the training data. In this work, we propose an \textbf{O}ptimal \textbf{P}arameter and \textbf{N}euron \textbf{P}runing (\textbf{OPNP}) approach, which aims to identify and remove those parameters and neurons that lead to over-fitting. The main method is divided into two steps. In the first step, we evaluate the sensitivity of the model parameters and neurons by averaging gradients over all training samples. In the second step, the parameters and neurons with exceptionally large or close to zero sensitivities are removed for prediction. Our proposal is training-free, compatible with other post-hoc methods, and exploring the information from all training data. Extensive experiments are performed on multiple OOD detection tasks and model architectures, showing that our proposed OPNP consistently outperforms the existing methods by a large margin.

</details>

### PDP: Parameter-free Differentiable Pruning is All You Need.
- **链接**: [arXiv:2305.11203](https://arxiv.org/abs/2305.11203) · 📚 被引 1
- **作者**: Minsik Cho, Saurabh Adya, Devang Naik
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DNN pruning is a popular way to reduce the size of a model, improve the inference latency, and minimize the power consumption on DNN accelerators. However, existing approaches might be too complex, expensive or ineffective to apply to a variety of vision/language tasks, DNN architectures and to honor structured pruning constraints. In this paper, we propose an efficient yet effective train-time pruning scheme, Parameter-free Differentiable Pruning (PDP), which offers state-of-the-art qualities in model size, accuracy, and training cost. PDP uses a dynamic function of weights during training to generate soft pruning masks for the weights in a parameter-free manner for a given pruning target. While differentiable, the simplicity and efficiency of PDP make it universal enough to deliver state-of-the-art random/structured/channel pruning results on various vision and natural language tasks. For example, for MobileNet-v1, PDP can achieve 68.2% top-1 ImageNet1k accuracy at 86.6% sparsity, which is 1.7% higher accuracy than those from the state-of-the-art algorithms. Also, PDP yields over 83.1% accuracy on Multi-Genre Natural Language Inference with 90% sparsity for BERT, while the next best from the existing techniques shows 81.5% accuracy. In addition, PDP can be applied to structured pruning, such as N:M pruning and channel pruning. For 1:4 structured pruning of ResNet18, PDP improved the top-1 ImageNet1k accuracy by over 3.6% over the state-of-the-art. For channel pruning of ResNet50, PDP reduced the top-1 ImageNet1k accuracy by 0.6% from the state-of-the-art.

</details>

### Structural Pruning for Diffusion Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/35c1d69d23bb5dd6b9abcd68be005d5c-Abstract-Conference.html) · 📚 被引 26
- **作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### You Only Condense Once: Two Rules for Pruning Condensed Datasets.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/7bdd36a198a8408f444834039b09f518-Abstract-Conference.html) · 📚 被引 8
- **作者**: Yang He, Lingao Xiao, Joey Tianyi Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### ZipLM: Inference-Aware Structured Pruning of Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/ced46a50befedcb884ccf0cbe8c3ad23-Abstract-Conference.html) · 📚 被引 2
- **作者**: Eldar Kurtic, Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Pruning vs Quantization: Which is Better?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/c48bc80aa5d3cbbdd712d1cc107b8319-Abstract-Conference.html) · 📚 被引 14
- **作者**: Andrey Kuzmin, Markus Nagel, Mart van Baalen, Arash Behboodi, Tijmen Blankevoort
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CAP: Correlation-Aware Pruning for Highly-Accurate Sparse Vision Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5bd9fbb3a5a985f80c16ddd0ec1dfc43-Abstract-Conference.html) · 📚 被引 1
- **作者**: Denis Kuznedelev, Eldar Kurtic, Elias Frantar, Dan Alistarh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### LLM-Pruner: On the Structural Pruning of Large Language Models.
- **链接**: [arXiv:2305.11627](https://arxiv.org/abs/2305.11627) · [代码](https://github.com/horseee/LLM-Pruner) · 📚 被引 88
- **作者**: Xinyin Ma, Gongfan Fang, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have shown remarkable capabilities in language understanding and generation. However, such impressive capability typically comes with a substantial model size, which presents significant challenges in both the deployment, inference, and training stages. With LLM being a general-purpose task solver, we explore its compression in a task-agnostic manner, which aims to preserve the multi-task solving and language generation ability of the original LLM. One challenge to achieving this is the enormous size of the training corpus of LLM, which makes both data transfer and model post-training over-burdensome. Thus, we tackle the compression of LLMs within the bound of two constraints: being task-agnostic and minimizing the reliance on the original training dataset. Our method, named LLM-Pruner, adopts structural pruning that selectively removes non-critical coupled structures based on gradient information, maximally preserving the majority of the LLM's functionality. To this end, the performance of pruned models can be efficiently recovered through tuning techniques, LoRA, in merely 3 hours, requiring only 50K data. We validate the LLM-Pruner on three LLMs, including LLaMA, Vicuna, and ChatGLM, and demonstrate that the compressed models still exhibit satisfactory capabilities in zero-shot classification and generation. The code is available at: https://github.com/horseee/LLM-Pruner

</details>

### Robust Data Pruning under Label Noise via Maximizing Re-labeling Accuracy.
- **链接**: [arXiv:2311.01002](https://arxiv.org/abs/2311.01002) · 📚 被引 2
- **作者**: Dongmin Park, Seola Choi, Doyoung Kim, Hwanjun Song, Jae-Gil Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data pruning, which aims to downsize a large training set into a small informative subset, is crucial for reducing the enormous computational costs of modern deep learning. Though large-scale data collections invariably contain annotation noise and numerous robust learning methods have been developed, data pruning for the noise-robust learning scenario has received little attention. With state-of-the-art Re-labeling methods that self-correct erroneous labels while training, it is challenging to identify which subset induces the most accurate re-labeling of erroneous labels in the entire training set. In this paper, we formalize the problem of data pruning with re-labeling. We first show that the likelihood of a training example being correctly re-labeled is proportional to the prediction confidence of its neighborhood in the subset. Therefore, we propose a novel data pruning algorithm, Prune4Rel, that finds a subset maximizing the total neighborhood confidence of all training examples, thereby maximizing the re-labeling accuracy and generalization performance. Extensive experiments on four real and one synthetic noisy datasets show that \algname{} outperforms the baselines with Re-labeling models by up to 9.1% as well as those with a standard model by up to 21.6%.

</details>

### Neural Sculpting: Uncovering hierarchically modular task structure in neural networks through pruning and network analysis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3b1675de6b49cc00084374213f8c38ae-Abstract-Conference.html) · 📚 被引 1
- **作者**: Shreyas Malakarjun Patil, Loizos Michael, Constantine Dovrolis
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Towards Data-Agnostic Pruning At Initialization: What Makes a Good Sparse Mask?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fd5013ea0c3f96931dec77174eaf9d80-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hoang Pham, The-Anh Ta, Shiwei Liu, Lichuan Xiang, Dung Le, Hongkai Wen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Greedy Pruning with Group Lasso Provably Generalizes for Matrix Sensing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/bd2107343c9cc973635d90dbfc122223-Abstract-Conference.html) · 📚 被引 0
- **作者**: Nived Rajaraman, Devvrit, Aryan Mokhtari, Kannan Ramchandran
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Data Pruning via Moving-one-Sample-out.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3abe23bf7e295b44369c24465d68987a-Abstract-Conference.html) · 📚 被引 8
- **作者**: Haoru Tan, Sitong Wu, Fei Du, Yukang Chen, Zhibin Wang, Fan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Towards Higher Ranks via Adversarial Weight Pruning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/040ace837dd270a87055bb10dd7c0392-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yuchuan Tian, Hanting Chen, Tianyu Guo, Chao Xu, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### SUBP: Soft Uniform Block Pruning for 1×N Sparse CNNs Multithreading Acceleration.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a36c3dbe676fa8445715a31a90c66ab3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jingyang Xiang, Siqi Li, Jun Chen, Guang Dai, Shipeng Bai, Yukai Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Selectivity Drives Productivity: Efficient Dataset Pruning for Enhanced Transfer Learning.
- **链接**: [arXiv:2310.08782](https://arxiv.org/abs/2310.08782) · [代码](https://github.com/OPTML-Group/DP4TL) · 📚 被引 2
- **作者**: Yihua Zhang, Yimeng Zhang, Aochuan Chen, Jinghan Jia, Jiancheng Liu, Gaowen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Massive data is often considered essential for deep learning applications, but it also incurs significant computational and infrastructural costs. Therefore, dataset pruning (DP) has emerged as an effective way to improve data efficiency by identifying and removing redundant training samples without sacrificing performance. In this work, we aim to address the problem of DP for transfer learning, i.e., how to prune a source dataset for improved pretraining efficiency and lossless finetuning accuracy on downstream target tasks. To our best knowledge, the problem of DP for transfer learning remains open, as previous studies have primarily addressed DP and transfer learning as separate problems. By contrast, we establish a unified viewpoint to integrate DP with transfer learning and find that existing DP methods are not suitable for the transfer learning paradigm. We then propose two new DP methods, label mapping and feature mapping, for supervised and self-supervised pretraining settings respectively, by revisiting the DP problem through the lens of source-target domain mapping. Furthermore, we demonstrate the effectiveness of our approach on numerous transfer learning tasks. We show that source data classes can be pruned by up to 40% ~ 80% without sacrificing downstream performance, resulting in a significant 2 ~ 5 times speed-up during the pretraining stage. Besides, our proposal exhibits broad applicability and can improve other computationally intensive transfer learning techniques, such as adversarial pretraining. Codes are available at https://github.com/OPTML-Group/DP4TL.

</details>

### Dynamic Sparsity Is Channel-Level Sparsity Learner.
- **链接**: [arXiv:2305.19454](https://arxiv.org/abs/2305.19454) · [代码](https://github.com/luuyin/chase) · 📚 被引 2
- **作者**: Lu Yin, Gen Li, Meng Fang, Li Shen, Tianjin Huang, Zhangyang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse training has received an upsurging interest in machine learning due to its tantalizing saving potential for the entire training process as well as inference. Dynamic sparse training (DST), as a leading sparse training approach, can train deep neural networks at high sparsity from scratch to match the performance of their dense counterparts. However, most if not all DST prior arts demonstrate their effectiveness on unstructured sparsity with highly irregular sparse patterns, which receives limited support in common hardware. This limitation hinders the usage of DST in practice. In this paper, we propose Channel-aware dynamic sparse (Chase), which for the first time seamlessly translates the promise of unstructured dynamic sparsity to GPU-friendly channel-level sparsity (not fine-grained N:M or group sparsity) during one end-to-end training process, without any ad-hoc operations. The resulting small sparse networks can be directly accelerated by commodity hardware, without using any particularly sparsity-aware hardware accelerators. This appealing outcome is partially motivated by a hidden phenomenon of dynamic sparsity: off-the-shelf unstructured DST implicitly involves biased parameter reallocation across channels, with a large fraction of channels (up to 60%) being sparser than others. By progressively identifying and removing these channels during training, our approach translates unstructured sparsity to channel-wise sparsity. Our experimental results demonstrate that Chase achieves 1.7 X inference throughput speedup on common GPU devices without compromising accuracy with ResNet-50 on ImageNet. We release our codes in https://github.com/luuyin/chase.

</details>

### Penalising the biases in norm regularisation enforces sparsity.
- **链接**: [arXiv:2303.01353](https://arxiv.org/abs/2303.01353) · 📚 被引 1
- **作者**: Etienne Boursier, Nicolas Flammarion
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Controlling the parameters' norm often yields good generalisation when training neural networks. Beyond simple intuitions, the relation between regularising parameters' norm and obtained estimators remains theoretically misunderstood. For one hidden ReLU layer networks with unidimensional data, this work shows the parameters' norm required to represent a function is given by the total variation of its second derivative, weighted by a $\sqrt{1+x^2}$ factor. Notably, this weighting factor disappears when the norm of bias terms is not regularised. The presence of this additional weighting factor is of utmost significance as it is shown to enforce the uniqueness and sparsity (in the number of kinks) of the minimal norm interpolator. Conversely, omitting the bias' norm allows for non-sparse solutions. Penalising the bias terms in the regularisation, either explicitly or implicitly, thus leads to sparse estimators.

</details>

### Path Regularization: A Convexity and Sparsity Inducing Regularization for Parallel ReLU Networks.
- **链接**: [arXiv:2110.09548](https://arxiv.org/abs/2110.09548) · 📚 被引 4
- **作者**: Tolga Ergen, Mert Pilanci
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding the fundamental principles behind the success of deep neural networks is one of the most important open questions in the current literature. To this end, we study the training problem of deep neural networks and introduce an analytic approach to unveil hidden convexity in the optimization landscape. We consider a deep parallel ReLU network architecture, which also includes standard deep networks and ResNets as its special cases. We then show that pathwise regularized training problems can be represented as an exact convex optimization problem. We further prove that the equivalent convex problem is regularized via a group sparsity inducing norm. Thus, a path regularized parallel ReLU network can be viewed as a parsimonious convex model in high dimensions. More importantly, since the original training problem may not be trainable in polynomial-time, we propose an approximate algorithm with a fully polynomial-time complexity in all data dimensions. Then, we prove strong global optimality guarantees for this algorithm. We also provide experiments corroborating our theory.

</details>

### Sparsity-Preserving Differentially Private Training of Large Embedding Models.
- **链接**: [arXiv:2311.08357](https://arxiv.org/abs/2311.08357) · 📚 被引 3
- **作者**: Badih Ghazi, Yangsibo Huang, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Amer Sinha et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As the use of large embedding models in recommendation systems and language applications increases, concerns over user data privacy have also risen. DP-SGD, a training algorithm that combines differential privacy with stochastic gradient descent, has been the workhorse in protecting user privacy without compromising model accuracy by much. However, applying DP-SGD naively to embedding models can destroy gradient sparsity, leading to reduced training efficiency. To address this issue, we present two new algorithms, DP-FEST and DP-AdaFEST, that preserve gradient sparsity during private training of large embedding models. Our algorithms achieve substantial reductions ($10^6 \times$) in gradient size, while maintaining comparable levels of accuracy, on benchmark real-world datasets.

</details>

### The Emergence of Essential Sparsity in Large Pre-trained Models: The Weights that Matter.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/7a69ab48efcbb0153e72d458fb091969-Abstract-Conference.html) · 📚 被引 1
- **作者**: Ajay Jaiswal, Shiwei Liu, Tianlong Chen, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Model Sparsity Can Simplify Machine Unlearning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a204aa68ab4e970e1ceccfb5b5cdc5e4-Abstract-Conference.html) · 📚 被引 36
- **作者**: Jinghan Jia, Jiancheng Liu, Parikshit Ram, Yuguang Yao, Gaowen Liu, Yang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Robust Model Reasoning and Fitting via Dual Sparsity Pursuit.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e1de63ec74f40d3234c4e053f3528e18-Abstract-Conference.html) · 📚 被引 1
- **作者**: Xingyu Jiang, Jiayi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### High-dimensional Contextual Bandit Problem without Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/9b35a0a20d617dc68ae98a7a57df2f51-Abstract-Conference.html) · 📚 被引 0
- **作者**: Junpei Komiyama, Masaaki Imaizumi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Emergence of Shape Bias in Convolutional Neural Networks through Activation Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e31c16c7b3e0ccee5159ae5443154fac-Abstract-Conference.html) · 📚 被引 2
- **作者**: Tianqin Li, Ziqi Wen, Yangfan Li, Tai Sing Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Stability-penalty-adaptive follow-the-regularized-leader: Sparsity, game-dependency, and best-of-both-worlds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/9408564a4229f4a933ac9bd09a29ee96-Abstract-Conference.html) · 📚 被引 0
- **作者**: Taira Tsuchiya, Shinji Ito, Junya Honda
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Generalizing Nonlinear ICA Beyond Structural Sparsity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2aebc17b683792a17dd4a24fcb038ba6-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yujia Zheng, Kun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
