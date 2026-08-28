# Multimodal — 2024 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 92 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### WikiDO: A New Benchmark Evaluating Cross-Modal Retrieval for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/fe759454e97d56d3aea73a1512364d5f-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 2
- **作者**: Tankala Pavan Kalyan, Piyush Singh Pasi, Sahil Dharod, Azeem Motiwala, Preethi Jyothi, Aditi Chaudhary et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI.
- **链接**: [arXiv:2408.03361](https://arxiv.org/abs/2408.03361) · 📚 被引 14
- **作者**: Pengcheng Chen, Jin Ye, Guoan Wang, Yanjun Li, Zhongying Deng, Wei Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision-Language Models (LVLMs) are capable of handling diverse data types such as imaging, text, and physiological signals, and can be applied in various fields. In the medical field, LVLMs have a high potential to offer substantial assistance for diagnosis and treatment. Before that, it is crucial to develop benchmarks to evaluate LVLMs' effectiveness in various medical applications. Current benchmarks are often built upon specific academic literature, mainly focusing on a single domain, and lacking varying perceptual granularities. Thus, they face specific challenges, including limited clinical relevance, incomplete evaluations, and insufficient guidance for interactive LVLMs. To address these limitations, we developed the GMAI-MMBench, the most comprehensive general medical AI benchmark with well-categorized data structure and multi-perceptual granularity to date. It is constructed from 284 datasets across 38 medical image modalities, 18 clinical-related tasks, 18 departments, and 4 perceptual granularities in a Visual Question Answering (VQA) format. Additionally, we implemented a lexical tree structure that allows users to customize evaluation tasks, accommodating various assessment needs and substantially supporting medical AI research and applications. We evaluated 50 LVLMs, and the results show that even the advanced GPT-4o only achieves an accuracy of 53.96%, indicating significant room for improvement. Moreover, we identified five key insufficiencies in current cutting-edge LVLMs that need to be addressed to advance the development of better medical applications. We believe that GMAI-MMBench will stimulate the community to build the next generation of LVLMs toward GMAI.

</details>

### Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/f2b9e8e7a36d43ddfd3d55113d56b1e0-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 5
- **作者**: Kehan Guo, Bozhao Nan, Yujun Zhou, Taicheng Guo, Zhichun Guo, Mihir Surve et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MLLM-CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/32923dff09f75cf1974c145764a523e2-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 5
- **作者**: Jihyung Kil, Zheda Mai, Justin Lee, Arpita Chowdhury, Zihe Wang, Kerrie Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models.
- **链接**: [arXiv:2406.05862](https://arxiv.org/abs/2406.05862)
- **作者**: Ziqiang Liu, Feiteng Fang, Xi Feng, Xeron Du, Chenhao Zhang, Noah Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advancements in the development of multimodal large language models (MLLMs) have consistently led to new breakthroughs on various benchmarks. In response, numerous challenging and comprehensive benchmarks have been proposed to more accurately assess the capabilities of MLLMs. However, there is a dearth of exploration of the higher-order perceptual capabilities of MLLMs. To fill this gap, we propose the Image Implication understanding Benchmark, II-Bench, which aims to evaluate the model's higher-order perception of images. Through extensive experiments on II-Bench across multiple MLLMs, we have made significant findings. Initially, a substantial gap is observed between the performance of MLLMs and humans on II-Bench. The pinnacle accuracy of MLLMs attains 74.8%, whereas human accuracy averages 90%, peaking at an impressive 98%. Subsequently, MLLMs perform worse on abstract and complex images, suggesting limitations in their ability to understand high-level semantics and capture image details. Finally, it is observed that most models exhibit enhanced accuracy when image sentiment polarity hints are incorporated into the prompts. This observation underscores a notable deficiency in their inherent understanding of image sentiment. We believe that II-Bench will inspire the community to develop the next generation of MLLMs, advancing the journey towards expert artificial general intelligence (AGI). II-Bench is publicly available at https://huggingface.co/datasets/m-a-p/II-Bench.

</details>

### DevBench: A multimodal developmental benchmark for language learning.
- **链接**: [arXiv:2406.10215](https://arxiv.org/abs/2406.10215) · 📚 被引 1
- **作者**: Alvin Wei Ming Tan, Chunhua Yu, Bria Long, Wanjing Ma, Tonya Murray, Rebecca D. Silverman et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How (dis)similar are the learning trajectories of vision-language models and children? Recent modeling work has attempted to understand the gap between models' and humans' data efficiency by constructing models trained on less data, especially multimodal naturalistic data. However, such models are often evaluated on adult-level benchmarks, with limited breadth in language abilities tested, and without direct comparison to behavioral data. We introduce DevBench, a multimodal benchmark comprising seven language evaluation tasks spanning the domains of lexical, syntactic, and semantic ability, with behavioral data from both children and adults. We evaluate a set of vision-language models on these tasks, comparing models and humans not only on accuracy but on their response patterns. Across tasks, models exhibit variation in their closeness to human response patterns, and models that perform better on a task also more closely resemble human behavioral responses. We also examine the developmental trajectory of OpenCLIP over training, finding that greater training results in closer approximations to adult response patterns. DevBench thus provides a benchmark for comparing models to human language development. These comparisons highlight ways in which model and human language learning processes diverge, providing insight into entry points for improving language models.

</details>

### WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/d1fa821312040303b089ae529dbf81a6-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 1
- **作者**: Michael Wornow, Avanika Narayan, Ben Viggiano, Ishan S. Khare, Tathagat Verma, Tibor Thompson et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/586640cda3db2dc77349013dcefee456-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 8
- **作者**: Yichi Zhang, Yao Huang, Yitong Sun, Chang Liu, Zhe Zhao, Zhengwei Fang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Unified Insights: Harnessing Multi-modal Data for Phenotype Imputation via View Decoupling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/05fbf28602c5c2c994499db18363fbbb-Abstract-Conference.html) · 📚 被引 0
- **作者**: Qiannan Zhang, Weishen Pan, Zilong Bai, Chang Su, Fei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### ChatTracker: Enhancing Visual Tracking Performance via Chatting with Multimodal Large Language Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/458567910b6d21f438f22aa20c036723-Abstract-Conference.html)
- **作者**: Yiming Sun, Fan Yu, Shaoxiang Chen, Yu Zhang, Junwei Huang, Yang Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### XMask3D: Cross-modal Mask Reasoning for Open Vocabulary 3D Semantic Segmentation.
- **链接**: [arXiv:2411.13243](https://arxiv.org/abs/2411.13243) · [代码](https://github.com/wangzy22/XMask3D) · 📚 被引 0
- **作者**: Ziyi Wang, Yanbo Wang, Xumin Yu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing methodologies in open vocabulary 3D semantic segmentation primarily concentrate on establishing a unified feature space encompassing 3D, 2D, and textual modalities. Nevertheless, traditional techniques such as global feature alignment or vision-language model distillation tend to impose only approximate correspondence, struggling notably with delineating fine-grained segmentation boundaries. To address this gap, we propose a more meticulous mask-level alignment between 3D features and the 2D-text embedding space through a cross-modal mask reasoning framework, XMask3D. In our approach, we developed a mask generator based on the denoising UNet from a pre-trained diffusion model, leveraging its capability for precise textual control over dense pixel representations and enhancing the open-world adaptability of the generated masks. We further integrate 3D global features as implicit conditions into the pre-trained 2D denoising UNet, enabling the generation of segmentation masks with additional 3D geometry awareness. Subsequently, the generated 2D masks are employed to align mask-level 3D representations with the vision-language feature space, thereby augmenting the open vocabulary capability of 3D geometry embeddings. Finally, we fuse complementary 2D and 3D mask features, resulting in competitive performance across multiple benchmarks for 3D open vocabulary semantic segmentation. Code is available at https://github.com/wangzy22/XMask3D.

</details>

### CountGD: Multi-Modal Open-World Counting.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/57c56985d9afe89bf78a8264c91071aa-Abstract-Conference.html) · 📚 被引 27
- **作者**: Niki Amini-Naieni, Tengda Han, Andrew Zisserman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/81a60d18e010b27b36cd465c6604b915-Abstract-Conference.html) · 📚 被引 14
- **作者**: Jiannan Wu, Muyan Zhong, Sen Xing, Zeqiang Lai, Zhaoyang Liu, Zhe Chen et al.
- **🏷️ 机构**: Shanghai AI Lab, Tsinghua / Shanghai AI Lab
- **会议**: NeurIPS 2024

### UKnow: A Unified Knowledge Protocol with Multimodal Knowledge Graph Datasets for Reasoning and Vision-Language Pre-Training.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/126784e4d5a92afff92d13aee155554b-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 1
- **作者**: Biao Gong, Shuai Tan, Yutong Feng, Xiaoying Xie, Yuyuan Li, Chaochao Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/40b9196c25fe1d64d87ca3a80a91d0ce-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 6
- **作者**: Anas Awadalla, Le Xue, Oscar Lo, Manli Shu, Hannah Lee, Etash Kumar Guha et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/27571b74d6cd650b8eb6cf1837953ae8-Abstract-Conference.html) · 📚 被引 5
- **作者**: Brandon Huang, Chancharik Mitra, Leonid Karlinsky, Assaf Arbelle, Trevor Darrell, Roei Herzig
- **🏷️ 机构**: UC Berkeley
- **会议**: NeurIPS 2024

### MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/4a3a14b9536806a0522930007c5512f7-Abstract-Conference.html) · 📚 被引 12
- **作者**: Leyang Shen, Gongwei Chen, Rui Shao, Weili Guan, Liqiang Nie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Implicit Multimodal Alignment: On the Generalization of Frozen LLMs to Multimodal Inputs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ec3c79dc0c2b85532cfd1012a4aaa923-Abstract-Conference.html) · 📚 被引 4
- **作者**: Mustafa Shukor, Matthieu Cord
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### FIRE: A Dataset for Feedback Integration and Refinement Evaluation of Multimodal Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b83bea9688047be30f54034c55716854-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 1
- **作者**: Pengxiang Li, Zhi Gao, Bofei Zhang, Tao Yuan, Yuwei Wu, Mehrtash Harandi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c78f639424b8d89ceb4f2efbb4dfe4f4-Abstract-Conference.html) · 📚 被引 9
- **作者**: Haoyu Chen, Wenbo Li, Jinjin Gu, Jingjing Ren, Sixiang Chen, Tian Ye et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts.
- **链接**: [arXiv:2405.05949](https://arxiv.org/abs/2405.05949) · [代码](https://github.com/SHI-Labs/CuMo) · 📚 被引 4
- **作者**: Jiachen Li, Xinyao Wang, Sijie Zhu, Chia-Wen Kuo, Lu Xu, Fan Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in Multimodal Large Language Models (LLMs) have focused primarily on scaling by increasing text-image pair data and enhancing LLMs to improve performance on multimodal tasks. However, these scaling approaches are computationally expensive and overlook the significance of improving model capabilities from the vision side. Inspired by the successful applications of Mixture-of-Experts (MoE) in LLMs, which improves model scalability during training while keeping inference costs similar to those of smaller models, we propose CuMo. CuMo incorporates Co-upcycled Top-K sparsely-gated Mixture-of-experts blocks into both the vision encoder and the MLP connector, thereby enhancing the multimodal LLMs with minimal additional activated parameters during inference. CuMo first pre-trains the MLP blocks and then initializes each expert in the MoE block from the pre-trained MLP block during the visual instruction tuning stage. Auxiliary losses are used to ensure a balanced loading of experts. CuMo outperforms state-of-the-art multimodal LLMs across various VQA and visual-instruction-following benchmarks using models within each model size group, all while training exclusively on open-sourced datasets. The code and model weights for CuMo are open-sourced at https://github.com/SHI-Labs/CuMo.

</details>

### SciFIBench: Benchmarking Large Multimodal Models for Scientific Figure Interpretation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/217bb44ab14621754db8a392163e6b07-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 1
- **作者**: Jonathan Roberts, Kai Han, Neil Houlsby, Samuel Albanie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Terra: A Multimodal Spatio-Temporal Dataset Spanning the Earth.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/7a6a7fbd1ee0c9684b3f919f79d129ef-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 12
- **作者**: Wei Chen, Xixuan Hao, Yuankai Wu, Yuxuan Liang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Facilitating Multimodal Classification via Dynamically Learning Modality Gap.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/71b17f00017da0d73823ccf7fbce2d4f-Abstract-Conference.html) · 📚 被引 10
- **作者**: Yang Yang, Fengqiang Wan, Qing-Yuan Jiang, Yi Xu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Unraveling Molecular Structure: A Multimodal Spectroscopic Dataset for Chemistry.
- **链接**: [arXiv:2407.17492](https://arxiv.org/abs/2407.17492) · 📚 被引 14
- **作者**: Marvin Alberts, Oliver Schilter, Federico Zipoli, Nina Hartrampf, Teodoro Laino
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spectroscopic techniques are essential tools for determining the structure of molecules. Different spectroscopic techniques, such as Nuclear magnetic resonance (NMR), Infrared spectroscopy, and Mass Spectrometry, provide insight into the molecular structure, including the presence or absence of functional groups. Chemists leverage the complementary nature of the different methods to their advantage. However, the lack of a comprehensive multimodal dataset, containing spectra from a variety of spectroscopic techniques, has limited machine-learning approaches mostly to single-modality tasks for predicting molecular structures from spectra. Here we introduce a dataset comprising simulated $^1$H-NMR, $^{13}$C-NMR, HSQC-NMR, Infrared, and Mass spectra (positive and negative ion modes) for 790k molecules extracted from chemical reactions in patent data. This dataset enables the development of foundation models for integrating information from multiple spectroscopic modalities, emulating the approach employed by human experts. Additionally, we provide benchmarks for evaluating single-modality tasks such as structure elucidation, predicting the spectra for a target molecule, and functional group predictions. This dataset has the potential automate structure elucidation, streamlining the molecular discovery pipeline from synthesis to structure determination. The dataset and code for the benchmarks can be found at https://rxn4chemistry.github.io/multimodal-spectroscopic-dataset.

</details>

### The Multimodal Universe: Enabling Large-Scale Machine Learning with 100 TB of Astronomical Scientific Data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6a57493d35fefea59d06396c7cb69228-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 4
- **作者**: Eirini Angeloudi, Jeroen Audenaert, Micah Bowles, Benjamin M. Boyd, David Chemaly, Brian Cherinka et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?
- **链接**: [arXiv:2407.10956](https://arxiv.org/abs/2407.10956) · 📚 被引 6
- **作者**: Ruisheng Cao, Fangyu Lei, Haoyuan Wu, Jixuan Chen, Yeqiao Fu, Hongcheng Gao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data science and engineering workflows often span multiple stages, from warehousing to orchestration, using tools like BigQuery, dbt, and Airbyte. As vision language models (VLMs) advance in multimodal understanding and code generation, VLM-based agents could potentially automate these workflows by generating SQL queries, Python code, and GUI operations. This automation can improve the productivity of experts while democratizing access to large-scale data analysis. In this paper, we introduce Spider2-V, the first multimodal agent benchmark focusing on professional data science and engineering workflows, featuring 494 real-world tasks in authentic computer environments and incorporating 20 enterprise-level professional applications. These tasks, derived from real-world use cases, evaluate the ability of a multimodal agent to perform data-related tasks by writing code and managing the GUI in enterprise data software systems. To balance realistic simulation with evaluation simplicity, we devote significant effort to developing automatic configurations for task setup and carefully crafting evaluation metrics for each task. Furthermore, we supplement multimodal agents with comprehensive documents of these enterprise data software systems. Our empirical evaluation reveals that existing state-of-the-art LLM/VLM-based agents do not reliably automate full data workflows (14.0% success). Even with step-by-step guidance, these agents still underperform in tasks that require fine-grained, knowledge-intensive GUI actions (16.2%) and involve remote cloud-hosted workspaces (10.6%). We hope that Spider2-V paves the way for autonomous multimodal agents to transform the automation of data science and engineering workflow. Our code and data are available at https://spider2-v.github.io.

</details>

### Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with Instruction Tuning.
- **链接**: [arXiv:2406.11161](https://arxiv.org/abs/2406.11161) · 📚 被引 108
- **作者**: Zebang Cheng, Zhi-Qi Cheng, Jun-Yan He, Kai Wang, Yuxiang Lin, Zheng Lian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate emotion perception is crucial for various applications, including human-computer interaction, education, and counseling. However, traditional single-modality approaches often fail to capture the complexity of real-world emotional expressions, which are inherently multimodal. Moreover, existing Multimodal Large Language Models (MLLMs) face challenges in integrating audio and recognizing subtle facial micro-expressions. To address this, we introduce the MERR dataset, containing 28,618 coarse-grained and 4,487 fine-grained annotated samples across diverse emotional categories. This dataset enables models to learn from varied scenarios and generalize to real-world applications. Furthermore, we propose Emotion-LLaMA, a model that seamlessly integrates audio, visual, and textual inputs through emotion-specific encoders. By aligning features into a shared space and employing a modified LLaMA model with instruction tuning, Emotion-LLaMA significantly enhances both emotional recognition and reasoning capabilities. Extensive evaluations show Emotion-LLaMA outperforms other MLLMs, achieving top scores in Clue Overlap (7.83) and Label Overlap (6.25) on EMER, an F1 score of 0.9036 on MER2023-SEMI challenge, and the highest UAR (45.59) and WAR (59.37) in zero-shot evaluations on DFEW dataset.

</details>

### DrivAerNet++: A Large-Scale Multimodal Car Dataset with Computational Fluid Dynamics Simulations and Deep Learning Benchmarks.
- **链接**: [arXiv:2406.09624](https://arxiv.org/abs/2406.09624) · [代码](https://github.com/Mohamedelrefaie/DrivAerNet) · 📚 被引 13
- **作者**: Mohamed Elrefaie, Florin Morar, Angela Dai, Faez Ahmed
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present DrivAerNet++, the largest and most comprehensive multimodal dataset for aerodynamic car design. DrivAerNet++ comprises 8,000 diverse car designs modeled with high-fidelity computational fluid dynamics (CFD) simulations. The dataset includes diverse car configurations such as fastback, notchback, and estateback, with different underbody and wheel designs to represent both internal combustion engines and electric vehicles. Each entry in the dataset features detailed 3D meshes, parametric models, aerodynamic coefficients, and extensive flow and surface field data, along with segmented parts for car classification and point cloud data. This dataset supports a wide array of machine learning applications including data-driven design optimization, generative modeling, surrogate model training, CFD simulation acceleration, and geometric classification. With more than 39 TB of publicly available engineering data, DrivAerNet++ fills a significant gap in available resources, providing high-quality, diverse data to enhance model training, promote generalization, and accelerate automotive design processes. Along with rigorous dataset validation, we also provide ML benchmarking results on the task of aerodynamic drag prediction, showcasing the breadth of applications supported by our dataset. This dataset is set to significantly impact automotive design and broader engineering disciplines by fostering innovation and improving the fidelity of aerodynamic evaluations. Dataset and code available at: https://github.com/Mohamedelrefaie/DrivAerNet.

</details>

### Data curation via joint example selection further accelerates multimodal learning.
- **链接**: [arXiv:2406.17711](https://arxiv.org/abs/2406.17711) · 📚 被引 5
- **作者**: Talfan Evans, Nikhil Parthasarathy, Hamza Merzic, Olivier J. Hénaff
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data curation is an essential component of large-scale pretraining. In this work, we demonstrate that jointly selecting batches of data is more effective for learning than selecting examples independently. Multimodal contrastive objectives expose the dependencies between data and thus naturally yield criteria for measuring the joint learnability of a batch. We derive a simple and tractable algorithm for selecting such batches, which significantly accelerate training beyond individually-prioritized data points. As performance improves by selecting from larger super-batches, we also leverage recent advances in model approximation to reduce the associated computational overhead. As a result, our approach--multimodal contrastive learning with joint example selection (JEST)--surpasses state-of-the-art models with up to 13$\times$ fewer iterations and 10$\times$ less computation. Essential to the performance of JEST is the ability to steer the data selection process towards the distribution of smaller, well-curated datasets via pretrained reference models, exposing the level of data curation as a new dimension for neural scaling laws.

</details>

### Make-it-Real: Unleashing Large Multimodal Model for Painting 3D Objects with Realistic Materials.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b3b55c366d641c07180c40e4f978f311-Abstract-Conference.html) · 📚 被引 6
- **作者**: Ye Fang, Zeyi Sun, Tong Wu, Jiaqi Wang, Ziwei Liu, Gordon Wetzstein et al.
- **🏷️ 机构**: CUHK
- **会议**: NeurIPS 2024

### MAN TruckScenes: A multimodal dataset for autonomous trucking in diverse conditions.
- **链接**: [arXiv:2407.07462](https://arxiv.org/abs/2407.07462) · 📚 被引 19
- **作者**: Felix Fent, Fabian Kuttenreich, Florian Ruch, Farija Rizwin, Stefan Juergens, Lorenz Lechermann et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous trucking is a promising technology that can greatly impact modern logistics and the environment. Ensuring its safety on public roads is one of the main duties that requires an accurate perception of the environment. To achieve this, machine learning methods rely on large datasets, but to this day, no such datasets are available for autonomous trucks. In this work, we present MAN TruckScenes, the first multimodal dataset for autonomous trucking. MAN TruckScenes allows the research community to come into contact with truck-specific challenges, such as trailer occlusions, novel sensor perspectives, and terminal environments for the first time. It comprises more than 740 scenes of 20s each within a multitude of different environmental conditions. The sensor set includes 4 cameras, 6 lidar, 6 radar sensors, 2 IMUs, and a high-precision GNSS. The dataset's 3D bounding boxes were manually annotated and carefully reviewed to achieve a high quality standard. Bounding boxes are available for 27 object classes, 15 attributes, and a range of more than 230m. The scenes are tagged according to 34 distinct scene tags, and all objects are tracked throughout the scene to promote a wide range of applications. Additionally, MAN TruckScenes is the first dataset to provide 4D radar data with 360° coverage and is thereby the largest radar dataset with annotated 3D bounding boxes. Finally, we provide extensive dataset analysis and baseline results. The dataset, development kit, and more are available online.

</details>

### BIOSCAN-5M: A Multimodal Dataset for Insect Biodiversity.
- **链接**: [arXiv:2406.12723](https://arxiv.org/abs/2406.12723) · [代码](https://github.com/bioscan-ml/BIOSCAN-5M) · 📚 被引 3
- **作者**: Zahra Gharaee, Scott C. Lowe, ZeMing Gong, Pablo Millan Arias, Nicholas Pellegrino, Austin T. Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As part of an ongoing worldwide effort to comprehend and monitor insect biodiversity, this paper presents the BIOSCAN-5M Insect dataset to the machine learning community and establish several benchmark tasks. BIOSCAN-5M is a comprehensive dataset containing multi-modal information for over 5 million insect specimens, and it significantly expands existing image-based biological datasets by including taxonomic labels, raw nucleotide barcode sequences, assigned barcode index numbers, geographical, and size information. We propose three benchmark experiments to demonstrate the impact of the multi-modal data types on the classification and clustering accuracy. First, we pretrain a masked language model on the DNA barcode sequences of the BIOSCAN-5M dataset, and demonstrate the impact of using this large reference library on species- and genus-level classification performance. Second, we propose a zero-shot transfer learning task applied to images and DNA barcodes to cluster feature embeddings obtained from self-supervised learning, to investigate whether meaningful clusters can be derived from these representation embeddings. Third, we benchmark multi-modality by performing contrastive learning on DNA barcodes, image data, and taxonomic information. This yields a general shared embedding space enabling taxonomic classification using multiple types of information and modalities. The code repository of the BIOSCAN-5M Insect dataset is available at https://github.com/bioscan-ml/BIOSCAN-5M.

</details>

### MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models.
- **链接**: [arXiv:2406.07594](https://arxiv.org/abs/2406.07594) · 📚 被引 11
- **作者**: Tianle Gu, Zeyang Zhou, Kexin Huang, Dandan Liang, Yixu Wang, Haiquan Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Powered by remarkable advancements in Large Language Models (LLMs), Multimodal Large Language Models (MLLMs) demonstrate impressive capabilities in manifold tasks. However, the practical application scenarios of MLLMs are intricate, exposing them to potential malicious instructions and thereby posing safety risks. While current benchmarks do incorporate certain safety considerations, they often lack comprehensive coverage and fail to exhibit the necessary rigor and robustness. For instance, the common practice of employing GPT-4V as both the evaluator and a model to be evaluated lacks credibility, as it tends to exhibit a bias toward its own responses. In this paper, we present MLLMGuard, a multidimensional safety evaluation suite for MLLMs, including a bilingual image-text evaluation dataset, inference utilities, and a lightweight evaluator. MLLMGuard's assessment comprehensively covers two languages (English and Chinese) and five important safety dimensions (Privacy, Bias, Toxicity, Truthfulness, and Legality), each with corresponding rich subtasks. Focusing on these dimensions, our evaluation dataset is primarily sourced from platforms such as social media, and it integrates text-based and image-based red teaming techniques with meticulous annotation by human experts. This can prevent inaccurate evaluation caused by data leakage when using open-source datasets and ensures the quality and challenging nature of our benchmark. Additionally, a fully automated lightweight evaluator termed GuardRank is developed, which achieves significantly higher evaluation accuracy than GPT-4. Our evaluation results across 13 advanced models indicate that MLLMs still have a substantial journey ahead before they can be considered safe and responsible.

</details>

### Classifier-guided Gradient Modulation for Enhanced Multimodal Learning.
- **链接**: [arXiv:2411.01409](https://arxiv.org/abs/2411.01409) · [代码](https://github.com/zrguo/CGGM) · 📚 被引 5
- **作者**: Zirun Guo, Tao Jin, Jingyuan Chen, Zhou Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning has developed very fast in recent years. However, during the multimodal training process, the model tends to rely on only one modality based on which it could learn faster, thus leading to inadequate use of other modalities. Existing methods to balance the training process always have some limitations on the loss functions, optimizers and the number of modalities and only consider modulating the magnitude of the gradients while ignoring the directions of the gradients. To solve these problems, in this paper, we present a novel method to balance multimodal learning with Classifier-Guided Gradient Modulation (CGGM), considering both the magnitude and directions of the gradients. We conduct extensive experiments on four multimodal datasets: UPMC-Food 101, CMU-MOSI, IEMOCAP and BraTS 2021, covering classification, regression and segmentation tasks. The results show that CGGM outperforms all the baselines and other state-of-the-art methods consistently, demonstrating its effectiveness and versatility. Our code is available at https://github.com/zrguo/CGGM.

</details>

### HEALNet: Multimodal Fusion for Heterogeneous Biomedical Data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/765871e77d2ca65126d3d64d31aa6908-Abstract-Conference.html) · 📚 被引 40
- **作者**: Konstantin Hemker, Nikola Simidjievski, Mateja Jamnik
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models.
- **链接**: [arXiv:2406.09403](https://arxiv.org/abs/2406.09403) · 📚 被引 12
- **作者**: Yushi Hu, Weijia Shi, Xingyu Fu, Dan Roth, Mari Ostendorf, Luke Zettlemoyer et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans draw to facilitate reasoning: we draw auxiliary lines when solving geometry problems; we mark and circle when reasoning on maps; we use sketches to amplify our ideas and relieve our limited-capacity working memory. However, such actions are missing in current multimodal language models (LMs). Current chain-of-thought and tool-use paradigms only use text as intermediate reasoning steps. In this work, we introduce Sketchpad, a framework that gives multimodal LMs a visual sketchpad and tools to draw on the sketchpad. The LM conducts planning and reasoning according to the visual artifacts it has drawn. Different from prior work, which uses text-to-image models to enable LMs to draw, Sketchpad enables LMs to draw with lines, boxes, marks, etc., which is closer to human sketching and better facilitates reasoning. Sketchpad can also use specialist vision models during the sketching process (e.g., draw bounding boxes with object detection models, draw masks with segmentation models), to further enhance visual perception and reasoning. We experiment with a wide range of math tasks (including geometry, functions, graphs, and chess) and complex visual reasoning tasks. Sketchpad substantially improves performance on all tasks over strong base models with no sketching, yielding an average gain of 12.7% on math tasks, and 8.6% on vision tasks. GPT-4o with Sketchpad sets a new state of the art on all tasks, including V*Bench (80.3%), BLINK spatial reasoning (83.9%), and visual correspondence (80.8%). All codes and data are in https://visualsketchpad.github.io/.

</details>

### Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight.
- **链接**: [arXiv:2407.15819](https://arxiv.org/abs/2407.15819) · 📚 被引 1
- **作者**: Ziyuan Huang, Kaixiang Ji, Biao Gong, Zhiwu Qing, Qinglong Zhang, Kecheng Zheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces Chain-of-Sight, a vision-language bridge module that accelerates the pre-training of Multimodal Large Language Models (MLLMs). Our approach employs a sequence of visual resamplers that capture visual details at various spacial scales. This architecture not only leverages global and local visual contexts effectively, but also facilitates the flexible extension of visual tokens through a compound token scaling strategy, allowing up to a 16x increase in the token count post pre-training. Consequently, Chain-of-Sight requires significantly fewer visual tokens in the pre-training phase compared to the fine-tuning phase. This intentional reduction of visual tokens during pre-training notably accelerates the pre-training process, cutting down the wall-clock training time by ~73%. Empirical results on a series of vision-language benchmarks reveal that the pre-train acceleration through Chain-of-Sight is achieved without sacrificing performance, matching or surpassing the standard pipeline of utilizing all visual tokens throughout the entire training process. Further scaling up the number of visual tokens for pre-training leads to stronger performances, competitive to existing approaches in a series of benchmarks.

</details>

### MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/b8f21f324ff277ba26aed2e944b7576b-Abstract-Conference.html) · 📚 被引 1
- **作者**: Chaoya Jiang, Hongrui Jia, Haiyang Xu, Wei Ye, Mengfan Dong, Ming Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing.
- **链接**: [arXiv:2407.04180](https://arxiv.org/abs/2407.04180) · [代码](https://github.com/idealab-isu/Slice-100K) · 📚 被引 1
- **作者**: Anushrut Jignasu, Kelly O. Marshall, Ankush Kumar Mishra, Lucas Nerone Rillo, Baskar Ganapathysubramanian, Aditya Balu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> G-code (Geometric code) or RS-274 is the most widely used computer numerical control (CNC) and 3D printing programming language. G-code provides machine instructions for the movement of the 3D printer, especially for the nozzle, stage, and extrusion of material for extrusion-based additive manufacturing. Currently, there does not exist a large repository of curated CAD models along with their corresponding G-code files for additive manufacturing. To address this issue, we present Slice-100K, a first-of-its-kind dataset of over 100,000 G-code files, along with their tessellated CAD model, LVIS (Large Vocabulary Instance Segmentation) categories, geometric properties, and renderings. We build our dataset from triangulated meshes derived from Objaverse-XL and Thingi10K datasets. We demonstrate the utility of this dataset by finetuning GPT-2 on a subset of the dataset for G-code translation from a legacy G-code format (Sailfish) to a more modern, widely used format (Marlin). Our dataset can be found at https://github.com/idealab-isu/Slice-100K. Slice-100K will be the first step in developing a multimodal foundation model for digital manufacturing.

</details>

### InstructG2I: Synthesizing Images from Multimodal Attributed Graphs.
- **链接**: [arXiv:2410.07157](https://arxiv.org/abs/2410.07157) · [代码](https://github.com/PeterGriffinJin/InstructG2I) · 📚 被引 3
- **作者**: Bowen Jin, Ziqi Pang, Bingjun Guo, Yu-Xiong Wang, Jiaxuan You, Jiawei Han
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we approach an overlooked yet critical task Graph2Image: generating images from multimodal attributed graphs (MMAGs). This task poses significant challenges due to the explosion in graph size, dependencies among graph entities, and the need for controllability in graph conditions. To address these challenges, we propose a graph context-conditioned diffusion model called InstructG2I. InstructG2I first exploits the graph structure and multimodal information to conduct informative neighbor sampling by combining personalized page rank and re-ranking based on vision-language features. Then, a Graph-QFormer encoder adaptively encodes the graph nodes into an auxiliary set of graph prompts to guide the denoising process of diffusion. Finally, we propose graph classifier-free guidance, enabling controllable generation by varying the strength of graph guidance and multiple connected edges to a node. Extensive experiments conducted on three datasets from different domains demonstrate the effectiveness and controllability of our approach. The code is available at https://github.com/PeterGriffinJin/InstructG2I.

</details>

### Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8fa604a81e5a236e2f38e917109571a3-Abstract-Conference.html)
- **作者**: Yinuo Jing, Ruxu Zhang, Kongming Liang, Yongxiang Li, Zhongjiang He, Zhanyu Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Coupled Mamba: Enhanced Multimodal Fusion with Coupled State Space Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6e09c213ac18d6375704a4f3ea75c4f8-Abstract-Conference.html) · 📚 被引 35
- **作者**: Wenbing Li, Hang Zhou, Junqing Yu, Zikai Song, Wei Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Learning Multimodal Behaviors from Scratch with Diffusion Policy Gradient.
- **链接**: [arXiv:2406.00681](https://arxiv.org/abs/2406.00681) · 📚 被引 4
- **作者**: Steven Li, Rickmer Krohn, Tao Chen, Anurag Ajay, Pulkit Agrawal, Georgia Chalvatzaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep reinforcement learning (RL) algorithms typically parameterize the policy as a deep network that outputs either a deterministic action or a stochastic one modeled as a Gaussian distribution, hence restricting learning to a single behavioral mode. Meanwhile, diffusion models emerged as a powerful framework for multimodal learning. However, the use of diffusion policies in online RL is hindered by the intractability of policy likelihood approximation, as well as the greedy objective of RL methods that can easily skew the policy to a single mode. This paper presents Deep Diffusion Policy Gradient (DDiffPG), a novel actor-critic algorithm that learns from scratch multimodal policies parameterized as diffusion models while discovering and maintaining versatile behaviors. DDiffPG explores and discovers multiple modes through off-the-shelf unsupervised clustering combined with novelty-based intrinsic motivation. DDiffPG forms a multimodal training batch and utilizes mode-specific Q-learning to mitigate the inherent greediness of the RL objective, ensuring the improvement of the diffusion policy across all modes. Our approach further allows the policy to be conditioned on mode-specific embeddings to explicitly control the learned modes. Empirical studies validate DDiffPG's capability to master multimodal behaviors in complex, high-dimensional continuous control tasks with sparse rewards, also showcasing proof-of-concept dynamic online replanning when navigating mazes with unseen obstacles.

</details>

### Single Image Unlearning: Efficient Machine Unlearning in Multimodal Large Language Models.
- **链接**: [arXiv:2405.12523](https://arxiv.org/abs/2405.12523) · 📚 被引 8
- **作者**: Jiaqi Li, Qianshan Wei, Chuanyi Zhang, Guilin Qi, Miaozeng Du, Yongrui Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Machine unlearning empowers individuals with the `right to be forgotten' by removing their private or sensitive information encoded in machine learning models. However, it remains uncertain whether MU can be effectively applied to Multimodal Large Language Models (MLLMs), particularly in scenarios of forgetting the leaked visual data of concepts. To overcome the challenge, we propose an efficient method, Single Image Unlearning (SIU), to unlearn the visual recognition of a concept by fine-tuning a single associated image for few steps. SIU consists of two key aspects: (i) Constructing Multifaceted fine-tuning data. We introduce four targets, based on which we construct fine-tuning data for the concepts to be forgotten; (ii) Jointly training loss. To synchronously forget the visual recognition of concepts and preserve the utility of MLLMs, we fine-tune MLLMs through a novel Dual Masked KL-divergence Loss combined with Cross Entropy loss. Alongside our method, we establish MMUBench, a new benchmark for MU in MLLMs and introduce a collection of metrics for its evaluation. Experimental results on MMUBench show that SIU completely surpasses the performance of existing methods. Furthermore, we surprisingly find that SIU can avoid invasive membership inference attacks and jailbreak attacks. To the best of our knowledge, we are the first to explore MU in MLLMs. We will release the code and benchmark in the near future.

</details>

### Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks.
- **链接**: [arXiv:2408.03615](https://arxiv.org/abs/2408.03615) · 📚 被引 5
- **作者**: Zaijing Li, Yuquan Xie, Rui Shao, Gongwei Chen, Dongmei Jiang, Liqiang Nie
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Building a general-purpose agent is a long-standing vision in the field of artificial intelligence. Existing agents have made remarkable progress in many domains, yet they still struggle to complete long-horizon tasks in an open world. We attribute this to the lack of necessary world knowledge and multimodal experience that can guide agents through a variety of long-horizon tasks. In this paper, we propose a Hybrid Multimodal Memory module to address the above challenges. It 1) transforms knowledge into Hierarchical Directed Knowledge Graph that allows agents to explicitly represent and learn world knowledge, and 2) summarises historical information into Abstracted Multimodal Experience Pool that provide agents with rich references for in-context learning. On top of the Hybrid Multimodal Memory module, a multimodal agent, Optimus-1, is constructed with dedicated Knowledge-guided Planner and Experience-Driven Reflector, contributing to a better planning and reflection in the face of long-horizon tasks in Minecraft. Extensive experimental results show that Optimus-1 significantly outperforms all existing agents on challenging long-horizon task benchmarks, and exhibits near human-level performance on many tasks. In addition, we introduce various Multimodal Large Language Models (MLLMs) as the backbone of Optimus-1. Experimental results show that Optimus-1 exhibits strong generalization with the help of the Hybrid Multimodal Memory module, outperforming the GPT-4V baseline on many tasks.

</details>

### Toward Robust Incomplete Multimodal Sentiment Analysis via Hierarchical Representation Learning.
- **链接**: [arXiv:2411.02793](https://arxiv.org/abs/2411.02793) · 📚 被引 10
- **作者**: Mingcheng Li, Dingkang Yang, Yang Liu, Shunli Wang, Jiawei Chen, Shuaibing Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Sentiment Analysis (MSA) is an important research area that aims to understand and recognize human sentiment through multiple modalities. The complementary information provided by multimodal fusion promotes better sentiment analysis compared to utilizing only a single modality. Nevertheless, in real-world applications, many unavoidable factors may lead to situations of uncertain modality missing, thus hindering the effectiveness of multimodal modeling and degrading the model's performance. To this end, we propose a Hierarchical Representation Learning Framework (HRLF) for the MSA task under uncertain missing modalities. Specifically, we propose a fine-grained representation factorization module that sufficiently extracts valuable sentiment information by factorizing modality into sentiment-relevant and modality-specific representations through crossmodal translation and sentiment semantic reconstruction. Moreover, a hierarchical mutual information maximization mechanism is introduced to incrementally maximize the mutual information between multi-scale representations to align and reconstruct the high-level semantics in the representations. Ultimately, we propose a hierarchical adversarial learning mechanism that further aligns and adapts the latent distribution of sentiment-relevant representations to produce robust joint multimodal representations. Comprehensive experiments on three datasets demonstrate that HRLF significantly improves MSA performance under uncertain modality missing cases.

</details>

### DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception.
- **链接**: [arXiv:2407.08303](https://arxiv.org/abs/2407.08303) · [代码](https://github.com/baaivision/DenseFusion) · 📚 被引 3
- **作者**: Xiaotong Li, Fan Zhang, Haiwen Diao, Yueze Wang, Xinlong Wang, Lingyu Duan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing Multimodal Large Language Models (MLLMs) increasingly emphasize complex understanding of various visual elements, including multiple objects, text information, and spatial relations. Their development for comprehensive visual perception hinges on the availability of high-quality image-text datasets that offer diverse visual elements and throughout image descriptions. However, the scarcity of such hyper-detailed datasets currently hinders progress within the MLLM community. The bottleneck stems from the limited perceptual capabilities of current caption engines, which fall short in providing complete and accurate annotations. To facilitate the cutting-edge research of MLLMs on comprehensive vision perception, we thereby propose Perceptual Fusion, using a low-budget but highly effective caption engine for complete and accurate image descriptions. Specifically, Perceptual Fusion integrates diverse perception experts as image priors to provide explicit information on visual elements and adopts an efficient MLLM as a centric pivot to mimic advanced MLLMs' perception abilities. We carefully select 1M highly representative images from uncurated LAION dataset and generate dense descriptions using our engine, dubbed DenseFusion-1M. Extensive experiments validate that our engine outperforms its counterparts, where the resulting dataset significantly improves the perception and cognition abilities of existing MLLMs across diverse vision-language benchmarks, especially with high-resolution images as inputs. The dataset and code are publicly available at https://github.com/baaivision/DenseFusion.

</details>

### HEMM: Holistic Evaluation of Multimodal Foundation Models.
- **链接**: [arXiv:2407.03418](https://arxiv.org/abs/2407.03418) · 📚 被引 1
- **作者**: Paul Pu Liang, Akshay Goindani, Talha Chafekar, Leena Mathur, Haofei Yu, Ruslan Salakhutdinov et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal foundation models that can holistically process text alongside images, video, audio, and other sensory modalities are increasingly used in a variety of real-world applications. However, it is challenging to characterize and study progress in multimodal foundation models, given the range of possible modeling decisions, tasks, and domains. In this paper, we introduce Holistic Evaluation of Multimodal Models (HEMM) to systematically evaluate the capabilities of multimodal foundation models across a set of 3 dimensions: basic skills, information flow, and real-world use cases. Basic multimodal skills are internal abilities required to solve problems, such as learning interactions across modalities, fine-grained alignment, multi-step reasoning, and the ability to handle external knowledge. Information flow studies how multimodal content changes during a task through querying, translation, editing, and fusion. Use cases span domain-specific challenges introduced in real-world multimedia, affective computing, natural sciences, healthcare, and human-computer interaction applications. Through comprehensive experiments across the 30 tasks in HEMM, we (1) identify key dataset dimensions (e.g., basic skills, information flows, and use cases) that pose challenges to today's models, and (2) distill performance trends regarding how different modeling dimensions (e.g., scale, pre-training data, multimodal alignment, pre-training, and instruction tuning objectives) influence performance. Our conclusions regarding challenging multimodal interactions, use cases, and tasks requiring reasoning and external knowledge, the benefits of data and model scale, and the impacts of instruction tuning yield actionable insights for future work in multimodal foundation models.

</details>

### Time-MMD: Multi-Domain Multimodal Dataset for Time Series Analysis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8e7768122f3eeec6d77cd2b424b72413-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 15
- **作者**: Haoxin Liu, Shangqing Xu, Zhiyuan Zhao, Lingkai Kong, Harshavardhan Kamarthi, Aditya B. Sasanur et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Visual Anchors Are Strong Information Aggregators For Multimodal Large Language Model.
- **链接**: [arXiv:2405.17815](https://arxiv.org/abs/2405.17815) · [代码](https://github.com/liuhaogeng/Anchor-Former) · 📚 被引 0
- **作者**: Haogeng Liu, Quanzeng You, Xiaotian Han, Yongfei Liu, Huaibo Huang, Ran He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of Multimodal Large Language Models (MLLMs), vision-language connector plays a crucial role to link the pre-trained vision encoders with Large Language Models (LLMs). Despite its importance, the vision-language connector has been relatively less explored. In this study, we aim to propose a strong vision-language connector that enables MLLMs to achieve high accuracy while maintain low computation cost. We first reveal the existence of the visual anchors in Vision Transformer and propose a cost-effective search algorithm to extract them. Building on these findings, we introduce the Anchor Former (AcFormer), a novel vision-language connector designed to leverage the rich prior knowledge obtained from these visual anchors during pretraining, guiding the aggregation of information. Through extensive experimentation, we demonstrate that the proposed method significantly reduces computational costs by nearly two-thirds compared with baseline, while simultaneously outperforming baseline methods. This highlights the effectiveness and efficiency of AcFormer. Codes are available at https://github.com/liuhaogeng/Anchor-Former.

</details>

### M$3$GPT: An Advanced Multimodal, Multitask Framework for Motion Comprehension and Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/316648eb8b4ffb6010f531b07848c300-Abstract-Conference.html) · 📚 被引 3
- **作者**: Mingshuang Luo, Ruibing Hou, Zhuo Li, Hong Chang, Zimo Liu, Yaowei Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### GenRL: Multimodal-foundation world models for generalization in embodied agents.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/3076133f08b40607d00a8f48f6acd71c-Abstract-Conference.html) · 📚 被引 2
- **作者**: Pietro Mazzaglia, Tim Verbelen, Bart Dhoedt, Aaron C. Courville, Sai Rajeswar Mudumba
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Towards Unified Multimodal Editing with Enhanced Knowledge Collaboration.
- **链接**: [arXiv:2409.19872](https://arxiv.org/abs/2409.19872) · [代码](https://github.com/beepkh/UniKE) · 📚 被引 1
- **作者**: Kaihang Pan, Zhaoyu Fan, Juncheng Li, Qifan Yu, Hao Fei, Siliang Tang et al.
- **🏷️ 机构**: NUS
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The swift advancement in Multimodal LLMs (MLLMs) also presents significant challenges for effective knowledge editing. Current methods, including intrinsic knowledge editing and external knowledge resorting, each possess strengths and weaknesses, struggling to balance the desired properties of reliability, generality, and locality when applied to MLLMs. In this paper, we propose UniKE, a novel multimodal editing method that establishes a unified perspective and paradigm for intrinsic knowledge editing and external knowledge resorting. Both types of knowledge are conceptualized as vectorized key-value memories, with the corresponding editing processes resembling the assimilation and accommodation phases of human cognition, conducted at the same semantic levels. Within such a unified framework, we further promote knowledge collaboration by disentangling the knowledge representations into the semantic and truthfulness spaces. Extensive experiments validate the effectiveness of our method, which ensures that the post-edit MLLM simultaneously maintains excellent reliability, generality, and locality. The code for UniKE is available at \url{https://github.com/beepkh/UniKE}.

</details>

### A Concept-Based Explainability Framework for Large Multimodal Models.
- **链接**: [arXiv:2406.08074](https://arxiv.org/abs/2406.08074) · [代码](https://github.com/mshukor/xl-vlms) · 📚 被引 5
- **作者**: Jayneel Parekh, Pegah Khayatan, Mustafa Shukor, Alasdair Newson, Matthieu Cord
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multimodal models (LMMs) combine unimodal encoders and large language models (LLMs) to perform multimodal tasks. Despite recent advancements towards the interpretability of these models, understanding internal representations of LMMs remains largely a mystery. In this paper, we present a novel framework for the interpretation of LMMs. We propose a dictionary learning based approach, applied to the representation of tokens. The elements of the learned dictionary correspond to our proposed concepts. We show that these concepts are well semantically grounded in both vision and text. Thus we refer to these as ``multi-modal concepts''. We qualitatively and quantitatively evaluate the results of the learnt concepts. We show that the extracted multimodal concepts are useful to interpret representations of test samples. Finally, we evaluate the disentanglement between different concepts and the quality of grounding concepts visually and textually. Our code is publicly available at https://github.com/mshukor/xl-vlms

</details>

### SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers.
- **链接**: [arXiv:2407.09413](https://arxiv.org/abs/2407.09413) · 📚 被引 13
- **作者**: Shraman Pramanick, Rama Chellappa, Subhashini Venugopalan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Seeking answers to questions within long scientific research articles is a crucial area of study that aids readers in quickly addressing their inquiries. However, existing question-answering (QA) datasets based on scientific papers are limited in scale and focus solely on textual content. We introduce SPIQA (Scientific Paper Image Question Answering), the first large-scale QA dataset specifically designed to interpret complex figures and tables within the context of scientific research articles across various domains of computer science. Leveraging the breadth of expertise and ability of multimodal large language models (MLLMs) to understand figures, we employ automatic and manual curation to create the dataset. We craft an information-seeking task on interleaved images and text that involves multiple images covering plots, charts, tables, schematic diagrams, and result visualizations. SPIQA comprises 270K questions divided into training, validation, and three different evaluation splits. Through extensive experiments with 12 prominent foundational models, we evaluate the ability of current multimodal systems to comprehend the nuanced aspects of research articles. Additionally, we propose a Chain-of-Thought (CoT) evaluation strategy with in-context retrieval that allows fine-grained, step-by-step assessment and improves model performance. We further explore the upper bounds of performance enhancement with additional textual information, highlighting its promising potential for future research and the dataset's impact on revolutionizing how we interact with scientific literature.

</details>

### Robust Sleep Staging over Incomplete Multimodal Physiological Signals via Contrastive Imagination.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/cb0f9020c00fc52a9f6c9dbfacc6ac58-Abstract-Conference.html) · 📚 被引 6
- **作者**: Qi Shen, Junchang Xin, Bing Tian Dai, Shudi Zhang, Zhiqiong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### IMPACT: A Large-scale Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/e3301977b92f28e32639ec99eb08f4a1-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 1
- **作者**: Homaira Huda Shomee, Zhu Wang, Sathya N. Ravi, Sourav Medya
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### QUEST: Quadruple Multimodal Contrastive Learning with Constraints and Self-Penalization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/32cc61322f1e2f56f989d29ccc7cfbb7-Abstract-Conference.html) · 📚 被引 1
- **作者**: Qi Song, Tianxiang Gong, Shiqi Gao, Haoyi Zhou, Jianxin Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Unsupervised Homography Estimation on Multimodal Image Pair via Alternating Optimization.
- **链接**: [arXiv:2411.13036](https://arxiv.org/abs/2411.13036) · [代码](https://github.com/songsang7/AltO) · 📚 被引 1
- **作者**: Sanghyeob Song, Jaihyun Lew, Hyemi Jang, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Estimating the homography between two images is crucial for mid- or high-level vision tasks, such as image stitching and fusion. However, using supervised learning methods is often challenging or costly due to the difficulty of collecting ground-truth data. In response, unsupervised learning approaches have emerged. Most early methods, though, assume that the given image pairs are from the same camera or have minor lighting differences. Consequently, while these methods perform effectively under such conditions, they generally fail when input image pairs come from different domains, referred to as multimodal image pairs. To address these limitations, we propose AltO, an unsupervised learning framework for estimating homography in multimodal image pairs. Our method employs a two-phase alternating optimization framework, similar to Expectation-Maximization (EM), where one phase reduces the geometry gap and the other addresses the modality gap. To handle these gaps, we use Barlow Twins loss for the modality gap and propose an extended version, Geometry Barlow Twins, for the geometry gap. As a result, we demonstrate that our method, AltO, can be trained on multimodal datasets without any ground-truth data. It not only outperforms other unsupervised methods but is also compatible with various architectures of homography estimators. The source code can be found at:~\url{https://github.com/songsang7/AltO}

</details>

### cPAPERS: A Dataset of Situated and Multimodal Interactive Conversations in Scientific Papers.
- **链接**: [arXiv:2406.08398](https://arxiv.org/abs/2406.08398) · 📚 被引 1
- **作者**: Anirudh Sundar, Jin Xu, William Gay, Christopher Richardson, Larry Heck
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> An emerging area of research in situated and multimodal interactive conversations (SIMMC) includes interactions in scientific papers. Since scientific papers are primarily composed of text, equations, figures, and tables, SIMMC methods must be developed specifically for each component to support the depth of inquiry and interactions required by research scientists. This work introduces Conversational Papers (cPAPERS), a dataset of conversational question-answer pairs from reviews of academic papers grounded in these paper components and their associated references from scientific documents available on arXiv. We present a data collection strategy to collect these question-answer pairs from OpenReview and associate them with contextual information from LaTeX source files. Additionally, we present a series of baseline approaches utilizing Large Language Models (LLMs) in both zero-shot and fine-tuned configurations to address the cPAPERS dataset.

</details>

### Unity by Diversity: Improved Representation Learning for Multimodal VAEs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/87726969ce38e9a676ca1fd4459ba77d-Abstract-Conference.html) · 📚 被引 3
- **作者**: Thomas M. Sutter, Yang Meng, Andrea Agostini, Daphné Chopard, Norbert Fortin, Julia E. Vogt et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Grounding Multimodal Large Language Models in Actions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/2406694fd7bc7e7bf257446a14f9ea63-Abstract-Conference.html) · 📚 被引 2
- **作者**: Andrew Szot, Bogdan Mazoure, Harsh Agrawal, R. Devon Hjelm, Zsolt Kira, Alexander Toshev
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Identifiable Shared Component Analysis of Unpaired Multimodal Mixtures.
- **链接**: [arXiv:2409.19422](https://arxiv.org/abs/2409.19422) · 📚 被引 0
- **作者**: Subash Timilsina, Sagar Shrestha, Xiao Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A core task in multi-modal learning is to integrate information from multiple feature spaces (e.g., text and audio), offering modality-invariant essential representations of data. Recent research showed that, classical tools such as {\it canonical correlation analysis} (CCA) provably identify the shared components up to minor ambiguities, when samples in each modality are generated from a linear mixture of shared and private components. Such identifiability results were obtained under the condition that the cross-modality samples are aligned/paired according to their shared information. This work takes a step further, investigating shared component identifiability from multi-modal linear mixtures where cross-modality samples are unaligned. A distribution divergence minimization-based loss is proposed, under which a suite of sufficient conditions ensuring identifiability of the shared components are derived. Our conditions are based on cross-modality distribution discrepancy characterization and density-preserving transform removal, which are much milder than existing studies relying on independent component analysis. More relaxed conditions are also provided via adding reasonable structural constraints, motivated by available side information in various applications. The identifiability claims are thoroughly validated using synthetic and real-world data.

</details>

### No "Zero-Shot" Without Exponential Data: Pretraining Concept Frequency Determines Multimodal Model Performance.
- **链接**: [arXiv:2404.04125](https://arxiv.org/abs/2404.04125) · 📚 被引 4
- **作者**: Vishaal Udandarao, Ameya Prabhu, Adhiraj Ghosh, Yash Sharma, Philip Torr, Adel Bibi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Web-crawled pretraining datasets underlie the impressive "zero-shot" evaluation performance of multimodal models, such as CLIP for classification/retrieval and Stable-Diffusion for image generation. However, it is unclear how meaningful the notion of "zero-shot" generalization is for such multimodal models, as it is not known to what extent their pretraining datasets encompass the downstream concepts targeted for during "zero-shot" evaluation. In this work, we ask: How is the performance of multimodal models on downstream concepts influenced by the frequency of these concepts in their pretraining datasets? We comprehensively investigate this question across 34 models and five standard pretraining datasets (CC-3M, CC-12M, YFCC-15M, LAION-400M, LAION-Aesthetics), generating over 300GB of data artifacts. We consistently find that, far from exhibiting "zero-shot" generalization, multimodal models require exponentially more data to achieve linear improvements in downstream "zero-shot" performance, following a sample inefficient log-linear scaling trend. This trend persists even when controlling for sample-level similarity between pretraining and downstream datasets, and testing on purely synthetic data distributions. Furthermore, upon benchmarking models on long-tailed data sampled based on our analysis, we demonstrate that multimodal models across the board perform poorly. We contribute this long-tail test set as the "Let it Wag!" benchmark to further research in this direction. Taken together, our study reveals an exponential need for training data which implies that the key to "zero-shot" generalization capabilities under large-scale training paradigms remains to be found.

</details>

### A Practitioner's Guide to Real-World Continual Multimodal Pretraining.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/f1a6a2cdc7e65dbb4579e78f97cd2665-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 2
- **作者**: Vishaal Udandarao, Karsten Roth, Sebastian Dziadzio, Ameya Prabhu, Mehdi Cherti, Oriol Vinyals et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### MmCows: A Multimodal Dataset for Dairy Cattle Monitoring.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6d8f3f71b22f9d2e9320d7bdb73acea7-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 13
- **作者**: Hien Vu, Omkar Prabhune, Unmesh Raskar, Dimuth Panditharatne, Hanwook Chung, Christopher Y. Choi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### CLIPLoss and Norm-Based Data Selection Methods for Multimodal Contrastive Learning.
- **链接**: [arXiv:2405.19547](https://arxiv.org/abs/2405.19547) · 📚 被引 5
- **作者**: Yiping Wang, Yifang Chen, Wendan Yan, Alex Fang, Wenjing Zhou, Kevin Jamieson et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Data selection has emerged as a core issue for large-scale visual-language model pretaining (e.g., CLIP), particularly with noisy web-curated datasets. Three main data selection approaches are: (1) leveraging external non-CLIP models to aid data selection, (2) training new CLIP-style embedding models that are more effective at selecting high-quality data than the original OpenAI CLIP model, and (3) designing better metrics or strategies universally applicable to any CLIP embedding without requiring specific model properties (e.g., CLIPScore is one popular metric). While the first two approaches have been extensively studied, the third remains under-explored. In this paper, we advance the third approach by proposing two new methods. Firstly, instead of classical CLIP scores that only consider the alignment between two modalities from a single sample, we introduce surrogate-CLIPLoss (s-CLIPLoss), a CLIP loss-inspired method that adds the alignment between one sample and its contrastive pairs as an extra normalization term for better quality measurement. Secondly, when downstream tasks are known, we propose a new norm-based metric, NormSim, to measure the similarity between pretraining data and target data. We test our methods on the data selection benchmark, DataComp~\cite{gadre2023datacomp}. Compared to the best baseline using only OpenAI's CLIP-L/14, our methods achieve a 5.3\% improvement on ImageNet-1k and a 2.8\% improvement on 38 downstream evaluation tasks. Moreover, both s-CLIPLoss and NormSim are compatible with existing techniques. By combining our methods with the current best methods DFN and HYPE, we can boost average performance on downstream tasks by 0.9\%, achieving a new state-of-the-art on the DataComp-medium benchmark.

</details>

### GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing.
- **链接**: [arXiv:2407.05600](https://arxiv.org/abs/2407.05600) · 📚 被引 7
- **作者**: Zhenyu Wang, Aoxue Li, Zhenguo Li, Xihui Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the success achieved by existing image generation and editing methods, current models still struggle with complex problems including intricate text prompts, and the absence of verification and self-correction mechanisms makes the generated images unreliable. Meanwhile, a single model tends to specialize in particular tasks and possess the corresponding capabilities, making it inadequate for fulfilling all user requirements. We propose GenArtist, a unified image generation and editing system, coordinated by a multimodal large language model (MLLM) agent. We integrate a comprehensive range of existing models into the tool library and utilize the agent for tool selection and execution. For a complex problem, the MLLM agent decomposes it into simpler sub-problems and constructs a tree structure to systematically plan the procedure of generation, editing, and self-correction with step-by-step verification. By automatically generating missing position-related inputs and incorporating position information, the appropriate tool can be effectively employed to address each sub-problem. Experiments demonstrate that GenArtist can perform various generation and editing tasks, achieving state-of-the-art performance and surpassing existing models such as SDXL and DALL-E 3, as can be seen in Fig. 1. Project page is https://zhenyuw16.github.io/GenArtist_page.

</details>

### Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset.
- **链接**: [arXiv:2402.14804](https://arxiv.org/abs/2402.14804) · 📚 被引 14
- **作者**: Ke Wang, Junting Pan, Weikang Shi, Zimu Lu, Houxing Ren, Aojun Zhou et al.
- **🏷️ 机构**: CUHK
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in Large Multimodal Models (LMMs) have shown promising results in mathematical reasoning within visual contexts, with models approaching human-level performance on existing benchmarks such as MathVista. However, we observe significant limitations in the diversity of questions and breadth of subjects covered by these benchmarks. To address this issue, we present the MATH-Vision (MATH-V) dataset, a meticulously curated collection of 3,040 high-quality mathematical problems with visual contexts sourced from real math competitions. Spanning 16 distinct mathematical disciplines and graded across 5 levels of difficulty, our dataset provides a comprehensive and diverse set of challenges for evaluating the mathematical reasoning abilities of LMMs. Through extensive experimentation, we unveil a notable performance gap between current LMMs and human performance on MATH-V, underscoring the imperative for further advancements in LMMs. Moreover, our detailed categorization allows for a thorough error analysis of LMMs, offering valuable insights to guide future research and development. The project is available at https://mathvision-cuhk.github.io

</details>

### CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs.
- **链接**: [arXiv:2406.18521](https://arxiv.org/abs/2406.18521) · 📚 被引 10
- **作者**: Zirui Wang, Mengzhou Xia, Luxi He, Howard Chen, Yitao Liu, Richard Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Chart understanding plays a pivotal role when applying Multimodal Large Language Models (MLLMs) to real-world tasks such as analyzing scientific papers or financial reports. However, existing datasets often focus on oversimplified and homogeneous charts with template-based questions, leading to an over-optimistic measure of progress. We demonstrate that although open-source models can appear to outperform strong proprietary models on these benchmarks, a simple stress test with slightly different charts or questions can deteriorate performance by up to 34.5%. In this work, we propose CharXiv, a comprehensive evaluation suite involving 2,323 natural, challenging, and diverse charts from arXiv papers. CharXiv includes two types of questions: 1) descriptive questions about examining basic chart elements and 2) reasoning questions that require synthesizing information across complex visual elements in the chart. To ensure quality, all charts and questions are handpicked, curated, and verified by human experts. Our results reveal a substantial, previously underestimated gap between the reasoning skills of the strongest proprietary model (i.e., GPT-4o), which achieves 47.1% accuracy, and the strongest open-source model (i.e., InternVL Chat V1.5), which achieves 29.2%. All models lag far behind human performance of 80.5%, underscoring weaknesses in the chart understanding capabilities of existing MLLMs. We hope CharXiv facilitates future research on MLLM chart understanding by providing a more realistic and faithful measure of progress. Project page and leaderboard: https://charxiv.github.io/

</details>

### Needle In A Multimodal Haystack.
- **链接**: [arXiv:2406.07230](https://arxiv.org/abs/2406.07230) · [代码](https://github.com/OpenGVLab/MM-NIAH)
- **作者**: Weiyun Wang, Shuibo Zhang, Yiming Ren, Yuchen Duan, Tiantong Li, Shuo Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rapid advancement of multimodal large language models (MLLMs), their evaluation has become increasingly comprehensive. However, understanding long multimodal content, as a foundational ability for real-world applications, remains underexplored. In this work, we present Needle In A Multimodal Haystack (MM-NIAH), the first benchmark specifically designed to systematically evaluate the capability of existing MLLMs to comprehend long multimodal documents. Our benchmark includes three types of evaluation tasks: multimodal retrieval, counting, and reasoning. In each task, the model is required to answer the questions according to different key information scattered throughout the given multimodal document. Evaluating the leading MLLMs on MM-NIAH, we observe that existing models still have significant room for improvement on these tasks, especially on vision-centric evaluation. We hope this work can provide a platform for further research on long multimodal document comprehension and contribute to the advancement of MLLMs. Code and benchmark are released at https://github.com/OpenGVLab/MM-NIAH.

</details>

### ControlMLLM: Training-Free Visual Prompt Learning for Multimodal Large Language Models.
- **链接**: [arXiv:2407.21534](https://arxiv.org/abs/2407.21534) · 📚 被引 6
- **作者**: Mingrui Wu, Xinyue Cai, Jiayi Ji, Jiale Li, Oucheng Huang, Gen Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we propose a training-free method to inject visual prompts into Multimodal Large Language Models (MLLMs) through test-time optimization of a learnable latent variable. We observe that attention, as the core module of MLLMs, connects text prompt tokens and visual tokens, ultimately determining the final results. Our approach involves adjusting visual tokens from the MLP output at test time, controlling the attention response to ensure text prompt tokens attend to visual tokens in referring regions. We optimize a learnable latent variable based on an energy function, enhancing the strength of referring regions in the attention map. This enables detailed region description and reasoning without the need for substantial training costs or model retraining. Our method offers a promising direction for integrating referring abilities into MLLMs, and supports referring with box, mask, scribble and point. The results demonstrate that our method exhibits out-of-domain generalization and interpretability.

</details>

### Multimodal Large Language Models Make Text-to-Image Generative Models Align Better.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/9421261e06f1a63a352b068f1ac90609-Abstract-Conference.html) · 📚 被引 8
- **作者**: Xun Wu, Shaohan Huang, Guolong Wang, Jing Xiong, Furu Wei
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Propensity Score Alignment of Unpaired Multimodal Data.
- **链接**: [arXiv:2404.01595](https://arxiv.org/abs/2404.01595) · 📚 被引 1
- **作者**: Johnny Xi, Jana Osea, Zuheng Xu, Jason S. Hartford
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal representation learning techniques typically rely on paired samples to learn common representations, but paired samples are challenging to collect in fields such as biology where measurement devices often destroy the samples. This paper presents an approach to address the challenge of aligning unpaired samples across disparate modalities in multimodal representation learning. We draw an analogy between potential outcomes in causal inference and potential views in multimodal observations, which allows us to use Rubin's framework to estimate a common space in which to match samples. Our approach assumes we collect samples that are experimentally perturbed by treatments, and uses this to estimate a propensity score from each modality, which encapsulates all shared information between a latent state and treatment and can be used to define a distance between samples. We experiment with two alignment techniques that leverage this distance -- shared nearest neighbours (SNN) and optimal transport (OT) matching -- and find that OT matching results in significant improvements over state-of-the-art alignment approaches in both a synthetic multi-modal setting and in real-world data from NeurIPS Multimodal Single-Cell Integration Challenge.

</details>

### Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models.
- **链接**: [arXiv:2407.18999](https://arxiv.org/abs/2407.18999) · 📚 被引 4
- **作者**: Baao Xie, Qiuyu Chen, Yunnan Wang, Zequn Zhang, Xin Jin, Wenjun Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Disentangled representation learning (DRL) aims to identify and decompose underlying factors behind observations, thus facilitating data perception and generation. However, current DRL approaches often rely on the unrealistic assumption that semantic factors are statistically independent. In reality, these factors may exhibit correlations, which off-the-shelf solutions have yet to properly address. To tackle this challenge, we introduce a bidirectional weighted graph-based framework, to learn factorized attributes and their interrelations within complex data. Specifically, we propose a $β$-VAE based module to extract factors as the initial nodes of the graph, and leverage the multimodal large language model (MLLM) to discover and rank latent correlations, thereby updating the weighted edges. By integrating these complementary modules, our model successfully achieves fine-grained, practical and unsupervised disentanglement. Experiments demonstrate our method's superior performance in disentanglement and reconstruction. Furthermore, the model inherits enhanced interpretability and generalizability from MLLMs.

</details>

### OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments.
- **链接**: [arXiv:2404.07972](https://arxiv.org/abs/2404.07972) · 📚 被引 38
- **作者**: Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous agents that accomplish complex computer tasks with minimal human interventions have the potential to transform human-computer interaction, significantly enhancing accessibility and productivity. However, existing benchmarks either lack an interactive environment or are limited to environments specific to certain applications or domains, failing to reflect the diverse and complex nature of real-world computer use, thereby limiting the scope of tasks and agent scalability. To address this issue, we introduce OSWorld, the first-of-its-kind scalable, real computer environment for multimodal agents, supporting task setup, execution-based evaluation, and interactive learning across various operating systems such as Ubuntu, Windows, and macOS. OSWorld can serve as a unified, integrated computer environment for assessing open-ended computer tasks that involve arbitrary applications. Building upon OSWorld, we create a benchmark of 369 computer tasks involving real web and desktop apps in open domains, OS file I/O, and workflows spanning multiple applications. Each task example is derived from real-world computer use cases and includes a detailed initial state setup configuration and a custom execution-based evaluation script for reliable, reproducible evaluation. Extensive evaluation of state-of-the-art LLM/VLM-based agents on OSWorld reveals significant deficiencies in their ability to serve as computer assistants. While humans can accomplish over 72.36% of the tasks, the best model achieves only 12.24% success, primarily struggling with GUI grounding and operational knowledge. Comprehensive analysis using OSWorld provides valuable insights for developing multimodal generalist agents that were not possible with previous benchmarks. Our code, environment, baseline models, and data are publicly available at https://os-world.github.io.

</details>

### WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/9dd4533e7e4e5ed809344280609c5b05-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Junlin Xie, Ruifei Zhang, Zhihong Chen, Xiang Wan, Guanbin Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Addressing Asynchronicity in Clinical Multimodal Fusion via Individualized Chest X-ray Generation.
- **链接**: [arXiv:2410.17918](https://arxiv.org/abs/2410.17918) · 📚 被引 1
- **作者**: Wenfang Yao, Chen Liu, Kejing Yin, William Kwok-Wai Cheung, Jing Qin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Integrating multi-modal clinical data, such as electronic health records (EHR) and chest X-ray images (CXR), is particularly beneficial for clinical prediction tasks. However, in a temporal setting, multi-modal data are often inherently asynchronous. EHR can be continuously collected but CXR is generally taken with a much longer interval due to its high cost and radiation dose. When clinical prediction is needed, the last available CXR image might have been outdated, leading to suboptimal predictions. To address this challenge, we propose DDL-CXR, a method that dynamically generates an up-to-date latent representation of the individualized CXR images. Our approach leverages latent diffusion models for patient-specific generation strategically conditioned on a previous CXR image and EHR time series, providing information regarding anatomical structures and disease progressions, respectively. In this way, the interaction across modalities could be better captured by the latent CXR generation process, ultimately improving the prediction performance. Experiments using MIMIC datasets show that the proposed model could effectively address asynchronicity in multimodal fusion and consistently outperform existing methods.

</details>

### T2Vs Meet VLMs: A Scalable Multimodal Dataset for Visual Harmfulness Recognition.
- **链接**: [arXiv:2409.19734](https://arxiv.org/abs/2409.19734) · [代码](https://github.com/nctu-eva-lab/VHD11K) · 📚 被引 1
- **作者**: Chen Yeh, You-Ming Chang, Wei-Chen Chiu, Ning Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To address the risks of encountering inappropriate or harmful content, researchers managed to incorporate several harmful contents datasets with machine learning methods to detect harmful concepts. However, existing harmful datasets are curated by the presence of a narrow range of harmful objects, and only cover real harmful content sources. This hinders the generalizability of methods based on such datasets, potentially leading to misjudgments. Therefore, we propose a comprehensive harmful dataset, Visual Harmful Dataset 11K (VHD11K), consisting of 10,000 images and 1,000 videos, crawled from the Internet and generated by 4 generative models, across a total of 10 harmful categories covering a full spectrum of harmful concepts with nontrivial definition. We also propose a novel annotation framework by formulating the annotation process as a multi-agent Visual Question Answering (VQA) task, having 3 different VLMs "debate" about whether the given image/video is harmful, and incorporating the in-context learning strategy in the debating process. Therefore, we can ensure that the VLMs consider the context of the given image/video and both sides of the arguments thoroughly before making decisions, further reducing the likelihood of misjudgments in edge cases. Evaluation and experimental results demonstrate that (1) the great alignment between the annotation from our novel annotation framework and those from human, ensuring the reliability of VHD11K; (2) our full-spectrum harmful dataset successfully identifies the inability of existing harmful content detection methods to detect extensive harmful contents and improves the performance of existing harmfulness recognition methods; (3) VHD11K outperforms the baseline dataset, SMID, as evidenced by the superior improvement in harmfulness recognition methods. The complete dataset and code can be found at https://github.com/nctu-eva-lab/VHD11K.

</details>

### DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution.
- **链接**: [arXiv:2411.02359](https://arxiv.org/abs/2411.02359) · [代码](https://github.com/yueyang130/DeeR-VLA) · 📚 被引 8
- **作者**: Yang Yue, Yulin Wang, Bingyi Kang, Yizeng Han, Shenzhi Wang, Shiji Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

</details>

### Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs.
- **链接**: [arXiv:2406.20098](https://arxiv.org/abs/2406.20098) · [代码](https://github.com/MBZUAI-LLM/web2code) · 📚 被引 8
- **作者**: Sukmin Yun, Haokun Lin, Rusiru Thushara, Mohammad Qazim Bhat, Yongxin Wang, Zutao Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have shown impressive success across modalities such as image, video, and audio in a variety of understanding and generation tasks. However, current MLLMs are surprisingly poor at understanding webpage screenshots and generating their corresponding HTML code. To address this problem, we propose $\texttt{Web2Code}$, a benchmark consisting of a new large-scale webpage-to-code dataset for instruction tuning and an evaluation framework for the webpage understanding and HTML code translation abilities of MLLMs. For dataset construction, we leverage pretrained LLMs to enhance existing webpage-to-code datasets as well as generate a diverse pool of new webpages rendered into images. Specifically, the inputs are webpage images and instructions, while the responses are the webpage's HTML code. We further include diverse natural language QA pairs about the webpage content in the responses to enable a more comprehensive understanding of the web content. To evaluate model performance in these tasks, we develop an evaluation framework for testing MLLMs' abilities in webpage understanding and web-to-code generation. Extensive experiments show that our proposed dataset is beneficial not only to our proposed tasks but also in the general visual domain. We hope our work will contribute to the development of general MLLMs suitable for web-based content generation and task automation. Our data and code are available at https://github.com/MBZUAI-LLM/web2code.

</details>

### E2E-MFD: Towards End-to-End Synchronous Multimodal Fusion Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/5ddfb189c022a317ff1c72e6639079de-Abstract-Conference.html) · 📚 被引 26
- **作者**: Jiaqing Zhang, Mingxiang Cao, Weiying Xie, Jie Lei, Daixun Li, Wenbo Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Wings: Learning Multimodal LLMs without Text-only Forgetting.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/3852f6d247ba7deb46e4e4be9e702601-Abstract-Conference.html) · 📚 被引 1
- **作者**: Yi-Kai Zhang, Shiyin Lu, Yang Li, Yanqing Ma, Qingguo Chen, Zhao Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Towards Robust Multimodal Sentiment Analysis with Incomplete Data.
- **链接**: [arXiv:2409.20012](https://arxiv.org/abs/2409.20012) · 📚 被引 25
- **作者**: Haoyu Zhang, Wenbin Wang, Tianshu Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The field of Multimodal Sentiment Analysis (MSA) has recently witnessed an emerging direction seeking to tackle the issue of data incompleteness. Recognizing that the language modality typically contains dense sentiment information, we consider it as the dominant modality and present an innovative Language-dominated Noise-resistant Learning Network (LNLN) to achieve robust MSA. The proposed LNLN features a dominant modality correction (DMC) module and dominant modality based multimodal learning (DMML) module, which enhances the model's robustness across various noise scenarios by ensuring the quality of dominant modality representations. Aside from the methodical design, we perform comprehensive experiments under random data missing scenarios, utilizing diverse and meaningful settings on several popular datasets (\textit{e.g.,} MOSI, MOSEI, and SIMS), providing additional uniformity, transparency, and fairness compared to existing evaluations in the literature. Empirically, LNLN consistently outperforms existing baselines, demonstrating superior performance across these challenging and extensive evaluation metrics.

</details>

### Adaptive Image Quality Assessment via Teaching Large Multimodal Model to Compare.
- **链接**: [arXiv:2405.19298](https://arxiv.org/abs/2405.19298) · 📚 被引 9
- **作者**: Hanwei Zhu, Haoning Wu, Yixuan Li, Zicheng Zhang, Baoliang Chen, Lingyu Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While recent advancements in large multimodal models (LMMs) have significantly improved their abilities in image quality assessment (IQA) relying on absolute quality rating, how to transfer reliable relative quality comparison outputs to continuous perceptual quality scores remains largely unexplored. To address this gap, we introduce Compare2Score-an all-around LMM-based no-reference IQA (NR-IQA) model, which is capable of producing qualitatively comparative responses and effectively translating these discrete comparative levels into a continuous quality score. Specifically, during training, we present to generate scaled-up comparative instructions by comparing images from the same IQA dataset, allowing for more flexible integration of diverse IQA datasets. Utilizing the established large-scale training corpus, we develop a human-like visual quality comparator. During inference, moving beyond binary choices, we propose a soft comparison method that calculates the likelihood of the test image being preferred over multiple predefined anchor images. The quality score is further optimized by maximum a posteriori estimation with the resulting probability matrix. Extensive experiments on nine IQA datasets validate that the Compare2Score effectively bridges text-defined comparative levels during training with converted single image quality score for inference, surpassing state-of-the-art IQA models across diverse scenarios. Moreover, we verify that the probability-matrix-based inference conversion not only improves the rating accuracy of Compare2Score but also zero-shot general-purpose LMMs, suggesting its intrinsic effectiveness.

</details>

### MoVA: Adapting Mixture of Vision Experts to Multimodal Context.
- **链接**: [arXiv:2404.13046](https://arxiv.org/abs/2404.13046) · 📚 被引 10
- **作者**: Zhuofan Zong, Bingqi Ma, Dazhong Shen, Guanglu Song, Hao Shao, Dongzhi Jiang et al.
- **🏷️ 机构**: CUHK, SenseTime
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As the key component in multimodal large language models (MLLMs), the ability of the visual encoder greatly affects MLLM's understanding on diverse image content. Although some large-scale pretrained vision encoders such as vision encoders in CLIP and DINOv2 have brought promising performance, we found that there is still no single vision encoder that can dominate various image content understanding, e.g., the CLIP vision encoder leads to outstanding results on general image understanding but poor performance on document or chart content. To alleviate the bias of CLIP vision encoder, we first delve into the inherent behavior of different pre-trained vision encoders and then propose the MoVA, a powerful and novel MLLM, adaptively routing and fusing task-specific vision experts with a coarse-to-fine mechanism. In the coarse-grained stage, we design a context-aware expert routing strategy to dynamically select the most suitable vision experts according to the user instruction, input image, and expertise of vision experts. This benefits from the powerful model function understanding ability of the large language model (LLM). In the fine-grained stage, we elaborately conduct the mixture-of-vision-expert adapter (MoV-Adapter) to extract and fuse task-specific knowledge from various experts. This coarse-to-fine paradigm effectively leverages representations from experts based on multimodal context and model expertise, further enhancing the generalization ability. We conduct extensive experiments to evaluate the effectiveness of the proposed approach. Without any bells and whistles, MoVA can achieve significant performance gains over current state-of-the-art methods in a wide range of challenging multimodal benchmarks.

</details>

### On the Comparison between Multi-modal and Single-modal Contrastive Learning.
- **链接**: [arXiv:2411.02837](https://arxiv.org/abs/2411.02837) · 📚 被引 5
- **作者**: Wei Huang, Andi Han, Yongqiang Chen, Yuan Cao, Zhiqiang Xu, Taiji Suzuki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal contrastive learning with language supervision has presented a paradigm shift in modern machine learning. By pre-training on a web-scale dataset, multi-modal contrastive learning can learn high-quality representations that exhibit impressive robustness and transferability. Despite its empirical success, the theoretical understanding is still in its infancy, especially regarding its comparison with single-modal contrastive learning. In this work, we introduce a feature learning theory framework that provides a theoretical foundation for understanding the differences between multi-modal and single-modal contrastive learning. Based on a data generation model consisting of signal and noise, our analysis is performed on a ReLU network trained with the InfoMax objective function. Through a trajectory-based optimization analysis and generalization characterization on downstream tasks, we identify the critical factor, which is the signal-to-noise ratio (SNR), that impacts the generalizability in downstream tasks of both multi-modal and single-modal contrastive learning. Through the cooperation between the two modalities, multi-modal learning can achieve better feature learning, leading to improvements in performance in downstream tasks compared to single-modal learning. Our analysis provides a unified framework that can characterize the optimization and generalization of both single-modal and multi-modal contrastive learning. Empirical experiments on both synthetic and real-world datasets further consolidate our theoretical findings.

</details>

### VeXKD: The Versatile Integration of Cross-Modal Fusion and Knowledge Distillation for 3D Perception.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/e34d908241aef40440e61d2a27715424-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yuzhe Ji, Yijie Chen, Liuqing Yang, Rui Ding, Meng Yang, Xinhu Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- MM-WLAuslan: Multi-View Multi-Modal Word-Level Australian Sign Language Recognition Dataset. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
