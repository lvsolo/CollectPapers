# Object Detection — 2022 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 97 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00571)
- **作者**: Jinyuan Liu, Xin Fan, Zhanbo Huang, Guanyao Wu, Risheng Liu, Wei Zhong et al.
- **🏷️ 机构**: School of Software Technology, Dalian University of Technology, DUT-RU International School of Information Science &#x0026; Engineering, Dalian University of Technology
- **会议**: CVPR 2022

### Omni-DETR: Omni-Supervised Object Detection with Transformers.
- **链接**: [arXiv:2203.16089](https://arxiv.org/abs/2203.16089) · [代码](https://github.com/amazon-research/omni-detr)
- **作者**: Pei Wang, Zhaowei Cai, Hao Yang, Gurumurthy Swaminathan, Nuno Vasconcelos, Bernt Schiele et al.
- **🏷️ 机构**: UC San Diego, AWS AI Labs
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We consider the problem of omni-supervised object detection, which can use unlabeled, fully labeled and weakly labeled annotations, such as image tags, counts, points, etc., for object detection. This is enabled by a unified architecture, Omni-DETR, based on the recent progress on student-teacher framework and end-to-end transformer based object detection. Under this unified architecture, different types of weak labels can be leveraged to generate accurate pseudo labels, by a bipartite matching based filtering mechanism, for the model to learn. In the experiments, Omni-DETR has achieved state-of-the-art results on multiple datasets and settings. And we have found that weak annotations can help to improve detection performance and a mixture of them can achieve a better trade-off between annotation cost and accuracy than the standard complete annotation. These findings could encourage larger object detection datasets with mixture annotations. The code is available at https://github.com/amazon-research/omni-detr.

### Explore Spatio-temporal Aggregation for Insubstantial Object Detection: Benchmark Dataset and Baseline.
- **链接**: [arXiv:2206.11459](https://arxiv.org/abs/2206.11459) · [代码](https://github.com/CalayZhou/IOD-Video)
- **作者**: Kailai Zhou, Yibo Wang, Tao Lv, Yunqian Li, Linsen Chen, Qiu Shen et al.
- **🏷️ 机构**: Nanjing University,Nanjing,China
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We endeavor on a rarely explored task named Insubstantial Object Detection (IOD), which aims to localize the object with following characteristics: (1) amorphous shape with indistinct boundary; (2) similarity to surroundings; (3) absence in color. Accordingly, it is far more challenging to distinguish insubstantial objects in a single static frame and the collaborative representation of spatial and temporal information is crucial. Thus, we construct an IOD-Video dataset comprised of 600 videos (141,017 frames) covering various distances, sizes, visibility, and scenes captured by different spectral ranges. In addition, we develop a spatio-temporal aggregation framework for IOD, in which different backbones are deployed and a spatio-temporal aggregation loss (STAloss) is elaborately designed to leverage the consistency along the time axis. Experiments conducted on IOD-Video dataset demonstrate that spatio-temporal aggregation can significantly improve the performance of IOD. We hope our work will attract further researches into this valuable yet challenging task. The code will be available at: \url{https://github.com/CalayZhou/IOD-Video}.

### OW-DETR: Open-world Detection Transformer.
- **链接**: [arXiv:2112.01513](https://arxiv.org/abs/2112.01513) · [代码](https://github.com/akshitac8/OW-DETR) · 📚 被引 215
- **作者**: Akshita Gupta, Sanath Narayan, K. J. Joseph, Salman Khan, Fahad Shahbaz Khan, Mubarak Shah
- **🏷️ 机构**: Inception Institute of Artificial Intelligence, IIT Hyderabad, Mohamed Bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Open-world object detection (OWOD) is a challenging computer vision problem, where the task is to detect a known set of object categories while simultaneously identifying unknown objects. Additionally, the model must incrementally learn new classes that become known in the next training episodes. Distinct from standard object detection, the OWOD setting poses significant challenges for generating quality candidate proposals on potentially unknown objects, separating the unknown objects from the background and detecting diverse unknown objects. Here, we introduce a novel end-to-end transformer-based framework, OW-DETR, for open-world object detection. The proposed OW-DETR comprises three dedicated components namely, attention-driven pseudo-labeling, novelty classification and objectness scoring to explicitly address the aforementioned OWOD challenges. Our OW-DETR explicitly encodes multi-scale contextual information, possesses less inductive bias, enables knowledge transfer from known classes to the unknown class and can better discriminate between unknown objects and background. Comprehensive experiments are performed on two benchmarks: MS-COCO and PASCAL VOC. The extensive ablations reveal the merits of our proposed contributions. Further, our model outperforms the recently introduced OWOD approach, ORE, with absolute gains ranging from 1.8% to 3.3% in terms of unknown recall on MS-COCO. In the case of incremental object detection, OW-DETR outperforms the state-of-the-art for all settings on PASCAL VOC. Our code is available at https://github.com/akshitac8/OW-DETR.

### Point-Level Region Contrast for Object Detection Pre-Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01559)
- **作者**: Yutong Bai, Xinlei Chen, Alexander Kirillov, Alan L. Yuille, Alexander C. Berg
- **🏷️ 机构**: Facebook AI Research (FAIR), Johns Hopkins University
- **会议**: CVPR 2022

### DETReg: Unsupervised Pretraining with Region Priors for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01420) · 📚 被引 113
- **作者**: Amir Bar, Xin Wang, Vadim Kantorov, Colorado J. Reed, Roei Herzig, Gal Chechik et al.
- **🏷️ 机构**: Tel-Aviv University, Microsoft Research, Berkeley AI Research
- **会议**: CVPR 2022

### Label Matching Semi-Supervised Object Detection.
- **链接**: [arXiv:2206.06608](https://arxiv.org/abs/2206.06608) · [代码](https://github.com/hikvision-research/SSOD)
- **作者**: Binbin Chen, Weijie Chen, Shicai Yang, Yunyi Xuan, Jie Song, Di Xie et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Semi-supervised object detection has made significant progress with the development of mean teacher driven self-training. Despite the promising results, the label mismatch problem is not yet fully explored in the previous works, leading to severe confirmation bias during self-training. In this paper, we delve into this problem and propose a simple yet effective LabelMatch framework from two different yet complementary perspectives, i.e., distribution-level and instance-level. For the former one, it is reasonable to approximate the class distribution of the unlabeled data from that of the labeled data according to Monte Carlo Sampling. Guided by this weakly supervision cue, we introduce a re-distribution mean teacher, which leverages adaptive label-distribution-aware confidence thresholds to generate unbiased pseudo labels to drive student learning. For the latter one, there exists an overlooked label assignment ambiguity problem across teacher-student models. To remedy this issue, we present a novel label assignment mechanism for self-training framework, namely proposal self-assignment, which injects the proposals from student into teacher and generates accurate pseudo labels to match each proposal in the student model accordingly. Experiments on both MS-COCO and PASCAL-VOC datasets demonstrate the considerable superiority of our proposed framework to other state-of-the-arts. Code will be available at https://github.com/hikvision-research/SSOD.

### Dense Learning based Semi-Supervised Object Detection.
- **链接**: [arXiv:2204.07300](https://arxiv.org/abs/2204.07300) · [代码](https://github.com/chenbinghui1/DSL) · 📚 被引 81
- **作者**: Binghui Chen, Pengyu Li, Xiang Chen, Biao Wang, Lei Zhang, Xian-Sheng Hua
- **🏷️ 机构**: Alibaba Group, The Hong Kong Polytechnic University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Semi-supervised object detection (SSOD) aims to facilitate the training and deployment of object detectors with the help of a large amount of unlabeled data. Though various self-training based and consistency-regularization based SSOD methods have been proposed, most of them are anchor-based detectors, ignoring the fact that in many real-world applications anchor-free detectors are more demanded. In this paper, we intend to bridge this gap and propose a DenSe Learning (DSL) based anchor-free SSOD algorithm. Specifically, we achieve this goal by introducing several novel techniques, including an Adaptive Filtering strategy for assigning multi-level and accurate dense pixel-wise pseudo-labels, an Aggregated Teacher for producing stable and precise pseudo-labels, and an uncertainty-consistency-regularization term among scales and shuffled patches for improving the generalization capability of the detector. Extensive experiments are conducted on MS-COCO and PASCAL-VOC, and the results show that our proposed DSL method records new state-of-the-art SSOD performance, surpassing existing methods by a large margin. Codes can be found at \textcolor{blue}{https://github.com/chenbinghui1/DSL}.

### Implicit Motion Handling for Video Camouflaged Object Detection.
- **链接**: [arXiv:2203.07363](https://arxiv.org/abs/2203.07363)
- **作者**: Xuelian Cheng, Huan Xiong, Deng-Ping Fan, Yiran Zhong, Mehrtash Harandi, Tom Drummond et al.
- **🏷️ 机构**: Monash University,Faculty of Engineering, Mohamed bin Zayed University of Artificial Intelligence, CVL, ETH Zurich
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We propose a new video camouflaged object detection (VCOD) framework that can exploit both short-term dynamics and long-term temporal consistency to detect camouflaged objects from video frames. An essential property of camouflaged objects is that they usually exhibit patterns similar to the background and thus make them hard to identify from still images. Therefore, effectively handling temporal dynamics in videos becomes the key for the VCOD task as the camouflaged objects will be noticeable when they move. However, current VCOD methods often leverage homography or optical flows to represent motions, where the detection error may accumulate from both the motion estimation error and the segmentation error. On the other hand, our method unifies motion estimation and object segmentation within a single optimization framework. Specifically, we build a dense correlation volume to implicitly capture motions between neighbouring frames and utilize the final segmentation supervision to optimize the implicit motion estimation and segmentation jointly. Furthermore, to enforce temporal consistency within a video sequence, we jointly utilize a spatio-temporal transformer to refine the short-term predictions. Extensive experiments on VCOD benchmarks demonstrate the architectural effectiveness of our approach. We also provide a large-scale VCOD dataset named MoCA-Mask with pixel-level handcrafted ground-truth masks and construct a comprehensive VCOD benchmark with previous methods to facilitate research in this direction. Dataset Link: https://xueliancheng.github.io/SLT-Net-project.

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
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00461)
- **作者**: Jiahao Fan, Huabin Liu, Wenjie Yang, John See, Aixin Zhang, Weiyao Lin
- **🏷️ 机构**: Shanghai Jiao Tong University,China, Heriot- Watt University,Malaysia
- **会议**: CVPR 2022

### Weakly Supervised Rotation-Invariant Aerial Object Detection Network.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01375)
- **作者**: Xiaoxu Feng, Xiwen Yao, Gong Cheng, Junwei Han
- **🏷️ 机构**: School of Automation, Northwestern Polytechnical University,Xi&#x0027;an,China
- **会议**: CVPR 2022

### Sequential Voting with Relational Box Fields for Active Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00241)
- **作者**: Qichen Fu, Xingyu Liu, Kris M. Kitani
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2022

### Can You Spot the Chameleon? Adversarially Camouflaging Images from Co-Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00219)
- **作者**: Ruijun Gao, Qing Guo, Felix Juefei-Xu, Hongkai Yu, Huazhu Fu, Wei Feng et al.
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University,China, Alibaba Group,USA, Cleveland State University,USA
- **会议**: CVPR 2022

### Scale-Equivalent Distillation for Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01412)
- **作者**: Qiushan Guo, Yao Mu, Jianyu Chen, Tianqi Wang, Yizhou Yu, Ping Luo
- **🏷️ 机构**: The University of Hong Kong, Tsinghua University
- **会议**: CVPR 2022

### Few-Shot Object Detection with Fully Cross-Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00525)
- **作者**: Guangxing Han, Jiawei Ma, Shiyuan Huang, Long Chen, Shih-Fu Chang
- **🏷️ 机构**: Columbia University
- **会议**: CVPR 2022

### Expanding Low-Density Latent Regions for Open-Set Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00937)
- **作者**: Jiaming Han, Yuqiang Ren, Jian Ding, Xingjia Pan, Ke Yan, Gui-Song Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### DESTR: Object Detection with Split Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00916)
- **作者**: Liqiang He, Sinisa Todorovic
- **🏷️ 机构**: Oregon State University,Corvallis,OR,USA,97330
- **会议**: CVPR 2022

### Cross Domain Object Detection by Target-Perceived Dual Branch Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00935)
- **作者**: Mengzhe He, Yali Wang, Jiaxi Wu, Yiru Wang, Hanqing Li, Bo Li et al.
- **🏷️ 机构**: Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,ShenZhen Key Lab of Computer Vision and Pattern Recognition, Beihang University, SenseTime Research
- **会议**: CVPR 2022

### Robust Region Feature Synthesizer for Zero-Shot Object Detection.
- **链接**: [arXiv:2201.00103](https://arxiv.org/abs/2201.00103)
- **作者**: Peiliang Huang, Junwei Han, De Cheng, Dingwen Zhang
- **🏷️ 机构**: School of Automation, Northwestern Poly technical University,Brain and Artificial Intelligence Lab, School of Telecommunications Engineering, Xidian University,State Key Laboratory of Integrated Services Networks
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Zero-shot object detection aims at incorporating class semantic vectors to realize the detection of (both seen and) unseen classes given an unconstrained test image. In this study, we reveal the core challenges in this research area: how to synthesize robust region features (for unseen objects) that are as intra-class diverse and inter-class separable as the real samples, so that strong unseen object detectors can be trained upon them. To address these challenges, we build a novel zero-shot object detection framework that contains an Intra-class Semantic Diverging component and an Inter-class Structure Preserving component. The former is used to realize the one-to-more mapping to obtain diverse visual features from each class semantic vector, preventing miss-classifying the real unseen objects as image backgrounds. While the latter is used to avoid the synthesized features too scattered to mix up the inter-class and foreground-background relationship. To demonstrate the effectiveness of the proposed approach, comprehensive experiments on PASCAL VOC, COCO, and DIOR datasets are conducted. Notably, our approach achieves the new state-of-the-art performance on PASCAL VOC and COCO and it is the first study to carry out zero-shot object detection in remote sensing imagery.

### Label, Verify, Correct: A Simple Few Shot Object Detection Method.
- **链接**: [arXiv:2112.05749](https://arxiv.org/abs/2112.05749)
- **作者**: Prannay Kaul, Weidi Xie, Andrew Zisserman
- **🏷️ 机构**: Visual Geometry Group, University of Oxford
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > The objective of this paper is few-shot object detection (FSOD) -- the task of expanding an object detector for a new category given only a few instances for training. We introduce a simple pseudo-labelling method to source high-quality pseudo-annotations from the training set, for each new category, vastly increasing the number of training instances and reducing class imbalance; our method finds previously unlabelled instances. Naïvely training with model predictions yields sub-optimal performance; we present two novel methods to improve the precision of the pseudo-labelling process: first, we introduce a verification technique to remove candidate detections with incorrect class labels; second, we train a specialised model to correct poor quality bounding boxes. After these two novel steps, we obtain a large set of high-quality pseudo-annotations that allow our final detector to be trained end-to-end. Additionally, we demonstrate our method maintains base class performance, and the utility of simple augmentations in FSOD. While benchmarking on PASCAL VOC and MS-COCO, our method achieves state-of-the-art or second-best performance compared to existing approaches across all number of shots.

### MUM: Mix Image Tiles and UnMix Feature Tiles for Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01411)
- **作者**: Jongmok Kim, Jooyoung Jang, Seunghyeon Seo, Jisoo Jeong, Jongkeun Na, Nojun Kwak
- **🏷️ 机构**: SNUAILAB,South Korea, Seoul National University,South Korea
- **会议**: CVPR 2022

### Interactron: Embodied Adaptive Object Detection.
- **链接**: [arXiv:2202.00660](https://arxiv.org/abs/2202.00660) · [代码](https://github.com/allenai/interactron)
- **作者**: Klemen Kotar, Roozbeh Mottaghi
- **🏷️ 机构**: PRIOR @ Allen Institute for AI
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Over the years various methods have been proposed for the problem of object detection. Recently, we have witnessed great strides in this domain owing to the emergence of powerful deep neural networks. However, there are typically two main assumptions common among these approaches. First, the model is trained on a fixed training set and is evaluated on a pre-recorded test set. Second, the model is kept frozen after the training phase, so no further updates are performed after the training is finished. These two assumptions limit the applicability of these methods to real-world settings. In this paper, we propose Interactron, a method for adaptive object detection in an interactive setting, where the goal is to perform object detection in images observed by an embodied agent navigating in different environments. Our idea is to continue training during inference and adapt the model at test time without any explicit supervision via interacting with the environment. Our adaptive object detection model provides a 7.2 point improvement in AP (and 12.7 points in AP50) over DETR, a recent, high-performance object detector. Moreover, we show that our object detection model adapts to environments with completely different appearance characteristics, and performs well in them. The code is available at: https://github.com/allenai/interactron .

### Interactive Multi-Class Tiny-Object Detection.
- **链接**: [arXiv:2203.15266](https://arxiv.org/abs/2203.15266) · [代码](https://github.com/ChungYi347/Interactive-Multi-Class-Tiny-Object-Detection)
- **作者**: Chunggi Lee, Seonwook Park, Heon Song, Jeongun Ryu, Sanghoon Kim, Haejoon Kim et al.
- **🏷️ 机构**: Lunit Inc.
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Annotating tens or hundreds of tiny objects in a given image is laborious yet crucial for a multitude of Computer Vision tasks. Such imagery typically contains objects from various categories, yet the multi-class interactive annotation setting for the detection task has thus far been unexplored. To address these needs, we propose a novel interactive annotation method for multiple instances of tiny objects from multiple classes, based on a few point-based user inputs. Our approach, C3Det, relates the full image context with annotator inputs in a local and global manner via late-fusion and feature-correlation, respectively. We perform experiments on the Tiny-DOTA and LCell datasets using both two-stage and one-stage object detection architectures to verify the efficacy of our approach. Our approach outperforms existing approaches in interactive annotation, achieving higher mAP with fewer clicks. Furthermore, we validate the annotation efficiency of our approach in a user study where it is shown to be 2.85x faster and yield only 0.36x task load (NASA-TLX, lower is better) compared to manual annotation. The code is available at https://github.com/ChungYi347/Interactive-Multi-Class-Tiny-Object-Detection.

### Source-Free Object Detection by Learning to Overlook Domain Style.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00785)
- **作者**: Shuaifeng Li, Mao Ye, Xiatian Zhu, Lihua Zhou, Lin Xiong
- **🏷️ 机构**: School of Computer Science and Engineering, University of Electronic Science and Technology of China, Centre for Vision, Speech and Signal Processing, University of Surrey
- **会议**: CVPR 2022

### Adaptive Hierarchical Representation Learning for Long-Tailed Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00235)
- **作者**: Banghuai Li
- **🏷️ 机构**: MEGVII Technology
- **会议**: CVPR 2022

### Oriented RepPoints for Aerial Object Detection.
- **链接**: [arXiv:2105.11111](https://arxiv.org/abs/2105.11111) · [代码](https://github.com/LiWentomng/OrientedRepPoints)
- **作者**: Wentong Li, Yijie Chen, Kaixuan Hu, Jianke Zhu
- **🏷️ 机构**: Zhejiang University, University of Electronic Science and Technology of China
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > In contrast to the generic object, aerial targets are often non-axis aligned with arbitrary orientations having the cluttered surroundings. Unlike the mainstreamed approaches regressing the bounding box orientations, this paper proposes an effective adaptive points learning approach to aerial object detection by taking advantage of the adaptive points representation, which is able to capture the geometric information of the arbitrary-oriented instances. To this end, three oriented conversion functions are presented to facilitate the classification and localization with accurate orientation. Moreover, we propose an effective quality assessment and sample assignment scheme for adaptive points learning toward choosing the representative oriented reppoints samples during training, which is able to capture the non-axis aligned features from adjacent objects or background noises. A spatial constraint is introduced to penalize the outlier points for roust adaptive learning. Experimental results on four challenging aerial datasets including DOTA, HRSC2016, UCAS-AOD and DIOR-R, demonstrate the efficacy of our proposed approach. The source code is availabel at: https://github.com/LiWentomng/OrientedRepPoints.

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

### SIGMA: Semantic-complete Graph Matching for Domain Adaptive Object Detection.
- **链接**: [arXiv:2203.06398](https://arxiv.org/abs/2203.06398) · [代码](https://github.com/CityU-AIM-Group/SIGMA)
- **作者**: Wuyang Li, Xinyu Liu, Yixuan Yuan
- **🏷️ 机构**: City University of Hong Kong
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Domain Adaptive Object Detection (DAOD) leverages a labeled domain to learn an object detector generalizing to a novel domain free of annotations. Recent advances align class-conditional distributions by narrowing down cross-domain prototypes (class centers). Though great success,they ignore the significant within-class variance and the domain-mismatched semantics within the training batch, leading to a sub-optimal adaptation. To overcome these challenges, we propose a novel SemantIc-complete Graph MAtching (SIGMA) framework for DAOD, which completes mismatched semantics and reformulates the adaptation with graph matching. Specifically, we design a Graph-embedded Semantic Completion module (GSC) that completes mismatched semantics through generating hallucination graph nodes in missing categories. Then, we establish cross-image graphs to model class-conditional distributions and learn a graph-guided memory bank for better semantic completion in turn. After representing the source and target data as graphs, we reformulate the adaptation as a graph matching problem, i.e., finding well-matched node pairs across graphs to reduce the domain gap, which is solved with a novel Bipartite Graph Matching adaptor (BGM). In a nutshell, we utilize graph nodes to establish semantic-aware node affinity and leverage graph edges as quadratic constraints in a structure-aware matching loss, achieving fine-grained adaptation with a node-to-node graph matching. Extensive experiments verify that SIGMA outperforms existing works significantly. Our code is available at https://github.com/CityU-AIM-Group/SIGMA.

### SIOD: Single Instance Annotated Per Category Per Image for Object Detection.
- **链接**: [arXiv:2203.15353](https://arxiv.org/abs/2203.15353)
- **作者**: Hanjun Li, Xingjia Pan, Ke Yan, Fan Tang, Wei-Shi Zheng
- **🏷️ 机构**: School of Computer Science and Engineering, Sun Yat-sen University, Tencent,Youtu Lab, Jilin University
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Object detection under imperfect data receives great attention recently. Weakly supervised object detection (WSOD) suffers from severe localization issues due to the lack of instance-level annotation, while semi-supervised object detection (SSOD) remains challenging led by the inter-image discrepancy between labeled and unlabeled data. In this study, we propose the Single Instance annotated Object Detection (SIOD), requiring only one instance annotation for each existing category in an image. Degraded from inter-task (WSOD) or inter-image (SSOD) discrepancies to the intra-image discrepancy, SIOD provides more reliable and rich prior knowledge for mining the rest of unlabeled instances and trades off the annotation cost and performance. Under the SIOD setting, we propose a simple yet effective framework, termed Dual-Mining (DMiner), which consists of a Similarity-based Pseudo Label Generating module (SPLG) and a Pixel-level Group Contrastive Learning module (PGCL). SPLG firstly mines latent instances from feature representation space to alleviate the annotation missing problem. To avoid being misled by inaccurate pseudo labels, we propose PGCL to boost the tolerance to false pseudo labels. Extensive experiments on MS COCO verify the feasibility of the SIOD setting and the superiority of the proposed method, which obtains consistent and significant improvements compared to baseline methods and achieves comparable results with fully supervised object detection (FSOD) methods with only 40% instances annotated.

### R(Det)2: Randomized Decision Routing for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00478)
- **作者**: Yali Li, Shengjin Wang
- **🏷️ 机构**: Tsinghua University and BNRist,Department of Electronic Engineering,Beijing,China
- **会议**: CVPR 2022

### Semi-Supervised Object Detection via Multi-instance Alignment with Global Class Prototypes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00958)
- **作者**: Aoxue Li, Peng Yuan, Zhenguo Li
- **🏷️ 机构**: Huawei Noah&#x0027;s Ark Lab,China
- **会议**: CVPR 2022

### Equalized Focal Loss for Dense Long-Tailed Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00686)
- **作者**: Bo Li, Yongqiang Yao, Jingru Tan, Gang Zhang, Fengwei Yu, Jianwei Lu et al.
- **🏷️ 机构**: Tongji University, Sense Time Research, Tsinghua University
- **会议**: CVPR 2022

### Segment and Complete: Defending Object Detectors against Adversarial Patch Attacks with Robust Patch Detection.
- **链接**: [arXiv:2112.04532](https://arxiv.org/abs/2112.04532) · [代码](https://github.com/joellliu/SegmentAndComplete)
- **作者**: Jiang Liu, Alexander Levine, Chun Pong Lau, Rama Chellappa, Soheil Feizi
- **🏷️ 机构**: Johns Hopkins University, University of Maryland, College Park
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Object detection plays a key role in many security-critical systems. Adversarial patch attacks, which are easy to implement in the physical world, pose a serious threat to state-of-the-art object detectors. Developing reliable defenses for object detectors against patch attacks is critical but severely understudied. In this paper, we propose Segment and Complete defense (SAC), a general framework for defending object detectors against patch attacks through detection and removal of adversarial patches. We first train a patch segmenter that outputs patch masks which provide pixel-level localization of adversarial patches. We then propose a self adversarial training algorithm to robustify the patch segmenter. In addition, we design a robust shape completion algorithm, which is guaranteed to remove the entire patch from the images if the outputs of the patch segmenter are within a certain Hamming distance of the ground-truth patch masks. Our experiments on COCO and xView datasets demonstrate that SAC achieves superior robustness even under strong adaptive attacks with no reduction in performance on clean images, and generalizes well to unseen patch shapes, attack budgets, and unseen attack methods. Furthermore, we present the APRICOT-Mask dataset, which augments the APRICOT dataset with pixel-level annotations of adversarial patches. We show SAC can significantly reduce the targeted attack success rate of physical patch attacks. Our code is available at https://github.com/joellliu/SegmentAndComplete.

### Towards Robust Adaptive Object Detection under Noisy Annotations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01381)
- **作者**: Xinyu Liu, Wuyang Li, Qiushi Yang, Baopu Li, Yixuan Yuan
- **🏷️ 机构**: City University of Hong Kong, Baidu USA LLC
- **会议**: CVPR 2022

### Unbiased Teacher v2: Semi-supervised Object Detection for Anchor-free and Anchor-based Detectors.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00959)
- **作者**: Yen-Cheng Liu, Chih-Yao Ma, Zsolt Kira
- **🏷️ 机构**: Georgia Institute of Technology, Meta
- **会议**: CVPR 2022

### OSKDet: Orientation-sensitive Keypoint Localization for Rotated Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00125)
- **作者**: Dongchen Lu, Dongmei Li, Yali Li, Shengjin Wang
- **🏷️ 机构**: Tsinghua University,Department of Electronic Engineering
- **会议**: CVPR 2022

### Active Teacher for Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01408)
- **作者**: Peng Mi, Jianghang Lin, Yiyi Zhou, Yunhang Shen, Gen Luo, Xiaoshuai Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2022

### Optimal Correction Cost for Object Detection Evaluation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.02043)
- **作者**: Mayu Otani, Riku Togashi, Yuta Nakashima, Esa Rahtu, Janne Heikkilä, Shin'ichi Satoh
- **🏷️ 机构**: CyberAgent, Inc., Osaka University, Tampere University
- **会议**: CVPR 2022

### Zoom In and Out: A Mixed-scale Triplet Network for Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00220)
- **作者**: Youwei Pang, Xiaoqi Zhao, Tian-Zhu Xiang, Lihe Zhang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,China, Inception Institute of Artificial Intelligence,UAE
- **会议**: CVPR 2022

### Forecasting from LiDAR via Future Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01669) · 📚 被引 34
- **作者**: Neehar Peri, Jonathon Luiten, Mengtian Li, Aljosa Osep, Laura Leal-Taixé, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University, TUM Munich
- **会议**: CVPR 2022

### Salvage of Supervision in Weakly Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01383)
- **作者**: Lin Sui, Chen-Lin Zhang, Jianxin Wu
- **🏷️ 机构**: State Key Laboratory for Novel Software Technology, Nanjing University,China
- **会议**: CVPR 2022

### Proper Reuse of Image Classification Features Improves Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01326)
- **作者**: Cristina Nader Vasconcelos, Vighnesh Birodkar, Vincent Dumoulin
- **🏷️ 机构**: Google Research, Brain Team
- **会议**: CVPR 2022

### C2AM Loss: Chasing a Better Decision Boundary for Long-Tail Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00685)
- **作者**: Tong Wang, Yousong Zhu, Yingying Chen, Chaoyang Zhao, Bin Yu, Jinqiao Wang et al.
- **🏷️ 机构**: National Laboratory of Pattern Recognition, Institute of Automation, Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2022

### Entropy-based Active Learning for Object Detection with Progressive Diversity Constraint.
- **链接**: [arXiv:2204.07965](https://arxiv.org/abs/2204.07965)
- **作者**: Jiaxi Wu, Jiaxin Chen, Di Huang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Software Development Environment,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Active learning is a promising alternative to alleviate the issue of high annotation cost in the computer vision tasks by consciously selecting more informative samples to label. Active learning for object detection is more challenging and existing efforts on it are relatively rare. In this paper, we propose a novel hybrid approach to address this problem, where the instance-level uncertainty and diversity are jointly considered in a bottom-up manner. To balance the computational complexity, the proposed approach is designed as a two-stage procedure. At the first stage, an Entropy-based Non-Maximum Suppression (ENMS) is presented to estimate the uncertainty of every image, which performs NMS according to the entropy in the feature space to remove predictions with redundant information gains. At the second stage, a diverse prototype (DivProto) strategy is explored to ensure the diversity across images by progressively converting it into the intra-class and inter-class diversities of the entropy-based class-specific prototypes. Extensive experiments are conducted on MS COCO and Pascal VOC, and the proposed approach achieves state of the art results and significantly outperforms the other counterparts, highlighting its superiority.

### Target-Relevant Knowledge Preservation for Multi-Source Domain Adaptive Object Detection.
- **链接**: [arXiv:2204.07964](https://arxiv.org/abs/2204.07964)
- **作者**: Jiaxi Wu, Jiaxin Chen, Mengzhe He, Yiru Wang, Bo Li, Bingqi Ma et al.
- **🏷️ 机构**: State Key Laboratory of Software Development Environment, Beihang University,Beijing,China, School of Computer Science and Engineering, Beihang University,Beijing,China, Shenzhen Institutes of Advanced Technology, Chinese Academy of Science
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Domain adaptive object detection (DAOD) is a promising way to alleviate performance drop of detectors in new scenes. Albeit great effort made in single source domain adaptation, a more generalized task with multiple source domains remains not being well explored, due to knowledge degradation during their combination. To address this issue, we propose a novel approach, namely target-relevant knowledge preservation (TRKP), to unsupervised multi-source DAOD. Specifically, TRKP adopts the teacher-student framework, where the multi-head teacher network is built to extract knowledge from labeled source domains and guide the student network to learn detectors in unlabeled target domain. The teacher network is further equipped with an adversarial multi-source disentanglement (AMSD) module to preserve source domain-specific knowledge and simultaneously perform cross-domain alignment. Besides, a holistic target-relevant mining (HTRM) scheme is developed to re-weight the source images according to the source-target relevance. By this means, the teacher network is enforced to capture target-relevant knowledge, thus benefiting decreasing domain shift when mentoring object detection in the target domain. Extensive experiments are conducted on various widely used benchmarks with new state-of-the-art scores reported, highlighting the effectiveness.

### Single-Domain Generalized Object Detection in Urban Scene via Cyclic-Disentangled Self-Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00092)
- **作者**: Aming Wu, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China
- **会议**: CVPR 2022

### Revisiting AP Loss for Dense Object Detection: Adaptive Ranking Pair Selection.
- **链接**: [arXiv:2207.12042](https://arxiv.org/abs/2207.12042) · [代码](https://github.com/Xudangliatiger/APE-Loss)
- **作者**: Dongli Xu, Jinhong Deng, Wen Li
- **🏷️ 机构**: School of Computer Science and Engineering &#x0026; Shenzhen Institute for Advanced Study University of Electronic Science and Technology of China
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Average precision (AP) loss has recently shown promising performance on the dense object detection task. However,a deep understanding of how AP loss affects the detector from a pairwise ranking perspective has not yet been developed.In this work, we revisit the average precision (AP)loss and reveal that the crucial element is that of selecting the ranking pairs between positive and negative samples.Based on this observation, we propose two strategies to improve the AP loss. The first of these is a novel Adaptive Pairwise Error (APE) loss that focusing on ranking pairs in both positive and negative samples. Moreover,we select more accurate ranking pairs by exploiting the normalized ranking scores and localization scores with a clustering algorithm. Experiments conducted on the MSCOCO dataset support our analysis and demonstrate the superiority of our proposed method compared with current classification and ranking loss. The code is available at https://github.com/Xudangliatiger/APE-Loss.

### Smartadapt: Multi-branch Object Detection Framework for Videos on Mobiles.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00256)
- **作者**: Ran Xu, Fangzhou Mu, Jayoung Lee, Preeti Mukherjee, Somali Chaterji, Saurabh Bagchi et al.
- **🏷️ 机构**: Purdue University, University of Wisconsin-Madison
- **会议**: CVPR 2022

### H2FA R-CNN: Holistic and Hierarchical Feature Alignment for Cross-domain Weakly Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01393)
- **作者**: Yunqiu Xu, Yifan Sun, Zongxin Yang, Jiaxu Miao, Yi Yang
- **🏷️ 机构**: Baidu Research, Zhejiang University,CCAI
- **会议**: CVPR 2022

### Balanced and Hierarchical Relation Learning for One-shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00744)
- **作者**: Hanqing Yang, Sijia Cai, Hualian Sheng, Bing Deng, Jianqiang Huang, Xian-Sheng Hua et al.
- **🏷️ 机构**: State Key Laboratory of Industrial Control Technology, College of Control Science and Engineering, Zhejiang University, DAMO Academy, Alibaba Group, Shudao Investment Group Co., Ltd
- **会议**: CVPR 2022

### Continual Object Detection via Prototypical Task Correlation Guided Gating Mechanism.
- **链接**: [arXiv:2205.03055](https://arxiv.org/abs/2205.03055)
- **作者**: Binbin Yang, Xinchi Deng, Han Shi, Changlin Li, Gengwei Zhang, Hang Xu et al.
- **🏷️ 机构**: Sun Yat-sen University, The Hong Kong University of Science and Technology, ReLER, AAII, UTS
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Continual learning is a challenging real-world problem for constructing a mature AI system when data are provided in a streaming fashion. Despite recent progress in continual classification, the researches of continual object detection are impeded by the diverse sizes and numbers of objects in each image. Different from previous works that tune the whole network for all tasks, in this work, we present a simple and flexible framework for continual object detection via pRotOtypical taSk corrElaTion guided gaTing mechAnism (ROSETTA). Concretely, a unified framework is shared by all tasks while task-aware gates are introduced to automatically select sub-models for specific tasks. In this way, various knowledge can be successively memorized by storing their corresponding sub-model weights in this system. To make ROSETTA automatically determine which experience is available and useful, a prototypical task correlation guided Gating Diversity Controller(GDC) is introduced to adaptively adjust the diversity of gates for the new task based on class-specific prototypes. GDC module computes class-to-class correlation matrix to depict the cross-task correlation, and hereby activates more exclusive gates for the new task if a significant domain gap is observed. Comprehensive experiments on COCO-VOC, KITTI-Kitchen, class-incremental detection on VOC and sequential learning of four tasks show that ROSETTA yields state-of-the-art performance on both task-based and class-based continual object detection.

### QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection.
- **链接**: [arXiv:2103.09136](https://arxiv.org/abs/2103.09136) · [代码](https://github.com/ChenhongyiYang/QueryDet-PyTorch)
- **作者**: Chenhongyi Yang, Zehao Huang, Naiyan Wang
- **🏷️ 机构**: University of Edinburgh, TuSimple
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > While general object detection with deep learning has achieved great success in the past few years, the performance and efficiency of detecting small objects are far from satisfactory. The most common and effective way to promote small object detection is to use high-resolution images or feature maps. However, both approaches induce costly computation since the computational cost grows squarely as the size of images and features increases. To get the best of two worlds, we propose QueryDet that uses a novel query mechanism to accelerate the inference speed of feature-pyramid based object detectors. The pipeline composes two steps: it first predicts the coarse locations of small objects on low-resolution features and then computes the accurate detection results using high-resolution features sparsely guided by those coarse positions. In this way, we can not only harvest the benefit of high-resolution feature maps but also avoid useless computation for the background area. On the popular COCO dataset, the proposed method improves the detection mAP by 1.0 and mAP-small by 2.0, and the high-resolution inference speed is improved to 3.0x on average. On VisDrone dataset, which contains more small objects, we create a new state-of-the-art while gaining a 2.3x high-resolution acceleration on average. Code is available at https://github.com/ChenhongyiYang/QueryDet-PyTorch.

### Real-time Object Detection for Streaming Perception.
- **链接**: [arXiv:2203.12338](https://arxiv.org/abs/2203.12338) · [代码](https://github.com/yancie-yjr/StreamYOLO) · 📚 被引 58
- **作者**: Jinrong Yang, Songtao Liu, Zeming Li, Xiaoping Li, Jian Sun
- **🏷️ 机构**: Huazhong University of Science and Technology, Megvii Technology
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > Autonomous driving requires the model to perceive the environment and (re)act within a low latency for safety. While past works ignore the inevitable changes in the environment after processing, streaming perception is proposed to jointly evaluate the latency and accuracy into a single metric for video online perception. In this paper, instead of searching trade-offs between accuracy and speed like previous works, we point out that endowing real-time models with the ability to predict the future is the key to dealing with this problem. We build a simple and effective framework for streaming perception. It equips a novel DualFlow Perception module (DFP), which includes dynamic and static flows to capture the moving trend and basic detection feature for streaming prediction. Further, we introduce a Trend-Aware Loss (TAL) combined with a trend factor to generate adaptive weights for objects with different moving speeds. Our simple method achieves competitive performance on Argoverse-HD dataset and improves the AP by 4.9% compared to the strong baseline, validating its effectiveness. Our code will be made available at https://github.com/yancie-yjr/StreamYOLO.

### Sylph: A Hypernetwork Framework for Incremental Few-shot Object Detection.
- **链接**: [arXiv:2203.13903](https://arxiv.org/abs/2203.13903)
- **作者**: Li Yin, Juan M. Perez-Rua, Kevin J. Liang
- **🏷️ 机构**: Meta AI
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > We study the challenging incremental few-shot object detection (iFSD) setting. Recently, hypernetwork-based approaches have been studied in the context of continuous and finetune-free iFSD with limited success. We take a closer look at important design choices of such methods, leading to several key improvements and resulting in a more accurate and flexible framework, which we call Sylph. In particular, we demonstrate the effectiveness of decoupling object classification from localization by leveraging a base detector that is pretrained for class-agnostic localization on a large-scale dataset. Contrary to what previous results have suggested, we show that with a carefully designed class-conditional hypernetwork, finetune-free iFSD can be highly effective, especially when a large number of base categories with abundant data are available for meta-training, almost approaching alternatives that undergo test-time-training. This result is even more significant considering its many practical advantages: (1) incrementally learning new classes in sequence without additional training, (2) detecting both novel and seen classes in a single pass, and (3) no forgetting of previously seen classes. We benchmark our model on both COCO and LVIS, reporting as high as 17% AP on the long-tail rare classes on LVIS, indicating the promise of hypernetwork-based iFSD.

### Democracy Does Matter: Comprehensive Feature Mining for Co-Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00105)
- **作者**: Siyue Yu, Jimin Xiao, Bingfeng Zhang, Eng Gee Lim
- **🏷️ 机构**: XJTLU
- **会议**: CVPR 2022

### Kernelized Few-shot Object Detection with Efficient Integral Aggregation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01861)
- **作者**: Shan Zhang, Lei Wang, Naila Murray, Piotr Koniusz
- **🏷️ 机构**: Australian National University, University of Wollongong, Meta AI Research
- **会议**: CVPR 2022

### Group R-CNN for Weakly Semi-supervised Object Detection with Points.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00920)
- **作者**: Shilong Zhang, Zhuoran Yu, Liyang Liu, Xinjiang Wang, Aojun Zhou, Kai Chen
- **🏷️ 机构**: Shanghai AI Laboratory, Georgia Institute of Technology, Tencent AI Platform Department,China
- **会议**: CVPR 2022

### Task-specific Inconsistency Alignment for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01382)
- **作者**: Liang Zhao, Limin Wang
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2022

### Semantic-aligned Fusion Transformer for One-shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00745)
- **作者**: Yizhou Zhao, Xun Guo, Yan Lu
- **🏷️ 机构**: Carnegie Mellon University, Microsoft Research Asia
- **会议**: CVPR 2022

### Localization Distillation for Dense Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00919)
- **作者**: Zhaohui Zheng, Rongguang Ye, Ping Wang, Dongwei Ren, Wangmeng Zuo, Qibin Hou et al.
- **🏷️ 机构**: Nankai University,TMCC, CS, School of Mathematics, Tianjin University, School of Computer Science and Technology, Harbin Institute of Technology
- **会议**: CVPR 2022

### Progressive End-to-End Object Detection in Crowded Scenes.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00093) · 📚 被引 73
- **作者**: Anlin Zheng, Yuang Zhang, Xiangyu Zhang, Xiaojuan Qi, Jian Sun
- **🏷️ 机构**: MEGVII Technology, Shanghai Jiao Tong University, University of Hong Kong
- **会议**: CVPR 2022

### Multi-Granularity Alignment Domain Adaptation for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00936)
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
