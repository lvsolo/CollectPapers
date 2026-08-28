# Video Understanding — 2023 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Collaborative Static and Dynamic Vision-Language Streams for Spatio-Temporal Video Grounding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02212) · 📚 被引 22
- **作者**: Zihang Lin, Chaolei Tan, Jian-Fang Hu, Zhi Jin, Tiancai Ye, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,China, Tencent,China
- **会议**: CVPR 2023

### Therbligs in Action: Video Understanding through Motion Primitives.
- **链接**: [arXiv:2304.03631](https://arxiv.org/abs/2304.03631) · 📚 被引 10
- **作者**: Eadom Dessalene, Michael Maynord, Cornelia Fermüller, Yiannis Aloimonos
- **🏷️ 机构**: University of Maryland, College Park,College Park,MD,USA,20742
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper we introduce a rule-based, compositional, and hierarchical modeling of action using Therbligs as our atoms. Introducing these atoms provides us with a consistent, expressive, contact-centered representation of action. Over the atoms we introduce a differentiable method of rule-based reasoning to regularize for logical consistency. Our approach is complementary to other approaches in that the Therblig-based representations produced by our architecture augment rather than replace existing architectures' representations. We release the first Therblig-centered annotations over two popular video datasets - EPIC Kitchens 100 and 50-Salads. We also broadly demonstrate benefits to adopting Therblig representations through evaluation on the following tasks: action segmentation, action anticipation, and action recognition - observing an average 10.5\%/7.53\%/6.5\% relative improvement, respectively, over EPIC Kitchens and an average 8.9\%/6.63\%/4.8\% relative improvement, respectively, over 50 Salads. Code and data will be made publicly available.

</details>

### System-Status-Aware Adaptive Network for Online Streaming Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01013) · 📚 被引 8
- **作者**: Lin Geng Foo, Jia Gong, Zhipeng Fan, Jun Liu
- **🏷️ 机构**: Singapore University of Technology and Design, New York University
- **会议**: CVPR 2023

### LAVENDER: Unifying Video-Language Understanding as Masked Language Modeling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02214) · 📚 被引 53
- **作者**: Linjie Li, Zhe Gan, Kevin Lin, Chung-Ching Lin, Zicheng Liu, Ce Liu et al.
- **🏷️ 机构**: Microsoft
- **会议**: CVPR 2023

### Selective Structured State-Spaces for Long-Form Video Understanding.
- **链接**: [arXiv:2303.14526](https://arxiv.org/abs/2303.14526) · 📚 被引 116
- **作者**: Jue Wang, Wentao Zhu, Pichao Wang, Xiang Yu, Linda Liu, Mohamed Omar et al.
- **🏷️ 机构**: Amazon Prime Video
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Effective modeling of complex spatiotemporal dependencies in long-form videos remains an open problem. The recently proposed Structured State-Space Sequence (S4) model with its linear complexity offers a promising direction in this space. However, we demonstrate that treating all image-tokens equally as done by S4 model can adversely affect its efficiency and accuracy. To address this limitation, we present a novel Selective S4 (i.e., S5) model that employs a lightweight mask generator to adaptively select informative image tokens resulting in more efficient and accurate modeling of long-term spatiotemporal dependencies in videos. Unlike previous mask-based token reduction methods used in transformers, our S5 model avoids the dense self-attention calculation by making use of the guidance of the momentum-updated S4 model. This enables our model to efficiently discard less informative tokens and adapt to various long-form video understanding tasks more effectively. However, as is the case for most token reduction methods, the informative image tokens could be dropped incorrectly. To improve the robustness and the temporal horizon of our model, we propose a novel long-short masked contrastive learning (LSMCL) approach that enables our model to predict longer temporal context using shorter input videos. We present extensive comparative results using three challenging long-form video understanding datasets (LVU, COIN and Breakfast), demonstrating that our approach consistently outperforms the previous state-of-the-art S4 model by up to 9.6% accuracy while reducing its memory footprint by 23%.

</details>

### Procedure-Aware Pretraining for Instructional Video Understanding.
- **链接**: [arXiv:2303.18230](https://arxiv.org/abs/2303.18230) · [代码](https://github.com/salesforce/paprika) · 📚 被引 38
- **作者**: Honglu Zhou, Roberto Martín-Martín, Mubbasir Kapadia, Silvio Savarese, Juan Carlos Niebles
- **🏷️ 机构**: Salesforce Research, Rutgers University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our goal is to learn a video representation that is useful for downstream procedure understanding tasks in instructional videos. Due to the small amount of available annotations, a key challenge in procedure understanding is to be able to extract from unlabeled videos the procedural knowledge such as the identity of the task (e.g., 'make latte'), its steps (e.g., 'pour milk'), or the potential next steps given partial progress in its execution. Our main insight is that instructional videos depict sequences of steps that repeat between instances of the same or different tasks, and that this structure can be well represented by a Procedural Knowledge Graph (PKG), where nodes are discrete steps and edges connect steps that occur sequentially in the instructional activities. This graph can then be used to generate pseudo labels to train a video representation that encodes the procedural knowledge in a more accessible form to generalize to multiple procedure understanding tasks. We build a PKG by combining information from a text-based procedural knowledge database and an unlabeled instructional video corpus and then use it to generate training pseudo labels with four novel pre-training objectives. We call this PKG-based pre-training procedure and the resulting model Paprika, Procedure-Aware PRe-training for Instructional Knowledge Acquisition. We evaluate Paprika on COIN and CrossTask for procedure understanding tasks such as task recognition, step recognition, and step forecasting. Paprika yields a video representation that improves over the state of the art: up to 11.23% gains in accuracy in 12 evaluation settings. Implementation is available at https://github.com/salesforce/paprika.

</details>

### TimeBalance: Temporally-Invariant and Temporally-Distinctive Video Representations for Semi-Supervised Action Recognition.
- **链接**: [arXiv:2303.16268](https://arxiv.org/abs/2303.16268) · [代码](https://github.com/DAVEISHAN/TimeBalance) · 📚 被引 17
- **作者**: Ishan Rajendrakumar Dave, Mamshad Nayeem Rizve, Chen Chen, Mubarak Shah
- **🏷️ 机构**: Center for Research in Computer Vision, University of Central Florida,Orlando,USA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-Supervised Learning can be more beneficial for the video domain compared to images because of its higher annotation cost and dimensionality. Besides, any video understanding task requires reasoning over both spatial and temporal dimensions. In order to learn both the static and motion related features for the semi-supervised action recognition task, existing methods rely on hard input inductive biases like using two-modalities (RGB and Optical-flow) or two-stream of different playback rates. Instead of utilizing unlabeled videos through diverse input streams, we rely on self-supervised video representations, particularly, we utilize temporally-invariant and temporally-distinctive representations. We observe that these representations complement each other depending on the nature of the action. Based on this observation, we propose a student-teacher semi-supervised learning framework, TimeBalance, where we distill the knowledge from a temporally-invariant and a temporally-distinctive teacher. Depending on the nature of the unlabeled video, we dynamically combine the knowledge of these two teachers based on a novel temporal similarity-based reweighting scheme. Our method achieves state-of-the-art performance on three action recognition benchmarks: UCF101, HMDB51, and Kinetics400. Code: https://github.com/DAVEISHAN/TimeBalance

</details>

### Video Test-Time Adaptation for Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02198)
- **作者**: Wei Lin, Muhammad Jehanzeb Mirza, Mateusz Kozinski, Horst Possegger, Hilde Kuehne, Horst Bischof
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### A Large-Scale Robustness Analysis of Video Action Recognition Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01412) · 📚 被引 29
- **作者**: Madeline Chantry Schiappa, Naman Biyani, Prudvi Kamtam, Shruti Vyas, Hamid Palangi, Vibhav Vineet et al.
- **🏷️ 机构**: University of Central Florida,CRCV, IIT Kanpur, Microsoft Research
- **会议**: CVPR 2023

### SVFormer: Semi-supervised Video Transformer for Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01804) · 📚 被引 109
- **作者**: Zhen Xing, Qi Dai, Han Hu, Jingjing Chen, Zuxuan Wu, Yu-Gang Jiang
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Microsoft Research Asia
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models. → [multimodal](../multimodal/Guideline%202023.md)
- Discovering the Real Association: Multimodal Causal Reasoning in Video Question Answering. → [multimodal](../multimodal/Guideline%202023.md)
- Spatio-Temporal Pixel-Level Contrastive Learning-based Source-Free Domain Adaptation for Video Semantic Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Ultrahigh Resolution Image/Video Matting with Spatio-Temporal Sparsity. → [network-pruning](../network-pruning/Guideline%202023.md)
- Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
