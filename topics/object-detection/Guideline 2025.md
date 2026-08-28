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

> Small object detection (SOD) in anti-UAV task is a challenging problem due to the small size of UAVs and complex backgrounds. Traditional frame-based cameras struggle to detect small objects in complex environments due to their low frame rates, limited dynamic range, and data redundancy. Event cameras, with microsecond temporal resolution and high dynamic range, provide a more effective solution for SOD. However, existing event-based object detection datasets are limited in scale, feature large targets size, and lack diverse backgrounds, making them unsuitable for SOD benchmarks. In this paper, we introduce a Event-based Small object detection (EVSOD) dataset (namely EV-UAV), the first large-scale, highly diverse benchmark for anti-UAV tasks. It includes 147 sequences with over 2.3 million event-level annotations, featuring extremely small targets (averaging 6.8 $\times$ 5.4 pixels) and diverse scenarios such as urban clutter and extreme lighting conditions. Furthermore, based on the observation that small moving targets form continuous curves in spatiotemporal event point clouds, we propose Event based Sparse Segmentation Network (EV-SpSegNet), a novel baseline for event segmentation in point cloud space, along with a Spatiotemporal Correlation (STC) loss that leverages motion continuity to guide the network in retaining target events. Extensive experiments on the EV-UAV dataset demonstrate the superiority of our method and provide a benchmark for future research in EVSOD. The dataset and code are at https://github.com/ChenYichen9527/Ev-UAV.

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

### When Pixel Difference Patterns Meet ViT: PiDiViT for Few-Shot Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02253)
- **作者**: Hongliang Zhou, Yongxiang Liu, Canyu Mo, Weijie Li, Bowen Peng, Li Liu
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

### PBCAT: Patch-Based Composite Adversarial Training Against Physically Realizable Attacks on Object Detection.
- **链接**: [arXiv:2506.23581](https://arxiv.org/abs/2506.23581) · 📚 被引 0
- **作者**: Xiao Li, Yiming Zhu, Yifan Huang, Wei Zhang, Yingzhe He, Jie Shi et al.
- **🏷️ 机构**: BNRist, IDG/McGovern Institute for Brain Research, THBI, Tsinghua University,Department of Computer Science and Technology, Huawei Technologies
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection plays a crucial role in many security-sensitive applications. However, several recent studies have shown that object detectors can be easily fooled by physically realizable attacks, \eg, adversarial patches and recent adversarial textures, which pose realistic and urgent threats. Adversarial Training (AT) has been recognized as the most effective defense against adversarial attacks. While AT has been extensively studied in the $l_\infty$ attack settings on classification models, AT against physically realizable attacks on object detectors has received limited exploration. Early attempts are only performed to defend against adversarial patches, leaving AT against a wider range of physically realizable attacks under-explored. In this work, we consider defending against various physically realizable attacks with a unified AT method. We propose PBCAT, a novel Patch-Based Composite Adversarial Training strategy. PBCAT optimizes the model by incorporating the combination of small-area gradient-guided adversarial patches and imperceptible global adversarial perturbations covering the entire image. With these designs, PBCAT has the potential to defend against not only adversarial patches but also unseen physically realizable attacks such as adversarial textures. Extensive experiments in multiple settings demonstrated that PBCAT significantly improved robustness against various physically realizable attacks over state-of-the-art defense methods. Notably, it improved the detection accuracy by 29.7\% over previous defense methods under one recent adversarial texture attack.

</details>

### Gradient-Reweighted Adversarial Camouflage for Physical Object Detection Evasion.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01288) · 📚 被引 0
- **作者**: Jiawei Liang, Siyuan Liang, Tianrui Lou, Ming Zhang, Wenjin Li, Dunqiu Fan et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, Nanyang Technological University, National Key Laboratory of Science and Technology on Information System Security
- **会议**: ICCV 2025

### LLM-Assisted Semantic Guidance for Sparsely Annotated Remote Sensing Object Detection.
- **链接**: [arXiv:2509.16970](https://arxiv.org/abs/2509.16970) · 📚 被引 0
- **作者**: Wei Liao, Chunyan Xu, Chenxu Wang, Zhen Cui
- **🏷️ 机构**: Nanjing University of Science and Technology,Nanjing,Jiangsu,China, Beijing Normal University,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse annotation in remote sensing object detection poses significant challenges due to dense object distributions and category imbalances. Although existing Dense Pseudo-Label methods have demonstrated substantial potential in pseudo-labeling tasks, they remain constrained by selection ambiguities and inconsistencies in confidence estimation.In this paper, we introduce an LLM-assisted semantic guidance framework tailored for sparsely annotated remote sensing object detection, exploiting the advanced semantic reasoning capabilities of large language models (LLMs) to distill high-confidence pseudo-labels.By integrating LLM-generated semantic priors, we propose a Class-Aware Dense Pseudo-Label Assignment mechanism that adaptively assigns pseudo-labels for both unlabeled and sparsely labeled data, ensuring robust supervision across varying data distributions. Additionally, we develop an Adaptive Hard-Negative Reweighting Module to stabilize the supervised learning branch by mitigating the influence of confounding background information. Extensive experiments on DOTA and HRSC2016 demonstrate that the proposed method outperforms existing single-stage detector-based frameworks, significantly improving detection performance under sparse annotations.

</details>

### Improving SAM for Camouflaged Object Detection via Dual Stream Adapters.
- **链接**: [arXiv:2503.06042](https://arxiv.org/abs/2503.06042) · 📚 被引 1
- **作者**: Jiaming Liu, Linghe Kong, Guihai Chen
- **🏷️ 机构**: School of Computer Science, Shanghai Jiao Tong University,Shanghai,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Segment anything model (SAM) has shown impressive general-purpose segmentation performance on natural images, but its performance on camouflaged object detection (COD) is unsatisfactory. In this paper, we propose SAM-COD that performs camouflaged object detection for RGB-D inputs. While keeping the SAM architecture intact, dual stream adapters are expanded on the image encoder to learn potential complementary information from RGB images and depth images, and fine-tune the mask decoder and its depth replica to perform dual-stream mask prediction. In practice, the dual stream adapters are embedded into the attention block of the image encoder in a parallel manner to facilitate the refinement and correction of the two types of image embeddings. To mitigate channel discrepancies arising from dual stream embeddings that do not directly interact with each other, we augment the association of dual stream embeddings using bidirectional knowledge distillation including a model distiller and a modal distiller. In addition, to predict the masks for RGB and depth attention maps, we hybridize the two types of image embeddings which are jointly learned with the prompt embeddings to update the initial prompt, and then feed them into the mask decoders to synchronize the consistency of image embeddings and prompt embeddings. Experimental results on four COD benchmarks show that our SAM-COD achieves excellent detection performance gains over SAM and achieves state-of-the-art results with a given fine-tuning paradigm.

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

### ASGS: Single-Domain Generalizable Open-Set Object Detection via Adaptive Subgraph Searching.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01944)
- **作者**: Yuxuan Yuan, Luyao Tang, Yixin Chen, Chaoqi Chen, Yue Huang, Xinghao Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### UPRE: Zero-Shot Domain Adaptation for Object Detection via Unified Prompt and Representation Enhancement.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00055) · 📚 被引 2
- **作者**: Xiao Zhang, Fei Wei, Yong Wang, Wenda Zhao, Feiyi Li, Xiangxiang Chu
- **🏷️ 机构**: Dalian University of Technology, AMAP, Alibaba Group
- **会议**: ICCV 2025

### WaveMamba: Wavelet-Driven Mamba Fusion for RGB-Infrared Object Detection.
- **链接**: [arXiv:2507.18173](https://arxiv.org/abs/2507.18173) · 📚 被引 14
- **作者**: Haodong Zhu, Wenhao Dong, Linlin Yang, Hong Li, Yuguang Yang, Yangyang Ren et al.
- **🏷️ 机构**: Beihang University,China, Communication University of China,China
- **会议**: ICCV 2025

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
