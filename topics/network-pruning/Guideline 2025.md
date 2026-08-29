# Network Pruning — 2025 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 33 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration.
- **链接**: [arXiv:2410.23317](https://arxiv.org/abs/2410.23317)
- **作者**: Dezhan Tu, Danylo Vashchilenko, Yuzhe Lu, Panpan Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have demonstrated impressive performance across a versatile set of tasks. A key challenge in accelerating VLMs is storing and accessing the large Key-Value (KV) cache that encodes long visual contexts, such as images or videos. While existing KV cache compression methods are effective for Large Language Models (LLMs), directly migrating them to VLMs yields suboptimal accuracy and speedup. To bridge the gap, we propose VL-Cache, a novel KV cache compression recipe tailored for accelerating VLM inference. In this paper, we first investigate the unique sparsity pattern of VLM attention by distinguishing visual and text tokens in prefill and decoding phases. Based on these observations, we introduce a layer-adaptive sparsity-aware cache budget allocation method that effectively distributes the limited cache budget across different layers, further reducing KV cache size without compromising accuracy. Additionally, we develop a modality-aware token scoring policy to better evaluate the token importance. Empirical results on multiple benchmark datasets demonstrate that retaining only 10% of KV cache achieves accuracy comparable to that with full cache. In a speed benchmark, our method accelerates end-to-end latency of generating 100 tokens by up to 2.33x and speeds up decoding by up to 7.08x, while reducing the memory footprint of KV cache in GPU by 90%.

</details>

### Mutual Effort for Efficiency: A Similarity-based Token Pruning for Vision Transformers in Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=GTcEe5fayC)
- **作者**: Sheng Li, Qitao Tan, Yue Dai, Zhenglun Kong, Tianyu Wang, Jun Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Probe Pruning: Accelerating LLMs through Dynamic Pruning via Model-Probing.
- **链接**: [arXiv:2502.15618](https://arxiv.org/abs/2502.15618) · [代码](https://github.com/Qi-Le1/Probe_Pruning)
- **作者**: Qi Le, Enmao Diao, Ziyan Wang, Xinran Wang, Jie Ding, Li Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Probe Pruning (PP), a novel framework for online, dynamic, structured pruning of Large Language Models (LLMs) applied in a batch-wise manner. PP leverages the insight that not all samples and tokens contribute equally to the model's output, and probing a small portion of each batch effectively identifies crucial weights, enabling tailored dynamic pruning for different batches. It comprises three main stages: probing, history-informed pruning, and full inference. In the probing stage, PP selects a small yet crucial set of hidden states, based on residual importance, to run a few model layers ahead. During the history-informed pruning stage, PP strategically integrates the probing states with historical states. Subsequently, it structurally prunes weights based on the integrated states and the PP importance score, a metric developed specifically to assess the importance of each weight channel in maintaining performance. In the final stage, full inference is conducted on the remaining weights. A major advantage of PP is its compatibility with existing models, as it operates without requiring additional neural network modules or fine-tuning. Comprehensive evaluations of PP on LLaMA-2/3 and OPT models reveal that even minimal probing-using just 1.5% of FLOPs-can substantially enhance the efficiency of structured pruning of LLMs. For instance, when evaluated on LLaMA-2-7B with WikiText2, PP achieves a 2.56 times lower ratio of performance degradation per unit of runtime reduction compared to the state-of-the-art method at a 40% pruning ratio. Our code is available at https://github.com/Qi-Le1/Probe_Pruning.

</details>

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

### ConceptPrune: Concept Editing in Diffusion Models via Skilled Neuron Pruning.
- **链接**: [arXiv:2405.19237](https://arxiv.org/abs/2405.19237)
- **作者**: Ruchika Chavhan, Da Li, Timothy M. Hospedales
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While large-scale text-to-image diffusion models have demonstrated impressive image-generation capabilities, there are significant concerns about their potential misuse for generating unsafe content, violating copyright, and perpetuating societal biases. Recently, the text-to-image generation community has begun addressing these concerns by editing or unlearning undesired concepts from pre-trained models. However, these methods often involve data-intensive and inefficient fine-tuning or utilize various forms of token remapping, rendering them susceptible to adversarial jailbreaks. In this paper, we present a simple and effective training-free approach, ConceptPrune, wherein we first identify critical regions within pre-trained models responsible for generating undesirable concepts, thereby facilitating straightforward concept unlearning via weight pruning. Experiments across a range of concepts including artistic styles, nudity, object erasure, and gender debiasing demonstrate that target concepts can be efficiently erased by pruning a tiny fraction, approximately 0.12% of total weights, enabling multi-concept erasure and robustness against various white-box and black-box adversarial attacks.

</details>

### Provence: efficient and robust context pruning for retrieval-augmented generation.
- **链接**: [arXiv:2501.16214](https://arxiv.org/abs/2501.16214)
- **作者**: Nadezhda Chirkova, Thibault Formal, Vassilina Nikoulina, Stéphane Clinchant
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Retrieval-augmented generation improves various aspects of large language models (LLMs) generation, but suffers from computational overhead caused by long contexts as well as the propagation of irrelevant retrieved information into generated responses. Context pruning deals with both aspects, by removing irrelevant parts of retrieved contexts before LLM generation. Existing context pruning approaches are however limited, and do not provide a universal model that would be both efficient and robust in a wide range of scenarios, e.g., when contexts contain a variable amount of relevant information or vary in length, or when evaluated on various domains. In this work, we close this gap and introduce Provence (Pruning and Reranking Of retrieVEd relevaNt ContExts), an efficient and robust context pruner for Question Answering, which dynamically detects the needed amount of pruning for a given context and can be used out-of-the-box for various domains. The three key ingredients of Provence are formulating the context pruning task as sequence labeling, unifying context pruning capabilities with context reranking, and training on diverse data. Our experimental results show that Provence enables context pruning with negligible to no drop in performance, in various domains and settings, at almost no cost in a standard RAG pipeline. We also conduct a deeper analysis alongside various ablations to provide insights into training context pruners for future work.

</details>

### Training-Free Dataset Pruning for Instance Segmentation.
- **链接**: [arXiv:2503.00828](https://arxiv.org/abs/2503.00828) · [代码](https://github.com/he-y/dataset-pruning-for-instance-segmentation)
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
- **链接**: [arXiv:2410.17711](https://arxiv.org/abs/2410.17711) · [代码](https://github.com/Dereck0602/calibration_data)
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
- **链接**: [arXiv:2506.01701](https://arxiv.org/abs/2506.01701) · [代码](https://github.com/hrtan/InfoMax)
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
- **链接**: [arXiv:2407.21018](https://arxiv.org/abs/2407.21018) · [代码](https://github.com/SalesforceAIResearch/ThinK)
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
