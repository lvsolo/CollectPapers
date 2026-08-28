# Object Detection — 2021 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 16 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Few-Shot Object Detection via Association and DIscrimination.
- **链接**: [arXiv:2111.11656](https://arxiv.org/abs/2111.11656)
- **作者**: Yuhang Cao, Jiaqi Wang, Ying Jin, Tong Wu, Kai Chen, Ziwei Liu et al.
- **🏷️ 机构**: CUHK
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has achieved substantial progress in the last decade. However, detecting novel classes with only few samples remains challenging, since deep learning under low data regime usually leads to a degraded feature space. Existing works employ a holistic fine-tuning paradigm to tackle this problem, where the model is first pre-trained on all base classes with abundant samples, and then it is used to carve the novel class feature space. Nonetheless, this paradigm is still imperfect. Durning fine-tuning, a novel class may implicitly leverage the knowledge of multiple base classes to construct its feature space, which induces a scattered feature space, hence violating the inter-class separability. To overcome these obstacles, we propose a two-step fine-tuning framework, Few-shot object detection via Association and DIscrimination (FADI), which builds up a discriminative feature space for each novel class with two integral steps. 1) In the association step, in contrast to implicitly leveraging multiple base classes, we construct a compact novel class feature space via explicitly imitating a specific base class feature space. Specifically, we associate each novel class with a base class according to their semantic similarity. After that, the feature space of a novel class can readily imitate the well-trained feature space of the associated base class. 2) In the discrimination step, to ensure the separability between the novel classes and associated base classes, we disentangle the classification branches for base and novel classes. To further enlarge the inter-class separability between all classes, a set-specialized margin loss is imposed. Extensive experiments on Pascal VOC and MS-COCO datasets demonstrate FADI achieves new SOTA performance, significantly improving the baseline in any shot/split by +18.7. Notably, the advantage is most announced on extremely few-shot scenarios.

</details>

### PolarStream: Streaming Object Detection and Segmentation with Polar Pillars.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/e1e32e235eee1f970470a3a6658dfdd5-Abstract.html)
- **作者**: Qi Chen, Sourabh Vora, Oscar Beijbom
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### An Empirical Study of Adder Neural Networks for Object Detection.
- **链接**: [arXiv:2112.13608](https://arxiv.org/abs/2112.13608)
- **作者**: Xinghao Chen, Chang Xu, Minjing Dong, Chunjing Xu, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adder neural networks (AdderNets) have shown impressive performance on image classification with only addition operations, which are more energy efficient than traditional convolutional neural networks built with multiplications. Compared with classification, there is a strong demand on reducing the energy consumption of modern object detectors via AdderNets for real-world applications such as autonomous driving and face detection. In this paper, we present an empirical study of AdderNets for object detection. We first reveal that the batch normalization statistics in the pre-trained adder backbone should not be frozen, since the relatively large feature variance of AdderNets. Moreover, we insert more shortcut connections in the neck part and design a new feature fusion architecture for avoiding the sparse features of adder layers. We present extensive ablation studies to explore several design choices of adder detectors. Comparisons with state-of-the-arts are conducted on COCO and PASCAL VOC benchmarks. Specifically, the proposed Adder FCOS achieves a 37.8\% AP on the COCO val set, demonstrating comparable performance to that of the convolutional counterpart with an about $1.4\times$ energy reduction.

</details>

### Bridging Non Co-occurrence with Unlabeled In-the-wild Data for Incremental Object Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/ffc58105bf6f8a91aba0fa2d99e6f106-Abstract.html) · 📚 被引 4
- **作者**: Na Dong, Yongqiang Zhang, Mingli Ding, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### You Only Look at One Sequence: Rethinking Transformer in Vision through Object Detection.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/dc912a253d1e9ba40e2c597ed2376640-Abstract.html)
- **作者**: Yuxin Fang, Bencheng Liao, Xinggang Wang, Jiemin Fang, Jiyang Qi, Rui Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Instance-Conditional Knowledge Distillation for Object Detection.
- **链接**: [arXiv:2110.12724](https://arxiv.org/abs/2110.12724) · [代码](https://github.com/megvii-research/ICD)
- **作者**: Zijian Kang, Peizhen Zhang, Xiangyu Zhang, Jian Sun, Nanning Zheng
- **🏷️ 机构**: MEGVII, XJTU
- **会议**: NeurIPS 2021

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

- Object DGCNN: 3D Object Detection using Dynamic Graphs. → [3d-detection](../3d-detection/Guideline%202021.md)
- Revisiting 3D Object Detection From an Egocentric Perspective. → [3d-detection](../3d-detection/Guideline%202021.md)
- Progressive Coordinate Transforms for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
