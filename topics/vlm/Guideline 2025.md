# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 120 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method.
- **链接**: [arXiv:2412.09082](https://arxiv.org/abs/2412.09082) · 📚 被引 15
- **作者**: Xinshuai Song, Weixing Chen, Yang Liu, Weikai Chen, Guanbin Li, Liang Lin
- **🏷️ 机构**: Sun Yat-sen University,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing Vision-Language Navigation (VLN) methods primarily focus on single-stage navigation, limiting their effectiveness in multi-stage and long-horizon tasks within complex and dynamic environments. To address these limitations, we propose a novel VLN task, named Long-Horizon Vision-Language Navigation (LH-VLN), which emphasizes long-term planning and decision consistency across consecutive subtasks. Furthermore, to support LH-VLN, we develop an automated data generation platform NavGen, which constructs datasets with complex task structures and improves data utility through a bidirectional, multi-granularity generation approach. To accurately evaluate complex tasks, we construct the Long-Horizon Planning and Reasoning in VLN (LHPR-VLN) benchmark consisting of 3,260 tasks with an average of 150 task steps, serving as the first dataset specifically designed for the long-horizon vision-language navigation task. Furthermore, we propose Independent Success Rate (ISR), Conditional Success Rate (CSR), and CSR weight by Ground Truth (CGT) metrics, to provide fine-grained assessments of task completion. To improve model adaptability in complex tasks, we propose a novel Multi-Granularity Dynamic Memory (MGDM) module that integrates short-term memory blurring with long-term memory retrieval to enable flexible navigation in dynamic environments. Our platform, benchmark and method supply LH-VLN with a robust data generation pipeline, comprehensive model evaluation dataset, reasonable metrics, and a novel VLN model, establishing a foundational framework for advancing LH-VLN.

</details>

### Forensics-Bench: A Comprehensive Forgery Detection Benchmark Suite for Large Vision Language Models.
- **链接**: [arXiv:2503.15024](https://arxiv.org/abs/2503.15024) · 📚 被引 3
- **作者**: Jin Wang, Chenghui Lv, Xian Li, Shichao Dong, Huadong Li, Kelu Yao et al.
- **🏷️ 机构**: The University of Hong Kong, Hangzhou Institute for Advanced Study, Zhejiang University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the rapid development of AIGC has significantly boosted the diversities of fake media spread in the Internet, posing unprecedented threats to social security, politics, law, and etc. To detect the ever-increasingly diverse malicious fake media in the new era of AIGC, recent studies have proposed to exploit Large Vision Language Models (LVLMs) to design robust forgery detectors due to their impressive performance on a wide range of multimodal tasks. However, it still lacks a comprehensive benchmark designed to comprehensively assess LVLMs' discerning capabilities on forgery media. To fill this gap, we present Forensics-Bench, a new forgery detection evaluation benchmark suite to assess LVLMs across massive forgery detection tasks, requiring comprehensive recognition, location and reasoning capabilities on diverse forgeries. Forensics-Bench comprises 63,292 meticulously curated multi-choice visual questions, covering 112 unique forgery detection types from 5 perspectives: forgery semantics, forgery modalities, forgery tasks, forgery types and forgery models. We conduct thorough evaluations on 22 open-sourced LVLMs and 3 proprietary models GPT-4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet, highlighting the significant challenges of comprehensive forgery detection posed by Forensics-Bench. We anticipate that Forensics-Bench will motivate the community to advance the frontier of LVLMs, striving for all-around forgery detectors in the era of AIGC. The deliverables will be updated at https://Forensics-Bench.github.io/.

</details>

### Generalized Few-shot 3D Point Cloud Segmentation with Vision-Language Model.
- **链接**: [arXiv:2503.16282](https://arxiv.org/abs/2503.16282) · [代码](https://github.com/ZhaochongAn/GFS-VL)
- **作者**: Zhaochong An, Guolei Sun, Yun Liu, Runjia Li, Junlin Han, Ender Konukoglu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalized few-shot 3D point cloud segmentation (GFS-PCS) adapts models to new classes with few support samples while retaining base class segmentation. Existing GFS-PCS methods enhance prototypes via interacting with support or query features but remain limited by sparse knowledge from few-shot samples. Meanwhile, 3D vision-language models (3D VLMs), generalizing across open-world novel classes, contain rich but noisy novel class knowledge. In this work, we introduce a GFS-PCS framework that synergizes dense but noisy pseudo-labels from 3D VLMs with precise yet sparse few-shot samples to maximize the strengths of both, named GFS-VL. Specifically, we present a prototype-guided pseudo-label selection to filter low-quality regions, followed by an adaptive infilling strategy that combines knowledge from pseudo-label contexts and few-shot samples to adaptively label the filtered, unlabeled areas. Additionally, we design a novel-base mix strategy to embed few-shot samples into training scenes, preserving essential context for improved novel class learning. Moreover, recognizing the limited diversity in current GFS-PCS benchmarks, we introduce two challenging benchmarks with diverse novel classes for comprehensive generalization evaluation. Experiments validate the effectiveness of our framework across models and datasets. Our approach and benchmarks provide a solid foundation for advancing GFS-PCS in the real world. The code is at https://github.com/ZhaochongAn/GFS-VL

</details>

### ProxyTransformation: Preshaping Point Cloud Manifold With Proxy Attention For 3D Visual Grounding.
- **链接**: [arXiv:2502.19247](https://arxiv.org/abs/2502.19247) · 📚 被引 0
- **作者**: Qihang Peng, Henry Zheng, Gao Huang
- **🏷️ 机构**: Tsinghua University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Embodied intelligence requires agents to interact with 3D environments in real time based on language instructions. A foundational task in this domain is ego-centric 3D visual grounding. However, the point clouds rendered from RGB-D images retain a large amount of redundant background data and inherent noise, both of which can interfere with the manifold structure of the target regions. Existing point cloud enhancement methods often require a tedious process to improve the manifold, which is not suitable for real-time tasks. We propose Proxy Transformation suitable for multimodal task to efficiently improve the point cloud manifold. Our method first leverages Deformable Point Clustering to identify the point cloud sub-manifolds in target regions. Then, we propose a Proxy Attention module that utilizes multimodal proxies to guide point cloud transformation. Built upon Proxy Attention, we design a submanifold transformation generation module where textual information globally guides translation vectors for different submanifolds, optimizing relative spatial relationships of target regions. Simultaneously, image information guides linear transformations within each submanifold, refining the local point cloud manifold of target regions. Extensive experiments demonstrate that Proxy Transformation significantly outperforms all existing methods, achieving an impressive improvement of 7.49% on easy targets and 4.60% on hard targets, while reducing the computational overhead of attention blocks by 40.6%. These results establish a new SOTA in ego-centric 3D visual grounding, showcasing the effectiveness and robustness of our approach.

</details>

### AA-CLIP: Enhancing Zero-Shot Anomaly Detection via Anomaly-Aware CLIP.
- **链接**: [arXiv:2503.06661](https://arxiv.org/abs/2503.06661) · [代码](https://github.com/Mwxinnn/AA-CLIP) · 📚 被引 63
- **作者**: Wenxin Ma, Xu Zhang, Qingsong Yao, Fenghe Tang, Chenxu Wu, Yingtai Li et al.
- **🏷️ 机构**: USTC,School of Biomedical Engineering, Division of Life Sciences and Medicine, Stanford University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Anomaly detection (AD) identifies outliers for applications like defect and lesion detection. While CLIP shows promise for zero-shot AD tasks due to its strong generalization capabilities, its inherent Anomaly-Unawareness leads to limited discrimination between normal and abnormal features. To address this problem, we propose Anomaly-Aware CLIP (AA-CLIP), which enhances CLIP's anomaly discrimination ability in both text and visual spaces while preserving its generalization capability. AA-CLIP is achieved through a straightforward yet effective two-stage approach: it first creates anomaly-aware text anchors to differentiate normal and abnormal semantics clearly, then aligns patch-level visual features with these anchors for precise anomaly localization. This two-stage strategy, with the help of residual adapters, gradually adapts CLIP in a controlled manner, achieving effective AD while maintaining CLIP's class knowledge. Extensive experiments validate AA-CLIP as a resource-efficient solution for zero-shot AD tasks, achieving state-of-the-art results in industrial and medical applications. The code is available at https://github.com/Mwxinnn/AA-CLIP.

</details>

### HoVLE: Unleashing the Power of Monolithic Vision-Language Models with Holistic Vision-Language Embedding.
- **链接**: [arXiv:2412.16158](https://arxiv.org/abs/2412.16158) · 📚 被引 2
- **作者**: Chenxin Tao, Shiqian Su, Xizhou Zhu, Chenyu Zhang, Zhe Chen, Jiawen Liu et al.
- **🏷️ 机构**: Tsinghua University, Nanjing University, Johns Hopkins University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advance of Large Language Models (LLMs) has catalyzed the development of Vision-Language Models (VLMs). Monolithic VLMs, which avoid modality-specific encoders, offer a promising alternative to the compositional ones but face the challenge of inferior performance. Most existing monolithic VLMs require tuning pre-trained LLMs to acquire vision abilities, which may degrade their language capabilities. To address this dilemma, this paper presents a novel high-performance monolithic VLM named HoVLE. We note that LLMs have been shown capable of interpreting images, when image embeddings are aligned with text embeddings. The challenge for current monolithic VLMs actually lies in the lack of a holistic embedding module for both vision and language inputs. Therefore, HoVLE introduces a holistic embedding module that converts visual and textual inputs into a shared space, allowing LLMs to process images in the same way as texts. Furthermore, a multi-stage training strategy is carefully designed to empower the holistic embedding module. It is first trained to distill visual features from a pre-trained vision encoder and text embeddings from the LLM, enabling large-scale training with unpaired random images and text tokens. The whole model further undergoes next-token prediction on multi-modal data to align the embeddings. Finally, an instruction-tuning stage is incorporated. Our experiments show that HoVLE achieves performance close to leading compositional models on various benchmarks, outperforming previous monolithic models by a large margin. Model available at https://huggingface.co/OpenGVLab/HoVLE.

</details>

### Florence-VL: Enhancing Vision-Language Models with Generative Vision Encoder and Depth-Breadth Fusion.
- **链接**: [arXiv:2412.04424](https://arxiv.org/abs/2412.04424) · 📚 被引 9
- **作者**: Jiuhai Chen, Jianwei Yang, Haiping Wu, Dianqi Li, Jianfeng Gao, Tianyi Zhou et al.
- **🏷️ 机构**: University of Maryland, Microsoft Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Florence-VL, a new family of multimodal large language models (MLLMs) with enriched visual representations produced by Florence-2, a generative vision foundation model. Unlike the widely used CLIP-style vision transformer trained by contrastive learning, Florence-2 can capture different levels and aspects of visual features, which are more versatile to be adapted to diverse downstream tasks. We propose a novel feature-fusion architecture and an innovative training recipe that effectively integrates Florence-2's visual features into pretrained LLMs, such as Phi 3.5 and LLama 3. In particular, we propose "depth-breath fusion (DBFusion)" to fuse the visual features extracted from different depths and under multiple prompts. Our model training is composed of end-to-end pretraining of the whole model followed by finetuning of the projection layer and the LLM, on a carefully designed recipe of diverse open-source datasets that include high-quality image captions and instruction-tuning pairs. Our quantitative analysis and visualization of Florence-VL's visual features show its advantages over popular vision encoders on vision-language alignment, where the enriched depth and breath play important roles. Florence-VL achieves significant improvements over existing state-of-the-art MLLMs across various multi-modal and vision-centric benchmarks covering general VQA, perception, hallucination, OCR, Chart, knowledge-intensive understanding, etc. To facilitate future research, our models and the complete training recipe are open-sourced. https://github.com/JiuhaiChen/Florence-VL

</details>

### Words or Vision: Do Vision-Language Models Have Blind Faith in Text?
- **链接**: [arXiv:2503.02199](https://arxiv.org/abs/2503.02199) · 📚 被引 10
- **作者**: Ailin Deng, Tri Cao, Zhirui Chen, Bryan Hooi
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) excel in integrating visual and textual information for vision-centric tasks, but their handling of inconsistencies between modalities is underexplored. We investigate VLMs' modality preferences when faced with visual data and varied textual inputs in vision-centered settings. By introducing textual variations to four vision-centric tasks and evaluating ten Vision-Language Models (VLMs), we discover a \emph{``blind faith in text''} phenomenon: VLMs disproportionately trust textual data over visual data when inconsistencies arise, leading to significant performance drops under corrupted text and raising safety concerns. We analyze factors influencing this text bias, including instruction prompts, language model size, text relevance, token order, and the interplay between visual and textual certainty. While certain factors, such as scaling up the language model size, slightly mitigate text bias, others like token order can exacerbate it due to positional biases inherited from language models. To address this issue, we explore supervised fine-tuning with text augmentation and demonstrate its effectiveness in reducing text bias. Additionally, we provide a theoretical analysis suggesting that the blind faith in text phenomenon may stem from an imbalance of pure text and multi-modal data during training. Our findings highlight the need for balanced training and careful consideration of modality interactions in VLMs to enhance their robustness and reliability in handling multi-modal data inconsistencies.

</details>

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
- **链接**: [arXiv:2412.13303](https://arxiv.org/abs/2412.13303) · 📚 被引 24
- **作者**: Pavan Kumar Anasosalu Vasu, Fartash Faghri, Chun-Liang Li, Cem Koc, Nate True, Albert Antony et al.
- **🏷️ 机构**: Apple
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling the input image resolution is essential for enhancing the performance of Vision Language Models (VLMs), particularly in text-rich image understanding tasks. However, popular visual encoders such as ViTs become inefficient at high resolutions due to the large number of tokens and high encoding latency caused by stacked self-attention layers. At different operational resolutions, the vision encoder of a VLM can be optimized along two axes: reducing encoding latency and minimizing the number of visual tokens passed to the LLM, thereby lowering overall latency. Based on a comprehensive efficiency analysis of the interplay between image resolution, vision latency, token count, and LLM size, we introduce FastVLM, a model that achieves an optimized trade-off between latency, model size and accuracy. FastVLM incorporates FastViTHD, a novel hybrid vision encoder designed to output fewer tokens and significantly reduce encoding time for high-resolution images. Unlike previous methods, FastVLM achieves the optimal balance between visual token count and image resolution solely by scaling the input image, eliminating the need for additional token pruning and simplifying the model design. In the LLaVA-1.5 setup, FastVLM achieves 3.2$\times$ improvement in time-to-first-token (TTFT) while maintaining similar performance on VLM benchmarks compared to prior works. Compared to LLaVa-OneVision at the highest resolution (1152$\times$1152), FastVLM achieves better performance on key benchmarks like SeedBench, MMMU and DocVQA, using the same 0.5B LLM, but with 85$\times$ faster TTFT and a vision encoder that is 3.4$\times$ smaller. Code and models are available at https://github.com/apple/ml-fastvlm.

</details>

### VisionZip: Longer is Better but Not Necessary in Vision Language Models.
- **链接**: [arXiv:2412.04467](https://arxiv.org/abs/2412.04467) · 📚 被引 44
- **作者**: Senqiao Yang, Yukang Chen, Zhuotao Tian, Chengyao Wang, Jingyao Li, Bei Yu et al.
- **🏷️ 机构**: CUHK, HITSZ
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in vision-language models have enhanced performance by increasing the length of visual tokens, making them much longer than text tokens and significantly raising computational costs. However, we observe that the visual tokens generated by popular vision encoders, such as CLIP and SigLIP, contain significant redundancy. To address this, we introduce VisionZip, a simple yet effective method that selects a set of informative tokens for input to the language model, reducing visual token redundancy and improving efficiency while maintaining model performance. The proposed VisionZip can be widely applied to image and video understanding tasks and is well-suited for multi-turn dialogues in real-world scenarios, where previous methods tend to underperform. Experimental results show that VisionZip outperforms the previous state-of-the-art method by at least 5% performance gains across nearly all settings. Moreover, our method significantly enhances model inference speed, improving the prefilling time by 8x and enabling the LLaVA-Next 13B model to infer faster than the LLaVA-Next 7B model while achieving better results. Furthermore, we analyze the causes of this redundancy and encourage the community to focus on extracting better visual features rather than merely increasing token length. Our code is available at https://github.com/dvlab-research/VisionZip .

</details>

### Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation.
- **链接**: [arXiv:2504.03193](https://arxiv.org/abs/2504.03193) · 📚 被引 12
- **作者**: Xin Zhang, Robby T. Tan
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Foundation Models (VFMs) and Vision-Language Models (VLMs) have gained traction in Domain Generalized Semantic Segmentation (DGSS) due to their strong generalization capabilities. However, existing DGSS methods often rely exclusively on either VFMs or VLMs, overlooking their complementary strengths. VFMs (e.g., DINOv2) excel at capturing fine-grained features, while VLMs (e.g., CLIP) provide robust text alignment but struggle with coarse granularity. Despite their complementary strengths, effectively integrating VFMs and VLMs with attention mechanisms is challenging, as the increased patch tokens complicate long-sequence modeling. To address this, we propose MFuser, a novel Mamba-based fusion framework that efficiently combines the strengths of VFMs and VLMs while maintaining linear scalability in sequence length. MFuser consists of two key components: MVFuser, which acts as a co-adapter to jointly fine-tune the two models by capturing both sequential and spatial dynamics; and MTEnhancer, a hybrid attention-Mamba module that refines text embeddings by incorporating image priors. Our approach achieves precise feature locality and strong text alignment without incurring significant computational overhead. Extensive experiments demonstrate that MFuser significantly outperforms state-of-the-art DGSS methods, achieving 68.20 mIoU on synthetic-to-real and 71.87 mIoU on real-to-real benchmarks. The code is available at https://github.com/devinxzhang/MFuser.

</details>

### ICT: Image-Object Cross-Level Trusted Intervention for Mitigating Object Hallucination in Large Vision-Language Models.
- **链接**: [arXiv:2411.15268](https://arxiv.org/abs/2411.15268) · 📚 被引 6
- **作者**: Junzhe Chen, Tianshu Zhang, Shiyu Huang, Yuwei Niu, Linfeng Zhang, Lijie Wen et al.
- **🏷️ 机构**: Tsinghua University, Zhipu AI, Chongqing University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the recent breakthroughs achieved by Large Vision Language Models (LVLMs) in understanding and responding to complex visual-textual contexts, their inherent hallucination tendencies limit their practical application in real-world scenarios that demand high levels of precision. Existing methods typically either fine-tune the LVLMs using additional data, which incurs extra costs in manual annotation and computational resources or perform comparisons at the decoding stage, which may eliminate useful language priors for reasoning while introducing inference time overhead. Therefore, we propose ICT, a lightweight, training-free method that calculates an intervention direction to shift the model's focus towards different levels of visual information, enhancing its attention to high-level and fine-grained visual details. During the forward pass stage, the intervention is applied to the attention heads that encode the overall image information and the fine-grained object details, effectively mitigating the phenomenon of overly language priors, and thereby alleviating hallucinations. Extensive experiments demonstrate that ICT achieves strong performance with a small amount of data and generalizes well across different datasets and models. Our code will be public.

</details>

### Skip Tuning: Pre-trained Vision-Language Models are Effective and Efficient Adapters Themselves.
- **链接**: [arXiv:2412.11509](https://arxiv.org/abs/2412.11509) · 📚 被引 6
- **作者**: Shihan Wu, Ji Zhang, Pengpeng Zeng, Lianli Gao, Jingkuan Song, Heng Tao Shen
- **🏷️ 机构**: University of Electronic Science and Technology of China (UESTC), Southwest Jiaotong University, UESTC,Shenzhen Institute for Advanced Study
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt tuning (PT) has long been recognized as an effective and efficient paradigm for transferring large pre-trained vision-language models (VLMs) to downstream tasks by learning a tiny set of context vectors. Nevertheless, in this work, we reveal that freezing the parameters of VLMs during learning the context vectors neither facilitates the transferability of pre-trained knowledge nor improves the memory and time efficiency significantly. Upon further investigation, we find that reducing both the length and width of the feature-gradient propagation flows of the full fine-tuning (FT) baseline is key to achieving effective and efficient knowledge transfer. Motivated by this, we propose Skip Tuning, a novel paradigm for adapting VLMs to downstream tasks. Unlike existing PT or adapter-based methods, Skip Tuning applies Layer-wise Skipping (LSkip) and Class-wise Skipping (CSkip) upon the FT baseline without introducing extra context vectors or adapter modules. Extensive experiments across a wide spectrum of benchmarks demonstrate the superior effectiveness and efficiency of our Skip Tuning over both PT and adapter-based methods. Code: https://github.com/Koorye/SkipTuning.

</details>

### Reproducible Vision-Language Models Meet Concepts Out of Pre-Training.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Reproducible_Vision-Language_Models_Meet_Concepts_Out_of_Pre-Training_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Ziliang Chen, Xin Huang, Xiaoxuan Fan, Keze Wang, Yuyu Zhou, Quanlong Guan et al.
- **🏷️ 机构**: Research Institute of Multiple Agents and Embodied Intelligence,Peng Cheng Laboratory, Sun Yat-sen University, Jinan University
- **会议**: CVPR 2025

### Nullu: Mitigating Object Hallucinations in Large Vision-Language Models via HalluSpace Projection.
- **链接**: [arXiv:2412.13817](https://arxiv.org/abs/2412.13817) · 📚 被引 10
- **作者**: Le Yang, Ziwei Zheng, Boxu Chen, Zhengyu Zhao, Chenhao Lin, Chao Shen
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,Xi&#x2019;an,China,710049
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have shown that large vision-language models (LVLMs) often suffer from the issue of object hallucinations (OH). To mitigate this issue, we introduce an efficient method that edits the model weights based on an unsafe subspace, which we call HalluSpace in this paper. With truthful and hallucinated text prompts accompanying the visual content as inputs, the HalluSpace can be identified by extracting the hallucinated embedding features and removing the truthful representations in LVLMs. By orthogonalizing the model weights, input features will be projected into the Null space of the HalluSpace to reduce OH, based on which we name our method Nullu. We reveal that HalluSpaces generally contain prior information in the large language models (LLMs) applied to build LVLMs, which have been shown as essential causes of OH in previous studies. Therefore, null space projection suppresses the LLMs' priors to filter out the hallucinated features, resulting in contextually accurate outputs. Experiments show that our method can effectively mitigate OH across different LVLM families without extra inference costs and also show strong performance in general LVLM benchmarks. Code is released at https://github.com/Ziwei-Zheng/Nullu.

</details>

### Evaluating Vision-Language Models as Evaluators in Path Planning.
- **链接**: [arXiv:2411.18711](https://arxiv.org/abs/2411.18711) · 📚 被引 1
- **作者**: Mohamed Aghzal, Xiang Yue, Erion Plaku, Ziyu Yao
- **🏷️ 机构**: George Mason University, Carnegie Mellon University, National Science Foundation
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite their promise to perform complex reasoning, large language models (LLMs) have been shown to have limited effectiveness in end-to-end planning. This has inspired an intriguing question: if these models cannot plan well, can they still contribute to the planning framework as a helpful plan evaluator? In this work, we generalize this question to consider LLMs augmented with visual understanding, i.e., Vision-Language Models (VLMs). We introduce PathEval, a novel benchmark evaluating VLMs as plan evaluators in complex path-planning scenarios. Succeeding in the benchmark requires a VLM to be able to abstract traits of optimal paths from the scenario description, demonstrate precise low-level perception on each path, and integrate this information to decide the better path. Our analysis of state-of-the-art VLMs reveals that these models face significant challenges on the benchmark. We observe that the VLMs can precisely abstract given scenarios to identify the desired traits and exhibit mixed performance in integrating the provided information. Yet, their vision component presents a critical bottleneck, with models struggling to perceive low-level details about a path. Our experimental results show that this issue cannot be trivially addressed via end-to-end fine-tuning; rather, task-specific discriminative adaptation of these vision encoders is needed for these VLMs to become effective path evaluators.

</details>

### Vision-Language Models Do Not Understand Negation.
- **链接**: [arXiv:2501.09425](https://arxiv.org/abs/2501.09425) · 📚 被引 18
- **作者**: Kumail Alhamoud, Shaden Alshammari, Yonglong Tian, Guohao Li, Philip H. S. Torr, Yoon Kim et al.
- **🏷️ 机构**: MIT, OpenAI, University of Oxford
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many practical vision-language applications require models that understand negation, e.g., when using natural language to retrieve images which contain certain objects but not others. Despite advancements in vision-language models (VLMs) through large-scale training, their ability to comprehend negation remains underexplored. This study addresses the question: how well do current VLMs understand negation? We introduce NegBench, a new benchmark designed to evaluate negation understanding across 18 task variations and $79$k examples spanning image, video, and medical datasets. The benchmark consists of two core tasks designed to evaluate negation understanding in diverse multimodal settings: Retrieval with Negation and Multiple Choice Questions with Negated Captions. Our evaluation reveals that modern VLMs struggle significantly with negation, often performing at chance level. To address these shortcomings, we explore a data-centric approach wherein we finetune CLIP models on large-scale synthetic datasets containing millions of negated captions. We show that this approach can result in a 10% increase in recall on negated queries and a 28% boost in accuracy on multiple-choice questions with negated captions.

</details>

### Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/An_Mitigating_Object_Hallucinations_in_Large_Vision-Language_Models_with_Assembly_of_CVPR_2025_paper.html) · 📚 被引 15
- **作者**: Wenbin An, Feng Tian, Sicong Leng, Jiahao Nie, Haonan Lin, Qianying Wang et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, Nanyang Technological University, Lenovo Research
- **会议**: CVPR 2025

### ProKeR: A Kernel Perspective on Few-Shot Adaptation of Large Vision-Language Models.
- **链接**: [arXiv:2501.11175](https://arxiv.org/abs/2501.11175) · 📚 被引 10
- **作者**: Yassir Bendou, Amine Ouasfi, Vincent Gripon, Adnane Boukhayma
- **🏷️ 机构**: IMT Atlantique,Brest,France, Inria, University Rennes, IRISA, CNRS
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The growing popularity of Contrastive Language-Image Pretraining (CLIP) has led to its widespread application in various visual downstream tasks. To enhance CLIP's effectiveness and versatility, efficient few-shot adaptation techniques have been widely adopted. Among these approaches, training-free methods, particularly caching methods exemplified by Tip-Adapter, have gained attention for their lightweight adaptation without the need for additional fine-tuning. In this paper, we revisit Tip-Adapter from a kernel perspective, showing that caching methods function as local adapters and are connected to a well-established kernel literature. Drawing on this insight, we offer a theoretical understanding of how these methods operate and suggest multiple avenues for enhancing the Tip-Adapter baseline. Notably, our analysis shows the importance of incorporating global information in local adapters. Therefore, we subsequently propose a global method that learns a proximal regularizer in a reproducing kernel Hilbert space (RKHS) using CLIP as a base learner. Our method, which we call ProKeR (Proximal Kernel ridge Regression), has a closed form solution and achieves state-of-the-art performances across 11 datasets in the standard few-shot adaptation benchmark.

</details>

### Not Only Text: Exploring Compositionality of Visual Representations in Vision-Language Models.
- **链接**: [arXiv:2503.17142](https://arxiv.org/abs/2503.17142) · 📚 被引 1
- **作者**: Davide Berasi, Matteo Farina, Massimiliano Mancini, Elisa Ricci, Nicola Strisciuglio
- **🏷️ 机构**: Fondazione Bruno Kessler, University of Trento, University of Twente
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) learn a shared feature space for text and images, enabling the comparison of inputs of different modalities. While prior works demonstrated that VLMs organize natural language representations into regular structures encoding composite meanings, it remains unclear if compositional patterns also emerge in the visual embedding space. In this work, we investigate compositionality in the image domain, where the analysis of compositional properties is challenged by noise and sparsity of visual data. We address these problems and propose a framework, called Geodesically Decomposable Embeddings (GDE), that approximates image representations with geometry-aware compositional structures in the latent space. We demonstrate that visual embeddings of pre-trained VLMs exhibit a compositional arrangement, and evaluate the effectiveness of this property in the tasks of compositional classification and group robustness. GDE achieves stronger performance in compositional classification compared to its counterpart method that assumes linear geometry of the latent space. Notably, it is particularly effective for group robustness, where we achieve higher results than task-specific solutions. Our results indicate that VLMs can automatically develop a human-like form of compositional reasoning in the visual domain, making their underlying processes more interpretable. Code is available at https://github.com/BerasiDavide/vlm_image_compositionality.

</details>

### SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments.
- **链接**: [arXiv:2412.00114](https://arxiv.org/abs/2412.00114) · 📚 被引 4
- **作者**: Yue Cao, Yun Xing, Jie Zhang, Di Lin, Tianwei Zhang, Ivor W. Tsang et al.
- **🏷️ 机构**: Agency for Science, Technology and Research (A*STAR),CFAR and IHPC,Singapore, Tianjin University,China, Nanyang Technological University,College of Computing and Data Science,Singapore
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (LVLMs) have shown remarkable capabilities in interpreting visual content. While existing works demonstrate these models' vulnerability to deliberately placed adversarial texts, such texts are often easily identifiable as anomalous. In this paper, we present the first approach to generate scene-coherent typographic adversarial attacks that mislead advanced LVLMs while maintaining visual naturalness through the capability of the LLM-based agent. Our approach addresses three critical questions: what adversarial text to generate, where to place it within the scene, and how to integrate it seamlessly. We propose a training-free, multi-modal LLM-driven scene-coherent typographic adversarial planning (SceneTAP) that employs a three-stage process: scene understanding, adversarial planning, and seamless integration. The SceneTAP utilizes chain-of-thought reasoning to comprehend the scene, formulate effective adversarial text, strategically plan its placement, and provide detailed instructions for natural integration within the image. This is followed by a scene-coherent TextDiffuser that executes the attack using a local diffusion mechanism. We extend our method to real-world scenarios by printing and placing generated patches in physical environments, demonstrating its practical implications. Extensive experiments show that our scene-coherent adversarial text successfully misleads state-of-the-art LVLMs, including ChatGPT-4o, even after capturing new images of physical setups. Our evaluations demonstrate a significant increase in attack success rates while maintaining visual naturalness and contextual appropriateness. This work highlights vulnerabilities in current vision-language models to sophisticated, scene-coherent adversarial attacks and provides insights into potential defense mechanisms.

</details>

### Lifelong Knowledge Editing for Vision Language Models with Low-Rank Mixture-of-Experts.
- **链接**: [arXiv:2411.15432](https://arxiv.org/abs/2411.15432) · 📚 被引 3
- **作者**: Qizhou Chen, Chengyu Wang, Dakan Wang, Taolin Zhang, Wangyue Li, Xiaofeng He
- **🏷️ 机构**: East China Normal University,Shanghai,China, Alibaba Cloud Computing,Hangzhou,China, Exacity Inc.,Shanghai,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model editing aims to correct inaccurate knowledge, update outdated information, and incorporate new data into Large Language Models (LLMs) without the need for retraining. This task poses challenges in lifelong scenarios where edits must be continuously applied for real-world applications. While some editors demonstrate strong robustness for lifelong editing in pure LLMs, Vision LLMs (VLLMs), which incorporate an additional vision modality, are not directly adaptable to existing LLM editors. In this paper, we propose LiveEdit, a LIfelong Vision language modEl Edit to bridge the gap between lifelong LLM editing and VLLMs. We begin by training an editing expert generator to independently produce low-rank experts for each editing instance, with the goal of correcting the relevant responses of the VLLM. A hard filtering mechanism is developed to utilize visual semantic knowledge, thereby coarsely eliminating visually irrelevant experts for input queries during the inference stage of the post-edited model. Finally, to integrate visually relevant experts, we introduce a soft routing mechanism based on textual semantic relevance to achieve multi-expert fusion. For evaluation, we establish a benchmark for lifelong VLLM editing. Extensive experiments demonstrate that LiveEdit offers significant advantages in lifelong VLLM editing scenarios. Further experiments validate the rationality and effectiveness of each module design in LiveEdit.

</details>

### SlideChat: A Large Vision-Language Assistant for Whole-Slide Pathology Image Understanding.
- **链接**: [arXiv:2410.11761](https://arxiv.org/abs/2410.11761) · 📚 被引 17
- **作者**: Ying Chen, Guoan Wang, Yuanfeng Ji, Yanjun Li, Jin Ye, Tianbin Li et al.
- **🏷️ 机构**: Shanghai AI Laboratory, Stanford University, Xiamen University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the progress made by multimodal large language models (MLLMs) in computational pathology, they remain limited by a predominant focus on patch-level analysis, missing essential contextual information at the whole-slide level. The lack of large-scale instruction datasets and the gigapixel scale of whole slide images (WSIs) pose significant developmental challenges. In this paper, we present SlideChat, the first vision-language assistant capable of understanding gigapixel whole-slide images, exhibiting excellent multimodal conversational capability and response complex instruction across diverse pathology scenarios. To support its development, we created SlideInstruction, the largest instruction-following dataset for WSIs consisting of 4.2K WSI captions and 176K VQA pairs with multiple categories. Furthermore, we propose SlideBench, a multimodal benchmark that incorporates captioning and VQA tasks to assess SlideChat's capabilities in varied clinical settings such as microscopy, diagnosis. Compared to both general and specialized MLLMs, SlideChat exhibits exceptional capabilities achieving state-of-the-art performance on 18 of 22 tasks. For example, it achieved an overall accuracy of 81.17% on SlideBench-VQA (TCGA), and 54.15% on SlideBench-VQA (BCNB). Our code, data, and model is publicly accessible at https://uni-medical.github.io/SlideChat.github.io.

</details>

### Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Deitke_Molmo_and_PixMo_Open_Weights_and_Open_Data_for_State-of-the-Art_CVPR_2025_paper.html) · 📚 被引 46
- **作者**: Matt Deitke, Christopher Clark, Sangho Lee, Rohun Tripathi, Yue Yang, Jae Sung Park et al.
- **🏷️ 机构**: Allen Institute for AI, University of Washington
- **会议**: CVPR 2025

### Rethinking Few-Shot Adaptation of Vision-Language Models in Two Stages.
- **链接**: [arXiv:2503.11609](https://arxiv.org/abs/2503.11609) · 📚 被引 7
- **作者**: Matteo Farina, Massimiliano Mancini, Giovanni Iacca, Elisa Ricci
- **🏷️ 机构**: University of Trento
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An old-school recipe for training a classifier is to (i) learn a good feature extractor and (ii) optimize a linear layer atop. When only a handful of samples are available per category, as in Few-Shot Adaptation (FSA), data are insufficient to fit a large number of parameters, rendering the above impractical. This is especially true with large pre-trained Vision-Language Models (VLMs), which motivated successful research at the intersection of Parameter-Efficient Fine-tuning (PEFT) and FSA. In this work, we start by analyzing the learning dynamics of PEFT techniques when trained on few-shot data from only a subset of categories, referred to as the ``base'' classes. We show that such dynamics naturally splits into two distinct phases: (i) task-level feature extraction and (ii) specialization to the available concepts. To accommodate this dynamic, we then depart from prompt- or adapter-based methods and tackle FSA differently. Specifically, given a fixed computational budget, we split it to (i) learn a task-specific feature extractor via PEFT and (ii) train a linear classifier on top. We call this scheme Two-Stage Few-Shot Adaptation (2SFS). Differently from established methods, our scheme enables a novel form of selective inference at a category level, i.e., at test time, only novel categories are embedded by the adapted text encoder, while embeddings of base categories are available within the classifier. Results with fixed hyperparameters across two settings, three backbones, and eleven datasets, show that 2SFS matches or surpasses the state-of-the-art, while established methods degrade significantly across settings.

</details>

### ReVisionLLM: Recursive Vision-Language Model for Temporal Grounding in Hour-Long Videos.
- **链接**: [arXiv:2411.14901](https://arxiv.org/abs/2411.14901) · 📚 被引 4
- **作者**: Tanveer Hannan, Md Mohaiminul Islam, Jindong Gu, Thomas Seidl, Gedas Bertasius
- **🏷️ 机构**: LMU Munich, UNC Chapel Hill, University of Oxford
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) excel at retrieving information from lengthy text, but their vision-language counterparts (VLMs) face difficulties with hour-long videos, especially for temporal grounding. Specifically, these VLMs are constrained by frame limitations, often losing essential temporal details needed for accurate event localization in extended video content. We propose ReVisionLLM, a recursive vision-language model designed to locate events in hour-long videos. Inspired by human search strategies, our model initially targets broad segments of interest, progressively revising its focus to pinpoint exact temporal boundaries. Our model can seamlessly handle videos of vastly different lengths, from minutes to hours. We also introduce a hierarchical training strategy that starts with short clips to capture distinct events and progressively extends to longer videos. To our knowledge, ReVisionLLM is the first VLM capable of temporal grounding in hour-long videos, outperforming previous state-of-the-art methods across multiple datasets by a significant margin (+2.6% R1@0.1 on MAD). The code is available at https://github.com/Tanveer81/ReVisionLLM.

</details>

### Exploring Visual Vulnerabilities via Multi-Loss Adversarial Search for Jailbreaking Vision-Language Models.
- **链接**: [arXiv:2411.18000](https://arxiv.org/abs/2411.18000) · 📚 被引 3
- **作者**: Shuyang Hao, Bryan Hooi, Jun Liu, Kai-Wei Chang, Zi Huang, Yujun Cai
- **🏷️ 机构**: Southeast University, National University of Singapore, Lancaster University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite inheriting security measures from underlying language models, Vision-Language Models (VLMs) may still be vulnerable to safety alignment issues. Through empirical analysis, we uncover two critical findings: scenario-matched images can significantly amplify harmful outputs, and contrary to common assumptions in gradient-based attacks, minimal loss values do not guarantee optimal attack effectiveness. Building on these insights, we introduce MLAI (Multi-Loss Adversarial Images), a novel jailbreak framework that leverages scenario-aware image generation for semantic alignment, exploits flat minima theory for robust adversarial image selection, and employs multi-image collaborative attacks for enhanced effectiveness. Extensive experiments demonstrate MLAI's significant impact, achieving attack success rates of 77.75% on MiniGPT-4 and 82.80% on LLaVA-2, substantially outperforming existing methods by margins of 34.37% and 12.77% respectively. Furthermore, MLAI shows considerable transferability to commercial black-box VLMs, achieving up to 60.11% success rate. Our work reveals fundamental visual vulnerabilities in current VLMs safety mechanisms and underscores the need for stronger defenses. Warning: This paper contains potentially harmful example text.

</details>

### Task-Aware Clustering for Prompting Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hao_Task-Aware_Clustering_for_Prompting_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Fusheng Hao, Fengxiang He, Fuxiang Wu, Tichao Wang, Chengqun Song, Jun Cheng
- **🏷️ 机构**: Chinese Academy of Sciences,Shenzhen Institute of Advanced Technology, University of Edinburgh
- **会议**: CVPR 2025

### MotionBench: Benchmarking and Improving Fine-grained Video Motion Understanding for Vision Language Models.
- **链接**: [arXiv:2501.02955](https://arxiv.org/abs/2501.02955) · 📚 被引 9
- **作者**: Wenyi Hong, Yean Cheng, Zhuoyi Yang, Weihan Wang, Lefan Wang, Xiaotao Gu et al.
- **🏷️ 机构**: Tsinghua University, Zhipu AI
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, vision language models (VLMs) have made significant advancements in video understanding. However, a crucial capability - fine-grained motion comprehension - remains under-explored in current benchmarks. To address this gap, we propose MotionBench, a comprehensive evaluation benchmark designed to assess the fine-grained motion comprehension of video understanding models. MotionBench evaluates models' motion-level perception through six primary categories of motion-oriented question types and includes data collected from diverse sources, ensuring a broad representation of real-world video content. Experimental results reveal that existing VLMs perform poorly in understanding fine-grained motions. To enhance VLM's ability to perceive fine-grained motion within a limited sequence length of LLM, we conduct extensive experiments reviewing VLM architectures optimized for video feature compression and propose a novel and efficient Through-Encoder (TE) Fusion method. Experiments show that higher frame rate inputs and TE Fusion yield improvements in motion understanding, yet there is still substantial room for enhancement. Our benchmark aims to guide and motivate the development of more capable video understanding models, emphasizing the importance of fine-grained motion comprehension. Project page: https://motion-bench.github.io .

</details>

### SLADE: Shielding against Dual Exploits in Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Hossain_SLADE_Shielding_against_Dual_Exploits_in_Large_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Md. Zarif Hossain, Ahmed Imteaj
- **🏷️ 机构**: Southern Illinois University,School of Computing,Carbondale,IL,USA,62901
- **会议**: CVPR 2025

### HiRes-LLaVA: Restoring Fragmentation Input in High-Resolution Large Vision-Language Models.
- **链接**: [arXiv:2407.08706](https://arxiv.org/abs/2407.08706) · 📚 被引 5
- **作者**: Runhui Huang, Xinpeng Ding, Chunwei Wang, Jianhua Han, Yulong Liu, Hengshuang Zhao et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, The Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution inputs enable Large Vision-Language Models (LVLMs) to discern finer visual details, enhancing their comprehension capabilities. To reduce the training and computation costs caused by high-resolution input, one promising direction is to use sliding windows to slice the input into uniform patches, each matching the input size of the well-trained vision encoder. Although efficient, this slicing strategy leads to the fragmentation of original input, i.e., the continuity of contextual information and spatial geometry is lost across patches, adversely affecting performance in cross-patch context perception and position-specific tasks. To overcome these shortcomings, we introduce HiRes-LLaVA, a novel framework designed to efficiently process any size of high-resolution input without altering the original contextual and geometric information. HiRes-LLaVA comprises two innovative components: (i) a SliceRestore adapter that reconstructs sliced patches into their original form, efficiently extracting both global and local features via down-up-sampling and convolution layers, and (ii) a Self-Mining Sampler to compresses the vision tokens based on themselves, preserving the original context and positional information while reducing training overhead. To assess the ability of handling context fragmentation, we construct a new benchmark, EntityGrid-QA, consisting of edge-related and position-related tasks. Our comprehensive experiments demonstrate the superiority of HiRes-LLaVA on both existing public benchmarks and on EntityGrid-QA, particularly on document-oriented tasks, establishing new standards for handling high-resolution inputs.

</details>

### VL2Lite: Task-Specific Knowledge Distillation from Large Vision-Language Models to Lightweight Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jang_VL2Lite_Task-Specific_Knowledge_Distillation_from_Large_Vision-Language_Models_to_Lightweight_CVPR_2025_paper.html) · 📚 被引 11
- **作者**: Jinseong Jang, Chunfei Ma, Byeongwon Lee
- **🏷️ 机构**: Vision Lab, AI R&amp;D Center, SK Telecom
- **会议**: CVPR 2025

### Devils in Middle Layers of Large Vision-Language Models: Interpreting, Detecting and Mitigating Object Hallucinations via Attention Lens.
- **链接**: [arXiv:2411.16724](https://arxiv.org/abs/2411.16724) · 📚 被引 15
- **作者**: Zhangqi Jiang, Junkai Chen, Beier Zhu, Tingjin Luo, Yankun Shen, Xu Yang
- **🏷️ 机构**: National University of Defense Technology, Southeast University, Nanyang Technological University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hallucinations in Large Vision-Language Models (LVLMs) significantly undermine their reliability, motivating researchers to explore the causes of hallucination. However, most studies primarily focus on the language aspect rather than the visual. In this paper, we address how LVLMs process visual information and whether this process causes hallucination. Firstly, we use the attention lens to identify the stages at which LVLMs handle visual data, discovering that the middle layers are crucial. Moreover, we find that these layers can be further divided into two stages: ''visual information enrichment'' and ''semantic refinement'' which respectively propagate visual data to object tokens and interpret it through text. By analyzing attention patterns during the visual information enrichment stage, we find that real tokens consistently receive higher attention weights than hallucinated ones, serving as a strong indicator of hallucination. Further examination of multi-head attention maps reveals that hallucination tokens often result from heads interacting with inconsistent objects. Based on these insights, we propose a simple inference-time method that adjusts visual attention by integrating information across various heads. Extensive experiments demonstrate that this approach effectively mitigates hallucinations in mainstream LVLMs without additional training costs. Code is available at https://github.com/ZhangqiJiang07/middle_layers_indicating_hallucinations.

</details>

### Your Large Vision-Language Model Only Needs A Few Attention Heads For Visual Grounding.
- **链接**: [arXiv:2503.06287](https://arxiv.org/abs/2503.06287) · 📚 被引 7
- **作者**: Seil Kang, Jinyeong Kim, Junhyeok Kim, Seong Jae Hwang
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual grounding seeks to localize the image region corresponding to a free-form text description. Recently, the strong multimodal capabilities of Large Vision-Language Models (LVLMs) have driven substantial improvements in visual grounding, though they inevitably require fine-tuning and additional model components to explicitly generate bounding boxes or segmentation masks. However, we discover that a few attention heads in frozen LVLMs demonstrate strong visual grounding capabilities. We refer to these heads, which consistently capture object locations related to text semantics, as localization heads. Using localization heads, we introduce a straightforward and effective training-free visual grounding framework that utilizes text-to-image attention maps from localization heads to identify the target objects. Surprisingly, only three out of thousands of attention heads are sufficient to achieve competitive localization performance compared to existing LVLM-based visual grounding methods that require fine-tuning. Our findings suggest that LVLMs can innately ground objects based on a deep comprehension of the text-image relationship, as they implicitly focus on relevant image regions to generate informative text outputs. All the source codes will be made available to the public.

</details>

### GFlowVLM: Enhancing Multi-step Reasoning in Vision-Language Models with Generative Flow Networks.
- **链接**: [arXiv:2503.06514](https://arxiv.org/abs/2503.06514) · 📚 被引 1
- **作者**: Haoqiang Kang, Enna Sachdeva, Piyush Gupta, Sangjae Bae, Kwonjoon Lee
- **🏷️ 机构**: Honda Research Institute,USA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have recently shown promising advancements in sequential decision-making tasks through task-specific fine-tuning. However, common fine-tuning methods, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) techniques like Proximal Policy Optimization (PPO), present notable limitations: SFT assumes Independent and Identically Distributed (IID) data, while PPO focuses on maximizing cumulative rewards. These limitations often restrict solution diversity and hinder generalization in multi-step reasoning tasks. To address these challenges, we introduce a novel framework, GFlowVLM, a framework that fine-tune VLMs using Generative Flow Networks (GFlowNets) to promote generation of diverse solutions for complex reasoning tasks. GFlowVLM models the environment as a non-Markovian decision process, allowing it to capture long-term dependencies essential for real-world applications. It takes observations and task descriptions as inputs to prompt chain-of-thought (CoT) reasoning which subsequently guides action selection. We use task based rewards to fine-tune VLM with GFlowNets. This approach enables VLMs to outperform prior fine-tuning methods, including SFT and RL. Empirical results demonstrate the effectiveness of GFlowVLM on complex tasks such as card games (NumberLine, BlackJack) and embodied planning tasks (ALFWorld), showing enhanced training efficiency, solution diversity, and stronger generalization capabilities across both in-distribution and out-of-distribution scenarios.

</details>

### BiomedCoOp: Learning to Prompt for Biomedical Vision-Language Models.
- **链接**: [arXiv:2411.15232](https://arxiv.org/abs/2411.15232) · 📚 被引 22
- **作者**: Taha Koleilat, Hojat Asgariandehkordi, Hassan Rivaz, Yiming Xiao
- **🏷️ 机构**: Concordia University,Montreal,Canada
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in vision-language models (VLMs), such as CLIP, have demonstrated substantial success in self-supervised representation learning for vision tasks. However, effectively adapting VLMs to downstream applications remains challenging, as their accuracy often depends on time-intensive and expertise-demanding prompt engineering, while full model fine-tuning is costly. This is particularly true for biomedical images, which, unlike natural images, typically suffer from limited annotated datasets, unintuitive image contrasts, and nuanced visual features. Recent prompt learning techniques, such as Context Optimization (CoOp) intend to tackle these issues, but still fall short in generalizability. Meanwhile, explorations in prompt learning for biomedical image analysis are still highly limited. In this work, we propose BiomedCoOp, a novel prompt learning framework that enables efficient adaptation of BiomedCLIP for accurate and highly generalizable few-shot biomedical image classification. Our approach achieves effective prompt context learning by leveraging semantic consistency with average prompt ensembles from Large Language Models (LLMs) and knowledge distillation with a statistics-based prompt selection strategy. We conducted comprehensive validation of our proposed framework on 11 medical datasets across 9 modalities and 10 organs against existing state-of-the-art methods, demonstrating significant improvements in both accuracy and generalizability. The code is publicly available at https://github.com/HealthX-Lab/BiomedCoOp.

</details>

### VLsI: Verbalized Layers-to-Interactions from Large to Small Vision Language Models.
- **链接**: [arXiv:2412.01822](https://arxiv.org/abs/2412.01822) · 📚 被引 4
- **作者**: Byung-Kwan Lee, Ryo Hachiuma, Yu-Chiang Frank Wang, Yong Man Ro, Yueh-Hua Wu
- **🏷️ 机构**: NVIDIA, KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent surge in high-quality visual instruction tuning samples from closed-source vision-language models (VLMs) such as GPT-4V has accelerated the release of open-source VLMs across various model sizes. However, scaling VLMs to improve performance using larger models brings significant computational challenges, especially for deployment on resource-constrained devices like mobile platforms and robots. To address this, we propose VLsI: Verbalized Layers-to-Interactions, a new VLM family in 2B and 7B model sizes, which prioritizes efficiency without compromising accuracy. VLsI leverages a unique, layer-wise distillation process, introducing intermediate "verbalizers" that map features from each layer to natural language space, allowing smaller VLMs to flexibly align with the reasoning processes of larger VLMs. This approach mitigates the training instability often encountered in output imitation and goes beyond typical final-layer tuning by aligning the small VLMs' layer-wise progression with that of the large ones. We validate VLsI across ten challenging vision-language benchmarks, achieving notable performance gains (11.0% for 2B and 17.4% for 7B) over GPT-4V without the need for model scaling, merging, or architectural changes.

</details>

### Cropper: Vision-Language Model for Image Cropping through In-Context Learning.
- **链接**: [arXiv:2408.07790](https://arxiv.org/abs/2408.07790) · 📚 被引 4
- **作者**: Seung Hyun Lee, Jijun Jiang, Yiran Xu, Zhuofang Li, Junjie Ke, Yinxiao Li et al.
- **🏷️ 机构**: Google Research, Google, Google DeepMind
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of image cropping is to identify visually appealing crops in an image. Conventional methods are trained on specific datasets and fail to adapt to new requirements. Recent breakthroughs in large vision-language models (VLMs) enable visual in-context learning without explicit training. However, downstream tasks with VLMs remain under explored. In this paper, we propose an effective approach to leverage VLMs for image cropping. First, we propose an efficient prompt retrieval mechanism for image cropping to automate the selection of in-context examples. Second, we introduce an iterative refinement strategy to iteratively enhance the predicted crops. The proposed framework, we refer to as Cropper, is applicable to a wide range of cropping tasks, including free-form cropping, subject-aware cropping, and aspect ratio-aware cropping. Extensive experiments demonstrate that Cropper significantly outperforms state-of-the-art methods across several benchmarks.

</details>

### MBQ: Modality-Balanced Quantization for Large Vision-Language Models.
- **链接**: [arXiv:2412.19509](https://arxiv.org/abs/2412.19509) · 📚 被引 8
- **作者**: Shiyao Li, Yingchun Hu, Xuefei Ning, Xihui Liu, Ke Hong, Xiaotao Jia et al.
- **🏷️ 机构**: Tsinghua University, Infinigence-AI, University of Hong Kong
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have enabled a variety of real-world applications. The large parameter size of VLMs brings large memory and computation overhead which poses significant challenges for deployment. Post-Training Quantization (PTQ) is an effective technique to reduce the memory and computation overhead. Existing PTQ methods mainly focus on large language models (LLMs), without considering the differences across other modalities. In this paper, we discover that there is a significant difference in sensitivity between language and vision tokens in large VLMs. Therefore, treating tokens from different modalities equally, as in existing PTQ methods, may over-emphasize the insensitive modalities, leading to significant accuracy loss. To deal with the above issue, we propose a simple yet effective method, Modality-Balanced Quantization (MBQ), for large VLMs. Specifically, MBQ incorporates the different sensitivities across modalities during the calibration process to minimize the reconstruction loss for better quantization parameters. Extensive experiments show that MBQ can significantly improve task accuracy by up to 4.4% and 11.6% under W3 and W4A8 quantization for 7B to 70B VLMs, compared to SOTA baselines. Additionally, we implement a W3 GPU kernel that fuses the dequantization and GEMV operators, achieving a 1.4x speedup on LLaVA-onevision-7B on the RTX 4090. The code is available at https://github.com/thu-nics/MBQ.

</details>

### DPC: Dual-Prompt Collaboration for Tuning Vision-Language Models.
- **链接**: [arXiv:2503.13443](https://arxiv.org/abs/2503.13443) · 📚 被引 13
- **作者**: Haoyang Li, Liang Wang, Chao Wang, Jing Jiang, Yan Peng, Guodong Long
- **🏷️ 机构**: Shanghai University, University of Technology Sydney
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Base-New Trade-off (BNT) problem universally exists during the optimization of CLIP-based prompt tuning, where continuous fine-tuning on base (target) classes leads to a simultaneous decrease of generalization ability on new (unseen) classes. Existing approaches attempt to regulate the prompt tuning process to balance BNT by appending constraints. However, imposed on the same target prompt, these constraints fail to fully avert the mutual exclusivity between the optimization directions for base and new. As a novel solution to this challenge, we propose the plug-and-play Dual-Prompt Collaboration (DPC) framework, the first that decoupling the optimization processes of base and new tasks at the prompt level. Specifically, we clone a learnable parallel prompt based on the backbone prompt, and introduce a variable Weighting-Decoupling framework to independently control the optimization directions of dual prompts specific to base or new tasks, thus avoiding the conflict in generalization. Meanwhile, we propose a Dynamic Hard Negative Optimizer, utilizing dual prompts to construct a more challenging optimization task on base classes for enhancement. For interpretability, we prove the feature channel invariance of the prompt vector during the optimization process, providing theoretical support for the Weighting-Decoupling of DPC. Extensive experiments on multiple backbones demonstrate that DPC can significantly improve base performance without introducing any external knowledge beyond the base classes, while maintaining generalization to new classes. Code is available at: https://github.com/JREion/DPC.

</details>

### Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Revisiting_Backdoor_Attacks_against_Large_Vision-Language_Models_from_Domain_Shift_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Siyuan Liang, Jiawei Liang, Tianyu Pang, Chao Du, Aishan Liu, Mingli Zhu et al.
- **🏷️ 机构**: Nanyang Technological University, Shenzhen Campus of Sun Yat-Sen University, Sea AI Lab,Singapore
- **会议**: CVPR 2025

### Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_Can_Large_Vision-Language_Models_Correct_Semantic_Grounding_Errors_By_Themselves_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Yuan-Hong Liao, Rafid Mahmood, Sanja Fidler, David Acuna
- **🏷️ 机构**: University of Toronto,Vector Institute, NVIDIA
- **会议**: CVPR 2025

### BIOMEDICA: An Open Biomedical Image-Caption Archive, Dataset, and Vision-Language Models Derived from Scientific Literature.
- **链接**: [arXiv:2501.07171](https://arxiv.org/abs/2501.07171) · 📚 被引 14
- **作者**: Alejandro Lozano, Min Woo Sun, James Burgess, Liangyu Chen, Jeffrey J. Nirschl, Jeffrey Gu et al.
- **🏷️ 机构**: Stanford University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The development of vision-language models (VLMs) is driven by large-scale and diverse multimodal datasets. However, progress toward generalist biomedical VLMs is limited by the lack of annotated, publicly accessible datasets across biology and medicine. Existing efforts are restricted to narrow domains, missing the full diversity of biomedical knowledge encoded in scientific literature. To address this gap, we introduce BIOMEDICA, a scalable, open-source framework to extract, annotate, and serialize the entirety of the PubMed Central Open Access subset into an easy-to-use, publicly accessible dataset. Our framework produces a comprehensive archive with over 24 million unique image-text pairs from over 6 million articles. Metadata and expert-guided annotations are also provided. We demonstrate the utility and accessibility of our resource by releasing BMCA-CLIP, a suite of CLIP-style models continuously pre-trained on the BIOMEDICA dataset via streaming, eliminating the need to download 27 TB of data locally. On average, our models achieve state-of-the-art performance across 40 tasks - spanning pathology, radiology, ophthalmology, dermatology, surgery, molecular biology, parasitology, and cell biology - excelling in zero-shot classification with a 6.56% average improvement (as high as 29.8% and 17.5% in dermatology and ophthalmology, respectively), and stronger image-text retrieval, all while using 10x less compute. To foster reproducibility and collaboration, we release our codebase and dataset for the broader research community.

</details>

### Benchmarking Large Vision-Language Models via Directed Scene Graph for Comprehensive Image Captioning.
- **链接**: [arXiv:2412.08614](https://arxiv.org/abs/2412.08614) · 📚 被引 6
- **作者**: Fan Lu, Wei Wu, Kecheng Zheng, Shuailei Ma, Biao Gong, Jiawei Liu et al.
- **🏷️ 机构**: University of Science and Technology of China,MoE Key Laboratory of Brain-Inspired Intelligent Perception and Cognition, Ant Group, Northeastern University,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating detailed captions comprehending text-rich visual content in images has received growing attention for Large Vision-Language Models (LVLMs). However, few studies have developed benchmarks specifically tailored for detailed captions to measure their accuracy and comprehensiveness. In this paper, we introduce a detailed caption benchmark, termed as CompreCap, to evaluate the visual context from a directed scene graph view. Concretely, we first manually segment the image into semantically meaningful regions (i.e., semantic segmentation mask) according to common-object vocabulary, while also distinguishing attributes of objects within all those regions. Then directional relation labels of these objects are annotated to compose a directed scene graph that can well encode rich compositional information of the image. Based on our directed scene graph, we develop a pipeline to assess the generated detailed captions from LVLMs on multiple levels, including the object-level coverage, the accuracy of attribute descriptions, the score of key relationships, etc. Experimental results on the CompreCap dataset confirm that our evaluation method aligns closely with human evaluation scores across LVLMs.

</details>

### SPARC: Score Prompting and Adaptive Fusion for Zero-Shot Multi-Label Recognition in Vision-Language Models.
- **链接**: [arXiv:2502.16911](https://arxiv.org/abs/2502.16911) · 📚 被引 2
- **作者**: Kevin Miller, Aditya Gangrade, Samarth Mishra, Kate Saenko, Venkatesh Saligrama
- **🏷️ 机构**: Boston University, Boston University and Meta AI (FAIR)
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot multi-label recognition (MLR) with Vision-Language Models (VLMs) faces significant challenges without training data, model tuning, or architectural modifications. Existing approaches require prompt tuning or architectural adaptations, limiting zero-shot applicability. Our work proposes a novel solution treating VLMs as black boxes, leveraging scores without training data or ground truth. Using large language model insights on object co-occurrence, we introduce compound prompts grounded in realistic object combinations. Analysis of these prompt scores reveals VLM biases and ``AND''/``OR'' signal ambiguities, notably that maximum compound scores are surprisingly suboptimal compared to second-highest scores. We address these through a debiasing and score-fusion algorithm that corrects image bias and clarifies VLM response behaviors. Our method enhances other zero-shot approaches, consistently improving their results. Experiments show superior mean Average Precision (mAP) compared to methods requiring training data, achieved through refined object ranking for robust zero-shot MLR.

</details>

### VILA-M3: Enhancing Vision-Language Models with Medical Expert Knowledge.
- **链接**: [arXiv:2411.12915](https://arxiv.org/abs/2411.12915) · 📚 被引 27
- **作者**: Vishwesh Nath, Wenqi Li, Dong Yang, Andriy Myronenko, Mingxin Zheng, Yao Lu et al.
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generalist vision language models (VLMs) have made significant strides in computer vision, but they fall short in specialized fields like healthcare, where expert knowledge is essential. In traditional computer vision tasks, creative or approximate answers may be acceptable, but in healthcare, precision is paramount.Current large multimodal models like Gemini and GPT-4o are insufficient for medical tasks due to their reliance on memorized internet knowledge rather than the nuanced expertise required in healthcare. VLMs are usually trained in three stages: vision pre-training, vision-language pre-training, and instruction fine-tuning (IFT). IFT has been typically applied using a mixture of generic and healthcare data. In contrast, we propose that for medical VLMs, a fourth stage of specialized IFT is necessary, which focuses on medical data and includes information from domain expert models. Domain expert models developed for medical use are crucial because they are specifically trained for certain clinical tasks, e.g. to detect tumors and classify abnormalities through segmentation and classification, which learn fine-grained features of medical data$-$features that are often too intricate for a VLM to capture effectively especially in radiology. This paper introduces a new framework, VILA-M3, for medical VLMs that utilizes domain knowledge via expert models. Through our experiments, we show an improved state-of-the-art (SOTA) performance with an average improvement of ~9% over the prior SOTA model Med-Gemini and ~6% over models trained on the specific tasks. Our approach emphasizes the importance of domain expertise in creating precise, reliable VLMs for medical applications.

</details>

### CALICO: Part-Focused Semantic Co-Segmentation with Large Vision-Language Models.
- **链接**: [arXiv:2412.19331](https://arxiv.org/abs/2412.19331) · 📚 被引 1
- **作者**: Kiet A. Nguyen, Adheesh Sunil Juvekar, Tianjiao Yu, Muntasir Wahed, Ismini Lourentzou
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in Large Vision-Language Models (LVLMs) have enabled general-purpose vision tasks through visual instruction tuning. While existing LVLMs can generate segmentation masks from text prompts for single images, they struggle with segmentation-grounded reasoning across images, especially at finer granularities such as object parts. In this paper, we introduce the new task of part-focused semantic co-segmentation, which involves identifying and segmenting common objects, as well as common and unique object parts across images. To address this task, we present CALICO, the first LVLM designed for multi-image part-level reasoning segmentation. CALICO features two key components, a novel Correspondence Extraction Module that identifies semantic part-level correspondences, and Correspondence Adaptation Modules that embed this information into the LVLM to facilitate multi-image understanding in a parameter-efficient manner. To support training and evaluation, we curate MixedParts, a large-scale multi-image segmentation dataset containing $\sim$2.4M samples across $\sim$44K images spanning diverse object and part categories. Experimental results demonstrate that CALICO, with just 0.3% of its parameters finetuned, achieves strong performance on this challenging task.

</details>

### NLPrompt: Noise-Label Prompt Learning for Vision-Language Models.
- **链接**: [arXiv:2412.01256](https://arxiv.org/abs/2412.01256) · 📚 被引 6
- **作者**: Bikang Pan, Qun Li, Xiaoying Tang, Wei Huang, Zhen Fang, Feng Liu et al.
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China, The Chinese University of Hong Kong,Shenzhen,China, RIKEN Center for Advanced Intelligence Project,Japan
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of vision-language foundation models, such as CLIP, has revolutionized image-text representation, enabling a broad range of applications via prompt learning. Despite its promise, real-world datasets often contain noisy labels that can degrade prompt learning performance. In this paper, we demonstrate that using mean absolute error (MAE) loss in prompt learning, named PromptMAE, significantly enhances robustness against noisy labels while maintaining high accuracy. Though MAE is straightforward and recognized for its robustness, it is rarely used in noisy-label learning due to its slow convergence and poor performance outside prompt learning scenarios. To elucidate the robustness of PromptMAE, we leverage feature learning theory to show that MAE can suppress the influence of noisy samples, thereby improving the signal-to-noise ratio and enhancing overall robustness. Additionally, we introduce PromptOT, a prompt-based optimal transport data purification method to enhance the robustness further. PromptOT employs text features in vision-language models as prototypes to construct an optimal transportation matrix. This matrix effectively partitions datasets into clean and noisy subsets, allowing for the application of cross-entropy loss to the clean subset and MAE loss to the noisy subset. Our Noise-Label Prompt Learning method, named NLPrompt, offers a simple and efficient approach that leverages the expressive representations and precise alignment capabilities of vision-language models for robust prompt learning. We validate NLPrompt through extensive experiments across various noise settings, demonstrating significant performance improvements.

</details>

### HalLoc: Token-level Localization of Hallucinations for Vision Language Models.
- **链接**: [arXiv:2506.10286](https://arxiv.org/abs/2506.10286) · 📚 被引 2
- **作者**: Eunkyu Park, Minyeong Kim, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hallucinations pose a significant challenge to the reliability of large vision-language models, making their detection essential for ensuring accuracy in critical applications. Current detection methods often rely on computationally intensive models, leading to high latency and resource demands. Their definitive outcomes also fail to account for real-world scenarios where the line between hallucinated and truthful information is unclear. To address these issues, we propose HalLoc, a dataset designed for efficient, probabilistic hallucination detection. It features 150K token-level annotated samples, including hallucination types, across Visual Question Answering (VQA), instruction-following, and image captioning tasks. This dataset facilitates the development of models that detect hallucinations with graded confidence, enabling more informed user interactions. Additionally, we introduce a baseline model trained on HalLoc, offering low-overhead, concurrent hallucination detection during generation. The model can be seamlessly integrated into existing VLMs, improving reliability while preserving efficiency. The prospect of a robust plug-and-play hallucination detection module opens new avenues for enhancing the trustworthiness of vision-language models in real-world applications. The HalLoc dataset and code are publicly available at: https://github.com/dbsltm/cvpr25_halloc.

</details>

### Hyperbolic Safety-Aware Vision-Language Models.
- **链接**: [arXiv:2503.12127](https://arxiv.org/abs/2503.12127) · 📚 被引 6
- **作者**: Tobia Poppi, Tejaswi Kasarla, Pascal Mettes, Lorenzo Baraldi, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy, University of Amsterdam,Netherlands
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Addressing the retrieval of unsafe content from vision-language models such as CLIP is an important step towards real-world integration. Current efforts have relied on unlearning techniques that try to erase the model's knowledge of unsafe concepts. While effective in reducing unwanted outputs, unlearning limits the model's capacity to discern between safe and unsafe content. In this work, we introduce a novel approach that shifts from unlearning to an awareness paradigm by leveraging the inherent hierarchical properties of the hyperbolic space. We propose to encode safe and unsafe content as an entailment hierarchy, where both are placed in different regions of hyperbolic space. Our HySAC, Hyperbolic Safety-Aware CLIP, employs entailment loss functions to model the hierarchical and asymmetrical relations between safe and unsafe image-text pairs. This modelling, ineffective in standard vision-language models due to their reliance on Euclidean embeddings, endows the model with awareness of unsafe content, enabling it to serve as both a multimodal unsafe classifier and a flexible content retriever, with the option to dynamically redirect unsafe queries toward safer alternatives or retain the original output. Extensive experiments show that our approach not only enhances safety recognition but also establishes a more adaptable and interpretable framework for content moderation in vision-language models. Our source code is available at https://github.com/aimagelab/HySAC.

</details>

### F3OCUS - Federated Finetuning of Vision-Language Foundation Models with Optimal Client Layer Updating Strategy via Multi-objective Meta-Heuristics.
- **链接**: [arXiv:2411.11912](https://arxiv.org/abs/2411.11912) · 📚 被引 4
- **作者**: Pramit Saha, Felix Wagner, Divyanshu Mishra, Can Peng, Anshul Thakur, David A. Clifton et al.
- **🏷️ 机构**: University of Oxford
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Effective training of large Vision-Language Models (VLMs) on resource-constrained client devices in Federated Learning (FL) requires the usage of parameter-efficient fine-tuning (PEFT) strategies. To this end, we demonstrate the impact of two factors \textit{viz.}, client-specific layer importance score that selects the most important VLM layers for fine-tuning and inter-client layer diversity score that encourages diverse layer selection across clients for optimal VLM layer selection. We first theoretically motivate and leverage the principal eigenvalue magnitude of layerwise Neural Tangent Kernels and show its effectiveness as client-specific layer importance score. Next, we propose a novel layer updating strategy dubbed F$^3$OCUS that jointly optimizes the layer importance and diversity factors by employing a data-free, multi-objective, meta-heuristic optimization on the server. We explore 5 different meta-heuristic algorithms and compare their effectiveness for selecting model layers and adapter layers towards PEFT-FL. Furthermore, we release a new MedVQA-FL dataset involving overall 707,962 VQA triplets and 9 modality-specific clients and utilize it to train and evaluate our method. Overall, we conduct more than 10,000 client-level experiments on 6 Vision-Language FL task settings involving 58 medical image datasets and 4 different VLM architectures of varying sizes to demonstrate the effectiveness of the proposed method.

</details>

### PARC: A Quantitative Framework Uncovering the Symmetries within Vision Language Models.
- **链接**: [arXiv:2506.14808](https://arxiv.org/abs/2506.14808) · 📚 被引 2
- **作者**: Jenny Schmalfuss, Nadine Chang, Vibashan VS, Maying Shen, Andrés Bruhn, José M. Álvarez
- **🏷️ 机构**: University of Stuttgart, NVIDIA, Johns Hopkins University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision language models (VLMs) respond to user-crafted text prompts and visual inputs, and are applied to numerous real-world problems. VLMs integrate visual modalities with large language models (LLMs), which are well known to be prompt-sensitive. Hence, it is crucial to determine whether VLMs inherit this instability to varying prompts. We therefore investigate which prompt variations VLMs are most sensitive to and which VLMs are most agnostic to prompt variations. To this end, we introduce PARC (Prompt Analysis via Reliability and Calibration), a VLM prompt sensitivity analysis framework built on three pillars: (1) plausible prompt variations in both the language and vision domain, (2) a novel model reliability score with built-in guarantees, and (3) a calibration step that enables dataset- and prompt-spanning prompt variation analysis. Regarding prompt variations, PARC's evaluation shows that VLMs mirror LLM language prompt sensitivity in the vision domain, and most destructive variations change the expected answer. Regarding models, outstandingly robust VLMs among 22 evaluated models come from the InternVL2 family. We further find indications that prompt sensitivity is linked to training data. The code will be at https://github.com/NVlabs/PARC.

</details>

### O-TPT: Orthogonality Constraints for Calibrating Test-time Prompt Tuning in Vision-Language Models.
- **链接**: [arXiv:2503.12096](https://arxiv.org/abs/2503.12096) · 📚 被引 8
- **作者**: Ashshak Sharifdeen, Muhammad Akhtar Munir, Sanoojan Baliah, Salman Khan, Muhammad Haris Khan
- **🏷️ 机构**: Mohamed Bin Zayed University of AI
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time prompt tuning for vision-language models (VLMs) is getting attention because of their ability to learn with unlabeled data without fine-tuning. Although test-time prompt tuning methods for VLMs can boost accuracy, the resulting models tend to demonstrate poor calibration, which casts doubts on the reliability and trustworthiness of these models. Notably, more attention needs to be devoted to calibrating the test-time prompt tuning in vision-language models. To this end, we propose a new approach, called O-TPT that introduces orthogonality constraints on the textual features corresponding to the learnable prompts for calibrating test-time prompt tuning in VLMs. Towards introducing orthogonality constraints, we make the following contributions. First, we uncover new insights behind the suboptimal calibration performance of existing methods relying on textual feature dispersion. Second, we show that imposing a simple orthogonalization of textual features is a more effective approach towards obtaining textual dispersion. We conduct extensive experiments on various datasets with different backbones and baselines. The results indicate that our method consistently outperforms the prior state of the art in significantly reducing the overall average calibration error. Also, our method surpasses the zero-shot calibration performance on fine-grained classification tasks.

</details>

### R-TPT: Improving Adversarial Robustness of Vision-Language Models through Test-Time Prompt Tuning.
- **链接**: [arXiv:2504.11195](https://arxiv.org/abs/2504.11195) · 📚 被引 5
- **作者**: Lijun Sheng, Jian Liang, Zilei Wang, Ran He
- **🏷️ 机构**: University of Science and Technology of China, Chinese Academy of Sciences,NLPR &#x0026; MAIS, Institute of Automation
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs), such as CLIP, have gained significant popularity as foundation models, with numerous fine-tuning methods developed to enhance performance on downstream tasks. However, due to their inherent vulnerability and the common practice of selecting from a limited set of open-source models, VLMs suffer from a higher risk of adversarial attacks than traditional vision models. Existing defense techniques typically rely on adversarial fine-tuning during training, which requires labeled data and lacks of flexibility for downstream tasks. To address these limitations, we propose robust test-time prompt tuning (R-TPT), which mitigates the impact of adversarial attacks during the inference stage. We first reformulate the classic marginal entropy objective by eliminating the term that introduces conflicts under adversarial conditions, retaining only the pointwise entropy minimization. Furthermore, we introduce a plug-and-play reliability-based weighted ensembling strategy, which aggregates useful information from reliable augmented views to strengthen the defense. R-TPT enhances defense against adversarial attacks without requiring labeled training data while offering high flexibility for inference tasks. Extensive experiments on widely used benchmarks with various attacks demonstrate the effectiveness of R-TPT. The code is available in https://github.com/TomSheng21/R-TPT.

</details>

### Taxonomy-Aware Evaluation of Vision-Language Models.
- **链接**: [arXiv:2504.05457](https://arxiv.org/abs/2504.05457)
- **作者**: Vésteinn Snæbjarnarson, Kevin Du, Niklas Stoehr, Serge J. Belongie, Ryan Cotterell, Nico Lang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> When a vision-language model (VLM) is prompted to identify an entity depicted in an image, it may answer 'I see a conifer,' rather than the specific label 'norway spruce'. This raises two issues for evaluation: First, the unconstrained generated text needs to be mapped to the evaluation label space (i.e., 'conifer'). Second, a useful classification measure should give partial credit to less-specific, but not incorrect, answers ('norway spruce' being a type of 'conifer'). To meet these requirements, we propose a framework for evaluating unconstrained text predictions, such as those generated from a vision-language model, against a taxonomy. Specifically, we propose the use of hierarchical precision and recall measures to assess the level of correctness and specificity of predictions with regard to a taxonomy. Experimentally, we first show that existing text similarity measures do not capture taxonomic similarity well. We then develop and compare different methods to map textual VLM predictions onto a taxonomy. This allows us to compute hierarchical similarity measures between the generated text and the ground truth labels. Finally, we analyze modern VLMs on fine-grained visual classification tasks based on our proposed taxonomic evaluation scheme.

</details>

### RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics.
- **链接**: [arXiv:2411.16537](https://arxiv.org/abs/2411.16537) · 📚 被引 19
- **作者**: Chan Hee Song, Valts Blukis, Jonathan Tremblay, Stephen Tyree, Yu Su, Stan Birchfield
- **🏷️ 机构**: The Ohio State University, NVIDIA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatial understanding is a crucial capability that enables robots to perceive their surroundings, reason about their environment, and interact with it meaningfully. In modern robotics, these capabilities are increasingly provided by vision-language models. However, these models face significant challenges in spatial reasoning tasks, as their training data are based on general-purpose image datasets that often lack sophisticated spatial understanding. For example, datasets frequently do not capture reference frame comprehension, yet effective spatial reasoning requires understanding whether to reason from ego-, world-, or object-centric perspectives. To address this issue, we introduce RoboSpatial, a large-scale dataset for spatial understanding in robotics. It consists of real indoor and tabletop scenes, captured as 3D scans and egocentric images, and annotated with rich spatial information relevant to robotics. The dataset includes 1M images, 5k 3D scans, and 3M annotated spatial relationships, and the pairing of 2D egocentric images with 3D scans makes it both 2D- and 3D- ready. Our experiments show that models trained with RoboSpatial outperform baselines on downstream tasks such as spatial affordance prediction, spatial relationship prediction, and robot manipulation.

</details>

### From Head to Tail: Towards Balanced Representation in Large Vision-Language Models through Adaptive Data Calibration.
- **链接**: [arXiv:2503.12821](https://arxiv.org/abs/2503.12821) · 📚 被引 0
- **作者**: Mingyang Song, Xiaoye Qu, Jiawei Zhou, Yu Cheng
- **🏷️ 机构**: Fudan University, Shanghai Artificial Intelligence Laboratory, Stony Brook University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) have achieved significant progress in combining visual comprehension with language generation. Despite this success, the training data of LVLMs still suffers from Long-Tail (LT) problems, where the data distribution is highly imbalanced. Previous works have mainly focused on traditional VLM architectures, i.e., CLIP or ViT, and specific tasks such as recognition and classification. Nevertheless, the exploration of LVLM (e.g. LLaVA) and more general tasks (e.g. Visual Question Answering and Visual Reasoning) remains under-explored. In this paper, we first conduct an in-depth analysis of the LT issues in LVLMs and identify two core causes: the overrepresentation of head concepts and the underrepresentation of tail concepts. Based on the above observation, we propose an $\textbf{A}$daptive $\textbf{D}$ata $\textbf{R}$efinement Framework ($\textbf{ADR}$), which consists of two stages: $\textbf{D}$ata $\textbf{R}$ebalancing ($\textbf{DR}$) and $\textbf{D}$ata $\textbf{S}$ynthesis ($\textbf{DS}$). In the DR stage, we adaptively rebalance the redundant data based on entity distributions, while in the DS stage, we leverage Denoising Diffusion Probabilistic Models (DDPMs) and scarce images to supplement underrepresented portions. Through comprehensive evaluations across eleven benchmarks, our proposed ADR effectively mitigates the long-tail problem in the training data, improving the average performance of LLaVA 1.5 relatively by 4.36%, without increasing the training data volume.

</details>

### LayoutVLM: Differentiable Optimization of 3D Layout via Vision-Language Models.
- **链接**: [arXiv:2412.02193](https://arxiv.org/abs/2412.02193) · 📚 被引 25
- **作者**: Fan-Yun Sun, Weiyu Liu, Siyi Gu, Dylan Lim, Goutam Bhat, Federico Tombari et al.
- **🏷️ 机构**: Stanford University, Google Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatial reasoning is a fundamental aspect of human cognition, enabling intuitive understanding and manipulation of objects in three-dimensional space. While foundation models demonstrate remarkable performance on some benchmarks, they still struggle with 3D reasoning tasks like arranging objects in space according to open-ended language instructions, particularly in dense and physically constrained environments. We introduce LayoutVLM, a framework and scene layout representation that exploits the semantic knowledge of Vision-Language Models (VLMs) and supports differentiable optimization to ensure physical plausibility. LayoutVLM employs VLMs to generate two mutually reinforcing representations from visually marked images, and a self-consistent decoding process to improve VLMs spatial planning. Our experiments show that LayoutVLM addresses the limitations of existing LLM and constraint-based approaches, producing physically plausible 3D layouts better aligned with the semantic intent of input language instructions. We also demonstrate that fine-tuning VLMs with the proposed scene layout representation extracted from existing scene datasets can improve their reasoning performance.

</details>

### Identifying and Mitigating Position Bias of Multi-image Vision-Language Models.
- **链接**: [arXiv:2503.13792](https://arxiv.org/abs/2503.13792) · 📚 被引 2
- **作者**: Xinyu Tian, Shu Zou, Zhaoyuan Yang, Jing Zhang
- **🏷️ 机构**: Australian National University, GE Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The evolution of Large Vision-Language Models (LVLMs) has progressed from single to multi-image reasoning. Despite this advancement, our findings indicate that LVLMs struggle to robustly utilize information across multiple images, with predictions significantly affected by the alteration of image positions. To further explore this issue, we introduce Position-wise Question Answering (PQA), a meticulously designed task to quantify reasoning capabilities at each position. Our analysis reveals a pronounced position bias in LVLMs: open-source models excel in reasoning with images positioned later but underperform with those in the middle or at the beginning, while proprietary models show improved comprehension for images at the beginning and end but struggle with those in the middle. Motivated by this, we propose SoFt Attention (SoFA), a simple, training-free approach that mitigates this bias by employing linear interpolation between inter-image causal attention and bidirectional counterparts. Experimental results demonstrate that SoFA reduces position bias and enhances the reasoning performance of existing LVLMs.

</details>

### On the Zero-shot Adversarial Robustness of Vision-Language Models: A Truly Zero-shot and Training-free Approach.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tong_On_the_Zero-shot_Adversarial_Robustness_of_Vision-Language_Models_A_Truly_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Baoshun Tong, Hanjiang Lai, Yan Pan, Jian Yin
- **🏷️ 机构**: Sun Yat-Sen University,China
- **会议**: CVPR 2025

### STING-BEE: Towards Vision-Language Model for Real-World X-ray Baggage Security Inspection.
- **链接**: [arXiv:2504.02823](https://arxiv.org/abs/2504.02823) · 📚 被引 9
- **作者**: Divya Velayudhan, Abdelfatah Hassan Ahmed, Mohamad Alansari, Neha Gour, Abderaouf Behouch, Taimur Hassan et al.
- **🏷️ 机构**: Khalifa University of Science and Technology, Abu Dhabi University, University of Bonn
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Advancements in Computer-Aided Screening (CAS) systems are essential for improving the detection of security threats in X-ray baggage scans. However, current datasets are limited in representing real-world, sophisticated threats and concealment tactics, and existing approaches are constrained by a closed-set paradigm with predefined labels. To address these challenges, we introduce STCray, the first multimodal X-ray baggage security dataset, comprising 46,642 image-caption paired scans across 21 threat categories, generated using an X-ray scanner for airport security. STCray is meticulously developed with our specialized protocol that ensures domain-aware, coherent captions, that lead to the multi-modal instruction following data in X-ray baggage security. This allows us to train a domain-aware visual AI assistant named STING-BEE that supports a range of vision-language tasks, including scene comprehension, referring threat localization, visual grounding, and visual question answering (VQA), establishing novel baselines for multi-modal learning in X-ray baggage security. Further, STING-BEE shows state-of-the-art generalization in cross-domain settings. Code, data, and models are available at https://divs1159.github.io/STING-BEE/.

</details>

### TAPT: Test-Time Adversarial Prompt Tuning for Robust Inference in Vision-Language Models.
- **链接**: [arXiv:2411.13136](https://arxiv.org/abs/2411.13136) · 📚 被引 3
- **作者**: Xin Wang, Kai Chen, Jiaming Zhang, Jingjing Chen, Xingjun Ma
- **🏷️ 机构**: Fudan University,Shanghai Key Lab of Intell. Info. Processing, School of CS, Hong Kong University of Science and Technology
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large pre-trained Vision-Language Models (VLMs) such as CLIP have demonstrated excellent zero-shot generalizability across various downstream tasks. However, recent studies have shown that the inference performance of CLIP can be greatly degraded by small adversarial perturbations, especially its visual modality, posing significant safety threats. To mitigate this vulnerability, in this paper, we propose a novel defense method called Test-Time Adversarial Prompt Tuning (TAPT) to enhance the inference robustness of CLIP against visual adversarial attacks. TAPT is a test-time defense method that learns defensive bimodal (textual and visual) prompts to robustify the inference process of CLIP. Specifically, it is an unsupervised method that optimizes the defensive prompts for each test sample by minimizing a multi-view entropy and aligning adversarial-clean distributions. We evaluate the effectiveness of TAPT on 11 benchmark datasets, including ImageNet and 10 other zero-shot datasets, demonstrating that it enhances the zero-shot adversarial robustness of the original CLIP by at least 48.9% against AutoAttack (AA), while largely maintaining performance on clean examples. Moreover, TAPT outperforms existing adversarial prompt tuning methods across various backbones, achieving an average robustness improvement of at least 36.6%.

</details>

### Embodied Scene Understanding for Vision Language Models via MetaVQA.
- **链接**: [arXiv:2501.09167](https://arxiv.org/abs/2501.09167) · 📚 被引 5
- **作者**: Weizhen Wang, Chenda Duan, Zhenghao Peng, Yuxin Liu, Bolei Zhou
- **🏷️ 机构**: University of California,Los Angeles
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Language Models (VLMs) demonstrate significant potential as embodied AI agents for various mobility applications. However, a standardized, closed-loop benchmark for evaluating their spatial reasoning and sequential decision-making capabilities is lacking. To address this, we present MetaVQA: a comprehensive benchmark designed to assess and enhance VLMs' understanding of spatial relationships and scene dynamics through Visual Question Answering (VQA) and closed-loop simulations. MetaVQA leverages Set-of-Mark prompting and top-down view ground-truth annotations from nuScenes and Waymo datasets to automatically generate extensive question-answer pairs based on diverse real-world traffic scenarios, ensuring object-centric and context-rich instructions. Our experiments show that fine-tuning VLMs with the MetaVQA dataset significantly improves their spatial reasoning and embodied scene comprehension in safety-critical simulations, evident not only in improved VQA accuracies but also in emerging safety-aware driving maneuvers. In addition, the learning demonstrates strong transferability from simulation to real-world observation. Code and data will be publicly available at https://metadriverse.github.io/metavqa .

</details>

### Vision-Language Model IP Protection via Prompt-based Learning.
- **链接**: [arXiv:2503.02393](https://arxiv.org/abs/2503.02393) · 📚 被引 2
- **作者**: Lianyu Wang, Meng Wang, Huazhu Fu, Daoqiang Zhang
- **🏷️ 机构**: Ministry of Education,The Key Laboratory of Brain-Machine Intelligence Technology,China, National University of Singapore,Centre for Innovation and Precision Eye Health, Yong Loo Lin School of Medicine, Institute of High Performance Computing, Agency for Science, Technology and Research,Singapore
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) like CLIP (Contrastive Language-Image Pre-Training) have seen remarkable success in visual recognition, highlighting the increasing need to safeguard the intellectual property (IP) of well-trained models. Effective IP protection extends beyond ensuring authorized usage; it also necessitates restricting model deployment to authorized data domains, particularly when the model is fine-tuned for specific target domains. However, current IP protection methods often rely solely on the visual backbone, which may lack sufficient semantic richness. To bridge this gap, we introduce IP-CLIP, a lightweight IP protection strategy tailored to CLIP, employing a prompt-based learning approach. By leveraging the frozen visual backbone of CLIP, we extract both image style and content information, incorporating them into the learning of IP prompt. This strategy acts as a robust barrier, effectively preventing the unauthorized transfer of features from authorized domains to unauthorized ones. Additionally, we propose a style-enhancement branch that constructs feature banks for both authorized and unauthorized domains. This branch integrates self-enhanced and cross-domain features, further strengthening IP-CLIP's capability to block features from unauthorized domains. Finally, we present new three metrics designed to better balance the performance degradation of authorized and unauthorized domains. Comprehensive experiments in various scenarios demonstrate its promising potential for application in IP protection tasks for VLMs.

</details>

### Steering Away from Harm: An Adaptive Approach to Defending Vision Language Model Against Jailbreaks.
- **链接**: [arXiv:2411.16721](https://arxiv.org/abs/2411.16721) · 📚 被引 4
- **作者**: Han Wang, Gang Wang, Huan Zhang
- **🏷️ 机构**: University of Illinois Urbana-Champaign
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Language Models (VLMs) can produce unintended and harmful content when exposed to adversarial attacks, particularly because their vision capabilities create new vulnerabilities. Existing defenses, such as input preprocessing, adversarial training, and response evaluation-based methods, are often impractical for real-world deployment due to their high costs. To address this challenge, we propose ASTRA, an efficient and effective defense by adaptively steering models away from adversarial feature directions to resist VLM attacks. Our key procedures involve finding transferable steering vectors representing the direction of harmful response and applying adaptive activation steering to remove these directions at inference time. To create effective steering vectors, we randomly ablate the visual tokens from the adversarial images and identify those most strongly associated with jailbreaks. These tokens are then used to construct steering vectors. During inference, we perform the adaptive steering method that involves the projection between the steering vectors and calibrated activation, resulting in little performance drops on benign inputs while strongly avoiding harmful outputs under adversarial inputs. Extensive experiments across multiple models and baselines demonstrate our state-of-the-art performance and high efficiency in mitigating jailbreak risks. Additionally, ASTRA exhibits good transferability, defending against unseen attacks (i.e., structured-based attack, perturbation-based attack with project gradient descent variants, and text-only attack). Our code is available at \url{https://github.com/ASTRAL-Group/ASTRA}.

</details>

### Towards Understanding How Knowledge Evolves in Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Towards_Understanding_How_Knowledge_Evolves_in_Large_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Sudong Wang, Yunjian Zhang, Yao Zhu, Jianing Li, Zizhe Wang, Yanwei Liu et al.
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Information Engeering, Tsinghua University
- **会议**: CVPR 2025

### Synthetic Data is an Elegant GIFT for Continual Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Synthetic_Data_is_an_Elegant_GIFT_for_Continual_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Bin Wu, Wuxuan Shi, Jinqiao Wang, Mang Ye
- **🏷️ 机构**: Wuhan University,School of Computer Science,Wuhan,China, Chinese Academy of Sciences,Institute of Automation,Beijing,China
- **会议**: CVPR 2025

### Chain of Attack: On the Robustness of Vision-Language Models Against Transfer-Based Adversarial Attacks.
- **链接**: [arXiv:2411.15720](https://arxiv.org/abs/2411.15720) · 📚 被引 9
- **作者**: Peng Xie, Yequan Bie, Jianda Mao, Yangqiu Song, Yang Wang, Hao Chen et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology,Hong Kong,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models (VLMs) have showcased remarkable performance in image and natural language understanding, such as image captioning and response generation. As the practical applications of vision-language models become increasingly widespread, their potential safety and robustness issues raise concerns that adversaries may evade the system and cause these models to generate toxic content through malicious attacks. Therefore, evaluating the robustness of open-source VLMs against adversarial attacks has garnered growing attention, with transfer-based attacks as a representative black-box attacking strategy. However, most existing transfer-based attacks neglect the importance of the semantic correlations between vision and text modalities, leading to sub-optimal adversarial example generation and attack performance. To address this issue, we present Chain of Attack (CoA), which iteratively enhances the generation of adversarial examples based on the multi-modal semantic update using a series of intermediate attacking steps, achieving superior adversarial transferability and efficiency. A unified attack success rate computing method is further proposed for automatic evasion evaluation. Extensive experiments conducted under the most realistic and high-stakes scenario, demonstrate that our attacking strategy can effectively mislead models to generate targeted responses using only black-box attacks without any knowledge of the victim models. The comprehensive robustness evaluation in our paper provides insight into the vulnerabilities of VLMs and offers a reference for the safety considerations of future model developments.

</details>

### SmartCLIP: Modular Vision-language Alignment with Identification Guarantees.
- **链接**: [arXiv:2507.22264](https://arxiv.org/abs/2507.22264) · 📚 被引 2
- **作者**: Shaoan Xie, Lingjing, Yujia Zheng, Yu Yao, Zeyu Tang, Eric P. Xing et al.
- **🏷️ 机构**: Carnegie Mellon University, University of Sydney, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Language-Image Pre-training (CLIP)~\citep{radford2021learning} has emerged as a pivotal model in computer vision and multimodal learning, achieving state-of-the-art performance at aligning visual and textual representations through contrastive learning. However, CLIP struggles with potential information misalignment in many image-text datasets and suffers from entangled representation. On the one hand, short captions for a single image in datasets like MSCOCO may describe disjoint regions in the image, leaving the model uncertain about which visual features to retain or disregard. On the other hand, directly aligning long captions with images can lead to the retention of entangled details, preventing the model from learning disentangled, atomic concepts -- ultimately limiting its generalization on certain downstream tasks involving short prompts. In this paper, we establish theoretical conditions that enable flexible alignment between textual and visual representations across varying levels of granularity. Specifically, our framework ensures that a model can not only \emph{preserve} cross-modal semantic information in its entirety but also \emph{disentangle} visual representations to capture fine-grained textual concepts. Building on this foundation, we introduce \ours, a novel approach that identifies and aligns the most relevant visual and textual representations in a modular manner. Superior performance across various tasks demonstrates its capability to handle information misalignment and supports our identification theory. The code is available at https://github.com/Mid-Push/SmartCLIP.

</details>

### Conical Visual Concentration for Efficient Large Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xing_Conical_Visual_Concentration_for_Efficient_Large_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Long Xing, Qidong Huang, Xiaoyi Dong, Jiajie Lu, Pan Zhang, Yuhang Zang et al.
- **🏷️ 机构**: University of Science and Technology of China, Shanghai AI Laboratory
- **会议**: CVPR 2025

### Post-pre-training for Modality Alignment in Vision-Language Foundation Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yamaguchi_Post-pre-training_for_Modality_Alignment_in_Vision-Language_Foundation_Models_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Shin'ya Yamaguchi, Dewei Feng, Sekitoshi Kanai, Kazuki Adachi, Daiki Chijiwa
- **🏷️ 机构**: NTT, MIT
- **会议**: CVPR 2025

### ResCLIP: Residual Attention for Training-free Dense Vision-language Inference.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.html) · 📚 被引 12
- **作者**: Yuhang Yang, Jinhong Deng, Wen Li, Lixin Duan
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: CVPR 2025

### Mitigating Hallucinations in Large Vision-Language Models via DPO: On-Policy Data Hold the Key.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Mitigating_Hallucinations_in_Large_Vision-Language_Models_via_DPO_On-Policy_Data_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Zhihe Yang, Xufang Luo, Dongqi Han, Yunjian Xu, Dongsheng Li
- **🏷️ 机构**: The Chinese University of Hong Kong, Microsoft Research Asia
- **会议**: CVPR 2025

### Once-Tuning-Multiple-Variants: Tuning Once and Expanded as Multiple Vision-Language Model Variants.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_Once-Tuning-Multiple-Variants_Tuning_Once_and_Expanded_as_Multiple_Vision-Language_Model_Variants_CVPR_2025_paper.html) · 📚 被引 0
- **作者**: Chong Yu, Tao Chen, Zhongxue Gan
- **🏷️ 机构**: Fudan University,Academy for Engineering and Technology,Shanghai,China,200433, Fudan University,School for Information Science and Technology,Shanghai,China,200433
- **会议**: CVPR 2025

### Realistic Test-Time Adaptation of Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zanella_Realistic_Test-Time_Adaptation_of_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Maxime Zanella, Clément Fuchs, Christophe De Vleeschouwer, Ismail Ben Ayed
- **🏷️ 机构**: UCLouvain,Belgium, &#x00C9;TS Montreal,Canada
- **会议**: CVPR 2025

### SPA-VL: A Comprehensive Safety Preference Alignment Dataset for Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_SPA-VL_A_Comprehensive_Safety_Preference_Alignment_Dataset_for_Vision_Language_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: Yongting Zhang, Lu Chen, Guodong Zheng, Yifeng Gao, Rui Zheng, Jinlan Fu et al.
- **🏷️ 机构**: University of Science and Technology of China, Fudan University, Shanghai Artificial Intelligence Laboratory
- **会议**: CVPR 2025

### Adaptive Parameter Selection for Tuning Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Adaptive_Parameter_Selection_for_Tuning_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Yi Zhang, Yi-Xuan Deng, Meng-Hao Guo, Shi-Min Hu
- **🏷️ 机构**: Beihang University,State Key Laboratory of Virtual Reality Technology and Systems, SCSE, Tsinghua University,Zhili College, Tsinghua University,BNRist,Department of Computer Science and Technology
- **会议**: CVPR 2025

### Joint Vision-Language Social Bias Removal for CLIP.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Joint_Vision-Language_Social_Bias_Removal_for_CLIP_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Haoyu Zhang, Yangyang Guo, Mohan S. Kankanhalli
- **🏷️ 机构**: National University of Singapore
- **会议**: CVPR 2025

### Automated Generation of Challenging Multiple-Choice Questions for Vision Language Model Evaluation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Automated_Generation_of_Challenging_Multiple-Choice_Questions_for_Vision_Language_Model_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Yuhui Zhang, Yuchang Su, Yiming Liu, Xiaohan Wang, James Burgess, Elaine Sui et al.
- **🏷️ 机构**: Stanford University, Tsinghua University, MIT
- **会议**: CVPR 2025

### Bayesian Test-Time Adaptation for Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Bayesian_Test-Time_Adaptation_for_Vision-Language_Models_CVPR_2025_paper.html) · 📚 被引 7
- **作者**: Lihua Zhou, Mao Ye, Shuaifeng Li, Nianxin Li, Xiatian Zhu, Lei Deng et al.
- **🏷️ 机构**: CAIR, HKSIS, CAS, UESTC, University of Surrey
- **会议**: CVPR 2025

### FireEdit: Fine-grained Instruction-based Image Editing via Region-aware Vision Language Model.
- **链接**: [arXiv:2503.19839](https://arxiv.org/abs/2503.19839) · 📚 被引 7
- **作者**: Jun Zhou, Jiahao Li, Zunnan Xu, Hanhui Li, Yiji Cheng, Fa-Ting Hong et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, Tencent,Hunyuan, Tsinghua University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Currently, instruction-based image editing methods have made significant progress by leveraging the powerful cross-modal understanding capabilities of vision language models (VLMs). However, they still face challenges in three key areas: 1) complex scenarios; 2) semantic consistency; and 3) fine-grained editing. To address these issues, we propose FireEdit, an innovative Fine-grained Instruction-based image editing framework that exploits a REgion-aware VLM. FireEdit is designed to accurately comprehend user instructions and ensure effective control over the editing process. Specifically, we enhance the fine-grained visual perception capabilities of the VLM by introducing additional region tokens. Relying solely on the output of the LLM to guide the diffusion model may lead to suboptimal editing results. Therefore, we propose a Time-Aware Target Injection module and a Hybrid Visual Cross Attention module. The former dynamically adjusts the guidance strength at various denoising stages by integrating timestep embeddings with the text embeddings. The latter enhances visual details for image editing, thereby preserving semantic consistency between the edited result and the source image. By combining the VLM enhanced with fine-grained region tokens and the time-dependent diffusion model, FireEdit demonstrates significant advantages in comprehending editing instructions and maintaining high semantic consistency. Extensive experiments indicate that our approach surpasses the state-of-the-art instruction-based image editing methods. Our project is available at https://zjgans.github.io/fireedit.github.io.

</details>

### CoSpace: Benchmarking Continuous Space Perception Ability for Vision-Language Models.
- **链接**: [arXiv:2503.14161](https://arxiv.org/abs/2503.14161) · 📚 被引 0
- **作者**: Yiqi Zhu, Ziyue Wang, Can Zhang, Peng Li, Yang Liu
- **🏷️ 机构**: Tsinghua University,Institute for AI,Dept. of Comp. Sci. &#x0026; Tech.,Beijing,China, University of Science and Technology,School of Computer and Communication Engineering,Beijing, Tsinghua University,Institute for AI Industry Research (AIR),Beijing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have recently witnessed significant progress in visual comprehension. As the permitting length of image context grows, VLMs can now comprehend a broader range of views and spaces. Current benchmarks provide insightful analysis of VLMs in tasks involving complex visual instructions following, multi-image understanding and spatial reasoning. However, they usually focus on spatially irrelevant images or discrete images captured from varied viewpoints. The compositional characteristic of images captured from a static viewpoint remains underestimated. We term this characteristic as Continuous Space Perception. When observing a scene from a static viewpoint while shifting orientations, it produces a series of spatially continuous images, enabling the reconstruction of the entire space. In this paper, we present CoSpace, a multi-image visual understanding benchmark designed to assess the Continuous Space perception ability for VLMs. CoSpace contains 2,918 images and 1,626 question-answer pairs, covering seven types of tasks. We conduct evaluation across 19 proprietary and open-source VLMs. Results reveal that there exist pitfalls on the continuous space perception ability for most of the evaluated models, including proprietary ones. Interestingly, we find that the main discrepancy between open-source and proprietary models lies not in accuracy but in the consistency of responses. We believe that enhancing the ability of continuous space perception is essential for VLMs to perform effectively in real-world tasks and encourage further research to advance this capability.

</details>

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
- Task Preference Optimization: Improving Multimodal Large Language Models with Vision Task Alignment. → [multimodal](../multimodal/Guideline%202025.md)
- PVC: Progressive Visual Token Compression for Unified Image and Video Processing in Large Vision-Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- Libra-Merging: Importance-redundancy and Pruning-merging Trade-off for Acceleration Plug-in in Large Vision-Language Model. → [network-pruning](../network-pruning/Guideline%202025.md)
- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models. → [video-understanding](../video-understanding/Guideline%202025.md)
- Anyattack: Towards Large-scale Self-supervised Adversarial Attacks on Vision-language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Accelerating Multimodal Large Language Models by Searching Optimal Vision Token Reduction. → [multimodal](../multimodal/Guideline%202025.md)
- Bridging Modalities: Improving Universal Multimodal Retrieval by Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- LoRASculpt: Sculpting LoRA for Harmonizing General and Specialized Knowledge in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- 4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- RAP: Retrieval-Augmented Personalization for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- XLRS-Bench: Could Your Multimodal LLMs Understand Extremely Large Ultra-High-Resolution Remote Sensing Imagery? → [multimodal](../multimodal/Guideline%202025.md)
- Cross-modal Information Flow in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- CoMM: A Coherent Interleaved Image-Text Dataset for Multimodal Understanding and Generation. → [multimodal](../multimodal/Guideline%202025.md)
- Augmenting Multimodal LLMs with Self-Reflective Tokens for Knowledge-based Visual Question Answering. → [multimodal](../multimodal/Guideline%202025.md)
- Insight-V: Exploring Long-Chain Visual Reasoning with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- AdaMMS: Model Merging for Heterogeneous Multimodal Large Language Models with Unsupervised Coefficient Optimization. → [multimodal](../multimodal/Guideline%202025.md)
- GroundingFace: Fine-grained Face Understanding via Pixel Grounding Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- CL-MoE: Enhancing Multimodal Large Language Model with Dual Momentum Mixture-of-Experts for Continual Visual Question Answering. → [multimodal](../multimodal/Guideline%202025.md)
- Playing the Fool: Jailbreaking LLMs and Multimodal LLMs with Out-of-Distribution Strategy. → [multimodal](../multimodal/Guideline%202025.md)
- Img-Diff: Contrastive Data Synthesis for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
