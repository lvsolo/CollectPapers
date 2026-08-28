# Multi-camera Perception — 2024 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 56 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MMVR: Millimeter-Wave Multi-view Radar Dataset and Benchmark for Indoor Perception.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72986-7_18) · 📚 被引 11
- **作者**: Mohammad Mahbubur Rahman, Ryoma Yataka, Sorachi Kato, Pu Wang, Peizhao Li, Adriano Cardace et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Make Your ViT-Based Multi-view 3D Detectors Faster via Token Compression.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_4)
- **作者**: Dingyuan Zhang, Dingkang Liang, Zichang Tan, Xiaoqing Ye, Cheng Zhang, Jingdong Wang et al.
- **🏷️ 机构**: HUAST
- **会议**: ECCV 2024

### ViewFormer: Exploring Spatiotemporal Modeling for Multi-view 3D Occupancy Perception via View-Guided Transformers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72775-7_6)
- **作者**: Jinke Li, Xiao He, Chonghua Zhou, Xiaoqiang Cheng, Yang Wen, Dan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Mahalanobis Distance-Based Multi-view Optimal Transport for Multi-view Crowd Localization.
- **链接**: [arXiv:2409.01726](https://arxiv.org/abs/2409.01726) · 📚 被引 8
- **作者**: Qi Zhang, Kaiyi Zhang, Antoni B. Chan, Hui Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view crowd localization predicts the ground locations of all people in the scene. Typical methods usually estimate the crowd density maps on the ground plane first, and then obtain the crowd locations. However, the performance of existing methods is limited by the ambiguity of the density maps in crowded areas, where local peaks can be smoothed away. To mitigate the weakness of density map supervision, optimal transport-based point supervision methods have been proposed in the single-image crowd localization tasks, but have not been explored for multi-view crowd localization yet. Thus, in this paper, we propose a novel Mahalanobis distance-based multi-view optimal transport (M-MVOT) loss specifically designed for multi-view crowd localization. First, we replace the Euclidean-based transport cost with the Mahalanobis distance, which defines elliptical iso-contours in the cost function whose long-axis and short-axis directions are guided by the view ray direction. Second, the object-to-camera distance in each view is used to adjust the optimal transport cost of each location further, where the wrong predictions far away from the camera are more heavily penalized. Finally, we propose a strategy to consider all the input camera views in the model loss (M-MVOT) by computing the optimal transport cost for each ground-truth point based on its closest camera. Experiments demonstrate the advantage of the proposed method over density map-based or common Euclidean distance-based optimal transport loss on several multi-view crowd localization datasets. Project page: https://vcc.tech/research/2024/MVOT.

</details>

### PanoFree: Tuning-Free Holistic Multi-view Image Generation with Cross-View Self-guidance.
- **链接**: [arXiv:2408.02157](https://arxiv.org/abs/2408.02157) · 📚 被引 5
- **作者**: Aoming Liu, Zhong Li, Zhang Chen, Nannan Li, Yi Xu, Bryan A. Plummer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Immersive scene generation, notably panorama creation, benefits significantly from the adaptation of large pre-trained text-to-image (T2I) models for multi-view image generation. Due to the high cost of acquiring multi-view images, tuning-free generation is preferred. However, existing methods are either limited to simple correspondences or require extensive fine-tuning to capture complex ones. We present PanoFree, a novel method for tuning-free multi-view image generation that supports an extensive array of correspondences. PanoFree sequentially generates multi-view images using iterative warping and inpainting, addressing the key issues of inconsistency and artifacts from error accumulation without the need for fine-tuning. It improves error accumulation by enhancing cross-view awareness and refines the warping and inpainting processes via cross-view guidance, risky area estimation and erasing, and symmetric bidirectional guided generation for loop closure, alongside guidance-based semantic and density control for scene structure preservation. In experiments on Planar, 360°, and Full Spherical Panoramas, PanoFree demonstrates significant error reduction, improves global consistency, and boosts image quality without extra fine-tuning. Compared to existing methods, PanoFree is up to 5x more efficient in time and 3x more efficient in GPU memory usage, and maintains superior diversity of results (2x better in our user study). PanoFree offers a viable alternative to costly fine-tuning or the use of additional pre-trained models. Project website at https://panofree.github.io/.

</details>

### MetaCap: Meta-learning Priors from Multi-view Imagery for Sparse-View Human Performance Capture and Rendering.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72952-2_20) · 📚 被引 7
- **作者**: Guoxing Sun, Rishabh Dabral, Pascal Fua, Christian Theobalt, Marc Habermann
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MVDiffusion++: A Dense High-Resolution Multi-view Diffusion Model for Single or Sparse-View 3D Object Reconstruction.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72640-8_10) · 📚 被引 41
- **作者**: Shitao Tang, Jiacheng Chen, Dilin Wang, Chengzhou Tang, Fuyang Zhang, Yuchen Fan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### HENet: Hybrid Encoding for End-to-End Multi-task 3D Perception from Multi-view Cameras.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72973-7_22) · 📚 被引 11
- **作者**: Zhongyu Xia, Zhiwei Lin, Xinhao Wang, Yongtao Wang, Yun Xing, Shengxiang Qi et al.
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2024

### MVPGS: Excavating Multi-view Priors for Gaussian Splatting from Sparse Input Views.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_12) · 📚 被引 27
- **作者**: Wangze Xu, Huachen Gao, Shihe Shen, Rui Peng, Jianbo Jiao, Ronggang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### PolyOculus: Simultaneous Multi-view Image-Based Novel View Synthesis.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73036-8_25) · 📚 被引 4
- **作者**: Jason J. Yu, Tristan Aumentado-Armstrong, Fereshteh Forghani, Konstantinos G. Derpanis, Marcus A. Brubaker
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Resolving Scale Ambiguity in Multi-view 3D Reconstruction Using Dual-Pixel Sensors.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72973-7_10) · 📚 被引 3
- **作者**: Kohei Ashida, Hiroaki Santo, Fumio Okura, Yasuyuki Matsushita
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MARs: Multi-view Attention Regularizations for Patch-Based Feature Recognition of Space Terrain.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73039-9_13) · 📚 被引 4
- **作者**: Timothy Chase Jr., Karthik Dantu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### DGE: Direct Gaussian 3D Editing by Consistent Multi-view Editing.
- **链接**: [arXiv:2404.18929](https://arxiv.org/abs/2404.18929) · 📚 被引 42
- **作者**: Minghao Chen, Iro Laina, Andrea Vedaldi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of editing 3D objects and scenes based on open-ended language instructions. A common approach to this problem is to use a 2D image generator or editor to guide the 3D editing process, obviating the need for 3D data. However, this process is often inefficient due to the need for iterative updates of costly 3D representations, such as neural radiance fields, either through individual view edits or score distillation sampling. A major disadvantage of this approach is the slow convergence caused by aggregating inconsistent information across views, as the guidance from 2D models is not multi-view consistent. We thus introduce the Direct Gaussian Editor (DGE), a method that addresses these issues in two stages. First, we modify a given high-quality image editor like InstructPix2Pix to be multi-view consistent. To do so, we propose a training-free approach that integrates cues from the 3D geometry of the underlying scene. Second, given a multi-view consistent edited sequence of images, we directly and efficiently optimize the 3D representation, which is based on 3D Gaussian Splatting. Because it avoids incremental and iterative edits, DGE is significantly more accurate and efficient than existing approaches and offers additional benefits, such as enabling selective editing of parts of the scene.

</details>

### 3DSA: Multi-view 3D Human Pose Estimation With 3D Space Attention Mechanisms.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73383-3_19) · 📚 被引 1
- **作者**: Bo-Han Chen, Chia-Chi Tsai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-view Images.
- **链接**: [arXiv:2403.14627](https://arxiv.org/abs/2403.14627) · 📚 被引 238
- **作者**: Yuedong Chen, Haofei Xu, Chuanxia Zheng, Bohan Zhuang, Marc Pollefeys, Andreas Geiger et al.
- **🏷️ 机构**: University of Tübingen
- **会议**: ECCV 2024

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
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72649-1_3) · 📚 被引 83
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

### Six-Point Method for Multi-camera Systems with Reduced Solution Space.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73001-6_7) · 📚 被引 27
- **作者**: Banglei Guan, Ji Zhao, Laurent Kneip
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### WoVoGen: World Volume-Aware Diffusion for Controllable Multi-camera Driving Scene Generation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72989-8_19) · 📚 被引 25
- **作者**: Jiachen Lu, Ze Huang, Zeyu Yang, Jiahui Zhang, Li Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### M2Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72952-2_16)
- **作者**: Yingshuang Zou, Yikang Ding, Xi Qiu, Haoqian Wang, Haotian Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### DiffusionDepth: Diffusion Denoising Approach for Monocular Depth Estimation.
- **链接**: [arXiv:2303.05021](https://arxiv.org/abs/2303.05021) · 📚 被引 75
- **作者**: Yiquan Duan, Xianda Guo, Zheng Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation is a challenging task that predicts the pixel-wise depth from a single 2D image. Current methods typically model this problem as a regression or classification task. We propose DiffusionDepth, a new approach that reformulates monocular depth estimation as a denoising diffusion process. It learns an iterative denoising process to `denoise' random depth distribution into a depth map with the guidance of monocular visual conditions. The process is performed in the latent space encoded by a dedicated depth encoder and decoder. Instead of diffusing ground truth (GT) depth, the model learns to reverse the process of diffusing the refined depth of itself into random depth distribution. This self-diffusion formulation overcomes the difficulty of applying generative models to sparse GT depth scenarios. The proposed approach benefits this task by refining depth estimation step by step, which is superior for generating accurate and highly detailed depth maps. Experimental results on KITTI and NYU-Depth-V2 datasets suggest that a simple yet efficient diffusion approach could reach state-of-the-art performance in both indoor and outdoor scenarios with acceptable inference time.

</details>

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

### Leveraging Near-Field Lighting for Monocular Depth Estimation from Endoscopy Videos.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73411-3_27) · 📚 被引 10
- **作者**: Akshay Paruchuri, Samuel Ehrenstein, Shuxian Wang, Inbar Fried, Stephen M. Pizer, Marc Niethammer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Diffusion Models for Monocular Depth Estimation: Overcoming Challenging Conditions.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73337-6_14) · 📚 被引 25
- **作者**: Fabio Tosi, Pierluigi Zama Ramirez, Matteo Poggi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Physics-Informed Knowledge Transfer for Underwater Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73209-6_26)
- **作者**: Jinghe Yang, Mingming Gong, Ye Pu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Improving Domain Generalization in Self-supervised Monocular Depth Estimation via Stabilized Adversarial Training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72691-0_11)
- **作者**: Yuanqi Yao, Gang Wu, Kui Jiang, Siao Liu, Jian Kuai, Xianming Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### FroSSL: Frobenius Norm Minimization for Efficient Multiview Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73024-5_5)
- **作者**: Oscar Skean, Aayush Dhakal, Nathan Jacobs, Luis Gonzalo Sánchez Giraldo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Revisit Self-supervised Depth Estimation with Local Structure-from-Motion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73007-8_3)
- **作者**: Shengjie Zhu, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

## 跨领域论文（完整笔记在其他领域）

- OPEN: Object-Wise Position Embedding for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Learning High-Resolution Vector Representation from Multi-camera Images for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Ray Denoising: Depth-Aware Hard Negative Sampling for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- RecurrentBEV: A Long-Term Temporal Fusion Framework for Multi-view 3D Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- DrivingDiffusion: Layout-Guided Multi-view Driving Scenarios Video Generation with Latent Diffusion Model. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
