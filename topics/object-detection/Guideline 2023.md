# Object Detection — 2023 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 95 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Distilling DETR with Visual-Linguistic Knowledge for Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00598)
- **作者**: Liangqi Li, Jiaxu Miao, Dahu Shi, Wenming Tan, Ye Ren, Yi Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### OmniLabel: A Challenging Benchmark for Language-Based Object Detection.
- **链接**: [arXiv:2304.11463](https://arxiv.org/abs/2304.11463) · 📚 被引 12
- **作者**: Samuel Schulter, Vijay Kumar B. G, Yumin Suh, Konstantinos M. Dafnis, Zhixing Zhang, Shiyu Zhao et al.
- **🏷️ 机构**: NEC Laboratories America, Rutgers University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Language-based object detection is a promising direction towards building a natural interface to describe objects in images that goes far beyond plain category names. While recent methods show great progress in that direction, proper evaluation is lacking. With OmniLabel, we propose a novel task definition, dataset, and evaluation metric. The task subsumes standard- and open-vocabulary detection as well as referring expressions. With more than 28K unique object descriptions on over 25K images, OmniLabel provides a challenging benchmark with diverse and complex object descriptions in a naturally open-vocabulary setting. Moreover, a key differentiation to existing benchmarks is that our object descriptions can refer to one, multiple or even no object, hence, providing negative examples in free-form text. The proposed evaluation handles the large label space and judges performance via a modified average precision metric, which we validate by evaluating strong language-based baselines. OmniLabel indeed provides a challenging test bed for future research on language-based detection.

</details>

### Cascade-DETR: Delving into High-Quality Universal Object Detection.
- **链接**: [arXiv:2307.11035](https://arxiv.org/abs/2307.11035) · [代码](https://github.com/SysCV/cascade-detr) · 📚 被引 54
- **作者**: Mingqiao Ye, Lei Ke, Siyuan Li, Yu-Wing Tai, Chi-Keung Tang, Martin Danelljan et al.
- **🏷️ 机构**: ETH Z&#x00FC;rich, Dartmouth College, HKUST
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object localization in general environments is a fundamental part of vision systems. While dominating on the COCO benchmark, recent Transformer-based detection methods are not competitive in diverse domains. Moreover, these methods still struggle to very accurately estimate the object bounding boxes in complex environments. We introduce Cascade-DETR for high-quality universal object detection. We jointly tackle the generalization to diverse domains and localization accuracy by proposing the Cascade Attention layer, which explicitly integrates object-centric information into the detection decoder by limiting the attention to the previous box prediction. To further enhance accuracy, we also revisit the scoring of queries. Instead of relying on classification scores, we predict the expected IoU of the query, leading to substantially more well-calibrated confidences. Lastly, we introduce a universal object detection benchmark, UDB10, that contains 10 datasets from diverse domains. While also advancing the state-of-the-art on COCO, Cascade-DETR substantially improves DETR-based detectors on all datasets in UDB10, even by over 10 mAP in some cases. The improvements under stringent quality requirements are even more pronounced. Our code and models will be released at https://github.com/SysCV/cascade-detr.

</details>

### Decoupled DETR: Spatially Disentangling Localization and Classification for Improved End-to-End Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00607) · 📚 被引 28
- **作者**: Manyuan Zhang, Guanglu Song, Yu Liu, Hongsheng Li
- **🏷️ 机构**: The Chinese University of HongKong,Multimedia Laboratory, SenseTime Research
- **会议**: ICCV 2023

### T-FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00435)
- **作者**: James Giroux, Martin Bouchard, Robert Laganière
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### DETRDistill: A Universal Knowledge Distillation Framework for DETR-families.
- **链接**: [arXiv:2211.10156](https://arxiv.org/abs/2211.10156) · 📚 被引 39
- **作者**: Jiahao Chang, Shuo Wang, Hai-Ming Xu, Zehui Chen, Chenhongyi Yang, Feng Zhao
- **🏷️ 机构**: University of Science and Technology of China, University of Adelaide, University of Edinburgh
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based detectors (DETRs) are becoming popular for their simple framework, but the large model size and heavy time consumption hinder their deployment in the real world. While knowledge distillation (KD) can be an appealing technique to compress giant detectors into small ones for comparable detection performance and low inference cost. Since DETRs formulate object detection as a set prediction problem, existing KD methods designed for classic convolution-based detectors may not be directly applicable. In this paper, we propose DETRDistill, a novel knowledge distillation method dedicated to DETR-families. Specifically, we first design a Hungarian-matching logits distillation to encourage the student model to have the exact predictions as that of teacher DETRs. Next, we propose a target-aware feature distillation to help the student model learn from the object-centric features of the teacher model. Finally, in order to improve the convergence rate of the student DETR, we introduce a query-prior assignment distillation to speed up the student model learning from well-trained queries and stable assignment of the teacher model. Extensive experimental results on the COCO dataset validate the effectiveness of our approach. Notably, DETRDistill consistently improves various DETRs by more than 2.0 mAP, even surpassing their teacher models.

</details>

### Objects do not disappear: Video object detection by single-frame object location anticipation.
- **链接**: [arXiv:2308.04770](https://arxiv.org/abs/2308.04770) · [代码](https://github.com/L-KID/Videoobject-detection-by-location-anticipation) · 📚 被引 11
- **作者**: Xin Liu, Fatemeh Karimi Nejadasl, Jan C. van Gemert, Olaf Booij, Silvia L. Pintea
- **🏷️ 机构**: Delft University of Technology,Computer Vision Lab, University of Amsterdam,Institute for Biodiversity and Ecosystem Dynamics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Objects in videos are typically characterized by continuous smooth motion. We exploit continuous smooth motion in three ways. 1) Improved accuracy by using object motion as an additional source of supervision, which we obtain by anticipating object locations from a static keyframe. 2) Improved efficiency by only doing the expensive feature computations on a small subset of all frames. Because neighboring video frames are often redundant, we only compute features for a single static keyframe and predict object locations in subsequent frames. 3) Reduced annotation cost, where we only annotate the keyframe and use smooth pseudo-motion between keyframes. We demonstrate computational efficiency, annotation efficiency, and improved mean average precision compared to the state-of-the-art on four datasets: ImageNet VID, EPIC KITCHENS-55, YouTube-BoundingBoxes, and Waymo Open dataset. Our source code is available at https://github.com/L-KID/Videoobject-detection-by-location-anticipation.

</details>

### Self-Supervised Object Detection from Egocentric Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00482)
- **作者**: Peri Akiva, Jing Huang, Kevin J. Liang, Rama Kovvuri, Xingyu Chen, Matt Feiszli et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### DiffusionDet: Diffusion Model for Object Detection.
- **链接**: [arXiv:2211.09788](https://arxiv.org/abs/2211.09788) · [代码](https://github.com/ShoufaChen/DiffusionDet) · 📚 被引 560
- **作者**: Shoufa Chen, Peize Sun, Yibing Song, Ping Luo
- **🏷️ 机构**: The University of Hong Kong, Tencent AI Lab
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose DiffusionDet, a new framework that formulates object detection as a denoising diffusion process from noisy boxes to object boxes. During the training stage, object boxes diffuse from ground-truth boxes to random distribution, and the model learns to reverse this noising process. In inference, the model refines a set of randomly generated boxes to the output results in a progressive way. Our work possesses an appealing property of flexibility, which enables the dynamic number of boxes and iterative evaluation. The extensive experiments on the standard benchmarks show that DiffusionDet achieves favorable performance compared to previous well-established detectors. For example, DiffusionDet achieves 5.3 AP and 4.8 AP gains when evaluated with more boxes and iteration steps, under a zero-shot transfer setting from COCO to CrowdHuman. Our code is available at https://github.com/ShoufaChen/DiffusionDet.

</details>

### Identity-Consistent Aggregation for Video Object Detection.
- **链接**: [arXiv:2308.07737](https://arxiv.org/abs/2308.07737) · 📚 被引 10
- **作者**: Chaorui Deng, Da Chen, Qi Wu
- **🏷️ 机构**: University of Adelaide,Australia Institute of Machine Learning, University of Bath,Department of Computer Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Video Object Detection (VID), a common practice is to leverage the rich temporal contexts from the video to enhance the object representations in each frame. Existing methods treat the temporal contexts obtained from different objects indiscriminately and ignore their different identities. While intuitively, aggregating local views of the same object in different frames may facilitate a better understanding of the object. Thus, in this paper, we aim to enable the model to focus on the identity-consistent temporal contexts of each object to obtain more comprehensive object representations and handle the rapid object appearance variations such as occlusion, motion blur, etc. However, realizing this goal on top of existing VID models faces low-efficiency problems due to their redundant region proposals and nonparallel frame-wise prediction manner. To aid this, we propose ClipVID, a VID model equipped with Identity-Consistent Aggregation (ICA) layers specifically designed for mining fine-grained and identity-consistent temporal contexts. It effectively reduces the redundancies through the set prediction strategy, making the ICA layers very efficient and further allowing us to design an architecture that makes parallel clip-wise predictions for the whole video clip. Extensive experimental results demonstrate the superiority of our method: a state-of-the-art (SOTA) performance (84.7% mAP) on the ImageNet VID dataset while running at a speed about 7x faster (39.3 fps) than previous SOTAs.

</details>

### Boosting Long-tailed Object Detection via Step-wise Learning on Smooth-tail Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00639) · 📚 被引 5
- **作者**: Na Dong, Yongqiang Zhang, Mingli Ding, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore,Department of Computer Science, Harbin Institute of Technology,School of Instrument Science and Engineering
- **会议**: ICCV 2023

### σ-Adaptive Decoupled Prototype for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01737) · 📚 被引 19
- **作者**: Jinhao Du, Shan Zhang, Qiang Chen, Haifeng Le, Yanpeng Sun, Yao Ni et al.
- **🏷️ 机构**: Baidu VIS, Australian National University, Beijing Union University
- **会议**: ICCV 2023

### Unleashing Vanilla Vision Transformer with Masked Image Modeling for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00574)
- **作者**: Yuxin Fang, Shusheng Yang, Shijie Wang, Yixiao Ge, Ying Shan, Xinggang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### CSDA: Learning Category-Scale Joint Feature for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01049) · 📚 被引 25
- **作者**: Changlong Gao, Chengxu Liu, Yujie Dun, Xueming Qian
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University
- **会议**: ICCV 2023

### FeatEnHancer: Enhancing Hierarchical Features for Object Detection and Beyond Under Low-Light Vision.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00619) · 📚 被引 93
- **作者**: Khurram Azeem Hashmi, Goutham Kallempudi, Didier Stricker, Muhammad Zeshan Afzal
- **🏷️ 机构**: German Research Center for Artificial Intelligence,DFKI, RPTU Kaiserslautern
- **会议**: ICCV 2023

### Unsupervised Prompt Tuning for Text-Driven Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00250) · 📚 被引 7
- **作者**: Weizhen He, Weijie Chen, Binbin Chen, Shicai Yang, Di Xie, Luojun Lin et al.
- **🏷️ 机构**: Zhejiang University, Hikvision Research Institute, Fuzhou University
- **会议**: ICCV 2023

### Novel Scenes & Classes: Towards Adaptive Open-set Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01446)
- **作者**: Wuyang Li, Xiaoqing Guo, Yixuan Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Large Selective Kernel Network for Remote Sensing Object Detection.
- **链接**: [arXiv:2303.09030](https://arxiv.org/abs/2303.09030) · [代码](https://github.com/zcablii/Large-Selective-Kernel-Network) · 📚 被引 807
- **作者**: Yuxuan Li, Qibin Hou, Zhaohui Zheng, Ming-Ming Cheng, Jian Yang, Xiang Li
- **🏷️ 机构**: Nankai University,VCIP, CS
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent research on remote sensing object detection has largely focused on improving the representation of oriented bounding boxes but has overlooked the unique prior knowledge presented in remote sensing scenarios. Such prior knowledge can be useful because tiny remote sensing objects may be mistakenly detected without referencing a sufficiently long-range context, and the long-range context required by different types of objects can vary. In this paper, we take these priors into account and propose the Large Selective Kernel Network (LSKNet). LSKNet can dynamically adjust its large spatial receptive field to better model the ranging context of various objects in remote sensing scenarios. To the best of our knowledge, this is the first time that large and selective kernel mechanisms have been explored in the field of remote sensing object detection. Without bells and whistles, LSKNet sets new state-of-the-art scores on standard benchmarks, i.e., HRSC2016 (98.46\% mAP), DOTA-v1.0 (81.85\% mAP) and FAIR1M-v1.0 (47.87\% mAP). Based on a similar technique, we rank 2nd place in 2022 the Greater Bay Area International Algorithm Competition. Code is available at https://github.com/zcablii/Large-Selective-Kernel-Network.

</details>

### Gradient-based Sampling for Class Imbalanced Semi-supervised Object Detection.
- **链接**: [arXiv:2403.15127](https://arxiv.org/abs/2403.15127) · [代码](https://github.com/nightkeepers/CI-SSOD) · 📚 被引 11
- **作者**: Jiaming Li, Xiangru Lin, Wei Zhang, Xiao Tan, Yingying Li, Junyu Han et al.
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,Guangzhou,China, Baidu Inc.,Department of Computer Vision Technology (VIS),China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current semi-supervised object detection (SSOD) algorithms typically assume class balanced datasets (PASCAL VOC etc.) or slightly class imbalanced datasets (MS-COCO, etc). This assumption can be easily violated since real world datasets can be extremely class imbalanced in nature, thus making the performance of semi-supervised object detectors far from satisfactory. Besides, the research for this problem in SSOD is severely under-explored. To bridge this research gap, we comprehensively study the class imbalance problem for SSOD under more challenging scenarios, thus forming the first experimental setting for class imbalanced SSOD (CI-SSOD). Moreover, we propose a simple yet effective gradient-based sampling framework that tackles the class imbalance problem from the perspective of two types of confirmation biases. To tackle confirmation bias towards majority classes, the gradient-based reweighting and gradient-based thresholding modules leverage the gradients from each class to fully balance the influence of the majority and minority classes. To tackle the confirmation bias from incorrect pseudo labels of minority classes, the class-rebalancing sampling module resamples unlabeled data following the guidance of the gradient-based reweighting module. Experiments on three proposed sub-tasks, namely MS-COCO, MS-COCO to Object365 and LVIS, suggest that our method outperforms current class imbalanced object detectors by clear margins, serving as a baseline for future research in CI-SSOD. Code will be available at https://github.com/nightkeepers/CI-SSOD.

</details>

### AlignDet: Aligning Pre-training and Fine-tuning in Object Detection.
- **链接**: [arXiv:2307.11077](https://arxiv.org/abs/2307.11077) · 📚 被引 26
- **作者**: Ming Li, Jie Wu, Xionghui Wang, Chen Chen, Jie Qin, Xuefeng Xiao et al.
- **🏷️ 机构**: ByteDance Inc, University of Central Florida,Center for Research in Computer Vision
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The paradigm of large-scale pre-training followed by downstream fine-tuning has been widely employed in various object detection algorithms. In this paper, we reveal discrepancies in data, model, and task between the pre-training and fine-tuning procedure in existing practices, which implicitly limit the detector's performance, generalization ability, and convergence speed. To this end, we propose AlignDet, a unified pre-training framework that can be adapted to various existing detectors to alleviate the discrepancies. AlignDet decouples the pre-training process into two stages, i.e., image-domain and box-domain pre-training. The image-domain pre-training optimizes the detection backbone to capture holistic visual abstraction, and box-domain pre-training learns instance-level semantics and task-aware concepts to initialize the parts out of the backbone. By incorporating the self-supervised pre-trained backbones, we can pre-train all modules for various detectors in an unsupervised paradigm. As depicted in Figure 1, extensive experiments demonstrate that AlignDet can achieve significant improvements across diverse protocols, such as detection algorithm, model backbone, data setting, and training schedule. For example, AlignDet improves FCOS by 5.3 mAP, RetinaNet by 2.1 mAP, Faster R-CNN by 3.3 mAP, and DETR by 2.3 mAP under fewer epochs.

</details>

### Augmented Box Replay: Overcoming Foreground Shift for Incremental Object Detection.
- **链接**: [arXiv:2307.12427](https://arxiv.org/abs/2307.12427) · 📚 被引 39
- **作者**: Yuyang Liu, Yang Cong, Dipam Goswami, Xialei Liu, Joost van de Weijer
- **🏷️ 机构**: Chinese Academy of Sciences,State Key Laboratory of Robotics, Shenyang Institute of Automation, South China University of Technology, Computer Vision Center, Barcelona
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In incremental learning, replaying stored samples from previous tasks together with current task samples is one of the most efficient approaches to address catastrophic forgetting. However, unlike incremental classification, image replay has not been successfully applied to incremental object detection (IOD). In this paper, we identify the overlooked problem of foreground shift as the main reason for this. Foreground shift only occurs when replaying images of previous tasks and refers to the fact that their background might contain foreground objects of the current task. To overcome this problem, a novel and efficient Augmented Box Replay (ABR) method is developed that only stores and replays foreground objects and thereby circumvents the foreground shift problem. In addition, we propose an innovative Attentive RoI Distillation loss that uses spatial attention from region-of-interest (RoI) features to constrain current model to focus on the most important information from old model. ABR significantly reduces forgetting of previous classes while maintaining high plasticity in current classes. Moreover, it considerably reduces the storage requirements when compared to standard image replay. Comprehensive experiments on Pascal-VOC and COCO datasets support the state-of-the-art performance of our model.

</details>

### Integrally Migrating Pre-trained Transformer Encoder-decoders for Visual Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00628) · 📚 被引 26
- **作者**: Feng Liu, Xiaosong Zhang, Zhiliang Peng, Zonghao Guo, Fang Wan, Xiangyang Ji et al.
- **🏷️ 机构**: University of Chinese Academy of Sciences, Tsinghua University
- **会议**: ICCV 2023

### Anchor-Intermediate Detector: Decoupling and Coupling Bounding Boxes for Accurate Object Detection.
- **链接**: [arXiv:2310.05666](https://arxiv.org/abs/2310.05666) · [代码](https://github.com/YilongLv/AID) · 📚 被引 7
- **作者**: Yilong Lv, Min Li, Yujie He, Zhuzhen He, Shaopeng Li, Aitao Yang
- **🏷️ 机构**: Xi&#x2019;an Institute of High Technology, National University of Defense Technology, Tsinghua University,Department of Automation
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anchor-based detectors have been continuously developed for object detection. However, the individual anchor box makes it difficult to predict the boundary's offset accurately. Instead of taking each bounding box as a closed individual, we consider using multiple boxes together to get prediction boxes. To this end, this paper proposes the \textbf{Box Decouple-Couple(BDC) strategy} in the inference, which no longer discards the overlapping boxes, but decouples the corner points of these boxes. Then, according to each corner's score, we couple the corner points to select the most accurate corner pairs. To meet the BDC strategy, a simple but novel model is designed named the \textbf{Anchor-Intermediate Detector(AID)}, which contains two head networks, i.e., an anchor-based head and an anchor-free \textbf{Corner-aware head}. The corner-aware head is able to score the corners of each bounding box to facilitate the coupling between corner points. Extensive experiments on MS COCO show that the proposed anchor-intermediate detector respectively outperforms their baseline RetinaNet and GFL method by $\sim$2.4 and $\sim$1.2 AP on the MS COCO test-dev dataset without any bells and whistles. Code is available at: https://github.com/YilongLv/AID.

</details>

### Adaptive Rotated Convolution for Rotated Object Detection.
- **链接**: [arXiv:2303.07820](https://arxiv.org/abs/2303.07820) · [代码](https://github.com/LeapLabTHU/ARC) · 📚 被引 191
- **作者**: Yifan Pu, Yiru Wang, Zhuofan Xia, Yizeng Han, Yulin Wang, Weihao Gan et al.
- **🏷️ 机构**: Tsinghua University,BNRist,Department of Automation, SenseTime Research, Mashang Consumer Finance Co., Ltd.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rotated object detection aims to identify and locate objects in images with arbitrary orientation. In this scenario, the oriented directions of objects vary considerably across different images, while multiple orientations of objects exist within an image. This intrinsic characteristic makes it challenging for standard backbone networks to extract high-quality features of these arbitrarily orientated objects. In this paper, we present Adaptive Rotated Convolution (ARC) module to handle the aforementioned challenges. In our ARC module, the convolution kernels rotate adaptively to extract object features with varying orientations in different images, and an efficient conditional computation mechanism is introduced to accommodate the large orientation variations of objects within an image. The two designs work seamlessly in rotated object detection problem. Moreover, ARC can conveniently serve as a plug-and-play module in various vision backbones to boost their representation ability to detect oriented objects accurately. Experiments on commonly used benchmarks (DOTA and HRSC2016) demonstrate that equipped with our proposed ARC module in the backbone network, the performance of multiple popular oriented object detectors is significantly improved (\eg +3.03\% mAP on Rotated RetinaNet and +4.16\% on CFA). Combined with the highly competitive method Oriented R-CNN, the proposed approach achieves state-of-the-art performance on the DOTA dataset with 81.77\% mAP. Code is available at \url{https://github.com/LeapLabTHU/ARC}.

</details>

### EdaDet: Open-Vocabulary Object Detection Using Early Dense Alignment.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01441)
- **作者**: Cheng Shi, Sibei Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Deep Directly-Trained Spiking Neural Networks for Object Detection.
- **链接**: [arXiv:2307.11411](https://arxiv.org/abs/2307.11411) · 📚 被引 129
- **作者**: Qiaoyi Su, Yuhong Chou, Yifan Hu, Jianing Li, Shijie Mei, Ziyang Zhang et al.
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Artificial Intelligence, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence, Tsinghua University,Department of Precision Instrument
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spiking neural networks (SNNs) are brain-inspired energy-efficient models that encode information in spatiotemporal dynamics. Recently, deep SNNs trained directly have shown great success in achieving high performance on classification tasks with very few time steps. However, how to design a directly-trained SNN for the regression task of object detection still remains a challenging problem. To address this problem, we propose EMS-YOLO, a novel directly-trained SNN framework for object detection, which is the first trial to train a deep SNN with surrogate gradients for object detection rather than ANN-SNN conversion strategies. Specifically, we design a full-spike residual block, EMS-ResNet, which can effectively extend the depth of the directly-trained SNN with low power consumption. Furthermore, we theoretically analyze and prove the EMS-ResNet could avoid gradient vanishing or exploding. The results demonstrate that our approach outperforms the state-of-the-art ANN-SNN conversion methods (at least 500 time steps) in extremely fewer time steps (only 4 time steps). It is shown that our model could achieve comparable performance to the ANN with the same architecture while consuming 5.83 times less energy on the frame-based COCO Dataset and the event-based Gen1 Dataset.

</details>

### SparseDet: Improving Sparsely Annotated Object Detection with Pseudo-positive Mining.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00623) · 📚 被引 15
- **作者**: Saksham Suri, Sai Saketh Rambhatla, Rama Chellappa, Abhinav Shrivastava
- **🏷️ 机构**: University of Maryland,College Park, Johns Hopkins University
- **会议**: ICCV 2023

### CoTDet: Affordance Knowledge Prompting for Task Driven Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00285) · 📚 被引 27
- **作者**: Jiajin Tang, Ge Zheng, Jingyi Yu, Sibei Yang
- **🏷️ 机构**: ShanghaiTech University,School of Information Science and Technology
- **会议**: ICCV 2023

### FemtoDet: An Object Detection Baseline for Energy Versus Performance Tradeoffs.
- **链接**: [arXiv:2301.06719](https://arxiv.org/abs/2301.06719) · 📚 被引 14
- **作者**: Peng Tu, Xu Xie, Guo Ai, Yuexiang Li, Yawen Huang, Yefeng Zheng
- **🏷️ 机构**: MicroBT Inc., Jarvis Lab Tencent
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient detectors for edge devices are often optimized for parameters or speed count metrics, which remain in weak correlation with the energy of detectors. However, some vision applications of convolutional neural networks, such as always-on surveillance cameras, are critical for energy constraints. This paper aims to serve as a baseline by designing detectors to reach tradeoffs between energy and performance from two perspectives: 1) We extensively analyze various CNNs to identify low-energy architectures, including selecting activation functions, convolutions operators, and feature fusion structures on necks. These underappreciated details in past work seriously affect the energy consumption of detectors; 2) To break through the dilemmatic energy-performance problem, we propose a balanced detector driven by energy using discovered low-energy components named \textit{FemtoDet}. In addition to the novel construction, we improve FemtoDet by considering convolutions and training strategy optimizations. Specifically, we develop a new instance boundary enhancement (IBE) module for convolution optimization to overcome the contradiction between the limited capacity of CNNs and detection tasks in diverse spatial representations, and propose a recursive warm-restart (RecWR) for optimizing training strategy to escape the sub-optimization of light-weight detectors by considering the data shift produced in popular augmentations. As a result, FemtoDet with only 68.77k parameters achieves a competitive score of 46.3 AP50 on PASCAL VOC and 1.11 W $\&$ 64.47 FPS on Qualcomm Snapdragon 865 CPU platforms. Extensive experiments on COCO and TJU-DHD datasets indicate that the proposed method achieves competitive results in diverse scenes.

</details>

### ALWOD: Active Learning for Weakly-Supervised Object Detection.
- **链接**: [arXiv:2309.07914](https://arxiv.org/abs/2309.07914) · [代码](https://github.com/seqam-lab/ALWOD) · 📚 被引 28
- **作者**: Yuting Wang, Velibor Ilic, Jiatong Li, Branislav Kisacanin, Vladimir Pavlovic
- **🏷️ 机构**: Rutgers University,NJ,USA, The Institute for Artificial Intelligence Research and Development of Serbia,Novi Sad,Serbia, Nvidia Corporation,TX,USA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection (OD), a crucial vision task, remains challenged by the lack of large training datasets with precise object localization labels. In this work, we propose ALWOD, a new framework that addresses this problem by fusing active learning (AL) with weakly and semi-supervised object detection paradigms. Because the performance of AL critically depends on the model initialization, we propose a new auxiliary image generator strategy that utilizes an extremely small labeled set, coupled with a large weakly tagged set of images, as a warm-start for AL. We then propose a new AL acquisition function, another critical factor in AL success, that leverages the student-teacher OD pair disagreement and uncertainty to effectively propose the most informative images to annotate. Finally, to complete the AL loop, we introduce a new labeling task delegated to human annotators, based on selection and correction of model-proposed detections, which is both rapid and effective in labeling the informative images. We demonstrate, across several challenging benchmarks, that ALWOD significantly narrows the gap between the ODs trained on few partially labeled but strategically selected image instances and those that rely on the fully-labeled data. Our code is publicly available on https://github.com/seqam-lab/ALWOD.

</details>

### Deep Equilibrium Object Detection.
- **链接**: [arXiv:2308.09564](https://arxiv.org/abs/2308.09564) · 📚 被引 7
- **作者**: Shuai Wang, Yao Teng, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Query-based object detectors directly decode image features into object instances with a set of learnable queries. These query vectors are progressively refined to stable meaningful representations through a sequence of decoder layers, and then used to directly predict object locations and categories with simple FFN heads. In this paper, we present a new query-based object detector (DEQDet) by designing a deep equilibrium decoder. Our DEQ decoder models the query vector refinement as the fixed point solving of an {implicit} layer and is equivalent to applying {infinite} steps of refinement. To be more specific to object decoding, we use a two-step unrolled equilibrium equation to explicitly capture the query vector refinement. Accordingly, we are able to incorporate refinement awareness into the DEQ training with the inexact gradient back-propagation (RAG). In addition, to stabilize the training of our DEQDet and improve its generalization ability, we devise the deep supervision scheme on the optimization path of DEQ with refinement-aware perturbation~(RAP). Our experiments demonstrate DEQDet converges faster, consumes less memory, and achieves better results than the baseline counterpart (AdaMixer). In particular, our DEQDet with ResNet50 backbone and 300 queries achieves the $49.5$ mAP and $33.0$ AP$_s$ on the MS COCO benchmark under $2\times$ training scheme (24 epochs).

</details>

### Open-Vocabulary Object Detection With an Open Corpus.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00622)
- **作者**: Jiong Wang, Huiming Zhang, Haiwen Hong, Xuan Jin, Yuan He, Hui Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### SAFE: Sensitivity-Aware Features for Out-of-Distribution Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02154) · 📚 被引 36
- **作者**: Samuel Wilson, Tobias Fischer, Feras Dayoub, Dimity Miller, Niko Sünderhauf
- **🏷️ 机构**: Queensland University of Technology,QUT Centre for Robotics, University of Adelaide,Australian Institute for Machine Learning
- **会议**: ICCV 2023

### Spatial Self-Distillation for Object Detection with Inaccurate Bounding Boxes.
- **链接**: [arXiv:2307.12101](https://arxiv.org/abs/2307.12101) · [代码](https://github.com/ucas-vg/PointTinyBenchmark) · 📚 被引 20
- **作者**: Di Wu, Pengfei Chen, Xuehui Yu, Guorong Li, Zhenjun Han, Jianbin Jiao
- **🏷️ 机构**: University of Chinese Academy of Sciences
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection via inaccurate bounding boxes supervision has boosted a broad interest due to the expensive high-quality annotation data or the occasional inevitability of low annotation quality (\eg tiny objects). The previous works usually utilize multiple instance learning (MIL), which highly depends on category information, to select and refine a low-quality box. Those methods suffer from object drift, group prediction and part domination problems without exploring spatial information. In this paper, we heuristically propose a \textbf{Spatial Self-Distillation based Object Detector (SSD-Det)} to mine spatial information to refine the inaccurate box in a self-distillation fashion. SSD-Det utilizes a Spatial Position Self-Distillation \textbf{(SPSD)} module to exploit spatial information and an interactive structure to combine spatial information and category information, thus constructing a high-quality proposal bag. To further improve the selection procedure, a Spatial Identity Self-Distillation \textbf{(SISD)} module is introduced in SSD-Det to obtain spatial confidence to help select the best proposals. Experiments on MS-COCO and VOC datasets with noisy box annotation verify our method's effectiveness and achieve state-of-the-art performance. The code is available at https://github.com/ucas-vg/PointTinyBenchmark/tree/SSD-Det.

</details>

### Bridging Cross-task Protocol Inconsistency for Distillation in Dense Object Detection.
- **链接**: [arXiv:2308.14286](https://arxiv.org/abs/2308.14286) · [代码](https://github.com/TinyTigerPan/BCKD) · 📚 被引 67
- **作者**: Longrong Yang, Xianpan Zhou, Xuewei Li, Liang Qiao, Zheyang Li, Ziwei Yang et al.
- **🏷️ 机构**: Zhejiang University,College of Computer Science &#x0026; Technology, Zhejiang University,Polytechnic Institute, Hikvision Research Institute
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge distillation (KD) has shown potential for learning compact models in dense object detection. However, the commonly used softmax-based distillation ignores the absolute classification scores for individual categories. Thus, the optimum of the distillation loss does not necessarily lead to the optimal student classification scores for dense object detectors. This cross-task protocol inconsistency is critical, especially for dense object detectors, since the foreground categories are extremely imbalanced. To address the issue of protocol differences between distillation and classification, we propose a novel distillation method with cross-task consistent protocols, tailored for the dense object detection. For classification distillation, we address the cross-task protocol inconsistency problem by formulating the classification logit maps in both teacher and student models as multiple binary-classification maps and applying a binary-classification distillation loss to each map. For localization distillation, we design an IoU-based Localization Distillation Loss that is free from specific network structures and can be compared with existing localization distillation losses. Our proposed method is simple but effective, and experimental results demonstrate its superiority over existing methods. Code is available at https://github.com/TinyTigerPan/BCKD.

</details>

### Cyclic-Bootstrap Labeling for Weakly Supervised Object Detection.
- **链接**: [arXiv:2308.05991](https://arxiv.org/abs/2308.05991) · [代码](https://github.com/Yinyf0804/WSOD-CBL) · 📚 被引 17
- **作者**: Yufei Yin, Jiajun Deng, Wengang Zhou, Li Li, Houqiang Li
- **🏷️ 机构**: University of Science and Technology of China,CAS Key Laboratory of Technology in GIPAS,EEIS Department, The University of Sydney
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in weakly supervised object detection is featured by a combination of multiple instance detection networks (MIDN) and ordinal online refinement. However, with only image-level annotation, MIDN inevitably assigns high scores to some unexpected region proposals when generating pseudo labels. These inaccurate high-scoring region proposals will mislead the training of subsequent refinement modules and thus hamper the detection performance. In this work, we explore how to ameliorate the quality of pseudo-labeling in MIDN. Formally, we devise Cyclic-Bootstrap Labeling (CBL), a novel weakly supervised object detection pipeline, which optimizes MIDN with rank information from a reliable teacher network. Specifically, we obtain this teacher network by introducing a weighted exponential moving average strategy to take advantage of various refinement modules. A novel class-specific ranking distillation algorithm is proposed to leverage the output of weighted ensembled teacher network for distilling MIDN with rank information. As a result, MIDN is guided to assign higher scores to accurate proposals among their neighboring ones, thus benefiting the subsequent pseudo labeling. Extensive experiments on the prevalent PASCAL VOC 2007 \& 2012 and COCO datasets demonstrate the superior performance of our CBL framework. Code will be available at https://github.com/Yinyf0804/WSOD-CBL/.

</details>

### Small Object Detection via Coarse-to-fine Proposal Generation and Imitation Learning.
- **链接**: [arXiv:2308.09534](https://arxiv.org/abs/2308.09534) · 📚 被引 135
- **作者**: Xiang Yuan, Gong Cheng, Kebing Yan, Qinghua Zeng, Junwei Han
- **🏷️ 机构**: Northwestern Polytechnical University,School of Automation,Xi&#x2019;an,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The past few years have witnessed the immense success of object detection, while current excellent detectors struggle on tackling size-limited instances. Concretely, the well-known challenge of low overlaps between the priors and object regions leads to a constrained sample pool for optimization, and the paucity of discriminative information further aggravates the recognition. To alleviate the aforementioned issues, we propose CFINet, a two-stage framework tailored for small object detection based on the Coarse-to-fine pipeline and Feature Imitation learning. Firstly, we introduce Coarse-to-fine RPN (CRPN) to ensure sufficient and high-quality proposals for small objects through the dynamic anchor selection strategy and cascade regression. Then, we equip the conventional detection head with a Feature Imitation (FI) branch to facilitate the region representations of size-limited instances that perplex the model in an imitation manner. Moreover, an auxiliary imitation loss following supervised contrastive learning paradigm is devised to optimize this branch. When integrated with Faster RCNN, CFINet achieves state-of-the-art performance on the large-scale small object detection benchmarks, SODA-D and SODA-A, underscoring its superiority over baseline detector and other mainstream detection approaches.

</details>

### A Dynamic Dual-Processing Object Detection Framework Inspired by the Brain's Recognition Mechanism.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00576) · 📚 被引 3
- **作者**: Minying Zhang, Tianpeng Bu, Lulu Hu
- **🏷️ 机构**: Alibaba Group,Hangzhou,China
- **会议**: ICCV 2023

### RecursiveDet: End-to-End Region-based Recursive Object Detection.
- **链接**: [arXiv:2307.13619](https://arxiv.org/abs/2307.13619) · [代码](https://github.com/bravezzzzzz/RecursiveDet) · 📚 被引 7
- **作者**: Jing Zhao, Li Sun, Qingli Li
- **🏷️ 机构**: East China Normal University,Shanghai Key Laboratory of Multidimensional Information Processing,Shanghai,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end region-based object detectors like Sparse R-CNN usually have multiple cascade bounding box decoding stages, which refine the current predictions according to their previous results. Model parameters within each stage are independent, evolving a huge cost. In this paper, we find the general setting of decoding stages is actually redundant. By simply sharing parameters and making a recursive decoder, the detector already obtains a significant improvement. The recursive decoder can be further enhanced by positional encoding (PE) of the proposal box, which makes it aware of the exact locations and sizes of input bounding boxes, thus becoming adaptive to proposals from different stages during the recursion. Moreover, we also design centerness-based PE to distinguish the RoI feature element and dynamic convolution kernels at different positions within the bounding box. To validate the effectiveness of the proposed method, we conduct intensive ablations and build the full model on three recent mainstream region-based detectors. The RecusiveDet is able to achieve obvious performance boosts with even fewer model parameters and slightly increased computation cost. Codes are available at https://github.com/bravezzzzzz/RecursiveDet.

</details>

### Class-aware Memory Guided Unbiased Weighting for Universal Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00469) · 📚 被引 2
- **作者**: Qinghai Lang, Zhenwei He, Xiaowei Fu, Lei Zhang
- **🏷️ 机构**: Chongqing University,School of Microelectronics and Communication Engineering,China
- **会议**: ICCV 2023

### Self-training and multi-task learning for limited data: evaluation study on object detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00107) · 📚 被引 1
- **作者**: Hoàng-Ân Lê, Minh-Tan Pham
- **🏷️ 机构**: Universit&#x00E9; Bretagne Sud, UMR 6074,IRISA,Vannes,France,56000
- **会议**: ICCV 2023

### DetOFA: Efficient Training of Once-for-All Networks for Object Detection using Path Filter.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00143) · 📚 被引 3
- **作者**: Yuiko Sakuma, Masato Ishii, Takuya Narihira
- **🏷️ 机构**: Sony Group Corporation,Tokyo,Japan
- **会议**: ICCV 2023

### Identification of Novel Classes for Improving Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00360)
- **作者**: Zeyu Shangguan, Mohammad Rostami
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### InterAug: A Tuning-Free Augmentation Policy for Data-Efficient and Robust Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00033) · 📚 被引 0
- **作者**: Kowshik Thopalli, Devi S, Jayaraman J. Thiagarajan
- **🏷️ 机构**: Lawrence Livermore National Labs,USA, SRM Institute of Science and Technology,India
- **会议**: ICCV 2023

### Fast Object Detection in High-Resolution Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00159) · 📚 被引 0
- **作者**: Ryan Tran, Atul Kanaujia, Vasu Parameswaran
- **🏷️ 机构**: Percipient.ai,Santa Clara,CA
- **会议**: ICCV 2023

### Adaptive Self-Training for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00098)
- **作者**: Renaud Vandeghen, Gilles Louppe, Marc Van Droogenbroeck
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Comparative Study of Natural Replay and Experience Replay in Online Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00386) · 📚 被引 0
- **作者**: Baptiste Wagner, Denis Pellerin, Sylvain Huet
- **🏷️ 机构**: Univ. Grenoble Alpes,CNRS, Grenoble INP, GIPSA-lab,Grenoble,France,38000
- **会议**: ICCV 2023

### Introspection of 2D Object Detection using Processed Neural Activation Patterns in Automated Driving Systems.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00437) · 📚 被引 3
- **作者**: Hakan Yekta Yatbaz, Mehrdad Dianati, Konstantinos Koufos, Roger Woodman
- **🏷️ 机构**: University of Warwick,WMG
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- ObjectFusion: Multi-modal 3D Object Detection with Object-Centric Fusion. → [3d-detection](../3d-detection/Guideline%202023.md)
- Object as Query: Lifting any 2D Object Detector to 3D Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Periodically Exchange Teacher-Student for Source-Free Object Detection. → [knowledge-distillation](../knowledge-distillation/Guideline%202023.md)
- Efficient Transformer-based 3D Object Detection with Dynamic Token Halting. → [3d-detection](../3d-detection/Guideline%202023.md)
- DistillBEV: Boosting Multi-Camera 3D Object Detection with Cross-Modal Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202023.md)
- Revisiting Domain-Adaptive 3D Object Detection by Reliable, Diverse and Class-balanced Pseudo-Labeling. → [3d-detection](../3d-detection/Guideline%202023.md)
- Learning with Noisy Data for Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- FocalFormer3D : Focusing on Hard Instance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Once Detected, Never Lost: Surpassing Human Performance in Offline LiDAR based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- A Fast Unified System for 3D Object Detection and Tracking. → [3d-detection](../3d-detection/Guideline%202023.md)
- UpCycling: Semi-supervised 3D Object Detection without Sharing Raw-level Unlabeled Scenes. → [3d-detection](../3d-detection/Guideline%202023.md)
- Alleviating Catastrophic Forgetting of Incremental Object Detection via Within-Class and Between-Class Knowledge Distillation. → [continual-learning](../continual-learning/Guideline%202023.md)
- Predict to Detect: Prediction-guided 3D Object Detection using Sequential Images. → [3d-detection](../3d-detection/Guideline%202023.md)
- PG-RCNN: Semantic Surface Point Generation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- Representation Disparity-aware Distillation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Videos. → [3d-detection](../3d-detection/Guideline%202023.md)
- Monocular 3D Object Detection with Bounding Box Denoising in 3D by Perceiver. → [3d-detection](../3d-detection/Guideline%202023.md)
- Kecor: Kernel Coding Rate Maximization for Active 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Fair and Comprehensive Comparisons for Image-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- DetZero: Rethinking Offboard 3D Object Detection with Long-term Sequential Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- PARTNER: Level up the Polar Representation for LiDAR 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Clusterformer: Cluster-based Transformer for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- SupFusion: Supervised LiDAR-Camera Fusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- 3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- GraphAlign: Enhancing Accurate Feature Alignment by Graph matching for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- ImGeoNet: Image-induced Geometry-aware Voxel Representation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Not Every Side Is Equal: Localization Uncertainty Estimation for Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Towards Universal LiDAR-Based 3D Object Detection by Multi-Domain Knowledge Transfer. → [3d-detection](../3d-detection/Guideline%202023.md)
- Label-Efficient Online Continual Object Detection in Streaming Video. → [continual-learning](../continual-learning/Guideline%202023.md)
- CoIn: Contrastive Instance Feature Mining for Outdoor 3D Object Detection with Very Limited Annotations. → [3d-detection](../3d-detection/Guideline%202023.md)
- Pixel-Aligned Recurrent Queries for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- MonoNeRD: NeRF-like Representations for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- NeRF-Det: Learning Geometry-Aware Volumetric Representation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Cross Modal Transformer: Towards Fast and Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Parametric Depth Based Feature Representation Learning for Object Detection and Segmentation in Bird's-Eye View. → [bev](../bev/Guideline%202023.md)
- MonoDETR: Depth-guided Transformer for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- QD-BEV : Quantization-aware View-guided Distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- SA-BEV: Generating Semantic-Aware Bird's-Eye-View Feature for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Masked Retraining Teacher-Student Framework for Domain Adaptive Object Detection. → [knowledge-distillation](../knowledge-distillation/Guideline%202023.md)
- An Empirical Analysis of Range for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- On Offline Evaluation of 3D Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202023.md)
- Tensor Factorization for Leveraging Cross-Modal Knowledge in Data-Constrained Infrared Object Detection. → [multimodal](../multimodal/Guideline%202023.md)
