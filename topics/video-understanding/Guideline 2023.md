# Video Understanding — 2023 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Collaborative Static and Dynamic Vision-Language Streams for Spatio-Temporal Video Grounding. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02212) · 📚 被引 22
- **作者**: Zihang Lin, Chaolei Tan, Jian-Fang Hu, Zhi Jin, Tiancai Ye, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,China, Tencent,China
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视频时空定位中静态与动态信息融合不足的问题。②提出协作式静态与动态视觉-语言流方法，通过双流架构分别处理静态场景和动态动作信息，并融合文本特征进行时空定位。③相比单流或简单拼接方法，显式建模静态与动态语义的互补性。④摘要未提供具体数据，但方法设计具有合理性。
- **摘要（英）**: This paper addresses the issue of insufficient integration of static and dynamic information in spatio-temporal video grounding. It proposes a collaborative static and dynamic vision-language stream method that processes static scenes and dynamic actions separately and fuses them with text features. Compared to single-stream or simple concatenation approaches, it explicitly models the complementarity of static and dynamic semantics. The abstract lacks specific quantitative results.
- **核心贡献**: 提出静态与动态视觉-语言双流协作框架用于视频时空定位。
- **创新点**: 显式分离并融合静态与动态语义信息。
- **结果**: 未报告具体性能数据。

### Therbligs in Action: Video Understanding through Motion Primitives. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2304.03631](https://arxiv.org/abs/2304.03631) · 📚 被引 10
- **作者**: Eadom Dessalene, Michael Maynord, Cornelia Fermüller, Yiannis Aloimonos
- **🏷️ 机构**: University of Maryland, College Park,College Park,MD,USA,20742
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视频理解中动作表示缺乏一致性和可解释性的问题。②提出基于Therbligs（动作基元）的规则化组合层次化动作建模，并发布两个数据集的动作基元标注。③相比现有方法，提供接触中心的表示和可微规则推理，增强逻辑一致性。④在动作分割、预测和识别任务上，EPIC Kitchens上相对提升10.5%/7.53%/6.5%，50 Salads上提升8.9%/6.63%/4.8%。
- **摘要（英）**: This paper addresses the lack of consistency and interpretability in action representations for video understanding. It introduces a rule-based, compositional, hierarchical action model using Therbligs as atoms, with differentiable rule-based reasoning. Compared to existing methods, it provides a contact-centered representation and releases Therblig annotations for two datasets. It achieves average relative improvements of 10.5%/7.53%/6.5% on EPIC Kitchens and 8.9%/6.63%/4.8% on 50 Salads across tasks.
- **核心贡献**: 提出Therbligs动作基元表示并发布标注数据集。
- **创新点**: 将工业工程中的Therbligs引入视频理解。
- **结果**: 在多个任务上取得显著相对提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper we introduce a rule-based, compositional, and hierarchical modeling of action using Therbligs as our atoms. Introducing these atoms provides us with a consistent, expressive, contact-centered representation of action. Over the atoms we introduce a differentiable method of rule-based reasoning to regularize for logical consistency. Our approach is complementary to other approaches in that the Therblig-based representations produced by our architecture augment rather than replace existing architectures' representations. We release the first Therblig-centered annotations over two popular video datasets - EPIC Kitchens 100 and 50-Salads. We also broadly demonstrate benefits to adopting Therblig representations through evaluation on the following tasks: action segmentation, action anticipation, and action recognition - observing an average 10.5\%/7.53\%/6.5\% relative improvement, respectively, over EPIC Kitchens and an average 8.9\%/6.63\%/4.8\% relative improvement, respectively, over 50 Salads. Code and data will be made publicly available.

</details>

### System-Status-Aware Adaptive Network for Online Streaming Video Understanding. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01013) · 📚 被引 8
- **作者**: Lin Geng Foo, Jia Gong, Zhipeng Fan, Jun Liu
- **🏷️ 机构**: Singapore University of Technology and Design, New York University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对在线流式视频理解中系统状态感知不足的问题。②提出系统状态感知的自适应网络，根据系统资源动态调整处理策略。③相比固定架构，提高资源利用效率和实时性。④摘要未提供具体数据。
- **摘要（英）**: This paper addresses the lack of system-status awareness in online streaming video understanding. It proposes a system-status-aware adaptive network that adjusts processing based on system resources. Compared to fixed architectures, it improves resource efficiency and real-time performance. The abstract lacks quantitative results.
- **核心贡献**: 提出系统状态感知的自适应网络用于在线视频理解。
- **创新点**: 动态调整网络策略以适应系统状态。
- **结果**: 未报告具体性能数据。

### LAVENDER: Unifying Video-Language Understanding as Masked Language Modeling. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02214) · 📚 被引 53
- **作者**: Linjie Li, Zhe Gan, Kevin Lin, Chung-Ching Lin, Zicheng Liu, Ce Liu et al.
- **🏷️ 机构**: Microsoft
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视频-语言理解任务中不同任务需要不同模型架构、缺乏统一框架的问题。②提出了LAVENDER，将视频-语言理解统一为掩码语言建模（MLM）任务，通过掩码语言建模和匹配机制，结合视频和文本输入，实现多任务学习。③相比以往方法，LAVENDER使用统一的MLM框架，简化了任务特定设计，并利用大规模预训练提升泛化能力。④在多个视频-语言基准上取得了领先性能，如视频问答和文本检索任务，展示了统一框架的有效性。
- **摘要（英）**: This paper addresses the lack of a unified framework for video-language understanding tasks. LAVENDER unifies these tasks as masked language modeling, enabling multi-task learning with a single architecture. It achieves state-of-the-art results on multiple benchmarks, demonstrating improved generalization.
- **核心贡献**: 提出LAVENDER，统一视频-语言理解为掩码语言建模。
- **创新点**: 使用MLM作为统一任务，减少任务特定架构。
- **结果**: 在多个基准上取得领先性能。

### Selective Structured State-Spaces for Long-Form Video Understanding. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2303.14526](https://arxiv.org/abs/2303.14526) · 📚 被引 116
- **作者**: Jue Wang, Wentao Zhu, Pichao Wang, Xiang Yu, Linda Liu, Mohamed Omar et al.
- **🏷️ 机构**: Amazon Prime Video
- **会议**: CVPR 2023
- **摘要（中）**: ①针对长视频理解中S4模型对所有图像令牌平等处理导致效率低和精度差的问题。②提出了选择性状态空间模型S5，通过轻量掩码生成器自适应选择信息丰富的图像令牌，并利用动量更新的S4模型指导令牌丢弃，避免密集自注意力计算。③相比S4和基于掩码的Transformer方法，S5更高效地建模长时时空依赖，并引入长-短掩码对比机制提升鲁棒性。④在长视频理解任务上，S5在效率和精度上均优于现有方法，尤其在处理长序列时表现突出。
- **摘要（英）**: This paper tackles the inefficiency of S4 models in long-form video understanding by treating all tokens equally. The proposed S5 model uses a lightweight mask generator to select informative tokens, guided by a momentum-updated S4, improving efficiency and accuracy. It outperforms existing methods on long-video tasks.
- **核心贡献**: 提出选择性状态空间模型S5，优化长视频令牌选择。
- **创新点**: 结合掩码生成和动量更新，避免密集注意力。
- **结果**: 在长视频任务上提升效率和精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Effective modeling of complex spatiotemporal dependencies in long-form videos remains an open problem. The recently proposed Structured State-Space Sequence (S4) model with its linear complexity offers a promising direction in this space. However, we demonstrate that treating all image-tokens equally as done by S4 model can adversely affect its efficiency and accuracy. To address this limitation, we present a novel Selective S4 (i.e., S5) model that employs a lightweight mask generator to adaptively select informative image tokens resulting in more efficient and accurate modeling of long-term spatiotemporal dependencies in videos. Unlike previous mask-based token reduction methods used in transformers, our S5 model avoids the dense self-attention calculation by making use of the guidance of the momentum-updated S4 model. This enables our model to efficiently discard less informative tokens and adapt to various long-form video understanding tasks more effectively. However, as is the case for most token reduction methods, the informative image tokens could be dropped incorrectly. To improve the robustness and the temporal horizon of our model, we propose a novel long-short masked contrastive learning (LSMCL) approach that enables our model to predict longer temporal context using shorter input videos. We present extensive comparative results using three challenging long-form video understanding datasets (LVU, COIN and Breakfast), demonstrating that our approach consistently outperforms the previous state-of-the-art S4 model by up to 9.6% accuracy while reducing its memory footprint by 23%.

</details>

### Procedure-Aware Pretraining for Instructional Video Understanding. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2303.18230](https://arxiv.org/abs/2303.18230) · 📚 被引 38
- **作者**: Honglu Zhou, Roberto Martín-Martín, Mubbasir Kapadia, Silvio Savarese, Juan Carlos Niebles
- **🏷️ 机构**: Salesforce Research, Rutgers University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对教学视频中程序理解任务标注少、难以提取程序性知识的问题。②提出了程序感知预训练方法，构建程序知识图（PKG）表示步骤序列，并利用其生成伪标签训练视频表示。③相比传统预训练，PKG结合文本数据库和未标注视频，生成四种预训练任务，增强对任务身份、步骤和下一步预测的编码。④在多个下游程序理解任务上，该方法显著提升了性能，尤其在步骤识别和任务分类上。
- **摘要（英）**: This paper addresses the challenge of limited annotations in instructional video understanding. It introduces a procedure-aware pretraining method using a Procedural Knowledge Graph to generate pseudo-labels, enhancing video representations. The approach improves performance on multiple downstream tasks.
- **核心贡献**: 提出程序感知预训练，利用PKG生成伪标签。
- **创新点**: 结合文本知识库和视频构建PKG。
- **结果**: 在程序理解任务上显著提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our goal is to learn a video representation that is useful for downstream procedure understanding tasks in instructional videos. Due to the small amount of available annotations, a key challenge in procedure understanding is to be able to extract from unlabeled videos the procedural knowledge such as the identity of the task (e.g., 'make latte'), its steps (e.g., 'pour milk'), or the potential next steps given partial progress in its execution. Our main insight is that instructional videos depict sequences of steps that repeat between instances of the same or different tasks, and that this structure can be well represented by a Procedural Knowledge Graph (PKG), where nodes are discrete steps and edges connect steps that occur sequentially in the instructional activities. This graph can then be used to generate pseudo labels to train a video representation that encodes the procedural knowledge in a more accessible form to generalize to multiple procedure understanding tasks. We build a PKG by combining information from a text-based procedural knowledge database and an unlabeled instructional video corpus and then use it to generate training pseudo labels with four novel pre-training objectives. We call this PKG-based pre-training procedure and the resulting model Paprika, Procedure-Aware PRe-training for Instructional Knowledge Acquisition. We evaluate Paprika on COIN and CrossTask for procedure understanding tasks such as task recognition, step recognition, and step forecasting. Paprika yields a video representation that improves over the state of the art: up to 11.23% gains in accuracy in 12 evaluation settings. Implementation is available at https://github.com/salesforce/paprika.

</details>

### TimeBalance: Temporally-Invariant and Temporally-Distinctive Video Representations for Semi-Supervised Action Recognition. **⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2303.16268](https://arxiv.org/abs/2303.16268) · 📚 被引 17
- **作者**: Ishan Rajendrakumar Dave, Mamshad Nayeem Rizve, Chen Chen, Mubarak Shah
- **🏷️ 机构**: Center for Research in Computer Vision, University of Central Florida,Orlando,USA
- **会议**: CVPR 2023
- **摘要（中）**: ①针对半监督动作识别中依赖多模态或双流输入的问题。②提出了TimeBalance框架，利用自监督的时间不变和时间区分表示，通过师生学习动态组合两个教师的知识，基于时间相似性重加权。③相比现有方法，TimeBalance无需额外输入流，仅利用自监督表示，适应不同动作类型。④在多个半监督动作识别基准上，TimeBalance取得了优于现有方法的性能，尤其在标注数据少时。
- **摘要（英）**: This paper addresses the reliance on multi-modal inputs in semi-supervised action recognition. TimeBalance distills knowledge from temporally-invariant and distinctive teachers with a reweighting scheme, improving performance. It achieves state-of-the-art results on benchmarks.
- **核心贡献**: 提出TimeBalance框架，动态组合时间表示。
- **创新点**: 基于时间相似性重加权教师知识。
- **结果**: 在半监督动作识别上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-Supervised Learning can be more beneficial for the video domain compared to images because of its higher annotation cost and dimensionality. Besides, any video understanding task requires reasoning over both spatial and temporal dimensions. In order to learn both the static and motion related features for the semi-supervised action recognition task, existing methods rely on hard input inductive biases like using two-modalities (RGB and Optical-flow) or two-stream of different playback rates. Instead of utilizing unlabeled videos through diverse input streams, we rely on self-supervised video representations, particularly, we utilize temporally-invariant and temporally-distinctive representations. We observe that these representations complement each other depending on the nature of the action. Based on this observation, we propose a student-teacher semi-supervised learning framework, TimeBalance, where we distill the knowledge from a temporally-invariant and a temporally-distinctive teacher. Depending on the nature of the unlabeled video, we dynamically combine the knowledge of these two teachers based on a novel temporal similarity-based reweighting scheme. Our method achieves state-of-the-art performance on three action recognition benchmarks: UCF101, HMDB51, and Kinetics400. Code: https://github.com/DAVEISHAN/TimeBalance

</details>

### Video Test-Time Adaptation for Action Recognition. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02198)
- **作者**: Wei Lin, Muhammad Jehanzeb Mirza, Mateusz Kozinski, Horst Possegger, Hilde Kuehne, Horst Bischof
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视频动作识别模型在测试时遇到分布偏移（如光照、视角变化）导致性能下降的问题。②提出了一种视频测试时自适应方法，在推理阶段利用未标注测试数据动态调整模型参数。③相比静态模型，该方法无需重新训练即可适应新环境，且针对视频时序特性设计了自适应策略。④实验表明在多个动作识别基准上显著提升了鲁棒性，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses performance degradation of video action recognition models under distribution shift at test time. It proposes a test-time adaptation method that adjusts model parameters using unlabeled test data, leveraging temporal characteristics. Compared to static models, it adapts without retraining, showing improved robustness on benchmarks, though specific numbers are absent.
- **核心贡献**: 提出视频动作识别的测试时自适应框架。
- **创新点**: 利用视频时序信息进行测试时参数调整。
- **结果**: 在基准上提升鲁棒性，具体数据未给出。

### A Large-Scale Robustness Analysis of Video Action Recognition Models. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01412) · 📚 被引 29
- **作者**: Madeline Chantry Schiappa, Naman Biyani, Prudvi Kamtam, Shruti Vyas, Hamid Palangi, Vibhav Vineet et al.
- **🏷️ 机构**: University of Central Florida,CRCV, IIT Kanpur, Microsoft Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视频动作识别模型在真实世界扰动下鲁棒性评估不足的问题。②进行了大规模鲁棒性分析，系统测试多种模型在各类扰动（如噪声、模糊）下的表现。③相比以往小规模评估，提供了更全面的基准和洞察。④发现现有模型对特定扰动敏感，但摘要未提供具体性能数据。
- **摘要（英）**: This paper addresses the lack of comprehensive robustness evaluation for video action recognition models under real-world perturbations. It conducts a large-scale analysis testing various models against multiple disturbances, providing a broader benchmark than prior work. Findings reveal sensitivity to certain perturbations, though specific results are not detailed.
- **核心贡献**: 构建大规模视频动作识别鲁棒性评估基准。
- **创新点**: 系统化分析多种扰动对模型的影响。
- **结果**: 揭示模型脆弱性，具体数据未提供。

### SVFormer: Semi-supervised Video Transformer for Action Recognition. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01804) · 📚 被引 109
- **作者**: Zhen Xing, Qi Dai, Han Hu, Jingjing Chen, Zuxuan Wu, Yu-Gang Jiang
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Microsoft Research Asia
- **会议**: CVPR 2023
- **摘要（中）**: ①针对视频Transformer在半监督动作识别中利用未标注数据不足的问题。②提出SVFormer，采用半监督学习策略，结合伪标签和一致性正则化训练视频Transformer。③相比现有半监督方法，设计了针对视频时空特性的增强和损失函数。④在多个基准上显著提升性能，尤其在低标注比例下，但摘要未给出具体数值。
- **摘要（英）**: This paper tackles insufficient use of unlabeled data in semi-supervised video action recognition with transformers. It proposes SVFormer, combining pseudo-labeling and consistency regularization tailored for video spatiotemporal features. Compared to existing methods, it improves performance significantly, especially with scarce labels, though exact numbers are omitted.
- **核心贡献**: 提出半监督视频Transformer框架SVFormer。
- **创新点**: 结合时空增强和一致性正则化。
- **结果**: 在低标注比例下显著提升性能。

### Understanding Video Scenes through Text: Insights from Text-based Video Question Answering. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2309.01380](https://arxiv.org/abs/2309.01380) · 📚 被引 3
- **作者**: Soumya Jahagirdar, Minesh Mathew, Dimosthenis Karatzas, C. V. Jawahar
- **🏷️ 机构**: IIIT Hyderabad,CVIT,India, Wadhwani AI, UAB,Computer Vision Center,Spain
- **会议**: ICCV 2023
- **摘要（中）**: ①该论文针对视频问答中文本理解的重要性问题，分析了NewsVideoQA和M4-ViteVQA两个数据集。②通过多层级分析数据集构建，并实验了仅文本模型BERT-QA。③发现BERT-QA在两个数据集上表现与原始方法相当，揭示了数据集构建的不足。④实验表明当前数据集可能过度依赖文本线索，缺乏对视觉和多帧理解的充分要求。
- **摘要（英）**: This paper analyzes two text-based video QA datasets, NewsVideoQA and M4-ViteVQA, revealing that a text-only model (BERT-QA) achieves comparable performance to original methods. The findings highlight shortcomings in dataset formulation, suggesting insufficient emphasis on visual and multi-frame understanding. This work provides critical insights for improving video QA benchmarks.
- **核心贡献**: 揭示了文本在视频QA数据集中的主导作用，指出数据集构建缺陷。
- **创新点**: 通过仅文本模型对比分析数据集质量。
- **结果**: BERT-QA性能与原始方法相当，表明数据集文本偏差。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Researchers have extensively studied the field of vision and language, discovering that both visual and textual content is crucial for understanding scenes effectively. Particularly, comprehending text in videos holds great significance, requiring both scene text understanding and temporal reasoning. This paper focuses on exploring two recently introduced datasets, NewsVideoQA and M4-ViteVQA, which aim to address video question answering based on textual content. The NewsVideoQA dataset contains question-answer pairs related to the text in news videos, while M4-ViteVQA comprises question-answer pairs from diverse categories like vlogging, traveling, and shopping. We provide an analysis of the formulation of these datasets on various levels, exploring the degree of visual understanding and multi-frame comprehension required for answering the questions. Additionally, the study includes experimentation with BERT-QA, a text-only model, which demonstrates comparable performance to the original methods on both datasets, indicating the shortcomings in the formulation of these datasets. Furthermore, we also look into the domain adaptation aspect by examining the effectiveness of training on M4-ViteVQA and evaluating on NewsVideoQA and vice-versa, thereby shedding light on the challenges and potential benefits of out-of-domain training.

</details>

### UniFormerV2: Unlocking the Potential of Image ViTs for Video Understanding. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00157) · 📚 被引 75
- **作者**: Kunchang Li, Yali Wang, Yinan He, Yizhuo Li, Yi Wang, Limin Wang et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Shenzhen Institute of Advanced Technology, Shanghai AI Laboratory, The University of Hong Kong
- **会议**: ICCV 2023
- **摘要（中）**: ①该论文针对视频理解中图像ViT迁移效率低的问题，提出了UniFormerV2框架。②方法通过解耦时空注意力，将图像ViT（如ViT-B/L）有效适配到视频任务，并引入局部-全局联合建模。③相比已有工作，UniFormerV2在保持高效的同时，显著提升视频表示能力，支持多尺度特征融合。④在Kinetics-400/600、Something-Something V1/V2等基准上达到SOTA，例如K400上top-1准确率超过90%，且推理速度优于同类方法。
- **摘要（英）**: UniFormerV2 unlocks the potential of image ViTs for video understanding by decoupling spatial-temporal attention and enabling efficient adaptation. It achieves state-of-the-art results on major benchmarks like Kinetics-400/600 and Something-Something, with top-1 accuracy exceeding 90% on K400 while maintaining high inference efficiency. The framework demonstrates strong generalization and scalability across diverse video tasks.
- **核心贡献**: 提出UniFormerV2，高效利用图像ViT实现视频理解SOTA。
- **创新点**: 解耦时空注意力并联合局部-全局建模，提升ViT视频适配能力。
- **结果**: 在多个视频基准上达到SOTA，K400准确率超90%。

### Verbs in Action: Improving verb understanding in video-language models.
- **链接**: [arXiv:2304.06708](https://arxiv.org/abs/2304.06708) · 📚 被引 54
- **作者**: Liliane Momeni, Mathilde Caron, Arsha Nagrani, Andrew Zisserman, Cordelia Schmid
- **🏷️ 机构**: University of Oxford,Visual Geometry Group,UK, Google Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding verbs is crucial to modelling how people and objects interact with each other and the environment through space and time. Recently, state-of-the-art video-language models based on CLIP have been shown to have limited verb understanding and to rely extensively on nouns, restricting their performance in real-world video applications that require action and temporal understanding. In this work, we improve verb understanding for CLIP-based video-language models by proposing a new Verb-Focused Contrastive (VFC) framework. This consists of two main components: (1) leveraging pretrained large language models (LLMs) to create hard negatives for cross-modal contrastive learning, together with a calibration strategy to balance the occurrence of concepts in positive and negative pairs; and (2) enforcing a fine-grained, verb phrase alignment loss. Our method achieves state-of-the-art results for zero-shot performance on three downstream tasks that focus on verb understanding: video-text matching, video question-answering and video classification. To the best of our knowledge, this is the first work which proposes a method to alleviate the verb understanding problem, and does not simply highlight it.

</details>

### Revisiting Kernel Temporal Segmentation as an Adaptive Tokenizer for Long-form Video Understanding.
- **链接**: [arXiv:2309.11569](https://arxiv.org/abs/2309.11569) · 📚 被引 3
- **作者**: Mohamed Afham, Satya Narayan Shukla, Omid Poursaeed, Pengchuan Zhang, Ashish Shah, Sernam Lim
- **🏷️ 机构**: Meta AI
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While most modern video understanding models operate on short-range clips, real-world videos are often several minutes long with semantically consistent segments of variable length. A common approach to process long videos is applying a short-form video model over uniformly sampled clips of fixed temporal length and aggregating the outputs. This approach neglects the underlying nature of long videos since fixed-length clips are often redundant or uninformative. In this paper, we aim to provide a generic and adaptive sampling approach for long-form videos in lieu of the de facto uniform sampling. Viewing videos as semantically consistent segments, we formulate a task-agnostic, unsupervised, and scalable approach based on Kernel Temporal Segmentation (KTS) for sampling and tokenizing long videos. We evaluate our method on long-form video understanding tasks such as video classification and temporal action localization, showing consistent gains over existing approaches and achieving state-of-the-art performance on long-form video modeling.

</details>

### Are current long-term video understanding datasets long-term?
- **链接**: [arXiv:2308.11244](https://arxiv.org/abs/2308.11244) · 📚 被引 2
- **作者**: Ombretta Strafforello, Klamer Schutte, Jan C. van Gemert
- **🏷️ 机构**: TU Delft, TNO, TNO, TU Delft
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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

### Multimodal Distillation for Egocentric Action Recognition.
- **链接**: [arXiv:2307.07483](https://arxiv.org/abs/2307.07483) · 📚 被引 36
- **作者**: Gorjan Radevski, Dusan Grujicic, Matthew B. Blaschko, Marie-Francine Moens, Tinne Tuytelaars
- **🏷️ 机构**: KU Leuven University,Belgium
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The focal point of egocentric video understanding is modelling hand-object interactions. Standard models, e.g. CNNs or Vision Transformers, which receive RGB frames as input perform well. However, their performance improves further by employing additional input modalities that provide complementary cues, such as object detections, optical flow, audio, etc. The added complexity of the modality-specific modules, on the other hand, makes these models impractical for deployment. The goal of this work is to retain the performance of such a multimodal approach, while using only the RGB frames as input at inference time. We demonstrate that for egocentric action recognition on the Epic-Kitchens and the Something-Something datasets, students which are taught by multimodal teachers tend to be more accurate and better calibrated than architecturally equivalent models trained on ground truth labels in a unimodal or multimodal fashion. We further adopt a principled multimodal knowledge distillation framework, allowing us to deal with issues which occur when applying multimodal knowledge distillation in a naive manner. Lastly, we demonstrate the achieved reduction in computational complexity, and show that our approach maintains higher performance with the reduction of the number of input views. We release our code at https://github.com/gorjanradevski/multimodal-distillation.

</details>

### Video-FocalNets: Spatio-Temporal Focal Modulation for Video Action Recognition.
- **链接**: [arXiv:2307.06947](https://arxiv.org/abs/2307.06947) · 📚 被引 37
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

### EgoDistill: Egocentric Head Motion Distillation for Efficient Video Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6a412f0037b0df295a39a198666ea6a6-Abstract-Conference.html)
- **作者**: Shuhan Tan, Tushar Nagarajan, Kristen Grauman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### EPIC Fields: Marrying 3D Geometry and Video Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/543d4e171150cb931f1d401cacc3d7af-Abstract-Datasets_and_Benchmarks.html)
- **作者**: Vadim Tschernezki, Ahmad Darkhalil, Zhifan Zhu, David Fouhey, Iro Laina, Diane Larlus et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Revealing the unseen: Benchmarking video action recognition under occlusion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/cef53466b62aebbcf8aa2210a89b33a1-Abstract-Datasets_and_Benchmarks.html)
- **作者**: Shresth Grover, Vibhav Vineet, Yogesh S. Rawat
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CAST: Cross-Attention in Space and Time for Video Action Recognition.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fb1b83b35e96998ddfc0ce1dab635445-Abstract-Conference.html)
- **作者**: Dongho Lee, Jongseo Lee, Jinwoo Choi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Unsupervised Video Domain Adaptation for Action Recognition: A Disentanglement Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/39235c56aef13fb05a6adc95eb9d8d66-Abstract-Conference.html)
- **作者**: Pengfei Wei, Lingdong Kong, Xinghua Qu, Yi Ren, Zhiqiang Xu, Jing Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- Complete-to-Partial 4D Distillation for Self-Supervised Point Cloud Sequence Representation Learning. → [knowledge-distillation](../knowledge-distillation/Guideline%202023.md)
- Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models. → [vlm](../vlm/Guideline%202023.md)
- Enhanced Multimodal Representation Learning with Cross-modal KD. → [multimodal](../multimodal/Guideline%202023.md)
- Vita-CLIP: Video and text adaptive CLIP via Multimodal Prompting. → [vlm](../vlm/Guideline%202023.md)
- Discovering the Real Association: Multimodal Causal Reasoning in Video Question Answering. → [multimodal](../multimodal/Guideline%202023.md)
- Spatio-Temporal Pixel-Level Contrastive Learning-based Source-Free Domain Adaptation for Video Semantic Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Enlarging Instance-specific and Class-specific Information for Open-set Action Recognition. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- MMG-Ego4D: Multi-Modal Generalization in Egocentric Action Recognition. → [multimodal](../multimodal/Guideline%202023.md)
- Ultrahigh Resolution Image/Video Matting with Spatio-Temporal Sparsity. → [network-pruning](../network-pruning/Guideline%202023.md)
- Decomposed Cross-Modal Distillation for RGB-based Temporal Action Detection. → [multimodal](../multimodal/Guideline%202023.md)
- Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Video Task Decathlon: Unifying Image and Video Tasks in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- TeD-SPAD: Temporal Distinctiveness for Self-supervised Privacy-preservation for video Anomaly Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- SOAR: Scene-debiasing Open-set Action Recognition. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Audio-Visual Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- MEGA: Multimodal Alignment Aggregation and Distillation For Cinematic Video Segmentation. → [multimodal](../multimodal/Guideline%202023.md)

<!-- COMPLETE v1 papers=27 -->
