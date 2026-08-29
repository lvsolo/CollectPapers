# VLM — 2024 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 66 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UMG-CLIP: A Unified Multi-granularity Vision Generalist for Open-World Understanding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72920-1_15) · 📚 被引 2
- **作者**: Bowen Shi, Peisen Zhao, Zichen Wang, Yuhang Zhang, Yaoming Wang, Jin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72761-0_4) · 📚 被引 130
- **作者**: Yunkang Cao, Jiangning Zhang, Luca Frittoli, Yuqi Cheng, Weiming Shen, Giacomo Boracchi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Vary: Scaling up the Vision Vocabulary for Large Vision-Language Model.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73235-5_23) · 📚 被引 47
- **作者**: Haoran Wei, Lingyu Kong, Jinyue Chen, Liang Zhao, Zheng Ge, Jinrong Yang et al.
- **🏷️ 机构**: MEGVII
- **会议**: ECCV 2024

### REVISION: Rendering Tools Enable Spatial Fidelity in Vision-Language Models.
- **链接**: [arXiv:2408.02231](https://arxiv.org/abs/2408.02231) · 📚 被引 3
- **作者**: Agneet Chatterjee, Yiran Luo, Tejas Gokhale, Yezhou Yang, Chitta Baral
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-to-Image (T2I) and multimodal large language models (MLLMs) have been adopted in solutions for several computer vision and multimodal learning tasks. However, it has been found that such vision-language models lack the ability to correctly reason over spatial relationships. To tackle this shortcoming, we develop the REVISION framework which improves spatial fidelity in vision-language models. REVISION is a 3D rendering based pipeline that generates spatially accurate synthetic images, given a textual prompt. REVISION is an extendable framework, which currently supports 100+ 3D assets, 11 spatial relationships, all with diverse camera perspectives and backgrounds. Leveraging images from REVISION as additional guidance in a training-free manner consistently improves the spatial consistency of T2I models across all spatial relationships, achieving competitive performance on the VISOR and T2I-CompBench benchmarks. We also design RevQA, a question-answering benchmark to evaluate the spatial reasoning abilities of MLLMs, and find that state-of-the-art models are not robust to complex spatial reasoning under adversarial settings. Our results and findings indicate that utilizing rendering-based frameworks is an effective approach for developing spatially-aware generative models.

</details>

### An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73004-7_2) · 📚 被引 130
- **作者**: Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Unveiling Typographic Deceptions: Insights of the Typographic Vulnerability in Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73202-7_11) · 📚 被引 9
- **作者**: Hao Cheng, Erjia Xiao, Jindong Gu, Le Yang, Jinhao Duan, Jize Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Quantized Prompt for Efficient Generalization of Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72655-2_4)
- **作者**: Tianxiang Hao, Xiaohan Ding, Juexiao Feng, Yuhong Yang, Hui Chen, Guiguang Ding
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### BlenderAlchemy: Editing 3D Graphics with Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73024-5_18) · 📚 被引 16
- **作者**: Ian Huang, Guandao Yang, Leonidas J. Guibas
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Reinforcement Learning Friendly Vision-Language Model for Minecraft.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73113-6_1) · 📚 被引 3
- **作者**: Haobin Jiang, Junpeng Yue, Hao Luo, Ziluo Ding, Zongqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### BRAVE: Broadening the Visual Encoding of Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72640-8_7) · 📚 被引 18
- **作者**: Oguzhan Fatih Kar, Alessio Tonioni, Petra Poklukar, Achin Kulshrestha, Amir Zamir, Federico Tombari
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Exploiting Semantic Reconstruction to Mitigate Hallucinations in Vision-Language Models.
- **链接**: [arXiv:2403.16167](https://arxiv.org/abs/2403.16167) · 📚 被引 4
- **作者**: Minchan Kim, Minyeong Kim, Junik Bae, Suhwan Choi, Sungkyung Kim, Buru Chang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hallucinations in vision-language models pose a significant challenge to their reliability, particularly in the generation of long captions. Current methods fall short of accurately identifying and mitigating these hallucinations. To address this issue, we introduce ESREAL, a novel unsupervised learning framework designed to suppress the generation of hallucinations through accurate localization and penalization of hallucinated tokens. Initially, ESREAL creates a reconstructed image based on the generated caption and aligns its corresponding regions with those of the original image. This semantic reconstruction aids in identifying both the presence and type of token-level hallucinations within the generated caption. Subsequently, ESREAL computes token-level hallucination scores by assessing the semantic similarity of aligned regions based on the type of hallucination. Finally, ESREAL employs a proximal policy optimization algorithm, where it selectively penalizes hallucinated tokens according to their token-level hallucination scores. Our framework notably reduces hallucinations in LLaVA, InstructBLIP, and mPLUG-Owl2 by 32.81%, 27.08%, and 7.46% on the CHAIR metric. This improvement is achieved solely through signals derived from the image itself, without the need for any image-text pairs.

</details>

### GalLoP: Learning Global and Local Prompts for Vision-Language Models.
- **链接**: [arXiv:2407.01400](https://arxiv.org/abs/2407.01400) · [代码](https://github.com/MarcLafon/gallop) · 📚 被引 32
- **作者**: Marc Lafon, Elias Ramzi, Clément Rambour, Nicolas Audebert, Nicolas Thome
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning has been widely adopted to efficiently adapt vision-language models (VLMs), e.g. CLIP, for few-shot image classification. Despite their success, most prompt learning methods trade-off between classification accuracy and robustness, e.g. in domain generalization or out-of-distribution (OOD) detection. In this work, we introduce Global-Local Prompts (GalLoP), a new prompt learning method that learns multiple diverse prompts leveraging both global and local visual features. The training of the local prompts relies on local features with an enhanced vision-text alignment. To focus only on pertinent features, this local alignment is coupled with a sparsity strategy in the selection of the local features. We enforce diversity on the set of prompts using a new ``prompt dropout'' technique and a multiscale strategy on the local prompts. GalLoP outperforms previous prompt learning methods on accuracy on eleven datasets in different few shots settings and with various backbones. Furthermore, GalLoP shows strong robustness performances in both domain generalization and OOD detection, even outperforming dedicated OOD detection methods. Code and instructions to reproduce our results: https://github.com/MarcLafon/gallop.

</details>

### ClearCLIP: Decomposing CLIP Representations for Dense Vision-Language Inference.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72970-6_9) · 📚 被引 60
- **作者**: Mengcheng Lan, Chaofeng Chen, Yiping Ke, Xinjiang Wang, Litong Feng, Wayne Zhang
- **🏷️ 机构**: CUHK / SenseTime
- **会议**: ECCV 2024

### FlexAttention for Efficient High-Resolution Vision-Language Models.
- **链接**: [arXiv:2407.20228](https://arxiv.org/abs/2407.20228) · 📚 被引 8
- **作者**: Junyan Li, Delin Chen, Tianle Cai, Peihao Chen, Yining Hong, Zhenfang Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current high-resolution vision-language models encode images as high-resolution image tokens and exhaustively take all these tokens to compute attention, which significantly increases the computational cost. To address this problem, we propose FlexAttention, a flexible attention mechanism for efficient high-resolution vision-language models. Specifically, a high-resolution image is encoded both as high-resolution tokens and low-resolution tokens, where only the low-resolution tokens and a few selected high-resolution tokens are utilized to calculate the attention map, which greatly shrinks the computational cost. The high-resolution tokens are selected via a high-resolution selection module which could retrieve tokens of relevant regions based on an input attention map. The selected high-resolution tokens are then concatenated to the low-resolution tokens and text tokens, and input to a hierarchical self-attention layer which produces an attention map that could be used for the next-step high-resolution token selection. The hierarchical self-attention process and high-resolution token selection process are performed iteratively for each attention layer. Experiments on multimodal benchmarks prove that our FlexAttention outperforms existing high-resolution VLMs (e.g., relatively ~9% in V* Bench, ~7% in TextVQA), while also significantly reducing the computational cost by nearly 40%.

</details>

### TrojVLM: Backdoor Attack Against Vision Language Models.
- **链接**: [arXiv:2409.19232](https://arxiv.org/abs/2409.19232) · 📚 被引 8
- **作者**: Weimin Lyu, Lu Pang, Tengfei Ma, Haibin Ling, Chao Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of Vision Language Models (VLMs) is a significant advancement in integrating computer vision with Large Language Models (LLMs) to produce detailed text descriptions based on visual inputs, yet it introduces new security vulnerabilities. Unlike prior work that centered on single modalities or classification tasks, this study introduces TrojVLM, the first exploration of backdoor attacks aimed at VLMs engaged in complex image-to-text generation. Specifically, TrojVLM inserts predetermined target text into output text when encountering poisoned images. Moreover, a novel semantic preserving loss is proposed to ensure the semantic integrity of the original image content. Our evaluation on image captioning and visual question answering (VQA) tasks confirms the effectiveness of TrojVLM in maintaining original semantic content while triggering specific target text outputs. This study not only uncovers a critical security risk in VLMs and image-to-text generation but also sets a foundation for future research on securing multimodal models against such sophisticated threats.

</details>

### Robust Calibration of Large Vision-Language Adapters.
- **链接**: [arXiv:2407.13588](https://arxiv.org/abs/2407.13588) · [代码](https://github.com/Bala93/CLIPCalib)
- **作者**: Balamurali Murugesan, Julio Silva-Rodríguez, Ismail Ben Ayed, Jose Dolz
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the critical issue of miscalibration in CLIP-based model adaptation, particularly in the challenging scenario of out-of-distribution (OOD) samples, which has been overlooked in the existing literature on CLIP adaptation. We empirically demonstrate that popular CLIP adaptation approaches, such as Adapters, Prompt Learning, and Test-Time Adaptation, substantially degrade the calibration capabilities of the zero-shot baseline in the presence of distributional drift. We identify the increase in logit ranges as the underlying cause of miscalibration of CLIP adaptation methods, contrasting with previous work on calibrating fully-supervised models. Motivated by these observations, we present a simple and model-agnostic solution to mitigate miscalibration, by scaling the logit range of each sample to its zero-shot prediction logits. We explore three different alternatives to achieve this, which can be either integrated during adaptation or directly used at inference time. Comprehensive experiments on popular OOD classification benchmarks demonstrate the effectiveness of the proposed approaches in mitigating miscalibration while maintaining discriminative performance, whose improvements are consistent across the three families of these increasingly popular approaches. The code is publicly available at: https://github.com/Bala93/CLIPCalib

</details>

### uCAP: An Unsupervised Prompting Method for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72904-1_25) · 📚 被引 1
- **作者**: A. Tuan Nguyen, Kai Sheng Tai, Bor-Chun Chen, Satya Narayan Shukla, Hanchao Yu, Philip Torr et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### CLIP-DPO: Vision-Language Models as a Source of Preference for Fixing Hallucinations in LVLMs.
- **链接**: [arXiv:2408.10433](https://arxiv.org/abs/2408.10433) · 📚 被引 10
- **作者**: Yassine Ouali, Adrian Bulat, Brais Martínez, Georgios Tzimiropoulos
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite recent successes, LVLMs or Large Vision Language Models are prone to hallucinating details like objects and their properties or relations, limiting their real-world deployment. To address this and improve their robustness, we present CLIP-DPO, a preference optimization method that leverages contrastively pre-trained Vision-Language (VL) embedding models, such as CLIP, for DPO-based optimization of LVLMs. Unlike prior works tackling LVLM hallucinations, our method does not rely on paid-for APIs, and does not require additional training data or the deployment of other external LVLMs. Instead, starting from the initial pool of supervised fine-tuning data, we generate a diverse set of predictions, which are ranked based on their CLIP image-text similarities, and then filtered using a robust rule-based approach to obtain a set of positive and negative pairs for DPO-based training. We applied CLIP-DPO fine-tuning to the MobileVLM-v2 family of models and to LlaVA-1.5, in all cases observing significant improvements in terms of hallucination reduction over baseline models. We also observe better performance for zero-shot classification, suggesting improved grounding capabilities, and verify that the original performance on standard LVLM benchmarks is overall preserved.

</details>

### Safe-CLIP: Removing NSFW Concepts from Vision-and-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73668-1_20) · 📚 被引 21
- **作者**: Samuele Poppi, Tobia Poppi, Federico Cocchi, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant.
- **链接**: [arXiv:2403.11299](https://arxiv.org/abs/2403.11299) · 📚 被引 6
- **作者**: Guohao Sun, Can Qin, Jiamian Wang, Zeyuan Chen, Ran Xu, Zhiqiang Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in vision-language models have shown notable generalization in broad tasks through visual instruction tuning. However, bridging the gap between the pre-trained vision encoder and the large language models (LLMs) becomes the whole network's bottleneck. To improve cross-modality alignment, existing works usually consider more visual instruction data covering a broader range of vision tasks to fine-tune the model for question-answering, which, however, is costly to obtain and has not thoroughly explored the rich contextual information contained in images. This paper first attempts to harness the overlooked context within visual instruction data, training the model to self-supervised "learning" how to ask high-quality questions. In this way, we introduce a novel framework named SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant. SQ-LLaVA exhibits proficiency in generating flexible and meaningful image-related questions while analyzing the visual clue and prior language knowledge, signifying an advanced level of generalized visual understanding. Moreover, fine-tuning SQ-LLaVA on higher-quality instruction data shows a performance improvement compared with traditional visual-instruction tuning methods. This improvement highlights the efficacy of self-questioning techniques in achieving a deeper and more nuanced comprehension of visual content across various contexts.

</details>

### Contrastive Region Guidance: Improving Grounding in Vision-Language Models Without Training.
- **链接**: [arXiv:2403.02325](https://arxiv.org/abs/2403.02325) · 📚 被引 12
- **作者**: David Wan, Jaemin Cho, Elias Stengel-Eskin, Mohit Bansal
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Highlighting particularly relevant regions of an image can improve the performance of vision-language models (VLMs) on various vision-language (VL) tasks by guiding the model to attend more closely to these regions of interest. For example, VLMs can be given a "visual prompt", where visual markers such as bounding boxes delineate key image regions. However, current VLMs that can incorporate visual guidance are either proprietary and expensive or require costly training on curated data that includes visual prompts. We introduce Contrastive Region Guidance (CRG), a training-free guidance method that enables open-source VLMs to respond to visual prompts. CRG contrasts model outputs produced with and without visual prompts, factoring out biases revealed by the model when answering without the information required to produce a correct answer (i.e., the model's prior). CRG achieves substantial improvements in a wide variety of VL tasks: When region annotations are provided, CRG increases absolute accuracy by up to 11.1% on ViP-Bench, a collection of six diverse region-based tasks such as recognition, math, and object relationship reasoning. We also show CRG's applicability to spatial reasoning, with 10% improvement on What'sUp, as well as to compositional generalization -- improving accuracy by 11.5% and 7.5% on two challenging splits from SugarCrepe -- and to image-text alignment for generated images, where we improve by up to 8.4 AUROC and 6.8 F1 points on SeeTRUE. When reference regions are absent, CRG allows us to re-rank proposed regions in referring expression comprehension and phrase grounding benchmarks like RefCOCO/+/g and Flickr30K Entities, with an average gain of 3.2% in accuracy. Our analysis explores alternative masking strategies for CRG, quantifies CRG's probability shift, and evaluates the role of region guidance strength, empirically validating CRG's design choices.

</details>

### SCLIP: Rethinking Self-Attention for Dense Vision-Language Inference.
- **链接**: [arXiv:2312.01597](https://arxiv.org/abs/2312.01597) · 📚 被引 80
- **作者**: Feng Wang, Jieru Mei, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in contrastive language-image pretraining (CLIP) have demonstrated strong capabilities in zero-shot classification by aligning visual representations with target text embeddings in an image level. However, in dense prediction tasks, CLIP often struggles to localize visual features within an image and fails to give accurate pixel-level predictions, which prevents it from functioning as a generalized visual foundation model. In this work, we aim to enhance CLIP's potential for semantic segmentation with minimal modifications to its pretrained models. By rethinking self-attention, we surprisingly find that CLIP can adapt to dense prediction tasks by simply introducing a novel Correlative Self-Attention (CSA) mechanism. Specifically, we replace the traditional self-attention block of CLIP vision encoder's last layer by our CSA module and reuse its pretrained projection matrices of query, key, and value, leading to a training-free adaptation approach for CLIP's zero-shot semantic segmentation. Extensive experiments show the advantage of CSA: we obtain a 38.2% average zero-shot mIoU across eight semantic segmentation benchmarks highlighted in this paper, significantly outperforming the existing SoTA's 33.9% and the vanilla CLIP's 14.1%.

</details>

### Cascade Prompt Learning for Vision-Language Model Adaptation.
- **链接**: [arXiv:2409.17805](https://arxiv.org/abs/2409.17805) · [代码](https://github.com/megvii-research/CasPL)
- **作者**: Ge Wu, Xin Zhang, Zheng Li, Zhaowei Chen, Jiajun Liang, Jian Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning has surfaced as an effective approach to enhance the performance of Vision-Language Models (VLMs) like CLIP when applied to downstream tasks. However, current learnable prompt tokens are primarily used for the single phase of adapting to tasks (i.e., adapting prompt), easily leading to overfitting risks. In this work, we propose a novel Cascade Prompt Learning CasPL framework to enable prompt learning to serve both generic and specific expertise (i.e., boosting and adapting prompt) simultaneously. Specifically, CasPL is a new learning paradigm comprising two distinct phases of learnable prompts: the first boosting prompt is crafted to extract domain-general knowledge from a senior larger CLIP teacher model by aligning their predicted logits using extensive unlabeled domain images. The second adapting prompt is then cascaded with the frozen first set to fine-tune the downstream tasks, following the approaches employed in prior research. In this manner, CasPL can effectively capture both domain-general and task-specific representations into explicitly different gradual groups of prompts, thus potentially alleviating overfitting issues in the target domain. It's worth noting that CasPL serves as a plug-and-play module that can seamlessly integrate into any existing prompt learning approach. CasPL achieves a significantly better balance between performance and inference speed, which is especially beneficial for deploying smaller VLM models in resource-constrained environments. Compared to the previous state-of-the-art method PromptSRC, CasPL shows an average improvement of 1.85% for base classes, 3.44% for novel classes, and 2.72% for the harmonic mean over 11 image classification datasets. Code is publicly available at: https://github.com/megvii-research/CasPL.

</details>

### Towards Real-World Adverse Weather Image Restoration: Enhancing Clearness and Semantics with Vision-Language Models.
- **链接**: [arXiv:2409.02101](https://arxiv.org/abs/2409.02101) · 📚 被引 11
- **作者**: Jiaqi Xu, Mengyang Wu, Xiaohu You, Chi-Wing Fu, Qi Dou, Pheng-Ann Heng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the limitations of adverse weather image restoration approaches trained on synthetic data when applied to real-world scenarios. We formulate a semi-supervised learning framework employing vision-language models to enhance restoration performance across diverse adverse weather conditions in real-world settings. Our approach involves assessing image clearness and providing semantics using vision-language models on real data, serving as supervision signals for training restoration models. For clearness enhancement, we use real-world data, utilizing a dual-step strategy with pseudo-labels assessed by vision-language models and weather prompt learning. For semantic enhancement, we integrate real-world data by adjusting weather conditions in vision-language model descriptions while preserving semantic meaning. Additionally, we introduce an effective training strategy to bootstrap restoration performance. Our approach achieves superior results in real-world adverse weather image restoration, demonstrated through qualitative and quantitative comparisons with state-of-the-art works.

</details>

### AddressCLIP: Empowering Vision-Language Models for City-Wide Image Address Localization.
- **链接**: [arXiv:2407.08156](https://arxiv.org/abs/2407.08156) · [代码](https://github.com/xsx1001/AddressCLIP) · 📚 被引 7
- **作者**: Shixiong Xu, Chenghao Zhang, Lubin Fan, Gaofeng Meng, Shiming Xiang, Jieping Ye
- **🏷️ 机构**:  Alibaba / Zhejiang Lab
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we introduce a new problem raised by social media and photojournalism, named Image Address Localization (IAL), which aims to predict the readable textual address where an image was taken. Existing two-stage approaches involve predicting geographical coordinates and converting them into human-readable addresses, which can lead to ambiguity and be resource-intensive. In contrast, we propose an end-to-end framework named AddressCLIP to solve the problem with more semantics, consisting of two key ingredients: i) image-text alignment to align images with addresses and scene captions by contrastive learning, and ii) image-geography matching to constrain image features with the spatial distance in terms of manifold learning. Additionally, we have built three datasets from Pittsburgh and San Francisco on different scales specifically for the IAL problem. Experiments demonstrate that our approach achieves compelling performance on the proposed datasets and outperforms representative transfer learning methods for vision-language models. Furthermore, extensive ablations and visualizations exhibit the effectiveness of the proposed method. The datasets and source code are available at https://github.com/xsx1001/AddressCLIP.

</details>

### ViGoR: Improving Visual Grounding of Large Vision Language Models with Fine-Grained Reward Modeling.
- **链接**: [arXiv:2402.06118](https://arxiv.org/abs/2402.06118) · [代码](https://github.com/amazon-science/vigor) · 📚 被引 7
- **作者**: Siming Yan, Min Bai, Weifeng Chen, Xiong Zhou, Qixing Huang, Li Erran Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> By combining natural language understanding, generation capabilities, and breadth of knowledge of large language models with image perception, recent large vision language models (LVLMs) have shown unprecedented visual reasoning capabilities. However, the generated text often suffers from inaccurate grounding in the visual input, resulting in errors such as hallucination of nonexistent scene elements, missing significant parts of the scene, and inferring incorrect attributes of and relationships between objects. To address these issues, we introduce a novel framework, ViGoR (Visual Grounding Through Fine-Grained Reward Modeling) that utilizes fine-grained reward modeling to significantly enhance the visual grounding of LVLMs over pre-trained baselines. This improvement is efficiently achieved using much cheaper human evaluations instead of full supervisions, as well as automated methods. We show the effectiveness of our approach through a variety of evaluation methods and benchmarks. Additionally, we released our human annotation (https://github.com/amazon-science/vigor) comprising 15,440 images and generated text pairs with fine-grained evaluations to contribute to related research in the community.

</details>

### BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-Language Models.
- **链接**: [arXiv:2407.13442](https://arxiv.org/abs/2407.13442) · 📚 被引 3
- **作者**: Moon Ye-Bin, Nam Hyeon-Woo, Wonseok Choi, Tae-Hyun Oh
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision language models (VLMs) perceive the world through a combination of a visual encoder and a large language model (LLM). The visual encoder, pre-trained on large-scale vision-text datasets, provides zero-shot generalization to visual data, and the LLM endows its high reasoning ability to VLMs. It leads VLMs to achieve high performance on wide benchmarks without fine-tuning, exhibiting zero or few-shot capability. However, recent studies show that VLMs are vulnerable to hallucination. This undesirable behavior degrades reliability and credibility, thereby making users unable to fully trust the output from VLMs. To enhance trustworthiness and better tackle the hallucination of VLMs, we curate a new evaluation dataset, called the BEfore-AFter hallucination dataset (BEAF), and introduce new metrics: True Understanding (TU), IGnorance (IG), StuBbornness (SB), and InDecision (ID). Unlike prior works that focus only on constructing questions and answers, the key idea of our benchmark is to manipulate visual scene information by image editing models and to design the metrics based on scene changes. This allows us to clearly assess whether VLMs correctly understand a given scene by observing the ability to perceive changes. We also visualize image-wise object relationship by virtue of our two-axis view: vision and text. Upon evaluating VLMs with our dataset, we observed that our metrics reveal different aspects of VLM hallucination that have not been reported before. Project page: \url{https://beafbench.github.io/}

</details>

### Attention Prompting on Image for Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73404-5_15) · 📚 被引 17
- **作者**: Runpeng Yu, Weihao Yu, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Adversarial Prompt Tuning for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72995-9_4)
- **作者**: Jiaming Zhang, Xingjun Ma, Xin Wang, Lingyu Qiu, Jiaqi Wang, Yu-Gang Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Reflective Instruction Tuning: Mitigating Hallucinations in Large Vision-Language Models.
- **链接**: [arXiv:2407.11422](https://arxiv.org/abs/2407.11422)
- **作者**: Jinrui Zhang, Teng Wang, Haigang Zhang, Ping Lu, Feng Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (LVLMs) have shown promising performance on a variety of vision-language tasks. However, they remain susceptible to hallucinations, generating outputs misaligned with visual content or instructions. While various mitigation strategies have been proposed, they often neglect a key contributor to hallucinations: lack of fine-grained reasoning supervision during training. Without intermediate reasoning steps, models may establish superficial shortcuts between instructions and responses, failing to internalize the inherent reasoning logic. To address this challenge, we propose reflective instruction tuning, which integrates rationale learning into visual instruction tuning. Unlike previous methods that learning from responses only, our approach entails the model predicting rationales justifying why responses are correct or incorrect. This fosters a deeper engagement with the fine-grained reasoning underlying each response, thus enhancing the model's reasoning proficiency. To facilitate this approach, we propose REVERIE, the first large-scale instruction-tuning dataset with ReflEctiVE RatIonalE annotations. REVERIE comprises 115k machine-generated reasoning instructions, each meticulously annotated with a corresponding pair of correct and confusing responses, alongside comprehensive rationales elucidating the justification behind the correctness or erroneousness of each response. Experimental results on multiple LVLM benchmarks reveal that reflective instruction tuning with the REVERIE dataset yields noticeable performance gain over the baseline model, demonstrating the effectiveness of reflecting from the rationales. Project page is at https://zjr2000.github.io/projects/reverie.

</details>

### Conceptual Codebook Learning for Vision-Language Models.
- **链接**: [arXiv:2407.02350](https://arxiv.org/abs/2407.02350) · 📚 被引 7
- **作者**: Yi Zhang, Ke Yu, Siqi Wu, Zhihai He
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose Conceptual Codebook Learning (CoCoLe), a novel fine-tuning method for vision-language models (VLMs) to address the challenge of improving the generalization capability of VLMs while fine-tuning them on downstream tasks in a few-shot setting. We recognize that visual concepts, such as textures, shapes, and colors are naturally transferable across domains and play a crucial role in generalization tasks. Motivated by this interesting finding, we learn a conceptual codebook consisting of visual concepts as keys and conceptual prompts as values, which serves as a link between the image encoder's outputs and the text encoder's inputs. Specifically, for a given image, we leverage the codebook to identify the most relevant conceptual prompts associated with the class embeddings to perform the classification. Additionally, we incorporate a handcrafted concept cache as a regularization to alleviate the overfitting issues in low-shot scenarios. We observe that this conceptual codebook learning method is able to achieve enhanced alignment between visual and linguistic modalities. Extensive experimental results demonstrate that our CoCoLe method remarkably outperforms the existing state-of-the-art methods across various evaluation settings, including base-to-new generalization, cross-dataset evaluation, and domain generalization tasks. Detailed ablation studies further confirm the efficacy of each component in CoCoLe.

</details>

### LAPT: Label-Driven Automated Prompt Tuning for OOD Detection with Vision-Language Models.
- **链接**: [arXiv:2407.08966](https://arxiv.org/abs/2407.08966) · [代码](https://github.com/YBZh/LAPT) · 📚 被引 11
- **作者**: Yabin Zhang, Wenjie Zhu, Chenhang He, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection is crucial for model reliability, as it identifies samples from unknown classes and reduces errors due to unexpected inputs. Vision-Language Models (VLMs) such as CLIP are emerging as powerful tools for OOD detection by integrating multi-modal information. However, the practical application of such systems is challenged by manual prompt engineering, which demands domain expertise and is sensitive to linguistic nuances. In this paper, we introduce Label-driven Automated Prompt Tuning (LAPT), a novel approach to OOD detection that reduces the need for manual prompt engineering. We develop distribution-aware prompts with in-distribution (ID) class names and negative labels mined automatically. Training samples linked to these class labels are collected autonomously via image synthesis and retrieval methods, allowing for prompt learning without manual effort. We utilize a simple cross-entropy loss for prompt optimization, with cross-modal and cross-distribution mixing strategies to reduce image noise and explore the intermediate space between distributions, respectively. The LAPT framework operates autonomously, requiring only ID class names as input and eliminating the need for manual intervention. With extensive experiments, LAPT consistently outperforms manually crafted prompts, setting a new standard for OOD detection. Moreover, LAPT not only enhances the distinction between ID and OOD samples, but also improves the ID classification accuracy and strengthens the generalization robustness to covariate shifts, resulting in outstanding performance in challenging full-spectrum OOD detection tasks. Codes are available at \url{https://github.com/YBZh/LAPT}.

</details>

### Training A Small Emotional Vision Language Model for Visual Art Comprehension.
- **链接**: [arXiv:2403.11150](https://arxiv.org/abs/2403.11150) · [代码](https://github.com/BetterZH/SEVLM-code) · 📚 被引 8
- **作者**: Jing Zhang, Liang Zheng, Meng Wang, Dan Guo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper develops small vision language models to understand visual art, which, given an art work, aims to identify its emotion category and explain this prediction with natural language. While small models are computationally efficient, their capacity is much limited compared with large models. To break this trade-off, this paper builds a small emotional vision language model (SEVLM) by emotion modeling and input-output feature alignment. On the one hand, based on valence-arousal-dominance (VAD) knowledge annotated by psychology experts, we introduce and fuse emotional features derived through VAD dictionary and a VAD head to align VAD vectors of predicted emotion explanation and the ground truth. This allows the vision language model to better understand and generate emotional texts, compared with using traditional text embeddings alone. On the other hand, we design a contrastive head to pull close embeddings of the image, its emotion class, and explanation, which aligns model outputs and inputs. On two public affective explanation datasets, we show that the proposed techniques consistently improve the visual art understanding performance of baseline SEVLMs. Importantly, the proposed model can be trained and evaluated on a single RTX 2080 Ti while exhibiting very strong performance: it not only outperforms the state-of-the-art small models but is also competitive compared with LLaVA 7B after fine-tuning and GPT4(V). The code is available at https://github.com/BetterZH/SEVLM-code.

</details>

### The First to Know: How Token Distributions Reveal Hidden Knowledge in Large Vision-Language Models?
- **链接**: [arXiv:2403.09037](https://arxiv.org/abs/2403.09037) · 📚 被引 8
- **作者**: Qinyu Zhao, Ming Xu, Kartik Gupta, Akshay Asthana, Liang Zheng, Stephen Gould
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (LVLMs), designed to interpret and respond to human instructions, occasionally generate hallucinated or harmful content due to inappropriate instructions. This study uses linear probing to shed light on the hidden knowledge at the output layers of LVLMs. We demonstrate that the logit distributions of the first tokens contain sufficient information to determine whether to respond to the instructions, including recognizing unanswerable visual questions, defending against jailbreaking attacks, and identifying deceptive questions. Such hidden knowledge is gradually lost in logits of subsequent tokens during response generation. Then, we illustrate a simple decoding strategy at the generation of the first token, effectively improving the generated content. In experiments, we find a few interesting insights: First, the CLIP model already contains a strong signal for solving these tasks, which indicates potential bias in the existing datasets. Second, we observe performance improvement by utilizing the first logit distributions on three additional tasks, including indicating uncertainty in math solving, mitigating hallucination, and image classification. Last, with the same training data, simply finetuning LVLMs improves models' performance but is still inferior to linear probing on these tasks.

</details>

### Adapt Without Forgetting: Distill Proximity from Dual Teachers in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72949-2_7) · 📚 被引 3
- **作者**: Mengyu Zheng, Yehui Tang, Zhiwei Hao, Kai Han, Yunhe Wang, Chang Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models.
- **链接**: [arXiv:2407.12366](https://arxiv.org/abs/2407.12366) · 📚 被引 56
- **作者**: Gengze Zhou, Yicong Hong, Zun Wang, Xin Eric Wang, Qi Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Capitalizing on the remarkable advancements in Large Language Models (LLMs), there is a burgeoning initiative to harness LLMs for instruction following robotic navigation. Such a trend underscores the potential of LLMs to generalize navigational reasoning and diverse language understanding. However, a significant discrepancy in agent performance is observed when integrating LLMs in the Vision-and-Language navigation (VLN) tasks compared to previous downstream specialist models. Furthermore, the inherent capacity of language to interpret and facilitate communication in agent interactions is often underutilized in these integrations. In this work, we strive to bridge the divide between VLN-specialized models and LLM-based navigation paradigms, while maintaining the interpretative prowess of LLMs in generating linguistic navigational reasoning. By aligning visual content in a frozen LLM, we encompass visual observation comprehension for LLMs and exploit a way to incorporate LLMs and navigation policy networks for effective action predictions and navigational reasoning. We demonstrate the data efficiency of the proposed methods and eliminate the gap between LM-based agents and state-of-the-art VLN specialists.

</details>

### DreamDiffusion: High-Quality EEG-to-Image Generation with Temporal Masked Signal Modeling and CLIP Alignment.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72751-1_27) · 📚 被引 11
- **作者**: Yunpeng Bai, Xintao Wang, Yan-Pei Cao, Yixiao Ge, Chun Yuan, Ying Shan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### TTD: Text-Tag Self-Distillation Enhancing Image-Text Alignment in CLIP to Alleviate Single Tag Bias.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73004-7_20) · 📚 被引 4
- **作者**: Sanghyun Jo, Soohyun Ryu, Sungyub Kim, Eunho Yang, Kyungsu Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

## 跨领域论文（完整笔记在其他领域）

- AutoEval-Video: An Automatic Benchmark for Assessing Large Vision Language Models in Open-Ended Video Question Answering. → [video-understanding](../video-understanding/Guideline%202024.md)
- MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning. → [object-detection](../object-detection/Guideline%202024.md)
- IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models. → [network-pruning](../network-pruning/Guideline%202024.md)
- Open-Set Recognition in the Age of Vision-Language Models. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Mind the Interference: Retaining Pre-trained Knowledge in Parameter Efficient Continual Learning of Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- Select and Distill: Selective Dual-Teacher Knowledge Transfer for Continual Learning on Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- BLINK: Multimodal Large Language Models Can See but Not Perceive. → [multimodal](../multimodal/Guideline%202024.md)
- Eyes Closed, Safety on: Protecting Multimodal LLMs via Image-to-Text Transformation. → [multimodal](../multimodal/Guideline%202024.md)
- Images are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents. → [multimodal](../multimodal/Guideline%202024.md)
- Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MM1: Methods, Analysis and Insights from Multimodal LLM Pre-training. → [multimodal](../multimodal/Guideline%202024.md)
- Strengthening Multimodal Large Language Model with Bootstrapped Preference Optimization. → [multimodal](../multimodal/Guideline%202024.md)
- MoMA: Multimodal LLM Adapter for Fast Personalized Image Generation. → [multimodal](../multimodal/Guideline%202024.md)
- Instruction Tuning-Free Visual Token Complement for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- AdaShield : Safeguarding Multimodal Large Language Models from Structure-Based Attack via Adaptive Shield Prompting. → [multimodal](../multimodal/Guideline%202024.md)
- A Comprehensive Study of Multimodal Large Language Models for Image Quality Assessment. → [multimodal](../multimodal/Guideline%202024.md)
- LLMGA: Multimodal Large Language Model Based Generation Assistant. → [multimodal](../multimodal/Guideline%202024.md)
- CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios. → [multimodal](../multimodal/Guideline%202024.md)
- Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Merlin: Empowering Multimodal LLMs with Foresight Minds. → [multimodal](../multimodal/Guideline%202024.md)
- FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- LLaVA-Grounding: Grounded Visual Chat with Large Multimodal Models. → [multimodal](../multimodal/Guideline%202024.md)
- GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator. → [multimodal](../multimodal/Guideline%202024.md)
- UniCode: Learning a Unified Codebook for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Class-Incremental Learning with CLIP: Adaptive Representation Adjustment and Parameter Fusion. → [continual-learning](../continual-learning/Guideline%202024.md)
