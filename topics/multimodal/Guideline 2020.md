# Multimodal — 2020 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multimodal Categorization of Crisis Events in Social Media.
- **链接**: [arXiv:2004.04917](https://arxiv.org/abs/2004.04917) · 📚 被引 107
- **作者**: Mahdi Abavisani, Liwei Wu, Shengli Hu, Joel R. Tetreault, Alejandro Jaimes
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent developments in image classification and natural language processing, coupled with the rapid growth in social media usage, have enabled fundamental advances in detecting breaking events around the world in real-time. Emergency response is one such area that stands to gain from these advances. By processing billions of texts and images a minute, events can be automatically detected to enable emergency response workers to better assess rapidly evolving situations and deploy resources accordingly. To date, most event detection techniques in this area have focused on image-only or text-only approaches, limiting detection performance and impacting the quality of information delivered to crisis response teams. In this paper, we present a new multimodal fusion method that leverages both images and texts as input. In particular, we introduce a cross-attention module that can filter uninformative and misleading components from weak modalities on a sample by sample basis. In addition, we employ a multimodal graph-based approach to stochastically transition between embeddings of different multimodal pairs during training to better regularize the learning process as well as dealing with limited training data by constructing new matched pairs from different samples. We show that our method outperforms the unimodal approaches and strong multimodal baselines by a large margin on three crisis-related tasks.

</details>

### Seeing Through Fog Without Seeing Fog: Deep Multimodal Sensor Fusion in Unseen Adverse Weather.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Bijelic_Seeing_Through_Fog_Without_Seeing_Fog_Deep_Multimodal_Sensor_Fusion_CVPR_2020_paper.html) · 📚 被引 559
- **作者**: Mario Bijelic, Tobias Gruber, Fahim Mannan, Florian Kraus, Werner Ritter, Klaus Dietmayer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Iterative Answer Prediction With Pointer-Augmented Multimodal Transformers for TextVQA.
- **链接**: [arXiv:1911.06258](https://arxiv.org/abs/1911.06258) · 📚 被引 157
- **作者**: Ronghang Hu, Amanpreet Singh, Trevor Darrell, Marcus Rohrbach
- **🏷️ 机构**: UC Berkeley
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many visual scenes contain text that carries crucial information, and it is thus essential to understand text in images for downstream reasoning tasks. For example, a deep water label on a warning sign warns people about the danger in the scene. Recent work has explored the TextVQA task that requires reading and understanding text in images to answer a question. However, existing approaches for TextVQA are mostly based on custom pairwise fusion mechanisms between a pair of two modalities and are restricted to a single prediction step by casting TextVQA as a classification task. In this work, we propose a novel model for the TextVQA task based on a multimodal transformer architecture accompanied by a rich representation for text in images. Our model naturally fuses different modalities homogeneously by embedding them into a common semantic space where self-attention is applied to model inter- and intra- modality context. Furthermore, it enables iterative answer decoding with a dynamic pointer network, allowing the model to form an answer through multi-step prediction instead of one-step classification. Our model outperforms existing approaches on three benchmark datasets for the TextVQA task by a large margin.

</details>

### MMTM: Multimodal Transfer Module for CNN Fusion.
- **链接**: [arXiv:1911.08670](https://arxiv.org/abs/1911.08670) · 📚 被引 161
- **作者**: Hamid Reza Vaezi Joze, Amirreza Shaban, Michael L. Iuzzolino, Kazuhito Koishida
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In late fusion, each modality is processed in a separate unimodal Convolutional Neural Network (CNN) stream and the scores of each modality are fused at the end. Due to its simplicity late fusion is still the predominant approach in many state-of-the-art multimodal applications. In this paper, we present a simple neural network module for leveraging the knowledge from multiple modalities in convolutional neural networks. The propose unit, named Multimodal Transfer Module (MMTM), can be added at different levels of the feature hierarchy, enabling slow modality fusion. Using squeeze and excitation operations, MMTM utilizes the knowledge of multiple modalities to recalibrate the channel-wise features in each CNN stream. Despite other intermediate fusion methods, the proposed module could be used for feature modality fusion in convolution layers with different spatial dimensions. Another advantage of the proposed method is that it could be added among unimodal branches with minimum changes in the their network architectures, allowing each branch to be initialized with existing pretrained weights. Experimental results show that our framework improves the recognition accuracy of well-known multimodal networks. We demonstrate state-of-the-art or competitive performance on four datasets that span the task domains of dynamic hand gesture recognition, speech enhancement, and action recognition with RGB and body joints.

</details>

### Hypergraph Attention Networks for Multimodal Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kim_Hypergraph_Attention_Networks_for_Multimodal_Learning_CVPR_2020_paper.html) · 📚 被引 75
- **作者**: Eun-Sol Kim, Woo-Young Kang, Kyoung-Woon On, Yu-Jung Heo, Byoung-Tak Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Multimodal Future Localization and Emergence Prediction for Objects in Egocentric View With a Reachability Prior.
- **链接**: [arXiv:2006.04700](https://arxiv.org/abs/2006.04700) · [代码](https://github.com/lmb-freiburg/FLN-EPN-RPN) · 📚 被引 29
- **作者**: Osama Makansi, Özgün Çiçek, Kevin Buchicchio, Thomas Brox
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work proposes a new challenge set for multimodal classification, focusing on detecting hate speech in multimodal memes. It is constructed such that unimodal models struggle and only multimodal models can succeed: difficult examples ("benign confounders") are added to the dataset to make it hard to rely on unimodal signals. The task requires subtle reasoning, yet is straightforward to evaluate as a binary classification problem. We provide baseline performance numbers for unimodal models, as well as for multimodal models with various degrees of sophistication. We find that state-of-the-art methods perform poorly compared to humans (64.73% vs. 84.7% accuracy), illustrating the difficulty of the task and highlighting the challenge that this important problem poses to the community.

</details>

### EmotiCon: Context-Aware Multimodal Emotion Recognition Using Frege's Principle.
- **链接**: [arXiv:2003.06692](https://arxiv.org/abs/2003.06692) · 📚 被引 151
- **作者**: Trisha Mittal, Pooja Guhan, Uttaran Bhattacharya, Rohan Chandra, Aniket Bera, Dinesh Manocha
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present EmotiCon, a learning-based algorithm for context-aware perceived human emotion recognition from videos and images. Motivated by Frege's Context Principle from psychology, our approach combines three interpretations of context for emotion recognition. Our first interpretation is based on using multiple modalities(e.g. faces and gaits) for emotion recognition. For the second interpretation, we gather semantic context from the input image and use a self-attention-based CNN to encode this information. Finally, we use depth maps to model the third interpretation related to socio-dynamic interactions and proximity among agents. We demonstrate the efficiency of our network through experiments on EMOTIC, a benchmark dataset. We report an Average Precision (AP) score of 35.48 across 26 classes, which is an improvement of 7-8 over prior methods. We also introduce a new dataset, GroupWalk, which is a collection of videos captured in multiple real-world settings of people walking. We report an AP of 65.83 across 4 categories on GroupWalk, which is also an improvement over prior methods.

</details>

### CoverNet: Multimodal Behavior Prediction Using Trajectory Sets.
- **链接**: [arXiv:1911.10298](https://arxiv.org/abs/1911.10298) · 📚 被引 388
- **作者**: Tung Phan-Minh, Elena Corina Grigore, Freddy A. Boulton, Oscar Beijbom, Eric M. Wolff
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present CoverNet, a new method for multimodal, probabilistic trajectory prediction for urban driving. Previous work has employed a variety of methods, including multimodal regression, occupancy maps, and 1-step stochastic policies. We instead frame the trajectory prediction problem as classification over a diverse set of trajectories. The size of this set remains manageable due to the limited number of distinct actions that can be taken over a reasonable prediction horizon. We structure the trajectory set to a) ensure a desired level of coverage of the state space, and b) eliminate physically impossible trajectories. By dynamically generating trajectory sets based on the agent's current state, we can further improve our method's efficiency. We demonstrate our approach on public, real-world self-driving datasets, and show that it outperforms state-of-the-art methods.

</details>

### EmotiCon: Context-Aware Multimodal Emotion Recognition Using Frege's Principle.
- **链接**: [arXiv:2003.06692](https://arxiv.org/abs/2003.06692) · 📚 被引 151
- **作者**: Trisha Mittal, Pooja Guhan, Uttaran Bhattacharya, Rohan Chandra, Aniket Bera, Dinesh Manocha
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present EmotiCon, a learning-based algorithm for context-aware perceived human emotion recognition from videos and images. Motivated by Frege's Context Principle from psychology, our approach combines three interpretations of context for emotion recognition. Our first interpretation is based on using multiple modalities(e.g. faces and gaits) for emotion recognition. For the second interpretation, we gather semantic context from the input image and use a self-attention-based CNN to encode this information. Finally, we use depth maps to model the third interpretation related to socio-dynamic interactions and proximity among agents. We demonstrate the efficiency of our network through experiments on EMOTIC, a benchmark dataset. We report an Average Precision (AP) score of 35.48 across 26 classes, which is an improvement of 7-8 over prior methods. We also introduce a new dataset, GroupWalk, which is a collection of videos captured in multiple real-world settings of people walking. We report an AP of 65.83 across 4 categories on GroupWalk, which is also an improvement over prior methods.

</details>

### CoverNet: Multimodal Behavior Prediction Using Trajectory Sets.
- **链接**: [arXiv:1911.10298](https://arxiv.org/abs/1911.10298) · 📚 被引 388
- **作者**: Tung Phan-Minh, Elena Corina Grigore, Freddy A. Boulton, Oscar Beijbom, Eric M. Wolff
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present CoverNet, a new method for multimodal, probabilistic trajectory prediction for urban driving. Previous work has employed a variety of methods, including multimodal regression, occupancy maps, and 1-step stochastic policies. We instead frame the trajectory prediction problem as classification over a diverse set of trajectories. The size of this set remains manageable due to the limited number of distinct actions that can be taken over a reasonable prediction horizon. We structure the trajectory set to a) ensure a desired level of coverage of the state space, and b) eliminate physically impossible trajectories. By dynamically generating trajectory sets based on the agent's current state, we can further improve our method's efficiency. We demonstrate our approach on public, real-world self-driving datasets, and show that it outperforms state-of-the-art methods.

</details>

### Self-Supervised MultiModal Versatile Networks.
- **链接**: [arXiv:2006.16228](https://arxiv.org/abs/2006.16228)
- **作者**: Jean-Baptiste Alayrac, Adrià Recasens, Rosalia Schneider, Relja Arandjelovic, Jason Ramapuram, Jeffrey De Fauw et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a multimodal camera relocalization framework that captures ambiguities and uncertainties with continuous mixture models defined on the manifold of camera poses. In highly ambiguous environments, which can easily arise due to symmetries and repetitive structures in the scene, computing one plausible solution (what most state-of-the-art methods currently regress) may not be sufficient. Instead we predict multiple camera pose hypotheses as well as the respective uncertainty for each prediction. Towards this aim, we use Bingham distributions, to model the orientation of the camera pose, and a multivariate Gaussian to model the position, with an end-to-end deep neural network. By incorporating a Winner-Takes-All training scheme, we finally obtain a mixture model that is well suited for explaining ambiguities in the scene, yet does not suffer from mode collapse, a common problem with mixture density networks. We introduce a new dataset specifically designed to foster camera localization research in ambiguous environments and exhaustively evaluate our method on synthetic as well as real data on both ambiguous scenes and on non-ambiguous benchmark datasets. We plan to release our code and dataset under $\href{https://multimodal3dvision.github.io}{multimodal3dvision.github.io}$.

</details>

## 🆕 增量新增

### Multi-Modal Domain Adaptation for Fine-Grained Action Recognition. **⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:2001.09691](https://arxiv.org/abs/2001.09691) · 📚 被引 173
- **作者**: Jonathan Munro, Dima Damen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对细粒度动作识别中环境偏差导致的域偏移问题，提出利用多模态（RGB和光流）的对应关系作为自监督对齐方法，结合对抗训练进行无监督域适应。在EPIC-Kitchens三个厨房数据集上，多模态自监督单独提升2.4%平均性能，结合对抗训练后比其他UDA方法提升3%。
- **摘要（英）**: This work addresses domain shift in fine-grained action recognition by exploiting multimodal correspondence as self-supervised alignment for UDA, combined with adversarial training. On EPIC-Kitchens, multi-modal self-supervision improves 2.4% over source-only, and combined with adversarial training outperforms other UDA methods by 3%.
- **核心贡献**: 提出多模态自监督对齐与对抗训练结合的UDA方法，用于细粒度动作识别。
- **创新点**: 利用模态间对应关系作为自监督信号，增强域适应中的特征对齐。
- **结果**: 在EPIC-Kitchens上显著提升域适应性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-grained action recognition datasets exhibit environmental bias, where multiple video sequences are captured from a limited number of environments. Training a model in one environment and deploying in another results in a drop in performance due to an unavoidable domain shift. Unsupervised Domain Adaptation (UDA) approaches have frequently utilised adversarial training between the source and target domains. However, these approaches have not explored the multi-modal nature of video within each domain. In this work we exploit the correspondence of modalities as a self-supervised alignment approach for UDA in addition to adversarial alignment. We test our approach on three kitchens from our large-scale dataset, EPIC-Kitchens, using two modalities commonly employed for action recognition: RGB and Optical Flow. We show that multi-modal self-supervision alone improves the performance over source-only training by 2.4% on average. We then combine adversarial training with multi-modal self-supervision, showing that our approach outperforms other UDA methods by 3%.

</details>

### Speech2Action: Cross-Modal Supervision for Action Recognition. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2003.13594](https://arxiv.org/abs/2003.13594) · 📚 被引 45
- **作者**: Arsha Nagrani, Chen Sun, David Ross, Rahul Sukthankar, Cordelia Schmid, Andrew Zisserman
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对动作识别中依赖人工标注的问题，探索从对话中预测动作的可能性，利用电影剧本训练BERT-based Speech2Action分类器，应用于大规模未标注电影语料，获得弱标签并训练视频模型。在标准动作识别基准上，无需任何手动标注动作示例，实现了优越性能。
- **摘要（英）**: This paper investigates predicting actions from dialogue, training a BERT-based classifier on screenplays and applying it to large unlabelled movie corpora to obtain weak labels. Training on these clips achieves superior action recognition performance without manual action annotations.
- **核心贡献**: 提出利用对话预测动作的跨模态弱监督方法，生成大规模弱标签训练数据。
- **创新点**: 通过电影剧本学习语音与动作的关联，实现无需人工标注的动作识别。
- **结果**: 在标准基准上超越现有方法，无需手动标注。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Is it possible to guess human action from dialogue alone? In this work we investigate the link between spoken words and actions in movies. We note that movie screenplays describe actions, as well as contain the speech of characters and hence can be used to learn this correlation with no additional supervision. We train a BERT-based Speech2Action classifier on over a thousand movie screenplays, to predict action labels from transcribed speech segments. We then apply this model to the speech segments of a large unlabelled movie corpus (188M speech segments from 288K movies). Using the predictions of this model, we obtain weak action labels for over 800K video clips. By training on these video clips, we demonstrate superior action recognition performance on standard action recognition benchmarks, without using a single manually labelled action example.

</details>

### Cross-Modal Weighting Network for RGB-D Salient Object Detection. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58520-4_39)
- **作者**: Gongyang Li, Zhi Liu, Linwei Ye, Yang Wang, Haibin Ling
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
- **摘要（中）**: 该论文摘要缺失，无法提供具体内容。根据标题推测，可能针对RGB-D显著目标检测中的跨模态加权问题，提出一种加权网络以融合RGB和深度信息。但缺乏摘要和实验细节，无法评估其方法和效果。
- **摘要（英）**: The abstract is missing, so specific details are unavailable. Based on the title, it likely addresses cross-modal weighting for RGB-D salient object detection, but without abstract and experiments, evaluation is impossible.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Interpretable, Multidimensional, Multimodal Anomaly Detection with Negative Sampling for Detection of Device Failure. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](http://proceedings.mlr.press/v119/sipple20a.html)
- **作者**: John Sipple
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020
- **摘要（中）**: ①该论文针对设备故障检测中的异常检测问题，旨在通过多模态数据识别异常模式。②提出了一种基于负采样的可解释、多维、多模态异常检测方法，利用负样本增强模型对异常边界的区分能力。③相比传统单模态或黑盒异常检测方法，该方法强调可解释性，并整合多维特征与多模态信息。④摘要未提供具体数据，但方法在设备故障场景中具有潜在应用价值。
- **摘要（英）**: This paper addresses anomaly detection for device failure using multimodal data, proposing an interpretable, multidimensional approach with negative sampling to improve boundary discrimination. It enhances existing methods by integrating explainability and multimodal features, though no quantitative results are reported in the abstract.
- **核心贡献**: 提出了一种结合负采样和可解释性的多模态异常检测框架。
- **创新点**: 将负采样策略应用于多模态异常检测以增强区分能力。
- **结果**: 摘要未提供具体性能数据，效果待验证。

## 跨领域论文（完整笔记在其他领域）

- ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes. → [3d-detection](../3d-detection/Guideline%202020.md)
- nuScenes: A Multimodal Dataset for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202020.md)
- Vision-Language Navigation With Self-Supervised Auxiliary Reasoning Tasks. → [self-supervised-vision](../self-supervised-vision/Guideline%202020.md)
- Creating Something From Nothing: Unsupervised Knowledge Distillation for Cross-Modal Hashing. → [knowledge-distillation](../knowledge-distillation/Guideline%202020.md)
<!-- COMPLETE v1 papers=15 -->
