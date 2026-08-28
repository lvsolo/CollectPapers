# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 32 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-supervised Models are Good Teaching Assistants for Vision Transformers.
- **链接**: [出版页](https://proceedings.mlr.press/v162/wu22c.html)
- **作者**: Haiyan Wu, Yuting Gao, Yinqi Zhang, Shaohui Lin, Yuan Xie, Xing Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language.
- **链接**: [arXiv:2202.03555](https://arxiv.org/abs/2202.03555)
- **作者**: Alexei Baevski, Wei-Ning Hsu, Qiantong Xu, Arun Babu, Jiatao Gu, Michael Auli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While the general idea of self-supervised learning is identical across modalities, the actual algorithms and objectives differ widely because they were developed with a single modality in mind. To get us closer to general self-supervised learning, we present data2vec, a framework that uses the same learning method for either speech, NLP or computer vision. The core idea is to predict latent representations of the full input data based on a masked view of the input in a self-distillation setup using a standard Transformer architecture. Instead of predicting modality-specific targets such as words, visual tokens or units of human speech which are local in nature, data2vec predicts contextualized latent representations that contain information from the entire input. Experiments on the major benchmarks of speech recognition, image classification, and natural language understanding demonstrate a new state of the art or competitive performance to predominant approaches.

</details>

### Self-supervised learning with random-projection quantizer for speech recognition.
- **链接**: [arXiv:2202.01855](https://arxiv.org/abs/2202.01855)
- **作者**: Chung-Cheng Chiu, James Qin, Yu Zhang, Jiahui Yu, Yonghui Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a simple and effective self-supervised learning approach for speech recognition. The approach learns a model to predict the masked speech signals, in the form of discrete labels generated with a random-projection quantizer. In particular the quantizer projects speech inputs with a randomly initialized matrix, and does a nearest-neighbor lookup in a randomly-initialized codebook. Neither the matrix nor the codebook is updated during self-supervised learning. Since the random-projection quantizer is not trained and is separated from the speech recognition model, the design makes the approach flexible and is compatible with universal speech recognition architecture. On LibriSpeech our approach achieves similar word-error-rates as previous work using self-supervised learning with non-streaming models, and provides lower word-error-rates and latency than wav2vec 2.0 and w2v-BERT with streaming models. On multilingual tasks the approach also provides significant improvement over wav2vec 2.0 and w2v-BERT.

</details>

### On the Difficulty of Defending Self-Supervised Learning against Model Extraction.
- **链接**: [arXiv:2205.07890](https://arxiv.org/abs/2205.07890)
- **作者**: Adam Dziedzic, Nikita Dhawan, Muhammad Ahmad Kaleem, Jonas Guan, Nicolas Papernot
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) is an increasingly popular ML paradigm that trains models to transform complex inputs into representations without relying on explicit labels. These representations encode similarity structures that enable efficient learning of multiple downstream tasks. Recently, ML-as-a-Service providers have commenced offering trained SSL models over inference APIs, which transform user inputs into useful representations for a fee. However, the high cost involved to train these models and their exposure over APIs both make black-box extraction a realistic security threat. We thus explore model stealing attacks against SSL. Unlike traditional model extraction on classifiers that output labels, the victim models here output representations; these representations are of significantly higher dimensionality compared to the low-dimensional prediction scores output by classifiers. We construct several novel attacks and find that approaches that train directly on a victim's stolen representations are query efficient and enable high accuracy for downstream models. We then show that existing defenses against model extraction are inadequate and not easily retrofitted to the specificities of SSL.

</details>

### Exploring the Gap between Collapsed & Whitened Features in Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v162/he22c.html)
- **作者**: Bobby He, Mete Ozay
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### ContentVec: An Improved Self-Supervised Speech Representation by Disentangling Speakers.
- **链接**: [出版页](https://proceedings.mlr.press/v162/qian22b.html)
- **作者**: Kaizhi Qian, Yang Zhang, Heting Gao, Junrui Ni, Cheng-I Lai, David D. Cox et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Contrastive UCB: Provably Efficient Contrastive Self-Supervised Learning in Online Reinforcement Learning.
- **链接**: [arXiv:2207.14800](https://arxiv.org/abs/2207.14800) · [代码](https://github.com/Baichenjia/Contrastive-UCB)
- **作者**: Shuang Qiu, Lingxiao Wang, Chenjia Bai, Zhuoran Yang, Zhaoran Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In view of its power in extracting feature representation, contrastive self-supervised learning has been successfully integrated into the practice of (deep) reinforcement learning (RL), leading to efficient policy learning in various applications. Despite its tremendous empirical successes, the understanding of contrastive learning for RL remains elusive. To narrow such a gap, we study how RL can be empowered by contrastive learning in a class of Markov decision processes (MDPs) and Markov games (MGs) with low-rank transitions. For both models, we propose to extract the correct feature representations of the low-rank model by minimizing a contrastive loss. Moreover, under the online setting, we propose novel upper confidence bound (UCB)-type algorithms that incorporate such a contrastive loss with online RL algorithms for MDPs or MGs. We further theoretically prove that our algorithm recovers the true representations and simultaneously achieves sample efficiency in learning the optimal policy and Nash equilibrium in MDPs and MGs. We also provide empirical studies to demonstrate the efficacy of the UCB-based contrastive learning method for RL. To the best of our knowledge, we provide the first provably efficient online RL algorithm that incorporates contrastive learning for representation learning. Our codes are available at https://github.com/Baichenjia/Contrastive-UCB.

</details>

### Adversarial Masking for Self-Supervised Learning.
- **链接**: [arXiv:2201.13100](https://arxiv.org/abs/2201.13100) · [代码](https://github.com/YugeTen/adios)
- **作者**: Yuge Shi, N. Siddharth, Philip H. S. Torr, Adam R. Kosiorek
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose ADIOS, a masked image model (MIM) framework for self-supervised learning, which simultaneously learns a masking function and an image encoder using an adversarial objective. The image encoder is trained to minimise the distance between representations of the original and that of a masked image. The masking function, conversely, aims at maximising this distance. ADIOS consistently improves on state-of-the-art self-supervised learning (SSL) methods on a variety of tasks and datasets -- including classification on ImageNet100 and STL10, transfer learning on CIFAR10/100, Flowers102 and iNaturalist, as well as robustness evaluated on the backgrounds challenge (Xiao et al., 2021) -- while generating semantically meaningful masks. Unlike modern MIM models such as MAE, BEiT and iBOT, ADIOS does not rely on the image-patch tokenisation construction of Vision Transformers, and can be implemented with convolutional backbones. We further demonstrate that the masks learned by ADIOS are more effective in improving representation learning of SSL methods than masking schemes used in popular MIM models. Code is available at https://github.com/YugeTen/adios.

</details>

### Self-Supervised Models of Audio Effectively Explain Human Cortical Responses to Speech.
- **链接**: [arXiv:2205.14252](https://arxiv.org/abs/2205.14252)
- **作者**: Aditya R. Vaidya, Shailee Jain, Alexander Huth
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised language models are very effective at predicting high-level cortical responses during language comprehension. However, the best current models of lower-level auditory processing in the human brain rely on either hand-constructed acoustic filters or representations from supervised audio neural networks. In this work, we capitalize on the progress of self-supervised speech representation learning (SSL) to create new state-of-the-art models of the human auditory system. Compared against acoustic baselines, phonemic features, and supervised models, representations from the middle layers of self-supervised models (APC, wav2vec, wav2vec 2.0, and HuBERT) consistently yield the best prediction performance for fMRI recordings within the auditory cortex (AC). Brain areas involved in low-level auditory processing exhibit a preference for earlier SSL model layers, whereas higher-level semantic areas prefer later layers. We show that these trends are due to the models' ability to encode information at multiple linguistic levels (acoustic, phonetic, and lexical) along their representation depth. Overall, these results show that self-supervised models effectively capture the hierarchy of information relevant to different stages of speech processing in human cortex.

</details>

### Self-Supervised Representation Learning via Latent Graph Prediction.
- **链接**: [arXiv:2202.08333](https://arxiv.org/abs/2202.08333)
- **作者**: Yaochen Xie, Zhao Xu, Shuiwang Ji
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) of graph neural networks is emerging as a promising way of leveraging unlabeled data. Currently, most methods are based on contrastive learning adapted from the image domain, which requires view generation and a sufficient number of negative samples. In contrast, existing predictive models do not require negative sampling, but lack theoretical guidance on the design of pretext training tasks. In this work, we propose the LaGraph, a theoretically grounded predictive SSL framework based on latent graph prediction. Learning objectives of LaGraph are derived as self-supervised upper bounds to objectives for predicting unobserved latent graphs. In addition to its improved performance, LaGraph provides explanations for recent successes of predictive models that include invariance-based objectives. We provide theoretical analysis comparing LaGraph to related methods in different domains. Our experimental results demonstrate the superiority of LaGraph in performance and the robustness to decreasing of training sample size on both graph-level and node-level tasks.

</details>

### Omni-Granular Ego-Semantic Propagation for Self-Supervised Graph Representation Learning.
- **链接**: [arXiv:2205.15746](https://arxiv.org/abs/2205.15746)
- **作者**: Ling Yang, Shenda Hong
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised/self-supervised graph representation learning is critical for downstream node- and graph-level classification tasks. Global structure of graphs helps discriminating representations and existing methods mainly utilize the global structure by imposing additional supervisions. However, their global semantics are usually invariant for all nodes/graphs and they fail to explicitly embed the global semantics to enrich the representations. In this paper, we propose Omni-Granular Ego-Semantic Propagation for Self-Supervised Graph Representation Learning (OEPG). Specifically, we introduce instance-adaptive global-aware ego-semantic descriptors, leveraging the first- and second-order feature differences between each node/graph and hierarchical global clusters of the entire graph dataset. The descriptors can be explicitly integrated into local graph convolution as new neighbor nodes. Besides, we design an omni-granular normalization on the whole scales and hierarchies of the ego-semantic to assign attentional weight to each descriptor from an omni-granular perspective. Specialized pretext tasks and cross-iteration momentum update are further developed for local-global mutual adaptation. In downstream tasks, OEPG consistently achieves the best performance with a 2%~6% accuracy gain on multiple datasets cross scales and domains. Notably, OEPG also generalizes to quantity- and topology-imbalance scenarios.

</details>

### Identity-Disentangled Adversarial Augmentation for Self-supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v162/yang22s.html)
- **作者**: Kaiwen Yang, Tianyi Zhou, Xinmei Tian, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Robust Task Representations for Offline Meta-Reinforcement Learning via Contrastive Learning.
- **链接**: [arXiv:2206.10442](https://arxiv.org/abs/2206.10442) · [代码](https://github.com/PKU-AI-Edge/CORRO)
- **作者**: Haoqi Yuan, Zongqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study offline meta-reinforcement learning, a practical reinforcement learning paradigm that learns from offline data to adapt to new tasks. The distribution of offline data is determined jointly by the behavior policy and the task. Existing offline meta-reinforcement learning algorithms cannot distinguish these factors, making task representations unstable to the change of behavior policies. To address this problem, we propose a contrastive learning framework for task representations that are robust to the distribution mismatch of behavior policies in training and test. We design a bi-level encoder structure, use mutual information maximization to formalize task representation learning, derive a contrastive learning objective, and introduce several approaches to approximate the true distribution of negative pairs. Experiments on a variety of offline meta-reinforcement learning benchmarks demonstrate the advantages of our method over prior methods, especially on the generalization to out-of-distribution behavior policies. The code is available at https://github.com/PKU-AI-Edge/CORRO.

</details>

### Do More Negative Samples Necessarily Hurt In Contrastive Learning?
- **链接**: [arXiv:2205.01789](https://arxiv.org/abs/2205.01789)
- **作者**: Pranjal Awasthi, Nishanth Dikkala, Pritish Kamath
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent investigations in noise contrastive estimation suggest, both empirically as well as theoretically, that while having more "negative samples" in the contrastive loss improves downstream classification performance initially, beyond a threshold, it hurts downstream performance due to a "collision-coverage" trade-off. But is such a phenomenon inherent in contrastive learning? We show in a simple theoretical setting, where positive pairs are generated by sampling from the underlying latent class (introduced by Saunshi et al. (ICML 2019)), that the downstream performance of the representation optimizing the (population) contrastive loss in fact does not degrade with the number of negative samples. Along the way, we give a structural characterization of the optimal representation in our framework, for noise contrastive estimation. We also provide empirical support for our theoretical results on CIFAR-10 and CIFAR-100 datasets.

</details>

### Gaussian Mixture Variational Autoencoder with Contrastive Learning for Multi-Label Classification.
- **链接**: [arXiv:2112.00976](https://arxiv.org/abs/2112.00976)
- **作者**: Junwen Bai, Shufeng Kong, Carla P. Gomes
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-label classification (MLC) is a prediction task where each sample can have more than one label. We propose a novel contrastive learning boosted multi-label prediction model based on a Gaussian mixture variational autoencoder (C-GMVAE), which learns a multimodal prior space and employs a contrastive loss. Many existing methods introduce extra complex neural modules like graph neural networks to capture the label correlations, in addition to the prediction modules. We find that by using contrastive learning in the supervised setting, we can exploit label information effectively in a data-driven manner, and learn meaningful feature and label embeddings which capture the label correlations and enhance the predictive power. Our method also adopts the idea of learning and aligning latent spaces for both features and labels. In contrast to previous works based on a unimodal prior, C-GMVAE imposes a Gaussian mixture structure on the latent space, to alleviate the posterior collapse and over-regularization issues. C-GMVAE outperforms existing methods on multiple public datasets and can often match other models' full performance with only 50% of the training data. Furthermore, we show that the learnt embeddings provide insights into the interpretation of label-label interactions.

</details>

### Perfectly Balanced: Improving Transfer and Robustness of Supervised Contrastive Learning.
- **链接**: [arXiv:2204.07596](https://arxiv.org/abs/2204.07596)
- **作者**: Mayee F. Chen, Daniel Y. Fu, Avanika Narayan, Michael Zhang, Zhao Song, Kayvon Fatahalian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An ideal learned representation should display transferability and robustness. Supervised contrastive learning (SupCon) is a promising method for training accurate models, but produces representations that do not capture these properties due to class collapse -- when all points in a class map to the same representation. Recent work suggests that "spreading out" these representations improves them, but the precise mechanism is poorly understood. We argue that creating spread alone is insufficient for better representations, since spread is invariant to permutations within classes. Instead, both the correct degree of spread and a mechanism for breaking this invariance are necessary. We first prove that adding a weighted class-conditional InfoNCE loss to SupCon controls the degree of spread. Next, we study three mechanisms to break permutation invariance: using a constrained encoder, adding a class-conditional autoencoder, and using data augmentation. We show that the latter two encourage clustering of latent subclasses under more realistic conditions than the former. Using these insights, we show that adding a properly-weighted class-conditional InfoNCE loss and a class-conditional autoencoder to SupCon achieves 11.1 points of lift on coarse-to-fine transfer across 5 standard datasets and 4.7 points on worst-group robustness on 3 datasets, setting state-of-the-art on CelebA by 11.5 points.

</details>

### Augment with Care: Contrastive Learning for Combinatorial Problems.
- **链接**: [出版页](https://proceedings.mlr.press/v162/duan22b.html)
- **作者**: Haonan Duan, Pashootan Vaezipoor, Max B. Paulus, Yangjun Ruan, Chris J. Maddison
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Revisiting Contrastive Learning through the Lens of Neighborhood Component Analysis: an Integrated Framework.
- **链接**: [arXiv:2112.04468](https://arxiv.org/abs/2112.04468)
- **作者**: Ching-Yun Ko, Jeet Mohapatra, Sijia Liu, Pin-Yu Chen, Luca Daniel, Lily Weng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a seminal tool in self-supervised representation learning, contrastive learning has gained unprecedented attention in recent years. In essence, contrastive learning aims to leverage pairs of positive and negative samples for representation learning, which relates to exploiting neighborhood information in a feature space. By investigating the connection between contrastive learning and neighborhood component analysis (NCA), we provide a novel stochastic nearest neighbor viewpoint of contrastive learning and subsequently propose a series of contrastive losses that outperform the existing ones. Under our proposed framework, we show a new methodology to design integrated contrastive losses that could simultaneously achieve good accuracy and robustness on downstream tasks. With the integrated framework, we achieve up to 6\% improvement on the standard accuracy and 17\% improvement on the robust accuracy.

</details>

### MetAug: Contrastive Learning via Meta Feature Augmentation.
- **链接**: [arXiv:2203.05119](https://arxiv.org/abs/2203.05119)
- **作者**: Jiangmeng Li, Wenwen Qiang, Changwen Zheng, Bing Su, Hui Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What matters for contrastive learning? We argue that contrastive learning heavily relies on informative features, or "hard" (positive or negative) features. Early works include more informative features by applying complex data augmentations and large batch size or memory bank, and recent works design elaborate sampling approaches to explore informative features. The key challenge toward exploring such features is that the source multi-view data is generated by applying random data augmentations, making it infeasible to always add useful information in the augmented data. Consequently, the informativeness of features learned from such augmented data is limited. In response, we propose to directly augment the features in latent space, thereby learning discriminative representations without a large amount of input data. We perform a meta learning technique to build the augmentation generator that updates its network parameters by considering the performance of the encoder. However, insufficient input data may lead the encoder to learn collapsed features and therefore malfunction the augmentation generator. A new margin-injected regularization is further added in the objective function to avoid the encoder learning a degenerate mapping. To contrast all features in one gradient back-propagation step, we adopt the proposed optimization-driven unified contrastive loss instead of the conventional contrastive loss. Empirically, our method achieves state-of-the-art results on several benchmark datasets.

</details>

### Let Invariant Rationale Discovery Inspire Graph Contrastive Learning.
- **链接**: [arXiv:2206.07869](https://arxiv.org/abs/2206.07869) · [代码](https://github.com/lsh0520/RGCL)
- **作者**: Sihang Li, Xiang Wang, An Zhang, Yingxin Wu, Xiangnan He, Tat-Seng Chua
- **🏷️ 机构**: NUS
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leading graph contrastive learning (GCL) methods perform graph augmentations in two fashions: (1) randomly corrupting the anchor graph, which could cause the loss of semantic information, or (2) using domain knowledge to maintain salient features, which undermines the generalization to other domains. Taking an invariance look at GCL, we argue that a high-performing augmentation should preserve the salient semantics of anchor graphs regarding instance-discrimination. To this end, we relate GCL with invariant rationale discovery, and propose a new framework, Rationale-aware Graph Contrastive Learning (RGCL). Specifically, without supervision signals, RGCL uses a rationale generator to reveal salient features about graph instance-discrimination as the rationale, and then creates rationale-aware views for contrastive learning. This rationale-aware pre-training scheme endows the backbone model with the powerful representation ability, further facilitating the fine-tuning on downstream tasks. On MNIST-Superpixel and MUTAG datasets, visual inspections on the discovered rationales showcase that the rationale generator successfully captures the salient features (i.e. distinguishing semantic nodes in graphs). On biochemical molecule and social network benchmark datasets, the state-of-the-art performance of RGCL demonstrates the effectiveness of rationale-aware views for contrastive learning. Our codes are available at https://github.com/lsh0520/RGCL.

</details>

### On Finite-Sample Identifiability of Contrastive Learning-Based Nonlinear Independent Component Analysis.
- **链接**: [arXiv:2206.06593](https://arxiv.org/abs/2206.06593)
- **作者**: Qi Lyu, Xiao Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Nonlinear independent component analysis (nICA) aims at recovering statistically independent latent components that are mixed by unknown nonlinear functions. Central to nICA is the identifiability of the latent components, which had been elusive until very recently. Specifically, Hyvärinen et al. have shown that the nonlinearly mixed latent components are identifiable (up to often inconsequential ambiguities) under a generalized contrastive learning (GCL) formulation, given that the latent components are independent conditioned on a certain auxiliary variable. The GCL-based identifiability of nICA is elegant, and establishes interesting connections between nICA and popular unsupervised/self-supervised learning paradigms in representation learning, causal learning, and factor disentanglement. However, existing identifiability analyses of nICA all build upon an unlimited sample assumption and the use of ideal universal function learners -- which creates a non-negligible gap between theory and practice. Closing the gap is a nontrivial challenge, as there is a lack of established ``textbook'' routine for finite sample analysis of such unsupervised problems. This work puts forth a finite-sample identifiability analysis of GCL-based nICA. Our analytical framework judiciously combines the properties of the GCL loss function, statistical generalization analysis, and numerical differentiation. Our framework also takes the learning function's approximation error into consideration, and reveals an intuitive trade-off between the complexity and expressiveness of the employed function learner. Numerical experiments are used to validate the theorems.

</details>

### Utilizing Expert Features for Contrastive Learning of Time-Series Representations.
- **链接**: [arXiv:2206.11517](https://arxiv.org/abs/2206.11517)
- **作者**: Manuel T. Nonnenmacher, Lukas Oldenburg, Ingo Steinwart, David Reeb
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present an approach that incorporates expert knowledge for time-series representation learning. Our method employs expert features to replace the commonly used data transformations in previous contrastive learning approaches. We do this since time-series data frequently stems from the industrial or medical field where expert features are often available from domain experts, while transformations are generally elusive for time-series data. We start by proposing two properties that useful time-series representations should fulfill and show that current representation learning approaches do not ensure these properties. We therefore devise ExpCLR, a novel contrastive learning approach built on an objective that utilizes expert features to encourage both properties for the learned representation. Finally, we demonstrate on three real-world time-series datasets that ExpCLR surpasses several state-of-the-art methods for both unsupervised and semi-supervised representation learning.

</details>

### Interventional Contrastive Learning with Meta Semantic Regularizer.
- **链接**: [arXiv:2206.14702](https://arxiv.org/abs/2206.14702)
- **作者**: Wenwen Qiang, Jiangmeng Li, Changwen Zheng, Bing Su, Hui Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning (CL)-based self-supervised learning models learn visual representations in a pairwise manner. Although the prevailing CL model has achieved great progress, in this paper, we uncover an ever-overlooked phenomenon: When the CL model is trained with full images, the performance tested in full images is better than that in foreground areas; when the CL model is trained with foreground areas, the performance tested in full images is worse than that in foreground areas. This observation reveals that backgrounds in images may interfere with the model learning semantic information and their influence has not been fully eliminated. To tackle this issue, we build a Structural Causal Model (SCM) to model the background as a confounder. We propose a backdoor adjustment-based regularization method, namely Interventional Contrastive Learning with Meta Semantic Regularizer (ICL-MSR), to perform causal intervention towards the proposed SCM. ICL-MSR can be incorporated into any existing CL methods to alleviate background distractions from representation learning. Theoretically, we prove that ICL-MSR achieves a tighter error bound. Empirically, our experiments on multiple benchmark datasets demonstrate that ICL-MSR is able to improve the performances of different state-of-the-art CL methods.

</details>

### Understanding Contrastive Learning Requires Incorporating Inductive Biases.
- **链接**: [arXiv:2202.14037](https://arxiv.org/abs/2202.14037)
- **作者**: Nikunj Saunshi, Jordan T. Ash, Surbhi Goel, Dipendra Misra, Cyril Zhang, Sanjeev Arora et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning is a popular form of self-supervised learning that encourages augmentations (views) of the same input to have more similar representations compared to augmentations of different inputs. Recent attempts to theoretically explain the success of contrastive learning on downstream classification tasks prove guarantees depending on properties of {\em augmentations} and the value of {\em contrastive loss} of representations. We demonstrate that such analyses, that ignore {\em inductive biases} of the function class and training algorithm, cannot adequately explain the success of contrastive learning, even {\em provably} leading to vacuous guarantees in some settings. Extensive experiments on image and text domains highlight the ubiquity of this problem -- different function classes and algorithms behave very differently on downstream tasks, despite having the same augmentations and contrastive losses. Theoretical analysis is presented for the class of linear representations, where incorporating inductive biases of the function class allows contrastive learning to work with less stringent conditions compared to prior analyses.

</details>

### Connect, Not Collapse: Explaining Contrastive Learning for Unsupervised Domain Adaptation.
- **链接**: [arXiv:2204.00570](https://arxiv.org/abs/2204.00570)
- **作者**: Kendrick Shen, Robbie M. Jones, Ananya Kumar, Sang Michael Xie, Jeff Z. HaoChen, Tengyu Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider unsupervised domain adaptation (UDA), where labeled data from a source domain (e.g., photographs) and unlabeled data from a target domain (e.g., sketches) are used to learn a classifier for the target domain. Conventional UDA methods (e.g., domain adversarial training) learn domain-invariant features to improve generalization to the target domain. In this paper, we show that contrastive pre-training, which learns features on unlabeled source and target data and then fine-tunes on labeled source data, is competitive with strong UDA methods. However, we find that contrastive pre-training does not learn domain-invariant features, diverging from conventional UDA intuitions. We show theoretically that contrastive pre-training can learn features that vary subtantially across domains but still generalize to the target domain, by disentangling domain and class information. Our results suggest that domain invariance is not necessary for UDA. We empirically validate our theory on benchmark vision datasets.

</details>

### Robustness Verification for Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v162/wang22q.html)
- **作者**: Zekai Wang, Weiwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Partial and Asymmetric Contrastive Learning for Out-of-Distribution Detection in Long-Tailed Recognition.
- **链接**: [arXiv:2207.01160](https://arxiv.org/abs/2207.01160) · [代码](https://github.com/amazon-research/long-tailed-ood-detection)
- **作者**: Haotao Wang, Aston Zhang, Yi Zhu, Shuai Zheng, Mu Li, Alex J. Smola et al.
- **🏷️ 机构**: AWS / CMU
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing out-of-distribution (OOD) detection methods are typically benchmarked on training sets with balanced class distributions. However, in real-world applications, it is common for the training sets to have long-tailed distributions. In this work, we first demonstrate that existing OOD detection methods commonly suffer from significant performance degradation when the training set is long-tail distributed. Through analysis, we posit that this is because the models struggle to distinguish the minority tail-class in-distribution samples, from the true OOD samples, making the tail classes more prone to be falsely detected as OOD. To solve this problem, we propose Partial and Asymmetric Supervised Contrastive Learning (PASCL), which explicitly encourages the model to distinguish between tail-class in-distribution samples and OOD samples. To further boost in-distribution classification accuracy, we propose Auxiliary Branch Finetuning, which uses two separate branches of BN and classification layers for anomaly detection and in-distribution classification, respectively. The intuition is that in-distribution and OOD anomaly data have different underlying distributions. Our method outperforms previous state-of-the-art method by $1.29\%$, $1.45\%$, $0.69\%$ anomaly detection false positive rate (FPR) and $3.24\%$, $4.06\%$, $7.89\%$ in-distribution classification accuracy on CIFAR10-LT, CIFAR100-LT, and ImageNet-LT, respectively. Code and pre-trained models are available at https://github.com/amazon-research/long-tailed-ood-detection.

</details>

### ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v162/xia22b.html)
- **作者**: Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

### Investigating Why Contrastive Learning Benefits Robustness against Label Noise.
- **链接**: [arXiv:2201.12498](https://arxiv.org/abs/2201.12498)
- **作者**: Yihao Xue, Kyle Whitecross, Baharan Mirzasoleiman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised Contrastive Learning (CL) has been recently shown to be very effective in preventing deep networks from overfitting noisy labels. Despite its empirical success, the theoretical understanding of the effect of contrastive learning on boosting robustness is very limited. In this work, we rigorously prove that the representation matrix learned by contrastive learning boosts robustness, by having: (i) one prominent singular value corresponding to each sub-class in the data, and significantly smaller remaining singular values; and (ii) {a large alignment between the prominent singular vectors and the clean labels of each sub-class. The above properties enable a linear layer trained on such representations to effectively learn the clean labels without overfitting the noise.} We further show that the low-rank structure of the Jacobian of deep networks pre-trained with contrastive learning allows them to achieve a superior performance initially, when fine-tuned on noisy labels. Finally, we demonstrate that the initial robustness provided by contrastive learning enables robust training methods to achieve state-of-the-art performance under extreme noise levels, e.g., an average of 27.18\% and 15.58\% increase in accuracy on CIFAR-10 and CIFAR-100 with 80\% symmetric noisy labels, and 4.11\% increase in accuracy on WebVision.

</details>

### Provable Stochastic Optimization for Global Contrastive Learning: Small Batch Does Not Harm Performance.
- **链接**: [arXiv:2202.12387](https://arxiv.org/abs/2202.12387)
- **作者**: Zhuoning Yuan, Yuexin Wu, Zi-Hao Qiu, Xianzhi Du, Lijun Zhang, Denny Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study contrastive learning from an optimization perspective, aiming to analyze and address a fundamental issue of existing contrastive learning methods that either rely on a large batch size or a large dictionary of feature vectors. We consider a global objective for contrastive learning, which contrasts each positive pair with all negative pairs for an anchor point. From the optimization perspective, we explain why existing methods such as SimCLR require a large batch size in order to achieve a satisfactory result. In order to remove such requirement, we propose a memory-efficient Stochastic Optimization algorithm for solving the Global objective of Contrastive Learning of Representations, named SogCLR. We show that its optimization error is negligible under a reasonable condition after a sufficient number of iterations or is diminishing for a slightly different global contrastive objective. Empirically, we demonstrate that SogCLR with small batch size (e.g., 256) can achieve similar performance as SimCLR with large batch size (e.g., 8192) on self-supervised learning task on ImageNet-1K. We also attempt to show that the proposed optimization technique is generic and can be applied to solving other contrastive losses, e.g., two-way contrastive losses for bimodal contrastive learning. The proposed method is implemented in our open-sourced library LibAUC (www.libauc.org).

</details>

### Contrastive Learning with Boosted Memorization.
- **链接**: [arXiv:2205.12693](https://arxiv.org/abs/2205.12693) · [代码](https://github.com/MediaBrain-SJTU/BCL)
- **作者**: Zhihan Zhou, Jiangchao Yao, Yanfeng Wang, Bo Han, Ya Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has achieved a great success in the representation learning of visual and textual data. However, the current methods are mainly validated on the well-curated datasets, which do not exhibit the real-world long-tailed distribution. Recent attempts to consider self-supervised long-tailed learning are made by rebalancing in the loss perspective or the model perspective, resembling the paradigms in the supervised long-tailed learning. Nevertheless, without the aid of labels, these explorations have not shown the expected significant promise due to the limitation in tail sample discovery or the heuristic structure design. Different from previous works, we explore this direction from an alternative perspective, i.e., the data perspective, and propose a novel Boosted Contrastive Learning (BCL) method. Specifically, BCL leverages the memorization effect of deep neural networks to automatically drive the information discrepancy of the sample views in contrastive learning, which is more efficient to enhance the long-tailed learning in the label-unaware context. Extensive experiments on a range of benchmark datasets demonstrate the effectiveness of BCL over several state-of-the-art methods. Our code is available at https://github.com/MediaBrain-SJTU/BCL.

</details>

## 跨领域论文（完整笔记在其他领域）

- MAE-DET: Revisiting Maximum Entropy Principle in Zero-Shot NAS for Efficient Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
