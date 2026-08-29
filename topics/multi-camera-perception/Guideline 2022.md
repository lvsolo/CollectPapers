# Multi-camera Perception — 2022 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 33 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multi-View Depth Estimation by Fusing Single-View Depth Probability with Multi-View Geometry.
- **链接**: [arXiv:2112.08177](https://arxiv.org/abs/2112.08177) · [代码](https://github.com/baegwangbin/MaGNet) · 📚 被引 60
- **作者**: Gwangbin Bae, Ignas Budvytis, Roberto Cipolla
- **🏷️ 机构**: University of Cambridge
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view depth estimation methods typically require the computation of a multi-view cost-volume, which leads to huge memory consumption and slow inference. Furthermore, multi-view matching can fail for texture-less surfaces, reflective surfaces and moving objects. For such failure modes, single-view depth estimation methods are often more reliable. To this end, we propose MaGNet, a novel framework for fusing single-view depth probability with multi-view geometry, to improve the accuracy, robustness and efficiency of multi-view depth estimation. For each frame, MaGNet estimates a single-view depth probability distribution, parameterized as a pixel-wise Gaussian. The distribution estimated for the reference frame is then used to sample per-pixel depth candidates. Such probabilistic sampling enables the network to achieve higher accuracy while evaluating fewer depth candidates. We also propose depth consistency weighting for the multi-view matching score, to ensure that the multi-view depth is consistent with the single-view predictions. The proposed method achieves state-of-the-art performance on ScanNet, 7-Scenes and KITTI. Qualitative evaluation demonstrates that our method is more robust against challenging artifacts such as texture-less/reflective surfaces and moving objects. Our code and model weights are available at https://github.com/baegwangbin/MaGNet.

</details>

### Deep Safe Multi-view Clustering: Reducing the Risk of Clustering Performance Degradation Caused by View Increase.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00030) · 📚 被引 90
- **作者**: Huayi Tang, Yong Liu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China
- **会议**: CVPR 2022

### Multi-level Feature Learning for Contrastive Multi-view Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01558)
- **作者**: Jie Xu, Huayi Tang, Yazhou Ren, Liang Peng, Xiaofeng Zhu, Lifang He
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Towards Discriminative Representation: Multi-view Trajectory Contrastive Learning for Online Multi-object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00863)
- **作者**: En Yu, Zhuoling Li, Shoudong Han
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### TransMVSNet: Global Context-aware Multi-view Stereo Network with Transformers.
- **链接**: [arXiv:2111.14600](https://arxiv.org/abs/2111.14600) · [代码](https://github.com/MegviiRobot/TransMVSNet) · 📚 被引 249
- **作者**: Yikang Ding, Wentao Yuan, Qingtian Zhu, Haotian Zhang, Xiangyue Liu, Yuanjiang Wang et al.
- **🏷️ 机构**: Megvii Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present TransMVSNet, based on our exploration of feature matching in multi-view stereo (MVS). We analogize MVS back to its nature of a feature matching task and therefore propose a powerful Feature Matching Transformer (FMT) to leverage intra- (self-) and inter- (cross-) attention to aggregate long-range context information within and across images. To facilitate a better adaptation of the FMT, we leverage an Adaptive Receptive Field (ARF) module to ensure a smooth transit in scopes of features and bridge different stages with a feature pathway to pass transformed features and gradients across different scales. In addition, we apply pair-wise feature correlation to measure similarity between features, and adopt ambiguity-reducing focal loss to strengthen the supervision. To the best of our knowledge, TransMVSNet is the first attempt to leverage Transformer into the task of MVS. As a result, our method achieves state-of-the-art performance on DTU dataset, Tanks and Temples benchmark, and BlendedMVS dataset. The code of our method will be made available at https://github.com/MegviiRobot/TransMVSNet .

</details>

### Weakly-Supervised Online Action Segmentation in Multi-View Instructional Videos.
- **链接**: [arXiv:2203.13309](https://arxiv.org/abs/2203.13309) · 📚 被引 25
- **作者**: Reza Ghoddoosian, Isht Dwivedi, Nakul Agarwal, Chiho Choi, Behzad Dariush
- **🏷️ 机构**: Honda Research Institute,USA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses a new problem of weakly-supervised online action segmentation in instructional videos. We present a framework to segment streaming videos online at test time using Dynamic Programming and show its advantages over greedy sliding window approach. We improve our framework by introducing the Online-Offline Discrepancy Loss (OODL) to encourage the segmentation results to have a higher temporal consistency. Furthermore, only during training, we exploit frame-wise correspondence between multiple views as supervision for training weakly-labeled instructional videos. In particular, we investigate three different multi-view inference techniques to generate more accurate frame-wise pseudo ground-truth with no additional annotation cost. We present results and ablation studies on two benchmark multi-view datasets, Breakfast and IKEA ASM. Experimental results show efficacy of the proposed methods both qualitatively and quantitatively in two domains of cooking and assembly.

</details>

### Multi-View Transformer for 3D Visual Grounding.
- **链接**: [arXiv:2204.02174](https://arxiv.org/abs/2204.02174) · [代码](https://github.com/sega-hsj/MVT-3DVG) · 📚 被引 112
- **作者**: Shijia Huang, Yilun Chen, Jiaya Jia, Liwei Wang
- **🏷️ 机构**: The Chinese University of Hong Kong
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The 3D visual grounding task aims to ground a natural language description to the targeted object in a 3D scene, which is usually represented in 3D point clouds. Previous works studied visual grounding under specific views. The vision-language correspondence learned by this way can easily fail once the view changes. In this paper, we propose a Multi-View Transformer (MVT) for 3D visual grounding. We project the 3D scene to a multi-view space, in which the position information of the 3D scene under different views are modeled simultaneously and aggregated together. The multi-view space enables the network to learn a more robust multi-modal representation for 3D visual grounding and eliminates the dependence on specific views. Extensive experiments show that our approach significantly outperforms all state-of-the-art methods. Specifically, on Nr3D and Sr3D datasets, our method outperforms the best competitor by 11.2% and 7.1% and even surpasses recent work with extra 2D assistance by 5.9% and 6.6%. Our code is available at https://github.com/sega-hsj/MVT-3DVG.

</details>

### Uncertainty-Aware Deep Multi-View Photometric Stereo.
- **链接**: [arXiv:2202.13071](https://arxiv.org/abs/2202.13071) · 📚 被引 36
- **作者**: Berk Kaya, Suryansh Kumar, Carlos Eduardo Porto de Oliveira, Vittorio Ferrari, Luc Van Gool
- **🏷️ 机构**: ETH Z&#x00FC;rich, Google Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a simple and effective solution to the longstanding classical multi-view photometric stereo (MVPS) problem. It is well-known that photometric stereo (PS) is excellent at recovering high-frequency surface details, whereas multi-view stereo (MVS) can help remove the low-frequency distortion due to PS and retain the global geometry of the shape. This paper proposes an approach that can effectively utilize such complementary strengths of PS and MVS. Our key idea is to combine them suitably while considering the per-pixel uncertainty of their estimates. To this end, we estimate per-pixel surface normals and depth using an uncertainty-aware deep-PS network and deep-MVS network, respectively. Uncertainty modeling helps select reliable surface normal and depth estimates at each pixel which then act as a true representative of the dense surface geometry. At each pixel, our approach either selects or discards deep-PS and deep-MVS network prediction depending on the prediction uncertainty measure. For dense, detailed, and precise inference of the object's surface profile, we propose to learn the implicit neural shape representation via a multilayer perceptron (MLP). Our approach encourages the MLP to converge to a natural zero-level set surface using the confident prediction from deep-PS and deep-MVS networks, providing superior dense surface reconstruction. Extensive experiments on the DiLiGenT-MV benchmark dataset show that our method provides high-quality shape recovery with a much lower memory footprint while outperforming almost all of the existing approaches.

</details>

### Neural 3D Video Synthesis from Multi-view Video.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00544) · 📚 被引 396
- **作者**: Tianye Li, Mira Slavcheva, Michael Zollhöfer, Simon Green, Christoph Lassner, Changil Kim et al.
- **🏷️ 机构**: University of Southern,California, Reality Labs Research, Meta
- **会议**: CVPR 2022

### PlaneMVS: 3D Plane Reconstruction from Multi-View Stereo.
- **链接**: [arXiv:2203.12082](https://arxiv.org/abs/2203.12082) · [代码](https://github.com/oppo-us-research/PlaneMVS) · 📚 被引 47
- **作者**: Jiachen Liu, Pan Ji, Nitin Bansal, Changjiang Cai, Qingan Yan, Xiaolei Huang et al.
- **🏷️ 机构**: The Pennsylvania State University, InnoPeak Technology, Inc.,OPPO US Research Center
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel framework named PlaneMVS for 3D plane reconstruction from multiple input views with known camera poses. Most previous learning-based plane reconstruction methods reconstruct 3D planes from single images, which highly rely on single-view regression and suffer from depth scale ambiguity. In contrast, we reconstruct 3D planes with a multi-view-stereo (MVS) pipeline that takes advantage of multi-view geometry. We decouple plane reconstruction into a semantic plane detection branch and a plane MVS branch. The semantic plane detection branch is based on a single-view plane detection framework but with differences. The plane MVS branch adopts a set of slanted plane hypotheses to replace conventional depth hypotheses to perform plane sweeping strategy and finally learns pixel-level plane parameters and its planar depth map. We present how the two branches are learned in a balanced way, and propose a soft-pooling loss to associate the outputs of the two branches and make them benefit from each other. Extensive experiments on various indoor datasets show that PlaneMVS significantly outperforms state-of-the-art (SOTA) single-view plane reconstruction methods on both plane detection and 3D geometry metrics. Our method even outperforms a set of SOTA learning-based MVS methods thanks to the learned plane priors. To the best of our knowledge, this is the first work on 3D plane reconstruction within an end-to-end MVS framework. Source code: https://github.com/oppo-us-research/PlaneMVS.

</details>

### MPC: Multi-view Probabilistic Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00929) · 📚 被引 10
- **作者**: Junjie Liu, Junlong Liu, Shaotian Yan, Rongxin Jiang, Xiang Tian, Boxuan Gu et al.
- **🏷️ 机构**: Zhejiang University, Alibaba Cloud Computing Ltd.
- **会议**: CVPR 2022

### Generalized Binary Search Network for Highly-Efficient Multi-View Stereo.
- **链接**: [arXiv:2112.02338](https://arxiv.org/abs/2112.02338) · [代码](https://github.com/MiZhenxing/GBi-Net) · 📚 被引 86
- **作者**: Zhenxing Mi, Di Chang, Dan Xu
- **🏷️ 机构**: The Hong Kong University of Science and Technology
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view Stereo (MVS) with known camera parameters is essentially a 1D search problem within a valid depth range. Recent deep learning-based MVS methods typically densely sample depth hypotheses in the depth range, and then construct prohibitively memory-consuming 3D cost volumes for depth prediction. Although coarse-to-fine sampling strategies alleviate this overhead issue to a certain extent, the efficiency of MVS is still an open challenge. In this work, we propose a novel method for highly efficient MVS that remarkably decreases the memory footprint, meanwhile clearly advancing state-of-the-art depth prediction performance. We investigate what a search strategy can be reasonably optimal for MVS taking into account of both efficiency and effectiveness. We first formulate MVS as a binary search problem, and accordingly propose a generalized binary search network for MVS. Specifically, in each step, the depth range is split into 2 bins with extra 1 error tolerance bin on both sides. A classification is performed to identify which bin contains the true depth. We also design three mechanisms to respectively handle classification errors, deal with out-of-range samples and decrease the training memory. The new formulation makes our method only sample a very small number of depth hypotheses in each step, which is highly memory efficient, and also greatly facilitates quick training convergence. Experiments on competitive benchmarks show that our method achieves state-of-the-art accuracy with much less memory. Particularly, our method obtains an overall score of 0.289 on DTU dataset and tops the first place on challenging Tanks and Temples advanced dataset among all the learning-based methods. The trained models and code will be released at https://github.com/MiZhenxing/GBi-Net.

</details>

### Rethinking Depth Estimation for Multi-View Stereo: A Unified Representation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00845) · 📚 被引 155
- **作者**: Rui Peng, Rongjie Wang, Zhenyu Wang, Yawen Lai, Ronggang Wang
- **🏷️ 机构**: School of Electronic and Computer Engineering, Peking University, Peng Cheng Laboratory
- **会议**: CVPR 2022

### Mining Multi-View Information: A Strong Self-Supervised Framework for Depth-based 3D Hand Pose and Mesh Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01990) · 📚 被引 26
- **作者**: Pengfei Ren, Haifeng Sun, Jiachang Hao, Jingyu Wang, Qi Qi, Jianxin Liao
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,State Key Laboratory of Networking and Switching Technology
- **会议**: CVPR 2022

### Learning Multi-View Aggregation In the Wild for Large-Scale 3D Semantic Segmentation.
- **链接**: [arXiv:2204.07548](https://arxiv.org/abs/2204.07548) · [代码](https://github.com/drprojects/DeepViewAgg) · 📚 被引 83
- **作者**: Damien Robert, Bruno Vallet, Loïc Landrieu
- **🏷️ 机构**: CSAI, ENGIE Lab CRIGEN,Stains,France, Univ Gustave Eiffel, ENSG, IGN, LASTIG,Marne-la-Vallee,France,F-77454
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works on 3D semantic segmentation propose to exploit the synergy between images and point clouds by processing each modality with a dedicated network and projecting learned 2D features onto 3D points. Merging large-scale point clouds and images raises several challenges, such as constructing a mapping between points and pixels, and aggregating features between multiple views. Current methods require mesh reconstruction or specialized sensors to recover occlusions, and use heuristics to select and aggregate available images. In contrast, we propose an end-to-end trainable multi-view aggregation model leveraging the viewing conditions of 3D points to merge features from images taken at arbitrary positions. Our method can combine standard 2D and 3D networks and outperforms both 3D models operating on colorized point clouds and hybrid 2D/3D networks without requiring colorization, meshing, or true depth maps. We set a new state-of-the-art for large-scale indoor/outdoor semantic segmentation on S3DIS (74.7 mIoU 6-Fold) and on KITTI-360 (58.3 mIoU). Our full pipeline is accessible at https://github.com/drprojects/DeepViewAgg, and only requires raw 3D scans and a set of images and poses.

</details>

### Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities.
- **链接**: [arXiv:2203.14712](https://arxiv.org/abs/2203.14712) · 📚 被引 201
- **作者**: Fadime Sener, Dibyadip Chatterjee, Daniel Shelepov, Kun He, Dipika Singhania, Robert Wang et al.
- **🏷️ 机构**: Meta Reality Labs Research, National University of Singapore
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Assembly101 is a new procedural activity dataset featuring 4321 videos of people assembling and disassembling 101 "take-apart" toy vehicles. Participants work without fixed instructions, and the sequences feature rich and natural variations in action ordering, mistakes, and corrections. Assembly101 is the first multi-view action dataset, with simultaneous static (8) and egocentric (4) recordings. Sequences are annotated with more than 100K coarse and 1M fine-grained action segments, and 18M 3D hand poses. We benchmark on three action understanding tasks: recognition, anticipation and temporal segmentation. Additionally, we propose a novel task of detecting mistakes. The unique recording format and rich set of annotations allow us to investigate generalization to new toys, cross-view transfer, long-tailed distributions, and pose vs. appearance. We envision that Assembly101 will serve as a new challenge to investigate various activity understanding problems.

</details>

### Efficient Multi-view Stereo by Iterative Dynamic Cost Volume.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00846) · 📚 被引 66
- **作者**: Shaoqian Wang, Bo Li, Yuchao Dai
- **🏷️ 机构**: School of Electronics and Information, Northwestern Polytechnical University,Xi&#x0027;an,China
- **会议**: CVPR 2022

### IterMVS: Iterative Probability Estimation for Efficient Multi-View Stereo.
- **链接**: [arXiv:2112.05126](https://arxiv.org/abs/2112.05126) · [代码](https://github.com/FangjinhuaWang/IterMVS) · 📚 被引 137
- **作者**: Fangjinhua Wang, Silvano Galliani, Christoph Vogel, Marc Pollefeys
- **🏷️ 机构**: ETH Zurich,Department of Computer Science, Microsoft Mixed Reality &#x0026; AI Zurich Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present IterMVS, a new data-driven method for high-resolution multi-view stereo. We propose a novel GRU-based estimator that encodes pixel-wise probability distributions of depth in its hidden state. Ingesting multi-scale matching information, our model refines these distributions over multiple iterations and infers depth and confidence. To extract the depth maps, we combine traditional classification and regression in a novel manner. We verify the efficiency and effectiveness of our method on DTU, Tanks&Temples and ETH3D. While being the most efficient method in both memory and run-time, our model achieves competitive performance on DTU and better generalization ability on Tanks&Temples as well as ETH3D than most state-of-the-art methods. Code is available at https://github.com/FangjinhuaWang/IterMVS.

</details>

### Multi-View Mesh Reconstruction with Neural Deferred Shading.
- **链接**: [arXiv:2212.04386](https://arxiv.org/abs/2212.04386) · 📚 被引 46
- **作者**: Markus Worchel, Rodrigo Diaz, Weiwen Hu, Oliver Schreer, Ingo Feldmann, Peter Eisert
- **🏷️ 机构**: Fraunhofer HHI
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an analysis-by-synthesis method for fast multi-view 3D reconstruction of opaque objects with arbitrary materials and illumination. State-of-the-art methods use both neural surface representations and neural rendering. While flexible, neural surface representations are a significant bottleneck in optimization runtime. Instead, we represent surfaces as triangle meshes and build a differentiable rendering pipeline around triangle rasterization and neural shading. The renderer is used in a gradient descent optimization where both a triangle mesh and a neural shader are jointly optimized to reproduce the multi-view images. We evaluate our method on a public 3D reconstruction dataset and show that it can match the reconstruction accuracy of traditional baselines and neural approaches while surpassing them in optimization runtime. Additionally, we investigate the shader and find that it learns an interpretable representation of appearance, enabling applications such as 3D material editing.

</details>

### RayMVSNet: Learning Ray-based 1D Implicit Fields for Accurate Multi-View Stereo.
- **链接**: [arXiv:2204.01320](https://arxiv.org/abs/2204.01320) · 📚 被引 40
- **作者**: Junhua Xi, Yifei Shi, Yijie Wang, Yulan Guo, Kai Xu
- **🏷️ 机构**: National University of Defense Technology
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning-based multi-view stereo (MVS) has by far centered around 3D convolution on cost volumes. Due to the high computation and memory consumption of 3D CNN, the resolution of output depth is often considerably limited. Different from most existing works dedicated to adaptive refinement of cost volumes, we opt to directly optimize the depth value along each camera ray, mimicking the range (depth) finding of a laser scanner. This reduces the MVS problem to ray-based depth optimization which is much more light-weight than full cost volume optimization. In particular, we propose RayMVSNet which learns sequential prediction of a 1D implicit field along each camera ray with the zero-crossing point indicating scene depth. This sequential modeling, conducted based on transformer features, essentially learns the epipolar line search in traditional multi-view stereo. We also devise a multi-task learning for better optimization convergence and depth accuracy. Our method ranks top on both the DTU and the Tanks \& Temples datasets over all previous learning-based methods, achieving overall reconstruction score of 0.33mm on DTU and f-score of 59.48% on Tanks & Temples.

</details>

### Self-supervised Spatial Reasoning on Multi-View Line Drawings.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01241) · 📚 被引 1
- **作者**: Siyuan Xiang, Anbang Yang, Yanfei Xue, Yaoqing Yang, Chen Feng
- **🏷️ 机构**: New York University Tandon School of Engineering, University of California,Berkeley
- **会议**: CVPR 2022

### Non-parametric Depth Distribution Modelling based Depth Inference for Multi-view Stereo.
- **链接**: [arXiv:2205.03783](https://arxiv.org/abs/2205.03783) · [代码](https://github.com/NVlabs/NP-CVP-MVSNet) · 📚 被引 37
- **作者**: Jiayu Yang, José M. Álvarez, Miaomiao Liu
- **🏷️ 机构**: Australian National University, NVIDIA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent cost volume pyramid based deep neural networks have unlocked the potential of efficiently leveraging high-resolution images for depth inference from multi-view stereo. In general, those approaches assume that the depth of each pixel follows a unimodal distribution. Boundary pixels usually follow a multi-modal distribution as they represent different depths; Therefore, the assumption results in an erroneous depth prediction at the coarser level of the cost volume pyramid and can not be corrected in the refinement levels leading to wrong depth predictions. In contrast, we propose constructing the cost volume by non-parametric depth distribution modeling to handle pixels with unimodal and multi-modal distributions. Our approach outputs multiple depth hypotheses at the coarser level to avoid errors in the early stage. As we perform local search around these multiple hypotheses in subsequent levels, our approach does not maintain the rigid depth spatial ordering and, therefore, we introduce a sparse cost aggregation network to derive information within each volume. We evaluate our approach extensively on two benchmark datasets: DTU and Tanks & Temples. Our experimental results show that our model outperforms existing methods by a large margin and achieves superior performance on boundary regions. Code is available at https://github.com/NVlabs/NP-CVP-MVSNet

</details>

### Multi-View Consistent Generative Adversarial Networks for 3D-aware Image Synthesis.
- **链接**: [arXiv:2204.06307](https://arxiv.org/abs/2204.06307) · 📚 被引 40
- **作者**: Xuanmeng Zhang, Zhedong Zheng, Daiheng Gao, Bang Zhang, Pan Pan, Yi Yang
- **🏷️ 机构**: University of Technology,ReLER, AAII,Sydney, DAMO Academy, Alibaba Group, Zhejiang University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D-aware image synthesis aims to generate images of objects from multiple views by learning a 3D representation. However, one key challenge remains: existing approaches lack geometry constraints, hence usually fail to generate multi-view consistent images. To address this challenge, we propose Multi-View Consistent Generative Adversarial Networks (MVCGAN) for high-quality 3D-aware image synthesis with geometry constraints. By leveraging the underlying 3D geometry information of generated images, i.e., depth and camera transformation matrix, we explicitly establish stereo correspondence between views to perform multi-view joint optimization. In particular, we enforce the photometric consistency between pairs of views and integrate a stereo mixup mechanism into the training process, encouraging the model to reason about the correct 3D shape. Besides, we design a two-stage training strategy with feature-level multi-view joint optimization to improve the image quality. Extensive experiments on three datasets demonstrate that MVCGAN achieves the state-of-the-art performance for 3D-aware image synthesis.

</details>

### LMGP: Lifted Multicut Meets Geometry Projections for Multi-Camera Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00866)
- **作者**: Duy M. H. Nguyen, Roberto Henschel, Bodo Rosenhahn, Daniel Sonntag, Paul Swoboda
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Reference-based Video Super-Resolution Using Multi-Camera Video Triplets.
- **链接**: [arXiv:2203.14537](https://arxiv.org/abs/2203.14537) · 📚 被引 35
- **作者**: Junyong Lee, Myeonghee Lee, Sunghyun Cho, Seungyong Lee
- **🏷️ 机构**: POSTECH
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose the first reference-based video super-resolution (RefVSR) approach that utilizes reference videos for high-fidelity results. We focus on RefVSR in a triple-camera setting, where we aim at super-resolving a low-resolution ultra-wide video utilizing wide-angle and telephoto videos. We introduce the first RefVSR network that recurrently aligns and propagates temporal reference features fused with features extracted from low-resolution frames. To facilitate the fusion and propagation of temporal reference features, we propose a propagative temporal fusion module. For learning and evaluation of our network, we present the first RefVSR dataset consisting of triplets of ultra-wide, wide-angle, and telephoto videos concurrently taken from triple cameras of a smartphone. We also propose a two-stage training strategy fully utilizing video triplets in the proposed dataset for real-world 4x video super-resolution. We extensively evaluate our method, and the result shows the state-of-the-art performance in 4x super-resolution.

</details>

### OmniFusion: 360 Monocular Depth Estimation via Geometry-Aware Fusion.
- **链接**: [arXiv:2203.00838](https://arxiv.org/abs/2203.00838) · 📚 被引 87
- **作者**: Yuyan Li, Yuliang Guo, Zhixin Yan, Xinyu Huang, Ye Duan, Liu Ren
- **🏷️ 机构**: University of Missouri, Bosch Research North America
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A well-known challenge in applying deep-learning methods to omnidirectional images is spherical distortion. In dense regression tasks such as depth estimation, where structural details are required, using a vanilla CNN layer on the distorted 360 image results in undesired information loss. In this paper, we propose a 360 monocular depth estimation pipeline, OmniFusion, to tackle the spherical distortion issue. Our pipeline transforms a 360 image into less-distorted perspective patches (i.e. tangent images) to obtain patch-wise predictions via CNN, and then merge the patch-wise results for final output. To handle the discrepancy between patch-wise predictions which is a major issue affecting the merging quality, we propose a new framework with the following key components. First, we propose a geometry-aware feature fusion mechanism that combines 3D geometric features with 2D image features to compensate for the patch-wise discrepancy. Second, we employ the self-attention-based transformer architecture to conduct a global aggregation of patch-wise information, which further improves the consistency. Last, we introduce an iterative depth refinement mechanism, to further refine the estimated depth based on the more accurate geometric features. Experiments show that our method greatly mitigates the distortion issue, and achieves state-of-the-art performances on several 360 monocular depth estimation benchmark datasets.

</details>

### P3Depth: Monocular Depth Estimation with a Piecewise Planarity Prior.
- **链接**: [arXiv:2204.02091](https://arxiv.org/abs/2204.02091) · [代码](https://github.com/SysCV/P3Depth) · 📚 被引 153
- **作者**: Vaishakh Patil, Christos Sakaridis, Alexander Liniger, Luc Van Gool
- **🏷️ 机构**: ETH Z&#x00FC;rich,Computer Vision Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation is vital for scene understanding and downstream tasks. We focus on the supervised setup, in which ground-truth depth is available only at training time. Based on knowledge about the high regularity of real 3D scenes, we propose a method that learns to selectively leverage information from coplanar pixels to improve the predicted depth. In particular, we introduce a piecewise planarity prior which states that for each pixel, there is a seed pixel which shares the same planar 3D surface with the former. Motivated by this prior, we design a network with two heads. The first head outputs pixel-level plane coefficients, while the second one outputs a dense offset vector field that identifies the positions of seed pixels. The plane coefficients of seed pixels are then used to predict depth at each position. The resulting prediction is adaptively fused with the initial prediction from the first head via a learned confidence to account for potential deviations from precise local planarity. The entire architecture is trained end-to-end thanks to the differentiability of the proposed modules and it learns to predict regular depth maps, with sharp edges at occlusion boundaries. An extensive evaluation of our method shows that we set the new state of the art in supervised monocular depth estimation, surpassing prior methods on NYU Depth-v2 and on the Garg split of KITTI. Our method delivers depth maps that yield plausible 3D reconstructions of the input scenes. Code is available at: https://github.com/SysCV/P3Depth

</details>

### Exploiting Pseudo Labels in a Self-Supervised Learning Framework for Improved Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00163) · 📚 被引 57
- **作者**: Andra Petrovai, Sergiu Nedevschi
- **🏷️ 机构**: Technical University of Cluj-Napoca,Romania
- **会议**: CVPR 2022

### 360MonoDepth: High-Resolution 360° Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00374) · 📚 被引 83
- **作者**: Manuel Rey-Area, Mingze Yuan, Christian Richardt
- **🏷️ 机构**: University of Bath
- **会议**: CVPR 2022

### CroMo: Cross-Modal Learning for Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00391) · 📚 被引 16
- **作者**: Yannick Verdié, Jifei Song, Barnabé Mas, Benjamin Busam, Ales Leonardis, Steven McDonagh
- **🏷️ 机构**: Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022

### Neural Window Fully-connected CRFs for Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00389) · 📚 被引 368
- **作者**: Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, Ping Tan
- **🏷️ 机构**: Alibaba Group
- **会议**: CVPR 2022

### Multi-Frame Self-Supervised Depth with Transformers.
- **链接**: [arXiv:2204.07616](https://arxiv.org/abs/2204.07616) · 📚 被引 97
- **作者**: Vitor Guizilini, Rares Ambrus, Dian Chen, Sergey Zakharov, Adrien Gaidon
- **🏷️ 机构**: Toyota Research Institute (TRI),Los Altos,CA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-frame depth estimation improves over single-frame approaches by also leveraging geometric relationships between images via feature matching, in addition to learning appearance-based features. In this paper we revisit feature matching for self-supervised monocular depth estimation, and propose a novel transformer architecture for cost volume generation. We use depth-discretized epipolar sampling to select matching candidates, and refine predictions through a series of self- and cross-attention layers. These layers sharpen the matching probability between pixel features, improving over standard similarity metrics prone to ambiguities and local minima. The refined cost volume is decoded into depth estimates, and the whole pipeline is trained end-to-end from videos using only a photometric objective. Experiments on the KITTI and DDAD datasets show that our DepthFormer architecture establishes a new state of the art in self-supervised monocular depth estimation, and is even competitive with highly specialized supervised single-frame architectures. We also show that our learned cross-attention network yields representations transferable across datasets, increasing the effectiveness of pre-training strategies. Project page: https://sites.google.com/tri.global/depthformer

</details>

## 跨领域论文（完整笔记在其他领域）

- A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation. → [3d-detection](../3d-detection/Guideline%202022.md)
