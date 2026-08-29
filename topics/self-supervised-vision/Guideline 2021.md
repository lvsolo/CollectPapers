# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 7 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### SLIM: Self-Supervised LiDAR Scene Flow and Motion Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01288) · 📚 被引 59
- **作者**: Stefan Andreas Baur, David Josef Emmerichs, Frank Moosmann, Peter Pinggera, Björn Ommer, Andreas Geiger
- **🏷️ 机构**: Mercedes-Benz AG,Stuttgart, University of Munich,Ludwig Maximilian, MPI-IS,T&#x00FC;bingen
- **会议**: ICCV 2021

### Guided Point Contrastive Learning for Semi-supervised Point Cloud Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00636) · 📚 被引 121
- **作者**: Li Jiang, Shaoshuai Shi, Zhuotao Tian, Xin Lai, Shu Liu, Chi-Wing Fu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, SmartMore
- **会议**: ICCV 2021

### Spatio-temporal Self-Supervised Representation Learning for 3D Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00647) · 📚 被引 187
- **作者**: Siyuan Huang, Yichen Xie, Song-Chun Zhu, Yixin Zhu
- **🏷️ 机构**: University of California,Los Angeles, Shanghai Jiao Tong University, Beijing Institute for General Artificial Intelligence
- **会议**: ICCV 2021

### Unsupervised Point Cloud Object Co-segmentation by Co-contrastive Learning and Mutual Attention Sampling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00724) · 📚 被引 13
- **作者**: Cheng-Kun Yang, Yung-Yu Chuang, Yen-Yu Lin
- **🏷️ 机构**: National Taiwan University, National Yang Ming Chiao Tung University
- **会议**: ICCV 2021

### Self-Supervised Pretraining of 3D Features on any Point-Cloud.
- **链接**: [arXiv:2101.02691](https://arxiv.org/abs/2101.02691)
- **作者**: Zaiwei Zhang, Rohit Girdhar, Armand Joulin, Ishan Misra
- **🏷️ 机构**: Facebook AI Research
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretraining on large labeled datasets is a prerequisite to achieve good performance in many computer vision tasks like 2D object recognition, video classification etc. However, pretraining is not widely used for 3D recognition tasks where state-of-the-art methods train models from scratch. A primary reason is the lack of large annotated datasets because 3D data is both difficult to acquire and time consuming to label. We present a simple self-supervised pertaining method that can work with any 3D data - single or multiview, indoor or outdoor, acquired by varied sensors, without 3D registration. We pretrain standard point cloud and voxel based model architectures, and show that joint pretraining further improves performance. We evaluate our models on 9 benchmarks for object detection, semantic segmentation, and object classification, where they achieve state-of-the-art results and can outperform supervised pretraining. We set a new state-of-the-art for object detection on ScanNet (69.0% mAP) and SUNRGBD (63.5% mAP). Our pretrained models are label efficient and improve performance for classes with few examples.

</details>

### Can Scale-Consistent Monocular Depth Be Learned in a Self-Supervised Scale-Invariant Manner?
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01249) · 📚 被引 42
- **作者**: Lijun Wang, Yifan Wang, Linzhao Wang, Yunlong Zhan, Ying Wang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology, Huawei Technologies Co., Ltd.
- **会议**: ICCV 2021

### Emerging Properties in Self-Supervised Vision Transformers.
- **链接**: [arXiv:2104.14294](https://arxiv.org/abs/2104.14294) · 📚 被引 5214
- **作者**: Mathilde Caron, Hugo Touvron, Ishan Misra, Hervé Jégou, Julien Mairal, Piotr Bojanowski et al.
- **🏷️ 机构**: Facebook AI Research, Univ. Grenoble Alpes, Inria, CNRS,Grenoble,France,38000
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we question if self-supervised learning provides new properties to Vision Transformer (ViT) that stand out compared to convolutional networks (convnets). Beyond the fact that adapting self-supervised methods to this architecture works particularly well, we make the following observations: first, self-supervised ViT features contain explicit information about the semantic segmentation of an image, which does not emerge as clearly with supervised ViTs, nor with convnets. Second, these features are also excellent k-NN classifiers, reaching 78.3% top-1 on ImageNet with a small ViT. Our study also underlines the importance of momentum encoder, multi-crop training, and the use of small patches with ViTs. We implement our findings into a simple self-supervised method, called DINO, which we interpret as a form of self-distillation with no labels. We show the synergy between DINO and ViTs by achieving 80.1% top-1 on ImageNet in linear evaluation with ViT-Base.

</details>

### An Empirical Study of Training Self-Supervised Vision Transformers.
- **链接**: [arXiv:2104.02057](https://arxiv.org/abs/2104.02057) · 📚 被引 1399
- **作者**: Xinlei Chen, Saining Xie, Kaiming He
- **🏷️ 机构**: Facebook AI Research (FAIR)
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper does not describe a novel method. Instead, it studies a straightforward, incremental, yet must-know baseline given the recent progress in computer vision: self-supervised learning for Vision Transformers (ViT). While the training recipes for standard convolutional networks have been highly mature and robust, the recipes for ViT are yet to be built, especially in the self-supervised scenarios where training becomes more challenging. In this work, we go back to basics and investigate the effects of several fundamental components for training self-supervised ViT. We observe that instability is a major issue that degrades accuracy, and it can be hidden by apparently good results. We reveal that these results are indeed partial failure, and they can be improved when training is made more stable. We benchmark ViT results in MoCo v3 and several other self-supervised frameworks, with ablations in various aspects. We discuss the currently positive evidence as well as challenges and open questions. We hope that this work will provide useful data points and experience for future research.

</details>

### SelfReg: Self-supervised Contrastive Regularization for Domain Generalization.
- **链接**: [arXiv:2104.09841](https://arxiv.org/abs/2104.09841) · [代码](https://github.com/dnap512/SelfReg) · 📚 被引 241
- **作者**: Daehee Kim, Youngjun Yoo, Seunghyun Park, Jinkyu Kim, Jaekoo Lee
- **🏷️ 机构**: Kookmin University,College of Computer Science, NAVER Corp,Clova AI Research, Korea University,Department of Computer Science and Engineering
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In general, an experimental environment for deep learning assumes that the training and the test dataset are sampled from the same distribution. However, in real-world situations, a difference in the distribution between two datasets, domain shift, may occur, which becomes a major factor impeding the generalization performance of the model. The research field to solve this problem is called domain generalization, and it alleviates the domain shift problem by extracting domain-invariant features explicitly or implicitly. In recent studies, contrastive learning-based domain generalization approaches have been proposed and achieved high performance. These approaches require sampling of the negative data pair. However, the performance of contrastive learning fundamentally depends on quality and quantity of negative data pairs. To address this issue, we propose a new regularization method for domain generalization based on contrastive learning, self-supervised contrastive regularization (SelfReg). The proposed approach use only positive data pairs, thus it resolves various problems caused by negative pair sampling. Moreover, we propose a class-specific domain perturbation layer (CDPL), which makes it possible to effectively apply mixup augmentation even when only positive data pairs are used. The experimental results show that the techniques incorporated by SelfReg contributed to the performance in a compatible manner. In the recent benchmark, DomainBed, the proposed method shows comparable performance to the conventional state-of-the-art alternatives. Codes are available at https://github.com/dnap512/SelfReg.

</details>

### SeLFVi: Self-supervised Light-Field Video Reconstruction from Stereo Video.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00249) · 📚 被引 6
- **作者**: Prasan A. Shedligeri, Florian Schiffers, Sushobhan Ghosh, Oliver Cossairt, Kaushik Mitra
- **🏷️ 机构**: IIT Madras,India, Northwestern University,USA
- **会议**: ICCV 2021

### Geography-Aware Self-Supervised Learning.
- **链接**: [arXiv:2011.09980](https://arxiv.org/abs/2011.09980)
- **作者**: Kumar Ayush, Burak Uzkent, Chenlin Meng, Kumar Tanmay, Marshall Burke, David B. Lobell et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Guided Point Contrastive Learning for Semi-supervised Point Cloud Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00636) · 📚 被引 121
- **作者**: Li Jiang, Shaoshuai Shi, Zhuotao Tian, Xin Lai, Shu Liu, Chi-Wing Fu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, SmartMore
- **会议**: ICCV 2021

### Spatio-temporal Self-Supervised Representation Learning for 3D Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00647) · 📚 被引 187
- **作者**: Siyuan Huang, Yichen Xie, Song-Chun Zhu, Yixin Zhu
- **🏷️ 机构**: University of California,Los Angeles, Shanghai Jiao Tong University, Beijing Institute for General Artificial Intelligence
- **会议**: ICCV 2021

### Unsupervised Point Cloud Object Co-segmentation by Co-contrastive Learning and Mutual Attention Sampling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00724) · 📚 被引 13
- **作者**: Cheng-Kun Yang, Yung-Yu Chuang, Yen-Yu Lin
- **🏷️ 机构**: National Taiwan University, National Yang Ming Chiao Tung University
- **会议**: ICCV 2021

</details>

### The Temporal Opportunist: Self-Supervised Multi-Frame Monocular Depth.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Watson_The_Temporal_Opportunist_Self-Supervised_Multi-Frame_Monocular_Depth_CVPR_2021_paper.html) · 📚 被引 316
- **作者**: Jamie Watson, Oisin Mac Aodha, Victor Prisacariu, Gabriel J. Brostow, Michael Firman
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In self-supervised representation learning, a common idea behind most of the state-of-the-art approaches is to enforce the robustness of the representations to predefined augmentations. A potential issue of this idea is the existence of completely collapsed solutions (i.e., constant features), which are typically avoided implicitly by carefully chosen implementation details. In this work, we study a relatively concise framework containing the most common components from recent approaches. We verify the existence of complete collapse and discover another reachable collapse pattern that is usually overlooked, namely dimensional collapse. We connect dimensional collapse with strong correlations between axes and consider such connection as a strong motivation for feature decorrelation (i.e., standardizing the covariance matrix). The gains from feature decorrelation are verified empirically to highlight the importance and the potential of this insight.

</details>

### ASCNet: Self-supervised Video Representation Learning with Appearance-Speed Consistency.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00799)
- **作者**: Deng Huang, Wenhao Wu, Weiwen Hu, Xu Liu, Dongliang He, Zhihua Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine learning-based program analyses have recently shown the promise of integrating formal and probabilistic reasoning towards aiding software development. However, in the absence of large annotated corpora, training these analyses is challenging. Towards addressing this, we present BugLab, an approach for self-supervised learning of bug detection and repair. BugLab co-trains two models: (1) a detector model that learns to detect and repair bugs in code, (2) a selector model that learns to create buggy code for the detector to use as training data. A Python implementation of BugLab improves by up to 30% upon baseline methods on a test dataset of 2374 real-life bugs and finds 19 previously unknown bugs in open-source software.

</details>

> Supervised deep learning-based hash and vector quantization are enabling fast and large-scale image retrieval systems. By fully exploiting label annotations, they are achieving outstanding retrieval performances compared to the conventional methods. However, it is painstaking to assign labels precisely for a vast amount of training data, and also, the annotation process is error-prone. To tackle these issues, we propose the first deep unsupervised image retrieval method dubbed Self-supervised Product Quantization (SPQ) network, which is label-free and trained in a self-supervised manner. We design a Cross Quantized Contrastive learning strategy that jointly learns codewords and deep visual descriptors by comparing individually transformed images (views). Our method analyzes the image contents to extract descriptive features, allowing us to understand image representations for accurate retrieval. By conducting extensive experiments on benchmarks, we demonstrate that the proposed method yields state-of-the-art results even without supervised pretraining.

</details>

### SSH: A Self-Supervised Framework for Image Harmonization.
- **链接**: [arXiv:2108.06805](https://arxiv.org/abs/2108.06805) · [代码](https://github.com/VITA-Group/SSHarmonization) · 📚 被引 69
- **作者**: Yifan Jiang, He Zhang, Jianming Zhang, Yilin Wang, Zhe Lin, Kalyan Sunkavalli et al.
- **🏷️ 机构**: The University of Texas at Austin, Adobe Inc
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image harmonization aims to improve the quality of image compositing by matching the "appearance" (\eg, color tone, brightness and contrast) between foreground and background images. However, collecting large-scale annotated datasets for this task requires complex professional retouching. Instead, we propose a novel Self-Supervised Harmonization framework (SSH) that can be trained using just "free" natural images without being edited. We reformulate the image harmonization problem from a representation fusion perspective, which separately processes the foreground and background examples, to address the background occlusion issue. This framework design allows for a dual data augmentation method, where diverse [foreground, background, pseudo GT] triplets can be generated by cropping an image with perturbations using 3D color lookup tables (LUTs). In addition, we build a real-world harmonization dataset as carefully created by expert users, for evaluation and benchmarking purposes. Our results show that the proposed self-supervised method outperforms previous state-of-the-art methods in terms of reference metrics, visual quality, and subject user study. Code and dataset are available at \url{https://github.com/VITA-Group/SSHarmonization}.

</details>

### Contrastive Attention Maps for Self-supervised Co-localization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00280) · 📚 被引 10
- **作者**: Minsong Ki, Youngjung Uh, Junsuk Choe, Hyeran Byun
- **🏷️ 机构**: Yonsei University,Department of Computer Science, Yonsei University,Department of Applied Information Engineering, Sogang University,Department of Computer Science and Engineering
- **会议**: ICCV 2021

### CDS: Cross-Domain Self-supervised Pre-training.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00899) · 📚 被引 40
- **作者**: Donghyun Kim, Kuniaki Saito, Tae-Hyun Oh, Bryan A. Plummer, Stan Sclaroff, Kate Saenko
- **🏷️ 机构**: Boston University, POSTECH
- **会议**: ICCV 2021

### Mean Shift for Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01016) · 📚 被引 67
- **作者**: Soroush Abbasi Koohpayegani, Ajinkya Tejankar, Hamed Pirsiavash
- **🏷️ 机构**: University of Maryland,Baltimore County
- **会议**: ICCV 2021

### Contrasting Contrastive Self-Supervised Representation Learning Pipelines.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00980) · 📚 被引 21
- **作者**: Klemen Kotar, Gabriel Ilharco, Ludwig Schmidt, Kiana Ehsani, Roozbeh Mottaghi
- **🏷️ 机构**: PRIOR @ Allen Institute for AI, University of Washington
- **会议**: ICCV 2021

### Video Autoencoder: self-supervised disentanglement of static 3D structure and motion.
- **链接**: [arXiv:2110.02951](https://arxiv.org/abs/2110.02951) · 📚 被引 30
- **作者**: Zihang Lai, Sifei Liu, Alexei A. Efros, Xiaolong Wang
- **🏷️ 机构**: Carnegie Mellon University, NVIDIA, UC Berkeley
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A video autoencoder is proposed for learning disentan- gled representations of 3D structure and camera pose from videos in a self-supervised manner. Relying on temporal continuity in videos, our work assumes that the 3D scene structure in nearby video frames remains static. Given a sequence of video frames as input, the video autoencoder extracts a disentangled representation of the scene includ- ing: (i) a temporally-consistent deep voxel feature to represent the 3D structure and (ii) a 3D trajectory of camera pose for each frame. These two representations will then be re-entangled for rendering the input video frames. This video autoencoder can be trained directly using a pixel reconstruction loss, without any ground truth 3D or camera pose annotations. The disentangled representation can be applied to a range of tasks, including novel view synthesis, camera pose estimation, and video generation by motion following. We evaluate our method on several large- scale natural video datasets, and show generalization results on out-of-domain images.

</details>

### Self-supervised Geometric Features Discovery via Interpretable Attention for Vehicle Re-Identification and Beyond.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00026) · 📚 被引 48
- **作者**: Ming Li, Xinming Huang, Ziming Zhang
- **🏷️ 机构**: Worcester Polytechnic Institute,Worcester,MA,USA
- **会议**: ICCV 2021

### StructDepth: Leveraging the structural regularities for self-supervised indoor depth estimation.
- **链接**: [arXiv:2108.08574](https://arxiv.org/abs/2108.08574) · [代码](https://github.com/SJTU-ViSYS/StructDepth) · 📚 被引 62
- **作者**: Boying Li, Yuan Huang, Zeyu Liu, Danping Zou, Wenxian Yu
- **🏷️ 机构**: Shanghai Key Laboratory of Navigation and Location-Based Services
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised monocular depth estimation has achieved impressive performance on outdoor datasets. Its performance however degrades notably in indoor environments because of the lack of textures. Without rich textures, the photometric consistency is too weak to train a good depth network. Inspired by the early works on indoor modeling, we leverage the structural regularities exhibited in indoor scenes, to train a better depth network. Specifically, we adopt two extra supervisory signals for self-supervised training: 1) the Manhattan normal constraint and 2) the co-planar constraint. The Manhattan normal constraint enforces the major surfaces (the floor, ceiling, and walls) to be aligned with dominant directions. The co-planar constraint states that the 3D points be well fitted by a plane if they are located within the same planar region. To generate the supervisory signals, we adopt two components to classify the major surface normal into dominant directions and detect the planar regions on the fly during training. As the predicted depth becomes more accurate after more training epochs, the supervisory signals also improve and in turn feedback to obtain a better depth model. Through extensive experiments on indoor benchmark datasets, the results show that our network outperforms the state-of-the-art methods. The source code is available at https://github.com/SJTU-ViSYS/StructDepth .

</details>

### Self-Supervised Video Representation Learning with Meta-Contrastive Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00813)
- **作者**: Yuanze Lin, Xun Guo, Yan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Self-Supervised Image Prior Learning with GMM from a Single Noisy Image.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00284) · 📚 被引 7
- **作者**: Haosen Liu, Xuan Liu, Jiangbo Lu, Shan Tan
- **🏷️ 机构**: Huazhong University of Science and Technology, SmartMore Corporation
- **会议**: ICCV 2021

### Self-Supervised Vessel Segmentation via Adversarial Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00744) · 📚 被引 79
- **作者**: Yuxin Ma, Yang Hua, Hanming Deng, Tao Song, Hao Wang, Zhengui Xue et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Queen&#x2019;s University Belfast, Louisiana State University
- **会议**: ICCV 2021

### Self-supervised Neural Networks for Spectral Snapshot Compressive Imaging.
- **链接**: [arXiv:2108.12654](https://arxiv.org/abs/2108.12654) · [代码](https://github.com/mengziyi64/CASSI-Self-Supervised) · 📚 被引 110
- **作者**: Ziyi Meng, Zhenming Yu, Kun Xu, Xin Yuan
- **🏷️ 机构**: Beijing University of Posts and Telecommunications, Westlake University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider using {\bf\em untrained neural networks} to solve the reconstruction problem of snapshot compressive imaging (SCI), which uses a two-dimensional (2D) detector to capture a high-dimensional (usually 3D) data-cube in a compressed manner. Various SCI systems have been built in recent years to capture data such as high-speed videos, hyperspectral images, and the state-of-the-art reconstruction is obtained by the deep neural networks. However, most of these networks are trained in an end-to-end manner by a large amount of corpus with sometimes simulated ground truth, measurement pairs. In this paper, inspired by the untrained neural networks such as deep image priors (DIP) and deep decoders, we develop a framework by integrating DIP into the plug-and-play regime, leading to a self-supervised network for spectral SCI reconstruction. Extensive synthetic and real data results show that the proposed algorithm without training is capable of achieving competitive results to the training based networks. Furthermore, by integrating the proposed method with a pre-trained deep denoising prior, we have achieved state-of-the-art results. {Our code is available at \url{https://github.com/mengziyi64/CASSI-Self-Supervised}.}

</details>

### Sample Efficient Detection and Classification of Adversarial Attacks via Self-Supervised Embeddings.
- **链接**: [arXiv:2108.13797](https://arxiv.org/abs/2108.13797) · 📚 被引 19
- **作者**: Mazda Moayeri, Soheil Feizi
- **🏷️ 机构**: University of Maryland,Department of Computer Science
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial robustness of deep models is pivotal in ensuring safe deployment in real world settings, but most modern defenses have narrow scope and expensive costs. In this paper, we propose a self-supervised method to detect adversarial attacks and classify them to their respective threat models, based on a linear model operating on the embeddings from a pre-trained self-supervised encoder. We use a SimCLR encoder in our experiments, since we show the SimCLR embedding distance is a good proxy for human perceptibility, enabling it to encapsulate many threat models at once. We call our method SimCat since it uses SimCLR encoder to catch and categorize various types of adversarial attacks, including L_p and non-L_p evasion attacks, as well as data poisonings. The simple nature of a linear classifier makes our method efficient in both time and sample complexity. For example, on SVHN, using only five pairs of clean and adversarial examples computed with a PGD-L_inf attack, SimCat's detection accuracy is over 85%. Moreover, on ImageNet, using only 25 examples from each threat model, SimCat can classify eight different attack types such as PGD-L_2, PGD-L_inf, CW-L_2, PPGD, LPA, StAdv, ReColor, and JPEG-L_inf, with over 40% accuracy. On STL10 data, we apply SimCat as a defense against poisoning attacks, such as BP, CP, FC, CLBD, HTBD, halving the success rate while using only twenty total poisons for training. We find that the detectors generalize well to unseen threat models. Lastly, we investigate the performance of our detection method under adaptive attacks and further boost its robustness against such attacks via adversarial training.

</details>

### Focus on the Positives: Self-Supervised Learning for Biodiversity Monitoring.
- **链接**: [arXiv:2108.06435](https://arxiv.org/abs/2108.06435) · 📚 被引 18
- **作者**: Omiros Pantazis, Gabriel J. Brostow, Kate E. Jones, Oisin Mac Aodha
- **🏷️ 机构**: University College London, University of Edinburgh
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the problem of learning self-supervised representations from unlabeled image collections. Unlike existing approaches that attempt to learn useful features by maximizing similarity between augmented versions of each input image or by speculatively picking negative samples, we instead also make use of the natural variation that occurs in image collections that are captured using static monitoring cameras. To achieve this, we exploit readily available context data that encodes information such as the spatial and temporal relationships between the input images. We are able to learn representations that are surprisingly effective for downstream supervised classification, by first identifying high probability positive pairs at training time, i.e. those images that are likely to depict the same visual concept. For the critical task of global biodiversity monitoring, this results in image features that can be adapted to challenging visual species classification tasks with limited human supervision. We present results on four different camera trap image collections, across three different families of self-supervised learning methods, and show that careful image selection at training time results in superior performance compared to existing baselines such as conventional self-supervised training and transfer learning.

</details>

### On Compositions of Transformations in Contrastive Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00944) · 📚 被引 37
- **作者**: Mandela Patrick, Yuki Markus Asano, Polina Kuznetsova, Ruth Fong, João F. Henriques, Geoffrey Zweig et al.
- **🏷️ 机构**: Facebook AI Research, University of Oxford,Visual Geometry Group
- **会议**: ICCV 2021

### Self-Supervised Real-to-Sim Scene Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01574) · 📚 被引 23
- **作者**: Aayush Prakash, Shoubhik Debnath, Jean-Francois Lafleche, Eric Cameracci, Gavriel State, Stan Birchfield et al.
- **🏷️ 机构**: NVIDIA
- **会议**: ICCV 2021

### Enhancing Self-supervised Video Representation Learning via Multi-level Feature Optimization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00789)
- **作者**: Rui Qian, Yuxi Li, Huabin Liu, John See, Shuangrui Ding, Xian Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Exploration methods based on pseudo-count of transitions or curiosity of dynamics have achieved promising results in solving reinforcement learning with sparse rewards. However, such methods are usually sensitive to environmental dynamics-irrelevant information, e.g., white-noise. To handle such dynamics-irrelevant information, we propose a Dynamic Bottleneck (DB) model, which attains a dynamics-relevant representation based on the information-bottleneck principle. Based on the DB model, we further propose DB-bonus, which encourages the agent to explore state-action pairs with high information gain. We establish theoretical connections between the proposed DB-bonus, the upper confidence bound (UCB) for linear case, and the visiting count for tabular case. We evaluate the proposed method on Atari suits with dynamics-irrelevant noises. Our experiments show that exploration with DB bonus outperforms several state-of-the-art exploration methods in noisy environments.

</details>

### The functional specialization of visual cortex emerges from training parallel pathways with self-supervised predictive learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/d384dec9f5f7a64a36b5c8f03b8a6d92-Abstract.html) · 📚 被引 30
- **作者**: Shahab Bakhtiari, Patrick J. Mineault, Timothy P. Lillicrap, Christopher C. Pack, Blake A. Richards
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### SEAL: Self-supervised Embodied Active Learning using Exploration and 3D Consistency.
- **链接**: [arXiv:2112.01001](https://arxiv.org/abs/2112.01001)
- **作者**: Devendra Singh Chaplot, Murtaza Dalal, Saurabh Gupta, Jitendra Malik, Ruslan Salakhutdinov
- **🏷️ 机构**: UC Berkeley
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we explore how we can build upon the data and models of Internet images and use them to adapt to robot vision without requiring any extra labels. We present a framework called Self-supervised Embodied Active Learning (SEAL). It utilizes perception models trained on internet images to learn an active exploration policy. The observations gathered by this exploration policy are labelled using 3D consistency and used to improve the perception model. We build and utilize 3D semantic maps to learn both action and perception in a completely self-supervised manner. The semantic map is used to compute an intrinsic motivation reward for training the exploration policy and for labelling the agent observations using spatio-temporal 3D consistency and label propagation. We demonstrate that the SEAL framework can be used to close the action-perception loop: it improves object detection and instance segmentation performance of a pretrained perception model by just moving around in training environments and the improved perception model can be used to improve Object Goal Navigation.

</details>

### Neural Analysis and Synthesis: Reconstructing Speech from Self-Supervised Representations.
- **链接**: [arXiv:2110.14513](https://arxiv.org/abs/2110.14513)
- **作者**: Hyeong-Seok Choi, Juheon Lee, Wansoo Kim, Jie Lee, Hoon Heo, Kyogu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a neural analysis and synthesis (NANSY) framework that can manipulate voice, pitch, and speed of an arbitrary speech signal. Most of the previous works have focused on using information bottleneck to disentangle analysis features for controllable synthesis, which usually results in poor reconstruction quality. We address this issue by proposing a novel training strategy based on information perturbation. The idea is to perturb information in the original input signal (e.g., formant, pitch, and frequency response), thereby letting synthesis networks selectively take essential attributes to reconstruct the input signal. Because NANSY does not need any bottleneck structures, it enjoys both high reconstruction quality and controllability. Furthermore, NANSY does not require any labels associated with speech data such as text and speaker information, but rather uses a new set of analysis features, i.e., wav2vec feature and newly proposed pitch feature, Yingram, which allows for fully self-supervised training. Taking advantage of fully self-supervised training, NANSY can be easily extended to a multilingual setting by simply training it with a multilingual dataset. The experiments show that NANSY can achieve significant improvement in performance in several applications such as zero-shot voice conversion, pitch shift, and time-scale modification.

</details>

### Revitalizing CNN Attention via Transformers in Self-Supervised Visual Representation Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/21be992eb8016e541a15953eee90760e-Abstract.html)
- **作者**: Chongjian Ge, Youwei Liang, Yibing Song, Jianbo Jiao, Jue Wang, Ping Luo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### There Is No Turning Back: A Self-Supervised Approach for Reversibility-Aware Reinforcement Learning.
- **链接**: [arXiv:2106.04480](https://arxiv.org/abs/2106.04480)
- **作者**: Nathan Grinsztajn, Johan Ferret, Olivier Pietquin, Philippe Preux, Matthieu Geist
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose to learn to distinguish reversible from irreversible actions for better informed decision-making in Reinforcement Learning (RL). From theoretical considerations, we show that approximate reversibility can be learned through a simple surrogate task: ranking randomly sampled trajectory events in chronological order. Intuitively, pairs of events that are always observed in the same order are likely to be separated by an irreversible sequence of actions. Conveniently, learning the temporal order of events can be done in a fully self-supervised way, which we use to estimate the reversibility of actions from experience, without any priors. We propose two different strategies that incorporate reversibility in RL agents, one strategy for exploration (RAE) and one strategy for control (RAC). We demonstrate the potential of reversibility-aware agents in several environments, including the challenging Sokoban game. In synthetic tasks, we show that we can learn control policies that never fail and reduce to zero the side-effects of interactions, even without access to the reward function.

</details>

### Self-Supervised Learning of Event-Based Optical Flow with Spiking Neural Networks.
- **链接**: [arXiv:2106.01862](https://arxiv.org/abs/2106.01862)
- **作者**: Jesse J. Hagenaars, Federico Paredes-Vallés, Guido de Croon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of neuromorphic computing promises extremely low-power and low-latency sensing and processing. Challenges in transferring learning algorithms from traditional artificial neural networks (ANNs) to spiking neural networks (SNNs) have so far prevented their application to large-scale, complex regression tasks. Furthermore, realizing a truly asynchronous and fully neuromorphic pipeline that maximally attains the abovementioned benefits involves rethinking the way in which this pipeline takes in and accumulates information. In the case of perception, spikes would be passed as-is and one-by-one between an event camera and an SNN, meaning all temporal integration of information must happen inside the network. In this article, we tackle these two problems. We focus on the complex task of learning to estimate optical flow from event-based camera inputs in a self-supervised manner, and modify the state-of-the-art ANN training pipeline to encode minimal temporal information in its inputs. Moreover, we reformulate the self-supervised loss function for event-based optical flow to improve its convexity. We perform experiments with various types of recurrent ANNs and SNNs using the proposed pipeline. Concerning SNNs, we investigate the effects of elements such as parameter initialization and optimization, surrogate gradient shape, and adaptive neuronal mechanisms. We find that initialization and surrogate gradient width play a crucial part in enabling learning with sparse inputs, while the inclusion of adaptivity and learnable neuronal parameters can improve performance. We show that the performance of the proposed ANNs and SNNs are on par with that of the current state-of-the-art ANNs trained in a self-supervised manner.

</details>

### Provable Guarantees for Self-Supervised Deep Learning with Spectral Contrastive Loss.
- **链接**: [arXiv:2106.04156](https://arxiv.org/abs/2106.04156)
- **作者**: Jeff Z. HaoChen, Colin Wei, Adrien Gaidon, Tengyu Ma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works in self-supervised learning have advanced the state-of-the-art by relying on the contrastive learning paradigm, which learns representations by pushing positive pairs, or similar examples from the same class, closer together while keeping negative pairs far apart. Despite the empirical successes, theoretical foundations are limited -- prior analyses assume conditional independence of the positive pairs given the same class label, but recent empirical applications use heavily correlated positive pairs (i.e., data augmentations of the same image). Our work analyzes contrastive learning without assuming conditional independence of positive pairs using a novel concept of the augmentation graph on data. Edges in this graph connect augmentations of the same data, and ground-truth classes naturally form connected sub-graphs. We propose a loss that performs spectral decomposition on the population augmentation graph and can be succinctly written as a contrastive learning objective on neural net representations. Minimizing this objective leads to features with provable accuracy guarantees under linear probe evaluation. By standard generalization bounds, these accuracy guarantees also hold when minimizing the training contrastive loss. Empirically, the features learned by our objective can match or outperform several strong baselines on benchmark vision datasets. In all, this work provides the first provable analysis for contrastive learning where guarantees for linear probe evaluation can apply to realistic empirical settings.

</details>

### Self-Supervised GANs with Label Augmentation.
- **链接**: [arXiv:2106.08601](https://arxiv.org/abs/2106.08601)
- **作者**: Liang Hou, Huawei Shen, Qi Cao, Xueqi Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, transformation-based self-supervised learning has been applied to generative adversarial networks (GANs) to mitigate catastrophic forgetting in the discriminator by introducing a stationary learning environment. However, the separate self-supervised tasks in existing self-supervised GANs cause a goal inconsistent with generative modeling due to the fact that their self-supervised classifiers are agnostic to the generator distribution. To address this problem, we propose a novel self-supervised GAN that unifies the GAN task with the self-supervised task by augmenting the GAN labels (real or fake) via self-supervision of data transformation. Specifically, the original discriminator and self-supervised classifier are unified into a label-augmented discriminator that predicts the augmented labels to be aware of both the generator distribution and the data distribution under every transformation, and then provide the discrepancy between them to optimize the generator. Theoretically, we prove that the optimal generator could converge to replicate the real data distribution. Empirically, we show that the proposed method significantly outperforms previous self-supervised and data augmentation GANs on both generative modeling and representation learning across benchmark datasets.

</details>

### Capturing implicit hierarchical structure in 3D biomedical images with self-supervised hyperbolic representations.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/291d43c696d8c3704cdbe0a72ade5f6c-Abstract.html)
- **作者**: Joy Hsu, Jeffrey Gu, Gong Her Wu, Wah Chiu, Serena Yeung
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### PLADE-Net: Towards Pixel-Level Accuracy for Self-Supervised Single-View Depth Estimation With Neural Positional Encoding and Distilled Matting Loss.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Gonzalez_PLADE-Net_Towards_Pixel-Level_Accuracy_for_Self-Supervised_Single-View_Depth_Estimation_With_CVPR_2021_paper.html) · 📚 被引 17
- **作者**: Juan Luis Gonzalez, Munchurl Kim
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology
- **会议**: CVPR 2021

### Safe Local Motion Planning With Self-Supervised Freespace Forecasting.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_Safe_Local_Motion_Planning_With_Self-Supervised_Freespace_Forecasting_CVPR_2021_paper.html) · 📚 被引 83
- **作者**: Peiyun Hu, Aaron Huang, John M. Dolan, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: CVPR 2021

### Self-Supervised 3D Mesh Reconstruction From Single Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_Self-Supervised_3D_Mesh_Reconstruction_From_Single_Images_CVPR_2021_paper.html) · 📚 被引 49
- **作者**: Tao Hu, Liwei Wang, Xiaogang Xu, Shu Liu, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: ICCV 2021

### Vi2CLR: Video and Image for Visual Contrastive Learning of Representation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00153)
- **作者**: Ali Diba, Vivek Sharma, Reza Safdari, Dariush Lotfi, M. Saquib Sarfraz, Rainer Stiefelhagen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### With a Little Help from My Friends: Nearest-Neighbor Contrastive Learning of Visual Representations.
- **链接**: [arXiv:2104.14548](https://arxiv.org/abs/2104.14548) · 📚 被引 332
- **作者**: Debidatta Dwibedi, Yusuf Aytar, Jonathan Tompson, Pierre Sermanet, Andrew Zisserman
- **🏷️ 机构**: Google Research, DeepMind
- **会议**: ICCV 2021

### The Way to my Heart is through Contrastive Learning: Remote Photoplethysmography from Unlabelled Video.
- **链接**: [arXiv:2111.09748](https://arxiv.org/abs/2111.09748) · 📚 被引 126
- **作者**: John Gideon, Simon Stent
- **🏷️ 机构**: Toyota Research Institute Cambridge,MA,USA
- **会议**: ICCV 2021

### Region-aware Contrastive Learning for Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01598) · 📚 被引 127
- **作者**: Hanzhe Hu, Jinshi Cui, Liwei Wang
- **🏷️ 机构**: Peking University,Key Laboratory of Machine Perception (MOE), School of EECS
- **会议**: ICCV 2021

### A Broad Study on the Transferability of Visual Representations with Contrastive Learning.
- **链接**: [arXiv:2103.13517](https://arxiv.org/abs/2103.13517) · 📚 被引 49
- **作者**: Ashraful Islam, Chun-Fu Chen, Rameswar Panda, Leonid Karlinsky, Richard J. Radke, Rogério Feris
- **🏷️ 机构**: Rensselaer Polytechnic Institute, MIT-IBM Watson AI Lab, IBM Research
- **会议**: ICCV 2021

### Contrasting Contrastive Self-Supervised Representation Learning Pipelines.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00980) · 📚 被引 21
- **作者**: Klemen Kotar, Gabriel Ilharco, Ludwig Schmidt, Kiana Ehsani, Roozbeh Mottaghi
- **🏷️ 机构**: PRIOR @ Allen Institute for AI, University of Washington
- **会议**: ICCV 2021

### Attentive and Contrastive Learning for Joint Depth and Motion Field Estimation.
- **链接**: [arXiv:2110.06853](https://arxiv.org/abs/2110.06853) · 📚 被引 31
- **作者**: Seokju Lee, François Rameau, Fei Pan, In So Kweon
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST)
- **会议**: ICCV 2021

### Motion-Focused Contrastive Learning of Video Representations*.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00211)
- **作者**: Rui Li, Yiheng Zhang, Zhaofan Qiu, Ting Yao, Dong Liu, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Self-Supervised Video Representation Learning with Meta-Contrastive Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00813)
- **作者**: Yuanze Lin, Xun Guo, Yan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer has been widely used for self-supervised pre-training in Natural Language Processing (NLP) and achieved great success. However, it has not been fully explored in visual self-supervised learning. Meanwhile, previous methods only consider the high-level feature and learning representation from a global perspective, which may fail to transfer to the downstream dense prediction tasks focusing on local features. In this paper, we present a novel Masked Self-supervised Transformer approach named MST, which can explicitly capture the local context of an image while preserving the global semantic information. Specifically, inspired by the Masked Language Modeling (MLM) in NLP, we propose a masked token strategy based on the multi-head self-attention map, which dynamically masks some tokens of local patches without damaging the crucial structure for self-supervised learning. More importantly, the masked tokens together with the remaining tokens are further recovered by a global image decoder, which preserves the spatial information of the image and is more friendly to the downstream dense prediction tasks. The experiments on multiple datasets demonstrate the effectiveness and generality of the proposed method. For instance, MST achieves Top-1 accuracy of 76.9% with DeiT-S only using 300-epoch pre-training by linear evaluation, which outperforms supervised methods with the same epoch by 0.4% and its comparable variant DINO by 1.0\%. For dense prediction tasks, MST also achieves 42.7% mAP on MS COCO object detection and 74.04% mIoU on Cityscapes segmentation only with 100-epoch pre-training.

</details>

### Self-Supervised Learning with Kernel Dependence Maximization.
- **链接**: [arXiv:2106.08320](https://arxiv.org/abs/2106.08320) · [代码](https://github.com/deepmind/ssl_hsic)
- **作者**: Yazhe Li, Roman Pogodin, Danica J. Sutherland, Arthur Gretton
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We approach self-supervised learning of image representations from a statistical dependence perspective, proposing Self-Supervised Learning with the Hilbert-Schmidt Independence Criterion (SSL-HSIC). SSL-HSIC maximizes dependence between representations of transformations of an image and the image identity, while minimizing the kernelized variance of those representations. This framework yields a new understanding of InfoNCE, a variational lower bound on the mutual information (MI) between different transformations. While the MI itself is known to have pathologies which can result in learning meaningless representations, its bound is much better behaved: we show that it implicitly approximates SSL-HSIC (with a slightly different regularizer). Our approach also gives us insight into BYOL, a negative-free SSL method, since SSL-HSIC similarly learns local neighborhoods of samples. SSL-HSIC allows us to directly optimize statistical dependence in time linear in the batch size, without restrictive data assumptions or indirect mutual information estimators. Trained with or without a target network, SSL-HSIC matches the current state-of-the-art for standard linear evaluation on ImageNet, semi-supervised learning and transfer to other classification and vision tasks such as semantic segmentation, depth estimation and object recognition. Code is available at https://github.com/deepmind/ssl_hsic .

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Drop, Swap, and Generate: A Self-Supervised Approach for Generating Neural Activity.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/58182b82110146887c02dbd78719e3d5-Abstract.html) · 📚 被引 8
- **作者**: Ran Liu, Mehdi Azabou, Max Dabagia, Chi-Heng Lin, Mohammad Gheshlaghi Azar, Keith B. Hengen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### TTT++: When Does Self-Supervised Test-Time Training Fail or Thrive?
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b618c3210e934362ac261db280128c22-Abstract.html)
- **作者**: Yuejiang Liu, Parth Kothari, Bastien van Delft, Baptiste Bellot-Gurlet, Taylor Mordan, Alexandre Alahi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Understanding Negative Samples in Instance Discriminative Self-supervised Representation Learning.
- **链接**: [arXiv:2102.06866](https://arxiv.org/abs/2102.06866)
- **作者**: Kento Nozawa, Issei Sato
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Instance discriminative self-supervised representation learning has been attracted attention thanks to its unsupervised nature and informative feature representation for downstream tasks. In practice, it commonly uses a larger number of negative samples than the number of supervised classes. However, there is an inconsistency in the existing analysis; theoretically, a large number of negative samples degrade classification performance on a downstream supervised task, while empirically, they improve the performance. We provide a novel framework to analyze this empirical result regarding negative samples using the coupon collector's problem. Our bound can implicitly incorporate the supervised loss of the downstream task in the self-supervised loss by increasing the number of negative samples. We confirm that our proposed analysis holds on real-world benchmark datasets.

</details>

### ISD: Self-Supervised Learning by Iterative Similarity Distillation.
- **链接**: [arXiv:2012.09259](https://arxiv.org/abs/2012.09259) · [代码](https://github.com/UMBCvision/ISD)
- **作者**: Ajinkya Tejankar, Soroush Abbasi Koohpayegani, Vipin Pillai, Paolo Favaro, Hamed Pirsiavash
- **🏷️ 机构**: University of Maryland,Baltimore County, University of Bern
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has been shown to learn useful and information-preserving representations. Neural Networks (NNs) are widely applied, yet their weight space is still not fully understood. Therefore, we propose to use SSL to learn hyper-representations of the weights of populations of NNs. To that end, we introduce domain specific data augmentations and an adapted attention architecture. Our empirical evaluation demonstrates that self-supervised representation learning in this domain is able to recover diverse NN model characteristics. Further, we show that the proposed learned representations outperform prior work for predicting hyper-parameters, test accuracy, and generalization gap as well as transfer to out-of-distribution settings.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared to feature point detection and description, detecting and matching line segments offer additional challenges. Yet, line features represent a promising complement to points for multi-view tasks. Lines are indeed well-defined by the image gradient, frequently appear even in poorly textured areas and offer robust structural cues. We thus hereby introduce the first joint detection and description of line segments in a single deep network. Thanks to a self-supervised training, our method does not require any annotated line labels and can therefore generalize to any dataset. Our detector offers repeatable and accurate localization of line segments in images, departing from the wireframe parsing approach. Leveraging the recent progresses in descriptor learning, our proposed line descriptor is highly discriminative, while remaining robust to viewpoint changes and occlusions. We evaluate our approach against previous line detection and description methods on several multi-view datasets created with homographic warps as well as real-world viewpoint changes. Our full pipeline yields higher repeatability, localization accuracy and matching metrics, and thus represents a first step to bridge the gap with learned feature points methods. Code and trained weights are available at https://github.com/cvg/SOLD2.

</details>

> Self-supervised learning holds promise in leveraging large amounts of unlabeled data, however much of its progress has thus far been limited to highly curated pre-training data such as ImageNet. We explore the effects of contrastive learning from larger, less-curated image datasets such as YFCC, and find there is indeed a large difference in the resulting representation quality. We hypothesize that this curation gap is due to a shift in the distribution of image classes -- which is more diverse and heavy-tailed -- resulting in less relevant negative samples to learn from. We test this hypothesis with a new approach, Divide and Contrast (DnC), which alternates between contrastive learning and clustering-based hard negative mining. When pretrained on less curated datasets, DnC greatly improves the performance of self-supervised learning on downstream tasks, while remaining competitive with the current state-of-the-art on curated datasets.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a new generative model for 3D garment deformations that enables us to learn, for the first time, a data-driven method for virtual try-on that effectively addresses garment-body collisions. In contrast to existing methods that require an undesirable postprocessing step to fix garment-body interpenetrations at test time, our approach directly outputs 3D garment configurations that do not collide with the underlying body. Key to our success is a new canonical space for garments that removes pose-and-shape deformations already captured by a new diffused human body model, which extrapolates body surface properties such as skinning weights and blendshapes to any 3D point. We leverage this representation to train a generative model with a novel self-supervised collision term that learns to reliably solve garment-body interpenetrations. We extensively evaluate and compare our results with recently proposed data-driven methods, and show that our method is the first to successfully address garment-body contact in unseen body shapes and motions, without compromising realism and detail.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in self-supervised learning (SSL) have largely closed the gap with supervised ImageNet pretraining. Despite their success these methods have been primarily applied to unlabeled ImageNet images, and show marginal gains when trained on larger sets of uncurated images. We hypothesize that current SSL methods perform best on iconic images, and struggle on complex scene images with many objects. Analyzing contrastive SSL methods shows that they have poor visual grounding and receive poor supervisory signal when trained on scene images. We propose Contrastive Attention-Supervised Tuning(CAST) to overcome these limitations. CAST uses unsupervised saliency maps to intelligently sample crops, and to provide grounding supervision via a Grad-CAM attention loss. Experiments on COCO show that CAST significantly improves the features learned by SSL methods on scene images, and further experiments show that CAST-trained models are more robust to changes in backgrounds.

</details>

### Self-Supervised 3D Face Reconstruction via Conditional Estimation.
- **链接**: [arXiv:2110.04800](https://arxiv.org/abs/2110.04800) · 📚 被引 26
- **作者**: Yandong Wen, Weiyang Liu, Bhiksha Raj, Rita Singh
- **🏷️ 机构**: Carnegie Mellon University, University of Cambridge
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous studies dominantly target at self-supervised learning on real-valued networks and have achieved many promising results. However, on the more challenging binary neural networks (BNNs), this task has not yet been fully explored in the community. In this paper, we focus on this more difficult scenario: learning networks where both weights and activations are binary, meanwhile, without any human annotated labels. We observe that the commonly used contrastive objective is not satisfying on BNNs for competitive accuracy, since the backbone network contains relatively limited capacity and representation ability. Hence instead of directly applying existing self-supervised methods, which cause a severe decline in performance, we present a novel guided learning paradigm from real-valued to distill binary networks on the final prediction distribution, to minimize the loss and obtain desirable accuracy. Our proposed method can boost the simple contrastive learning baseline by an absolute gain of 5.5~15% on BNNs. We further reveal that it is difficult for BNNs to recover the similar predictive distributions as real-valued models when training without labels. Thus, how to calibrate them is key to address the degradation in performance. Extensive experiments are conducted on the large-scale ImageNet and downstream datasets. Our method achieves substantial improvement over the simple contrastive learning baseline, and is even comparable to many mainstream supervised BNN methods. Code is available at https://github.com/szq0214/S2-BNN.

</details>

</details>

### Self-Supervised Representation Learning from Flow Equivariance.
- **链接**: [arXiv:2101.06553](https://arxiv.org/abs/2101.06553) · 📚 被引 19
- **作者**: Yuwen Xiong, Mengye Ren, Wenyuan Zeng, Raquel Urtasun Waabi
- **🏷️ 机构**: University of Toronto
- **会议**: ICCV 2021

### Dense Contrastive Learning for Self-Supervised Visual Pre-Training.
- **链接**: [arXiv:2011.09157](https://arxiv.org/abs/2011.09157) · 📚 被引 570
- **作者**: Xinlong Wang, Rufeng Zhang, Chunhua Shen, Tao Kong, Lei Li
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To date, most existing self-supervised learning methods are designed and optimized for image classification. These pre-trained models can be sub-optimal for dense prediction tasks due to the discrepancy between image-level prediction and pixel-level prediction. To fill this gap, we aim to design an effective, dense self-supervised learning method that directly works at the level of pixels (or local features) by taking into account the correspondence between local features. We present dense contrastive learning, which implements self-supervised learning by optimizing a pairwise contrastive (dis)similarity loss at the pixel level between two views of input images. Compared to the baseline method MoCo-v2, our method introduces negligible computation overhead (only <1% slower), but demonstrates consistently superior performance when transferring to downstream dense prediction tasks including object detection, semantic segmentation and instance segmentation; and outperforms the state-of-the-art methods by a large margin. Specifically, over the strong MoCo-v2 baseline, our method achieves significant improvements of 2.0% AP on PASCAL VOC object detection, 1.1% AP on COCO object detection, 0.9% AP on COCO instance segmentation, 3.0% mIoU on PASCAL VOC semantic segmentation and 1.8% mIoU on Cityscapes semantic segmentation. Code is available at: https://git.io/AdelaiDet

</details>

### Instance Localization for Self-Supervised Detection Pretraining.
- **链接**: [arXiv:2102.08318](https://arxiv.org/abs/2102.08318) · 📚 被引 103
- **作者**: Ceyuan Yang, Zhirong Wu, Bolei Zhou, Stephen Lin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prior research on self-supervised learning has led to considerable progress on image classification, but often with degraded transfer performance on object detection. The objective of this paper is to advance self-supervised pretrained models specifically for object detection. Based on the inherent difference between classification and detection, we propose a new self-supervised pretext task, called instance localization. Image instances are pasted at various locations and scales onto background images. The pretext task is to predict the instance category given the composited images as well as the foreground bounding boxes. We show that integration of bounding boxes into pretraining promotes better task alignment and architecture alignment for transfer learning. In addition, we propose an augmentation method on the bounding boxes to further enhance the feature alignment. As a result, our model becomes weaker at Imagenet semantic classification but stronger at image patch localization, with an overall stronger pretrained model for object detection. Experimental results demonstrate that our approach yields state-of-the-art transfer learning results for object detection on PASCAL VOC and MSCOCO.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Artists and video game designers often construct 2D animations using libraries of sprites -- textured patches of objects and characters. We propose a deep learning approach that decomposes sprite-based video animations into a disentangled representation of recurring graphic elements in a self-supervised manner. By jointly learning a dictionary of possibly transparent patches and training a network that places them onto a canvas, we deconstruct sprite-based content into a sparse, consistent, and explicit representation that can be easily used in downstream tasks, like editing or analysis. Our framework offers a promising approach for discovering recurring visual patterns in image collections without supervision.

</details>

> Learning a good representation for space-time correspondence is the key for various computer vision tasks, including tracking object bounding boxes and performing video object pixel segmentation. To learn generalizable representation for correspondence in large-scale, a variety of self-supervised pretext tasks are proposed to explicitly perform object-level or patch-level similarity learning. Instead of following the previous literature, we propose to learn correspondence using Video Frame-level Similarity (VFS) learning, i.e, simply learning from comparing video frames. Our work is inspired by the recent success in image-level contrastive learning and similarity learning for visual recognition. Our hypothesis is that if the representation is good for recognition, it requires the convolutional features to find correspondence between similar objects or parts. Our experiments show surprising results that VFS surpasses state-of-the-art self-supervised approaches for both OTB visual object tracking and DAVIS video object segmentation. We perform detailed analysis on what matters in VFS and reveals new properties on image and frame level similarity learning. Project page with code is available at https://jerryxu.net/VFS

### Contrastive Learning Based Hybrid Networks for Long-Tailed Image Classification.
- **链接**: [arXiv:2103.14267](https://arxiv.org/abs/2103.14267) · 📚 被引 291
- **作者**: Peng Wang, Kai Han, Xiu-Shen Wei, Lei Zhang, Lei Wang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the task of spatially localizing narrated interactions in videos. Key to our approach is the ability to learn to spatially localize interactions with self-supervision on a large corpus of videos with accompanying transcribed narrations. To achieve this goal, we propose a multilayer cross-modal attention network that enables effective optimization of a contrastive loss during training. We introduce a divided strategy that alternates between computing inter- and intra-modal attention across the visual and natural language modalities, which allows effective training via directly contrasting the two modalities' representations. We demonstrate the effectiveness of our approach by self-training on the HowTo100M instructional video dataset and evaluating on a newly collected dataset of localized described interactions in the YouCook2 dataset. We show that our approach outperforms alternative baselines, including shallow co-attention and full cross-modal attention. We also apply our approach to grounding phrases in images with weak supervision on Flickr30K and show that stacking multiple attention layers is effective and, when combined with a word-to-region loss, achieves state of the art on recall-at-one and pointing hand accuracies.

</details>

</details>

### Self-supervised Adversarial Robustness for the Low-label, High-data Regime.
- **链接**: [出版页](https://openreview.net/forum?id=bgQek2O63w)
- **作者**: Sven Gowal, Po-Sen Huang, Aäron van den Oord, Timothy A. Mann, Pushmeet Kohli
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning has been shown to be very effective in learning useful representations, and yet much of the success is achieved in data types such as images, audio, and text. The success is mainly enabled by taking advantage of spatial, temporal, or semantic structure in the data through augmentation. However, such structure may not exist in tabular datasets commonly used in fields such as healthcare, making it difficult to design an effective augmentation method, and hindering a similar progress in tabular data setting. In this paper, we introduce a new framework, Subsetting features of Tabular data (SubTab), that turns the task of learning from tabular data into a multi-view representation learning problem by dividing the input features to multiple subsets. We argue that reconstructing the data from the subset of its features rather than its corrupted version in an autoencoder setting can better capture its underlying latent representation. In this framework, the joint representation can be expressed as the aggregate of latent variables of the subsets at test time, which we refer to as collaborative inference. Our experiments show that the SubTab achieves the state of the art (SOTA) performance of 98.31% on MNIST in tabular setting, on par with CNN-based SOTA models, and surpasses existing baselines on three other real-world datasets by a significant margin.

</details>

> In most real world scenarios, a policy trained by reinforcement learning in one environment needs to be deployed in another, potentially quite different environment. However, generalization across different environments is known to be hard. A natural solution would be to keep training after deployment in the new environment, but this cannot be done if the new environment offers no reward signal. Our work explores the use of self-supervision to allow the policy to continue training after deployment without using any rewards. While previous methods explicitly anticipate changes in the new environment, we assume no prior knowledge of those changes yet still obtain significant improvements. Empirical evaluations are performed on diverse simulation environments from DeepMind Control suite and ViZDoom, as well as real robotic manipulation tasks in continuously changing environments, taking observations from an uncalibrated camera. Our method improves generalization in 31 out of 36 environments across various tasks and outperforms domain randomization on a majority of environments.

</details>

### On Self-Supervised Image Representations for GAN Evaluation.
- **链接**: [出版页](https://openreview.net/forum?id=NeRdBeTionN)
- **作者**: Stanislav Morozov, Andrey Voynov, Artem Babenko
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A good visual representation is an inference map from observations (images) to features (vectors) that faithfully reflects the hidden modularized generative factors (semantics). In this paper, we formulate the notion of "good" representation from a group-theoretic view using Higgins' definition of disentangled representation, and show that existing Self-Supervised Learning (SSL) only disentangles simple augmentation features such as rotation and colorization, thus unable to modularize the remaining semantics. To break the limitation, we propose an iterative SSL algorithm: Iterative Partition-based Invariant Risk Minimization (IP-IRM), which successfully grounds the abstract semantics and the group acting on them into concrete contrastive learning. At each iteration, IP-IRM first partitions the training samples into two subsets that correspond to an entangled group element. Then, it minimizes a subset-invariant contrastive loss, where the invariance guarantees to disentangle the group element. We prove that IP-IRM converges to a fully disentangled representation and show its effectiveness on various benchmarks. Codes are available at https://github.com/Wangt-CN/IP-IRM.

</details>

### Graph Adversarial Self-Supervised Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/7d3010c11d08cf990b7614d2c2ca9098-Abstract.html)
- **作者**: Longqi Yang, Liangliang Zhang, Wenjing Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning (CSL) has attracted increasing attention for model pre-training via unlabeled data. The resulted CSL models provide instance-discriminative visual features that are uniformly scattered in the feature space. During deployment, the common practice is to directly fine-tune CSL models with cross-entropy, which however may not be the best strategy in practice. Although cross-entropy tends to separate inter-class features, the resulting models still have limited capability for reducing intra-class feature scattering that exists in CSL models. In this paper, we investigate whether applying contrastive learning to fine-tuning would bring further benefits, and analytically find that optimizing the contrastive loss benefits both discriminative representation learning and model optimization during fine-tuning. Inspired by these findings, we propose Contrast-regularized tuning (Core-tuning), a new approach for fine-tuning CSL models. Instead of simply adding the contrastive loss to the objective of fine-tuning, Core-tuning further applies a novel hard pair mining strategy for more effective contrastive fine-tuning, as well as smoothing the decision boundary to better exploit the learned discriminative feature space. Extensive experiments on image classification and semantic segmentation verify the effectiveness of Core-tuning.

</details>

### Motif-based Graph Self-Supervised Learning for Molecular Property Prediction.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/85267d349a5e647ff0a9edcb5ffd1e02-Abstract.html)
- **作者**: Zaixi Zhang, Qi Liu, Hao Wang, Chengqiang Lu, Chee-Kong Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We ask the following question: what training information is required to design an effective outlier/out-of-distribution (OOD) detector, i.e., detecting samples that lie far away from the training distribution? Since unlabeled data is easily accessible for many applications, the most compelling approach is to develop detectors based on only unlabeled in-distribution data. However, we observe that most existing detectors based on unlabeled data perform poorly, often equivalent to a random prediction. In contrast, existing state-of-the-art OOD detectors achieve impressive performance but require access to fine-grained data labels for supervised training. We propose SSD, an outlier detector based on only unlabeled in-distribution data. We use self-supervised representation learning followed by a Mahalanobis distance based detection in the feature space. We demonstrate that SSD outperforms most existing detectors based on unlabeled data by a large margin. Additionally, SSD even achieves performance on par, and sometimes even better, with supervised training based detectors. Finally, we expand our detection framework with two key extensions. First, we formulate few-shot OOD detection, in which the detector has access to only one to five samples from each class of the targeted OOD dataset. Second, we extend our framework to incorporate training data labels, if available. We find that our novel detection framework based on SSD displays enhanced performance with these extensions, and achieves state-of-the-art performance. Our code is publicly available at https://github.com/inspire-group/SSD.

</details>

### Online Adversarial Purification based on Self-supervised Learning.
- **链接**: [出版页](https://openreview.net/forum?id=_i3ASPp12WS)
- **作者**: Changhao Shi, Chester Holtz, Gal Mishne
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised Learning (SSL) including the mainstream contrastive learning has achieved great success in learning visual representations without data annotations. However, most of methods mainly focus on the instance level information (\ie, the different augmented images of the same instance should have the same feature or cluster into the same class), but there is a lack of attention on the relationships between different instances. In this paper, we introduced a novel SSL paradigm, which we term as relational self-supervised learning (ReSSL) framework that learns representations by modeling the relationship between different instances. Specifically, our proposed method employs sharpened distribution of pairwise similarities among different instances as \textit{relation} metric, which is thus utilized to match the feature embeddings of different augmentations. Moreover, to boost the performance, we argue that weak augmentations matter to represent a more reliable relation, and leverage momentum strategy for practical efficiency. Experimental results show that our proposed ReSSL significantly outperforms the previous state-of-the-art algorithms in terms of both performance and training efficiency. Code is available at \url{https://github.com/KyleZheng1997/ReSSL}.

</details>

> A generalist robot must be able to complete a variety of tasks in its environment. One appealing way to specify each task is in terms of a goal observation. However, learning goal-reaching policies with reinforcement learning remains a challenging problem, particularly when hand-engineered reward functions are not available. Learned dynamics models are a promising approach for learning about the environment without rewards or task-directed data, but planning to reach goals with such a model requires a notion of functional similarity between observations and goal states. We present a self-supervised method for model-based visual goal reaching, which uses both a visual dynamics model as well as a dynamical distance function learned using model-free reinforcement learning. Our approach learns entirely using offline, unlabeled data, making it practical to scale to large and diverse datasets. In our experiments, we find that our method can successfully learn models that perform a variety of tasks at test-time, moving objects amid distractors with a simulated robotic arm and even learning to open and close a drawer using a real-world robot. In comparisons, we find that this approach substantially outperforms both model-free and model-based prior methods. Videos and visualizations are available here: http://sites.google.com/berkeley.edu/mbold.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning (CL) can learn generalizable feature representations and achieve the state-of-the-art performance of downstream tasks by finetuning a linear classifier on top of it. However, as adversarial robustness becomes vital in image classification, it remains unclear whether or not CL is able to preserve robustness to downstream tasks. The main challenge is that in the self-supervised pretraining + supervised finetuning paradigm, adversarial robustness is easily forgotten due to a learning task mismatch from pretraining to finetuning. We call such a challenge 'cross-task robustness transferability'. To address the above problem, in this paper we revisit and advance CL principles through the lens of robustness enhancement. We show that (1) the design of contrastive views matters: High-frequency components of images are beneficial to improving model robustness; (2) Augmenting CL with pseudo-supervision stimulus (e.g., resorting to feature clustering) helps preserve robustness without forgetting. Equipped with our new designs, we propose AdvCL, a novel adversarial contrastive pretraining framework. We show that AdvCL is able to enhance cross-task robustness transferability without loss of model accuracy and finetuning efficiency. With a thorough experimental study, we demonstrate that AdvCL outperforms the state-of-the-art self-supervised robust learning methods across multiple datasets (CIFAR-10, CIFAR-100, and STL-10) and finetuning schemes (linear evaluation and full model finetuning).

</details>

### Robust Contrastive Learning Using Negative Samples with Diminished Semantics.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/e5afb0f2dbc6d39b312d7406054cb4c6-Abstract.html)
- **作者**: Songwei Ge, Shlok Mishra, Chun-Liang Li, Haohan Wang, David Jacobs
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Model Adaptation: Historical Contrastive Learning for Unsupervised Domain Adaptation without Source Data.
- **链接**: [arXiv:2110.03374](https://arxiv.org/abs/2110.03374)
- **作者**: Jiaxing Huang, Dayan Guan, Aoran Xiao, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised domain adaptation aims to align a labeled source domain and an unlabeled target domain, but it requires to access the source data which often raises concerns in data privacy, data portability and data transmission efficiency. We study unsupervised model adaptation (UMA), or called Unsupervised Domain Adaptation without Source Data, an alternative setting that aims to adapt source-trained models towards target distributions without accessing source data. To this end, we design an innovative historical contrastive learning (HCL) technique that exploits historical source hypothesis to make up for the absence of source data in UMA. HCL addresses the UMA challenge from two perspectives. First, it introduces historical contrastive instance discrimination (HCID) that learns from target samples by contrasting their embeddings which are generated by the currently adapted model and the historical models. With the historical models, HCID encourages UMA to learn instance-discriminative target representations while preserving the source hypothesis. Second, it introduces historical contrastive category discrimination (HCCD) that pseudo-labels target samples to learn category-discriminative target representations. Specifically, HCCD re-weights pseudo labels according to their prediction consistency across the current and historical models. Extensive experiments show that HCL outperforms and state-of-the-art methods consistently across a variety of visual tasks and setups.

</details>

### Compressed Video Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/7647966b7343c29048673252e490f736-Abstract.html)
- **作者**: Yuqi Huo, Mingyu Ding, Haoyu Lu, Nanyi Fei, Zhiwu Lu, Ji-Rong Wen et al.
- **🏷️ 机构**: Renmin University
- **会议**: NeurIPS 2021

### Task-Adaptive Neural Network Search with Meta-Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b20bb95ab626d93fd976af958fbc61ba-Abstract.html)
- **作者**: Wonyong Jeong, Hayeon Lee, Geon Park, Eunyoung Hyung, Jinheon Baek, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Improving Contrastive Learning on Imbalanced Data via Open-World Sampling.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/2f37d10131f2a483a8dd005b3d14b0d9-Abstract.html)
- **作者**: Ziyu Jiang, Tianlong Chen, Ting Chen, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Disentangled Contrastive Learning on Graphs.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/b6cda17abb967ed28ec9610137aa45f7-Abstract.html)
- **作者**: Haoyang Li, Xin Wang, Ziwei Zhang, Zehuan Yuan, Hang Li, Wenwu Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Contrastive Learning of Global and Local Video Representations.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/38ef4b66cb25e92abe4d594acb841471-Abstract.html)
- **作者**: Shuang Ma, Zhaoyang Zeng, Daniel McDuff, Yale Song
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Object-aware Contrastive Learning for Debiased Scene Representation.
- **链接**: [arXiv:2108.00049](https://arxiv.org/abs/2108.00049)
- **作者**: Sangwoo Mo, Hyunwoo Kang, Kihyuk Sohn, Chun-Liang Li, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive self-supervised learning has shown impressive results in learning visual representations from unlabeled images by enforcing invariance against different data augmentations. However, the learned representations are often contextually biased to the spurious scene correlations of different objects or object and background, which may harm their generalization on the downstream tasks. To tackle the issue, we develop a novel object-aware contrastive learning framework that first (a) localizes objects in a self-supervised manner and then (b) debias scene correlations via appropriate data augmentations considering the inferred object locations. For (a), we propose the contrastive class activation map (ContraCAM), which finds the most discriminative regions (e.g., objects) in the image compared to the other images using the contrastively trained models. We further improve the ContraCAM to detect multiple objects and entire shapes via an iterative refinement procedure. For (b), we introduce two data augmentations based on ContraCAM, object-aware random crop and background mixup, which reduce contextual and background biases during contrastive self-supervised learning, respectively. Our experiments demonstrate the effectiveness of our representation learning framework, particularly when trained under multi-object images or evaluated under the background (and distribution) shifted images.

</details>

### Contrastive Learning for Neural Topic Model.
- **链接**: [arXiv:2110.12764](https://arxiv.org/abs/2110.12764)
- **作者**: Thong Nguyen, Anh Tuan Luu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent empirical studies show that adversarial topic models (ATM) can successfully capture semantic patterns of the document by differentiating a document with another dissimilar sample. However, utilizing that discriminative-generative architecture has two important drawbacks: (1) the architecture does not relate similar documents, which has the same document-word distribution of salient words; (2) it restricts the ability to integrate external information, such as sentiments of the document, which has been shown to benefit the training of neural topic model. To address those issues, we revisit the adversarial topic architecture in the viewpoint of mathematical analysis, propose a novel approach to re-formulate discriminative goal as an optimization problem, and design a novel sampling method which facilitates the integration of external variables. The reformulation encourages the model to incorporate the relations among similar samples and enforces the constraint on the similarity among dissimilar ones; while the sampling method, which is based on the internal input and reconstructed output, helps inform the model of salient words contributing to the main topic. Experimental results show that our framework outperforms other state-of-the-art neural topic models in three common benchmark datasets that belong to various domains, vocabulary sizes, and document lengths in terms of topic coherence.

</details>

### Can contrastive learning avoid shortcut solutions?
- **链接**: [arXiv:2106.11230](https://arxiv.org/abs/2106.11230) · [代码](https://github.com/joshr17/IFM)
- **作者**: Joshua Robinson, Li Sun, Ke Yu, Kayhan Batmanghelich, Stefanie Jegelka, Suvrit Sra
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The generalization of representations learned via contrastive learning depends crucially on what features of the data are extracted. However, we observe that the contrastive loss does not always sufficiently guide which features are extracted, a behavior that can negatively impact the performance on downstream tasks via "shortcuts", i.e., by inadvertently suppressing important predictive features. We find that feature extraction is influenced by the difficulty of the so-called instance discrimination task (i.e., the task of discriminating pairs of similar points from pairs of dissimilar ones). Although harder pairs improve the representation of some features, the improvement comes at the cost of suppressing previously well represented features. In response, we propose implicit feature modification (IFM), a method for altering positive and negative samples in order to guide contrastive models towards capturing a wider variety of predictive features. Empirically, we observe that IFM reduces feature suppression, and as a result improves performance on vision and medical imaging tasks. The code is available at: \url{https://github.com/joshr17/IFM}.

</details>

### CLDA: Contrastive Learning for Semi-Supervised Domain Adaptation.
- **链接**: [arXiv:2107.00085](https://arxiv.org/abs/2107.00085)
- **作者**: Ankit Singh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Domain Adaptation (UDA) aims to align the labeled source distribution with the unlabeled target distribution to obtain domain invariant predictive models. However, the application of well-known UDA approaches does not generalize well in Semi-Supervised Domain Adaptation (SSDA) scenarios where few labeled samples from the target domain are available. In this paper, we propose a simple Contrastive Learning framework for semi-supervised Domain Adaptation (CLDA) that attempts to bridge the intra-domain gap between the labeled and unlabeled target distributions and inter-domain gap between source and unlabeled target distribution in SSDA. We suggest employing class-wise contrastive learning to reduce the inter-domain gap and instance-level contrastive alignment between the original (input image) and strongly augmented unlabeled target images to minimize the intra-domain discrepancy. We have shown empirically that both of these modules complement each other to achieve superior performance. Experiments on three well-known domain adaptation benchmark datasets namely DomainNet, Office-Home, and Office31 demonstrate the effectiveness of our approach. CLDA achieves state-of-the-art results on all the above datasets.

</details>

### Adversarial Graph Augmentation to Improve Graph Contrastive Learning.
- **链接**: [arXiv:2106.05819](https://arxiv.org/abs/2106.05819)
- **作者**: Susheel Suresh, Pan Li, Cong Hao, Jennifer Neville
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning of graph neural networks (GNN) is in great need because of the widespread label scarcity issue in real-world graph/network data. Graph contrastive learning (GCL), by training GNNs to maximize the correspondence between the representations of the same graph in its different augmented forms, may yield robust and transferable GNNs even without using labels. However, GNNs trained by traditional GCL often risk capturing redundant graph features and thus may be brittle and provide sub-par performance in downstream tasks. Here, we propose a novel principle, termed adversarial-GCL (AD-GCL), which enables GNNs to avoid capturing redundant information during the training by optimizing adversarial graph augmentation strategies used in GCL. We pair AD-GCL with theoretical explanations and design a practical instantiation based on trainable edge-dropping graph augmentation. We experimentally validate AD-GCL by comparing with the state-of-the-art GCL methods and achieve performance gains of up-to $14\%$ in unsupervised, $6\%$ in transfer, and $3\%$ in semi-supervised learning settings overall with 18 different benchmark datasets for the tasks of molecule property regression and classification, and social network classification.

</details>

### Directed Graph Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/a3048e47310d6efaa4b1eaf55227bc92-Abstract.html)
- **作者**: Zekun Tong, Yuxuan Liang, Henghui Ding, Yongxing Dai, Xinke Li, Changhu Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### InfoGCL: Information-Aware Graph Contrastive Learning.
- **链接**: [arXiv:2110.15438](https://arxiv.org/abs/2110.15438)
- **作者**: Dongkuan Xu, Wei Cheng, Dongsheng Luo, Haifeng Chen, Xiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Various graph contrastive learning models have been proposed to improve the performance of learning tasks on graph datasets in recent years. While effective and prevalent, these models are usually carefully customized. In particular, although all recent researches create two contrastive views, they differ greatly in view augmentations, architectures, and objectives. It remains an open question how to build your graph contrastive learning model from scratch for particular graph learning tasks and datasets. In this work, we aim to fill this gap by studying how graph information is transformed and transferred during the contrastive learning process and proposing an information-aware graph contrastive learning framework called InfoGCL. The key point of this framework is to follow the Information Bottleneck principle to reduce the mutual information between contrastive parts while keeping task-relevant information intact at both the levels of the individual module and the entire framework so that the information loss during graph representation learning can be minimized. We show for the first time that all recent graph contrastive learning methods can be unified by our framework. We empirically validate our theoretical analysis on both node and graph classification benchmark datasets, and demonstrate that our algorithm significantly outperforms the state-of-the-arts.

</details>

## 跨领域论文（完整笔记在其他领域）

- Exploring Geometry-aware Contrast and Clustering Harmonization for Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Self-Supervised Object Detection via Generative Image Synthesis. → [object-detection](../object-detection/Guideline%202021.md)
- DetCo: Unsupervised Contrastive Learning for Object Detection. → [object-detection](../object-detection/Guideline%202021.md)
- Revealing the Reciprocal Relations between Self-Supervised Stereo and Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- MonoIndoor: Towards Good Practice of Self-Supervised Monocular Depth Estimation for Indoor Environments. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Fine-grained Semantics-aware Representation Enhancement for Self-supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-supervised Monocular Depth Estimation for All Day Images using Domain Separation. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Excavating the Potential Capacity of Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Regularizing Nighttime Weirdness: Efficient Self-supervised Monocular Depth Estimation in the Dark. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- MultiSiam: Self-supervised Multi-instance Siamese Representation Learning for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
- Multimodal Clustering Networks for Self-supervised Learning from Unlabeled Videos. → [multimodal](../multimodal/Guideline%202021.md)
- Domain Adaptive Semantic Segmentation with Self-Supervised Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- BossNAS: Exploring Hybrid CNN-transformers with Block-wisely Self-supervised Neural Architecture Search. → [neural-architecture-search](../neural-architecture-search/Guideline%202021.md)
- Digging into Uncertainty in Self-supervised Multi-view Stereo. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
