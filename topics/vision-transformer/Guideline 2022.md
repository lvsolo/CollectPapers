# Vision Transformer — 2022 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Q-ViT: Accurate and Fully Quantized Low-bit Vision Transformer.
- **链接**: [arXiv:2210.06707](https://arxiv.org/abs/2210.06707) · [代码](https://github.com/YanjingLi0202/Q-ViT) · 📚 被引 19
- **作者**: Yanjing Li, Sheng Xu, Baochang Zhang, Xianbin Cao, Peng Gao, Guodong Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The large pre-trained vision transformers (ViTs) have demonstrated remarkable performance on various visual tasks, but suffer from expensive computational and memory cost problems when deployed on resource-constrained devices. Among the powerful compression approaches, quantization extremely reduces the computation and memory consumption by low-bit parameters and bit-wise operations. However, low-bit ViTs remain largely unexplored and usually suffer from a significant performance drop compared with the real-valued counterparts. In this work, through extensive empirical analysis, we first identify the bottleneck for severe performance drop comes from the information distortion of the low-bit quantized self-attention map. We then develop an information rectification module (IRM) and a distribution guided distillation (DGD) scheme for fully quantized vision transformers (Q-ViT) to effectively eliminate such distortion, leading to a fully quantized ViTs. We evaluate our methods on popular DeiT and Swin backbones. Extensive experimental results show that our method achieves a much better performance than the prior arts. For example, our Q-ViT can theoretically accelerates the ViT-S by 6.14x and achieves about 80.9% Top-1 accuracy, even surpassing the full-precision counterpart by 1.0% on ImageNet dataset. Our codes and models are attached on https://github.com/YanjingLi0202/Q-ViT

</details>

### Orthogonal Transformer: An Efficient Vision Transformer Backbone with Token Orthogonalization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5d8c01de2dc698c54201c1c7d0b86974-Abstract-Conference.html) · 📚 被引 2
- **作者**: Huaibo Huang, Xiaoqiang Zhou, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### M³ViT: Mixture-of-Experts Vision Transformer for Efficient Multi-task Learning with Model-Accelerator Co-design.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/b653f34d576d1790481e3797cb740214-Abstract-Conference.html) · 📚 被引 10
- **作者**: Hanxue Liang, Zhiwen Fan, Rishov Sarkar, Ziyu Jiang, Tianlong Chen, Kai Zou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Expediting Large-Scale Vision Transformer for Dense Prediction without Fine-tuning.
- **链接**: [arXiv:2210.01035](https://arxiv.org/abs/2210.01035) · 📚 被引 0
- **作者**: Weicong Liang, Yuhui Yuan, Henghui Ding, Xiao Luo, Weihong Lin, Ding Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have recently achieved competitive results across various vision tasks but still suffer from heavy computation costs when processing a large number of tokens. Many advanced approaches have been developed to reduce the total number of tokens in large-scale vision transformers, especially for image classification tasks. Typically, they select a small group of essential tokens according to their relevance with the class token, then fine-tune the weights of the vision transformer. Such fine-tuning is less practical for dense prediction due to the much heavier computation and GPU memory cost than image classification. In this paper, we focus on a more challenging problem, i.e., accelerating large-scale vision transformers for dense prediction without any additional re-training or fine-tuning. In response to the fact that high-resolution representations are necessary for dense prediction, we present two non-parametric operators, a token clustering layer to decrease the number of tokens and a token reconstruction layer to increase the number of tokens. The following steps are performed to achieve this: (i) we use the token clustering layer to cluster the neighboring tokens together, resulting in low-resolution representations that maintain the spatial structures; (ii) we apply the following transformer layers only to these low-resolution representations or clustered tokens; and (iii) we use the token reconstruction layer to re-create the high-resolution representations from the refined low-resolution representations. The results obtained by our method are promising on five dense prediction tasks, including object detection, semantic segmentation, panoptic segmentation, instance segmentation, and depth estimation.

</details>

### Peripheral Vision Transformer.
- **链接**: [arXiv:2206.06801](https://arxiv.org/abs/2206.06801)
- **作者**: Juhong Min, Yucheng Zhao, Chong Luo, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human vision possesses a special type of visual processing systems called peripheral vision. Partitioning the entire visual field into multiple contour regions based on the distance to the center of our gaze, the peripheral vision provides us the ability to perceive various visual features at different regions. In this work, we take a biologically inspired approach and explore to model peripheral vision in deep neural networks for visual recognition. We propose to incorporate peripheral position encoding to the multi-head self-attention layers to let the network learn to partition the visual field into diverse peripheral regions given training data. We evaluate the proposed network, dubbed PerViT, on ImageNet-1K and systematically investigate the inner workings of the model for machine perception, showing that the network learns to perceive visual data similarly to the way that human vision does. The performance improvements in image classification over the baselines across different model sizes demonstrate the efficacy of the proposed method.

</details>

### ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation.
- **链接**: [arXiv:2204.12484](https://arxiv.org/abs/2204.12484) · [代码](https://github.com/ViTAE-Transformer/ViTPose) · 📚 被引 142
- **作者**: Yufei Xu, Jing Zhang, Qiming Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although no specific domain knowledge is considered in the design, plain vision transformers have shown excellent performance in visual recognition tasks. However, little effort has been made to reveal the potential of such simple structures for pose estimation tasks. In this paper, we show the surprisingly good capabilities of plain vision transformers for pose estimation from various aspects, namely simplicity in model structure, scalability in model size, flexibility in training paradigm, and transferability of knowledge between models, through a simple baseline model called ViTPose. Specifically, ViTPose employs plain and non-hierarchical vision transformers as backbones to extract features for a given person instance and a lightweight decoder for pose estimation. It can be scaled up from 100M to 1B parameters by taking the advantages of the scalable model capacity and high parallelism of transformers, setting a new Pareto front between throughput and performance. Besides, ViTPose is very flexible regarding the attention type, input resolution, pre-training and finetuning strategy, as well as dealing with multiple pose tasks. We also empirically demonstrate that the knowledge of large ViTPose models can be easily transferred to small ones via a simple knowledge token. Experimental results show that our basic ViTPose model outperforms representative methods on the challenging MS COCO Keypoint Detection benchmark, while the largest model sets a new state-of-the-art. The code and models are available at https://github.com/ViTAE-Transformer/ViTPose.

</details>

### Effectiveness of Vision Transformer for Fast and Accurate Single-Stage Pedestrian Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/afb8caec018d3c8f6ef8b81fa52386fe-Abstract-Conference.html) · 📚 被引 2
- **作者**: Jing Yuan, Panagiotis Barmpoutis, Tania Stathaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Green Hierarchical Vision Transformer for Masked Image Modeling. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- VTC-LFC: Vision Transformer Compression with Low-Frequency Components. → [network-pruning](../network-pruning/Guideline%202022.md)
- SAViT: Structure-Aware Vision Transformer Pruning via Collaborative Optimization. → [network-pruning](../network-pruning/Guideline%202022.md)
