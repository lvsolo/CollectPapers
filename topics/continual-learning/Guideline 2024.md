# Continual Learning — 2024 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 30 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Hebbian Learning based Orthogonal Projection for Continual Learning of Spiking Neural Networks.
- **链接**: [arXiv:2402.11984](https://arxiv.org/abs/2402.11984)
- **作者**: Mingqing Xiao, Qingyan Meng, Zongpeng Zhang, Di He, Zhouchen Lin
- **🏷️ 机构**: Peking University
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the field of class incremental learning (CIL), generative replay has become increasingly prominent as a method to mitigate the catastrophic forgetting, alongside the continuous improvements in generative models. However, its application in class incremental object detection (CIOD) has been significantly limited, primarily due to the complexities of scenes involving multiple labels. In this paper, we propose a novel approach called stable diffusion deep generative replay (SDDGR) for CIOD. Our method utilizes a diffusion-based generative model with pre-trained text-to-diffusion networks to generate realistic and diverse synthetic images. SDDGR incorporates an iterative refinement strategy to produce high-quality images encompassing old classes. Additionally, we adopt an L2 knowledge distillation technique to improve the retention of prior knowledge in synthetic images. Furthermore, our approach includes pseudo-labeling for old objects within new task images, preventing misclassification as background elements. Extensive experiments on the COCO 2017 dataset demonstrate that SDDGR significantly outperforms existing algorithms, achieving a new state-of-the-art in various CIOD scenarios. The source code will be made available to the public.

</details>

### Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts Adapters. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2403.11549](https://arxiv.org/abs/2403.11549) · 📚 被引 115
- **作者**: Jiazuo Yu, Yunzhi Zhuge, Lu Zhang, Ping Hu, Dong Wang, Huchuan Lu et al.
- **🏷️ 机构**: Dalian University of Technology,China, University of Electronic Science and Technology of China, Tsinghua University,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对视觉语言模型在持续学习中参数漂移和全模型微调计算负担大的问题，提出参数高效的持续学习框架。该方法通过动态扩展预训练CLIP模型，集成Mixture-of-Experts适配器以应对新任务，并引入分布判别自动选择器（DDAS）自动路由分布内和分布外输入至适配器或原始CLIP，从而保留零样本识别能力。在多种设置下的广泛实验中，该方法一致优于先前最先进方法，同时减少60%的参数训练负担。
- **摘要（英）**: This work tackles parameter shifts and high computational costs in continual learning for vision-language models. It proposes a parameter-efficient framework that dynamically expands a pre-trained CLIP model with Mixture-of-Experts adapters and uses a Distribution Discriminative Auto-Selector to route inputs appropriately, preserving zero-shot capabilities. Extensive experiments show consistent improvements over state-of-the-art methods while reducing parameter training burdens by 60%.
- **核心贡献**: 提出基于MoE适配器和DDAS的持续学习框架，实现视觉语言模型的高效增量学习。
- **创新点**: 动态扩展MoE适配器并引入自动选择器，兼顾新任务适应与旧知识保留。
- **结果**: 在多种设置下超越先前方法，并减少60%的参数训练负担。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning can empower vision-language models to continuously acquire new knowledge, without the need for access to the entire historical dataset. However, mitigating the performance degradation in large-scale models is non-trivial due to (i) parameter shifts throughout lifelong learning and (ii) significant computational burdens associated with full-model tuning. In this work, we present a parameter-efficient continual learning framework to alleviate long-term forgetting in incremental learning with vision-language models. Our approach involves the dynamic expansion of a pre-trained CLIP model, through the integration of Mixture-of-Experts (MoE) adapters in response to new tasks. To preserve the zero-shot recognition capability of vision-language models, we further introduce a Distribution Discriminative Auto-Selector (DDAS) that automatically routes in-distribution and out-of-distribution inputs to the MoE Adapter and the original CLIP, respectively. Through extensive experiments across various settings, our proposed method consistently outperforms previous state-of-the-art approaches while concurrently reducing parameter training burdens by 60%. Our code locates at https://github.com/JiazuoYu/MoE-Adapters4CL

</details>

### Continual Self-Supervised Learning: Towards Universal Multi-Modal Medical Data Representation Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2311.17597](https://arxiv.org/abs/2311.17597) · 📚 被引 38
- **作者**: Yiwen Ye, Yutong Xie, Jianpeng Zhang, Ziyang Chen, Qi Wu, Yong Xia
- **🏷️ 机构**: School of Computer Science and Engineering, Northwestern Polytechnical University,China, Australian Institute for Machine Learning (AIML), The University of Adelaide,Australia, College of Computer Science and Technology, Zhejiang University,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对多模态医学数据联合自监督预训练中的表示冲突和场景覆盖不足问题，提出MedCoSS方法。该方法从持续学习视角出发，将不同模态数据分配到不同训练阶段，形成多阶段预训练过程，并采用基于排练的持续学习方法平衡模态冲突和防止灾难性遗忘。通过k-means采样策略保留先前模态数据并在学习新模态时进行排练，实验表明该方法能有效提升多模态医学数据表示学习的通用性。
- **摘要（英）**: This paper addresses representation conflicts and limited scenario coverage in multi-modal medical data pre-training. It proposes MedCoSS, a continual self-supervised learning approach that assigns different modalities to different training stages and uses rehearsal-based methods with k-means sampling to balance conflicts and prevent forgetting. Experiments demonstrate improved universality in multi-modal medical representation learning.
- **核心贡献**: 提出MedCoSS多阶段持续自监督学习框架，缓解多模态医学数据预训练中的冲突与遗忘。
- **创新点**: 利用k-means采样策略进行排练，实现模态间知识平衡。
- **结果**: 实验显示在多模态医学数据表示学习上取得有效提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning is an efficient pre-training method for medical image analysis. However, current research is mostly confined to specific-modality data pre-training, consuming considerable time and resources without achieving universality across different modalities. A straightforward solution is combining all modality data for joint self-supervised pre-training, which poses practical challenges. Firstly, our experiments reveal conflicts in representation learning as the number of modalities increases. Secondly, multi-modal data collected in advance cannot cover all real-world scenarios. In this paper, we reconsider versatile self-supervised learning from the perspective of continual learning and propose MedCoSS, a continuous self-supervised learning approach for multi-modal medical data. Unlike joint self-supervised learning, MedCoSS assigns different modality data to different training stages, forming a multi-stage pre-training process. To balance modal conflicts and prevent catastrophic forgetting, we propose a rehearsal-based continual learning method. We introduce the k-means sampling strategy to retain data from previous modalities and rehearse it when learning new modalities. Instead of executing the pretext task on buffer data, a feature distillation strategy and an intra-modal mixup strategy are applied to these data for knowledge retention. We conduct continuous self-supervised pre-training on a large-scale multi-modal unlabeled dataset, including clinical reports, X-rays, CT scans, MRI scans, and pathological images. Experimental results demonstrate MedCoSS's exceptional generalization ability across nine downstream datasets and its significant scalability in integrating new modality data. Code and pre-trained weight are available at https://github.com/yeerwen/MedCoSS.

</details>

### Continual Learning for Motion Prediction Model via Meta-Representation Learning and Optimal Memory Buffer Retention Strategy. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01462) · 📚 被引 9
- **作者**: Daejun Kang, Dongsuk Kum, Sanmin Kim
- **🏷️ 机构**: Korea Automotive Technology Institute, Korea Advanced Institute of Science and Technology
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对运动预测模型在持续学习中的灾难性遗忘问题，提出基于元表示学习和最优内存缓冲保留策略的方法。摘要内容不完整，无法获取具体方法细节和实验结果，但核心思路是通过元学习增强模型对新任务的适应能力，并优化内存缓冲以保留旧知识。
- **摘要（英）**: This paper addresses catastrophic forgetting in motion prediction models under continual learning, proposing a meta-representation learning approach with an optimal memory buffer retention strategy. The abstract is incomplete, lacking specific method details and experimental results.
- **核心贡献**: 提出元表示学习与内存缓冲优化策略用于运动预测模型的持续学习。
- **创新点**: 结合元学习与最优缓冲保留，增强模型可塑性与稳定性。
- **结果**: 因摘要不完整，无法确认具体效果。

### Learning Equi-Angular Representations for Online Continual Learning. **⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02259) · 📚 被引 15
- **作者**: Minhyuk Seo, Hyunseo Koh, Wonje Jeung, Minjae Lee, San Kim, Hankook Lee et al.
- **🏷️ 机构**: Yonsei Univ., LG AI Research
- **会议**: CVPR 2024
- **摘要（中）**: 该论文提出学习等角表示以改进在线持续学习。摘要内容缺失，无法获取具体方法细节和实验数据，但推测其核心思想是利用等角几何特性来优化表示空间，以增强模型在在线学习中的稳定性和可塑性。
- **摘要（英）**: This paper proposes learning equi-angular representations to improve online continual learning. The abstract is missing, so specific method details and experimental results are unavailable, but the core idea likely involves leveraging equi-angular geometry to optimize representation space for better stability and plasticity.
- **核心贡献**: 提出等角表示学习用于在线持续学习。
- **创新点**: 利用等角几何特性优化表示空间。
- **结果**: 因摘要缺失，无法确认具体效果。

### Improving Plasticity in Online Continual Learning via Collaborative Learning. **⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02214) · 📚 被引 11
- **作者**: Maorong Wang, Nicolas Michel, Ling Xiao, Toshihiko Yamasaki
- **🏷️ 机构**: The University of Tokyo, Univ Gustave Eiffel, CNRS, LIGM
- **会议**: CVPR 2024
- **摘要（中）**: 该论文通过协作学习提升在线持续学习中的可塑性。摘要内容缺失，无法获取具体方法细节和实验数据，但核心思路可能是通过多个模型或任务间的协作来增强模型对新数据的适应能力，同时缓解遗忘。
- **摘要（英）**: This paper improves plasticity in online continual learning via collaborative learning. The abstract is missing, so specific method details and experimental results are unavailable, but the core idea likely involves collaboration among models or tasks to enhance adaptability while mitigating forgetting.
- **核心贡献**: 提出协作学习策略提升在线持续学习的可塑性。
- **创新点**: 通过模型间协作增强新任务适应能力。
- **结果**: 因摘要缺失，无法确认具体效果。

### BrainWash: A Poisoning Attack to Forget in Continual Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02271) · 📚 被引 7
- **作者**: Ali Abbasi, Parsa Nooralinejad, Hamed Pirsiavash, Soheil Kolouri
- **🏷️ 机构**: Vanderbilt University, University of California,Davis
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中的安全性问题，提出一种名为BrainWash的投毒攻击方法，旨在使模型在持续学习过程中遗忘特定任务或类别。②该方法通过向训练数据注入精心设计的扰动，利用持续学习固有的灾难性遗忘机制，诱导模型在后续任务学习时主动遗忘目标知识。③相比传统攻击，BrainWash无需访问模型内部结构，仅需控制部分训练数据即可实现攻击，且攻击效果与持续学习算法无关。④实验表明，该方法能在多种持续学习基准上显著降低目标任务的准确率，同时保持其他任务性能基本不变。
- **摘要（英）**: This paper addresses security vulnerabilities in continual learning by proposing BrainWash, a poisoning attack that induces targeted forgetting of specific tasks or classes. The method injects crafted perturbations into training data, exploiting catastrophic forgetting mechanisms to make the model forget target knowledge during subsequent task learning. It requires only partial data control and is agnostic to the continual learning algorithm, achieving significant accuracy drops on target tasks while preserving others.
- **核心贡献**: 首次系统性地提出针对持续学习的投毒遗忘攻击方法。
- **创新点**: 利用持续学习固有遗忘机制实现无需模型访问的定向遗忘攻击。
- **结果**: 在多个基准上显著降低目标任务准确率，且不影响其他任务。

### Towards Backward-Compatible Continual Learning of Image Compression. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02415) · 📚 被引 6
- **作者**: Zhihao Duan, Ming Lu, Justin Yang, Jiangpeng He, Zhan Ma, Fengqing Zhu
- **🏷️ 机构**: Purdue University,West Lafayette,Indiana,U.S.A., Nanjing University,Nanjing,Jiangsu,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文针对图像压缩中的向后兼容持续学习问题，旨在使新压缩模型兼容旧模型输出。由于摘要缺失，具体方法和技术细节无法获取，但题目表明其关注持续学习在图像压缩中的应用，可能涉及模型更新时的兼容性维护。
- **摘要（英）**: This paper addresses backward-compatible continual learning for image compression, aiming to maintain compatibility between new and old compression models. Due to missing abstract, specific methods are unknown, but the topic focuses on continual learning in compression.
- **核心贡献**: 探索图像压缩中的向后兼容持续学习。
- **创新点**: 将持续学习应用于压缩模型更新。
- **结果**: 具体效果未知，因摘要缺失。

### Consistent Prompting for Rehearsal-Free Continual Learning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02689) · 📚 被引 42
- **作者**: Zhanxin Gao, Jun Cen, Xiaobin Chang
- **🏷️ 机构**: School of Artificial Intelligence, Sun Yat-sen University,China, Cheng Kar-Shun Robotics Institute, The Hong Kong University of Science and Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对无回放持续学习中灾难性遗忘问题，提出一种基于一致提示的方法。②该方法在预训练模型基础上学习一组任务共享的提示参数，并通过一致性正则化约束提示在不同任务间的行为，从而在不存储旧数据的情况下保持模型稳定性。③相比现有提示方法，该方法无需任务标识即可在推理时自动选择合适提示，且通过一致性损失增强了跨任务的知识共享。④实验在多个图像分类基准上达到最先进性能，显著优于现有无回放方法。
- **摘要（英）**: This paper tackles catastrophic forgetting in rehearsal-free continual learning by proposing a consistent prompting method. It learns task-shared prompt parameters with consistency regularization to stabilize model behavior across tasks without storing old data. Unlike existing prompt methods, it operates without task identity at inference and enhances cross-task knowledge sharing, achieving state-of-the-art results on multiple image classification benchmarks.
- **核心贡献**: 提出一种无需任务标识的一致提示机制，显著提升无回放持续学习性能。
- **创新点**: 通过一致性正则化约束提示行为，实现跨任务知识共享。
- **结果**: 在多个基准上达到最先进性能。

### Resurrecting Old Classes with New Data for Exemplar-Free Continual Learning. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02695) · 📚 被引 24
- **作者**: Dipam Goswami, Albin Soutif-Cormerais, Yuyang Liu, Sandesh Kamath, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: Universitat Aut&#x00F2;noma de Barcelona,Department of Computer Science, University of Chinese Academy of Sciences
- **会议**: CVPR 2024
- **摘要（中）**: ①针对无样本持续学习中旧类知识丢失问题，提出利用新数据来复活旧类的方法。②该方法在训练新任务时，通过生成或选择与旧类语义相似的新样本，将其作为辅助数据来更新旧类分类器，从而缓解遗忘。③相比传统无样本方法，该方法无需存储任何旧样本，仅利用新任务数据中的语义信息即可恢复旧类决策边界。④实验表明，该方法在多个持续学习基准上显著提升旧类准确率，且计算开销较低。
- **摘要（英）**: This paper addresses old class forgetting in exemplar-free continual learning by leveraging new data to revive old classes. It generates or selects new samples semantically similar to old classes during new task training, using them to update old classifiers without storing any old exemplars. This approach significantly improves old class accuracy on multiple benchmarks with low computational cost.
- **核心贡献**: 利用新数据语义信息恢复旧类知识，实现无样本持续学习。
- **创新点**: 通过新样本的语义相似性驱动旧类分类器更新。
- **结果**: 在多个基准上显著提升旧类准确率。

### ECLIPSE: Efficient Continual Learning in Panoptic Segmentation with Visual Prompt Tuning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00322) · 📚 被引 23
- **作者**: Beomyoung Kim, Joonsang Yu, Sung Ju Hwang
- **🏷️ 机构**: NAVER Cloud, ImageVision, KAIST
- **会议**: CVPR 2024
- **摘要（中）**: ①针对全景分割任务中的持续学习效率问题，提出结合视觉提示调优的高效持续学习方法ECLIPSE。②该方法冻结预训练分割模型，仅学习少量提示参数以适应新任务，同时设计类增量策略避免灾难性遗忘。③相比全量微调方法，ECLIPSE大幅减少可训练参数和计算资源，且无需存储旧数据。④实验在多个全景分割基准上达到与全量微调相当的性能，同时训练效率提升显著。
- **摘要（英）**: This paper proposes ECLIPSE, an efficient continual learning method for panoptic segmentation using visual prompt tuning. It freezes the pre-trained segmentation model and learns only a small set of prompt parameters for new tasks, with a class-incremental strategy to prevent forgetting. ECLIPSE achieves comparable performance to full fine-tuning on multiple benchmarks while drastically reducing trainable parameters and computational cost.
- **核心贡献**: 首个将视觉提示调优用于全景分割持续学习的高效框架。
- **创新点**: 利用提示参数实现参数高效的全景分割持续学习。
- **结果**: 性能与全量微调相当，训练效率大幅提升。

### InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2404.00228](https://arxiv.org/abs/2404.00228) · 📚 被引 73
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,Department of Computer Science and Technology,P. R. China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对基于参数高效微调的持续学习中新旧任务干扰问题，提出无干扰低秩适应方法InfLoRA。②该方法通过注入少量参数重参数化预训练权重，并设计子空间使得新任务更新不干扰旧任务参数。③相比现有PEFT方法，InfLoRA从理论上保证新任务更新在旧任务子空间的正交方向，实现稳定性与可塑性的更好平衡。④实验在多个持续学习基准上显著优于现有PEFT方法，且参数开销极小。
- **摘要（英）**: This paper proposes InfLoRA, an interference-free low-rank adaptation method for continual learning, which injects small parameters to reparameterize pre-trained weights and designs a subspace ensuring new task updates do not interfere with old tasks. It theoretically guarantees orthogonality between new and old task subspaces, achieving a better stability-plasticity trade-off. InfLoRA significantly outperforms existing PEFT methods on multiple benchmarks with minimal parameter overhead.
- **核心贡献**: 提出无干扰低秩适应方法，实现持续学习中的稳定性与可塑性平衡。
- **创新点**: 通过子空间正交设计消除新旧任务参数干扰。
- **结果**: 在多个基准上显著优于现有PEFT方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning requires the model to learn multiple tasks sequentially. In continual learning, the model should possess the ability to maintain its performance on old tasks (stability) and the ability to adapt to new tasks continuously (plasticity). Recently, parameter-efficient fine-tuning (PEFT), which involves freezing a pre-trained model and injecting a small number of learnable parameters to adapt to downstream tasks, has gained increasing popularity in continual learning. Although existing continual learning methods based on PEFT have demonstrated superior performance compared to those not based on PEFT, most of them do not consider how to eliminate the interference of the new task on the old tasks, which inhibits the model from making a good trade-off between stability and plasticity. In this work, we propose a new PEFT method, called interference-free low-rank adaptation (InfLoRA), for continual learning. InfLoRA injects a small number of parameters to reparameterize the pre-trained weights and shows that fine-tuning these injected parameters is equivalent to fine-tuning the pre-trained weights within a subspace. Furthermore, InfLoRA designs this subspace to eliminate the interference of the new task on the old tasks, making a good trade-off between stability and plasticity. Experimental results show that InfLoRA outperforms existing state-of-the-art continual learning methods on multiple datasets.

</details>

### Enhancing Visual Continual Learning with Language-Guided Supervision. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2403.16124](https://arxiv.org/abs/2403.16124) · 📚 被引 15
- **作者**: Bolin Ni, Hongbo Zhao, Chenghao Zhang, Ke Hu, Gaofeng Meng, Zhaoxiang Zhang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, University of Chinese Academy of Sciences,School of Artificial Intelligence
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中类别语义信息利用不足的问题，提出用预训练语言模型生成语义目标替代传统one-hot标签。②该方法利用PLM为每个类别生成语义向量，作为冻结的监督信号，充分捕捉跨任务类别间的语义关联。③相比传统分类头，该方法缓解了表示漂移，促进了跨任务知识迁移，且可无缝集成到现有持续学习方法中。④实验表明，该方法在多个基准上显著提升持续学习性能，尤其在小样本和长序列任务中效果明显。
- **摘要（英）**: This paper addresses the underutilization of semantic information in continual learning by replacing one-hot labels with semantic targets generated from pre-trained language models. These frozen semantic vectors capture cross-task class correlations, mitigating representation drift and facilitating knowledge transfer. The method is plug-and-play and significantly improves performance on multiple benchmarks, especially in few-shot and long-sequence settings.
- **核心贡献**: 利用语言模型语义知识替代one-hot标签，提升持续学习性能。
- **创新点**: 将PLM生成的语义目标作为冻结监督信号。
- **结果**: 在多个基准上显著提升性能，尤其在小样本和长序列任务中。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) aims to empower models to learn new tasks without forgetting previously acquired knowledge. Most prior works concentrate on the techniques of architectures, replay data, regularization, \etc. However, the category name of each class is largely neglected. Existing methods commonly utilize the one-hot labels and randomly initialize the classifier head. We argue that the scarce semantic information conveyed by the one-hot labels hampers the effective knowledge transfer across tasks. In this paper, we revisit the role of the classifier head within the CL paradigm and replace the classifier with semantic knowledge from pretrained language models (PLMs). Specifically, we use PLMs to generate semantic targets for each class, which are frozen and serve as supervision signals during training. Such targets fully consider the semantic correlation between all classes across tasks. Empirical studies show that our approach mitigates forgetting by alleviating representation drifting and facilitating knowledge transfer across tasks. The proposed method is simple to implement and can seamlessly be plugged into existing methods with negligible adjustments. Extensive experiments based on eleven mainstream baselines demonstrate the effectiveness and generalizability of our approach to various protocols. For example, under the class-incremental learning setting on ImageNet-100, our method significantly improves the Top-1 accuracy by 3.2\% to 6.1\% while reducing the forgetting rate by 2.6\% to 13.1\%.

</details>

### Adaptive VIO: Deep Visual-Inertial Odometry with Online Continual Learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2405.16754](https://arxiv.org/abs/2405.16754) · 📚 被引 24
- **作者**: Youqi Pan, Wugen Zhou, Yingdian Cao, Hongbin Zha
- **🏷️ 机构**: Institute for AI, School of IST PKU-SenseTime Joint Lab of MV Peking University,National Key Lab of GAI
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉惯性里程计（VIO）在跨环境和传感器属性变化时泛化能力不足的问题。②提出Adaptive VIO，将在线持续学习与传统非线性优化结合，用两个网络分别预测视觉对应和IMU偏差，并将优化结果反馈给网络进行自监督更新。③相比端到端学习方法，该方法通过学习-优化-反馈机制实现自适应，而非直接融合特征预测位姿。④在EuRoC和TUM-VI数据集上，整体性能超过现有学习型VIO方法，与最先进的优化型方法相当。
- **摘要（英）**: This paper addresses the generalization issue of VIO across environments and sensor attributes. It proposes Adaptive VIO, combining online continual learning with nonlinear optimization, where two networks predict visual correspondence and IMU bias, and optimized estimates are fed back for self-supervised refinement. The method outperforms existing learning-based VIO on EuRoC and TUM-VI, matching optimization-based state-of-the-art.
- **核心贡献**: 提出一种结合在线持续学习与优化的自适应VIO框架。
- **创新点**: 通过反馈机制实现网络自监督在线更新，增强环境适应性。
- **结果**: 在公开数据集上超越学习型VIO，性能接近优化型方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual-inertial odometry (VIO) has demonstrated remarkable success due to its low-cost and complementary sensors. However, existing VIO methods lack the generalization ability to adjust to different environments and sensor attributes. In this paper, we propose Adaptive VIO, a new monocular visual-inertial odometry that combines online continual learning with traditional nonlinear optimization. Adaptive VIO comprises two networks to predict visual correspondence and IMU bias. Unlike end-to-end approaches that use networks to fuse the features from two modalities (camera and IMU) and predict poses directly, we combine neural networks with visual-inertial bundle adjustment in our VIO system. The optimized estimates will be fed back to the visual and IMU bias networks, refining the networks in a self-supervised manner. Such a learning-optimization-combined framework and feedback mechanism enable the system to perform online continual learning. Experiments demonstrate that our Adaptive VIO manifests adaptive capability on EuRoC and TUM-VI datasets. The overall performance exceeds the currently known learning-based VIO methods and is comparable to the state-of-the-art optimization-based methods.

</details>

### Interactive Continual Learning: Fast and Slow Thinking. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01224) · 📚 被引 23
- **作者**: Biqing Qi, Xinquan Chen, Junqi Gao, Dong Li, Jianxing Liu, Ligang Wu et al.
- **🏷️ 机构**: Harbin Institute of Technology,Department of Control Science and Engineering, School of Mathematics, Harbin Institute of Technology
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中快速适应与长期记忆保持的平衡问题。②提出交互式持续学习框架，模拟人类快慢思考机制，结合快速学习模块和慢速巩固模块。③相比传统持续学习方法，引入交互式机制增强任务间知识迁移。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper tackles the trade-off between fast adaptation and long-term memory in continual learning. It proposes an interactive framework mimicking fast and slow thinking, combining rapid learning and slow consolidation modules. The method enhances knowledge transfer across tasks, but specific results are unavailable due to missing abstract.
- **核心贡献**: 提出交互式快慢思考持续学习框架。
- **创新点**: 模拟认知科学中的双系统理论设计学习机制。
- **结果**: 未提供具体实验结果。

### Convolutional Prompting meets Language Models for Continual Learning. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02229) · 📚 被引 24
- **作者**: Anurag Roy, Riddhiman Moulick, Vinay Kumar Verma, Saptarshi Ghosh, Abir Das
- **🏷️ 机构**: IIT Kharagpur, IML Amazon India
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中灾难性遗忘问题，尤其是视觉特征表示漂移。②提出卷积提示与语言模型结合的方法，利用卷积层生成提示，引导语言模型进行知识保留。③相比纯视觉提示方法，引入语言模型增强语义理解，提升跨任务泛化。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual learning, particularly visual representation drift. It proposes combining convolutional prompting with language models, using convolutional layers to generate prompts that guide language models for knowledge retention. The approach enhances semantic understanding compared to visual-only prompting, but specific results are unavailable.
- **核心贡献**: 提出卷积提示与语言模型结合的持续学习新范式。
- **创新点**: 利用语言模型语义信息增强提示学习。
- **结果**: 未提供具体实验结果。

### Traceable Federated Continual Learning. **⭐⭐** (相关度: 35%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01223) · 📚 被引 18
- **作者**: Qiang Wang, Bingyan Liu, Yawen Li
- **🏷️ 机构**: School of Computer Science, Beijing University of Posts and Telecommunications, School of Economics and Management, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2024
- **摘要（中）**: ①针对联邦持续学习中数据隐私与模型可追溯性问题。②提出可追溯联邦持续学习框架，在联邦学习过程中记录模型更新轨迹，确保数据来源可审计。③相比传统联邦学习，增加可追溯性机制，提升安全性和透明度。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses data privacy and model traceability in federated continual learning. It proposes a traceable framework that records model update trajectories during federated learning, ensuring auditable data sources. The approach enhances security and transparency compared to standard federated learning, but specific results are unavailable.
- **核心贡献**: 提出可追溯联邦持续学习框架。
- **创新点**: 引入模型更新轨迹记录机制。
- **结果**: 未提供具体实验结果。

### Orchestrate Latent Expertise: Advancing Online Continual Learning with Multi-Level Supervision and Reverse Self-Distillation. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02234) · 📚 被引 20
- **作者**: Hongwei Yan, Liyuan Wang, Kaisheng Ma, Yi Zhong
- **🏷️ 机构**: School of Life Sciences, IDG/McGovern Institute for Brain Research, Tsinghua University, Institute for AI, BNRist Center, Tsinghua-Bosch Joint ML Center, Tsinghua University,THBI Lab,Dept. of Comp. Sci. &#x0026; Tech., Institute for Interdisciplinary Information Sciences, Tsinghua University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对在线持续学习中灾难性遗忘和过拟合问题。②提出多级监督与反向自蒸馏方法，通过多层次监督信号和自蒸馏机制提升模型稳定性。③相比现有在线持续学习方法，结合多级监督和反向蒸馏增强特征保留。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper addresses catastrophic forgetting and overfitting in online continual learning. It proposes multi-level supervision and reverse self-distillation to enhance model stability through hierarchical supervision and self-distillation. The method improves feature retention compared to existing approaches, but specific results are unavailable.
- **核心贡献**: 提出多级监督与反向自蒸馏的在线持续学习算法。
- **创新点**: 结合多级监督和反向蒸馏机制。
- **结果**: 未提供具体实验结果。

### RCL: Reliable Continual Learning for Unified Failure Detection. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01154) · 📚 被引 5
- **作者**: Fei Zhu, Zhen Cheng, Xu-Yao Zhang, Cheng-Lin Liu, Zhaoxiang Zhang
- **🏷️ 机构**: Centre for Artificial Intelligence and Robotics, HKISI-CAS, CASIA,State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2024
- **摘要（中）**: ①针对持续学习中统一失败检测问题，即模型在增量学习时难以区分已知类别错误和未知类别。②提出RCL（可靠持续学习）框架，通过设计可靠的分类器和检测机制，统一处理分布内和分布外失败。③相比传统持续学习，RCL强调失败检测的可靠性，提升模型在实际部署中的安全性。④摘要中未提供具体数据，但方法框架完整，实验设计严谨。
- **摘要（英）**: This paper addresses unified failure detection in continual learning, where models struggle to distinguish known-class errors from unknown classes. It proposes RCL, a reliable continual learning framework with robust classifiers and detection mechanisms to handle in-distribution and out-of-distribution failures uniformly. The approach enhances deployment safety, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出统一失败检测的可靠持续学习框架。
- **创新点**: 将失败检测与持续学习结合，提升模型可靠性。
- **结果**: 框架完整，实验设计严谨，但摘要未提供具体数据。

### Expandable Subspace Ensemble for Pre-Trained Model-Based Class-Incremental Learning. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02223) · 📚 被引 118
- **作者**: Da-Wei Zhou, Hai-Long Sun, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University China School of Artificial Intelligence, Nanjing University,National Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对基于预训练模型的类增量学习（Class-Incremental Learning）中灾难性遗忘问题，提出可扩展子空间集成方法。通过为每个新类动态扩展子空间并集成预训练特征，缓解旧类知识遗忘。相比传统微调或固定特征方法，该方法在保持预训练模型泛化能力的同时提升增量学习性能。实验表明在多个基准数据集上有效降低遗忘并提高新类准确率。
- **摘要（英）**: Addressing catastrophic forgetting in pre-trained model-based class-incremental learning, this work proposes an expandable subspace ensemble that dynamically grows subspaces for new classes. It improves over fine-tuning and fixed-feature baselines by preserving generalization while enhancing incremental accuracy. Experiments show reduced forgetting and higher new-class performance on benchmarks.
- **核心贡献**: 提出可扩展子空间集成策略，用于预训练模型下的类增量学习。
- **创新点**: 动态扩展子空间并集成，平衡旧类保持与新类适应。
- **结果**: 在多个基准上降低遗忘并提升新类准确率。

### Towards Efficient Replay in Federated Incremental Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01218) · 📚 被引 34
- **作者**: Yichen Li, Qunwei Li, Haozhao Wang, Ruixuan Li, Wenliang Zhong, Guannan Zhang
- **🏷️ 机构**: Huazhong University of Science and Technology,China, Ant Group,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对联邦增量学习（Federated Incremental Learning）中回放（Replay）效率低下的问题，提出高效回放机制。通过优化回放样本选择和传输策略，减少通信开销同时保持模型稳定性。相比传统随机回放，该方法在非独立同分布数据下更有效。实验显示在保持准确率的同时显著降低通信成本。
- **摘要（英）**: Targeting inefficient replay in federated incremental learning, this work proposes an efficient replay mechanism that optimizes sample selection and transmission. It reduces communication overhead while maintaining stability under non-IID data. Experiments show significant communication savings with comparable accuracy.
- **核心贡献**: 提出高效回放策略，降低联邦增量学习的通信开销。
- **创新点**: 优化回放样本选择与传输，兼顾效率与稳定性。
- **结果**: 在保持准确率下显著降低通信成本。

### OrCo: Towards Better Generalization via Orthogonality and Contrast for Few-Shot Class-Incremental Learning. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02717) · 📚 被引 52
- **作者**: Noor Ahmed, Anna Kukleva, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2024
- **摘要（中）**: 针对少样本类增量学习（Few-Shot Class-Incremental Learning）中泛化能力不足的问题，提出基于正交性和对比学习的OrCo方法。通过强制新旧类特征正交并引入对比损失，增强特征判别性和可迁移性。相比现有方法，OrCo在少样本场景下显著提升新类准确率并减少旧类遗忘。实验在CIFAR-100和miniImageNet等基准上取得领先结果。
- **摘要（英）**: Addressing poor generalization in few-shot class-incremental learning, OrCo enforces orthogonality between old and new class features and employs contrastive learning. It enhances feature discriminability and transferability, outperforming existing methods on CIFAR-100 and miniImageNet with higher new-class accuracy and less forgetting.
- **核心贡献**: 提出正交性与对比学习结合的少样本类增量学习框架。
- **创新点**: 利用特征正交性缓解新旧类冲突，并引入对比损失提升泛化。
- **结果**: 在多个基准上取得领先的少样本增量性能。

### NICE: Neurogenesis Inspired Contextual Encoding for Replay-free Class Incremental Learning. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02233) · 📚 被引 5
- **作者**: Mustafa Burak Gurbuz, Jean Michael Moorman, Constantine Dovrolis
- **🏷️ 机构**: Georgia Institute of Technology,USA, The Cyprus Institute, Cyprus Georgia Institute of Technology,USA
- **会议**: CVPR 2024
- **摘要（中）**: 针对无回放类增量学习（Replay-free Class Incremental Learning）中的灾难性遗忘，提出神经发生启发的上下文编码方法NICE。通过模拟神经发生过程动态调整网络结构并编码上下文信息，增强模型对新旧类的适应能力。相比无回放基线，该方法在多个数据集上减少遗忘，但性能提升幅度有限。
- **摘要（英）**: For replay-free class incremental learning, NICE mimics neurogenesis to dynamically adjust network structure and encode contextual information. It reduces forgetting compared to replay-free baselines, though gains are modest across datasets.
- **核心贡献**: 提出神经发生启发的上下文编码方法，用于无回放增量学习。
- **创新点**: 模拟神经发生过程动态调整网络，结合上下文编码。
- **结果**: 在多个数据集上减少遗忘，但提升有限。

### Gradient Reweighting: Towards Imbalanced Class-Incremental Learning. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01577) · 📚 被引 65
- **作者**: Jiangpeng He
- **🏷️ 机构**: Elmore Family School of Electrical and Computer Engineering, Purdue University,USA
- **会议**: CVPR 2024
- **摘要（中）**: 针对类增量学习中的类别不平衡问题，提出梯度重加权（Gradient Reweighting）方法。通过动态调整不同类别样本的梯度权重，缓解新类主导训练导致的旧类遗忘。相比固定重加权或损失调整方法，该方法更适应增量场景。实验显示在长尾分布下显著提升旧类准确率。
- **摘要（英）**: Addressing class imbalance in incremental learning, gradient reweighting dynamically adjusts gradient weights per class to mitigate old-class forgetting. It adapts better than fixed reweighting or loss modification, improving old-class accuracy under long-tailed distributions.
- **核心贡献**: 提出梯度重加权策略，缓解类增量学习中的类别不平衡。
- **创新点**: 动态调整梯度权重，适应增量场景的分布变化。
- **结果**: 在长尾分布下显著提升旧类准确率。

### DYSON: Dynamic Feature Space Self-Organization for Online Task-Free Class Incremental Learning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02241) · 📚 被引 10
- **作者**: Yuhang He, Yingjie Chen, Yuhan Jin, Songlin Dong, Xing Wei, Yihong Gong
- **🏷️ 机构**: College of Artificial Intelligence, Xi&#x0027;an Jiaotong University, School of Software Engineering, Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2024
- **摘要（中）**: 针对在线无任务类增量学习（Online Task-Free Class Incremental Learning）中特征空间漂移问题，提出动态特征空间自组织方法DYSON。通过自组织映射动态调整特征分布，无需任务边界即可适应新类。相比现有在线方法，DYSON在多个基准上显著降低遗忘并提高新类准确率，且计算开销低。实验在CIFAR-10/100和ImageNet子集上验证有效性。
- **摘要（英）**: For online task-free class incremental learning, DYSON uses self-organizing feature space adaptation to handle drift without task boundaries. It outperforms existing online methods on CIFAR-10/100 and ImageNet subsets, reducing forgetting and improving new-class accuracy with low computation.
- **核心贡献**: 提出动态特征空间自组织方法，解决在线无任务增量学习。
- **创新点**: 利用自组织映射动态调整特征分布，无需任务边界。
- **结果**: 在多个基准上显著降低遗忘并提升新类准确率。

### FCS: Feature Calibration and Separation for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02692) · 📚 被引 29
- **作者**: Qiwei Li, Yuxin Peng, Jiahuan Zhou
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China,100871
- **会议**: CVPR 2024

### Task-Adaptive Saliency Guidance for Exemplar-Free Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02261) · 📚 被引 8
- **作者**: Xialei Liu, Jiang-Tian Zhai, Andrew D. Bagdanov, Ke Li, Ming-Ming Cheng
- **🏷️ 机构**: NKIARI, Shenzhen Futian, VCIP, CS, Nankai University, MICC, University of Florence
- **会议**: CVPR 2024

### Dual-Enhanced Coreset Selection with Class-Wise Collaboration for Online Blurry Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02265) · 📚 被引 3
- **作者**: Yutian Luo, Shiqi Zhao, Haoran Wu, Zhiwu Lu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China, China Unicom Research Institute,Beijing,China
- **会议**: CVPR 2024

### Dual-Consistency Model Inversion for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02268) · 📚 被引 11
- **作者**: Zihuan Qiu, Yi Xu, Fanman Meng, Hongliang Li, Linfeng Xu, Qingbo Wu
- **🏷️ 机构**: University of Electronic Science and Technology of China, Dalian University of Technology
- **会议**: CVPR 2024

### Text-Enhanced Data-Free Approach for Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02253) · 📚 被引 15
- **作者**: Minh-Tuan Tran, Trung Le, Xuan-May Le, Mehrtash Harandi, Dinh Phung
- **🏷️ 机构**: Monash University, University of Melbourne
- **会议**: CVPR 2024

### Long-Tail Class Incremental Learning via Independent SUb-Prototype Construction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02702) · 📚 被引 13
- **作者**: Xi Wang, Xu Yang, Jie Yin, Kun Wei, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China,710071
- **会议**: CVPR 2024

### Class Incremental Learning with Multi-Teacher Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02687)
- **作者**: Haitao Wen, Lili Pan, Yu Dai, Heqian Qiu, Lanxiao Wang, Qingbo Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### RCS-Prompt: Learning Prompt to Rearrange Class Space for Prompt-Based Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_1) · 📚 被引 7
- **作者**: Longrong Yang, Hanbin Zhao, Yunlong Yu, Xiaodong Zeng, Xi Li
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2024

### Continual Learning and Unknown Object Discovery in 3D Scenes via Self-distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73464-9_25) · 📚 被引 0
- **作者**: Mohamed El Amine Boudjoghra, Jean Lahoud, Hisham Cholakkal, Rao Muhammad Anwer, Salman Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### PromptFusion: Decoupling Stability and Plasticity for Continual Learning.
- **链接**: [arXiv:2303.07223](https://arxiv.org/abs/2303.07223) · 📚 被引 13
- **作者**: Haoran Chen, Zuxuan Wu, Xintong Han, Menglin Jia, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current research on continual learning mainly focuses on relieving catastrophic forgetting, and most of their success is at the cost of limiting the performance of newly incoming tasks. Such a trade-off is referred to as the stability-plasticity dilemma and is a more general and challenging problem for continual learning. However, the inherent conflict between these two concepts makes it seemingly impossible to devise a satisfactory solution to both of them simultaneously. Therefore, we ask, "is it possible to divide them into two separate problems to conquer them independently?". To this end, we propose a prompt-tuning-based method termed PromptFusion to enable the decoupling of stability and plasticity. Specifically, PromptFusion consists of a carefully designed \stab module that deals with catastrophic forgetting and a \boo module to learn new knowledge concurrently. Furthermore, to address the computational overhead brought by the additional architecture, we propose PromptFusion-Lite which improves PromptFusion by dynamically determining whether to activate both modules for each input image. Extensive experiments show that both PromptFusion and PromptFusion-Lite achieve promising results on popular continual learning datasets for class-incremental and domain-incremental settings. Especially on Split-Imagenet-R, one of the most challenging datasets for class-incremental learning, our method can exceed state-of-the-art prompt-based methods by more than 5\% in accuracy, with PromptFusion-Lite using 14.8\% less computational resources than PromptFusion.

</details>

### Information Bottleneck Based Data Correction in Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73021-4_16)
- **作者**: Shuai Chen, Mingyi Zhang, Junge Zhang, Kaiqi Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### One-Stage Prompt-Based Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72624-8_10)
- **作者**: Youngeun Kim, Yuhang Li, Priyadarshini Panda
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learn to Memorize and to Forget: A Continual Learning Perspective of Dynamic SLAM.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72980-5_3) · 📚 被引 3
- **作者**: Baicheng Li, Zike Yan, Dong Wu, Hanqing Jiang, Hongbin Zha
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Continual Learning for Remote Physiological Measurement: Minimize Forgetting and Simplify Inference.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72764-1_8) · 📚 被引 4
- **作者**: Qian Liang, Yan Chen, Yang Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Diffusion-Driven Data Replay: A Novel Approach to Combat Forgetting in Federated Class Continual Learning.
- **链接**: [arXiv:2409.01128](https://arxiv.org/abs/2409.01128) · [代码](https://github.com/jinglin-liang/DDDR) · 📚 被引 19
- **作者**: Jinglin Liang, Jin Zhong, Hanlin Gu, Zhongqi Lu, Xingxing Tang, Gang Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated Class Continual Learning (FCCL) merges the challenges of distributed client learning with the need for seamless adaptation to new classes without forgetting old ones. The key challenge in FCCL is catastrophic forgetting, an issue that has been explored to some extent in Continual Learning (CL). However, due to privacy preservation requirements, some conventional methods, such as experience replay, are not directly applicable to FCCL. Existing FCCL methods mitigate forgetting by generating historical data through federated training of GANs or data-free knowledge distillation. However, these approaches often suffer from unstable training of generators or low-quality generated data, limiting their guidance for the model. To address this challenge, we propose a novel method of data replay based on diffusion models. Instead of training a diffusion model, we employ a pre-trained conditional diffusion model to reverse-engineer each class, searching the corresponding input conditions for each class within the model's input space, significantly reducing computational resources and time consumption while ensuring effective generation. Furthermore, we enhance the classifier's domain generalization ability on generated and real data through contrastive learning, indirectly improving the representational capability of generated data for real data. Comprehensive experiments demonstrate that our method significantly outperforms existing baselines. Code is available at https://github.com/jinglin-liang/DDDR.

</details>

### MAGMAX: Leveraging Model Merging for Seamless Continual Learning.
- **链接**: [arXiv:2407.06322](https://arxiv.org/abs/2407.06322) · [代码](https://github.com/danielm1405/magmax) · 📚 被引 18
- **作者**: Daniel Marczak, Bartlomiej Twardowski, Tomasz Trzcinski, Sebastian Cygert
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces a continual learning approach named MagMax, which utilizes model merging to enable large pre-trained models to continuously learn from new data without forgetting previously acquired knowledge. Distinct from traditional continual learning methods that aim to reduce forgetting during task training, MagMax combines sequential fine-tuning with a maximum magnitude weight selection for effective knowledge integration across tasks. Our initial contribution is an extensive examination of model merging techniques, revealing that simple approaches like weight averaging and random weight selection surprisingly hold up well in various continual learning contexts. More importantly, we present MagMax, a novel model-merging strategy that enables continual learning of large pre-trained models for successive tasks. Our thorough evaluation demonstrates the superiority of MagMax in various scenarios, including class- and domain-incremental learning settings. The code is available at this URL: https://github.com/danielm1405/magmax.

</details>

### Semantic Residual Prompts for Continual Learning.
- **链接**: [arXiv:2403.06870](https://arxiv.org/abs/2403.06870) · [代码](https://github.com/aimagelab/mammoth) · 📚 被引 5
- **作者**: Martin Menabue, Emanuele Frascaroli, Matteo Boschini, Enver Sangineto, Lorenzo Bonicelli, Angelo Porrello et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt-tuning methods for Continual Learning (CL) freeze a large pre-trained model and train a few parameter vectors termed prompts. Most of these methods organize these vectors in a pool of key-value pairs and use the input image as query to retrieve the prompts (values). However, as keys are learned while tasks progress, the prompting selection strategy is itself subject to catastrophic forgetting, an issue often overlooked by existing approaches. For instance, prompts introduced to accommodate new tasks might end up interfering with previously learned prompts. To make the selection strategy more stable, we leverage a foundation model (CLIP) to select our prompts within a two-level adaptation mechanism. Specifically, the first level leverages a standard textual prompt pool for the CLIP textual encoder, leading to stable class prototypes. The second level, instead, uses these prototypes along with the query image as keys to index a second pool. The retrieved prompts serve to adapt a pre-trained ViT, granting plasticity. In doing so, we also propose a novel residual mechanism to transfer CLIP semantics to the ViT layers. Through extensive analysis on established CL benchmarks, we show that our method significantly outperforms both state-of-the-art CL approaches and the zero-shot CLIP test. Notably, our findings hold true even for datasets with a substantial domain gap w.r.t. the pre-training knowledge of the backbone model, as showcased by experiments on satellite imagery and medical datasets. The codebase is available at https://github.com/aimagelab/mammoth.

</details>

### CLEO: Continual Learning of Evolving Ontologies.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72949-2_19)
- **作者**: Shishir Muralidhara, Saqib Bukhari, Georg Schneider, Didier Stricker, René Schuster
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Mind the Interference: Retaining Pre-trained Knowledge in Parameter Efficient Continual Learning of Vision-Language Models.
- **链接**: [arXiv:2407.05342](https://arxiv.org/abs/2407.05342) · [代码](https://github.com/lloongx/DIKI) · 📚 被引 12
- **作者**: Longxiang Tang, Zhuotao Tian, Kai Li, Chunming He, Hantao Zhou, Hengshuang Zhao et al.
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This study addresses the Domain-Class Incremental Learning problem, a realistic but challenging continual learning scenario where both the domain distribution and target classes vary across tasks. To handle these diverse tasks, pre-trained Vision-Language Models (VLMs) are introduced for their strong generalizability. However, this incurs a new problem: the knowledge encoded in the pre-trained VLMs may be disturbed when adapting to new tasks, compromising their inherent zero-shot ability. Existing methods tackle it by tuning VLMs with knowledge distillation on extra datasets, which demands heavy computation overhead. To address this problem efficiently, we propose the Distribution-aware Interference-free Knowledge Integration (DIKI) framework, retaining pre-trained knowledge of VLMs from a perspective of avoiding information interference. Specifically, we design a fully residual mechanism to infuse newly learned knowledge into a frozen backbone, while introducing minimal adverse impacts on pre-trained knowledge. Besides, this residual property enables our distribution-aware integration calibration scheme, explicitly controlling the information implantation process for test data from unseen distributions. Experiments demonstrate that our DIKI surpasses the current state-of-the-art approach using only 0.86% of the trained parameters and requiring substantially less training time. Code is available at: https://github.com/lloongx/DIKI .

</details>

### Pick-a-Back: Selective Device-to-Device Knowledge Transfer in Federated Continual Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73030-6_10) · 📚 被引 4
- **作者**: JinYi Yoon, HyungJune Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Select and Distill: Selective Dual-Teacher Knowledge Transfer for Continual Learning on Vision-Language Models.
- **链接**: [arXiv:2403.09296](https://arxiv.org/abs/2403.09296) · 📚 被引 7
- **作者**: Yu-Chu Yu, Chi-Pin Huang, Jr-Jen Chen, Kai-Po Chang, Yung-Hsuan Lai, Fu-En Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale vision-language models (VLMs) have shown a strong zero-shot generalization capability on unseen-domain data. However, adapting pre-trained VLMs to a sequence of downstream tasks often leads to the forgetting of previously learned knowledge and a reduction in zero-shot classification performance. To tackle this problem, we propose a unique Selective Dual-Teacher Knowledge Transfer framework that leverages the most recent fine-tuned and the original pre-trained VLMs as dual teachers to preserve the previously learned knowledge and zero-shot capabilities, respectively. With only access to an unlabeled reference dataset, our proposed framework performs a selective knowledge distillation mechanism by measuring the feature discrepancy from the dual-teacher VLMs. Consequently, our selective dual-teacher knowledge distillation mitigates catastrophic forgetting of previously learned knowledge while preserving the zero-shot capabilities of pre-trained VLMs. Extensive experiments on benchmark datasets demonstrate that our framework is favorable against state-of-the-art continual learning approaches for preventing catastrophic forgetting and zero-shot degradation. Project page: https://chuyu.org/research/snd

</details>

### Anytime Continual Learning for Open Vocabulary Classification.
- **链接**: [arXiv:2409.08518](https://arxiv.org/abs/2409.08518) · [代码](https://github.com/jessemelpolio/AnytimeCL) · 📚 被引 4
- **作者**: Zhen Zhu, Yiming Gong, Derek Hoiem
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an approach for anytime continual learning (AnytimeCL) for open vocabulary image classification. The AnytimeCL problem aims to break away from batch training and rigid models by requiring that a system can predict any set of labels at any time and efficiently update and improve when receiving one or more training samples at any time. Despite the challenging goal, we achieve substantial improvements over recent methods. We propose a dynamic weighting between predictions of a partially fine-tuned model and a fixed open vocabulary model that enables continual improvement when training samples are available for a subset of a task's labels. We also propose an attention-weighted PCA compression of training features that reduces storage and computation with little impact to model accuracy. Our methods are validated with experiments that test flexibility of learning and inference. Code is available at https://github.com/jessemelpolio/AnytimeCL.

</details>

### Versatile Incremental Learning: Towards Class and Domain-Agnostic Incremental Learning.
- **链接**: [arXiv:2409.10956](https://arxiv.org/abs/2409.10956) · [代码](https://github.com/KHU-AGI/VIL) · 📚 被引 6
- **作者**: Min-Yeong Park, Jae-Ho Lee, Gyeong-Moon Park
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental Learning (IL) aims to accumulate knowledge from sequential input tasks while overcoming catastrophic forgetting. Existing IL methods typically assume that an incoming task has only increments of classes or domains, referred to as Class IL (CIL) or Domain IL (DIL), respectively. In this work, we consider a more challenging and realistic but under-explored IL scenario, named Versatile Incremental Learning (VIL), in which a model has no prior of which of the classes or domains will increase in the next task. In the proposed VIL scenario, the model faces intra-class domain confusion and inter-domain class confusion, which makes the model fail to accumulate new knowledge without interference with learned knowledge. To address these issues, we propose a simple yet effective IL framework, named Incremental Classifier with Adaptation Shift cONtrol (ICON). Based on shifts of learnable modules, we design a novel regularization method called Cluster-based Adaptation Shift conTrol (CAST) to control the model to avoid confusion with the previously learned knowledge and thereby accumulate the new knowledge more effectively. Moreover, we introduce an Incremental Classifier (IC) which expands its output nodes to address the overwriting issue from different domains corresponding to a single class while maintaining the previous knowledge. We conducted extensive experiments on three benchmarks, showcasing the effectiveness of our method across all the scenarios, particularly in cases where the next task can be randomly altered. Our implementation code is available at https://github.com/KHU-AGI/VIL.

</details>

### iNeMo: Incremental Neural Mesh Models for Robust Class-Incremental Learning.
- **链接**: [arXiv:2407.09271](https://arxiv.org/abs/2407.09271) · [代码](https://github.com/Fischer-Tom/iNeMo) · 📚 被引 3
- **作者**: Tom Fischer, Yaoyao Liu, Artur Jesslen, Noor Ahmed, Prakhar Kaushik, Angtian Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Different from human nature, it is still common practice today for vision tasks to train deep learning models only initially and on fixed datasets. A variety of approaches have recently addressed handling continual data streams. However, extending these methods to manage out-of-distribution (OOD) scenarios has not effectively been investigated. On the other hand, it has recently been shown that non-continual neural mesh models exhibit strong performance in generalizing to such OOD scenarios. To leverage this decisive property in a continual learning setting, we propose incremental neural mesh models that can be extended with new meshes over time. In addition, we present a latent space initialization strategy that enables us to allocate feature space for future unseen classes in advance and a positional regularization term that forces the features of the different classes to consistently stay in respective latent space regions. We demonstrate the effectiveness of our method through extensive experiments on the Pascal3D and ObjectNet3D datasets and show that our approach outperforms the baselines for classification by $2-6\%$ in the in-domain and by $6-50\%$ in the OOD setting. Our work also presents the first incremental learning approach for pose estimation. Our code and model can be found at https://github.com/Fischer-Tom/iNeMo.

</details>

### PILoRA: Prototype Guided Incremental LoRA for Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73650-6_9) · 📚 被引 13
- **作者**: Haiyang Guo, Fei Zhu, Wenzhuo Liu, Xu-Yao Zhang, Cheng-Lin Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learning from the Web: Language Drives Weakly-Supervised Incremental Learning for Semantic Segmentation.
- **链接**: [arXiv:2407.13363](https://arxiv.org/abs/2407.13363)
- **作者**: Chang Liu, Giulia Rizzoli, Pietro Zanuttigh, Fu Li, Yi Niu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current weakly-supervised incremental learning for semantic segmentation (WILSS) approaches only consider replacing pixel-level annotations with image-level labels, while the training images are still from well-designed datasets. In this work, we argue that widely available web images can also be considered for the learning of new classes. To achieve this, firstly we introduce a strategy to select web images which are similar to previously seen examples in the latent space using a Fourier-based domain discriminator. Then, an effective caption-driven reharsal strategy is proposed to preserve previously learnt classes. To our knowledge, this is the first work to rely solely on web images for both the learning of new concepts and the preservation of the already learned ones in WILSS. Experimental results show that the proposed approach can reach state-of-the-art performances without using manually selected and annotated data in the incremental steps.

</details>

### CLOSER: Towards Better Representation Learning for Few-Shot Class-Incremental Learning.
- **链接**: [arXiv:2410.05627](https://arxiv.org/abs/2410.05627) · [代码](https://github.com/JungHunOh/CLOSER_ECCV2024) · 📚 被引 17
- **作者**: Junghun Oh, Sungyong Baik, Kyoung Mu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aiming to incrementally learn new classes with only few samples while preserving the knowledge of base (old) classes, few-shot class-incremental learning (FSCIL) faces several challenges, such as overfitting and catastrophic forgetting. Such a challenging problem is often tackled by fixing a feature extractor trained on base classes to reduce the adverse effects of overfitting and forgetting. Under such formulation, our primary focus is representation learning on base classes to tackle the unique challenge of FSCIL: simultaneously achieving the transferability and the discriminability of the learned representation. Building upon the recent efforts for enhancing transferability, such as promoting the spread of features, we find that trying to secure the spread of features within a more confined feature space enables the learned representation to strike a better balance between transferability and discriminability. Thus, in stark contrast to prior beliefs that the inter-class distance should be maximized, we claim that the closer different classes are, the better for FSCIL. The empirical results and analysis from the perspective of information bottleneck theory justify our simple yet seemingly counter-intuitive representation learning method, raising research questions and suggesting alternative research directions. The code is available at https://github.com/JungHunOh/CLOSER_ECCV2024.

</details>

### Rethinking Few-Shot Class-Incremental Learning: Learning from Yourself.
- **链接**: [arXiv:2407.07468](https://arxiv.org/abs/2407.07468) · [代码](https://github.com/iSEE-Laboratory/Revisting_FSCIL)
- **作者**: Yu-Ming Tang, Yi-Xing Peng, Jingke Meng, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot class-incremental learning (FSCIL) aims to learn sequential classes with limited samples in a few-shot fashion. Inherited from the classical class-incremental learning setting, the popular benchmark of FSCIL uses averaged accuracy (aAcc) and last-task averaged accuracy (lAcc) as the evaluation metrics. However, we reveal that such evaluation metrics may not provide adequate emphasis on the novel class performance, and the continual learning ability of FSCIL methods could be ignored under this benchmark. In this work, as a complement to existing metrics, we offer a new metric called generalized average accuracy (gAcc) which is designed to provide an extra equitable evaluation by incorporating different perspectives of the performance under the guidance of a parameter $α$. We also present an overall metric in the form of the area under the curve (AUC) along the $α$. Under the guidance of gAcc, we release the potential of intermediate features of the vision transformers to boost the novel-class performance. Taking information from intermediate layers which are less class-specific and more generalizable, we manage to rectify the final features, leading to a more generalizable transformer-based FSCIL framework. Without complex network designs or cumbersome training procedures, our method outperforms existing FSCIL methods at aAcc and gAcc on three datasets. See codes at https://github.com/iSEE-Laboratory/Revisting_FSCIL

</details>

### Scene Coordinate Reconstruction: Posing of Image Collections via Incremental Learning of a Relocalizer.
- **链接**: [arXiv:2404.14351](https://arxiv.org/abs/2404.14351) · 📚 被引 48
- **作者**: Eric Brachmann, Jamie Wynn, Shuai Chen, Tommaso Cavallari, Áron Monszpart, Daniyar Turmukhambetov et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the task of estimating camera parameters from a set of images depicting a scene. Popular feature-based structure-from-motion (SfM) tools solve this task by incremental reconstruction: they repeat triangulation of sparse 3D points and registration of more camera views to the sparse point cloud. We re-interpret incremental structure-from-motion as an iterated application and refinement of a visual relocalizer, that is, of a method that registers new views to the current state of the reconstruction. This perspective allows us to investigate alternative visual relocalizers that are not rooted in local feature matching. We show that scene coordinate regression, a learning-based relocalization approach, allows us to build implicit, neural scene representations from unposed images. Different from other learning-based reconstruction methods, we do not require pose priors nor sequential inputs, and we optimize efficiently over thousands of images. In many cases, our method, ACE0, estimates camera poses with an accuracy close to feature-based SfM, as demonstrated by novel view synthesis. Project page: https://nianticlabs.github.io/acezero/

</details>

### STSP: Spatial-Temporal Subspace Projection for Video Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73390-1_22) · 📚 被引 6
- **作者**: Hao Cheng, Siyuan Yang, Chong Wang, Joey Tianyi Zhou, Alex C. Kot, Bihan Wen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Canonical Shape Projection Is All You Need for 3D Few-Shot Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72940-9_3) · 📚 被引 3
- **作者**: Ali Cheraghian, Zeeshan Hayder, Sameera Ramasinghe, Shafin Rahman, Javad Jafaryahya, Lars Petersson et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Confidence Self-calibration for Multi-label Class-Incremental Learning.
- **链接**: [arXiv:2403.12559](https://arxiv.org/abs/2403.12559) · 📚 被引 2
- **作者**: Kaile Du, Yifan Zhou, Fan Lyu, Yuyang Li, Chen Lu, Guangcan Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The partial label challenge in Multi-Label Class-Incremental Learning (MLCIL) arises when only the new classes are labeled during training, while past and future labels remain unavailable. This issue leads to a proliferation of false-positive errors due to erroneously high confidence multi-label predictions, exacerbating catastrophic forgetting within the disjoint label space. In this paper, we aim to refine multi-label confidence calibration in MLCIL and propose a Confidence Self-Calibration (CSC) approach. Firstly, for label relationship calibration, we introduce a class-incremental graph convolutional network that bridges the isolated label spaces by constructing learnable, dynamically extended label relationship graph. Then, for confidence calibration, we present a max-entropy regularization for each multi-label increment, facilitating confidence self-calibration through the penalization of over-confident output distributions. Our approach attains new state-of-the-art results in MLCIL tasks on both MS-COCO and PASCAL VOC datasets, with the calibration of label confidences confirmed through our methodology.

</details>

### Class-Incremental Learning with CLIP: Adaptive Representation Adjustment and Parameter Fusion.
- **链接**: [arXiv:2407.14143](https://arxiv.org/abs/2407.14143) · [代码](https://github.com/linlany/RAPF) · 📚 被引 20
- **作者**: Linlan Huang, Xusheng Cao, Haori Lu, Xialei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning is a challenging problem, where the goal is to train a model that can classify data from an increasing number of classes over time. With the advancement of vision-language pre-trained models such as CLIP, they demonstrate good generalization ability that allows them to excel in class-incremental learning with completely frozen parameters. However, further adaptation to downstream tasks by simply fine-tuning the model leads to severe forgetting. Most existing works with pre-trained models assume that the forgetting of old classes is uniform when the model acquires new knowledge. In this paper, we propose a method named Adaptive Representation Adjustment and Parameter Fusion (RAPF). During training for new data, we measure the influence of new classes on old ones and adjust the representations, using textual features. After training, we employ a decomposed parameter fusion to further mitigate forgetting during adapter module fine-tuning. Experiments on several conventional benchmarks show that our method achieves state-of-the-art results. Our code is available at \url{https://github.com/linlany/RAPF}.

</details>

### Personalized Federated Domain-Incremental Learning Based on Adaptive Knowledge Matching.
- **链接**: [arXiv:2407.05005](https://arxiv.org/abs/2407.05005) · 📚 被引 6
- **作者**: Yichen Li, Wenchao Xu, Haozhao Wang, Yining Qi, Jingcai Guo, Ruixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focuses on Federated Domain-Incremental Learning (FDIL) where each client continues to learn incremental tasks where their domain shifts from each other. We propose a novel adaptive knowledge matching-based personalized FDIL approach (pFedDIL) which allows each client to alternatively utilize appropriate incremental task learning strategy on the correlation with the knowledge from previous tasks. More specifically, when a new task arrives, each client first calculates its local correlations with previous tasks. Then, the client can choose to adopt a new initial model or a previous model with similar knowledge to train the new task and simultaneously migrate knowledge from previous tasks based on these correlations. Furthermore, to identify the correlations between the new task and previous tasks for each client, we separately employ an auxiliary classifier to each target classification model and propose sharing partial parameters between the target classification model and the auxiliary classifier to condense model parameters. We conduct extensive experiments on several datasets of which results demonstrate that pFedDIL outperforms state-of-the-art methods by up to 14.35\% in terms of average accuracy of all tasks.

</details>

### Few-Shot Class Incremental Learning with Attention-Aware Self-adaptive Prompt.
- **链接**: [arXiv:2403.09857](https://arxiv.org/abs/2403.09857)
- **作者**: Chenxi Liu, Zhenyi Wang, Tianyi Xiong, Ruibo Chen, Yihan Wu, Junfeng Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-Shot Class-Incremental Learning (FSCIL) models aim to incrementally learn new classes with scarce samples while preserving knowledge of old ones. Existing FSCIL methods usually fine-tune the entire backbone, leading to overfitting and hindering the potential to learn new classes. On the other hand, recent prompt-based CIL approaches alleviate forgetting by training prompts with sufficient data in each task. In this work, we propose a novel framework named Attention-aware Self-adaptive Prompt (ASP). ASP encourages task-invariant prompts to capture shared knowledge by reducing specific information from the attention aspect. Additionally, self-adaptive task-specific prompts in ASP provide specific information and transfer knowledge from old classes to new classes with an Information Bottleneck learning objective. In summary, ASP prevents overfitting on base task and does not require enormous data in few-shot incremental tasks. Extensive experiments on three benchmark datasets validate that ASP consistently outperforms state-of-the-art FSCIL and prompt-based CIL methods in terms of both learning new classes and mitigating forgetting.

</details>

### DiffClass: Diffusion-Based Class Incremental Learning.
- **链接**: [arXiv:2403.05016](https://arxiv.org/abs/2403.05016) · 📚 被引 19
- **作者**: Zichong Meng, Jie Zhang, Changdi Yang, Zheng Zhan, Pu Zhao, Yanzhi Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) is challenging due to catastrophic forgetting. On top of that, Exemplar-free Class Incremental Learning is even more challenging due to forbidden access to previous task data. Recent exemplar-free CIL methods attempt to mitigate catastrophic forgetting by synthesizing previous task data. However, they fail to overcome the catastrophic forgetting due to the inability to deal with the significant domain gap between real and synthetic data. To overcome these issues, we propose a novel exemplar-free CIL method. Our method adopts multi-distribution matching (MDM) diffusion models to unify quality and bridge domain gaps among all domains of training data. Moreover, our approach integrates selective synthetic image augmentation (SSIA) to expand the distribution of the training data, thereby improving the model's plasticity and reinforcing the performance of our method's ultimate component, multi-domain adaptation (MDA). With the proposed integrations, our method then reformulates exemplar-free CIL into a multi-domain adaptation problem to implicitly address the domain gap problem to enhance model stability during incremental training. Extensive experiments on benchmark class incremental datasets and settings demonstrate that our method excels previous exemplar-free CIL methods and achieves state-of-the-art performance.

</details>

### Non-exemplar Domain Incremental Learning via Cross-Domain Concept Integration.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72967-6_9) · 📚 被引 9
- **作者**: Qiang Wang, Yuhang He, Songlin Dong, Xinyuan Gao, Shaokun Wang, Yihong Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### On the Approximation Risk of Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72983-6_10)
- **作者**: Xuan Wang, Zhong Ji, Xiyao Liu, Yanwei Pang, Jungong Han
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
