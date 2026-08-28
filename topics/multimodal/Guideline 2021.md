# Multimodal — 2021 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### There Is More Than Meets the Eye: Self-Supervised Multi-Object Detection and Tracking With Sound by Distilling Multimodal Knowledge.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Valverde_There_Is_More_Than_Meets_the_Eye_Self-Supervised_Multi-Object_Detection_CVPR_2021_paper.html) · 📚 被引 73
- **作者**: Francisco Rivera Valverde, Juana Valeria Hurtado, Abhinav Valada
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Robust Multimodal Vehicle Detection in Foggy Weather Using Complementary Lidar and Radar Signals.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Qian_Robust_Multimodal_Vehicle_Detection_in_Foggy_Weather_Using_Complementary_Lidar_CVPR_2021_paper.html) · 📚 被引 183
- **作者**: Kun Qian, Shilin Zhu, Xinyu Zhang, Li Erran Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### UC2: Universal Cross-Lingual Cross-Modal Vision-and-Language Pre-Training.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_UC2_Universal_Cross-Lingual_Cross-Modal_Vision-and-Language_Pre-Training_CVPR_2021_paper.html)
- **作者**: Mingyang Zhou, Luowei Zhou, Shuohang Wang, Yu Cheng, Linjie Li, Zhou Yu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Progressive Modality Reinforcement for Human Multimodal Emotion Recognition From Unaligned Multimodal Sequences.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Progressive_Modality_Reinforcement_for_Human_Multimodal_Emotion_Recognition_From_Unaligned_CVPR_2021_paper.html) · 📚 被引 191
- **作者**: Fengmao Lv, Xiang Chen, Yanyong Huang, Lixin Duan, Guosheng Lin
- **🏷️ 机构**: Southwest Jiaotong University, Platform and Content Group,Tencent, Southwestern University of Finance and Economics,Center of Statistical Research
- **会议**: CVPR 2021

### Revamping Cross-Modal Recipe Retrieval With Hierarchical Transformers and Self-Supervised Learning.
- **链接**: [arXiv:2103.13061](https://arxiv.org/abs/2103.13061) · 📚 被引 74
- **作者**: Amaia Salvador, Erhan Gundogdu, Loris Bazzani, Michael Donoser
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-modal recipe retrieval has recently gained substantial attention due to the importance of food in people's lives, as well as the availability of vast amounts of digital cooking recipes and food images to train machine learning models. In this work, we revisit existing approaches for cross-modal recipe retrieval and propose a simplified end-to-end model based on well established and high performing encoders for text and images. We introduce a hierarchical recipe Transformer which attentively encodes individual recipe components (titles, ingredients and instructions). Further, we propose a self-supervised loss function computed on top of pairs of individual recipe components, which is able to leverage semantic relationships within recipes, and enables training using both image-recipe and recipe-only samples. We conduct a thorough analysis and ablation studies to validate our design choices. As a result, our proposed method achieves state-of-the-art performance in the cross-modal recipe retrieval task on the Recipe1M dataset. We make code and models publicly available.

</details>

### Cross-Modal Contrastive Learning for Text-to-Image Generation.
- **链接**: [arXiv:2101.04702](https://arxiv.org/abs/2101.04702) · 📚 被引 293
- **作者**: Han Zhang, Jing Yu Koh, Jason Baldridge, Honglak Lee, Yinfei Yang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The output of text-to-image synthesis systems should be coherent, clear, photo-realistic scenes with high semantic fidelity to their conditioned text descriptions. Our Cross-Modal Contrastive Generative Adversarial Network (XMC-GAN) addresses this challenge by maximizing the mutual information between image and text. It does this via multiple contrastive losses which capture inter-modality and intra-modality correspondences. XMC-GAN uses an attentional self-modulation generator, which enforces strong text-image correspondence, and a contrastive discriminator, which acts as a critic as well as a feature encoder for contrastive learning. The quality of XMC-GAN's output is a major step up from previous models, as we show on three challenging datasets. On MS-COCO, not only does XMC-GAN improve state-of-the-art FID from 24.70 to 9.33, but--more importantly--people prefer XMC-GAN by 77.3 for image quality and 74.1 for image-text alignment, compared to three other recent models. XMC-GAN also generalizes to the challenging Localized Narratives dataset (which has longer, more detailed descriptions), improving state-of-the-art FID from 48.70 to 14.12. Lastly, we train and evaluate XMC-GAN on the challenging Open Images data, establishing a strong benchmark FID score of 26.91.

</details>

### Distilling Audio-Visual Knowledge by Compositional Contrastive Learning.
- **链接**: [arXiv:2104.10955](https://arxiv.org/abs/2104.10955) · [代码](https://github.com/yanbeic/CCL) · 📚 被引 65
- **作者**: Yanbei Chen, Yongqin Xian, A. Sophia Koepke, Ying Shan, Zeynep Akata
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Having access to multi-modal cues (e.g. vision and audio) empowers some cognitive tasks to be done faster compared to learning from a single modality. In this work, we propose to transfer knowledge across heterogeneous modalities, even though these data modalities may not be semantically correlated. Rather than directly aligning the representations of different modalities, we compose audio, image, and video representations across modalities to uncover richer multi-modal knowledge. Our main idea is to learn a compositional embedding that closes the cross-modal semantic gap and captures the task-relevant semantics, which facilitates pulling together representations across modalities by compositional contrastive learning. We establish a new, comprehensive multi-modal distillation benchmark on three video datasets: UCF101, ActivityNet, and VGGSound. Moreover, we demonstrate that our model significantly outperforms a variety of existing knowledge distillation methods in transferring audio-visual knowledge to improve video representation learning. Code is released here: https://github.com/yanbeic/CCL.

</details>

### Multimodal Contrastive Training for Visual Representation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yuan_Multimodal_Contrastive_Training_for_Visual_Representation_Learning_CVPR_2021_paper.html)
- **作者**: Xin Yuan, Zhe Lin, Jason Kuen, Jianming Zhang, Yilin Wang, Michael Maire et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### EvDistill: Asynchronous Events To End-Task Learning via Bidirectional Reconstruction-Guided Cross-Modal Knowledge Distillation.
- **链接**: [arXiv:2111.12341](https://arxiv.org/abs/2111.12341) · 📚 被引 76
- **作者**: Lin Wang, Yujeong Chae, Sung-Hoon Yoon, Tae-Kyun Kim, Kuk-Jin Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Event cameras sense per-pixel intensity changes and produce asynchronous event streams with high dynamic range and less motion blur, showing advantages over conventional cameras. A hurdle of training event-based models is the lack of large qualitative labeled data. Prior works learning end-tasks mostly rely on labeled or pseudo-labeled datasets obtained from the active pixel sensor (APS) frames; however, such datasets' quality is far from rivaling those based on the canonical images. In this paper, we propose a novel approach, called \textbf{EvDistill}, to learn a student network on the unlabeled and unpaired event data (target modality) via knowledge distillation (KD) from a teacher network trained with large-scale, labeled image data (source modality). To enable KD across the unpaired modalities, we first propose a bidirectional modality reconstruction (BMR) module to bridge both modalities and simultaneously exploit them to distill knowledge via the crafted pairs, causing no extra computation in the inference. The BMR is improved by the end-tasks and KD losses in an end-to-end manner. Second, we leverage the structural similarities of both modalities and adapt the knowledge by matching their distributions. Moreover, as most prior feature KD methods are uni-modality and less applicable to our problem, we propose to leverage an affinity graph KD loss to boost the distillation. Our extensive experiments on semantic segmentation and object recognition demonstrate that EvDistill achieves significantly better results than the prior works and KD with only events and APS frames.

</details>

## 跨领域论文（完整笔记在其他领域）

- PointAugmenting: Cross-Modal Augmentation for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202021.md)
- Shared Cross-Modal Trajectory Prediction for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
- Multi-Modal Fusion Transformer for End-to-End Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
