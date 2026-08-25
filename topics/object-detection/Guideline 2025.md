# Object Detection — 2025 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 51 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MI-DETR: An Object Detection Model with Multi-time Inquiries Mechanism.
- **链接**: [arXiv:2503.01463](https://arxiv.org/abs/2503.01463) · 📚 被引 17
- **作者**: Zhixiong Nan, Xianghong Li, Jifeng Dai, Tao Xiang
- **🏷️ 机构**: Chongqing University,College of Computer Science,Chongqing,China, Tsinghua University,Department of Electronic Engineering,Beijing,China
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Based on analyzing the character of cascaded decoder architecture commonly adopted in existing DETR-like models, this paper proposes a new decoder architecture. The cascaded decoder architecture constrains object queries to update in the cascaded direction, only enabling object queries to learn relatively-limited information from image features. However, the challenges for object detection in natural scenes (e.g., extremely-small, heavily-occluded, and confusingly mixed with the background) require an object detection model to fully utilize image features, which motivates us to propose a new decoder architecture with the parallel Multi-time Inquiries (MI) mechanism. MI enables object queries to learn more comprehensive information, and our MI based model, MI-DETR, outperforms all existing DETR-like models on COCO benchmark under different backbones and training epochs, achieving +2.3 AP and +0.6 AP improvements compared to the most representative model DINO and SOTA model Relation-DETR under ResNet-50 backbone. In addition, a series of diagnostic and visualization experiments demonstrate the effectiveness, rationality, and interpretability of MI.

### Object Detection using Event Camera: A MoE Heat Conduction based Detector and A New Benchmark Dataset.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Object_Detection_using_Event_Camera_A_MoE_Heat_Conduction_based_CVPR_2025_paper.html)
- **作者**: Xiao Wang, Yu Jin, Wentao Wu, Wei Zhang, Lin Zhu, Bo Jiang et al.
- **🏷️ 机构**: Anhui University,School of Computer Science and Technology,Hefei,China, Anhui University,School of Artificial Intelligence,Hefei,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: CVPR 2025

### Open-World Objectness Modeling Unifies Novel Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Open-World_Objectness_Modeling_Unifies_Novel_Object_Detection_CVPR_2025_paper.html)
- **作者**: Shan Zhang, Yao Ni, Jinhao Du, Yuan Xue, Philip Torr, Piotr Koniusz et al.
- **🏷️ 机构**: Australian Institute for Machine Learning, Australian National University, Peking University
- **会议**: CVPR 2025

### Test-Time Backdoor Detection for Object Detection Models.
- **链接**: [arXiv:2503.15293](https://arxiv.org/abs/2503.15293)
- **作者**: Hangtao Zhang, Yichen Wang, Shihui Yan, Chenyu Zhu, Ziqi Zhou, Linshan Hou et al.
- **🏷️ 机构**: Huazhong University of Science and Technology,School of Cyber Science and Engineering, Huazhong University of Science and Technology,School of Software Engineering, Huazhong University of Science and Technology,School of Computer Science and Technology
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Object detection models are vulnerable to backdoor attacks, where attackers poison a small subset of training samples by embedding a predefined trigger to manipulate prediction. Detecting poisoned samples (i.e., those containing triggers) at test time can prevent backdoor activation. However, unlike image classification tasks, the unique characteristics of object detection -- particularly its output of numerous objects -- pose fresh challenges for backdoor detection. The complex attack effects (e.g., "ghost" object emergence or "vanishing" object) further render current defenses fundamentally inadequate. To this end, we design TRAnsformation Consistency Evaluation (TRACE), a brand-new method for detecting poisoned samples at test time in object detection. Our journey begins with two intriguing observations: (1) poisoned samples exhibit significantly more consistent detection results than clean ones across varied backgrounds. (2) clean samples show higher detection consistency when introduced to different focal information. Based on these phenomena, TRACE applies foreground and background transformations to each test sample, then assesses transformation consistency by calculating the variance in objects confidences. TRACE achieves black-box, universal backdoor detection, with extensive experiments showing a 30% improvement in AUROC over state-of-the-art defenses and resistance to adaptive attacks.

### ReDiffDet: Rotation-equivariant Diffusion Model for Oriented Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_ReDiffDet_Rotation-equivariant_Diffusion_Model_for_Oriented_Object_Detection_CVPR_2025_paper.html)
- **作者**: Jiaqi Zhao, Zeyu Ding, Yong Zhou, Hancheng Zhu, Wen-Liang Du, Rui Yao
- **🏷️ 机构**: China University of Mining and Technology,School of Computer Science and Technology
- **会议**: CVPR 2025

### SEEN-DA: SEmantic ENtropy guided Domain-aware Attention for Domain Adaptive Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_SEEN-DA_SEmantic_ENtropy_guided_Domain-aware_Attention_for_Domain_Adaptive_Object_CVPR_2025_paper.html)
- **作者**: Haochen Li, Rui Zhang, Hantao Yao, Xin Zhang, Yifan Hao, Xinkai Song et al.
- **🏷️ 机构**: Institute of Software, CAS,Intelligent Software Research Center, Institute of Computing Technology, CAS,State Key Lab of Processors, University of Science and Technology of China,School of Information Science and Technology
- **会议**: CVPR 2025

### Learning Endogenous Attention for Incremental Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Song_Learning_Endogenous_Attention_for_Incremental_Object_Detection_CVPR_2025_paper.html)
- **作者**: Xiang Song, Yuhang He, Jingyuan Li, Qiang Wang, Yihong Gong
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence
- **会议**: CVPR 2025

### Point2RBox-v2: Rethinking Point-supervised Oriented Object Detection with Spatial Layout Among Instances.
- **链接**: [arXiv:2502.04268](https://arxiv.org/abs/2502.04268) · [代码](https://github.com/VisionXLab/point2rbox-v2)
- **作者**: Yi Yu, Botao Ren, Peiyuan Zhang, Mingxin Liu, Junwei Luo, Shaofeng Zhang et al.
- **🏷️ 机构**: Southeast University, Tsinghua University, Wuhan University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > With the rapidly increasing demand for oriented object detection (OOD), recent research involving weakly-supervised detectors for learning OOD from point annotations has gained great attention. In this paper, we rethink this challenging task setting with the layout among instances and present Point2RBox-v2. At the core are three principles: 1) Gaussian overlap loss. It learns an upper bound for each instance by treating objects as 2D Gaussian distributions and minimizing their overlap. 2) Voronoi watershed loss. It learns a lower bound for each instance through watershed on Voronoi tessellation. 3) Consistency loss. It learns the size/rotation variation between two output sets with respect to an input image and its augmented view. Supplemented by a few devised techniques, e.g. edge loss and copy-paste, the detector is further enhanced. To our best knowledge, Point2RBox-v2 is the first approach to explore the spatial layout among instances for learning point-supervised OOD. Our solution is elegant and lightweight, yet it is expected to give a competitive performance especially in densely packed scenes: 62.61%/86.15%/34.71% on DOTA/HRSC/FAIR1M. Code is available at https://github.com/VisionXLab/point2rbox-v2.

### Efficient Event-Based Object Detection: A Hybrid Neural Network with Spatial and Temporal Attention.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ahmed_Efficient_Event-Based_Object_Detection_A_Hybrid_Neural_Network_with_Spatial_CVPR_2025_paper.html)
- **作者**: Soikat Hasan Ahmed, Jan Finkbeiner, Emre Neftci
- **🏷️ 机构**: RWTH Aachen University,Forschungszentrum J&#x00FC;lich
- **会议**: CVPR 2025

### Fractal Calibration for Long-tailed Object Detection.
- **链接**: [arXiv:2410.11774](https://arxiv.org/abs/2410.11774) · [代码](https://github.com/kostas1515/FRACAL)
- **作者**: Konstantinos Panagiotis Alexandridis, Ismail Elezi, Jiankang Deng, Anh Nguyen, Shan Luo
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab, Imperial College London, University of Liverpool
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Real-world datasets follow an imbalanced distribution, which poses significant challenges in rare-category object detection. Recent studies tackle this problem by developing re-weighting and re-sampling methods, that utilise the class frequencies of the dataset. However, these techniques focus solely on the frequency statistics and ignore the distribution of the classes in image space, missing important information. In contrast to them, we propose FRActal CALibration (FRACAL): a novel post-calibration method for long-tailed object detection. FRACAL devises a logit adjustment method that utilises the fractal dimension to estimate how uniformly classes are distributed in image space. During inference, it uses the fractal dimension to inversely downweight the probabilities of uniformly spaced class predictions achieving balance in two axes: between frequent and rare categories, and between uniformly spaced and sparsely spaced classes. FRACAL is a post-processing method and it does not require any training, also it can be combined with many off-the-shelf models such as one-stage sigmoid detectors and two-stage instance segmentation models. FRACAL boosts the rare class performance by up to 8.6% and surpasses all previous methods on LVIS dataset, while showing good generalisation to other datasets such as COCO, V3Det and OpenImages. We provide the code at https://github.com/kostas1515/FRACAL.

### ReRAW: RGB-to-RAW Image Reconstruction via Stratified Sampling for Efficient Object Detection on the Edge.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Berdan_ReRAW_RGB-to-RAW_Image_Reconstruction_via_Stratified_Sampling_for_Efficient_Object_CVPR_2025_paper.html)
- **作者**: Radu Berdan, Beril Besbinar, Christoph Reinders, Junji Otsuka, Daisuke Iso
- **🏷️ 机构**: Sony AI, Leibniz University Hannover, Sony Group Corporation
- **会议**: CVPR 2025

### Believing is Seeing: Unobserved Object Detection using Generative Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Bhattacharjee_Believing_is_Seeing_Unobserved_Object_Detection_using_Generative_Models_CVPR_2025_paper.html)
- **作者**: Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome
- **🏷️ 机构**: The Australian National University,School of Computing
- **会议**: CVPR 2025

### Feature Information Driven Position Gaussian Distribution Estimation for Tiny Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Bian_Feature_Information_Driven_Position_Gaussian_Distribution_Estimation_for_Tiny_Object_CVPR_2025_paper.html)
- **作者**: Jinghao Bian, Mingtao Feng, Weisheng Dong, Fangfang Wu, Jianqiao Luo, Yaonan Wang et al.
- **🏷️ 机构**: Xidian University, Hunan University
- **会议**: CVPR 2025

### Shift the Lens: Environment-Aware Unsupervised Camouflaged Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Du_Shift_the_Lens_Environment-Aware_Unsupervised_Camouflaged_Object_Detection_CVPR_2025_paper.html)
- **作者**: Ji Du, Fangwei Hao, Mingyang Yu, Desheng Kong, Jiesheng Wu, Bin Wang et al.
- **🏷️ 机构**: Nankai University,College of Artificial Intelligence,China, The Hong Kong Polytechnic University,Department of Computing,Hong Kong
- **会议**: CVPR 2025

### Samba: A Unified Mamba-based Framework for General Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/He_Samba_A_Unified_Mamba-based_Framework_for_General_Salient_Object_Detection_CVPR_2025_paper.html)
- **作者**: Jiahao He, Keren Fu, Xiaohong Liu, Qijun Zhao
- **🏷️ 机构**: Sichuan University,College of CS, Shanghai Jiao Tong University,John Hopcroft Center
- **会议**: CVPR 2025

### Large Self-Supervised Models Bridge the Gap in Domain Adaptive Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lavoie_Large_Self-Supervised_Models_Bridge_the_Gap_in_Domain_Adaptive_Object_CVPR_2025_paper.html)
- **作者**: Marc-Antoine Lavoie, Anas Mahmoud, Steven L. Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Brain-Inspired Spiking Neural Networks for Energy-Efficient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Brain-Inspired_Spiking_Neural_Networks_for_Energy-Efficient_Object_Detection_CVPR_2025_paper.html)
- **作者**: Ziqi Li, Tao Gao, Yisheng An, Ting Chen, Jing Zhang, Yuanbo Wen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Pseudo Visible Feature Fine-Grained Fusion for Thermal Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Pseudo_Visible_Feature_Fine-Grained_Fusion_for_Thermal_Object_Detection_CVPR_2025_paper.html)
- **作者**: Ting Li, Mao Ye, Tianwen Wu, Nianxin Li, Shuaifeng Li, Song Tang et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, University of Shanghai for Science and Technology
- **会议**: CVPR 2025

### Towards RAW Object Detection in Diverse Conditions.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Towards_RAW_Object_Detection_in_Diverse_Conditions_CVPR_2025_paper.html)
- **作者**: Zhongyu Li, Xin Jin, Bo-Yuan Sun, Chun-Le Guo, Ming-Ming Cheng
- **🏷️ 机构**: VCIP, CS, Nankai University
- **会议**: CVPR 2025

### PointSR: Self-Regularized Point Supervision for Drone-View Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_PointSR_Self-Regularized_Point_Supervision_for_Drone-View_Object_Detection_CVPR_2025_paper.html)
- **作者**: Weizhuo Li, Yue Xi, Wenjing Jia, Zehao Zhang, Fei Li, Xiangzeng Liu et al.
- **🏷️ 机构**: Guangzhou Institute of Technology, Xidian University,Guangzhou,China, Faculty of Engineering and IT, University of Technology Sydney,Sydney,Australia, Xidian University,School of Computer Science and Technology,Xi&#x2019;an,China
- **会议**: CVPR 2025

### GauCho: Gaussian Distributions with Cholesky Decomposition for Oriented Object Detection.
- **链接**: [arXiv:2502.01565](https://arxiv.org/abs/2502.01565)
- **作者**: Jose Henrique Lima Marques, Jeffri Murrugarra-Llerena, Cláudio R. Jung
- **🏷️ 机构**: Federal University of Rio Grande do Sul, Stony Brook University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Oriented Object Detection (OOD) has received increased attention in the past years, being a suitable solution for detecting elongated objects in remote sensing analysis. In particular, using regression loss functions based on Gaussian distributions has become attractive since they yield simple and differentiable terms. However, existing solutions are still based on regression heads that produce Oriented Bounding Boxes (OBBs), and the known problem of angular boundary discontinuity persists. In this work, we propose a regression head for OOD that directly produces Gaussian distributions based on the Cholesky matrix decomposition. The proposed head, named GauCho, theoretically mitigates the boundary discontinuity problem and is fully compatible with recent Gaussian-based regression loss functions. Furthermore, we advocate using Oriented Ellipses (OEs) to represent oriented objects, which relates to GauCho through a bijective function and alleviates the encoding ambiguity problem for circular objects. Our experimental results show that GauCho can be a viable alternative to the traditional OBB head, achieving results comparable to or better than state-of-the-art detectors for the challenging dataset DOTA

### Search and Detect: Training-Free Long Tail Object Detection via Web-Image Retrieval.
- **链接**: [arXiv:2409.18733](https://arxiv.org/abs/2409.18733)
- **作者**: Mankeerat Sidhu, Hetarth Chopra, Ansel Blume, Jeonghwan Kim, Revanth Gangi Reddy, Heng Ji
- **🏷️ 机构**: University of Illinois Urbana Champaign,Urbana,USA
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > In this paper, we introduce SearchDet, a training-free long-tail object detection framework that significantly enhances open-vocabulary object detection performance. SearchDet retrieves a set of positive and negative images of an object to ground, embeds these images, and computes an input image-weighted query which is used to detect the desired concept in the image. Our proposed method is simple and training-free, yet achieves over 48.7% mAP improvement on ODinW and 59.1% mAP improvement on LVIS compared to state-of-the-art models such as GroundingDINO. We further show that our approach of basing object detection on a set of Web-retrieved exemplars is stable with respect to variations in the exemplars, suggesting a path towards eliminating costly data annotation and training procedures.

### SET: Spectral Enhancement for Tiny Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_SET_Spectral_Enhancement_for_Tiny_Object_Detection_CVPR_2025_paper.html)
- **作者**: Huixin Sun, Runqi Wang, Yanjing Li, Linlin Yang, Shaohui Lin, Xianbin Cao et al.
- **🏷️ 机构**: Beihang University,School of Electronic Information Engineering,Beijing,China, Beijing Jiaotong University,School of Computer Science and Technology, Communication University of China,State Key Laboratory of Media Convergence and Communication,Beijing,China
- **会议**: CVPR 2025

### AeroGen: Enhancing Remote Sensing Object Detection with Diffusion-Driven Data Generation.
- **链接**: [arXiv:2411.15497](https://arxiv.org/abs/2411.15497) · [代码](https://github.com/Sonettoo/AeroGen)
- **作者**: Datao Tang, Xiangyong Cao, Xuan Wu, Jialin Li, Jing Yao, Xueru Bai et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Computer Science and Technology,Xi&#x2019;an,China,710049, Chinese Academy of Sciences, Xidian University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Remote sensing image object detection (RSIOD) aims to identify and locate specific objects within satellite or aerial imagery. However, there is a scarcity of labeled data in current RSIOD datasets, which significantly limits the performance of current detection algorithms. Although existing techniques, e.g., data augmentation and semi-supervised learning, can mitigate this scarcity issue to some extent, they are heavily dependent on high-quality labeled data and perform worse in rare object classes. To address this issue, this paper proposes a layout-controllable diffusion generative model (i.e. AeroGen) tailored for RSIOD. To our knowledge, AeroGen is the first model to simultaneously support horizontal and rotated bounding box condition generation, thus enabling the generation of high-quality synthetic images that meet specific layout and object category requirements. Additionally, we propose an end-to-end data augmentation framework that integrates a diversity-conditioned generator and a filtering mechanism to enhance both the diversity and quality of generated data. Experimental results demonstrate that the synthetic data produced by our method are of high quality and diversity. Furthermore, the synthetic RSIOD data can significantly improve the detection performance of existing RSIOD models, i.e., the mAP metrics on DIOR, DIOR-R, and HRSC datasets are improved by 3.7%, 4.3%, and 2.43%, respectively. The code is available at https://github.com/Sonettoo/AeroGen.

### SimLTD: Simple Supervised and Semi-Supervised Long-Tailed Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tran_SimLTD_Simple_Supervised_and_Semi-Supervised_Long-Tailed_Object_Detection_CVPR_2025_paper.html)
- **作者**: Phi Vu Tran
- **🏷️ 机构**: LexisNexis Risk Solutions
- **会议**: CVPR 2025

### Visual Consensus Prompting for Co-Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Visual_Consensus_Prompting_for_Co-Salient_Object_Detection_CVPR_2025_paper.html)
- **作者**: Jie Wang, Nana Yu, Zihao Zhang, Yahong Han
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing,China
- **会议**: CVPR 2025

### Percept, Memory, and Imagine: World Feature Simulating for Open-Domain Unknown Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Percept_Memory_and_Imagine_World_Feature_Simulating_for_Open-Domain_Unknown_CVPR_2025_paper.html)
- **作者**: Aming Wu, Cheng Deng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### OW-OVD: Unified Open World and Open Vocabulary Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xi_OW-OVD_Unified_Open_World_and_Open_Vocabulary_Object_Detection_CVPR_2025_paper.html)
- **作者**: Xing Xi, Yangyang Huang, Ronghua Luo, Yu Qiu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### UCOD-DPL: Unsupervised Camouflaged Object Detection via Dynamic Pseudo-label Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yan_UCOD-DPL_Unsupervised_Camouflaged_Object_Detection_via_Dynamic_Pseudo-label_Learning_CVPR_2025_paper.html)
- **作者**: Weiqi Yan, Lvhai Chen, Huaijia Kou, Shengchuan Zhang, Yan Zhang, Liujuan Cao
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,P.R. China,361005
- **会议**: CVPR 2025

### SparseAlign: a Fully Sparse Framework for Cooperative Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yuan_SparseAlign_a_Fully_Sparse_Framework_for_Cooperative_Object_Detection_CVPR_2025_paper.html)
- **作者**: Yunshuang Yuan, Yan Xia, Daniel Cremers, Monika Sester
- **🏷️ 机构**: Leibniz University Hannover, Technical University of Munich
- **会议**: CVPR 2025

### Revisiting Generative Replay for Class Incremental Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Revisiting_Generative_Replay_for_Class_Incremental_Object_Detection_CVPR_2025_paper.html)
- **作者**: Shizhou Zhang, Xueqiang Lv, Yinghui Xing, Qirui Wu, Di Xu, Yanning Zhang
- **🏷️ 机构**: Northwestern Polytechnical University, Huawei Cloud Computing Technologies Co., Ltd
- **会议**: CVPR 2025

### Style Evolving along Chain-of-Thought for Unknown-Domain Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Style_Evolving_along_Chain-of-Thought_for_Unknown-Domain_Object_Detection_CVPR_2025_paper.html)
- **作者**: Zihao Zhang, Aming Wu, Yahong Han
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing,Tianjin,China, Xidian University,School of Electronic Engineering,Xi&#x2019;an,China
- **会议**: CVPR 2025

### BOOTPLACE: Bootstrapped Object Placement with Detection Transformers.
- **链接**: [arXiv:2503.21991](https://arxiv.org/abs/2503.21991)
- **作者**: Hang Zhou, Xinxin Zuo, Rui Ma, Li Cheng
- **🏷️ 机构**: University of Alberta, Concordia University, Jilin University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > In this paper, we tackle the copy-paste image-to-image composition problem with a focus on object placement learning. Prior methods have leveraged generative models to reduce the reliance for dense supervision. However, this often limits their capacity to model complex data distributions. Alternatively, transformer networks with a sparse contrastive loss have been explored, but their over-relaxed regularization often leads to imprecise object placement. We introduce BOOTPLACE, a novel paradigm that formulates object placement as a placement-by-detection problem. Our approach begins by identifying suitable regions of interest for object placement. This is achieved by training a specialized detection transformer on object-subtracted backgrounds, enhanced with multi-object supervisions. It then semantically associates each target compositing object with detected regions based on their complementary characteristics. Through a boostrapped training approach applied to randomly object-subtracted images, our model enforces meaningful placements through extensive paired data augmentation. Experimental results on established benchmarks demonstrate BOOTPLACE's superior performance in object repositioning, markedly surpassing state-of-the-art baselines on Cityscapes and OPA datasets with notable improvements in IOU scores. Additional ablation studies further showcase the compositionality and generalizability of our approach, supported by user study evaluations.

## 跨领域论文（完整笔记在其他领域）

- UniMamba: Unified Spatial-Channel Representation Learning with Group-Efficient Mamba for LiDAR-based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras. → [3d-detection](../3d-detection/Guideline%202025.md)
- RaCFormer: Towards High-Quality 3D Object Detection via Query-based Radar-Camera Fusion. → [3d-detection](../3d-detection/Guideline%202025.md)
- V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Cubify Anything: Scaling Indoor 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- FSHNet: Fully Sparse Hybrid Network for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- MonoTAKD: Teaching Assistant Knowledge Distillation for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- RICCARDO: Radar Hit Prediction and Convolution for Camera-Radar 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- GBlobs: Explicit Local Structure via Gaussian Blobs for Improved Cross-Domain LiDAR-based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Leveraging Temporal Cues for Semi-Supervised Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- MonoDGP: Monocular 3D Object Detection with Decoupled-Query and Geometry-Error Priors. → [3d-detection](../3d-detection/Guideline%202025.md)
- Uncertainty Meets Diversity: A Comprehensive Active Learning Framework for Indoor 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Efficient Test-time Adaptive Object Detection via Sensitivity-Guided Pruning. → [network-pruning](../network-pruning/Guideline%202025.md)
- CorrBEV: Multi-View 3D Object Detection by Correlation Learning with Multi-modal Prototypes. → [3d-detection](../3d-detection/Guideline%202025.md)
- ROD-MLLM: Towards More Reliable Object Detection in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- ViKIENet: Towards Efficient 3D Object Detection with Virtual Key Instance Enhanced Network. → [3d-detection](../3d-detection/Guideline%202025.md)
- SP3D: Boosting Sparsely-Supervised 3D Object Detection via Accurate Cross-Modal Semantic Prompts. → [3d-detection](../3d-detection/Guideline%202025.md)
- Learning Class Prototypes for Unified Sparse-Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
