# Video Understanding — 2023 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Tracking Anything with Decoupled Video Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00127) · 📚 被引 194
- **作者**: Ho Kei Cheng, Seoung Wug Oh, Brian L. Price, Alexander G. Schwing, Joon-Young Lee
- **🏷️ 机构**: University of Illinois Urbana-Champaign, Adobe Research
- **会议**: ICCV 2023

### Understanding Video Scenes through Text: Insights from Text-based Video Question Answering.
- **链接**: [arXiv:2309.01380](https://arxiv.org/abs/2309.01380) · 📚 被引 3
- **作者**: Soumya Jahagirdar, Minesh Mathew, Dimosthenis Karatzas, C. V. Jawahar
- **🏷️ 机构**: IIIT Hyderabad,CVIT,India, Wadhwani AI, UAB,Computer Vision Center,Spain
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Researchers have extensively studied the field of vision and language, discovering that both visual and textual content is crucial for understanding scenes effectively. Particularly, comprehending text in videos holds great significance, requiring both scene text understanding and temporal reasoning. This paper focuses on exploring two recently introduced datasets, NewsVideoQA and M4-ViteVQA, which aim to address video question answering based on textual content. The NewsVideoQA dataset contains question-answer pairs related to the text in news videos, while M4-ViteVQA comprises question-answer pairs from diverse categories like vlogging, traveling, and shopping. We provide an analysis of the formulation of these datasets on various levels, exploring the degree of visual understanding and multi-frame comprehension required for answering the questions. Additionally, the study includes experimentation with BERT-QA, a text-only model, which demonstrates comparable performance to the original methods on both datasets, indicating the shortcomings in the formulation of these datasets. Furthermore, we also look into the domain adaptation aspect by examining the effectiveness of training on M4-ViteVQA and evaluating on NewsVideoQA and vice-versa, thereby shedding light on the challenges and potential benefits of out-of-domain training.

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

## 跨领域论文（完整笔记在其他领域）

- Open-Vocabulary Video Question Answering: A New Benchmark for Evaluating the Generalizability of Video Question Answering Models. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- TeD-SPAD: Temporal Distinctiveness for Self-supervised Privacy-preservation for video Anomaly Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- MEGA: Multimodal Alignment Aggregation and Distillation For Cinematic Video Segmentation. → [multimodal](../multimodal/Guideline%202023.md)
