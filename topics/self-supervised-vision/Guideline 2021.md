# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning methods have significantly narrowed the gap between supervised and unsupervised learning on computer vision tasks. In this paper, we explore their application to geo-located datasets, e.g. remote sensing, where unlabeled data is often abundant but labeled data is scarce. We first show that due to their different characteristics, a non-trivial gap persists between contrastive and supervised learning on standard benchmarks. To close the gap, we propose novel training methods that exploit the spatio-temporal structure of remote sensing data. We leverage spatially aligned images over time to construct temporal positive pairs in contrastive learning and geo-location to design pre-text tasks. Our experiments show that our proposed method closes the gap between contrastive and supervised learning on image classification, object detection and semantic segmentation for remote sensing. Moreover, we demonstrate that the proposed method can also be applied to geo-tagged ImageNet images, improving downstream performance on various tasks. Project Webpage can be found at this link geography-aware-ssl.github.io.

</details>

### Big Self-Supervised Models Advance Medical Image Classification.
- **链接**: [arXiv:2101.05224](https://arxiv.org/abs/2101.05224) · 📚 被引 574
- **作者**: Shekoofeh Azizi, Basil Mustafa, Fiona Ryan, Zachary Beaver, Jan Freyberg, Jonathan Deaton et al.
- **🏷️ 机构**: Google Research and Health
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pretraining followed by supervised fine-tuning has seen success in image recognition, especially when labeled examples are scarce, but has received limited attention in medical image analysis. This paper studies the effectiveness of self-supervised learning as a pretraining strategy for medical image classification. We conduct experiments on two distinct tasks: dermatology skin condition classification from digital camera images and multi-label chest X-ray classification, and demonstrate that self-supervised learning on ImageNet, followed by additional self-supervised learning on unlabeled domain-specific medical images significantly improves the accuracy of medical image classifiers. We introduce a novel Multi-Instance Contrastive Learning (MICLe) method that uses multiple images of the underlying pathology per patient case, when available, to construct more informative positive pairs for self-supervised learning. Combining our contributions, we achieve an improvement of 6.7% in top-1 accuracy and an improvement of 1.1% in mean AUC on dermatology and chest X-ray classification respectively, outperforming strong supervised baselines pretrained on ImageNet. In addition, we show that big self-supervised models are robust to distribution shift and can learn efficiently with a small number of labeled medical images.

</details>

### Self-supervised Transfer Learning for Hand Mesh Recovery from Binocular Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01142) · 📚 被引 10
- **作者**: Zheng Chen, Sihan Wang, Yi Sun, Xiaohong Ma
- **🏷️ 机构**: Dalian University of Technology,China
- **会议**: ICCV 2021

### Towards High Fidelity Monocular Face Reconstruction with Rich Reflectance using Self-supervised Learning and Ray Tracing.
- **链接**: [arXiv:2103.15432](https://arxiv.org/abs/2103.15432) · 📚 被引 53
- **作者**: Abdallah Dib, Cédric Thébault, Junghyun Ahn, Philippe-Henri Gosselin, Christian Theobalt, Louis Chevallier
- **🏷️ 机构**: InterDigital R&#x0026;I, Max-Planck-Institute for Informatics
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robust face reconstruction from monocular image in general lighting conditions is challenging. Methods combining deep neural network encoders with differentiable rendering have opened up the path for very fast monocular reconstruction of geometry, lighting and reflectance. They can also be trained in self-supervised manner for increased robustness and better generalization. However, their differentiable rasterization based image formation models, as well as underlying scene parameterization, limit them to Lambertian face reflectance and to poor shape details. More recently, ray tracing was introduced for monocular face reconstruction within a classic optimization-based framework and enables state-of-the art results. However optimization-based approaches are inherently slow and lack robustness. In this paper, we build our work on the aforementioned approaches and propose a new method that greatly improves reconstruction quality and robustness in general scenes. We achieve this by combining a CNN encoder with a differentiable ray tracer, which enables us to base the reconstruction on much more advanced personalized diffuse and specular albedos, a more sophisticated illumination model and a plausible representation of self-shadows. This enables to take a big leap forward in reconstruction quality of shape, appearance and lighting even in scenes with difficult illumination. With consistent face attributes reconstruction, our method leads to practical applications such as relighting and self-shadows removal. Compared to state-of-the-art methods, our results show improved accuracy and validity of the approach.

</details>

### Contrast and Order Representations for Video Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00784) · 📚 被引 47
- **作者**: Kai Hu, Jie Shao, Yuan Liu, Bhiksha Raj, Marios Savvides, Zhiqiang Shen
- **🏷️ 机构**: Carnegie Mellon University, Fudan University, ByteDance
- **会议**: ICCV 2021

### On Feature Decorrelation in Self-Supervised Learning.
- **链接**: [arXiv:2105.00470](https://arxiv.org/abs/2105.00470)
- **作者**: Tianyu Hua, Wenxiao Wang, Zihui Xue, Sucheng Ren, Yue Wang, Hang Zhao
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

### Self-supervised Product Quantization for Deep Unsupervised Image Retrieval.
- **链接**: [arXiv:2109.02244](https://arxiv.org/abs/2109.02244) · 📚 被引 70
- **作者**: Young Kyun Jang, Nam Ik Cho
- **🏷️ 机构**: Seoul National University,Department of ECE, INMC,Seoul,Korea
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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
- **会议**: ICCV 2021

### Self-supervised Domain Adaptation for Forgery Localization of JPEG Compressed Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01476) · 📚 被引 33
- **作者**: Yuan Rao, Jiangqun Ni
- **🏷️ 机构**: Sun Yat-Sen University,School of Electronics and Information Technology,Guangzhou,China, Sun Yat-Sen University,School of Computer Science and Engineering,Guangzhou,China
- **会议**: ICCV 2021

### Broaden Your Views for Self-Supervised Video Learning.
- **链接**: [arXiv:2103.16559](https://arxiv.org/abs/2103.16559) · 📚 被引 71
- **作者**: Adrià Recasens, Pauline Luc, Jean-Baptiste Alayrac, Luyu Wang, Florian Strub, Corentin Tallec et al.
- **🏷️ 机构**: DeepMind
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most successful self-supervised learning methods are trained to align the representations of two independent views from the data. State-of-the-art methods in video are inspired by image techniques, where these two views are similarly extracted by cropping and augmenting the resulting crop. However, these methods miss a crucial element in the video domain: time. We introduce BraVe, a self-supervised learning framework for video. In BraVe, one of the views has access to a narrow temporal window of the video while the other view has a broad access to the video content. Our models learn to generalise from the narrow view to the general content of the video. Furthermore, BraVe processes the views with different backbones, enabling the use of alternative augmentations or modalities into the broad view such as optical flow, randomly convolved RGB frames, audio or their combinations. We demonstrate that BraVe achieves state-of-the-art results in self-supervised representation learning on standard video and audio classification benchmarks including UCF101, HMDB51, Kinetics, ESC-50 and AudioSet.

</details>

### Self-Supervised 3D Hand Pose Estimation from monocular RGB via Contrastive Learning.
- **链接**: [arXiv:2106.05953](https://arxiv.org/abs/2106.05953) · 📚 被引 72
- **作者**: Adrian Spurr, Aneesh Dahiya, Xi Wang, Xucong Zhang, Otmar Hilliges
- **🏷️ 机构**: ETH Zurich,Department of Computer Science,Switzerland
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Encouraged by the success of contrastive learning on image classification tasks, we propose a new self-supervised method for the structured regression task of 3D hand pose estimation. Contrastive learning makes use of unlabeled data for the purpose of representation learning via a loss formulation that encourages the learned feature representations to be invariant under any image transformation. For 3D hand pose estimation, it too is desirable to have invariance to appearance transformation such as color jitter. However, the task requires equivariance under affine transformations, such as rotation and translation. To address this issue, we propose an equivariant contrastive objective and demonstrate its effectiveness in the context of 3D hand pose estimation. We experimentally investigate the impact of invariant and equivariant contrastive objectives and show that learning equivariant features leads to better representations for the task of 3D hand pose estimation. Furthermore, we show that standard ResNets with sufficient depth, trained on additional unlabeled data, attain improvements of up to 14.5% in PA-EPE on FreiHAND and thus achieves state-of-the-art performance without any task specific, specialized architectures. Code and models are available at https://ait.ethz.ch/projects/2021/PeCLR/

</details>

### Self-supervised 3D Skeleton Action Representation Learning with Motion Consistency and Continuity.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01308) · 📚 被引 65
- **作者**: Yukun Su, Guosheng Lin, Qingyao Wu
- **🏷️ 机构**: South China University of Technology,School of Software and Engineering, Nanyang Technological University,School of Computer Science and Engineering
- **会议**: ICCV 2021

### ISD: Self-Supervised Learning by Iterative Similarity Distillation.
- **链接**: [arXiv:2012.09259](https://arxiv.org/abs/2012.09259) · [代码](https://github.com/UMBCvision/ISD)
- **作者**: Ajinkya Tejankar, Soroush Abbasi Koohpayegani, Vipin Pillai, Paolo Favaro, Hamed Pirsiavash
- **🏷️ 机构**: University of Maryland,Baltimore County, University of Bern
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, contrastive learning has achieved great results in self-supervised learning, where the main idea is to push two augmentations of an image (positive pairs) closer compared to other random images (negative pairs). We argue that not all random images are equal. Hence, we introduce a self supervised learning algorithm where we use a soft similarity for the negative images rather than a binary distinction between positive and negative pairs. We iteratively distill a slowly evolving teacher model to the student model by capturing the similarity of a query image to some random images and transferring that knowledge to the student. We argue that our method is less constrained compared to recent contrastive learning methods, so it can learn better features. Specifically, our method should handle unbalanced and unlabeled data better than existing contrastive learning methods, because the randomly chosen negative set might include many samples that are semantically similar to the query image. In this case, our method labels them as highly similar while standard contrastive methods label them as negative pairs. Our method achieves comparable results to the state-of-the-art models. We also show that our method performs better in the settings where the unlabeled data is unbalanced. Our code is available here: https://github.com/UMBCvision/ISD.

</details>

### Divide and Contrast: Self-supervised Learning from Uncurated Data.
- **链接**: [arXiv:2105.08054](https://arxiv.org/abs/2105.08054) · 📚 被引 34
- **作者**: Yonglong Tian, Olivier J. Hénaff, Aäron van den Oord
- **🏷️ 机构**: MIT, DeepMind
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning holds promise in leveraging large amounts of unlabeled data, however much of its progress has thus far been limited to highly curated pre-training data such as ImageNet. We explore the effects of contrastive learning from larger, less-curated image datasets such as YFCC, and find there is indeed a large difference in the resulting representation quality. We hypothesize that this curation gap is due to a shift in the distribution of image classes -- which is more diverse and heavy-tailed -- resulting in less relevant negative samples to learn from. We test this hypothesis with a new approach, Divide and Contrast (DnC), which alternates between contrastive learning and clustering-based hard negative mining. When pretrained on less curated datasets, DnC greatly improves the performance of self-supervised learning on downstream tasks, while remaining competitive with the current state-of-the-art on curated datasets.

</details>

### Solving Inefficiency of Self-supervised Representation Learning.
- **链接**: [arXiv:2104.08760](https://arxiv.org/abs/2104.08760) · [代码](https://github.com/wanggrun/triplet) · 📚 被引 55
- **作者**: Guangrun Wang, Keze Wang, Guangcong Wang, Philip H. S. Torr, Liang Lin
- **🏷️ 机构**: Sun Yat-sen University, DarkMatter AI Research, Nanyang Technological University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (especially contrastive learning) has attracted great interest due to its huge potential in learning discriminative representations in an unsupervised manner. Despite the acknowledged successes, existing contrastive learning methods suffer from very low learning efficiency, e.g., taking about ten times more training epochs than supervised learning for comparable recognition accuracy. In this paper, we reveal two contradictory phenomena in contrastive learning that we call under-clustering and over-clustering problems, which are major obstacles to learning efficiency. Under-clustering means that the model cannot efficiently learn to discover the dissimilarity between inter-class samples when the negative sample pairs for contrastive learning are insufficient to differentiate all the actual object classes. Over-clustering implies that the model cannot efficiently learn features from excessive negative sample pairs, forcing the model to over-cluster samples of the same actual classes into different clusters. To simultaneously overcome these two problems, we propose a novel self-supervised learning framework using a truncated triplet loss. Precisely, we employ a triplet loss tending to maximize the relative distance between the positive pair and negative pairs to address the under-clustering problem; and we construct the negative pair by selecting a negative sample deputy from all negative samples to avoid the over-clustering problem, guaranteed by the Bernoulli Distribution model. We extensively evaluate our framework in several large-scale benchmarks (e.g., ImageNet, SYSU-30k, and COCO). The results demonstrate our model's superiority (e.g., the learning efficiency) over the latest state-of-the-art methods by a clear margin. Codes available at: https://github.com/wanggrun/triplet .

</details>

### Self-Supervised 3D Face Reconstruction via Conditional Estimation.
- **链接**: [arXiv:2110.04800](https://arxiv.org/abs/2110.04800) · 📚 被引 26
- **作者**: Yandong Wen, Weiyang Liu, Bhiksha Raj, Rita Singh
- **🏷️ 机构**: Carnegie Mellon University, University of Cambridge
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a conditional estimation (CEST) framework to learn 3D facial parameters from 2D single-view images by self-supervised training from videos. CEST is based on the process of analysis by synthesis, where the 3D facial parameters (shape, reflectance, viewpoint, and illumination) are estimated from the face image, and then recombined to reconstruct the 2D face image. In order to learn semantically meaningful 3D facial parameters without explicit access to their labels, CEST couples the estimation of different 3D facial parameters by taking their statistical dependency into account. Specifically, the estimation of any 3D facial parameter is not only conditioned on the given image, but also on the facial parameters that have already been derived. Moreover, the reflectance symmetry and consistency among the video frames are adopted to improve the disentanglement of facial parameters. Together with a novel strategy for incorporating the reflectance symmetry and consistency, CEST can be efficiently trained with in-the-wild video clips. Both qualitative and quantitative experiments demonstrate the effectiveness of CEST.

</details>

### Self-Supervised Representation Learning from Flow Equivariance.
- **链接**: [arXiv:2101.06553](https://arxiv.org/abs/2101.06553) · 📚 被引 19
- **作者**: Yuwen Xiong, Mengye Ren, Wenyuan Zeng, Raquel Urtasun Waabi
- **🏷️ 机构**: University of Toronto
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised representation learning is able to learn semantically meaningful features; however, much of its recent success relies on multiple crops of an image with very few objects. Instead of learning view-invariant representation from simple images, humans learn representations in a complex world with changing scenes by observing object movement, deformation, pose variation, and ego motion. Motivated by this ability, we present a new self-supervised learning representation framework that can be directly deployed on a video stream of complex scenes with many moving objects. Our framework features a simple flow equivariance objective that encourages the network to predict the features of another frame by applying a flow transformation to the features of the current frame. Our representations, learned from high-resolution raw video, can be readily used for downstream tasks on static images. Readout experiments on challenging semantic segmentation, instance segmentation, and object detection benchmarks show that we are able to outperform representations obtained from previous state-of-the-art methods including SimCLR and BYOL.

</details>

### Virtual Multi-Modality Self-Supervised Foreground Matting for Human-Object Interaction.
- **链接**: [arXiv:2110.03278](https://arxiv.org/abs/2110.03278) · 📚 被引 5
- **作者**: Bo Xu, Han Huang, Cheng Lu, Ziwen Li, Yandong Guo
- **🏷️ 机构**: OPPO Research Institute, Xmotors
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing human matting algorithms tried to separate pure human-only foreground from the background. In this paper, we propose a Virtual Multi-modality Foreground Matting (VMFM) method to learn human-object interactive foreground (human and objects interacted with him or her) from a raw RGB image. The VMFM method requires no additional inputs, e.g. trimap or known background. We reformulate foreground matting as a self-supervised multi-modality problem: factor each input image into estimated depth map, segmentation mask, and interaction heatmap using three auto-encoders. In order to fully utilize the characteristics of each modality, we first train a dual encoder-to-decoder network to estimate the same alpha matte. Then we introduce a self-supervised method: Complementary Learning(CL) to predict deviation probability map and exchange reliable gradients across modalities without label. We conducted extensive experiments to analyze the effectiveness of each modality and the significance of different components in complementary learning. We demonstrate that our model outperforms the state-of-the-art methods.

</details>

### Rethinking Self-supervised Correspondence Learning: A Video Frame-level Similarity Perspective.
- **链接**: [arXiv:2103.17263](https://arxiv.org/abs/2103.17263) · 📚 被引 65
- **作者**: Jiarui Xu, Xiaolong Wang
- **🏷️ 机构**: UC San Diego
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning a good representation for space-time correspondence is the key for various computer vision tasks, including tracking object bounding boxes and performing video object pixel segmentation. To learn generalizable representation for correspondence in large-scale, a variety of self-supervised pretext tasks are proposed to explicitly perform object-level or patch-level similarity learning. Instead of following the previous literature, we propose to learn correspondence using Video Frame-level Similarity (VFS) learning, i.e, simply learning from comparing video frames. Our work is inspired by the recent success in image-level contrastive learning and similarity learning for visual recognition. Our hypothesis is that if the representation is good for recognition, it requires the convolutional features to find correspondence between similar objects or parts. Our experiments show surprising results that VFS surpasses state-of-the-art self-supervised approaches for both OTB visual object tracking and DAVIS video object segmentation. We perform detailed analysis on what matters in VFS and reveals new properties on image and frame level similarity learning. Project page with code is available at https://jerryxu.net/VFS

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
