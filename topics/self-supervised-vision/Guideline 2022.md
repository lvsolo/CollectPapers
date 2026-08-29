# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 79 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Supervised Global-Local Structure Modeling for Point Cloud Domain Adaptation with Reliable Voted Pseudo Labels.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00627) · 📚 被引 60
- **作者**: Hehe Fan, Xiaojun Chang, Wanyue Zhang, Yi Cheng, Ying Sun, Mohan S. Kankanhalli
- **🏷️ 机构**: School of Computing, National University of Singapore, ReLER Lab, AAII, University of Technology,Sydney, Max Planck Institute for Informatics
- **会议**: CVPR 2022

### RigidFlow: Self-Supervised Scene Flow Learning on Point Clouds by Local Rigidity Prior.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01645) · 📚 被引 48
- **作者**: Ruibo Li, Chi Zhang, Guosheng Lin, Zhe Wang, Chunhua Shen
- **🏷️ 机构**: Nanyang Technological University,S-Lab for Advanced Intelligence, School of Computer Science and Engineering, Nanyang Technological University, SenseTime Research
- **会议**: CVPR 2022

### Self-Supervised Arbitrary-Scale Point Clouds Upsampling via Implicit Neural Representation.
- **链接**: [arXiv:2204.08196](https://arxiv.org/abs/2204.08196) · [代码](https://github.com/xnowbzhao/sapcu) · 📚 被引 63
- **作者**: Wenbo Zhao, Xianming Liu, Zhiwei Zhong, Junjun Jiang, Wei Gao, Ge Li et al.
- **🏷️ 机构**: Harbin Institute of Technology, Peking University Shenzhen Graduate School, Tsinghua University
- **会议**: CVPR 2022

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

### Self-Supervised Material and Texture Representation Learning for Remote Sensing Tasks.
- **链接**: [arXiv:2112.01715](https://arxiv.org/abs/2112.01715) · 📚 被引 63
- **作者**: Peri Akiva, Matthew Purri, Matthew J. Leotta
- **🏷️ 机构**: Rutgers University, Kitware Inc
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning aims to learn image feature representations without the usage of manually annotated labels. It is often used as a precursor step to obtain useful initial network weights which contribute to faster convergence and superior performance of downstream tasks. While self-supervision allows one to reduce the domain gap between supervised and unsupervised learning without the usage of labels, the self-supervised objective still requires a strong inductive bias to downstream tasks for effective transfer learning. In this work, we present our material and texture based self-supervision method named MATTER (MATerial and TExture Representation Learning), which is inspired by classical material and texture methods. Material and texture can effectively describe any surface, including its tactile properties, color, and specularity. By extension, effective representation of material and texture can describe other semantic classes strongly associated with said material and texture. MATTER leverages multi-temporal, spatially aligned remote sensing imagery over unchanged regions to learn invariance to illumination and viewing angle as a mechanism to achieve consistency of material and texture representation. We show that our self-supervision pre-training method allows for up to 24.22% and 6.33% performance increase in unsupervised and fine-tuned setups, and up to 76% faster convergence on change detection, land cover classification, and semantic segmentation tasks.

</details>

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

### Knowledge-Driven Self-Supervised Representation Learning for Facial Action Unit Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01977) · 📚 被引 41
- **作者**: Yanan Chang, Shangfei Wang
- **🏷️ 机构**: University of Science and Technology of China,Hefei,Anhui,China
- **会议**: CVPR 2022

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

### SPAct: Self-supervised Privacy Preservation for Action Recognition.
- **链接**: [arXiv:2203.15205](https://arxiv.org/abs/2203.15205) · [代码](https://github.com/DAVEISHAN/SPAct) · 📚 被引 66
- **作者**: Ishan Rajendrakumar Dave, Chen Chen, Mubarak Shah
- **🏷️ 机构**: Center for Research in Computer Vision, University of Central Florida,Orlando,USA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual private information leakage is an emerging key issue for the fast growing applications of video understanding like activity recognition. Existing approaches for mitigating privacy leakage in action recognition require privacy labels along with the action labels from the video dataset. However, annotating frames of video dataset for privacy labels is not feasible. Recent developments of self-supervised learning (SSL) have unleashed the untapped potential of the unlabeled data. For the first time, we present a novel training framework which removes privacy information from input video in a self-supervised manner without requiring privacy labels. Our training framework consists of three main components: anonymization function, self-supervised privacy removal branch, and action recognition branch. We train our framework using a minimax optimization strategy to minimize the action recognition cost function and maximize the privacy cost function through a contrastive self-supervised loss. Employing existing protocols of known-action and privacy attributes, our framework achieves a competitive action-privacy trade-off to the existing state-of-the-art supervised methods. In addition, we introduce a new protocol to evaluate the generalization of learned the anonymization function to novel-action and privacy attributes and show that our self-supervised framework outperforms existing supervised methods. Code available at: https://github.com/DAVEISHAN/SPAct

</details>

### TransRank: Self-supervised Video Representation Learning via Ranking-based Transformation Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00301)
- **作者**: Haodong Duan, Nanxuan Zhao, Kai Chen, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2022

### Incremental Cross-view Mutual Distillation for Self-supervised Medical CT Synthesis.
- **链接**: [arXiv:2112.10325](https://arxiv.org/abs/2112.10325) · 📚 被引 26
- **作者**: Chaowei Fang, Liang Wang, Dingwen Zhang, Jun Xu, Yixuan Yuan, Junwei Han
- **🏷️ 机构**: Xidian University, Northwestern Polytechnical University, Nankai University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the constraints of the imaging device and high cost in operation time, computer tomography (CT) scans are usually acquired with low intra-slice resolution. Improving the intra-slice resolution is beneficial to the disease diagnosis for both human experts and computer-aided systems. To this end, this paper builds a novel medical slice synthesis to increase the between-slice resolution. Considering that the ground-truth intermediate medical slices are always absent in clinical practice, we introduce the incremental cross-view mutual distillation strategy to accomplish this task in the self-supervised learning manner. Specifically, we model this problem from three different views: slice-wise interpolation from axial view and pixel-wise interpolation from coronal and sagittal views. Under this circumstance, the models learned from different views can distill valuable knowledge to guide the learning processes of each other. We can repeat this process to make the models synthesize intermediate slice data with increasing inter-slice resolution. To demonstrate the effectiveness of the proposed approach, we conduct comprehensive experiments on a large-scale CT dataset. Quantitative and qualitative comparison results show that our method outperforms state-of-the-art algorithms by clear margins.

</details>

### Self-Supervised Models are Continual Learners.
- **链接**: [arXiv:2112.04215](https://arxiv.org/abs/2112.04215) · 📚 被引 134
- **作者**: Enrico Fini, Victor G. Turrisi da Costa, Xavier Alameda-Pineda, Elisa Ricci, Karteek Alahari, Julien Mairal
- **🏷️ 机构**: University of Trento, Inria
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised models have been shown to produce comparable or better visual representations than their supervised counterparts when trained offline on unlabeled data at scale. However, their efficacy is catastrophically reduced in a Continual Learning (CL) scenario where data is presented to the model sequentially. In this paper, we show that self-supervised loss functions can be seamlessly converted into distillation mechanisms for CL by adding a predictor network that maps the current state of the representations to their past state. This enables us to devise a framework for Continual self-supervised visual representation Learning that (i) significantly improves the quality of the learned representations, (ii) is compatible with several state-of-the-art self-supervised objectives, and (iii) needs little to no hyperparameter tuning. We demonstrate the effectiveness of our approach empirically by training six popular self-supervised models in various CL settings.

</details>

### DiRA: Discriminative, Restorative, and Adversarial Learning for Self-supervised Medical Image Analysis.
- **链接**: [arXiv:2204.10437](https://arxiv.org/abs/2204.10437) · [代码](https://github.com/JLiangLab/DiRA) · 📚 被引 88
- **作者**: Fatemeh Haghighi, Mohammad Reza Hosseinzadeh Taher, Michael B. Gotway, Jianming Liang
- **🏷️ 机构**: Arizona State University, Mayo Clinic
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Discriminative learning, restorative learning, and adversarial learning have proven beneficial for self-supervised learning schemes in computer vision and medical imaging. Existing efforts, however, omit their synergistic effects on each other in a ternary setup, which, we envision, can significantly benefit deep semantic representation learning. To realize this vision, we have developed DiRA, the first framework that unites discriminative, restorative, and adversarial learning in a unified manner to collaboratively glean complementary visual information from unlabeled medical images for fine-grained semantic representation learning. Our extensive experiments demonstrate that DiRA (1) encourages collaborative learning among three learning ingredients, resulting in more generalizable representation across organs, diseases, and modalities; (2) outperforms fully supervised ImageNet models and increases robustness in small data regimes, reducing annotation cost across multiple medical imaging applications; (3) learns fine-grained semantic representation, facilitating accurate lesion localization with only image-level annotation; and (4) enhances state-of-the-art restorative approaches, revealing that DiRA is a general mechanism for united representation learning. All code and pre-trained models are available at https: //github.com/JLiangLab/DiRA.

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

### Noise Distribution Adaptive Self-Supervised Image Denoising using Tweedie Distribution and Score Matching.
- **链接**: [arXiv:2112.03696](https://arxiv.org/abs/2112.03696) · 📚 被引 18
- **作者**: Kwanyoung Kim, Taesung Kwon, Jong Chul Ye
- **🏷️ 机构**: Kim Jaechul Graduate School of AI, KAIST,Department of Bio and Brain Engineering
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tweedie distributions are a special case of exponential dispersion models, which are often used in classical statistics as distributions for generalized linear models. Here, we reveal that Tweedie distributions also play key roles in modern deep learning era, leading to a distribution independent self-supervised image denoising formula without clean reference images. Specifically, by combining with the recent Noise2Score self-supervised image denoising approach and the saddle point approximation of Tweedie distribution, we can provide a general closed-form denoising formula that can be used for large classes of noise distributions without ever knowing the underlying noise distribution. Similar to the original Noise2Score, the new approach is composed of two successive steps: score matching using perturbed noisy images, followed by a closed form image denoising formula via distribution-independent Tweedie's formula. This also suggests a systematic algorithm to estimate the noise model and noise parameters for a given noisy image data set. Through extensive experiments, we demonstrate that the proposed method can accurately estimate noise models and parameters, and provide the state-of-the-art self-supervised image denoising performance in the benchmark dataset and real-world dataset.

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

### Cross-patch Dense Contrastive Learning for Semi-supervised Segmentation of Cellular Nuclei in Histopathologic Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01137) · 📚 被引 79
- **作者**: Huisi Wu, Zhaoze Wang, Youyi Song, Lin Yang, Jing Qin
- **🏷️ 机构**: Shenzhen University, The Hong Kong Polytechnic University
- **会议**: CVPR 2022

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

### SimMIM: a Simple Framework for Masked Image Modeling.
- **链接**: [arXiv:2111.09886](https://arxiv.org/abs/2111.09886) · [代码](https://github.com/microsoft/SimMIM) · 📚 被引 1154
- **作者**: Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Jianmin Bao, Zhuliang Yao et al.
- **🏷️ 机构**: Tsinghua University, Microsoft Research Asia, Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2022

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
