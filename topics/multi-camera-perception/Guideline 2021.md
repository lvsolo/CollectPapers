# Multi-camera Perception — 2021 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Multi-View Multi-Person 3D Pose Estimation With Plane Sweep Stereo. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Lin_Multi-View_Multi-Person_3D_Pose_Estimation_With_Plane_Sweep_Stereo_CVPR_2021_paper.html) · 📚 被引 69
- **作者**: Jiahao Lin, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多视角多人体3D姿态估计中，如何有效利用多视角几何信息进行深度估计的问题。②提出了基于平面扫描立体匹配的方法，通过构建代价体并回归深度图，进而提升3D姿态估计精度。③相比直接使用三角化或单目方法，该方法显式建模了多视角几何约束，并利用可微的深度估计模块。④在公开数据集上取得了优于基线方法的3D姿态估计精度，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses multi-view multi-person 3D pose estimation by leveraging plane sweep stereo to construct cost volumes for depth regression. It improves over triangulation-based methods by explicitly modeling multi-view geometry, achieving superior accuracy on public benchmarks, though specific numbers are not cited.
- **核心贡献**: 提出基于平面扫描立体的多视角3D姿态估计框架。
- **创新点**: 将深度估计与姿态估计联合优化，利用几何约束。
- **结果**: 在公开数据集上提升了3D姿态估计精度。

### Cross-View Cross-Scene Multi-View Crowd Counting. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_Cross-View_Cross-Scene_Multi-View_Crowd_Counting_CVPR_2021_paper.html) · 📚 被引 68
- **作者**: Qi Zhang, Wei Lin, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对跨视角、跨场景的多视角人群计数问题，现有方法难以适应不同场景的视角变化。②提出了一个跨视角跨场景的计数框架，通过域适应和视角对齐技术提升泛化能力。③相比单视角计数方法，该方法利用多视角信息增强特征表达，并引入场景无关的表示。④在多个数据集上验证了有效性，但摘要未给出具体数值。
- **摘要（英）**: This work tackles cross-view and cross-scene multi-view crowd counting by employing domain adaptation and view alignment to improve generalization. It leverages multi-view information for robust feature learning, outperforming single-view baselines, though quantitative results are not detailed.
- **核心贡献**: 提出跨视角跨场景的多视角人群计数方法。
- **创新点**: 结合域适应与视角对齐提升泛化。
- **结果**: 在多个数据集上验证了有效性。

### COMPLETER: Incomplete Multi-View Clustering via Contrastive Prediction. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Lin_COMPLETER_Incomplete_Multi-View_Clustering_via_Contrastive_Prediction_CVPR_2021_paper.html) · 📚 被引 404
- **作者**: Yijie Lin, Yuanbiao Gou, Zitao Liu, Boyun Li, Jiancheng Lv, Xi Peng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对不完整多视角聚类中缺失视角的预测问题。②提出了基于对比预测的COMPLETER方法，利用对比学习恢复缺失视角并增强聚类。③相比传统填充方法，该方法通过预测任务学习更鲁棒的表示。④在多个聚类基准上提升了性能，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses incomplete multi-view clustering by proposing a contrastive prediction method to recover missing views and improve clustering. It outperforms traditional imputation approaches on benchmarks, though specific metrics are not provided.
- **核心贡献**: 提出对比预测框架用于不完整多视角聚类。
- **创新点**: 利用对比学习进行缺失视角预测。
- **结果**: 在聚类任务上取得性能提升。

### Multi-View 3D Reconstruction of a Texture-Less Smooth Surface of Unknown Generic Reflectance. **⭐⭐** (相关度: 25%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Cheng_Multi-View_3D_Reconstruction_of_a_Texture-Less_Smooth_Surface_of_Unknown_CVPR_2021_paper.html) · 📚 被引 22
- **作者**: Ziang Cheng, Hongdong Li, Yuta Asano, Yinqiang Zheng, Imari Sato
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对无纹理光滑表面且反射率未知的多视角3D重建难题。②提出了结合光度立体与多视角几何的方法，估计表面形状和反射率。③相比传统方法，能处理复杂反射特性。④在合成和真实数据上验证了效果，但摘要未给出具体数值。
- **摘要（英）**: This paper tackles multi-view 3D reconstruction of texture-less surfaces with unknown reflectance by combining photometric stereo and multi-view geometry. It handles complex reflectance better than prior work, validated on synthetic and real data, though no specific numbers are cited.
- **核心贡献**: 提出无纹理表面重建方法。
- **创新点**: 联合估计形状与反射率。
- **结果**: 在相关数据集上验证了有效性。

### DeepVideoMVS: Multi-View Stereo on Video With Recurrent Spatio-Temporal Fusion. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2012.02177](https://arxiv.org/abs/2012.02177) · 📚 被引 76
- **作者**: Arda Düzçeker, Silvano Galliani, Christoph Vogel, Pablo Speciale, Mihai Dusmanu, Marc Pollefeys
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对视频流中的在线多视角深度预测问题，现有方法未充分利用时序信息。②提出了DeepVideoMVS，通过ConvLSTM在瓶颈层传播历史信息，并利用前序深度预测对隐藏状态进行视角变换。③相比静态多视角立体方法，该方法在保持实时性的同时显著提升深度预测精度。④在数百个室内场景中，多数评估指标上优于现有最先进方法，且计算开销小。
- **摘要（英）**: This paper addresses online multi-view depth prediction on video streams by introducing a ConvLSTM at the bottleneck to propagate temporal information, with hidden states warped using previous depth predictions. It outperforms state-of-the-art multi-view stereo methods on most metrics in hundreds of indoor scenes while maintaining real-time performance.
- **核心贡献**: 提出基于循环时空融合的实时多视角深度预测方法。
- **创新点**: 利用ConvLSTM和视角变换传播历史几何信息。
- **结果**: 在室内场景中超越现有方法，保持实时性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an online multi-view depth prediction approach on posed video streams, where the scene geometry information computed in the previous time steps is propagated to the current time step in an efficient and geometrically plausible way. The backbone of our approach is a real-time capable, lightweight encoder-decoder that relies on cost volumes computed from pairs of images. We extend it by placing a ConvLSTM cell at the bottleneck layer, which compresses an arbitrary amount of past information in its states. The novelty lies in propagating the hidden state of the cell by accounting for the viewpoint changes between time steps. At a given time step, we warp the previous hidden state into the current camera plane using the previous depth prediction. Our extension brings only a small overhead of computation time and memory consumption, while improving the depth predictions significantly. As a result, we outperform the existing state-of-the-art multi-view stereo methods on most of the evaluated metrics in hundreds of indoor scenes while maintaining a real-time performance. Code available: https://github.com/ardaduz/deep-video-mvs

</details>

### Recurrent Multi-View Alignment Network for Unsupervised Surface Registration. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2011.12104](https://arxiv.org/abs/2011.12104) · 📚 被引 47
- **作者**: Wanquan Feng, Juyong Zhang, Hongrui Cai, Haofei Xu, Junhui Hou, Hujun Bao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对无监督非刚性表面配准中高自由度与缺乏标注数据的问题。②提出了循环多视角对齐网络，将非刚性变换表示为多个刚性变换的组合，并通过可微损失在投影深度图上度量形状相似性。③相比现有方法，该表示约束了解空间，且支持端到端无监督训练。④在多个数据集上大幅超越先前最先进方法。
- **摘要（英）**: This paper addresses unsupervised non-rigid surface registration by representing transformations as combinations of rigid ones and using a recurrent framework with a differentiable loss on projected depth images. It outperforms previous state-of-the-art by a large margin on several datasets.
- **核心贡献**: 提出循环多视角对齐网络用于无监督表面配准。
- **创新点**: 用刚性变换组合表示非刚性变换并循环求解。
- **结果**: 在多个数据集上大幅超越现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning non-rigid registration in an end-to-end manner is challenging due to the inherent high degrees of freedom and the lack of labeled training data. In this paper, we resolve these two challenges simultaneously. First, we propose to represent the non-rigid transformation with a point-wise combination of several rigid transformations. This representation not only makes the solution space well-constrained but also enables our method to be solved iteratively with a recurrent framework, which greatly reduces the difficulty of learning. Second, we introduce a differentiable loss function that measures the 3D shape similarity on the projected multi-view 2D depth images so that our full framework can be trained end-to-end without ground truth supervision. Extensive experiments on several different datasets demonstrate that our proposed method outperforms the previous state-of-the-art by a large margin. The source codes are available at https://github.com/WanquanF/RMA-Net.

</details>

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

### Differentiable Diffusion for Dense Depth Estimation From Multi-View Images. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2106.08917](https://arxiv.org/abs/2106.08917) · 📚 被引 17
- **作者**: Numair Khan, Min H. Kim, James Tompkin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多视图图像中稠密深度估计问题，现有方法依赖昂贵的深度监督或复杂的优化。②提出可微扩散方法，通过优化稀疏点集的位置、深度和权重，使其扩散为深度图，并最小化多视图重投影误差，利用高斯点云和解析透射率进行可微渲染。③相比传统优化和深度学习方法，该方法能同时优化5万多个点，支持自监督训练，适用于光场和宽基线场景。④实验表明，在真实数据和自监督设置下，深度图在平均误差和离群误差上均有改进，重建质量高。
- **摘要（英）**: This paper addresses dense depth estimation from multi-view images by optimizing sparse points via differentiable diffusion into a depth map, minimizing multi-view reprojection error. It introduces an efficient optimization for over 50k points with Gaussian splatting, enabling self-supervised learning. Results show improved average and outlier errors over baselines, with high reconstruction quality.
- **核心贡献**: 提出可微扩散框架，实现从稀疏点集到稠密深度图的自监督优化。
- **创新点**: 利用高斯点云和解析透射率进行可微扩散，支持大规模点集高效优化。
- **结果**: 在光场和宽基线数据上，深度估计的平均和离群误差均显著降低。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method to estimate dense depth by optimizing a sparse set of points such that their diffusion into a depth map minimizes a multi-view reprojection error from RGB supervision. We optimize point positions, depths, and weights with respect to the loss by differential splatting that models points as Gaussians with analytic transmittance. Further, we develop an efficient optimization routine that can simultaneously optimize the 50k+ points required for complex scene reconstruction. We validate our routine using ground truth data and show high reconstruction quality. Then, we apply this to light field and wider baseline images via self supervision, and show improvements in both average and outlier error for depth maps diffused from inaccurate sparse points. Finally, we compare qualitative and quantitative results to image processing and deep learning methods. http://visual.cs.brown.edu/diffdiffdepth

</details>

### Multi-view Depth Estimation using Epipolar Spatio-Temporal Networks. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Long_Multi-view_Depth_Estimation_using_Epipolar_Spatio-Temporal_Networks_CVPR_2021_paper.html) · 📚 被引 55
- **作者**: Xiaoxiao Long, Lingjie Liu, Wei Li, Christian Theobalt, Wenping Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多视图深度估计中时间一致性和跨视角匹配问题。②提出极线时空网络，结合极线几何和时空特征提取，利用多帧信息增强深度预测。③相比单帧方法，引入时间维度，提升动态场景的鲁棒性。④摘要缺失，但预期在标准多视图数据集上表现优于基线。
- **摘要（英）**: This paper tackles multi-view depth estimation by integrating epipolar geometry with spatio-temporal networks, leveraging temporal cues across frames. The method enhances depth prediction robustness in dynamic scenes. Expected improvements over single-frame baselines are reported.
- **核心贡献**: 提出极线时空网络，融合多帧信息提升深度估计精度。
- **创新点**: 结合极线约束和时空特征，增强跨视角一致性。
- **结果**: 预期在动态场景中深度估计精度提升。

### Reconsidering Representation Alignment for Multi-View Clustering. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2103.07738](https://arxiv.org/abs/2103.07738) · 📚 被引 220
- **作者**: Daniel J. Trosten, Sigurd Løkse, Robert Jenssen, Michael Kampffmeyer
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对多视图聚类中表示对齐的缺陷，如聚类可分性降低和视图优先级抑制。②提出避免直接对齐的简单基线模型，并引入对比学习组件进行选择性对齐。③相比现有方法，保留视图优先级能力，提升聚类性能。④实验表明，在多个数据集上大幅超越当前最先进方法。
- **摘要（英）**: This paper identifies drawbacks of representation alignment in multi-view clustering, such as reduced cluster separability and view prioritization issues. It proposes a baseline without alignment, enhanced by contrastive learning for selective alignment. Results show large improvements over state-of-the-art on several datasets.
- **核心贡献**: 提出无对齐的多视图聚类基线，结合对比学习提升性能。
- **创新点**: 选择性对齐机制，避免直接分布匹配的负面影响。
- **结果**: 在多个数据集上显著优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aligning distributions of view representations is a core component of today's state of the art models for deep multi-view clustering. However, we identify several drawbacks with naïvely aligning representation distributions. We demonstrate that these drawbacks both lead to less separable clusters in the representation space, and inhibit the model's ability to prioritize views. Based on these observations, we develop a simple baseline model for deep multi-view clustering. Our baseline model avoids representation alignment altogether, while performing similar to, or better than, the current state of the art. We also expand our baseline model by adding a contrastive learning component. This introduces a selective alignment procedure that preserves the model's ability to prioritize views. Our experiments show that the contrastive learning component enhances the baseline model, improving on the current state of the art by a large margin on several datasets.

</details>

### MVTN: Multi-View Transformation Network for 3D Shape Recognition.
- **链接**: [arXiv:2011.13244](https://arxiv.org/abs/2011.13244) · [代码](https://github.com/ajhamdi/MVTN) · 📚 被引 219
- **作者**: Abdullah Hamdi, Silvio Giancola, Bernard Ghanem
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST),Thuwal,Saudi Arabia
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view projection methods have demonstrated their ability to reach state-of-the-art performance on 3D shape recognition. Those methods learn different ways to aggregate information from multiple views. However, the camera view-points for those views tend to be heuristically set and fixed for all shapes. To circumvent the lack of dynamism of current multi-view methods, we propose to learn those view-points. In particular, we introduce the Multi-View Transformation Network (MVTN) that regresses optimal view-points for 3D shape recognition, building upon advances in differentiable rendering. As a result, MVTN can be trained end-to-end along with any multi-view network for 3D shape classification. We integrate MVTN in a novel adaptive multi-view pipeline that can render either 3D meshes or point clouds. MVTN exhibits clear performance gains in the tasks of 3D shape classification and 3D shape retrieval without the need for extra training supervision. In these tasks, MVTN achieves state-of-the-art performance on ModelNet40, ShapeNet Core55, and the most recent and realistic ScanObjectNN dataset (up to 6% improvement). Interestingly, we also show that MVTN can provide network robustness against rotation and occlusion in the 3D domain. The code is available at https://github.com/ajhamdi/MVTN .

</details>

### PatchmatchNet: Learned Multi-View Patchmatch Stereo. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2012.01411](https://arxiv.org/abs/2012.01411) · 📚 被引 380
- **作者**: Fangjinhua Wang, Silvano Galliani, Christoph Vogel, Pablo Speciale, Marc Pollefeys
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对高分辨率多视图立体匹配中3D代价体积正则化的高计算和内存开销。②提出PatchmatchNet，一种可学习的级联Patchmatch框架，引入迭代多尺度Patchmatch和自适应传播评估。③相比传统方法，无需3D代价体积，效率更高，适合资源受限设备。④在DTU、Tanks & Temples和ETH3D上性能竞争力强，速度比最先进方法快至少2.5倍，内存减半。
- **摘要（英）**: This paper presents PatchmatchNet, a learnable cascade Patchmatch for high-resolution multi-view stereo, avoiding 3D cost volume regularization. It introduces iterative multi-scale Patchmatch with adaptive propagation. Results show competitive performance on DTU, Tanks & Temples, and ETH3D, with at least 2.5x speedup and half memory usage.
- **核心贡献**: 提出高效可学习的Patchmatch网络，替代3D代价体积。
- **创新点**: 迭代多尺度Patchmatch和自适应传播评估机制。
- **结果**: 在多个基准上性能优异，速度提升2.5倍以上，内存减半。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present PatchmatchNet, a novel and learnable cascade formulation of Patchmatch for high-resolution multi-view stereo. With high computation speed and low memory requirement, PatchmatchNet can process higher resolution imagery and is more suited to run on resource limited devices than competitors that employ 3D cost volume regularization. For the first time we introduce an iterative multi-scale Patchmatch in an end-to-end trainable architecture and improve the Patchmatch core algorithm with a novel and learned adaptive propagation and evaluation scheme for each iteration. Extensive experiments show a very competitive performance and generalization for our method on DTU, Tanks & Temples and ETH3D, but at a significantly higher efficiency than all existing top-performing models: at least two and a half times faster than state-of-the-art methods with twice less memory usage.

</details>

### IBRNet: Learning Multi-View Image-Based Rendering. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2102.13090](https://arxiv.org/abs/2102.13090) · 📚 被引 677
- **作者**: Qianqian Wang, Zhicheng Wang, Kyle Genova, Pratul P. Srinivasan, Howard Zhou, Jonathan T. Barron et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: ①针对复杂场景的新视图合成，现有神经场景表示需逐场景优化，泛化性差。②提出IBRNet，结合多层感知机和射线Transformer，从多个源视图动态提取外观信息，估计辐射和密度。③相比神经渲染，学习通用视图插值函数，可泛化到新场景。④实验表明，在泛化任务上优于现有方法，微调后与单场景最先进方法竞争。
- **摘要（英）**: This paper addresses novel view synthesis by learning a generic view interpolation function with a ray transformer, drawing appearance from source views. It generalizes to unseen scenes without per-scene optimization. Results outperform recent methods in generalization and are competitive after fine-tuning.
- **核心贡献**: 提出IBRNet，学习通用视图插值函数，支持新场景渲染。
- **创新点**: 射线Transformer动态融合多视图信息。
- **结果**: 在泛化任务上超越现有方法，微调后性能接近单场景最优。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method that synthesizes novel views of complex scenes by interpolating a sparse set of nearby views. The core of our method is a network architecture that includes a multilayer perceptron and a ray transformer that estimates radiance and volume density at continuous 5D locations (3D spatial locations and 2D viewing directions), drawing appearance information on the fly from multiple source views. By drawing on source views at render time, our method hearkens back to classic work on image-based rendering (IBR), and allows us to render high-resolution imagery. Unlike neural scene representation work that optimizes per-scene functions for rendering, we learn a generic view interpolation function that generalizes to novel scenes. We render images using classic volume rendering, which is fully differentiable and allows us to train using only multi-view posed images as supervision. Experiments show that our method outperforms recent novel view synthesis methods that also seek to generalize to novel scenes. Further, if fine-tuned on each scene, our method is competitive with state-of-the-art single-scene neural rendering methods. Project page: https://ibrnet.github.io/

</details>

### Self-Supervised Learning of Depth Inference for Multi-View Stereo.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_Self-Supervised_Learning_of_Depth_Inference_for_Multi-View_Stereo_CVPR_2021_paper.html) · 📚 被引 55
- **作者**: Jiayu Yang, José M. Álvarez, Miaomiao Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### DyGLIP: A Dynamic Graph Model With Link Prediction for Accurate Multi-Camera Multiple Object Tracking. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2106.06856](https://arxiv.org/abs/2106.06856) · 📚 被引 67
- **作者**: Kha Gia Quach, Pha A. Nguyen, Huu Le, Thanh-Dat Truong, Chi Nhan Duong, Minh-Triet Tran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对多相机多目标跟踪（MC-MOT）中数据关联的挑战，如光照变化、运动模式差异和跨相机轨迹遮挡，提出了一种基于动态图模型与链接预测（DyGLIP）的新方法。该方法通过动态图建模和链接预测改进特征表示，并能从相机切换时的轨迹丢失中恢复，且不依赖相机重叠率。实验表明，在多个实际数据集上显著优于现有MC-MOT算法，并支持在线和增量式设置。
- **摘要（英）**: This paper addresses the data association challenge in multi-camera multi-object tracking (MC-MOT), proposing a Dynamic Graph Model with Link Prediction (DyGLIP) that improves feature representations and recovers from lost tracks during camera transitions, regardless of overlap ratios. Experiments show large margins over existing MC-MOT algorithms on practical datasets, with support for online and incremental settings.
- **核心贡献**: 提出DyGLIP动态图模型，有效解决MC-MOT中的数据关联问题。
- **创新点**: 将链接预测引入动态图模型，增强跨相机轨迹关联的鲁棒性。
- **结果**: 在多个实际数据集上大幅超越现有MC-MOT算法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-Camera Multiple Object Tracking (MC-MOT) is a significant computer vision problem due to its emerging applicability in several real-world applications. Despite a large number of existing works, solving the data association problem in any MC-MOT pipeline is arguably one of the most challenging tasks. Developing a robust MC-MOT system, however, is still highly challenging due to many practical issues such as inconsistent lighting conditions, varying object movement patterns, or the trajectory occlusions of the objects between the cameras. To address these problems, this work, therefore, proposes a new Dynamic Graph Model with Link Prediction (DyGLIP) approach to solve the data association task. Compared to existing methods, our new model offers several advantages, including better feature representations and the ability to recover from lost tracks during camera transitions. Moreover, our model works gracefully regardless of the overlapping ratios between the cameras. Experimental results show that we outperform existing MC-MOT algorithms by a large margin on several practical datasets. Notably, our model works favorably on online settings but can be extended to an incremental approach for large-scale datasets.

</details>

### Wide-Baseline Multi-Camera Calibration Using Person Re-Identification. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2104.08568](https://arxiv.org/abs/2104.08568) · 📚 被引 26
- **作者**: Yan Xu, Yu-Jhe Li, Xinshuo Weng, Kris Kitani
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对大场景宽基线多相机标定中3D关键点匹配困难的问题，提出利用行人重识别（re-ID）技术将行人作为自然关键点进行跨相机关联，从而获取对应关系并求解相机位姿。该方法无需专用标定目标，仅需场景中可见行人，适用于频繁标定更新的场景。在多个不同场景数据集上进行了广泛实验验证。
- **摘要（英）**: This paper tackles wide-baseline multi-camera calibration by using person re-identification to associate pedestrians as natural keypoints across views, converting bounding box correspondences to point correspondences for pose estimation. It requires no specialized calibration targets, making it suitable for frequent recalibration, and is validated on diverse datasets.
- **核心贡献**: 提出基于行人重识别的宽基线相机标定方法。
- **创新点**: 利用行人作为自然关键点，避免传统标定目标依赖。
- **结果**: 在多个场景数据集上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the problem of estimating the 3D pose of a network of cameras for large-environment wide-baseline scenarios, e.g., cameras for construction sites, sports stadiums, and public spaces. This task is challenging since detecting and matching the same 3D keypoint observed from two very different camera views is difficult, making standard structure-from-motion (SfM) pipelines inapplicable. In such circumstances, treating people in the scene as "keypoints" and associating them across different camera views can be an alternative method for obtaining correspondences. Based on this intuition, we propose a method that uses ideas from person re-identification (re-ID) for wide-baseline camera calibration. Our method first employs a re-ID method to associate human bounding boxes across cameras, then converts bounding box correspondences to point correspondences, and finally solves for camera pose using multi-view geometry and bundle adjustment. Since our method does not require specialized calibration targets except for visible people, it applies to situations where frequent calibration updates are required. We perform extensive experiments on datasets captured from scenes of different sizes, camera settings (indoor and outdoor), and human activities (walking, playing basketball, construction). Experiment results show that our method achieves similar performance to standard SfM methods relying on manually labeled point correspondences.

</details>

### Monocular Depth Estimation via Listwise Ranking Using the Plackett-Luce Model. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2010.13118](https://arxiv.org/abs/2010.13118) · 📚 被引 12
- **作者**: Julian Lienen, Eyke Hüllermeier, Ralph Ewerth, Nils Nommensen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目深度估计中回归方法忽略相对深度顺序的问题，提出基于Plackett-Luce模型的列表排序方法，作为成对排序的推广。该方法结合先进神经网络架构和简单采样策略降低训练复杂度，并能从排序数据中恢复平移不变的度量深度。在多个基准数据集上进行了零样本评估。
- **摘要（英）**: This paper proposes a listwise ranking approach based on the Plackett-Luce model for monocular depth estimation, generalizing pairwise ranking to better capture relative depth order. It integrates with modern neural architectures and a sampling strategy to reduce complexity, enabling recovery of shift-invariant metric depth from ranking-only data, with zero-shot evaluation on benchmarks.
- **核心贡献**: 提出基于Plackett-Luce模型的列表排序深度估计方法。
- **创新点**: 将列表排序引入单目深度估计，超越成对比较。
- **结果**: 在多个基准数据集上展示了零样本评估结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In many real-world applications, the relative depth of objects in an image is crucial for scene understanding. Recent approaches mainly tackle the problem of depth prediction in monocular images by treating the problem as a regression task. Yet, being interested in an order relation in the first place, ranking methods suggest themselves as a natural alternative to regression, and indeed, ranking approaches leveraging pairwise comparisons as training information ("object A is closer to the camera than B") have shown promising performance on this problem. In this paper, we elaborate on the use of so-called listwise ranking as a generalization of the pairwise approach. Our method is based on the Plackett-Luce (PL) model, a probability distribution on rankings, which we combine with a state-of-the-art neural network architecture and a simple sampling strategy to reduce training complexity. Moreover, taking advantage of the representation of PL as a random utility model, the proposed predictor offers a natural way to recover (shift-invariant) metric depth information from ranking-only data provided at training time. An empirical evaluation on several benchmark datasets in a "zero-shot" setting demonstrates the effectiveness of our approach compared to existing ranking and regression methods.

</details>

### Boosting Monocular Depth Estimation Models to High-Resolution via Content-Adaptive Multi-Resolution Merging. **⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2105.14021](https://arxiv.org/abs/2105.14021) · 📚 被引 145
- **作者**: S. Mahdi H. Miangoleh, Sebastian Dille, Long Mai, Sylvain Paris, Yagiz Aksoy
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对单目深度估计模型输出分辨率低且缺乏细节的问题，分析了输入分辨率和场景结构对性能的影响，提出内容自适应多分辨率合并方法。通过合并低分辨率和高分辨率估计，利用深度合并网络平衡场景结构一致性和高频细节，并采用双估计和补丁选择方法增强局部细节。实验表明能生成多兆像素的高细节深度图。
- **摘要（英）**: This paper addresses low-resolution and detail-poor depth maps from monocular depth estimation by analyzing resolution and scene structure trade-offs, proposing a content-adaptive multi-resolution merging method. It merges low- and high-resolution estimates via a depth merging network, with double estimation and patch selection to add local details, generating multi-megapixel depth maps with high detail.
- **核心贡献**: 提出内容自适应多分辨率合并方法，提升单目深度估计分辨率。
- **创新点**: 利用分辨率与场景结构的权衡，通过合并网络增强细节。
- **结果**: 生成多兆像素高细节深度图。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks have shown great abilities in estimating depth from a single image. However, the inferred depth maps are well below one-megapixel resolution and often lack fine-grained details, which limits their practicality. Our method builds on our analysis on how the input resolution and the scene structure affects depth estimation performance. We demonstrate that there is a trade-off between a consistent scene structure and the high-frequency details, and merge low- and high-resolution estimations to take advantage of this duality using a simple depth merging network. We present a double estimation method that improves the whole-image depth estimation and a patch selection method that adds local details to the final result. We demonstrate that by merging estimations at different resolutions with changing context, we can generate multi-megapixel depth maps with a high level of detail using a pre-trained model.

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
