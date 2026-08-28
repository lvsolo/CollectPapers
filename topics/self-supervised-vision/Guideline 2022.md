# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 80 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### How Severe Is Benchmark-Sensitivity in Video Self-supervised Learning?
- **链接**: [arXiv:2203.14221](https://arxiv.org/abs/2203.14221) · 📚 被引 14
- **作者**: Fida Mohammad Thoker, Hazel Doughty, Piyush Bagad, Cees G. M. Snoek
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent success of video self-supervised learning models, there is much still to be understood about their generalization capability. In this paper, we investigate how sensitive video self-supervised learning is to the current conventional benchmark and whether methods generalize beyond the canonical evaluation setting. We do this across four different factors of sensitivity: domain, samples, actions and task. Our study which encompasses over 500 experiments on 7 video datasets, 9 self-supervised methods and 6 video understanding tasks, reveals that current benchmarks in video self-supervised learning are not good indicators of generalization along these sensitivity factors. Further, we find that self-supervised methods considerably lag behind vanilla supervised pre-training, especially when domain shift is large and the amount of available downstream samples are low. From our analysis, we distill the SEVERE-benchmark, a subset of our experiments, and discuss its implication for evaluating the generalizability of representations obtained by existing and future self-supervised video learning methods.

</details>

### SLiDE: Self-supervised LiDAR De-snowing Through Reconstruction Difficulty.
- **链接**: [arXiv:2208.04043](https://arxiv.org/abs/2208.04043) · 📚 被引 21
- **作者**: Gwangtak Bae, Byungjun Kim, Seongyong Ahn, Jihong Min, Inwook Shim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR is widely used to capture accurate 3D outdoor scene structures. However, LiDAR produces many undesirable noise points in snowy weather, which hamper analyzing meaningful 3D scene structures. Semantic segmentation with snow labels would be a straightforward solution for removing them, but it requires laborious point-wise annotation. To address this problem, we propose a novel self-supervised learning framework for snow points removal in LiDAR point clouds. Our method exploits the structural characteristic of the noise points: low spatial correlation with their neighbors. Our method consists of two deep neural networks: Point Reconstruction Network (PR-Net) reconstructs each point from its neighbors; Reconstruction Difficulty Network (RD-Net) predicts point-wise difficulty of the reconstruction by PR-Net, which we call reconstruction difficulty. With simple post-processing, our method effectively detects snow points without any label. Our method achieves the state-of-the-art performance among label-free approaches and is comparable to the fully-supervised method. Moreover, we demonstrate that our method can be exploited as a pretext task to improve label-efficiency of supervised training of de-snowing.

</details>

### SuperLine3D: Self-supervised Line Segmentation and Description for LiDAR Point Cloud.
- **链接**: [arXiv:2208.01925](https://arxiv.org/abs/2208.01925) · [代码](https://github.com/zxrzju/SuperLine3D.git) · 📚 被引 12
- **作者**: Xiangrui Zhao, Sheng Yang, Tianxin Huang, Jun Chen, Teng Ma, Mingyang Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Poles and building edges are frequently observable objects on urban roads, conveying reliable hints for various computer vision tasks. To repetitively extract them as features and perform association between discrete LiDAR frames for registration, we propose the first learning-based feature segmentation and description model for 3D lines in LiDAR point cloud. To train our model without the time consuming and tedious data labeling process, we first generate synthetic primitives for the basic appearance of target lines, and build an iterative line auto-labeling process to gradually refine line labels on real LiDAR scans. Our segmentation model can extract lines under arbitrary scale perturbations, and we use shared EdgeConv encoder layers to train the two segmentation and descriptor heads jointly. Base on the model, we can build a highly-available global registration module for point cloud registration, in conditions without initial transformation hints. Experiments have demonstrated that our line-based registration method is highly competitive to state-of-the-art point-based approaches. Our code is available at https://github.com/zxrzju/SuperLine3D.git.

</details>

### PointCLM: A Contrastive Learning-based Framework for Multi-instance Point Cloud Registration.
- **链接**: [arXiv:2209.00219](https://arxiv.org/abs/2209.00219)
- **作者**: Mingzhi Yuan, Zhihao Li, Qiuye Jin, Xinrong Chen, Manning Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-instance point cloud registration is the problem of estimating multiple poses of source point cloud instances within a target point cloud. Solving this problem is challenging since inlier correspondences of one instance constitute outliers of all the other instances. Existing methods often rely on time-consuming hypothesis sampling or features leveraging spatial consistency, resulting in limited performance. In this paper, we propose PointCLM, a contrastive learning-based framework for mutli-instance point cloud registration. We first utilize contrastive learning to learn well-distributed deep representations for the input putative correspondences. Then based on these representations, we propose a outlier pruning strategy and a clustering strategy to efficiently remove outliers and assign the remaining correspondences to correct instances. Our method outperforms the state-of-the-art methods on both synthetic and real datasets by a large margin.

</details>

### Masked Discrimination for Self-supervised Learning on Point Clouds.
- **链接**: [arXiv:2203.11183](https://arxiv.org/abs/2203.11183) · [代码](https://github.com/haotian-liu/MaskPoint) · 📚 被引 137
- **作者**: Haotian Liu, Mu Cai, Yong Jae Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked autoencoding has achieved great success for self-supervised learning in the image and language domains. However, mask based pretraining has yet to show benefits for point cloud understanding, likely due to standard backbones like PointNet being unable to properly handle the training versus testing distribution mismatch introduced by masking during training. In this paper, we bridge this gap by proposing a discriminative mask pretraining Transformer framework, MaskPoint}, for point clouds. Our key idea is to represent the point cloud as discrete occupancy values (1 if part of the point cloud; 0 if not), and perform simple binary classification between masked object points and sampled noise points as the proxy task. In this way, our approach is robust to the point sampling variance in point clouds, and facilitates learning rich representations. We evaluate our pretrained models across several downstream tasks, including 3D shape classification, segmentation, and real-word object detection, and demonstrate state-of-the-art results while achieving a significant pretraining speedup (e.g., 4.1x on ScanNet) compared to the prior state-of-the-art Transformer baseline. Code is available at https://github.com/haotian-liu/MaskPoint.

</details>

### Masked Autoencoders for Point Cloud Self-supervised Learning.
- **链接**: [arXiv:2203.06604](https://arxiv.org/abs/2203.06604)
- **作者**: Yatian Pang, Wenxiao Wang, Francis E. H. Tay, Wei Liu, Yonghong Tian, Li Yuan
- **🏷️ 机构**: National University of Singapore, Singapore, Institute for Infocomm Research, A*STAR, Singapore, School of Electronic and Computer Engineering, Peking University, Beijing, China
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a promising scheme of self-supervised learning, masked autoencoding has significantly advanced natural language processing and computer vision. Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud's properties, including leakage of location information and uneven information density. Concretely, we divide the input point cloud into irregular point patches and randomly mask them at a high ratio. Then, a standard Transformer based autoencoder, with an asymmetric design and a shifting mask tokens operation, learns high-level latent features from unmasked point patches, aiming to reconstruct the masked point patches. Extensive experiments show that our approach is efficient during pre-training and generalizes well on various downstream tasks. Specifically, our pre-trained models achieve 85.18% accuracy on ScanObjectNN and 94.04% accuracy on ModelNet40, outperforming all the other self-supervised learning methods. We show with our scheme, a simple architecture entirely based on standard Transformers can surpass dedicated Transformer models from supervised learning. Our approach also advances state-of-the-art accuracies by 1.5%-2.3% in the few-shot object classification. Furthermore, our work inspires the feasibility of applying unified architectures from languages and images to the point cloud.

</details>

### Differentiable Raycasting for Self-Supervised Occupancy Forecasting.
- **链接**: [arXiv:2210.01917](https://arxiv.org/abs/2210.01917) · 📚 被引 58
- **作者**: Tarasha Khurana, Peiyun Hu, Achal Dave, Jason Ziglar, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motion planning for safe autonomous driving requires learning how the environment around an ego-vehicle evolves with time. Ego-centric perception of driveable regions in a scene not only changes with the motion of actors in the environment, but also with the movement of the ego-vehicle itself. Self-supervised representations proposed for large-scale planning, such as ego-centric freespace, confound these two motions, making the representation difficult to use for downstream motion planners. In this paper, we use geometric occupancy as a natural alternative to view-dependent representations such as freespace. Occupancy maps naturally disentangle the motion of the environment from the motion of the ego-vehicle. However, one cannot directly observe the full 3D occupancy of a scene (due to occlusion), making it difficult to use as a signal for learning. Our key insight is to use differentiable raycasting to "render" future occupancy predictions into future LiDAR sweep predictions, which can be compared with ground-truth sweeps for self-supervised learning. The use of differentiable raycasting allows occupancy to emerge as an internal representation within the forecasting network. In the absence of groundtruth occupancy, we quantitatively evaluate the forecasting of raycasted LiDAR sweeps and show improvements of upto 15 F1 points. For downstream motion planners, where emergent occupancy can be directly used to guide non-driveable regions, this representation relatively reduces the number of collisions with objects by up to 17% as compared to freespace-centric motion planners.

</details>

### DevNet: Self-supervised Monocular Depth Learning via Density Volume Construction.
- **链接**: [arXiv:2209.06351](https://arxiv.org/abs/2209.06351) · [代码](https://github.com/gitkaichenzhou/DevNet) · 📚 被引 26
- **作者**: Kaichen Zhou, Lanqing Hong, Changhao Chen, Hang Xu, Chaoqiang Ye, Qingyong Hu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised depth learning from monocular images normally relies on the 2D pixel-wise photometric relation between temporally adjacent image frames. However, they neither fully exploit the 3D point-wise geometric correspondences, nor effectively tackle the ambiguities in the photometric warping caused by occlusions or illumination inconsistency. To address these problems, this work proposes Density Volume Construction Network (DevNet), a novel self-supervised monocular depth learning framework, that can consider 3D spatial information, and exploit stronger geometric constraints among adjacent camera frustums. Instead of directly regressing the pixel value from a single image, our DevNet divides the camera frustum into multiple parallel planes and predicts the pointwise occlusion probability density on each plane. The final depth map is generated by integrating the density along corresponding rays. During the training process, novel regularization strategies and loss functions are introduced to mitigate photometric ambiguities and overfitting. Without obviously enlarging model parameters size or running time, DevNet outperforms several representative baselines on both the KITTI-2015 outdoor dataset and NYU-V2 indoor dataset. In particular, the root-mean-square-deviation is reduced by around 4% with DevNet on both KITTI-2015 and NYU-V2 in the task of depth estimation. Code is available at https://github.com/gitkaichenzhou/DevNet.

</details>

### Hierarchically Self-supervised Transformer for Human Skeleton Representation Learning.
- **链接**: [arXiv:2207.09644](https://arxiv.org/abs/2207.09644)
- **作者**: Yuxiao Chen, Long Zhao, Jianbo Yuan, Yu Tian, Zhaoyang Xia, Shijie Geng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the success of fully-supervised human skeleton sequence modeling, utilizing self-supervised pre-training for skeleton sequence representation learning has been an active field because acquiring task-specific skeleton annotations at large scales is difficult. Recent studies focus on learning video-level temporal and discriminative information using contrastive learning, but overlook the hierarchical spatial-temporal nature of human skeletons. Different from such superficial supervision at the video level, we propose a self-supervised hierarchical pre-training scheme incorporated into a hierarchical Transformer-based skeleton sequence encoder (Hi-TRS), to explicitly capture spatial, short-term, and long-term temporal dependencies at frame, clip, and video levels, respectively. To evaluate the proposed self-supervised pre-training scheme with Hi-TRS, we conduct extensive experiments covering three skeleton-based downstream tasks including action recognition, action detection, and motion prediction. Under both supervised and semi-supervised evaluation protocols, our method achieves the state-of-the-art performance. Additionally, we demonstrate that the prior knowledge learned by our model in the pre-training stage has strong transfer capability for different downstream tasks.

</details>

### Towards Efficient and Effective Self-supervised Learning of Visual Representations.
- **链接**: [arXiv:2210.09866](https://arxiv.org/abs/2210.09866)
- **作者**: Sravanti Addepalli, Kaushal Bhogale, Priyam Dey, R. Venkatesh Babu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervision has emerged as a propitious method for visual representation learning after the recent paradigm shift from handcrafted pretext tasks to instance-similarity based approaches. Most state-of-the-art methods enforce similarity between various augmentations of a given image, while some methods additionally use contrastive approaches to explicitly ensure diverse representations. While these approaches have indeed shown promising direction, they require a significantly larger number of training iterations when compared to the supervised counterparts. In this work, we explore reasons for the slow convergence of these methods, and further propose to strengthen them using well-posed auxiliary tasks that converge significantly faster, and are also useful for representation learning. The proposed method utilizes the task of rotation prediction to improve the efficiency of existing state-of-the-art methods. We demonstrate significant gains in performance using the proposed method on multiple datasets, specifically for lower training epochs.

</details>

### Self-Supervised Classification Network.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_7)
- **作者**: Elad Amrani, Leonid Karlinsky, Alexander M. Bronstein
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Synergistic Self-supervised and Quantization Learning.
- **链接**: [arXiv:2207.05432](https://arxiv.org/abs/2207.05432) · [代码](https://github.com/megvii-research/SSQL-ECCV2022)
- **作者**: Yun-Hao Cao, Peiqin Sun, Yechang Huang, Jianxin Wu, Shuchang Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the success of self-supervised learning (SSL), it has become a mainstream paradigm to fine-tune from self-supervised pretrained models to boost the performance on downstream tasks. However, we find that current SSL models suffer severe accuracy drops when performing low-bit quantization, prohibiting their deployment in resource-constrained applications. In this paper, we propose a method called synergistic self-supervised and quantization learning (SSQL) to pretrain quantization-friendly self-supervised models facilitating downstream deployment. SSQL contrasts the features of the quantized and full precision models in a self-supervised fashion, where the bit-width for the quantized model is randomly selected in each step. SSQL not only significantly improves the accuracy when quantized to lower bit-widths, but also boosts the accuracy of full precision models in most cases. By only training once, SSQL can then benefit various downstream tasks at different bit-widths simultaneously. Moreover, the bit-width flexibility is achieved without additional storage overhead, requiring only one copy of weights during training and inference. We theoretically analyze the optimization process of SSQL, and conduct exhaustive experiments on various benchmarks to further demonstrate the effectiveness of our method. Our code is available at https://github.com/megvii-research/SSQL-ECCV2022.

</details>

### Sound Localization by Self-supervised Time Delay Estimation.
- **链接**: [arXiv:2204.12489](https://arxiv.org/abs/2204.12489) · 📚 被引 13
- **作者**: Ziyang Chen, David F. Fouhey, Andrew Owens
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sounds reach one microphone in a stereo pair sooner than the other, resulting in an interaural time delay that conveys their directions. Estimating a sound's time delay requires finding correspondences between the signals recorded by each microphone. We propose to learn these correspondences through self-supervision, drawing on recent techniques from visual tracking. We adapt the contrastive random walk of Jabri et al. to learn a cycle-consistent representation from unlabeled stereo sounds, resulting in a model that performs on par with supervised methods on "in the wild" internet recordings. We also propose a multimodal contrastive learning model that solves a visually-guided localization task: estimating the time delay for a particular person in a multi-speaker mixture, given a visual representation of their face. Project site: https://ificl.github.io/stereocrw/

</details>

### GOCA: Guided Online Cluster Assignment for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_1)
- **作者**: Huseyin Coskun, Alireza Zareian, Joshua L. Moore, Federico Tombari, Chen Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Trust, but Verify: Using Self-supervised Probing to Improve Trustworthiness.
- **链接**: [arXiv:2302.02628](https://arxiv.org/abs/2302.02628) · 📚 被引 0
- **作者**: Ailin Deng, Shen Li, Miao Xiong, Zhirui Chen, Bryan Hooi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Trustworthy machine learning is of primary importance to the practical deployment of deep learning models. While state-of-the-art models achieve astonishingly good performance in terms of accuracy, recent literature reveals that their predictive confidence scores unfortunately cannot be trusted: e.g., they are often overconfident when wrong predictions are made, or so even for obvious outliers. In this paper, we introduce a new approach of self-supervised probing, which enables us to check and mitigate the overconfidence issue for a trained model, thereby improving its trustworthiness. We provide a simple yet effective framework, which can be flexibly applied to existing trustworthiness-related methods in a plug-and-play manner. Extensive experiments on three trustworthiness-related tasks (misclassification detection, calibration and out-of-distribution detection) across various benchmarks verify the effectiveness of our proposed probing framework.

</details>

### SOS! Self-supervised Learning over Sets of Handled Objects in Egocentric Action Recognition.
- **链接**: [arXiv:2204.04796](https://arxiv.org/abs/2204.04796)
- **作者**: Victor Escorcia, Ricardo Guerrero, Xiatian Zhu, Brais Martínez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning an egocentric action recognition model from video data is challenging due to distractors (e.g., irrelevant objects) in the background. Further integrating object information into an action model is hence beneficial. Existing methods often leverage a generic object detector to identify and represent the objects in the scene. However, several important issues remain. Object class annotations of good quality for the target domain (dataset) are still required for learning good object representation. Besides, previous methods deeply couple the existing action models and need to retrain them jointly with object representation, leading to costly and inflexible integration. To overcome both limitations, we introduce Self-Supervised Learning Over Sets (SOS), an approach to pre-train a generic Objects In Contact (OIC) representation model from video object regions detected by an off-the-shelf hand-object contact detector. Instead of augmenting object regions individually as in conventional self-supervised learning, we view the action process as a means of natural data transformations with unique spatio-temporal continuity and exploit the inherent relationships among per-video object sets. Extensive experiments on two datasets, EPIC-KITCHENS-100 and EGTEA, show that our OIC significantly boosts the performance of multiple state-of-the-art video classification models.

</details>

### DisCo: Remedying Self-supervised Learning on Lightweight Models with Distilled Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_14) · 📚 被引 32
- **作者**: Yuting Gao, Jia-Xin Zhuang, Shaohui Lin, Hao Cheng, Xing Sun, Ke Li et al.
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

### Self-supervised Human Mesh Recovery with Cross-Representation Alignment.
- **链接**: [arXiv:2209.04596](https://arxiv.org/abs/2209.04596) · 📚 被引 8
- **作者**: Xuan Gong, Meng Zheng, Benjamin Planche, Srikrishna Karanam, Terrence Chen, David S. Doermann et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fully supervised human mesh recovery methods are data-hungry and have poor generalizability due to the limited availability and diversity of 3D-annotated benchmark datasets. Recent progress in self-supervised human mesh recovery has been made using synthetic-data-driven training paradigms where the model is trained from synthetic paired 2D representation (e.g., 2D keypoints and segmentation masks) and 3D mesh. However, on synthetic dense correspondence maps (i.e., IUV) few have been explored since the domain gap between synthetic training data and real testing data is hard to address for 2D dense representation. To alleviate this domain gap on IUV, we propose cross-representation alignment utilizing the complementary information from the robust but sparse representation (2D keypoints). Specifically, the alignment errors between initial mesh estimation and both 2D representations are forwarded into regressor and dynamically corrected in the following mesh regression. This adaptive cross-representation alignment explicitly learns from the deviations and captures complementary information: robustness from sparse representation and richness from dense representation. We conduct extensive experiments on multiple standard benchmark datasets and demonstrate competitive results, helping take a step towards reducing the annotation effort needed to produce state-of-the-art models in human mesh estimation.

</details>

### Generative Subgraph Contrast for Self-Supervised Graph Representation Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20056-4_6) · 📚 被引 13
- **作者**: Yuehui Han, Le Hui, Haobo Jiang, Jianjun Qian, Jin Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### GeoRefine: Self-supervised Online Depth Refinement for Accurate Dense Mapping.
- **链接**: [arXiv:2205.01656](https://arxiv.org/abs/2205.01656)
- **作者**: Pan Ji, Qingan Yan, Yuxin Ma, Yi Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a robust and accurate depth refinement system, named GeoRefine, for geometrically-consistent dense mapping from monocular sequences. GeoRefine consists of three modules: a hybrid SLAM module using learning-based priors, an online depth refinement module leveraging self-supervision, and a global mapping module via TSDF fusion. The proposed system is online by design and achieves great robustness and accuracy via: (i) a robustified hybrid SLAM that incorporates learning-based optical flow and/or depth; (ii) self-supervised losses that leverage SLAM outputs and enforce long-term geometric consistency; (iii) careful system design that avoids degenerate cases in online depth refinement. We extensively evaluate GeoRefine on multiple public datasets and reach as low as $5\%$ absolute relative depth errors.

</details>

### MoDA: Map Style Transfer for Self-supervised Domain Adaptation of Embodied Agents.
- **链接**: [arXiv:2211.15992](https://arxiv.org/abs/2211.15992) · 📚 被引 4
- **作者**: Eun Sun Lee, Junho Kim, SangWon Park, Young Min Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a domain adaptation method, MoDA, which adapts a pretrained embodied agent to a new, noisy environment without ground-truth supervision. Map-based memory provides important contextual information for visual navigation, and exhibits unique spatial structure mainly composed of flat walls and rectangular obstacles. Our adaptation approach encourages the inherent regularities on the estimated maps to guide the agent to overcome the prevalent domain discrepancy in a novel environment. Specifically, we propose an efficient learning curriculum to handle the visual and dynamics corruptions in an online manner, self-supervised with pseudo clean maps generated by style transfer networks. Because the map-based representation provides spatial knowledge for the agent's policy, our formulation can deploy the pretrained policy networks from simulators in a new setting. We evaluate MoDA in various practical scenarios and show that our proposed method quickly enhances the agent's performance in downstream tasks including localization, mapping, exploration, and point-goal navigation.

</details>

### A Closer Look at Invariances in Self-supervised Pre-training for 3D Vision.
- **链接**: [arXiv:2207.04997](https://arxiv.org/abs/2207.04997) · 📚 被引 21
- **作者**: Lanxiao Li, Michael Heizmann
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pre-training for 3D vision has drawn increasing research interest in recent years. In order to learn informative representations, a lot of previous works exploit invariances of 3D features, e.g., perspective-invariance between views of the same scene, modality-invariance between depth and RGB images, format-invariance between point clouds and voxels. Although they have achieved promising results, previous researches lack a systematic and fair comparison of these invariances. To address this issue, our work, for the first time, introduces a unified framework, under which various pre-training methods can be investigated. We conduct extensive experiments and provide a closer look at the contributions of different invariances in 3D pre-training. Also, we propose a simple but effective method that jointly pre-trains a 3D encoder and a depth map encoder using contrastive learning. Models pre-trained with our method gain significant performance boost in downstream tasks. For instance, a pre-trained VoteNet outperforms previous methods on SUN RGB-D and ScanNet object detection benchmarks with a clear margin.

</details>

### Self-supervised Social Relation Representation for Human Group Detection.
- **链接**: [arXiv:2203.03843](https://arxiv.org/abs/2203.03843) · 📚 被引 12
- **作者**: Jiacheng Li, Ruize Han, Haomin Yan, Zekun Qian, Wei Feng, Song Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human group detection, which splits crowd of people into groups, is an important step for video-based human social activity analysis. The core of human group detection is the human social relation representation and division.In this paper, we propose a new two-stage multi-head framework for human group detection. In the first stage, we propose a human behavior simulator head to learn the social relation feature embedding, which is self-supervisely trained by leveraging the socially grounded multi-person behavior relationship. In the second stage, based on the social relation embedding, we develop a self-attention inspired network for human group detection. Remarkable performance on two state-of-the-art large-scale benchmarks, i.e., PANDA and JRDB-Group, verifies the effectiveness of the proposed framework. Benefiting from the self-supervised social relation embedding, our method can provide promising results with very few (labeled) training data. We will release the source code to the public.

</details>

### Fusion from Decomposition: A Self-Supervised Decomposition Approach for Image Fusion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19797-0_41) · 📚 被引 151
- **作者**: Pengwei Liang, Junjun Jiang, Xianming Liu, Jiayi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Category-Level 6D Object Pose and Size Estimation Using Self-supervised Deep Prior Deformation Networks.
- **链接**: [arXiv:2207.05444](https://arxiv.org/abs/2207.05444) · [代码](https://github.com/JiehongLin/Self-DPDN) · 📚 被引 82
- **作者**: Jiehong Lin, Zewei Wei, Changxing Ding, Kui Jia
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It is difficult to precisely annotate object instances and their semantics in 3D space, and as such, synthetic data are extensively used for these tasks, e.g., category-level 6D object pose and size estimation. However, the easy annotations in synthetic domains bring the downside effect of synthetic-to-real (Sim2Real) domain gap. In this work, we aim to address this issue in the task setting of Sim2Real, unsupervised domain adaptation for category-level 6D object pose and size estimation. We propose a method that is built upon a novel Deep Prior Deformation Network, shortened as DPDN. DPDN learns to deform features of categorical shape priors to match those of object observations, and is thus able to establish deep correspondence in the feature space for direct regression of object poses and sizes. To reduce the Sim2Real domain gap, we formulate a novel self-supervised objective upon DPDN via consistency learning; more specifically, we apply two rigid transformations to each object observation in parallel, and feed them into DPDN respectively to yield dual sets of predictions; on top of the parallel learning, an inter-consistency term is employed to keep cross consistency between dual predictions for improving the sensitivity of DPDN to pose changes, while individual intra-consistency ones are used to enforce self-adaptation within each learning itself. We train DPDN on both training sets of the synthetic CAMERA25 and real-world REAL275 datasets; our results outperform the existing methods on REAL275 test set under both the unsupervised and supervised settings. Ablation studies also verify the efficacy of our designs. Our code is released publicly at https://github.com/JiehongLin/Self-DPDN.

</details>

### Source-Free Domain Adaptation with Contrastive Domain Alignment and Self-supervised Exploration for Face Anti-spoofing.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19775-8_30) · 📚 被引 45
- **作者**: Yuchen Liu, Yabo Chen, Wenrui Dai, Mengran Gou, Chun-Ting Huang, Hongkai Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Improving Self-supervised Lightweight Model Learning via Hard-Aware Metric Distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_17) · 📚 被引 5
- **作者**: Hao Liu, Mang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Self-supervised Learning of Visual Graph Matching.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20050-2_22)
- **作者**: Chang Liu, Shaofeng Zhang, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Motion Sensitive Contrastive Learning for Self-supervised Video Representation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19833-5_27)
- **作者**: Jingcheng Ni, Nan Zhou, Jie Qin, Qian Wu, Junqi Liu, Boxun Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Domain Knowledge-Informed Self-supervised Representations for Workout Form Assessment.
- **链接**: [arXiv:2202.14019](https://arxiv.org/abs/2202.14019) · [代码](https://github.com/ParitoshParmar/Fitness-AQA) · 📚 被引 20
- **作者**: Paritosh Parmar, Amol Gharat, Helge Rhodin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Maintaining proper form while exercising is important for preventing injuries and maximizing muscle mass gains. Detecting errors in workout form naturally requires estimating human's body pose. However, off-the-shelf pose estimators struggle to perform well on the videos recorded in gym scenarios due to factors such as camera angles, occlusion from gym equipment, illumination, and clothing. To aggravate the problem, the errors to be detected in the workouts are very subtle. To that end, we propose to learn exercise-oriented image and video representations from unlabeled samples such that a small dataset annotated by experts suffices for supervised error detection. In particular, our domain knowledge-informed self-supervised approaches (pose contrastive learning and motion disentangling) exploit the harmonic motion of the exercise actions, and capitalize on the large variances in camera angles, clothes, and illumination to learn powerful representations. To facilitate our self-supervised pretraining, and supervised finetuning, we curated a new exercise dataset, Fitness-AQA (https://github.com/ParitoshParmar/Fitness-AQA), comprising of three exercises: BackSquat, BarbellRow, and OverheadPress. It has been annotated by expert trainers for multiple crucial and typically occurring exercise errors. Experimental results show that our self-supervised representations outperform off-the-shelf 2D- and 3D-pose estimators and several other baselines. We also show that our approaches can be applied to other domains/tasks such as pose estimation and dive quality assessment.

</details>

### The Challenges of Continuous Self-Supervised Learning.
- **链接**: [arXiv:2203.12710](https://arxiv.org/abs/2203.12710)
- **作者**: Senthil Purushwalkam, Pedro Morgado, Abhinav Gupta
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) aims to eliminate one of the major bottlenecks in representation learning - the need for human annotations. As a result, SSL holds the promise to learn representations from data in-the-wild, i.e., without the need for finite and static datasets. Instead, true SSL algorithms should be able to exploit the continuous stream of data being generated on the internet or by agents exploring their environments. But do traditional self-supervised learning approaches work in this setup? In this work, we investigate this question by conducting experiments on the continuous self-supervised learning problem. While learning in the wild, we expect to see a continuous (infinite) non-IID data stream that follows a non-stationary distribution of visual concepts. The goal is to learn a representation that can be robust, adaptive yet not forgetful of concepts seen in the past. We show that a direct application of current methods to such continuous setup is 1) inefficient both computationally and in the amount of data required, 2) leads to inferior representations due to temporal correlations (non-IID data) in some sources of streaming data and 3) exhibits signs of catastrophic forgetting when trained on sources with non-stationary data distributions. We propose the use of replay buffers as an approach to alleviate the issues of inefficiency and temporal correlations. We further propose a novel method to enhance the replay buffer by maintaining the least redundant samples. Minimum redundancy (MinRed) buffers allow us to learn effective representations even in the most challenging streaming scenarios composed of sequential visual data obtained from a single embodied agent, and alleviates the problem of catastrophic forgetting when learning from data with non-stationary semantic distributions.

</details>

### Static and Dynamic Concepts for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_9)
- **作者**: Rui Qian, Shuangrui Ding, Xian Liu, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022

### Dual-Domain Self-supervised Learning and Model Adaption for Deep Compressive Imaging.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20056-4_24) · 📚 被引 11
- **作者**: Yuhui Quan, Xinran Qin, Tongyao Pang, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Federated Self-supervised Learning for Video Understanding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_29)
- **作者**: Yasar Abbas Ur Rehman, Yan Gao, Jiajun Shen, Pedro Porto Buarque de Gusmão, Nicholas D. Lane
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Completely Self-supervised Crowd Counting via Distribution Matching.
- **链接**: [arXiv:2009.06420](https://arxiv.org/abs/2009.06420) · [代码](https://github.com/val-iisc/css-ccnn) · 📚 被引 19
- **作者**: Deepak Babu Sam, Abhinav Agarwalla, Jimmy Joseph, Vishwanath A. Sindagi, R. Venkatesh Babu, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dense crowd counting is a challenging task that demands millions of head annotations for training models. Though existing self-supervised approaches could learn good representations, they require some labeled data to map these features to the end task of density estimation. We mitigate this issue with the proposed paradigm of complete self-supervision, which does not need even a single labeled image. The only input required to train, apart from a large set of unlabeled crowd images, is the approximate upper limit of the crowd count for the given dataset. Our method dwells on the idea that natural crowds follow a power law distribution, which could be leveraged to yield error signals for backpropagation. A density regressor is first pretrained with self-supervision and then the distribution of predictions is matched to the prior by optimizing Sinkhorn distance between the two. Experiments show that this results in effective learning of crowd features and delivers significant counting performance. Furthermore, we establish the superiority of our method in less data setting as well. The code and models for our approach is available at https://github.com/val-iisc/css-ccnn.

</details>

### Natural Synthetic Anomalies for Self-supervised Anomaly Detection and Localization.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_27)
- **作者**: Hannah M. Schlüter, Jeremy Tan, Benjamin Hou, Bernhard Kainz
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Social-SSL: Self-supervised Cross-Sequence Representation Learning Based on Transformers for Multi-agent Trajectory Prediction.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_14) · 📚 被引 26
- **作者**: Li-Wu Tsao, Yan-Kai Wang, Hao-Siang Lin, Hong-Han Shuai, Lai-Kuan Wong, Wen-Huang Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Self-supervised Sparse Representation for Video Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19778-9_42)
- **作者**: Jhih-Ciang Wu, He-Yen Hsieh, Ding-Jie Chen, Chiou-Shann Fuh, Tyng-Luh Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### UniMiSS: Universal Medical Self-supervised Learning via Breaking Dimensionality Barrier.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_33) · 📚 被引 59
- **作者**: Yutong Xie, Jianpeng Zhang, Yong Xia, Qi Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### PreTraM: Self-supervised Pre-training via Connecting Trajectory and Map.
- **链接**: [arXiv:2204.10435](https://arxiv.org/abs/2204.10435)
- **作者**: Chenfeng Xu, Tian Li, Chen Tang, Lingfeng Sun, Kurt Keutzer, Masayoshi Tomizuka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has recently achieved significant progress in trajectory forecasting. However, the scarcity of trajectory data inhibits the data-hungry deep-learning models from learning good representations. While mature representation learning methods exist in computer vision and natural language processing, these pre-training methods require large-scale data. It is hard to replicate these approaches in trajectory forecasting due to the lack of adequate trajectory data (e.g., 34K samples in the nuScenes dataset). To work around the scarcity of trajectory data, we resort to another data modality closely related to trajectories-HD-maps, which is abundantly provided in existing datasets. In this paper, we propose PreTraM, a self-supervised pre-training scheme via connecting trajectories and maps for trajectory forecasting. Specifically, PreTraM consists of two parts: 1) Trajectory-Map Contrastive Learning, where we project trajectories and maps to a shared embedding space with cross-modal contrastive learning, and 2) Map Contrastive Learning, where we enhance map representation with contrastive learning on large quantities of HD-maps. On top of popular baselines such as AgentFormer and Trajectron++, PreTraM boosts their performance by 5.5% and 6.9% relatively in FDE-10 on the challenging nuScenes dataset. We show that PreTraM improves data efficiency and scales well with model size.

</details>

### RegionCL: Exploring Contrastive Region Pairs for Self-supervised Representation Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_28) · 📚 被引 7
- **作者**: Yufei Xu, Qiming Zhang, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Domain Invariant Masked Autoencoders for Self-supervised Learning from Multi-domains.
- **链接**: [arXiv:2205.04771](https://arxiv.org/abs/2205.04771) · 📚 被引 14
- **作者**: Haiyang Yang, Shixiang Tang, Meilin Chen, Yizhou Wang, Feng Zhu, Lei Bai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalizing learned representations across significantly different visual domains is a fundamental yet crucial ability of the human visual system. While recent self-supervised learning methods have achieved good performances with evaluation set on the same domain as the training set, they will have an undesirable performance decrease when tested on a different domain. Therefore, the self-supervised learning from multiple domains task is proposed to learn domain-invariant features that are not only suitable for evaluation on the same domain as the training set but also can be generalized to unseen domains. In this paper, we propose a Domain-invariant Masked AutoEncoder (DiMAE) for self-supervised learning from multi-domains, which designs a new pretext task, \emph{i.e.,} the cross-domain reconstruction task, to learn domain-invariant features. The core idea is to augment the input image with style noise from different domains and then reconstruct the image from the embedding of the augmented image, regularizing the encoder to learn domain-invariant features. To accomplish the idea, DiMAE contains two critical designs, 1) content-preserved style mix, which adds style information from other domains to input while persevering the content in a parameter-free manner, and 2) multiple domain-specific decoders, which recovers the corresponding domain style of input to the encoded domain-invariant features for reconstruction. Experiments on PACS and DomainNet illustrate that DiMAE achieves considerable gains compared with recent state-of-the-art methods.

</details>

### PT4AL: Using Self-supervised Pretext Tasks for Active Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_34)
- **作者**: John Seon Keun Yi, Minseok Seo, Jongchan Park, Dong-Geol Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Self-supervised Interactive Object Segmentation Through a Singulation-and-Grasping Approach.
- **链接**: [arXiv:2207.09314](https://arxiv.org/abs/2207.09314) · 📚 被引 12
- **作者**: Houjian Yu, Changhyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Instance segmentation with unseen objects is a challenging problem in unstructured environments. To solve this problem, we propose a robot learning approach to actively interact with novel objects and collect each object's training label for further fine-tuning to improve the segmentation model performance, while avoiding the time-consuming process of manually labeling a dataset. The Singulation-and-Grasping (SaG) policy is trained through end-to-end reinforcement learning. Given a cluttered pile of objects, our approach chooses pushing and grasping motions to break the clutter and conducts object-agnostic grasping for which the SaG policy takes as input the visual observations and imperfect segmentation. We decompose the problem into three subtasks: (1) the object singulation subtask aims to separate the objects from each other, which creates more space that alleviates the difficulty of (2) the collision-free grasping subtask; (3) the mask generation subtask to obtain the self-labeled ground truth masks by using an optical flow-based binary classifier and motion cue post-processing for transfer learning. Our system achieves 70% singulation success rate in simulated cluttered scenes. The interactive segmentation of our system achieves 87.8%, 73.9%, and 69.3% average precision for toy blocks, YCB objects in simulation and real-world novel objects, respectively, which outperforms several baselines.

</details>

### Self-supervised Learning for Real-World Super-Resolution from Dual Zoomed Observations.
- **链接**: [arXiv:2203.01325](https://arxiv.org/abs/2203.01325) · [代码](https://github.com/cszhilu1998/SelfDZSR)
- **作者**: Zhilu Zhang, Ruohao Wang, Hongzhi Zhang, Yunjin Chen, Wangmeng Zuo
- **🏷️ 机构**: Faculty of Computing, Harbin Institute of Technology, Harbin, Heilongjiang, China
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we consider two challenging issues in reference-based super-resolution (RefSR), (i) how to choose a proper reference image, and (ii) how to learn real-world RefSR in a self-supervised manner. Particularly, we present a novel self-supervised learning approach for real-world image SR from observations at dual camera zooms (SelfDZSR). Considering the popularity of multiple cameras in modern smartphones, the more zoomed (telephoto) image can be naturally leveraged as the reference to guide the SR of the lesser zoomed (short-focus) image. Furthermore, SelfDZSR learns a deep network to obtain the SR result of short-focus image to have the same resolution as the telephoto image. For this purpose, we take the telephoto image instead of an additional high-resolution image as the supervision information and select a center patch from it as the reference to super-resolve the corresponding short-focus image patch. To mitigate the effect of the misalignment between short-focus low-resolution (LR) image and telephoto ground-truth (GT) image, we design an auxiliary-LR generator and map the GT to an auxiliary-LR while keeping the spatial position unchanged. Then the auxiliary-LR can be utilized to deform the LR features by the proposed adaptive spatial transformer networks (AdaSTN), and match the Ref features to GT. During testing, SelfDZSR can be directly deployed to super-solve the whole short-focus image with the reference of telephoto image. Experiments show that our method achieves better quantitative and qualitative performance against state-of-the-arts. Codes are available at https://github.com/cszhilu1998/SelfDZSR.

</details>

### Decoupled Adversarial Contrastive Learning for Self-supervised Adversarial Robustness.
- **链接**: [arXiv:2207.10899](https://arxiv.org/abs/2207.10899) · [代码](https://github.com/pantheon5100/DeACL)
- **作者**: Chaoning Zhang, Kang Zhang, Chenshuang Zhang, Axi Niu, Jiu Feng, Chang D. Yoo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial training (AT) for robust representation learning and self-supervised learning (SSL) for unsupervised representation learning are two active research fields. Integrating AT into SSL, multiple prior works have accomplished a highly significant yet challenging task: learning robust representation without labels. A widely used framework is adversarial contrastive learning which couples AT and SSL, and thus constitute a very complex optimization problem. Inspired by the divide-and-conquer philosophy, we conjecture that it might be simplified as well as improved by solving two sub-problems: non-robust SSL and pseudo-supervised AT. This motivation shifts the focus of the task from seeking an optimal integrating strategy for a coupled problem to finding sub-solutions for sub-problems. With this said, this work discards prior practices of directly introducing AT to SSL frameworks and proposed a two-stage framework termed Decoupled Adversarial Contrastive Learning (DeACL). Extensive experimental results demonstrate that our DeACL achieves SOTA self-supervised adversarial robustness while significantly reducing the training time, which validates its effectiveness and efficiency. Moreover, our DeACL constitutes a more explainable solution, and its success also bridges the gap with semi-supervised AT for exploiting unlabeled samples for robust representation learning. The code is publicly accessible at https://github.com/pantheon5100/DeACL.

</details>

### PASS: Part-Aware Self-Supervised Pre-Training for Person Re-Identification.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19781-9_12) · 📚 被引 80
- **作者**: Kuan Zhu, Haiyun Guo, Tianyi Yan, Yousong Zhu, Jinqiao Wang, Ming Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### SPot-the-Difference Self-supervised Pre-training for Anomaly Detection and Segmentation.
- **链接**: [arXiv:2207.14315](https://arxiv.org/abs/2207.14315) · [代码](https://github.com/amazon-research/spot-diff) · 📚 被引 523
- **作者**: Yang Zou, Jongheon Jeong, Latha Pemula, Dongqing Zhang, Onkar Dabeer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual anomaly detection is commonly used in industrial quality inspection. In this paper, we present a new dataset as well as a new self-supervised learning method for ImageNet pre-training to improve anomaly detection and segmentation in 1-class and 2-class 5/10/high-shot training setups. We release the Visual Anomaly (VisA) Dataset consisting of 10,821 high-resolution color images (9,621 normal and 1,200 anomalous samples) covering 12 objects in 3 domains, making it the largest industrial anomaly detection dataset to date. Both image and pixel-level labels are provided. We also propose a new self-supervised framework - SPot-the-difference (SPD) - which can regularize contrastive self-supervised pre-training, such as SimSiam, MoCo and SimCLR, to be more suitable for anomaly detection tasks. Our experiments on VisA and MVTec-AD dataset show that SPD consistently improves these contrastive pre-training baselines and even the supervised pre-training. For example, SPD improves Area Under the Precision-Recall curve (AU-PR) for anomaly segmentation by 5.9% and 6.8% over SimSiam and supervised pre-training respectively in the 2-class high-shot regime. We open-source the project at http://github.com/amazon-research/spot-diff .

</details>

### 4DContrast: Contrastive Learning with Dynamic Correspondences for 3D Scene Understanding.
- **链接**: [arXiv:2112.02990](https://arxiv.org/abs/2112.02990)
- **作者**: Yujin Chen, Matthias Nießner, Angela Dai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new approach to instill 4D dynamic object priors into learned 3D representations by unsupervised pre-training. We observe that dynamic movement of an object through an environment provides important cues about its objectness, and thus propose to imbue learned 3D representations with such dynamic understanding, that can then be effectively transferred to improved performance in downstream 3D semantic scene understanding tasks. We propose a new data augmentation scheme leveraging synthetic 3D shapes moving in static 3D environments, and employ contrastive learning under 3D-4D constraints that encode 4D invariances into the learned 3D representations. Experiments demonstrate that our unsupervised representation learning results in improvement in downstream 3D semantic segmentation, object detection, and instance segmentation tasks, and moreover, notably improves performance in data-scarce scenarios.

</details>

### Fast-MoCo: Boost Momentum-Based Contrastive Learning with Combinatorial Patches.
- **链接**: [arXiv:2207.08220](https://arxiv.org/abs/2207.08220) · 📚 被引 19
- **作者**: Yuanzheng Ci, Chen Lin, Lei Bai, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive-based self-supervised learning methods achieved great success in recent years. However, self-supervision requires extremely long training epochs (e.g., 800 epochs for MoCo v3) to achieve promising results, which is unacceptable for the general academic community and hinders the development of this topic. This work revisits the momentum-based contrastive learning frameworks and identifies the inefficiency in which two augmented views generate only one positive pair. We propose Fast-MoCo - a novel framework that utilizes combinatorial patches to construct multiple positive pairs from two augmented views, which provides abundant supervision signals that bring significant acceleration with neglectable extra computational cost. Fast-MoCo trained with 100 epochs achieves 73.5% linear evaluation accuracy, similar to MoCo v3 (ResNet-50 backbone) trained with 800 epochs. Extra training (200 epochs) further improves the result to 75.1%, which is on par with state-of-the-art methods. Experiments on several downstream tasks also confirm the effectiveness of Fast-MoCo.

</details>

### Action-Based Contrastive Learning for Trajectory Prediction.
- **链接**: [arXiv:2207.08664](https://arxiv.org/abs/2207.08664)
- **作者**: Marah Halawa, Olaf Hellwich, Pia Bideau
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Trajectory prediction is an essential task for successful human robot interaction, such as in autonomous driving. In this work, we address the problem of predicting future pedestrian trajectories in a first person view setting with a moving camera. To that end, we propose a novel action-based contrastive learning loss, that utilizes pedestrian action information to improve the learned trajectory embeddings. The fundamental idea behind this new loss is that trajectories of pedestrians performing the same action should be closer to each other in the feature space than the trajectories of pedestrians with significantly different actions. In other words, we argue that behavioral information about pedestrian action influences their future trajectory. Furthermore, we introduce a novel sampling strategy for trajectories that is able to effectively increase negative and positive contrastive samples. Additional synthetic trajectory samples are generated using a trained Conditional Variational Autoencoder (CVAE), which is at the core of several models developed for trajectory prediction. Results show that our proposed contrastive framework employs contextual information about pedestrian behavior, i.e. action, effectively, and it learns a better trajectory representation. Thus, integrating the proposed contrastive framework within a trajectory prediction model improves its results and outperforms state-of-the-art methods on three trajectory prediction benchmarks [31, 32, 26].

</details>

### Bi-directional Contrastive Learning for Domain Adaptive Semantic Segmentation.
- **链接**: [arXiv:2207.10892](https://arxiv.org/abs/2207.10892) · 📚 被引 29
- **作者**: Geon Lee, Chanho Eom, Wonkyung Lee, Hyekang Park, Bumsub Ham
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel unsupervised domain adaptation method for semantic segmentation that generalizes a model trained with source images and corresponding ground-truth labels to a target domain. A key to domain adaptive semantic segmentation is to learn domain-invariant and discriminative features without target ground-truth labels. To this end, we propose a bi-directional pixel-prototype contrastive learning framework that minimizes intra-class variations of features for the same object class, while maximizing inter-class variations for different ones, regardless of domains. Specifically, our framework aligns pixel-level features and a prototype of the same object class in target and source images (i.e., positive pairs), respectively, sets them apart for different classes (i.e., negative pairs), and performs the alignment and separation processes toward the other direction with pixel-level features in the source image and a prototype in the target image. The cross-domain matching encourages domain-invariant feature representations, while the bidirectional pixel-prototype correspondences aggregate features for the same object class, providing discriminative features. To establish training pairs for contrastive learning, we propose to generate dynamic pseudo labels of target images using a non-parametric label transfer, that is, pixel-prototype correspondences across different domains. We also present a calibration method compensating class-wise domain biases of prototypes gradually during training.

</details>

### Contrastive Learning for Diverse Disentangled Foreground Generation.
- **链接**: [arXiv:2211.02707](https://arxiv.org/abs/2211.02707)
- **作者**: Yuheng Li, Yijun Li, Jingwan Lu, Eli Shechtman, Yong Jae Lee, Krishna Kumar Singh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a new method for diverse foreground generation with explicit control over various factors. Existing image inpainting based foreground generation methods often struggle to generate diverse results and rarely allow users to explicitly control specific factors of variation (e.g., varying the facial identity or expression for face inpainting results). We leverage contrastive learning with latent codes to generate diverse foreground results for the same masked input. Specifically, we define two sets of latent codes, where one controls a pre-defined factor (``known''), and the other controls the remaining factors (``unknown''). The sampled latent codes from the two sets jointly bi-modulate the convolution kernels to guide the generator to synthesize diverse results. Experiments demonstrate the superiority of our method over state-of-the-arts in result diversity and generation controllability.

</details>

### FakeCLR: Exploring Contrastive Learning for Solving Latent Discontinuity in Data-Efficient GANs.
- **链接**: [arXiv:2207.08630](https://arxiv.org/abs/2207.08630) · [代码](https://github.com/iceli1007/FakeCLR) · 📚 被引 22
- **作者**: Ziqiang Li, Chaoyue Wang, Heliang Zheng, Jing Zhang, Bin Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data-Efficient GANs (DE-GANs), which aim to learn generative models with a limited amount of training data, encounter several challenges for generating high-quality samples. Since data augmentation strategies have largely alleviated the training instability, how to further improve the generative performance of DE-GANs becomes a hotspot. Recently, contrastive learning has shown the great potential of increasing the synthesis quality of DE-GANs, yet related principles are not well explored. In this paper, we revisit and compare different contrastive learning strategies in DE-GANs, and identify (i) the current bottleneck of generative performance is the discontinuity of latent space; (ii) compared to other contrastive learning strategies, Instance-perturbation works towards latent space continuity, which brings the major improvement to DE-GANs. Based on these observations, we propose FakeCLR, which only applies contrastive learning on perturbed fake samples, and devises three related training techniques: Noise-related Latent Augmentation, Diversity-aware Queue, and Forgetting Factor of Queue. Our experimental results manifest the new state of the arts on both few-shot generation and limited-data generation. On multiple datasets, FakeCLR acquires more than 15% FID improvement compared to existing DE-GANs. Code is available at https://github.com/iceli1007/FakeCLR.

</details>

### Pairwise Contrastive Learning Network for Action Quality Assessment.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19772-7_27) · 📚 被引 31
- **作者**: Mingzhe Li, Hongbo Zhang, Qing Lei, Zongwen Fan, Jinghua Liu, Ji-Xiang Du
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Multi-scale and Cross-scale Contrastive Learning for Semantic Segmentation.
- **链接**: [arXiv:2203.13409](https://arxiv.org/abs/2203.13409) · [代码](https://github.com/RViMLab/MS_CS_ContrSeg) · 📚 被引 25
- **作者**: Theodoros Pissas, Claudio S. Ravasio, Lyndon Da Cruz, Christos Bergeles
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work considers supervised contrastive learning for semantic segmentation. We apply contrastive learning to enhance the discriminative power of the multi-scale features extracted by semantic segmentation networks. Our key methodological insight is to leverage samples from the feature spaces emanating from multiple stages of a model's encoder itself requiring neither data augmentation nor online memory banks to obtain a diverse set of samples. To allow for such an extension we introduce an efficient and effective sampling process, that enables applying contrastive losses over the encoder's features at multiple scales. Furthermore, by first mapping the encoder's multi-scale representations to a common feature space, we instantiate a novel form of supervised local-global constraint by introducing cross-scale contrastive learning linking high-resolution local features to low-resolution global features. Combined, our multi-scale and cross-scale contrastive losses boost performance of various models (DeepLabV3, HRNet, OCRNet, UPerNet) with both CNN and Transformer backbones, when evaluated on 4 diverse datasets from natural (Cityscapes, PascalContext, ADE20K) but also surgical (CaDIS) domains. Our code is available at https://github.com/RViMLab/MS_CS_ContrSeg. datasets from natural (Cityscapes, PascalContext, ADE20K) but also surgical (CaDIS) domains.

</details>

### Network Binarization via Contrastive Learning.
- **链接**: [arXiv:2207.02970](https://arxiv.org/abs/2207.02970) · 📚 被引 22
- **作者**: Yuzhang Shang, Dan Xu, Ziliang Zong, Liqiang Nie, Yan Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural network binarization accelerates deep models by quantizing their weights and activations into 1-bit. However, there is still a huge performance gap between Binary Neural Networks (BNNs) and their full-precision (FP) counterparts. As the quantization error caused by weights binarization has been reduced in earlier works, the activations binarization becomes the major obstacle for further improvement of the accuracy. BNN characterises a unique and interesting structure, where the binary and latent FP activations exist in the same forward pass (i.e., $\text{Binarize}(\mathbf{a}_F) = \mathbf{a}_B$). To mitigate the information degradation caused by the binarization operation from FP to binary activations, we establish a novel contrastive learning framework while training BNNs through the lens of Mutual Information (MI) maximization. MI is introduced as the metric to measure the information shared between binary and FP activations, which assists binarization with contrastive learning. Specifically, the representation ability of the BNNs is greatly strengthened via pulling the positive pairs with binary and FP activations from the same input samples, as well as pushing negative pairs from different samples (the number of negative pairs can be exponentially large). This benefits the downstream tasks, not only classification but also segmentation and depth estimation, etc. The experimental results show that our method can be implemented as a pile-up module on existing state-of-the-art binarization methods and can remarkably improve the performance over them on CIFAR-10/100 and ImageNet, in addition to the great generalization ability on NYUD-v2.

</details>

### Unifying Visual Contrastive Learning for Object Recognition from a Graph Perspective.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_37) · 📚 被引 2
- **作者**: Shixiang Tang, Feng Zhu, Lei Bai, Rui Zhao, Chenyu Wang, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### CODER: Coupled Diversity-Sensitive Momentum Contrastive Learning for Image-Text Retrieval.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_40)
- **作者**: Haoran Wang, Dongliang He, Wenhao Wu, Boyang Xia, Min Yang, Fu Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Hierarchical Semi-supervised Contrastive Learning for Contamination-Resistant Anomaly Detection.
- **链接**: [arXiv:2207.11789](https://arxiv.org/abs/2207.11789) · [代码](https://github.com/GaoangW/HSCL) · 📚 被引 10
- **作者**: Gaoang Wang, Yibing Zhan, Xinchao Wang, Mingli Song, Klara Nahrstedt
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection aims at identifying deviant samples from the normal data distribution. Contrastive learning has provided a successful way to sample representation that enables effective discrimination on anomalies. However, when contaminated with unlabeled abnormal samples in training set under semi-supervised settings, current contrastive-based methods generally 1) ignore the comprehensive relation between training data, leading to suboptimal performance, and 2) require fine-tuning, resulting in low efficiency. To address the above two issues, in this paper, we propose a novel hierarchical semi-supervised contrastive learning (HSCL) framework, for contamination-resistant anomaly detection. Specifically, HSCL hierarchically regulates three complementary relations: sample-to-sample, sample-to-prototype, and normal-to-abnormal relations, enlarging the discrimination between normal and abnormal samples with a comprehensive exploration of the contaminated data. Besides, HSCL is an end-to-end learning approach that can efficiently learn discriminative representations without fine-tuning. HSCL achieves state-of-the-art performance in multiple scenarios, such as one-class classification and cross-dataset detection. Extensive ablation studies further verify the effectiveness of each considered relation. The code is available at https://github.com/GaoangW/HSCL.

</details>

### Dual Contrastive Learning with Anatomical Auxiliary Supervision for Few-Shot Medical Image Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_24) · 📚 被引 49
- **作者**: Huisi Wu, Fangyan Xiao, Chongxin Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### MaCLR: Motion-Aware Contrastive Learning of Representations for Videos.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19833-5_21) · 📚 被引 7
- **作者**: Fanyi Xiao, Joseph Tighe, Davide Modolo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### ConCL: Concept Contrastive Learning for Dense Prediction Pre-training in Pathology Images.
- **链接**: [arXiv:2207.06733](https://arxiv.org/abs/2207.06733) · 📚 被引 19
- **作者**: Jiawei Yang, Hanbo Chen, Yuan Liang, Junzhou Huang, Lei He, Jianhua Yao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detectingandsegmentingobjectswithinwholeslideimagesis essential in computational pathology workflow. Self-supervised learning (SSL) is appealing to such annotation-heavy tasks. Despite the extensive benchmarks in natural images for dense tasks, such studies are, unfortunately, absent in current works for pathology. Our paper intends to narrow this gap. We first benchmark representative SSL methods for dense prediction tasks in pathology images. Then, we propose concept contrastive learning (ConCL), an SSL framework for dense pre-training. We explore how ConCL performs with concepts provided by different sources and end up with proposing a simple dependency-free concept generating method that does not rely on external segmentation algorithms or saliency detection models. Extensive experiments demonstrate the superiority of ConCL over previous state-of-the-art SSL methods across different settings. Along our exploration, we distll several important and intriguing components contributing to the success of dense pre-training for pathology images. We hope this work could provide useful data points and encourage the community to conduct ConCL pre-training for problems of interest. Code is available.

</details>

### Few-Shot Classification with Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_17)
- **作者**: Zhanyuan Yang, Jinghua Wang, Yingying Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Decoupled Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_38)
- **作者**: Chun-Hsiao Yeh, Cheng-Yao Hong, Yen-Chi Hsu, Tyng-Luh Liu, Yubei Chen, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Adversarial Contrastive Learning via Asymmetric InfoNCE.
- **链接**: [arXiv:2207.08374](https://arxiv.org/abs/2207.08374) · [代码](https://github.com/yqy2001/A-InfoNCE)
- **作者**: Qiying Yu, Jieming Lou, Xianyuan Zhan, Qizhang Li, Wangmeng Zuo, Yang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning (CL) has recently been applied to adversarial learning tasks. Such practice considers adversarial samples as additional positive views of an instance, and by maximizing their agreements with each other, yields better adversarial robustness. However, this mechanism can be potentially flawed, since adversarial perturbations may cause instance-level identity confusion, which can impede CL performance by pulling together different instances with separate identities. To address this issue, we propose to treat adversarial samples unequally when contrasted, with an asymmetric InfoNCE objective ($A-InfoNCE$) that allows discriminating considerations of adversarial samples. Specifically, adversaries are viewed as inferior positives that induce weaker learning signals, or as hard negatives exhibiting higher contrast to other negative samples. In the asymmetric fashion, the adverse impacts of conflicting objectives between CL and adversarial learning can be effectively mitigated. Experiments show that our approach consistently outperforms existing Adversarial CL methods across different finetuning schemes without additional computational cost. The proposed A-InfoNCE is also a generic form that can be readily extended to other CL methods. Code is available at https://github.com/yqy2001/A-InfoNCE.

</details>

### Few-Shot Action Recognition with Hierarchical Matching and Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19772-7_18) · 📚 被引 51
- **作者**: Sipeng Zheng, Shizhe Chen, Qin Jin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### What to Hide from Your Students: Attention-Guided Masked Image Modeling.
- **链接**: [arXiv:2203.12719](https://arxiv.org/abs/2203.12719) · [代码](https://github.com/gkakogeorgiou/attmask) · 📚 被引 90
- **作者**: Ioannis Kakogeorgiou, Spyros Gidaris, Bill Psomas, Yannis Avrithis, Andrei Bursuc, Konstantinos Karantzalos et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers and masked language modeling are quickly being adopted and explored in computer vision as vision transformers and masked image modeling (MIM). In this work, we argue that image token masking differs from token masking in text, due to the amount and correlation of tokens in an image. In particular, to generate a challenging pretext task for MIM, we advocate a shift from random masking to informed masking. We develop and exhibit this idea in the context of distillation-based MIM, where a teacher transformer encoder generates an attention map, which we use to guide masking for the student. We thus introduce a novel masking strategy, called attention-guided masking (AttMask), and we demonstrate its effectiveness over random masking for dense distillation-based MIM as well as plain distillation-based self-supervised learning on classification tokens. We confirm that AttMask accelerates the learning process and improves the performance on a variety of downstream tasks. We provide the implementation code at https://github.com/gkakogeorgiou/attmask.

</details>

### Improved Masked Image Generation with Token-Critic.
- **链接**: [arXiv:2209.04439](https://arxiv.org/abs/2209.04439) · 📚 被引 23
- **作者**: José Lezama, Huiwen Chang, Lu Jiang, Irfan Essa
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-autoregressive generative transformers recently demonstrated impressive image generation performance, and orders of magnitude faster sampling than their autoregressive counterparts. However, optimal parallel sampling from the true joint distribution of visual tokens remains an open challenge. In this paper we introduce Token-Critic, an auxiliary model to guide the sampling of a non-autoregressive generative transformer. Given a masked-and-reconstructed real image, the Token-Critic model is trained to distinguish which visual tokens belong to the original image and which were sampled by the generative transformer. During non-autoregressive iterative sampling, Token-Critic is used to select which tokens to accept and which to reject and resample. Coupled with Token-Critic, a state-of-the-art generative transformer significantly improves its performance, and outperforms recent diffusion models and GANs in terms of the trade-off between generated image quality and diversity, in the challenging class-conditional ImageNet generation.

</details>

## 跨领域论文（完整笔记在其他领域）

- Object Discovery via Contrastive Learning for Weakly Supervised Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Exploring Resolution and Degradation Clues as Self-supervised Signal for Low Quality Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone. → [3d-detection](../3d-detection/Guideline%202022.md)
- KD-MVS: Knowledge Distillation Based Self-supervised Learning for Multi-view Stereo. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Emotion-aware Multi-view Contrastive Learning for Facial Emotion Recognition. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- RA-Depth: Resolution Adaptive Self-supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Towards Comprehensive Representation Enhancement in Semantics-Guided Self-supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Self-distilled Feature Aggregation for Self-supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Learning Mutual Modulation for Self-supervised Cross-Modal Super-Resolution. → [multimodal](../multimodal/Guideline%202022.md)
- S3C: Self-Supervised Stochastic Classifiers for Few-Shot Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- CMD: Self-supervised 3D Action Representation Learning with Cross-Modal Mutual Distillation. → [multimodal](../multimodal/Guideline%202022.md)
