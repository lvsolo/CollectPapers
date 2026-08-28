# Multi-camera Perception — 2021 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Visio-Temporal Attention for Multi-Camera Multi-Target Association.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00969) · 📚 被引 11
- **作者**: Yu-Jhe Li, Xinshuo Weng, Yan Xu, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: ICCV 2021

### Lightweight Multi-person Total Motion Capture Using Sparse Multi-view Cameras.
- **链接**: [arXiv:2108.10378](https://arxiv.org/abs/2108.10378)
- **作者**: Yuxiang Zhang, Zhe Li, Liang An, Mengcheng Li, Tao Yu, Yebin Liu
- **🏷️ 机构**: Tsinghua University,Department of Automation and BNRist
- **会议**: ICCV 2021

### COMPLETER: Incomplete Multi-View Clustering via Contrastive Prediction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Lin_COMPLETER_Incomplete_Multi-View_Clustering_via_Contrastive_Prediction_CVPR_2021_paper.html) · 📚 被引 404
- **作者**: Yijie Lin, Yuanbiao Gou, Zitao Liu, Boyun Li, Jiancheng Lv, Xi Peng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

> Multi-person total motion capture is extremely challenging when it comes to handle severe occlusions, different reconstruction granularities from body to face and hands, drastically changing observation scales and fast body movements. To overcome these challenges above, we contribute a lightweight total motion capture system for multi-person interactive scenarios using only sparse multi-view cameras. By contributing a novel hand and face bootstrapping algorithm, our method is capable of efficient localization and accurate association of the hands and faces even on severe occluded occasions. We leverage both pose regression and keypoints detection methods and further propose a unified two-stage parametric fitting method for achieving pixel-aligned accuracy. Moreover, for extremely self-occluded poses and close interactions, a novel feedback mechanism is proposed to propagate the pixel-aligned reconstructions into the next frame for more accurate association. Overall, we propose the first light-weight total capture system and achieves fast, robust and accurate multi-person total motion capture performance. The results and experiments show that our method achieves more accurate results than existing methods under sparse-view setups.

</details>

### DeepMultiCap: Performance Capture of Multiple Characters Using Sparse Multiview Cameras.
- **链接**: [arXiv:2105.00261](https://arxiv.org/abs/2105.00261) · 📚 被引 87
- **作者**: Yang Zheng, Ruizhi Shao, Yuxiang Zhang, Tao Yu, Zerong Zheng, Qionghai Dai et al.
- **🏷️ 机构**: Tsinghua University,Department of Automation and BNRist
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning non-rigid registration in an end-to-end manner is challenging due to the inherent high degrees of freedom and the lack of labeled training data. In this paper, we resolve these two challenges simultaneously. First, we propose to represent the non-rigid transformation with a point-wise combination of several rigid transformations. This representation not only makes the solution space well-constrained but also enables our method to be solved iteratively with a recurrent framework, which greatly reduces the difficulty of learning. Second, we introduce a differentiable loss function that measures the 3D shape similarity on the projected multi-view 2D depth images so that our full framework can be trained end-to-end without ground truth supervision. Extensive experiments on several different datasets demonstrate that our proposed method outperforms the previous state-of-the-art by a large margin. The source codes are available at https://github.com/WanquanF/RMA-Net.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method to estimate dense depth by optimizing a sparse set of points such that their diffusion into a depth map minimizes a multi-view reprojection error from RGB supervision. We optimize point positions, depths, and weights with respect to the loss by differential splatting that models points as Gaussians with analytic transmittance. Further, we develop an efficient optimization routine that can simultaneously optimize the 50k+ points required for complex scene reconstruction. We validate our routine using ground truth data and show high reconstruction quality. Then, we apply this to light field and wider baseline images via self supervision, and show improvements in both average and outlier error for depth maps diffused from inaccurate sparse points. Finally, we compare qualitative and quantitative results to image processing and deep learning methods. http://visual.cs.brown.edu/diffdiffdepth

</details>

> Satellite multi-view stereo (MVS) imagery is particularly suited for large-scale Earth surface reconstruction. Differing from the perspective camera model (pin-hole model) that is commonly used for close-range and aerial cameras, the cubic rational polynomial camera (RPC) model is the mainstream model for push-broom linear-array satellite cameras. However, the homography warping used in the prevailing learning based MVS methods is only applicable to pin-hole cameras. In order to apply the SOTA learning based MVS technology to the satellite MVS task for large-scale Earth surface reconstruction, RPC warping should be considered. In this work, we propose, for the first time, a rigorous RPC warping module. The rational polynomial coefficients are recorded as a tensor, and the RPC warping is formulated as a series of tensor transformations. Based on the RPC warping, we propose the deep learning based satellite MVS (SatMVS) framework for large-scale and wide depth range Earth surface reconstruction. We also introduce a large-scale satellite image dataset consisting of 519 5120${\times}$5120 images, which we call the TLC SatMVS dataset. The satellite images were acquired from a three-line camera (TLC) that catches triple-view images simultaneously, forming a valuable supplement to the existing open-source WorldView-3 datasets with single-scanline images. Experiments show that the proposed RPC warping module and the SatMVS framework can achieve a superior reconstruction accuracy compared to the pin-hole fitting method and conventional MVS methods. Code and data are available at https://github.com/WHU-GPCV/SatMVS.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aligning distributions of view representations is a core component of today's state of the art models for deep multi-view clustering. However, we identify several drawbacks with naïvely aligning representation distributions. We demonstrate that these drawbacks both lead to less separable clusters in the representation space, and inhibit the model's ability to prioritize views. Based on these observations, we develop a simple baseline model for deep multi-view clustering. Our baseline model avoids representation alignment altogether, while performing similar to, or better than, the current state of the art. We also expand our baseline model by adding a contrastive learning component. This introduces a selective alignment procedure that preserves the model's ability to prioritize views. Our experiments show that the contrastive learning component enhances the baseline model, improving on the current state of the art by a large margin on several datasets.

</details>

### Boosting Monocular Depth Estimation with Lightweight 3D Point Fusion.
- **链接**: [arXiv:2012.10296](https://arxiv.org/abs/2012.10296) · 📚 被引 26
- **作者**: Lam Huynh, Phong Nguyen, Jirí Matas, Esa Rahtu, Janne Heikkilä
- **🏷️ 机构**: University of Oulu, Czech Technical University in Prague, Tampere University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose enhancing monocular depth estimation by adding 3D points as depth guidance. Unlike existing depth completion methods, our approach performs well on extremely sparse and unevenly distributed point clouds, which makes it agnostic to the source of the 3D points. We achieve this by introducing a novel multi-scale 3D point fusion network that is both lightweight and efficient. We demonstrate its versatility on two different depth estimation problems where the 3D points have been acquired with conventional structure-from-motion and LiDAR. In both cases, our network performs on par with state-of-the-art depth completion methods and achieves significantly higher accuracy when only a small number of points is used while being more compact in terms of the number of parameters. We show that our method outperforms some contemporary deep learning based multi-view stereo and structure-from-motion methods both in accuracy and in compactness.

</details>

### MonoIndoor: Towards Good Practice of Self-Supervised Monocular Depth Estimation for Indoor Environments.
- **链接**: [arXiv:2107.12429](https://arxiv.org/abs/2107.12429) · 📚 被引 80
- **作者**: Pan Ji, Runze Li, Bir Bhanu, Yi Xu
- **🏷️ 机构**: InnoPeak Technology, Inc.,OPPO US Research Center, University of California Riverside
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the problem of estimating the 3D pose of a network of cameras for large-environment wide-baseline scenarios, e.g., cameras for construction sites, sports stadiums, and public spaces. This task is challenging since detecting and matching the same 3D keypoint observed from two very different camera views is difficult, making standard structure-from-motion (SfM) pipelines inapplicable. In such circumstances, treating people in the scene as "keypoints" and associating them across different camera views can be an alternative method for obtaining correspondences. Based on this intuition, we propose a method that uses ideas from person re-identification (re-ID) for wide-baseline camera calibration. Our method first employs a re-ID method to associate human bounding boxes across cameras, then converts bounding box correspondences to point correspondences, and finally solves for camera pose using multi-view geometry and bundle adjustment. Since our method does not require specialized calibration targets except for visible people, it applies to situations where frequent calibration updates are required. We perform extensive experiments on datasets captured from scenes of different sizes, camera settings (indoor and outdoor), and human activities (walking, playing basketball, construction). Experiment results show that our method achieves similar performance to standard SfM methods relying on manually labeled point correspondences.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In many real-world applications, the relative depth of objects in an image is crucial for scene understanding. Recent approaches mainly tackle the problem of depth prediction in monocular images by treating the problem as a regression task. Yet, being interested in an order relation in the first place, ranking methods suggest themselves as a natural alternative to regression, and indeed, ranking approaches leveraging pairwise comparisons as training information ("object A is closer to the camera than B") have shown promising performance on this problem. In this paper, we elaborate on the use of so-called listwise ranking as a generalization of the pairwise approach. Our method is based on the Plackett-Luce (PL) model, a probability distribution on rankings, which we combine with a state-of-the-art neural network architecture and a simple sampling strategy to reduce training complexity. Moreover, taking advantage of the representation of PL as a random utility model, the proposed predictor offers a natural way to recover (shift-invariant) metric depth information from ranking-only data provided at training time. An empirical evaluation on several benchmark datasets in a "zero-shot" setting demonstrates the effectiveness of our approach compared to existing ranking and regression methods.

</details>

> Self-supervised monocular depth estimation has been widely studied, owing to its practical importance and recent promising improvements. However, most works suffer from limited supervision of photometric consistency, especially in weak texture regions and at object boundaries. To overcome this weakness, we propose novel ideas to improve self-supervised monocular depth estimation by leveraging cross-domain information, especially scene semantics. We focus on incorporating implicit semantic knowledge into geometric representation enhancement and suggest two ideas: a metric learning approach that exploits the semantics-guided local geometry to optimize intermediate depth representations and a novel feature fusion module that judiciously utilizes cross-modality between two heterogeneous feature representations. We comprehensively evaluate our methods on the KITTI dataset and demonstrate that our method outperforms state-of-the-art methods. The source code is available at https://github.com/hyBlue/FSRE-Depth.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks have shown great abilities in estimating depth from a single image. However, the inferred depth maps are well below one-megapixel resolution and often lack fine-grained details, which limits their practicality. Our method builds on our analysis on how the input resolution and the scene structure affects depth estimation performance. We demonstrate that there is a trade-off between a consistent scene structure and the high-frequency details, and merge low- and high-resolution estimations to take advantage of this duality using a simple depth merging network. We present a double estimation method that improves the whole-image depth estimation and a patch selection method that adds local details to the final result. We demonstrate that by merging estimations at different resolutions with changing context, we can generate multi-megapixel depth maps with a high level of detail using a pre-trained model.

</details>

### Excavating the Potential Capacity of Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01527) · 📚 被引 99
- **作者**: Rui Peng, Ronggang Wang, Yawen Lai, Luyang Tang, Yangang Cai
- **🏷️ 机构**: Peking University,School of Electronic and Computer Engineering
- **会议**: ICCV 2021

### Regularizing Nighttime Weirdness: Efficient Self-supervised Monocular Depth Estimation in the Dark.
- **链接**: [arXiv:2108.03830](https://arxiv.org/abs/2108.03830) · 📚 被引 81
- **作者**: Kun Wang, Zhenyu Zhang, Zhiqiang Yan, Xiang Li, Baobei Xu, Jun Li et al.
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,China, Tencent YouTu Lab, Hikvision Research Institute
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation aims at predicting depth from a single image or video. Recently, self-supervised methods draw much attention since they are free of depth annotations and achieve impressive performance on several daytime benchmarks. However, they produce weird outputs in more challenging nighttime scenarios because of low visibility and varying illuminations, which bring weak textures and break brightness-consistency assumption, respectively. To address these problems, in this paper we propose a novel framework with several improvements: (1) we introduce Priors-Based Regularization to learn distribution knowledge from unpaired depth maps and prevent model from being incorrectly trained; (2) we leverage Mapping-Consistent Image Enhancement module to enhance image visibility and contrast while maintaining brightness consistency; and (3) we present Statistics-Based Mask strategy to tune the number of removed pixels within textureless regions, using dynamic statistics. Experimental results demonstrate the effectiveness of each component. Meanwhile, our framework achieves remarkable improvements and state-of-the-art results on two nighttime datasets.

</details>

### Towards Interpretable Deep Networks for Monocular Depth Estimation.
- **链接**: [arXiv:2108.05312](https://arxiv.org/abs/2108.05312) · [代码](https://github.com/youzunzhi/InterpretableMDE) · 📚 被引 15
- **作者**: Zunzhi You, Yi-Hsuan Tsai, Wei-Chen Chiu, Guanbin Li
- **🏷️ 机构**: Sun Yat-sen University, NEC Laboratories America, National Chiao Tung University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep networks for Monocular Depth Estimation (MDE) have achieved promising performance recently and it is of great importance to further understand the interpretability of these networks. Existing methods attempt to provide posthoc explanations by investigating visual cues, which may not explore the internal representations learned by deep networks. In this paper, we find that some hidden units of the network are selective to certain ranges of depth, and thus such behavior can be served as a way to interpret the internal representations. Based on our observations, we quantify the interpretability of a deep MDE network by the depth selectivity of its hidden units. Moreover, we then propose a method to train interpretable MDE deep networks without changing their original architectures, by assigning a depth range for each unit to select. Experimental results demonstrate that our method is able to enhance the interpretability of deep MDE networks by largely improving the depth selectivity of their units, while not harming or even improving the depth estimation accuracy. We further provide a comprehensive analysis to show the reliability of selective units, the applicability of our method on different layers, models, and datasets, and a demonstration on analysis of model error. Source code and models are available at https://github.com/youzunzhi/InterpretableMDE .

</details>

### Domain Adaptive Semantic Segmentation with Self-Supervised Depth Estimation.
- **链接**: [arXiv:2104.13613](https://arxiv.org/abs/2104.13613) · 📚 被引 132
- **作者**: Qin Wang, Dengxin Dai, Lukas Hoyer, Luc Van Gool, Olga Fink
- **🏷️ 机构**: ETH,Zurich,Switzerland
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain adaptation for semantic segmentation aims to improve the model performance in the presence of a distribution shift between source and target domain. Leveraging the supervision from auxiliary tasks~(such as depth estimation) has the potential to heal this shift because many visual tasks are closely related to each other. However, such a supervision is not always available. In this work, we leverage the guidance from self-supervised depth estimation, which is available on both domains, to bridge the domain gap. On the one hand, we propose to explicitly learn the task feature correlation to strengthen the target semantic predictions with the help of target depth estimation. On the other hand, we use the depth prediction discrepancy from source and target depth decoders to approximate the pixel-wise adaptation difficulty. The adaptation difficulty, inferred from depth, is then used to refine the target semantic segmentation pseudo-labels. The proposed method can be easily implemented into existing segmentation frameworks. We demonstrate the effectiveness of our approach on the benchmark tasks SYNTHIA-to-Cityscapes and GTA-to-Cityscapes, on which we achieve the new state-of-the-art performance of $55.0\%$ and $56.6\%$, respectively. Our code is available at \url{https://qin.ee/corda}.

</details>

### Digging into Uncertainty in Self-supervised Multi-view Stereo.
- **链接**: [arXiv:2108.12966](https://arxiv.org/abs/2108.12966) · 📚 被引 62
- **作者**: Hongbin Xu, Zhipeng Zhou, Yali Wang, Wenxiong Kang, Baigui Sun, Hao Li et al.
- **🏷️ 机构**: Chinese Academy of Sciences,ShenZhen Key Lab of Computer Vision and Pattern Recognition, Shenzhen Institute of Advanced Technology, Alibaba Group, South China University of Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised Multi-view stereo (MVS) with a pretext task of image reconstruction has achieved significant progress recently. However, previous methods are built upon intuitions, lacking comprehensive explanations about the effectiveness of the pretext task in self-supervised MVS. To this end, we propose to estimate epistemic uncertainty in self-supervised MVS, accounting for what the model ignores. Specially, the limitations can be categorized into two types: ambiguious supervision in foreground and invalid supervision in background. To address these issues, we propose a novel Uncertainty reduction Multi-view Stereo (UMVS) framework for self-supervised learning. To alleviate ambiguous supervision in foreground, we involve extra correspondence prior with a flow-depth consistency loss. The dense 2D correspondence of optical flows is used to regularize the 3D stereo correspondence in MVS. To handle the invalid supervision in background, we use Monte-Carlo Dropout to acquire the uncertainty map and further filter the unreliable supervision signals on invalid regions. Extensive experiments on DTU and Tank&Temples benchmark show that our U-MVS framework achieves the best performance among unsupervised MVS methods, with competitive performance with its supervised opponents.

</details>
