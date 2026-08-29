# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 88 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology.
- **链接**: [arXiv:2410.07087](https://arxiv.org/abs/2410.07087)
- **作者**: Xiangyu Wang, Donglin Yang, Ziqin Wang, Hohin Kwan, Jinyu Chen, Wenjun Wu et al.
- **🏷️ 机构**: CUHK
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Developing agents capable of navigating to a target location based on language instructions and visual information, known as vision-language navigation (VLN), has attracted widespread interest. Most research has focused on ground-based agents, while UAV-based VLN remains relatively underexplored. Recent efforts in UAV vision-language navigation predominantly adopt ground-based VLN settings, relying on predefined discrete action spaces and neglecting the inherent disparities in agent movement dynamics and the complexity of navigation tasks between ground and aerial environments. To address these disparities and challenges, we propose solutions from three perspectives: platform, benchmark, and methodology. To enable realistic UAV trajectory simulation in VLN tasks, we propose the OpenUAV platform, which features diverse environments, realistic flight control, and extensive algorithmic support. We further construct a target-oriented VLN dataset consisting of approximately 12k trajectories on this platform, serving as the first dataset specifically designed for realistic UAV VLN tasks. To tackle the challenges posed by complex aerial environments, we propose an assistant-guided UAV object search benchmark called UAV-Need-Help, which provides varying levels of guidance information to help UAVs better accomplish realistic VLN tasks. We also propose a UAV navigation LLM that, given multi-view images, task descriptions, and assistant instructions, leverages the multimodal understanding capabilities of the MLLM to jointly process visual and textual information, and performs hierarchical trajectory generation. The evaluation results of our method significantly outperform the baseline models, while there remains a considerable gap between our results and those achieved by human operators, underscoring the challenge presented by the UAV-Need-Help task.

</details>

### DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models.
- **链接**: [arXiv:2411.00836](https://arxiv.org/abs/2411.00836)
- **作者**: Chengke Zou, Xingang Guo, Rui Yang, Junyu Zhang, Bin Hu, Huan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advancements in Vision-Language Models (VLMs) have shown great potential in tackling mathematical reasoning tasks that involve visual context. Unlike humans who can reliably apply solution steps to similar problems with minor modifications, we found that SOTA VLMs like GPT-4o can consistently fail in these scenarios, revealing limitations in their mathematical reasoning capabilities. In this paper, we investigate the mathematical reasoning robustness in VLMs and evaluate how well these models perform under different variants of the same question, such as changes in visual numerical values or function graphs. While several vision-based math benchmarks have been developed to assess VLMs' problem-solving capabilities, these benchmarks contain only static sets of problems and cannot easily evaluate mathematical reasoning robustness. To fill this gap, we introduce DynaMath, a dynamic visual math benchmark designed for in-depth assessment of VLMs. DynaMath includes 501 high-quality, multi-topic seed questions, each represented as a Python program. Those programs are carefully designed and annotated to enable the automatic generation of a much larger set of concrete questions, including many different types of visual and textual variations. DynaMath allows us to evaluate the generalization ability of VLMs, by assessing their performance under varying input conditions of a seed question. We evaluated 14 SOTA VLMs with 5,010 generated concrete questions. Our results show that the worst-case model accuracy, defined as the percentage of correctly answered seed questions in all 10 variants, is significantly lower than the average-case accuracy. Our analysis emphasizes the need to study the robustness of VLMs' reasoning abilities, and DynaMath provides valuable insights to guide the development of more reliable models for mathematical reasoning.

</details>

### Tracking the Copyright of Large Vision-Language Models through Parameter Learning Adversarial Images.
- **链接**: [arXiv:2502.16593](https://arxiv.org/abs/2502.16593)
- **作者**: Yubo Wang, Jianting Tang, Chaohu Liu, Linli Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (LVLMs) have demonstrated remarkable image understanding and dialogue capabilities, allowing them to handle a variety of visual question answering tasks. However, their widespread availability raises concerns about unauthorized usage and copyright infringement, where users or individuals can develop their own LVLMs by fine-tuning published models. In this paper, we propose a novel method called Parameter Learning Attack (PLA) for tracking the copyright of LVLMs without modifying the original model. Specifically, we construct adversarial images through targeted attacks against the original model, enabling it to generate specific outputs. To ensure these attacks remain effective on potential fine-tuned models to trigger copyright tracking, we allow the original model to learn the trigger images by updating parameters in the opposite direction during the adversarial attack process. Notably, the proposed method can be applied after the release of the original model, thus not affecting the model's performance and behavior. To simulate real-world applications, we fine-tune the original model using various strategies across diverse datasets, creating a range of models for copyright verification. Extensive experiments demonstrate that our method can more effectively identify the original copyright of fine-tuned models compared to baseline methods. Therefore, this work provides a powerful tool for tracking copyrights and detecting unlicensed usage of LVLMs.

</details>

### Prompt as Knowledge Bank: Boost Vision-language model via Structural Representation for zero-shot medical detection.
- **链接**: [arXiv:2502.16223](https://arxiv.org/abs/2502.16223)
- **作者**: Yuguang Yang, Tongfei Chen, Haoyu Huang, Linlin Yang, Chunyu Xie, Dawei Leng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot medical detection can further improve detection performance without relying on annotated medical images even upon the fine-tuned model, showing great clinical value. Recent studies leverage grounded vision-language models (GLIP) to achieve this by using detailed disease descriptions as prompts for the target disease name during the inference phase. However, these methods typically treat prompts as equivalent context to the target name, making it difficult to assign specific disease knowledge based on visual information, leading to a coarse alignment between images and target descriptions. In this paper, we propose StructuralGLIP, which introduces an auxiliary branch to encode prompts into a latent knowledge bank layer-by-layer, enabling more context-aware and fine-grained alignment. Specifically, in each layer, we select highly similar features from both the image representation and the knowledge bank, forming structural representations that capture nuanced relationships between image patches and target descriptions. These features are then fused across modalities to further enhance detection performance. Extensive experiments demonstrate that StructuralGLIP achieves a +4.1\% AP improvement over prior state-of-the-art methods across seven zero-shot medical detection benchmarks, and consistently improves fine-tuned models by +3.2\% AP on endoscopy image datasets.

</details>

### How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?
- **链接**: [arXiv:2410.07571](https://arxiv.org/abs/2410.07571)
- **作者**: Seongyun Lee, Geewook Kim, Jiyeon Kim, Hyunji Lee, Hoyeon Chang, Sue Hyun Park et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language adaptation (VL adaptation) transforms Large Language Models (LLMs) into Large Vision-Language Models (LVLMs) for multimodal tasks, but this process often compromises the inherent safety capabilities embedded in the original LLMs. Despite potential harmfulness due to weakened safety measures, in-depth analysis on the effects of VL adaptation on safety remains under-explored. This study examines how VL adaptation influences safety and evaluates the impact of safety fine-tuning methods. Our analysis reveals that safety degradation occurs during VL adaptation, even when the training data is safe. While safety tuning techniques like supervised fine-tuning with safety datasets or reinforcement learning from human feedback mitigate some risks, they still lead to safety degradation and a reduction in helpfulness due to over-rejection issues. Further analysis of internal model weights suggests that VL adaptation may impact certain safety-related layers, potentially lowering overall safety levels. Additionally, our findings demonstrate that the objectives of VL adaptation and safety tuning are divergent, which often results in their simultaneous application being suboptimal. To address this, we suggest the weight merging approach as an optimal solution effectively reducing safety degradation while maintaining helpfulness. These insights help guide the development of more reliable and secure LVLMs for real-world applications.

</details>

### Natural Language Inference Improves Compositionality in Vision-Language Models.
- **链接**: [arXiv:2410.22315](https://arxiv.org/abs/2410.22315)
- **作者**: Paola Cascante-Bonilla, Yu Hou, Yang Trista Cao, Hal Daumé III, Rachel Rudinger
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compositional reasoning in Vision-Language Models (VLMs) remains challenging as these models often struggle to relate objects, attributes, and spatial relationships. Recent methods aim to address these limitations by relying on the semantics of the textual description, using Large Language Models (LLMs) to break them down into subsets of questions and answers. However, these methods primarily operate on the surface level, failing to incorporate deeper lexical understanding while introducing incorrect assumptions generated by the LLM. In response to these issues, we present Caption Expansion with Contradictions and Entailments (CECE), a principled approach that leverages Natural Language Inference (NLI) to generate entailments and contradictions from a given premise. CECE produces lexically diverse sentences while maintaining their core meaning. Through extensive experiments, we show that CECE enhances interpretability and reduces overreliance on biased or superficial features. By balancing CECE along the original premise, we achieve significant improvements over previous methods without requiring additional fine-tuning, producing state-of-the-art results on benchmarks that score agreement with human judgments for image-text alignment, and achieving an increase in performance on Winoground of +19.2% (group score) and +12.9% on EqBen (group score) over the best prior work (finetuned with targeted data).

</details>

### Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models.
- **链接**: [arXiv:2502.06130](https://arxiv.org/abs/2502.06130) · [代码](https://github.com/zhangce01/DeGF)
- **作者**: Ce Zhang, Zifu Wan, Zhehan Kan, Martin Q. Ma, Simon Stepputtis, Deva Ramanan et al.
- **🏷️ 机构**: CMU
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While recent Large Vision-Language Models (LVLMs) have shown remarkable performance in multi-modal tasks, they are prone to generating hallucinatory text responses that do not align with the given visual input, which restricts their practical applicability in real-world scenarios. In this work, inspired by the observation that the text-to-image generation process is the inverse of image-conditioned response generation in LVLMs, we explore the potential of leveraging text-to-image generative models to assist in mitigating hallucinations in LVLMs. We discover that generative models can offer valuable self-feedback for mitigating hallucinations at both the response and token levels. Building on this insight, we introduce self-correcting Decoding with Generative Feedback (DeGF), a novel training-free algorithm that incorporates feedback from text-to-image generative models into the decoding process to effectively mitigate hallucinations in LVLMs. Specifically, DeGF generates an image from the initial response produced by LVLMs, which acts as an auxiliary visual reference and provides self-feedback to verify and correct the initial response through complementary or contrastive decoding. Extensive experimental results validate the effectiveness of our approach in mitigating diverse types of hallucinations, consistently surpassing state-of-the-art methods across six benchmarks. Code is available at https://github.com/zhangce01/DeGF.

</details>

### Are Large Vision Language Models Good Game Players?
- **链接**: [arXiv:2503.02358](https://arxiv.org/abs/2503.02358) · [代码](https://github.com/xinke-wang/LVLM-Playground)
- **作者**: Xinyu Wang, Bohan Zhuang, Qi Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision Language Models (LVLMs) have demonstrated remarkable abilities in understanding and reasoning about both visual and textual information. However, existing evaluation methods for LVLMs, primarily based on benchmarks like Visual Question Answering and image captioning, often fail to capture the full scope of LVLMs' capabilities. These benchmarks are limited by issues such as inadequate assessment of detailed visual perception, data contamination, and a lack of focus on multi-turn reasoning. To address these challenges, we propose \method{}, a game-based evaluation framework designed to provide a comprehensive assessment of LVLMs' cognitive and reasoning skills in structured environments. \method{} uses a set of games to evaluate LVLMs on four core tasks: Perceiving, Question Answering, Rule Following, and End-to-End Playing, with each target task designed to assess specific abilities, including visual perception, reasoning, decision-making, etc. Based on this framework, we conduct extensive experiments that explore the limitations of current LVLMs, such as handling long structured outputs and perceiving detailed and dense elements. Code and data are publicly available at https://github.com/xinke-wang/LVLM-Playground.

</details>

### Generating CAD Code with Vision-Language Models for 3D Designs.
- **链接**: [arXiv:2410.05340](https://arxiv.org/abs/2410.05340)
- **作者**: Kamel Alrashedy, Pradyumna Tambwekar, Zulfiqar Haider Zaidi, Megan Langwasser, Wei Xu, Matthew C. Gombolay
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generative AI has transformed the fields of Design and Manufacturing by providing efficient and automated methods for generating and modifying 3D objects. One approach involves using Large Language Models (LLMs) to generate Computer- Aided Design (CAD) scripting code, which can then be executed to render a 3D object; however, the resulting 3D object may not meet the specified requirements. Testing the correctness of CAD generated code is challenging due to the complexity and structure of 3D objects (e.g., shapes, surfaces, and dimensions) that are not feasible in code. In this paper, we introduce CADCodeVerify, a novel approach to iteratively verify and improve 3D objects generated from CAD code. Our approach works by producing ameliorative feedback by prompting a Vision-Language Model (VLM) to generate and answer a set of validation questions to verify the generated object and prompt the VLM to correct deviations. To evaluate CADCodeVerify, we introduce, CADPrompt, the first benchmark for CAD code generation, consisting of 200 natural language prompts paired with expert-annotated scripting code for 3D objects to benchmark progress. Our findings show that CADCodeVerify improves VLM performance by providing visual feedback, enhancing the structure of the 3D objects, and increasing the success rate of the compiled program. When applied to GPT-4, CADCodeVerify achieved a 7.30% reduction in Point Cloud distance and a 5.0% improvement in success rate compared to prior work

</details>

### Attribute-based Visual Reprogramming for Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=j964C6y92q)
- **作者**: Chengyi Cai, Zesheng Ye, Lei Feng, Jianzhong Qi, Feng Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Noisy Test-Time Adaptation in Vision-Language Models.
- **链接**: [arXiv:2502.14604](https://arxiv.org/abs/2502.14604) · [代码](https://github.com/tmlr-group/ZS-NTTA)
- **作者**: Chentao Cao, Zhun Zhong, Zhanke Zhou, Tongliang Liu, Yang Liu, Kun Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation (TTA) aims to address distribution shifts between source and target data by relying solely on target data during testing. In open-world scenarios, models often encounter noisy samples, i.e., samples outside the in-distribution (ID) label space. Leveraging the zero-shot capability of pre-trained vision-language models (VLMs), this paper introduces Zero-Shot Noisy TTA (ZS-NTTA), focusing on adapting the model to target data with noisy samples during test-time in a zero-shot manner. We find existing TTA methods underperform under ZS-NTTA, often lagging behind even the frozen model. We conduct comprehensive experiments to analyze this phenomenon, revealing that the negative impact of unfiltered noisy data outweighs the benefits of clean data during model updating. Also, adapting a classifier for ID classification and noise detection hampers both sub-tasks. Built on this, we propose a framework that decouples the classifier and detector, focusing on developing an individual detector while keeping the classifier frozen. Technically, we introduce the Adaptive Noise Detector (AdaND), which utilizes the frozen model's outputs as pseudo-labels to train a noise detector. To handle clean data streams, we further inject Gaussian noise during adaptation, preventing the detector from misclassifying clean samples as noisy. Beyond the ZS-NTTA, AdaND can also improve the zero-shot out-of-distribution (ZS-OOD) detection ability of VLMs. Experiments show that AdaND outperforms in both ZS-NTTA and ZS-OOD detection. On ImageNet, AdaND achieves a notable improvement of $8.32\%$ in harmonic mean accuracy ($\text{Acc}_\text{H}$) for ZS-NTTA and $9.40\%$ in FPR95 for ZS-OOD detection, compared to SOTA methods. Importantly, AdaND is computationally efficient and comparable to the model-frozen method. The code is publicly available at: https://github.com/tmlr-group/ZS-NTTA.

</details>

### LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension.
- **链接**: [出版页](https://openreview.net/forum?id=PgXpOOqtyd)
- **作者**: Amaia Cardiel, Eloi Zablocki, Elias Ramzi, Oriane Siméoni, Matthieu Cord
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding.
- **链接**: [arXiv:2501.16411](https://arxiv.org/abs/2501.16411)
- **作者**: Wei Chow, Jiageng Mao, Boyi Li, Daniel Seita, Vitor Campagnolo Guizilini, Yue Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding the physical world is a fundamental challenge in embodied AI, critical for enabling agents to perform complex tasks and operate safely in real-world environments. While Vision-Language Models (VLMs) have shown great promise in reasoning and task planning for embodied agents, their ability to comprehend physical phenomena remains extremely limited. To close this gap, we introduce PhysBench, a comprehensive benchmark designed to evaluate VLMs' physical world understanding capability across a diverse set of tasks. PhysBench contains 10,002 entries of interleaved video-image-text data, categorized into four major domains: physical object properties, physical object relationships, physical scene understanding, and physics-based dynamics, further divided into 19 subclasses and 8 distinct capability dimensions. Our extensive experiments, conducted on 75 representative VLMs, reveal that while these models excel in common-sense reasoning, they struggle with understanding the physical world -- likely due to the absence of physical knowledge in their training data and the lack of embedded physical priors. To tackle the shortfall, we introduce PhysAgent, a novel framework that combines the generalization strengths of VLMs with the specialized expertise of vision models, significantly enhancing VLMs' physical understanding across a variety of tasks, including an 18.4\% improvement on GPT-4o. Furthermore, our results demonstrate that enhancing VLMs' physical world understanding capabilities can help embodied agents such as MOKA. We believe that PhysBench and PhysAgent offer valuable insights and contribute to bridging the gap between VLMs and physical world understanding.

</details>

### Locality Alignment Improves Vision-Language Models.
- **链接**: [arXiv:2410.11087](https://arxiv.org/abs/2410.11087)
- **作者**: Ian Connick Covert, Tony Sun, James Zou, Tatsunori Hashimoto
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision language models (VLMs) have seen growing adoption in recent years, but many still struggle with basic spatial reasoning errors. We hypothesize that this is due to VLMs adopting pre-trained vision backbones, specifically vision transformers (ViTs) trained with image-level supervision and minimal inductive biases. Such models may fail to encode the class contents at each position in the image, and our goal is to resolve this with a vision backbone that effectively captures both local and global image semantics. Our main insight is that we do not require new supervision to learn this capability - pre-trained models contain significant knowledge of local semantics that we can extract and use for scalable self-supervision. We propose a new efficient post-training stage for ViTs called locality alignment and a novel fine-tuning procedure called MaskEmbed that uses a masked reconstruction loss to learn semantic contributions for each image patch. We first evaluate locality alignment with a vision-only benchmark, finding that it improves a model's performance at patch-level semantic segmentation, especially for strong backbones trained with image-caption pairs (e.g., CLIP and SigLIP). We then train a series of VLMs with and without locality alignment, and show that locality-aligned backbones improve performance across a range of benchmarks, particularly ones that involve spatial understanding (e.g., RefCOCO, OCID-Ref, TallyQA, VSR, AI2D). Overall, we demonstrate that we can efficiently learn local semantic extraction via a locality alignment stage, and that this procedure benefits VLM training recipes that use off-the-shelf vision backbones.

</details>

### Tree of Attributes Prompt Learning for Vision-Language Models.
- **链接**: [arXiv:2410.11201](https://arxiv.org/abs/2410.11201) · [代码](https://github.com/HHenryD/TAP)
- **作者**: Tong Ding, Wanhua Li, Zhongqi Miao, Hanspeter Pfister
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning has proven effective in adapting vision language models for downstream tasks. However, existing methods usually append learnable prompt tokens solely with the category names to obtain textual features, which fails to fully leverage the rich context indicated in the category name. To address this issue, we propose the Tree of Attributes Prompt learning (TAP), which first instructs LLMs to generate a tree of attributes with a "concept - attribute - description" structure for each category, and then learn the hierarchy with vision and text prompt tokens. Unlike existing methods that merely augment category names with a set of unstructured descriptions, our approach essentially distills structured knowledge graphs associated with class names from LLMs. Furthermore, our approach introduces text and vision prompts designed to explicitly learn the corresponding visual attributes, effectively serving as domain experts. Additionally, the general and diverse descriptions generated based on the class names may be wrong or absent in the specific given images. To address this misalignment, we further introduce a vision-conditional pooling module to extract instance-specific text features. Extensive experimental results demonstrate that our approach outperforms state-of-the-art methods on the zero-shot base-to-novel generalization, cross-dataset transfer, as well as few-shot classification across 11 diverse datasets. Code is available at https://github.com/HHenryD/TAP.

</details>

### ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time.
- **链接**: [arXiv:2410.06625](https://arxiv.org/abs/2410.06625) · [代码](https://github.com/DripNowhy/ETA)
- **作者**: Yi Ding, Bolian Li, Ruqi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Language Models (VLMs) have become essential backbones for multimodal intelligence, yet significant safety challenges limit their real-world application. While textual inputs are often effectively safeguarded, adversarial visual inputs can easily bypass VLM defense mechanisms. Existing defense methods are either resource-intensive, requiring substantial data and compute, or fail to simultaneously ensure safety and usefulness in responses. To address these limitations, we propose a novel two-phase inference-time alignment framework, Evaluating Then Aligning (ETA): 1) Evaluating input visual contents and output responses to establish a robust safety awareness in multimodal settings, and 2) Aligning unsafe behaviors at both shallow and deep levels by conditioning the VLMs' generative distribution with an interference prefix and performing sentence-level best-of-N to search the most harmless and helpful generation paths. Extensive experiments show that ETA outperforms baseline methods in terms of harmlessness, helpfulness, and efficiency, reducing the unsafe rate by 87.5% in cross-modality attacks and achieving 96.6% win-ties in GPT-4 helpfulness evaluation. The code is publicly available at https://github.com/DripNowhy/ETA.

</details>

### ColPali: Efficient Document Retrieval with Vision Language Models.
- **链接**: [arXiv:2407.01449](https://arxiv.org/abs/2407.01449)
- **作者**: Manuel Faysse, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, Céline Hudelot et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Documents are visually rich structures that convey information through text, but also figures, page layouts, tables, or even fonts. Since modern retrieval systems mainly rely on the textual information they extract from document pages to index documents -often through lengthy and brittle processes-, they struggle to exploit key visual cues efficiently. This limits their capabilities in many practical document retrieval applications such as Retrieval Augmented Generation (RAG). To benchmark current systems on visually rich document retrieval, we introduce the Visual Document Retrieval Benchmark ViDoRe, composed of various page-level retrieval tasks spanning multiple domains, languages, and practical settings. The inherent complexity and performance shortcomings of modern systems motivate a new concept; doing document retrieval by directly embedding the images of the document pages. We release ColPali, a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages. Combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable. We release models, data, code and benchmarks under open licenses at https://hf.co/vidore.

</details>

### TLDR: Token-Level Detective Reward Model for Large Vision Language Models.
- **链接**: [arXiv:2410.04734](https://arxiv.org/abs/2410.04734)
- **作者**: Deqing Fu, Tong Xiao, Rui Wang, Wang Zhu, Pengchuan Zhang, Guan Pang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although reward models have been successful in improving multimodal large language models, the reward models themselves remain brutal and contain minimal information. Notably, existing reward models only mimic human annotations by assigning only one binary feedback to any text, no matter how long the text is. In the realm of multimodal language models, where models are required to process both images and texts, a naive reward model may learn implicit biases toward texts and become less grounded in images. In this paper, we propose a $\textbf{T}$oken-$\textbf{L}$evel $\textbf{D}$etective $\textbf{R}$eward Model ($\textbf{TLDR}$) to provide fine-grained annotations to each text token. We first introduce a perturbation-based method to generate synthetic hard negatives and their token-level labels to train TLDR models. Then we show the rich usefulness of TLDR models both in assisting off-the-shelf models to self-correct their generations, and in serving as a hallucination evaluation tool. We show that TLDR automatically trains a token-level likelihood optimization, and can improve the base model's performance significantly. Finally, we show that TLDR models can significantly speed up human annotation by 3 times to acquire a broader range of high-quality vision language data.

</details>

### Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models.
- **链接**: [arXiv:2408.02032](https://arxiv.org/abs/2408.02032)
- **作者**: Fushuo Huo, Wenchao Xu, Zhong Zhang, Haozhao Wang, Zhicheng Chen, Peilin Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Large Vision-Language Models (LVLMs) have rapidly advanced in recent years, the prevalent issue known as the `hallucination' problem has emerged as a significant bottleneck, hindering their real-world deployments. Existing methods mitigate this issue mainly from two perspectives: One approach leverages extra knowledge like robust instruction tuning LVLMs with curated datasets or employing auxiliary analysis networks, which inevitable incur additional costs. Another approach, known as contrastive decoding, induces hallucinations by manually disturbing the vision or instruction raw inputs and mitigates them by contrasting the outputs of the disturbed and original LVLMs. However, these approaches rely on empirical holistic input disturbances and double the inference cost. To avoid these issues, we propose a simple yet effective method named Self-Introspective Decoding (SID). Our empirical investigation reveals that pretrained LVLMs can introspectively assess the importance of vision tokens based on preceding vision and text (both instruction and generated) tokens. We develop the Context and Text-aware Token Selection (CT2S) strategy, which preserves only unimportant vision tokens after early layers of LVLMs to adaptively amplify text-informed hallucination during the auto-regressive decoding. This approach ensures that multimodal knowledge absorbed in the early layers induces multimodal contextual rather than aimless hallucinations. Subsequently, the original token logits subtract the amplified vision-and-text association hallucinations, guiding LVLMs decoding faithfully. Extensive experiments illustrate SID generates less-hallucination and higher-quality texts across various metrics, without extra knowledge and much additional computation burdens.

</details>

### TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data.
- **链接**: [arXiv:2410.06234](https://arxiv.org/abs/2410.06234) · [代码](https://github.com/ermongroup/TEOChat)
- **作者**: Jeremy Andrew Irvin, Emily Ruoyu Liu, Joyce Chuyi Chen, Ines Dormoy, Jinyoung Kim, Samar Khanna et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision and language assistants have enabled new capabilities for interpreting natural images. These approaches have recently been adapted to earth observation data, but they are only able to handle single image inputs, limiting their use for many real-world tasks. In this work, we develop a new vision and language assistant called TEOChat that can engage in conversations about temporal sequences of earth observation data. To train TEOChat, we curate an instruction-following dataset composed of many single image and temporal tasks including building change and damage assessment, semantic change detection, and temporal scene classification. We show that TEOChat can perform a wide variety of spatial and temporal reasoning tasks, substantially outperforming previous vision and language assistants, and even achieving comparable or better performance than several specialist models trained to perform specific tasks. Furthermore, TEOChat achieves impressive zero-shot performance on a change detection and change question answering dataset, outperforms GPT-4o and Gemini 1.5 Pro on multiple temporal tasks, and exhibits stronger single image capabilities than a comparable single image instruction-following model on scene classification, visual question answering, and captioning. We publicly release our data, model, and code at https://github.com/ermongroup/TEOChat .

</details>

### IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model.
- **链接**: [arXiv:2407.07577](https://arxiv.org/abs/2407.07577)
- **作者**: Yatai Ji, Shilong Zhang, Jie Wu, Peize Sun, Weifeng Chen, Xuefeng Xiao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advancement of Large Vision-Language models (LVLMs) has demonstrated a spectrum of emergent capabilities. Nevertheless, current models only focus on the visual content of a single scenario, while their ability to associate instances across different scenes has not yet been explored, which is essential for understanding complex visual content, such as movies with multiple characters and intricate plots. Towards movie understanding, a critical initial step for LVLMs is to unleash the potential of character identities memory and recognition across multiple visual scenarios. To achieve the goal, we propose visual instruction tuning with ID reference and develop an ID-Aware Large Vision-Language Model, IDA-VLM. Furthermore, our research introduces a novel benchmark MM-ID, to examine LVLMs on instance IDs memory and recognition across four dimensions: matching, location, question-answering, and captioning. Our findings highlight the limitations of existing LVLMs in recognizing and associating instance identities with ID reference. This paper paves the way for future artificial intelligence systems to possess multi-identity visual inputs, thereby facilitating the comprehension of complex visual narratives like movies.

</details>

### Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation.
- **链接**: [出版页](https://openreview.net/forum?id=R4h5PXzUuU)
- **作者**: Jihyo Kim, Seulbi Lee, Sangheum Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model.
- **链接**: [arXiv:2410.13882](https://arxiv.org/abs/2410.13882)
- **作者**: Long Le, Jason Xie, William Liang, Hung-Ju Wang, Yue Yang, Yecheng Jason Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Interactive 3D simulated objects are crucial in AR/VR, animations, and robotics, driving immersive experiences and advanced automation. However, creating these articulated objects requires extensive human effort and expertise, limiting their broader applications. To overcome this challenge, we present Articulate-Anything, a system that automates the articulation of diverse, complex objects from many input modalities, including text, images, and videos. Articulate-Anything leverages vision-language models (VLMs) to generate code that can be compiled into an interactable digital twin for use in standard 3D simulators. Our system exploits existing 3D asset datasets via a mesh retrieval mechanism, along with an actor-critic system that iteratively proposes, evaluates, and refines solutions for articulating the objects, self-correcting errors to achieve a robust outcome. Qualitative evaluations demonstrate Articulate-Anything's capability to articulate complex and even ambiguous object affordances by leveraging rich grounded inputs. In extensive quantitative experiments on the standard PartNet-Mobility dataset, Articulate-Anything substantially outperforms prior work, increasing the success rate from 8.7-11.6% to 75% and setting a new bar for state-of-the-art performance. We further showcase the utility of our system by generating 3D assets from in-the-wild video inputs, which are then used to train robotic policies for fine-grained manipulation tasks in simulation that go beyond basic pick and place. These policies are then transferred to a real robotic system.

</details>

### RA-TTA: Retrieval-Augmented Test-Time Adaptation for Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=V3zobHnS61)
- **作者**: Youngjun Lee, Doyoung Kim, Junhyeok Kang, Jihwan Bang, Hwanjun Song, Jae-Gil Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Efficient and Context-Aware Label Propagation for Zero-/Few-Shot Training-Free Adaptation of Vision-Language Model.
- **链接**: [arXiv:2412.18303](https://arxiv.org/abs/2412.18303) · [代码](https://github.com/Yushu-Li/ECALP)
- **作者**: Yushu Li, Yongyi Su, Adam Goodge, Kui Jia, Xun Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have revolutionized machine learning by leveraging large pre-trained models to tackle various downstream tasks. Although label, training, and data efficiency have improved, many state-of-the-art VLMs still require task-specific hyperparameter tuning and fail to fully exploit test samples. To overcome these challenges, we propose a graph-based approach for label-efficient adaptation and inference. Our method dynamically constructs a graph over text prompts, few-shot examples, and test samples, using label propagation for inference without task-specific tuning. Unlike existing zero-shot label propagation techniques, our approach requires no additional unlabeled support set and effectively leverages the test sample manifold through dynamic graph expansion. We further introduce a context-aware feature re-weighting mechanism to improve task adaptation accuracy. Additionally, our method supports efficient graph expansion, enabling real-time inductive inference. Extensive evaluations on downstream tasks, such as fine-grained categorization and out-of-distribution generalization, demonstrate the effectiveness of our approach. The source code is available at https://github.com/Yushu-Li/ECALP.

</details>

### VLMaterial: Procedural Material Generation with Large Vision-Language Models.
- **链接**: [arXiv:2501.18623](https://arxiv.org/abs/2501.18623)
- **作者**: Beichen Li, Rundi Wu, Armando Solar-Lezama, Changxi Zheng, Liang Shi, Bernd Bickel et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Procedural materials, represented as functional node graphs, are ubiquitous in computer graphics for photorealistic material appearance design. They allow users to perform intuitive and precise editing to achieve desired visual appearances. However, creating a procedural material given an input image requires professional knowledge and significant effort. In this work, we leverage the ability to convert procedural materials into standard Python programs and fine-tune a large pre-trained vision-language model (VLM) to generate such programs from input images. To enable effective fine-tuning, we also contribute an open-source procedural material dataset and propose to perform program-level augmentation by prompting another pre-trained large language model (LLM). Through extensive evaluation, we show that our method outperforms previous methods on both synthetic and real-world examples.

</details>

### Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning.
- **链接**: [出版页](https://openreview.net/forum?id=zY37C8d6bS)
- **作者**: Tian-Shuo Liu, Xu-Hui Liu, Ruifeng Chen, Lixuan Jin, Pengyuan Wang, Zhilong Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering.
- **链接**: [出版页](https://openreview.net/forum?id=LBl7Hez0fF)
- **作者**: Sheng Liu, Haotian Ye, James Zou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models.
- **链接**: [arXiv:2410.17637](https://arxiv.org/abs/2410.17637)
- **作者**: Ziyu Liu, Yuhang Zang, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Haodong Duan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual preference alignment involves training Large Vision-Language Models (LVLMs) to predict human preferences between visual inputs. This is typically achieved by using labeled datasets of chosen/rejected pairs and employing optimization algorithms like direct preference optimization (DPO). Existing visual alignment methods, primarily designed for single-image scenarios, struggle to effectively handle the complexity of multi-image tasks due to the scarcity of diverse training data and the high cost of annotating chosen/rejected pairs. We present Multi-Image Augmented Direct Preference Optimization (MIA-DPO), a visual preference alignment approach that effectively handles multi-image inputs. MIA-DPO mitigates the scarcity of diverse multi-image training data by extending single-image data with unrelated images arranged in grid collages or pic-in-pic formats, significantly reducing the costs associated with multi-image data annotations. Our observation reveals that attention values of LVLMs vary considerably across different images. We use attention values to identify and filter out rejected responses the model may have mistakenly focused on. Our attention-aware selection for constructing the chosen/rejected pairs without relying on (i) human annotation, (ii) extra data, and (iii) external models or APIs. MIA-DPO is compatible with various architectures and outperforms existing methods on five multi-image benchmarks, achieving an average performance boost of 3.0% on LLaVA-v1.5 and 4.3% on the recent InternLM-XC2.5. Moreover, MIA-DPO has a minimal effect on the model's ability to understand single images.

</details>

### Mixture of Experts Made Personalized: Federated Prompt Learning for Vision-Language Models.
- **链接**: [arXiv:2410.10114](https://arxiv.org/abs/2410.10114) · [代码](https://github.com/ljaiverson/pFedMoAP)
- **作者**: Jun Luo, Chen Chen, Shandong Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Federated prompt learning benefits federated learning with CLIP-like Vision-Language Model's (VLM's) robust representation learning ability through prompt learning. However, current federated prompt learning methods are habitually restricted to the traditional FL paradigm, where the participating clients are generally only allowed to download a single globally aggregated model from the server. While justifiable for training full-sized models under federated settings, in this work, we argue that this paradigm is ill-suited for lightweight prompts. By facilitating the clients to download multiple pre-aggregated prompts as fixed non-local experts, we propose Personalized Federated Mixture of Adaptive Prompts (pFedMoAP), a novel FL framework that personalizes the prompt learning process through the lens of Mixture of Experts (MoE). pFedMoAP implements a local attention-based gating network that learns to generate enhanced text features for better alignment with local image data, benefiting from both local and downloaded non-local adaptive prompt experts. Extensive experiments on 9 datasets under various federated settings demonstrate the efficacy of the proposed pFedMoAP algorithm. The code is available at https://github.com/ljaiverson/pFedMoAP.

</details>

### Backdooring Vision-Language Models with Out-Of-Distribution Data.
- **链接**: [arXiv:2410.01264](https://arxiv.org/abs/2410.01264)
- **作者**: Weimin Lyu, Jiachen Yao, Saumya Gupta, Lu Pang, Tao Sun, Lingjie Yi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of Vision-Language Models (VLMs) represents a significant advancement in integrating computer vision with Large Language Models (LLMs) to generate detailed text descriptions from visual inputs. Despite their growing importance, the security of VLMs, particularly against backdoor attacks, is under explored. Moreover, prior works often assume attackers have access to the original training data, which is often unrealistic. In this paper, we address a more practical and challenging scenario where attackers must rely solely on Out-Of-Distribution (OOD) data. We introduce VLOOD (Backdooring Vision-Language Models with Out-of-Distribution Data), a novel approach with two key contributions: (1) demonstrating backdoor attacks on VLMs in complex image-to-text tasks while minimizing degradation of the original semantics under poisoned inputs, and (2) proposing innovative techniques for backdoor injection without requiring any access to the original training data. Our evaluation on image captioning and visual question answering (VQA) tasks confirms the effectiveness of VLOOD, revealing a critical security vulnerability in VLMs and laying the foundation for future research on securing multimodal models against sophisticated threats.

</details>

### Vision Language Models are In-Context Value Learners.
- **链接**: [arXiv:2411.04549](https://arxiv.org/abs/2411.04549)
- **作者**: Yecheng Jason Ma, Joey Hejna, Chuyuan Fu, Dhruv Shah, Jacky Liang, Zhuo Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting temporal progress from visual trajectories is important for intelligent robots that can learn, adapt, and improve. However, learning such progress estimator, or temporal value function, across different tasks and domains requires both a large amount of diverse data and methods which can scale and generalize. To address these challenges, we present Generative Value Learning (\GVL), a universal value function estimator that leverages the world knowledge embedded in vision-language models (VLMs) to predict task progress. Naively asking a VLM to predict values for a video sequence performs poorly due to the strong temporal correlation between successive frames. Instead, GVL poses value estimation as a temporal ordering problem over shuffled video frames; this seemingly more challenging task encourages VLMs to more fully exploit their underlying semantic and temporal grounding capabilities to differentiate frames based on their perceived task progress, consequently producing significantly better value predictions. Without any robot or task specific training, GVL can in-context zero-shot and few-shot predict effective values for more than 300 distinct real-world tasks across diverse robot platforms, including challenging bimanual manipulation tasks. Furthermore, we demonstrate that GVL permits flexible multi-modal in-context learning via examples from heterogeneous tasks and embodiments, such as human videos. The generality of GVL enables various downstream applications pertinent to visuomotor policy learning, including dataset filtering, success detection, and advantage-weighted regression -- all without any model training or finetuning.

</details>

### Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset.
- **链接**: [arXiv:2411.03554](https://arxiv.org/abs/2411.03554)
- **作者**: Yingzi Ma, Jiongxiao Wang, Fei Wang, Siyuan Ma, Jiazhao Li, Jinsheng Pan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine unlearning has emerged as an effective strategy for forgetting specific information in the training data. However, with the increasing integration of visual data, privacy concerns in Vision Language Models (VLMs) remain underexplored. To address this, we introduce Facial Identity Unlearning Benchmark (FIUBench), a novel VLM unlearning benchmark designed to robustly evaluate the effectiveness of unlearning algorithms under the Right to be Forgotten setting. Specifically, we formulate the VLM unlearning task via constructing the Fictitious Facial Identity VQA dataset and apply a two-stage evaluation pipeline that is designed to precisely control the sources of information and their exposure levels. In terms of evaluation, since VLM supports various forms of ways to ask questions with the same semantic meaning, we also provide robust evaluation metrics including membership inference attacks and carefully designed adversarial privacy attacks to evaluate the performance of algorithms. Through the evaluation of four baseline VLM unlearning algorithms within FIUBench, we find that all methods remain limited in their unlearning performance, with significant trade-offs between model utility and forget quality. Furthermore, our findings also highlight the importance of privacy attacks for robust evaluations. We hope FIUBench will drive progress in developing more effective VLM unlearning algorithms.

</details>

### Towards Interpreting Visual Information Processing in Vision-Language Models.
- **链接**: [arXiv:2410.07149](https://arxiv.org/abs/2410.07149)
- **作者**: Clement Neo, Luke Ong, Philip Torr, Mor Geva, David Krueger, Fazl Barez
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) are powerful tools for processing and understanding text and images. We study the processing of visual tokens in the language model component of LLaVA, a prominent VLM. Our approach focuses on analyzing the localization of object information, the evolution of visual token representations across layers, and the mechanism of integrating visual information for predictions. Through ablation studies, we demonstrated that object identification accuracy drops by over 70\% when object-specific tokens are removed. We observed that visual token representations become increasingly interpretable in the vocabulary space across layers, suggesting an alignment with textual tokens corresponding to image content. Finally, we found that the model extracts object information from these refined representations at the last token position for prediction, mirroring the process in text-only language models for factual association tasks. These findings provide crucial insights into how VLMs process and integrate visual information, bridging the gap between our understanding of language and vision models, and paving the way for more interpretable and controllable multimodal systems.

</details>

### Compositional Entailment Learning for Hyperbolic Vision-Language Models.
- **链接**: [arXiv:2410.06912](https://arxiv.org/abs/2410.06912)
- **作者**: Avik Pal, Max van Spengler, Guido Maria D'Amely di Melendugno, Alessandro Flaborea, Fabio Galasso, Pascal Mettes
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image-text representation learning forms a cornerstone in vision-language models, where pairs of images and textual descriptions are contrastively aligned in a shared embedding space. Since visual and textual concepts are naturally hierarchical, recent work has shown that hyperbolic space can serve as a high-potential manifold to learn vision-language representation with strong downstream performance. In this work, for the first time we show how to fully leverage the innate hierarchical nature of hyperbolic embeddings by looking beyond individual image-text pairs. We propose Compositional Entailment Learning for hyperbolic vision-language models. The idea is that an image is not only described by a sentence but is itself a composition of multiple object boxes, each with their own textual description. Such information can be obtained freely by extracting nouns from sentences and using openly available localized grounding models. We show how to hierarchically organize images, image boxes, and their textual descriptions through contrastive and entailment-based objectives. Empirical evaluation on a hyperbolic vision-language model trained with millions of image-text pairs shows that the proposed compositional learning approach outperforms conventional Euclidean CLIP learning, as well as recent hyperbolic alternatives, with better zero-shot and retrieval generalization and clearly stronger hierarchical performance.

</details>

### ZIP: An Efficient Zeroth-order Prompt Tuning for Black-box Vision-Language Models.
- **链接**: [arXiv:2504.06838](https://arxiv.org/abs/2504.06838)
- **作者**: Seonghwan Park, Jaehyeon Jeong, Yongjun Kim, Jaeho Lee, Namhoon Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have introduced various approaches for prompt-tuning black-box vision-language models, referred to as black-box prompt-tuning (BBPT). While BBPT has demonstrated considerable potential, it is often found that many existing methods require an excessive number of queries (i.e., function evaluations), which poses a significant challenge in real-world scenarios where the number of allowed queries is limited. To tackle this issue, we propose Zeroth-order Intrinsic-dimensional Prompt-tuning (ZIP), a novel approach that enables efficient and robust prompt optimization in a purely black-box setting. The key idea of ZIP is to reduce the problem dimensionality and the variance of zeroth-order gradient estimates, such that the training is done fast with far less queries. We achieve this by re-parameterizing prompts in low-rank representations and designing intrinsic-dimensional clipping of estimated gradients. We evaluate ZIP on 13+ vision-language tasks in standard benchmarks and show that it achieves an average improvement of approximately 6% in few-shot accuracy and 48% in query efficiency compared to the best-performing alternative BBPT methods, establishing a new state of the art. Our ablation analysis further shows that the proposed clipping mechanism is robust and nearly optimal, without the need to manually select the clipping threshold, matching the result of expensive hyperparameter search.

</details>

### Failures to Find Transferable Image Jailbreaks Between Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=wvFnqVVUhN)
- **作者**: Rylan Schaeffer, Dan Valentine, Luke Bailey, James Chua, Cristóbal Eyzaguirre, Zane Durante et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Two Effects, One Trigger: On the Modality Gap, Object Bias, and Information Imbalance in Contrastive Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=uAFHCZRmXk)
- **作者**: Simon Schrodi, David T. Hoffmann, Max Argus, Volker Fischer, Thomas Brox
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=JUr0YOMvZA)
- **作者**: Kaishen Wang, Hengrui Gu, Meijun Gao, Kaixiong Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention.
- **链接**: [出版页](https://openreview.net/forum?id=Bjq4W7P2Us)
- **作者**: Tianyun Yang, Ziniu Li, Juan Cao, Chang Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model.
- **链接**: [arXiv:2406.19905](https://arxiv.org/abs/2406.19905) · [代码](https://github.com/longrongyang/STGC)
- **作者**: Longrong Yang, Dong Shen, Chaoxiang Cai, Fan Yang, Tingting Gao, Di Zhang et al.
- **🏷️ 机构**: ZJU
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Mixture-of-Experts (MoE) has gained increasing attention in studying Large Vision-Language Models (LVLMs). It uses a sparse model to replace the dense model, achieving comparable performance while activating fewer parameters during inference, thus significantly reducing the inference cost. Existing MoE methods in LVLM encourage different experts to specialize in different tokens, and they usually employ a router to predict the routing of each token. However, the router is not optimized concerning distinct parameter optimization directions generated from tokens within an expert. This may lead to severe interference between tokens within an expert. To address this problem, we propose to use the token-level gradient analysis to Solving Token Gradient Conflict (STGC) in this paper. Specifically, we first use token-level gradients to identify conflicting tokens in experts. After that, we add a regularization loss tailored to encourage conflicting tokens routing from their current experts to other experts, for reducing interference between tokens within an expert. Our method can serve as a plug-in for diverse LVLM methods, and extensive experimental results demonstrate its effectiveness. The code will be publicly available at https://github.com/longrongyang/STGC.

</details>

### Do Vision-Language Models Represent Space and How? Evaluating Spatial Frame of Reference under Ambiguities.
- **链接**: [arXiv:2410.17385](https://arxiv.org/abs/2410.17385)
- **作者**: Zheyuan Zhang, Fengyuan Hu, Jayjun Lee, Freda Shi, Parisa Kordjamshidi, Joyce Chai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatial expressions in situated communication can be ambiguous, as their meanings vary depending on the frames of reference (FoR) adopted by speakers and listeners. While spatial language understanding and reasoning by vision-language models (VLMs) have gained increasing attention, potential ambiguities in these models are still under-explored. To address this issue, we present the COnsistent Multilingual Frame Of Reference Test (COMFORT), an evaluation protocol to systematically assess the spatial reasoning capabilities of VLMs. We evaluate nine state-of-the-art VLMs using COMFORT. Despite showing some alignment with English conventions in resolving ambiguities, our experiments reveal significant shortcomings of VLMs: notably, the models (1) exhibit poor robustness and consistency, (2) lack the flexibility to accommodate multiple FoRs, and (3) fail to adhere to language-specific or culture-specific conventions in cross-lingual tests, as English tends to dominate other languages. With a growing effort to align vision-language models with human cognitive intuitions, we call for more attention to the ambiguous nature and cross-cultural diversity of spatial reasoning.

</details>

### VCR: A Task for Pixel-Level Complex Reasoning in Vision Language Models via Restoring Occluded Text.
- **链接**: [出版页](https://openreview.net/forum?id=s0Z4csHOoE)
- **作者**: Tianyu Zhang, Suyuchen Wang, Lu Li, Ge Zhang, Perouz Taslakian, Sai Rajeswar et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination.
- **链接**: [arXiv:2410.09874](https://arxiv.org/abs/2410.09874) · 📚 被引 0
- **作者**: Xinxin Zhao, Wenzhe Cai, Likun Tang, Teng Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual navigation is an essential skill for home-assistance robots, providing the object-searching ability to accomplish long-horizon daily tasks. Many recent approaches use Large Language Models (LLMs) for commonsense inference to improve exploration efficiency. However, the planning process of LLMs is limited within texts and it is difficult to represent the spatial occupancy and geometry layout only by texts. Both are important for making rational navigation decisions. In this work, we seek to unleash the spatial perception and planning ability of Vision-Language Models (VLMs), and explore whether the VLM, with only on-board camera captured RGB/RGB-D stream inputs, can efficiently finish the visual navigation tasks in a mapless manner. We achieve this by developing the imagination-powered navigation framework ImagineNav, which imagines the future observation images at valuable robot views and translates the complex navigation planning process into a rather simple best-view image selection problem for VLM. To generate appropriate candidate robot views for imagination, we introduce the Where2Imagine module, which is distilled to align with human navigation habits. Finally, to reach the VLM preferred views, an off-the-shelf point-goal navigation policy is utilized. Empirical experiments on the challenging open-vocabulary object navigation benchmarks demonstrates the superiority of our proposed system.

</details>

### BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks.
- **链接**: [arXiv:2410.20971](https://arxiv.org/abs/2410.20971) · [代码](https://github.com/Vinsonzyh/BlueSuffix)
- **作者**: Yunhan Zhao, Xiang Zheng, Lin Luo, Yige Li, Xingjun Ma, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we focus on black-box defense for VLMs against jailbreak attacks. Existing black-box defense methods are either unimodal or bimodal. Unimodal methods enhance either the vision or language module of the VLM, while bimodal methods robustify the model through text-image representation realignment. However, these methods suffer from two limitations: 1) they fail to fully exploit the cross-modal information, or 2) they degrade the model performance on benign inputs. To address these limitations, we propose a novel blue-team method BlueSuffix that defends target VLMs against jailbreak attacks without compromising its performance under black-box setting. BlueSuffix includes three key components: 1) a visual purifier against jailbreak images, 2) a textual purifier against jailbreak texts, and 3) a blue-team suffix generator using reinforcement fine-tuning for enhancing cross-modal robustness. We empirically show on four VLMs (LLaVA, MiniGPT-4, InstructionBLIP, and Gemini) and four safety benchmarks (Harmful Instruction, AdvBench, MM-SafetyBench, and RedTeam-2K) that BlueSuffix outperforms the baseline defenses by a significant margin. Our BlueSuffix opens up a promising direction for defending VLMs against jailbreak attacks. Code is available at https://github.com/Vinsonzyh/BlueSuffix.

</details>

### DenseGrounding: Improving Dense Language-Vision Semantics for Ego-centric 3D Visual Grounding.
- **链接**: [arXiv:2505.04965](https://arxiv.org/abs/2505.04965)
- **作者**: Henry Zheng, Hao Shi, Qihang Peng, Yong Xien Chng, Rui Huang, Yepeng Weng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Enabling intelligent agents to comprehend and interact with 3D environments through natural language is crucial for advancing robotics and human-computer interaction. A fundamental task in this field is ego-centric 3D visual grounding, where agents locate target objects in real-world 3D spaces based on verbal descriptions. However, this task faces two significant challenges: (1) loss of fine-grained visual semantics due to sparse fusion of point clouds with ego-centric multi-view images, (2) limited textual semantic context due to arbitrary language descriptions. We propose DenseGrounding, a novel approach designed to address these issues by enhancing both visual and textual semantics. For visual features, we introduce the Hierarchical Scene Semantic Enhancer, which retains dense semantics by capturing fine-grained global scene features and facilitating cross-modal alignment. For text descriptions, we propose a Language Semantic Enhancer that leverages large language models to provide rich context and diverse language descriptions with additional context during model training. Extensive experiments show that DenseGrounding significantly outperforms existing methods in overall accuracy, with improvements of 5.81% and 7.56% when trained on the comprehensive full dataset and smaller mini subset, respectively, further advancing the SOTA in egocentric 3D visual grounding. Our method also achieves 1st place and receives the Innovation Award in the CVPR 2024 Autonomous Grand Challenge Multi-view 3D Visual Grounding Track, validating its effectiveness and robustness.

</details>

### Learning Interleaved Image-Text Comprehension in Vision-Language Large Models.
- **链接**: [出版页](https://openreview.net/forum?id=jZsN9zo8Qi)
- **作者**: Chenyu Zhou, Mengdan Zhang, Peixian Chen, Chaoyou Fu, Yunhang Shen, Xiawu Zheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### REMEDY: Recipe Merging Dynamics in Large Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=iX7eHHE5Tx)
- **作者**: Didi Zhu, Yibing Song, Tao Shen, Ziyu Zhao, Jinluan Yang, Min Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

## 跨领域论文（完整笔记在其他领域）

- MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans? → [multimodal](../multimodal/Guideline%202025.md)
- MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection. → [multimodal](../multimodal/Guideline%202025.md)
- MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs. → [multimodal](../multimodal/Guideline%202025.md)
- SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Duoduo CLIP: Efficient 3D Understanding with Multi-View Images. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Open-Vocabulary Customization from CLIP via Data-Free Knowledge Distillation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification. → [multimodal](../multimodal/Guideline%202025.md)
- MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks. → [multimodal](../multimodal/Guideline%202025.md)
- C-CLIP: Multimodal Continual Learning for Vision-Language Model. → [continual-learning](../continual-learning/Guideline%202025.md)
- MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration. → [network-pruning](../network-pruning/Guideline%202025.md)
- Cross-Modal Safety Mechanism Transfer in Large Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Mm-Embed: Universal Multimodal Retrieval with Multimodal LLMS. → [multimodal](../multimodal/Guideline%202025.md)
- MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training. → [multimodal](../multimodal/Guideline%202025.md)
- CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- RetroInText: A Multimodal Large Language Model Enhanced Framework for Retrosynthetic Planning via In-Context Representation Learning. → [multimodal](../multimodal/Guideline%202025.md)
- Bridging Compressed Image Latents and Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Grounding Multimodal Large Language Model in GUI World. → [multimodal](../multimodal/Guideline%202025.md)
- LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models. → [multimodal](../multimodal/Guideline%202025.md)
- Multimodal Large Language Models for Inverse Molecular Design with Retrosynthetic Planning. → [multimodal](../multimodal/Guideline%202025.md)
- γ-MoD: Exploring Mixture-of-Depth Adaptation for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders. → [multimodal](../multimodal/Guideline%202025.md)
- Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks. → [multimodal](../multimodal/Guideline%202025.md)
- Towards Semantic Equivalence of Tokenization in Multimodal LLM. → [multimodal](../multimodal/Guideline%202025.md)
- MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA. → [multimodal](../multimodal/Guideline%202025.md)
- Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages. → [multimodal](../multimodal/Guideline%202025.md)
- ScImage: How good are multimodal large language models at scientific text-to-image generation? → [multimodal](../multimodal/Guideline%202025.md)
- LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token. → [multimodal](../multimodal/Guideline%202025.md)
- MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning. → [multimodal](../multimodal/Guideline%202025.md)
- ZooProbe: A Data Engine for Evaluating, Exploring, and Evolving Large-scale Training Data for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality. → [multimodal](../multimodal/Guideline%202025.md)
- Narrowing Information Bottleneck Theory for Multimodal Image-Text Representations Interpretability. → [multimodal](../multimodal/Guideline%202025.md)
- Discovering Clone Negatives via Adaptive Contrastive Learning for Image-Text Matching. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
