# VLM — 2024 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UMG-CLIP: A Unified Multi-granularity Vision Generalist for Open-World Understanding.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72920-1_15) · 📚 被引 2
- **作者**: Bowen Shi, Peisen Zhao, Zichen Wang, Yuhang Zhang, Yaoming Wang, Jin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-to-Image (T2I) and multimodal large language models (MLLMs) have been adopted in solutions for several computer vision and multimodal learning tasks. However, it has been found that such vision-language models lack the ability to correctly reason over spatial relationships. To tackle this shortcoming, we develop the REVISION framework which improves spatial fidelity in vision-language models. REVISION is a 3D rendering based pipeline that generates spatially accurate synthetic images, given a textual prompt. REVISION is an extendable framework, which currently supports 100+ 3D assets, 11 spatial relationships, all with diverse camera perspectives and backgrounds. Leveraging images from REVISION as additional guidance in a training-free manner consistently improves the spatial consistency of T2I models across all spatial relationships, achieving competitive performance on the VISOR and T2I-CompBench benchmarks. We also design RevQA, a question-answering benchmark to evaluate the spatial reasoning abilities of MLLMs, and find that state-of-the-art models are not robust to complex spatial reasoning under adversarial settings. Our results and findings indicate that utilizing rendering-based frameworks is an effective approach for developing spatially-aware generative models.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hallucinations in vision-language models pose a significant challenge to their reliability, particularly in the generation of long captions. Current methods fall short of accurately identifying and mitigating these hallucinations. To address this issue, we introduce ESREAL, a novel unsupervised learning framework designed to suppress the generation of hallucinations through accurate localization and penalization of hallucinated tokens. Initially, ESREAL creates a reconstructed image based on the generated caption and aligns its corresponding regions with those of the original image. This semantic reconstruction aids in identifying both the presence and type of token-level hallucinations within the generated caption. Subsequently, ESREAL computes token-level hallucination scores by assessing the semantic similarity of aligned regions based on the type of hallucination. Finally, ESREAL employs a proximal policy optimization algorithm, where it selectively penalizes hallucinated tokens according to their token-level hallucination scores. Our framework notably reduces hallucinations in LLaVA, InstructBLIP, and mPLUG-Owl2 by 32.81%, 27.08%, and 7.46% on the CHAIR metric. This improvement is achieved solely through signals derived from the image itself, without the need for any image-text pairs.

</details>

### CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/fde7f40f8ced5735006810534dc66b33-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 18
- **作者**: Peng Xia, Ze Chen, Juanxi Tian, Yangrui Gong, Ruibo Hou, Yue Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning has been widely adopted to efficiently adapt vision-language models (VLMs), e.g. CLIP, for few-shot image classification. Despite their success, most prompt learning methods trade-off between classification accuracy and robustness, e.g. in domain generalization or out-of-distribution (OOD) detection. In this work, we introduce Global-Local Prompts (GalLoP), a new prompt learning method that learns multiple diverse prompts leveraging both global and local visual features. The training of the local prompts relies on local features with an enhanced vision-text alignment. To focus only on pertinent features, this local alignment is coupled with a sparsity strategy in the selection of the local features. We enforce diversity on the set of prompts using a new ``prompt dropout'' technique and a multiscale strategy on the local prompts. GalLoP outperforms previous prompt learning methods on accuracy on eleven datasets in different few shots settings and with various backbones. Furthermore, GalLoP shows strong robustness performances in both domain generalization and OOD detection, even outperforming dedicated OOD detection methods. Code and instructions to reproduce our results: https://github.com/MarcLafon/gallop.

</details>

> Medical Vision-Language Pretraining (MedVLP) shows promise in learning generalizable and transferable visual representations from paired and unpaired medical images and reports. MedVLP can provide useful features to downstream tasks and facilitate adapting task-specific models to new setups using fewer examples. However, existing MedVLP methods often differ in terms of datasets, preprocessing, and finetuning implementations. This pose great challenges in evaluating how well a MedVLP method generalizes to various clinically-relevant tasks due to the lack of unified, standardized, and comprehensive benchmark. To fill this gap, we propose BenchX, a unified benchmark framework that enables head-to-head comparison and systematical analysis between MedVLP methods using public chest X-ray datasets. Specifically, BenchX is composed of three components: 1) Comprehensive datasets covering nine datasets and four medical tasks; 2) Benchmark suites to standardize data preprocessing, train-test splits, and parameter selection; 3) Unified finetuning protocols that accommodate heterogeneous MedVLP methods for consistent task adaptation in classification, segmentation, and report generation, respectively. Utilizing BenchX, we establish baselines for nine state-of-the-art MedVLP methods and found that the performance of some early MedVLP methods can be enhanced to surpass more recent ones, prompting a revisiting of the developments and conclusions from prior works in MedVLP. Our code are available at https://github.com/yangzhou12/BenchX.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current high-resolution vision-language models encode images as high-resolution image tokens and exhaustively take all these tokens to compute attention, which significantly increases the computational cost. To address this problem, we propose FlexAttention, a flexible attention mechanism for efficient high-resolution vision-language models. Specifically, a high-resolution image is encoded both as high-resolution tokens and low-resolution tokens, where only the low-resolution tokens and a few selected high-resolution tokens are utilized to calculate the attention map, which greatly shrinks the computational cost. The high-resolution tokens are selected via a high-resolution selection module which could retrieve tokens of relevant regions based on an input attention map. The selected high-resolution tokens are then concatenated to the low-resolution tokens and text tokens, and input to a hierarchical self-attention layer which produces an attention map that could be used for the next-step high-resolution token selection. The hierarchical self-attention process and high-resolution token selection process are performed iteratively for each attention layer. Experiments on multimodal benchmarks prove that our FlexAttention outperforms existing high-resolution VLMs (e.g., relatively ~9% in V* Bench, ~7% in TextVQA), while also significantly reducing the computational cost by nearly 40%.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting Human-Object Interactions (HOI) in zero-shot settings, where models must handle unseen classes, poses significant challenges. Existing methods that rely on aligning visual encoders with large Vision-Language Models (VLMs) to tap into the extensive knowledge of VLMs, require large, computationally expensive models and encounter training difficulties. Adapting VLMs with prompt learning offers an alternative to direct alignment. However, fine-tuning on task-specific datasets often leads to overfitting to seen classes and suboptimal performance on unseen classes, due to the absence of unseen class labels. To address these challenges, we introduce a novel prompt learning-based framework for Efficient Zero-Shot HOI detection (EZ-HOI). First, we introduce Large Language Model (LLM) and VLM guidance for learnable prompts, integrating detailed HOI descriptions and visual semantics to adapt VLMs to HOI tasks. However, because training datasets contain seen-class labels alone, fine-tuning VLMs on such datasets tends to optimize learnable prompts for seen classes instead of unseen ones. Therefore, we design prompt learning for unseen classes using information from related seen classes, with LLMs utilized to highlight the differences between unseen and related seen classes. Quantitative evaluations on benchmark datasets demonstrate that our EZ-HOI achieves state-of-the-art performance across various zero-shot settings with only 10.35% to 33.95% of the trainable parameters compared to existing methods. Code is available at https://github.com/ChelsieLei/EZ-HOI.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of Vision Language Models (VLMs) is a significant advancement in integrating computer vision with Large Language Models (LLMs) to produce detailed text descriptions based on visual inputs, yet it introduces new security vulnerabilities. Unlike prior work that centered on single modalities or classification tasks, this study introduces TrojVLM, the first exploration of backdoor attacks aimed at VLMs engaged in complex image-to-text generation. Specifically, TrojVLM inserts predetermined target text into output text when encountering poisoned images. Moreover, a novel semantic preserving loss is proposed to ensure the semantic integrity of the original image content. Our evaluation on image captioning and visual question answering (VQA) tasks confirms the effectiveness of TrojVLM in maintaining original semantic content while triggering specific target text outputs. This study not only uncovers a critical security risk in VLMs and image-to-text generation but also sets a foundation for future research on securing multimodal models against such sophisticated threats.

</details>

### Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models.
- **链接**: [arXiv:2410.21802](https://arxiv.org/abs/2410.21802) · [代码](https://github.com/zhyblue424/TGA-ZSR) · 📚 被引 2
- **作者**: Lu Yu, Haiyang Zhang, Changsheng Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper addresses the critical issue of miscalibration in CLIP-based model adaptation, particularly in the challenging scenario of out-of-distribution (OOD) samples, which has been overlooked in the existing literature on CLIP adaptation. We empirically demonstrate that popular CLIP adaptation approaches, such as Adapters, Prompt Learning, and Test-Time Adaptation, substantially degrade the calibration capabilities of the zero-shot baseline in the presence of distributional drift. We identify the increase in logit ranges as the underlying cause of miscalibration of CLIP adaptation methods, contrasting with previous work on calibrating fully-supervised models. Motivated by these observations, we present a simple and model-agnostic solution to mitigate miscalibration, by scaling the logit range of each sample to its zero-shot prediction logits. We explore three different alternatives to achieve this, which can be either integrated during adaptation or directly used at inference time. Comprehensive experiments on popular OOD classification benchmarks demonstrate the effectiveness of the proposed approaches in mitigating miscalibration while maintaining discriminative performance, whose improvements are consistent across the three families of these increasingly popular approaches. The code is publicly available at: https://github.com/Bala93/CLIPCalib

</details>

### Matryoshka Query Transformer for Large Vision-Language Models.
- **链接**: [arXiv:2405.19315](https://arxiv.org/abs/2405.19315) · 📚 被引 5
- **作者**: Wenbo Hu, Zi-Yi Dou, Liunian Harold Li, Amita Kamath, Nanyun Peng, Kai-Wei Chang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite recent successes, LVLMs or Large Vision Language Models are prone to hallucinating details like objects and their properties or relations, limiting their real-world deployment. To address this and improve their robustness, we present CLIP-DPO, a preference optimization method that leverages contrastively pre-trained Vision-Language (VL) embedding models, such as CLIP, for DPO-based optimization of LVLMs. Unlike prior works tackling LVLM hallucinations, our method does not rely on paid-for APIs, and does not require additional training data or the deployment of other external LVLMs. Instead, starting from the initial pool of supervised fine-tuning data, we generate a diverse set of predictions, which are ranked based on their CLIP image-text similarities, and then filtered using a robust rule-based approach to obtain a set of positive and negative pairs for DPO-based training. We applied CLIP-DPO fine-tuning to the MobileVLM-v2 family of models and to LlaVA-1.5, in all cases observing significant improvements in terms of hallucination reduction over baseline models. We also observe better performance for zero-shot classification, suggesting improved grounding capabilities, and verify that the original performance on standard LVLM benchmarks is overall preserved.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in vision-language models have shown notable generalization in broad tasks through visual instruction tuning. However, bridging the gap between the pre-trained vision encoder and the large language models (LLMs) becomes the whole network's bottleneck. To improve cross-modality alignment, existing works usually consider more visual instruction data covering a broader range of vision tasks to fine-tune the model for question-answering, which, however, is costly to obtain and has not thoroughly explored the rich contextual information contained in images. This paper first attempts to harness the overlooked context within visual instruction data, training the model to self-supervised "learning" how to ask high-quality questions. In this way, we introduce a novel framework named SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant. SQ-LLaVA exhibits proficiency in generating flexible and meaningful image-related questions while analyzing the visual clue and prior language knowledge, signifying an advanced level of generalized visual understanding. Moreover, fine-tuning SQ-LLaVA on higher-quality instruction data shows a performance improvement compared with traditional visual-instruction tuning methods. This improvement highlights the efficacy of self-questioning techniques in achieving a deeper and more nuanced comprehension of visual content across various contexts.

</details>

> Test-time adaptation, which enables models to generalize to diverse data with unlabeled test samples, holds significant value in real-world scenarios. Recently, researchers have applied this setting to advanced pre-trained vision-language models (VLMs), developing approaches such as test-time prompt tuning to further extend their practical applicability. However, these methods typically focus solely on adapting VLMs from a single modality and fail to accumulate task-specific knowledge as more samples are processed. To address this, we introduce Dual Prototype Evolving (DPE), a novel test-time adaptation approach for VLMs that effectively accumulates task-specific knowledge from multi-modalities. Specifically, we create and evolve two sets of prototypes--textual and visual--to progressively capture more accurate multi-modal representations for target classes during test time. Moreover, to promote consistent multi-modal representations, we introduce and optimize learnable residuals for each test sample to align the prototypes from both modalities. Extensive experimental results on 15 benchmark datasets demonstrate that our proposed DPE consistently outperforms previous state-of-the-art methods while also exhibiting competitive computational efficiency. Code is available at https://github.com/zhangce01/DPE-CLIP.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Highlighting particularly relevant regions of an image can improve the performance of vision-language models (VLMs) on various vision-language (VL) tasks by guiding the model to attend more closely to these regions of interest. For example, VLMs can be given a "visual prompt", where visual markers such as bounding boxes delineate key image regions. However, current VLMs that can incorporate visual guidance are either proprietary and expensive or require costly training on curated data that includes visual prompts. We introduce Contrastive Region Guidance (CRG), a training-free guidance method that enables open-source VLMs to respond to visual prompts. CRG contrasts model outputs produced with and without visual prompts, factoring out biases revealed by the model when answering without the information required to produce a correct answer (i.e., the model's prior). CRG achieves substantial improvements in a wide variety of VL tasks: When region annotations are provided, CRG increases absolute accuracy by up to 11.1% on ViP-Bench, a collection of six diverse region-based tasks such as recognition, math, and object relationship reasoning. We also show CRG's applicability to spatial reasoning, with 10% improvement on What'sUp, as well as to compositional generalization -- improving accuracy by 11.5% and 7.5% on two challenging splits from SugarCrepe -- and to image-text alignment for generated images, where we improve by up to 8.4 AUROC and 6.8 F1 points on SeeTRUE. When reference regions are absent, CRG allows us to re-rank proposed regions in referring expression comprehension and phrase grounding benchmarks like RefCOCO/+/g and Flickr30K Entities, with an average gain of 3.2% in accuracy. Our analysis explores alternative masking strategies for CRG, quantifies CRG's probability shift, and evaluates the role of region guidance strength, empirically validating CRG's design choices.

</details>

### Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem.
- **链接**: [arXiv:2411.00238](https://arxiv.org/abs/2411.00238) · 📚 被引 16
- **作者**: Declan Campbell, Sunayana Rane, Tyler Giallanza, Nicolò De Sabbata, Kia Ghods, Amogh Joshi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in contrastive language-image pretraining (CLIP) have demonstrated strong capabilities in zero-shot classification by aligning visual representations with target text embeddings in an image level. However, in dense prediction tasks, CLIP often struggles to localize visual features within an image and fails to give accurate pixel-level predictions, which prevents it from functioning as a generalized visual foundation model. In this work, we aim to enhance CLIP's potential for semantic segmentation with minimal modifications to its pretrained models. By rethinking self-attention, we surprisingly find that CLIP can adapt to dense prediction tasks by simply introducing a novel Correlative Self-Attention (CSA) mechanism. Specifically, we replace the traditional self-attention block of CLIP vision encoder's last layer by our CSA module and reuse its pretrained projection matrices of query, key, and value, leading to a training-free adaptation approach for CLIP's zero-shot semantic segmentation. Extensive experiments show the advantage of CSA: we obtain a 38.2% average zero-shot mIoU across eight semantic segmentation benchmarks highlighted in this paper, significantly outperforming the existing SoTA's 33.9% and the vanilla CLIP's 14.1%.

</details>

### VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions.
- **链接**: [arXiv:2410.20927](https://arxiv.org/abs/2410.20927) · 📚 被引 6
- **作者**: Guangyan Chen, Meiling Wang, Te Cui, Yao Mu, Haoyang Lu, Tianxing Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual imitation learning (VIL) provides an efficient and intuitive strategy for robotic systems to acquire novel skills. Recent advancements in Vision Language Models (VLMs) have demonstrated remarkable performance in vision and language reasoning capabilities for VIL tasks. Despite the progress, current VIL methods naively employ VLMs to learn high-level plans from human videos, relying on pre-defined motion primitives for executing physical interactions, which remains a major bottleneck. In this work, we present VLMimic, a novel paradigm that harnesses VLMs to directly learn even fine-grained action levels, only given a limited number of human videos. Specifically, VLMimic first grounds object-centric movements from human videos, and learns skills using hierarchical constraint representations, facilitating the derivation of skills with fine-grained action levels from limited human videos. These skills are refined and updated through an iterative comparison strategy, enabling efficient adaptation to unseen environments. Our extensive experiments exhibit that our VLMimic, using only 5 human videos, yields significant improvements of over 27% and 21% in RLBench and real-world manipulation tasks, and surpasses baselines by over 37% in long-horizon tasks.

</details>

### Conjugated Semantic Pool Improves OOD Detection with Pre-trained Vision-Language Models.
- **链接**: [arXiv:2410.08611](https://arxiv.org/abs/2410.08611) · [代码](https://github.com/MengyuanChen21/NeurIPS2024-CSP) · 📚 被引 8
- **作者**: Mengyuan Chen, Junyu Gao, Changsheng Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A straightforward pipeline for zero-shot out-of-distribution (OOD) detection involves selecting potential OOD labels from an extensive semantic pool and then leveraging a pre-trained vision-language model to perform classification on both in-distribution (ID) and OOD labels. In this paper, we theorize that enhancing performance requires expanding the semantic pool, while increasing the expected probability of selected OOD labels being activated by OOD samples, and ensuring low mutual dependence among the activations of these OOD labels. A natural expansion manner is to adopt a larger lexicon; however, the inevitable introduction of numerous synonyms and uncommon words fails to meet the above requirements, indicating that viable expansion manners move beyond merely selecting words from a lexicon. Since OOD detection aims to correctly classify input images into ID/OOD class groups, we can "make up" OOD label candidates which are not standard class names but beneficial for the process. Observing that the original semantic pool is comprised of unmodified specific class names, we correspondingly construct a conjugated semantic pool (CSP) consisting of modified superclass names, each serving as a cluster center for samples sharing similar properties across different categories. Consistent with our established theory, expanding OOD label candidates with the CSP satisfies the requirements and outperforms existing works by 7.89% in FPR95. Codes are available in https://github.com/MengyuanChen21/NeurIPS2024-CSP.

</details>

### Are We on the Right Way for Evaluating Large Vision-Language Models?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/2f8ee6a3d766b426d2618e555b5aeb39-Abstract-Conference.html) · 📚 被引 92
- **作者**: Lin Chen, Jinsong Li, Xiaoyi Dong, Pan Zhang, Yuhang Zang, Zehui Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Multi-Object Hallucination in Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/4ea4a1ea4d9ff273688c8e92bd087112-Abstract-Conference.html) · 📚 被引 8
- **作者**: Xuweiyi Chen, Ziqiao Ma, Xuejun Zhang, Sihan Xu, Shengyi Qian, Jianing Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### SpatialRGPT: Grounded Spatial Reasoning in Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/f38cb4cf9a5eaa92b3cfa481832719c6-Abstract-Conference.html) · 📚 被引 86
- **作者**: An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Enhancing Large Vision Language Models with Self-Training on Image Comprehension.
- **链接**: [arXiv:2405.19716](https://arxiv.org/abs/2405.19716) · 📚 被引 6
- **作者**: Yihe Deng, Pan Lu, Fan Yin, Ziniu Hu, Sheng Shen, Quanquan Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision language models (LVLMs) integrate large language models (LLMs) with pre-trained vision encoders, thereby activating the perception capability of the model to understand image inputs for different queries and conduct subsequent reasoning. Improving this capability requires high-quality vision-language data, which is costly and labor-intensive to acquire. Self-training approaches have been effective in single-modal settings to alleviate the need for labeled data by leveraging model's own generation. However, effective self-training remains a challenge regarding the unique visual perception and reasoning capability of LVLMs. To address this, we introduce Self-Training on Image Comprehension (STIC), which emphasizes a self-training approach specifically for image comprehension. First, the model self-constructs a preference dataset for image descriptions using unlabeled images. Preferred responses are generated through a step-by-step prompt, while dis-preferred responses are generated from either corrupted images or misleading prompts. To further self-improve reasoning on the extracted visual information, we let the model reuse a small portion of existing instruction-tuning data and append its self-generated image descriptions to the prompts. We validate the effectiveness of STIC across seven different benchmarks, demonstrating substantial performance gains of 4.0% on average while using 70% less supervised fine-tuning data than the current method. Further studies investigate various components of STIC and highlight its potential to leverage vast quantities of unlabeled images for self-training. Code and data are made publicly available.

</details>

### Unveiling Encoder-Free Vision-Language Models.
- **链接**: [arXiv:2406.11832](https://arxiv.org/abs/2406.11832) · [代码](https://github.com/baaivision/EVE) · 📚 被引 5
- **作者**: Haiwen Diao, Yufeng Cui, Xiaotong Li, Yueze Wang, Huchuan Lu, Xinlong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing vision-language models (VLMs) mostly rely on vision encoders to extract visual features followed by large language models (LLMs) for visual-language tasks. However, the vision encoders set a strong inductive bias in abstracting visual representation, e.g., resolution, aspect ratio, and semantic priors, which could impede the flexibility and efficiency of the VLMs. Training pure VLMs that accept the seamless vision and language inputs, i.e., without vision encoders, remains challenging and rarely explored. Empirical observations reveal that direct training without encoders results in slow convergence and large performance gaps. In this work, we bridge the gap between encoder-based and encoder-free models, and present a simple yet effective training recipe towards pure VLMs. Specifically, we unveil the key aspects of training encoder-free VLMs efficiently via thorough experiments: (1) Bridging vision-language representation inside one unified decoder; (2) Enhancing visual recognition capability via extra supervision. With these strategies, we launch EVE, an encoder-free vision-language model that can be trained and forwarded efficiently. Notably, solely utilizing 35M publicly accessible data, EVE can impressively rival the encoder-based VLMs of similar capacities across multiple vision-language benchmarks. It significantly outperforms the counterpart Fuyu-8B with mysterious training procedures and undisclosed training data. We believe that EVE provides a transparent and efficient route for developing a pure decoder-only architecture across modalities. Our code and models are publicly available at: https://github.com/baaivision/EVE.

</details>

### InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD.
- **链接**: [arXiv:2404.06512](https://arxiv.org/abs/2404.06512) · [代码](https://github.com/InternLM/InternLM-XComposer) · 📚 被引 12
- **作者**: Xiaoyi Dong, Pan Zhang, Yuhang Zang, Yuhang Cao, Bin Wang, Linke Ouyang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Large Vision-Language Model (LVLM) field has seen significant advancements, yet its progression has been hindered by challenges in comprehending fine-grained visual content due to limited resolution. Recent efforts have aimed to enhance the high-resolution understanding capabilities of LVLMs, yet they remain capped at approximately 1500 x 1500 pixels and constrained to a relatively narrow resolution range. This paper represents InternLM-XComposer2-4KHD, a groundbreaking exploration into elevating LVLM resolution capabilities up to 4K HD (3840 x 1600) and beyond. Concurrently, considering the ultra-high resolution may not be necessary in all scenarios, it supports a wide range of diverse resolutions from 336 pixels to 4K standard, significantly broadening its scope of applicability. Specifically, this research advances the patch division paradigm by introducing a novel extension: dynamic resolution with automatic patch configuration. It maintains the training image aspect ratios while automatically varying patch counts and configuring layouts based on a pre-trained Vision Transformer (ViT) (336 x 336), leading to dynamic training resolution from 336 pixels to 4K standard. Our research demonstrates that scaling training resolution up to 4K HD leads to consistent performance enhancements without hitting the ceiling of potential improvements. InternLM-XComposer2-4KHD shows superb capability that matches or even surpasses GPT-4V and Gemini Pro in 10 of the 16 benchmarks. The InternLM-XComposer2-4KHD model series with 7B parameters are publicly available at https://github.com/InternLM/InternLM-XComposer.

</details>

### IPO: Interpretable Prompt Optimization for Vision-Language Models.
- **链接**: [arXiv:2410.15397](https://arxiv.org/abs/2410.15397) · 📚 被引 7
- **作者**: Yingjun Du, Wenfang Sun, Cees Snoek
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models like CLIP have remarkably adapted to various downstream tasks. Nonetheless, their performance heavily depends on the specificity of the input text prompts, which requires skillful prompt template engineering. Instead, current approaches to prompt optimization learn the prompts through gradient descent, where the prompts are treated as adjustable parameters. However, these methods tend to lead to overfitting of the base classes seen during training and produce prompts that are no longer understandable by humans. This paper introduces a simple but interpretable prompt optimizer (IPO), that utilizes large language models (LLMs) to generate textual prompts dynamically. We introduce a Prompt Optimization Prompt that not only guides LLMs in creating effective prompts but also stores past prompts with their performance metrics, providing rich in-context information. Additionally, we incorporate a large multimodal model (LMM) to condition on visual content by generating image descriptions, which enhance the interaction between textual and visual modalities. This allows for thae creation of dataset-specific prompts that improve generalization performance, while maintaining human comprehension. Extensive testing across 11 datasets reveals that IPO not only improves the accuracy of existing gradient-descent-based prompt learning methods but also considerably enhances the interpretability of the generated prompts. By leveraging the strengths of LLMs, our approach ensures that the prompts remain human-understandable, thereby facilitating better transparency and oversight for vision-language models.

</details>

### SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations.
- **链接**: [arXiv:2406.11171](https://arxiv.org/abs/2406.11171) · 📚 被引 8
- **作者**: Sri Harsha Dumpala, Aman Jaiswal, Chandramouli Shama Sastry, Evangelos E. Milios, Sageev Oore, Hassan Sajjad
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite their remarkable successes, state-of-the-art large language models (LLMs), including vision-and-language models (VLMs) and unimodal language models (ULMs), fail to understand precise semantics. For example, semantically equivalent sentences expressed using different lexical compositions elicit diverging representations. The degree of this divergence and its impact on encoded semantics is not very well understood. In this paper, we introduce the SUGARCREPE++ dataset to analyze the sensitivity of VLMs and ULMs to lexical and semantic alterations. Each sample in SUGARCREPE++ dataset consists of an image and a corresponding triplet of captions: a pair of semantically equivalent but lexically different positive captions and one hard negative caption. This poses a 3-way semantic (in)equivalence problem to the language models. We comprehensively evaluate VLMs and ULMs that differ in architecture, pre-training objectives and datasets to benchmark the performance of SUGARCREPE++ dataset. Experimental results highlight the difficulties of VLMs in distinguishing between lexical and semantic variations, particularly in object attributes and spatial relations. Although VLMs with larger pre-training datasets, model sizes, and multiple pre-training objectives achieve better performance on SUGARCREPE++, there is a significant opportunity for improvement. We show that all the models which achieve better performance on compositionality datasets need not perform equally well on SUGARCREPE++, signifying that compositionality alone may not be sufficient for understanding semantic and lexical alterations. Given the importance of the property that the SUGARCREPE++ dataset targets, it serves as a new challenge to the vision-and-language community.

</details>

### Frustratingly Easy Test-Time Adaptation of Vision-Language Models.
- **链接**: [arXiv:2405.18330](https://arxiv.org/abs/2405.18330) · [代码](https://github.com/FarinaMatteo/zero) · 📚 被引 10
- **作者**: Matteo Farina, Gianni Franchi, Giovanni Iacca, Massimiliano Mancini, Elisa Ricci
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models seamlessly discriminate among arbitrary semantic categories, yet they still suffer from poor generalization when presented with challenging examples. For this reason, Episodic Test-Time Adaptation (TTA) strategies have recently emerged as powerful techniques to adapt VLMs in the presence of a single unlabeled image. The recent literature on TTA is dominated by the paradigm of prompt tuning by Marginal Entropy Minimization, which, relying on online backpropagation, inevitably slows down inference while increasing memory. In this work, we theoretically investigate the properties of this approach and unveil that a surprisingly strong TTA method lies dormant and hidden within it. We term this approach ZERO (TTA with "zero" temperature), whose design is both incredibly effective and frustratingly simple: augment N times, predict, retain the most confident predictions, and marginalize after setting the Softmax temperature to zero. Remarkably, ZERO requires a single batched forward pass through the vision encoder only and no backward passes. We thoroughly evaluate our approach following the experimental protocol established in the literature and show that ZERO largely surpasses or compares favorably w.r.t. the state-of-the-art while being almost 10x faster and 13x more memory-friendly than standard Test-Time Prompt Tuning. Thanks to its simplicity and comparatively negligible computation, ZERO can serve as a strong baseline for future work in this field. The code is available at https://github.com/FarinaMatteo/zero.

</details>

### BendVLM: Test-Time Debiasing of Vision-Language Embeddings.
- **链接**: [arXiv:2411.04420](https://arxiv.org/abs/2411.04420) · 📚 被引 4
- **作者**: Walter Gerych, Haoran Zhang, Kimia Hamidieh, Eileen Pan, Maanas K. Sharma, Tom Hartvigsen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language model (VLM) embeddings have been shown to encode biases present in their training data, such as societal biases that prescribe negative characteristics to members of various racial and gender identities. VLMs are being quickly adopted for a variety of tasks ranging from few-shot classification to text-guided image generation, making debiasing VLM embeddings crucial. Debiasing approaches that fine-tune the VLM often suffer from catastrophic forgetting. On the other hand, fine-tuning-free methods typically utilize a "one-size-fits-all" approach that assumes that correlation with the spurious attribute can be explained using a single linear direction across all possible inputs. In this work, we propose Bend-VLM, a nonlinear, fine-tuning-free approach for VLM embedding debiasing that tailors the debiasing operation to each unique input. This allows for a more flexible debiasing approach. Additionally, we do not require knowledge of the set of inputs a priori to inference time, making our method more appropriate for online, open-set tasks such as retrieval and text guided image generation.

</details>

### TransAgent: Transfer Vision-Language Foundation Models with Heterogeneous Agent Collaboration.
- **链接**: [arXiv:2410.12183](https://arxiv.org/abs/2410.12183) · 📚 被引 5
- **作者**: Yiwei Guo, Shaobin Zhuang, Kunchang Li, Yu Qiao, Yali Wang
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language foundation models (such as CLIP) have recently shown their power in transfer learning, owing to large-scale image-text pre-training. However, target domain data in the downstream tasks can be highly different from the pre-training phase, which makes it hard for such a single model to generalize well. Alternatively, there exists a wide range of expert models that contain diversified vision and/or language knowledge pre-trained on different modalities, tasks, networks, and datasets. Unfortunately, these models are "isolated agents" with heterogeneous structures, and how to integrate their knowledge for generalizing CLIP-like models has not been fully explored. To bridge this gap, we propose a general and concise TransAgent framework, which transports the knowledge of the isolated agents in a unified manner, and effectively guides CLIP to generalize with multi-source knowledge distillation. With such a distinct framework, we flexibly collaborate with 11 heterogeneous agents to empower vision-language foundation models, without further cost in the inference phase. Finally, our TransAgent achieves state-of-the-art performance on 11 visual recognition datasets. Under the same low-shot setting, it outperforms the popular CoOp with around 10% on average, and 20% on EuroSAT which contains large domain shifts.

</details>

### Hidden in Plain Sight: Evaluating Abstract Shape Recognition in Vision-Language Models.
- **链接**: [arXiv:2411.06287](https://arxiv.org/abs/2411.06287) · 📚 被引 1
- **作者**: Arshia Hemmat, Adam Davies, Tom A. Lamb, Jianhao Yuan, Philip Torr, Ashkan Khakzar et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the importance of shape perception in human vision, early neural image classifiers relied less on shape information for object recognition than other (often spurious) features. While recent research suggests that current large Vision-Language Models (VLMs) exhibit more reliance on shape, we find them to still be seriously limited in this regard. To quantify such limitations, we introduce IllusionBench, a dataset that challenges current cutting-edge VLMs to decipher shape information when the shape is represented by an arrangement of visual elements in a scene. Our extensive evaluations reveal that, while these shapes are easily detectable by human annotators, current VLMs struggle to recognize them, indicating important avenues for future work in developing more robust visual perception systems. The full dataset and codebase are available at: \url{https://arshiahemmat.github.io/illusionbench/}

</details>

### Déjà Vu Memorization in Vision-Language Models.
- **链接**: [arXiv:2402.02103](https://arxiv.org/abs/2402.02103)
- **作者**: Bargav Jayaraman, Chuan Guo, Kamalika Chaudhuri
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have emerged as the state-of-the-art representation learning solution, with myriads of downstream applications such as image classification, retrieval and generation. A natural question is whether these models memorize their training data, which also has implications for generalization. We propose a new method for measuring memorization in VLMs, which we call déjà vu memorization. For VLMs trained on image-caption pairs, we show that the model indeed retains information about individual objects in the training images beyond what can be inferred from correlations or the image caption. We evaluate déjà vu memorization at both sample and population level, and show that it is significant for OpenCLIP trained on as many as 50M image-caption pairs. Finally, we show that text randomization considerably mitigates memorization while only moderately impacting the model's downstream task performance.

</details>

### A Unified Debiasing Approach for Vision-Language Models across Modalities and Tasks.
- **链接**: [arXiv:2410.07593](https://arxiv.org/abs/2410.07593) · 📚 被引 4
- **作者**: Hoin Jung, Taeuk Jang, Xiaoqian Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in Vision-Language Models (VLMs) have enabled complex multimodal tasks by processing text and image data simultaneously, significantly enhancing the field of artificial intelligence. However, these models often exhibit biases that can skew outputs towards societal stereotypes, thus necessitating debiasing strategies. Existing debiasing methods focus narrowly on specific modalities or tasks, and require extensive retraining. To address these limitations, this paper introduces Selective Feature Imputation for Debiasing (SFID), a novel methodology that integrates feature pruning and low confidence imputation (LCI) to effectively reduce biases in VLMs. SFID is versatile, maintaining the semantic integrity of outputs and costly effective by eliminating the need for retraining. Our experimental results demonstrate SFID's effectiveness across various VLMs tasks including zero-shot classification, text-to-image retrieval, image captioning, and text-to-image generation, by significantly reducing gender biases without compromising performance. This approach not only enhances the fairness of VLMs applications but also preserves their efficiency and utility across diverse scenarios.

</details>

### What matters when building vision-language models?
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/a03037317560b8c5f2fb4b6466d4c439-Abstract-Conference.html) · 📚 被引 46
- **作者**: Hugo Laurençon, Léo Tronchon, Matthieu Cord, Victor Sanh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### VHELM: A Holistic Evaluation of Vision Language Models.
- **链接**: [arXiv:2410.07112](https://arxiv.org/abs/2410.07112) · 📚 被引 12
- **作者**: Tony Lee, Haoqin Tu, Chi Heem Wong, Wenhao Zheng, Yiyang Zhou, Yifan Mai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current benchmarks for assessing vision-language models (VLMs) often focus on their perception or problem-solving capabilities and neglect other critical aspects such as fairness, multilinguality, or toxicity. Furthermore, they differ in their evaluation procedures and the scope of the evaluation, making it difficult to compare models. To address these issues, we extend the HELM framework to VLMs to present the Holistic Evaluation of Vision Language Models (VHELM). VHELM aggregates various datasets to cover one or more of the 9 aspects: visual perception, knowledge, reasoning, bias, fairness, multilinguality, robustness, toxicity, and safety. In doing so, we produce a comprehensive, multi-dimensional view of the capabilities of the VLMs across these important factors. In addition, we standardize the standard inference parameters, methods of prompting, and evaluation metrics to enable fair comparisons across models. Our framework is designed to be lightweight and automatic so that evaluation runs are cheap and fast. Our initial run evaluates 22 VLMs on 21 existing datasets to provide a holistic snapshot of the models. We uncover new key findings, such as the fact that efficiency-focused models (e.g., Claude 3 Haiku or Gemini 1.5 Flash) perform significantly worse than their full models (e.g., Claude 3 Opus or Gemini 1.5 Pro) on the bias benchmark but not when evaluated on the other aspects. For transparency, we release the raw model generations and complete results on our website (https://crfm.stanford.edu/helm/vhelm/v2.0.1). VHELM is intended to be a living benchmark, and we hope to continue adding new datasets and models over time.

</details>

### SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/76954b4a44e158e738b4c64494977c6a-Abstract-Conference.html) · 📚 被引 3
- **作者**: Chuanhao Li, Zhen Li, Chenchen Jing, Shuo Liu, Wenqi Shao, Yuwei Wu et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

### NaturalBench: Evaluating Vision-Language Models on Natural Adversarial Samples.
- **链接**: [arXiv:2410.14669](https://arxiv.org/abs/2410.14669) · 📚 被引 3
- **作者**: Baiqi Li, Zhiqiu Lin, Wenxuan Peng, Jean de Dieu Nyandwi, Daniel Jiang, Zixian Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have made significant progress in recent visual-question-answering (VQA) benchmarks that evaluate complex visio-linguistic reasoning. However, are these models truly effective? In this work, we show that VLMs still struggle with natural images and questions that humans can easily answer, which we term natural adversarial samples. We also find it surprisingly easy to generate these VQA samples from natural image-text corpora using off-the-shelf models like CLIP and ChatGPT. We propose a semi-automated approach to collect a new benchmark, NaturalBench, for reliably evaluating VLMs with 10,000 human-verified VQA samples. Crucially, we adopt a $\textbf{vision-centric}$ design by pairing each question with two images that yield different answers, preventing blind solutions from answering without using the images. This makes NaturalBench more challenging than previous benchmarks that can be solved with commonsense priors. We evaluate 53 state-of-the-art VLMs on NaturalBench, showing that models like LLaVA-OneVision, Cambrian-1, Llama3.2-Vision, Molmo, Qwen2-VL, and even GPT-4o lag 50%-70% behind human performance (over 90%). We analyze why NaturalBench is hard from two angles: (1) Compositionality: Solving NaturalBench requires diverse visio-linguistic skills, including understanding attribute bindings, object relationships, and advanced reasoning like logic and counting. To this end, unlike prior work that uses a single tag per sample, we tag each NaturalBench sample with 1 to 8 skill tags for fine-grained evaluation. (2) Biases: NaturalBench exposes severe biases in VLMs, as models often choose the same answer regardless of the image. Lastly, we apply our benchmark curation method to diverse data sources, including long captions (over 100 words) and non-English languages like Chinese and Hindi, highlighting its potential for dynamic evaluations of VLMs.

</details>

### Membership Inference Attacks against Large Vision-Language Models.
- **链接**: [arXiv:2411.02902](https://arxiv.org/abs/2411.02902) · [代码](https://github.com/LIONS-EPFL/VL-MIA) · 📚 被引 8
- **作者**: Zhan Li, Yongtao Wu, Yihang Chen, Francesco Tonin, Elías Abad-Rocamora, Volkan Cevher
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (VLLMs) exhibit promising capabilities for processing multi-modal tasks across various application scenarios. However, their emergence also raises significant data security concerns, given the potential inclusion of sensitive information, such as private photos and medical records, in their training datasets. Detecting inappropriately used data in VLLMs remains a critical and unresolved issue, mainly due to the lack of standardized datasets and suitable methodologies. In this study, we introduce the first membership inference attack (MIA) benchmark tailored for various VLLMs to facilitate training data detection. Then, we propose a novel MIA pipeline specifically designed for token-level image detection. Lastly, we present a new metric called MaxRényi-K%, which is based on the confidence of the model output and applies to both text and image data. We believe that our work can deepen the understanding and methodology of MIAs in the context of VLLMs. Our code and datasets are available at https://github.com/LIONS-EPFL/VL-MIA.

</details>

### UMFC: Unsupervised Multi-Domain Feature Calibration for Vision-Language Models.
- **链接**: [arXiv:2411.06921](https://arxiv.org/abs/2411.06921) · [代码](https://github.com/GIT-LJc/UMFC) · 📚 被引 1
- **作者**: Jiachen Liang, Ruibing Hou, Minyang Hu, Hong Chang, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models (e.g., CLIP) have shown powerful zero-shot transfer capabilities. But they still struggle with domain shifts and typically require labeled data to adapt to downstream tasks, which could be costly. In this work, we aim to leverage unlabeled data that naturally spans multiple domains to enhance the transferability of vision-language models. Under this unsupervised multi-domain setting, we have identified inherent model bias within CLIP, notably in its visual and text encoders. Specifically, we observe that CLIP's visual encoder tends to prioritize encoding domain over discriminative category information, meanwhile its text encoder exhibits a preference for domain-relevant classes. To mitigate this model bias, we propose a training-free and label-free feature calibration method, Unsupervised Multi-domain Feature Calibration (UMFC). UMFC estimates image-level biases from domain-specific features and text-level biases from the direction of domain transition. These biases are subsequently subtracted from original image and text features separately, to render them domain-invariant. We evaluate our method on multiple settings including transductive learning and test-time adaptation. Extensive experiments show that our method outperforms CLIP and performs on par with the state-of-the-arts that need additional annotations or optimization. Our code is available at https://github.com/GIT-LJc/UMFC.

</details>

### Vision-Language Navigation with Energy-Based Policy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c3ec89aed795f9deeff3f1390c3bd882-Abstract-Conference.html) · 📚 被引 12
- **作者**: Rui Liu, Wenguan Wang, Yi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Pandora's Box: Towards Building Universal Attackers against Real-World Large Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5d516fc09b53e9a7fade4fbad703e686-Abstract-Conference.html) · 📚 被引 2
- **作者**: Daizong Liu, Mingyu Yang, Xiaoye Qu, Pan Zhou, Xiang Fang, Keke Tang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/563991b5c8b45fe75bea42db738223b2-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 4
- **作者**: Yujie Lu, Dongfu Jiang, Wenhu Chen, William Yang Wang, Yejin Choi, Bill Yuchen Lin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/dde040998d82553cf7f689e8ae173d5a-Abstract-Conference.html) · 📚 被引 8
- **作者**: Xinyu Lyu, Beitao Chen, Lianli Gao, Hengtao Shen, Jingkuan Song
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/7f2257d2b291b8d7e712c70b67e09412-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chenyang Ma, Kai Lu, Ta Ying Cheng, Niki Trigoni, Andrew Markham
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Towards Calibrated Robust Fine-Tuning of Vision-Language Models.
- **链接**: [arXiv:2311.01723](https://arxiv.org/abs/2311.01723) · 📚 被引 4
- **作者**: Changdae Oh, Hyesu Lim, Mijoo Kim, Dongyoon Han, Sangdoo Yun, Jaegul Choo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Improving out-of-distribution (OOD) generalization during in-distribution (ID) adaptation is a primary goal of robust fine-tuning of zero-shot models beyond naive fine-tuning. However, despite decent OOD generalization performance from recent robust fine-tuning methods, confidence calibration for reliable model output has not been fully addressed. This work proposes a robust fine-tuning method that improves both OOD accuracy and confidence calibration simultaneously in vision language models. Firstly, we show that both OOD classification and OOD calibration errors have a shared upper bound consisting of two terms of ID data: 1) ID calibration error and 2) the smallest singular value of the ID input covariance matrix. Based on this insight, we design a novel framework that conducts fine-tuning with a constrained multimodal contrastive loss enforcing a larger smallest singular value, which is further guided by the self-distillation of a moving-averaged model to achieve calibrated prediction as well. Starting from empirical evidence supporting our theoretical statements, we provide extensive experimental results on ImageNet distribution shift benchmarks that demonstrate the effectiveness of our theorem and its practical implementation.

</details>

### Federated Learning from Vision-Language Foundation Models: Theoretical Analysis and Method.
- **链接**: [arXiv:2409.19610](https://arxiv.org/abs/2409.19610) · 📚 被引 2
- **作者**: Bikang Pan, Wei Huang, Ye Shi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Integrating pretrained vision-language foundation models like CLIP into federated learning has attracted significant attention for enhancing generalization across diverse tasks. Typically, federated learning of vision-language models employs prompt learning to reduce communication and computational costs, i.e., prompt-based federated learning. However, there is limited theoretical analysis to understand the performance of prompt-based federated learning. In this work, we construct a theoretical analysis framework for prompt-based federated learning via feature learning theory. Specifically, we monitor the evolution of signal learning and noise memorization in prompt-based federated learning, demonstrating that performance can be assessed by the ratio of task-relevant to task-irrelevant coefficients. Furthermore, we draw an analogy between income and risk in portfolio optimization and the task-relevant and task-irrelevant terms in feature learning. Leveraging inspiration from portfolio optimization that combining two independent assets will maintain the income while reducing the risk, we introduce two prompts: global prompt and local prompt to construct a prompt portfolio to balance the generalization and personalization. Consequently, we showed the performance advantage of the prompt portfolio and derived the optimal mixing coefficient. These theoretical claims have been further supported by empirical experiments.

</details>

### TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/39781da4b5d05bc2908ce08e43bc6404-Abstract-Conference.html) · 📚 被引 6
- **作者**: Maitreya Patel, Abhiram Kusumba, Sheng Cheng, Changhoon Kim, Tejas Gokhale, Chitta Baral et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### No Filter: Cultural and Socioeconomic Diversity in Contrastive Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c07d71ff0bc042e4b9acd626a79597fa-Abstract-Conference.html) · 📚 被引 1
- **作者**: Angéline Pouget, Lucas Beyer, Emanuele Bugliarello, Xiao Wang, Andreas Steiner, Xiaohua Zhai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Image2Struct: Benchmarking Structure Extraction for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d0718553fd6b227a353c6432cf893285-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Josselin Somerville Roberts, Tony Lee, Chi Heem Wong, Michihiro Yasunaga, Yifan Mai, Percy Liang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Private Attribute Inference from Images with Vision-Language Models.
- **链接**: [arXiv:2404.10618](https://arxiv.org/abs/2404.10618) · 📚 被引 6
- **作者**: Batuhan Tömekçe, Mark Vero, Robin Staab, Martin T. Vechev
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As large language models (LLMs) become ubiquitous in our daily tasks and digital interactions, associated privacy risks are increasingly in focus. While LLM privacy research has primarily focused on the leakage of model training data, it has recently been shown that LLMs can make accurate privacy-infringing inferences from previously unseen texts. With the rise of vision-language models (VLMs), capable of understanding both images and text, a key question is whether this concern transfers to the previously unexplored domain of benign images posted online. To answer this question, we compile an image dataset with human-annotated labels of the image owner's personal attributes. In order to understand the privacy risks posed by VLMs beyond traditional human attribute recognition, our dataset consists of images where the inferable private attributes do not stem from direct depictions of humans. On this dataset, we evaluate 7 state-of-the-art VLMs, finding that they can infer various personal attributes at up to 77.6% accuracy. Concerningly, we observe that accuracy scales with the general capabilities of the models, implying that future models can be misused as stronger inferential adversaries, establishing an imperative for the development of adequate defenses.

</details>

### RaVL: Discovering and Mitigating Spurious Correlations in Fine-Tuned Vision-Language Models.
- **链接**: [arXiv:2411.04097](https://arxiv.org/abs/2411.04097) · 📚 被引 0
- **作者**: Maya Varma, Jean-Benoit Delbrouck, Zhihong Chen, Akshay Chaudhari, Curtis P. Langlotz
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-tuned vision-language models (VLMs) often capture spurious correlations between image features and textual attributes, resulting in degraded zero-shot performance at test time. Existing approaches for addressing spurious correlations (i) primarily operate at the global image-level rather than intervening directly on fine-grained image features and (ii) are predominantly designed for unimodal settings. In this work, we present RaVL, which takes a fine-grained perspective on VLM robustness by discovering and mitigating spurious correlations using local image features rather than operating at the global image level. Given a fine-tuned VLM, RaVL first discovers spurious correlations by leveraging a region-level clustering approach to identify precise image features contributing to zero-shot classification errors. Then, RaVL mitigates the identified spurious correlation with a novel region-aware loss function that enables the VLM to focus on relevant regions and ignore spurious relationships during fine-tuning. We evaluate RaVL on 654 VLMs with various model architectures, data domains, and learned spurious correlations. Our results show that RaVL accurately discovers (191% improvement over the closest baseline) and mitigates (8.2% improvement on worst-group image classification accuracy) spurious correlations. Qualitative evaluations on general-domain and medical-domain VLMs confirm our findings.

</details>

### Q-VLM: Post-training Quantization for Large Vision-Language Models.
- **链接**: [arXiv:2410.08119](https://arxiv.org/abs/2410.08119) · [代码](https://github.com/ChangyuanWang17/QVLM) · 📚 被引 6
- **作者**: Changyuan Wang, Ziwei Wang, Xiuwei Xu, Yansong Tang, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a post-training quantization framework of large vision-language models (LVLMs) for efficient multi-modal inference. Conventional quantization methods sequentially search the layer-wise rounding functions by minimizing activation discretization errors, which fails to acquire optimal quantization strategy without considering cross-layer dependency. On the contrary, we mine the cross-layer dependency that significantly influences discretization errors of the entire vision-language model, and embed this dependency into optimal quantization strategy searching with low search cost. Specifically, we observe the strong correlation between the activation entropy and the cross-layer dependency concerning output discretization errors. Therefore, we employ the entropy as the proxy to partition blocks optimally, which aims to achieve satisfying trade-offs between discretization errors and the search cost. Moreover, we optimize the visual encoder to disentangle the cross-layer dependency for fine-grained decomposition of search space, so that the search cost is further reduced without harming the quantization accuracy. Experimental results demonstrate that our method compresses the memory by 2.78x and increase generate speed by 1.44x about 13B LLaVA model without performance degradation on diverse multi-modal reasoning tasks. Code is available at https://github.com/ChangyuanWang17/QVLM.

</details>

### Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/89cc5e613d34f90de90c21e996e60b30-Abstract-Conference.html) · 📚 被引 18
- **作者**: Jiayu Wang, Yifei Ming, Zhenmei Shi, Vibhav Vineet, Xin Wang, Sharon Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Enhancing vision-language models for medical imaging: bridging the 3D gap with innovative slice selection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b53513b83232116ae25f57a174a7c993-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 6
- **作者**: Yuli Wang, Peng jian, Yuwei Dai, Craig K. Jones, Haris I. Sair, Jinglai Shen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Vision-Language Models are Strong Noisy Label Detectors.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6af08ba9468f0daca4b8dd388cb95824-Abstract-Conference.html) · 📚 被引 7
- **作者**: Tong Wei, Hao-Tian Li, Chun-Shu Li, Jiang-Xin Shi, Yufeng Li, Min-Ling Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Toward a Stable, Fair, and Comprehensive Evaluation of Object Hallucination in Large Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c9b551a2e195a209fc0b280de2f7f781-Abstract-Conference.html) · 📚 被引 1
- **作者**: Hongliang Wei, Xingtao Wang, Xianqi Zhang, Xiaopeng Fan, Debin Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Shadowcast: Stealthy Data Poisoning Attacks Against Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6a2e30664b9647f97d7b9275358d083c-Abstract-Conference.html) · 📚 被引 1
- **作者**: Yuancheng Xu, Jiarui Yao, Manli Shu, Yanchao Sun, Zichu Wu, Ning Yu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Voila-A: Aligning Vision-Language Models with User's Gaze Attention.
- **链接**: [arXiv:2401.09454](https://arxiv.org/abs/2401.09454) · 📚 被引 3
- **作者**: Kun Yan, Zeyu Wang, Lei Ji, Yuntao Wang, Nan Duan, Shuai Ma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, the integration of vision and language understanding has led to significant advancements in artificial intelligence, particularly through Vision-Language Models (VLMs). However, existing VLMs face challenges in handling real-world applications with complex scenes and multiple objects, as well as aligning their focus with the diverse attention patterns of human users. In this paper, we introduce gaze information, feasibly collected by AR or VR devices, as a proxy for human attention to guide VLMs and propose a novel approach, Voila-A, for gaze alignment to enhance the interpretability and effectiveness of these models in real-world applications. First, we collect hundreds of minutes of gaze data to demonstrate that we can mimic human gaze modalities using localized narratives. We then design an automatic data annotation pipeline utilizing GPT-4 to generate the VOILA-COCO dataset. Additionally, we innovate the Voila Perceiver modules to integrate gaze information into VLMs while preserving their pretrained knowledge. We evaluate Voila-A using a hold-out validation set and a newly collected VOILA-GAZE Testset, which features real-life scenarios captured with a gaze-tracking device. Our experimental results demonstrate that Voila-A significantly outperforms several baseline models. By aligning model attention with human gaze patterns, Voila-A paves the way for more intuitive, user-centric VLMs and fosters engaging human-AI interaction across a wide range of applications.

</details>

### Lever LM: Configuring In-Context Sequence to Lever Large Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b619cd6dcc986856b8a8da2b08d89396-Abstract-Conference.html) · 📚 被引 3
- **作者**: Xu Yang, Yingzhe Peng, Haoxuan Ma, Shuo Xu, Chi Zhang, Yucheng Han et al.
- **🏷️ 机构**: NUS
- **会议**: NeurIPS 2024

### Bridge the Modality and Capability Gaps in Vision-Language Model Selection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/3d007df4ae13adf9001f8969555b11bd-Abstract-Conference.html) · 📚 被引 3
- **作者**: Chao Yi, Yuhang He, De-Chuan Zhan, Han-Jia Ye
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Self-Calibrated Tuning of Vision-Language Models for Out-of-Distribution Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/666e5e1df2d04dbe2b545ea3a3e3f7d3-Abstract-Conference.html) · 📚 被引 3
- **作者**: Geng Yu, Jianing Zhu, Jiangchao Yao, Bo Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Boosting Vision-Language Models with Transduction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/71d7dbe2652bd4662d29fa269f059db4-Abstract-Conference.html) · 📚 被引 7
- **作者**: Maxime Zanella, Benoît Gérin, Ismail Ben Ayed
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c848b7d3adc08fcd0bf1df3101ba6728-Abstract-Conference.html) · 📚 被引 19
- **作者**: Simon Zhai, Hao Bai, Zipeng Lin, Jiayi Pan, Peter Tong, Yifei Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Rethinking Misalignment in Vision-Language Model Adaptation from a Causal Perspective.
- **链接**: [arXiv:2410.12816](https://arxiv.org/abs/2410.12816) · 📚 被引 7
- **作者**: Yanan Zhang, Jiangmeng Li, Lixiang Liu, Wenwen Qiang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Foundational Vision-Language models such as CLIP have exhibited impressive generalization in downstream tasks. However, CLIP suffers from a two-level misalignment issue, i.e., task misalignment and data misalignment, when adapting to specific tasks. Soft prompt tuning has mitigated the task misalignment, yet the data misalignment remains a challenge. To analyze the impacts of the data misalignment, we revisit the pre-training and adaptation processes of CLIP and develop a structural causal model. We discover that while we expect to capture task-relevant information for downstream tasks accurately, the task-irrelevant knowledge impacts the prediction results and hampers the modeling of the true relationships between the images and the predicted classes. As task-irrelevant knowledge is unobservable, we leverage the front-door adjustment and propose Causality-Guided Semantic Decoupling and Classification (CDC) to mitigate the interference of task-irrelevant knowledge. Specifically, we decouple semantics contained in the data of downstream tasks and perform classification based on each semantic. Furthermore, we employ the Dempster-Shafer evidence theory to evaluate the uncertainty of each prediction generated by diverse semantics. Experiments conducted in multiple different settings have consistently demonstrated the effectiveness of CDC.

</details>

### AdaNeg: Adaptive Negative Proxy Guided OOD Detection with Vision-Language Models.
- **链接**: [arXiv:2410.20149](https://arxiv.org/abs/2410.20149) · [代码](https://github.com/YBZh/OpenOOD-VLM) · 📚 被引 11
- **作者**: Yabin Zhang, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent research has shown that pre-trained vision-language models are effective at identifying out-of-distribution (OOD) samples by using negative labels as guidance. However, employing consistent negative labels across different OOD datasets often results in semantic misalignments, as these text labels may not accurately reflect the actual space of OOD images. To overcome this issue, we introduce \textit{adaptive negative proxies}, which are dynamically generated during testing by exploring actual OOD images, to align more closely with the underlying OOD label space and enhance the efficacy of negative proxy guidance. Specifically, our approach utilizes a feature memory bank to selectively cache discriminative features from test images, representing the targeted OOD distribution. This facilitates the creation of proxies that can better align with specific OOD datasets. While task-adaptive proxies average features to reflect the unique characteristics of each dataset, the sample-adaptive proxies weight features based on their similarity to individual test samples, exploring detailed sample-level nuances. The final score for identifying OOD samples integrates static negative labels with our proposed adaptive proxies, effectively combining textual and visual knowledge for enhanced performance. Our method is training-free and annotation-free, and it maintains fast testing speed. Extensive experiments across various benchmarks demonstrate the effectiveness of our approach, abbreviated as AdaNeg. Notably, on the large-scale ImageNet benchmark, our AdaNeg significantly outperforms existing methods, with a 2.45\% increase in AUROC and a 6.48\% reduction in FPR95. Codes are available at \url{https://github.com/YBZh/OpenOOD-VLM}.

</details>

### EvolveDirector: Approaching Advanced Text-to-Image Generation with Large Vision-Language Models.
- **链接**: [arXiv:2410.07133](https://arxiv.org/abs/2410.07133) · [代码](https://github.com/showlab/EvolveDirector) · 📚 被引 2
- **作者**: Rui Zhao, Hangjie Yuan, Yujie Wei, Shiwei Zhang, Yuchao Gu, Lingmin Ran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in generation models have showcased remarkable capabilities in generating fantastic content. However, most of them are trained on proprietary high-quality data, and some models withhold their parameters and only provide accessible application programming interfaces (APIs), limiting their benefits for downstream tasks. To explore the feasibility of training a text-to-image generation model comparable to advanced models using publicly available resources, we introduce EvolveDirector. This framework interacts with advanced models through their public APIs to obtain text-image data pairs to train a base model. Our experiments with extensive data indicate that the model trained on generated data of the advanced model can approximate its generation capability. However, it requires large-scale samples of 10 million or more. This incurs significant expenses in time, computational resources, and especially the costs associated with calling fee-based APIs. To address this problem, we leverage pre-trained large vision-language models (VLMs) to guide the evolution of the base model. VLM continuously evaluates the base model during training and dynamically updates and refines the training dataset by the discrimination, expansion, deletion, and mutation operations. Experimental results show that this paradigm significantly reduces the required data volume. Furthermore, when approaching multiple advanced models, EvolveDirector can select the best samples generated by them to learn powerful and balanced abilities. The final trained model Edgen is demonstrated to outperform these advanced models. The code and model weights are available at https://github.com/showlab/EvolveDirector.

</details>

### Calibrated Self-Rewarding Vision Language Models.
- **链接**: [arXiv:2405.14622](https://arxiv.org/abs/2405.14622) · [代码](https://github.com/YiyangZhou/CSR) · 📚 被引 0
- **作者**: Yiyang Zhou, Zhiyuan Fan, Dongjie Cheng, Sihan Yang, Zhaorun Chen, Chenhang Cui et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) have made substantial progress by integrating pre-trained large language models (LLMs) and vision models through instruction tuning. Despite these advancements, LVLMs often exhibit the hallucination phenomenon, where generated text responses appear linguistically plausible but contradict the input image, indicating a misalignment between image and text pairs. This misalignment arises because the model tends to prioritize textual information over visual input, even when both the language model and visual representations are of high quality. Existing methods leverage additional models or human annotations to curate preference data and enhance modality alignment through preference optimization. These approaches may not effectively reflect the target LVLM's preferences, making the curated preferences easily distinguishable. Our work addresses these challenges by proposing the Calibrated Self-Rewarding (CSR) approach, which enables the model to self-improve by iteratively generating candidate responses, evaluating the reward for each response, and curating preference data for fine-tuning. In the reward modeling, we employ a step-wise strategy and incorporate visual constraints into the self-rewarding process to place greater emphasis on visual input. Empirical results demonstrate that CSR enhances performance and reduces hallucinations across ten benchmarks and tasks, achieving substantial improvements over existing methods by 7.62%. Our empirical results are further supported by rigorous theoretical analysis, under mild assumptions, verifying the effectiveness of introducing visual constraints into the self-rewarding paradigm. Additionally, CSR shows compatibility with different vision-language models and the ability to incrementally improve performance through iterative fine-tuning. Our data and code are available at https://github.com/YiyangZhou/CSR.

</details>

### Few-Shot Adversarial Prompt Learning on Vision-Language Models.
- **链接**: [arXiv:2403.14774](https://arxiv.org/abs/2403.14774) · [代码](https://github.com/lionel-w2/FAP) · 📚 被引 3
- **作者**: Yiwei Zhou, Xiaobo Xia, Zhiwei Lin, Bo Han, Tongliang Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The vulnerability of deep neural networks to imperceptible adversarial perturbations has attracted widespread attention. Inspired by the success of vision-language foundation models, previous efforts achieved zero-shot adversarial robustness by aligning adversarial visual features with text supervision. However, in practice, they are still unsatisfactory due to several issues, including heavy adaptation cost, suboptimal text supervision, and uncontrolled natural generalization capacity. In this paper, to address these issues, we propose a few-shot adversarial prompt framework where adapting input sequences with limited data makes significant adversarial robustness improvement. Specifically, we achieve this by providing adversarially correlated text supervision that is end-to-end learned from adversarial examples. We also propose a novel training objective that enhances the consistency of multi-modal features while encourages differentiated uni-modal features between natural and adversarial examples. The proposed framework gives access to learn adversarial text supervision, which provides superior cross-modal adversarial alignment and matches state-of-the-art zero-shot adversarial robustness with only 1% training data. Code is available at: https://github.com/lionel-w2/FAP.

</details>

### AWT: Transferring Vision-Language Models via Augmentation, Weighting, and Transportation.
- **链接**: [arXiv:2407.04603](https://arxiv.org/abs/2407.04603) · 📚 被引 4
- **作者**: Yuhan Zhu, Yuyang Ji, Zhiyu Zhao, Gangshan Wu, Limin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models (VLMs) have shown impressive results in various visual classification tasks. However, we often fail to fully unleash their potential when adapting them for new concept understanding due to limited information on new classes. To address this limitation, we introduce a novel adaptation framework, AWT (Augment, Weight, then Transport). AWT comprises three key components: augmenting inputs with diverse visual perspectives and enriched class descriptions through image transformations and language models; dynamically weighting inputs based on the prediction entropy; and employing optimal transport to mine semantic correlations in the vision-language space. AWT can be seamlessly integrated into various VLMs, enhancing their zero-shot capabilities without additional training and facilitating few-shot learning through an integrated multimodal adapter module. We verify AWT in multiple challenging scenarios, including zero-shot and few-shot image classification, zero-shot video action recognition, and out-of-distribution generalization. AWT consistently outperforms the state-of-the-art methods in each setting. In addition, our extensive studies further demonstrate AWT's effectiveness and adaptability across different VLMs, architectures, and scales.

</details>

### Magnet: We Never Know How Text-to-Image Diffusion Models Work, Until We Learn How Vision-Language Models Function.
- **链接**: [arXiv:2409.19967](https://arxiv.org/abs/2409.19967) · 📚 被引 3
- **作者**: Chenyi Zhuang, Ying Hu, Pan Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-to-image diffusion models particularly Stable Diffusion, have revolutionized the field of computer vision. However, the synthesis quality often deteriorates when asked to generate images that faithfully represent complex prompts involving multiple attributes and objects. While previous studies suggest that blended text embeddings lead to improper attribute binding, few have explored this in depth. In this work, we critically examine the limitations of the CLIP text encoder in understanding attributes and investigate how this affects diffusion models. We discern a phenomenon of attribute bias in the text space and highlight a contextual issue in padding embeddings that entangle different concepts. We propose \textbf{Magnet}, a novel training-free approach to tackle the attribute binding problem. We introduce positive and negative binding vectors to enhance disentanglement, further with a neighbor strategy to increase accuracy. Extensive experiments show that Magnet significantly improves synthesis quality and binding accuracy with negligible computational cost, enabling the generation of unconventional and unnatural concepts.

</details>

## 跨领域论文（完整笔记在其他领域）

- MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning. → [object-detection](../object-detection/Guideline%202024.md)
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
- Mind the Interference: Retaining Pre-trained Knowledge in Parameter Efficient Continual Learning of Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- Select and Distill: Selective Dual-Teacher Knowledge Transfer for Continual Learning on Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- Class-Incremental Learning with CLIP: Adaptive Representation Adjustment and Parameter Fusion. → [continual-learning](../continual-learning/Guideline%202024.md)
- IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models. → [network-pruning](../network-pruning/Guideline%202024.md)

## 🆕 增量新增

### CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2403.08919](https://arxiv.org/abs/2403.08919) · 📚 被引 24
- **作者**: Chenbin Pan, Burhaneddin Yaman, Senem Velipasalar, Liu Ren
- **🏷️ 机构**: Syracuse University, Bosch Research North America &#x0026; Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024
- **摘要（中）**: 针对多视角图像BEV检测中缺乏清晰监督的问题，提出了CLIP-BEVFormer，利用对比学习增强BEV骨干网络，引入真值信息流。该方法通过CLIP对齐图像和BEV特征，提升3D检测性能。在nuScenes数据集上，NDS和mAP分别提升8.5%和9.2%，显著优于现有最先进模型。
- **摘要（英）**: This paper introduces CLIP-BEVFormer to address the lack of clear supervision in BEV detection by leveraging contrastive learning to enhance multi-view image-derived BEV backbones with ground truth flow. The method achieves significant improvements of 8.5% NDS and 9.2% mAP over state-of-the-art on nuScenes for 3D object detection.
- **核心贡献**: 提出了CLIP-BEVFormer，利用对比学习增强BEV特征并引入真值信息流。
- **创新点**: 将CLIP的对比学习机制引入BEV检测，解决监督不足问题。
- **结果**: 在nuScenes上NDS和mAP分别提升8.5%和9.2%，超越现有最先进方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving stands as a pivotal domain in computer vision, shaping the future of transportation. Within this paradigm, the backbone of the system plays a crucial role in interpreting the complex environment. However, a notable challenge has been the loss of clear supervision when it comes to Bird's Eye View elements. To address this limitation, we introduce CLIP-BEVFormer, a novel approach that leverages the power of contrastive learning techniques to enhance the multi-view image-derived BEV backbones with ground truth information flow. We conduct extensive experiments on the challenging nuScenes dataset and showcase significant and consistent improvements over the SOTA. Specifically, CLIP-BEVFormer achieves an impressive 8.5\% and 9.2\% enhancement in terms of NDS and mAP, respectively, over the previous best BEV model on the 3D object detection task.

</details>

### THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2405.05256](https://arxiv.org/abs/2405.05256) · 📚 被引 19
- **作者**: Prannay Kaul, Zhizhong Li, Hao Yang, Yonatan Dukler, Ashwin Swaminathan, C. J. Taylor et al.
- **🏷️ 机构**: University of Oxford,VGG, AWS AI Labs
- **会议**: CVPR 2024
- **摘要（中）**: ①针对大型视觉语言模型（LVLM）在自由形式生成中的幻觉问题，现有基准主要评估特定问题格式（如多项选择）的幻觉（Type II），而忽略了开放式回答中的幻觉（Type I），且两者往往负相关。②提出了THRONE，一个基于对象的自动评估框架，利用公开语言模型识别LVLM自由输出中的幻觉，并计算信息量丰富的指标。③改进点在于无需外部API调用，且专门针对Type I幻觉进行量化评估。④通过在多个最新LVLM上的评估，表明现有指标的改进并不减少Type I幻觉，揭示了现有基准的局限性。
- **摘要（英）**: This paper addresses the hallucination issue in large vision-language models (LVLMs) during free-form generation, which is often overlooked by existing benchmarks focusing on specific question formats. It proposes THRONE, an object-based automatic framework that uses public language models to detect hallucinations and compute informative metrics. The evaluation shows that improvements in existing metrics do not reduce Type I hallucinations, highlighting the limitations of current benchmarks.
- **核心贡献**: 提出了首个针对LVLM自由形式生成中Type I幻觉的自动评估框架THRONE。
- **创新点**: 利用公开语言模型自动识别幻觉，无需外部API，并区分Type I和Type II幻觉。
- **结果**: 实验表明现有指标改进与Type I幻觉减少不相关，揭示了基准的不足。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mitigating hallucinations in large vision-language models (LVLMs) remains an open problem. Recent benchmarks do not address hallucinations in open-ended free-form responses, which we term "Type I hallucinations". Instead, they focus on hallucinations responding to very specific question formats -- typically a multiple-choice response regarding a particular object or attribute -- which we term "Type II hallucinations". Additionally, such benchmarks often require external API calls to models which are subject to change. In practice, we observe that a reduction in Type II hallucinations does not lead to a reduction in Type I hallucinations but rather that the two forms of hallucinations are often anti-correlated. To address this, we propose THRONE, a novel object-based automatic framework for quantitatively evaluating Type I hallucinations in LVLM free-form outputs. We use public language models (LMs) to identify hallucinations in LVLM responses and compute informative metrics. By evaluating a large selection of recent LVLMs using public datasets, we show that an improvement in existing metrics do not lead to a reduction in Type I hallucinations, and that established benchmarks for measuring Type I hallucinations are incomplete. Finally, we provide a simple and effective data augmentation method to reduce Type I and Type II hallucinations as a strong baseline. Code is now available at https://github.com/amazon-science/THRONE .

</details>

### MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2402.04788](https://arxiv.org/abs/2402.04788)
- **作者**: Dongping Chen, Ruoxi Chen, Shilin Zhang, Yaochen Wang, Yinuo Liu, Huichi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024
- **摘要（中）**: ①针对多模态大语言模型作为评估器的能力缺乏基准的问题。②提出了MLLM-as-a-Judge基准，评估MLLM在评分、配对比较和批量排序三种任务中的判断能力。③相比现有工作，首次系统评估MLLM作为评估器的能力。④研究发现MLLM在配对比较中表现良好，但在评分和批量排序中与人类偏好有显著差异，且存在偏见和幻觉问题。
- **摘要（英）**: This paper addresses the lack of benchmarks for assessing MLLMs as judges. It introduces MLLM-as-a-Judge, evaluating MLLMs in scoring, pair comparison, and batch ranking tasks. It reveals that MLLMs perform well in pair comparison but diverge from human preferences in scoring and ranking, with biases and hallucinations.
- **核心贡献**: 提出了评估多模态大语言模型判断能力的基准。
- **创新点**: 首次系统评估MLLM作为评估器的能力。
- **结果**: 揭示了MLLM在评估任务中的局限。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) have gained significant attention recently, showing remarkable potential in artificial general intelligence. However, assessing the utility of MLLMs presents considerable challenges, primarily due to the absence of multimodal benchmarks that align with human preferences. Drawing inspiration from the concept of LLM-as-a-Judge within LLMs, this paper introduces a novel benchmark, termed MLLM-as-a-Judge, to assess the ability of MLLMs in assisting judges across diverse modalities, encompassing three distinct tasks: Scoring Evaluation, Pair Comparison, and Batch Ranking. Our study reveals that, while MLLMs demonstrate remarkable human-like discernment in Pair Comparison, there is a significant divergence from human preferences in Scoring Evaluation and Batch Ranking. Furthermore, a closer examination reveals persistent challenges in the judgment capacities of LLMs, including diverse biases, hallucinatory responses, and inconsistencies in judgment, even in advanced models such as GPT-4V. These findings emphasize the pressing need for enhancements and further research efforts to be undertaken before regarding MLLMs as fully reliable evaluators. In light of this, we advocate for additional efforts dedicated to supporting the continuous development within the domain of MLLM functioning as judges. The code and dataset are publicly available at our project homepage: \url{https://mllm-judge.github.io/}.

</details>

### MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI. **⭐⭐⭐⭐** (相关度: 45%)
- **链接**: [出版页](https://proceedings.mlr.press/v235/ying24a.html)
- **作者**: Kaining Ying, Fanqing Meng, Jin Wang, Zhiqian Li, Han Lin, Yue Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024
- **摘要（中）**: ①针对大型视觉语言模型在多任务AGI评估中缺乏全面基准的问题。②提出了MMT-Bench，一个综合多模态基准，用于评估大型视觉语言模型的多任务能力。③相比现有工作，覆盖更广泛的任务类型，旨在全面评估模型性能。④摘要未提供具体数据，但基准设计用于多任务AGI评估。
- **摘要（英）**: This paper addresses the lack of comprehensive benchmarks for evaluating large vision-language models towards multitask AGI. It proposes MMT-Bench, a comprehensive multimodal benchmark covering diverse tasks. It aims to provide a systematic evaluation of model capabilities across tasks.
- **核心贡献**: 提出了多任务AGI评估的综合多模态基准。
- **创新点**: 覆盖广泛任务类型，支持多任务能力评估。
- **结果**: 基准可用于评估大型视觉语言模型的多任务性能。

### VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/1198b53fa686831d5f0c0860d7ec4f34-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 5
- **作者**: Han Huang, Haitian Zhong, Tao Yu, Qiang Liu, Shu Wu, Liang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①该论文针对大型视觉语言模型（VLM）知识编辑缺乏统一基准的问题。②提出了VLKEB基准，用于系统评估VLM知识编辑方法的性能。③相比已有工作，该基准可能覆盖多种知识类型和编辑场景，提供更全面的评估框架。④摘要未提供具体数据，但基准的建立有助于推动VLM知识编辑研究。
- **摘要（英）**: This paper addresses the lack of a unified benchmark for knowledge editing in large vision-language models (VLMs). It introduces VLKEB, a benchmark designed to systematically evaluate VLM knowledge editing methods. Compared to existing work, it likely covers diverse knowledge types and editing scenarios, providing a comprehensive evaluation framework. The abstract lacks specific results, but the benchmark's establishment advances research in VLM knowledge editing.
- **核心贡献**: 提出了VLKEB基准，填补了VLM知识编辑评估的空白。
- **创新点**: 设计了覆盖多知识类型和编辑场景的评估框架。
- **结果**: 基准的建立为VLM知识编辑研究提供了统一评估平台。

### WikiDO: A New Benchmark Evaluating Cross-Modal Retrieval for Vision-Language Models. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/fe759454e97d56d3aea73a1512364d5f-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 2
- **作者**: Tankala Pavan Kalyan, Piyush Singh Pasi, Sahil Dharod, Azeem Motiwala, Preethi Jyothi, Aditi Chaudhary et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对视觉语言模型（VLM）在跨模态检索任务中缺乏专门基准的问题。②提出了WikiDO基准，用于评估VLM的跨模态检索能力。③相比现有基准，更专注于跨模态检索的细粒度评估。④摘要未提供具体数据，但基准的构建为VLM评估提供了新视角。
- **摘要（英）**: This paper addresses the lack of dedicated benchmarks for cross-modal retrieval in vision-language models. It introduces WikiDO, a new benchmark for evaluating such capabilities. Compared to existing benchmarks, it focuses on fine-grained cross-modal retrieval. Specific results are not detailed in the abstract.
- **核心贡献**: 提出了WikiDO基准，填补了跨模态检索评估的空白。
- **创新点**: 专注于跨模态检索的基准设计。
- **结果**: 基准构建完成，但未报告具体性能数据。

### ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b69396afc07a9ca3428d194f4db84c02-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 4
- **作者**: Shuo Liu, Kaining Ying, Hao Zhang, Yue Yang, Yuqi Lin, Tianle Zhang et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024
- **摘要（中）**: ①该论文针对大型视觉语言模型（VLM）多轮对话评估缺乏细粒度分析能力的问题。②提出了ConvBench，一个具有层次化消融能力的多轮对话评估基准。③相比已有基准，ConvBench支持对模型能力的层次化分解，便于定位性能瓶颈。④摘要未提供具体数据，但该基准有望提升VLM对话评估的准确性和可解释性。
- **摘要（英）**: This paper addresses the lack of fine-grained analysis in multi-turn conversation evaluation for large vision-language models (VLMs). It proposes ConvBench, a multi-turn conversation evaluation benchmark with hierarchical ablation capability. Compared to existing benchmarks, ConvBench enables hierarchical decomposition of model capabilities, facilitating bottleneck identification. The abstract lacks specific results, but the benchmark enhances evaluation accuracy and interpretability.
- **核心贡献**: 提出了ConvBench基准，支持多轮对话的层次化能力评估。
- **创新点**: 引入层次化消融机制，实现细粒度性能分析。
- **结果**: 基准的提出有望提升VLM对话评估的深度和可解释性。

### VLM4Bio: A Benchmark Dataset to Evaluate Pretrained Vision-Language Models for Trait Discovery from Biological Images. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2408.16176](https://arxiv.org/abs/2408.16176) · 📚 被引 2
- **作者**: M. Maruf, Arka Daw, Kazi Sajeed Mehrab, Harish Babu Manogaran, Abhilash Neog, Medha Sawhney et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①该论文针对预训练视觉语言模型（VLM）在生物图像性状发现中缺乏系统评估的问题。②提出了VLM4Bio数据集，包含469K问答对和30K图像，覆盖鱼类、鸟类和蝴蝶三类生物，涉及五个生物学任务，并评估了12个SOTA VLM的性能。③相比已有工作，该数据集专门针对生物多样性领域，提供了多任务、多物种的评估基准，并探索了提示技术和推理幻觉的影响。④实验揭示了当前VLM在生物问题回答中的能力边界，为领域应用提供了参考。
- **摘要（英）**: This paper addresses the lack of systematic evaluation of pretrained vision-language models (VLMs) for trait discovery from biological images. It introduces VLM4Bio, a dataset with 469K question-answer pairs and 30K images from fishes, birds, and butterflies, covering five biologically relevant tasks, and evaluates 12 state-of-the-art VLMs. Compared to existing work, it provides a domain-specific benchmark with multi-task and multi-species coverage, and explores prompting techniques and reasoning hallucination. Results reveal the capabilities and limitations of current VLMs in answering biological questions.
- **核心贡献**: 构建了VLM4Bio数据集，系统评估了12个VLM在生物性状发现任务中的表现。
- **创新点**: 针对生物多样性领域设计多任务基准，并分析提示和幻觉影响。
- **结果**: 揭示了VLM在生物图像问答中的能力边界，为后续优化提供依据。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Images are increasingly becoming the currency for documenting biodiversity on the planet, providing novel opportunities for accelerating scientific discoveries in the field of organismal biology, especially with the advent of large vision-language models (VLMs). We ask if pre-trained VLMs can aid scientists in answering a range of biologically relevant questions without any additional fine-tuning. In this paper, we evaluate the effectiveness of 12 state-of-the-art (SOTA) VLMs in the field of organismal biology using a novel dataset, VLM4Bio, consisting of 469K question-answer pairs involving 30K images from three groups of organisms: fishes, birds, and butterflies, covering five biologically relevant tasks. We also explore the effects of applying prompting techniques and tests for reasoning hallucination on the performance of VLMs, shedding new light on the capabilities of current SOTA VLMs in answering biologically relevant questions using images. The code and datasets for running all the analyses reported in this paper can be found at https://github.com/sammarfy/VLM4Bio.

</details>

### DevBench: A multimodal developmental benchmark for language learning. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2406.10215](https://arxiv.org/abs/2406.10215) · 📚 被引 1
- **作者**: Alvin Wei Ming Tan, Chunhua Yu, Bria Long, Wanjing Ma, Tonya Murray, Rebecca D. Silverman et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对视觉语言模型与儿童语言学习轨迹的相似性评估问题。②提出了DevBench多模态基准，包含七项语言任务，覆盖词汇、句法和语义能力，并与儿童和成人行为数据对比。③相比现有工作，直接比较模型与人类的行为模式，而不仅是准确率。④实验发现模型在不同任务上对人类响应模式的接近程度不同，且OpenCLIP训练越多越接近成人模式。
- **摘要（英）**: This paper addresses the similarity between vision-language models' and children's learning trajectories. It introduces DevBench, a multimodal benchmark with seven language tasks, comparing models to child and adult behavioral data. Unlike existing work, it compares response patterns, not just accuracy. Results show varying closeness to human patterns, with more training in OpenCLIP leading to closer adult approximations.
- **核心贡献**: 提出了DevBench基准，用于评估模型与人类语言学习轨迹的相似性。
- **创新点**: 直接对比模型与人类的行为响应模式。
- **结果**: 模型表现因任务而异，训练量增加更接近成人模式。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How (dis)similar are the learning trajectories of vision-language models and children? Recent modeling work has attempted to understand the gap between models' and humans' data efficiency by constructing models trained on less data, especially multimodal naturalistic data. However, such models are often evaluated on adult-level benchmarks, with limited breadth in language abilities tested, and without direct comparison to behavioral data. We introduce DevBench, a multimodal benchmark comprising seven language evaluation tasks spanning the domains of lexical, syntactic, and semantic ability, with behavioral data from both children and adults. We evaluate a set of vision-language models on these tasks, comparing models and humans not only on accuracy but on their response patterns. Across tasks, models exhibit variation in their closeness to human response patterns, and models that perform better on a task also more closely resemble human behavioral responses. We also examine the developmental trajectory of OpenCLIP over training, finding that greater training results in closer approximations to adult response patterns. DevBench thus provides a benchmark for comparing models to human language development. These comparisons highlight ways in which model and human language learning processes diverge, providing insight into entry points for improving language models.

</details>

### MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2406.14515](https://arxiv.org/abs/2406.14515) · 📚 被引 9
- **作者**: Xinyu Fang, Kangrui Mao, Haodong Duan, Xiangyu Zhao, Yining Li, Dahua Lin et al.
- **🏷️ 机构**: CUHK
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对传统视频问答基准无法全面评估模型时间理解能力的问题。②提出了MMBench-Video，一个包含长视频和自由形式问题的定量基准，采用GPT-4自动评估。③相比现有基准，覆盖了更全面的视频内容，并基于能力分类法进行人工标注。④评估了多个专有和开源模型，证明了基准的有效性和鲁棒性。
- **摘要（英）**: This paper addresses the limitations of traditional video QA benchmarks in assessing temporal comprehension. It introduces MMBench-Video, a quantitative benchmark with long videos and free-form questions, using GPT-4 for automated evaluation. Compared to existing benchmarks, it covers broader video content with human-annotated questions based on an ability taxonomy, and evaluates multiple models, demonstrating effectiveness and robustness.
- **核心贡献**: 提出了一个全面的长视频理解基准MMBench-Video。
- **创新点**: 采用GPT-4自动评估和基于能力分类法的人工标注。
- **结果**: 评估了多个模型，证明了基准的有效性和鲁棒性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of large vision-language models (LVLMs) has spurred research into their applications in multi-modal contexts, particularly in video understanding. Traditional VideoQA benchmarks, despite providing quantitative metrics, often fail to encompass the full spectrum of video content and inadequately assess models' temporal comprehension. To address these limitations, we introduce MMBench-Video, a quantitative benchmark designed to rigorously evaluate LVLMs' proficiency in video understanding. MMBench-Video incorporates lengthy videos from YouTube and employs free-form questions, mirroring practical use cases. The benchmark is meticulously crafted to probe the models' temporal reasoning skills, with all questions human-annotated according to a carefully constructed ability taxonomy. We employ GPT-4 for automated assessment, demonstrating superior accuracy and robustness over earlier LLM-based evaluations. Utilizing MMBench-Video, we have conducted comprehensive evaluations that include both proprietary and open-source LVLMs for images and videos. MMBench-Video stands as a valuable resource for the research community, facilitating improved evaluation of LVLMs and catalyzing progress in the field of video understanding. The evalutation code of MMBench-Video will be integrated into VLMEvalKit: https://github.com/open-compass/VLMEvalKit.

</details>

### Retrieval-Augmented Open-Vocabulary Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2404.05687](https://arxiv.org/abs/2404.05687) · 📚 被引 23
- **作者**: Jooyeon Kim, Eulrang Cho, Sehyung Kim, Hyunwoo J. Kim
- **🏷️ 机构**: Korea University,Department of Computer Science and Engineering, Samsung Research
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇目标检测中，现有方法仅利用正类伪标签和类名，忽略了负类信息和视觉特征增强。②提出了RALF，包含检索增强损失（RAL）和检索增强视觉特征（RAF），检索相关负类并利用LLM生成的概念增强视觉特征。③改进点在于引入负类语义和语言概念，提升模型对新颖类的泛化能力。④在COCO和LVIS上，COCO新颖类box AP50提升3.4，LVIS mask AP提升3.6。
- **摘要（英）**: This paper tackles open-vocabulary detection by proposing RALF, which retrieves negative classes for loss augmentation and uses LLM-generated verbalized concepts to enhance visual features. It improves generalization to novel categories, achieving up to +3.4 box AP50 on COCO and +3.6 mask AP on LVIS.
- **核心贡献**: 提出检索增强的损失和视觉特征，利用负类与语言概念提升OVD。
- **创新点**: 首次将负类检索和LLM概念融合到检测训练中。
- **结果**: COCO新颖类AP50提升3.4，LVIS mask AP提升3.6。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary object detection (OVD) has been studied with Vision-Language Models (VLMs) to detect novel objects beyond the pre-trained categories. Previous approaches improve the generalization ability to expand the knowledge of the detector, using 'positive' pseudo-labels with additional 'class' names, e.g., sock, iPod, and alligator. To extend the previous methods in two aspects, we propose Retrieval-Augmented Losses and visual Features (RALF). Our method retrieves related 'negative' classes and augments loss functions. Also, visual features are augmented with 'verbalized concepts' of classes, e.g., worn on the feet, handheld music player, and sharp teeth. Specifically, RALF consists of two modules: Retrieval Augmented Losses (RAL) and Retrieval-Augmented visual Features (RAF). RAL constitutes two losses reflecting the semantic similarity with negative vocabularies. In addition, RAF augments visual features with the verbalized concepts from a large language model (LLM). Our experiments demonstrate the effectiveness of RALF on COCO and LVIS benchmark datasets. We achieve improvement up to 3.4 box AP$_{50}^{\text{N}}$ on novel categories of the COCO dataset and 3.6 mask AP$_{\text{r}}$ gains on the LVIS dataset. Code is available at https://github.com/mlvlab/RALF .

</details>

### The Devil is in the Fine-Grained Details: Evaluating open-Vocabulary Object Detectors for Fine-Grained Understanding. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2311.17518](https://arxiv.org/abs/2311.17518) · 📚 被引 16
- **作者**: Lorenzo Bianchi, Fabio Carrara, Nicola Messina, Claudio Gennaro, Fabrizio Falchi
- **🏷️ 机构**: CNR-ISTI,Pisa,Italy
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇目标检测器在细粒度属性（如颜色、图案、材质）理解上的不足，本文提出了一种基于动态词汇生成的评估协议，通过引入硬负类来测试模型是否能够检测、区分并正确分配细粒度描述。作者构建了难度递增的基准套件，并评估了多个SOTA开放词汇检测器，发现它们在标准基准上表现优异，但在细粒度细节上普遍失败。该工作揭示了现有方法的局限性，并指出了未来研究方向。
- **摘要（英）**: This paper addresses the fine-grained understanding gap in open-vocabulary object detectors by introducing a dynamic vocabulary-based evaluation protocol with hard-negative classes. It benchmarks multiple SOTA detectors on a suite of increasing difficulty, revealing that they struggle with fine-grained attributes like color, pattern, and material. The findings highlight limitations and suggest promising research directions.
- **核心贡献**: 提出了首个针对开放词汇检测器细粒度理解的动态评估协议和基准套件。
- **创新点**: 通过动态生成硬负类词汇，系统性地测试模型对细粒度属性的区分能力。
- **结果**: 多个SOTA检测器在细粒度基准上性能显著下降，表明现有方法缺乏精细理解能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in large vision-language models enabled visual object detection in open-vocabulary scenarios, where object classes are defined in free-text formats during inference. In this paper, we aim to probe the state-of-the-art methods for open-vocabulary object detection to determine to what extent they understand fine-grained properties of objects and their parts. To this end, we introduce an evaluation protocol based on dynamic vocabulary generation to test whether models detect, discern, and assign the correct fine-grained description to objects in the presence of hard-negative classes. We contribute with a benchmark suite of increasing difficulty and probing different properties like color, pattern, and material. We further enhance our investigation by evaluating several state-of-the-art open-vocabulary object detectors using the proposed protocol and find that most existing solutions, which shine in standard open-vocabulary benchmarks, struggle to accurately capture and distinguish finer object details. We conclude the paper by highlighting the limitations of current methodologies and exploring promising research directions to overcome the discovered drawbacks. Data and code are available at https://lorebianchi98.github.io/FG-OVD/.

</details>

### From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models.
- **链接**: [arXiv:2404.00906](https://arxiv.org/abs/2404.00906) · 📚 被引 51
- **作者**: Rongjie Li, Songyang Zhang, Dahua Lin, Kai Chen, Xuming He
- **🏷️ 机构**: School of Information Science and Technology, ShanghaiTech University, Shanghai AI Laboratory
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scene graph generation (SGG) aims to parse a visual scene into an intermediate graph representation for downstream reasoning tasks. Despite recent advancements, existing methods struggle to generate scene graphs with novel visual relation concepts. To address this challenge, we introduce a new open-vocabulary SGG framework based on sequence generation. Our framework leverages vision-language pre-trained models (VLM) by incorporating an image-to-graph generation paradigm. Specifically, we generate scene graph sequences via image-to-text generation with VLM and then construct scene graphs from these sequences. By doing so, we harness the strong capabilities of VLM for open-vocabulary SGG and seamlessly integrate explicit relational modeling for enhancing the VL tasks. Experimental results demonstrate that our design not only achieves superior performance with an open vocabulary but also enhances downstream vision-language task performance through explicit relation modeling knowledge.

</details>

### Emergent Open-Vocabulary Semantic Segmentation from Off-the-Shelf Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00386) · 📚 被引 16
- **作者**: Jiayun Luo, Siddhesh Khandelwal, Leonid Sigal, Boyang Li
- **🏷️ 机构**: Nanyang Technological University,Singapore, University of British Columbia, Vector Institute for AI,Canada
- **会议**: CVPR 2024

### OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual Representation.
- **链接**: [arXiv:2404.01409](https://arxiv.org/abs/2404.01409) · 📚 被引 10
- **作者**: Xiongwei Wu, Sicheng Yu, Ee-Peng Lim, Chong-Wah Ngo
- **🏷️ 机构**: Singapore Management University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of food computing, segmenting ingredients from images poses substantial challenges due to the large intra-class variance among the same ingredients, the emergence of new ingredients, and the high annotation costs associated with large food segmentation datasets. Existing approaches primarily utilize a closed-vocabulary and static text embeddings setting. These methods often fall short in effectively handling the ingredients, particularly new and diverse ones. In response to these limitations, we introduce OVFoodSeg, a framework that adopts an open-vocabulary setting and enhances text embeddings with visual context. By integrating vision-language models (VLMs), our approach enriches text embedding with image-specific information through two innovative modules, eg, an image-to-text learner FoodLearner and an Image-Informed Text Encoder. The training process of OVFoodSeg is divided into two stages: the pre-training of FoodLearner and the subsequent learning phase for segmentation. The pre-training phase equips FoodLearner with the capability to align visual information with corresponding textual representations that are specifically related to food, while the second phase adapts both the FoodLearner and the Image-Informed Text Encoder for the segmentation task. By addressing the deficiencies of previous models, OVFoodSeg demonstrates a significant improvement, achieving an 4.9\% increase in mean Intersection over Union (mIoU) on the FoodSeg103 dataset, setting a new milestone for food image segmentation.

</details>

### SED: A Simple Encoder-Decoder for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2311.15537](https://arxiv.org/abs/2311.15537) · 📚 被引 90
- **作者**: Bin Xie, Jiale Cao, Jin Xie, Fahad Shahbaz Khan, Yanwei Pang
- **🏷️ 机构**: Tianjin University, Chongqing University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation strives to distinguish pixels into different semantic groups from an open set of categories. Most existing methods explore utilizing pre-trained vision-language models, in which the key is to adopt the image-level model for pixel-level segmentation task. In this paper, we propose a simple encoder-decoder, named SED, for open-vocabulary semantic segmentation, which comprises a hierarchical encoder-based cost map generation and a gradual fusion decoder with category early rejection. The hierarchical encoder-based cost map generation employs hierarchical backbone, instead of plain transformer, to predict pixel-level image-text cost map. Compared to plain transformer, hierarchical backbone better captures local spatial information and has linear computational complexity with respect to input size. Our gradual fusion decoder employs a top-down structure to combine cost map and the feature maps of different backbone levels for segmentation. To accelerate inference speed, we introduce a category early rejection scheme in the decoder that rejects many no-existing categories at the early layer of decoder, resulting in at most 4.7 times acceleration without accuracy degradation. Experiments are performed on multiple open-vocabulary semantic segmentation datasets, which demonstrates the efficacy of our SED method. When using ConvNeXt-B, our SED method achieves mIoU score of 31.6\% on ADE20K with 150 categories at 82 millisecond ($ms$) per image on a single A6000. We will release it at \url{https://github.com/xb534/SED.git}.

</details>

### DeIL: Direct-and-Inverse CLIP for Open-World Few-Shot Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02693) · 📚 被引 15
- **作者**: Shuai Shao, Yu Bai, Yan Wang, Baodi Liu, Yicong Zhou
- **🏷️ 机构**: Zhejiang Lab, China University of Petroleum (East China), Beihang University
- **会议**: CVPR 2024

### Towards Better Vision-Inspired Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01285) · 📚 被引 6
- **作者**: Yun-Hao Cao, Kaixiang Ji, Ziyuan Huang, Chuanyang Zheng, Jiajia Liu, Jian Wang et al.
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology, Ant Group
- **会议**: CVPR 2024

### DRESS : Instructing Large Vision-Language Models to Align and Interact with Humans via Natural Language Feedback.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01350) · 📚 被引 21
- **作者**: Yangyi Chen, Karan Sikka, Michael Cogswell, Heng Ji, Ajay Divakaran
- **🏷️ 机构**: SRI International, University of Illinois Urbana-Champaign
- **会议**: CVPR 2024

### Hallusionbench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01363) · 📚 被引 144
- **作者**: Tianrui Guan, Fuxiao Liu, Xiyang Wu, Ruiqi Xian, Zongxia Li, Xiaoyu Liu et al.
- **🏷️ 机构**: University of Maryland,College Park
- **会议**: CVPR 2024

### Language Models as Black-Box Optimizers for Vision-Language Models.
- **链接**: [arXiv:2309.05950](https://arxiv.org/abs/2309.05950) · 📚 被引 22
- **作者**: Shihong Liu, Samuel Yu, Zhiqiu Lin, Deepak Pathak, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) pre-trained on web-scale datasets have demonstrated remarkable capabilities on downstream tasks when fine-tuned with minimal data. However, many VLMs rely on proprietary data and are not open-source, which restricts the use of white-box approaches for fine-tuning. As such, we aim to develop a black-box approach to optimize VLMs through natural language prompts, thereby avoiding the need to access model parameters, feature embeddings, or even output logits. We propose employing chat-based LLMs to search for the best text prompt for VLMs. Specifically, we adopt an automatic hill-climbing procedure that converges to an effective prompt by evaluating the performance of current prompts and asking LLMs to refine them based on textual feedback, all within a conversational process without human-in-the-loop. In a challenging 1-shot image classification setup, our simple approach surpasses the white-box continuous prompting method (CoOp) by an average of 1.5% across 11 datasets including ImageNet. Our approach also outperforms both human-engineered and LLM-generated prompts. We highlight the advantage of conversational feedback that incorporates both positive and negative prompts, suggesting that LLMs can utilize the implicit gradient direction in textual feedback for a more efficient search. In addition, we find that the text prompts generated through our strategy are not only more interpretable but also transfer well across different VLM architectures in a black-box manner. Lastly, we apply our framework to optimize the state-of-the-art black-box VLM (DALL-E 3) for text-to-image generation, prompt inversion, and personalization.

</details>

### Sonic VisionLM: Playing Sound with Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02537) · 📚 被引 16
- **作者**: Zhifeng Xie, Shengye Yu, Qile He, Mengtian Li
- **🏷️ 机构**: Shanghai University
- **会议**: CVPR 2024

### Consistency and Uncertainty: Identifying Unreliable Responses From Black-Box Vision-Language Models for Selective Visual Question Answering.
- **链接**: [arXiv:2404.10193](https://arxiv.org/abs/2404.10193) · 📚 被引 21
- **作者**: Zaid Khan, Yun Fu
- **🏷️ 机构**: Northeastern University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of selective prediction is to allow an a model to abstain when it may not be able to deliver a reliable prediction, which is important in safety-critical contexts. Existing approaches to selective prediction typically require access to the internals of a model, require retraining a model or study only unimodal models. However, the most powerful models (e.g. GPT-4) are typically only available as black boxes with inaccessible internals, are not retrainable by end-users, and are frequently used for multimodal tasks. We study the possibility of selective prediction for vision-language models in a realistic, black-box setting. We propose using the principle of \textit{neighborhood consistency} to identify unreliable responses from a black-box vision-language model in question answering tasks. We hypothesize that given only a visual question and model response, the consistency of the model's responses over the neighborhood of a visual question will indicate reliability. It is impossible to directly sample neighbors in feature space in a black-box setting. Instead, we show that it is possible to use a smaller proxy model to approximately sample from the neighborhood. We find that neighborhood consistency can be used to identify model responses to visual questions that are likely unreliable, even in adversarial settings or settings that are out-of-distribution to the proxy model.

</details>

### PeVL: Pose-Enhanced Vision-Language Model for Fine-Grained Human Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01784) · 📚 被引 12
- **作者**: Haosong Zhang, Mei Chee Leong, Liyuan Li, Weisi Lin
- **🏷️ 机构**: Institute for Infocomm Research (I2R), A *STAR,Singapore, Nanyang Technological University,Singapore
- **会议**: CVPR 2024

### Dual Memory Networks: A Versatile Adaptation Approach for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02713) · 📚 被引 43
- **作者**: Yabin Zhang, Wenjie Zhu, Hui Tang, Zhiyuan Ma, Kaiyang Zhou, Lei Zhang
- **🏷️ 机构**: HKPolyU, HKUST, HKBU
- **会议**: CVPR 2024

### SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01370) · 📚 被引 225
- **作者**: Boyuan Chen, Zhuo Xu, Sean Kirmani, Brian Ichter, Dorsa Sadigh, Leonidas J. Guibas et al.
- **🏷️ 机构**: Google DeepMind, Google Research
- **会议**: CVPR 2024

### Distilling Vision-Language Models on Millions of Videos.
- **链接**: [arXiv:2401.06129](https://arxiv.org/abs/2401.06129) · 📚 被引 10
- **作者**: Yue Zhao, Long Zhao, Xingyi Zhou, Jialin Wu, Chun-Te Chu, Hui Miao et al.
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent advance in vision-language models is largely attributed to the abundance of image-text data. We aim to replicate this success for video-language models, but there simply is not enough human-curated video-text data available. We thus resort to fine-tuning a video-language model from a strong image-language baseline with synthesized instructional data. The resulting video model by video-instruction-tuning (VIIT) is then used to auto-label millions of videos to generate high-quality captions. We show the adapted video-language model performs well on a wide range of video-language benchmarks. For instance, it surpasses the best prior result on open-ended NExT-QA by 2.8%. Besides, our model generates detailed descriptions for previously unseen videos, which provide better textual supervision than existing methods. Experiments show that a video-language dual-encoder model contrastively trained on these auto-generated captions is 3.8% better than the strongest baseline that also leverages vision-language models. Our best model outperforms state-of-the-art methods on MSR-VTT zero-shot text-to-video retrieval by 6%. As a side product, we generate the largest video caption dataset to date.

</details>

### Leveraging Vision-Language Models for Improving Domain Generalization in Image Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02258) · 📚 被引 32
- **作者**: Sravanti Addepalli, Ashish Ramayee Asokan, Lakshay Sharma, R. Venkatesh Babu
- **🏷️ 机构**: Indian Institute of Science,Vision and AI Lab,Bangalore
- **会议**: CVPR 2024

### Active Prompt Learning in Vision Language Models.
- **链接**: [arXiv:2311.11178](https://arxiv.org/abs/2311.11178) · 📚 被引 9
- **作者**: Jihwan Bang, Sumyeong Ahn, Jae-Gil Lee
- **🏷️ 机构**: KAIST Michigan, State University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained Vision Language Models (VLMs) have demonstrated notable progress in various zero-shot tasks, such as classification and retrieval. Despite their performance, because improving performance on new tasks requires task-specific knowledge, their adaptation is essential. While labels are needed for the adaptation, acquiring them is typically expensive. To overcome this challenge, active learning, a method of achieving a high performance by obtaining labels for a small number of samples from experts, has been studied. Active learning primarily focuses on selecting unlabeled samples for labeling and leveraging them to train models. In this study, we pose the question, "how can the pre-trained VLMs be adapted under the active learning framework?" In response to this inquiry, we observe that (1) simply applying a conventional active learning framework to pre-trained VLMs even may degrade performance compared to random selection because of the class imbalance in labeling candidates, and (2) the knowledge of VLMs can provide hints for achieving the balance before labeling. Based on these observations, we devise a novel active learning framework for VLMs, denoted as PCB. To assess the effectiveness of our approach, we conduct experiments on seven different real-world datasets, and the results demonstrate that PCB surpasses conventional active learning and random sampling methods. Code will be available in https://github.com/kaist-dmlab/pcb .

</details>

### FFF: Fixing Flawed Foundations in contrastive pre-training results in very strong Vision-Language models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01344) · 📚 被引 8
- **作者**: Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
- **🏷️ 机构**: Samsung AI Center Cambridge,UK
- **会议**: CVPR 2024

### PracticalDG: Perturbation Distillation on Vision-Language Models for Hybrid Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02218) · 📚 被引 19
- **作者**: Zining Chen, Weiqiu Wang, Zhicheng Zhao, Fei Su, Aidong Men, Hongying Meng
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,The school of Artificial Intelligence, Brunel University Uxbridge
- **会议**: CVPR 2024

### EgoThink: Evaluating First-Person Perspective Thinking Capability of Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01355) · 📚 被引 26
- **作者**: Sijie Cheng, Zhicheng Guo, Jingwen Wu, Kechen Fang, Peng Li, Huaping Liu et al.
- **🏷️ 机构**: Tsinghua University,Department of Computer Science and Technology, University of Toronto,Department of Electrical and Computer Engineering, Tsinghua University,Zhili College
- **会议**: CVPR 2024

### JoAPR: Cleaning the Lens of Prompt Learning for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02711) · 📚 被引 6
- **作者**: Yuncheng Guo, Xiaodong Gu
- **🏷️ 机构**: Fudan University,Department of Electronic Engineering,Shanghai,China,200438
- **会议**: CVPR 2024

### RegionGPT: Towards Region Understanding Vision Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01309) · 📚 被引 54
- **作者**: Qiushan Guo, Shalini De Mello, Hongxu Yin, Wonmin Byeon, Ka Chun Cheung, Yizhou Yu et al.
- **🏷️ 机构**: The University of Hong Kong, NVIDIA
- **会议**: CVPR 2024

### Anchor-based Robust Finetuning of Vision-Language Models.
- **链接**: [arXiv:2404.06244](https://arxiv.org/abs/2404.06244) · 📚 被引 6
- **作者**: Jinwei Han, Zhiwen Lin, Zhongyisun Sun, Yingguo Gao, Ke Yan, Shouhong Ding et al.
- **🏷️ 机构**: School of Computer Science, Wuhan University, YouTu Lab, Tencent, Electronic Information School, Wuhan University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We aim at finetuning a vision-language model without hurting its out-of-distribution (OOD) generalization. We address two types of OOD generalization, i.e., i) domain shift such as natural to sketch images, and ii) zero-shot capability to recognize the category that was not contained in the finetune data. Arguably, the diminished OOD generalization after finetuning stems from the excessively simplified finetuning target, which only provides the class information, such as ``a photo of a [CLASS]''. This is distinct from the process in that CLIP was pretrained, where there is abundant text supervision with rich semantic information. Therefore, we propose to compensate for the finetune process using auxiliary supervision with rich semantic information, which acts as anchors to preserve the OOD generalization. Specifically, two types of anchors are elaborated in our method, including i) text-compensated anchor which uses the images from the finetune set but enriches the text supervision from a pretrained captioner, ii) image-text-pair anchor which is retrieved from the dataset similar to pretraining data of CLIP according to the downstream task, associating with the original CLIP text with rich semantics. Those anchors are utilized as auxiliary semantic information to maintain the original feature space of CLIP, thereby preserving the OOD generalization capabilities. Comprehensive experiments demonstrate that our method achieves in-distribution performance akin to conventional finetuning while attaining new state-of-the-art results on domain shift and zero-shot learning benchmarks.

</details>

### SocialCounterfactuals: Probing and Mitigating Intersectional Social Biases in Vision-Language Models with Counterfactual Examples.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01138) · 📚 被引 15
- **作者**: Phillip Howard, Avinash Madasu, Tiep Le, Gustavo A. Lujan-Moreno, Anahita Bhiwandiwalla, Vasudev Lal
- **🏷️ 机构**: Intel Labs
- **会议**: CVPR 2024

### Visual Program Distillation: Distilling Tools and Programmatic Reasoning into Vision-Language Models.
- **链接**: [arXiv:2312.03052](https://arxiv.org/abs/2312.03052) · 📚 被引 38
- **作者**: Yushi Hu, Otilia Stretcu, Chun-Ta Lu, Krishnamurthy Viswanathan, Kenji Hata, Enming Luo et al.
- **🏷️ 机构**: Google Research, University of Washington
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Solving complex visual tasks such as "Who invented the musical instrument on the right?" involves a composition of skills: understanding space, recognizing instruments, and also retrieving prior knowledge. Recent work shows promise by decomposing such tasks using a large language model (LLM) into an executable program that invokes specialized vision models. However, generated programs are error-prone: they omit necessary steps, include spurious ones, and are unable to recover when the specialized models give incorrect outputs. Moreover, they require loading multiple models, incurring high latency and computation costs. We propose Visual Program Distillation (VPD), an instruction tuning framework that produces a vision-language model (VLM) capable of solving complex visual tasks with a single forward pass. VPD distills the reasoning ability of LLMs by using them to sample multiple candidate programs, which are then executed and verified to identify a correct one. It translates each correct program into a language description of the reasoning steps, which are then distilled into a VLM. Extensive experiments show that VPD improves the VLM's ability to count, understand spatial relations, and reason compositionally. Our VPD-trained PaLI-X outperforms all prior VLMs, achieving state-of-the-art performance across complex vision tasks, including MMBench, OK-VQA, A-OKVQA, TallyQA, POPE, and Hateful Memes. An evaluation with human annotators also confirms that VPD improves model response factuality and consistency. Finally, experiments on content moderation demonstrate that VPD is also helpful for adaptation to real-world applications with limited data.

</details>

### Semantic Shield: Defending Vision-Language Models Against Backdooring and Poisoning via Fine-Grained Knowledge Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02344) · 📚 被引 3
- **作者**: Alvi Md. Ishmam, Christopher Thomas
- **🏷️ 机构**: Virginia Tech
- **会议**: CVPR 2024

### Efficient Test-Time Adaptation of Vision-Language Models.
- **链接**: [arXiv:2403.18293](https://arxiv.org/abs/2403.18293)
- **作者**: Adilbek Karmanov, Dayan Guan, Shijian Lu, Abdulmotaleb El Saddik, Eric P. Xing
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation with pre-trained vision-language models has attracted increasing attention for tackling distribution shifts during the test time. Though prior studies have achieved very promising performance, they involve intensive computation which is severely unaligned with test-time adaptation. We design TDA, a training-free dynamic adapter that enables effective and efficient test-time adaptation with vision-language models. TDA works with a lightweight key-value cache that maintains a dynamic queue with few-shot pseudo labels as values and the corresponding test-sample features as keys. Leveraging the key-value cache, TDA allows adapting to test data gradually via progressive pseudo label refinement which is super-efficient without incurring any backpropagation. In addition, we introduce negative pseudo labeling that alleviates the adverse impact of pseudo label noises by assigning pseudo labels to certain negative classes when the model is uncertain about its pseudo label predictions. Extensive experiments over two benchmarks demonstrate TDA's superior effectiveness and efficiency as compared with the state-of-the-art. The code has been released in \url{https://kdiaaa.github.io/tda/}.

</details>

### Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding.
- **链接**: [arXiv:2311.16922](https://arxiv.org/abs/2311.16922) · 📚 被引 184
- **作者**: Sicong Leng, Hang Zhang, Guanzheng Chen, Xin Li, Shijian Lu, Chunyan Miao et al.
- **🏷️ 机构**: DAMO Academy, Alibaba Group, Nanyang Technological University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) have advanced considerably, intertwining visual recognition and language understanding to generate content that is not only coherent but also contextually attuned. Despite their success, LVLMs still suffer from the issue of object hallucinations, where models generate plausible yet incorrect outputs that include objects that do not exist in the images. To mitigate this issue, we introduce Visual Contrastive Decoding (VCD), a simple and training-free method that contrasts output distributions derived from original and distorted visual inputs. The proposed VCD effectively reduces the over-reliance on statistical bias and unimodal priors, two essential causes of object hallucinations. This adjustment ensures the generated content is closely grounded to visual inputs, resulting in contextually accurate outputs. Our experiments show that VCD, without either additional training or the usage of external tools, significantly mitigates the object hallucination issue across different LVLM families. Beyond mitigating object hallucinations, VCD also excels in general LVLM benchmarks, highlighting its wide-ranging applicability.

</details>

### One Prompt Word is Enough to Boost Adversarial Robustness for Pre-Trained Vision-Language Models.
- **链接**: [arXiv:2403.01849](https://arxiv.org/abs/2403.01849) · 📚 被引 33
- **作者**: Lin Li, Haoyan Guan, Jianing Qiu, Michael W. Spratling
- **🏷️ 机构**: King&#x0027;s College,London, Imperial College,London
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large pre-trained Vision-Language Models (VLMs) like CLIP, despite having remarkable generalization ability, are highly vulnerable to adversarial examples. This work studies the adversarial robustness of VLMs from the novel perspective of the text prompt instead of the extensively studied model weights (frozen in this work). We first show that the effectiveness of both adversarial attack and defense are sensitive to the used text prompt. Inspired by this, we propose a method to improve resilience to adversarial attacks by learning a robust text prompt for VLMs. The proposed method, named Adversarial Prompt Tuning (APT), is effective while being both computationally and data efficient. Extensive experiments are conducted across 15 datasets and 4 data sparsity schemes (from 1-shot to full training data settings) to show APT's superiority over hand-engineered prompts and other state-of-the-art adaption methods. APT demonstrated excellent abilities in terms of the in-distribution performance and the generalization under input distribution shift and across datasets. Surprisingly, by simply adding one learned word to the prompts, APT can significantly boost the accuracy and robustness (epsilon=4/255) over the hand-engineered prompts by +13% and +8.5% on average respectively. The improvement further increases, in our most effective setting, to +26.4% for accuracy and +16.7% for robustness. Code is available at https://github.com/TreeLLi/APT.

</details>

### PromptKD: Unsupervised Prompt Distillation for Vision-Language Models.
- **链接**: [arXiv:2403.02781](https://arxiv.org/abs/2403.02781) · 📚 被引 110
- **作者**: Zheng Li, Xiang Li, Xinyi Fu, Xin Zhang, Weiqiang Wang, Shuo Chen et al.
- **🏷️ 机构**: College of Computer Science, Nankai University,PCA Lab, VCIP, NKIARI,Shenzhen Futian, Ant Group,Tiansuan Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning has emerged as a valuable technique in enhancing vision-language models (VLMs) such as CLIP for downstream tasks in specific domains. Existing work mainly focuses on designing various learning forms of prompts, neglecting the potential of prompts as effective distillers for learning from larger teacher models. In this paper, we introduce an unsupervised domain prompt distillation framework, which aims to transfer the knowledge of a larger teacher model to a lightweight target model through prompt-driven imitation using unlabeled domain images. Specifically, our framework consists of two distinct stages. In the initial stage, we pre-train a large CLIP teacher model using domain (few-shot) labels. After pre-training, we leverage the unique decoupled-modality characteristics of CLIP by pre-computing and storing the text features as class vectors only once through the teacher text encoder. In the subsequent stage, the stored class vectors are shared across teacher and student image encoders for calculating the predicted logits. Further, we align the logits of both the teacher and student models via KL divergence, encouraging the student image encoder to generate similar probability distributions to the teacher through the learnable prompts. The proposed prompt distillation process eliminates the reliance on labeled data, enabling the algorithm to leverage a vast amount of unlabeled images within the domain. Finally, the well-trained student image encoders and pre-stored text features (class vectors) are utilized for inference. To our best knowledge, we are the first to (1) perform unsupervised domain-specific prompt-driven knowledge distillation for CLIP, and (2) establish a practical pre-storing mechanism of text features as shared class vectors between teacher and student. Extensive experiments on 11 datasets demonstrate the effectiveness of our method.

</details>

### MoPE-CLIP: Structured Pruning for Efficient Vision-Language Models with Module-Wise Pruning Error Metric.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02584) · 📚 被引 21
- **作者**: Haokun Lin, Haoli Bai, Zhili Liu, Lu Hou, Muyi Sun, Linqi Song et al.
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences, Huawei Noah&#x0027;s Ark Lab, Institute of Automation, Chinese Academy of Sciences,CRIPAC &#x0026; MAIS
- **会议**: CVPR 2024

### Volumetric Environment Representation for Vision-Language Navigation.
- **链接**: [arXiv:2403.14158](https://arxiv.org/abs/2403.14158) · 📚 被引 43
- **作者**: Rui Liu, Wenguan Wang, Yi Yang
- **🏷️ 机构**: Zhejiang University,ReLER, CCAI
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

</details>

### FairCLIP: Harnessing Fairness in Vision-Language Learning.
- **链接**: [arXiv:2403.19949](https://arxiv.org/abs/2403.19949) · 📚 被引 53
- **作者**: Yan Luo, Min Shi, Muhammad Osama Khan, Muhammad Muneeb Afzal, Hao Huang, Shuaihang Yuan et al.
- **🏷️ 机构**: Harvard University,Harvard Ophthalmology AI Lab, Tandon School of Engineering, New York University, New York University Abu Dhabi,Multimedia and Visual Computing Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fairness is a critical concern in deep learning, especially in healthcare, where these models influence diagnoses and treatment decisions. Although fairness has been investigated in the vision-only domain, the fairness of medical vision-language (VL) models remains unexplored due to the scarcity of medical VL datasets for studying fairness. To bridge this research gap, we introduce the first fair vision-language medical dataset Harvard-FairVLMed that provides detailed demographic attributes, ground-truth labels, and clinical notes to facilitate an in-depth examination of fairness within VL foundation models. Using Harvard-FairVLMed, we conduct a comprehensive fairness analysis of two widely-used VL models (CLIP and BLIP2), pre-trained on both natural and medical domains, across four different protected attributes. Our results highlight significant biases in all VL models, with Asian, Male, Non-Hispanic, and Spanish being the preferred subgroups across the protected attributes of race, gender, ethnicity, and language, respectively. In order to alleviate these biases, we propose FairCLIP, an optimal-transport-based approach that achieves a favorable trade-off between performance and fairness by reducing the Sinkhorn distance between the overall sample distribution and the distributions corresponding to each demographic group. As the first VL dataset of its kind, Harvard-FairVLMed holds the potential to catalyze advancements in the development of machine learning models that are both ethically aware and clinically effective. Our dataset and code are available at https://ophai.hms.harvard.edu/datasets/harvard-fairvlmed10k.

</details>

### The Neglected Tails in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01234) · 📚 被引 31
- **作者**: Shubham Parashar, Zhiqiu Lin, Tian Liu, Xiangjue Dong, Yanan Li, Deva Ramanan et al.
- **🏷️ 机构**: Texas A&#x0026;M University, Carnegie Mellon University, Zhejiang Lab
- **会议**: CVPR 2024

### Jack of All Tasks, Master of Many: Designing General-purpose Coarse-to-Fine Vision-Language Model.
- **链接**: [arXiv:2312.12423](https://arxiv.org/abs/2312.12423) · 📚 被引 25
- **作者**: Shraman Pramanick, Guangxing Han, Rui Hou, Sayan Nag, Ser-Nam Lim, Nicolas Ballas et al.
- **🏷️ 机构**: Johns Hopkins University, Meta, University of Toronto
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability of large language models (LLMs) to process visual inputs has given rise to general-purpose vision systems, unifying various vision-language (VL) tasks by instruction tuning. However, due to the enormous diversity in input-output formats in the vision domain, existing general-purpose models fail to successfully integrate segmentation and multi-image inputs with coarse-level tasks into a single framework. In this work, we introduce VistaLLM, a powerful visual system that addresses coarse- and fine-grained VL tasks over single and multiple input images using a unified framework. VistaLLM utilizes an instruction-guided image tokenizer that filters global embeddings using task descriptions to extract compressed and refined features from numerous images. Moreover, VistaLLM employs a gradient-aware adaptive sampling technique to represent binary segmentation masks as sequences, significantly improving over previously used uniform sampling. To bolster the desired capability of VistaLLM, we curate CoinIt, a comprehensive coarse-to-fine instruction tuning dataset with 6.8M samples. We also address the lack of multi-image grounding datasets by introducing a novel task, AttCoSeg (Attribute-level Co-Segmentation), which boosts the model's reasoning and grounding capability over multiple input images. Extensive experiments on a wide range of V- and VL tasks demonstrate the effectiveness of VistaLLM by achieving consistent state-of-the-art performance over strong baselines across all downstream tasks. Our project page can be found at https://shramanpramanick.github.io/VistaLLM/.

</details>

### Building Vision-Language Models on Solid Foundations with Masked Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01348) · 📚 被引 8
- **作者**: Sepehr Sameni, Kushal Kafle, Hao Tan, Simon Jenni
- **🏷️ 机构**: University of Bern, Adobe Research
- **会议**: CVPR 2024

### Non-autoregressive Sequence-to-Sequence Vision-Language Models.
- **链接**: [arXiv:2403.02249](https://arxiv.org/abs/2403.02249) · 📚 被引 2
- **作者**: Kunyu Shi, Qi Dong, Luis Goncalves, Zhuowen Tu, Stefano Soatto
- **🏷️ 机构**: AWS AI Labs
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sequence-to-sequence vision-language models are showing promise, but their applicability is limited by their inference latency due to their autoregressive way of generating predictions. We propose a parallel decoding sequence-to-sequence vision-language model, trained with a Query-CTC loss, that marginalizes over multiple inference paths in the decoder. This allows us to model the joint distribution of tokens, rather than restricting to conditional distribution as in an autoregressive model. The resulting model, NARVL, achieves performance on-par with its state-of-the-art autoregressive counterpart, but is faster at inference time, reducing from the linear complexity associated with the sequential generation of tokens to a paradigm of constant time joint inference.

</details>

### A Closer Look at the Few-Shot Adaptation of Large Vision-Language Models.
- **链接**: [arXiv:2312.12730](https://arxiv.org/abs/2312.12730) · 📚 被引 50
- **作者**: Julio Silva-Rodríguez, Sina Hajimiri, Ismail Ben Ayed, Jose Dolz
- **🏷️ 机构**: &#x00E9;TS Montreal
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient transfer learning (ETL) is receiving increasing attention to adapt large pre-trained language-vision models on downstream tasks with a few labeled samples. While significant progress has been made, we reveal that state-of-the-art ETL approaches exhibit strong performance only in narrowly-defined experimental setups, and with a careful adjustment of hyperparameters based on a large corpus of labeled samples. In particular, we make two interesting, and surprising empirical observations. First, to outperform a simple Linear Probing baseline, these methods require to optimize their hyper-parameters on each target task. And second, they typically underperform -- sometimes dramatically -- standard zero-shot predictions in the presence of distributional drifts. Motivated by the unrealistic assumptions made in the existing literature, i.e., access to a large validation set and case-specific grid-search for optimal hyperparameters, we propose a novel approach that meets the requirements of real-world scenarios. More concretely, we introduce a CLass-Adaptive linear Probe (CLAP) objective, whose balancing term is optimized via an adaptation of the general Augmented Lagrangian method tailored to this context. We comprehensively evaluate CLAP on a broad span of datasets and scenarios, demonstrating that it consistently outperforms SoTA approaches, while yet being a much more efficient alternative.

</details>

### SyncMask: Synchronized Attentional Masking for Fashion-centric Vision-Language Pretraining.
- **链接**: [arXiv:2404.01156](https://arxiv.org/abs/2404.01156) · 📚 被引 14
- **作者**: Chull Hwan Song, Taebaek Hwang, Jooyoung Yoon, Shunghyun Choi, Yeong Hyeon Gu
- **🏷️ 机构**: Dealicious Inc., Sejong University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have made significant strides in cross-modal understanding through large-scale paired datasets. However, in fashion domain, datasets often exhibit a disparity between the information conveyed in image and text. This issue stems from datasets containing multiple images of a single fashion item all paired with one text, leading to cases where some textual details are not visible in individual images. This mismatch, particularly when non-co-occurring elements are masked, undermines the training of conventional VLM objectives like Masked Language Modeling and Masked Image Modeling, thereby hindering the model's ability to accurately align fine-grained visual and textual features. Addressing this problem, we propose Synchronized attentional Masking (SyncMask), which generate masks that pinpoint the image patches and word tokens where the information co-occur in both image and text. This synchronization is accomplished by harnessing cross-attentional features obtained from a momentum model, ensuring a precise alignment between the two modalities. Additionally, we enhance grouped batch sampling with semi-hard negatives, effectively mitigating false negative issues in Image-Text Matching and Image-Text Contrastive learning objectives within fashion datasets. Our experiments demonstrate the effectiveness of the proposed approach, outperforming existing methods in three downstream tasks.

</details>

### Label Propagation for Zero-shot Classification with Vision-Language Models.
- **链接**: [arXiv:2404.04072](https://arxiv.org/abs/2404.04072) · 📚 被引 15
- **作者**: Vladan Stojnic, Yannis Kalantidis, Giorgos Tolias
- **🏷️ 机构**: Czech Technical University in Prague,VRG, FEE, NAVER LABS Europe
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have demonstrated impressive performance on zero-shot classification, i.e. classification when provided merely with a list of class names. In this paper, we tackle the case of zero-shot classification in the presence of unlabeled data. We leverage the graph structure of the unlabeled data and introduce ZLaP, a method based on label propagation (LP) that utilizes geodesic distances for classification. We tailor LP to graphs containing both text and image features and further propose an efficient method for performing inductive inference based on a dual solution and a sparsification step. We perform extensive experiments to evaluate the effectiveness of our method on 14 common datasets and show that ZLaP outperforms the latest related works. Code: https://github.com/vladan-stojnic/ZLaP

</details>

### ArGue: Attribute-Guided Prompt Tuning for Vision-Language Models.
- **链接**: [arXiv:2311.16494](https://arxiv.org/abs/2311.16494) · 📚 被引 47
- **作者**: Xinyu Tian, Shu Zou, Zhaoyuan Yang, Jing Zhang
- **🏷️ 机构**: Australian National University, GE Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although soft prompt tuning is effective in efficiently adapting Vision-Language (V&L) models for downstream tasks, it shows limitations in dealing with distribution shifts. We address this issue with Attribute-Guided Prompt Tuning (ArGue), making three key contributions. 1) In contrast to the conventional approach of directly appending soft prompts preceding class names, we align the model with primitive visual attributes generated by Large Language Models (LLMs). We posit that a model's ability to express high confidence in these attributes signifies its capacity to discern the correct class rationales. 2) We introduce attribute sampling to eliminate disadvantageous attributes, thus only semantically meaningful attributes are preserved. 3) We propose negative prompting, explicitly enumerating class-agnostic attributes to activate spurious correlations and encourage the model to generate highly orthogonal probability distributions in relation to these negative features. In experiments, our method significantly outperforms current state-of-the-art prompt tuning methods on both novel class prediction and out-of-distribution generalization tasks.

</details>

### PartDistill: 3D Shape Part Segmentation by Vision-Language Model Distillation.
- **链接**: [arXiv:2312.04016](https://arxiv.org/abs/2312.04016) · 📚 被引 17
- **作者**: Ardian Umam, Cheng-Kun Yang, Min-Hung Chen, Jen-Hui Chuang, Yen-Yu Lin
- **🏷️ 机构**: National Yang Ming Chiao Tung University, MediaTek, NVIDIA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper proposes a cross-modal distillation framework, PartDistill, which transfers 2D knowledge from vision-language models (VLMs) to facilitate 3D shape part segmentation. PartDistill addresses three major challenges in this task: the lack of 3D segmentation in invisible or undetected regions in the 2D projections, inconsistent 2D predictions by VLMs, and the lack of knowledge accumulation across different 3D shapes. PartDistill consists of a teacher network that uses a VLM to make 2D predictions and a student network that learns from the 2D predictions while extracting geometrical features from multiple 3D shapes to carry out 3D part segmentation. A bi-directional distillation, including forward and backward distillations, is carried out within the framework, where the former forward distills the 2D predictions to the student network, and the latter improves the quality of the 2D predictions, which subsequently enhances the final 3D segmentation. Moreover, PartDistill can exploit generative models that facilitate effortless 3D shape creation for generating knowledge sources to be distilled. Through extensive experiments, PartDistill boosts the existing methods with substantial margins on widely used ShapeNetPart and PartNetE datasets, by more than 15% and 12% higher mIoU scores, respectively. The code for this work is available at https://github.com/ardianumam/PartDistill.

</details>

### Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation.
- **链接**: [arXiv:2404.01943](https://arxiv.org/abs/2404.01943) · 📚 被引 31
- **作者**: Zihan Wang, Xiangyang Li, Jiahao Yang, Yeqi Liu, Junjie Hu, Ming Jiang et al.
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences,Beijing,China,100190, University of Wisconsin,Department of Computer Science,Madison,WI,USA, Indiana University,Department of Human-centered Computing,Indianapolis,IN,USA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-language navigation (VLN) enables the agent to navigate to a remote location following the natural language instruction in 3D environments. At each navigation step, the agent selects from possible candidate locations and then makes the move. For better navigation planning, the lookahead exploration strategy aims to effectively evaluate the agent's next action by accurately anticipating the future environment of candidate locations. To this end, some existing works predict RGB images for future environments, while this strategy suffers from image distortion and high computational cost. To address these issues, we propose the pre-trained hierarchical neural radiance representation model (HNR) to produce multi-level semantic features for future environments, which are more robust and efficient than pixel-wise RGB reconstruction. Furthermore, with the predicted future environmental representations, our lookahead VLN model is able to construct the navigable future path tree and select the optimal path via efficient parallel evaluation. Extensive experiments on the VLN-CE datasets confirm the effectiveness of our method.

</details>

### MMA: Multi-Modal Adapter for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02249) · 📚 被引 83
- **作者**: Lingxiao Yang, Ru-Yuan Zhang, Yanchen Wang, Xiaohua Xie
- **🏷️ 机构**: Sun Yat-sen University, Shanghai Jiao Tong University, Stanford University
- **会议**: CVPR 2024

### Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts Adapters.
- **链接**: [arXiv:2403.11549](https://arxiv.org/abs/2403.11549) · 📚 被引 115
- **作者**: Jiazuo Yu, Yunzhi Zhuge, Lu Zhang, Ping Hu, Dong Wang, Huchuan Lu et al.
- **🏷️ 机构**: Dalian University of Technology,China, University of Electronic Science and Technology of China, Tsinghua University,China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning can empower vision-language models to continuously acquire new knowledge, without the need for access to the entire historical dataset. However, mitigating the performance degradation in large-scale models is non-trivial due to (i) parameter shifts throughout lifelong learning and (ii) significant computational burdens associated with full-model tuning. In this work, we present a parameter-efficient continual learning framework to alleviate long-term forgetting in incremental learning with vision-language models. Our approach involves the dynamic expansion of a pre-trained CLIP model, through the integration of Mixture-of-Experts (MoE) adapters in response to new tasks. To preserve the zero-shot recognition capability of vision-language models, we further introduce a Distribution Discriminative Auto-Selector (DDAS) that automatically routes in-distribution and out-of-distribution inputs to the MoE Adapter and the original CLIP, respectively. Through extensive experiments across various settings, our proposed method consistently outperforms previous state-of-the-art approaches while concurrently reducing parameter training burdens by 60%. Our code locates at https://github.com/JiazuoYu/MoE-Adapters4CL

</details>

### SC- Tune: Unleashing Self-Consistent Referential Comprehension in Large Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01242) · 📚 被引 6
- **作者**: Tongtian Yue, Jie Cheng, Longteng Guo, Xingyuan Dai, Zijia Zhao, Xingjian He et al.
- **🏷️ 机构**: Laboratory of Cognition and Decision Intelligence for Complex Systems, CASIA, State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA
- **会议**: CVPR 2024

### On the Test-Time Zero-Shot Generalization of Vision-Language Models: Do we Really need Prompt Learning?
- **链接**: [arXiv:2405.02266](https://arxiv.org/abs/2405.02266) · 📚 被引 34
- **作者**: Maxime Zanella, Ismail Ben Ayed
- **🏷️ 机构**: UCLouvain UMons, &#x00C9;ts Montr&#x00E9;al
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The development of large vision-language models, notably CLIP, has catalyzed research into effective adaptation techniques, with a particular focus on soft prompt tuning. Conjointly, test-time augmentation, which utilizes multiple augmented views of a single image to enhance zero-shot generalization, is emerging as a significant area of interest. This has predominantly directed research efforts toward test-time prompt tuning. In contrast, we introduce a robust MeanShift for Test-time Augmentation (MTA), which surpasses prompt-based methods without requiring this intensive training procedure. This positions MTA as an ideal solution for both standalone and API-based applications. Additionally, our method does not rely on ad hoc rules (e.g., confidence threshold) used in some previous test-time augmentation techniques to filter the augmented views. Instead, MTA incorporates a quality assessment variable for each view directly into its optimization process, termed as the inlierness score. This score is jointly optimized with a density mode seeking process, leading to an efficient training- and hyperparameter-free approach. We extensively benchmark our method on 15 datasets and demonstrate MTA's superiority and computational efficiency. Deployed easily as plug-and-play module on top of zero-shot models and state-of-the-art few-shot methods, MTA shows systematic and consistent improvements.

</details>

### Investigating Compositional Challenges in Vision-Language Models for Visual Grounding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01341) · 📚 被引 12
- **作者**: Yunan Zeng, Yan Huang, Jinjin Zhang, Zequn Jie, Zhenhua Chai, Liang Wang
- **🏷️ 机构**: Center for Research on Intelligent Perception and Computing (CRIPAC), Meituan
- **会议**: CVPR 2024

### Semantics-Aware Motion Retargeting with Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00210) · 📚 被引 11
- **作者**: Haodong Zhang, Zhike Chen, Haocheng Xu, Lei Hao, Xiaofei Wu, Songcen Xu et al.
- **🏷️ 机构**: Zhejiang University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2024

### Iterated Learning Improves Compositionality in Large Vision-Language Models.
- **链接**: [arXiv:2404.02145](https://arxiv.org/abs/2404.02145) · 📚 被引 3
- **作者**: Chenhao Zheng, Jieyu Zhang, Aniruddha Kembhavi, Ranjay Krishna
- **🏷️ 机构**: University of Michigan, University of Washington, Allen Institute for Artificial Intelligence
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A fundamental characteristic common to both human vision and natural language is their compositional nature. Yet, despite the performance gains contributed by large vision and language pretraining, recent investigations find that most-if not all-our state-of-the-art vision-language models struggle at compositionality. They are unable to distinguish between images of " a girl in white facing a man in black" and "a girl in black facing a man in white". Moreover, prior work suggests that compositionality doesn't arise with scale: larger model sizes or training data don't help. This paper develops a new iterated training algorithm that incentivizes compositionality. We draw on decades of cognitive science research that identifies cultural transmission-the need to teach a new generation-as a necessary inductive prior that incentivizes humans to develop compositional languages. Specifically, we reframe vision-language contrastive learning as the Lewis Signaling Game between a vision agent and a language agent, and operationalize cultural transmission by iteratively resetting one of the agent's weights during training. After every iteration, this training paradigm induces representations that become "easier to learn", a property of compositional languages: e.g. our model trained on CC3M and CC12M improves standard CLIP by 4.7%, 4.0% respectfully in the SugarCrepe benchmark.

</details>

### Honeybee: Locality-Enhanced Projector for Multimodal LLM.
- **链接**: [arXiv:2312.06742](https://arxiv.org/abs/2312.06742) · 📚 被引 84
- **作者**: Junbum Cha, Wooyoung Kang, Jonghwan Mun, Byungseok Roh
- **🏷️ 机构**: Kakao Brain
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Multimodal Large Language Models (MLLMs), a visual projector plays a crucial role in bridging pre-trained vision encoders with LLMs, enabling profound visual understanding while harnessing the LLMs' robust capabilities. Despite the importance of the visual projector, it has been relatively less explored. In this study, we first identify two essential projector properties: (i) flexibility in managing the number of visual tokens, crucial for MLLMs' overall efficiency, and (ii) preservation of local context from visual features, vital for spatial understanding. Based on these findings, we propose a novel projector design that is both flexible and locality-enhanced, effectively satisfying the two desirable properties. Additionally, we present comprehensive strategies to effectively utilize multiple and multifaceted instruction datasets. Through extensive experiments, we examine the impact of individual design choices. Finally, our proposed MLLM, Honeybee, remarkably outperforms previous state-of-the-art methods across various benchmarks, including MME, MMBench, SEED-Bench, and LLaVA-Bench, achieving significantly higher efficiency. Code and models are available at https://github.com/kakaobrain/honeybee.

</details>

### LION : Empowering Multimodal Large Language Model with Dual-Level Visual Knowledge.
- **链接**: [arXiv:2311.11860](https://arxiv.org/abs/2311.11860) · 📚 被引 45
- **作者**: Gongwei Chen, Leyang Shen, Rui Shao, Xiang Deng, Liqiang Nie
- **🏷️ 机构**: School of Computer Science and Technology, Harbin Institute of Technology,Shenzhen
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) have endowed LLMs with the ability to perceive and understand multi-modal signals. However, most of the existing MLLMs mainly adopt vision encoders pretrained on coarsely aligned image-text pairs, leading to insufficient extraction and reasoning of visual knowledge. To address this issue, we devise a dual-Level vIsual knOwledge eNhanced Multimodal Large Language Model (LION), which empowers the MLLM by injecting visual knowledge in two levels. 1) Progressive incorporation of fine-grained spatial-aware visual knowledge. We design a vision aggregator cooperated with region-level vision-language (VL) tasks to incorporate fine-grained spatial-aware visual knowledge into the MLLM. To alleviate the conflict between image-level and region-level VL tasks during incorporation, we devise a dedicated stage-wise instruction-tuning strategy with mixture-of-adapters. This progressive incorporation scheme contributes to the mutual promotion between these two kinds of VL tasks. 2) Soft prompting of high-level semantic visual evidence. We facilitate the MLLM with high-level semantic visual evidence by leveraging diverse image tags. To mitigate the potential influence caused by imperfect predicted tags, we propose a soft prompting method by embedding a learnable token into the tailored text instruction. Comprehensive experiments on several multi-modal benchmarks demonstrate the superiority of our model (e.g., improvement of 5% accuracy on VSR and 3% CIDEr on TextCaps over InstructBLIP, 5% accuracy on RefCOCOg over Kosmos-2).

</details>

### SmartEdit: Exploring Complex Instruction-Based Image Editing with Multimodal Large Language Models.
- **链接**: [arXiv:2312.06739](https://arxiv.org/abs/2312.06739) · 📚 被引 83
- **作者**: Yuzhou Huang, Liangbin Xie, Xintao Wang, Ziyang Yuan, Xiaodong Cun, Yixiao Ge et al.
- **🏷️ 机构**: The Chinese University of Hong Kong,Shenzhen,CUHK-SZ, ARC Lab, Tencent PCG, Tencent AI Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current instruction-based editing methods, such as InstructPix2Pix, often fail to produce satisfactory results in complex scenarios due to their dependence on the simple CLIP text encoder in diffusion models. To rectify this, this paper introduces SmartEdit, a novel approach to instruction-based image editing that leverages Multimodal Large Language Models (MLLMs) to enhance their understanding and reasoning capabilities. However, direct integration of these elements still faces challenges in situations requiring complex reasoning. To mitigate this, we propose a Bidirectional Interaction Module that enables comprehensive bidirectional information interactions between the input image and the MLLM output. During training, we initially incorporate perception data to boost the perception and understanding capabilities of diffusion models. Subsequently, we demonstrate that a small amount of complex instruction editing data can effectively stimulate SmartEdit's editing capabilities for more complex instructions. We further construct a new evaluation dataset, Reason-Edit, specifically tailored for complex instruction-based image editing. Both quantitative and qualitative results on this evaluation dataset indicate that our SmartEdit surpasses previous methods, paving the way for the practical application of complex instruction-based image editing.

</details>

### Sniffer: Multimodal Large Language Model for Explainable Out-of-Context Misinformation Detection.
- **链接**: [arXiv:2403.03170](https://arxiv.org/abs/2403.03170) · 📚 被引 80
- **作者**: Peng Qi, Zehong Yan, Wynne Hsu, Mong-Li Lee
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Misinformation is a prevalent societal issue due to its potential high risks. Out-of-context (OOC) misinformation, where authentic images are repurposed with false text, is one of the easiest and most effective ways to mislead audiences. Current methods focus on assessing image-text consistency but lack convincing explanations for their judgments, which is essential for debunking misinformation. While Multimodal Large Language Models (MLLMs) have rich knowledge and innate capability for visual reasoning and explanation generation, they still lack sophistication in understanding and discovering the subtle crossmodal differences. In this paper, we introduce SNIFFER, a novel multimodal large language model specifically engineered for OOC misinformation detection and explanation. SNIFFER employs two-stage instruction tuning on InstructBLIP. The first stage refines the model's concept alignment of generic objects with news-domain entities and the second stage leverages language-only GPT-4 generated OOC-specific instruction data to fine-tune the model's discriminatory powers. Enhanced by external tools and retrieval, SNIFFER not only detects inconsistencies between text and image but also utilizes external knowledge for contextual verification. Our experiments show that SNIFFER surpasses the original MLLM by over 40% and outperforms state-of-the-art methods in detection accuracy. SNIFFER also provides accurate and persuasive explanations as validated by quantitative and human evaluations.

</details>

### Link-Context Learning for Multimodal LLMs.
- **链接**: [arXiv:2308.07891](https://arxiv.org/abs/2308.07891) · 📚 被引 6
- **作者**: Yan Tai, Weichen Fan, Zhao Zhang, Ziwei Liu
- **🏷️ 机构**: Ningbo Institute of Digital Twin, Eastern Institute of Technology,Ningbo,China, SenseTime Research, Nanyang Technological University,S-Lab
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to learn from context with novel concepts, and deliver appropriate responses are essential in human conversations. Despite current Multimodal Large Language Models (MLLMs) and Large Language Models (LLMs) being trained on mega-scale datasets, recognizing unseen images or understanding novel concepts in a training-free manner remains a challenge. In-Context Learning (ICL) explores training-free few-shot learning, where models are encouraged to ``learn to learn" from limited tasks and generalize to unseen tasks. In this work, we propose link-context learning (LCL), which emphasizes "reasoning from cause and effect" to augment the learning capabilities of MLLMs. LCL goes beyond traditional ICL by explicitly strengthening the causal relationship between the support set and the query set. By providing demonstrations with causal links, LCL guides the model to discern not only the analogy but also the underlying causal associations between data points, which empowers MLLMs to recognize unseen images and understand novel concepts more effectively. To facilitate the evaluation of this novel approach, we introduce the ISEKAI dataset, comprising exclusively of unseen generated image-label pairs designed for link-context learning. Extensive experiments show that our LCL-MLLM exhibits strong link-context learning capabilities to novel concepts over vanilla MLLMs. Code and data will be released at https://github.com/isekai-portal/Link-Context-Learning.

</details>

### Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs.
- **链接**: [arXiv:2401.06209](https://arxiv.org/abs/2401.06209) · 📚 被引 192
- **作者**: Shengbang Tong, Zhuang Liu, Yuexiang Zhai, Yi Ma, Yann LeCun, Saining Xie
- **🏷️ 机构**: New York University, FAIR, Meta, UC Berkeley
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Is vision good enough for language? Recent advancements in multimodal models primarily stem from the powerful reasoning abilities of large language models (LLMs). However, the visual component typically depends only on the instance-level contrastive language-image pre-training (CLIP). Our research reveals that the visual capabilities in recent multimodal LLMs (MLLMs) still exhibit systematic shortcomings. To understand the roots of these errors, we explore the gap between the visual embedding space of CLIP and vision-only self-supervised learning. We identify ''CLIP-blind pairs'' - images that CLIP perceives as similar despite their clear visual differences. With these pairs, we construct the Multimodal Visual Patterns (MMVP) benchmark. MMVP exposes areas where state-of-the-art systems, including GPT-4V, struggle with straightforward questions across nine basic visual patterns, often providing incorrect answers and hallucinated explanations. We further evaluate various CLIP-based vision-and-language models and found a notable correlation between visual patterns that challenge CLIP models and those problematic for multimodal LLMs. As an initial effort to address these issues, we propose a Mixture of Features (MoF) approach, demonstrating that integrating vision self-supervised learning features with MLLMs can significantly enhance their visual grounding capabilities. Together, our research suggests visual representation learning remains an open challenge, and accurate visual grounding is crucial for future successful multimodal systems.

</details>

### GSVA: Generalized Segmentation via Multimodal Large Language Models.
- **链接**: [arXiv:2312.10103](https://arxiv.org/abs/2312.10103) · 📚 被引 83
- **作者**: Zhuofan Xia, Dongchen Han, Yizeng Han, Xuran Pan, Shiji Song, Gao Huang
- **🏷️ 机构**: Department of Automation, BNRist, Tsinghua University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalized Referring Expression Segmentation (GRES) extends the scope of classic RES to refer to multiple objects in one expression or identify the empty targets absent in the image. GRES poses challenges in modeling the complex spatial relationships of the instances in the image and identifying non-existing referents. Multimodal Large Language Models (MLLMs) have recently shown tremendous progress in these complicated vision-language tasks. Connecting Large Language Models (LLMs) and vision models, MLLMs are proficient in understanding contexts with visual inputs. Among them, LISA, as a representative, adopts a special [SEG] token to prompt a segmentation mask decoder, e.g., SAM, to enable MLLMs in the RES task. However, existing solutions to GRES remain unsatisfactory since current segmentation MLLMs cannot correctly handle the cases where users might reference multiple subjects in a singular prompt or provide descriptions incongruent with any image target. In this paper, we propose Generalized Segmentation Vision Assistant (GSVA) to address this gap. Specifically, GSVA reuses the [SEG] token to prompt the segmentation model towards supporting multiple mask references simultaneously and innovatively learns to generate a [REJ] token to reject the null targets explicitly. Experiments validate GSVA's efficacy in resolving the GRES issue, marking a notable enhancement and setting a new record on the GRES benchmark gRefCOCO dataset. GSVA also proves effective across various classic referring segmentation and comprehension tasks.

</details>

### CLIP-KD: An Empirical Study of CLIP Model Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01510) · 📚 被引 67
- **作者**: Chuanguang Yang, Zhulin An, Libo Huang, Junyu Bi, Xinqiang Yu, Han Yang et al.
- **🏷️ 机构**: Institute of Computing Technology,Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web. → [multimodal](../multimodal/Guideline%202024.md)
- MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MLLM-CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- YOLO-World: Real-Time Open-Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- SHiNe: Semantic Hierarchy Nexus for Open-Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Open Vocabulary Semantic Scene Sketch Understanding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Open-vocabulary object 6D pose estimation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- OMG: Towards Open-vocabulary Motion Generation via Mixture of Controllers. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Open-Vocabulary Segmentation with Semantic-Assisted Calibration. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- OVMR: Open-Vocabulary Recognition with Multi-Modal References. → [multimodal](../multimodal/Guideline%202024.md)
- Open-Vocabulary Semantic Segmentation with Image Embedding Balancing. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Transferable and Principled Efficiency for Open-Vocabulary Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Visual Programming for Zero-Shot Open-Vocabulary 3D Visual Grounding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Abductive Ego-View Accident Video Understanding for Safe Driving Perception. → [video-understanding](../video-understanding/Guideline%202024.md)
- MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer. → [network-pruning](../network-pruning/Guideline%202024.md)
- MULTIFLOW: Shifting Towards Task-Agnostic Vision-Language Pruning. → [network-pruning](../network-pruning/Guideline%202024.md)
- VCoder: Versatile Vision Encoders for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Source-Free Domain Adaptation with Frozen Multimodal Foundation Model. → [multimodal](../multimodal/Guideline%202024.md)
- Sieve: Multimodal Dataset Pruning Using Image Captioning Models. → [multimodal](../multimodal/Guideline%202024.md)
- MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation. → [multimodal](../multimodal/Guideline%202024.md)
- Multimodal Prompt Perceiver: Empower Adaptiveness, Generalizability and Fidelity for All-in-One Image Restoration. → [multimodal](../multimodal/Guideline%202024.md)
- ViP-LLaVA: Making Large Multimodal Models Understand Arbitrary Visual Prompts. → [multimodal](../multimodal/Guideline%202024.md)
- Hallucination Augmented Contrastive Learning for Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202024.md)
- SEED-Bench: Benchmarking Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- GLaMM: Pixel Grounding Large Multimodal Model. → [multimodal](../multimodal/Guideline%202024.md)
- TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- Data-Efficient Multimodal Fusion on a Single GPU. → [multimodal](../multimodal/Guideline%202024.md)
- Cloud-Device Collaborative Learning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Towards Language-Driven Video Inpainting via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Multimodal Pathway: Improve Transformers with Irrelevant Data from Other Modalities. → [multimodal](../multimodal/Guideline%202024.md)
- Exploring the Transferability of Visual Prompting for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MM-Narrator: Narrating Long-form Videos with Multimodal In-Context Learning. → [multimodal](../multimodal/Guideline%202024.md)
- TRINS: Towards Multimodal Language Models that Can Read. → [multimodal](../multimodal/Guideline%202024.md)
- Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Enhancing Visual Document Understanding with Contrastive Learning in Large Visual-Language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- OmniViD: A Generative Framework for Universal Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)


## 🆕 增量新增

### MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection.
- **链接**: [arXiv:2407.21465](https://arxiv.org/abs/2407.21465) · 📚 被引 3
- **作者**: Kuo Wang, Lechao Cheng, Weikai Chen, Pingping Zhang, Liang Lin, Fan Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning from pseudo-labels that generated with VLMs~(Vision Language Models) has been shown as a promising solution to assist open vocabulary detection (OVD) in recent studies. However, due to the domain gap between VLM and vision-detection tasks, pseudo-labels produced by the VLMs are prone to be noisy, while the training design of the detector further amplifies the bias. In this work, we investigate the root cause of VLMs' biased prediction under the OVD context. Our observations lead to a simple yet effective paradigm, coded MarvelOVD, that generates significantly better training targets and optimizes the learning procedure in an online manner by marrying the capability of the detector with the vision-language model. Our key insight is that the detector itself can act as a strong auxiliary guidance to accommodate VLM's inability of understanding both the ``background'' and the context of a proposal within the image. Based on it, we greatly purify the noisy pseudo-labels via Online Mining and propose Adaptive Reweighting to effectively suppress the biased training boxes that are not well aligned with the target object. In addition, we also identify a neglected ``base-novel-conflict'' problem and introduce stratified label assignments to prevent it. Extensive experiments on COCO and LVIS datasets demonstrate that our method outperforms the other state-of-the-arts by significant margins. Codes are available at https://github.com/wkfdb/MarvelOVD

</details>

### AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72761-0_4) · 📚 被引 129
- **作者**: Yunkang Cao, Jiangning Zhang, Luca Frittoli, Yuqi Cheng, Weiming Shen, Giacomo Boracchi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### BLINK: Multimodal Large Language Models Can See but Not Perceive.
- **链接**: [arXiv:2404.12390](https://arxiv.org/abs/2404.12390) · 📚 被引 60
- **作者**: Xingyu Fu, Yushi Hu, Bangzheng Li, Yu Feng, Haoyu Wang, Xudong Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Blink, a new benchmark for multimodal language models (LLMs) that focuses on core visual perception abilities not found in other evaluations. Most of the Blink tasks can be solved by humans "within a blink" (e.g., relative depth estimation, visual correspondence, forensics detection, and multi-view reasoning). However, we find these perception-demanding tasks cast significant challenges for current multimodal LLMs because they resist mediation through natural language. Blink reformats 14 classic computer vision tasks into 3,807 multiple-choice questions, paired with single or multiple images and visual prompting. While humans get 95.70% accuracy on average, Blink is surprisingly challenging for existing multimodal LLMs: even the best-performing GPT-4V and Gemini achieve accuracies of 51.26% and 45.72%, only 13.17% and 7.63% higher than random guessing, indicating that such perception abilities have not "emerged" yet in recent multimodal LLMs. Our analysis also highlights that specialist CV models could solve these problems much better, suggesting potential pathways for future improvements. We believe Blink will stimulate the community to help multimodal LLMs catch up with human-level visual perception.

</details>

### Eyes Closed, Safety on: Protecting Multimodal LLMs via Image-to-Text Transformation.
- **链接**: [arXiv:2403.09572](https://arxiv.org/abs/2403.09572) · 📚 被引 12
- **作者**: Yunhao Gou, Kai Chen, Zhili Liu, Lanqing Hong, Hang Xu, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have shown impressive reasoning abilities. However, they are also more vulnerable to jailbreak attacks than their LLM predecessors. Although still capable of detecting the unsafe responses, we observe that safety mechanisms of the pre-aligned LLMs in MLLMs can be easily bypassed with the introduction of image features. To construct robust MLLMs, we propose ECSO (Eyes Closed, Safety On), a novel training-free protecting approach that exploits the inherent safety awareness of MLLMs, and generates safer responses via adaptively transforming unsafe images into texts to activate the intrinsic safety mechanism of pre-aligned LLMs in MLLMs. Experiments on five state-of-the-art (SoTA) MLLMs demonstrate that ECSO enhances model safety significantly (e.g.,, 37.6% improvement on the MM-SafetyBench (SD+OCR) and 71.3% on VLSafe with LLaVA-1.5-7B), while consistently maintaining utility results on common MLLM benchmarks. Furthermore, we show that ECSO can be used as a data engine to generate supervised-finetuning (SFT) data for MLLM alignment without extra human intervention.

</details>

### Images are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models.
- **链接**: [arXiv:2403.09792](https://arxiv.org/abs/2403.09792) · 📚 被引 30
- **作者**: Yifan Li, Hangyu Guo, Kun Zhou, Wayne Xin Zhao, Ji-Rong Wen
- **🏷️ 机构**: Renmin University
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we study the harmlessness alignment problem of multimodal large language models (MLLMs). We conduct a systematic empirical analysis of the harmlessness performance of representative MLLMs and reveal that the image input poses the alignment vulnerability of MLLMs. Inspired by this, we propose a novel jailbreak method named HADES, which hides and amplifies the harmfulness of the malicious intent within the text input, using meticulously crafted images. Experimental results show that HADES can effectively jailbreak existing MLLMs, which achieves an average Attack Success Rate (ASR) of 90.26% for LLaVA-1.5 and 71.60% for Gemini Pro Vision. Our code and data are available at https://github.com/RUCAIBox/HADES.

</details>

### LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents.
- **链接**: [arXiv:2311.05437](https://arxiv.org/abs/2311.05437) · 📚 被引 44
- **作者**: Shilong Liu, Hao Cheng, Haotian Liu, Hao Zhang, Feng Li, Tianhe Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LLaVA-Plus is a general-purpose multimodal assistant that expands the capabilities of large multimodal models. It maintains a skill repository of pre-trained vision and vision-language models and can activate relevant tools based on users' inputs to fulfill real-world tasks. LLaVA-Plus is trained on multimodal instruction-following data to acquire the ability to use tools, covering visual understanding, generation, external knowledge retrieval, and compositions. Empirical results show that LLaVA-Plus outperforms LLaVA in existing capabilities and exhibits new ones. It is distinct in that the image query is directly grounded and actively engaged throughout the entire human-AI interaction sessions, significantly improving tool use performance and enabling new scenarios.

</details>

### Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models.
- **链接**: [arXiv:2404.13013](https://arxiv.org/abs/2404.13013) · 📚 被引 46
- **作者**: Chuofan Ma, Yi Jiang, Jiannan Wu, Zehuan Yuan, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Groma, a Multimodal Large Language Model (MLLM) with grounded and fine-grained visual perception ability. Beyond holistic image understanding, Groma is adept at region-level tasks such as region captioning and visual grounding. Such capabilities are built upon a localized visual tokenization mechanism, where an image input is decomposed into regions of interest and subsequently encoded into region tokens. By integrating region tokens into user instructions and model responses, we seamlessly enable Groma to understand user-specified region inputs and ground its textual output to images. Besides, to enhance the grounded chat ability of Groma, we curate a visually grounded instruction dataset by leveraging the powerful GPT-4V and visual prompting techniques. Compared with MLLMs that rely on the language model or external module for localization, Groma consistently demonstrates superior performances in standard referring and grounding benchmarks, highlighting the advantages of embedding localization into image tokenization. Project page: https://groma-mllm.github.io/.

</details>

### MM1: Methods, Analysis and Insights from Multimodal LLM Pre-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73397-0_18) · 📚 被引 80
- **作者**: Brandon McKinzie, Zhe Gan, Jean-Philippe Fauconnier, Sam Dodge, Bowen Zhang, Philipp Dufter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Strengthening Multimodal Large Language Model with Bootstrapped Preference Optimization.
- **链接**: [arXiv:2403.08730](https://arxiv.org/abs/2403.08730) · 📚 被引 14
- **作者**: Renjie Pi, Tianyang Han, Wei Xiong, Jipeng Zhang, Runtao Liu, Rui Pan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) excel in generating responses based on visual inputs. However, they often suffer from a bias towards generating responses similar to their pretraining corpus, overshadowing the importance of visual information. We treat this bias as a "preference" for pretraining statistics, which hinders the model's grounding in visual input. To mitigate this issue, we propose Bootstrapped Preference Optimization (BPO), which conducts preference learning with datasets containing negative responses bootstrapped from the model itself. Specifically, we propose the following two strategies: 1) using distorted image inputs to the MLLM for eliciting responses that contain signified pretraining bias; 2) leveraging text-based LLM to explicitly inject erroneous but common elements into the original response. Those undesirable responses are paired with original annotated responses from the datasets to construct the preference dataset, which is subsequently utilized to perform preference learning. Our approach effectively suppresses pretrained LLM bias, enabling enhanced grounding in visual inputs. Extensive experimentation demonstrates significant performance improvements across multiple benchmarks, advancing the state-of-the-art in multimodal conversational systems.

</details>

### Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning.
- **链接**: [arXiv:2407.04207](https://arxiv.org/abs/2407.04207)
- **作者**: Mainak Singha, Ankit Jha, Divyam Gupta, Pranav Singla, Biplab Banerjee
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the challenges inherent in sketch-based image retrieval (SBIR) across various settings, including zero-shot SBIR, generalized zero-shot SBIR, and fine-grained zero-shot SBIR, by leveraging the vision-language foundation model CLIP. While recent endeavors have employed CLIP to enhance SBIR, these approaches predominantly follow uni-modal prompt processing and overlook to exploit CLIP's integrated visual and textual capabilities fully. To bridge this gap, we introduce SpLIP, a novel multi-modal prompt learning scheme designed to operate effectively with frozen CLIP backbones. We diverge from existing multi-modal prompting methods that treat visual and textual prompts independently or integrate them in a limited fashion, leading to suboptimal generalization. SpLIP implements a bi-directional prompt-sharing strategy that enables mutual knowledge exchange between CLIP's visual and textual encoders, fostering a more cohesive and synergistic prompt processing mechanism that significantly reduces the semantic gap between the sketch and photo embeddings. In addition to pioneering multi-modal prompt learning, we propose two innovative strategies for further refining the embedding space. The first is an adaptive margin generation for the sketch-photo triplet loss, regulated by CLIP's class textual embeddings. The second introduces a novel task, termed conditional cross-modal jigsaw, aimed at enhancing fine-grained sketch-photo alignment by implicitly modeling sketches' viable patch arrangement using knowledge of unshuffled photos. Our comprehensive experimental evaluations across multiple benchmarks demonstrate the superior performance of SpLIP in all three SBIR scenarios. Project page: https://mainaksingha01.github.io/SpLIP/ .

</details>

### MoMA: Multimodal LLM Adapter for Fast Personalized Image Generation.
- **链接**: [arXiv:2404.05674](https://arxiv.org/abs/2404.05674) · 📚 被引 20
- **作者**: Kunpeng Song, Yizhe Zhu, Bingchen Liu, Qing Yan, Ahmed Elgammal, Xiao Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present MoMA: an open-vocabulary, training-free personalized image model that boasts flexible zero-shot capabilities. As foundational text-to-image models rapidly evolve, the demand for robust image-to-image translation grows. Addressing this need, MoMA specializes in subject-driven personalized image generation. Utilizing an open-source, Multimodal Large Language Model (MLLM), we train MoMA to serve a dual role as both a feature extractor and a generator. This approach effectively synergizes reference image and text prompt information to produce valuable image features, facilitating an image diffusion model. To better leverage the generated features, we further introduce a novel self-attention shortcut method that efficiently transfers image features to an image diffusion model, improving the resemblance of the target object in generated images. Remarkably, as a tuning-free plug-and-play module, our model requires only a single reference image and outperforms existing methods in generating images with high detail fidelity, enhanced identity-preservation and prompt faithfulness. Our work is open-source, thereby providing universal access to these advancements.

</details>

### HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning.
- **链接**: [arXiv:2407.15680](https://arxiv.org/abs/2407.15680) · 📚 被引 11
- **作者**: Zhecan Wang, Garrett Bingham, Adams Wei Yu, Quoc V. Le, Thang Luong, Golnaz Ghiasi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hallucination has been a major problem for large language models and remains a critical challenge when it comes to multimodality in which vision-language models (VLMs) have to deal with not just textual but also visual inputs. Despite rapid progress in VLMs, resources for evaluating and addressing multimodal hallucination are limited and mostly focused on evaluation. This work introduces HaloQuest, a novel visual question answering dataset that captures various aspects of multimodal hallucination such as false premises, insufficient contexts, and visual challenges. A novel idea from HaloQuest is to leverage synthetic images, apart from real ones, to enable dataset creation at scale. With over 7.7K examples spanning across a wide variety of categories, HaloQuest was designed to be both a challenging benchmark for VLMs and a fine-tuning dataset for advancing multimodal reasoning. Our experiments reveal that current models struggle with HaloQuest, with all open-source VLMs achieving below 36% accuracy. On the other hand, fine-tuning on HaloQuest significantly reduces hallucination rates while preserving performance on standard reasoning tasks. Our results discover that benchmarking with generated images is highly correlated (r=0.97) with real images. Last but not least, we propose a novel Auto-Eval mechanism that is highly correlated with human raters (r=0.99) for evaluating VLMs. In sum, this work makes concrete strides towards understanding, evaluating, and mitigating hallucination in VLMs, serving as an important step towards more reliable multimodal AI systems in the future.

</details>

### Instruction Tuning-Free Visual Token Complement for Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73004-7_26) · 📚 被引 3
- **作者**: Dongsheng Wang, Jiequan Cui, Miaoge Li, Wang Lin, Bo Chen, Hanwang Zhang
- **🏷️ 机构**: NUS
- **会议**: ECCV 2024

### AdaShield : Safeguarding Multimodal Large Language Models from Structure-Based Attack via Adaptive Shield Prompting.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72661-3_5) · 📚 被引 15
- **作者**: Yu Wang, Xiaogeng Liu, Yu Li, Muhao Chen, Chaowei Xiao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### A Comprehensive Study of Multimodal Large Language Models for Image Quality Assessment.
- **链接**: [arXiv:2403.10854](https://arxiv.org/abs/2403.10854)
- **作者**: Tianhe Wu, Kede Ma, Jie Liang, Yujiu Yang, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Multimodal Large Language Models (MLLMs) have experienced significant advancement in visual understanding and reasoning, their potential to serve as powerful, flexible, interpretable, and text-driven models for Image Quality Assessment (IQA) remains largely unexplored. In this paper, we conduct a comprehensive and systematic study of prompting MLLMs for IQA. We first investigate nine prompting systems for MLLMs as the combinations of three standardized testing procedures in psychophysics (i.e., the single-stimulus, double-stimulus, and multiple-stimulus methods) and three popular prompting strategies in natural language processing (i.e., the standard, in-context, and chain-of-thought prompting). We then present a difficult sample selection procedure, taking into account sample diversity and uncertainty, to further challenge MLLMs equipped with the respective optimal prompting systems. We assess three open-source and one closed-source MLLMs on several visual attributes of image quality (e.g., structural and textural distortions, geometric transformations, and color differences) in both full-reference and no-reference scenarios. Experimental results show that only the closed-source GPT-4V provides a reasonable account for human perception of image quality, but is weak at discriminating fine-grained quality variations (e.g., color differences) and at comparing visual quality of multiple images, tasks humans can perform effortlessly.

</details>

### UMBRAE: Unified Multimodal Brain Decoding.
- **链接**: [arXiv:2404.07202](https://arxiv.org/abs/2404.07202) · 📚 被引 17
- **作者**: Weihao Xia, Raoul de Charette, A. Cengiz Öztireli, Jing-Hao Xue
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address prevailing challenges of the brain-powered research, departing from the observation that the literature hardly recover accurate spatial information and require subject-specific models. To address these challenges, we propose UMBRAE, a unified multimodal decoding of brain signals. First, to extract instance-level conceptual and spatial details from neural signals, we introduce an efficient universal brain encoder for multimodal-brain alignment and recover object descriptions at multiple levels of granularity from subsequent multimodal large language model (MLLM). Second, we introduce a cross-subject training strategy mapping subject-specific features to a common feature space. This allows a model to be trained on multiple subjects without extra resources, even yielding superior results compared to subject-specific models. Further, we demonstrate this supports weakly-supervised adaptation to new subjects, with only a fraction of the total training data. Experiments demonstrate that UMBRAE not only achieves superior results in the newly introduced tasks but also outperforms methods in well established tasks. To assess our method, we construct and share with the community a comprehensive brain understanding benchmark BrainHub. Our code and benchmark are available at https://weihaox.github.io/UMBRAE.

</details>

### LLMGA: Multimodal Large Language Model Based Generation Assistant.
- **链接**: [arXiv:2311.16500](https://arxiv.org/abs/2311.16500) · 📚 被引 10
- **作者**: Bin Xia, Shiyin Wang, Yingfan Tao, Yitong Wang, Jiaya Jia
- **🏷️ 机构**: CUHK / SmartMore
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce a Multimodal Large Language Model-based Generation Assistant (LLMGA), leveraging the vast reservoir of knowledge and proficiency in reasoning, comprehension, and response inherent in Large Language Models (LLMs) to assist users in image generation and editing. Diverging from existing approaches where Multimodal Large Language Models (MLLMs) generate fixed-size embeddings to control Stable Diffusion (SD), our LLMGA provides a detailed language generation prompt for precise control over SD. This not only augments LLM context understanding but also reduces noise in generation prompts, yields images with more intricate and precise content, and elevates the interpretability of the network. To this end, we curate a comprehensive dataset comprising prompt refinement, similar image generation, inpainting \& outpainting, and instruction-based editing. Moreover, we propose a two-stage training scheme. In the first stage, we train the MLLM to grasp the properties of image generation and editing, enabling it to generate detailed prompts. In the second stage, we optimize SD to align with the MLLM's generation prompts. Additionally, we propose a reference-based restoration network to alleviate texture, brightness, and contrast disparities between generated and preserved regions during inpainting and outpainting. Extensive results show that LLMGA has promising generation and editing capabilities and can enable more flexible and expansive applications in an interactive manner.

</details>

### CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios.
- **链接**: [arXiv:2403.04640](https://arxiv.org/abs/2403.04640) · 📚 被引 20
- **作者**: Qilang Ye, Zitong Yu, Rui Shao, Xinyu Xie, Philip Torr, Xiaochun Cao
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper focuses on the challenge of answering questions in scenarios that are composed of rich and complex dynamic audio-visual components. Although existing Multimodal Large Language Models (MLLMs) can respond to audio-visual content, these responses are sometimes ambiguous and fail to describe specific audio-visual events. To overcome this limitation, we introduce the CAT, which enhances MLLM in three ways: 1) besides straightforwardly bridging audio and video, we design a clue aggregator that aggregates question-related clues in dynamic audio-visual scenarios to enrich the detailed knowledge required for large language models. 2) CAT is trained on a mixed multimodal dataset, allowing direct application in audio-visual scenarios. Notably, we collect an audio-visual joint instruction dataset named AVinstruct, to further enhance the capacity of CAT to model cross-semantic correlations. 3) we propose AI-assisted ambiguity-aware direct preference optimization, a strategy specialized in retraining the model to favor the non-ambiguity response and improve the ability to localize specific audio-visual objects. Extensive experimental results demonstrate that CAT outperforms existing methods on multimodal tasks, especially in Audio-Visual Question Answering (AVQA) tasks. The codes and the collected instructions are released at https://github.com/rikeilong/Bay-CAT.

</details>

### Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73039-9_14) · 📚 被引 38
- **作者**: Keen You, Haotian Zhang, Eldon Schoop, Floris Weers, Amanda Swearngin, Jeffrey Nichols et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Merlin: Empowering Multimodal LLMs with Foresight Minds.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73235-5_24) · 📚 被引 14
- **作者**: En Yu, Liang Zhao, Yana Wei, Jinrong Yang, Dongming Wu, Lingyu Kong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models.
- **链接**: [arXiv:2406.10740](https://arxiv.org/abs/2406.10740) · 📚 被引 4
- **作者**: Zhikai Zhang, Yitang Li, Haofeng Huang, Mingxian Lin, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human motion synthesis is a fundamental task in computer animation. Despite recent progress in this field utilizing deep learning and motion capture data, existing methods are always limited to specific motion categories, environments, and styles. This poor generalizability can be partially attributed to the difficulty and expense of collecting large-scale and high-quality motion data. At the same time, foundation models trained with internet-scale image and text data have demonstrated surprising world knowledge and reasoning ability for various downstream tasks. Utilizing these foundation models may help with human motion synthesis, which some recent works have superficially explored. However, these methods didn't fully unveil the foundation models' potential for this task and only support several simple actions and environments. In this paper, we for the first time, without any motion data, explore open-set human motion synthesis using natural language instructions as user control signals based on MLLMs across any motion task and environment. Our framework can be split into two stages: 1) sequential keyframe generation by utilizing MLLMs as a keyframe designer and animator; 2) motion filling between keyframes through interpolation and motion tracking. Our method can achieve general human motion synthesis for many downstream tasks. The promising results demonstrate the worth of mocap-free human motion synthesis aided by MLLMs and pave the way for future research.

</details>

### LLaVA-Grounding: Grounded Visual Chat with Large Multimodal Models.
- **链接**: [arXiv:2312.02949](https://arxiv.org/abs/2312.02949) · 📚 被引 54
- **作者**: Hao Zhang, Hongyang Li, Feng Li, Tianhe Ren, Xueyan Zou, Shilong Liu et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the recent significant advancements in large multi-modal models (LMMs), the importance of their grounding capability in visual chat is increasingly recognized. Despite recent efforts to enable LMMs to support grounding, their capabilities for grounding and chat are usually separate, and their chat performance drops dramatically when asked to ground. The problem is the lack of a dataset for grounded visual chat (GVC). Existing grounding datasets only contain short captions. To address this issue, we have created GVC data that allows for the combination of grounding and chat capabilities. To better evaluate the GVC capabilities, we have introduced a benchmark called Grounding-Bench. Additionally, we have proposed a model design that can support GVC and various types of visual prompts by connecting segmentation models with language models. Experimental results demonstrate that our model outperforms other LMMs on Grounding-Bench. Furthermore, our model achieves competitive performance on classic grounding benchmarks like RefCOCO/+/g and Flickr30K Entities. Our code will be released at https://github.com/UX-Decoder/LLaVA-Grounding .

</details>

### GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73337-6_8) · 📚 被引 3
- **作者**: Henry Hengyuan Zhao, Pan Zhou, Mike Zheng Shou
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### UniCode: Learning a Unified Codebook for Multimodal Large Language Models.
- **链接**: [arXiv:2403.09072](https://arxiv.org/abs/2403.09072) · 📚 被引 5
- **作者**: Sipeng Zheng, Bohan Zhou, Yicheng Feng, Ye Wang, Zongqing Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose \textbf{UniCode}, a novel approach within the domain of multimodal large language models (MLLMs) that learns a unified codebook to efficiently tokenize visual, text, and potentially other types of signals. This innovation addresses a critical limitation in existing MLLMs: their reliance on a text-only codebook, which restricts MLLM's ability to generate images and texts in a multimodal context. Towards this end, we propose a language-driven iterative training paradigm, coupled with an in-context pre-training task we term ``image decompression'', enabling our model to interpret compressed visual data and generate high-quality images.The unified codebook empowers our model to extend visual instruction tuning to non-linguistic generation tasks. Moreover, UniCode is adaptable to diverse stacked quantization approaches in order to compress visual signals into a more compact token representation. Despite using significantly fewer parameters and less data during training, Unicode demonstrates promising capabilities in visual reconstruction and generation. It also achieves performances comparable to leading MLLMs across a spectrum of VQA benchmarks.

</details>

## 跨领域论文（完整笔记在其他领域）

- OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web. → [multimodal](../multimodal/Guideline%202024.md)
- MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MLLM-CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Visual Programming for Zero-Shot Open-Vocabulary 3D Visual Grounding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- VCoder: Versatile Vision Encoders for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation. → [multimodal](../multimodal/Guideline%202024.md)
- ViP-LLaVA: Making Large Multimodal Models Understand Arbitrary Visual Prompts. → [multimodal](../multimodal/Guideline%202024.md)
- Honeybee: Locality-Enhanced Projector for Multimodal LLM. → [multimodal](../multimodal/Guideline%202024.md)
- LION : Empowering Multimodal Large Language Model with Dual-Level Visual Knowledge. → [multimodal](../multimodal/Guideline%202024.md)
- SmartEdit: Exploring Complex Instruction-Based Image Editing with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Hallucination Augmented Contrastive Learning for Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202024.md)
- SEED-Bench: Benchmarking Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Sniffer: Multimodal Large Language Model for Explainable Out-of-Context Misinformation Detection. → [multimodal](../multimodal/Guideline%202024.md)
- TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
- Link-Context Learning for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Cloud-Device Collaborative Learning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Towards Language-Driven Video Inpainting via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- GSVA: Generalized Segmentation via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Exploring the Transferability of Visual Prompting for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Unlocking Textual and Visual Wisdom: Open-Vocabulary 3D Object Detection Enhanced by Comprehensive Guidance from Text and Image. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Learning. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- BenchLMM: Benchmarking Cross-Style Visual Capability of Large Multimodal Models. → [multimodal](../multimodal/Guideline%202024.md)
- Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Dolphins: Multimodal Language Model for Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Self-supervised Visual Learning from Interactions with Objects. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Self-Supervised Audio-Visual Soundscape Stylization. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Learning the Unlearned: Mitigating Feature Suppression in Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Contrasting Deepfakes Diffusion via Contrastive Learning and Global-Local Similarities. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Meta-optimized Angular Margin Contrastive Framework for Video-Language Representation Learning. → [video-understanding](../video-understanding/Guideline%202024.md)
<!-- COMPLETE v1 papers=152 -->
