# Multimodal — 2024 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 27 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MIntRec2.0: A Large-scale Benchmark Dataset for Multimodal Intent Recognition and Out-of-scope Detection in Conversations.
- **链接**: [arXiv:2403.10943](https://arxiv.org/abs/2403.10943) · [代码](https://github.com/thuiar/MIntRec2.0)
- **作者**: Hanlei Zhang, Xin Wang, Hua Xu, Qianrui Zhou, Kai Gao, Jianhua Su et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal intent recognition poses significant challenges, requiring the incorporation of non-verbal modalities from real-world contexts to enhance the comprehension of human intentions. Existing benchmark datasets are limited in scale and suffer from difficulties in handling out-of-scope samples that arise in multi-turn conversational interactions. We introduce MIntRec2.0, a large-scale benchmark dataset for multimodal intent recognition in multi-party conversations. It contains 1,245 dialogues with 15,040 samples, each annotated within a new intent taxonomy of 30 fine-grained classes. Besides 9,304 in-scope samples, it also includes 5,736 out-of-scope samples appearing in multi-turn contexts, which naturally occur in real-world scenarios. Furthermore, we provide comprehensive information on the speakers in each utterance, enriching its utility for multi-party conversational research. We establish a general framework supporting the organization of single-turn and multi-turn dialogue data, modality feature extraction, multimodal fusion, as well as in-scope classification and out-of-scope detection. Evaluation benchmarks are built using classic multimodal fusion methods, ChatGPT, and human evaluators. While existing methods incorporating nonverbal information yield improvements, effectively leveraging context information and detecting out-of-scope samples remains a substantial challenge. Notably, large language models exhibit a significant performance gap compared to humans, highlighting the limitations of machine learning methods in the cognitive intent understanding task. We believe that MIntRec2.0 will serve as a valuable resource, providing a pioneering foundation for research in human-machine conversational interactions, and significantly facilitating related applications. The full dataset and codes are available at https://github.com/thuiar/MIntRec2.0.

</details>

### DV-3DLane: End-to-end Multi-modal 3D Lane Detection with Dual-view Representation.
- **链接**: [arXiv:2406.16072](https://arxiv.org/abs/2406.16072) · [代码](https://github.com/JMoonr/dv-3dlane)
- **作者**: Yueru Luo, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D lane estimation is crucial for ensuring safety in autonomous driving. However, prevailing monocular techniques suffer from depth loss and lighting variations, hampering accurate 3D lane detection. In contrast, LiDAR points offer geometric cues and enable precise localization. In this paper, we present DV-3DLane, a novel end-to-end Dual-View multi-modal 3D Lane detection framework that synergizes the strengths of both images and LiDAR points. We propose to learn multi-modal features in dual-view spaces, i.e., perspective view (PV) and bird's-eye-view (BEV), effectively leveraging the modal-specific information. To achieve this, we introduce three designs: 1) A bidirectional feature fusion strategy that integrates multi-modal features into each view space, exploiting their unique strengths. 2) A unified query generation approach that leverages lane-aware knowledge from both PV and BEV spaces to generate queries. 3) A 3D dual-view deformable attention mechanism, which aggregates discriminative features from both PV and BEV spaces into queries for accurate 3D lane detection. Extensive experiments on the public benchmark, OpenLane, demonstrate the efficacy and efficiency of DV-3DLane. It achieves state-of-the-art performance, with a remarkable 11.2 gain in F1 score and a substantial 53.5% reduction in errors. The code is available at \url{https://github.com/JMoonr/dv-3dlane}.

</details>

### Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond.
- **链接**: [出版页](https://openreview.net/forum?id=khAE1sTMdX)
- **作者**: Tianxin Wei, Bowen Jin, Ruirui Li, Hansi Zeng, Zhengyang Wang, Jianhui Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning.
- **链接**: [出版页](https://openreview.net/forum?id=5KojubHBr8)
- **作者**: Haozhe Zhao, Zefan Cai, Shuzheng Si, Xiaojian Ma, Kaikai An, Liang Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Multimodal Learning Without Labeled Multimodal Data: Guarantees and Applications.
- **链接**: [arXiv:2306.04539](https://arxiv.org/abs/2306.04539)
- **作者**: Paul Pu Liang, Chun Kai Ling, Yun Cheng, Alexander Obolenskiy, Yudong Liu, Rohan Pandey et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In many machine learning systems that jointly learn from multiple modalities, a core research question is to understand the nature of multimodal interactions: how modalities combine to provide new task-relevant information that was not present in either alone. We study this challenge of interaction quantification in a semi-supervised setting with only labeled unimodal data and naturally co-occurring multimodal data (e.g., unlabeled images and captions, video and corresponding audio) but when labeling them is time-consuming. Using a precise information-theoretic definition of interactions, our key contribution is the derivation of lower and upper bounds to quantify the amount of multimodal interactions in this semi-supervised setting. We propose two lower bounds: one based on the shared information between modalities and the other based on disagreement between separately trained unimodal classifiers, and derive an upper bound through connections to approximate algorithms for min-entropy couplings. We validate these estimated bounds and show how they accurately track true interactions. Finally, we show how these theoretical results can be used to estimate multimodal model performance, guide data collection, and select appropriate multimodal models for various tasks.

</details>

### Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions.
- **链接**: [出版页](https://openreview.net/forum?id=BXY6fe7q31)
- **作者**: Juncheng Li, Kaihang Pan, Zhiqi Ge, Minghe Gao, Wei Ji, Wenqiao Zhang et al.
- **🏷️ 机构**: NUS
- **会议**: ICLR 2024

### Jointly Training Large Autoregressive Multimodal Models.
- **链接**: [arXiv:2309.15564](https://arxiv.org/abs/2309.15564)
- **作者**: Emanuele Aiello, Lili Yu, Yixin Nie, Armen Aghajanyan, Barlas Oguz
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, advances in the large-scale pretraining of language and text-to-image models have revolutionized the field of machine learning. Yet, integrating these two modalities into a single, robust model capable of generating seamless multimodal outputs remains a significant challenge. To address this gap, we present the Joint Autoregressive Mixture (JAM) framework, a modular approach that systematically fuses existing text and image generation models. We also introduce a specialized, data-efficient instruction-tuning strategy, tailored for mixed-modal generation tasks. Our final instruct-tuned model demonstrates unparalleled performance in generating high-quality multimodal outputs and represents the first model explicitly designed for this purpose.

</details>

### CLIP the Bias: How Useful is Balancing Data in Multimodal Learning?
- **链接**: [出版页](https://openreview.net/forum?id=FIGXAxr9E4)
- **作者**: Ibrahim Alabdulmohsin, Xiao Wang, Andreas Peter Steiner, Priya Goyal, Alexander D'Amour, Xiaohua Zhai
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Neuroformer: Multimodal and Multitask Generative Pretraining for Brain Data.
- **链接**: [arXiv:2311.00136](https://arxiv.org/abs/2311.00136)
- **作者**: Antonis Antoniades, Yiyi Yu, Joseph Canzano, William Yang Wang, Spencer L. Smith
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art systems neuroscience experiments yield large-scale multimodal data, and these data sets require new tools for analysis. Inspired by the success of large pretrained models in vision and language domains, we reframe the analysis of large-scale, cellular-resolution neuronal spiking data into an autoregressive spatiotemporal generation problem. Neuroformer is a multimodal, multitask generative pretrained transformer (GPT) model that is specifically designed to handle the intricacies of data in systems neuroscience. It scales linearly with feature size, can process an arbitrary number of modalities, and is adaptable to downstream tasks, such as predicting behavior. We first trained Neuroformer on simulated datasets, and found that it both accurately predicted simulated neuronal circuit activity, and also intrinsically inferred the underlying neural circuit connectivity, including direction. When pretrained to decode neural responses, the model predicted the behavior of a mouse with only few-shot fine-tuning, suggesting that the model begins learning how to do so directly from the neural representations themselves, without any explicit supervision. We used an ablation study to show that joint training on neuronal responses and behavior boosted performance, highlighting the model's ability to associate behavioral and neural representations in an unsupervised manner. These findings show that Neuroformer can analyze neural datasets and their emergent properties, informing the development of models and hypotheses associated with the brain.

</details>

### DreamLLM: Synergistic Multimodal Comprehension and Creation.
- **链接**: [arXiv:2309.11499](https://arxiv.org/abs/2309.11499)
- **作者**: Runpei Dong, Chunrui Han, Yuang Peng, Zekun Qi, Zheng Ge, Jinrong Yang et al.
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents DreamLLM, a learning framework that first achieves versatile Multimodal Large Language Models (MLLMs) empowered with frequently overlooked synergy between multimodal comprehension and creation. DreamLLM operates on two fundamental principles. The first focuses on the generative modeling of both language and image posteriors by direct sampling in the raw multimodal space. This approach circumvents the limitations and information loss inherent to external feature extractors like CLIP, and a more thorough multimodal understanding is obtained. Second, DreamLLM fosters the generation of raw, interleaved documents, modeling both text and image contents, along with unstructured layouts. This allows DreamLLM to learn all conditional, marginal, and joint multimodal distributions effectively. As a result, DreamLLM is the first MLLM capable of generating free-form interleaved content. Comprehensive experiments highlight DreamLLM's superior performance as a zero-shot multimodal generalist, reaping from the enhanced learning synergy. Project page: https://dreamllm.github.io.

</details>

### Guiding Instruction-based Image Editing via Multimodal Large Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=S1RKWSyZ2Y)
- **作者**: Tsu-Jui Fu, Wenze Hu, Xianzhi Du, William Yang Wang, Yinfei Yang, Zhe Gan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Multimodal Web Navigation with Instruction-Finetuned Foundation Models.
- **链接**: [arXiv:2305.11854](https://arxiv.org/abs/2305.11854)
- **作者**: Hiroki Furuta, Kuang-Huei Lee, Ofir Nachum, Yutaka Matsuo, Aleksandra Faust, Shixiang Shane Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The progress of autonomous web navigation has been hindered by the dependence on billions of exploratory interactions via online reinforcement learning, and domain-specific model designs that make it difficult to leverage generalization from rich out-of-domain data. In this work, we study data-driven offline training for web agents with vision-language foundation models. We propose an instruction-following multimodal agent, WebGUM, that observes both webpage screenshots and HTML pages and outputs web navigation actions, such as click and type. WebGUM is trained by jointly finetuning an instruction-finetuned language model and a vision encoder with temporal and local perception on a large corpus of demonstrations. We empirically demonstrate this recipe improves the agent's ability of grounded multimodal perception, HTML comprehension, and multi-step reasoning, outperforming prior works by a significant margin. On the MiniWoB, we improve over the previous best offline methods by more than 45.8%, even outperforming online-finetuned SoTA, humans, and GPT-4-based agent. On the WebShop benchmark, our 3-billion-parameter model achieves superior performance to the existing SoTA, PaLM-540B. Furthermore, WebGUM exhibits strong positive transfer to the real-world planning tasks on the Mind2Web. We also collect 347K high-quality demonstrations using our trained models, 38 times larger than prior work, and make them available to promote future research in this direction.

</details>

### Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages.
- **链接**: [arXiv:2308.12038](https://arxiv.org/abs/2308.12038) · [代码](https://github.com/OpenBMB/VisCPM.git)
- **作者**: Jinyi Hu, Yuan Yao, Chongyi Wang, Shan Wang, Yinxu Pan, Qianyu Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently there has been a significant surge in multimodal learning in terms of both image-to-text and text-to-image generation. However, the success is typically limited to English, leaving other languages largely behind. Building a competitive counterpart in other languages is highly challenging due to the low-resource nature of non-English multimodal data (i.e., lack of large-scale, high-quality image-text data). In this work, we propose MPM, an effective training paradigm for training large multimodal models in non-English languages. MPM demonstrates that Multilingual language models can Pivot zero-shot Multimodal learning across languages. Specifically, based on a strong multilingual large language model, multimodal models pretrained on English-only image-text data can well generalize to other languages in a (quasi)-zero-shot manner, even surpassing models trained on image-text data in native languages. Taking Chinese as a practice of MPM, we build large multimodal models VisCPM in image-to-text and text-to-image generation, which achieve state-of-the-art (open-source) performance in Chinese. To facilitate future research, we open-source codes and model weights at https://github.com/OpenBMB/VisCPM.git.

</details>

### EQA-MX: Embodied Question Answering using Multimodal Expression.
- **链接**: [出版页](https://openreview.net/forum?id=7gUrYE50Rb)
- **作者**: Md Mofijul Islam, Alexi Gladstone, Riashat Islam, Tariq Iqbal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### On the generalization capacity of neural networks during generic multimodal reasoning.
- **链接**: [arXiv:2401.15030](https://arxiv.org/abs/2401.15030)
- **作者**: Takuya Ito, Soham Dan, Mattia Rigotti, James R. Kozloski, Murray Campbell
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of the Transformer has led to the development of large language models (LLM), which appear to demonstrate human-like capabilities. To assess the generality of this class of models and a variety of other base neural network architectures to multimodal domains, we evaluated and compared their capacity for multimodal generalization. We introduce a multimodal question-answer benchmark to evaluate three specific types of out-of-distribution (OOD) generalization performance: distractor generalization (generalization in the presence of distractors), systematic compositional generalization (generalization to new task permutations), and productive compositional generalization (generalization to more complex tasks structures). We found that across model architectures (e.g., RNNs, Transformers, Perceivers, etc.), models with multiple attention layers, or models that leveraged cross-attention mechanisms between input domains, fared better. Our positive results demonstrate that for multimodal distractor and systematic generalization, either cross-modal attention or models with deeper attention layers are key architectural features required to integrate multimodal inputs. On the other hand, neither of these architectural features led to productive generalization, suggesting fundamental limitations of existing architectures for specific types of multimodal generalization. These results demonstrate the strengths and limitations of specific architectural components underlying modern neural models for multimodal reasoning. Finally, we provide Generic COG (gCOG), a configurable benchmark with several multimodal generalization splits, for future studies to explore.

</details>

### Sampling Multimodal Distributions with the Vanilla Score: Benefits of Data-Based Initialization.
- **链接**: [arXiv:2310.01762](https://arxiv.org/abs/2310.01762)
- **作者**: Frederic Koehler, Thuy-Duong Vuong
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There is a long history, as well as a recent explosion of interest, in statistical and generative modeling approaches based on score functions -- derivatives of the log-likelihood of a distribution. In seminal works, Hyvärinen proposed vanilla score matching as a way to learn distributions from data by computing an estimate of the score function of the underlying ground truth, and established connections between this method and established techniques like Contrastive Divergence and Pseudolikelihood estimation. It is by now well-known that vanilla score matching has significant difficulties learning multimodal distributions. Although there are various ways to overcome this difficulty, the following question has remained unanswered -- is there a natural way to sample multimodal distributions using just the vanilla score? Inspired by a long line of related experimental works, we prove that the Langevin diffusion with early stopping, initialized at the empirical distribution, and run on a score function estimated from data successfully generates natural multimodal distributions (mixtures of log-concave distributions).

</details>

### Deep Generative Clustering with Multimodal Diffusion Variational Autoencoders.
- **链接**: [出版页](https://openreview.net/forum?id=k5THrhXDV3)
- **作者**: Emanuele Palumbo, Laura Manduchi, Sonia Laguna, Daphné Chopard, Julia E. Vogt
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Kosmos-G: Generating Images in Context with Multimodal Large Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=he6mX9LTyE)
- **作者**: Xichen Pan, Li Dong, Shaohan Huang, Zhiliang Peng, Wenhu Chen, Furu Wei
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Grounding Multimodal Large Language Models to the World.
- **链接**: [出版页](https://openreview.net/forum?id=lLmqxkfSIw)
- **作者**: Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao, Shaohan Huang, Shuming Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning.
- **链接**: [出版页](https://openreview.net/forum?id=mMaQvkMzDi)
- **作者**: Mustafa Shukor, Alexandre Ramé, Corentin Dancette, Matthieu Cord
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### InternVid: A Large-scale Video-Text Dataset for Multimodal Understanding and Generation.
- **链接**: [arXiv:2307.06942](https://arxiv.org/abs/2307.06942)
- **作者**: Yi Wang, Yinan He, Yizhuo Li, Kunchang Li, Jiashuo Yu, Xin Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces InternVid, a large-scale video-centric multimodal dataset that enables learning powerful and transferable video-text representations for multimodal understanding and generation. The InternVid dataset contains over 7 million videos lasting nearly 760K hours, yielding 234M video clips accompanied by detailed descriptions of total 4.1B words. Our core contribution is to develop a scalable approach to autonomously build a high-quality video-text dataset with large language models (LLM), thereby showcasing its efficacy in learning video-language representation at scale. Specifically, we utilize a multi-scale approach to generate video-related descriptions. Furthermore, we introduce ViCLIP, a video-text representation learning model based on ViT-L. Learned on InternVid via contrastive learning, this model demonstrates leading zero-shot action recognition and competitive video retrieval performance. Beyond basic video understanding tasks like recognition and retrieval, our dataset and model have broad applications. They are particularly beneficial for generating interleaved video-text data for learning a video-centric dialogue system, advancing video-to-text and text-to-video generation research. These proposed resources provide a tool for researchers and practitioners interested in multimodal video understanding and generation.

</details>

### Multimodal Patient Representation Learning with Missing Modalities and Labels.
- **链接**: [出版页](https://openreview.net/forum?id=Je5SHCKpPa)
- **作者**: Zhenbang Wu, Anant Dadu, Nicholas J. Tustison, Brian B. Avants, Mike A. Nalls, Jimeng Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Neuro-Inspired Information-Theoretic Hierarchical Perception for Multimodal Learning.
- **链接**: [arXiv:2404.09403](https://arxiv.org/abs/2404.09403)
- **作者**: Xiongye Xiao, Gengshuo Liu, Gaurav Gupta, Defu Cao, Shixuan Li, Yaxing Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Integrating and processing information from various sources or modalities are critical for obtaining a comprehensive and accurate perception of the real world in autonomous systems and cyber-physical systems. Drawing inspiration from neuroscience, we develop the Information-Theoretic Hierarchical Perception (ITHP) model, which utilizes the concept of information bottleneck. Different from most traditional fusion models that incorporate all modalities identically in neural networks, our model designates a prime modality and regards the remaining modalities as detectors in the information pathway, serving to distill the flow of information. Our proposed perception model focuses on constructing an effective and compact information flow by achieving a balance between the minimization of mutual information between the latent state and the input modal state, and the maximization of mutual information between the latent states and the remaining modal states. This approach leads to compact latent state representations that retain relevant information while minimizing redundancy, thereby substantially enhancing the performance of multimodal representation learning. Experimental evaluations on the MUStARD, CMU-MOSI, and CMU-MOSEI datasets demonstrate that our model consistently distills crucial information in multimodal learning scenarios, outperforming state-of-the-art benchmarks. Remarkably, on the CMU-MOSI dataset, ITHP surpasses human-level performance in the multimodal sentiment binary classification task across all evaluation metrics (i.e., Binary Accuracy, F1 Score, Mean Absolute Error, and Pearson Correlation).

</details>

### Multimodal Molecular Pretraining via Modality Blending.
- **链接**: [出版页](https://openreview.net/forum?id=oM7Jbxdk6Z)
- **作者**: Qiying Yu, Yudi Zhang, Yuyan Ni, Shikun Feng, Yanyan Lan, Hao Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Prototypical Information Bottlenecking and Disentangling for Multimodal Cancer Survival Prediction.
- **链接**: [arXiv:2401.01646](https://arxiv.org/abs/2401.01646)
- **作者**: Yilan Zhang, Yingxue Xu, Jianqi Chen, Fengying Xie, Hao Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning significantly benefits cancer survival prediction, especially the integration of pathological images and genomic data. Despite advantages of multimodal learning for cancer survival prediction, massive redundancy in multimodal data prevents it from extracting discriminative and compact information: (1) An extensive amount of intra-modal task-unrelated information blurs discriminability, especially for gigapixel whole slide images (WSIs) with many patches in pathology and thousands of pathways in genomic data, leading to an ``intra-modal redundancy" issue. (2) Duplicated information among modalities dominates the representation of multimodal data, which makes modality-specific information prone to being ignored, resulting in an ``inter-modal redundancy" issue. To address these, we propose a new framework, Prototypical Information Bottlenecking and Disentangling (PIBD), consisting of Prototypical Information Bottleneck (PIB) module for intra-modal redundancy and Prototypical Information Disentanglement (PID) module for inter-modal redundancy. Specifically, a variant of information bottleneck, PIB, is proposed to model prototypes approximating a bunch of instances for different risk levels, which can be used for selection of discriminative instances within modality. PID module decouples entangled multimodal data into compact distinct components: modality-common and modality-specific knowledge, under the guidance of the joint prototypical distribution. Extensive experiments on five cancer benchmark datasets demonstrated our superiority over other methods.

</details>

### VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=ygxTuVz9eU)
- **作者**: Zihao Zhu, Mingda Zhang, Shaokui Wei, Bingzhe Wu, Baoyuan Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Understanding the Robustness of Multi-modal Contrastive Learning to Distribution Shift.
- **链接**: [arXiv:2310.04971](https://arxiv.org/abs/2310.04971)
- **作者**: Yihao Xue, Siddharth Joshi, Dang Nguyen, Baharan Mirzasoleiman
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, multimodal contrastive learning (MMCL) approaches, such as CLIP, have achieved a remarkable success in learning representations that are robust against distribution shift and generalize to new domains. Despite the empirical success, the mechanism behind learning such generalizable representations is not understood. In this work, we rigorously analyze this problem and uncover two mechanisms behind MMCL's robustness: \emph{intra-class contrasting}, which allows the model to learn features with a high variance, and \emph{inter-class feature sharing}, where annotated details in one class help learning other classes better. Both mechanisms prevent spurious features that are over-represented in the training data to overshadow the generalizable core features. This yields superior zero-shot classification accuracy under distribution shift. Furthermore, we theoretically demonstrate the benefits of using rich captions on robustness and explore the effect of annotating different types of details in the captions. We validate our theoretical findings through experiments, including a well-designed synthetic experiment and an experiment involving training CLIP models on MSCOCO/Conceptual Captions and evaluating them on shifted ImageNets.

</details>
