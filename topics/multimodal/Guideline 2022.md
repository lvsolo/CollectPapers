# Multimodal — 2022 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Let Images Give You More: Point Cloud Cross-Modal Training for Shape Analysis.
- **链接**: [arXiv:2210.04208](https://arxiv.org/abs/2210.04208) · [代码](https://github.com/ZhanHeshen/PointCMT) · 📚 被引 0
- **作者**: Xu Yan, Heshen Zhan, Chaoda Zheng, Jiantao Gao, Ruimao Zhang, Shuguang Cui et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although recent point cloud analysis achieves impressive progress, the paradigm of representation learning from a single modality gradually meets its bottleneck. In this work, we take a step towards more discriminative 3D point cloud representation by fully taking advantages of images which inherently contain richer appearance information, e.g., texture, color, and shade. Specifically, this paper introduces a simple but effective point cloud cross-modality training (PointCMT) strategy, which utilizes view-images, i.e., rendered or projected 2D images of the 3D object, to boost point cloud analysis. In practice, to effectively acquire auxiliary knowledge from view images, we develop a teacher-student framework and formulate the cross modal learning as a knowledge distillation problem. PointCMT eliminates the distribution discrepancy between different modalities through novel feature and classifier enhancement criteria and avoids potential negative transfer effectively. Note that PointCMT effectively improves the point-only representation without architecture modification. Sufficient experiments verify significant gains on various datasets using appealing backbones, i.e., equipped with PointCMT, PointNet++ and PointMLP achieve state-of-the-art performance on two benchmarks, i.e., 94.4% and 86.7% accuracy on ModelNet40 and ScanObjectNN, respectively. Code will be made available at https://github.com/ZhanHeshen/PointCMT.

</details>

### Cross-modal Learning for Image-Guided Point Cloud Shape Completion.
- **链接**: [arXiv:2209.09552](https://arxiv.org/abs/2209.09552) · 📚 被引 15
- **作者**: Emanuele Aiello, Diego Valsesia, Enrico Magli
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper we explore the recent topic of point cloud completion, guided by an auxiliary image. We show how it is possible to effectively combine the information from the two modalities in a localized latent space, thus avoiding the need for complex point cloud reconstruction methods from single views used by the state-of-the-art. We also investigate a novel weakly-supervised setting where the auxiliary image provides a supervisory signal to the training process by using a differentiable renderer on the completed point cloud to measure fidelity in the image space. Experiments show significant improvements over state-of-the-art supervised methods for both unimodal and multimodal completion. We also show the effectiveness of the weakly-supervised approach which outperforms a number of supervised methods and is competitive with the latest supervised models only exploiting point cloud information.

</details>

### Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning.
- **链接**: [arXiv:2203.02053](https://arxiv.org/abs/2203.02053) · 📚 被引 55
- **作者**: Weixin Liang, Yuhui Zhang, Yongchan Kwon, Serena Yeung, James Y. Zou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present modality gap, an intriguing geometric phenomenon of the representation space of multi-modal models. Specifically, we show that different data modalities (e.g. images and text) are embedded at arm's length in their shared representation in multi-modal models such as CLIP. Our systematic analysis demonstrates that this gap is caused by a combination of model initialization and contrastive learning optimization. In model initialization, we show empirically and theoretically that the representation of a common deep neural network is restricted to a narrow cone. As a consequence, in a multi-modal model with two encoders, the representations of the two modalities are clearly apart when the model is initialized. During optimization, contrastive learning keeps the different modalities separate by a certain distance, which is influenced by the temperature parameter in the loss function. Our experiments further demonstrate that varying the modality gap distance has a significant impact in improving the model's downstream zero-shot classification performance and fairness. Our code and data are available at https://modalitygap.readthedocs.io/

</details>

### Multimodal Contrastive Learning with LIMoE: the Language-Image Mixture of Experts.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/3e67e84abf900bb2c7cbd5759bfce62d-Abstract-Conference.html)
- **作者**: Basil Mustafa, Carlos Riquelme, Joan Puigcerver, Rodolphe Jenatton, Neil Houlsby
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Long-Form Video-Language Pre-Training with Multimodal Temporal Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/f8290ccc2905538be1a7f7914ccef629-Abstract-Conference.html)
- **作者**: Yuchong Sun, Hongwei Xue, Ruihua Song, Bei Liu, Huan Yang, Jianlong Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
