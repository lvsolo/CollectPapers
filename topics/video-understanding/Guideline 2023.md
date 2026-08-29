# Video Understanding — 2023 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

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

> Researchers have extensively studied the field of vision and language, discovering that both visual and textual content is crucial for understanding scenes effectively. Particularly, comprehending text in videos holds great significance, requiring both scene text understanding and temporal reasoning. This paper focuses on exploring two recently introduced datasets, NewsVideoQA and M4-ViteVQA, which aim to address video question answering based on textual content. The NewsVideoQA dataset contains question-answer pairs related to the text in news videos, while M4-ViteVQA comprises question-answer pairs from diverse categories like vlogging, traveling, and shopping. We provide an analysis of the formulation of these datasets on various levels, exploring the degree of visual understanding and multi-frame comprehension required for answering the questions. Additionally, the study includes experimentation with BERT-QA, a text-only model, which demonstrates comparable performance to the original methods on both datasets, indicating the shortcomings in the formulation of these datasets. Furthermore, we also look into the domain adaptation aspect by examining the effectiveness of training on M4-ViteVQA and evaluating on NewsVideoQA and vice-versa, thereby shedding light on the challenges and potential benefits of out-of-domain training.

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

> Understanding verbs is crucial to modelling how people and objects interact with each other and the environment through space and time. Recently, state-of-the-art video-language models based on CLIP have been shown to have limited verb understanding and to rely extensively on nouns, restricting their performance in real-world video applications that require action and temporal understanding. In this work, we improve verb understanding for CLIP-based video-language models by proposing a new Verb-Focused Contrastive (VFC) framework. This consists of two main components: (1) leveraging pretrained large language models (LLMs) to create hard negatives for cross-modal contrastive learning, together with a calibration strategy to balance the occurrence of concepts in positive and negative pairs; and (2) enforcing a fine-grained, verb phrase alignment loss. Our method achieves state-of-the-art results for zero-shot performance on three downstream tasks that focus on verb understanding: video-text matching, video question-answering and video classification. To the best of our knowledge, this is the first work which proposes a method to alleviate the verb understanding problem, and does not simply highlight it.

</details>

### Procedure-Aware Pretraining for Instructional Video Understanding.
- **链接**: [arXiv:2303.18230](https://arxiv.org/abs/2303.18230) · 📚 被引 38
- **作者**: Honglu Zhou, Roberto Martín-Martín, Mubbasir Kapadia, Silvio Savarese, Juan Carlos Niebles
- **🏷️ 机构**: Salesforce Research, Rutgers University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While most modern video understanding models operate on short-range clips, real-world videos are often several minutes long with semantically consistent segments of variable length. A common approach to process long videos is applying a short-form video model over uniformly sampled clips of fixed temporal length and aggregating the outputs. This approach neglects the underlying nature of long videos since fixed-length clips are often redundant or uninformative. In this paper, we aim to provide a generic and adaptive sampling approach for long-form videos in lieu of the de facto uniform sampling. Viewing videos as semantically consistent segments, we formulate a task-agnostic, unsupervised, and scalable approach based on Kernel Temporal Segmentation (KTS) for sampling and tokenizing long videos. We evaluate our method on long-form video understanding tasks such as video classification and temporal action localization, showing consistent gains over existing approaches and achieving state-of-the-art performance on long-form video modeling.

</details>

### TimeBalance: Temporally-Invariant and Temporally-Distinctive Video Representations for Semi-Supervised Action Recognition.
- **链接**: [arXiv:2303.16268](https://arxiv.org/abs/2303.16268) · 📚 被引 17
- **作者**: Ishan Rajendrakumar Dave, Mamshad Nayeem Rizve, Chen Chen, Mubarak Shah
- **🏷️ 机构**: Center for Research in Computer Vision, University of Central Florida,Orlando,USA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many real-world applications, from sport analysis to surveillance, benefit from automatic long-term action recognition. In the current deep learning paradigm for automatic action recognition, it is imperative that models are trained and tested on datasets and tasks that evaluate if such models actually learn and reason over long-term information. In this work, we propose a method to evaluate how suitable a video dataset is to evaluate models for long-term action recognition. To this end, we define a long-term action as excluding all the videos that can be correctly recognized using solely short-term information. We test this definition on existing long-term classification tasks on three popular real-world datasets, namely Breakfast, CrossTask and LVU, to determine if these datasets are truly evaluating long-term recognition. Our study reveals that these datasets can be effectively solved using shortcuts based on short-term information. Following this finding, we encourage long-term action recognition researchers to make use of datasets that need long-term information to be solved.

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
- Unified Mask Embedding and Correspondence Learning for Self-Supervised Video Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Masked Motion Encoding for Self-Supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Spatio-Temporal Pixel-Level Contrastive Learning-based Source-Free Domain Adaptation for Video Semantic Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Ultrahigh Resolution Image/Video Matting with Spatio-Temporal Sparsity. → [network-pruning](../network-pruning/Guideline%202023.md)
