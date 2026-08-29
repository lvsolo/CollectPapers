# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 110 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GD-MAE: Generative Decoder for MAE Pre-Training on LiDAR Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00907) · 📚 被引 71
- **作者**: Honghui Yang, Tong He, Jiaheng Liu, Hua Chen, Boxi Wu, Binbin Lin et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, Shanghai AI Laboratory, COMAC Beijing Aircraft Technology Research Institute
- **会议**: CVPR 2023

### DeepMapping2: Self-Supervised Large-Scale LiDAR Map Optimization.
- **链接**: [arXiv:2212.06331](https://arxiv.org/abs/2212.06331) · 📚 被引 13
- **作者**: Chao Chen, Xinhao Liu, Yiming Li, Li Ding, Chen Feng
- **🏷️ 机构**: New York University, University of Rochester
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR mapping is important yet challenging in self-driving and mobile robotics. To tackle such a global point cloud registration problem, DeepMapping converts the complex map estimation into a self-supervised training of simple deep networks. Despite its broad convergence range on small datasets, DeepMapping still cannot produce satisfactory results on large-scale datasets with thousands of frames. This is due to the lack of loop closures and exact cross-frame point correspondences, and the slow convergence of its global localization network. We propose DeepMapping2 by adding two novel techniques to address these issues: (1) organization of training batch based on map topology from loop closing, and (2) self-supervised local-to-global point consistency loss leveraging pairwise registration. Our experiments and ablation studies on public datasets (KITTI, NCLT, and Nebula) demonstrate the effectiveness of our method.

</details>

### PointCMP: Contrastive Mask Prediction for Self-supervised Learning on Point Cloud Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00123) · 📚 被引 26
- **作者**: Zhiqiang Shen, Xiaoxiao Sheng, Longguang Wang, Yulan Guo, Qiong Liu, Xi Zhou
- **🏷️ 机构**: Shanghai Jiao Tong University, Aviation University of Air Force, Sun Yat-sen University
- **会议**: CVPR 2023

### ACL-SPC: Adaptive Closed-Loop System for Self-Supervised Point Cloud Completion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00910) · 📚 被引 27
- **作者**: Sangmin Hong, Mohsen Yavartanoo, Reyhaneh Neshatavar, Kyoung Mu Lee
- **🏷️ 机构**: IPAI, Seoul National University,Dept. of ECE &#x0026; ASRI,Seoul,Korea
- **会议**: CVPR 2023

### ToThePoint: Efficient Contrastive Learning of 3D Point Clouds via Recycling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02086) · 📚 被引 14
- **作者**: Xinglin Li, Jiajing Chen, Jinhui Ouyang, Hanhui Deng, Senem Velipasalar, Di Wu
- **🏷️ 机构**: Hunan University,China, Syracuse University,NY,USA
- **会议**: CVPR 2023

### Implicit Autoencoder for Point-Cloud Self-Supervised Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01336) · 📚 被引 44
- **作者**: Siming Yan, Zhenpei Yang, Haoxiang Li, Chen Song, Li Guan, Hao Kang et al.
- **🏷️ 机构**: The University of Texas at Austin, Wormpex AI Research
- **会议**: ICCV 2023

### SC3K: Self-supervised and Coherent 3D Keypoints Estimation from Rotated, Noisy, and Decimated Point Cloud Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02057) · 📚 被引 11
- **作者**: Mohammad Zohaib, Alessio Del Bue
- **🏷️ 机构**: Italian Institute of Technology (IIT),Pattern Analysis &#x0026; Computer Vision (PAVIS),Genoa,Italy
- **会议**: ICCV 2023

### SelfGraphVQA: A Self-Supervised Graph Neural Network for Scene-based Question Answering.
- **链接**: [arXiv:2310.01842](https://arxiv.org/abs/2310.01842) · 📚 被引 4
- **作者**: Bruno Souza, Marius Aasan, Hélio Pedrini, Adín Ramírez Rivera
- **🏷️ 机构**: University of Campinas, University of Oslo
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The intersection of vision and language is of major interest due to the increased focus on seamless integration between recognition and reasoning. Scene graphs (SGs) have emerged as a useful tool for multimodal image analysis, showing impressive performance in tasks such as Visual Question Answering (VQA). In this work, we demonstrate that despite the effectiveness of scene graphs in VQA tasks, current methods that utilize idealized annotated scene graphs struggle to generalize when using predicted scene graphs extracted from images. To address this issue, we introduce the SelfGraphVQA framework. Our approach extracts a scene graph from an input image using a pre-trained scene graph generator and employs semantically-preserving augmentation with self-supervised techniques. This method improves the utilization of graph representations in VQA tasks by circumventing the need for costly and potentially biased annotated data. By creating alternative views of the extracted graphs through image augmentations, we can learn joint embeddings by optimizing the informational content in their representations using an un-normalized contrastive approach. As we work with SGs, we experiment with three distinct maximization strategies: node-wise, graph-wise, and permutation-equivariant regularization. We empirically showcase the effectiveness of the extracted scene graph for VQA and demonstrate that these approaches enhance overall performance by highlighting the significance of visual information. This offers a more practical solution for VQA tasks that rely on SGs for complex reasoning questions.

</details>

### Randomized Quantization: A Generic Augmentation for Data Agnostic Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01494) · 📚 被引 10
- **作者**: Huimin Wu, Chenyang Lei, Xiao Sun, Peng-Shuai Wang, Qifeng Chen, Kwang-Ting Cheng et al.
- **🏷️ 机构**: HKUST, CAIR, HKISI CAS, Shanghai AI Lab
- **会议**: ICCV 2023

### Self-Supervised Burst Super-Resolution.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00973)
- **作者**: Goutam Bhat, Michaël Gharbi, Jiawen Chen, Luc Van Gool, Zhihao Xia
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Active Self-Supervised Learning: A Few Low-Cost Relationships Are All You Need.
- **链接**: [arXiv:2303.15256](https://arxiv.org/abs/2303.15256) · 📚 被引 9
- **作者**: Vivien Cabannes, Léon Bottou, Yann LeCun, Randall Balestriero
- **🏷️ 机构**: Meta AI
- **会议**: ICCV 2023

### SINC: Self-Supervised In-Context Learning for Vision-Language Tasks.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01415) · 📚 被引 6
- **作者**: Yi-Syuan Chen, Yun-Zhu Song, Cheng Yu Yeo, Bei Liu, Jianlong Fu, Hong-Han Shuai
- **🏷️ 机构**: National Yang Ming Chiao Tung University, Microsoft Research Asia
- **会议**: ICCV 2023

### Contrastive Continuity on Augmentation Stability Rehearsal for Continual Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00525) · 📚 被引 10
- **作者**: Haoyang Cheng, Haitao Wen, Xiaoliang Zhang, Heqian Qiu, Lanxiao Wang, Hongliang Li
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China
- **会议**: ICCV 2023

### Identity-Seeking Self-Supervised Representation Learning for Generalizable Person Re-identification.
- **链接**: [arXiv:2308.08887](https://arxiv.org/abs/2308.08887) · [代码](https://github.com/dcp15/ISR_ICCV2023_Oral) · 📚 被引 27
- **作者**: Zhaopeng Dou, Zhongdao Wang, Yali Li, Shengjin Wang
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper aims to learn a domain-generalizable (DG) person re-identification (ReID) representation from large-scale videos \textbf{without any annotation}. Prior DG ReID methods employ limited labeled data for training due to the high cost of annotation, which restricts further advances. To overcome the barriers of data and annotation, we propose to utilize large-scale unsupervised data for training. The key issue lies in how to mine identity information. To this end, we propose an Identity-seeking Self-supervised Representation learning (ISR) method. ISR constructs positive pairs from inter-frame images by modeling the instance association as a maximum-weight bipartite matching problem. A reliability-guided contrastive loss is further presented to suppress the adverse impact of noisy positive pairs, ensuring that reliable positive pairs dominate the learning process. The training cost of ISR scales approximately linearly with the data size, making it feasible to utilize large-scale data for training. The learned representation exhibits superior generalization ability. \textbf{Without human annotation and fine-tuning, ISR achieves 87.0\% Rank-1 on Market-1501 and 56.4\% Rank-1 on MSMT17}, outperforming the best supervised domain-generalizable method by 5.0\% and 19.5\%, respectively. In the pre-training$\rightarrow$fine-tuning scenario, ISR achieves state-of-the-art performance, with 88.4\% Rank-1 on MSMT17. The code is at \url{https://github.com/dcp15/ISR_ICCV2023_Oral}.

</details>

### SimFIR: A Simple Framework for Fisheye Image Rectification with Self-supervised Representation Learning.
- **链接**: [arXiv:2308.09040](https://arxiv.org/abs/2308.09040) · 📚 被引 27
- **作者**: Hao Feng, Wendi Wang, Jiajun Deng, Wengang Zhou, Li Li, Houqiang Li
- **🏷️ 机构**: University of Science and Technology of China,CAS Key Laboratory of Technology in GIPAS,EEIS Department, The University of Sydney
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In fisheye images, rich distinct distortion patterns are regularly distributed in the image plane. These distortion patterns are independent of the visual content and provide informative cues for rectification. To make the best of such rectification cues, we introduce SimFIR, a simple framework for fisheye image rectification based on self-supervised representation learning. Technically, we first split a fisheye image into multiple patches and extract their representations with a Vision Transformer (ViT). To learn fine-grained distortion representations, we then associate different image patches with their specific distortion patterns based on the fisheye model, and further subtly design an innovative unified distortion-aware pretext task for their learning. The transfer performance on the downstream rectification task is remarkably boosted, which verifies the effectiveness of the learned representations. Extensive experiments are conducted, and the quantitative and qualitative results demonstrate the superiority of our method over the state-of-the-art algorithms as well as its strong generalization ability on real-world fisheye images.

</details>

### TeD-SPAD: Temporal Distinctiveness for Self-supervised Privacy-preservation for video Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01251)
- **作者**: Joseph Fioresi, Ishan Rajendrakumar Dave, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-paced learning has been beneficial for tasks where some initial knowledge is available, such as weakly supervised learning and domain adaptation, to select and order the training sample sequence, from easy to complex. However its applicability remains unexplored in unsupervised learning, whereby the knowledge of the task matures during training. We propose a novel HYperbolic Self-Paced model (HYSP) for learning skeleton-based action representations. HYSP adopts self-supervision: it uses data augmentations to generate two views of the same sample, and it learns by matching one (named online) to the other (the target). We propose to use hyperbolic uncertainty to determine the algorithmic learning pace, under the assumption that less uncertain samples should be more strongly driving the training, with a larger weight and pace. Hyperbolic uncertainty is a by-product of the adopted hyperbolic neural networks, it matures during training and it comes with no extra cost, compared to the established Euclidean SSL framework counterparts. When tested on three established skeleton-based action recognition datasets, HYSP outperforms the state-of-the-art on PKU-MMD I, as well as on 2 out of 3 downstream tasks on NTU-60 and NTU-120. Additionally, HYSP only uses positive pairs and bypasses therefore the complex and computationally-demanding mining procedures required for the negatives in contrastive techniques. Code is available at https://github.com/paolomandica/HYSP.

</details>

### Self-supervised Image Denoising with Downsampled Invariance Loss and Conditional Blind-Spot Network.
- **链接**: [arXiv:2304.09507](https://arxiv.org/abs/2304.09507) · 📚 被引 15
- **作者**: Yeong Il Jang, Keuntek Lee, Gu Yong Park, Seyun Kim, Nam Ik Cho
- **🏷️ 机构**: Seoul National University,INMC,Department of ECE,Seoul,Korea, Gauss Labs Inc.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There have been many image denoisers using deep neural networks, which outperform conventional model-based methods by large margins. Recently, self-supervised methods have attracted attention because constructing a large real noise dataset for supervised training is an enormous burden. The most representative self-supervised denoisers are based on blind-spot networks, which exclude the receptive field's center pixel. However, excluding any input pixel is abandoning some information, especially when the input pixel at the corresponding output position is excluded. In addition, a standard blind-spot network fails to reduce real camera noise due to the pixel-wise correlation of noise, though it successfully removes independently distributed synthetic noise. Hence, to realize a more practical denoiser, we propose a novel self-supervised training framework that can remove real noise. For this, we derive the theoretic upper bound of a supervised loss where the network is guided by the downsampled blinded output. Also, we design a conditional blind-spot network (C-BSN), which selectively controls the blindness of the network to use the center pixel information. Furthermore, we exploit a random subsampler to decorrelate noise spatially, making the C-BSN free of visual artifacts that were often seen in downsample-based methods. Extensive experiments show that the proposed C-BSN achieves state-of-the-art performance on real-world datasets as a self-supervised denoiser and shows qualitatively pleasing results without any post-processing or refinement.

</details>

### EMR-MSF: Self-Supervised Recurrent Monocular Scene Flow Exploiting Ego-Motion Rigidity.
- **链接**: [arXiv:2309.01296](https://arxiv.org/abs/2309.01296) · 📚 被引 0
- **作者**: Zijie Jiang, Masatoshi Okutomi
- **🏷️ 机构**: Tokyo Institute of Technology
- **会议**: ICCV 2023

### Distilling Self-Supervised Vision Transformers for Weakly-Supervised Few-Shot Classification & Segmentation.
- **链接**: [arXiv:2307.03407](https://arxiv.org/abs/2307.03407) · 📚 被引 42
- **作者**: Dahyun Kang, Piotr Koniusz, Minsu Cho, Naila Murray
- **🏷️ 机构**: Meta AI, Data61 &#x2665; CSIRO, POSTECH
- **会议**: CVPR 2023

### An Embarrassingly Simple Backdoor Attack on Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00403) · 📚 被引 48
- **作者**: Changjiang Li, Ren Pang, Zhaohan Xi, Tianyu Du, Shouling Ji, Yuan Yao et al.
- **🏷️ 机构**: Pennsylvania State University, Zhejiang University, Nanjing University
- **会议**: ICCV 2023

> We address the task of weakly-supervised few-shot image classification and segmentation, by leveraging a Vision Transformer (ViT) pretrained with self-supervision. Our proposed method takes token representations from the self-supervised ViT and leverages their correlations, via self-attention, to produce classification and segmentation predictions through separate task heads. Our model is able to effectively learn to perform classification and segmentation in the absence of pixel-level labels during training, using only image-level labels. To do this it uses attention maps, created from tokens generated by the self-supervised ViT backbone, as pixel-level pseudo-labels. We also explore a practical setup with ``mixed" supervision, where a small number of training images contains ground-truth pixel-level labels and the remaining images have only image-level labels. For this mixed setup, we propose to improve the pseudo-labels using a pseudo-label enhancer that was trained using the available ground-truth pixel-level labels. Experiments on Pascal-5i and COCO-20i demonstrate significant performance gains in a variety of supervision settings, and in particular when little-to-no pixel-level labels are available.

</details>

### MixMAE: Mixed and Masked Autoencoder for Efficient Pretraining of Hierarchical Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00605) · 📚 被引 69
- **作者**: Jihao Liu, Xin Huang, Jinliang Zheng, Yu Liu, Hongsheng Li
- **🏷️ 机构**: CUHK MMLab, SenseTime Research
- **会议**: CVPR 2023

### SelfME: Self-Supervised Motion Learning for Micro-Expression Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01329) · 📚 被引 56
- **作者**: Xinqi Fan, Xueli Chen, Mingjie Jiang, Ali Raza Shahid, Hong Yan
- **🏷️ 机构**: City University of Hong Kong
- **会议**: CVPR 2023

### Semi-supervised learning made simple with self-supervised clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00311) · 📚 被引 39
- **作者**: Enrico Fini, Pietro Astolfi, Karteek Alahari, Xavier Alameda-Pineda, Julien Mairal, Moin Nabi et al.
- **🏷️ 机构**: University of Trento, Inria, SAP AI Research
- **会议**: CVPR 2023

### Canonical Fields: Self-Supervised Learning of Pose-Canonicalized Neural Fields.
- **链接**: [arXiv:2212.02493](https://arxiv.org/abs/2212.02493) · 📚 被引 8
- **作者**: Rohith Agaram, Shaurya Dewan, Rahul Sajnani, Adrien Poulenard, K. Madhava Krishna, Srinath Sridhar
- **🏷️ 机构**: IIIT-Hyderabad,RRC, Brown University, Stanford University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Beyond novel view synthesis, Neural Radiance Fields are useful for applications that interact with the real world. In this paper, we use them as an implicit map of a given scene and propose a camera relocalization algorithm tailored for this representation. The proposed method enables to compute in real-time the precise position of a device using a single RGB camera, during its navigation. In contrast with previous work, we do not rely on pose regression or photometric alignment but rather use dense local features obtained through volumetric rendering which are specialized on the scene with a self-supervised objective. As a result, our algorithm is more accurate than competitors, able to operate in dynamic outdoor environments with changing lightning conditions and can be readily integrated in any volumetric neural renderer.

</details>

### Representation Uncertainty in Self-Supervised Learning as Variational Inference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01511) · 📚 被引 12
- **作者**: Hiroki Nakamura, Masashi Okada, Tadahiro Taniguchi
- **🏷️ 机构**: Panasonic Holdings Corp., Ritsumeikan University
- **会议**: ICCV 2023

### Random Sub-Samples Generation for Self-Supervised Real Image Denoising.
- **链接**: [arXiv:2307.16825](https://arxiv.org/abs/2307.16825) · [代码](https://github.com/p1y2z3/SDAP) · 📚 被引 46
- **作者**: Yizhong Pan, Xiao Liu, Xiangyu Liao, Yuanzhouhan Cao, Chao Ren
- **🏷️ 机构**: Sichuan University,College of Electronics and Information Engineering,China, Beijing Jiaotong University,School of Computer and Information Technology,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With sufficient paired training samples, the supervised deep learning methods have attracted much attention in image denoising because of their superior performance. However, it is still very challenging to widely utilize the supervised methods in real cases due to the lack of paired noisy-clean images. Meanwhile, most self-supervised denoising methods are ineffective as well when applied to the real-world denoising tasks because of their strict assumptions in applications. For example, as a typical method for self-supervised denoising, the original blind spot network (BSN) assumes that the noise is pixel-wise independent, which is much different from the real cases. To solve this problem, we propose a novel self-supervised real image denoising framework named Sampling Difference As Perturbation (SDAP) based on Random Sub-samples Generation (RSG) with a cyclic sample difference loss. Specifically, we dig deeper into the properties of BSN to make it more suitable for real noise. Surprisingly, we find that adding an appropriate perturbation to the training images can effectively improve the performance of BSN. Further, we propose that the sampling difference can be considered as perturbation to achieve better results. Finally we propose a new BSN framework in combination with our RSG strategy. The results show that it significantly outperforms other state-of-the-art self-supervised denoising methods on real-world datasets. The code is available at https://github.com/p1y2z3/SDAP.

</details>

### Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture.
- **链接**: [arXiv:2301.08243](https://arxiv.org/abs/2301.08243)
- **作者**: Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael G. Rabbat et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised methods have shown remarkable progress in learning high-level semantics and low-level temporal correspondence. Building on these results, we take one step further and explore the possibility of integrating these two features to enhance object-centric representations. Our preliminary experiments indicate that query slot attention can extract different semantic components from the RGB feature map, while random sampling based slot attention can exploit temporal correspondence cues between frames to assist instance identification. Motivated by this, we propose a novel semantic-aware masked slot attention on top of the fused semantic features and correspondence maps. It comprises two slot attention stages with a set of shared learnable Gaussian distributions. In the first stage, we use the mean vectors as slot initialization to decompose potential semantics and generate semantic segmentation masks through iterative attention. In the second stage, for each semantics, we randomly sample slots from the corresponding Gaussian distribution and perform masked feature aggregation within the semantic area to exploit temporal correspondence patterns for instance identification. We adopt semantic- and instance-level temporal consistency as self-supervision to encourage temporally coherent object-centric representations. Our model effectively identifies multiple object instances with semantic structure, reaching promising results on unsupervised video object discovery. Furthermore, we achieve state-of-the-art performance on dense label propagation tasks, demonstrating the potential for object-centric analysis. The code is released at https://github.com/shvdiwnkozbw/SMTC.

</details>

### Learn TAROT with MENTOR: A Meta-Learned Self-supervised Approach for Trajectory Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00770) · 📚 被引 19
- **作者**: Mozhgan Pourkeshavarz, Changhe Chen, Amir Rasouli
- **🏷️ 机构**: Huawei,Noah&#x2019;s Ark Lab,Toronto,Canada
- **会议**: ICCV 2023

### Semantics Meets Temporal Correspondence: Self-supervised Object-centric Learning in Videos.
- **链接**: [arXiv:2308.09951](https://arxiv.org/abs/2308.09951) · [代码](https://github.com/shvdiwnkozbw/SMTC) · 📚 被引 13
- **作者**: Rui Qian, Shuangrui Ding, Xian Liu, Dahua Lin
- **🏷️ 机构**: The Chinese University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised methods have shown remarkable progress in learning high-level semantics and low-level temporal correspondence. Building on these results, we take one step further and explore the possibility of integrating these two features to enhance object-centric representations. Our preliminary experiments indicate that query slot attention can extract different semantic components from the RGB feature map, while random sampling based slot attention can exploit temporal correspondence cues between frames to assist instance identification. Motivated by this, we propose a novel semantic-aware masked slot attention on top of the fused semantic features and correspondence maps. It comprises two slot attention stages with a set of shared learnable Gaussian distributions. In the first stage, we use the mean vectors as slot initialization to decompose potential semantics and generate semantic segmentation masks through iterative attention. In the second stage, for each semantics, we randomly sample slots from the corresponding Gaussian distribution and perform masked feature aggregation within the semantic area to exploit temporal correspondence patterns for instance identification. We adopt semantic- and instance-level temporal consistency as self-supervision to encourage temporally coherent object-centric representations. Our model effectively identifies multiple object instances with semantic structure, reaching promising results on unsupervised video object discovery. Furthermore, we achieve state-of-the-art performance on dense label propagation tasks, demonstrating the potential for object-centric analysis. The code is released at https://github.com/shvdiwnkozbw/SMTC.

</details>

### Mixed Autoencoder for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2303.17152](https://arxiv.org/abs/2303.17152) · 📚 被引 35
- **作者**: Kai Chen, Zhili Liu, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Autoencoder (MAE) has demonstrated superior performance on various vision tasks via randomly masking image patches and reconstruction. However, effective data augmentation strategies for MAE still remain open questions, different from those in contrastive learning that serve as the most important part. This paper studies the prevailing mixing augmentation for MAE. We first demonstrate that naive mixing will in contrast degenerate model performance due to the increase of mutual information (MI). To address, we propose homologous recognition, an auxiliary pretext task, not only to alleviate the MI increasement by explicitly requiring each patch to recognize homologous patches, but also to perform object-aware self-supervised pre-training for better downstream dense perception performance. With extensive experiments, we demonstrate that our proposed Mixed Autoencoder (MixedAE) achieves the state-of-the-art transfer results among masked image modeling (MIM) augmentations on different downstream tasks with significant efficiency. Specifically, our MixedAE outperforms MAE by +0.3% accuracy, +1.7 mIoU and +0.9 AP on ImageNet-1K, ADE20K and COCO respectively with a standard ViT-Base. Moreover, MixedAE surpasses iBOT, a strong MIM method combined with instance discrimination, while accelerating training by 2x. To our best knowledge, this is the very first work to consider mixing for MIM from the perspective of pretext task design. Code will be made available.

</details>

### TexPose: Neural Texture Learning for Self-Supervised 6D Object Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00469) · 📚 被引 45
- **作者**: Hanzhi Chen, Fabian Manhardt, Nassir Navab, Benjamin Busam
- **🏷️ 机构**: Technical University of Munich, Google Inc.
- **会议**: CVPR 2023

### Beyond Appearance: A Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks.
- **链接**: [arXiv:2303.17602](https://arxiv.org/abs/2303.17602) · [代码](https://github.com/tinyvision/SOLIDER) · 📚 被引 144
- **作者**: Weihua Chen, Xianzhe Xu, Jian Jia, Hao Luo, Yaohua Wang, Fan Wang et al.
- **🏷️ 机构**: Alibaba Group
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-centric visual tasks have attracted increasing research attention due to their widespread applications. In this paper, we aim to learn a general human representation from massive unlabeled human images which can benefit downstream human-centric tasks to the maximum extent. We call this method SOLIDER, a Semantic cOntrollable seLf-supervIseD lEaRning framework. Unlike the existing self-supervised learning methods, prior knowledge from human images is utilized in SOLIDER to build pseudo semantic labels and import more semantic information into the learned representation. Meanwhile, we note that different downstream tasks always require different ratios of semantic information and appearance information. For example, human parsing requires more semantic information, while person re-identification needs more appearance information for identification purpose. So a single learned representation cannot fit for all requirements. To solve this problem, SOLIDER introduces a conditional network with a semantic controller. After the model is trained, users can send values to the controller to produce representations with different ratios of semantic information, which can fit different needs of downstream tasks. Finally, SOLIDER is verified on six downstream human-centric visual tasks. It outperforms state of the arts and builds new baselines for these tasks. The code is released in https://github.com/tinyvision/SOLIDER.

</details>

### StepFormer: Self-Supervised Step Discovery and Localization in Instructional Videos.
- **链接**: [arXiv:2304.13265](https://arxiv.org/abs/2304.13265) · 📚 被引 22
- **作者**: Nikita Dvornik, Isma Hadji, Ran Zhang, Konstantinos G. Derpanis, Richard P. Wildes, Allan D. Jepson
- **🏷️ 机构**: Samsung AI Centre Toronto
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Instructional videos are an important resource to learn procedural tasks from human demonstrations. However, the instruction steps in such videos are typically short and sparse, with most of the video being irrelevant to the procedure. This motivates the need to temporally localize the instruction steps in such videos, i.e. the task called key-step localization. Traditional methods for key-step localization require video-level human annotations and thus do not scale to large datasets. In this work, we tackle the problem with no human supervision and introduce StepFormer, a self-supervised model that discovers and localizes instruction steps in a video. StepFormer is a transformer decoder that attends to the video with learnable queries, and produces a sequence of slots capturing the key-steps in the video. We train our system on a large dataset of instructional videos, using their automatically-generated subtitles as the only source of supervision. In particular, we supervise our system with a sequence of text narrations using an order-aware loss function that filters out irrelevant phrases. We show that our model outperforms all previous unsupervised and weakly-supervised approaches on step detection and localization by a large margin on three challenging benchmarks. Moreover, our model demonstrates an emergent property to solve zero-shot multi-step localization and outperforms all relevant baselines at this task.

</details>

### Self-supervised Non-uniform Kernel Estimation with Flow-based Motion Prior for Blind Image Deblurring.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01736) · 📚 被引 60
- **作者**: Zhenxuan Fang, Fangfang Wu, Weisheng Dong, Xin Li, Jinjian Wu, Guangming Shi
- **🏷️ 机构**: Xidian University, West Virginia University
- **会议**: CVPR 2023

### Evolved Part Masking for Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01001) · 📚 被引 24
- **作者**: Zhanzhou Feng, Shiliang Zhang
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing
- **会议**: CVPR 2023

### Self-Supervised Implicit Glyph Attention for Text Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01467) · 📚 被引 26
- **作者**: Tongkun Guan, Chaochen Gu, Jingzheng Tu, Xue Yang, Qi Feng, Yudi Zhao et al.
- **🏷️ 机构**: AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Shanghai Jiao Tong University,Department of Automation
- **会议**: CVPR 2023

### Vid2Avatar: 3D Avatar Reconstruction from Videos in the Wild via Self-supervised Scene Decomposition.
- **链接**: [arXiv:2302.11566](https://arxiv.org/abs/2302.11566) · 📚 被引 121
- **作者**: Chen Guo, Tianjian Jiang, Xu Chen, Jie Song, Otmar Hilliges
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ubiquity of camera-enabled devices has led to large amounts of unlabeled image data being produced at the edge. The integration of self-supervised learning (SSL) and federated learning (FL) into one coherent system can potentially offer data privacy guarantees while also advancing the quality and robustness of the learned visual representations without needing to move data around. However, client bias and divergence during FL aggregation caused by data heterogeneity limits the performance of learned visual representations on downstream tasks. In this paper, we propose a new aggregation strategy termed Layer-wise Divergence Aware Weight Aggregation (L-DAWA) to mitigate the influence of client bias and divergence during FL aggregation. The proposed method aggregates weights at the layer-level according to the measure of angular divergence between the clients' model and the global model. Extensive experiments with cross-silo and cross-device settings on CIFAR-10/100 and Tiny ImageNet datasets demonstrate that our methods are effective and obtain new SOTA performance on both contrastive and non-contrastive SSL approaches.

</details>

### CLIP-S4: Language-Guided Self-Supervised Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01078)
- **作者**: Wenbin He, Suphanut Jamonnak, Liang Gou, Liu Ren
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Geometric Visual Similarity Learning in 3D Medical Image Self-Supervised Pre-training.
- **链接**: [arXiv:2303.00874](https://arxiv.org/abs/2303.00874) · [代码](https://github.com/YutingHe-list/GVSL) · 📚 被引 54
- **作者**: Yuting He, Guanyu Yang, Rongjun Ge, Yang Chen, Jean-Louis Coatrieux, Boyu Wang et al.
- **🏷️ 机构**: Southeast University, Nanjing University of Aeronautics and Astronautics, University of Rennes 1
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning inter-image similarity is crucial for 3D medical images self-supervised pre-training, due to their sharing of numerous same semantic regions. However, the lack of the semantic prior in metrics and the semantic-independent variation in 3D medical images make it challenging to get a reliable measurement for the inter-image similarity, hindering the learning of consistent representation for same semantics. We investigate the challenging problem of this task, i.e., learning a consistent representation between images for a clustering effect of same semantic features. We propose a novel visual similarity learning paradigm, Geometric Visual Similarity Learning, which embeds the prior of topological invariance into the measurement of the inter-image similarity for consistent representation of semantic regions. To drive this paradigm, we further construct a novel geometric matching head, the Z-matching head, to collaboratively learn the global and local similarity of semantic regions, guiding the efficient representation learning for different scale-level inter-image semantic features. Our experiments demonstrate that the pre-training with our learning of inter-image similarity yields more powerful inner-scene, inter-scene, and global-local transferring ability on four challenging 3D medical image tasks. Our codes and pre-trained models will be publicly available on https://github.com/YutingHe-list/GVSL.

</details>

### ReVISE: Self-Supervised Speech Resynthesis with Visual Input for Universal and Generalized Speech Regeneration.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01802) · 📚 被引 18
- **作者**: Wei-Ning Hsu, Tal Remez, Bowen Shi, Jacob Donley, Yossi Adi
- **🏷️ 机构**: FAIR, Meta AI Research, Meta Reality Labs Research
- **会议**: CVPR 2023

### Self-supervised AutoFlow.
- **链接**: [arXiv:2212.01762](https://arxiv.org/abs/2212.01762)
- **作者**: Hsin-Ping Huang, Charles Herrmann, Junhwa Hur, Erika Lu, Kyle Sargent, Austin Stone et al.
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deeper Vision Transformers (ViTs) are more challenging to train. We expose a degradation problem in deeper layers of ViT when using masked image modeling (MIM) for pre-training. To ease the training of deeper ViTs, we introduce a self-supervised learning framework called Masked Image Residual Learning (MIRL), which significantly alleviates the degradation problem, making scaling ViT along depth a promising direction for performance upgrade. We reformulate the pre-training objective for deeper layers of ViT as learning to recover the residual of the masked image. We provide extensive empirical evidence showing that deeper ViTs can be effectively optimized using MIRL and easily gain accuracy from increased depth. With the same level of computational complexity as ViT-Base and ViT-Large, we instantiate 4.5$\times$ and 2$\times$ deeper ViTs, dubbed ViT-S-54 and ViT-B-48. The deeper ViT-S-54, costing 3$\times$ less than ViT-Large, achieves performance on par with ViT-Large. ViT-B-48 achieves 86.2% top-1 accuracy on ImageNet. On one hand, deeper ViTs pre-trained with MIRL exhibit excellent generalization capabilities on downstream tasks, such as object detection and semantic segmentation. On the other hand, MIRL demonstrates high pre-training efficiency. With less pre-training time, MIRL yields competitive performance compared to other approaches.

</details>

### Generalized Semi-Supervised Learning via Self-Supervised Feature Adaptation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/bf145010b30dc5f14fa87dc152074e4d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jiachen Liang, Ruibing Hou, Hong Chang, Bingpeng Ma, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent Self-Supervised Learning (SSL) methods are able to learn feature representations that are invariant to different data augmentations, which can then be transferred to downstream tasks of interest. However, different downstream tasks require different invariances for their best performance, so the optimal choice of augmentations for SSL depends on the target task. In this paper, we aim to learn self-supervised features that generalize well across a variety of downstream tasks (e.g., object classification, detection and instance segmentation) without knowing any task information beforehand. We do so by Masked Augmentation Subspace Training (or MAST) to encode in the single feature space the priors from different data augmentations in a factorized way. Specifically, we disentangle the feature space into separate subspaces, each induced by a learnable mask that selects relevant feature dimensions to model invariance to a specific augmentation. We show the success of MAST in jointly capturing generalizable priors from different augmentations, using both unique and shared features across the subspaces. We further show that MAST benefits from uncertainty modeling to reweight ambiguous samples from strong augmentations that may cause similarity mismatch in each subspace. Experiments demonstrate that MAST consistently improves generalization on various downstream tasks, while being task-agnostic and efficient during SSL. We also provide interesting insights about how different augmentations are related and how uncertainty reflects learning difficulty.

</details>

### Towards the Generalization of Contrastive Self-Supervised Learning.
- **链接**: [arXiv:2111.00743](https://arxiv.org/abs/2111.00743)
- **作者**: Weiran Huang, Mingyang Yi, Xuyang Zhao, Zihao Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Computational pathology can lead to saving human lives, but models are annotation hungry and pathology images are notoriously expensive to annotate. Self-supervised learning has shown to be an effective method for utilizing unlabeled data, and its application to pathology could greatly benefit its downstream tasks. Yet, there are no principled studies that compare SSL methods and discuss how to adapt them for pathology. To address this need, we execute the largest-scale study of SSL pre-training on pathology image data, to date. Our study is conducted using 4 representative SSL methods on diverse downstream tasks. We establish that large-scale domain-aligned pre-training in pathology consistently out-performs ImageNet pre-training in standard SSL settings such as linear and fine-tuning evaluations, as well as in low-label regimes. Moreover, we propose a set of domain-specific techniques that we experimentally show leads to a performance boost. Lastly, for the first time, we apply SSL to the challenging task of nuclei instance segmentation and show large and consistent performance improvements under diverse settings.

</details>

### Self-Supervised Geometry-Aware Encoder for Style-Based 3D GAN Inversion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02006) · 📚 被引 27
- **作者**: Yushi Lan, Xuyi Meng, Shuai Yang, Chen Change Loy, Bo Dai
- **🏷️ 机构**: Nanyang Technological University,S-Lab,Singapore, Shanghai AI Laboratory
- **会议**: CVPR 2023

### SCOOP: Self-Supervised Correspondence and Optimization-Based Scene Flow.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00511) · 📚 被引 34
- **作者**: Itai Lang, Dror Aiger, Forrester Cole, Shai Avidan, Michael Rubinstein
- **🏷️ 机构**: Tel Aviv University, Google Research
- **会议**: CVPR 2023

### Correlational Image Modeling for Self-Supervised Visual Pre-Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01450) · 📚 被引 13
- **作者**: Wei Li, Jiahao Xie, Chen Change Loy
- **🏷️ 机构**: Nanyang Technological University,S-Lab
- **会议**: CVPR 2023

### Token Boosting for Robust Self-Supervised Visual Transformer Pre-training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02301) · 📚 被引 6
- **作者**: Tianjiao Li, Lin Geng Foo, Ping Hu, Xindi Shang, Hossein Rahmani, Zehuan Yuan et al.
- **🏷️ 机构**: Singapore University of Technology and Design, Boston University, ByteDance
- **会议**: CVPR 2023

### SECAD-Net: Self-Supervised CAD Reconstruction by Learning Sketch-Extrude Operations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01613) · 📚 被引 50
- **作者**: Pu Li, Jianwei Guo, Xiaopeng Zhang, Dong-Ming Yan
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,MAIS
- **会议**: CVPR 2023

### Spatial-then-Temporal Self-Supervised Learning for Video Correspondence.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00226) · 📚 被引 10
- **作者**: Rui Li, Dong Liu
- **🏷️ 机构**: University of Science and Technology of China,Hefei,China
- **会议**: CVPR 2023

### Self-Supervised Blind Motion Deblurring with Deep Expectation Maximization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01344) · 📚 被引 15
- **作者**: Ji Li, Weixi Wang, Yuesong Nan, Hui Ji
- **🏷️ 机构**: National University of Singapore,Department of Mathematics,Singapore,119076
- **会议**: CVPR 2023

### Unified Mask Embedding and Correspondence Learning for Self-Supervised Video Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01794)
- **作者**: Liulei Li, Wenguan Wang, Tianfei Zhou, Jianwu Li, Yi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Spatially Adaptive Self-Supervised Learning for Real-World Image Denoising.
- **链接**: [arXiv:2303.14934](https://arxiv.org/abs/2303.14934) · [代码](https://github.com/nagejacob/SpatiallyAdaptiveSSID) · 📚 被引 58
- **作者**: Junyi Li, Zhilu Zhang, Xiaoyu Liu, Chaoyu Feng, Xiaotao Wang, Lei Lei et al.
- **🏷️ 机构**: School of Computer Science and Technology, Harbin Institute of Technology,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent approaches in self-supervised learning of image representations can be categorized into different families of methods and, in particular, can be divided into contrastive and non-contrastive approaches. While differences between the two families have been thoroughly discussed to motivate new approaches, we focus more on the theoretical similarities between them. By designing contrastive and covariance based non-contrastive criteria that can be related algebraically and shown to be equivalent under limited assumptions, we show how close those families can be. We further study popular methods and introduce variations of them, allowing us to relate this theoretical result to current practices and show the influence (or lack thereof) of design choices on downstream performance. Motivated by our equivalence result, we investigate the low performance of SimCLR and show how it can match VICReg's with careful hyperparameter tuning, improving significantly over known baselines. We also challenge the popular assumption that non-contrastive methods need large output dimensions. Our theoretical and quantitative results suggest that the numerical gaps between contrastive and non-contrastive methods in certain regimes can be closed given better network design choices and hyperparameter tuning. The evidence shows that unifying different SOTA methods is an important direction to build a better understanding of self-supervised learning.

</details>

### Pose-disentangled Contrastive Learning for Self-supervised Facial Representation.
- **链接**: [arXiv:2211.13490](https://arxiv.org/abs/2211.13490) · [代码](https://github.com/DreamMr/PCL) · 📚 被引 29
- **作者**: Yuanyuan Liu, Wenbin Wang, Yibing Zhan, Shaoze Feng, Kejun Liu, Zhe Chen
- **🏷️ 机构**: School of Computer Science, China University of Geosciences,Wuhan,China, JD Explore Academy,China, The University of Sydney,Australia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised facial representation has recently attracted increasing attention due to its ability to perform face understanding without relying on large-scale annotated datasets heavily. However, analytically, current contrastive-based self-supervised learning (SSL) still performs unsatisfactorily for learning facial representation. More specifically, existing contrastive learning (CL) tends to learn pose-invariant features that cannot depict the pose details of faces, compromising the learning performance. To conquer the above limitation of CL, we propose a novel Pose-disentangled Contrastive Learning (PCL) method for general self-supervised facial representation. Our PCL first devises a pose-disentangled decoder (PDD) with a delicately designed orthogonalizing regulation, which disentangles the pose-related features from the face-aware features; therefore, pose-related and other pose-unrelated facial information could be performed in individual subnetworks and do not affect each other's training. Furthermore, we introduce a pose-related contrastive learning scheme that learns pose-related information based on data augmentation of the same image, which would deliver more effective face-aware representation for various downstream tasks. We conducted linear evaluation on four challenging downstream facial understanding tasks, ie, facial expression recognition, face recognition, AU detection and head pose estimation. Experimental results demonstrate that our method significantly outperforms state-of-the-art SSL methods. Code is available at https://github.com/DreamMr/PCL}{https://github.com/DreamMr/PCL

</details>

### Multiple Instance Learning via Iterative Self-Paced Supervised Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00327) · 📚 被引 35
- **作者**: Kangning Liu, Weicheng Zhu, Yiqiu Shen, Sheng Liu, Narges Razavian, Krzysztof J. Geras et al.
- **🏷️ 机构**: NYU Center for Data Science, NYU Grossman School of Medicine
- **会议**: CVPR 2023

### Markerless Camera-to-Robot Pose Estimation via Self-Supervised Sim-to-Real Transfer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02040) · 📚 被引 29
- **作者**: Jingpei Lu, Florian Richter, Michael C. Yip
- **🏷️ 机构**: University of California,San Diego
- **会议**: CVPR 2023

### DrapeNet: Garment Generation and Self-Supervised Draping.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00146) · 📚 被引 51
- **作者**: Luca De Luigi, Ren Li, Benoît Guillard, Mathieu Salzmann, Pascal Fua
- **🏷️ 机构**: University of Bologna, EPFL,CVLab
- **会议**: CVPR 2023

### Self-Supervised Image-to-Point Distillation via Semantically Tolerant Contrastive Loss.
- **链接**: [arXiv:2301.05709](https://arxiv.org/abs/2301.05709) · 📚 被引 29
- **作者**: Anas Mahmoud, Jordan S. K. Hu, Tianshu Kuai, Ali Harakeh, Liam Paull, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute, Mila, Universit&#x00E9; de Montr&#x00E9;al
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An effective framework for learning 3D representations for perception tasks is distilling rich self-supervised image features via contrastive learning. However, image-to point representation learning for autonomous driving datasets faces two main challenges: 1) the abundance of self-similarity, which results in the contrastive losses pushing away semantically similar point and image regions and thus disturbing the local semantic structure of the learned representations, and 2) severe class imbalance as pretraining gets dominated by over-represented classes. We propose to alleviate the self-similarity problem through a novel semantically tolerant image-to-point contrastive loss that takes into consideration the semantic distance between positive and negative image regions to minimize contrasting semantically similar point and image regions. Additionally, we address class imbalance by designing a class-agnostic balanced loss that approximates the degree of class imbalance through an aggregate sample-to-samples semantic similarity measure. We demonstrate that our semantically-tolerant contrastive loss with class balancing improves state-of-the art 2D-to-3D representation learning in all evaluation settings on 3D semantic segmentation. Our method consistently outperforms state-of-the-art 2D-to-3D representation learning frameworks across a wide range of 2D self-supervised pretrained models.

</details>

### HaLP: Hallucinating Latent Positives for Skeleton-based Self-Supervised Learning of Actions.
- **链接**: [arXiv:2304.00387](https://arxiv.org/abs/2304.00387) · [代码](https://github.com/anshulbshah/HaLP) · 📚 被引 41
- **作者**: Anshul Shah, Aniket Roy, Ketul Shah, Shlok Mishra, David Jacobs, Anoop Cherian et al.
- **🏷️ 机构**: Johns Hopkins University, University of Maryland,College Park, MERL
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised learning of skeleton sequence encoders for action recognition has received significant attention in recent times. However, learning such encoders without labels continues to be a challenging problem. While prior works have shown promising results by applying contrastive learning to pose sequences, the quality of the learned representations is often observed to be closely tied to data augmentations that are used to craft the positives. However, augmenting pose sequences is a difficult task as the geometric constraints among the skeleton joints need to be enforced to make the augmentations realistic for that action. In this work, we propose a new contrastive learning approach to train models for skeleton-based action recognition without labels. Our key contribution is a simple module, HaLP - to Hallucinate Latent Positives for contrastive learning. Specifically, HaLP explores the latent space of poses in suitable directions to generate new positives. To this end, we present a novel optimization formulation to solve for the synthetic positives with an explicit control on their hardness. We propose approximations to the objective, making them solvable in closed form with minimal overhead. We show via experiments that using these generated positives within a standard contrastive learning framework leads to consistent improvements across benchmarks such as NTU-60, NTU-120, and PKU-II on tasks like linear evaluation, transfer learning, and kNN evaluation. Our code will be made available at https://github.com/anshulbshah/HaLP.

</details>

### Self-Supervised 3D Scene Flow Estimation Guided by Superpoints.
- **链接**: [arXiv:2305.02528](https://arxiv.org/abs/2305.02528) · 📚 被引 33
- **作者**: Yaqi Shen, Le Hui, Jin Xie, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,Nanjing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D scene flow estimation aims to estimate point-wise motions between two consecutive frames of point clouds. Superpoints, i.e., points with similar geometric features, are usually employed to capture similar motions of local regions in 3D scenes for scene flow estimation. However, in existing methods, superpoints are generated with the offline clustering methods, which cannot characterize local regions with similar motions for complex 3D scenes well, leading to inaccurate scene flow estimation. To this end, we propose an iterative end-to-end superpoint based scene flow estimation framework, where the superpoints can be dynamically updated to guide the point-level flow prediction. Specifically, our framework consists of a flow guided superpoint generation module and a superpoint guided flow refinement module. In our superpoint generation module, we utilize the bidirectional flow information at the previous iteration to obtain the matching points of points and superpoint centers for soft point-to-superpoint association construction, in which the superpoints are generated for pairwise point clouds. With the generated superpoints, we first reconstruct the flow for each point by adaptively aggregating the superpoint-level flow, and then encode the consistency between the reconstructed flow of pairwise point clouds. Finally, we feed the consistency encoding along with the reconstructed flow into GRU to refine point-level flow. Extensive experiments on several different datasets show that our method can achieve promising performance.

</details>

### Learning Common Rationale to Improve Self-Supervised Representation for Fine-Grained Visual Recognition Problems.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01096) · 📚 被引 25
- **作者**: Yangyang Shu, Anton van den Hengel, Lingqiao Liu
- **🏷️ 机构**: School of Computer Science, The University of Adelaide
- **会议**: CVPR 2023

### Multi-Mode Online Knowledge Distillation for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2304.06461](https://arxiv.org/abs/2304.06461) · 📚 被引 38
- **作者**: Kaiyou Song, Jin Xie, Shan Zhang, Zimeng Luo
- **🏷️ 机构**: Megvii Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrastive self-supervised learning, the common way to learn discriminative representation is to pull different augmented "views" of the same image closer while pushing all other images further apart, which has been proven to be effective. However, it is unavoidable to construct undesirable views containing different semantic concepts during the augmentation procedure. It would damage the semantic consistency of representation to pull these augmentations closer in the feature space indiscriminately. In this study, we introduce feature-level augmentation and propose a novel semantics-consistent feature search (SCFS) method to mitigate this negative effect. The main idea of SCFS is to adaptively search semantics-consistent features to enhance the contrast between semantics-consistent regions in different augmentations. Thus, the trained model can learn to focus on meaningful object regions, improving the semantic representation ability. Extensive experiments conducted on different datasets and tasks demonstrate that SCFS effectively improves the performance of self-supervised learning and achieves state-of-the-art performance on different downstream tasks.

</details>

### MAPConNet: Self-supervised 3D Pose Transfer with Mesh and Point Contrastive Learning.
- **链接**: [arXiv:2304.13819](https://arxiv.org/abs/2304.13819) · 📚 被引 3
- **作者**: Jiaze Sun, Zhixiang Chen, Tae-Kyun Kim
- **🏷️ 机构**: Imperial College London, University of Sheffield
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D pose transfer is a challenging generation task that aims to transfer the pose of a source geometry onto a target geometry with the target identity preserved. Many prior methods require keypoint annotations to find correspondence between the source and target. Current pose transfer methods allow end-to-end correspondence learning but require the desired final output as ground truth for supervision. Unsupervised methods have been proposed for graph convolutional models but they require ground truth correspondence between the source and target inputs. We present a novel self-supervised framework for 3D pose transfer which can be trained in unsupervised, semi-supervised, or fully supervised settings without any correspondence labels. We introduce two contrastive learning constraints in the latent space: a mesh-level loss for disentangling global patterns including pose and identity, and a point-level loss for discriminating local semantics. We demonstrate quantitatively and qualitatively that our method achieves state-of-the-art results in supervised 3D pose transfer, with comparable results in unsupervised and semi-supervised settings. Our method is also generalisable to unseen human and animal data with complex topologies.

</details>

### Self-supervised Cross-view Representation Reconstruction for Change Captioning.
- **链接**: [arXiv:2309.16283](https://arxiv.org/abs/2309.16283) · [代码](https://github.com/tuyunbin/SCORER) · 📚 被引 33
- **作者**: Yunbin Tu, Liang Li, Li Su, Zheng-Jun Zha, Chenggang Yan, Qingming Huang
- **🏷️ 机构**: University of Chinese Academy of Sciences,Beijing,China, ICT, CAS,Key Lab of Intelligent Information Processing,Beijing,China, University of Science and Technology of China,Hefei,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Change captioning aims to describe the difference between a pair of similar images. Its key challenge is how to learn a stable difference representation under pseudo changes caused by viewpoint change. In this paper, we address this by proposing a self-supervised cross-view representation reconstruction (SCORER) network. Concretely, we first design a multi-head token-wise matching to model relationships between cross-view features from similar/dissimilar images. Then, by maximizing cross-view contrastive alignment of two similar images, SCORER learns two view-invariant image representations in a self-supervised way. Based on these, we reconstruct the representations of unchanged objects by cross-attention, thus learning a stable difference representation for caption generation. Further, we devise a cross-modal backward reasoning to improve the quality of caption. This module reversely models a ``hallucination'' representation with the caption and ``before'' representation. By pushing it closer to the ``after'' representation, we enforce the caption to be informative about the difference in a self-supervised manner. Extensive experiments show our method achieves the state-of-the-art results on four datasets. The code is available at https://github.com/tuyunbin/SCORER.

</details>

### Self-supervised Monocular Underwater Depth Recovery, Image Restoration, and a Real-sea Video Dataset.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01125) · 📚 被引 32
- **作者**: Nisha Varghese, Ashish Kumar, A. N. Rajagopalan
- **🏷️ 机构**: Indian Institute of Technology Madras,India
- **会议**: ICCV 2023

### Noise2Info: Noisy Image to Information of Noise for Self-Supervised Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01469) · 📚 被引 17
- **作者**: Jiachuan Wang, Shimin Di, Lei Chen, Charles Wang Wai Ng
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Hong Kong SAR,China
- **会议**: ICCV 2023

### Creative Birds: Self-Supervised Single-View 3D Style Transfer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00806) · 📚 被引 4
- **作者**: Renke Wang, Guimin Que, Shuo Chen, Xiang Li, Jun Li, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,China, RIKEN, Nankai University
- **会议**: ICCV 2023

### Denoising Diffusion Autoencoders are Unified Self-supervised Learners.
- **链接**: [arXiv:2303.09769](https://arxiv.org/abs/2303.09769) · [代码](https://github.com/FutureXiang/ddae) · 📚 被引 62
- **作者**: Weilai Xiang, Hongyu Yang, Di Huang, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,Beijing,China, Beihang University,School of Computer Science and Engineering,Beijing,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by recent advances in diffusion models, which are reminiscent of denoising autoencoders, we investigate whether they can acquire discriminative representations for classification via generative pre-training. This paper shows that the networks in diffusion models, namely denoising diffusion autoencoders (DDAE), are unified self-supervised learners: by pre-training on unconditional image generation, DDAE has already learned strongly linear-separable representations within its intermediate layers without auxiliary encoders, thus making diffusion pre-training emerge as a general approach for generative-and-discriminative dual learning. To validate this, we conduct linear probe and fine-tuning evaluations. Our diffusion-based approach achieves 95.9% and 50.0% linear evaluation accuracies on CIFAR-10 and Tiny-ImageNet, respectively, and is comparable to contrastive learning and masked autoencoders for the first time. Transfer learning from ImageNet also confirms the suitability of DDAE for Vision Transformers, suggesting the potential to scale DDAEs as unified foundation models. Code is available at github.com/FutureXiang/ddae.

</details>

### Stable and Causal Inference for Discriminative Self-supervised Deep Visual Representations.
- **链接**: [arXiv:2308.08321](https://arxiv.org/abs/2308.08321) · 📚 被引 1
- **作者**: Yuewei Yang, Hai Li, Yiran Chen
- **🏷️ 机构**: Duke University,Durham,USA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, discriminative self-supervised methods have made significant strides in advancing various visual tasks. The central idea of learning a data encoder that is robust to data distortions/augmentations is straightforward yet highly effective. Although many studies have demonstrated the empirical success of various learning methods, the resulting learned representations can exhibit instability and hinder downstream performance. In this study, we analyze discriminative self-supervised methods from a causal perspective to explain these unstable behaviors and propose solutions to overcome them. Our approach draws inspiration from prior works that empirically demonstrate the ability of discriminative self-supervised methods to demix ground truth causal sources to some extent. Unlike previous work on causality-empowered representation learning, we do not apply our solutions during the training process but rather during the inference process to improve time efficiency. Through experiments on both controlled image datasets and realistic image datasets, we show that our proposed solutions, which involve tempering a linear transformation with controlled synthetic data, are effective in addressing these issues.

</details>

### Self-supervised Learning of Implicit Shape Representation with Dense Correspondence for Deformable Objects.
- **链接**: [arXiv:2308.12590](https://arxiv.org/abs/2308.12590) · 📚 被引 4
- **作者**: Baowen Zhang, Jiahe Li, Xiaoming Deng, Yinda Zhang, Cuixia Ma, Hongan Wang
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Software, Google
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning 3D shape representation with dense correspondence for deformable objects is a fundamental problem in computer vision. Existing approaches often need additional annotations of specific semantic domain, e.g., skeleton poses for human bodies or animals, which require extra annotation effort and suffer from error accumulation, and they are limited to specific domain. In this paper, we propose a novel self-supervised approach to learn neural implicit shape representation for deformable objects, which can represent shapes with a template shape and dense correspondence in 3D. Our method does not require the priors of skeleton and skinning weight, and only requires a collection of shapes represented in signed distance fields. To handle the large deformation, we constrain the learned template shape in the same latent space with the training shapes, design a new formulation of local rigid constraint that enforces rigid transformation in local region and addresses local reflection issue, and present a new hierarchical rigid constraint to reduce the ambiguity due to the joint learning of template shape and correspondences. Extensive experiments show that our model can represent shapes with large deformations. We also show that our shape representation can support two typical applications, such as texture transfer and shape editing, with competitive performance. The code and models are available at https://iscas3dv.github.io/deformshape

</details>

### Modeling the Relative Visual Tempo for Self-supervised Skeleton-based Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01279) · 📚 被引 35
- **作者**: Yisheng Zhu, Hu Han, Zhengtao Yu, Guangcan Liu
- **🏷️ 机构**: Nanjing University of Posts and Telecommunications, Chinese Academy of Sciences (CAS),Key Laboratory of Intelligent Information Processing, Institute of Computing Technology (ICT), Kunming University of Science and Technology,Faculty of Information Engineering and Automation
- **会议**: ICCV 2023

### Multi-Label Self-Supervised Learning with Scene Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00616) · 📚 被引 17
- **作者**: Ke Zhu, Minghao Fu, Jianxin Wu
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China
- **会议**: ICCV 2023

### Iterative Denoiser and Noise Estimator for Self-Supervised Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01220) · 📚 被引 17
- **作者**: Yunhao Zou, Chenggang Yan, Ying Fu
- **🏷️ 机构**: Beijing Institute of Technology, Hangzhou Dianzi University
- **会议**: ICCV 2023

### Can Self-Supervised Representation Learning Methods Withstand Distribution Shifts and Corruptions?
- **链接**: [arXiv:2308.02525](https://arxiv.org/abs/2308.02525) · 📚 被引 6
- **作者**: Prakash Chandra Chhipa, Johan Rodahl Holmgren, Kanjar De, Rajkumar Saini, Marcus Liwicki
- **🏷️ 机构**: Lule&#x00E5; Tekniska Universitet,Machine Learning Group, EISLAB,Lule&#x00E5;,Sweden
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning in computer vision aims to leverage the inherent structure and relationships within data to learn meaningful representations without explicit human annotation, enabling a holistic understanding of visual scenes. Robustness in vision machine learning ensures reliable and consistent performance, enhancing generalization, adaptability, and resistance to noise, variations, and adversarial attacks. Self-supervised paradigms, namely contrastive learning, knowledge distillation, mutual information maximization, and clustering, have been considered to have shown advances in invariant learning representations. This work investigates the robustness of learned representations of self-supervised learning approaches focusing on distribution shifts and image corruptions in computer vision. Detailed experiments have been conducted to study the robustness of self-supervised learning methods on distribution shifts and image corruptions. The empirical analysis demonstrates a clear relationship between the performance of learned representations within self-supervised paradigms and the severity of distribution shifts and corruptions. Notably, higher levels of shifts and corruptions are found to significantly diminish the robustness of the learned representations. These findings highlight the critical impact of distribution shifts and image corruptions on the performance and resilience of self-supervised learning methods, emphasizing the need for effective strategies to mitigate their adverse effects. The study strongly advocates for future research in the field of self-supervised representation learning to prioritize the key aspects of safety and robustness in order to ensure practical applicability. The source code and results are available on GitHub.

</details>

### Contrastive Image Synthesis and Self-supervised Feature Adaptation for Cross-Modality Biomedical Image Segmentation.
- **链接**: [arXiv:2207.13240](https://arxiv.org/abs/2207.13240) · 📚 被引 3
- **作者**: Xinrong Hu, Corey Wang, Yiyu Shi
- **🏷️ 机构**: University of Notre Dame,Department of Computer Science and Engineering, Northwestern University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work presents a novel framework CISFA (Contrastive Image synthesis and Self-supervised Feature Adaptation)that builds on image domain translation and unsupervised feature adaptation for cross-modality biomedical image segmentation. Different from existing works, we use a one-sided generative model and add a weighted patch-wise contrastive loss between sampled patches of the input image and the corresponding synthetic image, which serves as shape constraints. Moreover, we notice that the generated images and input images share similar structural information but are in different modalities. As such, we enforce contrastive losses on the generated images and the input images to train the encoder of a segmentation model to minimize the discrepancy between paired images in the learned embedding space. Compared with existing works that rely on adversarial learning for feature adaptation, such a method enables the encoder to learn domain-independent features in a more explicit way. We extensively evaluate our methods on segmentation tasks containing CT and MRI images for abdominal cavities and whole hearts. Experimental results show that the proposed framework not only outputs synthetic images with less distortion of organ shapes, but also outperforms state-of-the-art domain adaptation methods by a large margin.

</details>

### Self-supervised Semantic Segmentation: Consistency over Transformation.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00280) · 📚 被引 6
- **作者**: Sanaz Karimijafarbigloo, Reza Azad, Amirhossein Kazerouni, Yury Velichko, Ulas Bagci, Dorit Merhof
- **🏷️ 机构**: University of Regensburg,Faculty of Informatics and Data Science,Germany, RWTH Aachen University,Faculty of Electrical Engineering and Information Technology,Germany, Iran University of Science and Technology,School of Electrical Engineering,Iran
- **会议**: ICCV 2023

### NU-Net: a self-supervised smart filter for enhancing blobs in bioimages.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00420) · 📚 被引 0
- **作者**: Seongbin Lim, Emmanuel Beaurepaire, Anatole Chessel
- **🏷️ 机构**: Institut Polytechnique de Paris,Laboratoire d&#x2019;Optique et Biosciences, CNRS, INSERM, &#x00C9;cole Polytechnique,Cedex,France
- **会议**: ICCV 2023

### Frequency-Aware Self-Supervised Long-Tailed Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00103) · 📚 被引 0
- **作者**: Ci-Siang Lin, Min-Hung Chen, Yu-Chiang Frank Wang
- **🏷️ 机构**: National Taiwan University,Graduate Institute of Communication Engineering,Taiwan, Nvidia,Taiwan
- **会议**: ICCV 2023

### Self-supervised Hypergraphs for Learning Multiple World Interpretations.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00105) · 📚 被引 9
- **作者**: Alina Marcu, Mihai Cristian Pîrvu, Dragos Costea, Emanuela Haller, Emil Slusanschi, Nabil Belbachir et al.
- **🏷️ 机构**: UPB, Bitdefender, NORCE
- **会议**: ICCV 2023

### DeepVAT: A Self-Supervised Technique for Cluster Assessment in Image Datasets.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00026) · 📚 被引 2
- **作者**: Alokendu Mazumder, Tirthajit Baruah, Akash Kumar Singh, Pagadala Krishna Murthy, Vishwajeet Pattanaik, Punit Rathore
- **🏷️ 机构**: Indian Institute of Science Bangalore,India, Indian Institute of Science Education and Research Bhopal,India
- **会议**: ICCV 2023

### Self-Supervised Anomaly Detection from Anomalous Training Data via Iterative Latent Token Masking.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00254) · 📚 被引 6
- **作者**: Ashay Patel, Petru-Daniel Tudosiu, Walter H. L. Pinaya, Mark S. Graham, Olusola Adeleke, Gary J. Cook et al.
- **🏷️ 机构**: King&#x2019;s College,London
- **会议**: ICCV 2023

### FedLID: Self-Supervised Federated Learning for Leveraging Limited Image Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00111) · 📚 被引 6
- **作者**: Athanasios Psaltis, Anestis Kastellos, Charalampos Z. Patrikakis, Petros Daras
- **🏷️ 机构**: Centre for Research and Technology Hellas,Thessaloniki,Greece, University of West Attica,Dept. of Electrical and Electronics Engineering,Athens,Greece
- **会议**: ICCV 2023

### Self-supervised Learning of Contextualized Local Visual Embeddings.
- **链接**: [arXiv:2310.00527](https://arxiv.org/abs/2310.00527) · 📚 被引 2
- **作者**: Thalles Silva, Hélio Pedrini, Adín Ramírez Rivera
- **🏷️ 机构**: University of Campinas,Institute of Computing,Campinas-SP,Brazil, University of Oslo,Department of Informatics,Oslo,Norway
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Contextualized Local Visual Embeddings (CLoVE), a self-supervised convolutional-based method that learns representations suited for dense prediction tasks. CLoVE deviates from current methods and optimizes a single loss function that operates at the level of contextualized local embeddings learned from output feature maps of convolution neural network (CNN) encoders. To learn contextualized embeddings, CLoVE proposes a normalized mult-head self-attention layer that combines local features from different parts of an image based on similarity. We extensively benchmark CLoVE's pre-trained representations on multiple datasets. CLoVE reaches state-of-the-art performance for CNN-based architectures in 4 dense prediction downstream tasks, including object detection, instance segmentation, keypoint detection, and dense pose estimation.

</details>

### A Horse with no Labels: Self-Supervised Horse Pose Estimation from Unlabelled Images and Synthetic Prior.
- **链接**: [arXiv:2308.03411](https://arxiv.org/abs/2308.03411) · 📚 被引 0
- **作者**: Jose Sosa, David C. Hogg
- **🏷️ 机构**: University of Leeds,School of Computing
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Obtaining labelled data to train deep learning methods for estimating animal pose is challenging. Recently, synthetic data has been widely used for pose estimation tasks, but most methods still rely on supervised learning paradigms utilising synthetic images and labels. Can training be fully unsupervised? Is a tiny synthetic dataset sufficient? What are the minimum assumptions that we could make for estimating animal pose? Our proposal addresses these questions through a simple yet effective self-supervised method that only assumes the availability of unlabelled images and a small set of synthetic 2D poses. We completely remove the need for any 3D or 2D pose annotations (or complex 3D animal models), and surprisingly our approach can still learn accurate 3D and 2D poses simultaneously. We train our method with unlabelled images of horses mainly collected for YouTube videos and a prior consisting of 2D synthetic poses. The latter is three times smaller than the number of images needed for training. We test our method on a challenging set of horse images and evaluate the predicted 3D and 2D poses. We demonstrate that it is possible to learn accurate animal poses even with as few assumptions as unlabelled images and a small set of 2D poses generated from synthetic data. Given the minimum requirements and the abundance of unlabelled data, our method could be easily deployed to different animals.

</details>

### OMG-Attack: Self-Supervised On-Manifold Generation of Transferable Evasion Attacks.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00397) · 📚 被引 1
- **作者**: Ofir Bar Tal, Adi Haviv, Amit H. Bermano
- **🏷️ 机构**: Tel Aviv University
- **会议**: ICCV 2023

### Efficient, Self-Supervised Human Pose Estimation with Inductive Prior Tuning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00351) · 📚 被引 2
- **作者**: Nobline Yoo, Olga Russakovsky
- **🏷️ 机构**: Princeton University
- **会议**: ICCV 2023

### Pointing Gesture Recognition via Self-supervised Regularization for ASD Screening.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00326) · 📚 被引 3
- **作者**: Cheol-Hwan Yoo, Jang-Hee Yoo, Ho-Won Kim, ByungOk Han
- **🏷️ 机构**: ETRI,Daejeon,Republic of Korea
- **会议**: ICCV 2023

### Contrastive Learning Relies More on Spatial Inductive Bias Than Supervised Learning: An Empirical Study.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01496) · 📚 被引 3
- **作者**: Yuanyi Zhong, Haoran Tang, Jun-Kun Chen, Yu-Xiong Wang
- **🏷️ 机构**: University of Illinois at Urbana-Champaign, University of Pennsylvania
- **会议**: ICCV 2023

### One-shot recognition of any material anywhere using contrastive learning with physics-based rendering.
- **链接**: [arXiv:2212.00648](https://arxiv.org/abs/2212.00648) · 📚 被引 8
- **作者**: Manuel S. Drehwald, Sagi Eppel, Jolina Li, Han Hao, Alán Aspuru-Guzik
- **🏷️ 机构**: Karlsruhe Institute of Technology, Vector Institute, University of Toronto
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual recognition of materials and their states is essential for understanding most aspects of the world, from determining whether food is cooked, metal is rusted, or a chemical reaction has occurred. However, current image recognition methods are limited to specific classes and properties and can't handle the vast number of material states in the world. To address this, we present MatSim: the first dataset and benchmark for computer vision-based recognition of similarities and transitions between materials and textures, focusing on identifying any material under any conditions using one or a few examples. The dataset contains synthetic and natural images. The synthetic images were rendered using giant collections of textures, objects, and environments generated by computer graphics artists. We use mixtures and gradual transitions between materials to allow the system to learn cases with smooth transitions between states (like gradually cooked food). We also render images with materials inside transparent containers to support beverage and chemistry lab use cases. We use this dataset to train a siamese net that identifies the same material in different objects, mixtures, and environments. The descriptor generated by this net can be used to identify the states of materials and their subclasses using a single image. We also present the first few-shot material recognition benchmark with images from a wide range of fields, including the state of foods and drinks, types of grounds, and many other use cases. We show that a net trained on the MatSim synthetic dataset outperforms state-of-the-art models like Clip on the benchmark and also achieves good results on other unsupervised material classification tasks.

</details>

### All4One: Symbiotic Neighbour Contrastive Learning via Self-Attention and Redundancy Reduction.
- **链接**: [arXiv:2303.09417](https://arxiv.org/abs/2303.09417) · 📚 被引 12
- **作者**: Imanol G. Estepa, Ignacio Sarasúa, Bhalaji Nagarajan, Petia Radeva
- **🏷️ 机构**: Universitat de Barcelona,Barcelona,Spain, NVIDIA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Nearest neighbour based methods have proved to be one of the most successful self-supervised learning (SSL) approaches due to their high generalization capabilities. However, their computational efficiency decreases when more than one neighbour is used. In this paper, we propose a novel contrastive SSL approach, which we call All4One, that reduces the distance between neighbour representations using ''centroids'' created through a self-attention mechanism. We use a Centroid Contrasting objective along with single Neighbour Contrasting and Feature Contrasting objectives. Centroids help in learning contextual information from multiple neighbours whereas the neighbour contrast enables learning representations directly from the neighbours and the feature contrast allows learning representations unique to the features. This combination enables All4One to outperform popular instance discrimination approaches by more than 1% on linear classification evaluation for popular benchmark datasets and obtains state-of-the-art (SoTA) results. Finally, we show that All4One is robust towards embedding dimensionalities and augmentations, surpassing NNCLR and Barlow Twins by more than 5% on low dimensionality and weak augmentation settings. The source code would be made available soon.

</details>

### Hierarchical Contrastive Learning for Pattern-Generalizable Image Corruption Detection.
- **链接**: [arXiv:2308.14061](https://arxiv.org/abs/2308.14061) · [代码](https://github.com/xyfJASON/HCL) · 📚 被引 5
- **作者**: Xin Feng, Yifeng Xu, Guangming Lu, Wenjie Pei
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Effective image restoration with large-size corruptions, such as blind image inpainting, entails precise detection of corruption region masks which remains extremely challenging due to diverse shapes and patterns of corruptions. In this work, we present a novel method for automatic corruption detection, which allows for blind corruption restoration without known corruption masks. Specifically, we develop a hierarchical contrastive learning framework to detect corrupted regions by capturing the intrinsic semantic distinctions between corrupted and uncorrupted regions. In particular, our model detects the corrupted mask in a coarse-to-fine manner by first predicting a coarse mask by contrastive learning in low-resolution feature space and then refines the uncertain area of the mask by high-resolution contrastive learning. A specialized hierarchical interaction mechanism is designed to facilitate the knowledge propagation of contrastive learning in different scales, boosting the modeling performance substantially. The detected multi-scale corruption masks are then leveraged to guide the corruption restoration. Detecting corrupted regions by learning the contrastive distinctions rather than the semantic patterns of corruptions, our model has well generalization ability across different corruption patterns. Extensive experiments demonstrate following merits of our model: 1) the superior performance over other methods on both corruption detection and various image restoration tasks including blind inpainting and watermark removal, and 2) strong generalization across different corruption patterns such as graffiti, random noise or other image content. Codes and trained weights are available at https://github.com/xyfJASON/HCL .

</details>

### Subclass-balancing Contrastive Learning for Long-tailed Recognition.
- **链接**: [arXiv:2306.15925](https://arxiv.org/abs/2306.15925) · 📚 被引 44
- **作者**: Chengkai Hou, Jieyu Zhang, Haonan Wang, Tianyi Zhou
- **🏷️ 机构**: Jilin University, University of Washington, National University of Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-tailed recognition with imbalanced class distribution naturally emerges in practical machine learning applications. Existing methods such as data reweighing, resampling, and supervised contrastive learning enforce the class balance with a price of introducing imbalance between instances of head class and tail class, which may ignore the underlying rich semantic substructures of the former and exaggerate the biases in the latter. We overcome these drawbacks by a novel ``subclass-balancing contrastive learning (SBCL)'' approach that clusters each head class into multiple subclasses of similar sizes as the tail classes and enforce representations to capture the two-layer class hierarchy between the original classes and their subclasses. Since the clustering is conducted in the representation space and updated during the course of training, the subclass labels preserve the semantic substructures of head classes. Meanwhile, it does not overemphasize tail class samples, so each individual instance contribute to the representation learning equally. Hence, our method achieves both the instance- and subclass-balance, while the original class labels are also learned through contrastive learning among subclasses from different classes. We evaluate SBCL over a list of long-tailed benchmark datasets and it achieves the state-of-the-art performance. In addition, we present extensive analyses and ablation studies of SBCL to verify its advantages.

</details>

### Unsupervised Domain Adaptation for Training Event-Based Networks Using Contrastive Learning and Uncorrelated Conditioning.
- **链接**: [arXiv:2303.12424](https://arxiv.org/abs/2303.12424) · 📚 被引 15
- **作者**: Dayuan Jian, Mohammad Rostami
- **🏷️ 机构**: University of Southern California
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Event-based cameras offer reliable measurements for preforming computer vision tasks in high-dynamic range environments and during fast motion maneuvers. However, adopting deep learning in event-based vision faces the challenge of annotated data scarcity due to recency of event cameras. Transferring the knowledge that can be obtained from conventional camera annotated data offers a practical solution to this challenge. We develop an unsupervised domain adaptation algorithm for training a deep network for event-based data image classification using contrastive learning and uncorrelated conditioning of data. Our solution outperforms the existing algorithms for this purpose.

</details>

### SCOB: Universal Text Understanding via Character-wise Supervised Contrastive Learning with Online Text Rendering for Bridging Domain Gap.
- **链接**: [arXiv:2309.12382](https://arxiv.org/abs/2309.12382) · [代码](https://github.com/naver-ai/scob) · 📚 被引 3
- **作者**: Daehee Kim, Yoonsik Kim, Donghyun Kim, Yumin Lim, Geewook Kim, Taeho Kil
- **🏷️ 机构**: NAVER Cloud AI, Seoul National University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by the great success of language model (LM)-based pre-training, recent studies in visual document understanding have explored LM-based pre-training methods for modeling text within document images. Among them, pre-training that reads all text from an image has shown promise, but often exhibits instability and even fails when applied to broader domains, such as those involving both visual documents and scene text images. This is a substantial limitation for real-world scenarios, where the processing of text image inputs in diverse domains is essential. In this paper, we investigate effective pre-training tasks in the broader domains and also propose a novel pre-training method called SCOB that leverages character-wise supervised contrastive learning with online text rendering to effectively pre-train document and scene text domains by bridging the domain gap. Moreover, SCOB enables weakly supervised learning, significantly reducing annotation costs. Extensive benchmarks demonstrate that SCOB generally improves vanilla pre-training methods and achieves comparable performance to state-of-the-art methods. Our findings suggest that SCOB can be served generally and effectively for read-type pre-training methods. The code will be available at https://github.com/naver-ai/scob.

</details>

### SeeABLE: Soft Discrepancies and Bounded Contrastive Learning for Exposing Deepfakes.
- **链接**: [arXiv:2211.11296](https://arxiv.org/abs/2211.11296) · 📚 被引 48
- **作者**: Nicolas Larue, Ngoc-Son Vu, Vitomir Struc, Peter Peer, Vassilis Christophides
- **🏷️ 机构**: ETIS - CY Cergy Paris University,ENSEA, CNRS,France, University of Ljubljana,Slovenia
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern deepfake detectors have achieved encouraging results, when training and test images are drawn from the same data collection. However, when these detectors are applied to images produced with unknown deepfake-generation techniques, considerable performance degradations are commonly observed. In this paper, we propose a novel deepfake detector, called SeeABLE, that formalizes the detection problem as a (one-class) out-of-distribution detection task and generalizes better to unseen deepfakes. Specifically, SeeABLE first generates local image perturbations (referred to as soft-discrepancies) and then pushes the perturbed faces towards predefined prototypes using a novel regression-based bounded contrastive loss. To strengthen the generalization performance of SeeABLE to unknown deepfake types, we generate a rich set of soft discrepancies and train the detector: (i) to localize, which part of the face was modified, and (ii) to identify the alteration type. To demonstrate the capabilities of SeeABLE, we perform rigorous experiments on several widely-used deepfake datasets and show that our model convincingly outperforms competing state-of-the-art detectors, while exhibiting highly encouraging generalization capabilities.

</details>

### JOTR: 3D Joint Contrastive Learning with Transformers for Occluded Human Mesh Recovery.
- **链接**: [arXiv:2307.16377](https://arxiv.org/abs/2307.16377) · 📚 被引 27
- **作者**: Jiahao Li, Zongxin Yang, Xiaohan Wang, Jianxin Ma, Chang Zhou, Yi Yang
- **🏷️ 机构**: Zhejiang University,ReLER, CCAI, Alibaba Group,DAMO Academy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we focus on the problem of 3D human mesh recovery from a single image under obscured conditions. Most state-of-the-art methods aim to improve 2D alignment technologies, such as spatial averaging and 2D joint sampling. However, they tend to neglect the crucial aspect of 3D alignment by improving 3D representations. Furthermore, recent methods struggle to separate the target human from occlusion or background in crowded scenes as they optimize the 3D space of target human with 3D joint coordinates as local supervision. To address these issues, a desirable method would involve a framework for fusing 2D and 3D features and a strategy for optimizing the 3D space globally. Therefore, this paper presents 3D JOint contrastive learning with TRansformers (JOTR) framework for handling occluded 3D human mesh recovery. Our method includes an encoder-decoder transformer architecture to fuse 2D and 3D representations for achieving 2D$\&$3D aligned results in a coarse-to-fine manner and a novel 3D joint contrastive learning approach for adding explicitly global supervision for the 3D feature space. The contrastive learning approach includes two contrastive losses: joint-to-joint contrast for enhancing the similarity of semantically similar voxels (i.e., human joints), and joint-to-non-joint contrast for ensuring discrimination from others (e.g., occlusions and background). Qualitative and quantitative analyses demonstrate that our method outperforms state-of-the-art competitors on both occlusion-specific and standard benchmarks, significantly improving the reconstruction of occluded humans.

</details>

### Semantic Information in Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00523)
- **作者**: Shengjiang Quan, Masahiro Hirano, Yuji Yamakawa
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### SMOC-Net: Leveraging Camera Pose for Self-Supervised Monocular Object Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02041) · 📚 被引 18
- **作者**: Tao Tan, Qiulei Dong
- **🏷️ 机构**: School of Artificial Intelligence, UCAS
- **会议**: CVPR 2023

### Unilaterally Aggregated Contrastive Learning with Hierarchical Augmentation for Anomaly Detection.
- **链接**: [arXiv:2308.10155](https://arxiv.org/abs/2308.10155) · 📚 被引 5
- **作者**: Guodong Wang, Yunhong Wang, Jie Qin, Dongming Zhang, Xiuguo Bao, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, Beihang University,School of Computer Science and Engineering,Beijing,China, NUAA,College of Computer Science and Technology,Nanjing,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection (AD), aiming to find samples that deviate from the training distribution, is essential in safety-critical applications. Though recent self-supervised learning based attempts achieve promising results by creating virtual outliers, their training objectives are less faithful to AD which requires a concentrated inlier distribution as well as a dispersive outlier distribution. In this paper, we propose Unilaterally Aggregated Contrastive Learning with Hierarchical Augmentation (UniCon-HA), taking into account both the requirements above. Specifically, we explicitly encourage the concentration of inliers and the dispersion of virtual outliers via supervised and unsupervised contrastive losses, respectively. Considering that standard contrastive data augmentation for generating positive views may induce outliers, we additionally introduce a soft mechanism to re-weight each augmented inlier according to its deviation from the inlier distribution, to ensure a purified concentration. Moreover, to prompt a higher concentration, inspired by curriculum learning, we adopt an easy-to-hard hierarchical augmentation strategy and perform contrastive aggregation at different depths of the network based on the strengths of data augmentation. Our method is evaluated under three AD settings including unlabeled one-class, unlabeled multi-class, and labeled multi-class, demonstrating its consistent superiority over other competitors.

</details>

### Boosting Novel Category Discovery Over Domains with Soft Contrastive Learning and All in One Classifier.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01089) · 📚 被引 18
- **作者**: Zelin Zang, Lei Shang, Senqiao Yang, Fei Wang, Baigui Sun, Xuansong Xie et al.
- **🏷️ 机构**: Westlake University, Alibaba Group
- **会议**: ICCV 2023

### Weakly-Supervised Text-driven Contrastive Learning for Facial Behavior Understanding.
- **链接**: [arXiv:2304.00058](https://arxiv.org/abs/2304.00058) · 📚 被引 23
- **作者**: Xiang Zhang, Taoyue Wang, Xiaotian Li, Huiyuan Yang, Lijun Yin
- **🏷️ 机构**: State University of New York,Binghamton, Rice University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has shown promising potential for learning robust representations by utilizing unlabeled data. However, constructing effective positive-negative pairs for contrastive learning on facial behavior datasets remains challenging. This is because such pairs inevitably encode the subject-ID information, and the randomly constructed pairs may push similar facial images away due to the limited number of subjects in facial behavior datasets. To address this issue, we propose to utilize activity descriptions, coarse-grained information provided in some datasets, which can provide high-level semantic information about the image sequences but is often neglected in previous studies. More specifically, we introduce a two-stage Contrastive Learning with Text-Embeded framework for Facial behavior understanding (CLEF). The first stage is a weakly-supervised contrastive learning method that learns representations from positive-negative pairs constructed using coarse-grained activity information. The second stage aims to train the recognition of facial expressions or facial action units by maximizing the similarity between image and the corresponding text label names. The proposed CLEF achieves state-of-the-art performance on three in-the-lab datasets for AU recognition and three in-the-wild datasets for facial expression recognition.

</details>

### Pre-training-free Image Manipulation Localization through Non-Mutually Exclusive Contrastive Learning.
- **链接**: [arXiv:2309.14900](https://arxiv.org/abs/2309.14900) · [代码](https://github.com/Knightzjz/NCL-IML) · 📚 被引 49
- **作者**: Jizhe Zhou, Xiaochen Ma, Xia Du, Ahmed Y. Al Hammadi, Wentao Feng
- **🏷️ 机构**: Sichuan University,College of Computer Science, Xiamen University of Technology,School of Computer and Information Engineering, Mohamed Bin Zayed University for Humanities,Strategy Affairs Office
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep Image Manipulation Localization (IML) models suffer from training data insufficiency and thus heavily rely on pre-training. We argue that contrastive learning is more suitable to tackle the data insufficiency problem for IML. Crafting mutually exclusive positives and negatives is the prerequisite for contrastive learning. However, when adopting contrastive learning in IML, we encounter three categories of image patches: tampered, authentic, and contour patches. Tampered and authentic patches are naturally mutually exclusive, but contour patches containing both tampered and authentic pixels are non-mutually exclusive to them. Simply abnegating these contour patches results in a drastic performance loss since contour patches are decisive to the learning outcomes. Hence, we propose the Non-mutually exclusive Contrastive Learning (NCL) framework to rescue conventional contrastive learning from the above dilemma. In NCL, to cope with the non-mutually exclusivity, we first establish a pivot structure with dual branches to constantly switch the role of contour patches between positives and negatives while training. Then, we devise a pivot-consistent loss to avoid spatial corruption caused by the role-switching process. In this manner, NCL both inherits the self-supervised merits to address the data insufficiency and retains a high manipulation localization accuracy. Extensive experiments verify that our NCL achieves state-of-the-art performance on all five benchmarks without any pre-training and is more robust on unseen real-life samples. The code is available at: https://github.com/Knightzjz/NCL-IML.

</details>

### PatchCraft Self-Supervised Training for Correlated Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00561) · 📚 被引 13
- **作者**: Gregory Vaksman, Michael Elad
- **🏷️ 机构**: CS Department - The Technion,Haifa,Israel
- **会议**: CVPR 2023

### Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00611)
- **作者**: Rui Wang, Dongdong Chen, Zuxuan Wu, Yinpeng Chen, Xiyang Dai, Mengchen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Augmenting Features via Contrastive Learning-based Generative Model for Long-Tailed Classification.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00108) · 📚 被引 1
- **作者**: Minho Park, Hyung-Il Kim, Hwa Jeon Song, Dong-oh Kang
- **🏷️ 机构**: Electronics and Telecommunications Research Institute (ETRI),South Korea
- **会议**: ICCV 2023

### PARTICLE: Part Discovery and Contrastive Learning for Fine-grained Recognition.
- **链接**: [arXiv:2309.13822](https://arxiv.org/abs/2309.13822) · 📚 被引 6
- **作者**: Oindrila Saha, Subhransu Maji
- **🏷️ 机构**: University of Massachusetts,Amherst
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vessel segmentation in medical images is one of the important tasks in the diagnosis of vascular diseases and therapy planning. Although learning-based segmentation approaches have been extensively studied, a large amount of ground-truth labels are required in supervised methods and confusing background structures make neural networks hard to segment vessels in an unsupervised manner. To address this, here we introduce a novel diffusion adversarial representation learning (DARL) model that leverages a denoising diffusion probabilistic model with adversarial learning, and apply it to vessel segmentation. In particular, for self-supervised vessel segmentation, DARL learns the background signal using a diffusion module, which lets a generation module effectively provide vessel representations. Also, by adversarial learning based on the proposed switchable spatially-adaptive denormalization, our model estimates synthetic fake vessel images as well as vessel segmentation masks, which further makes the model capture vessel-relevant semantic information. Once the proposed model is trained, the model generates segmentation masks in a single step and can be applied to general vascular structure segmentation of coronary angiography and retinal images. Experimental results on various datasets show that our method significantly outperforms existing unsupervised and self-supervised vessel segmentation methods.

</details>

### DLBD: A Self-Supervised Direct-Learned Binary Descriptor.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01521) · 📚 被引 7
- **作者**: Bin Xiao, Yang Hu, Bo Liu, Xiuli Bi, Weisheng Li, Xinbo Gao
- **🏷️ 机构**: Chongqing University of Posts and Telecommunications,Chongqing,China
- **会议**: CVPR 2023

### MAESTER: Masked Autoencoder Guided Segmentation at Pixel Resolution for Accurate, Self-Supervised Subcellular Structure Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00321) · 📚 被引 18
- **作者**: Ronald Xie, Kuan Pang, Gary D. Bader, Bo Wang
- **🏷️ 机构**: University of Toronto
- **会议**: CVPR 2023

### Self-Supervised Super-Plane for Neural 3D Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02051) · 📚 被引 13
- **作者**: Botao Ye, Sifei Liu, Xueting Li, Ming-Hsuan Yang
- **🏷️ 机构**: University of Chinese Academy of Sciences, NVIDIA, University of California,Merced
- **会议**: CVPR 2023

### CiCo: Domain-Aware Sign Language Retrieval via Cross-Lingual Contrastive Learning.
- **链接**: [arXiv:2303.12793](https://arxiv.org/abs/2303.12793) · [代码](https://github.com/FangyunWei/SLRT) · 📚 被引 33
- **作者**: Yiting Cheng, Fangyun Wei, Jianmin Bao, Dong Chen, Wenqiang Zhang
- **🏷️ 机构**: School of Computer Science, Fudan University, Microsoft Research Asia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work focuses on sign language retrieval-a recently proposed task for sign language understanding. Sign language retrieval consists of two sub-tasks: text-to-sign-video (T2V) retrieval and sign-video-to-text (V2T) retrieval. Different from traditional video-text retrieval, sign language videos, not only contain visual signals but also carry abundant semantic meanings by themselves due to the fact that sign languages are also natural languages. Considering this character, we formulate sign language retrieval as a cross-lingual retrieval problem as well as a video-text retrieval task. Concretely, we take into account the linguistic properties of both sign languages and natural languages, and simultaneously identify the fine-grained cross-lingual (i.e., sign-to-word) mappings while contrasting the texts and the sign videos in a joint embedding space. This process is termed as cross-lingual contrastive learning. Another challenge is raised by the data scarcity issue-sign language datasets are orders of magnitude smaller in scale than that of speech recognition. We alleviate this issue by adopting a domain-agnostic sign encoder pre-trained on large-scale sign videos into the target domain via pseudo-labeling. Our framework, termed as domain-aware sign language retrieval via Cross-lingual Contrastive learning or CiCo for short, outperforms the pioneering method by large margins on various datasets, e.g., +22.4 T2V and +28.0 V2T R@1 improvements on How2Sign dataset, and +13.7 T2V and +17.1 V2T R@1 improvements on PHOENIX-2014T dataset. Code and models are available at: https://github.com/FangyunWei/SLRT.

</details>

### Dynamic Graph Enhanced Contrastive Learning for Chest X-Ray Report Generation.
- **链接**: [arXiv:2303.10323](https://arxiv.org/abs/2303.10323) · 📚 被引 176
- **作者**: Mingjie Li, Bingqian Lin, Zicong Chen, Haokun Lin, Xiaodan Liang, Xiaojun Chang
- **🏷️ 机构**: AAII, University of Technology Sydney,ReLER, School of ISE, Sun Yat-Sen University, The University of Hong Kong
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Automatic radiology reporting has great clinical potential to relieve radiologists from heavy workloads and improve diagnosis interpretation. Recently, researchers have enhanced data-driven neural networks with medical knowledge graphs to eliminate the severe visual and textual bias in this task. The structures of such graphs are exploited by using the clinical dependencies formed by the disease topic tags via general knowledge and usually do not update during the training process. Consequently, the fixed graphs can not guarantee the most appropriate scope of knowledge and limit the effectiveness. To address the limitation, we propose a knowledge graph with Dynamic structure and nodes to facilitate medical report generation with Contrastive Learning, named DCL. In detail, the fundamental structure of our graph is pre-constructed from general knowledge. Then we explore specific knowledge extracted from the retrieved reports to add additional nodes or redefine their relations in a bottom-up manner. Each image feature is integrated with its very own updated graph before being fed into the decoder module for report generation. Finally, this paper introduces Image-Report Contrastive and Image-Report Matching losses to better represent visual features and textual information. Evaluated on IU-Xray and MIMIC-CXR datasets, our DCL outperforms previous state-of-the-art models on these two benchmarks.

</details>

### Promoting Semantic Connectivity: Dual Nearest Neighbors Contrastive Learning for Unsupervised Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00342) · 📚 被引 12
- **作者**: Yuchen Liu, Yaoming Wang, Yabo Chen, Wenrui Dai, Chenglin Li, Junni Zou et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering,China, Shanghai Jiao Tong University,Department of Computer Science and Engineering,China
- **会议**: CVPR 2023

### Class Prototypes based Contrastive Learning for Classifying Multi-Label and Fine-Grained Educational Videos.
- **链接**: [arXiv:2510.11204](https://arxiv.org/abs/2510.11204) · [代码](https://github.com/rohit-gupta/MMContrast) · 📚 被引 16
- **作者**: Rohit Gupta, Anirban Roy, Claire Christensen, Sujeong Kim, Sarah Gerard, Madeline Cincebeaux et al.
- **🏷️ 机构**: University of Central Florida,Center for Research in Computer Vision, SRI International
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent growth in the consumption of online media by children during early childhood necessitates data-driven tools enabling educators to filter out appropriate educational content for young learners. This paper presents an approach for detecting educational content in online videos. We focus on two widely used educational content classes: literacy and math. For each class, we choose prominent codes (sub-classes) based on the Common Core Standards. For example, literacy codes include `letter names', `letter sounds', and math codes include `counting', `sorting'. We pose this as a fine-grained multilabel classification problem as videos can contain multiple types of educational content and the content classes can get visually similar (e.g., `letter names' vs `letter sounds'). We propose a novel class prototypes based supervised contrastive learning approach that can handle fine-grained samples associated with multiple labels. We learn a class prototype for each class and a loss function is employed to minimize the distances between a class prototype and the samples from the class. Similarly, distances between a class prototype and the samples from other classes are maximized. As the alignment between visual and audio cues are crucial for effective comprehension, we consider a multimodal transformer network to capture the interaction between visual and audio cues in videos while learning the embedding for videos. For evaluation, we present a dataset, APPROVE, employing educational videos from YouTube labeled with fine-grained education classes by education researchers. APPROVE consists of 193 hours of expert-annotated videos with 19 classes. The proposed approach outperforms strong baselines on APPROVE and other benchmarks such as Youtube-8M, and COIN. The dataset is available at https://github.com/rohit-gupta/MMContrast/tree/main/APPROVE

</details>

### Pseudo-Label Guided Contrastive Learning for Semi-Supervised Medical Image Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01895) · 📚 被引 187
- **作者**: Hritam Basak, Zhaozheng Yin
- **🏷️ 机构**: Stony Brook University,NY,USA
- **会议**: CVPR 2023

### Weakly-Supervised Domain Adaptive Semantic Segmentation with Prototypical Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01481) · 📚 被引 30
- **作者**: Anurag Das, Yongqin Xian, Dengxin Dai, Bernt Schiele
- **🏷️ 机构**: Saarland Informatics Campus,MPI for Informatics, ETH Zurich
- **会议**: CVPR 2023

### MaskCon: Masked Contrastive Learning for Coarse-Labelled Dataset.
- **链接**: [arXiv:2303.12756](https://arxiv.org/abs/2303.12756) · [代码](https://github.com/MrChenFeng/MaskCon_CVPR2023) · 📚 被引 18
- **作者**: Chen Feng, Ioannis Patras
- **🏷️ 机构**: Queen Mary University of London,UK
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has achieved great success in recent years with the aid of advanced neural network structures and large-scale human-annotated datasets. However, it is often costly and difficult to accurately and efficiently annotate large-scale datasets, especially for some specialized domains where fine-grained labels are required. In this setting, coarse labels are much easier to acquire as they do not require expert knowledge. In this work, we propose a contrastive learning method, called $\textbf{Mask}$ed $\textbf{Con}$trastive learning~($\textbf{MaskCon}$) to address the under-explored problem setting, where we learn with a coarse-labelled dataset in order to address a finer labelling problem. More specifically, within the contrastive learning framework, for each sample our method generates soft-labels with the aid of coarse labels against other samples and another augmented view of the sample in question. By contrast to self-supervised contrastive learning where only the sample's augmentations are considered hard positives, and in supervised contrastive learning where only samples with the same coarse labels are considered hard positives, we propose soft labels based on sample distances, that are masked by the coarse labels. This allows us to utilize both inter-sample relations and coarse labels. We demonstrate that our method can obtain as special cases many existing state-of-the-art works and that it provides tighter bounds on the generalization error. Experimentally, our method achieves significant improvement over the current state-of-the-art in various datasets, including CIFAR10, CIFAR100, ImageNet-1K, Standford Online Products and Stanford Cars196 datasets. Code and annotations are available at https://github.com/MrChenFeng/MaskCon_CVPR2023.

</details>

### Hyperbolic Contrastive Learning for Visual Representations beyond Objects.
- **链接**: [arXiv:2212.00653](https://arxiv.org/abs/2212.00653) · [代码](https://github.com/shlokk/HCL) · 📚 被引 50
- **作者**: Songwei Ge, Shlok Mishra, Simon Kornblith, Chun-Liang Li, David Jacobs
- **🏷️ 机构**: University of Maryland,College Park, Google Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although self-/un-supervised methods have led to rapid progress in visual representation learning, these methods generally treat objects and scenes using the same lens. In this paper, we focus on learning representations for objects and scenes that preserve the structure among them. Motivated by the observation that visually similar objects are close in the representation space, we argue that the scenes and objects should instead follow a hierarchical structure based on their compositionality. To exploit such a structure, we propose a contrastive learning framework where a Euclidean loss is used to learn object representations and a hyperbolic loss is used to encourage representations of scenes to lie close to representations of their constituent objects in a hyperbolic space. This novel hyperbolic objective encourages the scene-object hypernymy among the representations by optimizing the magnitude of their norms. We show that when pretraining on the COCO and OpenImages datasets, the hyperbolic loss improves downstream performance of several baselines across multiple datasets and tasks, including image classification, object detection, and semantic segmentation. We also show that the properties of the learned representations allow us to solve various vision tasks that involve the interaction between scenes and objects in a zero-shot fashion. Our code can be found at \url{https://github.com/shlokk/HCL/tree/main/HCL}.

</details>

### Twin Contrastive Learning with Noisy Labels.
- **链接**: [arXiv:2303.06930](https://arxiv.org/abs/2303.06930) · [代码](https://github.com/Hzzone/TCL) · 📚 被引 108
- **作者**: Zhizhong Huang, Junping Zhang, Hongming Shan
- **🏷️ 机构**: School of Computer Science, Fudan University,Shanghai Key Lab of Intelligent Information Processing,Shanghai,China,200433, Institute of Science and Technology for Brain-inspired Intelligence and MOE Frontiers Center for Brain Science, Fudan University,Shanghai,China,200433
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning from noisy data is a challenging task that significantly degenerates the model performance. In this paper, we present TCL, a novel twin contrastive learning model to learn robust representations and handle noisy labels for classification. Specifically, we construct a Gaussian mixture model (GMM) over the representations by injecting the supervised model predictions into GMM to link label-free latent variables in GMM with label-noisy annotations. Then, TCL detects the examples with wrong labels as the out-of-distribution examples by another two-component GMM, taking into account the data distribution. We further propose a cross-supervision with an entropy regularization loss that bootstraps the true targets from model predictions to handle the noisy labels. As a result, TCL can learn discriminative representations aligned with estimated labels through mixup and contrastive learning. Extensive experimental results on several standard benchmarks and real-world datasets demonstrate the superior performance of TCL. In particular, TCL achieves 7.5\% improvements on CIFAR-10 with 90\% noisy label -- an extremely noisy scenario. The source code is available at \url{https://github.com/Hzzone/TCL}.

</details>

### Actionlet-Dependent Contrastive Learning for Unsupervised Skeleton-Based Action Recognition.
- **链接**: [arXiv:2303.10904](https://arxiv.org/abs/2303.10904) · 📚 被引 92
- **作者**: Lilang Lin, Jiahang Zhang, Jiaying Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The self-supervised pretraining paradigm has achieved great success in skeleton-based action recognition. However, these methods treat the motion and static parts equally, and lack an adaptive design for different parts, which has a negative impact on the accuracy of action recognition. To realize the adaptive action modeling of both parts, we propose an Actionlet-Dependent Contrastive Learning method (ActCLR). The actionlet, defined as the discriminative subset of the human skeleton, effectively decomposes motion regions for better action modeling. In detail, by contrasting with the static anchor without motion, we extract the motion region of the skeleton data, which serves as the actionlet, in an unsupervised manner. Then, centering on actionlet, a motion-adaptive data transformation method is built. Different data transformations are applied to actionlet and non-actionlet regions to introduce more diversity while maintaining their own characteristics. Meanwhile, we propose a semantic-aware feature pooling method to build feature representations among motion and static regions in a distinguished manner. Extensive experiments on NTU RGB+D and PKUMMD show that the proposed method achieves remarkable action recognition performance. More visualization and quantitative experiments demonstrate the effectiveness of our method. Our project website is available at https://langlandslin.github.io/projects/ActCLR/

</details>

### Pose-disentangled Contrastive Learning for Self-supervised Facial Representation.
- **链接**: [arXiv:2211.13490](https://arxiv.org/abs/2211.13490) · [代码](https://github.com/DreamMr/PCL) · 📚 被引 29
- **作者**: Yuanyuan Liu, Wenbin Wang, Yibing Zhan, Shaoze Feng, Kejun Liu, Zhe Chen
- **🏷️ 机构**: School of Computer Science, China University of Geosciences,Wuhan,China, JD Explore Academy,China, The University of Sydney,Australia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised facial representation has recently attracted increasing attention due to its ability to perform face understanding without relying on large-scale annotated datasets heavily. However, analytically, current contrastive-based self-supervised learning (SSL) still performs unsatisfactorily for learning facial representation. More specifically, existing contrastive learning (CL) tends to learn pose-invariant features that cannot depict the pose details of faces, compromising the learning performance. To conquer the above limitation of CL, we propose a novel Pose-disentangled Contrastive Learning (PCL) method for general self-supervised facial representation. Our PCL first devises a pose-disentangled decoder (PDD) with a delicately designed orthogonalizing regulation, which disentangles the pose-related features from the face-aware features; therefore, pose-related and other pose-unrelated facial information could be performed in individual subnetworks and do not affect each other's training. Furthermore, we introduce a pose-related contrastive learning scheme that learns pose-related information based on data augmentation of the same image, which would deliver more effective face-aware representation for various downstream tasks. We conducted linear evaluation on four challenging downstream facial understanding tasks, ie, facial expression recognition, face recognition, AU detection and head pose estimation. Experimental results demonstrate that our method significantly outperforms state-of-the-art SSL methods. Code is available at https://github.com/DreamMr/PCL}{https://github.com/DreamMr/PCL

</details>

### Spatio-Temporal Pixel-Level Contrastive Learning-based Source-Free Domain Adaptation for Video Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01015)
- **作者**: Shao-Yuan Lo, Poojan Oza, Sumanth Chennupati, Alejandro Galindo, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Change-Aware Sampling and Contrastive Learning for Satellite Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00509) · 📚 被引 96
- **作者**: Utkarsh Mall, Bharath Hariharan, Kavita Bala
- **🏷️ 机构**: Cornell University
- **会议**: CVPR 2023

### MobileVOS: Real-Time Video Object Segmentation Contrastive Learning meets Knowledge Distillation.
- **链接**: [arXiv:2303.07815](https://arxiv.org/abs/2303.07815) · 📚 被引 36
- **作者**: Roy Miles, Mehmet Kerim Yucel, Bruno Manganelli, Albert Saà-Garriga
- **🏷️ 机构**: Samsung Research,UK
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised training methods for transformers have demonstrated remarkable performance across various domains. Previous transformer-based models, such as masked autoencoders (MAE), typically utilize a single normalization layer for both the [CLS] symbol and the tokens. We propose in this paper a simple modification that employs separate normalization layers for the tokens and the [CLS] symbol to better capture their distinct characteristics and enhance downstream task performance. Our method aims to alleviate the potential negative effects of using the same normalization statistics for both token types, which may not be optimally aligned with their individual roles. We empirically show that by utilizing a separate normalization layer, the [CLS] embeddings can better encode the global contextual information and are distributed more uniformly in its anisotropic space. When replacing the conventional normalization layer with the two separate layers, we observe an average 2.7% performance improvement over the image, natural language, and graph domains.

</details>

### CADet: Fully Self-Supervised Out-Of-Distribution Detection With Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/1700ad4e6252e8f2955909f96367b34d-Abstract-Conference.html) · 📚 被引 3
- **作者**: Charles Guille-Escuret, Pau Rodríguez, David Vázquez, Ioannis Mitliagkas, João Monteiro
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### PUCA: Patch-Unshuffle and Channel Attention for Enhanced Self-Supervised Image Denoising.
- **链接**: [arXiv:2310.10088](https://arxiv.org/abs/2310.10088) · 📚 被引 10
- **作者**: Hyemi Jang, Junsung Park, Dahuin Jung, Jaihyun Lew, Ho Bae, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although supervised image denoising networks have shown remarkable performance on synthesized noisy images, they often fail in practice due to the difference between real and synthesized noise. Since clean-noisy image pairs from the real world are extremely costly to gather, self-supervised learning, which utilizes noisy input itself as a target, has been studied. To prevent a self-supervised denoising model from learning identical mapping, each output pixel should not be influenced by its corresponding input pixel; This requirement is known as J-invariance. Blind-spot networks (BSNs) have been a prevalent choice to ensure J-invariance in self-supervised image denoising. However, constructing variations of BSNs by injecting additional operations such as downsampling can expose blinded information, thereby violating J-invariance. Consequently, convolutions designed specifically for BSNs have been allowed only, limiting architectural flexibility. To overcome this limitation, we propose PUCA, a novel J-invariant U-Net architecture, for self-supervised denoising. PUCA leverages patch-unshuffle/shuffle to dramatically expand receptive fields while maintaining J-invariance and dilated attention blocks (DABs) for global context incorporation. Experimental results demonstrate that PUCA achieves state-of-the-art performance, outperforming existing methods in self-supervised image denoising.

</details>

### Modality-Agnostic Self-Supervised Learning with Meta-Learned Masked Auto-Encoder.
- **链接**: [arXiv:2310.16318](https://arxiv.org/abs/2310.16318) · [代码](https://github.com/alinlab/MetaMAE) · 📚 被引 1
- **作者**: Huiwon Jang, Jihoon Tack, Daewon Choi, Jongheon Jeong, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite its practical importance across a wide range of modalities, recent advances in self-supervised learning (SSL) have been primarily focused on a few well-curated domains, e.g., vision and language, often relying on their domain-specific knowledge. For example, Masked Auto-Encoder (MAE) has become one of the popular architectures in these domains, but less has explored its potential in other modalities. In this paper, we develop MAE as a unified, modality-agnostic SSL framework. In turn, we argue meta-learning as a key to interpreting MAE as a modality-agnostic learner, and propose enhancements to MAE from the motivation to jointly improve its SSL across diverse modalities, coined MetaMAE as a result. Our key idea is to view the mask reconstruction of MAE as a meta-learning task: masked tokens are predicted by adapting the Transformer meta-learner through the amortization of unmasked tokens. Based on this novel interpretation, we propose to integrate two advanced meta-learning techniques. First, we adapt the amortized latent of the Transformer encoder using gradient-based meta-learning to enhance the reconstruction. Then, we maximize the alignment between amortized and adapted latents through task contrastive learning which guides the Transformer encoder to better encode the task-specific knowledge. Our experiment demonstrates the superiority of MetaMAE in the modality-agnostic SSL benchmark (called DABS), significantly outperforming prior baselines. Code is available at https://github.com/alinlab/MetaMAE.

</details>

### Effective Targeted Attacks for Adversarial Self-Supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b28ae1166e1035c26b89d20f0286c9eb-Abstract-Conference.html) · 📚 被引 0
- **作者**: Minseon Kim, Hyeonjeong Ha, Sooel Son, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked image modeling (MIM) has become a popular strategy for self-supervised learning~(SSL) of visual representations with Vision Transformers. A representative MIM model, the masked auto-encoder (MAE), randomly masks a subset of image patches and reconstructs the masked patches given the unmasked patches. Concurrently, many recent works in self-supervised learning utilize the student/teacher paradigm which provides the student with an additional target based on the output of a teacher composed of an exponential moving average (EMA) of previous students. Although common, relatively little is known about the dynamics of the interaction between the student and teacher. Through analysis on a simple linear model, we find that the teacher conditionally removes previous gradient directions based on feature similarities which effectively acts as a conditional momentum regularizer. From this analysis, we present a simple SSL method, the Reconstruction-Consistent Masked Auto-Encoder (RC-MAE) by adding an EMA teacher to MAE. We find that RC-MAE converges faster and requires less memory usage than state-of-the-art self-distillation methods during pre-training, which may provide a way to enhance the practicality of prohibitively expensive self-supervised learning of Vision Transformer models. Additionally, we show that RC-MAE achieves more robustness and better performance compared to MAE on downstream tasks such as ImageNet-1K classification, object detection, and instance segmentation.

</details>

### MocoSFL: enabling cross-client collaborative self-supervised learning.
- **链接**: [出版页](https://openreview.net/forum?id=2QGJXyMNoPz)
- **作者**: Jingtao Li, Lingjuan Lyu, Daisuke Iso, Chaitali Chakrabarti, Michael Spranger
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has great potential for molecular representation learning given the complexity of molecular graphs, the large amounts of unlabelled data available, the considerable cost of obtaining labels experimentally, and the hence often only small training datasets. The importance of the topic is reflected in the variety of paradigms and architectures that have been investigated recently. Yet the differences in performance seem often minor and are barely understood to date. In this paper, we study SSL based on persistent homology (PH), a mathematical tool for modeling topological features of data that persist across multiple scales. It has several unique features which particularly suit SSL, naturally offering: different views of the data, stability in terms of distance preservation, and the opportunity to flexibly incorporate domain knowledge. We (1) investigate an autoencoder, which shows the general representational power of PH, and (2) propose a contrastive loss that complements existing approaches. We rigorously evaluate our approach for molecular property prediction and demonstrate its particular features in improving the embedding space: after SSL, the representations are better and offer considerably more predictive power than the baselines over different probing tasks; our loss increases baseline performance, sometimes largely; and we often obtain substantial improvements over very small datasets, a common scenario in practice.

</details>

### TopoSRL: Topology preserving self-supervised Simplicial Representation Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/caba69fbc9fa0b06241b98a44cab8b31-Abstract-Conference.html) · 📚 被引 0
- **作者**: Hiren Madhu, Sundeep Prabhakar Chepuri
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Do SSL Models Have Déjà Vu? A Case of Unintended Memorization in Self-supervised Learning.
- **链接**: [arXiv:2304.13850](https://arxiv.org/abs/2304.13850) · [代码](https://github.com/facebookresearch/DejaVu) · 📚 被引 0
- **作者**: Casey Meehan, Florian Bordes, Pascal Vincent, Kamalika Chaudhuri, Chuan Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) algorithms can produce useful image representations by learning to associate different parts of natural images with one another. However, when taken to the extreme, SSL models can unintendedly memorize specific parts in individual training samples rather than learning semantically meaningful associations. In this work, we perform a systematic study of the unintended memorization of image-specific information in SSL models -- which we refer to as déjà vu memorization. Concretely, we show that given the trained model and a crop of a training image containing only the background (e.g., water, sky, grass), it is possible to infer the foreground object with high accuracy or even visually reconstruct it. Furthermore, we show that déjà vu memorization is common to different SSL algorithms, is exacerbated by certain design choices, and cannot be detected by conventional techniques for evaluating representation quality. Our study of déjà vu memorization reveals previously unknown privacy risks in SSL models, as well as suggests potential practical mitigation strategies. Code is available at https://github.com/facebookresearch/DejaVu.

</details>

### Self-Supervised Learning with Lie Symmetries for Partial Differential Equations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5c46ae130105fa012da0446126c01d1d-Abstract-Conference.html) · 📚 被引 2
- **作者**: Grégoire Mialon, Quentin Garrido, Hannah Lawrence, Danyal Rehman, Yann LeCun, Bobak T. Kiani
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CLAMP: Prompt-based Contrastive Learning for Connecting Language and Animal Pose.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02229) · 📚 被引 29
- **作者**: Xu Zhang, Wen Wang, Zhe Chen, Yufei Xu, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: The University of Sydney,Australia, Zhejiang University,China
- **会议**: CVPR 2023

### Non-Contrastive Learning Meets Language-Image Pre-Training.
- **链接**: [arXiv:2210.09304](https://arxiv.org/abs/2210.09304) · 📚 被引 19
- **作者**: Jinghao Zhou, Li Dong, Zhe Gan, Lijuan Wang, Furu Wei
- **🏷️ 机构**: Microsoft
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Obtaining large pre-trained models that can be fine-tuned to new tasks with limited annotated samples has remained an open challenge for medical imaging data. While pre-trained deep networks on ImageNet and vision-language foundation models trained on web-scale data are prevailing approaches, their effectiveness on medical tasks is limited due to the significant domain shift between natural and medical images. To bridge this gap, we introduce LVM-Med, the first family of deep networks trained on large-scale medical datasets. We have collected approximately 1.3 million medical images from 55 publicly available datasets, covering a large number of organs and modalities such as CT, MRI, X-ray, and Ultrasound. We benchmark several state-of-the-art self-supervised algorithms on this dataset and propose a novel self-supervised contrastive learning algorithm using a graph-matching formulation. The proposed approach makes three contributions: (i) it integrates prior pair-wise image similarity metrics based on local and global information; (ii) it captures the structural constraints of feature embeddings through a loss function constructed via a combinatorial graph-matching objective; and (iii) it can be trained efficiently end-to-end using modern gradient-estimation techniques for black-box solvers. We thoroughly evaluate the proposed LVM-Med on 15 downstream medical tasks ranging from segmentation and classification to object detection, and both for the in and out-of-distribution settings. LVM-Med empirically outperforms a number of state-of-the-art supervised, self-supervised, and foundation models. For challenging tasks such as Brain Tumor Classification or Diabetic Retinopathy Grading, LVM-Med improves previous vision-language models trained on 1 billion masks by 6-7% while using only a ResNet-50.

</details>

### Masked Image Training for Generalizable Deep Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00169) · 📚 被引 106
- **作者**: Haoyu Chen, Jinjin Gu, Yihao Liu, Salma Abdel Magid, Chao Dong, Qiong Wang et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology (Guangzhou), Shanghai AI Lab, Harvard University
- **会议**: CVPR 2023

### MaskSketch: Unpaired Structure-guided Masked Image Generation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00187) · 📚 被引 35
- **作者**: Dina Bashkirova, José Lezama, Kihyuk Sohn, Kate Saenko, Irfan Essa
- **🏷️ 机构**: Boston University, Google Research
- **会议**: CVPR 2023

### MIC: Masked Image Consistency for Context-Enhanced Domain Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01128) · 📚 被引 329
- **作者**: Lukas Hoyer, Dengxin Dai, Haoran Wang, Luc Van Gool
- **🏷️ 机构**: ETH Zurich, Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2023

### Understanding Masked Image Modeling via Learning Occlusion Invariant Feature.
- **链接**: [arXiv:2208.04164](https://arxiv.org/abs/2208.04164) · 📚 被引 40
- **作者**: Xiangwen Kong, Xiangyu Zhang
- **🏷️ 机构**: MEGVII Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, Masked Image Modeling (MIM) achieves great success in self-supervised visual recognition. However, as a reconstruction-based framework, it is still an open question to understand how MIM works, since MIM appears very different from previous well-studied siamese approaches such as contrastive learning. In this paper, we propose a new viewpoint: MIM implicitly learns occlusion-invariant features, which is analogous to other siamese methods while the latter learns other invariance. By relaxing MIM formulation into an equivalent siamese form, MIM methods can be interpreted in a unified framework with conventional methods, among which only a) data transformations, i.e. what invariance to learn, and b) similarity measurements are different. Furthermore, taking MAE (He et al.) as a representative example of MIM, we empirically find the success of MIM models relates a little to the choice of similarity functions, but the learned occlusion invariant feature introduced by masked image -- it turns out to be a favored initialization for vision transformers, even though the learned feature could be less semantic. We hope our findings could inspire researchers to develop more powerful self-supervised methods in computer vision community.

</details>

### Rethinking Out-of-distribution (OOD) Detection: Masked Image Modeling is All You Need.
- **链接**: [arXiv:2302.02615](https://arxiv.org/abs/2302.02615) · 📚 被引 58
- **作者**: Jingyao Li, Pengguang Chen, Zexin He, Shaozuo Yu, Shu Liu, Jiaya Jia
- **🏷️ 机构**: The Chinese University of Hong Kong, SmartMore
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The core of out-of-distribution (OOD) detection is to learn the in-distribution (ID) representation, which is distinguishable from OOD samples. Previous work applied recognition-based methods to learn the ID features, which tend to learn shortcuts instead of comprehensive representations. In this work, we find surprisingly that simply using reconstruction-based methods could boost the performance of OOD detection significantly. We deeply explore the main contributors of OOD detection and find that reconstruction-based pretext tasks have the potential to provide a generally applicable and efficacious prior, which benefits the model in learning intrinsic data distributions of the ID dataset. Specifically, we take Masked Image Modeling as a pretext task for our OOD detection framework (MOOD). Without bells and whistles, MOOD outperforms previous SOTA of one-class OOD detection by 5.7%, multi-class OOD detection by 3.0%, and near-distribution OOD detection by 2.1%. It even defeats the 10-shot-per-class outlier exposure OOD detection, although we do not include any OOD samples for our detection

</details>

### Hard Patches Mining for Masked Image Modeling.
- **链接**: [arXiv:2304.05919](https://arxiv.org/abs/2304.05919) · 📚 被引 71
- **作者**: Haochen Wang, Kaiyou Song, Junsong Fan, Yuxi Wang, Jin Xie, Zhaoxiang Zhang
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,Center for Research on Intelligent Perception and Computing, National Laboratory of Pattern Recognition, Megvii Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked image modeling (MIM) has attracted much research attention due to its promising potential for learning scalable visual representations. In typical approaches, models usually focus on predicting specific contents of masked patches, and their performances are highly related to pre-defined mask strategies. Intuitively, this procedure can be considered as training a student (the model) on solving given problems (predict masked patches). However, we argue that the model should not only focus on solving given problems, but also stand in the shoes of a teacher to produce a more challenging problem by itself. To this end, we propose Hard Patches Mining (HPM), a brand-new framework for MIM pre-training. We observe that the reconstruction loss can naturally be the metric of the difficulty of the pre-training task. Therefore, we introduce an auxiliary loss predictor, predicting patch-wise losses first and deciding where to mask next. It adopts a relative relationship learning strategy to prevent overfitting to exact reconstruction loss values. Experiments under various settings demonstrate the effectiveness of HPM in constructing masked images. Furthermore, we empirically find that solely introducing the loss prediction objective leads to powerful representations, verifying the efficacy of the ability to be aware of where is hard to reconstruct.

</details>

### Masked Image Modeling with Local Multi-Scale Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00211) · 📚 被引 58
- **作者**: Haoqing Wang, Yehui Tang, Yunhe Wang, Jianyuan Guo, Zhi-Hong Deng, Kai Han
- **🏷️ 机构**: School of Intelligence Science and Technology, Peking University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023

### Revealing the Dark Secrets of Masked Image Modeling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01391) · 📚 被引 95
- **作者**: Zhenda Xie, Zigang Geng, Jingcheng Hu, Zheng Zhang, Han Hu, Yue Cao
- **🏷️ 机构**: Tsinghua University, University of Science and Technology of China, Microsoft Research Asia
- **会议**: CVPR 2023

### On Data Scaling in Masked Image Modeling.
- **链接**: [arXiv:2206.04664](https://arxiv.org/abs/2206.04664) · 📚 被引 52
- **作者**: Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Yixuan Wei, Qi Dai et al.
- **🏷️ 机构**: Tsinghua University, Xi&#x0027;an Jiaotong University, Microsoft Research Asia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An important goal of self-supervised learning is to enable model pre-training to benefit from almost unlimited data. However, one method that has recently become popular, namely masked image modeling (MIM), is suspected to be unable to benefit from larger data. In this work, we break this misconception through extensive experiments, with data scales ranging from 10\% of ImageNet-1K to full ImageNet-22K, model sizes ranging from 49 million to 1 billion, and training lengths ranging from 125K iterations to 500K iterations. Our study reveals that: (i) Masked image modeling is also demanding on larger data. We observed that very large models got over-fitted with relatively small data; (ii) The length of training matters. Large models trained with masked image modeling can benefit from more data with longer training; (iii) The validation loss in pre-training is a good indicator to measure how well the model performs for fine-tuning on multiple tasks. This observation allows us to pre-evaluate pre-trained models in advance without having to make costly trial-and-error assessments of downstream tasks. We hope that our findings will advance the understanding of masked image modeling in terms of scaling ability.

</details>

### Stare at What You See: Masked Image Modeling without Reconstruction.
- **链接**: [arXiv:2211.08887](https://arxiv.org/abs/2211.08887) · [代码](https://github.com/OpenPerceptionX/maskalign) · 📚 被引 22
- **作者**: Hongwei Xue, Peng Gao, Hongyang Li, Yu Qiao, Hao Sun, Houqiang Li et al.
- **🏷️ 机构**: University of Science and Technology of China, Shanghai Artificial Intelligence Laboratory, China Telecom Corporation Ltd., Data&#x0026;AI Technology Company
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Autoencoders (MAE) have been prevailing paradigms for large-scale vision representation pre-training. By reconstructing masked image patches from a small portion of visible image regions, MAE forces the model to infer semantic correlation within an image. Recently, some approaches apply semantic-rich teacher models to extract image features as the reconstruction target, leading to better performance. However, unlike the low-level features such as pixel values, we argue the features extracted by powerful teacher models already encode rich semantic correlation across regions in an intact image.This raises one question: is reconstruction necessary in Masked Image Modeling (MIM) with a teacher model? In this paper, we propose an efficient MIM paradigm named MaskAlign. MaskAlign simply learns the consistency of visible patch features extracted by the student model and intact image features extracted by the teacher model. To further advance the performance and tackle the problem of input inconsistency between the student and teacher model, we propose a Dynamic Alignment (DA) module to apply learnable alignment. Our experimental results demonstrate that masked modeling does not lose effectiveness even without reconstruction on masked regions. Combined with Dynamic Alignment, MaskAlign can achieve state-of-the-art performance with much higher efficiency. Code and models will be available at https://github.com/OpenPerceptionX/maskalign.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked Autoencoders (MAE) have been prevailing paradigms for large-scale vision representation pre-training. By reconstructing masked image patches from a small portion of visible image regions, MAE forces the model to infer semantic correlation within an image. Recently, some approaches apply semantic-rich teacher models to extract image features as the reconstruction target, leading to better performance. However, unlike the low-level features such as pixel values, we argue the features extracted by powerful teacher models already encode rich semantic correlation across regions in an intact image.This raises one question: is reconstruction necessary in Masked Image Modeling (MIM) with a teacher model? In this paper, we propose an efficient MIM paradigm named MaskAlign. MaskAlign simply learns the consistency of visible patch features extracted by the student model and intact image features extracted by the teacher model. To further advance the performance and tackle the problem of input inconsistency between the student and teacher model, we propose a Dynamic Alignment (DA) module to apply learnable alignment. Our experimental results demonstrate that masked modeling does not lose effectiveness even without reconstruction on masked regions. Combined with Dynamic Alignment, MaskAlign can achieve state-of-the-art performance with much higher efficiency. Code and models will be available at https://github.com/OpenPerceptionX/maskalign.

</details>

### PMatch: Paired Masked Image Modeling for Dense Geometric Matching.
- **链接**: [arXiv:2303.17342](https://arxiv.org/abs/2303.17342) · [代码](https://github.com/ShngJZ/PMatch) · 📚 被引 43
- **作者**: Shengjie Zhu, Xiaoming Liu
- **🏷️ 机构**: Michigan State University,Department of Computer Science and Engineering,East Lansing,MI,48824
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a simple, self-supervised method for magnifying subtle motions in video: given an input video and a magnification factor, we manipulate the video such that its new optical flow is scaled by the desired amount. To train our model, we propose a loss function that estimates the optical flow of the generated video and penalizes how far if deviates from the given magnification factor. Thus, training involves differentiating through a pretrained optical flow network. Since our model is self-supervised, we can further improve its performance through test-time adaptation, by finetuning it on the input video. It can also be easily extended to magnify the motions of only user-selected objects. Our approach avoids the need for synthetic magnification datasets that have been used to train prior learning-based approaches. Instead, it leverages the existing capabilities of off-the-shelf motion estimators. We demonstrate the effectiveness of our method through evaluations of both visual quality and quantitative metrics on a range of real-world and synthetic videos, and we show our method works for both supervised and unsupervised optical flow methods.

</details>

### Self-supervised video pretraining yields robust and more human-aligned visual representations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/cf57022dff0929796f85ac99d7cefa86-Abstract-Conference.html) · 📚 被引 1
- **作者**: Nikhil Parthasarathy, S. M. Ali Eslami, João Carreira, Olivier J. Hénaff
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Encoding Time-Series Explanations through Self-Supervised Model Behavior Consistency.
- **链接**: [arXiv:2306.02109](https://arxiv.org/abs/2306.02109) · 📚 被引 7
- **作者**: Owen Queen, Tom Hartvigsen, Teddy Koker, Huan He, Theodoros Tsiligkaridis, Marinka Zitnik
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Interpreting time series models is uniquely challenging because it requires identifying both the location of time series signals that drive model predictions and their matching to an interpretable temporal pattern. While explainers from other modalities can be applied to time series, their inductive biases do not transfer well to the inherently challenging interpretation of time series. We present TimeX, a time series consistency model for training explainers. TimeX trains an interpretable surrogate to mimic the behavior of a pretrained time series model. It addresses the issue of model faithfulness by introducing model behavior consistency, a novel formulation that preserves relations in the latent space induced by the pretrained model with relations in the latent space induced by TimeX. TimeX provides discrete attribution maps and, unlike existing interpretability methods, it learns a latent space of explanations that can be used in various ways, such as to provide landmarks to visually aggregate similar explanations and easily recognize temporal patterns. We evaluate TimeX on eight synthetic and real-world datasets and compare its performance against state-of-the-art interpretability methods. We also conduct case studies using physiological time series. Quantitative evaluations demonstrate that TimeX achieves the highest or second-highest performance in every metric compared to baselines across all datasets. Through case studies, we show that the novel components of TimeX show potential for training faithful, interpretable models that capture the behavior of pretrained time series models.

</details>

### Language-based Action Concept Spaces Improve Video Self-Supervised Learning.
- **链接**: [arXiv:2307.10922](https://arxiv.org/abs/2307.10922) · 📚 被引 2
- **作者**: Kanchana Ranasinghe, Michael S. Ryoo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent contrastive language image pre-training has led to learning highly transferable and robust image representations. However, adapting these models to video domains with minimal supervision remains an open problem. We explore a simple step in that direction, using language tied self-supervised learning to adapt an image CLIP model to the video domain. A backbone modified for temporal modeling is trained under self-distillation settings with train objectives operating in an action concept space. Feature vectors of various action concepts extracted from a language encoder using relevant textual prompts construct this space. We introduce two train objectives, concept distillation and concept alignment, that retain generality of original representations while enforcing relations between actions and their attributes. Our approach improves zero-shot and linear probing performance on three action recognition benchmarks.

</details>

### Uncovering the Hidden Dynamics of Video Self-supervised Learning under Distribution Shifts.
- **链接**: [arXiv:2306.02014](https://arxiv.org/abs/2306.02014) · 📚 被引 1
- **作者**: Pritam Sarkar, Ahmad Beirami, Ali Etemad
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video self-supervised learning (VSSL) has made significant progress in recent years. However, the exact behavior and dynamics of these models under different forms of distribution shift are not yet known. In this paper, we comprehensively study the behavior of six popular self-supervised methods (v-SimCLR, v-MoCo, v-BYOL, v-SimSiam, v-DINO, v-MAE) in response to various forms of natural distribution shift, i.e., (i) context shift, (ii) viewpoint shift, (iii) actor shift, (iv) source shift, (v) generalizability to unknown classes (zero-shot), and (vi) open-set recognition. To perform this extensive study, we carefully craft a test bed consisting of 17 in-distribution and out-of-distribution benchmark pairs using available public datasets and a series of evaluation protocols to stress-test the different methods under the intended shifts. Our study uncovers a series of intriguing findings and interesting behaviors of VSSL methods. For instance, we observe that while video models generally struggle with context shifts, v-MAE and supervised learning exhibit more robustness. Moreover, our study shows that v-MAE is a strong temporal learner, whereas contrastive methods, v-SimCLR and v-MoCo, exhibit strong performances against viewpoint shifts. When studying the notion of open-set recognition, we notice a trade-off between closed-set and open-set recognition performance if the pretrained VSSL encoders are used without finetuning. We hope that our work will contribute to the development of robust video representation learning frameworks for various real-world scenarios. The project page and code are available at: https://pritamqu.github.io/OOD-VSSL.

</details>

### SNAP: Self-Supervised Neural Maps for Visual Positioning and Semantic Understanding.
- **链接**: [arXiv:2306.05407](https://arxiv.org/abs/2306.05407) · 📚 被引 1
- **作者**: Paul-Edouard Sarlin, Eduard Trulls, Marc Pollefeys, Jan Hosang, Simon Lynen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semantic 2D maps are commonly used by humans and machines for navigation purposes, whether it's walking or driving. However, these maps have limitations: they lack detail, often contain inaccuracies, and are difficult to create and maintain, especially in an automated fashion. Can we use raw imagery to automatically create better maps that can be easily interpreted by both humans and machines? We introduce SNAP, a deep network that learns rich neural 2D maps from ground-level and overhead images. We train our model to align neural maps estimated from different inputs, supervised only with camera poses over tens of millions of StreetView images. SNAP can resolve the location of challenging image queries beyond the reach of traditional methods, outperforming the state of the art in localization by a large margin. Moreover, our neural maps encode not only geometry and appearance but also high-level semantics, discovered without explicit supervision. This enables effective pre-training for data-efficient semantic scene understanding, with the potential to unlock cost-efficient creation of more detailed maps.

</details>

### Self-Supervised Learning of Representations for Space Generates Multi-Modular Grid Cells.
- **链接**: [arXiv:2311.02316](https://arxiv.org/abs/2311.02316) · 📚 被引 3
- **作者**: Rylan Schaeffer, Mikail Khona, Tzuhsuan Ma, Cristóbal Eyzaguirre, Sanmi Koyejo, Ila Fiete
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To solve the spatial problems of mapping, localization and navigation, the mammalian lineage has developed striking spatial representations. One important spatial representation is the Nobel-prize winning grid cells: neurons that represent self-location, a local and aperiodic quantity, with seemingly bizarre non-local and spatially periodic activity patterns of a few discrete periods. Why has the mammalian lineage learnt this peculiar grid representation? Mathematical analysis suggests that this multi-periodic representation has excellent properties as an algebraic code with high capacity and intrinsic error-correction, but to date, there is no satisfactory synthesis of core principles that lead to multi-modular grid cells in deep recurrent neural networks. In this work, we begin by identifying key insights from four families of approaches to answering the grid cell question: coding theory, dynamical systems, function optimization and supervised deep learning. We then leverage our insights to propose a new approach that combines the strengths of all four approaches. Our approach is a self-supervised learning (SSL) framework - including data, data augmentations, loss functions and a network architecture - motivated from a normative perspective, without access to supervised position information or engineering of particular readout representations as needed in previous approaches. We show that multiple grid cell modules can emerge in networks trained on our SSL framework and that the networks and emergent representations generalize well outside their training distribution. This work contains insights for neuroscientists interested in the origins of grid cells as well as machine learning researchers interested in novel SSL frameworks.

</details>

### Self-Supervised Visual Acoustic Matching.
- **链接**: [arXiv:2307.15064](https://arxiv.org/abs/2307.15064) · 📚 被引 1
- **作者**: Arjun Somayazulu, Changan Chen, Kristen Grauman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Acoustic matching aims to re-synthesize an audio clip to sound as if it were recorded in a target acoustic environment. Existing methods assume access to paired training data, where the audio is observed in both source and target environments, but this limits the diversity of training data or requires the use of simulated data or heuristics to create paired samples. We propose a self-supervised approach to visual acoustic matching where training samples include only the target scene image and audio -- without acoustically mismatched source audio for reference. Our approach jointly learns to disentangle room acoustics and re-synthesize audio into the target environment, via a conditional GAN framework and a novel metric that quantifies the level of residual acoustic information in the de-biased audio. Training with either in-the-wild web data or simulated data, we demonstrate it outperforms the state-of-the-art on multiple challenging datasets and a wide variety of real-world audio and environments.

</details>

### FLSL: Feature-level Self-supervised Learning.
- **链接**: [arXiv:2306.06203](https://arxiv.org/abs/2306.06203) · [代码](https://github.com/ISL-CV/FLSL) · 📚 被引 0
- **作者**: Qing Su, Anton Netchaev, Hai Li, Shihao Ji
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current self-supervised learning (SSL) methods (e.g., SimCLR, DINO, VICReg,MOCOv3) target primarily on representations at instance level and do not generalize well to dense prediction tasks, such as object detection and segmentation.Towards aligning SSL with dense predictions, this paper demonstrates for the first time the underlying mean-shift clustering process of Vision Transformers (ViT), which aligns well with natural image semantics (e.g., a world of objects and stuffs). By employing transformer for joint embedding and clustering, we propose a two-level feature clustering SSL method, coined Feature-Level Self-supervised Learning (FLSL). We present the formal definition of the FLSL problem and construct the objectives from the mean-shift and k-means perspectives. We show that FLSL promotes remarkable semantic cluster representations and learns an embedding scheme amenable to intra-view and inter-view feature clustering. Experiments show that FLSL yields significant improvements in dense prediction tasks, achieving 44.9 (+2.8)% AP and 46.5% AP in object detection, as well as 40.8 (+2.3)% AP and 42.1% AP in instance segmentation on MS-COCO, using Mask R-CNN with ViT-S/16 and ViT-S/8 as backbone, respectively. FLSL consistently outperforms existing SSL methods across additional benchmarks, including UAV17 object detection on UAVDT, and video instance segmentation on DAVIS 2017.We conclude by presenting visualization and various ablation studies to better understand the success of FLSL. The source code is available at https://github.com/ISL-CV/FLSL.

</details>

### Evaluating Self-Supervised Learning for Molecular Graph Embeddings.
- **链接**: [arXiv:2206.08005](https://arxiv.org/abs/2206.08005) · 📚 被引 1
- **作者**: Hanchen Wang, Jean Kaddour, Shengchao Liu, Jian Tang, Joan Lasenby, Qi Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Self-Supervised Learning (GSSL) provides a robust pathway for acquiring embeddings without expert labelling, a capability that carries profound implications for molecular graphs due to the staggering number of potential molecules and the high cost of obtaining labels. However, GSSL methods are designed not for optimisation within a specific domain but rather for transferability across a variety of downstream tasks. This broad applicability complicates their evaluation. Addressing this challenge, we present "Molecular Graph Representation Evaluation" (MOLGRAPHEVAL), generating detailed profiles of molecular graph embeddings with interpretable and diversified attributes. MOLGRAPHEVAL offers a suite of probing tasks grouped into three categories: (i) generic graph, (ii) molecular substructure, and (iii) embedding space properties. By leveraging MOLGRAPHEVAL to benchmark existing GSSL methods against both current downstream datasets and our suite of tasks, we uncover significant inconsistencies between inferences drawn solely from existing datasets and those derived from more nuanced probing. These findings suggest that current evaluation methodologies fail to capture the entirety of the landscape.

</details>

### Keypoint-Augmented Self-Supervised Learning for Medical Image Segmentation with Limited Annotation.
- **链接**: [arXiv:2310.01680](https://arxiv.org/abs/2310.01680) · [代码](https://github.com/zshyang/kaf.git) · 📚 被引 4
- **作者**: Zhangsihao Yang, Mengwei Ren, Kaize Ding, Guido Gerig, Yalin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretraining CNN models (i.e., UNet) through self-supervision has become a powerful approach to facilitate medical image segmentation under low annotation regimes. Recent contrastive learning methods encourage similar global representations when the same image undergoes different transformations, or enforce invariance across different image/patch features that are intrinsically correlated. However, CNN-extracted global and local features are limited in capturing long-range spatial dependencies that are essential in biological anatomy. To this end, we present a keypoint-augmented fusion layer that extracts representations preserving both short- and long-range self-attention. In particular, we augment the CNN feature map at multiple scales by incorporating an additional input that learns long-range spatial self-attention among localized keypoint features. Further, we introduce both global and local self-supervised pretraining for the framework. At the global scale, we obtain global representations from both the bottleneck of the UNet, and by aggregating multiscale keypoint features. These global features are subsequently regularized through image-level contrastive objectives. At the local scale, we define a distance-based criterion to first establish correspondences among keypoints and encourage similarity between their features. Through extensive experiments on both MRI and CT segmentation tasks, we demonstrate the architectural advantages of our proposed method in comparison to both CNN and Transformer-based UNets, when all architectures are trained with randomly initialized weights. With our proposed pretraining strategy, our method further outperforms existing SSL methods by producing more robust self-attention and achieving state-of-the-art segmentation results. The code is available at https://github.com/zshyang/kaf.git.

</details>

### Self-supervised Graph Neural Networks via Low-Rank Decomposition.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6c33e4ea4ddfb05a78541022ab5a1fb9-Abstract-Conference.html) · 📚 被引 1
- **作者**: Liang Yang, Runjie Shi, Qiuliang Zhang, Bingxin Niu, Zhen Wang, Xiaochun Cao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### AdaptSSR: Pre-training User Model with Augmentation-Adaptive Self-Supervised Ranking.
- **链接**: [arXiv:2310.09706](https://arxiv.org/abs/2310.09706) · 📚 被引 1
- **作者**: Yang Yu, Qi Liu, Kai Zhang, Yuren Zhang, Chao Song, Min Hou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> User modeling, which aims to capture users' characteristics or interests, heavily relies on task-specific labeled data and suffers from the data sparsity issue. Several recent studies tackled this problem by pre-training the user model on massive user behavior sequences with a contrastive learning task. Generally, these methods assume different views of the same behavior sequence constructed via data augmentation are semantically consistent, i.e., reflecting similar characteristics or interests of the user, and thus maximizing their agreement in the feature space. However, due to the diverse interests and heavy noise in user behaviors, existing augmentation methods tend to lose certain characteristics of the user or introduce noisy behaviors. Thus, forcing the user model to directly maximize the similarity between the augmented views may result in a negative transfer. To this end, we propose to replace the contrastive learning task with a new pretext task: Augmentation-Adaptive SelfSupervised Ranking (AdaptSSR), which alleviates the requirement of semantic consistency between the augmented views while pre-training a discriminative user model. Specifically, we adopt a multiple pairwise ranking loss which trains the user model to capture the similarity orders between the implicitly augmented view, the explicitly augmented view, and views from other users. We further employ an in-batch hard negative sampling strategy to facilitate model training. Moreover, considering the distinct impacts of data augmentation on different behavior sequences, we design an augmentation-adaptive fusion mechanism to automatically adjust the similarity order constraint applied to each sample based on the estimated similarity between the augmented views. Extensive experiments on both public and industrial datasets with six downstream tasks verify the effectiveness of AdaptSSR.

</details>

### Better Correlation and Robustness: A Distribution-Balanced Self-Supervised Learning Framework for Automatic Dialogue Evaluation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a8b148559549ce33261e79b4400e0d77-Abstract-Conference.html) · 📚 被引 0
- **作者**: Peiwen Yuan, Xinglin Wang, Jiayi Shi, Bin Sun, Yiwei Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Discovering Hierarchical Achievements in Reinforcement Learning via Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/c919a2b5ec1de69f2629f9119676e336-Abstract-Conference.html) · 📚 被引 1
- **作者**: Seungyong Moon, Junyoung Yeom, Bumsoo Park, Hyun Oh Song
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Graph Contrastive Learning with Stable and Scalable Spectral Encoding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/8e9a6582caa59fda0302349702965171-Abstract-Conference.html) · 📚 被引 3
- **作者**: Deyu Bo, Yuan Fang, Yang Liu, Chuan Shi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Semi-Supervised Contrastive Learning for Deep Regression with Ordinal Rankings from Spectral Seriation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b2d4051f03a7038a2771dfbbe5c7b54e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weihang Dai, Yao Du, Hanru Bai, Kwang-Ting Cheng, Xiaomeng Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Finding Order in Chaos: A Novel Data Augmentation Method for Time Series in Contrastive Learning.
- **链接**: [arXiv:2309.13439](https://arxiv.org/abs/2309.13439) · [代码](https://github.com/eth-siplab/Finding_Order_in_Chaos) · 📚 被引 12
- **作者**: Berken Utku Demirel, Christian Holz
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of contrastive learning is well known to be dependent on data augmentation. Although the degree of data augmentations has been well controlled by utilizing pre-defined techniques in some domains like vision, time-series data augmentation is less explored and remains a challenging problem due to the complexity of the data generation mechanism, such as the intricate mechanism involved in the cardiovascular system. Moreover, there is no widely recognized and general time-series augmentation method that can be applied across different tasks. In this paper, we propose a novel data augmentation method for quasi-periodic time-series tasks that aims to connect intra-class samples together, and thereby find order in the latent space. Our method builds upon the well-known mixup technique by incorporating a novel approach that accounts for the periodic nature of non-stationary time-series. Also, by controlling the degree of chaos created by data augmentation, our method leads to improved feature representations and performance on downstream tasks. We evaluate our proposed method on three time-series tasks, including heart rate estimation, human activity recognition, and cardiovascular disease detection. Extensive experiments against state-of-the-art methods show that the proposed approach outperforms prior works on optimal data generation and known data augmentation techniques in the three tasks, reflecting the effectiveness of the presented method. Source code: https://github.com/eth-siplab/Finding_Order_in_Chaos

</details>

### Complementary Benefits of Contrastive Learning and Self-Training Under Distribution Shift.
- **链接**: [arXiv:2312.03318](https://arxiv.org/abs/2312.03318) · 📚 被引 0
- **作者**: Saurabh Garg, Amrith Setlur, Zachary C. Lipton, Sivaraman Balakrishnan, Virginia Smith, Aditi Raghunathan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-training and contrastive learning have emerged as leading techniques for incorporating unlabeled data, both under distribution shift (unsupervised domain adaptation) and when it is absent (semi-supervised learning). However, despite the popularity and compatibility of these techniques, their efficacy in combination remains unexplored. In this paper, we undertake a systematic empirical investigation of this combination, finding that (i) in domain adaptation settings, self-training and contrastive learning offer significant complementary gains; and (ii) in semi-supervised learning settings, surprisingly, the benefits are not synergistic. Across eight distribution shift datasets (e.g., BREEDs, WILDS), we demonstrate that the combined method obtains 3--8% higher accuracy than either approach independently. We then theoretically analyze these techniques in a simplified model of distribution shift, demonstrating scenarios under which the features produced by contrastive learning can yield a good initialization for self-training to further amplify gains and achieve optimal performance, even when either method alone would fail.

</details>

### Architecture Matters: Uncovering Implicit Mechanisms in Graph Contrastive Learning.
- **链接**: [arXiv:2311.02687](https://arxiv.org/abs/2311.02687) · [代码](https://github.com/PKU-ML/ArchitectureMattersGCL) · 📚 被引 0
- **作者**: Xiaojun Guo, Yifei Wang, Zeming Wei, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the prosperity of contrastive learning for visual representation learning (VCL), it is also adapted to the graph domain and yields promising performance. However, through a systematic study of various graph contrastive learning (GCL) methods, we observe that some common phenomena among existing GCL methods that are quite different from the original VCL methods, including 1) positive samples are not a must for GCL; 2) negative samples are not necessary for graph classification, neither for node classification when adopting specific normalization modules; 3) data augmentations have much less influence on GCL, as simple domain-agnostic augmentations (e.g., Gaussian noise) can also attain fairly good performance. By uncovering how the implicit inductive bias of GNNs works in contrastive learning, we theoretically provide insights into the above intriguing properties of GCL. Rather than directly porting existing VCL methods to GCL, we advocate for more attention toward the unique architecture of graph learning and consider its implicit influence when designing GCL methods. Code is available at https: //github.com/PKU-ML/ArchitectureMattersGCL.

</details>

### Three Towers: Flexible Contrastive Learning with Pretrained Image Models.
- **链接**: [arXiv:2305.16999](https://arxiv.org/abs/2305.16999) · 📚 被引 1
- **作者**: Jannik Kossen, Mark Collier, Basil Mustafa, Xiao Wang, Xiaohua Zhai, Lucas Beyer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Three Towers (3T), a flexible method to improve the contrastive learning of vision-language models by incorporating pretrained image classifiers. While contrastive models are usually trained from scratch, LiT (Zhai et al., 2022) has recently shown performance gains from using pretrained classifier embeddings. However, LiT directly replaces the image tower with the frozen embeddings, excluding any potential benefits from training the image tower contrastively. With 3T, we propose a more flexible strategy that allows the image tower to benefit from both pretrained embeddings and contrastive training. To achieve this, we introduce a third tower that contains the frozen pretrained embeddings, and we encourage alignment between this third tower and the main image-text towers. Empirically, 3T consistently improves over LiT and the CLIP-style from-scratch baseline for retrieval tasks. For classification, 3T reliably improves over the from-scratch baseline, and while it underperforms relative to LiT for JFT-pretrained models, it outperforms LiT for ImageNet-21k and Places365 pretraining.

</details>

### Certifiably Robust Graph Contrastive Learning.
- **链接**: [arXiv:2310.03312](https://arxiv.org/abs/2310.03312) · [代码](https://github.com/ventr1c/RES-GCL) · 📚 被引 2
- **作者**: Minhua Lin, Teng Xiao, Enyan Dai, Xiang Zhang, Suhang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Contrastive Learning (GCL) has emerged as a popular unsupervised graph representation learning method. However, it has been shown that GCL is vulnerable to adversarial attacks on both the graph structure and node attributes. Although empirical approaches have been proposed to enhance the robustness of GCL, the certifiable robustness of GCL is still remain unexplored. In this paper, we develop the first certifiably robust framework in GCL. Specifically, we first propose a unified criteria to evaluate and certify the robustness of GCL. We then introduce a novel technique, RES (Randomized Edgedrop Smoothing), to ensure certifiable robustness for any GCL model, and this certified robustness can be provably preserved in downstream tasks. Furthermore, an effective training method is proposed for robust GCL. Extensive experiments on real-world datasets demonstrate the effectiveness of our proposed method in providing effective certifiable robustness and enhancing the robustness of any GCL model. The source code of RES is available at https://github.com/ventr1c/RES-GCL.

</details>

### Towards Semi-Structured Automatic ICD Coding via Tree-based Contrastive Learning.
- **链接**: [arXiv:2310.09672](https://arxiv.org/abs/2310.09672) · 📚 被引 2
- **作者**: Chang Lu, Chandan K. Reddy, Ping Wang, Yue Ning
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Automatic coding of International Classification of Diseases (ICD) is a multi-label text categorization task that involves extracting disease or procedure codes from clinical notes. Despite the application of state-of-the-art natural language processing (NLP) techniques, there are still challenges including limited availability of data due to privacy constraints and the high variability of clinical notes caused by different writing habits of medical professionals and various pathological features of patients. In this work, we investigate the semi-structured nature of clinical notes and propose an automatic algorithm to segment them into sections. To address the variability issues in existing ICD coding models with limited data, we introduce a contrastive pre-training approach on sections using a soft multi-label similarity metric based on tree edit distance. Additionally, we design a masked section training strategy to enable ICD coding models to locate sections related to ICD codes. Extensive experimental results demonstrate that our proposed training strategies effectively enhance the performance of existing ICD coding methods.

</details>

### Towards a Unified Framework of Contrastive Learning for Disentangled Representations.
- **链接**: [arXiv:2311.04774](https://arxiv.org/abs/2311.04774) · 📚 被引 2
- **作者**: Stefan Matthes, Zhiwei Han, Hao Shen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has recently emerged as a promising approach for learning data representations that discover and disentangle the explanatory factors of the data. Previous analyses of such approaches have largely focused on individual contrastive losses, such as noise-contrastive estimation (NCE) and InfoNCE, and rely on specific assumptions about the data generating process. This paper extends the theoretical guarantees for disentanglement to a broader family of contrastive methods, while also relaxing the assumptions about the data distribution. Specifically, we prove identifiability of the true latents for four contrastive losses studied in this paper, without imposing common independence assumptions. The theoretical findings are validated on several benchmark datasets. Finally, practical limitations of these methods are also investigated.

</details>

### Slimmed Asymmetrical Contrastive Learning and Cross Distillation for Lightweight Model Training.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/8393d955a00c463a982cefe77d0404e1-Abstract-Conference.html) · 📚 被引 1
- **作者**: Jian Meng, Li Yang, Kyungmin Lee, Jinwoo Shin, Deliang Fan, Jae-sun Seo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors.
- **链接**: [arXiv:2305.18274](https://arxiv.org/abs/2305.18274) · 📚 被引 23
- **作者**: Paul S. Scotti, Atmadeep Banerjee, Jimmie Goode, Stepan Shabalin, Alex Nguyen, Ethan Cohen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present MindEye, a novel fMRI-to-image approach to retrieve and reconstruct viewed images from brain activity. Our model comprises two parallel submodules that are specialized for retrieval (using contrastive learning) and reconstruction (using a diffusion prior). MindEye can map fMRI brain activity to any high dimensional multimodal latent space, like CLIP image space, enabling image reconstruction using generative models that accept embeddings from this latent space. We comprehensively compare our approach with other existing methods, using both qualitative side-by-side comparisons and quantitative evaluations, and show that MindEye achieves state-of-the-art performance in both reconstruction and retrieval tasks. In particular, MindEye can retrieve the exact original image even among highly similar candidates indicating that its brain embeddings retain fine-grained image-specific information. This allows us to accurately retrieve images even from large-scale databases like LAION-5B. We demonstrate through ablations that MindEye's performance improvements over previous methods result from specialized submodules for retrieval and reconstruction, improved training techniques, and training models with orders of magnitude more parameters. Furthermore, we show that MindEye can better preserve low-level image features in the reconstructions by using img2img, with outputs from a separate autoencoder. All code is available on GitHub.

</details>

### Feature Dropout: Revisiting the Role of Augmentations in Contrastive Learning.
- **链接**: [arXiv:2212.08378](https://arxiv.org/abs/2212.08378) · 📚 被引 0
- **作者**: Alex Tamkin, Margalit Glasgow, Xiluo He, Noah D. Goodman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> What role do augmentations play in contrastive learning? Recent work suggests that good augmentations are label-preserving with respect to a specific downstream task. We complicate this picture by showing that label-destroying augmentations can be useful in the foundation model setting, where the goal is to learn diverse, general-purpose representations for multiple downstream tasks. We perform contrastive learning experiments on a range of image and audio datasets with multiple downstream tasks (e.g. for digits superimposed on photographs, predicting the class of one vs. the other). We find that Viewmaker Networks, a recently proposed model for learning augmentations for contrastive learning, produce label-destroying augmentations that stochastically destroy features needed for different downstream tasks. These augmentations are interpretable (e.g. altering shapes, digits, or letters added to images) and surprisingly often result in better performance compared to expert-designed augmentations, despite not preserving label information. To support our empirical results, we theoretically analyze a simple contrastive learning setting with a linear model. In this setting, label-destroying augmentations are crucial for preventing one set of features from suppressing the learning of features useful for another downstream task. Our results highlight the need for analyzing the interaction between multiple downstream tasks when trying to explain the success of foundation models.

</details>

### AI for Interpretable Chemistry: Predicting Radical Mechanistic Pathways via Contrastive Learning.
- **链接**: [arXiv:2311.01118](https://arxiv.org/abs/2311.01118) · 📚 被引 2
- **作者**: Mohammadamin Tavakoli, Pierre Baldi, Ann Marie Carlton, Yin Ting T. Chiu, Alexander Shmakov, David Van Vranken
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning-based reaction predictors have undergone significant architectural evolution. However, their reliance on reactions from the US Patent Office results in a lack of interpretable predictions and limited generalization capability to other chemistry domains, such as radical and atmospheric chemistry. To address these challenges, we introduce a new reaction predictor system, RMechRP, that leverages contrastive learning in conjunction with mechanistic pathways, the most interpretable representation of chemical reactions. Specifically designed for radical reactions, RMechRP provides different levels of interpretation of chemical reactions. We develop and train multiple deep-learning models using RMechDB, a public database of radical reactions, to establish the first benchmark for predicting radical reactions. Our results demonstrate the effectiveness of RMechRP in providing accurate and interpretable predictions of radical reactions, and its potential for various applications in atmospheric chemistry.

</details>

### Towards robust and generalizable representations of extracellular data using contrastive learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/83c637c3bc0ca88eda6cf4f5f45bdced-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ankit Vishnubhotla, Charlotte Loh, Akash Srivastava, Liam Paninski, Cole L. Hurwitz
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Understanding Contrastive Learning via Distributionally Robust Optimization.
- **链接**: [arXiv:2310.11048](https://arxiv.org/abs/2310.11048) · [代码](https://github.com/junkangwu/ADNCE) · 📚 被引 6
- **作者**: Junkang Wu, Jiawei Chen, Jiancan Wu, Wentao Shi, Xiang Wang, Xiangnan He
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This study reveals the inherent tolerance of contrastive learning (CL) towards sampling bias, wherein negative samples may encompass similar semantics (\eg labels). However, existing theories fall short in providing explanations for this phenomenon. We bridge this research gap by analyzing CL through the lens of distributionally robust optimization (DRO), yielding several key insights: (1) CL essentially conducts DRO over the negative sampling distribution, thus enabling robust performance across a variety of potential distributions and demonstrating robustness to sampling bias; (2) The design of the temperature $τ$ is not merely heuristic but acts as a Lagrange Coefficient, regulating the size of the potential distribution set; (3) A theoretical connection is established between DRO and mutual information, thus presenting fresh evidence for ``InfoNCE as an estimate of MI'' and a new estimation approach for $φ$-divergence-based generalized mutual information. We also identify CL's potential shortcomings, including over-conservatism and sensitivity to outliers, and introduce a novel Adjusted InfoNCE loss (ADNCE) to mitigate these issues. It refines potential distribution, improving performance and accelerating convergence. Extensive experiments on various domains (image, sentence, and graphs) validate the effectiveness of the proposal. The code is available at \url{https://github.com/junkangwu/ADNCE}.

</details>

### Simple and Asymmetric Graph Contrastive Learning without Augmentations.
- **链接**: [arXiv:2310.18884](https://arxiv.org/abs/2310.18884) · [代码](https://github.com/tengxiao1/GraphACL) · 📚 被引 7
- **作者**: Teng Xiao, Huaisheng Zhu, Zhengyu Chen, Suhang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Contrastive Learning (GCL) has shown superior performance in representation learning in graph-structured data. Despite their success, most existing GCL methods rely on prefabricated graph augmentation and homophily assumptions. Thus, they fail to generalize well to heterophilic graphs where connected nodes may have different class labels and dissimilar features. In this paper, we study the problem of conducting contrastive learning on homophilic and heterophilic graphs. We find that we can achieve promising performance simply by considering an asymmetric view of the neighboring nodes. The resulting simple algorithm, Asymmetric Contrastive Learning for Graphs (GraphACL), is easy to implement and does not rely on graph augmentations and homophily assumptions. We provide theoretical and empirical evidence that GraphACL can capture one-hop local neighborhood information and two-hop monophily similarity, which are both important for modeling heterophilic graphs. Experimental results show that the simple GraphACL significantly outperforms state-of-the-art graph contrastive learning and self-supervised learning methods on homophilic and heterophilic graphs. The code of GraphACL is available at https://github.com/tengxiao1/GraphACL.

</details>

### Spatially Resolved Gene Expression Prediction from Histology Images via Bi-modal Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/df656d6ed77b565e8dcdfbf568aead0a-Abstract-Conference.html) · 📚 被引 21
- **作者**: Ronald Xie, Kuan Pang, Sai Chung, Catia Perciani, Sonya MacParland, Bo Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Enhancing Adversarial Contrastive Learning via Adversarial Invariant Regularization.
- **链接**: [arXiv:2305.00374](https://arxiv.org/abs/2305.00374) · [代码](https://github.com/GodXuxilie/Enhancing_ACL_via_AIR) · 📚 被引 2
- **作者**: Xilie Xu, Jingfeng Zhang, Feng Liu, Masashi Sugiyama, Mohan S. Kankanhalli
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial contrastive learning (ACL) is a technique that enhances standard contrastive learning (SCL) by incorporating adversarial data to learn a robust representation that can withstand adversarial attacks and common corruptions without requiring costly annotations. To improve transferability, the existing work introduced the standard invariant regularization (SIR) to impose style-independence property to SCL, which can exempt the impact of nuisance style factors in the standard representation. However, it is unclear how the style-independence property benefits ACL-learned robust representations. In this paper, we leverage the technique of causal reasoning to interpret the ACL and propose adversarial invariant regularization (AIR) to enforce independence from style factors. We regulate the ACL using both SIR and AIR to output the robust representation. Theoretically, we show that AIR implicitly encourages the representational distance between different views of natural data and their adversarial variants to be independent of style factors. Empirically, our experimental results show that invariant regularization significantly improves the performance of state-of-the-art ACL methods in terms of both standard generalization and robustness on downstream tasks. To the best of our knowledge, we are the first to apply causal reasoning to interpret ACL and develop AIR for enhancing ACL-learned robust representations. Our source code is at https://github.com/GodXuxilie/Enhancing_ACL_via_AIR.

</details>

### Efficient Adversarial Contrastive Learning via Robustness-Aware Coreset Selection.
- **链接**: [arXiv:2302.03857](https://arxiv.org/abs/2302.03857) · [代码](https://github.com/GodXuxilie/Efficient_ACL_via_RCS) · 📚 被引 1
- **作者**: Xilie Xu, Jingfeng Zhang, Feng Liu, Masashi Sugiyama, Mohan S. Kankanhalli
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial contrastive learning (ACL) does not require expensive data annotations but outputs a robust representation that withstands adversarial attacks and also generalizes to a wide range of downstream tasks. However, ACL needs tremendous running time to generate the adversarial variants of all training data, which limits its scalability to large datasets. To speed up ACL, this paper proposes a robustness-aware coreset selection (RCS) method. RCS does not require label information and searches for an informative subset that minimizes a representational divergence, which is the distance of the representation between natural data and their virtual adversarial variants. The vanilla solution of RCS via traversing all possible subsets is computationally prohibitive. Therefore, we theoretically transform RCS into a surrogate problem of submodular maximization, of which the greedy search is an efficient solution with an optimality guarantee for the original problem. Empirically, our comprehensive results corroborate that RCS can speed up ACL by a large margin without significantly hurting the robustness transferability. Notably, to the best of our knowledge, we are the first to conduct ACL efficiently on the large-scale ImageNet-1K dataset to obtain an effective robust representation via RCS. Our source code is at https://github.com/GodXuxilie/Efficient_ACL_via_RCS.

</details>

### Provable Training for Graph Contrastive Learning.
- **链接**: [arXiv:2309.13944](https://arxiv.org/abs/2309.13944) · 📚 被引 1
- **作者**: Yue Yu, Xiao Wang, Mengmei Zhang, Nian Liu, Chuan Shi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Contrastive Learning (GCL) has emerged as a popular training approach for learning node embeddings from augmented graphs without labels. Despite the key principle that maximizing the similarity between positive node pairs while minimizing it between negative node pairs is well established, some fundamental problems are still unclear. Considering the complex graph structure, are some nodes consistently well-trained and following this principle even with different graph augmentations? Or are there some nodes more likely to be untrained across graph augmentations and violate the principle? How to distinguish these nodes and further guide the training of GCL? To answer these questions, we first present experimental evidence showing that the training of GCL is indeed imbalanced across all nodes. To address this problem, we propose the metric "node compactness", which is the lower bound of how a node follows the GCL principle related to the range of augmentations. We further derive the form of node compactness theoretically through bound propagation, which can be integrated into binary cross-entropy as a regularization. To this end, we propose the PrOvable Training (POT) for GCL, which regularizes the training of GCL to encode node embeddings that follows the GCL principle better. Through extensive experiments on various benchmarks, POT consistently improves the existing GCL approaches, serving as a friendly plugin.

</details>

### Identifiable Contrastive Learning with Automatic Feature Importance Discovery.
- **链接**: [arXiv:2310.18904](https://arxiv.org/abs/2310.18904) · [代码](https://github.com/PKU-ML/Tri-factor-Contrastive-Learning) · 📚 被引 0
- **作者**: Qi Zhang, Yifei Wang, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing contrastive learning methods rely on pairwise sample contrast $z_x^\top z_{x'}$ to learn data representations, but the learned features often lack clear interpretability from a human perspective. Theoretically, it lacks feature identifiability and different initialization may lead to totally different features. In this paper, we study a new method named tri-factor contrastive learning (triCL) that involves a 3-factor contrast in the form of $z_x^\top S z_{x'}$, where $S=\text{diag}(s_1,\dots,s_k)$ is a learnable diagonal matrix that automatically captures the importance of each feature. We show that by this simple extension, triCL can not only obtain identifiable features that eliminate randomness but also obtain more interpretable features that are ordered according to the importance matrix $S$. We show that features with high importance have nice interpretability by capturing common classwise features, and obtain superior performance when evaluated for image retrieval using a few features. The proposed triCL objective is general and can be applied to different contrastive learning methods like SimCLR and CLIP. We believe that it is a better alternative to existing 2-factor contrastive learning by improving its identifiability and interpretability with minimal overhead. Code is available at https://github.com/PKU-ML/Tri-factor-Contrastive-Learning.

</details>

### RevColV2: Exploring Disentangled Representations in Masked Image Modeling.
- **链接**: [arXiv:2309.01005](https://arxiv.org/abs/2309.01005) · [代码](https://github.com/megvii-research/RevCol) · 📚 被引 1
- **作者**: Qi Han, Yuxuan Cai, Xiangyu Zhang
- **🏷️ 机构**: MEGVII
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked image modeling (MIM) has become a prevalent pre-training setup for vision foundation models and attains promising performance. Despite its success, existing MIM methods discard the decoder network during downstream applications, resulting in inconsistent representations between pre-training and fine-tuning and can hamper downstream task performance. In this paper, we propose a new architecture, RevColV2, which tackles this issue by keeping the entire autoencoder architecture during both pre-training and fine-tuning. The main body of RevColV2 contains bottom-up columns and top-down columns, between which information is reversibly propagated and gradually disentangled. Such design enables our architecture with the nice property: maintaining disentangled low-level and semantic information at the end of the network in MIM pre-training. Our experimental results suggest that a foundation model with decoupled features can achieve competitive performance across multiple downstream vision tasks such as image classification, semantic segmentation and object detection. For example, after intermediate fine-tuning on ImageNet-22K dataset, RevColV2-L attains 88.4% top-1 accuracy on ImageNet-1K classification and 58.6 mIoU on ADE20K semantic segmentation. With extra teacher and large scale dataset, RevColv2-L achieves 62.1 box AP on COCO detection and 60.4 mIoU on ADE20K semantic segmentation. Code and models are released at https://github.com/megvii-research/RevCol

</details>

### HAP: Structure-Aware Masked Image Modeling for Human-Centric Perception.
- **链接**: [arXiv:2310.20695](https://arxiv.org/abs/2310.20695) · 📚 被引 1
- **作者**: Junkun Yuan, Xinyu Zhang, Hao Zhou, Jian Wang, Zhongwei Qiu, Zhiyin Shao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model pre-training is essential in human-centric perception. In this paper, we first introduce masked image modeling (MIM) as a pre-training approach for this task. Upon revisiting the MIM training strategy, we reveal that human structure priors offer significant potential. Motivated by this insight, we further incorporate an intuitive human structure prior - human parts - into pre-training. Specifically, we employ this prior to guide the mask sampling process. Image patches, corresponding to human part regions, have high priority to be masked out. This encourages the model to concentrate more on body structure information during pre-training, yielding substantial benefits across a range of human-centric perception tasks. To further capture human characteristics, we propose a structure-invariant alignment loss that enforces different masked views, guided by the human part prior, to be closely aligned for the same image. We term the entire method as HAP. HAP simply uses a plain ViT as the encoder yet establishes new state-of-the-art performance on 11 human-centric benchmarks, and on-par result on one dataset. For example, HAP achieves 78.1% mAP on MSMT17 for person re-identification, 86.54% mA on PA-100K for pedestrian attribute recognition, 78.2% AP on MS COCO for 2D pose estimation, and 56.0 PA-MPJPE on 3DPW for 3D pose and shape estimation.

</details>

### Self-Supervised Image-to-Point Distillation via Semantically Tolerant Contrastive Loss.
- **链接**: [arXiv:2301.05709](https://arxiv.org/abs/2301.05709) · 📚 被引 29
- **作者**: Anas Mahmoud, Jordan S. K. Hu, Tianshu Kuai, Ali Harakeh, Liam Paull, Steven L. Waslander
- **🏷️ 机构**: University of Toronto Robotics Institute, Mila, Universit&#x00E9; de Montr&#x00E9;al
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An effective framework for learning 3D representations for perception tasks is distilling rich self-supervised image features via contrastive learning. However, image-to point representation learning for autonomous driving datasets faces two main challenges: 1) the abundance of self-similarity, which results in the contrastive losses pushing away semantically similar point and image regions and thus disturbing the local semantic structure of the learned representations, and 2) severe class imbalance as pretraining gets dominated by over-represented classes. We propose to alleviate the self-similarity problem through a novel semantically tolerant image-to-point contrastive loss that takes into consideration the semantic distance between positive and negative image regions to minimize contrasting semantically similar point and image regions. Additionally, we address class imbalance by designing a class-agnostic balanced loss that approximates the degree of class imbalance through an aggregate sample-to-samples semantic similarity measure. We demonstrate that our semantically-tolerant contrastive loss with class balancing improves state-of-the art 2D-to-3D representation learning in all evaluation settings on 3D semantic segmentation. Our method consistently outperforms state-of-the-art 2D-to-3D representation learning frameworks across a wide range of 2D self-supervised pretrained models.

</details>

### Multi-Mode Online Knowledge Distillation for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2304.06461](https://arxiv.org/abs/2304.06461) · 📚 被引 38
- **作者**: Kaiyou Song, Jin Xie, Shan Zhang, Zimeng Luo
- **🏷️ 机构**: Megvii Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has made remarkable progress in visual representation learning. Some studies combine SSL with knowledge distillation (SSL-KD) to boost the representation learning performance of small models. In this study, we propose a Multi-mode Online Knowledge Distillation method (MOKD) to boost self-supervised visual representation learning. Different from existing SSL-KD methods that transfer knowledge from a static pre-trained teacher to a student, in MOKD, two different models learn collaboratively in a self-supervised manner. Specifically, MOKD consists of two distillation modes: self-distillation and cross-distillation modes. Among them, self-distillation performs self-supervised learning for each model independently, while cross-distillation realizes knowledge interaction between different models. In cross-distillation, a cross-attention feature search strategy is proposed to enhance the semantic feature alignment between different models. As a result, the two models can absorb knowledge from each other to boost their representation learning performance. Extensive experimental results on different backbones and datasets demonstrate that two heterogeneous models can benefit from MOKD and outperform their independently trained baseline. In addition, MOKD also outperforms existing SSL-KD methods for both the student and teacher models.

</details>

### Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00611)
- **作者**: Rui Wang, Dongdong Chen, Zuxuan Wu, Yinpeng Chen, Xiyang Dai, Mengchen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- Mask DINO: Towards A Unified Transformer-based Framework for Object Detection and Segmentation. → [object-detection](../object-detection/Guideline%202023.md)
- Object Detection with Self-Supervised Scene Adaptation. → [object-detection](../object-detection/Guideline%202023.md)
- MV-JAR: Masked Voxel Jigsaw and Reconstruction for LiDAR-Based Self-Supervised Pre-Training. → [3d-detection](../3d-detection/Guideline%202023.md)
- BKinD-3D: Self-Supervised 3D Keypoint Discovery from Multi-View Videos. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Lite-Mono: A Lightweight CNN and Transformer Architecture for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Open Vocabulary Semantic Segmentation with Patch Aligned Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Revisiting Multimodal Representation in Contrastive Learning: From Patch and Token Embeddings to Finite Discrete Tokens. → [multimodal](../multimodal/Guideline%202023.md)
- Self-Supervised Learning for Multimodal Non-Rigid 3D Shape Matching. → [multimodal](../multimodal/Guideline%202023.md)
- Best of Both Worlds: Multimodal Contrastive Learning with Tabular and Imaging Data. → [multimodal](../multimodal/Guideline%202023.md)
- PlaneDepth: Self-Supervised Depth Estimation via Orthogonal Planes. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- DualRefine: Self-Supervised Depth and Pose Estimation Through Iterative Epipolar Sampling and Refinement Toward Equilibrium. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Self-Supervised Video Forensics by Audio-Visual Anomaly Detection. → [multimodal](../multimodal/Guideline%202023.md)
- Coreset Sampling from Open-Set for Fine-Grained Self-Supervised Learning. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Fully Self-Supervised Depth Estimation from Defocus Clue. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Learning Audio-Visual Source Localization via False Negative Aware Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- Hunting Sparsity: Density-Guided Contrastive Learning for Semi-Supervised Semantic Segmentation. → [network-pruning](../network-pruning/Guideline%202023.md)
