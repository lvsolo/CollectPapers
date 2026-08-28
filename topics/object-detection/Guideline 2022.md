# Object Detection — 2022 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 81 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Rethinking Few-Shot Object Detection on a Multi-Domain Benchmark.
- **链接**: [arXiv:2207.11169](https://arxiv.org/abs/2207.11169) · [代码](https://github.com/amazon-research/few-shot-object-detection-benchmark)
- **作者**: Kibok Lee, Hao Yang, Satyaki Chakraborty, Zhaowei Cai, Gurumurthy Swaminathan, Avinash Ravichandran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing works on few-shot object detection (FSOD) focus on a setting where both pre-training and few-shot learning datasets are from a similar domain. However, few-shot algorithms are important in multiple domains; hence evaluation needs to reflect the broad applications. We propose a Multi-dOmain Few-Shot Object Detection (MoFSOD) benchmark consisting of 10 datasets from a wide range of domains to evaluate FSOD algorithms. We comprehensively analyze the impacts of freezing layers, different architectures, and different pre-training datasets on FSOD performance. Our empirical results show several key factors that have not been explored in previous works: 1) contrary to previous belief, on a multi-domain benchmark, fine-tuning (FT) is a strong baseline for FSOD, performing on par or better than the state-of-the-art (SOTA) algorithms; 2) utilizing FT as the baseline allows us to explore multiple architectures, and we found them to have a significant impact on down-stream few-shot tasks, even with similar pre-training performances; 3) by decoupling pre-training and few-shot learning, MoFSOD allows us to explore the impact of different pre-training datasets, and the right choice can boost the performance of the down-stream tasks significantly. Based on these findings, we list possible avenues of investigation for improving FSOD performance and propose two simple modifications to existing algorithms that lead to SOTA performance on the MoFSOD benchmark. The code is available at https://github.com/amazon-research/few-shot-object-detection-benchmark.

</details>

### A Simple Approach and Benchmark for 21, 000-Category Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_1) · 📚 被引 1
- **作者**: Yutong Lin, Chen Li, Yue Cao, Zheng Zhang, Jianfeng Wang, Lijuan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Towards Hard-Positive Query Mining for DETR-Based Human-Object Interaction Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19812-0_26) · 📚 被引 26
- **作者**: Xubin Zhong, Changxing Ding, Zijian Li, Shaoli Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Open-Vocabulary DETR with Conditional Matching.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_7)
- **作者**: Yuhang Zang, Wei Li, Kaiyang Zhou, Chen Huang, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ECCV 2022

### X-DETR: A Versatile Architecture for Instance-wise Vision-Language Tasks.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_17) · 📚 被引 32
- **作者**: Zhaowei Cai, Gukyeong Kwon, Avinash Ravichandran, Erhan Bas, Zhuowen Tu, Rahul Bhotika et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### A Large-Scale Multiple-objective Method for Black-box Attack Against Object Detection.
- **链接**: [arXiv:2209.07790](https://arxiv.org/abs/2209.07790) · 📚 被引 22
- **作者**: Siyuan Liang, Longkang Li, Yanbo Fan, Xiaojun Jia, Jingzhi Li, Baoyuan Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have shown that detectors based on deep models are vulnerable to adversarial examples, even in the black-box scenario where the attacker cannot access the model information. Most existing attack methods aim to minimize the true positive rate, which often shows poor attack performance, as another sub-optimal bounding box may be detected around the attacked bounding box to be the new true positive one. To settle this challenge, we propose to minimize the true positive rate and maximize the false positive rate, which can encourage more false positive objects to block the generation of new true positive bounding boxes. It is modeled as a multi-objective optimization (MOP) problem, of which the generic algorithm can search the Pareto-optimal. However, our task has more than two million decision variables, leading to low searching efficiency. Thus, we extend the standard Genetic Algorithm with Random Subset selection and Divide-and-Conquer, called GARSDC, which significantly improves the efficiency. Moreover, to alleviate the sensitivity to population quality in generic algorithms, we generate a gradient-prior initial population, utilizing the transferability between different detectors with similar backbones. Compared with the state-of-art attack methods, GARSDC decreases by an average 12.0 in the mAP and queries by about 1000 times in extensive experiments. Our codes can be found at https://github.com/LiangSiyuan21/ GARSDC.

</details>

### Object Discovery via Contrastive Learning for Weakly Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_18)
- **作者**: Jinhwan Seo, Wonho Bae, Danica J. Sutherland, Junhyug Noh, Daijin Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### ObjectBox: From Centers to Boxes for Anchor-Free Object Detection.
- **链接**: [arXiv:2207.06985](https://arxiv.org/abs/2207.06985) · [代码](https://github.com/MohsenZand/ObjectBox) · 📚 被引 75
- **作者**: Mohsen Zand, Ali Etemad, Michael A. Greenspan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present ObjectBox, a novel single-stage anchor-free and highly generalizable object detection approach. As opposed to both existing anchor-based and anchor-free detectors, which are more biased toward specific object scales in their label assignments, we use only object center locations as positive samples and treat all objects equally in different feature levels regardless of the objects' sizes or shapes. Specifically, our label assignment strategy considers the object center locations as shape- and size-agnostic anchors in an anchor-free fashion, and allows learning to occur at all scales for every object. To support this, we define new regression targets as the distances from two corners of the center cell location to the four sides of the bounding box. Moreover, to handle scale-variant objects, we propose a tailored IoU loss to deal with boxes with different sizes. As a result, our proposed object detector does not need any dataset-dependent hyperparameters to be tuned across datasets. We evaluate our method on MS-COCO 2017 and PASCAL VOC 2012 datasets, and compare our results to state-of-the-art methods. We observe that ObjectBox performs favorably in comparison to prior works. Furthermore, we perform rigorous ablation experiments to evaluate different components of our method. Our code is available at: https://github.com/MohsenZand/ObjectBox.

</details>

### SALISA: Saliency-Based Input Sampling for Efficient Video Object Detection.
- **链接**: [arXiv:2204.02397](https://arxiv.org/abs/2204.02397) · 📚 被引 11
- **作者**: Babak Ehteshami Bejnordi, Amirhossein Habibian, Fatih Porikli, Amir Ghodrati
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution images are widely adopted for high-performance object detection in videos. However, processing high-resolution inputs comes with high computation costs, and naive down-sampling of the input to reduce the computation costs quickly degrades the detection performance. In this paper, we propose SALISA, a novel non-uniform SALiency-based Input SAmpling technique for video object detection that allows for heavy down-sampling of unimportant background regions while preserving the fine-grained details of a high-resolution image. The resulting image is spatially smaller, leading to reduced computational costs while enabling a performance comparable to a high-resolution input. To achieve this, we propose a differentiable resampling module based on a thin plate spline spatial transformer network (TPS-STN). This module is regularized by a novel loss to provide an explicit supervision signal to learn to "magnify" salient regions. We report state-of-the-art results in the low compute regime on the ImageNet-VID and UA-DETRAC video object detection datasets. We demonstrate that on both datasets, the mAP of an EfficientDet-D1 (EfficientDet-D2) gets on par with EfficientDet-D2 (EfficientDet-D3) at a much lower computational cost. We also show that SALISA significantly improves the detection of small objects. In particular, SALISA with an EfficientDet-D1 detector improves the detection of small objects by $77\%$, and remarkably also outperforms EfficientDetD3 baseline.

</details>

### Semi-supervised Object Detection via VC Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_10) · 📚 被引 7
- **作者**: Changrui Chen, Kurt Debattista, Jungong Han
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### A Simple Single-Scale Vision Transformer for Object Detection and Instance Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_41)
- **作者**: Wuyang Chen, Xianzhi Du, Fan Yang, Lucas Beyer, Xiaohua Zhai, Tsung-Yi Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection.
- **链接**: [arXiv:2205.05979](https://arxiv.org/abs/2205.05979) · [代码](https://github.com/open-mmlab/OpenPCDet) · 📚 被引 75
- **作者**: Xuesong Chen, Shaoshuai Shi, Benjin Zhu, Ka Chun Cheung, Hang Xu, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate and reliable 3D detection is vital for many applications including autonomous driving vehicles and service robots. In this paper, we present a flexible and high-performance 3D detection framework, named MPPNet, for 3D temporal object detection with point cloud sequences. We propose a novel three-hierarchy framework with proxy points for multi-frame feature encoding and interactions to achieve better detection. The three hierarchies conduct per-frame feature encoding, short-clip feature fusion, and whole-sequence feature aggregation, respectively. To enable processing long-sequence point clouds with reasonable computational resources, intra-group feature mixing and inter-group feature attention are proposed to form the second and third feature encoding hierarchies, which are recurrently applied for aggregating multi-frame trajectory features. The proxy points not only act as consistent object representations for each frame, but also serve as the courier to facilitate feature interaction between frames. The experiments on large Waymo Open dataset show that our approach outperforms state-of-the-art methods with large margins when applied to both short (e.g., 4-frame) and long (e.g., 16-frame) point cloud sequences. Code is available at https://github.com/open-mmlab/OpenPCDet.

</details>

### Point-to-Box Network for Accurate Object Detection via Single Point Supervision.
- **链接**: [arXiv:2207.06827](https://arxiv.org/abs/2207.06827) · [代码](https://github.com/ucas-vg/P2BNet) · 📚 被引 75
- **作者**: Pengfei Chen, Xuehui Yu, Xumeng Han, Najmul Hassan, Kai Wang, Jiachen Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection using single point supervision has received increasing attention over the years. However, the performance gap between point supervised object detection (PSOD) and bounding box supervised detection remains large. In this paper, we attribute such a large performance gap to the failure of generating high-quality proposal bags which are crucial for multiple instance learning (MIL). To address this problem, we introduce a lightweight alternative to the off-the-shelf proposal (OTSP) method and thereby create the Point-to-Box Network (P2BNet), which can construct an inter-objects balanced proposal bag by generating proposals in an anchor-like way. By fully investigating the accurate position information, P2BNet further constructs an instance-level bag, avoiding the mixture of multiple objects. Finally, a coarse-to-fine policy in a cascade fashion is utilized to improve the IoU between proposals and ground-truth (GT). Benefiting from these strategies, P2BNet is able to produce high-quality instance-level bags for object detection. P2BNet improves the mean average precision (AP) by more than 50% relative to the previous best PSOD method on the MS COCO dataset. It also demonstrates the great potential to bridge the performance gap between point supervised and bounding-box supervised detectors. The code will be released at github.com/ucas-vg/P2BNet.

</details>

### Efficient Decoder-Free Object Detection with Transformers.
- **链接**: [arXiv:2206.06829](https://arxiv.org/abs/2206.06829) · 📚 被引 17
- **作者**: Peixian Chen, Mengdan Zhang, Yunhang Shen, Kekai Sheng, Yuting Gao, Xing Sun et al.
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers (ViTs) are changing the landscape of object detection approaches. A natural usage of ViTs in detection is to replace the CNN-based backbone with a transformer-based backbone, which is straightforward and effective, with the price of bringing considerable computation burden for inference. More subtle usage is the DETR family, which eliminates the need for many hand-designed components in object detection but introduces a decoder demanding an extra-long time to converge. As a result, transformer-based object detection can not prevail in large-scale applications. To overcome these issues, we propose a novel decoder-free fully transformer-based (DFFT) object detector, achieving high efficiency in both training and inference stages, for the first time. We simplify objection detection into an encoder-only single-level anchor-based dense prediction problem by centering around two entry points: 1) Eliminate the training-inefficient decoder and leverage two strong encoders to preserve the accuracy of single-level feature map prediction; 2) Explore low-level semantic features for the detection task with limited computational resources. In particular, we design a novel lightweight detection-oriented transformer backbone that efficiently captures low-level features with rich semantics based on a well-conceived ablation study. Extensive experiments on the MS COCO benchmark demonstrate that DFFT_SMALL outperforms DETR by 2.5% AP with 28% computation cost reduction and more than $10$x fewer training epochs. Compared with the cutting-edge anchor-based detector RetinaNet, DFFT_SMALL obtains over 5.5% AP gain while cutting down 70% computation cost.

</details>

### Exploring Resolution and Degradation Clues as Self-supervised Signal for Low Quality Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_28)
- **作者**: Ziteng Cui, Yingying Zhu, Lin Gu, Guo-Jun Qi, Xiaoxiao Li, Renrui Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Salient Object Detection for Point Clouds.
- **链接**: [arXiv:2207.11889](https://arxiv.org/abs/2207.11889)
- **作者**: Songlin Fan, Wei Gao, Ge Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper researches the unexplored task-point cloud salient object detection (SOD). Differing from SOD for images, we find the attention shift of point clouds may provoke saliency conflict, i.e., an object paradoxically belongs to salient and non-salient categories. To eschew this issue, we present a novel view-dependent perspective of salient objects, reasonably reflecting the most eye-catching objects in point cloud scenarios. Following this formulation, we introduce PCSOD, the first dataset proposed for point cloud SOD consisting of 2,872 in-/out-door 3D views. The samples in our dataset are labeled with hierarchical annotations, e.g., super-/sub-class, bounding box, and segmentation map, which endows the brilliant generalizability and broad applicability of our dataset verifying various conjectures. To evidence the feasibility of our solution, we further contribute a baseline model and benchmark five representative models for a comprehensive comparison. The proposed model can effectively analyze irregular and unordered points for detecting salient objects. Thanks to incorporating the task-tailored designs, our method shows visible superiority over other baselines, producing more satisfactory results. Extensive experiments and discussions reveal the promising potential of this research field, paving the way for further study.

</details>

### Few-Shot Video Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_5)
- **作者**: Qi Fan, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Few-Shot Object Detection with Model Calibration.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19800-7_42)
- **作者**: Qi Fan, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Open Vocabulary Object Detection with Pseudo Bounding-Box Labels.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_16)
- **作者**: Mingfei Gao, Chen Xing, Juan Carlos Niebles, Junnan Li, Ran Xu, Wenhao Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### AcroFOD: An Adaptive Method for Cross-Domain Few-Shot Object Detection.
- **链接**: [arXiv:2209.10904](https://arxiv.org/abs/2209.10904) · 📚 被引 35
- **作者**: Yipeng Gao, Lingxiao Yang, Yunmu Huang, Song Xie, Shiyong Li, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Under the domain shift, cross-domain few-shot object detection aims to adapt object detectors in the target domain with a few annotated target data. There exists two significant challenges: (1) Highly insufficient target domain data; (2) Potential over-adaptation and misleading caused by inappropriately amplified target samples without any restriction. To address these challenges, we propose an adaptive method consisting of two parts. First, we propose an adaptive optimization strategy to select augmented data similar to target samples rather than blindly increasing the amount. Specifically, we filter the augmented candidates which significantly deviate from the target feature distribution in the very beginning. Second, to further relieve the data limitation, we propose the multi-level domain-aware data augmentation to increase the diversity and rationality of augmented data, which exploits the cross-image foreground-background mixture. Experiments show that the proposed method achieves state-of-the-art performance on multiple benchmarks.

</details>

### SemAug: Semantically Meaningful Image Augmentations for Object Detection Through Language Grounding.
- **链接**: [arXiv:2208.07407](https://arxiv.org/abs/2208.07407) · 📚 被引 3
- **作者**: Morgan Heisler, Amin Banitalebi-Dehkordi, Yong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data augmentation is an essential technique in improving the generalization of deep neural networks. The majority of existing image-domain augmentations either rely on geometric and structural transformations, or apply different kinds of photometric distortions. In this paper, we propose an effective technique for image augmentation by injecting contextually meaningful knowledge into the scenes. Our method of semantically meaningful image augmentation for object detection via language grounding, SemAug, starts by calculating semantically appropriate new objects that can be placed into relevant locations in the image (the what and where problems). Then it embeds these objects into their relevant target locations, thereby promoting diversity of object instance distribution. Our method allows for introducing new object instances and categories that may not even exist in the training set. Furthermore, it does not require the additional overhead of training a context network, so it can be easily added to existing architectures. Our comprehensive set of evaluations showed that the proposed method is very effective in improving the generalization, while the overhead is negligible. In particular, for a wide range of model architectures, our method achieved ~2-4% and ~1-2% mAP improvements for the task of object detection on the Pascal VOC and COCO datasets, respectively.

</details>

### Object Detection as Probabilistic Set Prediction.
- **链接**: [arXiv:2203.07980](https://arxiv.org/abs/2203.07980) · [代码](https://github.com/georghess/pmb-nll) · 📚 被引 3
- **作者**: Georg Hess, Christoffer Petersson, Lennart Svensson
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate uncertainty estimates are essential for deploying deep object detectors in safety-critical systems. The development and evaluation of probabilistic object detectors have been hindered by shortcomings in existing performance measures, which tend to involve arbitrary thresholds or limit the detector's choice of distributions. In this work, we propose to view object detection as a set prediction task where detectors predict the distribution over the set of objects. Using the negative log-likelihood for random finite sets, we present a proper scoring rule for evaluating and training probabilistic object detectors. The proposed method can be applied to existing probabilistic detectors, is free from thresholds, and enables fair comparison between architectures. Three different types of detectors are evaluated on the COCO dataset. Our results indicate that the training of existing detectors is optimized toward non-probabilistic metrics. We hope to encourage the development of new object detectors that can accurately estimate their own uncertainty. Code available at https://github.com/georghess/pmb-nll.

</details>

### W2N: Switching from Weak Supervision to Noisy Supervision for Object Detection.
- **链接**: [arXiv:2207.12104](https://arxiv.org/abs/2207.12104) · [代码](https://github.com/1170300714/w2n_wsod) · 📚 被引 18
- **作者**: Zitong Huang, Yiping Bao, Bowen Dong, Erjin Zhou, Wangmeng Zuo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly-supervised object detection (WSOD) aims to train an object detector only requiring the image-level annotations. Recently, some works have managed to select the accurate boxes generated from a well-trained WSOD network to supervise a semi-supervised detection framework for better performance. However, these approaches simply divide the training set into labeled and unlabeled sets according to the image-level criteria, such that sufficient mislabeled or wrongly localized box predictions are chosen as pseudo ground-truths, resulting in a sub-optimal solution of detection performance. To overcome this issue, we propose a novel WSOD framework with a new paradigm that switches from weak supervision to noisy supervision (W2N). Generally, with given pseudo ground-truths generated from the well-trained WSOD network, we propose a two-module iterative training algorithm to refine pseudo labels and supervise better object detector progressively. In the localization adaptation module, we propose a regularization loss to reduce the proportion of discriminative parts in original pseudo ground-truths, obtaining better pseudo ground-truths for further training. In the semi-supervised module, we propose a two tasks instance-level split method to select high-quality labels for training a semi-supervised detector. Experimental results on different benchmarks verify the effectiveness of W2N, and our W2N outperforms all existing pure WSOD methods and transfer learning methods. Our code is publicly available at https://github.com/1170300714/w2n_wsod.

</details>

### Talisman: Targeted Active Learning for Object Detection with Rare Classes and Slices Using Submodular Mutual Information.
- **链接**: [arXiv:2112.00166](https://arxiv.org/abs/2112.00166) · 📚 被引 18
- **作者**: Suraj Kothawade, Saikat Ghosh, Sumit Shekhar, Yu Xiang, Rishabh K. Iyer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks based object detectors have shown great success in a variety of domains like autonomous vehicles, biomedical imaging, etc. It is known that their success depends on a large amount of data from the domain of interest. While deep models often perform well in terms of overall accuracy, they often struggle in performance on rare yet critical data slices. For example, data slices like "motorcycle at night" or "bicycle at night" are often rare but very critical slices for self-driving applications and false negatives on such rare slices could result in ill-fated failures and accidents. Active learning (AL) is a well-known paradigm to incrementally and adaptively build training datasets with a human in the loop. However, current AL based acquisition functions are not well-equipped to tackle real-world datasets with rare slices, since they are based on uncertainty scores or global descriptors of the image. We propose TALISMAN, a novel framework for Targeted Active Learning or object detectIon with rare slices using Submodular MutuAl iNformation. Our method uses the submodular mutual information functions instantiated using features of the region of interest (RoI) to efficiently target and acquire data points with rare slices. We evaluate our framework on the standard PASCAL VOC07+12 and BDD100K, a real-world self-driving dataset. We observe that TALISMAN outperforms other methods by in terms of average precision on rare slices, and in terms of mAP.

</details>

### SPSN: Superpixel Prototype Sampling Network for RGB-D Salient Object Detection.
- **链接**: [arXiv:2207.07898](https://arxiv.org/abs/2207.07898) · 📚 被引 92
- **作者**: Minhyeok Lee, Chaewon Park, Suhwan Cho, Sangyoun Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> RGB-D salient object detection (SOD) has been in the spotlight recently because it is an important preprocessing operation for various vision tasks. However, despite advances in deep learning-based methods, RGB-D SOD is still challenging due to the large domain gap between an RGB image and the depth map and low-quality depth maps. To solve this problem, we propose a novel superpixel prototype sampling network (SPSN) architecture. The proposed model splits the input RGB image and depth map into component superpixels to generate component prototypes. We design a prototype sampling network so that the network only samples prototypes corresponding to salient objects. In addition, we propose a reliance selection module to recognize the quality of each RGB and depth feature map and adaptively weight them in proportion to their reliability. The proposed method makes the model robust to inconsistencies between RGB images and depth maps and eliminates the influence of non-salient objects. Our method is evaluated on five popular datasets, achieving state-of-the-art performance. We prove the effectiveness of the proposed method through comparative experiments.

</details>

### Should All Proposals Be Treated Equally in Object Detection?
- **链接**: [arXiv:2207.03520](https://arxiv.org/abs/2207.03520) · 📚 被引 3
- **作者**: Yunsheng Li, Yinpeng Chen, Xiyang Dai, Dongdong Chen, Mengchen Liu, Pei Yu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The complexity-precision trade-off of an object detector is a critical problem for resource constrained vision tasks. Previous works have emphasized detectors implemented with efficient backbones. The impact on this trade-off of proposal processing by the detection head is investigated in this work. It is hypothesized that improved detection efficiency requires a paradigm shift, towards the unequal processing of proposals, assigning more computation to good proposals than poor ones. This results in better utilization of available computational budget, enabling higher accuracy for the same FLOPS. We formulate this as a learning problem where the goal is to assign operators to proposals, in the detection head, so that the total computational cost is constrained and the precision is maximized. The key finding is that such matching can be learned as a function that maps each proposal embedding into a one-hot code over operators. While this function induces a complex dynamic network routing mechanism, it can be implemented by a simple MLP and learned end-to-end with off-the-shelf object detectors. This 'dynamic proposal processing' (DPP) is shown to outperform state-of-the-art end-to-end object detectors (DETR, Sparse R-CNN) by a clear margin for a given computational complexity.

</details>

### Diverse Learner: Exploring Diverse Supervision for Semi-supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20056-4_37) · 📚 被引 2
- **作者**: Linfeng Li, Minyue Jiang, Yue Yu, Wei Zhang, Xiangru Lin, Yingying Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### PseCo: Pseudo Labeling and Consistency Training for Semi-Supervised Object Detection.
- **链接**: [arXiv:2203.16317](https://arxiv.org/abs/2203.16317) · [代码](https://github.com/ligang-cs/PseCo) · 📚 被引 127
- **作者**: Gang Li, Xiang Li, Yujie Wang, Yichao Wu, Ding Liang, Shanshan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we delve into two key techniques in Semi-Supervised Object Detection (SSOD), namely pseudo labeling and consistency training. We observe that these two techniques currently neglect some important properties of object detection, hindering efficient learning on unlabeled data. Specifically, for pseudo labeling, existing works only focus on the classification score yet fail to guarantee the localization precision of pseudo boxes; For consistency training, the widely adopted random-resize training only considers the label-level consistency but misses the feature-level one, which also plays an important role in ensuring the scale invariance. To address the problems incurred by noisy pseudo boxes, we design Noisy Pseudo box Learning (NPL) that includes Prediction-guided Label Assignment (PLA) and Positive-proposal Consistency Voting (PCV). PLA relies on model predictions to assign labels and makes it robust to even coarse pseudo boxes; while PCV leverages the regression consistency of positive proposals to reflect the localization quality of pseudo boxes. Furthermore, in consistency training, we propose Multi-view Scale-invariant Learning (MSL) that includes mechanisms of both label- and feature-level consistency, where feature consistency is achieved by aligning shifted feature pyramids between two images with identical content but varied scales. On COCO benchmark, our method, termed PSEudo labeling and COnsistency training (PseCo), outperforms the SOTA (Soft Teacher) by 2.0, 1.8, 2.0 points under 1%, 5%, and 10% labelling ratios, respectively. It also significantly improves the learning efficiency for SSOD, e.g., PseCo halves the training time of the SOTA approach but achieves even better performance. Code is available at https://github.com/ligang-cs/PseCo.

</details>

### Exploring Plain Vision Transformer Backbones for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_17)
- **作者**: Yanghao Li, Hanzi Mao, Ross B. Girshick, Kaiming He
- **🏷️ 机构**: MIT
- **会议**: ECCV 2022

### End-to-End Weakly Supervised Object Detection with Sparse Proposal Evolution.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_13) · 📚 被引 22
- **作者**: Mingxiang Liao, Fang Wan, Yuan Yao, Zhenjun Han, Jialing Zou, Yuze Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Open-Set Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20056-4_9)
- **作者**: Yen-Cheng Liu, Chih-Yao Ma, Xiaoliang Dai, Junjiao Tian, Peter Vajda, Zijian He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Robust Object Detection with Inaccurate Bounding Boxes.
- **链接**: [arXiv:2207.09697](https://arxiv.org/abs/2207.09697) · [代码](https://github.com/cxliu0/OA-MIL)
- **作者**: Chengxin Liu, Kewei Wang, Hao Lu, Zhiguo Cao, Ziming Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning accurate object detectors often requires large-scale training data with precise object bounding boxes. However, labeling such data is expensive and time-consuming. As the crowd-sourcing labeling process and the ambiguities of the objects may raise noisy bounding box annotations, the object detectors will suffer from the degenerated training data. In this work, we aim to address the challenge of learning robust object detectors with inaccurate bounding boxes. Inspired by the fact that localization precision suffers significantly from inaccurate bounding boxes while classification accuracy is less affected, we propose leveraging classification as a guidance signal for refining localization results. Specifically, by treating an object as a bag of instances, we introduce an Object-Aware Multiple Instance Learning approach (OA-MIL), featured with object-aware instance selection and object-aware instance extension. The former aims to select accurate instances for training, instead of directly using inaccurate box annotations. The latter focuses on generating high-quality instances for selection. Extensive experiments on synthetic noisy datasets (i.e., noisy PASCAL VOC and MS-COCO) and a real noisy wheat head dataset demonstrate the effectiveness of our OA-MIL. Code is available at https://github.com/cxliu0/OA-MIL.

</details>

### Mutually Reinforcing Structure with Proposal Contrastive Consistency for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20044-1_23) · 📚 被引 9
- **作者**: TianXue Ma, Mingwei Bi, Jian Zhang, Wang Yuan, Zhizhong Zhang, Yuan Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Few-Shot End-to-End Object Detection via Constantly Concentrated Encoding Across Heads.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19809-0_4) · 📚 被引 13
- **作者**: Jiawei Ma, Guangxing Han, Shiyuan Huang, Yuncong Yang, Shih-Fu Chang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Simple Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_42)
- **作者**: Matthias Minderer, Alexey A. Gritsenko, Austin Stone, Maxim Neumann, Dirk Weissenborn, Alexey Dosovitskiy et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### DetMatch: Two Teachers are Better than One for Joint 2D and 3D Semi-Supervised Object Detection.
- **链接**: [arXiv:2203.09510](https://arxiv.org/abs/2203.09510) · [代码](https://github.com/Divadi/DetMatch) · 📚 被引 24
- **作者**: Jinhyung Park, Chenfeng Xu, Yiyang Zhou, Masayoshi Tomizuka, Wei Zhan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While numerous 3D detection works leverage the complementary relationship between RGB images and point clouds, developments in the broader framework of semi-supervised object recognition remain uninfluenced by multi-modal fusion. Current methods develop independent pipelines for 2D and 3D semi-supervised learning despite the availability of paired image and point cloud frames. Observing that the distinct characteristics of each sensor cause them to be biased towards detecting different objects, we propose DetMatch, a flexible framework for joint semi-supervised learning on 2D and 3D modalities. By identifying objects detected in both sensors, our pipeline generates a cleaner, more robust set of pseudo-labels that both demonstrates stronger performance and stymies single-modality error propagation. Further, we leverage the richer semantics of RGB images to rectify incorrect 3D class predictions and improve localization of 3D boxes. Evaluating on the challenging KITTI and Waymo datasets, we improve upon strong semi-supervised learning methods and observe higher quality pseudo-labels. Code will be released at https://github.com/Divadi/DetMatch

</details>

### Few-Shot Object Detection by Knowledge Distillation Using Bag-of-Visual-Words Representations.
- **链接**: [arXiv:2207.12049](https://arxiv.org/abs/2207.12049) · 📚 被引 17
- **作者**: Wenjie Pei, Shuang Wu, Dianwen Mei, Fanglin Chen, Jiandong Tian, Guangming Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While fine-tuning based methods for few-shot object detection have achieved remarkable progress, a crucial challenge that has not been addressed well is the potential class-specific overfitting on base classes and sample-specific overfitting on novel classes. In this work we design a novel knowledge distillation framework to guide the learning of the object detector and thereby restrain the overfitting in both the pre-training stage on base classes and fine-tuning stage on novel classes. To be specific, we first present a novel Position-Aware Bag-of-Visual-Words model for learning a representative bag of visual words (BoVW) from a limited size of image set, which is used to encode general images based on the similarities between the learned visual words and an image. Then we perform knowledge distillation based on the fact that an image should have consistent BoVW representations in two different feature spaces. To this end, we pre-learn a feature space independently from the object detection, and encode images using BoVW in this space. The obtained BoVW representation for an image can be considered as distilled knowledge to guide the learning of object detector: the extracted features by the object detector for the same image are expected to derive the consistent BoVW representations with the distilled knowledge. Extensive experiments validate the effectiveness of our method and demonstrate the superiority over other state-of-the-art methods.

</details>

### Efficient One-Stage Video Object Detection by Exploiting Temporal Consistency.
- **链接**: [arXiv:2402.09241](https://arxiv.org/abs/2402.09241) · [代码](https://github.com/guanxiongsun/vfe.pytorch) · 📚 被引 15
- **作者**: Guanxiong Sun, Yang Hua, Guosheng Hu, Neil Robertson
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, one-stage detectors have achieved competitive accuracy and faster speed compared with traditional two-stage detectors on image data. However, in the field of video object detection (VOD), most existing VOD methods are still based on two-stage detectors. Moreover, directly adapting existing VOD methods to one-stage detectors introduces unaffordable computational costs. In this paper, we first analyse the computational bottlenecks of using one-stage detectors for VOD. Based on the analysis, we present a simple yet efficient framework to address the computational bottlenecks and achieve efficient one-stage VOD by exploiting the temporal consistency in video frames. Specifically, our method consists of a location-prior network to filter out background regions and a size-prior network to skip unnecessary computations on low-level feature maps for specific frames. We test our method on various modern one-stage detectors and conduct extensive experiments on the ImageNet VID dataset. Excellent experimental results demonstrate the superior effectiveness, efficiency, and compatibility of our method. The code is available at https://github.com/guanxiongsun/vfe.pytorch.

</details>

### Active Learning Strategies for Weakly-Supervised Object Detection.
- **链接**: [arXiv:2207.12112](https://arxiv.org/abs/2207.12112) · [代码](https://github.com/huyvvo/BiB)
- **作者**: Huy V. Vo, Oriane Siméoni, Spyros Gidaris, Andrei Bursuc, Patrick Pérez, Jean Ponce
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detectors trained with weak annotations are affordable alternatives to fully-supervised counterparts. However, there is still a significant performance gap between them. We propose to narrow this gap by fine-tuning a base pre-trained weakly-supervised detector with a few fully-annotated samples automatically selected from the training set using ``box-in-box'' (BiB), a novel active learning strategy designed specifically to address the well-documented failure modes of weakly-supervised detectors. Experiments on the VOC07 and COCO benchmarks show that BiB outperforms other active learning techniques and significantly improves the base weakly-supervised detector's performance with only a few fully-annotated images per class. BiB reaches 97% of the performance of fully-supervised Fast RCNN with only 10% of fully-annotated images on VOC07. On COCO, using on average 10 fully-annotated images per class, or equivalently 1% of the training set, BiB also reduces the performance gap (in AP) between the weakly-supervised detector and the fully-supervised Fast RCNN by over 70%, showing a good trade-off between performance and data efficiency. Our code is publicly available at https://github.com/huyvvo/BiB.

</details>

### PTSEFormer: Progressive Temporal-Spatial Enhanced TransFormer Towards Video Object Detection.
- **链接**: [arXiv:2209.02242](https://arxiv.org/abs/2209.02242) · [代码](https://github.com/Hon-Wong/PTSEFormer) · 📚 被引 39
- **作者**: Han Wang, Jun Tang, Xiaodong Liu, Shanyan Guan, Rong Xie, Li Song
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed a trend of applying context frames to boost the performance of object detection as video object detection. Existing methods usually aggregate features at one stroke to enhance the feature. These methods, however, usually lack spatial information from neighboring frames and suffer from insufficient feature aggregation. To address the issues, we perform a progressive way to introduce both temporal information and spatial information for an integrated enhancement. The temporal information is introduced by the temporal feature aggregation model (TFAM), by conducting an attention mechanism between the context frames and the target frame (i.e., the frame to be detected). Meanwhile, we employ a Spatial Transition Awareness Model (STAM) to convey the location transition information between each context frame and target frame. Built upon a transformer-based detector DETR, our PTSEFormer also follows an end-to-end fashion to avoid heavy post-processing procedures while achieving 88.1% mAP on the ImageNet VID dataset. Codes are available at https://github.com/Hon-Wong/PTSEFormer.

</details>

### Bridging Images and Videos: A Simple Learning Framework for Large Vocabulary Video Object Detection.
- **链接**: [arXiv:2212.10147](https://arxiv.org/abs/2212.10147) · 📚 被引 6
- **作者**: Sanghyun Woo, Kwanyong Park, Seoung Wug Oh, In So Kweon, Joon-Young Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling object taxonomies is one of the important steps toward a robust real-world deployment of recognition systems. We have faced remarkable progress in images since the introduction of the LVIS benchmark. To continue this success in videos, a new video benchmark, TAO, was recently presented. Given the recent encouraging results from both detection and tracking communities, we are interested in marrying those two advances and building a strong large vocabulary video tracker. However, supervisions in LVIS and TAO are inherently sparse or even missing, posing two new challenges for training the large vocabulary trackers. First, no tracking supervisions are in LVIS, which leads to inconsistent learning of detection (with LVIS and TAO) and tracking (only with TAO). Second, the detection supervisions in TAO are partial, which results in catastrophic forgetting of absent LVIS categories during video fine-tuning. To resolve these challenges, we present a simple but effective learning framework that takes full advantage of all available training data to learn detection and tracking while not losing any LVIS categories to recognize. With this new learning scheme, we show that consistent improvements of various large vocabulary trackers are capable, setting strong baseline results on the challenging TAO benchmarks.

</details>

### UC-OWOD: Unknown-Classified Open World Object Detection.
- **链接**: [arXiv:2207.11455](https://arxiv.org/abs/2207.11455) · [代码](https://github.com/JohnWuzh/UC-OWOD) · 📚 被引 64
- **作者**: Zhiheng Wu, Yue Lu, Xingyu Chen, Zhengxing Wu, Liwen Kang, Junzhi Yu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open World Object Detection (OWOD) is a challenging computer vision problem that requires detecting unknown objects and gradually learning the identified unknown classes. However, it cannot distinguish unknown instances as multiple unknown classes. In this work, we propose a novel OWOD problem called Unknown-Classified Open World Object Detection (UC-OWOD). UC-OWOD aims to detect unknown instances and classify them into different unknown classes. Besides, we formulate the problem and devise a two-stage object detector to solve UC-OWOD. First, unknown label-aware proposal and unknown-discriminative classification head are used to detect known and unknown objects. Then, similarity-based unknown classification and unknown clustering refinement modules are constructed to distinguish multiple unknown classes. Moreover, two novel evaluation protocols are designed to evaluate unknown-class detection. Abundant experiments and visualizations prove the effectiveness of the proposed method. Code is available at https://github.com/JohnWuzh/UC-OWOD.

</details>

### Multi-faceted Distillation of Base-Novel Commonality for Few-Shot Object Detection.
- **链接**: [arXiv:2207.11184](https://arxiv.org/abs/2207.11184) · 📚 被引 44
- **作者**: Shuang Wu, Wenjie Pei, Dianwen Mei, Fanglin Chen, Jiandong Tian, Guangming Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of existing methods for few-shot object detection follow the fine-tuning paradigm, which potentially assumes that the class-agnostic generalizable knowledge can be learned and transferred implicitly from base classes with abundant samples to novel classes with limited samples via such a two-stage training strategy. However, it is not necessarily true since the object detector can hardly distinguish between class-agnostic knowledge and class-specific knowledge automatically without explicit modeling. In this work we propose to learn three types of class-agnostic commonalities between base and novel classes explicitly: recognition-related semantic commonalities, localization-related semantic commonalities and distribution commonalities. We design a unified distillation framework based on a memory bank, which is able to perform distillation of all three types of commonalities jointly and efficiently. Extensive experiments demonstrate that our method can be readily integrated into most of existing fine-tuning based methods and consistently improve the performance by a large margin.

</details>

### RFLA: Gaussian Receptive Field Based Label Assignment for Tiny Object Detection.
- **链接**: [arXiv:2208.08738](https://arxiv.org/abs/2208.08738) · [代码](https://github.com/Chasel-Tsui/mmdet-rfla) · 📚 被引 290
- **作者**: Chang Xu, Jinwang Wang, Wen Yang, Huai Yu, Lei Yu, Gui-Song Xia
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting tiny objects is one of the main obstacles hindering the development of object detection. The performance of generic object detectors tends to drastically deteriorate on tiny object detection tasks. In this paper, we point out that either box prior in the anchor-based detector or point prior in the anchor-free detector is sub-optimal for tiny objects. Our key observation is that the current anchor-based or anchor-free label assignment paradigms will incur many outlier tiny-sized ground truth samples, leading to detectors imposing less focus on the tiny objects. To this end, we propose a Gaussian Receptive Field based Label Assignment (RFLA) strategy for tiny object detection. Specifically, RFLA first utilizes the prior information that the feature receptive field follows Gaussian distribution. Then, instead of assigning samples with IoU or center sampling strategy, a new Receptive Field Distance (RFD) is proposed to directly measure the similarity between the Gaussian receptive field and ground truth. Considering that the IoU-threshold based and center sampling strategy are skewed to large objects, we further design a Hierarchical Label Assignment (HLA) module based on RFD to achieve balanced learning for tiny objects. Extensive experiments on four datasets demonstrate the effectiveness of the proposed methods. Especially, our approach outperforms the state-of-the-art competitors with 4.0 AP points on the AI-TOD dataset. Codes are available at https://github.com/Chasel-Tsui/mmdet-rfla

</details>

### Prediction-Guided Distillation for Dense Object Detection.
- **链接**: [arXiv:2203.05469](https://arxiv.org/abs/2203.05469) · [代码](https://github.com/ChenhongyiYang/PGD) · 📚 被引 30
- **作者**: Chenhongyi Yang, Mateusz Ochal, Amos Storkey, Elliot J. Crowley
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world object detection models should be cheap and accurate. Knowledge distillation (KD) can boost the accuracy of a small, cheap detection model by leveraging useful information from a larger teacher model. However, a key challenge is identifying the most informative features produced by the teacher for distillation. In this work, we show that only a very small fraction of features within a ground-truth bounding box are responsible for a teacher's high detection performance. Based on this, we propose Prediction-Guided Distillation (PGD), which focuses distillation on these key predictive regions of the teacher and yields considerable gains in performance over many existing KD baselines. In addition, we propose an adaptive weighting scheme over the key regions to smooth out their influence and achieve even better performance. Our proposed approach outperforms current state-of-the-art KD baselines on a variety of advanced one-stage detection architectures. Specifically, on the COCO dataset, our method achieves between +3.1% and +4.6% AP improvement using ResNet-101 and ResNet-50 as the teacher and student backbones, respectively. On the CrowdHuman dataset, we achieve +3.2% and +2.0% improvements in MR and AP, also using these backbones. Our code is available at https://github.com/ChenhongyiYang/PGD.

</details>

### MTTrans: Cross-domain Object Detection with Mean Teacher Transformer.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_37) · 📚 被引 53
- **作者**: Jinze Yu, Jiaming Liu, Xiaobao Wei, Haoyi Zhou, Yohei Nakata, Denis A. Gudovskiy et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Time-rEversed DiffusioN tEnsor Transformer: A New TENET of Few-Shot Object Detection.
- **链接**: [arXiv:2210.16897](https://arxiv.org/abs/2210.16897) · 📚 被引 21
- **作者**: Shan Zhang, Naila Murray, Lei Wang, Piotr Koniusz
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Saliency Hierarchy Modeling via Generative Kernels for Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19815-1_33) · 📚 被引 11
- **作者**: Wenhu Zhang, Liangli Zheng, Huanyu Wang, Xintian Wu, Xi Li
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

### Exploiting Unlabeled Data with Vision and Language Models for Object Detection.
- **链接**: [arXiv:2207.08954](https://arxiv.org/abs/2207.08954) · 📚 被引 87
- **作者**: Shiyu Zhao, Zhixing Zhang, Samuel Schulter, Long Zhao, B. G. Vijay Kumar, Anastasis Stathopoulos et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Dense Teacher: Dense Pseudo-Labels for Semi-supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_3)
- **作者**: Hongyu Zhou, Zheng Ge, Songtao Liu, Weixin Mao, Zeming Li, Haiyan Yu et al.
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2022

### Bottom Up Top Down Detection Transformers for Language Grounding in Images and Point Clouds.
- **链接**: [arXiv:2112.08879](https://arxiv.org/abs/2112.08879) · 📚 被引 70
- **作者**: Ayush Jain, Nikolaos Gkanatsios, Ishita Mediratta, Katerina Fragkiadaki
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most models tasked to ground referential utterances in 2D and 3D scenes learn to select the referred object from a pool of object proposals provided by a pre-trained detector. This is limiting because an utterance may refer to visual entities at various levels of granularity, such as the chair, the leg of the chair, or the tip of the front leg of the chair, which may be missed by the detector. We propose a language grounding model that attends on the referential utterance and on the object proposal pool computed from a pre-trained detector to decode referenced objects with a detection head, without selecting them from the pool. In this way, it is helped by powerful pre-trained object detectors without being restricted by their misses. We call our model Bottom Up Top Down DEtection TRansformers (BUTD-DETR) because it uses both language guidance (top down) and objectness guidance (bottom-up) to ground referential utterances in images and point clouds. Moreover, BUTD-DETR casts object detection as referential grounding and uses object labels as language prompts to be grounded in the visual scene, augmenting supervision for the referential grounding task in this way. The proposed model sets a new state-of-the-art across popular 3D language grounding benchmarks with significant performance gains over previous 3D approaches (12.6% on SR3D, 11.6% on NR3D and 6.3% on ScanRefer). When applied in 2D images, it performs on par with the previous state of the art. We ablate the design choices of our model and quantify their contribution to performance. Our code and checkpoints can be found at the project website https://butd-detr.github.io.

</details>

## 跨领域论文（完整笔记在其他领域）

- Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Multimodal Object Detection via Probabilistic Ensembling. → [multimodal](../multimodal/Guideline%202022.md)
- SpatialDETR: Robust Scalable Transformer-Based 3D Object Detection From Multi-view Camera Images With Global Cross-Sensor Attention. → [3d-detection](../3d-detection/Guideline%202022.md)
- 3D Object Detection with a Self-supervised Lidar Scene Flow Backbone. → [3d-detection](../3d-detection/Guideline%202022.md)
- Cross-Modality Knowledge Distillation Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention for Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DEVIANT: Depth EquiVarIAnt NeTwork for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Densely Constrained Depth Estimator for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Unsupervised Domain Adaptation for Monocular 3D Object Detection via Self-training. → [3d-detection](../3d-detection/Guideline%202022.md)
- CODA: A Real-World Road Corner Case Dataset for Object Detection in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Enhancing Multi-modal Features Using Local Self-attention for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Semi-supervised Monocular 3D Object Detection by Multi-view Consistency. → [3d-detection](../3d-detection/Guideline%202022.md)
- Multimodal Transformer for Automatic 3D Annotation and Object Detection. → [multimodal](../multimodal/Guideline%202022.md)
- PETR: Position Embedding Transformation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Class-Agnostic Object Detection with Multi-modal Transformer. → [multimodal](../multimodal/Guideline%202022.md)
- Lidar Point Cloud Guided Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DID-M3D: Decoupling Instance Depth for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- FCAF3D: Fully Convolutional Anchor-Free 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rethinking IoU-based Optimization for Single-stage 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- PillarNet: Real-Time and High-Performance Pillar-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- EAutoDet: Efficient Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- Monocular 3D Object Detection with Depth from Motion. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Graph R-CNN: Towards Accurate 3D Object Detection with Semantic-Decorated Local Graph. → [3d-detection](../3d-detection/Guideline%202022.md)
- Semi-supervised 3D Object Detection with Proficient Teachers. → [3d-detection](../3d-detection/Guideline%202022.md)
- ProposalContrast: Unsupervised Pre-training for LiDAR-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- MVSalNet: Multi-view Augmentation for RGB-D Salient Object Detection. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- CenterFormer: Center-Based Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
