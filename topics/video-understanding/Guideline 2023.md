# Video Understanding — 2023 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Understanding Video Scenes through Text: Insights from Text-based Video Question Answering.
- **链接**: [arXiv:2309.01380](https://arxiv.org/abs/2309.01380) · 📚 被引 3
- **作者**: Soumya Jahagirdar, Minesh Mathew, Dimosthenis Karatzas, C. V. Jawahar
- **🏷️ 机构**: IIIT Hyderabad,CVIT,India, Wadhwani AI, UAB,Computer Vision Center,Spain
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper we introduce a rule-based, compositional, and hierarchical modeling of action using Therbligs as our atoms. Introducing these atoms provides us with a consistent, expressive, contact-centered representation of action. Over the atoms we introduce a differentiable method of rule-based reasoning to regularize for logical consistency. Our approach is complementary to other approaches in that the Therblig-based representations produced by our architecture augment rather than replace existing architectures' representations. We release the first Therblig-centered annotations over two popular video datasets - EPIC Kitchens 100 and 50-Salads. We also broadly demonstrate benefits to adopting Therblig representations through evaluation on the following tasks: action segmentation, action anticipation, and action recognition - observing an average 10.5\%/7.53\%/6.5\% relative improvement, respectively, over EPIC Kitchens and an average 8.9\%/6.63\%/4.8\% relative improvement, respectively, over 50 Salads. Code and data will be made publicly available.

</details>

### UniFormerV2: Unlocking the Potential of Image ViTs for Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00157) · 📚 被引 75
- **作者**: Kunchang Li, Yali Wang, Yinan He, Yizhuo Li, Yi Wang, Limin Wang et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Shenzhen Institute of Advanced Technology, Shanghai AI Laboratory, The University of Hong Kong
- **会议**: ICCV 2023

### Verbs in Action: Improving verb understanding in video-language models.
- **链接**: [arXiv:2304.06708](https://arxiv.org/abs/2304.06708) · 📚 被引 54
- **作者**: Liliane Momeni, Mathilde Caron, Arsha Nagrani, Andrew Zisserman, Cordelia Schmid
- **🏷️ 机构**: University of Oxford,Visual Geometry Group,UK, Google Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Effective modeling of complex spatiotemporal dependencies in long-form videos remains an open problem. The recently proposed Structured State-Space Sequence (S4) model with its linear complexity offers a promising direction in this space. However, we demonstrate that treating all image-tokens equally as done by S4 model can adversely affect its efficiency and accuracy. To address this limitation, we present a novel Selective S4 (i.e., S5) model that employs a lightweight mask generator to adaptively select informative image tokens resulting in more efficient and accurate modeling of long-term spatiotemporal dependencies in videos. Unlike previous mask-based token reduction methods used in transformers, our S5 model avoids the dense self-attention calculation by making use of the guidance of the momentum-updated S4 model. This enables our model to efficiently discard less informative tokens and adapt to various long-form video understanding tasks more effectively. However, as is the case for most token reduction methods, the informative image tokens could be dropped incorrectly. To improve the robustness and the temporal horizon of our model, we propose a novel long-short masked contrastive learning (LSMCL) approach that enables our model to predict longer temporal context using shorter input videos. We present extensive comparative results using three challenging long-form video understanding datasets (LVU, COIN and Breakfast), demonstrating that our approach consistently outperforms the previous state-of-the-art S4 model by up to 9.6% accuracy while reducing its memory footprint by 23%.

</details>

### Revisiting Kernel Temporal Segmentation as an Adaptive Tokenizer for Long-form Video Understanding.
- **链接**: [arXiv:2309.11569](https://arxiv.org/abs/2309.11569) · 📚 被引 3
- **作者**: Mohamed Afham, Satya Narayan Shukla, Omid Poursaeed, Pengchuan Zhang, Ashish Shah, Sernam Lim
- **🏷️ 机构**: Meta AI
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our goal is to learn a video representation that is useful for downstream procedure understanding tasks in instructional videos. Due to the small amount of available annotations, a key challenge in procedure understanding is to be able to extract from unlabeled videos the procedural knowledge such as the identity of the task (e.g., 'make latte'), its steps (e.g., 'pour milk'), or the potential next steps given partial progress in its execution. Our main insight is that instructional videos depict sequences of steps that repeat between instances of the same or different tasks, and that this structure can be well represented by a Procedural Knowledge Graph (PKG), where nodes are discrete steps and edges connect steps that occur sequentially in the instructional activities. This graph can then be used to generate pseudo labels to train a video representation that encodes the procedural knowledge in a more accessible form to generalize to multiple procedure understanding tasks. We build a PKG by combining information from a text-based procedural knowledge database and an unlabeled instructional video corpus and then use it to generate training pseudo labels with four novel pre-training objectives. We call this PKG-based pre-training procedure and the resulting model Paprika, Procedure-Aware PRe-training for Instructional Knowledge Acquisition. We evaluate Paprika on COIN and CrossTask for procedure understanding tasks such as task recognition, step recognition, and step forecasting. Paprika yields a video representation that improves over the state of the art: up to 11.23% gains in accuracy in 12 evaluation settings. Implementation is available at https://github.com/salesforce/paprika.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-Supervised Learning can be more beneficial for the video domain compared to images because of its higher annotation cost and dimensionality. Besides, any video understanding task requires reasoning over both spatial and temporal dimensions. In order to learn both the static and motion related features for the semi-supervised action recognition task, existing methods rely on hard input inductive biases like using two-modalities (RGB and Optical-flow) or two-stream of different playback rates. Instead of utilizing unlabeled videos through diverse input streams, we rely on self-supervised video representations, particularly, we utilize temporally-invariant and temporally-distinctive representations. We observe that these representations complement each other depending on the nature of the action. Based on this observation, we propose a student-teacher semi-supervised learning framework, TimeBalance, where we distill the knowledge from a temporally-invariant and a temporally-distinctive teacher. Depending on the nature of the unlabeled video, we dynamically combine the knowledge of these two teachers based on a novel temporal similarity-based reweighting scheme. Our method achieves state-of-the-art performance on three action recognition benchmarks: UCF101, HMDB51, and Kinetics400. Code: https://github.com/DAVEISHAN/TimeBalance

</details>

> Many real-world applications, from sport analysis to surveillance, benefit from automatic long-term action recognition. In the current deep learning paradigm for automatic action recognition, it is imperative that models are trained and tested on datasets and tasks that evaluate if such models actually learn and reason over long-term information. In this work, we propose a method to evaluate how suitable a video dataset is to evaluate models for long-term action recognition. To this end, we define a long-term action as excluding all the videos that can be correctly recognized using solely short-term information. We test this definition on existing long-term classification tasks on three popular real-world datasets, namely Breakfast, CrossTask and LVU, to determine if these datasets are truly evaluating long-term recognition. Our study reveals that these datasets can be effectively solved using shortcuts based on short-term information. Following this finding, we encourage long-term action recognition researchers to make use of datasets that need long-term information to be solved.

</details>

### Video Action Recognition with Attentive Semantic Units.
- **链接**: [arXiv:2303.09756](https://arxiv.org/abs/2303.09756) · 📚 被引 15
- **作者**: Yifei Chen, Dapeng Chen, Ruijin Liu, Hao Li, Wei Peng
- **🏷️ 机构**: IIRC, Huawei, Xi&#x2019;an Jiaotong University, Xiamen University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual-Language Models (VLMs) have significantly advanced action video recognition. Supervised by the semantics of action labels, recent works adapt the visual branch of VLMs to learn video representations. Despite the effectiveness proved by these works, we believe that the potential of VLMs has yet to be fully harnessed. In light of this, we exploit the semantic units (SU) hiding behind the action labels and leverage their correlations with fine-grained items in frames for more accurate action recognition. SUs are entities extracted from the language descriptions of the entire action set, including body parts, objects, scenes, and motions. To further enhance the alignments between visual contents and the SUs, we introduce a multi-region module (MRA) to the visual branch of the VLM. The MRA allows the perception of region-aware visual features beyond the original global feature. Our method adaptively attends to and selects relevant SUs with visual features of frames. With a cross-modal decoder, the selected SUs serve to decode spatiotemporal video representations. In summary, the SUs as the medium can boost discriminative ability and transferability. Specifically, in fully-supervised learning, our method achieved 87.8% top-1 accuracy on Kinetics-400. In K=2 few-shot experiments, our method surpassed the previous state-of-the-art by +7.1% and +15.0% on HMDB-51 and UCF-101, respectively.

</details>

### Video-FocalNets: Spatio-Temporal Focal Modulation for Video Action Recognition.
- **链接**: [arXiv:2307.06947](https://arxiv.org/abs/2307.06947) · [代码](https://github.com/TalalWasim/Video-FocalNets) · 📚 被引 37
- **作者**: Syed Talal Wasim, Muhammad Uzair Khattak, Muzammal Naseer, Salman Khan, Mubarak Shah, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI, University of Central Florida
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent video recognition models utilize Transformer models for long-range spatio-temporal context modeling. Video transformer designs are based on self-attention that can model global context at a high computational cost. In comparison, convolutional designs for videos offer an efficient alternative but lack long-range dependency modeling. Towards achieving the best of both designs, this work proposes Video-FocalNet, an effective and efficient architecture for video recognition that models both local and global contexts. Video-FocalNet is based on a spatio-temporal focal modulation architecture that reverses the interaction and aggregation steps of self-attention for better efficiency. Further, the aggregation step and the interaction step are both implemented using efficient convolution and element-wise multiplication operations that are computationally less expensive than their self-attention counterparts on video representations. We extensively explore the design space of focal modulation-based spatio-temporal context modeling and demonstrate our parallel spatial and temporal encoding design to be the optimal choice. Video-FocalNets perform favorably well against the state-of-the-art transformer-based models for video recognition on five large-scale datasets (Kinetics-400, Kinetics-600, SS-v2, Diving-48, and ActivityNet-1.3) at a lower computational cost. Our code/models are released at https://github.com/TalalWasim/Video-FocalNets.

</details>

### JEDI: Joint Expert Distillation in a Semi-Supervised Multi-Dataset Student-Teacher Scenario for Video Action Recognition.
- **链接**: [arXiv:2308.04934](https://arxiv.org/abs/2308.04934) · 📚 被引 2
- **作者**: Lucian Bicsi, Bogdan Alexe, Radu Tudor Ionescu, Marius Leordeanu
- **🏷️ 机构**: University of Bucharest, Politehnica University of Bucharest
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose JEDI, a multi-dataset semi-supervised learning method, which efficiently combines knowledge from multiple experts, learned on different datasets, to train and improve the performance of individual, per dataset, student models. Our approach achieves this by addressing two important problems in current machine learning research: generalization across datasets and limitations of supervised training due to scarcity of labeled data. We start with an arbitrary number of experts, pretrained on their own specific dataset, which form the initial set of student models. The teachers are immediately derived by concatenating the feature representations from the penultimate layers of the students. We then train all models in a student-teacher semi-supervised learning scenario until convergence. In our efficient approach, student-teacher training is carried out jointly and end-to-end, showing that both students and teachers improve their generalization capacity during training. We validate our approach on four video action recognition datasets. By simultaneously considering all datasets within a unified semi-supervised setting, we demonstrate significant improvements over the initial experts.

</details>

### Video Action Recognition with Adaptive Zooming Using Motion Residuals.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00131) · 📚 被引 2
- **作者**: Mostafa Shahabinejad, Irina Kezele, Seyed Shahabeddin Nabavi, Wentao Liu, Seel Patel, Yuanhao Yu et al.
- **🏷️ 机构**: Huawei Technologies,Noah&#x2019;s Ark Laboratories,Markham,Ontario,Canada, Concordia University,Montreal,Quebec,Canada
- **会议**: ICCV 2023

### Video BagNet: short temporal receptive fields increase robustness in long-term action recognition.
- **链接**: [arXiv:2308.11249](https://arxiv.org/abs/2308.11249) · 📚 被引 2
- **作者**: Ombretta Strafforello, Xin Liu, Klamer Schutte, Jan van Gemert
- **🏷️ 机构**: Delft University of Technology, TNO
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous work on long-term video action recognition relies on deep 3D-convolutional models that have a large temporal receptive field (RF). We argue that these models are not always the best choice for temporal modeling in videos. A large temporal receptive field allows the model to encode the exact sub-action order of a video, which causes a performance decrease when testing videos have a different sub-action order. In this work, we investigate whether we can improve the model robustness to the sub-action order by shrinking the temporal receptive field of action recognition models. For this, we design Video BagNet, a variant of the 3D ResNet-50 model with the temporal receptive field size limited to 1, 9, 17 or 33 frames. We analyze Video BagNet on synthetic and real-world video datasets and experimentally compare models with varying temporal receptive fields. We find that short receptive fields are robust to sub-action order changes, while larger temporal receptive fields are sensitive to the sub-action order.

</details>

### Dual Learning with Dynamic Knowledge Distillation for Partially Relevant Video Retrieval.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01038) · 📚 被引 29
- **作者**: Jianfeng Dong, Minsong Zhang, Zheng Zhang, Xianke Chen, Daizong Liu, Xiaoye Qu et al.
- **🏷️ 机构**: Zhejiang Gongshang University, Peking University, Huazhong University of Science and Technology
- **会议**: ICCV 2023

</details>

- Multimodal Motion Conditioned Diffusion Model for Skeleton-based Video Anomaly Detection. → [multimodal](../multimodal/Guideline%202023.md)
- MEGA: Multimodal Alignment Aggregation and Distillation For Cinematic Video Segmentation. → [multimodal](../multimodal/Guideline%202023.md)
- TeD-SPAD: Temporal Distinctiveness for Self-supervised Privacy-preservation for video Anomaly Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
