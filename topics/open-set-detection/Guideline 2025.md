# Open-set Detection — 2025 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OpenLex3D: A Tiered Benchmark for Open-Vocabulary 3D Scene Representations.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/05057404e0cab4fe58971dc3a7d6044c-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Christina Kassab, Sacha Morin, Martin Büchner, Matías Mattamala, Kumaraditya Gupta, Abhinav Valada et al.
- **🏷️ 机构**: University of Oxford, Mila, Université de Montréal, Albert-Ludwigs-Universität Freiburg
- **会议**: NeurIPS 2025

### Novel Class Discovery for Point Cloud Segmentation via Joint Learning of Causal Representation and Reasoning.
- **链接**: [arXiv:2510.13307](https://arxiv.org/abs/2510.13307) · 📚 被引 0
- **作者**: Yang Li, Aming Wu, Zihao Zhang, Yahong Han
- **🏷️ 机构**: Tsinghua-Berkeley Shenzhen Institute, Xidian University, Henan University of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we focus on Novel Class Discovery for Point Cloud Segmentation (3D-NCD), aiming to learn a model that can segment unlabeled (novel) 3D classes using only the supervision from labeled (base) 3D classes. The key to this task is to setup the exact correlations between the point representations and their base class labels, as well as the representation correlations between the points from base and novel classes. A coarse or statistical correlation learning may lead to the confusion in novel class inference. lf we impose a causal relationship as a strong correlated constraint upon the learning process, the essential point cloud representations that accurately correspond to the classes should be uncovered. To this end, we introduce a structural causal model (SCM) to re-formalize the 3D-NCD problem and propose a new method, i.e., Joint Learning of Causal Representation and Reasoning. Specifically, we first analyze hidden confounders in the base class representations and the causal relationships between the base and novel classes through SCM. We devise a causal representation prototype that eliminates confounders to capture the causal representations of base classes. A graph structure is then used to model the causal relationships between the base classes' causal representation prototypes and the novel class prototypes, enabling causal reasoning from base to novel classes. Extensive experiments and visualization results on 3D and 2D NCD semantic segmentation demonstrate the superiorities of our method.

</details>

### DOVTrack: Data-Efficient Open-Vocabulary Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/83538ee6cde54c0a3df02dc629ab8edd-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zekun Qian, Ruize Han, Zhixiang Wang, Junhui Hou, Wei Feng
- **🏷️ 机构**: Tianjin University           City University of Hong Kong, Shenzhen University of Advanced Technology, CyberAgent
- **会议**: NeurIPS 2025

### OpenHype: Hyperbolic Embeddings for Hierarchical Open-Vocabulary Radiance Fields.
- **链接**: [arXiv:2510.21441](https://arxiv.org/abs/2510.21441) · 📚 被引 1
- **作者**: Lisa Weijler, Sebastian Koch, Fabio Poiesi, Timo Ropinski, Pedro Hermosilla
- **🏷️ 机构**: Computer Vision Lab, TU Wien, University Ulm, Fondazione Bruno Kessler
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modeling the inherent hierarchical structure of 3D objects and 3D scenes is highly desirable, as it enables a more holistic understanding of environments for autonomous agents. Accomplishing this with implicit representations, such as Neural Radiance Fields, remains an unexplored challenge. Existing methods that explicitly model hierarchical structures often face significant limitations: they either require multiple rendering passes to capture embeddings at different levels of granularity, significantly increasing inference time, or rely on predefined, closed-set discrete hierarchies that generalize poorly to the diverse and nuanced structures encountered by agents in the real world. To address these challenges, we propose OpenHype, a novel approach that represents scene hierarchies using a continuous hyperbolic latent space. By leveraging the properties of hyperbolic geometry, OpenHype naturally encodes multi-scale relationships and enables smooth traversal of hierarchies through geodesic paths in latent space. Our method outperforms state-of-the-art approaches on standard benchmarks, demonstrating superior efficiency and adaptability in 3D scene understanding.

</details>

### Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation.
- **链接**: [arXiv:2506.09881](https://arxiv.org/abs/2506.09881) · [代码](https://github.com/anonymouse-9c53tp182bvz/Vireo) · 📚 被引 1
- **作者**: Siyu Chen, Ting Han, Chengzheng Fu, Changshe Zhang, Chaolei Wang, Jinhe Su et al.
- **🏷️ 机构**: Yale University, SUN YAT-SEN UNIVERSITY, Nanjing University of Aeronautics and Astronautics
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary semantic segmentation (OVSS) and domain generalization in semantic segmentation (DGSS) highlight a subtle complementarity that motivates Open-Vocabulary Domain-Generalized Semantic Segmentation (OV-DGSS). OV-DGSS aims to generate pixel-level masks for unseen categories while maintaining robustness across unseen domains, a critical capability for real-world scenarios such as autonomous driving in adverse conditions. We introduce Vireo, a novel single-stage framework for OV-DGSS that unifies the strengths of OVSS and DGSS for the first time. Vireo builds upon the frozen Visual Foundation Models (VFMs) and incorporates scene geometry via Depth VFMs to extract domain-invariant structural features. To bridge the gap between visual and textual modalities under domain shift, we propose three key components: (1) GeoText Prompts, which align geometric features with language cues and progressively refine VFM encoder representations; (2) Coarse Mask Prior Embedding (CMPE) for enhancing gradient flow for faster convergence and stronger textual influence; and (3) the Domain-Open-Vocabulary Vector Embedding Head (DOV-VEH), which fuses refined structural and semantic features for robust prediction. Comprehensive evaluation on these components demonstrates the effectiveness of our designs. Our proposed Vireo achieves the state-of-the-art performance and surpasses existing methods by a large margin in both domain generalization and open-vocabulary recognition, offering a unified and scalable solution for robust visual understanding in diverse and dynamic environments. Code is available at https://github.com/anonymouse-9c53tp182bvz/Vireo.

</details>

### Beyond the Seen: Bounded Distribution Estimation for Open-Vocabulary Learning.
- **链接**: [arXiv:2510.04770](https://arxiv.org/abs/2510.04770) · 📚 被引 0
- **作者**: Xiaomeng Fan, Yuchuan Mao, Zhi Gao, Yuwei Wu, Jin Chen, Yunde Jia
- **🏷️ 机构**: Beijing Institute of Technology, Shenzhen MSU-BIT University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary learning requires modeling the data distribution in open environments, which consists of both seen-class and unseen-class data. Existing methods estimate the distribution in open environments using seen-class data, where the absence of unseen classes makes the estimation error inherently unidentifiable. Intuitively, learning beyond the seen classes is crucial for distribution estimation to bound the estimation error. We theoretically demonstrate that the distribution can be effectively estimated by generating unseen-class data, through which the estimation error is upper-bounded. Building on this theoretical insight, we propose a novel open-vocabulary learning method, which generates unseen-class data for estimating the distribution in open environments. The method consists of a class-domain-wise data generation pipeline and a distribution alignment algorithm. The data generation pipeline generates unseen-class data under the guidance of a hierarchical semantic tree and domain information inferred from the seen-class data, facilitating accurate distribution estimation. With the generated data, the distribution alignment algorithm estimates and maximizes the posterior probability to enhance generalization in open-vocabulary learning. Extensive experiments on $11$ datasets demonstrate that our method outperforms baseline approaches by up to $14\%$, highlighting its effectiveness and superiority.

</details>

### Seg4Diff: Unveiling Open-Vocabulary Semantic Segmentation in Text-to-Image Diffusion Transformers.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/67b87de31003d4f56e3312a2e04b479d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chaehyun Kim, Heeseong Shin, Eunbeen Hong, Heeji Yoon, Anurag Arnab, Paul Hongsuck Seo et al.
- **🏷️ 机构**: KAIST, Korea Advanced Institute of Science &amp; Technology, Google DeepMind
- **会议**: NeurIPS 2025

### Open-Vocabulary Part Segmentation via Progressive and Boundary-Aware Strategy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/5c186016d0844767209dc36e9e61441b-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xinlong Li, Di Lin, Shaoyiyi Gao, Jiaxin Li, Ruonan Liu, Qing Guo
- **🏷️ 机构**: Tianjin University, nanjing university, Shanghai Jiao Tong University
- **会议**: NeurIPS 2025

### Interaction-Centric Knowledge Infusion and Transfer for Open Vocabulary Scene Graph Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f7b118ed1bfd2a9f366d55021a8bc1e0-Abstract-Conference.html) · 📚 被引 0
- **作者**: Lin Li, Chuhan Zhang, Dong Zhang, Chong Sun, Chen Li, Long Chen
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Hong Kong University of Science and Technology, HKUST
- **会议**: NeurIPS 2025

### Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f2644105c6680950b0adbfa0a2cfb177-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma et al.
- **🏷️ 机构**: Case Western Reserve University, Huazhong University of Science and Technology, Westlake University
- **会议**: NeurIPS 2025

### LangHOPS: Language Grounded Hierarchical Open-Vocabulary Part Segmentation.
- **链接**: [arXiv:2510.25263](https://arxiv.org/abs/2510.25263) · 📚 被引 0
- **作者**: Yang Miao, Jan-Nico Zaech, Xi Wang, Fabien Despinoy, Danda Pani Paudel, Luc Van Gool
- **🏷️ 机构**: INSAIT, Sofia University, Institute for Computer Science, Artificial Intelligence and Technology, ETHZ - ETH Zurich
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose LangHOPS, the first Multimodal Large Language Model (MLLM) based framework for open-vocabulary object-part instance segmentation. Given an image, LangHOPS can jointly detect and segment hierarchical object and part instances from open-vocabulary candidate categories. Unlike prior approaches that rely on heuristic or learnable visual grouping, our approach grounds object-part hierarchies in language space. It integrates the MLLM into the object-part parsing pipeline to leverage its rich knowledge and reasoning capabilities, and link multi-granularity concepts within the hierarchies. We evaluate LangHOPS across multiple challenging scenarios, including in-domain and cross-dataset object-part instance segmentation, and zero-shot semantic segmentation. LangHOPS achieves state-of-the-art results, surpassing previous methods by 5.5% Average Precision (AP) (in-domain) and 4.8% (cross-dataset) on the PartImageNet dataset and by 2.5% mIOU on unseen object parts in ADE20K (zero-shot). Ablation studies further validate the effectiveness of the language-grounded hierarchy and MLLM driven part query refinement strategy. The code will be released here.

</details>

### Test-Time Adaptation of Vision-Language Models for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6c5b82193c5d8e6aa5806239676ddc97-Abstract-Conference.html)
- **作者**: Mehrdad Noori, David Osowiechi, Gustavo Adolfo Vargas Hakim, Ali Bahri, Moslem Yazdanpanah, Sahar Dastani et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### OPMapper: Enhancing Open-Vocabulary Semantic Segmentation with Multi-Guidance Information.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d3248f63ad76392608963b97c095ca33-Abstract-Conference.html) · 📚 被引 1
- **作者**: Xuehui Wang, Chongjie Si, Xue Yang, Yuzhi Zhao, Wenhai Wang, Xiaokang Yang et al.
- **🏷️ 机构**: Shanghai Jiaotong University, Shanghai Jiao Tong University, Shanghai AI Laboratory
- **会议**: NeurIPS 2025

### COS3D: Collaborative Open-Vocabulary 3D Segmentation.
- **链接**: [arXiv:2510.20238](https://arxiv.org/abs/2510.20238) · [代码](https://github.com/Runsong123/COS3D) · 📚 被引 0
- **作者**: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Autodesk, Carnegie Mellon University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D segmentation is a fundamental yet challenging task, requiring a mutual understanding of both segmentation and language. However, existing Gaussian-splatting-based methods rely either on a single 3D language field, leading to inferior segmentation, or on pre-computed class-agnostic segmentations, suffering from error accumulation. To address these limitations, we present COS3D, a new collaborative prompt-segmentation framework that contributes to effectively integrating complementary language and segmentation cues throughout its entire pipeline. We first introduce the new concept of collaborative field, comprising an instance field and a language field, as the cornerstone for collaboration. During training, to effectively construct the collaborative field, our key idea is to capture the intrinsic relationship between the instance field and language field, through a novel instance-to-language feature mapping and designing an efficient two-stage training strategy. During inference, to bridge distinct characteristics of the two fields, we further design an adaptive language-to-instance prompt refinement, promoting high-quality prompt-segmentation inference. Extensive experiments not only demonstrate COS3D's leading performance over existing methods on two widely-used benchmarks but also show its high potential to various applications,~\ie, novel image-based 3D segmentation, hierarchical segmentation, and robotics. The code is publicly available at \href{https://github.com/Runsong123/COS3D}{https://github.com/Runsong123/COS3D}.

</details>

### Zero-Shot Detection of LLM-Generated Text via Implicit Reward Model.
- **链接**: [arXiv:2604.21223](https://arxiv.org/abs/2604.21223) · 📚 被引 0
- **作者**: Runheng Liu, Heyan Huang, Xingchen Xiao, Zhijing Wu
- **🏷️ 机构**: Beijing Institute of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have demonstrated remarkable capabilities across various tasks. However, their ability to generate human-like text has raised concerns about potential misuse. This underscores the need for reliable and effective methods to detect LLM-generated text. In this paper, we propose IRM, a novel zero-shot approach that leverages Implicit Reward Models for LLM-generated text detection. Such implicit reward models can be derived from publicly available instruction-tuned and base models. Previous reward-based method relies on preference construction and task-specific fine-tuning. In comparison, IRM requires neither preference collection nor additional training. We evaluate IRM on the DetectRL benchmark and demonstrate that IRM can achieve superior detection performance, outperforms existing zero-shot and supervised methods in LLM-generated text detection.

</details>

### OOD-Barrier: Build a Middle-Barrier for Open-Set Single-Image Test Time Adaptation via Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/dd391150be8cec625434323f6b1f9d14-Abstract-Conference.html)
- **作者**: Boyang Peng, Sanqing Qu, Tianpei Zou, Fan Lu, Ya Wu, Kai Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

## 跨领域论文（完整笔记在其他领域）

- GUIDED: Granular Understanding via Identification, Detection, and Discrimination for Fine-Grained Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- DitHub: A Modular Framework for Incremental Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- VL-SAM-V2: Open-World Object Detection with General and Specific Query Fusion. → [object-detection](../object-detection/Guideline%202025.md)
- Looking Beyond the Known: Towards a Data Discovery Guided Open-World Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- OVS Meets Continual Learning: Towards Sustainable Open-Vocabulary Segmentation. → [continual-learning](../continual-learning/Guideline%202025.md)
