# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLIP2: Contrastive Language-Image-Point Pretraining from Real-World Point Cloud Data.
- **链接**: [arXiv:2303.12417](https://arxiv.org/abs/2303.12417) · 📚 被引 84
- **作者**: Yihan Zeng, Chenhan Jiang, Jiageng Mao, Jianhua Han, Chaoqiang Ye, Qingqiu Huang et al.
- **🏷️ 机构**: Huawei Noah&#x0027;s Ark Lab, Hong Kong University of Science and Technology, The Chinese University of Hong Kong
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Language-Image Pre-training, benefiting from large-scale unlabeled text-image pairs, has demonstrated great performance in open-world vision understanding tasks. However, due to the limited Text-3D data pairs, adapting the success of 2D Vision-Language Models (VLM) to the 3D space remains an open problem. Existing works that leverage VLM for 3D understanding generally resort to constructing intermediate 2D representations for the 3D data, but at the cost of losing 3D geometry information. To take a step toward open-world 3D vision understanding, we propose Contrastive Language-Image-Point Cloud Pretraining (CLIP$^2$) to directly learn the transferable 3D point cloud representation in realistic scenarios with a novel proxy alignment mechanism. Specifically, we exploit naturally-existed correspondences in 2D and 3D scenarios, and build well-aligned and instance-based text-image-point proxies from those complex scenarios. On top of that, we propose a cross-modal contrastive objective to learn semantic and instance-level aligned point cloud representation. Experimental results on both indoor and outdoor scenarios show that our learned 3D representation has great transfer ability in downstream tasks, including zero-shot and few-shot 3D recognition, which boosts the state-of-the-art methods by large margins. Furthermore, we provide analyses of the capability of different representations in real scenarios and present the optional ensemble scheme.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Language-Image Pre-training, benefiting from large-scale unlabeled text-image pairs, has demonstrated great performance in open-world vision understanding tasks. However, due to the limited Text-3D data pairs, adapting the success of 2D Vision-Language Models (VLM) to the 3D space remains an open problem. Existing works that leverage VLM for 3D understanding generally resort to constructing intermediate 2D representations for the 3D data, but at the cost of losing 3D geometry information. To take a step toward open-world 3D vision understanding, we propose Contrastive Language-Image-Point Cloud Pretraining (CLIP$^2$) to directly learn the transferable 3D point cloud representation in realistic scenarios with a novel proxy alignment mechanism. Specifically, we exploit naturally-existed correspondences in 2D and 3D scenarios, and build well-aligned and instance-based text-image-point proxies from those complex scenarios. On top of that, we propose a cross-modal contrastive objective to learn semantic and instance-level aligned point cloud representation. Experimental results on both indoor and outdoor scenarios show that our learned 3D representation has great transfer ability in downstream tasks, including zero-shot and few-shot 3D recognition, which boosts the state-of-the-art methods by large margins. Furthermore, we provide analyses of the capability of different representations in real scenarios and present the optional ensemble scheme.

</details>

### Joint Visual Grounding and Tracking with Natural Language Specification.
- **链接**: [arXiv:2303.12027](https://arxiv.org/abs/2303.12027) · [代码](https://github.com/lizhou-cs/JointNLT) · 📚 被引 139
- **作者**: Li Zhou, Zikun Zhou, Kaige Mao, Zhenyu He
- **🏷️ 机构**: Harbin Institute of Technology,Shenzhen, Peng Cheng Laboratory
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-training across 3D vision and language remains under development because of limited training data. Recent works attempt to transfer vision-language pre-training models to 3D vision. PointCLIP converts point cloud data to multi-view depth maps, adopting CLIP for shape classification. However, its performance is restricted by the domain gap between rendered depth maps and images, as well as the diversity of depth distributions. To address this issue, we propose CLIP2Point, an image-depth pre-training method by contrastive learning to transfer CLIP to the 3D domain, and adapt it to point cloud classification. We introduce a new depth rendering setting that forms a better visual effect, and then render 52,460 pairs of images and depth maps from ShapeNet for pre-training. The pre-training scheme of CLIP2Point combines cross-modality learning to enforce the depth features for capturing expressive visual and textual features and intra-modality learning to enhance the invariance of depth aggregation. Additionally, we propose a novel Dual-Path Adapter (DPA) module, i.e., a dual-path structure with simplified adapters for few-shot learning. The dual-path structure allows the joint use of CLIP and CLIP2Point, and the simplified adapter can well fit few-shot tasks without post-search. Experimental results show that CLIP2Point is effective in transferring CLIP knowledge to 3D vision. Our CLIP2Point outperforms PointCLIP and other self-supervised 3D networks, achieving state-of-the-art results on zero-shot and few-shot classification.

</details>

### Bird's-Eye-View Scene Graph for Vision-Language Navigation.
- **链接**: [arXiv:2308.04758](https://arxiv.org/abs/2308.04758)
- **作者**: Rui Liu, Xiaohan Wang, Wenguan Wang, Yi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language navigation (VLN), which entails an agent to navigate 3D environments following human instructions, has shown great advances. However, current agents are built upon panoramic observations, which hinders their ability to perceive 3D scene geometry and easily leads to ambiguous selection of panoramic view. To address these limitations, we present a BEV Scene Graph (BSG), which leverages multi-step BEV representations to encode scene layouts and geometric cues of indoor environment under the supervision of 3D detection. During navigation, BSG builds a local BEV representation at each step and maintains a BEV-based global scene map, which stores and organizes all the online collected local BEV representations according to their topological relations. Based on BSG, the agent predicts a local BEV grid-level decision score and a global graph-level decision score, combined with a sub-view selection score on panoramic views, for more accurate action prediction. Our approach significantly outperforms state-of-the-art methods on REVERIE, R2R, and R4R, showing the potential of BEV perception in VLN.

</details>

### PointCLIP V2: Prompting CLIP and GPT for Powerful 3D Open-world Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00249) · 📚 被引 181
- **作者**: Xiangyang Zhu, Renrui Zhang, Bowei He, Ziyu Guo, Ziyao Zeng, Zipeng Qin et al.
- **🏷️ 机构**: City University of Hong Kong, The Chinese University of Hong Kong, Yale University
- **会议**: ICCV 2023

### CLIP-FO3D: Learning Free Open-world 3D Scene Representations from 2D Dense CLIP.
- **链接**: [arXiv:2303.04748](https://arxiv.org/abs/2303.04748) · 📚 被引 66
- **作者**: Junbo Zhang, Runpei Dong, Kaisheng Ma
- **🏷️ 机构**: Tsinghua University, Xi&#x2019;an Jiaotong University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training a 3D scene understanding model requires complicated human annotations, which are laborious to collect and result in a model only encoding close-set object semantics. In contrast, vision-language pre-training models (e.g., CLIP) have shown remarkable open-world reasoning properties. To this end, we propose directly transferring CLIP's feature space to 3D scene understanding model without any form of supervision. We first modify CLIP's input and forwarding process so that it can be adapted to extract dense pixel features for 3D scene contents. We then project multi-view image features to the point cloud and train a 3D scene understanding model with feature distillation. Without any annotations or additional training, our model achieves promising annotation-free semantic segmentation results on open-vocabulary semantics and long-tailed concepts. Besides, serving as a cross-modal pre-training framework, our method can be used to improve data efficiency during fine-tuning. Our model outperforms previous SOTA methods in various zero-shot and data-efficient learning benchmarks. Most importantly, our model successfully inherits CLIP's rich-structured knowledge, allowing 3D scene understanding models to recognize not only object concepts but also open-world semantics.

</details>

### CLIPN for Zero-Shot OOD Detection: Teaching CLIP to Say No.
- **链接**: [arXiv:2308.12213](https://arxiv.org/abs/2308.12213) · [代码](https://github.com/xmed-lab/CLIPN) · 📚 被引 105
- **作者**: Hualiang Wang, Yi Li, Huifeng Yao, Xiaomeng Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology,Department of Electronic and Computer Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection refers to training the model on an in-distribution (ID) dataset to classify whether the input images come from unknown classes. Considerable effort has been invested in designing various OOD detection methods based on either convolutional neural networks or transformers. However, zero-shot OOD detection methods driven by CLIP, which only require class names for ID, have received less attention. This paper presents a novel method, namely CLIP saying no (CLIPN), which empowers the logic of saying no within CLIP. Our key motivation is to equip CLIP with the capability of distinguishing OOD and ID samples using positive-semantic prompts and negation-semantic prompts. Specifically, we design a novel learnable no prompt and a no text encoder to capture negation semantics within images. Subsequently, we introduce two loss functions: the image-text binary-opposite loss and the text semantic-opposite loss, which we use to teach CLIPN to associate images with no prompts, thereby enabling it to identify unknown samples. Furthermore, we propose two threshold-free inference algorithms to perform OOD detection by utilizing negation semantics from no prompts and the text encoder. Experimental results on 9 benchmark datasets (3 ID datasets and 6 OOD datasets) for the OOD detection task demonstrate that CLIPN, based on ViT-B-16, outperforms 7 well-used algorithms by at least 2.34% and 11.64% in terms of AUROC and FPR95 for zero-shot OOD detection on ImageNet-1K. Our CLIPN can serve as a solid foundation for effectively leveraging CLIP in downstream OOD tasks. The code is available on https://github.com/xmed-lab/CLIPN.

</details>

### TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance.
- **链接**: [arXiv:2309.12314](https://arxiv.org/abs/2309.12314) · 📚 被引 73
- **作者**: Kan Wu, Houwen Peng, Zhenghong Zhou, Bin Xiao, Mengchen Liu, Lu Yuan et al.
- **🏷️ 机构**: Sun Yat-sen University, Microsoft, Huazhong University of Science &amp; Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adapter-style efficient transfer learning (ETL) has shown excellent performance in the tuning of vision-language models (VLMs) under the low-data regime, where only a few additional parameters are introduced to excavate the task-specific knowledge based on the general and powerful representation of VLMs. However, most adapter-style works face two limitations: (i) modeling task-specific knowledge with a single modality only; and (ii) overlooking the exploitation of the inter-class relationships in downstream tasks, thereby leading to sub-optimal solutions. To mitigate that, we propose an effective adapter-style tuning strategy, dubbed GraphAdapter, which performs the textual adapter by explicitly modeling the dual-modality structure knowledge (i.e., the correlation of different semantics/classes in textual and visual modalities) with a dual knowledge graph. In particular, the dual knowledge graph is established with two sub-graphs, i.e., a textual knowledge sub-graph, and a visual knowledge sub-graph, where the nodes and edges represent the semantics/classes and their correlations in two modalities, respectively. This enables the textual feature of each prompt to leverage the task-specific structure knowledge from both textual and visual modalities, yielding a more effective classifier for downstream tasks. Extensive experimental results on 11 benchmark datasets reveal that our GraphAdapter significantly outperforms previous adapter-based methods. The code will be released at https://github.com/lixinustc/GraphAdapter

</details>

### Meta-Adapter: An Online Few-shot Learner for Vision-Language Model.
- **链接**: [arXiv:2311.03774](https://arxiv.org/abs/2311.03774) · 📚 被引 8
- **作者**: Cheng Cheng, Lin Song, Ruoyi Xue, Hang Wang, Hongbin Sun, Yixiao Ge et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The contrastive vision-language pre-training, known as CLIP, demonstrates remarkable potential in perceiving open-world visual concepts, enabling effective zero-shot image recognition. Nevertheless, few-shot learning methods based on CLIP typically require offline fine-tuning of the parameters on few-shot samples, resulting in longer inference time and the risk of over-fitting in certain domains. To tackle these challenges, we propose the Meta-Adapter, a lightweight residual-style adapter, to refine the CLIP features guided by the few-shot samples in an online manner. With a few training samples, our method can enable effective few-shot learning capabilities and generalize to unseen data or tasks without additional fine-tuning, achieving competitive performance and high efficiency. Without bells and whistles, our approach outperforms the state-of-the-art online few-shot learning method by an average of 3.6\% on eight image classification datasets with higher inference speed. Furthermore, our model is simple and flexible, serving as a plug-and-play module directly applicable to downstream tasks. Without further fine-tuning, Meta-Adapter obtains notable performance improvements in open-vocabulary object detection and segmentation tasks.

</details>

### InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning.
- **链接**: [arXiv:2305.06500](https://arxiv.org/abs/2305.06500) · [代码](https://github.com/salesforce/LAVIS) · 📚 被引 438
- **作者**: Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale pre-training and instruction tuning have been successful at creating general-purpose language models with broad competence. However, building general-purpose vision-language models is challenging due to the rich input distributions and task diversity resulting from the additional visual input. Although vision-language pretraining has been widely studied, vision-language instruction tuning remains under-explored. In this paper, we conduct a systematic and comprehensive study on vision-language instruction tuning based on the pretrained BLIP-2 models. We gather 26 publicly available datasets, covering a wide variety of tasks and capabilities, and transform them into instruction tuning format. Additionally, we introduce an instruction-aware Query Transformer, which extracts informative features tailored to the given instruction. Trained on 13 held-in datasets, InstructBLIP attains state-of-the-art zero-shot performance across all 13 held-out datasets, substantially outperforming BLIP-2 and larger Flamingo models. Our models also lead to state-of-the-art performance when finetuned on individual downstream tasks (e.g., 90.7% accuracy on ScienceQA questions with image contexts). Furthermore, we qualitatively demonstrate the advantages of InstructBLIP over concurrent multimodal models. All InstructBLIP models are open-sourced at https://github.com/salesforce/LAVIS/tree/main/projects/instructblip.

</details>

### UP-DP: Unsupervised Prompt Learning for Data Pre-Selection with Vision-Language Models.
- **链接**: [arXiv:2307.11227](https://arxiv.org/abs/2307.11227) · 📚 被引 0
- **作者**: Xin Li, Sima Behpour, Thang Long Doan, Wenbin He, Liang Gou, Liu Ren
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we investigate the task of data pre-selection, which aims to select instances for labeling from an unlabeled dataset through a single pass, thereby optimizing performance for undefined downstream tasks with a limited annotation budget. Previous approaches to data pre-selection relied solely on visual features extracted from foundation models, such as CLIP and BLIP-2, but largely ignored the powerfulness of text features. In this work, we argue that, with proper design, the joint feature space of both vision and text can yield a better representation for data pre-selection. To this end, we introduce UP-DP, a simple yet effective unsupervised prompt learning approach that adapts vision-language models, like BLIP-2, for data pre-selection. Specifically, with the BLIP-2 parameters frozen, we train text prompts to extract the joint features with improved representation, ensuring a diverse cluster structure that covers the entire dataset. We extensively compare our method with the state-of-the-art using seven benchmark datasets in different settings, achieving up to a performance gain of 20%. Interestingly, the prompts learned from one dataset demonstrate significant generalizability and can be applied directly to enhance the feature extraction of BLIP-2 from other datasets. To the best of our knowledge, UP-DP is the first work to incorporate unsupervised prompt learning in a vision-language model for data pre-selection.

</details>

### SwapPrompt: Test-Time Prompt Adaptation for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/cdd0640218a27e9e2c0e52e324e25db0-Abstract-Conference.html) · 📚 被引 5
- **作者**: Xiaosong Ma, Jie Zhang, Song Guo, Wenchao Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### S-CLIP: Semi-supervised Vision-Language Learning using Few Specialist Captions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/c06f788963f0ce069f5b2dbf83fe7822-Abstract-Conference.html) · 📚 被引 3
- **作者**: Sangwoo Mo, Minkyu Kim, Kyungmin Lee, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Stable and low-precision training for large-scale vision-language models.
- **链接**: [arXiv:2304.13013](https://arxiv.org/abs/2304.13013) · 📚 被引 16
- **作者**: Mitchell Wortsman, Tim Dettmers, Luke Zettlemoyer, Ari Morcos, Ali Farhadi, Ludwig Schmidt
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce new methods for 1) accelerating and 2) stabilizing training for large language-vision models. 1) For acceleration, we introduce SwitchBack, a linear layer for int8 quantized training which provides a speed-up of 13-25% while matching the performance of bfloat16 training within 0.1 percentage points for the 1B parameter CLIP ViT-Huge -- the largest int8 training to date. Our main focus is int8 as GPU support for float8 is rare, though we also analyze float8 training through simulation. While SwitchBack proves effective for float8, we show that standard techniques are also successful if the network is trained and initialized so that large feature magnitudes are discouraged, which we accomplish via layer-scale initialized with zeros. 2) For stability, we analyze loss spikes and find they consistently occur 1-8 iterations after the squared gradients become under-estimated by their AdamW second moment estimator. As a result, we recommend an AdamW-Adafactor hybrid which avoids loss spikes when training a CLIP ViT-Huge model and outperforms gradient clipping at the scales we test.

</details>

### On Evaluating Adversarial Robustness of Large Vision-Language Models.
- **链接**: [arXiv:2305.16934](https://arxiv.org/abs/2305.16934) · [代码](https://github.com/yunqing-me/AttackVLM)
- **作者**: Yunqing Zhao, Tianyu Pang, Chao Du, Xiao Yang, Chongxuan Li, Ngai-Man Cheung et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (VLMs) such as GPT-4 have achieved unprecedented performance in response generation, especially with visual inputs, enabling more creative and adaptable interaction than large language models such as ChatGPT. Nonetheless, multimodal generation exacerbates safety concerns, since adversaries may successfully evade the entire system by subtly manipulating the most vulnerable modality (e.g., vision). To this end, we propose evaluating the robustness of open-source large VLMs in the most realistic and high-risk setting, where adversaries have only black-box system access and seek to deceive the model into returning the targeted responses. In particular, we first craft targeted adversarial examples against pretrained models such as CLIP and BLIP, and then transfer these adversarial examples to other VLMs such as MiniGPT-4, LLaVA, UniDiffuser, BLIP-2, and Img2Prompt. In addition, we observe that black-box queries on these VLMs can further improve the effectiveness of targeted evasion, resulting in a surprisingly high success rate for generating targeted responses. Our findings provide a quantitative understanding regarding the adversarial vulnerability of large VLMs and call for a more thorough examination of their potential security flaws before deployment in practice. Code is at https://github.com/yunqing-me/AttackVLM.

</details>

### Distilling Out-of-Distribution Robustness from Vision-Language Foundation Models.
- **链接**: [arXiv:2311.01441](https://arxiv.org/abs/2311.01441) · 📚 被引 2
- **作者**: Andy Zhou, Jindong Wang, Yu-Xiong Wang, Haohan Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale Transformer models bring significant improvements for various downstream vision language tasks with a unified architecture. The performance improvements come with increasing model size, resulting in slow inference speed and increased cost for severing. While some certain predictions benefit from the full complexity of the large-scale model, not all of inputs need the same amount of computation to conduct, potentially leading to computation resource waste. To handle this challenge, early exiting is proposed to adaptively allocate computational power in term of input complexity to improve inference efficiency. The existing early exiting strategies usually adopt output confidence based on intermediate layers as a proxy of input complexity to incur the decision of skipping following layers. However, such strategies cannot apply to encoder in the widely-used unified architecture with both encoder and decoder due to difficulty of output confidence estimation in the encoder. It is suboptimal in term of saving computation power to ignore the early exiting in encoder component. To handle this challenge, we propose a novel early exiting strategy for unified visual language models, which allows dynamically skip the layers in encoder and decoder simultaneously in term of input layer-wise similarities with multiple times of early exiting, namely \textbf{MuE}. By decomposing the image and text modalities in the encoder, MuE is flexible and can skip different layers in term of modalities, advancing the inference efficiency while minimizing performance drop. Experiments on the SNLI-VE and MS COCO datasets show that the proposed approach MuE can reduce expected inference time by up to 50\% and 40\% while maintaining 99\% and 96\% performance respectively.

</details>

### Improving Commonsense in Vision-Language Models via Knowledge Graph Riddles.
- **链接**: [arXiv:2211.16504](https://arxiv.org/abs/2211.16504) · [代码](https://github.com/pleaseconnectwifi/DANCE) · 📚 被引 7
- **作者**: Shuquan Ye, Yujia Xie, Dongdong Chen, Yichong Xu, Lu Yuan, Chenguang Zhu et al.
- **🏷️ 机构**: City University of Hong Kong, Microsoft
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focuses on analyzing and improving the commonsense ability of recent popular vision-language (VL) models. Despite the great success, we observe that existing VL-models still lack commonsense knowledge/reasoning ability (e.g., "Lemons are sour"), which is a vital component towards artificial general intelligence. Through our analysis, we find one important reason is that existing large-scale VL datasets do not contain much commonsense knowledge, which motivates us to improve the commonsense of VL-models from the data perspective. Rather than collecting a new VL training dataset, we propose a more scalable strategy, i.e., "Data Augmentation with kNowledge graph linearization for CommonsensE capability" (DANCE). It can be viewed as one type of data augmentation technique, which can inject commonsense knowledge into existing VL datasets on the fly during training. More specifically, we leverage the commonsense knowledge graph (e.g., ConceptNet) and create variants of text description in VL datasets via bidirectional sub-graph sequentialization. For better commonsense evaluation, we further propose the first retrieval-based commonsense diagnostic benchmark. By conducting extensive experiments on some representative VL-models, we demonstrate that our DANCE technique is able to significantly improve the commonsense ability while maintaining the performance on vanilla retrieval tasks. The code and data are available at https://github.com/pleaseconnectwifi/DANCE

</details>

### Meta-Personalizing Vision-Language Models to Find Named Instances in Video.
- **链接**: [arXiv:2306.10169](https://arxiv.org/abs/2306.10169) · 📚 被引 13
- **作者**: Chun-Hsiao Yeh, Bryan C. Russell, Josef Sivic, Fabian Caba Heilbron, Simon Jenni
- **🏷️ 机构**: University of California,Berkeley, Adobe Research, Czech Institute of Informatics, Robotics and Cybernetics at the Czech Technical University in Prague (CIIRC CTU)
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale vision-language models (VLM) have shown impressive results for language-guided search applications. While these models allow category-level queries, they currently struggle with personalized searches for moments in a video where a specific object instance such as ``My dog Biscuit'' appears. We present the following three contributions to address this problem. First, we describe a method to meta-personalize a pre-trained VLM, i.e., learning how to learn to personalize a VLM at test time to search in video. Our method extends the VLM's token vocabulary by learning novel word embeddings specific to each instance. To capture only instance-specific features, we represent each instance embedding as a combination of shared and learned global category features. Second, we propose to learn such personalization without explicit human supervision. Our approach automatically identifies moments of named visual instances in video using transcripts and vision-language similarity in the VLM's embedding space. Finally, we introduce This-Is-My, a personal video instance retrieval benchmark. We evaluate our approach on This-Is-My and DeepFashion2 and show that we obtain a 15% relative improvement over the state of the art on the latter dataset.

</details>

### GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods.
- **链接**: [arXiv:2301.01893](https://arxiv.org/abs/2301.01893) · 📚 被引 13
- **作者**: Da Yin, Feng Gao, Govind Thattai, Michael Johnston, Kai-Wei Chang
- **🏷️ 机构**: University of California,Los Angeles, Amazon Alexa AI
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A key goal for the advancement of AI is to develop technologies that serve the needs not just of one group but of all communities regardless of their geographical region. In fact, a significant proportion of knowledge is locally shared by people from certain regions but may not apply equally in other regions because of cultural differences. If a model is unaware of regional characteristics, it may lead to performance disparity across regions and result in bias against underrepresented groups. We propose GIVL, a Geographically Inclusive Vision-and-Language Pre-trained model. There are two attributes of geo-diverse visual concepts which can help to learn geo-diverse knowledge: 1) concepts under similar categories have unique knowledge and visual characteristics, 2) concepts with similar visual features may fall in completely different categories. Motivated by the attributes, we design new pre-training objectives Image Knowledge Matching (IKM) and Image Edit Checking (IEC) to pre-train GIVL. Compared with similar-size models pre-trained with similar scale of data, GIVL achieves state-of-the-art (SOTA) and more balanced performance on geo-diverse V&L tasks.

</details>

### IFSeg: Image-free Semantic Segmentation via Vision-Language Model.
- **链接**: [arXiv:2303.14396](https://arxiv.org/abs/2303.14396) · [代码](https://github.com/alinlab/ifseg) · 📚 被引 17
- **作者**: Sukmin Yun, Seong Hyeon Park, Paul Hongsuck Seo, Jinwoo Shin
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST), Google Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language (VL) pre-training has recently gained much attention for its transferability and flexibility in novel concepts (e.g., cross-modality transfer) across various visual tasks. However, VL-driven segmentation has been under-explored, and the existing approaches still have the burden of acquiring additional training images or even segmentation annotations to adapt a VL model to downstream segmentation tasks. In this paper, we introduce a novel image-free segmentation task where the goal is to perform semantic segmentation given only a set of the target semantic categories, but without any task-specific images and annotations. To tackle this challenging task, our proposed method, coined IFSeg, generates VL-driven artificial image-segmentation pairs and updates a pre-trained VL model to a segmentation task. We construct this artificial training data by creating a 2D map of random semantic categories and another map of their corresponding word tokens. Given that a pre-trained VL model projects visual and text tokens into a common space where tokens that share the semantics are located closely, this artificially generated word map can replace the real image inputs for such a VL model. Through an extensive set of experiments, our model not only establishes an effective baseline for this novel task but also demonstrates strong performances compared to existing methods that rely on stronger supervision, such as task-specific images and segmentation masks. Code is available at https://github.com/alinlab/ifseg.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language (VL) pre-training has recently gained much attention for its transferability and flexibility in novel concepts (e.g., cross-modality transfer) across various visual tasks. However, VL-driven segmentation has been under-explored, and the existing approaches still have the burden of acquiring additional training images or even segmentation annotations to adapt a VL model to downstream segmentation tasks. In this paper, we introduce a novel image-free segmentation task where the goal is to perform semantic segmentation given only a set of the target semantic categories, but without any task-specific images and annotations. To tackle this challenging task, our proposed method, coined IFSeg, generates VL-driven artificial image-segmentation pairs and updates a pre-trained VL model to a segmentation task. We construct this artificial training data by creating a 2D map of random semantic categories and another map of their corresponding word tokens. Given that a pre-trained VL model projects visual and text tokens into a common space where tokens that share the semantics are located closely, this artificially generated word map can replace the real image inputs for such a VL model. Through an extensive set of experiments, our model not only establishes an effective baseline for this novel task but also demonstrates strong performances compared to existing methods that rely on stronger supervision, such as task-specific images and segmentation masks. Code is available at https://github.com/alinlab/ifseg.

</details>

### Distribution-Aware Prompt Tuning for Vision-Language Models.
- **链接**: [arXiv:2309.03406](https://arxiv.org/abs/2309.03406) · [代码](https://github.com/mlvlab/DAPT) · 📚 被引 50
- **作者**: Eulrang Cho, Jooyeon Kim, Hyunwoo J. Kim
- **🏷️ 机构**: Korea University,Department of Computer Science and Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models (VLMs) have shown impressive performance on various downstream tasks by utilizing knowledge learned from large data. In general, the performance of VLMs on target tasks can be further improved by prompt tuning, which adds context to the input image or text. By leveraging data from target tasks, various prompt-tuning methods have been studied in the literature. A key to prompt tuning is the feature space alignment between two modalities via learnable vectors with model parameters fixed. We observed that the alignment becomes more effective when embeddings of each modality are `well-arranged' in the latent space. Inspired by this observation, we proposed distribution-aware prompt tuning (DAPT) for vision-language models, which is simple yet effective. Specifically, the prompts are learned by maximizing inter-dispersion, the distance between classes, as well as minimizing the intra-dispersion measured by the distance between embeddings from the same class. Our extensive experiments on 11 benchmark datasets demonstrate that our method significantly improves generalizability. The code is available at https://github.com/mlvlab/DAPT.

</details>

### Knowledge-Aware Prompt Tuning for Generalizable Vision-Language Models.
- **链接**: [arXiv:2308.11186](https://arxiv.org/abs/2308.11186) · 📚 被引 44
- **作者**: Baoshuo Kan, Teng Wang, Wenpeng Lu, Xiantong Zhen, Weili Guan, Feng Zheng
- **🏷️ 机构**: Qilu University of Technology (Shandong Academy of Sciences), Southern University of Science and Technology, United Imaging Healthcare
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models, e.g., CLIP, working with manually designed prompts have demonstrated great capacity of transfer learning. Recently, learnable prompts achieve state-of-the-art performance, which however are prone to overfit to seen classes, failing to generalize to unseen classes. In this paper, we propose a Knowledge-Aware Prompt Tuning (KAPT) framework for vision-language models. Our approach takes inspiration from human intelligence in which external knowledge is usually incorporated into recognizing novel categories of objects. Specifically, we design two complementary types of knowledge-aware prompts for the text encoder to leverage the distinctive characteristics of category-related external knowledge. The discrete prompt extracts the key information from descriptions of an object category, and the learned continuous prompt captures overall contexts. We further design an adaptation head for the visual encoder to aggregate salient attentive visual cues, which establishes discriminative and task-aware visual representations. We conduct extensive experiments on 11 widely-used benchmark datasets and the results verify the effectiveness in few-shot image classification, especially in generalizing to unseen categories. Compared with the state-of-the-art CoCoOp method, KAPT exhibits favorable performance and achieves an absolute gain of 3.22% on new classes and 2.57% in terms of harmonic mean.

</details>

### Distilling Large Vision-Language Model with Out-of-Distribution Generalizability.
- **链接**: [arXiv:2307.03135](https://arxiv.org/abs/2307.03135) · [代码](https://github.com/xuanlinli17/large_vlm_distillation_ood) · 📚 被引 28
- **作者**: Xuanlin Li, Yunhao Fang, Minghua Liu, Zhan Ling, Zhuowen Tu, Hao Su
- **🏷️ 机构**: UC San Diego
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models have achieved outstanding performance, but their size and computational requirements make their deployment on resource-constrained devices and time-sensitive tasks impractical. Model distillation, the process of creating smaller, faster models that maintain the performance of larger models, is a promising direction towards the solution. This paper investigates the distillation of visual representations in large teacher vision-language models into lightweight student models using a small- or mid-scale dataset. Notably, this study focuses on open-vocabulary out-of-distribution (OOD) generalization, a challenging problem that has been overlooked in previous model distillation literature. We propose two principles from vision and language modality perspectives to enhance student's OOD generalization: (1) by better imitating teacher's visual representation space, and carefully promoting better coherence in vision-language alignment with the teacher; (2) by enriching the teacher's language representations with informative and finegrained semantic attributes to effectively distinguish between different labels. We propose several metrics and conduct extensive experiments to investigate their techniques. The results demonstrate significant improvements in zero-shot and few-shot student performance on open-vocabulary out-of-distribution classification, highlighting the effectiveness of our proposed approaches. Poster: https://xuanlinli17.github.io/pdfs/iccv23_large_vlm_distillation_poster.pdf Code: https://github.com/xuanlinli17/large_vlm_distillation_ood

</details>

### Gradient-Regulated Meta-Prompt Learning for Generalizable Vision-Language Models.
- **链接**: [arXiv:2303.06571](https://arxiv.org/abs/2303.06571) · 📚 被引 24
- **作者**: Juncheng Li, Minghe Gao, Longhui Wei, Siliang Tang, Wenqiao Zhang, Mengze Li et al.
- **🏷️ 机构**: Zhejiang University, Huawei Cloud, National University of Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt tuning, a recently emerging paradigm, enables the powerful vision-language pre-training models to adapt to downstream tasks in a parameter -- and data -- efficient way, by learning the ``soft prompts'' to condition frozen pre-training models. Though effective, it is particularly problematic in the few-shot scenario, where prompt tuning performance is sensitive to the initialization and requires a time-consuming process to find a good initialization, thus restricting the fast adaptation ability of the pre-training models. In addition, prompt tuning could undermine the generalizability of the pre-training models, because the learnable prompt tokens are easy to overfit to the limited training samples. To address these issues, we introduce a novel Gradient-RegulAted Meta-prompt learning (GRAM) framework that jointly meta-learns an efficient soft prompt initialization for better adaptation and a lightweight gradient regulating function for strong cross-domain generalizability in a meta-learning paradigm using only the unlabeled image-text pre-training data. Rather than designing a specific prompt tuning method, our GRAM can be easily incorporated into various prompt tuning methods in a model-agnostic way, and comprehensive experiments show that GRAM brings about consistent improvement for them in several settings (i.e., few-shot learning, cross-domain generalization, cross-dataset generalization, etc.) over 11 datasets. Further, experiments show that GRAM enables the orthogonal methods of textual and visual prompt tuning to work in a mutually-enhanced way, offering better generalizability beyond the uni-modal prompt tuning methods.

</details>

### Black Box Few-Shot Adaptation for Vision-Language models.
- **链接**: [arXiv:2304.01752](https://arxiv.org/abs/2304.01752) · 📚 被引 35
- **作者**: Yassine Ouali, Adrian Bulat, Brais Martínez, Georgios Tzimiropoulos
- **🏷️ 机构**: Samsung AI Cambridge
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language (V-L) models trained with contrastive learning to align the visual and language modalities have been shown to be strong few-shot learners. Soft prompt learning is the method of choice for few-shot downstream adaptation aiming to bridge the modality gap caused by the distribution shift induced by the new domain. While parameter-efficient, prompt learning still requires access to the model weights and can be computationally infeasible for large models with billions of parameters. To address these shortcomings, in this work, we describe a black-box method for V-L few-shot adaptation that (a) operates on pre-computed image and text features and hence works without access to the model's weights, (b) it is orders of magnitude faster at training time, (c) it is amenable to both supervised and unsupervised training, and (d) it can be even used to align image and text features computed from uni-modal models. To achieve this, we propose Linear Feature Alignment (LFA), a simple linear approach for V-L re-alignment in the target domain. LFA is initialized from a closed-form solution to a least-squares problem and then it is iteratively updated by minimizing a re-ranking loss. Despite its simplicity, our approach can even surpass soft-prompt learning methods as shown by extensive experiments on 11 image and 2 video datasets.

</details>

### Perceptual Grouping in Contrastive Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00513) · 📚 被引 49
- **作者**: Kanchana Ranasinghe, Brandon McKinzie, Sachin Ravi, Yinfei Yang, Alexander Toshev, Jonathon Shlens
- **🏷️ 机构**: Apple
- **会议**: ICCV 2023

### LoGoPrompt: Synthetic Text Images Can Be Good Visual Prompts for Vision-Language Models.
- **链接**: [arXiv:2309.01155](https://arxiv.org/abs/2309.01155) · 📚 被引 22
- **作者**: Cheng Shi, Sibei Yang
- **🏷️ 机构**: ShanghaiTech University,School of Information Science and Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt engineering is a powerful tool used to enhance the performance of pre-trained models on downstream tasks. For example, providing the prompt "Let's think step by step" improved GPT-3's reasoning accuracy to 63% on MutiArith while prompting "a photo of" filled with a class name enables CLIP to achieve $80$\% zero-shot accuracy on ImageNet. While previous research has explored prompt learning for the visual modality, analyzing what constitutes a good visual prompt specifically for image recognition is limited. In addition, existing visual prompt tuning methods' generalization ability is worse than text-only prompting tuning. This paper explores our key insight: synthetic text images are good visual prompts for vision-language models! To achieve that, we propose our LoGoPrompt, which reformulates the classification objective to the visual prompt selection and addresses the chicken-and-egg challenge of first adding synthetic text images as class-wise visual prompts or predicting the class first. Without any trainable visual prompt parameters, experimental results on 16 datasets demonstrate that our method consistently outperforms state-of-the-art methods in few-shot learning, base-to-new generalization, and domain generalization.

</details>

### Linear Spaces of Meanings: Compositional Structures in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01412) · 📚 被引 17
- **作者**: Matthew Trager, Pramuditha Perera, Luca Zancato, Alessandro Achille, Parminder Bhatia, Stefano Soatto
- **🏷️ 机构**: AWS AI Labs
- **会议**: ICCV 2023

### SuS-X: Training-Free Name-Only Transfer of Vision-Language Models.
- **链接**: [arXiv:2211.16198](https://arxiv.org/abs/2211.16198) · [代码](https://github.com/vishaal27/SuS-X) · 📚 被引 80
- **作者**: Vishaal Udandarao, Ankush Gupta, Samuel Albanie
- **🏷️ 机构**: University of Cambridge, DeepMind,London
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Language-Image Pre-training (CLIP) has emerged as a simple yet effective way to train large-scale vision-language models. CLIP demonstrates impressive zero-shot classification and retrieval on diverse downstream tasks. However, to leverage its full potential, fine-tuning still appears to be necessary. Fine-tuning the entire CLIP model can be resource-intensive and unstable. Moreover, recent methods that aim to circumvent this need for fine-tuning still require access to images from the target distribution. In this paper, we pursue a different approach and explore the regime of training-free "name-only transfer" in which the only knowledge we possess about the downstream task comprises the names of downstream target categories. We propose a novel method, SuS-X, consisting of two key building blocks -- SuS and TIP-X, that requires neither intensive fine-tuning nor costly labelled data. SuS-X achieves state-of-the-art zero-shot classification results on 19 benchmark datasets. We further show the utility of TIP-X in the training-free few-shot setting, where we again achieve state-of-the-art results over strong training-free baselines. Code is available at https://github.com/vishaal27/SuS-X.

</details>

### Dreamwalker: Mental Planning for Continuous Vision-Language Navigation.
- **链接**: [arXiv:2308.07498](https://arxiv.org/abs/2308.07498) · 📚 被引 43
- **作者**: Hanqing Wang, Wei Liang, Luc Van Gool, Wenguan Wang
- **🏷️ 机构**: Beijing Institute of Technology, ETH Zurich,Computer Vision Lab, Zhejiang University,ReLER, CCAI
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> VLN-CE is a recently released embodied task, where AI agents need to navigate a freely traversable environment to reach a distant target location, given language instructions. It poses great challenges due to the huge space of possible strategies. Driven by the belief that the ability to anticipate the consequences of future actions is crucial for the emergence of intelligent and interpretable planning behavior, we propose DREAMWALKER -- a world model based VLN-CE agent. The world model is built to summarize the visual, topological, and dynamic properties of the complicated continuous environment into a discrete, structured, and compact representation. DREAMWALKER can simulate and evaluate possible plans entirely in such internal abstract world, before executing costly actions. As opposed to existing model-free VLN-CE agents simply making greedy decisions in the real world, which easily results in shortsighted behaviors, DREAMWALKER is able to make strategic planning through large amounts of ``mental experiments.'' Moreover, the imagined future scenarios reflect our agent's intention, making its decision-making process more transparent. Extensive experiments and ablation studies on VLN-CE dataset confirm the effectiveness of the proposed approach and outline fruitful directions for future work.

</details>

### Equivariant Similarity for Vision-Language Foundation Models.
- **链接**: [arXiv:2303.14465](https://arxiv.org/abs/2303.14465) · [代码](https://github.com/Wangt-CN/EqBen) · 📚 被引 20
- **作者**: Tan Wang, Kevin Lin, Linjie Li, Chung-Ching Lin, Zhengyuan Yang, Hanwang Zhang et al.
- **🏷️ 机构**: Nanyang Technological University, Microsoft
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This study explores the concept of equivariance in vision-language foundation models (VLMs), focusing specifically on the multimodal similarity function that is not only the major training objective but also the core delivery to support downstream tasks. Unlike the existing image-text similarity objective which only categorizes matched pairs as similar and unmatched pairs as dissimilar, equivariance also requires similarity to vary faithfully according to the semantic changes. This allows VLMs to generalize better to nuanced and unseen multimodal compositions. However, modeling equivariance is challenging as the ground truth of semantic change is difficult to collect. For example, given an image-text pair about a dog, it is unclear to what extent the similarity changes when the pixel is changed from dog to cat? To this end, we propose EqSim, a regularization loss that can be efficiently calculated from any two matched training pairs and easily pluggable into existing image-text retrieval fine-tuning. Meanwhile, to further diagnose the equivariance of VLMs, we present a new challenging benchmark EqBen. Compared to the existing evaluation sets, EqBen is the first to focus on "visual-minimal change". Extensive experiments show the lack of equivariance in current VLMs and validate the effectiveness of EqSim. Code is available at https://github.com/Wangt-CN/EqBen.

</details>

### Why Is Prompt Tuning for Vision-Language Models Robust to Noisy Labels?
- **链接**: [arXiv:2307.11978](https://arxiv.org/abs/2307.11978) · [代码](https://github.com/CEWu/PTNL) · 📚 被引 15
- **作者**: Cheng-En Wu, Yu Tian, Haichao Yu, Heng Wang, Pedro Morgado, Yu Hen Hu et al.
- **🏷️ 机构**: University of Wisconsin-Madison, ByteDance Inc.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models such as CLIP learn a generic text-image embedding from large-scale training data. A vision-language model can be adapted to a new classification task through few-shot prompt tuning. We find that such a prompt tuning process is highly robust to label noises. This intrigues us to study the key reasons contributing to the robustness of the prompt tuning paradigm. We conducted extensive experiments to explore this property and find the key factors are: 1) the fixed classname tokens provide a strong regularization to the optimization of the model, reducing gradients induced by the noisy samples; 2) the powerful pre-trained image-text embedding that is learned from diverse and generic web data provides strong prior knowledge for image classification. Further, we demonstrate that noisy zero-shot predictions from CLIP can be used to tune its own prompt, significantly enhancing prediction accuracy in the unsupervised setting. The code is available at https://github.com/CEWu/PTNL.

</details>

### Regularized Mask Tuning: Uncovering Hidden Knowledge in Pre-trained Vision-Language Models.
- **链接**: [arXiv:2307.15049](https://arxiv.org/abs/2307.15049) · 📚 被引 7
- **作者**: Kecheng Zheng, Wei Wu, Ruili Feng, Kai Zhu, Jiawei Liu, Deli Zhao et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, USTC, Alibaba Group
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt tuning and adapter tuning have shown great potential in transferring pre-trained vision-language models (VLMs) to various downstream tasks. In this work, we design a new type of tuning method, termed as regularized mask tuning, which masks the network parameters through a learnable selection. Inspired by neural pathways, we argue that the knowledge required by a downstream task already exists in the pre-trained weights but just gets concealed in the upstream pre-training stage. To bring the useful knowledge back into light, we first identify a set of parameters that are important to a given downstream task, then attach a binary mask to each parameter, and finally optimize these masks on the downstream data with the parameters frozen. When updating the mask, we introduce a novel gradient dropout strategy to regularize the parameter selection, in order to prevent the model from forgetting old knowledge and overfitting the downstream data. Experimental results on 11 datasets demonstrate the consistent superiority of our method over previous alternatives. It is noteworthy that we manage to deliver 18.73% performance improvement compared to the zero-shot CLIP via masking an average of only 2.56% parameters. Furthermore, our method is synergistic with most existing parameter-efficient tuning methods and can boost the performance on top of them. Project page can be found here (https://wuw2019.github.io/R-AMT/).

</details>

### ECO: Ensembling Context Optimization for Vision-Language Models.
- **链接**: [arXiv:2307.14063](https://arxiv.org/abs/2307.14063) · 📚 被引 7
- **作者**: Lorenzo Agnolucci, Alberto Baldrati, Francesco Todino, Federico Becattini, Marco Bertini, Alberto Del Bimbo
- **🏷️ 机构**: University of Florence,Italy, University of Siena,Italy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image recognition has recently witnessed a paradigm shift, where vision-language models are now used to perform few-shot classification based on textual prompts. Among these, the CLIP model has shown remarkable capabilities for zero-shot transfer by matching an image and a custom textual prompt in its latent space. This has paved the way for several works that focus on engineering or learning textual contexts for maximizing CLIP's classification capabilities. In this paper, we follow this trend by learning an ensemble of prompts for image classification. We show that learning diverse and possibly shorter contexts improves considerably and consistently the results rather than relying on a single trainable prompt. In particular, we report better few-shot capabilities with no additional cost at inference time. We demonstrate the capabilities of our approach on 11 different benchmarks.

</details>

### Vision-Language Models Performing Zero-Shot Tasks Exhibit Disparities Between Gender Groups.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00294) · 📚 被引 3
- **作者**: Melissa Hall, Laura Gustafson, Aaron Adcock, Ishan Misra, Candace Ross
- **🏷️ 机构**: Meta AI
- **会议**: ICCV 2023

### Towards Vision-Language Mechanistic Interpretability: A Causal Tracing Tool for BLIP.
- **链接**: [arXiv:2308.14179](https://arxiv.org/abs/2308.14179) · [代码](https://github.com/vedantpalit/Towards-Vision-Language-Mechanistic-Interpretability) · 📚 被引 16
- **作者**: Vedant Palit, Rohan Pandey, Aryaman Arora, Paul Pu Liang
- **🏷️ 机构**: IIT Kharagpur, Reworkd.ai, Georgetown University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mechanistic interpretability seeks to understand the neural mechanisms that enable specific behaviors in Large Language Models (LLMs) by leveraging causality-based methods. While these approaches have identified neural circuits that copy spans of text, capture factual knowledge, and more, they remain unusable for multimodal models since adapting these tools to the vision-language domain requires considerable architectural changes. In this work, we adapt a unimodal causal tracing tool to BLIP to enable the study of the neural mechanisms underlying image-conditioned text generation. We demonstrate our approach on a visual question answering dataset, highlighting the causal relevance of later layer representations for all tokens. Furthermore, we release our BLIP causal tracing tool as open source to enable further experimentation in vision-language mechanistic interpretability by the community. Our code is available at https://github.com/vedantpalit/Towards-Vision-Language-Mechanistic-Interpretability.

</details>

### Towards an Exhaustive Evaluation of Vision-Language Foundation Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00041) · 📚 被引 3
- **作者**: Emmanuelle Salin, Stéphane Ayache, Benoît Favre
- **🏷️ 机构**: Aix Marseille Univ, Universit&#x00E9; de Toulon,CNRS, LIS,Marseille,France
- **会议**: ICCV 2023

### ClipCrop: Conditioned Cropping Driven by Vision-Language Model.
- **链接**: [arXiv:2211.11492](https://arxiv.org/abs/2211.11492) · 📚 被引 5
- **作者**: Zhihang Zhong, Mingxi Cheng, Zhirong Wu, Yuhui Yuan, Yinqiang Zheng, Ji Li et al.
- **🏷️ 机构**: The University of Tokyo,Japan, Microsoft Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image cropping has progressed tremendously under the data-driven paradigm. However, current approaches do not account for the intentions of the user, which is an issue especially when the composition of the input image is complex. Moreover, labeling of cropping data is costly and hence the amount of data is limited, leading to poor generalization performance of current algorithms in the wild. In this work, we take advantage of vision-language models as a foundation for creating robust and user-intentional cropping algorithms. By adapting a transformer decoder with a pre-trained CLIP-based detection model, OWL-ViT, we develop a method to perform cropping with a text or image query that reflects the user's intention as guidance. In addition, our pipeline design allows the model to learn text-conditioned aesthetic cropping with a small cropping dataset, while inheriting the open-vocabulary ability acquired from millions of text-image pairs. We validate our model through extensive experiments on existing datasets as well as a new cropping test set we compiled that is characterized by content ambiguity.

</details>

### TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance.
- **链接**: [arXiv:2309.12314](https://arxiv.org/abs/2309.12314) · 📚 被引 73
- **作者**: Kan Wu, Houwen Peng, Zhenghong Zhou, Bin Xiao, Mengchen Liu, Lu Yuan et al.
- **🏷️ 机构**: Sun Yat-sen University, Microsoft, Huazhong University of Science &amp; Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel cross-modal distillation method, called TinyCLIP, for large-scale language-image pre-trained models. The method introduces two core techniques: affinity mimicking and weight inheritance. Affinity mimicking explores the interaction between modalities during distillation, enabling student models to mimic teachers' behavior of learning cross-modal feature alignment in a visual-linguistic affinity space. Weight inheritance transmits the pre-trained weights from the teacher models to their student counterparts to improve distillation efficiency. Moreover, we extend the method into a multi-stage progressive distillation to mitigate the loss of informative weights during extreme compression. Comprehensive experiments demonstrate the efficacy of TinyCLIP, showing that it can reduce the size of the pre-trained CLIP ViT-B/32 by 50%, while maintaining comparable zero-shot performance. While aiming for comparable performance, distillation with weight inheritance can speed up the training by 1.4 - 7.8 $\times$ compared to training from scratch. Moreover, our TinyCLIP ViT-8M/16, trained on YFCC-15M, achieves an impressive zero-shot top-1 accuracy of 41.1% on ImageNet, surpassing the original CLIP ViT-B/16 by 3.5% while utilizing only 8.9% parameters. Finally, we demonstrate the good transferability of TinyCLIP in various downstream tasks. Code and models will be open-sourced at https://aka.ms/tinyclip.

</details>

### Local 3D Editing via 3D Distillation of CLIP Knowledge.
- **链接**: [arXiv:2306.12570](https://arxiv.org/abs/2306.12570) · 📚 被引 20
- **作者**: Junha Hyung, Sungwon Hwang, Daejin Kim, Hyunji Lee, Jaegul Choo
- **🏷️ 机构**: KAIST AI, Scatter Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D content manipulation is an important computer vision task with many real-world applications (e.g., product design, cartoon generation, and 3D Avatar editing). Recently proposed 3D GANs can generate diverse photorealistic 3D-aware contents using Neural Radiance fields (NeRF). However, manipulation of NeRF still remains a challenging problem since the visual quality tends to degrade after manipulation and suboptimal control handles such as 2D semantic maps are used for manipulations. While text-guided manipulations have shown potential in 3D editing, such approaches often lack locality. To overcome these problems, we propose Local Editing NeRF (LENeRF), which only requires text inputs for fine-grained and localized manipulation. Specifically, we present three add-on modules of LENeRF, the Latent Residual Mapper, the Attention Field Network, and the Deformation Network, which are jointly used for local manipulations of 3D features by estimating a 3D attention field. The 3D attention field is learned in an unsupervised way, by distilling the zero-shot mask generation capability of CLIP to the 3D space with multi-view guidance. We conduct diverse experiments and thorough evaluations both quantitatively and qualitatively.

</details>

## 跨领域论文（完整笔记在其他领域）

- CLIP the Gap: A Single Domain Generalization Approach for Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Open-Vocabulary Semantic Segmentation with Mask-adapted CLIP. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models. → [multimodal](../multimodal/Guideline%202023.md)
- Vita-CLIP: Video and text adaptive CLIP via Multimodal Prompting. → [multimodal](../multimodal/Guideline%202023.md)
- CLIP-S4: Language-Guided Self-Supervised Semantic Segmentation. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)

## 🆕 增量新增

### CLIP the Gap: A Single Domain Generalization Approach for Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2301.05499](https://arxiv.org/abs/2301.05499) · 📚 被引 131
- **作者**: Vidit Vidit, Martin Engilberge, Mathieu Salzmann
- **🏷️ 机构**: CVLab, EPFL
- **会议**: CVPR 2023
- **摘要（中）**: 针对单域泛化目标检测（SDG）中同时学习鲁棒定位和表示困难的问题，提出利用预训练视觉-语言模型（如CLIP）通过文本提示引入语义域概念。方法包括对检测器骨干特征进行语义增强，以及基于文本的分类损失。在天气驾驶基准上，该方法比现有唯一的SDG检测方法Single-DGOD提升10%，验证了其有效性。
- **摘要（英）**: Addressing the challenge of single domain generalization in object detection, this work leverages a pre-trained vision-language model to introduce semantic domain concepts via textual prompts, using semantic augmentation on backbone features and a text-based classification loss. It outperforms the existing SDG detection method Single-DGOD by 10% on a weather-driving benchmark.
- **核心贡献**: 提出首个利用视觉-语言模型进行单域泛化目标检测的方法。
- **创新点**: 通过文本提示和语义增强策略，将语义域知识注入检测器特征。
- **结果**: 在天气驾驶基准上比现有方法提升10%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Single Domain Generalization (SDG) tackles the problem of training a model on a single source domain so that it generalizes to any unseen target domain. While this has been well studied for image classification, the literature on SDG object detection remains almost non-existent. To address the challenges of simultaneously learning robust object localization and representation, we propose to leverage a pre-trained vision-language model to introduce semantic domain concepts via textual prompts. We achieve this via a semantic augmentation strategy acting on the features extracted by the detector backbone, as well as a text-based classification loss. Our experiments evidence the benefits of our approach, outperforming by 10% the only existing SDG object detection method, Single-DGOD [49], on their own diverse weather-driving benchmark.

</details>

### Aligning Bag of Regions for Open-Vocabulary Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2302.13996](https://arxiv.org/abs/2302.13996) · 📚 被引 128
- **作者**: Size Wu, Wenwei Zhang, Sheng Jin, Wentao Liu, Chen Change Loy
- **🏷️ 机构**: Nanyang Technological University,S-Lab, The University of Hong Kong, SenseTime Research and Tetras.AI
- **会议**: CVPR 2023
- **摘要（中）**: 针对开放词汇目标检测中仅对齐单个区域嵌入而忽略场景中语义概念组合结构的问题，提出了一种对齐区域包（Bag of Regions）的方法。该方法将上下文相关的区域分组为包，将包内区域嵌入视为句子中的词，通过VLM的文本编码器获得包级嵌入，并与冻结VLM提取的对应特征对齐。相比已有工作，该方法充分利用了VLM隐式学习的组合结构，在开放词汇COCO和LVIS基准上，新类别的box AP50和mask AP分别提升了4.6和2.8。
- **摘要（英）**: This paper addresses the limitation of existing open-vocabulary detectors that align individual region embeddings, neglecting the compositional structure of semantic concepts. It proposes aligning bag-of-regions embeddings, where contextually related regions are grouped and processed by a VLM text encoder, achieving 4.6 box AP50 and 2.8 mask AP improvements on novel categories in COCO and LVIS.
- **核心贡献**: 提出区域包对齐策略，利用VLM的组合结构提升开放词汇检测。
- **创新点**: 将区域嵌入作为词序列输入VLM文本编码器，实现包级对齐。
- **结果**: 在COCO和LVIS新类别上分别提升4.6 box AP50和2.8 mask AP。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models (VLMs) learn to align vision and language representations on large-scale datasets, where each image-text pair usually contains a bag of semantic concepts. However, existing open-vocabulary object detectors only align region embeddings individually with the corresponding features extracted from the VLMs. Such a design leaves the compositional structure of semantic concepts in a scene under-exploited, although the structure may be implicitly learned by the VLMs. In this work, we propose to align the embedding of bag of regions beyond individual regions. The proposed method groups contextually interrelated regions as a bag. The embeddings of regions in a bag are treated as embeddings of words in a sentence, and they are sent to the text encoder of a VLM to obtain the bag-of-regions embedding, which is learned to be aligned to the corresponding features extracted by a frozen VLM. Applied to the commonly used Faster R-CNN, our approach surpasses the previous best results by 4.6 box AP50 and 2.8 mask AP on novel categories of open-vocabulary COCO and LVIS benchmarks, respectively. Code and models are available at https://github.com/wusize/ovdet.

</details>

### DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2304.04514](https://arxiv.org/abs/2304.04514) · 📚 被引 80
- **作者**: Lewei Yao, Jianhua Han, Xiaodan Liang, Dan Xu, Wei Zhang, Zhenguo Li et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab, Shenzhen Campus of Sun Yat-Sen University
- **会议**: CVPR 2023
- **摘要（中）**: 针对开放词汇检测依赖预训练VLM或伪标签过程的问题，提出了DetCLIPv2，一种直接从大规模图像-文本对中端到端学习词-区域对齐的高效可扩展框架。该方法通过最大化区域提议与文本词之间的相似性来指导对比学习，并采用统一数据格式混合检测、定位和图像-文本对数据进行训练。相比DetCLIP，DetCLIPv2利用13倍多的图像-文本对，训练时间相近且性能提升，展示了优越的开放词汇检测能力。
- **摘要（英）**: DetCLIPv2 proposes an efficient and scalable framework for open-vocabulary detection, directly learning word-region alignment from massive image-text pairs in an end-to-end manner. It uses maximum word-region similarity for contrastive learning and hybrid supervision, achieving superior performance with 13x more image-text pairs at similar training cost.
- **核心贡献**: 提出端到端词-区域对齐的开放词汇检测预训练框架。
- **创新点**: 利用最大词-区域相似性指导对比学习，并统一多种数据源。
- **结果**: 利用13倍图像-文本对，在相似训练时间内提升开放词汇检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents DetCLIPv2, an efficient and scalable training framework that incorporates large-scale image-text pairs to achieve open-vocabulary object detection (OVD). Unlike previous OVD frameworks that typically rely on a pre-trained vision-language model (e.g., CLIP) or exploit image-text pairs via a pseudo labeling process, DetCLIPv2 directly learns the fine-grained word-region alignment from massive image-text pairs in an end-to-end manner. To accomplish this, we employ a maximum word-region similarity between region proposals and textual words to guide the contrastive objective. To enable the model to gain localization capability while learning broad concepts, DetCLIPv2 is trained with a hybrid supervision from detection, grounding and image-text pair data under a unified data formulation. By jointly training with an alternating scheme and adopting low-resolution input for image-text pairs, DetCLIPv2 exploits image-text pair data efficiently and effectively: DetCLIPv2 utilizes 13X more image-text pairs than DetCLIP with a similar training time and improves performance. With 13M image-text pairs for pre-training, DetCLIPv2 demonstrates superior open-vocabulary detection performance, e.g., DetCLIPv2 with Swin-T backbone achieves 40.4% zero-shot AP on the LVIS benchmark, which outperforms previous works GLIP/GLIPv2/DetCLIP by 14.4/11.4/4.5% AP, respectively, and even beats its fully-supervised counterpart by a large margin.

</details>

### Open-Vocabulary Semantic Segmentation with Mask-adapted CLIP. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2210.04150](https://arxiv.org/abs/2210.04150) · 📚 被引 455
- **作者**: Feng Liang, Bichen Wu, Xiaoliang Dai, Kunpeng Li, Yinan Zhao, Hang Zhang et al.
- **🏷️ 机构**: The University of Texas at Austin, Meta Reality Labs, Cruise
- **会议**: CVPR 2023
- **摘要（中）**: 针对开放词汇语义分割中预训练CLIP模型在掩码图像上性能不佳的问题，提出掩码自适应CLIP方法。方法通过微调CLIP在掩码图像区域和文本描述上，并利用掩码提示调优处理空白区域，提升分割性能。相比传统两阶段方法，该工作通过微调和提示调优显著改善CLIP对掩码图像的适应性，实验表明掩码提示调优在不修改权重的情况下带来显著提升。
- **摘要（英）**: This paper addresses the bottleneck of pre-trained CLIP performing poorly on masked images in open-vocabulary semantic segmentation by proposing mask-adapted CLIP. It finetunes CLIP on masked regions and text descriptions, and uses mask prompt tuning to handle blank areas, significantly improving segmentation performance. Experiments show mask prompt tuning brings substantial gains without modifying CLIP weights.
- **核心贡献**: 提出掩码自适应CLIP和掩码提示调优，提升开放词汇语义分割性能。
- **创新点**: 通过微调和提示调优增强CLIP对掩码图像的适应性。
- **结果**: 掩码提示调优带来显著性能提升，且无需修改CLIP权重。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation aims to segment an image into semantic regions according to text descriptions, which may not have been seen during training. Recent two-stage methods first generate class-agnostic mask proposals and then leverage pre-trained vision-language models, e.g., CLIP, to classify masked regions. We identify the performance bottleneck of this paradigm to be the pre-trained CLIP model, since it does not perform well on masked images. To address this, we propose to finetune CLIP on a collection of masked image regions and their corresponding text descriptions. We collect training data by mining an existing image-caption dataset (e.g., COCO Captions), using CLIP to match masked image regions to nouns in the image captions. Compared with the more precise and manually annotated segmentation labels with fixed classes (e.g., COCO-Stuff), we find our noisy but diverse dataset can better retain CLIP's generalization ability. Along with finetuning the entire model, we utilize the "blank" areas in masked images using a method we dub mask prompt tuning. Experiments demonstrate mask prompt tuning brings significant improvement without modifying any weights of CLIP, and it can further improve a fully finetuned model. In particular, when trained on COCO and evaluated on ADE20K-150, our best model achieves 29.6% mIoU, which is +8.5% higher than the previous state-of-the-art. For the first time, open-vocabulary generalist models match the performance of supervised specialist models in 2017 without dataset-specific adaptations.

</details>

### Learning to Generate Text-Grounded Mask for Open-World Semantic Segmentation from Only Image-Text Pairs. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2212.00785](https://arxiv.org/abs/2212.00785) · 📚 被引 99
- **作者**: Junbum Cha, Jonghwan Mun, Byungseok Roh
- **🏷️ 机构**: Kakao Brain
- **会议**: CVPR 2023
- **摘要（中）**: 针对开放世界语义分割中对比学习训练与测试不一致（图像级对齐vs区域级对齐）的问题，提出文本接地对比学习（TCL）框架，直接学习区域-文本对齐。方法为给定文本生成分割掩码，提取文本接地图像嵌入并与文本嵌入对齐，从而直接提升掩码质量。在8个广泛使用的语义分割数据集上进行了统一评估，但摘要未提供具体数值。
- **摘要（英）**: Addressing the train-test discrepancy in open-world semantic segmentation, this work proposes Text-grounded Contrastive Learning (TCL) to directly learn region-text alignment by generating masks for text, extracting text-grounded embeddings, and aligning them with text embeddings. A unified evaluation on 8 datasets is presented, though specific performance numbers are not given in the abstract.
- **核心贡献**: 提出文本接地对比学习框架，实现直接区域-文本对齐。
- **创新点**: 通过生成掩码并提取文本接地嵌入，消除训练测试差异。
- **结果**: 在8个数据集上统一评估，但摘要未提供具体数据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle open-world semantic segmentation, which aims at learning to segment arbitrary visual concepts in images, by using only image-text pairs without dense annotations. Existing open-world segmentation methods have shown impressive advances by employing contrastive learning (CL) to learn diverse visual concepts and transferring the learned image-level understanding to the segmentation task. However, these CL-based methods suffer from a train-test discrepancy, since it only considers image-text alignment during training, whereas segmentation requires region-text alignment during testing. In this paper, we proposed a novel Text-grounded Contrastive Learning (TCL) framework that enables a model to directly learn region-text alignment. Our method generates a segmentation mask for a given text, extracts text-grounded image embedding from the masked region, and aligns it with text embedding via TCL. By learning region-text alignment directly, our framework encourages a model to directly improve the quality of generated segmentation masks. In addition, for a rigorous and fair comparison, we present a unified evaluation protocol with widely used 8 semantic segmentation datasets. TCL achieves state-of-the-art zero-shot segmentation performances with large margins in all datasets. Code is available at https://github.com/kakaobrain/tcl.

</details>

### Accelerating Vision-Language Pretraining with Free Language Modeling. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2303.14038](https://arxiv.org/abs/2303.14038) · 📚 被引 8
- **作者**: Teng Wang, Yixiao Ge, Feng Zheng, Ran Cheng, Ying Shan, Xiaohu Qie et al.
- **🏷️ 机构**: Southern University of Science and Technology, ARC Lab, Tencent PCG
- **会议**: CVPR 2023
- **摘要（中）**: 针对视觉语言预训练（VLP）中训练成本高、收敛慢的问题，该论文指出掩码语言建模（MLM）中预测率与损坏率耦合是主要障碍。作者提出自由语言建模（FLM）任务，实现100%预测率与任意损坏率解耦，并允许为每个预测token定制损坏跨度。相比MLM方法，FLM在相同GPU时间下训练速度提升2.5倍，同时保持性能，通过更灵活的双向上下文利用促进模型学习。
- **摘要（英）**: This paper addresses the high training cost and slow convergence in vision-language pretraining (VLP), attributing it to the entanglement of prediction rate and corruption rate in masked language modeling (MLM). It proposes Free Language Modeling (FLM), which decouples the prediction rate from corruption rate, enabling 100% prediction with arbitrary corruption and customized spans. FLM achieves a 2.5x pretraining time reduction over MLM-based methods while maintaining performance, by exploiting bidirectional contexts more flexibly.
- **核心贡献**: 提出FLM预训练任务，解耦预测率与损坏率，显著加速VLP训练。
- **创新点**: 创新性地实现100%预测率与任意损坏率解耦，并支持定制化损坏跨度。
- **结果**: 训练时间减少2.5倍，性能与MLM方法相当。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The state of the arts in vision-language pretraining (VLP) achieves exemplary performance but suffers from high training costs resulting from slow convergence and long training time, especially on large-scale web datasets. An essential obstacle to training efficiency lies in the entangled prediction rate (percentage of tokens for reconstruction) and corruption rate (percentage of corrupted tokens) in masked language modeling (MLM), that is, a proper corruption rate is achieved at the cost of a large portion of output tokens being excluded from prediction loss. To accelerate the convergence of VLP, we propose a new pretraining task, namely, free language modeling (FLM), that enables a 100% prediction rate with arbitrary corruption rates. FLM successfully frees the prediction rate from the tie-up with the corruption rate while allowing the corruption spans to be customized for each token to be predicted. FLM-trained models are encouraged to learn better and faster given the same GPU time by exploiting bidirectional contexts more flexibly. Extensive experiments show FLM could achieve an impressive 2.5x pretraining time reduction in comparison to the MLM-based methods, while keeping competitive performance on both vision-language understanding and generation tasks. Code will be public at https://github.com/TencentARC/FLM.

</details>

### Q: How to Specialize Large Vision-Language Models to Data-Scarce VQA Tasks? A: Self-Train on Unlabeled Images! **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2306.03932](https://arxiv.org/abs/2306.03932) · 📚 被引 13
- **作者**: Zaid Khan, B. G. Vijay Kumar, Samuel Schulter, Xiang Yu, Yun Fu, Manmohan Chandraker
- **🏷️ 机构**: Northeastern University, NEC Labs America, Amazon
- **会议**: CVPR 2023
- **摘要（中）**: 针对大规模视觉语言模型在数据稀缺的VQA任务上微调效果不佳的问题，提出SelTDA自训练数据增强策略。方法利用目标数据集和VLM构建教师模型，直接基于图像生成问答伪标签，扩充未标注图像，再微调初始VLM。相比标准微调，增强了对对抗性问题和域泛化的鲁棒性，且无需额外标注。
- **摘要（英）**: This paper tackles the challenge of finetuning large VLMs on data-scarce VQA tasks by introducing SelTDA, a self-taught data augmentation strategy that uses a teacher model to generate question-answer pseudolabels from unlabeled images. It improves robustness to adversarial questions and domain generalization without extra annotations.
- **核心贡献**: 提出了一种无需额外标注的自训练数据增强方法，提升VLM在数据稀缺任务上的泛化能力。
- **创新点**: 利用VLM自身生成伪标签来扩充训练数据，形成自举式学习。
- **结果**: 在多个VQA基准上增强了鲁棒性和数值推理能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Finetuning a large vision language model (VLM) on a target dataset after large scale pretraining is a dominant paradigm in visual question answering (VQA). Datasets for specialized tasks such as knowledge-based VQA or VQA in non natural-image domains are orders of magnitude smaller than those for general-purpose VQA. While collecting additional labels for specialized tasks or domains can be challenging, unlabeled images are often available. We introduce SelTDA (Self-Taught Data Augmentation), a strategy for finetuning large VLMs on small-scale VQA datasets. SelTDA uses the VLM and target dataset to build a teacher model that can generate question-answer pseudolabels directly conditioned on an image alone, allowing us to pseudolabel unlabeled images. SelTDA then finetunes the initial VLM on the original dataset augmented with freshly pseudolabeled images. We describe a series of experiments showing that our self-taught data augmentation increases robustness to adversarially searched questions, counterfactual examples and rephrasings, improves domain generalization, and results in greater retention of numerical reasoning skills. The proposed strategy requires no additional annotations or architectural modifications, and is compatible with any modern encoder-decoder multimodal transformer. Code available at https://github.com/codezakh/SelTDA.

</details>

### Task Residual for Tuning Vision-Language Models. **⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2211.10277](https://arxiv.org/abs/2211.10277) · 📚 被引 117
- **作者**: Tao Yu, Zhihe Lu, Xin Jin, Zhibo Chen, Xinchao Wang
- **🏷️ 机构**: National University of Singapore, University of Science and Technology of China
- **会议**: CVPR 2023
- **摘要（中）**: 针对视觉语言模型（VLM）迁移到下游任务时，现有高效迁移学习方法（如提示调优和适配器调优）会破坏或过度偏向前人知识的问题，该论文提出Task Residual Tuning（TaskRes）。该方法直接在文本分类器上操作，通过冻结原始分类器权重并调整一组残差参数来获得新分类器，显式解耦先验知识与任务特定知识。TaskRes在保留可靠先验知识的同时，灵活探索任务特定知识，在多个下游任务上表现优异。
- **摘要（英）**: This paper addresses the issue that existing efficient transfer learning methods for vision-language models (VLMs), such as prompt tuning and adapter-style tuning, either damage or excessively bias prior knowledge. It proposes Task Residual Tuning (TaskRes), which operates on the text-based classifier by freezing original weights and tuning a residual parameter set, explicitly decoupling prior and task-specific knowledge. TaskRes preserves reliable prior knowledge while enabling flexible task adaptation, achieving strong performance on downstream tasks.
- **核心贡献**: 提出TaskRes方法，通过残差调优解耦先验与任务知识，提升VLM迁移效率。
- **创新点**: 创新性地在文本分类器上使用残差参数，避免破坏预训练知识。
- **结果**: 在多个下游任务上性能优于现有ETL方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale vision-language models (VLMs) pre-trained on billion-level data have learned general visual representations and broad visual concepts. In principle, the well-learned knowledge structure of the VLMs should be inherited appropriately when being transferred to downstream tasks with limited data. However, most existing efficient transfer learning (ETL) approaches for VLMs either damage or are excessively biased towards the prior knowledge, e.g., prompt tuning (PT) discards the pre-trained text-based classifier and builds a new one while adapter-style tuning (AT) fully relies on the pre-trained features. To address this, we propose a new efficient tuning approach for VLMs named Task Residual Tuning (TaskRes), which performs directly on the text-based classifier and explicitly decouples the prior knowledge of the pre-trained models and new knowledge regarding a target task. Specifically, TaskRes keeps the original classifier weights from the VLMs frozen and obtains a new classifier for the target task by tuning a set of prior-independent parameters as a residual to the original one, which enables reliable prior knowledge preservation and flexible task-specific knowledge exploration. The proposed TaskRes is simple yet effective, which significantly outperforms previous ETL methods (e.g., PT and AT) on 11 benchmark datasets while requiring minimal effort for the implementation. Our code is available at https://github.com/geekyutao/TaskRes.

</details>

### Adaptive Zone-aware Hierarchical Planner for Vision-Language Navigation. **⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01432) · 📚 被引 38
- **作者**: Chen Gao, Xingyu Peng, Mi Yan, He Wang, Lirong Yang, Haibing Ren et al.
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, CFCS and School of EECS, Peking University, Meituan
- **会议**: CVPR 2023
- **摘要（中）**: 该论文摘要为空，无法获取具体研究内容。标题涉及视觉语言导航的自适应区域感知分层规划器，可能针对导航任务中的区域感知和规划问题，但缺乏详细信息。
- **摘要（英）**: The abstract is empty, so specific research content is unavailable. The title suggests an adaptive zone-aware hierarchical planner for vision-language navigation, potentially addressing region-aware planning, but details are missing.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### FAME-ViL: Multi-Tasking Vision-Language Model for Heterogeneous Fashion Tasks. **⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:2303.02483](https://arxiv.org/abs/2303.02483) · 📚 被引 50
- **作者**: Xiao Han, Xiatian Zhu, Licheng Yu, Li Zhang, Yi-Zhe Song, Tao Xiang
- **🏷️ 机构**: University of Surrey,CVSSP, Fudan University
- **会议**: CVPR 2023
- **摘要（中）**: 针对时尚领域多种异构视觉语言任务需要独立微调导致参数效率低的问题，提出FAME-ViL多任务学习方法。方法采用统一模型集成跨注意力适配器和任务特定适配器，并设计稳定多任务训练策略防止负迁移。相比独立模型，节省61.5%参数，同时保持或提升四个时尚任务性能。
- **摘要（英）**: This paper addresses parameter inefficiency in handling heterogeneous fashion V+L tasks by proposing FAME-ViL, a unified multi-task model with cross-attention and task-specific adapters, plus a stable training strategy. It saves 61.5% parameters while maintaining performance across four fashion tasks.
- **核心贡献**: 提出了一个参数高效的多任务视觉语言模型，适用于异构时尚任务。
- **创新点**: 结合适配器机制和负迁移抑制策略，实现单模型多任务学习。
- **结果**: 在四个时尚任务上显著减少参数并保持性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the fashion domain, there exists a variety of vision-and-language (V+L) tasks, including cross-modal retrieval, text-guided image retrieval, multi-modal classification, and image captioning. They differ drastically in each individual input/output format and dataset size. It has been common to design a task-specific model and fine-tune it independently from a pre-trained V+L model (e.g., CLIP). This results in parameter inefficiency and inability to exploit inter-task relatedness. To address such issues, we propose a novel FAshion-focused Multi-task Efficient learning method for Vision-and-Language tasks (FAME-ViL) in this work. Compared with existing approaches, FAME-ViL applies a single model for multiple heterogeneous fashion tasks, therefore being much more parameter-efficient. It is enabled by two novel components: (1) a task-versatile architecture with cross-attention adapters and task-specific adapters integrated into a unified V+L model, and (2) a stable and effective multi-task training strategy that supports learning from heterogeneous data and prevents negative transfer. Extensive experiments on four fashion tasks show that our FAME-ViL can save 61.5% of parameters over alternatives, while significantly outperforming the conventional independently trained single-task models. Code is available at https://github.com/BrandonHanx/FAME-ViL.

</details>

### VILA: Learning Image Aesthetics from User Comments with Vision-Language Pretraining. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2303.14302](https://arxiv.org/abs/2303.14302) · 📚 被引 83
- **作者**: Junjie Ke, Keren Ye, Jiahui Yu, Yonghui Wu, Peyman Milanfar, Feng Yang
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2023
- **摘要（中）**: 针对现有图像美学评估依赖人工评分标签、信息简化的问题，提出从用户评论学习美学，并采用视觉语言预训练方法。方法预训练图像-文本编码解码器，使用对比和生成目标学习美学语义，并设计轻量级排序适配器用于下游任务。在AVA-Captions数据集上，美学描述任务优于先前方法。
- **摘要（英）**: This paper addresses the oversimplification of human-rated scores in image aesthetic assessment by learning from user comments via vision-language pretraining, using contrastive and generative objectives, and a rank-based adapter. It outperforms prior works on aesthetic captioning over AVA-Captions.
- **核心贡献**: 提出了一个基于用户评论的美学视觉语言预训练模型。
- **创新点**: 利用自然语言评论作为监督信号，替代传统评分标签。
- **结果**: 在美学描述任务上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Assessing the aesthetics of an image is challenging, as it is influenced by multiple factors including composition, color, style, and high-level semantics. Existing image aesthetic assessment (IAA) methods primarily rely on human-labeled rating scores, which oversimplify the visual aesthetic information that humans perceive. Conversely, user comments offer more comprehensive information and are a more natural way to express human opinions and preferences regarding image aesthetics. In light of this, we propose learning image aesthetics from user comments, and exploring vision-language pretraining methods to learn multimodal aesthetic representations. Specifically, we pretrain an image-text encoder-decoder model with image-comment pairs, using contrastive and generative objectives to learn rich and generic aesthetic semantics without human labels. To efficiently adapt the pretrained model for downstream IAA tasks, we further propose a lightweight rank-based adapter that employs text as an anchor to learn the aesthetic ranking concept. Our results show that our pretrained aesthetic vision-language model outperforms prior works on image aesthetic captioning over the AVA-Captions dataset, and it has powerful zero-shot capability for aesthetic tasks such as zero-shot style classification and zero-shot IAA, surpassing many supervised baselines. With only minimal finetuning parameters using the proposed adapter module, our model achieves state-of-the-art IAA performance over the AVA dataset.

</details>

### CrowdCLIP: Unsupervised Crowd Counting via Vision-Language Model. **⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2304.04231](https://arxiv.org/abs/2304.04231) · 📚 被引 90
- **作者**: Dingkang Liang, Jiahao Xie, Zhikang Zou, Xiaoqing Ye, Wei Xu, Xiang Bai
- **🏷️ 机构**: Huazhong University of Science and Technology, Beijing University of Posts and Telecommunications, Baidu Inc.,China
- **会议**: CVPR 2023
- **摘要（中）**: 针对监督式人群计数依赖昂贵人工标注的问题，提出无监督框架CrowdCLIP。方法利用CLIP的视觉语言知识，通过多模态排序损失匹配排序文本提示和人群块，并在测试阶段用渐进过滤策略选择高潜力块映射到语言空间。在五个数据集上优于先前无监督方法。
- **摘要（英）**: This paper addresses costly manual labeling in crowd counting by proposing CrowdCLIP, an unsupervised framework leveraging CLIP's vision-language knowledge with a multi-modal ranking loss and progressive filtering. It achieves superior performance on five datasets compared to prior unsupervised methods.
- **核心贡献**: 首次将视觉语言模型用于无监督人群计数。
- **创新点**: 利用排序文本提示和渐进过滤策略实现无监督计数。
- **结果**: 在多个数据集上超越现有无监督方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Supervised crowd counting relies heavily on costly manual labeling, which is difficult and expensive, especially in dense scenes. To alleviate the problem, we propose a novel unsupervised framework for crowd counting, named CrowdCLIP. The core idea is built on two observations: 1) the recent contrastive pre-trained vision-language model (CLIP) has presented impressive performance on various downstream tasks; 2) there is a natural mapping between crowd patches and count text. To the best of our knowledge, CrowdCLIP is the first to investigate the vision language knowledge to solve the counting problem. Specifically, in the training stage, we exploit the multi-modal ranking loss by constructing ranking text prompts to match the size-sorted crowd patches to guide the image encoder learning. In the testing stage, to deal with the diversity of image patches, we propose a simple yet effective progressive filtering strategy to first select the highly potential crowd patches and then map them into the language space with various counting intervals. Extensive experiments on five challenging datasets demonstrate that the proposed CrowdCLIP achieves superior performance compared to previous unsupervised state-of-the-art counting methods. Notably, CrowdCLIP even surpasses some popular fully-supervised methods under the cross-dataset setting. The source code will be available at https://github.com/dk-liang/CrowdCLIP.

</details>

### @ CREPE: Can Vision-Language Foundation Models Reason Compositionally? **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01050) · 📚 被引 73
- **作者**: Zixian Ma, Jerry Hong, Mustafa Omer Gul, Mona Gandhi, Irena Gao, Ranjay Krishna
- **🏷️ 机构**: Stanford University, Cornell University, University of Pennsylvania
- **会议**: CVPR 2023
- **摘要（中）**: 该论文摘要为空，但标题表明其研究视觉语言基础模型的组合推理能力。可能针对VLM在组合性任务上的不足，提出评估或改进方法，但缺乏具体细节。
- **摘要（英）**: The abstract is empty, but the title indicates a study on compositional reasoning in vision-language foundation models. It likely addresses limitations in compositionality, but details are unavailable.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### HOICLIP: Efficient Knowledge Transfer for HOI Detection with Vision-Language Models. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2303.15786](https://arxiv.org/abs/2303.15786) · 📚 被引 91
- **作者**: Shan Ning, Longtian Qiu, Yongfei Liu, Xuming He
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China, ByteDance Inc.
- **会议**: CVPR 2023
- **摘要（中）**: 针对人类-物体交互（HOI）检测中依赖大规模训练数据且少样本/零样本性能差的问题，该论文提出HOICLIP框架，高效提取CLIP的先验知识。方法包括：引入交互解码器通过交叉注意力提取CLIP视觉特征中的信息区域，并与检测骨干融合；利用CLIP文本编码器生成分类器，并通过视觉语义算术和轻量适配器构建动词分类器；提出训练-free增强利用全局HOI预测。HOICLIP在少样本和零样本场景下显著提升泛化能力。
- **摘要（英）**: This paper addresses the issue of HOI detection relying on large-scale training data and suffering from poor few/zero-shot performance. It proposes HOICLIP, which efficiently extracts prior knowledge from CLIP via an interaction decoder with cross-attention, fused with the detection backbone, and leverages text embeddings for classifiers. HOICLIP achieves better generalization in few/zero-shot scenarios.
- **核心贡献**: 提出HOICLIP框架，高效迁移CLIP知识至HOI检测，提升少样本泛化。
- **创新点**: 创新性地使用交叉注意力提取CLIP视觉特征，并构建轻量动词分类器。
- **结果**: 在少样本和零样本HOI检测上性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-Object Interaction (HOI) detection aims to localize human-object pairs and recognize their interactions. Recently, Contrastive Language-Image Pre-training (CLIP) has shown great potential in providing interaction prior for HOI detectors via knowledge distillation. However, such approaches often rely on large-scale training data and suffer from inferior performance under few/zero-shot scenarios. In this paper, we propose a novel HOI detection framework that efficiently extracts prior knowledge from CLIP and achieves better generalization. In detail, we first introduce a novel interaction decoder to extract informative regions in the visual feature map of CLIP via a cross-attention mechanism, which is then fused with the detection backbone by a knowledge integration block for more accurate human-object pair detection. In addition, prior knowledge in CLIP text encoder is leveraged to generate a classifier by embedding HOI descriptions. To distinguish fine-grained interactions, we build a verb classifier from training data via visual semantic arithmetic and a lightweight verb representation adapter. Furthermore, we propose a training-free enhancement to exploit global HOI predictions from CLIP. Extensive experiments demonstrate that our method outperforms the state of the art by a large margin on various settings, e.g. +4.04 mAP on HICO-Det. The source code is available in https://github.com/Artanic30/HOICLIP.

</details>

### DeAR: Debiasing Vision-Language Models with Additive Residuals. **⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2303.10431](https://arxiv.org/abs/2303.10431) · 📚 被引 34
- **作者**: Ashish Seth, Mayur Hemani, Chirag Agarwal
- **🏷️ 机构**: IIT Madras,India, Adobe Inc.
- **会议**: CVPR 2023
- **摘要（中）**: 针对预训练视觉语言模型（VLM）因训练数据分布不均而存在社会偏见的问题，该论文提出DeAR（Debiasing with Additive Residuals）方法。DeAR学习加性残差图像表示来偏移原始表示，确保输出表示公平，减少不同身份群体间的区分能力。此外，论文引入受保护属性标签关联数据集以更好评估偏见，弥补现有公平性测试的不足。
- **摘要（英）**: This paper addresses societal biases in pre-trained vision-language models (VLMs) caused by skewed training data. It proposes DeAR, which learns additive residual image representations to offset original ones, ensuring fair outputs and reducing distinctions between identity groups. It also introduces a new dataset for better bias evaluation.
- **核心贡献**: 提出DeAR去偏方法，并引入新评估数据集。
- **创新点**: 创新性地使用加性残差表示进行去偏。
- **结果**: 有效减少VLM表示中的身份偏见。

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

### Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models.
- **链接**: [arXiv:2301.00182](https://arxiv.org/abs/2301.00182) · 📚 被引 106
- **作者**: Wenhao Wu, Xiaohan Wang, Haipeng Luo, Jingdong Wang, Yi Yang, Wanli Ouyang
- **🏷️ 机构**: The University of Sydney, Zhejiang University, University of Chinese Academy of Sciences
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) pre-trained on large-scale image-text pairs have demonstrated impressive transferability on various visual tasks. Transferring knowledge from such powerful VLMs is a promising direction for building effective video recognition models. However, current exploration in this field is still limited. We believe that the greatest value of pre-trained VLMs lies in building a bridge between visual and textual domains. In this paper, we propose a novel framework called BIKE, which utilizes the cross-modal bridge to explore bidirectional knowledge: i) We introduce the Video Attribute Association mechanism, which leverages the Video-to-Text knowledge to generate textual auxiliary attributes for complementing video recognition. ii) We also present a Temporal Concept Spotting mechanism that uses the Text-to-Video expertise to capture temporal saliency in a parameter-free manner, leading to enhanced video representation. Extensive studies on six popular video datasets, including Kinetics-400 & 600, UCF-101, HMDB-51, ActivityNet and Charades, show that our method achieves state-of-the-art performance in various recognition scenarios, such as general, zero-shot, and few-shot video recognition. Our best model achieves a state-of-the-art accuracy of 88.6% on the challenging Kinetics-400 using the released CLIP model. The code is available at https://github.com/whwu95/BIKE .

</details>

### Vita-CLIP: Video and text adaptive CLIP via Multimodal Prompting.
- **链接**: [arXiv:2304.03307](https://arxiv.org/abs/2304.03307) · 📚 被引 109
- **作者**: Syed Talal Wasim, Muzammal Naseer, Salman H. Khan, Fahad Shahbaz Khan, Mubarak Shah
- **🏷️ 机构**: Mohamed bin Zayed University of AI, University of Central Florida
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adopting contrastive image-text pretrained models like CLIP towards video classification has gained attention due to its cost-effectiveness and competitive performance. However, recent works in this area face a trade-off. Finetuning the pretrained model to achieve strong supervised performance results in low zero-shot generalization. Similarly, freezing the backbone to retain zero-shot capability causes significant drop in supervised accuracy. Because of this, recent works in literature typically train separate models for supervised and zero-shot action recognition. In this work, we propose a multimodal prompt learning scheme that works to balance the supervised and zero-shot performance under a single unified training. Our prompting approach on the vision side caters for three aspects: 1) Global video-level prompts to model the data distribution; 2) Local frame-level prompts to provide per-frame discriminative conditioning; and 3) a summary prompt to extract a condensed video representation. Additionally, we define a prompting scheme on the text side to augment the textual context. Through this prompting scheme, we can achieve state-of-the-art zero-shot performance on Kinetics-600, HMDB51 and UCF101 while remaining competitive in the supervised setting. By keeping the pretrained backbone frozen, we optimize a much lower number of parameters and retain the existing general representation which helps achieve the strong zero-shot performance. Our codes/models are released at https://github.com/TalalWasim/Vita-CLIP.

</details>

### Reproducible Scaling Laws for Contrastive Language-Image Learning.
- **链接**: [arXiv:2212.07143](https://arxiv.org/abs/2212.07143) · 📚 被引 620
- **作者**: Mehdi Cherti, Romain Beaumont, Ross Wightman, Mitchell Wortsman, Gabriel Ilharco, Cade Gordon et al.
- **🏷️ 机构**: LAION, HuggingFace, University of Washington
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling up neural networks has led to remarkable performance across a wide range of tasks. Moreover, performance often follows reliable scaling laws as a function of training set size, model size, and compute, which offers valuable guidance as large-scale experiments are becoming increasingly expensive. However, previous work on scaling laws has primarily used private data \& models or focused on uni-modal language or vision learning. To address these limitations, we investigate scaling laws for contrastive language-image pre-training (CLIP) with the public LAION dataset and the open-source OpenCLIP repository. Our large-scale experiments involve models trained on up to two billion image-text pairs and identify power law scaling for multiple downstream tasks including zero-shot classification, retrieval, linear probing, and end-to-end fine-tuning. We find that the training distribution plays a key role in scaling laws as the OpenAI and OpenCLIP models exhibit different scaling behavior despite identical model architectures and similar training recipes. We open-source our evaluation workflow and all models, including the largest public CLIP models, to ensure reproducibility and make scaling laws research more accessible. Source code and instructions to reproduce this study will be available at https://github.com/LAION-AI/scaling-laws-openclip

</details>

### Identity-Consistent Aggregation for Video Object Detection.
- **链接**: [arXiv:2308.07737](https://arxiv.org/abs/2308.07737) · 📚 被引 10
- **作者**: Chaorui Deng, Da Chen, Qi Wu
- **🏷️ 机构**: University of Adelaide,Australia Institute of Machine Learning, University of Bath,Department of Computer Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Video Object Detection (VID), a common practice is to leverage the rich temporal contexts from the video to enhance the object representations in each frame. Existing methods treat the temporal contexts obtained from different objects indiscriminately and ignore their different identities. While intuitively, aggregating local views of the same object in different frames may facilitate a better understanding of the object. Thus, in this paper, we aim to enable the model to focus on the identity-consistent temporal contexts of each object to obtain more comprehensive object representations and handle the rapid object appearance variations such as occlusion, motion blur, etc. However, realizing this goal on top of existing VID models faces low-efficiency problems due to their redundant region proposals and nonparallel frame-wise prediction manner. To aid this, we propose ClipVID, a VID model equipped with Identity-Consistent Aggregation (ICA) layers specifically designed for mining fine-grained and identity-consistent temporal contexts. It effectively reduces the redundancies through the set prediction strategy, making the ICA layers very efficient and further allowing us to design an architecture that makes parallel clip-wise predictions for the whole video clip. Extensive experimental results demonstrate the superiority of our method: a state-of-the-art (SOTA) performance (84.7% mAP) on the ImageNet VID dataset while running at a speed about 7x faster (39.3 fps) than previous SOTAs.

</details>

### EdaDet: Open-Vocabulary Object Detection Using Early Dense Alignment.
- **链接**: [arXiv:2309.01151](https://arxiv.org/abs/2309.01151) · 📚 被引 46
- **作者**: Cheng Shi, Sibei Yang
- **🏷️ 机构**: ShanghaiTech University,School of Information Science and Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models such as CLIP have boosted the performance of open-vocabulary object detection, where the detector is trained on base categories but required to detect novel categories. Existing methods leverage CLIP's strong zero-shot recognition ability to align object-level embeddings with textual embeddings of categories. However, we observe that using CLIP for object-level alignment results in overfitting to base categories, i.e., novel categories most similar to base categories have particularly poor performance as they are recognized as similar base categories. In this paper, we first identify that the loss of critical fine-grained local image semantics hinders existing methods from attaining strong base-to-novel generalization. Then, we propose Early Dense Alignment (EDA) to bridge the gap between generalizable local semantics and object-level prediction. In EDA, we use object-level supervision to learn the dense-level rather than object-level alignment to maintain the local fine-grained semantics. Extensive experiments demonstrate our superior performance to competing approaches under the same strict setting and without using external training resources, i.e., improving the +8.4% novel box AP50 on COCO and +3.9% rare mask AP on LVIS.

</details>

### CLIP2Point: Transfer CLIP to Point Cloud Classification with Image-Depth Pre-Training.
- **链接**: [arXiv:2210.01055](https://arxiv.org/abs/2210.01055) · 📚 被引 140
- **作者**: Tianyu Huang, Bowen Dong, Yunhan Yang, Xiaoshui Huang, Rynson W. H. Lau, Wanli Ouyang et al.
- **🏷️ 机构**: Harbin Institute of Technology, Shanghai AI Laboratory, City University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-training across 3D vision and language remains under development because of limited training data. Recent works attempt to transfer vision-language pre-training models to 3D vision. PointCLIP converts point cloud data to multi-view depth maps, adopting CLIP for shape classification. However, its performance is restricted by the domain gap between rendered depth maps and images, as well as the diversity of depth distributions. To address this issue, we propose CLIP2Point, an image-depth pre-training method by contrastive learning to transfer CLIP to the 3D domain, and adapt it to point cloud classification. We introduce a new depth rendering setting that forms a better visual effect, and then render 52,460 pairs of images and depth maps from ShapeNet for pre-training. The pre-training scheme of CLIP2Point combines cross-modality learning to enforce the depth features for capturing expressive visual and textual features and intra-modality learning to enhance the invariance of depth aggregation. Additionally, we propose a novel Dual-Path Adapter (DPA) module, i.e., a dual-path structure with simplified adapters for few-shot learning. The dual-path structure allows the joint use of CLIP and CLIP2Point, and the simplified adapter can well fit few-shot tasks without post-search. Experimental results show that CLIP2Point is effective in transferring CLIP knowledge to 3D vision. Our CLIP2Point outperforms PointCLIP and other self-supervised 3D networks, achieving state-of-the-art results on zero-shot and few-shot classification.

</details>

### CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning.
- **链接**: [arXiv:2303.03323](https://arxiv.org/abs/2303.03323) · 📚 被引 34
- **作者**: Hritik Bansal, Fan Yin, Nishad Singhi, Aditya Grover, Yu Yang, Kai-Wei Chang
- **🏷️ 机构**: UCLA
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal contrastive pretraining has been used to train multimodal representation models, such as CLIP, on large amounts of paired image-text data. However, previous studies have revealed that such models are vulnerable to backdoor attacks. Specifically, when trained on backdoored examples, CLIP learns spurious correlations between the embedded backdoor trigger and the target label, aligning their representations in the joint embedding space. Injecting even a small number of poisoned examples, such as 75 examples in 3 million pretraining data, can significantly manipulate the model's behavior, making it difficult to detect or unlearn such correlations. To address this issue, we propose CleanCLIP, a finetuning framework that weakens the learned spurious associations introduced by backdoor attacks by independently re-aligning the representations for individual modalities. We demonstrate that unsupervised finetuning using a combination of multimodal contrastive and unimodal self-supervised objectives for individual modalities can significantly reduce the impact of the backdoor attack. Additionally, we show that supervised finetuning on task-specific labeled image data removes the backdoor trigger from the CLIP vision encoder. We show empirically that CleanCLIP maintains model performance on benign examples while erasing a range of backdoor attacks on multimodal contrastive learning. The code and checkpoints are available at https://github.com/nishadsinghi/CleanCLIP.

</details>

### One-shot recognition of any material anywhere using contrastive learning with physics-based rendering.
- **链接**: [arXiv:2212.00648](https://arxiv.org/abs/2212.00648) · 📚 被引 8
- **作者**: Manuel S. Drehwald, Sagi Eppel, Jolina Li, Han Hao, Alán Aspuru-Guzik
- **🏷️ 机构**: Karlsruhe Institute of Technology, Vector Institute, University of Toronto
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual recognition of materials and their states is essential for understanding most aspects of the world, from determining whether food is cooked, metal is rusted, or a chemical reaction has occurred. However, current image recognition methods are limited to specific classes and properties and can't handle the vast number of material states in the world. To address this, we present MatSim: the first dataset and benchmark for computer vision-based recognition of similarities and transitions between materials and textures, focusing on identifying any material under any conditions using one or a few examples. The dataset contains synthetic and natural images. The synthetic images were rendered using giant collections of textures, objects, and environments generated by computer graphics artists. We use mixtures and gradual transitions between materials to allow the system to learn cases with smooth transitions between states (like gradually cooked food). We also render images with materials inside transparent containers to support beverage and chemistry lab use cases. We use this dataset to train a siamese net that identifies the same material in different objects, mixtures, and environments. The descriptor generated by this net can be used to identify the states of materials and their subclasses using a single image. We also present the first few-shot material recognition benchmark with images from a wide range of fields, including the state of foods and drinks, types of grounds, and many other use cases. We show that a net trained on the MatSim synthetic dataset outperforms state-of-the-art models like Clip on the benchmark and also achieves good results on other unsupervised material classification tasks.

</details>

### Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models.
- **链接**: [arXiv:2303.06628](https://arxiv.org/abs/2303.06628) · 📚 被引 90
- **作者**: Zangwei Zheng, Mingyuan Ma, Kai Wang, Ziheng Qin, Xiangyu Yue, Yang You
- **🏷️ 机构**: National University of Singapore, UC Berkeley, The Chinese University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) can help pre-trained vision-language models efficiently adapt to new or under-trained data distributions without re-training. Nevertheless, during the continual training of the Contrastive Language-Image Pre-training (CLIP) model, we observe that the model's zero-shot transfer ability significantly degrades due to catastrophic forgetting. Existing CL methods can mitigate forgetting by replaying previous data. However, since the CLIP dataset is private, replay methods cannot access the pre-training dataset. In addition, replaying data of previously learned downstream tasks can enhance their performance but comes at the cost of sacrificing zero-shot performance. To address this challenge, we propose a novel method ZSCL to prevent zero-shot transfer degradation in the continual learning of vision-language models in both feature and parameter space. In the feature space, a reference dataset is introduced for distillation between the current and initial models. The reference dataset should have semantic diversity but no need to be labeled, seen in pre-training, or matched image-text pairs. In parameter space, we prevent a large parameter shift by averaging weights during the training. We propose a more challenging Multi-domain Task Incremental Learning (MTIL) benchmark to evaluate different methods, where tasks are from various domains instead of class-separated in a single dataset. Our method outperforms other methods in the traditional class-incremental learning setting and the MTIL by 9.7% average score. Our code locates at https://github.com/Thunderbeee/ZSCL.

</details>

### ILLUME: Rationalizing Vision-Language Models through Human Interactions.
- **链接**: [出版页](https://proceedings.mlr.press/v202/brack23a.html)
- **作者**: Manuel Brack, Patrick Schramowski, Björn Deiseroth, Kristian Kersting
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Distilling Internet-Scale Vision-Language Models into Embodied Agents.
- **链接**: [出版页](https://proceedings.mlr.press/v202/sumers23a.html)
- **作者**: Theodore R. Sumers, Kenneth Marino, Arun Ahuja, Rob Fergus, Ishita Dasgupta
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### CityRefer: Geography-aware 3D Visual Grounding Dataset on City-scale Point Cloud Data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/f4cef76305dcad4efd3537da087ff520-Abstract-Datasets_and_Benchmarks.html)
- **作者**: Taiki Miyanishi, Fumiya Kitamori, Shuhei Kurita, Jungdae Lee, Motoaki Kawanabe, Nakamasa Inoue
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CLIP4HOI: Towards Adapting CLIP for Practical Zero-Shot HOI Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/8fd5bc08e744fe0dfe798c61d1575a22-Abstract-Conference.html)
- **作者**: Yunyao Mao, Jiajun Deng, Wengang Zhou, Li Li, Yao Fang, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- OmniLabel: A Challenging Benchmark for Language-Based Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Video OWL-ViT: Temporally-consistent open-world localization in video. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Learning to Detect and Segment for Open Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- OVTrack: Open-Vocabulary Multiple Object Tracking. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Open Vocabulary Semantic Segmentation with Patch Aligned Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Mask-Free OVIS: Open-Vocabulary Instance Segmentation without Manual Mask Annotations. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Learning Open-Vocabulary Semantic Segmentation Models From Natural Language Supervision. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Multimodality Helps Unimodality: Cross-Modal Few-Shot Learning with Multimodal Models. → [multimodal](../multimodal/Guideline%202023.md)
- Reveal: Retrieval-Augmented Visual-Language Pre-Training with Multi-Source Multimodal Knowledge Memory. → [multimodal](../multimodal/Guideline%202023.md)
- Non-Contrastive Learning Meets Language-Image Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- MaskCLIP: Masked Self-Distillation Advances Contrastive Language-Image Pretraining. → [knowledge-distillation](../knowledge-distillation/Guideline%202023.md)
- ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Unsupervised 3D Perception with 2D Vision-Language Distillation for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Contrastive Feature Masking Open-Vocabulary Vision Transformer. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Verbs in Action: Improving verb understanding in video-language models. → [video-understanding](../video-understanding/Guideline%202023.md)
- Video Action Recognition with Attentive Semantic Units. → [video-understanding](../video-understanding/Guideline%202023.md)
- Multimodal Parameter-Efficient Few-Shot Class Incremental Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- Exploring Open-Vocabulary Semantic Segmentation from CLIP Vision Encoder Distillation Only. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Open-VCLIP: Transforming CLIP to an Open-vocabulary Video Model via Interpolated Weight Optimization. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Convolutions Die Hard: Open-Vocabulary Segmentation with Single Frozen Convolutional CLIP. → [open-set-detection](../open-set-detection/Guideline%202023.md)
<!-- COMPLETE v1 papers=68 -->
