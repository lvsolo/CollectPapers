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
- **链接**: [arXiv:2512.03125](https://arxiv.org/abs/2512.03125) · 📚 被引 0
- **作者**: Xiwen Wei, Mustafa Munir, Radu Marculescu
- **🏷️ 机构**: University of Texas at Austin, University of Texas, Austin
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Advances in medical imaging and deep learning have propelled progress in whole slide image (WSI) analysis, with multiple instance learning (MIL) showing promise for efficient and accurate diagnostics. However, conventional MIL models often lack adaptability to evolving datasets, as they rely on static training that cannot incorporate new information without extensive retraining. Applying continual learning (CL) to MIL models is a possible solution, but often sees limited improvements. In this paper, we analyze CL in the context of attention MIL models and find that the model forgetting is mainly concentrated in the attention layers of the MIL model. Using the results of this analysis we propose two components for improving CL on MIL: Attention Knowledge Distillation (AKD) and the Pseudo-Bag Memory Pool (PMP). AKD mitigates catastrophic forgetting by focusing on retaining attention layer knowledge between learning sessions, while PMP reduces the memory footprint by selectively storing only the most informative patches, or ``pseudo-bags'' from WSIs. Experimental evaluations demonstrate that our method significantly improves both accuracy and memory efficiency on diverse WSI datasets, outperforming current state-of-the-art CL methods. This work provides a foundation for CL in large-scale, weakly annotated clinical datasets, paving the way for more adaptable and resilient diagnostic models.

</details>

### Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning.
- **链接**: [arXiv:2403.18886](https://arxiv.org/abs/2403.18886) · [代码](https://github.com/huiyiwang01/SEMA-CL) · 📚 被引 15
- **作者**: Huiyi Wang, Haodong Lu, Lina Yao, Dong Gong
- **🏷️ 机构**: University of New South Wales, CSIRO&#x2019;s Data61
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to continually accumulate knowledge from a non-stationary data stream without catastrophic forgetting of learned knowledge, requiring a balance between stability and adaptability. Relying on the generalizable representation in pre-trained models (PTMs), PTM-based CL methods perform effective continual adaptation on downstream tasks by adding learnable adapters or prompts upon the frozen PTMs. However, many existing PTM-based CL methods use restricted adaptation on a fixed set of these modules to avoid forgetting, suffering from limited CL ability. Periodically adding task-specific modules results in linear model growth rate and impaired knowledge reuse. We propose Self-Expansion of pre-trained models with Modularized Adaptation (SEMA), a novel approach to enhance the control of stability-plasticity balance in PTM-based CL. SEMA automatically decides to reuse or add adapter modules on demand in CL, depending on whether significant distribution shift that cannot be handled is detected at different representation levels. We design modular adapter consisting of a functional adapter and a representation descriptor. The representation descriptors are trained as a distribution shift indicator and used to trigger self-expansion signals. For better composing the adapters, an expandable weighting router is learned jointly for mixture of adapter outputs. SEMA enables better knowledge reuse and sub-linear expansion rate. Extensive experiments demonstrate the effectiveness of the proposed self-expansion method, achieving state-of-the-art performance compared to PTM-based CL methods without memory rehearsal. Code is available at https://github.com/huiyiwang01/SEMA-CL.

</details>

### Learning Expandable and Adaptable Representations for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4c19a67a61b5700f90ccb815a255aaad-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ruilong Yu, Mingyan Liu, Fei Ye, Adrian G. Bors, Rongyao Hu, Jingling Sun et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, Harbin Institute of Technology, Shenzhen, University of York
- **会议**: NeurIPS 2025

### Language Guided Concept Bottleneck Models for Interpretable Continual Learning.
- **链接**: [arXiv:2503.23283](https://arxiv.org/abs/2503.23283) · 📚 被引 5
- **作者**: Lu Yu, Haoyu Han, Zhe Tao, Hantao Yao, Changsheng Xu
- **🏷️ 机构**: Tianjin University of Technology,School of Computer Science and Engineering, University of Science and Technology of China,School of Information Science and Technology, Institute of Automation, University of Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to enable learning systems to acquire new knowledge constantly without forgetting previously learned information. CL faces the challenge of mitigating catastrophic forgetting while maintaining interpretability across tasks. Most existing CL methods focus primarily on preserving learned knowledge to improve model performance. However, as new information is introduced, the interpretability of the learning process becomes crucial for understanding the evolving decision-making process, yet it is rarely explored. In this paper, we introduce a novel framework that integrates language-guided Concept Bottleneck Models (CBMs) to address both challenges. Our approach leverages the Concept Bottleneck Layer, aligning semantic consistency with CLIP models to learn human-understandable concepts that can generalize across tasks. By focusing on interpretable concepts, our method not only enhances the models ability to retain knowledge over time but also provides transparent decision-making insights. We demonstrate the effectiveness of our approach by achieving superior performance on several datasets, outperforming state-of-the-art methods with an improvement of up to 3.06% in final average accuracy on ImageNet-subset. Additionally, we offer concept visualizations for model predictions, further advancing the understanding of interpretable continual learning.

</details>

### CL-LoRA: Continual Low-Rank Adaptation for Rehearsal-Free Class-Incremental Learning.
- **链接**: [arXiv:2505.24816](https://arxiv.org/abs/2505.24816) · 📚 被引 15
- **作者**: Jiangpeng He, Zhihao Duan, Fengqing Zhu
- **🏷️ 机构**: Massachusetts Institute of Technology,Cambridge,Massachusetts,U.S.A., Purdue University,West Lafayette,Indiana,U.S.A.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-Incremental Learning (CIL) aims to learn new classes sequentially while retaining the knowledge of previously learned classes. Recently, pre-trained models (PTMs) combined with parameter-efficient fine-tuning (PEFT) have shown remarkable performance in rehearsal-free CIL without requiring exemplars from previous tasks. However, existing adapter-based methods, which incorporate lightweight learnable modules into PTMs for CIL, create new adapters for each new task, leading to both parameter redundancy and failure to leverage shared knowledge across tasks. In this work, we propose ContinuaL Low-Rank Adaptation (CL-LoRA), which introduces a novel dual-adapter architecture combining \textbf{task-shared adapters} to learn cross-task knowledge and \textbf{task-specific adapters} to capture unique features of each new task. Specifically, the shared adapters utilize random orthogonal matrices and leverage knowledge distillation with gradient reassignment to preserve essential shared knowledge. In addition, we introduce learnable block-wise weights for task-specific adapters, which mitigate inter-task interference while maintaining the model's plasticity. We demonstrate CL-LoRA consistently achieves promising performance under multiple benchmarks with reduced training and inference computation, establishing a more efficient and scalable paradigm for continual learning with pre-trained models.

</details>

### KAC: Kolmogorov-Arnold Classifier for Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_KAC_Kolmogorov-Arnold_Classifier_for_Continual_Learning_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Yusong Hu, Zichen Liang, Fei Yang, Qibin Hou, Xialei Liu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University,VCIP, CS
- **会议**: CVPR 2025

### Do Your Best and Get Enough Rest for Continual Learning.
- **链接**: [arXiv:2503.18371](https://arxiv.org/abs/2503.18371) · [代码](https://github.com/hankyul2/ViewBatchModel) · 📚 被引 1
- **作者**: Hankyul Kang, Gregor Seifer, Donghyun Lee, Jongbin Ryu
- **🏷️ 机构**: Ajou University, KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> According to the forgetting curve theory, we can enhance memory retention by learning extensive data and taking adequate rest. This means that in order to effectively retain new knowledge, it is essential to learn it thoroughly and ensure sufficient rest so that our brain can memorize without forgetting. The main takeaway from this theory is that learning extensive data at once necessitates sufficient rest before learning the same data again. This aspect of human long-term memory retention can be effectively utilized to address the continual learning of neural networks. Retaining new knowledge for a long period of time without catastrophic forgetting is the critical problem of continual learning. Therefore, based on Ebbinghaus' theory, we introduce the view-batch model that adjusts the learning schedules to optimize the recall interval between retraining the same samples. The proposed view-batch model allows the network to get enough rest to learn extensive knowledge from the same samples with a recall interval of sufficient length. To this end, we specifically present two approaches: 1) a replay method that guarantees the optimal recall interval, and 2) a self-supervised learning that acquires extensive knowledge from a single training sample at a time. We empirically show that these approaches of our method are aligned with the forgetting curve theory, which can enhance long-term memory. In our experiments, we also demonstrate that our method significantly improves many state-of-the-art continual learning methods in various protocols and scenarios. We open-source this project at https://github.com/hankyul2/ViewBatchModel.

</details>

### Temporal-Difference Variational Continual Learning.
- **链接**: [arXiv:2410.07812](https://arxiv.org/abs/2410.07812) · 📚 被引 0
- **作者**: Luckeciano Carvalho Melo, Alessandro Abate, Yarin Gal
- **🏷️ 机构**: University of Oxford
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In continual learning (CL), catastrophic forgetting often arises due to feature drift. This challenge is particularly prominent in the exemplar-free continual learning (EFCL) setting, where samples from previous tasks cannot be retained, making it difficult to preserve prior knowledge. To address this issue, some EFCL methods aim to identify feature spaces that minimize the impact on previous tasks while accommodating new ones. However, they rely on static features or outdated statistics stored from old tasks, which prevents them from capturing the dynamic evolution of the feature space in CL, leading to performance degradation over time. In this paper, we introduce the Drift-Resistant Space (DRS), which effectively handles feature drifts without requiring explicit feature modeling or the storage of previous tasks. A novel parameter-efficient fine-tuning approach called Low-Rank Adaptation Subtraction (LoRA-) is proposed to develop the DRS. This method subtracts the LoRA weights of old tasks from the initial pre-trained weight before processing new task data to establish the DRS for model training. Therefore, LoRA- enhances stability, improves efficiency, and simplifies implementation. Furthermore, stabilizing feature drifts allows for better plasticity by learning with a triplet loss. Our method consistently achieves state-of-the-art results, especially for long task sequences, across multiple datasets.

</details>

### Dual-Space Semantic Synergy Distillation for Continual Learning of Unlabeled Streams.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1eaa5146756be028ad6fff1efcc8e6bd-Abstract-Conference.html) · 📚 被引 0
- **作者**: Donghao Sun, Xi Wang, Xu Yang, Kun Wei, Cheng Deng
- **🏷️ 机构**: Xidian University, ETHZ - ETH Zurich, Microsoft
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (OCL) seeks to learn new tasks from data streams that appear only once, while retaining knowledge of previously learned tasks. Most existing methods rely on replay, focusing on enhancing memory retention through regularization or distillation. However, they often overlook the adaptability of the model, limiting the ability to learn generalizable and discriminative features incrementally from online training data. To address this, we introduce a plug-and-play module, S6MOD, which can be integrated into most existing methods and directly improve adaptability. Specifically, S6MOD introduces an extra branch after the backbone, where a mixture of discretization selectively adjusts parameters in a selective state space model, enriching selective scan patterns such that the model can adaptively select the most sensitive discretization method for current dynamics. We further design a class-conditional routing algorithm for dynamic, uncertainty-based adjustment and implement a contrastive discretization loss to optimize it. Extensive experiments combining our module with various models demonstrate that S6MOD significantly enhances model adaptability, leading to substantial performance gains and achieving the state-of-the-art results.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of high-frequency data streams, achieving real-time learning within varying memory constraints is paramount. This paper presents Ferret, a comprehensive framework designed to enhance online accuracy of Online Continual Learning (OCL) algorithms while dynamically adapting to varying memory budgets. Ferret employs a fine-grained pipeline parallelism strategy combined with an iterative gradient compensation algorithm, ensuring seamless handling of high-frequency data with minimal latency, and effectively counteracting the challenge of stale gradients in parallel training. To adapt to varying memory budgets, its automated model partitioning and pipeline planning optimizes performance regardless of memory limitations. Extensive experiments across 20 benchmarks and 5 integrated OCL algorithms show Ferret's remarkable efficiency, achieving up to 3.7$\times$ lower memory overhead to reach the same online accuracy compared to competing methods. Furthermore, Ferret consistently outperforms these methods across diverse memory budgets, underscoring its superior adaptability. These findings position Ferret as a premier solution for efficient and adaptive OCL framework in real-time environments.

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

### Knowledge Graph Enhanced Generative Multi-modal Models for Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7b6d77bf723ab4fed4f88baf544683fb-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xusheng Cao, Haori Lu, Linlan Huang, Fei Yang, Xialei Liu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University, Adobe Systems
- **会议**: NeurIPS 2025

### Adapter Merging with Centroid Prototype Mapping for Scalable Class-Incremental Learning.
- **链接**: [arXiv:2412.18219](https://arxiv.org/abs/2412.18219) · [代码](https://github.com/tf63/ACMap) · 📚 被引 4
- **作者**: Takuma Fukuda, Hiroshi Kera, Kazuhiko Kawamoto
- **🏷️ 机构**: Chiba University, Chiba University Zuse Institute Berlin
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Adapter Merging with Centroid Prototype Mapping (ACMap), an exemplar-free framework for class-incremental learning (CIL) that addresses both catastrophic forgetting and scalability. While existing methods involve a trade-off between inference time and accuracy, ACMap consolidates task-specific adapters into a single adapter, thus achieving constant inference time across tasks without sacrificing accuracy. The framework employs adapter merging to build a shared subspace that aligns task representations and mitigates forgetting, while centroid prototype mapping maintains high accuracy by consistently adapting representations within the shared subspace. To further improve scalability, an early stopping strategy limits adapter merging as tasks increase. Extensive experiments on five benchmark datasets demonstrate that ACMap matches state-of-the-art accuracy while maintaining inference time comparable to the fastest existing methods. The code is available at https://github.com/tf63/ACMap.

</details>

### Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning.
- **链接**: [arXiv:2509.16738](https://arxiv.org/abs/2509.16738) · 📚 被引 1
- **作者**: Kai Jiang, Zhengyan Shi, Dell Zhang, Hongyuan Zhang, Xuelong Li
- **🏷️ 机构**: Tsinghua University, Microsoft Research, Institute of Artificial Intelligence (TeleAI), China Telecom
- **会议**: NeurIPS 2025

### Class-wise Balancing Data Replay for Federated Class-Incremental Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d611d06e3207330555fbc10810e70163-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhuang Qi, Ying-Peng Tang, Lei Meng, Han Yu, Xiaoxiao Li, Xiangxu Meng
- **🏷️ 机构**: Shandong University, Nanyang Technological University, Nanyang Technological University (NTU)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study model confidence calibration in class-incremental learning, where models learn from sequential tasks with different class sets. While existing works primarily focus on accuracy, maintaining calibrated confidence has been largely overlooked. Unfortunately, most post-hoc calibration techniques are not designed to work with the limited memories of old-task data typical in class-incremental learning, as retaining a sufficient validation set would be impractical. Thus, we propose T-CIL, a novel temperature scaling approach for class-incremental learning without a validation set for old tasks, that leverages adversarially perturbed exemplars from memory. Directly using exemplars is inadequate for temperature optimization, since they are already used for training. The key idea of T-CIL is to perturb exemplars more strongly for old tasks than for the new task by adjusting the perturbation direction based on feature distance, with the single magnitude determined using the new-task validation set. This strategy makes the perturbation magnitude computed from the new task also applicable to old tasks, leveraging the tendency that the accuracy of old tasks is lower than that of the new task. We empirically show that T-CIL significantly outperforms various baselines in terms of calibration on real datasets and can be integrated with existing class-incremental learning techniques with minimal impact on accuracy.

</details>

### Order-Robust Class Incremental Learning: Graph-Driven Dynamic Similarity Grouping.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lai_Order-Robust_Class_Incremental_Learning_Graph-Driven_Dynamic_Similarity_Grouping_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Guannan Lai, Yujie Li, Xiangkun Wang, Junbo Zhang, Tianrui Li, Xin Yang
- **🏷️ 机构**: Southwestern University of Finance and Economics,School of Computing and Artificial Intelligence, JD Intelligent Cities Research, Southwest Jiaotong University
- **会议**: CVPR 2025

### Tripartite Weight-Space Ensemble for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Tripartite_Weight-Space_Ensemble_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Juntae Lee, Munawar Hayat, Sungrack Yun
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: CVPR 2025

### Dynamic Integration of Task-Specific Adapters for Class Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Dynamic_Integration_of_Task-Specific_Adapters_for_Class_Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Jiashuo Li, Shaokun Wang, Bo Qian, Yuhang He, Xing Wei, Qiang Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence
- **会议**: CVPR 2025

### SEC-Prompt: SEmantic Complementary Prompting for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_SEC-PromptSEmantic_Complementary_Prompting_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Ye Liu, Meng Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Low-Rank Adaptation in Multilinear Operator Networks for Security-Preserving Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ta_Low-Rank_Adaptation_in_Multilinear_Operator_Networks_for_Security-Preserving_Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Huu Binh Ta, Duc Nguyen, Quyen Tran, Toan Tran, Tung Pham
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: CVPR 2025

### Activating Sparse Part Concepts for 3D Class Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tian_Activating_Sparse_Part_Concepts_for_3D_Class_Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Zhenya Tian, Jun Xiao, Lupeng Liu, Haiyong Jiang
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Artificial Intelligence
- **会议**: CVPR 2025

### Boosting Domain Incremental Learning: Selecting the Optimal Parameters is All You Need.
- **链接**: [arXiv:2505.23744](https://arxiv.org/abs/2505.23744) · 📚 被引 10
- **作者**: Qiang Wang, Xiang Song, Yuhang He, Jizhou Han, Chenhao Ding, Xinyuan Gao et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNNs) often underperform in real-world, dynamic settings where data distributions change over time. Domain Incremental Learning (DIL) offers a solution by enabling continual model adaptation, with Parameter-Isolation DIL (PIDIL) emerging as a promising paradigm to reduce knowledge conflicts. However, existing PIDIL methods struggle with parameter selection accuracy, especially as the number of domains and corresponding classes grows. To address this, we propose SOYO, a lightweight framework that improves domain selection in PIDIL. SOYO introduces a Gaussian Mixture Compressor (GMC) and Domain Feature Resampler (DFR) to store and balance prior domain data efficiently, while a Multi-level Domain Feature Fusion Network (MDFN) enhances domain feature extraction. Our framework supports multiple Parameter-Efficient Fine-Tuning (PEFT) methods and is validated across tasks such as image classification, object detection, and speech enhancement. Experimental results on six benchmarks demonstrate SOYO's consistent superiority over existing baselines, showcasing its robustness and adaptability in complex, evolving environments. The codes will be released in https://github.com/qwangcv/SOYO.

</details>

### pFedMxF: Personalized Federated Class-Incremental Learning with Mixture of Frequency Aggregation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_pFedMxF_Personalized_Federated_Class-Incremental_Learning_with_Mixture_of_Frequency_Aggregation_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Yifei Zhang, Hao Zhu, Alysa Ziying Tan, Dianzhi Yu, Longtao Huang, Han Yu
- **🏷️ 机构**: Nanyang Technological University,College of Computing and Data Science, Data61 &#x2665; CSRIO, The Chinese University of Hong Kong
- **会议**: CVPR 2025

### Attraction Diminishing and Distributing for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Attraction_Diminishing_and_Distributing_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Li-Jun Zhao, Zhen-Duo Chen, Yongxin Wang, Xin Luo, Xin-Shun Xu
- **🏷️ 机构**: Shandong University, MBZUAI
- **会议**: NeurIPS 2025
