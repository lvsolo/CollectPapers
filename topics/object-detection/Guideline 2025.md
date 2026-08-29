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

### Roboflow100-VL: A Multi-Domain Object Detection Benchmark for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1013f8ff40a194f3f12a6bcc5221bb34-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Matvei Popov, Peter Robicheaux, Anish Madan, Isaac Robinson, Joseph Nelson, Deva Ramanan et al.
- **🏷️ 机构**: CMU
- **会议**: NeurIPS 2025

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

> In object detection, the instance count is typically used to define whether a dataset exhibits a long-tail distribution, implicitly assuming that models will underperform on categories with fewer instances. This assumption has led to extensive research on category bias in datasets with imbalanced instance counts. However, models still exhibit category bias even in datasets where instance counts are relatively balanced, clearly indicating that instance count alone cannot explain this phenomenon. In this work, we first introduce the concept and measurement of category information amount. We observe a significant negative correlation between category information amount and accuracy, suggesting that category information amount more accurately reflects the learning difficulty of a category. Based on this observation, we propose Information Amount-Guided Angular Margin (IGAM) Loss. The core idea of IGAM is to dynamically adjust the decision space of each category based on its information amount, thereby reducing category bias in long-tail datasets. IGAM Loss not only performs well on long-tailed benchmark datasets such as LVIS v1.0 and COCO-LT but also shows significant improvement for underrepresented categories in the non-long-tailed dataset Pascal VOC. Comprehensive experiments demonstrate the potential of category information amount as a tool and the generality of our proposed method.

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
- **会议**: NeurIPS 2025

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-Domain Few-Shot Object Detection (CD-FSOD) aims to detect novel objects with only a handful of labeled samples from previously unseen domains. While data augmentation and generative methods have shown promise in few-shot learning, their effectiveness for CD-FSOD remains unclear due to the need for both visual realism and domain alignment. Existing strategies, such as copy-paste augmentation and text-to-image generation, often fail to preserve the correct object category or produce backgrounds coherent with the target domain, making them non-trivial to apply directly to CD-FSOD. To address these challenges, we propose Domain-RAG, a training-free, retrieval-guided compositional image generation framework tailored for CD-FSOD. Domain-RAG consists of three stages: domain-aware background retrieval, domain-guided background generation, and foreground-background composition. Specifically, the input image is first decomposed into foreground and background regions. We then retrieve semantically and stylistically similar images to guide a generative model in synthesizing a new background, conditioned on both the original and retrieved contexts. Finally, the preserved foreground is composed with the newly generated domain-aligned background to form the generated image. Without requiring any additional supervision or training, Domain-RAG produces high-quality, domain-consistent samples across diverse tasks, including CD-FSOD, remote sensing FSOD, and camouflaged FSOD. Extensive experiments show consistent improvements over strong baselines and establish new state-of-the-art results. Codes will be released upon acceptance.

</details>

### Towards Single-Source Domain Generalized Object Detection via Causal Visual Prompts.
- **链接**: [arXiv:2510.19487](https://arxiv.org/abs/2510.19487) · 📚 被引 0
- **作者**: Chen Li, Huiying Xu, Changxin Gao, Zeyu Wang, Yun Liu, Xinzhong Zhu
- **🏷️ 机构**: Tencent, Zhejiang Normal University, Huazhong University of Science and Technology
- **会议**: NeurIPS 2025

### R2Det: Exploring Relaxed Rotation Equivariance in 2D Object Detection.
- **链接**: [出版页](https://openreview.net/forum?id=EUeNr3e8AV)
- **作者**: Zhiqiang Wu, Yingjie Liu, Hanlin Dong, Xuan Tang, Jian Yang, Bo Jin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

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

## 🆕 增量新增

### Event-Based Tiny Object Detection: A Benchmark Dataset and Baseline. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2506.23575](https://arxiv.org/abs/2506.23575) · 📚 被引 6
- **作者**: Nuo Chen, Chao Xiao, Yimian Dai, Shiman He, Miao Li, Wei An
- **🏷️ 机构**: National University of Defense Technology, Nankai University
- **会议**: ICCV 2025
- **摘要（中）**: 针对反无人机任务中小目标检测的挑战，以及现有事件相机目标检测数据集规模有限、目标尺寸大、背景多样性不足的问题，引入了首个大规模高多样性的反无人机事件小目标检测基准数据集EV-UAV，包含147个序列、超过230万个事件级标注，目标平均尺寸仅6.8×5.4像素，覆盖城市杂乱和极端光照等场景。基于小运动目标在时空事件点云中形成连续曲线的观察，提出了事件稀疏分割网络EV-SpSegNet作为基线方法，用于事件分割任务。
- **摘要（英）**: To address challenges in anti-UAV small object detection and limitations of existing event-based datasets (e.g., scale, target size, diversity), this paper introduces EV-UAV, the first large-scale benchmark with 147 sequences and over 2.3 million event-level annotations, featuring tiny targets averaging 6.8×5.4 pixels. It proposes EV-SpSegNet, a sparse segmentation network baseline leveraging the continuous curves formed by small moving targets in spatiotemporal event point clouds.
- **核心贡献**: 发布首个大规模事件小目标检测基准EV-UAV并提出EV-SpSegNet基线。
- **创新点**: 利用事件点云中目标连续曲线特性设计稀疏分割网络。
- **结果**: 提供高多样性基准，支持极端场景下的小目标检测研究。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Small object detection (SOD) in anti-UAV task is a challenging problem due to the small size of UAVs and complex backgrounds. Traditional frame-based cameras struggle to detect small objects in complex environments due to their low frame rates, limited dynamic range, and data redundancy. Event cameras, with microsecond temporal resolution and high dynamic range, provide a more effective solution for SOD. However, existing event-based object detection datasets are limited in scale, feature large targets size, and lack diverse backgrounds, making them unsuitable for SOD benchmarks. In this paper, we introduce a Event-based Small object detection (EVSOD) dataset (namely EV-UAV), the first large-scale, highly diverse benchmark for anti-UAV tasks. It includes 147 sequences with over 2.3 million event-level annotations, featuring extremely small targets (averaging 6.8 $\times$ 5.4 pixels) and diverse scenarios such as urban clutter and extreme lighting conditions. Furthermore, based on the observation that small moving targets form continuous curves in spatiotemporal event point clouds, we propose Event based Sparse Segmentation Network (EV-SpSegNet), a novel baseline for event segmentation in point cloud space, along with a Spatiotemporal Correlation (STC) loss that leverages motion continuity to guide the network in retaining target events. Extensive experiments on the EV-UAV dataset demonstrate the superiority of our method and provide a benchmark for future research in EVSOD. The dataset and code are at https://github.com/ChenYichen9527/Ev-UAV.

</details>

### STEP-DETR: Advancing DETR-based Semi-Supervised Object Detection with Super Teacher and Pseudo-Label Guided Text Queries. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00294) · 📚 被引 3
- **作者**: Tahira Shehzadi, Khurram Azeem Hashmi, Shalini Sarode, Didier Stricker, Muhammad Zeshan Afzal
- **🏷️ 机构**: DFKI
- **会议**: ICCV 2025
- **摘要（中）**: 针对DETR-based半监督目标检测中伪标签质量低和训练不稳定的问题，提出了STEP-DETR方法，引入超级教师（Super Teacher）模型和伪标签引导的文本查询机制。超级教师通过更强的模型生成高质量伪标签，文本查询利用类别语义信息指导目标查询的初始化，从而提升半监督学习效率。该方法在标准半监督检测基准上验证了有效性，显著优于现有方法。
- **摘要（英）**: To address low pseudo-label quality and training instability in DETR-based semi-supervised object detection, STEP-DETR introduces a Super Teacher model for generating high-quality pseudo-labels and pseudo-label guided text queries to initialize object queries with category semantics. It demonstrates significant improvements over existing methods on standard semi-supervised detection benchmarks.
- **核心贡献**: 提出超级教师和文本查询引导的半监督DETR检测方法。
- **创新点**: 利用文本语义信息增强伪标签引导的查询初始化。
- **结果**: 在半监督检测基准上显著提升性能。

### When Pixel Difference Patterns Meet ViT: PiDiViT for Few-Shot Object Detection. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02253) · 📚 被引 1
- **作者**: Hongliang Zhou, Yongxiang Liu, Canyu Mo, Weijie Li, Bowen Peng, Li Liu
- **🏷️ 机构**: The College of Electronic Science and Technology, National University of Defense Technology,China
- **会议**: ICCV 2025
- **摘要（中）**: 针对少样本目标检测中特征表示能力不足的问题，提出PiDiViT，将像素差分模式与Vision Transformer结合，以增强局部纹理和边缘信息的捕捉。方法通过引入像素差分卷积模块，在ViT中注入细粒度局部模式，提升少样本场景下的特征判别力。相比传统ViT或CNN方法，PiDiViT在保持全局建模能力的同时强化了局部细节，实验在多个少样本检测基准上验证了有效性。
- **摘要（英）**: To address the limited feature representation in few-shot object detection, PiDiViT integrates pixel difference patterns with Vision Transformer to enhance local texture and edge capture. It injects fine-grained local patterns via pixel difference convolution, improving discriminative features while retaining global modeling. Experiments on few-shot benchmarks demonstrate its effectiveness over conventional ViT and CNN baselines.
- **核心贡献**: 提出像素差分模式与ViT结合的少样本检测框架。
- **创新点**: 将像素差分卷积嵌入ViT以增强局部模式感知。
- **结果**: 在少样本检测基准上取得优于基线方法的性能。

### DON'T NEED RETRAINING: A Mixture of DETR and Vision Foundation Models for Cross-Domain Few-Shot Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d77402f07113388562f5b51eaee89573-Abstract-Conference.html)
- **作者**: Changhan Liu, Xunzhi Xiang, Zixuan Duan, Wenbin Li, Qi Fan, Yang Gao
- **🏷️ 机构**: Nanjing university, NJU, Nanjing University
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对跨域少样本目标检测中模型需重新训练的问题，提出一种混合DETR与视觉基础模型的方法，无需重新训练即可适应新域。方法利用DETR的查询机制和视觉基础模型的泛化能力，通过特征对齐和提示调整实现跨域迁移。相比传统微调策略，该方法显著降低了适应成本，并提升了少样本场景下的检测性能。
- **摘要（英）**: To avoid retraining in cross-domain few-shot object detection, this work proposes a mixture of DETR and vision foundation models for direct adaptation. It leverages DETR's query mechanism and foundation model generalization via feature alignment and prompt tuning. This reduces adaptation cost and improves detection performance compared to fine-tuning baselines.
- **核心贡献**: 提出无需重新训练的跨域少样本检测框架。
- **创新点**: 混合DETR与视觉基础模型实现零训练适应。
- **结果**: 在跨域少样本场景中取得有效性能提升。

### CQ-DINO: Mitigating Gradient Dilution via Category Queries for Vast Vocabulary Object Detection. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2503.18430](https://arxiv.org/abs/2503.18430)
- **作者**: Zhichao Sun, Huazhang Hu, Yidong Ma, Gang Liu, Yibo Chen, Xu Tang et al.
- **🏷️ 机构**: Wuhan University, ShanghaiTech University, Xiaohongshu
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对大词汇量目标检测中正负梯度稀释问题，提出CQ-DINO框架，将分类重构为对象查询与可学习类别查询的对比任务。方法引入图像引导查询选择，通过交叉注意力自适应检索每图相关类别，减少负空间并重平衡梯度分布，同时支持显式层次类别关系或隐式相关性学习。实验在V3Det和COCO等数据集上验证了优越性能。
- **摘要（英）**: To mitigate positive and hard negative gradient dilution in vast vocabulary detection, CQ-DINO reformulates classification as contrastive learning between object and category queries. It uses image-guided query selection to retrieve top-K categories via cross-attention, rebalancing gradients and enabling implicit hard mining. Experiments on V3Det and COCO demonstrate superior performance.
- **核心贡献**: 提出类别查询对比学习框架缓解梯度稀释。
- **创新点**: 图像引导查询选择与层次类别关系集成。
- **结果**: 在V3Det和COCO上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the exponential growth of data, traditional object detection methods are increasingly struggling to handle vast vocabulary object detection tasks effectively. We analyze two key limitations of classification-based detectors: positive gradient dilution, where rare positive categories receive insufficient learning signals, and hard negative gradient dilution, where discriminative gradients are overwhelmed by numerous easy negatives. To address these challenges, we propose CQ-DINO, a category query-based object detection framework that reformulates classification as a contrastive task between object queries and learnable category queries. Our method introduces image-guided query selection, which reduces the negative space by adaptively retrieving top-K relevant categories per image via cross-attention, thereby rebalancing gradient distributions and facilitating implicit hard example mining. Furthermore, CQ-DINO flexibly integrates explicit hierarchical category relationships in structured datasets (e.g., V3Det) or learns implicit category correlations via self-attention in generic datasets (e.g., COCO). Experiments demonstrate that CQ-DINO achieves superior performance on the challenging V3Det benchmark (surpassing previous methods by 2.1% AP) while maintaining competitiveness in COCO. Our work provides a scalable solution for real-world detection systems requiring wide category coverage. The code is publicly at https://github.com/FireRedTeam/CQ-DINO.

</details>

### CSPCL: Category Semantic Prior Contrastive Learning for Deformable DETR-Based Prohibited Item Detectors. **⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2501.16665](https://arxiv.org/abs/2501.16665)
- **作者**: Mingyuan Li, Tong Jia, Hao Wang, Bowen Ma, Hui Lu, Shiyi Guo et al.
- **🏷️ 机构**: Northeastern University, Huawei Technologies Ltd.
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对X射线图像中前景背景特征耦合导致违禁品检测性能差的问题，提出类别语义先验对比学习机制，对齐分类器感知的类原型与内容查询，补充缺失的语义信息。方法设计CSP损失，包含类内截断吸引和类间自适应排斥，优于经典对比损失。实验表明该方法增强了模型对前景特征的敏感性，提升了检测精度。
- **摘要（英）**: To address foreground-background feature coupling in X-ray prohibited item detection, CSPCL aligns class prototypes with content queries to supplement semantic information. It introduces CSP loss with intra-class truncated attraction and inter-class adaptive repulsion, outperforming classic contrastive losses. Experiments show enhanced foreground sensitivity and improved detection accuracy.
- **核心贡献**: 提出类别语义先验对比学习用于违禁品检测。
- **创新点**: 类内截断吸引与类间自适应排斥损失设计。
- **结果**: 在X射线检测任务上提升性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prohibited item detection based on X-ray images is one of the most effective security inspection methods. However, the foreground-background feature coupling caused by the overlapping phenomenon specific to X-ray images makes general detectors designed for natural images perform poorly. To address this issue, we propose a Category Semantic Prior Contrastive Learning (CSPCL) mechanism, which aligns the class prototypes perceived by the classifier with the content queries to correct and supplement the missing semantic information responsible for classification, thereby enhancing the model sensitivity to foreground features. To achieve this alignment, we design a specific contrastive loss, CSP loss, which comprises the Intra-Class Truncated Attraction (ITA) loss and the Inter-Class Adaptive Repulsion (IAR) loss, and outperforms classic contrastive losses. Specifically, the ITA loss leverages class prototypes to attract intra-class content queries and preserves essential intra-class diversity via a gradient truncation function. The IAR loss employs class prototypes to adaptively repel inter-class content queries, with the repulsion strength scaled by prototype-prototype similarity, thereby improving inter-class discriminability, especially among similar categories. CSPCL is general and can be easily integrated into Deformable DETR-based models. Extensive experiments on the PIXray, OPIXray, PIDray, and CLCXray datasets demonstrate that CSPCL significantly enhances the performance of various state-of-the-art models without increasing inference complexity. The code is publicly available at https://github.com/Limingyuan001/CSPCL.

</details>

### RaCFormer: Towards High-Quality 3D Object Detection via Query-based Radar-Camera Fusion.
- **链接**: [arXiv:2412.12725](https://arxiv.org/abs/2412.12725) · 📚 被引 12
- **作者**: Xiaomeng Chu, Jiajun Deng, Guoliang You, Yifan Duan, Houqiang Li, Yanyong Zhang
- **🏷️ 机构**: University of Science and Technology of China, The University of Adelaide
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose Radar-Camera fusion transformer (RaCFormer) to boost the accuracy of 3D object detection by the following insight. The Radar-Camera fusion in outdoor 3D scene perception is capped by the image-to-BEV transformation--if the depth of pixels is not accurately estimated, the naive combination of BEV features actually integrates unaligned visual content. To avoid this problem, we propose a query-based framework that enables adaptive sampling of instance-relevant features from both the bird's-eye view (BEV) and the original image view. Furthermore, we enhance system performance by two key designs: optimizing query initialization and strengthening the representational capacity of BEV. For the former, we introduce an adaptive circular distribution in polar coordinates to refine the initialization of object queries, allowing for a distance-based adjustment of query density. For the latter, we initially incorporate a radar-guided depth head to refine the transformation from image view to BEV. Subsequently, we focus on leveraging the Doppler effect of radar and introduce an implicit dynamic catcher to capture the temporal elements within the BEV. Extensive experiments on nuScenes and View-of-Delft (VoD) datasets validate the merits of our design. Remarkably, our method achieves superior results of 64.9% mAP and 70.2% NDS on nuScenes. RaCFormer also secures the state-of-the-art performance on the VoD dataset. Code is available at https://github.com/cxmomo/RaCFormer.

</details>

### VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving.
- **链接**: [arXiv:2411.14716](https://arxiv.org/abs/2411.14716) · 📚 被引 6
- **作者**: Haiming Zhang, Wending Zhou, Yiyao Zhu, Xu Yan, Jiantao Gao, Dongfeng Bai et al.
- **🏷️ 机构**: FNii,Shenzhen, HKUST, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces VisionPAD, a novel self-supervised pre-training paradigm designed for vision-centric algorithms in autonomous driving. In contrast to previous approaches that employ neural rendering with explicit depth supervision, VisionPAD utilizes more efficient 3D Gaussian Splatting to reconstruct multi-view representations using only images as supervision. Specifically, we introduce a self-supervised method for voxel velocity estimation. By warping voxels to adjacent frames and supervising the rendered outputs, the model effectively learns motion cues in the sequential data. Furthermore, we adopt a multi-frame photometric consistency approach to enhance geometric perception. It projects adjacent frames to the current frame based on rendered depths and relative poses, boosting the 3D geometric representation through pure image supervision. Extensive experiments on autonomous driving datasets demonstrate that VisionPAD significantly improves performance in 3D object detection, occupancy prediction and map segmentation, surpassing state-of-the-art pre-training strategies by a considerable margin.

</details>

### OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving.
- **链接**: [arXiv:2506.23565](https://arxiv.org/abs/2506.23565) · 📚 被引 1
- **作者**: Mingqian Ji, Shanshan Zhang, Jian Yang
- **🏷️ 机构**: School of Computer Science and Engineering, Nanjing University of Science and Technology,PCA Lab,Nanjing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current multi-view 3D object detection methods typically transfer 2D features into 3D space using depth estimation or 3D position encoder, but in a fully data-driven and implicit manner, which limits the detection performance. Inspired by the success of radiance fields on 3D reconstruction, we assume they can be used to enhance the detector's ability of 3D geometry estimation. However, we observe a decline in detection performance, when we directly use them for 3D rendering as an auxiliary task. From our analysis, we find the performance drop is caused by the strong responses on the background when rendering the whole scene. To address this problem, we propose object-centric radiance fields, focusing on modeling foreground objects while discarding background noises. Specifically, we employ Object-centric Radiance Fields (OcRF) to enhance 3D voxel features via an auxiliary task of rendering foreground objects. We further use opacity - the side-product of rendering- to enhance the 2D foreground BEV features via Height-aware Opacity-based Attention (HOA), where attention maps at different height levels are generated separately via multiple networks in parallel. Extensive experiments on the nuScenes validation and test datasets demonstrate that our OcRFDet achieves superior performance, outperforming previous state-of-the-art methods with 57.2$\%$ mAP and 64.8$\%$ NDS on the nuScenes test benchmark. Code will be available at https://github.com/Mingqj/OcRFDet.

</details>

### RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion.
- **链接**: [arXiv:2509.17712](https://arxiv.org/abs/2509.17712) · 📚 被引 1
- **作者**: Geonho Bang, Minjae Seong, Jisong Kim, Geunju Baek, Daye Oh, Junhyung Kim et al.
- **🏷️ 机构**: Seoul National University, Hanyang University, Hyundai Motor Company
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Radar-camera fusion methods have emerged as a cost-effective approach for 3D object detection but still lag behind LiDAR-based methods in performance. Recent works have focused on employing temporal fusion and Knowledge Distillation (KD) strategies to overcome these limitations. However, existing approaches have not sufficiently accounted for uncertainties arising from object motion or sensor-specific errors inherent in radar and camera modalities. In this work, we propose RCTDistill, a novel cross-modal KD method based on temporal fusion, comprising three key modules: Range-Azimuth Knowledge Distillation (RAKD), Temporal Knowledge Distillation (TKD), and Region-Decoupled Knowledge Distillation (RDKD). RAKD is designed to consider the inherent errors in the range and azimuth directions, enabling effective knowledge transfer from LiDAR features to refine inaccurate BEV representations. TKD mitigates temporal misalignment caused by dynamic objects by aligning historical radar-camera BEV features with current LiDAR representations. RDKD enhances feature discrimination by distilling relational knowledge from the teacher model, allowing the student to differentiate foreground and background features. RCTDistill achieves state-of-the-art radar-camera fusion performance on both the nuScenes and View-of-Delft (VoD) datasets, with the fastest inference speed of 26.2 FPS.

</details>

### Cycle-Consistent Learning for Joint Layout-to-Image Generation and Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00639) · 📚 被引 1
- **作者**: Xinhao Cai, Qiuxia Lai, Gensheng Pei, Xiangbo Shu, Yazhou Yao, Wenguan Wang
- **🏷️ 机构**: Nanjing University of Science and Technology, Communication University of China, Zhejiang University
- **会议**: ICCV 2025

### Enhancing Prompt Generation with Adaptive Refinement for Camouflaged Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01922)
- **作者**: Xuehan Chen, Guangyu Ren, Tianhong Dai, Tania Stathaki, Hengyan Liu
- **🏷️ 机构**: Xi&#x0027;an Jiaotong-Liverpool University,China, Imperial College London,United Kingdom
- **会议**: ICCV 2025

### Debiased Teacher for Day-to-Night Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00248) · 📚 被引 2
- **作者**: Yiming Cui, Liang Li, Haibing Yin, Yuhan Gao, Yaoqi Sun, Chenggang Yan
- **🏷️ 机构**: Hangzhou Dianzi University, Institute of Computing Technology, Chinese Academy of Sciences, Lishui University
- **会议**: ICCV 2025

### Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection.
- **链接**: [arXiv:2510.18437](https://arxiv.org/abs/2510.18437) · 📚 被引 1
- **作者**: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen, Jiesheng Wu et al.
- **🏷️ 机构**: College of Artificial Intelligence, Nankai University,China, The Hong Kong Polytechnic University,Department of Computing,Hong Kong, School of Computer and Information, Anhui Normal University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> At the core of Camouflaged Object Detection (COD) lies segmenting objects from their highly similar surroundings. Previous efforts navigate this challenge primarily through image-level modeling or annotation-based optimization. Despite advancing considerably, this commonplace practice hardly taps valuable dataset-level contextual information or relies on laborious annotations. In this paper, we propose RISE, a RetrIeval SElf-augmented paradigm that exploits the entire training dataset to generate pseudo-labels for single images, which could be used to train COD models. RISE begins by constructing prototype libraries for environments and camouflaged objects using training images (without ground truth), followed by K-Nearest Neighbor (KNN) retrieval to generate pseudo-masks for each image based on these libraries. It is important to recognize that using only training images without annotations exerts a pronounced challenge in crafting high-quality prototype libraries. In this light, we introduce a Clustering-then-Retrieval (CR) strategy, where coarse masks are first generated through clustering, facilitating subsequent histogram-based image filtering and cross-category retrieval to produce high-confidence prototypes. In the KNN retrieval stage, to alleviate the effect of artifacts in feature maps, we propose Multi-View KNN Retrieval (MVKR), which integrates retrieval results from diverse views to produce more robust and precise pseudo-masks. Extensive experiments demonstrate that RISE outperforms state-of-the-art unsupervised and prompt-based methods. Code is available at https://github.com/xiaohainku/RISE.

</details>

### Unified Category-Level Object Detection and Pose Estimation from RGB Images Using 3D Prototypes.
- **链接**: [arXiv:2508.02157](https://arxiv.org/abs/2508.02157)
- **作者**: Tom Fischer, Xiaojie Zhang, Eddy Ilg
- **🏷️ 机构**: Saarland University, University of Technology Nuremberg
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recognizing objects in images is a fundamental problem in computer vision. Although detecting objects in 2D images is common, many applications require determining their pose in 3D space. Traditional category-level methods rely on RGB-D inputs, which may not always be available, or employ two-stage approaches that use separate models and representations for detection and pose estimation. For the first time, we introduce a unified model that integrates detection and pose estimation into a single framework for RGB images by leveraging neural mesh models with learned features and multi-model RANSAC. Our approach achieves state-of-the-art results for RGB category-level pose estimation on REAL275, improving on the current state-of-the-art by 22.9% averaged across all scale-agnostic metrics. Finally, we demonstrate that our unified method exhibits greater robustness compared to single-stage baselines. Our code and models are available at https://github.com/Fischer-Tom/unified-detection-and-pose-estimation.

</details>

### Beyond RGB: Adaptive Parallel Processing for RAW Object Detection.
- **链接**: [arXiv:2503.13163](https://arxiv.org/abs/2503.13163)
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

### Diffusion-Based Source-Biased Model for Single Domain Generalized Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00152) · 📚 被引 2
- **作者**: Han Jiang, Wenfei Yang, Tianzhu Zhang, Yongdong Zhang
- **🏷️ 机构**: University of Science and Technology of China
- **会议**: ICCV 2025

### Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection.
- **链接**: [arXiv:2508.02288](https://arxiv.org/abs/2508.02288) · 📚 被引 2
- **作者**: Jae-Young Kang, Hoonhee Cho, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is essential for autonomous systems, enabling precise localization and dimension estimation. While LiDAR and RGB cameras are widely used, their fixed frame rates create perception gaps in high-speed scenarios. Event cameras, with their asynchronous nature and high temporal resolution, offer a solution by capturing motion continuously. The recent approach, which integrates event cameras with conventional sensors for continuous-time detection, struggles in fast-motion scenarios due to its dependency on synchronized sensors. We propose a novel stereo 3D object detection framework that relies solely on event cameras, eliminating the need for conventional 3D sensors. To compensate for the lack of semantic and geometric information in event data, we introduce a dual filter mechanism that extracts both. Additionally, we enhance regression by aligning bounding boxes with object-centric information. Experiments show that our method outperforms prior approaches in dynamic environments, demonstrating the potential of event cameras for robust, continuous-time 3D perception. The code is available at https://github.com/mickeykang16/Ev-Stereo3D.

</details>

### EVT: Efficient View Transformation for Multi-Modal 3D Object Detection.
- **链接**: [arXiv:2411.10715](https://arxiv.org/abs/2411.10715) · 📚 被引 3
- **作者**: Yongjin Lee, Hyeon Mun Jeong, Yurim Jeon, Sanghyun Kim
- **🏷️ 机构**: ThorDrive Co., Ltd,South Korea, Seoul National University,South Korea
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal sensor fusion in Bird's Eye View (BEV) representation has become the leading approach for 3D object detection. However, existing methods often rely on depth estimators or transformer encoders to transform image features into BEV space, which reduces robustness or introduces significant computational overhead. Moreover, the insufficient geometric guidance in view transformation results in ray-directional misalignments, limiting the effectiveness of BEV representations. To address these challenges, we propose Efficient View Transformation (EVT), a novel 3D object detection framework that constructs a well-structured BEV representation, improving both accuracy and efficiency. Our approach focuses on two key aspects. First, Adaptive Sampling and Adaptive Projection (ASAP), which utilizes LiDAR guidance to generate 3D sampling points and adaptive kernels, enables more effective transformation of image features into BEV space and a refined BEV representation. Second, an improved query-based detection framework, incorporating group-wise mixed query selection and geometry-aware cross-attention, effectively captures both the common properties and the geometric structure of objects in the transformer decoder. On the nuScenes test set, EVT achieves state-of-the-art performance of 75.3% NDS with real-time inference speed.

</details>

### Power of Cooperative Supervision: Multiple Teachers Framework for Advanced 3D Semi-Supervised Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00657) · 📚 被引 1
- **作者**: Jin-Hee Lee, Jae-Keun Lee, Jeseok Kim, Kwon Soon
- **🏷️ 机构**: DGIST,Daegu,Republic of Korea
- **会议**: ICCV 2025

### Task-Specific Zero-Shot Quantization-Aware Training for Object Detection.
- **链接**: [arXiv:2507.16782](https://arxiv.org/abs/2507.16782) · 📚 被引 2
- **作者**: Changhao Li, Xinrui Chen, Ji Wang, Kang Zhao, Jianfei Chen
- **🏷️ 机构**: School of Computational Science and Engineering, Georgia Institute of Technology,Atlanta,USA, Shenzhen International Graduate School, Tsinghua University,China, School of Software, Tsinghua University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Quantization is a key technique to reduce network size and computational complexity by representing the network parameters with a lower precision. Traditional quantization methods rely on access to original training data, which is often restricted due to privacy concerns or security challenges. Zero-shot Quantization (ZSQ) addresses this by using synthetic data generated from pre-trained models, eliminating the need for real training data. Recently, ZSQ has been extended to object detection. However, existing methods use unlabeled task-agnostic synthetic images that lack the specific information required for object detection, leading to suboptimal performance. In this paper, we propose a novel task-specific ZSQ framework for object detection networks, which consists of two main stages. First, we introduce a bounding box and category sampling strategy to synthesize a task-specific calibration set from the pre-trained network, reconstructing object locations, sizes, and category distributions without any prior knowledge. Second, we integrate task-specific training into the knowledge distillation process to restore the performance of quantized detection networks. Extensive experiments conducted on the MS-COCO and Pascal VOC datasets demonstrate the efficiency and state-of-the-art performance of our method. Our code is publicly available at: https://github.com/DFQ-Dojo/dfq-toolkit .

</details>

### Continual Adaptation: Environment-Conditional Parameter Generation for Object Detection in Dynamic Scenarios.
- **链接**: [arXiv:2506.24063](https://arxiv.org/abs/2506.24063)
- **作者**: Deng Li, Aming Wu, Yang Li, Yaowei Wang, Yahong Han
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University,Tianjin,China, School of Computer Science and Information Engineering, Hefei University of Technology,Hefei,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In practice, environments constantly change over time and space, posing significant challenges for object detectors trained based on a closed-set assumption, i.e., training and test data share the same distribution. To this end, continual test-time adaptation has attracted much attention, aiming to improve detectors' generalization by fine-tuning a few specific parameters, e.g., BatchNorm layers. However, based on a small number of test images, fine-tuning certain parameters may affect the representation ability of other fixed parameters, leading to performance degradation. Instead, we explore a new mechanism, i.e., converting the fine-tuning process to a specific-parameter generation. Particularly, we first design a dual-path LoRA-based domain-aware adapter that disentangles features into domain-invariant and domain-specific components, enabling efficient adaptation. Additionally, a conditional diffusion-based parameter generation mechanism is presented to synthesize the adapter's parameters based on the current environment, preventing the optimization from getting stuck in local optima. Finally, we propose a class-centered optimal transport alignment method to mitigate catastrophic forgetting. Extensive experiments conducted on various continuous domain adaptive object detection tasks demonstrate the effectiveness. Meanwhile, visualization results show that the representation extracted by the generated parameters can capture more object-related information and strengthen the generalization ability.

</details>

### LMM-Det: Make Large Multimodal Models Excel in Object Detection.
- **链接**: [arXiv:2507.18300](https://arxiv.org/abs/2507.18300) · 📚 被引 1
- **作者**: Jincheng Li, Chunyu Xie, Ji Ao, Dawei Leng, Yuhui Yin
- **🏷️ 机构**: 360 AI Research, Beihang University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multimodal models (LMMs) have garnered wide-spread attention and interest within the artificial intelligence research and industrial communities, owing to their remarkable capability in multimodal understanding, reasoning, and in-context learning, among others. While LMMs have demonstrated promising results in tackling multimodal tasks like image captioning, visual question answering, and visual grounding, the object detection capabilities of LMMs exhibit a significant gap compared to specialist detectors. To bridge the gap, we depart from the conventional methods of integrating heavy detectors with LMMs and propose LMM-Det, a simple yet effective approach that leverages a Large Multimodal Model for vanilla object Detection without relying on specialized detection modules. Specifically, we conduct a comprehensive exploratory analysis when a large multimodal model meets with object detection, revealing that the recall rate degrades significantly compared with specialist detection models. To mitigate this, we propose to increase the recall rate by introducing data distribution adjustment and inference optimization tailored for object detection. We re-organize the instruction conversations to enhance the object detection capabilities of large multimodal models. We claim that a large multimodal model possesses detection capability without any extra detection modules. Extensive experiments support our claim and show the effectiveness of the versatile LMM-Det. The datasets, models, and codes are available at https://github.com/360CVGroup/LMM-Det.

</details>

### PBCAT: Patch-Based Composite Adversarial Training Against Physically Realizable Attacks on Object Detection.
- **链接**: [arXiv:2506.23581](https://arxiv.org/abs/2506.23581)
- **作者**: Xiao Li, Yiming Zhu, Yifan Huang, Wei Zhang, Yingzhe He, Jie Shi et al.
- **🏷️ 机构**: BNRist, IDG/McGovern Institute for Brain Research, THBI, Tsinghua University,Department of Computer Science and Technology, Huawei Technologies
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection plays a crucial role in many security-sensitive applications. However, several recent studies have shown that object detectors can be easily fooled by physically realizable attacks, \eg, adversarial patches and recent adversarial textures, which pose realistic and urgent threats. Adversarial Training (AT) has been recognized as the most effective defense against adversarial attacks. While AT has been extensively studied in the $l_\infty$ attack settings on classification models, AT against physically realizable attacks on object detectors has received limited exploration. Early attempts are only performed to defend against adversarial patches, leaving AT against a wider range of physically realizable attacks under-explored. In this work, we consider defending against various physically realizable attacks with a unified AT method. We propose PBCAT, a novel Patch-Based Composite Adversarial Training strategy. PBCAT optimizes the model by incorporating the combination of small-area gradient-guided adversarial patches and imperceptible global adversarial perturbations covering the entire image. With these designs, PBCAT has the potential to defend against not only adversarial patches but also unseen physically realizable attacks such as adversarial textures. Extensive experiments in multiple settings demonstrated that PBCAT significantly improved robustness against various physically realizable attacks over state-of-the-art defense methods. Notably, it improved the detection accuracy by 29.7\% over previous defense methods under one recent adversarial texture attack.

</details>

### Gradient-Reweighted Adversarial Camouflage for Physical Object Detection Evasion.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01288)
- **作者**: Jiawei Liang, Siyuan Liang, Tianrui Lou, Ming Zhang, Wenjin Li, Dunqiu Fan et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, Nanyang Technological University, National Key Laboratory of Science and Technology on Information System Security
- **会议**: ICCV 2025

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
- **链接**: [arXiv:2506.21260](https://arxiv.org/abs/2506.21260)
- **作者**: Munish Monga, Vishal M. Chudasama, Pankaj Wasnik, Biplab Banerjee
- **🏷️ 机构**: Sony Research,India, Indian Institute of Technology,Bombay
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world object detection systems, such as those in autonomous driving and surveillance, must continuously learn new object categories and simultaneously adapt to changing environmental conditions. Existing approaches, Class Incremental Object Detection (CIOD) and Domain Incremental Object Detection (DIOD) only address one aspect of this challenge. CIOD struggles in unseen domains, while DIOD suffers from catastrophic forgetting when learning new classes, limiting their real-world applicability. To overcome these limitations, we introduce Dual Incremental Object Detection (DuIOD), a more practical setting that simultaneously handles class and domain shifts in an exemplar-free manner. We propose DuET, a Task Arithmetic-based model merging framework that enables stable incremental learning while mitigating sign conflicts through a novel Directional Consistency Loss. Unlike prior methods, DuET is detector-agnostic, allowing models like YOLO11 and RT-DETR to function as real-time incremental object detectors. To comprehensively evaluate both retention and adaptation, we introduce the Retention-Adaptability Index (RAI), which combines the Average Retention Index (Avg RI) for catastrophic forgetting and the Average Generalization Index for domain adaptability into a common ground. Extensive experiments on the Pascal Series and Diverse Weather Series demonstrate DuET's effectiveness, achieving a +13.12% RAI improvement while preserving 89.3% Avg RI on the Pascal Series (4 tasks), as well as a +11.39% RAI improvement with 88.57% Avg RI on the Diverse Weather Series (3 tasks), outperforming existing methods.

</details>

### ForeSight: Multi-View Streaming Joint Object Detection and Trajectory Forecasting.
- **链接**: [arXiv:2508.07089](https://arxiv.org/abs/2508.07089) · 📚 被引 2
- **作者**: Sandro Papais, Letian Wang, Brian Cheong, Steven L. Waslander
- **🏷️ 机构**: University of Toronto
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce ForeSight, a novel joint detection and forecasting framework for vision-based 3D perception in autonomous vehicles. Traditional approaches treat detection and forecasting as separate sequential tasks, limiting their ability to leverage temporal cues. ForeSight addresses this limitation with a multi-task streaming and bidirectional learning approach, allowing detection and forecasting to share query memory and propagate information seamlessly. The forecast-aware detection transformer enhances spatial reasoning by integrating trajectory predictions from a multiple hypothesis forecast memory queue, while the streaming forecast transformer improves temporal consistency using past forecasts and refined detections. Unlike tracking-based methods, ForeSight eliminates the need for explicit object association, reducing error propagation with a tracking-free model that efficiently scales across multi-frame sequences. Experiments on the nuScenes dataset show that ForeSight achieves state-of-the-art performance, achieving an EPA of 54.9%, surpassing previous methods by 9.3%, while also attaining the best mAP and minADE among multi-view detection and forecasting models.

</details>

### DM-EFS: Dynamically Multiplexed Expanded Features Set form for Robust and Efficient Small Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02278)
- **作者**: Aashish Sharma
- **🏷️ 机构**: KLASS Engineering and Solutions,Singapore
- **会议**: ICCV 2025

### DiffRefine: Diffusion-Based Proposal Specific Point Cloud Densification for Cross-Domain Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00465)
- **作者**: Sangyun Shin, Yuhang He, Xinyu Hou, Samuel Hodgson, Andrew Markham, Niki Trigoni
- **🏷️ 机构**: University of Oxford,Department of Computer Science,United Kingdom, Microsoft Research
- **会议**: ICCV 2025

### Uncertainty-Aware Gradient Stabilization for Small Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00787) · 📚 被引 5
- **作者**: Huixin Sun, Yanjing Li, Linlin Yang, Xianbin Cao, Baochang Zhang
- **🏷️ 机构**: School of Electronic Information Engineering, Beihang University, CUC,State Key Laboratory of Media Convergence and Communication, School of Artificial Intelligence, Beihang University
- **会议**: ICCV 2025

### VISO: Accelerating In-Orbit Object Detection with Language-Guided Mask Learning and Sparse Inference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02163)
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

### Adversarial Attention Perturbations for Large Object Detection Transformers.
- **链接**: [arXiv:2508.02987](https://arxiv.org/abs/2508.02987) · 📚 被引 1
- **作者**: Zachary Yahn, Selim Furkan Tekin, Fatih Ilhan, Sihao Hu, Tiansheng Huang, Yichang Xu et al.
- **🏷️ 机构**: Georgia Institute of Technology,Atlanta,GA, Georgia Tech Research Institute,Atlanta,USA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adversarial perturbations are useful tools for exposing vulnerabilities in neural networks. Existing adversarial perturbation methods for object detection are either limited to attacking CNN-based detectors or weak against transformer-based detectors. This paper presents an Attention-Focused Offensive Gradient (AFOG) attack against object detection transformers. By design, AFOG is neural-architecture agnostic and effective for attacking both large transformer-based object detectors and conventional CNN-based detectors with a unified adversarial attention framework. This paper makes three original contributions. First, AFOG utilizes a learnable attention mechanism that focuses perturbations on vulnerable image regions in multi-box detection tasks, increasing performance over non-attention baselines by up to 30.6%. Second, AFOG's attack loss is formulated by integrating two types of feature loss through learnable attention updates with iterative injection of adversarial perturbations. Finally, AFOG is an efficient and stealthy adversarial perturbation method. It probes the weak spots of detection transformers by adding strategically generated and visually imperceptible perturbations which can cause well-trained object detection models to fail. Extensive experiments conducted with twelve large detection transformers on COCO demonstrate the efficacy of AFOG. Our empirical results also show that AFOG outperforms existing attacks on transformer-based and CNN-based object detectors by up to 83% with superior speed and imperceptibility. Code is available at https://github.com/zacharyyahn/AFOG.

</details>

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
<!-- COMPLETE v1 papers=88 -->
