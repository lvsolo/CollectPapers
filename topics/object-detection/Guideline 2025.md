# Object Detection — 2025 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 51 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MI-DETR: An Object Detection Model with Multi-time Inquiries Mechanism.
- **链接**: [arXiv:2503.01463](https://arxiv.org/abs/2503.01463) · 📚 被引 17
- **作者**: Zhixiong Nan, Xianghong Li, Jifeng Dai, Tao Xiang
- **🏷️ 机构**: Chongqing University,College of Computer Science,Chongqing,China, Tsinghua University,Department of Electronic Engineering,Beijing,China
- **会议**: CVPR 2025

### Roboflow100-VL: A Multi-Domain Object Detection Benchmark for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1013f8ff40a194f3f12a6bcc5221bb34-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Matvei Popov, Peter Robicheaux, Anish Madan, Isaac Robinson, Joseph Nelson, Deva Ramanan et al.
- **🏷️ 机构**: CMU
- **会议**: NeurIPS 2025

> Small object detection (SOD) in anti-UAV task is a challenging problem due to the small size of UAVs and complex backgrounds. Traditional frame-based cameras struggle to detect small objects in complex environments due to their low frame rates, limited dynamic range, and data redundancy. Event cameras, with microsecond temporal resolution and high dynamic range, provide a more effective solution for SOD. However, existing event-based object detection datasets are limited in scale, feature large targets size, and lack diverse backgrounds, making them unsuitable for SOD benchmarks. In this paper, we introduce a Event-based Small object detection (EVSOD) dataset (namely EV-UAV), the first large-scale, highly diverse benchmark for anti-UAV tasks. It includes 147 sequences with over 2.3 million event-level annotations, featuring extremely small targets (averaging 6.8 $\times$ 5.4 pixels) and diverse scenarios such as urban clutter and extreme lighting conditions. Furthermore, based on the observation that small moving targets form continuous curves in spatiotemporal event point clouds, we propose Event based Sparse Segmentation Network (EV-SpSegNet), a novel baseline for event segmentation in point cloud space, along with a Spatiotemporal Correlation (STC) loss that leverages motion continuity to guide the network in retaining target events. Extensive experiments on the EV-UAV dataset demonstrate the superiority of our method and provide a benchmark for future research in EVSOD. The dataset and code are at https://github.com/ChenYichen9527/Ev-UAV.

</details>

### Object Detection using Event Camera: A MoE Heat Conduction based Detector and A New Benchmark Dataset.
- **链接**: [arXiv:2412.06647](https://arxiv.org/abs/2412.06647) · [代码](https://github.com/Event-AHU/OpenEvDET) · 📚 被引 13
- **作者**: Xiao Wang, Yu Jin, Wentao Wu, Wei Zhang, Lin Zhu, Bo Jiang et al.
- **🏷️ 机构**: Anhui University,School of Computer Science and Technology,Hefei,China, Anhui University,School of Artificial Intelligence,Hefei,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection in event streams has emerged as a cutting-edge research area, demonstrating superior performance in low-light conditions, scenarios with motion blur, and rapid movements. Current detectors leverage spiking neural networks, Transformers, or convolutional neural networks as their core architectures, each with its own set of limitations including restricted performance, high computational overhead, or limited local receptive fields. This paper introduces a novel MoE (Mixture of Experts) heat conduction-based object detection algorithm that strikingly balances accuracy and computational efficiency. Initially, we employ a stem network for event data embedding, followed by processing through our innovative MoE-HCO blocks. Each block integrates various expert modules to mimic heat conduction within event streams. Subsequently, an IoU-based query selection module is utilized for efficient token extraction, which is then channeled into a detection head for the final object detection process. Furthermore, we are pleased to introduce EvDET200K, a novel benchmark dataset for event-based object detection. Captured with a high-definition Prophesee EVK4-HD event camera, this dataset encompasses 10 distinct categories, 200,000 bounding boxes, and 10,054 samples, each spanning 2 to 5 seconds. We also provide comprehensive results from over 15 state-of-the-art detectors, offering a solid foundation for future research and comparison. The source code of this paper will be released on: https://github.com/Event-AHU/OpenEvDET

</details>

### Open-World Objectness Modeling Unifies Novel Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Open-World_Objectness_Modeling_Unifies_Novel_Object_Detection_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Shan Zhang, Yao Ni, Jinhao Du, Yuan Xue, Philip Torr, Piotr Koniusz et al.
- **🏷️ 机构**: Australian Institute for Machine Learning, Australian National University, Peking University
- **会议**: CVPR 2025

### Test-Time Backdoor Detection for Object Detection Models.
- **链接**: [arXiv:2503.15293](https://arxiv.org/abs/2503.15293) · 📚 被引 3
- **作者**: Hangtao Zhang, Yichen Wang, Shihui Yan, Chenyu Zhu, Ziqi Zhou, Linshan Hou et al.
- **🏷️ 机构**: Huazhong University of Science and Technology,School of Cyber Science and Engineering, Huazhong University of Science and Technology,School of Software Engineering, Huazhong University of Science and Technology,School of Computer Science and Technology
- **会议**: CVPR 2025

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
- **链接**: [arXiv:2410.11774](https://arxiv.org/abs/2410.11774) · [代码](https://github.com/kostas1515/FRACAL) · 📚 被引 4
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
- **会议**: CVPR 2025

### Brain-Inspired Spiking Neural Networks for Energy-Efficient Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Brain-Inspired_Spiking_Neural_Networks_for_Energy-Efficient_Object_Detection_CVPR_2025_paper.html)
- **作者**: Ziqi Li, Tao Gao, Yisheng An, Ting Chen, Jing Zhang, Yuanbo Wen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Pseudo Visible Feature Fine-Grained Fusion for Thermal Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Pseudo_Visible_Feature_Fine-Grained_Fusion_for_Thermal_Object_Detection_CVPR_2025_paper.html) · 📚 被引 9
- **作者**: Ting Li, Mao Ye, Tianwen Wu, Nianxin Li, Shuaifeng Li, Song Tang et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, University of Shanghai for Science and Technology
- **会议**: CVPR 2025

### Towards RAW Object Detection in Diverse Conditions.
- **链接**: [arXiv:2411.15678](https://arxiv.org/abs/2411.15678) · [代码](https://github.com/lzyhha/AODRaw) · 📚 被引 6
- **作者**: Zhongyu Li, Xin Jin, Bo-Yuan Sun, Chun-Le Guo, Ming-Ming Cheng
- **🏷️ 机构**: VCIP, CS, Nankai University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing object detection methods often consider sRGB input, which was compressed from RAW data using ISP originally designed for visualization. However, such compression might lose crucial information for detection, especially under complex light and weather conditions. We introduce the AODRaw dataset, which offers 7,785 high-resolution real RAW images with 135,601 annotated instances spanning 62 categories, capturing a broad range of indoor and outdoor scenes under 9 distinct light and weather conditions. Based on AODRaw that supports RAW and sRGB object detection, we provide a comprehensive benchmark for evaluating current detection methods. We find that sRGB pre-training constrains the potential of RAW object detection due to the domain gap between sRGB and RAW, prompting us to directly pre-train on the RAW domain. However, it is harder for RAW pre-training to learn rich representations than sRGB pre-training due to the camera noise. To assist RAW pre-training, we distill the knowledge from an off-the-shelf model pre-trained on the sRGB domain. As a result, we achieve substantial improvements under diverse and adverse conditions without relying on extra pre-processing modules. Code and dataset are available at https://github.com/lzyhha/AODRaw.

</details>

### PointSR: Self-Regularized Point Supervision for Drone-View Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_PointSR_Self-Regularized_Point_Supervision_for_Drone-View_Object_Detection_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Weizhuo Li, Yue Xi, Wenjing Jia, Zehao Zhang, Fei Li, Xiangzeng Liu et al.
- **🏷️ 机构**: Guangzhou Institute of Technology, Xidian University,Guangzhou,China, Faculty of Engineering and IT, University of Technology Sydney,Sydney,Australia, Xidian University,School of Computer Science and Technology,Xi&#x2019;an,China
- **会议**: CVPR 2025

### GauCho: Gaussian Distributions with Cholesky Decomposition for Oriented Object Detection.
- **链接**: [arXiv:2502.01565](https://arxiv.org/abs/2502.01565) · 📚 被引 4
- **作者**: Jose Henrique Lima Marques, Jeffri Murrugarra-Llerena, Cláudio R. Jung
- **🏷️ 机构**: Federal University of Rio Grande do Sul, Stony Brook University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In practice, environments constantly change over time and space, posing significant challenges for object detectors trained based on a closed-set assumption, i.e., training and test data share the same distribution. To this end, continual test-time adaptation has attracted much attention, aiming to improve detectors' generalization by fine-tuning a few specific parameters, e.g., BatchNorm layers. However, based on a small number of test images, fine-tuning certain parameters may affect the representation ability of other fixed parameters, leading to performance degradation. Instead, we explore a new mechanism, i.e., converting the fine-tuning process to a specific-parameter generation. Particularly, we first design a dual-path LoRA-based domain-aware adapter that disentangles features into domain-invariant and domain-specific components, enabling efficient adaptation. Additionally, a conditional diffusion-based parameter generation mechanism is presented to synthesize the adapter's parameters based on the current environment, preventing the optimization from getting stuck in local optima. Finally, we propose a class-centered optimal transport alignment method to mitigate catastrophic forgetting. Extensive experiments conducted on various continuous domain adaptive object detection tasks demonstrate the effectiveness. Meanwhile, visualization results show that the representation extracted by the generated parameters can capture more object-related information and strengthen the generalization ability.

</details>

### Search and Detect: Training-Free Long Tail Object Detection via Web-Image Retrieval.
- **链接**: [arXiv:2409.18733](https://arxiv.org/abs/2409.18733) · 📚 被引 0
- **作者**: Mankeerat Sidhu, Hetarth Chopra, Ansel Blume, Jeonghwan Kim, Revanth Gangi Reddy, Heng Ji
- **🏷️ 机构**: University of Illinois Urbana Champaign,Urbana,USA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection plays a crucial role in many security-sensitive applications. However, several recent studies have shown that object detectors can be easily fooled by physically realizable attacks, \eg, adversarial patches and recent adversarial textures, which pose realistic and urgent threats. Adversarial Training (AT) has been recognized as the most effective defense against adversarial attacks. While AT has been extensively studied in the $l_\infty$ attack settings on classification models, AT against physically realizable attacks on object detectors has received limited exploration. Early attempts are only performed to defend against adversarial patches, leaving AT against a wider range of physically realizable attacks under-explored. In this work, we consider defending against various physically realizable attacks with a unified AT method. We propose PBCAT, a novel Patch-Based Composite Adversarial Training strategy. PBCAT optimizes the model by incorporating the combination of small-area gradient-guided adversarial patches and imperceptible global adversarial perturbations covering the entire image. With these designs, PBCAT has the potential to defend against not only adversarial patches but also unseen physically realizable attacks such as adversarial textures. Extensive experiments in multiple settings demonstrated that PBCAT significantly improved robustness against various physically realizable attacks over state-of-the-art defense methods. Notably, it improved the detection accuracy by 29.7\% over previous defense methods under one recent adversarial texture attack.

</details>

### SET: Spectral Enhancement for Tiny Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_SET_Spectral_Enhancement_for_Tiny_Object_Detection_CVPR_2025_paper.html) · 📚 被引 27
- **作者**: Huixin Sun, Runqi Wang, Yanjing Li, Linlin Yang, Shaohui Lin, Xianbin Cao et al.
- **🏷️ 机构**: Beihang University,School of Electronic Information Engineering,Beijing,China, Beijing Jiaotong University,School of Computer Science and Technology, Communication University of China,State Key Laboratory of Media Convergence and Communication,Beijing,China
- **会议**: CVPR 2025

### AeroGen: Enhancing Remote Sensing Object Detection with Diffusion-Driven Data Generation.
- **链接**: [arXiv:2411.15497](https://arxiv.org/abs/2411.15497) · [代码](https://github.com/Sonettoo/AeroGen) · 📚 被引 34
- **作者**: Datao Tang, Xiangyong Cao, Xuan Wu, Jialin Li, Jing Yao, Xueru Bai et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Computer Science and Technology,Xi&#x2019;an,China,710049, Chinese Academy of Sciences, Xidian University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse annotation in remote sensing object detection poses significant challenges due to dense object distributions and category imbalances. Although existing Dense Pseudo-Label methods have demonstrated substantial potential in pseudo-labeling tasks, they remain constrained by selection ambiguities and inconsistencies in confidence estimation.In this paper, we introduce an LLM-assisted semantic guidance framework tailored for sparsely annotated remote sensing object detection, exploiting the advanced semantic reasoning capabilities of large language models (LLMs) to distill high-confidence pseudo-labels.By integrating LLM-generated semantic priors, we propose a Class-Aware Dense Pseudo-Label Assignment mechanism that adaptively assigns pseudo-labels for both unlabeled and sparsely labeled data, ensuring robust supervision across varying data distributions. Additionally, we develop an Adaptive Hard-Negative Reweighting Module to stabilize the supervised learning branch by mitigating the influence of confounding background information. Extensive experiments on DOTA and HRSC2016 demonstrate that the proposed method outperforms existing single-stage detector-based frameworks, significantly improving detection performance under sparse annotations.

</details>

### SimLTD: Simple Supervised and Semi-Supervised Long-Tailed Object Detection.
- **链接**: [arXiv:2412.20047](https://arxiv.org/abs/2412.20047) · 📚 被引 6
- **作者**: Phi Vu Tran
- **🏷️ 机构**: LexisNexis Risk Solutions
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While modern visual recognition systems have made significant advancements, many continue to struggle with the open problem of learning from few exemplars. This paper focuses on the task of object detection in the setting where object classes follow a natural long-tailed distribution. Existing methods for long-tailed detection resort to external ImageNet labels to augment the low-shot training instances. However, such dependency on a large labeled database has limited utility in practical scenarios. We propose a versatile and scalable approach to leverage optional unlabeled images, which are easy to collect without the burden of human annotations. Our SimLTD framework is straightforward and intuitive, and consists of three simple steps: (1) pre-training on abundant head classes; (2) transfer learning on scarce tail classes; and (3) fine-tuning on a sampled set of both head and tail classes. Our approach can be viewed as an improved head-to-tail model transfer paradigm without the added complexities of meta-learning or knowledge distillation, as was required in past research. By harnessing supplementary unlabeled images, without extra image labels, SimLTD establishes new record results on the challenging LVIS v1 benchmark across both supervised and semi-supervised settings.

</details>

### Visual Consensus Prompting for Co-Salient Object Detection.
- **链接**: [arXiv:2504.14254](https://arxiv.org/abs/2504.14254) · [代码](https://github.com/WJ-CV/VCP) · 📚 被引 3
- **作者**: Jie Wang, Nana Yu, Zihao Zhang, Yahong Han
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Segment anything model (SAM) has shown impressive general-purpose segmentation performance on natural images, but its performance on camouflaged object detection (COD) is unsatisfactory. In this paper, we propose SAM-COD that performs camouflaged object detection for RGB-D inputs. While keeping the SAM architecture intact, dual stream adapters are expanded on the image encoder to learn potential complementary information from RGB images and depth images, and fine-tune the mask decoder and its depth replica to perform dual-stream mask prediction. In practice, the dual stream adapters are embedded into the attention block of the image encoder in a parallel manner to facilitate the refinement and correction of the two types of image embeddings. To mitigate channel discrepancies arising from dual stream embeddings that do not directly interact with each other, we augment the association of dual stream embeddings using bidirectional knowledge distillation including a model distiller and a modal distiller. In addition, to predict the masks for RGB and depth attention maps, we hybridize the two types of image embeddings which are jointly learned with the prompt embeddings to update the initial prompt, and then feed them into the mask decoders to synchronize the consistency of image embeddings and prompt embeddings. Experimental results on four COD benchmarks show that our SAM-COD achieves excellent detection performance gains over SAM and achieves state-of-the-art results with a given fine-tuning paradigm.

</details>

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
- **链接**: [arXiv:2506.07087](https://arxiv.org/abs/2506.07087) · 📚 被引 4
- **作者**: Weiqi Yan, Lvhai Chen, Huaijia Kou, Shengchuan Zhang, Yan Zhang, Liujuan Cao
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China,P.R. China,361005
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised Camoflaged Object Detection (UCOD) has gained attention since it doesn't need to rely on extensive pixel-level labels. Existing UCOD methods typically generate pseudo-labels using fixed strategies and train 1 x1 convolutional layers as a simple decoder, leading to low performance compared to fully-supervised methods. We emphasize two drawbacks in these approaches: 1). The model is prone to fitting incorrect knowledge due to the pseudo-label containing substantial noise. 2). The simple decoder fails to capture and learn the semantic features of camouflaged objects, especially for small-sized objects, due to the low-resolution pseudo-labels and severe confusion between foreground and background pixels. To this end, we propose a UCOD method with a teacher-student framework via Dynamic Pseudo-label Learning called UCOD-DPL, which contains an Adaptive Pseudo-label Module (APM), a Dual-Branch Adversarial (DBA) decoder, and a Look-Twice mechanism. The APM module adaptively combines pseudo-labels generated by fixed strategies and the teacher model to prevent the model from overfitting incorrect knowledge while preserving the ability for self-correction; the DBA decoder takes adversarial learning of different segmentation objectives, guides the model to overcome the foreground-background confusion of camouflaged objects, and the Look-Twice mechanism mimics the human tendency to zoom in on camouflaged objects and performs secondary refinement on small-sized objects. Extensive experiments show that our method demonstrates outstanding performance, even surpassing some existing fully supervised methods. The code is available now.

</details>

### SparseAlign: a Fully Sparse Framework for Cooperative Object Detection.
- **链接**: [arXiv:2503.12982](https://arxiv.org/abs/2503.12982) · 📚 被引 8
- **作者**: Yunshuang Yuan, Yan Xia, Daniel Cremers, Monika Sester
- **🏷️ 机构**: Leibniz University Hannover, Technical University of Munich
- **会议**: CVPR 2025

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

### R2Det: Exploring Relaxed Rotation Equivariance in 2D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=EUeNr3e8AV)
- **作者**: Zhiqiang Wu, Yingjie Liu, Hanlin Dong, Xuan Tang, Jian Yang, Bo Jin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

> Maritime object detection is essential for navigation safety, surveillance, and autonomous operations, yet constrained by two key challenges: the scarcity of annotated maritime data and poor generalization across various maritime attributes (e.g., object category, viewpoint, location, and imaging environment). To address these challenges, we propose Neptune-X, a data-centric generative-selection framework that enhances training effectiveness by leveraging synthetic data generation with task-aware sample selection. From the generation perspective, we develop X-to-Maritime, a multi-modality-conditioned generative model that synthesizes diverse and realistic maritime scenes. A key component is the Bidirectional Object-Water Attention module, which captures boundary interactions between objects and their aquatic surroundings to improve visual fidelity. To further improve downstream tasking performance, we propose Attribute-correlated Active Sampling, which dynamically selects synthetic samples based on their task relevance. To support robust benchmarking, we construct the Maritime Generation Dataset, the first dataset tailored for generative maritime learning, encompassing a wide range of semantic conditions. Extensive experiments demonstrate that our approach sets a new benchmark in maritime scene synthesis, significantly improving detection accuracy, particularly in challenging and previously underrepresented settings. The code is available at https://github.com/gy65896/Neptune-X.

</details>

### BOOTPLACE: Bootstrapped Object Placement with Detection Transformers.
- **链接**: [arXiv:2503.21991](https://arxiv.org/abs/2503.21991) · 📚 被引 1
- **作者**: Hang Zhou, Xinxin Zuo, Rui Ma, Li Cheng
- **🏷️ 机构**: University of Alberta, Concordia University, Jilin University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-Domain Few-Shot Object Detection (CD-FSOD) aims to detect novel objects with only a handful of labeled samples from previously unseen domains. While data augmentation and generative methods have shown promise in few-shot learning, their effectiveness for CD-FSOD remains unclear due to the need for both visual realism and domain alignment. Existing strategies, such as copy-paste augmentation and text-to-image generation, often fail to preserve the correct object category or produce backgrounds coherent with the target domain, making them non-trivial to apply directly to CD-FSOD. To address these challenges, we propose Domain-RAG, a training-free, retrieval-guided compositional image generation framework tailored for CD-FSOD. Domain-RAG consists of three stages: domain-aware background retrieval, domain-guided background generation, and foreground-background composition. Specifically, the input image is first decomposed into foreground and background regions. We then retrieve semantically and stylistically similar images to guide a generative model in synthesizing a new background, conditioned on both the original and retrieved contexts. Finally, the preserved foreground is composed with the newly generated domain-aligned background to form the generated image. Without requiring any additional supervision or training, Domain-RAG produces high-quality, domain-consistent samples across diverse tasks, including CD-FSOD, remote sensing FSOD, and camouflaged FSOD. Extensive experiments show consistent improvements over strong baselines and establish new state-of-the-art results. Codes will be released upon acceptance.

</details>

### Towards Single-Source Domain Generalized Object Detection via Causal Visual Prompts.
- **链接**: [arXiv:2510.19487](https://arxiv.org/abs/2510.19487) · 📚 被引 0
- **作者**: Chen Li, Huiying Xu, Changxin Gao, Zeyu Wang, Yun Liu, Xinzhong Zhu
- **🏷️ 机构**: Tencent, Zhejiang Normal University, Huazhong University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Single-source Domain Generalized Object Detection (SDGOD), as a cutting-edge research topic in computer vision, aims to enhance model generalization capability in unseen target domains through single-source domain training. Current mainstream approaches attempt to mitigate domain discrepancies via data augmentation techniques. However, due to domain shift and limited domain-specific knowledge, models tend to fall into the pitfall of spurious correlations. This manifests as the model's over-reliance on simplistic classification features (e.g., color) rather than essential domain-invariant representations like object contours. To address this critical challenge, we propose the Cauvis (Causal Visual Prompts) method. First, we introduce a Cross-Attention Prompts module that mitigates bias from spurious features by integrating visual prompts with cross-attention. To address the inadequate domain knowledge coverage and spurious feature entanglement in visual prompts for single-domain generalization, we propose a dual-branch adapter that disentangles causal-spurious features while achieving domain adaptation via high-frequency feature extraction. Cauvis achieves state-of-the-art performance with 15.9-31.4% gains over existing domain generalization methods on SDGOD datasets, while exhibiting significant robustness advantages in complex interference environments.

</details>

### VoxDet: Rethinking 3D Semantic Scene Completion as Dense Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7478016a59b9851ff6685a3fdd0f6b2e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Wuyang Li, Zhu Yu, Alexandre Alahi
- **🏷️ 机构**: EPFL - EPF Lausanne, Zhejiang University, EPFL
- **会议**: NeurIPS 2025

### VL-SAM-V2: Open-World Object Detection with General and Specific Query Fusion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/c3532dd633e600e9f6db57aa7ae0c858-Abstract-Conference.html)
- **作者**: Zhiwei Lin, Yongtao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### FlexEvent: Towards Flexible Event-Frame Object Detection at Varying Operational Frequencies.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/8064e4ebbcbe594628887b420956d8c3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dongyue Lu, Lingdong Kong, Gim Hee Lee, Camille Simon Chane, Wei Tsang Ooi
- **🏷️ 机构**: National University of Singapore, Ecole Nationale Supérieure de l'Electronique et de ses Applications
- **会议**: NeurIPS 2025

### Looking Beyond the Known: Towards a Data Discovery Guided Open-World Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/238597630b574e65fffb533444cf7d00-Abstract-Conference.html)
- **作者**: Anay Majee, Amitesh Gangrade, Rishabh Iyer
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### End-to-End Low-Light Enhancement for Object Detection with Learned Metadata from RAWs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/417f92ffb65cc4b8e8805b9be2fdbd9f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xuelin Shen, Haifeng Jiao, Yitong Wang, Yulin He, Wenhan Yang
- **🏷️ 机构**: GUANGMING Laboratory, Shenzhen University, ByteDance Inc
- **会议**: NeurIPS 2025

### Delving into Cascaded Instability: A Lipschitz Continuity View on Image Restoration and Object Detection Synergy.
- **链接**: [arXiv:2510.24232](https://arxiv.org/abs/2510.24232) · 📚 被引 0
- **作者**: Qing Zhao, Weijian Deng, Pengxu Wei, ZiYi Dong, Hannan Lu, Xiangyang Ji et al.
- **🏷️ 机构**: Sun Yat-sen University, Australian National University, SUN YAT-SEN UNIVERSITY
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To improve detection robustness in adverse conditions (e.g., haze and low light), image restoration is commonly applied as a pre-processing step to enhance image quality for the detector. However, the functional mismatch between restoration and detection networks can introduce instability and hinder effective integration -- an issue that remains underexplored. We revisit this limitation through the lens of Lipschitz continuity, analyzing the functional differences between restoration and detection networks in both the input space and the parameter space. Our analysis shows that restoration networks perform smooth, continuous transformations, while object detectors operate with discontinuous decision boundaries, making them highly sensitive to minor perturbations. This mismatch introduces instability in traditional cascade frameworks, where even imperceptible noise from restoration is amplified during detection, disrupting gradient flow and hindering optimization. To address this, we propose Lipschitz-regularized object detection (LROD), a simple yet effective framework that integrates image restoration directly into the detector's feature learning, harmonizing the Lipschitz continuity of both tasks during training. We implement this framework as Lipschitz-regularized YOLO (LR-YOLO), extending seamlessly to existing YOLO detectors. Extensive experiments on haze and low-light benchmarks demonstrate that LR-YOLO consistently improves detection stability, optimization smoothness, and overall accuracy.

</details>

### Rethinking Scale-Aware Temporal Encoding for Event-based Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d450dceeacd6083d1d550247377f2320-Abstract-Conference.html) · 📚 被引 1
- **作者**: Lin Zhu, Tengyu Long, Xiao Wang, Lizhi Wang, Hua Huang
- **🏷️ 机构**: Beijing Normal University, Beijing Institute of Technology, Beihang University
- **会议**: NeurIPS 2025

### ReCon: Region-Controllable Data Augmentation with Rectification and Alignment for Object Detection.
- **链接**: [arXiv:2510.15783](https://arxiv.org/abs/2510.15783) · [代码](https://github.com/haoweiz23/ReCon) · 📚 被引 0
- **作者**: Haowei Zhu, Tianxiang Pan, Rui Qin, Jun-Hai Yong, Bin Wang
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The scale and quality of datasets are crucial for training robust perception models. However, obtaining large-scale annotated data is both costly and time-consuming. Generative models have emerged as a powerful tool for data augmentation by synthesizing samples that adhere to desired distributions. However, current generative approaches often rely on complex post-processing or extensive fine-tuning on massive datasets to achieve satisfactory results, and they remain prone to content-position mismatches and semantic leakage. To overcome these limitations, we introduce ReCon, a novel augmentation framework that enhances the capacity of structure-controllable generative models for object detection. ReCon integrates region-guided rectification into the diffusion sampling process, using feedback from a pre-trained perception model to rectify misgenerated regions within diffusion sampling process. We further propose region-aligned cross-attention to enforce spatial-semantic alignment between image regions and their textual cues, thereby improving both semantic consistency and overall image fidelity. Extensive experiments demonstrate that ReCon substantially improve the quality and trainability of generated data, achieving consistent performance gains across various datasets, backbone architectures, and data scales. Our code is available at https://github.com/haoweiz23/ReCon .

</details>

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
