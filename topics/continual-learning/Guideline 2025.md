# Continual Learning — 2025 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OVS Meets Continual Learning: Towards Sustainable Open-Vocabulary Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/184cfed554856b4812b19cd0235a0f6a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dongjun Hwang, Yejin Kim, Minyoung Lee, Seong Joon Oh, Junsuk Choe
- **🏷️ 机构**: Sogang University, University of Tübingen
- **会议**: NeurIPS 2025

### Mitigating Intra- and Inter-modal Forgetting in Continual Learning of Unified Multimodal Models.
- **链接**: [arXiv:2512.03125](https://arxiv.org/abs/2512.03125) · [代码](https://github.com/Christina200/MoDE-official.git) · 📚 被引 0
- **作者**: Xiwen Wei, Mustafa Munir, Radu Marculescu
- **🏷️ 机构**: University of Texas at Austin, University of Texas, Austin
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unified Multimodal Generative Models (UMGMs) unify visual understanding and image generation within a single autoregressive framework. However, their ability to continually learn new tasks is severely hindered by catastrophic forgetting, both within a modality (intra-modal) and across modalities (inter-modal). While intra-modal forgetting has been studied in prior continual learning (CL) work, inter-modal forgetting remains largely unexplored. In this paper, we identify and empirically validate this phenomenon in UMGMs and provide a theoretical explanation rooted in gradient conflict between modalities. To address both intra- and inter-modal forgetting, we propose Modality-Decoupled Experts (MoDE), a lightweight and scalable architecture that isolates modality-specific updates to mitigate the gradient conflict and leverages knowledge distillation to prevent catastrophic forgetting and preserve pre-trained capabilities. Unlike previous CL methods that remain modality-coupled and suffer from modality gradient conflict, MoDE explicitly decouples modalities to prevent interference. Experiments across diverse benchmarks demonstrate that MoDE significantly mitigates both inter- and intra-modal forgetting, outperforming prior CL baselines in unified multimodal generation settings. Codes will be publicly available: https://github.com/Christina200/MoDE-official.git

</details>

### Confusion-Driven Self-Supervised Progressively Weighted Ensemble Learning for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6e1a97dfd2ce57ee4c006657ace4b9b6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Kai Hu, Yu Zhang, Yuan Zhang, Zhineng Chen, Xieping Gao
- **🏷️ 机构**: Xiangtan University, Communication University of China, Fudan University
- **会议**: NeurIPS 2025

### AnaCP: Toward Upper-Bound Continual Learning via Analytic Contrastive Projection.
- **链接**: [arXiv:2511.13880](https://arxiv.org/abs/2511.13880) · 📚 被引 0
- **作者**: Saleh Momeni, Changnan Xiao, Bing Liu
- **🏷️ 机构**: University of Illinois at Chicago, MiHoYo
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies the problem of class-incremental learning (CIL), a core setting within continual learning where a model learns a sequence of tasks, each containing a distinct set of classes. Traditional CIL methods, which do not leverage pre-trained models (PTMs), suffer from catastrophic forgetting (CF) due to the need to incrementally learn both feature representations and the classifier. The integration of PTMs into CIL has recently led to efficient approaches that treat the PTM as a fixed feature extractor combined with analytic classifiers, achieving state-of-the-art performance. However, they still face a major limitation: the inability to continually adapt feature representations to best suit the CIL tasks, leading to suboptimal performance. To address this, we propose AnaCP (Analytic Contrastive Projection), a novel method that preserves the efficiency of analytic classifiers while enabling incremental feature adaptation without gradient-based training, thereby eliminating the CF caused by gradient updates. Our experiments show that AnaCP not only outperforms existing baselines but also achieves the accuracy level of joint training, which is regarded as the upper bound of CIL.

</details>

### Contrastive Consolidation of Top-Down Modulations Achieves Sparsely Supervised Continual Learning.
- **链接**: [arXiv:2505.14125](https://arxiv.org/abs/2505.14125) · 📚 被引 0
- **作者**: Viet Anh Khoa Tran, Emre Neftci, Willem Wybo
- **🏷️ 机构**: Forschungszentrum Jülich
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Biological brains learn continually from a stream of unlabeled data, while integrating specialized information from sparsely labeled examples without compromising their ability to generalize. Meanwhile, machine learning methods are susceptible to catastrophic forgetting in this natural learning setting, as supervised specialist fine-tuning degrades performance on the original task. We introduce task-modulated contrastive learning (TMCL), which takes inspiration from the biophysical machinery in the neocortex, using predictive coding principles to integrate top-down information continually and without supervision. We follow the idea that these principles build a view-invariant representation space, and that this can be implemented using a contrastive loss. Then, whenever labeled samples of a new class occur, new affine modulations are learned that improve separation of the new class from all others, without affecting feedforward weights. By co-opting the view-invariance learning mechanism, we then train feedforward weights to match the unmodulated representation of a data sample to its modulated counterparts. This introduces modulation invariance into the representation space, and, by also using past modulations, stabilizes it. Our experiments show improvements in both class-incremental and transfer learning over state-of-the-art unsupervised approaches, as well as over comparable supervised approaches, using as few as 1% of available labels. Taken together, our work suggests that top-down modulations play a crucial role in balancing stability and plasticity.

</details>

### Bisecle: Binding and Separation in Continual Learning for Video Language Understanding.
- **链接**: [arXiv:2507.00469](https://arxiv.org/abs/2507.00469) · 📚 被引 0
- **作者**: Yue Tan, Xiaoqian Hu, Hao Xue, Celso de Melo, Flora D. Salim
- **🏷️ 机构**: University of New South Wales, The University of Queensland, The Hong Kong University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Frontier vision-language models (VLMs) have made remarkable improvements in video understanding tasks. However, real-world videos typically exist as continuously evolving data streams (e.g., dynamic scenes captured by wearable glasses), necessitating models to continually adapt to shifting data distributions and novel scenarios. Considering the prohibitive computational costs of fine-tuning models on new tasks, usually, a small subset of parameters is updated while the bulk of the model remains frozen. This poses new challenges to existing continual learning frameworks in the context of large multimodal foundation models, i.e., catastrophic forgetting and update conflict. While the foundation models struggle with parameter-efficient continual learning, the hippocampus in the human brain has evolved highly efficient mechanisms for memory formation and consolidation. Inspired by the rapid Binding and pattern separation mechanisms in the hippocampus, in this work, we propose Bisecle for video-language continual learning, where a multi-directional supervision module is used to capture more cross-modal relationships and a contrastive prompt learning scheme is designed to isolate task-specific knowledge to facilitate efficient memory storage. Binding and separation processes further strengthen the ability of VLMs to retain complex experiences, enabling robust and efficient continual learning in video understanding tasks. We perform a thorough evaluation of the proposed Bisecle, demonstrating its ability to mitigate forgetting and enhance cross-task generalization on several VideoQA benchmarks.

</details>

### Learning Multi-Source and Robust Representations for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/fff5dac3713ad2d1cf7c9e3c95cc361f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Fei Ye, YongCheng Zhong, Qihe Liu, Adrian G. Bors, Jingling Sun, Rongyao Hu et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, University of York
- **会议**: NeurIPS 2025

### Learning Expandable and Adaptable Representations for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4c19a67a61b5700f90ccb815a255aaad-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ruilong Yu, Mingyan Liu, Fei Ye, Adrian G. Bors, Rongyao Hu, Jingling Sun et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, Harbin Institute of Technology, Shenzhen, University of York
- **会议**: NeurIPS 2025

### Continuous Subspace Optimization for Continual Learning.
- **链接**: [arXiv:2505.11816](https://arxiv.org/abs/2505.11816) · 📚 被引 0
- **作者**: Quan Cheng, Yuanyu Wan, Lingyu Wu, Chenping Hou, Lijun Zhang
- **🏷️ 机构**: Nanjing University, Zhejiang University, National University of Defense Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to learn multiple tasks sequentially while preserving prior knowledge, but faces the challenge of catastrophic forgetting when adapting to new tasks. Recently, approaches leveraging pre-trained models have gained increasing popularity in mitigating this issue, due to the strong generalization ability of foundation models. To adjust pre-trained models for new tasks, existing methods usually employ low-rank adaptation, which restricts parameter updates to a fixed low-rank subspace. However, constraining the optimization space inherently compromises the model's learning capacity, resulting in inferior performance. To address this limitation, we propose Continuous Subspace Optimization for Continual Learning (CoSO) to fine-tune the model in a series of subspaces rather than a single one. These sequential subspaces are dynamically determined through the singular value decomposition of the gradients. CoSO updates the model by projecting gradients onto these subspaces, ensuring memory-efficient optimization. To mitigate forgetting, the optimization subspace of each task is constrained to be orthogonal to the historical task subspace. During task learning, CoSO maintains a task-specific component that captures the critical update directions for the current task. Upon completing a task, this component is used to update the historical task subspace, laying the groundwork for subsequent learning. Extensive experiments on multiple datasets demonstrate that CoSO significantly outperforms state-of-the-art methods, especially in challenging scenarios with long task sequences.

</details>

### REP: Resource-Efficient Prompting for Rehearsal-Free Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/59ea33ae3d096f3bcd5026b479710cf8-Abstract-Conference.html) · 📚 被引 0
- **作者**: Sungho Jeon, Xinyue Ma, Kwang In Kim, Myeongjae Jeon
- **🏷️ 机构**: POSTECH, Ulsan National Institute of Science and Technology, Pohang University of Science and Technology
- **会议**: NeurIPS 2025

### Gradient-Guided Epsilon Constraint Method for Online Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b3c2854d9e94282a373d8fa58b567b27-Abstract-Conference.html) · 📚 被引 0
- **作者**: Song Lai, Changyi Ma, Fei Zhu, Zhe Zhao, Xi Lin, Gaofeng Meng et al.
- **🏷️ 机构**: City University of Hong Kong, The Chinese University of Hong Kong, Centre for Artificial Intelligence and Robotics Hong Kong Institute of Science &amp; Innovation, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### Resource-Constrained Federated Continual Learning: What Does Matter?
- **链接**: [arXiv:2501.08737](https://arxiv.org/abs/2501.08737) · 📚 被引 0
- **作者**: Yichen Li, Yuying Wang, Jiahua Dong, Haozhao Wang, Yining Qi, Rui Zhang et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Suzhou University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated Continual Learning (FCL) aims to enable sequentially privacy-preserving model training on streams of incoming data that vary in edge devices by preserving previous knowledge while adapting to new data. Current FCL literature focuses on restricted data privacy and access to previously seen data while imposing no constraints on the training overhead. This is unreasonable for FCL applications in real-world scenarios, where edge devices are primarily constrained by resources such as storage, computational budget, and label rate. We revisit this problem with a large-scale benchmark and analyze the performance of state-of-the-art FCL approaches under different resource-constrained settings. Various typical FCL techniques and six datasets in two incremental learning scenarios (Class-IL and Domain-IL) are involved in our experiments. Through extensive experiments amounting to a total of over 1,000+ GPU hours, we find that, under limited resource-constrained settings, existing FCL approaches, with no exception, fail to achieve the expected performance. Our conclusions are consistent in the sensitivity analysis. This suggests that most existing FCL methods are particularly too resource-dependent for real-world deployment. Moreover, we study the performance of typical FCL techniques with resource constraints and shed light on future research directions in FCL.

</details>

### Turning the Tables: Enabling Backward Transfer via Causal-Aware LoRA in Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7c22f3719c9699c0ea4fe47fb536ff82-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chaoyang Li, Runze Ye, Jianyang Qin, Jinhao Cui, Lingzhi Wang, Ning Hu et al.
- **🏷️ 机构**: Harbin Institute of Technology (Shenzhen), Harbin Institute of Technology, Harbin Institute of Technology, Shenzhen
- **会议**: NeurIPS 2025

### Gated Integration of Low-Rank Adaptation for Continual Learning of Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/63692d8d567db671c700df5df912204a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yan-Shuo Liang, Jia-Rui Chen, Wu-Jun Li
- **🏷️ 机构**: Nanjing University
- **会议**: NeurIPS 2025

### Temporal-Difference Variational Continual Learning.
- **链接**: [arXiv:2410.07812](https://arxiv.org/abs/2410.07812) · 📚 被引 0
- **作者**: Luckeciano Carvalho Melo, Alessandro Abate, Yarin Gal
- **🏷️ 机构**: University of Oxford
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine Learning models in real-world applications must continuously learn new tasks to adapt to shifts in the data-generating distribution. Yet, for Continual Learning (CL), models often struggle to balance learning new tasks (plasticity) with retaining previous knowledge (memory stability). Consequently, they are susceptible to Catastrophic Forgetting, which degrades performance and undermines the reliability of deployed systems. In the Bayesian CL literature, variational methods tackle this challenge by employing a learning objective that recursively updates the posterior distribution while constraining it to stay close to its previous estimate. Nonetheless, we argue that these methods may be ineffective due to compounding approximation errors over successive recursions. To mitigate this, we propose new learning objectives that integrate the regularization effects of multiple previous posterior estimations, preventing individual errors from dominating future posterior updates and compounding over time. We reveal insightful connections between these objectives and Temporal-Difference methods, a popular learning mechanism in Reinforcement Learning and Neuroscience. Experiments on challenging CL benchmarks show that our approach effectively mitigates Catastrophic Forgetting, outperforming strong Variational CL methods.

</details>

### Train with Perturbation, Infer after Merging: A Two-Stage Framework for Continual Learning.
- **链接**: [arXiv:2505.22389](https://arxiv.org/abs/2505.22389) · 📚 被引 0
- **作者**: Haomiao Qiu, Miao Zhang, Ziyue Qiao, Liqiang Nie
- **🏷️ 机构**: Harbin Institute of Technology, Shenzhen, Aalborg University, Great Bay University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning (CL) aims to enable models to continuously acquire new knowledge from a sequence of tasks with avoiding the forgetting of learned information. However, existing CL methods only rely on the parameters of the most recent task for inference, which makes them susceptible to catastrophic forgetting. Inspired by the recent success of model merging techniques, we propose \textbf{Perturb-and-Merge (P\&M)}, a novel continual learning framework that integrates model merging into the CL paradigm to mitigate forgetting. Specifically, after training on each task, P\&M constructs a new model by forming a convex combination of the previous model and the newly trained task-specific model. Through theoretical analysis, We minimize the total loss increase across all tasks and derive a closed-form solution for the merging coefficient under mild assumptions. To further improve the performance of the merged model, we observe that the degradation introduced during merging can be alleviated by a regularization term composed of the task vector and the Hessian matrix of the loss function. Interestingly, we show that this term can be efficiently approximated using second-order symmetric finite differences, and a stochastic perturbation strategy along the task vector direction is accordingly devised which incurs no additional forward or backward passes while providing an effective approximation of the regularization term. Finally, we combine P\&M with LoRA, a parameter-efficient fine-tuning method, to reduce memory overhead. Our proposed approach achieves state-of-the-art performance on several continual learning benchmark datasets. The code is available at https://github.com/qhmiao/P-M-for-Continual-Learning.

</details>

### Separating the 'what' and 'how' of compositional computation to enable reuse and continual learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/82d07a9f247048b85f78786ac80e6fbf-Abstract-Conference.html) · 📚 被引 0
- **作者**: Haozhe Shan, Minni Sun, Lea Duncker
- **🏷️ 机构**: Columbia University
- **会议**: NeurIPS 2025

### Dual-Space Semantic Synergy Distillation for Continual Learning of Unlabeled Streams.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1eaa5146756be028ad6fff1efcc8e6bd-Abstract-Conference.html) · 📚 被引 0
- **作者**: Donghao Sun, Xi Wang, Xu Yang, Kun Wei, Cheng Deng
- **🏷️ 机构**: Xidian University, ETHZ - ETH Zurich, Microsoft
- **会议**: NeurIPS 2025

### Model Inversion with Layer-Specific Modeling and Alignment for Data-Free Continual Learning.
- **链接**: [arXiv:2510.26311](https://arxiv.org/abs/2510.26311) · 📚 被引 0
- **作者**: Ruilin Tong, Haodong Lu, Yuhang Liu, Dong Gong
- **🏷️ 机构**: University of New South Wales, The University of Adelaide, The University of New South Wales (UNSW)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to incrementally train a model on a sequence of tasks while retaining performance on prior ones. However, storing and replaying data is often infeasible due to privacy or security constraints and impractical for arbitrary pre-trained models. Data-free CL seeks to update models without access to previous data. Beyond regularization, we employ model inversion to synthesize data from the trained model, enabling replay without storing samples. Yet, model inversion in predictive models faces two challenges: (1) generating inputs solely from compressed output labels causes drift between synthetic and real data, and replaying such data can erode prior knowledge; (2) inversion is computationally expensive since each step backpropagates through the full model. These issues are amplified in large pre-trained models such as CLIP. To improve efficiency, we propose Per-layer Model Inversion (PMI), inspired by faster convergence in single-layer optimization. PMI provides strong initialization for full-model inversion, substantially reducing iterations. To mitigate feature shift, we model class-wise features via Gaussian distributions and contrastive model, ensuring alignment between synthetic and real features. Combining PMI and feature modeling, our approach enables continual learning of new classes by generating pseudo-images from semantic-aware projected features, achieving strong effectiveness and compatibility across multiple CL settings.

</details>

### The Dual Nature of Plasticity Loss in Deep Continual Learning: Dissection and Mitigation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6489f2c6ac6420124fcef2a489615a97-Abstract-Conference.html) · 📚 被引 0
- **作者**: Haoyu Wang, Wei Dai, Jiawei Zhang, Jialun Ma, Mingyi Huang, Yuguo Yu
- **🏷️ 机构**: Tianjin University, Fudan University
- **会议**: NeurIPS 2025

### Hybrid Re-matching for Continual Learning with Parameter-Efficient Tuning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a978bdfeb195e4a574c0def98806346a-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weicheng Wang, Guoli Jia, Xialei Liu, Liang Lin, Jufeng Yang
- **🏷️ 机构**: Nankai University, Tsinghua University, Sun Yat-Sen University
- **会议**: NeurIPS 2025

### Exploiting Task Relationships in Continual Learning via Transferability-Aware Task Embeddings.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f3e644506dad33613919fa85af6665d0-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yanru Wu, Jianning Wang, Xiangyu Chen, Aurora, Yang Tan, Hanbing Liu et al.
- **🏷️ 机构**: Tsinghua University, Harbin Institute of Technology, Tsinghua University, Tsinghua University
- **会议**: NeurIPS 2025

### C2Prompt: Class-aware Client Knowledge Interaction for Federated Continual Learning.
- **链接**: [arXiv:2509.19674](https://arxiv.org/abs/2509.19674) · 📚 被引 0
- **作者**: Kunlun Xu, Yibo Feng, Jiangmeng Li, Yongsheng Qi, Jiahuan Zhou
- **🏷️ 机构**: Peking University, University of Electronic Science and Technology of China, Institute of Software Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated continual learning (FCL) tackles scenarios of learning from continuously emerging task data across distributed clients, where the key challenge lies in addressing both temporal forgetting over time and spatial forgetting simultaneously. Recently, prompt-based FCL methods have shown advanced performance through task-wise prompt communication.In this study, we underscore that the existing prompt-based FCL methods are prone to class-wise knowledge coherence between prompts across clients. The class-wise knowledge coherence includes two aspects: (1) intra-class distribution gap across clients, which degrades the learned semantics across prompts, (2) inter-prompt class-wise relevance, which highlights cross-class knowledge confusion. During prompt communication, insufficient class-wise coherence exacerbates knowledge conflicts among new prompts and induces interference with old prompts, intensifying both spatial and temporal forgetting. To address these issues, we propose a novel Class-aware Client Knowledge Interaction (C${}^2$Prompt) method that explicitly enhances class-wise knowledge coherence during prompt communication. Specifically, a local class distribution compensation mechanism (LCDC) is introduced to reduce intra-class distribution disparities across clients, thereby reinforcing intra-class knowledge consistency. Additionally, a class-aware prompt aggregation scheme (CPA) is designed to alleviate inter-class knowledge confusion by selectively strengthening class-relevant knowledge aggregation. Extensive experiments on multiple FCL benchmarks demonstrate that C${}^2$Prompt achieves state-of-the-art performance. Our source code is available at https://github.com/zhoujiahuan1991/NeurIPS2025-C2Prompt

</details>

### Decentralized Dynamic Cooperation of Personalized Models for Federated Continual Learning.
- **链接**: [arXiv:2509.23683](https://arxiv.org/abs/2509.23683) · 📚 被引 0
- **作者**: Danni Yang, Zhikang Chen, Sen Cui, Mengyue Yang, Ding Li, Abudukelimu Wuerkaixi et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, University College London / University of Bristol
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated continual learning (FCL) has garnered increasing attention for its ability to support distributed computation in environments with evolving data distributions. However, the emergence of new tasks introduces both temporal and cross-client shifts, making catastrophic forgetting a critical challenge. Most existing works aggregate knowledge from clients into a global model, which may not enhance client performance since irrelevant knowledge could introduce interference, especially in heterogeneous scenarios. Additionally, directly applying decentralized approaches to FCL suffers from ineffective group formation caused by task changes. To address these challenges, we propose a decentralized dynamic cooperation framework for FCL, where clients establish dynamic cooperative learning coalitions to balance the acquisition of new knowledge and the retention of prior learning, thereby obtaining personalized models. To maximize model performance, each client engages in selective cooperation, dynamically allying with others who offer meaningful performance gains. This results in non-overlapping, variable coalitions at each stage of the task. Moreover, we use coalitional affinity game to simulate coalition relationships between clients. By assessing both client gradient coherence and model similarity, we quantify the client benefits derived from cooperation. We also propose a merge-blocking algorithm and a dynamic cooperative evolution algorithm to achieve cooperative and dynamic equilibrium. Comprehensive experiments demonstrate the superiority of our method compared to various baselines. Code is available at: https://github.com/ydn3229/DCFCL.

</details>

### Dynamic Siamese Expansion Framework for Improving Robustness in Online Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6749b4364bbdff0dedfab1b0f27a10c2-Abstract-Conference.html) · 📚 被引 1
- **作者**: Fei Ye, Yulong Zhao, Qihe Liu, Junlin Chen, Adrian G. Bors, Jingling Sun et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, ByteDance Inc., University of York
- **会议**: NeurIPS 2025

### Federated Continual Learning via Orchestrating Multi-Scale Expertise.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/20de741d21f1a038093c6e3ee7c09481-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xiaoyang Yi, Yang Liu, Binhan Yang, Jian Jun Zhang
- **🏷️ 机构**: Nankai University, Nanyang Technology University, Singapore, Vivo
- **会议**: NeurIPS 2025

### Online Functional Tensor Decomposition via Continual Learning for Streaming Data Completion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/3ba5c2a601f5d35b8072116bd192d174-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xi Zhang, Yanyi Li, Yisi Luo, Qi Xie, Deyu Meng
- **🏷️ 机构**: Nanyang Technological University, Xi'an Jiaotong University
- **会议**: NeurIPS 2025

### Policy Compatible Skill Incremental Learning via Lazy Learning Interface.
- **链接**: [arXiv:2509.20612](https://arxiv.org/abs/2509.20612) · 📚 被引 0
- **作者**: Daehee Lee, Dongsu Lee, TaeYoon Kwack, Wonje Choi, Honguk Woo
- **🏷️ 机构**: SungKyunKwan University, University of Texas at Austin, Sungkyunkwan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Skill Incremental Learning (SIL) is the process by which an embodied agent expands and refines its skill set over time by leveraging experience gained through interaction with its environment or by the integration of additional data. SIL facilitates efficient acquisition of hierarchical policies grounded in reusable skills for downstream tasks. However, as the skill repertoire evolves, it can disrupt compatibility with existing skill-based policies, limiting their reusability and generalization. In this work, we propose SIL-C, a novel framework that ensures skill-policy compatibility, allowing improvements in incrementally learned skills to enhance the performance of downstream policies without requiring policy re-training or structural adaptation. SIL-C employs a bilateral lazy learning-based mapping technique to dynamically align the subtask space referenced by policies with the skill space decoded into agent behaviors. This enables each subtask, derived from the policy's decomposition of a complex task, to be executed by selecting an appropriate skill based on trajectory distribution similarity. We evaluate SIL-C across diverse SIL scenarios and demonstrate that it maintains compatibility between evolving skills and downstream policies while ensuring efficiency throughout the learning process.

</details>

### Knowledge Graph Enhanced Generative Multi-modal Models for Class-Incremental Learning.
- **链接**: [arXiv:2503.18403](https://arxiv.org/abs/2503.18403) · 📚 被引 0
- **作者**: Xusheng Cao, Haori Lu, Linlan Huang, Fei Yang, Xialei Liu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University, Adobe Systems
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning in computer vision faces the critical challenge of catastrophic forgetting, where models struggle to retain prior knowledge while adapting to new tasks. Although recent studies have attempted to leverage the generalization capabilities of pre-trained models to mitigate overfitting on current tasks, models still tend to forget details of previously learned categories as tasks progress, leading to misclassification. To address these limitations, we introduce a novel Knowledge Graph Enhanced Generative Multi-modal model (KG-GMM) that builds an evolving knowledge graph throughout the learning process. Our approach utilizes relationships within the knowledge graph to augment the class labels and assigns different relations to similar categories to enhance model differentiation. During testing, we propose a Knowledge Graph Augmented Inference method that locates specific categories by analyzing relationships within the generated text, thereby reducing the loss of detailed information about old classes when learning new knowledge and alleviating forgetting. Experiments demonstrate that our method effectively leverages relational information to help the model correct mispredictions, achieving state-of-the-art results in both conventional CIL and few-shot CIL settings, confirming the efficacy of knowledge graphs at preserving knowledge in the continual learning scenarios.

</details>

### A Minimalistic Unified Framework for Incremental Learning across Image Restoration Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/30d0278f200f91407364eba31bee08dd-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xiaoxuan Gong, Jie Ma
- **🏷️ 机构**: Huazhong University of Science and Technology
- **会议**: NeurIPS 2025

### Learn and Ensemble Bridge Adapters for Multi-domain Task Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e9cbf616dac568a9cb3342761125db24-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ziqi Gu, Chunyan Xu, Wenxuan Fang, Xin Liu, Yide Qiu, Zhen Cui
- **🏷️ 机构**: Nanjing University of Science and Technology, Google, Beijing Normal University
- **会议**: NeurIPS 2025

### GraphKeeper: Graph Domain-Incremental Learning via Knowledge Disentanglement and Preservation.
- **链接**: [arXiv:2511.00097](https://arxiv.org/abs/2511.00097) · 📚 被引 0
- **作者**: Zihao Guo, Qingyun Sun, Ziwei Zhang, Haonan Yuan, Huiping Zhuang, Xingcheng Fu et al.
- **🏷️ 机构**: Beijing University of Aeronautics and Astronautics, Beihang University, South China University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph incremental learning (GIL), which continuously updates graph models by sequential knowledge acquisition, has garnered significant interest recently. However, existing GIL approaches focus on task-incremental and class-incremental scenarios within a single domain. Graph domain-incremental learning (Domain-IL), aiming at updating models across multiple graph domains, has become critical with the development of graph foundation models (GFMs), but remains unexplored in the literature. In this paper, we propose Graph Domain-Incremental Learning via Knowledge Dientanglement and Preservation (GraphKeeper), to address catastrophic forgetting in Domain-IL scenario from the perspectives of embedding shifts and decision boundary deviations. Specifically, to prevent embedding shifts and confusion across incremental graph domains, we first propose the domain-specific parameter-efficient fine-tuning together with intra- and inter-domain disentanglement objectives. Consequently, to maintain a stable decision boundary, we introduce deviation-free knowledge preservation to continuously fit incremental domains. Additionally, for graphs with unobservable domains, we perform domain-aware distribution discrimination to obtain precise embeddings. Extensive experiments demonstrate the proposed GraphKeeper achieves state-of-the-art results with 6.5%~16.6% improvement over the runner-up with negligible forgetting. Moreover, we show GraphKeeper can be seamlessly integrated with various representative GFMs, highlighting its broad applicative potential.

</details>

### Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning.
- **链接**: [arXiv:2509.16738](https://arxiv.org/abs/2509.16738) · 📚 被引 1
- **作者**: Kai Jiang, Zhengyan Shi, Dell Zhang, Hongyuan Zhang, Xuelong Li
- **🏷️ 机构**: Tsinghua University, Microsoft Research, Institute of Artificial Intelligence (TeleAI), China Telecom
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) aims to continuously learn new categories while retaining the knowledge of old ones. Pre-trained models (PTMs) show promising capabilities in CIL. However, existing approaches that apply lightweight fine-tuning to backbones still induce parameter drift, thereby compromising the generalization capability of pre-trained models. Parameter drift can be conceptualized as a form of noise that obscures critical patterns learned for previous tasks. However, recent researches have shown that noise is not always harmful. For example, the large number of visual patterns learned from pre-training can be easily abused by a single task, and introducing appropriate noise can suppress some low-correlation features, thus leaving a margin for future tasks. To this end, we propose learning beneficial noise for CIL guided by information theory and propose Mixture of Noise (Min), aiming to mitigate the degradation of backbone generalization from adapting new tasks. Specifically, task-specific noise is learned from high-dimension features of new tasks. Then, a set of weights is adjusted dynamically for optimal mixture of different task noise. Finally, Min embeds the beneficial noise into the intermediate features to mask the response of inefficient patterns. Extensive experiments on six benchmark datasets demonstrate that Min achieves state-of-the-art performance in most incremental settings, with particularly outstanding results in 50-steps incremental settings. This shows the significant potential for beneficial noise in continual learning. Code is available at https://github.com/ASCIIJK/MiN-NeurIPS2025.

</details>

### Class-wise Balancing Data Replay for Federated Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d611d06e3207330555fbc10810e70163-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhuang Qi, Ying-Peng Tang, Lei Meng, Han Yu, Xiaoxiao Li, Xiangxu Meng
- **🏷️ 机构**: Shandong University, Nanyang Technological University, Nanyang Technological University (NTU)
- **会议**: NeurIPS 2025

### Evolving and Regularizing Meta-Environment Learner for Fine-Grained Few-Shot Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/376b1b131609e764f687afca832e62b3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Li-Jun Zhao, Zhen-Duo Chen, Yongxin Wang, Xin Luo, Xin-Shun Xu
- **🏷️ 机构**: Shandong University, MBZUAI
- **会议**: NeurIPS 2025
