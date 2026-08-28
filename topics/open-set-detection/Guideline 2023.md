# Open-set Detection — 2023 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Compositional Prompt Tuning with Motion Cues for Open-vocabulary Video Relation Detection.
- **链接**: [arXiv:2302.00268](https://arxiv.org/abs/2302.00268) · [代码](https://github.com/Dawn-LX/OpenVoc-VidVRD)
- **作者**: Kaifeng Gao, Long Chen, Hanwang Zhang, Jun Xiao, Qianru Sun
- **🏷️ 机构**: NUS
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt tuning with large-scale pretrained vision-language models empowers open-vocabulary predictions trained on limited base categories, e.g., object classification and detection. In this paper, we propose compositional prompt tuning with motion cues: an extended prompt tuning paradigm for compositional predictions of video data. In particular, we present Relation Prompt (RePro) for Open-vocabulary Video Visual Relation Detection (Open-VidVRD), where conventional prompt tuning is easily biased to certain subject-object combinations and motion patterns. To this end, RePro addresses the two technical challenges of Open-VidVRD: 1) the prompt tokens should respect the two different semantic roles of subject and object, and 2) the tuning should account for the diverse spatio-temporal motion patterns of the subject-object compositions. Without bells and whistles, our RePro achieves a new state-of-the-art performance on two VidVRD benchmarks of not only the base training object and predicate categories, but also the unseen ones. Extensive ablations also demonstrate the effectiveness of the proposed compositional and multi-mode design of prompts. Code is available at https://github.com/Dawn-LX/OpenVoc-VidVRD.

</details>

## 跨领域论文（完整笔记在其他领域）

- Learning Object-Language Alignments for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Open-Vocabulary Object Detection upon Frozen Vision and Language Models. → [object-detection](../object-detection/Guideline%202023.md)
