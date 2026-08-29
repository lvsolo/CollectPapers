# Video Understanding — 2021 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Spatiotemporal Contrastive Video Representation Learning.
- **链接**: [arXiv:2008.03800](https://arxiv.org/abs/2008.03800) · [代码](https://github.com/tensorflow/models)
- **作者**: Rui Qian, Tianjian Meng, Boqing Gong, Ming-Hsuan Yang, Huisheng Wang, Serge J. Belongie et al.
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2021

### Long Short View Feature Decomposition via Contrastive Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00911) · 📚 被引 25
- **作者**: Nadine Behrmann, Mohsen Fayyaz, Juergen Gall, Mehdi Noroozi
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, University of Bonn
- **会议**: ICCV 2021

### Time-Equivariant Contrastive Video Representation Learning.
- **链接**: [arXiv:2112.03624](https://arxiv.org/abs/2112.03624) · 📚 被引 43
- **作者**: Simon Jenni, Hailin Jin
- **🏷️ 机构**: Adobe Research
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel self-supervised contrastive learning method to learn representations from unlabelled videos. Existing approaches ignore the specifics of input distortions, e.g., by learning invariance to temporal transformations. Instead, we argue that video representation should preserve video dynamics and reflect temporal manipulations of the input. Therefore, we exploit novel constraints to build representations that are equivariant to temporal transformations and better capture video dynamics. In our method, relative temporal transformations between augmented clips of a video are encoded in a vector and contrasted with other transformation vectors. To support temporal equivariance learning, we additionally propose the self-supervised classification of two clips of a video into 1. overlapping 2. ordered, or 3. unordered. Our experiments show that time-equivariant representations achieve state-of-the-art results in video retrieval and action recognition benchmarks on UCF101, HMDB51, and Diving48.

</details>

### Visual Semantic Role Labeling for Video Understanding.
- **链接**: [arXiv:2104.00990](https://arxiv.org/abs/2104.00990) · 📚 被引 44
- **作者**: Arka Sadhu, Tanmay Gupta, Mark Yatskar, Ram Nevatia, Aniruddha Kembhavi
- **🏷️ 机构**: University of Southern California, PRIOR @ Allen Institute for AI, University of Pennsylvania
- **会议**: CVPR 2021

## 跨领域论文（完整笔记在其他领域）

> Accurate video understanding involves reasoning about the relationships between actors, objects and their environment, often over long temporal intervals. In this paper, we propose a message passing graph neural network that explicitly models these spatio-temporal relations and can use explicit representations of objects, when supervision is available, and implicit representations otherwise. Our formulation generalises previous structured models for video understanding, and allows us to study how different design choices in graph structure and representation affect the model's performance. We demonstrate our method on two different tasks requiring relational reasoning in videos -- spatio-temporal action detection on AVA and UCF101-24, and video scene graph classification on the recent Action Genome dataset -- and achieve state-of-the-art results on all three datasets. Furthermore, we show quantitatively and qualitatively how our method is able to more effectively model relationships between relevant entities in the scene.

</details>

### Towards Long-Form Video Understanding.
- **链接**: [arXiv:2106.11310](https://arxiv.org/abs/2106.11310) · 📚 被引 120
- **作者**: Chao-Yuan Wu, Philipp Krähenbühl
- **🏷️ 机构**: UT Austin
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human pose is a useful feature for fine-grained sports action understanding. However, pose estimators are often unreliable when run on sports video due to domain shift and factors such as motion blur and occlusions. This leads to poor accuracy when downstream tasks, such as action recognition, depend on pose. End-to-end learning circumvents pose, but requires more labels to generalize. We introduce Video Pose Distillation (VPD), a weakly-supervised technique to learn features for new video domains, such as individual sports that challenge pose estimation. Under VPD, a student network learns to extract robust pose features from RGB frames in the sports video, such that, whenever pose is considered reliable, the features match the output of a pretrained teacher pose detector. Our strategy retains the best of both pose and end-to-end worlds, exploiting the rich visual patterns in raw video frames, while learning features that agree with the athletes' pose and motion in the target video domain to avoid over-fitting to patterns unrelated to athletes' motion. VPD features improve performance on few-shot, fine-grained action recognition, retrieval, and detection tasks in four real-world sports video datasets, without requiring additional ground-truth pose annotations.

</details>

### Temporal Query Networks for Fine-Grained Video Understanding.
- **链接**: [arXiv:2104.09496](https://arxiv.org/abs/2104.09496) · 📚 被引 88
- **作者**: Chuhan Zhang, Ankush Gupta, Andrew Zisserman
- **🏷️ 机构**: University of Oxford, DeepMind,London
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our objective in this work is fine-grained classification of actions in untrimmed videos, where the actions may be temporally extended or may span only a few frames of the video. We cast this into a query-response mechanism, where each query addresses a particular question, and has its own response label set. We make the following four contributions: (I) We propose a new model - a Temporal Query Network - which enables the query-response functionality, and a structural understanding of fine-grained actions. It attends to relevant segments for each query with a temporal attention mechanism, and can be trained using only the labels for each query. (ii) We propose a new way - stochastic feature bank update - to train a network on videos of various lengths with the dense sampling required to respond to fine-grained queries. (iii) We compare the TQN to other architectures and text supervision methods, and analyze their pros and cons. Finally, (iv) we evaluate the method extensively on the FineGym and Diving48 benchmarks for fine-grained action classification and surpass the state-of-the-art using only RGB features.

</details>

### No Frame Left Behind: Full Video Action Recognition.
- **链接**: [arXiv:2103.15395](https://arxiv.org/abs/2103.15395) · 📚 被引 41
- **作者**: Xin Liu, Silvia L. Pintea, Fatemeh Karimi Nejadasl, Olaf Booij, Jan C. van Gemert
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolution has been arguably the most important feature transform for modern neural networks, leading to the advance of deep learning. Recent emergence of Transformer networks, which replace convolution layers with self-attention blocks, has revealed the limitation of stationary convolution kernels and opened the door to the era of dynamic feature transforms. The existing dynamic transforms, including self-attention, however, are all limited for video understanding where correspondence relations in space and time, i.e., motion information, are crucial for effective representation. In this work, we introduce a relational feature transform, dubbed the relational self-attention (RSA), that leverages rich structures of spatio-temporal relations in videos by dynamically generating relational kernels and aggregating relational contexts. Our experiments and ablation studies show that the RSA network substantially outperforms convolution and self-attention counterparts, achieving the state of the art on the standard motion-centric benchmarks for video action recognition, such as Something-Something-V1 & V2, Diving48, and FineGym.

</details>

## 跨领域论文（完整笔记在其他领域）

- DeepVideoMVS: Multi-View Stereo on Video With Recurrent Spatio-Temporal Fusion. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-Supervised Video Representation Learning by Context and Motion Decoupling. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Removing the Background by Adding the Background: Towards Background Robust Self-Supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- VideoMoCo: Contrastive Video Representation Learning With Temporally Adversarial Examples. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)

## 🆕 增量新增

### Env-QA: A Video Question Answering Benchmark for Comprehensive Understanding of Dynamic Environments. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00170)
- **作者**: Difei Gao, Ruiping Wang, Ziyi Bai, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对视频问答中缺乏动态环境综合理解基准的问题。②提出了Env-QA基准，包含动态环境中的视频问答任务。③相比现有基准，更关注环境动态变化和复杂场景。④摘要未提供具体数据，但基准设计旨在推动该领域发展。
- **摘要（英）**: This paper addresses the lack of benchmarks for comprehensive video question answering in dynamic environments. It introduces Env-QA, a new benchmark focusing on dynamic environmental understanding. Compared to existing benchmarks, it emphasizes complex scene dynamics. Specific results are not detailed in the abstract.
- **核心贡献**: 提出了动态环境视频问答基准Env-QA。
- **创新点**: 聚焦动态环境中的视频问答任务。
- **结果**: 基准设计旨在推动领域发展，具体效果未提及。

### Unified Graph Structured Models for Video Understanding. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00801)
- **作者**: Anurag Arnab, Chen Sun, Cordelia Schmid
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对视频理解中多模态信息融合不足的问题。②提出了统一图结构模型，整合视频中的时空关系。③相比现有方法，利用图结构增强跨模态交互。④摘要未提供具体数据，但模型设计旨在提升视频理解性能。
- **摘要（英）**: This paper tackles the issue of insufficient multimodal fusion in video understanding. It proposes unified graph structured models to integrate spatiotemporal relationships. Compared to existing methods, it enhances cross-modal interaction via graph structures. Specific results are not provided in the abstract.
- **核心贡献**: 提出统一图结构模型用于视频理解。
- **创新点**: 利用图结构整合时空与多模态信息。
- **结果**: 性能提升未具体说明。

### Video Pose Distillation for Few-Shot, Fine-Grained Sports Action Recognition. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00912)
- **作者**: James Hong, Matthew Fisher, Michaël Gharbi, Kayvon Fatahalian
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对少样本细粒度体育动作识别中数据稀缺的问题。②提出了视频姿态蒸馏方法，利用姿态信息辅助动作识别。③相比现有方法，通过蒸馏姿态特征提升少样本性能。④摘要未提供具体数据，但方法旨在提升细粒度识别精度。
- **摘要（英）**: This paper addresses the challenge of few-shot fine-grained sports action recognition with limited data. It proposes video pose distillation to leverage pose information. Compared to existing methods, it distills pose features to improve few-shot performance. Specific results are not detailed in the abstract.
- **核心贡献**: 提出视频姿态蒸馏方法用于少样本动作识别。
- **创新点**: 利用姿态特征蒸馏提升细粒度识别。
- **结果**: 具体效果未提及。

### Learning Self-Similarity in Space and Time as Generalized Motion for Video Action Recognition. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01282)
- **作者**: Heeseung Kwon, Manjin Kim, Suha Kwak, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对视频动作识别中运动表示泛化性不足的问题。②提出了学习时空自相似性作为广义运动表示。③相比现有方法，自相似性捕获更鲁棒的时空模式。④摘要未提供具体数据，但方法旨在提升动作识别泛化能力。
- **摘要（英）**: This paper addresses the limited generalization of motion representations in video action recognition. It proposes learning self-similarity in space and time as a generalized motion representation. Compared to existing methods, self-similarity captures more robust spatiotemporal patterns. Specific results are not provided in the abstract.
- **核心贡献**: 提出时空自相似性作为广义运动表示。
- **创新点**: 利用自相似性增强运动表示的泛化性。
- **结果**: 性能提升未具体说明。

### MGSampler: An Explainable Sampling Strategy for Video Action Recognition. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00154)
- **作者**: Yuan Zhi, Zhan Tong, Limin Wang, Gangshan Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对视频动作识别中采样策略不可解释的问题。②提出了MGSampler，一种可解释的采样策略。③相比现有方法，提供可解释性并优化采样效率。④摘要未提供具体数据，但方法旨在提升识别性能与可解释性。
- **摘要（英）**: This paper addresses the lack of explainability in sampling strategies for video action recognition. It proposes MGSampler, an explainable sampling strategy. Compared to existing methods, it enhances interpretability and sampling efficiency. Specific results are not detailed in the abstract.
- **核心贡献**: 提出可解释的采样策略MGSampler。
- **创新点**: 结合可解释性优化视频采样。
- **结果**: 具体效果未提及。

### TeachText: CrossModal Generalized Distillation for Text-Video Retrieval. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01138)
- **作者**: Ioana Croitoru, Simion-Vlad Bogolin, Marius Leordeanu, Hailin Jin, Andrew Zisserman, Samuel Albanie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对文本-视频检索中跨模态知识迁移不足的问题。②提出了TeachText，一种跨模态广义蒸馏方法。③相比现有方法，通过蒸馏增强文本与视频的语义对齐。④摘要未提供具体数据，但方法旨在提升检索性能。
- **摘要（英）**: This paper addresses insufficient cross-modal knowledge transfer in text-video retrieval. It proposes TeachText, a cross-modal generalized distillation method. Compared to existing methods, it enhances semantic alignment via distillation. Specific results are not provided in the abstract.
- **核心贡献**: 提出跨模态蒸馏方法TeachText用于文本-视频检索。
- **创新点**: 利用蒸馏增强跨模态语义对齐。
- **结果**: 检索性能提升未具体说明。

### Is Space-Time Attention All You Need for Video Understanding? **⭐⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2102.05095](https://arxiv.org/abs/2102.05095)
- **作者**: Gedas Bertasius, Heng Wang, Lorenzo Torresani
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021
- **摘要（中）**: ①针对视频理解中3D卷积网络计算量大、难以捕捉长距离时空依赖的问题，提出纯自注意力架构TimeSformer。②方法将标准Transformer适配到视频，从帧级patch序列直接学习时空特征，并比较多种自注意力方案，发现分离注意力（时间与空间注意力分别应用）效果最佳。③相比3D卷积网络，无需卷积操作，训练更快，测试效率更高，且能处理超长视频。④在Kinetics-400和Kinetics-600上达到当时最优精度，且能处理超过一分钟的视频片段。
- **摘要（英）**: This paper tackles video understanding by proposing TimeSformer, a convolution-free architecture based solely on self-attention over space and time. It adapts the standard Transformer to video and finds divided attention (separate temporal and spatial attention) yields best accuracy. Compared to 3D CNNs, it trains faster, achieves higher test efficiency, and handles longer clips, reaching state-of-the-art on Kinetics-400/600.
- **核心贡献**: 提出首个纯自注意力视频分类架构TimeSformer。
- **创新点**: 分离时空注意力机制设计。
- **结果**: 在Kinetics-400/600上达到SOTA，训练和推理效率显著优于3D CNN。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a convolution-free approach to video classification built exclusively on self-attention over space and time. Our method, named "TimeSformer," adapts the standard Transformer architecture to video by enabling spatiotemporal feature learning directly from a sequence of frame-level patches. Our experimental study compares different self-attention schemes and suggests that "divided attention," where temporal attention and spatial attention are separately applied within each block, leads to the best video classification accuracy among the design choices considered. Despite the radically new design, TimeSformer achieves state-of-the-art results on several action recognition benchmarks, including the best reported accuracy on Kinetics-400 and Kinetics-600. Finally, compared to 3D convolutional networks, our model is faster to train, it can achieve dramatically higher test efficiency (at a small drop in accuracy), and it can also be applied to much longer video clips (over one minute long). Code and models are available at: https://github.com/facebookresearch/TimeSformer.

</details>

### Contrastive Learning of Global and Local Video Representations. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/38ef4b66cb25e92abe4d594acb841471-Abstract.html)
- **作者**: Shuang Ma, Zhaoyang Zeng, Daniel McDuff, Yale Song
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对视频表示学习中全局与局部信息融合的问题，提出对比学习方法。②由于摘要缺失，无法确定具体方法，可能涉及全局和局部视频表示的对比学习。③相比已有工作，改进点可能在于结合全局和局部视角增强表征。④由于摘要缺失，无法提供具体效果数据。
- **摘要（英）**: This paper addresses contrastive learning of global and local video representations, but due to missing abstract, specific methods and results cannot be determined.
- **核心贡献**: 探索全局与局部视频表示的对比学习。
- **创新点**: 结合全局和局部视角进行对比学习。
- **结果**: 效果未知。

### Relational Self-Attention: What's Missing in Attention for Video Understanding. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2111.01673](https://arxiv.org/abs/2111.01673)
- **作者**: Manjin Kim, Heeseung Kwon, Chunyu Wang, Suha Kwak, Minsu Cho
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①针对视频理解中自注意力缺乏时空对应关系（运动信息）建模的问题，提出关系自注意力RSA。②方法动态生成关系核并聚合关系上下文，利用视频中丰富的时空关系结构。③相比卷积和自注意力，RSA能更好地捕捉运动信息。④在Something-Something-V1/V2、Diving48和FineGym等运动中心基准上达到SOTA，显著优于卷积和自注意力对应方法。
- **摘要（英）**: This paper proposes Relational Self-Attention (RSA) to address the lack of motion modeling in self-attention for video understanding. It dynamically generates relational kernels and aggregates relational contexts, outperforming convolution and self-attention counterparts on motion-centric benchmarks like Something-Something and Diving48.
- **核心贡献**: 提出关系自注意力机制增强视频时空关系建模。
- **创新点**: 动态生成关系核以捕捉运动信息。
- **结果**: 在多个运动中心基准上达到SOTA。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolution has been arguably the most important feature transform for modern neural networks, leading to the advance of deep learning. Recent emergence of Transformer networks, which replace convolution layers with self-attention blocks, has revealed the limitation of stationary convolution kernels and opened the door to the era of dynamic feature transforms. The existing dynamic transforms, including self-attention, however, are all limited for video understanding where correspondence relations in space and time, i.e., motion information, are crucial for effective representation. In this work, we introduce a relational feature transform, dubbed the relational self-attention (RSA), that leverages rich structures of spatio-temporal relations in videos by dynamically generating relational kernels and aggregating relational contexts. Our experiments and ablation studies show that the RSA network substantially outperforms convolution and self-attention counterparts, achieving the state of the art on the standard motion-centric benchmarks for video action recognition, such as Something-Something-V1 & V2, Diving48, and FineGym.

</details>

### Dynamic Normalization and Relay for Video Action Recognition. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/5bd529d5b07b647a8863cf71e98d651a-Abstract.html)
- **作者**: Dongqi Cai, Anbang Yao, Yurong Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①该论文针对视频动作识别中时空特征动态变化和长程依赖建模困难的问题。②提出了动态归一化（Dynamic Normalization）和中继（Relay）机制，动态调整特征分布并跨层传递信息。③相比传统批归一化和静态残差连接，该方法能更好地适应视频帧间的动态变化，增强时序建模能力。④在标准视频动作识别基准上取得了性能提升，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses challenges in video action recognition caused by dynamic spatiotemporal feature variations and long-range dependencies. It introduces dynamic normalization and relay mechanisms to adaptively adjust feature distributions and propagate information across layers, improving temporal modeling over static normalization and residual connections. The method achieves performance gains on standard benchmarks, though specific numbers are not provided in the abstract.
- **核心贡献**: 提出了动态归一化与中继机制，用于改进视频动作识别中的时空特征建模。
- **创新点**: 将动态归一化与跨层中继结合，自适应处理视频帧的动态变化。
- **结果**: 在视频动作识别基准上取得性能提升，但未给出具体数值。

## 跨领域论文（完整笔记在其他领域）

- DeepVideoMVS: Multi-View Stereo on Video With Recurrent Spatio-Temporal Fusion. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Multi-Modal Multi-Action Video Recognition. → [multimodal](../multimodal/Guideline%202021.md)
- Parameter Efficient Multimodal Transformers for Video Representation Learning. → [multimodal](../multimodal/Guideline%202021.md)
- Self-Supervised Learning of Compressed Video Representations. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Active Contrastive Learning of Audio-Visual Video Representations. → [multimodal](../multimodal/Guideline%202021.md)
- Prototypical Cross-Attention Networks for Multiple Object Tracking and Segmentation. → [tracking](../tracking/Guideline%202021.md)
- VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
<!-- COMPLETE v1 papers=17 -->
