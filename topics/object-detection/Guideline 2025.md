# Object Detection — 2025 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 51 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MI-DETR: An Object Detection Model with Multi-time Inquiries Mechanism.
- **链接**: [arXiv:2503.01463](https://arxiv.org/abs/2503.01463) · 📚 被引 17
- **作者**: Zhixiong Nan, Xianghong Li, Jifeng Dai, Tao Xiang
- **🏷️ 机构**: Chongqing University,College of Computer Science,Chongqing,China, Tsinghua University,Department of Electronic Engineering,Beijing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Based on analyzing the character of cascaded decoder architecture commonly adopted in existing DETR-like models, this paper proposes a new decoder architecture. The cascaded decoder architecture constrains object queries to update in the cascaded direction, only enabling object queries to learn relatively-limited information from image features. However, the challenges for object detection in natural scenes (e.g., extremely-small, heavily-occluded, and confusingly mixed with the background) require an object detection model to fully utilize image features, which motivates us to propose a new decoder architecture with the parallel Multi-time Inquiries (MI) mechanism. MI enables object queries to learn more comprehensive information, and our MI based model, MI-DETR, outperforms all existing DETR-like models on COCO benchmark under different backbones and training epochs, achieving +2.3 AP and +0.6 AP improvements compared to the most representative model DINO and SOTA model Relation-DETR under ResNet-50 backbone. In addition, a series of diagnostic and visualization experiments demonstrate the effectiveness, rationality, and interpretability of MI.

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

> Oriented Object Detection (OOD) has received increased attention in the past years, being a suitable solution for detecting elongated objects in remote sensing analysis. In particular, using regression loss functions based on Gaussian distributions has become attractive since they yield simple and differentiable terms. However, existing solutions are still based on regression heads that produce Oriented Bounding Boxes (OBBs), and the known problem of angular boundary discontinuity persists. In this work, we propose a regression head for OOD that directly produces Gaussian distributions based on the Cholesky matrix decomposition. The proposed head, named GauCho, theoretically mitigates the boundary discontinuity problem and is fully compatible with recent Gaussian-based regression loss functions. Furthermore, we advocate using Oriented Ellipses (OEs) to represent oriented objects, which relates to GauCho through a bijective function and alleviates the encoding ambiguity problem for circular objects. Our experimental results show that GauCho can be a viable alternative to the traditional OBB head, achieving results comparable to or better than state-of-the-art detectors for the challenging dataset DOTA

</details>

### Search and Detect: Training-Free Long Tail Object Detection via Web-Image Retrieval.
- **链接**: [arXiv:2409.18733](https://arxiv.org/abs/2409.18733) · 📚 被引 0
- **作者**: Mankeerat Sidhu, Hetarth Chopra, Ansel Blume, Jeonghwan Kim, Revanth Gangi Reddy, Heng Ji
- **🏷️ 机构**: University of Illinois Urbana Champaign,Urbana,USA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce SearchDet, a training-free long-tail object detection framework that significantly enhances open-vocabulary object detection performance. SearchDet retrieves a set of positive and negative images of an object to ground, embeds these images, and computes an input image-weighted query which is used to detect the desired concept in the image. Our proposed method is simple and training-free, yet achieves over 48.7% mAP improvement on ODinW and 59.1% mAP improvement on LVIS compared to state-of-the-art models such as GroundingDINO. We further show that our approach of basing object detection on a set of Web-retrieved exemplars is stable with respect to variations in the exemplars, suggesting a path towards eliminating costly data annotation and training procedures.

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

> Remote sensing image object detection (RSIOD) aims to identify and locate specific objects within satellite or aerial imagery. However, there is a scarcity of labeled data in current RSIOD datasets, which significantly limits the performance of current detection algorithms. Although existing techniques, e.g., data augmentation and semi-supervised learning, can mitigate this scarcity issue to some extent, they are heavily dependent on high-quality labeled data and perform worse in rare object classes. To address this issue, this paper proposes a layout-controllable diffusion generative model (i.e. AeroGen) tailored for RSIOD. To our knowledge, AeroGen is the first model to simultaneously support horizontal and rotated bounding box condition generation, thus enabling the generation of high-quality synthetic images that meet specific layout and object category requirements. Additionally, we propose an end-to-end data augmentation framework that integrates a diversity-conditioned generator and a filtering mechanism to enhance both the diversity and quality of generated data. Experimental results demonstrate that the synthetic data produced by our method are of high quality and diversity. Furthermore, the synthetic RSIOD data can significantly improve the detection performance of existing RSIOD models, i.e., the mAP metrics on DIOR, DIOR-R, and HRSC datasets are improved by 3.7%, 4.3%, and 2.43%, respectively. The code is available at https://github.com/Sonettoo/AeroGen.

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

> Existing co-salient object detection (CoSOD) methods generally employ a three-stage architecture (i.e., encoding, consensus extraction & dispersion, and prediction) along with a typical full fine-tuning paradigm. Although they yield certain benefits, they exhibit two notable limitations: 1) This architecture relies on encoded features to facilitate consensus extraction, but the meticulously extracted consensus does not provide timely guidance to the encoding stage. 2) This paradigm involves globally updating all parameters of the model, which is parameter-inefficient and hinders the effective representation of knowledge within the foundation model for this task. Therefore, in this paper, we propose an interaction-effective and parameter-efficient concise architecture for the CoSOD task, addressing two key limitations. It introduces, for the first time, a parameter-efficient prompt tuning paradigm and seamlessly embeds consensus into the prompts to formulate task-specific Visual Consensus Prompts (VCP). Our VCP aims to induce the frozen foundation model to perform better on CoSOD tasks by formulating task-specific visual consensus prompts with minimized tunable parameters. Concretely, the primary insight of the purposeful Consensus Prompt Generator (CPG) is to enforce limited tunable parameters to focus on co-salient representations and generate consensus prompts. The formulated Consensus Prompt Disperser (CPD) leverages consensus prompts to form task-specific visual consensus prompts, thereby arousing the powerful potential of pre-trained models in addressing CoSOD tasks. Extensive experiments demonstrate that our concise VCP outperforms 13 cutting-edge full fine-tuning models, achieving the new state of the art (with 6.8% improvement in F_m metrics on the most challenging CoCA dataset). Source code has been available at https://github.com/WJ-CV/VCP.

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
