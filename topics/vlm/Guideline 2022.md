# VLM — 2022 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### PointCLIP: Point Cloud Understanding by CLIP.
- **链接**: [arXiv:2112.02413](https://arxiv.org/abs/2112.02413) · [代码](https://github.com/ZrrSkywalker/PointCLIP) · 📚 被引 421
- **作者**: Renrui Zhang, Ziyu Guo, Wei Zhang, Kunchang Li, Xupeng Miao, Bin Cui et al.
- **🏷️ 机构**: Shanghai AI Laboratory, Peking University,School of CS and Key Lab of HCST
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, zero-shot and few-shot learning via Contrastive Vision-Language Pre-training (CLIP) have shown inspirational performance on 2D visual recognition, which learns to match images with their corresponding texts in open-vocabulary settings. However, it remains under explored that whether CLIP, pre-trained by large-scale image-text pairs in 2D, can be generalized to 3D recognition. In this paper, we identify such a setting is feasible by proposing PointCLIP, which conducts alignment between CLIP-encoded point cloud and 3D category texts. Specifically, we encode a point cloud by projecting it into multi-view depth maps without rendering, and aggregate the view-wise zero-shot prediction to achieve knowledge transfer from 2D to 3D. On top of that, we design an inter-view adapter to better extract the global feature and adaptively fuse the few-shot knowledge learned from 3D into CLIP pre-trained in 2D. By just fine-tuning the lightweight adapter in the few-shot settings, the performance of PointCLIP could be largely improved. In addition, we observe the complementary property between PointCLIP and classical 3D-supervised networks. By simple ensembling, PointCLIP boosts baseline's performance and even surpasses state-of-the-art models. Therefore, PointCLIP is a promising alternative for effective 3D point cloud understanding via CLIP under low resource cost and data regime. We conduct thorough experiments on widely-adopted ModelNet10, ModelNet40 and the challenging ScanObjectNN to demonstrate the effectiveness of PointCLIP. The code is released at https://github.com/ZrrSkywalker/PointCLIP.

</details>

### 3DJCG: A Unified Framework for Joint Dense Captioning and Visual Grounding on 3D Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01597) · 📚 被引 94
- **作者**: Daigang Cai, Lichen Zhao, Jing Zhang, Lu Sheng, Dong Xu
- **🏷️ 机构**: College of Software, Beihang University,China, The University of Sydney,Australia
- **会议**: CVPR 2022

## 跨领域论文（完整笔记在其他领域）

- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [object-detection](../object-detection/Guideline%202022.md)
