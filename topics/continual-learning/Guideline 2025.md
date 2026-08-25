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
- **链接**: [arXiv:2505.10649](https://arxiv.org/abs/2505.10649)
- **作者**: Xianrui Li, Yufei Cui, Jun Li, Antoni B. Chan
- **🏷️ 机构**: City University of Hong Kong,Dept. of Computer Science, Noah&#x2019;s Ark Lab, Huawei Canada,Montreal,Canada, Guangzhou Bingli Technology Co., Ltd.,Guangzhou
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Advances in medical imaging and deep learning have propelled progress in whole slide image (WSI) analysis, with multiple instance learning (MIL) showing promise for efficient and accurate diagnostics. However, conventional MIL models often lack adaptability to evolving datasets, as they rely on static training that cannot incorporate new information without extensive retraining. Applying continual learning (CL) to MIL models is a possible solution, but often sees limited improvements. In this paper, we analyze CL in the context of attention MIL models and find that the model forgetting is mainly concentrated in the attention layers of the MIL model. Using the results of this analysis we propose two components for improving CL on MIL: Attention Knowledge Distillation (AKD) and the Pseudo-Bag Memory Pool (PMP). AKD mitigates catastrophic forgetting by focusing on retaining attention layer knowledge between learning sessions, while PMP reduces the memory footprint by selectively storing only the most informative patches, or ``pseudo-bags'' from WSIs. Experimental evaluations demonstrate that our method significantly improves both accuracy and memory efficiency on diverse WSI datasets, outperforming current state-of-the-art CL methods. This work provides a foundation for CL in large-scale, weakly annotated clinical datasets, paving the way for more adaptable and resilient diagnostic models.

### Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning.
- **链接**: [arXiv:2403.18886](https://arxiv.org/abs/2403.18886) · [代码](https://github.com/huiyiwang01/SEMA-CL)
- **作者**: Huiyi Wang, Haodong Lu, Lina Yao, Dong Gong
- **🏷️ 机构**: University of New South Wales, CSIRO&#x2019;s Data61
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Continual learning (CL) aims to continually accumulate knowledge from a non-stationary data stream without catastrophic forgetting of learned knowledge, requiring a balance between stability and adaptability. Relying on the generalizable representation in pre-trained models (PTMs), PTM-based CL methods perform effective continual adaptation on downstream tasks by adding learnable adapters or prompts upon the frozen PTMs. However, many existing PTM-based CL methods use restricted adaptation on a fixed set of these modules to avoid forgetting, suffering from limited CL ability. Periodically adding task-specific modules results in linear model growth rate and impaired knowledge reuse. We propose Self-Expansion of pre-trained models with Modularized Adaptation (SEMA), a novel approach to enhance the control of stability-plasticity balance in PTM-based CL. SEMA automatically decides to reuse or add adapter modules on demand in CL, depending on whether significant distribution shift that cannot be handled is detected at different representation levels. We design modular adapter consisting of a functional adapter and a representation descriptor. The representation descriptors are trained as a distribution shift indicator and used to trigger self-expansion signals. For better composing the adapters, an expandable weighting router is learned jointly for mixture of adapter outputs. SEMA enables better knowledge reuse and sub-linear expansion rate. Extensive experiments demonstrate the effectiveness of the proposed self-expansion method, achieving state-of-the-art performance compared to PTM-based CL methods without memory rehearsal. Code is available at https://github.com/huiyiwang01/SEMA-CL.

### Online Task-Free Continual Learning via Dynamic Expansionable Memory Distribution.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_Online_Task-Free_Continual_Learning_via_Dynamic_Expansionable_Memory_Distribution_CVPR_2025_paper.html)
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: University of Electronic Science and Technology of China,School of Information and Software Engineering,Chengdu, University of York,Department of Computer Science,York,UK,YO10 5GH
- **会议**: CVPR 2025

### Language Guided Concept Bottleneck Models for Interpretable Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Language_Guided_Concept_Bottleneck_Models_for_Interpretable_Continual_Learning_CVPR_2025_paper.html)
- **作者**: Lu Yu, Haoyu Han, Zhe Tao, Hantao Yao, Changsheng Xu
- **🏷️ 机构**: Tianjin University of Technology,School of Computer Science and Engineering, University of Science and Technology of China,School of Information Science and Technology, Institute of Automation, University of Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2025

### CL-LoRA: Continual Low-Rank Adaptation for Rehearsal-Free Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/He_CL-LoRA_Continual_Low-Rank_Adaptation_for_Rehearsal-Free_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Jiangpeng He, Zhihao Duan, Fengqing Zhu
- **🏷️ 机构**: Massachusetts Institute of Technology,Cambridge,Massachusetts,U.S.A., Purdue University,West Lafayette,Indiana,U.S.A.
- **会议**: CVPR 2025

### KAC: Kolmogorov-Arnold Classifier for Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_KAC_Kolmogorov-Arnold_Classifier_for_Continual_Learning_CVPR_2025_paper.html)
- **作者**: Yusong Hu, Zichen Liang, Fei Yang, Qibin Hou, Xialei Liu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University,VCIP, CS
- **会议**: CVPR 2025

### Do Your Best and Get Enough Rest for Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kang_Do_Your_Best_and_Get_Enough_Rest_for_Continual_Learning_CVPR_2025_paper.html)
- **作者**: Hankyul Kang, Gregor Seifer, Donghyun Lee, Jongbin Ryu
- **🏷️ 机构**: Ajou University, KAIST
- **会议**: CVPR 2025

### LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_LoRA_Subtraction_for_Drift-Resistant_Space_in_Exemplar-Free_Continual_Learning_CVPR_2025_paper.html)
- **作者**: Xuan Liu, Xiaobin Chang
- **🏷️ 机构**: School of Artificial Intelligence, Sun Yat-sen University,China
- **会议**: CVPR 2025

### Enhancing Online Continual Learning with Plug-and-Play State Space Model and Class-Conditional Mixture of Discretization.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Enhancing_Online_Continual_Learning_with_Plug-and-Play_State_Space_Model_and_CVPR_2025_paper.html)
- **作者**: Sihao Liu, Yibo Yang, Xiaojie Li, David A. Clifton, Bernard Ghanem
- **🏷️ 机构**: Harbin Institute of Technology, King Abdullah University of Science and Technology, Harbin Institute of Technology (Shenzhen)
- **会议**: CVPR 2025

### Handling Spatial-Temporal Data Heterogeneity for Federated Continual Learning via Tail Anchor.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Handling_Spatial-Temporal_Data_Heterogeneity_for_Federated_Continual_Learning_via_Tail_CVPR_2025_paper.html)
- **作者**: Hao Yu, Xin Yang, Le Zhang, Hanlin Gu, Tianrui Li, Lixin Fan et al.
- **🏷️ 机构**: Southwestern University of Finance and Economics, University of Electronic Science and Technology of China, WeBank
- **会议**: CVPR 2025

### Ferret: An Efficient Online Continual Learning Framework under Varying Memory Constraints.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Ferret_An_Efficient_Online_Continual_Learning_Framework_under_Varying_Memory_CVPR_2025_paper.html)
- **作者**: Yuhao Zhou, Yuxin Tian, Jindi Lv, Mingjia Shi, Yuanxi Li, Qing Ye et al.
- **🏷️ 机构**: Sichuan University, National University of Singapore, University of Illinois Urbana-Champaign
- **会议**: CVPR 2025

### BiLoRA: Almost-Orthogonal Parameter Spaces for Continual Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_BiLoRA_Almost-Orthogonal_Parameter_Spaces_for_Continual_Learning_CVPR_2025_paper.html)
- **作者**: Hao Zhu, Yifei Zhang, Junhao Dong, Piotr Koniusz
- **🏷️ 机构**: Data61&#x2665;CSIRO, Nanyang Technological University
- **会议**: CVPR 2025

### Learning Conditional Space-Time Prompt Distributions for Video Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zou_Learning_Conditional_Space-Time_Prompt_Distributions_for_Video_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Xiaohan Zou, Wenchao Ma, Shu Zhao
- **🏷️ 机构**: The Pennsylvania State University
- **会议**: CVPR 2025

### Dual Consolidation for Pre-Trained Model-Based Domain-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Dual_Consolidation_for_Pre-Trained_Model-Based_Domain-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Da-Wei Zhou, Zi-Wen Cai, Han-Jia Ye, Lijun Zhang, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University,School of Artificial Intelligence
- **会议**: CVPR 2025

### Reducing Class-wise Confusion for Incremental Learning with Disentangled Manifolds.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Reducing_Class-wise_Confusion_for_Incremental_Learning_with_Disentangled_Manifolds_CVPR_2025_paper.html)
- **作者**: Huitong Chen, Yu Wang, Yan Fan, Guosong Jiang, Qinghua Hu
- **🏷️ 机构**: Tianjin University,Tianjin Key Lab of Machine Learning, College of Intelligence and Computing,China
- **会议**: CVPR 2025

### Enhancing Few-Shot Class-Incremental Learning via Training-Free Bi-Level Modality Calibration.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Enhancing_Few-Shot_Class-Incremental_Learning_via_Training-Free_Bi-Level_Modality_Calibration_CVPR_2025_paper.html)
- **作者**: Yiyang Chen, Tianyu Ding, Lei Wang, Jing Huo, Yang Gao, Wenbin Li
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China, Microsoft,Applied Sciences Group,USA, University of Wollongong,Australia
- **会议**: CVPR 2025

### Adapter Merging with Centroid Prototype Mapping for Scalable Class-Incremental Learning.
- **链接**: [arXiv:2412.18219](https://arxiv.org/abs/2412.18219) · [代码](https://github.com/tf63/ACMap)
- **作者**: Takuma Fukuda, Hiroshi Kera, Kazuhiko Kawamoto
- **🏷️ 机构**: Chiba University, Chiba University Zuse Institute Berlin
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > We propose Adapter Merging with Centroid Prototype Mapping (ACMap), an exemplar-free framework for class-incremental learning (CIL) that addresses both catastrophic forgetting and scalability. While existing methods involve a trade-off between inference time and accuracy, ACMap consolidates task-specific adapters into a single adapter, thus achieving constant inference time across tasks without sacrificing accuracy. The framework employs adapter merging to build a shared subspace that aligns task representations and mitigates forgetting, while centroid prototype mapping maintains high accuracy by consistently adapting representations within the shared subspace. To further improve scalability, an early stopping strategy limits adapter merging as tasks increase. Extensive experiments on five benchmark datasets demonstrate that ACMap matches state-of-the-art accuracy while maintaining inference time comparable to the fastest existing methods. The code is available at https://github.com/tf63/ACMap.

### Knowledge Memorization and Rumination for Pre-trained Model-based Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_Knowledge_Memorization_and_Rumination_for_Pre-trained_Model-based_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Zijian Gao, Wangwang Jia, Xingxing Zhang, Dulan Zhou, Kele Xu, Dawei Feng et al.
- **🏷️ 机构**: National University of Defense Technology,College of Computer Science and Technology, Tsinghua University,School of Computer Science
- **会议**: CVPR 2025

### T-CIL: Temperature Scaling using Adversarial Perturbation for Calibration in Class-Incremental Learning.
- **链接**: [arXiv:2503.22163](https://arxiv.org/abs/2503.22163)
- **作者**: Seonghyeon Hwang, Minsu Kim, Steven Euijong Whang
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > We study model confidence calibration in class-incremental learning, where models learn from sequential tasks with different class sets. While existing works primarily focus on accuracy, maintaining calibrated confidence has been largely overlooked. Unfortunately, most post-hoc calibration techniques are not designed to work with the limited memories of old-task data typical in class-incremental learning, as retaining a sufficient validation set would be impractical. Thus, we propose T-CIL, a novel temperature scaling approach for class-incremental learning without a validation set for old tasks, that leverages adversarially perturbed exemplars from memory. Directly using exemplars is inadequate for temperature optimization, since they are already used for training. The key idea of T-CIL is to perturb exemplars more strongly for old tasks than for the new task by adjusting the perturbation direction based on feature distance, with the single magnitude determined using the new-task validation set. This strategy makes the perturbation magnitude computed from the new task also applicable to old tasks, leveraging the tendency that the accuracy of old tasks is lower than that of the new task. We empirically show that T-CIL significantly outperforms various baselines in terms of calibration on real datasets and can be integrated with existing class-incremental learning techniques with minimal impact on accuracy.

### Order-Robust Class Incremental Learning: Graph-Driven Dynamic Similarity Grouping.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lai_Order-Robust_Class_Incremental_Learning_Graph-Driven_Dynamic_Similarity_Grouping_CVPR_2025_paper.html)
- **作者**: Guannan Lai, Yujie Li, Xiangkun Wang, Junbo Zhang, Tianrui Li, Xin Yang
- **🏷️ 机构**: Southwestern University of Finance and Economics,School of Computing and Artificial Intelligence, JD Intelligent Cities Research, Southwest Jiaotong University
- **会议**: CVPR 2025

### Tripartite Weight-Space Ensemble for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Tripartite_Weight-Space_Ensemble_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Juntae Lee, Munawar Hayat, Sungrack Yun
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: CVPR 2025

### Dynamic Integration of Task-Specific Adapters for Class Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Dynamic_Integration_of_Task-Specific_Adapters_for_Class_Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Jiashuo Li, Shaokun Wang, Bo Qian, Yuhang He, Xing Wei, Qiang Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence
- **会议**: CVPR 2025

### SEC-Prompt: SEmantic Complementary Prompting for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_SEC-PromptSEmantic_Complementary_Prompting_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Ye Liu, Meng Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Low-Rank Adaptation in Multilinear Operator Networks for Security-Preserving Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ta_Low-Rank_Adaptation_in_Multilinear_Operator_Networks_for_Security-Preserving_Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Huu Binh Ta, Duc Nguyen, Quyen Tran, Toan Tran, Tung Pham
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: CVPR 2025

### Activating Sparse Part Concepts for 3D Class Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tian_Activating_Sparse_Part_Concepts_for_3D_Class_Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Zhenya Tian, Jun Xiao, Lupeng Liu, Haiyong Jiang
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Artificial Intelligence
- **会议**: CVPR 2025

### Boosting Domain Incremental Learning: Selecting the Optimal Parameters is All You Need.
- **链接**: [arXiv:2505.23744](https://arxiv.org/abs/2505.23744) · [代码](https://github.com/qwangcv/SOYO)
- **作者**: Qiang Wang, Xiang Song, Yuhang He, Jizhou Han, Chenhao Ding, Xinyuan Gao et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Deep neural networks (DNNs) often underperform in real-world, dynamic settings where data distributions change over time. Domain Incremental Learning (DIL) offers a solution by enabling continual model adaptation, with Parameter-Isolation DIL (PIDIL) emerging as a promising paradigm to reduce knowledge conflicts. However, existing PIDIL methods struggle with parameter selection accuracy, especially as the number of domains and corresponding classes grows. To address this, we propose SOYO, a lightweight framework that improves domain selection in PIDIL. SOYO introduces a Gaussian Mixture Compressor (GMC) and Domain Feature Resampler (DFR) to store and balance prior domain data efficiently, while a Multi-level Domain Feature Fusion Network (MDFN) enhances domain feature extraction. Our framework supports multiple Parameter-Efficient Fine-Tuning (PEFT) methods and is validated across tasks such as image classification, object detection, and speech enhancement. Experimental results on six benchmarks demonstrate SOYO's consistent superiority over existing baselines, showcasing its robustness and adaptability in complex, evolving environments. The codes will be released in https://github.com/qwangcv/SOYO.

### pFedMxF: Personalized Federated Class-Incremental Learning with Mixture of Frequency Aggregation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_pFedMxF_Personalized_Federated_Class-Incremental_Learning_with_Mixture_of_Frequency_Aggregation_CVPR_2025_paper.html)
- **作者**: Yifei Zhang, Hao Zhu, Alysa Ziying Tan, Dianzhi Yu, Longtao Huang, Han Yu
- **🏷️ 机构**: Nanyang Technological University,College of Computing and Data Science, Data61 &#x2665; CSRIO, The Chinese University of Hong Kong
- **会议**: CVPR 2025

### Attraction Diminishing and Distributing for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Attraction_Diminishing_and_Distributing_for_Few-Shot_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Li-Jun Zhao, Zhen-Duo Chen, Yongxin Wang, Xin Luo, Xin-Shun Xu
- **🏷️ 机构**: Shandong University,School of Software,China, Shandong Jianzhu University,School of Computer Science and Technology,China
- **会议**: CVPR 2025

### Task-Agnostic Guided Feature Expansion for Class-Incremental Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_Task-Agnostic_Guided_Feature_Expansion_for_Class-Incremental_Learning_CVPR_2025_paper.html)
- **作者**: Bowen Zheng, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2025

### Multi-Granularity Class Prototype Topology Distillation for Class-Incremental Source-Free Unsupervised Domain Adaptation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Multi-Granularity_Class_Prototype_Topology_Distillation_for_Class-Incremental_Source-Free_Unsupervised_Domain_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Peihua Deng, Jiehua Zhang, Xichun Sheng, Chenggang Yan, Yaoqi Sun, Ying Fu et al.
- **🏷️ 机构**: Hangzhou Dianzi University, Xi&#x2019;an Jiaotong University, Macao Polytechnic University
- **会议**: CVPR 2025
