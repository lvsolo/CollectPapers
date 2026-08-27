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
