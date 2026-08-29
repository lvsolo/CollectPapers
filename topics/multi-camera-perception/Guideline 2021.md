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

> Learning non-rigid registration in an end-to-end manner is challenging due to the inherent high degrees of freedom and the lack of labeled training data. In this paper, we resolve these two challenges simultaneously. First, we propose to represent the non-rigid transformation with a point-wise combination of several rigid transformations. This representation not only makes the solution space well-constrained but also enables our method to be solved iteratively with a recurrent framework, which greatly reduces the difficulty of learning. Second, we introduce a differentiable loss function that measures the 3D shape similarity on the projected multi-view 2D depth images so that our full framework can be trained end-to-end without ground truth supervision. Extensive experiments on several different datasets demonstrate that our proposed method outperforms the previous state-of-the-art by a large margin. The source codes are available at https://github.com/WanquanF/RMA-Net.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Aligning distributions of view representations is a core component of today's state of the art models for deep multi-view clustering. However, we identify several drawbacks with naïvely aligning representation distributions. We demonstrate that these drawbacks both lead to less separable clusters in the representation space, and inhibit the model's ability to prioritize views. Based on these observations, we develop a simple baseline model for deep multi-view clustering. Our baseline model avoids representation alignment altogether, while performing similar to, or better than, the current state of the art. We also expand our baseline model by adding a contrastive learning component. This introduces a selective alignment procedure that preserves the model's ability to prioritize views. Our experiments show that the contrastive learning component enhances the baseline model, improving on the current state of the art by a large margin on several datasets.

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

> We address the problem of estimating the 3D pose of a network of cameras for large-environment wide-baseline scenarios, e.g., cameras for construction sites, sports stadiums, and public spaces. This task is challenging since detecting and matching the same 3D keypoint observed from two very different camera views is difficult, making standard structure-from-motion (SfM) pipelines inapplicable. In such circumstances, treating people in the scene as "keypoints" and associating them across different camera views can be an alternative method for obtaining correspondences. Based on this intuition, we propose a method that uses ideas from person re-identification (re-ID) for wide-baseline camera calibration. Our method first employs a re-ID method to associate human bounding boxes across cameras, then converts bounding box correspondences to point correspondences, and finally solves for camera pose using multi-view geometry and bundle adjustment. Since our method does not require specialized calibration targets except for visible people, it applies to situations where frequent calibration updates are required. We perform extensive experiments on datasets captured from scenes of different sizes, camera settings (indoor and outdoor), and human activities (walking, playing basketball, construction). Experiment results show that our method achieves similar performance to standard SfM methods relying on manually labeled point correspondences.

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural networks have shown great abilities in estimating depth from a single image. However, the inferred depth maps are well below one-megapixel resolution and often lack fine-grained details, which limits their practicality. Our method builds on our analysis on how the input resolution and the scene structure affects depth estimation performance. We demonstrate that there is a trade-off between a consistent scene structure and the high-frequency details, and merge low- and high-resolution estimations to take advantage of this duality using a simple depth merging network. We present a double estimation method that improves the whole-image depth estimation and a patch selection method that adds local details to the final result. We demonstrate that by merging estimations at different resolutions with changing context, we can generate multi-megapixel depth maps with a high level of detail using a pre-trained model.

</details>

### Three Ways To Improve Semantic Segmentation With Self-Supervised Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hoyer_Three_Ways_To_Improve_Semantic_Segmentation_With_Self-Supervised_Depth_Estimation_CVPR_2021_paper.html) · 📚 被引 76
- **作者**: Lukas Hoyer, Dengxin Dai, Yuhua Chen, Adrian Köring, Suman Saha, Luc Van Gool
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
