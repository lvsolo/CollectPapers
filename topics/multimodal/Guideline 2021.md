# Multimodal — 2021 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Parameter Efficient Multimodal Transformers for Video Representation Learning.
- **链接**: [arXiv:2012.04124](https://arxiv.org/abs/2012.04124)
- **作者**: Sangho Lee, Youngjae Yu, Gunhee Kim, Thomas M. Breuel, Jan Kautz, Yale Song
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent success of Transformers in the language domain has motivated adapting it to a multimodal setting, where a new visual model is trained in tandem with an already pretrained language model. However, due to the excessive memory requirements from Transformers, existing work typically fixes the language model and train only the vision module, which limits its ability to learn cross-modal information in an end-to-end manner. In this work, we focus on reducing the parameters of multimodal Transformers in the context of audio-visual video representation learning. We alleviate the high memory requirement by sharing the parameters of Transformers across layers and modalities; we decompose the Transformer into modality-specific and modality-shared parts so that the model learns the dynamics of each modality both individually and together, and propose a novel parameter sharing scheme based on low-rank approximation. We show that our approach reduces parameters of the Transformers up to 97$\%$, allowing us to train our model end-to-end from scratch. We also propose a negative sampling approach based on an instance similarity measured on the CNN embedding space that our model learns together with the Transformers. To demonstrate our approach, we pretrain our model on 30-second clips (480 frames) from Kinetics-700 and transfer it to audio-visual classification tasks.

</details>

### Relating by Contrasting: A Data-efficient Framework for Multimodal Generative Models.
- **链接**: [arXiv:2007.01179](https://arxiv.org/abs/2007.01179)
- **作者**: Yuge Shi, Brooks Paige, Philip H. S. Torr, N. Siddharth
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning for generative models often refers to the learning of abstract concepts from the commonality of information in multiple modalities, such as vision and language. While it has proven effective for learning generalisable representations, the training of such models often requires a large amount of "related" multimodal data that shares commonality, which can be expensive to come by. To mitigate this, we develop a novel contrastive framework for generative model learning, allowing us to train the model not just by the commonality between modalities, but by the distinction between "related" and "unrelated" multimodal data. We show in experiments that our method enables data-efficient multimodal learning on challenging datasets for various multimodal VAE models. We also show that under our proposed framework, the generative model can accurately identify related samples from unrelated ones, making it possible to make use of the plentiful unlabeled, unpaired multimodal data.

</details>

### Generalized Multimodal ELBO.
- **链接**: [arXiv:2105.02470](https://arxiv.org/abs/2105.02470)
- **作者**: Thomas M. Sutter, Imant Daunhawer, Julia E. Vogt
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multiple data types naturally co-occur when describing real-world phenomena and learning from them is a long-standing goal in machine learning research. However, existing self-supervised generative models approximating an ELBO are not able to fulfill all desired requirements of multimodal models: their posterior approximation functions lead to a trade-off between the semantic coherence and the ability to learn the joint data distribution. We propose a new, generalized ELBO formulation for multimodal data that overcomes these limitations. The new objective encompasses two previous methods as special cases and combines their benefits without compromises. In extensive experiments, we demonstrate the advantage of the proposed method compared to state-of-the-art models in self-supervised, generative learning tasks.

</details>

### HalentNet: Multimodal Trajectory Forecasting with Hallucinative Intents.
- **链接**: [出版页](https://openreview.net/forum?id=9GBZBPn0Jx)
- **作者**: Deyao Zhu, Mohamed Zahran, Li Erran Li, Mohamed Elhoseiny
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Active Contrastive Learning of Audio-Visual Video Representations.
- **链接**: [出版页](https://openreview.net/forum?id=OMizHuea_HB)
- **作者**: Shuang Ma, Zhaoyang Zeng, Daniel McDuff, Yale Song
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
