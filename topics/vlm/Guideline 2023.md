# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 26 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLIP2: Contrastive Language-Image-Point Pretraining from Real-World Point Cloud Data.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01463) · 📚 被引 83
- **作者**: Yihan Zeng, Chenhan Jiang, Jiageng Mao, Jianhua Han, Chaoqiang Ye, Qingqiu Huang et al.
- **🏷️ 机构**: Huawei Noah&#x0027;s Ark Lab, Hong Kong University of Science and Technology, The Chinese University of Hong Kong
- **会议**: CVPR 2023

### Joint Visual Grounding and Tracking with Natural Language Specification.
- **链接**: [arXiv:2303.12027](https://arxiv.org/abs/2303.12027) · [代码](https://github.com/lizhou-cs/JointNLT) · 📚 被引 138
- **作者**: Li Zhou, Zikun Zhou, Kaige Mao, Zhenyu He
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, Peng Cheng Laboratory
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tracking by natural language specification aims to locate the referred target in a sequence based on the natural language description. Existing algorithms solve this issue in two steps, visual grounding and tracking, and accordingly deploy the separated grounding model and tracking model to implement these two steps, respectively. Such a separated framework overlooks the link between visual grounding and tracking, which is that the natural language descriptions provide global semantic cues for localizing the target for both two steps. Besides, the separated framework can hardly be trained end-to-end. To handle these issues, we propose a joint visual grounding and tracking framework, which reformulates grounding and tracking as a unified task: localizing the referred target based on the given visual-language references. Specifically, we propose a multi-source relation modeling module to effectively build the relation between the visual-language references and the test image. In addition, we design a temporal modeling module to provide a temporal clue with the guidance of the global semantic information for our model, which effectively improves the adaptability to the appearance variations of the target. Extensive experimental results on TNL2K, LaSOT, OTB99, and RefCOCOg demonstrate that our method performs favorably against state-of-the-art algorithms for both tracking and grounding. Code is available at https://github.com/lizhou-cs/JointNLT.

</details>

### Learning to Generate Text-Grounded Mask for Open-World Semantic Segmentation from Only Image-Text Pairs.
- **链接**: [arXiv:2212.00785](https://arxiv.org/abs/2212.00785) · [代码](https://github.com/kakaobrain/tcl) · 📚 被引 99
- **作者**: Junbum Cha, Jonghwan Mun, Byungseok Roh
- **🏷️ 机构**: Kakao Brain
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle open-world semantic segmentation, which aims at learning to segment arbitrary visual concepts in images, by using only image-text pairs without dense annotations. Existing open-world segmentation methods have shown impressive advances by employing contrastive learning (CL) to learn diverse visual concepts and transferring the learned image-level understanding to the segmentation task. However, these CL-based methods suffer from a train-test discrepancy, since it only considers image-text alignment during training, whereas segmentation requires region-text alignment during testing. In this paper, we proposed a novel Text-grounded Contrastive Learning (TCL) framework that enables a model to directly learn region-text alignment. Our method generates a segmentation mask for a given text, extracts text-grounded image embedding from the masked region, and aligns it with text embedding via TCL. By learning region-text alignment directly, our framework encourages a model to directly improve the quality of generated segmentation masks. In addition, for a rigorous and fair comparison, we present a unified evaluation protocol with widely used 8 semantic segmentation datasets. TCL achieves state-of-the-art zero-shot segmentation performances with large margins in all datasets. Code is available at https://github.com/kakaobrain/tcl.

</details>

### Accelerating Vision-Language Pretraining with Free Language Modeling.
- **链接**: [arXiv:2303.14038](https://arxiv.org/abs/2303.14038) · [代码](https://github.com/TencentARC/FLM) · 📚 被引 8
- **作者**: Teng Wang, Yixiao Ge, Feng Zheng, Ran Cheng, Ying Shan, Xiaohu Qie et al.
- **🏷️ 机构**: Southern University of Science and Technology, ARC Lab, Tencent PCG
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The state of the arts in vision-language pretraining (VLP) achieves exemplary performance but suffers from high training costs resulting from slow convergence and long training time, especially on large-scale web datasets. An essential obstacle to training efficiency lies in the entangled prediction rate (percentage of tokens for reconstruction) and corruption rate (percentage of corrupted tokens) in masked language modeling (MLM), that is, a proper corruption rate is achieved at the cost of a large portion of output tokens being excluded from prediction loss. To accelerate the convergence of VLP, we propose a new pretraining task, namely, free language modeling (FLM), that enables a 100% prediction rate with arbitrary corruption rates. FLM successfully frees the prediction rate from the tie-up with the corruption rate while allowing the corruption spans to be customized for each token to be predicted. FLM-trained models are encouraged to learn better and faster given the same GPU time by exploiting bidirectional contexts more flexibly. Extensive experiments show FLM could achieve an impressive 2.5x pretraining time reduction in comparison to the MLM-based methods, while keeping competitive performance on both vision-language understanding and generation tasks. Code will be public at https://github.com/TencentARC/FLM.

</details>

### Q: How to Specialize Large Vision-Language Models to Data-Scarce VQA Tasks? A: Self-Train on Unlabeled Images!
- **链接**: [arXiv:2306.03932](https://arxiv.org/abs/2306.03932) · [代码](https://github.com/codezakh/SelTDA) · 📚 被引 13
- **作者**: Zaid Khan, B. G. Vijay Kumar, Samuel Schulter, Xiang Yu, Yun Fu, Manmohan Chandraker
- **🏷️ 机构**: Northeastern University, NEC Labs America, Amazon
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Finetuning a large vision language model (VLM) on a target dataset after large scale pretraining is a dominant paradigm in visual question answering (VQA). Datasets for specialized tasks such as knowledge-based VQA or VQA in non natural-image domains are orders of magnitude smaller than those for general-purpose VQA. While collecting additional labels for specialized tasks or domains can be challenging, unlabeled images are often available. We introduce SelTDA (Self-Taught Data Augmentation), a strategy for finetuning large VLMs on small-scale VQA datasets. SelTDA uses the VLM and target dataset to build a teacher model that can generate question-answer pseudolabels directly conditioned on an image alone, allowing us to pseudolabel unlabeled images. SelTDA then finetunes the initial VLM on the original dataset augmented with freshly pseudolabeled images. We describe a series of experiments showing that our self-taught data augmentation increases robustness to adversarially searched questions, counterfactual examples and rephrasings, improves domain generalization, and results in greater retention of numerical reasoning skills. The proposed strategy requires no additional annotations or architectural modifications, and is compatible with any modern encoder-decoder multimodal transformer. Code available at https://github.com/codezakh/SelTDA.

</details>

### Task Residual for Tuning Vision-Language Models.
- **链接**: [arXiv:2211.10277](https://arxiv.org/abs/2211.10277) · [代码](https://github.com/geekyutao/TaskRes) · 📚 被引 117
- **作者**: Tao Yu, Zhihe Lu, Xin Jin, Zhibo Chen, Xinchao Wang
- **🏷️ 机构**: National University of Singapore, University of Science and Technology of China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale vision-language models (VLMs) pre-trained on billion-level data have learned general visual representations and broad visual concepts. In principle, the well-learned knowledge structure of the VLMs should be inherited appropriately when being transferred to downstream tasks with limited data. However, most existing efficient transfer learning (ETL) approaches for VLMs either damage or are excessively biased towards the prior knowledge, e.g., prompt tuning (PT) discards the pre-trained text-based classifier and builds a new one while adapter-style tuning (AT) fully relies on the pre-trained features. To address this, we propose a new efficient tuning approach for VLMs named Task Residual Tuning (TaskRes), which performs directly on the text-based classifier and explicitly decouples the prior knowledge of the pre-trained models and new knowledge regarding a target task. Specifically, TaskRes keeps the original classifier weights from the VLMs frozen and obtains a new classifier for the target task by tuning a set of prior-independent parameters as a residual to the original one, which enables reliable prior knowledge preservation and flexible task-specific knowledge exploration. The proposed TaskRes is simple yet effective, which significantly outperforms previous ETL methods (e.g., PT and AT) on 11 benchmark datasets while requiring minimal effort for the implementation. Our code is available at https://github.com/geekyutao/TaskRes.

</details>

### Adaptive Zone-aware Hierarchical Planner for Vision-Language Navigation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01432) · 📚 被引 38
- **作者**: Chen Gao, Xingyu Peng, Mi Yan, He Wang, Lirong Yang, Haibing Ren et al.
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, CFCS and School of EECS, Peking University, Meituan
- **会议**: CVPR 2023

### FAME-ViL: Multi-Tasking Vision-Language Model for Heterogeneous Fashion Tasks.
- **链接**: [arXiv:2303.02483](https://arxiv.org/abs/2303.02483) · [代码](https://github.com/BrandonHanx/FAME-ViL) · 📚 被引 50
- **作者**: Xiao Han, Xiatian Zhu, Licheng Yu, Li Zhang, Yi-Zhe Song, Tao Xiang
- **🏷️ 机构**: University of Surrey,CVSSP, Fudan University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the fashion domain, there exists a variety of vision-and-language (V+L) tasks, including cross-modal retrieval, text-guided image retrieval, multi-modal classification, and image captioning. They differ drastically in each individual input/output format and dataset size. It has been common to design a task-specific model and fine-tune it independently from a pre-trained V+L model (e.g., CLIP). This results in parameter inefficiency and inability to exploit inter-task relatedness. To address such issues, we propose a novel FAshion-focused Multi-task Efficient learning method for Vision-and-Language tasks (FAME-ViL) in this work. Compared with existing approaches, FAME-ViL applies a single model for multiple heterogeneous fashion tasks, therefore being much more parameter-efficient. It is enabled by two novel components: (1) a task-versatile architecture with cross-attention adapters and task-specific adapters integrated into a unified V+L model, and (2) a stable and effective multi-task training strategy that supports learning from heterogeneous data and prevents negative transfer. Extensive experiments on four fashion tasks show that our FAME-ViL can save 61.5% of parameters over alternatives, while significantly outperforming the conventional independently trained single-task models. Code is available at https://github.com/BrandonHanx/FAME-ViL.

</details>

### VILA: Learning Image Aesthetics from User Comments with Vision-Language Pretraining.
- **链接**: [arXiv:2303.14302](https://arxiv.org/abs/2303.14302) · 📚 被引 83
- **作者**: Junjie Ke, Keren Ye, Jiahui Yu, Yonghui Wu, Peyman Milanfar, Feng Yang
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Assessing the aesthetics of an image is challenging, as it is influenced by multiple factors including composition, color, style, and high-level semantics. Existing image aesthetic assessment (IAA) methods primarily rely on human-labeled rating scores, which oversimplify the visual aesthetic information that humans perceive. Conversely, user comments offer more comprehensive information and are a more natural way to express human opinions and preferences regarding image aesthetics. In light of this, we propose learning image aesthetics from user comments, and exploring vision-language pretraining methods to learn multimodal aesthetic representations. Specifically, we pretrain an image-text encoder-decoder model with image-comment pairs, using contrastive and generative objectives to learn rich and generic aesthetic semantics without human labels. To efficiently adapt the pretrained model for downstream IAA tasks, we further propose a lightweight rank-based adapter that employs text as an anchor to learn the aesthetic ranking concept. Our results show that our pretrained aesthetic vision-language model outperforms prior works on image aesthetic captioning over the AVA-Captions dataset, and it has powerful zero-shot capability for aesthetic tasks such as zero-shot style classification and zero-shot IAA, surpassing many supervised baselines. With only minimal finetuning parameters using the proposed adapter module, our model achieves state-of-the-art IAA performance over the AVA dataset.

</details>

### CrowdCLIP: Unsupervised Crowd Counting via Vision-Language Model.
- **链接**: [arXiv:2304.04231](https://arxiv.org/abs/2304.04231) · [代码](https://github.com/dk-liang/CrowdCLIP) · 📚 被引 90
- **作者**: Dingkang Liang, Jiahao Xie, Zhikang Zou, Xiaoqing Ye, Wei Xu, Xiang Bai
- **🏷️ 机构**: Huazhong University of Science and Technology, Beijing University of Posts and Telecommunications, Baidu Inc.,China
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised crowd counting relies heavily on costly manual labeling, which is difficult and expensive, especially in dense scenes. To alleviate the problem, we propose a novel unsupervised framework for crowd counting, named CrowdCLIP. The core idea is built on two observations: 1) the recent contrastive pre-trained vision-language model (CLIP) has presented impressive performance on various downstream tasks; 2) there is a natural mapping between crowd patches and count text. To the best of our knowledge, CrowdCLIP is the first to investigate the vision language knowledge to solve the counting problem. Specifically, in the training stage, we exploit the multi-modal ranking loss by constructing ranking text prompts to match the size-sorted crowd patches to guide the image encoder learning. In the testing stage, to deal with the diversity of image patches, we propose a simple yet effective progressive filtering strategy to first select the highly potential crowd patches and then map them into the language space with various counting intervals. Extensive experiments on five challenging datasets demonstrate that the proposed CrowdCLIP achieves superior performance compared to previous unsupervised state-of-the-art counting methods. Notably, CrowdCLIP even surpasses some popular fully-supervised methods under the cross-dataset setting. The source code will be available at https://github.com/dk-liang/CrowdCLIP.

</details>

### @ CREPE: Can Vision-Language Foundation Models Reason Compositionally?
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01050) · 📚 被引 73
- **作者**: Zixian Ma, Jerry Hong, Mustafa Omer Gul, Mona Gandhi, Irena Gao, Ranjay Krishna
- **🏷️ 机构**: Stanford University, Cornell University, University of Pennsylvania
- **会议**: CVPR 2023

### HOICLIP: Efficient Knowledge Transfer for HOI Detection with Vision-Language Models.
- **链接**: [arXiv:2303.15786](https://arxiv.org/abs/2303.15786) · [代码](https://github.com/Artanic30/HOICLIP) · 📚 被引 91
- **作者**: Shan Ning, Longtian Qiu, Yongfei Liu, Xuming He
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China, ByteDance Inc.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-Object Interaction (HOI) detection aims to localize human-object pairs and recognize their interactions. Recently, Contrastive Language-Image Pre-training (CLIP) has shown great potential in providing interaction prior for HOI detectors via knowledge distillation. However, such approaches often rely on large-scale training data and suffer from inferior performance under few/zero-shot scenarios. In this paper, we propose a novel HOI detection framework that efficiently extracts prior knowledge from CLIP and achieves better generalization. In detail, we first introduce a novel interaction decoder to extract informative regions in the visual feature map of CLIP via a cross-attention mechanism, which is then fused with the detection backbone by a knowledge integration block for more accurate human-object pair detection. In addition, prior knowledge in CLIP text encoder is leveraged to generate a classifier by embedding HOI descriptions. To distinguish fine-grained interactions, we build a verb classifier from training data via visual semantic arithmetic and a lightweight verb representation adapter. Furthermore, we propose a training-free enhancement to exploit global HOI predictions from CLIP. Extensive experiments demonstrate that our method outperforms the state of the art by a large margin on various settings, e.g. +4.04 mAP on HICO-Det. The source code is available in https://github.com/Artanic30/HOICLIP.

</details>

### DeAR: Debiasing Vision-Language Models with Additive Residuals.
- **链接**: [arXiv:2303.10431](https://arxiv.org/abs/2303.10431) · 📚 被引 34
- **作者**: Ashish Seth, Mayur Hemani, Chirag Agarwal
- **🏷️ 机构**: IIT Madras,India, Adobe Inc.
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large pre-trained vision-language models (VLMs) reduce the time for developing predictive models for various vision-grounded language downstream tasks by providing rich, adaptable image and text representations. However, these models suffer from societal biases owing to the skewed distribution of various identity groups in the training data. These biases manifest as the skewed similarity between the representations for specific text concepts and images of people of different identity groups and, therefore, limit the usefulness of such models in real-world high-stakes applications. In this work, we present DeAR (Debiasing with Additive Residuals), a novel debiasing method that learns additive residual image representations to offset the original representations, ensuring fair output representations. In doing so, it reduces the ability of the representations to distinguish between the different identity groups. Further, we observe that the current fairness tests are performed on limited face image datasets that fail to indicate why a specific text concept should/should not apply to them. To bridge this gap and better evaluate DeAR, we introduce the Protected Attribute Tag Association (PATA) dataset - a new context-based bias benchmarking dataset for evaluating the fairness of large pre-trained VLMs. Additionally, PATA provides visual context for a diverse human population in different scenarios with both positive and negative connotations. Experimental results for fairness and zero-shot performance preservation using multiple datasets demonstrate the efficacy of our framework.

</details>

### You Need Multiple Exiting: Dynamic Early Exiting for Accelerating Unified Vision Language Model.
- **链接**: [arXiv:2211.11152](https://arxiv.org/abs/2211.11152) · 📚 被引 31
- **作者**: Shengkun Tang, Yaqing Wang, Zhenglun Kong, Tianchi Zhang, Yao Li, Caiwen Ding et al.
- **🏷️ 机构**: North Carolina State University,Raleigh,USA, Google Research,New York,USA, Northeastern University,Boston,USA
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale Transformer models bring significant improvements for various downstream vision language tasks with a unified architecture. The performance improvements come with increasing model size, resulting in slow inference speed and increased cost for severing. While some certain predictions benefit from the full complexity of the large-scale model, not all of inputs need the same amount of computation to conduct, potentially leading to computation resource waste. To handle this challenge, early exiting is proposed to adaptively allocate computational power in term of input complexity to improve inference efficiency. The existing early exiting strategies usually adopt output confidence based on intermediate layers as a proxy of input complexity to incur the decision of skipping following layers. However, such strategies cannot apply to encoder in the widely-used unified architecture with both encoder and decoder due to difficulty of output confidence estimation in the encoder. It is suboptimal in term of saving computation power to ignore the early exiting in encoder component. To handle this challenge, we propose a novel early exiting strategy for unified visual language models, which allows dynamically skip the layers in encoder and decoder simultaneously in term of input layer-wise similarities with multiple times of early exiting, namely \textbf{MuE}. By decomposing the image and text modalities in the encoder, MuE is flexible and can skip different layers in term of modalities, advancing the inference efficiency while minimizing performance drop. Experiments on the SNLI-VE and MS COCO datasets show that the proposed approach MuE can reduce expected inference time by up to 50\% and 40\% while maintaining 99\% and 96\% performance respectively.

</details>

### Improving Commonsense in Vision-Language Models via Knowledge Graph Riddles.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00259) · 📚 被引 7
- **作者**: Shuquan Ye, Yujia Xie, Dongdong Chen, Yichong Xu, Lu Yuan, Chenguang Zhu et al.
- **🏷️ 机构**: City University of Hong Kong, Microsoft
- **会议**: CVPR 2023

### Meta-Personalizing Vision-Language Models to Find Named Instances in Video.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01833) · 📚 被引 13
- **作者**: Chun-Hsiao Yeh, Bryan C. Russell, Josef Sivic, Fabian Caba Heilbron, Simon Jenni
- **🏷️ 机构**: University of California,Berkeley, Adobe Research, Czech Institute of Informatics, Robotics and Cybernetics at the Czech Technical University in Prague (CIIRC CTU)
- **会议**: CVPR 2023

### GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01054) · 📚 被引 13
- **作者**: Da Yin, Feng Gao, Govind Thattai, Michael Johnston, Kai-Wei Chang
- **🏷️ 机构**: University of California,Los Angeles, Amazon Alexa AI
- **会议**: CVPR 2023

### IFSeg: Image-free Semantic Segmentation via Vision-Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00290) · 📚 被引 17
- **作者**: Sukmin Yun, Seong Hyeon Park, Paul Hongsuck Seo, Jinwoo Shin
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST), Google Research
- **会议**: CVPR 2023

### Reproducible Scaling Laws for Contrastive Language-Image Learning.
- **链接**: [arXiv:2212.07143](https://arxiv.org/abs/2212.07143) · [代码](https://github.com/LAION-AI/scaling-laws-openclip) · 📚 被引 620
- **作者**: Mehdi Cherti, Romain Beaumont, Ross Wightman, Mitchell Wortsman, Gabriel Ilharco, Cade Gordon et al.
- **🏷️ 机构**: LAION, HuggingFace, University of Washington
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling up neural networks has led to remarkable performance across a wide range of tasks. Moreover, performance often follows reliable scaling laws as a function of training set size, model size, and compute, which offers valuable guidance as large-scale experiments are becoming increasingly expensive. However, previous work on scaling laws has primarily used private data \& models or focused on uni-modal language or vision learning. To address these limitations, we investigate scaling laws for contrastive language-image pre-training (CLIP) with the public LAION dataset and the open-source OpenCLIP repository. Our large-scale experiments involve models trained on up to two billion image-text pairs and identify power law scaling for multiple downstream tasks including zero-shot classification, retrieval, linear probing, and end-to-end fine-tuning. We find that the training distribution plays a key role in scaling laws as the OpenAI and OpenCLIP models exhibit different scaling behavior despite identical model architectures and similar training recipes. We open-source our evaluation workflow and all models, including the largest public CLIP models, to ensure reproducibility and make scaling laws research more accessible. Source code and instructions to reproduce this study will be available at https://github.com/LAION-AI/scaling-laws-openclip

</details>

### MaskCLIP: Masked Self-Distillation Advances Contrastive Language-Image Pretraining.
- **链接**: [arXiv:2208.12262](https://arxiv.org/abs/2208.12262) · [代码](https://github.com/LightDXY/MaskCLIP) · 📚 被引 162
- **作者**: Xiaoyi Dong, Jianmin Bao, Yinglin Zheng, Ting Zhang, Dongdong Chen, Hao Yang et al.
- **🏷️ 机构**: University of Science and Technology of China, Microsoft Research Asia, Xiamen University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a simple yet effective framework MaskCLIP, which incorporates a newly proposed masked self-distillation into contrastive language-image pretraining. The core idea of masked self-distillation is to distill representation from a full image to the representation predicted from a masked image. Such incorporation enjoys two vital benefits. First, masked self-distillation targets local patch representation learning, which is complementary to vision-language contrastive focusing on text-related representation. Second, masked self-distillation is also consistent with vision-language contrastive from the perspective of training objective as both utilize the visual encoder for feature aligning, and thus is able to learn local semantics getting indirect supervision from the language. We provide specially designed experiments with a comprehensive analysis to validate the two benefits. Symmetrically, we also introduce the local semantic supervision into the text branch, which further improves the pretraining performance. With extensive experiments, we show that MaskCLIP, when applied to various challenging downstream tasks, achieves superior results in linear probing, finetuning, and zero-shot performance with the guidance of the language encoder. Code will be release at \url{https://github.com/LightDXY/MaskCLIP}.

</details>

## 跨领域论文（完整笔记在其他领域）

- CLIP the Gap: A Single Domain Generalization Approach for Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Open-Vocabulary Semantic Segmentation with Mask-adapted CLIP. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models. → [multimodal](../multimodal/Guideline%202023.md)
- Vita-CLIP: Video and text adaptive CLIP via Multimodal Prompting. → [multimodal](../multimodal/Guideline%202023.md)
- CLIP-S4: Language-Guided Self-Supervised Semantic Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
