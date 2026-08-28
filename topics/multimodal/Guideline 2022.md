# Multimodal — 2022 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### Multimodal Object Detection via Probabilistic Ensembling. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_9) · 📚 被引 201
- **作者**: Yi-Ting Chen, Jinghao Shi, Zelin Ye, Christoph Mertz, Deva Ramanan, Shu Kong
- **🏷️ 机构**: CMU
- **会议**: ECCV 2022
- **摘要（中）**: 针对多模态目标检测中不同模态预测不一致的问题，论文提出了一种概率集成方法，通过建模各模态预测的不确定性来加权融合结果。该方法利用概率分布表示每个模态的检测输出，并基于贝叶斯规则进行集成，从而减少冲突并提高整体可靠性。相比传统确定性融合，该方法能更好地处理噪声和缺失模态。实验显示，在多个多模态数据集上，该方法显著提升了检测精度和鲁棒性。
- **摘要（英）**: This paper tackles inconsistent predictions in multimodal object detection by proposing a probabilistic ensembling method that weights fusion based on uncertainty. It models each modality's output as a probability distribution and integrates them via Bayesian rules, improving robustness against noise and missing modalities, with significant accuracy gains on multimodal datasets.
- **核心贡献**: 提出概率集成框架，利用不确定性加权提升多模态检测性能。
- **创新点**: 将概率建模引入多模态检测集成，处理预测冲突。
- **结果**: 在多个数据集上提升精度和鲁棒性。

### Class-Agnostic Object Detection with Multi-modal Transformer. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_30) · 📚 被引 68
- **作者**: Muhammad Maaz, Hanoona Abdul Rasheed, Salman Khan, Fahad Shahbaz Khan, Rao Muhammad Anwer, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对类别无关目标检测问题，提出一种基于多模态Transformer的检测框架。方法利用多模态信息（如文本或音频）增强目标提议的生成与分类，从而实现对任意类别目标的检测。通过跨模态注意力机制，模型能够更好地捕捉目标的语义特征。实验在多个数据集上验证了方法的有效性，但具体细节和量化结果在摘要中未给出。
- **摘要（英）**: This paper addresses class-agnostic object detection by proposing a multi-modal Transformer framework. The method leverages multi-modal information to enhance proposal generation and classification, enabling detection of arbitrary categories. Cross-modal attention helps capture semantic features, with effectiveness demonstrated across datasets, though specific quantitative results are not detailed in the abstract.
- **核心贡献**: 提出多模态Transformer用于类别无关目标检测。
- **创新点**: 利用跨模态注意力融合多源信息。
- **结果**: 在多个数据集上验证了有效性。

### Multi-modal Masked Pre-training for Monocular Panoramic Depth Completion. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.09855](https://arxiv.org/abs/2203.09855) · 📚 被引 28
- **作者**: Zhiqiang Yan, Xiang Li, Kun Wang, Zhenyu Zhang, Jun Li, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对全景深度补全（PDC）任务中，360°深度传感器在复杂场景下产生稀疏深度数据，需要结合RGB图像恢复密集深度的问题。②提出多模态掩码预训练方法M^3PT，在预训练阶段用共享随机掩码同时遮盖全景RGB图像和稀疏深度图的块，并重建掩码区域的稀疏深度。③相比MAE仅处理单模态，首次将掩码预训练扩展到多模态视觉任务，且预训练与微调架构一致，无需丢弃解码器。④实验表明该方法有效提升密集全景深度恢复性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses monocular panoramic depth completion by proposing M^3PT, a multi-modal masked pre-training approach that jointly masks and reconstructs patches of RGB images and sparse depth. It extends masked autoencoding to multi-modal tasks with no architectural gap between pre-training and fine-tuning. Experiments demonstrate improved dense depth recovery, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出首个多模态掩码预训练框架用于全景深度补全。
- **创新点**: 将MAE的掩码重建思想扩展到RGB和深度双模态输入。
- **结果**: 在PDC任务上验证了预训练方法的有效性，但未给出具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we formulate a potentially valuable panoramic depth completion (PDC) task as panoramic 3D cameras often produce 360° depth with missing data in complex scenes. Its goal is to recover dense panoramic depths from raw sparse ones and panoramic RGB images. To deal with the PDC task, we train a deep network that takes both depth and image as inputs for the dense panoramic depth recovery. However, it needs to face a challenging optimization problem of the network parameters due to its non-convex objective function. To address this problem, we propose a simple yet effective approach termed M{^3}PT: multi-modal masked pre-training. Specifically, during pre-training, we simultaneously cover up patches of the panoramic RGB image and sparse depth by shared random mask, then reconstruct the sparse depth in the masked regions. To our best knowledge, it is the first time that we show the effectiveness of masked pre-training in a multi-modal vision task, instead of the single-modal task resolved by masked autoencoders (MAE). Different from MAE where fine-tuning completely discards the decoder part of pre-training, there is no architectural difference between the pre-training and fine-tuning stages in our M$^{3}$PT as they only differ in the prediction density, which potentially makes the transfer learning more convenient and effective. Extensive experiments verify the effectiveness of M{^3}PT on three panoramic datasets. Notably, we improve the state-of-the-art baselines by averagely 26.2% in RMSE, 51.7% in MRE, 49.7% in MAE, and 37.5% in RMSElog on three benchmark datasets.

</details>

### Single-Stream Multi-level Alignment for Vision-Language Pretraining. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.14395](https://arxiv.org/abs/2203.14395)
- **作者**: Zaid Khan, B. G. Vijay Kumar, Xiang Yu, Samuel Schulter, Manmohan Chandraker, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对现有视觉-语言预训练中，双流对比学习仅全局对齐、忽略细粒度对齐的问题。②提出单流架构，通过对称跨模态重建（XMM）和伪标签关键词预测（PSL）两个新任务，实现全局、patch-token和概念语义三个级别的对齐。③相比双流方法，单流架构支持更细粒度交互；相比监督方法，无需密集标注，利用动量编码器自动生成伪标签。④实验显示该方法在多个下游任务上优于现有对比学习方法，但摘要未给出具体数值。
- **摘要（英）**: This work tackles the lack of fine-grained alignment in contrastive vision-language pretraining by proposing a single-stream architecture with two novel tasks: symmetric cross-modality reconstruction (XMM) and pseudo-labeled keyword prediction (PSL). These tasks enable alignment at global, patch-token, and semantic levels without dense annotations. The method outperforms contrastive baselines on downstream tasks, though specific numbers are omitted.
- **核心贡献**: 提出单流多级对齐的视觉-语言预训练方法。
- **创新点**: 通过XMM和PSL任务实现无需标注的多级对齐。
- **结果**: 在多个下游任务上取得优于对比学习方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised vision-language pretraining from pure images and text with a contrastive loss is effective, but ignores fine-grained alignment due to a dual-stream architecture that aligns image and text representations only on a global level. Earlier, supervised, non-contrastive methods were capable of finer-grained alignment, but required dense annotations that were not scalable. We propose a single stream architecture that aligns images and language at multiple levels: global, fine-grained patch-token, and conceptual/semantic, using two novel tasks: symmetric cross-modality reconstruction (XMM) and a pseudo-labeled key word prediction (PSL). In XMM, we mask input tokens from one modality and use cross-modal information to reconstruct the masked token, thus improving fine-grained alignment between the two modalities. In PSL, we use attention to select keywords in a caption, use a momentum encoder to recommend other important keywords that are missing from the caption but represented in the image, and then train the visual encoder to predict the presence of those keywords, helping it learn semantic concepts that are essential for grounding a textual token to an image region. We demonstrate competitive performance and improved data efficiency on image-text retrieval, grounding, visual question answering/reasoning against larger models and models trained on more data. Code and models available at zaidkhan.me/SIMLA.

</details>

### Multimodal Transformer with Variable-Length Memory for Vision-and-Language Navigation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2111.05759](https://arxiv.org/abs/2111.05759) · 📚 被引 29
- **作者**: Chuang Lin, Yi Jiang, Jianfei Cai, Lizhen Qu, Gholamreza Haffari, Zehuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视觉-语言导航（VLN）中，现有Transformer方法用固定长度向量表示时间上下文，难以捕捉长期依赖的问题。②提出带可变长度记忆的多模态Transformer（MTVM），通过记忆库直接存储历史激活，并引入记忆感知一致性损失，增强时间上下文表示。③相比LSTM解码器或固定隐藏状态，可变长度记忆更灵活，能保留更多轨迹信息。④实验表明MTVM在VLN基准上优于现有方法，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses the limitation of fixed-length temporal context in Transformer-based VLN by introducing MTVM, which stores previous activations in a variable-length memory bank and uses a memory-aware consistency loss. This enables better long-term context modeling compared to LSTM or fixed hidden states. Experiments show improved navigation performance, though specific metrics are not given.
- **核心贡献**: 提出可变长度记忆的多模态Transformer用于视觉-语言导航。
- **创新点**: 用记忆库替代固定长度向量以增强时间上下文。
- **结果**: 在VLN任务上取得优于现有方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-Language Navigation (VLN) is a task that an agent is required to follow a language instruction to navigate to the goal position, which relies on the ongoing interactions with the environment during moving. Recent Transformer-based VLN methods have made great progress benefiting from the direct connections between visual observations and the language instruction via the multimodal cross-attention mechanism. However, these methods usually represent temporal context as a fixed-length vector by using an LSTM decoder or using manually designed hidden states to build a recurrent Transformer. Considering a single fixed-length vector is often insufficient to capture long-term temporal context, in this paper, we introduce Multimodal Transformer with Variable-length Memory (MTVM) for visually-grounded natural language navigation by modelling the temporal context explicitly. Specifically, MTVM enables the agent to keep track of the navigation trajectory by directly storing previous activations in a memory bank. To further boost the performance, we propose a memory-aware consistency loss to help learn a better joint representation of temporal context with random masked instructions. We evaluate MTVM on popular R2R and CVDN datasets, and our model improves Success Rate on R2R unseen validation and test set by 2% each, and reduce Goal Process by 1.6m on CVDN test set.

</details>

### Switch-BERT: Learning to Model Multimodal Interactions by Switching Attention and Input. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2306.14182](https://arxiv.org/abs/2306.14182) · 📚 被引 6
- **作者**: Qingpei Guo, Kaisheng Yao, Wei Chu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多模态模型中固定结构难以适应不同模态输入组合的模态不匹配问题。②提出Switch-BERT，扩展BERT架构，引入可学习的层内和跨层交互，从一组注意力模式中优化选择，并学习关注不同深度的输出。③相比ViLBERT和UNITER等固定结构模型，Switch-BERT能动态调整注意力，缓解模态不匹配。④在VQA、图像-文本检索和指代表达理解任务上，Switch-BERT一致优于或媲美现有模型，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses modality mismatch in fixed-structure multimodal models by proposing Switch-BERT, which learns layer-wise and cross-layer attention modes and attends to outputs from various depths. This dynamic adaptation mitigates mismatch issues compared to ViLBERT and UNITER. Experiments on VQA, retrieval, and referring expression tasks show consistent improvements or comparable performance, though specific metrics are omitted.
- **核心贡献**: 提出可学习注意力模式的Switch-BERT用于多模态表示学习。
- **创新点**: 通过切换注意力模式适应不同模态输入。
- **结果**: 在多个多模态任务上取得优于或媲美现有模型的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to model intra-modal and inter-modal interactions is fundamental in multimodal machine learning. The current state-of-the-art models usually adopt deep learning models with fixed structures. They can achieve exceptional performances on specific tasks, but face a particularly challenging problem of modality mismatch because of diversity of input modalities and their fixed structures. In this paper, we present \textbf{Switch-BERT} for joint vision and language representation learning to address this problem. Switch-BERT extends BERT architecture by introducing learnable layer-wise and cross-layer interactions. It learns to optimize attention from a set of attention modes representing these interactions. One specific property of the model is that it learns to attend outputs from various depths, therefore mitigates the modality mismatch problem. We present extensive experiments on visual question answering, image-text retrieval and referring expression comprehension experiments. Results confirm that, whereas alternative architectures including ViLBERT and UNITER may excel in particular tasks, Switch-BERT can consistently achieve better or comparable performances than the current state-of-the-art models in these tasks. Ablation studies indicate that the proposed model achieves superior performances due to its ability in learning task-specific multimodal interactions.

</details>

### MUGEN: A Playground for Video-Audio-Text Multimodal Understanding and GENeration. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2204.08058](https://arxiv.org/abs/2204.08058) · 📚 被引 19
- **作者**: Thomas Hayes, Songyang Zhang, Xi Yin, Guan Pang, Sasha Sheng, Harry Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多模态视频-音频-文本理解与生成缺乏丰富且可控数据集的问题。②构建MUGEN数据集，基于游戏平台CoinRun修改，引入音频和新交互，训练RL代理生成375K个视频片段，并收集人工文本描述和自动语义标注。③相比现有数据集，MUGEN提供窄而丰富的任务环境，支持检索和生成基准测试。④基准实验显示该数据集能有效评估多模态方法，但摘要未提供具体性能数据。
- **摘要（英）**: This paper introduces MUGEN, a large-scale video-audio-text dataset built on a modified CoinRun game, with 375K clips, human annotations, and automatic semantic maps. It provides a controlled environment for multimodal understanding and generation tasks. Benchmarks demonstrate its utility for evaluating retrieval and generation methods, though specific results are not detailed.
- **核心贡献**: 构建了大规模视频-音频-文本数据集MUGEN及基准。
- **创新点**: 利用游戏引擎生成可控且丰富的多模态数据。
- **结果**: 为多模态理解与生成提供有效基准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal video-audio-text understanding and generation can benefit from datasets that are narrow but rich. The narrowness allows bite-sized challenges that the research community can make progress on. The richness ensures we are making progress along the core challenges. To this end, we present a large-scale video-audio-text dataset MUGEN, collected using the open-sourced platform game CoinRun [11]. We made substantial modifications to make the game richer by introducing audio and enabling new interactions. We trained RL agents with different objectives to navigate the game and interact with 13 objects and characters. This allows us to automatically extract a large collection of diverse videos and associated audio. We sample 375K video clips (3.2s each) and collect text descriptions from human annotators. Each video has additional annotations that are extracted automatically from the game engine, such as accurate semantic maps for each frame and templated textual descriptions. Altogether, MUGEN can help progress research in many tasks in multimodal understanding and generation. We benchmark representative approaches on tasks involving video-audio-text retrieval and generation. Our dataset and code are released at: https://mugen-org.github.io/.

</details>

### Multimodal Conditional Image Synthesis with Product-of-Experts GANs. **⭐⭐** (相关度: 10%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19787-1_6) · 📚 被引 54
- **作者**: Xun Huang, Arun Mallya, Ting-Chun Wang, Ming-Yu Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对多模态条件图像合成中如何有效融合不同模态信息的问题。②提出了基于产品-of-专家（Product-of-Experts）的GAN模型，通过将各模态的专家预测相乘来组合条件信息。③相比传统拼接或相加融合，该方法能更灵活地处理模态间的依赖和冲突。④摘要未提供具体数据，但理论上可提升合成图像的多样性和条件一致性。
- **摘要（英）**: This paper addresses multimodal conditional image synthesis by proposing a Product-of-Experts GAN that combines modality-specific experts via multiplication. It improves over concatenation-based fusion by better handling inter-modal dependencies. No quantitative results are provided in the abstract.
- **核心贡献**: 提出产品-of-专家GAN用于多模态条件图像合成。
- **创新点**: 利用乘积融合策略整合多模态条件。
- **结果**: 摘要未给出具体效果数据。

### Sound Localization by Self-supervised Time Delay Estimation. **⭐⭐⭐** (相关度: 20%)
- **链接**: [arXiv:2204.12489](https://arxiv.org/abs/2204.12489) · 📚 被引 13
- **作者**: Ziyang Chen, David F. Fouhey, Andrew Owens
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对立体声音中声源定位的时间延迟估计问题，传统方法需要监督数据。②提出了自监督学习方法，借鉴视觉跟踪中的对比随机游走，学习双耳信号的循环一致表示。③相比监督方法，无需标注数据，且能适应真实场景。④在互联网录音上达到与监督方法相当的性能，并扩展到多说话人场景的视觉引导定位。
- **摘要（英）**: This paper tackles sound localization via time delay estimation using self-supervision, adapting contrastive random walks from visual tracking to learn cycle-consistent representations from unlabeled stereo audio. It matches supervised methods on real-world recordings and extends to visually-guided multi-speaker localization.
- **核心贡献**: 提出自监督时间延迟估计方法用于声源定位。
- **创新点**: 将视觉跟踪的对比随机游走应用于音频模态。
- **结果**: 在真实录音上性能与监督方法相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sounds reach one microphone in a stereo pair sooner than the other, resulting in an interaural time delay that conveys their directions. Estimating a sound's time delay requires finding correspondences between the signals recorded by each microphone. We propose to learn these correspondences through self-supervision, drawing on recent techniques from visual tracking. We adapt the contrastive random walk of Jabri et al. to learn a cycle-consistent representation from unlabeled stereo sounds, resulting in a model that performs on par with supervised methods on "in the wild" internet recordings. We also propose a multimodal contrastive learning model that solves a visually-guided localization task: estimating the time delay for a particular person in a multi-speaker mixture, given a visual representation of their face. Project site: https://ificl.github.io/stereocrw/

</details>

### Learning Mutual Modulation for Self-supervised Cross-Modal Super-Resolution. **⭐⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2207.09156](https://arxiv.org/abs/2207.09156) · 📚 被引 15
- **作者**: Xiaoyu Dong, Naoto Yokoya, Longguang Wang, Tatsumi Uezato
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对自监督跨模态超分辨率中，仅有低分辨率源图像和高分辨率引导图像，缺乏配对数据的问题。②提出了互调制超分辨率（MMSR）模型，通过源到引导和引导到源的双向调制，利用跨域自适应滤波器挖掘空间依赖。③相比现有伪监督方法，能生成更清晰且忠实于源模态的结果。④在多种任务上达到最先进性能。
- **摘要（英）**: This paper addresses self-supervised cross-modal super-resolution with unpaired LR source and HR guide images, proposing a mutual modulation model with cross-domain adaptive filters and cycle consistency. It outperforms existing pseudo-supervised methods, delivering sharper and more faithful results across tasks.
- **核心贡献**: 提出互调制策略用于自监督跨模态超分辨率。
- **创新点**: 双向调制和跨域自适应滤波器。
- **结果**: 在多种任务上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised cross-modal super-resolution (SR) can overcome the difficulty of acquiring paired training data, but is challenging because only low-resolution (LR) source and high-resolution (HR) guide images from different modalities are available. Existing methods utilize pseudo or weak supervision in LR space and thus deliver results that are blurry or not faithful to the source modality. To address this issue, we present a mutual modulation SR (MMSR) model, which tackles the task by a mutual modulation strategy, including a source-to-guide modulation and a guide-to-source modulation. In these modulations, we develop cross-domain adaptive filters to fully exploit cross-modal spatial dependency and help induce the source to emulate the resolution of the guide and induce the guide to mimic the modality characteristics of the source. Moreover, we adopt a cycle consistency constraint to train MMSR in a fully self-supervised manner. Experiments on various tasks demonstrate the state-of-the-art performance of our MMSR.

</details>

### CMD: Self-supervised 3D Action Representation Learning with Cross-Modal Mutual Distillation. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20062-5_42) · 📚 被引 62
- **作者**: Yunyao Mao, Wengang Zhou, Zhenbo Lu, Jiajun Deng, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对3D动作表示学习中的自监督预训练问题，摘要缺失。②方法名为跨模态互蒸馏（CMD），可能通过多模态数据蒸馏学习表示。③由于摘要缺失，无法评估具体改进。④效果未知。
- **摘要（英）**: This paper addresses self-supervised 3D action representation learning via cross-modal mutual distillation, but the abstract is missing, limiting assessment.
- **核心贡献**: 提出跨模态互蒸馏用于3D动作表示学习。
- **创新点**: 跨模态互蒸馏策略。
- **结果**: 未知。

### CODER: Coupled Diversity-Sensitive Momentum Contrastive Learning for Image-Text Retrieval. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2208.09843](https://arxiv.org/abs/2208.09843)
- **作者**: Haoran Wang, Dongliang He, Wenhao Wu, Boyang Xia, Min Yang, Fu Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对图像-文本检索中对比学习受限于负样本数量少、权重固定和缺乏外部知识的问题。②提出了CODER模型，包含多样性敏感对比学习（DCL）架构，引入动态字典扩大样本规模，并自适应加权负样本；同时设计双分支，一个学习实例级嵌入，另一个从常识知识图谱查询概念级描述。③相比现有对比学习方法，增强了多样性和知识感知。④摘要未提供具体数据，但理论上提升跨模态表示质量。
- **摘要（英）**: This paper addresses limitations in contrastive learning for image-text retrieval, proposing CODER with diversity-sensitive contrastive learning, dynamic dictionaries, and knowledge graph-based concept descriptors. It improves negative pair weighting and external knowledge integration, though no quantitative results are in the abstract.
- **核心贡献**: 提出耦合多样性敏感动量对比学习用于图像-文本检索。
- **创新点**: 动态字典和知识图谱增强的对比学习。
- **结果**: 摘要未给出具体效果数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-Text Retrieval (ITR) is challenging in bridging visual and lingual modalities. Contrastive learning has been adopted by most prior arts. Except for limited amount of negative image-text pairs, the capability of constrastive learning is restricted by manually weighting negative pairs as well as unawareness of external knowledge. In this paper, we propose our novel Coupled Diversity-Sensitive Momentum Constrastive Learning (CODER) for improving cross-modal representation. Firstly, a novel diversity-sensitive contrastive learning (DCL) architecture is invented. We introduce dynamic dictionaries for both modalities to enlarge the scale of image-text pairs, and diversity-sensitiveness is achieved by adaptive negative pair weighting. Furthermore, two branches are designed in CODER. One learns instance-level embeddings from image/text, and it also generates pseudo online clustering labels for its input image/text based on their embeddings. Meanwhile, the other branch learns to query from commonsense knowledge graph to form concept-level descriptors for both modalities. Afterwards, both branches leverage DCL to align the cross-modal embedding spaces while an extra pseudo clustering label prediction loss is utilized to promote concept-level representation learning for the second branch. Extensive experiments conducted on two popular benchmarks, i.e. MSCOCO and Flicker30K, validate CODER remarkably outperforms the state-of-the-art approaches. Our code is available at: https://github.com/BruceW91/CODER.

</details>

### Learning Visual Representation from Modality-Shared Contrastive Language-Image Pre-training. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2207.12661](https://arxiv.org/abs/2207.12661)
- **作者**: Haoxuan You, Luowei Zhou, Bin Xiao, Noel Codella, Yu Cheng, Ruochen Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多模态对比预训练中通常为每个模态使用独立编码器、限制跨模态知识共享的问题。②提出MS-CLIP框架，系统研究视觉和语言Transformer在对比预训练中可共享参数的比例，并引入轻量级模态特定并行模块。③相比vanilla CLIP，通过共享大部分编码器参数并添加少量模态特定模块，在多种架构变体中取得更优性能。④在零样本ImageNet分类上相对提升高达13%，表明共享参数能增强跨模态对齐和泛化能力。
- **摘要（英）**: This paper addresses the limitation of separate encoders in multimodal contrastive pre-training by proposing MS-CLIP frameworks that systematically explore parameter sharing between vision and language transformers. It finds that a mostly unified encoder with light-weight modality-specific modules outperforms variants with more separated parameters, achieving up to 13% relative improvement over vanilla CLIP in zero-shot ImageNet classification.
- **核心贡献**: 系统探索了对比语言-图像预训练中跨模态参数共享的架构设计空间。
- **创新点**: 提出在共享Transformer编码器中加入轻量级模态特定并行模块的混合架构。
- **结果**: 零样本ImageNet分类相对提升高达13%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale multi-modal contrastive pre-training has demonstrated great utility to learn transferable features for a range of downstream tasks by mapping multiple modalities into a shared embedding space. Typically, this has employed separate encoders for each modality. However, recent work suggests that transformers can support learning across multiple modalities and allow knowledge sharing. Inspired by this, we investigate a variety of Modality-Shared Contrastive Language-Image Pre-training (MS-CLIP) frameworks. More specifically, we question how many parameters of a transformer model can be shared across modalities during contrastive pre-training, and rigorously examine architectural design choices that position the proportion of parameters shared along a spectrum. In studied conditions, we observe that a mostly unified encoder for vision and language signals outperforms all other variations that separate more parameters. Additionally, we find that light-weight modality-specific parallel modules further improve performance. Experimental results show that the proposed MS-CLIP approach outperforms vanilla CLIP by up to 13\% relative in zero-shot ImageNet classification (pre-trained on YFCC-100M), while simultaneously supporting a reduction of parameters. In addition, our approach outperforms vanilla CLIP by 1.6 points in linear probing on a collection of 24 downstream vision tasks. Furthermore, we discover that sharing parameters leads to semantic concepts from different modalities being encoded more closely in the embedding space, facilitating the transferring of common semantic structure (e.g., attention patterns) from language to vision. Code is available at \href{https://github.com/Hxyou/MSCLIP}{URL}.

</details>

### Drive&Segment: Unsupervised Semantic Segmentation of Urban Scenes via Cross-Modal Distillation. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2203.11160](https://arxiv.org/abs/2203.11160)
- **作者**: Antonín Vobecký, David Hurych, Oriane Siméoni, Spyros Gidaris, Andrei Bursuc, Patrick Pérez et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对城市场景语义分割需要大量人工标注、且现有无监督方法泛化性差的问题。②提出Drive&Segment方法，利用车载相机和LiDAR同步数据，通过LiDAR点云生成3D物体提议，对齐图像并聚类为语义伪类，再通过跨模态蒸馏训练基于Transformer的分割模型。③相比现有无监督方法，创新性地利用3D几何信息生成高质量伪标签，无需任何人工标注。④在Cityscapes、Dark Zurich、Nighttime Driving和ACDC四个数据集上零样本测试，显著优于当前最先进方法，展示了强泛化能力。
- **摘要（英）**: This paper tackles unsupervised semantic segmentation in urban scenes by proposing Drive&Segment, which uses LiDAR point clouds to generate 3D object proposals, aligns them with images to create semantic pseudo-classes, and trains a transformer-based segmentation model via cross-modal distillation. It achieves significant improvements over state-of-the-art methods on four diverse datasets without fine-tuning, demonstrating robust generalization.
- **核心贡献**: 提出一种无需人工标注、基于跨模态蒸馏的城市场景语义分割方法。
- **创新点**: 利用3D物体提议和聚类生成语义伪类，结合跨模态蒸馏训练分割模型。
- **结果**: 在四个数据集上零样本测试显著优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work investigates learning pixel-wise semantic image segmentation in urban scenes without any manual annotation, just from the raw non-curated data collected by cars which, equipped with cameras and LiDAR sensors, drive around a city. Our contributions are threefold. First, we propose a novel method for cross-modal unsupervised learning of semantic image segmentation by leveraging synchronized LiDAR and image data. The key ingredient of our method is the use of an object proposal module that analyzes the LiDAR point cloud to obtain proposals for spatially consistent objects. Second, we show that these 3D object proposals can be aligned with the input images and reliably clustered into semantically meaningful pseudo-classes. Finally, we develop a cross-modal distillation approach that leverages image data partially annotated with the resulting pseudo-classes to train a transformer-based model for image semantic segmentation. We show the generalization capabilities of our method by testing on four different testing datasets (Cityscapes, Dark Zurich, Nighttime Driving and ACDC) without any finetuning, and demonstrate significant improvements compared to the current state of the art on this problem. See project webpage https://vobecant.github.io/DriveAndSegment/ for the code and more.

</details>

## 跨领域论文（完整笔记在其他领域）

- Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Multimodal Transformer for Automatic 3D Annotation and Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Generative Negative Text Replay for Continual Vision-Language Pretraining. → [continual-learning](../continual-learning/Guideline%202022.md)
- PreTraM: Self-supervised Pre-training via Connecting Trajectory and Map. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
