# Object Detection — 2020 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Generative Sparse Detection Networks for 3D Single-Shot Object Detection.
- **链接**: [arXiv:2006.12356](https://arxiv.org/abs/2006.12356) · 📚 被引 107
- **作者**: JunYoung Gwak, Christopher B. Choy, Silvio Savarese
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection has been widely studied due to its potential applicability to many promising areas such as robotics and augmented reality. Yet, the sparse nature of the 3D data poses unique challenges to this task. Most notably, the observable surface of the 3D point clouds is disjoint from the center of the instance to ground the bounding box prediction on. To this end, we propose Generative Sparse Detection Network (GSDN), a fully-convolutional single-shot sparse detection network that efficiently generates the support for object proposals. The key component of our model is a generative sparse tensor decoder, which uses a series of transposed convolutions and pruning layers to expand the support of sparse tensors while discarding unlikely object centers to maintain minimal runtime and memory footprint. GSDN can process unprecedentedly large-scale inputs with a single fully-convolutional feed-forward pass, thus does not require the heuristic post-processing stage that stitches results from sliding windows as other previous methods have. We validate our approach on three 3D indoor datasets including the large-scale 3D indoor reconstruction dataset where our method outperforms the state-of-the-art methods by a relative improvement of 7.14% while being 3.78 times faster than the best prior work.

</details>

### Few-Shot Object Detection and Viewpoint Estimation for Objects in the Wild.
- **链接**: [arXiv:2007.12107](https://arxiv.org/abs/2007.12107) · 📚 被引 100
- **作者**: Yang Xiao, Renaud Marlet
- **🏷️ 机构**: Laboratoire d\'Informatique Gaspard Monge, IMAGINE, Ecole des Ponts ParisTech, 52835 Champs-sur-Marne, Marne-la-Vallee, France, Imagine, ENPC, 52835 Marne-la-Vallee, NOUVELLE-AQUITAINE, France, 77455, IMAGINE, Laboratoire d\'Informatique Gaspard Monge, 129972 Marne-la-Valle, ., France, 77455
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects and estimating their viewpoints in images are key tasks of 3D scene understanding. Recent approaches have achieved excellent results on very large benchmarks for object detection and viewpoint estimation. However, performances are still lagging behind for novel object categories with few samples. In this paper, we tackle the problems of few-shot object detection and few-shot viewpoint estimation. We demonstrate on both tasks the benefits of guiding the network prediction with class-representative features extracted from data in different modalities: image patches for object detection, and aligned 3D models for viewpoint estimation. Despite its simplicity, our method outperforms state-of-the-art methods by a large margin on a range of datasets, including PASCAL and COCO for few-shot object detection, and Pascal3D+ and ObjectNet3D for few-shot viewpoint estimation. Furthermore, when the 3D model is not available, we introduce a simple category-agnostic viewpoint estimation method by exploiting geometrical similarities and consistent pose labelling across different classes. While it moderately reduces performance, this approach still obtains better results than previous methods in this setting. Last, for the first time, we tackle the combination of both few-shot tasks, on three challenging benchmarks for viewpoint estimation in the wild, ObjectNet3D, Pascal3D+ and Pix3D, showing very promising results.

</details>

### Video Object Detection via Object-Level Temporal Aggregation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58568-6_10)
- **作者**: Chun-Han Yao, Chen Fang, Xiaohui Shen, Yangyue Wan, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: ECCV 2020

### Arbitrary-Oriented Object Detection with Circular Smooth Label.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58598-3_40) · 📚 被引 560
- **作者**: Xue Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Many-Shot from Low-Shot: Learning to Annotate Using Mixed Supervision for Object Detection.
- **链接**: [arXiv:2008.09694](https://arxiv.org/abs/2008.09694) · 📚 被引 13
- **作者**: Carlo Biffi, Steven McDonagh, Philip H. S. Torr, Ales Leonardis, Sarah Parisot
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has witnessed significant progress by relying on large, manually annotated datasets. Annotating such datasets is highly time consuming and expensive, which motivates the development of weakly supervised and few-shot object detection methods. However, these methods largely underperform with respect to their strongly supervised counterpart, as weak training signals \emph{often} result in partial or oversized detections. Towards solving this problem we introduce, for the first time, an online annotation module (OAM) that learns to generate a many-shot set of \emph{reliable} annotations from a larger volume of weakly labelled images. Our OAM can be jointly trained with any fully supervised two-stage object detection method, providing additional training annotations on the fly. This results in a fully end-to-end strategy that only requires a low-shot set of fully annotated images. The integration of the OAM with Fast(er) R-CNN improves their performance by $17\%$ mAP, $9\%$ AP50 on PASCAL VOC 2007 and MS-COCO benchmarks, and significantly outperforms competing methods using mixed supervision.

</details>

### TIDE: A General Toolbox for Identifying Object Detection Errors.
- **链接**: [arXiv:2008.08115](https://arxiv.org/abs/2008.08115)
- **作者**: Daniel Bolya, Sean Foley, James Hays, Judy Hoffman
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce TIDE, a framework and associated toolbox for analyzing the sources of error in object detection and instance segmentation algorithms. Importantly, our framework is applicable across datasets and can be applied directly to output prediction files without required knowledge of the underlying prediction system. Thus, our framework can be used as a drop-in replacement for the standard mAP computation while providing a comprehensive analysis of each model's strengths and weaknesses. We segment errors into six types and, crucially, are the first to introduce a technique for measuring the contribution of each error in a way that isolates its effect on overall performance. We show that such a representation is critical for drawing accurate, comprehensive conclusions through in-depth analysis across 4 datasets and 7 recognition models. Available at https://dbolya.github.io/tide/

</details>

### APRICOT: A Dataset of Physical Adversarial Attacks on Object Detection.
- **链接**: [arXiv:1912.08166](https://arxiv.org/abs/1912.08166) · 📚 被引 38
- **作者**: A. Braunegg, Amartya Chakraborty, Michael Krumdick, Nicole Lape, Sara Leary, Keith Manville et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Physical adversarial attacks threaten to fool object detection systems, but reproducible research on the real-world effectiveness of physical patches and how to defend against them requires a publicly available benchmark dataset. We present APRICOT, a collection of over 1,000 annotated photographs of printed adversarial patches in public locations. The patches target several object categories for three COCO-trained detection models, and the photos represent natural variation in position, distance, lighting conditions, and viewing angle. Our analysis suggests that maintaining adversarial robustness in uncontrolled settings is highly challenging, but it is still possible to produce targeted detections under white-box and sometimes black-box settings. We establish baselines for defending against adversarial patches through several methods, including a detector supervised with synthetic data and unsupervised methods such as kernel density estimation, Bayesian uncertainty, and reconstruction error. Our results suggest that adversarial patches can be effectively flagged, both in a high-knowledge, attack-specific scenario, and in an unsupervised setting where patches are detected as anomalies in natural images. This dataset and the described experiments provide a benchmark for future research on the effectiveness of and defenses against physical adversarial objects in the wild.

</details>

### End-to-End Object Detection with Transformers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58452-8_13)
- **作者**: Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, Sergey Zagoruyko
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Progressively Guided Alternate Refinement Network for RGB-D Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58598-3_31) · 📚 被引 124
- **作者**: Shuhan Chen, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### PIoU Loss: Towards Accurate Oriented Object Detection in Complex Environments.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58558-7_12) · 📚 被引 282
- **作者**: Zhiming Chen, Kean Chen, Weiyao Lin, John See, Hui Yu, Yan Ke et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Hierarchical Context Embedding for Region-Based Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_38) · 📚 被引 26
- **作者**: Zhao-Min Chen, Xin Jin, Borui Zhao, Xiu-Shen Wei, Yanwen Guo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Dive Deeper into Box for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58542-6_25)
- **作者**: Ran Chen, Yong Liu, Mengdan Zhang, Shu Liu, Bei Yu, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### SPOT: Selective Point Cloud Voting for Better Proposal in Point Cloud Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58621-8_14) · 📚 被引 9
- **作者**: Hongyuan Du, Linjun Li, Bo Liu, Nuno Vasconcelos
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Corner Proposal Network for Anchor-Free, Two-Stage Object Detection.
- **链接**: [arXiv:2007.13816](https://arxiv.org/abs/2007.13816) · [代码](https://github.com/Duankaiwen/CPNDet) · 📚 被引 93
- **作者**: Kaiwen Duan, Lingxi Xie, Honggang Qi, Song Bai, Qingming Huang, Qi Tian
- **🏷️ 机构**: USTC
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of object detection is to determine the class and location of objects in an image. This paper proposes a novel anchor-free, two-stage framework which first extracts a number of object proposals by finding potential corner keypoint combinations and then assigns a class label to each proposal by a standalone classification stage. We demonstrate that these two stages are effective solutions for improving recall and precision, respectively, and they can be integrated into an end-to-end network. Our approach, dubbed Corner Proposal Network (CPN), enjoys the ability to detect objects of various scales and also avoids being confused by a large number of false-positive proposals. On the MS-COCO dataset, CPN achieves an AP of 49.2% which is competitive among state-of-the-art object detection methods. CPN also fits the scenario of computational efficiency, which achieves an AP of 41.6%/39.7% at 26.2/43.3 FPS, surpassing most competitors with the same inference speed. Code is available at https://github.com/Duankaiwen/CPNDet

</details>

### Dual Refinement Underwater Object Detection Network.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58565-5_17)
- **作者**: Baojie Fan, Wei Chen, Yang Cong, Jiandong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### BBS-Net: RGB-D Salient Object Detection with a Bifurcated Backbone Strategy Network.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58610-2_17) · 📚 被引 294
- **作者**: Deng-Ping Fan, Yingjie Zhai, Ali Borji, Jufeng Yang, Ling Shao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Highly Efficient Salient Object Detection with 100K Parameters.
- **链接**: [arXiv:2003.05643](https://arxiv.org/abs/2003.05643)
- **作者**: Shanghua Gao, Yong-Qiang Tan, Ming-Ming Cheng, Chengze Lu, Yunpeng Chen, Shuicheng Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Salient object detection models often demand a considerable amount of computation cost to make precise prediction for each pixel, making them hardly applicable on low-power devices. In this paper, we aim to relieve the contradiction between computation cost and model performance by improving the network efficiency to a higher degree. We propose a flexible convolutional module, namely generalized OctConv (gOctConv), to efficiently utilize both in-stage and cross-stages multi-scale features, while reducing the representation redundancy by a novel dynamic weight decay scheme. The effective dynamic weight decay scheme stably boosts the sparsity of parameters during training, supports learnable number of channels for each scale in gOctConv, allowing 80% of parameters reduce with negligible performance drop. Utilizing gOctConv, we build an extremely light-weighted model, namely CSNet, which achieves comparable performance with about 0.2% parameters (100k) of large models on popular salient object detection benchmarks.

</details>

### Mining Inter-Video Proposal Relations for Video Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_26) · 📚 被引 67
- **作者**: Mingfei Han, Yali Wang, Xiaojun Chang, Yu Qiao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2020

### Streaming Object Detection for 3-D Point Clouds.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58523-5_25)
- **作者**: Wei Han, Zhengdong Zhang, Benjamin Caine, Brandon Yang, Christoph Sprunk, Ouais Alsharif et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### LabelEnc: A New Intermediate Supervision Method for Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58595-2_32) · 📚 被引 18
- **作者**: Miao Hao, Yitao Liu, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2020

### Domain Adaptive Object Detection via Asymmetric Tri-Way Faster-RCNN.
- **链接**: [arXiv:2007.01571](https://arxiv.org/abs/2007.01571) · 📚 被引 118
- **作者**: Zhenwei He, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional object detection models inevitably encounter a performance drop as the domain disparity exists. Unsupervised domain adaptive object detection is proposed recently to reduce the disparity between domains, where the source domain is label-rich while the target domain is label-agnostic. The existing models follow a parameter shared siamese structure for adversarial domain alignment, which, however, easily leads to the collapse and out-of-control risk of the source domain and brings negative impact to feature adaption. The main reason is that the labeling unfairness (asymmetry) between source and target makes the parameter sharing mechanism unable to adapt. Therefore, in order to avoid the source domain collapse risk caused by parameter sharing, we propose an asymmetric tri-way Faster-RCNN (ATF) for domain adaptive object detection. Our ATF model has two distinct merits: 1) A ancillary net supervised by source label is deployed to learn ancillary target features and simultaneously preserve the discrimination of source domain, which enhances the structural discrimination (object classification vs. bounding box regression) of domain alignment. 2) The asymmetric structure consisting of a chief net and an independent ancillary net essentially overcomes the parameter sharing aroused source risk collapse. The adaption safety of the proposed ATF detector is guaranteed. Extensive experiments on a number of datasets, including Cityscapes, Foggy-cityscapes, KITTI, Sim10k, Pascal VOC, Clipart and Watercolor, demonstrate the SOTA performance of our method.

</details>

### Accurate RGB-D Salient Object Detection via Collaborative Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58523-5_4)
- **作者**: Wei Ji, Jingjing Li, Miao Zhang, Yongri Piao, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Learning Where to Focus for Efficient Video Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58517-4_2)
- **作者**: Zhengkai Jiang, Yu Liu, Ceyuan Yang, Jihao Liu, Peng Gao, Qian Zhang et al.
- **🏷️ 机构**: SenseTime
- **会议**: ECCV 2020

### Probabilistic Anchor Assignment with IoU Prediction for Object Detection.
- **链接**: [arXiv:2007.08103](https://arxiv.org/abs/2007.08103) · [代码](https://github.com/kkhoot/PAA) · 📚 被引 373
- **作者**: Kang Kim, Hee Seok Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In object detection, determining which anchors to assign as positive or negative samples, known as anchor assignment, has been revealed as a core procedure that can significantly affect a model's performance. In this paper we propose a novel anchor assignment strategy that adaptively separates anchors into positive and negative samples for a ground truth bounding box according to the model's learning status such that it is able to reason about the separation in a probabilistic manner. To do so we first calculate the scores of anchors conditioned on the model and fit a probability distribution to these scores. The model is then trained with anchors separated into positive and negative samples according to their probabilities. Moreover, we investigate the gap between the training and testing objectives and propose to predict the Intersection-over-Unions of detected boxes as a measure of localization quality to reduce the discrepancy. The combined score of classification and localization qualities serving as a box selection metric in non-maximum suppression well aligns with the proposed anchor assignment strategy and leads significant performance improvements. The proposed methods only add a single convolutional layer to RetinaNet baseline and does not require multiple anchors per location, so are efficient. Experimental results verify the effectiveness of the proposed methods. Especially, our models set new records for single-stage detectors on MS COCO test-dev dataset with various backbones. Code is available at https://github.com/kkhoot/PAA.

</details>

### RGB-D Salient Object Detection with Cross-Modality Modulation and Selection.
- **链接**: [arXiv:2007.07051](https://arxiv.org/abs/2007.07051)
- **作者**: Chongyi Li, Runmin Cong, Yongri Piao, Qianqian Xu, Chen Change Loy
- **🏷️ 机构**: NTU S-Lab
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present an effective method to progressively integrate and refine the cross-modality complementarities for RGB-D salient object detection (SOD). The proposed network mainly solves two challenging issues: 1) how to effectively integrate the complementary information from RGB image and its corresponding depth map, and 2) how to adaptively select more saliency-related features. First, we propose a cross-modality feature modulation (cmFM) module to enhance feature representations by taking the depth features as prior, which models the complementary relations of RGB-D data. Second, we propose an adaptive feature selection (AFS) module to select saliency-related features and suppress the inferior ones. The AFS module exploits multi-modality spatial feature fusion with the self-modality and cross-modality interdependencies of channel features are considered. Third, we employ a saliency-guided position-edge attention (sg-PEA) module to encourage our network to focus more on saliency-related regions. The above modules as a whole, called cmMS block, facilitates the refinement of saliency features in a coarse-to-fine fashion. Coupled with a bottom-up inference, the refined saliency features enable accurate and edge-preserving SOD. Extensive experiments demonstrate that our network outperforms state-of-the-art saliency detectors on six popular RGB-D SOD benchmarks.

</details>

### Quantum-Soft QUBO Suppression for Accurate Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58526-6_10) · 📚 被引 24
- **作者**: Junde Li, Swaroop Ghosh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Improving Object Detection with Selective Self-supervised Self-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58526-6_35)
- **作者**: Yandong Li, Di Huang, Danfeng Qin, Liqiang Wang, Boqing Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### MimicDet: Bridging the Gap Between One-Stage and Two-Stage Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58568-6_32) · 📚 被引 59
- **作者**: Xin Lu, Quanquan Li, Buyu Li, Junjie Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Cascade Graph Neural Networks for RGB-D Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58610-2_21)
- **作者**: Ao Luo, Xin Li, Fan Yang, Zhicheng Jiao, Hong Cheng, Siwei Lyu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### AABO: Adaptive Anchor Box Optimization for Object Detection via Bayesian Sub-sampling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58558-7_33) · 📚 被引 15
- **作者**: Wenshuo Ma, Tingzhong Tian, Hang Xu, Yimin Huang, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### OS2D: One-Stage One-Shot Object Detection by Matching Anchor Features.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58555-6_38) · 📚 被引 37
- **作者**: Anton Osokin, Denis Sumin, Vasily Lomakin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Hierarchical Dynamic Filtering Network for RGB-D Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58595-2_15) · 📚 被引 191
- **作者**: Youwei Pang, Lihe Zhang, Xiaoqi Zhao, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Chained-Tracker: Chaining Paired Attentive Regression Results for End-to-End Joint Multiple-Object Detection and Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58548-8_9) · 📚 被引 298
- **作者**: Jinlong Peng, Changan Wang, Fangbin Wan, Yang Wu, Yabiao Wang, Ying Tai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### BorderDet: Border Feature for Dense Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58452-8_32) · 📚 被引 120
- **作者**: Han Qiu, Yuchen Ma, Zeming Li, Songtao Liu, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2020

### TENet: Triple Excitation Network for Video Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58558-7_13)
- **作者**: Sucheng Ren, Chu Han, Xin Yang, Guoqiang Han, Shengfeng He
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### UFO2: A Unified Framework Towards Omni-supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58529-7_18) · 📚 被引 39
- **作者**: Zhongzheng Ren, Zhiding Yu, Xiaodong Yang, Ming-Yu Liu, Alexander G. Schwing, Jan Kautz
- **🏷️ 机构**: NVIDIA
- **会议**: ECCV 2020

### HoughNet: Integrating Near and Long-Range Evidence for Bottom-Up Object Detection.
- **链接**: [arXiv:2007.02355](https://arxiv.org/abs/2007.02355) · [代码](https://github.com/nerminsamet/houghnet)
- **作者**: Nermin Samet, Samet Hicsonmez, Emre Akbas
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents HoughNet, a one-stage, anchor-free, voting-based, bottom-up object detection method. Inspired by the Generalized Hough Transform, HoughNet determines the presence of an object at a certain location by the sum of the votes cast on that location. Votes are collected from both near and long-distance locations based on a log-polar vote field. Thanks to this voting mechanism, HoughNet is able to integrate both near and long-range, class-conditional evidence for visual recognition, thereby generalizing and enhancing current object detection methodology, which typically relies on only local evidence. On the COCO dataset, HoughNet's best model achieves 46.4 $AP$ (and 65.1 $AP_{50}$), performing on par with the state-of-the-art in bottom-up object detection and outperforming most major one-stage and two-stage methods. We further validate the effectiveness of our proposal in another task, namely, "labels to photo" image generation by integrating the voting module of HoughNet to two different GAN models and showing that the accuracy is significantly improved in both cases. Code is available at https://github.com/nerminsamet/houghnet.

</details>

### Enabling Deep Residual Networks for Weakly Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58598-3_8) · 📚 被引 39
- **作者**: Yunhang Shen, Rongrong Ji, Yan Wang, Zhiwei Chen, Feng Zheng, Feiyue Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Prior-Based Domain Adaptive Object Detection for Hazy and Rainy Conditions.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58568-6_45) · 📚 被引 161
- **作者**: Vishwanath A. Sindagi, Poojan Oza, Rajeev Yasarla, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Side-Aware Boundary Localization for More Precise Object Detection.
- **链接**: [arXiv:1912.04260](https://arxiv.org/abs/1912.04260) · [代码](https://github.com/open-mmlab/mmdetection) · 📚 被引 134
- **作者**: Jiaqi Wang, Wenwei Zhang, Yuhang Cao, Kai Chen, Jiangmiao Pang, Tao Gong et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current object detection frameworks mainly rely on bounding box regression to localize objects. Despite the remarkable progress in recent years, the precision of bounding box regression remains unsatisfactory, hence limiting performance in object detection. We observe that precise localization requires careful placement of each side of the bounding box. However, the mainstream approach, which focuses on predicting centers and sizes, is not the most effective way to accomplish this task, especially when there exists displacements with large variance between the anchors and the targets. In this paper, we propose an alternative approach, named as Side-Aware Boundary Localization (SABL), where each side of the bounding box is respectively localized with a dedicated network branch. To tackle the difficulty of precise localization in the presence of displacements with large variance, we further propose a two-step localization scheme, which first predicts a range of movement through bucket prediction and then pinpoints the precise position within the predicted bucket. We test the proposed method on both two-stage and single-stage detection frameworks. Replacing the standard bounding box regression branch with the proposed design leads to significant improvements on Faster R-CNN, RetinaNet, and Cascade R-CNN, by 3.0%, 1.7%, and 0.9%, respectively. Code is available at https://github.com/open-mmlab/mmdetection.

</details>

### Large Batch Optimization for Object Detection: Training COCO in 12 minutes.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58589-1_29) · 📚 被引 9
- **作者**: Tong Wang, Yousong Zhu, Chaoyang Zhao, Wei Zeng, Yaowei Wang, Jinqiao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Point-Set Anchors for Object Detection, Instance Segmentation and Pose Estimation.
- **链接**: [arXiv:2007.02846](https://arxiv.org/abs/2007.02846) · [代码](https://github.com/FangyunWei/PointSetAnchor) · 📚 被引 117
- **作者**: Fangyun Wei, Xiao Sun, Hongyang Li, Jingdong Wang, Stephen Lin
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A recent approach for object detection and human pose estimation is to regress bounding boxes or human keypoints from a central point on the object or person. While this center-point regression is simple and efficient, we argue that the image features extracted at a central point contain limited information for predicting distant keypoints or bounding box boundaries, due to object deformation and scale/orientation variation. To facilitate inference, we propose to instead perform regression from a set of points placed at more advantageous positions. This point set is arranged to reflect a good initialization for the given task, such as modes in the training data for pose estimation, which lie closer to the ground truth than the central point and provide more informative features for regression. As the utility of a point set depends on how well its scale, aspect ratio and rotation matches the target, we adopt the anchor box technique of sampling these transformations to generate additional point-set candidates. We apply this proposed framework, called Point-Set Anchors, to object detection, instance segmentation, and human pose estimation. Our results show that this general-purpose approach can achieve performance competitive with state-of-the-art methods for each of these tasks. Code is available at \url{https://github.com/FangyunWei/PointSetAnchor}

</details>

### Multi-scale Positive Sample Refinement for Few-Shot Object Detection.
- **链接**: [arXiv:2007.09384](https://arxiv.org/abs/2007.09384) · [代码](https://github.com/jiaxi-wu/MPSR) · 📚 被引 291
- **作者**: Jiaxi Wu, Songtao Liu, Di Huang, Yunhong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection (FSOD) helps detectors adapt to unseen classes with few training instances, and is useful when manual annotation is time-consuming or data acquisition is limited. Unlike previous attempts that exploit few-shot classification techniques to facilitate FSOD, this work highlights the necessity of handling the problem of scale variations, which is challenging due to the unique sample distribution. To this end, we propose a Multi-scale Positive Sample Refinement (MPSR) approach to enrich object scales in FSOD. It generates multi-scale positive samples as object pyramids and refines the prediction at various scales. We demonstrate its advantage by integrating it as an auxiliary branch to the popular architecture of Faster R-CNN with FPN, delivering a strong FSOD solution. Several experiments are conducted on PASCAL VOC and MS COCO, and the proposed approach achieves state of the art results and significantly outperforms other counterparts, which shows its effectiveness. Code is available at https://github.com/jiaxi-wu/MPSR.

</details>

### CenterNet Heatmap Propagation for Real-Time Video Object Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58595-2_14)
- **作者**: Zhujun Xu, Emir Hrustic, Damien Vivet
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

## 跨领域论文（完整笔记在其他领域）

- Object as Hotspots: An Anchor-Free 3D Object Detection Approach via Firing of Hotspots. → [3d-detection](../3d-detection/Guideline%202020.md)
- Monocular Differentiable Rendering for Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Kinematic 3D Object Detection in Monocular Video. → [3d-detection](../3d-detection/Guideline%202020.md)
- Improving 3D Object Detection Through Progressive Population Based Augmentation. → [3d-detection](../3d-detection/Guideline%202020.md)
- Finding Your (3D) Center: 3D Object Detection Using a Learned Loss. → [3d-detection](../3d-detection/Guideline%202020.md)
- EPNet: Enhancing Point Features with Image Semantics for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- An LSTM Approach to Temporal 3D Object Detection in LiDAR Point Clouds. → [3d-detection](../3d-detection/Guideline%202020.md)
- Cross-Modal Weighting Network for RGB-D Salient Object Detection. → [multimodal](../multimodal/Guideline%202020.md)
- Reinforced Axial Refinement Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Weakly Supervised 3D Object Detection from Lidar Point Cloud. → [3d-detection](../3d-detection/Guideline%202020.md)
- GeoGraph: Graph-Based Multi-view Object Detection with Geometric Cues End-to-End. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Distance-Normalized Unified Representation for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Towards Generalization Across Depth for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Pillar-Based Object Detection for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202020.md)
- InfoFocus: 3D Object Detection for Autonomous Driving with Dynamic Information Modeling. → [3d-detection](../3d-detection/Guideline%202020.md)
- Monocular 3D Object Detection via Feature Domain Adaptation. → [3d-detection](../3d-detection/Guideline%202020.md)
