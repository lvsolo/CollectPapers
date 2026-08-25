# Vision Transformer — 2024 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### HEAL-SWIN: A Vision Transformer on the Sphere.
- **链接**: [arXiv:2307.07313](https://arxiv.org/abs/2307.07313)
- **作者**: Oscar Carlsson, Jan E. Gerken, Hampus Linander, Heiner Spieß, Fredrik Ohlsson, Christoffer Petersson et al.
- **🏷️ 机构**: Chalmers University of Tech-nology, University of Gothenburg,Department of Mathematical Sciences,Gothenburg,Sweden,SE-41296, Neural Information Processing, Science of Intelligence, Technical University Berlin,Berlin,Germany,DE-10623, Ume&#x00E5; Uni-versity,Department of Mathematics and Mathematical Statistics,Ume&#x00E5;,Sweden,SE-90187
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > High-resolution wide-angle fisheye images are becoming more and more important for robotics applications such as autonomous driving. However, using ordinary convolutional neural networks or vision transformers on this data is problematic due to projection and distortion losses introduced when projecting to a rectangular grid on the plane. We introduce the HEAL-SWIN transformer, which combines the highly uniform Hierarchical Equal Area iso-Latitude Pixelation (HEALPix) grid used in astrophysics and cosmology with the Hierarchical Shifted-Window (SWIN) transformer to yield an efficient and flexible model capable of training on high-resolution, distortion-free spherical data. In HEAL-SWIN, the nested structure of the HEALPix grid is used to perform the patching and windowing operations of the SWIN transformer, enabling the network to process spherical representations with minimal computational overhead. We demonstrate the superior performance of our model on both synthetic and real automotive datasets, as well as a selection of other image datasets, for semantic segmentation, depth regression and classification tasks. Our code is publicly available at https://github.com/JanEGerken/HEAL-SWIN.

### H-ViT: A Hierarchical Vision Transformer for Deformable Image Registration.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01094)
- **作者**: Morteza Ghahremani, Mohammad Khateri, Bailiang Jian, Benedikt Wiestler, Ehsan Adeli, Christian Wachinger
- **🏷️ 机构**: Technical University of Munich, University of Eastern Finland, Stanford University
- **会议**: CVPR 2024

### DeiT-LT: Distillation Strikes Back for Vision Transformer Training on Long-Tailed Datasets.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02208)
- **作者**: Harsh Rangwani, Pradipto Mondal, Mayank Mishra, Ashish Ramayee Asokan, R. Venkatesh Babu
- **🏷️ 机构**: Indian Institute of Science,Bangalore, Indian Institute of Technology,Kharagpur
- **会议**: CVPR 2024

### ViT-CoMer: Vision Transformer with Convolutional Multi-scale Feature Interaction for Dense Predictions.
- **链接**: [arXiv:2403.07392](https://arxiv.org/abs/2403.07392)
- **作者**: Chunlong Xia, Xinliang Wang, Feng Lv, Xin Hao, Yifeng Shi
- **🏷️ 机构**: Baidu Inc.
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Although Vision Transformer (ViT) has achieved significant success in computer vision, it does not perform well in dense prediction tasks due to the lack of inner-patch information interaction and the limited diversity of feature scale. Most existing studies are devoted to designing vision-specific transformers to solve the above problems, which introduce additional pre-training costs. Therefore, we present a plain, pre-training-free, and feature-enhanced ViT backbone with Convolutional Multi-scale feature interaction, named ViT-CoMer, which facilitates bidirectional interaction between CNN and transformer. Compared to the state-of-the-art, ViT-CoMer has the following advantages: (1) We inject spatial pyramid multi-receptive field convolutional features into the ViT architecture, which effectively alleviates the problems of limited local information interaction and single-feature representation in ViT. (2) We propose a simple and efficient CNN-Transformer bidirectional fusion interaction module that performs multi-scale fusion across hierarchical features, which is beneficial for handling dense prediction tasks. (3) We evaluate the performance of ViT-CoMer across various dense prediction tasks, different frameworks, and multiple advanced pre-training. Notably, our ViT-CoMer-L achieves 64.3% AP on COCO val2017 without extra training data, and 62.1% mIoU on ADE20K val, both of which are comparable to state-of-the-art methods. We hope ViT-CoMer can serve as a new backbone for dense prediction tasks to facilitate future research. The code will be released at https://github.com/Traffic-X/ViT-CoMer.

### Progressive Semantic-Guided Vision Transformer for Zero-Shot Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02262)
- **作者**: Shiming Chen, Wenjin Hou, Salman H. Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI, Huazhong University of Science and Technology
- **会议**: CVPR 2024

### Low-Rank Rescaled Vision Transformer Fine-Tuning: A Residual Design Approach.
- **链接**: [arXiv:2403.19067](https://arxiv.org/abs/2403.19067)
- **作者**: Wei Dong, Xing Zhang, Bihui Chen, Dawei Yan, Zhijun Lin, Qingsen Yan et al.
- **🏷️ 机构**: School of Computer Science and Engineering, University of Electronic Science and Technology of China, College of Information and Control Engineering, Xi&#x0027;an University of Architecture and Technology, School of Computer Science, Northwestern Polytechnical University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Parameter-efficient fine-tuning for pre-trained Vision Transformers aims to adeptly tailor a model to downstream tasks by learning a minimal set of new adaptation parameters while preserving the frozen majority of pre-trained parameters. Striking a balance between retaining the generalizable representation capacity of the pre-trained model and acquiring task-specific features poses a key challenge. Currently, there is a lack of focus on guiding this delicate trade-off. In this study, we approach the problem from the perspective of Singular Value Decomposition (SVD) of pre-trained parameter matrices, providing insights into the tuning dynamics of existing methods. Building upon this understanding, we propose a Residual-based Low-Rank Rescaling (RLRR) fine-tuning strategy. This strategy not only enhances flexibility in parameter tuning but also ensures that new parameters do not deviate excessively from the pre-trained model through a residual design. Extensive experiments demonstrate that our method achieves competitive performance across various downstream image classification tasks, all while maintaining comparable new parameters. We believe this work takes a step forward in offering a unified perspective for interpreting existing methods and serves as motivation for the development of new approaches that move closer to effectively considering the crucial trade-off mentioned above. Our code is available at \href{https://github.com/zstarN70/RLRR.git}{https://github.com/zstarN70/RLRR.git}.

### Random Entangled Tokens for Adversarially Robust Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02318)
- **作者**: Huihui Gong, Minjing Dong, Siqi Ma, Seyit Camtepe, Surya Nepal, Chang Xu
- **🏷️ 机构**: The University of Sydney, City University of Hong Kong, The University of New South Wales
- **会议**: CVPR 2024

### SpikingResformer: Bridging ResNet and Vision Transformer in Spiking Neural Networks.
- **链接**: [arXiv:2403.14302](https://arxiv.org/abs/2403.14302)
- **作者**: Xinyu Shi, Zecheng Hao, Zhaofei Yu
- **🏷️ 机构**: Institute for Artificial Intelligence, Peking University, School of Computer Science, Peking University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The remarkable success of Vision Transformers in Artificial Neural Networks (ANNs) has led to a growing interest in incorporating the self-attention mechanism and transformer-based architecture into Spiking Neural Networks (SNNs). While existing methods propose spiking self-attention mechanisms that are compatible with SNNs, they lack reasonable scaling methods, and the overall architectures proposed by these methods suffer from a bottleneck in effectively extracting local features. To address these challenges, we propose a novel spiking self-attention mechanism named Dual Spike Self-Attention (DSSA) with a reasonable scaling method. Based on DSSA, we propose a novel spiking Vision Transformer architecture called SpikingResformer, which combines the ResNet-based multi-stage architecture with our proposed DSSA to improve both performance and energy efficiency while reducing parameters. Experimental results show that SpikingResformer achieves higher accuracy with fewer parameters and lower energy consumption than other spiking Vision Transformer counterparts. Notably, our SpikingResformer-L achieves 79.40% top-1 accuracy on ImageNet with 4 time-steps, which is the state-of-the-art result in the SNN field.

### Token Transformation Matters: Towards Faithful Post-Hoc Explanation for Vision Transformer.
- **链接**: [arXiv:2403.14552](https://arxiv.org/abs/2403.14552)
- **作者**: Junyi Wu, Bin Duan, Weitai Kang, Hao Tang, Yan Yan
- **🏷️ 机构**: Illinois Institute of Technology,Department of Computer Science,USA, Robotics Institute, Carnegie Mellon University,USA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > While Transformers have rapidly gained popularity in various computer vision applications, post-hoc explanations of their internal mechanisms remain largely unexplored. Vision Transformers extract visual information by representing image regions as transformed tokens and integrating them via attention weights. However, existing post-hoc explanation methods merely consider these attention weights, neglecting crucial information from the transformed tokens, which fails to accurately illustrate the rationales behind the models' predictions. To incorporate the influence of token transformation into interpretation, we propose TokenTM, a novel post-hoc explanation method that utilizes our introduced measurement of token transformation effects. Specifically, we quantify token transformation effects by measuring changes in token lengths and correlations in their directions pre- and post-transformation. Moreover, we develop initialization and aggregation rules to integrate both attention weights and token transformation effects across all layers, capturing holistic token contributions throughout the model. Experimental results on segmentation and perturbation tests demonstrate the superiority of our proposed TokenTM compared to state-of-the-art Vision Transformer explanation methods.

### On the Faithfulness of Vision Transformer Explanations.
- **链接**: [arXiv:2404.01415](https://arxiv.org/abs/2404.01415)
- **作者**: Junyi Wu, Weitai Kang, Hao Tang, Yuan Hong, Yan Yan
- **🏷️ 机构**: Illinois Institute of Technology,Department of Computer Science,USA, Robotics Institute, Carnegie Mellon University,USA, University of Connecticut,Department of Computer Science,USA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > To interpret Vision Transformers, post-hoc explanations assign salience scores to input pixels, providing human-understandable heatmaps. However, whether these interpretations reflect true rationales behind the model's output is still underexplored. To address this gap, we study the faithfulness criterion of explanations: the assigned salience scores should represent the influence of the corresponding input pixels on the model's predictions. To evaluate faithfulness, we introduce Salience-guided Faithfulness Coefficient (SaCo), a novel evaluation metric leveraging essential information of salience distribution. Specifically, we conduct pair-wise comparisons among distinct pixel groups and then aggregate the differences in their salience scores, resulting in a coefficient that indicates the explanation's degree of faithfulness. Our explorations reveal that current metrics struggle to differentiate between advanced explanation methods and Random Attribution, thereby failing to capture the faithfulness property. In contrast, our proposed SaCo offers a reliable faithfulness measurement, establishing a robust metric for interpretations. Furthermore, our SaCo demonstrates that the use of gradient and multi-layer aggregation can markedly enhance the faithfulness of attention-based explanation, shedding light on potential paths for advancing Vision Transformer explainability.

### SHViT: Single-Head Vision Transformer with Memory Efficient Macro Design.
- **链接**: [arXiv:2401.16456](https://arxiv.org/abs/2401.16456)
- **作者**: Seokju Yun, Youngmin Ro
- **🏷️ 机构**: University of Seoul,Machine Intelligence Laboratory,Korea
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recently, efficient Vision Transformers have shown great performance with low latency on resource-constrained devices. Conventionally, they use 4x4 patch embeddings and a 4-stage structure at the macro level, while utilizing sophisticated attention with multi-head configuration at the micro level. This paper aims to address computational redundancy at all design levels in a memory-efficient manner. We discover that using larger-stride patchify stem not only reduces memory access costs but also achieves competitive performance by leveraging token representations with reduced spatial redundancy from the early stages. Furthermore, our preliminary analyses suggest that attention layers in the early stages can be substituted with convolutions, and several attention heads in the latter stages are computationally redundant. To handle this, we introduce a single-head attention module that inherently prevents head redundancy and simultaneously boosts accuracy by parallelly combining global and local information. Building upon our solutions, we introduce SHViT, a Single-Head Vision Transformer that obtains the state-of-the-art speed-accuracy tradeoff. For example, on ImageNet-1k, our SHViT-S4 is 3.3x, 8.1x, and 2.4x faster than MobileViTv2 x1.0 on GPU, CPU, and iPhone12 mobile device, respectively, while being 1.3% more accurate. For object detection and instance segmentation on MS COCO using Mask-RCNN head, our model achieves performance comparable to FastViT-SA12 while exhibiting 3.8x and 2.0x lower backbone latency on GPU and mobile device, respectively.

## 跨领域论文（完整笔记在其他领域）

- Question Aware Vision Transformer for Multimodal Reasoning. → [multimodal](../multimodal/Guideline%202024.md)
- Once for Both: Single Stage of Importance and Sparsity Search for Vision Transformer Compression. → [network-pruning](../network-pruning/Guideline%202024.md)
- Dense Vision Transformer Compression with Few Samples. → [network-pruning](../network-pruning/Guideline%202024.md)
