# Multi-camera Perception — 2021 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multi-View Multi-Person 3D Pose Estimation With Plane Sweep Stereo.
- **链接**: [arXiv:2104.02273](https://arxiv.org/abs/2104.02273) · [代码](https://github.com/jiahaoLjh/PlaneSweepPose) · 📚 被引 69
- **作者**: Jiahao Lin, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing approaches for multi-view multi-person 3D pose estimation explicitly establish cross-view correspondences to group 2D pose detections from multiple camera views and solve for the 3D pose estimation for each person. Establishing cross-view correspondences is challenging in multi-person scenes, and incorrect correspondences will lead to sub-optimal performance for the multi-stage pipeline. In this work, we present our multi-view 3D pose estimation approach based on plane sweep stereo to jointly address the cross-view fusion and 3D pose reconstruction in a single shot. Specifically, we propose to perform depth regression for each joint of each 2D pose in a target camera view. Cross-view consistency constraints are implicitly enforced by multiple reference camera views via the plane sweep algorithm to facilitate accurate depth regression. We adopt a coarse-to-fine scheme to first regress the person-level depth followed by a per-person joint-level relative depth estimation. 3D poses are obtained from a simple back-projection given the estimated depths. We evaluate our approach on benchmark datasets where it outperforms previous state-of-the-arts while being remarkably efficient. Our code is available at https://github.com/jiahaoLjh/PlaneSweepPose.

</details>

### Cross-View Cross-Scene Multi-View Crowd Counting.
- **链接**: [arXiv:2205.01551](https://arxiv.org/abs/2205.01551) · 📚 被引 68
- **作者**: Qi Zhang, Wei Lin, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view crowd counting has been previously proposed to utilize multi-cameras to extend the field-of-view of a single camera, capturing more people in the scene, and improve counting performance for occluded people or those in low resolution. However, the current multi-view paradigm trains and tests on the same single scene and camera-views, which limits its practical application. In this paper, we propose a cross-view cross-scene (CVCS) multi-view crowd counting paradigm, where the training and testing occur on different scenes with arbitrary camera layouts. To dynamically handle the challenge of optimal view fusion under scene and camera layout change and non-correspondence noise due to camera calibration errors or erroneous features, we propose a CVCS model that attentively selects and fuses multiple views together using camera layout geometry, and a noise view regularization method to train the model to handle non-correspondence errors. We also generate a large synthetic multi-camera crowd counting dataset with a large number of scenes and camera views to capture many possible variations, which avoids the difficulty of collecting and annotating such a large real dataset. We then test our trained CVCS model on real multi-view counting datasets, by using unsupervised domain transfer. The proposed CVCS model trained on synthetic data outperforms the same model trained only on real data, and achieves promising performance compared to fully supervised methods that train and test on the same single scene.

</details>

### COMPLETER: Incomplete Multi-View Clustering via Contrastive Prediction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Lin_COMPLETER_Incomplete_Multi-View_Clustering_via_Contrastive_Prediction_CVPR_2021_paper.html) · 📚 被引 405
- **作者**: Yijie Lin, Yuanbiao Gou, Zitao Liu, Boyun Li, Jiancheng Lv, Xi Peng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Multi-View 3D Reconstruction of a Texture-Less Smooth Surface of Unknown Generic Reflectance.
- **链接**: [arXiv:2105.11599](https://arxiv.org/abs/2105.11599) · 📚 被引 22
- **作者**: Ziang Cheng, Hongdong Li, Yuta Asano, Yinqiang Zheng, Imari Sato
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recovering the 3D geometry of a purely texture-less object with generally unknown surface reflectance (e.g. non-Lambertian) is regarded as a challenging task in multi-view reconstruction. The major obstacle revolves around establishing cross-view correspondences where photometric constancy is violated. This paper proposes a simple and practical solution to overcome this challenge based on a co-located camera-light scanner device. Unlike existing solutions, we do not explicitly solve for correspondence. Instead, we argue the problem is generally well-posed by multi-view geometrical and photometric constraints, and can be solved from a small number of input views. We formulate the reconstruction task as a joint energy minimization over the surface geometry and reflectance. Despite this energy is highly non-convex, we develop an optimization algorithm that robustly recovers globally optimal shape and reflectance even from a random initialization. Extensive experiments on both simulated and real data have validated our method, and possible future extensions are discussed.

</details>

### DeepVideoMVS: Multi-View Stereo on Video With Recurrent Spatio-Temporal Fusion.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Duzceker_DeepVideoMVS_Multi-View_Stereo_on_Video_With_Recurrent_Spatio-Temporal_Fusion_CVPR_2021_paper.html)
- **作者**: Arda Düzçeker, Silvano Galliani, Christoph Vogel, Pablo Speciale, Mihai Dusmanu, Marc Pollefeys
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Recurrent Multi-View Alignment Network for Unsupervised Surface Registration.
- **链接**: [arXiv:2011.12104](https://arxiv.org/abs/2011.12104) · [代码](https://github.com/WanquanF/RMA-Net) · 📚 被引 47
- **作者**: Wanquan Feng, Juyong Zhang, Hongrui Cai, Haofei Xu, Junhui Hou, Hujun Bao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Multi-View Representation Learning via Total Correlation Objective.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/65a99bb7a3115fdede20da98b08a370f-Abstract.html)
- **作者**: HyeongJoo Hwang, Geon-Hyeong Kim, Seunghoon Hong, Kee-Eung Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Multi-view Contrastive Graph Clustering.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/10c66082c124f8afe3df4886f5e516e0-Abstract.html)
- **作者**: Erlin Pan, Zhao Kang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Differentiable Diffusion for Dense Depth Estimation From Multi-View Images.
- **链接**: [arXiv:2106.08917](https://arxiv.org/abs/2106.08917) · 📚 被引 17
- **作者**: Numair Khan, Min H. Kim, James Tompkin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method to estimate dense depth by optimizing a sparse set of points such that their diffusion into a depth map minimizes a multi-view reprojection error from RGB supervision. We optimize point positions, depths, and weights with respect to the loss by differential splatting that models points as Gaussians with analytic transmittance. Further, we develop an efficient optimization routine that can simultaneously optimize the 50k+ points required for complex scene reconstruction. We validate our routine using ground truth data and show high reconstruction quality. Then, we apply this to light field and wider baseline images via self supervision, and show improvements in both average and outlier error for depth maps diffused from inaccurate sparse points. Finally, we compare qualitative and quantitative results to image processing and deep learning methods. http://visual.cs.brown.edu/diffdiffdepth

</details>

### Multi-view Depth Estimation using Epipolar Spatio-Temporal Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Long_Multi-view_Depth_Estimation_using_Epipolar_Spatio-Temporal_Networks_CVPR_2021_paper.html) · 📚 被引 55
- **作者**: Xiaoxiao Long, Lingjie Liu, Wei Li, Christian Theobalt, Wenping Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Reconsidering Representation Alignment for Multi-View Clustering.
- **链接**: [arXiv:2103.07738](https://arxiv.org/abs/2103.07738) · 📚 被引 220
- **作者**: Daniel J. Trosten, Sigurd Løkse, Robert Jenssen, Michael Kampffmeyer
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### MVTN: Multi-View Transformation Network for 3D Shape Recognition.
- **链接**: [arXiv:2011.13244](https://arxiv.org/abs/2011.13244) · [代码](https://github.com/ajhamdi/MVTN) · 📚 被引 219
- **作者**: Abdullah Hamdi, Silvio Giancola, Bernard Ghanem
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST),Thuwal,Saudi Arabia
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view projection methods have demonstrated their ability to reach state-of-the-art performance on 3D shape recognition. Those methods learn different ways to aggregate information from multiple views. However, the camera view-points for those views tend to be heuristically set and fixed for all shapes. To circumvent the lack of dynamism of current multi-view methods, we propose to learn those view-points. In particular, we introduce the Multi-View Transformation Network (MVTN) that regresses optimal view-points for 3D shape recognition, building upon advances in differentiable rendering. As a result, MVTN can be trained end-to-end along with any multi-view network for 3D shape classification. We integrate MVTN in a novel adaptive multi-view pipeline that can render either 3D meshes or point clouds. MVTN exhibits clear performance gains in the tasks of 3D shape classification and 3D shape retrieval without the need for extra training supervision. In these tasks, MVTN achieves state-of-the-art performance on ModelNet40, ShapeNet Core55, and the most recent and realistic ScanObjectNN dataset (up to 6% improvement). Interestingly, we also show that MVTN can provide network robustness against rotation and occlusion in the 3D domain. The code is available at https://github.com/ajhamdi/MVTN .

</details>

### PatchmatchNet: Learned Multi-View Patchmatch Stereo.
- **链接**: [arXiv:2012.01411](https://arxiv.org/abs/2012.01411) · 📚 被引 380
- **作者**: Fangjinhua Wang, Silvano Galliani, Christoph Vogel, Pablo Speciale, Marc Pollefeys
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present PatchmatchNet, a novel and learnable cascade formulation of Patchmatch for high-resolution multi-view stereo. With high computation speed and low memory requirement, PatchmatchNet can process higher resolution imagery and is more suited to run on resource limited devices than competitors that employ 3D cost volume regularization. For the first time we introduce an iterative multi-scale Patchmatch in an end-to-end trainable architecture and improve the Patchmatch core algorithm with a novel and learned adaptive propagation and evaluation scheme for each iteration. Extensive experiments show a very competitive performance and generalization for our method on DTU, Tanks & Temples and ETH3D, but at a significantly higher efficiency than all existing top-performing models: at least two and a half times faster than state-of-the-art methods with twice less memory usage.

</details>

### IBRNet: Learning Multi-View Image-Based Rendering.
- **链接**: [arXiv:2102.13090](https://arxiv.org/abs/2102.13090) · 📚 被引 677
- **作者**: Qianqian Wang, Zhicheng Wang, Kyle Genova, Pratul P. Srinivasan, Howard Zhou, Jonathan T. Barron et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method that synthesizes novel views of complex scenes by interpolating a sparse set of nearby views. The core of our method is a network architecture that includes a multilayer perceptron and a ray transformer that estimates radiance and volume density at continuous 5D locations (3D spatial locations and 2D viewing directions), drawing appearance information on the fly from multiple source views. By drawing on source views at render time, our method hearkens back to classic work on image-based rendering (IBR), and allows us to render high-resolution imagery. Unlike neural scene representation work that optimizes per-scene functions for rendering, we learn a generic view interpolation function that generalizes to novel scenes. We render images using classic volume rendering, which is fully differentiable and allows us to train using only multi-view posed images as supervision. Experiments show that our method outperforms recent novel view synthesis methods that also seek to generalize to novel scenes. Further, if fine-tuned on each scene, our method is competitive with state-of-the-art single-scene neural rendering methods. Project page: https://ibrnet.github.io/

</details>

### Self-Supervised Learning of Depth Inference for Multi-View Stereo.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_Self-Supervised_Learning_of_Depth_Inference_for_Multi-View_Stereo_CVPR_2021_paper.html) · 📚 被引 55
- **作者**: Jiayu Yang, José M. Álvarez, Miaomiao Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### DyGLIP: A Dynamic Graph Model With Link Prediction for Accurate Multi-Camera Multiple Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Quach_DyGLIP_A_Dynamic_Graph_Model_With_Link_Prediction_for_Accurate_CVPR_2021_paper.html)
- **作者**: Kha Gia Quach, Pha A. Nguyen, Huu Le, Thanh-Dat Truong, Chi Nhan Duong, Minh-Triet Tran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Wide-Baseline Multi-Camera Calibration Using Person Re-Identification.
- **链接**: [arXiv:2104.08568](https://arxiv.org/abs/2104.08568) · 📚 被引 26
- **作者**: Yan Xu, Yu-Jhe Li, Xinshuo Weng, Kris Kitani
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised depth estimation for indoor environments is more challenging than its outdoor counterpart in at least the following two aspects: (i) the depth range of indoor sequences varies a lot across different frames, making it difficult for the depth network to induce consistent depth cues, whereas the maximum distance in outdoor scenes mostly stays the same as the camera usually sees the sky; (ii) the indoor sequences contain much more rotational motions, which cause difficulties for the pose network, while the motions of outdoor sequences are pre-dominantly translational, especially for driving datasets such as KITTI. In this paper, special considerations are given to those challenges and a set of good practices are consolidated for improving the performance of self-supervised monocular depth estimation in indoor environments. The proposed method mainly consists of two novel modules, \ie, a depth factorization module and a residual pose estimation module, each of which is designed to respectively tackle the aforementioned challenges. The effectiveness of each module is shown through a carefully conducted ablation study and the demonstration of the state-of-the-art performance on three indoor datasets, \ie, EuRoC, NYUv2, and 7-scenes.

</details>

### Monocular Depth Estimation via Listwise Ranking Using the Plackett-Luce Model.
- **链接**: [arXiv:2010.13118](https://arxiv.org/abs/2010.13118) · 📚 被引 12
- **作者**: Julian Lienen, Eyke Hüllermeier, Ralph Ewerth, Nils Nommensen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In many real-world applications, the relative depth of objects in an image is crucial for scene understanding. Recent approaches mainly tackle the problem of depth prediction in monocular images by treating the problem as a regression task. Yet, being interested in an order relation in the first place, ranking methods suggest themselves as a natural alternative to regression, and indeed, ranking approaches leveraging pairwise comparisons as training information ("object A is closer to the camera than B") have shown promising performance on this problem. In this paper, we elaborate on the use of so-called listwise ranking as a generalization of the pairwise approach. Our method is based on the Plackett-Luce (PL) model, a probability distribution on rankings, which we combine with a state-of-the-art neural network architecture and a simple sampling strategy to reduce training complexity. Moreover, taking advantage of the representation of PL as a random utility model, the proposed predictor offers a natural way to recover (shift-invariant) metric depth information from ranking-only data provided at training time. An empirical evaluation on several benchmark datasets in a "zero-shot" setting demonstrates the effectiveness of our approach compared to existing ranking and regression methods.

</details>

### Boosting Monocular Depth Estimation Models to High-Resolution via Content-Adaptive Multi-Resolution Merging.
- **链接**: [arXiv:2105.14021](https://arxiv.org/abs/2105.14021) · 📚 被引 145
- **作者**: S. Mahdi H. Miangoleh, Sebastian Dille, Long Mai, Sylvain Paris, Yagiz Aksoy
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

</details>

### Three Ways To Improve Semantic Segmentation With Self-Supervised Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hoyer_Three_Ways_To_Improve_Semantic_Segmentation_With_Self-Supervised_Depth_Estimation_CVPR_2021_paper.html) · 📚 被引 76
- **作者**: Lukas Hoyer, Dengxin Dai, Yuhua Chen, Adrian Köring, Suman Saha, Luc Van Gool
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

## 🆕 增量新增

### 3D-MAN: 3D Multi-Frame Attention Network for Object Detection. **⭐⭐⭐⭐** (相关度: 88%)
- **链接**: [arXiv:2103.16054](https://arxiv.org/abs/2103.16054) · 📚 被引 111
- **作者**: Zetong Yang, Yin Zhou, Zhifeng Chen, Jiquan Ngiam
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对3D目标检测中多帧信息利用不足的问题，提出3D-MAN多帧注意力网络。方法使用快速单帧检测器生成提议，存储于记忆库，并通过多视角对齐和聚合模块利用注意力网络提取时序特征。在Waymo开放数据集上达到最先进性能，优于现有单帧和多帧方法。
- **摘要（英）**: This paper proposes 3D-MAN, a multi-frame attention network for 3D detection, aggregating features from multiple perspectives via a memory bank and attention-based alignment. It achieves state-of-the-art results on Waymo Open Dataset, outperforming both single-frame and multi-frame methods.
- **核心贡献**: 提出3D-MAN网络，通过多帧注意力聚合提升3D检测精度。
- **创新点**: 设计多视角对齐和聚合模块，结合记忆库实现高效时序特征融合。
- **结果**: 在Waymo数据集上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is an important module in autonomous driving and robotics. However, many existing methods focus on using single frames to perform 3D detection, and do not fully utilize information from multiple frames. In this paper, we present 3D-MAN: a 3D multi-frame attention network that effectively aggregates features from multiple perspectives and achieves state-of-the-art performance on Waymo Open Dataset. 3D-MAN first uses a novel fast single-frame detector to produce box proposals. The box proposals and their corresponding feature maps are then stored in a memory bank. We design a multi-view alignment and aggregation module, using attention networks, to extract and aggregate the temporal features stored in the memory bank. This effectively combines the features coming from different perspectives of the scene. We demonstrate the effectiveness of our approach on the large-scale complex Waymo Open Dataset, achieving state-of-the-art results compared to published single-frame and multi-frame methods.

</details>

### Trusted Multi-View Classification. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openreview.net/forum?id=OOsR8BzCnl5)
- **作者**: Zongbo Han, Changqing Zhang, Huazhu Fu, Joey Tianyi Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021
- **摘要（中）**: 该论文标题为“可信多视图分类”，但摘要内容缺失，无法评估其具体问题、方法、改进和效果。可能涉及多视图数据分类中的可靠性或不确定性处理，但缺乏详细信息。
- **摘要（英）**: The paper titled 'Trusted Multi-View Classification' lacks an abstract, preventing assessment of its problem, method, and results. It likely addresses reliability in multi-view classification, but details are unavailable.
- **核心贡献**: 无法确定，因摘要缺失。
- **创新点**: 无法确定，因摘要缺失。
- **结果**: 无法确定，因摘要缺失。

### Real-Time and Accurate Self-Supervised Monocular Depth Estimation on Mobile Device. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://proceedings.mlr.press/v176/cai22a.html)
- **作者**: Hong Cai, Fei Yin, Tushar Singhal, Sandeep Pendyam, Parham Noorzad, Yinhao Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①这篇论文针对移动设备上实时且准确的自监督单目深度估计问题，但摘要内容缺失，无法具体判断其研究细节。②由于摘要未提供，无法得知具体方法或实验内容。③缺乏摘要信息，无法评估其相比已有工作的改进点。④由于摘要缺失，无法引用具体数据或效果。
- **摘要（英）**: This paper focuses on real-time and accurate self-supervised monocular depth estimation on mobile devices, but the abstract is missing, preventing a detailed assessment of its problem, method, and results. No specific contributions or experimental data can be extracted.
- **核心贡献**: 核心贡献不明确，因摘要缺失。
- **创新点**: 创新点不明确，因摘要缺失。
- **结果**: 效果不明确，因摘要缺失。

### SubTab: Subsetting Features of Tabular Data for Self-Supervised Representation Learning. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2110.04361](https://arxiv.org/abs/2110.04361)
- **作者**: Talip Ucar, Ehsan Hajiramezanali, Lindsay Edwards
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
- **摘要（中）**: ①这篇论文针对表格数据中自监督学习难以设计有效数据增强方法的问题，因为表格数据缺乏图像、音频等数据的空间、时间或语义结构。②提出了SubTab框架，通过将输入特征划分为多个子集，将表格数据学习转化为多视角表示学习问题，并在自编码器设置中从特征子集重建数据，而非使用损坏版本。③相比已有工作，SubTab利用特征子集重建而非数据损坏，能更好地捕获潜在表示，并引入协作推理机制，在测试时聚合子集的潜在变量作为联合表示。④实验表明SubTab在多个表格数据集上达到了最先进性能，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the challenge of self-supervised learning on tabular data, where designing effective augmentations is difficult due to the lack of spatial, temporal, or semantic structure. It proposes SubTab, a framework that divides input features into subsets to transform tabular learning into a multi-view representation learning problem, reconstructing data from feature subsets rather than corrupted versions. The method introduces collaborative inference to aggregate latent variables at test time, and experiments show state-of-the-art performance on multiple tabular datasets, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出了SubTab框架，通过特征子集划分实现表格数据的自监督多视角表示学习。
- **创新点**: 创新性地利用特征子集重建替代数据损坏，并引入协作推理机制。
- **结果**: 在多个表格数据集上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has been shown to be very effective in learning useful representations, and yet much of the success is achieved in data types such as images, audio, and text. The success is mainly enabled by taking advantage of spatial, temporal, or semantic structure in the data through augmentation. However, such structure may not exist in tabular datasets commonly used in fields such as healthcare, making it difficult to design an effective augmentation method, and hindering a similar progress in tabular data setting. In this paper, we introduce a new framework, Subsetting features of Tabular data (SubTab), that turns the task of learning from tabular data into a multi-view representation learning problem by dividing the input features to multiple subsets. We argue that reconstructing the data from the subset of its features rather than its corrupted version in an autoencoder setting can better capture its underlying latent representation. In this framework, the joint representation can be expressed as the aggregate of latent variables of the subsets at test time, which we refer to as collaborative inference. Our experiments show that the SubTab achieves the state of the art (SOTA) performance of 98.31% on MNIST in tabular setting, on par with CNN-based SOTA models, and surpasses existing baselines on three other real-world datasets by a significant margin.

</details>

## 跨领域论文（完整笔记在其他领域）

- Self-Supervised Learning of Depth Inference for Multi-View Stereo. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- STaR: Self-Supervised Tracking and Reconstruction of Rigid Objects in Motion With Neural Rendering. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Self-supervised Learning from a Multi-view Perspective. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
<!-- COMPLETE v1 papers=24 -->
