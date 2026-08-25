# Multimodal — 2025 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 31 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### AVF-MAE++: Scaling Affective Video Facial Masked Autoencoders via Efficient Audio-Visual Self-Supervised Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_AVF-MAE_Scaling_Affective_Video_Facial_Masked_Autoencoders_via_Efficient_Audio-Visual_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: Xuecheng Wu, Heli Sun, Yifan Wang, Jiayu Nie, Jie Zhang, Yabing Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Computer Science and Technology, University of Science and Technology of China, A*STAR,CFAR and IHPC
- **会议**: CVPR 2025

### ROD-MLLM: Towards More Reliable Object Detection in Multimodal Large Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_ROD-MLLM_Towards_More_Reliable_Object_Detection_in_Multimodal_Large_Language_CVPR_2025_paper.html)
- **作者**: Heng Yin, Yuqiang Ren, Ke Yan, Shouhong Ding, Yongtao Hao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting.
- **链接**: [arXiv:2506.09952](https://arxiv.org/abs/2506.09952) · [代码](https://github.com/wangzy22/UniPre3D)
- **作者**: Ziyi Wang, Yanran Zhang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,Department of Automation,China
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The scale diversity of point cloud data presents significant challenges in developing unified representation learning techniques for 3D vision. Currently, there are few unified 3D models, and no existing pre-training method is equally effective for both object- and scene-level point clouds. In this paper, we introduce UniPre3D, the first unified pre-training method that can be seamlessly applied to point clouds of any scale and 3D models of any architecture. Our approach predicts Gaussian primitives as the pre-training task and employs differentiable Gaussian splatting to render images, enabling precise pixel-level supervision and end-to-end optimization. To further regulate the complexity of the pre-training task and direct the model's focus toward geometric structures, we integrate 2D features from pre-trained image models to incorporate well-established texture knowledge. We validate the universal effectiveness of our proposed method through extensive experiments across a variety of object- and scene-level tasks, using diverse point cloud models as backbones. Code is available at https://github.com/wangzy22/UniPre3D.

### DreamTrack: Dreaming the Future for Multimodal Visual Object Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_DreamTrack_Dreaming_the_Future_for_Multimodal_Visual_Object_Tracking_CVPR_2025_paper.html)
- **作者**: Mingzhe Guo, Weiping Tan, Wenyu Ran, Liping Jing, Zhipeng Zhang
- **🏷️ 机构**: Beijing Jiaotong University, Shanghai Jiaotong University
- **会议**: CVPR 2025

### MambaVLT: Time-Evolving Multimodal State Space Model for Vision-Language Tracking.
- **链接**: [arXiv:2411.15459](https://arxiv.org/abs/2411.15459)
- **作者**: Xinqi Liu, Li Zhou, Zikun Zhou, Jianqiu Chen, Zhenyu He
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, Pengcheng Laboratory
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The vision-language tracking task aims to perform object tracking based on various modality references. Existing Transformer-based vision-language tracking methods have made remarkable progress by leveraging the global modeling ability of self-attention. However, current approaches still face challenges in effectively exploiting the temporal information and dynamically updating reference features during tracking. Recently, the State Space Model (SSM), known as Mamba, has shown astonishing ability in efficient long-sequence modeling. Particularly, its state space evolving process demonstrates promising capabilities in memorizing multimodal temporal information with linear complexity. Witnessing its success, we propose a Mamba-based vision-language tracking model to exploit its state space evolving ability in temporal space for robust multimodal tracking, dubbed MambaVLT. In particular, our approach mainly integrates a time-evolving hybrid state space block and a selective locality enhancement block, to capture contextual information for multimodal modeling and adaptive reference feature update. Besides, we introduce a modality-selection module that dynamically adjusts the weighting between visual and language references, mitigating potential ambiguities from either reference type. Extensive experimental results show that our method performs favorably against state-of-the-art trackers across diverse benchmarks.

### Cross-Modal and Uncertainty-Aware Agglomeration for Open-Vocabulary 3D Scene Understanding.
- **链接**: [arXiv:2503.16707](https://arxiv.org/abs/2503.16707) · [代码](https://github.com/TyroneLi/CUA_O3D)
- **作者**: Jinlong Li, Cristiano Saltori, Fabio Poiesi, Nicu Sebe
- **🏷️ 机构**: University of Trento, Fondazione Bruno Kessler
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The lack of a large-scale 3D-text corpus has led recent works to distill open-vocabulary knowledge from vision-language models (VLMs). However, these methods typically rely on a single VLM to align the feature spaces of 3D models within a common language space, which limits the potential of 3D models to leverage the diverse spatial and semantic capabilities encapsulated in various foundation models. In this paper, we propose Cross-modal and Uncertainty-aware Agglomeration for Open-vocabulary 3D Scene Understanding dubbed CUA-O3D, the first model to integrate multiple foundation models-such as CLIP, DINOv2, and Stable Diffusion-into 3D scene understanding. We further introduce a deterministic uncertainty estimation to adaptively distill and harmonize the heterogeneous 2D feature embeddings from these models. Our method addresses two key challenges: (1) incorporating semantic priors from VLMs alongside the geometric knowledge of spatially-aware vision foundation models, and (2) using a novel deterministic uncertainty estimation to capture model-specific uncertainties across diverse semantic and geometric sensitivities, helping to reconcile heterogeneous representations during training. Extensive experiments on ScanNetV2 and Matterport3D demonstrate that our method not only advances open-vocabulary segmentation but also achieves robust cross-domain alignment and competitive spatial perception capabilities. The code will be available at: https://github.com/TyroneLi/CUA_O3D.

### Towards Open-Vocabulary Audio-Visual Event Localization.
- **链接**: [arXiv:2411.11278](https://arxiv.org/abs/2411.11278)
- **作者**: Jinxing Zhou, Dan Guo, Ruohao Guo, Yuxin Mao, Jingjing Hu, Yiran Zhong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The Audio-Visual Event Localization (AVEL) task aims to temporally locate and classify video events that are both audible and visible. Most research in this field assumes a closed-set setting, which restricts these models' ability to handle test data containing event categories absent (unseen) during training. Recently, a few studies have explored AVEL in an open-set setting, enabling the recognition of unseen events as ``unknown'', but without providing category-specific semantics. In this paper, we advance the field by introducing the Open-Vocabulary Audio-Visual Event Localization (OV-AVEL) problem, which requires localizing audio-visual events and predicting explicit categories for both seen and unseen data at inference. To address this new task, we propose the OV-AVEBench dataset, comprising 24,800 videos across 67 real-life audio-visual scenes (seen:unseen = 46:21), each with manual segment-level annotation. We also establish three evaluation metrics for this task. Moreover, we investigate two baseline approaches, one training-free and one using a further fine-tuning paradigm. Specifically, we utilize the unified multimodal space from the pretrained ImageBind model to extract audio, visual, and textual (event classes) features. The training-free baseline then determines predictions by comparing the consistency of audio-text and visual-text feature similarities. The fine-tuning baseline incorporates lightweight temporal layers to encode temporal relations within the audio and visual modalities, using OV-AVEBench training data for model fine-tuning. We evaluate these baselines on the proposed OV-AVEBench dataset and discuss potential directions for future work in this new field.

### Towards Zero-Shot Anomaly Detection and Reasoning with Multimodal Large Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_Towards_Zero-Shot_Anomaly_Detection_and_Reasoning_with_Multimodal_Large_Language_CVPR_2025_paper.html)
- **作者**: Jiacong Xu, Shao-Yuan Lo, Bardia Safaei, Vishal M. Patel, Isht Dwivedi
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### S4-Driver: Scalable Self-Supervised Driving Multimodal Large Language Model with Spatio-Temporal Visual Representation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xie_S4-Driver_Scalable_Self-Supervised_Driving_Multimodal_Large_Language_Model_with_Spatio-Temporal_CVPR_2025_paper.html)
- **作者**: Yichen Xie, Runsheng Xu, Tong He, Jyh-Jing Hwang, Katie Luo, Jingwei Ji et al.
- **🏷️ 机构**: Fudan / Shanghai AI Lab
- **会议**: CVPR 2025

### MMTL-UniAD: A Unified Framework for Multimodal and Multi-Task Learning in Assistive Driving Perception.
- **链接**: [arXiv:2504.02264](https://arxiv.org/abs/2504.02264) · [代码](https://github.com/Wenzhuo-Liu/MMTL-UniAD)
- **作者**: Wenzhuo Liu, Wenshuo Wang, Yicheng Qiao, Qiannan Guo, Jiayin Zhu, Pengfei Li et al.
- **🏷️ 机构**: Beijing Institute of Technology,Zhuhai, Tsinghua University, HKUST(GZ)
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Advanced driver assistance systems require a comprehensive understanding of the driver's mental/physical state and traffic context but existing works often neglect the potential benefits of joint learning between these tasks. This paper proposes MMTL-UniAD, a unified multi-modal multi-task learning framework that simultaneously recognizes driver behavior (e.g., looking around, talking), driver emotion (e.g., anxiety, happiness), vehicle behavior (e.g., parking, turning), and traffic context (e.g., traffic jam, traffic smooth). A key challenge is avoiding negative transfer between tasks, which can impair learning performance. To address this, we introduce two key components into the framework: one is the multi-axis region attention network to extract global context-sensitive features, and the other is the dual-branch multimodal embedding to learn multimodal embeddings from both task-shared and task-specific features. The former uses a multi-attention mechanism to extract task-relevant features, mitigating negative transfer caused by task-unrelated features. The latter employs a dual-branch structure to adaptively adjust task-shared and task-specific parameters, enhancing cross-task knowledge transfer while reducing task conflicts. We assess MMTL-UniAD on the AIDE dataset, using a series of ablation studies, and show that it outperforms state-of-the-art methods across all four tasks. The code is available on https://github.com/Wenzhuo-Liu/MMTL-UniAD.

### Generating Multimodal Driving Scenes via Next-Scene Prediction.
- **链接**: [arXiv:2503.14945](https://arxiv.org/abs/2503.14945)
- **作者**: Yanhao Wu, Haoyang Zhang, Tianwei Lin, Lichao Huang, Shujie Luo, Rui Wu et al.
- **🏷️ 机构**: XJTU,School of Software Engineering, Horizon Robotics
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Generative models in Autonomous Driving (AD) enable diverse scene creation, yet existing methods fall short by only capturing a limited range of modalities, restricting the capability of generating controllable scenes for comprehensive evaluation of AD systems. In this paper, we introduce a multimodal generation framework that incorporates four major data modalities, including a novel addition of map modality. With tokenized modalities, our scene sequence generation framework autoregressively predicts each scene while managing computational demands through a two-stage approach. The Temporal AutoRegressive (TAR) component captures inter-frame dynamics for each modality while the Ordered AutoRegressive (OAR) component aligns modalities within each scene by sequentially predicting tokens in a fixed order. To maintain coherence between map and ego-action modalities, we introduce the Action-aware Map Alignment (AMA) module, which applies a transformation based on the ego-action to maintain coherence between these modalities. Our framework effectively generates complex, realistic driving scenes over extended sequences, ensuring multimodal consistency and offering fine-grained control over scene elements. Project page: https://yanhaowu.github.io/UMGen/

### Recurrence-Enhanced Vision-and-Language Transformers for Robust Multimodal Document Retrieval.
- **链接**: [arXiv:2503.01980](https://arxiv.org/abs/2503.01980) · [代码](https://github.com/aimagelab/ReT)
- **作者**: Davide Caffagni, Sara Sarto, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Cross-modal retrieval is gaining increasing efficacy and interest from the research community, thanks to large-scale training, novel architectural and learning designs, and its application in LLMs and multimodal LLMs. In this paper, we move a step forward and design an approach that allows for multimodal queries, composed of both an image and a text, and can search within collections of multimodal documents, where images and text are interleaved. Our model, ReT, employs multi-level representations extracted from different layers of both visual and textual backbones, both at the query and document side. To allow for multi-level and cross-modal understanding and feature extraction, ReT employs a novel Transformer-based recurrent cell that integrates both textual and visual features at different layers, and leverages sigmoidal gates inspired by the classical design of LSTMs. Extensive experiments on M2KR and M-BEIR benchmarks show that ReT achieves state-of-the-art performance across diverse settings. Our source code and trained models are publicly available at https://github.com/aimagelab/ReT.

### MIMO: A Medical Vision Language Model with Visual Referring Multimodal Input and Pixel Grounding Multimodal Output.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_MIMO_A_Medical_Vision_Language_Model_with_Visual_Referring_Multimodal_CVPR_2025_paper.html)
- **作者**: Yanyuan Chen, Dexuan Xu, Yu Huang, Songkun Zhan, Hanpin Wang, Dongxue Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Align-KD: Distilling Cross-Modal Alignment Knowledge for Mobile Vision-Language Large Model Enhancement.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Feng_Align-KD_Distilling_Cross-Modal_Alignment_Knowledge_for_Mobile_Vision-Language_Large_Model_CVPR_2025_paper.html)
- **作者**: Qianhan Feng, Wenshuo Li, Tong Lin, Xinghao Chen
- **🏷️ 机构**: Peking University,State Key Laboratory of General Artificial Intelligence, School of Intelligence Science and Technology,China, Huawei Noah&#x2019;s Ark Lab,China
- **会议**: CVPR 2025

### MMRL: Multi-Modal Representation Learning for Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_MMRL_Multi-Modal_Representation_Learning_for_Vision-Language_Models_CVPR_2025_paper.html)
- **作者**: Yuncheng Guo, Xiaodong Gu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Rethinking Vision-Language Model in Face Forensics: Multi-Modal Interpretable Forged Face Detector.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Rethinking_Vision-Language_Model_in_Face_Forensics_Multi-Modal_Interpretable_Forged_Face_CVPR_2025_paper.html)
- **作者**: Xiao Guo, Xiufeng Song, Yue Zhang, Xiaohong Liu, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Enhancing Vision-Language Compositional Understanding with Multimodal Synthetic Data.
- **链接**: [arXiv:2503.01167](https://arxiv.org/abs/2503.01167)
- **作者**: Haoxin Li, Boyang Li
- **🏷️ 机构**: Nanyang Technological University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Paired image-text data with subtle variations in-between (e.g., people holding surfboards vs. people holding shovels) hold the promise of producing Vision-Language Models with proper compositional understanding. Synthesizing such training data from generative models is a highly coveted prize due to the reduced cost of data collection. However, synthesizing training images for compositional learning presents three challenges: (1) efficiency in generating large quantities of images, (2) text alignment between the generated image and the caption in the exact place of the subtle change, and (3) image fidelity in ensuring sufficient similarity with the original real images in all other places. We propose SPARCL (Synthetic Perturbations for Advancing Robust Compositional Learning), which integrates image feature injection into a fast text-to-image generative model, followed by an image style transfer step, to meet the three challenges. Further, to cope with any residual issues of text alignment, we propose an adaptive margin loss to filter out potentially incorrect synthetic samples and focus the learning on informative hard samples. Evaluation on four compositional understanding benchmarks demonstrates that SPARCL significantly improves the compositionality of CLIP, boosting the average accuracy of the CLIP base model by over 8% across all benchmarks and outperforming state-of-the-art methods by 2% on three benchmarks.

### Multi-modal Contrastive Learning with Negative Sampling Calibration for Phenotypic Drug Discovery.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Rao_Multi-modal_Contrastive_Learning_with_Negative_Sampling_Calibration_for_Phenotypic_Drug_CVPR_2025_paper.html)
- **作者**: Jiahua Rao, Hanjing Lin, Leyu Chen, Jiancong Xie, Shuangjia Zheng, Yuedong Yang
- **🏷️ 机构**: Sun Yat-Sen University,School of Computer Science and Engineering, Shanghai Jiao Tong University,Global Institute of Future Technology
- **会议**: CVPR 2025

### DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models.
- **链接**: [arXiv:2503.02175](https://arxiv.org/abs/2503.02175) · [代码](https://github.com/vbdi/divprune) · 📚 被引 14
- **作者**: Saeed Ranjbar Alvar, Gursimran Singh, Mohammad Akbari, Yong Zhang
- **🏷️ 机构**: Huawei Technologies Canada Co., Ltd.
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Large Multimodal Models (LMMs) have emerged as powerful models capable of understanding various data modalities, including text, images, and videos. LMMs encode both text and visual data into tokens that are then combined and processed by an integrated Large Language Model (LLM). Including visual tokens substantially increases the total token count, often by thousands. The increased input length for LLM significantly raises the complexity of inference, resulting in high latency in LMMs. To address this issue, token pruning methods, which remove part of the visual tokens, are proposed. The existing token pruning methods either require extensive calibration and fine-tuning or rely on suboptimal importance metrics which results in increased redundancy among the retained tokens. In this paper, we first formulate token pruning as Max-Min Diversity Problem (MMDP) where the goal is to select a subset such that the diversity among the selected {tokens} is maximized. Then, we solve the MMDP to obtain the selected subset and prune the rest. The proposed method, DivPrune, reduces redundancy and achieves the highest diversity of the selected tokens. By ensuring high diversity, the selected tokens better represent the original tokens, enabling effective performance even at high pruning ratios without requiring fine-tuning. Extensive experiments with various LMMs show that DivPrune achieves state-of-the-art accuracy over 16 image- and video-language datasets. Additionally, DivPrune reduces both the end-to-end latency and GPU memory usage for the tested models. The code is available $\href{https://github.com/vbdi/divprune}{\text{here}}$.

### TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_TopV_Compatible_Token_Pruning_with_Inference_Time_Optimization_for_Fast_CVPR_2025_paper.html)
- **作者**: Cheng Yang, Yang Sui, Jinqi Xiao, Lingyi Huang, Yu Gong, Chendi Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### CASP: Compression of Large Multimodal Models Based on Attention Sparsity.
- **链接**: [arXiv:2503.05936](https://arxiv.org/abs/2503.05936) · 📚 被引 2
- **作者**: Mohsen Gholami, Mohammad Akbari, Kevin Cannons, Yong Zhang
- **🏷️ 机构**: Huawei Technologies Canada Co., Ltd.
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > In this work, we propose an extreme compression technique for Large Multimodal Models (LMMs). While previous studies have explored quantization as an efficient post-training compression method for Large Language Models (LLMs), low-bit compression for multimodal models remains under-explored. The redundant nature of inputs in multimodal models results in a highly sparse attention matrix. We theoretically and experimentally demonstrate that the attention matrix's sparsity bounds the compression error of the Query and Key weight matrices. Based on this, we introduce CASP, a model compression technique for LMMs. Our approach performs a data-aware low-rank decomposition on the Query and Key weight matrix, followed by quantization across all layers based on an optimal bit allocation process. CASP is compatible with any quantization technique and enhances state-of-the-art 2-bit quantization methods (AQLM and QuIP#) by an average of 21% on image- and video-language benchmarks.

### Multi-modal Knowledge Distillation-based Human Trajectory Forecasting.
- **链接**: [arXiv:2503.22201](https://arxiv.org/abs/2503.22201) · [代码](https://github.com/Jaewoo97/KDTF) · 📚 被引 10
- **作者**: Jaewoo Jeong, Seohee Lee, Daehee Park, Giwon Lee, Kuk-Jin Yoon
- **🏷️ 机构**: Visual Intelligence Lab., KAIST,Korea, Intelligent Systems and Learning Lab., DGIST,Korea
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Pedestrian trajectory forecasting is crucial in various applications such as autonomous driving and mobile robot navigation. In such applications, camera-based perception enables the extraction of additional modalities (human pose, text) to enhance prediction accuracy. Indeed, we find that textual descriptions play a crucial role in integrating additional modalities into a unified understanding. However, online extraction of text requires the use of VLM, which may not be feasible for resource-constrained systems. To address this challenge, we propose a multi-modal knowledge distillation framework: a student model with limited modality is distilled from a teacher model trained with full range of modalities. The comprehensive knowledge of a teacher model trained with trajectory, human pose, and text is distilled into a student model using only trajectory or human pose as a sole supplement. In doing so, we separately distill the core locomotion insights from intra-agent multi-modality and inter-agent interaction. Our generalizable framework is validated with two state-of-the-art models across three datasets on both ego-view (JRDB, SIT) and BEV-view (ETH/UCY) setups, utilizing both annotated and VLM-generated text captions. Distilled student models show consistent improvement in all prediction metrics for both full and instantaneous observations, improving up to ~13%. The code is available at https://github.com/Jaewoo97/KDTF.

### Cross-Modal Distillation for 2D/3D Multi-Object Discovery from 2D Motion.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lahlali_Cross-Modal_Distillation_for_2D3D_Multi-Object_Discovery_from_2D_Motion_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Saad Lahlali, Sandra Kara, Hejer Ammar, Florian Chabot, Nicolas Granger, Hervé Le Borgne et al.
- **🏷️ 机构**: Universit&#x00E9; Paris-Saclay,CEA, List,Palaiseau,France,F-91120
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- AVQACL: A Novel Benchmark for Audio-Visual Question Answering Continual Learning. → [continual-learning](../continual-learning/Guideline%202025.md)
- CorrBEV: Multi-View 3D Object Detection by Correlation Learning with Multi-modal Prototypes. → [3d-detection](../3d-detection/Guideline%202025.md)
- SP3D: Boosting Sparsely-Supervised 3D Object Detection via Accurate Cross-Modal Semantic Prompts. → [3d-detection](../3d-detection/Guideline%202025.md)
- Cross-Modal 3D Representation with Multi-View Images and Point Clouds. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- SDGOCC: Semantic and Depth-Guided Bird's-Eye View Transformation for 3D Multimodal Occupancy Prediction. → [bev](../bev/Guideline%202025.md)
- Distilling Multi-modal Large Language Models for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- GoalFlow: Goal-Driven Flow Matching for Multimodal Trajectories Generation in End-to-End Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Revisiting Audio-Visual Segmentation with Vision-Centric Transformer. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
