# Self-supervised Vision — 2020 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 34 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### From Image Collections to Point Clouds With Self-Supervised Shape and Pose Networks.
- **链接**: [arXiv:2005.01939](https://arxiv.org/abs/2005.01939) · 📚 被引 31
- **作者**: Navaneet K. L., Ansu Mathew, Shashank Kashyap, Wei-Chih Hung, Varun Jampani, R. Venkatesh Babu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Self-Supervised Relational Reasoning for Representation Learning.
- **链接**: [arXiv:2006.05849](https://arxiv.org/abs/2006.05849)
- **作者**: Massimiliano Patacchiola, Amos J. Storkey
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video prediction models combined with planning algorithms have shown promise in enabling robots to learn to perform many vision-based tasks through only self-supervision, reaching novel goals in cluttered scenes with unseen objects. However, due to the compounding uncertainty in long horizon video prediction and poor scalability of sampling-based planning optimizers, one significant limitation of these approaches is the ability to plan over long horizons to reach distant goals. To that end, we propose a framework for subgoal generation and planning, hierarchical visual foresight (HVF), which generates subgoal images conditioned on a goal image, and uses them for planning. The subgoal images are directly optimized to decompose the task into easy to plan segments, and as a result, we observe that the method naturally identifies semantically meaningful states as subgoals. Across three out of four simulated vision-based manipulation tasks, we find that our method achieves nearly a 200% performance improvement over planning without subgoals and model-free RL approaches. Further, our experiments illustrate that our approach extends to real, cluttered visual scenes. Project page: https://sites.google.com/stanford.edu/hvf

</details>

### Planning to Explore via Self-Supervised World Models.
- **链接**: [arXiv:2005.05960](https://arxiv.org/abs/2005.05960)
- **作者**: Ramanan Sekar, Oleh Rybkin, Kostas Daniilidis, Pieter Abbeel, Danijar Hafner, Deepak Pathak
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Monocular Trained Depth Estimation Using Self-Attention and Discrete Disparity Volume.
- **链接**: [arXiv:2003.13951](https://arxiv.org/abs/2003.13951) · 📚 被引 231
- **作者**: Adrian Johnston, Gustavo Carneiro
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning is showing great promise for monocular depth estimation, using geometry as the only source of supervision. Depth networks are indeed capable of learning representations that relate visual appearance to 3D properties by implicitly leveraging category-level patterns. In this work we investigate how to leverage more directly this semantic structure to guide geometric representation learning, while remaining in the self-supervised regime. Instead of using semantic labels and proxy losses in a multi-task approach, we propose a new architecture leveraging fixed pretrained semantic segmentation networks to guide self-supervised representation learning via pixel-adaptive convolutions. Furthermore, we propose a two-stage training process to overcome a common semantic bias on dynamic objects via resampling. Our method improves upon the state of the art for self-supervised monocular depth prediction over all pixels, fine-grained details, and per semantic categories.

</details>

### Self2Self With Dropout: Learning Self-Supervised Denoising From Single Image.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Quan_Self2Self_With_Dropout_Learning_Self-Supervised_Denoising_From_Single_Image_CVPR_2020_paper.html) · 📚 被引 381
- **作者**: Yuhui Quan, Mingqin Chen, Tongyao Pang, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Equivariant Attention Mechanism for Weakly Supervised Semantic Segmentation.
- **链接**: [arXiv:2004.04581](https://arxiv.org/abs/2004.04581) · 📚 被引 670
- **作者**: Yude Wang, Jie Zhang, Meina Kan, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work seeks the possibility of generating the human face from voice solely based on the audio-visual data without any human-labeled annotations. To this end, we propose a multi-modal learning framework that links the inference stage and generation stage. First, the inference networks are trained to match the speaker identity between the two different modalities. Then the trained inference networks cooperate with the generation network by giving conditional information about the voice. The proposed method exploits the recent development of GANs techniques and generates the human face directly from the speech waveform making our system fully end-to-end. We analyze the extent to which the network can naturally disentangle two latent factors that contribute to the generation of a face image - one that comes directly from a speech signal and the other that is not related to it - and explore whether the network can learn to generate natural human face image distribution by modeling these factors. Experimental results show that the proposed network can not only match the relationship between the human face and speech, but can also generate the high-quality human face sample conditioned on its speech. Finally, the correlation between the generated face and the corresponding speech is quantitatively measured to analyze the relationship between the two modalities.

</details>

### Adversarial Robustness: From Self-Supervised Pre-Training to Fine-Tuning.
- **链接**: [arXiv:2003.12862](https://arxiv.org/abs/2003.12862) · [代码](https://github.com/TAMU-VITA/Adv-SS-Pretraining) · 📚 被引 132
- **作者**: Tianlong Chen, Sijia Liu, Shiyu Chang, Yu Cheng, Lisa Amini, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Increasing model size when pretraining natural language representations often results in improved performance on downstream tasks. However, at some point further model increases become harder due to GPU/TPU memory limitations and longer training times. To address these problems, we present two parameter-reduction techniques to lower memory consumption and increase the training speed of BERT. Comprehensive empirical evidence shows that our proposed methods lead to models that scale much better compared to the original BERT. We also use a self-supervised loss that focuses on modeling inter-sentence coherence, and show it consistently helps downstream tasks with multi-sentence inputs. As a result, our best model establishes new state-of-the-art results on the GLUE, RACE, and \squad benchmarks while having fewer parameters compared to BERT-large. The code and the pretrained models are available at https://github.com/google-research/ALBERT.

</details>

### Hierarchical Foresight: Self-Supervised Learning of Long-Horizon Tasks via Visual Subgoal Generation.
- **链接**: [arXiv:1909.05829](https://arxiv.org/abs/1909.05829)
- **作者**: Suraj Nair, Chelsea Finn
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video prediction models combined with planning algorithms have shown promise in enabling robots to learn to perform many vision-based tasks through only self-supervision, reaching novel goals in cluttered scenes with unseen objects. However, due to the compounding uncertainty in long horizon video prediction and poor scalability of sampling-based planning optimizers, one significant limitation of these approaches is the ability to plan over long horizons to reach distant goals. To that end, we propose a framework for subgoal generation and planning, hierarchical visual foresight (HVF), which generates subgoal images conditioned on a goal image, and uses them for planning. The subgoal images are directly optimized to decompose the task into easy to plan segments, and as a result, we observe that the method naturally identifies semantically meaningful states as subgoals. Across three out of four simulated vision-based manipulation tasks, we find that our method achieves nearly a 200% performance improvement over planning without subgoals and model-free RL approaches. Further, our experiments illustrate that our approach extends to real, cluttered visual scenes. Project page: https://sites.google.com/stanford.edu/hvf

</details>

### Neural Outlier Rejection for Self-Supervised Keypoint Learning.
- **链接**: [arXiv:1912.10615](https://arxiv.org/abs/1912.10615)
- **作者**: Jiexiong Tang, Hanme Kim, Vitor Guizilini, Sudeep Pillai, Rares Ambrus
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Monocular Scene Flow Estimation.
- **链接**: [arXiv:2004.04143](https://arxiv.org/abs/2004.04143) · 📚 被引 99
- **作者**: Junhwa Hur, Stefan Roth
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Identifying salient points in images is a crucial component for visual odometry, Structure-from-Motion or SLAM algorithms. Recently, several learned keypoint methods have demonstrated compelling performance on challenging benchmarks. However, generating consistent and accurate training data for interest-point detection in natural images still remains challenging, especially for human annotators. We introduce IO-Net (i.e. InlierOutlierNet), a novel proxy task for the self-supervision of keypoint detection, description and matching. By making the sampling of inlier-outlier sets from point-pair correspondences fully differentiable within the keypoint learning framework, we show that are able to simultaneously self-supervise keypoint description and improve keypoint matching. Second, we introduce KeyPointNet, a keypoint-network architecture that is especially amenable to robust keypoint detection and description. We design the network to allow local keypoint aggregation to avoid artifacts due to spatial discretizations commonly used for this task, and we improve fine-grained keypoint descriptor performance by taking advantage of efficient sub-pixel convolutions to upsample the descriptor feature-maps to a higher operating resolution. Through extensive experiments and ablative analysis, we show that the proposed self-supervised keypoint learning method greatly improves the quality of feature matching and homography estimation on challenging benchmarks over the state-of-the-art.

</details>

### Self-Supervised Learning of Interpretable Keypoints From Unlabelled Videos.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Jakab_Self-Supervised_Learning_of_Interpretable_Keypoints_From_Unlabelled_Videos_CVPR_2020_paper.html) · 📚 被引 57
- **作者**: Tomas Jakab, Ankush Gupta, Hakan Bilen, Andrea Vedaldi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Steering Self-Supervised Feature Learning Beyond Local Pixel Statistics.
- **链接**: [arXiv:2004.02331](https://arxiv.org/abs/2004.02331) · 📚 被引 33
- **作者**: Simon Jenni, Hailin Jin, Paolo Favaro
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A structured understanding of our world in terms of objects, relations, and hierarchies is an important component of human cognition. Learning such a structured world model from raw sensory data remains a challenge. As a step towards this goal, we introduce Contrastively-trained Structured World Models (C-SWMs). C-SWMs utilize a contrastive approach for representation learning in environments with compositional structure. We structure each state embedding as a set of object representations and their relations, modeled by a graph neural network. This allows objects to be discovered from raw pixel observations without direct supervision as part of the learning process. We evaluate C-SWMs on compositional environments involving multiple interacting objects that can be manipulated independently by an agent, simple Atari games, and a multi-object physics simulation. Our experiments demonstrate that C-SWMs can overcome limitations of models based on pixel reconstruction and outperform typical representatives of this model class in highly structured environments, while learning interpretable object-based representations.

</details>

### Self-Supervised 3D Human Pose Estimation via Part Guided Novel Image Synthesis.
- **链接**: [arXiv:2004.04400](https://arxiv.org/abs/2004.04400) · 📚 被引 66
- **作者**: Jogendra Nath Kundu, Siddharth Seth, Varun Jampani, Mugalodi Rakesh, R. Venkatesh Babu, Anirban Chakraborty
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera captured human pose is an outcome of several sources of variation. Performance of supervised 3D pose estimation approaches comes at the cost of dispensing with variations, such as shape and appearance, that may be useful for solving other related tasks. As a result, the learned model not only inculcates task-bias but also dataset-bias because of its strong reliance on the annotated samples, which also holds true for weakly-supervised models. Acknowledging this, we propose a self-supervised learning framework to disentangle such variations from unlabeled video frames. We leverage the prior knowledge on human skeleton and poses in the form of a single part-based 2D puppet model, human pose articulation constraints, and a set of unpaired 3D poses. Our differentiable formalization, bridging the representation gap between the 3D pose and spatial part maps, not only facilitates discovery of interpretable pose disentanglement but also allows us to operate on videos with diverse camera movements. Qualitative results on unseen in-the-wild datasets establish our superior generalization across multiple tasks beyond the primary tasks of 3D pose estimation and part segmentation. Furthermore, we demonstrate state-of-the-art weakly-supervised 3D pose estimation performance on both Human3.6M and MPI-INF-3DHP datasets.

</details>

### MAST: A Memory-Augmented Self-Supervised Tracker.
- **链接**: [arXiv:2002.07793](https://arxiv.org/abs/2002.07793) · 📚 被引 134
- **作者**: Zihang Lai, Erika Lu, Weidi Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised representation learning approaches have recently surpassed their supervised learning counterparts on downstream tasks like object detection and image classification. Somewhat mysteriously the recent gains in performance come from training instance classification models, treating each image and it's augmented versions as samples of a single class. In this work, we first present quantitative experiments to demystify these gains. We demonstrate that approaches like MOCO and PIRL learn occlusion-invariant representations. However, they fail to capture viewpoint and category instance invariance which are crucial components for object recognition. Second, we demonstrate that these approaches obtain further gains from access to a clean object-centric training dataset like Imagenet. Finally, we propose an approach to leverage unstructured videos to learn representations that possess higher viewpoint invariance. Our results show that the learned representations outperform MOCOv2 trained on the same data in terms of invariances encoded and the performance on downstream image classification and semantic segmentation tasks.

</details>

### Self-Supervised Graph Transformer on Large-Scale Molecular Data.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/94aef38441efa3380a3bed3faf1f9d5d-Abstract.html)
- **作者**: Yu Rong, Yatao Bian, Tingyang Xu, Weiyang Xie, Ying Wei, Wenbing Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Identifying salient points in images is a crucial component for visual odometry, Structure-from-Motion or SLAM algorithms. Recently, several learned keypoint methods have demonstrated compelling performance on challenging benchmarks. However, generating consistent and accurate training data for interest-point detection in natural images still remains challenging, especially for human annotators. We introduce IO-Net (i.e. InlierOutlierNet), a novel proxy task for the self-supervision of keypoint detection, description and matching. By making the sampling of inlier-outlier sets from point-pair correspondences fully differentiable within the keypoint learning framework, we show that are able to simultaneously self-supervise keypoint description and improve keypoint matching. Second, we introduce KeyPointNet, a keypoint-network architecture that is especially amenable to robust keypoint detection and description. We design the network to allow local keypoint aggregation to avoid artifacts due to spatial discretizations commonly used for this task, and we improve fine-grained keypoint descriptor performance by taking advantage of efficient sub-pixel convolutions to upsample the descriptor feature-maps to a higher operating resolution. Through extensive experiments and ablative analysis, we show that the proposed self-supervised keypoint learning method greatly improves the quality of feature matching and homography estimation on challenging benchmarks over the state-of-the-art.

</details>

### Contrastive Learning of Structured World Models.
- **链接**: [arXiv:1911.12247](https://arxiv.org/abs/1911.12247)
- **作者**: Thomas N. Kipf, Elise van der Pol, Max Welling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A structured understanding of our world in terms of objects, relations, and hierarchies is an important component of human cognition. Learning such a structured world model from raw sensory data remains a challenge. As a step towards this goal, we introduce Contrastively-trained Structured World Models (C-SWMs). C-SWMs utilize a contrastive approach for representation learning in environments with compositional structure. We structure each state embedding as a set of object representations and their relations, modeled by a graph neural network. This allows objects to be discovered from raw pixel observations without direct supervision as part of the learning process. We evaluate C-SWMs on compositional environments involving multiple interacting objects that can be manipulated independently by an agent, simple Atari games, and a multi-object physics simulation. Our experiments demonstrate that C-SWMs can overcome limitations of models based on pixel reconstruction and outperform typical representatives of this model class in highly structured environments, while learning interpretable object-based representations.

</details>

### Cross-lingual Retrieval for Iterative Self-Supervised Training.
- **链接**: [arXiv:2006.09526](https://arxiv.org/abs/2006.09526)
- **作者**: Chau Tran, Yuqing Tang, Xian Li, Jiatao Gu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### PULSE: Self-Supervised Photo Upsampling via Latent Space Exploration of Generative Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Menon_PULSE_Self-Supervised_Photo_Upsampling_via_Latent_Space_Exploration_of_Generative_CVPR_2020_paper.html) · 📚 被引 406
- **作者**: Sachit Menon, Alexandru Damian, Shijia Hu, Nikhil Ravi, Cynthia Rudin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Learning of Pretext-Invariant Representations.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Misra_Self-Supervised_Learning_of_Pretext-Invariant_Representations_CVPR_2020_paper.html) · 📚 被引 935
- **作者**: Ishan Misra, Laurens van der Maaten
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Just Go With the Flow: Self-Supervised Scene Flow Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Mittal_Just_Go_With_the_Flow_Self-Supervised_Scene_Flow_Estimation_CVPR_2020_paper.html) · 📚 被引 122
- **作者**: Himangi Mittal, Brian Okorn, David Held
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Viewpoint Learning From Image Collections.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Mustikovela_Self-Supervised_Viewpoint_Learning_From_Image_Collections_CVPR_2020_paper.html) · 📚 被引 26
- **作者**: Siva Karthik Mustikovela, Varun Jampani, Shalini De Mello, Sifei Liu, Umar Iqbal, Carsten Rother et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### A Self-supervised Approach for Adversarial Robustness.
- **链接**: [arXiv:2006.04924](https://arxiv.org/abs/2006.04924) · [代码](https://github.com/Muzammal-Naseer/NRP) · 📚 被引 260
- **作者**: Muzammal Naseer, Salman H. Khan, Munawar Hayat, Fahad Shahbaz Khan, Fatih Porikli
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have demonstrated the cross-lingual alignment ability of multilingual pretrained language models. In this work, we found that the cross-lingual alignment can be further improved by training seq2seq models on sentence pairs mined using their own encoder outputs. We utilized these findings to develop a new approach -- cross-lingual retrieval for iterative self-supervised training (CRISS), where mining and training processes are applied iteratively, improving cross-lingual alignment and translation ability at the same time. Using this method, we achieved state-of-the-art unsupervised machine translation results on 9 language directions with an average improvement of 2.4 BLEU, and on the Tatoeba sentence retrieval task in the XTREME benchmark on 16 languages with an average improvement of 21.5% in absolute accuracy. Furthermore, CRISS also brings an additional 1.8 BLEU improvement on average compared to mBART, when finetuned on supervised machine translation downstream tasks.

</details>

### How Useful Is Self-Supervised Pretraining for Visual Tasks?
- **链接**: [arXiv:2003.14323](https://arxiv.org/abs/2003.14323) · [代码](https://github.com/princeton-vl/selfstudy) · 📚 被引 82
- **作者**: Alejandro Newell, Jia Deng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised frameworks that learn denoising models with merely individual noisy images have shown strong capability and promising performance in various image denoising tasks. Existing self-supervised denoising frameworks are mostly built upon the same theoretical foundation, where the denoising models are required to be J-invariant. However, our analyses indicate that the current theory and the J-invariance may lead to denoising models with reduced performance. In this work, we introduce Noise2Same, a novel self-supervised denoising framework. In Noise2Same, a new self-supervised loss is proposed by deriving a self-supervised upper bound of the typical supervised loss. In particular, Noise2Same requires neither J-invariance nor extra information about the noise model and can be used in a wider range of denoising applications. We analyze our proposed Noise2Same both theoretically and experimentally. The experimental results show that our Noise2Same remarkably outperforms previous self-supervised denoising methods in terms of denoising performance and training efficiency. Our code is available at https://github.com/divelab/Noise2Same.

</details>

### Fast(er) Reconstruction of Shredded Text Documents via Self-Supervised Deep Asymmetric Metric Learning.
- **链接**: [arXiv:2003.10063](https://arxiv.org/abs/2003.10063) · 📚 被引 7
- **作者**: Thiago M. Paixão, Rodrigo Ferreira Berriel, Maria C. S. Boeres, Alessandro L. Koerich, Claudine Badue, Alberto F. De Souza et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We create a framework for bootstrapping visual representation learning from a primitive visual grouping capability. We operationalize grouping via a contour detector that partitions an image into regions, followed by merging of those regions into a tree hierarchy. A small supervised dataset suffices for training this grouping primitive. Across a large unlabeled dataset, we apply this learned primitive to automatically predict hierarchical region structure. These predictions serve as guidance for self-supervised contrastive feature learning: we task a deep network with producing per-pixel embeddings whose pairwise distances respect the region hierarchy. Experiments demonstrate that our approach can serve as state-of-the-art generic pre-training, benefiting downstream tasks. We additionally explore applications to semantic region search and video-based object instance tracking.

</details>

### Self-Supervised Human Depth Estimation From Monocular Videos.
- **链接**: [arXiv:2005.03358](https://arxiv.org/abs/2005.03358) · 📚 被引 24
- **作者**: Feitong Tan, Hao Zhu, Zhaopeng Cui, Siyu Zhu, Marc Pollefeys, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous methods on estimating detailed human depth often require supervised training with `ground truth' depth data. This paper presents a self-supervised method that can be trained on YouTube videos without known depth, which makes training data collection simple and improves the generalization of the learned network. The self-supervised learning is achieved by minimizing a photo-consistency loss, which is evaluated between a video frame and its neighboring frames warped according to the estimated depth and the 3D non-rigid motion of the human body. To solve this non-rigid motion, we first estimate a rough SMPL model at each video frame and compute the non-rigid body motion accordingly, which enables self-supervised learning on estimating the shape details. Experiments demonstrate that our method enjoys better generalization and performs much better on data in the wild.

</details>

### Self-Supervised Human Depth Estimation From Monocular Videos.
- **链接**: [arXiv:2005.03358](https://arxiv.org/abs/2005.03358) · 📚 被引 24
- **作者**: Feitong Tan, Hao Zhu, Zhaopeng Cui, Siyu Zhu, Marc Pollefeys, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous methods on estimating detailed human depth often require supervised training with `ground truth' depth data. This paper presents a self-supervised method that can be trained on YouTube videos without known depth, which makes training data collection simple and improves the generalization of the learned network. The self-supervised learning is achieved by minimizing a photo-consistency loss, which is evaluated between a video frame and its neighboring frames warped according to the estimated depth and the 3D non-rigid motion of the human body. To solve this non-rigid motion, we first estimate a rough SMPL model at each video frame and compute the non-rigid body motion accordingly, which enables self-supervised learning on estimating the shape details. Experiments demonstrate that our method enjoys better generalization and performs much better on data in the wild.

</details>

### Joint Contrastive Learning with Infinite Possibilities.
- **链接**: [arXiv:2009.14776](https://arxiv.org/abs/2009.14776)
- **作者**: Qi Cai, Yu Wang, Yingwei Pan, Ting Yao, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Domain-Aware Generative Network for Generalized Zero-Shot Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wu_Self-Supervised_Domain-Aware_Generative_Network_for_Generalized_Zero-Shot_Learning_CVPR_2020_paper.html) · 📚 被引 54
- **作者**: Jiamin Wu, Tianzhu Zhang, Zheng-Jun Zha, Jiebo Luo, Yongdong Zhang, Feng Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Video Playback Rate Perception for Self-Supervised Spatio-Temporal Representation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Yao_Video_Playback_Rate_Perception_for_Self-Supervised_Spatio-Temporal_Representation_Learning_CVPR_2020_paper.html)
- **作者**: Yuan Yao, Chang Liu, Dezhao Luo, Yu Zhou, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Scene De-Occlusion.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhan_Self-Supervised_Scene_De-Occlusion_CVPR_2020_paper.html)
- **作者**: Xiaohang Zhan, Xingang Pan, Bo Dai, Ziwei Liu, Dahua Lin, Chen Change Loy
- **🏷️ 机构**: Shanghai AI Lab, CUHK
- **会议**: CVPR 2020

### Look-Into-Object: Self-Supervised Structure Modeling for Object Recognition.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhou_Look-Into-Object_Self-Supervised_Structure_Modeling_for_Object_Recognition_CVPR_2020_paper.html) · 📚 被引 73
- **作者**: Mohan Zhou, Yalong Bai, Wei Zhang, Tiejun Zhao, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### S3VAE: Self-Supervised Sequential VAE for Representation Disentanglement and Data Generation.
- **链接**: [arXiv:2005.11437](https://arxiv.org/abs/2005.11437) · 📚 被引 60
- **作者**: Yizhe Zhu, Martin Renqiang Min, Asim Kadav, Hans Peter Graf
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a sequential variational autoencoder to learn disentangled representations of sequential data (e.g., videos and audios) under self-supervision. Specifically, we exploit the benefits of some readily accessible supervisory signals from input data itself or some off-the-shelf functional models and accordingly design auxiliary tasks for our model to utilize these signals. With the supervision of the signals, our model can easily disentangle the representation of an input sequence into static factors and dynamic factors (i.e., time-invariant and time-varying parts). Comprehensive experiments across videos and audios verify the effectiveness of our model on representation disentanglement and generation of sequential data, and demonstrate that, our model with self-supervision performs comparable to, if not better than, the fully-supervised model with ground truth labels, and outperforms state-of-the-art unsupervised models by a large margin.

</details>

### Disentangled and Controllable Face Image Generation via 3D Imitative-Contrastive Learning.
- **链接**: [arXiv:2004.11660](https://arxiv.org/abs/2004.11660) · 📚 被引 287
- **作者**: Yu Deng, Jiaolong Yang, Dong Chen, Fang Wen, Xin Tong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose DiscoFaceGAN, an approach for face image generation of virtual people with disentangled, precisely-controllable latent representations for identity of non-existing people, expression, pose, and illumination. We embed 3D priors into adversarial learning and train the network to imitate the image formation of an analytic 3D face deformation and rendering process. To deal with the generation freedom induced by the domain gap between real and rendered faces, we further introduce contrastive learning to promote disentanglement by comparing pairs of generated images. Experiments show that through our imitative-contrastive learning, the factor variations are very well disentangled and the properties of a generated face can be precisely controlled. We also analyze the learned latent space and present several meaningful properties supporting factor disentanglement. Our method can also be used to embed real images into the disentangled latent space. We hope our method could provide new understandings of the relationship between physical properties and deep image synthesis.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose DiscoFaceGAN, an approach for face image generation of virtual people with disentangled, precisely-controllable latent representations for identity of non-existing people, expression, pose, and illumination. We embed 3D priors into adversarial learning and train the network to imitate the image formation of an analytic 3D face deformation and rendering process. To deal with the generation freedom induced by the domain gap between real and rendered faces, we further introduce contrastive learning to promote disentanglement by comparing pairs of generated images. Experiments show that through our imitative-contrastive learning, the factor variations are very well disentangled and the properties of a generated face can be precisely controlled. We also analyze the learned latent space and present several meaningful properties supporting factor disentanglement. Our method can also be used to embed real images into the disentangled latent space. We hope our method could provide new understandings of the relationship between physical properties and deep image synthesis.

</details>

## 跨领域论文（完整笔记在其他领域）

- 3D Packing for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Exploit Clues From Views: Self-Supervised and Regularized Learning for Multiview Object Recognition. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- On the Uncertainty of Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)

## 🆕 增量新增

### Vision-Language Navigation With Self-Supervised Auxiliary Reasoning Tasks. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:1911.07883](https://arxiv.org/abs/1911.07883) · 📚 被引 161
- **作者**: Fengda Zhu, Yi Zhu, Xiaojun Chang, Xiaodan Liang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对视觉语言导航（VLN）任务中智能体忽略环境隐含语义信息（如导航图、子轨迹语义）的问题。②提出了AuxRN框架，包含四个自监督辅助推理任务：解释先前动作、估计导航进度、预测下一朝向、评估轨迹一致性，以利用额外训练信号。③相比现有跨模态方法，通过辅助任务增强语义表示学习，使智能体能推理自身活动并全面感知环境。④实验表明辅助推理任务显著提升了导航性能，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the VLN task by introducing AuxRN, a framework with four self-supervised auxiliary reasoning tasks to exploit implicit semantic information in environments. It improves semantic representation learning and navigation performance, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出自监督辅助推理任务框架AuxRN，增强VLN智能体的语义推理能力。
- **创新点**: 设计四个自监督辅助任务，从多角度挖掘环境语义信息。
- **结果**: 实验显示辅助推理任务提升导航性能，但无具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation (VLN) is a task where agents learn to navigate following natural language instructions. The key to this task is to perceive both the visual scene and natural language sequentially. Conventional approaches exploit the vision and language features in cross-modal grounding. However, the VLN task remains challenging, since previous works have neglected the rich semantic information contained in the environment (such as implicit navigation graphs or sub-trajectory semantics). In this paper, we introduce Auxiliary Reasoning Navigation (AuxRN), a framework with four self-supervised auxiliary reasoning tasks to take advantage of the additional training signals derived from the semantic information. The auxiliary tasks have four reasoning objectives: explaining the previous actions, estimating the navigation progress, predicting the next orientation, and evaluating the trajectory consistency. As a result, these additional training signals help the agent to acquire knowledge of semantic representations in order to reason about its activity and build a thorough perception of the environment. Our experiments indicate that auxiliary reasoning tasks improve both the performance of the main task and the model generalizability by a large margin. Empirically, we demonstrate that an agent trained with self-supervised auxiliary reasoning tasks substantially outperforms the previous state-of-the-art method, being the best existing approach on the standard benchmark.

</details>

### Action Segmentation With Joint Self-Supervised Temporal Domain Adaptation. **⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2003.02824](https://arxiv.org/abs/2003.02824) · 📚 被引 90
- **作者**: Min-Hung Chen, Baopu Li, Yingze Bao, Ghassan AlRegib, Zsolt Kira
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对动作分割中时空变化导致性能不佳的问题，不同人执行同一动作存在差异，而标注数据有限。②提出自监督时间域适应（SSTDA），将动作分割视为跨域问题，通过两个自监督辅助任务（二元和序列域预测）对齐嵌入局部和全局时间动态的跨域特征。③相比其他域适应方法，SSTDA利用自监督信号更有效地减少域差异，无需额外标注。④在GTEA、50Salads和Breakfast数据集上，SSTDA大幅超越现有方法（如Breakfast上F1@25从59.6%提升至69.1%），且仅需65%的标注数据即可达到可比性能。
- **摘要（英）**: This paper addresses action segmentation under spatiotemporal variations by reformulating it as a cross-domain problem and proposing Self-Supervised Temporal Domain Adaptation (SSTDA) with two auxiliary tasks to align features. It outperforms state-of-the-art methods on GTEA, 50Salads, and Breakfast (e.g., F1@25 from 59.6% to 69.1% on Breakfast) and requires only 65% of labeled data.
- **核心贡献**: 提出自监督时间域适应方法，利用未标注视频提升动作分割性能。
- **创新点**: 设计二元和序列域预测任务，联合对齐局部和全局时间动态。
- **结果**: 在三个基准数据集上大幅超越现有方法，且数据效率高。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent progress of fully-supervised action segmentation techniques, the performance is still not fully satisfactory. One main challenge is the problem of spatiotemporal variations (e.g. different people may perform the same activity in various ways). Therefore, we exploit unlabeled videos to address this problem by reformulating the action segmentation task as a cross-domain problem with domain discrepancy caused by spatio-temporal variations. To reduce the discrepancy, we propose Self-Supervised Temporal Domain Adaptation (SSTDA), which contains two self-supervised auxiliary tasks (binary and sequential domain prediction) to jointly align cross-domain feature spaces embedded with local and global temporal dynamics, achieving better performance than other Domain Adaptation (DA) approaches. On three challenging benchmark datasets (GTEA, 50Salads, and Breakfast), SSTDA outperforms the current state-of-the-art method by large margins (e.g. for the F1@25 score, from 59.6% to 69.1% on Breakfast, from 73.4% to 81.5% on 50Salads, and from 83.6% to 89.1% on GTEA), and requires only 65% of the labeled training data for comparable performance, demonstrating the usefulness of adapting to unlabeled target videos across variations. The source code is available at https://github.com/cmhungsteve/SSTDA.

</details>

### SG-NN: Sparse Generative Neural Networks for Self-Supervised Scene Completion of RGB-D Scans. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Dai_SG-NN_Sparse_Generative_Neural_Networks_for_Self-Supervised_Scene_Completion_of_CVPR_2020_paper.html) · 📚 被引 122
- **作者**: Angela Dai, Christian Diller, Matthias Nießner
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对RGB-D扫描的场景补全问题，传统方法依赖大量标注的3D数据，成本高昂。②提出稀疏生成神经网络（SG-NN），利用自监督学习从单次扫描中预测缺失区域，通过稀疏卷积和生成模型处理不完整输入。③相比监督方法，SG-NN无需完整标注，利用扫描数据的内在结构进行训练，提高了泛化能力。④在合成和真实数据集上（如ScanNet）展示了有效的补全结果，但摘要中未提供具体数值。
- **摘要（英）**: This paper addresses scene completion from RGB-D scans using a sparse generative neural network (SG-NN) trained in a self-supervised manner, avoiding the need for dense annotations. It leverages sparse convolutions and generative modeling to predict missing regions, showing effective results on datasets like ScanNet.
- **核心贡献**: 提出自监督稀疏生成网络用于RGB-D场景补全。
- **创新点**: 结合稀疏卷积与生成模型，实现无标注训练。
- **结果**: 在ScanNet等数据集上验证了有效性。

### Self-Supervised Deep Visual Odometry With Online Adaptation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2005.06136](https://arxiv.org/abs/2005.06136) · 📚 被引 64
- **作者**: Shunkai Li, Xin Wang, Yingdian Cao, Fei Xue, Zike Yan, Hongbin Zha
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督视觉里程计在场景变化时性能下降的问题。②提出在线元学习算法，利用convLSTM聚合时空信息，使网络能持续适应新环境，并通过在线特征对齐方法处理环境变化。③相比现有方法，该网络能无缝适应不同环境，如虚拟到真实、室外到室内。④在未见过的室外场景、虚拟到真实和室外到室内等实验中，方法一致优于最先进的自监督VO方法。
- **摘要（英）**: This paper addresses the performance degradation of self-supervised visual odometry in novel scenes by proposing an online meta-learning algorithm with convLSTM for spatial-temporal aggregation and online feature alignment. The network adapts to new environments seamlessly, and experiments on unseen outdoor, virtual-to-real, and outdoor-to-indoor scenes show consistent improvements over state-of-the-art methods.
- **核心贡献**: 提出在线元学习算法，使自监督VO网络能持续适应新环境。
- **创新点**: 结合convLSTM和在线特征对齐，实现环境自适应。
- **结果**: 在多种场景迁移实验中优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised VO methods have shown great success in jointly estimating camera pose and depth from videos. However, like most data-driven methods, existing VO networks suffer from a notable decrease in performance when confronted with scenes different from the training data, which makes them unsuitable for practical applications. In this paper, we propose an online meta-learning algorithm to enable VO networks to continuously adapt to new environments in a self-supervised manner. The proposed method utilizes convolutional long short-term memory (convLSTM) to aggregate rich spatial-temporal information in the past. The network is able to memorize and learn from its past experience for better estimation and fast adaptation to the current frame. When running VO in the open world, in order to deal with the changing environment, we propose an online feature alignment method by aligning feature distributions at different time. Our VO network is able to seamlessly adapt to different environments. Extensive experiments on unseen outdoor scenes, virtual to real world and outdoor to indoor environments demonstrate that our method consistently outperforms state-of-the-art self-supervised VO baselines considerably.

</details>

### Sketch-BERT: Learning Sketch Bidirectional Encoder Representation From Transformers by Self-Supervised Learning of Sketch Gestalt. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2005.09159](https://arxiv.org/abs/2005.09159) · 📚 被引 57
- **作者**: Hangyu Lin, Yanwei Fu, Xiangyang Xue, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对草图理解中像素格式表示和CNN模型的局限性，以及SketchRNN表示仅适用于生成任务的问题。②提出Sketch-BERT模型，将BERT泛化到草图领域，包括新设计的草图嵌入网络和自监督的草图格式塔学习。③通过草图格式塔模型（SGM）辅助预训练，提升草图表示在下游任务中的性能。④实验表明，Sketch-BERT学习到的表示能改善草图识别和检索等下游任务的性能。
- **摘要（英）**: This paper addresses the limitations of pixel-based sketch understanding and the generative-only representation of SketchRNN by proposing Sketch-BERT, which adapts BERT to sketches with novel embedding networks and self-supervised sketch gestalt learning. The Sketch Gestalt Model aids pre-training, and experiments show improved performance on downstream tasks like recognition and retrieval.
- **核心贡献**: 提出Sketch-BERT模型，实现草图的双向编码器表示学习。
- **创新点**: 将BERT架构和自监督格式塔学习引入草图理解。
- **结果**: 在草图识别和检索任务上提升了性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous researches of sketches often considered sketches in pixel format and leveraged CNN based models in the sketch understanding. Fundamentally, a sketch is stored as a sequence of data points, a vector format representation, rather than the photo-realistic image of pixels. SketchRNN studied a generative neural representation for sketches of vector format by Long Short Term Memory networks (LSTM). Unfortunately, the representation learned by SketchRNN is primarily for the generation tasks, rather than the other tasks of recognition and retrieval of sketches. To this end and inspired by the recent BERT model, we present a model of learning Sketch Bidirectional Encoder Representation from Transformer (Sketch-BERT). We generalize BERT to sketch domain, with the novel proposed components and pre-training algorithms, including the newly designed sketch embedding networks, and the self-supervised learning of sketch gestalt. Particularly, towards the pre-training task, we present a novel Sketch Gestalt Model (SGM) to help train the Sketch-BERT. Experimentally, we show that the learned representation of Sketch-BERT can help and improve the performance of the downstream tasks of sketch recognition, sketch retrieval, and sketch gestalt.

</details>

### Flow2Stereo: Effective Self-Supervised Learning of Optical Flow and Stereo Matching. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_Flow2Stereo_Effective_Self-Supervised_Learning_of_Optical_Flow_and_Stereo_Matching_CVPR_2020_paper.html) · 📚 被引 60
- **作者**: Pengpeng Liu, Irwin King, Michael R. Lyu, Jia Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对光流和立体匹配的自监督学习效率问题。②提出Flow2Stereo方法，通过有效结合光流和立体匹配的自监督学习，利用几何一致性约束。③相比单独学习，该方法能共享特征和互补信息，提升学习效率。④摘要未提供具体数据，但预期在光流和立体匹配基准上表现优异。
- **摘要（英）**: This paper addresses the efficiency of self-supervised learning for optical flow and stereo matching by proposing Flow2Stereo, which combines both tasks with geometric consistency constraints. It shares features and complementary information to improve learning efficiency, though specific results are not detailed in the abstract.
- **核心贡献**: 提出Flow2Stereo方法，联合自监督学习光流和立体匹配。
- **创新点**: 利用几何一致性约束实现任务间的互补学习。
- **结果**: 预期在相关基准上提升性能。

### Self-Supervised Learning of Video-Induced Visual Invariances.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Tschannen_Self-Supervised_Learning_of_Video-Induced_Visual_Invariances_CVPR_2020_paper.html) · 📚 被引 34
- **作者**: Michael Tschannen, Josip Djolonga, Marvin Ritter, Aravindh Mahendran, Neil Houlsby, Sylvain Gelly et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Improving Object Detection with Selective Self-supervised Self-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58526-6_35)
- **作者**: Yandong Li, Di Huang, Danfeng Qin, Liqiang Wang, Boqing Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Adversarial Self-supervised Learning for Semi-supervised 3D Action Recognition.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58571-6_3)
- **作者**: Chenyang Si, Xuecheng Nie, Wei Wang, Liang Wang, Tieniu Tan, Jiashi Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Self-Supervised Learning of Appliance Usage.
- **链接**: [出版页](https://openreview.net/forum?id=B1lJzyStvS)
- **作者**: Chen-Yu Hsu, Abbas Zeitoun, Guang-He Lee, Dina Katabi, Tommi S. Jaakkola
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### vq-wav2vec: Self-Supervised Learning of Discrete Speech Representations.
- **链接**: [出版页](https://openreview.net/forum?id=rylwJxrYDS)
- **作者**: Alexei Baevski, Steffen Schneider, Michael Auli
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### From Inference to Generation: End-to-end Fully Self-supervised Generation of Human Face from Speech.
- **链接**: [出版页](https://openreview.net/forum?id=H1guaREYPr)
- **作者**: Hyeong-Seok Choi, Changdae Park, Kyogu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### Semantically-Guided Representation Learning for Self-Supervised Monocular Depth.
- **链接**: [出版页](https://openreview.net/forum?id=ByxT7TNFvH)
- **作者**: Vitor Guizilini, Rui Hou, Jie Li, Rares Ambrus, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### ALBERT: A Lite BERT for Self-supervised Learning of Language Representations.
- **链接**: [出版页](https://openreview.net/forum?id=H1eA7AEtvS)
- **作者**: Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### InfoGAN-CR and ModelCentrality: Self-supervised Model Training and Selection for Disentangling GANs.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lin20e.html)
- **作者**: Zinan Lin, Kiran Koshy Thekumparampil, Giulia Fanti, Sewoong Oh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Self-supervised Label Augmentation via Input Transformations.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lee20c.html)
- **作者**: Hankook Lee, Sung Ju Hwang, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Learning Compound Tasks without Task-specific Knowledge via Imitation and Self-supervised Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lee20f.html)
- **作者**: Sang-Hyun Lee, Seung-Woo Seo
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Automatic Shortcut Removal for Self-Supervised Representation Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v119/minderer20a.html)
- **作者**: Matthias Minderer, Olivier Bachem, Neil Houlsby, Michael Tschannen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Skew-Fit: State-Covering Self-Supervised Reinforcement Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v119/pong20a.html)
- **作者**: Vitchyr Pong, Murtaza Dalal, Steven Lin, Ashvin Nair, Shikhar Bahl, Sergey Levine
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Graph-based, Self-Supervised Program Repair from Diagnostic Feedback.
- **链接**: [出版页](http://proceedings.mlr.press/v119/yasunaga20a.html)
- **作者**: Michihiro Yasunaga, Percy Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### A Simple Framework for Contrastive Learning of Visual Representations.
- **链接**: [出版页](http://proceedings.mlr.press/v119/chen20j.html)
- **作者**: Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey E. Hinton
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### On Contrastive Learning for Likelihood-free Inference.
- **链接**: [出版页](http://proceedings.mlr.press/v119/durkan20a.html)
- **作者**: Conor Durkan, Iain Murray, George Papamakarios
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Self-Supervised Few-Shot Learning on Point Clouds.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/50c1f44e426560f3f2cdcb3e19e39903-Abstract.html)
- **作者**: Charu Sharma, Manohar Kaul
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

## 跨领域论文（完整笔记在其他领域）

- 3D Packing for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Exploit Clues From Views: Self-Supervised and Regularized Learning for Multiview Object Recognition. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- On the Uncertainty of Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Multi-Modal Domain Adaptation for Fine-Grained Action Recognition. → [multimodal](../multimodal/Guideline%202020.md)
- Monocular Differentiable Rendering for Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Forget About the LiDAR: Self-Supervised Depth Estimators with MED Probability Volumes. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
<!-- COMPLETE v1 papers=56 -->
