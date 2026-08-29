# Multimodal — 2025 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 120 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Time-IMM: A Dataset and Benchmark for Irregular Multimodal Multivariate Time Series.
- **链接**: [arXiv:2506.10412](https://arxiv.org/abs/2506.10412) · [代码](https://github.com/blacksnail789521/Time-IMM) · 📚 被引 1
- **作者**: Ching Chang, Jeehyun Hwang, Yidan Shi, Haixin Wang, Wei Wang, Wen-Chih Peng et al.
- **🏷️ 机构**: University of California, Los Angeles, UCLA Computer Science Department, University of California, Los Angeles, UCLA
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Time series data in real-world applications such as healthcare, climate modeling, and finance are often irregular, multimodal, and messy, with varying sampling rates, asynchronous modalities, and pervasive missingness. However, existing benchmarks typically assume clean, regularly sampled, unimodal data, creating a significant gap between research and real-world deployment. We introduce Time-IMM, a dataset specifically designed to capture cause-driven irregularity in multimodal multivariate time series. Time-IMM represents nine distinct types of time series irregularity, categorized into trigger-based, constraint-based, and artifact-based mechanisms. Complementing the dataset, we introduce IMM-TSF, a benchmark library for forecasting on irregular multimodal time series, enabling asynchronous integration and realistic evaluation. IMM-TSF includes specialized fusion modules, including a timestamp-to-text fusion module and a multimodality fusion module, which support both recency-aware averaging and attention-based integration strategies. Empirical results demonstrate that explicitly modeling multimodality on irregular time series data leads to substantial gains in forecasting performance. Time-IMM and IMM-TSF provide a foundation for advancing time series analysis under real-world conditions. The dataset is publicly available at https://github.com/blacksnail789521/Time-IMM, and the benchmark library can be accessed at https://github.com/blacksnail789521/IMM-TSF. Project page: https://blacksnail789521.github.io/time-imm-project-page/

</details>

### MIRAGE: A Benchmark for Multimodal Information-Seeking and Reasoning in Agricultural Expert-Guided Conversations.
- **链接**: [arXiv:2506.20100](https://arxiv.org/abs/2506.20100) · 📚 被引 1
- **作者**: Vardhan Dongre, Chi Gui, Shubham Garg, Hooshang Nayyeri, Gokhan Tur, Dilek Hakkani-Tur et al.
- **🏷️ 机构**: University of Illinois Urbana Champaign, University of Illinois at Urbana-Champaign, Amazon
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MIRAGE, a new benchmark for multimodal expert-level reasoning and decision-making in consultative interaction settings. Designed for the agriculture domain, MIRAGE captures the full complexity of expert consultations by combining natural user queries, expert-authored responses, and image-based context, offering a high-fidelity benchmark for evaluating models on grounded reasoning, clarification strategies, and long-form generation in a real-world, knowledge-intensive domain. Grounded in over 35,000 real user-expert interactions and curated through a carefully designed multi-step pipeline, MIRAGE spans diverse crop health, pest diagnosis, and crop management scenarios. The benchmark includes more than 7,000 unique biological entities, covering plant species, pests, and diseases, making it one of the most taxonomically diverse benchmarks available for vision-language models, grounded in the real world. Unlike existing benchmarks that rely on well-specified user inputs and closed-set taxonomies, MIRAGE features underspecified, context-rich scenarios with open-world settings, requiring models to infer latent knowledge gaps, handle rare entities, and either proactively guide the interaction or respond. Project Page: https://mirage-benchmark.github.io

</details>

### MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d79a27cf2772fe00be7f341efc0eb517-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin, Mengdan Zhang, Xu Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### OCRBench v2: An Improved Benchmark for Evaluating Large Multimodal Models on Visual Text Localization and Reasoning.
- **链接**: [arXiv:2501.00321](https://arxiv.org/abs/2501.00321) · 📚 被引 7
- **作者**: Ling Fu, Zhebin Kuang, Jiajun Song, Mingxin Huang, Biao Yang, Yuzhe Li et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, South China University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scoring the Optical Character Recognition (OCR) capabilities of Large Multimodal Models (LMMs) has witnessed growing interest. Existing benchmarks have highlighted the impressive performance of LMMs in text recognition; however, their abilities in certain challenging tasks, such as text localization, handwritten content extraction, and logical reasoning, remain underexplored. To bridge this gap, we introduce OCRBench v2, a large-scale bilingual text-centric benchmark with currently the most comprehensive set of tasks (4x more tasks than the previous multi-scene benchmark OCRBench), the widest coverage of scenarios (31 diverse scenarios), and thorough evaluation metrics, with 10,000 human-verified question-answering pairs and a high proportion of difficult samples. Moreover, we construct a private test set with 1,500 manually annotated images. The consistent evaluation trends observed across both public and private test sets validate the OCRBench v2's reliability. After carefully benchmarking state-of-the-art LMMs, we find that most LMMs score below 50 (100 in total) and suffer from five-type limitations, including less frequently encountered text recognition, fine-grained perception, layout perception, complex element parsing, and logical reasoning. The project website is at: https://99franklin.github.io/ocrbench_v2/

</details>

### AgMMU: A Comprehensive Agricultural Multimodal Understanding Benchmark.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6d5e00006b65fcc55c3c1798da821663-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 2
- **作者**: Aruna Gauba, Irene Pi, Yunze Man, Ziqi Pang, Vikram S. Adve, Yu-Xiong Wang
- **🏷️ 机构**: Rice University, CMU, Carnegie Mellon University, Department of Computer Science, University of Illinois at Urbana-Champaign
- **会议**: NeurIPS 2025

### MLLM-ISU: The First-Ever Comprehensive Benchmark for Multimodal Large Language Models based Intrusion Scene Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9df0def8b762ed74e0f9d5aa9a164399-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Fujun Han, Peng Ye
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Towards Better Dental AI: A Multimodal Benchmark and Instruction Dataset for Panoramic X-ray Analysis.
- **链接**: [arXiv:2509.09254](https://arxiv.org/abs/2509.09254) · [代码](https://github.com/isbrycee/OralGPT) · 📚 被引 0
- **作者**: Jing Hao, Yuxuan Fan, Yanpeng Sun, Kaixin Guo, Lizhuo Lin, Jinrong Yang et al.
- **🏷️ 机构**: University of Hong Kong, The Hong Kong University of Science and Technology, Nanjing University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in large vision-language models (LVLMs) have demonstrated strong performance on general-purpose medical tasks. However, their effectiveness in specialized domains such as dentistry remains underexplored. In particular, panoramic X-rays, a widely used imaging modality in oral radiology, pose interpretative challenges due to dense anatomical structures and subtle pathological cues, which are not captured by existing medical benchmarks or instruction datasets. To this end, we introduce MMOral, the first large-scale multimodal instruction dataset and benchmark tailored for panoramic X-ray interpretation. MMOral consists of 20,563 annotated images paired with 1.3 million instruction-following instances across diverse task types, including attribute extraction, report generation, visual question answering, and image-grounded dialogue. In addition, we present MMOral-Bench, a comprehensive evaluation suite covering five key diagnostic dimensions in dentistry. We evaluate 64 LVLMs on MMOral-Bench and find that even the best-performing model, i.e., GPT-4o, only achieves 41.45% accuracy, revealing significant limitations of current models in this domain. To promote the progress of this specific domain, we also propose OralGPT, which conducts supervised fine-tuning (SFT) upon Qwen2.5-VL-7B with our meticulously curated MMOral instruction dataset. Remarkably, a single epoch of SFT yields substantial performance enhancements for LVLMs, e.g., OralGPT demonstrates a 24.73% improvement. Both MMOral and OralGPT hold significant potential as a critical foundation for intelligent dentistry and enable more clinically impactful multimodal AI systems in the dental field. The dataset, model, benchmark, and evaluation suite are available at https://github.com/isbrycee/OralGPT.

</details>

### A Multimodal Benchmark for Framing of Oil & Gas Advertising and Potential Greenwashing Detection.
- **链接**: [arXiv:2510.21679](https://arxiv.org/abs/2510.21679) · 📚 被引 0
- **作者**: Gaku Morio, Harri Rowlands, Dominik Stammbach, Christopher D. Manning, Peter Henderson
- **🏷️ 机构**: Hitachi, CAST, Princeton University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Companies spend large amounts of money on public relations campaigns to project a positive brand image. However, sometimes there is a mismatch between what they say and what they do. Oil & gas companies, for example, are accused of "greenwashing" with imagery of climate-friendly initiatives. Understanding the framing, and changes in framing, at scale can help better understand the goals and nature of public relations campaigns. To address this, we introduce a benchmark dataset of expert-annotated video ads obtained from Facebook and YouTube. The dataset provides annotations for 13 framing types for more than 50 companies or advocacy groups across 20 countries. Our dataset is especially designed for the evaluation of vision-language models (VLMs), distinguishing it from past text-only framing datasets. Baseline experiments show some promising results, while leaving room for improvement for future work: GPT-4.1 can detect environmental messages with 79% F1 score, while our best model only achieves 46% F1 score on identifying framing around green innovation. We also identify challenges that VLMs must address, such as implicit framing, handling videos of various lengths, or implicit cultural backgrounds. Our dataset contributes to research in multimodal analysis of strategic communication in the energy sector.

</details>

### SMMILE: An expert-driven benchmark for multimodal medical in-context learning.
- **链接**: [arXiv:2506.21355](https://arxiv.org/abs/2506.21355) · 📚 被引 0
- **作者**: Melanie Rieff, Maya Varma, Ossian Rabow, Subathra Adithan, Julie Kim, Ken Chang et al.
- **🏷️ 机构**: ETHZ - ETH Zurich, Stanford University, Jawaharlal Institute of Postgraduate Medical Education and Research (JIPMER)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal in-context learning (ICL) remains underexplored despite significant potential for domains such as medicine. Clinicians routinely encounter diverse, specialized tasks requiring adaptation from limited examples, such as drawing insights from a few relevant prior cases or considering a constrained set of differential diagnoses. While multimodal large language models (MLLMs) have shown advances in medical visual question answering (VQA), their ability to learn multimodal tasks from context is largely unknown. We introduce SMMILE, the first expert-driven multimodal ICL benchmark for medical tasks. Eleven medical experts curated problems, each including a multimodal query and multimodal in-context examples as task demonstrations. SMMILE encompasses 111 problems (517 question-image-answer triplets) covering 6 medical specialties and 13 imaging modalities. We further introduce SMMILE++, an augmented variant with 1038 permuted problems. A comprehensive evaluation of 15 MLLMs demonstrates that most models exhibit moderate to poor multimodal ICL ability in medical tasks. In open-ended evaluations, ICL contributes only an 8% average improvement over zero-shot on SMMILE and 9.4% on SMMILE++. We observe a susceptibility for irrelevant in-context examples: even a single noisy or irrelevant example can degrade performance by up to 9.5%. Moreover, we observe that MLLMs are affected by a recency bias, where placing the most relevant example last can lead to substantial performance improvements of up to 71%. Our findings highlight critical limitations and biases in current MLLMs when learning multimodal medical tasks from context. SMMILE is available at https://smmile-benchmark.github.io.

</details>

### Hyperphantasia: A Benchmark for Evaluating the Mental Visualization Capabilities of Multimodal LLMs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/05a7ad45d75a3082d7a3a70de8743140-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Mohammad Shahab Sepehri, Berk Tinaz, Zalan Fabian, Mahdi Soltanolkotabi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### MTBBench: A Multimodal Sequential Clinical Decision-Making Benchmark in Oncology.
- **链接**: [arXiv:2511.20490](https://arxiv.org/abs/2511.20490) · 📚 被引 0
- **作者**: Kiril Vasilev, Alexandre Misrahi, Eeshaan Jain, Phil F. Cheng, Petros Liakopoulos, Olivier Michielin et al.
- **🏷️ 机构**: ETHZ - ETH Zurich, EPFL - EPF Lausanne, EPFL
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (LLMs) hold promise for biomedical reasoning, but current benchmarks fail to capture the complexity of real-world clinical workflows. Existing evaluations primarily assess unimodal, decontextualized question-answering, overlooking multi-agent decision-making environments such as Molecular Tumor Boards (MTBs). MTBs bring together diverse experts in oncology, where diagnostic and prognostic tasks require integrating heterogeneous data and evolving insights over time. Current benchmarks lack this longitudinal and multimodal complexity. We introduce MTBBench, an agentic benchmark simulating MTB-style decision-making through clinically challenging, multimodal, and longitudinal oncology questions. Ground truth annotations are validated by clinicians via a co-developed app, ensuring clinical relevance. We benchmark multiple open and closed-source LLMs and show that, even at scale, they lack reliability -- frequently hallucinating, struggling with reasoning from time-resolved data, and failing to reconcile conflicting evidence or different modalities. To address these limitations, MTBBench goes beyond benchmarking by providing an agentic framework with foundation model-based tools that enhance multi-modal and longitudinal reasoning, leading to task-level performance gains of up to 9.0% and 11.2%, respectively. Overall, MTBBench offers a challenging and realistic testbed for advancing multimodal LLM reasoning, reliability, and tool-use with a focus on MTB environments in precision oncology.

</details>

### InfoChartQA: A Benchmark for Multimodal Question Answering on Infographic Charts.
- **链接**: [arXiv:2505.19028](https://arxiv.org/abs/2505.19028) · [代码](https://github.com/CoolDawnAnt/InfoChartQA) · 📚 被引 0
- **作者**: Tianchi Xie, Minzhi Lin, Mengchen Liu, Yilin Ye, Changjian Chen, Shixia Liu
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Hong Kong University of Science and Technology, Hunan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding infographic charts with design-driven visual elements (e.g., pictograms, icons) requires both visual recognition and reasoning, posing challenges for multimodal large language models (MLLMs). However, existing visual-question answering benchmarks fall short in evaluating these capabilities of MLLMs due to the lack of paired plain charts and visual-element-based questions. To bridge this gap, we introduce InfoChartQA, a benchmark for evaluating MLLMs on infographic chart understanding. It includes 5,642 pairs of infographic and plain charts, each sharing the same underlying data but differing in visual presentations. We further design visual-element-based questions to capture their unique visual designs and communicative intent. Evaluation of 20 MLLMs reveals a substantial performance decline on infographic charts, particularly for visual-element-based questions related to metaphors. The paired infographic and plain charts enable fine-grained error analysis and ablation studies, which highlight new opportunities for advancing MLLMs in infographic chart understanding. We release InfoChartQA at https://github.com/CoolDawnAnt/InfoChartQA.

</details>

### TCM-Ladder: A Benchmark for Multimodal Question Answering on Traditional Chinese Medicine.
- **链接**: [arXiv:2505.24063](https://arxiv.org/abs/2505.24063) · 📚 被引 0
- **作者**: Jiacheng Xie, Yang Yu, Ziyang Zhang, Shuai Zeng, Jiaxuan He, Ayush Vasireddy et al.
- **🏷️ 机构**: University of Missouri, Nanjing University, Northwestern University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional Chinese Medicine (TCM), as an effective alternative medicine, has been receiving increasing attention. In recent years, the rapid development of large language models (LLMs) tailored for TCM has highlighted the urgent need for an objective and comprehensive evaluation framework to assess their performance on real-world tasks. However, existing evaluation datasets are limited in scope and primarily text-based, lacking a unified and standardized multimodal question-answering (QA) benchmark. To address this issue, we introduce TCM-Ladder, the first comprehensive multimodal QA dataset specifically designed for evaluating large TCM language models. The dataset covers multiple core disciplines of TCM, including fundamental theory, diagnostics, herbal formulas, internal medicine, surgery, pharmacognosy, and pediatrics. In addition to textual content, TCM-Ladder incorporates various modalities such as images and videos. The dataset was constructed using a combination of automated and manual filtering processes and comprises over 52,000 questions. These questions include single-choice, multiple-choice, fill-in-the-blank, diagnostic dialogue, and visual comprehension tasks. We trained a reasoning model on TCM-Ladder and conducted comparative experiments against nine state-of-the-art general domain and five leading TCM-specific LLMs to evaluate their performance on the dataset. Moreover, we propose Ladder-Score, an evaluation method specifically designed for TCM question answering that effectively assesses answer quality in terms of terminology usage and semantic expression. To the best of our knowledge, this is the first work to systematically evaluate mainstream general domain and TCM-specific LLMs on a unified multimodal benchmark. The datasets and leaderboard are publicly available at https://tcmladder.com and will be continuously updated.

</details>

### Can Large Language Models Help Multimodal Language Analysis? MMLA: A Comprehensive Benchmark.
- **链接**: [arXiv:2504.16427](https://arxiv.org/abs/2504.16427) · [代码](https://github.com/thuiar/MMLA) · 📚 被引 0
- **作者**: Hanlei Zhang, Zhuohang Li, Hua Xu, Yeshuang Zhu, Peiwu Wang, Haige Zhu et al.
- **🏷️ 机构**: Tsinghua University, Tencent Inc., Hebei University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal language analysis is a rapidly evolving field that leverages multiple modalities to enhance the understanding of high-level semantics underlying human conversational utterances. Despite its significance, little research has investigated the capability of multimodal large language models (MLLMs) to comprehend cognitive-level semantics. In this paper, we introduce MMLA, a comprehensive benchmark specifically designed to address this gap. MMLA comprises over 61K multimodal utterances drawn from both staged and real-world scenarios, covering six core dimensions of multimodal semantics: intent, emotion, dialogue act, sentiment, speaking style, and communication behavior. We evaluate eight mainstream branches of LLMs and MLLMs using three methods: zero-shot inference, supervised fine-tuning, and instruction tuning. Extensive experiments reveal that even fine-tuned models achieve only about 60%~70% accuracy, underscoring the limitations of current MLLMs in understanding complex human language. We believe that MMLA will serve as a solid foundation for exploring the potential of large language models in multimodal language analysis and provide valuable resources to advance this field. The datasets and code are open-sourced at https://github.com/thuiar/MMLA.

</details>

### Multimodal Causal Reasoning for UAV Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f5a24b8fa97f7073aff5e8baadf583f1-Abstract-Conference.html) · 📚 被引 0
- **作者**: Nianxin Li, Mao Ye, Lihua Zhou, Shuaifeng Li, Song Tang, Luping Ji et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, School of Computer Science and Engineering, University of Electronic Science and Technology of China, University of Shanghai for Science and Technology
- **会议**: NeurIPS 2025

### InstructHOI: Context-Aware Instruction for Multi-Modal Reasoning in Human-Object Interaction Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d1d7398c1444928ada8940f369665ad5-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jinguo Luo, Weihong Ren, Quanlong Zheng, Yanhao Zhang, Zhenlong Yuan, Zhiyong Wang et al.
- **🏷️ 机构**: Harbin Institute of Technology, Shenzhen, Guangdong OPPO Mobile Telecommunications Corp.,Ltd., Oppo AI center
- **会议**: NeurIPS 2025

### Multimodal LiDAR-Camera Novel View Synthesis with Unified Pose-free Neural Fields.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/70915b08a205ea5522528690d93518f6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weiyi Xue, Fan Lu, Yunwei Zhu, Zehan Zheng, Sanqing Qu, Jiangtong Li et al.
- **🏷️ 机构**: Tongji University, Johns Hopkins University, CNNC
- **会议**: NeurIPS 2025

### PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning.
- **链接**: [arXiv:2510.20406](https://arxiv.org/abs/2510.20406) · 📚 被引 0
- **作者**: Xiaogang Jia, Qian Wang, Anrui Wang, Han A. Wang, Balázs Gyenes, Emiliyan Gospodinov et al.
- **🏷️ 机构**: Karlsruhe Institute of Technology, Karlsruher Institut für Technologie, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robotic manipulation systems benefit from complementary sensing modalities, where each provides unique environmental information. Point clouds capture detailed geometric structure, while RGB images provide rich semantic context. Current point cloud methods struggle to capture fine-grained detail, especially for complex tasks, which RGB methods lack geometric awareness, which hinders their precision and generalization. We introduce PointMapPolicy, a novel approach that conditions diffusion policies on structured grids of points without downsampling. The resulting data type makes it easier to extract shape and spatial relationships from observations, and can be transformed between reference frames. Yet due to their structure in a regular grid, we enable the use of established computer vision techniques directly to 3D data. Using xLSTM as a backbone, our model efficiently fuses the point maps with RGB data for enhanced multi-modal perception. Through extensive experiments on the RoboCasa and CALVIN benchmarks and real robot evaluations, we demonstrate that our method achieves state-of-the-art performance across diverse manipulation tasks. The overview and demos are available on our project page: https://point-map.github.io/Point-Map/

</details>

### Multi-Modal View Enhanced Large Vision Models for Long-Term Time Series Forecasting.
- **链接**: [arXiv:2505.24003](https://arxiv.org/abs/2505.24003) · [代码](https://github.com/D2I-Group/dmmv) · 📚 被引 1
- **作者**: ChengAo Shen, Wenchao Yu, Ziming Zhao, Dongjin Song, Wei Cheng, Haifeng Chen et al.
- **🏷️ 机构**: University of Houston, NEC Laboratories America, University of Connecticut
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Time series, typically represented as numerical sequences, can also be transformed into images and texts, offering multi-modal views (MMVs) of the same underlying signal. These MMVs can reveal complementary patterns and enable the use of powerful pre-trained large models, such as large vision models (LVMs), for long-term time series forecasting (LTSF). However, as we identified in this work, the state-of-the-art (SOTA) LVM-based forecaster poses an inductive bias towards "forecasting periods". To harness this bias, we propose DMMV, a novel decomposition-based multi-modal view framework that leverages trend-seasonal decomposition and a novel backcast-residual based adaptive decomposition to integrate MMVs for LTSF. Comparative evaluations against 14 SOTA models across diverse datasets show that DMMV outperforms single-view and existing multi-modal baselines, achieving the best mean squared error (MSE) on 6 out of 8 benchmark datasets. The code for this paper is available at: https://github.com/D2I-Group/dmmv.

</details>

### Collaborating Vision, Depth, and Thermal Signals for Multi-Modal Tracking: Dataset and Algorithm.
- **链接**: [arXiv:2509.24741](https://arxiv.org/abs/2509.24741) · 📚 被引 0
- **作者**: Xuefeng Zhu, Tianyang Xu, Yifan Pan, Jinjie Gu, Xi Li, Jiwen Lu et al.
- **🏷️ 机构**: Jiangnan University, Zhejiang University, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing multi-modal object tracking approaches primarily focus on dual-modal paradigms, such as RGB-Depth or RGB-Thermal, yet remain challenged in complex scenarios due to limited input modalities. To address this gap, this work introduces a novel multi-modal tracking task that leverages three complementary modalities, including visible RGB, Depth (D), and Thermal Infrared (TIR), aiming to enhance robustness in complex scenarios. To support this task, we construct a new multi-modal tracking dataset, coined RGBDT500, which consists of 500 videos with synchronised frames across the three modalities. Each frame provides spatially aligned RGB, depth, and thermal infrared images with precise object bounding box annotations. Furthermore, we propose a novel multi-modal tracker, dubbed RDTTrack. RDTTrack integrates tri-modal information for robust tracking by leveraging a pretrained RGB-only tracking model and prompt learning techniques. In specific, RDTTrack fuses thermal infrared and depth modalities under a proposed orthogonal projection constraint, then integrates them with RGB signals as prompts for the pre-trained foundation tracking model, effectively harmonising tri-modal complementary cues. The experimental results demonstrate the effectiveness and advantages of the proposed method, showing significant improvements over existing dual-modal approaches in terms of tracking accuracy and robustness in complex scenarios. The dataset and source code are publicly available at https://xuefeng-zhu5.github.io/RGBDT500.

</details>

### OpenHOI: Open-World Hand-Object Interaction Synthesis with Multimodal Large Language Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f376f5dff6f6ec6364aea7a46ab49574-Abstract-Conference.html)
- **作者**: Zhenhao Zhang, Ye Shi, Lingxiao Yang, Suting Ni, Qi Ye, Jingya Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis.
- **链接**: [arXiv:2506.04217](https://arxiv.org/abs/2506.04217) · [代码](https://github.com/HHYHRHY/OWMM-Agent) · 📚 被引 0
- **作者**: Junting Chen, Haotian Liang, Lingxiao Du, Weiyun Wang, Mengkang Hu, Yao Mu et al.
- **🏷️ 机构**: School of Computer Science,            National University of Singapore, University of Science and Technology of China, Fudan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid progress of navigation, manipulation, and vision models has made mobile manipulators capable in many specialized tasks. However, the open-world mobile manipulation (OWMM) task remains a challenge due to the need for generalization to open-ended instructions and environments, as well as the systematic complexity to integrate high-level decision making with low-level robot control based on both global scene understanding and current agent state. To address this complexity, we propose a novel multi-modal agent architecture that maintains multi-view scene frames and agent states for decision-making and controls the robot by function calling. A second challenge is the hallucination from domain shift. To enhance the agent performance, we further introduce an agentic data synthesis pipeline for the OWMM task to adapt the VLM model to our task domain with instruction fine-tuning. We highlight our fine-tuned OWMM-VLM as the first dedicated foundation model for mobile manipulators with global scene understanding, robot state tracking, and multi-modal action generation in a unified model. Through experiments, we demonstrate that our model achieves SOTA performance compared to other foundation models including GPT-4o and strong zero-shot generalization in real world. The project page is at https://github.com/HHYHRHY/OWMM-Agent

</details>

### Genesis: Multimodal Driving Scene Generation with Spatio-Temporal and Cross-Modal Consistency.
- **链接**: [arXiv:2506.07497](https://arxiv.org/abs/2506.07497) · 📚 被引 0
- **作者**: Xiangyu Guo, Zhanqian Wu, Kaixin Xiong, Ziyang Xu, Lijun Zhou, Gangwei Xu et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, University of Pennsylvania, Xiaomi Corporation
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Genesis, a unified framework for joint generation of multi-view driving videos and LiDAR sequences with spatio-temporal and cross-modal consistency. Genesis employs a two-stage architecture that integrates a DiT-based video diffusion model with 3D-VAE encoding, and a BEV-aware LiDAR generator with NeRF-based rendering and adaptive sampling. Both modalities are directly coupled through a shared latent space, enabling coherent evolution across visual and geometric domains. To guide the generation with structured semantics, we introduce DataCrafter, a captioning module built on vision-language models that provides scene-level and instance-level supervision. Extensive experiments on the nuScenes benchmark demonstrate that Genesis achieves state-of-the-art performance across video and LiDAR metrics (FVD 16.95, FID 4.24, Chamfer 0.611), and benefits downstream tasks including segmentation and 3D detection, validating the semantic fidelity and practical utility of the generated data.

</details>

### VaMP: Variational Multi-Modal Prompt Learning for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/812e3f4ff9877b318689a22d81172cf3-Abstract-Conference.html)
- **作者**: Silin Cheng, Kai Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Analyzing Fine-Grained Alignment and Enhancing Vision Understanding in Multimodal Language Models.
- **链接**: [arXiv:2505.17316](https://arxiv.org/abs/2505.17316) · 📚 被引 0
- **作者**: Jiachen Jiang, Jinxin Zhou, Bo Peng, Xia Ning, Zhihui Zhu
- **🏷️ 机构**: Ohio State University, Columbus, Shanghai Jiaotong University, The Ohio State University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Achieving better alignment between vision embeddings and Large Language Models (LLMs) is crucial for enhancing the abilities of Multimodal LLMs (MLLMs), particularly for recent models that rely on powerful pretrained vision encoders and LLMs. A common approach to connect the pretrained vision encoder and LLM is through a projector applied after the vision encoder. However, the projector is often trained to enable the LLM to generate captions, and hence the mechanism by which LLMs understand each vision token remains unclear. In this work, we first investigate the role of the projector in compressing vision embeddings and aligning them with word embeddings. We show that the projector significantly compresses visual information, removing redundant details while preserving essential elements necessary for the LLM to understand visual content. We then examine patch-level alignment -- the alignment between each vision patch and its corresponding semantic words -- and propose a *multi-semantic alignment hypothesis*. Our analysis indicates that the projector trained by caption loss improves patch-level alignment but only to a limited extent, resulting in weak and coarse alignment. To address this issue, we propose *patch-aligned training* to efficiently enhance patch-level alignment. Our experiments show that patch-aligned training (1) achieves stronger compression capability and improved patch-level alignment, enabling the MLLM to generate higher-quality captions, (2) improves the MLLM's performance by 16% on referring expression grounding tasks, 4% on question-answering tasks, and 3% on modern instruction-following benchmarks when using the same supervised fine-tuning (SFT) setting. The proposed method can be easily extended to other multimodal models.

</details>

### Cross-modal Associations in Vision and Language Models: Revisiting the Bouba-Kiki Effect.
- **链接**: [arXiv:2507.10013](https://arxiv.org/abs/2507.10013) · 📚 被引 0
- **作者**: Tom Kouwenhoven, Kiana Shahrasbi, Tessa Verhoef
- **🏷️ 机构**: Leiden University, Leiden Institute of Advanced Computer Science, Leiden University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in multimodal models have raised questions about whether vision-and-language models (VLMs) integrate cross-modal information in ways that reflect human cognition. One well-studied test case in this domain is the bouba-kiki effect, where humans reliably associate pseudowords like `bouba' with round shapes and `kiki' with jagged ones. Given the mixed evidence found in prior studies for this effect in VLMs, we present a comprehensive re-evaluation focused on two variants of CLIP, ResNet and Vision Transformer (ViT), given their centrality in many state-of-the-art VLMs. We apply two complementary methods closely modelled after human experiments: a prompt-based evaluation that uses probabilities as a measure of model preference, and we use Grad-CAM as a novel approach to interpret visual attention in shape-word matching tasks. Our findings show that these model variants do not consistently exhibit the bouba-kiki effect. While ResNet shows a preference for round shapes, overall performance across both model variants lacks the expected associations. Moreover, direct comparison with prior human data on the same task shows that the models' responses fall markedly short of the robust, modality-integrated behaviour characteristic of human cognition. These results contribute to the ongoing debate about the extent to which VLMs truly understand cross-modal concepts, highlighting limitations in their internal representations and alignment with human intuitions.

</details>

### DetectiumFire: A Comprehensive Multi-modal Dataset Bridging Vision and Language for Fire Understanding.
- **链接**: [arXiv:2511.02495](https://arxiv.org/abs/2511.02495) · 📚 被引 0
- **作者**: Zixuan Liu, Siavash H. Khajavi, Guangkai Jiang
- **🏷️ 机构**: Tulane University, Aalto University, University of Helsinki
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in multi-modal models have demonstrated strong performance in tasks such as image generation and reasoning. However, applying these models to the fire domain remains challenging due to the lack of publicly available datasets with high-quality fire domain annotations. To address this gap, we introduce DetectiumFire, a large-scale, multi-modal dataset comprising of 22.5k high-resolution fire-related images and 2.5k real-world fire-related videos covering a wide range of fire types, environments, and risk levels. The data are annotated with both traditional computer vision labels (e.g., bounding boxes) and detailed textual prompts describing the scene, enabling applications such as synthetic data generation and fire risk reasoning. DetectiumFire offers clear advantages over existing benchmarks in scale, diversity, and data quality, significantly reducing redundancy and enhancing coverage of real-world scenarios. We validate the utility of DetectiumFire across multiple tasks, including object detection, diffusion-based image generation, and vision-language reasoning. Our results highlight the potential of this dataset to advance fire-related research and support the development of intelligent safety systems. We release DetectiumFire to promote broader exploration of fire understanding in the AI community. The dataset is available at https://kaggle.com/datasets/38b79c344bdfc55d1eed3d22fbaa9c31fad45e27edbbe9e3c529d6e5c4f93890

</details>

### AlignVLM: Bridging Vision and Language Latent Spaces for Multimodal Document Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d695f1d2b37df1310f3b9d2bbc7e0a2f-Abstract-Conference.html)
- **作者**: Ahmed Masry, Juan A. Rodríguez, Tianyu Zhang, Suyuchen Wang, Chao Wang, Aarash Feizi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Toward a Vision-Language Foundation Model for Medical Data: Multimodal Dataset and Benchmarks for Vietnamese PET/CT Report Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a9f5ebadfbf7b6b10d685c385713b35a-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Huu Tien Nguyen, Dac Thai Nguyen, The Minh Duc Nguyen, Trung Thanh Nguyen, Truong Thao Nguyen, Hieu H. Pham et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### ElasticMM: Efficient Multimodal LLMs Serving with Elastic Multimodal Parallelism.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/87726969ce38e9a676ca1fd4459ba77d-Abstract-Conference.html)
- **作者**: Zedong Liu, Shenggan Cheng, Guangming Tan, Yang You, Dingwen Tao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1add4b4f8373c64504cfe4a3054700a1-Abstract-Conference.html) · 📚 被引 0
- **作者**: Lukas Aichberger, Alasdair Paren, Guohao Li, Philip H. S. Torr, Yarin Gal, Adel Bibi
- **🏷️ 机构**: ELLIS / University Linz / University of Oxford, University of Oxford, Eigent.AI / CAMEL-AI.org
- **会议**: NeurIPS 2025

### Learning to Route: Per-Sample Adaptive Routing for Multimodal Multitask Prediction.
- **链接**: [arXiv:2509.12227](https://arxiv.org/abs/2509.12227) · 📚 被引 1
- **作者**: Marzieh Ajirak, Oded Bein, Ellen Rose Bowen, Dora Kanellopoulos, Avital Falk, Faith M. Gunning et al.
- **🏷️ 机构**: Cornell University, Weill Cornell, University of Michigan Medical School
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a unified framework for adaptive routing in multitask, multimodal prediction settings where data heterogeneity and task interactions vary across samples. Motivated by applications in psychotherapy where structured assessments and unstructured clinician notes coexist with partially missing data and correlated outcomes, we introduce a routing-based architecture that dynamically selects modality processing pathways and task-sharing strategies on a per-sample basis. Our model defines multiple modality paths, including raw and fused representations of text and numeric features and learns to route each input through the most informative expert combination. Task-specific predictions are produced by shared or independent heads depending on the routing decision, and the entire system is trained end-to-end. We evaluate the model on both synthetic data and real-world psychotherapy notes predicting depression and anxiety outcomes. Our experiments show that our method consistently outperforms fixed multitask or single-task baselines, and that the learned routing policy provides interpretable insights into modality relevance and task structure. This addresses critical challenges in personalized healthcare by enabling per-subject adaptive information processing that accounts for data heterogeneity and task correlations. Applied to psychotherapy, this framework could improve mental health outcomes, enhance treatment assignment precision, and increase clinical cost-effectiveness through personalized intervention strategies.

</details>

### Recursive Inference Scaling: A Winning Path to Scalable Inference in Language and Multimodal Systems.
- **链接**: [arXiv:2502.07503](https://arxiv.org/abs/2502.07503) · 📚 被引 0
- **作者**: Ibrahim Alabdulmohsin, Xiaohua Zhai
- **🏷️ 机构**: Google Deepmind, Google DeepMind
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inspired by recent findings on the fractal geometry of language, we introduce Recursive INference Scaling (RINS) as a complementary, plug-in recipe for scaling inference time in language and multimodal systems. RINS is a particular form of recursive depth that significantly outperforms +55 other variants, including the recent "repeat-all-over" (RAO) strategy in Mobile LLM (Liu et al., 2024) and latent recurrent thinking (Geiping et al., 2025). Unlike prior works, we carry out our comparisons on a compute-matched regime, and demonstrate that for a fixed model size and training compute budget, RINS substantially improves language modeling performance. It also generalizes beyond pure language tasks, delivering gains in multimodal systems, including a +2% improvement in 0-shot ImageNet accuracy for SigLIP-B/16. Additionally, by deriving data scaling laws, we show that RINS improves both the asymptotic performance limits and the scaling exponents. More importantly, with light-weight (linear) adapters (comprising <1% of model parameters) and stochastic dropout, RINS offers a no-regret strategy, meaning that RINS-enabled pretraining improves performance in language modeling even when recursive depth is not applied at inference time. This corresponds to improving performance on a training compute-, parameter-, and inference-matched regime, suggesting its potential as a viable component of LLM pretraining!

</details>

### Boosting Knowledge Utilization in Multimodal Large Language Models via Adaptive Logits Fusion and Attention Reallocation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html)
- **作者**: Wenbin An, Jiahao Nie, Feng Tian, Haonan Lin, Mingxiang Cai, Yaqiang Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Hallucination at a Glance: Controlled Visual Edits and Fine-Grained Multimodal Learning.
- **链接**: [arXiv:2506.07227](https://arxiv.org/abs/2506.07227) · 📚 被引 0
- **作者**: Tianyi Bai, Yuxuan Fan, Jiantao Qiu, Fupeng Sun, Jiayi Song, Junlin Han et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, shanghai AI lab, Imperial College London
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have achieved strong performance on vision-language tasks but still struggle with fine-grained visual differences, leading to hallucinations or missed semantic shifts. We attribute this to limitations in both training data and learning objectives. To address these issues, we propose a controlled data generation pipeline that produces minimally edited image pairs with semantically aligned captions. Using this pipeline, we construct the Micro Edit Dataset (MED), containing over 50K image-text pairs spanning 11 fine-grained edit categories, including attribute, count, position, and object presence changes. Building on MED, we introduce a supervised fine-tuning (SFT) framework with a feature-level consistency loss that promotes stable visual embeddings under small edits. We evaluate our approach on the Micro Edit Detection benchmark, which includes carefully balanced evaluation pairs designed to test sensitivity to subtle visual variations across the same edit categories. Our method improves difference detection accuracy and reduces hallucinations compared to strong baselines, including GPT-4o. Moreover, it yields consistent gains on standard vision-language tasks such as image captioning and visual question answering. These results demonstrate the effectiveness of combining targeted data and alignment objectives for enhancing fine-grained visual reasoning in MLLMs.

</details>

### Head Pursuit: Probing Attention Specialization in Multimodal Transformers.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a30e060cde25f9c1e73924d2f996542f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Lorenzo Basile, Valentino Maiorca, Diego Doimo, Francesco Locatello, Alberto Cazzaniga
- **🏷️ 机构**: Area Science Park  Trieste, Institute of Science and Technology Austria, Area Science Park Trieste, Italy
- **会议**: NeurIPS 2025

### PARTONOMY: Large Multimodal Models with Part-Level Visual Understanding.
- **链接**: [arXiv:2505.20759](https://arxiv.org/abs/2505.20759) · 📚 被引 0
- **作者**: Ansel Blume, Jeonghwan Kim, Hyeonjeong Ha, Elen Chatikyan, Xiaomeng Jin, Khanh Duy Nguyen et al.
- **🏷️ 机构**: University of Illinois Urbana Champaign, University of Illinois Urbana-Champaign (UIUC), Department of Computer Science, University of Illinois at Urbana-Champaign
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world objects are composed of distinctive, object-specific parts. Identifying these parts is key to performing fine-grained, compositional reasoning-yet, large multimodal models (LMMs) struggle to perform this seemingly straightforward task. In this work, we introduce PARTONOMY, an LMM benchmark designed for pixel-level part grounding. We construct PARTONOMY from existing part datasets and our own rigorously annotated set of images, encompassing 862 part labels and 534 object labels for evaluation. Unlike existing datasets that simply ask models to identify generic parts, PARTONOMY uses specialized concepts (e.g., agricultural airplane), and challenges models to compare objects' parts, consider part-whole relationships, and justify textual predictions with visual segmentations. Our experiments demonstrate significant limitations in state-of-the-art LMMs (e.g., LISA-13B achieves only 5.9% gIoU), highlighting a critical gap in their part grounding abilities. We note that existing segmentation-enabled LMMs (segmenting LMMs) have two key architectural shortcomings: they use special [SEG] tokens not seen during pretraining which induce distribution shift, and they discard predicted segmentations instead of using past predictions to guide future ones. To address these deficiencies, we train several part-centric LMMs and propose PLUM, a novel segmenting LMM that uses span tagging instead of segmentation tokens and that conditions on prior predictions in a feedback loop. We find that pretrained PLUM outperforms existing segmenting LMMs on reasoning segmentation, VQA, and visual hallucination benchmarks. In addition, PLUM finetuned on our proposed Explanatory Part Segmentation task is competitive with segmenting LMMs trained on significantly more segmentation data. Our work opens up new avenues towards enabling fine-grained, grounded visual understanding in LMMs.

</details>

### On the Value of Cross-Modal Misalignment in Multimodal Representation Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d6c06b4cab132aaade78d4d4d930b9c8-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yichao Cai, Yuhang Liu, Erdun Gao, Tianjiao Jiang, Zhen Zhang, Anton van den Hengel et al.
- **🏷️ 机构**: AIML, University of Adelaide, The University of Adelaide, University of Adelaide
- **会议**: NeurIPS 2025

### OmniVCus: Feedforward Subject-driven Video Customization with Multimodal Control Conditions.
- **链接**: [arXiv:2506.23361](https://arxiv.org/abs/2506.23361) · [代码](https://github.com/caiyuanhao1998/Open-OmniVCus) · 📚 被引 0
- **作者**: Yuanhao Cai, He Zhang, Xi Chen, Jinbo Xing, Yiwei Hu, Yuqian Zhou et al.
- **🏷️ 机构**: Johns Hopkins University, Adobe Systems, the University of Hong Kong, University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing feedforward subject-driven video customization methods mainly study single-subject scenarios due to the difficulty of constructing multi-subject training data pairs. Another challenging problem that how to use the signals such as depth, mask, camera, and text prompts to control and edit the subject in the customized video is still less explored. In this paper, we first propose a data construction pipeline, VideoCus-Factory, to produce training data pairs for multi-subject customization from raw videos without labels and control signals such as depth-to-video and mask-to-video pairs. Based on our constructed data, we develop an Image-Video Transfer Mixed (IVTM) training with image editing data to enable instructive editing for the subject in the customized video. Then we propose a diffusion Transformer framework, OmniVCus, with two embedding mechanisms, Lottery Embedding (LE) and Temporally Aligned Embedding (TAE). LE enables inference with more subjects by using the training subjects to activate more frame embeddings. TAE encourages the generation process to extract guidance from temporally aligned control signals by assigning the same frame embeddings to the control and noise tokens. Experiments demonstrate that our method significantly surpasses state-of-the-art methods in both quantitative and qualitative evaluations. Video demos are at our project page: https://caiyuanhao1998.github.io/project/OmniVCus/. Our code, models, data are released at https://github.com/caiyuanhao1998/Open-OmniVCus

</details>

### DreamPRM: Domain-reweighted Process Reward Model for Multimodal Reasoning.
- **链接**: [arXiv:2505.20241](https://arxiv.org/abs/2505.20241) · 📚 被引 0
- **作者**: Qi Cao, Ruiyi Wang, Ruiyi Zhang, Sai Ashish Somayajula, Pengtao Xie
- **🏷️ 机构**: University of California, San Diego
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reasoning has substantially improved the performance of large language models (LLMs) on complicated tasks. Central to the current reasoning studies, Process Reward Models (PRMs) offer a fine-grained evaluation of intermediate reasoning steps and guide the reasoning process. However, extending PRMs to multimodal large language models (MLLMs) introduces challenges. Since multimodal reasoning covers a wider range of tasks compared to text-only scenarios, the resulting distribution shift from the training to testing sets is more severe, leading to greater generalization difficulty. Training a reliable multimodal PRM, therefore, demands large and diverse datasets to ensure sufficient coverage. However, current multimodal reasoning datasets suffer from a marked quality imbalance, which degrades PRM performance and highlights the need for an effective data selection strategy. To address the issues, we introduce DreamPRM, a domain-reweighted training framework for multimodal PRMs which employs bi-level optimization. In the lower-level optimization, DreamPRM performs fine-tuning on multiple datasets with domain weights, allowing the PRM to prioritize high-quality reasoning signals and alleviating the impact of dataset quality imbalance. In the upper-level optimization, the PRM is evaluated on a separate meta-learning dataset; this feedback updates the domain weights through an aggregation loss function, thereby improving the generalization capability of trained PRM. Extensive experiments on multiple multimodal reasoning benchmarks covering both mathematical and general reasoning show that test-time scaling with DreamPRM consistently improves the performance of state-of-the-art MLLMs. Further comparisons reveal that DreamPRM's domain-reweighting strategy surpasses other data selection methods and yields higher accuracy gains than existing test-time scaling approaches.

</details>

### Amplifying Prominent Representations in Multimodal Learning via Variational Dirichlet Process.
- **链接**: [arXiv:2510.20736](https://arxiv.org/abs/2510.20736) · [代码](https://github.com/HKU-MedAI/DPMM.git) · 📚 被引 0
- **作者**: Tsai Hor Chan, Feng Wu, Yihang Chen, Guosheng Yin, Lequan Yu
- **🏷️ 机构**: University of Pennsylvania, University of Pennsylvania, University of Science and Technology of China, University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Developing effective multimodal fusion approaches has become increasingly essential in many real-world scenarios, such as health care and finance. The key challenge is how to preserve the feature expressiveness in each modality while learning cross-modal interactions. Previous approaches primarily focus on the cross-modal alignment, while over-emphasis on the alignment of marginal distributions of modalities may impose excess regularization and obstruct meaningful representations within each modality. The Dirichlet process (DP) mixture model is a powerful Bayesian non-parametric method that can amplify the most prominent features by its richer-gets-richer property, which allocates increasing weights to them. Inspired by this unique characteristic of DP, we propose a new DP-driven multimodal learning framework that automatically achieves an optimal balance between prominent intra-modal representation learning and cross-modal alignment. Specifically, we assume that each modality follows a mixture of multivariate Gaussian distributions and further adopt DP to calculate the mixture weights for all the components. This paradigm allows DP to dynamically allocate the contributions of features and select the most prominent ones, leveraging its richer-gets-richer property, thus facilitating multimodal feature fusion. Extensive experiments on several multimodal datasets demonstrate the superior performance of our model over other competitors. Ablation analysis further validates the effectiveness of DP in aligning modality distributions and its robustness to changes in key hyperparameters. Code is anonymously available at https://github.com/HKU-MedAI/DPMM.git

</details>

### SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/53f1c3ec5df814b5aabe9ae88a29bb49-Abstract-Conference.html)
- **作者**: Beitao Chen, Xinyu Lyu, Shengming Yuan, Jingkuan Song, Hengtao Shen, Lianli Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### MJ-Bench: Is Your Multimodal Reward Model Really a Good Judge for Text-to-Image Generation?
- **链接**: [arXiv:2407.04842](https://arxiv.org/abs/2407.04842) · 📚 被引 0
- **作者**: Zhaorun Chen, Zichen Wen, Yichao Du, Yiyang Zhou, Chenhang Cui, Siwei Han et al.
- **🏷️ 机构**: University of Chicago, Shanghai Jiao Tong University, University of Science and Technology of China
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While text-to-image models like DALLE-3 and Stable Diffusion are rapidly proliferating, they often encounter challenges such as hallucination, bias, and the production of unsafe, low-quality output. To effectively address these issues, it is crucial to align these models with desired behaviors based on feedback from a multimodal judge. Despite their significance, current multimodal judges frequently undergo inadequate evaluation of their capabilities and limitations, potentially leading to misalignment and unsafe fine-tuning outcomes. To address this issue, we introduce MJ-Bench, a novel benchmark which incorporates a comprehensive preference dataset to evaluate multimodal judges in providing feedback for image generation models across four key perspectives: alignment, safety, image quality, and bias. Specifically, we evaluate a large variety of multimodal judges including smaller-sized CLIP-based scoring models, open-source VLMs (e.g. LLaVA family), and close-source VLMs (e.g. GPT-4o, Claude 3) on each decomposed subcategory of our preference dataset. Experiments reveal that close-source VLMs generally provide better feedback, with GPT-4o outperforming other judges in average. Compared with open-source VLMs, smaller-sized scoring models can provide better feedback regarding text-image alignment and image quality, while VLMs provide more accurate feedback regarding safety and generation bias due to their stronger reasoning capabilities. Further studies in feedback scale reveal that VLM judges can generally provide more accurate and stable feedback in natural language (Likert-scale) than numerical scales. Notably, human evaluations on end-to-end fine-tuned models using separate feedback from these multimodal judges provide similar conclusions, further confirming the effectiveness of MJ-Bench. All data, code, models are available at https://huggingface.co/MJ-Bench.

</details>

### Decoupling Contrastive Decoding: Robust Hallucination Mitigation in Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f39cc9110544a067f024c1fb8b396128-Abstract-Conference.html)
- **作者**: Wei Chen, Xin Yan, Bin Wen, Fan Yang, Tingting Gao, Di Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### ModuLM: Enabling Modular and Multimodal Molecular Relational Learning with Large Language Models.
- **链接**: [arXiv:2506.00880](https://arxiv.org/abs/2506.00880) · 📚 被引 1
- **作者**: Zhuo Chen, Yizhen Zheng, Huan Yee Koh, Hongxin Xiang, Linjiang Chen, Wenjie Du et al.
- **🏷️ 机构**: ByteDance Inc., Monash University, Hunan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Molecular Relational Learning (MRL) aims to understand interactions between molecular pairs, playing a critical role in advancing biochemical research. With the recent development of large language models (LLMs), a growing number of studies have explored the integration of MRL with LLMs and achieved promising results. However, the increasing availability of diverse LLMs and molecular structure encoders has significantly expanded the model space, presenting major challenges for benchmarking. Currently, there is no LLM framework that supports both flexible molecular input formats and dynamic architectural switching. To address these challenges, reduce redundant coding, and ensure fair model comparison, we propose ModuLM, a framework designed to support flexible LLM-based model construction and diverse molecular representations. ModuLM provides a rich suite of modular components, including 8 types of 2D molecular graph encoders, 11 types of 3D molecular conformation encoders, 7 types of interaction layers, and 7 mainstream LLM backbones. Owing to its highly flexible model assembly mechanism, ModuLM enables the dynamic construction of over 50,000 distinct model configurations. In addition, we provide comprehensive results to demonstrate the effectiveness of ModuLM in supporting LLM-based MRL tasks.

</details>

### TRACE: Grounding Time Series in Context for Multimodal Embedding and Retrieval.
- **链接**: [arXiv:2506.09114](https://arxiv.org/abs/2506.09114) · 📚 被引 0
- **作者**: Jialin Chen, Ziyu Zhao, Gaukhar Nurbek, Aosong Feng, Ali Maatouk, Leandros Tassiulas et al.
- **🏷️ 机构**: Yale University, McGill University, McGill University, University of Texas Rio Grande Valley
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ubiquity of dynamic data in domains such as weather, healthcare, and energy underscores a growing need for effective interpretation and retrieval of time-series data. These data are inherently tied to domain-specific contexts, such as clinical notes or weather narratives, making cross-modal retrieval essential not only for downstream tasks but also for developing robust time-series foundation models by retrieval-augmented generation (RAG). Despite the increasing demand, time-series retrieval remains largely underexplored. Existing methods often lack semantic grounding, struggle to align heterogeneous modalities, and have limited capacity for handling multi-channel signals. To address this gap, we propose TRACE, a generic multimodal retriever that grounds time-series embeddings in aligned textual context. TRACE enables fine-grained channel-level alignment and employs hard negative mining to facilitate semantically meaningful retrieval. It supports flexible cross-modal retrieval modes, including Text-to-Timeseries and Timeseries-to-Text, effectively linking linguistic descriptions with complex temporal patterns. By retrieving semantically relevant pairs, TRACE enriches downstream models with informative context, leading to improved predictive accuracy and interpretability. Beyond a static retrieval engine, TRACE also serves as a powerful standalone encoder, with lightweight task-specific tuning that refines context-aware representations while maintaining strong cross-modal alignment. These representations achieve state-of-the-art performance on downstream forecasting and classification tasks. Extensive experiments across multiple domains highlight its dual utility, as both an effective encoder for downstream applications and a general-purpose retriever to enhance time-series models.

</details>

### Visual Thoughts: A Unified Perspective of Understanding Multimodal Chain-of-Thought.
- **链接**: [arXiv:2505.15510](https://arxiv.org/abs/2505.15510) · 📚 被引 0
- **作者**: Zihui Cheng, Qiguang Chen, Xiao Xu, Jiaqi Wang, Weiyun Wang, Hao Fei et al.
- **🏷️ 机构**: Central South University, Harbin Institute of Technology, China, National University of Singapore
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) have achieved significant success in multimodal tasks, with multimodal chain-of-thought (MCoT) further enhancing performance and interpretability. Recent MCoT methods fall into two categories: (i) Textual-MCoT (T-MCoT), which takes multimodal input and produces textual output; and (ii) Interleaved-MCoT (I-MCoT), which generates interleaved image-text outputs. Despite advances in both approaches, the mechanisms driving these improvements are not fully understood. To fill this gap, we first reveal that MCoT boosts LVLMs by incorporating visual thoughts, which convey image information to the reasoning process regardless of the MCoT format, depending only on clarity and conciseness of expression. Furthermore, to explore visual thoughts systematically, we define four distinct forms of visual thought expressions and analyze them comprehensively. Our findings demonstrate that these forms differ in clarity and conciseness, yielding varying levels of MCoT improvement. Additionally, we explore the internal nature of visual thoughts, finding that visual thoughts serve as intermediaries between the input image and reasoning to deeper transformer layers, enabling more advanced visual information transmission. We hope that the visual thoughts can inspire further breakthroughs for future MCoT research.

</details>

### AnomalyCoT: A Multi-Scenario Chain-of-Thought Dataset for Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6470d9c87259074429c1788a27aeee80-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Jiaxi Cheng, Yuliang Xu, Shoupeng Wang, Tao Ma, Yuchen He, Jinghe Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### A TRIANGLE Enables Multimodal Alignment Beyond Cosine Similarity.
- **链接**: [arXiv:2509.24734](https://arxiv.org/abs/2509.24734) · 📚 被引 0
- **作者**: Giordano Cicchetti, Eleonora Grassucci, Danilo Comminiello
- **🏷️ 机构**: University of Rome &quot;La Sapienza&quot;, Sapienza University of Rome
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning plays a pivotal role in advancing artificial intelligence systems by incorporating information from multiple modalities to build a more comprehensive representation. Despite its importance, current state-of-the-art models still suffer from severe limitations that prevent the successful development of a fully multimodal model. Such methods may not provide indicators that all the involved modalities are effectively aligned. As a result, some modalities may not be aligned, undermining the effectiveness of the model in downstream tasks where multiple modalities should provide additional information that the model fails to exploit. In this paper, we present TRIANGLE: TRI-modAl Neural Geometric LEarning, the novel proposed similarity measure that is directly computed in the higher-dimensional space spanned by the modality embeddings. TRIANGLE improves the joint alignment of three modalities via a triangle-area similarity, avoiding additional fusion layers or pairwise similarities. When incorporated in contrastive losses replacing cosine similarity, TRIANGLE significantly boosts the performance of multimodal modeling, while yielding interpretable alignment rationales. Extensive evaluation in three-modal tasks such as video-text and audio-text retrieval or audio-video classification, demonstrates that TRIANGLE achieves state-of-the-art results across different datasets improving the performance of cosine-based methods up to 9 points of Recall@1.

</details>

### QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training.
- **链接**: [arXiv:2506.00711](https://arxiv.org/abs/2506.00711) · [代码](https://github.com/DDVD233/QoQ_Med) · 📚 被引 0
- **作者**: David Dai, Peilin Chen, Chanakya Ekbote, Paul Pu Liang
- **🏷️ 机构**: Massachusetts Institute of Technology, MIT - Massachusetts Institute of Technology, MIT
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Clinical decision-making routinely demands reasoning over heterogeneous data, yet existing multimodal language models (MLLMs) remain largely vision-centric and fail to generalize across clinical specialties. To bridge this gap, we introduce QoQ-Med-7B/32B, the first open generalist clinical foundation model that jointly reasons across medical images, time-series signals, and text reports. QoQ-Med is trained with Domain-aware Relative Policy Optimization (DRPO), a novel reinforcement-learning objective that hierarchically scales normalized rewards according to domain rarity and modality difficulty, mitigating performance imbalance caused by skewed clinical data distributions. Trained on 2.61 million instruction tuning pairs spanning 9 clinical domains, we show that DRPO training boosts diagnostic performance by 43% in macro-F1 on average across all visual domains as compared to other critic-free training methods like GRPO. Furthermore, with QoQ-Med trained on intensive segmentation data, it is able to highlight salient regions related to the diagnosis, with an IoU 10x higher than open models while reaching the performance of OpenAI o4-mini. To foster reproducibility and downstream research, we release (i) the full model weights, (ii) the modular training pipeline, and (iii) all intermediate reasoning traces at https://github.com/DDVD233/QoQ_Med.

</details>

### Brain Harmony: A Multimodal Foundation Model Unifying Morphology and Function into 1D Tokens.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/b0832cc57899cfd2d3fedeb3f330ba80-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zijian Dong, Ruilin Li, Joanna Su Xian Chong, Niousha Dehestani, Yinghui Teng, Yi Lin et al.
- **🏷️ 机构**: National University of Singapore, Shanghai University, DIMACS, Rutgers University
- **会议**: NeurIPS 2025

### MIRAGE: Assessing Hallucination in Multimodal Reasoning Chains of MLLM.
- **链接**: [arXiv:2505.24238](https://arxiv.org/abs/2505.24238) · 📚 被引 0
- **作者**: Bowen Dong, Minheng Ni, Zitong Huang, Guanglei Yang, Wangmeng Zuo, Lei Zhang
- **🏷️ 机构**: Harbin Institute of Technology, Hong Kong Polytechnic University, Huawei Technologies Ltd.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal hallucination in multimodal large language models (MLLMs) restricts the correctness of MLLMs. However, multimodal hallucinations are multi-sourced and arise from diverse causes. Existing benchmarks fail to adequately distinguish between perception-induced hallucinations and reasoning-induced hallucinations. This failure constitutes a significant issue and hinders the diagnosis of multimodal reasoning failures within MLLMs. To address this, we propose the {\dataset} benchmark, which isolates reasoning hallucinations by constructing questions where input images are correctly perceived by MLLMs yet reasoning errors persist. {\dataset} introduces multi-granular evaluation metrics: accuracy, factuality, and LLMs hallucination score for hallucination quantification. Our analysis reveals that (1) the model scale, data scale, and training stages significantly affect the degree of logical, fabrication, and factual hallucinations; (2) current MLLMs show no effective improvement on spatial hallucinations caused by misinterpreted spatial relationships, indicating their limited visual reasoning capabilities; and (3) question types correlate with distinct hallucination patterns, highlighting targeted challenges and potential mitigation strategies. To address these challenges, we propose {\method}, a method that combines curriculum reinforcement fine-tuning to encourage models to generate logic-consistent reasoning chains by stepwise reducing learning difficulty, and collaborative hint inference to reduce reasoning complexity. {\method} establishes a baseline on {\dataset}, and reduces the logical hallucinations in original base models.

</details>

### BioReason: Incentivizing Multimodal Biological Reasoning within a DNA-LLM Model.
- **链接**: [arXiv:2505.23579](https://arxiv.org/abs/2505.23579) · [代码](https://github.com/bowang-lab/BioReason) · 📚 被引 3
- **作者**: Adibvafa Fallahpour, Andrew Magnuson, Purav Gupta, Shihao Ma, Jack Naimer, Arnav Shah et al.
- **🏷️ 机构**: NVIDIA, Arc Institute, Vector Institute, UHN, UofT, University of Toronto, École Polytechnique Fédérale de Lausanne
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unlocking deep and interpretable biological reasoning from complex genomic data remains a major AI challenge limiting scientific progress. While current DNA foundation models excel at representing sequences, they struggle with multi-step reasoning and lack transparent, biologically meaningful explanations. BioReason addresses this by tightly integrating a DNA foundation model with a large language model (LLM), enabling the LLM to directly interpret and reason over genomic information. Through supervised fine-tuning and reinforcement learning, BioReason learns to produce logical, biologically coherent deductions. It achieves major performance gains, boosting KEGG-based disease pathway prediction accuracy from 86% to 98% and improving variant effect prediction by an average of 15% over strong baselines. BioReason can reason over unseen biological entities and explain its decisions step by step, offering a transformative framework for interpretable, mechanistic AI in biology. All data, code, and checkpoints are available at https://github.com/bowang-lab/BioReason

</details>

### Prot2Text-V2: Protein Function Prediction with Multimodal Contrastive Alignment.
- **链接**: [arXiv:2505.11194](https://arxiv.org/abs/2505.11194) · 📚 被引 0
- **作者**: Xiao Fei, Michail Chatzianastasis, Sarah Almeida Carneiro, Hadi Abdine, Lawrence P. Petalidis, Michalis Vazirgiannis
- **🏷️ 机构**: École polytechnique, Ecole Polytechnique, École Polytechnique
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predicting protein function from sequence is a central challenge in computational biology. While existing methods rely heavily on structured ontologies or similarity-based techniques, they often lack the flexibility to express structure-free functional descriptions and novel biological functions. In this work, we introduce Prot2Text-V2, a novel multimodal sequence-to-text model that generates free-form natural language descriptions of protein function directly from amino acid sequences. Our method combines a protein language model as a sequence encoder (ESM-3B) and a decoder-only language model (LLaMA-3.1-8B-Instruct) through a lightweight nonlinear modality projector. A key innovation is our Hybrid Sequence-level Contrastive Alignment Learning (H-SCALE), which improves cross-modal learning by matching mean- and std-pooled protein embeddings with text representations via contrastive loss. After the alignment phase, we apply instruction-based fine-tuning using LoRA on the decoder to teach the model how to generate accurate protein function descriptions conditioned on the protein sequence. We train Prot2Text-V2 on about 250K curated entries from SwissProt and evaluate it under low-homology conditions, where test sequences have low similarity with training samples. Prot2Text-V2 consistently outperforms traditional and LLM-based baselines across various metrics.

</details>

### Counterfactual Evolution of Multimodal Datasets via Visual Programming.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/75c2ec5f98d7b2f50ad68033d2c07086-Abstract-Conference.html) · 📚 被引 0
- **作者**: Minghe Gao, Zhongqi Yue, Wenjie Yan, Yihao Hu, Wei Ji, Siliang Tang et al.
- **🏷️ 机构**: Zhejiang University, Nanyang Technological University, Southeast University
- **会议**: NeurIPS 2025

### Multimodal Negative Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e150e6d0a1e5214740c39c6e4503ba7a-Abstract-Conference.html)
- **作者**: Baoquan Gong, Xiyuan Gao, Pengfei Zhu, Qinghua Hu, Bing Cao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### With Limited Data for Multimodal Alignment, Let the STRUCTURE Guide You.
- **链接**: [arXiv:2506.16895](https://arxiv.org/abs/2506.16895) · 📚 被引 0
- **作者**: Fabian Gröger, Shuo Wen, Huyen Le, Maria Brbic
- **🏷️ 机构**: University of Basel, School of Computer and Communication Sciences, EPFL - EPF Lausanne, EPFL - EPF Lausanne
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal models have demonstrated powerful capabilities in complex tasks requiring multimodal alignment, including zero-shot classification and cross-modal retrieval. However, existing models typically rely on millions of paired multimodal samples, which are prohibitively expensive or infeasible to obtain in many domains. In this work, we explore the feasibility of building multimodal models with limited amount of paired data by aligning pretrained unimodal foundation models. We show that high-quality alignment is possible with as few as tens of thousands of paired samples$\unicode{x2013}$less than $1\%$ of the data typically used in the field. To achieve this, we introduce STRUCTURE, an effective regularization technique that preserves the neighborhood geometry of the latent space of unimodal encoders. Additionally, we show that aligning last layers is often suboptimal and demonstrate the benefits of aligning the layers with the highest representational similarity across modalities. These two components can be readily incorporated into existing alignment methods, yielding substantial gains across 24 zero-shot image classification and retrieval benchmarks, with average relative improvement of $51.6\%$ in classification and $91.8\%$ in retrieval tasks. Our results highlight the effectiveness and broad applicability of our framework for limited-sample multimodal learning and offer a promising path forward for resource-constrained domains.

</details>

### RBench-V: A Primary Assessment for Visual Reasoning Models with Multimodal Outputs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f0430903a14db90e5ce96f101902d6d7-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Meng-Hao Guo, Xuanyu Chu, Qianrui Yang, Zhe-Han Mo, Yiqing Shen, Pei-lin Li et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, University of Wisconsin, Madison
- **会议**: NeurIPS 2025

### LBMKGC: Large Model-Driven Balanced Multimodal Knowledge Graph Completion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a254abbfdd029d388fc35fd850bbc551-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yuan Guo, Qian Ma, Hui Li, Qiao Ning, Furui Zhan, Yu Gu et al.
- **🏷️ 机构**: Dalian Maritime University, School of Artificial Intelligence and Computer Science, Jiangnan University
- **会议**: NeurIPS 2025

### MRSAudio: A Large-Scale Multimodal Recorded Spatial Audio Dataset with Refined Annotations.
- **链接**: [arXiv:2510.10396](https://arxiv.org/abs/2510.10396) · 📚 被引 0
- **作者**: Wenxiang Guo, Changhao Pan, Zhiyuan Zhu, Xintong Hu, Yu Zhang, Li Tang et al.
- **🏷️ 机构**: Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans rely on multisensory integration to perceive spatial environments, where auditory cues enable sound source localization in three-dimensional space. Despite the critical role of spatial audio in immersive technologies such as VR/AR, most existing multimodal datasets provide only monaural audio, which limits the development of spatial audio generation and understanding. To address these challenges, we introduce MRSAudio, a large-scale multimodal spatial audio dataset designed to advance research in spatial audio understanding and generation. MRSAudio spans four distinct components: MRSLife, MRSSpeech, MRSMusic, and MRSSing, covering diverse real-world scenarios. The dataset includes synchronized binaural and ambisonic audio, exocentric and egocentric video, motion trajectories, and fine-grained annotations such as transcripts, phoneme boundaries, lyrics, scores, and prompts. To demonstrate the utility and versatility of MRSAudio, we establish five foundational tasks: audio spatialization, and spatial text to speech, spatial singing voice synthesis, spatial music generation and sound event localization and detection. Results show that MRSAudio enables high-quality spatial modeling and supports a broad range of spatial audio research. Demos and dataset access are available at https://mrsaudio.github.io.

</details>

### MixPrompt: Efficient Mixed Prompting for Multimodal Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/31f527006510a66f6accf141483efa4c-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zhiwei Hao, Zhongyu Xiao, Jianyuan Guo, Li Shen, Yong Luo, Han Hu et al.
- **🏷️ 机构**: Beijing Institute of Technology, City University of Hong Kong (CityUHK), Sun Yat-Sen University
- **会议**: NeurIPS 2025

### CogPhys: Assessing Cognitive Load via Multimodal Remote and Contact-based Physiological Sensing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/014e80b61aca7a85630e6da5d63427c6-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Anirudh Bindiganavale Harish, Peikun Guo, Bhargav Ghanekar, Diya Gupta, Akilesh Rajavenkatanarayanan, Manoj Sharma et al.
- **🏷️ 机构**: Rice University, General Motors, alcon
- **会议**: NeurIPS 2025

### VLForgery Face Triad: Detection, Localization and Attribution via Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/ee94bf235482e4c1f689c04c81656dbf-Abstract-Conference.html)
- **作者**: Xinan He, Yue Zhou, Bing Fan, Bin Li, Guopu Zhu, Feng Ding
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6b628a3d7cb8055eb6fd2dd48c586347-Abstract-Conference.html)
- **作者**: Zhentao He, Can Zhang, Ziheng Wu, Zhenghao Chen, Yufei Zhan, Yifan Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Unlabeled Data Improves Fine-Grained Image Zero-shot Classification with Multimodal LLMs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6b7f9d9c1217a748391800871ff7d17d-Abstract-Conference.html)
- **作者**: Yunqi Hong, Sohyun An, Andrew Bai, Neil Y. C. Lin, Cho-Jui Hsieh
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Knowledge-based Visual Question Answer with Multimodal Processing, Retrieval and Filtering.
- **链接**: [arXiv:2510.14605](https://arxiv.org/abs/2510.14605) · [代码](https://github.com/cqu-student/Wiki-PRF) · 📚 被引 0
- **作者**: Yuyang Hong, Jiaqi Gu, Qi Yang, Lubin Fan, Yue Wu, Ying Wang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Alibaba Group, UCAS
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Knowledge-based visual question answering (KB-VQA) requires visual language models (VLMs) to integrate visual understanding with external knowledge retrieval. Although retrieval-augmented generation (RAG) achieves significant advances in this task by combining knowledge-base querying, it still struggles with the quality of multimodal queries and the relevance of retrieved results. To overcome these challenges, we propose a novel three-stage method, termed Wiki-PRF, including Processing, Retrieval and Filtering stages. The processing stage dynamically invokes visual tools to extract precise multimodal information for retrieval. The retrieval stage integrates visual and text features to achieve multimodal knowledge retrieval. The filtering stage performs relevance filtering and concentration on retrieval results. To this end, we introduce a visual language model trained with answer accuracy and format consistency as reward signals via a reinforcement learning manner. This enhances the model's reasoning, tool invocation for accurate queries, and filtering of irrelevant content. Experiments on benchmark datasets (E-VQA and InfoSeek) show significant improvements~(36.0 and 42.8) in answer quality, achieving state-of-the-art performance. Code is available at https://github.com/cqu-student/Wiki-PRF

</details>

### CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a2ebbe4f2714db7d124e7eac35b40db7-Abstract-Conference.html)
- **作者**: Kornel Howil, Joanna Waczynska, Piotr Borycki, Tadeusz Dziarmaga, Marcin Mazur, Przemyslaw Spurek
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### DREAM: Drafting with Refined Target Features and Entropy-Adaptive Cross-Attention Fusion for Multimodal Speculative Decoding.
- **链接**: [arXiv:2505.19201](https://arxiv.org/abs/2505.19201) · [代码](https://github.com/SAI-Lab-NYU/DREAM.git) · 📚 被引 0
- **作者**: Yunhai Hu, Tianhua Xia, Zining Liu, Rahul Raman, Xingyu Liu, Bo Bao et al.
- **🏷️ 机构**: New York University, University of Pennsylvania, University of Pennsylvania, Beijing University of Posts and Telecommunications
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Speculative decoding (SD) has emerged as a powerful method for accelerating autoregressive generation in large language models (LLMs), yet its integration into vision-language models (VLMs) remains underexplored. We introduce DREAM, a novel speculative decoding framework tailored for VLMs that combines three key innovations: (1) a cross-attention-based mechanism to inject intermediate features from the target model into the draft model for improved alignment, (2) adaptive intermediate feature selection based on attention entropy to guide efficient draft model training, and (3) visual token compression to reduce draft model latency. DREAM enables efficient, accurate, and parallel multimodal decoding with significant throughput improvement. Experiments across a diverse set of recent popular VLMs, including LLaVA, Pixtral, SmolVLM and Gemma3, demonstrate up to 3.6x speedup over conventional decoding and significantly outperform prior SD baselines in both inference throughput and speculative draft acceptance length across a broad range of multimodal benchmarks. The code is publicly available at: https://github.com/SAI-Lab-NYU/DREAM.git

</details>

### MLLM-For3D: Adapting Multimodal Large Language Model for 3D Reasoning Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4f0a2a0b2ca6ffd5c8d5de26d3e8d54d-Abstract-Conference.html)
- **作者**: Jiaxin Huang, Runnan Chen, Ziwen Li, Zhengqing Gao, Xiao He, Yandong Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### SAM-R1: Leveraging SAM for Reward Feedback in Multimodal Segmentation via Reinforcement Learning.
- **链接**: [arXiv:2505.22596](https://arxiv.org/abs/2505.22596) · 📚 被引 2
- **作者**: Jiaqi Huang, Zunnan Xu, Jun Zhou, Ting Liu, Yicheng Xiao, Mingwen Ou et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, Ant Financial
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leveraging multimodal large models for image segmentation has become a prominent research direction. However, existing approaches typically rely heavily on manually annotated datasets that include explicit reasoning processes, which are costly and time-consuming to produce. Recent advances suggest that reinforcement learning (RL) can endow large models with reasoning capabilities without requiring such reasoning-annotated data. In this paper, we propose SAM-R1, a novel framework that enables multimodal large models to perform fine-grained reasoning in image understanding tasks. Our approach is the first to incorporate fine-grained segmentation settings during the training of multimodal reasoning models. By integrating task-specific, fine-grained rewards with a tailored optimization objective, we further enhance the model's reasoning and segmentation alignment. We also leverage the Segment Anything Model (SAM) as a strong and flexible reward provider to guide the learning process. With only 3k training samples, SAM-R1 achieves strong performance across multiple benchmarks, demonstrating the effectiveness of reinforcement learning in equipping multimodal models with segmentation-oriented reasoning capabilities.

</details>

### ChartSketcher: Reasoning with Multimodal Feedback and Reflection for Chart Understanding.
- **链接**: [arXiv:2505.19076](https://arxiv.org/abs/2505.19076) · 📚 被引 1
- **作者**: Muye Huang, Lingling Zhang, Jie Ma, Han Lai, Fangzhi Xu, Yifei Li et al.
- **🏷️ 机构**: Xi'an Jiaotong University, Huazhong University of Science and Technology, Ohio State University, Columbus
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Charts are high-density visualization carriers for complex data, serving as a crucial medium for information extraction and analysis. Automated chart understanding poses significant challenges to existing multimodal large language models (MLLMs) due to the need for precise and complex visual reasoning. Current step-by-step reasoning models primarily focus on text-based logical reasoning for chart understanding. However, they struggle to refine or correct their reasoning when errors stem from flawed visual understanding, as they lack the ability to leverage multimodal interaction for deeper comprehension. Inspired by human cognitive behavior, we propose ChartSketcher, a multimodal feedback-driven step-by-step reasoning method designed to address these limitations. ChartSketcher is a chart understanding model that employs Sketch-CoT, enabling MLLMs to annotate intermediate reasoning steps directly onto charts using a programmatic sketching library, iteratively feeding these visual annotations back into the reasoning process. This mechanism enables the model to visually ground its reasoning and refine its understanding over multiple steps. We employ a two-stage training strategy: a cold start phase to learn sketch-based reasoning patterns, followed by off-policy reinforcement learning to enhance reflection and generalization. Experiments demonstrate that ChartSketcher achieves promising performance on chart understanding benchmarks and general vision tasks, providing an interactive and interpretable approach to chart comprehension.

</details>

### MIDAS: Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning.
- **链接**: [arXiv:2509.25831](https://arxiv.org/abs/2509.25831) · 📚 被引 0
- **作者**: Seonghyeon Hwang, Soyoung Choi, Steven Euijong Whang
- **🏷️ 机构**: Samsung Research, KAIST
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal models often over-rely on dominant modalities, failing to achieve optimal performance. While prior work focuses on modifying training objectives or optimization procedures, data-centric solutions remain underexplored. We propose MIDAS, a novel data augmentation strategy that generates misaligned samples with semantically inconsistent cross-modal information, labeled using unimodal confidence scores to compel learning from contradictory signals. However, this confidence-based labeling can still favor the more confident modality. To address this within our misaligned samples, we introduce weak-modality weighting, which dynamically increases the loss weight of the least confident modality, thereby helping the model fully utilize weaker modality. Furthermore, when misaligned features exhibit greater similarity to the aligned features, these misaligned samples pose a greater challenge, thereby enabling the model to better distinguish between classes. To leverage this, we propose hard-sample weighting, which prioritizes such semantically ambiguous misaligned samples. Experiments on multiple multimodal classification benchmarks demonstrate that MIDAS significantly outperforms related baselines in addressing modality imbalance.

</details>

### Elevating Visual Perception in Multimodal LLMs with Visual Embedding Distillation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/75ed738c083f8941cfc990245e4f6265-Abstract-Conference.html)
- **作者**: Jitesh Jain, Zhengyuan Yang, Humphrey Shi, Jianfeng Gao, Jianwei Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### A Multimodal BiMamba Network with Test-Time Adaptation for Emotion Recognition Based on Physiological Signals.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d616a353c711f11c722e3f28d2d9e956-Abstract-Conference.html) · 📚 被引 1
- **作者**: Ziyu Jia, Tingyu Du, Zhengyu Tian, Hongkai Li, Yong Zhang, Chenyu Liu
- **🏷️ 机构**: Institute of automation, Chinese academy of science, Beijing Jiaotong University, CASIA
- **会议**: NeurIPS 2025

### Rethinking Multimodal Learning from the Perspective of Mitigating Classification Ability Disproportion.
- **链接**: [arXiv:2502.20120](https://arxiv.org/abs/2502.20120) · [代码](https://github.com/njustkmg/NeurIPS25-AUG) · 📚 被引 1
- **作者**: Qing-Yuan Jiang, Longfei Huang, Yang Yang
- **🏷️ 机构**: Nanjing University of Science and Technology, Shanghai Jiao Tong University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning (MML) is significantly constrained by modality imbalance, leading to suboptimal performance in practice. While existing approaches primarily focus on balancing the learning of different modalities to address this issue, they fundamentally overlook the inherent disproportion in model classification ability, which serves as the primary cause of this phenomenon. In this paper, we propose a novel multimodal learning approach to dynamically balance the classification ability of weak and strong modalities by incorporating the principle of boosting. Concretely, we first propose a sustained boosting algorithm in multimodal learning by simultaneously optimizing the classification and residual errors. Subsequently, we introduce an adaptive classifier assignment strategy to dynamically facilitate the classification performance of the weak modality. Furthermore, we theoretically analyze the convergence property of the cross-modal gap function, ensuring the effectiveness of the proposed boosting scheme. To this end, the classification ability of strong and weak modalities is expected to be balanced, thereby mitigating the imbalance issue. Empirical experiments on widely used datasets reveal the superiority of our method through comparison with various state-of-the-art (SOTA) multimodal learning baselines. The source code is available at https://github.com/njustkmg/NeurIPS25-AUG.

</details>

### VLM-R³: Region Recognition, Reasoning, and Refinement for Enhanced Multimodal Chain-of-Thought.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/5c4e0e38691e2aa08bba4cefc4c6e852-Abstract-Conference.html)
- **作者**: Chaoya Jiang, Yongrui Heng, Wei Ye, Haiyang Xu, Ming Yan, Ji Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Co-Reinforcement Learning for Unified Multimodal Understanding and Generation.
- **链接**: [arXiv:2505.17534](https://arxiv.org/abs/2505.17534) · [代码](https://github.com/mm-vl/ULM-R1) · 📚 被引 2
- **作者**: Jingjing Jiang, Chongjie Si, Jun Luo, Hanwang Zhang, Chao Ma
- **🏷️ 机构**: Shanghai Jiao Tong University, Nanyang Technological University, NTU
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a pioneering exploration of reinforcement learning (RL) via group relative policy optimization for unified multimodal large language models (ULMs), aimed at simultaneously reinforcing generation and understanding capabilities. Through systematic pilot studies, we uncover the significant potential of ULMs to enable the synergistic co-evolution of dual capabilities within a shared policy optimization framework. Building on this insight, we introduce CoRL, a co-reinforcement learning framework comprising a unified RL stage for joint optimization and a refined RL stage for task-specific enhancement. With the proposed CoRL, our resulting model, ULM-R1, achieves average improvements of 7% on three text-to-image generation datasets and 23% on nine multimodal understanding benchmarks. These results demonstrate the effectiveness of CoRL and highlight the substantial benefit of reinforcement learning in facilitating cross-task synergy and optimization for ULMs. Code is available at https://github.com/mm-vl/ULM-R1.

</details>

### Multimodal Tabular Reasoning with Privileged Structured Information.
- **链接**: [arXiv:2506.04088](https://arxiv.org/abs/2506.04088) · 📚 被引 0
- **作者**: Jun-Peng Jiang, Yu Xia, Hai-Long Sun, Shiyin Lu, Qingguo Chen, Weihua Luo et al.
- **🏷️ 机构**: NanJing University, Alibaba Group, Nanjing University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tabular reasoning involves multi-step information extraction and logical inference over tabular data. While recent advances have leveraged large language models (LLMs) for reasoning over structured tables, such high-quality textual representations are often unavailable in real-world settings, where tables typically appear as images. In this paper, we tackle the task of tabular reasoning from table images, leveraging privileged structured information available during training to enhance multimodal large language models (MLLMs). The key challenges lie in the complexity of accurately aligning structured information with visual representations, and in effectively transferring structured reasoning skills to MLLMs despite the input modality gap. To address these, we introduce TabUlar Reasoning with Bridged infOrmation ({\sc Turbo}), a new framework for multimodal tabular reasoning with privileged structured tables. {\sc Turbo} benefits from a structure-aware reasoning trace generator based on DeepSeek-R1, contributing to high-quality modality-bridged data. On this basis, {\sc Turbo} repeatedly generates and selects the advantageous reasoning paths, further enhancing the model's tabular reasoning ability. Experimental results demonstrate that, with limited ($9$k) data, {\sc Turbo} achieves state-of-the-art performance ($+7.2\%$ vs. previous SOTA) across multiple datasets.

</details>

### Structure-Aware Fusion with Progressive Injection for Multimodal Molecular Representation Learning.
- **链接**: [arXiv:2510.23640](https://arxiv.org/abs/2510.23640) · [代码](https://github.com/selmiss/MuMo) · 📚 被引 0
- **作者**: Zihao Jing, Yan Sun, Yan Yi Li, Sugitha Janarthanan, Alana Deng, Pingzhao Hu
- **🏷️ 机构**: University of Western Ontario, Western University, University of Toronto
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal molecular models often suffer from 3D conformer unreliability and modality collapse, limiting their robustness and generalization. We propose MuMo, a structured multimodal fusion framework that addresses these challenges in molecular representation through two key strategies. To reduce the instability of conformer-dependent fusion, we design a Structured Fusion Pipeline (SFP) that combines 2D topology and 3D geometry into a unified and stable structural prior. To mitigate modality collapse caused by naive fusion, we introduce a Progressive Injection (PI) mechanism that asymmetrically integrates this prior into the sequence stream, preserving modality-specific modeling while enabling cross-modal enrichment. Built on a state space backbone, MuMo supports long-range dependency modeling and robust information propagation. Across 29 benchmark tasks from Therapeutics Data Commons (TDC) and MoleculeNet, MuMo achieves an average improvement of 2.7% over the best-performing baseline on each task, ranking first on 22 of them, including a 27% improvement on the LD50 task. These results validate its robustness to 3D conformer noise and the effectiveness of multimodal fusion in molecular representation. The code is available at: github.com/selmiss/MuMo.

</details>

### Flex-Judge: Text-Only Reasoning Unleashes Zero-Shot Multimodal Evaluators.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/9c7eeda2dc98e61baa9a5884afd231bc-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jongwoo Ko, Sungnyun Kim, Sungwoo Cho, Se-Young Yun
- **🏷️ 机构**: Microsoft, KAIST
- **会议**: NeurIPS 2025

### Balancing Multimodal Training Through Game-Theoretic Regularization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f5784de266e45bd09333721b0a602b61-Abstract-Conference.html) · 📚 被引 0
- **作者**: Konstantinos Kontras, Thomas Strypsteen, Christos Chatzichristos, Paul Pu Liang, Matthew B. Blaschko, Maarten De Vos
- **🏷️ 机构**: KU Leuven, Katholieke Universiteit Leuven, MIT
- **会议**: NeurIPS 2025

### CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder.
- **链接**: [arXiv:2510.18583](https://arxiv.org/abs/2510.18583) · 📚 被引 0
- **作者**: Yongmin Lee, Hye Won Chung
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology, KAIST
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal dataset distillation aims to synthesize a small set of image-text pairs that enables efficient training of large-scale vision-language models. While dataset distillation has shown promise in unimodal tasks, extending it to multimodal contrastive learning presents key challenges: learning cross-modal alignment and managing the high computational cost of large encoders. Prior approaches address scalability by freezing the text encoder and update only the image encoder and text projection layer. However, we find this severely limits semantic alignment and becomes a bottleneck for performance scaling. We propose CovMatch, a scalable dataset distillation framework that aligns the cross-covariance of real and synthetic features while regularizing feature distributions within each modality. Unlike prior approaches, CovMatch enables joint optimization of both encoders, leading to stronger cross-modal alignment and improved performance. Evaluated on Flickr30K and COCO, CovMatch outperforms state-of-the-art multimodal distillation methods and achieves up to 6.8% absolute gains in retrieval accuracy using only 500 synthetic pairs.

</details>

### Generalized Contrastive Learning for Universal Multimodal Retrieval.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4e23bee2df5fc72018d9d74d875d7cf3-Abstract-Conference.html)
- **作者**: Jungsoo Lee, Janghoon Cho, Hyojin Park, Durga Malladi, Kyuwoong Hwang, Fatih Porikli et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### InfantAgent-Next: A Multimodal Generalist Agent for Automated Computer Interaction.
- **链接**: [arXiv:2505.10887](https://arxiv.org/abs/2505.10887) · [代码](https://github.com/bin123apple/InfantAgent) · 📚 被引 0
- **作者**: Bin Lei, Weitai Kang, Zijian Zhang, Winson Chen, Xi Xie, Shan Zuo et al.
- **🏷️ 机构**: University of Minnesota - Twin Cities, University of Illinois Chicago, University of Connecticut
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces \textsc{InfantAgent-Next}, a generalist agent capable of interacting with computers in a multimodal manner, encompassing text, images, audio, and video. Unlike existing approaches that either build intricate workflows around a single large model or only provide workflow modularity, our agent integrates tool-based and pure vision agents within a highly modular architecture, enabling different models to collaboratively solve decoupled tasks in a step-by-step manner. Our generality is demonstrated by our ability to evaluate not only pure vision-based real-world benchmarks (i.e., OSWorld), but also more general or tool-intensive benchmarks (e.g., GAIA and SWE-Bench). Specifically, we achieve $\mathbf{7.27\%}$ accuracy on OSWorld, higher than Claude-Computer-Use. Codes and evaluation scripts are open-sourced at https://github.com/bin123apple/InfantAgent.

</details>

### The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio.
- **链接**: [arXiv:2410.12787](https://arxiv.org/abs/2410.12787) · 📚 被引 0
- **作者**: Sicong Leng, Yun Xing, Zesen Cheng, Yang Zhou, Hang Zhang, Xin Li et al.
- **🏷️ 机构**: Nanyang Technological University, University of Alberta, Peking University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in large multimodal models (LMMs) have significantly enhanced performance across diverse tasks, with ongoing efforts to further integrate additional modalities such as video and audio. However, most existing LMMs remain vulnerable to hallucinations, the discrepancy between the factual multimodal input and the generated textual output, which has limited their applicability in various real-world scenarios. This paper presents the first systematic investigation of hallucinations in LMMs involving the three most common modalities: language, visual, and audio. Our study reveals two key contributors to hallucinations: overreliance on unimodal priors and spurious inter-modality correlations. To address these challenges, we introduce the benchmark The Curse of Multi-Modalities (CMM), which comprehensively evaluates hallucinations in LMMs, providing a detailed analysis of their underlying issues. Our findings highlight key vulnerabilities, including imbalances in modality integration and biases from training data, underscoring the need for balanced cross-modal learning and enhanced hallucination mitigation strategies. Based on our observations and findings, we suggest potential research directions that could enhance the reliability of LMMs.

</details>

### URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model.
- **链接**: [arXiv:2511.00940](https://arxiv.org/abs/2511.00940) · 📚 被引 0
- **作者**: Zhe Li, Xiang Bai, Jieyu Zhang, Zhuangzhe Wu, Che Xu, Ying Li et al.
- **🏷️ 机构**: Peking University, Huazhong University of Science and Technology, Department of Computer Science, University of Washington
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Constructing accurate digital twins of articulated objects is essential for robotic simulation training and embodied AI world model building, yet historically requires painstaking manual modeling or multi-stage pipelines. In this work, we propose \textbf{URDF-Anything}, an end-to-end automatic reconstruction framework based on a 3D multimodal large language model (MLLM). URDF-Anything utilizes an autoregressive prediction framework based on point-cloud and text multimodal input to jointly optimize geometric segmentation and kinematic parameter prediction. It implements a specialized $[SEG]$ token mechanism that interacts directly with point cloud features, enabling fine-grained part-level segmentation while maintaining consistency with the kinematic parameter predictions. Experiments on both simulated and real-world datasets demonstrate that our method significantly outperforms existing approaches regarding geometric segmentation (mIoU 17\% improvement), kinematic parameter prediction (average error reduction of 29\%), and physical executability (surpassing baselines by 50\%). Notably, our method exhibits excellent generalization ability, performing well even on objects outside the training set. This work provides an efficient solution for constructing digital twins for robotic simulation, significantly enhancing the sim-to-real transfer capability.

</details>

### AOR: Anatomical Ontology-Guided Reasoning for Medical Large Multimodal Model in Chest X-Ray Interpretation.
- **链接**: [arXiv:2505.02830](https://arxiv.org/abs/2505.02830) · 📚 被引 1
- **作者**: Qingqiu Li, Zihang Cui, Seongsu Bae, Jilan Xu, Runtian Yuan, Yuejie Zhang et al.
- **🏷️ 机构**: Fudan University, Xidian University, KAIST
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Chest X-rays (CXRs) are the most frequently performed imaging examinations in clinical settings. Recent advancements in Large Multimodal Models (LMMs) have enabled automated CXR interpretation, enhancing diagnostic accuracy and efficiency. However, despite their strong visual understanding, current Medical LMMs (MLMMs) still face two major challenges: (1) Insufficient region-level understanding and interaction, and (2) Limited accuracy and interpretability due to single-step reasoning. In this paper, we empower MLMMs with anatomy-centric reasoning capabilities to enhance their interactivity and explainability. Specifically, we first propose an Anatomical Ontology-Guided Reasoning (AOR) framework, which centers on cross-modal region-level information to facilitate multi-step reasoning. Next, under the guidance of expert physicians, we develop AOR-Instruction, a large instruction dataset for MLMMs training. Our experiments demonstrate AOR's superior performance in both VQA and report generation tasks.

</details>

### Iterative Tool Usage Exploration for Multimodal Agents via Step-wise Preference Tuning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/55d16334943f8728073e17139e5baa3d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Pengxiang Li, Zhi Gao, Bofei Zhang, Yapeng Mi, Xiaojian (Shawn) Ma, Chenrui Shi et al.
- **🏷️ 机构**: Beijing Institute of Technology, Beijing Institute for General Artificial Intelligence, BIGAI
- **会议**: NeurIPS 2025

### LaViDa: A Large Diffusion Language Model for Multimodal Understanding.
- **链接**: [arXiv:2505.16839](https://arxiv.org/abs/2505.16839) · 📚 被引 2
- **作者**: Shufan Li, Konstantinos Kallidromitis, Hritik Bansal, Akash Gokul, Yusuke Kato, Kazuki Kozuka et al.
- **🏷️ 机构**: University of California, Los Angeles, Panasonic, University of California, Los Angeles (UCLA)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern Vision-Language Models (VLMs) can solve a wide range of tasks requiring visual reasoning. In real-world scenarios, desirable properties for VLMs include fast inference and controllable generation (e.g., constraining outputs to adhere to a desired format). However, existing autoregressive (AR) VLMs like LLaVA struggle in these aspects. Discrete diffusion models (DMs) offer a promising alternative, enabling parallel decoding for faster inference and bidirectional context for controllable generation through text-infilling. While effective in language-only settings, DMs' potential for multimodal tasks is underexplored. We introduce LaViDa, a family of VLMs built on DMs. We build LaViDa by equipping DMs with a vision encoder and jointly fine-tune the combined parts for multimodal instruction following. To address challenges encountered, LaViDa incorporates novel techniques such as complementary masking for effective training, prefix KV cache for efficient inference, and timestep shifting for high-quality sampling. Experiments show that LaViDa achieves competitive or superior performance to AR VLMs on multi-modal benchmarks such as MMMU, while offering unique advantages of DMs, including flexible speed-quality tradeoff, controllability, and bidirectional reasoning. On COCO captioning, LaViDa surpasses Open-LLaVa-Next-8B by +4.1 CIDEr with 1.92x speedup. On bidirectional tasks, it achieves +59% improvement on Constrained Poem Completion. These results demonstrate LaViDa as a strong alternative to AR VLMs. Code and models will be released in the camera-ready version.

</details>

### See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/59a9cc95f046e9125d8816ef971873e7-Abstract-Conference.html)
- **作者**: Pengteng Li, Pinhao Song, Wuyang Li, Huizai Yao, Weiyu Guo, Yijie Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Revealing Multimodal Causality with Large Language Models.
- **链接**: [arXiv:2509.17784](https://arxiv.org/abs/2509.17784) · 📚 被引 0
- **作者**: Jin Li, Shoujin Wang, Qi Zhang, Feng Liu, Tongliang Liu, Longbing Cao et al.
- **🏷️ 机构**: University of Science and Technology of China, University of Technology Sydney, Fudan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Uncovering cause-and-effect mechanisms from data is fundamental to scientific progress. While large language models (LLMs) show promise for enhancing causal discovery (CD) from unstructured data, their application to the increasingly prevalent multimodal setting remains a critical challenge. Even with the advent of multimodal LLMs (MLLMs), their efficacy in multimodal CD is hindered by two primary limitations: (1) difficulty in exploring intra- and inter-modal interactions for comprehensive causal variable identification; and (2) insufficiency to handle structural ambiguities with purely observational data. To address these challenges, we propose MLLM-CD, a novel framework for multimodal causal discovery from unstructured data. It consists of three key components: (1) a novel contrastive factor discovery module to identify genuine multimodal factors based on the interactions explored from contrastive sample pairs; (2) a statistical causal structure discovery module to infer causal relationships among discovered factors; and (3) an iterative multimodal counterfactual reasoning module to refine the discovery outcomes iteratively by incorporating the world knowledge and reasoning capabilities of MLLMs. Extensive experiments on both synthetic and real-world datasets demonstrate the effectiveness of the proposed MLLM-CD in revealing genuine factors and causal relationships among them from multimodal unstructured data.

</details>

### Watch and Listen: Understanding Audio-Visual-Speech Moments with Multimodal LLM.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/bbe0acd1ad5cf41bb87a484992a70cbd-Abstract-Conference.html)
- **作者**: Zinuo Li, Xian Zhang, Yongxin Guo, Mohammed Bennamoun, Farid Boussaïd, Girish Dwivedi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Can Large Multimodal Models Understand Agricultural Scenes? Benchmarking with AgroMind.
- **链接**: [arXiv:2505.12207](https://arxiv.org/abs/2505.12207) · 📚 被引 0
- **作者**: Qingmei Li, Yang Zhang, Zurong Mai, Yuhang Chen, Shuohong Lou, Henglian Huang et al.
- **🏷️ 机构**: Tsinghua University, National University of Singapore, SUN YAT-SEN UNIVERSITY
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) has demonstrated capabilities across various domains, but comprehensive benchmarks for agricultural remote sensing (RS) remain scarce. Existing benchmarks designed for agricultural RS scenarios exhibit notable limitations, primarily in terms of insufficient scene diversity in the dataset and oversimplified task design. To bridge this gap, we introduce AgroMind, a comprehensive agricultural remote sensing benchmark covering four task dimensions: spatial perception, object understanding, scene understanding, and scene reasoning, with a total of 13 task types, ranging from crop identification and health monitoring to environmental analysis. We curate a high-quality evaluation set by integrating eight public datasets and one private farmland plot dataset, containing 27,247 QA pairs and 19,615 images. The pipeline begins with multi-source data pre-processing, including collection, format standardization, and annotation refinement. We then generate a diverse set of agriculturally relevant questions through the systematic definition of tasks. Finally, we employ LMMs for inference, generating responses, and performing detailed examinations. We evaluated 20 open-source LMMs and 4 closed-source models on AgroMind. Experiments reveal significant performance gaps, particularly in spatial reasoning and fine-grained recognition, it is notable that human performance lags behind several leading LMMs. By establishing a standardized evaluation framework for agricultural RS, AgroMind reveals the limitations of LMMs in domain knowledge and highlights critical challenges for future work. Data and code can be accessed at https://rssysu.github.io/AgroMind/.

</details>

### SpaceServe: Spatial Multiplexing of Complementary Encoders and Decoders for Multimodal LLMs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/720e7ebc49c84252abc0754dddf80976-Abstract-Conference.html)
- **作者**: Zhicheng Li, Shuoming Zhang, Jiacheng Zhao, Siqi Li, Xiyu Shi, Yangyu Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Bifrost-1: Bridging Multimodal LLMs and Diffusion Models with Patch-level CLIP Latents.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/651516f9bc689d5508285f0784c0d90b-Abstract-Conference.html)
- **作者**: Han Lin, Jaemin Cho, Amir Zadeh, Chuan Li, Mohit Bansal
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### CyIN: Cyclic Informative Latent Space for Bridging Complete and Incomplete Multimodal Learning.
- **链接**: [arXiv:2602.04920](https://arxiv.org/abs/2602.04920) · 📚 被引 0
- **作者**: Ronghao Lin, Qiaolin He, Sijie Mai, Ying Zeng, Aolin Xiong, Li Huang et al.
- **🏷️ 机构**: Sun Yat-Sen University, SUN YAT-SEN UNIVERSITY, South China Normal University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal machine learning, mimicking the human brain's ability to integrate various modalities has seen rapid growth. Most previous multimodal models are trained on perfectly paired multimodal input to reach optimal performance. In real-world deployments, however, the presence of modality is highly variable and unpredictable, causing the pre-trained models in suffering significant performance drops and fail to remain robust with dynamic missing modalities circumstances. In this paper, we present a novel Cyclic INformative Learning framework (CyIN) to bridge the gap between complete and incomplete multimodal learning. Specifically, we firstly build an informative latent space by adopting token- and label-level Information Bottleneck (IB) cyclically among various modalities. Capturing task-related features with variational approximation, the informative bottleneck latents are purified for more efficient cross-modal interaction and multimodal fusion. Moreover, to supplement the missing information caused by incomplete multimodal input, we propose cross-modal cyclic translation by reconstruct the missing modalities with the remained ones through forward and reverse propagation process. With the help of the extracted and reconstructed informative latents, CyIN succeeds in jointly optimizing complete and incomplete multimodal learning in one unified model. Extensive experiments on 4 multimodal datasets demonstrate the superior performance of our method in both complete and diverse incomplete scenarios.

</details>

### ACT as Human: Multimodal Large Language Model Data Annotation with Critical Thinking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/22bbfc36cb32d0baf7cd1c832da6f5e9-Abstract-Conference.html)
- **作者**: Lequan Lin, Dai Shi, Andi Han, Feng Chen, Qiuzheng Chen, Jiawen Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Table2LaTeX-RL: High-Fidelity LaTeX Code Generation from Table Images via Reinforced Multimodal Language Models.
- **链接**: [arXiv:2509.17589](https://arxiv.org/abs/2509.17589) · 📚 被引 0
- **作者**: Jun Ling, Yao Qi, Tao Huang, Shibo Zhou, Yanqin Huang, Jiang Yang et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China, Zhejiang Lab, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we address the task of table image to LaTeX code generation, with the goal of automating the reconstruction of high-quality, publication-ready tables from visual inputs. A central challenge of this task lies in accurately handling complex tables -- those with large sizes, deeply nested structures, and semantically rich or irregular cell content -- where existing methods often fail. We begin with a comprehensive analysis, identifying key challenges and highlighting the limitations of current evaluation protocols. To overcome these issues, we propose a reinforced multimodal large language model (MLLM) framework, where a pre-trained MLLM is fine-tuned on a large-scale table-to-LaTeX dataset. To further improve generation quality, we introduce a dual-reward reinforcement learning strategy based on Group Relative Policy Optimization (GRPO). Unlike standard approaches that optimize purely over text outputs, our method incorporates both a structure-level reward on LaTeX code and a visual fidelity reward computed from rendered outputs, enabling direct optimization of the visual output quality. We adopt a hybrid evaluation protocol combining TEDS-Structure and CW-SSIM, and show that our method achieves state-of-the-art performance, particularly on structurally complex tables, demonstrating the effectiveness and robustness of our approach.

</details>

### On Fairness of Unified Multimodal Large Language Model for Image Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d33e36e286131629c540fe0f0761f1f7-Abstract-Conference.html)
- **作者**: Ming Liu, Hao Chen, Jindong Wang, Liwen Wang, Bhiksha Raj, Wensheng Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### Extremely Simple Multimodal Outlier Synthesis for Out-of-Distribution Detection and Segmentation.
- **链接**: [arXiv:2505.16985](https://arxiv.org/abs/2505.16985) · [代码](https://github.com/mona4399/FeatureMixing) · 📚 被引 2
- **作者**: Moru Liu, Hao Dong, Jessica Kelly, Olga Fink, Mario Trapp
- **🏷️ 机构**: Technische Universität München, Peking University, Fraunhofer IKS
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection and segmentation are crucial for deploying machine learning models in safety-critical applications such as autonomous driving and robot-assisted surgery. While prior research has primarily focused on unimodal image data, real-world applications are inherently multimodal, requiring the integration of multiple modalities for improved OOD detection. A key challenge is the lack of supervision signals from unknown data, leading to overconfident predictions on OOD samples. To address this challenge, we propose Feature Mixing, an extremely simple and fast method for multimodal outlier synthesis with theoretical support, which can be further optimized to help the model better distinguish between in-distribution (ID) and OOD data. Feature Mixing is modality-agnostic and applicable to various modality combinations. Additionally, we introduce CARLA-OOD, a novel multimodal dataset for OOD segmentation, featuring synthetic OOD objects across diverse scenes and weather conditions. Extensive experiments on SemanticKITTI, nuScenes, CARLA-OOD datasets, and the MultiOOD benchmark demonstrate that Feature Mixing achieves state-of-the-art performance with a $10 \times$ to $370 \times$ speedup. Our source code and dataset will be available at https://github.com/mona4399/FeatureMixing.

</details>

### Plug-and-play Feature Causality Decomposition for Multimodal Representation Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/55123f38c9f4acf417335cff41be6e27-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ye Liu, Zihan Ji, Hongmin Cai
- **🏷️ 机构**: South China University of Technology
- **会议**: NeurIPS 2025

### ThinkSound: Chain-of-Thought Reasoning in Multimodal LLMs for Audio Generation and Editing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/710f3f8473b93394505a082f9a8f3ba2-Abstract-Conference.html)
- **作者**: Huadai Liu, Kaicheng Luo, Jialei Wang, Wen Wang, Qian Chen, Zhou Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### From Pose to Muscle: Multimodal Learning for Piano Hand Muscle Electromyography.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a7d80c990c77ae2570087243ec802314-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ruofan Liu, Yichen Peng, Takanori Oku, Chen-Chieh Liao, Erwin Wu, Shinichi Furuya et al.
- **🏷️ 机构**: Institute of Science Tokyo, Japan Advanced Institute of Science and Technology, Tokyo Institute of Technology, Shibaura Institute of Technology
- **会议**: NeurIPS 2025

### Hierarchical Information Aggregation for Incomplete Multimodal Alzheimer's Disease Diagnosis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4da4dd613cc9e63932d643b9c6e8f86f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chengliang Liu, Yuanxi Que, Qihao Xu, Yabo Liu, Jie Wen, Jinghua Wang et al.
- **🏷️ 机构**: Shenzhen University, Harbin Institute of Technology, Harbin Institute of Technology, Shenzhen
- **会议**: NeurIPS 2025

### Mitigating Hallucination Through Theory-Consistent Symmetric Multimodal Preference Optimization.
- **链接**: [arXiv:2506.11712](https://arxiv.org/abs/2506.11712) · 📚 被引 0
- **作者**: Wenqi Liu, Xuemeng Song, Jiaxi Li, Yinwei Wei, Na Zheng, Jianhua Yin et al.
- **🏷️ 机构**: Shandong University, City University of Hong Kong, University of Georgia
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Direct Preference Optimization (DPO) has emerged as an effective approach for mitigating hallucination in Multimodal Large Language Models (MLLMs). Although existing methods have achieved significant progress by utilizing vision-oriented contrastive objectives for enhancing MLLMs' attention to visual inputs and hence reducing hallucination, they suffer from non-rigorous optimization objective function and indirect preference supervision. To address these limitations, we propose a Symmetric Multimodal Preference Optimization (SymMPO), which conducts symmetric preference learning with direct preference supervision (i.e., response pairs) for visual understanding enhancement, while maintaining rigorous theoretical alignment with standard DPO. In addition to conventional ordinal preference learning, SymMPO introduces a preference margin consistency loss to quantitatively regulate the preference gap between symmetric preference pairs. Comprehensive evaluation across five benchmarks demonstrate SymMPO's superior performance, validating its effectiveness in hallucination mitigation of MLLMs.

</details>

### Continual Multimodal Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/453a27b717972ef94a9a9113d236ad2f-Abstract-Conference.html)
- **作者**: Xiaohao Liu, Xiaobo Xia, See-Kiong Ng, Tat-Seng Chua
- **🏷️ 机构**: NUS
- **会议**: NeurIPS 2025

### Multimodal Disease Progression Modeling via Spatiotemporal Disentanglement and Multiscale Alignment.
- **链接**: [arXiv:2510.11112](https://arxiv.org/abs/2510.11112) · 📚 被引 0
- **作者**: Chen Liu, Wenfang Yao, Kejing Yin, William K. Cheung, Jing Qin
- **🏷️ 机构**: The Hong Kong Polytechnic University, Hong Kong Baptist University, Hong Kong Polytechnic University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Longitudinal multimodal data, including electronic health records (EHR) and sequential chest X-rays (CXRs), is critical for modeling disease progression, yet remains underutilized due to two key challenges: (1) redundancy in consecutive CXR sequences, where static anatomical regions dominate over clinically-meaningful dynamics, and (2) temporal misalignment between sparse, irregular imaging and continuous EHR data. We introduce $\texttt{DiPro}$, a novel framework that addresses these challenges through region-aware disentanglement and multi-timescale alignment. First, we disentangle static (anatomy) and dynamic (pathology progression) features in sequential CXRs, prioritizing disease-relevant changes. Second, we hierarchically align these static and dynamic CXR features with asynchronous EHR data via local (pairwise interval-level) and global (full-sequence) synchronization to model coherent progression pathways. Extensive experiments on the MIMIC dataset demonstrate that $\texttt{DiPro}$ could effectively extract temporal clinical dynamics and achieve state-of-the-art performance on both disease progression identification and general ICU prediction tasks.

</details>

### Situat3DChange: Situated 3D Change Understanding Dataset for Multimodal Large Language Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/832eca9904003740d25abef22b07abdb-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Ruiping Liu, Junwei Zheng, Yufan Chen, Zirui Wang, Kunyu Peng, Kailun Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### The Indra Representation Hypothesis for Multimodal Alignment.
- **链接**: [arXiv:2604.04496](https://arxiv.org/abs/2604.04496) · [代码](https://github.com/Jianglin954/Indra) · 📚 被引 0
- **作者**: Jianglin Lu, Hailing Wang, Kuo Yang, Yitian Zhang, Simon Jenni, Yun Fu
- **🏷️ 机构**: Northeastern University, Adobe Systems
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have uncovered an interesting phenomenon: unimodal foundation models tend to learn convergent representations, regardless of differences in architecture, training objectives, or data modalities. However, these representations are essentially internal abstractions of samples that characterize samples independently, leading to limited expressiveness. In this paper, we propose The Indra Representation Hypothesis, inspired by the philosophical metaphor of Indra's Net. We argue that representations from unimodal foundation models are converging to implicitly reflect a shared relational structure underlying reality, akin to the relational ontology of Indra's Net. We formalize this hypothesis using the V-enriched Yoneda embedding from category theory, defining the Indra representation as a relational profile of each sample with respect to others. This formulation is shown to be unique, complete, and structure-preserving under a given cost function. We instantiate the Indra representation using angular distance and evaluate it in cross-model and cross-modal scenarios involving vision, language, and audio. Extensive experiments demonstrate that Indra representations consistently enhance robustness and alignment across architectures and modalities, providing a theoretically grounded and practical framework for training-free alignment of unimodal foundation models. Our code is available at https://github.com/Jianglin954/Indra.

</details>

### Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/8196be81e68289d7a9ece21ed7f5750a-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Yaxin Luo, Zhaoyi Li, Jiacheng Liu, Jiacheng Cui, Xiaohan Zhao, Zhiqiang Shen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### OpenOmni: Advancing Open-Source Omnimodal Large Language Models with Progressive Multimodal Alignment and Real-time Emotional Speech Synthesis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/e92381dba235a8309f08ce46376189a9-Abstract-Conference.html) · 📚 被引 0
- **作者**: Run Luo, Ting-En Lin, Haonan Zhang, Yuchuan Wu, Xiong Liu, Yongbin Li et al.
- **🏷️ 机构**: Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Chinese Academy of Sciences, Alibaba Group, University of Electronic Science and Technology of China
- **会议**: NeurIPS 2025

### OmniResponse: Online Multimodal Conversational Response Generation in Dyadic Interactions.
- **链接**: [arXiv:2505.21724](https://arxiv.org/abs/2505.21724) · 📚 被引 0
- **作者**: Cheng Luo, Jianghui Wang, Bing Li, Siyang Song, Bernard Ghanem
- **🏷️ 机构**: King Abdullah University of Science and Technology, Beijing Institute for General Artificial Intelligence, KAUST
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce Online Multimodal Conversational Response Generation (OMCRG), a novel task designed to produce synchronized verbal and non-verbal listener feedback online, based on the speaker's multimodal inputs. OMCRG captures natural dyadic interactions and introduces new challenges in aligning generated audio with listeners' facial responses. To tackle these challenges, we incorporate text as an intermediate modality to connect audio and facial responses. We propose OmniResponse, a Multimodal Large Language Model (MLLM) that autoregressively generates accurate multimodal listener responses. OmniResponse leverages a pretrained LLM enhanced with two core components: Chrono-Text Markup, which precisely timestamps generated text tokens, and TempoVoice, a controllable online text-to-speech (TTS) module that outputs speech synchronized with facial responses. To advance OMCRG research, we offer ResponseNet, a dataset of 696 detailed dyadic interactions featuring synchronized split-screen videos, multichannel audio, transcripts, and annotated facial behaviors. Comprehensive evaluations on ResponseNet demonstrate that OmniResponse outperforms baseline models in terms of semantic speech content, audio-visual synchronization, and generation quality. Our dataset, code, and models are publicly available.

</details>

### Unlocking Multimodal Mathematical Reasoning via Process Reward Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/4757e472d97ca980c24a487622f7ff00-Abstract-Conference.html) · 📚 被引 0
- **作者**: Ruilin Luo, Zhuofan Zheng, Lei Wang, Yifan Wang, Xinzhe Ni, Zicheng Lin et al.
- **🏷️ 机构**: Tsinghua University, ByteDance Inc., Griffith University
- **会议**: NeurIPS 2025

### IRRISIGHT: A Large-Scale Multimodal Dataset and Scalable Pipeline to Address Irrigation and Water Management in Agriculture.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/0821a1413339bf79ba01876783d95c53-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Nibir Chandra Mandal, Oishee Bintey Hoque, Mandy L. Wilson, Samarth Swarup, Sayjro Kossi Nouwakpo, Abhijin Adiga et al.
- **🏷️ 机构**: University of Virginia, Charlottesville, University of Virginia, US Department of Agriculture
- **会议**: NeurIPS 2025

### CrypticBio: A Large Multimodal Dataset for Visually Confusing Species.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/0216c27a05dc3ca81677734fca1f7aca-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Georgiana Manolache, Gerard Schouten, Joaquin Vanschoren
- **🏷️ 机构**: Fontys University of Applied Sciences, Eindhoven University of Technology, Google DeepMind
- **会议**: NeurIPS 2025

### MAESTRO : Adaptive Sparse Attention and Robust Learning for Multimodal Dynamic Time Series.
- **链接**: [arXiv:2509.25278](https://arxiv.org/abs/2509.25278) · 📚 被引 0
- **作者**: Payal Mohapatra, Yueyuan Sui, Akash Pandey, Stephen Xia, Qi Zhu
- **🏷️ 机构**: Northwestern University, Yale University, Nanjing University of Aeronautics and Astronautics
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> From clinical healthcare to daily living, continuous sensor monitoring across multiple modalities has shown great promise for real-world intelligent decision-making but also faces various challenges. In this work, we introduce MAESTRO, a novel framework that overcomes key limitations of existing multimodal learning approaches: (1) reliance on a single primary modality for alignment, (2) pairwise modeling of modalities, and (3) assumption of complete modality observations. These limitations hinder the applicability of these approaches in real-world multimodal time-series settings, where primary modality priors are often unclear, the number of modalities can be large (making pairwise modeling impractical), and sensor failures often result in arbitrary missing observations. At its core, MAESTRO facilitates dynamic intra- and cross-modal interactions based on task relevance, and leverages symbolic tokenization and adaptive attention budgeting to construct long multimodal sequences, which are processed via sparse cross-modal attention. The resulting cross-modal tokens are routed through a sparse Mixture-of-Experts (MoE) mechanism, enabling black-box specialization under varying modality combinations. We evaluate MAESTRO against 10 baselines on four diverse datasets spanning three applications, and observe average relative improvements of 4% and 8% over the best existing multimodal and multivariate approaches, respectively, under complete observations. Under partial observations -- with up to 40% of missing modalities -- MAESTRO achieves an average 9% improvement. Further analysis also demonstrates the robustness and efficiency of MAESTRO's sparse, modality-aware design for learning from dynamic time series.

</details>

### Learning Reconfigurable Representations for Multimodal Federated Learning with Missing Data.
- **链接**: [arXiv:2510.22880](https://arxiv.org/abs/2510.22880) · [代码](https://github.com/nmduonggg/PEPSY) · 📚 被引 0
- **作者**: Duong M. Nguyen, Trong Nghia Hoang, Thanh Trung Huynh, Quoc Viet Hung Nguyen, Phi Le Nguyen
- **🏷️ 机构**: University of Illinois Urbana-Champaign, Washington State University, VinUniversity
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal federated learning in real-world settings often encounters incomplete and heterogeneous data across clients. This results in misaligned local feature representations that limit the effectiveness of model aggregation. Unlike prior work that assumes either differing modality sets without missing input features or a shared modality set with missing features across clients, we consider a more general and realistic setting where each client observes a different subset of modalities and might also have missing input features within each modality. To address the resulting misalignment in learned representations, we propose a new federated learning framework featuring locally adaptive representations based on learnable client-side embedding controls that encode each client's data-missing patterns. These embeddings serve as reconfiguration signals that align the globally aggregated representation with each client's local context, enabling more effective use of shared information. Furthermore, the embedding controls can be algorithmically aggregated across clients with similar data-missing patterns to enhance the robustness of reconfiguration signals in adapting the global representation. Empirical results on multiple federated multimodal benchmarks with diverse data-missing patterns across clients demonstrate the efficacy of the proposed method, achieving up to 36.45\% performance improvement under severe data incompleteness. The method is also supported by a theoretical analysis with an explicit performance bound that matches our empirical observations. Our source codes are provided at https://github.com/nmduonggg/PEPSY

</details>

### Point-RFT: Improving Multimodal Reasoning with Visually Grounded Reinforcement Finetuning.
- **链接**: [arXiv:2505.19702](https://arxiv.org/abs/2505.19702) · 📚 被引 0
- **作者**: Minheng Ni, Zhengyuan Yang, Linjie Li, Chung-Ching Lin, Kevin Lin, Wangmeng Zuo et al.
- **🏷️ 机构**: Hong Kong Polytechnic University, Microsoft, Harbin Institute of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in large language models have significantly improved textual reasoning through the effective use of Chain-of-Thought (CoT) and reinforcement learning. However, extending these successes to vision-language tasks remains challenging due to inherent limitations in text-only CoT, such as visual hallucinations and insufficient multimodal integration. In this paper, we introduce Point-RFT, a multimodal reasoning framework explicitly designed to leverage visually grounded CoT reasoning for visual document understanding. Our approach consists of two stages: First, we conduct format finetuning using a curated dataset of 71K diverse visual reasoning problems, each annotated with detailed, step-by-step rationales explicitly grounded to corresponding visual elements. Second, we employ reinforcement finetuning targeting visual document understanding. On ChartQA, our approach improves accuracy from 70.88% (format-finetuned baseline) to 90.04%, surpassing the 83.92% accuracy achieved by reinforcement finetuning relying solely on text-based CoT. The result shows that our grounded CoT is more effective for multimodal reasoning compared with the text-only CoT. Moreover, Point-RFT exhibits superior generalization capability across several out-of-domain visual document reasoning benchmarks, including CharXiv, PlotQA, IconQA, TabMWP, etc., and highlights its potential in complex real-world scenarios.

</details>

## 跨领域论文（完整笔记在其他领域）

- STSBench: A Spatio-temporal Scenario Benchmark for Multi-modal Large Language Models in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- mmWalk: Towards Multi-modal Multi-view Walking Assistance. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
