# Multimodal — 2022 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-supervised object detection from audio-visual correspondence.
- **链接**: [arXiv:2104.06401](https://arxiv.org/abs/2104.06401) · 📚 被引 40
- **作者**: Triantafyllos Afouras, Yuki M. Asano, Francois Fagan, Andrea Vedaldi, Florian Metze
- **🏷️ 机构**: University of Oxford, University of Amsterdam, Meta AI
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the problem of learning object detectors without supervision. Differently from weakly-supervised object detection, we do not assume image-level class labels. Instead, we extract a supervisory signal from audio-visual data, using the audio component to "teach" the object detector. While this problem is related to sound source localisation, it is considerably harder because the detector must classify the objects by type, enumerate each instance of the object, and do so even when the object is silent. We tackle this problem by first designing a self-supervised framework with a contrastive objective that jointly learns to classify and localise objects. Then, without using any supervision, we simply use these self-supervised labels and boxes to train an image-based object detector. With this, we outperform previous unsupervised and weakly-supervised detectors for the task of object detection and sound source localization. We also show that we can align this detector to ground-truth classes with as little as one label per pseudo-class, and show how our method can learn to detect generic objects that go beyond instruments, such as airplanes and cats.

</details>

### CrossPoint: Self-Supervised Cross-Modal Contrastive Learning for 3D Point Cloud Understanding.
- **链接**: [arXiv:2203.00680](https://arxiv.org/abs/2203.00680) · [代码](https://github.com/MohamedAfham/CrossPoint) · 📚 被引 274
- **作者**: Mohamed Afham, Isuru Dissanayake, Dinithi Dissanayake, Amaya Dharmasiri, Kanchana Thilakarathna, Ranga Rodrigo
- **🏷️ 机构**: Univeristy of Moratuwa,Dept. of Electronic and Telecommunication Engineering,Sri Lanka, The University of Sydney
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Manual annotation of large-scale point cloud dataset for varying tasks such as 3D object classification, segmentation and detection is often laborious owing to the irregular structure of point clouds. Self-supervised learning, which operates without any human labeling, is a promising approach to address this issue. We observe in the real world that humans are capable of mapping the visual concepts learnt from 2D images to understand the 3D world. Encouraged by this insight, we propose CrossPoint, a simple cross-modal contrastive learning approach to learn transferable 3D point cloud representations. It enables a 3D-2D correspondence of objects by maximizing agreement between point clouds and the corresponding rendered 2D image in the invariant space, while encouraging invariance to transformations in the point cloud modality. Our joint training objective combines the feature correspondences within and across modalities, thus ensembles a rich learning signal from both 3D point cloud and 2D image modalities in a self-supervised fashion. Experimental results show that our approach outperforms the previous unsupervised learning methods on a diverse range of downstream tasks including 3D object classification and segmentation. Further, the ablation studies validate the potency of our approach for a better point cloud understanding. Code and pretrained models are available at http://github.com/MohamedAfham/CrossPoint.

</details>

### Text2Pos: Text-to-Point-Cloud Cross-Modal Localization.
- **链接**: [arXiv:2203.15125](https://arxiv.org/abs/2203.15125) · 📚 被引 26
- **作者**: Manuel Kolmet, Qunjie Zhou, Aljosa Osep, Laura Leal-Taixé
- **🏷️ 机构**: Technical University of Munich,Germany
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Natural language-based communication with mobile devices and home appliances is becoming increasingly popular and has the potential to become natural for communicating with mobile robots in the future. Towards this goal, we investigate cross-modal text-to-point-cloud localization that will allow us to specify, for example, a vehicle pick-up or goods delivery location. In particular, we propose Text2Pos, a cross-modal localization module that learns to align textual descriptions with localization cues in a coarse- to-fine manner. Given a point cloud of the environment, Text2Pos locates a position that is specified via a natural language-based description of the immediate surroundings. To train Text2Pos and study its performance, we construct KITTI360Pose, the first dataset for this task based on the recently introduced KITTI360 dataset. Our experiments show that we can localize 65% of textual queries within 15m distance to query locations for top-10 retrieved locations. This is a starting point that we hope will spark future developments towards language-based navigation.

</details>

### Multimodal Colored Point Cloud to Image Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00654) · 📚 被引 4
- **作者**: Noam Rotstein, Amit Bracha, Ron Kimmel
- **🏷️ 机构**: Technion - Israel Institute of Technology
- **会议**: CVPR 2022

### Learnable Irrelevant Modality Dropout for Multimodal Action Recognition on Modality-Specific Annotated Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01957) · 📚 被引 30
- **作者**: Saghir Alfasly, Jian Lu, Chen Xu, Yuru Zou
- **🏷️ 机构**: Shenzhen University,Shenzhen Key Laboratory of Advanced Machine Learning and Applications,China
- **会议**: CVPR 2022

### Interact before Align: Leveraging Cross-Modal Knowledge for Domain Adaptive Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01431) · 📚 被引 32
- **作者**: Lijin Yang, Yifei Huang, Yusuke Sugano, Yoichi Sato
- **🏷️ 机构**: Institute of Industrial Science, The University of Tokyo
- **会议**: CVPR 2022

### Robust Cross-Modal Representation Learning with Progressive Self-Distillation.
- **链接**: [arXiv:2204.04588](https://arxiv.org/abs/2204.04588) · 📚 被引 46
- **作者**: Alex Andonian, Shixing Chen, Raffay Hamid
- **🏷️ 机构**: MIT CSAIL, Amazon Prime Video
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The learning objective of vision-language approach of CLIP does not effectively account for the noisy many-to-many correspondences found in web-harvested image captioning datasets, which contributes to its compute and data inefficiency. To address this challenge, we introduce a novel training framework based on cross-modal contrastive learning that uses progressive self-distillation and soft image-text alignments to more efficiently learn robust representations from noisy data. Our model distills its own knowledge to dynamically generate soft-alignment targets for a subset of images and captions in every minibatch, which are then used to update its parameters. Extensive evaluation across 14 benchmark datasets shows that our method consistently outperforms its CLIP counterpart in multiple settings, including: (a) zero-shot classification, (b) linear probe transfer, and (c) image-text retrieval, without incurring added computational cost. Analysis using an ImageNet-based robustness test-bed reveals that our method offers better effective robustness to natural distribution shifts compared to both ImageNet-trained models and CLIP itself. Lastly, pretraining with datasets spanning two orders of magnitude in size shows that our improvements over CLIP tend to scale with number of training examples.

</details>

## 跨领域论文（完整笔记在其他领域）

- DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
