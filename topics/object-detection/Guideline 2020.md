# Object Detection — 2020 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Cross-Domain Document Object Detection: Benchmark Suite and Method.
- **链接**: [arXiv:2003.13197](https://arxiv.org/abs/2003.13197) · [代码](https://github.com/kailigo/cddod) · 📚 被引 41
- **作者**: Kai Li, Curtis Wigington, Chris Tensmeyer, Handong Zhao, Nikolaos Barmpalios, Vlad I. Morariu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Decomposing images of document pages into high-level semantic regions (e.g., figures, tables, paragraphs), document object detection (DOD) is fundamental for downstream tasks like intelligent document editing and understanding. DOD remains a challenging problem as document objects vary significantly in layout, size, aspect ratio, texture, etc. An additional challenge arises in practice because large labeled training datasets are only available for domains that differ from the target domain. We investigate cross-domain DOD, where the goal is to learn a detector for the target domain using labeled data from the source domain and only unlabeled data from the target domain. Documents from the two domains may vary significantly in layout, language, and genre. We establish a benchmark suite consisting of different types of PDF document datasets that can be utilized for cross-domain DOD model training and evaluation. For each dataset, we provide the page images, bounding box annotations, PDF files, and the rendering layers extracted from the PDF files. Moreover, we propose a novel cross-domain DOD model which builds upon the standard detection model and addresses domain shifts by incorporating three novel alignment modules: Feature Pyramid Alignment (FPA) module, Region Alignment (RA) module and Rendering Layer alignment (RLA) module. Extensive experiments on the benchmark suite substantiate the efficacy of the three proposed modules and the proposed method significantly outperforms the baseline methods. The project page is at \url{https://github.com/kailigo/cddod}.

</details>

### Rethinking Classification and Localization for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wu_Rethinking_Classification_and_Localization_for_Object_Detection_CVPR_2020_paper.html) · 📚 被引 625
- **作者**: Yue Wu, Yinpeng Chen, Lu Yuan, Zicheng Liu, Lijuan Wang, Hongzhi Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Context R-CNN: Long Term Temporal Context for Per-Camera Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Beery_Context_R-CNN_Long_Term_Temporal_Context_for_Per-Camera_Object_Detection_CVPR_2020_paper.html) · 📚 被引 113
- **作者**: Sara Beery, Guanhang Wu, Vivek Rathod, Ronny Votel, Jonathan Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Learning a Unified Sample Weighting Network for Object Detection.
- **链接**: [arXiv:2006.06568](https://arxiv.org/abs/2006.06568) · [代码](https://github.com/caiqi/sample-weighting-network) · 📚 被引 36
- **作者**: Qi Cai, Yingwei Pan, Yu Wang, Jingen Liu, Ting Yao, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Region sampling or weighting is significantly important to the success of modern region-based object detectors. Unlike some previous works, which only focus on "hard" samples when optimizing the objective function, we argue that sample weighting should be data-dependent and task-dependent. The importance of a sample for the objective function optimization is determined by its uncertainties to both object classification and bounding box regression tasks. To this end, we devise a general loss function to cover most region-based object detectors with various sampling strategies, and then based on it we propose a unified sample weighting network to predict a sample's task weights. Our framework is simple yet effective. It leverages the samples' uncertainty distributions on classification loss, regression loss, IoU, and probability score, to predict sample weights. Our approach has several advantages: (i). It jointly learns sample weights for both classification and regression tasks, which differentiates it from most previous work. (ii). It is a data-driven process, so it avoids some manual parameter tuning. (iii). It can be effortlessly plugged into most object detectors and achieves noticeable performance improvements without affecting their inference time. Our approach has been thoroughly evaluated with recent object detection frameworks and it can consistently boost the detection accuracy. Code has been made available at \url{https://github.com/caiqi/sample-weighting-network}.

</details>

### D2Det: Towards High Quality Object Detection and Instance Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Cao_D2Det_Towards_High_Quality_Object_Detection_and_Instance_Segmentation_CVPR_2020_paper.html) · 📚 被引 179
- **作者**: Jiale Cao, Hisham Cholakkal, Rao Muhammad Anwer, Fahad Shahbaz Khan, Yanwei Pang, Ling Shao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Prime Sample Attention in Object Detection.
- **链接**: [arXiv:1904.04821](https://arxiv.org/abs/1904.04821) · 📚 被引 187
- **作者**: Yuhang Cao, Kai Chen, Chen Change Loy, Dahua Lin
- **🏷️ 机构**: NTU S-Lab, CUHK
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> It is a common paradigm in object detection frameworks to treat all samples equally and target at maximizing the performance on average. In this work, we revisit this paradigm through a careful study on how different samples contribute to the overall performance measured in terms of mAP. Our study suggests that the samples in each mini-batch are neither independent nor equally important, and therefore a better classifier on average does not necessarily mean higher mAP. Motivated by this study, we propose the notion of Prime Samples, those that play a key role in driving the detection performance. We further develop a simple yet effective sampling and learning strategy called PrIme Sample Attention (PISA) that directs the focus of the training process towards such samples. Our experiments demonstrate that it is often more effective to focus on prime samples than hard samples when training a detector. Particularly, On the MSCOCO dataset, PISA outperforms the random sampling baseline and hard mining schemes, e.g., OHEM and Focal Loss, consistently by around 2% on both single-stage and two-stage detectors, even with a strong backbone ResNeXt-101.

</details>

### Memory Enhanced Global-Local Aggregation for Video Object Detection.
- **链接**: [arXiv:2003.12063](https://arxiv.org/abs/2003.12063) · [代码](https://github.com/Scalsol/mega.pytorch) · 📚 被引 316
- **作者**: Yihong Chen, Yue Cao, Han Hu, Liwei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How do humans recognize an object in a piece of video? Due to the deteriorated quality of single frame, it may be hard for people to identify an occluded object in this frame by just utilizing information within one image. We argue that there are two important cues for humans to recognize objects in videos: the global semantic information and the local localization information. Recently, plenty of methods adopt the self-attention mechanisms to enhance the features in key frame with either global semantic information or local localization information. In this paper we introduce memory enhanced global-local aggregation (MEGA) network, which is among the first trials that takes full consideration of both global and local information. Furthermore, empowered by a novel and carefully-designed Long Range Memory (LRM) module, our proposed MEGA could enable the key frame to get access to much more content than any previous methods. Enhanced by these two sources of information, our method achieves state-of-the-art performance on ImageNet VID dataset. Code is available at \url{https://github.com/Scalsol/mega.pytorch}.

</details>

> The Feature Pyramid Network (FPN) presents a remarkable approach to alleviate the scale variance in object representation by performing instance-level assignments. Nevertheless, this strategy ignores the distinct characteristics of different sub-regions in an instance. To this end, we propose a fine-grained dynamic head to conditionally select a pixel-level combination of FPN features from different scales for each instance, which further releases the ability of multi-scale feature representation. Moreover, we design a spatial gate with the new activation function to reduce computational complexity dramatically through spatially sparse convolutions. Extensive experiments demonstrate the effectiveness and efficiency of the proposed method on several state-of-the-art detection benchmarks. Code is available at https://github.com/StevenGrove/DynamicHead.

</details>

### Restoring Negative Information in Few-Shot Object Detection.
- **链接**: [arXiv:2010.11714](https://arxiv.org/abs/2010.11714) · [代码](https://github.com/yang-yk/NP-RepMet)
- **作者**: Yukuan Yang, Fangyun Wei, Miaojing Shi, Guoqi Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Based on the framework of multiple instance learning (MIL), tremendous works have promoted the advances of weakly supervised object detection (WSOD). However, most MIL-based methods tend to localize instances to their discriminative parts instead of the whole content. In this paper, we propose a spatial likelihood voting (SLV) module to converge the proposal localizing process without any bounding box annotations. Specifically, all region proposals in a given image play the role of voters every iteration during training, voting for the likelihood of each category in spatial dimensions. After dilating alignment on the area with large likelihood values, the voting results are regularized as bounding boxes, being used for the final classification and localization. Based on SLV, we further propose an end-to-end training framework for multi-task learning. The classification and localization tasks promote each other, which further improves the detection performance. Extensive experiments on the PASCAL VOC 2007 and 2012 datasets demonstrate the superior performance of SLV.

</details>

</details>

### CoADNet: Collaborative Aggregation-and-Distribution Networks for Co-Salient Object Detection.
- **链接**: [arXiv:2011.04887](https://arxiv.org/abs/2011.04887)
- **作者**: Qijian Zhang, Runmin Cong, Junhui Hou, Chongyi Li, Yao Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the blooming success of architecture search for vision tasks in resource-constrained environments, the design of on-device object detection architectures have mostly been manual. The few automated search efforts are either centered around non-mobile-friendly search spaces or not guided by on-device latency. We propose MnasFPN, a mobile-friendly search space for the detection head, and combine it with latency-aware architecture search to produce efficient object detection models. The learned MnasFPN head, when paired with MobileNetV2 body, outperforms MobileNetV3+SSDLite by 1.8 mAP at similar latency on Pixel. It is also both 1.0 mAP more accurate and 10% faster than NAS-FPNLite. Ablation studies show that the majority of the performance gain comes from innovations in the search space. Further explorations reveal an interesting coupling between the search space design and the search algorithm, and that the complexity of MnasFPN search space may be at a local optimum.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Keypoint-based detectors have achieved pretty-well performance. However, incorrect keypoint matching is still widespread and greatly affects the performance of the detector. In this paper, we propose CentripetalNet which uses centripetal shift to pair corner keypoints from the same instance. CentripetalNet predicts the position and the centripetal shift of the corner points and matches corners whose shifted results are aligned. Combining position information, our approach matches corner points more accurately than the conventional embedding approaches do. Corner pooling extracts information inside the bounding boxes onto the border. To make this information more aware at the corners, we design a cross-star deformable convolution network to conduct feature adaption. Furthermore, we explore instance segmentation on anchor-free detectors by equipping our CentripetalNet with a mask prediction module. On MS-COCO test-dev, our CentripetalNet not only outperforms all existing anchor-free detectors with an AP of 48.0% but also achieves comparable performance to the state-of-the-art instance segmentation approaches with a 40.2% MaskAP. Code will be available at https://github.com/KiveeDong/CentripetalNet.

</details>

### Associate-3Ddet: Perceptual-to-Conceptual Association for 3D Point Cloud Object Detection.
- **链接**: [arXiv:2006.04356](https://arxiv.org/abs/2006.04356) · 📚 被引 86
- **作者**: Liang Du, Xiaoqing Ye, Xiao Tan, Jianfeng Feng, Zhenbo Xu, Errui Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection from 3D point clouds remains a challenging task, though recent studies pushed the envelope with the deep learning techniques. Owing to the severe spatial occlusion and inherent variance of point density with the distance to sensors, appearance of a same object varies a lot in point cloud data. Designing robust feature representation against such appearance changes is hence the key issue in a 3D object detection method. In this paper, we innovatively propose a domain adaptation like approach to enhance the robustness of the feature representation. More specifically, we bridge the gap between the perceptual domain where the feature comes from a real scene and the conceptual domain where the feature is extracted from an augmented scene consisting of non-occlusion point cloud rich of detailed information. This domain adaptation approach mimics the functionality of the human brain when proceeding object perception. Extensive experiments demonstrate that our simple yet effective approach fundamentally boosts the performance of 3D point cloud object detection and achieves the state-of-the-art results.

</details>

### Few-Shot Object Detection With Attention-RPN and Multi-Relation Detector.
- **链接**: [arXiv:1908.01998](https://arxiv.org/abs/1908.01998) · [代码](https://github.com/fanq15/Few-Shot-Object-Detection-Dataset) · 📚 被引 522
- **作者**: Qi Fan, Wei Zhuo, Chi-Keung Tang, Yu-Wing Tai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Conventional methods for object detection typically require a substantial amount of training data and preparing such high-quality training data is very labor-intensive. In this paper, we propose a novel few-shot object detection network that aims at detecting objects of unseen categories with only a few annotated examples. Central to our method are our Attention-RPN, Multi-Relation Detector and Contrastive Training strategy, which exploit the similarity between the few shot support set and query set to detect novel objects while suppressing false detection in the background. To train our network, we contribute a new dataset that contains 1000 categories of various objects with high-quality annotations. To the best of our knowledge, this is one of the first datasets specifically designed for few-shot object detection. Once our few-shot network is trained, it can detect objects of unseen categories without further training or fine-tuning. Our method is general and has a wide range of potential applications. We produce a new state-of-the-art performance on different datasets in the few-shot setting. The dataset link is https://github.com/fanq15/Few-Shot-Object-Detection-Dataset.

</details>

### Camouflaged Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Fan_Camouflaged_Object_Detection_CVPR_2020_paper.html)
- **作者**: Deng-Ping Fan, Ge-Peng Ji, Guolei Sun, Ming-Ming Cheng, Jianbing Shen, Ling Shao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Taking a Deeper Look at Co-Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Fan_Taking_a_Deeper_Look_at_Co-Salient_Object_Detection_CVPR_2020_paper.html) · 📚 被引 77
- **作者**: Deng-Ping Fan, Zheng Lin, Ge-Peng Ji, Dingwen Zhang, Huazhu Fu, Ming-Ming Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection.
- **链接**: [arXiv:2004.08515](https://arxiv.org/abs/2004.08515) · [代码](https://github.com/kerenfu/JLDCF) · 📚 被引 308
- **作者**: Keren Fu, Deng-Ping Fan, Ge-Peng Ji, Qijun Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a novel joint learning and densely-cooperative fusion (JL-DCF) architecture for RGB-D salient object detection. Existing models usually treat RGB and depth as independent information and design separate networks for feature extraction from each. Such schemes can easily be constrained by a limited amount of training data or over-reliance on an elaborately-designed training process. In contrast, our JL-DCF learns from both RGB and depth inputs through a Siamese network. To this end, we propose two effective components: joint learning (JL), and densely-cooperative fusion (DCF). The JL module provides robust saliency feature learning, while the latter is introduced for complementary feature discovery. Comprehensive experiments on four popular metrics show that the designed framework yields a robust RGB-D saliency detector with good generalization. As a result, JL-DCF significantly advances the top-1 D3Net model by an average of ~1.9% (S-measure) across six challenging datasets, showing that the proposed framework offers a potential solution for real-world applications and could provide more insight into the cross-modality complementarity task. The code will be available at https://github.com/kerenfu/JLDCF/.

</details>

### AugFPN: Improving Multi-Scale Feature Learning for Object Detection.
- **链接**: [arXiv:1912.05384](https://arxiv.org/abs/1912.05384) · 📚 被引 515
- **作者**: Chaoxu Guo, Bin Fan, Qian Zhang, Shiming Xiang, Chunhong Pan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current state-of-the-art detectors typically exploit feature pyramid to detect objects at different scales. Among them, FPN is one of the representative works that build a feature pyramid by multi-scale features summation. However, the design defects behind prevent the multi-scale features from being fully exploited. In this paper, we begin by first analyzing the design defects of feature pyramid in FPN, and then introduce a new feature pyramid architecture named AugFPN to address these problems. Specifically, AugFPN consists of three components: Consistent Supervision, Residual Feature Augmentation, and Soft RoI Selection. AugFPN narrows the semantic gaps between features of different scales before feature fusion through Consistent Supervision. In feature fusion, ratio-invariant context information is extracted by Residual Feature Augmentation to reduce the information loss of feature map at the highest pyramid level. Finally, Soft RoI Selection is employed to learn a better RoI feature adaptively after feature fusion. By replacing FPN with AugFPN in Faster R-CNN, our models achieve 2.3 and 1.6 points higher Average Precision (AP) when using ResNet50 and MobileNet-v2 as backbone respectively. Furthermore, AugFPN improves RetinaNet by 1.6 points AP and FCOS by 0.9 points AP when using ResNet50 as backbone. Codes will be made available.

</details>

### Cylindrical Convolutional Networks for Joint Object Detection and Viewpoint Estimation.
- **链接**: [arXiv:2003.11303](https://arxiv.org/abs/2003.11303) · 📚 被引 14
- **作者**: Sunghun Joung, Seungryong Kim, Hanjae Kim, Minsu Kim, Ig-Jae Kim, Junghyun Cho et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing techniques to encode spatial invariance within deep convolutional neural networks only model 2D transformation fields. This does not account for the fact that objects in a 2D space are a projection of 3D ones, and thus they have limited ability to severe object viewpoint changes. To overcome this limitation, we introduce a learnable module, cylindrical convolutional networks (CCNs), that exploit cylindrical representation of a convolutional kernel defined in the 3D space. CCNs extract a view-specific feature through a view-specific convolutional kernel to predict object category scores at each viewpoint. With the view-specific feature, we simultaneously determine objective category and viewpoints using the proposed sinusoidal soft-argmax module. Our experiments demonstrate the effectiveness of the cylindrical convolutional networks on joint object detection and viewpoint estimation.

</details>

### Multiple Anchor Learning for Visual Object Detection.
- **链接**: [arXiv:1912.02252](https://arxiv.org/abs/1912.02252) · 📚 被引 82
- **作者**: Wei Ke, Tianliang Zhang, Zeyi Huang, Qixiang Ye, Jianzhuang Liu, Dong Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Classification and localization are two pillars of visual object detectors. However, in CNN-based detectors, these two modules are usually optimized under a fixed set of candidate (or anchor) bounding boxes. This configuration significantly limits the possibility to jointly optimize classification and localization. In this paper, we propose a Multiple Instance Learning (MIL) approach that selects anchors and jointly optimizes the two modules of a CNN-based object detector. Our approach, referred to as Multiple Anchor Learning (MAL), constructs anchor bags and selects the most representative anchors from each bag. Such an iterative selection process is potentially NP-hard to optimize. To address this issue, we solve MAL by repetitively depressing the confidence of selected anchors by perturbing their corresponding features. In an adversarial selection-depression manner, MAL not only pursues optimal solutions but also fully leverages multiple anchors/features to learn a detection model. Experiments show that MAL improves the baseline RetinaNet with significant margins on the commonly used MS-COCO object detection benchmark and achieves new state-of-the-art detection performance compared with recent methods.

</details>

### NETNet: Neighbor Erasing and Transferring Network for Better Single Shot Object Detection.
- **链接**: [arXiv:2001.06690](https://arxiv.org/abs/2001.06690) · 📚 被引 36
- **作者**: Yazhao Li, Yanwei Pang, Jianbing Shen, Jiale Cao, Ling Shao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the advantages of real-time detection and improved performance, single-shot detectors have gained great attention recently. To solve the complex scale variations, single-shot detectors make scale-aware predictions based on multiple pyramid layers. However, the features in the pyramid are not scale-aware enough, which limits the detection performance. Two common problems in single-shot detectors caused by object scale variations can be observed: (1) small objects are easily missed; (2) the salient part of a large object is sometimes detected as an object. With this observation, we propose a new Neighbor Erasing and Transferring (NET) mechanism to reconfigure the pyramid features and explore scale-aware features. In NET, a Neighbor Erasing Module (NEM) is designed to erase the salient features of large objects and emphasize the features of small objects in shallow layers. A Neighbor Transferring Module (NTM) is introduced to transfer the erased features and highlight large objects in deep layers. With this mechanism, a single-shot network called NETNet is constructed for scale-aware object detection. In addition, we propose to aggregate nearest neighboring pyramid features to enhance our NET. NETNet achieves 38.5% AP at a speed of 27 FPS and 32.0% AP at a speed of 55 FPS on MS COCO dataset. As a result, NETNet achieves a better trade-off for real-time and accurate object detection.

</details>

### Overcoming Classifier Imbalance for Long-Tail Object Detection With Balanced Group Softmax.
- **链接**: [arXiv:2006.10408](https://arxiv.org/abs/2006.10408) · [代码](https://github.com/FishYuLi/BalancedGroupSoftmax) · 📚 被引 231
- **作者**: Yu Li, Tao Wang, Bingyi Kang, Sheng Tang, Chunfeng Wang, Jintao Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Solving long-tail large vocabulary object detection with deep learning based models is a challenging and demanding task, which is however under-explored.In this work, we provide the first systematic analysis on the underperformance of state-of-the-art models in front of long-tail distribution. We find existing detection methods are unable to model few-shot classes when the dataset is extremely skewed, which can result in classifier imbalance in terms of parameter magnitude. Directly adapting long-tail classification models to detection frameworks can not solve this problem due to the intrinsic difference between detection and classification.In this work, we propose a novel balanced group softmax (BAGS) module for balancing the classifiers within the detection frameworks through group-wise training. It implicitly modulates the training process for the head and tail classes and ensures they are both sufficiently trained, without requiring any extra sampling for the instances from the tail classes.Extensive experiments on the very recent long-tail large vocabulary object recognition benchmark LVIS show that our proposed BAGS significantly improves the performance of detectors with various backbones and frameworks on both object detection and instance segmentation. It beats all state-of-the-art methods transferred from long-tail image classification and establishes new state-of-the-art.Code is available at https://github.com/FishYuLi/BalancedGroupSoftmax.

</details>

### Learning From Noisy Anchors for One-Stage Object Detection.
- **链接**: [arXiv:1912.05086](https://arxiv.org/abs/1912.05086) · 📚 被引 86
- **作者**: Hengduo Li, Zuxuan Wu, Chen Zhu, Caiming Xiong, Richard Socher, Larry S. Davis
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art object detectors rely on regressing and classifying an extensive list of possible anchors, which are divided into positive and negative samples based on their intersection-over-union (IoU) with corresponding groundtruth objects. Such a harsh split conditioned on IoU results in binary labels that are potentially noisy and challenging for training. In this paper, we propose to mitigate noise incurred by imperfect label assignment such that the contributions of anchors are dynamically determined by a carefully constructed cleanliness score associated with each anchor. Exploring outputs from both regression and classification branches, the cleanliness scores, estimated without incurring any additional computational overhead, are used not only as soft labels to supervise the training of the classification branch but also sample re-weighting factors for improved localization and classification accuracy. We conduct extensive experiments on COCO, and demonstrate, among other things, the proposed approach steadily improves RetinaNet by ~2% with various backbones.

</details>

### Dynamic Refinement Network for Oriented and Densely Packed Object Detection.
- **链接**: [arXiv:2005.09973](https://arxiv.org/abs/2005.09973) · [代码](https://github.com/Anymake/DRN_CVPR2020) · 📚 被引 382
- **作者**: Xingjia Pan, Yuqiang Ren, Kekai Sheng, Weiming Dong, Haolei Yuan, Xiaowei Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has achieved remarkable progress in the past decade. However, the detection of oriented and densely packed objects remains challenging because of following inherent reasons: (1) receptive fields of neurons are all axis-aligned and of the same shape, whereas objects are usually of diverse shapes and align along various directions; (2) detection models are typically trained with generic knowledge and may not generalize well to handle specific objects at test time; (3) the limited dataset hinders the development on this task. To resolve the first two issues, we present a dynamic refinement network that consists of two novel components, i.e., a feature selection module (FSM) and a dynamic refinement head (DRH). Our FSM enables neurons to adjust receptive fields in accordance with the shapes and orientations of target objects, whereas the DRH empowers our model to refine the prediction dynamically in an object-aware manner. To address the limited availability of related benchmarks, we collect an extensive and fully annotated dataset, namely, SKU110K-R, which is relabeled with oriented bounding boxes based on SKU110K. We perform quantitative evaluations on several publicly available benchmarks including DOTA, HRSC2016, SKU110K, and our own SKU110K-R dataset. Experimental results show that our method achieves consistent and substantial gains compared with baseline approaches. The code and dataset are available at https://github.com/Anymake/DRN_CVPR2020.

</details>

### Multi-Scale Interactive Network for Salient Object Detection.
- **链接**: [arXiv:2007.09062](https://arxiv.org/abs/2007.09062) · 📚 被引 751
- **作者**: Youwei Pang, Xiaoqi Zhao, Lihe Zhang, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Large-Scale Object Detection in the Wild From Imbalanced Multi-Labels.
- **链接**: [arXiv:2005.08455](https://arxiv.org/abs/2005.08455) · 📚 被引 54
- **作者**: Junran Peng, Xingyuan Bu, Ming Sun, Zhaoxiang Zhang, Tieniu Tan, Junjie Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training with more data has always been the most stable and effective way of improving performance in deep learning era. As the largest object detection dataset so far, Open Images brings great opportunities and challenges for object detection in general and sophisticated scenarios. However, owing to its semi-automatic collecting and labeling pipeline to deal with the huge data scale, Open Images dataset suffers from label-related problems that objects may explicitly or implicitly have multiple labels and the label distribution is extremely imbalanced. In this work, we quantitatively analyze these label problems and provide a simple but effective solution. We design a concurrent softmax to handle the multi-label problems in object detection and propose a soft-sampling methods with hybrid training scheduler to deal with the label imbalance. Overall, our method yields a dramatic improvement of 3.34 points, leading to the best single model with 60.90 mAP on the public object detection test set of Open Images. And our ensembling result achieves 67.17 mAP, which is 4.29 points higher than the best result of Open Images public test 2018.

</details>

### Incremental Few-Shot Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Perez-Rua_Incremental_Few-Shot_Object_Detection_CVPR_2020_paper.html)
- **作者**: Juan-Manuel Pérez-Rúa, Xiatian Zhu, Timothy M. Hospedales, Tao Xiang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### A2dele: Adaptive and Attentive Depth Distiller for Efficient RGB-D Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Piao_A2dele_Adaptive_and_Attentive_Depth_Distiller_for_Efficient_RGB-D_Salient_CVPR_2020_paper.html) · 📚 被引 236
- **作者**: Yongri Piao, Zhengkun Rong, Miao Zhang, Weisong Ren, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### DR Loss: Improving Object Detection by Distributional Ranking.
- **链接**: [arXiv:1907.10156](https://arxiv.org/abs/1907.10156) · [代码](https://github.com/idstcv/DR_loss) · 📚 被引 60
- **作者**: Qi Qian, Lei Chen, Hao Li, Rong Jin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of object detection algorithms can be categorized into two classes: two-stage detectors and one-stage detectors. Recently, many efforts have been devoted to one-stage detectors for the simple yet effective architecture. Different from two-stage detectors, one-stage detectors aim to identify foreground objects from all candidates in a single stage. This architecture is efficient but can suffer from the imbalance issue with respect to two aspects: the inter-class imbalance between the number of candidates from foreground and background classes and the intra-class imbalance in the hardness of background candidates, where only a few candidates are hard to be identified. In this work, we propose a novel distributional ranking (DR) loss to handle the challenge. For each image, we convert the classification problem to a ranking problem, which considers pairs of candidates within the image, to address the inter-class imbalance problem. Then, we push the distributions of confidence scores for foreground and background towards the decision boundary. After that, we optimize the rank of the expectations of derived distributions in lieu of original pairs. Our method not only mitigates the intra-class imbalance issue in background candidates but also improves the efficiency for the ranking algorithm. By merely replacing the focal loss in RetinaNet with the developed DR loss and applying ResNet-101 as the backbone, mAP of the single-scale test on COCO can be improved from 39.1% to 41.7% without bells and whistles, which demonstrates the effectiveness of the proposed loss function. Code is available at \url{https://github.com/idstcv/DR_loss}.

</details>

### Offset Bin Classification Network for Accurate Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Qiu_Offset_Bin_Classification_Network_for_Accurate_Object_Detection_CVPR_2020_paper.html) · 📚 被引 34
- **作者**: Heqian Qiu, Hongliang Li, Qingbo Wu, Hengcan Shi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Instance-Aware, Context-Focused, and Memory-Efficient Weakly Supervised Object Detection.
- **链接**: [arXiv:2004.04725](https://arxiv.org/abs/2004.04725) · [代码](https://github.com/NVlabs/wetectron) · 📚 被引 183
- **作者**: Zhongzheng Ren, Zhiding Yu, Xiaodong Yang, Ming-Yu Liu, Yong Jae Lee, Alexander G. Schwing et al.
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised learning has emerged as a compelling tool for object detection by reducing the need for strong supervision during training. However, major challenges remain: (1) differentiation of object instances can be ambiguous; (2) detectors tend to focus on discriminative parts rather than entire objects; (3) without ground truth, object proposals have to be redundant for high recalls, causing significant memory consumption. Addressing these challenges is difficult, as it often requires to eliminate uncertainties and trivial solutions. To target these issues we develop an instance-aware and context-focused unified framework. It employs an instance-aware self-training algorithm and a learnable Concrete DropBlock while devising a memory-efficient sequential batch back-propagation. Our proposed method achieves state-of-the-art results on COCO ($12.1\% ~AP$, $24.8\% ~AP_{50}$), VOC 2007 ($54.9\% ~AP$), and VOC 2012 ($52.1\% ~AP$), improving baselines by great margins. In addition, the proposed method is the first to benchmark ResNet based models and weakly supervised video object detection. Code, models, and more details will be made available at: https://github.com/NVlabs/wetectron.

</details>

### Noise-Aware Fully Webly Supervised Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Shen_Noise-Aware_Fully_Webly_Supervised_Object_Detection_CVPR_2020_paper.html) · 📚 被引 30
- **作者**: Yunhang Shen, Rongrong Ji, Zhiwei Chen, Xiaopeng Hong, Feng Zheng, Jianzhuang Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### EfficientDet: Scalable and Efficient Object Detection.
- **链接**: [arXiv:1911.09070](https://arxiv.org/abs/1911.09070) · [代码](https://github.com/google/automl) · 📚 被引 7871
- **作者**: Mingxing Tan, Ruoming Pang, Quoc V. Le
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model efficiency has become increasingly important in computer vision. In this paper, we systematically study neural network architecture design choices for object detection and propose several key optimizations to improve efficiency. First, we propose a weighted bi-directional feature pyramid network (BiFPN), which allows easy and fast multiscale feature fusion; Second, we propose a compound scaling method that uniformly scales the resolution, depth, and width for all backbone, feature network, and box/class prediction networks at the same time. Based on these optimizations and better backbones, we have developed a new family of object detectors, called EfficientDet, which consistently achieve much better efficiency than prior art across a wide spectrum of resource constraints. In particular, with single model and single-scale, our EfficientDet-D7 achieves state-of-the-art 55.1 AP on COCO test-dev with 77M parameters and 410B FLOPs, being 4x - 9x smaller and using 13x - 42x fewer FLOPs than previous detectors. Code is available at https://github.com/google/automl/tree/master/efficientdet.

</details>

### Physically Realizable Adversarial Examples for LiDAR Object Detection.
- **链接**: [arXiv:2004.00543](https://arxiv.org/abs/2004.00543) · 📚 被引 201
- **作者**: James Tu, Mengye Ren, Sivabalan Manivasagam, Ming Liang, Bin Yang, Richard Du et al.
- **🏷️ 机构**: Waabi / University of Toronto
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern autonomous driving systems rely heavily on deep learning models to process point cloud sensory data; meanwhile, deep models have been shown to be susceptible to adversarial attacks with visually imperceptible perturbations. Despite the fact that this poses a security concern for the self-driving industry, there has been very little exploration in terms of 3D perception, as most adversarial attacks have only been applied to 2D flat images. In this paper, we address this issue and present a method to generate universal 3D adversarial objects to fool LiDAR detectors. In particular, we demonstrate that placing an adversarial object on the rooftop of any target vehicle to hide the vehicle entirely from LiDAR detectors with a success rate of 80%. We report attack results on a suite of detectors using various input representation of point clouds. We also conduct a pilot study on adversarial defense using data augmentation. This is one step closer towards safer self-driving under unseen conditions from limited training data.

</details>

### Mixture Dense Regression for Object Detection and Human Pose Estimation.
- **链接**: [arXiv:1912.00821](https://arxiv.org/abs/1912.00821) · 📚 被引 41
- **作者**: Ali Varamesh, Tinne Tuytelaars
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mixture models are well-established learning approaches that, in computer vision, have mostly been applied to inverse or ill-defined problems. However, they are general-purpose divide-and-conquer techniques, splitting the input space into relatively homogeneous subsets in a data-driven manner. Not only ill-defined but also well-defined complex problems should benefit from them. To this end, we devise a framework for spatial regression using mixture density networks. We realize the framework for object detection and human pose estimation. For both tasks, a mixture model yields higher accuracy and divides the input space into interpretable modes. For object detection, mixture components focus on object scale, with the distribution of components closely following that of ground truth the object scale. This practically alleviates the need for multi-scale testing, providing a superior speed-accuracy trade-off. For human pose estimation, a mixture model divides the data based on viewpoint and uncertainty -- namely, front and back views, with back view imposing higher uncertainty. We conduct experiments on the MS COCO dataset and do not face any mode collapse.

</details>

### Robust Object Detection Under Occlusion With Context-Aware CompositionalNets.
- **链接**: [arXiv:2005.11643](https://arxiv.org/abs/2005.11643) · 📚 被引 120
- **作者**: Angtian Wang, Yihong Sun, Adam Kortylewski, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting partially occluded objects is a difficult task. Our experimental results show that deep learning approaches, such as Faster R-CNN, are not robust at object detection under occlusion. Compositional convolutional neural networks (CompositionalNets) have been shown to be robust at classifying occluded objects by explicitly representing the object as a composition of parts. In this work, we propose to overcome two limitations of CompositionalNets which will enable them to detect partially occluded objects: 1) CompositionalNets, as well as other DCNN architectures, do not explicitly separate the representation of the context from the object itself. Under strong object occlusion, the influence of the context is amplified which can have severe negative effects for detection at test time. In order to overcome this, we propose to segment the context during training via bounding box annotations. We then use the segmentation to learn a context-aware CompositionalNet that disentangles the representation of the context and the object. 2) We extend the part-based voting scheme in CompositionalNets to vote for the corners of the object's bounding box, which enables the model to reliably estimate bounding boxes for partially occluded objects. Our extensive experiments show that our proposed model can detect objects robustly, increasing the detection performance of strongly occluded vehicles from PASCAL3D+ and MS-COCO by 41% and 35% respectively in absolute performance relative to Faster R-CNN.

</details>

### Scale-Equalizing Pyramid Convolution for Object Detection.
- **链接**: [arXiv:2005.03101](https://arxiv.org/abs/2005.03101) · [代码](https://github.com/jshilong/SEPC) · 📚 被引 119
- **作者**: Xinjiang Wang, Shilong Zhang, Zhuoran Yu, Litong Feng, Wayne Zhang
- **🏷️ 机构**: CUHK / SenseTime
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Feature pyramid has been an efficient method to extract features at different scales. Development over this method mainly focuses on aggregating contextual information at different levels while seldom touching the inter-level correlation in the feature pyramid. Early computer vision methods extracted scale-invariant features by locating the feature extrema in both spatial and scale dimension. Inspired by this, a convolution across the pyramid level is proposed in this study, which is termed pyramid convolution and is a modified 3-D convolution. Stacked pyramid convolutions directly extract 3-D (scale and spatial) features and outperforms other meticulously designed feature fusion modules. Based on the viewpoint of 3-D convolution, an integrated batch normalization that collects statistics from the whole feature pyramid is naturally inserted after the pyramid convolution. Furthermore, we also show that the naive pyramid convolution, together with the design of RetinaNet head, actually best applies for extracting features from a Gaussian pyramid, whose properties can hardly be satisfied by a feature pyramid. In order to alleviate this discrepancy, we build a scale-equalizing pyramid convolution (SEPC) that aligns the shared pyramid convolution kernel only at high-level feature maps. Being computationally efficient and compatible with the head design of most single-stage object detectors, the SEPC module brings significant performance improvement ($>4$AP increase on MS-COCO2017 dataset) in state-of-the-art one-stage object detectors, and a light version of SEPC also has $\sim3.5$AP gain with only around 7% inference time increase. The pyramid convolution also functions well as a stand-alone module in two-stage object detectors and is able to improve the performance by $\sim2$AP. The source code can be found at https://github.com/jshilong/SEPC.

</details>

### Label Decoupling Framework for Salient Object Detection.
- **链接**: [arXiv:2008.11048](https://arxiv.org/abs/2008.11048) · 📚 被引 317
- **作者**: Jun Wei, Shuhui Wang, Zhe Wu, Chi Su, Qingming Huang, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To get more accurate saliency maps, recent methods mainly focus on aggregating multi-level features from fully convolutional network (FCN) and introducing edge information as auxiliary supervision. Though remarkable progress has been achieved, we observe that the closer the pixel is to the edge, the more difficult it is to be predicted, because edge pixels have a very imbalance distribution. To address this problem, we propose a label decoupling framework (LDF) which consists of a label decoupling (LD) procedure and a feature interaction network (FIN). LD explicitly decomposes the original saliency map into body map and detail map, where body map concentrates on center areas of objects and detail map focuses on regions around edges. Detail map works better because it involves much more pixels than traditional edge supervision. Different from saliency map, body map discards edge pixels and only pays attention to center areas. This successfully avoids the distraction from edge pixels during training. Therefore, we employ two branches in FIN to deal with body map and detail map respectively. Feature interaction (FI) is designed to fuse the two complementary branches to predict the saliency map, which is then used to refine the two branches again. This iterative refinement is helpful for learning better representations and more precise saliency maps. Comprehensive experiments on six benchmark datasets demonstrate that LDF outperforms state-of-the-art approaches on different evaluation metrics.

</details>

### Exploring Bottom-Up and Top-Down Cues With Attentive Learning for Webly Supervised Object Detection.
- **链接**: [arXiv:2003.09790](https://arxiv.org/abs/2003.09790) · 📚 被引 10
- **作者**: Zhonghua Wu, Qingyi Tao, Guosheng Lin, Jianfei Cai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fully supervised object detection has achieved great success in recent years. However, abundant bounding boxes annotations are needed for training a detector for novel classes. To reduce the human labeling effort, we propose a novel webly supervised object detection (WebSOD) method for novel classes which only requires the web images without further annotations. Our proposed method combines bottom-up and top-down cues for novel class detection. Within our approach, we introduce a bottom-up mechanism based on the well-trained fully supervised object detector (i.e. Faster RCNN) as an object region estimator for web images by recognizing the common objectiveness shared by base and novel classes. With the estimated regions on the web images, we then utilize the top-down attention cues as the guidance for region classification. Furthermore, we propose a residual feature refinement (RFR) block to tackle the domain mismatch between web domain and the target domain. We demonstrate our proposed method on PASCAL VOC dataset with three different novel/base splits. Without any target-domain novel-class images and annotations, our proposed webly supervised object detection model is able to achieve promising performance for novel classes. Moreover, we also conduct transfer learning experiments on large scale ILSVRC 2013 detection dataset and achieve state-of-the-art performance.

</details>

### Exploring Categorical Regularization for Domain Adaptive Object Detection.
- **链接**: [arXiv:2003.09152](https://arxiv.org/abs/2003.09152) · 📚 被引 293
- **作者**: Chang-Dong Xu, Xing-Ran Zhao, Xin Jin, Xiu-Shen Wei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### LiDAR-Based Online 3D Video Object Detection With Graph-Based Message Passing and Spatiotemporal Transformer Attention.
- **链接**: [arXiv:2004.01389](https://arxiv.org/abs/2004.01389) · 📚 被引 133
- **作者**: Junbo Yin, Jianbing Shen, Chenye Guan, Dingfu Zhou, Ruigang Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing LiDAR-based 3D object detectors usually focus on the single-frame detection, while ignoring the spatiotemporal information in consecutive point cloud frames. In this paper, we propose an end-to-end online 3D video object detector that operates on point cloud sequences. The proposed model comprises a spatial feature encoding component and a spatiotemporal feature aggregation component. In the former component, a novel Pillar Message Passing Network (PMPNet) is proposed to encode each discrete point cloud frame. It adaptively collects information for a pillar node from its neighbors by iterative message passing, which effectively enlarges the receptive field of the pillar feature. In the latter component, we propose an Attentive Spatiotemporal Transformer GRU (AST-GRU) to aggregate the spatiotemporal information, which enhances the conventional ConvGRU with an attentive memory gating mechanism. AST-GRU contains a Spatial Transformer Attention (STA) module and a Temporal Transformer Attention (TTA) module, which can emphasize the foreground objects and align the dynamic objects, respectively. Experimental results demonstrate that the proposed 3D video object detector achieves state-of-the-art performance on the large-scale nuScenes benchmark.

</details>

### Weakly-Supervised Salient Object Detection via Scribble Annotations.
- **链接**: [arXiv:2003.07685](https://arxiv.org/abs/2003.07685) · [代码](https://github.com/JingZhang617/Scribble_Saliency) · 📚 被引 277
- **作者**: Jing Zhang, Xin Yu, Aixuan Li, Peipei Song, Bowen Liu, Yuchao Dai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared with laborious pixel-wise dense labeling, it is much easier to label data by scribbles, which only costs 1$\sim$2 seconds to label one image. However, using scribble labels to learn salient object detection has not been explored. In this paper, we propose a weakly-supervised salient object detection model to learn saliency from such annotations. In doing so, we first relabel an existing large-scale salient object detection dataset with scribbles, namely S-DUTS dataset. Since object structure and detail information is not identified by scribbles, directly training with scribble labels will lead to saliency maps of poor boundary localization. To mitigate this problem, we propose an auxiliary edge detection task to localize object edges explicitly, and a gated structure-aware loss to place constraints on the scope of structure to be recovered. Moreover, we design a scribble boosting scheme to iteratively consolidate our scribble annotations, which are then employed as supervision to learn high-quality saliency maps. As existing saliency evaluation metrics neglect to measure structure alignment of the predictions, the saliency map ranking metric may not comply with human perception. We present a new metric, termed saliency structure measure, to measure the structure alignment of the predicted saliency maps, which is more consistent with human perception. Extensive experiments on six benchmark datasets demonstrate that our method not only outperforms existing weakly-supervised/unsupervised methods, but also is on par with several fully-supervised state-of-the-art models. Our code and data is publicly available at https://github.com/JingZhang617/Scribble_Saliency.

</details>

## 跨领域论文（完整笔记在其他领域）

- MLCVNet: Multi-Level Context VoteNet for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Density-Based Clustering for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202020.md)
- DSGN: Deep Stereo Geometry Network for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- A Hierarchical Graph Network for 3D Object Detection on Point Clouds. → [3d-detection](../3d-detection/Guideline%202020.md)
- MonoPair: Monocular 3D Object Detection Using Pairwise Spatial Relationships. → [3d-detection](../3d-detection/Guideline%202020.md)
- Learning Depth-Guided Convolutions for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Hit-Detector: Hierarchical Trinity Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- Structure Aware Single-Stage 3D Object Detection From Point Cloud. → [3d-detection](../3d-detection/Guideline%202020.md)
- What You See is What You Get: Exploiting Visibility for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- SP-NAS: Serial-to-Parallel Backbone Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- IDA-3D: Instance-Depth-Aware 3D Object Detection From Stereo Vision for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202020.md)
- ImVoteNet: Boosting 3D Object Detection in Point Clouds With Image Votes. → [3d-detection](../3d-detection/Guideline%202020.md)
- End-to-End Pseudo-LiDAR for Image-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Point-GNN: Graph Neural Network for 3D Object Detection in a Point Cloud. → [3d-detection](../3d-detection/Guideline%202020.md)
- Disp R-CNN: Stereo 3D Object Detection via Shape Prior Guided Instance Disparity Estimation. → [3d-detection](../3d-detection/Guideline%202020.md)
- PointPainting: Sequential Fusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- NAS-FCOS: Fast Neural Architecture Search for Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202020.md)
- HVNet: Hybrid Voxel Network for LiDAR Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- SESS: Self-Ensembling Semi-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
