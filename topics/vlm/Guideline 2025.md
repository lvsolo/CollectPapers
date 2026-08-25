# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 58 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology.
- **链接**: [出版页](https://openreview.net/forum?id=rUvCIvI4eB)
- **作者**: Xiangyu Wang, Donglin Yang, Ziqin Wang, Hohin Kwan, Jinyu Chen, Wenjun Wu et al.
- **🏷️ 机构**: CUHK
- **会议**: ICLR 2025

### DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=VOAMTA8jKu)
- **作者**: Chengke Zou, Xingang Guo, Rui Yang, Junyu Zhang, Bin Hu, Huan Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Tracking the Copyright of Large Vision-Language Models through Parameter Learning Adversarial Images.
- **链接**: [arXiv:2502.16593](https://arxiv.org/abs/2502.16593)
- **作者**: Yubo Wang, Jianting Tang, Chaohu Liu, Linli Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

- **摘要（英，原文）**:

  > Large vision-language models (LVLMs) have demonstrated remarkable image understanding and dialogue capabilities, allowing them to handle a variety of visual question answering tasks. However, their widespread availability raises concerns about unauthorized usage and copyright infringement, where users or individuals can develop their own LVLMs by fine-tuning published models. In this paper, we propose a novel method called Parameter Learning Attack (PLA) for tracking the copyright of LVLMs without modifying the original model. Specifically, we construct adversarial images through targeted attacks against the original model, enabling it to generate specific outputs. To ensure these attacks remain effective on potential fine-tuned models to trigger copyright tracking, we allow the original model to learn the trigger images by updating parameters in the opposite direction during the adversarial attack process. Notably, the proposed method can be applied after the release of the original model, thus not affecting the model's performance and behavior. To simulate real-world applications, we fine-tune the original model using various strategies across diverse datasets, creating a range of models for copyright verification. Extensive experiments demonstrate that our method can more effectively identify the original copyright of fine-tuned models compared to baseline methods. Therefore, this work provides a powerful tool for tracking copyrights and detecting unlicensed usage of LVLMs.

### Prompt as Knowledge Bank: Boost Vision-language model via Structural Representation for zero-shot medical detection.
- **链接**: [arXiv:2502.16223](https://arxiv.org/abs/2502.16223)
- **作者**: Yuguang Yang, Tongfei Chen, Haoyu Huang, Linlin Yang, Chunyu Xie, Dawei Leng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

- **摘要（英，原文）**:

  > Zero-shot medical detection can further improve detection performance without relying on annotated medical images even upon the fine-tuned model, showing great clinical value. Recent studies leverage grounded vision-language models (GLIP) to achieve this by using detailed disease descriptions as prompts for the target disease name during the inference phase. However, these methods typically treat prompts as equivalent context to the target name, making it difficult to assign specific disease knowledge based on visual information, leading to a coarse alignment between images and target descriptions. In this paper, we propose StructuralGLIP, which introduces an auxiliary branch to encode prompts into a latent knowledge bank layer-by-layer, enabling more context-aware and fine-grained alignment. Specifically, in each layer, we select highly similar features from both the image representation and the knowledge bank, forming structural representations that capture nuanced relationships between image patches and target descriptions. These features are then fused across modalities to further enhance detection performance. Extensive experiments demonstrate that StructuralGLIP achieves a +4.1\% AP improvement over prior state-of-the-art methods across seven zero-shot medical detection benchmarks, and consistently improves fine-tuned models by +3.2\% AP on endoscopy image datasets.

### How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?
- **链接**: [arXiv:2410.07571](https://arxiv.org/abs/2410.07571)
- **作者**: Seongyun Lee, Geewook Kim, Jiyeon Kim, Hyunji Lee, Hoyeon Chang, Sue Hyun Park et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

- **摘要（英，原文）**:

  > Vision-Language adaptation (VL adaptation) transforms Large Language Models (LLMs) into Large Vision-Language Models (LVLMs) for multimodal tasks, but this process often compromises the inherent safety capabilities embedded in the original LLMs. Despite potential harmfulness due to weakened safety measures, in-depth analysis on the effects of VL adaptation on safety remains under-explored. This study examines how VL adaptation influences safety and evaluates the impact of safety fine-tuning methods. Our analysis reveals that safety degradation occurs during VL adaptation, even when the training data is safe. While safety tuning techniques like supervised fine-tuning with safety datasets or reinforcement learning from human feedback mitigate some risks, they still lead to safety degradation and a reduction in helpfulness due to over-rejection issues. Further analysis of internal model weights suggests that VL adaptation may impact certain safety-related layers, potentially lowering overall safety levels. Additionally, our findings demonstrate that the objectives of VL adaptation and safety tuning are divergent, which often results in their simultaneous application being suboptimal. To address this, we suggest the weight merging approach as an optimal solution effectively reducing safety degradation while maintaining helpfulness. These insights help guide the development of more reliable and secure LVLMs for real-world applications.

### Natural Language Inference Improves Compositionality in Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=G3aXjVAJjU)
- **作者**: Paola Cascante-Bonilla, Yu Hou, Yang Trista Cao, Hal Daumé III, Rachel Rudinger
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=tTBXePRKSx)
- **作者**: Ce Zhang, Zifu Wan, Zhehan Kan, Martin Q. Ma, Simon Stepputtis, Deva Ramanan et al.
- **🏷️ 机构**: CMU
- **会议**: ICLR 2025

### Are Large Vision Language Models Good Game Players?
- **链接**: [出版页](https://openreview.net/forum?id=c4OGMNyzPT)
- **作者**: Xinyu Wang, Bohan Zhuang, Qi Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Generating CAD Code with Vision-Language Models for 3D Designs.
- **链接**: [出版页](https://openreview.net/forum?id=BLWaTeucYX)
- **作者**: Kamel Alrashedy, Pradyumna Tambwekar, Zulfiqar Haider Zaidi, Megan Langwasser, Wei Xu, Matthew C. Gombolay
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Attribute-based Visual Reprogramming for Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=j964C6y92q)
- **作者**: Chengyi Cai, Zesheng Ye, Lei Feng, Jianzhong Qi, Feng Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Noisy Test-Time Adaptation in Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=iylpeTI0Ql)
- **作者**: Chentao Cao, Zhun Zhong, Zhanke Zhou, Tongliang Liu, Yang Liu, Kun Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension.
- **链接**: [出版页](https://openreview.net/forum?id=PgXpOOqtyd)
- **作者**: Amaia Cardiel, Eloi Zablocki, Elias Ramzi, Oriane Siméoni, Matthieu Cord
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding.
- **链接**: [出版页](https://openreview.net/forum?id=Q6a9W6kzv5)
- **作者**: Wei Chow, Jiageng Mao, Boyi Li, Daniel Seita, Vitor Campagnolo Guizilini, Yue Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Locality Alignment Improves Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=qssVptHTPN)
- **作者**: Ian Connick Covert, Tony Sun, James Zou, Tatsunori Hashimoto
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Tree of Attributes Prompt Learning for Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=wFs2E5wCw6)
- **作者**: Tong Ding, Wanhua Li, Zhongqi Miao, Hanspeter Pfister
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time.
- **链接**: [出版页](https://openreview.net/forum?id=QoDDNkx4fP)
- **作者**: Yi Ding, Bolian Li, Ruqi Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### ColPali: Efficient Document Retrieval with Vision Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=ogjBpZ8uSi)
- **作者**: Manuel Faysse, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, Céline Hudelot et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### TLDR: Token-Level Detective Reward Model for Large Vision Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=Zy2XgaGpDw)
- **作者**: Deqing Fu, Tong Xiao, Rui Wang, Wang Zhu, Pengchuan Zhang, Guan Pang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=rsZwwjYHuD)
- **作者**: Fushuo Huo, Wenchao Xu, Zhong Zhang, Haozhao Wang, Zhicheng Chen, Peilin Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### TEOChat: A Large Vision-Language Assistant for Temporal Earth Observation Data.
- **链接**: [出版页](https://openreview.net/forum?id=pZz0nOroGv)
- **作者**: Jeremy Andrew Irvin, Emily Ruoyu Liu, Joyce Chuyi Chen, Ines Dormoy, Jinyoung Kim, Samar Khanna et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model.
- **链接**: [出版页](https://openreview.net/forum?id=N5YTixK4F1)
- **作者**: Yatai Ji, Shilong Zhang, Jie Wu, Peize Sun, Weifeng Chen, Xuefeng Xiao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Reflexive Guidance: Improving OoDD in Vision-Language Models via Self-Guided Image-Adaptive Concept Generation.
- **链接**: [出版页](https://openreview.net/forum?id=R4h5PXzUuU)
- **作者**: Jihyo Kim, Seulbi Lee, Sangheum Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model.
- **链接**: [出版页](https://openreview.net/forum?id=s3FTX4Ay55)
- **作者**: Long Le, Jason Xie, William Liang, Hung-Ju Wang, Yue Yang, Yecheng Jason Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

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

- **摘要（英，原文）**:

  > Vision-language models (VLMs) have revolutionized machine learning by leveraging large pre-trained models to tackle various downstream tasks. Although label, training, and data efficiency have improved, many state-of-the-art VLMs still require task-specific hyperparameter tuning and fail to fully exploit test samples. To overcome these challenges, we propose a graph-based approach for label-efficient adaptation and inference. Our method dynamically constructs a graph over text prompts, few-shot examples, and test samples, using label propagation for inference without task-specific tuning. Unlike existing zero-shot label propagation techniques, our approach requires no additional unlabeled support set and effectively leverages the test sample manifold through dynamic graph expansion. We further introduce a context-aware feature re-weighting mechanism to improve task adaptation accuracy. Additionally, our method supports efficient graph expansion, enabling real-time inductive inference. Extensive evaluations on downstream tasks, such as fine-grained categorization and out-of-distribution generalization, demonstrate the effectiveness of our approach. The source code is available at https://github.com/Yushu-Li/ECALP.

### VLMaterial: Procedural Material Generation with Large Vision-Language Models.
- **链接**: [arXiv:2501.18623](https://arxiv.org/abs/2501.18623)
- **作者**: Beichen Li, Rundi Wu, Armando Solar-Lezama, Changxi Zheng, Liang Shi, Bernd Bickel et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

- **摘要（英，原文）**:

  > Procedural materials, represented as functional node graphs, are ubiquitous in computer graphics for photorealistic material appearance design. They allow users to perform intuitive and precise editing to achieve desired visual appearances. However, creating a procedural material given an input image requires professional knowledge and significant effort. In this work, we leverage the ability to convert procedural materials into standard Python programs and fine-tune a large pre-trained vision-language model (VLM) to generate such programs from input images. To enable effective fine-tuning, we also contribute an open-source procedural material dataset and propose to perform program-level augmentation by prompting another pre-trained large language model (LLM). Through extensive evaluation, we show that our method outperforms previous methods on both synthetic and real-world examples.

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
- **链接**: [出版页](https://openreview.net/forum?id=f7WBRSuf9l)
- **作者**: Ziyu Liu, Yuhang Zang, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Haodong Duan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Mixture of Experts Made Personalized: Federated Prompt Learning for Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=xiDJaTim3P)
- **作者**: Jun Luo, Chen Chen, Shandong Wu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Backdooring Vision-Language Models with Out-Of-Distribution Data.
- **链接**: [出版页](https://openreview.net/forum?id=tZozeR3VV7)
- **作者**: Weimin Lyu, Jiachen Yao, Saumya Gupta, Lu Pang, Tao Sun, Lingjie Yi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Vision Language Models are In-Context Value Learners.
- **链接**: [出版页](https://openreview.net/forum?id=friHAl5ofG)
- **作者**: Yecheng Jason Ma, Joey Hejna, Chuyuan Fu, Dhruv Shah, Jacky Liang, Zhuo Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset.
- **链接**: [出版页](https://openreview.net/forum?id=0y3hGn1wOk)
- **作者**: Yingzi Ma, Jiongxiao Wang, Fei Wang, Siyuan Ma, Jiazhao Li, Jinsheng Pan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Towards Interpreting Visual Information Processing in Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=chanJGoa7f)
- **作者**: Clement Neo, Luke Ong, Philip Torr, Mor Geva, David Krueger, Fazl Barez
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Compositional Entailment Learning for Hyperbolic Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=3i13Gev2hV)
- **作者**: Avik Pal, Max van Spengler, Guido Maria D'Amely di Melendugno, Alessandro Flaborea, Fabio Galasso, Pascal Mettes
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### ZIP: An Efficient Zeroth-order Prompt Tuning for Black-box Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=2OegVbwvY2)
- **作者**: Seonghwan Park, Jaehyeon Jeong, Yongjun Kim, Jaeho Lee, Namhoon Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

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
- **链接**: [出版页](https://openreview.net/forum?id=VxvnV6slP0)
- **作者**: Longrong Yang, Dong Shen, Chaoxiang Cai, Fan Yang, Tingting Gao, Di Zhang et al.
- **🏷️ 机构**: ZJU
- **会议**: ICLR 2025

### Do Vision-Language Models Represent Space and How? Evaluating Spatial Frame of Reference under Ambiguities.
- **链接**: [arXiv:2410.17385](https://arxiv.org/abs/2410.17385)
- **作者**: Zheyuan Zhang, Fengyuan Hu, Jayjun Lee, Freda Shi, Parisa Kordjamshidi, Joyce Chai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

- **摘要（英，原文）**:

  > Spatial expressions in situated communication can be ambiguous, as their meanings vary depending on the frames of reference (FoR) adopted by speakers and listeners. While spatial language understanding and reasoning by vision-language models (VLMs) have gained increasing attention, potential ambiguities in these models are still under-explored. To address this issue, we present the COnsistent Multilingual Frame Of Reference Test (COMFORT), an evaluation protocol to systematically assess the spatial reasoning capabilities of VLMs. We evaluate nine state-of-the-art VLMs using COMFORT. Despite showing some alignment with English conventions in resolving ambiguities, our experiments reveal significant shortcomings of VLMs: notably, the models (1) exhibit poor robustness and consistency, (2) lack the flexibility to accommodate multiple FoRs, and (3) fail to adhere to language-specific or culture-specific conventions in cross-lingual tests, as English tends to dominate other languages. With a growing effort to align vision-language models with human cognitive intuitions, we call for more attention to the ambiguous nature and cross-cultural diversity of spatial reasoning.

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

- **摘要（英，原文）**:

  > Visual navigation is an essential skill for home-assistance robots, providing the object-searching ability to accomplish long-horizon daily tasks. Many recent approaches use Large Language Models (LLMs) for commonsense inference to improve exploration efficiency. However, the planning process of LLMs is limited within texts and it is difficult to represent the spatial occupancy and geometry layout only by texts. Both are important for making rational navigation decisions. In this work, we seek to unleash the spatial perception and planning ability of Vision-Language Models (VLMs), and explore whether the VLM, with only on-board camera captured RGB/RGB-D stream inputs, can efficiently finish the visual navigation tasks in a mapless manner. We achieve this by developing the imagination-powered navigation framework ImagineNav, which imagines the future observation images at valuable robot views and translates the complex navigation planning process into a rather simple best-view image selection problem for VLM. To generate appropriate candidate robot views for imagination, we introduce the Where2Imagine module, which is distilled to align with human navigation habits. Finally, to reach the VLM preferred views, an off-the-shelf point-goal navigation policy is utilized. Empirical experiments on the challenging open-vocabulary object navigation benchmarks demonstrates the superiority of our proposed system.

### BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks.
- **链接**: [出版页](https://openreview.net/forum?id=wwVGZRnAYG)
- **作者**: Yunhan Zhao, Xiang Zheng, Lin Luo, Yige Li, Xingjun Ma, Yu-Gang Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### DenseGrounding: Improving Dense Language-Vision Semantics for Ego-centric 3D Visual Grounding.
- **链接**: [出版页](https://openreview.net/forum?id=iGafR0hSln)
- **作者**: Henry Zheng, Hao Shi, Qihang Peng, Yong Xien Chng, Rui Huang, Yepeng Weng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

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
- Duoduo CLIP: Efficient 3D Understanding with Multi-View Images. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Open-Vocabulary Customization from CLIP via Data-Free Knowledge Distillation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification. → [multimodal](../multimodal/Guideline%202025.md)
- MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks. → [multimodal](../multimodal/Guideline%202025.md)
- C-CLIP: Multimodal Continual Learning for Vision-Language Model. → [continual-learning](../continual-learning/Guideline%202025.md)
- MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration. → [network-pruning](../network-pruning/Guideline%202025.md)
- Cross-Modal Safety Mechanism Transfer in Large Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
