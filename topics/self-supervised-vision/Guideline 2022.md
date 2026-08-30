# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 79 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Self-Supervised Global-Local Structure Modeling for Point Cloud Domain Adaptation with Reliable Voted Pseudo Labels. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00627) · 📚 被引 60
- **作者**: Hehe Fan, Xiaojun Chang, Wanyue Zhang, Yi Cheng, Ying Sun, Mohan S. Kankanhalli
- **🏷️ 机构**: School of Computing, National University of Singapore, ReLER Lab, AAII, University of Technology,Sydney, Max Planck Institute for Informatics
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对点云领域自适应中标签稀缺和域间差异导致性能下降的问题，提出了一种自监督全局-局部结构建模方法。②方法通过全局和局部结构建模来学习域不变特征，并利用可靠的投票伪标签进行训练，以增强跨域泛化能力。③相比现有域自适应方法，该方法无需目标域标签，且通过自监督方式缓解了伪标签噪声问题。④实验表明该方法在多个点云域自适应基准上取得了优于现有方法的性能。
- **摘要（英）**: This paper addresses point cloud domain adaptation by proposing a self-supervised global-local structure modeling approach with reliable voted pseudo labels. It learns domain-invariant features and mitigates pseudo-label noise without target labels, achieving superior performance on multiple benchmarks.
- **核心贡献**: 提出了一种结合全局-局部结构建模和可靠投票伪标签的自监督点云域自适应方法。
- **创新点**: 利用自监督全局-局部结构建模增强域不变性，并设计投票机制提高伪标签可靠性。
- **结果**: 在多个点云域自适应任务上取得了优于现有方法的性能。

### RigidFlow: Self-Supervised Scene Flow Learning on Point Clouds by Local Rigidity Prior. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01645) · 📚 被引 48
- **作者**: Ruibo Li, Chi Zhang, Guosheng Lin, Zhe Wang, Chunhua Shen
- **🏷️ 机构**: Nanyang Technological University,S-Lab for Advanced Intelligence, School of Computer Science and Engineering, Nanyang Technological University, SenseTime Research
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对点云场景流估计依赖大量标注数据且泛化性差的问题，提出了一种基于局部刚性先验的自监督学习方法。②方法利用局部刚性假设，通过自监督方式训练场景流估计网络，无需真实流标注。③相比有监督方法，该方法在跨域场景下具有更好的泛化能力，且避免了昂贵的标注成本。④实验在多个点云场景流数据集上验证了方法的有效性，性能接近甚至超越有监督方法。
- **摘要（英）**: This paper proposes RigidFlow, a self-supervised scene flow learning method on point clouds using a local rigidity prior. It eliminates the need for ground-truth flow labels and improves cross-domain generalization, achieving performance comparable to supervised methods on multiple datasets.
- **核心贡献**: 提出了一种基于局部刚性先验的自监督点云场景流学习方法。
- **创新点**: 将局部刚性假设引入自监督训练，有效替代了昂贵的流标注。
- **结果**: 在多个数据集上性能接近甚至超越有监督方法。

### Self-Supervised Arbitrary-Scale Point Clouds Upsampling via Implicit Neural Representation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2204.08196](https://arxiv.org/abs/2204.08196) · 📚 被引 63
- **作者**: Wenbo Zhao, Xianming Liu, Zhiwei Zhong, Junjun Jiang, Wei Gao, Ge Li et al.
- **🏷️ 机构**: Harbin Institute of Technology, Peking University Shenzhen Graduate School, Tsinghua University
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对点云上采样任务依赖成对监督数据和不同尺度需独立训练网络的问题，提出了一种自监督且支持任意尺度放大的方法。②方法将上采样视为在隐式曲面上寻找种子点的最近投影点，定义两个隐式神经函数分别估计投影方向和距离，并通过两个前置任务进行自监督训练。③相比现有监督方法，该方法无需成对数据，且单一网络即可处理任意放大倍数。④实验表明该方法在多个数据集上取得了与监督方法相当甚至更优的性能。
- **摘要（英）**: This paper proposes a self-supervised arbitrary-scale point cloud upsampling method via implicit neural representation, formulating upsampling as finding nearest projection points on an implicit surface. It eliminates paired supervision and supports flexible magnification with a single network, achieving competitive or better performance than supervised methods.
- **核心贡献**: 提出了一种自监督且支持任意尺度放大的点云上采样方法。
- **创新点**: 利用隐式神经表示和双前置任务实现自监督上采样，无需成对数据。
- **结果**: 在多个数据集上性能与监督方法相当或更优。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point clouds upsampling is a challenging issue to generate dense and uniform point clouds from the given sparse input. Most existing methods either take the end-to-end supervised learning based manner, where large amounts of pairs of sparse input and dense ground-truth are exploited as supervision information; or treat up-scaling of different scale factors as independent tasks, and have to build multiple networks to handle upsampling with varying factors. In this paper, we propose a novel approach that achieves self-supervised and magnification-flexible point clouds upsampling simultaneously. We formulate point clouds upsampling as the task of seeking nearest projection points on the implicit surface for seed points. To this end, we define two implicit neural functions to estimate projection direction and distance respectively, which can be trained by two pretext learning tasks. Experimental results demonstrate that our self-supervised learning based scheme achieves competitive or even better performance than supervised learning based state-of-the-art methods. The source code is publicly available at https://github.com/xnowbzhao/sapcu.

</details>

### Vision-Language Pre-Training with Triple Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01522) · 📚 被引 258
- **作者**: Jinyu Yang, Jiali Duan, Son Tran, Yi Xu, Sampath Chanda, Liqun Chen et al.
- **🏷️ 机构**: University Of Texas at Arlington, Amazon
- **会议**: CVPR 2022

### Scaling Vision Transformers to Gigapixel Images via Hierarchical Self-Supervised Learning.
- **链接**: [arXiv:2206.02647](https://arxiv.org/abs/2206.02647) · 📚 被引 531
- **作者**: Richard J. Chen, Chengkuan Chen, Yicong Li, Tiffany Y. Chen, Andrew D. Trister, Rahul G. Krishnan et al.
- **🏷️ 机构**: Harvard, BWH, Broad Institute, Bill &#x0026; Melinda Gates Foundation, University of Toronto
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) and their multi-scale and hierarchical variations have been successful at capturing image representations but their use has been generally studied for low-resolution images (e.g. - 256x256, 384384). For gigapixel whole-slide imaging (WSI) in computational pathology, WSIs can be as large as 150000x150000 pixels at 20X magnification and exhibit a hierarchical structure of visual tokens across varying resolutions: from 16x16 images capture spatial patterns among cells, to 4096x4096 images characterizing interactions within the tissue microenvironment. We introduce a new ViT architecture called the Hierarchical Image Pyramid Transformer (HIPT), which leverages the natural hierarchical structure inherent in WSIs using two levels of self-supervised learning to learn high-resolution image representations. HIPT is pretrained across 33 cancer types using 10,678 gigapixel WSIs, 408,218 4096x4096 images, and 104M 256x256 images. We benchmark HIPT representations on 9 slide-level tasks, and demonstrate that: 1) HIPT with hierarchical pretraining outperforms current state-of-the-art methods for cancer subtyping and survival prediction, 2) self-supervised ViTs are able to model important inductive biases about the hierarchical structure of phenotypes in the tumor microenvironment.

</details>

### Patch-level Representation Learning for Self-supervised Vision Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00817) · 📚 被引 57
- **作者**: Sukmin Yun, Hankook Lee, Jaehyung Kim, Jinwoo Shin
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST)
- **会议**: CVPR 2022

### Self-supervised Image-specific Prototype Exploration for Weakly Supervised Semantic Segmentation.
- **链接**: [arXiv:2203.02909](https://arxiv.org/abs/2203.02909) · [代码](https://github.com/chenqi1126/SIPE) · 📚 被引 190
- **作者**: Qi Chen, Lingxiao Yang, Jianhuang Lai, Xiaohua Xie
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-Sen University,China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly Supervised Semantic Segmentation (WSSS) based on image-level labels has attracted much attention due to low annotation costs. Existing methods often rely on Class Activation Mapping (CAM) that measures the correlation between image pixels and classifier weight. However, the classifier focuses only on the discriminative regions while ignoring other useful information in each image, resulting in incomplete localization maps. To address this issue, we propose a Self-supervised Image-specific Prototype Exploration (SIPE) that consists of an Image-specific Prototype Exploration (IPE) and a General-Specific Consistency (GSC) loss. Specifically, IPE tailors prototypes for every image to capture complete regions, formed our Image-Specific CAM (IS-CAM), which is realized by two sequential steps. In addition, GSC is proposed to construct the consistency of general CAM and our specific IS-CAM, which further optimizes the feature representation and empowers a self-correction ability of prototype exploration. Extensive experiments are conducted on PASCAL VOC 2012 and MS COCO 2014 segmentation benchmark and results show our SIPE achieves new state-of-the-art performance using only image-level labels. The code is available at https://github.com/chenqi1126/SIPE.

</details>

### Masked Feature Prediction for Self-Supervised Visual Pre-Training.
- **链接**: [arXiv:2112.09133](https://arxiv.org/abs/2112.09133) · 📚 被引 500
- **作者**: Chen Wei, Haoqi Fan, Saining Xie, Chao-Yuan Wu, Alan L. Yuille, Christoph Feichtenhofer
- **🏷️ 机构**: Facebook AI Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Masked Feature Prediction (MaskFeat) for self-supervised pre-training of video models. Our approach first randomly masks out a portion of the input sequence and then predicts the feature of the masked regions. We study five different types of features and find Histograms of Oriented Gradients (HOG), a hand-crafted feature descriptor, works particularly well in terms of both performance and efficiency. We observe that the local contrast normalization in HOG is essential for good results, which is in line with earlier work using HOG for visual recognition. Our approach can learn abundant visual knowledge and drive large-scale Transformer-based models. Without using extra model weights or supervision, MaskFeat pre-trained on unlabeled videos achieves unprecedented results of 86.7% with MViT-L on Kinetics-400, 88.3% on Kinetics-600, 80.4% on Kinetics-700, 39.8 mAP on AVA, and 75.0% on SSv2. MaskFeat further generalizes to image input, which can be interpreted as a video with a single frame and obtains competitive results on ImageNet.

</details>

### Cross-Architecture Self-supervised Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01867)
- **作者**: Sheng Guo, Zihua Xiong, Yujie Zhong, Limin Wang, Xiaobo Guo, Bing Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Directional Self-supervised Learning for Heavy Image Augmentations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01619) · 📚 被引 17
- **作者**: Yalong Bai, Yifan Yang, Wei Zhang, Tao Mei
- **🏷️ 机构**: JD Explore Academy, Peking University
- **会议**: CVPR 2022

### DATA: Domain-Aware and Task-Aware Self-supervised Learning.
- **链接**: [arXiv:2203.09041](https://arxiv.org/abs/2203.09041) · [代码](https://github.com/GAIA-vision/GAIA-ssl) · 📚 被引 9
- **作者**: Qing Chang, Junran Peng, Lingxi Xie, Jiajun Sun, Haoran Yin, Qi Tian et al.
- **🏷️ 机构**: University of Chinese Academy of Sciences, Huawei Inc.
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The paradigm of training models on massive data without label through self-supervised learning (SSL) and finetuning on many downstream tasks has become a trend recently. However, due to the high training costs and the unconsciousness of downstream usages, most self-supervised learning methods lack the capability to correspond to the diversities of downstream scenarios, as there are various data domains, different vision tasks and latency constraints on models. Neural architecture search (NAS) is one universally acknowledged fashion to conquer the issues above, but applying NAS on SSL seems impossible as there is no label or metric provided for judging model selection. In this paper, we present DATA, a simple yet effective NAS approach specialized for SSL that provides Domain-Aware and Task-Aware pre-training. Specifically, we (i) train a supernet which could be deemed as a set of millions of networks covering a wide range of model scales without any label, (ii) propose a flexible searching mechanism compatible with SSL that enables finding networks of different computation costs, for various downstream vision tasks and data domains without explicit metric provided. Instantiated With MoCo v2, our method achieves promising results across a wide range of computation costs on downstream tasks, including image classification, object detection and semantic segmentation. DATA is orthogonal to most existing SSL methods and endows them the ability of customization on downstream needs. Extensive experiments on other SSL methods demonstrate the generalizability of the proposed method. Code is released at https://github.com/GAIA-vision/GAIA-ssl

</details>

### Knowledge-Driven Self-Supervised Representation Learning for Facial Action Unit Recognition. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01977) · 📚 被引 41
- **作者**: Yanan Chang, Shangfei Wang
- **🏷️ 机构**: University of Science and Technology of China,Hefei,Anhui,China
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对面部动作单元（AU）识别中标注成本高和类不平衡问题，提出了一种知识驱动的自监督表征学习方法。②方法利用AU之间的先验知识（如共现关系）设计自监督任务，以学习更具判别性的表征。③相比通用自监督方法，该方法结合了领域知识，更适应AU识别的特定需求。④实验在多个AU识别基准上验证了方法的有效性，性能优于现有自监督基线。
- **摘要（英）**: This paper proposes a knowledge-driven self-supervised representation learning method for facial action unit recognition, leveraging prior knowledge of AU co-occurrence to design pretext tasks. It improves discriminative representation and outperforms generic self-supervised baselines on multiple benchmarks.
- **核心贡献**: 提出了一种知识驱动的自监督AU识别方法，利用AU共现先验设计预训练任务。
- **创新点**: 将AU领域知识引入自监督学习，增强表征的判别性。
- **结果**: 在多个AU识别基准上优于现有自监督方法。

### Self-Supervised Image Representation Learning with Geometric Set Consistency.
- **链接**: [arXiv:2203.15361](https://arxiv.org/abs/2203.15361) · 📚 被引 9
- **作者**: Nenglun Chen, Lei Chu, Hao Pan, Yan Lu, Wenping Wang
- **🏷️ 机构**: The University of Hong Kong, Microsoft Research Asia, Texas A&#x0026;M University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a method for self-supervised image representation learning under the guidance of 3D geometric consistency. Our intuition is that 3D geometric consistency priors such as smooth regions and surface discontinuities may imply consistent semantics or object boundaries, and can act as strong cues to guide the learning of 2D image representations without semantic labels. Specifically, we introduce 3D geometric consistency into a contrastive learning framework to enforce the feature consistency within image views. We propose to use geometric consistency sets as constraints and adapt the InfoNCE loss accordingly. We show that our learned image representations are general. By fine-tuning our pre-trained representations for various 2D image-based downstream tasks, including semantic segmentation, object detection, and instance segmentation on real-world indoor scene datasets, we achieve superior performance compared with state-of-the-art methods.

</details>

### Neural Shape Mating: Self-Supervised Object Assembly with Adversarial Shape Priors.
- **链接**: [arXiv:2205.14886](https://arxiv.org/abs/2205.14886) · 📚 被引 34
- **作者**: Yun-Chun Chen, Haoda Li, Dylan Turpin, Alec Jacobson, Animesh Garg
- **🏷️ 机构**: University of Toronto
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning to autonomously assemble shapes is a crucial skill for many robotic applications. While the majority of existing part assembly methods focus on correctly posing semantic parts to recreate a whole object, we interpret assembly more literally: as mating geometric parts together to achieve a snug fit. By focusing on shape alignment rather than semantic cues, we can achieve across-category generalization. In this paper, we introduce a novel task, pairwise 3D geometric shape mating, and propose Neural Shape Mating (NSM) to tackle this problem. Given the point clouds of two object parts of an unknown category, NSM learns to reason about the fit of the two parts and predict a pair of 3D poses that tightly mate them together. We couple the training of NSM with an implicit shape reconstruction task to make NSM more robust to imperfect point cloud observations. To train NSM, we present a self-supervised data collection pipeline that generates pairwise shape mating data with ground truth by randomly cutting an object mesh into two parts, resulting in a dataset that consists of 200K shape mating pairs from numerous object meshes with diverse cut types. We train NSM on the collected dataset and compare it with several point cloud registration methods and one part assembly baseline. Extensive experimental results and ablation studies under various settings demonstrate the effectiveness of the proposed algorithm. Additional material is available at: https://neural-shape-mating.github.io/

</details>

### Self-supervised Learning of Adversarial Example: Towards Good Generalizations for Deepfake Detection.
- **链接**: [arXiv:2203.12208](https://arxiv.org/abs/2203.12208) · [代码](https://github.com/liangchen527/SLADD) · 📚 被引 288
- **作者**: Liang Chen, Yong Zhang, Yibing Song, Lingqiao Liu, Jue Wang
- **🏷️ 机构**: The University of Adelaide, Tencent AI Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies in deepfake detection have yielded promising results when the training and testing face forgeries are from the same dataset. However, the problem remains challenging when one tries to generalize the detector to forgeries created by unseen methods in the training dataset. This work addresses the generalizable deepfake detection from a simple principle: a generalizable representation should be sensitive to diverse types of forgeries. Following this principle, we propose to enrich the "diversity" of forgeries by synthesizing augmented forgeries with a pool of forgery configurations and strengthen the "sensitivity" to the forgeries by enforcing the model to predict the forgery configurations. To effectively explore the large forgery augmentation space, we further propose to use the adversarial training strategy to dynamically synthesize the most challenging forgeries to the current model. Through extensive experiments, we show that the proposed strategies are surprisingly effective (see Figure 1), and they could achieve superior performance than the current state-of-the-art methods. Code is available at \url{https://github.com/liangchen527/SLADD}.

</details>

### SPAct: Self-supervised Privacy Preservation for Action Recognition. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2203.15205](https://arxiv.org/abs/2203.15205) · 📚 被引 66
- **作者**: Ishan Rajendrakumar Dave, Chen Chen, Mubarak Shah
- **🏷️ 机构**: Center for Research in Computer Vision, University of Central Florida,Orlando,USA
- **会议**: CVPR 2022
- **摘要（中）**: ①针对视频动作识别中视觉隐私泄露问题，现有方法需要隐私标签，但标注成本高。②提出SPAct框架，包含匿名化函数、自监督隐私移除分支和动作识别分支，通过最小最大优化和对比自监督损失训练。③首次在无需隐私标签的情况下实现隐私移除，利用自监督学习挖掘未标注数据潜力。④在已知动作和隐私属性的协议下，取得了与现有监督方法相当的动作-隐私权衡。
- **摘要（英）**: This paper addresses visual privacy leakage in action recognition without requiring privacy labels. It proposes SPAct, a self-supervised framework with an anonymization function, a privacy removal branch, and an action recognition branch, trained via minimax optimization and contrastive loss. It achieves competitive action-privacy trade-offs compared to supervised methods.
- **核心贡献**: 提出首个无需隐私标签的自监督隐私移除框架。
- **创新点**: 利用对比自监督损失实现隐私移除与动作识别的联合优化。
- **结果**: 在标准协议下达到与监督方法相当的隐私-动作权衡。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual private information leakage is an emerging key issue for the fast growing applications of video understanding like activity recognition. Existing approaches for mitigating privacy leakage in action recognition require privacy labels along with the action labels from the video dataset. However, annotating frames of video dataset for privacy labels is not feasible. Recent developments of self-supervised learning (SSL) have unleashed the untapped potential of the unlabeled data. For the first time, we present a novel training framework which removes privacy information from input video in a self-supervised manner without requiring privacy labels. Our training framework consists of three main components: anonymization function, self-supervised privacy removal branch, and action recognition branch. We train our framework using a minimax optimization strategy to minimize the action recognition cost function and maximize the privacy cost function through a contrastive self-supervised loss. Employing existing protocols of known-action and privacy attributes, our framework achieves a competitive action-privacy trade-off to the existing state-of-the-art supervised methods. In addition, we introduce a new protocol to evaluate the generalization of learned the anonymization function to novel-action and privacy attributes and show that our self-supervised framework outperforms existing supervised methods. Code available at: https://github.com/DAVEISHAN/SPAct

</details>

### TransRank: Self-supervised Video Representation Learning via Ranking-based Transformation Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00301)
- **作者**: Haodong Duan, Nanxuan Zhao, Kai Chen, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2022

### Self-Supervised Models are Continual Learners.
- **链接**: [arXiv:2112.04215](https://arxiv.org/abs/2112.04215) · 📚 被引 134
- **作者**: Enrico Fini, Victor G. Turrisi da Costa, Xavier Alameda-Pineda, Elisa Ricci, Karteek Alahari, Julien Mairal
- **🏷️ 机构**: University of Trento, Inria
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised models have been shown to produce comparable or better visual representations than their supervised counterparts when trained offline on unlabeled data at scale. However, their efficacy is catastrophically reduced in a Continual Learning (CL) scenario where data is presented to the model sequentially. In this paper, we show that self-supervised loss functions can be seamlessly converted into distillation mechanisms for CL by adding a predictor network that maps the current state of the representations to their past state. This enables us to devise a framework for Continual self-supervised visual representation Learning that (i) significantly improves the quality of the learned representations, (ii) is compatible with several state-of-the-art self-supervised objectives, and (iii) needs little to no hyperparameter tuning. We demonstrate the effectiveness of our approach empirically by training six popular self-supervised models in various CL settings.

</details>

### Enhancing Face Recognition with Self-Supervised 3D Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00403) · 📚 被引 26
- **作者**: Mingjie He, Jie Zhang, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: Institute of Computing Technology, CAS,Key Lab of Intelligent Information Processing of Chinese Academy of Sciences (CAS),Beijing,China,100190
- **会议**: CVPR 2022

### Learning Where to Learn in Cross-View Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01405) · 📚 被引 42
- **作者**: Lang Huang, Shan You, Mingkai Zheng, Fei Wang, Chen Qian, Toshihiko Yamasaki
- **🏷️ 机构**: The University of Tokyo, SenseTime Research, The University of Sydney
- **会议**: CVPR 2022

### SLIC: Self-Supervised Learning with Iterative Clustering for Human Action Videos.
- **链接**: [arXiv:2206.12534](https://arxiv.org/abs/2206.12534) · 📚 被引 27
- **作者**: Salar Hosseini Khorasgani, Yuxuan Chen, Florian Shkurti
- **🏷️ 机构**: University of Toronto
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised methods have significantly closed the gap with end-to-end supervised learning for image classification. In the case of human action videos, however, where both appearance and motion are significant factors of variation, this gap remains significant. One of the key reasons for this is that sampling pairs of similar video clips, a required step for many self-supervised contrastive learning methods, is currently done conservatively to avoid false positives. A typical assumption is that similar clips only occur temporally close within a single video, leading to insufficient examples of motion similarity. To mitigate this, we propose SLIC, a clustering-based self-supervised contrastive learning method for human action videos. Our key contribution is that we improve upon the traditional intra-video positive sampling by using iterative clustering to group similar video instances. This enables our method to leverage pseudo-labels from the cluster assignments to sample harder positives and negatives. SLIC outperforms state-of-the-art video retrieval baselines by +15.4% on top-1 recall on UCF101 and by +5.7% when directly transferred to HMDB51. With end-to-end finetuning for action classification, SLIC achieves 83.2% top-1 accuracy (+0.8%) on UCF101 and 54.5% on HMDB51 (+1.6%). SLIC is also competitive with the state-of-the-art in action classification after self-supervised pretraining on Kinetics400.

</details>

### Self-Supervised Dense Consistency Regularization for Image-to-Image Translation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01776) · 📚 被引 25
- **作者**: Minsu Ko, Eunju Cha, Sungjoo Suh, Huijin Lee, Jae-Joon Han, Jinwoo Shin et al.
- **🏷️ 机构**: Samsung Advanced Institute of Technology (SAIT),South Korea, Korea Advanced Institute of Science and Technology (KAIST),South Korea, Seoul National University (SNU),South Korea
- **会议**: CVPR 2022

### Uncertainty-Aware Adaptation for Self-Supervised 3D Human Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01980) · 📚 被引 41
- **作者**: Jogendra Nath Kundu, Siddharth Seth, Pradyumna YM, Varun Jampani, Anirban Chakraborty, R. Venkatesh Babu
- **🏷️ 机构**: Indian Institute of Science,Bangalore, Google Research
- **会议**: CVPR 2022

### Self-Supervised Equivariant Learning for Oriented Keypoint Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00480) · 📚 被引 41
- **作者**: Jongmin Lee, Byungjin Kim, Minsu Cho
- **🏷️ 机构**: Pohang University of Science and Technology (POSTECH),South Korea
- **会议**: CVPR 2022

### AP-BSN: Self-Supervised Denoising for Real-World Images via Asymmetric PD and Blind-Spot Network.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01720) · 📚 被引 160
- **作者**: Wooseok Lee, Sanghyun Son, Kyoung Mu Lee
- **🏷️ 机构**: Seoul National University,Dept. of ECE &#x0026; ASRI
- **会议**: CVPR 2022

### Locality-Aware Inter-and Intra-Video Reconstruction for Self-Supervised Correspondence Learning.
- **链接**: [arXiv:2203.14333](https://arxiv.org/abs/2203.14333) · 📚 被引 40
- **作者**: Liulei Li, Tianfei Zhou, Wenguan Wang, Lu Yang, Jianwu Li, Yi Yang
- **🏷️ 机构**: Beijing Institute of Technology, ETH Zurich, ReLER, AAII, University of Technology Sydney
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our target is to learn visual correspondence from unlabeled videos. We develop LIIR, a locality-aware inter-and intra-video reconstruction framework that fills in three missing pieces, i.e., instance discrimination, location awareness, and spatial compactness, of self-supervised correspondence learning puzzle. First, instead of most existing efforts focusing on intra-video self-supervision only, we exploit cross video affinities as extra negative samples within a unified, inter-and intra-video reconstruction scheme. This enables instance discriminative representation learning by contrasting desired intra-video pixel association against negative inter-video correspondence. Second, we merge position information into correspondence matching, and design a position shifting strategy to remove the side-effect of position encoding during inter-video affinity computation, making our LIIR location-sensitive. Third, to make full use of the spatial continuity nature of video data, we impose a compactness-based constraint on correspondence matching, yielding more sparse and reliable solutions. The learned representation surpasses self-supervised state-of-the-arts on label propagation tasks including objects, semantic parts, and keypoints.

</details>

### UniVIP: A Unified Framework for Self-Supervised Visual Pre-training.
- **链接**: [arXiv:2203.06965](https://arxiv.org/abs/2203.06965) · 📚 被引 24
- **作者**: Zhaowen Li, Yousong Zhu, Fan Yang, Wei Li, Chaoyang Zhao, Yingying Chen et al.
- **🏷️ 机构**: National Laboratory of Pattern Recognition, Institute of Automation, CAS,Beijing,China, SenseTime Research, S-Lab, Nanyang Technological University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) holds promise in leveraging large amounts of unlabeled data. However, the success of popular SSL methods has limited on single-centric-object images like those in ImageNet and ignores the correlation among the scene and instances, as well as the semantic difference of instances in the scene. To address the above problems, we propose a Unified Self-supervised Visual Pre-training (UniVIP), a novel self-supervised framework to learn versatile visual representations on either single-centric-object or non-iconic dataset. The framework takes into account the representation learning at three levels: 1) the similarity of scene-scene, 2) the correlation of scene-instance, 3) the discrimination of instance-instance. During the learning, we adopt the optimal transport algorithm to automatically measure the discrimination of instances. Massive experiments show that UniVIP pre-trained on non-iconic COCO achieves state-of-the-art transfer performance on a variety of downstream tasks, such as image classification, semi-supervised learning, object detection and segmentation. Furthermore, our method can also exploit single-centric-object dataset such as ImageNet and outperforms BYOL by 2.5% with the same pre-training epochs in linear probing, and surpass current self-supervised object detection methods on COCO dataset, demonstrating its universality and potential.

</details>

### Contrastive Dual Gating: Learning Sparse Features With Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01194) · 📚 被引 4
- **作者**: Jian Meng, Li Yang, Jinwoo Shin, Deliang Fan, Jae-Sun Seo
- **🏷️ 机构**: Arizona State University,USA, KAIST,South Korea
- **会议**: CVPR 2022

### Rethinking the Augmentation Module in Contrastive Learning: Learning Hierarchical Augmentation Invariance with Expanded Views.
- **链接**: [arXiv:2206.00227](https://arxiv.org/abs/2206.00227) · 📚 被引 37
- **作者**: Junbo Zhang, Kaisheng Ma
- **🏷️ 机构**: Tsinghua University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A data augmentation module is utilized in contrastive learning to transform the given data example into two views, which is considered essential and irreplaceable. However, the predetermined composition of multiple data augmentations brings two drawbacks. First, the artificial choice of augmentation types brings specific representational invariances to the model, which have different degrees of positive and negative effects on different downstream tasks. Treating each type of augmentation equally during training makes the model learn non-optimal representations for various downstream tasks and limits the flexibility to choose augmentation types beforehand. Second, the strong data augmentations used in classic contrastive learning methods may bring too much invariance in some cases, and fine-grained information that is essential to some downstream tasks may be lost. This paper proposes a general method to alleviate these two problems by considering where and what to contrast in a general contrastive learning framework. We first propose to learn different augmentation invariances at different depths of the model according to the importance of each data augmentation instead of learning representational invariances evenly in the backbone. We then propose to expand the contrast content with augmentation embeddings to reduce the misleading effects of strong data augmentations. Experiments based on several baseline methods demonstrate that we learn better representations for various benchmarks on classification, detection, and segmentation downstream tasks.

</details>

### Frame-wise Action Representations for Long Videos via Sequence Contrastive Learning.
- **链接**: [arXiv:2203.14957](https://arxiv.org/abs/2203.14957) · [代码](https://github.com/minghchen/CARL_code) · 📚 被引 40
- **作者**: Minghao Chen, Fangyun Wei, Chong Li, Deng Cai
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, College of Computer Science, Microsoft Research Asia
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prior works on action representation learning mainly focus on designing various architectures to extract the global representations for short video clips. In contrast, many practical applications such as video alignment have strong demand for learning dense representations for long videos. In this paper, we introduce a novel contrastive action representation learning (CARL) framework to learn frame-wise action representations, especially for long videos, in a self-supervised manner. Concretely, we introduce a simple yet efficient video encoder that considers spatio-temporal context to extract frame-wise representations. Inspired by the recent progress of self-supervised learning, we present a novel sequence contrastive loss (SCL) applied on two correlated views obtained through a series of spatio-temporal data augmentations. SCL optimizes the embedding space by minimizing the KL-divergence between the sequence similarity of two augmented views and a prior Gaussian distribution of timestamp distance. Experiments on FineGym, PennAction and Pouring datasets show that our method outperforms previous state-of-the-art by a large margin for downstream fine-grained action classification. Surprisingly, although without training on paired videos, our approach also shows outstanding performance on video alignment and fine-grained frame retrieval tasks. Code and models are available at https://github.com/minghchen/CARL_code.

</details>

### Unpaired Deep Image Deraining Using Dual Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00206) · 📚 被引 189
- **作者**: Xiang Chen, Jinshan Pan, Kui Jiang, Yufeng Li, Yufeng Huang, Caihua Kong et al.
- **🏷️ 机构**: Shenyang Aerospace University, Nanjing University of Science and Technology, Wuhan University
- **会议**: CVPR 2022

### Contrastive Learning for Unsupervised Video Highlight Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01365) · 📚 被引 36
- **作者**: Taivanbat Badamdorj, Mrigank Rochan, Yang Wang, Li Cheng
- **🏷️ 机构**: University of Alberta, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022

### UTC: A Unified Transformer with Inter-Task Contrastive Learning for Visual Dialog.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01757) · 📚 被引 36
- **作者**: Cheng Chen, Zhenshan Tan, Qingrong Cheng, Xin Jiang, Qun Liu, Yudong Zhu et al.
- **🏷️ 机构**: Fudan University,Department of Electronic Engineering, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022

### Robust Contrastive Learning against Noisy Views.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01617) · 📚 被引 64
- **作者**: Ching-Yao Chuang, R. Devon Hjelm, Xin Wang, Vibhav Vineet, Neel Joshi, Antonio Torralba et al.
- **🏷️ 机构**: MIT CSAIL, Microsoft Research
- **会议**: CVPR 2022

### Fine-grained Temporal Contrastive Learning for Weakly-supervised Temporal Action Localization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01937) · 📚 被引 84
- **作者**: Junyu Gao, Mengyuan Chen, Changsheng Xu
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences (CASIA),National Lab of Pattern Recognition (NLPR)
- **会议**: CVPR 2022

### SCS-Co: Self-Consistent Style Contrastive Learning for Image Harmonization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01909) · 📚 被引 43
- **作者**: Yucheng Hang, Bin Xia, Wenming Yang, Qingmin Liao
- **🏷️ 机构**: Shenzhen International Graduate School, Tsinghua University,China
- **会议**: CVPR 2022

### QS-Attn: Query-Selected Attention for Contrastive Learning in I2I Translation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01775) · 📚 被引 108
- **作者**: Xueqi Hu, Xinyue Zhou, Qiusheng Huang, Zhengyi Shi, Li Sun, Qingli Li
- **🏷️ 机构**: Shanghai Key Laboratory of Multidimensional Information Processing
- **会议**: CVPR 2022

### Exploring Patch-wise Semantic Relation for Contrastive Learning in Image-to-Image Translation Tasks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01772) · 📚 被引 104
- **作者**: Chanyong Jung, Gihyun Kwon, Jong Chul Ye
- **🏷️ 机构**: Department of Bio and Brain Engineering, Kim Jaechul Graduate School of AI, KAIST
- **会议**: CVPR 2022

### UBoCo: Unsupervised Boundary Contrastive Learning for Generic Event Boundary Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01944) · 📚 被引 32
- **作者**: Hyolim Kang, Jinwoo Kim, Taehyun Kim, Seon Joo Kim
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2022

### UNICON: Combating Label Noise Through Uniform Selection and Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00945) · 📚 被引 156
- **作者**: Nazmul Karim, Mamshad Nayeem Rizve, Nazanin Rahnavard, Ajmal Mian, Mubarak Shah
- **🏷️ 机构**: UCF,Department of Electrical and Computer Engineering,USA, UCF,Center for Research in Computer Vision,USA, UWA,Department of Computer Science and Software Engineering,Australia
- **会议**: CVPR 2022

### Targeted Supervised Contrastive Learning for Long-Tailed Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00679) · 📚 被引 190
- **作者**: Tianhong Li, Peng Cao, Yuan Yuan, Lijie Fan, Yuzhe Yang, Rogério Feris et al.
- **🏷️ 机构**: MIT CSAIL, MIT-IBM Watson AI Lab
- **会议**: CVPR 2022

### Contextual Outpainting with Object-Level Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01116) · 📚 被引 10
- **作者**: Jiacheng Li, Chang Chen, Zhiwei Xiong
- **🏷️ 机构**: University of Science and Technology of China, Huawei Technologies Co., Ltd.,Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022

### Selective-Supervised Contrastive Learning with Noisy Labels.
- **链接**: [arXiv:2203.04181](https://arxiv.org/abs/2203.04181) · [代码](https://github.com/ShikunLi/Sel-CL) · 📚 被引 184
- **作者**: Shikun Li, Xiaobo Xia, Shiming Ge, Tongliang Liu
- **🏷️ 机构**: Institute of Information Engineering, Chinese Academy of Sciences,China, The University of Sydney,Trustworthy Machine Learning Lab,Australia
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep networks have strong capacities of embedding data into latent representations and finishing following tasks. However, the capacities largely come from high-quality annotated labels, which are expensive to collect. Noisy labels are more affordable, but result in corrupted representations, leading to poor generalization performance. To learn robust representations and handle noisy labels, we propose selective-supervised contrastive learning (Sel-CL) in this paper. Specifically, Sel-CL extend supervised contrastive learning (Sup-CL), which is powerful in representation learning, but is degraded when there are noisy labels. Sel-CL tackles the direct cause of the problem of Sup-CL. That is, as Sup-CL works in a \textit{pair-wise} manner, noisy pairs built by noisy labels mislead representation learning. To alleviate the issue, we select confident pairs out of noisy ones for Sup-CL without knowing noise rates. In the selection process, by measuring the agreement between learned representations and given labels, we first identify confident examples that are exploited to build confident pairs. Then, the representation similarity distribution in the built confident pairs is exploited to identify more confident pairs out of noisy pairs. All obtained confident pairs are finally used for Sup-CL to enhance representations. Experiments on multiple noisy datasets demonstrate the robustness of the learned representations by our method, following the state-of-the-art performance. Source codes are available at https://github.com/ShikunLi/Sel-CL

</details>

### Multi-marginal Contrastive Learning for Multilabel Subcellular Protein Localization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01997) · 📚 被引 4
- **作者**: Ziyi Liu, Zengmao Wang, Bo Du
- **🏷️ 机构**: Institute of Artificial Intelligence, School of Computer Science, Wuhan University,National Engineering Research Center for Multimedia Software, Hubei Key Laboratory of Multimedia and Network Communication Engineering,Wuhan,China
- **会议**: CVPR 2022

### Probabilistic Representations for Video Contrastive Learning.
- **链接**: [arXiv:2204.03946](https://arxiv.org/abs/2204.03946) · 📚 被引 49
- **作者**: Jungin Park, Jiyoung Lee, Ig-Jae Kim, Kwanghoon Sohn
- **🏷️ 机构**: Yonsei University, NAVER AI Lab, Korea Institute of Science and Technology (KIST)
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents Probabilistic Video Contrastive Learning, a self-supervised representation learning method that bridges contrastive learning with probabilistic representation. We hypothesize that the clips composing the video have different distributions in short-term duration, but can represent the complicated and sophisticated video distribution through combination in a common embedding space. Thus, the proposed method represents video clips as normal distributions and combines them into a Mixture of Gaussians to model the whole video distribution. By sampling embeddings from the whole video distribution, we can circumvent the careful sampling strategy or transformations to generate augmented views of the clips, unlike previous deterministic methods that have mainly focused on such sample generation strategies for contrastive learning. We further propose a stochastic contrastive loss to learn proper video distributions and handle the inherent uncertainty from the nature of the raw video. Experimental results verify that our probabilistic embedding stands as a state-of-the-art video representation learning for action recognition and video retrieval on the most popular benchmarks, including UCF101 and HMDB51.

</details>

### Fair Contrastive Learning for Facial Attribute Classification.
- **链接**: [arXiv:2203.16209](https://arxiv.org/abs/2203.16209) · [代码](https://github.com/sungho-CoolG/FSCL) · 📚 被引 69
- **作者**: Sungho Park, Jewook Lee, Pilhyeon Lee, Sunhee Hwang, Dohyung Kim, Hyeran Byun
- **🏷️ 机构**: Yonsei University, LG Uplus, SK Inc.
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning visual representation of high quality is essential for image classification. Recently, a series of contrastive representation learning methods have achieved preeminent success. Particularly, SupCon outperformed the dominant methods based on cross-entropy loss in representation learning. However, we notice that there could be potential ethical risks in supervised contrastive learning. In this paper, we for the first time analyze unfairness caused by supervised contrastive learning and propose a new Fair Supervised Contrastive Loss (FSCL) for fair visual representation learning. Inheriting the philosophy of supervised contrastive learning, it encourages representation of the same class to be closer to each other than that of different classes, while ensuring fairness by penalizing the inclusion of sensitive attribute information in representation. In addition, we introduce a group-wise normalization to diminish the disparities of intra-group compactness and inter-class separability between demographic groups that arouse unfair classification. Through extensive experiments on CelebA and UTK Face, we validate that the proposed method significantly outperforms SupCon and existing state-of-the-art methods in terms of the trade-off between top-1 accuracy and fairness. Moreover, our method is robust to the intensity of data bias and effectively works in incomplete supervised settings. Our code is available at https://github.com/sungho-CoolG/FSCL.

</details>

### Consistent Explanations by Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00997) · 📚 被引 14
- **作者**: Vipin Pillai, Soroush Abbasi Koohpayegani, Ashley Ouligian, Dennis Fong, Hamed Pirsiavash
- **🏷️ 机构**: University of Maryland,Baltimore County, Northrop Grumman, University of California,Davis
- **会议**: CVPR 2022

### Contrastive Learning for Space-time Correspondence via Self-cycle Consistency.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01427) · 📚 被引 14
- **作者**: Jeany Son
- **🏷️ 机构**: AI Graduate School, GIST,Gwangju,South Korea
- **会议**: CVPR 2022

### Long-Short Temporal Contrastive Learning of Video Transformers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01362) · 📚 被引 42
- **作者**: Jue Wang, Gedas Bertasius, Du Tran, Lorenzo Torresani
- **🏷️ 机构**: Facebook AI Research, UNC Chapel Hill
- **会议**: CVPR 2022

### Rethinking Minimal Sufficient Representation in Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01557) · 📚 被引 66
- **作者**: Haoqing Wang, Xun Guo, Zhi-Hong Deng, Yan Lu
- **🏷️ 机构**: Peking University, Microsoft Research Asia
- **会议**: CVPR 2022

### ContrastMask: Contrastive Learning to Segment Every Thing.
- **链接**: [arXiv:2203.09775](https://arxiv.org/abs/2203.09775) · 📚 被引 46
- **作者**: Xuehui Wang, Kai Zhao, Ruixin Zhang, Shouhong Ding, Yan Wang, Wei Shen
- **🏷️ 机构**: AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, Youtu Lab, Tencent, Shanghai Key Lab of Multidimensional Information Processing, ECNU
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Partially-supervised instance segmentation is a task which requests segmenting objects from novel unseen categories via learning on limited seen categories with annotated masks thus eliminating demands of heavy annotation burden. The key to addressing this task is to build an effective class-agnostic mask segmentation model. Unlike previous methods that learn such models only on seen categories, in this paper, we propose a new method, named ContrastMask, which learns a mask segmentation model on both seen and unseen categories under a unified pixel-level contrastive learning framework. In this framework, annotated masks of seen categories and pseudo masks of unseen categories serve as a prior for contrastive learning, where features from the mask regions (foreground) are pulled together, and are contrasted against those from the background, and vice versa. Through this framework, feature discrimination between foreground and background is largely improved, facilitating learning of the class-agnostic mask segmentation model. Exhaustive experiments on the COCO dataset demonstrate the superiority of our method, which outperforms previous state-of-the-arts.

</details>

### Noise Is Also Useful: Negative Correlation-Steered Latent Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00013) · 📚 被引 16
- **作者**: Jiexi Yan, Lei Luo, Chenghao Xu, Cheng Deng, Heng Huang
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China,710071, University of Pittsburgh,Department of Electrical and Computer Engineering,PA,USA,15260
- **会议**: CVPR 2022

### Unified Contrastive Learning in Image-Text-Label Space.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01857)
- **作者**: Jianwei Yang, Chunyuan Li, Pengchuan Zhang, Bin Xiao, Ce Liu, Lu Yuan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### PCL: Proxy-based Contrastive Learning for Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00696) · 📚 被引 125
- **作者**: Xufeng Yao, Yang Bai, Xinyun Zhang, Yuechen Zhang, Qi Sun, Ran Chen et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, SmartMore
- **会议**: CVPR 2022

### Unsupervised Deraining: Where Contrastive Learning Meets Self-similarity.
- **链接**: [arXiv:2203.11509](https://arxiv.org/abs/2203.11509) · 📚 被引 81
- **作者**: Yuntong Ye, Changfeng Yu, Yi Chang, Lin Zhu, Xi-Le Zhao, Luxin Yan et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Peking University, University of Electronic Science and Technology of China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image deraining is a typical low-level image restoration task, which aims at decomposing the rainy image into two distinguishable layers: the clean image layer and the rain layer. Most of the existing learning-based deraining methods are supervisedly trained on synthetic rainy-clean pairs. The domain gap between the synthetic and real rains makes them less generalized to different real rainy scenes. Moreover, the existing methods mainly utilize the property of the two layers independently, while few of them have considered the mutually exclusive relationship between the two layers. In this work, we propose a novel non-local contrastive learning (NLCL) method for unsupervised image deraining. Consequently, we not only utilize the intrinsic self-similarity property within samples but also the mutually exclusive property between the two layers, so as to better differ the rain layer from the clean image. Specifically, the non-local self-similarity image layer patches as the positives are pulled together and similar rain layer patches as the negatives are pushed away. Thus the similar positive/negative samples that are close in the original space benefit us to enrich more discriminative representation. Apart from the self-similarity sampling strategy, we analyze how to choose an appropriate feature encoder in NLCL. Extensive experiments on different real rainy datasets demonstrate that the proposed method obtains state-of-the-art performance in real deraining.

</details>

### Contextualized Spatio-Temporal Contrastive Learning with Self-Supervision.
- **链接**: [arXiv:2112.05181](https://arxiv.org/abs/2112.05181) · 📚 被引 26
- **作者**: Liangzhe Yuan, Rui Qian, Yin Cui, Boqing Gong, Florian Schroff, Ming-Hsuan Yang et al.
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern self-supervised learning algorithms typically enforce persistency of instance representations across views. While being very effective on learning holistic image and video representations, such an objective becomes sub-optimal for learning spatio-temporally fine-grained features in videos, where scenes and instances evolve through space and time. In this paper, we present Contextualized Spatio-Temporal Contrastive Learning (ConST-CL) to effectively learn spatio-temporally fine-grained video representations via self-supervision. We first design a region-based pretext task which requires the model to transform in-stance representations from one view to another, guided by context features. Further, we introduce a simple network design that successfully reconciles the simultaneous learning process of both holistic and local representations. We evaluate our learned representations on a variety of downstream tasks and show that ConST-CL achieves competitive results on 6 datasets, including Kinetics, UCF, HMDB, AVA-Kinetics, AVA and OTB.

</details>

### Use All The Labels: A Hierarchical Multi-Label Contrastive Learning Framework.
- **链接**: [arXiv:2204.13207](https://arxiv.org/abs/2204.13207) · [代码](https://github.com/salesforce/hierarchicalContrastiveLearning) · 📚 被引 84
- **作者**: Shu Zhang, Ran Xu, Caiming Xiong, Chetan Ramaiah
- **🏷️ 机构**: Salesforce Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current contrastive learning frameworks focus on leveraging a single supervisory signal to learn representations, which limits the efficacy on unseen data and downstream tasks. In this paper, we present a hierarchical multi-label representation learning framework that can leverage all available labels and preserve the hierarchical relationship between classes. We introduce novel hierarchy preserving losses, which jointly apply a hierarchical penalty to the contrastive loss, and enforce the hierarchy constraint. The loss function is data driven and automatically adapts to arbitrary multi-label structures. Experiments on several datasets show that our relationship-preserving embedding performs well on a variety of tasks and outperform the baseline supervised and self-supervised approaches. Code is available at https://github.com/salesforce/hierarchicalContrastiveLearning.

</details>

### Dual Temperature Helps Contrastive Learning Without Many Negative Samples: Towards Understanding and Simplifying MoCo.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01404) · 📚 被引 43
- **作者**: Chaoning Zhang, Kang Zhang, Trung X. Pham, Axi Niu, Zhinan Qiao, Chang D. Yoo et al.
- **🏷️ 机构**: KAIST, Northwestern Polytechnical University, University of North Texas
- **会议**: CVPR 2022

### Balanced Contrastive Learning for Long-Tailed Visual Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00678) · 📚 被引 1
- **作者**: Jianggang Zhu, Zheng Wang, Jingjing Chen, Yi-Ping Phoebe Chen, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Estimating Fine-Grained Noise Model via Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01235) · 📚 被引 30
- **作者**: Yunhao Zou, Ying Fu
- **🏷️ 机构**: School of Computer Science and Technology, Beijing Institute of Technology
- **会议**: CVPR 2022

### SimMIM: a Simple Framework for Masked Image Modeling. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2111.09886](https://arxiv.org/abs/2111.09886) · 📚 被引 1154
- **作者**: Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Jianmin Bao, Zhuliang Yao et al.
- **🏷️ 机构**: Tsinghua University, Microsoft Research Asia, Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2022
- **摘要（中）**: ①该论文针对掩码图像建模方法中复杂设计（如块状掩码、离散VAE标记化）的必要性问题，提出了一个简化框架SimMIM。②方法采用随机掩码、直接回归原始RGB像素值，并使用轻量线性预测头，系统研究了各组件的影响。③相比现有方法，SimMIM简化了设计但性能更强，证明了简单设计足以学习良好表征。④使用ViT-B在ImageNet-1K上预训练后微调达到83.8% top-1准确率，超越之前最佳方法0.6%；在SwinV2-H（约6.5亿参数）上达到87.1%。
- **摘要（英）**: This paper presents SimMIM, a simple framework for masked image modeling using random masking, raw pixel regression, and a linear prediction head. It systematically shows that simple designs achieve strong representation learning, surpassing prior methods with ViT-B (83.8% top-1) and SwinV2-H (87.1%) on ImageNet-1K.
- **核心贡献**: 提出了一个简化且高效的掩码图像建模框架SimMIM，并系统验证了各组件的作用。
- **创新点**: 证明了随机掩码、像素回归和线性头等简单设计即可超越复杂方法。
- **结果**: 在ImageNet-1K上以ViT-B达到83.8%准确率，SwinV2-H达到87.1%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents SimMIM, a simple framework for masked image modeling. We simplify recently proposed related approaches without special designs such as block-wise masking and tokenization via discrete VAE or clustering. To study what let the masked image modeling task learn good representations, we systematically study the major components in our framework, and find that simple designs of each component have revealed very strong representation learning performance: 1) random masking of the input image with a moderately large masked patch size (e.g., 32) makes a strong pre-text task; 2) predicting raw pixels of RGB values by direct regression performs no worse than the patch classification approaches with complex designs; 3) the prediction head can be as light as a linear layer, with no worse performance than heavier ones. Using ViT-B, our approach achieves 83.8% top-1 fine-tuning accuracy on ImageNet-1K by pre-training also on this dataset, surpassing previous best approach by +0.6%. When applied on a larger model of about 650 million parameters, SwinV2-H, it achieves 87.1% top-1 accuracy on ImageNet-1K using only ImageNet-1K data. We also leverage this approach to facilitate the training of a 3B model (SwinV2-G), that by $40\times$ less data than that in previous practice, we achieve the state-of-the-art on four representative vision benchmarks. The code and models will be publicly available at https://github.com/microsoft/SimMIM.

</details>

### VICRegL: Self-Supervised Learning of Local Visual Features.
- **链接**: [arXiv:2210.01571](https://arxiv.org/abs/2210.01571) · [代码](https://github.com/facebookresearch/VICRegL) · 📚 被引 23
- **作者**: Adrien Bardes, Jean Ponce, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

- Self-supervised object detection from audio-visual correspondence. → [multimodal](../multimodal/Guideline%202022.md)
- Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- CrossPoint: Self-Supervised Cross-Modal Contrastive Learning for 3D Point Cloud Understanding. → [multimodal](../multimodal/Guideline%202022.md)
- Towards Discriminative Representation: Multi-view Trajectory Contrastive Learning for Online Multi-object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Mining Multi-View Information: A Strong Self-Supervised Framework for Depth-based 3D Hand Pose and Mesh Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Self-supervised Spatial Reasoning on Multi-View Line Drawings. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Exploiting Pseudo Labels in a Self-Supervised Learning Framework for Improved Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- ContIG: Self-supervised Multimodal Contrastive Learning for Medical Imaging with Genetics. → [multimodal](../multimodal/Guideline%202022.md)
- Fire Together Wire Together: A Dynamic Pruning Approach with Self-Supervised Mask Prediction. → [network-pruning](../network-pruning/Guideline%202022.md)
- Multi-Frame Self-Supervised Depth with Transformers. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- M5Product: Self-harmonized Contrastive Learning for E-commercial Multi-modal Pretraining. → [multimodal](../multimodal/Guideline%202022.md)
- EI-CLIP: Entity-aware Interventional Contrastive Learning for E-commerce Cross-modal Retrieval. → [multimodal](../multimodal/Guideline%202022.md)
- C2 AM: Contrastive learning of Class-agnostic Activation Map for Weakly Supervised Object Localization and Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202022.md)

## 🆕 增量新增

### How Severe Is Benchmark-Sensitivity in Video Self-supervised Learning? **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2203.14221](https://arxiv.org/abs/2203.14221) · 📚 被引 14
- **作者**: Fida Mohammad Thoker, Hazel Doughty, Piyush Bagad, Cees G. M. Snoek
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视频自监督学习模型在标准基准上表现良好但泛化能力未知的问题，系统研究了其对领域、样本、动作和任务四类因素的敏感性。②通过在7个视频数据集、9种自监督方法和6个视频理解任务上进行了超过500次实验，评估了模型在不同敏感性因素下的表现。③相比已有工作仅关注单一基准，该研究首次全面揭示了当前基准无法有效反映模型泛化能力，且自监督方法在领域偏移大和下游样本少时显著落后于有监督预训练。④基于分析结果，提出了SEVERE基准子集，用于更可靠地评估视频自监督表示的可泛化性。
- **摘要（英）**: This paper investigates the sensitivity of video self-supervised learning to domain, samples, actions, and task factors through over 500 experiments across 7 datasets and 6 tasks. It reveals that current benchmarks poorly indicate generalization and that self-supervised methods lag behind supervised pre-training under large domain shifts and low sample availability. The authors distill a SEVERE benchmark subset to better evaluate representation generalizability.
- **核心贡献**: 系统揭示了视频自监督学习对基准的敏感性，并提出了更可靠的SEVERE评估基准。
- **创新点**: 首次从多因素角度全面分析视频自监督学习的泛化能力，并设计基准子集。
- **结果**: 发现现有基准无法有效指示泛化能力，自监督方法在挑战性场景下显著落后于有监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent success of video self-supervised learning models, there is much still to be understood about their generalization capability. In this paper, we investigate how sensitive video self-supervised learning is to the current conventional benchmark and whether methods generalize beyond the canonical evaluation setting. We do this across four different factors of sensitivity: domain, samples, actions and task. Our study which encompasses over 500 experiments on 7 video datasets, 9 self-supervised methods and 6 video understanding tasks, reveals that current benchmarks in video self-supervised learning are not good indicators of generalization along these sensitivity factors. Further, we find that self-supervised methods considerably lag behind vanilla supervised pre-training, especially when domain shift is large and the amount of available downstream samples are low. From our analysis, we distill the SEVERE-benchmark, a subset of our experiments, and discuss its implication for evaluating the generalizability of representations obtained by existing and future self-supervised video learning methods.

</details>

### CrossPoint: Self-Supervised Cross-Modal Contrastive Learning for 3D Point Cloud Understanding. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2203.00680](https://arxiv.org/abs/2203.00680) · 📚 被引 274
- **作者**: Mohamed Afham, Isuru Dissanayake, Dinithi Dissanayake, Amaya Dharmasiri, Kanchana Thilakarathna, Ranga Rodrigo
- **🏷️ 机构**: Univeristy of Moratuwa,Dept. of Electronic and Telecommunication Engineering,Sri Lanka, The University of Sydney
- **会议**: CVPR 2022
- **摘要（中）**: ①针对点云数据人工标注成本高的问题，探索自监督学习以学习可迁移的3D点云表示。②提出了CrossPoint，一种跨模态对比学习方法，通过最大化点云与对应渲染2D图像在不变空间中的一致性，并鼓励点云模态内的变换不变性，联合优化跨模态和模态内特征对应。③相比仅使用点云的自监督方法，利用2D图像先验知识增强3D理解。④在多个下游任务（如3D分类、分割）上优于现有无监督方法，展示了跨模态学习的有效性。
- **摘要（英）**: This paper tackles the high annotation cost of point clouds by proposing CrossPoint, a cross-modal contrastive learning method that aligns point clouds with rendered 2D images in an invariant space while encouraging transformation invariance within the point cloud modality. It outperforms prior unsupervised methods on downstream tasks like 3D classification and segmentation, demonstrating the benefit of leveraging 2D priors.
- **核心贡献**: 提出跨模态对比学习框架，提升3D点云自监督表示质量。
- **创新点**: 结合2D图像模态增强3D点云自监督学习。
- **结果**: 在多个下游任务上优于现有无监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Manual annotation of large-scale point cloud dataset for varying tasks such as 3D object classification, segmentation and detection is often laborious owing to the irregular structure of point clouds. Self-supervised learning, which operates without any human labeling, is a promising approach to address this issue. We observe in the real world that humans are capable of mapping the visual concepts learnt from 2D images to understand the 3D world. Encouraged by this insight, we propose CrossPoint, a simple cross-modal contrastive learning approach to learn transferable 3D point cloud representations. It enables a 3D-2D correspondence of objects by maximizing agreement between point clouds and the corresponding rendered 2D image in the invariant space, while encouraging invariance to transformations in the point cloud modality. Our joint training objective combines the feature correspondences within and across modalities, thus ensembles a rich learning signal from both 3D point cloud and 2D image modalities in a self-supervised fashion. Experimental results show that our approach outperforms the previous unsupervised learning methods on a diverse range of downstream tasks including 3D object classification and segmentation. Further, the ablation studies validate the potency of our approach for a better point cloud understanding. Code and pretrained models are available at http://github.com/MohamedAfham/CrossPoint.

</details>

### Object Discovery via Contrastive Learning for Weakly Supervised Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2208.07576](https://arxiv.org/abs/2208.07576)
- **作者**: Jinhwan Seo, Wonho Bae, Danica J. Sutherland, Junhyug Noh, Daijin Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对弱监督目标检测中常用argmax标注法忽略大量实例的问题，提出一种新的多实例标注方法——对象发现（object discovery），并引入弱监督对比损失（WSCL），在无实例级信息下构建可信相似度阈值，利用同类嵌入向量的一致特征进行采样。该方法在MS-COCO 2014/2017和PASCAL VOC 2012上取得新的最先进结果，在VOC 2007上表现有竞争力。相比现有自监督实例级监督方法，显著提升了对多实例的召回率。
- **摘要（英）**: To address the issue that argmax labeling in weakly supervised object detection often ignores many instances, this paper proposes object discovery, a novel multiple instance labeling method, and introduces weakly supervised contrastive loss (WSCL) to construct credible similarity thresholds without instance-level information. It achieves state-of-the-art results on MS-COCO 2014/2017 and PASCAL VOC 2012, with competitive performance on VOC 2007, improving recall of multiple instances.
- **核心贡献**: 提出对象发现与弱监督对比损失，提升多实例标注质量。
- **创新点**: 在无实例级监督下设计对比学习采样机制。
- **结果**: 在多个基准上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly Supervised Object Detection (WSOD) is a task that detects objects in an image using a model trained only on image-level annotations. Current state-of-the-art models benefit from self-supervised instance-level supervision, but since weak supervision does not include count or location information, the most common ``argmax'' labeling method often ignores many instances of objects. To alleviate this issue, we propose a novel multiple instance labeling method called object discovery. We further introduce a new contrastive loss under weak supervision where no instance-level information is available for sampling, called weakly supervised contrastive loss (WSCL). WSCL aims to construct a credible similarity threshold for object discovery by leveraging consistent features for embedding vectors in the same class. As a result, we achieve new state-of-the-art results on MS-COCO 2014 and 2017 as well as PASCAL VOC 2012, and competitive results on PASCAL VOC 2007.

</details>

### SLiDE: Self-supervised LiDAR De-snowing Through Reconstruction Difficulty. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2208.04043](https://arxiv.org/abs/2208.04043) · 📚 被引 21
- **作者**: Gwangtak Bae, Byungjun Kim, Seongyong Ahn, Jihong Min, Inwook Shim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对雪天LiDAR点云中噪声点影响3D场景分析的问题，提出了一种无需标注的自监督去雪方法。②利用噪声点与邻居空间相关性低的特性，设计了PR-Net重建点云和RD-Net预测重建难度，通过后处理检测雪点。③相比需要逐点标注的语义分割方法，该方法完全自监督，避免了人工标注成本，且性能优于现有无标签方法。④在实验中，该方法达到了无标签方法中的最先进性能，并与全监督方法相当，同时可作为预训练任务提升下游任务的标签效率。
- **摘要（英）**: This paper proposes a self-supervised framework for snow point removal in LiDAR point clouds, using PR-Net for reconstruction and RD-Net for difficulty prediction. It exploits low spatial correlation of noise points, achieving state-of-the-art performance among label-free methods and comparable results to fully supervised approaches. The method also serves as a pretext task for label-efficient learning.
- **核心贡献**: 提出了首个自监督LiDAR去雪框架，无需标注即可有效检测雪点。
- **创新点**: 利用重建难度作为代理任务，捕捉噪声点的结构特性。
- **结果**: 性能优于无标签方法，与全监督方法相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR is widely used to capture accurate 3D outdoor scene structures. However, LiDAR produces many undesirable noise points in snowy weather, which hamper analyzing meaningful 3D scene structures. Semantic segmentation with snow labels would be a straightforward solution for removing them, but it requires laborious point-wise annotation. To address this problem, we propose a novel self-supervised learning framework for snow points removal in LiDAR point clouds. Our method exploits the structural characteristic of the noise points: low spatial correlation with their neighbors. Our method consists of two deep neural networks: Point Reconstruction Network (PR-Net) reconstructs each point from its neighbors; Reconstruction Difficulty Network (RD-Net) predicts point-wise difficulty of the reconstruction by PR-Net, which we call reconstruction difficulty. With simple post-processing, our method effectively detects snow points without any label. Our method achieves the state-of-the-art performance among label-free approaches and is comparable to the fully-supervised method. Moreover, we demonstrate that our method can be exploited as a pretext task to improve label-efficiency of supervised training of de-snowing.

</details>

### SuperLine3D: Self-supervised Line Segmentation and Description for LiDAR Point Cloud.
- **链接**: [arXiv:2208.01925](https://arxiv.org/abs/2208.01925) · 📚 被引 12
- **作者**: Xiangrui Zhao, Sheng Yang, Tianxin Huang, Jun Chen, Teng Ma, Mingyang Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Poles and building edges are frequently observable objects on urban roads, conveying reliable hints for various computer vision tasks. To repetitively extract them as features and perform association between discrete LiDAR frames for registration, we propose the first learning-based feature segmentation and description model for 3D lines in LiDAR point cloud. To train our model without the time consuming and tedious data labeling process, we first generate synthetic primitives for the basic appearance of target lines, and build an iterative line auto-labeling process to gradually refine line labels on real LiDAR scans. Our segmentation model can extract lines under arbitrary scale perturbations, and we use shared EdgeConv encoder layers to train the two segmentation and descriptor heads jointly. Base on the model, we can build a highly-available global registration module for point cloud registration, in conditions without initial transformation hints. Experiments have demonstrated that our line-based registration method is highly competitive to state-of-the-art point-based approaches. Our code is available at https://github.com/zxrzju/SuperLine3D.git.

</details>

### PointCLM: A Contrastive Learning-based Framework for Multi-instance Point Cloud Registration.
- **链接**: [arXiv:2209.00219](https://arxiv.org/abs/2209.00219)
- **作者**: Mingzhi Yuan, Zhihao Li, Qiuye Jin, Xinrong Chen, Manning Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-instance point cloud registration is the problem of estimating multiple poses of source point cloud instances within a target point cloud. Solving this problem is challenging since inlier correspondences of one instance constitute outliers of all the other instances. Existing methods often rely on time-consuming hypothesis sampling or features leveraging spatial consistency, resulting in limited performance. In this paper, we propose PointCLM, a contrastive learning-based framework for mutli-instance point cloud registration. We first utilize contrastive learning to learn well-distributed deep representations for the input putative correspondences. Then based on these representations, we propose a outlier pruning strategy and a clustering strategy to efficiently remove outliers and assign the remaining correspondences to correct instances. Our method outperforms the state-of-the-art methods on both synthetic and real datasets by a large margin.

</details>

### Masked Discrimination for Self-supervised Learning on Point Clouds.
- **链接**: [arXiv:2203.11183](https://arxiv.org/abs/2203.11183) · 📚 被引 137
- **作者**: Haotian Liu, Mu Cai, Yong Jae Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Masked autoencoding has achieved great success for self-supervised learning in the image and language domains. However, mask based pretraining has yet to show benefits for point cloud understanding, likely due to standard backbones like PointNet being unable to properly handle the training versus testing distribution mismatch introduced by masking during training. In this paper, we bridge this gap by proposing a discriminative mask pretraining Transformer framework, MaskPoint}, for point clouds. Our key idea is to represent the point cloud as discrete occupancy values (1 if part of the point cloud; 0 if not), and perform simple binary classification between masked object points and sampled noise points as the proxy task. In this way, our approach is robust to the point sampling variance in point clouds, and facilitates learning rich representations. We evaluate our pretrained models across several downstream tasks, including 3D shape classification, segmentation, and real-word object detection, and demonstrate state-of-the-art results while achieving a significant pretraining speedup (e.g., 4.1x on ScanNet) compared to the prior state-of-the-art Transformer baseline. Code is available at https://github.com/haotian-liu/MaskPoint.

</details>

### Masked Autoencoders for Point Cloud Self-supervised Learning.
- **链接**: [arXiv:2203.06604](https://arxiv.org/abs/2203.06604)
- **作者**: Yatian Pang, Wenxiao Wang, Francis E. H. Tay, Wei Liu, Yonghong Tian, Li Yuan
- **🏷️ 机构**: National University of Singapore, Singapore, Institute for Infocomm Research, A*STAR, Singapore, School of Electronic and Computer Engineering, Peking University, Beijing, China
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a promising scheme of self-supervised learning, masked autoencoding has significantly advanced natural language processing and computer vision. Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud's properties, including leakage of location information and uneven information density. Concretely, we divide the input point cloud into irregular point patches and randomly mask them at a high ratio. Then, a standard Transformer based autoencoder, with an asymmetric design and a shifting mask tokens operation, learns high-level latent features from unmasked point patches, aiming to reconstruct the masked point patches. Extensive experiments show that our approach is efficient during pre-training and generalizes well on various downstream tasks. Specifically, our pre-trained models achieve 85.18% accuracy on ScanObjectNN and 94.04% accuracy on ModelNet40, outperforming all the other self-supervised learning methods. We show with our scheme, a simple architecture entirely based on standard Transformers can surpass dedicated Transformer models from supervised learning. Our approach also advances state-of-the-art accuracies by 1.5%-2.3% in the few-shot object classification. Furthermore, our work inspires the feasibility of applying unified architectures from languages and images to the point cloud.

</details>

### Differentiable Raycasting for Self-Supervised Occupancy Forecasting.
- **链接**: [arXiv:2210.01917](https://arxiv.org/abs/2210.01917) · 📚 被引 58
- **作者**: Tarasha Khurana, Peiyun Hu, Achal Dave, Jason Ziglar, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motion planning for safe autonomous driving requires learning how the environment around an ego-vehicle evolves with time. Ego-centric perception of driveable regions in a scene not only changes with the motion of actors in the environment, but also with the movement of the ego-vehicle itself. Self-supervised representations proposed for large-scale planning, such as ego-centric freespace, confound these two motions, making the representation difficult to use for downstream motion planners. In this paper, we use geometric occupancy as a natural alternative to view-dependent representations such as freespace. Occupancy maps naturally disentangle the motion of the environment from the motion of the ego-vehicle. However, one cannot directly observe the full 3D occupancy of a scene (due to occlusion), making it difficult to use as a signal for learning. Our key insight is to use differentiable raycasting to "render" future occupancy predictions into future LiDAR sweep predictions, which can be compared with ground-truth sweeps for self-supervised learning. The use of differentiable raycasting allows occupancy to emerge as an internal representation within the forecasting network. In the absence of groundtruth occupancy, we quantitatively evaluate the forecasting of raycasted LiDAR sweeps and show improvements of upto 15 F1 points. For downstream motion planners, where emergent occupancy can be directly used to guide non-driveable regions, this representation relatively reduces the number of collisions with objects by up to 17% as compared to freespace-centric motion planners.

</details>

### KD-MVS: Knowledge Distillation Based Self-supervised Learning for Multi-view Stereo.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_36) · 📚 被引 31
- **作者**: Yikang Ding, Qingtian Zhu, Xiangyue Liu, Wentao Yuan, Haotian Zhang, Chi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### MvDeCor: Multi-view Dense Correspondence Learning for Fine-Grained 3D Segmentation.
- **链接**: [arXiv:2208.08580](https://arxiv.org/abs/2208.08580) · 📚 被引 10
- **作者**: Gopal Sharma, Kangxue Yin, Subhransu Maji, Evangelos Kalogerakis, Or Litany, Sanja Fidler
- **🏷️ 机构**: NVIDIA / University of Toronto
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose to utilize self-supervised techniques in the 2D domain for fine-grained 3D shape segmentation tasks. This is inspired by the observation that view-based surface representations are more effective at modeling high-resolution surface details and texture than their 3D counterparts based on point clouds or voxel occupancy. Specifically, given a 3D shape, we render it from multiple views, and set up a dense correspondence learning task within the contrastive learning framework. As a result, the learned 2D representations are view-invariant and geometrically consistent, leading to better generalization when trained on a limited number of labeled shapes compared to alternatives that utilize self-supervision in 2D or 3D alone. Experiments on textured (RenderPeople) and untextured (PartNet) 3D datasets show that our method outperforms state-of-the-art alternatives in fine-grained part segmentation. The improvements over baselines are greater when only a sparse set of views is available for training or when shapes are textured, indicating that MvDeCor benefits from both 2D processing and 3D geometric reasoning.

</details>

### DevNet: Self-supervised Monocular Depth Learning via Density Volume Construction.
- **链接**: [arXiv:2209.06351](https://arxiv.org/abs/2209.06351) · 📚 被引 26
- **作者**: Kaichen Zhou, Lanqing Hong, Changhao Chen, Hang Xu, Chaoqiang Ye, Qingyong Hu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised depth learning from monocular images normally relies on the 2D pixel-wise photometric relation between temporally adjacent image frames. However, they neither fully exploit the 3D point-wise geometric correspondences, nor effectively tackle the ambiguities in the photometric warping caused by occlusions or illumination inconsistency. To address these problems, this work proposes Density Volume Construction Network (DevNet), a novel self-supervised monocular depth learning framework, that can consider 3D spatial information, and exploit stronger geometric constraints among adjacent camera frustums. Instead of directly regressing the pixel value from a single image, our DevNet divides the camera frustum into multiple parallel planes and predicts the pointwise occlusion probability density on each plane. The final depth map is generated by integrating the density along corresponding rays. During the training process, novel regularization strategies and loss functions are introduced to mitigate photometric ambiguities and overfitting. Without obviously enlarging model parameters size or running time, DevNet outperforms several representative baselines on both the KITTI-2015 outdoor dataset and NYU-V2 indoor dataset. In particular, the root-mean-square-deviation is reduced by around 4% with DevNet on both KITTI-2015 and NYU-V2 in the task of depth estimation. Code is available at https://github.com/gitkaichenzhou/DevNet.

</details>

### Hierarchically Self-supervised Transformer for Human Skeleton Representation Learning.
- **链接**: [arXiv:2207.09644](https://arxiv.org/abs/2207.09644)
- **作者**: Yuxiao Chen, Long Zhao, Jianbo Yuan, Yu Tian, Zhaoyang Xia, Shijie Geng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the success of fully-supervised human skeleton sequence modeling, utilizing self-supervised pre-training for skeleton sequence representation learning has been an active field because acquiring task-specific skeleton annotations at large scales is difficult. Recent studies focus on learning video-level temporal and discriminative information using contrastive learning, but overlook the hierarchical spatial-temporal nature of human skeletons. Different from such superficial supervision at the video level, we propose a self-supervised hierarchical pre-training scheme incorporated into a hierarchical Transformer-based skeleton sequence encoder (Hi-TRS), to explicitly capture spatial, short-term, and long-term temporal dependencies at frame, clip, and video levels, respectively. To evaluate the proposed self-supervised pre-training scheme with Hi-TRS, we conduct extensive experiments covering three skeleton-based downstream tasks including action recognition, action detection, and motion prediction. Under both supervised and semi-supervised evaluation protocols, our method achieves the state-of-the-art performance. Additionally, we demonstrate that the prior knowledge learned by our model in the pre-training stage has strong transfer capability for different downstream tasks.

</details>

### Towards Efficient and Effective Self-supervised Learning of Visual Representations.
- **链接**: [arXiv:2210.09866](https://arxiv.org/abs/2210.09866)
- **作者**: Sravanti Addepalli, Kaushal Bhogale, Priyam Dey, R. Venkatesh Babu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervision has emerged as a propitious method for visual representation learning after the recent paradigm shift from handcrafted pretext tasks to instance-similarity based approaches. Most state-of-the-art methods enforce similarity between various augmentations of a given image, while some methods additionally use contrastive approaches to explicitly ensure diverse representations. While these approaches have indeed shown promising direction, they require a significantly larger number of training iterations when compared to the supervised counterparts. In this work, we explore reasons for the slow convergence of these methods, and further propose to strengthen them using well-posed auxiliary tasks that converge significantly faster, and are also useful for representation learning. The proposed method utilizes the task of rotation prediction to improve the efficiency of existing state-of-the-art methods. We demonstrate significant gains in performance using the proposed method on multiple datasets, specifically for lower training epochs.

</details>

### Self-Supervised Classification Network.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_7)
- **作者**: Elad Amrani, Leonid Karlinsky, Alexander M. Bronstein
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Synergistic Self-supervised and Quantization Learning.
- **链接**: [arXiv:2207.05432](https://arxiv.org/abs/2207.05432)
- **作者**: Yun-Hao Cao, Peiqin Sun, Yechang Huang, Jianxin Wu, Shuchang Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the success of self-supervised learning (SSL), it has become a mainstream paradigm to fine-tune from self-supervised pretrained models to boost the performance on downstream tasks. However, we find that current SSL models suffer severe accuracy drops when performing low-bit quantization, prohibiting their deployment in resource-constrained applications. In this paper, we propose a method called synergistic self-supervised and quantization learning (SSQL) to pretrain quantization-friendly self-supervised models facilitating downstream deployment. SSQL contrasts the features of the quantized and full precision models in a self-supervised fashion, where the bit-width for the quantized model is randomly selected in each step. SSQL not only significantly improves the accuracy when quantized to lower bit-widths, but also boosts the accuracy of full precision models in most cases. By only training once, SSQL can then benefit various downstream tasks at different bit-widths simultaneously. Moreover, the bit-width flexibility is achieved without additional storage overhead, requiring only one copy of weights during training and inference. We theoretically analyze the optimization process of SSQL, and conduct exhaustive experiments on various benchmarks to further demonstrate the effectiveness of our method. Our code is available at https://github.com/megvii-research/SSQL-ECCV2022.

</details>

### Sound Localization by Self-supervised Time Delay Estimation.
- **链接**: [arXiv:2204.12489](https://arxiv.org/abs/2204.12489) · 📚 被引 13
- **作者**: Ziyang Chen, David F. Fouhey, Andrew Owens
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sounds reach one microphone in a stereo pair sooner than the other, resulting in an interaural time delay that conveys their directions. Estimating a sound's time delay requires finding correspondences between the signals recorded by each microphone. We propose to learn these correspondences through self-supervision, drawing on recent techniques from visual tracking. We adapt the contrastive random walk of Jabri et al. to learn a cycle-consistent representation from unlabeled stereo sounds, resulting in a model that performs on par with supervised methods on "in the wild" internet recordings. We also propose a multimodal contrastive learning model that solves a visually-guided localization task: estimating the time delay for a particular person in a multi-speaker mixture, given a visual representation of their face. Project site: https://ificl.github.io/stereocrw/

</details>

### GOCA: Guided Online Cluster Assignment for Self-supervised Video Representation Learning.
- **链接**: [arXiv:2207.10158](https://arxiv.org/abs/2207.10158) · 📚 被引 4
- **作者**: Huseyin Coskun, Alireza Zareian, Joshua L. Moore, Federico Tombari, Chen Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Clustering is a ubiquitous tool in unsupervised learning. Most of the existing self-supervised representation learning methods typically cluster samples based on visually dominant features. While this works well for image-based self-supervision, it often fails for videos, which require understanding motion rather than focusing on background. Using optical flow as complementary information to RGB can alleviate this problem. However, we observe that a naive combination of the two views does not provide meaningful gains. In this paper, we propose a principled way to combine two views. Specifically, we propose a novel clustering strategy where we use the initial cluster assignment of each view as prior to guide the final cluster assignment of the other view. This idea will enforce similar cluster structures for both views, and the formed clusters will be semantically abstract and robust to noisy inputs coming from each individual view. Additionally, we propose a novel regularization strategy to address the feature collapse problem, which is common in cluster-based self-supervised learning methods. Our extensive evaluation shows the effectiveness of our learned representations on downstream tasks, e.g., video retrieval and action recognition. Specifically, we outperform the state of the art by 7% on UCF and 4% on HMDB for video retrieval, and 5% on UCF and 6% on HMDB for video classification

</details>

### Trust, but Verify: Using Self-supervised Probing to Improve Trustworthiness.
- **链接**: [arXiv:2302.02628](https://arxiv.org/abs/2302.02628)
- **作者**: Ailin Deng, Shen Li, Miao Xiong, Zhirui Chen, Bryan Hooi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Trustworthy machine learning is of primary importance to the practical deployment of deep learning models. While state-of-the-art models achieve astonishingly good performance in terms of accuracy, recent literature reveals that their predictive confidence scores unfortunately cannot be trusted: e.g., they are often overconfident when wrong predictions are made, or so even for obvious outliers. In this paper, we introduce a new approach of self-supervised probing, which enables us to check and mitigate the overconfidence issue for a trained model, thereby improving its trustworthiness. We provide a simple yet effective framework, which can be flexibly applied to existing trustworthiness-related methods in a plug-and-play manner. Extensive experiments on three trustworthiness-related tasks (misclassification detection, calibration and out-of-distribution detection) across various benchmarks verify the effectiveness of our proposed probing framework.

</details>

### SOS! Self-supervised Learning over Sets of Handled Objects in Egocentric Action Recognition.
- **链接**: [arXiv:2204.04796](https://arxiv.org/abs/2204.04796)
- **作者**: Victor Escorcia, Ricardo Guerrero, Xiatian Zhu, Brais Martínez
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning an egocentric action recognition model from video data is challenging due to distractors (e.g., irrelevant objects) in the background. Further integrating object information into an action model is hence beneficial. Existing methods often leverage a generic object detector to identify and represent the objects in the scene. However, several important issues remain. Object class annotations of good quality for the target domain (dataset) are still required for learning good object representation. Besides, previous methods deeply couple the existing action models and need to retrain them jointly with object representation, leading to costly and inflexible integration. To overcome both limitations, we introduce Self-Supervised Learning Over Sets (SOS), an approach to pre-train a generic Objects In Contact (OIC) representation model from video object regions detected by an off-the-shelf hand-object contact detector. Instead of augmenting object regions individually as in conventional self-supervised learning, we view the action process as a means of natural data transformations with unique spatio-temporal continuity and exploit the inherent relationships among per-video object sets. Extensive experiments on two datasets, EPIC-KITCHENS-100 and EGTEA, show that our OIC significantly boosts the performance of multiple state-of-the-art video classification models.

</details>

### DisCo: Remedying Self-supervised Learning on Lightweight Models with Distilled Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_14) · 📚 被引 32
- **作者**: Yuting Gao, Jia-Xin Zhuang, Shaohui Lin, Hao Cheng, Xing Sun, Ke Li et al.
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

### Self-supervised Human Mesh Recovery with Cross-Representation Alignment.
- **链接**: [arXiv:2209.04596](https://arxiv.org/abs/2209.04596) · 📚 被引 8
- **作者**: Xuan Gong, Meng Zheng, Benjamin Planche, Srikrishna Karanam, Terrence Chen, David S. Doermann et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fully supervised human mesh recovery methods are data-hungry and have poor generalizability due to the limited availability and diversity of 3D-annotated benchmark datasets. Recent progress in self-supervised human mesh recovery has been made using synthetic-data-driven training paradigms where the model is trained from synthetic paired 2D representation (e.g., 2D keypoints and segmentation masks) and 3D mesh. However, on synthetic dense correspondence maps (i.e., IUV) few have been explored since the domain gap between synthetic training data and real testing data is hard to address for 2D dense representation. To alleviate this domain gap on IUV, we propose cross-representation alignment utilizing the complementary information from the robust but sparse representation (2D keypoints). Specifically, the alignment errors between initial mesh estimation and both 2D representations are forwarded into regressor and dynamically corrected in the following mesh regression. This adaptive cross-representation alignment explicitly learns from the deviations and captures complementary information: robustness from sparse representation and richness from dense representation. We conduct extensive experiments on multiple standard benchmark datasets and demonstrate competitive results, helping take a step towards reducing the annotation effort needed to produce state-of-the-art models in human mesh estimation.

</details>

### Generative Subgraph Contrast for Self-Supervised Graph Representation Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20056-4_6) · 📚 被引 13
- **作者**: Yuehui Han, Le Hui, Haobo Jiang, Jianjun Qian, Jin Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### GeoRefine: Self-supervised Online Depth Refinement for Accurate Dense Mapping.
- **链接**: [arXiv:2205.01656](https://arxiv.org/abs/2205.01656)
- **作者**: Pan Ji, Qingan Yan, Yuxin Ma, Yi Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a robust and accurate depth refinement system, named GeoRefine, for geometrically-consistent dense mapping from monocular sequences. GeoRefine consists of three modules: a hybrid SLAM module using learning-based priors, an online depth refinement module leveraging self-supervision, and a global mapping module via TSDF fusion. The proposed system is online by design and achieves great robustness and accuracy via: (i) a robustified hybrid SLAM that incorporates learning-based optical flow and/or depth; (ii) self-supervised losses that leverage SLAM outputs and enforce long-term geometric consistency; (iii) careful system design that avoids degenerate cases in online depth refinement. We extensively evaluate GeoRefine on multiple public datasets and reach as low as $5\%$ absolute relative depth errors.

</details>

### MoDA: Map Style Transfer for Self-supervised Domain Adaptation of Embodied Agents.
- **链接**: [arXiv:2211.15992](https://arxiv.org/abs/2211.15992) · 📚 被引 4
- **作者**: Eun Sun Lee, Junho Kim, SangWon Park, Young Min Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a domain adaptation method, MoDA, which adapts a pretrained embodied agent to a new, noisy environment without ground-truth supervision. Map-based memory provides important contextual information for visual navigation, and exhibits unique spatial structure mainly composed of flat walls and rectangular obstacles. Our adaptation approach encourages the inherent regularities on the estimated maps to guide the agent to overcome the prevalent domain discrepancy in a novel environment. Specifically, we propose an efficient learning curriculum to handle the visual and dynamics corruptions in an online manner, self-supervised with pseudo clean maps generated by style transfer networks. Because the map-based representation provides spatial knowledge for the agent's policy, our formulation can deploy the pretrained policy networks from simulators in a new setting. We evaluate MoDA in various practical scenarios and show that our proposed method quickly enhances the agent's performance in downstream tasks including localization, mapping, exploration, and point-goal navigation.

</details>

### A Closer Look at Invariances in Self-supervised Pre-training for 3D Vision.
- **链接**: [arXiv:2207.04997](https://arxiv.org/abs/2207.04997) · 📚 被引 21
- **作者**: Lanxiao Li, Michael Heizmann
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised pre-training for 3D vision has drawn increasing research interest in recent years. In order to learn informative representations, a lot of previous works exploit invariances of 3D features, e.g., perspective-invariance between views of the same scene, modality-invariance between depth and RGB images, format-invariance between point clouds and voxels. Although they have achieved promising results, previous researches lack a systematic and fair comparison of these invariances. To address this issue, our work, for the first time, introduces a unified framework, under which various pre-training methods can be investigated. We conduct extensive experiments and provide a closer look at the contributions of different invariances in 3D pre-training. Also, we propose a simple but effective method that jointly pre-trains a 3D encoder and a depth map encoder using contrastive learning. Models pre-trained with our method gain significant performance boost in downstream tasks. For instance, a pre-trained VoteNet outperforms previous methods on SUN RGB-D and ScanNet object detection benchmarks with a clear margin.

</details>

### Self-supervised Social Relation Representation for Human Group Detection.
- **链接**: [arXiv:2203.03843](https://arxiv.org/abs/2203.03843) · 📚 被引 12
- **作者**: Jiacheng Li, Ruize Han, Haomin Yan, Zekun Qian, Wei Feng, Song Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human group detection, which splits crowd of people into groups, is an important step for video-based human social activity analysis. The core of human group detection is the human social relation representation and division.In this paper, we propose a new two-stage multi-head framework for human group detection. In the first stage, we propose a human behavior simulator head to learn the social relation feature embedding, which is self-supervisely trained by leveraging the socially grounded multi-person behavior relationship. In the second stage, based on the social relation embedding, we develop a self-attention inspired network for human group detection. Remarkable performance on two state-of-the-art large-scale benchmarks, i.e., PANDA and JRDB-Group, verifies the effectiveness of the proposed framework. Benefiting from the self-supervised social relation embedding, our method can provide promising results with very few (labeled) training data. We will release the source code to the public.

</details>

### Fusion from Decomposition: A Self-Supervised Decomposition Approach for Image Fusion.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19797-0_41) · 📚 被引 151
- **作者**: Pengwei Liang, Junjun Jiang, Xianming Liu, Jiayi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Category-Level 6D Object Pose and Size Estimation Using Self-supervised Deep Prior Deformation Networks.
- **链接**: [arXiv:2207.05444](https://arxiv.org/abs/2207.05444) · 📚 被引 82
- **作者**: Jiehong Lin, Zewei Wei, Changxing Ding, Kui Jia
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It is difficult to precisely annotate object instances and their semantics in 3D space, and as such, synthetic data are extensively used for these tasks, e.g., category-level 6D object pose and size estimation. However, the easy annotations in synthetic domains bring the downside effect of synthetic-to-real (Sim2Real) domain gap. In this work, we aim to address this issue in the task setting of Sim2Real, unsupervised domain adaptation for category-level 6D object pose and size estimation. We propose a method that is built upon a novel Deep Prior Deformation Network, shortened as DPDN. DPDN learns to deform features of categorical shape priors to match those of object observations, and is thus able to establish deep correspondence in the feature space for direct regression of object poses and sizes. To reduce the Sim2Real domain gap, we formulate a novel self-supervised objective upon DPDN via consistency learning; more specifically, we apply two rigid transformations to each object observation in parallel, and feed them into DPDN respectively to yield dual sets of predictions; on top of the parallel learning, an inter-consistency term is employed to keep cross consistency between dual predictions for improving the sensitivity of DPDN to pose changes, while individual intra-consistency ones are used to enforce self-adaptation within each learning itself. We train DPDN on both training sets of the synthetic CAMERA25 and real-world REAL275 datasets; our results outperform the existing methods on REAL275 test set under both the unsupervised and supervised settings. Ablation studies also verify the efficacy of our designs. Our code is released publicly at https://github.com/JiehongLin/Self-DPDN.

</details>

### Source-Free Domain Adaptation with Contrastive Domain Alignment and Self-supervised Exploration for Face Anti-spoofing.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19775-8_30) · 📚 被引 45
- **作者**: Yuchen Liu, Yabo Chen, Wenrui Dai, Mengran Gou, Chun-Ting Huang, Hongkai Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Improving Self-supervised Lightweight Model Learning via Hard-Aware Metric Distillation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_17) · 📚 被引 5
- **作者**: Hao Liu, Mang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Self-supervised Learning of Visual Graph Matching.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20050-2_22)
- **作者**: Chang Liu, Shaofeng Zhang, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Motion Sensitive Contrastive Learning for Self-supervised Video Representation.
- **链接**: [arXiv:2208.06105](https://arxiv.org/abs/2208.06105)
- **作者**: Jingcheng Ni, Nan Zhou, Jie Qin, Qian Wu, Junqi Liu, Boxun Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has shown great potential in video representation learning. However, existing approaches fail to sufficiently exploit short-term motion dynamics, which are crucial to various down-stream video understanding tasks. In this paper, we propose Motion Sensitive Contrastive Learning (MSCL) that injects the motion information captured by optical flows into RGB frames to strengthen feature learning. To achieve this, in addition to clip-level global contrastive learning, we develop Local Motion Contrastive Learning (LMCL) with frame-level contrastive objectives across the two modalities. Moreover, we introduce Flow Rotation Augmentation (FRA) to generate extra motion-shuffled negative samples and Motion Differential Sampling (MDS) to accurately screen training samples. Extensive experiments on standard benchmarks validate the effectiveness of the proposed method. With the commonly-used 3D ResNet-18 as the backbone, we achieve the top-1 accuracies of 91.5\% on UCF101 and 50.3\% on Something-Something v2 for video classification, and a 65.6\% Top-1 Recall on UCF101 for video retrieval, notably improving the state-of-the-art.

</details>

### Domain Knowledge-Informed Self-supervised Representations for Workout Form Assessment.
- **链接**: [arXiv:2202.14019](https://arxiv.org/abs/2202.14019) · 📚 被引 20
- **作者**: Paritosh Parmar, Amol Gharat, Helge Rhodin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Maintaining proper form while exercising is important for preventing injuries and maximizing muscle mass gains. Detecting errors in workout form naturally requires estimating human's body pose. However, off-the-shelf pose estimators struggle to perform well on the videos recorded in gym scenarios due to factors such as camera angles, occlusion from gym equipment, illumination, and clothing. To aggravate the problem, the errors to be detected in the workouts are very subtle. To that end, we propose to learn exercise-oriented image and video representations from unlabeled samples such that a small dataset annotated by experts suffices for supervised error detection. In particular, our domain knowledge-informed self-supervised approaches (pose contrastive learning and motion disentangling) exploit the harmonic motion of the exercise actions, and capitalize on the large variances in camera angles, clothes, and illumination to learn powerful representations. To facilitate our self-supervised pretraining, and supervised finetuning, we curated a new exercise dataset, Fitness-AQA (https://github.com/ParitoshParmar/Fitness-AQA), comprising of three exercises: BackSquat, BarbellRow, and OverheadPress. It has been annotated by expert trainers for multiple crucial and typically occurring exercise errors. Experimental results show that our self-supervised representations outperform off-the-shelf 2D- and 3D-pose estimators and several other baselines. We also show that our approaches can be applied to other domains/tasks such as pose estimation and dive quality assessment.

</details>

### The Challenges of Continuous Self-Supervised Learning.
- **链接**: [arXiv:2203.12710](https://arxiv.org/abs/2203.12710)
- **作者**: Senthil Purushwalkam, Pedro Morgado, Abhinav Gupta
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) aims to eliminate one of the major bottlenecks in representation learning - the need for human annotations. As a result, SSL holds the promise to learn representations from data in-the-wild, i.e., without the need for finite and static datasets. Instead, true SSL algorithms should be able to exploit the continuous stream of data being generated on the internet or by agents exploring their environments. But do traditional self-supervised learning approaches work in this setup? In this work, we investigate this question by conducting experiments on the continuous self-supervised learning problem. While learning in the wild, we expect to see a continuous (infinite) non-IID data stream that follows a non-stationary distribution of visual concepts. The goal is to learn a representation that can be robust, adaptive yet not forgetful of concepts seen in the past. We show that a direct application of current methods to such continuous setup is 1) inefficient both computationally and in the amount of data required, 2) leads to inferior representations due to temporal correlations (non-IID data) in some sources of streaming data and 3) exhibits signs of catastrophic forgetting when trained on sources with non-stationary data distributions. We propose the use of replay buffers as an approach to alleviate the issues of inefficiency and temporal correlations. We further propose a novel method to enhance the replay buffer by maintaining the least redundant samples. Minimum redundancy (MinRed) buffers allow us to learn effective representations even in the most challenging streaming scenarios composed of sequential visual data obtained from a single embodied agent, and alleviates the problem of catastrophic forgetting when learning from data with non-stationary semantic distributions.

</details>

### Static and Dynamic Concepts for Self-supervised Video Representation Learning.
- **链接**: [arXiv:2207.12795](https://arxiv.org/abs/2207.12795) · 📚 被引 20
- **作者**: Rui Qian, Shuangrui Ding, Xian Liu, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel learning scheme for self-supervised video representation learning. Motivated by how humans understand videos, we propose to first learn general visual concepts then attend to discriminative local areas for video understanding. Specifically, we utilize static frame and frame difference to help decouple static and dynamic concepts, and respectively align the concept distributions in latent space. We add diversity and fidelity regularizations to guarantee that we learn a compact set of meaningful concepts. Then we employ a cross-attention mechanism to aggregate detailed local features of different concepts, and filter out redundant concepts with low activations to perform local concept contrast. Extensive experiments demonstrate that our method distills meaningful static and dynamic concepts to guide video understanding, and obtains state-of-the-art results on UCF-101, HMDB-51, and Diving-48.

</details>

### Dual-Domain Self-supervised Learning and Model Adaption for Deep Compressive Imaging.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20056-4_24) · 📚 被引 11
- **作者**: Yuhui Quan, Xinran Qin, Tongyao Pang, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Federated Self-supervised Learning for Video Understanding.
- **链接**: [arXiv:2207.01975](https://arxiv.org/abs/2207.01975)
- **作者**: Yasar Abbas Ur Rehman, Yan Gao, Jiajun Shen, Pedro Porto Buarque de Gusmão, Nicholas D. Lane
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ubiquity of camera-enabled mobile devices has lead to large amounts of unlabelled video data being produced at the edge. Although various self-supervised learning (SSL) methods have been proposed to harvest their latent spatio-temporal representations for task-specific training, practical challenges including privacy concerns and communication costs prevent SSL from being deployed at large scales. To mitigate these issues, we propose the use of Federated Learning (FL) to the task of video SSL. In this work, we evaluate the performance of current state-of-the-art (SOTA) video-SSL techniques and identify their shortcomings when integrated into the large-scale FL setting simulated with kinetics-400 dataset. We follow by proposing a novel federated SSL framework for video, dubbed FedVSSL, that integrates different aggregation strategies and partial weight updating. Extensive experiments demonstrate the effectiveness and significance of FedVSSL as it outperforms the centralized SOTA for the downstream retrieval task by 6.66% on UCF-101 and 5.13% on HMDB-51.

</details>

### Completely Self-supervised Crowd Counting via Distribution Matching.
- **链接**: [arXiv:2009.06420](https://arxiv.org/abs/2009.06420) · 📚 被引 19
- **作者**: Deepak Babu Sam, Abhinav Agarwalla, Jimmy Joseph, Vishwanath A. Sindagi, R. Venkatesh Babu, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dense crowd counting is a challenging task that demands millions of head annotations for training models. Though existing self-supervised approaches could learn good representations, they require some labeled data to map these features to the end task of density estimation. We mitigate this issue with the proposed paradigm of complete self-supervision, which does not need even a single labeled image. The only input required to train, apart from a large set of unlabeled crowd images, is the approximate upper limit of the crowd count for the given dataset. Our method dwells on the idea that natural crowds follow a power law distribution, which could be leveraged to yield error signals for backpropagation. A density regressor is first pretrained with self-supervision and then the distribution of predictions is matched to the prior by optimizing Sinkhorn distance between the two. Experiments show that this results in effective learning of crowd features and delivers significant counting performance. Furthermore, we establish the superiority of our method in less data setting as well. The code and models for our approach is available at https://github.com/val-iisc/css-ccnn.

</details>

### Natural Synthetic Anomalies for Self-supervised Anomaly Detection and Localization.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_27)
- **作者**: Hannah M. Schlüter, Jeremy Tan, Benjamin Hou, Bernhard Kainz
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Social-SSL: Self-supervised Cross-Sequence Representation Learning Based on Transformers for Multi-agent Trajectory Prediction.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20047-2_14) · 📚 被引 26
- **作者**: Li-Wu Tsao, Yan-Kai Wang, Hao-Siang Lin, Hong-Han Shuai, Lai-Kuan Wong, Wen-Huang Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Self-supervised Sparse Representation for Video Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19778-9_42)
- **作者**: Jhih-Ciang Wu, He-Yen Hsieh, Ding-Jie Chen, Chiou-Shann Fuh, Tyng-Luh Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### PreTraM: Self-supervised Pre-training via Connecting Trajectory and Map.
- **链接**: [arXiv:2204.10435](https://arxiv.org/abs/2204.10435)
- **作者**: Chenfeng Xu, Tian Li, Chen Tang, Lingfeng Sun, Kurt Keutzer, Masayoshi Tomizuka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning has recently achieved significant progress in trajectory forecasting. However, the scarcity of trajectory data inhibits the data-hungry deep-learning models from learning good representations. While mature representation learning methods exist in computer vision and natural language processing, these pre-training methods require large-scale data. It is hard to replicate these approaches in trajectory forecasting due to the lack of adequate trajectory data (e.g., 34K samples in the nuScenes dataset). To work around the scarcity of trajectory data, we resort to another data modality closely related to trajectories-HD-maps, which is abundantly provided in existing datasets. In this paper, we propose PreTraM, a self-supervised pre-training scheme via connecting trajectories and maps for trajectory forecasting. Specifically, PreTraM consists of two parts: 1) Trajectory-Map Contrastive Learning, where we project trajectories and maps to a shared embedding space with cross-modal contrastive learning, and 2) Map Contrastive Learning, where we enhance map representation with contrastive learning on large quantities of HD-maps. On top of popular baselines such as AgentFormer and Trajectron++, PreTraM boosts their performance by 5.5% and 6.9% relatively in FDE-10 on the challenging nuScenes dataset. We show that PreTraM improves data efficiency and scales well with model size.

</details>

### RegionCL: Exploring Contrastive Region Pairs for Self-supervised Representation Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19827-4_28) · 📚 被引 7
- **作者**: Yufei Xu, Qiming Zhang, Jing Zhang, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Domain Invariant Masked Autoencoders for Self-supervised Learning from Multi-domains.
- **链接**: [arXiv:2205.04771](https://arxiv.org/abs/2205.04771) · 📚 被引 14
- **作者**: Haiyang Yang, Shixiang Tang, Meilin Chen, Yizhou Wang, Feng Zhu, Lei Bai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalizing learned representations across significantly different visual domains is a fundamental yet crucial ability of the human visual system. While recent self-supervised learning methods have achieved good performances with evaluation set on the same domain as the training set, they will have an undesirable performance decrease when tested on a different domain. Therefore, the self-supervised learning from multiple domains task is proposed to learn domain-invariant features that are not only suitable for evaluation on the same domain as the training set but also can be generalized to unseen domains. In this paper, we propose a Domain-invariant Masked AutoEncoder (DiMAE) for self-supervised learning from multi-domains, which designs a new pretext task, \emph{i.e.,} the cross-domain reconstruction task, to learn domain-invariant features. The core idea is to augment the input image with style noise from different domains and then reconstruct the image from the embedding of the augmented image, regularizing the encoder to learn domain-invariant features. To accomplish the idea, DiMAE contains two critical designs, 1) content-preserved style mix, which adds style information from other domains to input while persevering the content in a parameter-free manner, and 2) multiple domain-specific decoders, which recovers the corresponding domain style of input to the encoded domain-invariant features for reconstruction. Experiments on PACS and DomainNet illustrate that DiMAE achieves considerable gains compared with recent state-of-the-art methods.

</details>

### PT4AL: Using Self-supervised Pretext Tasks for Active Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_34)
- **作者**: John Seon Keun Yi, Minseok Seo, Jongchan Park, Dong-Geol Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Self-supervised Interactive Object Segmentation Through a Singulation-and-Grasping Approach.
- **链接**: [arXiv:2207.09314](https://arxiv.org/abs/2207.09314) · 📚 被引 12
- **作者**: Houjian Yu, Changhyun Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Instance segmentation with unseen objects is a challenging problem in unstructured environments. To solve this problem, we propose a robot learning approach to actively interact with novel objects and collect each object's training label for further fine-tuning to improve the segmentation model performance, while avoiding the time-consuming process of manually labeling a dataset. The Singulation-and-Grasping (SaG) policy is trained through end-to-end reinforcement learning. Given a cluttered pile of objects, our approach chooses pushing and grasping motions to break the clutter and conducts object-agnostic grasping for which the SaG policy takes as input the visual observations and imperfect segmentation. We decompose the problem into three subtasks: (1) the object singulation subtask aims to separate the objects from each other, which creates more space that alleviates the difficulty of (2) the collision-free grasping subtask; (3) the mask generation subtask to obtain the self-labeled ground truth masks by using an optical flow-based binary classifier and motion cue post-processing for transfer learning. Our system achieves 70% singulation success rate in simulated cluttered scenes. The interactive segmentation of our system achieves 87.8%, 73.9%, and 69.3% average precision for toy blocks, YCB objects in simulation and real-world novel objects, respectively, which outperforms several baselines.

</details>

### Self-supervised Learning for Real-World Super-Resolution from Dual Zoomed Observations.
- **链接**: [arXiv:2203.01325](https://arxiv.org/abs/2203.01325)
- **作者**: Zhilu Zhang, Ruohao Wang, Hongzhi Zhang, Yunjin Chen, Wangmeng Zuo
- **🏷️ 机构**: Faculty of Computing, Harbin Institute of Technology, Harbin, Heilongjiang, China
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we consider two challenging issues in reference-based super-resolution (RefSR), (i) how to choose a proper reference image, and (ii) how to learn real-world RefSR in a self-supervised manner. Particularly, we present a novel self-supervised learning approach for real-world image SR from observations at dual camera zooms (SelfDZSR). Considering the popularity of multiple cameras in modern smartphones, the more zoomed (telephoto) image can be naturally leveraged as the reference to guide the SR of the lesser zoomed (short-focus) image. Furthermore, SelfDZSR learns a deep network to obtain the SR result of short-focus image to have the same resolution as the telephoto image. For this purpose, we take the telephoto image instead of an additional high-resolution image as the supervision information and select a center patch from it as the reference to super-resolve the corresponding short-focus image patch. To mitigate the effect of the misalignment between short-focus low-resolution (LR) image and telephoto ground-truth (GT) image, we design an auxiliary-LR generator and map the GT to an auxiliary-LR while keeping the spatial position unchanged. Then the auxiliary-LR can be utilized to deform the LR features by the proposed adaptive spatial transformer networks (AdaSTN), and match the Ref features to GT. During testing, SelfDZSR can be directly deployed to super-solve the whole short-focus image with the reference of telephoto image. Experiments show that our method achieves better quantitative and qualitative performance against state-of-the-arts. Codes are available at https://github.com/cszhilu1998/SelfDZSR.

</details>

### Decoupled Adversarial Contrastive Learning for Self-supervised Adversarial Robustness.
- **链接**: [arXiv:2207.10899](https://arxiv.org/abs/2207.10899)
- **作者**: Chaoning Zhang, Kang Zhang, Chenshuang Zhang, Axi Niu, Jiu Feng, Chang D. Yoo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial training (AT) for robust representation learning and self-supervised learning (SSL) for unsupervised representation learning are two active research fields. Integrating AT into SSL, multiple prior works have accomplished a highly significant yet challenging task: learning robust representation without labels. A widely used framework is adversarial contrastive learning which couples AT and SSL, and thus constitute a very complex optimization problem. Inspired by the divide-and-conquer philosophy, we conjecture that it might be simplified as well as improved by solving two sub-problems: non-robust SSL and pseudo-supervised AT. This motivation shifts the focus of the task from seeking an optimal integrating strategy for a coupled problem to finding sub-solutions for sub-problems. With this said, this work discards prior practices of directly introducing AT to SSL frameworks and proposed a two-stage framework termed Decoupled Adversarial Contrastive Learning (DeACL). Extensive experimental results demonstrate that our DeACL achieves SOTA self-supervised adversarial robustness while significantly reducing the training time, which validates its effectiveness and efficiency. Moreover, our DeACL constitutes a more explainable solution, and its success also bridges the gap with semi-supervised AT for exploiting unlabeled samples for robust representation learning. The code is publicly accessible at https://github.com/pantheon5100/DeACL.

</details>

### PASS: Part-Aware Self-Supervised Pre-Training for Person Re-Identification.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19781-9_12) · 📚 被引 80
- **作者**: Kuan Zhu, Haiyun Guo, Tianyi Yan, Yousong Zhu, Jinqiao Wang, Ming Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### SPot-the-Difference Self-supervised Pre-training for Anomaly Detection and Segmentation.
- **链接**: [arXiv:2207.14315](https://arxiv.org/abs/2207.14315) · 📚 被引 523
- **作者**: Yang Zou, Jongheon Jeong, Latha Pemula, Dongqing Zhang, Onkar Dabeer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual anomaly detection is commonly used in industrial quality inspection. In this paper, we present a new dataset as well as a new self-supervised learning method for ImageNet pre-training to improve anomaly detection and segmentation in 1-class and 2-class 5/10/high-shot training setups. We release the Visual Anomaly (VisA) Dataset consisting of 10,821 high-resolution color images (9,621 normal and 1,200 anomalous samples) covering 12 objects in 3 domains, making it the largest industrial anomaly detection dataset to date. Both image and pixel-level labels are provided. We also propose a new self-supervised framework - SPot-the-difference (SPD) - which can regularize contrastive self-supervised pre-training, such as SimSiam, MoCo and SimCLR, to be more suitable for anomaly detection tasks. Our experiments on VisA and MVTec-AD dataset show that SPD consistently improves these contrastive pre-training baselines and even the supervised pre-training. For example, SPD improves Area Under the Precision-Recall curve (AU-PR) for anomaly segmentation by 5.9% and 6.8% over SimSiam and supervised pre-training respectively in the 2-class high-shot regime. We open-source the project at http://github.com/amazon-research/spot-diff .

</details>

### 4DContrast: Contrastive Learning with Dynamic Correspondences for 3D Scene Understanding.
- **链接**: [arXiv:2112.02990](https://arxiv.org/abs/2112.02990)
- **作者**: Yujin Chen, Matthias Nießner, Angela Dai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a new approach to instill 4D dynamic object priors into learned 3D representations by unsupervised pre-training. We observe that dynamic movement of an object through an environment provides important cues about its objectness, and thus propose to imbue learned 3D representations with such dynamic understanding, that can then be effectively transferred to improved performance in downstream 3D semantic scene understanding tasks. We propose a new data augmentation scheme leveraging synthetic 3D shapes moving in static 3D environments, and employ contrastive learning under 3D-4D constraints that encode 4D invariances into the learned 3D representations. Experiments demonstrate that our unsupervised representation learning results in improvement in downstream 3D semantic segmentation, object detection, and instance segmentation tasks, and moreover, notably improves performance in data-scarce scenarios.

</details>

### Fast-MoCo: Boost Momentum-Based Contrastive Learning with Combinatorial Patches.
- **链接**: [arXiv:2207.08220](https://arxiv.org/abs/2207.08220) · 📚 被引 19
- **作者**: Yuanzheng Ci, Chen Lin, Lei Bai, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive-based self-supervised learning methods achieved great success in recent years. However, self-supervision requires extremely long training epochs (e.g., 800 epochs for MoCo v3) to achieve promising results, which is unacceptable for the general academic community and hinders the development of this topic. This work revisits the momentum-based contrastive learning frameworks and identifies the inefficiency in which two augmented views generate only one positive pair. We propose Fast-MoCo - a novel framework that utilizes combinatorial patches to construct multiple positive pairs from two augmented views, which provides abundant supervision signals that bring significant acceleration with neglectable extra computational cost. Fast-MoCo trained with 100 epochs achieves 73.5% linear evaluation accuracy, similar to MoCo v3 (ResNet-50 backbone) trained with 800 epochs. Extra training (200 epochs) further improves the result to 75.1%, which is on par with state-of-the-art methods. Experiments on several downstream tasks also confirm the effectiveness of Fast-MoCo.

</details>

### Bi-directional Contrastive Learning for Domain Adaptive Semantic Segmentation.
- **链接**: [arXiv:2207.10892](https://arxiv.org/abs/2207.10892) · 📚 被引 29
- **作者**: Geon Lee, Chanho Eom, Wonkyung Lee, Hyekang Park, Bumsub Ham
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel unsupervised domain adaptation method for semantic segmentation that generalizes a model trained with source images and corresponding ground-truth labels to a target domain. A key to domain adaptive semantic segmentation is to learn domain-invariant and discriminative features without target ground-truth labels. To this end, we propose a bi-directional pixel-prototype contrastive learning framework that minimizes intra-class variations of features for the same object class, while maximizing inter-class variations for different ones, regardless of domains. Specifically, our framework aligns pixel-level features and a prototype of the same object class in target and source images (i.e., positive pairs), respectively, sets them apart for different classes (i.e., negative pairs), and performs the alignment and separation processes toward the other direction with pixel-level features in the source image and a prototype in the target image. The cross-domain matching encourages domain-invariant feature representations, while the bidirectional pixel-prototype correspondences aggregate features for the same object class, providing discriminative features. To establish training pairs for contrastive learning, we propose to generate dynamic pseudo labels of target images using a non-parametric label transfer, that is, pixel-prototype correspondences across different domains. We also present a calibration method compensating class-wise domain biases of prototypes gradually during training.

</details>

### Contrastive Learning for Diverse Disentangled Foreground Generation.
- **链接**: [arXiv:2211.02707](https://arxiv.org/abs/2211.02707)
- **作者**: Yuheng Li, Yijun Li, Jingwan Lu, Eli Shechtman, Yong Jae Lee, Krishna Kumar Singh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a new method for diverse foreground generation with explicit control over various factors. Existing image inpainting based foreground generation methods often struggle to generate diverse results and rarely allow users to explicitly control specific factors of variation (e.g., varying the facial identity or expression for face inpainting results). We leverage contrastive learning with latent codes to generate diverse foreground results for the same masked input. Specifically, we define two sets of latent codes, where one controls a pre-defined factor (``known''), and the other controls the remaining factors (``unknown''). The sampled latent codes from the two sets jointly bi-modulate the convolution kernels to guide the generator to synthesize diverse results. Experiments demonstrate the superiority of our method over state-of-the-arts in result diversity and generation controllability.

</details>

### FakeCLR: Exploring Contrastive Learning for Solving Latent Discontinuity in Data-Efficient GANs.
- **链接**: [arXiv:2207.08630](https://arxiv.org/abs/2207.08630) · 📚 被引 22
- **作者**: Ziqiang Li, Chaoyue Wang, Heliang Zheng, Jing Zhang, Bin Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data-Efficient GANs (DE-GANs), which aim to learn generative models with a limited amount of training data, encounter several challenges for generating high-quality samples. Since data augmentation strategies have largely alleviated the training instability, how to further improve the generative performance of DE-GANs becomes a hotspot. Recently, contrastive learning has shown the great potential of increasing the synthesis quality of DE-GANs, yet related principles are not well explored. In this paper, we revisit and compare different contrastive learning strategies in DE-GANs, and identify (i) the current bottleneck of generative performance is the discontinuity of latent space; (ii) compared to other contrastive learning strategies, Instance-perturbation works towards latent space continuity, which brings the major improvement to DE-GANs. Based on these observations, we propose FakeCLR, which only applies contrastive learning on perturbed fake samples, and devises three related training techniques: Noise-related Latent Augmentation, Diversity-aware Queue, and Forgetting Factor of Queue. Our experimental results manifest the new state of the arts on both few-shot generation and limited-data generation. On multiple datasets, FakeCLR acquires more than 15% FID improvement compared to existing DE-GANs. Code is available at https://github.com/iceli1007/FakeCLR.

</details>

### Pairwise Contrastive Learning Network for Action Quality Assessment.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19772-7_27) · 📚 被引 31
- **作者**: Mingzhe Li, Hongbo Zhang, Qing Lei, Zongwen Fan, Jinghua Liu, Ji-Xiang Du
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Multi-scale and Cross-scale Contrastive Learning for Semantic Segmentation.
- **链接**: [arXiv:2203.13409](https://arxiv.org/abs/2203.13409) · 📚 被引 25
- **作者**: Theodoros Pissas, Claudio S. Ravasio, Lyndon Da Cruz, Christos Bergeles
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work considers supervised contrastive learning for semantic segmentation. We apply contrastive learning to enhance the discriminative power of the multi-scale features extracted by semantic segmentation networks. Our key methodological insight is to leverage samples from the feature spaces emanating from multiple stages of a model's encoder itself requiring neither data augmentation nor online memory banks to obtain a diverse set of samples. To allow for such an extension we introduce an efficient and effective sampling process, that enables applying contrastive losses over the encoder's features at multiple scales. Furthermore, by first mapping the encoder's multi-scale representations to a common feature space, we instantiate a novel form of supervised local-global constraint by introducing cross-scale contrastive learning linking high-resolution local features to low-resolution global features. Combined, our multi-scale and cross-scale contrastive losses boost performance of various models (DeepLabV3, HRNet, OCRNet, UPerNet) with both CNN and Transformer backbones, when evaluated on 4 diverse datasets from natural (Cityscapes, PascalContext, ADE20K) but also surgical (CaDIS) domains. Our code is available at https://github.com/RViMLab/MS_CS_ContrSeg. datasets from natural (Cityscapes, PascalContext, ADE20K) but also surgical (CaDIS) domains.

</details>

### Network Binarization via Contrastive Learning.
- **链接**: [arXiv:2207.02970](https://arxiv.org/abs/2207.02970) · 📚 被引 22
- **作者**: Yuzhang Shang, Dan Xu, Ziliang Zong, Liqiang Nie, Yan Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural network binarization accelerates deep models by quantizing their weights and activations into 1-bit. However, there is still a huge performance gap between Binary Neural Networks (BNNs) and their full-precision (FP) counterparts. As the quantization error caused by weights binarization has been reduced in earlier works, the activations binarization becomes the major obstacle for further improvement of the accuracy. BNN characterises a unique and interesting structure, where the binary and latent FP activations exist in the same forward pass (i.e., $\text{Binarize}(\mathbf{a}_F) = \mathbf{a}_B$). To mitigate the information degradation caused by the binarization operation from FP to binary activations, we establish a novel contrastive learning framework while training BNNs through the lens of Mutual Information (MI) maximization. MI is introduced as the metric to measure the information shared between binary and FP activations, which assists binarization with contrastive learning. Specifically, the representation ability of the BNNs is greatly strengthened via pulling the positive pairs with binary and FP activations from the same input samples, as well as pushing negative pairs from different samples (the number of negative pairs can be exponentially large). This benefits the downstream tasks, not only classification but also segmentation and depth estimation, etc. The experimental results show that our method can be implemented as a pile-up module on existing state-of-the-art binarization methods and can remarkably improve the performance over them on CIFAR-10/100 and ImageNet, in addition to the great generalization ability on NYUD-v2.

</details>

### Unifying Visual Contrastive Learning for Object Recognition from a Graph Perspective.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_37) · 📚 被引 2
- **作者**: Shixiang Tang, Feng Zhu, Lei Bai, Rui Zhao, Chenyu Wang, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### CODER: Coupled Diversity-Sensitive Momentum Contrastive Learning for Image-Text Retrieval.
- **链接**: [arXiv:2208.09843](https://arxiv.org/abs/2208.09843)
- **作者**: Haoran Wang, Dongliang He, Wenhao Wu, Boyang Xia, Min Yang, Fu Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-Text Retrieval (ITR) is challenging in bridging visual and lingual modalities. Contrastive learning has been adopted by most prior arts. Except for limited amount of negative image-text pairs, the capability of constrastive learning is restricted by manually weighting negative pairs as well as unawareness of external knowledge. In this paper, we propose our novel Coupled Diversity-Sensitive Momentum Constrastive Learning (CODER) for improving cross-modal representation. Firstly, a novel diversity-sensitive contrastive learning (DCL) architecture is invented. We introduce dynamic dictionaries for both modalities to enlarge the scale of image-text pairs, and diversity-sensitiveness is achieved by adaptive negative pair weighting. Furthermore, two branches are designed in CODER. One learns instance-level embeddings from image/text, and it also generates pseudo online clustering labels for its input image/text based on their embeddings. Meanwhile, the other branch learns to query from commonsense knowledge graph to form concept-level descriptors for both modalities. Afterwards, both branches leverage DCL to align the cross-modal embedding spaces while an extra pseudo clustering label prediction loss is utilized to promote concept-level representation learning for the second branch. Extensive experiments conducted on two popular benchmarks, i.e. MSCOCO and Flicker30K, validate CODER remarkably outperforms the state-of-the-art approaches. Our code is available at: https://github.com/BruceW91/CODER.

</details>

### Hierarchical Semi-supervised Contrastive Learning for Contamination-Resistant Anomaly Detection.
- **链接**: [arXiv:2207.11789](https://arxiv.org/abs/2207.11789) · 📚 被引 10
- **作者**: Gaoang Wang, Yibing Zhan, Xinchao Wang, Mingli Song, Klara Nahrstedt
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection aims at identifying deviant samples from the normal data distribution. Contrastive learning has provided a successful way to sample representation that enables effective discrimination on anomalies. However, when contaminated with unlabeled abnormal samples in training set under semi-supervised settings, current contrastive-based methods generally 1) ignore the comprehensive relation between training data, leading to suboptimal performance, and 2) require fine-tuning, resulting in low efficiency. To address the above two issues, in this paper, we propose a novel hierarchical semi-supervised contrastive learning (HSCL) framework, for contamination-resistant anomaly detection. Specifically, HSCL hierarchically regulates three complementary relations: sample-to-sample, sample-to-prototype, and normal-to-abnormal relations, enlarging the discrimination between normal and abnormal samples with a comprehensive exploration of the contaminated data. Besides, HSCL is an end-to-end learning approach that can efficiently learn discriminative representations without fine-tuning. HSCL achieves state-of-the-art performance in multiple scenarios, such as one-class classification and cross-dataset detection. Extensive ablation studies further verify the effectiveness of each considered relation. The code is available at https://github.com/GaoangW/HSCL.

</details>

### MaCLR: Motion-Aware Contrastive Learning of Representations for Videos.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19833-5_21) · 📚 被引 7
- **作者**: Fanyi Xiao, Joseph Tighe, Davide Modolo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Few-Shot Classification with Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_17)
- **作者**: Zhanyuan Yang, Jinghua Wang, Yingying Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Decoupled Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_38)
- **作者**: Chun-Hsiao Yeh, Cheng-Yao Hong, Yen-Chi Hsu, Tyng-Luh Liu, Yubei Chen, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Adversarial Contrastive Learning via Asymmetric InfoNCE.
- **链接**: [arXiv:2207.08374](https://arxiv.org/abs/2207.08374)
- **作者**: Qiying Yu, Jieming Lou, Xianyuan Zhan, Qizhang Li, Wangmeng Zuo, Yang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning (CL) has recently been applied to adversarial learning tasks. Such practice considers adversarial samples as additional positive views of an instance, and by maximizing their agreements with each other, yields better adversarial robustness. However, this mechanism can be potentially flawed, since adversarial perturbations may cause instance-level identity confusion, which can impede CL performance by pulling together different instances with separate identities. To address this issue, we propose to treat adversarial samples unequally when contrasted, with an asymmetric InfoNCE objective ($A-InfoNCE$) that allows discriminating considerations of adversarial samples. Specifically, adversaries are viewed as inferior positives that induce weaker learning signals, or as hard negatives exhibiting higher contrast to other negative samples. In the asymmetric fashion, the adverse impacts of conflicting objectives between CL and adversarial learning can be effectively mitigated. Experiments show that our approach consistently outperforms existing Adversarial CL methods across different finetuning schemes without additional computational cost. The proposed A-InfoNCE is also a generic form that can be readily extended to other CL methods. Code is available at https://github.com/yqy2001/A-InfoNCE.

</details>

### Few-Shot Action Recognition with Hierarchical Matching and Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19772-7_18) · 📚 被引 51
- **作者**: Sipeng Zheng, Shizhe Chen, Qin Jin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### What to Hide from Your Students: Attention-Guided Masked Image Modeling.
- **链接**: [arXiv:2203.12719](https://arxiv.org/abs/2203.12719) · 📚 被引 90
- **作者**: Ioannis Kakogeorgiou, Spyros Gidaris, Bill Psomas, Yannis Avrithis, Andrei Bursuc, Konstantinos Karantzalos et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformers and masked language modeling are quickly being adopted and explored in computer vision as vision transformers and masked image modeling (MIM). In this work, we argue that image token masking differs from token masking in text, due to the amount and correlation of tokens in an image. In particular, to generate a challenging pretext task for MIM, we advocate a shift from random masking to informed masking. We develop and exhibit this idea in the context of distillation-based MIM, where a teacher transformer encoder generates an attention map, which we use to guide masking for the student. We thus introduce a novel masking strategy, called attention-guided masking (AttMask), and we demonstrate its effectiveness over random masking for dense distillation-based MIM as well as plain distillation-based self-supervised learning on classification tokens. We confirm that AttMask accelerates the learning process and improves the performance on a variety of downstream tasks. We provide the implementation code at https://github.com/gkakogeorgiou/attmask.

</details>

### Improved Masked Image Generation with Token-Critic.
- **链接**: [arXiv:2209.04439](https://arxiv.org/abs/2209.04439) · 📚 被引 23
- **作者**: José Lezama, Huiwen Chang, Lu Jiang, Irfan Essa
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Non-autoregressive generative transformers recently demonstrated impressive image generation performance, and orders of magnitude faster sampling than their autoregressive counterparts. However, optimal parallel sampling from the true joint distribution of visual tokens remains an open challenge. In this paper we introduce Token-Critic, an auxiliary model to guide the sampling of a non-autoregressive generative transformer. Given a masked-and-reconstructed real image, the Token-Critic model is trained to distinguish which visual tokens belong to the original image and which were sampled by the generative transformer. During non-autoregressive iterative sampling, Token-Critic is used to select which tokens to accept and which to reject and resample. Coupled with Token-Critic, a state-of-the-art generative transformer significantly improves its performance, and outperforms recent diffusion models and GANs in terms of the trade-off between generated image quality and diversity, in the challenging class-conditional ImageNet generation.

</details>

### Efficient Self-supervised Vision Transformers for Representation Learning.
- **链接**: [arXiv:2106.09785](https://arxiv.org/abs/2106.09785) · 📚 被引 57
- **作者**: Chunyuan Li, Jianwei Yang, Pengchuan Zhang, Mei Gao, Bin Xiao, Xiyang Dai et al.
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST)
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper investigates two techniques for developing efficient self-supervised vision transformers (EsViT) for visual representation learning. First, we show through a comprehensive empirical study that multi-stage architectures with sparse self-attentions can significantly reduce modeling complexity but with a cost of losing the ability to capture fine-grained correspondences between image regions. Second, we propose a new pre-training task of region matching which allows the model to capture fine-grained region dependencies and as a result significantly improves the quality of the learned vision representations. Our results show that combining the two techniques, EsViT achieves 81.3% top-1 on the ImageNet linear probe evaluation, outperforming prior arts with around an order magnitude of higher throughput. When transferring to downstream linear classification tasks, EsViT outperforms its supervised counterpart on 17 out of 18 datasets. The code and models are publicly available: https://github.com/microsoft/esvit

</details>

### Procedural generalization by planning with self-supervised world models.
- **链接**: [arXiv:2111.01587](https://arxiv.org/abs/2111.01587)
- **作者**: Ankesh Anand, Jacob C. Walker, Yazhe Li, Eszter Vértes, Julian Schrittwieser, Sherjil Ozair et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One of the key promises of model-based reinforcement learning is the ability to generalize using an internal model of the world to make predictions in novel environments and tasks. However, the generalization ability of model-based agents is not well understood because existing work has focused on model-free agents when benchmarking generalization. Here, we explicitly measure the generalization ability of model-based agents in comparison to their model-free counterparts. We focus our analysis on MuZero (Schrittwieser et al., 2020), a powerful model-based agent, and evaluate its performance on both procedural and task generalization. We identify three factors of procedural generalization -- planning, self-supervised representation learning, and procedural data diversity -- and show that by combining these techniques, we achieve state-of-the art generalization performance and data efficiency on Procgen (Cobbe et al., 2019). However, we find that these factors do not always provide the same benefits for the task generalization benchmarks in Meta-World (Yu et al., 2019), indicating that transfer remains a challenge and may require different approaches than procedural generalization. Overall, we suggest that building generalizable agents requires moving beyond the single-task, model-free paradigm and towards self-supervised model-based agents that are trained in rich, procedural, multi-task environments.

</details>

### Scarf: Self-Supervised Contrastive Learning using Random Feature Corruption.
- **链接**: [arXiv:2106.15147](https://arxiv.org/abs/2106.15147)
- **作者**: Dara Bahri, Heinrich Jiang, Yi Tay, Donald Metzler
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised contrastive representation learning has proved incredibly successful in the vision and natural language domains, enabling state-of-the-art performance with orders of magnitude less labeled data. However, such methods are domain-specific and little has been done to leverage this technique on real-world tabular datasets. We propose SCARF, a simple, widely-applicable technique for contrastive learning, where views are formed by corrupting a random subset of features. When applied to pre-train deep neural networks on the 69 real-world, tabular classification datasets from the OpenML-CC18 benchmark, SCARF not only improves classification accuracy in the fully-supervised setting but does so also in the presence of label noise and in the semi-supervised setting where only a fraction of the available training data is labeled. We show that SCARF complements existing strategies and outperforms alternatives like autoencoders. We conduct comprehensive ablations, detailing the importance of a range of factors.

</details>

### VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning.
- **链接**: [arXiv:2105.04906](https://arxiv.org/abs/2105.04906)
- **作者**: Adrien Bardes, Jean Ponce, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent self-supervised methods for image representation learning are based on maximizing the agreement between embedding vectors from different views of the same image. A trivial solution is obtained when the encoder outputs constant vectors. This collapse problem is often avoided through implicit biases in the learning architecture, that often lack a clear justification or interpretation. In this paper, we introduce VICReg (Variance-Invariance-Covariance Regularization), a method that explicitly avoids the collapse problem with a simple regularization term on the variance of the embeddings along each dimension individually. VICReg combines the variance term with a decorrelation mechanism based on redundancy reduction and covariance regularization, and achieves results on par with the state of the art on several downstream tasks. In addition, we show that incorporating our new variance term into other methods helps stabilize the training and leads to performance improvements.

</details>

### Node Feature Extraction by Self-Supervised Multi-scale Neighborhood Prediction.
- **链接**: [arXiv:2111.00064](https://arxiv.org/abs/2111.00064)
- **作者**: Eli Chien, Wei-Cheng Chang, Cho-Jui Hsieh, Hsiang-Fu Yu, Jiong Zhang, Olgica Milenkovic et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning on graphs has attracted significant attention in the learning community due to numerous real-world applications. In particular, graph neural networks (GNNs), which take numerical node features and graph structure as inputs, have been shown to achieve state-of-the-art performance on various graph-related learning tasks. Recent works exploring the correlation between numerical node features and graph structure via self-supervised learning have paved the way for further performance improvements of GNNs. However, methods used for extracting numerical node features from raw data are still graph-agnostic within standard GNN pipelines. This practice is sub-optimal as it prevents one from fully utilizing potential correlations between graph topology and node attributes. To mitigate this issue, we propose a new self-supervised learning framework, Graph Information Aided Node feature exTraction (GIANT). GIANT makes use of the eXtreme Multi-label Classification (XMC) formalism, which is crucial for fine-tuning the language model based on graph information, and scales to large datasets. We also provide a theoretical analysis that justifies the use of XMC over link prediction and motivates integrating XR-Transformers, a powerful method for solving XMC problems, into the GIANT framework. We demonstrate the superior performance of GIANT over the standard GNN pipeline on Open Graph Benchmark datasets: For example, we improve the accuracy of the top-ranked method GAMLP from $68.25\%$ to $69.67\%$, SGC from $63.29\%$ to $66.10\%$ and MLP from $47.24\%$ to $61.10\%$ on the ogbn-papers100M dataset by leveraging GIANT.

</details>

### Equivariant Self-Supervised Learning: Encouraging Equivariance in Representations.
- **链接**: [出版页](https://openreview.net/forum?id=gKLAAfiytI)
- **作者**: Rumen Dangovski, Li Jing, Charlotte Loh, Seungwook Han, Akash Srivastava, Brian Cheung et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### How Well Does Self-Supervised Pre-Training Perform with Streaming Data?
- **链接**: [出版页](https://openreview.net/forum?id=EwqEx5ipbOu)
- **作者**: Dapeng Hu, Shipeng Yan, Qizhengqiu Lu, Lanqing Hong, Hailin Hu, Yifan Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### SPIRAL: Self-supervised Perturbation-Invariant Representation Learning for Speech Pre-Training.
- **链接**: [arXiv:2201.10207](https://arxiv.org/abs/2201.10207)
- **作者**: Wenyong Huang, Zhenhe Zhang, Yu Ting Yeung, Xin Jiang, Qun Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a new approach for speech pre-training named SPIRAL which works by learning denoising representation of perturbed data in a teacher-student framework. Specifically, given a speech utterance, we first feed the utterance to a teacher network to obtain corresponding representation. Then the same utterance is perturbed and fed to a student network. The student network is trained to output representation resembling that of the teacher. At the same time, the teacher network is updated as moving average of student's weights over training steps. In order to prevent representation collapse, we apply an in-utterance contrastive loss as pre-training objective and impose position randomization on the input to the teacher. SPIRAL achieves competitive or better results compared to state-of-the-art speech pre-training method wav2vec 2.0, with significant reduction of training cost (80% for BASE model, 65% for LARGE model). Furthermore, we address the problem of noise-robustness that is critical to real-world speech applications. We propose multi-condition pre-training by perturbing the student's input with various types of additive noise. We demonstrate that multi-condition pre-trained SPIRAL models are more robust to noisy speech (9.0% - 13.3% relative word error rate reduction on real noisy test data), compared to applying multi-condition training solely in the fine-tuning stage. Source code is available at https://github.com/huawei-noah/Speech-Backbones/tree/main/SPIRAL.

</details>

### Automated Self-Supervised Learning for Graphs.
- **链接**: [arXiv:2106.05470](https://arxiv.org/abs/2106.05470)
- **作者**: Wei Jin, Xiaorui Liu, Xiangyu Zhao, Yao Ma, Neil Shah, Jiliang Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph self-supervised learning has gained increasing attention due to its capacity to learn expressive node representations. Many pretext tasks, or loss functions have been designed from distinct perspectives. However, we observe that different pretext tasks affect downstream tasks differently cross datasets, which suggests that searching pretext tasks is crucial for graph self-supervised learning. Different from existing works focusing on designing single pretext tasks, this work aims to investigate how to automatically leverage multiple pretext tasks effectively. Nevertheless, evaluating representations derived from multiple pretext tasks without direct access to ground truth labels makes this problem challenging. To address this obstacle, we make use of a key principle of many real-world graphs, i.e., homophily, or the principle that "like attracts like," as the guidance to effectively search various self-supervised pretext tasks. We provide theoretical understanding and empirical evidence to justify the flexibility of homophily in this search task. Then we propose the AutoSSL framework which can automatically search over combinations of various self-supervised tasks. By evaluating the framework on 7 real-world datasets, our experimental results show that AutoSSL can significantly boost the performance on downstream tasks including node clustering and node classification compared with training under individual tasks. Code is released at https://github.com/ChandlerBang/AutoSSL.

</details>

### Understanding Dimensional Collapse in Contrastive Self-supervised Learning.
- **链接**: [arXiv:2110.09348](https://arxiv.org/abs/2110.09348)
- **作者**: Li Jing, Pascal Vincent, Yann LeCun, Yuandong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised visual representation learning aims to learn useful representations without relying on human annotations. Joint embedding approach bases on maximizing the agreement between embedding vectors from different views of the same image. Various methods have been proposed to solve the collapsing problem where all embedding vectors collapse to a trivial constant solution. Among these methods, contrastive learning prevents collapse via negative sample pairs. It has been shown that non-contrastive methods suffer from a lesser collapse problem of a different nature: dimensional collapse, whereby the embedding vectors end up spanning a lower-dimensional subspace instead of the entire available embedding space. Here, we show that dimensional collapse also happens in contrastive learning. In this paper, we shed light on the dynamics at play in contrastive learning that leads to dimensional collapse. Inspired by our theory, we propose a novel contrastive learning method, called DirectCLR, which directly optimizes the representation space without relying on an explicit trainable projector. Experiments show that DirectCLR outperforms SimCLR with a trainable linear projector on ImageNet.

</details>

### Self-supervised Learning is More Robust to Dataset Imbalance.
- **链接**: [arXiv:2110.05025](https://arxiv.org/abs/2110.05025)
- **作者**: Hong Liu, Jeff Z. HaoChen, Adrien Gaidon, Tengyu Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) is a scalable way to learn general visual representations since it learns without labels. However, large-scale unlabeled datasets in the wild often have long-tailed label distributions, where we know little about the behavior of SSL. In this work, we systematically investigate self-supervised learning under dataset imbalance. First, we find out via extensive experiments that off-the-shelf self-supervised representations are already more robust to class imbalance than supervised representations. The performance gap between balanced and imbalanced pre-training with SSL is significantly smaller than the gap with supervised learning, across sample sizes, for both in-domain and, especially, out-of-domain evaluation. Second, towards understanding the robustness of SSL, we hypothesize that SSL learns richer features from frequent data: it may learn label-irrelevant-but-transferable features that help classify the rare classes and downstream tasks. In contrast, supervised learning has no incentive to learn features irrelevant to the labels from frequent examples. We validate this hypothesis with semi-synthetic experiments and theoretical analyses on a simplified setting. Third, inspired by the theoretical insights, we devise a re-weighted regularization technique that consistently improves the SSL representation quality on imbalanced datasets with several evaluation criteria, closing the small gap between balanced and imbalanced datasets with the same number of examples.

</details>

### Self-Supervised Inference in State-Space Models.
- **链接**: [出版页](https://openreview.net/forum?id=VPjw9KPWRSK)
- **作者**: David Ruhe, Patrick Forré
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Self-Supervised Graph Neural Networks for Improved Electroencephalographic Seizure Analysis.
- **链接**: [出版页](https://openreview.net/forum?id=k9bx1EfHI_-)
- **作者**: Siyi Tang, Jared Dunnmon, Khaled Kamal Saab, Xuan Zhang, Qianying Huang, Florian Dubost et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Bag of Instances Aggregation Boosts Self-supervised Distillation.
- **链接**: [出版页](https://openreview.net/forum?id=N0uJGWDw21d)
- **作者**: Haohang Xu, Jiemin Fang, Xiaopeng Zhang, Lingxi Xie, Xinggang Wang, Wenrui Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### How Does SimSiam Avoid Collapse Without Negative Samples? A Unified Understanding with Self-supervised Contrastive Learning.
- **链接**: [arXiv:2203.16262](https://arxiv.org/abs/2203.16262)
- **作者**: Chaoning Zhang, Kang Zhang, Chenshuang Zhang, Trung X. Pham, Chang D. Yoo, In So Kweon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To avoid collapse in self-supervised learning (SSL), a contrastive loss is widely used but often requires a large number of negative samples. Without negative samples yet achieving competitive performance, a recent work has attracted significant attention for providing a minimalist simple Siamese (SimSiam) method to avoid collapse. However, the reason for how it avoids collapse without negative samples remains not fully clear and our investigation starts by revisiting the explanatory claims in the original SimSiam. After refuting their claims, we introduce vector decomposition for analyzing the collapse based on the gradient analysis of the $l_2$-normalized representation vector. This yields a unified perspective on how negative samples and SimSiam alleviate collapse. Such a unified perspective comes timely for understanding the recent progress in SSL.

</details>

### Divergence-aware Federated Self-Supervised Learning.
- **链接**: [arXiv:2204.04385](https://arxiv.org/abs/2204.04385)
- **作者**: Weiming Zhuang, Yonggang Wen, Shuai Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) is capable of learning remarkable representations from centrally available data. Recent works further implement federated learning with SSL to learn from rapidly growing decentralized unlabeled images (e.g., from cameras and phones), often resulted from privacy constraints. Extensive attention has been paid to SSL approaches based on Siamese networks. However, such an effort has not yet revealed deep insights into various fundamental building blocks for the federated self-supervised learning (FedSSL) architecture. We aim to fill in this gap via in-depth empirical study and propose a new method to tackle the non-independently and identically distributed (non-IID) data problem of decentralized data. Firstly, we introduce a generalized FedSSL framework that embraces existing SSL methods based on Siamese networks and presents flexibility catering to future methods. In this framework, a server coordinates multiple clients to conduct SSL training and periodically updates local models of clients with the aggregated global model. Using the framework, our study uncovers unique insights of FedSSL: 1) stop-gradient operation, previously reported to be essential, is not always necessary in FedSSL; 2) retaining local knowledge of clients in FedSSL is particularly beneficial for non-IID data. Inspired by the insights, we then propose a new approach for model update, Federated Divergence-aware Exponential Moving Average update (FedEMA). FedEMA updates local models of clients adaptively using EMA of the global model, where the decay rate is dynamically measured by model divergence. Extensive experiments demonstrate that FedEMA outperforms existing methods by 3-4% on linear evaluation. We hope that this work will provide useful insights for future research.

</details>

### The Close Relationship Between Contrastive Learning and Meta-Learning.
- **链接**: [出版页](https://openreview.net/forum?id=gICys3ITSmj)
- **作者**: Renkun Ni, Manli Shu, Hossein Souri, Micah Goldblum, Tom Goldstein
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

### Learning Disentangled Representation by Exploiting Pretrained Generative Models: A Contrastive Learning View.
- **链接**: [出版页](https://openreview.net/forum?id=j-63FSNcO5a)
- **作者**: Xuanchi Ren, Tao Yang, Yuwang Wang, Wenjun Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022

## 跨领域论文（完整笔记在其他领域）

- MAE-DET: Revisiting Maximum Entropy Principle in Zero-Shot NAS for Efficient Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- Self-supervised object detection from audio-visual correspondence. → [object-detection](../object-detection/Guideline%202022.md)
- Point-Level Region Contrast for Object Detection Pre-Training. → [object-detection](../object-detection/Guideline%202022.md)
- DETReg: Unsupervised Pretraining with Region Priors for Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Expanding Low-Density Latent Regions for Open-Set Object Detection. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- Revisiting the "Video" in Video-Language Understanding. → [video-understanding](../video-understanding/Guideline%202022.md)
- Probing Representation Forgetting in Supervised and Unsupervised Continual Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Learning to Imagine: Diversify Memory for Incremental Learning using Unlabeled Data. → [continual-learning](../continual-learning/Guideline%202022.md)
- Fire Together Wire Together: A Dynamic Pruning Approach with Self-Supervised Mask Prediction. → [network-pruning](../network-pruning/Guideline%202022.md)
- Robust Cross-Modal Representation Learning with Progressive Self-Distillation. → [multimodal](../multimodal/Guideline%202022.md)
- Exploring Resolution and Degradation Clues as Self-supervised Signal for Low Quality Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone. → [3d-detection](../3d-detection/Guideline%202022.md)
- Exploring Plain Vision Transformer Backbones for Object Detection. → [vision-transformer](../vision-transformer/Guideline%202022.md)
- Open-Set Semi-Supervised Object Detection. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Emotion-aware Multi-view Contrastive Learning for Facial Emotion Recognition. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- RA-Depth: Resolution Adaptive Self-supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Towards Comprehensive Representation Enhancement in Semantics-Guided Self-supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Multi-modal Masked Pre-training for Monocular Panoramic Depth Completion. → [multimodal](../multimodal/Guideline%202022.md)
- Self-distilled Feature Aggregation for Self-supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Single-Stream Multi-level Alignment for Vision-Language Pretraining. → [vlm](../vlm/Guideline%202022.md)
- Online Continual Learning with Contrastive Vision Transformer. → [continual-learning](../continual-learning/Guideline%202022.md)
- Learning Mutual Modulation for Self-supervised Cross-Modal Super-Resolution. → [multimodal](../multimodal/Guideline%202022.md)
- S3C: Self-Supervised Stochastic Classifiers for Few-Shot Class-Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- CMD: Self-supervised 3D Action Representation Learning with Cross-Modal Mutual Distillation. → [multimodal](../multimodal/Guideline%202022.md)
- Action-Based Contrastive Learning for Trajectory Prediction. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction. → [multimodal](../multimodal/Guideline%202022.md)

<!-- COMPLETE v1 papers=149 -->
