# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 23 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### For self-supervised learning, Rationality implies generalization, provably.
- **链接**: [arXiv:2010.08508](https://arxiv.org/abs/2010.08508)
- **作者**: Yamini Bansal, Gal Kaplun, Boaz Barak
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We prove a new upper bound on the generalization gap of classifiers that are obtained by first using self-supervision to learn a representation $r$ of the training data, and then fitting a simple (e.g., linear) classifier $g$ to the labels. Specifically, we show that (under the assumptions described below) the generalization gap of such classifiers tends to zero if $\mathsf{C}(g) \ll n$, where $\mathsf{C}(g)$ is an appropriately-defined measure of the simple classifier $g$'s complexity, and $n$ is the number of training samples. We stress that our bound is independent of the complexity of the representation $r$. We do not make any structural or conditional-independence assumptions on the representation-learning task, which can use the same training dataset that is later used for classification. Rather, we assume that the training procedure satisfies certain natural noise-robustness (adding small amount of label noise causes small degradation in performance) and rationality (getting the wrong label is not better than getting no label at all) conditions that widely hold across many standard architectures. We show that our bound is non-vacuous for many popular representation-learning based classifiers on CIFAR-10 and ImageNet, including SimCLR, AMDIM and MoCo.

</details>

### CoCon: A Self-Supervised Approach for Controlled Text Generation.
- **链接**: [arXiv:2006.03535](https://arxiv.org/abs/2006.03535)
- **作者**: Alvin Chan, Yew-Soon Ong, Bill Pung, Aston Zhang, Jie Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained Transformer-based language models (LMs) display remarkable natural language generation capabilities. With their immense potential, controlling text generation of such LMs is getting attention. While there are studies that seek to control high-level attributes (such as sentiment and topic) of generated text, there is still a lack of more precise control over its content at the word- and phrase-level. Here, we propose Content-Conditioner (CoCon) to control an LM's output text with a content input, at a fine-grained level. In our self-supervised approach, the CoCon block learns to help the LM complete a partially-observed text sequence by conditioning with content inputs that are withheld from the LM. Through experiments, we show that CoCon can naturally incorporate target content into generated texts and control high-level text attributes in a zero-shot manner.

</details>

### SEED: Self-supervised Distillation For Visual Representation.
- **链接**: [arXiv:2101.04731](https://arxiv.org/abs/2101.04731)
- **作者**: Zhiyuan Fang, Jianfeng Wang, Lijuan Wang, Lei Zhang, Yezhou Yang, Zicheng Liu
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper is concerned with self-supervised learning for small models. The problem is motivated by our empirical studies that while the widely used contrastive self-supervised learning method has shown great progress on large model training, it does not work well for small models. To address this problem, we propose a new learning paradigm, named SElf-SupErvised Distillation (SEED), where we leverage a larger network (as Teacher) to transfer its representational knowledge into a smaller architecture (as Student) in a self-supervised fashion. Instead of directly learning from unlabeled data, we train a student encoder to mimic the similarity score distribution inferred by a teacher over a set of instances. We show that SEED dramatically boosts the performance of small networks on downstream tasks. Compared with self-supervised baselines, SEED improves the top-1 accuracy from 42.2% to 67.6% on EfficientNet-B0 and from 36.3% to 68.2% on MobileNet-v3-Large on the ImageNet-1k dataset.

</details>

### Self-supervised Adversarial Robustness for the Low-label, High-data Regime.
- **链接**: [出版页](https://openreview.net/forum?id=bgQek2O63w)
- **作者**: Sven Gowal, Po-Sen Huang, Aäron van den Oord, Timothy A. Mann, Pushmeet Kohli
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Self-Supervised Policy Adaptation during Deployment.
- **链接**: [arXiv:2007.04309](https://arxiv.org/abs/2007.04309)
- **作者**: Nicklas Hansen, Rishabh Jangir, Yu Sun, Guillem Alenyà, Pieter Abbeel, Alexei A. Efros et al.
- **🏷️ 机构**: UC Berkeley
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In most real world scenarios, a policy trained by reinforcement learning in one environment needs to be deployed in another, potentially quite different environment. However, generalization across different environments is known to be hard. A natural solution would be to keep training after deployment in the new environment, but this cannot be done if the new environment offers no reward signal. Our work explores the use of self-supervision to allow the policy to continue training after deployment without using any rewards. While previous methods explicitly anticipate changes in the new environment, we assume no prior knowledge of those changes yet still obtain significant improvements. Empirical evaluations are performed on diverse simulation environments from DeepMind Control suite and ViZDoom, as well as real robotic manipulation tasks in continuously changing environments, taking observations from an uncalibrated camera. Our method improves generalization in 31 out of 36 environments across various tasks and outperforms domain randomization on a majority of environments.

</details>

### On Self-Supervised Image Representations for GAN Evaluation.
- **链接**: [出版页](https://openreview.net/forum?id=NeRdBeTionN)
- **作者**: Stanislav Morozov, Andrey Voynov, Artem Babenko
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Mathematical Reasoning via Self-supervised Skip-tree Training.
- **链接**: [出版页](https://openreview.net/forum?id=YmqAnY0CMEy)
- **作者**: Markus Norman Rabe, Dennis Lee, Kshitij Bansal, Christian Szegedy
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### SSD: A Unified Framework for Self-Supervised Outlier Detection.
- **链接**: [arXiv:2103.12051](https://arxiv.org/abs/2103.12051) · [代码](https://github.com/inspire-group/SSD)
- **作者**: Vikash Sehwag, Mung Chiang, Prateek Mittal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We ask the following question: what training information is required to design an effective outlier/out-of-distribution (OOD) detector, i.e., detecting samples that lie far away from the training distribution? Since unlabeled data is easily accessible for many applications, the most compelling approach is to develop detectors based on only unlabeled in-distribution data. However, we observe that most existing detectors based on unlabeled data perform poorly, often equivalent to a random prediction. In contrast, existing state-of-the-art OOD detectors achieve impressive performance but require access to fine-grained data labels for supervised training. We propose SSD, an outlier detector based on only unlabeled in-distribution data. We use self-supervised representation learning followed by a Mahalanobis distance based detection in the feature space. We demonstrate that SSD outperforms most existing detectors based on unlabeled data by a large margin. Additionally, SSD even achieves performance on par, and sometimes even better, with supervised training based detectors. Finally, we expand our detection framework with two key extensions. First, we formulate few-shot OOD detection, in which the detector has access to only one to five samples from each class of the targeted OOD dataset. Second, we extend our framework to incorporate training data labels, if available. We find that our novel detection framework based on SSD displays enhanced performance with these extensions, and achieves state-of-the-art performance. Our code is publicly available at https://github.com/inspire-group/SSD.

</details>

### Online Adversarial Purification based on Self-supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=_i3ASPp12WS)
- **作者**: Changhao Shi, Chester Holtz, Gal Mishne
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Model-Based Visual Planning with Self-Supervised Functional Distances.
- **链接**: [arXiv:2012.15373](https://arxiv.org/abs/2012.15373)
- **作者**: Stephen Tian, Suraj Nair, Frederik Ebert, Sudeep Dasari, Benjamin Eysenbach, Chelsea Finn et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A generalist robot must be able to complete a variety of tasks in its environment. One appealing way to specify each task is in terms of a goal observation. However, learning goal-reaching policies with reinforcement learning remains a challenging problem, particularly when hand-engineered reward functions are not available. Learned dynamics models are a promising approach for learning about the environment without rewards or task-directed data, but planning to reach goals with such a model requires a notion of functional similarity between observations and goal states. We present a self-supervised method for model-based visual goal reaching, which uses both a visual dynamics model as well as a dynamical distance function learned using model-free reinforcement learning. Our approach learns entirely using offline, unlabeled data, making it practical to scale to large and diverse datasets. In our experiments, we find that our method can successfully learn models that perform a variety of tasks at test-time, moving objects amid distractors with a simulated robotic arm and even learning to open and close a drawer using a real-world robot. In comparisons, we find that this approach substantially outperforms both model-free and model-based prior methods. Videos and visualizations are available here: http://sites.google.com/berkeley.edu/mbold.

</details>

### Self-supervised Representation Learning with Relative Predictive Coding.
- **链接**: [出版页](https://openreview.net/forum?id=068E_JSq9O)
- **作者**: Yao-Hung Hubert Tsai, Martin Q. Ma, Muqiao Yang, Han Zhao, Louis-Philippe Morency, Ruslan Salakhutdinov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Self-Supervised Learning of Compressed Video Representations.
- **链接**: [出版页](https://openreview.net/forum?id=jMPcEkJpdD)
- **作者**: Youngjae Yu, Sangho Lee, Gunhee Kim, Yale Song
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Self-supervised Visual Reinforcement Learning with Object-centric Representations.
- **链接**: [arXiv:2011.14381](https://arxiv.org/abs/2011.14381)
- **作者**: Andrii Zadaianchuk, Maximilian Seitzer, Georg Martius
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous agents need large repertoires of skills to act reasonably on new tasks that they have not seen before. However, acquiring these skills using only a stream of high-dimensional, unstructured, and unlabeled observations is a tricky challenge for any autonomous agent. Previous methods have used variational autoencoders to encode a scene into a low-dimensional vector that can be used as a goal for an agent to discover new skills. Nevertheless, in compositional/multi-object environments it is difficult to disentangle all the factors of variation into such a fixed-length representation of the whole scene. We propose to use object-centric representations as a modular and structured observation space, which is learned with a compositional generative world model. We show that the structure in the representations in combination with goal-conditioned attention policies helps the autonomous agent to discover and learn useful skills. These skills can be further combined to address compositional tasks like the manipulation of several different objects.

</details>

### What Should Not Be Contrastive in Contrastive Learning.
- **链接**: [arXiv:2008.05659](https://arxiv.org/abs/2008.05659)
- **作者**: Tete Xiao, Xiaolong Wang, Alexei A. Efros, Trevor Darrell
- **🏷️ 机构**: UC Berkeley
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent self-supervised contrastive methods have been able to produce impressive transferable visual representations by learning to be invariant to different data augmentations. However, these methods implicitly assume a particular set of representational invariances (e.g., invariance to color), and can perform poorly when a downstream task violates this assumption (e.g., distinguishing red vs. yellow cars). We introduce a contrastive learning framework which does not require prior knowledge of specific, task-dependent invariances. Our model learns to capture varying and invariant factors for visual representations by constructing separate embedding spaces, each of which is invariant to all but one augmentation. We use a multi-head network with a shared backbone which captures information across each augmentation and alone outperforms all baselines on downstream tasks. We further find that the concatenation of the invariant and varying spaces performs best across all tasks we investigate, including coarse-grained, fine-grained, and few-shot downstream classification tasks, and various data corruptions.

</details>

### Prototypical Contrastive Learning of Unsupervised Representations.
- **链接**: [arXiv:2005.04966](https://arxiv.org/abs/2005.04966) · [代码](https://github.com/salesforce/PCL)
- **作者**: Junnan Li, Pan Zhou, Caiming Xiong, Steven C. H. Hoi
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents Prototypical Contrastive Learning (PCL), an unsupervised representation learning method that addresses the fundamental limitations of instance-wise contrastive learning. PCL not only learns low-level features for the task of instance discrimination, but more importantly, it implicitly encodes semantic structures of the data into the learned embedding space. Specifically, we introduce prototypes as latent variables to help find the maximum-likelihood estimation of the network parameters in an Expectation-Maximization framework. We iteratively perform E-step as finding the distribution of prototypes via clustering and M-step as optimizing the network via contrastive learning. We propose ProtoNCE loss, a generalized version of the InfoNCE loss for contrastive learning, which encourages representations to be closer to their assigned prototypes. PCL outperforms state-of-the-art instance-wise contrastive learning methods on multiple benchmarks with substantial improvement in low-resource transfer learning. Code and pretrained models are available at https://github.com/salesforce/PCL.

</details>

### Supervised Contrastive Learning for Pre-trained Language Model Fine-tuning.
- **链接**: [arXiv:2011.01403](https://arxiv.org/abs/2011.01403)
- **作者**: Beliz Gunel, Jingfei Du, Alexis Conneau, Veselin Stoyanov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art natural language understanding classification models follow two-stages: pre-training a large language model on an auxiliary task, and then fine-tuning the model on a task-specific labeled dataset using cross-entropy loss. However, the cross-entropy loss has several shortcomings that can lead to sub-optimal generalization and instability. Driven by the intuition that good generalization requires capturing the similarity between examples in one class and contrasting them with examples in other classes, we propose a supervised contrastive learning (SCL) objective for the fine-tuning stage. Combined with cross-entropy, our proposed SCL loss obtains significant improvements over a strong RoBERTa-Large baseline on multiple datasets of the GLUE benchmark in few-shot learning settings, without requiring specialized architecture, data augmentations, memory banks, or additional unsupervised data. Our proposed fine-tuning objective leads to models that are more robust to different levels of noise in the fine-tuning training data, and can generalize better to related tasks with limited labeled data.

</details>

### Universal Weakly Supervised Segmentation by Pixel-to-Segment Contrastive Learning.
- **链接**: [arXiv:2105.00957](https://arxiv.org/abs/2105.00957) · [代码](https://github.com/twke18/SPML)
- **作者**: Tsung-Wei Ke, Jyh-Jing Hwang, Stella X. Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised segmentation requires assigning a label to every pixel based on training instances with partial annotations such as image-level tags, object bounding boxes, labeled points and scribbles. This task is challenging, as coarse annotations (tags, boxes) lack precise pixel localization whereas sparse annotations (points, scribbles) lack broad region coverage. Existing methods tackle these two types of weak supervision differently: Class activation maps are used to localize coarse labels and iteratively refine the segmentation model, whereas conditional random fields are used to propagate sparse labels to the entire image. We formulate weakly supervised segmentation as a semi-supervised metric learning problem, where pixels of the same (different) semantics need to be mapped to the same (distinctive) features. We propose 4 types of contrastive relationships between pixels and segments in the feature space, capturing low-level image similarity, semantic annotation, co-occurrence, and feature affinity They act as priors; the pixel-wise feature can be learned from training images with any partial annotations in a data-driven fashion. In particular, unlabeled pixels in training images participate not only in data-driven grouping within each image, but also in discriminative feature learning within and across images. We deliver a universal weakly supervised segmenter with significant gains on Pascal VOC and DensePose. Our code is publicly available at https://github.com/twke18/SPML.

</details>

### Contrastive Learning with Adversarial Perturbations for Conditional Text Generation.
- **链接**: [arXiv:2012.07280](https://arxiv.org/abs/2012.07280)
- **作者**: Seanie Lee, Dong Bok Lee, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, sequence-to-sequence (seq2seq) models with the Transformer architecture have achieved remarkable performance on various conditional text generation tasks, such as machine translation. However, most of them are trained with teacher forcing with the ground truth label given at each time step, without being exposed to incorrectly generated tokens during training, which hurts its generalization to unseen inputs, that is known as the "exposure bias" problem. In this work, we propose to mitigate the conditional text generation problem by contrasting positive pairs with negative pairs, such that the model is exposed to various valid or incorrect perturbations of the inputs, for improved generalization. However, training the model with naive contrastive learning framework using random non-target sequences as negative examples is suboptimal, since they are easily distinguishable from the correct output, especially so with models pretrained with large text corpora. Also, generating positive examples requires domain-specific augmentation heuristics which may not generalize over diverse domains. To tackle this problem, we propose a principled method to generate positive and negative samples for contrastive learning of seq2seq models. Specifically, we generate negative examples by adding small perturbations to the input sequence to minimize its conditional likelihood, and positive examples by adding large perturbations while enforcing it to have a high conditional likelihood. Such "hard" positive and negative pairs generated using our method guides the model to better distinguish correct outputs from incorrect ones. We empirically show that our proposed method significantly improves the generalization of the seq2seq on three text generation tasks - machine translation, text summarization, and question generation.

</details>

### Contrastive Learning with Hard Negative Samples.
- **链接**: [出版页](https://openreview.net/forum?id=CR1XOQ0UTh-)
- **作者**: Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Conditional Negative Sampling for Contrastive Learning of Visual Representations.
- **链接**: [出版页](https://openreview.net/forum?id=v8b3e5jN66j)
- **作者**: Mike Wu, Milan Mossé, Chengxu Zhuang, Daniel Yamins, Noah D. Goodman
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval.
- **链接**: [出版页](https://openreview.net/forum?id=zeFrfgyZln)
- **作者**: Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul N. Bennett et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

## 跨领域论文（完整笔记在其他领域）

- Self-supervised Learning from a Multi-view Perspective. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Active Contrastive Learning of Audio-Visual Video Representations. → [multimodal](../multimodal/Guideline%202021.md)
