# Open-set Detection — 2022 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-Vocabulary One-Stage Detection with Hierarchical Visual-Language Knowledge Distillation.
- **链接**: [arXiv:2203.10593](https://arxiv.org/abs/2203.10593) · 📚 被引 39
- **作者**: Zongyang Ma, Guan Luo, Jin Gao, Liang Li, Yuxin Chen, Shaoru Wang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,NLPR, Beijing Institute of Basic Medical Sciences,Brain Science Center, Nanchana Hangkong University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection aims to detect novel object categories beyond the training set. The advanced open-vocabulary two-stage detectors employ instance-level visual-to-visual knowledge distillation to align the visual space of the detector with the semantic space of the Pre-trained Visual-Language Model (PVLM). However, in the more efficient one-stage detector, the absence of class-agnostic object proposals hinders the knowledge distillation on unseen objects, leading to severe performance degradation. In this paper, we propose a hierarchical visual-language knowledge distillation method, i.e., HierKD, for open-vocabulary one-stage detection. Specifically, a global-level knowledge distillation is explored to transfer the knowledge of unseen categories from the PVLM to the detector. Moreover, we combine the proposed global-level knowledge distillation and the common instance-level knowledge distillation to learn the knowledge of seen and unseen categories simultaneously. Extensive experiments on MS-COCO show that our method significantly surpasses the previous best one-stage detector with 11.9\% and 6.7\% $AP_{50}$ gains under the zero-shot detection and generalized zero-shot detection settings, and reduces the $AP_{50}$ performance gap from 14\% to 7.3\% compared to the best two-stage detector.

</details>

## 跨领域论文（完整笔记在其他领域）

- Unknown-Aware Object Detection: Learning What You Don't Know from Videos in the Wild. → [object-detection](../object-detection/Guideline%202022.md)
- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [object-detection](../object-detection/Guideline%202022.md)
- Expanding Low-Density Latent Regions for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
