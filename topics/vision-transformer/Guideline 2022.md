# Vision Transformer — 2022 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Q-ViT: Accurate and Fully Quantized Low-bit Vision Transformer.
- **链接**: [arXiv:2210.06707](https://arxiv.org/abs/2210.06707) · [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/deb921bff461a7b0a5c344a4871e7101-Abstract-Conference.html) · [代码](https://github.com/YanjingLi0202/Q-ViT)
- **作者**: Yanjing Li, Sheng Xu, Baochang Zhang, Xianbin Cao, Peng Gao, Guodong Guo
- **🏷️ 机构**: Beihang University
- **会议**: NeurIPS 2022

- **摘要（英，原文）**:

  > The large pre-trained vision transformers (ViTs) have demonstrated remarkable performance on various visual tasks, but suffer from expensive computational and memory cost problems when deployed on resource-constrained devices. Among the powerful compression approaches, quantization extremely reduces the computation and memory consumption by low-bit parameters and bit-wise operations. However, low-bit ViTs remain largely unexplored and usually suffer from a significant performance drop compared with the real-valued counterparts. In this work, through extensive empirical analysis, we first identify the bottleneck for severe performance drop comes from the information distortion of the low-bit quantized self-attention map. We then develop an information rectification module (IRM) and a distribution guided distillation (DGD) scheme for fully quantized vision transformers (Q-ViT) to effectively eliminate such distortion, leading to a fully quantized ViTs. We evaluate our methods on popular DeiT and Swin backbones. Extensive experimental results show that our method achieves a much better performance than the prior arts. For example, our Q-ViT can theoretically accelerates the ViT-S by 6.14x and achieves about 80.9% Top-1 accuracy, even surpassing the full-precision counterpart by 1.0% on ImageNet dataset. Our codes and models are attached on https://github.com/YanjingLi0202/Q-ViT

### Orthogonal Transformer: An Efficient Vision Transformer Backbone with Token Orthogonalization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5d8c01de2dc698c54201c1c7d0b86974-Abstract-Conference.html) · 📚 35 citations
- **作者**: Huaibo Huang, Xiaoqiang Zhou, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### M³ViT: Mixture-of-Experts Vision Transformer for Efficient Multi-task Learning with Model-Accelerator Co-design.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/b653f34d576d1790481e3797cb740214-Abstract-Conference.html) · 📚 169 citations
- **作者**: Hanxue Liang, Zhiwen Fan, Rishov Sarkar, Ziyu Jiang, Tianlong Chen, Kai Zou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Expediting Large-Scale Vision Transformer for Dense Prediction without Fine-tuning.
- **链接**: [arXiv:2210.01035](https://arxiv.org/abs/2210.01035) · [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/e6c2e85db1f1039177c4495ccd399ac4-Abstract-Conference.html) · 📚 48 citations
- **作者**: Weicong Liang, Yuhui Yuan, Henghui Ding, Xiao Luo, Weihong Lin, Ding Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

- **摘要（英，原文）**:

  > Vision transformers have recently achieved competitive results across various vision tasks but still suffer from heavy computation costs when processing a large number of tokens. Many advanced approaches have been developed to reduce the total number of tokens in large-scale vision transformers, especially for image classification tasks. Typically, they select a small group of essential tokens according to their relevance with the class token, then fine-tune the weights of the vision transformer. Such fine-tuning is less practical for dense prediction due to the much heavier computation and GPU memory cost than image classification. In this paper, we focus on a more challenging problem, i.e., accelerating large-scale vision transformers for dense prediction without any additional re-training or fine-tuning. In response to the fact that high-resolution representations are necessary for dense prediction, we present two non-parametric operators, a token clustering layer to decrease the number of tokens and a token reconstruction layer to increase the number of tokens. The following steps are performed to achieve this: (i) we use the token clustering layer to cluster the neighboring tokens together, resulting in low-resolution representations that maintain the spatial structures; (ii) we apply the following transformer layers only to these low-resolution representations or clustered tokens; and (iii) we use the token reconstruction layer to re-create the high-resolution representations from the refined low-resolution representations. The results obtained by our method are promising on five dense prediction tasks, including object detection, semantic segmentation, panoptic segmentation, instance segmentation, and depth estimation.

### Peripheral Vision Transformer.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/cf78a15772ec1a6aee9bbee2d2b382c3-Abstract-Conference.html) · 📚 49 citations
- **作者**: Juhong Min, Yucheng Zhao, Chong Luo, Minsu Cho
- **🏷️ 机构**: Pohang University of Science and Technology, POSTECH CSE
- **会议**: NeurIPS 2022

### ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/fbb10d319d44f8c3b4720873e4177c65-Abstract-Conference.html) · 📚 1046 citations
- **作者**: Yufei Xu, Jing Zhang, Qiming Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Effectiveness of Vision Transformer for Fast and Accurate Single-Stage Pedestrian Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/afb8caec018d3c8f6ef8b81fa52386fe-Abstract-Conference.html)
- **作者**: Jing Yuan, Panagiotis Barmpoutis, Tania Stathaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Green Hierarchical Vision Transformer for Masked Image Modeling. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- VTC-LFC: Vision Transformer Compression with Low-Frequency Components. → [network-pruning](../network-pruning/Guideline%202022.md)
- SAViT: Structure-Aware Vision Transformer Pruning via Collaborative Optimization. → [network-pruning](../network-pruning/Guideline%202022.md)
