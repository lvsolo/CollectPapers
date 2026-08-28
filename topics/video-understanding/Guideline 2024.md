# Video Understanding — 2024 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 20 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### Uncovering what, why and How: A Comprehensive Benchmark for Causation Understanding of Video Anomaly. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2405.00181](https://arxiv.org/abs/2405.00181) · 📚 被引 31
- **作者**: Hang Du, Sicheng Zhang, Binzhu Xie, Guoshun Nan, Jiayang Zhang, Junrui Xu et al.
- **🏷️ 机构**: Beijing University of Posts and Telecommunications, Nanyang Technological University
- **会议**: CVPR 2024
- **摘要（中）**: 针对视频异常理解（VAU）中仅关注检测和定位、缺乏对异常原因和影响深度理解的问题，该论文提出了一个综合基准CUVA，包含异常类型、时间、事件描述、原因自然语言解释和影响自由文本等多层次标注。同时引入MMEval评估指标，以更好地对齐人类偏好，衡量现有大语言模型对视频异常因果关系的理解能力。相比已有基准，CUVA更注重实用性和因果推理，为视频异常理解提供了更全面的评估框架。
- **摘要（英）**: This paper addresses the lack of deep causal understanding in video anomaly understanding by introducing CUVA, a comprehensive benchmark with multi-level annotations for anomaly type, cause, and effect. It also proposes MMEval, a novel metric aligned with human preferences to evaluate LLMs' comprehension of video anomaly causation. This advances beyond existing detection-focused benchmarks toward more practical and interpretable anomaly analysis.
- **核心贡献**: 提出了首个面向视频异常因果理解的综合基准CUVA和评估指标MMEval。
- **创新点**: 将视频异常理解从检测扩展到因果推理，并设计人类偏好对齐的评估指标。
- **结果**: 提供了全面的标注基准和评估工具，但具体性能数据未在摘要中给出。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video anomaly understanding (VAU) aims to automatically comprehend unusual occurrences in videos, thereby enabling various applications such as traffic surveillance and industrial manufacturing. While existing VAU benchmarks primarily concentrate on anomaly detection and localization, our focus is on more practicality, prompting us to raise the following crucial questions: "what anomaly occurred?", "why did it happen?", and "how severe is this abnormal event?". In pursuit of these answers, we present a comprehensive benchmark for Causation Understanding of Video Anomaly (CUVA). Specifically, each instance of the proposed benchmark involves three sets of human annotations to indicate the "what", "why" and "how" of an anomaly, including 1) anomaly type, start and end times, and event descriptions, 2) natural language explanations for the cause of an anomaly, and 3) free text reflecting the effect of the abnormality. In addition, we also introduce MMEval, a novel evaluation metric designed to better align with human preferences for CUVA, facilitating the measurement of existing LLMs in comprehending the underlying cause and corresponding effect of video anomalies. Finally, we propose a novel prompt-based method that can serve as a baseline approach for the challenging CUVA. We conduct extensive experiments to show the superiority of our evaluation metric and the prompt-based approach. Our code and dataset are available at https://github.com/fesvhtr/CUVA.

</details>

### A Unified Framework for Human-centric Point Cloud Video Understanding. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2403.20031](https://arxiv.org/abs/2403.20031) · 📚 被引 4
- **作者**: Yiteng Xu, Kecheng Ye, Xiao Han, Yiming Ren, Xinge Zhu, Yuexin Ma
- **🏷️ 机构**: ShanghaiTech University, The Chinese University of Hong Kong
- **会议**: CVPR 2024
- **摘要（中）**: 针对人类中心点云视频理解（PVU）中现有方法通常针对单一任务且依赖大量标注数据、泛化能力差的问题，该论文提出一个统一框架，利用人体结构语义和运动动态的先验知识，探索数据内在特征，实现通用的人类点云视频理解。实验表明，该方法在动作识别和3D姿态估计等多个任务上达到最先进性能。相比已有工作，该框架强调通用性和数据效率。
- **摘要（英）**: This paper tackles the poor generalization and task-specific limitations of human-centric point cloud video understanding by proposing a unified framework that leverages human body structural semantics and motion dynamics priors. It achieves state-of-the-art performance on action recognition and 3D pose estimation, demonstrating improved generalization across tasks. This advances beyond single-task, label-hungry approaches.
- **核心贡献**: 提出了一个利用人体先验知识的统一框架，用于通用人类点云视频理解。
- **创新点**: 结合人体结构语义和运动动态，实现跨任务的泛化能力。
- **结果**: 在动作识别和3D姿态估计上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-centric Point Cloud Video Understanding (PVU) is an emerging field focused on extracting and interpreting human-related features from sequences of human point clouds, further advancing downstream human-centric tasks and applications. Previous works usually focus on tackling one specific task and rely on huge labeled data, which has poor generalization capability. Considering that human has specific characteristics, including the structural semantics of human body and the dynamics of human motions, we propose a unified framework to make full use of the prior knowledge and explore the inherent features in the data itself for generalized human-centric point cloud video understanding. Extensive experiments demonstrate that our method achieves state-of-the-art performance on various human-related tasks, including action recognition and 3D pose estimation. All datasets and code will be released soon.

</details>

### Distilling Vision-Language Models on Millions of Videos. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2401.06129](https://arxiv.org/abs/2401.06129) · 📚 被引 10
- **作者**: Yue Zhao, Long Zhao, Xingyi Zhou, Jialin Wu, Chun-Te Chu, Hui Miao et al.
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2024
- **摘要（中）**: 针对视频-语言模型训练中人工标注视频-文本数据不足的问题，该论文提出从强图像-语言基线模型微调视频模型，利用视频指令微调（VIIT）自动标注数百万视频生成高质量描述。实验表明，该模型在多个视频-语言基准上表现优异，如开放NExT-QA上超越最佳结果2.8%，MSR-VTT零样本文本到视频检索上超越最先进方法6%。相比已有方法，生成的描述提供更好的文本监督。
- **摘要（英）**: This paper addresses the scarcity of human-curated video-text data by fine-tuning a video-language model from a strong image-language baseline with synthesized instructional data, then auto-labeling millions of videos. The model surpasses prior best results on NExT-QA by 2.8% and MSR-VTT zero-shot retrieval by 6%, demonstrating superior textual supervision. This advances video-language learning with scalable data generation.
- **核心贡献**: 提出了视频指令微调方法，自动生成大规模高质量视频描述。
- **创新点**: 利用图像-语言模型迁移到视频领域，并通过自标注数据增强训练。
- **结果**: 在多个基准上超越最先进方法，如NExT-QA提升2.8%，MSR-VTT检索提升6%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent advance in vision-language models is largely attributed to the abundance of image-text data. We aim to replicate this success for video-language models, but there simply is not enough human-curated video-text data available. We thus resort to fine-tuning a video-language model from a strong image-language baseline with synthesized instructional data. The resulting video model by video-instruction-tuning (VIIT) is then used to auto-label millions of videos to generate high-quality captions. We show the adapted video-language model performs well on a wide range of video-language benchmarks. For instance, it surpasses the best prior result on open-ended NExT-QA by 2.8%. Besides, our model generates detailed descriptions for previously unseen videos, which provide better textual supervision than existing methods. Experiments show that a video-language dual-encoder model contrastively trained on these auto-generated captions is 3.8% better than the strongest baseline that also leverages vision-language models. Our best model outperforms state-of-the-art methods on MSR-VTT zero-shot text-to-video retrieval by 6%. As a side product, we generate the largest video caption dataset to date.

</details>

### HIG: Hierarchical Interlacement Graph Approach to Scene Graph Generation in Video Understanding. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2312.03050](https://arxiv.org/abs/2312.03050) · 📚 被引 14
- **作者**: Trong-Thuan Nguyen, Pha A. Nguyen, Khoa Luu
- **🏷️ 机构**: University of Arkansas,CVIU Lab
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视频场景图生成中现有方法难以处理复杂交互和多样关系的问题。②提出了新数据集ASPIRe，包含外观-情境-位置-交互-关系谓词，并提出了层次交织图（HIG）方法，通过统一层和图结构深入理解场景变化。③相比现有方法，HIG在五个不同任务上均展现出优越性能。④实验证明HIG在多种场景下优于其他方法。
- **摘要（英）**: This paper tackles complex interactivity understanding in video scene graph generation. It introduces the ASPIRe dataset with diverse predicates and the Hierarchical Interlacement Graph (HIG) method, which uses a unified layer-graph structure for deep scene insights. HIG demonstrates superior performance across five tasks in various scenarios.
- **核心贡献**: 提出ASPIRe数据集和HIG方法，提升视频交互理解能力。
- **创新点**: 层次交织图结构统一处理多种交互任务。
- **结果**: 在多个场景任务上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual interactivity understanding within visual scenes presents a significant challenge in computer vision. Existing methods focus on complex interactivities while leveraging a simple relationship model. These methods, however, struggle with a diversity of appearance, situation, position, interaction, and relation in videos. This limitation hinders the ability to fully comprehend the interplay within the complex visual dynamics of subjects. In this paper, we delve into interactivities understanding within visual content by deriving scene graph representations from dense interactivities among humans and objects. To achieve this goal, we first present a new dataset containing Appearance-Situation-Position-Interaction-Relation predicates, named ASPIRe, offering an extensive collection of videos marked by a wide range of interactivities. Then, we propose a new approach named Hierarchical Interlacement Graph (HIG), which leverages a unified layer and graph within a hierarchical structure to provide deep insights into scene changes across five distinct tasks. Our approach demonstrates superior performance to other methods through extensive experiments conducted in various scenarios.

</details>

### A Backpack Full of Skills: Egocentric Video Understanding with Diverse Task Perspectives. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01730) · 📚 被引 4
- **作者**: Simone Alberto Peirone, Francesca Pistilli, Antonio Alliegro, Giuseppe Averta
- **🏷️ 机构**: Politecnico di Torino
- **会议**: CVPR 2024
- **摘要（中）**: ①针对第一人称视频理解中任务视角多样性的问题。②论文标题暗示提出一种多任务学习方法，但摘要缺失，无法评估具体方法。③缺乏摘要导致无法判断创新点和效果。④无法提供具体数据。
- **摘要（英）**: This paper addresses egocentric video understanding with diverse task perspectives, but the abstract is missing, preventing assessment of methodology and results.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### MovieChat: From Dense Token to Sparse Memory for Long Video Understanding. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2307.16449](https://arxiv.org/abs/2307.16449) · 📚 被引 186
- **作者**: Enxin Song, Wenhao Chai, Guanhong Wang, Yucheng Zhang, Haoyang Zhou, Feiyang Wu et al.
- **🏷️ 机构**: Zhejiang University, University of Washington, Microsoft Research Asia
- **会议**: CVPR 2024
- **摘要（中）**: ①针对长视频理解中计算复杂度高、内存消耗大和长期时序连接困难的问题。②提出了MovieChat，基于Atkinson-Shiffrin记忆模型，利用Transformer token作为记忆载体，结合专门设计的记忆机制，实现从密集token到稀疏记忆的转换。③相比现有系统仅能处理短视频，MovieChat能高效处理长视频，并发布了MovieChat-1K基准（含1K长视频和14K人工标注）。④在长视频理解任务上达到最先进性能。
- **摘要（英）**: This paper addresses computational and memory challenges in long video understanding. MovieChat leverages the Atkinson-Shiffrin memory model with Transformer tokens as memory carriers, enabling efficient processing of long videos. It achieves state-of-the-art performance and introduces the MovieChat-1K benchmark with 1K videos and 14K annotations.
- **核心贡献**: 提出MovieChat模型和MovieChat-1K基准，解决长视频理解中的内存和时序问题。
- **创新点**: 将认知记忆模型融入Transformer token机制，实现稀疏记忆管理。
- **结果**: 在长视频理解上达到最先进性能，并提供新基准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, integrating video foundation models and large language models to build a video understanding system can overcome the limitations of specific pre-defined vision tasks. Yet, existing systems can only handle videos with very few frames. For long videos, the computation complexity, memory cost, and long-term temporal connection impose additional challenges. Taking advantage of the Atkinson-Shiffrin memory model, with tokens in Transformers being employed as the carriers of memory in combination with our specially designed memory mechanism, we propose the MovieChat to overcome these challenges. MovieChat achieves state-of-the-art performance in long video understanding, along with the released MovieChat-1K benchmark with 1K long video and 14K manual annotations for validation of the effectiveness of our method.

</details>

### OmniViD: A Generative Framework for Universal Video Understanding. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2403.17935](https://arxiv.org/abs/2403.17935) · 📚 被引 22
- **作者**: Junke Wang, Dongdong Chen, Chong Luo, Bo He, Lu Yuan, Zuxuan Wu et al.
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Microsoft Cloud &#x002B; AI, Microsoft Research Asia
- **会议**: CVPR 2024
- **摘要（中）**: 针对视频理解任务（如识别、描述、跟踪）因架构和标注格式不同而难以统一的问题，提出OmniViD生成式框架，将语言作为标签并引入时间和框token，将多种视频任务统一为视频基础的token生成。该方法采用完全共享的编码器-解码器架构，覆盖分类、描述和定位任务。相比现有任务特定模型，实现了统一输出空间和架构。实验表明该简单直接的方法在多种视频任务上有效。
- **摘要（英）**: To address the fragmentation of video understanding tasks due to distinct architectures and annotation formats, OmniViD proposes a generative framework unifying tasks as video-grounded token generation using language labels with time and box tokens. It employs a fully shared encoder-decoder architecture for classification, captioning, and localization. Experiments demonstrate the effectiveness of this simple approach across diverse video tasks.
- **核心贡献**: 提出统一视频理解任务的生成式框架OmniViD。
- **创新点**: 利用语言标签和时间/框token统一多种视频任务的输出空间。
- **结果**: 实验验证了统一框架在多种视频任务上的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The core of video understanding tasks, such as recognition, captioning, and tracking, is to automatically detect objects or actions in a video and analyze their temporal evolution. Despite sharing a common goal, different tasks often rely on distinct model architectures and annotation formats. In contrast, natural language processing benefits from a unified output space, i.e., text sequences, which simplifies the training of powerful foundational language models, such as GPT-3, with extensive training corpora. Inspired by this, we seek to unify the output space of video understanding tasks by using languages as labels and additionally introducing time and box tokens. In this way, a variety of video tasks could be formulated as video-grounded token generation. This enables us to address various types of video tasks, including classification (such as action recognition), captioning (covering clip captioning, video question answering, and dense video captioning), and localization tasks (such as visual object tracking) within a fully shared encoder-decoder architecture, following a generative framework. Through comprehensive experiments, we demonstrate such a simple and straightforward idea is quite effective and can achieve state-of-the-art or competitive results on seven video benchmarks, providing a novel perspective for more universal video understanding. Code is available at https://github.com/wangjk666/OmniVid.

</details>

### Compositional Video Understanding with Spatiotemporal Structure-based Transformers. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01774) · 📚 被引 6
- **作者**: Hoyeoung Yun, Jinwoo Ahn, Minseo Kim, Eun-Sol Kim
- **🏷️ 机构**: Hanyang University,Department of Computer Science, Hanyang University,Department of Artificial Intelligence Application
- **会议**: CVPR 2024
- **摘要（中）**: 针对视频理解中时空结构建模不足的问题，提出基于时空结构的Transformer方法，通过显式建模视频中的组合性时空关系来提升理解能力。该方法利用Transformer架构捕捉帧间和区域间的复杂交互。相比传统方法，增强了模型对视频动态结构的表征。摘要未提供具体实验数据，效果待验证。
- **摘要（英）**: Addressing insufficient spatiotemporal structure modeling in video understanding, this work proposes a spatiotemporal structure-based Transformer to explicitly capture compositional relationships. It leverages Transformer architecture to model complex interactions across frames and regions. The approach enhances representation of dynamic video structures, though specific results are not detailed in the abstract.
- **核心贡献**: 提出基于时空结构的Transformer用于组合性视频理解。
- **创新点**: 显式建模视频中的组合性时空结构。
- **结果**: 未提供具体数据，效果待验证。

### Align Before Adapt: Leveraging Entity-to-Region Alignments for Generalizable Video Action Recognition. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2311.15619](https://arxiv.org/abs/2311.15619) · 📚 被引 15
- **作者**: Yifei Chen, Dapeng Chen, Ruijin Liu, Sai Zhou, Wenyuan Xue, Wei Peng
- **🏷️ 机构**: Huawei Technologies,IT Innovation and Research Center
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有视频动作识别中“先适应后对齐”范式忽略静态图像到复杂活动概念映射的问题，提出“先对齐后适应”（ALT）范式，在适应视频表示学习前，利用实体-区域对齐匹配区域感知图像嵌入到离线文本语料库，并将对齐实体的文本嵌入作为Transformer视频适配器的查询，提取视频中重要实体语义。该方法重用视觉-语言对齐，通过底层实体解释动作，有助于理解不熟悉或未见类别。
- **摘要（英）**: To address the limitation of the 'adapt then align' paradigm in mapping static images to complex activity concepts, ALT proposes an 'Align before Adapt' paradigm, exploiting entity-to-region alignments before video adaptation. It uses aligned entity text embeddings as queries in a transformer adapter to extract key semantics. This reuses visual-language alignment and explains actions via entities, aiding generalization to unseen categories.
- **核心贡献**: 提出先对齐后适应的视频动作识别范式ALT。
- **创新点**: 在适应前利用实体-区域对齐增强语义理解。
- **结果**: 有助于提升对复杂动作和未见类别的识别能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale visual-language pre-trained models have achieved significant success in various video tasks. However, most existing methods follow an "adapt then align" paradigm, which adapts pre-trained image encoders to model video-level representations and utilizes one-hot or text embedding of the action labels for supervision. This paradigm overlooks the challenge of mapping from static images to complicated activity concepts. In this paper, we propose a novel "Align before Adapt" (ALT) paradigm. Prior to adapting to video representation learning, we exploit the entity-to-region alignments for each frame. The alignments are fulfilled by matching the region-aware image embeddings to an offline-constructed text corpus. With the aligned entities, we feed their text embeddings to a transformer-based video adapter as the queries, which can help extract the semantics of the most important entities from a video to a vector. This paradigm reuses the visual-language alignment of VLP during adaptation and tries to explain an action by the underlying entities. This helps understand actions by bridging the gap with complex activity semantics, particularly when facing unfamiliar or unseen categories. ALT demonstrates competitive performance while maintaining remarkably low computational costs. In fully supervised experiments, it achieves 88.1% top-1 accuracy on Kinetics-400 with only 4947 GFLOPs. Moreover, ALT outperforms the previous state-of-the-art methods in both zero-shot and few-shot experiments, emphasizing its superior generalizability across various learning scenarios.

</details>

### Ranking Distillation for Open-Ended Video Question Answering with Insufficient Labels. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2403.14430](https://arxiv.org/abs/2403.14430) · 📚 被引 6
- **作者**: Tianming Liang, Chaolei Tan, Beihao Xia, Wei-Shi Zheng, Jian-Fang Hu
- **🏷️ 机构**: Sun Yat-sen University,China, Huazhong University of Science and Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放域视频问答中标签不足（通常每问一个答案）导致将所有未标注答案视为负标签的问题，提出排名蒸馏框架RADI，利用教师模型生成潜在答案排名，丰富标签信息，无需额外人工标注。提出两种鲁棒且无参数的排名蒸馏方法：成对方法引入自适应软间隔，以及另一种方法，避免对不完美教师模型的过度自信。该方法缓解了标签不足问题，提升泛化能力。
- **摘要（英）**: To mitigate insufficient labels in open-ended video QA, RADI proposes a ranking distillation framework using a teacher model to generate rankings for potential answers, enriching label information without extra annotation. It introduces two robust parameter-free ranking distillation approaches, including a pairwise method with adaptive soft margins to avoid overconfidence. This improves generalization under label scarcity.
- **核心贡献**: 提出排名蒸馏框架RADI解决视频问答标签不足问题。
- **创新点**: 利用教师模型排名知识并设计无参数鲁棒蒸馏方法。
- **结果**: 缓解标签不足，提升模型泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focuses on open-ended video question answering, which aims to find the correct answers from a large answer set in response to a video-related question. This is essentially a multi-label classification task, since a question may have multiple answers. However, due to annotation costs, the labels in existing benchmarks are always extremely insufficient, typically one answer per question. As a result, existing works tend to directly treat all the unlabeled answers as negative labels, leading to limited ability for generalization. In this work, we introduce a simple yet effective ranking distillation framework (RADI) to mitigate this problem without additional manual annotation. RADI employs a teacher model trained with incomplete labels to generate rankings for potential answers, which contain rich knowledge about label priority as well as label-associated visual cues, thereby enriching the insufficient labeling information. To avoid overconfidence in the imperfect teacher model, we further present two robust and parameter-free ranking distillation approaches: a pairwise approach which introduces adaptive soft margins to dynamically refine the optimization constraints on various pairwise rankings, and a listwise approach which adopts sampling-based partial listwise learning to resist the bias in teacher ranking. Extensive experiments on five popular benchmarks consistently show that both our pairwise and listwise RADIs outperform state-of-the-art methods. Further analysis demonstrates the effectiveness of our methods on the insufficient labeling problem.

</details>

### Language-aware Visual Semantic Distillation for Video Question Answering. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02560) · 📚 被引 6
- **作者**: Bo Zou, Chao Yang, Yu Qiao, Chengbin Quan, Youjian Zhao
- **🏷️ 机构**: Tsinghua University,Beijing,China, Shanghai AI Laboratory,Shanghai,China, Tsinghua University,Zhongguancun Laboratory,Beijing,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对视频问答中视觉语义与语言信息融合不足的问题，提出语言感知的视觉语义蒸馏方法，利用语言信息指导视觉特征的蒸馏，增强跨模态语义对齐。该方法可能通过教师-学生框架或注意力机制实现。相比现有方法，更强调语言对视觉语义的引导作用。摘要未提供具体实验数据，效果待验证。
- **摘要（英）**: Addressing insufficient fusion of visual semantics and language in video QA, this work proposes language-aware visual semantic distillation to guide visual feature distillation with language information, enhancing cross-modal alignment. It likely employs a teacher-student framework or attention mechanism. The approach emphasizes language-guided visual semantics, though specific results are not provided.
- **核心贡献**: 提出语言感知的视觉语义蒸馏方法用于视频问答。
- **创新点**: 利用语言信息引导视觉语义蒸馏。
- **结果**: 未提供具体数据，效果待验证。

## 跨领域论文（完整笔记在其他领域）

- MVBench: A Comprehensive Multi-modal Video Understanding Benchmark. → [multimodal](../multimodal/Guideline%202024.md)
- Open-Vocabulary Video Anomaly Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Abductive Ego-View Accident Video Understanding for Safe Driving Perception. → [multimodal](../multimodal/Guideline%202024.md)
- MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- Mirasol3B: A Multimodal Autoregressive Model for Time-Aligned and Contextual Modalities. → [multimodal](../multimodal/Guideline%202024.md)
- TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language. → [multimodal](../multimodal/Guideline%202024.md)
- Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- TIM: A Time Interval Machine for Audio-Visual Action Recognition. → [multimodal](../multimodal/Guideline%202024.md)
