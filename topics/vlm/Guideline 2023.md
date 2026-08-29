# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLIP2Point: Transfer CLIP to Point Cloud Classification with Image-Depth Pre-Training.
- **链接**: [arXiv:2210.01055](https://arxiv.org/abs/2210.01055) · 📚 被引 140
- **作者**: Tianyu Huang, Bowen Dong, Yunhan Yang, Xiaoshui Huang, Rynson W. H. Lau, Wanli Ouyang et al.
- **🏷️ 机构**: Harbin Institute of Technology, Shanghai AI Laboratory, City University of Hong Kong
- **会议**: ICCV 2023

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

> Out-of-distribution (OOD) detection refers to training the model on an in-distribution (ID) dataset to classify whether the input images come from unknown classes. Considerable effort has been invested in designing various OOD detection methods based on either convolutional neural networks or transformers. However, zero-shot OOD detection methods driven by CLIP, which only require class names for ID, have received less attention. This paper presents a novel method, namely CLIP saying no (CLIPN), which empowers the logic of saying no within CLIP. Our key motivation is to equip CLIP with the capability of distinguishing OOD and ID samples using positive-semantic prompts and negation-semantic prompts. Specifically, we design a novel learnable no prompt and a no text encoder to capture negation semantics within images. Subsequently, we introduce two loss functions: the image-text binary-opposite loss and the text semantic-opposite loss, which we use to teach CLIPN to associate images with no prompts, thereby enabling it to identify unknown samples. Furthermore, we propose two threshold-free inference algorithms to perform OOD detection by utilizing negation semantics from no prompts and the text encoder. Experimental results on 9 benchmark datasets (3 ID datasets and 6 OOD datasets) for the OOD detection task demonstrate that CLIPN, based on ViT-B-16, outperforms 7 well-used algorithms by at least 2.34% and 11.64% in terms of AUROC and FPR95 for zero-shot OOD detection on ImageNet-1K. Our CLIPN can serve as a solid foundation for effectively leveraging CLIP in downstream OOD tasks. The code is available on https://github.com/xmed-lab/CLIPN.

</details>

### VL-Match: Enhancing Vision-Language Pretraining with Token-Level and Instance-Level Matching.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00244) · 📚 被引 4
- **作者**: Junyu Bi, Daixuan Cheng, Ping Yao, Bochen Pang, Yuefeng Zhan, Chuanguang Yang et al.
- **🏷️ 机构**: Institute of Computing Technology,Chinese Academy of Sciences,Beijing,China, Microsoft Corporation
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language (VL) pre-training has recently gained much attention for its transferability and flexibility in novel concepts (e.g., cross-modality transfer) across various visual tasks. However, VL-driven segmentation has been under-explored, and the existing approaches still have the burden of acquiring additional training images or even segmentation annotations to adapt a VL model to downstream segmentation tasks. In this paper, we introduce a novel image-free segmentation task where the goal is to perform semantic segmentation given only a set of the target semantic categories, but without any task-specific images and annotations. To tackle this challenging task, our proposed method, coined IFSeg, generates VL-driven artificial image-segmentation pairs and updates a pre-trained VL model to a segmentation task. We construct this artificial training data by creating a 2D map of random semantic categories and another map of their corresponding word tokens. Given that a pre-trained VL model projects visual and text tokens into a common space where tokens that share the semantics are located closely, this artificially generated word map can replace the real image inputs for such a VL model. Through an extensive set of experiments, our model not only establishes an effective baseline for this novel task but also demonstrates strong performances compared to existing methods that rely on stronger supervision, such as task-specific images and segmentation masks. Code is available at https://github.com/alinlab/ifseg.

</details>

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

### Local 3D Editing via 3D Distillation of CLIP Knowledge.
- **链接**: [arXiv:2306.12570](https://arxiv.org/abs/2306.12570) · 📚 被引 20
- **作者**: Junha Hyung, Sungwon Hwang, Daejin Kim, Hyunji Lee, Jaegul Choo
- **🏷️ 机构**: KAIST AI, Scatter Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D content manipulation is an important computer vision task with many real-world applications (e.g., product design, cartoon generation, and 3D Avatar editing). Recently proposed 3D GANs can generate diverse photorealistic 3D-aware contents using Neural Radiance fields (NeRF). However, manipulation of NeRF still remains a challenging problem since the visual quality tends to degrade after manipulation and suboptimal control handles such as 2D semantic maps are used for manipulations. While text-guided manipulations have shown potential in 3D editing, such approaches often lack locality. To overcome these problems, we propose Local Editing NeRF (LENeRF), which only requires text inputs for fine-grained and localized manipulation. Specifically, we present three add-on modules of LENeRF, the Latent Residual Mapper, the Attention Field Network, and the Deformation Network, which are jointly used for local manipulations of 3D features by estimating a 3D attention field. The 3D attention field is learned in an unsupervised way, by distilling the zero-shot mask generation capability of CLIP to the 3D space with multi-view guidance. We conduct diverse experiments and thorough evaluations both quantitatively and qualitatively.

</details>

## 跨领域论文（完整笔记在其他领域）

- Task-Oriented Multi-Modal Mutual Learning for Vision-Language Models. → [multimodal](../multimodal/Guideline%202023.md)
- Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202023.md)
- CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- CLIPTrans: Transferring Visual Knowledge with Pre-trained Models for Multimodal Machine Translation. → [multimodal](../multimodal/Guideline%202023.md)
- CLIP-Decoder : ZeroShot Multilabel Classification using Multimodal CLIP Aligned Representations. → [multimodal](../multimodal/Guideline%202023.md)
- Exploring Open-Vocabulary Semantic Segmentation from CLIP Vision Encoder Distillation Only. → [open-set-detection](../open-set-detection/Guideline%202023.md)
