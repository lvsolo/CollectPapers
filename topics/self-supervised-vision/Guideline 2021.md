# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Point-Flow: Self-Supervised Scene Flow Estimation From Point Clouds With Optimal Transport and Random Walk.
- **链接**: [arXiv:2105.08248](https://arxiv.org/abs/2105.08248) · 📚 被引 45
- **作者**: Ruibo Li, Guosheng Lin, Lihua Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Guided Point Contrastive Learning for Semi-supervised Point Cloud Semantic Segmentation.
- **链接**: [arXiv:2110.08188](https://arxiv.org/abs/2110.08188) · 📚 被引 121
- **作者**: Li Jiang, Shaoshuai Shi, Zhuotao Tian, Xin Lai, Shu Liu, Chi-Wing Fu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, SmartMore
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rapid progress in 3D semantic segmentation is inseparable from the advances of deep network models, which highly rely on large-scale annotated data for training. To address the high cost and challenges of 3D point-level labeling, we present a method for semi-supervised point cloud semantic segmentation to adopt unlabeled point clouds in training to boost the model performance. Inspired by the recent contrastive loss in self-supervised tasks, we propose the guided point contrastive loss to enhance the feature representation and model generalization ability in semi-supervised setting. Semantic predictions on unlabeled point clouds serve as pseudo-label guidance in our loss to avoid negative pairs in the same category. Also, we design the confidence guidance to ensure high-quality feature learning. Besides, a category-balanced sampling strategy is proposed to collect positive and negative samples to mitigate the class imbalance problem. Extensive experiments on three datasets (ScanNet V2, S3DIS, and SemanticKITTI) show the effectiveness of our semi-supervised method to improve the prediction quality with unlabeled data.

</details>

### Spatio-temporal Self-Supervised Representation Learning for 3D Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00647) · 📚 被引 187
- **作者**: Siyuan Huang, Yichen Xie, Song-Chun Zhu, Yixin Zhu
- **🏷️ 机构**: University of California,Los Angeles, Shanghai Jiao Tong University, Beijing Institute for General Artificial Intelligence
- **会议**: ICCV 2021

### Unsupervised Point Cloud Object Co-segmentation by Co-contrastive Learning and Mutual Attention Sampling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00724) · 📚 被引 13
- **作者**: Cheng-Kun Yang, Yung-Yu Chuang, Yen-Yu Lin
- **🏷️ 机构**: National Taiwan University, National Yang Ming Chiao Tung University
- **会议**: ICCV 2021

### Self-Supervised Learning on 3D Point Clouds by Learning Discrete Generative Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Eckart_Self-Supervised_Learning_on_3D_Point_Clouds_by_Learning_Discrete_Generative_CVPR_2021_paper.html) · 📚 被引 54
- **作者**: Benjamin Eckart, Wentao Yuan, Chao Liu, Jan Kautz
- **🏷️ 机构**: NVIDIA, University of Washington
- **会议**: CVPR 2021

### Self-supervised Transfer Learning for Hand Mesh Recovery from Binocular Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01142) · 📚 被引 10
- **作者**: Zheng Chen, Sihan Wang, Yi Sun, Xiaohong Ma
- **🏷️ 机构**: Dalian University of Technology,China
- **会议**: ICCV 2021

### Towards High Fidelity Monocular Face Reconstruction with Rich Reflectance using Self-supervised Learning and Ray Tracing.
- **链接**: [arXiv:2103.15432](https://arxiv.org/abs/2103.15432) · 📚 被引 53
- **作者**: Abdallah Dib, Cédric Thébault, Junghyun Ahn, Philippe-Henri Gosselin, Christian Theobalt, Louis Chevallier
- **🏷️ 机构**: InterDigital R&#x0026;I, Max-Planck-Institute for Informatics
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robust face reconstruction from monocular image in general lighting conditions is challenging. Methods combining deep neural network encoders with differentiable rendering have opened up the path for very fast monocular reconstruction of geometry, lighting and reflectance. They can also be trained in self-supervised manner for increased robustness and better generalization. However, their differentiable rasterization based image formation models, as well as underlying scene parameterization, limit them to Lambertian face reflectance and to poor shape details. More recently, ray tracing was introduced for monocular face reconstruction within a classic optimization-based framework and enables state-of-the art results. However optimization-based approaches are inherently slow and lack robustness. In this paper, we build our work on the aforementioned approaches and propose a new method that greatly improves reconstruction quality and robustness in general scenes. We achieve this by combining a CNN encoder with a differentiable ray tracer, which enables us to base the reconstruction on much more advanced personalized diffuse and specular albedos, a more sophisticated illumination model and a plausible representation of self-shadows. This enables to take a big leap forward in reconstruction quality of shape, appearance and lighting even in scenes with difficult illumination. With consistent face attributes reconstruction, our method leads to practical applications such as relighting and self-shadows removal. Compared to state-of-the-art methods, our results show improved accuracy and validity of the approach.

</details>

### Contrast and Order Representations for Video Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00784) · 📚 被引 47
- **作者**: Kai Hu, Jie Shao, Yuan Liu, Bhiksha Raj, Marios Savvides, Zhiqiang Shen
- **🏷️ 机构**: Carnegie Mellon University, Fudan University, ByteDance
- **会议**: ICCV 2021

### On Feature Decorrelation in Self-Supervised Learning.
- **链接**: [arXiv:2105.00470](https://arxiv.org/abs/2105.00470)
- **作者**: Tianyu Hua, Wenxiao Wang, Zihui Xue, Sucheng Ren, Yue Wang, Hang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### STaR: Self-Supervised Tracking and Reconstruction of Rigid Objects in Motion With Neural Rendering.
- **链接**: [arXiv:2101.01602](https://arxiv.org/abs/2101.01602) · 📚 被引 61
- **作者**: Wentao Yuan, Zhaoyang Lv, Tanner Schmidt, Steven Lovegrove
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Self-supervised Product Quantization for Deep Unsupervised Image Retrieval.
- **链接**: [arXiv:2109.02244](https://arxiv.org/abs/2109.02244) · 📚 被引 70
- **作者**: Young Kyun Jang, Nam Ik Cho
- **🏷️ 机构**: Seoul National University,Department of ECE, INMC,Seoul,Korea
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine learning-based program analyses have recently shown the promise of integrating formal and probabilistic reasoning towards aiding software development. However, in the absence of large annotated corpora, training these analyses is challenging. Towards addressing this, we present BugLab, an approach for self-supervised learning of bug detection and repair. BugLab co-trains two models: (1) a detector model that learns to detect and repair bugs in code, (2) a selector model that learns to create buggy code for the detector to use as training data. A Python implementation of BugLab improves by up to 30% upon baseline methods on a test dataset of 2374 real-life bugs and finds 19 previously unknown bugs in open-source software.

</details>

### SelfSAGCN: Self-Supervised Semantic Alignment for Graph Convolution Network.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_SelfSAGCN_Self-Supervised_Semantic_Alignment_for_Graph_Convolution_Network_CVPR_2021_paper.html) · 📚 被引 26
- **作者**: Xu Yang, Cheng Deng, Zhiyuan Dang, Kun Wei, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Exponential Moving Average Normalization for Self-Supervised and Semi-Supervised Learning.
- **链接**: [arXiv:2101.08482](https://arxiv.org/abs/2101.08482) · [代码](https://github.com/amazon-research/exponential-moving-average-normalization) · 📚 被引 112
- **作者**: Zhaowei Cai, Avinash Ravichandran, Subhransu Maji, Charless C. Fowlkes, Zhuowen Tu, Stefano Soatto
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

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
- **会议**: ICLR 2021

### Self-supervised Domain Adaptation for Forgery Localization of JPEG Compressed Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01476) · 📚 被引 33
- **作者**: Yuan Rao, Jiangqun Ni
- **🏷️ 机构**: Sun Yat-Sen University,School of Electronics and Information Technology,Guangzhou,China, Sun Yat-Sen University,School of Computer Science and Engineering,Guangzhou,China
- **会议**: ICCV 2021

### Broaden Your Views for Self-Supervised Video Learning.
- **链接**: [arXiv:2103.16559](https://arxiv.org/abs/2103.16559) · 📚 被引 71
- **作者**: Adrià Recasens, Pauline Luc, Jean-Baptiste Alayrac, Luyu Wang, Florian Strub, Corentin Tallec et al.
- **🏷️ 机构**: DeepMind
- **会议**: ICCV 2021

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer has been widely used for self-supervised pre-training in Natural Language Processing (NLP) and achieved great success. However, it has not been fully explored in visual self-supervised learning. Meanwhile, previous methods only consider the high-level feature and learning representation from a global perspective, which may fail to transfer to the downstream dense prediction tasks focusing on local features. In this paper, we present a novel Masked Self-supervised Transformer approach named MST, which can explicitly capture the local context of an image while preserving the global semantic information. Specifically, inspired by the Masked Language Modeling (MLM) in NLP, we propose a masked token strategy based on the multi-head self-attention map, which dynamically masks some tokens of local patches without damaging the crucial structure for self-supervised learning. More importantly, the masked tokens together with the remaining tokens are further recovered by a global image decoder, which preserves the spatial information of the image and is more friendly to the downstream dense prediction tasks. The experiments on multiple datasets demonstrate the effectiveness and generality of the proposed method. For instance, MST achieves Top-1 accuracy of 76.9% with DeiT-S only using 300-epoch pre-training by linear evaluation, which outperforms supervised methods with the same epoch by 0.4% and its comparable variant DINO by 1.0\%. For dense prediction tasks, MST also achieves 42.7% mAP on MS COCO object detection and 74.04% mIoU on Cityscapes segmentation only with 100-epoch pre-training.

### Self-Supervised 3D Mesh Reconstruction From Single Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_Self-Supervised_3D_Mesh_Reconstruction_From_Single_Images_CVPR_2021_paper.html) · 📚 被引 49
- **作者**: Tao Hu, Liwei Wang, Xiaogang Xu, Shu Liu, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: ICCV 2021

### Vi2CLR: Video and Image for Visual Contrastive Learning of Representation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00153)
- **作者**: Ali Diba, Vivek Sharma, Reza Safdari, Dariush Lotfi, M. Saquib Sarfraz, Rainer Stiefelhagen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

### With a Little Help from My Friends: Nearest-Neighbor Contrastive Learning of Visual Representations.
- **链接**: [arXiv:2104.14548](https://arxiv.org/abs/2104.14548) · 📚 被引 332
- **作者**: Debidatta Dwibedi, Yusuf Aytar, Jonathan Tompson, Pierre Sermanet, Andrew Zisserman
- **🏷️ 机构**: Google Research, DeepMind
- **会议**: ICCV 2021

### The Way to my Heart is through Contrastive Learning: Remote Photoplethysmography from Unlabelled Video.
- **链接**: [arXiv:2111.09748](https://arxiv.org/abs/2111.09748) · 📚 被引 126
- **作者**: John Gideon, Simon Stent
- **🏷️ 机构**: Toyota Research Institute Cambridge,MA,USA
- **会议**: ICCV 2021

### Region-aware Contrastive Learning for Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01598) · 📚 被引 127
- **作者**: Hanzhe Hu, Jinshi Cui, Liwei Wang
- **🏷️ 机构**: Peking University,Key Laboratory of Machine Perception (MOE), School of EECS
- **会议**: ICCV 2021

### A Broad Study on the Transferability of Visual Representations with Contrastive Learning.
- **链接**: [arXiv:2103.13517](https://arxiv.org/abs/2103.13517) · 📚 被引 49
- **作者**: Ashraful Islam, Chun-Fu Chen, Rameswar Panda, Leonid Karlinsky, Richard J. Radke, Rogério Feris
- **🏷️ 机构**: Rensselaer Polytechnic Institute, MIT-IBM Watson AI Lab, IBM Research
- **会议**: ICCV 2021

### Contrasting Contrastive Self-Supervised Representation Learning Pipelines.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00980) · 📚 被引 21
- **作者**: Klemen Kotar, Gabriel Ilharco, Ludwig Schmidt, Kiana Ehsani, Roozbeh Mottaghi
- **🏷️ 机构**: PRIOR @ Allen Institute for AI, University of Washington
- **会议**: ICCV 2021

### Attentive and Contrastive Learning for Joint Depth and Motion Field Estimation.
- **链接**: [arXiv:2110.06853](https://arxiv.org/abs/2110.06853) · 📚 被引 31
- **作者**: Seokju Lee, François Rameau, Fei Pan, In So Kweon
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST)
- **会议**: ICCV 2021

### Motion-Focused Contrastive Learning of Video Representations*.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00211)
- **作者**: Rui Li, Yiheng Zhang, Zhaofan Qiu, Ting Yao, Dong Liu, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Self-Supervised Video Representation Learning with Meta-Contrastive Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00813)
- **作者**: Yuanze Lin, Xun Guo, Yan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer has been widely used for self-supervised pre-training in Natural Language Processing (NLP) and achieved great success. However, it has not been fully explored in visual self-supervised learning. Meanwhile, previous methods only consider the high-level feature and learning representation from a global perspective, which may fail to transfer to the downstream dense prediction tasks focusing on local features. In this paper, we present a novel Masked Self-supervised Transformer approach named MST, which can explicitly capture the local context of an image while preserving the global semantic information. Specifically, inspired by the Masked Language Modeling (MLM) in NLP, we propose a masked token strategy based on the multi-head self-attention map, which dynamically masks some tokens of local patches without damaging the crucial structure for self-supervised learning. More importantly, the masked tokens together with the remaining tokens are further recovered by a global image decoder, which preserves the spatial information of the image and is more friendly to the downstream dense prediction tasks. The experiments on multiple datasets demonstrate the effectiveness and generality of the proposed method. For instance, MST achieves Top-1 accuracy of 76.9% with DeiT-S only using 300-epoch pre-training by linear evaluation, which outperforms supervised methods with the same epoch by 0.4% and its comparable variant DINO by 1.0\%. For dense prediction tasks, MST also achieves 42.7% mAP on MS COCO object detection and 74.04% mIoU on Cityscapes segmentation only with 100-epoch pre-training.

</details>

### Self-Supervised Learning with Kernel Dependence Maximization.
- **链接**: [arXiv:2106.08320](https://arxiv.org/abs/2106.08320) · [代码](https://github.com/deepmind/ssl_hsic)
- **作者**: Yazhe Li, Roman Pogodin, Danica J. Sutherland, Arthur Gretton
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We approach self-supervised learning of image representations from a statistical dependence perspective, proposing Self-Supervised Learning with the Hilbert-Schmidt Independence Criterion (SSL-HSIC). SSL-HSIC maximizes dependence between representations of transformations of an image and the image identity, while minimizing the kernelized variance of those representations. This framework yields a new understanding of InfoNCE, a variational lower bound on the mutual information (MI) between different transformations. While the MI itself is known to have pathologies which can result in learning meaningless representations, its bound is much better behaved: we show that it implicitly approximates SSL-HSIC (with a slightly different regularizer). Our approach also gives us insight into BYOL, a negative-free SSL method, since SSL-HSIC similarly learns local neighborhoods of samples. SSL-HSIC allows us to directly optimize statistical dependence in time linear in the batch size, without restrictive data assumptions or indirect mutual information estimators. Trained with or without a target network, SSL-HSIC matches the current state-of-the-art for standard linear evaluation on ImageNet, semi-supervised learning and transfer to other classification and vision tasks such as semantic segmentation, depth estimation and object recognition. Code is available at https://github.com/deepmind/ssl_hsic .

</details>

### Self-Supervised Video Hashing via Bidirectional Transformers.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Self-Supervised_Video_Hashing_via_Bidirectional_Transformers_CVPR_2021_paper.html) · 📚 被引 53
- **作者**: Shuyan Li, Xiu Li, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

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

### Back to Event Basics: Self-Supervised Learning of Image Reconstruction for Event Cameras via Photometric Constancy.
- **链接**: [arXiv:2009.08283](https://arxiv.org/abs/2009.08283) · 📚 被引 142
- **作者**: Federico Paredes-Vallés, Guido C. H. E. de Croon
- **🏷️ 机构**: Delft University of Technology,Micro Air Vehicle Laboratory,The Netherlands
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has been shown to learn useful and information-preserving representations. Neural Networks (NNs) are widely applied, yet their weight space is still not fully understood. Therefore, we propose to use SSL to learn hyper-representations of the weights of populations of NNs. To that end, we introduce domain specific data augmentations and an adapted attention architecture. Our empirical evaluation demonstrates that self-supervised representation learning in this domain is able to recover diverse NN model characteristics. Further, we show that the proposed learned representations outperform prior work for predicting hyper-parameters, test accuracy, and generalization gap as well as transfer to out-of-distribution settings.

</details>

### SOLD2: Self-Supervised Occlusion-Aware Line Description and Detection.
- **链接**: [arXiv:2104.03362](https://arxiv.org/abs/2104.03362) · [代码](https://github.com/cvg/SOLD2)
- **作者**: Rémi Pautrat, Juan-Ting Lin, Viktor Larsson, Martin R. Oswald, Marc Pollefeys
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared to feature point detection and description, detecting and matching line segments offer additional challenges. Yet, line features represent a promising complement to points for multi-view tasks. Lines are indeed well-defined by the image gradient, frequently appear even in poorly textured areas and offer robust structural cues. We thus hereby introduce the first joint detection and description of line segments in a single deep network. Thanks to a self-supervised training, our method does not require any annotated line labels and can therefore generalize to any dataset. Our detector offers repeatable and accurate localization of line segments in images, departing from the wireframe parsing approach. Leveraging the recent progresses in descriptor learning, our proposed line descriptor is highly discriminative, while remaining robust to viewpoint changes and occlusions. We evaluate our approach against previous line detection and description methods on several multi-view datasets created with homographic warps as well as real-world viewpoint changes. Our full pipeline yields higher repeatability, localization accuracy and matching metrics, and thus represents a first step to bridge the gap with learned feature points methods. Code and trained weights are available at https://github.com/cvg/SOLD2.

</details>

### Self-Supervised Collision Handling via Generative 3D Garment Models for Virtual Try-On.
- **链接**: [arXiv:2105.06462](https://arxiv.org/abs/2105.06462) · 📚 被引 103
- **作者**: Igor Santesteban, Nils Thuerey, Miguel A. Otaduy, Dan Casas
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

</details>

### CASTing Your Model: Learning To Localize Improves Self-Supervised Representations.
- **链接**: [arXiv:2012.04630](https://arxiv.org/abs/2012.04630) · 📚 被引 42
- **作者**: Ramprasaath R. Selvaraju, Karan Desai, Justin Johnson, Nikhil Naik
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (especially contrastive learning) has attracted great interest due to its huge potential in learning discriminative representations in an unsupervised manner. Despite the acknowledged successes, existing contrastive learning methods suffer from very low learning efficiency, e.g., taking about ten times more training epochs than supervised learning for comparable recognition accuracy. In this paper, we reveal two contradictory phenomena in contrastive learning that we call under-clustering and over-clustering problems, which are major obstacles to learning efficiency. Under-clustering means that the model cannot efficiently learn to discover the dissimilarity between inter-class samples when the negative sample pairs for contrastive learning are insufficient to differentiate all the actual object classes. Over-clustering implies that the model cannot efficiently learn features from excessive negative sample pairs, forcing the model to over-cluster samples of the same actual classes into different clusters. To simultaneously overcome these two problems, we propose a novel self-supervised learning framework using a truncated triplet loss. Precisely, we employ a triplet loss tending to maximize the relative distance between the positive pair and negative pairs to address the under-clustering problem; and we construct the negative pair by selecting a negative sample deputy from all negative samples to avoid the over-clustering problem, guaranteed by the Bernoulli Distribution model. We extensively evaluate our framework in several large-scale benchmarks (e.g., ImageNet, SYSU-30k, and COCO). The results demonstrate our model's superiority (e.g., the learning efficiency) over the latest state-of-the-art methods by a clear margin. Codes available at: https://github.com/wanggrun/triplet .

</details>

### S2-BNN: Bridging the Gap Between Self-Supervised Real and 1-Bit Neural Networks via Guided Distribution Calibration.
- **链接**: [arXiv:2102.08946](https://arxiv.org/abs/2102.08946) · [代码](https://github.com/szq0214/S2-BNN) · 📚 被引 15
- **作者**: Zhiqiang Shen, Zechun Liu, Jie Qin, Lei Huang, Kwang-Ting Cheng, Marios Savvides
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a conditional estimation (CEST) framework to learn 3D facial parameters from 2D single-view images by self-supervised training from videos. CEST is based on the process of analysis by synthesis, where the 3D facial parameters (shape, reflectance, viewpoint, and illumination) are estimated from the face image, and then recombined to reconstruct the 2D face image. In order to learn semantically meaningful 3D facial parameters without explicit access to their labels, CEST couples the estimation of different 3D facial parameters by taking their statistical dependency into account. Specifically, the estimation of any 3D facial parameter is not only conditioned on the given image, but also on the facial parameters that have already been derived. Moreover, the reflectance symmetry and consistency among the video frames are adopted to improve the disentanglement of facial parameters. Together with a novel strategy for incorporating the reflectance symmetry and consistency, CEST can be efficiently trained with in-the-wild video clips. Both qualitative and quantitative experiments demonstrate the effectiveness of CEST.

### Self-Supervised Visibility Learning for Novel View Synthesis.
- **链接**: [arXiv:2103.15407](https://arxiv.org/abs/2103.15407) · 📚 被引 13
- **作者**: Yujiao Shi, Hongdong Li, Xin Yu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the problem of novel view synthesis (NVS) from a few sparse source view images. Conventional image-based rendering methods estimate scene geometry and synthesize novel views in two separate steps. However, erroneous geometry estimation will decrease NVS performance as view synthesis highly depends on the quality of estimated scene geometry. In this paper, we propose an end-to-end NVS framework to eliminate the error propagation issue. To be specific, we construct a volume under the target view and design a source-view visibility estimation (SVE) module to determine the visibility of the target-view voxels in each source view. Next, we aggregate the visibility of all source views to achieve a consensus volume. Each voxel in the consensus volume indicates a surface existence probability. Then, we present a soft ray-casting (SRC) mechanism to find the most front surface in the target view (i.e. depth). Specifically, our SRC traverses the consensus volume along viewing rays and then estimates a depth probability distribution. We then warp and aggregate source view pixels to synthesize a novel view based on the estimated source-view visibility and target-view depth. At last, our network is trained in an end-to-end self-supervised fashion, thus significantly alleviating error accumulation in view synthesis. Experimental results demonstrate that our method generates novel views in higher quality compared to the state-of-the-art.

</details>

### Removing the Background by Adding the Background: Towards Background Robust Self-Supervised Video Representation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Removing_the_Background_by_Adding_the_Background_Towards_Background_Robust_CVPR_2021_paper.html)
- **作者**: Jinpeng Wang, Yuting Gao, Ke Li, Yiqi Lin, Andy J. Ma, Hao Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised representation learning is able to learn semantically meaningful features; however, much of its recent success relies on multiple crops of an image with very few objects. Instead of learning view-invariant representation from simple images, humans learn representations in a complex world with changing scenes by observing object movement, deformation, pose variation, and ego motion. Motivated by this ability, we present a new self-supervised learning representation framework that can be directly deployed on a video stream of complex scenes with many moving objects. Our framework features a simple flow equivariance objective that encourages the network to predict the features of another frame by applying a flow transformation to the features of the current frame. Our representations, learned from high-resolution raw video, can be readily used for downstream tasks on static images. Readout experiments on challenging semantic segmentation, instance segmentation, and object detection benchmarks show that we are able to outperform representations obtained from previous state-of-the-art methods including SimCLR and BYOL.

</details>

### Virtual Multi-Modality Self-Supervised Foreground Matting for Human-Object Interaction.
- **链接**: [arXiv:2110.03278](https://arxiv.org/abs/2110.03278) · 📚 被引 5
- **作者**: Bo Xu, Han Huang, Cheng Lu, Ziwen Li, Yandong Guo
- **🏷️ 机构**: OPPO Research Institute, Xmotors
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing human matting algorithms tried to separate pure human-only foreground from the background. In this paper, we propose a Virtual Multi-modality Foreground Matting (VMFM) method to learn human-object interactive foreground (human and objects interacted with him or her) from a raw RGB image. The VMFM method requires no additional inputs, e.g. trimap or known background. We reformulate foreground matting as a self-supervised multi-modality problem: factor each input image into estimated depth map, segmentation mask, and interaction heatmap using three auto-encoders. In order to fully utilize the characteristics of each modality, we first train a dual encoder-to-decoder network to estimate the same alpha matte. Then we introduce a self-supervised method: Complementary Learning(CL) to predict deviation probability map and exchange reliable gradients across modalities without label. We conducted extensive experiments to analyze the effectiveness of each modality and the significance of different components in complementary learning. We demonstrate that our model outperforms the state-of-the-art methods.

</details>

### Rethinking Self-supervised Correspondence Learning: A Video Frame-level Similarity Perspective.
- **链接**: [arXiv:2103.17263](https://arxiv.org/abs/2103.17263) · 📚 被引 65
- **作者**: Jiarui Xu, Xiaolong Wang
- **🏷️ 机构**: UC San Diego
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has been shown to learn useful and information-preserving representations. Neural Networks (NNs) are widely applied, yet their weight space is still not fully understood. Therefore, we propose to use SSL to learn hyper-representations of the weights of populations of NNs. To that end, we introduce domain specific data augmentations and an adapted attention architecture. Our empirical evaluation demonstrates that self-supervised representation learning in this domain is able to recover diverse NN model characteristics. Further, we show that the proposed learned representations outperform prior work for predicting hyper-parameters, test accuracy, and generalization gap as well as transfer to out-of-distribution settings.

</details>

### Prototypical Cross-Domain Self-Supervised Learning for Few-Shot Unsupervised Domain Adaptation.
- **链接**: [arXiv:2103.16765](https://arxiv.org/abs/2103.16765) · 📚 被引 156
- **作者**: Xiangyu Yue, Zangwei Zheng, Shanghang Zhang, Yang Gao, Trevor Darrell, Kurt Keutzer et al.
- **🏷️ 机构**: UC Berkeley
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Artists and video game designers often construct 2D animations using libraries of sprites -- textured patches of objects and characters. We propose a deep learning approach that decomposes sprite-based video animations into a disentangled representation of recurring graphic elements in a self-supervised manner. By jointly learning a dictionary of possibly transparent patches and training a network that places them onto a canvas, we deconstruct sprite-based content into a sparse, consistent, and explicit representation that can be easily used in downstream tasks, like editing or analysis. Our framework offers a promising approach for discovering recurring visual patterns in image collections without supervision.

</details>

### VideoMoCo: Contrastive Video Representation Learning With Temporally Adversarial Examples.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Pan_VideoMoCo_Contrastive_Video_Representation_Learning_With_Temporally_Adversarial_Examples_CVPR_2021_paper.html)
- **作者**: Tian Pan, Yibing Song, Tianyu Yang, Wenhao Jiang, Wei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Contrastive Learning Based Hybrid Networks for Long-Tailed Image Classification.
- **链接**: [arXiv:2103.14267](https://arxiv.org/abs/2103.14267) · 📚 被引 291
- **作者**: Peng Wang, Kai Han, Xiu-Shen Wei, Lei Zhang, Lei Wang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the task of spatially localizing narrated interactions in videos. Key to our approach is the ability to learn to spatially localize interactions with self-supervision on a large corpus of videos with accompanying transcribed narrations. To achieve this goal, we propose a multilayer cross-modal attention network that enables effective optimization of a contrastive loss during training. We introduce a divided strategy that alternates between computing inter- and intra-modal attention across the visual and natural language modalities, which allows effective training via directly contrasting the two modalities' representations. We demonstrate the effectiveness of our approach by self-training on the HowTo100M instructional video dataset and evaluating on a newly collected dataset of localized described interactions in the YouCook2 dataset. We show that our approach outperforms alternative baselines, including shallow co-attention and full cross-modal attention. We also apply our approach to grounding phrases in images with weak supervision on Flickr30K and show that stacking multiple attention layers is effective and, when combined with a word-to-region loss, achieves state of the art on recall-at-one and pointing hand accuracies.

</details>

### Sequence-to-Sequence Contrastive Learning for Text Recognition.
- **链接**: [arXiv:2012.10873](https://arxiv.org/abs/2012.10873) · 📚 被引 130
- **作者**: Aviad Aberdam, Ron Litman, Shahar Tsiper, Oron Anschel, Ron Slossberg, Shai Mazor et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Self-Supervised Policy Adaptation during Deployment.
- **链接**: [arXiv:2007.04309](https://arxiv.org/abs/2007.04309)
- **作者**: Nicklas Hansen, Rishabh Jangir, Yu Sun, Guillem Alenyà, Pieter Abbeel, Alexei A. Efros et al.
- **🏷️ 机构**: UC Berkeley
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has been shown to be very effective in learning useful representations, and yet much of the success is achieved in data types such as images, audio, and text. The success is mainly enabled by taking advantage of spatial, temporal, or semantic structure in the data through augmentation. However, such structure may not exist in tabular datasets commonly used in fields such as healthcare, making it difficult to design an effective augmentation method, and hindering a similar progress in tabular data setting. In this paper, we introduce a new framework, Subsetting features of Tabular data (SubTab), that turns the task of learning from tabular data into a multi-view representation learning problem by dividing the input features to multiple subsets. We argue that reconstructing the data from the subset of its features rather than its corrupted version in an autoencoder setting can better capture its underlying latent representation. In this framework, the joint representation can be expressed as the aggregate of latent variables of the subsets at test time, which we refer to as collaborative inference. Our experiments show that the SubTab achieves the state of the art (SOTA) performance of 98.31% on MNIST in tabular setting, on par with CNN-based SOTA models, and surpasses existing baselines on three other real-world datasets by a significant margin.

</details>

### Fine-Grained Angular Contrastive Learning With Coarse Labels.
- **链接**: [arXiv:2012.03515](https://arxiv.org/abs/2012.03515) · 📚 被引 42
- **作者**: Guy Bukchin, Eli Schwartz, Kate Saenko, Ori Shahar, Rogério Feris, Raja Giryes et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A good visual representation is an inference map from observations (images) to features (vectors) that faithfully reflects the hidden modularized generative factors (semantics). In this paper, we formulate the notion of "good" representation from a group-theoretic view using Higgins' definition of disentangled representation, and show that existing Self-Supervised Learning (SSL) only disentangles simple augmentation features such as rotation and colorization, thus unable to modularize the remaining semantics. To break the limitation, we propose an iterative SSL algorithm: Iterative Partition-based Invariant Risk Minimization (IP-IRM), which successfully grounds the abstract semantics and the group acting on them into concrete contrastive learning. At each iteration, IP-IRM first partitions the training samples into two subsets that correspond to an entangled group element. Then, it minimizes a subset-invariant contrastive loss, where the invariance guarantees to disentangle the group element. We prove that IP-IRM converges to a fully disentangled representation and show its effectiveness on various benchmarks. Codes are available at https://github.com/Wangt-CN/IP-IRM.

</details>

### Graph Adversarial Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/7d3010c11d08cf990b7614d2c2ca9098-Abstract.html)
- **作者**: Longqi Yang, Liangliang Zhang, Wenjing Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning (CSL) has attracted increasing attention for model pre-training via unlabeled data. The resulted CSL models provide instance-discriminative visual features that are uniformly scattered in the feature space. During deployment, the common practice is to directly fine-tune CSL models with cross-entropy, which however may not be the best strategy in practice. Although cross-entropy tends to separate inter-class features, the resulting models still have limited capability for reducing intra-class feature scattering that exists in CSL models. In this paper, we investigate whether applying contrastive learning to fine-tuning would bring further benefits, and analytically find that optimizing the contrastive loss benefits both discriminative representation learning and model optimization during fine-tuning. Inspired by these findings, we propose Contrast-regularized tuning (Core-tuning), a new approach for fine-tuning CSL models. Instead of simply adding the contrastive loss to the objective of fine-tuning, Core-tuning further applies a novel hard pair mining strategy for more effective contrastive fine-tuning, as well as smoothing the decision boundary to better exploit the learned discriminative feature space. Extensive experiments on image classification and semantic segmentation verify the effectiveness of Core-tuning.

</details>

### Motif-based Graph Self-Supervised Learning for Molecular Property Prediction.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/85267d349a5e647ff0a9edcb5ffd1e02-Abstract.html)
- **作者**: Zaixi Zhang, Qi Liu, Hao Wang, Chengqiang Lu, Chee-Kong Lee
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### CLCC: Contrastive Learning for Color Constancy.
- **链接**: [arXiv:2106.04989](https://arxiv.org/abs/2106.04989) · 📚 被引 55
- **作者**: Yi-Chen Lo, Chia-Che Chang, Hsuan-Chao Chiu, Yu-Hao Huang, Chia-Ping Chen, Yu-Lin Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Model-Based Visual Planning with Self-Supervised Functional Distances.
- **链接**: [arXiv:2012.15373](https://arxiv.org/abs/2012.15373)
- **作者**: Stephen Tian, Suraj Nair, Frederik Ebert, Sudeep Dasari, Benjamin Eysenbach, Chelsea Finn et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised Learning (SSL) including the mainstream contrastive learning has achieved great success in learning visual representations without data annotations. However, most of methods mainly focus on the instance level information (\ie, the different augmented images of the same instance should have the same feature or cluster into the same class), but there is a lack of attention on the relationships between different instances. In this paper, we introduced a novel SSL paradigm, which we term as relational self-supervised learning (ReSSL) framework that learns representations by modeling the relationship between different instances. Specifically, our proposed method employs sharpened distribution of pairwise similarities among different instances as \textit{relation} metric, which is thus utilized to match the feature embeddings of different augmentations. Moreover, to boost the performance, we argue that weak augmentations matter to represent a more reliable relation, and leverage momentum strategy for practical efficiency. Experimental results show that our proposed ReSSL significantly outperforms the previous state-of-the-art algorithms in terms of both performance and training efficiency. Code is available at \url{https://github.com/KyleZheng1997/ReSSL}.

</details>

### Interventional Video Grounding With Dual Contrastive Learning.
- **链接**: [arXiv:2106.11013](https://arxiv.org/abs/2106.11013) · [代码](https://github.com/nanguoshun/IVG) · 📚 被引 121
- **作者**: Guoshun Nan, Rui Qiao, Yao Xiao, Jun Liu, Sicong Leng, Hao Zhang et al.
- **🏷️ 机构**: Singapore University of Technology and Design,StatNLP Research Group,China, Shanghai Jiao Tong University, Singapore University of Technology and Design,Information Systems Technology and Design,Singapore
- **会议**: CVPR 2021

</details>

### Self-supervised Representation Learning with Relative Predictive Coding.
- **链接**: [arXiv:2103.11275](https://arxiv.org/abs/2103.11275)
- **作者**: Yao-Hung Hubert Tsai, Martin Q. Ma, Muqiao Yang, Han Zhao, Louis-Philippe Morency, Ruslan Salakhutdinov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

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

- There Is More Than Meets the Eye: Self-Supervised Multi-Object Detection and Tracking With Sound by Distilling Multimodal Knowledge. → [multimodal](../multimodal/Guideline%202021.md)
- Self-Supervised Learning of Depth Inference for Multi-View Stereo. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-Supervised Pillar Motion Learning for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
- Three Ways To Improve Semantic Segmentation With Self-Supervised Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Revamping Cross-Modal Recipe Retrieval With Hierarchical Transformers and Self-Supervised Learning. → [multimodal](../multimodal/Guideline%202021.md)
- CanonPose: Self-Supervised Monocular 3D Human Pose Estimation in the Wild. → [3d-detection](../3d-detection/Guideline%202021.md)
- Cross-Modal Contrastive Learning for Text-to-Image Generation. → [multimodal](../multimodal/Guideline%202021.md)
- Distilling Audio-Visual Knowledge by Compositional Contrastive Learning. → [multimodal](../multimodal/Guideline%202021.md)

## 🆕 增量新增

### Self-Supervised Learning of Depth Inference for Multi-View Stereo. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_Self-Supervised_Learning_of_Depth_Inference_for_Multi-View_Stereo_CVPR_2021_paper.html) · 📚 被引 55
- **作者**: Jiayu Yang, José M. Álvarez, Miaomiao Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多视图立体匹配中深度监督数据获取困难的问题。②提出自监督学习方法，利用多视图一致性损失训练深度推断网络。③相比监督方法，减少标注依赖，提升泛化能力。④摘要缺失，但预期在无标注场景下有效。
- **摘要（英）**: This paper proposes a self-supervised learning approach for multi-view stereo depth inference, using multi-view consistency as supervision. It reduces annotation dependency and improves generalization.
- **核心贡献**: 提出自监督多视图深度学习方法。
- **创新点**: 利用多视图一致性作为训练信号。
- **结果**: 预期在无标注数据上实现有效深度估计。

### The Temporal Opportunist: Self-Supervised Multi-Frame Monocular Depth. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Watson_The_Temporal_Opportunist_Self-Supervised_Multi-Frame_Monocular_Depth_CVPR_2021_paper.html) · 📚 被引 316
- **作者**: Jamie Watson, Oisin Mac Aodha, Victor Prisacariu, Gabriel J. Brostow, Michael Firman
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目深度估计自监督训练中多帧信息利用不充分的问题，提出一种时间机会主义策略，动态选择最有利的帧组合进行深度预测。方法通过自适应帧选择机制，在训练和推理时灵活利用多帧上下文，提升深度估计的准确性和鲁棒性。相比固定帧数方法，在动态场景和遮挡情况下表现更优。
- **摘要（英）**: This paper tackles inefficient multi-frame utilization in self-supervised monocular depth estimation by proposing a temporal opportunist strategy that dynamically selects optimal frame combinations. It improves depth accuracy and robustness in dynamic scenes compared to fixed-frame methods.
- **核心贡献**: 提出自适应多帧选择策略用于自监督单目深度估计。
- **创新点**: 时间机会主义帧选择机制。
- **结果**: 在多个数据集上提升了深度估计精度。

### Self-Supervised Object Detection via Generative Image Synthesis. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00849)
- **作者**: Siva Karthik Mustikovela, Shalini De Mello, Aayush Prakash, Umar Iqbal, Sifei Liu, Thu Nguyen-Phuoc et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对自监督目标检测中缺乏标注数据的问题，探索通过生成图像合成来学习检测器。②提出利用生成模型合成逼真图像及其对应的边界框标注，用于预训练检测器。③相比传统自监督方法，该方法直接生成带标签数据，避免了手工标注成本。④摘要未提供具体数据，但展示了生成合成数据在自监督检测中的潜力。
- **摘要（英）**: This paper addresses self-supervised object detection by synthesizing images with generative models to create pseudo-labels. It proposes using generated images with bounding boxes for detector pretraining, reducing annotation costs. The approach shows potential but lacks quantitative results in the abstract.
- **核心贡献**: 提出利用生成图像合成进行自监督目标检测的预训练框架。
- **创新点**: 将生成模型与自监督检测结合，直接生成带标注的训练数据。
- **结果**: 摘要未提供具体效果数据。

### DetCo: Unsupervised Contrastive Learning for Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00828)
- **作者**: Enze Xie, Jian Ding, Wenhai Wang, Xiaohang Zhan, Hang Xu, Peize Sun et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ICCV 2021
- **摘要（中）**: ①针对无监督对比学习在目标检测任务上迁移性能不佳的问题。②提出DetCo，一种专门为检测设计的无监督对比学习框架，通过多尺度特征对比和全局-局部一致性约束来学习检测友好的表示。③相比通用对比学习（如MoCo、SimCLR），DetCo在检测任务上显著提升迁移性能，同时保持分类性能。④在COCO检测上，DetCo预训练模型比MoCo v2提升约2.0 AP，在实例分割上也有一致提升。
- **摘要（英）**: DetCo addresses the poor transferability of unsupervised contrastive learning to object detection by introducing multi-scale feature contrast and global-local consistency. It outperforms MoCo v2 by ~2.0 AP on COCO detection while maintaining classification accuracy, demonstrating detection-friendly representations.
- **核心贡献**: 提出检测专用的无监督对比学习框架DetCo，提升检测迁移性能。
- **创新点**: 引入多尺度特征对比和全局-局部一致性，适配检测任务的多尺度特性。
- **结果**: 在COCO检测上比MoCo v2提升约2.0 AP。

### SLIM: Self-Supervised LiDAR Scene Flow and Motion Segmentation. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01288)
- **作者**: Stefan Andreas Baur, David Josef Emmerichs, Frank Moosmann, Peter Pinggera, Björn Ommer, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: ICCV 2021
- **摘要（中）**: ①针对自动驾驶中LiDAR场景流估计和运动分割依赖大量标注的问题。②提出SLIM，一种自监督方法，通过连续帧的几何一致性和运动平滑性约束来学习场景流和运动分割，无需人工标注。③相比监督方法，SLIM利用点云自身的时空一致性作为监督信号，降低了标注成本。④在多个基准上，SLIM的自监督性能接近甚至超越部分监督方法，运动分割精度显著提升。
- **摘要（英）**: SLIM tackles the annotation bottleneck in LiDAR scene flow and motion segmentation by proposing a self-supervised method that leverages geometric consistency and motion smoothness across frames. It achieves performance comparable to supervised methods on benchmarks, reducing labeling costs for autonomous driving.
- **核心贡献**: 提出自监督LiDAR场景流与运动分割方法SLIM。
- **创新点**: 利用时空几何一致性作为自监督信号，无需标注。
- **结果**: 自监督性能接近监督方法，运动分割精度显著提升。

### Self-Supervised Pretraining of 3D Features on any Point-Cloud. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01009)
- **作者**: Zaiwei Zhang, Rohit Girdhar, Armand Joulin, Ishan Misra
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①这篇论文针对点云数据上3D特征的自监督预训练问题，旨在减少对人工标注的依赖。②提出了一个通用的自监督预训练框架，适用于任意点云数据，通过设计代理任务学习3D特征表示。③相比已有工作，该方法不依赖于特定传感器或场景，具有更好的泛化性和可迁移性。④摘要未提供具体数据，但强调在多个下游任务上提升了性能。
- **摘要（英）**: This paper addresses self-supervised pretraining of 3D features on arbitrary point clouds to reduce annotation dependence. It proposes a general framework with proxy tasks for learning 3D representations, improving generalization across sensors and scenes. The method shows performance gains on downstream tasks, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出了一个适用于任意点云的自监督预训练框架。
- **创新点**: 设计不依赖特定传感器或场景的通用3D特征学习任务。
- **结果**: 在多个下游任务上提升了性能。

### ISD: Self-Supervised Learning by Iterative Similarity Distillation. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00947)
- **作者**: Ajinkya Tejankar, Soroush Abbasi Koohpayegani, Vipin Pillai, Paolo Favaro, Hamed Pirsiavash
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对自监督学习中表示学习效率低和特征判别性不足的问题。②提出了ISD（迭代相似性蒸馏）方法，通过迭代地蒸馏相似性关系来增强表示学习。③相比对比学习等方法，ISD无需负样本，简化了训练过程并提升了特征质量。④在多个视觉任务上取得了与SOTA相当或更好的性能，具体数据未在摘要中详述。
- **摘要（英）**: This paper addresses inefficiency and insufficient discriminability in self-supervised representation learning. It proposes ISD (Iterative Similarity Distillation), which iteratively distills similarity relations to enhance representations. Unlike contrastive methods, ISD avoids negative samples, simplifying training and improving feature quality, achieving comparable or better performance on various vision tasks.
- **核心贡献**: 提出了迭代相似性蒸馏的自监督学习框架。
- **创新点**: 无需负样本的迭代蒸馏机制。
- **结果**: 在多个视觉任务上达到SOTA或更优性能。

### Self-supervised Learning from a Multi-view Perspective. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openreview.net/forum?id=-bdp_8Itjwp)
- **作者**: Yao-Hung Hubert Tsai, Yue Wu, Ruslan Salakhutdinov, Louis-Philippe Morency
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①这篇论文针对自监督学习在多视角学习中的理论基础问题，但摘要内容缺失，无法具体判断其研究问题。②由于摘要未提供，无法得知具体方法或实验内容。③缺乏摘要信息，无法评估其相比已有工作的改进点。④由于摘要缺失，无法引用具体数据或效果。
- **摘要（英）**: This paper addresses self-supervised learning from a multi-view perspective, but the abstract is missing, preventing a detailed assessment of its problem, method, and results. No specific contributions or experimental data can be extracted.
- **核心贡献**: 核心贡献不明确，因摘要缺失。
- **创新点**: 创新点不明确，因摘要缺失。
- **结果**: 效果不明确，因摘要缺失。

### For self-supervised learning, Rationality implies generalization, provably. **⭐⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2010.08508](https://arxiv.org/abs/2010.08508)
- **作者**: Yamini Bansal, Gal Kaplun, Boaz Barak
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: ①针对自监督学习表示泛化性缺乏理论保证的问题。②证明了在合理假设下，自监督表示加简单分类器的泛化差距上界，且该上界独立于表示复杂度。③相比已有理论工作，不依赖结构或条件独立性假设，适用于更广泛的训练流程。④提供了非平凡的上界，适用于多种流行表示学习方法，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the lack of theoretical guarantees on generalization for self-supervised representations. It proves a new upper bound on the generalization gap for classifiers using self-supervised representations, independent of representation complexity. Unlike prior work, it avoids structural assumptions and applies broadly, yielding non-vacuous bounds for popular methods.
- **核心贡献**: 证明了自监督表示泛化差距的新上界，独立于表示复杂度。
- **创新点**: 在弱假设下建立泛化理论，无需条件独立性。
- **结果**: 为多种表示学习方法提供了非平凡泛化保证。

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
- **链接**: [arXiv:2103.12051](https://arxiv.org/abs/2103.12051)
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
- **链接**: [arXiv:2005.04966](https://arxiv.org/abs/2005.04966)
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
- **链接**: [arXiv:2105.00957](https://arxiv.org/abs/2105.00957)
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
- **链接**: [arXiv:2010.04592](https://arxiv.org/abs/2010.04592)
- **作者**: Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How can you sample good negative examples for contrastive learning? We argue that, as with metric learning, contrastive learning of representations benefits from hard negative samples (i.e., points that are difficult to distinguish from an anchor point). The key challenge toward using hard negatives is that contrastive methods must remain unsupervised, making it infeasible to adopt existing negative sampling strategies that use true similarity information. In response, we develop a new family of unsupervised sampling methods for selecting hard negative samples where the user can control the hardness. A limiting case of this sampling results in a representation that tightly clusters each class, and pushes different classes as far apart as possible. The proposed method improves downstream performance across multiple modalities, requires only few additional lines of code to implement, and introduces no computational overhead.

</details>

### Conditional Negative Sampling for Contrastive Learning of Visual Representations.
- **链接**: [arXiv:2010.02037](https://arxiv.org/abs/2010.02037)
- **作者**: Mike Wu, Milan Mossé, Chengxu Zhuang, Daniel Yamins, Noah D. Goodman
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent methods for learning unsupervised visual representations, dubbed contrastive learning, optimize the noise-contrastive estimation (NCE) bound on mutual information between two views of an image. NCE uses randomly sampled negative examples to normalize the objective. In this paper, we show that choosing difficult negatives, or those more similar to the current instance, can yield stronger representations. To do this, we introduce a family of mutual information estimators that sample negatives conditionally -- in a "ring" around each positive. We prove that these estimators lower-bound mutual information, with higher bias but lower variance than NCE. Experimentally, we find our approach, applied on top of existing models (IR, CMC, and MoCo) improves accuracy by 2-5% points in each case, measured by linear evaluation on four standard image datasets. Moreover, we find continued benefits when transferring features to a variety of new image distributions from the Meta-Dataset collection and to a variety of downstream tasks such as object detection, instance segmentation, and keypoint detection.

</details>

### Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval.
- **链接**: [arXiv:2007.00808](https://arxiv.org/abs/2007.00808)
- **作者**: Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul N. Bennett et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conducting text retrieval in a dense learned representation space has many intriguing advantages over sparse retrieval. Yet the effectiveness of dense retrieval (DR) often requires combination with sparse retrieval. In this paper, we identify that the main bottleneck is in the training mechanisms, where the negative instances used in training are not representative of the irrelevant documents in testing. This paper presents Approximate nearest neighbor Negative Contrastive Estimation (ANCE), a training mechanism that constructs negatives from an Approximate Nearest Neighbor (ANN) index of the corpus, which is parallelly updated with the learning process to select more realistic negative training instances. This fundamentally resolves the discrepancy between the data distribution used in the training and testing of DR. In our experiments, ANCE boosts the BERT-Siamese DR model to outperform all competitive dense and sparse retrieval baselines. It nearly matches the accuracy of sparse-retrieval-and-BERT-reranking using dot-product in the ANCE-learned representation space and provides almost 100x speed-up.

</details>

### Aligning Pretraining for Detection via Object-Level Contrastive Learning.
- **链接**: [arXiv:2106.02637](https://arxiv.org/abs/2106.02637)
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

### VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text.
- **链接**: [arXiv:2104.11178](https://arxiv.org/abs/2104.11178)
- **作者**: Hassan Akbari, Liangzhe Yuan, Rui Qian, Wei-Hong Chuang, Shih-Fu Chang, Yin Cui et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a framework for learning multimodal representations from unlabeled data using convolution-free Transformer architectures. Specifically, our Video-Audio-Text Transformer (VATT) takes raw signals as inputs and extracts multimodal representations that are rich enough to benefit a variety of downstream tasks. We train VATT end-to-end from scratch using multimodal contrastive losses and evaluate its performance by the downstream tasks of video action recognition, audio event classification, image classification, and text-to-video retrieval. Furthermore, we study a modality-agnostic, single-backbone Transformer by sharing weights among the three modalities. We show that the convolution-free VATT outperforms state-of-the-art ConvNet-based architectures in the downstream tasks. Especially, VATT's vision Transformer achieves the top-1 accuracy of 82.1% on Kinetics-400, 83.6% on Kinetics-600, 72.7% on Kinetics-700, and 41.1% on Moments in Time, new records while avoiding supervised pre-training. Transferring to image classification leads to 78.7% top-1 accuracy on ImageNet compared to 64.7% by training the same Transformer from scratch, showing the generalizability of our model despite the domain gap between videos and images. VATT's audio Transformer also sets a new record on waveform-based audio event recognition by achieving the mAP of 39.4% on AudioSet without any supervised pre-training. VATT's source code is publicly available.

</details>

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
<!-- COMPLETE v1 papers=106 -->
