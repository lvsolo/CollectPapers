# Continual Learning — 2025 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 26 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### C-CLIP: Multimodal Continual Learning for Vision-Language Model.
- **链接**: [出版页](https://openreview.net/forum?id=sb7qHFYwBc)
- **作者**: Wenzhuo Liu, Fei Zhu, Longhui Wei, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Vision and Language Synergy for Rehearsal Free Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=9aZ2ixiYGd)
- **作者**: Muhammad Anwar Ma'sum, Mahardhika Pratama, Savitha Ramasamy, Lin Liu, Habibullah, Ryszard Kowalczyk
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Active Learning for Continual Learning: Keeping the Past Alive in the Present.
- **链接**: [arXiv:2501.14278](https://arxiv.org/abs/2501.14278)
- **作者**: Jaehyun Park, Dongmin Park, Jae-Gil Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) enables deep neural networks to adapt to ever-changing data distributions. In practice, there may be scenarios where annotation is costly, leading to active continual learning (ACL), which performs active learning (AL) for the CL scenarios when reducing the labeling cost by selecting the most informative subset is preferable. However, conventional AL strategies are not suitable for ACL, as they focus solely on learning the new knowledge, leading to catastrophic forgetting of previously learned tasks. Therefore, ACL requires a new AL strategy that can balance the prevention of catastrophic forgetting and the ability to quickly learn new tasks. In this paper, we propose AccuACL, Accumulated informativeness-based Active Continual Learning, by the novel use of the Fisher information matrix as a criterion for sample selection, derived from a theoretical analysis of the Fisher-optimality preservation properties within the framework of ACL, while also addressing the scalability issue of Fisher information-based AL. Extensive experiments demonstrate that AccuACL significantly outperforms AL baselines across various CL algorithms, increasing the average accuracy and forgetting by 23.8% and 17.0%, respectively, on average.

</details>

### Federated Continual Learning Goes Online: Uncertainty-Aware Memory Management for Vision Tasks and Beyond.
- **链接**: [出版页](https://openreview.net/forum?id=f65RuQgVlp)
- **作者**: Giuseppe Serra, Florian Buettner
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Theory on Mixture-of-Experts in Continual Learning.
- **链接**: [arXiv:2406.16437](https://arxiv.org/abs/2406.16437)
- **作者**: Hongbo Li, Sen Lin, Lingjie Duan, Yingbin Liang, Ness B. Shroff
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) has garnered significant attention because of its ability to adapt to new tasks that arrive over time. Catastrophic forgetting (of old tasks) has been identified as a major issue in CL, as the model adapts to new tasks. The Mixture-of-Experts (MoE) model has recently been shown to effectively mitigate catastrophic forgetting in CL, by employing a gating network to sparsify and distribute diverse tasks among multiple experts. However, there is a lack of theoretical analysis of MoE and its impact on the learning performance in CL. This paper provides the first theoretical results to characterize the impact of MoE in CL via the lens of overparameterized linear regression tasks. We establish the benefit of MoE over a single expert by proving that the MoE model can diversify its experts to specialize in different tasks, while its router learns to select the right expert for each task and balance the loads across all experts. Our study further suggests an intriguing fact that the MoE in CL needs to terminate the update of the gating network after sufficient training rounds to attain system convergence, which is not needed in the existing MoE studies that do not consider the continual task arrival. Furthermore, we provide explicit expressions for the expected forgetting and overall generalization error to characterize the benefit of MoE in the learning performance in CL. Interestingly, adding more experts requires additional rounds before convergence, which may not enhance the learning performance. Finally, we conduct experiments on both synthetic and real datasets to extend these insights from linear models to deep neural networks (DNNs), which also shed light on the practical algorithm design for MoE in CL.

</details>

### Adaptive Retention & Correction: Test-Time Training for Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=9bLdbp46Q1)
- **作者**: Haoran Chen, Micah Goldblum, Zuxuan Wu, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### CLDyB: Towards Dynamic Benchmarking for Continual Learning with Pre-trained Models.
- **链接**: [arXiv:2503.04655](https://arxiv.org/abs/2503.04655) · [代码](https://github.com/szc12153/CLDyB)
- **作者**: Shengzhuang Chen, Yikai Liao, Xiaoxiao Sun, Kede Ma, Ying Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of the foundation model era has sparked significant research interest in leveraging pre-trained representations for continual learning (CL), yielding a series of top-performing CL methods on standard evaluation benchmarks. Nonetheless, there are growing concerns regarding potential data contamination during the pre-training stage. Furthermore, standard evaluation benchmarks, which are typically static, fail to capture the complexities of real-world CL scenarios, resulting in saturated performance. To address these issues, we describe CL on dynamic benchmarks (CLDyB), a general computational framework based on Markov decision processes for evaluating CL methods reliably. CLDyB dynamically identifies inherently difficult and algorithm-dependent tasks for the given CL methods, and determines challenging task orders using Monte Carlo tree search. Leveraging CLDyB, we first conduct a joint evaluation of multiple state-of-the-art CL methods, leading to a set of commonly challenging and generalizable task sequences where existing CL methods tend to perform poorly. We then conduct separate evaluations of individual CL methods using CLDyB, discovering their respective strengths and weaknesses. The source code and generated task sequences are publicly accessible at https://github.com/szc12153/CLDyB.

</details>

### STAR: Stability-Inducing Weight Perturbation for Continual Learning.
- **链接**: [arXiv:2503.01595](https://arxiv.org/abs/2503.01595)
- **作者**: Masih Eskandar, Tooba Imtiaz, Davin Hill, Zifeng Wang, Jennifer G. Dy
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans can naturally learn new and varying tasks in a sequential manner. Continual learning is a class of learning algorithms that updates its learned model as it sees new data (on potentially new tasks) in a sequence. A key challenge in continual learning is that as the model is updated to learn new tasks, it becomes susceptible to catastrophic forgetting, where knowledge of previously learned tasks is lost. A popular approach to mitigate forgetting during continual learning is to maintain a small buffer of previously-seen samples and to replay them during training. However, this approach is limited by the small buffer size, and while forgetting is reduced, it is still present. In this paper, we propose a novel loss function, STAR, that exploits the worst-case parameter perturbation that reduces the KL-divergence of model predictions with that of its local parameter neighborhood to promote stability and alleviate forgetting. STAR can be combined with almost any existing rehearsal-based method as a plug-and-play component. We empirically show that STAR consistently improves the performance of existing methods by up to 15% across varying baselines and achieves superior or competitive accuracy to that of state-of-the-art methods aimed at improving rehearsal-based continual learning.

</details>

### Self-Normalized Resets for Plasticity in Continual Learning.
- **链接**: [arXiv:2410.20098](https://arxiv.org/abs/2410.20098)
- **作者**: Vivek F. Farias, Adam Daniel Jozefiak
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Plasticity Loss is an increasingly important phenomenon that refers to the empirical observation that as a neural network is continually trained on a sequence of changing tasks, its ability to adapt to a new task diminishes over time. We introduce Self-Normalized Resets (SNR), a simple adaptive algorithm that mitigates plasticity loss by resetting a neuron's weights when evidence suggests its firing rate has effectively dropped to zero. Across a battery of continual learning problems and network architectures, we demonstrate that SNR consistently attains superior performance compared to its competitor algorithms. We also demonstrate that SNR is robust to its sole hyperparameter, its rejection percentile threshold, while competitor algorithms show significant sensitivity. SNR's threshold-based reset mechanism is motivated by a simple hypothesis test that we derive. Seen through the lens of this hypothesis test, competing reset proposals yield suboptimal error rates in correctly detecting inactive neurons, potentially explaining our experimental observations. We also conduct a theoretical investigation of the optimization landscape for the problem of learning a single ReLU. We show that even when initialized adversarially, an idealized version of SNR learns the target ReLU, while regularization based approaches can fail to learn.

</details>

### Advancing Prompt-Based Methods for Replay-Independent General Continual Learning.
- **链接**: [arXiv:2503.00677](https://arxiv.org/abs/2503.00677) · [代码](https://github.com/kangzhiq/MISA)
- **作者**: Zhiqi Kang, Liyuan Wang, Xingxing Zhang, Karteek Alahari
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> General continual learning (GCL) is a broad concept to describe real-world continual learning (CL) problems, which are often characterized by online data streams without distinct transitions between tasks, i.e., blurry task boundaries. Such requirements result in poor initial performance, limited generalizability, and severe catastrophic forgetting, heavily impacting the effectiveness of mainstream GCL models trained from scratch. While the use of a frozen pretrained backbone with appropriate prompt tuning can partially address these challenges, such prompt-based methods remain suboptimal for CL of remaining tunable parameters on the fly. In this regard, we propose an innovative approach named MISA (Mask and Initial Session Adaption) to advance prompt-based methods in GCL. It includes a forgetting-aware initial session adaption that employs pretraining data to initialize prompt parameters and improve generalizability, as well as a non-parametric logit mask of the output layers to mitigate catastrophic forgetting. Empirical results demonstrate substantial performance gains of our approach compared to recent competitors, especially without a replay buffer (e.g., up to 18.39%, 22.06%, and 11.96% performance lead on CIFAR-100, Tiny-ImageNet, and ImageNet-R, respectively). Moreover, our approach features the plug-in nature for prompt-based methods, independence of replay, ease of implementation, and avoidance of CL-relevant hyperparameters, serving as a strong baseline for GCL research. Our source code is publicly available at https://github.com/kangzhiq/MISA

</details>

### Optimal Protocols for Continual Learning via Statistical Physics and Control Theory.
- **链接**: [arXiv:2409.18061](https://arxiv.org/abs/2409.18061) · 📚 被引 3
- **作者**: Francesco Mori, Stefano Sarao Mannelli, Francesca Mignacco
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Artificial neural networks often struggle with catastrophic forgetting when learning multiple tasks sequentially, as training on new tasks degrades the performance on previously learned tasks. Recent theoretical work has addressed this issue by analysing learning curves in synthetic frameworks under predefined training protocols. However, these protocols relied on heuristics and lacked a solid theoretical foundation assessing their optimality. In this paper, we fill this gap by combining exact equations for training dynamics, derived using statistical physics techniques, with optimal control methods. We apply this approach to teacher-student models for continual learning and multi-task problems, obtaining a theory for task-selection protocols maximising performance while minimising forgetting. Our theoretical analysis offers non-trivial yet interpretable strategies for mitigating catastrophic forgetting, shedding light on how optimal learning protocols modulate established effects, such as the influence of task similarity on forgetting. Finally, we validate our theoretical findings with experiments on real-world data.

</details>

### LoRanPAC: Low-rank Random Features and Pre-trained Models for Bridging Theory and Practice in Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=bqv7M0wc4x)
- **作者**: Liangzu Peng, Juan Elenter, Joshua Agterberg, Alejandro Ribeiro, René Vidal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### MIRACLE 3D: Memory-efficient Integrated Robust Approach for Continual Learning on 3D Point Clouds via Shape Model Construction.
- **链接**: [出版页](https://openreview.net/forum?id=ANBuEJesgx)
- **作者**: Hossein Resani, Behrooz Nasihatkon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning.
- **链接**: [arXiv:2410.17961](https://arxiv.org/abs/2410.17961) · [代码](https://github.com/aimagelab/fed-mammoth)
- **作者**: Riccardo Salami, Pietro Buzzega, Matteo Mosconi, Jacopo Bonato, Luigi Sabetta, Simone Calderara
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model merging has emerged as a crucial technique in Deep Learning, enabling the integration of multiple models into a unified system while preserving perfor-mance and scalability. In this respect, the compositional properties of low-rank adaptation techniques (e.g., LoRA) have proven beneficial, as simple averaging LoRA modules yields a single model that mostly integrates the capabilities of all individual modules. Building on LoRA, we take a step further by imposing that the merged model matches the responses of all learned modules. Solving this objective in closed form yields an indeterminate system with A and B as unknown variables, indicating the existence of infinitely many closed-form solutions. To address this challenge, we introduce LoRM, an alternating optimization strategy that trains one LoRA matrix at a time. This allows solving for each unknown variable individually, thus finding a unique solution. We apply our proposed methodology to Federated Class-Incremental Learning (FCIL), ensuring alignment of model responses both between clients and across tasks. Our method demonstrates state-of-the-art performance across a range of FCIL scenarios. The code to reproduce our experiments is available at github.com/aimagelab/fed-mammoth.

</details>

### Budgeted Online Continual Learning by Adaptive Layer Freezing and Frequency-based Sampling.
- **链接**: [arXiv:2410.15143](https://arxiv.org/abs/2410.15143)
- **作者**: Minhyuk Seo, Hyunseo Koh, Jonghyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The majority of online continual learning (CL) advocates single-epoch training and imposes restrictions on the size of replay memory. However, single-epoch training would incur a different amount of computations per CL algorithm, and the additional storage cost to store logit or model in addition to replay memory is largely ignored in calculating the storage budget. Arguing different computational and storage budgets hinder fair comparison among CL algorithms in practice, we propose to use floating point operations (FLOPs) and total memory size in Byte as a metric for computational and memory budgets, respectively, to compare and develop CL algorithms in the same 'total resource budget.' To improve a CL method in a limited total budget, we propose adaptive layer freezing that does not update the layers for less informative batches to reduce computational costs with a negligible loss of accuracy. In addition, we propose a memory retrieval method that allows the model to learn the same amount of knowledge as using random retrieval in fewer iterations. Empirical validations on the CIFAR-10/100, CLEAR-10/100, and ImageNet-1K datasets demonstrate that the proposed approach outperforms the state-of-the-art methods within the same total budget

</details>

### Coreset Selection via Reducible Loss in Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=mAztx8QO3B)
- **作者**: Ruilin Tong, Yuhang Liu, Javen Qinfeng Shi, Dong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Boosting Multiple Views for pretrained-based Continual Learning.
- **链接**: [出版页](https://openreview.net/forum?id=AZR4R3lw7y)
- **作者**: Quyen Tran, Tung Lam Tran, Khanh Doan, Toan Tran, Dinh Q. Phung, Khoat Than et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Meta-Continual Learning of Neural Fields.
- **链接**: [arXiv:2504.05806](https://arxiv.org/abs/2504.05806) · [代码](https://github.com/seungyoon-woo/mcl-nf)
- **作者**: Seungyoon Woo, Junhyeog Yun, Gunhee Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Fields (NF) have gained prominence as a versatile framework for complex data representation. This work unveils a new problem setting termed \emph{Meta-Continual Learning of Neural Fields} (MCL-NF) and introduces a novel strategy that employs a modular architecture combined with optimization-based meta-learning. Focused on overcoming the limitations of existing methods for continual learning of neural fields, such as catastrophic forgetting and slow convergence, our strategy achieves high-quality reconstruction with significantly improved learning speed. We further introduce Fisher Information Maximization loss for neural radiance fields (FIM-NeRF), which maximizes information gains at the sample level to enhance learning generalization, with proved convergence guarantee and generalization bound. We perform extensive evaluations across image, audio, video reconstruction, and view synthesis tasks on six diverse datasets, demonstrating our method's superiority in reconstruction quality and speed over existing MCL and CL-NF approaches. Notably, our approach attains rapid adaptation of neural fields for city-scale NeRF rendering with reduced parameter requirement. Code is available at https://github.com/seungyoon-woo/mcl-nf.

</details>

### Spurious Forgetting in Continual Learning of Language Models.
- **链接**: [arXiv:2501.13453](https://arxiv.org/abs/2501.13453)
- **作者**: Junhao Zheng, Xidi Cai, Shengjie Qiu, Qianli Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in large language models (LLMs) reveal a perplexing phenomenon in continual learning: despite extensive training, models experience significant performance declines, raising questions about task alignment and underlying knowledge retention. This study first explores the concept of "spurious forgetting", proposing that such performance drops often reflect a decline in task alignment rather than true knowledge loss. Through controlled experiments with a synthesized dataset, we investigate the dynamics of model performance during the initial training phases of new tasks, discovering that early optimization steps can disrupt previously established task alignments. Our theoretical analysis connects these shifts to orthogonal updates in model weights, providing a robust framework for understanding this behavior. Ultimately, we introduce a Freezing strategy that fix the bottom layers of the model, leading to substantial improvements in four continual learning scenarios. Our findings underscore the critical distinction between task alignment and knowledge retention, paving the way for more effective strategies in continual learning.

</details>

### BrainUICL: An Unsupervised Individual Continual Learning Framework for EEG Applications.
- **链接**: [出版页](https://openreview.net/forum?id=6jjAYmppGQ)
- **作者**: Yangxuan Zhou, Sha Zhao, Jiquan Wang, Haiteng Jiang, Shijian Li, Tao Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### LOIRE: LifelOng learning on Incremental data via pre-trained language model gRowth Efficiently.
- **链接**: [出版页](https://openreview.net/forum?id=F5PlYMC5ik)
- **作者**: Xue Han, Yitong Wang, Junlan Feng, Wenchun Gao, Qian Hu, Chao Deng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Prototype antithesis for biological few-shot class-incremental learning.
- **链接**: [出版页](https://openreview.net/forum?id=bRqaHn3J5I)
- **作者**: Binghao Liu, Han Yang, Fang Wan, Fei Gu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Federated Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=ZiPoAlKf9Y)
- **作者**: Muhammad Anwar Ma'sum, Mahardhika Pratama, Lin Liu, Habibullah, Ryszard Kowalczyk
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Federated Class-Incremental Learning: A Hybrid Approach Using Latent Exemplars and Data-Free Techniques to Address Local and Global Forgetting.
- **链接**: [arXiv:2501.15356](https://arxiv.org/abs/2501.15356)
- **作者**: Milad Khademi Nori, Il-Min Kim, Guanghui Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated Class-Incremental Learning (FCIL) refers to a scenario where a dynamically changing number of clients collaboratively learn an ever-increasing number of incoming tasks. FCIL is known to suffer from local forgetting due to class imbalance at each client and global forgetting due to class imbalance across clients. We develop a mathematical framework for FCIL that formulates local and global forgetting. Then, we propose an approach called Hybrid Rehearsal (HR), which utilizes latent exemplars and data-free techniques to address local and global forgetting, respectively. HR employs a customized autoencoder designed for both data classification and the generation of synthetic data. To determine the embeddings of new tasks for all clients in the latent space of the encoder, the server uses the Lennard-Jones Potential formulations. Meanwhile, at the clients, the decoder decodes the stored low-dimensional latent space exemplars back to the high-dimensional input space, used to address local forgetting. To overcome global forgetting, the decoder generates synthetic data. Furthermore, our mathematical framework proves that our proposed approach HR can, in principle, tackle the two local and global forgetting challenges. In practice, extensive experiments demonstrate that while preserving privacy, our proposed approach outperforms the state-of-the-art baselines on multiple FCIL benchmarks with low compute and memory footprints.

</details>

### A Second-Order Perspective on Model Compositionality and Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=OZVTqoli2N)
- **作者**: Angelo Porrello, Lorenzo Bonicelli, Pietro Buzzega, Monica Millunzi, Simone Calderara, Rita Cucchiara
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### SD-LoRA: Scalable Decoupled Low-Rank Adaptation for Class Incremental Learning.
- **链接**: [出版页](https://openreview.net/forum?id=5U1rlpX68A)
- **作者**: Yichen Wu, Hongming Piao, Long-Kai Huang, Renzhen Wang, Wanhua Li, Hanspeter Pfister et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
