# Continual Learning — 2025 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 31 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### AVQACL: A Novel Benchmark for Audio-Visual Question Answering Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_AVQACL_A_Novel_Benchmark_for_Audio-Visual_Question_Answering_Continual_Learning_CVPR_2025_paper.html)
- **作者**: Kaixuan Wu, Xinde Li, Xinling Li, Chuanfei Hu, Guoliang Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Advancing Multiple Instance Learning with Continual Learning for Whole Slide Imaging.
- **链接**: [arXiv:2505.10649](https://arxiv.org/abs/2505.10649) · 📚 被引 1
- **作者**: Xianrui Li, Yufei Cui, Jun Li, Antoni B. Chan
- **🏷️ 机构**: City University of Hong Kong,Dept. of Computer Science, Noah&#x2019;s Ark Lab, Huawei Canada,Montreal,Canada, Guangzhou Bingli Technology Co., Ltd.,Guangzhou
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Advances in medical imaging and deep learning have propelled progress in whole slide image (WSI) analysis, with multiple instance learning (MIL) showing promise for efficient and accurate diagnostics. However, conventional MIL models often lack adaptability to evolving datasets, as they rely on static training that cannot incorporate new information without extensive retraining. Applying continual learning (CL) to MIL models is a possible solution, but often sees limited improvements. In this paper, we analyze CL in the context of attention MIL models and find that the model forgetting is mainly concentrated in the attention layers of the MIL model. Using the results of this analysis we propose two components for improving CL on MIL: Attention Knowledge Distillation (AKD) and the Pseudo-Bag Memory Pool (PMP). AKD mitigates catastrophic forgetting by focusing on retaining attention layer knowledge between learning sessions, while PMP reduces the memory footprint by selectively storing only the most informative patches, or ``pseudo-bags'' from WSIs. Experimental evaluations demonstrate that our method significantly improves both accuracy and memory efficiency on diverse WSI datasets, outperforming current state-of-the-art CL methods. This work provides a foundation for CL in large-scale, weakly annotated clinical datasets, paving the way for more adaptable and resilient diagnostic models.

</details>

### Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning.
- **链接**: [arXiv:2403.18886](https://arxiv.org/abs/2403.18886) · 📚 被引 15
- **作者**: Huiyi Wang, Haodong Lu, Lina Yao, Dong Gong
- **🏷️ 机构**: University of New South Wales, CSIRO&#x2019;s Data61
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to continually accumulate knowledge from a non-stationary data stream without catastrophic forgetting of learned knowledge, requiring a balance between stability and adaptability. Relying on the generalizable representation in pre-trained models (PTMs), PTM-based CL methods perform effective continual adaptation on downstream tasks by adding learnable adapters or prompts upon the frozen PTMs. However, many existing PTM-based CL methods use restricted adaptation on a fixed set of these modules to avoid forgetting, suffering from limited CL ability. Periodically adding task-specific modules results in linear model growth rate and impaired knowledge reuse. We propose Self-Expansion of pre-trained models with Modularized Adaptation (SEMA), a novel approach to enhance the control of stability-plasticity balance in PTM-based CL. SEMA automatically decides to reuse or add adapter modules on demand in CL, depending on whether significant distribution shift that cannot be handled is detected at different representation levels. We design modular adapter consisting of a functional adapter and a representation descriptor. The representation descriptors are trained as a distribution shift indicator and used to trigger self-expansion signals. For better composing the adapters, an expandable weighting router is learned jointly for mixture of adapter outputs. SEMA enables better knowledge reuse and sub-linear expansion rate. Extensive experiments demonstrate the effectiveness of the proposed self-expansion method, achieving state-of-the-art performance compared to PTM-based CL methods without memory rehearsal. Code is available at https://github.com/huiyiwang01/SEMA-CL.

</details>

### Online Task-Free Continual Learning via Dynamic Expansionable Memory Distribution.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_Online_Task-Free_Continual_Learning_via_Dynamic_Expansionable_Memory_Distribution_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: University of Electronic Science and Technology of China,School of Information and Software Engineering,Chengdu, University of York,Department of Computer Science,York,UK,YO10 5GH
- **会议**: CVPR 2025

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
- **链接**: [arXiv:2503.21076](https://arxiv.org/abs/2503.21076) · 📚 被引 5
- **作者**: Yusong Hu, Zichen Liang, Fei Yang, Qibin Hou, Xialei Liu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University,VCIP, CS
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning requires models to train continuously across consecutive tasks without forgetting. Most existing methods utilize linear classifiers, which struggle to maintain a stable classification space while learning new tasks. Inspired by the success of Kolmogorov-Arnold Networks (KAN) in preserving learning stability during simple continual regression tasks, we set out to explore their potential in more complex continual learning scenarios. In this paper, we introduce the Kolmogorov-Arnold Classifier (KAC), a novel classifier developed for continual learning based on the KAN structure. We delve into the impact of KAN's spline functions and introduce Radial Basis Functions (RBF) for improved compatibility with continual learning. We replace linear classifiers with KAC in several recent approaches and conduct experiments across various continual learning benchmarks, all of which demonstrate performance improvements, highlighting the effectiveness and robustness of KAC in continual learning. The code is available at https://github.com/Ethanhuhuhu/KAC.

</details>

### Do Your Best and Get Enough Rest for Continual Learning.
- **链接**: [arXiv:2503.18371](https://arxiv.org/abs/2503.18371) · 📚 被引 1
- **作者**: Hankyul Kang, Gregor Seifer, Donghyun Lee, Jongbin Ryu
- **🏷️ 机构**: Ajou University, KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> According to the forgetting curve theory, we can enhance memory retention by learning extensive data and taking adequate rest. This means that in order to effectively retain new knowledge, it is essential to learn it thoroughly and ensure sufficient rest so that our brain can memorize without forgetting. The main takeaway from this theory is that learning extensive data at once necessitates sufficient rest before learning the same data again. This aspect of human long-term memory retention can be effectively utilized to address the continual learning of neural networks. Retaining new knowledge for a long period of time without catastrophic forgetting is the critical problem of continual learning. Therefore, based on Ebbinghaus' theory, we introduce the view-batch model that adjusts the learning schedules to optimize the recall interval between retraining the same samples. The proposed view-batch model allows the network to get enough rest to learn extensive knowledge from the same samples with a recall interval of sufficient length. To this end, we specifically present two approaches: 1) a replay method that guarantees the optimal recall interval, and 2) a self-supervised learning that acquires extensive knowledge from a single training sample at a time. We empirically show that these approaches of our method are aligned with the forgetting curve theory, which can enhance long-term memory. In our experiments, we also demonstrate that our method significantly improves many state-of-the-art continual learning methods in various protocols and scenarios. We open-source this project at https://github.com/hankyul2/ViewBatchModel.

</details>

### LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning.
- **链接**: [arXiv:2503.18985](https://arxiv.org/abs/2503.18985) · 📚 被引 8
- **作者**: Xuan Liu, Xiaobin Chang
- **🏷️ 机构**: School of Artificial Intelligence, Sun Yat-sen University,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In continual learning (CL), catastrophic forgetting often arises due to feature drift. This challenge is particularly prominent in the exemplar-free continual learning (EFCL) setting, where samples from previous tasks cannot be retained, making it difficult to preserve prior knowledge. To address this issue, some EFCL methods aim to identify feature spaces that minimize the impact on previous tasks while accommodating new ones. However, they rely on static features or outdated statistics stored from old tasks, which prevents them from capturing the dynamic evolution of the feature space in CL, leading to performance degradation over time. In this paper, we introduce the Drift-Resistant Space (DRS), which effectively handles feature drifts without requiring explicit feature modeling or the storage of previous tasks. A novel parameter-efficient fine-tuning approach called Low-Rank Adaptation Subtraction (LoRA-) is proposed to develop the DRS. This method subtracts the LoRA weights of old tasks from the initial pre-trained weight before processing new task data to establish the DRS for model training. Therefore, LoRA- enhances stability, improves efficiency, and simplifies implementation. Furthermore, stabilizing feature drifts allows for better plasticity by learning with a triplet loss. Our method consistently achieves state-of-the-art results, especially for long task sequences, across multiple datasets.

</details>

### Enhancing Online Continual Learning with Plug-and-Play State Space Model and Class-Conditional Mixture of Discretization.
- **链接**: [arXiv:2412.18177](https://arxiv.org/abs/2412.18177) · 📚 被引 1
- **作者**: Sihao Liu, Yibo Yang, Xiaojie Li, David A. Clifton, Bernard Ghanem
- **🏷️ 机构**: Harbin Institute of Technology, King Abdullah University of Science and Technology, Harbin Institute of Technology (Shenzhen)
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (OCL) seeks to learn new tasks from data streams that appear only once, while retaining knowledge of previously learned tasks. Most existing methods rely on replay, focusing on enhancing memory retention through regularization or distillation. However, they often overlook the adaptability of the model, limiting the ability to learn generalizable and discriminative features incrementally from online training data. To address this, we introduce a plug-and-play module, S6MOD, which can be integrated into most existing methods and directly improve adaptability. Specifically, S6MOD introduces an extra branch after the backbone, where a mixture of discretization selectively adjusts parameters in a selective state space model, enriching selective scan patterns such that the model can adaptively select the most sensitive discretization method for current dynamics. We further design a class-conditional routing algorithm for dynamic, uncertainty-based adjustment and implement a contrastive discretization loss to optimize it. Extensive experiments combining our module with various models demonstrate that S6MOD significantly enhances model adaptability, leading to substantial performance gains and achieving the state-of-the-art results.

</details>

### Handling Spatial-Temporal Data Heterogeneity for Federated Continual Learning via Tail Anchor.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Handling_Spatial-Temporal_Data_Heterogeneity_for_Federated_Continual_Learning_via_Tail_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Hao Yu, Xin Yang, Le Zhang, Hanlin Gu, Tianrui Li, Lixin Fan et al.
- **🏷️ 机构**: Southwestern University of Finance and Economics, University of Electronic Science and Technology of China, WeBank
- **会议**: CVPR 2025

### Ferret: An Efficient Online Continual Learning Framework under Varying Memory Constraints.
- **链接**: [arXiv:2503.12053](https://arxiv.org/abs/2503.12053) · 📚 被引 0
- **作者**: Yuhao Zhou, Yuxin Tian, Jindi Lv, Mingjia Shi, Yuanxi Li, Qing Ye et al.
- **🏷️ 机构**: Sichuan University, National University of Singapore, University of Illinois Urbana-Champaign
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of high-frequency data streams, achieving real-time learning within varying memory constraints is paramount. This paper presents Ferret, a comprehensive framework designed to enhance online accuracy of Online Continual Learning (OCL) algorithms while dynamically adapting to varying memory budgets. Ferret employs a fine-grained pipeline parallelism strategy combined with an iterative gradient compensation algorithm, ensuring seamless handling of high-frequency data with minimal latency, and effectively counteracting the challenge of stale gradients in parallel training. To adapt to varying memory budgets, its automated model partitioning and pipeline planning optimizes performance regardless of memory limitations. Extensive experiments across 20 benchmarks and 5 integrated OCL algorithms show Ferret's remarkable efficiency, achieving up to 3.7$\times$ lower memory overhead to reach the same online accuracy compared to competing methods. Furthermore, Ferret consistently outperforms these methods across diverse memory budgets, underscoring its superior adaptability. These findings position Ferret as a premier solution for efficient and adaptive OCL framework in real-time environments.

</details>

### BiLoRA: Almost-Orthogonal Parameter Spaces for Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_BiLoRA_Almost-Orthogonal_Parameter_Spaces_for_Continual_Learning_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Hao Zhu, Yifei Zhang, Junhao Dong, Piotr Koniusz
- **🏷️ 机构**: Data61&#x2665;CSIRO, Nanyang Technological University
- **会议**: CVPR 2025

### Learning Conditional Space-Time Prompt Distributions for Video Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zou_Learning_Conditional_Space-Time_Prompt_Distributions_for_Video_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Xiaohan Zou, Wenchao Ma, Shu Zhao
- **🏷️ 机构**: The Pennsylvania State University
- **会议**: CVPR 2025

### Dual Consolidation for Pre-Trained Model-Based Domain-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Dual_Consolidation_for_Pre-Trained_Model-Based_Domain-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 14
- **作者**: Da-Wei Zhou, Zi-Wen Cai, Han-Jia Ye, Lijun Zhang, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University,School of Artificial Intelligence
- **会议**: CVPR 2025

### Reducing Class-wise Confusion for Incremental Learning with Disentangled Manifolds.
- **链接**: [arXiv:2503.17677](https://arxiv.org/abs/2503.17677) · 📚 被引 5
- **作者**: Huitong Chen, Yu Wang, Yan Fan, Guosong Jiang, Qinghua Hu
- **🏷️ 机构**: Tianjin University,Tianjin Key Lab of Machine Learning, College of Intelligence and Computing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class incremental learning (CIL) aims to enable models to continuously learn new classes without catastrophically forgetting old ones. A promising direction is to learn and use prototypes of classes during incremental updates. Despite simplicity and intuition, we find that such methods suffer from inadequate representation capability and unsatisfied feature overlap. These two factors cause class-wise confusion and limited performance. In this paper, we develop a Confusion-REduced AuTo-Encoder classifier (CREATE) for CIL. Specifically, our method employs a lightweight auto-encoder module to learn compact manifold for each class in the latent subspace, constraining samples to be well reconstructed only on the semantically correct auto-encoder. Thus, the representation stability and capability of class distributions are enhanced, alleviating the potential class-wise confusion problem. To further distinguish the overlapped features, we propose a confusion-aware latent space separation loss that ensures samples are closely distributed in their corresponding low-dimensional manifold while keeping away from the distributions of features from other classes. Our method demonstrates stronger representational capacity and discrimination ability by learning disentangled manifolds and reduces class confusion. Extensive experiments on multiple datasets and settings show that CREATE outperforms other state-of-the-art methods up to 5.41%.

</details>

### Enhancing Few-Shot Class-Incremental Learning via Training-Free Bi-Level Modality Calibration.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Enhancing_Few-Shot_Class-Incremental_Learning_via_Training-Free_Bi-Level_Modality_Calibration_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Yiyang Chen, Tianyu Ding, Lei Wang, Jing Huo, Yang Gao, Wenbin Li
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China, Microsoft,Applied Sciences Group,USA, University of Wollongong,Australia
- **会议**: CVPR 2025

### Adapter Merging with Centroid Prototype Mapping for Scalable Class-Incremental Learning.
- **链接**: [arXiv:2412.18219](https://arxiv.org/abs/2412.18219) · 📚 被引 4
- **作者**: Takuma Fukuda, Hiroshi Kera, Kazuhiko Kawamoto
- **🏷️ 机构**: Chiba University, Chiba University Zuse Institute Berlin
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Adapter Merging with Centroid Prototype Mapping (ACMap), an exemplar-free framework for class-incremental learning (CIL) that addresses both catastrophic forgetting and scalability. While existing methods involve a trade-off between inference time and accuracy, ACMap consolidates task-specific adapters into a single adapter, thus achieving constant inference time across tasks without sacrificing accuracy. The framework employs adapter merging to build a shared subspace that aligns task representations and mitigates forgetting, while centroid prototype mapping maintains high accuracy by consistently adapting representations within the shared subspace. To further improve scalability, an early stopping strategy limits adapter merging as tasks increase. Extensive experiments on five benchmark datasets demonstrate that ACMap matches state-of-the-art accuracy while maintaining inference time comparable to the fastest existing methods. The code is available at https://github.com/tf63/ACMap.

</details>

### Knowledge Memorization and Rumination for Pre-trained Model-based Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_Knowledge_Memorization_and_Rumination_for_Pre-trained_Model-based_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Zijian Gao, Wangwang Jia, Xingxing Zhang, Dulan Zhou, Kele Xu, Dawei Feng et al.
- **🏷️ 机构**: National University of Defense Technology,College of Computer Science and Technology, Tsinghua University,School of Computer Science
- **会议**: CVPR 2025

### T-CIL: Temperature Scaling using Adversarial Perturbation for Calibration in Class-Incremental Learning.
- **链接**: [arXiv:2503.22163](https://arxiv.org/abs/2503.22163) · 📚 被引 1
- **作者**: Seonghyeon Hwang, Minsu Kim, Steven Euijong Whang
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study model confidence calibration in class-incremental learning, where models learn from sequential tasks with different class sets. While existing works primarily focus on accuracy, maintaining calibrated confidence has been largely overlooked. Unfortunately, most post-hoc calibration techniques are not designed to work with the limited memories of old-task data typical in class-incremental learning, as retaining a sufficient validation set would be impractical. Thus, we propose T-CIL, a novel temperature scaling approach for class-incremental learning without a validation set for old tasks, that leverages adversarially perturbed exemplars from memory. Directly using exemplars is inadequate for temperature optimization, since they are already used for training. The key idea of T-CIL is to perturb exemplars more strongly for old tasks than for the new task by adjusting the perturbation direction based on feature distance, with the single magnitude determined using the new-task validation set. This strategy makes the perturbation magnitude computed from the new task also applicable to old tasks, leveraging the tendency that the accuracy of old tasks is lower than that of the new task. We empirically show that T-CIL significantly outperforms various baselines in terms of calibration on real datasets and can be integrated with existing class-incremental learning techniques with minimal impact on accuracy.

</details>

### Order-Robust Class Incremental Learning: Graph-Driven Dynamic Similarity Grouping.
- **链接**: [arXiv:2502.20032](https://arxiv.org/abs/2502.20032) · 📚 被引 4
- **作者**: Guannan Lai, Yujie Li, Xiangkun Wang, Junbo Zhang, Tianrui Li, Xin Yang
- **🏷️ 机构**: Southwestern University of Finance and Economics,School of Computing and Artificial Intelligence, JD Intelligent Cities Research, Southwest Jiaotong University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) aims to enable models to learn new classes sequentially while retaining knowledge of previous ones. Although current methods have alleviated catastrophic forgetting (CF), recent studies highlight that the performance of CIL models is highly sensitive to the order of class arrival, particularly when sequentially introduced classes exhibit high inter-class similarity. To address this critical yet understudied challenge of class order sensitivity, we first extend existing CIL frameworks through theoretical analysis, proving that grouping classes with lower pairwise similarity during incremental phases significantly improves model robustness to order variations. Building on this insight, we propose Graph-Driven Dynamic Similarity Grouping (GDDSG), a novel method that employs graph coloring algorithms to dynamically partition classes into similarity-constrained groups. Each group trains an isolated CIL sub-model and constructs meta-features for class group identification. Experimental results demonstrate that our method effectively addresses the issue of class order sensitivity while achieving optimal performance in both model accuracy and anti-forgetting capability. Our code is available at https://github.com/AIGNLAI/GDDSG.

</details>

### Tripartite Weight-Space Ensemble for Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2506.15720](https://arxiv.org/abs/2506.15720) · 📚 被引 0
- **作者**: Juntae Lee, Munawar Hayat, Sungrack Yun
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class incremental learning (FSCIL) enables the continual learning of new concepts with only a few training examples. In FSCIL, the model undergoes substantial updates, making it prone to forgetting previous concepts and overfitting to the limited new examples. Most recent trend is typically to disentangle the learning of the representation from the classification head of the model. A well-generalized feature extractor on the base classes (many examples and many classes) is learned, and then fixed during incremental learning. Arguing that the fixed feature extractor restricts the model's adaptability to new classes, we introduce a novel FSCIL method to effectively address catastrophic forgetting and overfitting issues. Our method enables to seamlessly update the entire model with a few examples. We mainly propose a tripartite weight-space ensemble (Tri-WE). Tri-WE interpolates the base, immediately previous, and current models in weight-space, especially for the classification heads of the models. Then, it collaboratively maintains knowledge from the base and previous models. In addition, we recognize the challenges of distilling generalized representations from the previous model from scarce data. Hence, we suggest a regularization loss term using amplified data knowledge distillation. Simply intermixing the few-shot data, we can produce richer data enabling the distillation of critical knowledge from the previous model. Consequently, we attain state-of-the-art results on the miniImageNet, CUB200, and CIFAR100 datasets.

</details>

### Dynamic Integration of Task-Specific Adapters for Class Incremental Learning.
- **链接**: [arXiv:2409.14983](https://arxiv.org/abs/2409.14983) · 📚 被引 4
- **作者**: Jiashuo Li, Shaokun Wang, Bo Qian, Yuhang He, Xing Wei, Qiang Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-exemplar class Incremental Learning (NECIL) enables models to continuously acquire new classes without retraining from scratch and storing old task exemplars, addressing privacy and storage issues. However, the absence of data from earlier tasks exacerbates the challenge of catastrophic forgetting in NECIL. In this paper, we propose a novel framework called Dynamic Integration of task-specific Adapters (DIA), which comprises two key components: Task-Specific Adapter Integration (TSAI) and Patch-Level Model Alignment. TSAI boosts compositionality through a patch-level adapter integration strategy, which provides a more flexible compositional solution while maintaining low computation costs. Patch-Level Model Alignment maintains feature consistency and accurate decision boundaries via two specialized mechanisms: Patch-Level Distillation Loss (PDL) and Patch-Level Feature Reconstruction method (PFR). Specifically, the PDL preserves feature-level consistency between successive models by implementing a distillation loss based on the contributions of patch tokens to new class learning. The PFR facilitates accurate classifier alignment by reconstructing old class features from previous tasks that adapt to new task knowledge. Extensive experiments validate the effectiveness of our DIA, revealing significant improvements on benchmark datasets in the NECIL setting, maintaining an optimal balance between computational complexity and accuracy.

</details>

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
- **🏷️ 机构**: Shandong University,School of Software,China, Shandong Jianzhu University,School of Computer Science and Technology,China
- **会议**: CVPR 2025

### Task-Agnostic Guided Feature Expansion for Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_Task-Agnostic_Guided_Feature_Expansion_for_Class-Incremental_Learning_CVPR_2025_paper.html) · 📚 被引 16
- **作者**: Bowen Zheng, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2025

### Multi-Granularity Class Prototype Topology Distillation for Class-Incremental Source-Free Unsupervised Domain Adaptation.
- **链接**: [arXiv:2411.16064](https://arxiv.org/abs/2411.16064) · 📚 被引 7
- **作者**: Peihua Deng, Jiehua Zhang, Xichun Sheng, Chenggang Yan, Yaoqi Sun, Ying Fu et al.
- **🏷️ 机构**: Hangzhou Dianzi University, Xi&#x2019;an Jiaotong University, Macao Polytechnic University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper explores the Class-Incremental Source-Free Unsupervised Domain Adaptation (CI-SFUDA) problem, where the unlabeled target data come incrementally without access to labeled source instances. This problem poses two challenges, the interference of similar source-class knowledge in target-class representation learning and the shocks of new target knowledge to old ones. To address them, we propose the Multi-Granularity Class Prototype Topology Distillation (GROTO) algorithm, which effectively transfers the source knowledge to the class-incremental target domain. Concretely, we design the multi-granularity class prototype self-organization module and the prototype topology distillation module. First, we mine the positive classes by modeling accumulation distributions. Next, we introduce multi-granularity class prototypes to generate reliable pseudo-labels, and exploit them to promote the positive-class target feature self-organization. Second, the positive-class prototypes are leveraged to construct the topological structures of source and target feature spaces. Then, we perform the topology distillation to continually mitigate the shocks of new target knowledge to old ones. Extensive experiments demonstrate that our proposed method achieves state-of-the-art performance on three public datasets. Code is available at https://github.com/dengpeihua/GROTO.

</details>
