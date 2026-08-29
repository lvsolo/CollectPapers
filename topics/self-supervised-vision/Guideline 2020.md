# Self-supervised Vision — 2020 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-supervised Keypoint Correspondences for Multi-person Pose Estimation and Tracking in Videos.
- **链接**: [arXiv:2004.12652](https://arxiv.org/abs/2004.12652) · 📚 被引 35
- **作者**: Umer Rafi, Andreas Doering, Bastian Leibe, Juergen Gall
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video annotation is expensive and time consuming. Consequently, datasets for multi-person pose estimation and tracking are less diverse and have more sparse annotations compared to large scale image datasets for human pose estimation. This makes it challenging to learn deep learning based models for associating keypoints across frames that are robust to nuisance factors such as motion blur and occlusions for the task of multi-person pose tracking. To address this issue, we propose an approach that relies on keypoint correspondences for associating persons in videos. Instead of training the network for estimating keypoint correspondences on video data, it is trained on a large scale image datasets for human pose estimation using self-supervision. Combined with a top-down framework for human pose estimation, we use keypoints correspondences to (i) recover missed pose detections (ii) associate pose detections across video frames. Our approach achieves state-of-the-art results for multi-frame pose estimation and multi-person pose tracking on the PosTrack $2017$ and PoseTrack $2018$ data sets.

</details>

### Info3D: Representation Learning on 3D Objects Using Mutual Information Maximization and Contrastive Learning.
- **链接**: [arXiv:2006.02598](https://arxiv.org/abs/2006.02598) · 📚 被引 74
- **作者**: Aditya Sanghi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A major endeavor of computer vision is to represent, understand and extract structure from 3D data. Towards this goal, unsupervised learning is a powerful and necessary tool. Most current unsupervised methods for 3D shape analysis use datasets that are aligned, require objects to be reconstructed and suffer from deteriorated performance on downstream tasks. To solve these issues, we propose to extend the InfoMax and contrastive learning principles on 3D shapes. We show that we can maximize the mutual information between 3D objects and their "chunks" to improve the representations in aligned datasets. Furthermore, we can achieve rotation invariance in SO${(3)}$ group by maximizing the mutual information between the 3D objects and their geometric transformed versions. Finally, we conduct several experiments such as clustering, transfer learning, shape retrieval, and achieve state of art results.

</details>

### Contrastive Learning for Weakly Supervised Phrase Grounding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58580-8_44)
- **作者**: Tanmay Gupta, Arash Vahdat, Gal Chechik, Xiaodong Yang, Jan Kautz, Derek Hoiem
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Contrastive Learning for Unpaired Image-to-Image Translation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58545-7_19) · 📚 被引 0
- **作者**: Taesung Park, Alexei A. Efros, Richard Zhang, Jun-Yan Zhu
- **🏷️ 机构**: UC Berkeley, CMU
- **会议**: ECCV 2020

### Adversarial Self-supervised Learning for Semi-supervised 3D Action Recognition.
- **链接**: [arXiv:2007.05934](https://arxiv.org/abs/2007.05934) · 📚 被引 55
- **作者**: Chenyang Si, Xuecheng Nie, Wei Wang, Liang Wang, Tieniu Tan, Jiashi Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of semi-supervised 3D action recognition which has been rarely explored before. Its major challenge lies in how to effectively learn motion representations from unlabeled data. Self-supervised learning (SSL) has been proved very effective at learning representations from unlabeled data in the image domain. However, few effective self-supervised approaches exist for 3D action recognition, and directly applying SSL for semi-supervised learning suffers from misalignment of representations learned from SSL and supervised learning tasks. To address these issues, we present Adversarial Self-Supervised Learning (ASSL), a novel framework that tightly couples SSL and the semi-supervised scheme via neighbor relation exploration and adversarial learning. Specifically, we design an effective SSL scheme to improve the discrimination capability of learned representations for 3D action recognition, through exploring the data relations within a neighborhood. We further propose an adversarial regularization to align the feature distributions of labeled and unlabeled samples. To demonstrate effectiveness of the proposed ASSL in semi-supervised 3D action recognition, we conduct extensive experiments on NTU and N-UCLA datasets. The results confirm its advantageous performance over state-of-the-art semi-supervised methods in the few label regime for 3D action recognition.

</details>

### Reversing the Cycle: Self-supervised Deep Stereo Through Enhanced Monocular Distillation.
- **链接**: [arXiv:2008.07130](https://arxiv.org/abs/2008.07130) · [代码](https://github.com/FilippoAleotti/Reversing) · 📚 被引 32
- **作者**: Filippo Aleotti, Fabio Tosi, Li Zhang, Matteo Poggi, Stefano Mattoccia
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In many fields, self-supervised learning solutions are rapidly evolving and filling the gap with supervised approaches. This fact occurs for depth estimation based on either monocular or stereo, with the latter often providing a valid source of self-supervision for the former. In contrast, to soften typical stereo artefacts, we propose a novel self-supervised paradigm reversing the link between the two. Purposely, in order to train deep stereo networks, we distill knowledge through a monocular completion network. This architecture exploits single-image clues and few sparse points, sourced by traditional stereo algorithms, to estimate dense yet accurate disparity maps by means of a consensus mechanism over multiple estimations. We thoroughly evaluate with popular stereo datasets the impact of different supervisory signals showing how stereo networks trained with our paradigm outperform existing self-supervised frameworks. Finally, our proposal achieves notable generalization capabilities dealing with domain shift issues. Code available at https://github.com/FilippoAleotti/Reversing

</details>

## 跨领域论文（完整笔记在其他领域）

- Monocular Differentiable Rendering for Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Improving Object Detection with Selective Self-supervised Self-training. → [object-detection](../object-detection/Guideline%202020.md)
- Self-Supervised Monocular 3D Face Reconstruction by Occlusion-Aware Multi-view Geometry Consistency. → [3d-detection](../3d-detection/Guideline%202020.md)
- S3Net: Semantic-Aware Self-supervised Depth Estimation with Monocular Videos and Synthetic Data. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Self-supervised Monocular Depth Estimation: Solving the Dynamic Object Problem by Semantic Guidance. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
