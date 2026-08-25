# Tracking — 2020 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### GNN3DMOT: Graph Neural Network for 3D Multi-Object Tracking With 2D-3D Multi-Feature Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Weng_GNN3DMOT_Graph_Neural_Network_for_3D_Multi-Object_Tracking_With_2D-3D_CVPR_2020_paper.html) · 📚 被引 214
- **作者**: Xinshuo Weng, Yongxin Wang, Yunze Man, Kris M. Kitani
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### A Unified Object Motion and Affinity Model for Online Multi-Object Tracking.
- **链接**: [arXiv:2003.11291](https://arxiv.org/abs/2003.11291) · 📚 被引 105
- **作者**: Junbo Yin, Wenguan Wang, Qinghao Meng, Ruigang Yang, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Current popular online multi-object tracking (MOT) solutions apply single object trackers (SOTs) to capture object motions, while often requiring an extra affinity network to associate objects, especially for the occluded ones. This brings extra computational overhead due to repetitive feature extraction for SOT and affinity computation. Meanwhile, the model size of the sophisticated affinity network is usually non-trivial. In this paper, we propose a novel MOT framework that unifies object motion and affinity model into a single network, named UMA, in order to learn a compact feature that is discriminative for both object motion and affinity measure. In particular, UMA integrates single object tracking and metric learning into a unified triplet network by means of multi-task learning. Such design brings advantages of improved computation efficiency, low memory requirement and simplified training procedure. In addition, we equip our model with a task-specific attention module, which is used to boost task-aware feature learning. The proposed UMA can be easily trained end-to-end, and is elegant - requiring only one training stage. Experimental results show that it achieves promising performance on several MOT Challenge benchmarks.

### Learning a Neural Solver for Multiple Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Braso_Learning_a_Neural_Solver_for_Multiple_Object_Tracking_CVPR_2020_paper.html) · 📚 被引 410
- **作者**: Guillem Brasó, Laura Leal-Taixé
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### SQE: a Self Quality Evaluation Metric for Parameters Optimization in Multi-Object Tracking.
- **链接**: [arXiv:2004.07472](https://arxiv.org/abs/2004.07472) · 📚 被引 7
- **作者**: Yanru Huang, Feiyu Zhu, Zheni Zeng, Xi Qiu, Yuan Shen, Jianan Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > We present a novel self quality evaluation metric SQE for parameters optimization in the challenging yet critical multi-object tracking task. Current evaluation metrics all require annotated ground truth, thus will fail in the test environment and realistic circumstances prohibiting further optimization after training. By contrast, our metric reflects the internal characteristics of trajectory hypotheses and measures tracking performance without ground truth. We demonstrate that trajectories with different qualities exhibit different single or multiple peaks over feature distance distribution, inspiring us to design a simple yet effective method to assess the quality of trajectories using a two-class Gaussian mixture model. Experiments mainly on MOT16 Challenge data sets verify the effectiveness of our method in both correlating with existing metrics and enabling parameters self-optimization to achieve better performance. We believe that our conclusions and method are inspiring for future multi-object tracking in practice.

### Learning Multi-Object Tracking and Segmentation From Automatic Annotations.
- **链接**: [arXiv:1912.02096](https://arxiv.org/abs/1912.02096) · 📚 被引 59
- **作者**: Lorenzo Porzi, Markus Hofinger, Idoia Ruiz, Joan Serrat, Samuel Rota Bulò, Peter Kontschieder
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > In this work we contribute a novel pipeline to automatically generate training data, and to improve over state-of-the-art multi-object tracking and segmentation (MOTS) methods. Our proposed track mining algorithm turns raw street-level videos into high-fidelity MOTS training data, is scalable and overcomes the need of expensive and time-consuming manual annotation approaches. We leverage state-of-the-art instance segmentation results in combination with optical flow predictions, also trained on automatically harvested training data. Our second major contribution is MOTSNet - a deep learning, tracking-by-detection architecture for MOTS - deploying a novel mask-pooling layer for improved object association over time. Training MOTSNet with our automatically extracted data leads to significantly improved sMOTSA scores on the novel KITTI MOTS dataset (+1.9%/+7.5% on cars/pedestrians), and MOTSNet improves by +4.1% over previously best methods on the MOTSChallenge dataset. Our most impressive finding is that we can improve over previous best-performing works, even in complete absence of manually annotated MOTS training data.

### One-Shot Adversarial Attacks on Visual Tracking With Dual Attention.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_One-Shot_Adversarial_Attacks_on_Visual_Tracking_With_Dual_Attention_CVPR_2020_paper.html) · 📚 被引 91
- **作者**: Xuesong Chen, Xiyu Yan, Feng Zheng, Yong Jiang, Shu-Tao Xia, Yong Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Siamese Box Adaptive Network for Visual Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_Siamese_Box_Adaptive_Network_for_Visual_Tracking_CVPR_2020_paper.html) · 📚 被引 914
- **作者**: Zedu Chen, Bineng Zhong, Guorong Li, Shengping Zhang, Rongrong Ji
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Probabilistic Regression for Visual Tracking.
- **链接**: [arXiv:2003.12565](https://arxiv.org/abs/2003.12565) · [代码](https://github.com/visionml/pytracking) · 📚 被引 703
- **作者**: Martin Danelljan, Luc Van Gool, Radu Timofte
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Visual tracking is fundamentally the problem of regressing the state of the target in each video frame. While significant progress has been achieved, trackers are still prone to failures and inaccuracies. It is therefore crucial to represent the uncertainty in the target estimation. Although current prominent paradigms rely on estimating a state-dependent confidence score, this value lacks a clear probabilistic interpretation, complicating its use. In this work, we therefore propose a probabilistic regression formulation and apply it to tracking. Our network predicts the conditional probability density of the target state given an input image. Crucially, our formulation is capable of modeling label noise stemming from inaccurate annotations and ambiguities in the task. The regression network is trained by minimizing the Kullback-Leibler divergence. When applied for tracking, our formulation not only allows a probabilistic representation of the output, but also substantially improves the performance. Our tracker sets a new state-of-the-art on six datasets, achieving 59.8% AUC on LaSOT and 75.8% Success on TrackingNet. The code and models are available at https://github.com/visionml/pytracking.

### Correlation-Guided Attention for Corner Detection Based Visual Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Du_Correlation-Guided_Attention_for_Corner_Detection_Based_Visual_Tracking_CVPR_2020_paper.html) · 📚 被引 143
- **作者**: Fei Du, Peng Liu, Wei Zhao, Xianglong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Recursive Least-Squares Estimator-Aided Online Learning for Visual Tracking.
- **链接**: [arXiv:2112.14016](https://arxiv.org/abs/2112.14016) · 📚 被引 17
- **作者**: Jin Gao, Weiming Hu, Yan Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Tracking visual objects from a single initial exemplar in the testing phase has been broadly cast as a one-/few-shot problem, i.e., one-shot learning for initial adaptation and few-shot learning for online adaptation. The recent few-shot online adaptation methods incorporate the prior knowledge from large amounts of annotated training data via complex meta-learning optimization in the offline phase. This helps the online deep trackers to achieve fast adaptation and reduce overfitting risk in tracking. In this paper, we propose a simple yet effective recursive least-squares estimator-aided online learning approach for few-shot online adaptation without requiring offline training. It allows an in-built memory retention mechanism for the model to remember the knowledge about the object seen before, and thus the seen data can be safely removed from training. This also bears certain similarities to the emerging continual learning field in preventing catastrophic forgetting. This mechanism enables us to unveil the power of modern online deep trackers without incurring too much extra computational cost. We evaluate our approach based on two networks in the online learning families for tracking, i.e., multi-layer perceptrons in RT-MDNet and convolutional neural networks in DiMP. The consistent improvements on several challenging tracking benchmarks demonstrate its effectiveness and efficiency.

### SiamCAR: Siamese Fully Convolutional Classification and Regression for Visual Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Guo_SiamCAR_Siamese_Fully_Convolutional_Classification_and_Regression_for_Visual_Tracking_CVPR_2020_paper.html) · 📚 被引 850
- **作者**: Dongyan Guo, Jun Wang, Ying Cui, Zhenhua Wang, Shengyong Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### AutoTrack: Towards High-Performance Visual Tracking for UAV With Automatic Spatio-Temporal Regularization.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_AutoTrack_Towards_High-Performance_Visual_Tracking_for_UAV_With_Automatic_Spatio-Temporal_CVPR_2020_paper.html) · 📚 被引 398
- **作者**: Yiming Li, Changhong Fu, Fangqiang Ding, Ziyuan Huang, Geng Lu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### RetinaTrack: Online Single Stage Joint Detection and Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Lu_RetinaTrack_Online_Single_Stage_Joint_Detection_and_Tracking_CVPR_2020_paper.html) · 📚 被引 226
- **作者**: Zhichao Lu, Vivek Rathod, Ronny Votel, Jonathan Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Siam R-CNN: Visual Tracking by Re-Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Voigtlaender_Siam_R-CNN_Visual_Tracking_by_Re-Detection_CVPR_2020_paper.html) · 📚 被引 689
- **作者**: Paul Voigtlaender, Jonathon Luiten, Philip H. S. Torr, Bastian Leibe
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
