# Open-set Detection — 2024 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OVT-B: A New Large-Scale Benchmark for Open-Vocabulary Multi-Object Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/1adeeac24ce6168e20bcee85645720e9-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Haiji Liang, Ruize Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### OpenGaussian: Towards Point-Level 3D Gaussian-based Open Vocabulary Understanding.
- **链接**: [arXiv:2406.02058](https://arxiv.org/abs/2406.02058) · 📚 被引 22
- **作者**: Yanmin Wu, Jiarui Meng, Haijie Li, Chenming Wu, Yahao Shi, Xinhua Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces OpenGaussian, a method based on 3D Gaussian Splatting (3DGS) capable of 3D point-level open vocabulary understanding. Our primary motivation stems from observing that existing 3DGS-based open vocabulary methods mainly focus on 2D pixel-level parsing. These methods struggle with 3D point-level tasks due to weak feature expressiveness and inaccurate 2D-3D feature associations. To ensure robust feature presentation and 3D point-level understanding, we first employ SAM masks without cross-frame associations to train instance features with 3D consistency. These features exhibit both intra-object consistency and inter-object distinction. Then, we propose a two-stage codebook to discretize these features from coarse to fine levels. At the coarse level, we consider the positional information of 3D points to achieve location-based clustering, which is then refined at the fine level. Finally, we introduce an instance-level 3D-2D feature association method that links 3D points to 2D masks, which are further associated with 2D CLIP features. Extensive experiments, including open vocabulary-based 3D object selection, 3D point cloud understanding, click-based 3D object selection, and ablation studies, demonstrate the effectiveness of our proposed method. The source code is available at our project page: https://3d-aigc.github.io/OpenGaussian

</details>

### Understanding Multi-Granularity for Open-Vocabulary Part Segmentation.
- **链接**: [arXiv:2406.11384](https://arxiv.org/abs/2406.11384) · 📚 被引 3
- **作者**: Jiho Choi, Seonho Lee, Seungho Lee, Minhyun Lee, Hyunjung Shim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary part segmentation (OVPS) is an emerging research area focused on segmenting fine-grained entities using diverse and previously unseen vocabularies. Our study highlights the inherent complexities of part segmentation due to intricate boundaries and diverse granularity, reflecting the knowledge-based nature of part identification. To address these challenges, we propose PartCLIPSeg, a novel framework utilizing generalized parts and object-level contexts to mitigate the lack of generalization in fine-grained parts. PartCLIPSeg integrates competitive part relationships and attention control, alleviating ambiguous boundaries and underrepresented parts. Experimental results demonstrate that PartCLIPSeg outperforms existing state-of-the-art OVPS methods, offering refined segmentation and an advanced understanding of part relationships within images. Through extensive experiments, our model demonstrated a significant improvement over the state-of-the-art models on the Pascal-Part-116, ADE20K-Part-234, and PartImageNet datasets.

</details>

### Renovating Names in Open-Vocabulary Segmentation Benchmarks.
- **链接**: [arXiv:2403.09593](https://arxiv.org/abs/2403.09593) · 📚 被引 1
- **作者**: Haiwen Huang, Songyou Peng, Dan Zhang, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Names are essential to both human cognition and vision-language models. Open-vocabulary models utilize class names as text prompts to generalize to categories unseen during training. However, the precision of these names is often overlooked in existing datasets. In this paper, we address this underexplored problem by presenting a framework for "renovating" names in open-vocabulary segmentation benchmarks (RENOVATE). Our framework features a renaming model that enhances the quality of names for each visual segment. Through experiments, we demonstrate that our renovated names help train stronger open-vocabulary models with up to 15% relative improvement and significantly enhance training efficiency with improved data quality. We also show that our renovated names improve evaluation by better measuring misclassification and enabling fine-grained model analysis. We will provide our code and relabelings for several popular segmentation datasets (MS COCO, ADE20K, Cityscapes) to the research community.

</details>

### Relationship Prompt Learning is Enough for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8773cdaf02c5af3528e05f1cee816129-Abstract-Conference.html) · 📚 被引 4
- **作者**: Jiahao Li, Yang Lu, Yuan Xie, Yanyun Qu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Towards Open-Vocabulary Semantic Segmentation Without Semantic Labels.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/1119587863e78451f080da2a768c4935-Abstract-Conference.html) · 📚 被引 6
- **作者**: Heeseong Shin, Chaehyun Kim, Sunghwan Hong, Seokju Cho, Anurag Arnab, Paul Hongsuck Seo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Does Video-Text Pretraining Help Open-Vocabulary Online Action Detection?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5598cf1b2905a26ddb863e6705588327-Abstract-Conference.html) · 📚 被引 3
- **作者**: Qingsong Zhao, Yi Wang, Jilan Xu, Yinan He, Zifan Song, Limin Wang et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- ImOV3D: Learning Open Vocabulary Point Clouds 3D Object Detection from Only 2D Images. → [3d-detection](../3d-detection/Guideline%202024.md)
- Open-Vocabulary Object Detection via Language Hierarchy. → [object-detection](../object-detection/Guideline%202024.md)
- Training an Open-Vocabulary Monocular 3D Detection Model without 3D Data. → [3d-detection](../3d-detection/Guideline%202024.md)
- XMask3D: Cross-modal Mask Reasoning for Open Vocabulary 3D Semantic Segmentation. → [multimodal](../multimodal/Guideline%202024.md)
- UMB: Understanding Model Behavior for Open-World Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
