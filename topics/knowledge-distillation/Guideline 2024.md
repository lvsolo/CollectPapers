# Knowledge Distillation — 2024 Guideline

> 领域: 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Distill Gold from Massive Ores: Bi-level Data Pruning Towards Efficient Dataset Distillation. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72661-3_14) · 📚 被引 6
- **作者**: Yue Xu, Yong-Lu Li, Kaitong Cui, Ziyu Wang, Cewu Lu, Yu-Wing Tai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 该论文针对数据集蒸馏中数据冗余和效率低下的问题，提出了一种双层数据剪枝方法，旨在从大规模数据中提取关键样本以优化蒸馏过程。方法通过粗粒度筛选和细粒度选择两个阶段，减少数据冗余并提升蒸馏效率。实验表明该方法在多个数据集上显著降低了计算成本，同时保持了蒸馏性能。
- **摘要（英）**: This paper tackles data redundancy in dataset distillation by proposing a bi-level data pruning method that selects critical samples from large-scale data. The approach combines coarse and fine-grained selection to improve efficiency, achieving reduced computational cost while maintaining distillation performance on multiple benchmarks.
- **核心贡献**: 提出双层数据剪枝策略，提升数据集蒸馏效率。
- **创新点**: 将数据剪枝与蒸馏结合，实现高效样本选择。
- **结果**: 在多个数据集上降低计算成本并保持性能。

### Multi-modal Relation Distillation for Unified 3D Representation Learning. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2407.14007](https://arxiv.org/abs/2407.14007)
- **作者**: Huiqun Wang, Yiping Bao, Panwang Pan, Zeming Li, Xiao Liu, Ruijie Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对多模态预训练中忽略样本间结构关系的问题，提出了多模态关系蒸馏（MRD）框架，用于统一3D表示学习。该方法通过蒸馏大型视觉-语言模型到3D骨干网络，捕获模态内和跨模态关系，生成更具判别性的3D形状表示。在零样本分类和跨模态检索任务上取得了新的最先进性能。
- **摘要（英）**: This paper introduces Multi-modal Relation Distillation (MRD) to capture intra- and cross-modal relations in 3D pre-training, distilling knowledge from vision-language models into 3D backbones. It produces more discriminative 3D representations and achieves state-of-the-art performance on zero-shot classification and cross-modal retrieval.
- **核心贡献**: 提出MRD框架，通过关系蒸馏提升3D表示学习。
- **创新点**: 显式建模模态内和跨模态关系，超越简单特征对齐。
- **结果**: 在零样本分类和检索任务上达到SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in multi-modal pre-training for 3D point clouds have demonstrated promising results by aligning heterogeneous features across 3D shapes and their corresponding 2D images and language descriptions. However, current straightforward solutions often overlook intricate structural relations among samples, potentially limiting the full capabilities of multi-modal learning. To address this issue, we introduce Multi-modal Relation Distillation (MRD), a tri-modal pre-training framework, which is designed to effectively distill reputable large Vision-Language Models (VLM) into 3D backbones. MRD aims to capture both intra-relations within each modality as well as cross-relations between different modalities and produce more discriminative 3D shape representations. Notably, MRD achieves significant improvements in downstream zero-shot classification tasks and cross-modality retrieval tasks, delivering new state-of-the-art performance.

</details>

### Open Vocabulary 3D Scene Understanding via Geometry Guided Self-Distillation. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2407.13362](https://arxiv.org/abs/2407.13362) · 📚 被引 5
- **作者**: Pengfei Wang, Yuxi Wang, Shuai Li, Zhaoxiang Zhang, Zhen Lei, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024
- **摘要（中）**: 针对开放词汇3D场景理解中3D文本配对数据稀缺的问题，提出了几何引导自蒸馏（GGSD）方法。该方法通过几何引导蒸馏模块从2D预训练模型迁移知识，并利用3D几何先验减少2D模型的噪声，增强表示学习。由于3D表示的优势，蒸馏后的3D学生模型性能显著超越2D教师模型，并通过自蒸馏进一步提升。
- **摘要（英）**: This paper proposes Geometry Guided Self-Distillation (GGSD) for open vocabulary 3D scene understanding, distilling knowledge from 2D models while leveraging 3D geometric priors to reduce noise. The 3D student model surpasses the 2D teacher, and self-distillation further boosts performance.
- **核心贡献**: 提出GGSD，结合几何引导蒸馏和自蒸馏，提升开放词汇3D理解。
- **创新点**: 利用3D几何先验增强蒸馏过程，实现学生超越教师。
- **结果**: 3D学生模型性能显著优于2D教师。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The scarcity of large-scale 3D-text paired data poses a great challenge on open vocabulary 3D scene understanding, and hence it is popular to leverage internet-scale 2D data and transfer their open vocabulary capabilities to 3D models through knowledge distillation. However, the existing distillation-based 3D scene understanding approaches rely on the representation capacity of 2D models, disregarding the exploration of geometric priors and inherent representational advantages offered by 3D data. In this paper, we propose an effective approach, namely Geometry Guided Self-Distillation (GGSD), to learn superior 3D representations from 2D pre-trained models. Specifically, we first design a geometry guided distillation module to distill knowledge from 2D models, and then leverage the 3D geometric priors to alleviate the inherent noise in 2D models and enhance the representation learning process. Due to the advantages of 3D representation, the performance of the distilled 3D student model can significantly surpass that of the 2D teacher model. This motivates us to further leverage the representation advantages of 3D data through self-distillation. As a result, our proposed GGSD approach outperforms the existing open vocabulary 3D scene understanding methods by a large margin, as demonstrated by our experiments on both indoor and outdoor benchmark datasets.

</details>

### SOHES: Self-supervised Open-world Hierarchical Entity Segmentation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2404.12386](https://arxiv.org/abs/2404.12386)
- **作者**: Shengcao Cao, Jiuxiang Gu, Jason Kuen, Hao Tan, Ruiyi Zhang, Handong Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: 针对开放世界实体分割依赖昂贵人工标注的问题，提出了自监督开放世界层次实体分割（SOHES）方法。该方法通过自探索、自指导和自纠正三个阶段，利用预训练自监督表示生成伪标签，并通过师生互学习纠正噪声，实现无需人工标注的实体和部件分割。在自监督开放世界分割任务上取得了前所未有的性能。
- **摘要（英）**: This paper presents SOHES, a self-supervised approach for open-world hierarchical entity segmentation that eliminates human annotations. It uses self-exploration, self-instruction, and self-correction phases with pseudo-labels and teacher-student mutual learning, achieving unprecedented performance.
- **核心贡献**: 提出SOHES，实现无需标注的开放世界层次实体分割。
- **创新点**: 三阶段自监督流程结合师生互学习，有效处理伪标签噪声。
- **结果**: 在自监督开放世界分割上达到最优性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-world entity segmentation, as an emerging computer vision task, aims at segmenting entities in images without being restricted by pre-defined classes, offering impressive generalization capabilities on unseen images and concepts. Despite its promise, existing entity segmentation methods like Segment Anything Model (SAM) rely heavily on costly expert annotators. This work presents Self-supervised Open-world Hierarchical Entity Segmentation (SOHES), a novel approach that eliminates the need for human annotations. SOHES operates in three phases: self-exploration, self-instruction, and self-correction. Given a pre-trained self-supervised representation, we produce abundant high-quality pseudo-labels through visual feature clustering. Then, we train a segmentation model on the pseudo-labels, and rectify the noises in pseudo-labels via a teacher-student mutual-learning procedure. Beyond segmenting entities, SOHES also captures their constituent parts, providing a hierarchical understanding of visual entities. Using raw images as the sole training data, our method achieves unprecedented performance in self-supervised open-world segmentation, marking a significant milestone towards high-quality open-world entity segmentation in the absence of human-annotated masks. Project page: https://SOHES-ICLR.github.io.

</details>

### A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openreview.net/forum?id=Ixi4j6LtdX)
- **作者**: Ayan Sengupta, Shantanu Dixit, Md. Shad Akhtar, Tanmoy Chakraborty
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: 该论文探讨了教师-学生协作知识蒸馏中教师质量的影响，提出了一种改进的协作蒸馏框架。方法强调优秀学习者能更好地指导教学，通过动态调整师生交互提升蒸馏效果。但摘要内容不完整，缺乏具体实验数据和详细方法描述。
- **摘要（英）**: This paper discusses teacher-student collaborative knowledge distillation, emphasizing that better learners can teach more effectively. It proposes a framework with dynamic teacher-student interaction, but the abstract lacks experimental details.
- **核心贡献**: 提出改进的教师-学生协作蒸馏框架。
- **创新点**: 强调教师质量对蒸馏效果的影响。
- **结果**: 未提供具体数据。

### Hybrid Distillation: Connecting Masked Autoencoders with Contrastive Learners. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2306.15876](https://arxiv.org/abs/2306.15876)
- **作者**: Bowen Shi, Xiaopeng Zhang, Yaoming Wang, Jin Li, Wenrui Dai, Junni Zou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: ①该论文针对自监督表示学习中对比学习（CL）和掩码图像建模（MIM）两种范式各有优劣的问题，即CL擅长捕获全局模式并提升特征判别性，而MIM能引入更多局部和多样化的注意力，但现有方法难以同时获得两者的优势。②作者提出了一种简单有效的混合蒸馏策略（Hybrid Distillation），利用监督/对比学习教师模型和MIM教师模型共同指导学生模型，其中学生模型模仿MIM教师的token关系以缓解注意力坍塌，并蒸馏监督/CL教师的特征图以增强判别能力。③相比先前特征蒸馏和掩码特征重建方法，该方法避免了因不对称设计导致的判别性下降，同时有效结合了两种范式的优点。④实验表明，该方法在多个下游任务上取得了优于单一范式或简单组合方法的性能，具体数据未在摘要中给出，但验证了其有效性。
- **摘要（英）**: This paper addresses the challenge of combining the strengths of contrastive learning (CL) and masked image modeling (MIM) in self-supervised representation learning, where CL excels at global pattern capture and discrimination while MIM promotes local and diverse attention. The authors propose a Hybrid Distillation strategy that uses both a supervised/CL teacher and an MIM teacher to jointly guide a student model, imitating token relations from the MIM teacher to prevent attention collapse and distilling feature maps from the supervised/CL teacher for discriminability. This approach outperforms prior feature distillation and mask reconstruction methods by avoiding discrimination loss from asymmetric designs, achieving superior performance on downstream tasks.
- **核心贡献**: 提出混合蒸馏策略，通过双教师联合指导实现判别性和多样性的统一。
- **创新点**: 创新性地结合MIM教师的token关系蒸馏和CL教师的特征图蒸馏，避免注意力坍塌同时增强判别力。
- **结果**: 在多个下游任务上验证了优于单一范式或简单组合方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Representation learning has been evolving from traditional supervised training to Contrastive Learning (CL) and Masked Image Modeling (MIM). Previous works have demonstrated their pros and cons in specific scenarios, i.e., CL and supervised pre-training excel at capturing longer-range global patterns and enabling better feature discrimination, while MIM can introduce more local and diverse attention across all transformer layers. In this paper, we explore how to obtain a model that combines their strengths. We start by examining previous feature distillation and mask feature reconstruction methods and identify their limitations. We find that their increasing diversity mainly derives from the asymmetric designs, but these designs may in turn compromise the discrimination ability. In order to better obtain both discrimination and diversity, we propose a simple but effective Hybrid Distillation strategy, which utilizes both the supervised/CL teacher and the MIM teacher to jointly guide the student model. Hybrid Distill imitates the token relations of the MIM teacher to alleviate attention collapse, as well as distills the feature maps of the supervised/CL teacher to enable discrimination. Furthermore, a progressive redundant token masking strategy is also utilized to reduce the distilling costs and avoid falling into local optima. Experiment results prove that Hybrid Distill can achieve superior performance on different benchmarks.

</details>

## 跨领域论文（完整笔记在其他领域）

- MVIP-NeRF: Multi-View 3D Inpainting on NeRF Scenes via Diffusion Prior. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- On the Road to Portability: Compressing End-to-End Motion Planner for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Select and Distill: Selective Dual-Teacher Knowledge Transfer for Continual Learning on Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)

<!-- COMPLETE v1 papers=6 -->
