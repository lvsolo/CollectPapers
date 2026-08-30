# Self-supervised Vision — 2020 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 34 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### From Image Collections to Point Clouds With Self-Supervised Shape and Pose Networks. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2005.01939](https://arxiv.org/abs/2005.01939) · 📚 被引 31
- **作者**: Navaneet K. L., Ansu Mathew, Shashank Kashyap, Wei-Chih Hung, Varun Jampani, R. Venkatesh Babu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对从单张图像重建3D物体时依赖3D或多视角监督的问题，提出仅使用单视角图像和轮廓的自监督方法。②同时学习3D点云重建和姿态估计网络，利用可微点云渲染器进行2D监督，并通过随机采样姿态和循环一致性约束增强3D几何推理。③相比需要姿态监督的方法，本方法在训练时无需任何姿态信息，更实用。④在ShapeNet和Pix3D数据集上，尽管监督更少，性能与姿态监督方法相当。
- **摘要（英）**: This paper proposes a self-supervised method for 3D object reconstruction from single images, requiring only image collections and silhouettes without pose supervision. It jointly learns point cloud reconstruction and pose estimation with cycle consistency, achieving competitive performance on ShapeNet and Pix3D compared to pose-supervised methods.
- **核心贡献**: 提出仅需单视图图像和轮廓的自监督3D重建与姿态估计方法。
- **创新点**: 通过随机姿态旋转和循环一致性实现无姿态监督的3D几何学习。
- **结果**: 在ShapeNet和Pix3D上达到与姿态监督方法相当的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing 3D models from 2D images is one of the fundamental problems in computer vision. In this work, we propose a deep learning technique for 3D object reconstruction from a single image. Contrary to recent works that either use 3D supervision or multi-view supervision, we use only single view images with no pose information during training as well. This makes our approach more practical requiring only an image collection of an object category and the corresponding silhouettes. We learn both 3D point cloud reconstruction and pose estimation networks in a self-supervised manner, making use of differentiable point cloud renderer to train with 2D supervision. A key novelty of the proposed technique is to impose 3D geometric reasoning into predicted 3D point clouds by rotating them with randomly sampled poses and then enforcing cycle consistency on both 3D reconstructions and poses. In addition, using single-view supervision allows us to do test-time optimization on a given test image. Experiments on the synthetic ShapeNet and real-world Pix3D datasets demonstrate that our approach, despite using less supervision, can achieve competitive performance compared to pose-supervised and multi-view supervised approaches.

</details>

### Self-Supervised Relational Reasoning for Representation Learning.
- **链接**: [arXiv:2006.05849](https://arxiv.org/abs/2006.05849)
- **作者**: Massimiliano Patacchiola, Amos J. Storkey
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video prediction models combined with planning algorithms have shown promise in enabling robots to learn to perform many vision-based tasks through only self-supervision, reaching novel goals in cluttered scenes with unseen objects. However, due to the compounding uncertainty in long horizon video prediction and poor scalability of sampling-based planning optimizers, one significant limitation of these approaches is the ability to plan over long horizons to reach distant goals. To that end, we propose a framework for subgoal generation and planning, hierarchical visual foresight (HVF), which generates subgoal images conditioned on a goal image, and uses them for planning. The subgoal images are directly optimized to decompose the task into easy to plan segments, and as a result, we observe that the method naturally identifies semantically meaningful states as subgoals. Across three out of four simulated vision-based manipulation tasks, we find that our method achieves nearly a 200% performance improvement over planning without subgoals and model-free RL approaches. Further, our experiments illustrate that our approach extends to real, cluttered visual scenes. Project page: https://sites.google.com/stanford.edu/hvf

</details>

### Planning to Explore via Self-Supervised World Models.
- **链接**: [arXiv:2005.05960](https://arxiv.org/abs/2005.05960)
- **作者**: Ramanan Sekar, Oleh Rybkin, Kostas Daniilidis, Pieter Abbeel, Danijar Hafner, Deepak Pathak
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Monocular Trained Depth Estimation Using Self-Attention and Discrete Disparity Volume. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2003.13951](https://arxiv.org/abs/2003.13951) · 📚 被引 231
- **作者**: Adrian Johnston, Gustavo Carneiro
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督单目深度估计中卷积操作局部性限制和连续深度预测精度不足的问题。②提出在自监督框架中引入自注意力机制和离散视差体积预测，自注意力能捕捉非连续区域的上下文信息，离散预测提高深度精度。③相比现有自监督方法，增强了全局上下文建模能力，并改进了深度离散化策略。④实验表明，该方法在KITTI等基准上显著提升了深度估计精度，但摘要未给出具体数值。
- **摘要（英）**: This paper improves self-supervised monocular depth estimation by introducing self-attention to capture global context and discrete disparity volume prediction for finer depth granularity. It outperforms existing self-supervised methods on benchmarks like KITTI, though specific numbers are not in the abstract.
- **核心贡献**: 提出结合自注意力和离散视差体积的自监督单目深度估计方法。
- **创新点**: 利用自注意力捕捉非连续区域上下文，并采用离散视差预测提升精度。
- **结果**: 在KITTI等基准上显著提升深度估计精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation has become one of the most studied applications in computer vision, where the most accurate approaches are based on fully supervised learning models. However, the acquisition of accurate and large ground truth data sets to model these fully supervised methods is a major challenge for the further development of the area. Self-supervised methods trained with monocular videos constitute one the most promising approaches to mitigate the challenge mentioned above due to the wide-spread availability of training data. Consequently, they have been intensively studied, where the main ideas explored consist of different types of model architectures, loss functions, and occlusion masks to address non-rigid motion. In this paper, we propose two new ideas to improve self-supervised monocular trained depth estimation: 1) self-attention, and 2) discrete disparity prediction. Compared with the usual localised convolution operation, self-attention can explore a more general contextual information that allows the inference of similar disparity values at non-contiguous regions of the image. Discrete disparity prediction has been shown by fully supervised methods to provide a more robust and sharper depth estimation than the more common continuous disparity prediction, besides enabling the estimation of depth uncertainty. We show that the extension of the state-of-the-art self-supervised monocular trained depth estimator Monodepth2 with these two ideas allows us to design a model that produces the best results in the field in KITTI 2015 and Make3D, closing the gap with respect self-supervised stereo training and fully supervised approaches.

</details>

### Self2Self With Dropout: Learning Self-Supervised Denoising From Single Image. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Quan_Self2Self_With_Dropout_Learning_Self-Supervised_Denoising_From_Single_Image_CVPR_2020_paper.html) · 📚 被引 381
- **作者**: Yuhui Quan, Mingqin Chen, Tongyao Pang, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对单张图像自监督去噪问题，传统方法依赖多张噪声图像或统计先验。②提出Self2Self方法，利用dropout在单张图像上训练网络，通过多次采样预测平均实现去噪。③相比BM3D等传统方法，无需外部数据，完全自监督。④在合成和真实噪声图像上表现接近监督方法，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses single-image self-supervised denoising. It proposes Self2Self, which trains a network with dropout on a single noisy image and averages multiple predictions. It achieves performance comparable to supervised methods without external data, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出基于dropout的单图像自监督去噪框架。
- **创新点**: 利用dropout的随机性实现单图像自监督训练。
- **结果**: 在单图像去噪任务上达到接近监督方法的性能。

### Self-Supervised Equivariant Attention Mechanism for Weakly Supervised Semantic Segmentation. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2004.04581](https://arxiv.org/abs/2004.04581) · 📚 被引 668
- **作者**: Yude Wang, Jie Zhang, Meina Kan, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对弱监督语义分割中CAM与真实掩码差距大的问题。②提出自监督等变注意力机制SEAM，通过变换图像的一致性正则化提供额外监督，并设计像素相关模块PCM利用上下文信息细化预测。③相比现有CAM方法，首次将等变性约束引入弱监督分割。④在PASCAL VOC 2012上优于现有方法，但摘要未给出具体数值。
- **摘要（英）**: This paper tackles the gap between CAMs and ground-truth masks in weakly supervised semantic segmentation. It proposes SEAM, a self-supervised equivariant attention mechanism with consistency regularization on transformed images, and a pixel correlation module for refinement. It outperforms prior methods on PASCAL VOC 2012, though exact numbers are omitted.
- **核心贡献**: 提出等变一致性正则化提升弱监督分割性能。
- **创新点**: 将等变性约束引入CAM训练。
- **结果**: 在PASCAL VOC 2012上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-level weakly supervised semantic segmentation is a challenging problem that has been deeply studied in recent years. Most of advanced solutions exploit class activation map (CAM). However, CAMs can hardly serve as the object mask due to the gap between full and weak supervisions. In this paper, we propose a self-supervised equivariant attention mechanism (SEAM) to discover additional supervision and narrow the gap. Our method is based on the observation that equivariance is an implicit constraint in fully supervised semantic segmentation, whose pixel-level labels take the same spatial transformation as the input images during data augmentation. However, this constraint is lost on the CAMs trained by image-level supervision. Therefore, we propose consistency regularization on predicted CAMs from various transformed images to provide self-supervision for network learning. Moreover, we propose a pixel correlation module (PCM), which exploits context appearance information and refines the prediction of current pixel by its similar neighbors, leading to further improvement on CAMs consistency. Extensive experiments on PASCAL VOC 2012 dataset demonstrate our method outperforms state-of-the-art methods using the same level of supervision. The code is released online.

</details>

### Adversarial Robustness: From Self-Supervised Pre-Training to Fine-Tuning. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2003.12862](https://arxiv.org/abs/2003.12862) · 📚 被引 132
- **作者**: Tianlong Chen, Sijia Liu, Shiyu Chang, Yu Cheng, Lisa Amini, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督预训练模型在对抗鲁棒性方面未被探索的问题。②首次将对抗训练引入自监督预训练，生成通用鲁棒预训练模型，并发现其可提升下游微调的鲁棒性和计算效率。③相比传统端到端对抗训练，在CIFAR-10上鲁棒准确率提升3.83%，标准准确率提升1.3%。④集成多种预训练任务进一步将鲁棒准确率提升3.59%。
- **摘要（英）**: This paper addresses the unexplored adversarial robustness of self-supervised pretrained models. It introduces adversarial training into self-supervision to create robust pretrained models, which boost downstream fine-tuning robustness and save computation. It achieves 3.83% higher robust accuracy and 1.3% higher standard accuracy on CIFAR-10, with ensemble methods adding 3.59% more.
- **核心贡献**: 首次提供通用鲁棒自监督预训练模型。
- **创新点**: 将对抗训练融入自监督预训练阶段。
- **结果**: 在CIFAR-10上显著提升鲁棒和标准准确率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained models from self-supervision are prevalently used in fine-tuning downstream tasks faster or for better accuracy. However, gaining robustness from pretraining is left unexplored. We introduce adversarial training into self-supervision, to provide general-purpose robust pre-trained models for the first time. We find these robust pre-trained models can benefit the subsequent fine-tuning in two ways: i) boosting final model robustness; ii) saving the computation cost, if proceeding towards adversarial fine-tuning. We conduct extensive experiments to demonstrate that the proposed framework achieves large performance margins (eg, 3.83% on robust accuracy and 1.3% on standard accuracy, on the CIFAR-10 dataset), compared with the conventional end-to-end adversarial training baseline. Moreover, we find that different self-supervised pre-trained models have a diverse adversarial vulnerability. It inspires us to ensemble several pretraining tasks, which boosts robustness more. Our ensemble strategy contributes to a further improvement of 3.59% on robust accuracy, while maintaining a slightly higher standard accuracy on CIFAR-10. Our codes are available at https://github.com/TAMU-VITA/Adv-SS-Pretraining.

</details>

### Hierarchical Foresight: Self-Supervised Learning of Long-Horizon Tasks via Visual Subgoal Generation.
- **链接**: [arXiv:1909.05829](https://arxiv.org/abs/1909.05829)
- **作者**: Suraj Nair, Chelsea Finn
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video prediction models combined with planning algorithms have shown promise in enabling robots to learn to perform many vision-based tasks through only self-supervision, reaching novel goals in cluttered scenes with unseen objects. However, due to the compounding uncertainty in long horizon video prediction and poor scalability of sampling-based planning optimizers, one significant limitation of these approaches is the ability to plan over long horizons to reach distant goals. To that end, we propose a framework for subgoal generation and planning, hierarchical visual foresight (HVF), which generates subgoal images conditioned on a goal image, and uses them for planning. The subgoal images are directly optimized to decompose the task into easy to plan segments, and as a result, we observe that the method naturally identifies semantically meaningful states as subgoals. Across three out of four simulated vision-based manipulation tasks, we find that our method achieves nearly a 200% performance improvement over planning without subgoals and model-free RL approaches. Further, our experiments illustrate that our approach extends to real, cluttered visual scenes. Project page: https://sites.google.com/stanford.edu/hvf

</details>

### Neural Outlier Rejection for Self-Supervised Keypoint Learning.
- **链接**: [arXiv:1912.10615](https://arxiv.org/abs/1912.10615)
- **作者**: Jiexiong Tang, Hanme Kim, Vitor Guizilini, Sudeep Pillai, Rares Ambrus
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Monocular Scene Flow Estimation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2004.04143](https://arxiv.org/abs/2004.04143) · 📚 被引 99
- **作者**: Junhwa Hur, Stefan Roth
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对单目场景流估计这一病态问题，即从连续两帧图像同时估计3D结构和3D运动，现有方法精度低且缺乏实用方案。②提出一种逆问题视角的单一CNN，从经典光流代价体积中同时估计深度和3D运动，并采用自监督学习与3D损失函数及遮挡推理来利用无标签数据。③相比已有工作，创新性地将光流代价体积作为输入，并通过代理损失和增强设置验证设计选择。④在无监督/自监督单目场景流方法中达到最先进精度，在光流和单目深度估计子任务上也有竞争力，半监督微调进一步提升精度并实现实时性能。
- **摘要（英）**: This paper addresses the ill-posed monocular scene flow estimation problem by proposing a single CNN that jointly estimates depth and 3D motion from an optical flow cost volume, using self-supervised learning with 3D losses and occlusion reasoning. It achieves state-of-the-art accuracy among unsupervised/self-supervised methods and competitive results on subtasks, with real-time performance after semi-supervised fine-tuning.
- **核心贡献**: 提出了一种基于光流代价体积的单一CNN自监督单目场景流估计方法。
- **创新点**: 将经典光流代价体积作为输入，结合3D损失和遮挡推理实现自监督联合估计。
- **结果**: 在无监督/自监督方法中达到最先进精度，并支持实时推理。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene flow estimation has been receiving increasing attention for 3D environment perception. Monocular scene flow estimation -- obtaining 3D structure and 3D motion from two temporally consecutive images -- is a highly ill-posed problem, and practical solutions are lacking to date. We propose a novel monocular scene flow method that yields competitive accuracy and real-time performance. By taking an inverse problem view, we design a single convolutional neural network (CNN) that successfully estimates depth and 3D motion simultaneously from a classical optical flow cost volume. We adopt self-supervised learning with 3D loss functions and occlusion reasoning to leverage unlabeled data. We validate our design choices, including the proxy loss and augmentation setup. Our model achieves state-of-the-art accuracy among unsupervised/self-supervised learning approaches to monocular scene flow, and yields competitive results for the optical flow and monocular depth estimation sub-tasks. Semi-supervised fine-tuning further improves the accuracy and yields promising results in real-time.

</details>

### Self-Supervised Learning of Interpretable Keypoints From Unlabelled Videos. **⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Jakab_Self-Supervised_Learning_of_Interpretable_Keypoints_From_Unlabelled_Videos_CVPR_2020_paper.html) · 📚 被引 57
- **作者**: Tomas Jakab, Ankush Gupta, Hakan Bilen, Andrea Vedaldi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对从无标注视频中学习可解释关键点的问题。②提出自监督方法，利用视频中的运动一致性学习关键点，无需人工标注。③相比现有方法，强调关键点的可解释性和时序一致性。④摘要未提供具体数据，但方法在多个基准上验证。
- **摘要（英）**: This paper addresses learning interpretable keypoints from unlabelled videos. It proposes a self-supervised method leveraging motion consistency to learn keypoints without annotations. It emphasizes interpretability and temporal consistency, though specific metrics are not provided.
- **核心贡献**: 提出自监督可解释关键点学习方法。
- **创新点**: 利用视频运动一致性学习关键点。
- **结果**: 在无标注视频上学习到可解释关键点，具体效果未详述。

### Steering Self-Supervised Feature Learning Beyond Local Pixel Statistics. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2004.02331](https://arxiv.org/abs/2004.02331) · 📚 被引 33
- **作者**: Simon Jenni, Hailin Jin, Paolo Favaro
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督特征学习依赖局部像素统计、难以捕捉全局图像统计的问题。②提出基于图像变换判别的新原则，并设计了一种名为有限上下文修复（LCI）的新变换，仅用小块矩形边界修复图像块。③相比已有方法，LCI能迫使网络学习更全局的特征，从而更好地表示物体形状和上下文。④实验表明，该方法在物体分类和检测等下游任务上泛化性能更优。
- **摘要（英）**: This paper addresses the limitation of self-supervised feature learning relying on local pixel statistics. It introduces a principle based on discriminating image transformations and a novel transformation, limited context inpainting (LCI), which inpaints patches using only a small boundary. LCI encourages learning more global features, improving generalization to downstream tasks like classification and detection.
- **核心贡献**: 提出基于变换判别的新原则和LCI变换，推动自监督学习向全局特征迈进。
- **创新点**: 创新性地利用有限上下文修复作为变换，量化局部与全局统计的判别难度。
- **结果**: 在分类和检测任务上展示了更好的泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel principle for self-supervised feature learning based on the discrimination of specific transformations of an image. We argue that the generalization capability of learned features depends on what image neighborhood size is sufficient to discriminate different image transformations: The larger the required neighborhood size and the more global the image statistics that the feature can describe. An accurate description of global image statistics allows to better represent the shape and configuration of objects and their context, which ultimately generalizes better to new tasks such as object classification and detection. This suggests a criterion to choose and design image transformations. Based on this criterion, we introduce a novel image transformation that we call limited context inpainting (LCI). This transformation inpaints an image patch conditioned only on a small rectangular pixel boundary (the limited context). Because of the limited boundary information, the inpainter can learn to match local pixel statistics, but is unlikely to match the global statistics of the image. We claim that the same principle can be used to justify the performance of transformations such as image rotations and warping. Indeed, we demonstrate experimentally that learning to discriminate transformations such as LCI, image warping and rotations, yields features with state of the art generalization capabilities on several datasets such as Pascal VOC, STL-10, CelebA, and ImageNet. Remarkably, our trained features achieve a performance on Places on par with features trained through supervised learning with ImageNet labels.

</details>

### Self-Supervised 3D Human Pose Estimation via Part Guided Novel Image Synthesis. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2004.04400](https://arxiv.org/abs/2004.04400) · 📚 被引 66
- **作者**: Jogendra Nath Kundu, Siddharth Seth, Varun Jampani, Mugalodi Rakesh, R. Venkatesh Babu, Anirban Chakraborty
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对监督3D姿态估计中的任务偏差和数据集偏差问题。②提出自监督框架，利用2D木偶模型、姿态约束和未配对3D姿态，通过可微分形式化解耦形状和外观等变化。③相比弱监督方法，该方法能更好地泛化到未见数据集，并支持多任务。④在3D姿态估计和部件分割上展示了优越的跨数据集泛化性能。
- **摘要（英）**: This paper tackles task and dataset bias in supervised 3D pose estimation. It proposes a self-supervised framework that disentangles variations using a 2D puppet model and unpaired 3D poses via differentiable formalization. The method improves generalization to unseen datasets and supports multiple tasks.
- **核心贡献**: 提出可微分的姿态解耦框架，增强跨数据集泛化。
- **创新点**: 利用2D木偶模型和未配对3D姿态实现自监督解耦。
- **结果**: 在未见数据集上表现优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera captured human pose is an outcome of several sources of variation. Performance of supervised 3D pose estimation approaches comes at the cost of dispensing with variations, such as shape and appearance, that may be useful for solving other related tasks. As a result, the learned model not only inculcates task-bias but also dataset-bias because of its strong reliance on the annotated samples, which also holds true for weakly-supervised models. Acknowledging this, we propose a self-supervised learning framework to disentangle such variations from unlabeled video frames. We leverage the prior knowledge on human skeleton and poses in the form of a single part-based 2D puppet model, human pose articulation constraints, and a set of unpaired 3D poses. Our differentiable formalization, bridging the representation gap between the 3D pose and spatial part maps, not only facilitates discovery of interpretable pose disentanglement but also allows us to operate on videos with diverse camera movements. Qualitative results on unseen in-the-wild datasets establish our superior generalization across multiple tasks beyond the primary tasks of 3D pose estimation and part segmentation. Furthermore, we demonstrate state-of-the-art weakly-supervised 3D pose estimation performance on both Human3.6M and MPI-INF-3DHP datasets.

</details>

### MAST: A Memory-Augmented Self-Supervised Tracker. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2002.07793](https://arxiv.org/abs/2002.07793) · 📚 被引 134
- **作者**: Zihang Lai, Erika Lu, Weidi Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督密集跟踪性能远低于监督方法的问题。②提出MAST模型，通过重新评估自监督训练和重建损失的选择，并引入记忆增强架构。③相比已有自监督方法，性能提升15%，并首次达到与监督方法相当的水平。④在视频目标分割基准上，自监督方法在泛化性指标上优于多数监督方法。
- **摘要（英）**: This paper addresses the performance gap in self-supervised dense tracking. It proposes MAST, which reassesses training choices and adds a memory component, achieving a 15% improvement over prior self-supervised methods. The model matches supervised performance and shows superior generalizability.
- **核心贡献**: 提出记忆增强的自监督密集跟踪模型，性能大幅提升。
- **创新点**: 引入记忆组件和优化训练策略，首次媲美监督方法。
- **结果**: 在基准上超越自监督方法15%，泛化性优于监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent interest in self-supervised dense tracking has yielded rapid progress, but performance still remains far from supervised methods. We propose a dense tracking model trained on videos without any annotations that surpasses previous self-supervised methods on existing benchmarks by a significant margin (+15%), and achieves performance comparable to supervised methods. In this paper, we first reassess the traditional choices used for self-supervised training and reconstruction loss by conducting thorough experiments that finally elucidate the optimal choices. Second, we further improve on existing methods by augmenting our architecture with a crucial memory component. Third, we benchmark on large-scale semi-supervised video object segmentation(aka. dense tracking), and propose a new metric: generalizability. Our first two contributions yield a self-supervised network that for the first time is competitive with supervised methods on standard evaluation metrics of dense tracking. When measuring generalizability, we show self-supervised approaches are actually superior to the majority of supervised methods. We believe this new generalizability metric can better capture the real-world use-cases for dense tracking, and will spur new interest in this research direction.

</details>

### Self-Supervised Graph Transformer on Large-Scale Molecular Data.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/94aef38441efa3380a3bed3faf1f9d5d-Abstract.html)
- **作者**: Yu Rong, Yatao Bian, Tingyang Xu, Weiyang Xie, Ying Wei, Wenbing Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Identifying salient points in images is a crucial component for visual odometry, Structure-from-Motion or SLAM algorithms. Recently, several learned keypoint methods have demonstrated compelling performance on challenging benchmarks. However, generating consistent and accurate training data for interest-point detection in natural images still remains challenging, especially for human annotators. We introduce IO-Net (i.e. InlierOutlierNet), a novel proxy task for the self-supervision of keypoint detection, description and matching. By making the sampling of inlier-outlier sets from point-pair correspondences fully differentiable within the keypoint learning framework, we show that are able to simultaneously self-supervise keypoint description and improve keypoint matching. Second, we introduce KeyPointNet, a keypoint-network architecture that is especially amenable to robust keypoint detection and description. We design the network to allow local keypoint aggregation to avoid artifacts due to spatial discretizations commonly used for this task, and we improve fine-grained keypoint descriptor performance by taking advantage of efficient sub-pixel convolutions to upsample the descriptor feature-maps to a higher operating resolution. Through extensive experiments and ablative analysis, we show that the proposed self-supervised keypoint learning method greatly improves the quality of feature matching and homography estimation on challenging benchmarks over the state-of-the-art.

</details>

### Contrastive Learning of Structured World Models.
- **链接**: [arXiv:1911.12247](https://arxiv.org/abs/1911.12247)
- **作者**: Thomas N. Kipf, Elise van der Pol, Max Welling
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A structured understanding of our world in terms of objects, relations, and hierarchies is an important component of human cognition. Learning such a structured world model from raw sensory data remains a challenge. As a step towards this goal, we introduce Contrastively-trained Structured World Models (C-SWMs). C-SWMs utilize a contrastive approach for representation learning in environments with compositional structure. We structure each state embedding as a set of object representations and their relations, modeled by a graph neural network. This allows objects to be discovered from raw pixel observations without direct supervision as part of the learning process. We evaluate C-SWMs on compositional environments involving multiple interacting objects that can be manipulated independently by an agent, simple Atari games, and a multi-object physics simulation. Our experiments demonstrate that C-SWMs can overcome limitations of models based on pixel reconstruction and outperform typical representatives of this model class in highly structured environments, while learning interpretable object-based representations.

</details>

### Cross-lingual Retrieval for Iterative Self-Supervised Training.
- **链接**: [arXiv:2006.09526](https://arxiv.org/abs/2006.09526)
- **作者**: Chau Tran, Yuqing Tang, Xian Li, Jiatao Gu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### PULSE: Self-Supervised Photo Upsampling via Latent Space Exploration of Generative Models. **⭐⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Menon_PULSE_Self-Supervised_Photo_Upsampling_via_Latent_Space_Exploration_of_Generative_CVPR_2020_paper.html) · 📚 被引 406
- **作者**: Sachit Menon, Alexandru Damian, Shijia Hu, Nikhil Ravi, Cynthia Rudin
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督图像超分辨率问题，即如何利用生成模型的潜空间实现高倍数上采样。②提出PULSE方法，通过在预训练GAN的潜空间中搜索与低分辨率图像下采样一致的潜在编码，生成高分辨率图像。③相比传统超分方法，不依赖成对训练数据，利用生成先验实现感知质量提升。④在面部图像上达到与现有方法相当或更好的感知质量，但保真度有限。
- **摘要（英）**: This paper addresses self-supervised image super-resolution by exploring the latent space of a pre-trained GAN. PULSE searches for latent codes that downscale to match the input low-resolution image, generating high-resolution outputs without paired training data. It achieves competitive perceptual quality on face images but with limited fidelity.
- **核心贡献**: 提出利用GAN潜空间搜索实现无配对数据的自监督超分辨率方法。
- **创新点**: 将超分问题转化为潜空间优化问题，利用生成先验。
- **结果**: 在面部图像上实现高感知质量超分，但保真度不足。

### Self-Supervised Learning of Pretext-Invariant Representations. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Misra_Self-Supervised_Learning_of_Pretext-Invariant_Representations_CVPR_2020_paper.html) · 📚 被引 935
- **作者**: Ishan Misra, Laurens van der Maaten
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督表示学习中预文本任务选择敏感的问题，即不同预文本任务导致表示质量差异大。②提出预文本不变表示学习（PIRL），通过构造预文本任务的等价变换，使表示对预文本任务不变。③相比SimCLR等对比方法，PIRL更关注任务不变性而非增强不变性，提升表示泛化性。④在ImageNet线性评估和下游任务上优于多种自监督方法。
- **摘要（英）**: This paper tackles the sensitivity of self-supervised representations to pretext task choice. PIRL learns representations invariant to pretext task transformations, improving generalization over contrastive methods like SimCLR. It achieves superior linear evaluation and downstream task performance on ImageNet.
- **核心贡献**: 提出预文本不变表示学习框架，增强自监督表示的泛化性。
- **创新点**: 引入任务不变性作为自监督学习的新目标。
- **结果**: 在ImageNet上线性评估和下游任务优于现有自监督方法。

### Just Go With the Flow: Self-Supervised Scene Flow Estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Mittal_Just_Go_With_the_Flow_Self-Supervised_Scene_Flow_Estimation_CVPR_2020_paper.html) · 📚 被引 122
- **作者**: Himangi Mittal, Brian Okorn, David Held
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对场景流估计依赖大量标注数据的问题，即真实场景流标注昂贵且难以获取。②提出自监督场景流估计方法，利用点云序列的刚性运动一致性和局部几何约束作为监督信号。③相比监督方法，无需标注即可训练，且利用多帧一致性提升鲁棒性。④在FlyingThings3D和KITTI上达到与监督方法相当的性能，且泛化性更好。
- **摘要（英）**: This paper addresses the scarcity of labeled scene flow data by proposing a self-supervised method that leverages rigid motion consistency and local geometric constraints in point cloud sequences. It trains without annotations and achieves performance comparable to supervised methods on FlyingThings3D and KITTI, with better generalization.
- **核心贡献**: 提出无需标注的自监督场景流估计方法，利用几何一致性。
- **创新点**: 将刚性运动先验作为自监督信号，替代人工标注。
- **结果**: 在多个数据集上达到与监督方法相当的性能。

### Self-Supervised Viewpoint Learning From Image Collections. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Mustikovela_Self-Supervised_Viewpoint_Learning_From_Image_Collections_CVPR_2020_paper.html) · 📚 被引 26
- **作者**: Siva Karthik Mustikovela, Varun Jampani, Shalini De Mello, Sifei Liu, Umar Iqbal, Carsten Rother et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对从图像集合中学习视角表示的问题，即无标注时如何估计物体视角。②提出自监督视角学习方法，通过重建图像和视角一致性约束训练编码器。③相比监督方法，无需视角标注，利用多视图一致性提升视角估计准确性。④在合成和真实数据集上验证了方法的有效性，但精度低于监督方法。
- **摘要（英）**: This paper tackles viewpoint estimation from unlabeled image collections by proposing a self-supervised method that trains an encoder via image reconstruction and viewpoint consistency. It avoids annotation and improves accuracy with multi-view consistency, though underperforming supervised methods.
- **核心贡献**: 提出自监督视角学习方法，利用重建和一致性约束。
- **创新点**: 将视角估计转化为自监督重建任务。
- **结果**: 在多个数据集上验证有效性，但精度有限。

### A Self-supervised Approach for Adversarial Robustness. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2006.04924](https://arxiv.org/abs/2006.04924) · 📚 被引 260
- **作者**: Muzammal Naseer, Salman H. Khan, Munawar Hayat, Fahad Shahbaz Khan, Fatih Porikli
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对对抗样本防御缺乏泛化性的问题，即现有防御方法难以应对未知攻击。②提出自监督对抗训练机制，在输入空间进行防御，结合对抗训练和输入处理。③相比传统对抗训练，该方法可跨任务泛化，且作为即插即用模块保护多种视觉系统。④在分类任务上，将平移不变集成攻击成功率从82.6%降至31.9%，优于现有最先进方法。
- **摘要（英）**: This paper addresses the lack of generalization in adversarial defenses by proposing a self-supervised adversarial training mechanism in input space. It combines adversarial training and input processing, offering cross-task protection and plug-and-play deployment. It reduces translation-invariant ensemble attack success from 82.6% to 31.9% on classification.
- **核心贡献**: 提出自监督对抗训练方法，提升防御的泛化性和可移植性。
- **创新点**: 在输入空间进行自监督对抗训练，实现跨任务防御。
- **结果**: 显著降低未知攻击成功率，优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial examples can cause catastrophic mistakes in Deep Neural Network (DNNs) based vision systems e.g., for classification, segmentation and object detection. The vulnerability of DNNs against such attacks can prove a major roadblock towards their real-world deployment. Transferability of adversarial examples demand generalizable defenses that can provide cross-task protection. Adversarial training that enhances robustness by modifying target model's parameters lacks such generalizability. On the other hand, different input processing based defenses fall short in the face of continuously evolving attacks. In this paper, we take the first step to combine the benefits of both approaches and propose a self-supervised adversarial training mechanism in the input space. By design, our defense is a generalizable approach and provides significant robustness against the \textbf{unseen} adversarial attacks (\eg by reducing the success rate of translation-invariant \textbf{ensemble} attack from 82.6\% to 31.9\% in comparison to previous state-of-the-art). It can be deployed as a plug-and-play solution to protect a variety of vision systems, as we demonstrate for the case of classification, segmentation and detection. Code is available at: {\small\url{https://github.com/Muzammal-Naseer/NRP}}.

</details>

### How Useful Is Self-Supervised Pretraining for Visual Tasks? **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2003.14323](https://arxiv.org/abs/2003.14323) · 📚 被引 82
- **作者**: Alejandro Newell, Jia Deng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督预训练在实际应用中的效用问题，即不同算法在不同任务和数据集上的表现差异。②通过合成数据集和多种下游任务，系统评估多种自监督算法，控制数据难度和标签数量。③相比以往研究，提供了更全面的实证分析，揭示线性评估与微调性能不相关。④发现自监督效用随标签数量增加而下降，且受任务和数据属性影响。
- **摘要（英）**: This paper investigates the utility of self-supervised pretraining across synthetic datasets and downstream tasks. It systematically evaluates multiple algorithms, revealing that utility decreases with label availability and varies by task and data properties. It also finds linear evaluation does not correlate with finetuning performance.
- **核心贡献**: 系统评估自监督预训练在不同条件下的效用，提供实证见解。
- **创新点**: 利用合成数据实现可控实验，揭示关键影响因素。
- **结果**: 发现线性评估与微调不相关，指导实践选择。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances have spurred incredible progress in self-supervised pretraining for vision. We investigate what factors may play a role in the utility of these pretraining methods for practitioners. To do this, we evaluate various self-supervised algorithms across a comprehensive array of synthetic datasets and downstream tasks. We prepare a suite of synthetic data that enables an endless supply of annotated images as well as full control over dataset difficulty. Our experiments offer insights into how the utility of self-supervision changes as the number of available labels grows as well as how the utility changes as a function of the downstream task and the properties of the training data. We also find that linear evaluation does not correlate with finetuning performance. Code and data is available at \href{https://www.github.com/princeton-vl/selfstudy}{github.com/princeton-vl/selfstudy}.

</details>

### Fast(er) Reconstruction of Shredded Text Documents via Self-Supervised Deep Asymmetric Metric Learning. **⭐⭐** (相关度: 10%)
- **链接**: [arXiv:2003.10063](https://arxiv.org/abs/2003.10063) · 📚 被引 7
- **作者**: Thiago M. Paixão, Rodrigo Ferreira Berriel, Maria C. S. Boeres, Alessandro L. Koerich, Claudine Badue, Alberto F. De Souza et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①该论文针对机械碎纸文档自动重建中，成对碎片兼容性评估计算成本高的问题，传统深度模型需要对每对碎片进行推理，导致计算量随碎片数量呈二次方增长。②提出了一种可扩展的深度学习方法，通过自监督深度非对称度量学习，将碎片内容投影到公共度量空间，使推理次数从二次方降至线性。③相比现有方法，该方法不直接预测兼容性，而是利用非对称投影学习嵌入表示，显著降低了计算复杂度。④实验表明，该方法在保持重建精度的同时，大幅减少了推理开销，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the high computational cost of pairwise compatibility evaluation in shredded document reconstruction, where deep models require inference for each pair, leading to quadratic scaling. It proposes a scalable deep learning approach using self-supervised asymmetric metric learning to project shred content into a common space, reducing inference to linear scaling. The method improves efficiency over existing approaches while maintaining reconstruction accuracy, though specific quantitative results are not detailed in the abstract.
- **核心贡献**: 提出了一种线性扩展的碎片兼容性评估方法，通过非对称度量学习替代逐对推理。
- **创新点**: 利用自监督非对称投影将碎片映射到公共度量空间，避免二次方推理。
- **结果**: 推理次数从二次方降至线性，同时保持重建精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The reconstruction of shredded documents consists in arranging the pieces of paper (shreds) in order to reassemble the original aspect of such documents. This task is particularly relevant for supporting forensic investigation as documents may contain criminal evidence. As an alternative to the laborious and time-consuming manual process, several researchers have been investigating ways to perform automatic digital reconstruction. A central problem in automatic reconstruction of shredded documents is the pairwise compatibility evaluation of the shreds, notably for binary text documents. In this context, deep learning has enabled great progress for accurate reconstructions in the domain of mechanically-shredded documents. A sensitive issue, however, is that current deep model solutions require an inference whenever a pair of shreds has to be evaluated. This work proposes a scalable deep learning approach for measuring pairwise compatibility in which the number of inferences scales linearly (rather than quadratically) with the number of shreds. Instead of predicting compatibility directly, deep models are leveraged to asymmetrically project the raw shred content onto a common metric space in which distance is proportional to the compatibility. Experimental results show that our method has accuracy comparable to the state-of-the-art with a speed-up of about 22 times for a test instance with 505 shreds (20 mixed shredded-pages from different documents).

</details>

### Self-Supervised Human Depth Estimation From Monocular Videos.
- **链接**: [arXiv:2005.03358](https://arxiv.org/abs/2005.03358) · 📚 被引 24
- **作者**: Feitong Tan, Hao Zhu, Zhaopeng Cui, Siyu Zhu, Marc Pollefeys, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous methods on estimating detailed human depth often require supervised training with `ground truth' depth data. This paper presents a self-supervised method that can be trained on YouTube videos without known depth, which makes training data collection simple and improves the generalization of the learned network. The self-supervised learning is achieved by minimizing a photo-consistency loss, which is evaluated between a video frame and its neighboring frames warped according to the estimated depth and the 3D non-rigid motion of the human body. To solve this non-rigid motion, we first estimate a rough SMPL model at each video frame and compute the non-rigid body motion accordingly, which enables self-supervised learning on estimating the shape details. Experiments demonstrate that our method enjoys better generalization and performs much better on data in the wild.

</details>

### Self-Supervised Human Depth Estimation From Monocular Videos.
- **链接**: [arXiv:2005.03358](https://arxiv.org/abs/2005.03358) · 📚 被引 24
- **作者**: Feitong Tan, Hao Zhu, Zhaopeng Cui, Siyu Zhu, Marc Pollefeys, Ping Tan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous methods on estimating detailed human depth often require supervised training with `ground truth' depth data. This paper presents a self-supervised method that can be trained on YouTube videos without known depth, which makes training data collection simple and improves the generalization of the learned network. The self-supervised learning is achieved by minimizing a photo-consistency loss, which is evaluated between a video frame and its neighboring frames warped according to the estimated depth and the 3D non-rigid motion of the human body. To solve this non-rigid motion, we first estimate a rough SMPL model at each video frame and compute the non-rigid body motion accordingly, which enables self-supervised learning on estimating the shape details. Experiments demonstrate that our method enjoys better generalization and performs much better on data in the wild.

</details>

### Joint Contrastive Learning with Infinite Possibilities.
- **链接**: [arXiv:2009.14776](https://arxiv.org/abs/2009.14776)
- **作者**: Qi Cai, Yu Wang, Yingwei Pan, Ting Yao, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Domain-Aware Generative Network for Generalized Zero-Shot Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wu_Self-Supervised_Domain-Aware_Generative_Network_for_Generalized_Zero-Shot_Learning_CVPR_2020_paper.html) · 📚 被引 54
- **作者**: Jiamin Wu, Tianzhu Zhang, Zheng-Jun Zha, Jiebo Luo, Yongdong Zhang, Feng Wu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Video Playback Rate Perception for Self-Supervised Spatio-Temporal Representation Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Yao_Video_Playback_Rate_Perception_for_Self-Supervised_Spatio-Temporal_Representation_Learning_CVPR_2020_paper.html)
- **作者**: Yuan Yao, Chang Liu, Dezhao Luo, Yu Zhou, Qixiang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Self-Supervised Scene De-Occlusion.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhan_Self-Supervised_Scene_De-Occlusion_CVPR_2020_paper.html)
- **作者**: Xiaohang Zhan, Xingang Pan, Bo Dai, Ziwei Liu, Dahua Lin, Chen Change Loy
- **🏷️ 机构**: Shanghai AI Lab, CUHK
- **会议**: CVPR 2020

### Look-Into-Object: Self-Supervised Structure Modeling for Object Recognition.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhou_Look-Into-Object_Self-Supervised_Structure_Modeling_for_Object_Recognition_CVPR_2020_paper.html) · 📚 被引 73
- **作者**: Mohan Zhou, Yalong Bai, Wei Zhang, Tiejun Zhao, Tao Mei
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### S3VAE: Self-Supervised Sequential VAE for Representation Disentanglement and Data Generation.
- **链接**: [arXiv:2005.11437](https://arxiv.org/abs/2005.11437) · 📚 被引 60
- **作者**: Yizhe Zhu, Martin Renqiang Min, Asim Kadav, Hans Peter Graf
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a sequential variational autoencoder to learn disentangled representations of sequential data (e.g., videos and audios) under self-supervision. Specifically, we exploit the benefits of some readily accessible supervisory signals from input data itself or some off-the-shelf functional models and accordingly design auxiliary tasks for our model to utilize these signals. With the supervision of the signals, our model can easily disentangle the representation of an input sequence into static factors and dynamic factors (i.e., time-invariant and time-varying parts). Comprehensive experiments across videos and audios verify the effectiveness of our model on representation disentanglement and generation of sequential data, and demonstrate that, our model with self-supervision performs comparable to, if not better than, the fully-supervised model with ground truth labels, and outperforms state-of-the-art unsupervised models by a large margin.

</details>

### Disentangled and Controllable Face Image Generation via 3D Imitative-Contrastive Learning.
- **链接**: [arXiv:2004.11660](https://arxiv.org/abs/2004.11660) · 📚 被引 287
- **作者**: Yu Deng, Jiaolong Yang, Dong Chen, Fang Wen, Xin Tong
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose DiscoFaceGAN, an approach for face image generation of virtual people with disentangled, precisely-controllable latent representations for identity of non-existing people, expression, pose, and illumination. We embed 3D priors into adversarial learning and train the network to imitate the image formation of an analytic 3D face deformation and rendering process. To deal with the generation freedom induced by the domain gap between real and rendered faces, we further introduce contrastive learning to promote disentanglement by comparing pairs of generated images. Experiments show that through our imitative-contrastive learning, the factor variations are very well disentangled and the properties of a generated face can be precisely controlled. We also analyze the learned latent space and present several meaningful properties supporting factor disentanglement. Our method can also be used to embed real images into the disentangled latent space. We hope our method could provide new understandings of the relationship between physical properties and deep image synthesis.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose DiscoFaceGAN, an approach for face image generation of virtual people with disentangled, precisely-controllable latent representations for identity of non-existing people, expression, pose, and illumination. We embed 3D priors into adversarial learning and train the network to imitate the image formation of an analytic 3D face deformation and rendering process. To deal with the generation freedom induced by the domain gap between real and rendered faces, we further introduce contrastive learning to promote disentanglement by comparing pairs of generated images. Experiments show that through our imitative-contrastive learning, the factor variations are very well disentangled and the properties of a generated face can be precisely controlled. We also analyze the learned latent space and present several meaningful properties supporting factor disentanglement. Our method can also be used to embed real images into the disentangled latent space. We hope our method could provide new understandings of the relationship between physical properties and deep image synthesis.

</details>

## 跨领域论文（完整笔记在其他领域）

- 3D Packing for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Exploit Clues From Views: Self-Supervised and Regularized Learning for Multiview Object Recognition. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- On the Uncertainty of Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)

## 🆕 增量新增

### Vision-Language Navigation With Self-Supervised Auxiliary Reasoning Tasks. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:1911.07883](https://arxiv.org/abs/1911.07883) · 📚 被引 161
- **作者**: Fengda Zhu, Yi Zhu, Xiaojun Chang, Xiaodan Liang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对视觉语言导航（VLN）任务中智能体忽略环境隐含语义信息（如导航图、子轨迹语义）的问题。②提出了AuxRN框架，包含四个自监督辅助推理任务：解释先前动作、估计导航进度、预测下一朝向、评估轨迹一致性，以利用额外训练信号。③相比现有跨模态方法，通过辅助任务增强语义表示学习，使智能体能推理自身活动并全面感知环境。④实验表明辅助推理任务显著提升了导航性能，但摘要未提供具体数据。
- **摘要（英）**: This paper addresses the VLN task by introducing AuxRN, a framework with four self-supervised auxiliary reasoning tasks to exploit implicit semantic information in environments. It improves semantic representation learning and navigation performance, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出自监督辅助推理任务框架AuxRN，增强VLN智能体的语义推理能力。
- **创新点**: 设计四个自监督辅助任务，从多角度挖掘环境语义信息。
- **结果**: 实验显示辅助推理任务提升导航性能，但无具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation (VLN) is a task where agents learn to navigate following natural language instructions. The key to this task is to perceive both the visual scene and natural language sequentially. Conventional approaches exploit the vision and language features in cross-modal grounding. However, the VLN task remains challenging, since previous works have neglected the rich semantic information contained in the environment (such as implicit navigation graphs or sub-trajectory semantics). In this paper, we introduce Auxiliary Reasoning Navigation (AuxRN), a framework with four self-supervised auxiliary reasoning tasks to take advantage of the additional training signals derived from the semantic information. The auxiliary tasks have four reasoning objectives: explaining the previous actions, estimating the navigation progress, predicting the next orientation, and evaluating the trajectory consistency. As a result, these additional training signals help the agent to acquire knowledge of semantic representations in order to reason about its activity and build a thorough perception of the environment. Our experiments indicate that auxiliary reasoning tasks improve both the performance of the main task and the model generalizability by a large margin. Empirically, we demonstrate that an agent trained with self-supervised auxiliary reasoning tasks substantially outperforms the previous state-of-the-art method, being the best existing approach on the standard benchmark.

</details>

### Action Segmentation With Joint Self-Supervised Temporal Domain Adaptation. **⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2003.02824](https://arxiv.org/abs/2003.02824) · 📚 被引 90
- **作者**: Min-Hung Chen, Baopu Li, Yingze Bao, Ghassan AlRegib, Zsolt Kira
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对动作分割中时空变化导致性能不佳的问题，不同人执行同一动作存在差异，而标注数据有限。②提出自监督时间域适应（SSTDA），将动作分割视为跨域问题，通过两个自监督辅助任务（二元和序列域预测）对齐嵌入局部和全局时间动态的跨域特征。③相比其他域适应方法，SSTDA利用自监督信号更有效地减少域差异，无需额外标注。④在GTEA、50Salads和Breakfast数据集上，SSTDA大幅超越现有方法（如Breakfast上F1@25从59.6%提升至69.1%），且仅需65%的标注数据即可达到可比性能。
- **摘要（英）**: This paper addresses action segmentation under spatiotemporal variations by reformulating it as a cross-domain problem and proposing Self-Supervised Temporal Domain Adaptation (SSTDA) with two auxiliary tasks to align features. It outperforms state-of-the-art methods on GTEA, 50Salads, and Breakfast (e.g., F1@25 from 59.6% to 69.1% on Breakfast) and requires only 65% of labeled data.
- **核心贡献**: 提出自监督时间域适应方法，利用未标注视频提升动作分割性能。
- **创新点**: 设计二元和序列域预测任务，联合对齐局部和全局时间动态。
- **结果**: 在三个基准数据集上大幅超越现有方法，且数据效率高。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent progress of fully-supervised action segmentation techniques, the performance is still not fully satisfactory. One main challenge is the problem of spatiotemporal variations (e.g. different people may perform the same activity in various ways). Therefore, we exploit unlabeled videos to address this problem by reformulating the action segmentation task as a cross-domain problem with domain discrepancy caused by spatio-temporal variations. To reduce the discrepancy, we propose Self-Supervised Temporal Domain Adaptation (SSTDA), which contains two self-supervised auxiliary tasks (binary and sequential domain prediction) to jointly align cross-domain feature spaces embedded with local and global temporal dynamics, achieving better performance than other Domain Adaptation (DA) approaches. On three challenging benchmark datasets (GTEA, 50Salads, and Breakfast), SSTDA outperforms the current state-of-the-art method by large margins (e.g. for the F1@25 score, from 59.6% to 69.1% on Breakfast, from 73.4% to 81.5% on 50Salads, and from 83.6% to 89.1% on GTEA), and requires only 65% of the labeled training data for comparable performance, demonstrating the usefulness of adapting to unlabeled target videos across variations. The source code is available at https://github.com/cmhungsteve/SSTDA.

</details>

### SG-NN: Sparse Generative Neural Networks for Self-Supervised Scene Completion of RGB-D Scans. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Dai_SG-NN_Sparse_Generative_Neural_Networks_for_Self-Supervised_Scene_Completion_of_CVPR_2020_paper.html) · 📚 被引 122
- **作者**: Angela Dai, Christian Diller, Matthias Nießner
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对RGB-D扫描的场景补全问题，传统方法依赖大量标注的3D数据，成本高昂。②提出稀疏生成神经网络（SG-NN），利用自监督学习从单次扫描中预测缺失区域，通过稀疏卷积和生成模型处理不完整输入。③相比监督方法，SG-NN无需完整标注，利用扫描数据的内在结构进行训练，提高了泛化能力。④在合成和真实数据集上（如ScanNet）展示了有效的补全结果，但摘要中未提供具体数值。
- **摘要（英）**: This paper addresses scene completion from RGB-D scans using a sparse generative neural network (SG-NN) trained in a self-supervised manner, avoiding the need for dense annotations. It leverages sparse convolutions and generative modeling to predict missing regions, showing effective results on datasets like ScanNet.
- **核心贡献**: 提出自监督稀疏生成网络用于RGB-D场景补全。
- **创新点**: 结合稀疏卷积与生成模型，实现无标注训练。
- **结果**: 在ScanNet等数据集上验证了有效性。

### Self-Supervised Deep Visual Odometry With Online Adaptation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2005.06136](https://arxiv.org/abs/2005.06136) · 📚 被引 64
- **作者**: Shunkai Li, Xin Wang, Yingdian Cao, Fei Xue, Zike Yan, Hongbin Zha
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对自监督视觉里程计在场景变化时性能下降的问题。②提出在线元学习算法，利用convLSTM聚合时空信息，使网络能持续适应新环境，并通过在线特征对齐方法处理环境变化。③相比现有方法，该网络能无缝适应不同环境，如虚拟到真实、室外到室内。④在未见过的室外场景、虚拟到真实和室外到室内等实验中，方法一致优于最先进的自监督VO方法。
- **摘要（英）**: This paper addresses the performance degradation of self-supervised visual odometry in novel scenes by proposing an online meta-learning algorithm with convLSTM for spatial-temporal aggregation and online feature alignment. The network adapts to new environments seamlessly, and experiments on unseen outdoor, virtual-to-real, and outdoor-to-indoor scenes show consistent improvements over state-of-the-art methods.
- **核心贡献**: 提出在线元学习算法，使自监督VO网络能持续适应新环境。
- **创新点**: 结合convLSTM和在线特征对齐，实现环境自适应。
- **结果**: 在多种场景迁移实验中优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised VO methods have shown great success in jointly estimating camera pose and depth from videos. However, like most data-driven methods, existing VO networks suffer from a notable decrease in performance when confronted with scenes different from the training data, which makes them unsuitable for practical applications. In this paper, we propose an online meta-learning algorithm to enable VO networks to continuously adapt to new environments in a self-supervised manner. The proposed method utilizes convolutional long short-term memory (convLSTM) to aggregate rich spatial-temporal information in the past. The network is able to memorize and learn from its past experience for better estimation and fast adaptation to the current frame. When running VO in the open world, in order to deal with the changing environment, we propose an online feature alignment method by aligning feature distributions at different time. Our VO network is able to seamlessly adapt to different environments. Extensive experiments on unseen outdoor scenes, virtual to real world and outdoor to indoor environments demonstrate that our method consistently outperforms state-of-the-art self-supervised VO baselines considerably.

</details>

### Sketch-BERT: Learning Sketch Bidirectional Encoder Representation From Transformers by Self-Supervised Learning of Sketch Gestalt. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2005.09159](https://arxiv.org/abs/2005.09159) · 📚 被引 57
- **作者**: Hangyu Lin, Yanwei Fu, Xiangyang Xue, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对草图理解中像素格式表示和CNN模型的局限性，以及SketchRNN表示仅适用于生成任务的问题。②提出Sketch-BERT模型，将BERT泛化到草图领域，包括新设计的草图嵌入网络和自监督的草图格式塔学习。③通过草图格式塔模型（SGM）辅助预训练，提升草图表示在下游任务中的性能。④实验表明，Sketch-BERT学习到的表示能改善草图识别和检索等下游任务的性能。
- **摘要（英）**: This paper addresses the limitations of pixel-based sketch understanding and the generative-only representation of SketchRNN by proposing Sketch-BERT, which adapts BERT to sketches with novel embedding networks and self-supervised sketch gestalt learning. The Sketch Gestalt Model aids pre-training, and experiments show improved performance on downstream tasks like recognition and retrieval.
- **核心贡献**: 提出Sketch-BERT模型，实现草图的双向编码器表示学习。
- **创新点**: 将BERT架构和自监督格式塔学习引入草图理解。
- **结果**: 在草图识别和检索任务上提升了性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous researches of sketches often considered sketches in pixel format and leveraged CNN based models in the sketch understanding. Fundamentally, a sketch is stored as a sequence of data points, a vector format representation, rather than the photo-realistic image of pixels. SketchRNN studied a generative neural representation for sketches of vector format by Long Short Term Memory networks (LSTM). Unfortunately, the representation learned by SketchRNN is primarily for the generation tasks, rather than the other tasks of recognition and retrieval of sketches. To this end and inspired by the recent BERT model, we present a model of learning Sketch Bidirectional Encoder Representation from Transformer (Sketch-BERT). We generalize BERT to sketch domain, with the novel proposed components and pre-training algorithms, including the newly designed sketch embedding networks, and the self-supervised learning of sketch gestalt. Particularly, towards the pre-training task, we present a novel Sketch Gestalt Model (SGM) to help train the Sketch-BERT. Experimentally, we show that the learned representation of Sketch-BERT can help and improve the performance of the downstream tasks of sketch recognition, sketch retrieval, and sketch gestalt.

</details>

### Flow2Stereo: Effective Self-Supervised Learning of Optical Flow and Stereo Matching. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_Flow2Stereo_Effective_Self-Supervised_Learning_of_Optical_Flow_and_Stereo_Matching_CVPR_2020_paper.html) · 📚 被引 60
- **作者**: Pengpeng Liu, Irwin King, Michael R. Lyu, Jia Xu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对光流和立体匹配的自监督学习效率问题。②提出Flow2Stereo方法，通过有效结合光流和立体匹配的自监督学习，利用几何一致性约束。③相比单独学习，该方法能共享特征和互补信息，提升学习效率。④摘要未提供具体数据，但预期在光流和立体匹配基准上表现优异。
- **摘要（英）**: This paper addresses the efficiency of self-supervised learning for optical flow and stereo matching by proposing Flow2Stereo, which combines both tasks with geometric consistency constraints. It shares features and complementary information to improve learning efficiency, though specific results are not detailed in the abstract.
- **核心贡献**: 提出Flow2Stereo方法，联合自监督学习光流和立体匹配。
- **创新点**: 利用几何一致性约束实现任务间的互补学习。
- **结果**: 预期在相关基准上提升性能。

### Self-Supervised Learning of Video-Induced Visual Invariances.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Tschannen_Self-Supervised_Learning_of_Video-Induced_Visual_Invariances_CVPR_2020_paper.html) · 📚 被引 34
- **作者**: Michael Tschannen, Josip Djolonga, Marvin Ritter, Aravindh Mahendran, Neil Houlsby, Sylvain Gelly et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Improving Object Detection with Selective Self-supervised Self-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58526-6_35)
- **作者**: Yandong Li, Di Huang, Danfeng Qin, Liqiang Wang, Boqing Gong
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Adversarial Self-supervised Learning for Semi-supervised 3D Action Recognition.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58571-6_3)
- **作者**: Chenyang Si, Xuecheng Nie, Wei Wang, Liang Wang, Tieniu Tan, Jiashi Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Self-Supervised Learning of Appliance Usage.
- **链接**: [出版页](https://openreview.net/forum?id=B1lJzyStvS)
- **作者**: Chen-Yu Hsu, Abbas Zeitoun, Guang-He Lee, Dina Katabi, Tommi S. Jaakkola
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### vq-wav2vec: Self-Supervised Learning of Discrete Speech Representations.
- **链接**: [出版页](https://openreview.net/forum?id=rylwJxrYDS)
- **作者**: Alexei Baevski, Steffen Schneider, Michael Auli
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### From Inference to Generation: End-to-end Fully Self-supervised Generation of Human Face from Speech.
- **链接**: [出版页](https://openreview.net/forum?id=H1guaREYPr)
- **作者**: Hyeong-Seok Choi, Changdae Park, Kyogu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### Semantically-Guided Representation Learning for Self-Supervised Monocular Depth.
- **链接**: [出版页](https://openreview.net/forum?id=ByxT7TNFvH)
- **作者**: Vitor Guizilini, Rui Hou, Jie Li, Rares Ambrus, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### ALBERT: A Lite BERT for Self-supervised Learning of Language Representations.
- **链接**: [出版页](https://openreview.net/forum?id=H1eA7AEtvS)
- **作者**: Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### InfoGAN-CR and ModelCentrality: Self-supervised Model Training and Selection for Disentangling GANs.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lin20e.html)
- **作者**: Zinan Lin, Kiran Koshy Thekumparampil, Giulia Fanti, Sewoong Oh
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Self-supervised Label Augmentation via Input Transformations.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lee20c.html)
- **作者**: Hankook Lee, Sung Ju Hwang, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Learning Compound Tasks without Task-specific Knowledge via Imitation and Self-supervised Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v119/lee20f.html)
- **作者**: Sang-Hyun Lee, Seung-Woo Seo
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Automatic Shortcut Removal for Self-Supervised Representation Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v119/minderer20a.html)
- **作者**: Matthias Minderer, Olivier Bachem, Neil Houlsby, Michael Tschannen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Skew-Fit: State-Covering Self-Supervised Reinforcement Learning.
- **链接**: [出版页](http://proceedings.mlr.press/v119/pong20a.html)
- **作者**: Vitchyr Pong, Murtaza Dalal, Steven Lin, Ashvin Nair, Shikhar Bahl, Sergey Levine
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Graph-based, Self-Supervised Program Repair from Diagnostic Feedback.
- **链接**: [出版页](http://proceedings.mlr.press/v119/yasunaga20a.html)
- **作者**: Michihiro Yasunaga, Percy Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### A Simple Framework for Contrastive Learning of Visual Representations.
- **链接**: [出版页](http://proceedings.mlr.press/v119/chen20j.html)
- **作者**: Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey E. Hinton
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### On Contrastive Learning for Likelihood-free Inference.
- **链接**: [出版页](http://proceedings.mlr.press/v119/durkan20a.html)
- **作者**: Conor Durkan, Iain Murray, George Papamakarios
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2020

### Self-Supervised Few-Shot Learning on Point Clouds.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/50c1f44e426560f3f2cdcb3e19e39903-Abstract.html)
- **作者**: Charu Sharma, Manohar Kaul
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

## 跨领域论文（完整笔记在其他领域）

- 3D Packing for Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Exploit Clues From Views: Self-Supervised and Regularized Learning for Multiview Object Recognition. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- On the Uncertainty of Self-Supervised Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Multi-Modal Domain Adaptation for Fine-Grained Action Recognition. → [multimodal](../multimodal/Guideline%202020.md)
- Monocular Differentiable Rendering for Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Forget About the LiDAR: Self-Supervised Depth Estimators with MED Probability Volumes. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)

<!-- COMPLETE v1 papers=56 -->
