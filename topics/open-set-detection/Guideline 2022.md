# Open-set Detection — 2022 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-Vocabulary One-Stage Detection with Hierarchical Visual-Language Knowledge Distillation.
- **链接**: [arXiv:2203.10593](https://arxiv.org/abs/2203.10593) · 📚 被引 39
- **作者**: Zongyang Ma, Guan Luo, Jin Gao, Liang Li, Yuxin Chen, Shaoru Wang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,NLPR, Beijing Institute of Basic Medical Sciences,Brain Science Center, Nanchana Hangkong University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection aims to detect novel object categories beyond the training set. The advanced open-vocabulary two-stage detectors employ instance-level visual-to-visual knowledge distillation to align the visual space of the detector with the semantic space of the Pre-trained Visual-Language Model (PVLM). However, in the more efficient one-stage detector, the absence of class-agnostic object proposals hinders the knowledge distillation on unseen objects, leading to severe performance degradation. In this paper, we propose a hierarchical visual-language knowledge distillation method, i.e., HierKD, for open-vocabulary one-stage detection. Specifically, a global-level knowledge distillation is explored to transfer the knowledge of unseen categories from the PVLM to the detector. Moreover, we combine the proposed global-level knowledge distillation and the common instance-level knowledge distillation to learn the knowledge of seen and unseen categories simultaneously. Extensive experiments on MS-COCO show that our method significantly surpasses the previous best one-stage detector with 11.9\% and 6.7\% $AP_{50}$ gains under the zero-shot detection and generalized zero-shot detection settings, and reduces the $AP_{50}$ performance gap from 14\% to 7.3\% compared to the best two-stage detector.

</details>

### C2 AM: Contrastive learning of Class-agnostic Activation Map for Weakly Supervised Object Localization and Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00106) · 📚 被引 144
- **作者**: Jinheng Xie, Jianfeng Xiang, Junliang Chen, Xianxu Hou, Xiaodong Zhao, Linlin Shen
- **🏷️ 机构**: School of Computer Science &#x0026; Software Engineering, Shenzhen University,China
- **会议**: CVPR 2022

> Existing open-vocabulary object detectors typically enlarge their vocabulary sizes by leveraging different forms of weak supervision. This helps generalize to novel objects at inference. Two popular forms of weak-supervision used in open-vocabulary detection (OVD) include pretrained CLIP model and image-level supervision. We note that both these modes of supervision are not optimally aligned for the detection task: CLIP is trained with image-text pairs and lacks precise localization of objects while the image-level supervision has been used with heuristics that do not accurately specify local object regions. In this work, we propose to address this problem by performing object-centric alignment of the language embeddings from the CLIP model. Furthermore, we visually ground the objects with only image-level supervision using a pseudo-labeling process that provides high-quality object proposals and helps expand the vocabulary during training. We establish a bridge between the above two object-alignment strategies via a novel weight transfer function that aggregates their complimentary strengths. In essence, the proposed model seeks to minimize the gap between object and image-centric representations in the OVD setting. On the COCO benchmark, our proposed approach achieves 36.6 AP50 on novel classes, an absolute 8.2 gain over the previous best performance. For LVIS, we surpass the state-of-the-art ViLD model by 5.0 mask AP for rare categories and 3.4 overall. Code: https://github.com/hanoonaR/object-centric-ovd.

- Unknown-Aware Object Detection: Learning What You Don't Know from Videos in the Wild. → [object-detection](../object-detection/Guideline%202022.md)
- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [object-detection](../object-detection/Guideline%202022.md)
- Expanding Low-Density Latent Regions for Open-Set Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Open-Vocabulary Instance Segmentation via Robust Cross-Modal Pseudo-Labeling. → [multimodal](../multimodal/Guideline%202022.md)
