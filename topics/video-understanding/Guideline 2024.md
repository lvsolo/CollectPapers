# Video Understanding — 2024 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Uncovering what, why and How: A Comprehensive Benchmark for Causation Understanding of Video Anomaly.
- **链接**: [arXiv:2405.00181](https://arxiv.org/abs/2405.00181) · [代码](https://github.com/fesvhtr/CUVA) · 📚 被引 31
- **作者**: Hang Du, Sicheng Zhang, Binzhu Xie, Guoshun Nan, Jiayang Zhang, Junrui Xu et al.
- **🏷️ 机构**: Beijing University of Posts and Telecommunications, Nanyang Technological University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Video anomaly understanding (VAU) aims to automatically comprehend unusual occurrences in videos, thereby enabling various applications such as traffic surveillance and industrial manufacturing. While existing VAU benchmarks primarily concentrate on anomaly detection and localization, our focus is on more practicality, prompting us to raise the following crucial questions: "what anomaly occurred?", "why did it happen?", and "how severe is this abnormal event?". In pursuit of these answers, we present a comprehensive benchmark for Causation Understanding of Video Anomaly (CUVA). Specifically, each instance of the proposed benchmark involves three sets of human annotations to indicate the "what", "why" and "how" of an anomaly, including 1) anomaly type, start and end times, and event descriptions, 2) natural language explanations for the cause of an anomaly, and 3) free text reflecting the effect of the abnormality. In addition, we also introduce MMEval, a novel evaluation metric designed to better align with human preferences for CUVA, facilitating the measurement of existing LLMs in comprehending the underlying cause and corresponding effect of video anomalies. Finally, we propose a novel prompt-based method that can serve as a baseline approach for the challenging CUVA. We conduct extensive experiments to show the superiority of our evaluation metric and the prompt-based approach. Our code and dataset are available at https://github.com/fesvhtr/CUVA.

### A Unified Framework for Human-centric Point Cloud Video Understanding.
- **链接**: [arXiv:2403.20031](https://arxiv.org/abs/2403.20031) · 📚 被引 4
- **作者**: Yiteng Xu, Kecheng Ye, Xiao Han, Yiming Ren, Xinge Zhu, Yuexin Ma
- **🏷️ 机构**: ShanghaiTech University, The Chinese University of Hong Kong
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Human-centric Point Cloud Video Understanding (PVU) is an emerging field focused on extracting and interpreting human-related features from sequences of human point clouds, further advancing downstream human-centric tasks and applications. Previous works usually focus on tackling one specific task and rely on huge labeled data, which has poor generalization capability. Considering that human has specific characteristics, including the structural semantics of human body and the dynamics of human motions, we propose a unified framework to make full use of the prior knowledge and explore the inherent features in the data itself for generalized human-centric point cloud video understanding. Extensive experiments demonstrate that our method achieves state-of-the-art performance on various human-related tasks, including action recognition and 3D pose estimation. All datasets and code will be released soon.

### Abductive Ego-View Accident Video Understanding for Safe Driving Perception.
- **链接**: [arXiv:2403.00436](https://arxiv.org/abs/2403.00436) · 📚 被引 33
- **作者**: Jianwu Fang, Lei-Lei Li, Junfei Zhou, Junbin Xiao, Hongkai Yu, Chen Lv et al.
- **🏷️ 机构**: Xi&#x0027;an Jiaotong University, Chang&#x0027;an University, National University of Singapore
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present MM-AU, a novel dataset for Multi-Modal Accident video Understanding. MM-AU contains 11,727 in-the-wild ego-view accident videos, each with temporally aligned text descriptions. We annotate over 2.23 million object boxes and 58,650 pairs of video-based accident reasons, covering 58 accident categories. MM-AU supports various accident understanding tasks, particularly multimodal video diffusion to understand accident cause-effect chains for safe driving. With MM-AU, we present an Abductive accident Video understanding framework for Safe Driving perception (AdVersa-SD). AdVersa-SD performs video diffusion via an Object-Centric Video Diffusion (OAVD) method which is driven by an abductive CLIP model. This model involves a contrastive interaction loss to learn the pair co-occurrence of normal, near-accident, accident frames with the corresponding text descriptions, such as accident reasons, prevention advice, and accident categories. OAVD enforces the causal region learning while fixing the content of the original frame background in video generation, to find the dominant cause-effect chain for certain accidents. Extensive experiments verify the abductive ability of AdVersa-SD and the superiority of OAVD against the state-of-the-art diffusion models. Additionally, we provide careful benchmark evaluations for object detection and accident reason answering since AdVersa-SD relies on precise object and accident reason information.

### Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding.
- **链接**: [arXiv:2311.08046](https://arxiv.org/abs/2311.08046) · [代码](https://github.com/PKU-YuanGroup/Chat-UniVi) · 📚 被引 156
- **作者**: Peng Jin, Ryuichi Takanobu, Wancai Zhang, Xiaochun Cao, Li Yuan
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University,Shenzhen,China, Peng Cheng Laboratory,Shenzhen,China, Nari Technology Co.,Ltd.,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large language models have demonstrated impressive universal capabilities across a wide range of open-ended tasks and have extended their utility to encompass multimodal conversations. However, existing methods encounter challenges in effectively handling both image and video understanding, particularly with limited visual tokens. In this work, we introduce Chat-UniVi, a Unified Vision-language model capable of comprehending and engaging in conversations involving images and videos through a unified visual representation. Specifically, we employ a set of dynamic visual tokens to uniformly represent images and videos. This representation framework empowers the model to efficiently utilize a limited number of visual tokens to simultaneously capture the spatial details necessary for images and the comprehensive temporal relationship required for videos. Moreover, we leverage a multi-scale representation, enabling the model to perceive both high-level semantic concepts and low-level visual details. Notably, Chat-UniVi is trained on a mixed dataset containing both images and videos, allowing direct application to tasks involving both mediums without requiring any modifications. Extensive experimental results demonstrate that Chat-UniVi consistently outperforms even existing methods exclusively designed for either images or videos. Code is available at https://github.com/PKU-YuanGroup/Chat-UniVi.

### HIG: Hierarchical Interlacement Graph Approach to Scene Graph Generation in Video Understanding.
- **链接**: [arXiv:2312.03050](https://arxiv.org/abs/2312.03050) · 📚 被引 14
- **作者**: Trong-Thuan Nguyen, Pha A. Nguyen, Khoa Luu
- **🏷️ 机构**: University of Arkansas,CVIU Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Visual interactivity understanding within visual scenes presents a significant challenge in computer vision. Existing methods focus on complex interactivities while leveraging a simple relationship model. These methods, however, struggle with a diversity of appearance, situation, position, interaction, and relation in videos. This limitation hinders the ability to fully comprehend the interplay within the complex visual dynamics of subjects. In this paper, we delve into interactivities understanding within visual content by deriving scene graph representations from dense interactivities among humans and objects. To achieve this goal, we first present a new dataset containing Appearance-Situation-Position-Interaction-Relation predicates, named ASPIRe, offering an extensive collection of videos marked by a wide range of interactivities. Then, we propose a new approach named Hierarchical Interlacement Graph (HIG), which leverages a unified layer and graph within a hierarchical structure to provide deep insights into scene changes across five distinct tasks. Our approach demonstrates superior performance to other methods through extensive experiments conducted in various scenarios.

### A Backpack Full of Skills: Egocentric Video Understanding with Diverse Task Perspectives.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01730) · 📚 被引 4
- **作者**: Simone Alberto Peirone, Francesca Pistilli, Antonio Alliegro, Giuseppe Averta
- **🏷️ 机构**: Politecnico di Torino
- **会议**: CVPR 2024

### MovieChat: From Dense Token to Sparse Memory for Long Video Understanding.
- **链接**: [arXiv:2307.16449](https://arxiv.org/abs/2307.16449) · 📚 被引 186
- **作者**: Enxin Song, Wenhao Chai, Guanhong Wang, Yucheng Zhang, Haoyang Zhou, Feiyang Wu et al.
- **🏷️ 机构**: Zhejiang University, University of Washington, Microsoft Research Asia
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recently, integrating video foundation models and large language models to build a video understanding system can overcome the limitations of specific pre-defined vision tasks. Yet, existing systems can only handle videos with very few frames. For long videos, the computation complexity, memory cost, and long-term temporal connection impose additional challenges. Taking advantage of the Atkinson-Shiffrin memory model, with tokens in Transformers being employed as the carriers of memory in combination with our specially designed memory mechanism, we propose the MovieChat to overcome these challenges. MovieChat achieves state-of-the-art performance in long video understanding, along with the released MovieChat-1K benchmark with 1K long video and 14K manual annotations for validation of the effectiveness of our method.

### OmniViD: A Generative Framework for Universal Video Understanding.
- **链接**: [arXiv:2403.17935](https://arxiv.org/abs/2403.17935) · [代码](https://github.com/wangjk666/OmniVid) · 📚 被引 22
- **作者**: Junke Wang, Dongdong Chen, Chong Luo, Bo He, Lu Yuan, Zuxuan Wu et al.
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, Microsoft Cloud &#x002B; AI, Microsoft Research Asia
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The core of video understanding tasks, such as recognition, captioning, and tracking, is to automatically detect objects or actions in a video and analyze their temporal evolution. Despite sharing a common goal, different tasks often rely on distinct model architectures and annotation formats. In contrast, natural language processing benefits from a unified output space, i.e., text sequences, which simplifies the training of powerful foundational language models, such as GPT-3, with extensive training corpora. Inspired by this, we seek to unify the output space of video understanding tasks by using languages as labels and additionally introducing time and box tokens. In this way, a variety of video tasks could be formulated as video-grounded token generation. This enables us to address various types of video tasks, including classification (such as action recognition), captioning (covering clip captioning, video question answering, and dense video captioning), and localization tasks (such as visual object tracking) within a fully shared encoder-decoder architecture, following a generative framework. Through comprehensive experiments, we demonstrate such a simple and straightforward idea is quite effective and can achieve state-of-the-art or competitive results on seven video benchmarks, providing a novel perspective for more universal video understanding. Code is available at https://github.com/wangjk666/OmniVid.

### Compositional Video Understanding with Spatiotemporal Structure-based Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01774) · 📚 被引 6
- **作者**: Hoyeoung Yun, Jinwoo Ahn, Minseo Kim, Eun-Sol Kim
- **🏷️ 机构**: Hanyang University,Department of Computer Science, Hanyang University,Department of Artificial Intelligence Application
- **会议**: CVPR 2024

### Align Before Adapt: Leveraging Entity-to-Region Alignments for Generalizable Video Action Recognition.
- **链接**: [arXiv:2311.15619](https://arxiv.org/abs/2311.15619) · 📚 被引 15
- **作者**: Yifei Chen, Dapeng Chen, Ruijin Liu, Sai Zhou, Wenyuan Xue, Wei Peng
- **🏷️ 机构**: Huawei Technologies,IT Innovation and Research Center
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large-scale visual-language pre-trained models have achieved significant success in various video tasks. However, most existing methods follow an "adapt then align" paradigm, which adapts pre-trained image encoders to model video-level representations and utilizes one-hot or text embedding of the action labels for supervision. This paradigm overlooks the challenge of mapping from static images to complicated activity concepts. In this paper, we propose a novel "Align before Adapt" (ALT) paradigm. Prior to adapting to video representation learning, we exploit the entity-to-region alignments for each frame. The alignments are fulfilled by matching the region-aware image embeddings to an offline-constructed text corpus. With the aligned entities, we feed their text embeddings to a transformer-based video adapter as the queries, which can help extract the semantics of the most important entities from a video to a vector. This paradigm reuses the visual-language alignment of VLP during adaptation and tries to explain an action by the underlying entities. This helps understand actions by bridging the gap with complex activity semantics, particularly when facing unfamiliar or unseen categories. ALT demonstrates competitive performance while maintaining remarkably low computational costs. In fully supervised experiments, it achieves 88.1% top-1 accuracy on Kinetics-400 with only 4947 GFLOPs. Moreover, ALT outperforms the previous state-of-the-art methods in both zero-shot and few-shot experiments, emphasizing its superior generalizability across various learning scenarios.

### Ranking Distillation for Open-Ended Video Question Answering with Insufficient Labels.
- **链接**: [arXiv:2403.14430](https://arxiv.org/abs/2403.14430) · 📚 被引 6
- **作者**: Tianming Liang, Chaolei Tan, Beihao Xia, Wei-Shi Zheng, Jian-Fang Hu
- **🏷️ 机构**: Sun Yat-sen University,China, Huazhong University of Science and Technology,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > This paper focuses on open-ended video question answering, which aims to find the correct answers from a large answer set in response to a video-related question. This is essentially a multi-label classification task, since a question may have multiple answers. However, due to annotation costs, the labels in existing benchmarks are always extremely insufficient, typically one answer per question. As a result, existing works tend to directly treat all the unlabeled answers as negative labels, leading to limited ability for generalization. In this work, we introduce a simple yet effective ranking distillation framework (RADI) to mitigate this problem without additional manual annotation. RADI employs a teacher model trained with incomplete labels to generate rankings for potential answers, which contain rich knowledge about label priority as well as label-associated visual cues, thereby enriching the insufficient labeling information. To avoid overconfidence in the imperfect teacher model, we further present two robust and parameter-free ranking distillation approaches: a pairwise approach which introduces adaptive soft margins to dynamically refine the optimization constraints on various pairwise rankings, and a listwise approach which adopts sampling-based partial listwise learning to resist the bias in teacher ranking. Extensive experiments on five popular benchmarks consistently show that both our pairwise and listwise RADIs outperform state-of-the-art methods. Further analysis demonstrates the effectiveness of our methods on the insufficient labeling problem.

### Language-aware Visual Semantic Distillation for Video Question Answering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02560) · 📚 被引 6
- **作者**: Bo Zou, Chao Yang, Yu Qiao, Chengbin Quan, Youjian Zhao
- **🏷️ 机构**: Tsinghua University,Beijing,China, Shanghai AI Laboratory,Shanghai,China, Tsinghua University,Zhongguancun Laboratory,Beijing,China
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- MVBench: A Comprehensive Multi-modal Video Understanding Benchmark. → [multimodal](../multimodal/Guideline%202024.md)
- Open-Vocabulary Video Anomaly Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
