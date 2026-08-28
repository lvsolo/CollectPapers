# Self-supervised Vision — 2025 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 45 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### BOE-ViT: Boosting Orientation Estimation with Equivariance in Self-Supervised 3D Subtomogram Alignment.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jiang_BOE-ViT_Boosting_Orientation_Estimation_with_Equivariance_in_Self-Supervised_3D_Subtomogram_CVPR_2025_paper.html)
- **作者**: Runmin Jiang, Jackson Daggett, Shriya Pingulkar, Yizhou Zhao, Priyanshu Dhingra, Daniel Brown et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Multi-Scale Neighborhood Occupancy Masked Autoencoder for Self-Supervised Learning in LiDAR Point Clouds.
- **链接**: [arXiv:2502.20316](https://arxiv.org/abs/2502.20316) · 📚 被引 5
- **作者**: Mohamed Abdelsamad, Michael Ulrich, Claudius Gläser, Abhinav Valada
- **🏷️ 机构**: Bosch Center for AI, University of Freiburg
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked autoencoders (MAE) have shown tremendous potential for self-supervised learning (SSL) in vision and beyond. However, point clouds from LiDARs used in automated driving are particularly challenging for MAEs since large areas of the 3D volume are empty. Consequently, existing work suffers from leaking occupancy information into the decoder and has significant computational complexity, thereby limiting the SSL pre-training to only 2D bird's eye view encoders in practice. In this work, we propose the novel neighborhood occupancy MAE (NOMAE) that overcomes the aforementioned challenges by employing masked occupancy reconstruction only in the neighborhood of non-masked voxels. We incorporate voxel masking and occupancy reconstruction at multiple scales with our proposed hierarchical mask generation technique to capture features of objects of different sizes in the point cloud. NOMAEs are extremely flexible and can be directly employed for SSL in existing 3D architectures. We perform extensive evaluations on the nuScenes and Waymo Open datasets for the downstream perception tasks of semantic segmentation and 3D object detection, comparing with both discriminative and generative SSL methods. The results demonstrate that NOMAE sets the new state-of-the-art on multiple benchmarks for multiple point cloud perception tasks.

</details>

### PSA-SSL: Pose and Size-aware Self-Supervised Learning on LiDAR Point Clouds.
- **链接**: [arXiv:2503.13914](https://arxiv.org/abs/2503.13914) · [代码](https://github.com/TRAILab/PSA-SSL) · 📚 被引 4
- **作者**: Barza Nisar, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) on 3D point clouds has the potential to learn feature representations that can transfer to diverse sensors and multiple downstream perception tasks. However, recent SSL approaches fail to define pretext tasks that retain geometric information such as object pose and scale, which can be detrimental to the performance of downstream localization and geometry-sensitive 3D scene understanding tasks, such as 3D semantic segmentation and 3D object detection. We propose PSA-SSL, a novel extension to point cloud SSL that learns object pose and size-aware (PSA) features. Our approach defines a self-supervised bounding box regression pretext task, which retains object pose and size information. Furthermore, we incorporate LiDAR beam pattern augmentation on input point clouds, which encourages learning sensor-agnostic features. Our experiments demonstrate that with a single pretrained model, our light-weight yet effective extensions achieve significant improvements on 3D semantic segmentation with limited labels across popular autonomous driving datasets (Waymo, nuScenes, SemanticKITTI). Moreover, our approach outperforms other state-of-the-art SSL methods on 3D semantic segmentation (using up to 10 times less labels), as well as on 3D object detection. Our code will be released on https://github.com/TRAILab/PSA-SSL.

</details>

### A Unified Approach to Interpreting Self-supervised Pre-training Methods for 3D Point Clouds via Interactions.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_A_Unified_Approach_to_Interpreting_Self-supervised_Pre-training_Methods_for_3D_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Qiang Li, Jian Ruan, Fanghao Wu, Yuchi Chen, Zhihua Wei, Wen Shen
- **🏷️ 机构**: Tongji University,Shanghai,China
- **会议**: CVPR 2025

### Self-Supervised Large Scale Point Cloud Completion for Archaeological Site Restoration.
- **链接**: [arXiv:2503.04030](https://arxiv.org/abs/2503.04030) · 📚 被引 2
- **作者**: Aocheng Li, James Zimmer-Dauphinee, Rajesh Kalyanam, Ian Lindsay, Parker VanValkenburgh, Steven A. Wernke et al.
- **🏷️ 机构**: Purdue University, Vanderbilt University, Brown University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point cloud completion helps restore partial incomplete point clouds suffering occlusions. Current self-supervised methods fail to give high fidelity completion for large objects with missing surfaces and unbalanced distribution of available points. In this paper, we present a novel method for restoring large-scale point clouds with limited and imbalanced ground-truth. Using rough boundary annotations for a region of interest, we project the original point clouds into a multiple-center-of-projection (MCOP) image, where fragments are projected to images of 5 channels (RGB, depth, and rotation). Completion of the original point cloud is reduced to inpainting the missing pixels in the MCOP images. Due to lack of complete structures and an unbalanced distribution of existing parts, we develop a self-supervised scheme which learns to infill the MCOP image with points resembling existing "complete" patches. Special losses are applied to further enhance the regularity and consistency of completed MCOP images, which is mapped back to 3D to form final restoration. Extensive experiments demonstrate the superiority of our method in completing 600+ incomplete and unbalanced archaeological structures in Peru.

</details>

### On-Device Self-Supervised Learning of Low-Latency Monocular Depth from Only Events.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hagenaars_On-Device_Self-Supervised_Learning_of_Low-Latency_Monocular_Depth_from_Only_Events_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Jesse J. Hagenaars, Yilun Wu, Federico Paredes-Vallés, Stein Stroobants, Guido C. H. E. de Croon
- **🏷️ 机构**: MAVLab, TU Delft, EUISPC, Sony Semiconductor Solutions Europe, Sony Europe B.V
- **会议**: CVPR 2025

### Improved Monocular Depth Prediction Using Distance Transform Over Pre-semantic Contours with Self-supervised Neural Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hariat_Improved_Monocular_Depth_Prediction_Using_Distance_Transform_Over_Pre-semantic_Contours_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Marwane Hariat, Antoine Manzanera, David Filliat
- **🏷️ 机构**: Institut Polytechnique de Paris,U2IS, ENSTA,Palaiseau,France
- **会议**: CVPR 2025

### Masked Scene Modeling: Narrowing the Gap Between Supervised and Self-Supervised Learning in 3D Scene Understanding.
- **链接**: [arXiv:2504.06719](https://arxiv.org/abs/2504.06719) · [代码](https://github.com/phermosilla/msm) · 📚 被引 0
- **作者**: Pedro Hermosilla, Christian Stippel, Leon Sick
- **🏷️ 机构**: TU Wien, Ulm University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has transformed 2D computer vision by enabling models trained on large, unannotated datasets to provide versatile off-the-shelf features that perform similarly to models trained with labels. However, in 3D scene understanding, self-supervised methods are typically only used as a weight initialization step for task-specific fine-tuning, limiting their utility for general-purpose feature extraction. This paper addresses this shortcoming by proposing a robust evaluation protocol specifically designed to assess the quality of self-supervised features for 3D scene understanding. Our protocol uses multi-resolution feature sampling of hierarchical models to create rich point-level representations that capture the semantic capabilities of the model and, hence, are suitable for evaluation with linear probing and nearest-neighbor methods. Furthermore, we introduce the first self-supervised model that performs similarly to supervised models when only off-the-shelf features are used in a linear probing setup. In particular, our model is trained natively in 3D with a novel self-supervised approach based on a Masked Scene Modeling objective, which reconstructs deep features of masked patches in a bottom-up manner and is specifically tailored to hierarchical 3D models. Our experiments not only demonstrate that our method achieves competitive performance to supervised models, but also surpasses existing self-supervised approaches by a large margin. The model and training code can be found at our Github repository (https://github.com/phermosilla/msm).

</details>

### Self-Supervised Learning for Color Spike Camera Reconstruction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Dong_Self-Supervised_Learning_for_Color_Spike_Camera_Reconstruction_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Yanchen Dong, Ruiqin Xiong, Xiaopeng Fan, Zhaofei Yu, Yonghong Tian, Tiejun Huang
- **🏷️ 机构**: Peking University,School of Computer Science, Harbin Institute of Technology,School of Computer Science and Technology, Peking University,Institute for Artificial Intelligence
- **会议**: CVPR 2025

### Sonata: Self-Supervised Learning of Reliable Point Representations.
- **链接**: [arXiv:2503.16429](https://arxiv.org/abs/2503.16429) · 📚 被引 19
- **作者**: Xiaoyang Wu, Daniel DeTone, Duncan P. Frost, Tianwei Shen, Chris Xie, Nan Yang et al.
- **🏷️ 机构**: The University of Hong Kong, Meta Reality Labs Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we question whether we have a reliable self-supervised point cloud model that can be used for diverse 3D tasks via simple linear probing, even with limited data and minimal computation. We find that existing 3D self-supervised learning approaches fall short when evaluated on representation quality through linear probing. We hypothesize that this is due to what we term the "geometric shortcut", which causes representations to collapse to low-level spatial features. This challenge is unique to 3D and arises from the sparse nature of point cloud data. We address it through two key strategies: obscuring spatial information and enhancing the reliance on input features, ultimately composing a Sonata of 140k point clouds through self-distillation. Sonata is simple and intuitive, yet its learned representations are strong and reliable: zero-shot visualizations demonstrate semantic grouping, alongside strong spatial reasoning through nearest-neighbor relationships. Sonata demonstrates exceptional parameter and data efficiency, tripling linear probing accuracy (from 21.8% to 72.5%) on ScanNet and nearly doubling performance with only 1% of the data compared to previous approaches. Full fine-tuning further advances SOTA across both 3D indoor and outdoor perception tasks.

</details>

### Linguistics-aware Masked Image Modeling for Self-supervised Scene Text Recognition.
- **链接**: [arXiv:2503.18746](https://arxiv.org/abs/2503.18746) · 📚 被引 8
- **作者**: Yifei Zhang, Chang Liu, Jin Wei, Xiaomeng Yang, Yu Zhou, Can Ma et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Information Engineering, Tsinghua University,Department of Automation and BNRist, Lenovo Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text images are unique in their dual nature, encompassing both visual and linguistic information. The visual component encompasses structural and appearance-based features, while the linguistic dimension incorporates contextual and semantic elements. In scenarios with degraded visual quality, linguistic patterns serve as crucial supplements for comprehension, highlighting the necessity of integrating both aspects for robust scene text recognition (STR). Contemporary STR approaches often use language models or semantic reasoning modules to capture linguistic features, typically requiring large-scale annotated datasets. Self-supervised learning, which lacks annotations, presents challenges in disentangling linguistic features related to the global context. Typically, sequence contrastive learning emphasizes the alignment of local features, while masked image modeling (MIM) tends to exploit local structures to reconstruct visual patterns, resulting in limited linguistic knowledge. In this paper, we propose a Linguistics-aware Masked Image Modeling (LMIM) approach, which channels the linguistic information into the decoding process of MIM through a separate branch. Specifically, we design a linguistics alignment module to extract vision-independent features as linguistic guidance using inputs with different visual appearances. As features extend beyond mere visual structures, LMIM must consider the global context to achieve reconstruction. Extensive experiments on various benchmarks quantitatively demonstrate our state-of-the-art performance, and attention visualizations qualitatively show the simultaneous capture of both visual and linguistic information.

</details>

### Positive2Negative: Breaking the Information-Lossy Barrier in Self-Supervised Single Image Denoising.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Positive2Negative_Breaking_the_Information-Lossy_Barrier_in_Self-Supervised_Single_Image_Denoising_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Tong Li, Lizhi Wang, Zhiyuan Xu, Lin Zhu, Wanxuan Lu, Hua Huang
- **🏷️ 机构**: Beijing Institute of Technology,School of Computer Science and Technology, Beijing Normal University,School of Artificial Intelligence, Chinese Academy of Sciences,Aerospace Information Research Institute
- **会议**: CVPR 2025

### Self-Supervised Cross-View Correspondence with Predictive Cycle Consistency.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Baade_Self-Supervised_Cross-View_Correspondence_with_Predictive_Cycle_Consistency_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Alan Baade, Changan Chen
- **🏷️ 机构**: The University of Texas at Austin, Stanford University
- **会议**: CVPR 2025

### Probing the Mid-level Vision Capabilities of Self-Supervised Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Probing_the_Mid-level_Vision_Capabilities_of_Self-Supervised_Learning_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Xuweiyi Chen, Markus Marks, Zezhou Cheng
- **🏷️ 机构**: University of Virginia, California Institute of Technology
- **会议**: CVPR 2025

### ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_ArticulatedGS_Self-supervised_Digital_Twin_Modeling_of_Articulated_Objects_using_3D_CVPR_2025_paper.html) · 📚 被引 13
- **作者**: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu
- **🏷️ 机构**: University of Science and Technology of China, National University of Defense Technology, Shenzhen University
- **会议**: CVPR 2025

### SF2T: Self-supervised Fragment Finetuning of Video-LLMs for Fine-Grained Understanding.
- **链接**: [arXiv:2504.07745](https://arxiv.org/abs/2504.07745) · 📚 被引 3
- **作者**: Yangliu Hu, Zikai Song, Na Feng, Yawei Luo, Junqing Yu, Yi-Ping Phoebe Chen et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Zhejiang University, La Trobe University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video-based Large Language Models (Video-LLMs) have witnessed substantial advancements in recent years, propelled by the advancement in multi-modal LLMs. Although these models have demonstrated proficiency in providing the overall description of videos, they struggle with fine-grained understanding, particularly in aspects such as visual dynamics and video details inquiries. To tackle these shortcomings, we find that fine-tuning Video-LLMs on self-supervised fragment tasks, greatly improve their fine-grained video understanding abilities. Hence we propose two key contributions:(1) Self-Supervised Fragment Fine-Tuning (SF$^2$T), a novel effortless fine-tuning method, employs the rich inherent characteristics of videos for training, while unlocking more fine-grained understanding ability of Video-LLMs. Moreover, it relieves researchers from labor-intensive annotations and smartly circumvents the limitations of natural language, which often fails to capture the complex spatiotemporal variations in videos; (2) A novel benchmark dataset, namely FineVidBench, for rigorously assessing Video-LLMs' performance at both the scene and fragment levels, offering a comprehensive evaluation of their capabilities. We assessed multiple models and validated the effectiveness of SF$^2$T on them. Experimental results reveal that our approach improves their ability to capture and interpret spatiotemporal details.

</details>

### GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding.
- **链接**: [arXiv:2412.13193](https://arxiv.org/abs/2412.13193) · [代码](https://github.com/hustvl/GaussTR) · 📚 被引 9
- **作者**: Haoyi Jiang, Liu Liu, Tianheng Cheng, Xinjie Wang, Tianwei Lin, Zhizhong Su et al.
- **🏷️ 机构**: Huazhong University of Science &#x0026; Technology, Horizon Robotics
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D Semantic Occupancy Prediction is fundamental for spatial understanding, yet existing approaches face challenges in scalability and generalization due to their reliance on extensive labeled data and computationally intensive voxel-wise representations. In this paper, we introduce GaussTR, a novel Gaussian-based Transformer framework that unifies sparse 3D modeling with foundation model alignment through Gaussian representations to advance 3D spatial understanding. GaussTR predicts sparse sets of Gaussians in a feed-forward manner to represent 3D scenes. By splatting the Gaussians into 2D views and aligning the rendered features with foundation models, GaussTR facilitates self-supervised 3D representation learning and enables open-vocabulary semantic occupancy prediction without requiring explicit annotations. Empirical experiments on the Occ3D-nuScenes dataset demonstrate GaussTR's state-of-the-art zero-shot performance of 12.27 mIoU, along with a 40% reduction in training time. These results highlight the efficacy of GaussTR for scalable and holistic 3D spatial understanding, with promising implications in autonomous driving and embodied agents. The code is available at https://github.com/hustvl/GaussTR.

</details>

### AeSPa : Attention-guided Self-supervised Parallel Imaging for MRI Reconstruction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Joo_AeSPa__Attention-guided_Self-supervised_Parallel_Imaging_for_MRI_Reconstruction_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Jinho Joo, Hyeseong Kim, Hyeyeon Won, Deukhee Lee, Taejoon Eo, Dosik Hwang
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2025

### Noise Modeling in One Hour: Minimizing Preparation Efforts for Self-supervised Low-Light RAW Image Denoising.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Noise_Modeling_in_One_Hour_Minimizing_Preparation_Efforts_for_Self-supervised_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Feiran Li, Haiyang Jiang, Daisuke Iso
- **🏷️ 机构**: Tokyo University, Sony Research
- **会议**: CVPR 2025

### AutoSSVH: Exploring Automated Frame Sampling for Efficient Self-Supervised Video Hashing.
- **链接**: [arXiv:2504.03587](https://arxiv.org/abs/2504.03587) · [代码](https://github.com/EliSpectre/CVPR25-AutoSSVH) · 📚 被引 7
- **作者**: Niu Lian, Jun Li, Jinpeng Wang, Ruisheng Luo, Yaowei Wang, Shu-Tao Xia et al.
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, Tsinghua University,Tsinghua Shenzhen International Graduate School, Peng Cheng Laboratory,Research Center of Artificial Intelligence
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Video Hashing (SSVH) compresses videos into hash codes for efficient indexing and retrieval using unlabeled training videos. Existing approaches rely on random frame sampling to learn video features and treat all frames equally. This results in suboptimal hash codes, as it ignores frame-specific information density and reconstruction difficulty. To address this limitation, we propose a new framework, termed AutoSSVH, that employs adversarial frame sampling with hash-based contrastive learning. Our adversarial sampling strategy automatically identifies and selects challenging frames with richer information for reconstruction, enhancing encoding capability. Additionally, we introduce a hash component voting strategy and a point-to-set (P2Set) hash-based contrastive objective, which help capture complex inter-video semantic relationships in the Hamming space and improve the discriminability of learned hash codes. Extensive experiments demonstrate that AutoSSVH achieves superior retrieval efficacy and efficiency compared to state-of-the-art approaches. Code is available at https://github.com/EliSpectre/CVPR25-AutoSSVH.

</details>

### VoteFlow: Enforcing Local Rigidity in Self-Supervised Scene Flow.
- **链接**: [arXiv:2503.22328](https://arxiv.org/abs/2503.22328) · [代码](https://github.com/tudelft-iv/VoteFlow) · 📚 被引 5
- **作者**: Yancong Lin, Shiming Wang, Liangliang Nan, Julian F. P. Kooij, Holger Caesar
- **🏷️ 机构**: TU Delft
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene flow estimation aims to recover per-point motion from two adjacent LiDAR scans. However, in real-world applications such as autonomous driving, points rarely move independently of others, especially for nearby points belonging to the same object, which often share the same motion. Incorporating this locally rigid motion constraint has been a key challenge in self-supervised scene flow estimation, which is often addressed by post-processing or appending extra regularization. While these approaches are able to improve the rigidity of predicted flows, they lack an architectural inductive bias for local rigidity within the model structure, leading to suboptimal learning efficiency and inferior performance. In contrast, we enforce local rigidity with a lightweight add-on module in neural network design, enabling end-to-end learning. We design a discretized voting space that accommodates all possible translations and then identify the one shared by nearby points by differentiable voting. Additionally, to ensure computational efficiency, we operate on pillars rather than points and learn representative features for voting per pillar. We plug the Voting Module into popular model designs and evaluate its benefit on Argoverse 2 and Waymo datasets. We outperform baseline works with only marginal compute overhead. Code is available at https://github.com/tudelft-iv/VoteFlow.

</details>

### Rotation-Equivariant Self-Supervised Method in Image Denoising.
- **链接**: [arXiv:2505.19618](https://arxiv.org/abs/2505.19618) · 📚 被引 6
- **作者**: Hanze Liu, Jiahong Fu, Qi Xie, Deyu Meng
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,Xi&#x2019;an,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised image denoising methods have garnered significant research attention in recent years, for this kind of method reduces the requirement of large training datasets. Compared to supervised methods, self-supervised methods rely more on the prior embedded in deep networks themselves. As a result, most of the self-supervised methods are designed with Convolution Neural Networks (CNNs) architectures, which well capture one of the most important image prior, translation equivariant prior. Inspired by the great success achieved by the introduction of translational equivariance, in this paper, we explore the way to further incorporate another important image prior. Specifically, we first apply high-accuracy rotation equivariant convolution to self-supervised image denoising. Through rigorous theoretical analysis, we have proved that simply replacing all the convolution layers with rotation equivariant convolution layers would modify the network into its rotation equivariant version. To the best of our knowledge, this is the first time that rotation equivariant image prior is introduced to self-supervised image denoising at the network architecture level with a comprehensive theoretical analysis of equivariance errors, which offers a new perspective to the field of self-supervised image denoising. Moreover, to further improve the performance, we design a new mask mechanism to fusion the output of rotation equivariant network and vanilla CNN-based network, and construct an adaptive rotation equivariant framework. Through extensive experiments on three typical methods, we have demonstrated the effectiveness of the proposed method.

</details>

### When the Future Becomes the Past: Taming Temporal Correspondence for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_When_the_Future_Becomes_the_Past_Taming_Temporal_Correspondence_for_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Qingming Huang
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Computer Science and Technology, Institute of Computing Technology,Chinese Academy of Sciences, Institute of Information Engineering,Chinese Academy of Sciences
- **会议**: CVPR 2025

### Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for Large Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Stealthy_Backdoor_Attack_in_Self-Supervised_Learning_Vision_Encoders_for_Large_CVPR_2025_paper.html)
- **作者**: Zhaoyi Liu, Huan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Shading Meets Motion: Self-supervised Indoor 3D Reconstruction Via Simultaneous Shape-from-Shading and Structure-from-Motion.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_Shading_Meets_Motion_Self-supervised_Indoor_3D_Reconstruction_Via_Simultaneous_Shape-from-Shading_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Guoyu Lu
- **🏷️ 机构**: Intelligent Vision and Sensing Lab Binghamton University
- **会议**: CVPR 2025

### SpatialDreamer: Self-supervised Stereo Video Synthesis from Monocular Input.
- **链接**: [arXiv:2411.11934](https://arxiv.org/abs/2411.11934) · 📚 被引 2
- **作者**: Zhen Lv, Yangqi Long, Congzhentao Huang, Cao Li, Chengfei Lv, Hao Ren et al.
- **🏷️ 机构**: Alibaba Group, Sun Yat-sen University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Stereo video synthesis from a monocular input is a demanding task in the fields of spatial computing and virtual reality. The main challenges of this task lie on the insufficiency of high-quality paired stereo videos for training and the difficulty of maintaining the spatio-temporal consistency between frames. Existing methods primarily address these issues by directly applying novel view synthesis (NVS) techniques to video, while facing limitations such as the inability to effectively represent dynamic scenes and the requirement for large amounts of training data. In this paper, we introduce a novel self-supervised stereo video synthesis paradigm via a video diffusion model, termed SpatialDreamer, which meets the challenges head-on. Firstly, to address the stereo video data insufficiency, we propose a Depth based Video Generation module DVG, which employs a forward-backward rendering mechanism to generate paired videos with geometric and temporal priors. Leveraging data generated by DVG, we propose RefinerNet along with a self-supervised synthetic framework designed to facilitate efficient and dedicated training. More importantly, we devise a consistency control module, which consists of a metric of stereo deviation strength and a Temporal Interaction Learning module TIL for geometric and temporal consistency ensurance respectively. We evaluated the proposed method against various benchmark methods, with the results showcasing its superior performance.

</details>

### Generalized Recorrupted-to-Recorrupted: Self-Supervised Learning Beyond Gaussian Noise.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Monroy_Generalized_Recorrupted-to-Recorrupted_Self-Supervised_Learning_Beyond_Gaussian_Noise_CVPR_2025_paper.html) · 📚 被引 9
- **作者**: Brayan Monroy, Jorge Bacca, Julián Tachella
- **🏷️ 机构**: Universidad Industrial de Santander, CNRS &amp; ENS Lyon
- **会议**: CVPR 2025

### Self-supervised ControlNet with Spatio-Temporal Mamba for Real-world Video Super-resolution.
- **链接**: [arXiv:2506.01037](https://arxiv.org/abs/2506.01037) · 📚 被引 5
- **作者**: Shijun Shi, Jing Xu, Lijing Lu, Zhihang Li, Kai Hu
- **🏷️ 机构**: Jiangnan University, University of Science and Technology of China, Peking University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing diffusion-based video super-resolution (VSR) methods are susceptible to introducing complex degradations and noticeable artifacts into high-resolution videos due to their inherent randomness. In this paper, we propose a noise-robust real-world VSR framework by incorporating self-supervised learning and Mamba into pre-trained latent diffusion models. To ensure content consistency across adjacent frames, we enhance the diffusion model with a global spatio-temporal attention mechanism using the Video State-Space block with a 3D Selective Scan module, which reinforces coherence at an affordable computational cost. To further reduce artifacts in generated details, we introduce a self-supervised ControlNet that leverages HR features as guidance and employs contrastive learning to extract degradation-insensitive features from LR videos. Finally, a three-stage training strategy based on a mixture of HR-LR videos is proposed to stabilize VSR training. The proposed Self-supervised ControlNet with Spatio-Temporal Continuous Mamba based VSR algorithm achieves superior perceptual quality than state-of-the-arts on real-world VSR benchmark datasets, validating the effectiveness of the proposed model design and training strategies.

</details>

### Self-Supervised Spatial Correspondence Across Modalities.
- **链接**: [arXiv:2506.03148](https://arxiv.org/abs/2506.03148) · 📚 被引 1
- **作者**: Ayush Shrivastava, Andrew Owens
- **🏷️ 机构**: University of Michigan
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method for finding cross-modal space-time correspondences. Given two images from different visual modalities, such as an RGB image and a depth map, our model identifies which pairs of pixels correspond to the same physical points in the scene. To solve this problem, we extend the contrastive random walk framework to simultaneously learn cycle-consistent feature representations for both cross-modal and intra-modal matching. The resulting model is simple and has no explicit photo-consistency assumptions. It can be trained entirely using unlabeled data, without the need for any spatially aligned multimodal image pairs. We evaluate our method on both geometric and semantic correspondence tasks. For geometric matching, we consider challenging tasks such as RGB-to-depth and RGB-to-thermal matching (and vice versa); for semantic matching, we evaluate on photo-sketch and cross-style image alignment. Our method achieves strong performance across all benchmarks.

</details>

### Common3D: Self-Supervised Learning of 3D Morphable Models for Common Objects in Neural Feature Space.
- **链接**: [arXiv:2504.21749](https://arxiv.org/abs/2504.21749) · 📚 被引 1
- **作者**: Leonhard Sommer, Olaf Dünkel, Christian Theobalt, Adam Kortylewski
- **🏷️ 机构**: University of Freiburg, Max Planck Institute for Informatics
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D morphable models (3DMMs) are a powerful tool to represent the possible shapes and appearances of an object category. Given a single test image, 3DMMs can be used to solve various tasks, such as predicting the 3D shape, pose, semantic correspondence, and instance segmentation of an object. Unfortunately, 3DMMs are only available for very few object categories that are of particular interest, like faces or human bodies, as they require a demanding 3D data acquisition and category-specific training process. In contrast, we introduce a new method, Common3D, that learns 3DMMs of common objects in a fully self-supervised manner from a collection of object-centric videos. For this purpose, our model represents objects as a learned 3D template mesh and a deformation field that is parameterized as an image-conditioned neural network. Different from prior works, Common3D represents the object appearance with neural features instead of RGB colors, which enables the learning of more generalizable representations through an abstraction from pixel intensities. Importantly, we train the appearance features using a contrastive objective by exploiting the correspondences defined through the deformable template mesh. This leads to higher quality correspondence features compared to related works and a significantly improved model performance at estimating 3D object pose and semantic correspondence. Common3D is the first completely self-supervised method that can solve various vision tasks in a zero-shot manner.

</details>

### ONDA-Pose: Occlusion-Aware Neural Domain Adaptation for Self-Supervised 6D Object Pose Estimation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tan_ONDA-Pose_Occlusion-Aware_Neural_Domain_Adaptation_for_Self-Supervised_6D_Object_Pose_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Tao Tan, Qiulei Dong
- **🏷️ 机构**: University of Chinese Academy of Sciences State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA,School of Artificial Intelligence
- **会议**: CVPR 2025

### FSFM: A Generalizable Face Security Foundation Model via Self-Supervised Facial Representation Learning.
- **链接**: [arXiv:2412.12032](https://arxiv.org/abs/2412.12032) · 📚 被引 9
- **作者**: Gaojian Wang, Feng Lin, Tong Wu, Zhenguang Liu, Zhongjie Ba, Kui Ren
- **🏷️ 机构**: Zhejiang University,State Key Laboratory of Blockchain and Data Security
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work asks: with abundant, unlabeled real faces, how to learn a robust and transferable facial representation that boosts various face security tasks with respect to generalization performance? We make the first attempt and propose a self-supervised pretraining framework to learn fundamental representations of real face images, FSFM, that leverages the synergy between masked image modeling (MIM) and instance discrimination (ID). We explore various facial masking strategies for MIM and present a simple yet powerful CRFR-P masking, which explicitly forces the model to capture meaningful intra-region consistency and challenging inter-region coherency. Furthermore, we devise the ID network that naturally couples with MIM to establish underlying local-to-global correspondence via tailored self-distillation. These three learning objectives, namely 3C, empower encoding both local features and global semantics of real faces. After pretraining, a vanilla ViT serves as a universal vision foundation model for downstream face security tasks: cross-dataset deepfake detection, cross-domain face anti-spoofing, and unseen diffusion facial forgery detection. Extensive experiments on 10 public datasets demonstrate that our model transfers better than supervised pretraining, visual and facial self-supervised learning arts, and even outperforms task-specialized SOTA methods.

</details>

### Synthetic-to-Real Self-supervised Robust Depth Estimation via Learning with Motion and Structure Priors.
- **链接**: [arXiv:2503.20211](https://arxiv.org/abs/2503.20211) · 📚 被引 4
- **作者**: Weilong Yan, Ming Li, Haipeng Li, Shuwei Shao, Robby T. Tan
- **🏷️ 机构**: National University of Singapore, Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), University of Electronic Science and Technology of China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised depth estimation from monocular cameras in diverse outdoor conditions, such as daytime, rain, and nighttime, is challenging due to the difficulty of learning universal representations and the severe lack of labeled real-world adverse data. Previous methods either rely on synthetic inputs and pseudo-depth labels or directly apply daytime strategies to adverse conditions, resulting in suboptimal results. In this paper, we present the first synthetic-to-real robust depth estimation framework, incorporating motion and structure priors to capture real-world knowledge effectively. In the synthetic adaptation, we transfer motion-structure knowledge inside cost volumes for better robust representation, using a frozen daytime model to train a depth estimator in synthetic adverse conditions. In the innovative real adaptation, which targets to fix synthetic-real gaps, models trained earlier identify the weather-insensitive regions with a designed consistency-reweighting strategy to emphasize valid pseudo-labels. We introduce a new regularization by gathering explicit depth distributions to constrain the model when facing real-world data. Experiments show that our method outperforms the state-of-the-art across diverse conditions in multi-frame and single-frame evaluations. We achieve improvements of 7.5% and 4.3% in AbsRel and RMSE on average for nuScenes and Robotcar datasets (daytime, nighttime, rain). In zero-shot evaluation of DrivingStereo (rain, fog), our method generalizes better than the previous ones.

</details>

### ImagineFSL: Self-Supervised Pretraining Matters on Imagined Base Set for VLM-based Few-shot Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_ImagineFSL_Self-Supervised_Pretraining_Matters_on_Imagined_Base_Set_for_VLM-based_CVPR_2025_paper.html)
- **作者**: Haoyuan Yang, Xiaoou Li, Jiaming Lv, Xianjun Cheng, Qilong Wang, Peihua Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### TAGA: Self-supervised Learning for Template-free Animatable Gaussian Articulated Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhai_TAGA_Self-supervised_Learning_for_Template-free_Animatable_Gaussian_Articulated_Model_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Zhichao Zhai, Guikun Chen, Wenguan Wang, Dong Zheng, Jun Xiao
- **🏷️ 机构**: Zhejiang University
- **会议**: CVPR 2025

### Invisible Backdoor Attack against Self-supervised Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Invisible_Backdoor_Attack_against_Self-supervised_Learning_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Hanrong Zhang, Zhenting Wang, Boheng Li, Fulin Lin, Tingxu Han, Mingyu Jin et al.
- **🏷️ 机构**: Zhejiang University, Rutgers University, Nanyang Technological University
- **会议**: CVPR 2025

### Anyattack: Towards Large-scale Self-supervised Adversarial Attacks on Vision-language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Anyattack_Towards_Large-scale_Self-supervised_Adversarial_Attacks_on_Vision-language_Models_CVPR_2025_paper.html)
- **作者**: Jiaming Zhang, Junhong Ye, Xingjun Ma, Yige Li, Yunfan Yang, Yunhao Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### From Prototypes to General Distributions: An Efficient Curriculum for Masked Image Modeling.
- **链接**: [arXiv:2411.10685](https://arxiv.org/abs/2411.10685) · 📚 被引 3
- **作者**: Jinhong Lin, Cheng-En Wu, Huanran Li, Jifan Zhang, Yu Hen Hu, Pedro Morgado
- **🏷️ 机构**: University of Wisconsin&#x2013;Madison
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Image Modeling (MIM) has emerged as a powerful self-supervised learning paradigm for visual representation learning, enabling models to acquire rich visual representations by predicting masked portions of images from their visible regions. While this approach has shown promising results, we hypothesize that its effectiveness may be limited by optimization challenges during early training stages, where models are expected to learn complex image distributions from partial observations before developing basic visual processing capabilities. To address this limitation, we propose a prototype-driven curriculum leagrning framework that structures the learning process to progress from prototypical examples to more complex variations in the dataset. Our approach introduces a temperature-based annealing scheme that gradually expands the training distribution, enabling more stable and efficient learning trajectories. Through extensive experiments on ImageNet-1K, we demonstrate that our curriculum learning strategy significantly improves both training efficiency and representation quality while requiring substantially fewer training epochs compared to standard Masked Auto-Encoding. Our findings suggest that carefully controlling the order of training examples plays a crucial role in self-supervised visual learning, providing a practical solution to the early-stage optimization challenges in MIM.

</details>

## 跨领域论文（完整笔记在其他领域）

- AVF-MAE++: Scaling Affective Video Facial Masked Autoencoders via Efficient Audio-Visual Self-Supervised Learning. → [multimodal](../multimodal/Guideline%202025.md)
- Large Self-Supervised Models Bridge the Gap in Domain Adaptive Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Learning from Synchronization: Self-Supervised Uncalibrated Multi-View Person Association in Challenging Scenes. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Enhanced Contrastive Learning with Multi-view Longitudinal Data for Chest X-ray Report Generation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- GeoDepth: From Point-to-Depth to Plane-to-Depth Modeling for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- S4-Driver: Scalable Self-Supervised Driving Multimodal Large Language Model with Spatio-Temporal Visual Representation. → [multimodal](../multimodal/Guideline%202025.md)
