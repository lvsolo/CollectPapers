# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 70 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Generalized Few-shot 3D Point Cloud Segmentation with Vision-Language Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/An_Generalized_Few-shot_3D_Point_Cloud_Segmentation_with_Vision-Language_Model_CVPR_2025_paper.html)
- **作者**: Zhaochong An, Guolei Sun, Yun Liu, Runjia Li, Junlin Han, Ender Konukoglu et al.
- **🏷️ 机构**: University of Oxford, Meta
- **会议**: CVPR 2025

### ProxyTransformation: Preshaping Point Cloud Manifold With Proxy Attention For 3D Visual Grounding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_ProxyTransformation_Preshaping_Point_Cloud_Manifold_With_Proxy_Attention_For_3D_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Qihang Peng, Henry Zheng, Gao Huang
- **🏷️ 机构**: Tsinghua University
- **会议**: CVPR 2025

### AA-CLIP: Enhancing Zero-Shot Anomaly Detection via Anomaly-Aware CLIP.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_AA-CLIP_Enhancing_Zero-Shot_Anomaly_Detection_via_Anomaly-Aware_CLIP_CVPR_2025_paper.html) · 📚 被引 63
- **作者**: Wenxin Ma, Xu Zhang, Qingsong Yao, Fenghe Tang, Chenxu Wu, Yingtai Li et al.
- **🏷️ 机构**: USTC,School of Biomedical Engineering, Division of Life Sciences and Medicine, Stanford University
- **会议**: CVPR 2025

### HoVLE: Unleashing the Power of Monolithic Vision-Language Models with Holistic Vision-Language Embedding.
- **链接**: [arXiv:2412.16158](https://arxiv.org/abs/2412.16158) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tao_HoVLE_Unleashing_the_Power_of_Monolithic_Vision-Language_Models_with_Holistic_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Chenxin Tao, Shiqian Su, Xizhou Zhu, Chenyu Zhang, Zhe Chen, Jiawen Liu et al.
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab, Shanghai AI Lab
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The rapid advance of Large Language Models (LLMs) has catalyzed the development of Vision-Language Models (VLMs). Monolithic VLMs, which avoid modality-specific encoders, offer a promising alternative to the compositional ones but face the challenge of inferior performance. Most existing monolithic VLMs require tuning pre-trained LLMs to acquire vision abilities, which may degrade their language capabilities. To address this dilemma, this paper presents a novel high-performance monolithic VLM named HoVLE. We note that LLMs have been shown capable of interpreting images, when image embeddings are aligned with text embeddings. The challenge for current monolithic VLMs actually lies in the lack of a holistic embedding module for both vision and language inputs. Therefore, HoVLE introduces a holistic embedding module that converts visual and textual inputs into a shared space, allowing LLMs to process images in the same way as texts. Furthermore, a multi-stage training strategy is carefully designed to empower the holistic embedding module. It is first trained to distill visual features from a pre-trained vision encoder and text embeddings from the LLM, enabling large-scale training with unpaired random images and text tokens. The whole model further undergoes next-token prediction on multi-modal data to align the embeddings. Finally, an instruction-tuning stage is incorporated. Our experiments show that HoVLE achieves performance close to leading compositional models on various benchmarks, outperforming previous monolithic models by a large margin. Model available at https://huggingface.co/OpenGVLab/HoVLE.

### Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion.
- **链接**: [arXiv:2412.04424](https://arxiv.org/abs/2412.04424) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Florence-VL_Enhancing_Vision-Language_Models_with_Generative_Vision_Encoder_and_Depth-Breadth_CVPR_2025_paper.html) · [代码](https://github.com/JiuhaiChen/Florence-VL) · 📚 被引 9
- **作者**: Jiuhai Chen, Jianwei Yang, Haiping Wu, Dianqi Li, Jianfeng Gao, Tianyi Zhou et al.
- **🏷️ 机构**: University of Maryland, Microsoft Research
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > We present Florence-VL, a new family of multimodal large language models (MLLMs) with enriched visual representations produced by Florence-2, a generative vision foundation model. Unlike the widely used CLIP-style vision transformer trained by contrastive learning, Florence-2 can capture different levels and aspects of visual features, which are more versatile to be adapted to diverse downstream tasks. We propose a novel feature-fusion architecture and an innovative training recipe that effectively integrates Florence-2's visual features into pretrained LLMs, such as Phi 3.5 and LLama 3. In particular, we propose "depth-breath fusion (DBFusion)" to fuse the visual features extracted from different depths and under multiple prompts. Our model training is composed of end-to-end pretraining of the whole model followed by finetuning of the projection layer and the LLM, on a carefully designed recipe of diverse open-source datasets that include high-quality image captions and instruction-tuning pairs. Our quantitative analysis and visualization of Florence-VL's visual features show its advantages over popular vision encoders on vision-language alignment, where the enriched depth and breath play important roles. Florence-VL achieves significant improvements over existing state-of-the-art MLLMs across various multi-modal and vision-centric benchmarks covering general VQA, perception, hallucination, OCR, Chart, knowledge-intensive understanding, etc. To facilitate future research, our models and the complete training recipe are open-sourced. https://github.com/JiuhaiChen/Florence-VL

### Words or Vision: Do Vision-Language Models Have Blind Faith in Text?
- **链接**: [arXiv:2503.02199](https://arxiv.org/abs/2503.02199) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Words_or_Vision_Do_Vision-Language_Models_Have_Blind_Faith_in_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: Ailin Deng, Tri Cao, Zhirui Chen, Bryan Hooi
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Vision-Language Models (VLMs) excel in integrating visual and textual information for vision-centric tasks, but their handling of inconsistencies between modalities is underexplored. We investigate VLMs' modality preferences when faced with visual data and varied textual inputs in vision-centered settings. By introducing textual variations to four vision-centric tasks and evaluating ten Vision-Language Models (VLMs), we discover a \emph{``blind faith in text''} phenomenon: VLMs disproportionately trust textual data over visual data when inconsistencies arise, leading to significant performance drops under corrupted text and raising safety concerns. We analyze factors influencing this text bias, including instruction prompts, language model size, text relevance, token order, and the interplay between visual and textual certainty. While certain factors, such as scaling up the language model size, slightly mitigate text bias, others like token order can exacerbate it due to positional biases inherited from language models. To address this issue, we explore supervised fine-tuning with text augmentation and demonstrate its effectiveness in reducing text bias. Additionally, we provide a theoretical analysis suggesting that the blind faith in text phenomenon may stem from an imbalance of pure text and multi-modal data during training. Our findings highlight the need for balanced training and careful consideration of modality interactions in VLMs to enhance their robustness and reliability in handling multi-modal data inconsistencies.

### What's in the Image? A Deep-Dive into the Vision of Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kaduri_Whats_in_the_Image_A_Deep-Dive_into_the_Vision_of_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Omri Kaduri, Shai Bagon, Tali Dekel
- **🏷️ 机构**: Weizmann Institute of Science
- **会议**: CVPR 2025

### Seeing the Abstract: Translating the Abstract Language for Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Talon_Seeing_the_Abstract_Translating_the_Abstract_Language_for_Vision_Language_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Davide Talon, Federico Girella, Ziyue Liu, Marco Cristani, Yiming Wang
- **🏷️ 机构**: Fondazione Bruno Kessler, University of Verona
- **会议**: CVPR 2025

### FastVLM: Efficient Vision Encoding for Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Vasu_FastVLM_Efficient_Vision_Encoding_for_Vision_Language_Models_CVPR_2025_paper.html) · 📚 被引 24
- **作者**: Pavan Kumar Anasosalu Vasu, Fartash Faghri, Chun-Liang Li, Cem Koc, Nate True, Albert Antony et al.
- **🏷️ 机构**: Apple
- **会议**: CVPR 2025

### VisionZip: Longer is Better but Not Necessary in Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_VisionZip_Longer_is_Better_but_Not_Necessary_in_Vision_Language_CVPR_2025_paper.html) · 📚 被引 43
- **作者**: Senqiao Yang, Yukang Chen, Zhuotao Tian, Chengyao Wang, Jingyao Li, Bei Yu et al.
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: CVPR 2025

### Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Mamba_as_a_Bridge_Where_Vision_Foundation_Models_Meet_Vision_CVPR_2025_paper.html) · 📚 被引 11
- **作者**: Xin Zhang, Robby T. Tan
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2025

### ICT: Image-Object Cross-Level Trusted Intervention for Mitigating Object Hallucination in Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_ICT_Image-Object_Cross-Level_Trusted_Intervention_for_Mitigating_Object_Hallucination_in_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Junzhe Chen, Tianshu Zhang, Shiyu Huang, Yuwei Niu, Linfeng Zhang, Lijie Wen et al.
- **🏷️ 机构**: Tsinghua University, Zhipu AI, Chongqing University
- **会议**: CVPR 2025

### Skip Tuning: Pre-trained Vision-Language Models are Effective and Efficient Adapters Themselves.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Skip_Tuning_Pre-trained_Vision-Language_Models_are_Effective_and_Efficient_Adapters_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Shihan Wu, Ji Zhang, Pengpeng Zeng, Lianli Gao, Jingkuan Song, Heng Tao Shen
- **🏷️ 机构**: University of Electronic Science and Technology of China (UESTC), Southwest Jiaotong University, UESTC,Shenzhen Institute for Advanced Study
- **会议**: CVPR 2025

### Reproducible Vision-Language Models Meet Concepts Out of Pre-Training.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Reproducible_Vision-Language_Models_Meet_Concepts_Out_of_Pre-Training_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Ziliang Chen, Xin Huang, Xiaoxuan Fan, Keze Wang, Yuyu Zhou, Quanlong Guan et al.
- **🏷️ 机构**: Research Institute of Multiple Agents and Embodied Intelligence,Peng Cheng Laboratory, Sun Yat-sen University, Jinan University
- **会议**: CVPR 2025

### Nullu: Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Nullu_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_via_HalluSpace_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: Le Yang, Ziwei Zheng, Boxu Chen, Zhengyu Zhao, Chenhao Lin, Chao Shen
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,Xi&#x2019;an,China,710049
- **会议**: CVPR 2025

### Evaluating Vision-Language Models as Evaluators in Path Planning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Aghzal_Evaluating_Vision-Language_Models_as_Evaluators_in_Path_Planning_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Mohamed Aghzal, Xiang Yue, Erion Plaku, Ziyu Yao
- **🏷️ 机构**: George Mason University, Carnegie Mellon University, National Science Foundation
- **会议**: CVPR 2025

### Vision-Language Models Do Not Understand Negation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Alhamoud_Vision-Language_Models_Do_Not_Understand_Negation_CVPR_2025_paper.html) · 📚 被引 18
- **作者**: Kumail Alhamoud, Shaden Alshammari, Yonglong Tian, Guohao Li, Philip H. S. Torr, Yoon Kim et al.
- **🏷️ 机构**: MIT, OpenAI, University of Oxford
- **会议**: CVPR 2025

### Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/An_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_with_Assembly_of_CVPR_2025_paper.html) · 📚 被引 15
- **作者**: Wenbin An, Feng Tian, Sicong Leng, Jiahao Nie, Haonan Lin, Qianying Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, Nanyang Technological University, Lenovo Research
- **会议**: CVPR 2025

### ProKeR: A Kernel Perspective on Few-Shot Adaptation of Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Bendou_ProKeR_A_Kernel_Perspective_on_Few-Shot_Adaptation_of_Large_Vision-Language_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: Yassir Bendou, Amine Ouasfi, Vincent Gripon, Adnane Boukhayma
- **🏷️ 机构**: IMT Atlantique,Brest,France, Inria, University Rennes, IRISA, CNRS
- **会议**: CVPR 2025

### Not Only Text: Exploring Compositionality of Visual Representations in Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Berasi_Not_Only_Text_Exploring_Compositionality_of_Visual_Representations_in_Vision-Language_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Davide Berasi, Matteo Farina, Massimiliano Mancini, Elisa Ricci, Nicola Strisciuglio
- **🏷️ 机构**: Fondazione Bruno Kessler, University of Trento, University of Twente
- **会议**: CVPR 2025

### SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Cao_SceneTAP_Scene-Coherent_Typographic_Adversarial_Planner_against_Vision-Language_Models_in_Real-World_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Yue Cao, Yun Xing, Jie Zhang, Di Lin, Tianwei Zhang, Ivor W. Tsang et al.
- **🏷️ 机构**: Agency for Science, Technology and Research (A*STAR),CFAR and IHPC,Singapore, Tianjin University,China, Nanyang Technological University,College of Computing and Data Science,Singapore
- **会议**: CVPR 2025

### Lifelong Knowledge Editing for Vision Language Models with Low-Rank Mixture-of-Experts.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Lifelong_Knowledge_Editing_for_Vision_Language_Models_with_Low-Rank_Mixture-of-Experts_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Qizhou Chen, Chengyu Wang, Dakan Wang, Taolin Zhang, Wangyue Li, Xiaofeng He
- **🏷️ 机构**: East China Normal University,Shanghai,China, Alibaba Cloud Computing,Hangzhou,China, Exacity Inc.,Shanghai,China
- **会议**: CVPR 2025

### SlideChat: A Large Vision-Language Assistant for Whole-Slide Pathology Image Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SlideChat_A_Large_Vision-Language_Assistant_for_Whole-Slide_Pathology_Image_Understanding_CVPR_2025_paper.html) · 📚 被引 17
- **作者**: Ying Chen, Guoan Wang, Yuanfeng Ji, Yanjun Li, Jin Ye, Tianbin Li et al.
- **🏷️ 机构**: Shanghai AI Laboratory, Stanford University, Xiamen University
- **会议**: CVPR 2025

### Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Deitke_Molmo_and_PixMo_Open_Weights_and_Open_Data_for_State-of-the-Art_CVPR_2025_paper.html) · 📚 被引 46
- **作者**: Matt Deitke, Christopher Clark, Sangho Lee, Rohun Tripathi, Yue Yang, Jae Sung Park et al.
- **🏷️ 机构**: Allen Institute for AI, University of Washington
- **会议**: CVPR 2025

### Rethinking Few-Shot Adaptation of Vision-Language Models in Two Stages.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Farina_Rethinking_Few-Shot_Adaptation_of_Vision-Language_Models_in_Two_Stages_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Matteo Farina, Massimiliano Mancini, Giovanni Iacca, Elisa Ricci
- **🏷️ 机构**: University of Trento
- **会议**: CVPR 2025

### ReVisionLLM: Recursive Vision-Language Model for Temporal Grounding in Hour-Long Videos.
- **链接**: [arXiv:2411.14901](https://arxiv.org/abs/2411.14901) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hannan_ReVisionLLM_Recursive_Vision-Language_Model_for_Temporal_Grounding_in_Hour-Long_Videos_CVPR_2025_paper.html) · [代码](https://github.com/Tanveer81/ReVisionLLM) · 📚 被引 3
- **作者**: Tanveer Hannan, Md Mohaiminul Islam, Jindong Gu, Thomas Seidl, Gedas Bertasius
- **🏷️ 机构**: LMU Munich, UNC Chapel Hill, University of Oxford
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Large language models (LLMs) excel at retrieving information from lengthy text, but their vision-language counterparts (VLMs) face difficulties with hour-long videos, especially for temporal grounding. Specifically, these VLMs are constrained by frame limitations, often losing essential temporal details needed for accurate event localization in extended video content. We propose ReVisionLLM, a recursive vision-language model designed to locate events in hour-long videos. Inspired by human search strategies, our model initially targets broad segments of interest, progressively revising its focus to pinpoint exact temporal boundaries. Our model can seamlessly handle videos of vastly different lengths, from minutes to hours. We also introduce a hierarchical training strategy that starts with short clips to capture distinct events and progressively extends to longer videos. To our knowledge, ReVisionLLM is the first VLM capable of temporal grounding in hour-long videos, outperforming previous state-of-the-art methods across multiple datasets by a significant margin (+2.6% R1@0.1 on MAD). The code is available at https://github.com/Tanveer81/ReVisionLLM.

### Exploring Visual Vulnerabilities via Multi-Loss Adversarial Search for Jailbreaking Vision-Language Models.
- **链接**: [arXiv:2411.18000](https://arxiv.org/abs/2411.18000) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hao_Exploring_Visual_Vulnerabilities_via_Multi-Loss_Adversarial_Search_for_Jailbreaking_Vision-Language_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Shuyang Hao, Bryan Hooi, Jun Liu, Kai-Wei Chang, Zi Huang, Yujun Cai
- **🏷️ 机构**: Southeast University, National University of Singapore, Lancaster University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Despite inheriting security measures from underlying language models, Vision-Language Models (VLMs) may still be vulnerable to safety alignment issues. Through empirical analysis, we uncover two critical findings: scenario-matched images can significantly amplify harmful outputs, and contrary to common assumptions in gradient-based attacks, minimal loss values do not guarantee optimal attack effectiveness. Building on these insights, we introduce MLAI (Multi-Loss Adversarial Images), a novel jailbreak framework that leverages scenario-aware image generation for semantic alignment, exploits flat minima theory for robust adversarial image selection, and employs multi-image collaborative attacks for enhanced effectiveness. Extensive experiments demonstrate MLAI's significant impact, achieving attack success rates of 77.75% on MiniGPT-4 and 82.80% on LLaVA-2, substantially outperforming existing methods by margins of 34.37% and 12.77% respectively. Furthermore, MLAI shows considerable transferability to commercial black-box VLMs, achieving up to 60.11% success rate. Our work reveals fundamental visual vulnerabilities in current VLMs safety mechanisms and underscores the need for stronger defenses. Warning: This paper contains potentially harmful example text.

### Task-Aware Clustering for Prompting Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hao_Task-Aware_Clustering_for_Prompting_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Fusheng Hao, Fengxiang He, Fuxiang Wu, Tichao Wang, Chengqun Song, Jun Cheng
- **🏷️ 机构**: Chinese Academy of Sciences,Shenzhen Institute of Advanced Technology, University of Edinburgh
- **会议**: CVPR 2025

### MotionBench: Benchmarking and Improving Fine-grained Video Motion Understanding for Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hong_MotionBench_Benchmarking_and_Improving_Fine-grained_Video_Motion_Understanding_for_Vision_CVPR_2025_paper.html) · 📚 被引 9
- **作者**: Wenyi Hong, Yean Cheng, Zhuoyi Yang, Weihan Wang, Lefan Wang, Xiaotao Gu et al.
- **🏷️ 机构**: Tsinghua University, Zhipu AI
- **会议**: CVPR 2025

### SLADE: Shielding against Dual Exploits in Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hossain_SLADE_Shielding_against_Dual_Exploits_in_Large_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Md. Zarif Hossain, Ahmed Imteaj
- **🏷️ 机构**: Southern Illinois University,School of Computing,Carbondale,IL,USA,62901
- **会议**: CVPR 2025

### HiRes-LLaVA: Restoring Fragmentation Input in High-Resolution Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_HiRes-LLaVA_Restoring_Fragmentation_Input_in_High-Resolution_Large_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Runhui Huang, Xinpeng Ding, Chunwei Wang, Jianhua Han, Yulong Liu, Hengshuang Zhao et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, The Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2025

### VL2Lite: Task-Specific Knowledge Distillation from Large Vision-Language Models to Lightweight Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jang_VL2Lite_Task-Specific_Knowledge_Distillation_from_Large_Vision-Language_Models_to_Lightweight_CVPR_2025_paper.html) · 📚 被引 11
- **作者**: Jinseong Jang, Chunfei Ma, Byeongwon Lee
- **🏷️ 机构**: Vision Lab, AI R&amp;D Center, SK Telecom
- **会议**: CVPR 2025

### Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jiang_Devils_in_Middle_Layers_of_Large_Vision-Language_Models_Interpreting_Detecting_CVPR_2025_paper.html) · 📚 被引 15
- **作者**: Zhangqi Jiang, Junkai Chen, Beier Zhu, Tingjin Luo, Yankun Shen, Xu Yang
- **🏷️ 机构**: National University of Defense Technology, Southeast University, Nanyang Technological University
- **会议**: CVPR 2025

### Your Large Vision-Language Model Only Needs A Few Attention Heads For Visual Grounding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kang_Your_Large_Vision-Language_Model_Only_Needs_A_Few_Attention_Heads_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Seil Kang, Jinyeong Kim, Junhyeok Kim, Seong Jae Hwang
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2025

### GFlowVLM: Enhancing Multi-step Reasoning in Vision-Language Models with Generative Flow Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Kang_GFlowVLM_Enhancing_Multi-step_Reasoning_in_Vision-Language_Models_with_Generative_Flow_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Haoqiang Kang, Enna Sachdeva, Piyush Gupta, Sangjae Bae, Kwonjoon Lee
- **🏷️ 机构**: Honda Research Institute,USA
- **会议**: CVPR 2025

### BiomedCoOp: Learning to Prompt for Biomedical Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Koleilat_BiomedCoOp_Learning_to_Prompt_for_Biomedical_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 22
- **作者**: Taha Koleilat, Hojat Asgariandehkordi, Hassan Rivaz, Yiming Xiao
- **🏷️ 机构**: Concordia University,Montreal,Canada
- **会议**: CVPR 2025

### VLsI: Verbalized Layers-to-Interactions from Large to Small Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_VLsI_Verbalized_Layers-to-Interactions_from_Large_to_Small_Vision_Language_Models_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Byung-Kwan Lee, Ryo Hachiuma, Yu-Chiang Frank Wang, Yong Man Ro, Yueh-Hua Wu
- **🏷️ 机构**: NVIDIA, KAIST
- **会议**: CVPR 2025

### Cropper: Vision-Language Model for Image Cropping through In-Context Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Cropper_Vision-Language_Model_for_Image_Cropping_through_In-Context_Learning_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Seung Hyun Lee, Jijun Jiang, Yiran Xu, Zhuofang Li, Junjie Ke, Yinxiao Li et al.
- **🏷️ 机构**: Google Research, Google, Google DeepMind
- **会议**: CVPR 2025

### MBQ: Modality-Balanced Quantization for Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_MBQ_Modality-Balanced_Quantization_for_Large_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Shiyao Li, Yingchun Hu, Xuefei Ning, Xihui Liu, Ke Hong, Xiaotao Jia et al.
- **🏷️ 机构**: Tsinghua University, Infinigence-AI, University of Hong Kong
- **会议**: CVPR 2025

### DPC: Dual-Prompt Collaboration for Tuning Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_DPC_Dual-Prompt_Collaboration_for_Tuning_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 13
- **作者**: Haoyang Li, Liang Wang, Chao Wang, Jing Jiang, Yan Peng, Guodong Long
- **🏷️ 机构**: Shanghai University, University of Technology Sydney
- **会议**: CVPR 2025

### Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Revisiting_Backdoor_Attacks_against_Large_Vision-Language_Models_from_Domain_Shift_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Siyuan Liang, Jiawei Liang, Tianyu Pang, Chao Du, Aishan Liu, Mingli Zhu et al.
- **🏷️ 机构**: Nanyang Technological University, Shenzhen Campus of Sun Yat-Sen University, Sea AI Lab,Singapore
- **会议**: CVPR 2025

### Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_Can_Large_Vision-Language_Models_Correct_Semantic_Grounding_Errors_By_Themselves_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Yuan-Hong Liao, Rafid Mahmood, Sanja Fidler, David Acuna
- **🏷️ 机构**: NVIDIA / University of Toronto
- **会议**: CVPR 2025

### BIOMEDICA: An Open Biomedical Image-Caption Archive, Dataset, and Vision-Language Models Derived from Scientific Literature.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lozano_BIOMEDICA_An_Open_Biomedical_Image-Caption_Archive_Dataset_and_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 14
- **作者**: Alejandro Lozano, Min Woo Sun, James Burgess, Liangyu Chen, Jeffrey J. Nirschl, Jeffrey Gu et al.
- **🏷️ 机构**: Stanford University
- **会议**: CVPR 2025

### Benchmarking Large Vision-Language Models via Directed Scene Graph for Comprehensive Image Captioning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_Benchmarking_Large_Vision-Language_Models_via_Directed_Scene_Graph_for_Comprehensive_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Fan Lu, Wei Wu, Kecheng Zheng, Shuailei Ma, Biao Gong, Jiawei Liu et al.
- **🏷️ 机构**: University of Science and Technology of China,MoE Key Laboratory of Brain-Inspired Intelligent Perception and Cognition, Ant Group, Northeastern University,China
- **会议**: CVPR 2025

### SPARC: Score Prompting and Adaptive Fusion for Zero-Shot Multi-Label Recognition in Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Miller_SPARC_Score_Prompting_and_Adaptive_Fusion_for_Zero-Shot_Multi-Label_Recognition_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Kevin Miller, Aditya Gangrade, Samarth Mishra, Kate Saenko, Venkatesh Saligrama
- **🏷️ 机构**: Boston University, Boston University and Meta AI (FAIR)
- **会议**: CVPR 2025

### VILA-M3: Enhancing Vision-Language Models with Medical Expert Knowledge.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Nath_VILA-M3_Enhancing_Vision-Language_Models_with_Medical_Expert_Knowledge_CVPR_2025_paper.html) · 📚 被引 27
- **作者**: Vishwesh Nath, Wenqi Li, Dong Yang, Andriy Myronenko, Mingxin Zheng, Yao Lu et al.
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2025

### CALICO: Part-Focused Semantic Co-Segmentation with Large Vision-Language Models.
- **链接**: [arXiv:2412.19331](https://arxiv.org/abs/2412.19331) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Nguyen_CALICO_Part-Focused_Semantic_Co-Segmentation_with_Large_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Kiet A. Nguyen, Adheesh Sunil Juvekar, Tianjiao Yu, Muntasir Wahed, Ismini Lourentzou
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Recent advances in Large Vision-Language Models (LVLMs) have enabled general-purpose vision tasks through visual instruction tuning. While existing LVLMs can generate segmentation masks from text prompts for single images, they struggle with segmentation-grounded reasoning across images, especially at finer granularities such as object parts. In this paper, we introduce the new task of part-focused semantic co-segmentation, which involves identifying and segmenting common objects, as well as common and unique object parts across images. To address this task, we present CALICO, the first LVLM designed for multi-image part-level reasoning segmentation. CALICO features two key components, a novel Correspondence Extraction Module that identifies semantic part-level correspondences, and Correspondence Adaptation Modules that embed this information into the LVLM to facilitate multi-image understanding in a parameter-efficient manner. To support training and evaluation, we curate MixedParts, a large-scale multi-image segmentation dataset containing $\sim$2.4M samples across $\sim$44K images spanning diverse object and part categories. Experimental results demonstrate that CALICO, with just 0.3% of its parameters finetuned, achieves strong performance on this challenging task.

### NLPrompt: Noise-Label Prompt Learning for Vision-Language Models.
- **链接**: [arXiv:2412.01256](https://arxiv.org/abs/2412.01256) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Pan_NLPrompt_Noise-Label_Prompt_Learning_for_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Bikang Pan, Qun Li, Xiaoying Tang, Wei Huang, Zhen Fang, Feng Liu et al.
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China, The Chinese University of Hong Kong,Shenzhen,China, RIKEN Center for Advanced Intelligence Project,Japan
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The emergence of vision-language foundation models, such as CLIP, has revolutionized image-text representation, enabling a broad range of applications via prompt learning. Despite its promise, real-world datasets often contain noisy labels that can degrade prompt learning performance. In this paper, we demonstrate that using mean absolute error (MAE) loss in prompt learning, named PromptMAE, significantly enhances robustness against noisy labels while maintaining high accuracy. Though MAE is straightforward and recognized for its robustness, it is rarely used in noisy-label learning due to its slow convergence and poor performance outside prompt learning scenarios. To elucidate the robustness of PromptMAE, we leverage feature learning theory to show that MAE can suppress the influence of noisy samples, thereby improving the signal-to-noise ratio and enhancing overall robustness. Additionally, we introduce PromptOT, a prompt-based optimal transport data purification method to enhance the robustness further. PromptOT employs text features in vision-language models as prototypes to construct an optimal transportation matrix. This matrix effectively partitions datasets into clean and noisy subsets, allowing for the application of cross-entropy loss to the clean subset and MAE loss to the noisy subset. Our Noise-Label Prompt Learning method, named NLPrompt, offers a simple and efficient approach that leverages the expressive representations and precise alignment capabilities of vision-language models for robust prompt learning. We validate NLPrompt through extensive experiments across various noise settings, demonstrating significant performance improvements.

### HalLoc: Token-level Localization of Hallucinations for Vision Language Models.
- **链接**: [arXiv:2506.10286](https://arxiv.org/abs/2506.10286) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Park_HalLoc_Token-level_Localization_of_Hallucinations_for_Vision_Language_Models_CVPR_2025_paper.html) · [代码](https://github.com/dbsltm/cvpr25_halloc) · 📚 被引 2
- **作者**: Eunkyu Park, Minyeong Kim, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Hallucinations pose a significant challenge to the reliability of large vision-language models, making their detection essential for ensuring accuracy in critical applications. Current detection methods often rely on computationally intensive models, leading to high latency and resource demands. Their definitive outcomes also fail to account for real-world scenarios where the line between hallucinated and truthful information is unclear. To address these issues, we propose HalLoc, a dataset designed for efficient, probabilistic hallucination detection. It features 150K token-level annotated samples, including hallucination types, across Visual Question Answering (VQA), instruction-following, and image captioning tasks. This dataset facilitates the development of models that detect hallucinations with graded confidence, enabling more informed user interactions. Additionally, we introduce a baseline model trained on HalLoc, offering low-overhead, concurrent hallucination detection during generation. The model can be seamlessly integrated into existing VLMs, improving reliability while preserving efficiency. The prospect of a robust plug-and-play hallucination detection module opens new avenues for enhancing the trustworthiness of vision-language models in real-world applications. The HalLoc dataset and code are publicly available at: https://github.com/dbsltm/cvpr25_halloc.

### Hyperbolic Safety-Aware Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Poppi_Hyperbolic_Safety-Aware_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Tobia Poppi, Tejaswi Kasarla, Pascal Mettes, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy, University of Amsterdam,Netherlands
- **会议**: CVPR 2025

### F3OCUS - Federated Finetuning of Vision-Language Foundation Models with Optimal Client Layer Updating Strategy via Multi-objective Meta-Heuristics.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Saha_F3OCUS_-_Federated_Finetuning_of_Vision-Language_Foundation_Models_with_Optimal_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Pramit Saha, Felix Wagner, Divyanshu Mishra, Can Peng, Anshul Thakur, David A. Clifton et al.
- **🏷️ 机构**: University of Oxford
- **会议**: CVPR 2025

### PARC: A Quantitative Framework Uncovering the Symmetries within Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Schmalfuss_PARC_A_Quantitative_Framework_Uncovering_the_Symmetries_within_Vision_Language_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Jenny Schmalfuss, Nadine Chang, Vibashan VS, Maying Shen, Andrés Bruhn, José M. Álvarez
- **🏷️ 机构**: University of Stuttgart, NVIDIA, Johns Hopkins University
- **会议**: CVPR 2025

### O-TPT: Orthogonality Constraints for Calibrating Test-time Prompt Tuning in Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sharifdeen_O-TPT_Orthogonality_Constraints_for_Calibrating_Test-time_Prompt_Tuning_in_Vision-Language_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Ashshak Sharifdeen, Muhammad Akhtar Munir, Sanoojan Baliah, Salman Khan, Muhammad Haris Khan
- **🏷️ 机构**: Mohamed Bin Zayed University of AI
- **会议**: CVPR 2025

### R-TPT: Improving Adversarial Robustness of Vision-Language Models through Test-Time Prompt Tuning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Sheng_R-TPT_Improving_Adversarial_Robustness_of_Vision-Language_Models_through_Test-Time_Prompt_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Lijun Sheng, Jian Liang, Zilei Wang, Ran He
- **🏷️ 机构**: University of Science and Technology of China, Chinese Academy of Sciences,NLPR &#x0026; MAIS, Institute of Automation
- **会议**: CVPR 2025

### Taxonomy-Aware Evaluation of Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Snaebjarnarson_Taxonomy-Aware_Evaluation_of_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: Vésteinn Snæbjarnarson, Kevin Du, Niklas Stoehr, Serge J. Belongie, Ryan Cotterell, Nico Lang et al.
- **🏷️ 机构**: （机构待查）
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
- Instruct-CLIP: Improving Instruction-Guided Image Editing with Automated Data Refinement Using Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
