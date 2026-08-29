# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UP-DETR: Unsupervised Pre-Training for Object Detection With Transformers.
- **链接**: [arXiv:2011.09094](https://arxiv.org/abs/2011.09094) · [代码](https://github.com/dddzg/up-detr) · 📚 被引 447
- **作者**: Zhigang Dai, Bolun Cai, Yugeng Lin, Junying Chen
- **🏷️ 机构**: South China University of Technology,School of Software Engineering, Tencent Wechat AI
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DEtection TRansformer (DETR) for object detection reaches competitive performance compared with Faster R-CNN via a transformer encoder-decoder architecture. However, trained with scratch transformers, DETR needs large-scale training data and an extreme long training schedule even on COCO dataset. Inspired by the great success of pre-training transformers in natural language processing, we propose a novel pretext task named random query patch detection in Unsupervised Pre-training DETR (UP-DETR). Specifically, we randomly crop patches from the given image and then feed them as queries to the decoder. The model is pre-trained to detect these query patches from the input image. During the pre-training, we address two critical issues: multi-task learning and multi-query localization. (1) To trade off classification and localization preferences in the pretext task, we find that freezing the CNN backbone is the prerequisite for the success of pre-training transformers. (2) To perform multi-query localization, we develop UP-DETR with multi-query patch detection with attention mask. Besides, UP-DETR also provides a unified perspective for fine-tuning object detection and one-shot detection tasks. In our experiments, UP-DETR significantly boosts the performance of DETR with faster convergence and higher average precision on object detection, one-shot detection and panoptic segmentation. Code and pre-training models: https://github.com/dddzg/up-detr.

</details>

### Uncertainty-Aware Joint Salient Object and Camouflaged Object Detection.
- **链接**: [arXiv:2104.02628](https://arxiv.org/abs/2104.02628) · 📚 被引 270
- **作者**: Aixuan Li, Jing Zhang, Yunqiu Lv, Bowen Liu, Tong Zhang, Yuchao Dai
- **🏷️ 机构**: Northwestern Polytechnical University,China, Australian National University,Australia, EPFL,Switzerland
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual salient object detection (SOD) aims at finding the salient object(s) that attract human attention, while camouflaged object detection (COD) on the contrary intends to discover the camouflaged object(s) that hidden in the surrounding. In this paper, we propose a paradigm of leveraging the contradictory information to enhance the detection ability of both salient object detection and camouflaged object detection. We start by exploiting the easy positive samples in the COD dataset to serve as hard positive samples in the SOD task to improve the robustness of the SOD model. Then, we introduce a similarity measure module to explicitly model the contradicting attributes of these two tasks. Furthermore, considering the uncertainty of labeling in both tasks' datasets, we propose an adversarial learning network to achieve both higher order similarity measure and network confidence estimation. Experimental results on benchmark datasets demonstrate that our solution leads to state-of-the-art (SOTA) performance for both tasks.

</details>

### Instant-Teaching: An End-to-End Semi-Supervised Object Detection Framework.
- **链接**: [arXiv:2103.11402](https://arxiv.org/abs/2103.11402) · 📚 被引 194
- **作者**: Qiang Zhou, Chaohui Yu, Zhibin Wang, Qi Qian, Hao Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised learning based object detection frameworks demand plenty of laborious manual annotations, which may not be practical in real applications. Semi-supervised object detection (SSOD) can effectively leverage unlabeled data to improve the model performance, which is of great significance for the application of object detection models. In this paper, we revisit SSOD and propose Instant-Teaching, a completely end-to-end and effective SSOD framework, which uses instant pseudo labeling with extended weak-strong data augmentations for teaching during each training iteration. To alleviate the confirmation bias problem and improve the quality of pseudo annotations, we further propose a co-rectify scheme based on Instant-Teaching, denoted as Instant-Teaching$^*$. Extensive experiments on both MS-COCO and PASCAL VOC datasets substantiate the superiority of our framework. Specifically, our method surpasses state-of-the-art methods by 4.2 mAP on MS-COCO when using $2\%$ labeled data. Even with full supervised information of MS-COCO, the proposed method still outperforms state-of-the-art methods by about 1.0 mAP. On PASCAL VOC, we can achieve more than 5 mAP improvement by applying VOC07 as labeled data and VOC12 as unlabeled data.

</details>

### Points As Queries: Weakly Semi-Supervised Object Detection by Points.
- **链接**: [arXiv:2104.07434](https://arxiv.org/abs/2104.07434) · 📚 被引 87
- **作者**: Liangyu Chen, Tong Yang, Xiangyu Zhang, Wei Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel point annotated setting for the weakly semi-supervised object detection task, in which the dataset comprises small fully annotated images and large weakly annotated images by points. It achieves a balance between tremendous annotation burden and detection performance. Based on this setting, we analyze existing detectors and find that these detectors have difficulty in fully exploiting the power of the annotated points. To solve this, we introduce a new detector, Point DETR, which extends DETR by adding a point encoder. Extensive experiments conducted on MS-COCO dataset in various data settings show the effectiveness of our method. In particular, when using 20% fully labeled data from COCO, our detector achieves a promising performance, 33.3 AP, which outperforms a strong baseline (FCOS) by 2.0 AP, and we demonstrate the point annotations bring over 10 points in various AR metrics.

</details>

### GAIA: A Transfer Learning System of Object Detection That Fits Your Needs.
- **链接**: [arXiv:2106.11346](https://arxiv.org/abs/2106.11346) · 📚 被引 35
- **作者**: Xingyuan Bu, Junran Peng, Junjie Yan, Tieniu Tan, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transfer learning with pre-training on large-scale datasets has played an increasingly significant role in computer vision and natural language processing recently. However, as there exist numerous application scenarios that have distinctive demands such as certain latency constraints and specialized data distributions, it is prohibitively expensive to take advantage of large-scale pre-training for per-task requirements. In this paper, we focus on the area of object detection and present a transfer learning system named GAIA, which could automatically and efficiently give birth to customized solutions according to heterogeneous downstream needs. GAIA is capable of providing powerful pre-trained weights, selecting models that conform to downstream demands such as latency constraints and specified data domains, and collecting relevant data for practitioners who have very few datapoints for their tasks. With GAIA, we achieve promising results on COCO, Objects365, Open Images, Caltech, CityPersons, and UODB which is a collection of datasets including KITTI, VOC, WiderFace, DOTA, Clipart, Comic, and more. Taking COCO as an example, GAIA is able to efficiently produce models covering a wide range of latency from 16ms to 53ms, and yields AP from 38.2 to 46.5 without whistles and bells. To benefit every practitioner in the community of object detection, GAIA is released at https://github.com/GAIA-vision.

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection is an important computer vision task with plenty of real-world applications; therefore, how to enhance its robustness against adversarial attacks has emerged as a crucial issue. However, most of the previous defense methods focused on the classification task and had few analysis in the context of the object detection task. In this work, to address the issue, we present a novel class-aware robust adversarial training paradigm for the object detection task. For a given image, the proposed approach generates an universal adversarial perturbation to simultaneously attack all the occurred objects in the image through jointly maximizing the respective loss for each object. Meanwhile, instead of normalizing the total loss with the number of objects, the proposed approach decomposes the total loss into class-wise losses and normalizes each class loss using the number of objects for the class. The adversarial training based on the class weighted loss can not only balances the influence of each class but also effectively and evenly improves the adversarial robustness of trained models for all the object classes as compared with the previous defense methods. Furthermore, with the recent development of fast adversarial training, we provide a fast version of the proposed algorithm which can be trained faster than the traditional adversarial training while keeping comparable performance. With extensive experiments on the challenging PASCAL-VOC and MS-COCO datasets, the evaluation results demonstrate that the proposed defense methods can effectively enhance the robustness of the object detection models.

</details>

### Scale-Aware Automatic Augmentation for Object Detection.
- **链接**: [arXiv:2103.17220](https://arxiv.org/abs/2103.17220) · [代码](https://github.com/Jia-Research-Lab/SA-AutoAug) · 📚 被引 49
- **作者**: Yukang Chen, Yanwei Li, Tao Kong, Lu Qi, Ruihang Chu, Lei Li et al.
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Scale-aware AutoAug to learn data augmentation policies for object detection. We define a new scale-aware search space, where both image- and box-level augmentations are designed for maintaining scale invariance. Upon this search space, we propose a new search metric, termed Pareto Scale Balance, to facilitate search with high efficiency. In experiments, Scale-aware AutoAug yields significant and consistent improvement on various object detectors (e.g., RetinaNet, Faster R-CNN, Mask R-CNN, and FCOS), even compared with strong multi-scale training baselines. Our searched augmentation policies are transferable to other datasets and box-level tasks beyond object detection (e.g., instance segmentation and keypoint estimation) to improve performance. The search cost is much less than previous automated augmentation approaches for object detection. It is notable that our searched policies have meaningful patterns, which intuitively provide valuable insight for human data augmentation design. Code and models will be available at https://github.com/Jia-Research-Lab/SA-AutoAug.

</details>

### AQD: Towards Accurate Quantized Object Detection.
- **链接**: [arXiv:2007.06919](https://arxiv.org/abs/2007.06919) · [代码](https://github.com/ziplab/QTool) · 📚 被引 27
- **作者**: Peng Chen, Jing Liu, Bohan Zhuang, Mingkui Tan, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Network quantization allows inference to be conducted using low-precision arithmetic for improved inference efficiency of deep neural networks on edge devices. However, designing aggressively low-bit (e.g., 2-bit) quantization schemes on complex tasks, such as object detection, still remains challenging in terms of severe performance degradation and unverifiable efficiency on common hardware. In this paper, we propose an Accurate Quantized object Detection solution, termed AQD, to fully get rid of floating-point computation. To this end, we target using fixed-point operations in all kinds of layers, including the convolutional layers, normalization layers, and skip connections, allowing the inference to be executed using integer-only arithmetic. To demonstrate the improved latency-vs-accuracy trade-off, we apply the proposed methods on RetinaNet and FCOS. In particular, experimental results on MS-COCO dataset show that our AQD achieves comparable or even better performance compared with the full-precision counterpart under extremely low-bit schemes, which is of great practical value. Source code and models are available at: https://github.com/ziplab/QTool

</details>

### Robust and Accurate Object Detection via Adversarial Learning.
- **链接**: [arXiv:2103.13886](https://arxiv.org/abs/2103.13886) · [代码](https://github.com/google/automl) · 📚 被引 60
- **作者**: Xiangning Chen, Cihang Xie, Mingxing Tan, Li Zhang, Cho-Jui Hsieh, Boqing Gong
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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Localization Quality Estimation (LQE) is crucial and popular in the recent advancement of dense object detectors since it can provide accurate ranking scores that benefit the Non-Maximum Suppression processing and improve detection performance. As a common practice, most existing methods predict LQE scores through vanilla convolutional features shared with object classification or bounding box regression. In this paper, we explore a completely novel and different perspective to perform LQE -- based on the learned distributions of the four parameters of the bounding box. The bounding box distributions are inspired and introduced as "General Distribution" in GFLV1, which describes the uncertainty of the predicted bounding boxes well. Such a property makes the distribution statistics of a bounding box highly correlated to its real localization quality. Specifically, a bounding box distribution with a sharp peak usually corresponds to high localization quality, and vice versa. By leveraging the close correlation between distribution statistics and the real localization quality, we develop a considerably lightweight Distribution-Guided Quality Predictor (DGQP) for reliable LQE based on GFLV1, thus producing GFLV2. To our best knowledge, it is the first attempt in object detection to use a highly relevant, statistical representation to facilitate LQE. Extensive experiments demonstrate the effectiveness of our method. Notably, GFLV2 (ResNet-101) achieves 46.2 AP at 14.6 FPS, surpassing the previous state-of-the-art ATSS baseline (43.6 AP at 14.6 FPS) by absolute 2.6 AP on COCO {\tt test-dev}, without sacrificing the efficiency both in training and inference. Code will be available at https://github.com/implus/GFocalV2.

</details>

### Beyond Max-Margin: Class Margin Equilibrium for Few-Shot Object Detection.
- **链接**: [arXiv:2103.04612](https://arxiv.org/abs/2103.04612) · [代码](https://github.com/Bohao-Lee/CME) · 📚 被引 180
- **作者**: Bohao Li, Boyu Yang, Chang Liu, Feng Liu, Rongrong Ji, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection has made substantial progressby representing novel class objects using the feature representation learned upon a set of base class objects. However,an implicit contradiction between novel class classification and representation is unfortunately ignored. On the one hand, to achieve accurate novel class classification, the distributions of either two base classes must be far away fromeach other (max-margin). On the other hand, to precisely represent novel classes, the distributions of base classes should be close to each other to reduce the intra-class distance of novel classes (min-margin). In this paper, we propose a class margin equilibrium (CME) approach, with the aim to optimize both feature space partition and novel class reconstruction in a systematic way. CME first converts the few-shot detection problem to the few-shot classification problem by using a fully connected layer to decouple localization features. CME then reserves adequate margin space for novel classes by introducing simple-yet-effective class margin loss during feature learning. Finally, CME pursues margin equilibrium by disturbing the features of novel class instances in an adversarial min-max fashion. Experiments on Pascal VOC and MS-COCO datasets show that CME significantly improves upon two baseline detectors (up to $3\sim 5\%$ in average), achieving state-of-the-art performance. Code is available at https://github.com/Bohao-Lee/CME .

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

> Mainstream object detectors based on the fully convolutional network has achieved impressive performance. While most of them still need a hand-designed non-maximum suppression (NMS) post-processing, which impedes fully end-to-end training. In this paper, we give the analysis of discarding NMS, where the results reveal that a proper label assignment plays a crucial role. To this end, for fully convolutional detectors, we introduce a Prediction-aware One-To-One (POTO) label assignment for classification to enable end-to-end detection, which obtains comparable performance with NMS. Besides, a simple 3D Max Filtering (3DMF) is proposed to utilize the multi-scale features and improve the discriminability of convolutions in the local region. With these techniques, our end-to-end framework achieves competitive performance against many state-of-the-art detectors with NMS on COCO and CrowdHuman datasets. The code is available at https://github.com/Megvii-BaseDetection/DeFCN .

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
