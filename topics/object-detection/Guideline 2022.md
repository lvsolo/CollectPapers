# Object Detection — 2022 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 19 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Prototypical VoteNet for Few-Shot 3D Point Cloud Object Detection.
- **链接**: [arXiv:2210.05593](https://arxiv.org/abs/2210.05593) · 📚 被引 3
- **作者**: Shizhen Zhao, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing 3D point cloud object detection approaches heavily rely on large amounts of labeled training data. However, the labeling process is costly and time-consuming. This paper considers few-shot 3D point cloud object detection, where only a few annotated samples of novel classes are needed with abundant samples of base classes. To this end, we propose Prototypical VoteNet to recognize and localize novel instances, which incorporates two new modules: Prototypical Vote Module (PVM) and Prototypical Head Module (PHM). Specifically, as the 3D basic geometric structures can be shared among categories, PVM is designed to leverage class-agnostic geometric prototypes, which are learned from base classes, to refine local features of novel categories.Then PHM is proposed to utilize class prototypes to enhance the global feature of each object, facilitating subsequent object localization and classification, which is trained by the episodic training strategy. To evaluate the model in this new setting, we contribute two new benchmark datasets, FS-ScanNet and FS-SUNRGBD. We conduct extensive experiments to demonstrate the effectiveness of Prototypical VoteNet, and our proposed method shows significant and consistent improvements compared to baselines on two benchmark datasets.

</details>

### Unsupervised Object Detection Pretraining with Joint Object Priors Generation and Detector Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/50ca96a1a9ebe0b5e5688a504feb6107-Abstract-Conference.html)
- **作者**: Yizhou Wang, Meilin Chen, Shixiang Tang, Feng Zhu, Haiyang Yang, Lei Bai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Decoupling Classifier for Boosting Few-shot Object Detection and Instance Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/764ba7236fb63743014fafbd87dd4f0e-Abstract-Conference.html)
- **作者**: Bin-Bin Gao, Xiaochen Chen, Zhongyi Huang, Congchong Nie, Jun Liu, Jinxiang Lai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### DTG-SSOD: Dense Teacher Guidance for Semi-Supervised Object Detection.
- **链接**: [arXiv:2207.05536](https://arxiv.org/abs/2207.05536) · 📚 被引 1
- **作者**: Gang Li, Xiang Li, Yujie Wang, Yichao Wu, Ding Liang, Shanshan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Mean-Teacher (MT) scheme is widely adopted in semi-supervised object detection (SSOD). In MT, the sparse pseudo labels, offered by the final predictions of the teacher (e.g., after Non Maximum Suppression (NMS) post-processing), are adopted for the dense supervision for the student via hand-crafted label assignment. However, the sparse-to-dense paradigm complicates the pipeline of SSOD, and simultaneously neglects the powerful direct, dense teacher supervision. In this paper, we attempt to directly leverage the dense guidance of teacher to supervise student training, i.e., the dense-to-dense paradigm. Specifically, we propose the Inverse NMS Clustering (INC) and Rank Matching (RM) to instantiate the dense supervision, without the widely used, conventional sparse pseudo labels. INC leads the student to group candidate boxes into clusters in NMS as the teacher does, which is implemented by learning grouping information revealed in NMS procedure of the teacher. After obtaining the same grouping scheme as the teacher via INC, the student further imitates the rank distribution of the teacher over clustered candidates through Rank Matching. With the proposed INC and RM, we integrate Dense Teacher Guidance into Semi-Supervised Object Detection (termed DTG-SSOD), successfully abandoning sparse pseudo labels and enabling more informative learning on unlabeled data. On COCO benchmark, our DTG-SSOD achieves state-of-the-art performance under various labelling ratios. For example, under 10% labelling ratio, DTG-SSOD improves the supervised baseline from 26.9 to 35.9 mAP, outperforming the previous best method Soft Teacher by 1.9 points.

</details>

### Towards Improving Calibration in Object Detection Under Domain Shift.
- **链接**: [arXiv:2209.07601](https://arxiv.org/abs/2209.07601)
- **作者**: Muhammad Akhtar Munir, Muhammad Haris Khan, M. Saquib Sarfraz, Mohsen Ali
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With deep neural network based solution more readily being incorporated in real-world applications, it has been pressing requirement that predictions by such models, especially in safety-critical environments, be highly accurate and well-calibrated. Although some techniques addressing DNN calibration have been proposed, they are only limited to visual classification applications and in-domain predictions. Unfortunately, very little to no attention is paid towards addressing calibration of DNN-based visual object detectors, that occupy similar space and importance in many decision making systems as their visual classification counterparts. In this work, we study the calibration of DNN-based object detection models, particularly under domain shift. To this end, we first propose a new, plug-and-play, train-time calibration loss for object detection (coined as TCD). It can be used with various application-specific loss functions as an auxiliary loss function to improve detection calibration. Second, we devise a new implicit technique for improving calibration in self-training based domain adaptive detectors, featuring a new uncertainty quantification mechanism for object detection. We demonstrate TCD is capable of enhancing calibration with notable margins (1) across different DNN-based object detection paradigms both in in-domain and out-of-domain predictions, and (2) in different domain-adaptive detectors across challenging adaptation scenarios. Finally, we empirically show that our implicit calibration technique can be used in tandem with TCD during adaptation to further boost calibration in diverse domain shift scenarios.

</details>

### Semi-Supervised Video Salient Object Detection Based on Uncertainty-Guided Pseudo Labels.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/24f7b98aef14fcd68acf3c941af1b59e-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yongri Piao, Chenyang Lu, Miao Zhang, Huchuan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Structural Knowledge Distillation for Object Detection.
- **链接**: [arXiv:2211.13133](https://arxiv.org/abs/2211.13133) · 📚 被引 3
- **作者**: Philip de Rijk, Lukas Schneider, Marius Cordts, Dariu Gavrila
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge Distillation (KD) is a well-known training paradigm in deep neural networks where knowledge acquired by a large teacher model is transferred to a small student. KD has proven to be an effective technique to significantly improve the student's performance for various tasks including object detection. As such, KD techniques mostly rely on guidance at the intermediate feature level, which is typically implemented by minimizing an lp-norm distance between teacher and student activations during training. In this paper, we propose a replacement for the pixel-wise independent lp-norm based on the structural similarity (SSIM). By taking into account additional contrast and structural cues, feature importance, correlation and spatial dependence in the feature space are considered in the loss formulation. Extensive experiments on MSCOCO demonstrate the effectiveness of our method across different training schemes and architectures. Our method adds only little computational overhead, is straightforward to implement and at the same time it significantly outperforms the standard lp-norms. Moreover, more complex state-of-the-art KD methods using attention-based sampling mechanisms are outperformed, including a +3.5 AP gain using a Faster R-CNN R-50 compared to a vanilla model.

</details>

### Rethinking Image Restoration for Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/1cac8326ce3fbe79171db9754211530c-Abstract-Conference.html)
- **作者**: Shangquan Sun, Wenqi Ren, Tao Wang, Xiaochun Cao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- Sparse2Dense: Learning to Densify 3D Features for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- MsSVT: Mixed-scale Sparse Voxel Transformer for 3D Object Detection on Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- Fully Sparse 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Unifying Voxel-based Representation with Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Spatial Pruned Sparse Convolution for Efficient 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- K-Radar: 4D Radar Object Detection for Autonomous Driving in Various Weather Conditions. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- Fully Convolutional One-Stage 3D Object Detection on LiDAR Range Images. → [3d-detection](../3d-detection/Guideline%202022.md)
- CAGroup3D: Class-Aware Grouping for 3D Object Detection on Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- DeepInteraction: 3D Object Detection via Modality Interaction. → [3d-detection](../3d-detection/Guideline%202022.md)
- Towards Efficient 3D Object Detection with Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202022.md)
- MoGDE: Boosting Mobile Monocular 3D Object Detection with Ground Depth Estimation. → [3d-detection](../3d-detection/Guideline%202022.md)
