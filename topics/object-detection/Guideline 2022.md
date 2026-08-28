# Object Detection — 2022 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 54 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OW-DETR: Open-world Detection Transformer.
- **链接**: [arXiv:2112.01513](https://arxiv.org/abs/2112.01513) · [代码](https://github.com/akshitac8/OW-DETR) · 📚 被引 215
- **作者**: Akshita Gupta, Sanath Narayan, K. J. Joseph, Salman Khan, Fahad Shahbaz Khan, Mubarak Shah
- **🏷️ 机构**: Inception Institute of Artificial Intelligence, IIT Hyderabad, Mohamed Bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-world object detection (OWOD) is a challenging computer vision problem, where the task is to detect a known set of object categories while simultaneously identifying unknown objects. Additionally, the model must incrementally learn new classes that become known in the next training episodes. Distinct from standard object detection, the OWOD setting poses significant challenges for generating quality candidate proposals on potentially unknown objects, separating the unknown objects from the background and detecting diverse unknown objects. Here, we introduce a novel end-to-end transformer-based framework, OW-DETR, for open-world object detection. The proposed OW-DETR comprises three dedicated components namely, attention-driven pseudo-labeling, novelty classification and objectness scoring to explicitly address the aforementioned OWOD challenges. Our OW-DETR explicitly encodes multi-scale contextual information, possesses less inductive bias, enables knowledge transfer from known classes to the unknown class and can better discriminate between unknown objects and background. Comprehensive experiments are performed on two benchmarks: MS-COCO and PASCAL VOC. The extensive ablations reveal the merits of our proposed contributions. Further, our model outperforms the recently introduced OWOD approach, ORE, with absolute gains ranging from 1.8% to 3.3% in terms of unknown recall on MS-COCO. In the case of incremental object detection, OW-DETR outperforms the state-of-the-art for all settings on PASCAL VOC. Our code is available at https://github.com/akshitac8/OW-DETR.

</details>

### Point-Level Region Contrast for Object Detection Pre-Training.
- **链接**: [arXiv:2202.04639](https://arxiv.org/abs/2202.04639) · 📚 被引 39
- **作者**: Yutong Bai, Xinlei Chen, Alexander Kirillov, Alan L. Yuille, Alexander C. Berg
- **🏷️ 机构**: Facebook AI Research (FAIR), Johns Hopkins University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work we present point-level region contrast, a self-supervised pre-training approach for the task of object detection. This approach is motivated by the two key factors in detection: localization and recognition. While accurate localization favors models that operate at the pixel- or point-level, correct recognition typically relies on a more holistic, region-level view of objects. Incorporating this perspective in pre-training, our approach performs contrastive learning by directly sampling individual point pairs from different regions. Compared to an aggregated representation per region, our approach is more robust to the change in input region quality, and further enables us to implicitly improve initial region assignments via online knowledge distillation during training. Both advantages are important when dealing with imperfect regions encountered in the unsupervised setting. Experiments show point-level region contrast improves on state-of-the-art pre-training methods for object detection and segmentation across multiple tasks and datasets, and we provide extensive ablation studies and visualizations to aid understanding. Code will be made available.

</details>

### DETReg: Unsupervised Pretraining with Region Priors for Object Detection.
- **链接**: [arXiv:2106.04550](https://arxiv.org/abs/2106.04550) · 📚 被引 113
- **作者**: Amir Bar, Xin Wang, Vadim Kantorov, Colorado J. Reed, Roei Herzig, Gal Chechik et al.
- **🏷️ 机构**: Tel-Aviv University, Microsoft Research, Berkeley AI Research
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent self-supervised pretraining methods for object detection largely focus on pretraining the backbone of the object detector, neglecting key parts of detection architecture. Instead, we introduce DETReg, a new self-supervised method that pretrains the entire object detection network, including the object localization and embedding components. During pretraining, DETReg predicts object localizations to match the localizations from an unsupervised region proposal generator and simultaneously aligns the corresponding feature embeddings with embeddings from a self-supervised image encoder. We implement DETReg using the DETR family of detectors and show that it improves over competitive baselines when finetuned on COCO, PASCAL VOC, and Airbus Ship benchmarks. In low-data regimes DETReg achieves improved performance, e.g., when training with only 1% of the labels and in the few-shot learning settings.

</details>

### Label Matching Semi-Supervised Object Detection.
- **链接**: [arXiv:2206.06608](https://arxiv.org/abs/2206.06608) · [代码](https://github.com/hikvision-research/SSOD)
- **作者**: Binbin Chen, Weijie Chen, Shicai Yang, Yunyi Xuan, Jie Song, Di Xie et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised object detection has made significant progress with the development of mean teacher driven self-training. Despite the promising results, the label mismatch problem is not yet fully explored in the previous works, leading to severe confirmation bias during self-training. In this paper, we delve into this problem and propose a simple yet effective LabelMatch framework from two different yet complementary perspectives, i.e., distribution-level and instance-level. For the former one, it is reasonable to approximate the class distribution of the unlabeled data from that of the labeled data according to Monte Carlo Sampling. Guided by this weakly supervision cue, we introduce a re-distribution mean teacher, which leverages adaptive label-distribution-aware confidence thresholds to generate unbiased pseudo labels to drive student learning. For the latter one, there exists an overlooked label assignment ambiguity problem across teacher-student models. To remedy this issue, we present a novel label assignment mechanism for self-training framework, namely proposal self-assignment, which injects the proposals from student into teacher and generates accurate pseudo labels to match each proposal in the student model accordingly. Experiments on both MS-COCO and PASCAL-VOC datasets demonstrate the considerable superiority of our proposed framework to other state-of-the-arts. Code will be available at https://github.com/hikvision-research/SSOD.

</details>

### Dense Learning based Semi-Supervised Object Detection.
- **链接**: [arXiv:2204.07300](https://arxiv.org/abs/2204.07300) · [代码](https://github.com/chenbinghui1/DSL) · 📚 被引 81
- **作者**: Binghui Chen, Pengyu Li, Xiang Chen, Biao Wang, Lei Zhang, Xian-Sheng Hua
- **🏷️ 机构**: Alibaba Group, The Hong Kong Polytechnic University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semi-supervised object detection (SSOD) aims to facilitate the training and deployment of object detectors with the help of a large amount of unlabeled data. Though various self-training based and consistency-regularization based SSOD methods have been proposed, most of them are anchor-based detectors, ignoring the fact that in many real-world applications anchor-free detectors are more demanded. In this paper, we intend to bridge this gap and propose a DenSe Learning (DSL) based anchor-free SSOD algorithm. Specifically, we achieve this goal by introducing several novel techniques, including an Adaptive Filtering strategy for assigning multi-level and accurate dense pixel-wise pseudo-labels, an Aggregated Teacher for producing stable and precise pseudo-labels, and an uncertainty-consistency-regularization term among scales and shuffled patches for improving the generalization capability of the detector. Extensive experiments are conducted on MS-COCO and PASCAL-VOC, and the results show that our proposed DSL method records new state-of-the-art SSOD performance, surpassing existing methods by a large margin. Codes can be found at \textcolor{blue}{https://github.com/chenbinghui1/DSL}.

</details>

### Implicit Motion Handling for Video Camouflaged Object Detection.
- **链接**: [arXiv:2203.07363](https://arxiv.org/abs/2203.07363) · 📚 被引 79
- **作者**: Xuelian Cheng, Huan Xiong, Deng-Ping Fan, Yiran Zhong, Mehrtash Harandi, Tom Drummond et al.
- **🏷️ 机构**: Monash University,Faculty of Engineering, Mohamed bin Zayed University of Artificial Intelligence, CVL, ETH Zurich
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a new video camouflaged object detection (VCOD) framework that can exploit both short-term dynamics and long-term temporal consistency to detect camouflaged objects from video frames. An essential property of camouflaged objects is that they usually exhibit patterns similar to the background and thus make them hard to identify from still images. Therefore, effectively handling temporal dynamics in videos becomes the key for the VCOD task as the camouflaged objects will be noticeable when they move. However, current VCOD methods often leverage homography or optical flows to represent motions, where the detection error may accumulate from both the motion estimation error and the segmentation error. On the other hand, our method unifies motion estimation and object segmentation within a single optimization framework. Specifically, we build a dense correlation volume to implicitly capture motions between neighbouring frames and utilize the final segmentation supervision to optimize the implicit motion estimation and segmentation jointly. Furthermore, to enforce temporal consistency within a video sequence, we jointly utilize a spatio-temporal transformer to refine the short-term predictions. Extensive experiments on VCOD benchmarks demonstrate the architectural effectiveness of our approach. We also provide a large-scale VCOD dataset named MoCA-Mask with pixel-level handcrafted ground-truth masks and construct a comprehensive VCOD benchmark with previous methods to facilitate research in this direction. Dataset Link: https://xueliancheng.github.io/SLT-Net-project.

</details>

### Unknown-Aware Object Detection: Learning What You Don't Know from Videos in the Wild.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01331)
- **作者**: Xuefeng Du, Xin Wang, Gabriel Gozum, Yixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01369)
- **作者**: Yu Du, Fangyun Wei, Zihe Zhang, Miaojing Shi, Yue Gao, Guoqi Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Not All Labels Are Equal: Rationalizing The Labeling Costs for Training Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01409) · 📚 被引 42
- **作者**: Ismail Elezi, Zhiding Yu, Anima Anandkumar, Laura Leal-Taixé, José M. Álvarez
- **🏷️ 机构**: TUM, NVIDIA
- **会议**: CVPR 2022

### Speed up Object Detection on Gigapixel-level Images with Patch Arrangement.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00461) · 📚 被引 12
- **作者**: Jiahao Fan, Huabin Liu, Wenjie Yang, John See, Aixin Zhang, Weiyao Lin
- **🏷️ 机构**: Shanghai Jiao Tong University,China, Heriot- Watt University,Malaysia
- **会议**: CVPR 2022

### Weakly Supervised Rotation-Invariant Aerial Object Detection Network.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01375) · 📚 被引 52
- **作者**: Xiaoxu Feng, Xiwen Yao, Gong Cheng, Junwei Han
- **🏷️ 机构**: School of Automation, Northwestern Polytechnical University,Xi&#x0027;an,China
- **会议**: CVPR 2022

### Sequential Voting with Relational Box Fields for Active Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00241) · 📚 被引 11
- **作者**: Qichen Fu, Xingyu Liu, Kris M. Kitani
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2022

### Can You Spot the Chameleon? Adversarially Camouflaging Images from Co-Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00219) · 📚 被引 18
- **作者**: Ruijun Gao, Qing Guo, Felix Juefei-Xu, Hongkai Yu, Huazhu Fu, Wei Feng et al.
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University,China, Alibaba Group,USA, Cleveland State University,USA
- **会议**: CVPR 2022

### Scale-Equivalent Distillation for Semi-Supervised Object Detection.
- **链接**: [arXiv:2203.12244](https://arxiv.org/abs/2203.12244) · 📚 被引 38
- **作者**: Qiushan Guo, Yao Mu, Jianyu Chen, Tianqi Wang, Yizhou Yu, Ping Luo
- **🏷️ 机构**: The University of Hong Kong, Tsinghua University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent Semi-Supervised Object Detection (SS-OD) methods are mainly based on self-training, i.e., generating hard pseudo-labels by a teacher model on unlabeled data as supervisory signals. Although they achieved certain success, the limited labeled data in semi-supervised learning scales up the challenges of object detection. We analyze the challenges these methods meet with the empirical experiment results. We find that the massive False Negative samples and inferior localization precision lack consideration. Besides, the large variance of object sizes and class imbalance (i.e., the extreme ratio between background and object) hinder the performance of prior arts. Further, we overcome these challenges by introducing a novel approach, Scale-Equivalent Distillation (SED), which is a simple yet effective end-to-end knowledge distillation framework robust to large object size variance and class imbalance. SED has several appealing benefits compared to the previous works. (1) SED imposes a consistency regularization to handle the large scale variance problem. (2) SED alleviates the noise problem from the False Negative samples and inferior localization precision. (3) A re-weighting strategy can implicitly screen the potential foreground regions of the unlabeled data to reduce the effect of class imbalance. Extensive experiments show that SED consistently outperforms the recent state-of-the-art methods on different datasets with significant margins. For example, it surpasses the supervised counterpart by more than 10 mAP when using 5% and 10% labeled data on MS-COCO.

</details>

### Few-Shot Object Detection with Fully Cross-Transformer.
- **链接**: [arXiv:2203.15021](https://arxiv.org/abs/2203.15021) · 📚 被引 187
- **作者**: Guangxing Han, Jiawei Ma, Shiyuan Huang, Long Chen, Shih-Fu Chang
- **🏷️ 机构**: Columbia University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-shot object detection (FSOD), with the aim to detect novel objects using very few training examples, has recently attracted great research interest in the community. Metric-learning based methods have been demonstrated to be effective for this task using a two-branch based siamese network, and calculate the similarity between image regions and few-shot examples for detection. However, in previous works, the interaction between the two branches is only restricted in the detection head, while leaving the remaining hundreds of layers for separate feature extraction. Inspired by the recent work on vision transformers and vision-language transformers, we propose a novel Fully Cross-Transformer based model (FCT) for FSOD by incorporating cross-transformer into both the feature backbone and detection head. The asymmetric-batched cross-attention is proposed to aggregate the key information from the two branches with different batch sizes. Our model can improve the few-shot similarity learning between the two branches by introducing the multi-level interactions. Comprehensive experiments on both PASCAL VOC and MSCOCO FSOD benchmarks demonstrate the effectiveness of our model.

</details>

### Expanding Low-Density Latent Regions for Open-Set Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00937)
- **作者**: Jiaming Han, Yuqiang Ren, Jian Ding, Xingjia Pan, Ke Yan, Gui-Song Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### DESTR: Object Detection with Split Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00916) · 📚 被引 69
- **作者**: Liqiang He, Sinisa Todorovic
- **🏷️ 机构**: Oregon State University,Corvallis,OR,USA,97330
- **会议**: CVPR 2022

### Cross Domain Object Detection by Target-Perceived Dual Branch Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00935) · 📚 被引 94
- **作者**: Mengzhe He, Yali Wang, Jiaxi Wu, Yiru Wang, Hanqing Li, Bo Li et al.
- **🏷️ 机构**: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,ShenZhen Key Lab of Computer Vision and Pattern Recognition, Beihang University, SenseTime Research
- **会议**: CVPR 2022

### Robust Region Feature Synthesizer for Zero-Shot Object Detection.
- **链接**: [arXiv:2201.00103](https://arxiv.org/abs/2201.00103) · 📚 被引 51
- **作者**: Peiliang Huang, Junwei Han, De Cheng, Dingwen Zhang
- **🏷️ 机构**: School of Automation, Northwestern Poly technical University,Brain and Artificial Intelligence Lab, School of Telecommunications Engineering, Xidian University,State Key Laboratory of Integrated Services Networks
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot object detection aims at incorporating class semantic vectors to realize the detection of (both seen and) unseen classes given an unconstrained test image. In this study, we reveal the core challenges in this research area: how to synthesize robust region features (for unseen objects) that are as intra-class diverse and inter-class separable as the real samples, so that strong unseen object detectors can be trained upon them. To address these challenges, we build a novel zero-shot object detection framework that contains an Intra-class Semantic Diverging component and an Inter-class Structure Preserving component. The former is used to realize the one-to-more mapping to obtain diverse visual features from each class semantic vector, preventing miss-classifying the real unseen objects as image backgrounds. While the latter is used to avoid the synthesized features too scattered to mix up the inter-class and foreground-background relationship. To demonstrate the effectiveness of the proposed approach, comprehensive experiments on PASCAL VOC, COCO, and DIOR datasets are conducted. Notably, our approach achieves the new state-of-the-art performance on PASCAL VOC and COCO and it is the first study to carry out zero-shot object detection in remote sensing imagery.

</details>

### Label, Verify, Correct: A Simple Few Shot Object Detection Method.
- **链接**: [arXiv:2112.05749](https://arxiv.org/abs/2112.05749) · 📚 被引 116
- **作者**: Prannay Kaul, Weidi Xie, Andrew Zisserman
- **🏷️ 机构**: Visual Geometry Group, University of Oxford
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The objective of this paper is few-shot object detection (FSOD) -- the task of expanding an object detector for a new category given only a few instances for training. We introduce a simple pseudo-labelling method to source high-quality pseudo-annotations from the training set, for each new category, vastly increasing the number of training instances and reducing class imbalance; our method finds previously unlabelled instances. Naïvely training with model predictions yields sub-optimal performance; we present two novel methods to improve the precision of the pseudo-labelling process: first, we introduce a verification technique to remove candidate detections with incorrect class labels; second, we train a specialised model to correct poor quality bounding boxes. After these two novel steps, we obtain a large set of high-quality pseudo-annotations that allow our final detector to be trained end-to-end. Additionally, we demonstrate our method maintains base class performance, and the utility of simple augmentations in FSOD. While benchmarking on PASCAL VOC and MS-COCO, our method achieves state-of-the-art or second-best performance compared to existing approaches across all number of shots.

</details>

### MUM: Mix Image Tiles and UnMix Feature Tiles for Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01411) · 📚 被引 35
- **作者**: Jongmok Kim, Jooyoung Jang, Seunghyeon Seo, Jisoo Jeong, Jongkeun Na, Nojun Kwak
- **🏷️ 机构**: SNUAILAB,South Korea, Seoul National University,South Korea
- **会议**: CVPR 2022

### Interactron: Embodied Adaptive Object Detection.
- **链接**: [arXiv:2202.00660](https://arxiv.org/abs/2202.00660) · [代码](https://github.com/allenai/interactron) · 📚 被引 31
- **作者**: Klemen Kotar, Roozbeh Mottaghi
- **🏷️ 机构**: PRIOR @ Allen Institute for AI
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Over the years various methods have been proposed for the problem of object detection. Recently, we have witnessed great strides in this domain owing to the emergence of powerful deep neural networks. However, there are typically two main assumptions common among these approaches. First, the model is trained on a fixed training set and is evaluated on a pre-recorded test set. Second, the model is kept frozen after the training phase, so no further updates are performed after the training is finished. These two assumptions limit the applicability of these methods to real-world settings. In this paper, we propose Interactron, a method for adaptive object detection in an interactive setting, where the goal is to perform object detection in images observed by an embodied agent navigating in different environments. Our idea is to continue training during inference and adapt the model at test time without any explicit supervision via interacting with the environment. Our adaptive object detection model provides a 7.2 point improvement in AP (and 12.7 points in AP50) over DETR, a recent, high-performance object detector. Moreover, we show that our object detection model adapts to environments with completely different appearance characteristics, and performs well in them. The code is available at: https://github.com/allenai/interactron .

</details>

### Interactive Multi-Class Tiny-Object Detection.
- **链接**: [arXiv:2203.15266](https://arxiv.org/abs/2203.15266) · [代码](https://github.com/ChungYi347/Interactive-Multi-Class-Tiny-Object-Detection) · 📚 被引 31
- **作者**: Chunggi Lee, Seonwook Park, Heon Song, Jeongun Ryu, Sanghoon Kim, Haejoon Kim et al.
- **🏷️ 机构**: Lunit Inc.
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Annotating tens or hundreds of tiny objects in a given image is laborious yet crucial for a multitude of Computer Vision tasks. Such imagery typically contains objects from various categories, yet the multi-class interactive annotation setting for the detection task has thus far been unexplored. To address these needs, we propose a novel interactive annotation method for multiple instances of tiny objects from multiple classes, based on a few point-based user inputs. Our approach, C3Det, relates the full image context with annotator inputs in a local and global manner via late-fusion and feature-correlation, respectively. We perform experiments on the Tiny-DOTA and LCell datasets using both two-stage and one-stage object detection architectures to verify the efficacy of our approach. Our approach outperforms existing approaches in interactive annotation, achieving higher mAP with fewer clicks. Furthermore, we validate the annotation efficiency of our approach in a user study where it is shown to be 2.85x faster and yield only 0.36x task load (NASA-TLX, lower is better) compared to manual annotation. The code is available at https://github.com/ChungYi347/Interactive-Multi-Class-Tiny-Object-Detection.

</details>

### Source-Free Object Detection by Learning to Overlook Domain Style.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00785) · 📚 被引 86
- **作者**: Shuaifeng Li, Mao Ye, Xiatian Zhu, Lihua Zhou, Lin Xiong
- **🏷️ 机构**: School of Computer Science and Engineering, University of Electronic Science and Technology of China, Centre for Vision, Speech and Signal Processing, University of Surrey
- **会议**: CVPR 2022

### Adaptive Hierarchical Representation Learning for Long-Tailed Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00235) · 📚 被引 17
- **作者**: Banghuai Li
- **🏷️ 机构**: MEGVII Technology
- **会议**: CVPR 2022

### Oriented RepPoints for Aerial Object Detection.
- **链接**: [arXiv:2105.11111](https://arxiv.org/abs/2105.11111) · [代码](https://github.com/LiWentomng/OrientedRepPoints) · 📚 被引 524
- **作者**: Wentong Li, Yijie Chen, Kaixuan Hu, Jianke Zhu
- **🏷️ 机构**: Zhejiang University, University of Electronic Science and Technology of China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In contrast to the generic object, aerial targets are often non-axis aligned with arbitrary orientations having the cluttered surroundings. Unlike the mainstreamed approaches regressing the bounding box orientations, this paper proposes an effective adaptive points learning approach to aerial object detection by taking advantage of the adaptive points representation, which is able to capture the geometric information of the arbitrary-oriented instances. To this end, three oriented conversion functions are presented to facilitate the classification and localization with accurate orientation. Moreover, we propose an effective quality assessment and sample assignment scheme for adaptive points learning toward choosing the representative oriented reppoints samples during training, which is able to capture the non-axis aligned features from adjacent objects or background noises. A spatial constraint is introduced to penalize the outlier points for roust adaptive learning. Experimental results on four challenging aerial datasets including DOTA, HRSC2016, UCAS-AOD and DIOR-R, demonstrate the efficacy of our proposed approach. The source code is availabel at: https://github.com/LiWentomng/OrientedRepPoints.

</details>

### Cross-Domain Adaptive Teacher for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00743)
- **作者**: Yu-Jhe Li, Xiaoliang Dai, Chih-Yao Ma, Yen-Cheng Liu, Kan Chen, Bichen Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### A Dual Weighting Label Assignment Scheme for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00917) · 📚 被引 117
- **作者**: Shuai Li, Chenhang He, Ruihuang Li, Lei Zhang
- **🏷️ 机构**: The Hong Kong Polytechnic University
- **会议**: CVPR 2022

### Forecasting from LiDAR via Future Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01669) · 📚 被引 34
- **作者**: Neehar Peri, Jonathon Luiten, Mengtian Li, Aljosa Osep, Laura Leal-Taixé, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University, TUM Munich
- **会议**: CVPR 2022

### Single-Domain Generalized Object Detection in Urban Scene via Cyclic-Disentangled Self-Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00092) · 📚 被引 122
- **作者**: Aming Wu, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China
- **会议**: CVPR 2022

### Localization Distillation for Dense Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00919) · 📚 被引 197
- **作者**: Zhaohui Zheng, Rongguang Ye, Ping Wang, Dongwei Ren, Wangmeng Zuo, Qibin Hou et al.
- **🏷️ 机构**: Nankai University,TMCC, CS, School of Mathematics, Tianjin University, School of Computer Science and Technology, Harbin Institute of Technology
- **会议**: CVPR 2022

## 跨领域论文（完整笔记在其他领域）

- Bridged Transformer for Vision and Point Cloud 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Self-supervised object detection from audio-visual correspondence. → [multimodal](../multimodal/Guideline%202022.md)
- TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers. → [3d-detection](../3d-detection/Guideline%202022.md)
- Pseudo-Stereo for Monocular 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Focal Sparse Convolutional Networks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention. → [3d-detection](../3d-detection/Guideline%202022.md)
- A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation. → [3d-detection](../3d-detection/Guideline%202022.md)
- Overcoming Catastrophic Forgetting in Incremental Object Detection via Elastic Response Distillation. → [continual-learning](../continual-learning/Guideline%202022.md)
- Homography Loss for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Snowfall Simulation for Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Voxel Set Transformer: A Set-to-Set Approach to 3D Object Detection from Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- Point Density-Aware Voxels for LiDAR 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- MonoDTR: Monocular 3D Object Detection with Depth-Aware Transformer. → [3d-detection](../3d-detection/Guideline%202022.md)
- 3D-VField: Adversarial Augmentation of Point Clouds for Domain Generalization in 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- LIFT: Learning 4D LiDAR Image Fusion Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SS3D: Sparsely-Supervised 3D Object Detection from Point Cloud. → [3d-detection](../3d-detection/Guideline%202022.md)
- Boosting 3D Object Detection by Simulating Multimodality on Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- Diversity Matters: Fully Exploiting Depth Clues for Reliable Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. → [3d-detection](../3d-detection/Guideline%202022.md)
- CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
