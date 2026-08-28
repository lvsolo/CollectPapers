# VLM — 2024 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 94 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/1198b53fa686831d5f0c0860d7ec4f34-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 5
- **作者**: Han Huang, Haitian Zhong, Tao Yu, Qiang Liu, Shu Wu, Liang Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b69396afc07a9ca3428d194f4db84c02-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 4
- **作者**: Shuo Liu, Kaining Ying, Hao Zhang, Yue Yang, Yuqi Lin, Tianle Zhang et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2024

### VLM4Bio: A Benchmark Dataset to Evaluate Pretrained Vision-Language Models for Trait Discovery from Biological Images.
- **链接**: [arXiv:2408.16176](https://arxiv.org/abs/2408.16176) · [代码](https://github.com/sammarfy/VLM4Bio) · 📚 被引 2
- **作者**: M. Maruf, Arka Daw, Kazi Sajeed Mehrab, Harish Babu Manogaran, Abhilash Neog, Medha Sawhney et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Images are increasingly becoming the currency for documenting biodiversity on the planet, providing novel opportunities for accelerating scientific discoveries in the field of organismal biology, especially with the advent of large vision-language models (VLMs). We ask if pre-trained VLMs can aid scientists in answering a range of biologically relevant questions without any additional fine-tuning. In this paper, we evaluate the effectiveness of 12 state-of-the-art (SOTA) VLMs in the field of organismal biology using a novel dataset, VLM4Bio, consisting of 469K question-answer pairs involving 30K images from three groups of organisms: fishes, birds, and butterflies, covering five biologically relevant tasks. We also explore the effects of applying prompting techniques and tests for reasoning hallucination on the performance of VLMs, shedding new light on the capabilities of current SOTA VLMs in answering biologically relevant questions using images. The code and datasets for running all the analyses reported in this paper can be found at https://github.com/sammarfy/VLM4Bio.

</details>

### CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/fde7f40f8ced5735006810534dc66b33-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 18
- **作者**: Peng Xia, Ze Chen, Juanxi Tian, Yangrui Gong, Ruibo Hou, Yue Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### BenchX: A Unified Benchmark Framework for Medical Vision-Language Pretraining on Chest X-Rays.
- **链接**: [arXiv:2410.21969](https://arxiv.org/abs/2410.21969) · [代码](https://github.com/yangzhou12/BenchX) · 📚 被引 1
- **作者**: Yang Zhou, Tan Li Hui Faith, Yanyu Xu, Sicong Leng, Xinxing Xu, Yong Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Medical Vision-Language Pretraining (MedVLP) shows promise in learning generalizable and transferable visual representations from paired and unpaired medical images and reports. MedVLP can provide useful features to downstream tasks and facilitate adapting task-specific models to new setups using fewer examples. However, existing MedVLP methods often differ in terms of datasets, preprocessing, and finetuning implementations. This pose great challenges in evaluating how well a MedVLP method generalizes to various clinically-relevant tasks due to the lack of unified, standardized, and comprehensive benchmark. To fill this gap, we propose BenchX, a unified benchmark framework that enables head-to-head comparison and systematical analysis between MedVLP methods using public chest X-ray datasets. Specifically, BenchX is composed of three components: 1) Comprehensive datasets covering nine datasets and four medical tasks; 2) Benchmark suites to standardize data preprocessing, train-test splits, and parameter selection; 3) Unified finetuning protocols that accommodate heterogeneous MedVLP methods for consistent task adaptation in classification, segmentation, and report generation, respectively. Utilizing BenchX, we establish baselines for nine state-of-the-art MedVLP methods and found that the performance of some early MedVLP methods can be enhanced to surpass more recent ones, prompting a revisiting of the developments and conclusions from prior works in MedVLP. Our code are available at https://github.com/yangzhou12/BenchX.

</details>

### EZ-HOI: VLM Adaptation via Guided Prompt Learning for Zero-Shot HOI Detection.
- **链接**: [arXiv:2410.23904](https://arxiv.org/abs/2410.23904) · [代码](https://github.com/ChelsieLei/EZ-HOI) · 📚 被引 14
- **作者**: Qinqian Lei, Bo Wang, Robby T. Tan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting Human-Object Interactions (HOI) in zero-shot settings, where models must handle unseen classes, poses significant challenges. Existing methods that rely on aligning visual encoders with large Vision-Language Models (VLMs) to tap into the extensive knowledge of VLMs, require large, computationally expensive models and encounter training difficulties. Adapting VLMs with prompt learning offers an alternative to direct alignment. However, fine-tuning on task-specific datasets often leads to overfitting to seen classes and suboptimal performance on unseen classes, due to the absence of unseen class labels. To address these challenges, we introduce a novel prompt learning-based framework for Efficient Zero-Shot HOI detection (EZ-HOI). First, we introduce Large Language Model (LLM) and VLM guidance for learnable prompts, integrating detailed HOI descriptions and visual semantics to adapt VLMs to HOI tasks. However, because training datasets contain seen-class labels alone, fine-tuning VLMs on such datasets tends to optimize learnable prompts for seen classes instead of unseen ones. Therefore, we design prompt learning for unseen classes using information from related seen classes, with LLMs utilized to highlight the differences between unseen and related seen classes. Quantitative evaluations on benchmark datasets demonstrate that our EZ-HOI achieves state-of-the-art performance across various zero-shot settings with only 10.35% to 33.95% of the trainable parameters compared to existing methods. Code is available at https://github.com/ChelsieLei/EZ-HOI.

</details>

### Homology Consistency Constrained Efficient Tuning for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/a9338cd6e092ff1f96c3749b08cdc537-Abstract-Conference.html) · 📚 被引 0
- **作者**: Huatian Zhang, Lei Zhang, Yongdong Zhang, Zhendong Mao
- **🏷️ 机构**: PolyU / OPPO
- **会议**: NeurIPS 2024

### Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models.
- **链接**: [arXiv:2410.21802](https://arxiv.org/abs/2410.21802) · [代码](https://github.com/zhyblue424/TGA-ZSR) · 📚 被引 2
- **作者**: Lu Yu, Haiyang Zhang, Changsheng Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the impressive zero-shot capabilities, pre-trained vision-language models (e.g. CLIP), have attracted widespread attention and adoption across various domains. Nonetheless, CLIP has been observed to be susceptible to adversarial examples. Through experimental analysis, we have observed a phenomenon wherein adversarial perturbations induce shifts in text-guided attention. Building upon this observation, we propose a simple yet effective strategy: Text-Guided Attention for Zero-Shot Robustness (TGA-ZSR). This framework incorporates two components: the Attention Refinement module and the Attention-based Model Constraint module. Our goal is to maintain the generalization of the CLIP model and enhance its adversarial robustness: The Attention Refinement module aligns the text-guided attention obtained from the target model via adversarial examples with the text-guided attention acquired from the original model via clean examples. This alignment enhances the model's robustness. Additionally, the Attention-based Model Constraint module acquires text-guided attention from both the target and original models using clean examples. Its objective is to maintain model performance on clean samples while enhancing overall robustness. The experiments validate that our method yields a 9.58% enhancement in zero-shot robust accuracy over the current state-of-the-art techniques across 16 datasets. Our code is available at https://github.com/zhyblue424/TGA-ZSR.

</details>

### Matryoshka Query Transformer for Large Vision-Language Models.
- **链接**: [arXiv:2405.19315](https://arxiv.org/abs/2405.19315) · 📚 被引 5
- **作者**: Wenbo Hu, Zi-Yi Dou, Liunian Harold Li, Amita Kamath, Nanyun Peng, Kai-Wei Chang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) typically encode an image into a fixed number of visual tokens (e.g., 576) and process these tokens with a language model. Despite their strong performance, LVLMs face challenges in adapting to varying computational constraints. This raises the question: can we achieve flexibility in the number of visual tokens to suit different tasks and computational resources? We answer this with an emphatic yes. Inspired by Matryoshka Representation Learning, we introduce the Matryoshka Query Transformer (MQT), capable of encoding an image into m visual tokens during inference, where m can be any number up to a predefined maximum. This is achieved by employing a query transformer with M latent query tokens to compress the visual embeddings. During each training step, we randomly select m <= M latent query tokens and train the model using only these first m tokens, discarding the rest. Combining MQT with LLaVA, we train a single model once, and flexibly and drastically reduce the number of inference-time visual tokens while maintaining similar or better performance compared to training independent models for each number of tokens. Our model, MQT-LLAVA, matches LLaVA-1.5 performance across 11 benchmarks using a maximum of 256 tokens instead of LLaVA's fixed 576. Reducing to 16 tokens (8x less TFLOPs) only sacrifices the performance by 2.4 points on MMBench. On certain tasks such as ScienceQA and MMMU, we can even go down to only 2 visual tokens with performance drops of just 3% and 6% each. Our exploration of the trade-off between the accuracy and computational cost brought about by the number of visual tokens facilitates future research to achieve the best of both worlds.

</details>

### Dual Prototype Evolving for Test-Time Generalization of Vision-Language Models.
- **链接**: [arXiv:2410.12790](https://arxiv.org/abs/2410.12790) · [代码](https://github.com/zhangce01/DPE-CLIP) · 📚 被引 6
- **作者**: Ce Zhang, Simon Stepputtis, Katia P. Sycara, Yaqi Xie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation, which enables models to generalize to diverse data with unlabeled test samples, holds significant value in real-world scenarios. Recently, researchers have applied this setting to advanced pre-trained vision-language models (VLMs), developing approaches such as test-time prompt tuning to further extend their practical applicability. However, these methods typically focus solely on adapting VLMs from a single modality and fail to accumulate task-specific knowledge as more samples are processed. To address this, we introduce Dual Prototype Evolving (DPE), a novel test-time adaptation approach for VLMs that effectively accumulates task-specific knowledge from multi-modalities. Specifically, we create and evolve two sets of prototypes--textual and visual--to progressively capture more accurate multi-modal representations for target classes during test time. Moreover, to promote consistent multi-modal representations, we introduce and optimize learnable residuals for each test sample to align the prototypes from both modalities. Extensive experimental results on 15 benchmark datasets demonstrate that our proposed DPE consistently outperforms previous state-of-the-art methods while also exhibiting competitive computational efficiency. Code is available at https://github.com/zhangce01/DPE-CLIP.

</details>

### Unveiling the Tapestry of Consistency in Large Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d6f094ba0f5ce1720466342f78031bdb-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yuan Zhang, Fei Xiao, Tao Huang, Chun-Kai Fan, Hongyuan Dong, Jiawen Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem.
- **链接**: [arXiv:2411.00238](https://arxiv.org/abs/2411.00238) · 📚 被引 16
- **作者**: Declan Campbell, Sunayana Rane, Tyler Giallanza, Nicolò De Sabbata, Kia Ghods, Amogh Joshi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work has documented striking heterogeneity in the performance of state-of-the-art vision language models (VLMs), including both multimodal language models and text-to-image models. These models are able to describe and generate a diverse array of complex, naturalistic images, yet they exhibit surprising failures on basic multi-object reasoning tasks -- such as counting, localization, and simple forms of visual analogy -- that humans perform with near perfect accuracy. To better understand this puzzling pattern of successes and failures, we turn to theoretical accounts of the binding problem in cognitive science and neuroscience, a fundamental problem that arises when a shared set of representational resources must be used to represent distinct entities (e.g., to represent multiple objects in an image), necessitating the use of serial processing to avoid interference. We find that many of the puzzling failures of state-of-the-art VLMs can be explained as arising due to the binding problem, and that these failure modes are strikingly similar to the limitations exhibited by rapid, feedforward processing in the human brain.

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

- WikiDO: A New Benchmark Evaluating Cross-Modal Retrieval for Vision-Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MLLM-CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Revisiting Few-Shot Object Detection with Vision-Language Models. → [object-detection](../object-detection/Guideline%202024.md)
- ChatTracker: Enhancing Visual Tracking Performance via Chatting with Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202024.md)
- VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks. → [multimodal](../multimodal/Guideline%202024.md)
- CLAP4CLIP: Continual Learning with Probabilistic Finetuning for Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- Advancing Cross-domain Discriminability in Continual Learning of Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202024.md)
- MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts. → [multimodal](../multimodal/Guideline%202024.md)
- MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight. → [multimodal](../multimodal/Guideline%202024.md)
- MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202024.md)
- Single Image Unlearning: Efficient Machine Unlearning in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Visual Anchors Are Strong Information Aggregators For Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202024.md)
- Grounding Multimodal Large Language Models in Actions. → [multimodal](../multimodal/Guideline%202024.md)
- Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- CLIPLoss and Norm-Based Data Selection Methods for Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing. → [multimodal](../multimodal/Guideline%202024.md)
- CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- ControlMLLM: Training-Free Visual Prompt Learning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Multimodal Large Language Models Make Text-to-Image Generative Models Align Better. → [multimodal](../multimodal/Guideline%202024.md)
- Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- T2Vs Meet VLMs: A Scalable Multimodal Dataset for Visual Harmfulness Recognition. → [multimodal](../multimodal/Guideline%202024.md)
- DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution. → [multimodal](../multimodal/Guideline%202024.md)
- Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Wings: Learning Multimodal LLMs without Text-only Forgetting. → [multimodal](../multimodal/Guideline%202024.md)
