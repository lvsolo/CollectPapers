# Object Detection — 2025 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 64 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Event-Based Tiny Object Detection: A Benchmark Dataset and Baseline.
- **链接**: [arXiv:2506.23575](https://arxiv.org/abs/2506.23575) · [代码](https://github.com/ChenYichen9527/Ev-UAV) · 📚 被引 6
- **作者**: Nuo Chen, Chao Xiao, Yimian Dai, Shiman He, Miao Li, Wei An
- **🏷️ 机构**: National University of Defense Technology, Nankai University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Based on analyzing the character of cascaded decoder architecture commonly adopted in existing DETR-like models, this paper proposes a new decoder architecture. The cascaded decoder architecture constrains object queries to update in the cascaded direction, only enabling object queries to learn relatively-limited information from image features. However, the challenges for object detection in natural scenes (e.g., extremely-small, heavily-occluded, and confusingly mixed with the background) require an object detection model to fully utilize image features, which motivates us to propose a new decoder architecture with the parallel Multi-time Inquiries (MI) mechanism. MI enables object queries to learn more comprehensive information, and our MI based model, MI-DETR, outperforms all existing DETR-like models on COCO benchmark under different backbones and training epochs, achieving +2.3 AP and +0.6 AP improvements compared to the most representative model DINO and SOTA model Relation-DETR under ResNet-50 backbone. In addition, a series of diagnostic and visualization experiments demonstrate the effectiveness, rationality, and interpretability of MI.

</details>

</details>

### Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-Time Open-Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01938)
- **作者**: Yehao Lu, Minghe Weng, Zekang Xiao, Rui Jiang, Wei Su, Guangcong Zheng et al.
- **🏷️ 机构**: ZJU
- **会议**: ICCV 2025

### STEP-DETR: Advancing DETR-based Semi-Supervised Object Detection with Super Teacher and Pseudo-Label Guided Text Queries.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00294) · 📚 被引 3
- **作者**: Tahira Shehzadi, Khurram Azeem Hashmi, Shalini Sarode, Didier Stricker, Muhammad Zeshan Afzal
- **🏷️ 机构**: DFKI
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection models are vulnerable to backdoor attacks, where attackers poison a small subset of training samples by embedding a predefined trigger to manipulate prediction. Detecting poisoned samples (i.e., those containing triggers) at test time can prevent backdoor activation. However, unlike image classification tasks, the unique characteristics of object detection -- particularly its output of numerous objects -- pose fresh challenges for backdoor detection. The complex attack effects (e.g., "ghost" object emergence or "vanishing" object) further render current defenses fundamentally inadequate. To this end, we design TRAnsformation Consistency Evaluation (TRACE), a brand-new method for detecting poisoned samples at test time in object detection. Our journey begins with two intriguing observations: (1) poisoned samples exhibit significantly more consistent detection results than clean ones across varied backgrounds. (2) clean samples show higher detection consistency when introduced to different focal information. Based on these phenomena, TRACE applies foreground and background transformations to each test sample, then assesses transformation consistency by calculating the variance in objects confidences. TRACE achieves black-box, universal backdoor detection, with extensive experiments showing a 30% improvement in AUROC over state-of-the-art defenses and resistance to adaptive attacks.

</details>

### ReDiffDet: Rotation-equivariant Diffusion Model for Oriented Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_ReDiffDet_Rotation-equivariant_Diffusion_Model_for_Oriented_Object_Detection_CVPR_2025_paper.html) · 📚 被引 17
- **作者**: Jiaqi Zhao, Zeyu Ding, Yong Zhou, Hancheng Zhu, Wen-Liang Du, Rui Yao
- **🏷️ 机构**: China University of Mining and Technology,School of Computer Science and Technology
- **会议**: CVPR 2025

### SEEN-DA: SEmantic ENtropy guided Domain-aware Attention for Domain Adaptive Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_SEEN-DA_SEmantic_ENtropy_guided_Domain-aware_Attention_for_Domain_Adaptive_Object_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Haochen Li, Rui Zhang, Hantao Yao, Xin Zhang, Yifan Hao, Xinkai Song et al.
- **🏷️ 机构**: Institute of Software, CAS,Intelligent Software Research Center, Institute of Computing Technology, CAS,State Key Lab of Processors, University of Science and Technology of China,School of Information Science and Technology
- **会议**: CVPR 2025

### Learning Endogenous Attention for Incremental Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Song_Learning_Endogenous_Attention_for_Incremental_Object_Detection_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Xiang Song, Yuhang He, Jingyuan Li, Qiang Wang, Yihong Gong
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering, Xi&#x2019;an Jiaotong University,College of Artificial Intelligence
- **会议**: CVPR 2025

### Point2RBox-v2: Rethinking Point-supervised Oriented Object Detection with Spatial Layout Among Instances.
- **链接**: [arXiv:2502.04268](https://arxiv.org/abs/2502.04268) · [代码](https://github.com/VisionXLab/point2rbox-v2) · 📚 被引 13
- **作者**: Yi Yu, Botao Ren, Peiyuan Zhang, Mingxin Liu, Junwei Luo, Shaofeng Zhang et al.
- **🏷️ 机构**: Southeast University, Tsinghua University, Wuhan University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rapidly increasing demand for oriented object detection (OOD), recent research involving weakly-supervised detectors for learning OOD from point annotations has gained great attention. In this paper, we rethink this challenging task setting with the layout among instances and present Point2RBox-v2. At the core are three principles: 1) Gaussian overlap loss. It learns an upper bound for each instance by treating objects as 2D Gaussian distributions and minimizing their overlap. 2) Voronoi watershed loss. It learns a lower bound for each instance through watershed on Voronoi tessellation. 3) Consistency loss. It learns the size/rotation variation between two output sets with respect to an input image and its augmented view. Supplemented by a few devised techniques, e.g. edge loss and copy-paste, the detector is further enhanced. To our best knowledge, Point2RBox-v2 is the first approach to explore the spatial layout among instances for learning point-supervised OOD. Our solution is elegant and lightweight, yet it is expected to give a competitive performance especially in densely packed scenes: 62.61%/86.15%/34.71% on DOTA/HRSC/FAIR1M. Code is available at https://github.com/VisionXLab/point2rbox-v2.

</details>

### Efficient Event-Based Object Detection: A Hybrid Neural Network with Spatial and Temporal Attention.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ahmed_Efficient_Event-Based_Object_Detection_A_Hybrid_Neural_Network_with_Spatial_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Soikat Hasan Ahmed, Jan Finkbeiner, Emre Neftci
- **🏷️ 机构**: RWTH Aachen University,Forschungszentrum J&#x00FC;lich
- **会议**: CVPR 2025

### Fractal Calibration for Long-tailed Object Detection.
- **链接**: [arXiv:2410.11774](https://arxiv.org/abs/2410.11774) · [代码](https://github.com/kostas1515/FRACAL) · 📚 被引 3
- **作者**: Konstantinos Panagiotis Alexandridis, Ismail Elezi, Jiankang Deng, Anh Nguyen, Shan Luo
- **🏷️ 机构**: Huawei Noah&#x2019;s Ark Lab, Imperial College London, University of Liverpool
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world datasets follow an imbalanced distribution, which poses significant challenges in rare-category object detection. Recent studies tackle this problem by developing re-weighting and re-sampling methods, that utilise the class frequencies of the dataset. However, these techniques focus solely on the frequency statistics and ignore the distribution of the classes in image space, missing important information. In contrast to them, we propose FRActal CALibration (FRACAL): a novel post-calibration method for long-tailed object detection. FRACAL devises a logit adjustment method that utilises the fractal dimension to estimate how uniformly classes are distributed in image space. During inference, it uses the fractal dimension to inversely downweight the probabilities of uniformly spaced class predictions achieving balance in two axes: between frequent and rare categories, and between uniformly spaced and sparsely spaced classes. FRACAL is a post-processing method and it does not require any training, also it can be combined with many off-the-shelf models such as one-stage sigmoid detectors and two-stage instance segmentation models. FRACAL boosts the rare class performance by up to 8.6% and surpasses all previous methods on LVIS dataset, while showing good generalisation to other datasets such as COCO, V3Det and OpenImages. We provide the code at https://github.com/kostas1515/FRACAL.

</details>

### ReRAW: RGB-to-RAW Image Reconstruction via Stratified Sampling for Efficient Object Detection on the Edge.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Berdan_ReRAW_RGB-to-RAW_Image_Reconstruction_via_Stratified_Sampling_for_Efficient_Object_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Radu Berdan, Beril Besbinar, Christoph Reinders, Junji Otsuka, Daisuke Iso
- **🏷️ 机构**: Sony AI, Leibniz University Hannover, Sony Group Corporation
- **会议**: CVPR 2025

### Believing is Seeing: Unobserved Object Detection using Generative Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Bhattacharjee_Believing_is_Seeing_Unobserved_Object_Detection_using_Generative_Models_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome
- **🏷️ 机构**: The Australian National University,School of Computing
- **会议**: CVPR 2025

### Feature Information Driven Position Gaussian Distribution Estimation for Tiny Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Bian_Feature_Information_Driven_Position_Gaussian_Distribution_Estimation_for_Tiny_Object_CVPR_2025_paper.html) · 📚 被引 14
- **作者**: Jinghao Bian, Mingtao Feng, Weisheng Dong, Fangfang Wu, Jianqiao Luo, Yaonan Wang et al.
- **🏷️ 机构**: Xidian University, Hunan University
- **会议**: CVPR 2025

### Shift the Lens: Environment-Aware Unsupervised Camouflaged Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Du_Shift_the_Lens_Environment-Aware_Unsupervised_Camouflaged_Object_Detection_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Ji Du, Fangwei Hao, Mingyang Yu, Desheng Kong, Jiesheng Wu, Bin Wang et al.
- **🏷️ 机构**: Nankai University,College of Artificial Intelligence,China, The Hong Kong Polytechnic University,Department of Computing,Hong Kong
- **会议**: CVPR 2025

### Samba: A Unified Mamba-based Framework for General Salient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/He_Samba_A_Unified_Mamba-based_Framework_for_General_Salient_Object_Detection_CVPR_2025_paper.html) · 📚 被引 14
- **作者**: Jiahao He, Keren Fu, Xiaohong Liu, Qijun Zhao
- **🏷️ 机构**: Sichuan University,College of CS, Shanghai Jiao Tong University,John Hopcroft Center
- **会议**: CVPR 2025

### Large Self-Supervised Models Bridge the Gap in Domain Adaptive Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lavoie_Large_Self-Supervised_Models_Bridge_the_Gap_in_Domain_Adaptive_Object_CVPR_2025_paper.html)
- **作者**: Marc-Antoine Lavoie, Anas Mahmoud, Steven L. Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Active Learning Meets Foundation Models: Fast Remote Sensing Data Annotation for Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00572) · 📚 被引 0
- **作者**: Marvin Burges, Philipe Ambrozio Dias, Carson Woody, Sarah Walters, Dalton D. Lunga
- **🏷️ 机构**: TU Wien,Vienna,Vienna,Austria, Oak Ridge National Laboratory,Oak Ridge,Tennessee,USA
- **会议**: ICCV 2025

### Cycle-Consistent Learning for Joint Layout-to-Image Generation and Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00639) · 📚 被引 1
- **作者**: Xinhao Cai, Qiuxia Lai, Gensheng Pei, Xiangbo Shu, Yazhou Yao, Wenguan Wang
- **🏷️ 机构**: Nanjing University of Science and Technology, Communication University of China, Zhejiang University
- **会议**: ICCV 2025

### Enhancing Prompt Generation with Adaptive Refinement for Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01922) · 📚 被引 0
- **作者**: Xuehan Chen, Guangyu Ren, Tianhong Dai, Tania Stathaki, Hengyan Liu
- **🏷️ 机构**: Xi&#x0027;an Jiaotong-Liverpool University,China, Imperial College London,United Kingdom
- **会议**: ICCV 2025

### Debiased Teacher for Day-to-Night Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00248) · 📚 被引 2
- **作者**: Yiming Cui, Liang Li, Haibing Yin, Yuhan Gao, Yaoqi Sun, Chenggang Yan
- **🏷️ 机构**: Hangzhou Dianzi University, Institute of Computing Technology, Chinese Academy of Sciences, Lishui University
- **会议**: ICCV 2025

### Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection.
- **链接**: [arXiv:2510.18437](https://arxiv.org/abs/2510.18437) · [代码](https://github.com/xiaohainku/RISE) · 📚 被引 1
- **作者**: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen, Jiesheng Wu et al.
- **🏷️ 机构**: College of Artificial Intelligence, Nankai University,China, The Hong Kong Polytechnic University,Department of Computing,Hong Kong, School of Computer and Information, Anhui Normal University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> At the core of Camouflaged Object Detection (COD) lies segmenting objects from their highly similar surroundings. Previous efforts navigate this challenge primarily through image-level modeling or annotation-based optimization. Despite advancing considerably, this commonplace practice hardly taps valuable dataset-level contextual information or relies on laborious annotations. In this paper, we propose RISE, a RetrIeval SElf-augmented paradigm that exploits the entire training dataset to generate pseudo-labels for single images, which could be used to train COD models. RISE begins by constructing prototype libraries for environments and camouflaged objects using training images (without ground truth), followed by K-Nearest Neighbor (KNN) retrieval to generate pseudo-masks for each image based on these libraries. It is important to recognize that using only training images without annotations exerts a pronounced challenge in crafting high-quality prototype libraries. In this light, we introduce a Clustering-then-Retrieval (CR) strategy, where coarse masks are first generated through clustering, facilitating subsequent histogram-based image filtering and cross-category retrieval to produce high-confidence prototypes. In the KNN retrieval stage, to alleviate the effect of artifacts in feature maps, we propose Multi-View KNN Retrieval (MVKR), which integrates retrieval results from diverse views to produce more robust and precise pseudo-masks. Extensive experiments demonstrate that RISE outperforms state-of-the-art unsupervised and prompt-based methods. Code is available at https://github.com/xiaohainku/RISE.

</details>

### Unified Category-Level Object Detection and Pose Estimation from RGB Images Using 3D Prototypes.
- **链接**: [arXiv:2508.02157](https://arxiv.org/abs/2508.02157) · [代码](https://github.com/Fischer-Tom/unified-detection-and-pose-estimation) · 📚 被引 0
- **作者**: Tom Fischer, Xiaojie Zhang, Eddy Ilg
- **🏷️ 机构**: Saarland University, University of Technology Nuremberg
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recognizing objects in images is a fundamental problem in computer vision. Although detecting objects in 2D images is common, many applications require determining their pose in 3D space. Traditional category-level methods rely on RGB-D inputs, which may not always be available, or employ two-stage approaches that use separate models and representations for detection and pose estimation. For the first time, we introduce a unified model that integrates detection and pose estimation into a single framework for RGB images by leveraging neural mesh models with learned features and multi-model RANSAC. Our approach achieves state-of-the-art results for RGB category-level pose estimation on REAL275, improving on the current state-of-the-art by 22.9% averaged across all scale-agnostic metrics. Finally, we demonstrate that our unified method exhibits greater robustness compared to single-stage baselines. Our code and models are available at https://github.com/Fischer-Tom/unified-detection-and-pose-estimation.

</details>

### Beyond RGB: Adaptive Parallel Processing for RAW Object Detection.
- **链接**: [arXiv:2503.13163](https://arxiv.org/abs/2503.13163) · 📚 被引 0
- **作者**: Shani Gamrian, Hila Barel, Feiran Li, Masakazu Yoshimura, Daisuke Iso
- **🏷️ 机构**: Sony Research, Sony Group Corporation
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection models are typically applied to standard RGB images processed through Image Signal Processing (ISP) pipelines, which are designed to enhance sensor-captured RAW images for human vision. However, these ISP functions can lead to a loss of critical information that may be essential in optimizing for computer vision tasks, such as object detection. In this work, we introduce Raw Adaptation Module (RAM), a module designed to replace the traditional ISP, with parameters optimized specifically for RAW object detection. Inspired by the parallel processing mechanisms of the human visual system, RAM departs from existing learned ISP methods by applying multiple ISP functions in parallel rather than sequentially, allowing for a more comprehensive capture of image features. These processed representations are then fused in a specialized module, which dynamically integrates and optimizes the information for the target task. This novel approach not only leverages the full potential of RAW sensor data but also enables task-specific pre-processing, resulting in superior object detection performance. Our approach outperforms RGB-based methods and achieves state-of-the-art results across diverse RAW image datasets under varying lighting conditions and dynamic ranges.

</details>

### Dark-ISP: Enhancing RAW Image Processing for Low-Light Object Detection.
- **链接**: [arXiv:2509.09183](https://arxiv.org/abs/2509.09183) · 📚 被引 4
- **作者**: Jiasheng Guo, Xin Gao, Yuxiang Yan, Guanghao Li, Jian Pu
- **🏷️ 机构**: Institute of Science and Technology for Brain-inspired Intelligence, Fudan University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Low-light Object detection is crucial for many real-world applications but remains challenging due to degraded image quality. While recent studies have shown that RAW images offer superior potential over RGB images, existing approaches either use RAW-RGB images with information loss or employ complex frameworks. To address these, we propose a lightweight and self-adaptive Image Signal Processing (ISP) plugin, Dark-ISP, which directly processes Bayer RAW images in dark environments, enabling seamless end-to-end training for object detection. Our key innovations are: (1) We deconstruct conventional ISP pipelines into sequential linear (sensor calibration) and nonlinear (tone mapping) sub-modules, recasting them as differentiable components optimized through task-driven losses. Each module is equipped with content-aware adaptability and physics-informed priors, enabling automatic RAW-to-RGB conversion aligned with detection objectives. (2) By exploiting the ISP pipeline's intrinsic cascade structure, we devise a Self-Boost mechanism that facilitates cooperation between sub-modules. Through extensive experiments on three RAW image datasets, we demonstrate that our method outperforms state-of-the-art RGB- and RAW-based detection approaches, achieving superior results with minimal parameters in challenging low-light environments.

</details>

### DoppDrive: Doppler-Driven Temporal Aggregation for Improved Radar Object Detection.
- **链接**: [arXiv:2508.12330](https://arxiv.org/abs/2508.12330) · 📚 被引 2
- **作者**: Yuval Haitman, Oded Bialer
- **🏷️ 机构**: General Motors, Technical Center Israel
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Radar-based object detection is essential for autonomous driving due to radar's long detection range. However, the sparsity of radar point clouds, especially at long range, poses challenges for accurate detection. Existing methods increase point density through temporal aggregation with ego-motion compensation, but this approach introduces scatter from dynamic objects, degrading detection performance. We propose DoppDrive, a novel Doppler-Driven temporal aggregation method that enhances radar point cloud density while minimizing scatter. Points from previous frames are shifted radially according to their dynamic Doppler component to eliminate radial scatter, with each point assigned a unique aggregation duration based on its Doppler and angle to minimize tangential scatter. DoppDrive is a point cloud density enhancement step applied before detection, compatible with any detector, and we demonstrate that it significantly improves object detection performance across various detectors and datasets.

</details>

### Dual-Rate Dynamic Teacher for Source-Free Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00200) · 📚 被引 2
- **作者**: Qi He, Xiao Wu, Jun-Yan He, Shuai Li
- **🏷️ 机构**: Southwest Jiaotong University,China, Meituan Inc.,China, The Hong Kong Polytechnic University,China
- **会议**: ICCV 2025

### OpenRSD: Towards Open-Prompts for Object Detection in Remote Sensing Images.
- **链接**: [arXiv:2503.06146](https://arxiv.org/abs/2503.06146) · 📚 被引 3
- **作者**: Ziyue Huang, Yongchao Feng, Ziqi Liu, Shuai Yang, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Remote sensing object detection has made significant progress, but most studies still focus on closed-set detection, limiting generalization across diverse datasets. Open-vocabulary object detection (OVD) provides a solution by leveraging multimodal associations between text prompts and visual features. However, existing OVD methods for remote sensing (RS) images are constrained by small-scale datasets and fail to address the unique challenges of remote sensing interpretation, include oriented object detection and the need for both high precision and real-time performance in diverse scenarios. To tackle these challenges, we propose OpenRSD, a universal open-prompt RS object detection framework. OpenRSD supports multimodal prompts and integrates multi-task detection heads to balance accuracy and real-time requirements. Additionally, we design a multi-stage training pipeline to enhance the generalization of model. Evaluated on seven public datasets, OpenRSD demonstrates superior performance in oriented and horizontal bounding box detection, with real-time inference capabilities suitable for large-scale RS image analysis. Compared to YOLO-World, OpenRSD exhibits an 8.7\% higher average precision and achieves an inference speed of 20.8 FPS. Codes and models will be released.

</details>

### Diffusion-Based Source-Biased Model for Single Domain Generalized Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00152) · 📚 被引 2
- **作者**: Han Jiang, Wenfei Yang, Tianzhu Zhang, Yongdong Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2025

### Power of Cooperative Supervision: Multiple Teachers Framework for Advanced 3D Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00657) · 📚 被引 1
- **作者**: Jin-Hee Lee, Jae-Keun Lee, Jeseok Kim, Kwon Soon
- **🏷️ 机构**: DGIST,Daegu,Republic of Korea
- **会议**: ICCV 2025

### Task-Specific Zero-Shot Quantization-Aware Training for Object Detection.
- **链接**: [arXiv:2507.16782](https://arxiv.org/abs/2507.16782) · [代码](https://github.com/DFQ-Dojo/dfq-toolkit) · 📚 被引 2
- **作者**: Changhao Li, Xinrui Chen, Ji Wang, Kang Zhao, Jianfei Chen
- **🏷️ 机构**: School of Computational Science and Engineering, Georgia Institute of Technology,Atlanta,USA, Shenzhen International Graduate School, Tsinghua University,China, School of Software, Tsinghua University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Quantization is a key technique to reduce network size and computational complexity by representing the network parameters with a lower precision. Traditional quantization methods rely on access to original training data, which is often restricted due to privacy concerns or security challenges. Zero-shot Quantization (ZSQ) addresses this by using synthetic data generated from pre-trained models, eliminating the need for real training data. Recently, ZSQ has been extended to object detection. However, existing methods use unlabeled task-agnostic synthetic images that lack the specific information required for object detection, leading to suboptimal performance. In this paper, we propose a novel task-specific ZSQ framework for object detection networks, which consists of two main stages. First, we introduce a bounding box and category sampling strategy to synthesize a task-specific calibration set from the pre-trained network, reconstructing object locations, sizes, and category distributions without any prior knowledge. Second, we integrate task-specific training into the knowledge distillation process to restore the performance of quantized detection networks. Extensive experiments conducted on the MS-COCO and Pascal VOC datasets demonstrate the efficiency and state-of-the-art performance of our method. Our code is publicly available at: https://github.com/DFQ-Dojo/dfq-toolkit .

</details>

### Benefit from Seen: Enhancing Open-Vocabulary Object Detection by Bridging Visual and Textual Co-Occurrence Knowledge.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02053)
- **作者**: Yanqi Li, Jianwei Niu, Tao Ren
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Continual Adaptation: Environment-Conditional Parameter Generation for Object Detection in Dynamic Scenarios.
- **链接**: [arXiv:2506.24063](https://arxiv.org/abs/2506.24063) · 📚 被引 0
- **作者**: Deng Li, Aming Wu, Yang Li, Yaowei Wang, Yahong Han
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University,Tianjin,China, School of Computer Science and Information Engineering, Hefei University of Technology,Hefei,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In practice, environments constantly change over time and space, posing significant challenges for object detectors trained based on a closed-set assumption, i.e., training and test data share the same distribution. To this end, continual test-time adaptation has attracted much attention, aiming to improve detectors' generalization by fine-tuning a few specific parameters, e.g., BatchNorm layers. However, based on a small number of test images, fine-tuning certain parameters may affect the representation ability of other fixed parameters, leading to performance degradation. Instead, we explore a new mechanism, i.e., converting the fine-tuning process to a specific-parameter generation. Particularly, we first design a dual-path LoRA-based domain-aware adapter that disentangles features into domain-invariant and domain-specific components, enabling efficient adaptation. Additionally, a conditional diffusion-based parameter generation mechanism is presented to synthesize the adapter's parameters based on the current environment, preventing the optimization from getting stuck in local optima. Finally, we propose a class-centered optimal transport alignment method to mitigate catastrophic forgetting. Extensive experiments conducted on various continuous domain adaptive object detection tasks demonstrate the effectiveness. Meanwhile, visualization results show that the representation extracted by the generated parameters can capture more object-related information and strengthen the generalization ability.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Oriented Object Detection (OOD) has received increased attention in the past years, being a suitable solution for detecting elongated objects in remote sensing analysis. In particular, using regression loss functions based on Gaussian distributions has become attractive since they yield simple and differentiable terms. However, existing solutions are still based on regression heads that produce Oriented Bounding Boxes (OBBs), and the known problem of angular boundary discontinuity persists. In this work, we propose a regression head for OOD that directly produces Gaussian distributions based on the Cholesky matrix decomposition. The proposed head, named GauCho, theoretically mitigates the boundary discontinuity problem and is fully compatible with recent Gaussian-based regression loss functions. Furthermore, we advocate using Oriented Ellipses (OEs) to represent oriented objects, which relates to GauCho through a bijective function and alleviates the encoding ambiguity problem for circular objects. Our experimental results show that GauCho can be a viable alternative to the traditional OBB head, achieving results comparable to or better than state-of-the-art detectors for the challenging dataset DOTA

</details>

> Object detection plays a crucial role in many security-sensitive applications. However, several recent studies have shown that object detectors can be easily fooled by physically realizable attacks, \eg, adversarial patches and recent adversarial textures, which pose realistic and urgent threats. Adversarial Training (AT) has been recognized as the most effective defense against adversarial attacks. While AT has been extensively studied in the $l_\infty$ attack settings on classification models, AT against physically realizable attacks on object detectors has received limited exploration. Early attempts are only performed to defend against adversarial patches, leaving AT against a wider range of physically realizable attacks under-explored. In this work, we consider defending against various physically realizable attacks with a unified AT method. We propose PBCAT, a novel Patch-Based Composite Adversarial Training strategy. PBCAT optimizes the model by incorporating the combination of small-area gradient-guided adversarial patches and imperceptible global adversarial perturbations covering the entire image. With these designs, PBCAT has the potential to defend against not only adversarial patches but also unseen physically realizable attacks such as adversarial textures. Extensive experiments in multiple settings demonstrated that PBCAT significantly improved robustness against various physically realizable attacks over state-of-the-art defense methods. Notably, it improved the detection accuracy by 29.7\% over previous defense methods under one recent adversarial texture attack.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce SearchDet, a training-free long-tail object detection framework that significantly enhances open-vocabulary object detection performance. SearchDet retrieves a set of positive and negative images of an object to ground, embeds these images, and computes an input image-weighted query which is used to detect the desired concept in the image. Our proposed method is simple and training-free, yet achieves over 48.7% mAP improvement on ODinW and 59.1% mAP improvement on LVIS compared to state-of-the-art models such as GroundingDINO. We further show that our approach of basing object detection on a set of Web-retrieved exemplars is stable with respect to variations in the exemplars, suggesting a path towards eliminating costly data annotation and training procedures.

</details>

### LLM-Assisted Semantic Guidance for Sparsely Annotated Remote Sensing Object Detection.
- **链接**: [arXiv:2509.16970](https://arxiv.org/abs/2509.16970) · 📚 被引 0
- **作者**: Wei Liao, Chunyan Xu, Chenxu Wang, Zhen Cui
- **🏷️ 机构**: Nanjing University of Science and Technology,Nanjing,Jiangsu,China, Beijing Normal University,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Remote sensing image object detection (RSIOD) aims to identify and locate specific objects within satellite or aerial imagery. However, there is a scarcity of labeled data in current RSIOD datasets, which significantly limits the performance of current detection algorithms. Although existing techniques, e.g., data augmentation and semi-supervised learning, can mitigate this scarcity issue to some extent, they are heavily dependent on high-quality labeled data and perform worse in rare object classes. To address this issue, this paper proposes a layout-controllable diffusion generative model (i.e. AeroGen) tailored for RSIOD. To our knowledge, AeroGen is the first model to simultaneously support horizontal and rotated bounding box condition generation, thus enabling the generation of high-quality synthetic images that meet specific layout and object category requirements. Additionally, we propose an end-to-end data augmentation framework that integrates a diversity-conditioned generator and a filtering mechanism to enhance both the diversity and quality of generated data. Experimental results demonstrate that the synthetic data produced by our method are of high quality and diversity. Furthermore, the synthetic RSIOD data can significantly improve the detection performance of existing RSIOD models, i.e., the mAP metrics on DIOR, DIOR-R, and HRSC datasets are improved by 3.7%, 4.3%, and 2.43%, respectively. The code is available at https://github.com/Sonettoo/AeroGen.

</details>

### Improving SAM for Camouflaged Object Detection via Dual Stream Adapters.
- **链接**: [arXiv:2503.06042](https://arxiv.org/abs/2503.06042) · 📚 被引 1
- **作者**: Jiaming Liu, Linghe Kong, Guihai Chen
- **🏷️ 机构**: School of Computer Science, Shanghai Jiao Tong University,Shanghai,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing co-salient object detection (CoSOD) methods generally employ a three-stage architecture (i.e., encoding, consensus extraction & dispersion, and prediction) along with a typical full fine-tuning paradigm. Although they yield certain benefits, they exhibit two notable limitations: 1) This architecture relies on encoded features to facilitate consensus extraction, but the meticulously extracted consensus does not provide timely guidance to the encoding stage. 2) This paradigm involves globally updating all parameters of the model, which is parameter-inefficient and hinders the effective representation of knowledge within the foundation model for this task. Therefore, in this paper, we propose an interaction-effective and parameter-efficient concise architecture for the CoSOD task, addressing two key limitations. It introduces, for the first time, a parameter-efficient prompt tuning paradigm and seamlessly embeds consensus into the prompts to formulate task-specific Visual Consensus Prompts (VCP). Our VCP aims to induce the frozen foundation model to perform better on CoSOD tasks by formulating task-specific visual consensus prompts with minimized tunable parameters. Concretely, the primary insight of the purposeful Consensus Prompt Generator (CPG) is to enforce limited tunable parameters to focus on co-salient representations and generate consensus prompts. The formulated Consensus Prompt Disperser (CPD) leverages consensus prompts to form task-specific visual consensus prompts, thereby arousing the powerful potential of pre-trained models in addressing CoSOD tasks. Extensive experiments demonstrate that our concise VCP outperforms 13 cutting-edge full fine-tuning models, achieving the new state of the art (with 6.8% improvement in F_m metrics on the most challenging CoCA dataset). Source code has been available at https://github.com/WJ-CV/VCP.

</details>

### Gradient Decomposition and Alignment for Incremental Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00427) · 📚 被引 3
- **作者**: Wenlong Luo, Shizhou Zhang, De Cheng, Yinghui Xing, Guoqiang Liang, Peng Wang et al.
- **🏷️ 机构**: Northwestern Polytechnical University,China, Xidian University,China
- **会议**: ICCV 2025

### DuET: Dual Incremental Object Detection via Exemplar-Free Task Arithmetic.
- **链接**: [arXiv:2506.21260](https://arxiv.org/abs/2506.21260) · 📚 被引 0
- **作者**: Munish Monga, Vishal M. Chudasama, Pankaj Wasnik, Biplab Banerjee
- **🏷️ 机构**: Sony Research,India, Indian Institute of Technology,Bombay
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world object detection systems, such as those in autonomous driving and surveillance, must continuously learn new object categories and simultaneously adapt to changing environmental conditions. Existing approaches, Class Incremental Object Detection (CIOD) and Domain Incremental Object Detection (DIOD) only address one aspect of this challenge. CIOD struggles in unseen domains, while DIOD suffers from catastrophic forgetting when learning new classes, limiting their real-world applicability. To overcome these limitations, we introduce Dual Incremental Object Detection (DuIOD), a more practical setting that simultaneously handles class and domain shifts in an exemplar-free manner. We propose DuET, a Task Arithmetic-based model merging framework that enables stable incremental learning while mitigating sign conflicts through a novel Directional Consistency Loss. Unlike prior methods, DuET is detector-agnostic, allowing models like YOLO11 and RT-DETR to function as real-time incremental object detectors. To comprehensively evaluate both retention and adaptation, we introduce the Retention-Adaptability Index (RAI), which combines the Average Retention Index (Avg RI) for catastrophic forgetting and the Average Generalization Index for domain adaptability into a common ground. Extensive experiments on the Pascal Series and Diverse Weather Series demonstrate DuET's effectiveness, achieving a +13.12% RAI improvement while preserving 89.3% Avg RI on the Pascal Series (4 tasks), as well as a +11.39% RAI improvement with 88.57% Avg RI on the Diverse Weather Series (3 tasks), outperforming existing methods.

</details>

### SFUOD: Source-Free Unknown Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00334)
- **作者**: Keon-Hee Park, Seun-An Choe, Gyeong-Moon Park
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### DM-EFS: Dynamically Multiplexed Expanded Features Set form for Robust and Efficient Small Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02278) · 📚 被引 0
- **作者**: Aashish Sharma
- **🏷️ 机构**: KLASS Engineering and Solutions,Singapore
- **会议**: ICCV 2025

### DiffRefine: Diffusion-Based Proposal Specific Point Cloud Densification for Cross-Domain Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00465) · 📚 被引 0
- **作者**: Sangyun Shin, Yuhang He, Xinyu Hou, Samuel Hodgson, Andrew Markham, Niki Trigoni
- **🏷️ 机构**: University of Oxford,Department of Computer Science,United Kingdom, Microsoft Research
- **会议**: ICCV 2025

### Dual Domain Control via Active Learning for Remote Sensing Domain Incremental Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00363) · 📚 被引 1
- **作者**: Jiachen Sun, De Cheng, Xi Yang, Nannan Wang
- **🏷️ 机构**: School of Telecommunications Engineering, Xidian University,State Key Laboratory of Integrated Services Networks,Xi&#x0027;an,China,710071
- **会议**: ICCV 2025

### Uncertainty-Aware Gradient Stabilization for Small Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00787) · 📚 被引 5
- **作者**: Huixin Sun, Yanjing Li, Linlin Yang, Xianbin Cao, Baochang Zhang
- **🏷️ 机构**: School of Electronic Information Engineering, Beihang University, CUC,State Key Laboratory of Media Convergence and Communication, School of Artificial Intelligence, Beihang University
- **会议**: ICCV 2025

### VISO: Accelerating In-Orbit Object Detection with Language-Guided Mask Learning and Sparse Inference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02163) · 📚 被引 0
- **作者**: Meiqi Wang, Han Qiu
- **🏷️ 机构**: Tsinghua University
- **会议**: ICCV 2025

### Measuring the Impact of Rotation Equivariance on Aerial Object Detection.
- **链接**: [arXiv:2507.09896](https://arxiv.org/abs/2507.09896) · 📚 被引 2
- **作者**: Xiuyu Wu, Xinhao Wang, Xiubin Zhu, Lan Yang, Jiyuan Liu, Xingchen Hu
- **🏷️ 机构**: Xidian University, National University of Defense Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the arbitrary orientation of objects in aerial images, rotation equivariance is a critical property for aerial object detectors. However, recent studies on rotation-equivariant aerial object detection remain scarce. Most detectors rely on data augmentation to enable models to learn approximately rotation-equivariant features. A few detectors have constructed rotation-equivariant networks, but due to the breaking of strict rotation equivariance by typical downsampling processes, these networks only achieve approximately rotation-equivariant backbones. Whether strict rotation equivariance is necessary for aerial image object detection remains an open question. In this paper, we implement a strictly rotation-equivariant backbone and neck network with a more advanced network structure and compare it with approximately rotation-equivariant networks to quantitatively measure the impact of rotation equivariance on the performance of aerial image detectors. Additionally, leveraging the inherently grouped nature of rotation-equivariant features, we propose a multi-branch head network that reduces the parameter count while improving detection accuracy. Based on the aforementioned improvements, this study proposes the Multi-branch head rotation-equivariant single-stage Detector (MessDet), which achieves state-of-the-art performance on the challenging aerial image datasets DOTA-v1.0, DOTA-v1.5 and DIOR-R with an exceptionally low parameter count.

</details>

### Visual Textualization for Image Prompted Object Detection.
- **链接**: [arXiv:2506.23785](https://arxiv.org/abs/2506.23785) · [代码](https://github.com/WitGotFlg/VisTex-OVLM) · 📚 被引 0
- **作者**: Yongjian Wu, Yang Zhou, Jiya Saiyin, Bingzheng Wei, Yan Xu
- **🏷️ 机构**: School of Biological Science and Medical Engineering, Beihang University, ByteDance Inc.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose VisTex-OVLM, a novel image prompted object detection method that introduces visual textualization -- a process that projects a few visual exemplars into the text feature space to enhance Object-level Vision-Language Models' (OVLMs) capability in detecting rare categories that are difficult to describe textually and nearly absent from their pre-training data, while preserving their pre-trained object-text alignment. Specifically, VisTex-OVLM leverages multi-scale textualizing blocks and a multi-stage fusion strategy to integrate visual information from visual exemplars, generating textualized visual tokens that effectively guide OVLMs alongside text prompts. Unlike previous methods, our method maintains the original architecture of OVLM, maintaining its generalization capabilities while enhancing performance in few-shot settings. VisTex-OVLM demonstrates superior performance across open-set datasets which have minimal overlap with OVLM's pre-training data and achieves state-of-the-art results on few-shot benchmarks PASCAL VOC and MSCOCO. The code will be released at https://github.com/WitGotFlg/VisTex-OVLM.

</details>

### Adversarial Attention Perturbations for Large Object Detection Transformers.
- **链接**: [arXiv:2508.02987](https://arxiv.org/abs/2508.02987) · [代码](https://github.com/zacharyyahn/AFOG) · 📚 被引 1
- **作者**: Zachary Yahn, Selim Furkan Tekin, Fatih Ilhan, Sihao Hu, Tiansheng Huang, Yichang Xu et al.
- **🏷️ 机构**: Georgia Institute of Technology,Atlanta,GA, Georgia Tech Research Institute,Atlanta,USA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial perturbations are useful tools for exposing vulnerabilities in neural networks. Existing adversarial perturbation methods for object detection are either limited to attacking CNN-based detectors or weak against transformer-based detectors. This paper presents an Attention-Focused Offensive Gradient (AFOG) attack against object detection transformers. By design, AFOG is neural-architecture agnostic and effective for attacking both large transformer-based object detectors and conventional CNN-based detectors with a unified adversarial attention framework. This paper makes three original contributions. First, AFOG utilizes a learnable attention mechanism that focuses perturbations on vulnerable image regions in multi-box detection tasks, increasing performance over non-attention baselines by up to 30.6%. Second, AFOG's attack loss is formulated by integrating two types of feature loss through learnable attention updates with iterative injection of adversarial perturbations. Finally, AFOG is an efficient and stealthy adversarial perturbation method. It probes the weak spots of detection transformers by adding strategically generated and visually imperceptible perturbations which can cause well-trained object detection models to fail. Extensive experiments conducted with twelve large detection transformers on COCO demonstrate the efficacy of AFOG. Our empirical results also show that AFOG outperforms existing attacks on transformer-based and CNN-based object detectors by up to 83% with superior speed and imperceptibility. Code is available at https://github.com/zacharyyahn/AFOG.

</details>

### 3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00697)
- **作者**: Yung-Hsu Yang, Luigi Piccinelli, Mattia Segù, Siyuan Li, Rui Huang, Yuqian Fu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### ESCNet: Edge-Semantic Collaborative Network for Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01865) · 📚 被引 10
- **作者**: Sheng Ye, Xin Chen, Yan Zhang, Xianming Lin, Liujuan Cao
- **🏷️ 机构**: Ministry of Education of China, Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing,P.R. China,361005
- **会议**: ICCV 2025

### Automated Model Evaluation for Object Detection Via Prediction Consistency and Reliability.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01838) · 📚 被引 1
- **作者**: Seungju Yoo, Hyuk Kwon, Joong-Won Hwang, Kibok Lee
- **🏷️ 机构**: Yonsei University, ETRI
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cooperative perception can increase the view field and decrease the occlusion of an ego vehicle, hence improving the perception performance and safety of autonomous driving. Despite the success of previous works on cooperative object detection, they mostly operate on dense Bird's Eye View (BEV) feature maps, which are computationally demanding and can hardly be extended to long-range detection problems. More efficient fully sparse frameworks are rarely explored. In this work, we design a fully sparse framework, SparseAlign, with three key features: an enhanced sparse 3D backbone, a query-based temporal context learning module, and a robust detection head specially tailored for sparse features. Extensive experimental results on both OPV2V and DairV2X datasets show that our framework, despite its sparsity, outperforms the state of the art with less communication bandwidth requirements. In addition, experiments on the OPV2Vt and DairV2Xt datasets for time-aligned cooperative object detection also show a significant performance gain compared to the baseline works.

</details>

### Revisiting Generative Replay for Class Incremental Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Revisiting_Generative_Replay_for_Class_Incremental_Object_Detection_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Shizhou Zhang, Xueqiang Lv, Yinghui Xing, Qirui Wu, Di Xu, Yanning Zhang
- **🏷️ 机构**: Northwestern Polytechnical University, Huawei Cloud Computing Technologies Co., Ltd
- **会议**: CVPR 2025

### Style Evolving along Chain-of-Thought for Unknown-Domain Object Detection.
- **链接**: [arXiv:2503.09968](https://arxiv.org/abs/2503.09968) · 📚 被引 1
- **作者**: Zihao Zhang, Aming Wu, Yahong Han
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing,Tianjin,China, Xidian University,School of Electronic Engineering,Xi&#x2019;an,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, a task of Single-Domain Generalized Object Detection (Single-DGOD) is proposed, aiming to generalize a detector to multiple unknown domains never seen before during training. Due to the unavailability of target-domain data, some methods leverage the multimodal capabilities of vision-language models, using textual prompts to estimate cross-domain information, enhancing the model's generalization capability. These methods typically use a single textual prompt, often referred to as the one-step prompt method. However, when dealing with complex styles such as the combination of rain and night, we observe that the performance of the one-step prompt method tends to be relatively weak. The reason may be that many scenes incorporate not just a single style but a combination of multiple styles. The one-step prompt method may not effectively synthesize combined information involving various styles. To address this limitation, we propose a new method, i.e., Style Evolving along Chain-of-Thought, which aims to progressively integrate and expand style information along the chain of thought, enabling the continual evolution of styles. Specifically, by progressively refining style descriptions and guiding the diverse evolution of styles, this approach enables more accurate simulation of various style characteristics and helps the model gradually learn and adapt to subtle differences between styles. Additionally, it exposes the model to a broader range of style features with different data distributions, thereby enhancing its generalization capability in unseen domains. The significant performance gains over five adverse-weather scenarios and the Real to Art benchmark demonstrate the superiorities of our method.

</details>

### BOOTPLACE: Bootstrapped Object Placement with Detection Transformers.
- **链接**: [arXiv:2503.21991](https://arxiv.org/abs/2503.21991) · 📚 被引 1
- **作者**: Hang Zhou, Xinxin Zuo, Rui Ma, Li Cheng
- **🏷️ 机构**: University of Alberta, Concordia University, Jilin University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we tackle the copy-paste image-to-image composition problem with a focus on object placement learning. Prior methods have leveraged generative models to reduce the reliance for dense supervision. However, this often limits their capacity to model complex data distributions. Alternatively, transformer networks with a sparse contrastive loss have been explored, but their over-relaxed regularization often leads to imprecise object placement. We introduce BOOTPLACE, a novel paradigm that formulates object placement as a placement-by-detection problem. Our approach begins by identifying suitable regions of interest for object placement. This is achieved by training a specialized detection transformer on object-subtracted backgrounds, enhanced with multi-object supervisions. It then semantically associates each target compositing object with detected regions based on their complementary characteristics. Through a boostrapped training approach applied to randomly object-subtracted images, our model enforces meaningful placements through extensive paired data augmentation. Experimental results on established benchmarks demonstrate BOOTPLACE's superior performance in object repositioning, markedly surpassing state-of-the-art baselines on Cityscapes and OPA datasets with notable improvements in IOU scores. Additional ablation studies further showcase the compositionality and generalizability of our approach, supported by user study evaluations.

</details>

## 跨领域论文（完整笔记在其他领域）

- Fusion Meets Diverse Conditions: A High-Diversity Benchmark and Baseline for UAV-Based Multimodal Object Detection with Condition Cues. → [multimodal](../multimodal/Guideline%202025.md)
- OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202025.md)
- RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion. → [3d-detection](../3d-detection/Guideline%202025.md)
- Robust 3D Object Detection Using Probabilistic Point Clouds From Single-Photon Lidars. → [3d-detection](../3d-detection/Guideline%202025.md)
- OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations. → [3d-detection](../3d-detection/Guideline%202025.md)
- Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts. → [3d-detection](../3d-detection/Guideline%202025.md)
- GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-Based Transformer. → [3d-detection](../3d-detection/Guideline%202025.md)
- Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- MemDistill: Distilling LiDAR Knowledge into Memory for Camera-Only 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- EVT: Efficient View Transformation for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- LMM-Det: Make Large Multimodal Models Excel in Object Detection. → [multimodal](../multimodal/Guideline%202025.md)
- Perspective-Invariant 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge. → [3d-detection](../3d-detection/Guideline%202025.md)
- ForeSight: Multi-View Streaming Joint Object Detection and Trajectory Forecasting. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers. → [3d-detection](../3d-detection/Guideline%202025.md)
- Height-Fidelity Dense Global Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Motal: Unsupervised 3D Object Detection by Modality and Task-Specific Knowledge Transfer. → [3d-detection](../3d-detection/Guideline%202025.md)
- Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning. → [3d-detection](../3d-detection/Guideline%202025.md)
- Boosting Multi-View Indoor 3D Object Detection Via Adaptive 3D Volume Construction. → [3d-detection](../3d-detection/Guideline%202025.md)
- Harnessing Uncertainty-Aware Bounding Boxes for Unsupervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Rethinking Multi-Modal Object Detection From the Perspective of Mono-Modality Feature Learning. → [multimodal](../multimodal/Guideline%202025.md)
- CVFusion: Cross-View Fusion of 4D Radar and Camera for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
