# Multi-camera Perception — 2024 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MMVR: Millimeter-Wave Multi-view Radar Dataset and Benchmark for Indoor Perception.
- **链接**: [arXiv:2406.10708](https://arxiv.org/abs/2406.10708) · 📚 被引 11
- **作者**: Mohammad Mahbubur Rahman, Ryoma Yataka, Sorachi Kato, Pu Wang, Peizhao Li, Adriano Cardace et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared with an extensive list of automotive radar datasets that support autonomous driving, indoor radar datasets are scarce at a smaller scale in the format of low-resolution radar point clouds and usually under an open-space single-room setting. In this paper, we scale up indoor radar data collection using multi-view high-resolution radar heatmap in a multi-day, multi-room, and multi-subject setting, with an emphasis on the diversity of environment and subjects. Referred to as the millimeter-wave multi-view radar (MMVR) dataset, it consists of $345$K multi-view radar frames collected from $25$ human subjects over $6$ different rooms, $446$K annotated bounding boxes/segmentation instances, and $7.59$ million annotated keypoints to support three major perception tasks of object detection, pose estimation, and instance segmentation, respectively. For each task, we report performance benchmarks under two protocols: a single subject in an open space and multiple subjects in several cluttered rooms with two data splits: random split and cross-environment split over $395$ 1-min data segments. We anticipate that MMVR facilitates indoor radar perception development for indoor vehicle (robot/humanoid) navigation, building energy management, and elderly care for better efficiency, user experience, and safety. The MMVR dataset is available at https://doi.org/10.5281/zenodo.12611978.

</details>

### FroSSL: Frobenius Norm Minimization for Efficient Multiview Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73024-5_5)
- **作者**: Oscar Skean, Aayush Dhakal, Nathan Jacobs, Luis Gonzalo Sánchez Giraldo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### UniCorn: A Unified Contrastive Learning Approach for Multi-view Molecular Representation Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/feng24f.html)
- **作者**: Shikun Feng, Yuyan Ni, Minghao Li, Yanwen Huang, Zhi-Ming Ma, Wei-Ying Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

> Multi-view crowd localization predicts the ground locations of all people in the scene. Typical methods usually estimate the crowd density maps on the ground plane first, and then obtain the crowd locations. However, the performance of existing methods is limited by the ambiguity of the density maps in crowded areas, where local peaks can be smoothed away. To mitigate the weakness of density map supervision, optimal transport-based point supervision methods have been proposed in the single-image crowd localization tasks, but have not been explored for multi-view crowd localization yet. Thus, in this paper, we propose a novel Mahalanobis distance-based multi-view optimal transport (M-MVOT) loss specifically designed for multi-view crowd localization. First, we replace the Euclidean-based transport cost with the Mahalanobis distance, which defines elliptical iso-contours in the cost function whose long-axis and short-axis directions are guided by the view ray direction. Second, the object-to-camera distance in each view is used to adjust the optimal transport cost of each location further, where the wrong predictions far away from the camera are more heavily penalized. Finally, we propose a strategy to consider all the input camera views in the model loss (M-MVOT) by computing the optimal transport cost for each ground-truth point based on its closest camera. Experiments demonstrate the advantage of the proposed method over density map-based or common Euclidean distance-based optimal transport loss on several multi-view crowd localization datasets. Project page: https://vcc.tech/research/2024/MVOT.

### Adversarially Robust Deep Multi-View Clustering: A Novel Attack and Defense Framework.
- **链接**: [出版页](https://proceedings.mlr.press/v235/huang24ai.html)
- **作者**: Haonan Huang, Guoxu Zhou, Yanghang Zheng, Yuning Qiu, Andong Wang, Qibin Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### CAT3D: Create Anything in 3D with Multi-View Diffusion Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/89e4433fec4b99f1d859db57af1e0a0f-Abstract-Conference.html) · 📚 被引 31
- **作者**: Ruiqi Gao, Aleksander Holynski, Philipp Henzler, Arthur Brussee, Ricardo Martin-Brualla, Pratul P. Srinivasan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Immersive scene generation, notably panorama creation, benefits significantly from the adaptation of large pre-trained text-to-image (T2I) models for multi-view image generation. Due to the high cost of acquiring multi-view images, tuning-free generation is preferred. However, existing methods are either limited to simple correspondences or require extensive fine-tuning to capture complex ones. We present PanoFree, a novel method for tuning-free multi-view image generation that supports an extensive array of correspondences. PanoFree sequentially generates multi-view images using iterative warping and inpainting, addressing the key issues of inconsistency and artifacts from error accumulation without the need for fine-tuning. It improves error accumulation by enhancing cross-view awareness and refines the warping and inpainting processes via cross-view guidance, risky area estimation and erasing, and symmetric bidirectional guided generation for loop closure, alongside guidance-based semantic and density control for scene structure preservation. In experiments on Planar, 360°, and Full Spherical Panoramas, PanoFree demonstrates significant error reduction, improves global consistency, and boosts image quality without extra fine-tuning. Compared to existing methods, PanoFree is up to 5x more efficient in time and 3x more efficient in GPU memory usage, and maintains superior diversity of results (2x better in our user study). PanoFree offers a viable alternative to costly fine-tuning or the use of additional pre-trained models. Project website at https://panofree.github.io/.

</details>

### EgoSim: An Egocentric Multi-view Simulator and Real Dataset for Body-worn Cameras during Motion and Activity.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c1017d0a006d31dfbfd4cf1e9189d747-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 2
- **作者**: Dominik Hollidt, Paul Streli, Jiaxi Jiang, Yasaman Haghighi, Changlin Qian, Xintong Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of editing 3D objects and scenes based on open-ended language instructions. A common approach to this problem is to use a 2D image generator or editor to guide the 3D editing process, obviating the need for 3D data. However, this process is often inefficient due to the need for iterative updates of costly 3D representations, such as neural radiance fields, either through individual view edits or score distillation sampling. A major disadvantage of this approach is the slow convergence caused by aggregating inconsistent information across views, as the guidance from 2D models is not multi-view consistent. We thus introduce the Direct Gaussian Editor (DGE), a method that addresses these issues in two stages. First, we modify a given high-quality image editor like InstructPix2Pix to be multi-view consistent. To do so, we propose a training-free approach that integrates cues from the 3D geometry of the underlying scene. Second, given a multi-view consistent edited sequence of images, we directly and efficiently optimize the 3D representation, which is based on 3D Gaussian Splatting. Because it avoids incremental and iterative edits, DGE is significantly more accurate and efficient than existing approaches and offers additional benefits, such as enabling selective editing of parts of the scene.

</details>

> We present MV2Cyl, a novel method for reconstructing 3D from 2D multi-view images, not merely as a field or raw geometry but as a sketch-extrude CAD model. Extracting extrusion cylinders from raw 3D geometry has been extensively researched in computer vision, while the processing of 3D data through neural networks has remained a bottleneck. Since 3D scans are generally accompanied by multi-view images, leveraging 2D convolutional neural networks allows these images to be exploited as a rich source for extracting extrusion cylinder information. However, we observe that extracting only the surface information of the extrudes and utilizing it results in suboptimal outcomes due to the challenges in the occlusion and surface segmentation. By synergizing with the extracted base curve information, we achieve the optimal reconstruction result with the best accuracy in 2D sketch and extrude parameter estimation. Our experiments, comparing our method with previous work that takes a raw 3D point cloud as input, demonstrate the effectiveness of our approach by taking advantage of multi-view images. Our project page can be found at http://mv2cyl.github.io .

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MVSplat, an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians. To accurately localize the Gaussian centers, we build a cost volume representation via plane sweeping, where the cross-view feature similarities stored in the cost volume can provide valuable geometry cues to the estimation of depth. We also learn other Gaussian primitives' parameters jointly with the Gaussian centers while only relying on photometric supervision. We demonstrate the importance of the cost volume representation in learning feed-forward Gaussians via extensive experimental evaluations. On the large-scale RealEstate10K and ACID benchmarks, MVSplat achieves state-of-the-art performance with the fastest feed-forward inference speed (22~fps). More impressively, compared to the latest state-of-the-art method pixelSplat, MVSplat uses $10\times$ fewer parameters and infers more than $2\times$ faster while providing higher appearance and geometry quality as well as better cross-dataset generalization.

</details>

### MeshAvatar: Learning High-Quality Triangular Human Avatars from Multi-view Videos.
- **链接**: [arXiv:2407.08414](https://arxiv.org/abs/2407.08414) · 📚 被引 21
- **作者**: Yushuo Chen, Zerong Zheng, Zhe Li, Chao Xu, Yebin Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel pipeline for learning high-quality triangular human avatars from multi-view videos. Recent methods for avatar learning are typically based on neural radiance fields (NeRF), which is not compatible with traditional graphics pipeline and poses great challenges for operations like editing or synthesizing under different environments. To overcome these limitations, our method represents the avatar with an explicit triangular mesh extracted from an implicit SDF field, complemented by an implicit material field conditioned on given poses. Leveraging this triangular avatar representation, we incorporate physics-based rendering to accurately decompose geometry and texture. To enhance both the geometric and appearance details, we further employ a 2D UNet as the network backbone and introduce pseudo normal ground-truth as additional supervision. Experiments show that our method can learn triangular avatars with high-quality geometry reconstruction and plausible material decomposition, inherently supporting editing, manipulation or relighting operations.

</details>

### Portrait4D-V2: Pseudo Multi-view Data Creates Better 4D Head Synthesizer.
- **链接**: [arXiv:2403.13570](https://arxiv.org/abs/2403.13570) · 📚 被引 28
- **作者**: Yu Deng, Duomin Wang, Baoyuan Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel learning approach for feed-forward one-shot 4D head avatar synthesis. Different from existing methods that often learn from reconstructing monocular videos guided by 3DMM, we employ pseudo multi-view videos to learn a 4D head synthesizer in a data-driven manner, avoiding reliance on inaccurate 3DMM reconstruction that could be detrimental to the synthesis performance. The key idea is to first learn a 3D head synthesizer using synthetic multi-view images to convert monocular real videos into multi-view ones, and then utilize the pseudo multi-view videos to learn a 4D head synthesizer via cross-view self-reenactment. By leveraging a simple vision transformer backbone with motion-aware cross-attentions, our method exhibits superior performance compared to previous methods in terms of reconstruction fidelity, geometry consistency, and motion control accuracy. We hope our method offers novel insights into integrating 3D priors with 2D supervisions for improved 4D head avatar creation.

</details>

### Sur2f: A Hybrid Representation for High-Quality and Efficient Surface Reconstruction from Multi-view Images.
- **链接**: [arXiv:2401.03704](https://arxiv.org/abs/2401.03704) · 📚 被引 7
- **作者**: Zhangjin Huang, Zhihao Liang, Kui Jia
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view surface reconstruction is an ill-posed, inverse problem in 3D vision research. It involves modeling the geometry and appearance with appropriate surface representations. Most of the existing methods rely either on explicit meshes, using surface rendering of meshes for reconstruction, or on implicit field functions, using volume rendering of the fields for reconstruction. The two types of representations in fact have their respective merits. In this work, we propose a new hybrid representation, termed Sur2f, aiming to better benefit from both representations in a complementary manner. Technically, we learn two parallel streams of an implicit signed distance field and an explicit surrogate surface Sur2f mesh, and unify volume rendering of the implicit signed distance function (SDF) and surface rendering of the surrogate mesh with a shared, neural shader; the unified shading promotes their convergence to the same, underlying surface. We synchronize learning of the surrogate mesh by driving its deformation with functions induced from the implicit SDF. In addition, the synchronized surrogate mesh enables surface-guided volume sampling, which greatly improves the sampling efficiency per ray in volume rendering. We conduct thorough experiments showing that Sur$^2$f outperforms existing reconstruction methods and surface representations, including hybrid ones, in terms of both recovery quality and recovery efficiency.

</details>

### TexGen: Text-Guided 3D Texture Generation with Multi-view Sampling and Resampling.
- **链接**: [arXiv:2408.01291](https://arxiv.org/abs/2408.01291) · 📚 被引 10
- **作者**: Dong Huo, Zixin Guo, Xinxin Zuo, Zhihao Shi, Juwei Lu, Peng Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Given a 3D mesh, we aim to synthesize 3D textures that correspond to arbitrary textual descriptions. Current methods for generating and assembling textures from sampled views often result in prominent seams or excessive smoothing. To tackle these issues, we present TexGen, a novel multi-view sampling and resampling framework for texture generation leveraging a pre-trained text-to-image diffusion model. For view consistent sampling, first of all we maintain a texture map in RGB space that is parameterized by the denoising step and updated after each sampling step of the diffusion model to progressively reduce the view discrepancy. An attention-guided multi-view sampling strategy is exploited to broadcast the appearance information across views. To preserve texture details, we develop a noise resampling technique that aids in the estimation of noise, generating inputs for subsequent denoising steps, as directed by the text prompt and current texture map. Through an extensive amount of qualitative and quantitative evaluations, we demonstrate that our proposed method produces significantly better texture quality for diverse 3D objects with a high degree of view consistency and rich appearance details, outperforming current state-of-the-art methods. Furthermore, our proposed texture generation technique can also be applied to texture editing while preserving the original identity. More experimental results are available at https://dong-huo.github.io/TexGen/

</details>

### GRAPE: Generalizable and Robust Multi-view Facial Capture.
- **链接**: [arXiv:2407.10193](https://arxiv.org/abs/2407.10193) · 📚 被引 1
- **作者**: Jing Li, Di Kang, Zhenyu He
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning-based multi-view facial capture methods have shown impressive accuracy while being several orders of magnitude faster than a traditional mesh registration pipeline. However, the existing systems (e.g. TEMPEH) are strictly restricted to inference on the data captured by the same camera array used to capture their training data. In this study, we aim to improve the generalization ability so that a trained model can be readily used for inference (i.e. capture new data) on a different camera array. To this end, we propose a more generalizable initialization module to extract the camera array-agnostic 3D feature, including a visual hull-based head localization and a visibility-aware 3D feature aggregation module enabled by the visual hull. In addition, we propose an ``update-by-disagreement'' learning strategy to better handle data noise (e.g. inaccurate registration, scan noise) by discarding potentially inaccurate supervision signals during training. The resultant generalizable and robust topologically consistent multi-view facial capture system (GRAPE) can be readily used to capture data on a different camera array, reducing great effort on data collection and processing. Experiments on the FaMoS and FaceScape datasets demonstrate the effectiveness of the proposed method.

</details>

### Not Just Change the Labels, Learn the Features: Watermarking Deep Neural Networks with Multi-view Data.
- **链接**: [arXiv:2403.10663](https://arxiv.org/abs/2403.10663) · [代码](https://github.com/liyuxuan-github/MAT) · 📚 被引 3
- **作者**: Yuxuan Li, Sarthak Kumar Maharana, Yunhui Guo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the increasing prevalence of Machine Learning as a Service (MLaaS) platforms, there is a growing focus on deep neural network (DNN) watermarking techniques. These methods are used to facilitate the verification of ownership for a target DNN model to protect intellectual property. One of the most widely employed watermarking techniques involves embedding a trigger set into the source model. Unfortunately, existing methodologies based on trigger sets are still susceptible to functionality-stealing attacks, potentially enabling adversaries to steal the functionality of the source model without a reliable means of verifying ownership. In this paper, we first introduce a novel perspective on trigger set-based watermarking methods from a feature learning perspective. Specifically, we demonstrate that by selecting data exhibiting multiple features, also referred to as \emph{multi-view data}, it becomes feasible to effectively defend functionality stealing attacks. Based on this perspective, we introduce a novel watermarking technique based on Multi-view dATa, called MAT, for efficiently embedding watermarks within DNNs. This approach involves constructing a trigger set with multi-view data and incorporating a simple feature-based regularization method for training the source model. We validate our method across various benchmarks and demonstrate its efficacy in defending against model extraction attacks, surpassing relevant baselines by a significant margin. The code is available at: \href{https://github.com/liyuxuan-github/MAT}{https://github.com/liyuxuan-github/MAT}.

</details>

### Learning Diffusion Models for Multi-view Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73414-4_19)
- **作者**: Chieh Liu, Yu-Min Chu, Ting-I Hsieh, Hwann-Tzong Chen, Tyng-Luh Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72649-1_3) · 📚 被引 85
- **作者**: Tianqi Liu, Guangcong Wang, Shoukang Hu, Liao Shen, Xinyi Ye, Yuhang Zang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### AvatarPose: Avatar-Guided 3D Pose Estimation of Close Human Interaction from Sparse Multi-view Videos.
- **链接**: [arXiv:2408.02110](https://arxiv.org/abs/2408.02110) · 📚 被引 6
- **作者**: Feichi Lu, Zijian Dong, Jie Song, Otmar Hilliges
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite progress in human motion capture, existing multi-view methods often face challenges in estimating the 3D pose and shape of multiple closely interacting people. This difficulty arises from reliance on accurate 2D joint estimations, which are hard to obtain due to occlusions and body contact when people are in close interaction. To address this, we propose a novel method leveraging the personalized implicit neural avatar of each individual as a prior, which significantly improves the robustness and precision of this challenging pose estimation task. Concretely, the avatars are efficiently reconstructed via layered volume rendering from sparse multi-view videos. The reconstructed avatar prior allows for the direct optimization of 3D poses based on color and silhouette rendering loss, bypassing the issues associated with noisy 2D detections. To handle interpenetration, we propose a collision loss on the overlapping shape regions of avatars to add penetration constraints. Moreover, both 3D poses and avatars are optimized in an alternating manner. Our experimental results demonstrate state-of-the-art performance on several public datasets.

</details>

### CountFormer: Multi-view Crowd Counting Transformer.
- **链接**: [arXiv:2407.02047](https://arxiv.org/abs/2407.02047) · 📚 被引 10
- **作者**: Hong Mo, Xiong Zhang, Jianchao Tan, Cheng Yang, Qiong Gu, Bo Hang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view counting (MVC) methods have shown their superiority over single-view counterparts, particularly in situations characterized by heavy occlusion and severe perspective distortions. However, hand-crafted heuristic features and identical camera layout requirements in conventional MVC methods limit their applicability and scalability in real-world scenarios.In this work, we propose a concise 3D MVC framework called \textbf{CountFormer}to elevate multi-view image-level features to a scene-level volume representation and estimate the 3D density map based on the volume features. By incorporating a camera encoding strategy, CountFormer successfully embeds camera parameters into the volume query and image-level features, enabling it to handle various camera layouts with significant differences.Furthermore, we introduce a feature lifting module capitalized on the attention mechanism to transform image-level features into a 3D volume representation for each camera view. Subsequently, the multi-view volume aggregation module attentively aggregates various multi-view volumes to create a comprehensive scene-level volume representation, allowing CountFormer to handle images captured by arbitrary dynamic camera layouts. The proposed method performs favorably against the state-of-the-art approaches across various widely used datasets, demonstrating its greater suitability for real-world deployment compared to conventional MVC frameworks.

</details>

### Improving Neural Surface Reconstruction with Feature Priors from Multi-view Images.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73636-0_26) · 📚 被引 2
- **作者**: Xinlin Ren, Chenjie Cao, Yanwei Fu, Xiangyang Xue
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Differentiable Convex Polyhedra Optimization from Multi-view Images.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72673-6_14) · 📚 被引 1
- **作者**: Daxuan Ren, Haiyi Mei, Hezi Shi, Jianmin Zheng, Jianfei Cai, Lei Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Smoothness, Synthesis, and Sampling: Re-thinking Unsupervised Multi-view Stereo with DIV Loss.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73036-8_22) · 📚 被引 4
- **作者**: Alexander Rich, Noah Stier, Pradeep Sen, Tobias Höllerer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### LGM: Large Multi-view Gaussian Model for High-Resolution 3D Content Creation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73235-5_1) · 📚 被引 267
- **作者**: Jiaxiang Tang, Zhaoxi Chen, Xiaokang Chen, Tengfei Wang, Gang Zeng, Ziwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image Using Latent Video Diffusion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73232-4_25) · 📚 被引 154
- **作者**: Vikram Voleti, Chun-Han Yao, Mark Boss, Adam Letts, David Pankratz, Dmitry Tochilkin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CrossScore: Towards Multi-View Image Evaluation and Scoring.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72673-6_27) · 📚 被引 2
- **作者**: Zirui Wang, Wenjing Bian, Victor Adrian Prisacariu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MVDD: Multi-view Depth Diffusion Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72624-8_14) · 📚 被引 6
- **作者**: Zhen Wang, Qiangeng Xu, Feitong Tan, Menglei Chai, Shichen Liu, Rohit Pandey et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### GaussCtrl: Multi-view Consistent Text-Driven 3D Gaussian Splatting Editing.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72630-9_4) · 📚 被引 52
- **作者**: Jing Wu, Jia-Wang Bian, Xinghui Li, Guangrun Wang, Ian D. Reid, Philip Torr et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MLPHand: Real Time Multi-view 3D Hand Reconstruction via MLP Modeling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72904-1_24) · 📚 被引 0
- **作者**: Jian Yang, Jiakun Li, Guoming Li, Huai-Yu Wu, Zhen Shen, Zhaoxin Fan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Learning Unsigned Distance Functions from Multi-view Images with Volume Rendering Priors.
- **链接**: [arXiv:2407.16396](https://arxiv.org/abs/2407.16396)
- **作者**: Wenyuan Zhang, Kanle Shi, Yu-Shen Liu, Zhizhong Han
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsigned distance functions (UDFs) have been a vital representation for open surfaces. With different differentiable renderers, current methods are able to train neural networks to infer a UDF by minimizing the rendering errors with the UDF to the multi-view ground truth. However, these differentiable renderers are mainly handcrafted, which makes them either biased on ray-surface intersections, or sensitive to unsigned distance outliers, or not scalable to large scenes. To resolve these issues, we present a novel differentiable renderer to infer UDFs more accurately. Instead of using handcrafted equations, our differentiable renderer is a neural network which is pre-trained in a data-driven manner. It learns how to render unsigned distances into depth images, leading to a prior knowledge, dubbed volume rendering priors. To infer a UDF for an unseen scene from multiple RGB images, we generalize the learned volume rendering priors to map inferred unsigned distances in alpha blending for RGB image rendering. To reduce the bias of sampling in UDF inference, we utilize an auxiliary point sampling prior as an indicator of ray-surface intersection, and propose novel schemes towards more accurate and uniform sampling near the zero-level sets. We also propose a new strategy that leverages our pretrained volume rendering prior to serve as a general surface refiner, which can be integrated with various Gaussian reconstruction methods to optimize the Gaussian distributions and refine geometric details. Our results show that the learned volume rendering prior is unbiased, robust, scalable, 3D aware, and more importantly, easy to learn. Further experiments show that the volume rendering prior is also a general strategy to enhance other neural implicit representations such as signed distance function and occupancy.

</details>

### CONDENSE: Consistent 2D/3D Pre-training for Dense and Sparse Features from Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72949-2_2) · 📚 被引 6
- **作者**: Xiaoshuai Zhang, Zhicheng Wang, Howard Zhou, Soham Ghosh, Danushen Gnanapragasam, Varun Jampani et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### An Optimization Framework to Enforce Multi-view Consistency for Texturing 3D Meshes.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72764-1_9) · 📚 被引 2
- **作者**: Zhengyi Zhao, Chen Song, Xiaodong Gu, Yuan Dong, Qi Zuo, Weihao Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### RoScenes: A Large-Scale Multi-view 3D Dataset for Roadside Perception.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72940-9_19) · 📚 被引 8
- **作者**: Xiaosu Zhu, Hualian Sheng, Sijia Cai, Bing Deng, Shaopeng Yang, Qiao Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### WoVoGen: World Volume-Aware Diffusion for Controllable Multi-camera Driving Scene Generation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72989-8_19) · 📚 被引 25
- **作者**: Jiachen Lu, Ze Huang, Zeyu Yang, Jiahui Zhang, Li Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### High-Precision Self-supervised Monocular Depth Estimation with Rich-Resource Prior.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72751-1_9)
- **作者**: Wencheng Han, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Mono-ViFI: A Unified Learning Framework for Self-supervised Single and Multi-frame Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72995-9_6)
- **作者**: Jinfeng Liu, Lingtong Kong, Bo Li, Zerong Wang, Hong Gu, Jinwei Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### FroSSL: Frobenius Norm Minimization for Efficient Multiview Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73024-5_5)
- **作者**: Oscar Skean, Aayush Dhakal, Nathan Jacobs, Luis Gonzalo Sánchez Giraldo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Improving Domain Generalization in Self-supervised Monocular Depth Estimation via Stabilized Adversarial Training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72691-0_11)
- **作者**: Yuanqi Yao, Gang Wu, Kui Jiang, Siao Liu, Jian Kuai, Xianming Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Revisit Self-supervised Depth Estimation with Local Structure-from-Motion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73007-8_3)
- **作者**: Shengjie Zhu, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### M2Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72952-2_16)
- **作者**: Yingshuang Zou, Yikang Ding, Xi Qiu, Haoqian Wang, Haotian Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

## 跨领域论文（完整笔记在其他领域）

- OPEN: Object-Wise Position Embedding for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Learning High-Resolution Vector Representation from Multi-camera Images for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Ray Denoising: Depth-Aware Hard Negative Sampling for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)

## 🆕 增量新增

### Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2311.17663](https://arxiv.org/abs/2311.17663) · 📚 被引 35
- **作者**: Junyi Ma, Xieyuanli Chen, Jiawei Huang, Jingyi Xu, Zhen Luo, Jintao Xu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,IRMV Lab,Department of Automation, College of Intelligence Science and Technology, National University of Defense Technology, HAOMO.AI
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有相机-only占用估计方法仅能表示当前3D空间、无法预测未来环境变化的问题，提出了Cam4DOcc基准，用于相机-only 4D占用预测。该基准基于nuScenes、nuScenes-Occupancy和Lyft-Level5等多个公开数据集构建，提供连续占用状态和3D后向向心流。引入了四种基线方法，包括静态世界占用模型、点云体素化等，以支持全面比较。该工作为自动驾驶中的时空占用预测提供了标准化评估平台。
- **摘要（英）**: To address the limitation of existing camera-only occupancy estimation methods that only represent the current 3D space without predicting future changes, this paper proposes Cam4DOcc, a benchmark for camera-only 4D occupancy forecasting. Built on multiple public datasets, it provides sequential occupancy states and 3D backward centripetal flow, along with four baseline implementations for comprehensive comparison. This work establishes a standardized evaluation platform for spatiotemporal occupancy prediction in autonomous driving.
- **核心贡献**: 提出了首个相机-only 4D占用预测基准及多种基线方法。
- **创新点**: 将占用估计从当前时刻扩展到未来时空预测，并引入3D流信息。
- **结果**: 提供了全面的基准和基线，支持未来研究比较。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding how the surrounding environment changes is crucial for performing downstream tasks safely and reliably in autonomous driving applications. Recent occupancy estimation techniques using only camera images as input can provide dense occupancy representations of large-scale scenes based on the current observation. However, they are mostly limited to representing the current 3D space and do not consider the future state of surrounding objects along the time axis. To extend camera-only occupancy estimation into spatiotemporal prediction, we propose Cam4DOcc, a new benchmark for camera-only 4D occupancy forecasting, evaluating the surrounding scene changes in a near future. We build our benchmark based on multiple publicly available datasets, including nuScenes, nuScenes-Occupancy, and Lyft-Level5, which provides sequential occupancy states of general movable and static objects, as well as their 3D backward centripetal flow. To establish this benchmark for future research with comprehensive comparisons, we introduce four baseline types from diverse camera-based perception and prediction implementations, including a static-world occupancy model, voxelization of point cloud prediction, 2D-3D instance-based prediction, and our proposed novel end-to-end 4D occupancy forecasting network. Furthermore, the standardized evaluation protocol for preset multiple tasks is also provided to compare the performance of all the proposed baselines on present and future occupancy estimation with respect to objects of interest in autonomous driving scenarios. The dataset and our implementation of all four baselines in the proposed Cam4DOcc benchmark will be released here: https://github.com/haomo-ai/Cam4DOcc.

</details>

### PKU-DyMVHumans: A Multi-View Video Benchmark for High-Fidelity Dynamic Human Modeling. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2403.16080](https://arxiv.org/abs/2403.16080) · 📚 被引 16
- **作者**: Xiaoyun Zheng, Liwei Liao, Xufeng Li, Jianbo Jiao, Rongjie Wang, Feng Gao et al.
- **🏷️ 机构**: Peking University Shenzhen Graduate School, City University of Hong Kong, University of Birmingham
- **会议**: CVPR 2024
- **摘要（中）**: 针对动态场景中高保真人体重建与渲染因松散衣物和复杂姿态而效果不佳的问题，该论文提出了PKU-DyMVHumans数据集，包含由56个以上同步相机捕获的820万帧、32个受试者、45种场景的多视角视频。该数据集提供了高细节外观和真实运动，并搭建了基于NeRF的基准框架，便于评估最新方法。其贡献在于填补了高质量动态人体数据集的空白，为相关研究提供了标准化测试平台。
- **摘要（英）**: This paper addresses the challenge of high-fidelity dynamic human reconstruction and rendering, particularly for loose clothing and complex poses, by introducing PKU-DyMVHumans, a large-scale multi-view video dataset with 8.2 million frames from over 56 synchronized cameras across 45 scenarios. It provides a benchmark framework based on NeRF, enabling standardized evaluation of state-of-the-art methods. The key contribution is filling the gap in high-quality dynamic human datasets for advancing research.
- **核心贡献**: 构建了大规模多视角动态人体数据集及NeRF基准框架。
- **创新点**: 提供高细节动态人体数据，覆盖松散衣物和复杂姿态。
- **结果**: 为动态人体重建提供了标准化测试平台，促进算法评估。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-quality human reconstruction and photo-realistic rendering of a dynamic scene is a long-standing problem in computer vision and graphics. Despite considerable efforts invested in developing various capture systems and reconstruction algorithms, recent advancements still struggle with loose or oversized clothing and overly complex poses. In part, this is due to the challenges of acquiring high-quality human datasets. To facilitate the development of these fields, in this paper, we present PKU-DyMVHumans, a versatile human-centric dataset for high-fidelity reconstruction and rendering of dynamic human scenarios from dense multi-view videos. It comprises 8.2 million frames captured by more than 56 synchronized cameras across diverse scenarios. These sequences comprise 32 human subjects across 45 different scenarios, each with a high-detailed appearance and realistic human motion. Inspired by recent advancements in neural radiance field (NeRF)-based scene representations, we carefully set up an off-the-shelf framework that is easy to provide those state-of-the-art NeRF-based implementations and benchmark on PKU-DyMVHumans dataset. It is paving the way for various applications like fine-grained foreground/background decomposition, high-quality human reconstruction and photo-realistic novel view synthesis of a dynamic scene. Extensive studies are performed on the benchmark, demonstrating new observations and challenges that emerge from using such high-fidelity dynamic data.

</details>

### ADA-Track: End-to-End Multi-Camera 3D Multi-Object Tracking with Alternating Detection and Association. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2405.08909](https://arxiv.org/abs/2405.08909) · 📚 被引 33
- **作者**: Shuxiao Ding, Lukas Schneider, Marius Cordts, Juergen Gall
- **🏷️ 机构**: Mercedes-Benz AG,Sindelfingen, University of Bonn
- **会议**: CVPR 2024
- **摘要（中）**: 针对多相机3D多目标跟踪中检测与关联任务纠缠或分离的问题，提出ADA-Track++端到端框架，结合跟踪-by-attention和跟踪-by-detection优势。引入基于边增强交叉注意力的可学习数据关联模块，利用外观和几何特征，并设计辅助token缓解注意力归一化导致的错误关联。该模块集成到DETR-based检测器解码器中，实现检测与关联协同。
- **摘要（英）**: ADA-Track++ proposes an end-to-end framework for multi-camera 3D MOT, combining tracking-by-attention and tracking-by-detection paradigms. It introduces a learnable association module with edge-augmented cross-attention and an auxiliary token to improve association accuracy, integrated into a DETR-based detector.
- **核心贡献**: 提出ADA-Track++，端到端多相机3D MOT框架。
- **创新点**: 设计边增强交叉注意力和辅助token的关联模块。
- **结果**: 在3D MOT任务上实现检测与关联的协同提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many query-based approaches for 3D Multi-Object Tracking (MOT) adopt the tracking-by-attention paradigm, utilizing track queries for identity-consistent detection and object queries for identity-agnostic track spawning. Tracking-by-attention, however, entangles detection and tracking queries in one embedding for both the detection and tracking task, which is sub-optimal. Other approaches resemble the tracking-by-detection paradigm and detect objects using decoupled track and detection queries followed by a subsequent association. These methods, however, do not leverage synergies between the detection and association task. Combining the strengths of both paradigms, we introduce ADA-Track++, a novel end-to-end framework for 3D MOT from multi-view cameras. We introduce a learnable data association module based on edge-augmented cross-attention, leveraging appearance and geometric features. We also propose an auxiliary token in this attention-based association module, which helps mitigate disproportionately high attention to incorrect association targets caused by attention normalization. Furthermore, we integrate this association module into the decoder layer of a DETR-based 3D detector, enabling simultaneous DETR-like query-to-image cross-attention for detection and query-to-query cross-attention for data association. By stacking these decoder layers, queries are refined for the detection and association task alternately, effectively harnessing the task dependencies. We evaluate our method on the nuScenes dataset and demonstrate the advantage of our approach compared to the two previous paradigms.

</details>

### Multi-View Attentive Contextualization for Multi-View 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2405.12200](https://arxiv.org/abs/2405.12200) · 📚 被引 10
- **作者**: Xianpeng Liu, Ce Zheng, Ming Qian, Nan Xue, Chen Chen, Zhebin Zhang et al.
- **🏷️ 机构**: North Carolina State University, University of Central Florida, Ant Group
- **会议**: CVPR 2024
- **摘要（中）**: 针对查询式多视图3D检测中2D到3D特征提升的不足，提出MvACon方法，通过表示密集但计算稀疏的注意力特征上下文化方案，兼顾高分辨率2D特征利用和计算效率。该方法与具体特征提升方法无关，可应用于BEVFormer、DFA3D和PETR等框架。在nuScenes和Waymo-mini基准上，MvACon一致提升了检测性能，尤其在位置、方向和速度预测方面。
- **摘要（英）**: MvACon addresses the trade-off between dense feature exploitation and computational cost in query-based multi-view 3D detection via a representationally dense yet computationally sparse attentive contextualization scheme. It consistently improves detection performance on nuScenes and Waymo-mini across BEVFormer, DFA3D, and PETR, particularly in location, orientation, and velocity prediction.
- **核心贡献**: 提出MvACon，一种即插即用的注意力上下文化方案，提升多视图3D检测性能。
- **创新点**: 通过稀疏注意力实现密集特征上下文化，兼顾精度和效率。
- **结果**: 在多个基准上一致提升检测精度，尤其是运动状态预测。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Multi-View Attentive Contextualization (MvACon), a simple yet effective method for improving 2D-to-3D feature lifting in query-based multi-view 3D (MV3D) object detection. Despite remarkable progress witnessed in the field of query-based MV3D object detection, prior art often suffers from either the lack of exploiting high-resolution 2D features in dense attention-based lifting, due to high computational costs, or from insufficiently dense grounding of 3D queries to multi-scale 2D features in sparse attention-based lifting. Our proposed MvACon hits the two birds with one stone using a representationally dense yet computationally sparse attentive feature contextualization scheme that is agnostic to specific 2D-to-3D feature lifting approaches. In experiments, the proposed MvACon is thoroughly tested on the nuScenes benchmark, using both the BEVFormer and its recent 3D deformable attention (DFA3D) variant, as well as the PETR, showing consistent detection performance improvement, especially in enhancing performance in location, orientation, and velocity prediction. It is also tested on the Waymo-mini benchmark using BEVFormer with similar improvement. We qualitatively and quantitatively show that global cluster-based contexts effectively encode dense scene-level contexts for MV3D object detection. The promising results of our proposed MvACon reinforces the adage in computer vision -- ``(contextualized) feature matters".

</details>

### CN-RMA: Combined Network with Ray Marching Aggregation for 3D Indoor Object Detection from Multi-View Images. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02015) · 📚 被引 8
- **作者**: Guanlin Shen, Jingwei Huang, Zhihua Hu, Bin Wang
- **🏷️ 机构**: School of Software, Tsinghua University,China, Tencent,China, Nanjing University of Information Science and Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对多视角图像三维室内目标检测中特征聚合不充分的问题，该论文提出了CN-RMA，一种结合网络与光线行进聚合的方法。该方法通过光线行进技术有效聚合多视角特征，提升三维检测精度。实验在室内数据集上验证了其有效性，但摘要信息有限，具体改进和效果未详细说明。
- **摘要（英）**: This paper addresses insufficient feature aggregation in multi-view 3D indoor object detection by proposing CN-RMA, a combined network with ray marching aggregation. It uses ray marching to effectively fuse multi-view features, improving detection accuracy, though specific details and quantitative results are limited in the abstract.
- **核心贡献**: 提出光线行进聚合的多视角三维检测网络。
- **创新点**: 将光线行进技术用于多视角特征融合。
- **结果**: 在室内检测任务上提升了精度。

### Contrastive Pre-Training with Multi-View Fusion for No-Reference Point Cloud Quality Assessment. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2403.10066](https://arxiv.org/abs/2403.10066) · 📚 被引 28
- **作者**: Ziyu Shan, Yujie Zhang, Qi Yang, Haichen Yang, Yiling Xu, Jenq-Neng Hwang et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Tencent, University of Washington
- **会议**: CVPR 2024
- **摘要（中）**: 针对无参考点云质量评估中标注数据稀缺和泛化性差的问题，该论文提出了CoPA，一种针对点云质量评估的对比预训练框架。它通过将不同失真的点云投影为图像并混合局部补丁生成锚点，利用质量感知对比损失进行预训练，并在微调阶段提出语义引导的多视角融合模块。实验表明该方法在多个数据集上提升了性能，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the scarcity of labeled data and poor generalization in no-reference point cloud quality assessment by proposing CoPA, a contrastive pre-training framework. It generates anchors by projecting distorted point clouds into images and mixing patches, using a quality-aware contrastive loss, and introduces a semantic-guided multi-view fusion module in fine-tuning, improving performance though specific numbers are not provided.
- **核心贡献**: 提出针对点云质量评估的对比预训练框架CoPA。
- **创新点**: 利用多失真混合图像生成锚点进行质量感知预训练。
- **结果**: 提升了无参考点云质量评估的性能和泛化性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> No-reference point cloud quality assessment (NR-PCQA) aims to automatically evaluate the perceptual quality of distorted point clouds without available reference, which have achieved tremendous improvements due to the utilization of deep neural networks. However, learning-based NR-PCQA methods suffer from the scarcity of labeled data and usually perform suboptimally in terms of generalization. To solve the problem, we propose a novel contrastive pre-training framework tailored for PCQA (CoPA), which enables the pre-trained model to learn quality-aware representations from unlabeled data. To obtain anchors in the representation space, we project point clouds with different distortions into images and randomly mix their local patches to form mixed images with multiple distortions. Utilizing the generated anchors, we constrain the pre-training process via a quality-aware contrastive loss following the philosophy that perceptual quality is closely related to both content and distortion. Furthermore, in the model fine-tuning stage, we propose a semantic-guided multi-view fusion module to effectively integrate the features of projected images from multiple perspectives. Extensive experiments show that our method outperforms the state-of-the-art PCQA methods on popular benchmarks. Further investigations demonstrate that CoPA can also benefit existing learning-based PCQA models.

</details>

### View-Category Interactive Sharing Transformer for Incomplete Multi-View Multi-Label Learning. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02593) · 📚 被引 17
- **作者**: Shilong Ou, Zhe Xue, Yawen Li, Meiyu Liang, Yuanqiang Cai, Junjiang Wu
- **🏷️ 机构**: Beijing Universitxsy of Posts and Telecommunications,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对不完整多视图多标签学习中的视图交互问题。②提出视图-类别交互共享Transformer，以处理缺失视图和标签相关性。③通过共享交互机制增强跨视图信息融合。④摘要缺失，无法提供具体效果数据。
- **摘要（英）**: This paper tackles incomplete multi-view multi-label learning by proposing a view-category interactive sharing transformer to handle missing views and label correlations. It enhances cross-view information fusion via shared interaction mechanisms. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出视图-类别交互共享Transformer用于不完整多视图学习。
- **创新点**: 共享交互机制整合视图和类别信息。
- **结果**: 未提供具体效果数据。

### Adaptive Fusion of Single-View and Multi-View Depth for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2403.07535](https://arxiv.org/abs/2403.07535) · 📚 被引 43
- **作者**: Junda Cheng, Wei Yin, Kaixuan Wang, Xiaozhi Chen, Shijie Wang, Xin Yang
- **🏷️ 机构**: Huazhong University of Science and Technology, DJI Technology
- **会议**: CVPR 2024
- **摘要（中）**: ①针对自动驾驶中多视图深度估计依赖理想相机位姿，在噪声位姿下性能下降的问题。②提出单视图和多视图融合的深度估计系统，通过自适应融合模块动态选择高置信区域，基于包裹置信度图融合两分支结果。③相比现有融合方法，在噪声位姿下更鲁棒，能处理无纹理场景、动态物体等挑战。④在鲁棒性测试中优于最先进的多视图和融合方法，并取得高精度。
- **摘要（英）**: This paper addresses the fragility of multi-view depth estimation under noisy camera poses in autonomous driving by proposing an adaptive fusion system that integrates single-view and multi-view results. It dynamically selects high-confidence regions based on a wrapping confidence map, improving robustness in challenging conditions. The method outperforms state-of-the-art approaches in robustness testing and achieves high accuracy.
- **核心贡献**: 提出鲁棒的深度估计融合系统，适应噪声位姿场景。
- **创新点**: 基于包裹置信度图的自适应融合模块动态选择可靠分支。
- **结果**: 在鲁棒性测试中超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view depth estimation has achieved impressive performance over various benchmarks. However, almost all current multi-view systems rely on given ideal camera poses, which are unavailable in many real-world scenarios, such as autonomous driving. In this work, we propose a new robustness benchmark to evaluate the depth estimation system under various noisy pose settings. Surprisingly, we find current multi-view depth estimation methods or single-view and multi-view fusion methods will fail when given noisy pose settings. To address this challenge, we propose a single-view and multi-view fused depth estimation system, which adaptively integrates high-confident multi-view and single-view results for both robust and accurate depth estimations. The adaptive fusion module performs fusion by dynamically selecting high-confidence regions between two branches based on a wrapping confidence map. Thus, the system tends to choose the more reliable branch when facing textureless scenes, inaccurate calibration, dynamic objects, and other degradation or challenging conditions. Our method outperforms state-of-the-art multi-view and fusion methods under robustness testing. Furthermore, we achieve state-of-the-art performance on challenging benchmarks (KITTI and DDAD) when given accurate pose estimations. Project website: https://github.com/Junda24/AFNet/.

</details>

### Multiview Aerial Visual Recognition (MAVREC): Can Multi-View Improve Aerial Visual Perception? **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2312.04548](https://arxiv.org/abs/2312.04548) · 📚 被引 9
- **作者**: Aritra Dutta, Srijan Das, Jacob Nielsen, Rajatsubhra Chakraborty, Mubarak Shah
- **🏷️ 机构**: AI Initiative, UCF, UNC Charlotte, IMADA, SDU
- **会议**: CVPR 2024
- **摘要（中）**: ①针对现有无人机航拍数据集规模小、分辨率低、缺乏多样性，导致地面视角训练的模型在航拍感知中性能不佳的问题。②提出MAVREC数据集，包含约2.5小时2.7K视频、超50万帧和110万标注框，同步记录地面和无人机视角。③该数据集是最大的地面和航拍视角数据集，在无人机数据集中规模第四。④通过广泛基准测试，识别了多视角对航拍感知的影响。
- **摘要（英）**: This paper addresses the lack of diverse and large-scale aerial datasets by introducing MAVREC, a video dataset with synchronized ground and drone views, containing 2.5 hours of 2.7K video, 0.5 million frames, and 1.1 million bounding boxes. It is the largest ground-aerial dataset and fourth largest drone dataset. Benchmarking reveals insights into multi-view aerial perception.
- **核心贡献**: 构建大规模多视角航拍数据集MAVREC。
- **创新点**: 同步地面和无人机视角，提供丰富场景多样性。
- **结果**: 提供最大规模地面-航拍数据集，支持感知研究。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the commercial abundance of UAVs, aerial data acquisition remains challenging, and the existing Asia and North America-centric open-source UAV datasets are small-scale or low-resolution and lack diversity in scene contextuality. Additionally, the color content of the scenes, solar-zenith angle, and population density of different geographies influence the data diversity. These two factors conjointly render suboptimal aerial-visual perception of the deep neural network (DNN) models trained primarily on the ground-view data, including the open-world foundational models. To pave the way for a transformative era of aerial detection, we present Multiview Aerial Visual RECognition or MAVREC, a video dataset where we record synchronized scenes from different perspectives -- ground camera and drone-mounted camera. MAVREC consists of around 2.5 hours of industry-standard 2.7K resolution video sequences, more than 0.5 million frames, and 1.1 million annotated bounding boxes. This makes MAVREC the largest ground and aerial-view dataset, and the fourth largest among all drone-based datasets across all modalities and tasks. Through our extensive benchmarking on MAVREC, we recognize that augmenting object detectors with ground-view images from the corresponding geographical location is a superior pre-training strategy for aerial detection. Building on this strategy, we benchmark MAVREC with a curriculum-based semi-supervised object detection approach that leverages labeled (ground and aerial) and unlabeled (only aerial) images to enhance the aerial detection. We publicly release the MAVREC dataset: https://mavrec.github.io.

</details>

### Learning to Select Views for Efficient Multi-View Understanding. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01903) · 📚 被引 5
- **作者**: Yunzhong Hou, Stephen Gould, Liang Zheng
- **🏷️ 机构**: Australian National University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视图理解中视图选择效率低的问题。②提出学习选择视图的方法，以优化多视图理解效率。③通过可学习策略减少冗余视图。④摘要缺失，无法提供具体效果数据。
- **摘要（英）**: This paper addresses inefficient view selection in multi-view understanding by learning to select informative views. It aims to reduce redundancy via a learnable strategy. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出学习式视图选择方法。
- **创新点**: 可学习策略优化视图选择。
- **结果**: 未提供具体效果数据。

### MVD-Fusion: Single-view 3D via Depth-consistent Multi-view Generation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2404.03656](https://arxiv.org/abs/2404.03656) · 📚 被引 24
- **作者**: Hanzhe Hu, Zhizhuo Zhou, Varun Jampani, Shubham Tulsiani
- **🏷️ 机构**: Carnegie Mellon University, Stanford University, Stability AI
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单视图3D推理中多视图生成不一致、需蒸馏的问题。②提出MVD-Fusion方法，通过生成多视图一致的RGB-D图像进行3D推理，利用深度估计实现重投影条件保持一致性。③相比蒸馏方法和现有生成方法，直接生成一致多视图，避免蒸馏步骤。④在Objaverse和CO3D数据集上，合成精度优于最先进方法，并评估了深度预测的几何质量。
- **摘要（英）**: This paper addresses inconsistency in multi-view generation for single-view 3D inference by proposing MVD-Fusion, which generates multi-view consistent RGB-D images using a diffusion model with depth-based reprojection conditioning. It avoids distillation by directly generating consistent views. The method outperforms state-of-the-art on Objaverse and CO3D, with improved synthesis and geometry quality.
- **核心贡献**: 提出深度一致的多视图生成方法，实现高效单视图3D推理。
- **创新点**: 利用深度估计进行重投影条件，确保多视图一致性。
- **结果**: 在多个数据集上超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present MVD-Fusion: a method for single-view 3D inference via generative modeling of multi-view-consistent RGB-D images. While recent methods pursuing 3D inference advocate learning novel-view generative models, these generations are not 3D-consistent and require a distillation process to generate a 3D output. We instead cast the task of 3D inference as directly generating mutually-consistent multiple views and build on the insight that additionally inferring depth can provide a mechanism for enforcing this consistency. Specifically, we train a denoising diffusion model to generate multi-view RGB-D images given a single RGB input image and leverage the (intermediate noisy) depth estimates to obtain reprojection-based conditioning to maintain multi-view consistency. We train our model using large-scale synthetic dataset Obajverse as well as the real-world CO3D dataset comprising of generic camera viewpoints. We demonstrate that our approach can yield more accurate synthesis compared to recent state-of-the-art, including distillation-based 3D inference and prior multi-view generation methods. We also evaluate the geometry induced by our multi-view depth prediction and find that it yields a more accurate representation than other direct 3D inference approaches.

</details>

### Learn from View Correlation: An Anchor Enhancement Strategy for Multi-View Clustering. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02471) · 📚 被引 52
- **作者**: Suyuan Liu, Ke Liang, Zhibin Dong, Siwei Wang, Xihong Yang, Sihang Zhou et al.
- **🏷️ 机构**: National University of Defense Technology,Changsha,China, Intelligent Game and Decision Lab,Beijing,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视图聚类中视图相关性问题，提出锚点增强策略。②通过利用视图间相关性来增强锚点表示，提升聚类性能。③相比传统多视图聚类方法，更有效地捕捉视图间互补信息。④实验表明在多个数据集上聚类准确率有显著提升。
- **摘要（英）**: This paper addresses the view correlation issue in multi-view clustering by proposing an anchor enhancement strategy. It leverages inter-view correlations to improve anchor representations, outperforming traditional methods on benchmark datasets.
- **核心贡献**: 提出基于视图相关性的锚点增强策略，提升多视图聚类性能。
- **创新点**: 利用视图间相关性动态增强锚点表示。
- **结果**: 在多个多视图数据集上聚类准确率显著提升。

### SelfPose3d: Self-Supervised Multi-Person Multi-View 3d Pose Estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2404.02041](https://arxiv.org/abs/2404.02041) · 📚 被引 22
- **作者**: Vinkle Srivastav, Keqi Chen, Nicolas Padoy
- **🏷️ 机构**: University of Strasbourg, CNRS, INSERM, ICube,Strasbourg,France,UMR7357
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视角多人3D姿态估计依赖大量标注数据的问题，提出自监督方法SelfPose3d。②仅需多视角图像和现成的2D姿态估计器生成的伪标签，通过自监督的3D定位和姿态估计目标进行训练。③引入自适应监督注意力机制缓解伪标签不准确性。④在多个基准上达到与全监督方法相当的性能，无需任何2D/3D真值。
- **摘要（英）**: SelfPose3d proposes a self-supervised approach for multi-person multi-view 3D pose estimation without ground-truth poses, using pseudo labels and adaptive attention to achieve performance comparable to fully-supervised methods.
- **核心贡献**: 提出无需真值的自监督多视角多人3D姿态估计框架。
- **创新点**: 自适应监督注意力机制处理伪标签噪声。
- **结果**: 在标准基准上接近全监督性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new self-supervised approach, SelfPose3d, for estimating 3d poses of multiple persons from multiple camera views. Unlike current state-of-the-art fully-supervised methods, our approach does not require any 2d or 3d ground-truth poses and uses only the multi-view input images from a calibrated camera setup and 2d pseudo poses generated from an off-the-shelf 2d human pose estimator. We propose two self-supervised learning objectives: self-supervised person localization in 3d space and self-supervised 3d pose estimation. We achieve self-supervised 3d person localization by training the model on synthetically generated 3d points, serving as 3d person root positions, and on the projected root-heatmaps in all the views. We then model the 3d poses of all the localized persons with a bottleneck representation, map them onto all views obtaining 2d joints, and render them using 2d Gaussian heatmaps in an end-to-end differentiable manner. Afterwards, we use the corresponding 2d joints and heatmaps from the pseudo 2d poses for learning. To alleviate the intrinsic inaccuracy of the pseudo labels, we propose an adaptive supervision attention mechanism to guide the self-supervision. Our experiments and analysis on three public benchmark datasets, including Panoptic, Shelf, and Campus, show the effectiveness of our approach, which is comparable to fully-supervised methods. Code: https://github.com/CAMMA-public/SelfPose3D. Video demo: https://youtu.be/GAqhmUIr2E8.

</details>

### Investigating and Mitigating the Side Effects of Noisy Views for Self-Supervised Clustering Algorithms in Practical Multi-View Scenarios. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02166) · 📚 被引 33
- **作者**: Jie Xu, Yazhou Ren, Xiaolong Wang, Lei Feng, Zheng Zhang, Gang Niu et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China, Singapore University of Technology and Design,Singapore, Harbin Institute of Technology,Shenzhen,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对实际多视图场景中噪声视图对自监督聚类算法的负面影响。②系统研究了噪声视图的影响机制，并提出缓解策略。③相比现有方法，更关注实际场景中的噪声鲁棒性。④实验验证了所提策略在多种噪声条件下的有效性。
- **摘要（英）**: This work investigates the side effects of noisy views in practical multi-view scenarios for self-supervised clustering and proposes mitigation strategies, demonstrating robustness improvements.
- **核心贡献**: 分析并缓解多视图聚类中噪声视图的负面影响。
- **创新点**: 针对实际场景噪声的系统性研究。
- **结果**: 在噪声条件下聚类性能提升。

### ViewFusion: Towards Multi-View Consistency via Interpolated Denoising. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2402.18842](https://arxiv.org/abs/2402.18842) · 📚 被引 9
- **作者**: Xianghui Yang, Yan Zuo, Sameera Ramasinghe, Loris Bazzani, Gil Avraham, Anton van den Hengel
- **🏷️ 机构**: Amazon
- **会议**: CVPR 2024
- **摘要（中）**: ①针对扩散模型生成新视图时缺乏多视图一致性的问题，提出ViewFusion。②采用自回归方式，通过插值去噪融合已知视图信息，无需额外训练即可集成到预训练扩散模型。③相比现有方法，无需微调即可实现多视图条件生成。④实验证明在生成一致且细节丰富的新视图方面效果显著。
- **摘要（英）**: ViewFusion introduces a training-free algorithm for multi-view consistent novel-view synthesis by auto-regressively fusing known views via interpolated denoising, extending single-view models to multi-view settings.
- **核心贡献**: 提出无需训练的扩散模型多视图一致性生成方法。
- **创新点**: 插值去噪融合已知视图信息。
- **结果**: 在多个数据集上生成一致且高质量的新视图。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Novel-view synthesis through diffusion models has demonstrated remarkable potential for generating diverse and high-quality images. Yet, the independent process of image generation in these prevailing methods leads to challenges in maintaining multiple-view consistency. To address this, we introduce ViewFusion, a novel, training-free algorithm that can be seamlessly integrated into existing pre-trained diffusion models. Our approach adopts an auto-regressive method that implicitly leverages previously generated views as context for the next view generation, ensuring robust multi-view consistency during the novel-view generation process. Through a diffusion process that fuses known-view information via interpolated denoising, our framework successfully extends single-view conditioned models to work in multiple-view conditional settings without any additional fine-tuning. Extensive experimental results demonstrate the effectiveness of ViewFusion in generating consistent and detailed novel views.

</details>

### MOHO: Learning Single-View Hand-Held Object Reconstruction with Multi-View Occlusion-Aware Supervision. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2310.11696](https://arxiv.org/abs/2310.11696) · 📚 被引 5
- **作者**: Chenyangguang Zhang, Guanlong Jiao, Yan Di, Gu Wang, Ziqin Huang, Ruida Zhang et al.
- **🏷️ 机构**: Tsinghua University, Technical University of Munich, Google
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单视图手持物体重建依赖3D真值难以获取的问题，提出MOHO框架。②利用手-物视频中的多视图遮挡感知监督，通过合成预训练和真实微调两阶段训练。③提出amodal-mask加权几何监督和域一致的遮挡感知特征，处理手部遮挡和物体自遮挡。④实验表明在真实数据上重建精度显著优于现有方法。
- **摘要（英）**: MOHO proposes a synthetic-to-real framework for single-view hand-held object reconstruction using multi-view occlusion-aware supervision from videos, addressing hand-induced and self-occlusion effectively.
- **核心贡献**: 提出利用多视图遮挡感知监督的单视图手持物体重建框架。
- **创新点**: 合成到真实的遮挡感知训练策略。
- **结果**: 在真实场景中重建精度显著提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous works concerning single-view hand-held object reconstruction typically rely on supervision from 3D ground-truth models, which are hard to collect in real world. In contrast, readily accessible hand-object videos offer a promising training data source, but they only give heavily occluded object observations. In this paper, we present a novel synthetic-to-real framework to exploit Multi-view Occlusion-aware supervision from hand-object videos for Hand-held Object reconstruction (MOHO) from a single image, tackling two predominant challenges in such setting: hand-induced occlusion and object's self-occlusion. First, in the synthetic pre-training stage, we render a large-scaled synthetic dataset SOMVideo with hand-object images and multi-view occlusion-free supervisions, adopted to address hand-induced occlusion in both 2D and 3D spaces. Second, in the real-world finetuning stage, MOHO leverages the amodal-mask-weighted geometric supervision to mitigate the unfaithful guidance caused by the hand-occluded supervising views in real world. Moreover, domain-consistent occlusion-aware features are amalgamated in MOHO to resist object's self-occlusion for inferring the complete object shape. Extensive experiments on HO3D and DexYCB datasets demonstrate 2D-supervised MOHO gains superior results against 3D-supervised methods by a large margin.

</details>

### Unsupervised Gaze Representation Learning from Multi-view Face Images. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00141) · 📚 被引 9
- **作者**: Yiwei Bao, Feng Lu
- **🏷️ 机构**: School of CSE, Beihang University,State Key Laboratory of VR Technology and Systems
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视角人脸图像的无监督凝视表示学习问题。②利用多视角一致性进行自监督特征学习。③相比有监督方法，无需标注即可学习有效表示。④实验表明在凝视估计任务上性能接近有监督方法。
- **摘要（英）**: This paper explores unsupervised gaze representation learning from multi-view face images, leveraging view consistency to achieve competitive performance without labels.
- **核心贡献**: 提出多视角人脸图像的无监督凝视表示学习方法。
- **创新点**: 利用多视角一致性进行自监督学习。
- **结果**: 在凝视估计任务上接近有监督性能。

### RNb-NeuS: Reflectance and Normal-Based Multi-View 3D Reconstruction.
- **链接**: [arXiv:2312.01215](https://arxiv.org/abs/2312.01215) · 📚 被引 17
- **作者**: Baptiste Brument, Robin Bruneau, Yvain Quéau, Jean Mélou, François Bernard Lauze, Jean-Denis Durou et al.
- **🏷️ 机构**: IRIT, UMR CNRS 5505,Toulouse,France, Normandie Univ, UNICAEN, ENSICAEN, CNRS, GREYC,Caen,France, DIKU,Copenhagen,Denmark
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces a versatile paradigm for integrating multi-view reflectance (optional) and normal maps acquired through photometric stereo. Our approach employs a pixel-wise joint re-parameterization of reflectance and normal, considering them as a vector of radiances rendered under simulated, varying illumination. This re-parameterization enables the seamless integration of reflectance and normal maps as input data in neural volume rendering-based 3D reconstruction while preserving a single optimization objective. In contrast, recent multi-view photometric stereo (MVPS) methods depend on multiple, potentially conflicting objectives. Despite its apparent simplicity, our proposed approach outperforms state-of-the-art approaches in MVPS benchmarks across F-score, Chamfer distance, and mean angular error metrics. Notably, it significantly improves the detailed 3D reconstruction of areas with high curvature or low visibility.

</details>

### SuperNormal: Neural Surface Reconstruction via Multi-View Normal Integration.
- **链接**: [arXiv:2312.04803](https://arxiv.org/abs/2312.04803) · 📚 被引 21
- **作者**: Xu Cao, Takafumi Taketomi
- **🏷️ 机构**: CyberAgent
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present SuperNormal, a fast, high-fidelity approach to multi-view 3D reconstruction using surface normal maps. With a few minutes, SuperNormal produces detailed surfaces on par with 3D scanners. We harness volume rendering to optimize a neural signed distance function (SDF) powered by multi-resolution hash encoding. To accelerate training, we propose directional finite difference and patch-based ray marching to approximate the SDF gradients numerically. While not compromising reconstruction quality, this strategy is nearly twice as efficient as analytical gradients and about three times faster than axis-aligned finite difference. Experiments on the benchmark dataset demonstrate the superiority of SuperNormal in efficiency and accuracy compared to existing multi-view photometric stereo methods. On our captured objects, SuperNormal produces more fine-grained geometry than recent neural 3D reconstruction methods.

</details>

### MVIP-NeRF: Multi-View 3D Inpainting on NeRF Scenes via Diffusion Prior.
- **链接**: [arXiv:2405.02859](https://arxiv.org/abs/2405.02859) · 📚 被引 27
- **作者**: Honghua Chen, Chen Change Loy, Xingang Pan
- **🏷️ 机构**: Nanyang Technological University,S-Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the emergence of successful NeRF inpainting methods built upon explicit RGB and depth 2D inpainting supervisions, these methods are inherently constrained by the capabilities of their underlying 2D inpainters. This is due to two key reasons: (i) independently inpainting constituent images results in view-inconsistent imagery, and (ii) 2D inpainters struggle to ensure high-quality geometry completion and alignment with inpainted RGB images. To overcome these limitations, we propose a novel approach called MVIP-NeRF that harnesses the potential of diffusion priors for NeRF inpainting, addressing both appearance and geometry aspects. MVIP-NeRF performs joint inpainting across multiple views to reach a consistent solution, which is achieved via an iterative optimization process based on Score Distillation Sampling (SDS). Apart from recovering the rendered RGB images, we also extract normal maps as a geometric representation and define a normal SDS loss that motivates accurate geometry inpainting and alignment with the appearance. Additionally, we formulate a multi-view SDS score function to distill generative priors simultaneously from different view images, ensuring consistent visual completion when dealing with large view variations. Our experimental results show better appearance and geometry recovery than previous NeRF inpainting methods.

</details>

### Sculpt3D: Multi-View Consistent Text-to-3D Generation with Sparse 3D Prior.
- **链接**: [arXiv:2403.09140](https://arxiv.org/abs/2403.09140) · 📚 被引 20
- **作者**: Cheng Chen, Xiaofeng Yang, Fan Yang, Chengzeng Feng, Zhoujie Fu, Chuan-Sheng Foo et al.
- **🏷️ 机构**: Nanyang Technological University, Institute for Infocomm Research A*STAR,Singapore
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works on text-to-3d generation show that using only 2D diffusion supervision for 3D generation tends to produce results with inconsistent appearances (e.g., faces on the back view) and inaccurate shapes (e.g., animals with extra legs). Existing methods mainly address this issue by retraining diffusion models with images rendered from 3D data to ensure multi-view consistency while struggling to balance 2D generation quality with 3D consistency. In this paper, we present a new framework Sculpt3D that equips the current pipeline with explicit injection of 3D priors from retrieved reference objects without re-training the 2D diffusion model. Specifically, we demonstrate that high-quality and diverse 3D geometry can be guaranteed by keypoints supervision through a sparse ray sampling approach. Moreover, to ensure accurate appearances of different views, we further modulate the output of the 2D diffusion model to the correct patterns of the template views without altering the generated object's style. These two decoupled designs effectively harness 3D information from reference objects to generate 3D objects while preserving the generation quality of the 2D diffusion model. Extensive experiments show our method can largely improve the multi-view consistency while retaining fidelity and diversity. Our project page is available at: https://stellarcheng.github.io/Sculpt3D/.

</details>

### 2S-UDF: A Novel Two-Stage UDF Learning Method for Robust Non-Watertight Model Reconstruction from Multi-View Images.
- **链接**: [arXiv:2303.15368](https://arxiv.org/abs/2303.15368) · 📚 被引 10
- **作者**: Junkai Deng, Fei Hou, Xuhui Chen, Wencheng Wang, Ying He
- **🏷️ 机构**: Institute of Software,State Key Laboratory of Computer Science, Chinese Academy of Sciences, School of Computer Science and Engineering, Nanyang Technological University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, building on the foundation of neural radiance field, various techniques have emerged to learn unsigned distance fields (UDF) to reconstruct 3D non-watertight models from multi-view images. Yet, a central challenge in UDF-based volume rendering is formulating a proper way to convert unsigned distance values into volume density, ensuring that the resulting weight function remains unbiased and sensitive to occlusions. Falling short on these requirements often results in incorrect topology or large reconstruction errors in resulting models. This paper addresses this challenge by presenting a novel two-stage algorithm, 2S-UDF, for learning a high-quality UDF from multi-view images. Initially, the method applies an easily trainable density function that, while slightly biased and transparent, aids in coarse reconstruction. The subsequent stage then refines the geometry and appearance of the object to achieve a high-quality reconstruction by directly adjusting the weight function used in volume rendering to ensure that it is unbiased and occlusion-aware. Decoupling density and weight in two stages makes our training stable and robust, distinguishing our technique from existing UDF learning approaches. Evaluations on the DeepFashion3D, DTU, and BlendedMVS datasets validate the robustness and effectiveness of our proposed approach. In both quantitative metrics and visual quality, the results indicate our superior performance over other UDF learning techniques in reconstructing 3D non-watertight models from multi-view images. Our code is available at https://bitbucket.org/jkdeng/2sudf/.

</details>

### VMINer: Versatile Multi-view Inverse Rendering with Near-and Far-field Light Sources.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01121) · 📚 被引 9
- **作者**: Fan Fei, Jiajun Tang, Ping Tan, Boxin Shi
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing, Hong Kong University of Science and Technology
- **会议**: CVPR 2024

### Visual Anagrams: Generating Multi-View Optical Illusions with Diffusion Models.
- **链接**: [arXiv:2311.17919](https://arxiv.org/abs/2311.17919) · 📚 被引 26
- **作者**: Daniel Geng, Inbum Park, Andrew Owens
- **🏷️ 机构**: University of Michigan
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the problem of synthesizing multi-view optical illusions: images that change appearance upon a transformation, such as a flip or rotation. We propose a simple, zero-shot method for obtaining these illusions from off-the-shelf text-to-image diffusion models. During the reverse diffusion process, we estimate the noise from different views of a noisy image, and then combine these noise estimates together and denoise the image. A theoretical analysis suggests that this method works precisely for views that can be written as orthogonal transformations, of which permutations are a subset. This leads to the idea of a visual anagram--an image that changes appearance under some rearrangement of pixels. This includes rotations and flips, but also more exotic pixel permutations such as a jigsaw rearrangement. Our approach also naturally extends to illusions with more than two views. We provide both qualitative and quantitative results demonstrating the effectiveness and flexibility of our method. Please see our project webpage for additional visualizations and results: https://dangeng.github.io/visual_anagrams/

</details>

### EpiDiff: Enhancing Multi-View Synthesis via Localized Epipolar-Constrained Diffusion.
- **链接**: [arXiv:2312.06725](https://arxiv.org/abs/2312.06725) · 📚 被引 40
- **作者**: Zehuan Huang, Hao Wen, Junting Dong, Yaohui Wang, Yangguang Li, Xinyuan Chen et al.
- **🏷️ 机构**: Beihang University, Shanghai AI Laboratory, VAST
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating multiview images from a single view facilitates the rapid generation of a 3D mesh conditioned on a single image. Recent methods that introduce 3D global representation into diffusion models have shown the potential to generate consistent multiviews, but they have reduced generation speed and face challenges in maintaining generalizability and quality. To address this issue, we propose EpiDiff, a localized interactive multiview diffusion model. At the core of the proposed approach is to insert a lightweight epipolar attention block into the frozen diffusion model, leveraging epipolar constraints to enable cross-view interaction among feature maps of neighboring views. The newly initialized 3D modeling module preserves the original feature distribution of the diffusion model, exhibiting compatibility with a variety of base diffusion models. Experiments show that EpiDiff generates 16 multiview images in just 12 seconds, and it surpasses previous methods in quality evaluation metrics, including PSNR, SSIM and LPIPS. Additionally, EpiDiff can generate a more diverse distribution of views, improving the reconstruction quality from generated multiviews. Please see our project page at https://huanngzh.github.io/EpiDiff/.

</details>

### ESR-NeRF: Emissive Source Reconstruction Using LDR Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00440) · 📚 被引 4
- **作者**: Jinseo Jeong, Junseo Koo, Qimeng Zhang, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: CVPR 2024

### SPAD: Spatially Aware Multi-View Diffusers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00956) · 📚 被引 22
- **作者**: Yash Kant, Aliaksandr Siarohin, Ziyi Wu, Michael Vasilkovsky, Guocheng Qian, Jian Ren et al.
- **🏷️ 机构**: University of Toronto, Snap Research, KAUST
- **会议**: CVPR 2024

### MAS: Multi-view Ancestral Sampling for 3D Motion Generation Using 2D Diffusion.
- **链接**: [arXiv:2310.14729](https://arxiv.org/abs/2310.14729) · 📚 被引 14
- **作者**: Roy Kapon, Guy Tevet, Daniel Cohen-Or, Amit H. Bermano
- **🏷️ 机构**: Tel Aviv University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Multi-view Ancestral Sampling (MAS), a method for 3D motion generation, using 2D diffusion models that were trained on motions obtained from in-the-wild videos. As such, MAS opens opportunities to exciting and diverse fields of motion previously under-explored as 3D data is scarce and hard to collect. MAS works by simultaneously denoising multiple 2D motion sequences representing different views of the same 3D motion. It ensures consistency across all views at each diffusion step by combining the individual generations into a unified 3D sequence, and projecting it back to the original views. We demonstrate MAS on 2D pose data acquired from videos depicting professional basketball maneuvers, rhythmic gymnastic performances featuring a ball apparatus, and horse races. In each of these domains, 3D motion capture is arduous, and yet, MAS generates diverse and realistic 3D sequences. Unlike the Score Distillation approach, which optimizes each sample by repeatedly applying small fixes, our method uses a sampling process that was constructed for the diffusion framework. As we demonstrate, MAS avoids common issues such as out-of-domain sampling and mode-collapse. https://guytevet.github.io/mas-page/

</details>

### Rethinking Multi-View Representation Learning via Distilled Disentangling.
- **链接**: [arXiv:2403.10897](https://arxiv.org/abs/2403.10897) · 📚 被引 30
- **作者**: Guanzhou Ke, Bo Wang, Xiaoli Wang, Shengfeng He
- **🏷️ 机构**: Beijing Jiaotong University, Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, Nanjing University of Science and Technology
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view representation learning aims to derive robust representations that are both view-consistent and view-specific from diverse data sources. This paper presents an in-depth analysis of existing approaches in this domain, highlighting a commonly overlooked aspect: the redundancy between view-consistent and view-specific representations. To this end, we propose an innovative framework for multi-view representation learning, which incorporates a technique we term 'distilled disentangling'. Our method introduces the concept of masked cross-view prediction, enabling the extraction of compact, high-quality view-consistent representations from various sources without incurring extra computational overhead. Additionally, we develop a distilled disentangling module that efficiently filters out consistency-related information from multi-view representations, resulting in purer view-specific representations. This approach significantly reduces redundancy between view-consistent and view-specific representations, enhancing the overall efficiency of the learning process. Our empirical evaluations reveal that higher mask ratios substantially improve the quality of view-consistent representations. Moreover, we find that reducing the dimensionality of view-consistent representations relative to that of view-specific representations further refines the quality of the combined representations. Our code is accessible at: https://github.com/Guanzhou-Ke/MRDD.

</details>

### UnionFormer: Unified-Learning Transformer with Multi-View Representation for Image Manipulation Detection and Localization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01190) · 📚 被引 22
- **作者**: Shuaibo Li, Wei Ma, Jianwei Guo, Shibiao Xu, Benchong Li, Xiaopeng Zhang
- **🏷️ 机构**: Beijing University of Technology, Institute of Automation, Chinese Academy of Sciences,MAIS, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2024

### One-2-3-45++: Fast Single Image to 3D Objects with Consistent Multi-View Generation and 3D Diffusion.
- **链接**: [arXiv:2311.07885](https://arxiv.org/abs/2311.07885) · 📚 被引 155
- **作者**: Minghua Liu, Ruoxi Shi, Linghao Chen, Zhuoyang Zhang, Chao Xu, Xinyue Wei et al.
- **🏷️ 机构**: UC San Diego, Tsinghua University, UCLA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in open-world 3D object generation have been remarkable, with image-to-3D methods offering superior fine-grained control over their text-to-3D counterparts. However, most existing models fall short in simultaneously providing rapid generation speeds and high fidelity to input images - two features essential for practical applications. In this paper, we present One-2-3-45++, an innovative method that transforms a single image into a detailed 3D textured mesh in approximately one minute. Our approach aims to fully harness the extensive knowledge embedded in 2D diffusion models and priors from valuable yet limited 3D data. This is achieved by initially finetuning a 2D diffusion model for consistent multi-view image generation, followed by elevating these images to 3D with the aid of multi-view conditioned 3D native diffusion models. Extensive experimental evaluations demonstrate that our method can produce high-quality, diverse 3D assets that closely mirror the original input image. Our project webpage: https://sudo-ai-3d.github.io/One2345plus_page.

</details>

### S2MVTC: A Simple Yet Efficient Scalable Multi-View Tensor Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02274) · 📚 被引 23
- **作者**: Zhen Long, Qiyuan Wang, Yazhou Ren, Yipeng Liu, Ce Zhu
- **🏷️ 机构**: University of Electronic Science &#x0026; Technology of China
- **会议**: CVPR 2024

### Direct2.5: Diverse Text-to-3D Generation via Multi-view 2.5D Diffusion.
- **链接**: [arXiv:2311.15980](https://arxiv.org/abs/2311.15980) · 📚 被引 22
- **作者**: Yuanxun Lu, Jingyang Zhang, Shiwei Li, Tian Fang, David McKinnon, Yanghai Tsin et al.
- **🏷️ 机构**: Nanjing University, Apple, The Hong Kong University of Science and Technology
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in generative AI have unveiled significant potential for the creation of 3D content. However, current methods either apply a pre-trained 2D diffusion model with the time-consuming score distillation sampling (SDS), or a direct 3D diffusion model trained on limited 3D data losing generation diversity. In this work, we approach the problem by employing a multi-view 2.5D diffusion fine-tuned from a pre-trained 2D diffusion model. The multi-view 2.5D diffusion directly models the structural distribution of 3D data, while still maintaining the strong generalization ability of the original 2D diffusion model, filling the gap between 2D diffusion-based and direct 3D diffusion-based methods for 3D content generation. During inference, multi-view normal maps are generated using the 2.5D diffusion, and a novel differentiable rasterization scheme is introduced to fuse the almost consistent multi-view normal maps into a consistent 3D model. We further design a normal-conditioned multi-view image generation module for fast appearance generation given the 3D geometry. Our method is a one-pass diffusion process and does not require any SDS optimization as post-processing. We demonstrate through extensive experiments that, our direct 2.5D generation with the specially-designed fusion scheme can achieve diverse, mode-seeking-free, and high-fidelity 3D content generation in only 10 seconds. Project page: https://nju-3dv.github.io/projects/direct25.

</details>

### Wired Perspectives: Multi-View Wire Art Embraces Generative AI.
- **链接**: [arXiv:2311.15421](https://arxiv.org/abs/2311.15421) · 📚 被引 9
- **作者**: Zhiyu Qu, Lan Yang, Honggang Zhang, Tao Xiang, Kaiyue Pang, Yi-Zhe Song
- **🏷️ 机构**: SketchX, CVSSP, University of Surrey, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Creating multi-view wire art (MVWA), a static 3D sculpture with diverse interpretations from different viewpoints, is a complex task even for skilled artists. In response, we present DreamWire, an AI system enabling everyone to craft MVWA easily. Users express their vision through text prompts or scribbles, freeing them from intricate 3D wire organisation. Our approach synergises 3D Bézier curves, Prim's algorithm, and knowledge distillation from diffusion models or their variants (e.g., ControlNet). This blend enables the system to represent 3D wire art, ensuring spatial continuity and overcoming data scarcity. Extensive evaluation and analysis are conducted to shed insight on the inner workings of the proposed system, including the trade-off between connectivity and visual aesthetics.

</details>

### MVCPS-NeuS: Multi-View Constrained Photometric Stereo for Neural Surface Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01935) · 📚 被引 7
- **作者**: Hiroaki Santo, Fumio Okura, Yasuyuki Matsushita
- **🏷️ 机构**: Graduate School of Information Science and Technology, Osaka University
- **会议**: CVPR 2024

### Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection.
- **链接**: [arXiv:2403.12580](https://arxiv.org/abs/2403.12580) · 📚 被引 119
- **作者**: Chengjie Wang, Wenbing Zhu, Bin-Bin Gao, Zhenye Gan, Jiangning Zhang, Zhihao Gu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Fudan University, Youtu Lab,Tencent
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Industrial anomaly detection (IAD) has garnered significant attention and experienced rapid development. However, the recent development of IAD approach has encountered certain difficulties due to dataset limitations. On the one hand, most of the state-of-the-art methods have achieved saturation (over 99% in AUROC) on mainstream datasets such as MVTec, and the differences of methods cannot be well distinguished, leading to a significant gap between public datasets and actual application scenarios. On the other hand, the research on various new practical anomaly detection settings is limited by the scale of the dataset, posing a risk of overfitting in evaluation results. Therefore, we propose a large-scale, Real-world, and multi-view Industrial Anomaly Detection dataset, named Real-IAD, which contains 150K high-resolution images of 30 different objects, an order of magnitude larger than existing datasets. It has a larger range of defect area and ratio proportions, making it more challenging than previous datasets. To make the dataset closer to real application scenarios, we adopted a multi-view shooting method and proposed sample-level evaluation metrics. In addition, beyond the general unsupervised anomaly detection setting, we propose a new setting for Fully Unsupervised Industrial Anomaly Detection (FUIAD) based on the observation that the yield rate in industrial production is usually greater than 60%, which has more practical application value. Finally, we report the results of popular IAD methods on the Real-IAD dataset, providing a highly challenging benchmark to promote the development of the IAD field.

</details>

### GoMVS: Geometrically Consistent Cost Aggregation for Multi-View Stereo.
- **链接**: [arXiv:2404.07992](https://arxiv.org/abs/2404.07992) · 📚 被引 47
- **作者**: Jiang Wu, Rui Li, Haofei Xu, Wenxun Zhao, Yu Zhu, Jinqiu Sun et al.
- **🏷️ 机构**: Northwestern Poly technical University, ETH Zurich
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Matching cost aggregation plays a fundamental role in learning-based multi-view stereo networks. However, directly aggregating adjacent costs can lead to suboptimal results due to local geometric inconsistency. Related methods either seek selective aggregation or improve aggregated depth in the 2D space, both are unable to handle geometric inconsistency in the cost volume effectively. In this paper, we propose GoMVS to aggregate geometrically consistent costs, yielding better utilization of adjacent geometries. More specifically, we correspond and propagate adjacent costs to the reference pixel by leveraging the local geometric smoothness in conjunction with surface normals. We achieve this by the geometric consistent propagation (GCP) module. It computes the correspondence from the adjacent depth hypothesis space to the reference depth space using surface normals, then uses the correspondence to propagate adjacent costs to the reference geometry, followed by a convolution for aggregation. Our method achieves new state-of-the-art performance on DTU, Tanks & Temple, and ETH3D datasets. Notably, our method ranks 1st on the Tanks & Temple Advanced benchmark.

</details>

### Carve3D: Improving Multi-view Reconstruction Consistency for Diffusion Models with RL Finetuning.
- **链接**: [arXiv:2312.13980](https://arxiv.org/abs/2312.13980) · 📚 被引 12
- **作者**: Desai Xie, Jiahao Li, Hao Tan, Xin Sun, Zhixin Shu, Yi Zhou et al.
- **🏷️ 机构**: Adobe Research, Kiel University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view diffusion models, obtained by applying Supervised Finetuning (SFT) to text-to-image diffusion models, have driven recent breakthroughs in text-to-3D research. However, due to the limited size and quality of existing 3D datasets, they still suffer from multi-view inconsistencies and Neural Radiance Field (NeRF) reconstruction artifacts. We argue that multi-view diffusion models can benefit from further Reinforcement Learning Finetuning (RLFT), which allows models to learn from the data generated by themselves and improve beyond their dataset limitations during SFT. To this end, we introduce Carve3D, an improved RLFT algorithm coupled with a novel Multi-view Reconstruction Consistency (MRC) metric, to enhance the consistency of multi-view diffusion models. To measure the MRC metric on a set of multi-view images, we compare them with their corresponding NeRF renderings at the same camera viewpoints. The resulting model, which we denote as Carve3DM, demonstrates superior multi-view consistency and NeRF reconstruction quality than existing models. Our results suggest that pairing SFT with Carve3D's RLFT is essential for developing multi-view-consistent diffusion models, mirroring the standard Large Language Model (LLM) alignment pipeline. Our code, training and testing data, and video results are available at: https://desaixie.github.io/carve-3d.

</details>

### MVHumanNet: A Large-Scale Dataset of Multi-View Daily Dressing Human Captures.
- **链接**: [arXiv:2312.02963](https://arxiv.org/abs/2312.02963) · 📚 被引 31
- **作者**: Zhangyang Xiong, Chenghong Li, Kenkun Liu, Hongjie Liao, Jianqiao Hu, Junyi Zhu et al.
- **🏷️ 机构**: FNii, CUHKSZ, SSE, CUHKSZ
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this era, the success of large language models and text-to-image models can be attributed to the driving force of large-scale datasets. However, in the realm of 3D vision, while remarkable progress has been made with models trained on large-scale synthetic and real-captured object data like Objaverse and MVImgNet, a similar level of progress has not been observed in the domain of human-centric tasks partially due to the lack of a large-scale human dataset. Existing datasets of high-fidelity 3D human capture continue to be mid-sized due to the significant challenges in acquiring large-scale high-quality 3D human data. To bridge this gap, we present MVHumanNet, a dataset that comprises multi-view human action sequences of 4,500 human identities. The primary focus of our work is on collecting human data that features a large number of diverse identities and everyday clothing using a multi-view human capture system, which facilitates easily scalable data collection. Our dataset contains 9,000 daily outfits, 60,000 motion sequences and 645 million frames with extensive annotations, including human masks, camera parameters, 2D and 3D keypoints, SMPL/SMPLX parameters, and corresponding textual descriptions. To explore the potential of MVHumanNet in various 2D and 3D visual tasks, we conducted pilot studies on view-consistent action recognition, human NeRF reconstruction, text-driven view-unconstrained human image generation, as well as 2D view-unconstrained human image and 3D avatar generation. Extensive experiments demonstrate the performance improvements and effective applications enabled by the scale provided by MVHumanNet. As the current largest-scale 3D human dataset, we hope that the release of MVHumanNet data with annotations will foster further innovations in the domain of 3D human-centric tasks at scale.

</details>

### Differentiable Information Bottleneck for Deterministic Multi-View Clustering.
- **链接**: [arXiv:2403.15681](https://arxiv.org/abs/2403.15681) · 📚 被引 28
- **作者**: Xiaoqiang Yan, Zhixiang Jin, Fengshou Han, Yangdong Ye
- **🏷️ 机构**: School of Computer and Artificial Intelligence, Zhengzhou University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent several years, the information bottleneck (IB) principle provides an information-theoretic framework for deep multi-view clustering (MVC) by compressing multi-view observations while preserving the relevant information of multiple views. Although existing IB-based deep MVC methods have achieved huge success, they rely on variational approximation and distribution assumption to estimate the lower bound of mutual information, which is a notoriously hard and impractical problem in high-dimensional multi-view spaces. In this work, we propose a new differentiable information bottleneck (DIB) method, which provides a deterministic and analytical MVC solution by fitting the mutual information without the necessity of variational approximation. Specifically, we first propose to directly fit the mutual information of high-dimensional spaces by leveraging normalized kernel Gram matrix, which does not require any auxiliary neural estimator to estimate the lower bound of mutual information. Then, based on the new mutual information measurement, a deterministic multi-view neural network with analytical gradients is explicitly trained to parameterize IB principle, which derives a deterministic compression of input variables from different views. Finally, a triplet consistency discovery mechanism is devised, which is capable of mining the feature consistency, cluster consistency and joint consistency based on the deterministic and compact representations. Extensive experimental results show the superiority of our DIB method on 6 benchmarks compared with 13 state-of-the-art baselines.

</details>

### ConsistNet: Enforcing 3D Consistency for Multi-View Images Diffusion.
- **链接**: [arXiv:2310.10343](https://arxiv.org/abs/2310.10343) · 📚 被引 34
- **作者**: Jiayu Yang, Ziang Cheng, Yunfei Duan, Pan Ji, Hongdong Li
- **🏷️ 机构**: Tencent, Australian National University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Given a single image of a 3D object, this paper proposes a novel method (named ConsistNet) that is able to generate multiple images of the same object, as if seen they are captured from different viewpoints, while the 3D (multi-view) consistencies among those multiple generated images are effectively exploited. Central to our method is a multi-view consistency block which enables information exchange across multiple single-view diffusion processes based on the underlying multi-view geometry principles. ConsistNet is an extension to the standard latent diffusion model, and consists of two sub-modules: (a) a view aggregation module that unprojects multi-view features into global 3D volumes and infer consistency, and (b) a ray aggregation module that samples and aggregate 3D consistent features back to each view to enforce consistency. Our approach departs from previous methods in multi-view image generation, in that it can be easily dropped-in pre-trained LDMs without requiring explicit pixel correspondences or depth prediction. Experiments show that our method effectively learns 3D consistency over a frozen Zero123 backbone and can generate 16 surrounding views of the object within 40 seconds on a single A100 GPU. Our code will be made available on https://github.com/JiayuYANG/ConsistNet

</details>

### DreamComposer: Controllable 3D Object Generation via Multi-View Conditions.
- **链接**: [arXiv:2312.03611](https://arxiv.org/abs/2312.03611) · 📚 被引 10
- **作者**: Yunhan Yang, Yukun Huang, Xiaoyang Wu, Yuan-Chen Guo, Song-Hai Zhang, Hengshuang Zhao et al.
- **🏷️ 机构**: The University of Hong Kong, VAST, Tsinghua University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Utilizing pre-trained 2D large-scale generative models, recent works are capable of generating high-quality novel views from a single in-the-wild image. However, due to the lack of information from multiple views, these works encounter difficulties in generating controllable novel views. In this paper, we present DreamComposer, a flexible and scalable framework that can enhance existing view-aware diffusion models by injecting multi-view conditions. Specifically, DreamComposer first uses a view-aware 3D lifting module to obtain 3D representations of an object from multiple views. Then, it renders the latent features of the target view from 3D representations with the multi-view feature fusion module. Finally the target view features extracted from multi-view inputs are injected into a pre-trained diffusion model. Experiments show that DreamComposer is compatible with state-of-the-art diffusion models for zero-shot novel view synthesis, further enhancing them to generate high-fidelity novel view images with multi-view conditions, ready for controllable 3D object reconstruction and various other applications.

</details>

### Multi-View Aggregation Network for Dichotomous Image Segmentation.
- **链接**: [arXiv:2404.07445](https://arxiv.org/abs/2404.07445) · 📚 被引 19
- **作者**: Qian Yu, Xiaoqi Zhao, Youwei Pang, Lihe Zhang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dichotomous Image Segmentation (DIS) has recently emerged towards high-precision object segmentation from high-resolution natural images. When designing an effective DIS model, the main challenge is how to balance the semantic dispersion of high-resolution targets in the small receptive field and the loss of high-precision details in the large receptive field. Existing methods rely on tedious multiple encoder-decoder streams and stages to gradually complete the global localization and local refinement. Human visual system captures regions of interest by observing them from multiple views. Inspired by it, we model DIS as a multi-view object perception problem and provide a parsimonious multi-view aggregation network (MVANet), which unifies the feature fusion of the distant view and close-up view into a single stream with one encoder-decoder structure. With the help of the proposed multi-view complementary localization and refinement modules, our approach established long-range, profound visual interactions across multiple views, allowing the features of the detailed close-up view to focus on highly slender structures.Experiments on the popular DIS-5K dataset show that our MVANet significantly outperforms state-of-the-art methods in both accuracy and speed. The source code and datasets will be publicly available at \href{https://github.com/qianyu-dlut/MVANet}{MVANet}.

</details>

### TULIP: Multi-Camera 3D Precision Assessment of Parkinson's Disease.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02128) · 📚 被引 9
- **作者**: Kyungdo Kim, Sihan Lyu, Sneha Mantri, Timothy W. Dunn
- **🏷️ 机构**: Duke University,Department of Biomedical Engineering,Durham,NC,USA, Duke University,Department of Neurology,Durham,NC,USA
- **会议**: CVPR 2024

### Mind The Edge: Refining Depth Edges in Sparsely-Supervised Monocular Depth Estimation.
- **链接**: [arXiv:2212.05315](https://arxiv.org/abs/2212.05315) · 📚 被引 11
- **作者**: Lior Talker, Aviad Cohen, Erez Yosef, Alexandra Dana, Michael Dinerstein
- **🏷️ 机构**: Samsung Israel R&#x0026;D Center,Tel Aviv,Israel
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular Depth Estimation (MDE) is a fundamental problem in computer vision with numerous applications. Recently, LIDAR-supervised methods have achieved remarkable per-pixel depth accuracy in outdoor scenes. However, significant errors are typically found in the proximity of depth discontinuities, i.e., depth edges, which often hinder the performance of depth-dependent applications that are sensitive to such inaccuracies, e.g., novel view synthesis and augmented reality. Since direct supervision for the location of depth edges is typically unavailable in sparse LIDAR-based scenes, encouraging the MDE model to produce correct depth edges is not straightforward. To the best of our knowledge this paper is the first attempt to address the depth edges issue for LIDAR-supervised scenes. In this work we propose to learn to detect the location of depth edges from densely-supervised synthetic data, and use it to generate supervision for the depth edges in the MDE training. To quantitatively evaluate our approach, and due to the lack of depth edges GT in LIDAR-based scenes, we manually annotated subsets of the KITTI and the DDAD datasets with depth edges ground truth. We demonstrate significant gains in the accuracy of the depth edges with comparable per-pixel depth accuracy on several challenging datasets. Code and datasets are available at \url{https://github.com/liortalker/MindTheEdge}.

</details>

### Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation.
- **链接**: [arXiv:2312.02145](https://arxiv.org/abs/2312.02145) · 📚 被引 470
- **作者**: Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, Konrad Schindler
- **🏷️ 机构**: Photogrammetry and Remote Sensing, ETH Z&#x00FC;rich
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation is a fundamental computer vision task. Recovering 3D depth from a single image is geometrically ill-posed and requires scene understanding, so it is not surprising that the rise of deep learning has led to a breakthrough. The impressive progress of monocular depth estimators has mirrored the growth in model capacity, from relatively modest CNNs to large Transformer architectures. Still, monocular depth estimators tend to struggle when presented with images with unfamiliar content and layout, since their knowledge of the visual world is restricted by the data seen during training, and challenged by zero-shot generalization to new domains. This motivates us to explore whether the extensive priors captured in recent generative diffusion models can enable better, more generalizable depth estimation. We introduce Marigold, a method for affine-invariant monocular depth estimation that is derived from Stable Diffusion and retains its rich prior knowledge. The estimator can be fine-tuned in a couple of days on a single GPU using only synthetic training data. It delivers state-of-the-art performance across a wide range of datasets, including over 20% performance gains in specific cases. Project page: https://marigoldmonodepth.github.io.

</details>

### From-Ground-To-Objects: Coarse-to-Fine Self-supervised Monocular Depth Estimation of Dynamic Objects with Ground Contact Prior.
- **链接**: [arXiv:2312.10118](https://arxiv.org/abs/2312.10118) · 📚 被引 17
- **作者**: Jaeho Moon, Juan Luis Gonzalez Bello, Byeongjun Kwon, Munchurl Kim
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised monocular depth estimation (DE) is an approach to learning depth without costly depth ground truths. However, it often struggles with moving objects that violate the static scene assumption during training. To address this issue, we introduce a coarse-to-fine training strategy leveraging the ground contacting prior based on the observation that most moving objects in outdoor scenes contact the ground. In the coarse training stage, we exclude the objects in dynamic classes from the reprojection loss calculation to avoid inaccurate depth learning. To provide precise supervision on the depth of the objects, we present a novel Ground-contacting-prior Disparity Smoothness Loss (GDS-Loss) that encourages a DE network to align the depth of the objects with their ground-contacting points. Subsequently, in the fine training stage, we refine the DE network to learn the detailed depth of the objects from the reprojection loss, while ensuring accurate DE on the moving object regions by employing our regularization loss with a cost-volume-based weighting factor. Our overall coarse-to-fine training strategy can easily be integrated with existing DE methods without any modifications, significantly enhancing DE performance on challenging Cityscapes and KITTI datasets, especially in the moving object regions.

</details>

### Mining Supervision for Dynamic Regions in Self-Supervised Monocular Depth Estimation.
- **链接**: [arXiv:2404.14908](https://arxiv.org/abs/2404.14908) · 📚 被引 8
- **作者**: Hoang Chuong Nguyen, Tianyu Wang, José M. Álvarez, Miaomiao Liu
- **🏷️ 机构**: Australian National University, NVIDIA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focuses on self-supervised monocular depth estimation in dynamic scenes trained on monocular videos. Existing methods jointly estimate pixel-wise depth and motion, relying mainly on an image reconstruction loss. Dynamic regions1 remain a critical challenge for these methods due to the inherent ambiguity in depth and motion estimation, resulting in inaccurate depth estimation. This paper proposes a self-supervised training framework exploiting pseudo depth labels for dynamic regions from training data. The key contribution of our framework is to decouple depth estimation for static and dynamic regions of images in the training data. We start with an unsupervised depth estimation approach, which provides reliable depth estimates for static regions and motion cues for dynamic regions and allows us to extract moving object information at the instance level. In the next stage, we use an object network to estimate the depth of those moving objects assuming rigid motions. Then, we propose a new scale alignment module to address the scale ambiguity between estimated depths for static and dynamic regions. We can then use the depth labels generated to train an end-to-end depth estimation network and improve its performance. Extensive experiments on the Cityscapes and KITTI datasets show that our self-training strategy consistently outperforms existing self/unsupervised depth estimation methods.

</details>

### ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation.
- **链接**: [arXiv:2403.18807](https://arxiv.org/abs/2403.18807) · 📚 被引 56
- **作者**: Suraj Patni, Aradhye Agarwal, Chetan Arora
- **🏷️ 机构**: Indian Institute of Technology Delhi
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the absence of parallax cues, a learning-based single image depth estimation (SIDE) model relies heavily on shading and contextual cues in the image. While this simplicity is attractive, it is necessary to train such models on large and varied datasets, which are difficult to capture. It has been shown that using embeddings from pre-trained foundational models, such as CLIP, improves zero shot transfer in several applications. Taking inspiration from this, in our paper we explore the use of global image priors generated from a pre-trained ViT model to provide more detailed contextual information. We argue that the embedding vector from a ViT model, pre-trained on a large dataset, captures greater relevant information for SIDE than the usual route of generating pseudo image captions, followed by CLIP based text embeddings. Based on this idea, we propose a new SIDE model using a diffusion backbone which is conditioned on ViT embeddings. Our proposed design establishes a new state-of-the-art (SOTA) for SIDE on NYUv2 dataset, achieving Abs Rel error of 0.059 (14% improvement) compared to 0.069 by the current SOTA (VPD). And on KITTI dataset, achieving Sq Rel error of 0.139 (2% improvement) compared to 0.142 by the current SOTA (GEDepth). For zero-shot transfer with a model trained on NYUv2, we report mean relative improvement of (20%, 23%, 81%, 25%) over NeWCRFs on (Sun-RGBD, iBims1, DIODE, HyperSim) datasets, compared to (16%, 18%, 45%, 9%) by ZoeDepth. The project page is available at https://ecodepth-iitd.github.io

</details>

### WorDepth: Variational Language Prior for Monocular Depth Estimation.
- **链接**: [arXiv:2404.03635](https://arxiv.org/abs/2404.03635) · 📚 被引 30
- **作者**: Ziyao Zeng, Daniel Wang, Fengyu Yang, Hyoungseob Park, Stefano Soatto, Dong Lao et al.
- **🏷️ 机构**: Yale University, University of California,Los Angeles
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Three-dimensional (3D) reconstruction from a single image is an ill-posed problem with inherent ambiguities, i.e. scale. Predicting a 3D scene from text description(s) is similarly ill-posed, i.e. spatial arrangements of objects described. We investigate the question of whether two inherently ambiguous modalities can be used in conjunction to produce metric-scaled reconstructions. To test this, we focus on monocular depth estimation, the problem of predicting a dense depth map from a single image, but with an additional text caption describing the scene. To this end, we begin by encoding the text caption as a mean and standard deviation; using a variational framework, we learn the distribution of the plausible metric reconstructions of 3D scenes corresponding to the text captions as a prior. To "select" a specific reconstruction or depth map, we encode the given image through a conditional sampler that samples from the latent space of the variational text encoder, which is then decoded to the output depth map. Our approach is trained alternatingly between the text and image branches: in one optimization step, we predict the mean and standard deviation from the text description and sample from a standard Gaussian, and in the other, we sample using a (image) conditional sampler. Once trained, we directly predict depth from the encoded text using the conditional sampler. We demonstrate our approach on indoor (NYUv2) and outdoor (KITTI) scenarios, where we show that language can consistently improve performance in both.

</details>

### Physical 3D Adversarial Attacks against Monocular Depth Estimation in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02308) · 📚 被引 57
- **作者**: Junhao Zheng, Chenhao Lin, Jiahao Sun, Zhengyu Zhao, Qian Li, Chao Shen
- **🏷️ 机构**: Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China,710049
- **会议**: CVPR 2024

### Driving Into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving.
- **链接**: [arXiv:2311.17918](https://arxiv.org/abs/2311.17918) · 📚 被引 116
- **作者**: Yuqi Wang, Jiawei He, Lue Fan, Hongxin Li, Yuntao Chen, Zhaoxiang Zhang
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences (UCAS), Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, MAIS, Centre for Artificial Intelligence and Robotics (HKISI_CAS)
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

</details>

### Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving.
- **链接**: [arXiv:2404.04804](https://arxiv.org/abs/2404.04804) · 📚 被引 74
- **作者**: Jinlong Li, Baolu Li, Zhengzhong Tu, Xinyu Liu, Qing Guo, Felix Juefei-Xu et al.
- **🏷️ 机构**: Cleveland State University, University of Texas at Austin, Centre for Frontier AI Research (CFAR), A&#x002A;STAR
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-centric perception systems for autonomous driving have gained considerable attention recently due to their cost-effectiveness and scalability, especially compared to LiDAR-based systems. However, these systems often struggle in low-light conditions, potentially compromising their performance and safety. To address this, our paper introduces LightDiff, a domain-tailored framework designed to enhance the low-light image quality for autonomous driving applications. Specifically, we employ a multi-condition controlled diffusion model. LightDiff works without any human-collected paired data, leveraging a dynamic data degradation process instead. It incorporates a novel multi-condition adapter that adaptively controls the input weights from different modalities, including depth maps, RGB images, and text captions, to effectively illuminate dark scenes while maintaining context consistency. Furthermore, to align the enhanced images with the detection model's knowledge, LightDiff employs perception-specific scores as rewards to guide the diffusion training process through reinforcement learning. Extensive experiments on the nuScenes datasets demonstrate that LightDiff can significantly improve the performance of several state-of-the-art 3D detectors in night-time conditions while achieving high visual quality scores, highlighting its potential to safeguard autonomous driving.

</details>

### OPEN: Object-Wise Position Embedding for Multi-view 3D Object Detection.
- **链接**: [arXiv:2407.10753](https://arxiv.org/abs/2407.10753) · 📚 被引 15
- **作者**: Jinghua Hou, Tong Wang, Xiaoqing Ye, Zhe Liu, Shi Gong, Xiao Tan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate depth information is crucial for enhancing the performance of multi-view 3D object detection. Despite the success of some existing multi-view 3D detectors utilizing pixel-wise depth supervision, they overlook two significant phenomena: 1) the depth supervision obtained from LiDAR points is usually distributed on the surface of the object, which is not so friendly to existing DETR-based 3D detectors due to the lack of the depth of 3D object center; 2) for distant objects, fine-grained depth estimation of the whole object is more challenging. Therefore, we argue that the object-wise depth (or 3D center of the object) is essential for accurate detection. In this paper, we propose a new multi-view 3D object detector named OPEN, whose main idea is to effectively inject object-wise depth information into the network through our proposed object-wise position embedding. Specifically, we first employ an object-wise depth encoder, which takes the pixel-wise depth map as a prior, to accurately estimate the object-wise depth. Then, we utilize the proposed object-wise position embedding to encode the object-wise depth information into the transformer decoder, thereby producing 3D object-aware features for final detection. Extensive experiments verify the effectiveness of our proposed method. Furthermore, OPEN achieves a new state-of-the-art performance with 64.4% NDS and 56.7% mAP on the nuScenes test benchmark.

</details>

### Learning High-Resolution Vector Representation from Multi-camera Images for 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72761-0_22) · 📚 被引 3
- **作者**: Zhili Chen, Shuangjie Xu, Maosheng Ye, Zian Qian, Xiaoyi Zou, Dit-Yan Yeung et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Ray Denoising: Depth-Aware Hard Negative Sampling for Multi-view 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72967-6_12) · 📚 被引 27
- **作者**: Feng Liu, Tengteng Huang, Qianjing Zhang, Haotian Yao, Chi Zhang, Fang Wan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### AEDNet: Adaptive Embedding and Multiview-Aware Disentanglement for Point Cloud Completion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73247-8_8) · 📚 被引 4
- **作者**: Zhiheng Fu, Longguang Wang, Lian Xu, Zhiyong Wang, Hamid Laga, Yulan Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### BLINK: Multimodal Large Language Models Can See but Not Perceive.
- **链接**: [arXiv:2404.12390](https://arxiv.org/abs/2404.12390) · 📚 被引 60
- **作者**: Xingyu Fu, Yushi Hu, Bangzheng Li, Yu Feng, Haoyu Wang, Xudong Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Blink, a new benchmark for multimodal language models (LLMs) that focuses on core visual perception abilities not found in other evaluations. Most of the Blink tasks can be solved by humans "within a blink" (e.g., relative depth estimation, visual correspondence, forensics detection, and multi-view reasoning). However, we find these perception-demanding tasks cast significant challenges for current multimodal LLMs because they resist mediation through natural language. Blink reformats 14 classic computer vision tasks into 3,807 multiple-choice questions, paired with single or multiple images and visual prompting. While humans get 95.70% accuracy on average, Blink is surprisingly challenging for existing multimodal LLMs: even the best-performing GPT-4V and Gemini achieve accuracies of 51.26% and 45.72%, only 13.17% and 7.63% higher than random guessing, indicating that such perception abilities have not "emerged" yet in recent multimodal LLMs. Our analysis also highlights that specialist CV models could solve these problems much better, suggesting potential pathways for future improvements. We believe Blink will stimulate the community to help multimodal LLMs catch up with human-level visual perception.

</details>

### Multi-View Representation is What You Need for Point-Cloud Pre-Training.
- **链接**: [出版页](https://openreview.net/forum?id=imZcqOrbig)
- **作者**: Siming Yan, Chen Song, Youkang Kong, Qixing Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### MVSFormer++: Revealing the Devil in Transformer's Details for Multi-View Stereo.
- **链接**: [arXiv:2401.11673](https://arxiv.org/abs/2401.11673)
- **作者**: Chenjie Cao, Xinlin Ren, Yanwei Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in learning-based Multi-View Stereo (MVS) methods have prominently featured transformer-based models with attention mechanisms. However, existing approaches have not thoroughly investigated the profound influence of transformers on different MVS modules, resulting in limited depth estimation capabilities. In this paper, we introduce MVSFormer++, a method that prudently maximizes the inherent characteristics of attention to enhance various components of the MVS pipeline. Formally, our approach involves infusing cross-view information into the pre-trained DINOv2 model to facilitate MVS learning. Furthermore, we employ different attention mechanisms for the feature encoder and cost volume regularization, focusing on feature and spatial aggregations respectively. Additionally, we uncover that some design details would substantially impact the performance of transformer modules in MVS, including normalized 3D positional encoding, adaptive attention scaling, and the position of layer normalization. Comprehensive experiments on DTU, Tanks-and-Temples, BlendedMVS, and ETH3D validate the effectiveness of the proposed method. Notably, MVSFormer++ achieves state-of-the-art performance on the challenging DTU and Tanks-and-Temples benchmarks.

</details>

### UC-NERF: Neural Radiance Field for Under-Calibrated Multi-View Cameras in Autonomous Driving.
- **链接**: [arXiv:2311.16945](https://arxiv.org/abs/2311.16945)
- **作者**: Kai Cheng, Xiaoxiao Long, Wei Yin, Jin Wang, Zhiqiang Wu, Yuexin Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-camera setups find widespread use across various applications, such as autonomous driving, as they greatly expand sensing capabilities. Despite the fast development of Neural radiance field (NeRF) techniques and their wide applications in both indoor and outdoor scenes, applying NeRF to multi-camera systems remains very challenging. This is primarily due to the inherent under-calibration issues in multi-camera setup, including inconsistent imaging effects stemming from separately calibrated image signal processing units in diverse cameras, and system errors arising from mechanical vibrations during driving that affect relative camera poses. In this paper, we present UC-NeRF, a novel method tailored for novel view synthesis in under-calibrated multi-view camera systems. Firstly, we propose a layer-based color correction to rectify the color inconsistency in different image regions. Second, we propose virtual warping to generate more viewpoint-diverse but color-consistent virtual views for color correction and 3D recovery. Finally, a spatiotemporally constrained pose refinement is designed for more robust and accurate pose calibration in multi-camera systems. Our method not only achieves state-of-the-art performance of novel view synthesis in multi-camera setups, but also effectively facilitates depth estimation in large-scale outdoor scenes with the synthesized novel views.

</details>

### Performance Gaps in Multi-view Clustering under the Nested Matrix-Tensor Model.
- **链接**: [arXiv:2402.10677](https://arxiv.org/abs/2402.10677)
- **作者**: Hugo Lebeau, Mohamed El Amine Seddik, José Henrique de Morais Goulart
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We study the estimation of a planted signal hidden in a recently introduced nested matrix-tensor model, which is an extension of the classical spiked rank-one tensor model, motivated by multi-view clustering. Prior work has theoretically examined the performance of a tensor-based approach, which relies on finding a best rank-one approximation, a problem known to be computationally hard. A tractable alternative approach consists in computing instead the best rank-one (matrix) approximation of an unfolding of the observed tensor data, but its performance was hitherto unknown. We quantify here the performance gap between these two approaches, in particular by deriving the precise algorithmic threshold of the unfolding approach and demonstrating that it exhibits a BBP-type transition behavior. This work is therefore in line with recent contributions which deepen our understanding of why tensor-based methods surpass matrix-based methods in handling structured tensor data.

</details>

### SyncDreamer: Generating Multiview-consistent Images from a Single-view Image.
- **链接**: [arXiv:2309.03453](https://arxiv.org/abs/2309.03453)
- **作者**: Yuan Liu, Cheng Lin, Zijiao Zeng, Xiaoxiao Long, Lingjie Liu, Taku Komura et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present a novel diffusion model called that generates multiview-consistent images from a single-view image. Using pretrained large-scale 2D diffusion models, recent work Zero123 demonstrates the ability to generate plausible novel views from a single-view image of an object. However, maintaining consistency in geometry and colors for the generated images remains a challenge. To address this issue, we propose a synchronized multiview diffusion model that models the joint probability distribution of multiview images, enabling the generation of multiview-consistent images in a single reverse process. SyncDreamer synchronizes the intermediate states of all the generated images at every step of the reverse process through a 3D-aware feature attention mechanism that correlates the corresponding features across different views. Experiments show that SyncDreamer generates images with high consistency across different views, thus making it well-suited for various 3D generation tasks such as novel-view-synthesis, text-to-3D, and image-to-3D.

</details>

### GTA: A Geometry-Aware Attention Mechanism for Multi-View Transformers.
- **链接**: [arXiv:2310.10375](https://arxiv.org/abs/2310.10375)
- **作者**: Takeru Miyato, Bernhard Jaeger, Max Welling, Andreas Geiger
- **🏷️ 机构**: University of Tübingen
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As transformers are equivariant to the permutation of input tokens, encoding the positional information of tokens is necessary for many tasks. However, since existing positional encoding schemes have been initially designed for NLP tasks, their suitability for vision tasks, which typically exhibit different structural properties in their data, is questionable. We argue that existing positional encoding schemes are suboptimal for 3D vision tasks, as they do not respect their underlying 3D geometric structure. Based on this hypothesis, we propose a geometry-aware attention mechanism that encodes the geometric structure of tokens as relative transformation determined by the geometric relationship between queries and key-value pairs. By evaluating on multiple novel view synthesis (NVS) datasets in the sparse wide-baseline multi-view setting, we show that our attention, called Geometric Transform Attention (GTA), improves learning efficiency and performance of state-of-the-art transformer-based NVS models without any additional learned parameters and only minor computational overhead.

</details>

### MVDream: Multi-view Diffusion for 3D Generation.
- **链接**: [arXiv:2308.16512](https://arxiv.org/abs/2308.16512)
- **作者**: Yichun Shi, Peng Wang, Jianglong Ye, Long Mai, Kejie Li, Xiao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MVDream, a diffusion model that is able to generate consistent multi-view images from a given text prompt. Learning from both 2D and 3D data, a multi-view diffusion model can achieve the generalizability of 2D diffusion models and the consistency of 3D renderings. We demonstrate that such a multi-view diffusion model is implicitly a generalizable 3D prior agnostic to 3D representations. It can be applied to 3D generation via Score Distillation Sampling, significantly enhancing the consistency and stability of existing 2D-lifting methods. It can also learn new concepts from a few 2D examples, akin to DreamBooth, but for 3D generation.

</details>

### DMV3D: Denoising Multi-view Diffusion Using 3D Large Reconstruction Model.
- **链接**: [arXiv:2311.09217](https://arxiv.org/abs/2311.09217)
- **作者**: Yinghao Xu, Hao Tan, Fujun Luan, Sai Bi, Peng Wang, Jiahao Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose \textbf{DMV3D}, a novel 3D generation approach that uses a transformer-based 3D large reconstruction model to denoise multi-view diffusion. Our reconstruction model incorporates a triplane NeRF representation and can denoise noisy multi-view images via NeRF reconstruction and rendering, achieving single-stage 3D generation in $\sim$30s on single A100 GPU. We train \textbf{DMV3D} on large-scale multi-view image datasets of highly diverse objects using only image reconstruction losses, without accessing 3D assets. We demonstrate state-of-the-art results for the single-image reconstruction problem where probabilistic modeling of unseen object parts is required for generating diverse reconstructions with sharp textures. We also show high-quality text-to-3D generation results outperforming previous 3D diffusion models. Our project website is at: https://justimyhxu.github.io/projects/dmv3d/ .

</details>

### Multi-View Causal Representation Learning with Partial Observability.
- **链接**: [arXiv:2311.04056](https://arxiv.org/abs/2311.04056)
- **作者**: Dingling Yao, Danru Xu, Sébastien Lachapelle, Sara Magliacane, Perouz Taslakian, Georg Martius et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a unified framework for studying the identifiability of representations learned from simultaneously observed views, such as different data modalities. We allow a partially observed setting in which each view constitutes a nonlinear mixture of a subset of underlying latent variables, which can be causally related. We prove that the information shared across all subsets of any number of views can be learned up to a smooth bijection using contrastive learning and a single encoder per view. We also provide graphical criteria indicating which latent variables can be identified through a simple set of rules, which we refer to as identifiability algebra. Our general framework and theoretical results unify and extend several previous works on multi-view nonlinear ICA, disentanglement, and causal representation learning. We experimentally validate our claims on numerical, image, and multi-modal data sets. Further, we demonstrate that the performance of prior methods is recovered in different special cases of our setup. Overall, we find that access to multiple partial views enables us to identify a more fine-grained representation, under the generally milder assumption of partial observability.

</details>

### Unconstrained Stochastic CCA: Unifying Multiview and Self-Supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=PHLVmV88Zy)
- **作者**: James Chapman, Lennie Wells, Ana Lawry Aguila
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### A Mutual Information Perspective on Federated Contrastive Learning.
- **链接**: [arXiv:2405.02081](https://arxiv.org/abs/2405.02081)
- **作者**: Christos Louizos, Matthias Reisser, Denis Korzhenkov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We investigate contrastive learning in the federated setting through the lens of SimCLR and multi-view mutual information maximization. In doing so, we uncover a connection between contrastive representation learning and user verification; by adding a user verification loss to each client's local SimCLR loss we recover a lower bound to the global multi-view mutual information. To accommodate for the case of when some labelled data are available at the clients, we extend our SimCLR variant to the federated semi-supervised setting. We see that a supervised SimCLR objective can be obtained with two changes: a) the contrastive loss is computed between datapoints that share the same label and b) we require an additional auxiliary head that predicts the correct labels from either of the two views. Along with the proposed SimCLR extensions, we also study how different sources of non-i.i.d.-ness can impact the performance of federated unsupervised learning through global mutual information maximization; we find that a global objective is beneficial for some sources of non-i.i.d.-ness but can be detrimental for others. We empirically evaluate our proposed extensions in various tasks to validate our claims and furthermore demonstrate that our proposed modifications generalize to other pretraining methods.

</details>

### Unified Domain Generalization and Adaptation for Multi-View 3D Object Detection.
- **链接**: [arXiv:2410.22461](https://arxiv.org/abs/2410.22461) · 📚 被引 4
- **作者**: Gyusam Chang, Jiwon Lee, Donghyun Kim, Jinkyu Kim, Dongwook Lee, Daehyun Ji et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in 3D object detection leveraging multi-view cameras have demonstrated their practical and economical value in various challenging vision tasks. However, typical supervised learning approaches face challenges in achieving satisfactory adaptation toward unseen and unlabeled target datasets (\ie, direct transfer) due to the inevitable geometric misalignment between the source and target domains. In practice, we also encounter constraints on resources for training models and collecting annotations for the successful deployment of 3D object detectors. In this paper, we propose Unified Domain Generalization and Adaptation (UDGA), a practical solution to mitigate those drawbacks. We first propose Multi-view Overlap Depth Constraint that leverages the strong association between multi-view, significantly alleviating geometric gaps due to perspective view changes. Then, we present a Label-Efficient Domain Adaptation approach to handle unfamiliar targets with significantly fewer amounts of labels (\ie, 1$\%$ and 5$\%)$, while preserving well-defined source knowledge for training efficiency. Overall, UDGA framework enables stable detection performance in both source and target domains, effectively bridging inevitable domain gaps, while demanding fewer annotations. We demonstrate the robustness of UDGA with large-scale benchmarks: nuScenes, Lyft, and Waymo, where our framework outperforms the current state-of-the-art methods.

</details>

### MVSDet: Multi-View Indoor 3D Object Detection via Efficient Plane Sweeps.
- **链接**: [arXiv:2410.21566](https://arxiv.org/abs/2410.21566) · 📚 被引 3
- **作者**: Yating Xu, Chen Li, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The key challenge of multi-view indoor 3D object detection is to infer accurate geometry information from images for precise 3D detection. Previous method relies on NeRF for geometry reasoning. However, the geometry extracted from NeRF is generally inaccurate, which leads to sub-optimal detection performance. In this paper, we propose MVSDet which utilizes plane sweep for geometry-aware 3D object detection. To circumvent the requirement for a large number of depth planes for accurate depth prediction, we design a probabilistic sampling and soft weighting mechanism to decide the placement of pixel features on the 3D volume. We select multiple locations that score top in the probability volume for each pixel and use their probability score to indicate the confidence. We further apply recent pixel-aligned Gaussian Splatting to regularize depth prediction and improve detection performance with little computation overhead. Extensive experiments on ScanNet and ARKitScenes datasets are conducted to show the superiority of our model. Our code is available at https://github.com/Pixie8888/MVSDet.

</details>

### Bridging Gaps: Federated Multi-View Clustering in Heterogeneous Hybrid Views.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/412fb8623bf8b6d56fb6285ea295447e-Abstract-Conference.html) · 📚 被引 17
- **作者**: Xinyue Chen, Yazhou Ren, Jie Xu, Fangfei Lin, Xiaorong Pu, Yang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Alleviate Anchor-Shift: Explore Blind Spots with Cross-View Reconstruction for Incomplete Multi-View Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/9f42f06a54ce3b709ad78d34c73e4363-Abstract-Conference.html) · 📚 被引 3
- **作者**: Suyuan Liu, Siwei Wang, Ke Liang, Junpu Zhang, Zhibin Dong, Tianrui Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MM-WLAuslan: Multi-View Multi-Modal Word-Level Australian Sign Language Recognition Dataset.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/812c59ba55c03a68a10c25017bdb696e-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 6
- **作者**: Xin Shen, Heming Du, Hongwei Sheng, Shuyun Wang, Hui Chen, Huiqiang Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Evaluate then Cooperate: Shapley-based View Cooperation Enhancement for Multi-view Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/f46b6689a645184b5ff84b4feb3e7bb4-Abstract-Conference.html) · 📚 被引 3
- **作者**: Fangdi Wang, Jiaqi Jin, Jingtao Hu, Suyuan Liu, Xihong Yang, Siwei Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MVInpainter: Learning Multi-View Consistent Inpainting to Bridge 2D and 3D Editing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b3bac97f3227c52c0179a6d967480867-Abstract-Conference.html) · 📚 被引 10
- **作者**: Chenjie Cao, Chaohui Yu, Fan Wang, Xiangyang Xue, Yanwei Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### A Global Depth-Range-Free Multi-View Stereo Transformer Network with Pose Embedding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/770b5223b47d4304042826b29733e864-Abstract-Conference.html)
- **作者**: Yitong Dong, Yijin Li, Zhaoyang Huang, Weikang Bian, Jingbo Liu, Hujun Bao et al.
- **🏷️ 机构**: CUHK
- **会议**: NeurIPS 2024

### From Dictionary to Tensor: A Scalable Multi-View Subspace Clustering Framework with Triple Information Enhancement.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/bb68f698772f14b6d8eaef4529fb9176-Abstract-Conference.html) · 📚 被引 3
- **作者**: Zhibin Gu, Songhe Feng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Robust Contrastive Multi-view Clustering against Dual Noisy Correspondence.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/dbe81b08f7dc4dd8b43bc62dedfd9662-Abstract-Conference.html) · 📚 被引 13
- **作者**: Ruiming Guo, Mouxing Yang, Yijie Lin, Xi Peng, Peng Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MV2Cyl: Reconstructing 3D Extrusion Cylinders from Multi-View Images.
- **链接**: [arXiv:2406.10853](https://arxiv.org/abs/2406.10853) · 📚 被引 4
- **作者**: Eunji Hong, Minh Hieu Nguyen, Mikaela Angelina Uy, Minhyuk Sung
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present MV2Cyl, a novel method for reconstructing 3D from 2D multi-view images, not merely as a field or raw geometry but as a sketch-extrude CAD model. Extracting extrusion cylinders from raw 3D geometry has been extensively researched in computer vision, while the processing of 3D data through neural networks has remained a bottleneck. Since 3D scans are generally accompanied by multi-view images, leveraging 2D convolutional neural networks allows these images to be exploited as a rich source for extracting extrusion cylinder information. However, we observe that extracting only the surface information of the extrudes and utilizing it results in suboptimal outcomes due to the challenges in the occlusion and surface segmentation. By synergizing with the extracted base curve information, we achieve the optimal reconstruction result with the best accuracy in 2D sketch and extrude parameter estimation. Our experiments, comparing our method with previous work that takes a raw 3D point cloud as input, demonstrate the effectiveness of our approach by taking advantage of multi-view images. Our project page can be found at http://mv2cyl.github.io .

</details>

### Animate3D: Animating Any 3D Model with Multi-view Video Diffusion.
- **链接**: [arXiv:2407.11398](https://arxiv.org/abs/2407.11398) · 📚 被引 6
- **作者**: Yanqin Jiang, Chaohui Yu, Chenjie Cao, Fan Wang, Weiming Hu, Jin Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in 4D generation mainly focus on generating 4D content by distilling pre-trained text or single-view image-conditioned models. It is inconvenient for them to take advantage of various off-the-shelf 3D assets with multi-view attributes, and their results suffer from spatiotemporal inconsistency owing to the inherent ambiguity in the supervision signals. In this work, we present Animate3D, a novel framework for animating any static 3D model. The core idea is two-fold: 1) We propose a novel multi-view video diffusion model (MV-VDM) conditioned on multi-view renderings of the static 3D object, which is trained on our presented large-scale multi-view video dataset (MV-Video). 2) Based on MV-VDM, we introduce a framework combining reconstruction and 4D Score Distillation Sampling (4D-SDS) to leverage the multi-view video diffusion priors for animating 3D objects. Specifically, for MV-VDM, we design a new spatiotemporal attention module to enhance spatial and temporal consistency by integrating 3D and video diffusion models. Additionally, we leverage the static 3D model's multi-view renderings as conditions to preserve its identity. For animating 3D models, an effective two-stage pipeline is proposed: we first reconstruct motions directly from generated multi-view videos, followed by the introduced 4D-SDS to refine both appearance and motion. Benefiting from accurate motion learning, we could achieve straightforward mesh animation. Qualitative and quantitative experiments demonstrate that Animate3D significantly outperforms previous approaches. Data, code, and models will be open-released.

</details>

### Vivid-ZOO: Multi-View Video Generation with Diffusion Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/71c9eb0913e6c7fda3afd69c914b1a0c-Abstract-Conference.html) · 📚 被引 7
- **作者**: Bing Li, Cheng Zheng, Wenxuan Zhu, Jinjie Mai, Biao Zhang, Peter Wonka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### $SE(3)$ Equivariant Ray Embeddings for Implicit Multi-View Depth Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/18aee41e1bb41bbb8fee53cfff8138b7-Abstract-Conference.html)
- **作者**: Yinshuang Xu, Dian Chen, Katherine Liu, Sergey Zakharov, Rares Ambrus, Kostas Daniilidis et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### RETR: Multi-View Radar Detection Transformer for Indoor Perception.
- **链接**: [arXiv:2411.10293](https://arxiv.org/abs/2411.10293) · 📚 被引 3
- **作者**: Ryoma Yataka, Adriano Cardace, Perry Wang, Petros Boufounos, Ryuhei Takahashi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Indoor radar perception has seen rising interest due to affordable costs driven by emerging automotive imaging radar developments and the benefits of reduced privacy concerns and reliability under hazardous conditions (e.g., fire and smoke). However, existing radar perception pipelines fail to account for distinctive characteristics of the multi-view radar setting. In this paper, we propose Radar dEtection TRansformer (RETR), an extension of the popular DETR architecture, tailored for multi-view radar perception. RETR inherits the advantages of DETR, eliminating the need for hand-crafted components for object detection and segmentation in the image plane. More importantly, RETR incorporates carefully designed modifications such as 1) depth-prioritized feature similarity via a tunable positional encoding (TPE); 2) a tri-plane loss from both radar and camera coordinates; and 3) a learnable radar-to-camera transformation via reparameterization, to account for the unique multi-view radar setting. Evaluated on two indoor radar perception datasets, our approach outperforms existing state-of-the-art methods by a margin of 15.38+ AP for object detection and 11.91+ IoU for instance segmentation, respectively. Our implementation is available at https://github.com/merlresearch/radar-detection-transformer.

</details>

### 4Diffusion: Multi-view Video Diffusion Model for 4D Generation.
- **链接**: [arXiv:2405.20674](https://arxiv.org/abs/2405.20674) · 📚 被引 17
- **作者**: Haiyu Zhang, Xinyuan Chen, Yaohui Wang, Xihui Liu, Yunhong Wang, Yu Qiao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current 4D generation methods have achieved noteworthy efficacy with the aid of advanced diffusion generative models. However, these methods lack multi-view spatial-temporal modeling and encounter challenges in integrating diverse prior knowledge from multiple diffusion models, resulting in inconsistent temporal appearance and flickers. In this paper, we propose a novel 4D generation pipeline, namely 4Diffusion, aimed at generating spatial-temporally consistent 4D content from a monocular video. We first design a unified diffusion model tailored for multi-view video generation by incorporating a learnable motion module into a frozen 3D-aware diffusion model to capture multi-view spatial-temporal correlations. After training on a curated dataset, our diffusion model acquires reasonable temporal consistency and inherently preserves the generalizability and spatial consistency of the 3D-aware diffusion model. Subsequently, we propose 4D-aware Score Distillation Sampling loss, which is based on our multi-view video diffusion model, to optimize 4D representation parameterized by dynamic NeRF. This aims to eliminate discrepancies arising from multiple diffusion models, allowing for generating spatial-temporally consistent 4D content. Moreover, we devise an anchor loss to enhance the appearance details and facilitate the learning of dynamic NeRF. Extensive qualitative and quantitative experiments demonstrate that our method achieves superior performance compared to previous methods.

</details>

### Gaussian Graph Network: Learning Efficient and Generalizable Gaussian Representations from Multi-view Images.
- **链接**: [arXiv:2503.16338](https://arxiv.org/abs/2503.16338) · 📚 被引 2
- **作者**: Shengjun Zhang, Xin Fei, Fangfu Liu, Haixu Song, Yueqi Duan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D Gaussian Splatting (3DGS) has demonstrated impressive novel view synthesis performance. While conventional methods require per-scene optimization, more recently several feed-forward methods have been proposed to generate pixel-aligned Gaussian representations with a learnable network, which are generalizable to different scenes. However, these methods simply combine pixel-aligned Gaussians from multiple views as scene representations, thereby leading to artifacts and extra memory cost without fully capturing the relations of Gaussians from different images. In this paper, we propose Gaussian Graph Network (GGN) to generate efficient and generalizable Gaussian representations. Specifically, we construct Gaussian Graphs to model the relations of Gaussian groups from different views. To support message passing at Gaussian level, we reformulate the basic graph operations over Gaussian representations, enabling each Gaussian to benefit from its connected Gaussian groups with Gaussian feature fusion. Furthermore, we design a Gaussian pooling layer to aggregate various Gaussian groups for efficient representations. We conduct experiments on the large-scale RealEstate10K and ACID datasets to demonstrate the efficiency and generalization of our method. Compared to the state-of-the-art methods, our model uses fewer Gaussians and achieves better image quality with higher rendering speed.

</details>

### Depth Anywhere: Enhancing 360 Monocular Depth Estimation via Perspective Distillation and Unlabeled Data Augmentation.
- **链接**: [arXiv:2406.12849](https://arxiv.org/abs/2406.12849) · 📚 被引 10
- **作者**: Ning-Hsu Wang, Yu-Lun Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately estimating depth in 360-degree imagery is crucial for virtual reality, autonomous navigation, and immersive media applications. Existing depth estimation methods designed for perspective-view imagery fail when applied to 360-degree images due to different camera projections and distortions, whereas 360-degree methods perform inferior due to the lack of labeled data pairs. We propose a new depth estimation framework that utilizes unlabeled 360-degree data effectively. Our approach uses state-of-the-art perspective depth estimation models as teacher models to generate pseudo labels through a six-face cube projection technique, enabling efficient labeling of depth in 360-degree images. This method leverages the increasing availability of large datasets. Our approach includes two main stages: offline mask generation for invalid regions and an online semi-supervised joint training regime. We tested our approach on benchmark datasets such as Matterport3D and Stanford2D3D, showing significant improvements in depth estimation accuracy, particularly in zero-shot scenarios. Our proposed training pipeline can enhance any 360 monocular depth estimator and demonstrates effective knowledge transfer across different camera projections and data types. See our project page for results: https://albert100121.github.io/Depth-Anywhere/

</details>

### Beware of Road Markings: A New Adversarial Patch Attack to Monocular Depth Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/7d26958422928e08465d5dd6cf0cb4cb-Abstract-Conference.html) · 📚 被引 3
- **作者**: Hangcheng Liu, Zhenhu Wu, Hao Wang, Xingshuo Han, Shangwei Guo, Tao Xiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### DCDepth: Progressive Monocular Depth Estimation in Discrete Cosine Domain.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/76bea0a1cf7bf9b78f842009f6de15a1-Abstract-Conference.html) · 📚 被引 7
- **作者**: Kun Wang, Zhiqiang Yan, Junkai Fan, Wanlu Zhu, Xiang Li, Jun Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### BetterDepth: Plug-and-Play Diffusion Refiner for Zero-Shot Monocular Depth Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c4b652b7e228b18e1c65478da3a4a2cf-Abstract-Conference.html) · 📚 被引 2
- **作者**: Xiang Zhang, Bingxin Ke, Hayko Riemenschneider, Nando Metzger, Anton Obukhov, Markus Gross et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples.
- **链接**: [arXiv:2410.14669](https://arxiv.org/abs/2410.14669) · 📚 被引 3
- **作者**: Baiqi Li, Zhiqiu Lin, Wenxuan Peng, Jean de Dieu Nyandwi, Daniel Jiang, Zixian Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have made significant progress in recent visual-question-answering (VQA) benchmarks that evaluate complex visio-linguistic reasoning. However, are these models truly effective? In this work, we show that VLMs still struggle with natural images and questions that humans can easily answer, which we term natural adversarial samples. We also find it surprisingly easy to generate these VQA samples from natural image-text corpora using off-the-shelf models like CLIP and ChatGPT. We propose a semi-automated approach to collect a new benchmark, NaturalBench, for reliably evaluating VLMs with 10,000 human-verified VQA samples. Crucially, we adopt a $\textbf{vision-centric}$ design by pairing each question with two images that yield different answers, preventing blind solutions from answering without using the images. This makes NaturalBench more challenging than previous benchmarks that can be solved with commonsense priors. We evaluate 53 state-of-the-art VLMs on NaturalBench, showing that models like LLaVA-OneVision, Cambrian-1, Llama3.2-Vision, Molmo, Qwen2-VL, and even GPT-4o lag 50%-70% behind human performance (over 90%). We analyze why NaturalBench is hard from two angles: (1) Compositionality: Solving NaturalBench requires diverse visio-linguistic skills, including understanding attribute bindings, object relationships, and advanced reasoning like logic and counting. To this end, unlike prior work that uses a single tag per sample, we tag each NaturalBench sample with 1 to 8 skill tags for fine-grained evaluation. (2) Biases: NaturalBench exposes severe biases in VLMs, as models often choose the same answer regardless of the image. Lastly, we apply our benchmark curation method to diverse data sources, including long captions (over 100 words) and non-English languages like Chinese and Hindi, highlighting its potential for dynamic evaluations of VLMs.

</details>

### Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/946ecab300b0695fe24b53a92e632935-Abstract-Conference.html) · 📚 被引 1
- **作者**: Yang Jiao, Shaoxiang Chen, Zequn Jie, Jingjing Chen, Lin Ma, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. → [vlm](../vlm/Guideline%202024.md)
- MTMMC: A Large-Scale Real-World Multi-Modal Camera Tracking Benchmark. → [multimodal](../multimodal/Guideline%202024.md)
- Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors. → [object-detection](../object-detection/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- PointOBB: Learning Oriented Object Detection via Single Point Supervision. → [object-detection](../object-detection/Guideline%202024.md)
- From a Bird's Eye View to See: Joint Camera and Subject Registration without the Camera Calibration. → [bev](../bev/Guideline%202024.md)
- SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- MaskClustering: View Consensus Based Mask Graph Clustering for Open-Vocabulary 3D Instance Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving. → [object-detection](../object-detection/Guideline%202024.md)
- Volumetric Environment Representation for Vision-Language Navigation. → [vlm](../vlm/Guideline%202024.md)
- EMOPortraits: Emotion-Enhanced Multimodal One-Shot Head Avatars. → [multimodal](../multimodal/Guideline%202024.md)
- OmniSeg3D: Omniversal 3D Segmentation via Hierarchical Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- SimPB: A Single Model for 2D and 3D Object Detection from Multiple Cameras. → [3d-detection](../3d-detection/Guideline%202024.md)
- FroSSL: Frobenius Norm Minimization for Efficient Multiview Self-supervised Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- CRT-Fusion: Camera, Radar, Temporal Fusion Using Motion Information for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Autonomous Driving with Spiking Neural Networks. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
<!-- COMPLETE v1 papers=128 -->
