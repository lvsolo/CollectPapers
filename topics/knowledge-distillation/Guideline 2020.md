# Knowledge Distillation — 2020 Guideline

> 领域: 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2025](Guideline%202025.md), [2024](Guideline%202024.md), [2023](Guideline%202023.md), [2022](Guideline%202022.md), [2021](Guideline%202021.md)

### Creating Something From Nothing: Unsupervised Knowledge Distillation for Cross-Modal Hashing. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2004.00280](https://arxiv.org/abs/2004.00280) · 📚 被引 115
- **作者**: Hengtong Hu, Lingxi Xie, Richang Hong, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对跨模态哈希中监督方法需要大量标注的问题，提出利用无监督方法输出指导监督方法训练的教师-学生优化框架，实现知识蒸馏。在MIRFlickr和NUS-WIDE基准上，该方法大幅超越所有现有无监督方法。
- **摘要（英）**: This paper proposes a teacher-student optimization framework for cross-modal hashing, using unsupervised method outputs to guide supervised training. It outperforms all existing unsupervised methods by a large margin on MIRFlickr and NUS-WIDE.
- **核心贡献**: 提出无监督知识蒸馏框架，将无监督方法输出作为监督信号指导跨模态哈希训练。
- **创新点**: 利用教师-学生优化实现无监督到监督的知识迁移，减少标注依赖。
- **结果**: 在多个基准上大幅超越现有无监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, cross-modal hashing (CMH) has attracted increasing attentions, mainly because its potential ability of mapping contents from different modalities, especially in vision and language, into the same space, so that it becomes efficient in cross-modal data retrieval. There are two main frameworks for CMH, differing from each other in whether semantic supervision is required. Compared to the unsupervised methods, the supervised methods often enjoy more accurate results, but require much heavier labors in data annotation. In this paper, we propose a novel approach that enables guiding a supervised method using outputs produced by an unsupervised method. Specifically, we make use of teacher-student optimization for propagating knowledge. Experiments are performed on two popular CMH benchmarks, i.e., the MIRFlickr and NUS-WIDE datasets. Our approach outperforms all existing unsupervised methods by a large margin.

</details>
<!-- COMPLETE v1 papers=1 -->
