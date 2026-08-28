# Self-supervised Vision — 2020 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Supervised Monocular Trained Depth Estimation Using Self-Attention and Discrete Disparity Volume.
- **链接**: [arXiv:2003.13951](https://arxiv.org/abs/2003.13951) · 📚 被引 231
- **作者**: Adrian Johnston, Gustavo Carneiro
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation has become one of the most studied applications in computer vision, where the most accurate approaches are based on fully supervised learning models. However, the acquisition of accurate and large ground truth data sets to model these fully supervised methods is a major challenge for the further development of the area. Self-supervised methods trained with monocular videos constitute one the most promising approaches to mitigate the challenge mentioned above due to the wide-spread availability of training data. Consequently, they have been intensively studied, where the main ideas explored consist of different types of model architectures, loss functions, and occlusion masks to address non-rigid motion. In this paper, we propose two new ideas to improve self-supervised monocular trained depth estimation: 1) self-attention, and 2) discrete disparity prediction. Compared with the usual localised convolution operation, self-attention can explore a more general contextual information that allows the inference of similar disparity values at non-contiguous regions of the image. Discrete disparity prediction has been shown by fully supervised methods to provide a more robust and sharper depth estimation than the more common continuous disparity prediction, besides enabling the estimation of depth uncertainty. We show that the extension of the state-of-the-art self-supervised monocular trained depth estimator Monodepth2 with these two ideas allows us to design a model that produces the best results in the field in KITTI 2015 and Make3D, closing the gap with respect self-supervised stereo training and fully supervised approaches.

</details>

</details>

### Contrastive Learning for Weakly Supervised Phrase Grounding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58580-8_44)
- **作者**: Tanmay Gupta, Arash Vahdat, Gal Chechik, Xiaodong Yang, Jan Kautz, Derek Hoiem
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous methods on estimating detailed human depth often require supervised training with `ground truth' depth data. This paper presents a self-supervised method that can be trained on YouTube videos without known depth, which makes training data collection simple and improves the generalization of the learned network. The self-supervised learning is achieved by minimizing a photo-consistency loss, which is evaluated between a video frame and its neighboring frames warped according to the estimated depth and the 3D non-rigid motion of the human body. To solve this non-rigid motion, we first estimate a rough SMPL model at each video frame and compute the non-rigid body motion accordingly, which enables self-supervised learning on estimating the shape details. Experiments demonstrate that our method enjoys better generalization and performs much better on data in the wild.

</details>

</details>

### wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations.
- **链接**: [arXiv:2006.11477](https://arxiv.org/abs/2006.11477)
- **作者**: Alexei Baevski, Yuhao Zhou, Abdelrahman Mohamed, Michael Auli
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Self2Self With Dropout: Learning Self-Supervised Denoising From Single Image.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Quan_Self2Self_With_Dropout_Learning_Self-Supervised_Denoising_From_Single_Image_CVPR_2020_paper.html) · 📚 被引 381
- **作者**: Yuhui Quan, Mingqin Chen, Tongyao Pang, Hui Ji
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Self-Supervised Equivariant Attention Mechanism for Weakly Supervised Semantic Segmentation.
- **链接**: [arXiv:2004.04581](https://arxiv.org/abs/2004.04581) · 📚 被引 668
- **作者**: Yude Wang, Jie Zhang, Meina Kan, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-level weakly supervised semantic segmentation is a challenging problem that has been deeply studied in recent years. Most of advanced solutions exploit class activation map (CAM). However, CAMs can hardly serve as the object mask due to the gap between full and weak supervisions. In this paper, we propose a self-supervised equivariant attention mechanism (SEAM) to discover additional supervision and narrow the gap. Our method is based on the observation that equivariance is an implicit constraint in fully supervised semantic segmentation, whose pixel-level labels take the same spatial transformation as the input images during data augmentation. However, this constraint is lost on the CAMs trained by image-level supervision. Therefore, we propose consistency regularization on predicted CAMs from various transformed images to provide self-supervision for network learning. Moreover, we propose a pixel correlation module (PCM), which exploits context appearance information and refines the prediction of current pixel by its similar neighbors, leading to further improvement on CAMs consistency. Extensive experiments on PASCAL VOC 2012 dataset demonstrate our method outperforms state-of-the-art methods using the same level of supervision. The code is released online.

</details>

### Adversarial Robustness: From Self-Supervised Pre-Training to Fine-Tuning.
- **链接**: [arXiv:2003.12862](https://arxiv.org/abs/2003.12862) · [代码](https://github.com/TAMU-VITA/Adv-SS-Pretraining) · 📚 被引 132
- **作者**: Tianlong Chen, Sijia Liu, Shiyu Chang, Yu Cheng, Lisa Amini, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained models from self-supervision are prevalently used in fine-tuning downstream tasks faster or for better accuracy. However, gaining robustness from pretraining is left unexplored. We introduce adversarial training into self-supervision, to provide general-purpose robust pre-trained models for the first time. We find these robust pre-trained models can benefit the subsequent fine-tuning in two ways: i) boosting final model robustness; ii) saving the computation cost, if proceeding towards adversarial fine-tuning. We conduct extensive experiments to demonstrate that the proposed framework achieves large performance margins (eg, 3.83% on robust accuracy and 1.3% on standard accuracy, on the CIFAR-10 dataset), compared with the conventional end-to-end adversarial training baseline. Moreover, we find that different self-supervised pre-trained models have a diverse adversarial vulnerability. It inspires us to ensemble several pretraining tasks, which boosts robustness more. Our ensemble strategy contributes to a further improvement of 3.59% on robust accuracy, while maintaining a slightly higher standard accuracy on CIFAR-10. Our codes are available at https://github.com/TAMU-VITA/Adv-SS-Pretraining.

</details>

### Action Segmentation With Joint Self-Supervised Temporal Domain Adaptation.
- **链接**: [arXiv:2003.02824](https://arxiv.org/abs/2003.02824) · [代码](https://github.com/cmhungsteve/SSTDA) · 📚 被引 90
- **作者**: Min-Hung Chen, Baopu Li, Yingze Bao, Ghassan AlRegib, Zsolt Kira
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent progress of fully-supervised action segmentation techniques, the performance is still not fully satisfactory. One main challenge is the problem of spatiotemporal variations (e.g. different people may perform the same activity in various ways). Therefore, we exploit unlabeled videos to address this problem by reformulating the action segmentation task as a cross-domain problem with domain discrepancy caused by spatio-temporal variations. To reduce the discrepancy, we propose Self-Supervised Temporal Domain Adaptation (SSTDA), which contains two self-supervised auxiliary tasks (binary and sequential domain prediction) to jointly align cross-domain feature spaces embedded with local and global temporal dynamics, achieving better performance than other Domain Adaptation (DA) approaches. On three challenging benchmark datasets (GTEA, 50Salads, and Breakfast), SSTDA outperforms the current state-of-the-art method by large margins (e.g. for the F1@25 score, from 59.6% to 69.1% on Breakfast, from 73.4% to 81.5% on 50Salads, and from 83.6% to 89.1% on GTEA), and requires only 65% of the labeled training data for comparable performance, demonstrating the usefulness of adapting to unlabeled target videos across variations. The source code is available at https://github.com/cmhungsteve/SSTDA.

</details>

### SG-NN: Sparse Generative Neural Networks for Self-Supervised Scene Completion of RGB-D Scans.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Dai_SG-NN_Sparse_Generative_Neural_Networks_for_Self-Supervised_Scene_Completion_of_CVPR_2020_paper.html) · 📚 被引 122
- **作者**: Angela Dai, Christian Diller, Matthias Nießner
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Discriminative Sounding Objects Localization via Self-supervised Audiovisual Matching.
- **链接**: [arXiv:2010.05466](https://arxiv.org/abs/2010.05466) · [代码](https://github.com/DTaoo/Discriminative-Sounding-Objects-Localization)
- **作者**: Di Hu, Rui Qian, Minyue Jiang, Xiao Tan, Shilei Wen, Errui Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene flow estimation has been receiving increasing attention for 3D environment perception. Monocular scene flow estimation -- obtaining 3D structure and 3D motion from two temporally consecutive images -- is a highly ill-posed problem, and practical solutions are lacking to date. We propose a novel monocular scene flow method that yields competitive accuracy and real-time performance. By taking an inverse problem view, we design a single convolutional neural network (CNN) that successfully estimates depth and 3D motion simultaneously from a classical optical flow cost volume. We adopt self-supervised learning with 3D loss functions and occlusion reasoning to leverage unlabeled data. We validate our design choices, including the proxy loss and augmentation setup. Our model achieves state-of-the-art accuracy among unsupervised/self-supervised learning approaches to monocular scene flow, and yields competitive results for the optical flow and monocular depth estimation sub-tasks. Semi-supervised fine-tuning further improves the accuracy and yields promising results in real-time.

</details>

</details>

### Self-supervised Auxiliary Learning with Meta-paths for Heterogeneous Graphs.
- **链接**: [arXiv:2007.08294](https://arxiv.org/abs/2007.08294)
- **作者**: Dasol Hwang, Jinyoung Park, Sunyoung Kwon, Kyung-Min Kim, Jung-Woo Ha, Hyunwoo J. Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph neural networks have shown superior performance in a wide range of applications providing a powerful representation of graph-structured data. Recent works show that the representation can be further improved by auxiliary tasks. However, the auxiliary tasks for heterogeneous graphs, which contain rich semantic information with various types of nodes and edges, have less explored in the literature. In this paper, to learn graph neural networks on heterogeneous graphs we propose a novel self-supervised auxiliary learning method using meta-paths, which are composite relations of multiple edge types. Our proposed method is learning to learn a primary task by predicting meta-paths as auxiliary tasks. This can be viewed as a type of meta-learning. The proposed method can identify an effective combination of auxiliary tasks and automatically balance them to improve the primary task. Our methods can be applied to any graph neural networks in a plug-in manner without manual labeling or additional data. The experiments demonstrate that the proposed method consistently improves the performance of link prediction and node classification on heterogeneous graphs.

</details>

### Adversarial Self-Supervised Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/1f1baa5b8edac74eb4eaa329f14a0361-Abstract.html)
- **作者**: Minseon Kim, Jihoon Tack, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel principle for self-supervised feature learning based on the discrimination of specific transformations of an image. We argue that the generalization capability of learned features depends on what image neighborhood size is sufficient to discriminate different image transformations: The larger the required neighborhood size and the more global the image statistics that the feature can describe. An accurate description of global image statistics allows to better represent the shape and configuration of objects and their context, which ultimately generalizes better to new tasks such as object classification and detection. This suggests a criterion to choose and design image transformations. Based on this criterion, we introduce a novel image transformation that we call limited context inpainting (LCI). This transformation inpaints an image patch conditioned only on a small rectangular pixel boundary (the limited context). Because of the limited boundary information, the inpainter can learn to match local pixel statistics, but is unlikely to match the global statistics of the image. We claim that the same principle can be used to justify the performance of transformations such as image rotations and warping. Indeed, we demonstrate experimentally that learning to discriminate transformations such as LCI, image warping and rotations, yields features with state of the art generalization capabilities on several datasets such as Pascal VOC, STL-10, CelebA, and ImageNet. Remarkably, our trained features achieve a performance on Places on par with features trained through supervised learning with ImageNet labels.

</details>

### Self-Supervised 3D Human Pose Estimation via Part Guided Novel Image Synthesis.
- **链接**: [arXiv:2004.04400](https://arxiv.org/abs/2004.04400) · 📚 被引 66
- **作者**: Jogendra Nath Kundu, Siddharth Seth, Varun Jampani, Mugalodi Rakesh, R. Venkatesh Babu, Anirban Chakraborty
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera captured human pose is an outcome of several sources of variation. Performance of supervised 3D pose estimation approaches comes at the cost of dispensing with variations, such as shape and appearance, that may be useful for solving other related tasks. As a result, the learned model not only inculcates task-bias but also dataset-bias because of its strong reliance on the annotated samples, which also holds true for weakly-supervised models. Acknowledging this, we propose a self-supervised learning framework to disentangle such variations from unlabeled video frames. We leverage the prior knowledge on human skeleton and poses in the form of a single part-based 2D puppet model, human pose articulation constraints, and a set of unpaired 3D poses. Our differentiable formalization, bridging the representation gap between the 3D pose and spatial part maps, not only facilitates discovery of interpretable pose disentanglement but also allows us to operate on videos with diverse camera movements. Qualitative results on unseen in-the-wild datasets establish our superior generalization across multiple tasks beyond the primary tasks of 3D pose estimation and part segmentation. Furthermore, we demonstrate state-of-the-art weakly-supervised 3D pose estimation performance on both Human3.6M and MPI-INF-3DHP datasets.

</details>

### From Image Collections to Point Clouds With Self-Supervised Shape and Pose Networks.
- **链接**: [arXiv:2005.01939](https://arxiv.org/abs/2005.01939) · 📚 被引 31
- **作者**: Navaneet K. L., Ansu Mathew, Shashank Kashyap, Wei-Chih Hung, Varun Jampani, R. Venkatesh Babu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing 3D models from 2D images is one of the fundamental problems in computer vision. In this work, we propose a deep learning technique for 3D object reconstruction from a single image. Contrary to recent works that either use 3D supervision or multi-view supervision, we use only single view images with no pose information during training as well. This makes our approach more practical requiring only an image collection of an object category and the corresponding silhouettes. We learn both 3D point cloud reconstruction and pose estimation networks in a self-supervised manner, making use of differentiable point cloud renderer to train with 2D supervision. A key novelty of the proposed technique is to impose 3D geometric reasoning into predicted 3D point clouds by rotating them with randomly sampled poses and then enforcing cycle consistency on both 3D reconstructions and poses. In addition, using single-view supervision allows us to do test-time optimization on a given test image. Experiments on the synthetic ShapeNet and real-world Pix3D datasets demonstrate that our approach, despite using less supervision, can achieve competitive performance compared to pose-supervised and multi-view supervised approaches.

</details>

### MAST: A Memory-Augmented Self-Supervised Tracker.
- **链接**: [arXiv:2002.07793](https://arxiv.org/abs/2002.07793) · 📚 被引 134
- **作者**: Zihang Lai, Erika Lu, Weidi Xie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent interest in self-supervised dense tracking has yielded rapid progress, but performance still remains far from supervised methods. We propose a dense tracking model trained on videos without any annotations that surpasses previous self-supervised methods on existing benchmarks by a significant margin (+15%), and achieves performance comparable to supervised methods. In this paper, we first reassess the traditional choices used for self-supervised training and reconstruction loss by conducting thorough experiments that finally elucidate the optimal choices. Second, we further improve on existing methods by augmenting our architecture with a crucial memory component. Third, we benchmark on large-scale semi-supervised video object segmentation(aka. dense tracking), and propose a new metric: generalizability. Our first two contributions yield a self-supervised network that for the first time is competitive with supervised methods on standard evaluation metrics of dense tracking. When measuring generalizability, we show self-supervised approaches are actually superior to the majority of supervised methods. We believe this new generalizability metric can better capture the real-world use-cases for dense tracking, and will spur new interest in this research direction.

</details>

### Self-Supervised Deep Visual Odometry With Online Adaptation.
- **链接**: [arXiv:2005.06136](https://arxiv.org/abs/2005.06136) · 📚 被引 64
- **作者**: Shunkai Li, Xin Wang, Yingdian Cao, Fei Xue, Zike Yan, Hongbin Zha
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised VO methods have shown great success in jointly estimating camera pose and depth from videos. However, like most data-driven methods, existing VO networks suffer from a notable decrease in performance when confronted with scenes different from the training data, which makes them unsuitable for practical applications. In this paper, we propose an online meta-learning algorithm to enable VO networks to continuously adapt to new environments in a self-supervised manner. The proposed method utilizes convolutional long short-term memory (convLSTM) to aggregate rich spatial-temporal information in the past. The network is able to memorize and learn from its past experience for better estimation and fast adaptation to the current frame. When running VO in the open world, in order to deal with the changing environment, we propose an online feature alignment method by aligning feature distributions at different time. Our VO network is able to seamlessly adapt to different environments. Extensive experiments on unseen outdoor scenes, virtual to real world and outdoor to indoor environments demonstrate that our method consistently outperforms state-of-the-art self-supervised VO baselines considerably.

</details>

### Sketch-BERT: Learning Sketch Bidirectional Encoder Representation From Transformers by Self-Supervised Learning of Sketch Gestalt.
- **链接**: [arXiv:2005.09159](https://arxiv.org/abs/2005.09159) · 📚 被引 57
- **作者**: Hangyu Lin, Yanwei Fu, Xiangyang Xue, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous researches of sketches often considered sketches in pixel format and leveraged CNN based models in the sketch understanding. Fundamentally, a sketch is stored as a sequence of data points, a vector format representation, rather than the photo-realistic image of pixels. SketchRNN studied a generative neural representation for sketches of vector format by Long Short Term Memory networks (LSTM). Unfortunately, the representation learned by SketchRNN is primarily for the generation tasks, rather than the other tasks of recognition and retrieval of sketches. To this end and inspired by the recent BERT model, we present a model of learning Sketch Bidirectional Encoder Representation from Transformer (Sketch-BERT). We generalize BERT to sketch domain, with the novel proposed components and pre-training algorithms, including the newly designed sketch embedding networks, and the self-supervised learning of sketch gestalt. Particularly, towards the pre-training task, we present a novel Sketch Gestalt Model (SGM) to help train the Sketch-BERT. Experimentally, we show that the learned representation of Sketch-BERT can help and improve the performance of the downstream tasks of sketch recognition, sketch retrieval, and sketch gestalt.

</details>

### Flow2Stereo: Effective Self-Supervised Learning of Optical Flow and Stereo Matching.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_Flow2Stereo_Effective_Self-Supervised_Learning_of_Optical_Flow_and_Stereo_Matching_CVPR_2020_paper.html) · 📚 被引 60
- **作者**: Pengpeng Liu, Irwin King, Michael R. Lyu, Jia Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In self-supervised learning, a system is tasked with achieving a surrogate objective by defining alternative targets on a set of unlabeled data. The aim is to build useful representations that can be used in downstream tasks, without costly manual annotation. In this work, we propose a novel self-supervised formulation of relational reasoning that allows a learner to bootstrap a signal from information implicit in unlabeled data. Training a relation head to discriminate how entities relate to themselves (intra-reasoning) and other entities (inter-reasoning), results in rich and descriptive representations in the underlying neural network backbone, which can be used in downstream tasks such as classification and image retrieval. We evaluate the proposed method following a rigorous experimental procedure, using standard datasets, protocols, and backbones. Self-supervised relational reasoning outperforms the best competitor in all conditions by an average 14% in accuracy, and the most recent state-of-the-art model by 3%. We link the effectiveness of the method to the maximization of a Bernoulli log-likelihood, which can be considered as a proxy for maximizing the mutual information, resulting in a more efficient objective with respect to the commonly used contrastive losses.

</details>

### Demystifying Contrastive Self-Supervised Learning: Invariances, Augmentations and Dataset Biases.
- **链接**: [arXiv:2007.13916](https://arxiv.org/abs/2007.13916)
- **作者**: Senthil Purushwalkam, Abhinav Gupta
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Self-Supervised Learning of Pretext-Invariant Representations.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Misra_Self-Supervised_Learning_of_Pretext-Invariant_Representations_CVPR_2020_paper.html) · 📚 被引 935
- **作者**: Ishan Misra, Laurens van der Maaten
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Learning to Orient Surfaces by Self-supervised Spherical CNNs.
- **链接**: [arXiv:2011.03298](https://arxiv.org/abs/2011.03298)
- **作者**: Riccardo Spezialetti, Federico Stella, Marlon Marcon, Luciano Silva, Samuele Salti, Luigi Di Stefano
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Defining and reliably finding a canonical orientation for 3D surfaces is key to many Computer Vision and Robotics applications. This task is commonly addressed by handcrafted algorithms exploiting geometric cues deemed as distinctive and robust by the designer. Yet, one might conjecture that humans learn the notion of the inherent orientation of 3D objects from experience and that machines may do so alike. In this work, we show the feasibility of learning a robust canonical orientation for surfaces represented as point clouds. Based on the observation that the quintessential property of a canonical orientation is equivariance to 3D rotations, we propose to employ Spherical CNNs, a recently introduced machinery that can learn equivariant representations defined on the Special Orthogonal group SO(3). Specifically, spherical correlations compute feature maps whose elements define 3D rotations. Our method learns such feature maps from raw data by a self-supervised training procedure and robustly selects a rotation to transform the input point cloud into a learned canonical orientation. Thereby, we realize the first end-to-end learning approach to define and extract the canonical orientation of 3D shapes, which we aptly dub Compass. Experiments on several public datasets prove its effectiveness at orienting local surface patches as well as whole objects.

</details>

### 3D Self-Supervised Methods for Medical Imaging.
- **链接**: [arXiv:2006.03829](https://arxiv.org/abs/2006.03829)
- **作者**: Aiham Taleb, Winfried Loetzsch, Noel Danz, Julius Severin, Thomas Gärtner, Benjamin Bergner et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning methods have witnessed a recent surge of interest after proving successful in multiple application fields. In this work, we leverage these techniques, and we propose 3D versions for five different self-supervised methods, in the form of proxy tasks. Our methods facilitate neural network feature learning from unlabeled 3D images, aiming to reduce the required cost for expert annotation. The developed algorithms are 3D Contrastive Predictive Coding, 3D Rotation prediction, 3D Jigsaw puzzles, Relative 3D patch location, and 3D Exemplar networks. Our experiments show that pretraining models with our 3D tasks yields more powerful semantic representations, and enables solving downstream tasks more accurately and efficiently, compared to training the models from scratch and to pretraining them on 2D slices. We demonstrate the effectiveness of our methods on three downstream tasks from the medical imaging domain: i) Brain Tumor Segmentation from 3D MRI, ii) Pancreas Tumor Segmentation from 3D CT, and iii) Diabetic Retinopathy Detection from 2D Fundus images. In each task, we assess the gains in data-efficiency, performance, and speed of convergence. Interestingly, we also find gains when transferring the learned representations, by our methods, from a large unlabeled 3D corpus to a small downstream-specific dataset. We achieve results competitive to state-of-the-art solutions at a fraction of the computational expense. We publish our implementations for the developed algorithms (both 3D and 2D versions) as an open-source library, in an effort to allow other researchers to apply and extend our methods on their datasets.

</details>

### Cross-lingual Retrieval for Iterative Self-Supervised Training.
- **链接**: [arXiv:2006.09526](https://arxiv.org/abs/2006.09526)
- **作者**: Chau Tran, Yuqing Tang, Xian Li, Jiatao Gu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial examples can cause catastrophic mistakes in Deep Neural Network (DNNs) based vision systems e.g., for classification, segmentation and object detection. The vulnerability of DNNs against such attacks can prove a major roadblock towards their real-world deployment. Transferability of adversarial examples demand generalizable defenses that can provide cross-task protection. Adversarial training that enhances robustness by modifying target model's parameters lacks such generalizability. On the other hand, different input processing based defenses fall short in the face of continuously evolving attacks. In this paper, we take the first step to combine the benefits of both approaches and propose a self-supervised adversarial training mechanism in the input space. By design, our defense is a generalizable approach and provides significant robustness against the \textbf{unseen} adversarial attacks (\eg by reducing the success rate of translation-invariant \textbf{ensemble} attack from 82.6\% to 31.9\% in comparison to previous state-of-the-art). It can be deployed as a plug-and-play solution to protect a variety of vision systems, as we demonstrate for the case of classification, segmentation and detection. Code is available at: {\small\url{https://github.com/Muzammal-Naseer/NRP}}.

</details>

</details>

### Noise2Same: Optimizing A Self-Supervised Bound for Image Denoising.
- **链接**: [arXiv:2010.11971](https://arxiv.org/abs/2010.11971) · [代码](https://github.com/divelab/Noise2Same)
- **作者**: Yaochen Xie, Zhengyang Wang, Shuiwang Ji
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances have spurred incredible progress in self-supervised pretraining for vision. We investigate what factors may play a role in the utility of these pretraining methods for practitioners. To do this, we evaluate various self-supervised algorithms across a comprehensive array of synthetic datasets and downstream tasks. We prepare a suite of synthetic data that enables an endless supply of annotated images as well as full control over dataset difficulty. Our experiments offer insights into how the utility of self-supervision changes as the number of available labels grows as well as how the utility changes as a function of the downstream task and the properties of the training data. We also find that linear evaluation does not correlate with finetuning performance. Code and data is available at \href{https://www.github.com/princeton-vl/selfstudy}{github.com/princeton-vl/selfstudy}.

</details>

</details>

### Self-Supervised Visual Representation Learning from Hierarchical Grouping.
- **链接**: [arXiv:2012.03044](https://arxiv.org/abs/2012.03044)
- **作者**: Xiao Zhang, Michael Maire
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The reconstruction of shredded documents consists in arranging the pieces of paper (shreds) in order to reassemble the original aspect of such documents. This task is particularly relevant for supporting forensic investigation as documents may contain criminal evidence. As an alternative to the laborious and time-consuming manual process, several researchers have been investigating ways to perform automatic digital reconstruction. A central problem in automatic reconstruction of shredded documents is the pairwise compatibility evaluation of the shreds, notably for binary text documents. In this context, deep learning has enabled great progress for accurate reconstructions in the domain of mechanically-shredded documents. A sensitive issue, however, is that current deep model solutions require an inference whenever a pair of shreds has to be evaluated. This work proposes a scalable deep learning approach for measuring pairwise compatibility in which the number of inferences scales linearly (rather than quadratically) with the number of shreds. Instead of predicting compatibility directly, deep models are leveraged to asymmetrically project the raw shred content onto a common metric space in which distance is proportional to the compatibility. Experimental results show that our method has accuracy comparable to the state-of-the-art with a speed-up of about 22 times for a test instance with 505 shreds (20 mixed shredded-pages from different documents).

</details>

### Self-Supervised Learning of Video-Induced Visual Invariances.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Tschannen_Self-Supervised_Learning_of_Video-Induced_Visual_Invariances_CVPR_2020_paper.html) · 📚 被引 34
- **作者**: Michael Tschannen, Josip Djolonga, Marvin Ritter, Aravindh Mahendran, Neil Houlsby, Sylvain Gelly et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Contrastive learning of global and local features for medical image segmentation with limited annotations.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/949686ecef4ee20a62d16b4a2d7ccca3-Abstract.html)
- **作者**: Krishna Chaitanya, Ertunc Erdil, Neerav Karani, Ender Konukoglu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Debiased Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/63c3ddcc7b23daa1e42dc41f9a44a873-Abstract.html)
- **作者**: Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Self-paced Contrastive Learning with Hybrid Memory for Domain Adaptive Object Re-ID.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/821fa74b50ba3f7cba1e6c53e8fa6845-Abstract.html)
- **作者**: Yixiao Ge, Feng Zhu, Dapeng Chen, Rui Zhao, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: NeurIPS 2020

### Contrastive Learning with Adversarial Examples.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/c68c9c8258ea7d85472dd6fd0015f047-Abstract.html)
- **作者**: Chih-Hui Ho, Nuno Vasconcelos
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Robust Pre-Training by Adversarial Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/ba7e36c43aff315c00ec2b8625e3b719-Abstract.html)
- **作者**: Ziyu Jiang, Tianlong Chen, Ting Chen, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Hard Negative Mixing for Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/f7cade80b7cc92b991cf4d2806d6bd78-Abstract.html)
- **作者**: Yannis Kalantidis, Mert Bülent Sariyildiz, Noé Pion, Philippe Weinzaepfel, Diane Larlus
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### ContraGAN: Contrastive Learning for Conditional Image Generation.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/f490c742cd8318b8ee6dca10af2a163f-Abstract.html)
- **作者**: Minguk Kang, Jaesik Park
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Supervised Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/d89a66c7c80a29b1bdbab0f2a1a94af8-Abstract.html)
- **作者**: Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Few-shot Visual Reasoning with Meta-Analogical Contrastive Learning.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/c39e1a03859f9ee215bc49131d0caf33-Abstract.html)
- **作者**: Youngsung Kim, Jinwoo Shin, Eunho Yang, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### CSI: Novelty Detection via Contrastive Learning on Distributionally Shifted Instances.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/8965f76632d7672e7d3cf29c87ecaa0c-Abstract.html)
- **作者**: Jihoon Tack, Sangwoo Mo, Jongheon Jeong, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Soft Contrastive Learning for Visual Localization.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/7f2cba89a7116c7c6b0a769572d5fad9-Abstract.html)
- **作者**: Janine Thoma, Danda Pani Paudel, Luc Van Gool
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### What Makes for Good Views for Contrastive Learning?
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/4c2e5eaae9152079b9e95845750bb9ab-Abstract.html)
- **作者**: Yonglong Tian, Chen Sun, Ben Poole, Dilip Krishnan, Cordelia Schmid, Phillip Isola
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

### Graph Contrastive Learning with Augmentations.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2020/hash/3fe230348e9a12c13120749e3f9fa4cd-Abstract.html)
- **作者**: Yuning You, Tianlong Chen, Yongduo Sui, Ting Chen, Zhangyang Wang, Yang Shen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2020

## 跨领域论文（完整笔记在其他领域）

- Monocular Differentiable Rendering for Self-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202020.md)
- Improving Object Detection with Selective Self-supervised Self-training. → [object-detection](../object-detection/Guideline%202020.md)
- Self-Supervised Monocular 3D Face Reconstruction by Occlusion-Aware Multi-view Geometry Consistency. → [3d-detection](../3d-detection/Guideline%202020.md)
- S3Net: Semantic-Aware Self-supervised Depth Estimation with Monocular Videos and Synthetic Data. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
- Self-supervised Monocular Depth Estimation: Solving the Dynamic Object Problem by Semantic Guidance. → [multi-camera-perception](../multi-camera-perception/Guideline%202020.md)
