# Network Pruning — 2024 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 28 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### ECoFLaP: Efficient Coarse-to-Fine Layer-Wise Pruning for Vision-Language Models.
- **链接**: [arXiv:2310.02998](https://arxiv.org/abs/2310.02998)
- **作者**: Yi-Lin Sung, Jaehong Yoon, Mohit Bansal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) can understand the world comprehensively by integrating rich information from different modalities, achieving remarkable advancements on various multimodal downstream tasks. However, deploying LVLMs is often problematic due to their massive computational/energy costs and carbon consumption. Such issues make it infeasible to adopt conventional iterative global pruning, which is costly due to computing the Hessian matrix of the entire large model for sparsification. Alternatively, several studies have recently proposed layer-wise pruning approaches to avoid the expensive computation of global pruning and efficiently compress model weights according to their importance within a layer. However, they often suffer from suboptimal model compression due to their lack of a global perspective. To address this limitation in recent efficient pruning methods for large models, we propose Efficient Coarse-to-Fine LayerWise Pruning (ECoFLaP), a two-stage coarse-to-fine weight pruning approach for LVLMs. We first determine the sparsity ratios of different layers or blocks by leveraging the global importance score, which is efficiently computed based on the zeroth-order approximation of the global model gradients. Then, the model performs local layer-wise unstructured weight pruning based on globally-informed sparsity ratios. We validate our proposed method across various multimodal and unimodal models and datasets, demonstrating significant performance improvements over prevalent pruning techniques in the high-sparsity regime.

</details>

### Data-independent Module-aware Pruning for Hierarchical Vision Transformers.
- **链接**: [arXiv:2404.13648](https://arxiv.org/abs/2404.13648) · [代码](https://github.com/he-y/Data-independent-Module-Aware-Pruning)
- **作者**: Yang He, Joey Tianyi Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hierarchical vision transformers (ViTs) have two advantages over conventional ViTs. First, hierarchical ViTs achieve linear computational complexity with respect to image size by local self-attention. Second, hierarchical ViTs create hierarchical feature maps by merging image patches in deeper layers for dense prediction. However, existing pruning methods ignore the unique properties of hierarchical ViTs and use the magnitude value as the weight importance. This approach leads to two main drawbacks. First, the "local" attention weights are compared at a "global" level, which may cause some "locally" important weights to be pruned due to their relatively small magnitude "globally". The second issue with magnitude pruning is that it fails to consider the distinct weight distributions of the network, which are essential for extracting coarse to fine-grained features at various hierarchical levels. To solve the aforementioned issues, we have developed a Data-independent Module-Aware Pruning method (DIMAP) to compress hierarchical ViTs. To ensure that "local" attention weights at different hierarchical levels are compared fairly in terms of their contribution, we treat them as a module and examine their contribution by analyzing their information distortion. Furthermore, we introduce a novel weight metric that is solely based on weights and does not require input images, thereby eliminating the dependence on the patch merging process. Our method validates its usefulness and strengths on Swin Transformers of different sizes on ImageNet-1k classification. Notably, the top-5 accuracy drop is only 0.07% when we remove 52.5% FLOPs and 52.7% parameters of Swin-B. When we reduce 33.2% FLOPs and 33.2% parameters of Swin-S, we can even achieve a 0.8% higher relative top-5 accuracy than the original model. Code is available at: https://github.com/he-y/Data-independent-Module-Aware-Pruning

</details>

### Synergistic Patch Pruning for Vision Transformer: Unifying Intra- & Inter-Layer Patch Importance.
- **链接**: [出版页](https://openreview.net/forum?id=COO51g41Q4)
- **作者**: Yuyao Zhang, Lan Wei, Nikolaos M. Freris
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### StructComp: Substituting propagation with Structural Compression in Training Graph Contrastive Learning.
- **链接**: [arXiv:2312.04865](https://arxiv.org/abs/2312.04865)
- **作者**: Shengzhong Zhang, Wenjie Yang, Xinyuan Cao, Hongwei Zhang, Zengfeng Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph contrastive learning (GCL) has become a powerful tool for learning graph data, but its scalability remains a significant challenge. In this work, we propose a simple yet effective training framework called Structural Compression (StructComp) to address this issue. Inspired by a sparse low-rank approximation on the diffusion matrix, StructComp trains the encoder with the compressed nodes. This allows the encoder not to perform any message passing during the training stage, and significantly reduces the number of sample pairs in the contrastive loss. We theoretically prove that the original GCL loss can be approximated with the contrastive loss computed by StructComp. Moreover, StructComp can be regarded as an additional regularization term for GCL models, resulting in a more robust encoder. Empirical studies on various datasets show that StructComp greatly reduces the time and memory consumption while improving model performance compared to the vanilla GCL models and scalable training methods.

</details>

### D2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=thbtoAkCe9)
- **作者**: Adyasha Maharana, Prateek Yadav, Mohit Bansal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Candidate Label Set Pruning: A Data-centric Perspective for Deep Partial-label Learning.
- **链接**: [出版页](https://openreview.net/forum?id=Fk5IzauJ7F)
- **作者**: Shuo He, Chaojie Wang, Guowu Yang, Lei Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Adversarial Feature Map Pruning for Backdoor.
- **链接**: [出版页](https://openreview.net/forum?id=IOEEDkla96)
- **作者**: Dong Huang, Qingwen Bu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Effective pruning of web-scale datasets based on complexity of concept clusters.
- **链接**: [arXiv:2401.04578](https://arxiv.org/abs/2401.04578)
- **作者**: Amro Abbas, Evgenia Rusak, Kushal Tirumala, Wieland Brendel, Kamalika Chaudhuri, Ari S. Morcos
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Utilizing massive web-scale datasets has led to unprecedented performance gains in machine learning models, but also imposes outlandish compute requirements for their training. In order to improve training and data efficiency, we here push the limits of pruning large-scale multimodal datasets for training CLIP-style models. Today's most effective pruning method on ImageNet clusters data samples into separate concepts according to their embedding and prunes away the most prototypical samples. We scale this approach to LAION and improve it by noting that the pruning rate should be concept-specific and adapted to the complexity of the concept. Using a simple and intuitive complexity measure, we are able to reduce the training cost to a quarter of regular training. By filtering from the LAION dataset, we find that training on a smaller set of high-quality data can lead to higher performance with significantly lower training costs. More specifically, we are able to outperform the LAION-trained OpenCLIP-ViT-B32 model on ImageNet zero-shot accuracy by 1.1p.p. while only using 27.7% of the data and training compute. Despite a strong reduction in training cost, we also see improvements on ImageNet dist. shifts, retrieval tasks and VTAB. On the DataComp Medium benchmark, we achieve a new state-of-the-art Imagehttps://info.arxiv.org/help/prep#commentsNet zero-shot accuracy and a competitive average zero-shot accuracy on 38 evaluation tasks.

</details>

### Adaptive Sharpness-Aware Pruning for Robust Sparse Networks.
- **链接**: [arXiv:2306.14306](https://arxiv.org/abs/2306.14306)
- **作者**: Anna Bair, Hongxu Yin, Maying Shen, Pavlo Molchanov, José M. Álvarez
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robustness and compactness are two essential attributes of deep learning models that are deployed in the real world. The goals of robustness and compactness may seem to be at odds, since robustness requires generalization across domains, while the process of compression exploits specificity in one domain. We introduce Adaptive Sharpness-Aware Pruning (AdaSAP), which unifies these goals through the lens of network sharpness. The AdaSAP method produces sparse networks that are robust to input variations which are unseen at training time. We achieve this by strategically incorporating weight perturbations in order to optimize the loss landscape. This allows the model to be both primed for pruning and regularized for improved robustness. AdaSAP improves the robust accuracy of pruned models on image classification by up to +6% on ImageNet C and +4% on ImageNet V2, and on object detection by +4% on a corrupted Pascal VOC dataset, over a wide range of compression ratios, pruning criteria, and network architectures, outperforming recent pruning art by large margins.

</details>

### Sparse Spiking Neural Network: Exploiting Heterogeneity in Timescales for Pruning Recurrent SNN.
- **链接**: [arXiv:2403.03409](https://arxiv.org/abs/2403.03409)
- **作者**: Biswadeep Chakraborty, Beomseok Kang, Harshit Kumar, Saibal Mukhopadhyay
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recurrent Spiking Neural Networks (RSNNs) have emerged as a computationally efficient and brain-inspired learning model. The design of sparse RSNNs with fewer neurons and synapses helps reduce the computational complexity of RSNNs. Traditionally, sparse SNNs are obtained by first training a dense and complex SNN for a target task, and, then, pruning neurons with low activity (activity-based pruning) while maintaining task performance. In contrast, this paper presents a task-agnostic methodology for designing sparse RSNNs by pruning a large randomly initialized model. We introduce a novel Lyapunov Noise Pruning (LNP) algorithm that uses graph sparsification methods and utilizes Lyapunov exponents to design a stable sparse RSNN from a randomly initialized RSNN. We show that the LNP can leverage diversity in neuronal timescales to design a sparse Heterogeneous RSNN (HRSNN). Further, we show that the same sparse HRSNN model can be trained for different tasks, such as image classification and temporal prediction. We experimentally show that, in spite of being task-agnostic, LNP increases computational efficiency (fewer neurons and synapses) and prediction performance of RSNNs compared to traditional activity-based pruning of trained dense models.

</details>

### Sparse Weight Averaging with Multiple Particles for Iterative Magnitude Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=Y9t7MqZtCR)
- **作者**: Moonseok Choi, Hyungi Lee, Giung Nam, Juho Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### The Need for Speed: Pruning Transformers with One Recipe.
- **链接**: [arXiv:2403.17921](https://arxiv.org/abs/2403.17921)
- **作者**: Samir Khaki, Konstantinos N. Plataniotis
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the $\textbf{O}$ne-shot $\textbf{P}$runing $\textbf{T}$echnique for $\textbf{I}$nterchangeable $\textbf{N}$etworks ($\textbf{OPTIN}$) framework as a tool to increase the efficiency of pre-trained transformer architectures $\textit{without requiring re-training}$. Recent works have explored improving transformer efficiency, however often incur computationally expensive re-training procedures or depend on architecture-specific characteristics, thus impeding practical wide-scale adoption. To address these shortcomings, the OPTIN framework leverages intermediate feature distillation, capturing the long-range dependencies of model parameters (coined $\textit{trajectory}$), to produce state-of-the-art results on natural language, image classification, transfer learning, and semantic segmentation tasks $\textit{without re-training}$. Given a FLOP constraint, the OPTIN framework will compress the network while maintaining competitive accuracy performance and improved throughput. Particularly, we show a $\leq 2$% accuracy degradation from NLP baselines and a $0.5$% improvement from state-of-the-art methods on image classification at competitive FLOPs reductions. We further demonstrate the generalization of tasks and architecture with comparative performance using Mask2Former for semantic segmentation and cnn-style networks. OPTIN presents one of the first one-shot efficient frameworks for compressing transformer architectures that generalizes well across different class domains, in particular: natural language and image-related tasks, without $\textit{re-training}$.

</details>

### Adaptive Window Pruning for Efficient Local Motion Deblurring.
- **链接**: [arXiv:2306.14268](https://arxiv.org/abs/2306.14268)
- **作者**: Haoying Li, Jixin Zhao, Shangchen Zhou, Huajun Feng, Chongyi Li, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Local motion blur commonly occurs in real-world photography due to the mixing between moving objects and stationary backgrounds during exposure. Existing image deblurring methods predominantly focus on global deblurring, inadvertently affecting the sharpness of backgrounds in locally blurred images and wasting unnecessary computation on sharp pixels, especially for high-resolution images. This paper aims to adaptively and efficiently restore high-resolution locally blurred images. We propose a local motion deblurring vision Transformer (LMD-ViT) built on adaptive window pruning Transformer blocks (AdaWPT). To focus deblurring on local regions and reduce computation, AdaWPT prunes unnecessary windows, only allowing the active windows to be involved in the deblurring processes. The pruning operation relies on the blurriness confidence predicted by a confidence predictor that is trained end-to-end using a reconstruction loss with Gumbel-Softmax re-parameterization and a pruning loss guided by annotated blur masks. Our method removes local motion blur effectively without distorting sharp regions, demonstrated by its exceptional perceptual and quantitative improvements compared to state-of-the-art methods. In addition, our approach substantially reduces FLOPs by 66% and achieves more than a twofold increase in inference speed compared to Transformer-based deblurring methods. We will make our code and annotated blur masks publicly available.

</details>

### What Makes a Good Prune? Maximal Unstructured Pruning for Maximal Cosine Similarity.
- **链接**: [出版页](https://openreview.net/forum?id=jsvvPVVzwf)
- **作者**: Gabryel Mason-Williams, Fredrik Dahlqvist
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=s2NjWfaYdZ)
- **作者**: Seungcheol Park, Hojun Choi, U Kang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### InfoBatch: Lossless Training Speed Up by Unbiased Dynamic Data Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=C61sk5LsK6)
- **作者**: Ziheng Qin, Kai Wang, Zangwei Zheng, Jianyang Gu, Xiangyu Peng, Zhaopan Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Towards Energy Efficient Spiking Neural Networks: An Unstructured Pruning Framework.
- **链接**: [出版页](https://openreview.net/forum?id=eoSeaK4QJo)
- **作者**: Xinyu Shi, Jianhao Ding, Zecheng Hao, Zhaofei Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### A Simple and Effective Pruning Approach for Large Language Models.
- **链接**: [arXiv:2306.11695](https://arxiv.org/abs/2306.11695) · [代码](https://github.com/locuslab/wanda)
- **作者**: Mingjie Sun, Zhuang Liu, Anna Bair, J. Zico Kolter
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As their size increases, Large Languages Models (LLMs) are natural candidates for network pruning methods: approaches that drop a subset of network weights while striving to preserve performance. Existing methods, however, require either retraining, which is rarely affordable for billion-scale LLMs, or solving a weight reconstruction problem reliant on second-order information, which may also be computationally expensive. In this paper, we introduce a novel, straightforward yet effective pruning method, termed Wanda (Pruning by Weights and activations), designed to induce sparsity in pretrained LLMs. Motivated by the recent observation of emergent large magnitude features in LLMs, our approach prunes weights with the smallest magnitudes multiplied by the corresponding input activations, on a per-output basis. Notably, Wanda requires no retraining or weight update, and the pruned LLM can be used as is. We conduct a thorough evaluation of our method Wanda on LLaMA and LLaMA-2 across various language benchmarks. Wanda significantly outperforms the established baseline of magnitude pruning and performs competitively against recent method involving intensive weight update. Code is available at https://github.com/locuslab/wanda.

</details>

### Towards Meta-Pruning via Optimal Transport.
- **链接**: [arXiv:2402.07839](https://arxiv.org/abs/2402.07839) · [代码](https://github.com/alexandertheus/Intra-Fusion)
- **作者**: Alexander Theus, Olin Geimer, Friedrich Wicke, Thomas Hofmann, Sotiris Anagnostidis, Sidak Pal Singh
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Structural pruning of neural networks conventionally relies on identifying and discarding less important neurons, a practice often resulting in significant accuracy loss that necessitates subsequent fine-tuning efforts. This paper introduces a novel approach named Intra-Fusion, challenging this prevailing pruning paradigm. Unlike existing methods that focus on designing meaningful neuron importance metrics, Intra-Fusion redefines the overlying pruning procedure. Through utilizing the concepts of model fusion and Optimal Transport, we leverage an agnostically given importance metric to arrive at a more effective sparse model representation. Notably, our approach achieves substantial accuracy recovery without the need for resource-intensive fine-tuning, making it an efficient and promising tool for neural network compression. Additionally, we explore how fusion can be added to the pruning process to significantly decrease the training time while maintaining competitive performance. We benchmark our results for various networks on commonly used datasets such as CIFAR-10, CIFAR-100, and ImageNet. More broadly, we hope that the proposed Intra-Fusion approach invigorates exploration into a fresh alternative to the predominant compression approaches. Our code is available here: https://github.com/alexandertheus/Intra-Fusion.

</details>

### Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning.
- **链接**: [arXiv:2310.06694](https://arxiv.org/abs/2310.06694)
- **作者**: Mengzhou Xia, Tianyu Gao, Zhiyuan Zeng, Danqi Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The popularity of LLaMA (Touvron et al., 2023a;b) and other recently emerged moderate-sized large language models (LLMs) highlights the potential of building smaller yet powerful LLMs. Regardless, the cost of training such models from scratch on trillions of tokens remains high. In this work, we study structured pruning as an effective means to develop smaller LLMs from pre-trained, larger models. Our approach employs two key techniques: (1) targeted structured pruning, which prunes a larger model to a specified target shape by removing layers, heads, and intermediate and hidden dimensions in an end-to-end manner, and (2) dynamic batch loading, which dynamically updates the composition of sampled data in each training batch based on varying losses across different domains. We demonstrate the efficacy of our approach by presenting the Sheared-LLaMA series, pruning the LLaMA2-7B model down to 1.3B and 2.7B parameters. Sheared-LLaMA models outperform state-of-the-art open-source models of equivalent sizes, such as Pythia, INCITE, OpenLLaMA and the concurrent TinyLlama models, on a wide range of downstream and instruction tuning evaluations, while requiring only 3% of compute compared to training such models from scratch. This work provides compelling evidence that leveraging existing LLMs with structured pruning is a far more cost-effective approach for building competitive small-scale LLMs

</details>

### BESA: Pruning Large Language Models with Blockwise Parameter-Efficient Sparsity Allocation.
- **链接**: [arXiv:2402.16880](https://arxiv.org/abs/2402.16880) · [代码](https://github.com/OpenGVLab/LLMPrune-BESA)
- **作者**: Peng Xu, Wenqi Shao, Mengzhao Chen, Shitao Tang, Kaipeng Zhang, Peng Gao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have demonstrated outstanding performance in various tasks, such as text summarization, text question-answering, and etc. While their performance is impressive, the computational footprint due to their vast number of parameters can be prohibitive. Existing solutions such as SparseGPT and Wanda attempt to alleviate this issue through weight pruning. However, their layer-wise approach results in significant perturbation to the model's output and requires meticulous hyperparameter tuning, such as the pruning rate, which can adversely affect overall model performance. To address this, this paper introduces a novel LLM pruning technique dubbed blockwise parameter-efficient sparsity allocation (BESA) by applying a blockwise reconstruction loss. In contrast to the typical layer-wise pruning techniques, BESA is characterized by two distinctive attributes: i) it targets the overall pruning error with respect to individual transformer blocks, and ii) it allocates layer-specific sparsity in a differentiable manner, both of which ensure reduced performance degradation after pruning. Our experiments show that BESA achieves state-of-the-art performance, efficiently pruning LLMs like LLaMA1, and LLaMA2 with 7B to 70B parameters on a single A100 GPU in just five hours. Code is available at https://github.com/OpenGVLab/LLMPrune-BESA.

</details>

### FedP3: Federated Personalized and Privacy-friendly Network Pruning under Model Heterogeneity.
- **链接**: [arXiv:2404.09816](https://arxiv.org/abs/2404.09816)
- **作者**: Kai Yi, Nidham Gazagnadou, Peter Richtárik, Lingjuan Lyu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The interest in federated learning has surged in recent research due to its unique ability to train a global model using privacy-secured information held locally on each client. This paper pays particular attention to the issue of client-side model heterogeneity, a pervasive challenge in the practical implementation of FL that escalates its complexity. Assuming a scenario where each client possesses varied memory storage, processing capabilities and network bandwidth - a phenomenon referred to as system heterogeneity - there is a pressing need to customize a unique model for each client. In response to this, we present an effective and adaptable federated framework FedP3, representing Federated Personalized and Privacy-friendly network Pruning, tailored for model heterogeneity scenarios. Our proposed methodology can incorporate and adapt well-established techniques to its specific instances. We offer a theoretical interpretation of FedP3 and its locally differential-private variant, DP-FedP3, and theoretically validate their efficiencies.

</details>

### SWAP: Sparse Entropic Wasserstein Regression for Robust Network Pruning.
- **链接**: [出版页](https://openreview.net/forum?id=LJWizuuBUy)
- **作者**: Lei You, Hei Victor Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=Tr0lPx9woF) · 📚 被引 22
- **作者**: Yingtao Zhang, Haoli Bai, Haokun Lin, Jialin Zhao, Lu Hou, Carlo Vittorio Cannistraci
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Sparse Model Soups: A Recipe for Improved Pruning via Model Averaging.
- **链接**: [arXiv:2306.16788](https://arxiv.org/abs/2306.16788)
- **作者**: Max Zimmer, Christoph Spiegel, Sebastian Pokutta
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks can be significantly compressed by pruning, yielding sparse models with reduced storage and computational demands while preserving predictive performance. Model soups (Wortsman et al., 2022) enhance generalization and out-of-distribution (OOD) performance by averaging the parameters of multiple models into a single one, without increasing inference time. However, achieving both sparsity and parameter averaging is challenging as averaging arbitrary sparse models reduces the overall sparsity due to differing sparse connectivities. This work addresses these challenges by demonstrating that exploring a single retraining phase of Iterative Magnitude Pruning (IMP) with varied hyperparameter configurations such as batch ordering or weight decay yields models suitable for averaging, sharing identical sparse connectivity by design. Averaging these models significantly enhances generalization and OOD performance over their individual counterparts. Building on this, we introduce Sparse Model Soups (SMS), a novel method for merging sparse models by initiating each prune-retrain cycle with the averaged model from the previous phase. SMS preserves sparsity, exploits sparse network benefits, is modular and fully parallelizable, and substantially improves IMP's performance. We further demonstrate that SMS can be adapted to enhance state-of-the-art pruning-during-training approaches.

</details>

### Dynamic Sparse Training with Structured Sparsity.
- **链接**: [arXiv:2305.02299](https://arxiv.org/abs/2305.02299)
- **作者**: Mike Lasby, Anna Golubeva, Utku Evci, Mihai Nica, Yani Ioannou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dynamic Sparse Training (DST) methods achieve state-of-the-art results in sparse neural network training, matching the generalization of dense models while enabling sparse training and inference. Although the resulting models are highly sparse and theoretically less computationally expensive, achieving speedups with unstructured sparsity on real-world hardware is challenging. In this work, we propose a sparse-to-sparse DST method, Structured RigL (SRigL), to learn a variant of fine-grained structured N:M sparsity by imposing a constant fan-in constraint. Using our empirical analysis of existing DST methods at high sparsity, we additionally employ a neuron ablation method which enables SRigL to achieve state-of-the-art sparse-to-sparse structured DST performance on a variety of Neural Network (NN) architectures. Using a 90% sparse linear layer, we demonstrate a real-world acceleration of 3.4x/2.5x on CPU for online inference and 1.7x/13.0x on GPU for inference with a batch size of 256 when compared to equivalent dense/unstructured (CSR) sparse layers, respectively.

</details>

### ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models.
- **链接**: [arXiv:2310.04564](https://arxiv.org/abs/2310.04564)
- **作者**: Iman Mirzadeh, Keivan Alizadeh-Vahid, Sachin Mehta, Carlo C. del Mundo, Oncel Tuzel, Golnoosh Samei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Language Models (LLMs) with billions of parameters have drastically transformed AI applications. However, their demanding computation during inference has raised significant challenges for deployment on resource-constrained devices. Despite recent trends favoring alternative activation functions such as GELU or SiLU, known for increased computation, this study strongly advocates for reinstating ReLU activation in LLMs. We demonstrate that using the ReLU activation function has a negligible impact on convergence and performance while significantly reducing computation and weight transfer. This reduction is particularly valuable during the memory-bound inference step, where efficiency is paramount. Exploring sparsity patterns in ReLU-based LLMs, we unveil the reutilization of activated neurons for generating new tokens and leveraging these insights, we propose practical strategies to substantially reduce LLM inference computation up to three times, using ReLU activations with minimal performance trade-offs.

</details>

### Deep Neural Network Initialization with Sparsity Inducing activations.
- **链接**: [arXiv:2402.16184](https://arxiv.org/abs/2402.16184)
- **作者**: Ilan Price, Nicholas Daultry Ball, Adam C. Jones, Samuel C. H. Lam, Jared Tanner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inducing and leveraging sparse activations during training and inference is a promising avenue for improving the computational efficiency of deep networks, which is increasingly important as network sizes continue to grow and their application becomes more widespread. Here we use the large width Gaussian process limit to analyze the behaviour, at random initialization, of nonlinear activations that induce sparsity in the hidden outputs. A previously unreported form of training instability is proven for arguably two of the most natural candidates for hidden layer sparsification; those being a shifted ReLU ($φ(x)=\max(0, x-τ)$ for $τ\ge 0$) and soft thresholding ($φ(x)=0$ for $|x|\leτ$ and $x-\text{sign}(x)τ$ for $|x|>τ$). We show that this instability is overcome by clipping the nonlinear activation magnitude, at a level prescribed by the shape of the associated Gaussian process variance map. Numerical experiments verify the theory and show that the proposed magnitude clipped sparsifying activations can be trained with training and test fractional sparsity as high as 85\% while retaining close to full accuracy.

</details>
