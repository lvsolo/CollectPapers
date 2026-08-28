# Self-supervised Vision — 2025 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 54 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Temporal Overlapping Prediction: A Self-Supervised Pre-Training Method for LiDAR Moving Object Segmentation.
- **链接**: [arXiv:2503.07167](https://arxiv.org/abs/2503.07167) · 📚 被引 1
- **作者**: Ziliang Miao, Runjian Chen, Yixi Cai, Buwei He, Wenquan Zhao, Wenqi Shao et al.
- **🏷️ 机构**: The University of Hong Kong, KTH Royal Institute of Technology, Southern University of Science and Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Moving object segmentation (MOS) on LiDAR point clouds is crucial for autonomous systems like self-driving vehicles. Previous supervised approaches rely heavily on costly manual annotations, while LiDAR sequences naturally capture temporal motion cues that can be leveraged for self-supervised learning. In this paper, we propose Temporal Overlapping Prediction (TOP), a self-supervised pre-training method that alleviate the labeling burden for MOS. TOP explores the temporal overlapping points that commonly observed by current and adjacent scans, and learns spatiotemporal representations by predicting the occupancy states of temporal overlapping points. Moreover, we utilize current occupancy reconstruction as an auxiliary pre-training objective, which enhances the current structural awareness of the model. We conduct extensive experiments and observe that the conventional metric Intersection-over-Union (IoU) shows strong bias to objects with more scanned points, which might neglect small or distant objects. To compensate for this bias, we introduce an additional metric called mIoU_obj to evaluate object-level performance. Experiments on nuScenes and SemanticKITTI show that TOPoutperforms both supervised training-from-scratch baseline and other self-supervised pre-training baselines by up to 28.77% relative improvement, demonstrating strong transferability across LiDAR setups and generalization to other tasks. Code and pre-trained models will be publicly available upon publication.

</details>

### ASCENT: Annotation-Free Self-Supervised Contrastive Embeddings for 3D Neuron Tracking in Fluorescence Microscopy.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01362) · 📚 被引 1
- **作者**: Haejun Han, Hang Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### T-REGS: Minimum Spanning Tree Regularization for Self-Supervised Learning.
- **链接**: [arXiv:2510.23484](https://arxiv.org/abs/2510.23484) · 📚 被引 0
- **作者**: Julie Mordacq, David Loiseaux, Vicky Kalogeiton, Steve Oudot
- **🏷️ 机构**: Inria Saclay, Ecole Polytechnique, Lawrence Berkeley National Lab, Ecole polytechnique, IP Paris
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked autoencoders (MAE) have shown tremendous potential for self-supervised learning (SSL) in vision and beyond. However, point clouds from LiDARs used in automated driving are particularly challenging for MAEs since large areas of the 3D volume are empty. Consequently, existing work suffers from leaking occupancy information into the decoder and has significant computational complexity, thereby limiting the SSL pre-training to only 2D bird's eye view encoders in practice. In this work, we propose the novel neighborhood occupancy MAE (NOMAE) that overcomes the aforementioned challenges by employing masked occupancy reconstruction only in the neighborhood of non-masked voxels. We incorporate voxel masking and occupancy reconstruction at multiple scales with our proposed hierarchical mask generation technique to capture features of objects of different sizes in the point cloud. NOMAEs are extremely flexible and can be directly employed for SSL in existing 3D architectures. We perform extensive evaluations on the nuScenes and Waymo Open datasets for the downstream perception tasks of semantic segmentation and 3D object detection, comparing with both discriminative and generative SSL methods. The results demonstrate that NOMAE sets the new state-of-the-art on multiple benchmarks for multiple point cloud perception tasks.

</details>

### ShapeEmbed: a self-supervised learning framework for 2D contour quantification.
- **链接**: [arXiv:2507.01009](https://arxiv.org/abs/2507.01009) · 📚 被引 0
- **作者**: Anna Foix Romero, Craig Russell, Alexander Krull, Virginie Uhlmann
- **🏷️ 机构**: EMBL's European Bioinformatics Institute, European Bioinformatics Institute - EMBL, Birmingham University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) on 3D point clouds has the potential to learn feature representations that can transfer to diverse sensors and multiple downstream perception tasks. However, recent SSL approaches fail to define pretext tasks that retain geometric information such as object pose and scale, which can be detrimental to the performance of downstream localization and geometry-sensitive 3D scene understanding tasks, such as 3D semantic segmentation and 3D object detection. We propose PSA-SSL, a novel extension to point cloud SSL that learns object pose and size-aware (PSA) features. Our approach defines a self-supervised bounding box regression pretext task, which retains object pose and size information. Furthermore, we incorporate LiDAR beam pattern augmentation on input point clouds, which encourages learning sensor-agnostic features. Our experiments demonstrate that with a single pretrained model, our light-weight yet effective extensions achieve significant improvements on 3D semantic segmentation with limited labels across popular autonomous driving datasets (Waymo, nuScenes, SemanticKITTI). Moreover, our approach outperforms other state-of-the-art SSL methods on 3D semantic segmentation (using up to 10 times less labels), as well as on 3D object detection. Our code will be released on https://github.com/TRAILab/PSA-SSL.

</details>

### Not All Data are Good Labels: On the Self-supervised Labeling for Time Series Forecasting.
- **链接**: [arXiv:2502.14704](https://arxiv.org/abs/2502.14704) · 📚 被引 0
- **作者**: Yuxuan Yang, Dalin Zhang, Yuxuan Liang, Hua Lu, Gang Chen, Huan Li
- **🏷️ 机构**: Zhejiang University, Hangzhou Dianzi University, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: NeurIPS 2025

### Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks.
- **链接**: [arXiv:2509.17174](https://arxiv.org/abs/2509.17174) · 📚 被引 0
- **作者**: Kijung Yoon
- **🏷️ 机构**: Hanyang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point cloud completion helps restore partial incomplete point clouds suffering occlusions. Current self-supervised methods fail to give high fidelity completion for large objects with missing surfaces and unbalanced distribution of available points. In this paper, we present a novel method for restoring large-scale point clouds with limited and imbalanced ground-truth. Using rough boundary annotations for a region of interest, we project the original point clouds into a multiple-center-of-projection (MCOP) image, where fragments are projected to images of 5 channels (RGB, depth, and rotation). Completion of the original point cloud is reduced to inpainting the missing pixels in the MCOP images. Due to lack of complete structures and an unbalanced distribution of existing parts, we develop a self-supervised scheme which learns to infill the MCOP image with points resembling existing "complete" patches. Special losses are applied to further enhance the regularity and consistency of completed MCOP images, which is mapped back to 3D to form final restoration. Extensive experiments demonstrate the superiority of our method in completing 600+ incomplete and unbalanced archaeological structures in Peru.

</details>

### On-Device Self-Supervised Learning of Low-Latency Monocular Depth from Only Events.
- **链接**: [arXiv:2412.06359](https://arxiv.org/abs/2412.06359) · 📚 被引 1
- **作者**: Jesse J. Hagenaars, Yilun Wu, Federico Paredes-Vallés, Stein Stroobants, Guido C. H. E. de Croon
- **🏷️ 机构**: MAVLab, TU Delft, EUISPC, Sony Semiconductor Solutions Europe, Sony Europe B.V
- **会议**: CVPR 2025

### CellCLIP - Learning Perturbation Effects in Cell Painting via Text-Guided Contrastive Learning.
- **链接**: [arXiv:2506.06290](https://arxiv.org/abs/2506.06290) · 📚 被引 0
- **作者**: Mingyu Lu, Ethan Weinberger, Chanwoo Kim, Su-In Lee
- **🏷️ 机构**: University of Washington
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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
- **链接**: [arXiv:2412.16460](https://arxiv.org/abs/2412.16460) · [代码](https://github.com/Li-Tong-621/P2N) · 📚 被引 5
- **作者**: Tong Li, Lizhi Wang, Zhiyuan Xu, Lin Zhu, Wanxuan Lu, Hua Huang
- **🏷️ 机构**: Beijing Institute of Technology,School of Computer Science and Technology, Beijing Normal University,School of Artificial Intelligence, Chinese Academy of Sciences,Aerospace Information Research Institute
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image denoising enhances image quality, serving as a foundational technique across various computational photography applications. The obstacle to clean image acquisition in real scenarios necessitates the development of self-supervised image denoising methods only depending on noisy images, especially a single noisy image. Existing self-supervised image denoising paradigms (Noise2Noise and Noise2Void) rely heavily on information-lossy operations, such as downsampling and masking, culminating in low quality denoising performance. In this paper, we propose a novel self-supervised single image denoising paradigm, Positive2Negative, to break the information-lossy barrier. Our paradigm involves two key steps: Renoised Data Construction (RDC) and Denoised Consistency Supervision (DCS). RDC renoises the predicted denoised image by the predicted noise to construct multiple noisy images, preserving all the information of the original image. DCS ensures consistency across the multiple denoised images, supervising the network to learn robust denoising. Our Positive2Negative paradigm achieves state-of-the-art performance in self-supervised single image denoising with significant speed improvements. The code is released to the public at https://github.com/Li-Tong-621/P2N.

</details>

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

> We introduce a novel approach for simultaneous self-supervised video alignment and action segmentation based on a unified optimal transport framework. In particular, we first tackle self-supervised video alignment by developing a fused Gromov-Wasserstein optimal transport formulation with a structural prior, which trains efficiently on GPUs and needs only a few iterations for solving the optimal transport problem. Our single-task method achieves the state-of-the-art performance on multiple video alignment benchmarks and outperforms VAVA, which relies on a traditional Kantorovich optimal transport formulation with an optimality prior. Furthermore, we extend our approach by proposing a unified optimal transport framework for joint self-supervised video alignment and action segmentation, which requires training and storing a single model and saves both time and memory consumption as compared to two different single-task models. Extensive evaluations on several video alignment and action segmentation datasets demonstrate that our multi-task method achieves comparable video alignment yet superior action segmentation results over previous methods in video alignment and action segmentation respectively. Finally, to the best of our knowledge, this is the first work to unify video alignment and action segmentation into a single model. Our code is available on our research website: https://retrocausal.ai/research/.

</details>

### AIM: Amending Inherent Interpretability via Self-Supervised Masking.
- **链接**: [arXiv:2508.11502](https://arxiv.org/abs/2508.11502) · 📚 被引 0
- **作者**: Eyad Alshami, Shashank Agnihotri, Bernt Schiele, Margret Keuper
- **🏷️ 机构**: Max-Planck-Institute for Informatics, Saarland Informatics Campus,Germany, Data and Web Science Group, University of Mannheim,Germany
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It has been observed that deep neural networks (DNNs) often use both genuine as well as spurious features. In this work, we propose "Amending Inherent Interpretability via Self-Supervised Masking" (AIM), a simple yet interestingly effective method that promotes the network's utilization of genuine features over spurious alternatives without requiring additional annotations. In particular, AIM uses features at multiple encoding stages to guide a self-supervised, sample-specific feature-masking process. As a result, AIM enables the training of well-performing and inherently interpretable models that faithfully summarize the decision process. We validate AIM across a diverse range of challenging datasets that test both out-of-distribution generalization and fine-grained visual understanding. These include general-purpose classification benchmarks such as ImageNet100, HardImageNet, and ImageWoof, as well as fine-grained classification datasets such as Waterbirds, TravelingBirds, and CUB-200. AIM demonstrates significant dual benefits: interpretability improvements, as measured by the Energy Pointing Game (EPG) score, and accuracy gains over strong baselines. These consistent gains across domains and architectures provide compelling evidence that AIM promotes the use of genuine and meaningful features that directly contribute to improved generalization and human-aligned interpretability.

</details>

### Progressor: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement.
- **链接**: [arXiv:2411.17764](https://arxiv.org/abs/2411.17764) · 📚 被引 0
- **作者**: Tewodros W. Ayalew, Xiao Zhang, Kevin Yuanbo Wu, Tianchong Jiang, Michael Maire, Matthew R. Walter
- **🏷️ 机构**: University of Chicago,USA, Toyota Technological Institute at Chicago,USA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present PROGRESSOR, a novel framework that learns a task-agnostic reward function from videos, enabling policy training through goal-conditioned reinforcement learning (RL) without manual supervision. Underlying this reward is an estimate of the distribution over task progress as a function of the current, initial, and goal observations that is learned in a self-supervised fashion. Crucially, PROGRESSOR refines rewards adversarially during online RL training by pushing back predictions for out-of-distribution observations, to mitigate distribution shift inherent in non-expert observations. Utilizing this progress prediction as a dense reward together with an adversarial push-back, we show that PROGRESSOR enables robots to learn complex behaviors without any external supervision. Pretrained on large-scale egocentric human video from EPIC-KITCHENS, PROGRESSOR requires no fine-tuning on in-domain task-specific data for generalization to real-robot offline RL under noisy demonstrations, outperforming contemporary methods that provide dense visual reward for robotic learning. Our findings highlight the potential of PROGRESSOR for scalable robotic applications where direct action labels and task-specific rewards are not readily available.

</details>

### Adversarial Robustness of Discriminative Self-Supervised Learning in Vision.
- **链接**: [arXiv:2503.06361](https://arxiv.org/abs/2503.06361) · 📚 被引 0
- **作者**: Ömer Veysel Çagatan, Ömer Faruk Tal, M. Emre Gürsoy
- **🏷️ 机构**: Ko&#x00E7; University,Department of Computer Engineering
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has advanced significantly in visual representation learning, yet comprehensive evaluations of its adversarial robustness remain limited. In this study, we evaluate the adversarial robustness of seven discriminative self-supervised models and one supervised model across diverse tasks, including ImageNet classification, transfer learning, segmentation, and detection. Our findings suggest that discriminative SSL models generally exhibit better robustness to adversarial attacks compared to their supervised counterpart on ImageNet, with this advantage extending to transfer learning when using linear evaluation. However, when fine-tuning is applied, the robustness gap between SSL and supervised models narrows considerably. Similarly, this robustness advantage diminishes in segmentation and detection tasks. We also investigate how various factors might influence adversarial robustness, including architectural choices, training duration, data augmentations, and batch sizes. Our analysis contributes to the ongoing exploration of adversarial robustness in visual self-supervised representation systems.

</details>

### Backdooring Self-Supervised Contrastive Learning by Noisy Alignment.
- **链接**: [arXiv:2508.14015](https://arxiv.org/abs/2508.14015) · [代码](https://github.com/jsrdcht/Noisy-Alignment) · 📚 被引 1
- **作者**: Tuo Chen, Jie Gui, Minjing Dong, Ju Jia, Lanting Fang, Jian Liu
- **🏷️ 机构**: Southeast University, City University of Hong Kong, Beijing Institute of Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised contrastive learning (CL) effectively learns transferable representations from unlabeled data containing images or image-text pairs but suffers vulnerability to data poisoning backdoor attacks (DPCLs). An adversary can inject poisoned images into pretraining datasets, causing compromised CL encoders to exhibit targeted misbehavior in downstream tasks. Existing DPCLs, however, achieve limited efficacy due to their dependence on fragile implicit co-occurrence between backdoor and target object and inadequate suppression of discriminative features in backdoored images. We propose Noisy Alignment (NA), a DPCL method that explicitly suppresses noise components in poisoned images. Inspired by powerful training-controllable CL attacks, we identify and extract the critical objective of noisy alignment, adapting it effectively into data-poisoning scenarios. Our method implements noisy alignment by strategically manipulating contrastive learning's random cropping mechanism, formulating this process as an image layout optimization problem with theoretically derived optimal parameters. The resulting method is simple yet effective, achieving state-of-the-art performance compared to existing DPCLs, while maintaining clean-data accuracy. Furthermore, Noisy Alignment demonstrates robustness against common backdoor defenses. Codes can be found at https://github.com/jsrdcht/Noisy-Alignment.

</details>

### DASH: 4D Hash Encoding with Self-Supervised Decomposition for Real-Time Dynamic Scene Rendering.
- **链接**: [arXiv:2507.19141](https://arxiv.org/abs/2507.19141) · [代码](https://github.com/chenj02/DASH) · 📚 被引 0
- **作者**: Jie Chen, Zhangchi Hu, Peixi Wu, Huyue Zhu, Hebei Li, Xiaoyan Sun
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dynamic scene reconstruction is a long-term challenge in 3D vision. Existing plane-based methods in dynamic Gaussian splatting suffer from an unsuitable low-rank assumption, causing feature overlap and poor rendering quality. Although 4D hash encoding provides an explicit representation without low-rank constraints, directly applying it to the entire dynamic scene leads to substantial hash collisions and redundancy. To address these challenges, we present DASH, a real-time dynamic scene rendering framework that employs 4D hash encoding coupled with self-supervised decomposition. Our approach begins with a self-supervised decomposition mechanism that separates dynamic and static components without manual annotations or precomputed masks. Next, we introduce a multiresolution 4D hash encoder for dynamic elements, providing an explicit representation that avoids the low-rank assumption. Finally, we present a spatio-temporal smoothness regularization strategy to mitigate unstable deformation artifacts. Experiments on real-world datasets demonstrate that DASH achieves state-of-the-art dynamic rendering performance, exhibiting enhanced visual quality at real-time speeds of 264 FPS on a single 4090 GPU. Code: https://github.com/chenj02/DASH.

</details>

### SAMora: Enhancing SAM through Hierarchical Self-Supervised Pre-Training for Medical Images.
- **链接**: [arXiv:2511.08626](https://arxiv.org/abs/2511.08626) · [代码](https://github.com/ShChen233/SAMora) · 📚 被引 1
- **作者**: Shuhang Chen, Hangjie Yuan, Pengwei Liu, Hanxue Gu, Tao Feng, Dong Ni
- **🏷️ 机构**: Zhejiang University, Duke University, Tsinghua University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Segment Anything Model (SAM) has demonstrated significant potential in medical image segmentation. Yet, its performance is limited when only a small amount of labeled data is available, while there is abundant valuable yet often overlooked hierarchical information in medical data. To address this limitation, we draw inspiration from self-supervised learning and propose SAMora, an innovative framework that captures hierarchical medical knowledge by applying complementary self-supervised learning objectives at the image, patch, and pixel levels. To fully exploit the complementarity of hierarchical knowledge within LoRAs, we introduce HL-Attn, a hierarchical fusion module that integrates multi-scale features while maintaining their distinct characteristics. SAMora is compatible with various SAM variants, including SAM2, SAMed, and H-SAM. Experimental results on the Synapse, LA, and PROMISE12 datasets demonstrate that SAMora outperforms existing SAM variants. It achieves state-of-the-art performance in both few-shot and fully supervised settings while reducing fine-tuning epochs by 90%. The code is available at https://github.com/ShChen233/SAMora.

</details>

### USP: Unified Self-Supervised Pretraining for Image Generation and Understanding.
- **链接**: [arXiv:2503.06132](https://arxiv.org/abs/2503.06132) · [代码](https://github.com/AMAP-ML/USP) · 📚 被引 3
- **作者**: Xiangxiang Chu, Renda Li, Yong Wang
- **🏷️ 机构**: AMAP, Alibaba Group
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have highlighted the interplay between diffusion models and representation learning. Intermediate representations from diffusion models can be leveraged for downstream visual tasks, while self-supervised vision models can enhance the convergence and generation quality of diffusion models. However, transferring pretrained weights from vision models to diffusion models is challenging due to input mismatches and the use of latent spaces. To address these challenges, we propose Unified Self-supervised Pretraining (USP), a framework that initializes diffusion models via masked latent modeling in a Variational Autoencoder (VAE) latent space. USP achieves comparable performance in understanding tasks while significantly improving the convergence speed and generation quality of diffusion models. Our code will be publicly available at https://github.com/AMAP-ML/USP.

</details>

### Embodied Image Captioning: Self-Supervised Learning Agents for Spatially Coherent Image Descriptions.
- **链接**: [arXiv:2504.08531](https://arxiv.org/abs/2504.08531) · 📚 被引 0
- **作者**: Tommaso Galliena, Tommaso Apicella, Stefano Rosa, Pietro Morerio, Alessio Del Bue, Lorenzo Natale
- **🏷️ 机构**: Istituto Italiano di Tecnologia,Genoa,Italy
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a self-supervised method to improve an agent's abilities in describing arbitrary objects while actively exploring a generic environment. This is a challenging problem, as current models struggle to obtain coherent image captions due to different camera viewpoints and clutter. We propose a three-phase framework to fine-tune existing captioning models that enhances caption accuracy and consistency across views via a consensus mechanism. First, an agent explores the environment, collecting noisy image-caption pairs. Then, a consistent pseudo-caption for each object instance is distilled via consensus using a large language model. Finally, these pseudo-captions are used to fine-tune an off-the-shelf captioning model, with the addition of contrastive learning. We analyse the performance of the combination of captioning models, exploration policies, pseudo-labeling methods, and fine-tuning strategies, on our manually labeled test set. Results show that a policy can be trained to mine samples with higher disagreement compared to classical baselines. Our pseudo-captioning method, in combination with all policies, has a higher semantic similarity compared to other existing methods, and fine-tuning improves caption accuracy and consistency by a significant margin. Code and test set annotations available at https://hsp-iit.github.io/embodied-captioning/

</details>

### Self-Supervised Learning of Hybrid Part-Aware 3D Representations of 2D Gaussians and Superquadrics.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00900) · 📚 被引 4
- **作者**: Zhirui Gao, Renjiao Yi, Yuhang Huang, Wei Chen, Chenyang Zhu, Kai Xu
- **🏷️ 机构**: National University of Defense Technology
- **会议**: ICCV 2025

### No Pose at All: Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views.
- **链接**: [arXiv:2508.01171](https://arxiv.org/abs/2508.01171) · 📚 被引 3
- **作者**: Ranran Huang, Krystian Mikolajczyk
- **🏷️ 机构**: Imperial College London
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce SPFSplat, an efficient framework for 3D Gaussian splatting from sparse multi-view images, requiring no ground-truth poses during training or inference. It employs a shared feature extraction backbone, enabling simultaneous prediction of 3D Gaussian primitives and camera poses in a canonical space from unposed inputs within a single feed-forward step. Alongside the rendering loss based on estimated novel-view poses, a reprojection loss is integrated to enforce the learning of pixel-aligned Gaussian primitives for enhanced geometric constraints. This pose-free training paradigm and efficient one-step feed-forward design make SPFSplat well-suited for practical applications. Remarkably, despite the absence of pose supervision, SPFSplat achieves state-of-the-art performance in novel view synthesis even under significant viewpoint changes and limited image overlap. It also surpasses recent methods trained with geometry priors in relative pose estimation. Code and trained models are available on our project page: https://ranrhuang.github.io/spfsplat/.

</details>

### Rayzer: a Self-Supervised Large View Synthesis Model.
- **链接**: [arXiv:2505.00702](https://arxiv.org/abs/2505.00702) · 📚 被引 4
- **作者**: Hanwen Jiang, Hao Tan, Peng Wang, Hai Jin, Yue Zhao, Sai Bi et al.
- **🏷️ 机构**: The University of Texas at Austin, Adobe Research, Cornell University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present RayZer, a self-supervised multi-view 3D Vision model trained without any 3D supervision, i.e., camera poses and scene geometry, while exhibiting emerging 3D awareness. Concretely, RayZer takes unposed and uncalibrated images as input, recovers camera parameters, reconstructs a scene representation, and synthesizes novel views. During training, RayZer relies solely on its self-predicted camera poses to render target views, eliminating the need for any ground-truth camera annotations and allowing RayZer to be trained with 2D image supervision. The emerging 3D awareness of RayZer is attributed to two key factors. First, we design a self-supervised framework, which achieves 3D-aware auto-encoding of input images by disentangling camera and scene representations. Second, we design a transformer-based model in which the only 3D prior is the ray structure, connecting camera, pixel, and scene simultaneously. RayZer demonstrates comparable or even superior novel view synthesis performance than ``oracle'' methods that rely on pose annotations in both training and testing. Project: https://hwjiang1510.github.io/RayZer/

</details>

### Blind2Sound: Self-Supervised Image Denoising Without Residual Noise.
- **链接**: [arXiv:2303.05183](https://arxiv.org/abs/2303.05183) · 📚 被引 0
- **作者**: Jiazheng Liu, Zejin Wang, Bohao Chen, Hua Han
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Brain Cognition and Brain-inspired Intelligence Technology,Beijing,China, School of Advanced Interdisciplinary Sciences, University of Chinese Academy of Sciences,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised blind denoising for Poisson-Gaussian noise remains a challenging task. Pseudo-supervised pairs constructed from single noisy images re-corrupt the signal and degrade the performance. The visible blindspots solve the information loss in masked inputs. However, without explicitly noise sensing, mean square error as an objective function cannot adjust denoising intensities for dynamic noise levels, leading to noticeable residual noise. In this paper, we propose Blind2Sound, a simple yet effective approach to overcome residual noise in denoised images. The proposed adaptive re-visible loss senses noise levels and performs personalized denoising without noise residues while retaining the signal lossless. The theoretical analysis of intermediate medium gradients guarantees stable training, while the Cramer Gaussian loss acts as a regularization to facilitate the accurate perception of noise levels and improve the performance of the denoiser. Experiments on synthetic and real-world datasets show the superior performance of our method, especially for single-channel images.

</details>

### CoSMIC: Continual Self-Supervised Learning for Multi-Domain Medical Imaging Via Conditional Mutual Information Maximization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02140) · 📚 被引 0
- **作者**: Yihang Liu, Ying Wen, Longzhen Yang, Lianghua He, Heng Tao Shen
- **🏷️ 机构**: Tongji University, East China Normal University
- **会议**: ICCV 2025

### TESPEC: Temporally-Enhanced Self-Supervised Pretraining for Event Cameras.
- **链接**: [arXiv:2508.00913](https://arxiv.org/abs/2508.00913) · 📚 被引 1
- **作者**: Mohammad Mohammadi, Ziyi Wu, Igor Gilitschenski
- **🏷️ 机构**: University of Toronto
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-term temporal information is crucial for event-based perception tasks, as raw events only encode pixel brightness changes. Recent works show that when trained from scratch, recurrent models achieve better results than feedforward models in these tasks. However, when leveraging self-supervised pre-trained weights, feedforward models can outperform their recurrent counterparts. Current self-supervised learning (SSL) methods for event-based pre-training largely mimic RGB image-based approaches. They pre-train feedforward models on raw events within a short time interval, ignoring the temporal information of events. In this work, we introduce TESPEC, a self-supervised pre-training framework tailored for learning spatio-temporal information. TESPEC is well-suited for recurrent models, as it is the first framework to leverage long event sequences during pre-training. TESPEC employs the masked image modeling paradigm with a new reconstruction target. We design a novel method to accumulate events into pseudo grayscale videos containing high-level semantic information about the underlying scene, which is robust to sensor noise and reduces motion blur. Reconstructing this target thus requires the model to reason about long-term history of events. Extensive experiments demonstrate our state-of-the-art results in downstream tasks, including object detection, semantic segmentation, and monocular depth estimation. Project webpage: https://mhdmohammadi.github.io/TESPEC_webpage.

</details>

### Self-Supervised Sparse Sensor Fusion for Long Range Perception.
- **链接**: [arXiv:2508.13995](https://arxiv.org/abs/2508.13995) · 📚 被引 2
- **作者**: Edoardo Palladin, Samuel Brucker, Filippo Ghilotti, Praveen Narayanan, Mario Bijelic, Felix Heide
- **🏷️ 机构**: Torc Robotics
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Outside of urban hubs, autonomous cars and trucks have to master driving on intercity highways. Safe, long-distance highway travel at speeds exceeding 100 km/h demands perception distances of at least 250 m, which is about five times the 50-100m typically addressed in city driving, to allow sufficient planning and braking margins. Increasing the perception ranges also allows to extend autonomy from light two-ton passenger vehicles to large-scale forty-ton trucks, which need a longer planning horizon due to their high inertia. However, most existing perception approaches focus on shorter ranges and rely on Bird's Eye View (BEV) representations, which incur quadratic increases in memory and compute costs as distance grows. To overcome this limitation, we built on top of a sparse representation and introduced an efficient 3D encoding of multi-modal and temporal features, along with a novel self-supervised pre-training scheme that enables large-scale learning from unlabeled camera-LiDAR data. Our approach extends perception distances to 250 meters and achieves an 26.6% improvement in mAP in object detection and a decrease of 30.5% in Chamfer Distance in LiDAR forecasting compared to existing methods, reaching distances up to 250 meters. Project Page: https://light.princeton.edu/lrs4fusion/

</details>

### Structure-Aware Semantic Discrepancy and Consistency for 3D Medical Image Self-Supervised Learning.
- **链接**: [arXiv:2507.02581](https://arxiv.org/abs/2507.02581) · 📚 被引 3
- **作者**: Tan Pan, Zhaorui Tan, Kaiyu Guo, Dongli Xu, Weidi Xu, Chen Jiang et al.
- **🏷️ 机构**: AI3, Fudan University, Shanghai Academy of Artificial Intelligence for Science, The University of Queensland
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D medical image self-supervised learning (mSSL) holds great promise for medical analysis. Effectively supporting broader applications requires considering anatomical structure variations in location, scale, and morphology, which are crucial for capturing meaningful distinctions. However, previous mSSL methods partition images with fixed-size patches, often ignoring the structure variations. In this work, we introduce a novel perspective on 3D medical images with the goal of learning structure-aware representations. We assume that patches within the same structure share the same semantics (semantic consistency) while those from different structures exhibit distinct semantics (semantic discrepancy). Based on this assumption, we propose an mSSL framework named $S^2DC$, achieving Structure-aware Semantic Discrepancy and Consistency in two steps. First, $S^2DC$ enforces distinct representations for different patches to increase semantic discrepancy by leveraging an optimal transport strategy. Second, $S^2DC$ advances semantic consistency at the structural level based on neighborhood similarity distribution. By bridging patch-level and structure-level representations, $S^2DC$ achieves structure-aware representations. Thoroughly evaluated across 10 datasets, 4 tasks, and 3 modalities, our proposed method consistently outperforms the state-of-the-art methods in mSSL.

</details>

### Mosic: Optimal-Transport Motion Trajectory for Dense Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00617) · 📚 被引 0
- **作者**: Mohammadreza Salehi, Shashanka Venkataramanan, Ioana Simion, Efstratios Gavves, Cees G. M. Snoek, Yuki M. Asano
- **🏷️ 机构**: VIS Lab, UvA, Valeo.ai, Fundamental AI Lab, UTN
- **会议**: ICCV 2025

### SHeaP: Self-Supervised Head Geometry Predictor Learned via 2D Gaussians.
- **链接**: [arXiv:2504.12292](https://arxiv.org/abs/2504.12292) · 📚 被引 3
- **作者**: Liam Schoneveld, Zhe Chen, Davide Davoli, Jiapeng Tang, Saimon Terazawa, Ko Nishino et al.
- **🏷️ 机构**: Woven by Toyota, Toyota Motor Europe NV/SA associated partner by contracted service, Technical University of Munich
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate, real-time 3D reconstruction of human heads from monocular images and videos underlies numerous visual applications. As 3D ground truth data is hard to come by at scale, previous methods have sought to learn from abundant 2D videos in a self-supervised manner. Typically, this involves the use of differentiable mesh rendering, which is effective but faces limitations. To improve on this, we propose SHeaP (Self-supervised Head Geometry Predictor Learned via 2D Gaussians). Given a source image, we predict a 3DMM mesh and a set of Gaussians that are rigged to this mesh. We then reanimate this rigged head avatar to match a target frame, and backpropagate photometric losses to both the 3DMM and Gaussian prediction networks. We find that using Gaussians for rendering substantially improves the effectiveness of this self-supervised approach. Training solely on 2D data, our method surpasses existing self-supervised approaches in geometric evaluations on the NoW benchmark for neutral faces and a new benchmark for non-neutral expressions. Our method also produces highly expressive meshes, outperforming state-of-the-art in emotion classification.

</details>

### Prototype-Based Contrastive Learning with Stage-Wise Progressive Augmentation for Self-Supervised Fine-Grained Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00393) · 📚 被引 2
- **作者**: Baofeng Tan, Xiu-Shen Wei, Lin Zhao
- **🏷️ 机构**: School of Computer Science and Engineering, Nanjing University of Science and Technology, School of Computer Science and Engineering, Southeast University,Key Laboratory of New Generation Artificial Intelligence Technology and Its Interdisciplinary Applications
- **会议**: ICCV 2025

### An OpenMind for 3D Medical Vision Self-supervised Learning.
- **链接**: [arXiv:2412.17041](https://arxiv.org/abs/2412.17041) · 📚 被引 5
- **作者**: Tassilo Wald, Constantin Ulrich, Jonathan Suprijadi, Sebastian Ziegler, Michal Nohel, Robin Peretzke et al.
- **🏷️ 机构**: German Cancer Research Center (DKFZ),Division of Medical Image Computing,Heidelberg,Germany, Brno University of Technology,Faculty of Electrical Engineering and Communication,Czech Republic
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of self-supervised learning (SSL) for 3D medical images lacks consistency and standardization. While many methods have been developed, it is impossible to identify the current state-of-the-art, due to i) varying and small pretraining datasets, ii) varying architectures, and iii) being evaluated on differing downstream datasets. In this paper, we bring clarity to this field and lay the foundation for further method advancements through three key contributions: We a) publish the largest publicly available pre-training dataset comprising 114k 3D brain MRI volumes, enabling all practitioners to pre-train on a large-scale dataset. We b) benchmark existing 3D self-supervised learning methods on this dataset for a state-of-the-art CNN and Transformer architecture, clarifying the state of 3D SSL pre-training. Among many findings, we show that pre-trained methods can exceed a strong from-scratch nnU-Net ResEnc-L baseline. Lastly, we c) publish the code of our pre-training and fine-tuning frameworks and provide the pre-trained models created during the benchmarking process to facilitate rapid adoption and reproduction.

</details>

### S3E: Self-Supervised State Estimation for Radar-Inertial System.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02477)
- **作者**: Shengpeng Wang, Yulong Xie, Qing Liao, Wei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pre-trained audio networks have seen widespread adoption in real-world systems, particularly in multi-modal large language models. These networks are often employed in a frozen state, under the assumption that the SSL pre-training has sufficiently equipped them to handle real-world audio. However, a critical question remains: how well do these models actually perform in real-world conditions, where audio is typically polyphonic and complex, involving multiple overlapping sound sources? Current audio SSL methods are often benchmarked on datasets predominantly featuring monophonic audio, such as environmental sounds, and speech. As a result, the ability of SSL models to generalize to polyphonic audio, a common characteristic in natural scenarios, remains underexplored. This limitation raises concerns about the practical robustness of SSL models in more realistic audio settings. To address this gap, we introduce Self-Supervised Learning from Audio Mixtures (SSLAM), a novel direction in audio SSL research, designed to improve, designed to improve the model's ability to learn from polyphonic data while maintaining strong performance on monophonic data. We thoroughly evaluate SSLAM on standard audio SSL benchmark datasets which are predominantly monophonic and conduct a comprehensive comparative analysis against SOTA methods using a range of high-quality, publicly available polyphonic datasets. SSLAM not only improves model performance on polyphonic audio, but also maintains or exceeds performance on standard audio SSL benchmarks. Notably, it achieves up to a 3.9\% improvement on the AudioSet-2M (AS-2M), reaching a mean average precision (mAP) of 50.2. For polyphonic datasets, SSLAM sets new SOTA in both linear evaluation and fine-tuning regimes with performance improvements of up to 9.1\% (mAP).

### DyCON: Dynamic Uncertainty-aware Consistency and Contrastive Learning for Semi-supervised Medical Image Segmentation.
- **链接**: [arXiv:2504.04566](https://arxiv.org/abs/2504.04566) · 📚 被引 25
- **作者**: Maregu Assefa, Muzammal Naseer, Iyyakutti Iyappan Ganapathi, Syed Sadaf Ali, Mohamed L. Seghier, Naoufel Werghi
- **🏷️ 机构**: C2PS - Khalifa University of Science and Technology,Abu Dhabi,UAE
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised learning in medical image segmentation leverages unlabeled data to reduce annotation burdens through consistency learning. However, current methods struggle with class imbalance and high uncertainty from pathology variations, leading to inaccurate segmentation in 3D medical images. To address these challenges, we present DyCON, a Dynamic Uncertainty-aware Consistency and Contrastive Learning framework that enhances the generalization of consistency methods with two complementary losses: Uncertainty-aware Consistency Loss (UnCL) and Focal Entropy-aware Contrastive Loss (FeCL). UnCL enforces global consistency by dynamically weighting the contribution of each voxel to the consistency loss based on its uncertainty, preserving high-uncertainty regions instead of filtering them out. Initially, UnCL prioritizes learning from uncertain voxels with lower penalties, encouraging the model to explore challenging regions. As training progress, the penalty shift towards confident voxels to refine predictions and ensure global consistency. Meanwhile, FeCL enhances local feature discrimination in imbalanced regions by introducing dual focal mechanisms and adaptive confidence adjustments into the contrastive principle. These mechanisms jointly prioritizes hard positives and negatives while focusing on uncertain sample pairs, effectively capturing subtle lesion variations under class imbalance. Extensive evaluations on four diverse medical image segmentation datasets (ISLES'22, BraTS'19, LA, Pancreas) show DyCON's superior performance against SOTA methods.

</details>

### Instruct-CLIP: Improving Instruction-Guided Image Editing with Automated Data Refinement Using Contrastive Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Instruct-CLIP_Improving_Instruction-Guided_Image_Editing_with_Automated_Data_Refinement_Using_CVPR_2025_paper.html)
- **作者**: Sherry X. Chen, Misha Sra, Pradeep Sen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Collapse-Proof Non-Contrastive Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/sansone25a.html)
- **作者**: Emanuele Sansone, Tim Lebailly, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> AI-generated face detectors trained via supervised learning typically rely on synthesized images from specific generators, limiting their generalization to emerging generative techniques. To overcome this limitation, we introduce a self-supervised method based on bi-level optimization. In the inner loop, we pretrain a vision encoder only on photographic face images using a set of linearly weighted pretext tasks: classification of categorical exchangeable image file format (EXIF) tags, ranking of ordinal EXIF tags, and detection of artificial face manipulations. The outer loop then optimizes the relative weights of these pretext tasks to enhance the coarse-grained detection of manipulated faces, serving as a proxy task for identifying AI-generated faces. In doing so, it aligns self-supervised learning more closely with the ultimate goal of AI-generated face detection. Once pretrained, the encoder remains fixed, and AI-generated faces are detected either as anomalies under a Gaussian mixture model fitted to photographic face features or by a lightweight two-layer perceptron serving as a binary classifier. Extensive experiments demonstrate that our detectors significantly outperform existing approaches in both one-class and binary classification settings, exhibiting strong generalization to unseen generators.

</details>

### Salvaging the Overlooked: Leveraging Class-Aware Contrastive Learning for Multi-Class Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01989) · 📚 被引 6
- **作者**: Lei Fan, Junjie Huang, Donglin Di, Anyang Su, Tianyou Song, Maurice Pagnucco et al.
- **🏷️ 机构**: UNSW,Sydney, DZ-Matrix, Columbia University
- **会议**: ICCV 2025

### Vector Contrastive Learning for Pixel-Wise Pretraining in Medical Vision.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01844) · 📚 被引 2
- **作者**: Yuting He, Shuo Li
- **🏷️ 机构**: Case Western Reserve University,Dept. of BME,Cleveland,US
- **会议**: ICCV 2025

### Robust Dataset Condensation using Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00274) · 📚 被引 0
- **作者**: Nicole Hee-Yeon Kim, Hwanjun Song
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST),Daejeon,Republic of Korea
- **会议**: ICCV 2025

### Selective Contrastive Learning for Weakly Supervised Affordance Grounding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00495) · 📚 被引 2
- **作者**: WonJun Moon, Hyun Seok Seong, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: ICCV 2025

### AMD: Adaptive Momentum and Decoupled Contrastive Learning Framework for Robust Long-Tail Trajectory Prediction.
- **链接**: [arXiv:2507.01801](https://arxiv.org/abs/2507.01801) · 📚 被引 1
- **作者**: Bin Rao, Haicheng Liao, Yanchen Guan, Chengyue Wang, Bonan Wang, Jiaxun Zhang et al.
- **🏷️ 机构**: University of Macau,State Key Laboratory of Internet of Things for Smart City
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately predicting the future trajectories of traffic agents is essential in autonomous driving. However, due to the inherent imbalance in trajectory distributions, tail data in natural datasets often represents more complex and hazardous scenarios. Existing studies typically rely solely on a base model's prediction error, without considering the diversity and uncertainty of long-tail trajectory patterns. We propose an adaptive momentum and decoupled contrastive learning framework (AMD), which integrates unsupervised and supervised contrastive learning strategies. By leveraging an improved momentum contrast learning (MoCo-DT) and decoupled contrastive learning (DCL) module, our framework enhances the model's ability to recognize rare and complex trajectories. Additionally, we design four types of trajectory random augmentation methods and introduce an online iterative clustering strategy, allowing the model to dynamically update pseudo-labels and better adapt to the distributional shifts in long-tail data. We propose three different criteria to define long-tail trajectories and conduct extensive comparative experiments on the nuScenes and ETH$/$UCY datasets. The results show that AMD not only achieves optimal performance in long-tail trajectory prediction but also demonstrates outstanding overall prediction accuracy.

</details>

### DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-Based Human Action Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01278) · 📚 被引 1
- **作者**: Haitao Tian
- **🏷️ 机构**: University of Ottawa,Canada
- **会议**: ICCV 2025

### FIX-CLIP: Dual-Branch Hierarchical Contrastive Learning via Synthetic Captions for Better Understanding of Long Text.
- **链接**: [arXiv:2507.10095](https://arxiv.org/abs/2507.10095) · [代码](https://github.com/bcwang-sjtu/Fix-CLIP) · 📚 被引 4
- **作者**: Bingchao Wang, Zhiwei Ning, Jianyu Ding, Xuanang Gao, Yin Li, Dongsheng Jiang et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Huawei Inc.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> CLIP has shown promising performance across many short-text tasks in a zero-shot manner. However, limited by the input length of the text encoder, CLIP struggles on under-stream tasks with long-text inputs ($>77$ tokens). To remedy this issue, we propose FIX-CLIP, which includes three novel modules: (1) A dual-branch training pipeline that aligns short and long texts with masked and raw images, respectively, which boosts the long-text representation while preserving the short-text ability. (2) Multiple learnable regional prompts with unidirectional masks in Transformer layers for regional information extraction. (3) A hierarchical feature alignment module in the intermediate encoder layers to promote the consistency of multi-scale features. Furthermore, we collect 30M images and utilize existing MLLMs to synthesize long-text captions for training. Extensive experiments show that FIX-CLIP achieves state-of-the-art performance on both long-text and short-text retrieval benchmarks. For downstream applications, we reveal that FIX-CLIP's text encoder delivers promising performance in a plug-and-play manner for diffusion models with long-text input. The code is available at https://github.com/bcwang-sjtu/Fix-CLIP.

</details>

### Keep Your Friends Close, and Your Enemies Farther: Distance-Aware Voxel-Wise Contrastive Learning for Semi-Supervised Multi-Organ Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02027) · 📚 被引 0
- **作者**: Haochen Zhao, Jianwei Niu, Xuefeng Liu, Xiaozheng Xie, Li Kuang, Haotian Yang et al.
- **🏷️ 机构**: SCSE, Beihang University,State Key Laboratory of Virtual Reality Technology and Systems, School of Computer and Communication Engineering, University of Science and Technology Beijing, Hangzhou International Innovation Institute of Beihang University
- **会议**: ICCV 2025

### Harnessing Massive Satellite Imagery with Efficient Masked Image Modeling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00652) · 📚 被引 6
- **作者**: Fengxiang Wang, Hongzhen Wang, Di Wang, Zonghao Guo, Zhenyu Zhong, Long Lan et al.
- **🏷️ 机构**: College of Computer Science and Technology, National University of Defense Technology, Xiaomi Corp., School of Computer Science, Wuhan University
- **会议**: ICCV 2025

### Beyond [cls]: Exploring the True Potential of Masked Image Modeling Representations.
- **链接**: [arXiv:2412.03215](https://arxiv.org/abs/2412.03215) · 📚 被引 3
- **作者**: Marcin Przewiezlikowski, Randall Balestriero, Wojciech Jasinski, Marek Smieja, Bartosz Zielinski
- **🏷️ 机构**: Jagiellonian University,Faculty of Mathematics and Computer Science, Brown University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Image Modeling (MIM) has emerged as a promising approach for Self-Supervised Learning (SSL) of visual representations. However, the out-of-the-box performance of MIMs is typically inferior to competing approaches. Most users cannot afford fine-tuning due to the need for large amounts of data, high GPU consumption, and specialized user knowledge. Therefore, the practical use of MIM representations is limited. In this paper we ask what is the reason for the poor out-of-the-box performance of MIMs. Is it due to weaker features produced by MIM models, or is it due to suboptimal usage? Through detailed analysis, we show that attention in MIMs is spread almost uniformly over many patches, leading to ineffective aggregation by the [cls] token. Based on this insight, we propose Selective Aggregation to better capture the rich semantic information retained in patch tokens, which significantly improves the out-of-the-box performance of MIM.

</details>

### Unsupervised Part Discovery via Descriptor-Based Masked Image Restoration with Optimized Constraints.
- **链接**: [arXiv:2507.11985](https://arxiv.org/abs/2507.11985) · [代码](https://github.com/Jiahao-UTS/MPAE) · 📚 被引 0
- **作者**: Jiahao Xia, Yike Wu, Wenjian Huang, Jianguo Zhang, Jian Zhang
- **🏷️ 机构**: University of Technology Sydney,Faculty of Engineering and IT, Southern University of Science and Technology,Dept. of Comp. Sci. and Eng.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Part-level features are crucial for image understanding, but few studies focus on them because of the lack of fine-grained labels. Although unsupervised part discovery can eliminate the reliance on labels, most of them cannot maintain robustness across various categories and scenarios, which restricts their application range. To overcome this limitation, we present a more effective paradigm for unsupervised part discovery, named Masked Part Autoencoder (MPAE). It first learns part descriptors as well as a feature map from the inputs and produces patch features from a masked version of the original images. Then, the masked regions are filled with the learned part descriptors based on the similarity between the local features and descriptors. By restoring these masked patches using the part descriptors, they become better aligned with their part shapes, guided by appearance features from unmasked patches. Finally, MPAE robustly discovers meaningful parts that closely match the actual object shapes, even in complex scenarios. Moreover, several looser yet more effective constraints are proposed to enable MPAE to identify the presence of parts across various scenarios and categories in an unsupervised manner. This provides the foundation for addressing challenges posed by occlusion and for exploring part similarity across multiple categories. Extensive experiments demonstrate that our method robustly discovers meaningful parts across various categories and scenarios. The code is available at the project https://github.com/Jiahao-UTS/MPAE.

</details>

## 跨领域论文（完整笔记在其他领域）

- Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-Time Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Talking to DINO: Bridging Self-Supervised Vision Backbones with Language for Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Differential-Informed Sample Selection Accelerates Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202025.md)
- Point Cloud Self-Supervised Learning via 3D to Multi-View Masked Learner. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- GaussianOcc: Fully Self-Supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting. → [occupancy](../occupancy/Guideline%202025.md)
- AD-GS: Object-Aware B-Spline Gaussian Splatting for Self-Supervised Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Hybrid-Grained Feature Aggregation with Coarse-to-Fine Language Guidance for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
