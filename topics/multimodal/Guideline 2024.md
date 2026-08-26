# Multimodal — 2024 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 85 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MTMMC: A Large-Scale Real-World Multi-Modal Camera Tracking Benchmark.
- **链接**: [arXiv:2403.20225](https://arxiv.org/abs/2403.20225) · 📚 被引 6
- **作者**: Sanghyun Woo, Kwanyong Park, Inkyu Shin, Myungchul Kim, In So Kweon
- **🏷️ 机构**: New York University, ETRI, KAIST
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multi-target multi-camera tracking is a crucial task that involves identifying and tracking individuals over time using video streams from multiple cameras. This task has practical applications in various fields, such as visual surveillance, crowd behavior analysis, and anomaly detection. However, due to the difficulty and cost of collecting and labeling data, existing datasets for this task are either synthetically generated or artificially constructed within a controlled camera network setting, which limits their ability to model real-world dynamics and generalize to diverse camera configurations. To address this issue, we present MTMMC, a real-world, large-scale dataset that includes long video sequences captured by 16 multi-modal cameras in two different environments - campus and factory - across various time, weather, and season conditions. This dataset provides a challenging test-bed for studying multi-camera tracking under diverse real-world complexities and includes an additional input modality of spatially aligned and temporally synchronized RGB and thermal cameras, which enhances the accuracy of multi-camera tracking. MTMMC is a super-set of existing datasets, benefiting independent fields such as person detection, re-identification, and multiple object tracking. We provide baselines and new learning setups on this dataset and set the reference scores for future studies. The datasets, models, and test server will be made publicly available.

### MMMU: A Massive Multi-Discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI.
- **链接**: [arXiv:2311.16502](https://arxiv.org/abs/2311.16502) · 📚 被引 399
- **作者**: Xiang Yue, Yuansheng Ni, Tianyu Zheng, Kai Zhang, Ruoqi Liu, Ge Zhang et al.
- **🏷️ 机构**: IN. AI Research, University of Waterloo, Independent
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We introduce MMMU: a new benchmark designed to evaluate multimodal models on massive multi-discipline tasks demanding college-level subject knowledge and deliberate reasoning. MMMU includes 11.5K meticulously collected multimodal questions from college exams, quizzes, and textbooks, covering six core disciplines: Art & Design, Business, Science, Health & Medicine, Humanities & Social Science, and Tech & Engineering. These questions span 30 subjects and 183 subfields, comprising 30 highly heterogeneous image types, such as charts, diagrams, maps, tables, music sheets, and chemical structures. Unlike existing benchmarks, MMMU focuses on advanced perception and reasoning with domain-specific knowledge, challenging models to perform tasks akin to those faced by experts. The evaluation of 14 open-source LMMs as well as the proprietary GPT-4V(ision) and Gemini highlights the substantial challenges posed by MMMU. Even the advanced GPT-4V and Gemini Ultra only achieve accuracies of 56% and 59% respectively, indicating significant room for improvement. We believe MMMU will stimulate the community to build next-generation multimodal foundation models towards expert artificial general intelligence.

### MVBench: A Comprehensive Multi-modal Video Understanding Benchmark.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02095)
- **作者**: Kunchang Li, Yali Wang, Yinan He, Yizhuo Li, Yi Wang, Yi Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Weakly Misalignment-Free Adaptive Feature Alignment for UAVs-Based Multimodal Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02534) · 📚 被引 83
- **作者**: Chen Chen, Jiahao Qi, Xingyue Liu, Kangcheng Bin, Ruigang Fu, Xikun Hu et al.
- **🏷️ 机构**: National University of Defense Technology,China
- **会议**: CVPR 2024

### Open-World Human-Object Interaction Detection via Multi-Modal Prompts.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01604) · 📚 被引 28
- **作者**: Jie Yang, Bingliang Li, Ailing Zeng, Lei Zhang, Ruimao Zhang
- **🏷️ 机构**: The Chinese University of Hong Kong,Shenzhen, International Digital Economy Academy
- **会议**: CVPR 2024

### Scene-adaptive and Region-aware Multi-modal Prompt for Open Vocabulary Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01584)
- **作者**: Xiaowei Zhao, Xianglong Liu, Duorui Wang, Yajun Gao, Zhide Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis.
- **链接**: [arXiv:2402.17483](https://arxiv.org/abs/2402.17483) · 📚 被引 13
- **作者**: Tang Tao, Guangrun Wang, Yixing Lao, Peng Chen, Jie Liu, Liang Lin et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, University of Oxford, HKU
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Neural implicit fields have been a de facto standard in novel view synthesis. Recently, there exist some methods exploring fusing multiple modalities within a single field, aiming to share implicit features from different modalities to enhance reconstruction performance. However, these modalities often exhibit misaligned behaviors: optimizing for one modality, such as LiDAR, can adversely affect another, like camera performance, and vice versa. In this work, we conduct comprehensive analyses on the multimodal implicit field of LiDAR-camera joint synthesis, revealing the underlying issue lies in the misalignment of different sensors. Furthermore, we introduce AlignMiF, a geometrically aligned multimodal implicit field with two proposed modules: Geometry-Aware Alignment (GAA) and Shared Geometry Initialization (SGI). These modules effectively align the coarse geometry across different modalities, significantly enhancing the fusion process between LiDAR and camera data. Through extensive experiments across various datasets and scenes, we demonstrate the effectiveness of our approach in facilitating better interaction between LiDAR and camera modalities within a unified neural field. Specifically, our proposed AlignMiF, achieves remarkable improvement over recent implicit fusion methods (+2.01 and +3.11 image PSNR on the KITTI-360 and Waymo datasets) and consistently surpasses single modality performance (13.8% and 14.2% reduction in LiDAR Chamfer Distance on the respective datasets).

### Draw Step by Step: Reconstructing CAD Construction Sequences from Point Clouds via Multimodal Diffusion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02564) · 📚 被引 23
- **作者**: Weijian Ma, Shuaiqi Chen, Yunzhong Lou, Xueyang Li, Xiangdong Zhou
- **🏷️ 机构**: School of Computer Science and Technology, Fudan University
- **会议**: CVPR 2024

### StreamingFlow: Streaming Occupancy Forecasting with Asynchronous Multi-modal Data Streams via Neural Ordinary Differential Equation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01405) · 📚 被引 3
- **作者**: Yining Shi, Kun Jiang, Ke Wang, Jiusi Li, Yunlong Wang, Mengmeng Yang et al.
- **🏷️ 机构**: School of Vehicle and Mobility, Tsinghua University, KargoBot, Inc
- **会议**: CVPR 2024

### SDSTrack: Self-Distillation Symmetric Adapter Learning for Multi-Modal Visual Object Tracking.
- **链接**: [arXiv:2403.16002](https://arxiv.org/abs/2403.16002) · [代码](https://github.com/hoqolo/SDSTrack) · 📚 被引 113
- **作者**: Xiaojun Hou, Jiazheng Xing, Yijie Qian, Yaowei Guo, Shuo Xin, Junhao Chen et al.
- **🏷️ 机构**: Zhejiang University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multimodal Visual Object Tracking (VOT) has recently gained significant attention due to its robustness. Early research focused on fully fine-tuning RGB-based trackers, which was inefficient and lacked generalized representation due to the scarcity of multimodal data. Therefore, recent studies have utilized prompt tuning to transfer pre-trained RGB-based trackers to multimodal data. However, the modality gap limits pre-trained knowledge recall, and the dominance of the RGB modality persists, preventing the full utilization of information from other modalities. To address these issues, we propose a novel symmetric multimodal tracking framework called SDSTrack. We introduce lightweight adaptation for efficient fine-tuning, which directly transfers the feature extraction ability from RGB to other domains with a small number of trainable parameters and integrates multimodal features in a balanced, symmetric manner. Furthermore, we design a complementary masked patch distillation strategy to enhance the robustness of trackers in complex environments, such as extreme weather, poor imaging, and sensor failure. Extensive experiments demonstrate that SDSTrack outperforms state-of-the-art methods in various multimodal tracking scenarios, including RGB+Depth, RGB+Thermal, and RGB+Event tracking, and exhibits impressive results in extreme conditions. Our source code is available at https://github.com/hoqolo/SDSTrack.

### OVMR: Open-Vocabulary Recognition with Multi-Modal References.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01568)
- **作者**: Zehong Ma, Shiliang Zhang, Longhui Wei, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01487)
- **作者**: Jianjian Cao, Peng Ye, Shengze Li, Chong Yu, Yansong Tang, Jiwen Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### VCoder: Versatile Vision Encoders for Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02644)
- **作者**: Jitesh Jain, Jianwei Yang, Humphrey Shi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action.
- **链接**: [arXiv:2312.17172](https://arxiv.org/abs/2312.17172) · 📚 被引 95
- **作者**: Jiasen Lu, Christopher Clark, Sangho Lee, Zichen Zhang, Savya Khosla, Ryan Marten et al.
- **🏷️ 机构**: Allen Institute for AI, University of Illinois Urbana-Champaign
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

### MMA: Multi-Modal Adapter for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02249)
- **作者**: Lingxiao Yang, Ru-Yuan Zhang, Yanchen Wang, Xiaohua Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Source-Free Domain Adaptation with Frozen Multimodal Foundation Model.
- **链接**: [arXiv:2311.16510](https://arxiv.org/abs/2311.16510) · 📚 被引 55
- **作者**: Song Tang, Wenxin Su, Mao Ye, Xiatian Zhu
- **🏷️ 机构**: University of Shanghai for Science and Technology, University of Electronic Science and Technology of China, University of Surrey
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Source-Free Domain Adaptation (SFDA) aims to adapt a source model for a target domain, with only access to unlabeled target training data and the source model pre-trained on a supervised source domain. Relying on pseudo labeling and/or auxiliary supervision, conventional methods are inevitably error-prone. To mitigate this limitation, in this work we for the first time explore the potentials of off-the-shelf vision-language (ViL) multimodal models (e.g.,CLIP) with rich whilst heterogeneous knowledge. We find that directly applying the ViL model to the target domain in a zero-shot fashion is unsatisfactory, as it is not specialized for this particular task but largely generic. To make it task specific, we propose a novel Distilling multimodal Foundation model(DIFO)approach. Specifically, DIFO alternates between two steps during adaptation: (i) Customizing the ViL model by maximizing the mutual information with the target model in a prompt learning manner, (ii) Distilling the knowledge of this customized ViL model to the target model. For more fine-grained and reliable distillation, we further introduce two effective regularization terms, namely most-likely category encouragement and predictive consistency. Extensive experiments show that DIFO significantly outperforms the state-of-the-art alternatives. Code is here

### Sieve: Multimodal Dataset Pruning Using Image Captioning Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02116)
- **作者**: Anas Mahmoud, Mostafa Elhoushi, Amro Abbas, Yu Yang, Newsha Ardalani, Hugh Leather et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01282)
- **作者**: Bo He, Hengduo Li, Young Kyun Jang, Menglin Jia, Xuefei Cao, Ashish Shah et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Multimodal Representation Learning by Alternating Unimodal Adaptation.
- **链接**: [arXiv:2311.10707](https://arxiv.org/abs/2311.10707) · [代码](https://github.com/Cecile-hi/Multimodal-Learning-with-Alternating-Unimodal-Adaptation) · 📚 被引 56
- **作者**: Xiaohui Zhang, Jaehong Yoon, Mohit Bansal, Huaxiu Yao
- **🏷️ 机构**: UNC-Chapel Hill
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multimodal learning, which integrates data from diverse sensory modes, plays a pivotal role in artificial intelligence. However, existing multimodal learning methods often struggle with challenges where some modalities appear more dominant than others during multimodal learning, resulting in suboptimal performance. To address this challenge, we propose MLA (Multimodal Learning with Alternating Unimodal Adaptation). MLA reframes the conventional joint multimodal learning process by transforming it into an alternating unimodal learning process, thereby minimizing interference between modalities. Simultaneously, it captures cross-modal interactions through a shared head, which undergoes continuous optimization across different modalities. This optimization process is controlled by a gradient modification mechanism to prevent the shared head from losing previously acquired information. During the inference phase, MLA utilizes a test-time uncertainty-based model fusion mechanism to integrate multimodal information. Extensive experiments are conducted on five diverse datasets, encompassing scenarios with complete modalities and scenarios with missing modalities. These experiments demonstrate the superiority of MLA over competing prior approaches. Our code is available at https://github.com/Cecile-hi/Multimodal-Learning-with-Alternating-Unimodal-Adaptation.

### ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01710)
- **作者**: Xiaoqi Li, Mingxu Zhang, Yiran Geng, Haoran Geng, Yuxing Long, Yan Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Multimodal Prompt Perceiver: Empower Adaptiveness, Generalizability and Fidelity for All-in-One Image Restoration.
- **链接**: [arXiv:2312.02918](https://arxiv.org/abs/2312.02918) · 📚 被引 73
- **作者**: Yuang Ai, Huaibo Huang, Xiaoqiang Zhou, Jiexiang Wang, Ran He
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,MAIS &#x0026; CRIPAC,Beijing,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Despite substantial progress, all-in-one image restoration (IR) grapples with persistent challenges in handling intricate real-world degradations. This paper introduces MPerceiver: a novel multimodal prompt learning approach that harnesses Stable Diffusion (SD) priors to enhance adaptiveness, generalizability and fidelity for all-in-one image restoration. Specifically, we develop a dual-branch module to master two types of SD prompts: textual for holistic representation and visual for multiscale detail representation. Both prompts are dynamically adjusted by degradation predictions from the CLIP image encoder, enabling adaptive responses to diverse unknown degradations. Moreover, a plug-in detail refinement module improves restoration fidelity via direct encoder-to-decoder information transformation. To assess our method, MPerceiver is trained on 9 tasks for all-in-one IR and outperforms state-of-the-art task-specific methods across most tasks. Post multitask pre-training, MPerceiver attains a generalized representation in low-level vision, exhibiting remarkable zero-shot and few-shot capabilities in unseen tasks. Extensive experiments on 16 IR tasks underscore the superiority of MPerceiver in terms of adaptiveness, generalizability and fidelity.

### Can Language Beat Numerical Regression? Language-Based Multimodal Trajectory Prediction.
- **链接**: [arXiv:2403.18447](https://arxiv.org/abs/2403.18447) · [代码](https://github.com/inhwanbae/LMTrajectory) · 📚 被引 49
- **作者**: Inhwan Bae, Junoh Lee, Hae-Gon Jeon
- **🏷️ 机构**: AI Graduate School, School of Electrical Engineering and Computer Science Gwangju Institute of Science and Technology,Gwangju,South Korea
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Language models have demonstrated impressive ability in context understanding and generative performance. Inspired by the recent success of language foundation models, in this paper, we propose LMTraj (Language-based Multimodal Trajectory predictor), which recasts the trajectory prediction task into a sort of question-answering problem. Departing from traditional numerical regression models, which treat the trajectory coordinate sequence as continuous signals, we consider them as discrete signals like text prompts. Specially, we first transform an input space for the trajectory coordinate into the natural language space. Here, the entire time-series trajectories of pedestrians are converted into a text prompt, and scene images are described as text information through image captioning. The transformed numerical and image data are then wrapped into the question-answering template for use in a language model. Next, to guide the language model in understanding and reasoning high-level knowledge, such as scene context and social relationships between pedestrians, we introduce an auxiliary multi-task question and answering. We then train a numerical tokenizer with the prompt data. We encourage the tokenizer to separate the integer and decimal parts well, and leverage it to capture correlations between the consecutive numbers in the language model. Lastly, we train the language model using the numerical tokenizer and all of the question-answer prompts. Here, we propose a beam-search-based most-likely prediction and a temperature-based multimodal prediction to implement both deterministic and stochastic inferences. Applying our LMTraj, we show that the language-based model can be a powerful pedestrian trajectory predictor, and outperforms existing numerical-based predictor methods. Code is publicly available at https://github.com/inhwanbae/LMTrajectory .

### ViP-LLaVA: Making Large Multimodal Models Understand Arbitrary Visual Prompts.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01227)
- **作者**: Mu Cai, Haotian Liu, Siva Karthik Mustikovela, Gregory P. Meyer, Yuning Chai, Dennis Park et al.
- **🏷️ 机构**: Waymo
- **会议**: CVPR 2024

### Honeybee: Locality-Enhanced Projector for Multimodal LLM.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01311)
- **作者**: Junbum Cha, Wooyoung Kang, Jonghwan Mun, Byungseok Roh
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### LION : Empowering Multimodal Large Language Model with Dual-Level Visual Knowledge.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02506)
- **作者**: Gongwei Chen, Leyang Shen, Rui Shao, Xiang Deng, Liqiang Nie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping.
- **链接**: [arXiv:2312.04521](https://arxiv.org/abs/2312.04521) · 📚 被引 73
- **作者**: Alex Costanzino, Pierluigi Zama Ramirez, Giuseppe Lisanti, Luigi Di Stefano
- **🏷️ 机构**: University of Bologna,CVLAB,Department of Computer Science and Engineering (DISI),Italy
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The paper explores the industrial multimodal Anomaly Detection (AD) task, which exploits point clouds and RGB images to localize anomalies. We introduce a novel light and fast framework that learns to map features from one modality to the other on nominal samples. At test time, anomalies are detected by pinpointing inconsistencies between observed and mapped features. Extensive experiments show that our approach achieves state-of-the-art detection and segmentation performance in both the standard and few-shot settings on the MVTec 3D-AD dataset while achieving faster inference and occupying less memory than previous multimodal AD methods. Moreover, we propose a layer-pruning technique to improve memory and time efficiency with a marginal sacrifice in performance.

### On the Robustness of Large Multimodal Models Against Image Adversarial Attacks.
- **链接**: [arXiv:2312.03777](https://arxiv.org/abs/2312.03777) · 📚 被引 51
- **作者**: Xuanming Cui, Alejandro Aparcedo, Young Kyun Jang, Ser-Nam Lim
- **🏷️ 机构**: University of Central Florida
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advances in instruction tuning have led to the development of State-of-the-Art Large Multimodal Models (LMMs). Given the novelty of these models, the impact of visual adversarial attacks on LMMs has not been thoroughly examined. We conduct a comprehensive study of the robustness of various LMMs against different adversarial attacks, evaluated across tasks including image classification, image captioning, and Visual Question Answer (VQA). We find that in general LMMs are not robust to visual adversarial inputs. However, our findings suggest that context provided to the model via prompts, such as questions in a QA pair helps to mitigate the effects of visual adversarial inputs. Notably, the LMMs evaluated demonstrated remarkable resilience to such attacks on the ScienceQA task with only an 8.10% drop in performance compared to their visual counterparts which dropped 99.73%. We also propose a new approach to real-world image classification which we term query decomposition. By incorporating existence queries into our input prompt we observe diminished attack effectiveness and improvements in image classification accuracy. This research highlights a previously under-explored facet of LMM robustness and sets the stage for future work aimed at strengthening the resilience of multimodal systems in adversarial environments.

### EMOPortraits: Emotion-Enhanced Multimodal One-Shot Head Avatars.
- **链接**: [arXiv:2404.19110](https://arxiv.org/abs/2404.19110) · 📚 被引 41
- **作者**: Nikita Drobyshev, Antoni Bigata Casademunt, Konstantinos Vougioukas, Zoe Landgraf, Stavros Petridis, Maja Pantic
- **🏷️ 机构**: Imperial College London
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Head avatars animated by visual signals have gained popularity, particularly in cross-driving synthesis where the driver differs from the animated character, a challenging but highly practical approach. The recently presented MegaPortraits model has demonstrated state-of-the-art results in this domain. We conduct a deep examination and evaluation of this model, with a particular focus on its latent space for facial expression descriptors, and uncover several limitations with its ability to express intense face motions. To address these limitations, we propose substantial changes in both training pipeline and model architecture, to introduce our EMOPortraits model, where we: Enhance the model's capability to faithfully support intense, asymmetric face expressions, setting a new state-of-the-art result in the emotion transfer task, surpassing previous methods in both metrics and quality. Incorporate speech-driven mode to our model, achieving top-tier performance in audio-driven facial animation, making it possible to drive source identity through diverse modalities, including visual signal, audio, or a blend of both. We propose a novel multi-view video dataset featuring a wide range of intense and asymmetric facial expressions, filling the gap with absence of such data in existing datasets.

### Question Aware Vision Transformer for Multimodal Reasoning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01315)
- **作者**: Roy Ganz, Yair Kittenplon, Aviad Aberdam, Elad Ben-Avraham, Oren Nuriel, Shai Mazor et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Embracing Unimodal Aleatoric Uncertainty for Robust Multimodal Fusion.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02538) · 📚 被引 52
- **作者**: Zixian Gao, Xun Jiang, Xing Xu, Fumin Shen, Yujie Li, Heng Tao Shen
- **🏷️ 机构**: Center for Future Media &#x0026; School of Computer Science and Engineering, University of Electronic Science and Technology of China,China, Kyushu Institute of Technology,Japan
- **会议**: CVPR 2024

### PAIR Diffusion: A Comprehensive Multimodal Object-Level Image Editor.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00822) · 📚 被引 13
- **作者**: Vidit Goel, Elia Peruzzo, Yifan Jiang, Dejia Xu, Xingqian Xu, Nicu Sebe et al.
- **🏷️ 机构**: Picsart AI Research (PAIR), University of Trento, UT Austin
- **会议**: CVPR 2024

### SmartEdit: Exploring Complex Instruction-Based Image Editing with Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00799)
- **作者**: Yuzhou Huang, Liangbin Xie, Xintao Wang, Ziyang Yuan, Xiaodong Cun, Yixiao Ge et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Modeling Dense Multimodal Interactions Between Biological Pathways and Histology for Survival Prediction.
- **链接**: [arXiv:2304.06819](https://arxiv.org/abs/2304.06819) · [代码](https://github.com/ajv012/SurvPath) · 📚 被引 130
- **作者**: Guillaume Jaume, Anurag Vaidya, Richard J. Chen, Drew F. K. Williamson, Paul Pu Liang, Faisal Mahmood
- **🏷️ 机构**: Mass General Brigham, CMU
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Integrating whole-slide images (WSIs) and bulk transcriptomics for predicting patient survival can improve our understanding of patient prognosis. However, this multimodal task is particularly challenging due to the different nature of these data: WSIs represent a very high-dimensional spatial description of a tumor, while bulk transcriptomics represent a global description of gene expression levels within that tumor. In this context, our work aims to address two key challenges: (1) how can we tokenize transcriptomics in a semantically meaningful and interpretable way?, and (2) how can we capture dense multimodal interactions between these two modalities? Specifically, we propose to learn biological pathway tokens from transcriptomics that can encode specific cellular functions. Together with histology patch tokens that encode the different morphological patterns in the WSI, we argue that they form appropriate reasoning units for downstream interpretability analyses. We propose fusing both modalities using a memory-efficient multimodal Transformer that can model interactions between pathway and histology patch tokens. Our proposed model, SURVPATH, achieves state-of-the-art performance when evaluated against both unimodal and multimodal baselines on five datasets from The Cancer Genome Atlas. Our interpretability framework identifies key multimodal prognostic factors, and, as such, can provide valuable insights into the interaction between genotype and phenotype, enabling a deeper understanding of the underlying biological mechanisms at play. We make our code public at: https://github.com/ajv012/SurvPath.

### DIEM: Decomposition-Integration Enhancing Multimodal Insights.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02578) · 📚 被引 1
- **作者**: Xinyi Jiang, Guoming Wang, Junhao Guo, Juncheng Li, Wenqiao Zhang, Rongxing Lu et al.
- **🏷️ 机构**: Zhejiang University, University of New Brunswick
- **会议**: CVPR 2024

### Hallucination Augmented Contrastive Learning for Multimodal Large Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02553)
- **作者**: Chaoya Jiang, Haiyang Xu, Mengfan Dong, Jiaxing Chen, Wei Ye, Ming Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### MV-Adapter: Multimodal Video Transfer Learning for Video Text Retrieval.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02563) · 📚 被引 26
- **作者**: Xiaojie Jin, Bowen Zhang, Weibo Gong, Kai Xu, Xueqing Deng, Peng Wang et al.
- **🏷️ 机构**: Bytedance Inc., Hefei University of Technology
- **会议**: CVPR 2024

### Modeling Multimodal Social Interactions: New Challenges and Baselines with Densely Aligned Representations.
- **链接**: [arXiv:2403.02090](https://arxiv.org/abs/2403.02090) · 📚 被引 8
- **作者**: Sangmin Lee, Bolin Lai, Fiona Ryan, Bikram Boote, James M. Rehg
- **🏷️ 机构**: University of Illinois Urbana-Champaign, Georgia Institute of Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Understanding social interactions involving both verbal and non-verbal cues is essential for effectively interpreting social situations. However, most prior works on multimodal social cues focus predominantly on single-person behaviors or rely on holistic visual representations that are not aligned to utterances in multi-party environments. Consequently, they are limited in modeling the intricate dynamics of multi-party interactions. In this paper, we introduce three new challenging tasks to model the fine-grained dynamics between multiple people: speaking target identification, pronoun coreference resolution, and mentioned player prediction. We contribute extensive data annotations to curate these new challenges in social deduction game settings. Furthermore, we propose a novel multimodal baseline that leverages densely aligned language-visual representations by synchronizing visual features with their corresponding utterances. This facilitates concurrently capturing verbal and non-verbal cues pertinent to social reasoning. Experiments demonstrate the effectiveness of the proposed approach with densely aligned multimodal representations in modeling fine-grained social interactions. Project website: https://sangmin-git.github.io/projects/MMSI.

### HHMR: Holistic Hand Mesh Recovery by Enhancing the Multimodal Controllability of Graph Diffusion Models.
- **链接**: [arXiv:2406.01334](https://arxiv.org/abs/2406.01334) · 📚 被引 12
- **作者**: Mengcheng Li, Hongwen Zhang, Yuxiang Zhang, Ruizhi Shao, Tao Yu, Yebin Liu
- **🏷️ 机构**: Tsinghua University,Department of Automation, School of Artificial Intelligence, Beijing Normal University, Beijing National Research Center for Information Science and Technology, Tsinghua University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent years have witnessed a trend of the deep integration of the generation and reconstruction paradigms. In this paper, we extend the ability of controllable generative models for a more comprehensive hand mesh recovery task: direct hand mesh generation, inpainting, reconstruction, and fitting in a single framework, which we name as Holistic Hand Mesh Recovery (HHMR). Our key observation is that different kinds of hand mesh recovery tasks can be achieved by a single generative model with strong multimodal controllability, and in such a framework, realizing different tasks only requires giving different signals as conditions. To achieve this goal, we propose an all-in-one diffusion framework based on graph convolution and attention mechanisms for holistic hand mesh recovery. In order to achieve strong control generation capability while ensuring the decoupling of multimodal control signals, we map different modalities to a shared feature space and apply cross-scale random masking in both modality and feature levels. In this way, the correlation between different modalities can be fully exploited during the learning of hand priors. Furthermore, we propose Condition-aligned Gradient Guidance to enhance the alignment of the generated model with the control signals, which significantly improves the accuracy of the hand mesh reconstruction and fitting. Experiments show that our novel framework can realize multiple hand mesh recovery tasks simultaneously and outperform the existing methods in different tasks, which provides more possibilities for subsequent downstream applications including gesture recognition, pose generation, mesh editing, and so on.

### SEED-Bench: Benchmarking Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01263)
- **作者**: Bohao Li, Yuying Ge, Yixiao Ge, Guangzhi Wang, Rui Wang, Ruimao Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### All in One Framework for Multimodal Re-Identification in the Wild.
- **链接**: [arXiv:2405.04741](https://arxiv.org/abs/2405.04741) · 📚 被引 28
- **作者**: He Li, Mang Ye, Ming Zhang, Bo Du
- **🏷️ 机构**: Institute of Artificial Intelligence, School of Computer Science, Wuhan University,National Engineering Research Center for Multimedia Software, Hubei Luojia Laboratory,Wuhan,China, Guangzhou Urban Planning Design Survey Research Institute,Guangzhou,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In Re-identification (ReID), recent advancements yield noteworthy progress in both unimodal and cross-modal retrieval tasks. However, the challenge persists in developing a unified framework that could effectively handle varying multimodal data, including RGB, infrared, sketches, and textual information. Additionally, the emergence of large-scale models shows promising performance in various vision tasks but the foundation model in ReID is still blank. In response to these challenges, a novel multimodal learning paradigm for ReID is introduced, referred to as All-in-One (AIO), which harnesses a frozen pre-trained big model as an encoder, enabling effective multimodal retrieval without additional fine-tuning. The diverse multimodal data in AIO are seamlessly tokenized into a unified space, allowing the modality-shared frozen encoder to extract identity-consistent features comprehensively across all modalities. Furthermore, a meticulously crafted ensemble of cross-modality heads is designed to guide the learning trajectory. AIO is the \textbf{first} framework to perform all-in-one ReID, encompassing four commonly used modalities. Experiments on cross-modal and multimodal ReID reveal that AIO not only adeptly handles various modal data but also excels in challenging contexts, showcasing exceptional performance in zero-shot and domain generalization scenarios.

### Correlation-Decoupled Knowledge Distillation for Multimodal Sentiment Analysis with Incomplete Modalities.
- **链接**: [arXiv:2404.16456](https://arxiv.org/abs/2404.16456) · 📚 被引 57
- **作者**: Mingcheng Li, Dingkang Yang, Xiao Zhao, Shuaibing Wang, Yan Wang, Kun Yang et al.
- **🏷️ 机构**: Academy for Engineering and Technology, Fudan University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multimodal sentiment analysis (MSA) aims to understand human sentiment through multimodal data. Most MSA efforts are based on the assumption of modality completeness. However, in real-world applications, some practical factors cause uncertain modality missingness, which drastically degrades the model's performance. To this end, we propose a Correlation-decoupled Knowledge Distillation (CorrKD) framework for the MSA task under uncertain missing modalities. Specifically, we present a sample-level contrastive distillation mechanism that transfers comprehensive knowledge containing cross-sample correlations to reconstruct missing semantics. Moreover, a category-guided prototype distillation mechanism is introduced to capture cross-category correlations using category prototypes to align feature distributions and generate favorable joint representations. Eventually, we design a response-disentangled consistency distillation strategy to optimize the sentiment decision boundaries of the student network through response disentanglement and mutual information maximization. Comprehensive experiments on three datasets indicate that our framework can achieve favorable improvements compared with several baselines.

### Querying as Prompt: Parameter-Efficient Learning for Multimodal Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02536) · 📚 被引 5
- **作者**: Tian Liang, Jing Huang, Ming Kong, Luyuan Chen, Qiang Zhu
- **🏷️ 机构**: Zhejiang University, Beijing Information Science and Technology University
- **会议**: CVPR 2024

### BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02327)
- **作者**: Siyuan Liang, Mingli Zhu, Aishan Liu, Baoyuan Wu, Xiaochun Cao, Ee-Chien Chang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Multimodal Sense-Informed Forecasting of 3D Human Motions.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00209) · 📚 被引 11
- **作者**: Zhenyu Lou, Qiongjie Cui, Haofan Wang, Xu Tang, Hong Zhou
- **🏷️ 机构**: Zhejiang University, Nanjing University of Science and Technology, Xiaohongshu Inc
- **会议**: CVPR 2024

### Compositional Chain-of-Thought Prompting for Large Multimodal Models.
- **链接**: [arXiv:2311.17076](https://arxiv.org/abs/2311.17076) · [代码](https://github.com/chancharikmitra/CCoT) · 📚 被引 96
- **作者**: Chancharik Mitra, Brandon Huang, Trevor Darrell, Roei Herzig
- **🏷️ 机构**: University of California,Berkeley
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The combination of strong visual backbones and Large Language Model (LLM) reasoning has led to Large Multimodal Models (LMMs) becoming the current standard for a wide range of vision and language (VL) tasks. However, recent research has shown that even the most advanced LMMs still struggle to capture aspects of compositional visual reasoning, such as attributes and relationships between objects. One solution is to utilize scene graphs (SGs)--a formalization of objects and their relations and attributes that has been extensively used as a bridge between the visual and textual domains. Yet, scene graph data requires scene graph annotations, which are expensive to collect and thus not easily scalable. Moreover, finetuning an LMM based on SG data can lead to catastrophic forgetting of the pretraining objective. To overcome this, inspired by chain-of-thought methods, we propose Compositional Chain-of-Thought (CCoT), a novel zero-shot Chain-of-Thought prompting method that utilizes SG representations in order to extract compositional knowledge from an LMM. Specifically, we first generate an SG using the LMM, and then use that SG in the prompt to produce a response. Through extensive experiments, we find that the proposed CCoT approach not only improves LMM performance on several vision and language VL compositional benchmarks but also improves the performance of several popular LMMs on general multimodal benchmarks, without the need for fine-tuning or annotated ground-truth SGs. Code: https://github.com/chancharikmitra/CCoT

### Generate Subgoal Images Before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01327) · 📚 被引 9
- **作者**: Fei Ni, Jianye Hao, Shiguang Wu, Longxin Kou, Jiashun Liu, Yan Zheng et al.
- **🏷️ 机构**: Tianjin University,China, Huawei Noah&#x0027;s Ark Lab,China
- **会议**: CVPR 2024

### Summarize the Past to Predict the Future: Natural Language Descriptions of Context Boost Multimodal Object Interaction Anticipation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01731) · 📚 被引 15
- **作者**: Razvan-George Pasca, Alexey Gavryushin, Muhammad Hamza, Yen-Ling Kuo, Kaichun Mo, Luc Van Gool et al.
- **🏷️ 机构**: ETH Zurich, Univ. of Zurich, Univ. of Virginia
- **会议**: CVPR 2024

### Mirasol3B: A Multimodal Autoregressive Model for Time-Aligned and Contextual Modalities.
- **链接**: [arXiv:2311.05698](https://arxiv.org/abs/2311.05698) · 📚 被引 16
- **作者**: A. J. Piergiovanni, Isaac Noble, Dahun Kim, Michael S. Ryoo, Victor Gomes, Anelia Angelova
- **🏷️ 机构**: Google DeepMind, Google Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > One of the main challenges of multimodal learning is the need to combine heterogeneous modalities (e.g., video, audio, text). For example, video and audio are obtained at much higher rates than text and are roughly aligned in time. They are often not synchronized with text, which comes as a global context, e.g., a title, or a description. Furthermore, video and audio inputs are of much larger volumes, and grow as the video length increases, which naturally requires more compute dedicated to these modalities and makes modeling of long-range dependencies harder. We here decouple the multimodal modeling, dividing it into separate, focused autoregressive models, processing the inputs according to the characteristics of the modalities. We propose a multimodal model, called Mirasol3B, consisting of an autoregressive component for the time-synchronized modalities (audio and video), and an autoregressive component for the context modalities which are not necessarily aligned in time but are still sequential. To address the long-sequences of the video-audio inputs, we propose to further partition the video and audio sequences in consecutive snippets and autoregressively process their representations. To that end, we propose a Combiner mechanism, which models the audio-video information jointly within a timeframe. The Combiner learns to extract audio and video features from raw spatio-temporal signals, and then learns to fuse these features producing compact but expressive representations per snippet. Our approach achieves the state-of-the-art on well established multimodal benchmarks, outperforming much larger models. It effectively addresses the high computational demand of media inputs by both learning compact representations, controlling the sequence length of the audio-video feature representations, and modeling their dependencies in time.

### Sniffer: Multimodal Large Language Model for Explainable Out-of-Context Misinformation Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01240)
- **作者**: Peng Qi, Zehong Yan, Wynne Hsu, Mong-Li Lee
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### MMSum: A Dataset for Multimodal Summarization and Thumbnail Generation of Videos.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02069) · 📚 被引 9
- **作者**: Jielin Qiu, Jiacheng Zhu, William Han, Aditesh Kumar, Karthik Mittal, Claire Jin et al.
- **🏷️ 机构**: Carnegie Mellon University, MIT CSAIL, Microsoft Azure AI
- **会议**: CVPR 2024

### GLaMM: Pixel Grounding Large Multimodal Model.
- **链接**: [arXiv:2311.03356](https://arxiv.org/abs/2311.03356) · 📚 被引 203
- **作者**: Hanoona Abdul Rasheed, Muhammad Maaz, Sahal Shaji Mullappilly, Abdelrahman M. Shaker, Salman H. Khan, Hisham Cholakkal et al.
- **🏷️ 机构**: Mohamed bin Zayed University of AI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large Multimodal Models (LMMs) extend Large Language Models to the vision domain. Initial LMMs used holistic images and text prompts to generate ungrounded textual responses. Recently, region-level LMMs have been used to generate visually grounded responses. However, they are limited to only referring to a single object category at a time, require users to specify the regions, or cannot offer dense pixel-wise object grounding. In this work, we present Grounding LMM (GLaMM), the first model that can generate natural language responses seamlessly intertwined with corresponding object segmentation masks. GLaMM not only grounds objects appearing in the conversations but is flexible enough to accept both textual and optional visual prompts (region of interest) as input. This empowers users to interact with the model at various levels of granularity, both in textual and visual domains. Due to the lack of standard benchmarks for the novel setting of visually Grounded Conversation Generation (GCG), we introduce a comprehensive evaluation protocol with our curated grounded conversations. Our proposed GCG task requires densely grounded concepts in natural scenes at a large-scale. To this end, we propose a densely annotated Grounding-anything Dataset (GranD) using our proposed automated annotation pipeline that encompasses 7.5M unique concepts grounded in a total of 810M regions available with segmentation masks. Besides GCG, GLaMM also performs effectively on several downstream tasks, e.g., referring expression segmentation, image and region-level captioning and vision-language conversations.

### PixelLM: Pixel Reasoning with Large Multimodal Model.
- **链接**: [arXiv:2312.02228](https://arxiv.org/abs/2312.02228) · 📚 被引 81
- **作者**: Zhongwei Ren, Zhicheng Huang, Yunchao Wei, Yao Zhao, Dongmei Fu, Jiashi Feng et al.
- **🏷️ 机构**: Beijing Jiaotong University, University of Science and Technology Beijing, ByteDance Inc.
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > While large multimodal models (LMMs) have achieved remarkable progress, generating pixel-level masks for image reasoning tasks involving multiple open-world targets remains a challenge. To bridge this gap, we introduce PixelLM, an effective and efficient LMM for pixel-level reasoning and understanding. Central to PixelLM is a novel, lightweight pixel decoder and a comprehensive segmentation codebook. The decoder efficiently produces masks from the hidden embeddings of the codebook tokens, which encode detailed target-relevant information. With this design, PixelLM harmonizes with the structure of popular LMMs and avoids the need for additional costly segmentation models. Furthermore, we propose a target refinement loss to enhance the model's ability to differentiate between multiple targets, leading to substantially improved mask quality. To advance research in this area, we construct MUSE, a high-quality multi-target reasoning segmentation benchmark. PixelLM excels across various pixel-level image reasoning and understanding tasks, outperforming well-established methods in multiple benchmarks, including MUSE, single- and multi-referring segmentation. Comprehensive ablations confirm the efficacy of each proposed component. All code, models, and datasets will be publicly available.

### TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01357)
- **作者**: Shuhuai Ren, Linli Yao, Shicheng Li, Xu Sun, Lu Hou
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### OmniVec2 - A Novel Transformer Based Network for Large Scale Multimodal and Multitask Learning.
- **链接**: [arXiv:2507.13364](https://arxiv.org/abs/2507.13364) · 📚 被引 36
- **作者**: Siddharth Srivastava, Gaurav Sharma
- **🏷️ 机构**: Typeface
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present a novel multimodal multitask network and associated training algorithm. The method is capable of ingesting data from approximately 12 different modalities namely image, video, audio, text, depth, point cloud, time series, tabular, graph, X-ray, infrared, IMU, and hyperspectral. The proposed approach utilizes modality specialized tokenizers, a shared transformer architecture, and cross-attention mechanisms to project the data from different modalities into a unified embedding space. It addresses multimodal and multitask scenarios by incorporating modality-specific task heads for different tasks in respective modalities. We propose a novel pretraining strategy with iterative modality switching to initialize the network, and a training algorithm which trades off fully joint training over all modalities, with training on pairs of modalities at a time. We provide comprehensive evaluation across 25 datasets from 12 modalities and show state of the art performances, demonstrating the effectiveness of the proposed architecture, pretraining strategy and adapted multitask training.

### Generative Multimodal Models are In-Context Learners.
- **链接**: [arXiv:2312.13286](https://arxiv.org/abs/2312.13286) · 📚 被引 126
- **作者**: Quan Sun, Yufeng Cui, Xiaosong Zhang, Fan Zhang, Qiying Yu, Yueze Wang et al.
- **🏷️ 机构**: Beijing Academy of Artificial Intelligence, Tsinghua University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The human ability to easily solve multimodal tasks in context (i.e., with only a few demonstrations or simple instructions), is what current multimodal systems have largely struggled to imitate. In this work, we demonstrate that the task-agnostic in-context learning capabilities of large multimodal models can be significantly enhanced by effective scaling-up. We introduce Emu2, a generative multimodal model with 37 billion parameters, trained on large-scale multimodal sequences with a unified autoregressive objective. Emu2 exhibits strong multimodal in-context learning abilities, even emerging to solve tasks that require on-the-fly reasoning, such as visual prompting and object-grounded generation. The model sets a new record on multiple multimodal understanding tasks in few-shot settings. When instruction-tuned to follow specific instructions, Emu2 further achieves new state-of-the-art on challenging tasks such as question answering benchmarks for large multimodal models and open-ended subject-driven generation. These achievements demonstrate that Emu2 can serve as a base model and general-purpose interface for a wide range of multimodal tasks. Code and models are publicly available to facilitate future research.

### Contextual Augmented Global Contrast for Multimodal Intent Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02546) · 📚 被引 32
- **作者**: Kaili Sun, Zhiwen Xie, Mang Ye, Huyin Zhang
- **🏷️ 机构**: School of Computer Science, Wuhan University,Wuhan,China, School of Computer Science, Central China Normal University,Wuhan,China
- **会议**: CVPR 2024

### GlitchBench: Can Large Multimodal Models Detect Video Game Glitches?
- **链接**: [arXiv:2312.05291](https://arxiv.org/abs/2312.05291) · 📚 被引 14
- **作者**: Mohammad Reza Taesiri, Tianjun Feng, Cor-Paul Bezemer, Anh Nguyen
- **🏷️ 机构**: University of Alberta, Auburn University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large multimodal models (LMMs) have evolved from large language models (LLMs) to integrate multiple input modalities, such as visual inputs. This integration augments the capacity of LLMs for tasks requiring visual comprehension and reasoning. However, the extent and limitations of their enhanced abilities are not fully understood, especially when it comes to real-world tasks. To address this gap, we introduce GlitchBench, a novel benchmark derived from video game quality assurance tasks, to test and evaluate the reasoning capabilities of LMMs. Our benchmark is curated from a variety of unusual and glitched scenarios from video games and aims to challenge both the visual and linguistic reasoning powers of LMMs in detecting and interpreting out-of-the-ordinary events. We evaluate multiple state-of-the-art LMMs, and we show that GlitchBench presents a new challenge for these models. Code and data are available at: https://glitchbench.github.io/

### Link-Context Learning for Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02566)
- **作者**: Yan Tai, Weichen Fan, Zhao Zhang, Ziwei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00914)
- **作者**: Shengbang Tong, Zhuang Liu, Yuexiang Zhai, Yi Ma, Yann LeCun, Saining Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Data-Efficient Multimodal Fusion on a Single GPU.
- **链接**: [arXiv:2312.10144](https://arxiv.org/abs/2312.10144) · [代码](https://github.com/layer6ai-labs/fusemix) · 📚 被引 8
- **作者**: Noël Vouitsis, Zhaoyan Liu, Satya Krishna Gorti, Valentin Villecroze, Jesse C. Cresswell, Guangwei Yu et al.
- **🏷️ 机构**: Layer 6 AI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The goal of multimodal alignment is to learn a single latent space that is shared between multimodal inputs. The most powerful models in this space have been trained using massive datasets of paired inputs and large-scale computational resources, making them prohibitively expensive to train in many practical scenarios. We surmise that existing unimodal encoders pre-trained on large amounts of unimodal data should provide an effective bootstrap to create multimodal models from unimodal ones at much lower costs. We therefore propose FuseMix, a multimodal augmentation scheme that operates on the latent spaces of arbitrary pre-trained unimodal encoders. Using FuseMix for multimodal alignment, we achieve competitive performance -- and in certain cases outperform state-of-the art methods -- in both image-text and audio-text retrieval, with orders of magnitude less compute and data: for example, we outperform CLIP on the Flickr30K text-to-image retrieval task with $\sim \! 600\times$ fewer GPU days and $\sim \! 80\times$ fewer image-text pairs. Additionally, we show how our method can be applied to convert pre-trained text-to-image generative models into audio-to-image ones. Code is available at: https://github.com/layer6ai-labs/fusemix.

### Polos: Multimodal Metric Learning from Human Feedback for Image Captioning.
- **链接**: [arXiv:2402.18091](https://arxiv.org/abs/2402.18091) · 📚 被引 19
- **作者**: Yuiga Wada, Kanta Kaneda, Daichi Saito, Komei Sugiura
- **🏷️ 机构**: Keio University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Establishing an automatic evaluation metric that closely aligns with human judgments is essential for effectively developing image captioning models. Recent data-driven metrics have demonstrated a stronger correlation with human judgments than classic metrics such as CIDEr; however they lack sufficient capabilities to handle hallucinations and generalize across diverse images and texts partially because they compute scalar similarities merely using embeddings learned from tasks unrelated to image captioning evaluation. In this study, we propose Polos, a supervised automatic evaluation metric for image captioning models. Polos computes scores from multimodal inputs, using a parallel feature extraction mechanism that leverages embeddings trained through large-scale contrastive learning. To train Polos, we introduce Multimodal Metric Learning from Human Feedback (M$^2$LHF), a framework for developing metrics based on human feedback. We constructed the Polaris dataset, which comprises 131K human judgments from 550 evaluators, which is approximately ten times larger than standard datasets. Our approach achieved state-of-the-art performance on Composite, Flickr8K-Expert, Flickr8K-CF, PASCAL-50S, FOIL, and the Polaris dataset, thereby demonstrating its effectiveness and robustness.

### Cloud-Device Collaborative Learning for Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01202)
- **作者**: Guanqun Wang, Jiaming Liu, Chenxuan Li, Yuan Zhang, Junpeng Ma, Xinyu Wei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### Enhancing Multimodal Cooperation via Sample-Level Modality Valuation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02581) · 📚 被引 36
- **作者**: Yake Wei, Ruoxuan Feng, Zihe Wang, Di Hu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing
- **会议**: CVPR 2024

### Omni-SMoLA: Boosting Generalist Multimodal Models with Soft Mixture of Low-Rank Experts.
- **链接**: [arXiv:2312.00968](https://arxiv.org/abs/2312.00968) · 📚 被引 16
- **作者**: Jialin Wu, Xia Hu, Yaqing Wang, Bo Pang, Radu Soricut
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large multi-modal models (LMMs) exhibit remarkable performance across numerous tasks. However, generalist LMMs often suffer from performance degradation when tuned over a large collection of tasks. Recent research suggests that Mixture of Experts (MoE) architectures are useful for instruction tuning, but for LMMs of parameter size around O(50-100B), the prohibitive cost of replicating and storing the expert models severely limits the number of experts we can use. We propose Omni-SMoLA, an architecture that uses the Soft MoE approach to (softly) mix many multimodal low rank experts, and avoids introducing a significant number of new parameters compared to conventional MoE models. The core intuition here is that the large model provides a foundational backbone, while different lightweight experts residually learn specialized knowledge, either per-modality or multimodally. Extensive experiments demonstrate that the SMoLA approach helps improve the generalist performance across a broad range of generative vision-and-language tasks, achieving new SoTA generalist performance that often matches or outperforms single specialized LMM baselines, as well as new SoTA specialist performance.

### Towards Language-Driven Video Inpainting via Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01188)
- **作者**: Jianzong Wu, Xiangtai Li, Chenyang Si, Shangchen Zhou, Jingkang Yang, Jiangning Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01243)
- **作者**: Penghao Wu, Saining Xie
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### GSVA: Generalized Segmentation via Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00370)
- **作者**: Zhuofan Xia, Dongchen Han, Yizeng Han, Xuran Pan, Shiji Song, Gao Huang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### ULIP-2: Towards Scalable Multimodal Pre-Training for 3D Understanding.
- **链接**: [arXiv:2305.08275](https://arxiv.org/abs/2305.08275) · [代码](https://github.com/salesforce/ULIP) · 📚 被引 110
- **作者**: Le Xue, Ning Yu, Shu Zhang, Artemis Panagopoulou, Junnan Li, Roberto Martín-Martín et al.
- **🏷️ 机构**: Salesforce AI Research, University of Texas at Austin, Stanford University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advancements in multimodal pre-training have shown promising efficacy in 3D representation learning by aligning multimodal features across 3D shapes, their 2D counterparts, and language descriptions. However, the methods used by existing frameworks to curate such multimodal data, in particular language descriptions for 3D shapes, are not scalable, and the collected language descriptions are not diverse. To address this, we introduce ULIP-2, a simple yet effective tri-modal pre-training framework that leverages large multimodal models to automatically generate holistic language descriptions for 3D shapes. It only needs 3D data as input, eliminating the need for any manual 3D annotations, and is therefore scalable to large datasets. ULIP-2 is also equipped with scaled-up backbones for better multimodal representation learning. We conduct experiments on two large-scale 3D datasets, Objaverse and ShapeNet, and augment them with tri-modal datasets of 3D point clouds, images, and language for training ULIP-2. Experiments show that ULIP-2 demonstrates substantial benefits in three downstream tasks: zero-shot 3D classification, standard 3D classification with fine-tuning, and 3D captioning (3D-to-language generation). It achieves a new SOTA of 50.6% (top-1) on Objaverse-LVIS and 84.7% (top-1) on ModelNet40 in zero-shot classification. In the ScanObjectNN benchmark for standard fine-tuning, ULIP-2 reaches an overall accuracy of 91.5% with a compact model of only 1.4 million parameters. ULIP-2 sheds light on a new paradigm for scalable multimodal 3D representation learning without human annotations and shows significant improvements over existing baselines. The code and datasets are released at https://github.com/salesforce/ULIP.

### RELI11D: A Comprehensive Multimodal Human Motion Dataset and Method.
- **链接**: [arXiv:2403.19501](https://arxiv.org/abs/2403.19501) · 📚 被引 10
- **作者**: Ming Yan, Yan Zhang, Shuqiang Cai, Shuqi Fan, Xincheng Lin, Yudi Dai et al.
- **🏷️ 机构**: Fujian Key Laboratory of Sensing and Computing for Smart Cities, Xiamen University, Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Ministry of Education of China, School of Informatics, Xiamen University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Comprehensive capturing of human motions requires both accurate captures of complex poses and precise localization of the human within scenes. Most of the HPE datasets and methods primarily rely on RGB, LiDAR, or IMU data. However, solely using these modalities or a combination of them may not be adequate for HPE, particularly for complex and fast movements. For holistic human motion understanding, we present RELI11D, a high-quality multimodal human motion dataset involves LiDAR, IMU system, RGB camera, and Event camera. It records the motions of 10 actors performing 5 sports in 7 scenes, including 3.32 hours of synchronized LiDAR point clouds, IMU measurement data, RGB videos and Event steams. Through extensive experiments, we demonstrate that the RELI11D presents considerable challenges and opportunities as it contains many rapid and complex motions that require precise location. To address the challenge of integrating different modalities, we propose LEIR, a multimodal baseline that effectively utilizes LiDAR Point Cloud, Event stream, and RGB through our cross-attention fusion strategy. We show that LEIR exhibits promising results for rapid motions and daily motions and that utilizing the characteristics of multiple modalities can indeed improve HPE performance. Both the dataset and source code will be released publicly to the research community, fostering collaboration and enabling further exploration in this field.

### MMA-Diffusion: MultiModal Attack on Diffusion Models.
- **链接**: [arXiv:2311.17516](https://arxiv.org/abs/2311.17516) · 📚 被引 59
- **作者**: Yijun Yang, Ruiyuan Gao, Xiaosen Wang, Tsung-Yi Ho, Nan Xu, Qiang Xu
- **🏷️ 机构**: The Chinese University of Hong Kong, Huawei Singular Security Lab, Institute of Automation, Chinese Academy of Sciences
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In recent years, Text-to-Image (T2I) models have seen remarkable advancements, gaining widespread adoption. However, this progress has inadvertently opened avenues for potential misuse, particularly in generating inappropriate or Not-Safe-For-Work (NSFW) content. Our work introduces MMA-Diffusion, a framework that presents a significant and realistic threat to the security of T2I models by effectively circumventing current defensive measures in both open-source models and commercial online services. Unlike previous approaches, MMA-Diffusion leverages both textual and visual modalities to bypass safeguards like prompt filters and post-hoc safety checkers, thus exposing and highlighting the vulnerabilities in existing defense mechanisms.

### Binding Touch to Everything: Learning Unified Multimodal Tactile Representations.
- **链接**: [arXiv:2401.18084](https://arxiv.org/abs/2401.18084) · 📚 被引 59
- **作者**: Fengyu Yang, Chao Feng, Ziyang Chen, Hyoungseob Park, Daniel Wang, Yiming Dou et al.
- **🏷️ 机构**: Yale University, University of Michigan
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The ability to associate touch with other modalities has huge implications for humans and computational systems. However, multimodal learning with touch remains challenging due to the expensive data collection process and non-standardized sensor outputs. We introduce UniTouch, a unified tactile model for vision-based touch sensors connected to multiple modalities, including vision, language, and sound. We achieve this by aligning our UniTouch embeddings to pretrained image embeddings already associated with a variety of other modalities. We further propose learnable sensor-specific tokens, allowing the model to learn from a set of heterogeneous tactile sensors, all at the same time. UniTouch is capable of conducting various touch sensing tasks in the zero-shot setting, from robot grasping prediction to touch image question answering. To the best of our knowledge, UniTouch is the first to demonstrate such capabilities. Project page: https://cfeng16.github.io/UniTouch/

### Narrative Action Evaluation with Prompt-Guided Multimodal Interaction.
- **链接**: [arXiv:2404.14471](https://arxiv.org/abs/2404.14471) · [代码](https://github.com/shiyi-zh0408/NAE_CVPR2024) · 📚 被引 17
- **作者**: Shiyi Zhang, Sule Bai, Guangyi Chen, Lei Chen, Jiwen Lu, Junle Wang et al.
- **🏷️ 机构**: Shenzhen International Graduate School, Tsinghua University, Carnegie Mellon University,Pittsburgh,PA,USA, Tsinghua University,Department of Automation
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this paper, we investigate a new problem called narrative action evaluation (NAE). NAE aims to generate professional commentary that evaluates the execution of an action. Unlike traditional tasks such as score-based action quality assessment and video captioning involving superficial sentences, NAE focuses on creating detailed narratives in natural language. These narratives provide intricate descriptions of actions along with objective evaluations. NAE is a more challenging task because it requires both narrative flexibility and evaluation rigor. One existing possible solution is to use multi-task learning, where narrative language and evaluative information are predicted separately. However, this approach results in reduced performance for individual tasks because of variations between tasks and differences in modality between language information and evaluation information. To address this, we propose a prompt-guided multimodal interaction framework. This framework utilizes a pair of transformers to facilitate the interaction between different modalities of information. It also uses prompts to transform the score regression task into a video-text matching task, thus enabling task interactivity. To support further research in this field, we re-annotate the MTL-AQA and FineGym datasets with high-quality and comprehensive action narration. Additionally, we establish benchmarks for NAE. Extensive experiment results prove that our method outperforms separate learning methods and naive multi-task learning methods. Data and code are released at https://github.com/shiyi-zh0408/NAE_CVPR2024.

### Multimodal Pathway: Improve Transformers with Irrelevant Data from Other Modalities.
- **链接**: [arXiv:2401.14405](https://arxiv.org/abs/2401.14405) · [代码](https://github.com/AILab-CVC/M2PT) · 📚 被引 8
- **作者**: Yiyuan Zhang, Xiaohan Ding, Kaixiong Gong, Yixiao Ge, Ying Shan, Xiangyu Yue
- **🏷️ 机构**: The Chinese University of Hong Kong,MMLab, Tencent AI Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We propose to improve transformers of a specific modality with irrelevant data from other modalities, e.g., improve an ImageNet model with audio or point cloud datasets. We would like to highlight that the data samples of the target modality are irrelevant to the other modalities, which distinguishes our method from other works utilizing paired (e.g., CLIP) or interleaved data of different modalities. We propose a methodology named Multimodal Pathway - given a target modality and a transformer designed for it, we use an auxiliary transformer trained with data of another modality and construct pathways to connect components of the two models so that data of the target modality can be processed by both models. In this way, we utilize the universal sequence-to-sequence modeling abilities of transformers obtained from two modalities. As a concrete implementation, we use a modality-specific tokenizer and task-specific head as usual but utilize the transformer blocks of the auxiliary model via a proposed method named Cross-Modal Re-parameterization, which exploits the auxiliary weights without any inference costs. On the image, point cloud, video, and audio recognition tasks, we observe significant and consistent performance improvements with irrelevant data from other modalities. The code and models are available at https://github.com/AILab-CVC/M2PT.

### Exploring the Transferability of Visual Prompting for Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02508)
- **作者**: Yichi Zhang, Yinpeng Dong, Siyuan Zhang, Tianzan Min, Hang Su, Jun Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### C3Net: Compound Conditioned ControlNet for Multimodal Content Generation.
- **链接**: [arXiv:2311.17951](https://arxiv.org/abs/2311.17951) · 📚 被引 6
- **作者**: Juntao Zhang, Yuehuai Liu, Yu-Wing Tai, Chi-Keung Tang
- **🏷️ 机构**: HKUST, Dartmouth College
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present Compound Conditioned ControlNet, C3Net, a novel generative neural architecture taking conditions from multiple modalities and synthesizing multimodal contents simultaneously (e.g., image, text, audio). C3Net adapts the ControlNet architecture to jointly train and make inferences on a production-ready diffusion model and its trainable copies. Specifically, C3Net first aligns the conditions from multi-modalities to the same semantic latent space using modality-specific encoders based on contrastive training. Then, it generates multimodal outputs based on the aligned latent space, whose semantic information is combined using a ControlNet-like architecture called Control C3-UNet. Correspondingly, with this system design, our model offers an improved solution for joint-modality generation through learning and explaining multimodal conditions instead of simply taking linear interpolations on the latent space. Meanwhile, as we align conditions to a unified latent space, C3Net only requires one trainable Control C3-UNet to work on multimodal semantic information. Furthermore, our model employs unimodal pretraining on the condition alignment stage, outperforming the non-pretrained alignment even on relatively scarce training data and thus demonstrating high-quality compound condition generation. We contribute the first high-quality tri-modal validation set to validate quantitatively that C3Net outperforms or is on par with first and contemporary state-of-the-art multimodal generation. Our codes and tri-modal dataset will be released.

### MM-Narrator: Narrating Long-form Videos with Multimodal In-Context Learning.
- **链接**: [arXiv:2311.17435](https://arxiv.org/abs/2311.17435) · 📚 被引 26
- **作者**: Chaoyi Zhang, Kevin Lin, Zhengyuan Yang, Jianfeng Wang, Linjie Li, Chung-Ching Lin et al.
- **🏷️ 机构**: University of Sydney, Microsoft, Advanced Micro Devices
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present MM-Narrator, a novel system leveraging GPT-4 with multimodal in-context learning for the generation of audio descriptions (AD). Unlike previous methods that primarily focused on downstream fine-tuning with short video clips, MM-Narrator excels in generating precise audio descriptions for videos of extensive lengths, even beyond hours, in an autoregressive manner. This capability is made possible by the proposed memory-augmented generation process, which effectively utilizes both the short-term textual context and long-term visual memory through an efficient register-and-recall mechanism. These contextual memories compile pertinent past information, including storylines and character identities, ensuring an accurate tracking and depicting of story-coherent and character-centric audio descriptions. Maintaining the training-free design of MM-Narrator, we further propose a complexity-based demonstration selection strategy to largely enhance its multi-step reasoning capability via few-shot multimodal in-context learning (MM-ICL). Experimental results on MAD-eval dataset demonstrate that MM-Narrator consistently outperforms both the existing fine-tuning-based approaches and LLM-based approaches in most scenarios, as measured by standard evaluation metrics. Additionally, we introduce the first segment-based evaluator for recurrent text generation. Empowered by GPT-4, this evaluator comprehensively reasons and marks AD generation performance in various extendable dimensions.

### MMVP: A Multimodal MoCap Dataset with Vision and Pressure Sensors.
- **链接**: [arXiv:2403.17610](https://arxiv.org/abs/2403.17610) · 📚 被引 12
- **作者**: He Zhang, Shenghao Ren, Haolei Yuan, Jianhui Zhao, Fan Li, Shuangpeng Sun et al.
- **🏷️ 机构**: Beihang University, Nanjing University, Tsinghua University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Foot contact is an important cue for human motion capture, understanding, and generation. Existing datasets tend to annotate dense foot contact using visual matching with thresholding or incorporating pressure signals. However, these approaches either suffer from low accuracy or are only designed for small-range and slow motion. There is still a lack of a vision-pressure multimodal dataset with large-range and fast human motion, as well as accurate and dense foot-contact annotation. To fill this gap, we propose a Multimodal MoCap Dataset with Vision and Pressure sensors, named MMVP. MMVP provides accurate and dense plantar pressure signals synchronized with RGBD observations, which is especially useful for both plausible shape estimation, robust pose fitting without foot drifting, and accurate global translation tracking. To validate the dataset, we propose an RGBD-P SMPL fitting method and also a monocular-video-based baseline framework, VP-MoCap, for human motion capture. Experiments demonstrate that our RGBD-P SMPL Fitting results significantly outperform pure visual motion capture. Moreover, VP-MoCap outperforms SOTA methods in foot-contact and global translation estimation accuracy. We believe the configuration of the dataset and the baseline frameworks will stimulate the research in this direction and also provide a good reference for MoCap applications in various domains. Project page: https://metaverse-ai-lab-thu.github.io/MMVP-Dataset/.

### TRINS: Towards Multimodal Language Models that Can Read.
- **链接**: [arXiv:2406.06730](https://arxiv.org/abs/2406.06730) · 📚 被引 1
- **作者**: Ruiyi Zhang, Yanzhe Zhang, Jian Chen, Yufan Zhou, Jiuxiang Gu, Changyou Chen et al.
- **🏷️ 机构**: Adobe Research, Georgia Institute of Technology, State University of New York at Buffalo
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large multimodal language models have shown remarkable proficiency in understanding and editing images. However, a majority of these visually-tuned models struggle to comprehend the textual content embedded in images, primarily due to the limitation of training data. In this work, we introduce TRINS: a Text-Rich image INStruction dataset, with the objective of enhancing the reading ability of the multimodal large language model. TRINS is built upon LAION using hybrid data annotation strategies that include machine-assisted and human-assisted annotation processes. It contains 39,153 text-rich images, captions, and 102,437 questions. Specifically, we show that the number of words per annotation in TRINS is significantly longer than that of related datasets, providing new challenges. Furthermore, we introduce a simple and effective architecture, called a Language-vision Reading Assistant (LaRA), which is good at understanding textual content within images. LaRA outperforms existing state-of-the-art multimodal large language models on the TRINS dataset, as well as other classical benchmarks. Lastly, we conducted a comprehensive evaluation with TRINS on various text-rich image understanding and generation tasks, demonstrating its effectiveness.

### Continual Self-Supervised Learning: Towards Universal Multi-Modal Medical Data Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01057)
- **作者**: Yiwen Ye, Yutong Xie, Jianpeng Zhang, Ziyang Chen, Qi Wu, Yong Xia
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### ES3: Evolving Self-Supervised Learning of Robust Audio-Visual Speech Representations.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02556)
- **作者**: Yuanhang Zhang, Shuang Yang, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### TIM: A Time Interval Machine for Audio-Visual Action Recognition.
- **链接**: [arXiv:2404.05559](https://arxiv.org/abs/2404.05559) · [代码](https://github.com/JacobChalk/TIM) · 📚 被引 29
- **作者**: Jacob Chalk, Jaesung Huh, Evangelos Kazakos, Andrew Zisserman, Dima Damen
- **🏷️ 机构**: University of Bristol, University of Oxford,VGG, Czech Technical University in Prague
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Diverse actions give rise to rich audio-visual signals in long videos. Recent works showcase that the two modalities of audio and video exhibit different temporal extents of events and distinct labels. We address the interplay between the two modalities in long videos by explicitly modelling the temporal extents of audio and visual events. We propose the Time Interval Machine (TIM) where a modality-specific time interval poses as a query to a transformer encoder that ingests a long video input. The encoder then attends to the specified interval, as well as the surrounding context in both modalities, in order to recognise the ongoing action. We test TIM on three long audio-visual video datasets: EPIC-KITCHENS, Perception Test, and AVE, reporting state-of-the-art (SOTA) for recognition. On EPIC-KITCHENS, we beat previous SOTA that utilises LLMs and significantly larger pre-training by 2.9% top-1 action recognition accuracy. Additionally, we show that TIM can be adapted for action detection, using dense multi-scale interval queries, outperforming SOTA on EPIC-KITCHENS-100 for most metrics, and showing strong performance on the Perception Test. Our ablations show the critical role of integrating the two modalities and modelling their time intervals in achieving this performance. Code and models at: https://github.com/JacobChalk/TIM

### C2KD: Bridging the Modality Gap for Cross-Modal Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01515)
- **作者**: Fushuo Huo, Wenchao Xu, Jingcai Guo, Haozhao Wang, Song Guo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Holistic Autonomous Driving Understanding by Bird'View Injected Multi-Modal Large Models. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
