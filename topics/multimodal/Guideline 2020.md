# Multimodal — 2020 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Multimodal Categorization of Crisis Events in Social Media. **⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2004.04917](https://arxiv.org/abs/2004.04917) · 📚 被引 107
- **作者**: Mahdi Abavisani, Liwei Wu, Shengli Hu, Joel R. Tetreault, Alejandro Jaimes
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对社交媒体危机事件检测中图像和文本单模态方法性能受限的问题。②提出一种多模态融合方法，引入跨注意力模块过滤弱模态中的无信息或误导性成分，并采用基于图的随机过渡策略正则化训练。③相比图像或文本单独处理方法，实现了更有效的多模态融合。④实验表明该方法提升了危机事件检测性能，但摘要未提供具体数据。
- **摘要（英）**: This paper proposes a multimodal fusion method for crisis event detection, using a cross-attention module to filter uninformative components and a graph-based stochastic transition for regularization. It improves detection performance over unimodal approaches, though specific metrics are not given.
- **核心贡献**: 提出跨注意力与图正则化的多模态融合方法，用于危机事件检测。
- **创新点**: 设计跨注意力模块和随机图过渡策略，增强多模态融合鲁棒性。
- **结果**: 实验显示检测性能提升，但未提供具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent developments in image classification and natural language processing, coupled with the rapid growth in social media usage, have enabled fundamental advances in detecting breaking events around the world in real-time. Emergency response is one such area that stands to gain from these advances. By processing billions of texts and images a minute, events can be automatically detected to enable emergency response workers to better assess rapidly evolving situations and deploy resources accordingly. To date, most event detection techniques in this area have focused on image-only or text-only approaches, limiting detection performance and impacting the quality of information delivered to crisis response teams. In this paper, we present a new multimodal fusion method that leverages both images and texts as input. In particular, we introduce a cross-attention module that can filter uninformative and misleading components from weak modalities on a sample by sample basis. In addition, we employ a multimodal graph-based approach to stochastically transition between embeddings of different multimodal pairs during training to better regularize the learning process as well as dealing with limited training data by constructing new matched pairs from different samples. We show that our method outperforms the unimodal approaches and strong multimodal baselines by a large margin on three crisis-related tasks.

</details>

### Seeing Through Fog Without Seeing Fog: Deep Multimodal Sensor Fusion in Unseen Adverse Weather. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Bijelic_Seeing_Through_Fog_Without_Seeing_Fog_Deep_Multimodal_Sensor_Fusion_CVPR_2020_paper.html) · 📚 被引 559
- **作者**: Mario Bijelic, Tobias Gruber, Fahim Mannan, Florian Kraus, Werner Ritter, Klaus Dietmayer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自动驾驶在未知恶劣天气（如雾天）下传感器感知性能下降的问题。②提出深度多模态传感器融合方法，在训练时使用清晰天气数据，测试时直接应用于雾天场景，无需显式去雾。③相比传统去雾或单模态方法，通过多模态融合提升鲁棒性。④摘要不完整，未提供具体效果数据，但该方向对自动驾驶感知至关重要。
- **摘要（英）**: This paper addresses sensor perception degradation in unseen adverse weather for autonomous driving, proposing a deep multimodal fusion approach that trains on clear weather and tests directly in fog without explicit dehazing. It aims to improve robustness over unimodal methods, though results are not detailed in the incomplete abstract.
- **核心贡献**: 提出无需去雾的深度多模态融合方法，提升未知恶劣天气下的感知鲁棒性。
- **创新点**: 利用多模态融合在训练-测试域差异下实现鲁棒感知。
- **结果**: 摘要不完整，未提供具体效果数据。

### Iterative Answer Prediction With Pointer-Augmented Multimodal Transformers for TextVQA. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:1911.06258](https://arxiv.org/abs/1911.06258) · 📚 被引 157
- **作者**: Ronghang Hu, Amanpreet Singh, Trevor Darrell, Marcus Rohrbach
- **🏷️ 机构**: UC Berkeley
- **会议**: CVPR 2020
- **摘要（中）**: ①针对TextVQA任务中现有方法依赖自定义成对融合机制且仅单步预测的问题。②提出基于多模态Transformer的模型，将不同模态嵌入共同语义空间，通过自注意力建模模态内和模态间上下文，并采用动态指针网络实现迭代答案解码。③相比现有方法，实现了同质化融合和多步预测。④在三个基准数据集上优于现有方法，但摘要未提供具体数值。
- **摘要（英）**: This paper proposes a multimodal transformer with dynamic pointer network for TextVQA, enabling homogeneous fusion and iterative answer decoding. It outperforms existing methods on three benchmarks, though specific numbers are not given.
- **核心贡献**: 提出多模态Transformer与动态指针网络，实现TextVQA的迭代答案预测。
- **创新点**: 利用自注意力同质化融合和多步解码机制。
- **结果**: 在三个基准数据集上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many visual scenes contain text that carries crucial information, and it is thus essential to understand text in images for downstream reasoning tasks. For example, a deep water label on a warning sign warns people about the danger in the scene. Recent work has explored the TextVQA task that requires reading and understanding text in images to answer a question. However, existing approaches for TextVQA are mostly based on custom pairwise fusion mechanisms between a pair of two modalities and are restricted to a single prediction step by casting TextVQA as a classification task. In this work, we propose a novel model for the TextVQA task based on a multimodal transformer architecture accompanied by a rich representation for text in images. Our model naturally fuses different modalities homogeneously by embedding them into a common semantic space where self-attention is applied to model inter- and intra- modality context. Furthermore, it enables iterative answer decoding with a dynamic pointer network, allowing the model to form an answer through multi-step prediction instead of one-step classification. Our model outperforms existing approaches on three benchmark datasets for the TextVQA task by a large margin.

</details>

### MMTM: Multimodal Transfer Module for CNN Fusion. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:1911.08670](https://arxiv.org/abs/1911.08670) · 📚 被引 161
- **作者**: Hamid Reza Vaezi Joze, Amirreza Shaban, Michael L. Iuzzolino, Kazuhito Koishida
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对多模态CNN融合中晚期融合简单但缺乏中间交互的问题。②提出多模态迁移模块（MMTM），利用squeeze和excitation操作在特征层级进行通道重校准，实现慢速融合。③相比其他中间融合方法，MMTM可处理不同空间维度的卷积层，且对网络架构改动小，可复用预训练权重。④实验表明在多个识别任务上提升了准确率，但摘要未提供具体数据。
- **摘要（英）**: This paper introduces MMTM, a module for channel-wise recalibration in multimodal CNN fusion, enabling slow fusion with minimal architectural changes. It improves recognition accuracy on several tasks, though specific metrics are not detailed.
- **核心贡献**: 提出MMTM模块，实现轻量级多模态特征融合。
- **创新点**: 利用squeeze-excitation操作进行通道重校准，支持不同空间维度融合。
- **结果**: 实验显示识别准确率提升，但未提供具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In late fusion, each modality is processed in a separate unimodal Convolutional Neural Network (CNN) stream and the scores of each modality are fused at the end. Due to its simplicity late fusion is still the predominant approach in many state-of-the-art multimodal applications. In this paper, we present a simple neural network module for leveraging the knowledge from multiple modalities in convolutional neural networks. The propose unit, named Multimodal Transfer Module (MMTM), can be added at different levels of the feature hierarchy, enabling slow modality fusion. Using squeeze and excitation operations, MMTM utilizes the knowledge of multiple modalities to recalibrate the channel-wise features in each CNN stream. Despite other intermediate fusion methods, the proposed module could be used for feature modality fusion in convolution layers with different spatial dimensions. Another advantage of the proposed method is that it could be added among unimodal branches with minimum changes in the their network architectures, allowing each branch to be initialized with existing pretrained weights. Experimental results show that our framework improves the recognition accuracy of well-known multimodal networks. We demonstrate state-of-the-art or competitive performance on four datasets that span the task domains of dynamic hand gesture recognition, speech enhancement, and action recognition with RGB and body joints.

</details>

### Hypergraph Attention Networks for Multimodal Learning. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Kim_Hypergraph_Attention_Networks_for_Multimodal_Learning_CVPR_2020_paper.html) · 📚 被引 75
- **作者**: Eun-Sol Kim, Woo-Young Kang, Kyoung-Woon On, Yu-Jung Heo, Byoung-Tak Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对多模态学习中复杂高阶关系建模不足的问题。②提出超图注意力网络，利用超图结构捕捉多模态数据间的高阶交互。③相比传统图方法，超图能建模更复杂的关联。④摘要不完整，未提供具体效果数据。
- **摘要（英）**: This paper proposes hypergraph attention networks for multimodal learning to capture high-order interactions. It extends graph-based methods to hypergraphs, though results are not detailed in the incomplete abstract.
- **核心贡献**: 提出超图注意力网络用于多模态高阶关系建模。
- **创新点**: 利用超图结构增强多模态交互建模能力。
- **结果**: 摘要不完整，未提供具体效果数据。

### Multimodal Future Localization and Emergence Prediction for Objects in Egocentric View With a Reachability Prior. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2006.04700](https://arxiv.org/abs/2006.04700) · 📚 被引 29
- **作者**: Osama Makansi, Özgün Çiçek, Kevin Buchicchio, Thomas Brox
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对自动驾驶中单目相机视角下未来动态预测的挑战，包括部分可见性和自车运动导致的视野变化，以及未来状态分布的多模态性。提出利用当前图像的语义图估计可达性先验，并结合规划的自车运动将其传播到未来，同时采用多假设学习进行多模态预测。相比以往依赖地图结构知识的方法，该方法无需地图先验，首次实现了新物体出现的预测，并在未见数据集上展示了零样本迁移能力。实验表明，可达性先验与多假设学习结合显著提升了跟踪物体未来位置预测的准确性。
- **摘要（英）**: This paper addresses the challenges of predicting future dynamics in egocentric driving views, including partial visibility and multimodal future distributions. It proposes a reachability prior estimated from the semantic map and propagated via planned egomotion, combined with multi-hypothesis learning, without requiring map priors. Experiments show improved multimodal prediction of tracked objects and, for the first time, emergence of new objects, with promising zero-shot transfer to unseen datasets.
- **核心贡献**: 提出了一种无需地图先验的可达性先验传播方法，结合多假设学习，实现了对物体未来位置和新物体出现的多模态预测。
- **创新点**: 利用语义图估计可达性先验并传播到未来，首次实现了新物体出现的预测。
- **结果**: 在实验中显著提升了多模态预测性能，并展示了零样本迁移能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we investigate the problem of anticipating future dynamics, particularly the future location of other vehicles and pedestrians, in the view of a moving vehicle. We approach two fundamental challenges: (1) the partial visibility due to the egocentric view with a single RGB camera and considerable field-of-view change due to the egomotion of the vehicle; (2) the multimodality of the distribution of future states. In contrast to many previous works, we do not assume structural knowledge from maps. We rather estimate a reachability prior for certain classes of objects from the semantic map of the present image and propagate it into the future using the planned egomotion. Experiments show that the reachability prior combined with multi-hypotheses learning improves multimodal prediction of the future location of tracked objects and, for the first time, the emergence of new objects. We also demonstrate promising zero-shot transfer to unseen datasets. Source code is available at $\href{https://github.com/lmb-freiburg/FLN-EPN-RPN}{\text{this https URL.}}$

</details>

### EmotiCon: Context-Aware Multimodal Emotion Recognition Using Frege's Principle. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2003.06692](https://arxiv.org/abs/2003.06692) · 📚 被引 151
- **作者**: Trisha Mittal, Pooja Guhan, Uttaran Bhattacharya, Rohan Chandra, Aniket Bera, Dinesh Manocha
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对视频和图像中人类情绪识别缺乏上下文感知的问题，提出EmotiCon算法，结合三种上下文解释：多模态（人脸和步态）、语义上下文（自注意力CNN）和社会动态交互（深度图）。在EMOTIC基准上，平均精度达到35.48，比先前方法提升7-8个点；并引入新数据集GroupWalk，平均精度65.83。
- **摘要（英）**: This paper presents EmotiCon, a context-aware emotion recognition algorithm combining multimodal, semantic, and socio-dynamic contexts. It achieves an AP of 35.48 on EMOTIC, improving 7-8 points over prior methods, and introduces the GroupWalk dataset with an AP of 65.83.
- **核心贡献**: 提出了结合三种上下文解释的情绪识别算法，并引入新数据集。
- **创新点**: 基于Frege原则，将多模态、语义和社会交互上下文统一建模。
- **结果**: 在EMOTIC和GroupWalk上均显著优于先前方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present EmotiCon, a learning-based algorithm for context-aware perceived human emotion recognition from videos and images. Motivated by Frege's Context Principle from psychology, our approach combines three interpretations of context for emotion recognition. Our first interpretation is based on using multiple modalities(e.g. faces and gaits) for emotion recognition. For the second interpretation, we gather semantic context from the input image and use a self-attention-based CNN to encode this information. Finally, we use depth maps to model the third interpretation related to socio-dynamic interactions and proximity among agents. We demonstrate the efficiency of our network through experiments on EMOTIC, a benchmark dataset. We report an Average Precision (AP) score of 35.48 across 26 classes, which is an improvement of 7-8 over prior methods. We also introduce a new dataset, GroupWalk, which is a collection of videos captured in multiple real-world settings of people walking. We report an AP of 65.83 across 4 categories on GroupWalk, which is also an improvement over prior methods.

</details>

### CoverNet: Multimodal Behavior Prediction Using Trajectory Sets. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:1911.10298](https://arxiv.org/abs/1911.10298) · 📚 被引 388
- **作者**: Tung Phan-Minh, Elena Corina Grigore, Freddy A. Boulton, Oscar Beijbom, Eric M. Wolff
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对城市驾驶中多模态、概率性轨迹预测的挑战。②提出CoverNet方法，将轨迹预测视为在多样化轨迹集上的分类问题，通过动态生成轨迹集确保状态空间覆盖并排除物理不可行轨迹。③相比多模态回归、占用图等方法，分类框架更简洁高效，且轨迹集可动态调整。④在公开真实驾驶数据集上优于现有最先进方法，展示了有效性和效率。
- **摘要（英）**: This paper tackles multimodal probabilistic trajectory prediction for urban driving. CoverNet frames prediction as classification over a diverse trajectory set, dynamically generated to ensure coverage and exclude infeasible paths. Compared to regression or occupancy-based methods, it offers a simpler and more efficient framework. Experiments on public datasets show superior performance over state-of-the-art.
- **核心贡献**: 提出基于轨迹集分类的多模态轨迹预测方法。
- **创新点**: 将轨迹预测转化为分类问题并动态生成轨迹集。
- **结果**: 在公开数据集上优于最先进方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present CoverNet, a new method for multimodal, probabilistic trajectory prediction for urban driving. Previous work has employed a variety of methods, including multimodal regression, occupancy maps, and 1-step stochastic policies. We instead frame the trajectory prediction problem as classification over a diverse set of trajectories. The size of this set remains manageable due to the limited number of distinct actions that can be taken over a reasonable prediction horizon. We structure the trajectory set to a) ensure a desired level of coverage of the state space, and b) eliminate physically impossible trajectories. By dynamically generating trajectory sets based on the agent's current state, we can further improve our method's efficiency. We demonstrate our approach on public, real-world self-driving datasets, and show that it outperforms state-of-the-art methods.

</details>

### EmotiCon: Context-Aware Multimodal Emotion Recognition Using Frege's Principle. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2003.06692](https://arxiv.org/abs/2003.06692) · 📚 被引 151
- **作者**: Trisha Mittal, Pooja Guhan, Uttaran Bhattacharya, Rohan Chandra, Aniket Bera, Dinesh Manocha
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对视频和图像中人类情绪识别缺乏上下文感知的问题，提出EmotiCon算法，结合三种上下文解释：多模态（人脸和步态）、语义上下文（自注意力CNN）和社会动态交互（深度图）。在EMOTIC基准上，平均精度达到35.48，比先前方法提升7-8个点；并引入新数据集GroupWalk，平均精度65.83。
- **摘要（英）**: This paper presents EmotiCon, a context-aware emotion recognition algorithm combining multimodal, semantic, and socio-dynamic contexts. It achieves an AP of 35.48 on EMOTIC, improving 7-8 points over prior methods, and introduces the GroupWalk dataset with an AP of 65.83.
- **核心贡献**: 提出了结合三种上下文解释的情绪识别算法，并引入新数据集。
- **创新点**: 基于Frege原则，将多模态、语义和社会交互上下文统一建模。
- **结果**: 在EMOTIC和GroupWalk上均显著优于先前方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present EmotiCon, a learning-based algorithm for context-aware perceived human emotion recognition from videos and images. Motivated by Frege's Context Principle from psychology, our approach combines three interpretations of context for emotion recognition. Our first interpretation is based on using multiple modalities(e.g. faces and gaits) for emotion recognition. For the second interpretation, we gather semantic context from the input image and use a self-attention-based CNN to encode this information. Finally, we use depth maps to model the third interpretation related to socio-dynamic interactions and proximity among agents. We demonstrate the efficiency of our network through experiments on EMOTIC, a benchmark dataset. We report an Average Precision (AP) score of 35.48 across 26 classes, which is an improvement of 7-8 over prior methods. We also introduce a new dataset, GroupWalk, which is a collection of videos captured in multiple real-world settings of people walking. We report an AP of 65.83 across 4 categories on GroupWalk, which is also an improvement over prior methods.

</details>

### CoverNet: Multimodal Behavior Prediction Using Trajectory Sets. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:1911.10298](https://arxiv.org/abs/1911.10298) · 📚 被引 388
- **作者**: Tung Phan-Minh, Elena Corina Grigore, Freddy A. Boulton, Oscar Beijbom, Eric M. Wolff
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对城市驾驶中多模态、概率性轨迹预测的挑战。②提出CoverNet方法，将轨迹预测视为在多样化轨迹集上的分类问题，通过动态生成轨迹集确保状态空间覆盖并排除物理不可行轨迹。③相比多模态回归、占用图等方法，分类框架更简洁高效，且轨迹集可动态调整。④在公开真实驾驶数据集上优于现有最先进方法，展示了有效性和效率。
- **摘要（英）**: This paper tackles multimodal probabilistic trajectory prediction for urban driving. CoverNet frames prediction as classification over a diverse trajectory set, dynamically generated to ensure coverage and exclude infeasible paths. Compared to regression or occupancy-based methods, it offers a simpler and more efficient framework. Experiments on public datasets show superior performance over state-of-the-art.
- **核心贡献**: 提出基于轨迹集分类的多模态轨迹预测方法。
- **创新点**: 将轨迹预测转化为分类问题并动态生成轨迹集。
- **结果**: 在公开数据集上优于最先进方法。

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
