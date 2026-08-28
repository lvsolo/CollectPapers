# Self-supervised Vision — 2021 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 60 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Point-Flow: Self-Supervised Scene Flow Estimation From Point Clouds With Optimal Transport and Random Walk.
- **链接**: [arXiv:2105.08248](https://arxiv.org/abs/2105.08248) · 📚 被引 45
- **作者**: Ruibo Li, Guosheng Lin, Lihua Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the scarcity of annotated scene flow data, self-supervised scene flow learning in point clouds has attracted increasing attention. In the self-supervised manner, establishing correspondences between two point clouds to approximate scene flow is an effective approach. Previous methods often obtain correspondences by applying point-wise matching that only takes the distance on 3D point coordinates into account, introducing two critical issues: (1) it overlooks other discriminative measures, such as color and surface normal, which often bring fruitful clues for accurate matching; and (2) it often generates sub-par performance, as the matching is operated in an unconstrained situation, where multiple points can be ended up with the same corresponding point. To address the issues, we formulate this matching task as an optimal transport problem. The output optimal assignment matrix can be utilized to guide the generation of pseudo ground truth. In this optimal transport, we design the transport cost by considering multiple descriptors and encourage one-to-one matching by mass equality constraints. Also, constructing a graph on the points, a random walk module is introduced to encourage the local consistency of the pseudo labels. Comprehensive experiments on FlyingThings3D and KITTI show that our method achieves state-of-the-art performance among self-supervised learning methods. Our self-supervised method even performs on par with some supervised learning approaches, although we do not need any ground truth flow for training.

</details>

### Self-Supervised Learning on 3D Point Clouds by Learning Discrete Generative Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Eckart_Self-Supervised_Learning_on_3D_Point_Clouds_by_Learning_Discrete_Generative_CVPR_2021_paper.html) · 📚 被引 54
- **作者**: Benjamin Eckart, Wentao Yuan, Chao Liu, Jan Kautz
- **🏷️ 机构**: NVIDIA, University of Washington
- **会议**: CVPR 2021

### The Temporal Opportunist: Self-Supervised Multi-Frame Monocular Depth.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Watson_The_Temporal_Opportunist_Self-Supervised_Multi-Frame_Monocular_Depth_CVPR_2021_paper.html) · 📚 被引 316
- **作者**: Jamie Watson, Oisin Mac Aodha, Victor Prisacariu, Gabriel J. Brostow, Michael Firman
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### STaR: Self-Supervised Tracking and Reconstruction of Rigid Objects in Motion With Neural Rendering.
- **链接**: [arXiv:2101.01602](https://arxiv.org/abs/2101.01602) · 📚 被引 61
- **作者**: Wentao Yuan, Zhaoyang Lv, Tanner Schmidt, Steven Lovegrove
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present STaR, a novel method that performs Self-supervised Tracking and Reconstruction of dynamic scenes with rigid motion from multi-view RGB videos without any manual annotation. Recent work has shown that neural networks are surprisingly effective at the task of compressing many views of a scene into a learned function which maps from a viewing ray to an observed radiance value via volume rendering. Unfortunately, these methods lose all their predictive power once any object in the scene has moved. In this work, we explicitly model rigid motion of objects in the context of neural representations of radiance fields. We show that without any additional human specified supervision, we can reconstruct a dynamic scene with a single rigid object in motion by simultaneously decomposing it into its two constituent parts and encoding each with its own neural representation. We achieve this by jointly optimizing the parameters of two neural radiance fields and a set of rigid poses which align the two fields at each frame. On both synthetic and real world datasets, we demonstrate that our method can render photorealistic novel views, where novelty is measured on both spatial and temporal axes. Our factored representation furthermore enables animation of unseen object motion.

</details>

### SelfSAGCN: Self-Supervised Semantic Alignment for Graph Convolution Network.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_SelfSAGCN_Self-Supervised_Semantic_Alignment_for_Graph_Convolution_Network_CVPR_2021_paper.html) · 📚 被引 26
- **作者**: Xu Yang, Cheng Deng, Zhiyuan Dang, Kun Wei, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Exponential Moving Average Normalization for Self-Supervised and Semi-Supervised Learning.
- **链接**: [arXiv:2101.08482](https://arxiv.org/abs/2101.08482) · [代码](https://github.com/amazon-research/exponential-moving-average-normalization) · 📚 被引 112
- **作者**: Zhaowei Cai, Avinash Ravichandran, Subhransu Maji, Charless C. Fowlkes, Zhuowen Tu, Stefano Soatto
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a plug-in replacement for batch normalization (BN) called exponential moving average normalization (EMAN), which improves the performance of existing student-teacher based self- and semi-supervised learning techniques. Unlike the standard BN, where the statistics are computed within each batch, EMAN, used in the teacher, updates its statistics by exponential moving average from the BN statistics of the student. This design reduces the intrinsic cross-sample dependency of BN and enhances the generalization of the teacher. EMAN improves strong baselines for self-supervised learning by 4-6/1-2 points and semi-supervised learning by about 7/2 points, when 1%/10% supervised labels are available on ImageNet. These improvements are consistent across methods, network architectures, training duration, and datasets, demonstrating the general effectiveness of this technique. The code is available at https://github.com/amazon-research/exponential-moving-average-normalization.

</details>

### The Lottery Tickets Hypothesis for Supervised and Self-Supervised Pre-Training in Computer Vision Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_The_Lottery_Tickets_Hypothesis_for_Supervised_and_Self-Supervised_Pre-Training_in_CVPR_2021_paper.html) · 📚 被引 46
- **作者**: Tianlong Chen, Jonathan Frankle, Shiyu Chang, Sijia Liu, Yang Zhang, Michael Carbin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### SelfDoc: Self-Supervised Document Representation Learning.
- **链接**: [arXiv:2106.03331](https://arxiv.org/abs/2106.03331) · 📚 被引 115
- **作者**: Peizhao Li, Jiuxiang Gu, Jason Kuen, Vlad I. Morariu, Handong Zhao, Rajiv Jain et al.
- **🏷️ 机构**: Brandeis University, Adobe Research
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose SelfDoc, a task-agnostic pre-training framework for document image understanding. Because documents are multimodal and are intended for sequential reading, our framework exploits the positional, textual, and visual information of every semantically meaningful component in a document, and it models the contextualization between each block of content. Unlike existing document pre-training models, our model is coarse-grained instead of treating individual words as input, therefore avoiding an overly fine-grained with excessive contextualization. Beyond that, we introduce cross-modal learning in the model pre-training phase to fully leverage multimodal information from unlabeled documents. For downstream usage, we propose a novel modality-adaptive attention mechanism for multimodal feature fusion by adaptively emphasizing language and vision signals. Our framework benefits from self-supervised pre-training on documents without requiring annotations by a feature masking training strategy. It achieves superior performance on multiple downstream tasks with significantly fewer document images used in the pre-training stage compared to previous works.

</details>

### SelfAugment: Automatic Augmentation Policies for Self-Supervised Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Reed_SelfAugment_Automatic_Augmentation_Policies_for_Self-Supervised_Learning_CVPR_2021_paper.html) · 📚 被引 25
- **作者**: Colorado J. Reed, Sean Metzger, Aravind Srinivas, Trevor Darrell, Kurt Keutzer
- **🏷️ 机构**: UC Berkeley
- **会议**: CVPR 2021

### Self-Supervised Wasserstein Pseudo-Labeling for Semi-Supervised Image Classification.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Taherkhani_Self-Supervised_Wasserstein_Pseudo-Labeling_for_Semi-Supervised_Image_Classification_CVPR_2021_paper.html) · 📚 被引 31
- **作者**: Fariborz Taherkhani, Ali Dabouei, Sobhan Soleymani, Jeremy M. Dawson, Nasser M. Nasrabadi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Self-Supervised Learning for Semi-Supervised Temporal Action Proposal.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Self-Supervised_Learning_for_Semi-Supervised_Temporal_Action_Proposal_CVPR_2021_paper.html) · 📚 被引 62
- **作者**: Xiang Wang, Shiwei Zhang, Zhiwu Qing, Yuanjie Shao, Changxin Gao, Nong Sang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Self-Supervised Geometric Perception.
- **链接**: [arXiv:2103.03114](https://arxiv.org/abs/2103.03114)
- **作者**: Heng Yang, Wei Dong, Luca Carlone, Vladlen Koltun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present self-supervised geometric perception (SGP), the first general framework to learn a feature descriptor for correspondence matching without any ground-truth geometric model labels (e.g., camera poses, rigid transformations). Our first contribution is to formulate geometric perception as an optimization problem that jointly optimizes the feature descriptor and the geometric models given a large corpus of visual measurements (e.g., images, point clouds). Under this optimization formulation, we show that two important streams of research in vision, namely robust model fitting and deep feature learning, correspond to optimizing one block of the unknown variables while fixing the other block. This analysis naturally leads to our second contribution -- the SGP algorithm that performs alternating minimization to solve the joint optimization. SGP iteratively executes two meta-algorithms: a teacher that performs robust model fitting given learned features to generate geometric pseudo-labels, and a student that performs deep feature learning under noisy supervision of the pseudo-labels. As a third contribution, we apply SGP to two perception problems on large-scale real datasets, namely relative camera pose estimation on MegaDepth and point cloud registration on 3DMatch. We demonstrate that SGP achieves state-of-the-art performance that is on-par or superior to the supervised oracles trained using ground-truth labels.

</details>

### Self-Supervised Simultaneous Multi-Step Prediction of Road Dynamics and Cost Map.
- **链接**: [arXiv:2103.01039](https://arxiv.org/abs/2103.01039) · 📚 被引 2
- **作者**: Elmira Amirloo Abolfathi, Mohsen Rohani, Ershad Banijamali, Jun Luo, Pascal Poupart
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While supervised learning is widely used for perception modules in conventional autonomous driving solutions, scalability is hindered by the huge amount of data labeling needed. In contrast, while end-to-end architectures do not require labeled data and are potentially more scalable, interpretability is sacrificed. We introduce a novel architecture that is trained in a fully self-supervised fashion for simultaneous multi-step prediction of space-time cost map and road dynamics. Our solution replaces the manually designed cost function for motion planning with a learned high dimensional cost map that is naturally interpretable and allows diverse contextual information to be integrated without manual data labeling. Experiments on real world driving data show that our solution leads to lower number of collisions and road violations in long planning horizons in comparison to baselines, demonstrating the feasibility of fully self-supervised prediction without sacrificing either scalability or interpretability.

</details>

### Self-Supervised Augmentation Consistency for Adapting Semantic Segmentation.
- **链接**: [arXiv:2105.00097](https://arxiv.org/abs/2105.00097) · 📚 被引 227
- **作者**: Nikita Araslanov, Stefan Roth
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose an approach to domain adaptation for semantic segmentation that is both practical and highly accurate. In contrast to previous work, we abandon the use of computationally involved adversarial objectives, network ensembles and style transfer. Instead, we employ standard data augmentation techniques $-$ photometric noise, flipping and scaling $-$ and ensure consistency of the semantic predictions across these image transformations. We develop this principle in a lightweight self-supervised framework trained on co-evolving pseudo labels without the need for cumbersome extra training rounds. Simple in training from a practitioner's standpoint, our approach is remarkably effective. We achieve significant improvements of the state-of-the-art segmentation accuracy after adaptation, consistent both across different choices of the backbone architecture and adaptation scenarios.

</details>

### Vectorization and Rasterization: Self-Supervised Learning for Sketch and Handwriting.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Bhunia_Vectorization_and_Rasterization_Self-Supervised_Learning_for_Sketch_and_Handwriting_CVPR_2021_paper.html) · 📚 被引 56
- **作者**: Ayan Kumar Bhunia, Pinaki Nath Chowdhury, Yongxin Yang, Timothy M. Hospedales, Tao Xiang, Yi-Zhe Song
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Model-Based 3D Hand Reconstruction via Self-Supervised Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Model-Based_3D_Hand_Reconstruction_via_Self-Supervised_Learning_CVPR_2021_paper.html) · 📚 被引 107
- **作者**: Yujin Chen, Zhigang Tu, Di Kang, Linchao Bao, Ying Zhang, Xuefei Zhe et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Pareto Self-Supervised Training for Few-Shot Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Pareto_Self-Supervised_Training_for_Few-Shot_Learning_CVPR_2021_paper.html) · 📚 被引 114
- **作者**: Zhengyu Chen, Jixie Ge, Heshen Zhan, Siteng Huang, Donglin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Shot Contrastive Self-Supervised Learning for Scene Boundary Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Shot_Contrastive_Self-Supervised_Learning_for_Scene_Boundary_Detection_CVPR_2021_paper.html) · 📚 被引 47
- **作者**: Shixing Chen, Xiaohan Nie, David Fan, Dongqing Zhang, Vimal Bhat, Raffay Hamid
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### SPSG: Self-Supervised Photometric Scene Generation From RGB-D Scans.
- **链接**: [arXiv:2006.14660](https://arxiv.org/abs/2006.14660) · 📚 被引 33
- **作者**: Angela Dai, Yawar Siddiqui, Justus Thies, Julien Valentin, Matthias Nießner
- **🏷️ 机构**: Technical University of Munich, Google
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present SPSG, a novel approach to generate high-quality, colored 3D models of scenes from RGB-D scan observations by learning to infer unobserved scene geometry and color in a self-supervised fashion. Our self-supervised approach learns to jointly inpaint geometry and color by correlating an incomplete RGB-D scan with a more complete version of that scan. Notably, rather than relying on 3D reconstruction losses to inform our 3D geometry and color reconstruction, we propose adversarial and perceptual losses operating on 2D renderings in order to achieve high-resolution, high-quality colored reconstructions of scenes. This exploits the high-resolution, self-consistent signal from individual raw RGB-D frames, in contrast to fused 3D reconstructions of the frames which exhibit inconsistencies from view-dependent effects, such as color balancing or pose inconsistencies. Thus, by informing our 3D scene generation directly through 2D signal, we produce high-quality colored reconstructions of 3D scenes, outperforming state of the art on both synthetic and real data.

</details>

### How Well Do Self-Supervised Models Transfer?
- **链接**: [arXiv:2011.13377](https://arxiv.org/abs/2011.13377) · 📚 被引 153
- **作者**: Linus Ericsson, Henry Gouk, Timothy M. Hospedales
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised visual representation learning has seen huge progress recently, but no large scale evaluation has compared the many models now available. We evaluate the transfer performance of 13 top self-supervised models on 40 downstream tasks, including many-shot and few-shot recognition, object detection, and dense prediction. We compare their performance to a supervised baseline and show that on most tasks the best self-supervised models outperform supervision, confirming the recently observed trend in the literature. We find ImageNet Top-1 accuracy to be highly correlated with transfer to many-shot recognition, but increasingly less so for few-shot, object detection and dense prediction. No single self-supervised method dominates overall, suggesting that universal pre-training is still unsolved. Our analysis of features suggests that top self-supervised learners fail to preserve colour information as well as supervised alternatives, but tend to induce better classifier calibration, and less attentive overfitting than supervised learners.

</details>

### Anomaly Detection in Video via Self-Supervised and Multi-Task Learning.
- **链接**: [arXiv:2011.07491](https://arxiv.org/abs/2011.07491) · 📚 被引 321
- **作者**: Mariana-Iuliana Georgescu, Antonio Barbalau, Radu Tudor Ionescu, Fahad Shahbaz Khan, Marius Popescu, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection in video is a challenging computer vision problem. Due to the lack of anomalous events at training time, anomaly detection requires the design of learning methods without full supervision. In this paper, we approach anomalous event detection in video through self-supervised and multi-task learning at the object level. We first utilize a pre-trained detector to detect objects. Then, we train a 3D convolutional neural network to produce discriminative anomaly-specific information by jointly learning multiple proxy tasks: three self-supervised and one based on knowledge distillation. The self-supervised tasks are: (i) discrimination of forward/backward moving objects (arrow of time), (ii) discrimination of objects in consecutive/intermittent frames (motion irregularity) and (iii) reconstruction of object-specific appearance information. The knowledge distillation task takes into account both classification and detection information, generating large prediction discrepancies between teacher and student models when anomalies occur. To the best of our knowledge, we are the first to approach anomalous event detection in video as a multi-task learning problem, integrating multiple self-supervised and knowledge distillation proxy tasks in a single architecture. Our lightweight architecture outperforms the state-of-the-art methods on three benchmarks: Avenue, ShanghaiTech and UCSD Ped2. Additionally, we perform an ablation study demonstrating the importance of integrating self-supervised learning and normality-specific distillation in a multi-task learning setting.

</details>

### OBoW: Online Bag-of-Visual-Words Generation for Self-Supervised Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Gidaris_OBoW_Online_Bag-of-Visual-Words_Generation_for_Self-Supervised_Learning_CVPR_2021_paper.html) · 📚 被引 70
- **作者**: Spyros Gidaris, Andrei Bursuc, Gilles Puy, Nikos Komodakis, Matthieu Cord, Patrick Pérez
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### PLADE-Net: Towards Pixel-Level Accuracy for Self-Supervised Single-View Depth Estimation With Neural Positional Encoding and Distilled Matting Loss.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Gonzalez_PLADE-Net_Towards_Pixel-Level_Accuracy_for_Self-Supervised_Single-View_Depth_Estimation_With_CVPR_2021_paper.html) · 📚 被引 17
- **作者**: Juan Luis Gonzalez, Munchurl Kim
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology
- **会议**: CVPR 2021

### Safe Local Motion Planning With Self-Supervised Freespace Forecasting.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_Safe_Local_Motion_Planning_With_Self-Supervised_Freespace_Forecasting_CVPR_2021_paper.html) · 📚 被引 83
- **作者**: Peiyun Hu, Aaron Huang, John M. Dolan, David Held, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: CVPR 2021

### Self-Supervised 3D Mesh Reconstruction From Single Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hu_Self-Supervised_3D_Mesh_Reconstruction_From_Single_Images_CVPR_2021_paper.html) · 📚 被引 49
- **作者**: Tao Hu, Liwei Wang, Xiaogang Xu, Shu Liu, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2021

### Neighbor2Neighbor: Self-Supervised Denoising From Single Noisy Images.
- **链接**: [arXiv:2101.02824](https://arxiv.org/abs/2101.02824) · 📚 被引 403
- **作者**: Tao Huang, Songjiang Li, Xu Jia, Huchuan Lu, Jianzhuang Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the last few years, image denoising has benefited a lot from the fast development of neural networks. However, the requirement of large amounts of noisy-clean image pairs for supervision limits the wide use of these models. Although there have been a few attempts in training an image denoising model with only single noisy images, existing self-supervised denoising approaches suffer from inefficient network training, loss of useful information, or dependence on noise modeling. In this paper, we present a very simple yet effective method named Neighbor2Neighbor to train an effective image denoising model with only noisy images. Firstly, a random neighbor sub-sampler is proposed for the generation of training image pairs. In detail, input and target used to train a network are images sub-sampled from the same noisy image, satisfying the requirement that paired pixels of paired images are neighbors and have very similar appearance with each other. Secondly, a denoising network is trained on sub-sampled training pairs generated in the first stage, with a proposed regularizer as additional loss for better performance. The proposed Neighbor2Neighbor framework is able to enjoy the progress of state-of-the-art supervised denoising networks in network architecture design. Moreover, it avoids heavy dependence on the assumption of the noise distribution. We explain our approach from a theoretical perspective and further validate it through extensive experiments, including synthetic experiments with different noise distributions in sRGB space and real-world experiments on a denoising benchmark dataset in raw-RGB space.

</details>

### Self-Supervised Video Representation Learning by Context and Motion Decoupling.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Huang_Self-Supervised_Video_Representation_Learning_by_Context_and_Motion_Decoupling_CVPR_2021_paper.html)
- **作者**: Lianghua Huang, Yu Liu, Bin Wang, Pan Pan, Yinghui Xu, Rong Jin
- **🏷️ 机构**: SenseTime
- **会议**: CVPR 2021

### Self-Supervised Motion Learning From Static Images.
- **链接**: [arXiv:2104.00240](https://arxiv.org/abs/2104.00240) · 📚 被引 18
- **作者**: Ziyuan Huang, Shiwei Zhang, Jianwen Jiang, Mingqian Tang, Rong Jin, Marcelo H. Ang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Motions are reflected in videos as the movement of pixels, and actions are essentially patterns of inconsistent motions between the foreground and the background. To well distinguish the actions, especially those with complicated spatio-temporal interactions, correctly locating the prominent motion areas is of crucial importance. However, most motion information in existing videos are difficult to label and training a model with good motion representations with supervision will thus require a large amount of human labour for annotation. In this paper, we address this problem by self-supervised learning. Specifically, we propose to learn Motion from Static Images (MoSI). The model learns to encode motion information by classifying pseudo motions generated by MoSI. We furthermore introduce a static mask in pseudo motions to create local motion patterns, which forces the model to additionally locate notable motion areas for the correct classification.We demonstrate that MoSI can discover regions with large motion even without fine-tuning on the downstream datasets. As a result, the learned motion representations boost the performance of tasks requiring understanding of complex scenes and motions, i.e., action recognition. Extensive experiments show the consistent and transferable improvements achieved by MoSI. Codes will be soon released.

</details>

### Self-Supervised Multi-Frame Monocular Scene Flow.
- **链接**: [arXiv:2105.02216](https://arxiv.org/abs/2105.02216) · 📚 被引 49
- **作者**: Junhwa Hur, Stefan Roth
- **🏷️ 机构**: TU Darmstadt,Department of Computer Science
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating 3D scene flow from a sequence of monocular images has been gaining increased attention due to the simple, economical capture setup. Owing to the severe ill-posedness of the problem, the accuracy of current methods has been limited, especially that of efficient, real-time approaches. In this paper, we introduce a multi-frame monocular scene flow network based on self-supervised learning, improving the accuracy over previous networks while retaining real-time efficiency. Based on an advanced two-frame baseline with a split-decoder design, we propose (i) a multi-frame model using a triple frame input and convolutional LSTM connections, (ii) an occlusion-aware census loss for better accuracy, and (iii) a gradient detaching strategy to improve training stability. On the KITTI dataset, we observe state-of-the-art accuracy among monocular scene flow methods based on self-supervised learning.

</details>

### Self-Supervised Video GANs: Learning for Appearance Consistency and Motion Coherency.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Hyun_Self-Supervised_Video_GANs_Learning_for_Appearance_Consistency_and_Motion_Coherency_CVPR_2021_paper.html) · 📚 被引 16
- **作者**: Sangeek Hyun, Jihwan Kim, Jae-Pil Heo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### FlowStep3D: Model Unrolling for Self-Supervised Scene Flow Estimation.
- **链接**: [arXiv:2011.10147](https://arxiv.org/abs/2011.10147) · 📚 被引 81
- **作者**: Yair Kittenplon, Yonina C. Eldar, Dan Raviv
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating the 3D motion of points in a scene, known as scene flow, is a core problem in computer vision. Traditional learning-based methods designed to learn end-to-end 3D flow often suffer from poor generalization. Here we present a recurrent architecture that learns a single step of an unrolled iterative alignment procedure for refining scene flow predictions. Inspired by classical algorithms, we demonstrate iterative convergence toward the solution using strong regularization. The proposed method can handle sizeable temporal deformations and suggests a slimmer architecture than competitive all-to-all correlation approaches. Trained on FlyingThings3D synthetic data only, our network successfully generalizes to real scans, outperforming all existing methods by a large margin on the KITTI self-supervised benchmark.

</details>

### Dual-Stream Multiple Instance Learning Network for Whole Slide Image Classification With Self-Supervised Contrastive Learning.
- **链接**: [arXiv:2011.08939](https://arxiv.org/abs/2011.08939) · [代码](https://github.com/binli123/dsmil-wsi) · 📚 被引 778
- **作者**: Bin Li, Yin Li, Kevin W. Eliceiri
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the challenging problem of whole slide image (WSI) classification. WSIs have very high resolutions and usually lack localized annotations. WSI classification can be cast as a multiple instance learning (MIL) problem when only slide-level labels are available. We propose a MIL-based method for WSI classification and tumor detection that does not require localized annotations. Our method has three major components. First, we introduce a novel MIL aggregator that models the relations of the instances in a dual-stream architecture with trainable distance measurement. Second, since WSIs can produce large or unbalanced bags that hinder the training of MIL models, we propose to use self-supervised contrastive learning to extract good representations for MIL and alleviate the issue of prohibitive memory cost for large bags. Third, we adopt a pyramidal fusion mechanism for multiscale WSI features, and further improve the accuracy of classification and localization. Our model is evaluated on two representative WSI datasets. The classification accuracy of our model compares favorably to fully-supervised methods, with less than 2% accuracy gap across datasets. Our results also outperform all previous MIL-based methods. Additional benchmark results on standard MIL datasets further demonstrate the superior performance of our MIL aggregator on general MIL problems. GitHub repository: https://github.com/binli123/dsmil-wsi

</details>

### Self-Supervised Video Hashing via Bidirectional Transformers.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Self-Supervised_Video_Hashing_via_Bidirectional_Transformers_CVPR_2021_paper.html) · 📚 被引 53
- **作者**: Shuyan Li, Xiu Li, Jiwen Lu, Jie Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### CutPaste: Self-Supervised Learning for Anomaly Detection and Localization.
- **链接**: [arXiv:2104.04015](https://arxiv.org/abs/2104.04015) · 📚 被引 991
- **作者**: Chun-Liang Li, Kihyuk Sohn, Jinsung Yoon, Tomas Pfister
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We aim at constructing a high performance model for defect detection that detects unknown anomalous patterns of an image without anomalous data. To this end, we propose a two-stage framework for building anomaly detectors using normal training data only. We first learn self-supervised deep representations and then build a generative one-class classifier on learned representations. We learn representations by classifying normal data from the CutPaste, a simple data augmentation strategy that cuts an image patch and pastes at a random location of a large image. Our empirical study on MVTec anomaly detection dataset demonstrates the proposed algorithm is general to be able to detect various types of real-world defects. We bring the improvement upon previous arts by 3.1 AUCs when learning representations from scratch. By transfer learning on pretrained representations on ImageNet, we achieve a new state-of-theart 96.6 AUC. Lastly, we extend the framework to learn and extract representations from patches to allow localizing defective areas without annotations during training.

</details>

### Back to Event Basics: Self-Supervised Learning of Image Reconstruction for Event Cameras via Photometric Constancy.
- **链接**: [arXiv:2009.08283](https://arxiv.org/abs/2009.08283) · 📚 被引 142
- **作者**: Federico Paredes-Vallés, Guido C. H. E. de Croon
- **🏷️ 机构**: Delft University of Technology,Micro Air Vehicle Laboratory,The Netherlands
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Event cameras are novel vision sensors that sample, in an asynchronous fashion, brightness increments with low latency and high temporal resolution. The resulting streams of events are of high value by themselves, especially for high speed motion estimation. However, a growing body of work has also focused on the reconstruction of intensity frames from the events, as this allows bridging the gap with the existing literature on appearance- and frame-based computer vision. Recent work has mostly approached this problem using neural networks trained with synthetic, ground-truth data. In this work we approach, for the first time, the intensity reconstruction problem from a self-supervised learning perspective. Our method, which leverages the knowledge of the inner workings of event cameras, combines estimated optical flow and the event-based photometric constancy to train neural networks without the need for any ground-truth or synthetic data. Results across multiple datasets show that the performance of the proposed self-supervised approach is in line with the state-of-the-art. Additionally, we propose a novel, lightweight neural network for optical flow estimation that achieves high speed inference with only a minor drop in performance.

</details>

### SOLD2: Self-Supervised Occlusion-Aware Line Description and Detection.
- **链接**: [arXiv:2104.03362](https://arxiv.org/abs/2104.03362) · [代码](https://github.com/cvg/SOLD2)
- **作者**: Rémi Pautrat, Juan-Ting Lin, Viktor Larsson, Martin R. Oswald, Marc Pollefeys
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared to feature point detection and description, detecting and matching line segments offer additional challenges. Yet, line features represent a promising complement to points for multi-view tasks. Lines are indeed well-defined by the image gradient, frequently appear even in poorly textured areas and offer robust structural cues. We thus hereby introduce the first joint detection and description of line segments in a single deep network. Thanks to a self-supervised training, our method does not require any annotated line labels and can therefore generalize to any dataset. Our detector offers repeatable and accurate localization of line segments in images, departing from the wireframe parsing approach. Leveraging the recent progresses in descriptor learning, our proposed line descriptor is highly discriminative, while remaining robust to viewpoint changes and occlusions. We evaluate our approach against previous line detection and description methods on several multi-view datasets created with homographic warps as well as real-world viewpoint changes. Our full pipeline yields higher repeatability, localization accuracy and matching metrics, and thus represents a first step to bridge the gap with learned feature points methods. Code and trained weights are available at https://github.com/cvg/SOLD2.

</details>

### Self-Supervised Collision Handling via Generative 3D Garment Models for Virtual Try-On.
- **链接**: [arXiv:2105.06462](https://arxiv.org/abs/2105.06462) · 📚 被引 103
- **作者**: Igor Santesteban, Nils Thuerey, Miguel A. Otaduy, Dan Casas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a new generative model for 3D garment deformations that enables us to learn, for the first time, a data-driven method for virtual try-on that effectively addresses garment-body collisions. In contrast to existing methods that require an undesirable postprocessing step to fix garment-body interpenetrations at test time, our approach directly outputs 3D garment configurations that do not collide with the underlying body. Key to our success is a new canonical space for garments that removes pose-and-shape deformations already captured by a new diffused human body model, which extrapolates body surface properties such as skinning weights and blendshapes to any 3D point. We leverage this representation to train a generative model with a novel self-supervised collision term that learns to reliably solve garment-body interpenetrations. We extensively evaluate and compare our results with recently proposed data-driven methods, and show that our method is the first to successfully address garment-body contact in unseen body shapes and motions, without compromising realism and detail.

</details>

### CASTing Your Model: Learning To Localize Improves Self-Supervised Representations.
- **链接**: [arXiv:2012.04630](https://arxiv.org/abs/2012.04630) · 📚 被引 42
- **作者**: Ramprasaath R. Selvaraju, Karan Desai, Justin Johnson, Nikhil Naik
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in self-supervised learning (SSL) have largely closed the gap with supervised ImageNet pretraining. Despite their success these methods have been primarily applied to unlabeled ImageNet images, and show marginal gains when trained on larger sets of uncurated images. We hypothesize that current SSL methods perform best on iconic images, and struggle on complex scene images with many objects. Analyzing contrastive SSL methods shows that they have poor visual grounding and receive poor supervisory signal when trained on scene images. We propose Contrastive Attention-Supervised Tuning(CAST) to overcome these limitations. CAST uses unsupervised saliency maps to intelligently sample crops, and to provide grounding supervision via a Grad-CAM attention loss. Experiments on COCO show that CAST significantly improves the features learned by SSL methods on scene images, and further experiments show that CAST-trained models are more robust to changes in backgrounds.

</details>

### S2-BNN: Bridging the Gap Between Self-Supervised Real and 1-Bit Neural Networks via Guided Distribution Calibration.
- **链接**: [arXiv:2102.08946](https://arxiv.org/abs/2102.08946) · [代码](https://github.com/szq0214/S2-BNN) · 📚 被引 15
- **作者**: Zhiqiang Shen, Zechun Liu, Jie Qin, Lei Huang, Kwang-Ting Cheng, Marios Savvides
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous studies dominantly target at self-supervised learning on real-valued networks and have achieved many promising results. However, on the more challenging binary neural networks (BNNs), this task has not yet been fully explored in the community. In this paper, we focus on this more difficult scenario: learning networks where both weights and activations are binary, meanwhile, without any human annotated labels. We observe that the commonly used contrastive objective is not satisfying on BNNs for competitive accuracy, since the backbone network contains relatively limited capacity and representation ability. Hence instead of directly applying existing self-supervised methods, which cause a severe decline in performance, we present a novel guided learning paradigm from real-valued to distill binary networks on the final prediction distribution, to minimize the loss and obtain desirable accuracy. Our proposed method can boost the simple contrastive learning baseline by an absolute gain of 5.5~15% on BNNs. We further reveal that it is difficult for BNNs to recover the similar predictive distributions as real-valued models when training without labels. Thus, how to calibrate them is key to address the degradation in performance. Extensive experiments are conducted on the large-scale ImageNet and downstream datasets. Our method achieves substantial improvement over the simple contrastive learning baseline, and is even comparable to many mainstream supervised BNN methods. Code is available at https://github.com/szq0214/S2-BNN.

</details>

### Self-Supervised Visibility Learning for Novel View Synthesis.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Shi_Self-Supervised_Visibility_Learning_for_Novel_View_Synthesis_CVPR_2021_paper.html) · 📚 被引 13
- **作者**: Yujiao Shi, Hongdong Li, Xin Yu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Removing the Background by Adding the Background: Towards Background Robust Self-Supervised Video Representation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Removing_the_Background_by_Adding_the_Background_Towards_Background_Robust_CVPR_2021_paper.html)
- **作者**: Jinpeng Wang, Yuting Gao, Ke Li, Yiqi Lin, Andy J. Ma, Hao Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Dense Contrastive Learning for Self-Supervised Visual Pre-Training.
- **链接**: [arXiv:2011.09157](https://arxiv.org/abs/2011.09157) · 📚 被引 570
- **作者**: Xinlong Wang, Rufeng Zhang, Chunhua Shen, Tao Kong, Lei Li
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To date, most existing self-supervised learning methods are designed and optimized for image classification. These pre-trained models can be sub-optimal for dense prediction tasks due to the discrepancy between image-level prediction and pixel-level prediction. To fill this gap, we aim to design an effective, dense self-supervised learning method that directly works at the level of pixels (or local features) by taking into account the correspondence between local features. We present dense contrastive learning, which implements self-supervised learning by optimizing a pairwise contrastive (dis)similarity loss at the pixel level between two views of input images. Compared to the baseline method MoCo-v2, our method introduces negligible computation overhead (only <1% slower), but demonstrates consistently superior performance when transferring to downstream dense prediction tasks including object detection, semantic segmentation and instance segmentation; and outperforms the state-of-the-art methods by a large margin. Specifically, over the strong MoCo-v2 baseline, our method achieves significant improvements of 2.0% AP on PASCAL VOC object detection, 1.1% AP on COCO object detection, 0.9% AP on COCO instance segmentation, 3.0% mIoU on PASCAL VOC semantic segmentation and 1.8% mIoU on Cityscapes semantic segmentation. Code is available at: https://git.io/AdelaiDet

</details>

### Instance Localization for Self-Supervised Detection Pretraining.
- **链接**: [arXiv:2102.08318](https://arxiv.org/abs/2102.08318) · 📚 被引 103
- **作者**: Ceyuan Yang, Zhirong Wu, Bolei Zhou, Stephen Lin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prior research on self-supervised learning has led to considerable progress on image classification, but often with degraded transfer performance on object detection. The objective of this paper is to advance self-supervised pretrained models specifically for object detection. Based on the inherent difference between classification and detection, we propose a new self-supervised pretext task, called instance localization. Image instances are pasted at various locations and scales onto background images. The pretext task is to predict the instance category given the composited images as well as the foreground bounding boxes. We show that integration of bounding boxes into pretraining promotes better task alignment and architecture alignment for transfer learning. In addition, we propose an augmentation method on the bounding boxes to further enhance the feature alignment. As a result, our model becomes weaker at Imagenet semantic classification but stronger at image patch localization, with an overall stronger pretrained model for object detection. Experimental results demonstrate that our approach yields state-of-the-art transfer learning results for object detection on PASCAL VOC and MSCOCO.

</details>

### Prototypical Cross-Domain Self-Supervised Learning for Few-Shot Unsupervised Domain Adaptation.
- **链接**: [arXiv:2103.16765](https://arxiv.org/abs/2103.16765) · 📚 被引 156
- **作者**: Xiangyu Yue, Zangwei Zheng, Shanghang Zhang, Yang Gao, Trevor Darrell, Kurt Keutzer et al.
- **🏷️ 机构**: UC Berkeley
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Domain Adaptation (UDA) transfers predictive models from a fully-labeled source domain to an unlabeled target domain. In some applications, however, it is expensive even to collect labels in the source domain, making most previous works impractical. To cope with this problem, recent work performed instance-wise cross-domain self-supervised learning, followed by an additional fine-tuning stage. However, the instance-wise self-supervised learning only learns and aligns low-level discriminative features. In this paper, we propose an end-to-end Prototypical Cross-domain Self-Supervised Learning (PCS) framework for Few-shot Unsupervised Domain Adaptation (FUDA). PCS not only performs cross-domain low-level feature alignment, but it also encodes and aligns semantic structures in the shared embedding space across domains. Our framework captures category-wise semantic structures of the data by in-domain prototypical contrastive learning; and performs feature alignment through cross-domain prototypical self-supervision. Compared with state-of-the-art methods, PCS improves the mean classification accuracy over different domain pairs on FUDA by 10.5%, 3.5%, 9.0%, and 13.2% on Office, Office-Home, VisDA-2017, and DomainNet, respectively. Our project page is at http://xyue.io/pcs-fuda/index.html

</details>

### VideoMoCo: Contrastive Video Representation Learning With Temporally Adversarial Examples.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Pan_VideoMoCo_Contrastive_Video_Representation_Learning_With_Temporally_Adversarial_Examples_CVPR_2021_paper.html)
- **作者**: Tian Pan, Yibing Song, Tianyu Yang, Wenhao Jiang, Wei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Contrastive Learning Based Hybrid Networks for Long-Tailed Image Classification.
- **链接**: [arXiv:2103.14267](https://arxiv.org/abs/2103.14267) · 📚 被引 291
- **作者**: Peng Wang, Kai Han, Xiu-Shen Wei, Lei Zhang, Lei Wang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning discriminative image representations plays a vital role in long-tailed image classification because it can ease the classifier learning in imbalanced cases. Given the promising performance contrastive learning has shown recently in representation learning, in this work, we explore effective supervised contrastive learning strategies and tailor them to learn better image representations from imbalanced data in order to boost the classification accuracy thereon. Specifically, we propose a novel hybrid network structure being composed of a supervised contrastive loss to learn image representations and a cross-entropy loss to learn classifiers, where the learning is progressively transited from feature learning to the classifier learning to embody the idea that better features make better classifiers. We explore two variants of contrastive loss for feature learning, which vary in the forms but share a common idea of pulling the samples from the same class together in the normalized embedding space and pushing the samples from different classes apart. One of them is the recently proposed supervised contrastive (SC) loss, which is designed on top of the state-of-the-art unsupervised contrastive loss by incorporating positive samples from the same class. The other is a prototypical supervised contrastive (PSC) learning strategy which addresses the intensive memory consumption in standard SC loss and thus shows more promise under limited memory budget. Extensive experiments on three long-tailed classification datasets demonstrate the advantage of the proposed contrastive learning based hybrid networks in long-tailed classification.

</details>

### Sequence-to-Sequence Contrastive Learning for Text Recognition.
- **链接**: [arXiv:2012.10873](https://arxiv.org/abs/2012.10873) · 📚 被引 130
- **作者**: Aviad Aberdam, Ron Litman, Shahar Tsiper, Oron Anschel, Ron Slossberg, Shai Mazor et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a framework for sequence-to-sequence contrastive learning (SeqCLR) of visual representations, which we apply to text recognition. To account for the sequence-to-sequence structure, each feature map is divided into different instances over which the contrastive loss is computed. This operation enables us to contrast in a sub-word level, where from each image we extract several positive pairs and multiple negative examples. To yield effective visual representations for text recognition, we further suggest novel augmentation heuristics, different encoder architectures and custom projection heads. Experiments on handwritten text and on scene text show that when a text decoder is trained on the learned representations, our method outperforms non-sequential contrastive methods. In addition, when the amount of supervision is reduced, SeqCLR significantly improves performance compared with supervised training, and when fine-tuned with 100% of the labels, our method achieves state-of-the-art results on standard handwritten text recognition benchmarks.

</details>

### Fine-Grained Angular Contrastive Learning With Coarse Labels.
- **链接**: [arXiv:2012.03515](https://arxiv.org/abs/2012.03515) · 📚 被引 42
- **作者**: Guy Bukchin, Eli Schwartz, Kate Saenko, Ori Shahar, Rogério Feris, Raja Giryes et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot learning methods offer pre-training techniques optimized for easier later adaptation of the model to new classes (unseen during training) using one or a few examples. This adaptivity to unseen classes is especially important for many practical applications where the pre-trained label space cannot remain fixed for effective use and the model needs to be "specialized" to support new categories on the fly. One particularly interesting scenario, essentially overlooked by the few-shot literature, is Coarse-to-Fine Few-Shot (C2FS), where the training classes (e.g. animals) are of much `coarser granularity' than the target (test) classes (e.g. breeds). A very practical example of C2FS is when the target classes are sub-classes of the training classes. Intuitively, it is especially challenging as (both regular and few-shot) supervised pre-training tends to learn to ignore intra-class variability which is essential for separating sub-classes. In this paper, we introduce a novel 'Angular normalization' module that allows to effectively combine supervised and self-supervised contrastive pre-training to approach the proposed C2FS task, demonstrating significant gains in a broad study over multiple baselines and datasets. We hope that this work will help to pave the way for future research on this new, challenging, and very practical topic of C2FS classification.

</details>

### Joint Generative and Contrastive Learning for Unsupervised Person Re-Identification.
- **链接**: [arXiv:2012.09071](https://arxiv.org/abs/2012.09071)
- **作者**: Hao Chen, Yaohui Wang, Benoit Lagadec, Antitza Dantcheva, François Brémond
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent self-supervised contrastive learning provides an effective approach for unsupervised person re-identification (ReID) by learning invariance from different views (transformed versions) of an input. In this paper, we incorporate a Generative Adversarial Network (GAN) and a contrastive learning module into one joint training framework. While the GAN provides online data augmentation for contrastive learning, the contrastive module learns view-invariant features for generation. In this context, we propose a mesh-based view generator. Specifically, mesh projections serve as references towards generating novel views of a person. In addition, we propose a view-invariant loss to facilitate contrastive learning between original and generated views. Deviating from previous GAN-based unsupervised ReID methods involving domain adaptation, we do not rely on a labeled source dataset, which makes our method more flexible. Extensive experimental results show that our method significantly outperforms state-of-the-art methods under both, fully unsupervised and unsupervised domain adaptive settings on several large scale ReID datsets.

</details>

### Mining Better Samples for Contrastive Learning of Temporal Correspondence.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Jeon_Mining_Better_Samples_for_Contrastive_Learning_of_Temporal_Correspondence_CVPR_2021_paper.html) · 📚 被引 22
- **作者**: Sangryul Jeon, Dongbo Min, Seungryong Kim, Kwanghoon Sohn
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### CLCC: Contrastive Learning for Color Constancy.
- **链接**: [arXiv:2106.04989](https://arxiv.org/abs/2106.04989) · 📚 被引 55
- **作者**: Yi-Chen Lo, Chia-Che Chang, Hsuan-Chao Chiu, Yu-Hao Huang, Chia-Ping Chen, Yu-Lin Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present CLCC, a novel contrastive learning framework for color constancy. Contrastive learning has been applied for learning high-quality visual representations for image classification. One key aspect to yield useful representations for image classification is to design illuminant invariant augmentations. However, the illuminant invariant assumption conflicts with the nature of the color constancy task, which aims to estimate the illuminant given a raw image. Therefore, we construct effective contrastive pairs for learning better illuminant-dependent features via a novel raw-domain color augmentation. On the NUS-8 dataset, our method provides $17.5\%$ relative improvements over a strong baseline, reaching state-of-the-art performance without increasing model complexity. Furthermore, our method achieves competitive performance on the Gehler dataset with $3\times$ fewer parameters compared to top-ranking deep learning methods. More importantly, we show that our model is more robust to different scenes under close proximity of illuminants, significantly reducing $28.7\%$ worst-case error in data-sparse regions.

</details>

### Interventional Video Grounding With Dual Contrastive Learning.
- **链接**: [arXiv:2106.11013](https://arxiv.org/abs/2106.11013) · [代码](https://github.com/nanguoshun/IVG) · 📚 被引 121
- **作者**: Guoshun Nan, Rui Qiao, Yao Xiao, Jun Liu, Sicong Leng, Hao Zhang et al.
- **🏷️ 机构**: Singapore University of Technology and Design,StatNLP Research Group,China, Shanghai Jiao Tong University, Singapore University of Technology and Design,Information Systems Technology and Design,Singapore
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video grounding aims to localize a moment from an untrimmed video for a given textual query. Existing approaches focus more on the alignment of visual and language stimuli with various likelihood-based matching or regression strategies, i.e., P(Y|X). Consequently, these models may suffer from spurious correlations between the language and video features due to the selection bias of the dataset. 1) To uncover the causality behind the model and data, we first propose a novel paradigm from the perspective of the causal inference, i.e., interventional video grounding (IVG) that leverages backdoor adjustment to deconfound the selection bias based on structured causal model (SCM) and do-calculus P(Y|do(X)). Then, we present a simple yet effective method to approximate the unobserved confounder as it cannot be directly sampled from the dataset. 2) Meanwhile, we introduce a dual contrastive learning approach (DCL) to better align the text and video by maximizing the mutual information (MI) between query and video clips, and the MI between start/end frames of a target moment and the others within a video to learn more informative visual representations. Experiments on three standard benchmarks show the effectiveness of our approaches. Our code is available on GitHub: https://github.com/nanguoshun/IVG.

</details>

## 跨领域论文（完整笔记在其他领域）

- There Is More Than Meets the Eye: Self-Supervised Multi-Object Detection and Tracking With Sound by Distilling Multimodal Knowledge. → [multimodal](../multimodal/Guideline%202021.md)
- Self-Supervised Learning of Depth Inference for Multi-View Stereo. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-Supervised Pillar Motion Learning for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202021.md)
- Three Ways To Improve Semantic Segmentation With Self-Supervised Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Revamping Cross-Modal Recipe Retrieval With Hierarchical Transformers and Self-Supervised Learning. → [multimodal](../multimodal/Guideline%202021.md)
- CanonPose: Self-Supervised Monocular 3D Human Pose Estimation in the Wild. → [3d-detection](../3d-detection/Guideline%202021.md)
- Cross-Modal Contrastive Learning for Text-to-Image Generation. → [multimodal](../multimodal/Guideline%202021.md)
- Distilling Audio-Visual Knowledge by Compositional Contrastive Learning. → [multimodal](../multimodal/Guideline%202021.md)
