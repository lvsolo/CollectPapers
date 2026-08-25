# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 78 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Generalized Few-shot 3D Point Cloud Segmentation with Vision-Language Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/An_Generalized_Few-shot_3D_Point_Cloud_Segmentation_with_Vision-Language_Model_CVPR_2025_paper.html)
- **作者**: Zhaochong An, Guolei Sun, Yun Liu, Runjia Li, Junlin Han, Ender Konukoglu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### ProxyTransformation: Preshaping Point Cloud Manifold With Proxy Attention For 3D Visual Grounding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_ProxyTransformation_Preshaping_Point_Cloud_Manifold_With_Proxy_Attention_For_3D_CVPR_2025_paper.html)
- **作者**: Qihang Peng, Henry Zheng, Gao Huang
- **🏷️ 机构**: Tsinghua University
- **会议**: CVPR 2025

### AA-CLIP: Enhancing Zero-Shot Anomaly Detection via Anomaly-Aware CLIP.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_AA-CLIP_Enhancing_Zero-Shot_Anomaly_Detection_via_Anomaly-Aware_CLIP_CVPR_2025_paper.html)
- **作者**: Wenxin Ma, Xu Zhang, Qingsong Yao, Fenghe Tang, Chenxu Wu, Yingtai Li et al.
- **🏷️ 机构**: USTC,School of Biomedical Engineering, Division of Life Sciences and Medicine, Stanford University
- **会议**: CVPR 2025

### HoVLE: Unleashing the Power of Monolithic Vision-Language Models with Holistic Vision-Language Embedding.
- **链接**: [arXiv:2412.16158](https://arxiv.org/abs/2412.16158) · 📚 被引 2
- **作者**: Chenxin Tao, Shiqian Su, Xizhou Zhu, Chenyu Zhang, Zhe Chen, Jiawen Liu et al.
- **🏷️ 机构**: Tsinghua University, Nanjing University, Johns Hopkins University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The rapid advance of Large Language Models (LLMs) has catalyzed the development of Vision-Language Models (VLMs). Monolithic VLMs, which avoid modality-specific encoders, offer a promising alternative to the compositional ones but face the challenge of inferior performance. Most existing monolithic VLMs require tuning pre-trained LLMs to acquire vision abilities, which may degrade their language capabilities. To address this dilemma, this paper presents a novel high-performance monolithic VLM named HoVLE. We note that LLMs have been shown capable of interpreting images, when image embeddings are aligned with text embeddings. The challenge for current monolithic VLMs actually lies in the lack of a holistic embedding module for both vision and language inputs. Therefore, HoVLE introduces a holistic embedding module that converts visual and textual inputs into a shared space, allowing LLMs to process images in the same way as texts. Furthermore, a multi-stage training strategy is carefully designed to empower the holistic embedding module. It is first trained to distill visual features from a pre-trained vision encoder and text embeddings from the LLM, enabling large-scale training with unpaired random images and text tokens. The whole model further undergoes next-token prediction on multi-modal data to align the embeddings. Finally, an instruction-tuning stage is incorporated. Our experiments show that HoVLE achieves performance close to leading compositional models on various benchmarks, outperforming previous monolithic models by a large margin. Model available at https://huggingface.co/OpenGVLab/HoVLE.

### Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion.
- **链接**: [arXiv:2412.04424](https://arxiv.org/abs/2412.04424) · [代码](https://github.com/JiuhaiChen/Florence-VL)
- **作者**: Jiuhai Chen, Jianwei Yang, Haiping Wu, Dianqi Li, Jianfeng Gao, Tianyi Zhou et al.
- **🏷️ 机构**: University of Maryland, Microsoft Research
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > We present Florence-VL, a new family of multimodal large language models (MLLMs) with enriched visual representations produced by Florence-2, a generative vision foundation model. Unlike the widely used CLIP-style vision transformer trained by contrastive learning, Florence-2 can capture different levels and aspects of visual features, which are more versatile to be adapted to diverse downstream tasks. We propose a novel feature-fusion architecture and an innovative training recipe that effectively integrates Florence-2's visual features into pretrained LLMs, such as Phi 3.5 and LLama 3. In particular, we propose "depth-breath fusion (DBFusion)" to fuse the visual features extracted from different depths and under multiple prompts. Our model training is composed of end-to-end pretraining of the whole model followed by finetuning of the projection layer and the LLM, on a carefully designed recipe of diverse open-source datasets that include high-quality image captions and instruction-tuning pairs. Our quantitative analysis and visualization of Florence-VL's visual features show its advantages over popular vision encoders on vision-language alignment, where the enriched depth and breath play important roles. Florence-VL achieves significant improvements over existing state-of-the-art MLLMs across various multi-modal and vision-centric benchmarks covering general VQA, perception, hallucination, OCR, Chart, knowledge-intensive understanding, etc. To facilitate future research, our models and the complete training recipe are open-sourced. https://github.com/JiuhaiChen/Florence-VL

### Words or Vision: Do Vision-Language Models Have Blind Faith in Text?
- **链接**: [arXiv:2503.02199](https://arxiv.org/abs/2503.02199)
- **作者**: Ailin Deng, Tri Cao, Zhirui Chen, Bryan Hooi
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Vision-Language Models (VLMs) excel in integrating visual and textual information for vision-centric tasks, but their handling of inconsistencies between modalities is underexplored. We investigate VLMs' modality preferences when faced with visual data and varied textual inputs in vision-centered settings. By introducing textual variations to four vision-centric tasks and evaluating ten Vision-Language Models (VLMs), we discover a \emph{``blind faith in text''} phenomenon: VLMs disproportionately trust textual data over visual data when inconsistencies arise, leading to significant performance drops under corrupted text and raising safety concerns. We analyze factors influencing this text bias, including instruction prompts, language model size, text relevance, token order, and the interplay between visual and textual certainty. While certain factors, such as scaling up the language model size, slightly mitigate text bias, others like token order can exacerbate it due to positional biases inherited from language models. To address this issue, we explore supervised fine-tuning with text augmentation and demonstrate its effectiveness in reducing text bias. Additionally, we provide a theoretical analysis suggesting that the blind faith in text phenomenon may stem from an imbalance of pure text and multi-modal data during training. Our findings highlight the need for balanced training and careful consideration of modality interactions in VLMs to enhance their robustness and reliability in handling multi-modal data inconsistencies.

### What's in the Image? A Deep-Dive into the Vision of Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kaduri_Whats_in_the_Image_A_Deep-Dive_into_the_Vision_of_CVPR_2025_paper.html)
- **作者**: Omri Kaduri, Shai Bagon, Tali Dekel
- **🏷️ 机构**: Weizmann Institute of Science
- **会议**: CVPR 2025

### Seeing the Abstract: Translating the Abstract Language for Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Talon_Seeing_the_Abstract_Translating_the_Abstract_Language_for_Vision_Language_CVPR_2025_paper.html)
- **作者**: Davide Talon, Federico Girella, Ziyue Liu, Marco Cristani, Yiming Wang
- **🏷️ 机构**: Fondazione Bruno Kessler, University of Verona
- **会议**: CVPR 2025

### FastVLM: Efficient Vision Encoding for Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Vasu_FastVLM_Efficient_Vision_Encoding_for_Vision_Language_Models_CVPR_2025_paper.html)
- **作者**: Pavan Kumar Anasosalu Vasu, Fartash Faghri, Chun-Liang Li, Cem Koc, Nate True, Albert Antony et al.
- **🏷️ 机构**: Apple
- **会议**: CVPR 2025

### VisionZip: Longer is Better but Not Necessary in Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_VisionZip_Longer_is_Better_but_Not_Necessary_in_Vision_Language_CVPR_2025_paper.html) · 📚 被引 44
- **作者**: Senqiao Yang, Yukang Chen, Zhuotao Tian, Chengyao Wang, Jingyao Li, Bei Yu et al.
- **🏷️ 机构**: CUHK, HITSZ
- **会议**: CVPR 2025

### Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Mamba_as_a_Bridge_Where_Vision_Foundation_Models_Meet_Vision_CVPR_2025_paper.html)
- **作者**: Xin Zhang, Robby T. Tan
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2025

### ICT: Image-Object Cross-Level Trusted Intervention for Mitigating Object Hallucination in Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ICT_Image-Object_Cross-Level_Trusted_Intervention_for_Mitigating_Object_Hallucination_in_CVPR_2025_paper.html)
- **作者**: Junzhe Chen, Tianshu Zhang, Shiyu Huang, Yuwei Niu, Linfeng Zhang, Lijie Wen et al.
- **🏷️ 机构**: Tsinghua University, Zhipu AI, Chongqing University
- **会议**: CVPR 2025

### Skip Tuning: Pre-trained Vision-Language Models are Effective and Efficient Adapters Themselves.
- **链接**: [arXiv:2412.11509](https://arxiv.org/abs/2412.11509) · [代码](https://github.com/Koorye/SkipTuning)
- **作者**: Shihan Wu, Ji Zhang, Pengpeng Zeng, Lianli Gao, Jingkuan Song, Heng Tao Shen
- **🏷️ 机构**: University of Electronic Science and Technology of China (UESTC), Southwest Jiaotong University, UESTC,Shenzhen Institute for Advanced Study
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Prompt tuning (PT) has long been recognized as an effective and efficient paradigm for transferring large pre-trained vision-language models (VLMs) to downstream tasks by learning a tiny set of context vectors. Nevertheless, in this work, we reveal that freezing the parameters of VLMs during learning the context vectors neither facilitates the transferability of pre-trained knowledge nor improves the memory and time efficiency significantly. Upon further investigation, we find that reducing both the length and width of the feature-gradient propagation flows of the full fine-tuning (FT) baseline is key to achieving effective and efficient knowledge transfer. Motivated by this, we propose Skip Tuning, a novel paradigm for adapting VLMs to downstream tasks. Unlike existing PT or adapter-based methods, Skip Tuning applies Layer-wise Skipping (LSkip) and Class-wise Skipping (CSkip) upon the FT baseline without introducing extra context vectors or adapter modules. Extensive experiments across a wide spectrum of benchmarks demonstrate the superior effectiveness and efficiency of our Skip Tuning over both PT and adapter-based methods. Code: https://github.com/Koorye/SkipTuning.

### Reproducible Vision-Language Models Meet Concepts Out of Pre-Training.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Reproducible_Vision-Language_Models_Meet_Concepts_Out_of_Pre-Training_CVPR_2025_paper.html)
- **作者**: Ziliang Chen, Xin Huang, Xiaoxuan Fan, Keze Wang, Yuyu Zhou, Quanlong Guan et al.
- **🏷️ 机构**: Research Institute of Multiple Agents and Embodied Intelligence,Peng Cheng Laboratory, Sun Yat-sen University, Jinan University
- **会议**: CVPR 2025

### Nullu: Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection.
- **链接**: [arXiv:2412.13817](https://arxiv.org/abs/2412.13817) · [代码](https://github.com/Ziwei-Zheng/Nullu)
- **作者**: Le Yang, Ziwei Zheng, Boxu Chen, Zhengyu Zhao, Chenhao Lin, Chao Shen
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,Xi&#x2019;an,China,710049
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Recent studies have shown that large vision-language models (LVLMs) often suffer from the issue of object hallucinations (OH). To mitigate this issue, we introduce an efficient method that edits the model weights based on an unsafe subspace, which we call HalluSpace in this paper. With truthful and hallucinated text prompts accompanying the visual content as inputs, the HalluSpace can be identified by extracting the hallucinated embedding features and removing the truthful representations in LVLMs. By orthogonalizing the model weights, input features will be projected into the Null space of the HalluSpace to reduce OH, based on which we name our method Nullu. We reveal that HalluSpaces generally contain prior information in the large language models (LLMs) applied to build LVLMs, which have been shown as essential causes of OH in previous studies. Therefore, null space projection suppresses the LLMs' priors to filter out the hallucinated features, resulting in contextually accurate outputs. Experiments show that our method can effectively mitigate OH across different LVLM families without extra inference costs and also show strong performance in general LVLM benchmarks. Code is released at https://github.com/Ziwei-Zheng/Nullu.

### Evaluating Vision-Language Models as Evaluators in Path Planning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Aghzal_Evaluating_Vision-Language_Models_as_Evaluators_in_Path_Planning_CVPR_2025_paper.html)
- **作者**: Mohamed Aghzal, Xiang Yue, Erion Plaku, Ziyu Yao
- **🏷️ 机构**: George Mason University, Carnegie Mellon University, National Science Foundation
- **会议**: CVPR 2025

### Vision-Language Models Do Not Understand Negation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Alhamoud_Vision-Language_Models_Do_Not_Understand_Negation_CVPR_2025_paper.html)
- **作者**: Kumail Alhamoud, Shaden Alshammari, Yonglong Tian, Guohao Li, Philip H. S. Torr, Yoon Kim et al.
- **🏷️ 机构**: MIT, OpenAI, University of Oxford
- **会议**: CVPR 2025

### Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/An_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_with_Assembly_of_CVPR_2025_paper.html)
- **作者**: Wenbin An, Feng Tian, Sicong Leng, Jiahao Nie, Haonan Lin, Qianying Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, Nanyang Technological University, Lenovo Research
- **会议**: CVPR 2025

### ProKeR: A Kernel Perspective on Few-Shot Adaptation of Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Bendou_ProKeR_A_Kernel_Perspective_on_Few-Shot_Adaptation_of_Large_Vision-Language_CVPR_2025_paper.html)
- **作者**: Yassir Bendou, Amine Ouasfi, Vincent Gripon, Adnane Boukhayma
- **🏷️ 机构**: IMT Atlantique,Brest,France, Inria, University Rennes, IRISA, CNRS
- **会议**: CVPR 2025

### Not Only Text: Exploring Compositionality of Visual Representations in Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Berasi_Not_Only_Text_Exploring_Compositionality_of_Visual_Representations_in_Vision-Language_CVPR_2025_paper.html)
- **作者**: Davide Berasi, Matteo Farina, Massimiliano Mancini, Elisa Ricci, Nicola Strisciuglio
- **🏷️ 机构**: Fondazione Bruno Kessler, University of Trento, University of Twente
- **会议**: CVPR 2025

### SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Cao_SceneTAP_Scene-Coherent_Typographic_Adversarial_Planner_against_Vision-Language_Models_in_Real-World_CVPR_2025_paper.html)
- **作者**: Yue Cao, Yun Xing, Jie Zhang, Di Lin, Tianwei Zhang, Ivor W. Tsang et al.
- **🏷️ 机构**: Agency for Science, Technology and Research (A*STAR),CFAR and IHPC,Singapore, Tianjin University,China, Nanyang Technological University,College of Computing and Data Science,Singapore
- **会议**: CVPR 2025

### Lifelong Knowledge Editing for Vision Language Models with Low-Rank Mixture-of-Experts.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Lifelong_Knowledge_Editing_for_Vision_Language_Models_with_Low-Rank_Mixture-of-Experts_CVPR_2025_paper.html)
- **作者**: Qizhou Chen, Chengyu Wang, Dakan Wang, Taolin Zhang, Wangyue Li, Xiaofeng He
- **🏷️ 机构**: East China Normal University,Shanghai,China, Alibaba Cloud Computing,Hangzhou,China, Exacity Inc.,Shanghai,China
- **会议**: CVPR 2025

### SlideChat: A Large Vision-Language Assistant for Whole-Slide Pathology Image Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SlideChat_A_Large_Vision-Language_Assistant_for_Whole-Slide_Pathology_Image_Understanding_CVPR_2025_paper.html)
- **作者**: Ying Chen, Guoan Wang, Yuanfeng Ji, Yanjun Li, Jin Ye, Tianbin Li et al.
- **🏷️ 机构**: Shanghai AI Laboratory, Stanford University, Xiamen University
- **会议**: CVPR 2025

### Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Deitke_Molmo_and_PixMo_Open_Weights_and_Open_Data_for_State-of-the-Art_CVPR_2025_paper.html)
- **作者**: Matt Deitke, Christopher Clark, Sangho Lee, Rohun Tripathi, Yue Yang, Jae Sung Park et al.
- **🏷️ 机构**: Allen Institute for AI, University of Washington
- **会议**: CVPR 2025

### Rethinking Few-Shot Adaptation of Vision-Language Models in Two Stages.
- **链接**: [arXiv:2503.11609](https://arxiv.org/abs/2503.11609)
- **作者**: Matteo Farina, Massimiliano Mancini, Giovanni Iacca, Elisa Ricci
- **🏷️ 机构**: University of Trento
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > An old-school recipe for training a classifier is to (i) learn a good feature extractor and (ii) optimize a linear layer atop. When only a handful of samples are available per category, as in Few-Shot Adaptation (FSA), data are insufficient to fit a large number of parameters, rendering the above impractical. This is especially true with large pre-trained Vision-Language Models (VLMs), which motivated successful research at the intersection of Parameter-Efficient Fine-tuning (PEFT) and FSA. In this work, we start by analyzing the learning dynamics of PEFT techniques when trained on few-shot data from only a subset of categories, referred to as the ``base'' classes. We show that such dynamics naturally splits into two distinct phases: (i) task-level feature extraction and (ii) specialization to the available concepts. To accommodate this dynamic, we then depart from prompt- or adapter-based methods and tackle FSA differently. Specifically, given a fixed computational budget, we split it to (i) learn a task-specific feature extractor via PEFT and (ii) train a linear classifier on top. We call this scheme Two-Stage Few-Shot Adaptation (2SFS). Differently from established methods, our scheme enables a novel form of selective inference at a category level, i.e., at test time, only novel categories are embedded by the adapted text encoder, while embeddings of base categories are available within the classifier. Results with fixed hyperparameters across two settings, three backbones, and eleven datasets, show that 2SFS matches or surpasses the state-of-the-art, while established methods degrade significantly across settings.

### ReVisionLLM: Recursive Vision-Language Model for Temporal Grounding in Hour-Long Videos.
- **链接**: [arXiv:2411.14901](https://arxiv.org/abs/2411.14901) · [代码](https://github.com/Tanveer81/ReVisionLLM)
- **作者**: Tanveer Hannan, Md Mohaiminul Islam, Jindong Gu, Thomas Seidl, Gedas Bertasius
- **🏷️ 机构**: LMU Munich, UNC Chapel Hill, University of Oxford
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Large language models (LLMs) excel at retrieving information from lengthy text, but their vision-language counterparts (VLMs) face difficulties with hour-long videos, especially for temporal grounding. Specifically, these VLMs are constrained by frame limitations, often losing essential temporal details needed for accurate event localization in extended video content. We propose ReVisionLLM, a recursive vision-language model designed to locate events in hour-long videos. Inspired by human search strategies, our model initially targets broad segments of interest, progressively revising its focus to pinpoint exact temporal boundaries. Our model can seamlessly handle videos of vastly different lengths, from minutes to hours. We also introduce a hierarchical training strategy that starts with short clips to capture distinct events and progressively extends to longer videos. To our knowledge, ReVisionLLM is the first VLM capable of temporal grounding in hour-long videos, outperforming previous state-of-the-art methods across multiple datasets by a significant margin (+2.6% R1@0.1 on MAD). The code is available at https://github.com/Tanveer81/ReVisionLLM.

### Exploring Visual Vulnerabilities via Multi-Loss Adversarial Search for Jailbreaking Vision-Language Models.
- **链接**: [arXiv:2411.18000](https://arxiv.org/abs/2411.18000)
- **作者**: Shuyang Hao, Bryan Hooi, Jun Liu, Kai-Wei Chang, Zi Huang, Yujun Cai
- **🏷️ 机构**: Southeast University, National University of Singapore, Lancaster University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Despite inheriting security measures from underlying language models, Vision-Language Models (VLMs) may still be vulnerable to safety alignment issues. Through empirical analysis, we uncover two critical findings: scenario-matched images can significantly amplify harmful outputs, and contrary to common assumptions in gradient-based attacks, minimal loss values do not guarantee optimal attack effectiveness. Building on these insights, we introduce MLAI (Multi-Loss Adversarial Images), a novel jailbreak framework that leverages scenario-aware image generation for semantic alignment, exploits flat minima theory for robust adversarial image selection, and employs multi-image collaborative attacks for enhanced effectiveness. Extensive experiments demonstrate MLAI's significant impact, achieving attack success rates of 77.75% on MiniGPT-4 and 82.80% on LLaVA-2, substantially outperforming existing methods by margins of 34.37% and 12.77% respectively. Furthermore, MLAI shows considerable transferability to commercial black-box VLMs, achieving up to 60.11% success rate. Our work reveals fundamental visual vulnerabilities in current VLMs safety mechanisms and underscores the need for stronger defenses. Warning: This paper contains potentially harmful example text.

### Task-Aware Clustering for Prompting Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hao_Task-Aware_Clustering_for_Prompting_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Fusheng Hao, Fengxiang He, Fuxiang Wu, Tichao Wang, Chengqun Song, Jun Cheng
- **🏷️ 机构**: Chinese Academy of Sciences,Shenzhen Institute of Advanced Technology, University of Edinburgh
- **会议**: CVPR 2025

### MotionBench: Benchmarking and Improving Fine-grained Video Motion Understanding for Vision Language Models.
- **链接**: [arXiv:2501.02955](https://arxiv.org/abs/2501.02955)
- **作者**: Wenyi Hong, Yean Cheng, Zhuoyi Yang, Weihan Wang, Lefan Wang, Xiaotao Gu et al.
- **🏷️ 机构**: Tsinghua University, Zhipu AI
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > In recent years, vision language models (VLMs) have made significant advancements in video understanding. However, a crucial capability - fine-grained motion comprehension - remains under-explored in current benchmarks. To address this gap, we propose MotionBench, a comprehensive evaluation benchmark designed to assess the fine-grained motion comprehension of video understanding models. MotionBench evaluates models' motion-level perception through six primary categories of motion-oriented question types and includes data collected from diverse sources, ensuring a broad representation of real-world video content. Experimental results reveal that existing VLMs perform poorly in understanding fine-grained motions. To enhance VLM's ability to perceive fine-grained motion within a limited sequence length of LLM, we conduct extensive experiments reviewing VLM architectures optimized for video feature compression and propose a novel and efficient Through-Encoder (TE) Fusion method. Experiments show that higher frame rate inputs and TE Fusion yield improvements in motion understanding, yet there is still substantial room for enhancement. Our benchmark aims to guide and motivate the development of more capable video understanding models, emphasizing the importance of fine-grained motion comprehension. Project page: https://motion-bench.github.io .

### SLADE: Shielding against Dual Exploits in Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hossain_SLADE_Shielding_against_Dual_Exploits_in_Large_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Md. Zarif Hossain, Ahmed Imteaj
- **🏷️ 机构**: Southern Illinois University,School of Computing,Carbondale,IL,USA,62901
- **会议**: CVPR 2025

### HiRes-LLaVA: Restoring Fragmentation Input in High-Resolution Large Vision-Language Models.
- **链接**: [arXiv:2407.08706](https://arxiv.org/abs/2407.08706)
- **作者**: Runhui Huang, Xinpeng Ding, Chunwei Wang, Jianhua Han, Yulong Liu, Hengshuang Zhao et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, The Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > High-resolution inputs enable Large Vision-Language Models (LVLMs) to discern finer visual details, enhancing their comprehension capabilities. To reduce the training and computation costs caused by high-resolution input, one promising direction is to use sliding windows to slice the input into uniform patches, each matching the input size of the well-trained vision encoder. Although efficient, this slicing strategy leads to the fragmentation of original input, i.e., the continuity of contextual information and spatial geometry is lost across patches, adversely affecting performance in cross-patch context perception and position-specific tasks. To overcome these shortcomings, we introduce HiRes-LLaVA, a novel framework designed to efficiently process any size of high-resolution input without altering the original contextual and geometric information. HiRes-LLaVA comprises two innovative components: (i) a SliceRestore adapter that reconstructs sliced patches into their original form, efficiently extracting both global and local features via down-up-sampling and convolution layers, and (ii) a Self-Mining Sampler to compresses the vision tokens based on themselves, preserving the original context and positional information while reducing training overhead. To assess the ability of handling context fragmentation, we construct a new benchmark, EntityGrid-QA, consisting of edge-related and position-related tasks. Our comprehensive experiments demonstrate the superiority of HiRes-LLaVA on both existing public benchmarks and on EntityGrid-QA, particularly on document-oriented tasks, establishing new standards for handling high-resolution inputs.

### VL2Lite: Task-Specific Knowledge Distillation from Large Vision-Language Models to Lightweight Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jang_VL2Lite_Task-Specific_Knowledge_Distillation_from_Large_Vision-Language_Models_to_Lightweight_CVPR_2025_paper.html)
- **作者**: Jinseong Jang, Chunfei Ma, Byeongwon Lee
- **🏷️ 机构**: Vision Lab, AI R&amp;D Center, SK Telecom
- **会议**: CVPR 2025

### Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens.
- **链接**: [arXiv:2411.16724](https://arxiv.org/abs/2411.16724) · [代码](https://github.com/ZhangqiJiang07/middle_layers_indicating_hallucinations)
- **作者**: Zhangqi Jiang, Junkai Chen, Beier Zhu, Tingjin Luo, Yankun Shen, Xu Yang
- **🏷️ 机构**: National University of Defense Technology, Southeast University, Nanyang Technological University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Hallucinations in Large Vision-Language Models (LVLMs) significantly undermine their reliability, motivating researchers to explore the causes of hallucination. However, most studies primarily focus on the language aspect rather than the visual. In this paper, we address how LVLMs process visual information and whether this process causes hallucination. Firstly, we use the attention lens to identify the stages at which LVLMs handle visual data, discovering that the middle layers are crucial. Moreover, we find that these layers can be further divided into two stages: ''visual information enrichment'' and ''semantic refinement'' which respectively propagate visual data to object tokens and interpret it through text. By analyzing attention patterns during the visual information enrichment stage, we find that real tokens consistently receive higher attention weights than hallucinated ones, serving as a strong indicator of hallucination. Further examination of multi-head attention maps reveals that hallucination tokens often result from heads interacting with inconsistent objects. Based on these insights, we propose a simple inference-time method that adjusts visual attention by integrating information across various heads. Extensive experiments demonstrate that this approach effectively mitigates hallucinations in mainstream LVLMs without additional training costs. Code is available at https://github.com/ZhangqiJiang07/middle_layers_indicating_hallucinations.

### Your Large Vision-Language Model Only Needs A Few Attention Heads For Visual Grounding.
- **链接**: [arXiv:2503.06287](https://arxiv.org/abs/2503.06287)
- **作者**: Seil Kang, Jinyeong Kim, Junhyeok Kim, Seong Jae Hwang
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Visual grounding seeks to localize the image region corresponding to a free-form text description. Recently, the strong multimodal capabilities of Large Vision-Language Models (LVLMs) have driven substantial improvements in visual grounding, though they inevitably require fine-tuning and additional model components to explicitly generate bounding boxes or segmentation masks. However, we discover that a few attention heads in frozen LVLMs demonstrate strong visual grounding capabilities. We refer to these heads, which consistently capture object locations related to text semantics, as localization heads. Using localization heads, we introduce a straightforward and effective training-free visual grounding framework that utilizes text-to-image attention maps from localization heads to identify the target objects. Surprisingly, only three out of thousands of attention heads are sufficient to achieve competitive localization performance compared to existing LVLM-based visual grounding methods that require fine-tuning. Our findings suggest that LVLMs can innately ground objects based on a deep comprehension of the text-image relationship, as they implicitly focus on relevant image regions to generate informative text outputs. All the source codes will be made available to the public.

### GFlowVLM: Enhancing Multi-step Reasoning in Vision-Language Models with Generative Flow Networks.
- **链接**: [arXiv:2503.06514](https://arxiv.org/abs/2503.06514)
- **作者**: Haoqiang Kang, Enna Sachdeva, Piyush Gupta, Sangjae Bae, Kwonjoon Lee
- **🏷️ 机构**: Honda Research Institute,USA
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Vision-Language Models (VLMs) have recently shown promising advancements in sequential decision-making tasks through task-specific fine-tuning. However, common fine-tuning methods, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) techniques like Proximal Policy Optimization (PPO), present notable limitations: SFT assumes Independent and Identically Distributed (IID) data, while PPO focuses on maximizing cumulative rewards. These limitations often restrict solution diversity and hinder generalization in multi-step reasoning tasks. To address these challenges, we introduce a novel framework, GFlowVLM, a framework that fine-tune VLMs using Generative Flow Networks (GFlowNets) to promote generation of diverse solutions for complex reasoning tasks. GFlowVLM models the environment as a non-Markovian decision process, allowing it to capture long-term dependencies essential for real-world applications. It takes observations and task descriptions as inputs to prompt chain-of-thought (CoT) reasoning which subsequently guides action selection. We use task based rewards to fine-tune VLM with GFlowNets. This approach enables VLMs to outperform prior fine-tuning methods, including SFT and RL. Empirical results demonstrate the effectiveness of GFlowVLM on complex tasks such as card games (NumberLine, BlackJack) and embodied planning tasks (ALFWorld), showing enhanced training efficiency, solution diversity, and stronger generalization capabilities across both in-distribution and out-of-distribution scenarios.

### BiomedCoOp: Learning to Prompt for Biomedical Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Koleilat_BiomedCoOp_Learning_to_Prompt_for_Biomedical_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Taha Koleilat, Hojat Asgariandehkordi, Hassan Rivaz, Yiming Xiao
- **🏷️ 机构**: Concordia University,Montreal,Canada
- **会议**: CVPR 2025

### VLsI: Verbalized Layers-to-Interactions from Large to Small Vision Language Models.
- **链接**: [arXiv:2412.01822](https://arxiv.org/abs/2412.01822)
- **作者**: Byung-Kwan Lee, Ryo Hachiuma, Yu-Chiang Frank Wang, Yong Man Ro, Yueh-Hua Wu
- **🏷️ 机构**: NVIDIA, KAIST
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The recent surge in high-quality visual instruction tuning samples from closed-source vision-language models (VLMs) such as GPT-4V has accelerated the release of open-source VLMs across various model sizes. However, scaling VLMs to improve performance using larger models brings significant computational challenges, especially for deployment on resource-constrained devices like mobile platforms and robots. To address this, we propose VLsI: Verbalized Layers-to-Interactions, a new VLM family in 2B and 7B model sizes, which prioritizes efficiency without compromising accuracy. VLsI leverages a unique, layer-wise distillation process, introducing intermediate "verbalizers" that map features from each layer to natural language space, allowing smaller VLMs to flexibly align with the reasoning processes of larger VLMs. This approach mitigates the training instability often encountered in output imitation and goes beyond typical final-layer tuning by aligning the small VLMs' layer-wise progression with that of the large ones. We validate VLsI across ten challenging vision-language benchmarks, achieving notable performance gains (11.0% for 2B and 17.4% for 7B) over GPT-4V without the need for model scaling, merging, or architectural changes.

### Cropper: Vision-Language Model for Image Cropping through In-Context Learning.
- **链接**: [arXiv:2408.07790](https://arxiv.org/abs/2408.07790)
- **作者**: Seung Hyun Lee, Jijun Jiang, Yiran Xu, Zhuofang Li, Junjie Ke, Yinxiao Li et al.
- **🏷️ 机构**: Google Research, Google, Google DeepMind
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The goal of image cropping is to identify visually appealing crops in an image. Conventional methods are trained on specific datasets and fail to adapt to new requirements. Recent breakthroughs in large vision-language models (VLMs) enable visual in-context learning without explicit training. However, downstream tasks with VLMs remain under explored. In this paper, we propose an effective approach to leverage VLMs for image cropping. First, we propose an efficient prompt retrieval mechanism for image cropping to automate the selection of in-context examples. Second, we introduce an iterative refinement strategy to iteratively enhance the predicted crops. The proposed framework, we refer to as Cropper, is applicable to a wide range of cropping tasks, including free-form cropping, subject-aware cropping, and aspect ratio-aware cropping. Extensive experiments demonstrate that Cropper significantly outperforms state-of-the-art methods across several benchmarks.

### MBQ: Modality-Balanced Quantization for Large Vision-Language Models.
- **链接**: [arXiv:2412.19509](https://arxiv.org/abs/2412.19509) · [代码](https://github.com/thu-nics/MBQ)
- **作者**: Shiyao Li, Yingchun Hu, Xuefei Ning, Xihui Liu, Ke Hong, Xiaotao Jia et al.
- **🏷️ 机构**: Tsinghua University, Infinigence-AI, University of Hong Kong
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Vision-Language Models (VLMs) have enabled a variety of real-world applications. The large parameter size of VLMs brings large memory and computation overhead which poses significant challenges for deployment. Post-Training Quantization (PTQ) is an effective technique to reduce the memory and computation overhead. Existing PTQ methods mainly focus on large language models (LLMs), without considering the differences across other modalities. In this paper, we discover that there is a significant difference in sensitivity between language and vision tokens in large VLMs. Therefore, treating tokens from different modalities equally, as in existing PTQ methods, may over-emphasize the insensitive modalities, leading to significant accuracy loss. To deal with the above issue, we propose a simple yet effective method, Modality-Balanced Quantization (MBQ), for large VLMs. Specifically, MBQ incorporates the different sensitivities across modalities during the calibration process to minimize the reconstruction loss for better quantization parameters. Extensive experiments show that MBQ can significantly improve task accuracy by up to 4.4% and 11.6% under W3 and W4A8 quantization for 7B to 70B VLMs, compared to SOTA baselines. Additionally, we implement a W3 GPU kernel that fuses the dequantization and GEMV operators, achieving a 1.4x speedup on LLaVA-onevision-7B on the RTX 4090. The code is available at https://github.com/thu-nics/MBQ.

### DPC: Dual-Prompt Collaboration for Tuning Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_DPC_Dual-Prompt_Collaboration_for_Tuning_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Haoyang Li, Liang Wang, Chao Wang, Jing Jiang, Yan Peng, Guodong Long
- **🏷️ 机构**: Shanghai University, University of Technology Sydney
- **会议**: CVPR 2025

### Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Revisiting_Backdoor_Attacks_against_Large_Vision-Language_Models_from_Domain_Shift_CVPR_2025_paper.html)
- **作者**: Siyuan Liang, Jiawei Liang, Tianyu Pang, Chao Du, Aishan Liu, Mingli Zhu et al.
- **🏷️ 机构**: Nanyang Technological University, Shenzhen Campus of Sun Yat-Sen University, Sea AI Lab,Singapore
- **会议**: CVPR 2025

### Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_Can_Large_Vision-Language_Models_Correct_Semantic_Grounding_Errors_By_Themselves_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Yuan-Hong Liao, Rafid Mahmood, Sanja Fidler, David Acuna
- **🏷️ 机构**: University of Toronto,Vector Institute, NVIDIA
- **会议**: CVPR 2025

### BIOMEDICA: An Open Biomedical Image-Caption Archive, Dataset, and Vision-Language Models Derived from Scientific Literature.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lozano_BIOMEDICA_An_Open_Biomedical_Image-Caption_Archive_Dataset_and_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Alejandro Lozano, Min Woo Sun, James Burgess, Liangyu Chen, Jeffrey J. Nirschl, Jeffrey Gu et al.
- **🏷️ 机构**: Stanford University
- **会议**: CVPR 2025

### Benchmarking Large Vision-Language Models via Directed Scene Graph for Comprehensive Image Captioning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_Benchmarking_Large_Vision-Language_Models_via_Directed_Scene_Graph_for_Comprehensive_CVPR_2025_paper.html)
- **作者**: Fan Lu, Wei Wu, Kecheng Zheng, Shuailei Ma, Biao Gong, Jiawei Liu et al.
- **🏷️ 机构**: University of Science and Technology of China,MoE Key Laboratory of Brain-Inspired Intelligent Perception and Cognition, Ant Group, Northeastern University,China
- **会议**: CVPR 2025

### SPARC: Score Prompting and Adaptive Fusion for Zero-Shot Multi-Label Recognition in Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Miller_SPARC_Score_Prompting_and_Adaptive_Fusion_for_Zero-Shot_Multi-Label_Recognition_CVPR_2025_paper.html)
- **作者**: Kevin Miller, Aditya Gangrade, Samarth Mishra, Kate Saenko, Venkatesh Saligrama
- **🏷️ 机构**: Boston University, Boston University and Meta AI (FAIR)
- **会议**: CVPR 2025

### VILA-M3: Enhancing Vision-Language Models with Medical Expert Knowledge.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Nath_VILA-M3_Enhancing_Vision-Language_Models_with_Medical_Expert_Knowledge_CVPR_2025_paper.html)
- **作者**: Vishwesh Nath, Wenqi Li, Dong Yang, Andriy Myronenko, Mingxin Zheng, Yao Lu et al.
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2025

### CALICO: Part-Focused Semantic Co-Segmentation with Large Vision-Language Models.
- **链接**: [arXiv:2412.19331](https://arxiv.org/abs/2412.19331)
- **作者**: Kiet A. Nguyen, Adheesh Sunil Juvekar, Tianjiao Yu, Muntasir Wahed, Ismini Lourentzou
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Recent advances in Large Vision-Language Models (LVLMs) have enabled general-purpose vision tasks through visual instruction tuning. While existing LVLMs can generate segmentation masks from text prompts for single images, they struggle with segmentation-grounded reasoning across images, especially at finer granularities such as object parts. In this paper, we introduce the new task of part-focused semantic co-segmentation, which involves identifying and segmenting common objects, as well as common and unique object parts across images. To address this task, we present CALICO, the first LVLM designed for multi-image part-level reasoning segmentation. CALICO features two key components, a novel Correspondence Extraction Module that identifies semantic part-level correspondences, and Correspondence Adaptation Modules that embed this information into the LVLM to facilitate multi-image understanding in a parameter-efficient manner. To support training and evaluation, we curate MixedParts, a large-scale multi-image segmentation dataset containing $\sim$2.4M samples across $\sim$44K images spanning diverse object and part categories. Experimental results demonstrate that CALICO, with just 0.3% of its parameters finetuned, achieves strong performance on this challenging task.

### NLPrompt: Noise-Label Prompt Learning for Vision-Language Models.
- **链接**: [arXiv:2412.01256](https://arxiv.org/abs/2412.01256)
- **作者**: Bikang Pan, Qun Li, Xiaoying Tang, Wei Huang, Zhen Fang, Feng Liu et al.
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China, The Chinese University of Hong Kong,Shenzhen,China, RIKEN Center for Advanced Intelligence Project,Japan
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The emergence of vision-language foundation models, such as CLIP, has revolutionized image-text representation, enabling a broad range of applications via prompt learning. Despite its promise, real-world datasets often contain noisy labels that can degrade prompt learning performance. In this paper, we demonstrate that using mean absolute error (MAE) loss in prompt learning, named PromptMAE, significantly enhances robustness against noisy labels while maintaining high accuracy. Though MAE is straightforward and recognized for its robustness, it is rarely used in noisy-label learning due to its slow convergence and poor performance outside prompt learning scenarios. To elucidate the robustness of PromptMAE, we leverage feature learning theory to show that MAE can suppress the influence of noisy samples, thereby improving the signal-to-noise ratio and enhancing overall robustness. Additionally, we introduce PromptOT, a prompt-based optimal transport data purification method to enhance the robustness further. PromptOT employs text features in vision-language models as prototypes to construct an optimal transportation matrix. This matrix effectively partitions datasets into clean and noisy subsets, allowing for the application of cross-entropy loss to the clean subset and MAE loss to the noisy subset. Our Noise-Label Prompt Learning method, named NLPrompt, offers a simple and efficient approach that leverages the expressive representations and precise alignment capabilities of vision-language models for robust prompt learning. We validate NLPrompt through extensive experiments across various noise settings, demonstrating significant performance improvements.

### HalLoc: Token-level Localization of Hallucinations for Vision Language Models.
- **链接**: [arXiv:2506.10286](https://arxiv.org/abs/2506.10286) · [代码](https://github.com/dbsltm/cvpr25_halloc)
- **作者**: Eunkyu Park, Minyeong Kim, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Hallucinations pose a significant challenge to the reliability of large vision-language models, making their detection essential for ensuring accuracy in critical applications. Current detection methods often rely on computationally intensive models, leading to high latency and resource demands. Their definitive outcomes also fail to account for real-world scenarios where the line between hallucinated and truthful information is unclear. To address these issues, we propose HalLoc, a dataset designed for efficient, probabilistic hallucination detection. It features 150K token-level annotated samples, including hallucination types, across Visual Question Answering (VQA), instruction-following, and image captioning tasks. This dataset facilitates the development of models that detect hallucinations with graded confidence, enabling more informed user interactions. Additionally, we introduce a baseline model trained on HalLoc, offering low-overhead, concurrent hallucination detection during generation. The model can be seamlessly integrated into existing VLMs, improving reliability while preserving efficiency. The prospect of a robust plug-and-play hallucination detection module opens new avenues for enhancing the trustworthiness of vision-language models in real-world applications. The HalLoc dataset and code are publicly available at: https://github.com/dbsltm/cvpr25_halloc.

### Hyperbolic Safety-Aware Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Poppi_Hyperbolic_Safety-Aware_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Tobia Poppi, Tejaswi Kasarla, Pascal Mettes, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy, University of Amsterdam,Netherlands
- **会议**: CVPR 2025

### F3OCUS - Federated Finetuning of Vision-Language Foundation Models with Optimal Client Layer Updating Strategy via Multi-objective Meta-Heuristics.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Saha_F3OCUS_-_Federated_Finetuning_of_Vision-Language_Foundation_Models_with_Optimal_CVPR_2025_paper.html)
- **作者**: Pramit Saha, Felix Wagner, Divyanshu Mishra, Can Peng, Anshul Thakur, David A. Clifton et al.
- **🏷️ 机构**: University of Oxford
- **会议**: CVPR 2025

### PARC: A Quantitative Framework Uncovering the Symmetries within Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Schmalfuss_PARC_A_Quantitative_Framework_Uncovering_the_Symmetries_within_Vision_Language_CVPR_2025_paper.html)
- **作者**: Jenny Schmalfuss, Nadine Chang, Vibashan VS, Maying Shen, Andrés Bruhn, José M. Álvarez
- **🏷️ 机构**: University of Stuttgart, NVIDIA, Johns Hopkins University
- **会议**: CVPR 2025

### O-TPT: Orthogonality Constraints for Calibrating Test-time Prompt Tuning in Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sharifdeen_O-TPT_Orthogonality_Constraints_for_Calibrating_Test-time_Prompt_Tuning_in_Vision-Language_CVPR_2025_paper.html)
- **作者**: Ashshak Sharifdeen, Muhammad Akhtar Munir, Sanoojan Baliah, Salman Khan, Muhammad Haris Khan
- **🏷️ 机构**: Mohamed Bin Zayed University of AI
- **会议**: CVPR 2025

### R-TPT: Improving Adversarial Robustness of Vision-Language Models through Test-Time Prompt Tuning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sheng_R-TPT_Improving_Adversarial_Robustness_of_Vision-Language_Models_through_Test-Time_Prompt_CVPR_2025_paper.html)
- **作者**: Lijun Sheng, Jian Liang, Zilei Wang, Ran He
- **🏷️ 机构**: University of Science and Technology of China, Chinese Academy of Sciences,NLPR &#x0026; MAIS, Institute of Automation
- **会议**: CVPR 2025

### Taxonomy-Aware Evaluation of Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Snaebjarnarson_Taxonomy-Aware_Evaluation_of_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Vésteinn Snæbjarnarson, Kevin Du, Niklas Stoehr, Serge J. Belongie, Ryan Cotterell, Nico Lang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Retaining Knowledge and Enhancing Long-Text Representations in CLIP through Dual-Teacher Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Feng_Retaining_Knowledge_and_Enhancing_Long-Text_Representations_in_CLIP_through_Dual-Teacher_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Yuheng Feng, Changsong Wen, Zelin Peng, Li jiaye, Siyu Zhu
- **🏷️ 机构**: Fudan University, Shanghai Jiao Tong University
- **会议**: CVPR 2025

### Classifier-guided CLIP Distillation for Unsupervised Multi-label Classification.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kim_Classifier-guided_CLIP_Distillation_for_Unsupervised_Multi-label_Classification_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Dongseob Kim, Hyunjung Shim
- **🏷️ 机构**: Samsung Electronics,Republic of Korea, KAIST,Republic of Korea
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- ROD-MLLM: Towards More Reliable Object Detection in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Fine-Grained Image-Text Correspondence with Cost Aggregation for Open-Vocabulary Part Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Understanding Fine-tuning CLIP for Open-vocabulary Semantic Segmentation in Hyperbolic Space. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Towards Zero-Shot Anomaly Detection and Reasoning with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- S4-Driver: Scalable Self-Supervised Driving Multimodal Large Language Model with Spatio-Temporal Visual Representation. → [multimodal](../multimodal/Guideline%202025.md)
- Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for Large Vision Language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- BOLT: Boost Large Vision-Language Model Without Training for Long-form Video Understanding. → [video-understanding](../video-understanding/Guideline%202025.md)
- MIMO: A Medical Vision Language Model with Visual Referring Multimodal Input and Pixel Grounding Multimodal Output. → [multimodal](../multimodal/Guideline%202025.md)
- MMRL: Multi-Modal Representation Learning for Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Rethinking Vision-Language Model in Face Forensics: Multi-Modal Interpretable Forged Face Detector. → [multimodal](../multimodal/Guideline%202025.md)
- EfficientLLaVA: Generalizable Auto-Pruning for Large Vision-language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding. → [video-understanding](../video-understanding/Guideline%202025.md)
- ImagineFSL: Self-Supervised Pretraining Matters on Imagined Base Set for VLM-based Few-shot Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Anyattack: Towards Large-scale Self-supervised Adversarial Attacks on Vision-language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Instruct-CLIP: Improving Instruction-Guided Image Editing with Automated Data Refinement Using Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding. → [3d-detection](../3d-detection/Guideline%202025.md)
- Libra-Merging: Importance-redundancy and Pruning-merging Trade-off for Acceleration Plug-in in Large Vision-Language Model. → [network-pruning](../network-pruning/Guideline%202025.md)
- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
