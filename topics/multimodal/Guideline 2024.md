# Multimodal — 2024 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark.
- **链接**: [arXiv:2402.04788](https://arxiv.org/abs/2402.04788)
- **作者**: Dongping Chen, Ruoxi Chen, Shilin Zhang, Yaochen Wang, Yinuo Liu, Huichi Zhou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) have gained significant attention recently, showing remarkable potential in artificial general intelligence. However, assessing the utility of MLLMs presents considerable challenges, primarily due to the absence of multimodal benchmarks that align with human preferences. Drawing inspiration from the concept of LLM-as-a-Judge within LLMs, this paper introduces a novel benchmark, termed MLLM-as-a-Judge, to assess the ability of MLLMs in assisting judges across diverse modalities, encompassing three distinct tasks: Scoring Evaluation, Pair Comparison, and Batch Ranking. Our study reveals that, while MLLMs demonstrate remarkable human-like discernment in Pair Comparison, there is a significant divergence from human preferences in Scoring Evaluation and Batch Ranking. Furthermore, a closer examination reveals persistent challenges in the judgment capacities of LLMs, including diverse biases, hallucinatory responses, and inconsistencies in judgment, even in advanced models such as GPT-4V. These findings emphasize the pressing need for enhancements and further research efforts to be undertaken before regarding MLLMs as fully reliable evaluators. In light of this, we advocate for additional efforts dedicated to supporting the continuous development within the domain of MLLM functioning as judges. The code and dataset are publicly available at our project homepage: \url{https://mllm-judge.github.io/}.

</details>

### MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI.
- **链接**: [出版页](https://proceedings.mlr.press/v235/ying24a.html)
- **作者**: Kaining Ying, Fanqing Meng, Jin Wang, Zhiqian Li, Han Lin, Yue Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### A Touch, Vision, and Language Dataset for Multimodal Alignment.
- **链接**: [arXiv:2402.13232](https://arxiv.org/abs/2402.13232)
- **作者**: Letian Fu, Gaurav Datta, Huang Huang, William Chung-Ho Panitch, Jaimyn Drake, Joseph Ortiz et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Touch is an important sensing modality for humans, but it has not yet been incorporated into a multimodal generative language model. This is partially due to the difficulty of obtaining natural language labels for tactile data and the complexity of aligning tactile readings with both visual observations and language descriptions. As a step towards bridging that gap, this work introduces a new dataset of 44K in-the-wild vision-touch pairs, with English language labels annotated by humans (10%) and textual pseudo-labels from GPT-4V (90%). We use this dataset to train a vision-language-aligned tactile encoder for open-vocabulary classification and a touch-vision-language (TVL) model for text generation using the trained encoder. Results suggest that by incorporating touch, the TVL model improves (+29% classification accuracy) touch-vision-language alignment over existing models trained on any pair of those modalities. Although only a small fraction of the dataset is human-labeled, the TVL model demonstrates improved visual-tactile understanding over GPT-4V (+12%) and open-source vision-language models (+32%) on a new touch-vision understanding benchmark. Code and data: https://tactile-vlm.github.io.

</details>

### Machine Vision Therapy: Multimodal Large Language Models Can Enhance Visual Robustness via Denoising In-Context Learning.
- **链接**: [arXiv:2312.02546](https://arxiv.org/abs/2312.02546) · [代码](https://github.com/tmllab/Machine_Vision_Therapy)
- **作者**: Zhuo Huang, Chang Liu, Yinpeng Dong, Hang Su, Shibao Zheng, Tongliang Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although vision models such as Contrastive Language-Image Pre-Training (CLIP) show impressive generalization performance, their zero-shot robustness is still limited under Out-of-Distribution (OOD) scenarios without fine-tuning. Instead of undesirably providing human supervision as commonly done, it is possible to take advantage of Multi-modal Large Language Models (MLLMs) that hold powerful visual understanding abilities. However, MLLMs are shown to struggle with vision problems due to the incompatibility of tasks, thus hindering their utilization. In this paper, we propose to effectively leverage MLLMs to conduct Machine Vision Therapy which aims to rectify the noisy predictions from vision models. By fine-tuning with the denoised labels, the learning model performance can be boosted in an unsupervised manner. To solve the incompatibility issue, we propose a novel Denoising In-Context Learning (DICL) strategy to align vision tasks with MLLMs. Concretely, by estimating a transition matrix that captures the probability of one class being confused with another, an instruction containing a correct exemplar and an erroneous one from the most probable noisy class can be constructed. Such an instruction can help any MLLMs with ICL ability to detect and rectify incorrect predictions of vision models. Through extensive experiments on ImageNet, WILDS, DomainBed, and other OOD datasets, we carefully validate the quantitative and qualitative effectiveness of our method. Our code is available at https://github.com/tmllab/Machine_Vision_Therapy.

</details>

### Revealing Vision-Language Integration in the Brain with Multimodal Networks.
- **链接**: [arXiv:2406.14481](https://arxiv.org/abs/2406.14481)
- **作者**: Vighnesh Subramaniam, Colin Conwell, Christopher Wang, Gabriel Kreiman, Boris Katz, Ignacio Cases et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We use (multi)modal deep neural networks (DNNs) to probe for sites of multimodal integration in the human brain by predicting stereoencephalography (SEEG) recordings taken while human subjects watched movies. We operationalize sites of multimodal integration as regions where a multimodal vision-language model predicts recordings better than unimodal language, unimodal vision, or linearly-integrated language-vision models. Our target DNN models span different architectures (e.g., convolutional networks and transformers) and multimodal training techniques (e.g., cross-attention and contrastive learning). As a key enabling step, we first demonstrate that trained vision and language models systematically outperform their randomly initialized counterparts in their ability to predict SEEG signals. We then compare unimodal and multimodal models against one another. Because our target DNN models often have different architectures, number of parameters, and training sets (possibly obscuring those differences attributable to integration), we carry out a controlled comparison of two models (SLIP and SimCLR), which keep all of these attributes the same aside from input modality. Using this approach, we identify a sizable number of neural sites (on average 141 out of 1090 total sites or 12.94%) and brain regions where multimodal integration seems to occur. Additionally, we find that among the variants of multimodal training techniques we assess, CLIP-style training is the best suited for downstream prediction of the neural activity in these sites.

</details>

### Improving Context Understanding in Multimodal Large Language Models via Multimodal Composition Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24s.html)
- **作者**: Wei Li, Hehe Fan, Yongkang Wong, Yi Yang, Mohan S. Kankanhalli
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### RoboMP2: A Robotic Multimodal Perception-Planning Framework with Multimodal Large Language Models.
- **链接**: [arXiv:2404.04929](https://arxiv.org/abs/2404.04929)
- **作者**: Qi Lv, Hao Li, Xiang Deng, Rui Shao, Michael Yu Wang, Liqiang Nie
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) have shown impressive reasoning abilities and general intelligence in various domains. It inspires researchers to train end-to-end MLLMs or utilize large models to generate policies with human-selected prompts for embodied agents. However, these methods exhibit limited generalization capabilities on unseen tasks or scenarios, and overlook the multimodal environment information which is critical for robots to make decisions. In this paper, we introduce a novel Robotic Multimodal Perception-Planning (RoboMP$^2$) framework for robotic manipulation which consists of a Goal-Conditioned Multimodal Preceptor (GCMP) and a Retrieval-Augmented Multimodal Planner (RAMP). Specially, GCMP captures environment states by employing a tailored MLLMs for embodied agents with the abilities of semantic reasoning and localization. RAMP utilizes coarse-to-fine retrieval method to find the $k$ most-relevant policies as in-context demonstrations to enhance the planner. Extensive experiments demonstrate the superiority of RoboMP$^2$ on both VIMA benchmark and real-world tasks, with around 10% improvement over the baselines.

</details>

### RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis.
- **链接**: [arXiv:2402.16117](https://arxiv.org/abs/2402.16117)
- **作者**: Yao Mu, Junting Chen, Qinglong Zhang, Shoufa Chen, Qiaojun Yu, Chongjian Ge et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Robotic behavior synthesis, the problem of understanding multimodal inputs and generating precise physical control for robots, is an important part of Embodied AI. Despite successes in applying multimodal large language models for high-level understanding, it remains challenging to translate these conceptual understandings into detailed robotic actions while achieving generalization across various scenarios. In this paper, we propose a tree-structured multimodal code generation framework for generalized robotic behavior synthesis, termed RoboCodeX. RoboCodeX decomposes high-level human instructions into multiple object-centric manipulation units consisting of physical preferences such as affordance and safety constraints, and applies code generation to introduce generalization ability across various robotics platforms. To further enhance the capability to map conceptual and perceptual understanding into control commands, a specialized multimodal reasoning dataset is collected for pre-training and an iterative self-updating methodology is introduced for supervised fine-tuning. Extensive experiments demonstrate that RoboCodeX achieves state-of-the-art performance in both simulators and real robots on four different kinds of manipulation tasks and one navigation task.

</details>

### FreeBind: Free Lunch in Unified Multimodal Space via Knowledge Fusion.
- **链接**: [arXiv:2405.04883](https://arxiv.org/abs/2405.04883)
- **作者**: Zehan Wang, Ziang Zhang, Xize Cheng, Rongjie Huang, Luping Liu, Zhenhui Ye et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unified multi-model representation spaces are the foundation of multimodal understanding and generation. However, the billions of model parameters and catastrophic forgetting problems make it challenging to further enhance pre-trained unified spaces. In this work, we propose FreeBind, an idea that treats multimodal representation spaces as basic units, and freely augments pre-trained unified space by integrating knowledge from extra expert spaces via "space bonds". Specifically, we introduce two kinds of basic space bonds: 1) Space Displacement Bond and 2) Space Combination Bond. Based on these basic bonds, we design Complex Sequential & Parallel Bonds to effectively integrate multiple spaces simultaneously. Benefiting from the modularization concept, we further propose a coarse-to-fine customized inference strategy to flexibly adjust the enhanced unified space for different purposes. Experimentally, we bind ImageBind with extra image-text and audio-text expert spaces, resulting in three main variants: ImageBind++, InternVL_IB, and InternVL_IB++. These resulting spaces outperform ImageBind on 5 audio-image-text downstream tasks across 9 datasets. Moreover, via customized inference, it even surpasses the advanced audio-text and image-text expert spaces.

</details>

### SyCoCa: Symmetrizing Contrastive Captioners with Attentive Masking for Multimodal Alignment.
- **链接**: [arXiv:2401.02137](https://arxiv.org/abs/2401.02137)
- **作者**: Ziping Ma, Furong Xu, Jian Liu, Ming Yang, Qingpei Guo
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal alignment between language and vision is the fundamental topic in current vision-language model research. Contrastive Captioners (CoCa), as a representative method, integrates Contrastive Language-Image Pretraining (CLIP) and Image Caption (IC) into a unified framework, resulting in impressive results. CLIP imposes a bidirectional constraints on global representation of entire images and sentences. Although IC conducts an unidirectional image-to-text generation on local representation, it lacks any constraint on local text-to-image reconstruction, which limits the ability to understand images at a fine-grained level when aligned with texts. To achieve multimodal alignment from both global and local perspectives, this paper proposes Symmetrizing Contrastive Captioners (SyCoCa), which introduces bidirectional interactions on images and texts across the global and local representation levels. Specifically, we expand a Text-Guided Masked Image Modeling (TG-MIM) head based on ITC and IC heads. The improved SyCoCa can further leverage textual cues to reconstruct contextual images and visual cues to predict textual contents. When implementing bidirectional local interactions, the local contents of images tend to be cluttered or unrelated to their textual descriptions. Thus, we employ an attentive masking strategy to select effective image patches for interaction. Extensive experiments on five vision-language tasks, including image-text retrieval, image-captioning, visual question answering, and zero-shot/finetuned image classification, validate the effectiveness of our proposed method.

</details>

### Enhancing Storage and Computational Efficiency in Federated Multimodal Learning for Large-Scale Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24az.html)
- **作者**: Zixin Zhang, Fan Qi, Changsheng Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs.
- **链接**: [arXiv:2401.11708](https://arxiv.org/abs/2401.11708) · [代码](https://github.com/YangLing0818/RPG-DiffusionMaster)
- **作者**: Ling Yang, Zhaochen Yu, Chenlin Meng, Minkai Xu, Stefano Ermon, Bin Cui
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models have exhibit exceptional performance in text-to-image generation and editing. However, existing methods often face challenges when handling complex text prompts that involve multiple objects with multiple attributes and relationships. In this paper, we propose a brand new training-free text-to-image generation/editing framework, namely Recaption, Plan and Generate (RPG), harnessing the powerful chain-of-thought reasoning ability of multimodal LLMs to enhance the compositionality of text-to-image diffusion models. Our approach employs the MLLM as a global planner to decompose the process of generating complex images into multiple simpler generation tasks within subregions. We propose complementary regional diffusion to enable region-wise compositional generation. Furthermore, we integrate text-guided image generation and editing within the proposed RPG in a closed-loop fashion, thereby enhancing generalization ability. Extensive experiments demonstrate our RPG outperforms state-of-the-art text-to-image diffusion models, including DALL-E 3 and SDXL, particularly in multi-category object composition and text-image semantic alignment. Notably, our RPG framework exhibits wide compatibility with various MLLM architectures (e.g., MiniGPT-4) and diffusion backbones (e.g., ControlNet). Our code is available at: https://github.com/YangLing0818/RPG-DiffusionMaster

</details>

### Integrating Multimodal Data for Joint Generative Modeling of Complex Dynamics.
- **链接**: [出版页](https://proceedings.mlr.press/v235/brenner24a.html)
- **作者**: Manuel Brenner, Florian Hess, Georgia Koppe, Daniel Durstewitz
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Generative Flows on Discrete State-Spaces: Enabling Multimodal Flows with Applications to Protein Co-Design.
- **链接**: [出版页](https://proceedings.mlr.press/v235/campbell24a.html)
- **作者**: Andrew Campbell, Jason Yim, Regina Barzilay, Tom Rainforth, Tommi S. Jaakkola
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### FedMBridge: Bridgeable Multimodal Federated Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/chen24ba.html)
- **作者**: Jiayi Chen, Aidong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### LLark: A Multimodal Instruction-Following Language Model for Music.
- **链接**: [出版页](https://proceedings.mlr.press/v235/gardner24a.html)
- **作者**: Joshua Patrick Gardner, Simon Durand, Daniel Stoller, Rachel M. Bittner
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast.
- **链接**: [arXiv:2402.08567](https://arxiv.org/abs/2402.08567)
- **作者**: Xiangming Gu, Xiaosen Zheng, Tianyu Pang, Chao Du, Qian Liu, Ye Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A multimodal large language model (MLLM) agent can receive instructions, capture images, retrieve histories from memory, and decide which tools to use. Nonetheless, red-teaming efforts have revealed that adversarial images/prompts can jailbreak an MLLM and cause unaligned behaviors. In this work, we report an even more severe safety issue in multi-agent environments, referred to as infectious jailbreak. It entails the adversary simply jailbreaking a single agent, and without any further intervention from the adversary, (almost) all agents will become infected exponentially fast and exhibit harmful behaviors. To validate the feasibility of infectious jailbreak, we simulate multi-agent environments containing up to one million LLaVA-1.5 agents, and employ randomized pair-wise chat as a proof-of-concept instantiation for multi-agent interaction. Our results show that feeding an (infectious) adversarial image into the memory of any randomly chosen agent is sufficient to achieve infectious jailbreak. Finally, we derive a simple principle for determining whether a defense mechanism can provably restrain the spread of infectious jailbreak, but how to design a practical defense that meets this principle remains an open question to investigate. Our project page is available at https://sail-sg.github.io/Agent-Smith/.

</details>

### GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer.
- **链接**: [arXiv:2406.01210](https://arxiv.org/abs/2406.01210) · [代码](https://github.com/JiaDingCN/GeminiFusion)
- **作者**: Ding Jia, Jianyuan Guo, Kai Han, Han Wu, Chao Zhang, Chang Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-modal transformers have demonstrated superiority in various vision tasks by effectively integrating different modalities. This paper first critiques prior token exchange methods which replace less informative tokens with inter-modal features, and demonstrate exchange based methods underperform cross-attention mechanisms, while the computational demand of the latter inevitably restricts its use with longer sequences. To surmount the computational challenges, we propose GeminiFusion, a pixel-wise fusion approach that capitalizes on aligned cross-modal representations. GeminiFusion elegantly combines intra-modal and inter-modal attentions, dynamically integrating complementary information across modalities. We employ a layer-adaptive noise to adaptively control their interplay on a per-layer basis, thereby achieving a harmonized fusion process. Notably, GeminiFusion maintains linear complexity with respect to the number of input tokens, ensuring this multimodal framework operates with efficiency comparable to unimodal networks. Comprehensive evaluations across multimodal image-to-image translation, 3D object detection and arbitrary-modal semantic segmentation tasks, including RGB, depth, LiDAR, event data, etc. demonstrate the superior performance of our GeminiFusion against leading-edge techniques. The PyTorch code is available at https://github.com/JiaDingCN/GeminiFusion

</details>

### On Stronger Computational Separations Between Multimodal and Unimodal Machine Learning.
- **链接**: [arXiv:2404.02254](https://arxiv.org/abs/2404.02254)
- **作者**: Ari Karchmer
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, multimodal machine learning has enjoyed huge empirical success (e.g. GPT-4). Motivated to develop theoretical justification for this empirical success, Lu (NeurIPS '23, ALT '24) introduces a theory of multimodal learning, and considers possible \textit{separations} between theoretical models of multimodal and unimodal learning. In particular, Lu (ALT '24) shows a computational separation, which is relevant to \textit{worst-case} instances of the learning task. In this paper, we give a stronger \textit{average-case} computational separation, where for ``typical'' instances of the learning task, unimodal learning is computationally hard, but multimodal learning is easy. We then question how ``natural'' the average-case separation is. Would it be encountered in practice? To this end, we prove that under basic conditions, any given computational separation between average-case unimodal and multimodal learning tasks implies a corresponding cryptographic key agreement protocol. We suggest to interpret this as evidence that very strong \textit{computational} advantages of multimodal learning may arise \textit{infrequently} in practice, since they exist only for the ``pathological'' case of inherently cryptographic distributions. However, this does not apply to possible (super-polynomial) \textit{statistical} advantages.

</details>

### Mastering Robot Manipulation with Multimodal Prompts through Pretraining and Multi-task Fine-tuning.
- **链接**: [arXiv:2310.09676](https://arxiv.org/abs/2310.09676)
- **作者**: Jiachen Li, Qiaozi Gao, Michael Johnston, Xiaofeng Gao, Xuehai He, Hangjie Shi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt-based learning has been demonstrated as a compelling paradigm contributing to large language models' tremendous success (LLMs). Inspired by their success in language tasks, existing research has leveraged LLMs in embodied instruction following and task planning. In this work, we tackle the problem of training a robot to understand multimodal prompts, interleaving vision signals with text descriptions. This type of task poses a major challenge to robots' capability to understand the interconnection and complementarity between vision and language signals. In this work, we introduce an effective framework that learns a policy to perform robot manipulation with multimodal prompts from multi-task expert trajectories. Our methods consist of a two-stage training pipeline that performs inverse dynamics pretraining and multi-task finetuning. To facilitate multimodal understanding, we design our multimodal prompt encoder by augmenting a pretrained LM with a residual connection to the visual input and model the dependencies among action dimensions. Empirically, we evaluate the efficacy of our method on the VIMA-BENCH and establish a new state-of-the-art (10% improvement in success rate). Moreover, we demonstrate that our model exhibits remarkable in-context learning ability. Project page: \url{https://midas-icml.github.io/}.

</details>

### VisionGraph: Leveraging Large Multimodal Models for Graph Theory Problems in Visual Context.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24ab.html)
- **作者**: Yunxin Li, Baotian Hu, Haoyuan Shi, Wei Wang, Longyue Wang, Min Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### DecisionNCE: Embodied Multimodal Representations via Implicit Preference Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24cr.html)
- **作者**: Jianxiong Li, Jinliang Zheng, Yinan Zheng, Liyuan Mao, Xiao Hu, Sijie Cheng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement.
- **链接**: [arXiv:2403.06659](https://arxiv.org/abs/2403.06659) · [代码](https://github.com/cheliu-computation/MERL)
- **作者**: Che Liu, Zhongwei Wan, Cheng Ouyang, Anand Shah, Wenjia Bai, Rossella Arcucci
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Electrocardiograms (ECGs) are non-invasive diagnostic tools crucial for detecting cardiac arrhythmic diseases in clinical practice. While ECG Self-supervised Learning (eSSL) methods show promise in representation learning from unannotated ECG data, they often overlook the clinical knowledge that can be found in reports. This oversight and the requirement for annotated samples for downstream tasks limit eSSL's versatility. In this work, we address these issues with the Multimodal ECG Representation Learning (MERL}) framework. Through multimodal learning on ECG records and associated reports, MERL is capable of performing zero-shot ECG classification with text prompts, eliminating the need for training data in downstream tasks. At test time, we propose the Clinical Knowledge Enhanced Prompt Engineering (CKEPE) approach, which uses Large Language Models (LLMs) to exploit external expert-verified clinical knowledge databases, generating more descriptive prompts and reducing hallucinations in LLM-generated content to boost zero-shot classification. Based on MERL, we perform the first benchmark across six public ECG datasets, showing the superior performance of MERL compared against eSSL methods. Notably, MERL achieves an average AUC score of 75.2% in zero-shot classification (without training data), 3.2% higher than linear probed eSSL methods with 10\% annotated training data, averaged across all six datasets. Code and models are available at https://github.com/cheliu-computation/MERL

</details>

### Auto-Encoding Morph-Tokens for Multimodal LLM.
- **链接**: [arXiv:2405.01926](https://arxiv.org/abs/2405.01926) · [代码](https://github.com/DCDmllm/MorphTokens)
- **作者**: Kaihang Pan, Siliang Tang, Juncheng Li, Zhaoyu Fan, Wei Chow, Shuicheng Yan et al.
- **🏷️ 机构**: NUS
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> For multimodal LLMs, the synergy of visual comprehension (textual output) and generation (visual output) presents an ongoing challenge. This is due to a conflicting objective: for comprehension, an MLLM needs to abstract the visuals; for generation, it needs to preserve the visuals as much as possible. Thus, the objective is a dilemma for visual-tokens. To resolve the conflict, we propose encoding images into morph-tokens to serve a dual purpose: for comprehension, they act as visual prompts instructing MLLM to generate texts; for generation, they take on a different, non-conflicting role as complete visual-tokens for image reconstruction, where the missing visual cues are recovered by the MLLM. Extensive experiments show that morph-tokens can achieve a new SOTA for multimodal comprehension and generation simultaneously. Our project is available at https://github.com/DCDmllm/MorphTokens.

</details>

### A Multimodal Automated Interpretability Agent.
- **链接**: [arXiv:2404.14394](https://arxiv.org/abs/2404.14394)
- **作者**: Tamar Rott Shaham, Sarah Schwettmann, Franklin Wang, Achyuta Rajaram, Evan Hernandez, Jacob Andreas et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper describes MAIA, a Multimodal Automated Interpretability Agent. MAIA is a system that uses neural models to automate neural model understanding tasks like feature interpretation and failure mode discovery. It equips a pre-trained vision-language model with a set of tools that support iterative experimentation on subcomponents of other models to explain their behavior. These include tools commonly used by human interpretability researchers: for synthesizing and editing inputs, computing maximally activating exemplars from real-world datasets, and summarizing and describing experimental results. Interpretability experiments proposed by MAIA compose these tools to describe and explain system behavior. We evaluate applications of MAIA to computer vision models. We first characterize MAIA's ability to describe (neuron-level) features in learned representations of images. Across several trained models and a novel dataset of synthetic vision neurons with paired ground-truth descriptions, MAIA produces descriptions comparable to those generated by expert human experimenters. We then show that MAIA can aid in two additional interpretability tasks: reducing sensitivity to spurious features, and automatically identifying inputs likely to be mis-classified.

</details>

### Multimodal Prototyping for cancer survival prediction.
- **链接**: [arXiv:2407.00224](https://arxiv.org/abs/2407.00224)
- **作者**: Andrew H. Song, Richard J. Chen, Guillaume Jaume, Anurag J. Vaidya, Alexander S. Baras, Faisal Mahmood
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal survival methods combining gigapixel histology whole-slide images (WSIs) and transcriptomic profiles are particularly promising for patient prognostication and stratification. Current approaches involve tokenizing the WSIs into smaller patches (>10,000 patches) and transcriptomics into gene groups, which are then integrated using a Transformer for predicting outcomes. However, this process generates many tokens, which leads to high memory requirements for computing attention and complicates post-hoc interpretability analyses. Instead, we hypothesize that we can: (1) effectively summarize the morphological content of a WSI by condensing its constituting tokens using morphological prototypes, achieving more than 300x compression; and (2) accurately characterize cellular functions by encoding the transcriptomic profile with biological pathway prototypes, all in an unsupervised fashion. The resulting multimodal tokens are then processed by a fusion network, either with a Transformer or an optimal transport cross-alignment, which now operates with a small and fixed number of tokens without approximations. Extensive evaluation on six cancer types shows that our framework outperforms state-of-the-art methods with much less computation while unlocking new interpretability analyses.

</details>

### ConTextual: Evaluating Context-Sensitive Text-Rich Visual Reasoning in Large Multimodal Models.
- **链接**: [arXiv:2401.13311](https://arxiv.org/abs/2401.13311)
- **作者**: Rohan Wadhawan, Hritik Bansal, Kai-Wei Chang, Nanyun Peng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many real-world tasks require an agent to reason jointly over text and visual objects, (e.g., navigating in public spaces), which we refer to as context-sensitive text-rich visual reasoning. Specifically, these tasks require an understanding of the context in which the text interacts with visual elements within an image. However, there is a lack of existing datasets to benchmark the state-of-the-art multimodal models' capability on context-sensitive text-rich visual reasoning. In this paper, we introduce ConTextual, a novel dataset featuring human-crafted instructions that require context-sensitive reasoning for text-rich images. We conduct experiments to assess the performance of 14 foundation models (GPT-4V, Gemini-Pro-Vision, LLaVA-Next) and establish a human performance baseline. Further, we perform human evaluations of the model responses and observe a significant performance gap of 30.8% between GPT-4V (the current best-performing Large Multimodal Model) and human performance. Our fine-grained analysis reveals that GPT-4V encounters difficulties interpreting time-related data and infographics. However, it demonstrates proficiency in comprehending abstract visual contexts such as memes and quotes. Finally, our qualitative analysis uncovers various factors contributing to poor performance including lack of precise visual perception and hallucinations. Our dataset, code, and leaderboard can be found on the project page https://con-textual.github.io/

</details>

### MMPareto: Boosting Multimodal Learning with Innocent Unimodal Assistance.
- **链接**: [arXiv:2405.17730](https://arxiv.org/abs/2405.17730) · [代码](https://github.com/GeWu-Lab/MMPareto_ICML2024)
- **作者**: Yake Wei, Di Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning methods with targeted unimodal learning objectives have exhibited their superior efficacy in alleviating the imbalanced multimodal learning problem. However, in this paper, we identify the previously ignored gradient conflict between multimodal and unimodal learning objectives, potentially misleading the unimodal encoder optimization. To well diminish these conflicts, we observe the discrepancy between multimodal loss and unimodal loss, where both gradient magnitude and covariance of the easier-to-learn multimodal loss are smaller than the unimodal one. With this property, we analyze Pareto integration under our multimodal scenario and propose MMPareto algorithm, which could ensure a final gradient with direction that is common to all learning objectives and enhanced magnitude to improve generalization, providing innocent unimodal assistance. Finally, experiments across multiple types of modalities and frameworks with dense cross-modal interaction indicate our superior and extendable method performance. Our method is also expected to facilitate multi-task cases with a clear discrepancy in task difficulty, demonstrating its ideal scalability. The source code and dataset are available at https://github.com/GeWu-Lab/MMPareto_ICML2024.

</details>

### NExT-GPT: Any-to-Any Multimodal LLM.
- **链接**: [arXiv:2309.05519](https://arxiv.org/abs/2309.05519)
- **作者**: Shengqiong Wu, Hao Fei, Leigang Qu, Wei Ji, Tat-Seng Chua
- **🏷️ 机构**: NUS
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While recently Multimodal Large Language Models (MM-LLMs) have made exciting strides, they mostly fall prey to the limitation of only input-side multimodal understanding, without the ability to produce content in multiple modalities. As we humans always perceive the world and communicate with people through various modalities, developing any-to-any MM-LLMs capable of accepting and delivering content in any modality becomes essential to human-level AI. To fill the gap, we present an end-to-end general-purpose any-to-any MM-LLM system, NExT-GPT. We connect an LLM with multimodal adaptors and different diffusion decoders, enabling NExT-GPT to perceive inputs and generate outputs in arbitrary combinations of text, images, videos, and audio. By leveraging the existing well-trained highly-performing encoders and decoders, NExT-GPT is tuned with only a small amount of parameter (1%) of certain projection layers, which not only benefits low-cost training and also facilitates convenient expansion to more potential modalities. Moreover, we introduce a modality-switching instruction tuning (MosIT) and manually curate a high-quality dataset for MosIT, based on which NExT-GPT is empowered with complex cross-modal semantic understanding and content generation. Overall, our research showcases the promising possibility of building an AI agent capable of modeling universal modalities, paving the way for more human-like AI research in the community. Project page: https://next-gpt.github.io/

</details>

### Low-Rank Similarity Mining for Multimodal Dataset Distillation.
- **链接**: [arXiv:2406.03793](https://arxiv.org/abs/2406.03793) · [代码](https://github.com/silicx/LoRS_Distill)
- **作者**: Yue Xu, Zhilin Lin, Yusong Qiu, Cewu Lu, Yong-Lu Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Though dataset distillation has witnessed rapid development in recent years, the distillation of multimodal data, e.g., image-text pairs, poses unique and under-explored challenges. Unlike unimodal data, image-text contrastive learning (ITC) data lack inherent categorization and should instead place greater emphasis on modality correspondence. In this work, we propose Low-Rank Similarity Mining (LoRS) for multimodal dataset distillation, that concurrently distills a ground truth similarity matrix with image-text pairs, and leverages low-rank factorization for efficiency and scalability. The proposed approach brings significant improvement to the existing algorithms, marking a significant contribution to the field of visual-language dataset distillation. We advocate adopting LoRS as a foundational synthetic data setup for image-text dataset distillation. Our code is available at https://github.com/silicx/LoRS_Distill.

</details>

### Unlocking the Power of Spatial and Temporal Information in Medical Multimodal Pre-training.
- **链接**: [arXiv:2405.19654](https://arxiv.org/abs/2405.19654) · [代码](https://github.com/SVT-Yang/MedST)
- **作者**: Jinxia Yang, Bing Su, Xin Zhao, Ji-Rong Wen
- **🏷️ 机构**: Renmin University
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Medical vision-language pre-training methods mainly leverage the correspondence between paired medical images and radiological reports. Although multi-view spatial images and temporal sequences of image-report pairs are available in off-the-shelf multi-modal medical datasets, most existing methods have not thoroughly tapped into such extensive supervision signals. In this paper, we introduce the Med-ST framework for fine-grained spatial and temporal modeling to exploit information from multiple spatial views of chest radiographs and temporal historical records. For spatial modeling, Med-ST employs the Mixture of View Expert (MoVE) architecture to integrate different visual features from both frontal and lateral views. To achieve a more comprehensive alignment, Med-ST not only establishes the global alignment between whole images and texts but also introduces modality-weighted local alignment between text tokens and spatial regions of images. For temporal modeling, we propose a novel cross-modal bidirectional cycle consistency objective by forward mapping classification (FMC) and reverse mapping regression (RMR). By perceiving temporal information from simple to complex, Med-ST can learn temporal semantics. Experimental results across four distinct tasks demonstrate the effectiveness of Med-ST, especially in temporal classification tasks. Our code and model are available at https://github.com/SVT-Yang/MedST.

</details>

### MM-Vet: Evaluating Large Multimodal Models for Integrated Capabilities.
- **链接**: [arXiv:2308.02490](https://arxiv.org/abs/2308.02490)
- **作者**: Weihao Yu, Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Zicheng Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose MM-Vet, an evaluation benchmark that examines large multimodal models (LMMs) on complicated multimodal tasks. Recent LMMs have shown various intriguing abilities, such as solving math problems written on the blackboard, reasoning about events and celebrities in news images, and explaining visual jokes. Rapid model advancements pose challenges to evaluation benchmark development. Problems include: (1) How to systematically structure and evaluate the complicated multimodal tasks; (2) How to design evaluation metrics that work well across question and answer types; and (3) How to give model insights beyond a simple performance ranking. To this end, we present MM-Vet, designed based on the insight that the intriguing ability to solve complicated tasks is often achieved by a generalist model being able to integrate different core vision-language (VL) capabilities. MM-Vet defines 6 core VL capabilities and examines the 16 integrations of interest derived from the capability combination. For evaluation metrics, we propose an LLM-based evaluator for open-ended outputs. The evaluator enables the evaluation across different question types and answer styles, resulting in a unified scoring metric. We evaluate representative LMMs on MM-Vet, providing insights into the capabilities of different LMM system paradigms and models.

</details>

### Sparse-to-dense Multimodal Image Registration via Multi-Task Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24ar.html)
- **作者**: Kaining Zhang, Jiayi Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Understanding Unimodal Bias in Multimodal Deep Linear Networks.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24aa.html)
- **作者**: Yedi Zhang, Peter E. Latham, Andrew M. Saxe
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### EquiAV: Leveraging Equivariance for Audio-Visual Contrastive Learning.
- **链接**: [arXiv:2403.09502](https://arxiv.org/abs/2403.09502) · [代码](https://github.com/JongSuk1/EquiAV)
- **作者**: Jongsuk Kim, Hyeongkeun Lee, Kyeongha Rho, Junmo Kim, Joon Son Chung
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in self-supervised audio-visual representation learning have demonstrated its potential to capture rich and comprehensive representations. However, despite the advantages of data augmentation verified in many learning methods, audio-visual learning has struggled to fully harness these benefits, as augmentations can easily disrupt the correspondence between input pairs. To address this limitation, we introduce EquiAV, a novel framework that leverages equivariance for audio-visual contrastive learning. Our approach begins with extending equivariance to audio-visual learning, facilitated by a shared attention-based transformation predictor. It enables the aggregation of features from diverse augmentations into a representative embedding, providing robust supervision. Notably, this is achieved with minimal computational overhead. Extensive ablation studies and qualitative results verify the effectiveness of our method. EquiAV outperforms previous works across various audio-visual benchmarks. The code is available on https://github.com/JongSuk1/EquiAV.

</details>
