# Open-set Detection — 2023 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-VCLIP: Transforming CLIP to an Open-vocabulary Video Model via Interpolated Weight Optimization.
- **链接**: [出版页](https://proceedings.mlr.press/v202/weng23b.html)
- **作者**: Zejia Weng, Xitong Yang, Ang Li, Zuxuan Wu, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Open-Vocabulary Universal Image Segmentation with MaskCLIP.
- **链接**: [出版页](https://proceedings.mlr.press/v202/ding23c.html)
- **作者**: Zheng Ding, Jieke Wang, Zhuowen Tu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### SegCLIP: Patch Aggregation with Learnable Centers for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2211.14813](https://arxiv.org/abs/2211.14813) · [代码](https://github.com/ArrowLuo/SegCLIP)
- **作者**: Huaishao Luo, Junwei Bao, Youzheng Wu, Xiaodong He, Tianrui Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the contrastive language-image pre-training, e.g., CLIP, has demonstrated promising results on various downstream tasks. The pre-trained model can capture enriched visual concepts for images by learning from a large scale of text-image data. However, transferring the learned visual knowledge to open-vocabulary semantic segmentation is still under-explored. In this paper, we propose a CLIP-based model named SegCLIP for the topic of open-vocabulary segmentation in an annotation-free manner. The SegCLIP achieves segmentation based on ViT and the main idea is to gather patches with learnable centers to semantic regions through training on text-image pairs. The gathering operation can dynamically capture the semantic groups, which can be used to generate the final segmentation results. We further propose a reconstruction loss on masked patches and a superpixel-based KL loss with pseudo-labels to enhance the visual representation. Experimental results show that our model achieves comparable or superior segmentation accuracy on the PASCAL VOC 2012 (+0.3% mIoU), PASCAL Context (+2.3% mIoU), and COCO (+2.2% mIoU) compared with baselines. We release the code at https://github.com/ArrowLuo/SegCLIP.

</details>

## 跨领域论文（完整笔记在其他领域）

- Multi-Modal Classifiers for Open-Vocabulary Object Detection. → [multimodal](../multimodal/Guideline%202023.md)
