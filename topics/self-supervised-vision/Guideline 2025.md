# Self-supervised Vision — 2025 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 50 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Temporal Overlapping Prediction: A Self-Supervised Pre-Training Method for LiDAR Moving Object Segmentation.
- **链接**: [arXiv:2503.07167](https://arxiv.org/abs/2503.07167) · 📚 被引 1
- **作者**: Ziliang Miao, Runjian Chen, Yixi Cai, Buwei He, Wenquan Zhao, Wenqi Shao et al.
- **🏷️ 机构**: The University of Hong Kong, KTH Royal Institute of Technology, Southern University of Science and Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Moving object segmentation (MOS) on LiDAR point clouds is crucial for autonomous systems like self-driving vehicles. Previous supervised approaches rely heavily on costly manual annotations, while LiDAR sequences naturally capture temporal motion cues that can be leveraged for self-supervised learning. In this paper, we propose Temporal Overlapping Prediction (TOP), a self-supervised pre-training method that alleviate the labeling burden for MOS. TOP explores the temporal overlapping points that commonly observed by current and adjacent scans, and learns spatiotemporal representations by predicting the occupancy states of temporal overlapping points. Moreover, we utilize current occupancy reconstruction as an auxiliary pre-training objective, which enhances the current structural awareness of the model. We conduct extensive experiments and observe that the conventional metric Intersection-over-Union (IoU) shows strong bias to objects with more scanned points, which might neglect small or distant objects. To compensate for this bias, we introduce an additional metric called mIoU_obj to evaluate object-level performance. Experiments on nuScenes and SemanticKITTI show that TOPoutperforms both supervised training-from-scratch baseline and other self-supervised pre-training baselines by up to 28.77% relative improvement, demonstrating strong transferability across LiDAR setups and generalization to other tasks. Code and pre-trained models will be publicly available upon publication.

</details>

### ASCENT: Annotation-Free Self-Supervised Contrastive Embeddings for 3D Neuron Tracking in Fluorescence Microscopy.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01362) · 📚 被引 1
- **作者**: Haejun Han, Hang Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Boosting Generative Adversarial Transferability with Self-Supervised Vision Transformer Features.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00057)
- **作者**: Shangbo Wu, Yu-an Tan, Ruinan Ma, Wencong Ma, Dehua Zhu, Yuanzhang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Joint Self-Supervised Video Alignment and Action Segmentation.
- **链接**: [arXiv:2503.16832](https://arxiv.org/abs/2503.16832) · 📚 被引 3
- **作者**: Ali Shah Ali, Syed Ahmed Mahmood, Mubin Saeed, Andrey Konin, M. Zeeshan Zia, Quoc-Huy Tran
- **🏷️ 机构**: Retrocausal, Inc.,Redmond,WA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel approach for simultaneous self-supervised video alignment and action segmentation based on a unified optimal transport framework. In particular, we first tackle self-supervised video alignment by developing a fused Gromov-Wasserstein optimal transport formulation with a structural prior, which trains efficiently on GPUs and needs only a few iterations for solving the optimal transport problem. Our single-task method achieves the state-of-the-art performance on multiple video alignment benchmarks and outperforms VAVA, which relies on a traditional Kantorovich optimal transport formulation with an optimality prior. Furthermore, we extend our approach by proposing a unified optimal transport framework for joint self-supervised video alignment and action segmentation, which requires training and storing a single model and saves both time and memory consumption as compared to two different single-task models. Extensive evaluations on several video alignment and action segmentation datasets demonstrate that our multi-task method achieves comparable video alignment yet superior action segmentation results over previous methods in video alignment and action segmentation respectively. Finally, to the best of our knowledge, this is the first work to unify video alignment and action segmentation into a single model. Our code is available on our research website: https://retrocausal.ai/research/.

</details>

### AIM: Amending Inherent Interpretability via Self-Supervised Masking.
- **链接**: [arXiv:2508.11502](https://arxiv.org/abs/2508.11502) · 📚 被引 0
- **作者**: Eyad Alshami, Shashank Agnihotri, Bernt Schiele, Margret Keuper
- **🏷️ 机构**: Max-Planck-Institute for Informatics, Saarland Informatics Campus,Germany, Data and Web Science Group, University of Mannheim,Germany
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It has been observed that deep neural networks (DNNs) often use both genuine as well as spurious features. In this work, we propose "Amending Inherent Interpretability via Self-Supervised Masking" (AIM), a simple yet interestingly effective method that promotes the network's utilization of genuine features over spurious alternatives without requiring additional annotations. In particular, AIM uses features at multiple encoding stages to guide a self-supervised, sample-specific feature-masking process. As a result, AIM enables the training of well-performing and inherently interpretable models that faithfully summarize the decision process. We validate AIM across a diverse range of challenging datasets that test both out-of-distribution generalization and fine-grained visual understanding. These include general-purpose classification benchmarks such as ImageNet100, HardImageNet, and ImageWoof, as well as fine-grained classification datasets such as Waterbirds, TravelingBirds, and CUB-200. AIM demonstrates significant dual benefits: interpretability improvements, as measured by the Energy Pointing Game (EPG) score, and accuracy gains over strong baselines. These consistent gains across domains and architectures provide compelling evidence that AIM promotes the use of genuine and meaningful features that directly contribute to improved generalization and human-aligned interpretability.

</details>

### Progressor: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement.
- **链接**: [arXiv:2411.17764](https://arxiv.org/abs/2411.17764) · 📚 被引 0
- **作者**: Tewodros W. Ayalew, Xiao Zhang, Kevin Yuanbo Wu, Tianchong Jiang, Michael Maire, Matthew R. Walter
- **🏷️ 机构**: University of Chicago,USA, Toyota Technological Institute at Chicago,USA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present PROGRESSOR, a novel framework that learns a task-agnostic reward function from videos, enabling policy training through goal-conditioned reinforcement learning (RL) without manual supervision. Underlying this reward is an estimate of the distribution over task progress as a function of the current, initial, and goal observations that is learned in a self-supervised fashion. Crucially, PROGRESSOR refines rewards adversarially during online RL training by pushing back predictions for out-of-distribution observations, to mitigate distribution shift inherent in non-expert observations. Utilizing this progress prediction as a dense reward together with an adversarial push-back, we show that PROGRESSOR enables robots to learn complex behaviors without any external supervision. Pretrained on large-scale egocentric human video from EPIC-KITCHENS, PROGRESSOR requires no fine-tuning on in-domain task-specific data for generalization to real-robot offline RL under noisy demonstrations, outperforming contemporary methods that provide dense visual reward for robotic learning. Our findings highlight the potential of PROGRESSOR for scalable robotic applications where direct action labels and task-specific rewards are not readily available.

</details>

### Adversarial Robustness of Discriminative Self-Supervised Learning in Vision.
- **链接**: [arXiv:2503.06361](https://arxiv.org/abs/2503.06361) · 📚 被引 0
- **作者**: Ömer Veysel Çagatan, Ömer Faruk Tal, M. Emre Gürsoy
- **🏷️ 机构**: Ko&#x00E7; University,Department of Computer Engineering
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has advanced significantly in visual representation learning, yet comprehensive evaluations of its adversarial robustness remain limited. In this study, we evaluate the adversarial robustness of seven discriminative self-supervised models and one supervised model across diverse tasks, including ImageNet classification, transfer learning, segmentation, and detection. Our findings suggest that discriminative SSL models generally exhibit better robustness to adversarial attacks compared to their supervised counterpart on ImageNet, with this advantage extending to transfer learning when using linear evaluation. However, when fine-tuning is applied, the robustness gap between SSL and supervised models narrows considerably. Similarly, this robustness advantage diminishes in segmentation and detection tasks. We also investigate how various factors might influence adversarial robustness, including architectural choices, training duration, data augmentations, and batch sizes. Our analysis contributes to the ongoing exploration of adversarial robustness in visual self-supervised representation systems.

</details>

### Backdooring Self-Supervised Contrastive Learning by Noisy Alignment.
- **链接**: [arXiv:2508.14015](https://arxiv.org/abs/2508.14015) · [代码](https://github.com/jsrdcht/Noisy-Alignment) · 📚 被引 1
- **作者**: Tuo Chen, Jie Gui, Minjing Dong, Ju Jia, Lanting Fang, Jian Liu
- **🏷️ 机构**: Southeast University, City University of Hong Kong, Beijing Institute of Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised contrastive learning (CL) effectively learns transferable representations from unlabeled data containing images or image-text pairs but suffers vulnerability to data poisoning backdoor attacks (DPCLs). An adversary can inject poisoned images into pretraining datasets, causing compromised CL encoders to exhibit targeted misbehavior in downstream tasks. Existing DPCLs, however, achieve limited efficacy due to their dependence on fragile implicit co-occurrence between backdoor and target object and inadequate suppression of discriminative features in backdoored images. We propose Noisy Alignment (NA), a DPCL method that explicitly suppresses noise components in poisoned images. Inspired by powerful training-controllable CL attacks, we identify and extract the critical objective of noisy alignment, adapting it effectively into data-poisoning scenarios. Our method implements noisy alignment by strategically manipulating contrastive learning's random cropping mechanism, formulating this process as an image layout optimization problem with theoretically derived optimal parameters. The resulting method is simple yet effective, achieving state-of-the-art performance compared to existing DPCLs, while maintaining clean-data accuracy. Furthermore, Noisy Alignment demonstrates robustness against common backdoor defenses. Codes can be found at https://github.com/jsrdcht/Noisy-Alignment.

</details>

### DASH: 4D Hash Encoding with Self-Supervised Decomposition for Real-Time Dynamic Scene Rendering.
- **链接**: [arXiv:2507.19141](https://arxiv.org/abs/2507.19141) · [代码](https://github.com/chenj02/DASH) · 📚 被引 0
- **作者**: Jie Chen, Zhangchi Hu, Peixi Wu, Huyue Zhu, Hebei Li, Xiaoyan Sun
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dynamic scene reconstruction is a long-term challenge in 3D vision. Existing plane-based methods in dynamic Gaussian splatting suffer from an unsuitable low-rank assumption, causing feature overlap and poor rendering quality. Although 4D hash encoding provides an explicit representation without low-rank constraints, directly applying it to the entire dynamic scene leads to substantial hash collisions and redundancy. To address these challenges, we present DASH, a real-time dynamic scene rendering framework that employs 4D hash encoding coupled with self-supervised decomposition. Our approach begins with a self-supervised decomposition mechanism that separates dynamic and static components without manual annotations or precomputed masks. Next, we introduce a multiresolution 4D hash encoder for dynamic elements, providing an explicit representation that avoids the low-rank assumption. Finally, we present a spatio-temporal smoothness regularization strategy to mitigate unstable deformation artifacts. Experiments on real-world datasets demonstrate that DASH achieves state-of-the-art dynamic rendering performance, exhibiting enhanced visual quality at real-time speeds of 264 FPS on a single 4090 GPU. Code: https://github.com/chenj02/DASH.

</details>

### SAMora: Enhancing SAM through Hierarchical Self-Supervised Pre-Training for Medical Images.
- **链接**: [arXiv:2511.08626](https://arxiv.org/abs/2511.08626) · [代码](https://github.com/ShChen233/SAMora) · 📚 被引 1
- **作者**: Shuhang Chen, Hangjie Yuan, Pengwei Liu, Hanxue Gu, Tao Feng, Dong Ni
- **🏷️ 机构**: Zhejiang University, Duke University, Tsinghua University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Segment Anything Model (SAM) has demonstrated significant potential in medical image segmentation. Yet, its performance is limited when only a small amount of labeled data is available, while there is abundant valuable yet often overlooked hierarchical information in medical data. To address this limitation, we draw inspiration from self-supervised learning and propose SAMora, an innovative framework that captures hierarchical medical knowledge by applying complementary self-supervised learning objectives at the image, patch, and pixel levels. To fully exploit the complementarity of hierarchical knowledge within LoRAs, we introduce HL-Attn, a hierarchical fusion module that integrates multi-scale features while maintaining their distinct characteristics. SAMora is compatible with various SAM variants, including SAM2, SAMed, and H-SAM. Experimental results on the Synapse, LA, and PROMISE12 datasets demonstrate that SAMora outperforms existing SAM variants. It achieves state-of-the-art performance in both few-shot and fully supervised settings while reducing fine-tuning epochs by 90%. The code is available at https://github.com/ShChen233/SAMora.

</details>

### Harnessing Text-to-Image Diffusion Models for Point Cloud Self-Supervised Learning.
- **链接**: [arXiv:2507.09102](https://arxiv.org/abs/2507.09102) · [代码](https://github.com/wdttt/PointSD) · 📚 被引 0
- **作者**: Yiyang Chen, Shanshan Zhao, Lunhao Duan, Changxing Ding, Dacheng Tao
- **🏷️ 机构**: South China University of Technology, Alibaba International Digital Commerce Group, Nanyang Technological University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion-based models, widely used in text-to-image generation, have proven effective in 2D representation learning. Recently, this framework has been extended to 3D self-supervised learning by constructing a conditional point generator for enhancing 3D representations. However, its performance remains constrained by the 3D diffusion model, which is trained on the available 3D datasets with limited size. We hypothesize that the robust capabilities of text-to-image diffusion models, particularly Stable Diffusion (SD), which is trained on large-scale datasets, can help overcome these limitations. To investigate this hypothesis, we propose PointSD, a framework that leverages the SD model for 3D self-supervised learning. By replacing the SD model's text encoder with a 3D encoder, we train a point-to-image diffusion model that allows point clouds to guide the denoising of rendered noisy images. With the trained point-to-image diffusion model, we use noise-free images as the input and point clouds as the condition to extract SD features. Next, we train a 3D backbone by aligning its features with these SD features, thereby facilitating direct semantic learning. Comprehensive experiments on downstream point cloud tasks and ablation studies demonstrate that the SD model can enhance point cloud self-supervised learning. Code is publicly available at https://github.com/wdttt/PointSD.

</details>

### USP: Unified Self-Supervised Pretraining for Image Generation and Understanding.
- **链接**: [arXiv:2503.06132](https://arxiv.org/abs/2503.06132) · [代码](https://github.com/AMAP-ML/USP) · 📚 被引 3
- **作者**: Xiangxiang Chu, Renda Li, Yong Wang
- **🏷️ 机构**: AMAP, Alibaba Group
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have highlighted the interplay between diffusion models and representation learning. Intermediate representations from diffusion models can be leveraged for downstream visual tasks, while self-supervised vision models can enhance the convergence and generation quality of diffusion models. However, transferring pretrained weights from vision models to diffusion models is challenging due to input mismatches and the use of latent spaces. To address these challenges, we propose Unified Self-supervised Pretraining (USP), a framework that initializes diffusion models via masked latent modeling in a Variational Autoencoder (VAE) latent space. USP achieves comparable performance in understanding tasks while significantly improving the convergence speed and generation quality of diffusion models. Our code will be publicly available at https://github.com/AMAP-ML/USP.

</details>

### Embodied Image Captioning: Self-Supervised Learning Agents for Spatially Coherent Image Descriptions.
- **链接**: [arXiv:2504.08531](https://arxiv.org/abs/2504.08531) · 📚 被引 0
- **作者**: Tommaso Galliena, Tommaso Apicella, Stefano Rosa, Pietro Morerio, Alessio Del Bue, Lorenzo Natale
- **🏷️ 机构**: Istituto Italiano di Tecnologia,Genoa,Italy
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a self-supervised method to improve an agent's abilities in describing arbitrary objects while actively exploring a generic environment. This is a challenging problem, as current models struggle to obtain coherent image captions due to different camera viewpoints and clutter. We propose a three-phase framework to fine-tune existing captioning models that enhances caption accuracy and consistency across views via a consensus mechanism. First, an agent explores the environment, collecting noisy image-caption pairs. Then, a consistent pseudo-caption for each object instance is distilled via consensus using a large language model. Finally, these pseudo-captions are used to fine-tune an off-the-shelf captioning model, with the addition of contrastive learning. We analyse the performance of the combination of captioning models, exploration policies, pseudo-labeling methods, and fine-tuning strategies, on our manually labeled test set. Results show that a policy can be trained to mine samples with higher disagreement compared to classical baselines. Our pseudo-captioning method, in combination with all policies, has a higher semantic similarity compared to other existing methods, and fine-tuning improves caption accuracy and consistency by a significant margin. Code and test set annotations available at https://hsp-iit.github.io/embodied-captioning/

</details>

### Self-Supervised Learning of Hybrid Part-Aware 3D Representations of 2D Gaussians and Superquadrics.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00900) · 📚 被引 4
- **作者**: Zhirui Gao, Renjiao Yi, Yuhang Huang, Wei Chen, Chenyang Zhu, Kai Xu
- **🏷️ 机构**: National University of Defense Technology
- **会议**: ICCV 2025

### No Pose at All: Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views.
- **链接**: [arXiv:2508.01171](https://arxiv.org/abs/2508.01171) · 📚 被引 3
- **作者**: Ranran Huang, Krystian Mikolajczyk
- **🏷️ 机构**: Imperial College London
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce SPFSplat, an efficient framework for 3D Gaussian splatting from sparse multi-view images, requiring no ground-truth poses during training or inference. It employs a shared feature extraction backbone, enabling simultaneous prediction of 3D Gaussian primitives and camera poses in a canonical space from unposed inputs within a single feed-forward step. Alongside the rendering loss based on estimated novel-view poses, a reprojection loss is integrated to enforce the learning of pixel-aligned Gaussian primitives for enhanced geometric constraints. This pose-free training paradigm and efficient one-step feed-forward design make SPFSplat well-suited for practical applications. Remarkably, despite the absence of pose supervision, SPFSplat achieves state-of-the-art performance in novel view synthesis even under significant viewpoint changes and limited image overlap. It also surpasses recent methods trained with geometry priors in relative pose estimation. Code and trained models are available on our project page: https://ranrhuang.github.io/spfsplat/.

</details>

### Rayzer: a Self-Supervised Large View Synthesis Model.
- **链接**: [arXiv:2505.00702](https://arxiv.org/abs/2505.00702) · 📚 被引 4
- **作者**: Hanwen Jiang, Hao Tan, Peng Wang, Hai Jin, Yue Zhao, Sai Bi et al.
- **🏷️ 机构**: The University of Texas at Austin, Adobe Research, Cornell University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present RayZer, a self-supervised multi-view 3D Vision model trained without any 3D supervision, i.e., camera poses and scene geometry, while exhibiting emerging 3D awareness. Concretely, RayZer takes unposed and uncalibrated images as input, recovers camera parameters, reconstructs a scene representation, and synthesizes novel views. During training, RayZer relies solely on its self-predicted camera poses to render target views, eliminating the need for any ground-truth camera annotations and allowing RayZer to be trained with 2D image supervision. The emerging 3D awareness of RayZer is attributed to two key factors. First, we design a self-supervised framework, which achieves 3D-aware auto-encoding of input images by disentangling camera and scene representations. Second, we design a transformer-based model in which the only 3D prior is the ray structure, connecting camera, pixel, and scene simultaneously. RayZer demonstrates comparable or even superior novel view synthesis performance than ``oracle'' methods that rely on pose annotations in both training and testing. Project: https://hwjiang1510.github.io/RayZer/

</details>

### Blind2Sound: Self-Supervised Image Denoising Without Residual Noise.
- **链接**: [arXiv:2303.05183](https://arxiv.org/abs/2303.05183) · 📚 被引 0
- **作者**: Jiazheng Liu, Zejin Wang, Bohao Chen, Hua Han
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Brain Cognition and Brain-inspired Intelligence Technology,Beijing,China, School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised blind denoising for Poisson-Gaussian noise remains a challenging task. Pseudo-supervised pairs constructed from single noisy images re-corrupt the signal and degrade the performance. The visible blindspots solve the information loss in masked inputs. However, without explicitly noise sensing, mean square error as an objective function cannot adjust denoising intensities for dynamic noise levels, leading to noticeable residual noise. In this paper, we propose Blind2Sound, a simple yet effective approach to overcome residual noise in denoised images. The proposed adaptive re-visible loss senses noise levels and performs personalized denoising without noise residues while retaining the signal lossless. The theoretical analysis of intermediate medium gradients guarantees stable training, while the Cramer Gaussian loss acts as a regularization to facilitate the accurate perception of noise levels and improve the performance of the denoiser. Experiments on synthetic and real-world datasets show the superior performance of our method, especially for single-channel images.

</details>

### CoSMIC: Continual Self-Supervised Learning for Multi-Domain Medical Imaging Via Conditional Mutual Information Maximization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02140) · 📚 被引 0
- **作者**: Yihang Liu, Ying Wen, Longzhen Yang, Lianghua He, Heng Tao Shen
- **🏷️ 机构**: Tongji University, East China Normal University
- **会议**: ICCV 2025

### TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras.
- **链接**: [arXiv:2508.00913](https://arxiv.org/abs/2508.00913) · 📚 被引 1
- **作者**: Mohammad Mohammadi, Ziyi Wu, Igor Gilitschenski
- **🏷️ 机构**: University of Toronto
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-term temporal information is crucial for event-based perception tasks, as raw events only encode pixel brightness changes. Recent works show that when trained from scratch, recurrent models achieve better results than feedforward models in these tasks. However, when leveraging self-supervised pre-trained weights, feedforward models can outperform their recurrent counterparts. Current self-supervised learning (SSL) methods for event-based pre-training largely mimic RGB image-based approaches. They pre-train feedforward models on raw events within a short time interval, ignoring the temporal information of events. In this work, we introduce TESPEC, a self-supervised pre-training framework tailored for learning spatio-temporal information. TESPEC is well-suited for recurrent models, as it is the first framework to leverage long event sequences during pre-training. TESPEC employs the masked image modeling paradigm with a new reconstruction target. We design a novel method to accumulate events into pseudo grayscale videos containing high-level semantic information about the underlying scene, which is robust to sensor noise and reduces motion blur. Reconstructing this target thus requires the model to reason about long-term history of events. Extensive experiments demonstrate our state-of-the-art results in downstream tasks, including object detection, semantic segmentation, and monocular depth estimation. Project webpage: https://mhdmohammadi.github.io/TESPEC_webpage.

</details>

### Self-Supervised Sparse Sensor Fusion for Long Range Perception.
- **链接**: [arXiv:2508.13995](https://arxiv.org/abs/2508.13995) · 📚 被引 2
- **作者**: Edoardo Palladin, Samuel Brucker, Filippo Ghilotti, Praveen Narayanan, Mario Bijelic, Felix Heide
- **🏷️ 机构**: Torc Robotics
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Outside of urban hubs, autonomous cars and trucks have to master driving on intercity highways. Safe, long-distance highway travel at speeds exceeding 100 km/h demands perception distances of at least 250 m, which is about five times the 50-100m typically addressed in city driving, to allow sufficient planning and braking margins. Increasing the perception ranges also allows to extend autonomy from light two-ton passenger vehicles to large-scale forty-ton trucks, which need a longer planning horizon due to their high inertia. However, most existing perception approaches focus on shorter ranges and rely on Bird's Eye View (BEV) representations, which incur quadratic increases in memory and compute costs as distance grows. To overcome this limitation, we built on top of a sparse representation and introduced an efficient 3D encoding of multi-modal and temporal features, along with a novel self-supervised pre-training scheme that enables large-scale learning from unlabeled camera-LiDAR data. Our approach extends perception distances to 250 meters and achieves an 26.6% improvement in mAP in object detection and a decrease of 30.5% in Chamfer Distance in LiDAR forecasting compared to existing methods, reaching distances up to 250 meters. Project Page: https://light.princeton.edu/lrs4fusion/

</details>

### Structure-Aware Semantic Discrepancy and Consistency for 3D Medical Image Self-Supervised Learning.
- **链接**: [arXiv:2507.02581](https://arxiv.org/abs/2507.02581) · 📚 被引 3
- **作者**: Tan Pan, Zhaorui Tan, Kaiyu Guo, Dongli Xu, Weidi Xu, Chen Jiang et al.
- **🏷️ 机构**: AI3, Fudan University, Shanghai Academy of Artificial Intelligence for Science, The University of Queensland
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D medical image self-supervised learning (mSSL) holds great promise for medical analysis. Effectively supporting broader applications requires considering anatomical structure variations in location, scale, and morphology, which are crucial for capturing meaningful distinctions. However, previous mSSL methods partition images with fixed-size patches, often ignoring the structure variations. In this work, we introduce a novel perspective on 3D medical images with the goal of learning structure-aware representations. We assume that patches within the same structure share the same semantics (semantic consistency) while those from different structures exhibit distinct semantics (semantic discrepancy). Based on this assumption, we propose an mSSL framework named $S^2DC$, achieving Structure-aware Semantic Discrepancy and Consistency in two steps. First, $S^2DC$ enforces distinct representations for different patches to increase semantic discrepancy by leveraging an optimal transport strategy. Second, $S^2DC$ advances semantic consistency at the structural level based on neighborhood similarity distribution. By bridging patch-level and structure-level representations, $S^2DC$ achieves structure-aware representations. Thoroughly evaluated across 10 datasets, 4 tasks, and 3 modalities, our proposed method consistently outperforms the state-of-the-art methods in mSSL.

</details>

### Mosic: Optimal-Transport Motion Trajectory for Dense Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00617) · 📚 被引 0
- **作者**: Mohammadreza Salehi, Shashanka Venkataramanan, Ioana Simion, Efstratios Gavves, Cees G. M. Snoek, Yuki M. Asano
- **🏷️ 机构**: VIS Lab, UvA, Valeo.ai, Fundamental AI Lab, UTN
- **会议**: ICCV 2025

### SHeaP: Self-Supervised Head Geometry Predictor Learned via 2D Gaussians.
- **链接**: [arXiv:2504.12292](https://arxiv.org/abs/2504.12292) · 📚 被引 3
- **作者**: Liam Schoneveld, Zhe Chen, Davide Davoli, Jiapeng Tang, Saimon Terazawa, Ko Nishino et al.
- **🏷️ 机构**: Woven by Toyota, Toyota Motor Europe NV/SA associated partner by contracted service, Technical University of Munich
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate, real-time 3D reconstruction of human heads from monocular images and videos underlies numerous visual applications. As 3D ground truth data is hard to come by at scale, previous methods have sought to learn from abundant 2D videos in a self-supervised manner. Typically, this involves the use of differentiable mesh rendering, which is effective but faces limitations. To improve on this, we propose SHeaP (Self-supervised Head Geometry Predictor Learned via 2D Gaussians). Given a source image, we predict a 3DMM mesh and a set of Gaussians that are rigged to this mesh. We then reanimate this rigged head avatar to match a target frame, and backpropagate photometric losses to both the 3DMM and Gaussian prediction networks. We find that using Gaussians for rendering substantially improves the effectiveness of this self-supervised approach. Training solely on 2D data, our method surpasses existing self-supervised approaches in geometric evaluations on the NoW benchmark for neutral faces and a new benchmark for non-neutral expressions. Our method also produces highly expressive meshes, outperforming state-of-the-art in emotion classification.

</details>

### Prototype-Based Contrastive Learning with Stage-Wise Progressive Augmentation for Self-Supervised Fine-Grained Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00393) · 📚 被引 2
- **作者**: Baofeng Tan, Xiu-Shen Wei, Lin Zhao
- **🏷️ 机构**: School of Computer Science and Engineering, Nanjing University of Science and Technology, School of Computer Science and Engineering, Southeast University,Key Laboratory of New Generation Artificial Intelligence Technology and Its Interdisciplinary Applications
- **会议**: ICCV 2025

### An OpenMind for 3D Medical Vision Self-supervised Learning.
- **链接**: [arXiv:2412.17041](https://arxiv.org/abs/2412.17041) · 📚 被引 5
- **作者**: Tassilo Wald, Constantin Ulrich, Jonathan Suprijadi, Sebastian Ziegler, Michal Nohel, Robin Peretzke et al.
- **🏷️ 机构**: German Cancer Research Center (DKFZ),Division of Medical Image Computing,Heidelberg,Germany, Brno University of Technology,Faculty of Electrical Engineering and Communication,Czech Republic
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of self-supervised learning (SSL) for 3D medical images lacks consistency and standardization. While many methods have been developed, it is impossible to identify the current state-of-the-art, due to i) varying and small pretraining datasets, ii) varying architectures, and iii) being evaluated on differing downstream datasets. In this paper, we bring clarity to this field and lay the foundation for further method advancements through three key contributions: We a) publish the largest publicly available pre-training dataset comprising 114k 3D brain MRI volumes, enabling all practitioners to pre-train on a large-scale dataset. We b) benchmark existing 3D self-supervised learning methods on this dataset for a state-of-the-art CNN and Transformer architecture, clarifying the state of 3D SSL pre-training. Among many findings, we show that pre-trained methods can exceed a strong from-scratch nnU-Net ResEnc-L baseline. Lastly, we c) publish the code of our pre-training and fine-tuning frameworks and provide the pre-trained models created during the benchmarking process to facilitate rapid adoption and reproduction.

</details>

### S3E: Self-Supervised State Estimation for Radar-Inertial System.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02477)
- **作者**: Shengpeng Wang, Yulong Xie, Qing Liao, Wei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### StruMamba3D: Exploring Structural Mamba for Self-Supervised Point Cloud Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02651) · 📚 被引 2
- **作者**: Chuxin Wang, Yixin Zha, Wenfei Yang, Tianzhu Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2025

### SignRep: Enhancing Self-Supervised Sign Representations.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02117) · 📚 被引 0
- **作者**: Ryan Wong, Necati Cihan Camgöz, Richard Bowden
- **🏷️ 机构**: University of Surrey, Meta Reality Labs
- **会议**: ICCV 2025

### Self-Supervised Monocular 4D Scene Reconstruction for Egocentric Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00829) · 📚 被引 1
- **作者**: Chengbo Yuan, Geng Chen, Li Yi, Yang Gao
- **🏷️ 机构**: Institute for Interdisciplinary Information Sciences, Tsinghua University, Shanghai Qi Zhi Institute
- **会议**: ICCV 2025

### Towards More Diverse and Challenging Pre-Training for Point Cloud Learning: Self-Supervised Cross Reconstruction with Decoupled Views.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02665) · 📚 被引 3
- **作者**: Xiangdong Zhang, Shaofeng Zhang, Junchi Yan
- **🏷️ 机构**: School of AI, Shanghai Jiao Tong University
- **会议**: ICCV 2025

### CoraLSRT: Revisiting Coral Reef Semantic Segmentation by Feature Rectification via Self-Supervised Guidance.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01857) · 📚 被引 4
- **作者**: Ziqiang Zheng, Yuk-Kwan Wong, Binh-Son Hua, Jianbo Shi, Sai-Kit Yeung
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Trinity College Dublin, University of Pennsylvania
- **会议**: ICCV 2025

### Bi-Level Optimization for Self-Supervised AI-Generated Face Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01762) · 📚 被引 1
- **作者**: Mian Zou, Nan Zhong, Baosheng Yu, Yibing Zhan, Kede Ma
- **🏷️ 机构**: Jiangxi University of Finance and Economics, City University of Hong Kong, Nanyang Technological University
- **会议**: ICCV 2025

### Salvaging the Overlooked: Leveraging Class-Aware Contrastive Learning for Multi-Class Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01989) · 📚 被引 6
- **作者**: Lei Fan, Junjie Huang, Donglin Di, Anyang Su, Tianyou Song, Maurice Pagnucco et al.
- **🏷️ 机构**: UNSW,Sydney, DZ-Matrix, Columbia University
- **会议**: ICCV 2025

### Vector Contrastive Learning for Pixel-Wise Pretraining in Medical Vision.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01844) · 📚 被引 2
- **作者**: Yuting He, Shuo Li
- **🏷️ 机构**: Case Western Reserve University,Dept. of BME,Cleveland,US
- **会议**: ICCV 2025

### Robust Dataset Condensation using Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00274) · 📚 被引 0
- **作者**: Nicole Hee-Yeon Kim, Hwanjun Song
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST),Daejeon,Republic of Korea
- **会议**: ICCV 2025

### Selective Contrastive Learning for Weakly Supervised Affordance Grounding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00495) · 📚 被引 2
- **作者**: WonJun Moon, Hyun Seok Seong, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: ICCV 2025

### AMD: Adaptive Momentum and Decoupled Contrastive Learning Framework for Robust Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2507.01801](https://arxiv.org/abs/2507.01801) · 📚 被引 1
- **作者**: Bin Rao, Haicheng Liao, Yanchen Guan, Chengyue Wang, Bonan Wang, Jiaxun Zhang et al.
- **🏷️ 机构**: University of Macau,State Key Laboratory of Internet of Things for Smart City
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately predicting the future trajectories of traffic agents is essential in autonomous driving. However, due to the inherent imbalance in trajectory distributions, tail data in natural datasets often represents more complex and hazardous scenarios. Existing studies typically rely solely on a base model's prediction error, without considering the diversity and uncertainty of long-tail trajectory patterns. We propose an adaptive momentum and decoupled contrastive learning framework (AMD), which integrates unsupervised and supervised contrastive learning strategies. By leveraging an improved momentum contrast learning (MoCo-DT) and decoupled contrastive learning (DCL) module, our framework enhances the model's ability to recognize rare and complex trajectories. Additionally, we design four types of trajectory random augmentation methods and introduce an online iterative clustering strategy, allowing the model to dynamically update pseudo-labels and better adapt to the distributional shifts in long-tail data. We propose three different criteria to define long-tail trajectories and conduct extensive comparative experiments on the nuScenes and ETH$/$UCY datasets. The results show that AMD not only achieves optimal performance in long-tail trajectory prediction but also demonstrates outstanding overall prediction accuracy.

</details>

### DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-Based Human Action Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01278) · 📚 被引 1
- **作者**: Haitao Tian
- **🏷️ 机构**: University of Ottawa,Canada
- **会议**: ICCV 2025

### FIX-CLIP: Dual-Branch Hierarchical Contrastive Learning via Synthetic Captions for Better Understanding of Long Text.
- **链接**: [arXiv:2507.10095](https://arxiv.org/abs/2507.10095) · [代码](https://github.com/bcwang-sjtu/Fix-CLIP) · 📚 被引 4
- **作者**: Bingchao Wang, Zhiwei Ning, Jianyu Ding, Xuanang Gao, Yin Li, Dongsheng Jiang et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Huawei Inc.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> CLIP has shown promising performance across many short-text tasks in a zero-shot manner. However, limited by the input length of the text encoder, CLIP struggles on under-stream tasks with long-text inputs ($>77$ tokens). To remedy this issue, we propose FIX-CLIP, which includes three novel modules: (1) A dual-branch training pipeline that aligns short and long texts with masked and raw images, respectively, which boosts the long-text representation while preserving the short-text ability. (2) Multiple learnable regional prompts with unidirectional masks in Transformer layers for regional information extraction. (3) A hierarchical feature alignment module in the intermediate encoder layers to promote the consistency of multi-scale features. Furthermore, we collect 30M images and utilize existing MLLMs to synthesize long-text captions for training. Extensive experiments show that FIX-CLIP achieves state-of-the-art performance on both long-text and short-text retrieval benchmarks. For downstream applications, we reveal that FIX-CLIP's text encoder delivers promising performance in a plug-and-play manner for diffusion models with long-text input. The code is available at https://github.com/bcwang-sjtu/Fix-CLIP.

</details>

### Keep Your Friends Close, and Your Enemies Farther: Distance-Aware Voxel-Wise Contrastive Learning for Semi-Supervised Multi-Organ Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02027) · 📚 被引 0
- **作者**: Haochen Zhao, Jianwei Niu, Xuefeng Liu, Xiaozheng Xie, Li Kuang, Haotian Yang et al.
- **🏷️ 机构**: SCSE, Beihang University,State Key Laboratory of Virtual Reality Technology and Systems, School of Computer and Communication Engineering, University of Science and Technology Beijing, Hangzhou International Innovation Institute of Beihang University
- **会议**: ICCV 2025

### Harnessing Massive Satellite Imagery with Efficient Masked Image Modeling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00652) · 📚 被引 6
- **作者**: Fengxiang Wang, Hongzhen Wang, Di Wang, Zonghao Guo, Zhenyu Zhong, Long Lan et al.
- **🏷️ 机构**: College of Computer Science and Technology, National University of Defense Technology, Xiaomi Corp., School of Computer Science, Wuhan University
- **会议**: ICCV 2025

### Beyond [cls]: Exploring the True Potential of Masked Image Modeling Representations.
- **链接**: [arXiv:2412.03215](https://arxiv.org/abs/2412.03215) · 📚 被引 3
- **作者**: Marcin Przewiezlikowski, Randall Balestriero, Wojciech Jasinski, Marek Smieja, Bartosz Zielinski
- **🏷️ 机构**: Jagiellonian University,Faculty of Mathematics and Computer Science, Brown University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Image Modeling (MIM) has emerged as a promising approach for Self-Supervised Learning (SSL) of visual representations. However, the out-of-the-box performance of MIMs is typically inferior to competing approaches. Most users cannot afford fine-tuning due to the need for large amounts of data, high GPU consumption, and specialized user knowledge. Therefore, the practical use of MIM representations is limited. In this paper we ask what is the reason for the poor out-of-the-box performance of MIMs. Is it due to weaker features produced by MIM models, or is it due to suboptimal usage? Through detailed analysis, we show that attention in MIMs is spread almost uniformly over many patches, leading to ineffective aggregation by the [cls] token. Based on this insight, we propose Selective Aggregation to better capture the rich semantic information retained in patch tokens, which significantly improves the out-of-the-box performance of MIM.

</details>

### Unsupervised Part Discovery via Descriptor-Based Masked Image Restoration with Optimized Constraints.
- **链接**: [arXiv:2507.11985](https://arxiv.org/abs/2507.11985) · [代码](https://github.com/Jiahao-UTS/MPAE) · 📚 被引 0
- **作者**: Jiahao Xia, Yike Wu, Wenjian Huang, Jianguo Zhang, Jian Zhang
- **🏷️ 机构**: University of Technology Sydney,Faculty of Engineering and IT, Southern University of Science and Technology,Dept. of Comp. Sci. and Eng.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Part-level features are crucial for image understanding, but few studies focus on them because of the lack of fine-grained labels. Although unsupervised part discovery can eliminate the reliance on labels, most of them cannot maintain robustness across various categories and scenarios, which restricts their application range. To overcome this limitation, we present a more effective paradigm for unsupervised part discovery, named Masked Part Autoencoder (MPAE). It first learns part descriptors as well as a feature map from the inputs and produces patch features from a masked version of the original images. Then, the masked regions are filled with the learned part descriptors based on the similarity between the local features and descriptors. By restoring these masked patches using the part descriptors, they become better aligned with their part shapes, guided by appearance features from unmasked patches. Finally, MPAE robustly discovers meaningful parts that closely match the actual object shapes, even in complex scenarios. Moreover, several looser yet more effective constraints are proposed to enable MPAE to identify the presence of parts across various scenarios and categories in an unsupervised manner. This provides the foundation for addressing challenges posed by occlusion and for exploring part similarity across multiple categories. Extensive experiments demonstrate that our method robustly discovers meaningful parts across various categories and scenarios. The code is available at the project https://github.com/Jiahao-UTS/MPAE.

</details>

## 跨领域论文（完整笔记在其他领域）

- Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-Time Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Talking to DINO: Bridging Self-Supervised Vision Backbones with Language for Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Differential-Informed Sample Selection Accelerates Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202025.md)
- Point Cloud Self-Supervised Learning via 3D to Multi-View Masked Learner. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- GaussianOcc: Fully Self-Supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting. → [occupancy](../occupancy/Guideline%202025.md)
- AD-GS: Object-Aware B-Spline Gaussian Splatting for Self-Supervised Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Hybrid-Grained Feature Aggregation with Coarse-to-Fine Language Guidance for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
