# Object Detection — 2022 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 97 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection.
- **链接**: [arXiv:2203.16220](https://arxiv.org/abs/2203.16220) · 📚 被引 1108
- **作者**: Jinyuan Liu, Xin Fan, Zhanbo Huang, Guanyao Wu, Risheng Liu, Wei Zhong et al.
- **🏷️ 机构**: School of Software Technology, Dalian University of Technology, DUT-RU International School of Information Science &#x0026; Engineering, Dalian University of Technology
- **会议**: CVPR 2022

### Omni-DETR: Omni-Supervised Object Detection with Transformers.
- **链接**: [arXiv:2203.16089](https://arxiv.org/abs/2203.16089) · 📚 被引 39
- **作者**: Pei Wang, Zhaowei Cai, Hao Yang, Gurumurthy Swaminathan, Nuno Vasconcelos, Bernt Schiele et al.
- **🏷️ 机构**: UC San Diego, AWS AI Labs
- **会议**: CVPR 2022

### Explore Spatio-temporal Aggregation for Insubstantial Object Detection: Benchmark Dataset and Baseline.
- **链接**: [arXiv:2206.11459](https://arxiv.org/abs/2206.11459) · [代码](https://github.com/CalayZhou/IOD-Video) · 📚 被引 25
- **作者**: Kailai Zhou, Yibo Wang, Tao Lv, Yunqian Li, Linsen Chen, Qiu Shen et al.
- **🏷️ 机构**: Nanjing University,Nanjing,China
- **会议**: CVPR 2022

### Omni-DETR: Omni-Supervised Object Detection with Transformers.
- **链接**: [arXiv:2203.16089](https://arxiv.org/abs/2203.16089) · 📚 被引 39
- **作者**: Pei Wang, Zhaowei Cai, Hao Yang, Gurumurthy Swaminathan, Nuno Vasconcelos, Bernt Schiele et al.
- **🏷️ 机构**: UC San Diego, AWS AI Labs
- **会议**: CVPR 2022

> We endeavor on a rarely explored task named Insubstantial Object Detection (IOD), which aims to localize the object with following characteristics: (1) amorphous shape with indistinct boundary; (2) similarity to surroundings; (3) absence in color. Accordingly, it is far more challenging to distinguish insubstantial objects in a single static frame and the collaborative representation of spatial and temporal information is crucial. Thus, we construct an IOD-Video dataset comprised of 600 videos (141,017 frames) covering various distances, sizes, visibility, and scenes captured by different spectral ranges. In addition, we develop a spatio-temporal aggregation framework for IOD, in which different backbones are deployed and a spatio-temporal aggregation loss (STAloss) is elaborately designed to leverage the consistency along the time axis. Experiments conducted on IOD-Video dataset demonstrate that spatio-temporal aggregation can significantly improve the performance of IOD. We hope our work will attract further researches into this valuable yet challenging task. The code will be available at: \url{https://github.com/CalayZhou/IOD-Video}.

</details>

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
- **链接**: [arXiv:2205.01291](https://arxiv.org/abs/2205.01291) · 📚 被引 94
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
- **链接**: [arXiv:2203.09730](https://arxiv.org/abs/2203.09730) · 📚 被引 117
- **作者**: Shuai Li, Chenhang He, Ruihuang Li, Lei Zhang
- **🏷️ 机构**: The Hong Kong Polytechnic University
- **会议**: CVPR 2022

### SIGMA: Semantic-complete Graph Matching for Domain Adaptive Object Detection.
- **链接**: [arXiv:2203.06398](https://arxiv.org/abs/2203.06398) · 📚 被引 227
- **作者**: Wuyang Li, Xinyu Liu, Yixuan Yuan
- **🏷️ 机构**: City University of Hong Kong
- **会议**: CVPR 2022

### SIOD: Single Instance Annotated Per Category Per Image for Object Detection.
- **链接**: [arXiv:2203.15353](https://arxiv.org/abs/2203.15353) · 📚 被引 20
- **作者**: Hanjun Li, Xingjia Pan, Ke Yan, Fan Tang, Wei-Shi Zheng
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University, Tencent,Youtu Lab, Jilin University
- **会议**: CVPR 2022

### R(Det)2: Randomized Decision Routing for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00478) · 📚 被引 9
- **作者**: Yali Li, Shengjin Wang
- **🏷️ 机构**: Tsinghua University and BNRist,Department of Electronic Engineering,Beijing,China
- **会议**: CVPR 2022

### Semi-Supervised Object Detection via Multi-instance Alignment with Global Class Prototypes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00958) · 📚 被引 14
- **作者**: Aoxue Li, Peng Yuan, Zhenguo Li
- **🏷️ 机构**: Huawei Noah&#x0027;s Ark Lab,China
- **会议**: CVPR 2022

### Equalized Focal Loss for Dense Long-Tailed Object Detection.
- **链接**: [arXiv:2201.02593](https://arxiv.org/abs/2201.02593) · 📚 被引 132
- **作者**: Bo Li, Yongqiang Yao, Jingru Tan, Gang Zhang, Fengwei Yu, Jianwei Lu et al.
- **🏷️ 机构**: Tongji University, Sense Time Research, Tsinghua University
- **会议**: CVPR 2022

### Segment and Complete: Defending Object Detectors against Adversarial Patch Attacks with Robust Patch Detection.
- **链接**: [arXiv:2112.04532](https://arxiv.org/abs/2112.04532) · 📚 被引 110
- **作者**: Jiang Liu, Alexander Levine, Chun Pong Lau, Rama Chellappa, Soheil Feizi
- **🏷️ 机构**: Johns Hopkins University, University of Maryland, College Park
- **会议**: CVPR 2022

### Towards Robust Adaptive Object Detection under Noisy Annotations.
- **链接**: [arXiv:2204.02620](https://arxiv.org/abs/2204.02620) · 📚 被引 42
- **作者**: Xinyu Liu, Wuyang Li, Qiushi Yang, Baopu Li, Yixuan Yuan
- **🏷️ 机构**: City University of Hong Kong, Baidu USA LLC
- **会议**: CVPR 2022

### Unbiased Teacher v2: Semi-supervised Object Detection for Anchor-free and Anchor-based Detectors.
- **链接**: [arXiv:2206.09500](https://arxiv.org/abs/2206.09500) · 📚 被引 131
- **作者**: Yen-Cheng Liu, Chih-Yao Ma, Zsolt Kira
- **🏷️ 机构**: Georgia Institute of Technology, Meta
- **会议**: CVPR 2022

### OSKDet: Orientation-sensitive Keypoint Localization for Rotated Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00125) · 📚 被引 25
- **作者**: Dongchen Lu, Dongmei Li, Yali Li, Shengjin Wang
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering
- **会议**: CVPR 2022

### Active Teacher for Semi-Supervised Object Detection.
- **链接**: [arXiv:2303.08348](https://arxiv.org/abs/2303.08348)
- **作者**: Peng Mi, Jianghang Lin, Yiyi Zhou, Yunhang Shen, Gen Luo, Xiaoshuai Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Optimal Correction Cost for Object Detection Evaluation.
- **链接**: [arXiv:2203.14438](https://arxiv.org/abs/2203.14438) · 📚 被引 21
- **作者**: Mayu Otani, Riku Togashi, Yuta Nakashima, Esa Rahtu, Janne Heikkilä, Shin'ichi Satoh
- **🏷️ 机构**: CyberAgent, Inc., Osaka University, Tampere University
- **会议**: CVPR 2022

### Zoom In and Out: A Mixed-scale Triplet Network for Camouflaged Object Detection.
- **链接**: [arXiv:2203.02688](https://arxiv.org/abs/2203.02688) · 📚 被引 443
- **作者**: Youwei Pang, Xiaoqi Zhao, Tian-Zhu Xiang, Lihe Zhang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, Inception Institute of Artificial Intelligence,UAE
- **会议**: CVPR 2022

### Forecasting from LiDAR via Future Object Detection.
- **链接**: [arXiv:2203.16297](https://arxiv.org/abs/2203.16297) · 📚 被引 34
- **作者**: Neehar Peri, Jonathon Luiten, Mengtian Li, Aljosa Osep, Laura Leal-Taixé, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University, TUM Munich
- **会议**: CVPR 2022

### Salvage of Supervision in Weakly Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01383) · 📚 被引 21
- **作者**: Lin Sui, Chen-Lin Zhang, Jianxin Wu
- **🏷️ 机构**: State Key Laboratory for Novel Software Technology, Nanjing University,China
- **会议**: CVPR 2022

### Proper Reuse of Image Classification Features Improves Object Detection.
- **链接**: [arXiv:2204.00484](https://arxiv.org/abs/2204.00484) · 📚 被引 23
- **作者**: Cristina Nader Vasconcelos, Vighnesh Birodkar, Vincent Dumoulin
- **🏷️ 机构**: Google Research, Brain Team
- **会议**: CVPR 2022

### C2AM Loss: Chasing a Better Decision Boundary for Long-Tail Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00685) · 📚 被引 26
- **作者**: Tong Wang, Yousong Zhu, Yingying Chen, Chaoyang Zhao, Bin Yu, Jinqiao Wang et al.
- **🏷️ 机构**: National Laboratory of Pattern Recognition, Institute of Automation, Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2022

### Entropy-based Active Learning for Object Detection with Progressive Diversity Constraint.
- **链接**: [arXiv:2204.07965](https://arxiv.org/abs/2204.07965) · 📚 被引 90
- **作者**: Jiaxi Wu, Jiaxin Chen, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China
- **会议**: CVPR 2022

### Target-Relevant Knowledge Preservation for Multi-Source Domain Adaptive Object Detection.
- **链接**: [arXiv:2204.07964](https://arxiv.org/abs/2204.07964) · 📚 被引 31
- **作者**: Jiaxi Wu, Jiaxin Chen, Mengzhe He, Yiru Wang, Bo Li, Bingqi Ma et al.
- **🏷️ 机构**: State Key Laboratory of Software Development Environment, Beihang University,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China, Shenzhen Institutes of Advanced Technology, Chinese Academy of Science
- **会议**: CVPR 2022

### Single-Domain Generalized Object Detection in Urban Scene via Cyclic-Disentangled Self-Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00092) · 📚 被引 122
- **作者**: Aming Wu, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China
- **会议**: CVPR 2022

### Revisiting AP Loss for Dense Object Detection: Adaptive Ranking Pair Selection.
- **链接**: [arXiv:2207.12042](https://arxiv.org/abs/2207.12042) · 📚 被引 9
- **作者**: Dongli Xu, Jinhong Deng, Wen Li
- **🏷️ 机构**: School of Computer Science and Engineering &#x0026; Shenzhen Institute for Advanced Study University of Electronic Science and Technology of China
- **会议**: CVPR 2022

### Smartadapt: Multi-branch Object Detection Framework for Videos on Mobiles.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00256) · 📚 被引 16
- **作者**: Ran Xu, Fangzhou Mu, Jayoung Lee, Preeti Mukherjee, Somali Chaterji, Saurabh Bagchi et al.
- **🏷️ 机构**: Purdue University, University of Wisconsin-Madison
- **会议**: CVPR 2022

### H2FA R-CNN: Holistic and Hierarchical Feature Alignment for Cross-domain Weakly Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01393) · 📚 被引 49
- **作者**: Yunqiu Xu, Yifan Sun, Zongxin Yang, Jiaxu Miao, Yi Yang
- **🏷️ 机构**: Baidu Research, Zhejiang University,CCAI
- **会议**: CVPR 2022

### Balanced and Hierarchical Relation Learning for One-shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00744) · 📚 被引 26
- **作者**: Hanqing Yang, Sijia Cai, Hualian Sheng, Bing Deng, Jianqiang Huang, Xian-Sheng Hua et al.
- **🏷️ 机构**: State Key Laboratory of Industrial Control Technology, College of Control Science and Engineering, Zhejiang University, DAMO Academy, Alibaba Group, Shudao Investment Group Co., Ltd
- **会议**: CVPR 2022

### Continual Object Detection via Prototypical Task Correlation Guided Gating Mechanism.
- **链接**: [arXiv:2205.03055](https://arxiv.org/abs/2205.03055) · 📚 被引 38
- **作者**: Binbin Yang, Xinchi Deng, Han Shi, Changlin Li, Gengwei Zhang, Hang Xu et al.
- **🏷️ 机构**: Sun Yat-sen University, The Hong Kong University of Science and Technology, ReLER, AAII, UTS
- **会议**: CVPR 2022

### QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection.
- **链接**: [arXiv:2103.09136](https://arxiv.org/abs/2103.09136) · 📚 被引 524
- **作者**: Chenhongyi Yang, Zehao Huang, Naiyan Wang
- **🏷️ 机构**: University of Edinburgh, TuSimple
- **会议**: CVPR 2022

### Real-time Object Detection for Streaming Perception.
- **链接**: [arXiv:2203.12338](https://arxiv.org/abs/2203.12338) · 📚 被引 58
- **作者**: Jinrong Yang, Songtao Liu, Zeming Li, Xiaoping Li, Jian Sun
- **🏷️ 机构**: Huazhong University of Science and Technology, Megvii Technology
- **会议**: CVPR 2022

### Sylph: A Hypernetwork Framework for Incremental Few-shot Object Detection.
- **链接**: [arXiv:2203.13903](https://arxiv.org/abs/2203.13903) · 📚 被引 47
- **作者**: Li Yin, Juan M. Perez-Rua, Kevin J. Liang
- **🏷️ 机构**: Meta AI
- **会议**: CVPR 2022

### Democracy Does Matter: Comprehensive Feature Mining for Co-Salient Object Detection.
- **链接**: [arXiv:2203.05787](https://arxiv.org/abs/2203.05787) · 📚 被引 77
- **作者**: Siyue Yu, Jimin Xiao, Bingfeng Zhang, Eng Gee Lim
- **🏷️ 机构**: XJTLU
- **会议**: CVPR 2022

### Kernelized Few-shot Object Detection with Efficient Integral Aggregation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01861) · 📚 被引 64
- **作者**: Shan Zhang, Lei Wang, Naila Murray, Piotr Koniusz
- **🏷️ 机构**: Australian National University, University of Wollongong, Meta AI Research
- **会议**: CVPR 2022

### Group R-CNN for Weakly Semi-supervised Object Detection with Points.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00920) · 📚 被引 52
- **作者**: Shilong Zhang, Zhuoran Yu, Liyang Liu, Xinjiang Wang, Aojun Zhou, Kai Chen
- **🏷️ 机构**: Shanghai AI Laboratory, Georgia Institute of Technology, Tencent AI Platform Department,China
- **会议**: CVPR 2022

### Task-specific Inconsistency Alignment for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01382) · 📚 被引 122
- **作者**: Liang Zhao, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2022

### Semantic-aligned Fusion Transformer for One-shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00745) · 📚 被引 30
- **作者**: Yizhou Zhao, Xun Guo, Yan Lu
- **🏷️ 机构**: Carnegie Mellon University, Microsoft Research Asia
- **会议**: CVPR 2022

### Localization Distillation for Dense Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00919) · 📚 被引 197
- **作者**: Zhaohui Zheng, Rongguang Ye, Ping Wang, Dongwei Ren, Wangmeng Zuo, Qibin Hou et al.
- **🏷️ 机构**: Nankai University,TMCC, CS, School of Mathematics, Tianjin University, School of Computer Science and Technology, Harbin Institute of Technology
- **会议**: CVPR 2022

### Progressive End-to-End Object Detection in Crowded Scenes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00093) · 📚 被引 73
- **作者**: Anlin Zheng, Yuang Zhang, Xiangyu Zhang, Xiaojuan Qi, Jian Sun
- **🏷️ 机构**: MEGVII Technology, Shanghai Jiao Tong University, University of Hong Kong
- **会议**: CVPR 2022

### Multi-Granularity Alignment Domain Adaptation for Object Detection.
- **链接**: [arXiv:2203.16897](https://arxiv.org/abs/2203.16897) · 📚 被引 111
- **作者**: Wenzhang Zhou, Dawei Du, Libo Zhang, Tiejian Luo, Yanjun Wu
- **🏷️ 机构**: University of Chinese Academy of Sciences,Beijing,China, Kitware, Inc.,NY,USA, Institute of Software, Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Domain adaptive object detection is challenging due to distinctive data distribution between source domain and target domain. In this paper, we propose a unified multi-granularity alignment based object detection framework towards domain-invariant feature learning. To this end, we encode the dependencies across different granularity perspectives including pixel-, instance-, and category-levels simultaneously to align two domains. Based on pixel-level feature maps from the backbone network, we first develop the omni-scale gated fusion module to aggregate discriminative representations of instances by scale-aware convolutions, leading to robust multi-scale object detection. Meanwhile, the multi-granularity discriminators are proposed to identify which domain different granularities of samples(i.e., pixels, instances, and categories) come from. Notably, we leverage not only the instance discriminability in different categories but also the category consistency between two domains. Extensive experiments are carried out on multiple domain adaptation scenarios, demonstrating the effectiveness of our framework over state-of-the-art algorithms on top of anchor-free FCOS and anchor-based Faster RCNN detectors with different backbones.

</details>

### Progressive End-to-End Object Detection in Crowded Scenes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00093) · 📚 被引 73
- **作者**: Anlin Zheng, Yuang Zhang, Xiangyu Zhang, Xiaojuan Qi, Jian Sun
- **🏷️ 机构**: MEGVII Technology, Shanghai Jiao Tong University, University of Hong Kong
- **会议**: CVPR 2022

### Multi-Granularity Alignment Domain Adaptation for Object Detection.
- **链接**: [arXiv:2203.16897](https://arxiv.org/abs/2203.16897) · 📚 被引 111
- **作者**: Wenzhang Zhou, Dawei Du, Libo Zhang, Tiejian Luo, Yanjun Wu
- **🏷️ 机构**: University of Chinese Academy of Sciences,Beijing,China, Kitware, Inc.,NY,USA, Institute of Software, Chinese Academy of Sciences,Beijing,China
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
- Voxel Field Fusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Diversity Matters: Fully Exploiting Depth Clues for Reliable Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- MonoJSG: Joint Semantic and Geometric Cost Volume for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Exploring Geometric Consistency for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SS3D: Sparsely-Supervised 3D Object Detection from Point Cloud. → [3d-detection](../3d-detection/Guideline%202022.md)
- RBGNet: Ray-based Grouping for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Back to Reality: Weakly-supervised 3D Object Detection with Shape-guided Label Enhancement. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rotationally Equivariant 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DAIR-V2X: A Large-Scale Dataset for Vehicle-Infrastructure Cooperative 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- LIFT: Learning 4D LiDAR Image Fusion Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Dimension Embeddings for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Boosting 3D Object Detection by Simulating Multimodality on Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)

## 🆕 增量新增

### Rethinking Few-Shot Object Detection on a Multi-Domain Benchmark. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2207.11169](https://arxiv.org/abs/2207.11169)
- **作者**: Kibok Lee, Hao Yang, Satyaki Chakraborty, Zhaowei Cai, Gurumurthy Swaminathan, Avinash Ravichandran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对现有少样本目标检测（FSOD）评估多局限于同域预训练和微调的问题，该论文提出了一个包含10个跨域数据集的Multi-dOmain Few-Shot Object Detection（MoFSOD）基准。通过系统分析冻结层、不同架构和预训练数据集的影响，发现微调（FT）在跨域基准上表现与SOTA相当或更优，且架构选择对下游任务影响显著。该工作为FSOD提供了更全面的评估框架，并揭示了以往被忽视的关键因素。
- **摘要（英）**: This paper addresses the limitation of few-shot object detection (FSOD) evaluation being confined to similar domains by proposing a Multi-dOmain FSOD (MoFSOD) benchmark with 10 diverse datasets. It reveals that fine-tuning is a strong baseline, architecture choice significantly impacts downstream performance, and pre-training data selection matters, providing a more comprehensive evaluation framework.
- **核心贡献**: 提出了首个多域少样本目标检测基准MoFSOD，并系统分析了影响FSOD性能的关键因素。
- **创新点**: 引入跨域评估视角，重新审视微调基线在FSOD中的有效性。
- **结果**: 微调在跨域基准上达到与SOTA相当或更优的性能，且架构和预训练数据选择影响显著。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing works on few-shot object detection (FSOD) focus on a setting where both pre-training and few-shot learning datasets are from a similar domain. However, few-shot algorithms are important in multiple domains; hence evaluation needs to reflect the broad applications. We propose a Multi-dOmain Few-Shot Object Detection (MoFSOD) benchmark consisting of 10 datasets from a wide range of domains to evaluate FSOD algorithms. We comprehensively analyze the impacts of freezing layers, different architectures, and different pre-training datasets on FSOD performance. Our empirical results show several key factors that have not been explored in previous works: 1) contrary to previous belief, on a multi-domain benchmark, fine-tuning (FT) is a strong baseline for FSOD, performing on par or better than the state-of-the-art (SOTA) algorithms; 2) utilizing FT as the baseline allows us to explore multiple architectures, and we found them to have a significant impact on down-stream few-shot tasks, even with similar pre-training performances; 3) by decoupling pre-training and few-shot learning, MoFSOD allows us to explore the impact of different pre-training datasets, and the right choice can boost the performance of the down-stream tasks significantly. Based on these findings, we list possible avenues of investigation for improving FSOD performance and propose two simple modifications to existing algorithms that lead to SOTA performance on the MoFSOD benchmark. The code is available at https://github.com/amazon-research/few-shot-object-detection-benchmark.

</details>

### A Simple Approach and Benchmark for 21, 000-Category Object Detection. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20083-0_1) · 📚 被引 1
- **作者**: Yutong Lin, Chen Li, Yue Cao, Zheng Zhang, Jianfeng Wang, Lijuan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对大规模类别（21,000类）目标检测的挑战，提出了一种简单的方法和基准。由于摘要缺失，具体方法细节不明，但推测涉及高效分类器设计和数据集构建。该工作旨在推动极大规模目标检测的研究，但缺乏实验数据支持。
- **摘要（英）**: This paper proposes a simple approach and benchmark for 21,000-category object detection, aiming to address challenges in extreme-scale classification. Details are limited due to missing abstract, but it likely focuses on scalable classifier design and dataset creation.
- **核心贡献**: 提出了21,000类目标检测的基准和简单方法。
- **创新点**: 探索极大规模类别下的目标检测方法。
- **结果**: 未提供具体实验结果。

### Towards Hard-Positive Query Mining for DETR-Based Human-Object Interaction Detection. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19812-0_26) · 📚 被引 26
- **作者**: Xubin Zhong, Changxing Ding, Zijian Li, Shaoli Huang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文针对基于DETR的人-物交互（HOI）检测中难正样本挖掘不足的问题，提出了一种面向难正样本的查询挖掘方法。通过改进查询生成和匹配策略，增强模型对复杂交互的识别能力。但摘要缺失，具体技术细节和实验效果未知。
- **摘要（英）**: This paper addresses the challenge of hard-positive query mining in DETR-based human-object interaction (HOI) detection, proposing methods to improve query generation and matching for complex interactions. Specifics are unavailable due to missing abstract.
- **核心贡献**: 提出了DETR框架下的难正样本查询挖掘方法。
- **创新点**: 将难样本挖掘思想引入DETR的查询机制。
- **结果**: 未提供具体实验结果。

### X-DETR: A Versatile Architecture for Instance-wise Vision-Language Tasks. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_17) · 📚 被引 32
- **作者**: Zhaowei Cai, Gukyeong Kwon, Avinash Ravichandran, Erhan Bas, Zhuowen Tu, Rahul Bhotika et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 该论文提出了X-DETR，一个用于实例级视觉-语言任务的通用架构。该架构统一了检测、分割、视觉问答等多种任务，通过Transformer实现跨模态交互。摘要缺失，但该工作旨在提供多功能解决方案，可能推动多模态感知的集成。
- **摘要（英）**: This paper introduces X-DETR, a versatile architecture for instance-wise vision-language tasks, unifying detection, segmentation, and VQA via Transformer-based cross-modal interaction. It aims to provide a general solution for multimodal perception.
- **核心贡献**: 提出了实例级视觉-语言任务的通用架构X-DETR。
- **创新点**: 统一多种视觉-语言任务于单一Transformer架构。
- **结果**: 未提供具体实验结果。

### Sparse DETR: Efficient End-to-End Object Detection with Learnable Sparsity. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2111.14330](https://arxiv.org/abs/2111.14330)
- **作者**: Byungseok Roh, Jaewoong Shin, Wuhyun Shin, Saehoon Kim
- **🏷️ 机构**: Yanan University, Chongqing University of Science and Technology
- **会议**: ICLR 2022
- **摘要（中）**: 针对Deformable DETR中编码器计算开销大的问题，本文提出Sparse DETR，通过可学习稀疏性仅更新解码器可能引用的编码器token。方法基于初步观察：仅更新部分编码器token时检测性能几乎不下降。此外，在选中的token上应用辅助检测损失，在最小化计算开销的同时提升性能。实验表明，Sparse DETR在仅使用10%编码器token的情况下，性能优于Deformable DETR。
- **摘要（英）**: This paper addresses the high encoder computation cost in Deformable DETR by proposing Sparse DETR, which selectively updates only tokens likely referenced by the decoder via learnable sparsity. It also applies an auxiliary detection loss on selected tokens to improve performance with minimal overhead. Sparse DETR achieves better performance than Deformable DETR with only 10% of encoder tokens.
- **核心贡献**: 提出可学习稀疏性机制，大幅降低编码器计算成本。
- **创新点**: 基于观察发现仅更新部分token即可保持性能，设计稀疏更新策略。
- **结果**: 在10%编码器token下性能优于Deformable DETR。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> DETR is the first end-to-end object detector using a transformer encoder-decoder architecture and demonstrates competitive performance but low computational efficiency on high resolution feature maps. The subsequent work, Deformable DETR, enhances the efficiency of DETR by replacing dense attention with deformable attention, which achieves 10x faster convergence and improved performance. Deformable DETR uses the multiscale feature to ameliorate performance, however, the number of encoder tokens increases by 20x compared to DETR, and the computation cost of the encoder attention remains a bottleneck. In our preliminary experiment, we observe that the detection performance hardly deteriorates even if only a part of the encoder token is updated. Inspired by this observation, we propose Sparse DETR that selectively updates only the tokens expected to be referenced by the decoder, thus help the model effectively detect objects. In addition, we show that applying an auxiliary detection loss on the selected tokens in the encoder improves the performance while minimizing computational overhead. We validate that Sparse DETR achieves better performance than Deformable DETR even with only 10% encoder tokens on the COCO dataset. Albeit only the encoder tokens are sparsified, the total computation cost decreases by 38% and the frames per second (FPS) increases by 42% compared to Deformable DETR. Code is available at https://github.com/kakaobrain/sparse-detr

</details>

### Bridged Transformer for Vision and Point Cloud 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2210.01391](https://arxiv.org/abs/2210.01391) · 📚 被引 55
- **作者**: Yikai Wang, TengQi Ye, Lele Cao, Wenbing Huang, Fuchun Sun, Fengxiang He et al.
- **🏷️ 机构**: Tsinghua University,Beijing National Research Center for Information Science and Technology (BNRist), State Key Lab on Intelligent Technology and Systems,Department of Computer Science and Technology, ByteDance Inc., Institute for AI Industry Research (AIR), Tsinghua University
- **会议**: CVPR 2022
- **摘要（中）**: 针对2D图像与3D点云因几何异构难以直接融合进行3D目标检测的问题，提出Bridged Transformer (BrT)端到端架构。BrT利用对象查询作为桥梁统一3D和2D空间表示，并通过点-块投影实现特征聚合，增强图像与点云间的关联。相比现有方法，BrT能无缝融合多视角图像与点云，在SUN RGB-D和ScanNetV2数据集上超越现有最先进方法。
- **摘要（英）**: To address the challenge of fusing heterogeneous 2D images and 3D point clouds for 3D object detection, this paper proposes Bridged Transformer (BrT), an end-to-end architecture that uses object queries to bridge 3D and 2D spaces and point-to-patch projections for feature aggregation. BrT surpasses state-of-the-art methods on SUN RGB-D and ScanNetV2 datasets, demonstrating effective multimodal fusion.
- **核心贡献**: 提出基于对象查询的桥接Transformer架构，统一2D和3D表示实现高效融合。
- **创新点**: 利用对象查询作为跨模态桥梁，结合点-块投影增强特征关联。
- **结果**: 在SUN RGB-D和ScanNetV2上取得最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is a crucial research topic in computer vision, which usually uses 3D point clouds as input in conventional setups. Recently, there is a trend of leveraging multiple sources of input data, such as complementing the 3D point cloud with 2D images that often have richer color and fewer noises. However, due to the heterogeneous geometrics of the 2D and 3D representations, it prevents us from applying off-the-shelf neural networks to achieve multimodal fusion. To that end, we propose Bridged Transformer (BrT), an end-to-end architecture for 3D object detection. BrT is simple and effective, which learns to identify 3D and 2D object bounding boxes from both points and image patches. A key element of BrT lies in the utilization of object queries for bridging 3D and 2D spaces, which unifies different sources of data representations in Transformer. We adopt a form of feature aggregation realized by point-to-patch projections which further strengthen the correlations between images and points. Moreover, BrT works seamlessly for fusing the point cloud with multi-view images. We experimentally show that BrT surpasses state-of-the-art methods on SUN RGB-D and ScanNetV2 datasets.

</details>

### Self-supervised object detection from audio-visual correspondence. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2104.06401](https://arxiv.org/abs/2104.06401) · 📚 被引 40
- **作者**: Triantafyllos Afouras, Yuki M. Asano, Francois Fagan, Andrea Vedaldi, Florian Metze
- **🏷️ 机构**: University of Oxford, University of Amsterdam, Meta AI
- **会议**: CVPR 2022
- **摘要（中）**: 针对无监督目标检测中缺乏类别标签的问题，提出利用音视频对应关系作为监督信号训练检测器。方法设计自监督对比框架联合学习分类和定位，然后使用生成的伪标签训练图像检测器。相比弱监督和无监督方法，在目标检测和声源定位任务上表现更优，且能用极少标签对齐到真实类别。
- **摘要（英）**: This paper tackles unsupervised object detection by leveraging audio-visual correspondence as a supervisory signal, using a contrastive framework to jointly learn classification and localization. The method outperforms prior unsupervised and weakly-supervised detectors on object detection and sound source localization, and can align to ground-truth classes with minimal labels.
- **核心贡献**: 提出首个利用音视频对应关系进行自监督目标检测的框架。
- **创新点**: 以音频为监督信号，通过对比学习联合学习分类与定位。
- **结果**: 在多个基准上超越现有无监督和弱监督检测器。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the problem of learning object detectors without supervision. Differently from weakly-supervised object detection, we do not assume image-level class labels. Instead, we extract a supervisory signal from audio-visual data, using the audio component to "teach" the object detector. While this problem is related to sound source localisation, it is considerably harder because the detector must classify the objects by type, enumerate each instance of the object, and do so even when the object is silent. We tackle this problem by first designing a self-supervised framework with a contrastive objective that jointly learns to classify and localise objects. Then, without using any supervision, we simply use these self-supervised labels and boxes to train an image-based object detector. With this, we outperform previous unsupervised and weakly-supervised detectors for the task of object detection and sound source localization. We also show that we can align this detector to ground-truth classes with as little as one label per pseudo-class, and show how our method can learn to detect generic objects that go beyond instruments, such as airplanes and cats.

</details>

### VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.09704](https://arxiv.org/abs/2203.09704) · 📚 被引 92
- **作者**: Shengheng Deng, Zhihao Liang, Lin Sun, Kui Jia
- **🏷️ 机构**: South China University of Technology, Magic Leap,Sunnyvale,CA
- **会议**: CVPR 2022
- **摘要（中）**: ①针对多视图3D检测中特征融合缺乏全局空间上下文的问题。②提出VISTA模块，通过双交叉视图空间注意力自适应融合BEV和RV特征，并解耦分类和回归任务。③相比现有融合方法，VISTA利用卷积替代MLP，增强空间建模能力。④在KITTI和nuScenes基准上验证了有效性，提升了检测精度。
- **摘要（英）**: This paper proposes VISTA, a plug-and-play fusion module with dual cross-view spatial attention for 3D detection, improving feature fusion and achieving better performance on KITTI and nuScenes.
- **核心贡献**: 提出VISTA注意力融合模块，增强3D检测。
- **创新点**: 双交叉视图空间注意力和任务解耦。
- **结果**: 在多个基准上取得性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting objects from LiDAR point clouds is of tremendous significance in autonomous driving. In spite of good progress, accurate and reliable 3D detection is yet to be achieved due to the sparsity and irregularity of LiDAR point clouds. Among existing strategies, multi-view methods have shown great promise by leveraging the more comprehensive information from both bird's eye view (BEV) and range view (RV). These multi-view methods either refine the proposals predicted from single view via fused features, or fuse the features without considering the global spatial context; their performance is limited consequently. In this paper, we propose to adaptively fuse multi-view features in a global spatial context via Dual Cross-VIew SpaTial Attention (VISTA). The proposed VISTA is a novel plug-and-play fusion module, wherein the multi-layer perceptron widely adopted in standard attention modules is replaced with a convolutional one. Thanks to the learned attention mechanism, VISTA can produce fused features of high quality for prediction of proposals. We decouple the classification and regression tasks in VISTA, and an additional constraint of attention variance is applied that enables the attention module to focus on specific targets instead of generic points. We conduct thorough experiments on the benchmarks of nuScenes and Waymo; results confirm the efficacy of our designs. At the time of submission, our method achieves 63.0% in overall mAP and 69.8% in NDS on the nuScenes benchmark, outperforming all published methods by up to 24% in safety-crucial categories such as cyclist. The source code in PyTorch is available at https://github.com/Gorilla-Lab-SCUT/VISTA

</details>

### A Versatile Multi-View Framework for LiDAR-based 3D Object Detection with Guidance from Panoptic Segmentation.
- **链接**: [arXiv:2203.02133](https://arxiv.org/abs/2203.02133) · 📚 被引 24
- **作者**: Hamidreza Fazlali, Yixuan Xu, Yuan Ren, Bingbing Liu
- **🏷️ 机构**: Huawei Noah&#x0027;s Ark Lab, Canada at the time of writing
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection using LiDAR data is an indispensable component for autonomous driving systems. Yet, only a few LiDAR-based 3D object detection methods leverage segmentation information to further guide the detection process. In this paper, we propose a novel multi-task framework that jointly performs 3D object detection and panoptic segmentation. In our method, the 3D object detection backbone in Bird's-Eye-View (BEV) plane is augmented by the injection of Range-View (RV) feature maps from the 3D panoptic segmentation backbone. This enables the detection backbone to leverage multi-view information to address the shortcomings of each projection view. Furthermore, foreground semantic information is incorporated to ease the detection task by highlighting the locations of each object class in the feature maps. Finally, a new center density heatmap generated based on the instance-level information further guides the detection backbone by suggesting possible box center locations for objects. Our method works with any BEV-based 3D object detection method, and as shown by extensive experiments on the nuScenes dataset, it provides significant performance gains. Notably, the proposed method based on a single-stage CenterPoint 3D object detection network achieved state-of-the-art performance on nuScenes 3D Detection Benchmark with 67.3 NDS.

</details>

### A Large-Scale Multiple-objective Method for Black-box Attack Against Object Detection.
- **链接**: [arXiv:2209.07790](https://arxiv.org/abs/2209.07790) · 📚 被引 22
- **作者**: Siyuan Liang, Longkang Li, Yanbo Fan, Xiaojun Jia, Jingzhi Li, Baoyuan Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have shown that detectors based on deep models are vulnerable to adversarial examples, even in the black-box scenario where the attacker cannot access the model information. Most existing attack methods aim to minimize the true positive rate, which often shows poor attack performance, as another sub-optimal bounding box may be detected around the attacked bounding box to be the new true positive one. To settle this challenge, we propose to minimize the true positive rate and maximize the false positive rate, which can encourage more false positive objects to block the generation of new true positive bounding boxes. It is modeled as a multi-objective optimization (MOP) problem, of which the generic algorithm can search the Pareto-optimal. However, our task has more than two million decision variables, leading to low searching efficiency. Thus, we extend the standard Genetic Algorithm with Random Subset selection and Divide-and-Conquer, called GARSDC, which significantly improves the efficiency. Moreover, to alleviate the sensitivity to population quality in generic algorithms, we generate a gradient-prior initial population, utilizing the transferability between different detectors with similar backbones. Compared with the state-of-art attack methods, GARSDC decreases by an average 12.0 in the mAP and queries by about 1000 times in extensive experiments. Our codes can be found at https://github.com/LiangSiyuan21/ GARSDC.

</details>

### ObjectBox: From Centers to Boxes for Anchor-Free Object Detection.
- **链接**: [arXiv:2207.06985](https://arxiv.org/abs/2207.06985) · 📚 被引 75
- **作者**: Mohsen Zand, Ali Etemad, Michael A. Greenspan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present ObjectBox, a novel single-stage anchor-free and highly generalizable object detection approach. As opposed to both existing anchor-based and anchor-free detectors, which are more biased toward specific object scales in their label assignments, we use only object center locations as positive samples and treat all objects equally in different feature levels regardless of the objects' sizes or shapes. Specifically, our label assignment strategy considers the object center locations as shape- and size-agnostic anchors in an anchor-free fashion, and allows learning to occur at all scales for every object. To support this, we define new regression targets as the distances from two corners of the center cell location to the four sides of the bounding box. Moreover, to handle scale-variant objects, we propose a tailored IoU loss to deal with boxes with different sizes. As a result, our proposed object detector does not need any dataset-dependent hyperparameters to be tuned across datasets. We evaluate our method on MS-COCO 2017 and PASCAL VOC 2012 datasets, and compare our results to state-of-the-art methods. We observe that ObjectBox performs favorably in comparison to prior works. Furthermore, we perform rigorous ablation experiments to evaluate different components of our method. Our code is available at: https://github.com/MohsenZand/ObjectBox.

</details>

### SALISA: Saliency-Based Input Sampling for Efficient Video Object Detection.
- **链接**: [arXiv:2204.02397](https://arxiv.org/abs/2204.02397) · 📚 被引 11
- **作者**: Babak Ehteshami Bejnordi, Amirhossein Habibian, Fatih Porikli, Amir Ghodrati
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution images are widely adopted for high-performance object detection in videos. However, processing high-resolution inputs comes with high computation costs, and naive down-sampling of the input to reduce the computation costs quickly degrades the detection performance. In this paper, we propose SALISA, a novel non-uniform SALiency-based Input SAmpling technique for video object detection that allows for heavy down-sampling of unimportant background regions while preserving the fine-grained details of a high-resolution image. The resulting image is spatially smaller, leading to reduced computational costs while enabling a performance comparable to a high-resolution input. To achieve this, we propose a differentiable resampling module based on a thin plate spline spatial transformer network (TPS-STN). This module is regularized by a novel loss to provide an explicit supervision signal to learn to "magnify" salient regions. We report state-of-the-art results in the low compute regime on the ImageNet-VID and UA-DETRAC video object detection datasets. We demonstrate that on both datasets, the mAP of an EfficientDet-D1 (EfficientDet-D2) gets on par with EfficientDet-D2 (EfficientDet-D3) at a much lower computational cost. We also show that SALISA significantly improves the detection of small objects. In particular, SALISA with an EfficientDet-D1 detector improves the detection of small objects by $77\%$, and remarkably also outperforms EfficientDetD3 baseline.

</details>

### Semi-supervised Object Detection via VC Learning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19821-2_10) · 📚 被引 7
- **作者**: Changrui Chen, Kurt Debattista, Jungong Han
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### A Simple Single-Scale Vision Transformer for Object Detection and Instance Segmentation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_41)
- **作者**: Wuyang Chen, Xianzhi Du, Fan Yang, Lucas Beyer, Xiaohua Zhai, Tsung-Yi Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection.
- **链接**: [arXiv:2205.05979](https://arxiv.org/abs/2205.05979) · 📚 被引 75
- **作者**: Xuesong Chen, Shaoshuai Shi, Benjin Zhu, Ka Chun Cheung, Hang Xu, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate and reliable 3D detection is vital for many applications including autonomous driving vehicles and service robots. In this paper, we present a flexible and high-performance 3D detection framework, named MPPNet, for 3D temporal object detection with point cloud sequences. We propose a novel three-hierarchy framework with proxy points for multi-frame feature encoding and interactions to achieve better detection. The three hierarchies conduct per-frame feature encoding, short-clip feature fusion, and whole-sequence feature aggregation, respectively. To enable processing long-sequence point clouds with reasonable computational resources, intra-group feature mixing and inter-group feature attention are proposed to form the second and third feature encoding hierarchies, which are recurrently applied for aggregating multi-frame trajectory features. The proxy points not only act as consistent object representations for each frame, but also serve as the courier to facilitate feature interaction between frames. The experiments on large Waymo Open dataset show that our approach outperforms state-of-the-art methods with large margins when applied to both short (e.g., 4-frame) and long (e.g., 16-frame) point cloud sequences. Code is available at https://github.com/open-mmlab/OpenPCDet.

</details>

### Point-to-Box Network for Accurate Object Detection via Single Point Supervision.
- **链接**: [arXiv:2207.06827](https://arxiv.org/abs/2207.06827) · 📚 被引 75
- **作者**: Pengfei Chen, Xuehui Yu, Xumeng Han, Najmul Hassan, Kai Wang, Jiachen Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection using single point supervision has received increasing attention over the years. However, the performance gap between point supervised object detection (PSOD) and bounding box supervised detection remains large. In this paper, we attribute such a large performance gap to the failure of generating high-quality proposal bags which are crucial for multiple instance learning (MIL). To address this problem, we introduce a lightweight alternative to the off-the-shelf proposal (OTSP) method and thereby create the Point-to-Box Network (P2BNet), which can construct an inter-objects balanced proposal bag by generating proposals in an anchor-like way. By fully investigating the accurate position information, P2BNet further constructs an instance-level bag, avoiding the mixture of multiple objects. Finally, a coarse-to-fine policy in a cascade fashion is utilized to improve the IoU between proposals and ground-truth (GT). Benefiting from these strategies, P2BNet is able to produce high-quality instance-level bags for object detection. P2BNet improves the mean average precision (AP) by more than 50% relative to the previous best PSOD method on the MS COCO dataset. It also demonstrates the great potential to bridge the performance gap between point supervised and bounding-box supervised detectors. The code will be released at github.com/ucas-vg/P2BNet.

</details>

### Efficient Decoder-Free Object Detection with Transformers.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20080-9_5) · 📚 被引 17
- **作者**: Peixian Chen, Mengdan Zhang, Yunhang Shen, Kekai Sheng, Yuting Gao, Xing Sun et al.
- **🏷️ 机构**: ZJU
- **会议**: ECCV 2022

### Exploring Resolution and Degradation Clues as Self-supervised Signal for Low Quality Object Detection.
- **链接**: [arXiv:2208.03062](https://arxiv.org/abs/2208.03062) · 📚 被引 24
- **作者**: Ziteng Cui, Yingying Zhu, Lin Gu, Guo-Jun Qi, Xiaoxiao Li, Renrui Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image restoration algorithms such as super resolution (SR) are indispensable pre-processing modules for object detection in low quality images. Most of these algorithms assume the degradation is fixed and known a priori. However, in practical, either the real degradation or optimal up-sampling ratio rate is unknown or differs from assumption, leading to a deteriorating performance for both the pre-processing module and the consequent high-level task such as object detection. Here, we propose a novel self-supervised framework to detect objects in degraded low resolution images. We utilizes the downsampling degradation as a kind of transformation for self-supervised signals to explore the equivariant representation against various resolutions and other degradation conditions. The Auto Encoding Resolution in Self-supervision (AERIS) framework could further take the advantage of advanced SR architectures with an arbitrary resolution restoring decoder to reconstruct the original correspondence from the degraded input image. Both the representation learning and object detection are optimized jointly in an end-to-end training fashion. The generic AERIS framework could be implemented on various mainstream object detection architectures with different backbones. The extensive experiments show that our methods has achieved superior performance compared with existing methods when facing variant degradation situations. Code would be released at https://github.com/cuiziteng/ECCV_AERIS.

</details>

## 跨领域论文（完整笔记在其他领域）

- Open-Vocabulary DETR with Conditional Matching. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- V2X-ViT: Vehicle-to-Everything Cooperative Perception with Vision Transformer. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- MAE-DET: Revisiting Maximum Entropy Principle in Zero-Shot NAS for Efficient Object Detection. → [neural-architecture-search](../neural-architecture-search/Guideline%202022.md)
- Prototypical VoteNet for Few-Shot 3D Point Cloud Object Detection. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers. → [3d-detection](../3d-detection/Guideline%202022.md)
- Pseudo-Stereo for Monocular 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Focal Sparse Convolutional Networks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Unknown-Aware Object Detection: Learning What You Don't Know from Videos in the Wild. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Overcoming Catastrophic Forgetting in Incremental Object Detection via Elastic Response Distillation. → [continual-learning](../continual-learning/Guideline%202022.md)
- Homography Loss for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- LiDAR Snowfall Simulation for Robust 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Expanding Low-Density Latent Regions for Open-Set Object Detection. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Voxel Set Transformer: A Set-to-Set Approach to 3D Object Detection from Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- Point Density-Aware Voxels for LiDAR 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- MonoDTR: Monocular 3D Object Detection with Depth-Aware Transformer. → [3d-detection](../3d-detection/Guideline%202022.md)
- 3D-VField: Adversarial Augmentation of Point Clouds for Domain Generalization in 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Time3D: End-to-End Joint Monocular 3D Object Detection and Tracking for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Voxel Field Fusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Diversity Matters: Fully Exploiting Depth Clues for Reliable Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- MonoJSG: Joint Semantic and Geometric Cost Volume for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Exploring Geometric Consistency for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- SS3D: Sparsely-Supervised 3D Object Detection from Point Cloud. → [3d-detection](../3d-detection/Guideline%202022.md)
- RBGNet: Ray-based Grouping for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Back to Reality: Weakly-supervised 3D Object Detection with Shape-guided Label Enhancement. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rope3D: The Roadside Perception Dataset for Autonomous Driving and Monocular 3D Object Detection Task. → [3d-detection](../3d-detection/Guideline%202022.md)
- Rotationally Equivariant 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- DAIR-V2X: A Large-Scale Dataset for Vehicle-Infrastructure Cooperative 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- LIFT: Learning 4D LiDAR Image Fusion Transformer for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- CAT-Det: Contrastively Augmented Transformer for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Dimension Embeddings for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Boosting 3D Object Detection by Simulating Multimodality on Point Clouds. → [3d-detection](../3d-detection/Guideline%202022.md)
- Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- Energy-based Latent Aligner for Incremental Learning. → [continual-learning](../continual-learning/Guideline%202022.md)
- Open-Vocabulary One-Stage Detection with Hierarchical Visual-Language Knowledge Distillation. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Object Discovery via Contrastive Learning for Weakly Supervised Object Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Deformable Feature Aggregation for Dynamic Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Multimodal Object Detection via Probabilistic Ensembling. → [multimodal](../multimodal/Guideline%202022.md)
<!-- COMPLETE v1 papers=87 -->
