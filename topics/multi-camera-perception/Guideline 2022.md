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

### Towards Comprehensive Representation Enhancement in Semantics-Guided Self-supervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_18) · 📚 被引 21
- **作者**: Jingyuan Ma, Xiangyu Lei, Nan Liu, Xian Zhao, Shiliang Pu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Adaptive Co-teaching for Unsupervised Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19769-7_6)
- **作者**: Weisong Ren, Lijun Wang, Yongri Piao, Miao Zhang, Huchuan Lu, Ting Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Spike Transformer: Monocular Depth Estimation for Spiking Camera.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20071-7_3) · 📚 被引 28
- **作者**: Jiyuan Zhang, Lulu Tang, Zhaofei Yu, Jiwen Lu, Tie-Jun Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Towards Scale-Aware, Robust, and Generalizable Unsupervised Monocular Depth Estimation by Integrating IMU Motion Dynamics.
- **链接**: [arXiv:2207.04680](https://arxiv.org/abs/2207.04680) · 📚 被引 38
- **作者**: Sen Zhang, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised monocular depth and ego-motion estimation has drawn extensive research attention in recent years. Although current methods have reached a high up-to-scale accuracy, they usually fail to learn the true scale metric due to the inherent scale ambiguity from training with monocular sequences. In this work, we tackle this problem and propose DynaDepth, a novel scale-aware framework that integrates information from vision and IMU motion dynamics. Specifically, we first propose an IMU photometric loss and a cross-sensor photometric consistency loss to provide dense supervision and absolute scales. To fully exploit the complementary information from both sensors, we further drive a differentiable camera-centric extended Kalman filter (EKF) to update the IMU preintegrated motions when observing visual measurements. In addition, the EKF formulation enables learning an ego-motion uncertainty measure, which is non-trivial for unsupervised methods. By leveraging IMU during training, DynaDepth not only learns an absolute scale, but also provides a better generalization ability and robustness against vision degradation such as illumination change and moving objects. We validate the effectiveness of DynaDepth by conducting extensive experiments and simulations on the KITTI and Make3D datasets.

</details>

### Self-distilled Feature Aggregation for Self-supervised Monocular Depth Estimation.
- **链接**: [arXiv:2209.07088](https://arxiv.org/abs/2209.07088) · [代码](https://github.com/ZM-Zhou/SDFA-Net_pytorch)
- **作者**: Zhengming Zhou, Qiulei Dong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised monocular depth estimation has received much attention recently in computer vision. Most of the existing works in literature aggregate multi-scale features for depth prediction via either straightforward concatenation or element-wise addition, however, such feature aggregation operations generally neglect the contextual consistency between multi-scale features. Addressing this problem, we propose the Self-Distilled Feature Aggregation (SDFA) module for simultaneously aggregating a pair of low-scale and high-scale features and maintaining their contextual consistency. The SDFA employs three branches to learn three feature offset maps respectively: one offset map for refining the input low-scale feature and the other two for refining the input high-scale feature under a designed self-distillation manner. Then, we propose an SDFA-based network for self-supervised monocular depth estimation, and design a self-distilled training strategy to train the proposed network with the SDFA module. Experimental results on the KITTI dataset demonstrate that the proposed method outperforms the comparative state-of-the-art methods in most cases. The code is available at https://github.com/ZM-Zhou/SDFA-Net_pytorch.

</details>

### KD-MVS: Knowledge Distillation Based Self-supervised Learning for Multi-view Stereo.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_36) · 📚 被引 31
- **作者**: Yikang Ding, Qingtian Zhu, Xiangyue Liu, Wentao Yuan, Haotian Zhang, Chi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Emotion-aware Multi-view Contrastive Learning for Facial Emotion Recognition.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19778-9_11) · 📚 被引 16
- **作者**: Dae Ha Kim, Byung Cheol Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

## 跨领域论文（完整笔记在其他领域）

- A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation. → [3d-detection](../3d-detection/Guideline%202022.md)

## 🆕 增量新增

### SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19842-7_14) · 📚 被引 24
- **作者**: Simon Doll, Richard Schulz, Lukas Schneider, Viviane Benzin, Markus Enzweiler, Hendrik P. A. Lensch
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角相机3D目标检测中，现有方法难以有效利用全局跨传感器信息，导致检测精度和鲁棒性不足的问题。②提出了SpatialDETR，一种基于Transformer的架构，通过全局跨传感器注意力机制，将多视角图像特征与3D空间位置信息融合，实现端到端的3D目标检测。③相比现有方法，引入了可扩展的注意力设计，能够处理任意数量的相机视角，并增强了对不同传感器配置的适应性。④在nuScenes等基准上取得了显著的性能提升，展示了良好的鲁棒性和可扩展性。
- **摘要（英）**: This paper addresses the challenge of effectively leveraging global cross-sensor information in multi-view camera-based 3D object detection. It proposes SpatialDETR, a scalable Transformer-based architecture with global cross-sensor attention, enabling end-to-end detection. The method improves robustness and scalability over existing approaches, achieving significant performance gains on benchmarks like nuScenes.
- **核心贡献**: 提出了一种可扩展的基于Transformer的多视角3D检测框架，引入全局跨传感器注意力。
- **创新点**: 全局跨传感器注意力机制，支持任意数量相机视角的灵活融合。
- **结果**: 在nuScenes基准上显著提升了检测精度和鲁棒性。

### PseCo: Pseudo Labeling and Consistency Training for Semi-Supervised Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.16317](https://arxiv.org/abs/2203.16317)
- **作者**: Gang Li, Xiang Li, Yujie Wang, Yichao Wu, Ding Liang, Shanshan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对半监督目标检测中伪标签定位精度不足和一致性训练仅关注标签级而忽略特征级一致性的问题。②提出了PseCo框架，包含Noisy Pseudo box Learning (NPL)和Multi-view Scale-invariant Learning (MSL)两个模块，NPL通过Prediction-guided Label Assignment和Positive-proposal Consistency Voting处理噪声伪框，MSL引入多视图尺度不变学习。③相比现有方法，同时优化了伪标签的定位质量和特征级一致性，更贴合目标检测的特性。④在COCO等标准基准上显著提升了半监督检测性能，尤其在低标注比例下表现突出。
- **摘要（英）**: This paper addresses the issues of imprecise pseudo boxes and insufficient feature-level consistency in semi-supervised object detection. It proposes PseCo with NPL and MSL modules to improve localization quality and scale invariance. The method achieves significant performance gains on COCO benchmarks, especially under low annotation ratios.
- **核心贡献**: 提出了PseCo框架，通过NPL和MSL分别解决伪标签定位噪声和特征级一致性问题。
- **创新点**: 创新性地将预测引导的标签分配和正提议一致性投票用于伪标签质量提升，并引入多视图尺度不变学习。
- **结果**: 在COCO基准上显著提升半监督检测精度，低标注比例下性能提升尤为明显。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we delve into two key techniques in Semi-Supervised Object Detection (SSOD), namely pseudo labeling and consistency training. We observe that these two techniques currently neglect some important properties of object detection, hindering efficient learning on unlabeled data. Specifically, for pseudo labeling, existing works only focus on the classification score yet fail to guarantee the localization precision of pseudo boxes; For consistency training, the widely adopted random-resize training only considers the label-level consistency but misses the feature-level one, which also plays an important role in ensuring the scale invariance. To address the problems incurred by noisy pseudo boxes, we design Noisy Pseudo box Learning (NPL) that includes Prediction-guided Label Assignment (PLA) and Positive-proposal Consistency Voting (PCV). PLA relies on model predictions to assign labels and makes it robust to even coarse pseudo boxes; while PCV leverages the regression consistency of positive proposals to reflect the localization quality of pseudo boxes. Furthermore, in consistency training, we propose Multi-view Scale-invariant Learning (MSL) that includes mechanisms of both label- and feature-level consistency, where feature consistency is achieved by aligning shifted feature pyramids between two images with identical content but varied scales. On COCO benchmark, our method, termed PSEudo labeling and COnsistency training (PseCo), outperforms the SOTA (Soft Teacher) by 2.0, 1.8, 2.0 points under 1%, 5%, and 10% labelling ratios, respectively. It also significantly improves the learning efficiency for SSOD, e.g., PseCo halves the training time of the SOTA approach but achieves even better performance. Code is available at https://github.com/ligang-cs/PseCo.

</details>

### Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_41)
- **作者**: Qing Lian, Yanbo Xu, Weilong Yao, Yingcong Chen, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对单目3D目标检测中标注数据稀缺的问题，本文提出基于多视图一致性的半监督方法。方法利用多视图几何一致性生成伪标签，并设计一致性损失进行训练。实验表明该方法能有效利用未标注数据提升检测性能。
- **摘要（英）**: This paper proposes a semi-supervised monocular 3D detection method using multi-view consistency, which generates pseudo-labels via geometric consistency and trains with consistency losses. Experiments show improved performance by leveraging unlabeled data.
- **核心贡献**: 提出多视图一致性驱动的半监督单目3D检测框架。
- **创新点**: 利用多视图几何一致性生成高质量伪标签。
- **结果**: 有效利用未标注数据提升检测性能。

### PETR: Position Embedding Transformation for Multi-view 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2203.05625](https://arxiv.org/abs/2203.05625)
- **作者**: Yingfei Liu, Tiancai Wang, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2022
- **摘要（中）**: 针对多视图3D检测中如何有效利用3D位置信息的问题，该论文提出PETR，通过位置嵌入变换将3D坐标编码到图像特征中，生成3D位置感知特征，并利用对象查询进行端到端检测。相比基于投影或体素的方法，PETR简化了流程并提升了性能。在nuScenes上达到50.4% NDS和44.1% mAP，排名第一，成为强基线。
- **摘要（英）**: This paper introduces PETR for multi-view 3D detection by encoding 3D coordinates into image features via position embedding transformation, enabling end-to-end detection with object queries. It achieves state-of-the-art 50.4% NDS and 44.1% mAP on nuScenes, ranking first and serving as a strong baseline.
- **核心贡献**: 提出位置嵌入变换机制，统一多视图特征与查询交互。
- **创新点**: 将3D位置信息直接嵌入图像特征，避免复杂投影。
- **结果**: 在nuScenes上取得SOTA性能并排名第一。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we develop position embedding transformation (PETR) for multi-view 3D object detection. PETR encodes the position information of 3D coordinates into image features, producing the 3D position-aware features. Object query can perceive the 3D position-aware features and perform end-to-end object detection. PETR achieves state-of-the-art performance (50.4% NDS and 44.1% mAP) on standard nuScenes dataset and ranks 1st place on the benchmark. It can serve as a simple yet strong baseline for future research. Code is available at \url{https://github.com/megvii-research/PETR}.

</details>

### MVSalNet: Multi-view Augmentation for RGB-D Salient Object Detection. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19818-2_16) · 📚 被引 29
- **作者**: Jiayuan Zhou, Lijun Wang, Huchuan Lu, Kaining Huang, Xinchu Shi, Bocong Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对RGB-D显著目标检测中多视图信息利用不足的问题。②提出了MVSalNet，通过多视图增强策略提升深度和RGB特征的融合效果。③相比单视图方法，增强了跨视图的互补性。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper proposes MVSalNet for RGB-D salient object detection with multi-view augmentation. It enhances feature fusion across views but lacks detailed experimental results in the abstract.
- **核心贡献**: 提出多视图增强的RGB-D显著目标检测网络。
- **创新点**: 多视图增强策略用于RGB-D特征融合。
- **结果**: 未提供具体性能数据。

### Sequential Multi-view Fusion Network for Fast LiDAR Point Motion Estimation. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_17) · 📚 被引 3
- **作者**: Gang Zhang, Xiaoyan Li, Zhenhua Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对LiDAR点云运动估计的实时性问题。②提出了序列多视图融合网络，通过多帧信息融合加速运动估计。③相比单帧方法，利用了时序信息提升准确性。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper introduces a sequential multi-view fusion network for fast LiDAR point motion estimation. It leverages temporal information across frames but lacks detailed results in the abstract.
- **核心贡献**: 提出序列多视图融合网络用于LiDAR运动估计。
- **创新点**: 多帧时序融合策略提升运动估计速度。
- **结果**: 未提供具体性能数据。

### RC-MVSNet: Unsupervised Multi-View Stereo with Neural Rendering. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2203.03949](https://arxiv.org/abs/2203.03949) · 📚 被引 54
- **作者**: Di Chang, Aljaz Bozic, Tong Zhang, Qingsong Yan, Yingcong Chen, Sabine Süsstrunk et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对无监督多视图立体匹配中非朗伯表面和遮挡导致的对应关系歧义问题。②提出了RC-MVSNet，引入神经渲染的深度渲染一致性损失和参考视图合成损失。③相比现有无监督方法，通过几何约束和合成监督缓解了光照和遮挡影响。④在DTU和Tanks&Temples基准上达到无监督SOTA，性能接近有监督方法。
- **摘要（英）**: This paper addresses correspondence ambiguity in unsupervised MVS caused by non-Lambertian surfaces and occlusions. RC-MVSNet introduces depth rendering consistency and reference view synthesis losses. It achieves state-of-the-art unsupervised performance on DTU and Tanks&Temples, competitive with supervised methods.
- **核心贡献**: 提出基于神经渲染的无监督MVS方法，解决遮挡和非朗伯表面问题。
- **创新点**: 深度渲染一致性损失和参考视图合成损失联合优化。
- **结果**: 在DTU和Tanks&Temples上达到无监督SOTA，接近有监督性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Finding accurate correspondences among different views is the Achilles' heel of unsupervised Multi-View Stereo (MVS). Existing methods are built upon the assumption that corresponding pixels share similar photometric features. However, multi-view images in real scenarios observe non-Lambertian surfaces and experience occlusions. In this work, we propose a novel approach with neural rendering (RC-MVSNet) to solve such ambiguity issues of correspondences among views. Specifically, we impose a depth rendering consistency loss to constrain the geometry features close to the object surface to alleviate occlusions. Concurrently, we introduce a reference view synthesis loss to generate consistent supervision, even for non-Lambertian surfaces. Extensive experiments on DTU and Tanks\&Temples benchmarks demonstrate that our RC-MVSNet approach achieves state-of-the-art performance over unsupervised MVS frameworks and competitive performance to many supervised methods.The code is released at https://github.com/Boese0601/RC-MVSNet

</details>

### FLEX: Extrinsic Parameters-free Multi-view 3D Human Motion Reconstruction. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_11) · 📚 被引 31
- **作者**: Brian Gordon, Sigal Raab, Guy Azov, Raja Giryes, Daniel Cohen-Or
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角3D人体运动重建中依赖相机外参的问题。②提出了FLEX方法，无需外参即可重建3D人体运动。③相比传统方法，消除了标定需求，提升了实用性。④摘要缺失，无法提供具体数据。
- **摘要（英）**: This paper introduces FLEX for multi-view 3D human motion reconstruction without extrinsic parameters. It removes calibration requirements, enhancing practicality, but lacks detailed results in the abstract.
- **核心贡献**: 提出无需外参的多视角3D人体运动重建方法。
- **创新点**: 去除外参依赖，简化多相机系统部署。
- **结果**: 未提供具体性能数据。

### Depth Field Networks For Generalizable Multi-view Scene Representation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.14287](https://arxiv.org/abs/2207.14287) · 📚 被引 13
- **作者**: Vitor Guizilini, Igor Vasiljevic, Jiading Fang, Rare Ambru, Greg Shakhnarovich, Matthew R. Walter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多视角场景表示中传统几何约束（如代价体、极线约束）导致领域泛化差的问题，提出深度场网络（DeFiNe），学习隐式多视角一致场景表示，并引入3D数据增强作为几何先验以增加视角多样性，同时将视图合成作为辅助任务提升深度估计。相比依赖显式几何约束的专用架构，该方法无需几何约束即可在立体和视频深度估计上达到最先进水平，并在零样本领域泛化上大幅提升。
- **摘要（英）**: To address poor domain generalization in multi-view scene representation caused by explicit geometric constraints, this paper proposes Depth Field Networks (DeFiNe), which learn an implicit multi-view consistent representation with 3D data augmentation as geometric prior and view synthesis as auxiliary task. Without explicit geometric constraints, DeFiNe achieves state-of-the-art results in stereo and video depth estimation and significantly improves zero-shot domain generalization.
- **核心贡献**: 提出无需显式几何约束的隐式多视角场景表示方法，提升深度估计的泛化能力。
- **创新点**: 将几何先验编码为输入而非约束，并引入3D数据增强和视图合成辅助任务。
- **结果**: 在立体和视频深度估计上达到最先进水平，零样本泛化大幅提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern 3D computer vision leverages learning to boost geometric reasoning, mapping image data to classical structures such as cost volumes or epipolar constraints to improve matching. These architectures are specialized according to the particular problem, and thus require significant task-specific tuning, often leading to poor domain generalization performance. Recently, generalist Transformer architectures have achieved impressive results in tasks such as optical flow and depth estimation by encoding geometric priors as inputs rather than as enforced constraints. In this paper, we extend this idea and propose to learn an implicit, multi-view consistent scene representation, introducing a series of 3D data augmentation techniques as a geometric inductive prior to increase view diversity. We also show that introducing view synthesis as an auxiliary task further improves depth estimation. Our Depth Field Networks (DeFiNe) achieve state-of-the-art results in stereo and video depth estimation without explicit geometric constraints, and improve on zero-shot domain generalization by a wide margin.

</details>

### MODE: Multi-view Omnidirectional Depth Estimation with 360$\circ $ Cameras. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_12)
- **作者**: Ming Li, Xueqian Jin, Xuejiao Hu, Jingzhao Dai, Sidan Du, Yang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对360度相机全景深度估计问题，提出多视角全向深度估计方法（MODE），利用多视角几何和全景图像特性提升深度精度。但摘要缺失，无法评估具体技术细节和性能数据。
- **摘要（英）**: This paper addresses omnidirectional depth estimation with 360-degree cameras by proposing a multi-view method that leverages panoramic geometry. However, the abstract is missing, so specific techniques and results cannot be assessed.
- **核心贡献**: 提出多视角全向深度估计方法。
- **创新点**: 结合全景相机多视角几何进行深度估计。
- **结果**: 未提供具体实验结果。

### Neural Strands: Learning Hair Geometry and Appearance from Multi-view Images. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2207.14067](https://arxiv.org/abs/2207.14067) · 📚 被引 42
- **作者**: Radu Alexandru Rosu, Shunsuke Saito, Ziyan Wang, Chenglei Wu, Sven Behnke, Giljoo Nam
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对多视角图像中头发几何和外观建模的挑战，提出Neural Strands框架，基于神经头皮纹理编码每根发丝的几何和外观，并通过光栅化实现实时渲染。引入多视角几何先验，首次实现外观和显式头发几何的联合学习。实验证明该方法在保真度和效率上优于体积方法，支持实时高保真渲染。
- **摘要（英）**: For modeling hair geometry and appearance from multi-view images, this paper proposes Neural Strands, using a neural scalp texture to encode per-strand geometry and appearance, with rasterization-based neural rendering for real-time view-dependent effects. Jointly learning appearance and explicit geometry with multi-view priors, it achieves high fidelity and efficiency for various hairstyles.
- **核心贡献**: 提出基于神经纹理的头发几何和外观联合建模方法。
- **创新点**: 神经头皮纹理和光栅化神经渲染。
- **结果**: 实现实时高保真渲染，优于体积方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Neural Strands, a novel learning framework for modeling accurate hair geometry and appearance from multi-view image inputs. The learned hair model can be rendered in real-time from any viewpoint with high-fidelity view-dependent effects. Our model achieves intuitive shape and style control unlike volumetric counterparts. To enable these properties, we propose a novel hair representation based on a neural scalp texture that encodes the geometry and appearance of individual strands at each texel location. Furthermore, we introduce a novel neural rendering framework based on rasterization of the learned hair strands. Our neural rendering is strand-accurate and anti-aliased, making the rendering view-consistent and photorealistic. Combining appearance with a multi-view geometric prior, we enable, for the first time, the joint learning of appearance and explicit hair geometry from a multi-view setup. We demonstrate the efficacy of our approach in terms of fidelity and efficiency for various hairstyles.

</details>

### A Real World Dataset for Multi-view 3D Reconstruction. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2203.11397](https://arxiv.org/abs/2203.11397) · 📚 被引 10
- **作者**: Rakesh Shrestha, Siqi Hu, Minghao Gou, Ziyuan Liu, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多视角3D重建缺乏真实世界基准数据集的问题。②构建了包含998个日常桌面物体3D模型和84.7万张真实RGB-D图像的数据集，并半自动标注相机位姿和物体位姿。③相比合成数据集，提供了真实世界的多视角图像和精确标注，填补了该任务基准的空白。④数据集和标注工具、评估基线已公开，可支持形状重建、姿态估计等任务。
- **摘要（英）**: This paper addresses the lack of real-world benchmarks for multi-view 3D reconstruction by presenting a dataset of 998 3D models with 847,000 real RGB-D images and semi-automated pose annotations. It fills the gap by providing accurate real-world data, and the dataset, tools, and baselines are publicly available.
- **核心贡献**: 提供了大规模真实世界多视角3D重建数据集及标注工具。
- **创新点**: 半自动化的相机和物体位姿标注流程。
- **结果**: 公开了998个物体和84.7万张图像的数据集，支持多种3D任务。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a dataset of 998 3D models of everyday tabletop objects along with their 847,000 real world RGB and depth images. Accurate annotations of camera poses and object poses for each image are performed in a semi-automated fashion to facilitate the use of the dataset for myriad 3D applications like shape reconstruction, object pose estimation, shape retrieval etc. We primarily focus on learned multi-view 3D reconstruction due to the lack of appropriate real world benchmark for the task and demonstrate that our dataset can fill that gap. The entire annotated dataset along with the source code for the annotation tools and evaluation baselines is available at http://www.ocrtoc.org/3d-reconstruction.html.

</details>

### MVSTER: Epipolar Transformer for Efficient Multi-view Stereo. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2204.07346](https://arxiv.org/abs/2204.07346) · 📚 被引 115
- **作者**: Xiaofeng Wang, Zheng Zhu, Guan Huang, Fangbo Qin, Yun Ye, Yijia He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对学习型多视角立体（MVS）方法在代价体融合时未充分利用3D空间关联且计算开销大的问题。②提出了MVSTER，利用极线Transformer高效学习2D语义和3D空间关联，采用可分离的单目深度估计器增强2D语义，并通过交叉注意力沿极线构建数据相关的3D关联。③相比MVSNet和CasMVSNet，在DTU基准上分别获得34%和14%的相对提升，同时效率显著提高。④实验表明达到了最先进的重建性能。
- **摘要（英）**: This paper tackles inefficient cost volume fusion in MVS by proposing MVSTER, which uses an epipolar Transformer to jointly learn 2D semantics and 3D spatial associations, with a detachable monocular depth estimator. It achieves 34% and 14% relative improvements over MVSNet and CasMVSNet on DTU, with higher efficiency.
- **核心贡献**: 提出极线Transformer架构，高效融合2D和3D信息用于MVS。
- **创新点**: 利用交叉注意力沿极线构建数据相关的3D关联。
- **结果**: 在DTU基准上实现最先进性能，相对MVSNet提升34%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning-based Multi-View Stereo (MVS) methods warp source images into the reference camera frustum to form 3D volumes, which are fused as a cost volume to be regularized by subsequent networks. The fusing step plays a vital role in bridging 2D semantics and 3D spatial associations. However, previous methods utilize extra networks to learn 2D information as fusing cues, underusing 3D spatial correlations and bringing additional computation costs. Therefore, we present MVSTER, which leverages the proposed epipolar Transformer to learn both 2D semantics and 3D spatial associations efficiently. Specifically, the epipolar Transformer utilizes a detachable monocular depth estimator to enhance 2D semantics and uses cross-attention to construct data-dependent 3D associations along epipolar line. Additionally, MVSTER is built in a cascade structure, where entropy-regularized optimal transport is leveraged to propagate finer depth estimations in each stage. Extensive experiments show MVSTER achieves state-of-the-art reconstruction performance with significantly higher efficiency: Compared with MVSNet and CasMVSNet, our MVSTER achieves 34% and 14% relative improvements on the DTU benchmark, with 80% and 51% relative reductions in running time. MVSTER also ranks first on Tanks&Temples-Advanced among all published works. Code is released at https://github.com/JeffWang987.

</details>

### Incomplete Multi-view Domain Adaptation via Channel Enhancement and Knowledge Transfer. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19830-4_12) · 📚 被引 5
- **作者**: Haifeng Xia, Pu Wang, Zhengming Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对不完整多视角域适应问题，即不同视角数据缺失且分布不一致。②提出了通道增强和知识迁移的方法，但摘要内容不完整，缺乏具体技术细节。③改进点不明确，可能涉及特征通道增强和跨域知识迁移。④效果未在摘要中给出。
- **摘要（英）**: This paper addresses incomplete multi-view domain adaptation with channel enhancement and knowledge transfer, but the abstract lacks technical details and results, limiting its assessment.
- **核心贡献**: 提出通道增强和知识迁移策略用于不完整多视角域适应。
- **创新点**: 结合通道增强与知识迁移处理数据缺失和分布偏移。
- **结果**: 未报告具体效果。

### PS-NeRF: Neural Inverse Rendering for Multi-view Photometric Stereo. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2207.11406](https://arxiv.org/abs/2207.11406) · 📚 被引 69
- **作者**: Wenqi Yang, Guanying Chen, Chaofeng Chen, Zhenfang Chen, Kwan-Yee K. Wong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对传统多视角光度立体（MVPS）方法多阶段分离导致误差累积的问题。②提出了PS-NeRF，一种基于隐式表示的神经逆渲染方法，联合估计几何、材质和光照。③利用多光图像估计每视角法线图以正则化神经辐射场，并通过阴影感知的可微渲染层联合优化法线、BRDF和光照。④在合成和真实数据集上，形状重建精度远超现有MVPS和神经渲染方法。
- **摘要（英）**: This paper addresses error accumulation in traditional MVPS by proposing PS-NeRF, a neural inverse rendering method that jointly estimates geometry, materials, and lights using implicit representation. It regularizes normals from multi-light images and optimizes via shadow-aware differentiable rendering, achieving far more accurate reconstruction than existing methods.
- **核心贡献**: 提出联合估计几何、材质和光照的神经逆渲染框架。
- **创新点**: 利用多光法线正则化和阴影感知渲染优化隐式表示。
- **结果**: 在合成和真实数据集上重建精度显著优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional multi-view photometric stereo (MVPS) methods are often composed of multiple disjoint stages, resulting in noticeable accumulated errors. In this paper, we present a neural inverse rendering method for MVPS based on implicit representation. Given multi-view images of a non-Lambertian object illuminated by multiple unknown directional lights, our method jointly estimates the geometry, materials, and lights. Our method first employs multi-light images to estimate per-view surface normal maps, which are used to regularize the normals derived from the neural radiance field. It then jointly optimizes the surface normals, spatially-varying BRDFs, and lights based on a shadow-aware differentiable rendering layer. After optimization, the reconstructed object can be used for novel-view rendering, relighting, and material editing. Experiments on both synthetic and real datasets demonstrate that our method achieves far more accurate shape reconstruction than existing MVPS and neural rendering methods. Our code and model can be found at https://ywq.github.io/psnerf.

</details>

### MVDG: A Unified Multi-view Framework for Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19812-0_10)
- **作者**: Jian Zhang, Lei Qi, Yinghuan Shi, Yang Gao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Calibration-Free Multi-view Crowd Counting.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_14) · 📚 被引 13
- **作者**: Qi Zhang, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### 3D Random Occlusion and Multi-layer Projection for Deep Multi-camera Pedestrian Localization.
- **链接**: [arXiv:2207.10895](https://arxiv.org/abs/2207.10895) · 📚 被引 35
- **作者**: Rui Qiu, Ming Xu, Yuyao Yan, Jeremy S. Smith, Xi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although deep-learning based methods for monocular pedestrian detection have made great progress, they are still vulnerable to heavy occlusions. Using multi-view information fusion is a potential solution but has limited applications, due to the lack of annotated training samples in existing multi-view datasets, which increases the risk of overfitting. To address this problem, a data augmentation method is proposed to randomly generate 3D cylinder occlusions, on the ground plane, which are of the average size of pedestrians and projected to multiple views, to relieve the impact of overfitting in the training. Moreover, the feature map of each view is projected to multiple parallel planes at different heights, by using homographies, which allows the CNNs to fully utilize the features across the height of each pedestrian to infer the locations of pedestrians on the ground plane. The proposed 3DROM method has a greatly improved performance in comparison with the state-of-the-art deep-learning based methods for multi-view pedestrian detection.

</details>

### Affine Correspondences Between Multi-camera Systems for 6DOF Relative Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19824-3_37)
- **作者**: Banglei Guan, Ji Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### RA-Depth: Resolution Adaptive Self-supervised Monocular Depth Estimation.
- **链接**: [arXiv:2207.11984](https://arxiv.org/abs/2207.11984)
- **作者**: Mu He, Le Hui, Yikai Bian, Jian Ren, Jin Xie, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing self-supervised monocular depth estimation methods can get rid of expensive annotations and achieve promising results. However, these methods suffer from severe performance degradation when directly adopting a model trained on a fixed resolution to evaluate at other different resolutions. In this paper, we propose a resolution adaptive self-supervised monocular depth estimation method (RA-Depth) by learning the scale invariance of the scene depth. Specifically, we propose a simple yet efficient data augmentation method to generate images with arbitrary scales for the same scene. Then, we develop a dual high-resolution network that uses the multi-path encoder and decoder with dense interactions to aggregate multi-scale features for accurate depth inference. Finally, to explicitly learn the scale invariance of the scene depth, we formulate a cross-scale depth consistency loss on depth predictions with different scales. Extensive experiments on the KITTI, Make3D and NYU-V2 datasets demonstrate that RA-Depth not only achieves state-of-the-art performance, but also exhibits a good ability of resolution adaptation.

</details>

### Depth Map Decomposition for Monocular Depth Estimation.
- **链接**: [arXiv:2208.10762](https://arxiv.org/abs/2208.10762)
- **作者**: Jinyoung Jun, Jaehan Lee, Chul Lee, Chang-Su Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel algorithm for monocular depth estimation that decomposes a metric depth map into a normalized depth map and scale features. The proposed network is composed of a shared encoder and three decoders, called G-Net, N-Net, and M-Net, which estimate gradient maps, a normalized depth map, and a metric depth map, respectively. M-Net learns to estimate metric depths more accurately using relative depth features extracted by G-Net and N-Net. The proposed algorithm has the advantage that it can use datasets without metric depth labels to improve the performance of metric depth estimation. Experimental results on various datasets demonstrate that the proposed algorithm not only provides competitive performance to state-of-the-art algorithms but also yields acceptable results even when only a small amount of metric depth data is available for its training.

</details>

### Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches.
- **链接**: [arXiv:2207.04718](https://arxiv.org/abs/2207.04718) · 📚 被引 11
- **作者**: Zhiyuan Cheng, James Liang, Hongjun Choi, Guanhong Tao, Zhiwen Cao, Dongfang Liu et al.
- **🏷️ 机构**: School of Automation, Northwestern Polytechnical University, Xi&#x2019;an, Shaanxi, China
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has substantially boosted the performance of Monocular Depth Estimation (MDE), a critical component in fully vision-based autonomous driving (AD) systems (e.g., Tesla and Toyota). In this work, we develop an attack against learning-based MDE. In particular, we use an optimization-based method to systematically generate stealthy physical-object-oriented adversarial patches to attack depth estimation. We balance the stealth and effectiveness of our attack with object-oriented adversarial design, sensitive region localization, and natural style camouflage. Using real-world driving scenarios, we evaluate our attack on concurrent MDE models and a representative downstream task for AD (i.e., 3D object detection). Experimental results show that our method can generate stealthy, effective, and robust adversarial patches for different target objects and models and achieves more than 6 meters mean depth estimation error and 93% attack success rate (ASR) in object detection with a patch of 1/9 of the vehicle's rear area. Field tests on three different driving routes with a real vehicle indicate that we cause over 6 meters mean depth estimation error and reduce the object detection rate from 90.70% to 5.16% in continuous video frames.

</details>

### BRNet: Exploring Comprehensive Features for Monocular Depth Estimation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19839-7_34) · 📚 被引 40
- **作者**: Wencheng Han, Junbo Yin, Xiaogang Jin, Xiangdong Dai, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Gradient-Based Uncertainty for Monocular Depth Estimation.
- **链接**: [arXiv:2208.02005](https://arxiv.org/abs/2208.02005)
- **作者**: Julia Hornauer, Vasileios Belagiannis
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In monocular depth estimation, disturbances in the image context, like moving objects or reflecting materials, can easily lead to erroneous predictions. For that reason, uncertainty estimates for each pixel are necessary, in particular for safety-critical applications such as automated driving. We propose a post hoc uncertainty estimation approach for an already trained and thus fixed depth estimation model, represented by a deep neural network. The uncertainty is estimated with the gradients which are extracted with an auxiliary loss function. To avoid relying on ground-truth information for the loss definition, we present an auxiliary loss function based on the correspondence of the depth prediction for an image and its horizontally flipped counterpart. Our approach achieves state-of-the-art uncertainty estimation results on the KITTI and NYU Depth V2 benchmarks without the need to retrain the neural network. Models and code are publicly available at https://github.com/jhornauer/GrUMoDepth.

</details>

### Curvature-Guided Dynamic Scale Networks for Multi-View Stereo.
- **链接**: [arXiv:2112.05999](https://arxiv.org/abs/2112.05999)
- **作者**: Khang Truong Giang, Soohwan Song, Sungho Jo
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view stereo (MVS) is a crucial task for precise 3D reconstruction. Most recent studies tried to improve the performance of matching cost volume in MVS by designing aggregated 3D cost volumes and their regularization. This paper focuses on learning a robust feature extraction network to enhance the performance of matching costs without heavy computation in the other steps. In particular, we present a dynamic scale feature extraction network, namely, CDSFNet. It is composed of multiple novel convolution layers, each of which can select a proper patch scale for each pixel guided by the normal curvature of the image surface. As a result, CDFSNet can estimate the optimal patch scales to learn discriminative features for accurate matching computation between reference and source images. By combining the robust extracted features with an appropriate cost formulation strategy, our resulting MVS architecture can estimate depth maps more precisely. Extensive experiments showed that the proposed method outperforms other state-of-the-art methods on complex outdoor scenes. It significantly improves the completeness of reconstructed models. As a result, the method can process higher resolution inputs within faster run-time and lower memory than other MVS methods. Our source code is available at url{https://github.com/TruongKhang/cds-mvsnet}.

</details>

### MetAug: Contrastive Learning via Meta Feature Augmentation.
- **链接**: [arXiv:2203.05119](https://arxiv.org/abs/2203.05119)
- **作者**: Jiangmeng Li, Wenwen Qiang, Changwen Zheng, Bing Su, Hui Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What matters for contrastive learning? We argue that contrastive learning heavily relies on informative features, or "hard" (positive or negative) features. Early works include more informative features by applying complex data augmentations and large batch size or memory bank, and recent works design elaborate sampling approaches to explore informative features. The key challenge toward exploring such features is that the source multi-view data is generated by applying random data augmentations, making it infeasible to always add useful information in the augmented data. Consequently, the informativeness of features learned from such augmented data is limited. In response, we propose to directly augment the features in latent space, thereby learning discriminative representations without a large amount of input data. We perform a meta learning technique to build the augmentation generator that updates its network parameters by considering the performance of the encoder. However, insufficient input data may lead the encoder to learn collapsed features and therefore malfunction the augmentation generator. A new margin-injected regularization is further added in the objective function to avoid the encoder learning a degenerate mapping. To contrast all features in one gradient back-propagation step, we adopt the proposed optimization-driven unified contrastive loss instead of the conventional contrastive loss. Empirically, our method achieves state-of-the-art results on several benchmark datasets.

</details>

## 跨领域论文（完整笔记在其他领域）

- BEVFormer: Learning Bird's-Eye-View Representation from Multi-camera Images via Spatiotemporal Transformers. → [bev](../bev/Guideline%202022.md)
- Bridged Transformer for Vision and Point Cloud 3D Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention. → [object-detection](../object-detection/Guideline%202022.md)
- A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation. → [object-detection](../object-detection/Guideline%202022.md)
- PointCLIP: Point Cloud Understanding by CLIP. → [vlm](../vlm/Guideline%202022.md)
- KD-MVS: Knowledge Distillation Based Self-supervised Learning for Multi-view Stereo. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- PPT: Token-Pruned Pose Transformer for Monocular and Multi-view Human Pose Estimation. → [network-pruning](../network-pruning/Guideline%202022.md)
- MvDeCor: Multi-view Dense Correspondence Learning for Fine-Grained 3D Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- DevNet: Self-supervised Monocular Depth Learning via Density Volume Construction. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
<!-- COMPLETE v1 papers=65 -->
