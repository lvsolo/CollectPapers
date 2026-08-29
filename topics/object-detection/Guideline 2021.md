# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UP-DETR: Unsupervised Pre-Training for Object Detection With Transformers.
- **链接**: [arXiv:2011.09094](https://arxiv.org/abs/2011.09094) · [代码](https://github.com/dddzg/up-detr) · 📚 被引 447
- **作者**: Zhigang Dai, Bolun Cai, Yugeng Lin, Junying Chen
- **🏷️ 机构**: South China University of Technology,School of Software Engineering, Tencent Wechat AI
- **会议**: CVPR 2021

### MosaicOS: A Simple and Effective Use of Object-Centric Images for Long-Tailed Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00047) · 📚 被引 37
- **作者**: Cheng Zhang, Tai-Yu Pan, Yandong Li, Hexiang Hu, Dong Xuan, Soravit Changpinyo et al.
- **🏷️ 机构**: The Ohio State University, Google Research, University of Southern California
- **会议**: ICCV 2021

### Uncertainty-Guided Transformer Reasoning for Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00411) · 📚 被引 310
- **作者**: Fan Yang, Qiang Zhai, Xin Li, Rui Huang, Ao Luo, Hong Cheng et al.
- **🏷️ 机构**: AIQ, Uestc, Megvii
- **会议**: ICCV 2021

### Robust Object Detection via Instance-Level Temporal Cycle Confusion.
- **链接**: [arXiv:2104.08381](https://arxiv.org/abs/2104.08381) · 📚 被引 25
- **作者**: Xin Wang, Thomas E. Huang, Benlin Liu, Fisher Yu, Xiaolong Wang, Joseph E. Gonzalez et al.
- **🏷️ 机构**: Microsoft Research, ETH Z&#x00FC;rich, University of Washington
- **会议**: ICCV 2021

### Uncertainty-Aware Joint Salient Object and Camouflaged Object Detection.
- **链接**: [arXiv:2104.02628](https://arxiv.org/abs/2104.02628) · 📚 被引 270
- **作者**: Aixuan Li, Jing Zhang, Yunqiu Lv, Bowen Liu, Tong Zhang, Yuchao Dai
- **🏷️ 机构**: Northwestern Polytechnical University,China, Australian National University,Australia, EPFL,Switzerland
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A large gap exists between fully-supervised object detection and weakly-supervised object detection. To narrow this gap, some methods consider knowledge transfer from additional fully-supervised dataset. But these methods do not fully exploit discriminative category information in the fully-supervised dataset, thus causing low mAP. To solve this issue, we propose a novel category transfer framework for weakly supervised object detection. The intuition is to fully leverage both visually-discriminative and semantically-correlated category information in the fully-supervised dataset to enhance the object-classification ability of a weakly-supervised detector. To handle overlapping category transfer, we propose a double-supervision mean teacher to gather common category information and bridge the domain gap between two datasets. To handle non-overlapping category transfer, we propose a semantic graph convolutional network to promote the aggregation of semantic features between correlated categories. Experiments are conducted with Pascal VOC 2007 as the target weakly-supervised dataset and COCO as the source fully-supervised dataset. Our category transfer framework achieves 63.5% mAP and 80.3% CorLoc with 5 overlapping categories between two datasets, which outperforms the state-of-the-art methods. Codes are avaliable at https://github.com/MediaBrain-SJTU/CaT.

</details>

### Dual Bipartite Graph Learning: A General Approach for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00270) · 📚 被引 59
- **作者**: Chaoqi Chen, Jiongcheng Li, Zebiao Zheng, Yue Huang, Xinghao Ding, Yizhou Yu
- **🏷️ 机构**: The University of Hong Kong, Xiamen University
- **会议**: ICCV 2021

### Robust Small Object Detection on the Water Surface through Fusion of Camera and Millimeter Wave Radar.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01498) · 📚 被引 93
- **作者**: Yuwei Cheng, Hu Xu, Yimin Liu
- **🏷️ 机构**: Tsinghua University, ORCA-Uboat
- **会议**: ICCV 2021

### Active Learning for Deep Object Detection via Probabilistic Modeling.
- **链接**: [arXiv:2103.16130](https://arxiv.org/abs/2103.16130) · 📚 被引 110
- **作者**: Jiwoong Choi, Ismail Elezi, Hyuk-Jae Lee, Clément Farabet, José M. Álvarez
- **🏷️ 机构**: Seoul National University, Technical University of Munich, NVIDIA
- **会议**: ICCV 2021

### Instant-Teaching: An End-to-End Semi-Supervised Object Detection Framework.
- **链接**: [arXiv:2103.11402](https://arxiv.org/abs/2103.11402) · 📚 被引 194
- **作者**: Qiang Zhou, Chaohui Yu, Zhibin Wang, Qi Qian, Hao Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Rank & Sort Loss for Object Detection and Instance Segmentation.
- **链接**: [arXiv:2107.11669](https://arxiv.org/abs/2107.11669) · 📚 被引 46
- **作者**: Kemal Oksuz, Baris Can Cam, Emre Akbas, Sinan Kalkan
- **🏷️ 机构**: Middle East Technical University,Dept. of Computer Engineering,Ankara,Turkey
- **会议**: ICCV 2021

### MFNet: Multi-filter Directive Network for Weakly Supervised Salient Object Detection.
- **链接**: [arXiv:2112.01732](https://arxiv.org/abs/2112.01732) · 📚 被引 85
- **作者**: Yongri Piao, Jian Wang, Miao Zhang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China
- **会议**: ICCV 2021

### DeFRCN: Decoupled Faster R-CNN for Few-Shot Object Detection.
- **链接**: [arXiv:2108.09017](https://arxiv.org/abs/2108.09017) · 📚 被引 363
- **作者**: Limeng Qiao, Yuxuan Zhao, Zhiyuan Li, Xi Qiu, Jianan Wu, Chi Zhang
- **🏷️ 机构**: Megvii Technology
- **会议**: ICCV 2021

### Points As Queries: Weakly Semi-Supervised Object Detection by Points.
- **链接**: [arXiv:2104.07434](https://arxiv.org/abs/2104.07434) · 📚 被引 87
- **作者**: Liangyu Chen, Tong Yang, Xiangyu Zhang, Wei Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### SimROD: A Simple Adaptation Method for Robust Object Detection.
- **链接**: [arXiv:2107.13389](https://arxiv.org/abs/2107.13389) · 📚 被引 47
- **作者**: Rindra Ramamonjison, Amin Banitalebi-Dehkordi, Xinyu Kang, Xiaolong Bai, Yong Zhang
- **🏷️ 机构**: Huawei Technologies Canada Co., Ltd, University of British Columbia, Huawei Cloud
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a Simple and effective unsupervised adaptation method for Robust Object Detection (SimROD). To overcome the challenging issues of domain shift and pseudo-label noise, our method integrates a novel domain-centric augmentation method, a gradual self-labeling adaptation procedure, and a teacher-guided fine-tuning mechanism. Using our method, target domain samples can be leveraged to adapt object detection models without changing the model architecture or generating synthetic data. When applied to image corruptions and high-level cross-domain adaptation benchmarks, our method outperforms prior baselines on multiple domain adaptation benchmarks. SimROD achieves new state-of-the-art on standard real-to-synthetic and cross-camera setup benchmarks. On the image corruption benchmark, models adapted with our method achieved a relative robustness improvement of 15-25% AP50 on Pascal-C and 5-6% AP on COCO-C and Cityscapes-C. On the cross-domain benchmark, our method outperformed the best baseline performance by up to 8% AP50 on Comic dataset and up to 4% on Watercolor dataset.

</details>

### Seeking Similarities over Differences: Similarity-based Domain Alignment for Adaptive Object Detection.
- **链接**: [arXiv:2110.01428](https://arxiv.org/abs/2110.01428) · 📚 被引 74
- **作者**: Farzaneh Rezaeianaran, Rakshith Shetty, Rahaf Aljundi, Daniel Olmeda Reino, Shanshan Zhang, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Toyota Motor Europe, Nanjing University of Science and Technology
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In order to robustly deploy object detectors across a wide range of scenarios, they should be adaptable to shifts in the input distribution without the need to constantly annotate new data. This has motivated research in Unsupervised Domain Adaptation (UDA) algorithms for detection. UDA methods learn to adapt from labeled source domains to unlabeled target domains, by inducing alignment between detector features from source and target domains. Yet, there is no consensus on what features to align and how to do the alignment. In our work, we propose a framework that generalizes the different components commonly used by UDA methods laying the ground for an in-depth analysis of the UDA design space. Specifically, we propose a novel UDA algorithm, ViSGA, a direct implementation of our framework, that leverages the best design choices and introduces a simple but effective method to aggregate features at instance-level based on visual similarity before inducing group alignment via adversarial training. We show that both similarity-based grouping and adversarial training allows our model to focus on coarsely aligning feature groups, without being forced to match all instances across loosely aligned domains. Finally, we examine the applicability of ViSGA to the setting where labeled data are gathered from different sources. Experiments show that not only our method outperforms previous single-source approaches on Sim2Real and Adverse Weather, but also generalizes well to the multi-source setting.

</details>

### Scene Context-Aware Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00412) · 📚 被引 69
- **作者**: Avishek Siris, Jianbo Jiao, Gary K. L. Tam, Xianghua Xie, Rynson W. H. Lau
- **🏷️ 机构**: Swansea University,Department of Computer Science, University of Oxford, City University of Hong Kong
- **会议**: ICCV 2021

### GAIA: A Transfer Learning System of Object Detection That Fits Your Needs.
- **链接**: [arXiv:2106.11346](https://arxiv.org/abs/2106.11346) · 📚 被引 35
- **作者**: Xingyuan Bu, Junran Peng, Junjie Yan, Tieniu Tan, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current state-of-the-art two-stage detectors generate oriented proposals through time-consuming schemes. This diminishes the detectors' speed, thereby becoming the computational bottleneck in advanced oriented object detection systems. This work proposes an effective and simple oriented object detection framework, termed Oriented R-CNN, which is a general two-stage oriented detector with promising accuracy and efficiency. To be specific, in the first stage, we propose an oriented Region Proposal Network (oriented RPN) that directly generates high-quality oriented proposals in a nearly cost-free manner. The second stage is oriented R-CNN head for refining oriented Regions of Interest (oriented RoIs) and recognizing them. Without tricks, oriented R-CNN with ResNet50 achieves state-of-the-art detection accuracy on two commonly-used datasets for oriented object detection including DOTA (75.87% mAP) and HRSC2016 (96.50% mAP), while having a speed of 15.1 FPS with the image size of 1024$\times$1024 on a single RTX 2080Ti. We hope our work could inspire rethinking the design of oriented detectors and serve as a baseline for oriented object detection. Code is available at https://github.com/jbwang1997/OBBDetection.

</details>

### Adaptive Image Transformer for One-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Adaptive_Image_Transformer_for_One-Shot_Object_Detection_CVPR_2021_paper.html) · 📚 被引 57
- **作者**: Ding-Jie Chen, He-Yen Hsieh, Tyng-Luh Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Class-Aware Robust Adversarial Training for Object Detection.
- **链接**: [arXiv:2103.16148](https://arxiv.org/abs/2103.16148) · 📚 被引 52
- **作者**: Pin-Chun Chen, Bo-Han Kung, Jun-Cheng Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Improve Object Detection with Feature-based Knowledge Distillation: Towards Accurate and Efficient Detectors.
- **链接**: [出版页](https://openreview.net/forum?id=uKhGRvM8QNH)
- **作者**: Linfeng Zhang, Kaisheng Ma
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data augmentation has become a de facto component for training high-performance deep image classifiers, but its potential is under-explored for object detection. Noting that most state-of-the-art object detectors benefit from fine-tuning a pre-trained classifier, we first study how the classifiers' gains from various data augmentations transfer to object detection. The results are discouraging; the gains diminish after fine-tuning in terms of either accuracy or robustness. This work instead augments the fine-tuning stage for object detectors by exploring adversarial examples, which can be viewed as a model-dependent data augmentation. Our method dynamically selects the stronger adversarial images sourced from a detector's classification and localization branches and evolves with the detector to ensure the augmentation policy stays current and relevant. This model-dependent augmentation generalizes to different object detectors better than AutoAugment, a model-agnostic augmentation policy searched based on one particular detector. Our approach boosts the performance of state-of-the-art EfficientDets by +1.1 mAP on the COCO object detection benchmark. It also improves the detectors' robustness against natural distortions by +3.8 mAP and against domain shift by +1.3 mAP. Models are available at https://github.com/google/automl/tree/master/efficientdet/Det-AdvProp.md

</details>

### Dynamic Head: Unifying Object Detection Heads With Attentions.
- **链接**: [arXiv:2106.08322](https://arxiv.org/abs/2106.08322) · [代码](https://github.com/microsoft/DynamicHead) · 📚 被引 942
- **作者**: Xiyang Dai, Yinpeng Chen, Bin Xiao, Dongdong Chen, Mengchen Liu, Lu Yuan et al.
- **🏷️ 机构**: Microsoft,Redmond,USA
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The complex nature of combining localization and classification in object detection has resulted in the flourished development of methods. Previous works tried to improve the performance in various object detection heads but failed to present a unified view. In this paper, we present a novel dynamic head framework to unify object detection heads with attentions. By coherently combining multiple self-attention mechanisms between feature levels for scale-awareness, among spatial locations for spatial-awareness, and within output channels for task-awareness, the proposed approach significantly improves the representation ability of object detection heads without any computational overhead. Further experiments demonstrate that the effectiveness and efficiency of the proposed dynamic head on the COCO benchmark. With a standard ResNeXt-101-DCN backbone, we largely improve the performance over popular object detectors and achieve a new state-of-the-art at 54.0 AP. Furthermore, with latest transformer backbone and extra data, we can push current best COCO result to a new record at 60.6 AP. The code will be released at https://github.com/microsoft/DynamicHead.

</details>

### General Instance Distillation for Object Detection.
- **链接**: [arXiv:2103.02340](https://arxiv.org/abs/2103.02340) · 📚 被引 236
- **作者**: Xing Dai, Zeren Jiang, Zhao Wu, Yiping Bao, Zhicheng Wang, Si Liu et al.
- **🏷️ 机构**: MEGVII Technology, BeiHang University
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, knowledge distillation has been proved to be an effective solution for model compression. This approach can make lightweight student models acquire the knowledge extracted from cumbersome teacher models. However, previous distillation methods of detection have weak generalization for different detection frameworks and rely heavily on ground truth (GT), ignoring the valuable relation information between instances. Thus, we propose a novel distillation method for detection tasks based on discriminative instances without considering the positive or negative distinguished by GT, which is called general instance distillation (GID). Our approach contains a general instance selection module (GISM) to make full use of feature-based, relation-based and response-based knowledge for distillation. Extensive results demonstrate that the student model achieves significant AP improvement and even outperforms the teacher in various detection frameworks. Specifically, RetinaNet with ResNet-50 achieves 39.1% in mAP with GID on COCO dataset, which surpasses the baseline 36.2% by 2.9%, and even better than the ResNet-101 based teacher model with 38.1% AP.

</details>

### Unbiased Mean Teacher for Cross-Domain Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Deng_Unbiased_Mean_Teacher_for_Cross-Domain_Object_Detection_CVPR_2021_paper.html) · 📚 被引 336
- **作者**: Jinhong Deng, Wen Li, Yuhua Chen, Lixin Duan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Group Collaborative Learning for Co-Salient Object Detection.
- **链接**: [arXiv:2104.01108](https://arxiv.org/abs/2104.01108) · 📚 被引 101
- **作者**: Qi Fan, Deng-Ping Fan, Huazhu Fu, Chi-Keung Tang, Ling Shao, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel group collaborative learning framework (GCoNet) capable of detecting co-salient objects in real time (16ms), by simultaneously mining consensus representations at group level based on the two necessary criteria: 1) intra-group compactness to better formulate the consistency among co-salient objects by capturing their inherent shared attributes using our novel group affinity module; 2) inter-group separability to effectively suppress the influence of noisy objects on the output by introducing our new group collaborating module conditioning the inconsistent consensus. To learn a better embedding space without extra computational overhead, we explicitly employ auxiliary classification supervision. Extensive experiments on three challenging benchmarks, i.e., CoCA, CoSOD3k, and Cosal2015, demonstrate that our simple GCoNet outperforms 10 cutting-edge models and achieves the new state-of-the-art. We demonstrate this paper's new technical contributions on a number of important downstream computer vision applications including content aware co-segmentation, co-localization based automatic thumbnails, etc.

</details>

### Generalized Few-Shot Object Detection Without Forgetting.
- **链接**: [arXiv:2105.09491](https://arxiv.org/abs/2105.09491) · 📚 被引 166
- **作者**: Zhibo Fan, Yuchen Ma, Zeming Li, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently few-shot object detection is widely adopted to deal with data-limited situations. While most previous works merely focus on the performance on few-shot categories, we claim that detecting all classes is crucial as test samples may contain any instances in realistic applications, which requires the few-shot detector to learn new concepts without forgetting. Through analysis on transfer learning based methods, some neglected but beneficial properties are utilized to design a simple yet effective few-shot detector, Retentive R-CNN. It consists of Bias-Balanced RPN to debias the pretrained RPN and Re-detector to find few-shot class objects without forgetting previous knowledge. Extensive experiments on few-shot detection benchmarks show that Retentive R-CNN significantly outperforms state-of-the-art methods on overall performance among all settings as it can achieve competitive results on few-shot classes and does not degrade the base class performance at all. Our approach has demonstrated that the long desired never-forgetting learner is available in object detection.

</details>

### OTA: Optimal Transport Assignment for Object Detection.
- **链接**: [arXiv:2103.14259](https://arxiv.org/abs/2103.14259) · [代码](https://github.com/Megvii-BaseDetection/OTA) · 📚 被引 484
- **作者**: Zheng Ge, Songtao Liu, Zeming Li, Osamu Yoshie, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in label assignment in object detection mainly seek to independently define positive/negative training samples for each ground-truth (gt) object. In this paper, we innovatively revisit the label assignment from a global perspective and propose to formulate the assigning procedure as an Optimal Transport (OT) problem -- a well-studied topic in Optimization Theory. Concretely, we define the unit transportation cost between each demander (anchor) and supplier (gt) pair as the weighted summation of their classification and regression losses. After formulation, finding the best assignment solution is converted to solve the optimal transport plan at minimal transportation costs, which can be solved via Sinkhorn-Knopp Iteration. On COCO, a single FCOS-ResNet-50 detector equipped with Optimal Transport Assignment (OTA) can reach 40.7% mAP under 1X scheduler, outperforming all other existing assigning methods. Extensive experiments conducted on COCO and CrowdHuman further validate the effectiveness of our proposed OTA, especially its superiority in crowd scenarios. The code is available at https://github.com/Megvii-BaseDetection/OTA.

</details>

### Depth From Camera Motion and Object Detection.
- **链接**: [arXiv:2103.01468](https://arxiv.org/abs/2103.01468) · 📚 被引 33
- **作者**: Brent A. Griffin, Jason J. Corso
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the problem of learning to estimate the depth of detected objects given some measurement of camera motion (e.g., from robot kinematics or vehicle odometry). We achieve this by 1) designing a recurrent neural network (DBox) that estimates the depth of objects using a generalized representation of bounding boxes and uncalibrated camera movement and 2) introducing the Object Depth via Motion and Detection Dataset (ODMD). ODMD training data are extensible and configurable, and the ODMD benchmark includes 21,600 examples across four validation and test sets. These sets include mobile robot experiments using an end-effector camera to locate objects from the YCB dataset and examples with perturbations added to camera motion or bounding box data. In addition to the ODMD benchmark, we evaluate DBox in other monocular application domains, achieving state-of-the-art results on existing driving and robotics benchmarks and estimating the depth of objects using a camera phone.

</details>

### Positive-Unlabeled Data Purification in the Wild for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Guo_Positive-Unlabeled_Data_Purification_in_the_Wild_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 7
- **作者**: Jianyuan Guo, Kai Han, Han Wu, Chao Zhang, Xinghao Chen, Chunjing Xu et al.
- **🏷️ 机构**: Huawei Technologies,Noah&#x2019;s Ark Lab, University of Sydney,School of Computer Science, Faculty of Engineering, Peking University,Key Lab of Machine Perception (MOE),Dept. of Machine Intelligence
- **会议**: CVPR 2021

### Beyond Bounding-Box: Convex-Hull Feature Adaptation for Oriented and Densely Packed Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Guo_Beyond_Bounding-Box_Convex-Hull_Feature_Adaptation_for_Oriented_and_Densely_Packed_CVPR_2021_paper.html) · 📚 被引 244
- **作者**: Zonghao Guo, Chang Liu, Xiaosong Zhang, Jianbin Jiao, Xiangyang Ji, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### ReDet: A Rotation-Equivariant Detector for Aerial Object Detection.
- **链接**: [arXiv:2103.07733](https://arxiv.org/abs/2103.07733) · 📚 被引 889
- **作者**: Jiaming Han, Jian Ding, Nan Xue, Gui-Song Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Informative and Consistent Correspondence Mining for Cross-Domain Weakly Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hou_Informative_and_Consistent_Correspondence_Mining_for_Cross-Domain_Weakly_Supervised_Object_CVPR_2021_paper.html) · 📚 被引 16
- **作者**: Luwei Hou, Yu Zhang, Kui Fu, Jia Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Dense Relation Distillation With Context-Aware Aggregation for Few-Shot Object Detection.
- **链接**: [arXiv:2103.17115](https://arxiv.org/abs/2103.17115) · [代码](https://github.com/hzhupku/DCNet) · 📚 被引 192
- **作者**: Hanzhe Hu, Shuai Bai, Aoxue Li, Jinshi Cui, Liwei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional deep learning based methods for object detection require a large amount of bounding box annotations for training, which is expensive to obtain such high quality annotated data. Few-shot object detection, which learns to adapt to novel classes with only a few annotated examples, is very challenging since the fine-grained feature of novel object can be easily overlooked with only a few data available. In this work, aiming to fully exploit features of annotated novel object and capture fine-grained features of query object, we propose Dense Relation Distillation with Context-aware Aggregation (DCNet) to tackle the few-shot detection problem. Built on the meta-learning based framework, Dense Relation Distillation module targets at fully exploiting support features, where support features and query feature are densely matched, covering all spatial locations in a feed-forward fashion. The abundant usage of the guidance information endows model the capability to handle common challenges such as appearance changes and occlusions. Moreover, to better capture scale-aware features, Context-aware Aggregation module adaptively harnesses features from different scales for a more comprehensive feature representation. Extensive experiments illustrate that our proposed approach achieves state-of-the-art results on PASCAL VOC and MS COCO datasets. Code will be made available at https://github.com/hzhupku/DCNet.

</details>

### SAIL-VOS 3D: A Synthetic Dataset and Baselines for Object Detection and 3D Mesh Reconstruction From Video Data.
- **链接**: [arXiv:2105.08612](https://arxiv.org/abs/2105.08612) · 📚 被引 15
- **作者**: Yuan-Ting Hu, Jiahong Wang, Raymond A. Yeh, Alexander G. Schwing
- **🏷️ 机构**: University of Illinois at Urbana-Champaign
- **会议**: CVPR 2021

### Interpolation-Based Semi-Supervised Learning for Object Detection.
- **链接**: [arXiv:2006.02158](https://arxiv.org/abs/2006.02158) · 📚 被引 45
- **作者**: Jisoo Jeong, Vikas Verma, Minsung Hyun, Juho Kannala, Nojun Kwak
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Calibrated RGB-D Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Ji_Calibrated_RGB-D_Salient_Object_Detection_CVPR_2021_paper.html)
- **作者**: Wei Ji, Jingjing Li, Shuang Yu, Miao Zhang, Yongri Piao, Shunyu Yao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Towards Open World Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Joseph_Towards_Open_World_Object_Detection_CVPR_2021_paper.html)
- **作者**: K. J. Joseph, Salman H. Khan, Fahad Shahbaz Khan, Vineeth N. Balasubramanian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### UniT: Unified Knowledge Transfer for Any-Shot Object Detection and Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Khandelwal_UniT_Unified_Knowledge_Transfer_for_Any-Shot_Object_Detection_and_Segmentation_CVPR_2021_paper.html) · 📚 被引 24
- **作者**: Siddhesh Khandelwal, Raghav Goyal, Leonid Sigal
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Transformation Invariant Few-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Transformation_Invariant_Few-Shot_Object_Detection_CVPR_2021_paper.html) · 📚 被引 88
- **作者**: Aoxue Li, Zhenguo Li
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab,China
- **会议**: CVPR 2021

### Generalized Focal Loss V2: Learning Reliable Localization Quality Estimation for Dense Object Detection.
- **链接**: [arXiv:2011.12885](https://arxiv.org/abs/2011.12885) · [代码](https://github.com/implus/GFocalV2) · 📚 被引 399
- **作者**: Xiang Li, Wenhai Wang, Xiaolin Hu, Jun Li, Jinhui Tang, Jian Yang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: CVPR 2021

### End-to-End Semi-Supervised Object Detection with Soft Teacher.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00305) · 📚 被引 509
- **作者**: Mengde Xu, Zheng Zhang, Han Hu, Jianfeng Wang, Lijuan Wang, Fangyun Wei et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Microsoft
- **会议**: ICCV 2021

### Multi-Source Domain Adaptation for Object Detection.
- **链接**: [arXiv:2106.15793](https://arxiv.org/abs/2106.15793) · 📚 被引 46
- **作者**: Xingxu Yao, Sicheng Zhao, Pengfei Xu, Jufeng Yang
- **🏷️ 机构**: Nankai University,China, Columbia University,USA, Didi Chuxing,China
- **会议**: ICCV 2021

### Dynamic Context-Sensitive Filtering Network for Video Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00158) · 📚 被引 112
- **作者**: Miao Zhang, Jie Liu, Yifei Wang, Yongri Piao, Shunyu Yao, Wei Ji et al.
- **🏷️ 机构**: Dalian University of Technology,China, University of Alberta,Canada
- **会议**: ICCV 2021

### Beyond Max-Margin: Class Margin Equilibrium for Few-Shot Object Detection.
- **链接**: [arXiv:2103.04612](https://arxiv.org/abs/2103.04612) · [代码](https://github.com/Bohao-Lee/CME) · 📚 被引 180
- **作者**: Bohao Li, Boyu Yang, Chang Liu, Feng Liu, Rongrong Ji, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To reduce annotation labor associated with object detection, an increasing number of studies focus on transferring the learned knowledge from a labeled source domain to another unlabeled target domain. However, existing methods assume that the labeled data are sampled from a single source domain, which ignores a more generalized scenario, where labeled data are from multiple source domains. For the more challenging task, we propose a unified Faster R-CNN based framework, termed Divide-and-Merge Spindle Network (DMSN), which can simultaneously enhance domain invariance and preserve discriminative power. Specifically, the framework contains multiple source subnets and a pseudo target subnet. First, we propose a hierarchical feature alignment strategy to conduct strong and weak alignments for low- and high-level features, respectively, considering their different effects for object detection. Second, we develop a novel pseudo subnet learning algorithm to approximate optimal parameters of pseudo target subset by weighted combination of parameters in different source subnets. Finally, a consistency regularization for region proposal network is proposed to facilitate each subnet to learn more abstract invariances. Extensive experiments on different adaptation scenarios demonstrate the effectiveness of the proposed model.

</details>

### Few-Shot Object Detection via Classification Refinement and Distractor Retreatment.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Few-Shot_Object_Detection_via_Classification_Refinement_and_Distractor_Retreatment_CVPR_2021_paper.html) · 📚 被引 83
- **作者**: Yiting Li, Haiyue Zhu, Yu Cheng, Wenxin Wang, Chek Sing Teo, Cheng Xiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### RankDetNet: Delving Into Ranking Constraints for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Liu_RankDetNet_Delving_Into_Ranking_Constraints_for_Object_Detection_CVPR_2021_paper.html) · 📚 被引 15
- **作者**: Ji Liu, Dong Li, Rongzhang Zheng, Lu Tian, Yi Shan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### IQDet: Instance-Wise Quality Distribution Sampling for Object Detection.
- **链接**: [arXiv:2104.06936](https://arxiv.org/abs/2104.06936) · 📚 被引 62
- **作者**: Yuchen Ma, Songtao Liu, Zeming Li, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### Neural Auto-Exposure for High-Dynamic Range Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Onzon_Neural_Auto-Exposure_for_High-Dynamic_Range_Object_Detection_CVPR_2021_paper.html) · 📚 被引 50
- **作者**: Emmanuel Onzon, Fahim Mannan, Felix Heide
- **🏷️ 机构**: Algolux, Princeton University,Algolux
- **会议**: CVPR 2021

### Improved Handling of Motion Blur in Online Object Detection.
- **链接**: [arXiv:2011.14448](https://arxiv.org/abs/2011.14448) · 📚 被引 42
- **作者**: Mohamed Sayed, Gabriel J. Brostow
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We wish to detect specific categories of objects, for online vision systems that will run in the real world. Object detection is already very challenging. It is even harder when the images are blurred, from the camera being in a car or a hand-held phone. Most existing efforts either focused on sharp images, with easy to label ground truth, or they have treated motion blur as one of many generic corruptions. Instead, we focus especially on the details of egomotion induced blur. We explore five classes of remedies, where each targets different potential causes for the performance gap between sharp and blurred images. For example, first deblurring an image changes its human interpretability, but at present, only partly improves object detection. The other four classes of remedies address multi-scale texture, out-of-distribution testing, label generation, and conditioning by blur-type. Surprisingly, we discover that custom label generation aimed at resolving spatial ambiguity, ahead of all others, markedly improves object detection. Also, in contrast to findings from classification, we see a noteworthy boost by conditioning our model on bespoke categories of motion blur. We validate and cross-breed the different remedies experimentally on blurred COCO images and real-world blur datasets, producing an easy and practical favorite model with superior detection rates.

</details>

### FSCE: Few-Shot Object Detection via Contrastive Proposal Encoding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_FSCE_Few-Shot_Object_Detection_via_Contrastive_Proposal_Encoding_CVPR_2021_paper.html) · 📚 被引 505
- **作者**: Bo Sun, Banghuai Li, Shengcai Cai, Ye Yuan, Chi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Sparse R-CNN: End-to-End Object Detection With Learnable Proposals.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_Sparse_R-CNN_End-to-End_Object_Detection_With_Learnable_Proposals_CVPR_2021_paper.html) · 📚 被引 1310
- **作者**: Peize Sun, Rufeng Zhang, Yi Jiang, Tao Kong, Chenfeng Xu, Wei Zhan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Equalization Loss v2: A New Gradient Balance Approach for Long-Tailed Object Detection.
- **链接**: [arXiv:2012.08548](https://arxiv.org/abs/2012.08548) · [代码](https://github.com/tztztztztz/eqlv2) · 📚 被引 179
- **作者**: Jingru Tan, Xin Lu, Gang Zhang, Changqing Yin, Quanquan Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently proposed decoupled training methods emerge as a dominant paradigm for long-tailed object detection. But they require an extra fine-tuning stage, and the disjointed optimization of representation and classifier might lead to suboptimal results. However, end-to-end training methods, like equalization loss (EQL), still perform worse than decoupled training methods. In this paper, we reveal the main issue in long-tailed object detection is the imbalanced gradients between positives and negatives, and find that EQL does not solve it well. To address the problem of imbalanced gradients, we introduce a new version of equalization loss, called equalization loss v2 (EQL v2), a novel gradient guided reweighing mechanism that re-balances the training process for each category independently and equally. Extensive experiments are performed on the challenging LVIS benchmark. EQL v2 outperforms origin EQL by about 4 points overall AP with 14-18 points improvements on the rare categories. More importantly, it also surpasses decoupled training methods. Without further tuning for the Open Images dataset, EQL v2 improves EQL by 7.3 points AP, showing strong generalization ability. Codes have been released at https://github.com/tztztztztz/eqlv2

</details>

### Humble Teachers Teach Better Students for Semi-Supervised Object Detection.
- **链接**: [arXiv:2106.10456](https://arxiv.org/abs/2106.10456) · 📚 被引 180
- **作者**: Yihe Tang, Weifeng Chen, Yijun Luo, Yuting Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a semi-supervised approach for contemporary object detectors following the teacher-student dual model framework. Our method is featured with 1) the exponential moving averaging strategy to update the teacher from the student online, 2) using plenty of region proposals and soft pseudo-labels as the student's training targets, and 3) a light-weighted detection-specific data ensemble for the teacher to generate more reliable pseudo-labels. Compared to the recent state-of-the-art -- STAC, which uses hard labels on sparsely selected hard pseudo samples, the teacher in our model exposes richer information to the student with soft-labels on many proposals. Our model achieves COCO-style AP of 53.04% on VOC07 val set, 8.4% better than STAC, when using VOC12 as unlabeled data. On MS-COCO, it outperforms prior work when only a small percentage of data is taken as labeled. It also reaches 53.8% AP on MS-COCO test-dev with 3.1% gain over the fully supervised ResNet-152 Cascaded R-CNN, by tapping into unlabeled data of a similar size to the labeled data.

</details>

### Unsupervised Object Detection With LIDAR Clues.
- **链接**: [arXiv:2011.12953](https://arxiv.org/abs/2011.12953) · 📚 被引 26
- **作者**: Hao Tian, Yuntao Chen, Jifeng Dai, Zhaoxiang Zhang, Xizhou Zhu
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the importance of unsupervised object detection, to the best of our knowledge, there is no previous work addressing this problem. One main issue, widely known to the community, is that object boundaries derived only from 2D image appearance are ambiguous and unreliable. To address this, we exploit LiDAR clues to aid unsupervised object detection. By exploiting the 3D scene structure, the issue of localization can be considerably mitigated. We further identify another major issue, seldom noticed by the community, that the long-tailed and open-ended (sub-)category distribution should be accommodated. In this paper, we present the first practical method for unsupervised object detection with the aid of LiDAR clues. In our approach, candidate object segments based on 3D point clouds are firstly generated. Then, an iterative segment labeling process is conducted to assign segment labels and to train a segment labeling network, which is based on features from both 2D images and 3D point clouds. The labeling process is carefully designed so as to mitigate the issue of long-tailed and open-ended distribution. The final segment labels are set as pseudo annotations for object detection network training. Extensive experiments on the large-scale Waymo Open dataset suggest that the derived unsupervised object detection method achieves reasonable accuracy compared with that of strong supervision within the LiDAR visible range. Code shall be released.

</details>

### MeGA-CDA: Memory Guided Attention for Category-Aware Unsupervised Domain Adaptive Object Detection.
- **链接**: [arXiv:2103.04224](https://arxiv.org/abs/2103.04224) · 📚 被引 160
- **作者**: Vibashan VS, Vikram Gupta, Poojan Oza, Vishwanath A. Sindagi, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing approaches for unsupervised domain adaptive object detection perform feature alignment via adversarial training. While these methods achieve reasonable improvements in performance, they typically perform category-agnostic domain alignment, thereby resulting in negative transfer of features. To overcome this issue, in this work, we attempt to incorporate category information into the domain adaptation process by proposing Memory Guided Attention for Category-Aware Domain Adaptation (MeGA-CDA). The proposed method consists of employing category-wise discriminators to ensure category-aware feature alignment for learning domain-invariant discriminative features. However, since the category information is not available for the target samples, we propose to generate memory-guided category-specific attention maps which are then used to route the features appropriately to the corresponding category discriminator. The proposed method is evaluated on several benchmark datasets and is shown to outperform existing approaches.

</details>

### Data-Uncertainty Guided Multi-Phase Learning for Semi-Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Data-Uncertainty_Guided_Multi-Phase_Learning_for_Semi-Supervised_Object_Detection_CVPR_2021_paper.html) · 📚 被引 83
- **作者**: Zhenyu Wang, Yali Li, Ye Guo, Lu Fang, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### End-to-End Object Detection With Fully Convolutional Network.
- **链接**: [arXiv:2012.03544](https://arxiv.org/abs/2012.03544) · [代码](https://github.com/Megvii-BaseDetection/DeFCN)
- **作者**: Jianfeng Wang, Lin Song, Zeming Li, Hongbin Sun, Jian Sun, Nanning Zheng
- **🏷️ 机构**: MEGVII, XJTU
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge distillation has shown great success in classification, however, it is still challenging for detection. In a typical image for detection, representations from different locations may have different contributions to detection targets, making the distillation hard to balance. In this paper, we propose a conditional distillation framework to distill the desired knowledge, namely knowledge that is beneficial in terms of both classification and localization for every instance. The framework introduces a learnable conditional decoding module, which retrieves information given each target instance as query. Specifically, we encode the condition information as query and use the teacher's representations as key. The attention between query and key is used to measure the contribution of different features, guided by a localization-recognition-sensitive auxiliary task. Extensive experiments demonstrate the efficacy of our method: we observe impressive improvements under various settings. Notably, we boost RetinaNet with ResNet-50 backbone from 37.4 to 40.7 mAP (+3.3) under 1x schedule, that even surpasses the teacher (40.4 mAP) with ResNet-101 backbone under 3x schedule. Code has been released on https://github.com/megvii-research/ICD.

</details>

### Joint Semantic Mining for Weakly Supervised RGB-D Salient Object Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/642e92efb79421734881b53e1e1b18b6-Abstract.html)
- **作者**: Jingjing Li, Wei Ji, Qi Bi, Cheng Yan, Miao Zhang, Yongri Piao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Mixed Supervised Object Detection by Transferring Mask Prior and Semantic Similarity.
- **链接**: [arXiv:2110.14191](https://arxiv.org/abs/2110.14191) · [代码](https://github.com/bcmi/TraMaS-Weak-Shot-Object-Detection)
- **作者**: Yan Liu, Zhijie Zhang, Li Niu, Junjie Chen, Liqing Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has achieved promising success, but requires large-scale fully-annotated data, which is time-consuming and labor-extensive. Therefore, we consider object detection with mixed supervision, which learns novel object categories using weak annotations with the help of full annotations of existing base object categories. Previous works using mixed supervision mainly learn the class-agnostic objectness from fully-annotated categories, which can be transferred to upgrade the weak annotations to pseudo full annotations for novel categories. In this paper, we further transfer mask prior and semantic similarity to bridge the gap between novel categories and base categories. Specifically, the ability of using mask prior to help detect objects is learned from base categories and transferred to novel categories. Moreover, the semantic similarity between objects learned from base categories is transferred to denoise the pseudo full annotations for novel categories. Experimental results on three benchmark datasets demonstrate the effectiveness of our method over existing methods. Codes are available at https://github.com/bcmi/TraMaS-Weak-Shot-Object-Detection.

</details>

### SSAL: Synergizing between Self-Training and Adversarial Learning for Domain Adaptive Object Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/c0cccc24dd23ded67404f5e511c342b0-Abstract.html)
- **作者**: Muhammad Akhtar Munir, Muhammad Haris Khan, M. Saquib Sarfraz, Mohsen Ali
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### On Model Calibration for Long-Tailed Object Detection and Instance Segmentation.
- **链接**: [arXiv:2107.02170](https://arxiv.org/abs/2107.02170) · [代码](https://github.com/tydpan/NorCal)
- **作者**: Tai-Yu Pan, Cheng Zhang, Yandong Li, Hexiang Hu, Dong Xuan, Soravit Changpinyo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vanilla models for object detection and instance segmentation suffer from the heavy bias toward detecting frequent objects in the long-tailed setting. Existing methods address this issue mostly during training, e.g., by re-sampling or re-weighting. In this paper, we investigate a largely overlooked approach -- post-processing calibration of confidence scores. We propose NorCal, Normalized Calibration for long-tailed object detection and instance segmentation, a simple and straightforward recipe that reweighs the predicted scores of each class by its training sample size. We show that separately handling the background class and normalizing the scores over classes for each proposal are keys to achieving superior performance. On the LVIS dataset, NorCal can effectively improve nearly all the baseline models not only on rare classes but also on common and frequent classes. Finally, we conduct extensive analysis and ablation studies to offer insights into various modeling choices and mechanisms of our approach. Our code is publicly available at https://github.com/tydpan/NorCal/.

</details>

### Searching Parameterized AP Loss for Object Detection.
- **链接**: [arXiv:2112.05138](https://arxiv.org/abs/2112.05138) · [代码](https://github.com/fundamentalvision/Parameterized-AP-Loss)
- **作者**: Chenxin Tao, Zizhang Li, Xizhou Zhu, Gao Huang, Yong Liu, Jifeng Dai
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Loss functions play an important role in training deep-network-based object detectors. The most widely used evaluation metric for object detection is Average Precision (AP), which captures the performance of localization and classification sub-tasks simultaneously. However, due to the non-differentiable nature of the AP metric, traditional object detectors adopt separate differentiable losses for the two sub-tasks. Such a mis-alignment issue may well lead to performance degradation. To address this, existing works seek to design surrogate losses for the AP metric manually, which requires expertise and may still be sub-optimal. In this paper, we propose Parameterized AP Loss, where parameterized functions are introduced to substitute the non-differentiable components in the AP calculation. Different AP approximations are thus represented by a family of parameterized functions in a unified formula. Automatic parameter search algorithm is then employed to search for the optimal parameters. Extensive experiments on the COCO benchmark with three different object detectors (i.e., RetinaNet, Faster R-CNN, and Deformable DETR) demonstrate that the proposed Parameterized AP Loss consistently outperforms existing handcrafted losses. Code is released at https://github.com/fundamentalvision/Parameterized-AP-Loss.

</details>

### Generalized and Discriminative Few-Shot Object Detection via SVD-Dictionary Enhancement.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/325995af77a0e8b06d1204a171010b3a-Abstract.html)
- **作者**: Aming Wu, Suqi Zhao, Cheng Deng, Wei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Learning High-Precision Bounding Box for Rotated Object Detection via Kullback-Leibler Divergence.
- **链接**: [arXiv:2106.01883](https://arxiv.org/abs/2106.01883) · [代码](https://github.com/yangxue0827/RotationDetection)
- **作者**: Xue Yang, Xiaojiang Yang, Jirui Yang, Qi Ming, Wentao Wang, Qi Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing rotated object detectors are mostly inherited from the horizontal detection paradigm, as the latter has evolved into a well-developed area. However, these detectors are difficult to perform prominently in high-precision detection due to the limitation of current regression loss design, especially for objects with large aspect ratios. Taking the perspective that horizontal detection is a special case for rotated object detection, in this paper, we are motivated to change the design of rotation regression loss from induction paradigm to deduction methodology, in terms of the relation between rotation and horizontal detection. We show that one essential challenge is how to modulate the coupled parameters in the rotation regression loss, as such the estimated parameters can influence to each other during the dynamic joint optimization, in an adaptive and synergetic way. Specifically, we first convert the rotated bounding box into a 2-D Gaussian distribution, and then calculate the Kullback-Leibler Divergence (KLD) between the Gaussian distributions as the regression loss. By analyzing the gradient of each parameter, we show that KLD (and its derivatives) can dynamically adjust the parameter gradients according to the characteristics of the object. It will adjust the importance (gradient weight) of the angle parameter according to the aspect ratio. This mechanism can be vital for high-precision detection as a slight angle error would cause a serious accuracy drop for large aspect ratios objects. More importantly, we have proved that KLD is scale invariant. We further show that the KLD loss can be degenerated into the popular $l_{n}$-norm loss for horizontal detection. Experimental results on seven datasets using different detectors show its consistent superiority, and codes are available at https://github.com/yangxue0827/RotationDetection and https://github.com/open-mmlab/mmrotate.

</details>

## 跨领域论文（完整笔记在其他领域）

- Objects Are Different: Flexible Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- GrooMeD-NMS: Grouped Mathematically Differentiable NMS for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- 3DIoUMatch: Leveraging IoU Prediction for Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- To the Point: Efficient 3D Object Detection in the Range Image With Graph Convolution Kernels. → [3d-detection](../3d-detection/Guideline%202021.md)
- MonoRUn: Monocular 3D Object Detection by Reconstruction and Uncertainty Propagation. → [3d-detection](../3d-detection/Guideline%202021.md)
- Back-Tracing Representative Points for Voting-Based 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202021.md)
- LiDAR-Aug: A General Rendering-Based Augmentation Framework for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- OPANAS: One-Shot Path Aggregation Network Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202021.md)
- Delving Into Localization Errors for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- HVPR: Hybrid Voxel-Point Representation for Single-Stage 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- 3D Object Detection With Pointformer. → [3d-detection](../3d-detection/Guideline%202021.md)
- Offboard 3D Object Detection From Point Cloud Sequences. → [3d-detection](../3d-detection/Guideline%202021.md)
- Categorical Depth Distribution Network for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- RSN: Range Sparse Net for Efficient, Accurate LiDAR 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- There Is More Than Meets the Eye: Self-Supervised Multi-Object Detection and Tracking With Sound by Distilling Multimodal Knowledge. → [multimodal](../multimodal/Guideline%202021.md)
- PointAugmenting: Cross-Modal Augmentation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Depth-Conditioned Dynamic Message Propagation for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
