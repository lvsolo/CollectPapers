# Multi-camera Perception — 2021 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 33 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multi-VAE: Learning Disentangled View-common and View-peculiar Visual Representations for Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00910) · 📚 被引 130
- **作者**: Jie Xu, Yazhou Ren, Huayi Tang, Xiaorong Pu, Xiaofeng Zhu, Ming Zeng et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China,School of Computer Science and Engineering,Chengdu,China,611731, Carnegie Mellon University,Department of Electrical Computer Engineering,PA,USA,15213, Lehigh Univerisity,Department of Computer Science and Engineering,PA,USA,18015
- **会议**: ICCV 2021

### Just a Few Points are All You Need for Multi-view Stereo: A Novel Semi-supervised Learning Method for Multi-view Stereo.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00612) · 📚 被引 9
- **作者**: Taekyung Kim, Jaehoon Choi, Seokeon Choi, Dongki Jung, Changick Kim
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology, University of Maryland, NAVER LABS
- **会议**: ICCV 2021

### Image Manipulation Detection by Multi-View Multi-Scale Supervision.
- **链接**: [arXiv:2104.06832](https://arxiv.org/abs/2104.06832) · 📚 被引 244
- **作者**: Xinru Chen, Chengbo Dong, Jiaqi Ji, Juan Cao, Xirong Li
- **🏷️ 机构**: Renmin University of China,MoE Key Lab of Data Engineering and Knowledge Engineering, Chinese Academy of Sciences,Institute of Computing Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The key challenge of image manipulation detection is how to learn generalizable features that are sensitive to manipulations in novel data, whilst specific to prevent false alarms on authentic images. Current research emphasizes the sensitivity, with the specificity overlooked. In this paper we address both aspects by multi-view feature learning and multi-scale supervision. By exploiting noise distribution and boundary artifact surrounding tampered regions, the former aims to learn semantic-agnostic and thus more generalizable features. The latter allows us to learn from authentic images which are nontrivial to be taken into account by current semantic segmentation network based methods. Our thoughts are realized by a new network which we term MVSS-Net. Extensive experiments on five benchmark sets justify the viability of MVSS-Net for both pixel-level and image-level manipulation detection.

</details>

### Shape-aware Multi-Person Pose Estimation from Multi-View Images.
- **链接**: [arXiv:2110.02330](https://arxiv.org/abs/2110.02330) · 📚 被引 46
- **作者**: Zijian Dong, Jie Song, Xu Chen, Chen Guo, Otmar Hilliges
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper we contribute a simple yet effective approach for estimating 3D poses of multiple people from multi-view images. Our proposed coarse-to-fine pipeline first aggregates noisy 2D observations from multiple camera views into 3D space and then associates them into individual instances based on a confidence-aware majority voting technique. The final pose estimates are attained from a novel optimization scheme which links high-confidence multi-view 2D observations and 3D joint candidates. Moreover, a statistical parametric body model such as SMPL is leveraged as a regularizing prior for these 3D joint candidates. Specifically, both 3D poses and SMPL parameters are optimized jointly in an alternating fashion. Here the parametric models help in correcting implausible 3D pose estimates and filling in missing joint detections while updated 3D poses in turn guide obtaining better SMPL estimations. By linking 2D and 3D observations, our method is both accurate and generalizes to different data sources because it better decouples the final 3D pose from the inter-person constellation and is more robust to noisy 2D detections. We systematically evaluate our method on public datasets and achieve state-of-the-art performance. The code and video will be available on the project page: https://ait.ethz.ch/projects/2021/multi-human-pose/.

</details>

### Graph-Based 3D Multi-Person Pose Estimation Using Multi-View Images.
- **链接**: [arXiv:2109.05885](https://arxiv.org/abs/2109.05885) · 📚 被引 57
- **作者**: Size Wu, Sheng Jin, Wentao Liu, Lei Bai, Chen Qian, Dong Liu et al.
- **🏷️ 机构**: University of Science and Technology of China, The University of Hong Kong, SenseTime Research and Tetras.AI
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper studies the task of estimating the 3D human poses of multiple persons from multiple calibrated camera views. Following the top-down paradigm, we decompose the task into two stages, i.e. person localization and pose estimation. Both stages are processed in coarse-to-fine manners. And we propose three task-specific graph neural networks for effective message passing. For 3D person localization, we first use Multi-view Matching Graph Module (MMG) to learn the cross-view association and recover coarse human proposals. The Center Refinement Graph Module (CRG) further refines the results via flexible point-based prediction. For 3D pose estimation, the Pose Regression Graph Module (PRG) learns both the multi-view geometry and structural relations between human joints. Our approach achieves state-of-the-art performance on CMU Panoptic and Shelf datasets with significantly lower computation complexity.

</details>

### Lightweight Multi-person Total Motion Capture Using Sparse Multi-view Cameras.
- **链接**: [arXiv:2108.10378](https://arxiv.org/abs/2108.10378) · 📚 被引 49
- **作者**: Yuxiang Zhang, Zhe Li, Liang An, Mengcheng Li, Tao Yu, Yebin Liu
- **🏷️ 机构**: Tsinghua University,Department of Automation and BNRist
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-person total motion capture is extremely challenging when it comes to handle severe occlusions, different reconstruction granularities from body to face and hands, drastically changing observation scales and fast body movements. To overcome these challenges above, we contribute a lightweight total motion capture system for multi-person interactive scenarios using only sparse multi-view cameras. By contributing a novel hand and face bootstrapping algorithm, our method is capable of efficient localization and accurate association of the hands and faces even on severe occluded occasions. We leverage both pose regression and keypoints detection methods and further propose a unified two-stage parametric fitting method for achieving pixel-aligned accuracy. Moreover, for extremely self-occluded poses and close interactions, a novel feedback mechanism is proposed to propagate the pixel-aligned reconstructions into the next frame for more accurate association. Overall, we propose the first light-weight total capture system and achieves fast, robust and accurate multi-person total motion capture performance. The results and experiments show that our method achieves more accurate results than existing methods under sparse-view setups.

</details>

### One-pass Multi-view Clustering for Large-scale Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01212) · 📚 被引 126
- **作者**: Jiyuan Liu, Xinwang Liu, Yuexiang Yang, Li Liu, Siqi Wang, Weixuan Liang et al.
- **🏷️ 机构**: National University of Defense Technology,Changsha,China,410072
- **会议**: ICCV 2021

### Multi-view 3D Reconstruction with Transformers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00567)
- **作者**: Dan Wang, Xinrui Cui, Xun Chen, Zhengxia Zou, Tianyang Shi, Septimiu E. Salcudean et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### MVSNeRF: Fast Generalizable Radiance Field Reconstruction from Multi-View Stereo.
- **链接**: [arXiv:2103.15595](https://arxiv.org/abs/2103.15595) · 📚 被引 760
- **作者**: Anpei Chen, Zexiang Xu, Fuqiang Zhao, Xiaoshuai Zhang, Fanbo Xiang, Jingyi Yu et al.
- **🏷️ 机构**: ShanghaiTech University, Adobe Research, University of California,San Diego
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present MVSNeRF, a novel neural rendering approach that can efficiently reconstruct neural radiance fields for view synthesis. Unlike prior works on neural radiance fields that consider per-scene optimization on densely captured images, we propose a generic deep neural network that can reconstruct radiance fields from only three nearby input views via fast network inference. Our approach leverages plane-swept cost volumes (widely used in multi-view stereo) for geometry-aware scene reasoning, and combines this with physically based volume rendering for neural radiance field reconstruction. We train our network on real objects in the DTU dataset, and test it on three different datasets to evaluate its effectiveness and generalizability. Our approach can generalize across scenes (even indoor scenes, completely different from our training scenes of objects) and generate realistic view synthesis results using only three input images, significantly outperforming concurrent works on generalizable radiance field reconstruction. Moreover, if dense images are captured, our estimated radiance field representation can be easily fine-tuned; this leads to fast per-scene reconstruction with higher rendering quality and substantially less optimization time than NeRF.

</details>

### Rational Polynomial Camera Model Warping for Deep Learning Based Satellite Multi-View Stereo Matching.
- **链接**: [arXiv:2109.11121](https://arxiv.org/abs/2109.11121) · [代码](https://github.com/WHU-GPCV/SatMVS) · 📚 被引 35
- **作者**: Jian Gao, Jin Liu, Shunping Ji
- **🏷️ 机构**: Wuhan University,School of Remote Sensing and information Engineering,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Satellite multi-view stereo (MVS) imagery is particularly suited for large-scale Earth surface reconstruction. Differing from the perspective camera model (pin-hole model) that is commonly used for close-range and aerial cameras, the cubic rational polynomial camera (RPC) model is the mainstream model for push-broom linear-array satellite cameras. However, the homography warping used in the prevailing learning based MVS methods is only applicable to pin-hole cameras. In order to apply the SOTA learning based MVS technology to the satellite MVS task for large-scale Earth surface reconstruction, RPC warping should be considered. In this work, we propose, for the first time, a rigorous RPC warping module. The rational polynomial coefficients are recorded as a tensor, and the RPC warping is formulated as a series of tensor transformations. Based on the RPC warping, we propose the deep learning based satellite MVS (SatMVS) framework for large-scale and wide depth range Earth surface reconstruction. We also introduce a large-scale satellite image dataset consisting of 519 5120${\times}$5120 images, which we call the TLC SatMVS dataset. The satellite images were acquired from a three-line camera (TLC) that catches triple-view images simultaneously, forming a valuable supplement to the existing open-source WorldView-3 datasets with single-scanline images. Experiments show that the proposed RPC warping module and the SatMVS framework can achieve a superior reconstruction accuracy compared to the pin-hole fitting method and conventional MVS methods. Code and data are available at https://github.com/WHU-GPCV/SatMVS.

</details>

### MVTN: Multi-View Transformation Network for 3D Shape Recognition.
- **链接**: [arXiv:2011.13244](https://arxiv.org/abs/2011.13244) · [代码](https://github.com/ajhamdi/MVTN) · 📚 被引 219
- **作者**: Abdullah Hamdi, Silvio Giancola, Bernard Ghanem
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST),Thuwal,Saudi Arabia
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view projection methods have demonstrated their ability to reach state-of-the-art performance on 3D shape recognition. Those methods learn different ways to aggregate information from multiple views. However, the camera view-points for those views tend to be heuristically set and fixed for all shapes. To circumvent the lack of dynamism of current multi-view methods, we propose to learn those view-points. In particular, we introduce the Multi-View Transformation Network (MVTN) that regresses optimal view-points for 3D shape recognition, building upon advances in differentiable rendering. As a result, MVTN can be trained end-to-end along with any multi-view network for 3D shape classification. We integrate MVTN in a novel adaptive multi-view pipeline that can render either 3D meshes or point clouds. MVTN exhibits clear performance gains in the tasks of 3D shape classification and 3D shape retrieval without the need for extra training supervision. In these tasks, MVTN achieves state-of-the-art performance on ModelNet40, ShapeNet Core55, and the most recent and realistic ScanObjectNN dataset (up to 6% improvement). Interestingly, we also show that MVTN can provide network robustness against rotation and occlusion in the 3D domain. The code is available at https://github.com/ajhamdi/MVTN .

</details>

### Learning Efficient Photometric Feature Transform for Multi-view Stereo.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00590) · 📚 被引 2
- **作者**: Kaizhang Kang, Cihui Xie, Ruisheng Zhu, Xiaohe Ma, Ping Tan, Hongzhi Wu et al.
- **🏷️ 机构**: Zhejiang University, Simon Fraser University
- **会议**: ICCV 2021

### Human Detection and Segmentation via Multi-view Consensus.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00285) · 📚 被引 2
- **作者**: Isinsu Katircioglu, Helge Rhodin, Jörg Spörri, Mathieu Salzmann, Pascal Fua
- **🏷️ 机构**: EPFL,Lausanne,Switzerland, UBC,Vancouver,Canada, Balgrist University Hospital,Zurich,Switzerland
- **会议**: ICCV 2021

### Topologically Consistent Multi-View Face Inference Using Volumetric Sampling.
- **链接**: [arXiv:2110.02948](https://arxiv.org/abs/2110.02948) · 📚 被引 20
- **作者**: Tianye Li, Shichen Liu, Timo Bolkart, Jiayi Liu, Hao Li, Yajie Zhao
- **🏷️ 机构**: USC Institute for Creative Technologies, MPI for Intelligent Systems,T&#x00FC;bingen
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-fidelity face digitization solutions often combine multi-view stereo (MVS) techniques for 3D reconstruction and a non-rigid registration step to establish dense correspondence across identities and expressions. A common problem is the need for manual clean-up after the MVS step, as 3D scans are typically affected by noise and outliers and contain hairy surface regions that need to be cleaned up by artists. Furthermore, mesh registration tends to fail for extreme facial expressions. Most learning-based methods use an underlying 3D morphable model (3DMM) to ensure robustness, but this limits the output accuracy for extreme facial expressions. In addition, the global bottleneck of regression architectures cannot produce meshes that tightly fit the ground truth surfaces. We propose ToFu, Topologically consistent Face from multi-view, a geometry inference framework that can produce topologically consistent meshes across facial identities and expressions using a volumetric representation instead of an explicit underlying 3DMM. Our novel progressive mesh generation network embeds the topological structure of the face in a feature volume, sampled from geometry-aware local features. A coarse-to-fine architecture facilitates dense and accurate facial mesh predictions in a consistent mesh topology. ToFu further captures displacement maps for pore-level geometric details and facilitates high-quality rendering in the form of albedo and specular reflectance maps. These high-quality assets are readily usable by production studios for avatar creation, animation and physically-based skin rendering. We demonstrate state-of-the-art geometric and correspondence accuracy, while only taking 0.385 seconds to compute a mesh with 10K vertices, which is three orders of magnitude faster than traditional techniques. The code and the model are available for research purposes at https://tianyeli.github.io/tofu.

</details>

### EPP-MVSNet: Epipolar-assembling based Depth Prediction for Multi-view Stereo.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00568) · 📚 被引 130
- **作者**: Xinjun Ma, Yue Gong, Qirui Wang, Jingwei Huang, Lei Chen, Fan Yu
- **🏷️ 机构**: Huawei Technologies,Distributed and Parallel Software Lab, Hong Kong University of Science and Technology,Department of Computer Science and Engineering
- **会议**: ICCV 2021

### UNISURF: Unifying Neural Implicit Surfaces and Radiance Fields for Multi-View Reconstruction.
- **链接**: [arXiv:2104.10078](https://arxiv.org/abs/2104.10078) · 📚 被引 588
- **作者**: Michael Oechsle, Songyou Peng, Andreas Geiger
- **🏷️ 机构**: Max Planck Institute for Intelligent Systems,T&#x00FC;bingen
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural implicit 3D representations have emerged as a powerful paradigm for reconstructing surfaces from multi-view images and synthesizing novel views. Unfortunately, existing methods such as DVR or IDR require accurate per-pixel object masks as supervision. At the same time, neural radiance fields have revolutionized novel view synthesis. However, NeRF's estimated volume density does not admit accurate surface reconstruction. Our key insight is that implicit surface models and radiance fields can be formulated in a unified way, enabling both surface and volume rendering using the same model. This unified perspective enables novel, more efficient sampling procedures and the ability to reconstruct accurate surfaces without input masks. We compare our method on the DTU, BlendedMVS, and a synthetic indoor dataset. Our experiments demonstrate that we outperform NeRF in terms of reconstruction quality while performing on par with IDR without requiring masks.

</details>

### Multi-View Radar Semantic Segmentation.
- **链接**: [arXiv:2103.16214](https://arxiv.org/abs/2103.16214) · [代码](https://github.com/valeoai/MVRSS)
- **作者**: Arthur Ouaknine, Alasdair Newson, Patrick Pérez, Florence Tupin, Julien Rebut
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding the scene around the ego-vehicle is key to assisted and autonomous driving. Nowadays, this is mostly conducted using cameras and laser scanners, despite their reduced performances in adverse weather conditions. Automotive radars are low-cost active sensors that measure properties of surrounding objects, including their relative speed, and have the key advantage of not being impacted by rain, snow or fog. However, they are seldom used for scene understanding due to the size and complexity of radar raw data and the lack of annotated datasets. Fortunately, recent open-sourced datasets have opened up research on classification, object detection and semantic segmentation with raw radar signals using end-to-end trainable models. In this work, we propose several novel architectures, and their associated losses, which analyse multiple "views" of the range-angle-Doppler radar tensor to segment it semantically. Experiments conducted on the recent CARRADA dataset demonstrate that our best model outperforms alternative models, derived either from the semantic segmentation of natural images or from radar scene understanding, while requiring significantly fewer parameters. Both our code and trained models are available at https://github.com/valeoai/MVRSS.

</details>

### Stacked Homography Transformations for Multi-View Pedestrian Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00599) · 📚 被引 55
- **作者**: Liangchen Song, Jialian Wu, Ming Yang, Qian Zhang, Yuan Li, Junsong Yuan
- **🏷️ 机构**: University at Buffalo, Horizon Robotics, Inc, Google, Inc
- **会议**: ICCV 2021

### NerfingMVS: Guided Optimization of Neural Radiance Fields for Indoor Multi-view Stereo.
- **链接**: [arXiv:2109.01129](https://arxiv.org/abs/2109.01129) · [代码](https://github.com/weiyithu/NerfingMVS) · 📚 被引 228
- **作者**: Yi Wei, Shaohui Liu, Yongming Rao, Wang Zhao, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: Tsinghua University,Department of Automation,China, ETH,Zurich, Tsinghua University,Department of Computer Science and Technology,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we present a new multi-view depth estimation method that utilizes both conventional reconstruction and learning-based priors over the recently proposed neural radiance fields (NeRF). Unlike existing neural network based optimization method that relies on estimated correspondences, our method directly optimizes over implicit volumes, eliminating the challenging step of matching pixels in indoor scenes. The key to our approach is to utilize the learning-based priors to guide the optimization process of NeRF. Our system firstly adapts a monocular depth network over the target scene by finetuning on its sparse SfM+MVS reconstruction from COLMAP. Then, we show that the shape-radiance ambiguity of NeRF still exists in indoor environments and propose to address the issue by employing the adapted depth priors to monitor the sampling process of volume rendering. Finally, a per-pixel confidence map acquired by error computation on the rendered image can be used to further improve the depth quality. Experiments show that our proposed framework significantly outperforms state-of-the-art methods on indoor scenes, with surprising findings presented on the effectiveness of correspondence-based optimization and NeRF-based optimization over the adapted depth priors. In addition, we show that the guided optimization scheme does not sacrifice the original synthesis capability of neural radiance fields, improving the rendering quality on both seen and novel views. Code is available at https://github.com/weiyithu/NerfingMVS.

</details>

### AA-RMVSNet: Adaptive Aggregation Recurrent Multi-view Stereo Network.
- **链接**: [arXiv:2108.03824](https://arxiv.org/abs/2108.03824) · [代码](https://github.com/QT-Zhu/AA-RMVSNet) · 📚 被引 177
- **作者**: Zizhuang Wei, Qingtian Zhu, Chen Min, Yisong Chen, Guoping Wang
- **🏷️ 机构**: Peking University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present a novel recurrent multi-view stereo network based on long short-term memory (LSTM) with adaptive aggregation, namely AA-RMVSNet. We firstly introduce an intra-view aggregation module to adaptively extract image features by using context-aware convolution and multi-scale aggregation, which efficiently improves the performance on challenging regions, such as thin objects and large low-textured surfaces. To overcome the difficulty of varying occlusion in complex scenes, we propose an inter-view cost volume aggregation module for adaptive pixel-wise view aggregation, which is able to preserve better-matched pairs among all views. The two proposed adaptive aggregation modules are lightweight, effective and complementary regarding improving the accuracy and completeness of 3D reconstruction. Instead of conventional 3D CNNs, we utilize a hybrid network with recurrent structure for cost volume regularization, which allows high-resolution reconstruction and finer hypothetical plane sweep. The proposed network is trained end-to-end and achieves excellent performance on various datasets. It ranks $1^{st}$ among all submissions on Tanks and Temples benchmark and achieves competitive results on DTU dataset, which exhibits strong generalizability and robustness. Implementation of our method is available at https://github.com/QT-Zhu/AA-RMVSNet.

</details>

### Digging into Uncertainty in Self-supervised Multi-view Stereo.
- **链接**: [arXiv:2108.12966](https://arxiv.org/abs/2108.12966) · 📚 被引 62
- **作者**: Hongbin Xu, Zhipeng Zhou, Yali Wang, Wenxiong Kang, Baigui Sun, Hao Li et al.
- **🏷️ 机构**: Chinese Academy of Sciences,ShenZhen Key Lab of Computer Vision and Pattern Recognition, Shenzhen Institute of Advanced Technology, Alibaba Group, South China University of Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised Multi-view stereo (MVS) with a pretext task of image reconstruction has achieved significant progress recently. However, previous methods are built upon intuitions, lacking comprehensive explanations about the effectiveness of the pretext task in self-supervised MVS. To this end, we propose to estimate epistemic uncertainty in self-supervised MVS, accounting for what the model ignores. Specially, the limitations can be categorized into two types: ambiguious supervision in foreground and invalid supervision in background. To address these issues, we propose a novel Uncertainty reduction Multi-view Stereo (UMVS) framework for self-supervised learning. To alleviate ambiguous supervision in foreground, we involve extra correspondence prior with a flow-depth consistency loss. The dense 2D correspondence of optical flows is used to regularize the 3D stereo correspondence in MVS. To handle the invalid supervision in background, we use Monte-Carlo Dropout to acquire the uncertainty map and further filter the unreliable supervision signals on invalid regions. Extensive experiments on DTU and Tank&Temples benchmark show that our U-MVS framework achieves the best performance among unsupervised MVS methods, with competitive performance with its supervised opponents.

</details>

### Learning Signed Distance Field for Multi-view Surface Reconstruction.
- **链接**: [arXiv:2108.09964](https://arxiv.org/abs/2108.09964) · 📚 被引 101
- **作者**: Jingyang Zhang, Yao Yao, Long Quan
- **🏷️ 机构**: The Hong Kong University of Science and Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works on implicit neural representations have shown promising results for multi-view surface reconstruction. However, most approaches are limited to relatively simple geometries and usually require clean object masks for reconstructing complex and concave objects. In this work, we introduce a novel neural surface reconstruction framework that leverages the knowledge of stereo matching and feature consistency to optimize the implicit surface representation. More specifically, we apply a signed distance field (SDF) and a surface light field to represent the scene geometry and appearance respectively. The SDF is directly supervised by geometry from stereo matching, and is refined by optimizing the multi-view feature consistency and the fidelity of rendered images. Our method is able to improve the robustness of geometry estimation and support reconstruction of complex scene topologies. Extensive experiments have been conducted on DTU, EPFL and Tanks and Temples datasets. Compared to previous state-of-the-art methods, our method achieves better mesh reconstruction in wide open scenes without masks as input.

</details>

### A Confidence-based Iterative Solver of Depths and Surface Normals for Deep Multi-view Stereo.
- **链接**: [arXiv:2201.07609](https://arxiv.org/abs/2201.07609) · [代码](https://github.com/thuzhaowang/idn-solver) · 📚 被引 12
- **作者**: Wang Zhao, Shaohui Liu, Yi Wei, Hengkai Guo, Yong-Jin Liu
- **🏷️ 机构**: Tsinghua University, ETH Zurich, ByteDance Inc
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce a deep multi-view stereo (MVS) system that jointly predicts depths, surface normals and per-view confidence maps. The key to our approach is a novel solver that iteratively solves for per-view depth map and normal map by optimizing an energy potential based on the locally planar assumption. Specifically, the algorithm updates depth map by propagating from neighboring pixels with slanted planes, and updates normal map with local probabilistic plane fitting. Both two steps are monitored by a customized confidence map. This solver is not only effective as a post-processing tool for plane-based depth refinement and completion, but also differentiable such that it can be efficiently integrated into deep learning pipelines. Our multi-view stereo system employs multiple optimization steps of the solver over the initial prediction of depths and surface normals. The whole system can be trained end-to-end, decoupling the challenging problem of matching pixels within poorly textured regions from the cost-volume based neural network. Experimental results on ScanNet and RGB-D Scenes V2 demonstrate state-of-the-art performance of the proposed deep MVS system on multi-view depth estimation, with our proposed solver consistently improving the depth quality over both conventional and deep learning based MVS pipelines. Code is available at https://github.com/thuzhaowang/idn-solver.

</details>

### Revealing the Reciprocal Relations between Self-Supervised Stereo and Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01524) · 📚 被引 33
- **作者**: Zhi Chen, Xiaoqing Ye, Wei Yang, Zhenbo Xu, Xiao Tan, Zhikang Zou et al.
- **🏷️ 机构**: University of Science and Technology of China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: ICCV 2021

### Adaptive confidence thresholding for monocular depth estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01257) · 📚 被引 32
- **作者**: Hyesong Choi, Hunsang Lee, Sunkyung Kim, Sunok Kim, Seungryong Kim, Kwanghoon Sohn et al.
- **🏷️ 机构**: Ewha W. University, Yonsei University, Korea Aerospace University
- **会议**: ICCV 2021

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

> Self-supervised depth estimation for indoor environments is more challenging than its outdoor counterpart in at least the following two aspects: (i) the depth range of indoor sequences varies a lot across different frames, making it difficult for the depth network to induce consistent depth cues, whereas the maximum distance in outdoor scenes mostly stays the same as the camera usually sees the sky; (ii) the indoor sequences contain much more rotational motions, which cause difficulties for the pose network, while the motions of outdoor sequences are pre-dominantly translational, especially for driving datasets such as KITTI. In this paper, special considerations are given to those challenges and a set of good practices are consolidated for improving the performance of self-supervised monocular depth estimation in indoor environments. The proposed method mainly consists of two novel modules, \ie, a depth factorization module and a residual pose estimation module, each of which is designed to respectively tackle the aforementioned challenges. The effectiveness of each module is shown through a carefully conducted ablation study and the demonstration of the state-of-the-art performance on three indoor datasets, \ie, EuRoC, NYUv2, and 7-scenes.

</details>

### Fine-grained Semantics-aware Representation Enhancement for Self-supervised Monocular Depth Estimation.
- **链接**: [arXiv:2108.08829](https://arxiv.org/abs/2108.08829) · [代码](https://github.com/hyBlue/FSRE-Depth) · 📚 被引 119
- **作者**: Hyunyoung Jung, Eunhyeok Park, Sungjoo Yoo
- **🏷️ 机构**: Seoul National University, POSTECH
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised monocular depth estimation has been widely studied, owing to its practical importance and recent promising improvements. However, most works suffer from limited supervision of photometric consistency, especially in weak texture regions and at object boundaries. To overcome this weakness, we propose novel ideas to improve self-supervised monocular depth estimation by leveraging cross-domain information, especially scene semantics. We focus on incorporating implicit semantic knowledge into geometric representation enhancement and suggest two ideas: a metric learning approach that exploits the semantics-guided local geometry to optimize intermediate depth representations and a novel feature fusion module that judiciously utilizes cross-modality between two heterogeneous feature representations. We comprehensively evaluate our methods on the KITTI dataset and demonstrate that our method outperforms state-of-the-art methods. The source code is available at https://github.com/hyBlue/FSRE-Depth.

</details>

### Self-supervised Monocular Depth Estimation for All Day Images using Domain Separation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01250) · 📚 被引 78
- **作者**: Lina Liu, Xibin Song, Mengmeng Wang, Yong Liu, Liangjun Zhang
- **🏷️ 机构**: Zhejiang University,Institute of Cyber-Systems and Control,China, Baidu Research,China
- **会议**: ICCV 2021

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
