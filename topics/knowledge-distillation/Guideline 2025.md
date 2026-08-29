# Knowledge Distillation — 2025 Guideline

> 领域: 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### What to Distill? Fast Knowledge Distillation with Adaptive Sampling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00232) · 📚 被引 0
- **作者**: Byungchul Chae, Seonyeong Heo
- **🏷️ 机构**: Kyung Hee University; SqueezeBits Inc., Kyung Hee University
- **会议**: ICCV 2025

## 🆕 增量新增

### Multi-modal Knowledge Distillation-based Human Trajectory Forecasting. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2503.22201](https://arxiv.org/abs/2503.22201) · 📚 被引 10
- **作者**: Jaewoo Jeong, Seohee Lee, Daehee Park, Giwon Lee, Kuk-Jin Yoon
- **🏷️ 机构**: Visual Intelligence Lab., KAIST,Korea, Intelligent Systems and Learning Lab., DGIST,Korea
- **会议**: CVPR 2025
- **摘要（中）**: 针对行人轨迹预测中在线提取文本模态需依赖VLM、资源受限系统难以部署的问题，提出多模态知识蒸馏框架：教师模型使用轨迹、人体姿态和文本全模态训练，学生模型仅用轨迹或姿态作为补充模态，分别蒸馏智能体内部多模态和智能体间交互知识。在JRDB、SIT和ETH/UCY数据集上验证了框架的泛化性。相比已有工作，该方法有效降低了推理时的模态需求，同时保持了预测精度。
- **摘要（英）**: To address the challenge of online text extraction requiring VLM in trajectory forecasting, this paper proposes a multi-modal knowledge distillation framework where a teacher trained with trajectory, pose, and text distills knowledge into a student using only trajectory or pose. It separately distills intra-agent and inter-agent knowledge, validated on JRDB, SIT, and ETH/UCY datasets, reducing modality requirements while maintaining accuracy.
- **核心贡献**: 提出了一种多模态知识蒸馏框架，使轨迹预测模型在无需VLM的情况下利用文本知识。
- **创新点**: 将多模态知识蒸馏应用于轨迹预测，并分离智能体内外知识蒸馏。
- **结果**: 在多个数据集上验证了学生模型在减少模态下的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pedestrian trajectory forecasting is crucial in various applications such as autonomous driving and mobile robot navigation. In such applications, camera-based perception enables the extraction of additional modalities (human pose, text) to enhance prediction accuracy. Indeed, we find that textual descriptions play a crucial role in integrating additional modalities into a unified understanding. However, online extraction of text requires the use of VLM, which may not be feasible for resource-constrained systems. To address this challenge, we propose a multi-modal knowledge distillation framework: a student model with limited modality is distilled from a teacher model trained with full range of modalities. The comprehensive knowledge of a teacher model trained with trajectory, human pose, and text is distilled into a student model using only trajectory or human pose as a sole supplement. In doing so, we separately distill the core locomotion insights from intra-agent multi-modality and inter-agent interaction. Our generalizable framework is validated with two state-of-the-art models across three datasets on both ego-view (JRDB, SIT) and BEV-view (ETH/UCY) setups, utilizing both annotated and VLM-generated text captions. Distilled student models show consistent improvement in all prediction metrics for both full and instantaneous observations, improving up to ~13%. The code is available at https://github.com/Jaewoo97/KDTF.

</details>

### Boost Self-Supervised Dataset Distillation via Parameterization, Predefined Augmentation, and Approximation. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2507.21455](https://arxiv.org/abs/2507.21455)
- **作者**: Sheng-Feng Yu, Jia-Jiun Yao, Wei-Chen Chiu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对大规模数据集训练成本高昂的问题，探索自监督数据集蒸馏（Self-Supervised Dataset Distillation）以生成紧凑且具有跨架构泛化能力的蒸馏集。②提出了三种新技术：基于低维基底的图像和表示参数化、预定义增强策略、以及近似方法，以更忠实紧凑地保留原始数据集的关键特征。③与现有聚焦监督数据集蒸馏的工作不同，该方法同时蒸馏图像和自监督训练表示，增强跨架构泛化性。④摘要未提供具体性能数据，但声称蒸馏集在跨架构场景下表现更优。
- **摘要（英）**: This paper tackles the high training cost of large datasets by introducing self-supervised dataset distillation, which distills images and their self-supervised representations into a compact set with enhanced cross-architecture generalizability. It proposes novel techniques including parameterization via low-dimensional bases, predefined augmentation, and approximation to preserve key dataset characteristics. The method shows improved cross-architecture performance, though specific metrics are not given in the abstract.
- **核心贡献**: 提出了自监督数据集蒸馏的新框架，通过参数化和近似技术提升蒸馏集的紧凑性和泛化能力。
- **创新点**: 首次将数据集蒸馏与自监督表示学习结合，并引入低维基底参数化。
- **结果**: 蒸馏集在跨架构泛化性上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although larger datasets are crucial for training large deep models, the rapid growth of dataset size has brought a significant challenge in terms of considerable training costs, which even results in prohibitive computational expenses. Dataset Distillation becomes a popular technique recently to reduce the dataset size via learning a highly compact set of representative exemplars, where the model trained with these exemplars ideally should have comparable performance with respect to the one trained with the full dataset. While most of existing works upon dataset distillation focus on supervised datasets, we instead aim to distill images and their self-supervisedly trained representations into a distilled set. This procedure, named as Self-Supervised Dataset Distillation, effectively extracts rich information from real datasets, yielding the distilled sets with enhanced cross-architecture generalizability. Particularly, in order to preserve the key characteristics of original dataset more faithfully and compactly, several novel techniques are proposed: 1) we introduce an innovative parameterization upon images and representations via distinct low-dimensional bases, where the base selection for parameterization is experimentally shown to play a crucial role; 2) we tackle the instability induced by the randomness of data augmentation -- a key component in self-supervised learning but being underestimated in the prior work of self-supervised dataset distillation -- by utilizing predetermined augmentations; 3) we further leverage a lightweight network to model the connections among the representations of augmented views from the same image, leading to more compact pairs of distillation. Extensive experiments conducted on various datasets validate the superiority of our approach in terms of distillation efficiency, cross-architecture generalization, and transfer learning performance.

</details>

### Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2410.11325](https://arxiv.org/abs/2410.11325)
- **作者**: Wenda Xu, Rujun Han, Zifeng Wang, Long T. Le, Dhruv Madeka, Lei Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对知识蒸馏中教师-学生知识差距导致监督KD分布不匹配和on-policy KD低质量训练样本的问题。②提出了推测性知识蒸馏（SKD），通过学生和教师模型的协作生成高质量训练数据：学生提出token，教师根据自身分布替换排名不佳的token，从而自适应传递知识。③相比监督KD和on-policy KD，SKD同时对齐学生推理分布并利用教师知识，避免低质量反馈。④在翻译、摘要、数学和指令跟随等文本生成任务上进行了评估，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the teacher-student knowledge gap in knowledge distillation, where supervised KD suffers from distribution mismatch and on-policy KD from low-quality samples. It proposes Speculative Knowledge Distillation (SKD), where the student proposes tokens and the teacher replaces poorly ranked ones, enabling adaptive knowledge transfer aligned with the student's inference distribution. SKD is evaluated on text generation tasks including translation, summarization, math, and instruction following, though specific results are not detailed.
- **核心贡献**: 提出了推测性知识蒸馏方法，通过学生提议和教师替换token实现高质量训练数据生成。
- **创新点**: 利用学生和教师的协作采样机制，同时保证训练数据质量和分布对齐。
- **结果**: 在多个文本生成任务上验证了有效性，但具体数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in knowledge distillation (KD) have enabled smaller student models to approach the performance of larger teacher models. However, popular methods such as supervised KD and on-policy KD, are adversely impacted by the knowledge gaps between teacher-student in practical scenarios. Supervised KD suffers from a distribution mismatch between training with a static dataset and inference over final student-generated outputs. Conversely, on-policy KD, which uses student-generated samples for training, can suffer from low-quality training examples with which teacher models are not familiar, resulting in inaccurate teacher feedback. To address these limitations, we introduce Speculative Knowledge Distillation (SKD), a novel approach that leverages cooperation between student and teacher models to generate high-quality training data on-the-fly while aligning with the student's inference-time distribution. In SKD, the student proposes tokens, and the teacher replaces poorly ranked ones based on its own distribution, transferring high-quality knowledge adaptively. We evaluate SKD on various text generation tasks, including translation, summarization, math, and instruction following, and show that SKD consistently outperforms existing KD methods across different domains, data sizes, and model initialization strategies.

</details>

## 跨领域论文（完整笔记在其他领域）

- UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning. → [object-detection](../object-detection/Guideline%202025.md)
- HiLoTs: High-Low Temporal Sensitive Representation Learning for Semi-Supervised LiDAR Segmentation in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- VoCo-LLaMA: Towards Vision Compression with Large Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
<!-- COMPLETE v1 papers=4 -->
