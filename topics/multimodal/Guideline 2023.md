# Multimodal — 2023 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multi-Modal Classifiers for Open-Vocabulary Object Detection.
- **链接**: [arXiv:2306.05493](https://arxiv.org/abs/2306.05493)
- **作者**: Prannay Kaul, Weidi Xie, Andrew Zisserman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of this paper is open-vocabulary object detection (OVOD) $\unicode{x2013}$ building a model that can detect objects beyond the set of categories seen at training, thus enabling the user to specify categories of interest at inference without the need for model retraining. We adopt a standard two-stage object detector architecture, and explore three ways for specifying novel categories: via language descriptions, via image exemplars, or via a combination of the two. We make three contributions: first, we prompt a large language model (LLM) to generate informative language descriptions for object classes, and construct powerful text-based classifiers; second, we employ a visual aggregator on image exemplars that can ingest any number of images as input, forming vision-based classifiers; and third, we provide a simple method to fuse information from language descriptions and image exemplars, yielding a multi-modal classifier. When evaluating on the challenging LVIS open-vocabulary benchmark we demonstrate that: (i) our text-based classifiers outperform all previous OVOD works; (ii) our vision-based classifiers perform as well as text-based classifiers in prior work; (iii) using multi-modal classifiers perform better than either modality alone; and finally, (iv) our text-based and multi-modal classifiers yield better performance than a fully-supervised detector.

</details>

### Data Poisoning Attacks Against Multimodal Encoders.
- **链接**: [arXiv:2209.15266](https://arxiv.org/abs/2209.15266)
- **作者**: Ziqing Yang, Xinlei He, Zheng Li, Michael Backes, Mathias Humbert, Pascal Berrang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the newly emerged multimodal models, which leverage both visual and linguistic modalities to train powerful encoders, have gained increasing attention. However, learning from a large-scale unlabeled dataset also exposes the model to the risk of potential poisoning attacks, whereby the adversary aims to perturb the model's training data to trigger malicious behaviors in it. In contrast to previous work, only poisoning visual modality, in this work, we take the first step to studying poisoning attacks against multimodal models in both visual and linguistic modalities. Specially, we focus on answering two questions: (1) Is the linguistic modality also vulnerable to poisoning attacks? and (2) Which modality is most vulnerable? To answer the two questions, we propose three types of poisoning attacks against multimodal models. Extensive evaluations on different datasets and model architectures show that all three attacks can achieve significant attack performance while maintaining model utility in both visual and linguistic modalities. Furthermore, we observe that the poisoning effect differs between different modalities. To mitigate the attacks, we propose both pre-training and post-training defenses. We empirically show that both defenses can significantly reduce the attack performance while preserving the model's utility.

</details>

### PaLM-E: An Embodied Multimodal Language Model.
- **链接**: [arXiv:2303.03378](https://arxiv.org/abs/2303.03378)
- **作者**: Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world, e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts. Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings. We train these encodings end-to-end, in conjunction with a pre-trained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, and captioning. Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, and further, exhibits positive transfer: the model benefits from diverse joint training across internet-scale language, vision, and visual-language domains. Our largest model, PaLM-E-562B with 562B parameters, in addition to being trained on robotics tasks, is a visual-language generalist with state-of-the-art performance on OK-VQA, and retains generalist language capabilities with increasing scale.

</details>

### Reparameterized Policy Learning for Multimodal Trajectory Optimization.
- **链接**: [arXiv:2307.10710](https://arxiv.org/abs/2307.10710)
- **作者**: Zhiao Huang, Litian Liang, Zhan Ling, Xuanlin Li, Chuang Gan, Hao Su
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We investigate the challenge of parametrizing policies for reinforcement learning (RL) in high-dimensional continuous action spaces. Our objective is to develop a multimodal policy that overcomes limitations inherent in the commonly-used Gaussian parameterization. To achieve this, we propose a principled framework that models the continuous RL policy as a generative model of optimal trajectories. By conditioning the policy on a latent variable, we derive a novel variational bound as the optimization objective, which promotes exploration of the environment. We then present a practical model-based RL method, called Reparameterized Policy Gradient (RPG), which leverages the multimodal policy parameterization and learned world model to achieve strong exploration capabilities and high data efficiency. Empirical results demonstrate that our method can help agents evade local optima in tasks with dense rewards and solve challenging sparse-reward environments by incorporating an object-centric intrinsic reward. Our method consistently outperforms previous approaches across a range of tasks. Code and supplementary materials are available on the project page https://haosulab.github.io/RPG/

</details>

### VIMA: Robot Manipulation with Multimodal Prompts.
- **链接**: [出版页](https://proceedings.mlr.press/v202/jiang23b.html)
- **作者**: Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### MEWL: Few-shot multimodal word learning with referential uncertainty.
- **链接**: [arXiv:2306.00503](https://arxiv.org/abs/2306.00503)
- **作者**: Guangyuan Jiang, Manjie Xu, Shiji Xin, Wei Liang, Yujia Peng, Chi Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Without explicit feedback, humans can rapidly learn the meaning of words. Children can acquire a new word after just a few passive exposures, a process known as fast mapping. This word learning capability is believed to be the most fundamental building block of multimodal understanding and reasoning. Despite recent advancements in multimodal learning, a systematic and rigorous evaluation is still missing for human-like word learning in machines. To fill in this gap, we introduce the MachinE Word Learning (MEWL) benchmark to assess how machines learn word meaning in grounded visual scenes. MEWL covers human's core cognitive toolkits in word learning: cross-situational reasoning, bootstrapping, and pragmatic learning. Specifically, MEWL is a few-shot benchmark suite consisting of nine tasks for probing various word learning capabilities. These tasks are carefully designed to be aligned with the children's core abilities in word learning and echo the theories in the developmental literature. By evaluating multimodal and unimodal agents' performance with a comparative analysis of human performance, we notice a sharp divergence in human and machine word learning. We further discuss these differences between humans and machines and call for human-like few-shot word learning in machines.

</details>

### Grounding Language Models to Images for Multimodal Inputs and Outputs.
- **链接**: [出版页](https://proceedings.mlr.press/v202/koh23a.html)
- **作者**: Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Calibrating Multimodal Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/ma23i.html)
- **作者**: Huan Ma, Qingyang Zhang, Changqing Zhang, Bingzhe Wu, Huazhu Fu, Joey Tianyi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Robustness in Multimodal Learning under Train-Test Modality Mismatch.
- **链接**: [出版页](https://proceedings.mlr.press/v202/mckinzie23a.html)
- **作者**: Brandon McKinzie, Vaishaal Shankar, Joseph Yitan Cheng, Yinfei Yang, Jonathon Shlens, Alexander T. Toshev
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### π-Tuning: Transferring Multimodal Foundation Models with Optimal Multi-task Interpolation.
- **链接**: [arXiv:2304.14381](https://arxiv.org/abs/2304.14381) · [代码](https://github.com/TencentARC/pi-Tuning)
- **作者**: Chengyue Wu, Teng Wang, Yixiao Ge, Zeyu Lu, Ruisong Zhou, Ying Shan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Foundation models have achieved great advances in multi-task learning with a unified interface of unimodal and multimodal tasks. However, the potential of such multi-task learners has not been exploited during transfer learning. In this work, we present a universal parameter-efficient transfer learning method, termed Predict-Interpolate Tuning ($π$-Tuning), for vision, language, and vision-language tasks. It aggregates the parameters of lightweight task-specific experts learned from similar tasks to aid the target downstream task. The task similarities are predicted in a unified modality-independent space, yielding a scalable graph to demonstrate task relationships. $π$-Tuning has several appealing benefits. First, it flexibly explores both intra- and inter-modal transferability between similar tasks to improve the accuracy and robustness of transfer learning, especially in data-scarce scenarios. Second, it offers a systematical solution for transfer learning with multi-task prediction-and-then-interpolation, compatible with diverse types of parameter-efficient experts, such as prompt and adapter. Third, an extensive study of task-level mutual benefits on 14 unimodal and 6 multimodal datasets shows that $π$-Tuning surpasses fine-tuning and other parameter-efficient transfer learning methods both in full-shot and low-shot regimes. The task graph also enables an in-depth interpretable analysis of task transferability across modalities. The code will be available at https://github.com/TencentARC/pi-Tuning.

</details>

### Retrieval-Augmented Multimodal Language Modeling.
- **链接**: [arXiv:2211.12561](https://arxiv.org/abs/2211.12561)
- **作者**: Michihiro Yasunaga, Armen Aghajanyan, Weijia Shi, Richard James, Jure Leskovec, Percy Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent multimodal models such as DALL-E and CM3 have achieved remarkable progress in text-to-image and image-to-text generation. However, these models store all learned knowledge (e.g., the appearance of the Eiffel Tower) in the model parameters, requiring increasingly larger models and training data to capture more knowledge. To integrate knowledge in a more scalable and modular way, we propose a retrieval-augmented multimodal model, which enables a base multimodal model (generator) to refer to relevant text and images fetched by a retriever from external memory (e.g., documents on the web). Specifically, for the retriever, we use a pretrained CLIP, and for the generator, we train a CM3 Transformer on the LAION dataset. Our resulting model, named Retrieval-Augmented CM3 (RA-CM3), is the first multimodal model that can retrieve and generate both text and images. We show that RA-CM3 significantly outperforms baseline multimodal models such as DALL-E and CM3 on both image and caption generation tasks (12 FID and 17 CIDEr improvements on MS-COCO), while requiring much less compute for training (<30% of DALL-E). Moreover, we show that RA-CM3 exhibits novel capabilities, such as faithful image generation and multimodal in-context learning (e.g., image generation from demonstrations).

</details>

### Improving Medical Predictions by Irregular Multimodal Electronic Health Records Modeling.
- **链接**: [arXiv:2210.12156](https://arxiv.org/abs/2210.12156)
- **作者**: Xinlu Zhang, Shiyang Li, Zhiyu Chen, Xifeng Yan, Linda Ruth Petzold
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Health conditions among patients in intensive care units (ICUs) are monitored via electronic health records (EHRs), composed of numerical time series and lengthy clinical note sequences, both taken at irregular time intervals. Dealing with such irregularity in every modality, and integrating irregularity into multimodal representations to improve medical predictions, is a challenging problem. Our method first addresses irregularity in each single modality by (1) modeling irregular time series by dynamically incorporating hand-crafted imputation embeddings into learned interpolation embeddings via a gating mechanism, and (2) casting a series of clinical note representations as multivariate irregular time series and tackling irregularity via a time attention mechanism. We further integrate irregularity in multimodal fusion with an interleaved attention mechanism across temporal steps. To the best of our knowledge, this is the first work to thoroughly model irregularity in multimodalities for improving medical predictions. Our proposed methods for two medical prediction tasks consistently outperforms state-of-the-art (SOTA) baselines in each single modality and multimodal fusion scenarios. Specifically, we observe relative improvements of 6.5\%, 3.6\%, and 4.3\% in F1 for time series, clinical notes, and multimodal fusion, respectively. These results demonstrate the effectiveness of our methods and the importance of considering irregularity in multimodal EHRs.

</details>

### Provable Dynamic Fusion for Low-Quality Multimodal Data.
- **链接**: [arXiv:2306.02050](https://arxiv.org/abs/2306.02050)
- **作者**: Qingyang Zhang, Haitao Wu, Changqing Zhang, Qinghua Hu, Huazhu Fu, Joey Tianyi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The inherent challenge of multimodal fusion is to precisely capture the cross-modal correlation and flexibly conduct cross-modal interaction. To fully release the value of each modality and mitigate the influence of low-quality multimodal data, dynamic multimodal fusion emerges as a promising learning paradigm. Despite its widespread use, theoretical justifications in this field are still notably lacking. Can we design a provably robust multimodal fusion method? This paper provides theoretical understandings to answer this question under a most popular multimodal fusion framework from the generalization perspective. We proceed to reveal that several uncertainty estimation solutions are naturally available to achieve robust multimodal fusion. Then a novel multimodal fusion framework termed Quality-aware Multimodal Fusion (QMF) is proposed, which can improve the performance in terms of classification accuracy and model robustness. Extensive experimental results on multiple benchmarks can support our findings.

</details>

### On the Generalization of Multi-modal Contrastive Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v202/zhang23an.html)
- **作者**: Qi Zhang, Yifei Wang, Yisen Wang
- **🏷️ 机构**: Peking University
- **会议**: ICML 2023
