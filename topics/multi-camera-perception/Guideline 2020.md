# Multi-camera Perception — 2020 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 23 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Learning Multiview 3D Point Cloud Registration.
- **链接**: [arXiv:2001.05119](https://arxiv.org/abs/2001.05119) · [代码](https://github.com/zgojcic/3D_multiview_reg) · 📚 被引 160
- **作者**: Zan Gojcic, Caifa Zhou, Jan D. Wegner, Leonidas J. Guibas, Tolga Birdal
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > We present a novel, end-to-end learnable, multiview 3D point cloud registration algorithm. Registration of multiple scans typically follows a two-stage pipeline: the initial pairwise alignment and the globally consistent refinement. The former is often ambiguous due to the low overlap of neighboring point clouds, symmetries and repetitive scene parts. Therefore, the latter global refinement aims at establishing the cyclic consistency across multiple scans and helps in resolving the ambiguous cases. In this paper we propose, to the best of our knowledge, the first end-to-end algorithm for joint learning of both parts of this two-stage problem. Experimental evaluation on well accepted benchmark datasets shows that our approach outperforms the state-of-the-art by a significant margin, while being end-to-end trainable and computationally less costly. Moreover, we present detailed analysis and an ablation study that validate the novel components of our approach. The source code and pretrained models are publicly available under https://github.com/zgojcic/3D_multiview_reg.

### End-to-End Learning Local Multi-View Descriptors for 3D Point Clouds.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_End-to-End_Learning_Local_Multi-View_Descriptors_for_3D_Point_Clouds_CVPR_2020_paper.html) · 📚 被引 102
- **作者**: Lei Li, Siyu Zhu, Hongbo Fu, Ping Tan, Chiew-Lan Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### BlendedMVS: A Large-Scale Dataset for Generalized Multi-View Stereo Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Yao_BlendedMVS_A_Large-Scale_Dataset_for_Generalized_Multi-View_Stereo_Networks_CVPR_2020_paper.html) · 📚 被引 450
- **作者**: Yao Yao, Zixin Luo, Shiwei Li, Jingyang Zhang, Yufan Ren, Lei Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Deep Facial Non-Rigid Multi-View Stereo.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Bai_Deep_Facial_Non-Rigid_Multi-View_Stereo_CVPR_2020_paper.html) · 📚 被引 56
- **作者**: Ziqian Bai, Zhaopeng Cui, Jamal Ahmed Rahim, Xiaoming Liu, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### 4D Visualization of Dynamic Events From Unconstrained Multi-View Videos.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Bansal_4D_Visualization_of_Dynamic_Events_From_Unconstrained_Multi-View_Videos_CVPR_2020_paper.html) · 📚 被引 61
- **作者**: Aayush Bansal, Minh Vo, Yaser Sheikh, Deva Ramanan, Srinivasa G. Narasimhan
- **🏷️ 机构**: CMU
- **会议**: CVPR 2020

### Deep 3D Capture: Geometry and Reflectance From Sparse Multi-View Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Bi_Deep_3D_Capture_Geometry_and_Reflectance_From_Sparse_Multi-View_Images_CVPR_2020_paper.html) · 📚 被引 77
- **作者**: Sai Bi, Zexiang Xu, Kalyan Sunkavalli, David J. Kriegman, Ravi Ramamoorthi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Gu_Cascade_Cost_Volume_for_High-Resolution_Multi-View_Stereo_and_Stereo_Matching_CVPR_2020_paper.html) · 📚 被引 785
- **作者**: Xiaodong Gu, Zhiwen Fan, Siyu Zhu, Zuozhuo Dai, Feitong Tan, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Exploit Clues From Views: Self-Supervised and Regularized Learning for Multiview Object Recognition.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Ho_Exploit_Clues_From_Views_Self-Supervised_and_Regularized_Learning_for_Multiview_CVPR_2020_paper.html)
- **作者**: Chih-Hui Ho, Bo Liu, Tz-Ying Wu, Nuno Vasconcelos
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Weakly-Supervised 3D Human Pose Learning via Multi-View Images in the Wild.
- **链接**: [arXiv:2003.07581](https://arxiv.org/abs/2003.07581) · 📚 被引 98
- **作者**: Umar Iqbal, Pavlo Molchanov, Jan Kautz
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > One major challenge for monocular 3D human pose estimation in-the-wild is the acquisition of training data that contains unconstrained images annotated with accurate 3D poses. In this paper, we address this challenge by proposing a weakly-supervised approach that does not require 3D annotations and learns to estimate 3D poses from unlabeled multi-view data, which can be acquired easily in in-the-wild environments. We propose a novel end-to-end learning framework that enables weakly-supervised training using multi-view consistency. Since multi-view consistency is prone to degenerated solutions, we adopt a 2.5D pose representation and propose a novel objective function that can only be minimized when the predictions of the trained model are consistent and plausible across all camera views. We evaluate our proposed approach on two large scale datasets (Human3.6M and MPII-INF-3DHP) where it achieves state-of-the-art performance among semi-/weakly-supervised methods.

### A Novel Recurrent Encoder-Decoder Structure for Large-Scale Multi-View Stereo Reconstruction From an Open Aerial Dataset.
- **链接**: [arXiv:2003.00637](https://arxiv.org/abs/2003.00637) · 📚 被引 110
- **作者**: Jin Liu, Shunping Ji
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > A great deal of research has demonstrated recently that multi-view stereo (MVS) matching can be solved with deep learning methods. However, these efforts were focused on close-range objects and only a very few of the deep learning-based methods were specifically designed for large-scale 3D urban reconstruction due to the lack of multi-view aerial image benchmarks. In this paper, we present a synthetic aerial dataset, called the WHU dataset, we created for MVS tasks, which, to our knowledge, is the first large-scale multi-view aerial dataset. It was generated from a highly accurate 3D digital surface model produced from thousands of real aerial images with precise camera parameters. We also introduce in this paper a novel network, called RED-Net, for wide-range depth inference, which we developed from a recurrent encoder-decoder structure to regularize cost maps across depths and a 2D fully convolutional network as framework. RED-Net's low memory requirements and high performance make it suitable for large-scale and highly accurate 3D Earth surface reconstruction. Our experiments confirmed that not only did our method exceed the current state-of-the-art MVS methods by more than 50% mean absolute error (MAE) with less memory and computational cost, but its efficiency as well. It outperformed one of the best commercial software programs based on conventional methods, improving their efficiency 16 times over. Moreover, we proved that our RED-Net model pre-trained on the synthetic WHU dataset can be efficiently transferred to very different multi-view aerial image datasets without any fine-tuning. Dataset are available at http://gpcv.whu.edu.cn/data.

### KeyPose: Multi-View 3D Labeling and Keypoint Estimation for Transparent Objects.
- **链接**: [arXiv:1912.02805](https://arxiv.org/abs/1912.02805) · 📚 被引 111
- **作者**: Xingyu Liu, Rico Jonschkowski, Anelia Angelova, Kurt Konolige
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Estimating the 3D pose of desktop objects is crucial for applications such as robotic manipulation. Many existing approaches to this problem require a depth map of the object for both training and prediction, which restricts them to opaque, lambertian objects that produce good returns in an RGBD sensor. In this paper we forgo using a depth sensor in favor of raw stereo input. We address two problems: first, we establish an easy method for capturing and labeling 3D keypoints on desktop objects with an RGB camera; and second, we develop a deep neural network, called $KeyPose$, that learns to accurately predict object poses using 3D keypoints, from stereo input, and works even for transparent objects. To evaluate the performance of our method, we create a dataset of 15 clear objects in five classes, with 48K 3D-keypoint labeled images. We train both instance and category models, and show generalization to new textures, poses, and objects. KeyPose surpasses state-of-the-art performance in 3D pose estimation on this dataset by factors of 1.5 to 3.5, even in cases where the competing method is provided with ground-truth depth. Stereo input is essential for this performance as it improves results compared to using monocular input by a factor of 2. We will release a public version of the data capture and labeling pipeline, the transparent object database, and the KeyPose models and evaluation code. Project website: https://sites.google.com/corp/view/keypose.

### Attention-Aware Multi-View Stereo.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Luo_Attention-Aware_Multi-View_Stereo_CVPR_2020_paper.html)
- **作者**: Keyang Luo, Tao Guan, Lili Ju, Yuesong Wang, Zhuo Chen, Yawei Luo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Lightweight Multi-View 3D Pose Estimation Through Camera-Disentangled Representation.
- **链接**: [arXiv:2004.02186](https://arxiv.org/abs/2004.02186) · 📚 被引 111
- **作者**: Edoardo Remelli, Shangchen Han, Sina Honari, Pascal Fua, Robert Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > We present a lightweight solution to recover 3D pose from multi-view images captured with spatially calibrated cameras. Building upon recent advances in interpretable representation learning, we exploit 3D geometry to fuse input images into a unified latent representation of pose, which is disentangled from camera view-points. This allows us to reason effectively about 3D pose across different views without using compute-intensive volumetric grids. Our architecture then conditions the learned representation on camera projection operators to produce accurate per-view 2d detections, that can be simply lifted to 3D via a differentiable Direct Linear Transform (DLT) layer. In order to do it efficiently, we propose a novel implementation of DLT that is orders of magnitude faster on GPU architectures than standard SVD-based triangulation methods. We evaluate our approach on two large-scale human pose datasets (H36M and Total Capture): our method outperforms or performs comparably to the state-of-the-art volumetric methods, while, unlike them, yielding real-time performance.

### Mesh-Guided Multi-View Stereo With Pyramid Architecture.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wang_Mesh-Guided_Multi-View_Stereo_With_Pyramid_Architecture_CVPR_2020_paper.html) · 📚 被引 34
- **作者**: Yuesong Wang, Tao Guan, Zhuo Chen, Yawei Luo, Keyang Luo, Lili Ju
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Multi-View Neural Human Rendering.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wu_Multi-View_Neural_Human_Rendering_CVPR_2020_paper.html) · 📚 被引 95
- **作者**: Minye Wu, Yuehao Wang, Qiang Hu, Jingyi Yu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Learning Multi-View Camera Relocalization With Graph Neural Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Xue_Learning_Multi-View_Camera_Relocalization_With_Graph_Neural_Networks_CVPR_2020_paper.html) · 📚 被引 65
- **作者**: Fei Xue, Xin Wu, Shaojun Cai, Junqiu Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Cost Volume Pyramid Based Depth Inference for Multi-View Stereo.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Yang_Cost_Volume_Pyramid_Based_Depth_Inference_for_Multi-View_Stereo_CVPR_2020_paper.html) · 📚 被引 333
- **作者**: Jiayu Yang, Wei Mao, José M. Álvarez, Miaomiao Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Fast-MVSNet: Sparse-to-Dense Multi-View Stereo With Learned Propagation and Gauss-Newton Refinement.
- **链接**: [arXiv:2003.13017](https://arxiv.org/abs/2003.13017) · [代码](https://github.com/svip-lab/FastMVSNet) · 📚 被引 231
- **作者**: Zehao Yu, Shenghua Gao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Almost all previous deep learning-based multi-view stereo (MVS) approaches focus on improving reconstruction quality. Besides quality, efficiency is also a desirable feature for MVS in real scenarios. Towards this end, this paper presents a Fast-MVSNet, a novel sparse-to-dense coarse-to-fine framework, for fast and accurate depth estimation in MVS. Specifically, in our Fast-MVSNet, we first construct a sparse cost volume for learning a sparse and high-resolution depth map. Then we leverage a small-scale convolutional neural network to encode the depth dependencies for pixels within a local region to densify the sparse high-resolution depth map. At last, a simple but efficient Gauss-Newton layer is proposed to further optimize the depth map. On one hand, the high-resolution depth map, the data-adaptive propagation method and the Gauss-Newton layer jointly guarantee the effectiveness of our method. On the other hand, all modules in our Fast-MVSNet are lightweight and thus guarantee the efficiency of our approach. Besides, our approach is also memory-friendly because of the sparse depth representation. Extensive experimental results show that our method is 5$\times$ and 14$\times$ faster than Point-MVSNet and R-MVSNet, respectively, while achieving comparable or even better results on the challenging Tanks and Temples dataset as well as the DTU dataset. Code is available at https://github.com/svip-lab/FastMVSNet.

### Fusing Wearable IMUs With Multi-View Images for Human Pose Estimation: A Geometric Approach.
- **链接**: [arXiv:2003.11163](https://arxiv.org/abs/2003.11163) · [代码](https://github.com/CHUNYUWANG/imu-human-pose-pytorch) · 📚 被引 66
- **作者**: Zhe Zhang, Chunyu Wang, Wenhu Qin, Wenjun Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > We propose to estimate 3D human pose from multi-view images and a few IMUs attached at person's limbs. It operates by firstly detecting 2D poses from the two signals, and then lifting them to the 3D space. We present a geometric approach to reinforce the visual features of each pair of joints based on the IMUs. This notably improves 2D pose estimation accuracy especially when one joint is occluded. We call this approach Orientation Regularized Network (ORN). Then we lift the multi-view 2D poses to the 3D space by an Orientation Regularized Pictorial Structure Model (ORPSM) which jointly minimizes the projection error between the 3D and 2D poses, along with the discrepancy between the 3D pose and IMU orientations. The simple two-step approach reduces the error of the state-of-the-art by a large margin on a public dataset. Our code will be released at https://github.com/CHUNYUWANG/imu-human-pose-pytorch.

### SDC-Depth: Semantic Divide-and-Conquer Network for Monocular Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wang_SDC-Depth_Semantic_Divide-and-Conquer_Network_for_Monocular_Depth_Estimation_CVPR_2020_paper.html) · 📚 被引 111
- **作者**: Lijun Wang, Jianming Zhang, Oliver Wang, Zhe Lin, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### 3D Packing for Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Guizilini_3D_Packing_for_Self-Supervised_Monocular_Depth_Estimation_CVPR_2020_paper.html)
- **作者**: Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raventos, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### On the Uncertainty of Self-Supervised Monocular Depth Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Poggi_On_the_Uncertainty_of_Self-Supervised_Monocular_Depth_Estimation_CVPR_2020_paper.html)
- **作者**: Matteo Poggi, Filippo Aleotti, Fabio Tosi, Stefano Mattoccia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Predicting Sharp and Accurate Occlusion Boundaries in Monocular Depth Estimation Using Displacement Fields.
- **链接**: [arXiv:2002.12730](https://arxiv.org/abs/2002.12730) · 📚 被引 54
- **作者**: Michaël Ramamonjisoa, Yuming Du, Vincent Lepetit
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Current methods for depth map prediction from monocular images tend to predict smooth, poorly localized contours for the occlusion boundaries in the input image. This is unfortunate as occlusion boundaries are important cues to recognize objects, and as we show, may lead to a way to discover new objects from scene reconstruction. To improve predicted depth maps, recent methods rely on various forms of filtering or predict an additive residual depth map to refine a first estimate. We instead learn to predict, given a depth map predicted by some reconstruction method, a 2D displacement field able to re-sample pixels around the occlusion boundaries into sharper reconstructions. Our method can be applied to the output of any depth estimation method, in an end-to-end trainable fashion. For evaluation, we manually annotated the occlusion boundaries in all the images in the test split of popular NYUv2-Depth dataset. We show that our approach improves the localization of occlusion boundaries for all state-of-the-art monocular depth estimation methods that we could evaluate, without degrading the depth accuracy for the rest of the images.
