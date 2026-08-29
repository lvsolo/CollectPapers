# Self-supervised Vision — 2023 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 98 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Forecast-MAE: Self-supervised Pre-training for Motion Forecasting with Masked Autoencoders.
- **链接**: [arXiv:2308.09882](https://arxiv.org/abs/2308.09882) · [代码](https://github.com/jchengai/forecast-mae) · 📚 被引 104
- **作者**: Jie Cheng, Xiaodong Mei, Ming Liu
- **🏷️ 机构**: HKUST
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This study explores the application of self-supervised learning (SSL) to the task of motion forecasting, an area that has not yet been extensively investigated despite the widespread success of SSL in computer vision and natural language processing. To address this gap, we introduce Forecast-MAE, an extension of the mask autoencoders framework that is specifically designed for self-supervised learning of the motion forecasting task. Our approach includes a novel masking strategy that leverages the strong interconnections between agents' trajectories and road networks, involving complementary masking of agents' future or history trajectories and random masking of lane segments. Our experiments on the challenging Argoverse 2 motion forecasting benchmark show that Forecast-MAE, which utilizes standard Transformer blocks with minimal inductive bias, achieves competitive performance compared to state-of-the-art methods that rely on supervised learning and sophisticated designs. Moreover, it outperforms the previous self-supervised learning method by a significant margin. Code is available at https://github.com/jchengai/forecast-mae.

</details>

### Temporal DINO: A Self-supervised Video Strategy to Enhance Action Prediction.
- **链接**: [arXiv:2308.04589](https://arxiv.org/abs/2308.04589) · 📚 被引 3
- **作者**: Izzeddin Teeti, Rongali Sai Bhargav, Vivek Singh, Andrew Bradley, Biplab Banerjee, Fabio Cuzzolin
- **🏷️ 机构**: Oxford Brookes University,VAIL, Indian Institute of Technology,Bombay
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emerging field of action prediction plays a vital role in various computer vision applications such as autonomous driving, activity analysis and human-computer interaction. Despite significant advancements, accurately predicting future actions remains a challenging problem due to high dimensionality, complex dynamics and uncertainties inherent in video data. Traditional supervised approaches require large amounts of labelled data, which is expensive and time-consuming to obtain. This paper introduces a novel self-supervised video strategy for enhancing action prediction inspired by DINO (self-distillation with no labels). The Temporal-DINO approach employs two models; a 'student' processing past frames; and a 'teacher' processing both past and future frames, enabling a broader temporal context. During training, the teacher guides the student to learn future context by only observing past frames. The strategy is evaluated on ROAD dataset for the action prediction downstream task using 3D-ResNet, Transformer, and LSTM architectures. The experimental results showcase significant improvements in prediction performance across these architectures, with our method achieving an average enhancement of 9.9% Precision Points (PP), highlighting its effectiveness in enhancing the backbones' capabilities of capturing long-term dependencies. Furthermore, our approach demonstrates efficiency regarding the pretraining dataset size and the number of epochs required. This method overcomes limitations present in other approaches, including considering various backbone architectures, addressing multiple prediction horizons, reducing reliance on hand-crafted augmentations, and streamlining the pretraining process into a single stage. These findings highlight the potential of our approach in diverse video-based tasks such as activity recognition, motion planning, and scene understanding.

</details>

### P2C: Self-Supervised Point Cloud Completion from Single Partial Clouds.
- **链接**: [arXiv:2307.14726](https://arxiv.org/abs/2307.14726) · [代码](https://github.com/CuiRuikai/Partial2Complete) · 📚 被引 43
- **作者**: Ruikai Cui, Shi Qiu, Saeed Anwar, Jiawei Liu, Chaoyue Xing, Jing Zhang et al.
- **🏷️ 机构**: Australian National University, King Fahd University of Petroleum and Minerals
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point cloud completion aims to recover the complete shape based on a partial observation. Existing methods require either complete point clouds or multiple partial observations of the same object for learning. In contrast to previous approaches, we present Partial2Complete (P2C), the first self-supervised framework that completes point cloud objects using training samples consisting of only a single incomplete point cloud per object. Specifically, our framework groups incomplete point clouds into local patches as input and predicts masked patches by learning prior information from different partial objects. We also propose Region-Aware Chamfer Distance to regularize shape mismatch without limiting completion capability, and devise the Normal Consistency Constraint to incorporate a local planarity assumption, encouraging the recovered shape surface to be continuous and complete. In this way, P2C no longer needs multiple observations or complete point clouds as ground truth. Instead, structural cues are learned from a category-specific dataset to complete partial point clouds of objects. We demonstrate the effectiveness of our approach on both synthetic ShapeNet data and real-world ScanNet data, showing that P2C produces comparable results to methods trained with complete shapes, and outperforms methods learned with multiple partial observations. Code is available at https://github.com/CuiRuikai/Partial2Complete.

</details>

### Point Contrastive Prediction with Semantic Clustering for Self-Supervised Learning on Point Cloud Videos.
- **链接**: [arXiv:2308.09247](https://arxiv.org/abs/2308.09247) · 📚 被引 20
- **作者**: Xiaoxiao Sheng, Zhiqiang Shen, Gang Xiao, Longguang Wang, Yulan Guo, Hehe Fan
- **🏷️ 机构**: Shanghai Jiao Tong University, Aviation University of Air Force, Sun Yat-Sen University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a unified point cloud video self-supervised learning framework for object-centric and scene-centric data. Previous methods commonly conduct representation learning at the clip or frame level and cannot well capture fine-grained semantics. Instead of contrasting the representations of clips or frames, in this paper, we propose a unified self-supervised framework by conducting contrastive learning at the point level. Moreover, we introduce a new pretext task by achieving semantic alignment of superpoints, which further facilitates the representations to capture semantic cues at multiple scales. In addition, due to the high redundancy in the temporal dimension of dynamic point clouds, directly conducting contrastive learning at the point level usually leads to massive undesired negatives and insufficient modeling of positive representations. To remedy this, we propose a selection strategy to retain proper negatives and make use of high-similarity samples from other instances as positive supplements. Extensive experiments show that our method outperforms supervised counterparts on a wide range of downstream tasks and demonstrates the superior transferability of the learned representations.

</details>

### Masked Spatio-Temporal Structure Prediction for Self-supervised Learning on Point Cloud Videos.
- **链接**: [arXiv:2308.09245](https://arxiv.org/abs/2308.09245) · 📚 被引 23
- **作者**: Zhiqiang Shen, Xiaoxiao Sheng, Hehe Fan, Longguang Wang, Yulan Guo, Qiong Liu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Zhejiang University, Aviation University of Air Force
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the community has made tremendous progress in developing effective methods for point cloud video understanding that learn from massive amounts of labeled data. However, annotating point cloud videos is usually notoriously expensive. Moreover, training via one or only a few traditional tasks (e.g., classification) may be insufficient to learn subtle details of the spatio-temporal structure existing in point cloud videos. In this paper, we propose a Masked Spatio-Temporal Structure Prediction (MaST-Pre) method to capture the structure of point cloud videos without human annotations. MaST-Pre is based on spatio-temporal point-tube masking and consists of two self-supervised learning tasks. First, by reconstructing masked point tubes, our method is able to capture the appearance information of point cloud videos. Second, to learn motion, we propose a temporal cardinality difference prediction task that estimates the change in the number of points within a point tube. In this way, MaST-Pre is forced to model the spatial and temporal structure in point cloud videos. Extensive experiments on MSRAction-3D, NTU-RGBD, NvGesture, and SHREC'17 demonstrate the effectiveness of the proposed method.

</details>

### Implicit Autoencoder for Point-Cloud Self-Supervised Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01336) · 📚 被引 44
- **作者**: Siming Yan, Zhenpei Yang, Haoxiang Li, Chen Song, Li Guan, Hao Kang et al.
- **🏷️ 机构**: The University of Texas at Austin, Wormpex AI Research
- **会议**: ICCV 2023

### SC3K: Self-supervised and Coherent 3D Keypoints Estimation from Rotated, Noisy, and Decimated Point Cloud Data.
- **链接**: [arXiv:2308.05410](https://arxiv.org/abs/2308.05410) · [代码](https://github.com/IITPAVIS/SC3K) · 📚 被引 11
- **作者**: Mohammad Zohaib, Alessio Del Bue
- **🏷️ 机构**: Italian Institute of Technology (IIT),Pattern Analysis &#x0026; Computer Vision (PAVIS),Genoa,Italy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a new method to infer keypoints from arbitrary object categories in practical scenarios where point cloud data (PCD) are noisy, down-sampled and arbitrarily rotated. Our proposed model adheres to the following principles: i) keypoints inference is fully unsupervised (no annotation given), ii) keypoints position error should be low and resilient to PCD perturbations (robustness), iii) keypoints should not change their indexes for the intra-class objects (semantic coherence), iv) keypoints should be close to or proximal to PCD surface (compactness). We achieve these desiderata by proposing a new self-supervised training strategy for keypoints estimation that does not assume any a priori knowledge of the object class, and a model architecture with coupled auxiliary losses that promotes the desired keypoints properties. We compare the keypoints estimated by the proposed approach with those of the state-of-the-art unsupervised approaches. The experiments show that our approach outperforms by estimating keypoints with improved coverage (+9.41%) while being semantically consistent (+4.66%) that best characterizes the object's 3D shape for downstream tasks. Code and data are available at: https://github.com/IITPAVIS/SC3K

</details>

### Self-supervised Monocular Underwater Depth Recovery, Image Restoration, and a Real-sea Video Dataset.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01125) · 📚 被引 32
- **作者**: Nisha Varghese, Ashish Kumar, A. N. Rajagopalan
- **🏷️ 机构**: Indian Institute of Technology Madras,India
- **会议**: ICCV 2023

### SINC: Self-Supervised In-Context Learning for Vision-Language Tasks.
- **链接**: [arXiv:2307.07742](https://arxiv.org/abs/2307.07742) · 📚 被引 6
- **作者**: Yi-Syuan Chen, Yun-Zhu Song, Cheng Yu Yeo, Bei Liu, Jianlong Fu, Hong-Han Shuai
- **🏷️ 机构**: National Yang Ming Chiao Tung University, Microsoft Research Asia
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Pre-trained Transformers exhibit an intriguing capacity for in-context learning. Without gradient updates, these models can rapidly construct new predictors from demonstrations presented in the inputs. Recent works promote this ability in the vision-language domain by incorporating visual information into large language models that can already make in-context predictions. However, these methods could inherit issues in the language domain, such as template sensitivity and hallucination. Also, the scale of these language models raises a significant demand for computations, making learning and operating these models resource-intensive. To this end, we raise a question: ``How can we enable in-context learning without relying on the intrinsic in-context ability of large language models?". To answer it, we propose a succinct and general framework, Self-supervised IN-Context learning (SINC), that introduces a meta-model to learn on self-supervised prompts consisting of tailored demonstrations. The learned models can be transferred to downstream tasks for making in-context predictions on-the-fly. Extensive experiments show that SINC outperforms gradient-based methods in various vision-language tasks under few-shot settings. Furthermore, the designs of SINC help us investigate the benefits of in-context learning across different tasks, and the analysis further reveals the essential components for the emergence of in-context learning in the vision-language domain.

</details>

### SelfGraphVQA: A Self-Supervised Graph Neural Network for Scene-based Question Answering.
- **链接**: [arXiv:2310.01842](https://arxiv.org/abs/2310.01842) · 📚 被引 4
- **作者**: Bruno Souza, Marius Aasan, Hélio Pedrini, Adín Ramírez Rivera
- **🏷️ 机构**: University of Campinas, University of Oslo
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The intersection of vision and language is of major interest due to the increased focus on seamless integration between recognition and reasoning. Scene graphs (SGs) have emerged as a useful tool for multimodal image analysis, showing impressive performance in tasks such as Visual Question Answering (VQA). In this work, we demonstrate that despite the effectiveness of scene graphs in VQA tasks, current methods that utilize idealized annotated scene graphs struggle to generalize when using predicted scene graphs extracted from images. To address this issue, we introduce the SelfGraphVQA framework. Our approach extracts a scene graph from an input image using a pre-trained scene graph generator and employs semantically-preserving augmentation with self-supervised techniques. This method improves the utilization of graph representations in VQA tasks by circumventing the need for costly and potentially biased annotated data. By creating alternative views of the extracted graphs through image augmentations, we can learn joint embeddings by optimizing the informational content in their representations using an un-normalized contrastive approach. As we work with SGs, we experiment with three distinct maximization strategies: node-wise, graph-wise, and permutation-equivariant regularization. We empirically showcase the effectiveness of the extracted scene graph for VQA and demonstrate that these approaches enhance overall performance by highlighting the significance of visual information. This offers a more practical solution for VQA tasks that rely on SGs for complex reasoning questions.

</details>

### Randomized Quantization: A Generic Augmentation for Data Agnostic Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01494) · 📚 被引 10
- **作者**: Huimin Wu, Chenyang Lei, Xiao Sun, Peng-Shuai Wang, Qifeng Chen, Kwang-Ting Cheng et al.
- **🏷️ 机构**: HKUST, CAIR, HKISI CAS, Shanghai AI Lab
- **会议**: ICCV 2023

### Self-Supervised Burst Super-Resolution.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00973)
- **作者**: Goutam Bhat, Michaël Gharbi, Jiawen Chen, Luc Van Gool, Zhihao Xia
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Active Self-Supervised Learning: A Few Low-Cost Relationships Are All You Need.
- **链接**: [arXiv:2303.15256](https://arxiv.org/abs/2303.15256) · 📚 被引 9
- **作者**: Vivien Cabannes, Léon Bottou, Yann LeCun, Randall Balestriero
- **🏷️ 机构**: Meta AI
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) has emerged as the solution of choice to learn transferable representations from unlabeled data. However, SSL requires to build samples that are known to be semantically akin, i.e. positive views. Requiring such knowledge is the main limitation of SSL and is often tackled by ad-hoc strategies e.g. applying known data-augmentations to the same input. In this work, we formalize and generalize this principle through Positive Active Learning (PAL) where an oracle queries semantic relationships between samples. PAL achieves three main objectives. First, it unveils a theoretically grounded learning framework beyond SSL, based on similarity graphs, that can be extended to tackle supervised and semi-supervised learning depending on the employed oracle. Second, it provides a consistent algorithm to embed a priori knowledge, e.g. some observed labels, into any SSL losses without any change in the training pipeline. Third, it provides a proper active learning framework yielding low-cost solutions to annotate datasets, arguably bringing the gap between theory and practice of active learning that is based on simple-to-answer-by-non-experts queries of semantic relationships between inputs.

</details>

### Contrastive Continuity on Augmentation Stability Rehearsal for Continual Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00525) · 📚 被引 10
- **作者**: Haoyang Cheng, Haitao Wen, Xiaoliang Zhang, Heqian Qiu, Lanxiao Wang, Hongliang Li
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China
- **会议**: ICCV 2023

### Identity-Seeking Self-Supervised Representation Learning for Generalizable Person Re-identification.
- **链接**: [arXiv:2308.08887](https://arxiv.org/abs/2308.08887) · [代码](https://github.com/dcp15/ISR_ICCV2023_Oral) · 📚 被引 27
- **作者**: Zhaopeng Dou, Zhongdao Wang, Yali Li, Shengjin Wang
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper aims to learn a domain-generalizable (DG) person re-identification (ReID) representation from large-scale videos \textbf{without any annotation}. Prior DG ReID methods employ limited labeled data for training due to the high cost of annotation, which restricts further advances. To overcome the barriers of data and annotation, we propose to utilize large-scale unsupervised data for training. The key issue lies in how to mine identity information. To this end, we propose an Identity-seeking Self-supervised Representation learning (ISR) method. ISR constructs positive pairs from inter-frame images by modeling the instance association as a maximum-weight bipartite matching problem. A reliability-guided contrastive loss is further presented to suppress the adverse impact of noisy positive pairs, ensuring that reliable positive pairs dominate the learning process. The training cost of ISR scales approximately linearly with the data size, making it feasible to utilize large-scale data for training. The learned representation exhibits superior generalization ability. \textbf{Without human annotation and fine-tuning, ISR achieves 87.0\% Rank-1 on Market-1501 and 56.4\% Rank-1 on MSMT17}, outperforming the best supervised domain-generalizable method by 5.0\% and 19.5\%, respectively. In the pre-training$\rightarrow$fine-tuning scenario, ISR achieves state-of-the-art performance, with 88.4\% Rank-1 on MSMT17. The code is at \url{https://github.com/dcp15/ISR_ICCV2023_Oral}.

</details>

### SimFIR: A Simple Framework for Fisheye Image Rectification with Self-supervised Representation Learning.
- **链接**: [arXiv:2308.09040](https://arxiv.org/abs/2308.09040) · 📚 被引 27
- **作者**: Hao Feng, Wendi Wang, Jiajun Deng, Wengang Zhou, Li Li, Houqiang Li
- **🏷️ 机构**: University of Science and Technology of China,CAS Key Laboratory of Technology in GIPAS,EEIS Department, The University of Sydney
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In fisheye images, rich distinct distortion patterns are regularly distributed in the image plane. These distortion patterns are independent of the visual content and provide informative cues for rectification. To make the best of such rectification cues, we introduce SimFIR, a simple framework for fisheye image rectification based on self-supervised representation learning. Technically, we first split a fisheye image into multiple patches and extract their representations with a Vision Transformer (ViT). To learn fine-grained distortion representations, we then associate different image patches with their specific distortion patterns based on the fisheye model, and further subtly design an innovative unified distortion-aware pretext task for their learning. The transfer performance on the downstream rectification task is remarkably boosted, which verifies the effectiveness of the learned representations. Extensive experiments are conducted, and the quantitative and qualitative results demonstrate the superiority of our method over the state-of-the-art algorithms as well as its strong generalization ability on real-world fisheye images.

</details>

### TeD-SPAD: Temporal Distinctiveness for Self-supervised Privacy-preservation for video Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01251)
- **作者**: Joseph Fioresi, Ishan Rajendrakumar Dave, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Self-supervised Character-to-Character Distillation for Text Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01784) · 📚 被引 40
- **作者**: Tongkun Guan, Wei Shen, Xue Yang, Qi Feng, Zekun Jiang, Xiaokang Yang
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University,Department of Automation
- **会议**: ICCV 2023

### Pseudo Flow Consistency for Self-Supervised 6D Object Pose Estimation.
- **链接**: [arXiv:2308.10016](https://arxiv.org/abs/2308.10016) · 📚 被引 17
- **作者**: Yang Hai, Rui Song, Jiaojiao Li, David Ferstl, Yinlin Hu
- **🏷️ 机构**: State Key Laboratory of ISN, Xidian University, MagicLeap
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most self-supervised 6D object pose estimation methods can only work with additional depth information or rely on the accurate annotation of 2D segmentation masks, limiting their application range. In this paper, we propose a 6D object pose estimation method that can be trained with pure RGB images without any auxiliary information. We first obtain a rough pose initialization from networks trained on synthetic images rendered from the target's 3D mesh. Then, we introduce a refinement strategy leveraging the geometry constraint in synthetic-to-real image pairs from multiple different views. We formulate this geometry constraint as pixel-level flow consistency between the training images with dynamically generated pseudo labels. We evaluate our method on three challenging datasets and demonstrate that it outperforms state-of-the-art self-supervised methods significantly, with neither 2D annotations nor additional depth images.

</details>

### Self-supervised Image Denoising with Downsampled Invariance Loss and Conditional Blind-Spot Network.
- **链接**: [arXiv:2304.09507](https://arxiv.org/abs/2304.09507) · 📚 被引 15
- **作者**: Yeong Il Jang, Keuntek Lee, Gu Yong Park, Seyun Kim, Nam Ik Cho
- **🏷️ 机构**: Seoul National University,INMC,Department of ECE,Seoul,Korea, Gauss Labs Inc.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There have been many image denoisers using deep neural networks, which outperform conventional model-based methods by large margins. Recently, self-supervised methods have attracted attention because constructing a large real noise dataset for supervised training is an enormous burden. The most representative self-supervised denoisers are based on blind-spot networks, which exclude the receptive field's center pixel. However, excluding any input pixel is abandoning some information, especially when the input pixel at the corresponding output position is excluded. In addition, a standard blind-spot network fails to reduce real camera noise due to the pixel-wise correlation of noise, though it successfully removes independently distributed synthetic noise. Hence, to realize a more practical denoiser, we propose a novel self-supervised training framework that can remove real noise. For this, we derive the theoretic upper bound of a supervised loss where the network is guided by the downsampled blinded output. Also, we design a conditional blind-spot network (C-BSN), which selectively controls the blindness of the network to use the center pixel information. Furthermore, we exploit a random subsampler to decorrelate noise spatially, making the C-BSN free of visual artifacts that were often seen in downsample-based methods. Extensive experiments show that the proposed C-BSN achieves state-of-the-art performance on real-world datasets as a self-supervised denoiser and shows qualitatively pleasing results without any post-processing or refinement.

</details>

### EMR-MSF: Self-Supervised Recurrent Monocular Scene Flow Exploiting Ego-Motion Rigidity.
- **链接**: [arXiv:2309.01296](https://arxiv.org/abs/2309.01296) · 📚 被引 0
- **作者**: Zijie Jiang, Masatoshi Okutomi
- **🏷️ 机构**: Tokyo Institute of Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised monocular scene flow estimation, aiming to understand both 3D structures and 3D motions from two temporally consecutive monocular images, has received increasing attention for its simple and economical sensor setup. However, the accuracy of current methods suffers from the bottleneck of less-efficient network architecture and lack of motion rigidity for regularization. In this paper, we propose a superior model named EMR-MSF by borrowing the advantages of network architecture design under the scope of supervised learning. We further impose explicit and robust geometric constraints with an elaborately constructed ego-motion aggregation module where a rigidity soft mask is proposed to filter out dynamic regions for stable ego-motion estimation using static regions. Moreover, we propose a motion consistency loss along with a mask regularization loss to fully exploit static regions. Several efficient training strategies are integrated including a gradient detachment technique and an enhanced view synthesis process for better performance. Our proposed method outperforms the previous self-supervised works by a large margin and catches up to the performance of supervised methods. On the KITTI scene flow benchmark, our approach improves the SF-all metric of the state-of-the-art self-supervised monocular method by 44% and demonstrates superior performance across sub-tasks including depth and visual odometry, amongst other self-supervised single-task or multi-task methods.

</details>

### Anatomical Invariance Modeling and Semantic Alignment for Self-supervised Learning in 3D Medical Image Analysis.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01453) · 📚 被引 27
- **作者**: Yankai Jiang, Mingze Sun, Heng Guo, Xiaoyu Bai, Ke Yan, Le Lu et al.
- **🏷️ 机构**: Alibaba Group,DAMO Academy
- **会议**: ICCV 2023

### An Embarrassingly Simple Backdoor Attack on Self-supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00403) · 📚 被引 48
- **作者**: Changjiang Li, Ren Pang, Zhaohan Xi, Tianyu Du, Shouling Ji, Yuan Yao et al.
- **🏷️ 机构**: Pennsylvania State University, Zhejiang University, Nanjing University
- **会议**: ICCV 2023

### Self-supervised Pre-training for Mirror Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01123) · 📚 被引 7
- **作者**: Jiaying Lin, Rynson W. H. Lau
- **🏷️ 机构**: City University of Hong Kong
- **会议**: ICCV 2023

### Geometrized Transformer for Self-Supervised Homography Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00876) · 📚 被引 33
- **作者**: Jiazhen Liu, Xirong Li
- **🏷️ 机构**: Renmin University of China,Key Lab of DEKE
- **会议**: ICCV 2023

### DDS2M: Self-Supervised Denoising Diffusion Spatio-Spectral Model for Hyperspectral Image Restoration.
- **链接**: [arXiv:2303.06682](https://arxiv.org/abs/2303.06682) · 📚 被引 74
- **作者**: Yuchun Miao, Lefei Zhang, Liangpei Zhang, Dacheng Tao
- **🏷️ 机构**: Wuhan University,National Engineering Research Center for Multimedia Software, School of Computer Science, Wuhan University,State Key Lab. of Information Engineering in Surveying, Mapping and Remote Sensing, The University of Sydney,Sydney AI Centre, School of Computer Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models have recently received a surge of interest due to their impressive performance for image restoration, especially in terms of noise robustness. However, existing diffusion-based methods are trained on a large amount of training data and perform very well in-distribution, but can be quite susceptible to distribution shift. This is especially inappropriate for data-starved hyperspectral image (HSI) restoration. To tackle this problem, this work puts forth a self-supervised diffusion model for HSI restoration, namely Denoising Diffusion Spatio-Spectral Model (\texttt{DDS2M}), which works by inferring the parameters of the proposed Variational Spatio-Spectral Module (VS2M) during the reverse diffusion process, solely using the degraded HSI without any extra training data. In VS2M, a variational inference-based loss function is customized to enable the untrained spatial and spectral networks to learn the posterior distribution, which serves as the transitions of the sampling chain to help reverse the diffusion process. Benefiting from its self-supervised nature and the diffusion process, \texttt{DDS2M} enjoys stronger generalization ability to various HSIs compared to existing diffusion-based methods and superior robustness to noise compared to existing HSI restoration methods. Extensive experiments on HSI denoising, noisy HSI completion and super-resolution on a variety of HSIs demonstrate \texttt{DDS2M}'s superiority over the existing task-specific state-of-the-arts.

</details>

### CROSSFIRE: Camera Relocalization On Self-Supervised Features from an Implicit Representation.
- **链接**: [arXiv:2303.04869](https://arxiv.org/abs/2303.04869) · 📚 被引 50
- **作者**: Arthur Moreau, Nathan Piasco, Moussâb Bennehar, Dzmitry Tsishkou, Bogdan Stanciulescu, Arnaud de La Fortelle
- **🏷️ 机构**: Noah&#x2019;s Ark IoV Team,Huawei,France, PSL University, Centre for Robotics,Mines Paris
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Beyond novel view synthesis, Neural Radiance Fields are useful for applications that interact with the real world. In this paper, we use them as an implicit map of a given scene and propose a camera relocalization algorithm tailored for this representation. The proposed method enables to compute in real-time the precise position of a device using a single RGB camera, during its navigation. In contrast with previous work, we do not rely on pose regression or photometric alignment but rather use dense local features obtained through volumetric rendering which are specialized on the scene with a self-supervised objective. As a result, our algorithm is more accurate than competitors, able to operate in dynamic outdoor environments with changing lightning conditions and can be readily integrated in any volumetric neural renderer.

</details>

### Representation Uncertainty in Self-Supervised Learning as Variational Inference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01511) · 📚 被引 12
- **作者**: Hiroki Nakamura, Masashi Okada, Tadahiro Taniguchi
- **🏷️ 机构**: Panasonic Holdings Corp., Ritsumeikan University
- **会议**: ICCV 2023

### Random Sub-Samples Generation for Self-Supervised Real Image Denoising.
- **链接**: [arXiv:2307.16825](https://arxiv.org/abs/2307.16825) · [代码](https://github.com/p1y2z3/SDAP) · 📚 被引 46
- **作者**: Yizhong Pan, Xiao Liu, Xiangyu Liao, Yuanzhouhan Cao, Chao Ren
- **🏷️ 机构**: Sichuan University,College of Electronics and Information Engineering,China, Beijing Jiaotong University,School of Computer and Information Technology,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With sufficient paired training samples, the supervised deep learning methods have attracted much attention in image denoising because of their superior performance. However, it is still very challenging to widely utilize the supervised methods in real cases due to the lack of paired noisy-clean images. Meanwhile, most self-supervised denoising methods are ineffective as well when applied to the real-world denoising tasks because of their strict assumptions in applications. For example, as a typical method for self-supervised denoising, the original blind spot network (BSN) assumes that the noise is pixel-wise independent, which is much different from the real cases. To solve this problem, we propose a novel self-supervised real image denoising framework named Sampling Difference As Perturbation (SDAP) based on Random Sub-samples Generation (RSG) with a cyclic sample difference loss. Specifically, we dig deeper into the properties of BSN to make it more suitable for real noise. Surprisingly, we find that adding an appropriate perturbation to the training images can effectively improve the performance of BSN. Further, we propose that the sampling difference can be considered as perturbation to achieve better results. Finally we propose a new BSN framework in combination with our RSG strategy. The results show that it significantly outperforms other state-of-the-art self-supervised denoising methods on real-world datasets. The code is available at https://github.com/p1y2z3/SDAP.

</details>

### Learn TAROT with MENTOR: A Meta-Learned Self-supervised Approach for Trajectory Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00770) · 📚 被引 19
- **作者**: Mozhgan Pourkeshavarz, Changhe Chen, Amir Rasouli
- **🏷️ 机构**: Huawei,Noah&#x2019;s Ark Lab,Toronto,Canada
- **会议**: ICCV 2023

### Semantics Meets Temporal Correspondence: Self-supervised Object-centric Learning in Videos.
- **链接**: [arXiv:2308.09951](https://arxiv.org/abs/2308.09951) · [代码](https://github.com/shvdiwnkozbw/SMTC) · 📚 被引 13
- **作者**: Rui Qian, Shuangrui Ding, Xian Liu, Dahua Lin
- **🏷️ 机构**: The Chinese University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised methods have shown remarkable progress in learning high-level semantics and low-level temporal correspondence. Building on these results, we take one step further and explore the possibility of integrating these two features to enhance object-centric representations. Our preliminary experiments indicate that query slot attention can extract different semantic components from the RGB feature map, while random sampling based slot attention can exploit temporal correspondence cues between frames to assist instance identification. Motivated by this, we propose a novel semantic-aware masked slot attention on top of the fused semantic features and correspondence maps. It comprises two slot attention stages with a set of shared learnable Gaussian distributions. In the first stage, we use the mean vectors as slot initialization to decompose potential semantics and generate semantic segmentation masks through iterative attention. In the second stage, for each semantics, we randomly sample slots from the corresponding Gaussian distribution and perform masked feature aggregation within the semantic area to exploit temporal correspondence patterns for instance identification. We adopt semantic- and instance-level temporal consistency as self-supervision to encourage temporally coherent object-centric representations. Our model effectively identifies multiple object instances with semantic structure, reaching promising results on unsupervised video object discovery. Furthermore, we achieve state-of-the-art performance on dense label propagation tasks, demonstrating the potential for object-centric analysis. The code is released at https://github.com/shvdiwnkozbw/SMTC.

</details>

### MOST: Multiple Object localization with Self-supervised Transformers for object discovery.
- **链接**: [arXiv:2304.05387](https://arxiv.org/abs/2304.05387) · 📚 被引 15
- **作者**: Sai Saketh Rambhatla, Ishan Misra, Rama Chellappa, Abhinav Shrivastava
- **🏷️ 机构**: Meta, Johns Hopkins University, University of Maryland,College Park
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the challenging task of unsupervised object localization in this work. Recently, transformers trained with self-supervised learning have been shown to exhibit object localization properties without being trained for this task. In this work, we present Multiple Object localization with Self-supervised Transformers (MOST) that uses features of transformers trained using self-supervised learning to localize multiple objects in real world images. MOST analyzes the similarity maps of the features using box counting; a fractal analysis tool to identify tokens lying on foreground patches. The identified tokens are then clustered together, and tokens of each cluster are used to generate bounding boxes on foreground regions. Unlike recent state-of-the-art object localization methods, MOST can localize multiple objects per image and outperforms SOTA algorithms on several object localization and discovery benchmarks on PASCAL-VOC 07, 12 and COCO20k datasets. Additionally, we show that MOST can be used for self-supervised pre-training of object detectors, and yields consistent improvements on fully, semi-supervised object detection and unsupervised region proposal generation.

</details>

### Sempart: Self-supervised Multi-resolution Partitioning of Image Semantics.
- **链接**: [arXiv:2309.10972](https://arxiv.org/abs/2309.10972) · 📚 被引 4
- **作者**: Sriram Ravindran, Debraj Basu
- **🏷️ 机构**: Adobe
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately determining salient regions of an image is challenging when labeled data is scarce. DINO-based self-supervised approaches have recently leveraged meaningful image semantics captured by patch-wise features for locating foreground objects. Recent methods have also incorporated intuitive priors and demonstrated value in unsupervised methods for object partitioning. In this paper, we propose SEMPART, which jointly infers coarse and fine bi-partitions over an image's DINO-based semantic graph. Furthermore, SEMPART preserves fine boundary details using graph-driven regularization and successfully distills the coarse mask semantics into the fine mask. Our salient object detection and single object localization findings suggest that SEMPART produces high-quality masks rapidly without additional post-processing and benefits from co-optimizing the coarse and fine branches.

</details>

### L-DAWA: Layer-wise Divergence Aware Weight Aggregation in Federated Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2307.07393](https://arxiv.org/abs/2307.07393) · 📚 被引 23
- **作者**: Yasar Abbas Ur Rehman, Yan Gao, Pedro Porto Buarque de Gusmão, Mina Alibeigi, Jiajun Shen, Nicholas D. Lane
- **🏷️ 机构**: TCL AI Lab,Hong Kong, University of Cambridge,United Kingdom
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ubiquity of camera-enabled devices has led to large amounts of unlabeled image data being produced at the edge. The integration of self-supervised learning (SSL) and federated learning (FL) into one coherent system can potentially offer data privacy guarantees while also advancing the quality and robustness of the learned visual representations without needing to move data around. However, client bias and divergence during FL aggregation caused by data heterogeneity limits the performance of learned visual representations on downstream tasks. In this paper, we propose a new aggregation strategy termed Layer-wise Divergence Aware Weight Aggregation (L-DAWA) to mitigate the influence of client bias and divergence during FL aggregation. The proposed method aggregates weights at the layer-level according to the measure of angular divergence between the clients' model and the global model. Extensive experiments with cross-silo and cross-device settings on CIFAR-10/100 and Tiny ImageNet datasets demonstrate that our methods are effective and obtain new SOTA performance on both contrastive and non-contrastive SSL approaches.

</details>

### Time Does Tell: Self-Supervised Time-Tuning of Dense Image Representations.
- **链接**: [arXiv:2308.11796](https://arxiv.org/abs/2308.11796) · [代码](https://github.com/SMSD75/Timetuning) · 📚 被引 17
- **作者**: Mohammadreza Salehi, Efstratios Gavves, Cees G. M. Snoek, Yuki M. Asano
- **🏷️ 机构**: University of Amsterdam,QUVA Lab
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatially dense self-supervised learning is a rapidly growing problem domain with promising applications for unsupervised segmentation and pretraining for dense downstream tasks. Despite the abundance of temporal data in the form of videos, this information-rich source has been largely overlooked. Our paper aims to address this gap by proposing a novel approach that incorporates temporal consistency in dense self-supervised learning. While methods designed solely for images face difficulties in achieving even the same performance on videos, our method improves not only the representation quality for videos-but also images. Our approach, which we call time-tuning, starts from image-pretrained models and fine-tunes them with a novel self-supervised temporal-alignment clustering loss on unlabeled videos. This effectively facilitates the transfer of high-level information from videos to image representations. Time-tuning improves the state-of-the-art by 8-10% for unsupervised semantic segmentation on videos and matches it for images. We believe this method paves the way for further self-supervised scaling by leveraging the abundant availability of videos. The implementation can be found here : https://github.com/SMSD75/Timetuning

</details>

### STEPs: Self-Supervised Key Step Extraction and Localization from Unlabeled Procedural Videos.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00952) · 📚 被引 11
- **作者**: Anshul Shah, Benjamin Lundell, Harpreet Sawhney, Rama Chellappa
- **🏷️ 机构**: Johns Hopkins University, Microsoft Mixed Reality
- **会议**: ICCV 2023

### Self-supervised Learning to Bring Dual Reversed Rolling Shutter Images Alive.
- **链接**: [arXiv:2305.19862](https://arxiv.org/abs/2305.19862) · [代码](https://github.com/shangwei5/SelfDRSC) · 📚 被引 9
- **作者**: Wei Shang, Dongwei Ren, Chaoyu Feng, Xiaotao Wang, Lei Lei, Wangmeng Zuo
- **🏷️ 机构**: Harbin Institute of Technology,School of Computer Science and Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern consumer cameras usually employ the rolling shutter (RS) mechanism, where images are captured by scanning scenes row-by-row, yielding RS distortions for dynamic scenes. To correct RS distortions, existing methods adopt a fully supervised learning manner, where high framerate global shutter (GS) images should be collected as ground-truth supervision. In this paper, we propose a Self-supervised learning framework for Dual reversed RS distortions Correction (SelfDRSC), where a DRSC network can be learned to generate a high framerate GS video only based on dual RS images with reversed distortions. In particular, a bidirectional distortion warping module is proposed for reconstructing dual reversed RS images, and then a self-supervised loss can be deployed to train DRSC network by enhancing the cycle consistency between input and reconstructed dual reversed RS images. Besides start and end RS scanning time, GS images at arbitrary intermediate scanning time can also be supervised in SelfDRSC, thus enabling the learned DRSC network to generate a high framerate GS video. Moreover, a simple yet effective self-distillation strategy is introduced in self-supervised loss for mitigating boundary artifacts in generated GS images. On synthetic dataset, SelfDRSC achieves better or comparable quantitative metrics in comparison to state-of-the-art methods trained in the full supervision manner. On real-world RS cases, our SelfDRSC can produce high framerate GS videos with finer correction textures and better temporary consistency. The source code and trained models are made publicly available at https://github.com/shangwei5/SelfDRSC. We also provide an implementation in HUAWEI Mindspore at https://github.com/Hunter-Will/SelfDRSC-mindspore.

</details>

### FreeCOS: Self-Supervised Learning from Fractals and Unlabeled Images for Curvilinear Object Segmentation.
- **链接**: [arXiv:2307.07245](https://arxiv.org/abs/2307.07245) · [代码](https://github.com/TY-Shi/FreeCOS) · 📚 被引 18
- **作者**: Tianyi Shi, Xiaohuan Ding, Liang Zhang, Xin Yang
- **🏷️ 机构**: Huazhong University of Science &#x0026; Technology,School of EIC
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Curvilinear object segmentation is critical for many applications. However, manually annotating curvilinear objects is very time-consuming and error-prone, yielding insufficiently available annotated datasets for existing supervised methods and domain adaptation methods. This paper proposes a self-supervised curvilinear object segmentation method that learns robust and distinctive features from fractals and unlabeled images (FreeCOS). The key contributions include a novel Fractal-FDA synthesis (FFS) module and a geometric information alignment (GIA) approach. FFS generates curvilinear structures based on the parametric Fractal L-system and integrates the generated structures into unlabeled images to obtain synthetic training images via Fourier Domain Adaptation. GIA reduces the intensity differences between the synthetic and unlabeled images by comparing the intensity order of a given pixel to the values of its nearby neighbors. Such image alignment can explicitly remove the dependency on absolute intensity values and enhance the inherent geometric characteristics which are common in both synthetic and real images. In addition, GIA aligns features of synthetic and real images via the prediction space adaptation loss (PSAL) and the curvilinear mask contrastive loss (CMCL). Extensive experimental results on four public datasets, i.e., XCAD, DRIVE, STARE and CrackTree demonstrate that our method outperforms the state-of-the-art unsupervised methods, self-supervised methods and traditional methods by a large margin. The source code of this work is available at https://github.com/TY-Shi/FreeCOS.

</details>

### Learning by Sorting: Self-supervised Learning with Group Ordering Constraints.
- **链接**: [arXiv:2301.02009](https://arxiv.org/abs/2301.02009) · 📚 被引 7
- **作者**: Nina Shvetsova, Felix Petersen, Anna Kukleva, Bernt Schiele, Hilde Kuehne
- **🏷️ 机构**: Goethe University Frankfurt, Stanford University, Max-Planck-Institute for Informatics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has become an important tool in learning representations from unlabeled data mainly relying on the idea of minimizing distance between positive data pairs, e.g., views from the same images, and maximizing distance between negative data pairs, e.g., views from different images. This paper proposes a new variation of the contrastive learning objective, Group Ordering Constraints (GroCo), that leverages the idea of sorting the distances of positive and negative pairs and computing the respective loss based on how many positive pairs have a larger distance than the negative pairs, and thus are not ordered correctly. To this end, the GroCo loss is based on differentiable sorting networks, which enable training with sorting supervision by matching a differentiable permutation matrix, which is produced by sorting a given set of scores, to a respective ground truth permutation matrix. Applying this idea to groupwise pre-ordered inputs of multiple positive and negative pairs allows introducing the GroCo loss with implicit emphasis on strong positives and negatives, leading to better optimization of the local neighborhood. We evaluate the proposed formulation on various self-supervised learning benchmarks and show that it not only leads to improved results compared to vanilla contrastive learning but also shows competitive performance to comparable methods in linear probing and outperforms current methods in k-NN performance.

</details>

### Semantics-Consistent Feature Search for Self-Supervised Visual Representation Learning.
- **链接**: [arXiv:2212.06486](https://arxiv.org/abs/2212.06486) · 📚 被引 4
- **作者**: Kaiyou Song, Shan Zhang, Zimeng Luo, Tong Wang, Jin Xie
- **🏷️ 机构**: Megvii Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrastive self-supervised learning, the common way to learn discriminative representation is to pull different augmented "views" of the same image closer while pushing all other images further apart, which has been proven to be effective. However, it is unavoidable to construct undesirable views containing different semantic concepts during the augmentation procedure. It would damage the semantic consistency of representation to pull these augmentations closer in the feature space indiscriminately. In this study, we introduce feature-level augmentation and propose a novel semantics-consistent feature search (SCFS) method to mitigate this negative effect. The main idea of SCFS is to adaptively search semantics-consistent features to enhance the contrast between semantics-consistent regions in different augmentations. Thus, the trained model can learn to focus on meaningful object regions, improving the semantic representation ability. Extensive experiments conducted on different datasets and tasks demonstrate that SCFS effectively improves the performance of self-supervised learning and achieves state-of-the-art performance on different downstream tasks.

</details>

### MAPConNet: Self-supervised 3D Pose Transfer with Mesh and Point Contrastive Learning.
- **链接**: [arXiv:2304.13819](https://arxiv.org/abs/2304.13819) · 📚 被引 3
- **作者**: Jiaze Sun, Zhixiang Chen, Tae-Kyun Kim
- **🏷️ 机构**: Imperial College London, University of Sheffield
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D pose transfer is a challenging generation task that aims to transfer the pose of a source geometry onto a target geometry with the target identity preserved. Many prior methods require keypoint annotations to find correspondence between the source and target. Current pose transfer methods allow end-to-end correspondence learning but require the desired final output as ground truth for supervision. Unsupervised methods have been proposed for graph convolutional models but they require ground truth correspondence between the source and target inputs. We present a novel self-supervised framework for 3D pose transfer which can be trained in unsupervised, semi-supervised, or fully supervised settings without any correspondence labels. We introduce two contrastive learning constraints in the latent space: a mesh-level loss for disentangling global patterns including pose and identity, and a point-level loss for discriminating local semantics. We demonstrate quantitatively and qualitatively that our method achieves state-of-the-art results in supervised 3D pose transfer, with comparable results in unsupervised and semi-supervised settings. Our method is also generalisable to unseen human and animal data with complex topologies.

</details>

### Self-supervised Cross-view Representation Reconstruction for Change Captioning.
- **链接**: [arXiv:2309.16283](https://arxiv.org/abs/2309.16283) · [代码](https://github.com/tuyunbin/SCORER) · 📚 被引 33
- **作者**: Yunbin Tu, Liang Li, Li Su, Zheng-Jun Zha, Chenggang Yan, Qingming Huang
- **🏷️ 机构**: University of Chinese Academy of Sciences,Beijing,China, ICT, CAS,Key Lab of Intelligent Information Processing,Beijing,China, University of Science and Technology of China,Hefei,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Change captioning aims to describe the difference between a pair of similar images. Its key challenge is how to learn a stable difference representation under pseudo changes caused by viewpoint change. In this paper, we address this by proposing a self-supervised cross-view representation reconstruction (SCORER) network. Concretely, we first design a multi-head token-wise matching to model relationships between cross-view features from similar/dissimilar images. Then, by maximizing cross-view contrastive alignment of two similar images, SCORER learns two view-invariant image representations in a self-supervised way. Based on these, we reconstruct the representations of unchanged objects by cross-attention, thus learning a stable difference representation for caption generation. Further, we devise a cross-modal backward reasoning to improve the quality of caption. This module reversely models a ``hallucination'' representation with the caption and ``before'' representation. By pushing it closer to the ``after'' representation, we enforce the caption to be informative about the difference in a self-supervised manner. Extensive experiments show our method achieves the state-of-the-art results on four datasets. The code is available at https://github.com/tuyunbin/SCORER.

</details>

### Noise2Info: Noisy Image to Information of Noise for Self-Supervised Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01469) · 📚 被引 17
- **作者**: Jiachuan Wang, Shimin Di, Lei Chen, Charles Wang Wai Ng
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Hong Kong SAR,China
- **会议**: ICCV 2023

### Creative Birds: Self-Supervised Single-View 3D Style Transfer.
- **链接**: [arXiv:2307.14127](https://arxiv.org/abs/2307.14127) · [代码](https://github.com/wrk226/creative_birds) · 📚 被引 4
- **作者**: Renke Wang, Guimin Que, Shuo Chen, Xiang Li, Jun Li, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,China, RIKEN, Nankai University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel method for single-view 3D style transfer that generates a unique 3D object with both shape and texture transfer. Our focus lies primarily on birds, a popular subject in 3D reconstruction, for which no existing single-view 3D transfer methods have been developed.The method we propose seeks to generate a 3D mesh shape and texture of a bird from two single-view images. To achieve this, we introduce a novel shape transfer generator that comprises a dual residual gated network (DRGNet), and a multi-layer perceptron (MLP). DRGNet extracts the features of source and target images using a shared coordinate gate unit, while the MLP generates spatial coordinates for building a 3D mesh. We also introduce a semantic UV texture transfer module that implements textural style transfer using semantic UV segmentation, which ensures consistency in the semantic meaning of the transferred regions. This module can be widely adapted to many existing approaches. Finally, our method constructs a novel 3D bird using a differentiable renderer. Experimental results on the CUB dataset verify that our method achieves state-of-the-art performance on the single-view 3D style transfer task. Code is available in https://github.com/wrk226/creative_birds.

</details>

### Denoising Diffusion Autoencoders are Unified Self-supervised Learners.
- **链接**: [arXiv:2303.09769](https://arxiv.org/abs/2303.09769) · [代码](https://github.com/FutureXiang/ddae) · 📚 被引 62
- **作者**: Weilai Xiang, Hongyu Yang, Di Huang, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,Beijing,China, Beihang University,School of Computer Science and Engineering,Beijing,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by recent advances in diffusion models, which are reminiscent of denoising autoencoders, we investigate whether they can acquire discriminative representations for classification via generative pre-training. This paper shows that the networks in diffusion models, namely denoising diffusion autoencoders (DDAE), are unified self-supervised learners: by pre-training on unconditional image generation, DDAE has already learned strongly linear-separable representations within its intermediate layers without auxiliary encoders, thus making diffusion pre-training emerge as a general approach for generative-and-discriminative dual learning. To validate this, we conduct linear probe and fine-tuning evaluations. Our diffusion-based approach achieves 95.9% and 50.0% linear evaluation accuracies on CIFAR-10 and Tiny-ImageNet, respectively, and is comparable to contrastive learning and masked autoencoders for the first time. Transfer learning from ImageNet also confirms the suitability of DDAE for Vision Transformers, suggesting the potential to scale DDAEs as unified foundation models. Code is available at github.com/FutureXiang/ddae.

</details>

### Stable and Causal Inference for Discriminative Self-supervised Deep Visual Representations.
- **链接**: [arXiv:2308.08321](https://arxiv.org/abs/2308.08321) · 📚 被引 1
- **作者**: Yuewei Yang, Hai Li, Yiran Chen
- **🏷️ 机构**: Duke University,Durham,USA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, discriminative self-supervised methods have made significant strides in advancing various visual tasks. The central idea of learning a data encoder that is robust to data distortions/augmentations is straightforward yet highly effective. Although many studies have demonstrated the empirical success of various learning methods, the resulting learned representations can exhibit instability and hinder downstream performance. In this study, we analyze discriminative self-supervised methods from a causal perspective to explain these unstable behaviors and propose solutions to overcome them. Our approach draws inspiration from prior works that empirically demonstrate the ability of discriminative self-supervised methods to demix ground truth causal sources to some extent. Unlike previous work on causality-empowered representation learning, we do not apply our solutions during the training process but rather during the inference process to improve time efficiency. Through experiments on both controlled image datasets and realistic image datasets, we show that our proposed solutions, which involve tempering a linear transformation with controlled synthetic data, are effective in addressing these issues.

</details>

### Self-supervised Learning of Implicit Shape Representation with Dense Correspondence for Deformable Objects.
- **链接**: [arXiv:2308.12590](https://arxiv.org/abs/2308.12590) · 📚 被引 4
- **作者**: Baowen Zhang, Jiahe Li, Xiaoming Deng, Yinda Zhang, Cuixia Ma, Hongan Wang
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Software, Google
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning 3D shape representation with dense correspondence for deformable objects is a fundamental problem in computer vision. Existing approaches often need additional annotations of specific semantic domain, e.g., skeleton poses for human bodies or animals, which require extra annotation effort and suffer from error accumulation, and they are limited to specific domain. In this paper, we propose a novel self-supervised approach to learn neural implicit shape representation for deformable objects, which can represent shapes with a template shape and dense correspondence in 3D. Our method does not require the priors of skeleton and skinning weight, and only requires a collection of shapes represented in signed distance fields. To handle the large deformation, we constrain the learned template shape in the same latent space with the training shapes, design a new formulation of local rigid constraint that enforces rigid transformation in local region and addresses local reflection issue, and present a new hierarchical rigid constraint to reduce the ambiguity due to the joint learning of template shape and correspondences. Extensive experiments show that our model can represent shapes with large deformations. We also show that our shape representation can support two typical applications, such as texture transfer and shape editing, with competitive performance. The code and models are available at https://iscas3dv.github.io/deformshape

</details>

### Modeling the Relative Visual Tempo for Self-supervised Skeleton-based Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01279) · 📚 被引 35
- **作者**: Yisheng Zhu, Hu Han, Zhengtao Yu, Guangcan Liu
- **🏷️ 机构**: Nanjing University of Posts and Telecommunications, Chinese Academy of Sciences (CAS),Key Laboratory of Intelligent Information Processing, Institute of Computing Technology (ICT), Kunming University of Science and Technology,Faculty of Information Engineering and Automation
- **会议**: ICCV 2023

### Multi-Label Self-Supervised Learning with Scene Images.
- **链接**: [arXiv:2308.03286](https://arxiv.org/abs/2308.03286) · 📚 被引 17
- **作者**: Ke Zhu, Minghao Fu, Jianxin Wu
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) methods targeting scene images have seen a rapid growth recently, and they mostly rely on either a dedicated dense matching mechanism or a costly unsupervised object discovery module. This paper shows that instead of hinging on these strenuous operations, quality image representations can be learned by treating scene/multi-label image SSL simply as a multi-label classification problem, which greatly simplifies the learning framework. Specifically, multiple binary pseudo-labels are assigned for each input image by comparing its embeddings with those in two dictionaries, and the network is optimized using the binary cross entropy loss. The proposed method is named Multi-Label Self-supervised learning (MLS). Visualizations qualitatively show that clearly the pseudo-labels by MLS can automatically find semantically similar pseudo-positive pairs across different images to facilitate contrastive learning. MLS learns high quality representations on MS-COCO and achieves state-of-the-art results on classification, detection and segmentation benchmarks. At the same time, MLS is much simpler than existing methods, making it easier to deploy and for further exploration.

</details>

### Iterative Denoiser and Noise Estimator for Self-Supervised Image Denoising.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01220) · 📚 被引 17
- **作者**: Yunhao Zou, Chenggang Yan, Ying Fu
- **🏷️ 机构**: Beijing Institute of Technology, Hangzhou Dianzi University
- **会议**: ICCV 2023

### Can Self-Supervised Representation Learning Methods Withstand Distribution Shifts and Corruptions?
- **链接**: [arXiv:2308.02525](https://arxiv.org/abs/2308.02525) · 📚 被引 6
- **作者**: Prakash Chandra Chhipa, Johan Rodahl Holmgren, Kanjar De, Rajkumar Saini, Marcus Liwicki
- **🏷️ 机构**: Lule&#x00E5; Tekniska Universitet,Machine Learning Group, EISLAB,Lule&#x00E5;,Sweden
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning in computer vision aims to leverage the inherent structure and relationships within data to learn meaningful representations without explicit human annotation, enabling a holistic understanding of visual scenes. Robustness in vision machine learning ensures reliable and consistent performance, enhancing generalization, adaptability, and resistance to noise, variations, and adversarial attacks. Self-supervised paradigms, namely contrastive learning, knowledge distillation, mutual information maximization, and clustering, have been considered to have shown advances in invariant learning representations. This work investigates the robustness of learned representations of self-supervised learning approaches focusing on distribution shifts and image corruptions in computer vision. Detailed experiments have been conducted to study the robustness of self-supervised learning methods on distribution shifts and image corruptions. The empirical analysis demonstrates a clear relationship between the performance of learned representations within self-supervised paradigms and the severity of distribution shifts and corruptions. Notably, higher levels of shifts and corruptions are found to significantly diminish the robustness of the learned representations. These findings highlight the critical impact of distribution shifts and image corruptions on the performance and resilience of self-supervised learning methods, emphasizing the need for effective strategies to mitigate their adverse effects. The study strongly advocates for future research in the field of self-supervised representation learning to prioritize the key aspects of safety and robustness in order to ensure practical applicability. The source code and results are available on GitHub.

</details>

### Contrastive Image Synthesis and Self-supervised Feature Adaptation for Cross-Modality Biomedical Image Segmentation.
- **链接**: [arXiv:2207.13240](https://arxiv.org/abs/2207.13240) · 📚 被引 3
- **作者**: Xinrong Hu, Corey Wang, Yiyu Shi
- **🏷️ 机构**: University of Notre Dame,Department of Computer Science and Engineering, Northwestern University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work presents a novel framework CISFA (Contrastive Image synthesis and Self-supervised Feature Adaptation)that builds on image domain translation and unsupervised feature adaptation for cross-modality biomedical image segmentation. Different from existing works, we use a one-sided generative model and add a weighted patch-wise contrastive loss between sampled patches of the input image and the corresponding synthetic image, which serves as shape constraints. Moreover, we notice that the generated images and input images share similar structural information but are in different modalities. As such, we enforce contrastive losses on the generated images and the input images to train the encoder of a segmentation model to minimize the discrepancy between paired images in the learned embedding space. Compared with existing works that rely on adversarial learning for feature adaptation, such a method enables the encoder to learn domain-independent features in a more explicit way. We extensively evaluate our methods on segmentation tasks containing CT and MRI images for abdominal cavities and whole hearts. Experimental results show that the proposed framework not only outputs synthetic images with less distortion of organ shapes, but also outperforms state-of-the-art domain adaptation methods by a large margin.

</details>

### Self-supervised Semantic Segmentation: Consistency over Transformation.
- **链接**: [arXiv:2309.00143](https://arxiv.org/abs/2309.00143) · [代码](https://github.com/mindflow-institue/SSCT) · 📚 被引 6
- **作者**: Sanaz Karimijafarbigloo, Reza Azad, Amirhossein Kazerouni, Yury Velichko, Ulas Bagci, Dorit Merhof
- **🏷️ 机构**: University of Regensburg,Faculty of Informatics and Data Science,Germany, RWTH Aachen University,Faculty of Electrical Engineering and Information Technology,Germany, Iran University of Science and Technology,School of Electrical Engineering,Iran
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate medical image segmentation is of utmost importance for enabling automated clinical decision procedures. However, prevailing supervised deep learning approaches for medical image segmentation encounter significant challenges due to their heavy dependence on extensive labeled training data. To tackle this issue, we propose a novel self-supervised algorithm, \textbf{S$^3$-Net}, which integrates a robust framework based on the proposed Inception Large Kernel Attention (I-LKA) modules. This architectural enhancement makes it possible to comprehensively capture contextual information while preserving local intricacies, thereby enabling precise semantic segmentation. Furthermore, considering that lesions in medical images often exhibit deformations, we leverage deformable convolution as an integral component to effectively capture and delineate lesion deformations for superior object boundary definition. Additionally, our self-supervised strategy emphasizes the acquisition of invariance to affine transformations, which is commonly encountered in medical scenarios. This emphasis on robustness with respect to geometric distortions significantly enhances the model's ability to accurately model and handle such distortions. To enforce spatial consistency and promote the grouping of spatially connected image pixels with similar feature representations, we introduce a spatial consistency loss term. This aids the network in effectively capturing the relationships among neighboring pixels and enhancing the overall segmentation quality. The S$^3$-Net approach iteratively learns pixel-level feature representations for image content clustering in an end-to-end manner. Our experimental results on skin lesion and lung organ segmentation tasks show the superior performance of our method compared to the SOTA approaches. https://github.com/mindflow-institue/SSCT

</details>

### NU-Net: a self-supervised smart filter for enhancing blobs in bioimages.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00420) · 📚 被引 0
- **作者**: Seongbin Lim, Emmanuel Beaurepaire, Anatole Chessel
- **🏷️ 机构**: Institut Polytechnique de Paris,Laboratoire d&#x2019;Optique et Biosciences, CNRS, INSERM, &#x00C9;cole Polytechnique,Cedex,France
- **会议**: ICCV 2023

### Frequency-Aware Self-Supervised Long-Tailed Learning.
- **链接**: [arXiv:2309.04723](https://arxiv.org/abs/2309.04723) · 📚 被引 0
- **作者**: Ci-Siang Lin, Min-Hung Chen, Yu-Chiang Frank Wang
- **🏷️ 机构**: National Taiwan University,Graduate Institute of Communication Engineering,Taiwan, Nvidia,Taiwan
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data collected from the real world typically exhibit long-tailed distributions, where frequent classes contain abundant data while rare ones have only a limited number of samples. While existing supervised learning approaches have been proposed to tackle such data imbalance, the requirement of label supervision would limit their applicability to real-world scenarios in which label annotation might not be available. Without the access to class labels nor the associated class frequencies, we propose Frequency-Aware Self-Supervised Learning (FASSL) in this paper. Targeting at learning from unlabeled data with inherent long-tailed distributions, the goal of FASSL is to produce discriminative feature representations for downstream classification tasks. In FASSL, we first learn frequency-aware prototypes, reflecting the associated long-tailed distribution. Particularly focusing on rare-class samples, the relationships between image data and the derived prototypes are further exploited with the introduced self-supervised learning scheme. Experiments on long-tailed image datasets quantitatively and qualitatively verify the effectiveness of our learning scheme.

</details>

### Self-supervised Hypergraphs for Learning Multiple World Interpretations.
- **链接**: [arXiv:2308.07615](https://arxiv.org/abs/2308.07615) · 📚 被引 9
- **作者**: Alina Marcu, Mihai Cristian Pîrvu, Dragos Costea, Emanuela Haller, Emil Slusanschi, Nabil Belbachir et al.
- **🏷️ 机构**: UPB, Bitdefender, NORCE
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a method for learning multiple scene representations given a small labeled set, by exploiting the relationships between such representations in the form of a multi-task hypergraph. We also show how we can use the hypergraph to improve a powerful pretrained VisTransformer model without any additional labeled data. In our hypergraph, each node is an interpretation layer (e.g., depth or segmentation) of the scene. Within each hyperedge, one or several input nodes predict the layer at the output node. Thus, each node could be an input node in some hyperedges and an output node in others. In this way, multiple paths can reach the same node, to form ensembles from which we obtain robust pseudolabels, which allow self-supervised learning in the hypergraph. We test different ensemble models and different types of hyperedges and show superior performance to other multi-task graph models in the field. We also introduce Dronescapes, a large video dataset captured with UAVs in different complex real-world scenes, with multiple representations, suitable for multi-task learning.

</details>

### DeepVAT: A Self-Supervised Technique for Cluster Assessment in Image Datasets.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00026) · 📚 被引 2
- **作者**: Alokendu Mazumder, Tirthajit Baruah, Akash Kumar Singh, Pagadala Krishna Murthy, Vishwajeet Pattanaik, Punit Rathore
- **🏷️ 机构**: Indian Institute of Science Bangalore,India, Indian Institute of Science Education and Research Bhopal,India
- **会议**: ICCV 2023

### Self-Supervised Anomaly Detection from Anomalous Training Data via Iterative Latent Token Masking.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00254) · 📚 被引 6
- **作者**: Ashay Patel, Petru-Daniel Tudosiu, Walter H. L. Pinaya, Mark S. Graham, Olusola Adeleke, Gary J. Cook et al.
- **🏷️ 机构**: King&#x2019;s College,London
- **会议**: ICCV 2023

### FedLID: Self-Supervised Federated Learning for Leveraging Limited Image Data.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00111) · 📚 被引 6
- **作者**: Athanasios Psaltis, Anestis Kastellos, Charalampos Z. Patrikakis, Petros Daras
- **🏷️ 机构**: Centre for Research and Technology Hellas,Thessaloniki,Greece, University of West Attica,Dept. of Electrical and Electronics Engineering,Athens,Greece
- **会议**: ICCV 2023

### Self-supervised Learning of Contextualized Local Visual Embeddings.
- **链接**: [arXiv:2310.00527](https://arxiv.org/abs/2310.00527) · 📚 被引 2
- **作者**: Thalles Silva, Hélio Pedrini, Adín Ramírez Rivera
- **🏷️ 机构**: University of Campinas,Institute of Computing,Campinas-SP,Brazil, University of Oslo,Department of Informatics,Oslo,Norway
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Contextualized Local Visual Embeddings (CLoVE), a self-supervised convolutional-based method that learns representations suited for dense prediction tasks. CLoVE deviates from current methods and optimizes a single loss function that operates at the level of contextualized local embeddings learned from output feature maps of convolution neural network (CNN) encoders. To learn contextualized embeddings, CLoVE proposes a normalized mult-head self-attention layer that combines local features from different parts of an image based on similarity. We extensively benchmark CLoVE's pre-trained representations on multiple datasets. CLoVE reaches state-of-the-art performance for CNN-based architectures in 4 dense prediction downstream tasks, including object detection, instance segmentation, keypoint detection, and dense pose estimation.

</details>

### A Horse with no Labels: Self-Supervised Horse Pose Estimation from Unlabelled Images and Synthetic Prior.
- **链接**: [arXiv:2308.03411](https://arxiv.org/abs/2308.03411) · 📚 被引 0
- **作者**: Jose Sosa, David C. Hogg
- **🏷️ 机构**: University of Leeds,School of Computing
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Obtaining labelled data to train deep learning methods for estimating animal pose is challenging. Recently, synthetic data has been widely used for pose estimation tasks, but most methods still rely on supervised learning paradigms utilising synthetic images and labels. Can training be fully unsupervised? Is a tiny synthetic dataset sufficient? What are the minimum assumptions that we could make for estimating animal pose? Our proposal addresses these questions through a simple yet effective self-supervised method that only assumes the availability of unlabelled images and a small set of synthetic 2D poses. We completely remove the need for any 3D or 2D pose annotations (or complex 3D animal models), and surprisingly our approach can still learn accurate 3D and 2D poses simultaneously. We train our method with unlabelled images of horses mainly collected for YouTube videos and a prior consisting of 2D synthetic poses. The latter is three times smaller than the number of images needed for training. We test our method on a challenging set of horse images and evaluate the predicted 3D and 2D poses. We demonstrate that it is possible to learn accurate animal poses even with as few assumptions as unlabelled images and a small set of 2D poses generated from synthetic data. Given the minimum requirements and the abundance of unlabelled data, our method could be easily deployed to different animals.

</details>

### OMG-Attack: Self-Supervised On-Manifold Generation of Transferable Evasion Attacks.
- **链接**: [arXiv:2310.03707](https://arxiv.org/abs/2310.03707) · 📚 被引 1
- **作者**: Ofir Bar Tal, Adi Haviv, Amit H. Bermano
- **🏷️ 机构**: Tel Aviv University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Evasion Attacks (EA) are used to test the robustness of trained neural networks by distorting input data to misguide the model into incorrect classifications. Creating these attacks is a challenging task, especially with the ever-increasing complexity of models and datasets. In this work, we introduce a self-supervised, computationally economical method for generating adversarial examples, designed for the unseen black-box setting. Adapting techniques from representation learning, our method generates on-manifold EAs that are encouraged to resemble the data distribution. These attacks are comparable in effectiveness compared to the state-of-the-art when attacking the model trained on, but are significantly more effective when attacking unseen models, as the attacks are more related to the data rather than the model itself. Our experiments consistently demonstrate the method is effective across various models, unseen data categories, and even defended models, suggesting a significant role for on-manifold EAs when targeting unseen models.

</details>

### Efficient, Self-Supervised Human Pose Estimation with Inductive Prior Tuning.
- **链接**: [arXiv:2311.02815](https://arxiv.org/abs/2311.02815) · 📚 被引 2
- **作者**: Nobline Yoo, Olga Russakovsky
- **🏷️ 机构**: Princeton University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of 2D human pose estimation (HPE) is to localize anatomical landmarks, given an image of a person in a pose. SOTA techniques make use of thousands of labeled figures (finetuning transformers or training deep CNNs), acquired using labor-intensive crowdsourcing. On the other hand, self-supervised methods re-frame the HPE task as a reconstruction problem, enabling them to leverage the vast amount of unlabeled visual data, though at the present cost of accuracy. In this work, we explore ways to improve self-supervised HPE. We (1) analyze the relationship between reconstruction quality and pose estimation accuracy, (2) develop a model pipeline that outperforms the baseline which inspired our work, using less than one-third the amount of training data, and (3) offer a new metric suitable for self-supervised settings that measures the consistency of predicted body part length proportions. We show that a combination of well-engineered reconstruction losses and inductive priors can help coordinate pose learning alongside reconstruction in a self-supervised paradigm.

</details>

### Pointing Gesture Recognition via Self-supervised Regularization for ASD Screening.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00326) · 📚 被引 3
- **作者**: Cheol-Hwan Yoo, Jang-Hee Yoo, Ho-Won Kim, ByungOk Han
- **🏷️ 机构**: ETRI,Daejeon,Republic of Korea
- **会议**: ICCV 2023

### Contrastive Learning Relies More on Spatial Inductive Bias Than Supervised Learning: An Empirical Study.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01496) · 📚 被引 3
- **作者**: Yuanyi Zhong, Haoran Tang, Jun-Kun Chen, Yu-Xiong Wang
- **🏷️ 机构**: University of Illinois at Urbana-Champaign, University of Pennsylvania
- **会议**: ICCV 2023

### One-shot recognition of any material anywhere using contrastive learning with physics-based rendering.
- **链接**: [arXiv:2212.00648](https://arxiv.org/abs/2212.00648) · 📚 被引 8
- **作者**: Manuel S. Drehwald, Sagi Eppel, Jolina Li, Han Hao, Alán Aspuru-Guzik
- **🏷️ 机构**: Karlsruhe Institute of Technology, Vector Institute, University of Toronto
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual recognition of materials and their states is essential for understanding most aspects of the world, from determining whether food is cooked, metal is rusted, or a chemical reaction has occurred. However, current image recognition methods are limited to specific classes and properties and can't handle the vast number of material states in the world. To address this, we present MatSim: the first dataset and benchmark for computer vision-based recognition of similarities and transitions between materials and textures, focusing on identifying any material under any conditions using one or a few examples. The dataset contains synthetic and natural images. The synthetic images were rendered using giant collections of textures, objects, and environments generated by computer graphics artists. We use mixtures and gradual transitions between materials to allow the system to learn cases with smooth transitions between states (like gradually cooked food). We also render images with materials inside transparent containers to support beverage and chemistry lab use cases. We use this dataset to train a siamese net that identifies the same material in different objects, mixtures, and environments. The descriptor generated by this net can be used to identify the states of materials and their subclasses using a single image. We also present the first few-shot material recognition benchmark with images from a wide range of fields, including the state of foods and drinks, types of grounds, and many other use cases. We show that a net trained on the MatSim synthetic dataset outperforms state-of-the-art models like Clip on the benchmark and also achieves good results on other unsupervised material classification tasks.

</details>

### All4One: Symbiotic Neighbour Contrastive Learning via Self-Attention and Redundancy Reduction.
- **链接**: [arXiv:2303.09417](https://arxiv.org/abs/2303.09417) · 📚 被引 12
- **作者**: Imanol G. Estepa, Ignacio Sarasúa, Bhalaji Nagarajan, Petia Radeva
- **🏷️ 机构**: Universitat de Barcelona,Barcelona,Spain, NVIDIA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Nearest neighbour based methods have proved to be one of the most successful self-supervised learning (SSL) approaches due to their high generalization capabilities. However, their computational efficiency decreases when more than one neighbour is used. In this paper, we propose a novel contrastive SSL approach, which we call All4One, that reduces the distance between neighbour representations using ''centroids'' created through a self-attention mechanism. We use a Centroid Contrasting objective along with single Neighbour Contrasting and Feature Contrasting objectives. Centroids help in learning contextual information from multiple neighbours whereas the neighbour contrast enables learning representations directly from the neighbours and the feature contrast allows learning representations unique to the features. This combination enables All4One to outperform popular instance discrimination approaches by more than 1% on linear classification evaluation for popular benchmark datasets and obtains state-of-the-art (SoTA) results. Finally, we show that All4One is robust towards embedding dimensionalities and augmentations, surpassing NNCLR and Barlow Twins by more than 5% on low dimensionality and weak augmentation settings. The source code would be made available soon.

</details>

### Hierarchical Contrastive Learning for Pattern-Generalizable Image Corruption Detection.
- **链接**: [arXiv:2308.14061](https://arxiv.org/abs/2308.14061) · [代码](https://github.com/xyfJASON/HCL) · 📚 被引 5
- **作者**: Xin Feng, Yifeng Xu, Guangming Lu, Wenjie Pei
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Effective image restoration with large-size corruptions, such as blind image inpainting, entails precise detection of corruption region masks which remains extremely challenging due to diverse shapes and patterns of corruptions. In this work, we present a novel method for automatic corruption detection, which allows for blind corruption restoration without known corruption masks. Specifically, we develop a hierarchical contrastive learning framework to detect corrupted regions by capturing the intrinsic semantic distinctions between corrupted and uncorrupted regions. In particular, our model detects the corrupted mask in a coarse-to-fine manner by first predicting a coarse mask by contrastive learning in low-resolution feature space and then refines the uncertain area of the mask by high-resolution contrastive learning. A specialized hierarchical interaction mechanism is designed to facilitate the knowledge propagation of contrastive learning in different scales, boosting the modeling performance substantially. The detected multi-scale corruption masks are then leveraged to guide the corruption restoration. Detecting corrupted regions by learning the contrastive distinctions rather than the semantic patterns of corruptions, our model has well generalization ability across different corruption patterns. Extensive experiments demonstrate following merits of our model: 1) the superior performance over other methods on both corruption detection and various image restoration tasks including blind inpainting and watermark removal, and 2) strong generalization across different corruption patterns such as graffiti, random noise or other image content. Codes and trained weights are available at https://github.com/xyfJASON/HCL .

</details>

### Subclass-balancing Contrastive Learning for Long-tailed Recognition.
- **链接**: [arXiv:2306.15925](https://arxiv.org/abs/2306.15925) · 📚 被引 44
- **作者**: Chengkai Hou, Jieyu Zhang, Haonan Wang, Tianyi Zhou
- **🏷️ 机构**: Jilin University, University of Washington, National University of Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-tailed recognition with imbalanced class distribution naturally emerges in practical machine learning applications. Existing methods such as data reweighing, resampling, and supervised contrastive learning enforce the class balance with a price of introducing imbalance between instances of head class and tail class, which may ignore the underlying rich semantic substructures of the former and exaggerate the biases in the latter. We overcome these drawbacks by a novel ``subclass-balancing contrastive learning (SBCL)'' approach that clusters each head class into multiple subclasses of similar sizes as the tail classes and enforce representations to capture the two-layer class hierarchy between the original classes and their subclasses. Since the clustering is conducted in the representation space and updated during the course of training, the subclass labels preserve the semantic substructures of head classes. Meanwhile, it does not overemphasize tail class samples, so each individual instance contribute to the representation learning equally. Hence, our method achieves both the instance- and subclass-balance, while the original class labels are also learned through contrastive learning among subclasses from different classes. We evaluate SBCL over a list of long-tailed benchmark datasets and it achieves the state-of-the-art performance. In addition, we present extensive analyses and ablation studies of SBCL to verify its advantages.

</details>

### Unsupervised Domain Adaptation for Training Event-Based Networks Using Contrastive Learning and Uncorrelated Conditioning.
- **链接**: [arXiv:2303.12424](https://arxiv.org/abs/2303.12424) · 📚 被引 15
- **作者**: Dayuan Jian, Mohammad Rostami
- **🏷️ 机构**: University of Southern California
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Event-based cameras offer reliable measurements for preforming computer vision tasks in high-dynamic range environments and during fast motion maneuvers. However, adopting deep learning in event-based vision faces the challenge of annotated data scarcity due to recency of event cameras. Transferring the knowledge that can be obtained from conventional camera annotated data offers a practical solution to this challenge. We develop an unsupervised domain adaptation algorithm for training a deep network for event-based data image classification using contrastive learning and uncorrelated conditioning of data. Our solution outperforms the existing algorithms for this purpose.

</details>

### SCOB: Universal Text Understanding via Character-wise Supervised Contrastive Learning with Online Text Rendering for Bridging Domain Gap.
- **链接**: [arXiv:2309.12382](https://arxiv.org/abs/2309.12382) · [代码](https://github.com/naver-ai/scob) · 📚 被引 3
- **作者**: Daehee Kim, Yoonsik Kim, Donghyun Kim, Yumin Lim, Geewook Kim, Taeho Kil
- **🏷️ 机构**: NAVER Cloud AI, Seoul National University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by the great success of language model (LM)-based pre-training, recent studies in visual document understanding have explored LM-based pre-training methods for modeling text within document images. Among them, pre-training that reads all text from an image has shown promise, but often exhibits instability and even fails when applied to broader domains, such as those involving both visual documents and scene text images. This is a substantial limitation for real-world scenarios, where the processing of text image inputs in diverse domains is essential. In this paper, we investigate effective pre-training tasks in the broader domains and also propose a novel pre-training method called SCOB that leverages character-wise supervised contrastive learning with online text rendering to effectively pre-train document and scene text domains by bridging the domain gap. Moreover, SCOB enables weakly supervised learning, significantly reducing annotation costs. Extensive benchmarks demonstrate that SCOB generally improves vanilla pre-training methods and achieves comparable performance to state-of-the-art methods. Our findings suggest that SCOB can be served generally and effectively for read-type pre-training methods. The code will be available at https://github.com/naver-ai/scob.

</details>

### SeeABLE: Soft Discrepancies and Bounded Contrastive Learning for Exposing Deepfakes.
- **链接**: [arXiv:2211.11296](https://arxiv.org/abs/2211.11296) · 📚 被引 48
- **作者**: Nicolas Larue, Ngoc-Son Vu, Vitomir Struc, Peter Peer, Vassilis Christophides
- **🏷️ 机构**: ETIS - CY Cergy Paris University,ENSEA, CNRS,France, University of Ljubljana,Slovenia
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern deepfake detectors have achieved encouraging results, when training and test images are drawn from the same data collection. However, when these detectors are applied to images produced with unknown deepfake-generation techniques, considerable performance degradations are commonly observed. In this paper, we propose a novel deepfake detector, called SeeABLE, that formalizes the detection problem as a (one-class) out-of-distribution detection task and generalizes better to unseen deepfakes. Specifically, SeeABLE first generates local image perturbations (referred to as soft-discrepancies) and then pushes the perturbed faces towards predefined prototypes using a novel regression-based bounded contrastive loss. To strengthen the generalization performance of SeeABLE to unknown deepfake types, we generate a rich set of soft discrepancies and train the detector: (i) to localize, which part of the face was modified, and (ii) to identify the alteration type. To demonstrate the capabilities of SeeABLE, we perform rigorous experiments on several widely-used deepfake datasets and show that our model convincingly outperforms competing state-of-the-art detectors, while exhibiting highly encouraging generalization capabilities.

</details>

### JOTR: 3D Joint Contrastive Learning with Transformers for Occluded Human Mesh Recovery.
- **链接**: [arXiv:2307.16377](https://arxiv.org/abs/2307.16377) · 📚 被引 27
- **作者**: Jiahao Li, Zongxin Yang, Xiaohan Wang, Jianxin Ma, Chang Zhou, Yi Yang
- **🏷️ 机构**: Zhejiang University,ReLER, CCAI, Alibaba Group,DAMO Academy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we focus on the problem of 3D human mesh recovery from a single image under obscured conditions. Most state-of-the-art methods aim to improve 2D alignment technologies, such as spatial averaging and 2D joint sampling. However, they tend to neglect the crucial aspect of 3D alignment by improving 3D representations. Furthermore, recent methods struggle to separate the target human from occlusion or background in crowded scenes as they optimize the 3D space of target human with 3D joint coordinates as local supervision. To address these issues, a desirable method would involve a framework for fusing 2D and 3D features and a strategy for optimizing the 3D space globally. Therefore, this paper presents 3D JOint contrastive learning with TRansformers (JOTR) framework for handling occluded 3D human mesh recovery. Our method includes an encoder-decoder transformer architecture to fuse 2D and 3D representations for achieving 2D$\&$3D aligned results in a coarse-to-fine manner and a novel 3D joint contrastive learning approach for adding explicitly global supervision for the 3D feature space. The contrastive learning approach includes two contrastive losses: joint-to-joint contrast for enhancing the similarity of semantically similar voxels (i.e., human joints), and joint-to-non-joint contrast for ensuring discrimination from others (e.g., occlusions and background). Qualitative and quantitative analyses demonstrate that our method outperforms state-of-the-art competitors on both occlusion-specific and standard benchmarks, significantly improving the reconstruction of occluded humans.

</details>

### Semantic Information in Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00523)
- **作者**: Shengjiang Quan, Masahiro Hirano, Yuji Yamakawa
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Scene Graph Contrastive Learning for Embodied Navigation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00999) · 📚 被引 21
- **作者**: Kunal Pratap Singh, Jordi Salvador, Luca Weihs, Aniruddha Kembhavi
- **🏷️ 机构**: Allen Institute for AI
- **会议**: ICCV 2023

### Unilaterally Aggregated Contrastive Learning with Hierarchical Augmentation for Anomaly Detection.
- **链接**: [arXiv:2308.10155](https://arxiv.org/abs/2308.10155) · 📚 被引 5
- **作者**: Guodong Wang, Yunhong Wang, Jie Qin, Dongming Zhang, Xiuguo Bao, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, Beihang University,School of Computer Science and Engineering,Beijing,China, NUAA,College of Computer Science and Technology,Nanjing,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection (AD), aiming to find samples that deviate from the training distribution, is essential in safety-critical applications. Though recent self-supervised learning based attempts achieve promising results by creating virtual outliers, their training objectives are less faithful to AD which requires a concentrated inlier distribution as well as a dispersive outlier distribution. In this paper, we propose Unilaterally Aggregated Contrastive Learning with Hierarchical Augmentation (UniCon-HA), taking into account both the requirements above. Specifically, we explicitly encourage the concentration of inliers and the dispersion of virtual outliers via supervised and unsupervised contrastive losses, respectively. Considering that standard contrastive data augmentation for generating positive views may induce outliers, we additionally introduce a soft mechanism to re-weight each augmented inlier according to its deviation from the inlier distribution, to ensure a purified concentration. Moreover, to prompt a higher concentration, inspired by curriculum learning, we adopt an easy-to-hard hierarchical augmentation strategy and perform contrastive aggregation at different depths of the network based on the strengths of data augmentation. Our method is evaluated under three AD settings including unlabeled one-class, unlabeled multi-class, and labeled multi-class, demonstrating its consistent superiority over other competitors.

</details>

### Boosting Novel Category Discovery Over Domains with Soft Contrastive Learning and All in One Classifier.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01089) · 📚 被引 18
- **作者**: Zelin Zang, Lei Shang, Senqiao Yang, Fei Wang, Baigui Sun, Xuansong Xie et al.
- **🏷️ 机构**: Westlake University, Alibaba Group
- **会议**: ICCV 2023

### Weakly-Supervised Text-driven Contrastive Learning for Facial Behavior Understanding.
- **链接**: [arXiv:2304.00058](https://arxiv.org/abs/2304.00058) · 📚 被引 23
- **作者**: Xiang Zhang, Taoyue Wang, Xiaotian Li, Huiyuan Yang, Lijun Yin
- **🏷️ 机构**: State University of New York,Binghamton, Rice University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive learning has shown promising potential for learning robust representations by utilizing unlabeled data. However, constructing effective positive-negative pairs for contrastive learning on facial behavior datasets remains challenging. This is because such pairs inevitably encode the subject-ID information, and the randomly constructed pairs may push similar facial images away due to the limited number of subjects in facial behavior datasets. To address this issue, we propose to utilize activity descriptions, coarse-grained information provided in some datasets, which can provide high-level semantic information about the image sequences but is often neglected in previous studies. More specifically, we introduce a two-stage Contrastive Learning with Text-Embeded framework for Facial behavior understanding (CLEF). The first stage is a weakly-supervised contrastive learning method that learns representations from positive-negative pairs constructed using coarse-grained activity information. The second stage aims to train the recognition of facial expressions or facial action units by maximizing the similarity between image and the corresponding text label names. The proposed CLEF achieves state-of-the-art performance on three in-the-lab datasets for AU recognition and three in-the-wild datasets for facial expression recognition.

</details>

### Pre-training-free Image Manipulation Localization through Non-Mutually Exclusive Contrastive Learning.
- **链接**: [arXiv:2309.14900](https://arxiv.org/abs/2309.14900) · [代码](https://github.com/Knightzjz/NCL-IML) · 📚 被引 49
- **作者**: Jizhe Zhou, Xiaochen Ma, Xia Du, Ahmed Y. Al Hammadi, Wentao Feng
- **🏷️ 机构**: Sichuan University,College of Computer Science, Xiamen University of Technology,School of Computer and Information Engineering, Mohamed Bin Zayed University for Humanities,Strategy Affairs Office
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep Image Manipulation Localization (IML) models suffer from training data insufficiency and thus heavily rely on pre-training. We argue that contrastive learning is more suitable to tackle the data insufficiency problem for IML. Crafting mutually exclusive positives and negatives is the prerequisite for contrastive learning. However, when adopting contrastive learning in IML, we encounter three categories of image patches: tampered, authentic, and contour patches. Tampered and authentic patches are naturally mutually exclusive, but contour patches containing both tampered and authentic pixels are non-mutually exclusive to them. Simply abnegating these contour patches results in a drastic performance loss since contour patches are decisive to the learning outcomes. Hence, we propose the Non-mutually exclusive Contrastive Learning (NCL) framework to rescue conventional contrastive learning from the above dilemma. In NCL, to cope with the non-mutually exclusivity, we first establish a pivot structure with dual branches to constantly switch the role of contour patches between positives and negatives while training. Then, we devise a pivot-consistent loss to avoid spatial corruption caused by the role-switching process. In this manner, NCL both inherits the self-supervised merits to address the data insufficiency and retains a high manipulation localization accuracy. Extensive experiments verify that our NCL achieves state-of-the-art performance on all five benchmarks without any pre-training and is more robust on unseen real-life samples. The code is available at: https://github.com/Knightzjz/NCL-IML.

</details>

### Geometric Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00028)
- **作者**: Yeskendir Koishekenov, Sharvaree P. Vadgama, Riccardo Valperga, Erik J. Bekkers
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Augmenting Features via Contrastive Learning-based Generative Model for Long-Tailed Classification.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00108) · 📚 被引 1
- **作者**: Minho Park, Hyung-Il Kim, Hwa Jeon Song, Dong-oh Kang
- **🏷️ 机构**: Electronics and Telecommunications Research Institute (ETRI),South Korea
- **会议**: ICCV 2023

### PARTICLE: Part Discovery and Contrastive Learning for Fine-grained Recognition.
- **链接**: [arXiv:2309.13822](https://arxiv.org/abs/2309.13822) · 📚 被引 6
- **作者**: Oindrila Saha, Subhransu Maji
- **🏷️ 机构**: University of Massachusetts,Amherst
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We develop techniques for refining representations for fine-grained classification and segmentation tasks in a self-supervised manner. We find that fine-tuning methods based on instance-discriminative contrastive learning are not as effective, and posit that recognizing part-specific variations is crucial for fine-grained categorization. We present an iterative learning approach that incorporates part-centric equivariance and invariance objectives. First, pixel representations are clustered to discover parts. We analyze the representations from convolutional and vision transformer networks that are best suited for this task. Then, a part-centric learning step aggregates and contrasts representations of parts within an image. We show that this improves the performance on image classification and part segmentation tasks across datasets. For example, under a linear-evaluation scheme, the classification accuracy of a ResNet50 trained on ImageNet using DetCon, a self-supervised learning approach, improves from 35.4% to 42.0% on the Caltech-UCSD Birds, from 35.5% to 44.1% on the FGVC Aircraft, and from 29.7% to 37.4% on the Stanford Cars. We also observe significant gains in few-shot part segmentation tasks using the proposed technique, while instance-discriminative learning was not as effective. Smaller, yet consistent, improvements are also observed for stronger networks based on transformers.

</details>

## 跨领域论文（完整笔记在其他领域）

- Self-Supervised Object Detection from Egocentric Videos. → [object-detection](../object-detection/Guideline%202023.md)
- Unleashing Vanilla Vision Transformer with Masked Image Modeling for Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Multi-view Self-supervised Disentanglement for General Image Denoising. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- GeoMIM: Towards Better 3D Knowledge Transfer via Masked Image Modeling for Multi-view 3D Understanding. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- CL-MVSNet: Unsupervised Multi-view Stereo with Dual-level Contrastive Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Two-in-One Depth: Bridging the Gap Between Monocular and Binocular Self-supervised Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative Convolution Network. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Self-supervised Monocular Depth Estimation: Let's Talk About The Weather. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- 3D Distillation: Improving Self-Supervised Monocular Depth Estimation on Reflective Surfaces. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- GasMono: Geometry-Aided Self-Supervised Monocular Depth Estimation for Indoor Scenes. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- SceneRF: Self-Supervised Monocular 3D Scene Reconstruction with Radiance Fields. → [3d-detection](../3d-detection/Guideline%202023.md)
- DeLiRa: Self-Supervised Depth, Light, and Radiance Fields. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- HaMuCo: Hand Pose Estimation via Multiview Collaborative Self-Supervised Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Margin Contrastive Learning with Learnable-Vector for Continual Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- Multimodal Contrastive Learning and Tabular Attention for Automated Alzheimer's Disease Prediction. → [multimodal](../multimodal/Guideline%202023.md)
