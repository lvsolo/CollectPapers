# VLM — 2025 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 120 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MMCSBench: A Fine-Grained Benchmark for Large Vision-Language Models in Camouflage Scenes.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/2c09ffac15c54c56bde4db13acfef196-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Jing Zhang, Ruiheng Zhang, Zhe Cao, Kaizheng Chen
- **🏷️ 机构**: Beijing Institute of Technology
- **会议**: NeurIPS 2025

### DualCnst: Enhancing Zero-Shot Out-of-Distribution Detection via Text-Image Consistency in Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e2ee3cb9742aa92f2780d9e27649d270-Abstract-Conference.html) · 📚 被引 0
- **作者**: Fayi Le, Wenwu He, Chentao Cao, Dong Liang, Zhuo-Xu Cui
- **🏷️ 机构**: Fujian University of Technology, Hong Kong Baptist University, Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a7bfdee9544cea324cf183ac03c7d5c0-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jialiang Kang, Han Shu, Wenshuo Li, Yingjie Zhai, Xinghao Chen
- **🏷️ 机构**: Peking University, Huawei Noah's Ark Lab, Huawei Technologies Ltd.
- **会议**: NeurIPS 2025

### VisionThink: Smart and Efficient Vision Language Model via Reinforcement Learning.
- **链接**: [arXiv:2507.13348](https://arxiv.org/abs/2507.13348) · [代码](https://github.com/dvlab-research/VisionThink) · 📚 被引 0
- **作者**: Senqiao Yang, Junyi Li, Xin Lai, Jinming Wu, Wei Li, Zejun Ma et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, The University of Hong Kong, Southwest Jiaotong University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in vision-language models (VLMs) have improved performance by increasing the number of visual tokens, which are often significantly longer than text tokens. However, we observe that most real-world scenarios do not require such an extensive number of visual tokens. While the performance drops significantly in a small subset of OCR-related tasks, models still perform accurately in most other general VQA tasks with only 1/4 resolution. Therefore, we propose to dynamically process distinct samples with different resolutions, and present a new paradigm for visual token compression, namely, VisionThink. It starts with a downsampled image and smartly decides whether it is sufficient for problem solving. Otherwise, the model could output a special token to request the higher-resolution image. Compared to existing Efficient VLM methods that compress tokens using fixed pruning ratios or thresholds, VisionThink autonomously decides whether to compress tokens case by case. As a result, it demonstrates strong fine-grained visual understanding capability on OCR-related tasks, and meanwhile saves substantial visual tokens on simpler tasks. We adopt reinforcement learning and propose the LLM-as-Judge strategy to successfully apply RL to general VQA tasks. Moreover, we carefully design a reward function and penalty mechanism to achieve a stable and reasonable image resize call ratio. Extensive experiments demonstrate the superiority, efficiency, and effectiveness of our method. Our code is available at https://github.com/dvlab-research/VisionThink.

</details>

### MolVision: Molecular Property Prediction with Vision Language Models.
- **链接**: [arXiv:2507.03283](https://arxiv.org/abs/2507.03283) · 📚 被引 0
- **作者**: Deepan Adak, Yogesh S. Rawat, Shruti Vyas
- **🏷️ 机构**: National Institute of Technology Kurukshetra, University of Central Florida
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Molecular property prediction is a fundamental task in computational chemistry with critical applications in drug discovery and materials science. While recent works have explored Large Language Models (LLMs) for this task, they primarily rely on textual molecular representations such as SMILES/SELFIES, which can be ambiguous and structurally less informative. In this work, we introduce MolVision, a novel approach that leverages Vision-Language Models (VLMs) by integrating both molecular structure as images and textual descriptions to enhance property prediction. We construct a benchmark spanning ten diverse datasets, covering classification, regression and description tasks. Evaluating nine different VLMs in zero-shot, few-shot, and fine-tuned settings, we find that visual information improves prediction performance, particularly when combined with efficient fine-tuning strategies such as LoRA. Our results reveal that while visual information alone is insufficient, multimodal fusion significantly enhances generalization across molecular properties. Adaptation of vision encoder for molecular images in conjunction with LoRA further improves the performance. The code and data is available at : $\href{https://molvision.github.io/MolVision/}{https://molvision.github.io/MolVision/}$.

</details>

### CHOICE: Benchmarking the Remote Sensing Capabilities of Large Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/befe25a01cf4dbe9635e85f835d31250-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Xiao An, Jiaxing Sun, Zihan Gui, Wei He
- **🏷️ 机构**: Wuhan University, Shanghai Artificial Intelligence Laboratory
- **会议**: NeurIPS 2025

### Scaffolding Dexterous Manipulation with Vision-Language Models.
- **链接**: [arXiv:2506.19212](https://arxiv.org/abs/2506.19212) · 📚 被引 0
- **作者**: Vincent de Bakker, Joey Hejna, Tyler Ga Wei Lum, Onur Celik, Aleksandar Taranovic, Denis Blessing et al.
- **🏷️ 机构**: Karlsruher Institut für Technologie, Stanford University, Stanford University, Computer Science Department, Stanford University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control. While reinforcement learning (RL) can alleviate the data bottleneck by generating experience in simulation, it typically relies on carefully designed, task-specific reward functions, which hinder scalability and generalization. Thus, contemporary works in dexterous manipulation have often bootstrapped from reference trajectories. These trajectories specify target hand poses that guide the exploration of RL policies and object poses that enable dense, task-agnostic rewards. However, sourcing suitable trajectories - particularly for dexterous hands - remains a significant challenge. Yet, the precise details in explicit reference trajectories are often unnecessary, as RL ultimately refines the motion. Our key insight is that modern vision-language models (VLMs) already encode the commonsense spatial and semantic knowledge needed to specify tasks and guide exploration effectively. Given a task description (e.g., "open the cabinet") and a visual scene, our method uses an off-the-shelf VLM to first identify task-relevant keypoints (e.g., handles, buttons) and then synthesize 3D trajectories for hand motion and object motion. Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or "scaffolds" with high fidelity. Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies. Moreover, we showcase that our method transfers to real-world robotic hands without any human demonstrations or handcrafted rewards.

</details>

### Mint: A Simple Test-Time Adaptation of Vision-Language Models against Common Corruptions.
- **链接**: [arXiv:2510.22127](https://arxiv.org/abs/2510.22127) · [代码](https://github.com/baowenxuan/Mint) · 📚 被引 0
- **作者**: Wenxuan Bao, Ruxi Deng, Jingrui He
- **🏷️ 机构**: VISA, University of Illinois Urbana-Champaign, University of Illinois at Urbana-Champaign
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pretrained vision-language models such as CLIP achieve strong zero-shot generalization but remain vulnerable to distribution shifts caused by input corruptions. In this work, we investigate how corruptions affect CLIP's image embeddings and uncover a consistent phenomenon we term as embedding variance collapse, where both intra-class and inter-class variances shrink as corruption severity increases. We find that this collapse is closely tied to performance degradation, with inter-class variance strongly correlated with classification accuracy. To explain this phenomenon, we analyze how corruptions alter the structure of the embedding space. Our theoretical results suggest that the visual encoder tends to encode corruption-related signals, which dilute class-discriminative features and compress the representation geometry. We further show that maximizing inter-class variance, even when estimated from pseudo-labels, can provably enhance embedding quality. Based on this insight, we propose Mint, a simple test-time adaptation method that maximizes pseudo-label-based inter-class variance on the fly using a mean accumulator and a gradient accumulator. Mint operates effectively with small batch sizes and consistently improves performance across multiple corruption benchmarks and CLIP architectures. Our code is available at https://github.com/baowenxuan/Mint .

</details>

### Towards Building Model/Prompt-Transferable Attackers against Large Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/fe5e73e8817e3b4d4d0a2b9a7396495f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xiaowen Cai, Daizong Liu, Xiaoye Qu, Xiang Fang, Jianfeng Dong, Keke Tang et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Wuhan University, Shanghai Artificial Intelligence Laboratory
- **会议**: NeurIPS 2025

### SD-VLM: Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models.
- **链接**: [arXiv:2509.17664](https://arxiv.org/abs/2509.17664) · [代码](https://github.com/cpystan/SD-VLM) · 📚 被引 0
- **作者**: Pingyi Chen, Yujing Lou, Shen Cao, Jinhui Guo, Lubin Fan, Yue Wu et al.
- **🏷️ 机构**: Westlake University, Alibaba Cloud Computing, Alibaba
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While vision language models (VLMs) excel in 2D semantic visual understanding, their ability to quantitatively reason about 3D spatial relationships remains under-explored, due to the deficiency of 2D images' spatial representation ability. In this paper, we analyze the problem hindering VLMs' spatial understanding abilities and propose SD-VLM, a novel framework that significantly enhances fundamental spatial perception abilities of VLMs through two key contributions: (1) propose Massive Spatial Measuring and Understanding (MSMU) dataset with precise spatial annotations, and (2) introduce a simple depth positional encoding method strengthening VLMs' spatial awareness. MSMU dataset covers massive quantitative spatial tasks with 700K QA pairs, 2.5M physical numerical annotations, and 10K chain-of-thought augmented samples. We have trained SD-VLM, a strong generalist VLM which shows superior quantitative spatial measuring and understanding capability. SD-VLM not only achieves state-of-the-art performance on our proposed MSMU-Bench, but also shows spatial generalization abilities on other spatial understanding benchmarks including Q-Spatial and SpatialRGPT-Bench. Extensive experiments demonstrate that SD-VLM outperforms GPT-4o and Intern-VL3-78B by 26.91% and 25.56% respectively on MSMU-Bench. Code and models are released at https://github.com/cpystan/SD-VLM.

</details>

### Unveiling Chain of Step Reasoning for Vision-Language Models with Fine-grained Rewards.
- **链接**: [arXiv:2509.19003](https://arxiv.org/abs/2509.19003) · [代码](https://github.com/baaivision/CoS) · 📚 被引 0
- **作者**: Honghao Chen, Xingzhou Lou, Xiaokun Feng, Kaiqi Huang, Xinlong Wang
- **🏷️ 机构**: Institute of automation, Chinese academy of science, Chinese Academy of Sciences, CASIA, , Institute of automation, Chinese academy of science
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Chain of thought reasoning has demonstrated remarkable success in large language models, yet its adaptation to vision-language reasoning remains an open challenge with unclear best practices. Existing attempts typically employ reasoning chains at a coarse-grained level, which struggles to perform fine-grained structured reasoning and, more importantly, are difficult to evaluate the reward and quality of intermediate reasoning. In this work, we delve into chain of step reasoning for vision-language models, enabling assessing reasoning step quality accurately and leading to effective reinforcement learning and inference-time scaling with fine-grained rewards. We present a simple, effective, and fully transparent framework, including the step-level reasoning data, process reward model (PRM), and reinforcement learning training. With the proposed approaches, our models set strong baselines with consistent improvements on challenging vision-language benchmarks. More importantly, we conduct a thorough empirical analysis and ablation study, unveiling the impact of each component and several intriguing properties of inference-time scaling. We believe this paper serves as a baseline for vision-language models and offers insights into more complex multimodal reasoning. Our dataset, PRM, and code will be available at https://github.com/baaivision/CoS.

</details>

### Eagle 2.5: Boosting Long-Context Post-Training for Frontier Vision-Language Models.
- **链接**: [arXiv:2504.15271](https://arxiv.org/abs/2504.15271) · 📚 被引 1
- **作者**: Guo Chen, Zhiqi Li, Shihao Wang, Jindong Jiang, Yicheng Liu, Lidong Lu et al.
- **🏷️ 机构**: Nanjing University, NVIDIA, Hong Kong Polytechnic University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Eagle 2.5, a family of frontier vision-language models (VLMs) for long-context multimodal learning. Our work addresses the challenges in long video comprehension and high-resolution image understanding, introducing a generalist framework for both tasks. The proposed training framework incorporates Automatic Degrade Sampling and Image Area Preservation, two techniques that preserve contextual integrity and visual details. The framework also includes numerous efficiency optimizations in the pipeline for long-context data training. Finally, we propose Eagle-Video-110K, a novel dataset that integrates both story-level and clip-level annotations, facilitating long-video understanding. Eagle 2.5 demonstrates substantial improvements on long-context multimodal benchmarks, providing a robust solution to the limitations of existing VLMs. Notably, our best model Eagle 2.5-8B achieves 72.4% on Video-MME with 512 input frames, matching the results of top-tier commercial model such as GPT-4o and large-scale open-source models like Qwen2.5-VL-72B and InternVL2.5-78B.

</details>

### Safe + Safe = Unsafe? Exploring How Safe Images Can Be Exploited to Jailbreak Large Vision-Language Models.
- **链接**: [arXiv:2411.11496](https://arxiv.org/abs/2411.11496) · [代码](https://github.com/gzcch/Safety_Snowball_Agent) · 📚 被引 0
- **作者**: Chenhang Cui, Gelei Deng, An Zhang, Jingnan Zheng, Yicong Li, Lianli Gao et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, Nanyang Technological University, University of Science and Technology of China
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in Large Vision-Language Models (LVLMs) have showcased strong reasoning abilities across multiple modalities, achieving significant breakthroughs in various real-world applications. Despite this great success, the safety guardrail of LVLMs may not cover the unforeseen domains introduced by the visual modality. Existing studies primarily focus on eliciting LVLMs to generate harmful responses via carefully crafted image-based jailbreaks designed to bypass alignment defenses. In this study, we reveal that a safe image can be exploited to achieve the same jailbreak consequence when combined with additional safe images and prompts. This stems from two fundamental properties of LVLMs: universal reasoning capabilities and safety snowball effect. Building on these insights, we propose Safety Snowball Agent (SSA), a novel agent-based framework leveraging agents' autonomous and tool-using abilities to jailbreak LVLMs. SSA operates through two principal stages: (1) initial response generation, where tools generate or retrieve jailbreak images based on potential harmful intents, and (2) harmful snowballing, where refined subsequent prompts induce progressively harmful outputs. Our experiments demonstrate that \ours can use nearly any image to induce LVLMs to produce unsafe content, achieving high success jailbreaking rates against the latest LVLMs. Unlike prior works that exploit alignment flaws, \ours leverages the inherent properties of LVLMs, presenting a profound challenge for enforcing safety in generative multimodal systems. Our code is avaliable at \url{https://github.com/gzcch/Safety_Snowball_Agent}.

</details>

### Test-Time Spectrum-Aware Latent Steering for Zero-Shot Generalization in Vision-Language Models.
- **链接**: [arXiv:2511.09809](https://arxiv.org/abs/2511.09809) · [代码](https://github.com/kdafnis/STS) · 📚 被引 0
- **作者**: Konstantinos M. Dafnis, Dimitris N. Metaxas
- **🏷️ 机构**: Rutgers University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) excel at zero-shot inference but often degrade under test-time domain shifts. For this reason, episodic test-time adaptation strategies have recently emerged as powerful techniques for adapting VLMs to a single unlabeled image. However, existing adaptation strategies, such as test-time prompt tuning, typically require backpropagating through large encoder weights or altering core model components. In this work, we introduce Spectrum-Aware Test-Time Steering (STS), a lightweight adaptation framework that extracts a spectral subspace from the textual embeddings to define principal semantic directions and learns to steer latent representations in a spectrum-aware manner by adapting a small number of per-sample shift parameters to minimize entropy across augmented views. STS operates entirely at inference in the latent space, without backpropagation through or modification of the frozen encoders. Building on standard evaluation protocols, our comprehensive experiments demonstrate that STS largely surpasses or compares favorably against state-of-the-art test-time adaptation methods, while introducing only a handful of additional parameters and achieving inference speeds up to 8x faster with a 12x smaller memory footprint than conventional test-time prompt tuning. The code is available at https://github.com/kdafnis/STS.

</details>

### Towards Self-Refinement of Vision-Language Models with Triangular Consistency.
- **链接**: [arXiv:2510.10487](https://arxiv.org/abs/2510.10487) · [代码](https://github.com/dengyl20/SRF-LLaVA-1.5) · 📚 被引 0
- **作者**: Yunlong Deng, Guangyi Chen, Tianpei Gu, Lingjing Kong, Yan Li, Zeyu Tang et al.
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence, MBZUAI&amp;CMU, ByteDance Inc.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) integrate visual knowledge with the analytical capabilities of Large Language Models (LLMs) through supervised visual instruction tuning, using image-question-answer triplets. However, the potential of VLMs trained without supervised instruction remains largely unexplored. This study validates that VLMs possess inherent self-refinement capabilities, enabling them to generate high-quality supervised data without external inputs and thereby learn autonomously. Specifically, to stimulate the self-refinement ability of VLMs, we propose a self-refinement framework based on a Triangular Consistency principle: within the image-query-answer triangle, any masked elements should be consistently and accurately reconstructed. The framework involves three steps: (1) We enable the instruction generation ability of VLMs by adding multi-task instruction tuning like image$\rightarrow$question-answer or image-answer$\rightarrow$question. (2) We generate image-query-answer triplets from unlabeled images and use the Triangular Consistency principle for filtering. (3) The model is further updated using the filtered synthetic data. To investigate the underlying mechanisms behind this self-refinement capability, we conduct a theoretical analysis from a causal perspective. Using the widely recognized LLaVA-1.5 as our baseline, our experiments reveal that the model can autonomously achieve consistent, though deliberately modest, improvements across multiple benchmarks without any external supervision, such as human annotations or environmental feedback. We expect that the insights of this study on the self-refinement ability of VLMs can inspire future research on the learning mechanism of VLMs. Code is available at https://github.com/dengyl20/SRF-LLaVA-1.5.

</details>

### Sherlock: Self-Correcting Reasoning in Vision-Language Models.
- **链接**: [arXiv:2505.22651](https://arxiv.org/abs/2505.22651) · 📚 被引 0
- **作者**: Yi Ding, Ruqi Zhang
- **🏷️ 机构**: Nanyang Technological University, Purdue University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reasoning Vision-Language Models (VLMs) have shown promising performance on complex multimodal tasks. However, they still face significant challenges: they are highly sensitive to reasoning errors, require large volumes of annotated data or accurate verifiers, and struggle to generalize beyond specific domains. To address these limitations, we explore self-correction as a strategy to enhance reasoning VLMs. We first conduct an in-depth analysis of reasoning VLMs' self-correction abilities and identify key gaps. Based on our findings, we introduce Sherlock, a self-correction and self-improvement training framework. Sherlock introduces a trajectory-level self-correction objective, a preference data construction method based on visual perturbation, and a dynamic $β$ for preference tuning. Once the model acquires self-correction capabilities using only 20k randomly sampled annotated data, it continues to self-improve without external supervision. Built on the Llama3.2-Vision-11B model, Sherlock achieves remarkable results across eight benchmarks, reaching an average accuracy of 64.1 with direct generation and 65.4 after self-correction. It outperforms LLaVA-CoT (63.2), Mulberry (63.9), and LlamaV-o1 (63.4) while using less than 20% of the annotated data.

</details>

### Robust SuperAlignment: Weak-to-Strong Robustness Generalization for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1a87980b9853e84dfb295855b425c262-Abstract-Conference.html) · 📚 被引 1
- **作者**: Junhao Dong, Cong Zhang, Xinghua Qu, Zejun Ma, Piotr Koniusz, Yew Soon Ong
- **🏷️ 机构**: Nanyang Technological University / CFAR, A*STAR, Nanyang Technological University, Bytedance AI Lab
- **会议**: NeurIPS 2025

### Hierarchical Semantic-Augmented Navigation: Optimal Transport and Graph-Driven Reasoning for Vision-Language Navigation.
- **链接**: [arXiv:2606.01565](https://arxiv.org/abs/2606.01565) · 📚 被引 0
- **作者**: Xiang Fang, Wanlong Fang, Changshuo Wang
- **🏷️ 机构**: Huazhong University of Science and Technology, Nanyang Technological University, University College London, University of London
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation in Continuous Environments (VLN-CE) poses a formidable challenge for autonomous agents, requiring seamless integration of natural language instructions and visual observations to navigate complex 3D indoor spaces. Existing approaches often falter in long-horizon tasks due to limited scene understanding, inefficient planning, and lack of robust decision-making frameworks. We introduce the \textbf{Hierarchical Semantic-Augmented Navigation (HSAN)} framework, a groundbreaking approach that redefines VLN-CE through three synergistic innovations. First, HSAN constructs a dynamic hierarchical semantic scene graph, leveraging vision-language models to capture multi-level environmental representations, from objects to regions to zones, enabling nuanced spatial reasoning. Second, it employs an optimal transport-based topological planner, grounded in Kantorovich's duality, to select long-term goals by balancing semantic relevance and spatial accessibility with theoretical guarantees of optimality. Third, a graph-aware reinforcement learning policy ensures precise low-level control, navigating subgoals while robustly avoiding obstacles. By integrating spectral graph theory, optimal transport, and advanced multi-modal learning, HSAN addresses the shortcomings of static maps and heuristic planners prevalent in prior work. Extensive experiments on multiple challenging VLN-CE datasets demonstrate that HSAN achieves state-of-the-art performance, with significant improvements in navigation success and generalization to unseen environments.

</details>

### Enhancing Vision-Language Model Reliability with Uncertainty-Guided Dropout Decoding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/db48d94a42706019262ed8304fa658c5-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yixiong Fang, Ziran Yang, Zhaorun Chen, Zhuokai Zhao, Jiawei Zhou
- **🏷️ 机构**: Carnegie Mellon University, Princeton University, University of Chicago
- **会议**: NeurIPS 2025

### Statistics Caching Test-Time Adaptation for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/09eadc995e2a0293f1bc622a3e68fb18-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zenghao Guan, Yucan Zhou, Wu Liu, Xiaoyan Gu
- **🏷️ 机构**: Institute of Information Engineering，Chinese Academy of Sciences, Tianjin University, JD Explore Academy
- **会议**: NeurIPS 2025

### Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging.
- **链接**: [arXiv:2510.20639](https://arxiv.org/abs/2510.20639) · [代码](https://github.com/ibrahimethemhamamci/BTB3D) · 📚 被引 0
- **作者**: Ibrahim Ethem Hamamci, Sezgin Er, Suprosanna Shit, Hadrien Reynaud, Dong Yang, Pengfei Guo et al.
- **🏷️ 机构**: University of Zurich, Istanbul Medipol University, TUM
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in vision-language modeling for 3D medical imaging has been fueled by large-scale computed tomography (CT) corpora with paired free-text reports, stronger architectures, and powerful pretrained models. This has enabled applications such as automated report generation and text-conditioned 3D image synthesis. Yet, current approaches struggle with high-resolution, long-sequence volumes: contrastive pretraining often yields vision encoders that are misaligned with clinical language, and slice-wise tokenization blurs fine anatomy, reducing diagnostic performance on downstream tasks. We introduce BTB3D (Better Tokens for Better 3D), a causal convolutional encoder-decoder that unifies 2D and 3D training and inference while producing compact, frequency-aware volumetric tokens. A three-stage training curriculum enables (i) local reconstruction, (ii) overlapping-window tiling, and (iii) long-context decoder refinement, during which the model learns from short slice excerpts yet generalizes to scans exceeding 300 slices without additional memory overhead. BTB3D sets a new state-of-the-art on two key tasks: it improves BLEU scores and increases clinical F1 by 40% over CT2Rep, CT-CHAT, and Merlin for report generation; and it reduces FID by 75% and halves FVD compared to GenerateCT and MedSyn for text-to-CT synthesis, producing anatomically consistent 512*512*241 volumes. These results confirm that precise three-dimensional tokenization, rather than larger language backbones alone, is essential for scalable vision-language modeling in 3D medical imaging. The codebase is available at: https://github.com/ibrahimethemhamamci/BTB3D

</details>

### DOTA: Distributional Test-time Adaptation of Vision-Language Models.
- **链接**: [arXiv:2409.19375](https://arxiv.org/abs/2409.19375) · 📚 被引 1
- **作者**: Zongbo Han, Jialong Yang, Guangyu Wang, Junfan Li, Qianli Xu, Mike Zheng Shou et al.
- **🏷️ 机构**: Tianjin University, Beijing University of Posts and Telecommunications, Harbin Institute of Technology Shenzhen
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language foundation models (VLMs), such as CLIP, exhibit remarkable performance across a wide range of tasks. However, deploying these models can be unreliable when significant distribution gaps exist between training and test data, while fine-tuning for diverse scenarios is often costly. Cache-based test-time adapters offer an efficient alternative by storing representative test samples to guide subsequent classifications. Yet, these methods typically employ naive cache management with limited capacity, leading to severe catastrophic forgetting when samples are inevitably dropped during updates. In this paper, we propose DOTA (DistributiOnal Test-time Adaptation), a simple yet effective method addressing this limitation. Crucially, instead of merely memorizing individual test samples, DOTA continuously estimates the underlying distribution of the test data stream. Test-time posterior probabilities are then computed using these dynamically estimated distributions via Bayes' theorem for adaptation. This distribution-centric approach enables the model to continually learn and adapt to the deployment environment. Extensive experiments validate that DOTA significantly mitigates forgetting and achieves state-of-the-art performance compared to existing methods.

</details>

### FineGRAIN: Evaluating Failure Modes of Text-to-Image Models with Vision Language Model Judges.
- **链接**: [arXiv:2512.02161](https://arxiv.org/abs/2512.02161) · 📚 被引 0
- **作者**: Kevin David Hayes, Micah Goldblum, Vikash Sehwag, Gowthami Somepalli, Ashwinee Panda, Tom Goldstein
- **🏷️ 机构**: University of Maryland, Columbia University, Princeton University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-to-image (T2I) models are capable of generating visually impressive images, yet they often fail to accurately capture specific attributes in user prompts, such as the correct number of objects with the specified colors. The diversity of such errors underscores the need for a hierarchical evaluation framework that can compare prompt adherence abilities of different image generation models. Simultaneously, benchmarks of vision language models (VLMs) have not kept pace with the complexity of scenes that VLMs are used to annotate. In this work, we propose a structured methodology for jointly evaluating T2I models and VLMs by testing whether VLMs can identify 27 specific failure modes in the images generated by T2I models conditioned on challenging prompts. Our second contribution is a dataset of prompts and images generated by 5 T2I models (Flux, SD3-Medium, SD3-Large, SD3.5-Medium, SD3.5-Large) and the corresponding annotations from VLMs (Molmo, InternVL3, Pixtral) annotated by an LLM (Llama3) to test whether VLMs correctly identify the failure mode in a generated image. By analyzing failure modes on a curated set of prompts, we reveal systematic errors in attribute fidelity and object representation. Our findings suggest that current metrics are insufficient to capture these nuanced errors, highlighting the importance of targeted benchmarks for advancing generative model reliability and interpretability.

</details>

### TaiwanVQA: Benchmarking and Enhancing Cultural Understanding in Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1c27e0352b819d61fbd6b65eef125b23-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Hsin-Yi Hsieh, Shang-Wei Liu, Chang-Chih Meng, Chien-Hua Chen, Shuo-Yueh Lin, Hung-Ju Lin et al.
- **🏷️ 机构**: Academia Sinica, National Yang Ming Chiao Tung University, National Central University
- **会议**: NeurIPS 2025

### HMVLM: Human Motion-Vision-Language Model via MoE LoRA.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/8cb564df771e9eacbfe9d72bd46a24a9-Abstract-Conference.html)
- **作者**: Lei Hu, Yongjing Ye, Shihong Xia
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### MM-OPERA: Benchmarking Open-ended Association Reasoning for Large Vision-Language Models.
- **链接**: [arXiv:2510.26937](https://arxiv.org/abs/2510.26937) · [代码](https://github.com/MM-OPERA-Bench/MM-OPERA) · 📚 被引 0
- **作者**: Zimeng Huang, Jinxin Ke, Xiaoxuan Fan, Yufeng Yang, Yang Liu, Liu Zhonghan et al.
- **🏷️ 机构**: Sun Yat-sen University, SUN YAT-SEN UNIVERSITY, Jinan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) have exhibited remarkable progress. However, deficiencies remain compared to human intelligence, such as hallucination and shallow pattern matching. In this work, we aim to evaluate a fundamental yet underexplored intelligence: association, a cornerstone of human cognition for creative thinking and knowledge integration. Current benchmarks, often limited to closed-ended tasks, fail to capture the complexity of open-ended association reasoning vital for real-world applications. To address this, we present MM-OPERA, a systematic benchmark with 11,497 instances across two open-ended tasks: Remote-Item Association (RIA) and In-Context Association (ICA), aligning association intelligence evaluation with human psychometric principles. It challenges LVLMs to resemble the spirit of divergent thinking and convergent associative reasoning through free-form responses and explicit reasoning paths. We deploy tailored LLM-as-a-Judge strategies to evaluate open-ended outputs, applying process-reward-informed judgment to dissect reasoning with precision. Extensive empirical studies on state-of-the-art LVLMs, including sensitivity analysis of task instances, validity analysis of LLM-as-a-Judge strategies, and diversity analysis across abilities, domains, languages, cultures, etc., provide a comprehensive and nuanced understanding of the limitations of current LVLMs in associative reasoning, paving the way for more human-like and general-purpose AI. The dataset and code are available at https://github.com/MM-OPERA-Bench/MM-OPERA.

</details>

### Approximate Domain Unlearning for Vision-Language Models.
- **链接**: [arXiv:2510.08132](https://arxiv.org/abs/2510.08132) · 📚 被引 0
- **作者**: Kodai Kawamura, Yuta Goto, Rintaro Yanagi, Hirokatsu Kataoka, Go Irie
- **🏷️ 机构**: National University of Singapore, Tokyo University of Science, AIST, National Institute of Advanced Industrial Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained Vision-Language Models (VLMs) exhibit strong generalization capabilities, enabling them to recognize a wide range of objects across diverse domains without additional training. However, they often retain irrelevant information beyond the requirements of specific downstream tasks, raising concerns about computational efficiency and potential information leakage. This has motivated growing interest in approximate unlearning, which aims to selectively remove unnecessary knowledge while preserving overall model performance. Existing approaches to approximate unlearning have primarily focused on class unlearning, where a VLM is retrained to fail to recognize specified object classes while maintaining accuracy for others. However, merely forgetting object classes is often insufficient in practical applications. For instance, an autonomous driving system should accurately recognize real cars while avoiding misrecognition of illustrated cars depicted in roadside advertisements as real cars, which could be hazardous. In this paper, we introduce Approximate Domain Unlearning (ADU), a novel problem setting that requires reducing recognition accuracy for images from specified domains (e.g., illustration) while preserving accuracy for other domains (e.g., real). ADU presents new technical challenges: due to the strong domain generalization capability of pre-trained VLMs, domain distributions are highly entangled in the feature space, making naive approaches based on penalizing target domains ineffective. To tackle this limitation, we propose a novel approach that explicitly disentangles domain distributions and adaptively captures instance-specific domain information. Extensive experiments show that our approach outperforms baselines built upon VLM tuning techniques, paving the way for practical and fine-grained unlearning in VLMs. Code: https://kodaikawamura.github.io/Domain_Unlearning/.

</details>

### Active Test-time Vision-Language Navigation.
- **链接**: [arXiv:2506.06630](https://arxiv.org/abs/2506.06630) · 📚 被引 0
- **作者**: Heeju Ko, Sung June Kim, Gyeongrok Oh, Jeongyoon Yoon, Honglak Lee, Sujin Jang et al.
- **🏷️ 机构**: Korea University, Korea university, LG AI Research / U. Michigan
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation (VLN) policies trained on offline datasets often exhibit degraded task performance when deployed in unfamiliar navigation environments at test time, where agents are typically evaluated without access to external interaction or feedback. Entropy minimization has emerged as a practical solution for reducing prediction uncertainty at test time; however, it can suffer from accumulated errors, as agents may become overconfident in incorrect actions without sufficient contextual grounding. To tackle these challenges, we introduce ATENA (Active TEst-time Navigation Agent), a test-time active learning framework that enables a practical human-robot interaction via episodic feedback on uncertain navigation outcomes. In particular, ATENA learns to increase certainty in successful episodes and decrease it in failed ones, improving uncertainty calibration. Here, we propose mixture entropy optimization, where entropy is obtained from a combination of the action and pseudo-expert distributions-a hypothetical action distribution assuming the agent's selected action to be optimal-controlling both prediction confidence and action preference. In addition, we propose a self-active learning strategy that enables an agent to evaluate its navigation outcomes based on confident predictions. As a result, the agent stays actively engaged throughout all iterations, leading to well-grounded and adaptive decision-making. Extensive evaluations on challenging VLN benchmarks-REVERIE, R2R, and R2R-CE-demonstrate that ATENA successfully overcomes distributional shifts at test time, outperforming the compared baseline methods across various settings.

</details>

### CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation.
- **链接**: [arXiv:2507.14312](https://arxiv.org/abs/2507.14312) · 📚 被引 0
- **作者**: Marc Lafon, Gustavo Adolfo Vargas Hakim, Clément Rambour, Christian Desrosiers, Nicolas Thome
- **🏷️ 机构**: Sorbonne Université - ISIR, École de technologie supérieure, Université du Québec, Sorbonne Université - Faculté des Sciences (Paris VI)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) like CLIP exhibit strong zero-shot capabilities but often fail to generalize under distribution shifts. Test-time adaptation (TTA) allows models to update at inference time without labeled data, typically via entropy minimization. However, this objective is fundamentally misaligned with the contrastive image-text training of VLMs, limiting adaptation performance and introducing failure modes such as pseudo-label drift and class collapse. We propose CLIPTTA, a new gradient-based TTA method for vision-language models that leverages a soft contrastive loss aligned with CLIP's pre-training objective. We provide a theoretical analysis of CLIPTTA's gradients, showing how its batch-aware design mitigates the risk of collapse. We further extend CLIPTTA to the open-set setting, where both in-distribution (ID) and out-of-distribution (OOD) samples are encountered, using an Outlier Contrastive Exposure (OCE) loss to improve OOD detection. Evaluated on 75 datasets spanning diverse distribution shifts, CLIPTTA consistently outperforms entropy-based objectives and is highly competitive with state-of-the-art TTA methods, outperforming them on a large number of datasets and exhibiting more stable performance across diverse shifts.

</details>

### Unified Reinforcement and Imitation Learning for Vision-Language Models.
- **链接**: [arXiv:2510.19307](https://arxiv.org/abs/2510.19307) · 📚 被引 0
- **作者**: Byung-Kwan Lee, Ryo Hachiuma, Yong Man Ro, Yu-Chiang Frank Wang, Yueh-Hua Wu
- **🏷️ 机构**: NVIDIA, Korea Advanced Institute of Science and Technology, AIRoA
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have achieved remarkable progress, yet their large scale often renders them impractical for resource-constrained environments. This paper introduces Unified Reinforcement and Imitation Learning (RIL), a novel and efficient training algorithm designed to create powerful, lightweight VLMs. RIL distinctively combines the strengths of reinforcement learning with adversarial imitation learning. This enables smaller student VLMs not only to mimic the sophisticated text generation of large teacher models but also to systematically improve their generative capabilities through reinforcement signals. Key to our imitation framework is an LLM-based discriminator that adeptly distinguishes between student and teacher outputs, complemented by guidance from multiple large teacher VLMs to ensure diverse learning. This unified learning strategy, leveraging both reinforcement and imitation, empowers student models to achieve significant performance gains, making them competitive with leading closed-source VLMs. Extensive experiments on diverse vision-language benchmarks demonstrate that RIL significantly narrows the performance gap with state-of-the-art open- and closed-source VLMs and, in several instances, surpasses them.

</details>

### BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models.
- **链接**: [arXiv:2506.07961](https://arxiv.org/abs/2506.07961) · 📚 被引 1
- **作者**: Peiyan Li, Yixiang Chen, Hongtao Wu, Xiao Ma, Xiangnan Wu, Yan Huang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Institute of automation, Chinese academy of science, Chinese Academy of Sciences, Bytedance Research
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website:https://bridgevla.github.io/

</details>

### Uni-MuMER: Unified Multi-Task Fine-Tuning of Vision-Language Model for Handwritten Mathematical Expression Recognition.
- **链接**: [arXiv:2505.23566](https://arxiv.org/abs/2505.23566) · [代码](https://github.com/BFlameSwift/Uni-MuMER) · 📚 被引 2
- **作者**: Yu Li, Jin Jiang, Jianhua Zhu, Shuai Peng, Baole Wei, Yuxuan Zhou et al.
- **🏷️ 机构**: Peking University, Zhongguancun Institute of Artificial Intelligence
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Handwritten Mathematical Expression Recognition (HMER) remains a persistent challenge in Optical Character Recognition (OCR) due to the inherent freedom of symbol layouts and variability in handwriting styles. Prior methods have faced performance bottlenecks by proposing isolated architectural modifications, making them difficult to integrate coherently into a unified framework. Meanwhile, recent advances in pretrained vision-language models (VLMs) have demonstrated strong cross-task generalization, offering a promising foundation for developing unified solutions. In this paper, we introduce Uni-MuMER, which fully fine-tunes a VLM for the HMER task without modifying its architecture, effectively injecting domain-specific knowledge into a generalist framework. Our method integrates three data-driven tasks: Tree-Aware Chain-of-Thought (Tree-CoT) for structured spatial reasoning, Error-Driven Learning (EDL) for reducing confusion among visually similar characters, and Symbol Counting (SC) for improving recognition consistency in long expressions. Experiments on the CROHME and HME100K datasets show that Uni-MuMER achieves super state-of-the-art performance, outperforming the best lightweight specialized model SSAN by 16.31\% and the top-performing VLM Gemini2.5-flash by 24.42\% under zero-shot setting. Our datasets, models, and code are open-sourced at: {https://github.com/BFlameSwift/Uni-MuMER

</details>

### HoPE: Hybrid of Position Embedding for Long Context Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/ee37d51b3c003d89acba2363dde256af-Abstract-Conference.html) · 📚 被引 0
- **作者**: Haoran Li, Yingjie Qin, Baoyuan Ou, Lai Xu, Ruiwen Xu
- **🏷️ 机构**: University of the Chinese Academy of Sciences University of Illinois Urbana-Champaign, Fudan University, Engineer
- **会议**: NeurIPS 2025

### Recognition through Reasoning: Reinforcing Image Geo-localization with Large Vision-Language Models.
- **链接**: [arXiv:2506.14674](https://arxiv.org/abs/2506.14674) · [代码](https://github.com/lingli1996/GLOBE) · 📚 被引 1
- **作者**: Ling Li, Yao Zhou, Yuxuan Liang, Fugee Tsung, Jiaheng Wei
- **🏷️ 机构**: Institute of Software, CAS, Tencent Wechat, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous methods for image geo-localization have typically treated the task as either classification or retrieval, often relying on black-box decisions that lack interpretability. The rise of large vision-language models (LVLMs) has enabled a rethinking of geo-localization as a reasoning-driven task grounded in visual cues. However, two major challenges persist. On the data side, existing reasoning-focused datasets are primarily based on street-view imagery, offering limited scene diversity and constrained viewpoints. On the modeling side, current approaches predominantly rely on supervised fine-tuning, which yields only marginal improvements in reasoning capabilities. To address these challenges, we propose a novel pipeline that constructs a reasoning-oriented geo-localization dataset, MP16-Reason, using diverse social media images. We introduce GLOBE, Group-relative policy optimization for Localizability assessment and Optimized visual-cue reasoning, yielding Bi-objective geo-Enhancement for the VLM in recognition and reasoning. GLOBE incorporates task-specific rewards that jointly enhance localizability assessment, visual-cue reasoning, and geolocation accuracy. Both qualitative and quantitative results demonstrate that GLOBE outperforms state-of-the-art open-source LVLMs on geo-localization tasks, particularly in diverse visual scenes, while also generating more insightful and interpretable reasoning trajectories. The data and code are available at https://github.com/lingli1996/GLOBE.

</details>

### ShotBench: Expert-Level Cinematic Understanding in Vision-Language Models.
- **链接**: [arXiv:2506.21356](https://arxiv.org/abs/2506.21356) · 📚 被引 0
- **作者**: Hongbo Liu, Jingwen He, Yi Jin, Dian Zheng, Yuhao Dong, Fan Zhang et al.
- **🏷️ 机构**: Tongji University, The Chinese University of Hong Kong, SUN YAT-SEN UNIVERSITY
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cinematography, the fundamental visual language of film, is essential for conveying narrative, emotion, and aesthetic quality. While recent Vision-Language Models (VLMs) demonstrate strong general visual understanding, their proficiency in comprehending the nuanced cinematic grammar embedded within individual shots remains largely unexplored and lacks robust evaluation. This critical gap limits both fine-grained visual comprehension and the precision of AI-assisted video generation. To address this, we introduce ShotBench, a comprehensive benchmark specifically designed for cinematic language understanding. It features over 3.5k expert-annotated QA pairs from images and video clips, meticulously curated from over 200 acclaimed (predominantly Oscar-nominated) films and spanning eight key cinematography dimensions. Our evaluation of 24 leading VLMs on ShotBench reveals their substantial limitations: even the top-performing model achieves less than 60% average accuracy, particularly struggling with fine-grained visual cues and complex spatial reasoning. To catalyze advancement in this domain, we construct ShotQA, a large-scale multimodal dataset comprising approximately 70k cinematic QA pairs. Leveraging ShotQA, we develop ShotVL through supervised fine-tuning and Group Relative Policy Optimization. ShotVL significantly outperforms all existing open-source and proprietary models on ShotBench, establishing new state-of-the-art performance. We open-source our models, data, and code to foster rapid progress in this crucial area of AI-driven cinematic understanding and generation.

</details>

### IR3D-Bench: Evaluating Vision-Language Model Scene Understanding as Agentic Inverse Rendering.
- **链接**: [arXiv:2506.23329](https://arxiv.org/abs/2506.23329) · 📚 被引 3
- **作者**: Hengyu Liu, Chenxin Li, Zhengxin Li, Yipeng Wu, Wuyang Li, Zhiqin Yang et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Tianjin University, EPFL - EPF Lausanne
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) excel at descriptive tasks, but whether they truly understand scenes from visual observations remains uncertain. We introduce IR3D-Bench, a benchmark challenging VLMs to demonstrate understanding through active creation rather than passive recognition. Grounded in the analysis-by-synthesis paradigm, IR3D-Bench tasks Vision-Language Agents (VLAs) with actively using programming and rendering tools to recreate the underlying 3D structure of an input image, achieving agentic inverse rendering through tool use. This "understanding-by-creating" approach probes the tool-using generative capacity of VLAs, moving beyond the descriptive or conversational capacity measured by traditional scene understanding benchmarks. We provide a comprehensive suite of metrics to evaluate geometric accuracy, spatial relations, appearance attributes, and overall plausibility. Initial experiments on agentic inverse rendering powered by various state-of-the-art VLMs highlight current limitations, particularly in visual precision rather than basic tool usage. IR3D-Bench, including data and evaluation protocols, is released to facilitate systematic study and development of tool-using VLAs towards genuine scene understanding by creating.

</details>

### LOMIA: Label-Only Membership Inference Attacks against Pre-trained Large Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e1de63ec74f40d3234c4e053f3528e18-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yihao Liu, Xinqi Lyu, Dong Wang, Yanjie Li, Bin Xiao
- **🏷️ 机构**: The Hong Kong Polytechnic University, Meta Platforms Inc., Hong Kong Polytechnic University
- **会议**: NeurIPS 2025

### SSR: Enhancing Depth Perception in Vision-Language Models via Rationale-Guided Spatial Reasoning.
- **链接**: [arXiv:2505.12448](https://arxiv.org/abs/2505.12448) · 📚 被引 0
- **作者**: Yang Liu, Ming Ma, Xiaomin Yu, Pengxiang Ding, Han Zhao, Mingyang Sun et al.
- **🏷️ 机构**: Nanyang Technology University, Singapore, Harbin Institute of Technology, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite impressive advancements in Visual-Language Models (VLMs) for multi-modal tasks, their reliance on RGB inputs limits precise spatial understanding. Existing methods for integrating spatial cues, such as point clouds or depth, either require specialized sensors or fail to effectively exploit depth information for higher-order reasoning. To this end, we propose a novel Spatial Sense and Reasoning method, dubbed SSR, a novel framework that transforms raw depth data into structured, interpretable textual rationales. These textual rationales serve as meaningful intermediate representations to significantly enhance spatial reasoning capabilities. Additionally, we leverage knowledge distillation to compress the generated rationales into compact latent embeddings, which facilitate resource-efficient and plug-and-play integration into existing VLMs without retraining. To enable comprehensive evaluation, we introduce a new dataset named SSR-CoT, a million-scale visual-language reasoning dataset enriched with intermediate spatial reasoning annotations, and present SSRBench, a comprehensive multi-task benchmark. Extensive experiments on multiple benchmarks demonstrate SSR substantially improves depth utilization and enhances spatial reasoning, thereby advancing VLMs toward more human-like multi-modal understanding. Project page: https://yliu-cs.github.io/SSR.

</details>

### From Human Attention to Diagnosis: Semantic Patch-Level Integration of Vision-Language Models in Medical Imaging.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/be7bc8aa38696723cebe296b6122d7e3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dmitry Lvov, Ilya Pershin
- **🏷️ 机构**: Innopolis University
- **会议**: NeurIPS 2025

### ExGra-Med: Extended Context Graph Alignment for Medical Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9df0a10002a16365d03792ee5098376d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Duy M. H. Nguyen, Nghiem Tuong Diep, Trung Nguyen, Hoang-Bao Le, Tai D. Nguyen, Anh-Tien Nguyen et al.
- **🏷️ 机构**: DFKI &amp; Max Planck Research School for Intelligent Systems, German Research Center for AI, Dublin City University
- **会议**: NeurIPS 2025

### Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models.
- **链接**: [arXiv:2504.02821](https://arxiv.org/abs/2504.02821) · [代码](https://github.com/ExplainableML/sae-for-vlm) · 📚 被引 2
- **作者**: Mateusz Pach, Shyamgopal Karthik, Quentin Bouniot, Serge J. Belongie, Zeynep Akata
- **🏷️ 机构**: Helmholtz Zentrum München GmbH Ingolstädter Landstraße 1 85764 Neuherberg DE 129521671, Genmo, CEA-List, Université Paris-Saclay / Université St-Etienne, H. Curien Lab.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Sparse Autoencoders (SAEs) have recently gained attention as a means to improve the interpretability and steerability of Large Language Models (LLMs), both of which are essential for AI safety. In this work, we extend the application of SAEs to Vision-Language Models (VLMs), such as CLIP, and introduce a comprehensive framework for evaluating monosemanticity at the neuron-level in visual representations. To ensure that our evaluation aligns with human perception, we propose a benchmark derived from a large-scale user study. Our experimental results reveal that SAEs trained on VLMs significantly enhance the monosemanticity of individual neurons, with sparsity and wide latents being the most influential factors. Further, we demonstrate that applying SAE interventions on CLIP's vision encoder directly steers multimodal LLM outputs (e.g., LLaVA), without any modifications to the underlying language model. These findings emphasize the practicality and efficacy of SAEs as an unsupervised tool for enhancing both interpretability and control of VLMs. Code and benchmark data are available at https://github.com/ExplainableML/sae-for-vlm.

</details>

### FlySearch: Exploring how vision-language models explore.
- **链接**: [arXiv:2506.02896](https://arxiv.org/abs/2506.02896) · 📚 被引 0
- **作者**: Adam Pardyl, Dominik Matuszek, Mateusz Przebieracz, Marek Cygan, Bartosz Zielinski, Maciej Wolczyk
- **🏷️ 机构**: IDEAS NCBR; Jagiellonian University, Jagiellonian University in Krakow, Faculty of Mathematics and Computer Science of the Jagiellonian University, Jagiellonian University in Krakow
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The real world is messy and unstructured. Uncovering critical information often requires active, goal-driven exploration. It remains to be seen whether Vision-Language Models (VLMs), which recently emerged as a popular zero-shot tool in many difficult tasks, can operate effectively in such conditions. In this paper, we answer this question by introducing FlySearch, a 3D, outdoor, photorealistic environment for searching and navigating to objects in complex scenes. We define three sets of scenarios with varying difficulty and observe that state-of-the-art VLMs cannot reliably solve even the simplest exploration tasks, with the gap to human performance increasing as the tasks get harder. We identify a set of central causes, ranging from vision hallucination, through context misunderstanding, to task planning failures, and we show that some of them can be addressed by finetuning. We publicly release the benchmark, scenarios, and the underlying codebase.

</details>

### An Information-theoretical Framework for Understanding Out-of-distribution Detection with Pretrained Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/02d965b818b0567a3dab507dddbfb9ec-Abstract-Conference.html) · 📚 被引 3
- **作者**: Bo Peng, Jie Lu, Guangquan Zhang, Zhen Fang
- **🏷️ 机构**: Shanghai Jiaotong University, University of Technology Sydney, University of Technology Sydney (UTS)
- **会议**: NeurIPS 2025

### ROVER: Recursive Reasoning Over Videos with Vision-Language Models for Embodied Tasks.
- **链接**: [arXiv:2508.01943](https://arxiv.org/abs/2508.01943) · 📚 被引 0
- **作者**: Philip Schroeder, Ondrej Biza, Thomas Weng, Hongyin Luo, Jim Glass
- **🏷️ 机构**: Massachusetts Institute of Technology, Robotics and AI Institute
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have exhibited impressive capabilities across diverse image understanding tasks, but still struggle in settings that require reasoning over extended sequences of camera frames from a video. This limits their utility in embodied settings, which require reasoning over long frame sequences from a continuous stream of visual input at each moment of a task attempt. To address this limitation, we propose ROVER (Reasoning Over VidEo Recursively), a framework that enables the model to recursively decompose long-horizon video trajectories into segments corresponding to shorter subtasks within the trajectory. In doing so, ROVER facilitates more focused and accurate reasoning over temporally localized frame sequences without losing global context. We evaluate ROVER, implemented using an in-context learning approach, on diverse OpenX Embodiment videos and on a new dataset derived from RoboCasa that consists of 543 videos showing both expert and perturbed non-expert trajectories across 27 robotic manipulation tasks. ROVER outperforms strong baselines across three video reasoning tasks: task progress estimation, frame-level natural language reasoning, and video question answering. We observe that, by reducing the number of frames the model reasons over at each timestep, ROVER mitigates hallucinations, especially during unexpected or non-optimal moments of a trajectory. In addition, by enabling the implementation of a subtask-specific sliding context window, ROVER's time complexity scales linearly with video length, an asymptotic improvement over baselines. Demos, code, and data available at: https://rover-vlm.github.io

</details>

### On Epistemic Uncertainty of Visual Tokens for Object Hallucinations in Large Vision-Language Models.
- **链接**: [arXiv:2510.09008](https://arxiv.org/abs/2510.09008) · 📚 被引 0
- **作者**: Hoigi Seo, Dong Un Kang, Hyunjin Cho, Joohoon Lee, Se Young Chun
- **🏷️ 机构**: Seoul National University, Harvard University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (LVLMs), which integrate a vision encoder (VE) with a large language model, have achieved remarkable success across various tasks. However, there are still crucial challenges in LVLMs such as object hallucination, generating descriptions of objects that are not in the input image. Here, we argue that uncertain visual tokens within the VE is a key factor that contributes to object hallucination. Our statistical analysis found that there are positive correlations between visual tokens with high epistemic uncertainty and the occurrence of hallucinations. Furthermore, we show theoretically and empirically that visual tokens in early VE layers that exhibit large representation deviations under small adversarial perturbations indicate high epistemic uncertainty. Based on these findings, we propose a simple yet effective strategy to mitigate object hallucination by modifying the VE only. Our method comprises a proxy method with adversarial perturbations for identifying uncertain visual tokens efficiently and a method to mask these uncertain visual tokens during the self-attention process in the middle layers of the VE, suppressing their influence on visual encoding and thus alleviating hallucinations. Extensive experiments show that our method significantly reduces object hallucinations in LVLMs and can synergistically work with other prior arts.

</details>

### The Illusion of Progress? A Critical Look at Test-Time Adaptation for Vision-Language Models.
- **链接**: [arXiv:2506.24000](https://arxiv.org/abs/2506.24000) · 📚 被引 1
- **作者**: Lijun Sheng, Jian Liang, Ran He, Zilei Wang, Tieniu Tan
- **🏷️ 机构**: USTC, Wuhan University, NLPR, CASIA
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation (TTA) methods have gained significant attention for enhancing the performance of vision-language models (VLMs) such as CLIP during inference, without requiring additional labeled data. However, current TTA researches generally suffer from major limitations such as duplication of baseline results, limited evaluation metrics, inconsistent experimental settings, and insufficient analysis. These problems hinder fair comparisons between TTA methods and make it difficult to assess their practical strengths and weaknesses. To address these challenges, we introduce TTA-VLM, a comprehensive benchmark for evaluating TTA methods on VLMs. Our benchmark implements 8 episodic TTA and 7 online TTA methods within a unified and reproducible framework, and evaluates them across 15 widely used datasets. Unlike prior studies focused solely on CLIP, we extend the evaluation to SigLIP--a model trained with a Sigmoid loss--and include training-time tuning methods such as CoOp, MaPLe, and TeCoA to assess generality. Beyond classification accuracy, TTA-VLM incorporates various evaluation metrics, including robustness, calibration, out-of-distribution detection, and stability, enabling a more holistic assessment of TTA methods. Through extensive experiments, we find that 1) existing TTA methods produce limited gains compared to the previous pioneering work; 2) current TTA methods exhibit poor collaboration with training-time fine-tuning methods; 3) accuracy gains frequently come at the cost of reduced model trustworthiness. We release TTA-VLM to provide fair comparison and comprehensive evaluation of TTA methods for VLMs, and we hope it encourages the community to develop more reliable and generalizable TTA strategies.

</details>

### World-aware Planning Narratives Enhance Large Vision-Language Model Planner.
- **链接**: [arXiv:2506.21230](https://arxiv.org/abs/2506.21230) · 📚 被引 0
- **作者**: Junhao Shi, Zhaoye Fei, Siyin Wang, Qipeng Guo, Jingjing Gong, Xipeng Qiu
- **🏷️ 机构**: Fudan University, Tsinghua University, Tsinghua University, AWS
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) show promise for embodied planning tasks but struggle with complex scenarios involving unfamiliar environments and multi-step goals. Current approaches rely on environment-agnostic imitation learning that disconnects instructions from environmental contexts, causing models to struggle with context-sensitive instructions and rely on supplementary cues rather than visual reasoning during long-horizon interactions. In this work, we propose World-Aware Planning Narrative Enhancement (WAP), a framework that infuses LVLMs with comprehensive environmental understanding through four cognitive capabilities (visual appearance modeling, spatial reasoning, functional abstraction, and syntactic grounding) while developing and evaluating models using only raw visual observations through curriculum learning. Evaluations on the EB-ALFRED benchmark demonstrate substantial improvements, with Qwen2.5-VL achieving a 60.7 absolute improvement in task success rates, particularly in commonsense reasoning (+60.0) and long-horizon planning (+70.0). Notably, our enhanced open-source models outperform proprietary systems like GPT-4o and Claude-3.5-Sonnet by a large margin.

</details>

### JailBound: Jailbreaking Internal Safety Boundaries of Vision-Language Models.
- **链接**: [arXiv:2505.19610](https://arxiv.org/abs/2505.19610) · 📚 被引 0
- **作者**: Jiaxin Song, Yixu Wang, Jie Li, Xuan Tong, Rui Yu, Yan Teng et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Fudan University, Xiamen University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) exhibit impressive performance, yet the integration of powerful vision encoders has significantly broadened their attack surface, rendering them increasingly susceptible to jailbreak attacks. However, lacking well-defined attack objectives, existing jailbreak methods often struggle with gradient-based strategies prone to local optima and lacking precise directional guidance, and typically decouple visual and textual modalities, thereby limiting their effectiveness by neglecting crucial cross-modal interactions. Inspired by the Eliciting Latent Knowledge (ELK) framework, we posit that VLMs encode safety-relevant information within their internal fusion-layer representations, revealing an implicit safety decision boundary in the latent space. This motivates exploiting boundary to steer model behavior. Accordingly, we propose JailBound, a novel latent space jailbreak framework comprising two stages: (1) Safety Boundary Probing, which addresses the guidance issue by approximating decision boundary within fusion layer's latent space, thereby identifying optimal perturbation directions towards the target region; and (2) Safety Boundary Crossing, which overcomes the limitations of decoupled approaches by jointly optimizing adversarial perturbations across both image and text inputs. This latter stage employs an innovative mechanism to steer the model's internal state towards policy-violating outputs while maintaining cross-modal semantic consistency. Extensive experiments on six diverse VLMs demonstrate JailBound's efficacy, achieves 94.32% white-box and 67.28% black-box attack success averagely, which are 6.17% and 21.13% higher than SOTA methods, respectively. Our findings expose a overlooked safety risk in VLMs and highlight the urgent need for more robust defenses. Warning: This paper contains potentially sensitive, harmful and offensive content.

</details>

### VideoGameQA-Bench: Evaluating Vision-Language Models for Video Game Quality Assurance.
- **链接**: [arXiv:2505.15952](https://arxiv.org/abs/2505.15952) · 📚 被引 0
- **作者**: Mohammad Reza Taesiri, Abhijay Ghildyal, Saman Zadtootaghaj, Nabajeet Barman, Cor-Paul Bezemer
- **🏷️ 机构**: University of Alberta, Sony Interactive Entertainment
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With video games now generating the highest revenues in the entertainment industry, optimizing game development workflows has become essential for the sector's sustained growth. Recent advancements in Vision-Language Models (VLMs) offer considerable potential to automate and enhance various aspects of game development, particularly Quality Assurance (QA), which remains one of the industry's most labor-intensive processes with limited automation options. To accurately evaluate the performance of VLMs in video game QA tasks and determine their effectiveness in handling real-world scenarios, there is a clear need for standardized benchmarks, as existing benchmarks are insufficient to address the specific requirements of this domain. To bridge this gap, we introduce VideoGameQA-Bench, a comprehensive benchmark that covers a wide array of game QA activities, including visual unit testing, visual regression testing, needle-in-a-haystack tasks, glitch detection, and bug report generation for both images and videos of various games. Code and data are available at: https://asgaardlab.github.io/videogameqa-bench/

</details>

### Reason-RFT: Reinforcement Fine-Tuning for Visual Reasoning of Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/08d70284b013c03ba89cd2b642bc864b-Abstract-Conference.html) · 📚 被引 1
- **作者**: Huajie Tan, Yuheng Ji, Xiaoshuai Hao, Xiansheng Chen, Pengwei Wang, Zhongyuan Wang et al.
- **🏷️ 机构**: Institute of automation, Chinese academy of science, Chinese Academy of Sciences, SAIT-China Lab, Samsung Research Center, Beijing Academy of Artificial Intelligence
- **会议**: NeurIPS 2025

### ChartMuseum: Testing Visual Reasoning Capabilities of Large Vision-Language Models.
- **链接**: [arXiv:2505.13444](https://arxiv.org/abs/2505.13444) · 📚 被引 1
- **作者**: Liyan Tang, Grace Kim, Xinyu Zhao, Thom Lake, Wenxuan Ding, Fangcong Yin et al.
- **🏷️ 机构**: University of Texas, Austin, University of Pennsylvania, University of Pennsylvania, Massachusetts Institute of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Chart understanding presents a unique challenge for large vision-language models (LVLMs), as it requires the integration of sophisticated textual and visual reasoning capabilities. However, current LVLMs exhibit a notable imbalance between these skills, falling short on visual reasoning that is difficult to perform in text. We conduct a case study using a synthetic dataset solvable only through visual reasoning and show that model performance degrades significantly with increasing visual complexity, while human performance remains robust. We then introduce ChartMuseum, a new Chart Question Answering (QA) benchmark containing 1,162 expert-annotated questions spanning multiple reasoning types, curated from real-world charts across 184 sources, specifically built to evaluate complex visual and textual reasoning. Unlike prior chart understanding benchmarks -- where frontier models perform similarly and near saturation -- our benchmark exposes a substantial gap between model and human performance, while effectively differentiating model capabilities: although humans achieve 93% accuracy, the best-performing model Gemini-2.5-Pro attains only 63.0%, and the leading open-source LVLM Qwen2.5-VL-72B-Instruct achieves only 38.5%. Moreover, on questions requiring primarily visual reasoning, all models experience a 35%-55% performance drop from text-reasoning-heavy question performance. Lastly, our qualitative error analysis reveals specific categories of visual reasoning that are challenging for current LVLMs.

</details>

### FlowCut: Rethinking Redundancy via Information Flow for Efficient Vision-Language Models.
- **链接**: [arXiv:2505.19536](https://arxiv.org/abs/2505.19536) · [代码](https://github.com/TungChintao/FlowCut) · 📚 被引 0
- **作者**: Jintao Tong, Wenwei Jin, Pengda Qin, Anqi Li, Yixiong Zou, Yuhong Li et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Xiaohongshu, Tencent
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models (LVLMs) excel at multimodal understanding but suffer from high computational costs due to redundant vision tokens. Existing pruning methods typically rely on single-layer attention scores to rank and prune redundant visual tokens to solve this inefficiency. However, as the interaction between tokens and layers is complicated, this raises a basic question: Is such a simple single-layer criterion sufficient to identify redundancy? To answer this question, we rethink the emergence of redundant visual tokens from a fundamental perspective: information flow, which models the interaction between tokens and layers by capturing how information moves between tokens across layers. We find (1) the CLS token acts as an information relay, which can simplify the complicated flow analysis; (2) the redundancy emerges progressively and dynamically via layer-wise attention concentration; and (3) relying solely on attention scores from single layers can lead to contradictory redundancy identification. Based on this, we propose FlowCut, an information-flow-aware pruning framework, mitigating the insufficiency of the current criterion for identifying redundant tokens and better aligning with the model's inherent behaviors. Extensive experiments show that FlowCut achieves superior results, outperforming SoTA by 1.6% on LLaVA-1.5-7B with 88.9% token reduction, and by 4.3% on LLaVA-NeXT-7B with 94.4% reduction, delivering 3.2x speed-up in the prefilling stage. Our code is available at https://github.com/TungChintao/FlowCut

</details>

### TRoVe: Discovering Error-Inducing Static Feature Biases in Temporal Vision-Language Models.
- **链接**: [arXiv:2512.01048](https://arxiv.org/abs/2512.01048) · [代码](https://github.com/Stanford-AIMI/TRoVe) · 📚 被引 0
- **作者**: Maya Varma, Jean-Benoit Delbrouck, Sophie Ostmeier, Akshay Chaudhari, Curtis Langlotz
- **🏷️ 机构**: Stanford University, HOPPR - Stanford
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have made great strides in addressing temporal understanding tasks, which involve characterizing visual changes across a sequence of images. However, recent works have suggested that when making predictions, VLMs may rely on static feature biases, such as background or object features, rather than dynamic visual changes. Static feature biases are a type of shortcut and can contribute to systematic prediction errors on downstream tasks; as a result, identifying and characterizing error-inducing static feature biases is critical prior to real-world model deployment. In this work, we introduce TRoVe, an automated approach for discovering error-inducing static feature biases learned by temporal VLMs. Given a trained VLM and an annotated validation dataset associated with a downstream classification task, TRoVe extracts candidate static features from the dataset and scores each feature by (i) the effect of the feature on classification errors as well as (ii) the extent to which the VLM relies on the feature when making predictions. In order to quantitatively evaluate TRoVe, we introduce an evaluation framework consisting of 101 trained temporal VLMs paired with ground-truth annotations for learned static feature biases. We use this framework to demonstrate that TRoVe can accurately identify error-inducing static feature biases in VLMs, achieving a 28.6% improvement over the closest baseline. Finally, we apply TRoVe to 7 off-the-shelf VLMs and 2 temporal understanding tasks, surfacing previously-unknown static feature biases and demonstrating that knowledge of learned biases can aid in improving model performance at test time. Our code is available at https://github.com/Stanford-AIMI/TRoVe.

</details>

### Towards General Continuous Memory for Vision-Language Models.
- **链接**: [arXiv:2505.17670](https://arxiv.org/abs/2505.17670) · 📚 被引 1
- **作者**: Wenyi Wu, Zixuan Song, Kun Zhou, Yifei Shao, Zhiting Hu, Biwei Huang
- **🏷️ 机构**: University of California, San Diego, xAI / UCSD
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Language models (LMs) and their extension, vision-language models (VLMs), have achieved remarkable performance across various tasks. However, they still struggle with complex reasoning tasks that require multimodal or multilingual real-world knowledge. To support such capabilities, an external memory system that can efficiently provide relevant multimodal information is essential. Existing approaches generally concatenate image and text tokens into a long sequence as memory, which, however, may drastically increase context length and even degrade performance. In contrast, we propose using continuous memory, a compact set of dense embeddings to more effectively and efficiently represent multimodal and multilingual knowledge. Our key insight is that a VLM can serve as its own continuous memory encoder. We empirically show that this design improves performance on complex multimodal reasoning tasks. Building on this, we introduce a data-efficient and parameter-efficient method to fine-tune the VLM into a memory encoder, requiring only 1.2% of the model's parameters and a small corpus of 15.6K self-synthesized samples. Our approach CoMEM utilizes VLM's original capabilities to encode arbitrary multimodal and multilingual knowledge into just 8 continuous embeddings. Since the inference-time VLM remains frozen, our memory module is plug-and-play and can be flexibly integrated as needed. Extensive experiments across eight multimodal reasoning benchmarks demonstrate the effectiveness of our approach.

</details>

### Hawaii: Hierarchical Visual Knowledge Transfer for Efficient Vision-Language Models.
- **链接**: [arXiv:2506.19072](https://arxiv.org/abs/2506.19072) · [代码](https://github.com/yimuwangcs/wise-hawaii) · 📚 被引 0
- **作者**: Yimu Wang, Mozhgan Nasr Azadani, Sean Sedwards, Krzysztof Czarnecki
- **🏷️ 机构**: University of Waterloo
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Improving the visual understanding ability of vision-language models (VLMs) is crucial for enhancing their performance across various tasks. While using multiple pretrained visual experts has shown great promise, it often incurs significant computational costs during training and inference. To address this challenge, we propose HAWAII, a novel framework that distills knowledge from multiple visual experts into a single vision encoder, enabling it to inherit the complementary strengths of several experts with minimal computational overhead. To mitigate conflicts among different teachers and switch between different teacher-specific knowledge, instead of using a fixed set of adapters for multiple teachers, we propose to use teacher-specific Low-Rank Adaptation (LoRA) adapters with a corresponding router. Each adapter is aligned with a specific teacher, avoiding noisy guidance during distillation. To enable efficient knowledge distillation, we propose fine-grained and coarse-grained distillation. At the fine-grained level, token importance scores are employed to emphasize the most informative tokens from each teacher adaptively. At the coarse-grained level, we summarize the knowledge from multiple teachers and transfer it to the student using a set of general-knowledge LoRA adapters with a router. Extensive experiments on various vision-language tasks demonstrate the superiority of HAWAII compared to popular open-source VLMs. The code is available at https://github.com/yimuwangcs/wise-hawaii.

</details>

### VLMLight: Safety-Critical Traffic Signal Control via Vision-Language Meta-Control and Dual-Branch Reasoning Architecture.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/3849b5861dcaeaf4758eef0979a98cc6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Maonan Wang, Yirong Chen, Aoyu Pang, Yuxin Cai, Chung Shue Chen, Yuheng Kan et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Shanghai Artificial Intelligence Laboratory, Carnegie Mellon University
- **会议**: NeurIPS 2025

### Image Token Matters: Mitigating Hallucination in Discrete Tokenizer-based Large Vision-Language Models via Latent Editing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a17c939f1bdee90ec74a9c3cb938d8c3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weixing Wang, Zifeng Ding, Jindong Gu, Rui Cao, Christoph Meinel, Gerard de Melo et al.
- **🏷️ 机构**: Hasso Plattner Institute, University of Cambridge, Google &amp; University of Oxford
- **会议**: NeurIPS 2025

### Learning Robust Vision-Language Models from Natural Latent Spaces.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e75c198ec770e78fd3851845e85c65d9-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhangyun Wang, Ni Ding, Aniket Mahanti
- **🏷️ 机构**: University of Auckland
- **会议**: NeurIPS 2025

### Think or Not? Selective Reasoning via Reinforcement Learning for Vision-Language Models.
- **链接**: [arXiv:2505.16854](https://arxiv.org/abs/2505.16854) · [代码](https://github.com/kokolerk/TON) · 📚 被引 0
- **作者**: Jiaqi Wang, Kevin Qinghong Lin, James Cheng, Mike Zheng Shou
- **🏷️ 机构**: Beijing University of Posts and Telecommunications, University of Oxford, The Chinese University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reinforcement Learning (RL) has proven to be an effective post-training strategy for enhancing reasoning in vision-language models (VLMs). Group Relative Policy Optimization (GRPO) is a recent prominent method that encourages models to generate complete reasoning traces before answering, leading to increased token usage and computational cost. Inspired by the human-like thinking process-where people skip reasoning for easy questions but think carefully when needed-we explore how to enable VLMs to first decide when reasoning is necessary. To realize this, we propose TON, a two-stage training strategy: (i) a supervised fine-tuning (SFT) stage with a simple yet effective 'thought dropout' operation, where reasoning traces are randomly replaced with empty thoughts. This introduces a think-or-not format that serves as a cold start for selective reasoning; (ii) a GRPO stage that enables the model to freely explore when to think or not, while maximizing task-aware outcome rewards. Experimental results show that TON can reduce the completion length by up to 90% compared to vanilla GRPO, without sacrificing performance or even improving it. Further evaluations across LLM (GSM8K), VLM (CLEVR, Super-CLEVR, GeoQA), and Agentic (AITZ) tasks-covering a range of reasoning difficulties under both 3B and 7B models-consistently reveal that the model progressively learns to bypass unnecessary reasoning steps as training advances. These findings shed light on the path toward human-like reasoning patterns in RL approaches. Our code is available at https://github.com/kokolerk/TON.

</details>

### Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation.
- **链接**: [arXiv:2505.11383](https://arxiv.org/abs/2505.11383) · 📚 被引 2
- **作者**: Zihan Wang, Seungjun Lee, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore, national university of singaore, National University of Singapore
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-Language Navigation (VLN) is a core task where embodied agents leverage their spatial mobility to navigate in 3D environments toward designated destinations based on natural language instructions. Recently, video-language large models (Video-VLMs) with strong generalization capabilities and rich commonsense knowledge have shown remarkable performance when applied to VLN tasks. However, these models still encounter the following challenges when applied to real-world 3D navigation: 1) Insufficient understanding of 3D geometry and spatial semantics; 2) Limited capacity for large-scale exploration and long-term environmental memory; 3) Poor adaptability to dynamic and changing environments.To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in navigation action prediction. Given posed RGB-D images, our Dynam3D projects 2D CLIP features into 3D space and constructs multi-level 3D patch-instance-zone representations for 3D geometric and semantic understanding with a dynamic and layer-wise update strategy. Our Dynam3D is capable of online encoding and localization of 3D instances, and dynamically updates them in changing environments to provide large-scale exploration and long-term memory capabilities for navigation. By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings. Furthermore, experiments for pre-exploration, lifelong memory, and real-world robot validate the effectiveness of practical deployment.

</details>

### VL-Rethinker: Incentivizing Self-Reflection of Vision-Language Models with Reinforcement Learning.
- **链接**: [arXiv:2504.08837](https://arxiv.org/abs/2504.08837) · 📚 被引 0
- **作者**: Haozhe Wang, Chao Qu, Zuming Huang, Wei Chu, Fangzhen Lin, Wenhu Chen
- **🏷️ 机构**: HKUST, Ant Financial Services Group, Inf Tech
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, slow-thinking systems like GPT-o1 and DeepSeek-R1 have demonstrated great potential in solving challenging problems through explicit reflection. They significantly outperform the best fast-thinking models, such as GPT-4o, on various math and science benchmarks. However, their multimodal reasoning capabilities remain on par with fast-thinking models. For instance, GPT-o1's performance on benchmarks like MathVista, MathVerse, and MathVision is similar to fast-thinking models. In this paper, we aim to enhance the slow-thinking capabilities of vision-language models using reinforcement learning (without relying on distillation) to advance the state of the art. First, we adapt the GRPO algorithm with a novel technique called Selective Sample Replay (SSR) to address the vanishing advantages problem. While this approach yields strong performance, the resulting RL-trained models exhibit limited self-reflection or self-verification. To further encourage slow-thinking, we introduce Forced Rethinking, which appends a rethinking trigger token to the end of rollouts in RL training, explicitly enforcing a self-reflection reasoning step. By combining these two techniques, our model, VL-Rethinker, advances state-of-the-art scores on MathVista, MathVerse to achieve 80.4%, 63.5% respectively. VL-Rethinker also achieves open-source SoTA on multi-disciplinary benchmarks such as MathVision, MMMU-Pro, EMMA, and MEGA-Bench, narrowing the gap with OpenAI-o1. Our empirical results show the effectiveness of our approaches.

</details>

### Attention! Your Vision Language Model Could Be Maliciously Manipulated.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/baf0fab890edc9dce805d7c518058712-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xiaosen Wang, Shaokang Wang, Zhijin Ge, Yuyang Luo, Shudong Zhang
- **🏷️ 机构**: Huawei Technologies Ltd., Shanghai Jiao Tong University, Xidian University
- **会议**: NeurIPS 2025

### Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation.
- **链接**: [arXiv:2505.11886](https://arxiv.org/abs/2505.11886) · 📚 被引 1
- **作者**: Shuo Wang, Yongcai Wang, Wanting Li, Xudong Cai, Yucheng Wang, Maiyue Chen et al.
- **🏷️ 机构**: CAS, Renmin University of China, Institute of automation, Chinese academy of science, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation (VLN) is a critical task for developing embodied agents that can follow natural language instructions to navigate in complex real-world environments. Recent advances in VLN by large pretrained models have significantly improved generalization and instruction grounding compared to traditional approaches. However, the role of reasoning strategies in navigation-an action-centric, long-horizon task-remains underexplored, despite Chain-of-Thought (CoT) reasoning's demonstrated success in static tasks like visual question answering. To address this gap, we conduct the first systematic evaluation of reasoning strategies for VLN, including No-Think (direct action prediction), Pre-Think (reason before action), and Post-Think (reason after action). Surprisingly, our findings reveal the Inference-time Reasoning Collapse issue, where inference-time reasoning degrades navigation accuracy, highlighting the challenges of integrating reasoning into VLN. Based on this insight, we propose Aux-Think, a framework that trains models to internalize structured reasoning patterns through CoT supervision, while inferring action directly without reasoning in online prediction. To support this framework, we release R2R-CoT-320k, the first Chain-of-Thought annotated dataset for VLN. Extensive experiments show that Aux-Think reduces training effort greatly and achieves the best performance under the same data scale.

</details>

### Time-R1: Post-Training Large Vision Language Model for Temporal Video Grounding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7801b29c93b599b8d0c44138596bdeed-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ye Wang, Ziheng Wang, Boshen Xu, Yang Du, Kejun Lin, Zihan Xiao et al.
- **🏷️ 机构**: Renmin University of China, Beijing University of Posts and Telecommunications, Xiaomi Corporation
- **会议**: NeurIPS 2025

### GRE Suite: Geo-localization Inference via Fine-Tuned Vision-Language Models and Enhanced Reasoning Chains.
- **链接**: [arXiv:2505.18700](https://arxiv.org/abs/2505.18700) · [代码](https://github.com/Thorin215/GRE) · 📚 被引 0
- **作者**: Chun Wang, Xiaojun Ye, Xiaoran Pan, Zihao Pan, Haofan Wang, Yiren Song
- **🏷️ 机构**: Zhejiang University, Alibaba Group, Carnegie Mellon University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in Visual Language Models (VLMs) have demonstrated exceptional performance in visual reasoning tasks. However, geo-localization presents unique challenges, requiring the extraction of multigranular visual cues from images and their integration with external world knowledge for systematic reasoning. Current approaches to geo-localization tasks often lack robust reasoning mechanisms and explainability, limiting their effectiveness. To address these limitations, we propose the Geo Reason Enhancement (GRE) Suite, a novel framework that augments VLMs with structured reasoning chains for accurate and interpretable location inference. The GRE Suite is systematically developed across three key dimensions: dataset, model, and benchmark. First, we introduce GRE30K, a high-quality geo-localization reasoning dataset designed to facilitate fine-grained visual and contextual analysis. Next, we present the GRE model, which employs a multi-stage reasoning strategy to progressively infer scene attributes, local details, and semantic features, thereby narrowing down potential geographic regions with enhanced precision. Finally, we construct the Geo Reason Evaluation Benchmark (GREval-Bench), a comprehensive evaluation framework that assesses VLMs across diverse urban, natural, and landmark scenes to measure both coarse-grained (e.g., country, continent) and fine-grained (e.g., city, street) localization performance. Experimental results demonstrate that GRE significantly outperforms existing methods across all granularities of geo-localization tasks, underscoring the efficacy of reasoning-augmented VLMs in complex geographic inference. Code and data will be released at https://github.com/Thorin215/GRE.

</details>

### MMLongBench: Benchmarking Long-Context Vision-Language Models Effectively and Thoroughly.
- **链接**: [arXiv:2505.10610](https://arxiv.org/abs/2505.10610) · 📚 被引 0
- **作者**: Zhaowei Wang, Wenhao Yu, Xiyu Ren, Jipeng Zhang, Yu Zhao, Rohit Saxena et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Tencent Seattle, Hong Kong University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid extension of context windows in large vision-language models has given rise to long-context vision-language models (LCVLMs), which are capable of handling hundreds of images with interleaved text tokens in a single forward pass. In this work, we introduce MMLongBench, the first benchmark covering a diverse set of long-context vision-language tasks, to evaluate LCVLMs effectively and thoroughly. MMLongBench is composed of 13,331 examples spanning five different categories of downstream tasks, such as Visual RAG and Many-Shot ICL. It also provides broad coverage of image types, including various natural and synthetic images. To assess the robustness of the models to different input lengths, all examples are delivered at five standardized input lengths (8K-128K tokens) via a cross-modal tokenization scheme that combines vision patches and text tokens. Through a thorough benchmarking of 46 closed-source and open-source LCVLMs, we provide a comprehensive analysis of the current models' vision-language long-context ability. Our results show that: i) performance on a single task is a weak proxy for overall long-context capability; ii) both closed-source and open-source models face challenges in long-context vision-language tasks, indicating substantial room for future improvement; iii) models with stronger reasoning ability tend to exhibit better long-context performance. By offering wide task coverage, various image types, and rigorous length control, MMLongBench provides the missing foundation for diagnosing and advancing the next generation of LCVLMs.

</details>

### CURV: Coherent Uncertainty-Aware Reasoning in Vision-Language Models for X-Ray Report Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/86a99b74adac7c77998902371f53850d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ziao Wang, Sixing Yan, Kejing Yin, Xiaofeng Zhang, William K. Cheung
- **🏷️ 机构**: Hong Kong Baptist University, Shanghai Jiaotong University
- **会议**: NeurIPS 2025

### Quantifying Cross-Modality Memorization in Vision-Language Models.
- **链接**: [arXiv:2506.05198](https://arxiv.org/abs/2506.05198) · 📚 被引 0
- **作者**: Yuxin Wen, Yangsibo Huang, Tom Goldstein, Ravi Kumar, Badih Ghazi, Chiyuan Zhang
- **🏷️ 机构**: University of Maryland, Google, Google Research
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding what and how neural networks memorize during training is crucial, both from the perspective of unintentional memorization of potentially sensitive information and from the standpoint of effective knowledge acquisition for real-world, knowledge-intensive tasks. While previous studies primarily investigate memorization within a single modality, such as text memorization in large language models or image memorization in diffusion models, unified multimodal models are becoming increasingly prevalent in practical applications. In this work, we focus on the unique characteristics of cross-modality memorization and conduct a systematic study centered on vision-language models. To facilitate controlled experiments, we first introduce a synthetic persona dataset comprising diverse synthetic person images and textual descriptions. We quantify factual knowledge memorization and cross-modal transferability by training models on a single modality and evaluating their performance in the other. Our results reveal that facts learned in one modality transfer to the other, but a significant gap exists between recalling information in the source and target modalities. Furthermore, we observe that this gap exists across various scenarios, including more capable models, machine unlearning, and the multi-hop case. At the end, we propose a baseline method to mitigate this challenge. We hope our study can inspire future research on developing more robust multimodal learning techniques to enhance cross-modal transferability.

</details>

### Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing.
- **链接**: [arXiv:2506.09965](https://arxiv.org/abs/2506.09965) · 📚 被引 0
- **作者**: Junfei Wu, Jian Guan, Kaituo Feng, Qiang Liu, Shu Wu, Liang Wang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Ant Group, The Chinese University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As textual reasoning with large language models (LLMs) has advanced significantly, there has been growing interest in enhancing the multimodal reasoning capabilities of large vision-language models (LVLMs). However, existing methods primarily approach multimodal reasoning in a straightforward, text-centric manner, where both reasoning and answer derivation are conducted purely through text, with the only difference being the presence of multimodal input. As a result, these methods often encounter fundamental limitations in spatial reasoning tasks that demand precise geometric understanding and continuous spatial tracking-capabilities that humans achieve through mental visualization and manipulation. To address the limitations, we propose drawing to reason in space, a novel paradigm that enables LVLMs to reason through elementary drawing operations in the visual space. By equipping models with basic drawing operations, including annotating bounding boxes and drawing auxiliary lines, we empower them to express and analyze spatial relationships through direct visual manipulation, meanwhile avoiding the performance ceiling imposed by specialized perception tools in previous tool-integrated reasoning approaches. To cultivate this capability, we develop a three-stage training framework: cold-start training with synthetic data to establish basic drawing abilities, reflective rejection sampling to enhance self-reflection behaviors, and reinforcement learning to directly optimize for target rewards. Extensive experiments demonstrate that our model, named VILASR, consistently outperforms existing methods across diverse spatial reasoning benchmarks, involving maze navigation, static spatial reasoning, video-based reasoning, and multi-view-based reasoning tasks, with an average improvement of 18.4%.

</details>

### Generate, but Verify: Reducing Hallucination in Vision-Language Models with Retrospective Resampling.
- **链接**: [arXiv:2504.13169](https://arxiv.org/abs/2504.13169) · 📚 被引 0
- **作者**: Tsung-Han Wu, Heekyung Lee, Jiaxin Ge, Joseph E. Gonzalez, Trevor Darrell, David M. Chan
- **🏷️ 机构**: University of California, Berkeley, Pohang University of Science and Technology, UC Berkeley
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) excel at visual understanding but often suffer from visual hallucinations, where they generate descriptions of nonexistent objects, actions, or concepts, posing significant risks in safety-critical applications. Existing hallucination mitigation methods typically follow one of two paradigms: generation adjustment, which modifies decoding behavior to align text with visual inputs, and post-hoc verification, where external models assess and correct outputs. While effective, generation adjustment methods often rely on heuristics and lack correction mechanisms, while post-hoc verification is complicated, typically requiring multiple models and tending to reject outputs rather than refine them. In this work, we introduce REVERSE, a unified framework that integrates hallucination-aware training with on-the-fly self-verification. By leveraging a new hallucination-verification dataset containing over 1.3M semi-synthetic samples, along with a novel inference-time retrospective resampling technique, our approach enables VLMs to both detect hallucinations during generation and dynamically revise those hallucinations. Our evaluations show that REVERSE achieves state-of-the-art hallucination reduction, outperforming the best existing methods by up to 12% on CHAIR-MSCOCO and 34% on HaloQuest. Our dataset, model, and code are available at: https://reverse-vlm.github.io.

</details>

### Fast-Slow Thinking GRPO for Large Vision-Language Model Reasoning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/fa9259a773e85c49624aea9de2ff9146-Abstract-Conference.html) · 📚 被引 1
- **作者**: Wenyi Xiao, Leilei Gan
- **🏷️ 机构**: Zhejiang University
- **会议**: NeurIPS 2025

### MindOmni: Unleashing Reasoning Generation in Vision Language Models with RGPO.
- **链接**: [arXiv:2505.13031](https://arxiv.org/abs/2505.13031) · [代码](https://github.com/TencentARC/MindOmni) · 📚 被引 0
- **作者**: Yicheng Xiao, Lin Song, Yukang Chen, Yingmin Luo, Yuxin Chen, Yukang Gan et al.
- **🏷️ 机构**: Southern University of Science and Technology, Tencent AI Lab, NVIDIA Research
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent text-to-image systems face limitations in handling multimodal inputs and complex reasoning tasks. We introduce MindOmni, a unified multimodal large language model that addresses these challenges by incorporating reasoning generation through reinforcement learning. MindOmni leverages a three-phase training strategy: i) design of a unified vision language model with a decoder-only diffusion module, ii) supervised fine-tuning with Chain-of-Thought (CoT) instruction data, and iii) our proposed Reasoning Generation Policy Optimization (RGPO) algorithm, utilizing multimodal feedback to effectively guide policy updates. Experimental results demonstrate that MindOmni outperforms existing models, achieving impressive performance on both understanding and generation benchmarks, meanwhile showcasing advanced fine-grained reasoning generation capabilities, especially with mathematical reasoning instruction. All codes will be made public at https://github.com/TencentARC/MindOmni

</details>

### VLM in a flash: I/O-Efficient Sparsification of Vision-Language Model via Neuron Chunking.
- **链接**: [arXiv:2511.18692](https://arxiv.org/abs/2511.18692) · 📚 被引 0
- **作者**: Kichang Yang, Seonjun Kim, Minjae Kim, Nairan Zhang, Chi Zhang, Youngki Lee
- **🏷️ 机构**: Seoul National University, Amazon, University of California, Los Angeles
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Edge deployment of large Vision-Language Models (VLMs) increasingly relies on flash-based weight offloading, where activation sparsification is used to reduce I/O overhead. However, conventional sparsification remains model-centric, selecting neurons solely by activation magnitude and neglecting how access patterns influence flash performance. We present Neuron Chunking, an I/O-efficient sparsification strategy that operates on chunks (i.e., groups of contiguous neurons in memory) and couples neuron importance with storage access cost. The method models I/O latency through a lightweight abstraction of access contiguity and selects chunks with high utility, defined as neuron importance normalized by estimated latency. By aligning sparsification decisions with the underlying storage behavior, Neuron Chunking improves I/O efficiency by up to 4.65x and 5.76x on Jetson Orin Nano and Jetson AGX Orin, respectively.

</details>

### Escaping the SpuriVerse: Can Large Vision-Language Models Generalize Beyond Seen Spurious Correlations?
- **链接**: [arXiv:2506.18322](https://arxiv.org/abs/2506.18322) · 📚 被引 0
- **作者**: Yiwei Yang, Chung Peng Lee, Shangbin Feng, Dora Zhao, Bingbing Wen, Anthony Z. Liu et al.
- **🏷️ 机构**: University of Washington, Princeton University, Sony Research / Stanford University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Finetuning can cause spurious correlations to arise between non-essential features and the target labels, but benchmarks to study these effects involve contrived settings and narrow tasks. In contrast, we consider spurious correlations in multi-modal Large Vision Language Models (LVLMs) pretrained on extensive and diverse datasets without explicit task supervision. We develop a benchmark by sourcing GPT-4o errors on real-world visual-question-answering (VQA) benchmarks, then curating a subset through LVLM-human annotation and synthetic counterfactual evaluation to identify errors caused by spurious correlations. This process yields SpuriVerse, a novel benchmark comprised of 124 distinct types of spurious correlations extracted from real-world datasets, each containing 1 realistic and 10 synthetic VQA samples for a total of 1364 multiple choice questions. We evaluate 15 open and closed-source LVLMs on SpuriVerse, finding that even state-of-the-art closed-source models struggle significantly, achieving at best only 37.1% accuracy. Fine-tuning on synthetic examples that emphasize the spurious correlation improves performance to 78.40%, suggesting that training on diverse spurious patterns generalizes to unseen situations: models appear to learn to avoid "shortcuts" and attend to the overall image context.

</details>

### FOCUS: Unified Vision-Language Modeling for Interactive Editing Driven by Referential Segmentation.
- **链接**: [arXiv:2506.16806](https://arxiv.org/abs/2506.16806) · 📚 被引 0
- **作者**: Fan Yang, Yousong Zhu, Xin Li, Yufei Zhan, Hongyin Zhao, Shurong Zheng et al.
- **🏷️ 机构**: Research, Microsoft, China University of Mining Technology - Beijing, Pengcheng Laboratory
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent Large Vision Language Models (LVLMs) demonstrate promising capabilities in unifying visual understanding and generative modeling, enabling both accurate content understanding and flexible editing. However, current approaches treat "what to see" and "how to edit" separately: they either perform isolated object segmentation or utilize segmentation masks merely as conditional prompts for local edit generation tasks, often relying on multiple disjointed models. To bridge these gaps, we introduce FOCUS, a unified LVLM that integrates segmentation-aware perception and controllable object-centric generation within an end-to-end framework. FOCUS employs a dual-branch visual encoder to simultaneously capture global semantic context and fine-grained spatial details. In addition, we leverage a MoVQGAN-based visual tokenizer to produce discrete visual tokens that enhance generation quality. To enable accurate and controllable image editing, we propose a progressive multi-stage training pipeline, where segmentation masks are jointly optimized and used as spatial condition prompts to guide the diffusion decoder. This strategy aligns visual encoding, segmentation, and generation modules, effectively bridging segmentation-aware perception with fine-grained visual synthesis. Extensive experiments across three core tasks, including multimodal understanding, referring segmentation accuracy, and controllable image generation, demonstrate that FOCUS achieves strong performance by jointly optimizing visual perception and generative capabilities.

</details>

### SharpZO: Hybrid Sharpness-Aware Vision Language Model Prompt Tuning via Forward-Only Passes.
- **链接**: [arXiv:2506.20990](https://arxiv.org/abs/2506.20990) · 📚 被引 0
- **作者**: Yifan Yang, Zhen Zhang, Rupak Vignesh Swaminathan, Jing Liu, Nathan Susanj, Zheng Zhang
- **🏷️ 机构**: University of California, Santa Barbara, Nanjing University, Amazon
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-tuning vision language models (VLMs) has achieved remarkable performance across various downstream tasks; yet, it requires access to model gradients through backpropagation (BP), making them unsuitable for memory-constrained, inference-only edge devices. To address this limitation, previous work has explored various BP-free fine-tuning methods. However, these approaches often rely on high-variance evolutionary strategies (ES) or zeroth-order (ZO) optimization, and often fail to achieve satisfactory performance. In this paper, we propose a hybrid Sharpness-aware Zeroth-order optimization (SharpZO) approach, specifically designed to enhance the performance of ZO VLM fine-tuning via a sharpness-aware warm-up training. SharpZO features a two-stage optimization process: a sharpness-aware ES stage that globally explores and smooths the loss landscape to construct a strong initialization, followed by a fine-grained local search via sparse ZO optimization. The entire optimization relies solely on forward passes. Detailed theoretical analysis and extensive experiments on CLIP models demonstrate that SharpZO significantly improves accuracy and convergence speed, achieving up to 7% average gain over state-of-the-art forward-only methods.

</details>

### GoalLadder: Incremental Goal Discovery with Vision-Language Models.
- **链接**: [arXiv:2506.16396](https://arxiv.org/abs/2506.16396) · 📚 被引 0
- **作者**: Alexey Zakharov, Shimon Whiteson
- **🏷️ 机构**: Department of Computer Science, University of Oxford, University of Amsterdam
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Natural language can offer a concise and human-interpretable means of specifying reinforcement learning (RL) tasks. The ability to extract rewards from a language instruction can enable the development of robotic systems that can learn from human guidance; however, it remains a challenging problem, especially in visual environments. Existing approaches that employ large, pretrained language models either rely on non-visual environment representations, require prohibitively large amounts of feedback, or generate noisy, ill-shaped reward functions. In this paper, we propose a novel method, GoalLadder, that leverages vision-language models (VLMs) to train RL agents from a single language instruction in visual environments. GoalLadder works by incrementally discovering states that bring the agent closer to completing a task specified in natural language. To do so, it queries a VLM to identify states that represent an improvement in agent's task progress and to rank them using pairwise comparisons. Unlike prior work, GoalLadder does not trust VLM's feedback completely; instead, it uses it to rank potential goal states using an ELO-based rating system, thus reducing the detrimental effects of noisy VLM feedback. Over the course of training, the agent is tasked with minimising the distance to the top-ranked goal in a learned embedding space, which is trained on unlabelled visual data. This key feature allows us to bypass the need for abundant and accurate feedback typically required to train a well-shaped reward function. We demonstrate that GoalLadder outperforms existing related methods on classic control and robotic manipulation environments with the average final success rate of $\sim$95% compared to only $\sim$45% of the best competitor.

</details>

### CF-VLM: CounterFactual Vision-Language Fine-tuning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/541b6d155146d142a5e10d787d1d430f-Abstract-Conference.html)
- **作者**: Jusheng Zhang, Kaitong Cai, Yijia Fan, Jian Wang, Keze Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### From Flatland to Space: Teaching Vision-Language Models to Perceive and Reason in 3D.
- **链接**: [arXiv:2503.22976](https://arxiv.org/abs/2503.22976) · 📚 被引 0
- **作者**: Jiahui Zhang, Yurui Chen, Yueming Xu, Ze Huang, Jilin Mei, Junhui Chen et al.
- **🏷️ 机构**: Fudan University, Huawei Technologies Ltd.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in LVLMs have improved vision-language understanding, but they still struggle with spatial perception, limiting their ability to reason about complex 3D scenes. Unlike previous approaches that incorporate 3D representations into models to improve spatial understanding, we aim to unlock the potential of VLMs by leveraging spatially relevant image data. To this end, we introduce a novel 2D spatial data generation and annotation pipeline built upon scene data with 3D ground-truth. This pipeline enables the creation of a diverse set of spatial tasks, ranging from basic perception tasks to more complex reasoning tasks. Leveraging this pipeline, we construct SPAR-7M, a large-scale dataset generated from thousands of scenes across multiple public datasets. In addition, we introduce SPAR-Bench, a benchmark designed to offer a more comprehensive evaluation of spatial capabilities compared to existing spatial benchmarks, supporting both single-view and multi-view inputs. Training on both SPAR-7M and large-scale 2D datasets enables our models to achieve state-of-the-art performance on 2D spatial benchmarks. Further fine-tuning on 3D task-specific datasets yields competitive results, underscoring the effectiveness of our dataset in enhancing spatial reasoning.

</details>

### Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents.
- **链接**: [arXiv:2502.01218](https://arxiv.org/abs/2502.01218) · 📚 被引 0
- **作者**: Zhizhen Zhang, Lei Zhu, Zhen Fang, Zi Huang, Yadan Luo
- **🏷️ 机构**: The University of Queensland, The Hong Kong University of Science and Technology, University of Technology Sydney
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-training vision-language representations on human action videos has emerged as a promising approach to reduce reliance on large-scale expert demonstrations for training embodied agents. However, prior methods often employ time contrastive learning based on goal-reaching heuristics, progressively aligning language instructions from the initial to the final frame. This overemphasis on future frames can result in erroneous vision-language associations, as actions may terminate early or include irrelevant moments in the end. To address this issue, we propose Action Temporal Coherence Learning (AcTOL) to learn ordered and continuous vision-language representations without rigid goal-based constraint. AcTOL treats a video as a continuous trajectory where it (1) contrasts semantic differences between frames to reflect their natural ordering, and (2) imposes a local Brownian bridge constraint to ensure smooth transitions across intermediate frames. Extensive imitation learning experiments on both simulated and real robots show that the pretrained features significantly enhance downstream manipulation tasks with high robustness to different linguistic styles of instructions, offering a viable pathway toward generalized embodied agents.

</details>

### RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics.
- **链接**: [arXiv:2506.04308](https://arxiv.org/abs/2506.04308) · 📚 被引 2
- **作者**: Enshen Zhou, Jingkun An, Cheng Chi, Yi Han, Shanyu Rong, Chi Zhang et al.
- **🏷️ 机构**: Beihang University, Beijing Academy of Artificial Intelligence, Peking University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatial referring is a fundamental capability of embodied robots to interact with the 3D physical world. However, even with the powerful pretrained vision language models (VLMs), recent approaches are still not qualified to accurately understand the complex 3D scenes and dynamically reason about the instruction-indicated locations for interaction. To this end, we propose RoboRefer, a 3D-aware VLM that can first achieve precise spatial understanding by integrating a disentangled but dedicated depth encoder via supervised fine-tuning (SFT). Moreover, RoboRefer advances generalized multi-step spatial reasoning via reinforcement fine-tuning (RFT), with metric-sensitive process reward functions tailored for spatial referring tasks. To support SFT and RFT training, we introduce RefSpatial, a large-scale dataset of 20M QA pairs (2x prior), covering 31 spatial relations (vs. 15 prior) and supporting complex reasoning processes (up to 5 steps). In addition, we introduce RefSpatial-Bench, a challenging benchmark filling the gap in evaluating spatial referring with multi-step reasoning. Experiments show that SFT-trained RoboRefer achieves state-of-the-art spatial understanding, with an average success rate of 89.6%. RFT-trained RoboRefer further outperforms all other baselines by a large margin, even surpassing Gemini-2.5-Pro by 17.4% in average accuracy on RefSpatial-Bench. Notably, RoboRefer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (e,g., UR5, G1 humanoid) in cluttered real-world scenes.

</details>

### DrVD-Bench: Do Vision-Language Models Reason Like Human Doctors in Medical Image Diagnosis?
- **链接**: [arXiv:2505.24173](https://arxiv.org/abs/2505.24173) · 📚 被引 0
- **作者**: Tianhong Zhou, Yin Xu, Yingtao Zhu, Chuxi Xiao, Haiyang Bian, Lei Wei et al.
- **🏷️ 机构**: Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) exhibit strong zero-shot generalization on natural images and show early promise in interpretable medical image analysis. However, existing benchmarks do not systematically evaluate whether these models truly reason like human clinicians or merely imitate superficial patterns. To address this gap, we propose DrVD-Bench, the first multimodal benchmark for clinical visual reasoning. DrVD-Bench consists of three modules: Visual Evidence Comprehension, Reasoning Trajectory Assessment, and Report Generation Evaluation, comprising a total of 7,789 image-question pairs. Our benchmark covers 20 task types, 17 diagnostic categories, and five imaging modalities-CT, MRI, ultrasound, radiography, and pathology. DrVD-Bench is explicitly structured to reflect the clinical reasoning workflow from modality recognition to lesion identification and diagnosis. We benchmark 19 VLMs, including general-purpose and medical-specific, open-source and proprietary models, and observe that performance drops sharply as reasoning complexity increases. While some models begin to exhibit traces of human-like reasoning, they often still rely on shortcut correlations rather than grounded visual understanding. DrVD-Bench offers a rigorous and structured evaluation framework to guide the development of clinically trustworthy VLMs.

</details>

### Training-Free Test-Time Adaptation via Shape and Style Guidance for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e07ad202df8672e3cf9d0203d86f5a55-Abstract-Conference.html) · 📚 被引 0
- **作者**: Shenglong Zhou, Manjiang Yin, Leiyu Sun, Shicai Yang, Di Xie, Jiang Zhu
- **🏷️ 机构**: Hangzhou Hikvision Digital Technology Co., Ltd, University of Science and Technology of China, Xi'an University of Electronic Science and Technology
- **会议**: NeurIPS 2025

### Learning to Steer: Input-dependent Steering for Multimodal LLMs.
- **链接**: [arXiv:2508.12815](https://arxiv.org/abs/2508.12815) · 📚 被引 0
- **作者**: Jayneel Parekh, Pegah Khayatan, Mustafa Shukor, Arnaud Dapogny, Alasdair Newson, Matthieu Cord
- **🏷️ 机构**: ISIR, Sorbonne Université, Sorbonne Université - Faculté des Sciences (Paris VI), Sorbonne University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Steering has emerged as a practical approach to enable post-hoc guidance of LLMs towards enforcing a specific behavior. However, it remains largely underexplored for multimodal LLMs (MLLMs); furthermore, existing steering techniques, such as mean steering, rely on a single steering vector, applied independently of the input query. This paradigm faces limitations when the desired behavior is dependent on the example at hand. For example, a safe answer may consist in abstaining from answering when asked for an illegal activity, or may point to external resources or consultation with an expert when asked about medical advice. In this paper, we investigate a fine-grained steering that uses an input-specific linear shift. This shift is computed using contrastive input-specific prompting. However, the input-specific prompts required for this approach are not known at test time. Therefore, we propose to train a small auxiliary module to predict the input-specific steering vector. Our approach, dubbed as L2S (Learn-to-Steer), demonstrates that it reduces hallucinations and enforces safety in MLLMs, outperforming other static baselines. Our code is publicly available at https://jayneelparekh.github.io/learn-to-steer/

</details>

## 跨领域论文（完整笔记在其他领域）

- Roboflow100-VL: A Multi-Domain Object Detection Benchmark for Vision-Language Models. → [object-detection](../object-detection/Guideline%202025.md)
- MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- MLLM-ISU: The First-Ever Comprehensive Benchmark for Multimodal Large Language Models based Intrusion Scene Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- Hyperphantasia: A Benchmark for Evaluating the Mental Visualization Capabilities of Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- Test-Time Adaptation of Vision-Language Models for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- OpenHOI: Open-World Hand-Object Interaction Synthesis with Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- SURDS: Benchmarking Spatial Understanding and Reasoning in Driving Scenarios with Vision Language Models. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Glance2Gaze: Efficient Vision-Language Models from Glance Fusion to Gaze Compression. → [network-pruning](../network-pruning/Guideline%202025.md)
- VaMP: Variational Multi-Modal Prompt Learning for Vision-Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Balanced Token Pruning: Accelerating Vision Language Models Beyond Local Optimization. → [network-pruning](../network-pruning/Guideline%202025.md)
- AlignVLM: Bridging Vision and Language Latent Spaces for Multimodal Document Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- Toward a Vision-Language Foundation Model for Medical Data: Multimodal Dataset and Benchmarks for Vietnamese PET/CT Report Generation. → [multimodal](../multimodal/Guideline%202025.md)
- OOD-Barrier: Build a Middle-Barrier for Open-Set Single-Image Test Time Adaptation via Vision Language Models. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- QSVD: Efficient Low-rank Approximation for Unified Query-Key-Value Weight Compression in Low-Precision Vision-Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- ElasticMM: Efficient Multimodal LLMs Serving with Elastic Multimodal Parallelism. → [multimodal](../multimodal/Guideline%202025.md)
- Boosting Knowledge Utilization in Multimodal Large Language Models via Adaptive Logits Fusion and Attention Reallocation. → [multimodal](../multimodal/Guideline%202025.md)
- SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism. → [multimodal](../multimodal/Guideline%202025.md)
- Decoupling Contrastive Decoding: Robust Hallucination Mitigation in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- AnomalyCoT: A Multi-Scenario Chain-of-Thought Dataset for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- VLForgery Face Triad: Detection, Localization and Attribution via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
- Unlabeled Data Improves Fine-Grained Image Zero-shot Classification with Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting. → [multimodal](../multimodal/Guideline%202025.md)
- MLLM-For3D: Adapting Multimodal Large Language Model for 3D Reasoning Segmentation. → [multimodal](../multimodal/Guideline%202025.md)
- Elevating Visual Perception in Multimodal LLMs with Visual Embedding Distillation. → [multimodal](../multimodal/Guideline%202025.md)
- VLM-R³: Region Recognition, Reasoning, and Refinement for Enhanced Multimodal Chain-of-Thought. → [multimodal](../multimodal/Guideline%202025.md)
- See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- Watch and Listen: Understanding Audio-Visual-Speech Moments with Multimodal LLM. → [multimodal](../multimodal/Guideline%202025.md)
- SpaceServe: Spatial Multiplexing of Complementary Encoders and Decoders for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202025.md)
- Bifrost-1: Bridging Multimodal LLMs and Diffusion Models with Patch-level CLIP Latents. → [multimodal](../multimodal/Guideline%202025.md)
- ACT as Human: Multimodal Large Language Model Data Annotation with Critical Thinking. → [multimodal](../multimodal/Guideline%202025.md)
- On Fairness of Unified Multimodal Large Language Model for Image Generation. → [multimodal](../multimodal/Guideline%202025.md)
- ThinkSound: Chain-of-Thought Reasoning in Multimodal LLMs for Audio Generation and Editing. → [multimodal](../multimodal/Guideline%202025.md)
- Situat3DChange: Situated 3D Change Understanding Dataset for Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents. → [multimodal](../multimodal/Guideline%202025.md)
- MVU-Eval: Towards Multi-Video Understanding Evaluation for Multimodal LLMs. → [video-understanding](../video-understanding/Guideline%202025.md)
