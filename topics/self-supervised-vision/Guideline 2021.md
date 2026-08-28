# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 58 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Aligning Pretraining for Detection via Object-Level Contrastive Learning.
- **链接**: [arXiv:2106.02637](https://arxiv.org/abs/2106.02637) · [代码](https://github.com/hologerry/SoCo)
- **作者**: Fangyun Wei, Yue Gao, Zhirong Wu, Han Hu, Stephen Lin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-level contrastive representation learning has proven to be highly effective as a generic model for transfer learning. Such generality for transfer learning, however, sacrifices specificity if we are interested in a certain downstream task. We argue that this could be sub-optimal and thus advocate a design principle which encourages alignment between the self-supervised pretext task and the downstream task. In this paper, we follow this principle with a pretraining method specifically designed for the task of object detection. We attain alignment in the following three aspects: 1) object-level representations are introduced via selective search bounding boxes as object proposals; 2) the pretraining network architecture incorporates the same dedicated modules used in the detection pipeline (e.g. FPN); 3) the pretraining is equipped with object detection properties such as object-level translation invariance and scale invariance. Our method, called Selective Object COntrastive learning (SoCo), achieves state-of-the-art results for transfer performance on COCO detection using a Mask R-CNN framework. Code is available at https://github.com/hologerry/SoCo.

</details>

### Leveraging SE(3) Equivariance for Self-supervised Category-Level Object Pose Estimation from Point Clouds.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/81e74d678581a3bb7a720b019f4f1a93-Abstract.html)
- **作者**: Xiaolong Li, Yijia Weng, Li Yi, Leonidas J. Guibas, A. Lynn Abbott, Shuran Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Self-Supervised Multi-Object Tracking with Cross-input Consistency.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/71e09b16e21f7b6919bbfc43f6a5b2f0-Abstract.html)
- **作者**: Favyen Bastani, Songtao He, Samuel Madden
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Self-Supervised Bug Detection and Repair.
- **链接**: [arXiv:2105.12787](https://arxiv.org/abs/2105.12787)
- **作者**: Miltiadis Allamanis, Henry Jackson-Flux, Marc Brockschmidt
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine learning-based program analyses have recently shown the promise of integrating formal and probabilistic reasoning towards aiding software development. However, in the absence of large annotated corpora, training these analyses is challenging. Towards addressing this, we present BugLab, an approach for self-supervised learning of bug detection and repair. BugLab co-trains two models: (1) a detector model that learns to detect and repair bugs in code, (2) a selector model that learns to create buggy code for the detector to use as training data. A Python implementation of BugLab improves by up to 30% upon baseline methods on a test dataset of 2374 real-life bugs and finds 19 previously unknown bugs in open-source software.

</details>

### Dynamic Bottleneck for Robust Self-Supervised Exploration.
- **链接**: [arXiv:2110.10735](https://arxiv.org/abs/2110.10735)
- **作者**: Chenjia Bai, Lingxiao Wang, Lei Han, Animesh Garg, Jianye Hao, Peng Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Exploration methods based on pseudo-count of transitions or curiosity of dynamics have achieved promising results in solving reinforcement learning with sparse rewards. However, such methods are usually sensitive to environmental dynamics-irrelevant information, e.g., white-noise. To handle such dynamics-irrelevant information, we propose a Dynamic Bottleneck (DB) model, which attains a dynamics-relevant representation based on the information-bottleneck principle. Based on the DB model, we further propose DB-bonus, which encourages the agent to explore state-action pairs with high information gain. We establish theoretical connections between the proposed DB-bonus, the upper confidence bound (UCB) for linear case, and the visiting count for tabular case. We evaluate the proposed method on Atari suits with dynamics-irrelevant noises. Our experiments show that exploration with DB bonus outperforms several state-of-the-art exploration methods in noisy environments.

</details>

### The functional specialization of visual cortex emerges from training parallel pathways with self-supervised predictive learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/d384dec9f5f7a64a36b5c8f03b8a6d92-Abstract.html) · 📚 被引 30
- **作者**: Shahab Bakhtiari, Patrick J. Mineault, Timothy P. Lillicrap, Christopher C. Pack, Blake A. Richards
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### SEAL: Self-supervised Embodied Active Learning using Exploration and 3D Consistency.
- **链接**: [arXiv:2112.01001](https://arxiv.org/abs/2112.01001)
- **作者**: Devendra Singh Chaplot, Murtaza Dalal, Saurabh Gupta, Jitendra Malik, Ruslan Salakhutdinov
- **🏷️ 机构**: UC Berkeley
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we explore how we can build upon the data and models of Internet images and use them to adapt to robot vision without requiring any extra labels. We present a framework called Self-supervised Embodied Active Learning (SEAL). It utilizes perception models trained on internet images to learn an active exploration policy. The observations gathered by this exploration policy are labelled using 3D consistency and used to improve the perception model. We build and utilize 3D semantic maps to learn both action and perception in a completely self-supervised manner. The semantic map is used to compute an intrinsic motivation reward for training the exploration policy and for labelling the agent observations using spatio-temporal 3D consistency and label propagation. We demonstrate that the SEAL framework can be used to close the action-perception loop: it improves object detection and instance segmentation performance of a pretrained perception model by just moving around in training environments and the improved perception model can be used to improve Object Goal Navigation.

</details>

### Neural Analysis and Synthesis: Reconstructing Speech from Self-Supervised Representations.
- **链接**: [arXiv:2110.14513](https://arxiv.org/abs/2110.14513)
- **作者**: Hyeong-Seok Choi, Juheon Lee, Wansoo Kim, Jie Lee, Hoon Heo, Kyogu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a neural analysis and synthesis (NANSY) framework that can manipulate voice, pitch, and speed of an arbitrary speech signal. Most of the previous works have focused on using information bottleneck to disentangle analysis features for controllable synthesis, which usually results in poor reconstruction quality. We address this issue by proposing a novel training strategy based on information perturbation. The idea is to perturb information in the original input signal (e.g., formant, pitch, and frequency response), thereby letting synthesis networks selectively take essential attributes to reconstruct the input signal. Because NANSY does not need any bottleneck structures, it enjoys both high reconstruction quality and controllability. Furthermore, NANSY does not require any labels associated with speech data such as text and speaker information, but rather uses a new set of analysis features, i.e., wav2vec feature and newly proposed pitch feature, Yingram, which allows for fully self-supervised training. Taking advantage of fully self-supervised training, NANSY can be easily extended to a multilingual setting by simply training it with a multilingual dataset. The experiments show that NANSY can achieve significant improvement in performance in several applications such as zero-shot voice conversion, pitch shift, and time-scale modification.

</details>

### Revitalizing CNN Attention via Transformers in Self-Supervised Visual Representation Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/21be992eb8016e541a15953eee90760e-Abstract.html)
- **作者**: Chongjian Ge, Youwei Liang, Yibing Song, Jianbo Jiao, Jue Wang, Ping Luo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### There Is No Turning Back: A Self-Supervised Approach for Reversibility-Aware Reinforcement Learning.
- **链接**: [arXiv:2106.04480](https://arxiv.org/abs/2106.04480)
- **作者**: Nathan Grinsztajn, Johan Ferret, Olivier Pietquin, Philippe Preux, Matthieu Geist
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose to learn to distinguish reversible from irreversible actions for better informed decision-making in Reinforcement Learning (RL). From theoretical considerations, we show that approximate reversibility can be learned through a simple surrogate task: ranking randomly sampled trajectory events in chronological order. Intuitively, pairs of events that are always observed in the same order are likely to be separated by an irreversible sequence of actions. Conveniently, learning the temporal order of events can be done in a fully self-supervised way, which we use to estimate the reversibility of actions from experience, without any priors. We propose two different strategies that incorporate reversibility in RL agents, one strategy for exploration (RAE) and one strategy for control (RAC). We demonstrate the potential of reversibility-aware agents in several environments, including the challenging Sokoban game. In synthetic tasks, we show that we can learn control policies that never fail and reduce to zero the side-effects of interactions, even without access to the reward function.

</details>

### Self-Supervised Learning of Event-Based Optical Flow with Spiking Neural Networks.
- **链接**: [arXiv:2106.01862](https://arxiv.org/abs/2106.01862)
- **作者**: Jesse J. Hagenaars, Federico Paredes-Vallés, Guido de Croon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of neuromorphic computing promises extremely low-power and low-latency sensing and processing. Challenges in transferring learning algorithms from traditional artificial neural networks (ANNs) to spiking neural networks (SNNs) have so far prevented their application to large-scale, complex regression tasks. Furthermore, realizing a truly asynchronous and fully neuromorphic pipeline that maximally attains the abovementioned benefits involves rethinking the way in which this pipeline takes in and accumulates information. In the case of perception, spikes would be passed as-is and one-by-one between an event camera and an SNN, meaning all temporal integration of information must happen inside the network. In this article, we tackle these two problems. We focus on the complex task of learning to estimate optical flow from event-based camera inputs in a self-supervised manner, and modify the state-of-the-art ANN training pipeline to encode minimal temporal information in its inputs. Moreover, we reformulate the self-supervised loss function for event-based optical flow to improve its convexity. We perform experiments with various types of recurrent ANNs and SNNs using the proposed pipeline. Concerning SNNs, we investigate the effects of elements such as parameter initialization and optimization, surrogate gradient shape, and adaptive neuronal mechanisms. We find that initialization and surrogate gradient width play a crucial part in enabling learning with sparse inputs, while the inclusion of adaptivity and learnable neuronal parameters can improve performance. We show that the performance of the proposed ANNs and SNNs are on par with that of the current state-of-the-art ANNs trained in a self-supervised manner.

</details>

### Provable Guarantees for Self-Supervised Deep Learning with Spectral Contrastive Loss.
- **链接**: [arXiv:2106.04156](https://arxiv.org/abs/2106.04156)
- **作者**: Jeff Z. HaoChen, Colin Wei, Adrien Gaidon, Tengyu Ma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works in self-supervised learning have advanced the state-of-the-art by relying on the contrastive learning paradigm, which learns representations by pushing positive pairs, or similar examples from the same class, closer together while keeping negative pairs far apart. Despite the empirical successes, theoretical foundations are limited -- prior analyses assume conditional independence of the positive pairs given the same class label, but recent empirical applications use heavily correlated positive pairs (i.e., data augmentations of the same image). Our work analyzes contrastive learning without assuming conditional independence of positive pairs using a novel concept of the augmentation graph on data. Edges in this graph connect augmentations of the same data, and ground-truth classes naturally form connected sub-graphs. We propose a loss that performs spectral decomposition on the population augmentation graph and can be succinctly written as a contrastive learning objective on neural net representations. Minimizing this objective leads to features with provable accuracy guarantees under linear probe evaluation. By standard generalization bounds, these accuracy guarantees also hold when minimizing the training contrastive loss. Empirically, the features learned by our objective can match or outperform several strong baselines on benchmark vision datasets. In all, this work provides the first provable analysis for contrastive learning where guarantees for linear probe evaluation can apply to realistic empirical settings.

</details>

### Self-Supervised GANs with Label Augmentation.
- **链接**: [arXiv:2106.08601](https://arxiv.org/abs/2106.08601)
- **作者**: Liang Hou, Huawei Shen, Qi Cao, Xueqi Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, transformation-based self-supervised learning has been applied to generative adversarial networks (GANs) to mitigate catastrophic forgetting in the discriminator by introducing a stationary learning environment. However, the separate self-supervised tasks in existing self-supervised GANs cause a goal inconsistent with generative modeling due to the fact that their self-supervised classifiers are agnostic to the generator distribution. To address this problem, we propose a novel self-supervised GAN that unifies the GAN task with the self-supervised task by augmenting the GAN labels (real or fake) via self-supervision of data transformation. Specifically, the original discriminator and self-supervised classifier are unified into a label-augmented discriminator that predicts the augmented labels to be aware of both the generator distribution and the data distribution under every transformation, and then provide the discrepancy between them to optimize the generator. Theoretically, we prove that the optimal generator could converge to replicate the real data distribution. Empirically, we show that the proposed method significantly outperforms previous self-supervised and data augmentation GANs on both generative modeling and representation learning across benchmark datasets.

</details>

### Capturing implicit hierarchical structure in 3D biomedical images with self-supervised hyperbolic representations.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/291d43c696d8c3704cdbe0a72ade5f6c-Abstract.html)
- **作者**: Joy Hsu, Jeffrey Gu, Gong Her Wu, Wah Chiu, Serena Yeung
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Local plasticity rules can learn deep representations using self-supervised contrastive predictions.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/feade1d2047977cd0cefdafc40175a99-Abstract.html)
- **作者**: Bernd Illing, Jean Ventura, Guillaume Bellec, Wulfram Gerstner
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Noise2Score: Tweedie's Approach to Self-Supervised Image Denoising without Clean Images.
- **链接**: [arXiv:2106.07009](https://arxiv.org/abs/2106.07009)
- **作者**: Kwanyoung Kim, Jong Chul Ye
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, there has been extensive research interest in training deep networks to denoise images without clean reference. However, the representative approaches such as Noise2Noise, Noise2Void, Stein's unbiased risk estimator (SURE), etc. seem to differ from one another and it is difficult to find the coherent mathematical structure. To address this, here we present a novel approach, called Noise2Score, which reveals a missing link in order to unite these seemingly different approaches. Specifically, we show that image denoising problems without clean images can be addressed by finding the mode of the posterior distribution and that the Tweedie's formula offers an explicit solution through the score function (i.e. the gradient of log likelihood). Our method then uses the recent finding that the score function can be stably estimated from the noisy images using the amortized residual denoising autoencoder, the method of which is closely related to Noise2Noise or Nose2Void. Our Noise2Score approach is so universal that the same network training can be used to remove noises from images that are corrupted by any exponential family distributions and noise parameters. Using extensive experiments with Gaussian, Poisson, and Gamma noises, we show that Noise2Score significantly outperforms the state-of-the-art self-supervised denoising methods in the benchmark data set such as (C)BSD68, Set12, and Kodak, etc.

</details>

### Self-Supervised Learning with Data Augmentations Provably Isolates Content from Style.
- **链接**: [arXiv:2106.04619](https://arxiv.org/abs/2106.04619)
- **作者**: Julius von Kügelgen, Yash Sharma, Luigi Gresele, Wieland Brendel, Bernhard Schölkopf, Michel Besserve et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised representation learning has shown remarkable success in a number of domains. A common practice is to perform data augmentation via hand-crafted transformations intended to leave the semantics of the data invariant. We seek to understand the empirical success of this approach from a theoretical perspective. We formulate the augmentation process as a latent variable model by postulating a partition of the latent representation into a content component, which is assumed invariant to augmentation, and a style component, which is allowed to change. Unlike prior work on disentanglement and independent component analysis, we allow for both nontrivial statistical and causal dependencies in the latent space. We study the identifiability of the latent representation based on pairs of views of the observations and prove sufficient conditions that allow us to identify the invariant content partition up to an invertible mapping in both generative and discriminative settings. We find numerical simulations with dependent latent variables are consistent with our theory. Lastly, we introduce Causal3DIdent, a dataset of high-dimensional, visually complex images with rich causal dependencies, which we use to study the effect of data augmentations performed in practice.

</details>

### Predicting What You Already Know Helps: Provable Self-Supervised Learning.
- **链接**: [arXiv:2008.01064](https://arxiv.org/abs/2008.01064)
- **作者**: Jason D. Lee, Qi Lei, Nikunj Saunshi, Jiacheng Zhuo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised representation learning solves auxiliary prediction tasks (known as pretext tasks) without requiring labeled data to learn useful semantic representations. These pretext tasks are created solely using the input features, such as predicting a missing image patch, recovering the color channels of an image from context, or predicting missing words in text; yet predicting this \textit{known} information helps in learning representations effective for downstream prediction tasks. We posit a mechanism exploiting the statistical connections between certain {\em reconstruction-based} pretext tasks that guarantee to learn a good representation. Formally, we quantify how the approximate independence between the components of the pretext task (conditional on the label and latent variables) allows us to learn representations that can solve the downstream task by just training a linear layer on top of the learned representation. We prove the linear layer yields small approximation error even for complex ground truth function class and will drastically reduce labeled sample complexity. Next, we show a simple modification of our method leads to nonlinear CCA, analogous to the popular SimSiam algorithm, and show similar guarantees for nonlinear CCA.

</details>

### MST: Masked Self-Supervised Transformer for Visual Representation.
- **链接**: [arXiv:2106.05656](https://arxiv.org/abs/2106.05656)
- **作者**: Zhaowen Li, Zhiyang Chen, Fan Yang, Wei Li, Yousong Zhu, Chaoyang Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer has been widely used for self-supervised pre-training in Natural Language Processing (NLP) and achieved great success. However, it has not been fully explored in visual self-supervised learning. Meanwhile, previous methods only consider the high-level feature and learning representation from a global perspective, which may fail to transfer to the downstream dense prediction tasks focusing on local features. In this paper, we present a novel Masked Self-supervised Transformer approach named MST, which can explicitly capture the local context of an image while preserving the global semantic information. Specifically, inspired by the Masked Language Modeling (MLM) in NLP, we propose a masked token strategy based on the multi-head self-attention map, which dynamically masks some tokens of local patches without damaging the crucial structure for self-supervised learning. More importantly, the masked tokens together with the remaining tokens are further recovered by a global image decoder, which preserves the spatial information of the image and is more friendly to the downstream dense prediction tasks. The experiments on multiple datasets demonstrate the effectiveness and generality of the proposed method. For instance, MST achieves Top-1 accuracy of 76.9% with DeiT-S only using 300-epoch pre-training by linear evaluation, which outperforms supervised methods with the same epoch by 0.4% and its comparable variant DINO by 1.0\%. For dense prediction tasks, MST also achieves 42.7% mAP on MS COCO object detection and 74.04% mIoU on Cityscapes segmentation only with 100-epoch pre-training.

</details>

### Self-Supervised Learning with Kernel Dependence Maximization.
- **链接**: [arXiv:2106.08320](https://arxiv.org/abs/2106.08320) · [代码](https://github.com/deepmind/ssl_hsic)
- **作者**: Yazhe Li, Roman Pogodin, Danica J. Sutherland, Arthur Gretton
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We approach self-supervised learning of image representations from a statistical dependence perspective, proposing Self-Supervised Learning with the Hilbert-Schmidt Independence Criterion (SSL-HSIC). SSL-HSIC maximizes dependence between representations of transformations of an image and the image identity, while minimizing the kernelized variance of those representations. This framework yields a new understanding of InfoNCE, a variational lower bound on the mutual information (MI) between different transformations. While the MI itself is known to have pathologies which can result in learning meaningless representations, its bound is much better behaved: we show that it implicitly approximates SSL-HSIC (with a slightly different regularizer). Our approach also gives us insight into BYOL, a negative-free SSL method, since SSL-HSIC similarly learns local neighborhoods of samples. SSL-HSIC allows us to directly optimize statistical dependence in time linear in the batch size, without restrictive data assumptions or indirect mutual information estimators. Trained with or without a target network, SSL-HSIC matches the current state-of-the-art for standard linear evaluation on ImageNet, semi-supervised learning and transfer to other classification and vision tasks such as semantic segmentation, depth estimation and object recognition. Code is available at https://github.com/deepmind/ssl_hsic .

</details>

### Credal Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/7866c91c59f8bffc92a79a7cd09f9af9-Abstract.html)
- **作者**: Julian Lienen, Eyke Hüllermeier
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Drop, Swap, and Generate: A Self-Supervised Approach for Generating Neural Activity.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/58182b82110146887c02dbd78719e3d5-Abstract.html) · 📚 被引 8
- **作者**: Ran Liu, Mehdi Azabou, Max Dabagia, Chi-Heng Lin, Mohammad Gheshlaghi Azar, Keith B. Hengen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### TTT++: When Does Self-Supervised Test-Time Training Fail or Thrive?
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b618c3210e934362ac261db280128c22-Abstract.html)
- **作者**: Yuejiang Liu, Parth Kothari, Bastien van Delft, Baptiste Bellot-Gurlet, Taylor Mordan, Alexandre Alahi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Understanding Negative Samples in Instance Discriminative Self-supervised Representation Learning.
- **链接**: [arXiv:2102.06866](https://arxiv.org/abs/2102.06866)
- **作者**: Kento Nozawa, Issei Sato
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Instance discriminative self-supervised representation learning has been attracted attention thanks to its unsupervised nature and informative feature representation for downstream tasks. In practice, it commonly uses a larger number of negative samples than the number of supervised classes. However, there is an inconsistency in the existing analysis; theoretically, a large number of negative samples degrade classification performance on a downstream supervised task, while empirically, they improve the performance. We provide a novel framework to analyze this empirical result regarding negative samples using the coupon collector's problem. Our bound can implicitly incorporate the supervised loss of the downstream task in the self-supervised loss by increasing the number of negative samples. We confirm that our proposed analysis holds on real-world benchmark datasets.

</details>

### Self-Paced Contrastive Learning for Semi-supervised Medical Image Segmentation with Meta-labels.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/8b5c8441a8ff8e151b191c53c1842a38-Abstract.html)
- **作者**: Jizong Peng, Ping Wang, Christian Desrosiers, Marco Pedersoli
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Self-Supervised Representation Learning on Neural Network Weights for Model Characteristic Prediction.
- **链接**: [arXiv:2110.15288](https://arxiv.org/abs/2110.15288)
- **作者**: Konstantin Schürholt, Dimche Kostadinov, Damian Borth
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has been shown to learn useful and information-preserving representations. Neural Networks (NNs) are widely applied, yet their weight space is still not fully understood. Therefore, we propose to use SSL to learn hyper-representations of the weights of populations of NNs. To that end, we introduce domain specific data augmentations and an adapted attention architecture. Our empirical evaluation demonstrates that self-supervised representation learning in this domain is able to recover diverse NN model characteristics. Further, we show that the proposed learned representations outperform prior work for predicting hyper-parameters, test accuracy, and generalization gap as well as transfer to out-of-distribution settings.

</details>

### MarioNette: Self-Supervised Sprite Learning.
- **链接**: [arXiv:2104.14553](https://arxiv.org/abs/2104.14553)
- **作者**: Dmitriy Smirnov, Michaël Gharbi, Matthew Fisher, Vitor Guizilini, Alexei A. Efros, Justin M. Solomon
- **🏷️ 机构**: UC Berkeley
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Artists and video game designers often construct 2D animations using libraries of sprites -- textured patches of objects and characters. We propose a deep learning approach that decomposes sprite-based video animations into a disentangled representation of recurring graphic elements in a self-supervised manner. By jointly learning a dictionary of possibly transparent patches and training a network that places them onto a canvas, we deconstruct sprite-based content into a sparse, consistent, and explicit representation that can be easily used in downstream tasks, like editing or analysis. Our framework offers a promising approach for discovering recurring visual patterns in image collections without supervision.

</details>

### Canonical Capsules: Self-Supervised Capsules in Canonical Pose.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/d1ee59e20ad01cedc15f5118a7626099-Abstract.html)
- **作者**: Weiwei Sun, Andrea Tagliasacchi, Boyang Deng, Sara Sabour, Soroosh Yazdani, Geoffrey E. Hinton et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Look at What I'm Doing: Self-Supervised Spatial Grounding of Narrations in Instructional Videos.
- **链接**: [arXiv:2110.10596](https://arxiv.org/abs/2110.10596)
- **作者**: Reuben Tan, Bryan A. Plummer, Kate Saenko, Hailin Jin, Bryan C. Russell
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the task of spatially localizing narrated interactions in videos. Key to our approach is the ability to learn to spatially localize interactions with self-supervision on a large corpus of videos with accompanying transcribed narrations. To achieve this goal, we propose a multilayer cross-modal attention network that enables effective optimization of a contrastive loss during training. We introduce a divided strategy that alternates between computing inter- and intra-modal attention across the visual and natural language modalities, which allows effective training via directly contrasting the two modalities' representations. We demonstrate the effectiveness of our approach by self-training on the HowTo100M instructional video dataset and evaluating on a newly collected dataset of localized described interactions in the YouCook2 dataset. We show that our approach outperforms alternative baselines, including shallow co-attention and full cross-modal attention. We also apply our approach to grounding phrases in images with weak supervision on Flickr30K and show that stacking multiple attention layers is effective and, when combined with a word-to-region loss, achieves state of the art on recall-at-one and pointing hand accuracies.

</details>

### SubTab: Subsetting Features of Tabular Data for Self-Supervised Representation Learning.
- **链接**: [arXiv:2110.04361](https://arxiv.org/abs/2110.04361)
- **作者**: Talip Ucar, Ehsan Hajiramezanali, Lindsay Edwards
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has been shown to be very effective in learning useful representations, and yet much of the success is achieved in data types such as images, audio, and text. The success is mainly enabled by taking advantage of spatial, temporal, or semantic structure in the data through augmentation. However, such structure may not exist in tabular datasets commonly used in fields such as healthcare, making it difficult to design an effective augmentation method, and hindering a similar progress in tabular data setting. In this paper, we introduce a new framework, Subsetting features of Tabular data (SubTab), that turns the task of learning from tabular data into a multi-view representation learning problem by dividing the input features to multiple subsets. We argue that reconstructing the data from the subset of its features rather than its corrupted version in an autoencoder setting can better capture its underlying latent representation. In this framework, the joint representation can be expressed as the aggregate of latent variables of the subsets at test time, which we refer to as collaborative inference. Our experiments show that the SubTab achieves the state of the art (SOTA) performance of 98.31% on MNIST in tabular setting, on par with CNN-based SOTA models, and surpasses existing baselines on three other real-world datasets by a significant margin.

</details>

### Improving Self-supervised Learning with Automated Unsupervised Outlier Arbitration.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/e8855b3528cb03d1def9803220bd3cb9-Abstract.html)
- **作者**: Yu Wang, Jingyang Lin, Jingjing Zou, Yingwei Pan, Ting Yao, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Self-Supervised Learning Disentangled Group Representation as Feature.
- **链接**: [arXiv:2110.15255](https://arxiv.org/abs/2110.15255) · [代码](https://github.com/Wangt-CN/IP-IRM)
- **作者**: Tan Wang, Zhongqi Yue, Jianqiang Huang, Qianru Sun, Hanwang Zhang
- **🏷️ 机构**: NUS
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A good visual representation is an inference map from observations (images) to features (vectors) that faithfully reflects the hidden modularized generative factors (semantics). In this paper, we formulate the notion of "good" representation from a group-theoretic view using Higgins' definition of disentangled representation, and show that existing Self-Supervised Learning (SSL) only disentangles simple augmentation features such as rotation and colorization, thus unable to modularize the remaining semantics. To break the limitation, we propose an iterative SSL algorithm: Iterative Partition-based Invariant Risk Minimization (IP-IRM), which successfully grounds the abstract semantics and the group acting on them into concrete contrastive learning. At each iteration, IP-IRM first partitions the training samples into two subsets that correspond to an entangled group element. Then, it minimizes a subset-invariant contrastive loss, where the invariance guarantees to disentangle the group element. We prove that IP-IRM converges to a fully disentangled representation and show its effectiveness on various benchmarks. Codes are available at https://github.com/Wangt-CN/IP-IRM.

</details>

### Graph Adversarial Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/7d3010c11d08cf990b7614d2c2ca9098-Abstract.html)
- **作者**: Longqi Yang, Liangliang Zhang, Wenjing Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Unleashing the Power of Contrastive Self-Supervised Visual Models via Contrast-Regularized Fine-Tuning.
- **链接**: [arXiv:2102.06605](https://arxiv.org/abs/2102.06605)
- **作者**: Yifan Zhang, Bryan Hooi, Dapeng Hu, Jian Liang, Jiashi Feng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning (CSL) has attracted increasing attention for model pre-training via unlabeled data. The resulted CSL models provide instance-discriminative visual features that are uniformly scattered in the feature space. During deployment, the common practice is to directly fine-tune CSL models with cross-entropy, which however may not be the best strategy in practice. Although cross-entropy tends to separate inter-class features, the resulting models still have limited capability for reducing intra-class feature scattering that exists in CSL models. In this paper, we investigate whether applying contrastive learning to fine-tuning would bring further benefits, and analytically find that optimizing the contrastive loss benefits both discriminative representation learning and model optimization during fine-tuning. Inspired by these findings, we propose Contrast-regularized tuning (Core-tuning), a new approach for fine-tuning CSL models. Instead of simply adding the contrastive loss to the objective of fine-tuning, Core-tuning further applies a novel hard pair mining strategy for more effective contrastive fine-tuning, as well as smoothing the decision boundary to better exploit the learned discriminative feature space. Extensive experiments on image classification and semantic segmentation verify the effectiveness of Core-tuning.

</details>

### Motif-based Graph Self-Supervised Learning for Molecular Property Prediction.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/85267d349a5e647ff0a9edcb5ffd1e02-Abstract.html)
- **作者**: Zaixi Zhang, Qi Liu, Hao Wang, Chengqiang Lu, Chee-Kong Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### From Canonical Correlation Analysis to Self-supervised Graph Neural Networks.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/00ac8ed3b4327bdd4ebbebcb2ba10a00-Abstract.html)
- **作者**: Hengrui Zhang, Qitian Wu, Junchi Yan, David Wipf, Philip S. Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### ReSSL: Relational Self-Supervised Learning with Weak Augmentation.
- **链接**: [arXiv:2107.09282](https://arxiv.org/abs/2107.09282) · [代码](https://github.com/KyleZheng1997/ReSSL)
- **作者**: Mingkai Zheng, Shan You, Fei Wang, Chen Qian, Changshui Zhang, Xiaogang Wang et al.
- **🏷️ 机构**: CUHK / Shanghai AI Lab
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised Learning (SSL) including the mainstream contrastive learning has achieved great success in learning visual representations without data annotations. However, most of methods mainly focus on the instance level information (\ie, the different augmented images of the same instance should have the same feature or cluster into the same class), but there is a lack of attention on the relationships between different instances. In this paper, we introduced a novel SSL paradigm, which we term as relational self-supervised learning (ReSSL) framework that learns representations by modeling the relationship between different instances. Specifically, our proposed method employs sharpened distribution of pairwise similarities among different instances as \textit{relation} metric, which is thus utilized to match the feature embeddings of different augmentations. Moreover, to boost the performance, we argue that weak augmentations matter to represent a more reliable relation, and leverage momentum strategy for practical efficiency. Experimental results show that our proposed ReSSL significantly outperforms the previous state-of-the-art algorithms in terms of both performance and training efficiency. Code is available at \url{https://github.com/KyleZheng1997/ReSSL}.

</details>

### Artistic Style Transfer with Internal-external Learning and Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/df5354693177e83e8ba089e94b7b6b55-Abstract.html)
- **作者**: Haibo Chen, Lei Zhao, Zhizhong Wang, Huiming Zhang, Zhiwen Zuo, Ailin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### A Contrastive Learning Approach for Training Variational Autoencoder Priors.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/0496604c1d80f66fbeb963c12e570a26-Abstract.html)
- **作者**: Jyoti Aneja, Alexander G. Schwing, Jan Kautz, Arash Vahdat
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### When does Contrastive Learning Preserve Adversarial Robustness from Pretraining to Finetuning?
- **链接**: [arXiv:2111.01124](https://arxiv.org/abs/2111.01124)
- **作者**: Lijie Fan, Sijia Liu, Pin-Yu Chen, Gaoyuan Zhang, Chuang Gan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning (CL) can learn generalizable feature representations and achieve the state-of-the-art performance of downstream tasks by finetuning a linear classifier on top of it. However, as adversarial robustness becomes vital in image classification, it remains unclear whether or not CL is able to preserve robustness to downstream tasks. The main challenge is that in the self-supervised pretraining + supervised finetuning paradigm, adversarial robustness is easily forgotten due to a learning task mismatch from pretraining to finetuning. We call such a challenge 'cross-task robustness transferability'. To address the above problem, in this paper we revisit and advance CL principles through the lens of robustness enhancement. We show that (1) the design of contrastive views matters: High-frequency components of images are beneficial to improving model robustness; (2) Augmenting CL with pseudo-supervision stimulus (e.g., resorting to feature clustering) helps preserve robustness without forgetting. Equipped with our new designs, we propose AdvCL, a novel adversarial contrastive pretraining framework. We show that AdvCL is able to enhance cross-task robustness transferability without loss of model accuracy and finetuning efficiency. With a thorough experimental study, we demonstrate that AdvCL outperforms the state-of-the-art self-supervised robust learning methods across multiple datasets (CIFAR-10, CIFAR-100, and STL-10) and finetuning schemes (linear evaluation and full model finetuning).

</details>

### Robust Contrastive Learning Using Negative Samples with Diminished Semantics.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/e5afb0f2dbc6d39b312d7406054cb4c6-Abstract.html)
- **作者**: Songwei Ge, Shlok Mishra, Chun-Liang Li, Haohan Wang, David Jacobs
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Model Adaptation: Historical Contrastive Learning for Unsupervised Domain Adaptation without Source Data.
- **链接**: [arXiv:2110.03374](https://arxiv.org/abs/2110.03374)
- **作者**: Jiaxing Huang, Dayan Guan, Aoran Xiao, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised domain adaptation aims to align a labeled source domain and an unlabeled target domain, but it requires to access the source data which often raises concerns in data privacy, data portability and data transmission efficiency. We study unsupervised model adaptation (UMA), or called Unsupervised Domain Adaptation without Source Data, an alternative setting that aims to adapt source-trained models towards target distributions without accessing source data. To this end, we design an innovative historical contrastive learning (HCL) technique that exploits historical source hypothesis to make up for the absence of source data in UMA. HCL addresses the UMA challenge from two perspectives. First, it introduces historical contrastive instance discrimination (HCID) that learns from target samples by contrasting their embeddings which are generated by the currently adapted model and the historical models. With the historical models, HCID encourages UMA to learn instance-discriminative target representations while preserving the source hypothesis. Second, it introduces historical contrastive category discrimination (HCCD) that pseudo-labels target samples to learn category-discriminative target representations. Specifically, HCCD re-weights pseudo labels according to their prediction consistency across the current and historical models. Extensive experiments show that HCL outperforms and state-of-the-art methods consistently across a variety of visual tasks and setups.

</details>

### Compressed Video Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/7647966b7343c29048673252e490f736-Abstract.html)
- **作者**: Yuqi Huo, Mingyu Ding, Haoyu Lu, Nanyi Fei, Zhiwu Lu, Ji-Rong Wen et al.
- **🏷️ 机构**: Renmin University
- **会议**: NeurIPS 2021

### Task-Adaptive Neural Network Search with Meta-Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b20bb95ab626d93fd976af958fbc61ba-Abstract.html)
- **作者**: Wonyong Jeong, Hayeon Lee, Geon Park, Eunyoung Hyung, Jinheon Baek, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Improving Contrastive Learning on Imbalanced Data via Open-World Sampling.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/2f37d10131f2a483a8dd005b3d14b0d9-Abstract.html)
- **作者**: Ziyu Jiang, Tianlong Chen, Ting Chen, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Disentangled Contrastive Learning on Graphs.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b6cda17abb967ed28ec9610137aa45f7-Abstract.html)
- **作者**: Haoyang Li, Xin Wang, Ziwei Zhang, Zehuan Yuan, Hang Li, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Contrastive Learning of Global and Local Video Representations.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/38ef4b66cb25e92abe4d594acb841471-Abstract.html)
- **作者**: Shuang Ma, Zhaoyang Zeng, Daniel McDuff, Yale Song
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Object-aware Contrastive Learning for Debiased Scene Representation.
- **链接**: [arXiv:2108.00049](https://arxiv.org/abs/2108.00049)
- **作者**: Sangwoo Mo, Hyunwoo Kang, Kihyuk Sohn, Chun-Liang Li, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning has shown impressive results in learning visual representations from unlabeled images by enforcing invariance against different data augmentations. However, the learned representations are often contextually biased to the spurious scene correlations of different objects or object and background, which may harm their generalization on the downstream tasks. To tackle the issue, we develop a novel object-aware contrastive learning framework that first (a) localizes objects in a self-supervised manner and then (b) debias scene correlations via appropriate data augmentations considering the inferred object locations. For (a), we propose the contrastive class activation map (ContraCAM), which finds the most discriminative regions (e.g., objects) in the image compared to the other images using the contrastively trained models. We further improve the ContraCAM to detect multiple objects and entire shapes via an iterative refinement procedure. For (b), we introduce two data augmentations based on ContraCAM, object-aware random crop and background mixup, which reduce contextual and background biases during contrastive self-supervised learning, respectively. Our experiments demonstrate the effectiveness of our representation learning framework, particularly when trained under multi-object images or evaluated under the background (and distribution) shifted images.

</details>

### Contrastive Learning for Neural Topic Model.
- **链接**: [arXiv:2110.12764](https://arxiv.org/abs/2110.12764)
- **作者**: Thong Nguyen, Anh Tuan Luu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent empirical studies show that adversarial topic models (ATM) can successfully capture semantic patterns of the document by differentiating a document with another dissimilar sample. However, utilizing that discriminative-generative architecture has two important drawbacks: (1) the architecture does not relate similar documents, which has the same document-word distribution of salient words; (2) it restricts the ability to integrate external information, such as sentiments of the document, which has been shown to benefit the training of neural topic model. To address those issues, we revisit the adversarial topic architecture in the viewpoint of mathematical analysis, propose a novel approach to re-formulate discriminative goal as an optimization problem, and design a novel sampling method which facilitates the integration of external variables. The reformulation encourages the model to incorporate the relations among similar samples and enforces the constraint on the similarity among dissimilar ones; while the sampling method, which is based on the internal input and reconstructed output, helps inform the model of salient words contributing to the main topic. Experimental results show that our framework outperforms other state-of-the-art neural topic models in three common benchmark datasets that belong to various domains, vocabulary sizes, and document lengths in terms of topic coherence.

</details>

### Can contrastive learning avoid shortcut solutions?
- **链接**: [arXiv:2106.11230](https://arxiv.org/abs/2106.11230) · [代码](https://github.com/joshr17/IFM)
- **作者**: Joshua Robinson, Li Sun, Ke Yu, Kayhan Batmanghelich, Stefanie Jegelka, Suvrit Sra
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The generalization of representations learned via contrastive learning depends crucially on what features of the data are extracted. However, we observe that the contrastive loss does not always sufficiently guide which features are extracted, a behavior that can negatively impact the performance on downstream tasks via "shortcuts", i.e., by inadvertently suppressing important predictive features. We find that feature extraction is influenced by the difficulty of the so-called instance discrimination task (i.e., the task of discriminating pairs of similar points from pairs of dissimilar ones). Although harder pairs improve the representation of some features, the improvement comes at the cost of suppressing previously well represented features. In response, we propose implicit feature modification (IFM), a method for altering positive and negative samples in order to guide contrastive models towards capturing a wider variety of predictive features. Empirically, we observe that IFM reduces feature suppression, and as a result improves performance on vision and medical imaging tasks. The code is available at: \url{https://github.com/joshr17/IFM}.

</details>

### CLDA: Contrastive Learning for Semi-Supervised Domain Adaptation.
- **链接**: [arXiv:2107.00085](https://arxiv.org/abs/2107.00085)
- **作者**: Ankit Singh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Domain Adaptation (UDA) aims to align the labeled source distribution with the unlabeled target distribution to obtain domain invariant predictive models. However, the application of well-known UDA approaches does not generalize well in Semi-Supervised Domain Adaptation (SSDA) scenarios where few labeled samples from the target domain are available. In this paper, we propose a simple Contrastive Learning framework for semi-supervised Domain Adaptation (CLDA) that attempts to bridge the intra-domain gap between the labeled and unlabeled target distributions and inter-domain gap between source and unlabeled target distribution in SSDA. We suggest employing class-wise contrastive learning to reduce the inter-domain gap and instance-level contrastive alignment between the original (input image) and strongly augmented unlabeled target images to minimize the intra-domain discrepancy. We have shown empirically that both of these modules complement each other to achieve superior performance. Experiments on three well-known domain adaptation benchmark datasets namely DomainNet, Office-Home, and Office31 demonstrate the effectiveness of our approach. CLDA achieves state-of-the-art results on all the above datasets.

</details>

### Adversarial Graph Augmentation to Improve Graph Contrastive Learning.
- **链接**: [arXiv:2106.05819](https://arxiv.org/abs/2106.05819)
- **作者**: Susheel Suresh, Pan Li, Cong Hao, Jennifer Neville
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning of graph neural networks (GNN) is in great need because of the widespread label scarcity issue in real-world graph/network data. Graph contrastive learning (GCL), by training GNNs to maximize the correspondence between the representations of the same graph in its different augmented forms, may yield robust and transferable GNNs even without using labels. However, GNNs trained by traditional GCL often risk capturing redundant graph features and thus may be brittle and provide sub-par performance in downstream tasks. Here, we propose a novel principle, termed adversarial-GCL (AD-GCL), which enables GNNs to avoid capturing redundant information during the training by optimizing adversarial graph augmentation strategies used in GCL. We pair AD-GCL with theoretical explanations and design a practical instantiation based on trainable edge-dropping graph augmentation. We experimentally validate AD-GCL by comparing with the state-of-the-art GCL methods and achieve performance gains of up-to $14\%$ in unsupervised, $6\%$ in transfer, and $3\%$ in semi-supervised learning settings overall with 18 different benchmark datasets for the tasks of molecule property regression and classification, and social network classification.

</details>

### Directed Graph Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/a3048e47310d6efaa4b1eaf55227bc92-Abstract.html)
- **作者**: Zekun Tong, Yuxuan Liang, Henghui Ding, Yongxing Dai, Xinke Li, Changhu Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### InfoGCL: Information-Aware Graph Contrastive Learning.
- **链接**: [arXiv:2110.15438](https://arxiv.org/abs/2110.15438)
- **作者**: Dongkuan Xu, Wei Cheng, Dongsheng Luo, Haifeng Chen, Xiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Various graph contrastive learning models have been proposed to improve the performance of learning tasks on graph datasets in recent years. While effective and prevalent, these models are usually carefully customized. In particular, although all recent researches create two contrastive views, they differ greatly in view augmentations, architectures, and objectives. It remains an open question how to build your graph contrastive learning model from scratch for particular graph learning tasks and datasets. In this work, we aim to fill this gap by studying how graph information is transformed and transferred during the contrastive learning process and proposing an information-aware graph contrastive learning framework called InfoGCL. The key point of this framework is to follow the Information Bottleneck principle to reduce the mutual information between contrastive parts while keeping task-relevant information intact at both the levels of the individual module and the entire framework so that the information loss during graph representation learning can be minimized. We show for the first time that all recent graph contrastive learning methods can be unified by our framework. We empirically validate our theoretical analysis on both node and graph classification benchmark datasets, and demonstrate that our algorithm significantly outperforms the state-of-the-arts.

</details>

## 跨领域论文（完整笔记在其他领域）

- Explainable Semantic Space by Grounding Language to Vision with Cross-Modal Contrastive Learning. → [multimodal](../multimodal/Guideline%202021.md)
- VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text. → [multimodal](../multimodal/Guideline%202021.md)
- Real-Time and Accurate Self-Supervised Monocular Depth Estimation on Mobile Device. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- PARP: Prune, Adjust and Re-Prune for Self-Supervised Speech Recognition. → [network-pruning](../network-pruning/Guideline%202021.md)
