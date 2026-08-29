# Multimodal — 2023 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 48 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A Multi-modal Global Instance Tracking Benchmark (MGIT): Better Locating Target in Complex Spatio-temporal and Causal Relationship.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/4ea14e6090343523ddcd5d3ca449695f-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 3
- **作者**: Shiyu Hu, Dailing Zhang, Meiqi Wu, Xiaokun Feng, Xuchen Li, Xin Zhao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Multimodal Clinical Benchmark for Emergency Care (MC-BEC): A Comprehensive Benchmark for Evaluating Foundation Models in Emergency Medicine.
- **链接**: [arXiv:2311.04937](https://arxiv.org/abs/2311.04937) · 📚 被引 3
- **作者**: Emma Chen, Aman Kansal, Julie Chen, Boyang Tom Jin, Julia Rachel Reisler, David A. Kim et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose the Multimodal Clinical Benchmark for Emergency Care (MC-BEC), a comprehensive benchmark for evaluating foundation models in Emergency Medicine using a dataset of 100K+ continuously monitored Emergency Department visits from 2020-2022. MC-BEC focuses on clinically relevant prediction tasks at timescales from minutes to days, including predicting patient decompensation, disposition, and emergency department (ED) revisit, and includes a standardized evaluation framework with train-test splits and evaluation metrics. The multimodal dataset includes a wide range of detailed clinical data, including triage information, prior diagnoses and medications, continuously measured vital signs, electrocardiogram and photoplethysmograph waveforms, orders placed and medications administered throughout the visit, free-text reports of imaging studies, and information on ED diagnosis, disposition, and subsequent revisits. We provide performance baselines for each prediction task to enable the evaluation of multimodal, multitask models. We believe that MC-BEC will encourage researchers to develop more effective, generalizable, and accessible foundation models for multimodal clinical data.

</details>

### Perception Test: A Diagnostic Benchmark for Multimodal Video Models.
- **链接**: [arXiv:2305.13786](https://arxiv.org/abs/2305.13786) · [代码](https://github.com/deepmind/perception_test) · 📚 被引 15
- **作者**: Viorica Patraucean, Lucas Smaira, Ankush Gupta, Adrià Recasens, Larisa Markeeva, Dylan Banarse et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a novel multimodal video benchmark - the Perception Test - to evaluate the perception and reasoning skills of pre-trained multimodal models (e.g. Flamingo, SeViLA, or GPT-4). Compared to existing benchmarks that focus on computational tasks (e.g. classification, detection or tracking), the Perception Test focuses on skills (Memory, Abstraction, Physics, Semantics) and types of reasoning (descriptive, explanatory, predictive, counterfactual) across video, audio, and text modalities, to provide a comprehensive and efficient evaluation tool. The benchmark probes pre-trained models for their transfer capabilities, in a zero-shot / few-shot or limited finetuning regime. For these purposes, the Perception Test introduces 11.6k real-world videos, 23s average length, designed to show perceptually interesting situations, filmed by around 100 participants worldwide. The videos are densely annotated with six types of labels (multiple-choice and grounded video question-answers, object and point tracks, temporal action and sound segments), enabling both language and non-language evaluations. The fine-tuning and validation splits of the benchmark are publicly available (CC-BY license), in addition to a challenge server with a held-out test split. Human baseline results compared to state-of-the-art video QA models show a substantial gap in performance (91.4% vs 46.2%), suggesting that there is significant room for improvement in multimodal video understanding. Dataset, baseline code, and challenge server are available at https://github.com/deepmind/perception_test

</details>

### M3Exam: A Multilingual, Multimodal, Multilevel Benchmark for Examining Large Language Models.
- **链接**: [arXiv:2306.05179](https://arxiv.org/abs/2306.05179) · 📚 被引 6
- **作者**: Wenxuan Zhang, Mahani Aljunied, Chang Gao, Yew Ken Chia, Lidong Bing
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### YouTubePD: A Multimodal Benchmark for Parkinson's Disease Analysis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/acffd5024f52c3a9ecc8ccb4b75b4e5c-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 3
- **作者**: Andy Zhou, Samuel Li, Pranav Sriram, Xiang Li, Jiahua Dong, Ansh Sharma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Multi-modal Queried Object Detection in the Wild.
- **链接**: [arXiv:2305.18980](https://arxiv.org/abs/2305.18980) · [代码](https://github.com/YifanXu74/MQ-Det) · 📚 被引 1
- **作者**: Yifan Xu, Mengdan Zhang, Chaoyou Fu, Peixian Chen, Xiaoshan Yang, Ke Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MQ-Det, an efficient architecture and pre-training strategy design to utilize both textual description with open-set generalization and visual exemplars with rich description granularity as category queries, namely, Multi-modal Queried object Detection, for real-world detection with both open-vocabulary categories and various granularity. MQ-Det incorporates vision queries into existing well-established language-queried-only detectors. A plug-and-play gated class-scalable perceiver module upon the frozen detector is proposed to augment category text with class-wise visual information. To address the learning inertia problem brought by the frozen detector, a vision conditioned masked language prediction strategy is proposed. MQ-Det's simple yet effective architecture and training strategy design is compatible with most language-queried object detectors, thus yielding versatile applications. Experimental results demonstrate that multi-modal queries largely boost open-world detection. For instance, MQ-Det significantly improves the state-of-the-art open-set detector GLIP by +7.8% AP on the LVIS benchmark via multi-modal queries without any downstream finetuning, and averagely +6.3% AP on 13 few-shot downstream tasks, with merely additional 3% modulating time required by GLIP. Code is available at https://github.com/YifanXu74/MQ-Det.

</details>

### M2SODAI: Multi-Modal Maritime Object Detection Dataset With RGB and Hyperspectral Image Sensors.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a8757b889350a3782b384a3ec0dfbae9-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 2
- **作者**: Jonggyu Jang, Sangwoo Oh, Youjin Kim, Dongmin Seo, Youngchol Choi, Hyun Jong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### VLATTACK: Multimodal Adversarial Attacks on Vision-Language Tasks via Pre-trained Models.
- **链接**: [arXiv:2310.04655](https://arxiv.org/abs/2310.04655) · [代码](https://github.com/ericyinyzy/VLAttack) · 📚 被引 11
- **作者**: Ziyi Yin, Muchao Ye, Tianrong Zhang, Tianyu Du, Jinguo Zhu, Han Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language (VL) pre-trained models have shown their superiority on many multimodal tasks. However, the adversarial robustness of such models has not been fully explored. Existing approaches mainly focus on exploring the adversarial robustness under the white-box setting, which is unrealistic. In this paper, we aim to investigate a new yet practical task to craft image and text perturbations using pre-trained VL models to attack black-box fine-tuned models on different downstream tasks. Towards this end, we propose VLATTACK to generate adversarial samples by fusing perturbations of images and texts from both single-modal and multimodal levels. At the single-modal level, we propose a new block-wise similarity attack (BSA) strategy to learn image perturbations for disrupting universal representations. Besides, we adopt an existing text attack strategy to generate text perturbations independent of the image-modal attack. At the multimodal level, we design a novel iterative cross-search attack (ICSA) method to update adversarial image-text pairs periodically, starting with the outputs from the single-modal level. We conduct extensive experiments to attack five widely-used VL pre-trained models for six tasks. Experimental results show that VLATTACK achieves the highest attack success rates on all tasks compared with state-of-the-art baselines, which reveals a blind spot in the deployment of pre-trained VL models. Source codes can be found at https://github.com/ericyinyzy/VLAttack.

</details>

### Brain encoding models based on multimodal transformers can transfer across language and vision.
- **链接**: [arXiv:2305.12248](https://arxiv.org/abs/2305.12248) · 📚 被引 7
- **作者**: Jerry Tang, Meng Du, Vy A. Vo, Vasudev Lal, Alexander Huth
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Encoding models have been used to assess how the human brain represents concepts in language and vision. While language and vision rely on similar concept representations, current encoding models are typically trained and tested on brain responses to each modality in isolation. Recent advances in multimodal pretraining have produced transformers that can extract aligned representations of concepts in language and vision. In this work, we used representations from multimodal transformers to train encoding models that can transfer across fMRI responses to stories and movies. We found that encoding models trained on brain responses to one modality can successfully predict brain responses to the other modality, particularly in cortical regions that represent conceptual meaning. Further analysis of these encoding models revealed shared semantic dimensions that underlie concept representations in language and vision. Comparing encoding models trained using representations from multimodal and unimodal transformers, we found that multimodal transformers learn more aligned representations of concepts in language and vision. Our results demonstrate how multimodal transformers can provide insights into the brain's capacity for multimodal processing.

</details>

### Parameter-efficient Tuning of Large-scale Multimodal Foundation Model.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/32ebb6b560ee58abbdae834e5f37cb5d-Abstract-Conference.html) · 📚 被引 6
- **作者**: Haixin Wang, Xinlong Yang, Jianlong Chang, Dian Jin, Jinan Sun, Shikun Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### MuSe-GNN: Learning Unified Gene Representation From Multimodal Biological Graph Data.
- **链接**: [arXiv:2310.02275](https://arxiv.org/abs/2310.02275) · 📚 被引 11
- **作者**: Tianyu Liu, Yuge Wang, Rex Ying, Hongyu Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Discovering genes with similar functions across diverse biomedical contexts poses a significant challenge in gene representation learning due to data heterogeneity. In this study, we resolve this problem by introducing a novel model called Multimodal Similarity Learning Graph Neural Network, which combines Multimodal Machine Learning and Deep Graph Neural Networks to learn gene representations from single-cell sequencing and spatial transcriptomic data. Leveraging 82 training datasets from 10 tissues, three sequencing techniques, and three species, we create informative graph structures for model training and gene representations generation, while incorporating regularization with weighted similarity learning and contrastive learning to learn cross-data gene-gene relationships. This novel design ensures that we can offer gene representations containing functional similarity across different contexts in a joint space. Comprehensive benchmarking analysis shows our model's capacity to effectively capture gene function similarity across multiple modalities, outperforming state-of-the-art methods in gene representation learning by up to 97.5%. Moreover, we employ bioinformatics tools in conjunction with gene representations to uncover pathway enrichment, regulation causal networks, and functions of disease-associated or dosage-sensitive genes. Therefore, our model efficiently produces unified gene representations for the analysis of gene functions, tissue functions, diseases, and species evolution.

</details>

### Integration-free Training for Spatio-temporal Multimodal Covariate Deep Kernel Point Processes.
- **链接**: [arXiv:2310.05485](https://arxiv.org/abs/2310.05485) · 📚 被引 0
- **作者**: Yixuan Zhang, Quyu Kong, Feng Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we propose a novel deep spatio-temporal point process model, Deep Kernel Mixture Point Processes (DKMPP), that incorporates multimodal covariate information. DKMPP is an enhanced version of Deep Mixture Point Processes (DMPP), which uses a more flexible deep kernel to model complex relationships between events and covariate data, improving the model's expressiveness. To address the intractable training procedure of DKMPP due to the non-integrable deep kernel, we utilize an integration-free method based on score matching, and further improve efficiency by adopting a scalable denoising score matching method. Our experiments demonstrate that DKMPP and its corresponding score-based estimators outperform baseline models, showcasing the advantages of incorporating covariate information, utilizing a deep kernel, and employing score-based estimators.

</details>

### Alternating Gradient Descent and Mixture-of-Experts for Integrated Multimodal Perception.
- **链接**: [arXiv:2305.06324](https://arxiv.org/abs/2305.06324) · 📚 被引 1
- **作者**: Hassan Akbari, Dan Kondratyuk, Yin Cui, Rachel Hornung, Huisheng Wang, Hartwig Adam
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Integrated Multimodal Perception (IMP), a simple and scalable multimodal multi-task training and modeling approach. IMP integrates multimodal inputs including image, video, text, and audio into a single Transformer encoder with minimal modality-specific components. IMP makes use of a novel design that combines Alternating Gradient Descent (AGD) and Mixture-of-Experts (MoE) for efficient model and task scaling. We conduct extensive empirical studies and reveal the following key insights: 1) Performing gradient descent updates by alternating on diverse modalities, loss functions, and tasks, with varying input resolutions, efficiently improves the model. 2) Sparsification with MoE on a single modality-agnostic encoder substantially improves the performance, outperforming dense models that use modality-specific encoders or additional fusion layers and greatly mitigates the conflicts between modalities. IMP achieves competitive performance on a wide range of downstream tasks including video classification, image classification, image-text, and video-text retrieval. Most notably, we train a sparse IMP-MoE-L variant focusing on video tasks that achieves new state-of-the-art in zero-shot video classification: 77.0% on Kinetics-400, 76.8% on Kinetics-600, and 68.3% on Kinetics-700, improving the previous state-of-the-art by +5%, +6.7%, and +5.8%, respectively, while using only 15% of their total training computational cost.

</details>

### Learning to Taste: A Multimodal Wine Dataset.
- **链接**: [arXiv:2308.16900](https://arxiv.org/abs/2308.16900) · 📚 被引 2
- **作者**: Thoranna Bender, Simon Møe Sørensen, Alireza Kashani, Kristjan Eldjarn Hjorleifsson, Grethe Hyldig, Søren Hauberg et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present WineSensed, a large multimodal wine dataset for studying the relations between visual perception, language, and flavor. The dataset encompasses 897k images of wine labels and 824k reviews of wines curated from the Vivino platform. It has over 350k unique bottlings, annotated with year, region, rating, alcohol percentage, price, and grape composition. We obtained fine-grained flavor annotations on a subset by conducting a wine-tasting experiment with 256 participants who were asked to rank wines based on their similarity in flavor, resulting in more than 5k pairwise flavor distances. We propose a low-dimensional concept embedding algorithm that combines human experience with automatic machine similarity kernels. We demonstrate that this shared concept embedding space improves upon separate embedding spaces for coarse flavor classification (alcohol percentage, country, grape, price, rating) and aligns with the intricate human perception of flavor.

</details>

### Into the LAION's Den: Investigating Hate in Multimodal Datasets.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/42f225509e8263e2043c9d834ccd9a2b-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 17
- **作者**: Abeba Birhane, Vinay Uday Prabhu, Sanghyun Han, Vishnu Boddeti, Sasha Luccioni
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### StressID: a Multimodal Dataset for Stress Identification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5f09bfe6730e9627a9f800d01a8ad5cd-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 5
- **作者**: Hava Chaptoukaev, Valeriya Strizhkova, Michele Panariello, Bianca Dalpaos, Aglind Reka, Valeria Manera et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### AircraftVerse: A Large-Scale Multimodal Dataset of Aerial Vehicle Designs.
- **链接**: [arXiv:2306.05562](https://arxiv.org/abs/2306.05562) · [代码](https://github.com/SRI-CSL/AircraftVerse) · 📚 被引 3
- **作者**: Adam D. Cobb, Anirban Roy, Daniel Elenius, F. Michael Heim, Brian Swenson, Sydney Whittington et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present AircraftVerse, a publicly available aerial vehicle design dataset. Aircraft design encompasses different physics domains and, hence, multiple modalities of representation. The evaluation of these cyber-physical system (CPS) designs requires the use of scientific analytical and simulation models ranging from computer-aided design tools for structural and manufacturing analysis, computational fluid dynamics tools for drag and lift computation, battery models for energy estimation, and simulation models for flight control and dynamics. AircraftVerse contains 27,714 diverse air vehicle designs - the largest corpus of engineering designs with this level of complexity. Each design comprises the following artifacts: a symbolic design tree describing topology, propulsion subsystem, battery subsystem, and other design details; a STandard for the Exchange of Product (STEP) model data; a 3D CAD design using a stereolithography (STL) file format; a 3D point cloud for the shape of the design; and evaluation results from high fidelity state-of-the-art physics models that characterize performance metrics such as maximum flight distance and hover-time. We also present baseline surrogate models that use different modalities of design representation to predict design performance metrics, which we provide as part of our dataset release. Finally, we discuss the potential impact of this dataset on the use of learning in aircraft design and, more generally, in CPS. AircraftVerse is accompanied by a data card, and it is released under Creative Commons Attribution-ShareAlike (CC BY-SA) license. The dataset is hosted at https://zenodo.org/record/6525446, baseline models and code at https://github.com/SRI-CSL/AircraftVerse, and the dataset description at https://aircraftverse.onrender.com/.

</details>

### ProBio: A Protocol-guided Multimodal Dataset for Molecular Biology Lab.
- **链接**: [arXiv:2311.00556](https://arxiv.org/abs/2311.00556) · 📚 被引 2
- **作者**: Jieming Cui, Ziren Gong, Baoxiong Jia, Siyuan Huang, Zilong Zheng, Jianzhu Ma et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The challenge of replicating research results has posed a significant impediment to the field of molecular biology. The advent of modern intelligent systems has led to notable progress in various domains. Consequently, we embarked on an investigation of intelligent monitoring systems as a means of tackling the issue of the reproducibility crisis. Specifically, we first curate a comprehensive multimodal dataset, named ProBio, as an initial step towards this objective. This dataset comprises fine-grained hierarchical annotations intended for the purpose of studying activity understanding in BioLab. Next, we devise two challenging benchmarks, transparent solution tracking and multimodal action recognition, to emphasize the unique characteristics and difficulties associated with activity understanding in BioLab settings. Finally, we provide a thorough experimental evaluation of contemporary video understanding models and highlight their limitations in this specialized domain to identify potential avenues for future research. We hope ProBio with associated benchmarks may garner increased focus on modern AI techniques in the realm of molecular biology.

</details>

### DataComp: In search of the next generation of multimodal datasets.
- **链接**: [arXiv:2304.14108](https://arxiv.org/abs/2304.14108)
- **作者**: Samir Yitzhak Gadre, Gabriel Ilharco, Alex Fang, Jonathan Hayase, Georgios Smyrnis, Thao Nguyen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal datasets are a critical component in recent breakthroughs such as Stable Diffusion and GPT-4, yet their design does not receive the same research attention as model architectures or training algorithms. To address this shortcoming in the ML ecosystem, we introduce DataComp, a testbed for dataset experiments centered around a new candidate pool of 12.8 billion image-text pairs from Common Crawl. Participants in our benchmark design new filtering techniques or curate new data sources and then evaluate their new dataset by running our standardized CLIP training code and testing the resulting model on 38 downstream test sets. Our benchmark consists of multiple compute scales spanning four orders of magnitude, which enables the study of scaling trends and makes the benchmark accessible to researchers with varying resources. Our baseline experiments show that the DataComp workflow leads to better training sets. In particular, our best baseline, DataComp-1B, enables training a CLIP ViT-L/14 from scratch to 79.2% zero-shot accuracy on ImageNet, outperforming OpenAI's CLIP ViT-L/14 by 3.7 percentage points while using the same training procedure and compute. We release DataComp and all accompanying code at www.datacomp.ai.

</details>

### RegBN: Batch Normalization of Multimodal Data with Regularization.
- **链接**: [arXiv:2310.00641](https://arxiv.org/abs/2310.00641) · [代码](https://github.com/mogvision/regbn) · 📚 被引 2
- **作者**: Morteza Ghahremani, Christian Wachinger
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent years have witnessed a surge of interest in integrating high-dimensional data captured by multisource sensors, driven by the impressive success of neural networks in the integration of multimodal data. However, the integration of heterogeneous multimodal data poses a significant challenge, as confounding effects and dependencies among such heterogeneous data sources introduce unwanted variability and bias, leading to suboptimal performance of multimodal models. Therefore, it becomes crucial to normalize the low- or high-level features extracted from data modalities before their fusion takes place. This paper introduces a novel approach for the normalization of multimodal data, called RegBN, that incorporates regularization. RegBN uses the Frobenius norm as a regularizer term to address the side effects of confounders and underlying dependencies among different data sources. The proposed method generalizes well across multiple modalities and eliminates the need for learnable parameters, simplifying training and inference. We validate the effectiveness of RegBN on eight databases from five research areas, encompassing diverse modalities such as language, audio, image, video, depth, tabular, and 3D MRI. The proposed method demonstrates broad applicability across different architectures such as multilayer perceptrons, convolutional neural networks, and vision transformers, enabling effective normalization of both low- and high-level features in multimodal neural networks. RegBN is available at \url{https://github.com/mogvision/regbn}.

</details>

### INSPECT: A Multimodal Dataset for Patient Outcome Prediction of Pulmonary Embolisms.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/39736af1b9d87a1fddad9f84a6bcf64c-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 4
- **作者**: Shih-Cheng Huang, Zepeng Huo, Ethan Steinberg, Chia-Chun Chiang, Curtis P. Langlotz, Matthew P. Lungren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Beyond Unimodal: Generalising Neural Processes for Multimodal Uncertainty Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/839e23e5b1c52cfd1268f4023a3af0d6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Myong Chol Jung, He Zhao, Joanna Dipnall, Lan Du
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Guide Your Agent with Adaptive Multimodal Rewards.
- **链接**: [arXiv:2309.10790](https://arxiv.org/abs/2309.10790) · 📚 被引 2
- **作者**: Changyeon Kim, Younggyo Seo, Hao Liu, Lisa Lee, Jinwoo Shin, Honglak Lee et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Developing an agent capable of adapting to unseen environments remains a difficult challenge in imitation learning. This work presents Adaptive Return-conditioned Policy (ARP), an efficient framework designed to enhance the agent's generalization ability using natural language task descriptions and pre-trained multimodal encoders. Our key idea is to calculate a similarity between visual observations and natural language instructions in the pre-trained multimodal embedding space (such as CLIP) and use it as a reward signal. We then train a return-conditioned policy using expert demonstrations labeled with multimodal rewards. Because the multimodal rewards provide adaptive signals at each timestep, our ARP effectively mitigates the goal misgeneralization. This results in superior generalization performances even when faced with unseen text instructions, compared to existing text-conditioned policies. To improve the quality of rewards, we also introduce a fine-tuning method for pre-trained multimodal encoders, further enhancing the performance. Video demonstrations and source code are available on the project website: \url{https://sites.google.com/view/2023arp}.

</details>

### Generating Images with Multimodal Language Models.
- **链接**: [arXiv:2305.17216](https://arxiv.org/abs/2305.17216) · 📚 被引 22
- **作者**: Jing Yu Koh, Daniel Fried, Russ Salakhutdinov
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a method to fuse frozen text-only large language models (LLMs) with pre-trained image encoder and decoder models, by mapping between their embedding spaces. Our model demonstrates a wide suite of multimodal capabilities: image retrieval, novel image generation, and multimodal dialogue. Ours is the first approach capable of conditioning on arbitrarily interleaved image and text inputs to generate coherent image (and text) outputs. To achieve strong performance on image generation, we propose an efficient mapping network to ground the LLM to an off-the-shelf text-to-image generation model. This mapping network translates hidden representations of text into the embedding space of the visual models, enabling us to leverage the strong text representations of the LLM for visual outputs. Our approach outperforms baseline generation models on tasks with longer and more complex language. In addition to novel image generation, our model is also capable of image retrieval from a prespecified dataset, and decides whether to retrieve or generate at inference time. This is done with a learnt decision module which conditions on the hidden representations of the LLM. Our model exhibits a wider range of capabilities compared to prior multimodal language models. It can process image-and-text inputs, and produce retrieved images, generated images, and generated text -- outperforming non-LLM based generation models across several text-to-image tasks that measure context dependence.

</details>

### Quantifying & Modeling Multimodal Interactions: An Information Decomposition Framework.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/575286a73f238b6516ce0467d67eadb2-Abstract-Conference.html) · 📚 被引 12
- **作者**: Paul Pu Liang, Yun Cheng, Xiang Fan, Chun Kai Ling, Suzanne Nie, Richard J. Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### FOCAL: Contrastive Learning for Multimodal Time-Series Sensing Signals in Factorized Orthogonal Latent Space.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/93e98ddf39a9beb0a97fbbe56a986c80-Abstract-Conference.html)
- **作者**: Shengzhong Liu, Tomoyoshi Kimura, Dongxin Liu, Ruijie Wang, Jinyang Li, Suhas N. Diggavi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### A Theory of Multimodal Learning.
- **链接**: [arXiv:2309.12458](https://arxiv.org/abs/2309.12458)
- **作者**: Zhou Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human perception of the empirical world involves recognizing the diverse appearances, or 'modalities', of underlying objects. Despite the longstanding consideration of this perspective in philosophy and cognitive science, the study of multimodality remains relatively under-explored within the field of machine learning. Nevertheless, current studies of multimodal machine learning are limited to empirical practices, lacking theoretical foundations beyond heuristic arguments. An intriguing finding from the practice of multimodal learning is that a model trained on multiple modalities can outperform a finely-tuned unimodal model, even on unimodal tasks. This paper provides a theoretical framework that explains this phenomenon, by studying generalization properties of multimodal learning algorithms. We demonstrate that multimodal learning allows for a superior generalization bound compared to unimodal learning, up to a factor of $O(\sqrt{n})$, where $n$ represents the sample size. Such advantage occurs when both connection and heterogeneity exist between the modalities.

</details>

### Foundation Model is Efficient Multimodal Multitask Model Selector.
- **链接**: [arXiv:2308.06262](https://arxiv.org/abs/2308.06262) · [代码](https://github.com/OpenGVLab/Multitask-Model-Selector) · 📚 被引 1
- **作者**: Fanqing Meng, Wenqi Shao, Zhanglin Peng, Chonghe Jiang, Kaipeng Zhang, Yu Qiao et al.
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper investigates an under-explored but important problem: given a collection of pre-trained neural networks, predicting their performance on each multi-modal task without fine-tuning them, such as image recognition, referring, captioning, visual question answering, and text question answering. A brute-force approach is to finetune all models on all target datasets, bringing high computational costs. Although recent-advanced approaches employed lightweight metrics to measure models' transferability,they often depend heavily on the prior knowledge of a single task, making them inapplicable in a multi-modal multi-task scenario. To tackle this issue, we propose an efficient multi-task model selector (EMMS), which employs large-scale foundation models to transform diverse label formats such as categories, texts, and bounding boxes of different downstream tasks into a unified noisy label embedding. EMMS can estimate a model's transferability through a simple weighted linear regression, which can be efficiently solved by an alternating minimization algorithm with a convergence guarantee. Extensive experiments on 5 downstream tasks with 24 datasets show that EMMS is fast, effective, and generic enough to assess the transferability of pre-trained models, making it the first model selection method in the multi-task scenario. For instance, compared with the state-of-the-art method LogME enhanced by our label embeddings, EMMS achieves 9.0\%, 26.3\%, 20.1\%, 54.8\%, 12.2\% performance gain on image recognition, referring, captioning, visual question answering, and text question answering, while bringing 5.13x, 6.29x, 3.59x, 6.19x, and 5.66x speedup in wall-clock time, respectively. The code is available at https://github.com/OpenGVLab/Multitask-Model-Selector.

</details>

### 4M: Massively Multimodal Masked Modeling.
- **链接**: [arXiv:2312.06647](https://arxiv.org/abs/2312.06647) · 📚 被引 6
- **作者**: David Mizrahi, Roman Bachmann, Oguzhan Fatih Kar, Teresa Yeo, Mingfei Gao, Afshin Dehghan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current machine learning models for vision are often highly specialized and limited to a single modality and task. In contrast, recent large language models exhibit a wide range of capabilities, hinting at a possibility for similarly versatile models in computer vision. In this paper, we take a step in this direction and propose a multimodal training scheme called 4M. It consists of training a single unified Transformer encoder-decoder using a masked modeling objective across a wide range of input/output modalities - including text, images, geometric, and semantic modalities, as well as neural network feature maps. 4M achieves scalability by unifying the representation space of all modalities through mapping them into discrete tokens and performing multimodal masked modeling on a small randomized subset of tokens. 4M leads to models that exhibit several key capabilities: (1) they can perform a diverse set of vision tasks out of the box, (2) they excel when fine-tuned for unseen downstream tasks or new input modalities, and (3) they can function as a generative model that can be conditioned on arbitrary modalities, enabling a wide variety of expressive multimodal editing capabilities with remarkable flexibility. Through experimental analyses, we demonstrate the potential of 4M for training versatile and scalable foundation models for vision tasks, setting the stage for further exploration in multimodal learning for vision and other domains.

</details>

### Improving multimodal datasets with image captioning.
- **链接**: [arXiv:2307.10350](https://arxiv.org/abs/2307.10350) · 📚 被引 10
- **作者**: Thao Nguyen, Samir Yitzhak Gadre, Gabriel Ilharco, Sewoong Oh, Ludwig Schmidt
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Massive web datasets play a key role in the success of large vision-language models like CLIP and Flamingo. However, the raw web data is noisy, and existing filtering methods to reduce noise often come at the expense of data diversity. Our work focuses on caption quality as one major source of noise, and studies how generated captions can increase the utility of web-scraped datapoints with nondescript text. Through exploring different mixing strategies for raw and generated captions, we outperform the best filtering method proposed by the DataComp benchmark by 2% on ImageNet and 4% on average across 38 tasks, given a candidate pool of 128M image-text pairs. Our best approach is also 2x better at Flickr and MS-COCO retrieval. We then analyze what makes synthetic captions an effective source of text supervision. In experimenting with different image captioning models, we also demonstrate that the performance of a model on standard image captioning benchmarks (e.g., NoCaps CIDEr) is not a reliable indicator of the utility of the captions it generates for multimodal training. Finally, our experiments with using generated captions at DataComp's large scale (1.28B image-text pairs) offer insights into the limitations of synthetic text, as well as the importance of image curation with increasing training data quantity. The synthetic captions used in our experiments are now available on HuggingFace.

</details>

### ASIF: Coupled Data Turns Unimodal Models to Multimodal without Training.
- **链接**: [arXiv:2210.01738](https://arxiv.org/abs/2210.01738) · 📚 被引 0
- **作者**: Antonio Norelli, Marco Fumero, Valentino Maiorca, Luca Moschella, Emanuele Rodolà, Francesco Locatello
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> CLIP proved that aligning visual and language spaces is key to solving many vision tasks without explicit training, but required to train image and text encoders from scratch on a huge dataset. LiT improved this by only training the text encoder and using a pre-trained vision network. In this paper, we show that a common space can be created without any training at all, using single-domain encoders (trained with or without supervision) and a much smaller amount of image-text pairs. Furthermore, our model has unique properties. Most notably, deploying a new version with updated training samples can be done in a matter of seconds. Additionally, the representations in the common space are easily interpretable as every dimension corresponds to the similarity of the input to a unique image-text pair in the multimodal dataset. Experiments on standard zero-shot visual benchmarks demonstrate the typical transfer ability of image-text models. Overall, our method represents a simple yet surprisingly strong baseline for foundation multimodal models, raising important questions on their data efficiency and on the role of retrieval in machine learning.

</details>

### MultiMoDN - Multimodal, Multi-Task, Interpretable Modular Networks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/5951641ad71b0052cf776f9b71f18932-Abstract-Conference.html)
- **作者**: Vinitra Swamy, Malika Satayeva, Jibril Frej, Thierry Bossy, Thijs Vogels, Martin Jaggi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Mass-Producing Failures of Multimodal Systems with Language Models.
- **链接**: [arXiv:2306.12105](https://arxiv.org/abs/2306.12105) · [代码](https://github.com/tsb0601/MultiMon) · 📚 被引 8
- **作者**: Shengbang Tong, Erik Jones, Jacob Steinhardt
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deployed multimodal systems can fail in ways that evaluators did not anticipate. In order to find these failures before deployment, we introduce MultiMon, a system that automatically identifies systematic failures -- generalizable, natural-language descriptions of patterns of model failures. To uncover systematic failures, MultiMon scrapes a corpus for examples of erroneous agreement: inputs that produce the same output, but should not. It then prompts a language model (e.g., GPT-4) to find systematic patterns of failure and describe them in natural language. We use MultiMon to find 14 systematic failures (e.g., "ignores quantifiers") of the CLIP text-encoder, each comprising hundreds of distinct inputs (e.g., "a shelf with a few/many books"). Because CLIP is the backbone for most state-of-the-art multimodal systems, these inputs produce failures in Midjourney 5.1, DALL-E, VideoFusion, and others. MultiMon can also steer towards failures relevant to specific use cases, such as self-driving cars. We see MultiMon as a step towards evaluation that autonomously explores the long tail of potential system failures. Code for MULTIMON is available at https://github.com/tsb0601/MultiMon.

</details>

### Training Transitive and Commutative Multimodal Transformers with LoReTTa.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/860a092bb4d9d81d3133a01c50c01578-Abstract-Conference.html) · 📚 被引 0
- **作者**: Manuel Tran, Yashin Dicente Cid, Amal Lahiani, Fabian J. Theis, Tingying Peng, Eldad Klaiman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Implicit Differentiable Outlier Detection Enable Robust Deep Multimodal Analysis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2cf153951b5e9b39564fc4a0ef6adc1a-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zhu Wang, Sourav Medya, Sathya N. Ravi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Injecting Multimodal Information into Rigid Protein Docking via Bi-level Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/77fa0e7d45c6687f1958de0b31e9fc05-Abstract-Conference.html) · 📚 被引 1
- **作者**: Ruijia Wang, YiWu Sun, Yujie Luo, Shaochuan Li, Cheng Yang, Xingyi Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### HOH: Markerless Multimodal Human-Object-Human Handover Dataset with Large Object Count.
- **链接**: [arXiv:2310.00723](https://arxiv.org/abs/2310.00723) · 📚 被引 1
- **作者**: Noah Wiederhold, Ava Megyeri, DiMaggio Paris, Sean Banerjee, Natasha Banerjee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Achieving Cross Modal Generalization with Multimodal Unified Representation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/c89f09849eb5af489abb122394ff0f0b-Abstract-Conference.html) · 📚 被引 5
- **作者**: Yan Xia, Hai Huang, Jieming Zhu, Zhou Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Multimodal Deep Learning Model Unveils Behavioral Dynamics of V1 Activity in Freely Moving Mice.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/31a19921acd38cdf7a8c86ec032cef2d-Abstract-Conference.html) · 📚 被引 2
- **作者**: Aiwen Xu, Yuchen Hou, Cristopher Niell, Michael Beyeler
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### RH-BrainFS: Regional Heterogeneous Multimodal Brain Networks Fusion Strategy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b9c353d02e565f0f7cba94c4f3584eaa-Abstract-Conference.html) · 📚 被引 5
- **作者**: Hongting Ye, Yalu Zheng, Yueying Li, Ke Zhang, Youyong Kong, Yonggui Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### SPAE: Semantic Pyramid AutoEncoder for Multimodal Generation with Frozen LLMs.
- **链接**: [arXiv:2306.17842](https://arxiv.org/abs/2306.17842) · 📚 被引 4
- **作者**: Lijun Yu, Yong Cheng, Zhiruo Wang, Vivek Kumar, Wolfgang Macherey, Yanping Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Intelligent Knee Sleeves: A Real-time Multimodal Dataset for 3D Lower Body Motion Estimation Using Smart Textile.
- **链接**: [arXiv:2311.12829](https://arxiv.org/abs/2311.12829) · 📚 被引 1
- **作者**: Wenwen Zhang, Arvin Tashakori, Zenan Jiang, Amir Servati, Harishkumar Narayana, Saeid Soltanian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The kinematics of human movements and locomotion are closely linked to the activation and contractions of muscles. To investigate this, we present a multimodal dataset with benchmarks collected using a novel pair of Intelligent Knee Sleeves (Texavie MarsWear Knee Sleeves) for human pose estimation. Our system utilizes synchronized datasets that comprise time-series data from the Knee Sleeves and the corresponding ground truth labels from the visualized motion capture camera system. We employ these to generate 3D human models solely based on the wearable data of individuals performing different activities. We demonstrate the effectiveness of this camera-free system and machine learning algorithms in the assessment of various movements and exercises, including extension to unseen exercises and individuals. The results show an average error of 7.21 degrees across all eight lower body joints when compared to the ground truth, indicating the effectiveness and reliability of the Knee Sleeve system for the prediction of different lower body joints beyond the knees. The results enable human pose estimation in a seamless manner without being limited by visual occlusion or the field of view of cameras. Our results show the potential of multimodal wearable sensing in a variety of applications from home fitness to sports, healthcare, and physical rehabilitation focusing on pose and movement estimation.

</details>

### DDCoT: Duty-Distinct Chain-of-Thought Prompting for Multimodal Reasoning in Language Models.
- **链接**: [arXiv:2310.16436](https://arxiv.org/abs/2310.16436) · 📚 被引 29
- **作者**: Ge Zheng, Bin Yang, Jiajin Tang, Hong-Yu Zhou, Sibei Yang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A long-standing goal of AI systems is to perform complex multimodal reasoning like humans. Recently, large language models (LLMs) have made remarkable strides in such multi-step reasoning on the language modality solely by leveraging the chain of thought (CoT) to mimic human thinking. However, the transfer of these advancements to multimodal contexts introduces heightened challenges, including but not limited to the impractical need for labor-intensive annotation and the limitations in terms of flexibility, generalizability, and explainability. To evoke CoT reasoning in multimodality, this work first conducts an in-depth analysis of these challenges posed by multimodality and presents two key insights: "keeping critical thinking" and "letting everyone do their jobs" in multimodal CoT reasoning. Furthermore, this study proposes a novel DDCoT prompting that maintains a critical attitude through negative-space prompting and incorporates multimodality into reasoning by first dividing the reasoning responsibility of LLMs into reasoning and recognition and then integrating the visual recognition capability of visual models into the joint reasoning process. The rationales generated by DDCoT not only improve the reasoning abilities of both large and small language models in zero-shot prompting and fine-tuning learning, significantly outperforming state-of-the-art methods but also exhibit impressive generalizability and explainability.

</details>

### Multimodal C4: An Open, Billion-scale Corpus of Images Interleaved with Text.
- **链接**: [arXiv:2304.06939](https://arxiv.org/abs/2304.06939) · 📚 被引 4
- **作者**: Wanrong Zhu, Jack Hessel, Anas Awadalla, Samir Yitzhak Gadre, Jesse Dodge, Alex Fang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In-context vision and language models like Flamingo support arbitrarily interleaved sequences of images and text as input. This format not only enables few-shot learning via interleaving independent supervised (image, text) examples, but also, more complex prompts involving interaction between images, e.g., "What do image A and image B have in common?" To support this interface, pretraining occurs over web corpora that similarly contain interleaved images+text. To date, however, large-scale data of this form have not been publicly available. We release Multimodal C4, an augmentation of the popular text-only C4 corpus with images interleaved. We use a linear assignment algorithm to place images into longer bodies of text using CLIP features, a process that we show outperforms alternatives. Multimodal C4 spans everyday topics like cooking, travel, technology, etc. A manual inspection of a random sample of documents shows that a vast majority (88%) of images are topically relevant, and that linear assignment frequently selects individual sentences specifically well-aligned with each image (80%). After filtering NSFW images, ads, etc., the resulting corpus consists of 101.2M documents with 571M images interleaved in 43B English tokens.

</details>

## 跨领域论文（完整笔记在其他领域）

- CoDA: Collaborative Novel Box Discovery and Cross-modal Alignment for Open-vocabulary 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Leveraging Vision-Centric Multi-Modal Expertise for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Unleash the Potential of Image Branch for Cross-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
