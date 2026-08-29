# VLM — 2024 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 28 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Bridging Environments and Language with Rendering Functions and Vision-Language Models.
- **链接**: [arXiv:2409.16024](https://arxiv.org/abs/2409.16024)
- **作者**: Théo Cachet, Christopher R. Dance, Olivier Sigaud
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have tremendous potential for grounding language, and thus enabling language-conditioned agents (LCAs) to perform diverse tasks specified with text. This has motivated the study of LCAs based on reinforcement learning (RL) with rewards given by rendering images of an environment and evaluating those images with VLMs. If single-task RL is employed, such approaches are limited by the cost and time required to train a policy for each new task. Multi-task RL (MTRL) is a natural alternative, but requires a carefully designed corpus of training tasks and does not always generalize reliably to new tasks. Therefore, this paper introduces a novel decomposition of the problem of building an LCA: first find an environment configuration that has a high VLM score for text describing a task; then use a (pretrained) goal-conditioned policy to reach that configuration. We also explore several enhancements to the speed and quality of VLM-based LCAs, notably, the use of distilled models, and the evaluation of configurations from multiple viewpoints to resolve the ambiguities inherent in a single 2D view. We demonstrate our approach on the Humanoid environment, showing that it results in LCAs that outperform MTRL baselines in zero-shot generalization, without requiring any textual task descriptions or other forms of environment-specific annotation during training. Videos and an interactive demo can be found at https://europe.naverlabs.com/text2control

</details>

### Revisiting the Role of Language Priors in Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/lin24c.html)
- **作者**: Zhiqiu Lin, Xinyue Chen, Deepak Pathak, Pengchuan Zhang, Deva Ramanan
- **🏷️ 机构**: CMU
- **会议**: ICML 2024

### Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models.
- **链接**: [arXiv:2402.12336](https://arxiv.org/abs/2402.12336) · [代码](https://github.com/chs20/RobustVLM)
- **作者**: Christian Schlarmann, Naman Deep Singh, Francesco Croce, Matthias Hein
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal foundation models like OpenFlamingo, LLaVA, and GPT-4 are increasingly used for various real-world tasks. Prior work has shown that these models are highly vulnerable to adversarial attacks on the vision modality. These attacks can be leveraged to spread fake information or defraud users, and thus pose a significant risk, which makes the robustness of large multi-modal foundation models a pressing problem. The CLIP model, or one of its variants, is used as a frozen vision encoder in many large vision-language models (LVLMs), e.g. LLaVA and OpenFlamingo. We propose an unsupervised adversarial fine-tuning scheme to obtain a robust CLIP vision encoder, which yields robustness on all vision down-stream tasks (LVLMs, zero-shot classification) that rely on CLIP. In particular, we show that stealth-attacks on users of LVLMs by a malicious third party providing manipulated images are no longer possible once one replaces the original CLIP model with our robust one. No retraining or fine-tuning of the down-stream LVLMs is required. The code and robust models are available at https://github.com/chs20/RobustVLM

</details>

### Visual-Text Cross Alignment: Refining the Similarity Score in Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24ag.html)
- **作者**: Jinhao Li, Haopeng Li, Sarah Monazam Erfani, Lei Feng, James Bailey, Feng Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Amend to Alignment: Decoupled Prompt Tuning for Mitigating Spurious Correlation in Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/zhang24as.html)
- **作者**: Jie Zhang, Xiaosong Ma, Song Guo, Peng Li, Wenchao Xu, Xueyang Tang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Modeling Caption Diversity in Contrastive Vision-Language Pretraining.
- **链接**: [arXiv:2405.00740](https://arxiv.org/abs/2405.00740)
- **作者**: Samuel Lavoie, Polina Kirichenko, Mark Ibrahim, Mido Assran, Andrew Gordon Wilson, Aaron C. Courville et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> There are a thousand ways to caption an image. Contrastive Language Pretraining (CLIP) on the other hand, works by mapping an image and its caption to a single vector -- limiting how well CLIP-like models can represent the diverse ways to describe an image. In this work, we introduce Llip, Latent Language Image Pretraining, which models the diversity of captions that could match an image. Llip's vision encoder outputs a set of visual features that are mixed into a final representation by conditioning on information derived from the text. We show that Llip outperforms non-contextualized baselines like CLIP and SigLIP on a variety of tasks even with large-scale encoders. Llip improves zero-shot classification by an average of 2.9% zero-shot classification benchmarks with a ViT-G/14 encoder. Specifically, Llip attains a zero-shot top-1 accuracy of 83.5% on ImageNet outperforming a similarly sized CLIP by 1.4%. We also demonstrate improvement on zero-shot retrieval on MS-COCO by 6.0%. We provide a comprehensive analysis of the components introduced by the method and demonstrate that Llip leads to richer visual representations.

</details>

### GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model.
- **链接**: [arXiv:2406.18572](https://arxiv.org/abs/2406.18572) · [代码](https://github.com/lingli1996/GeoReasoner)
- **作者**: Ling Li, Yu Ye, Bingchuan Jiang, Wei Zeng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work tackles the problem of geo-localization with a new paradigm using a large vision-language model (LVLM) augmented with human inference knowledge. A primary challenge here is the scarcity of data for training the LVLM - existing street-view datasets often contain numerous low-quality images lacking visual clues, and lack any reasoning inference. To address the data-quality issue, we devise a CLIP-based network to quantify the degree of street-view images being locatable, leading to the creation of a new dataset comprising highly locatable street views. To enhance reasoning inference, we integrate external knowledge obtained from real geo-localization games, tapping into valuable human inference capabilities. The data are utilized to train GeoReasoner, which undergoes fine-tuning through dedicated reasoning and location-tuning stages. Qualitative and quantitative evaluations illustrate that GeoReasoner outperforms counterpart LVLMs by more than 25% at country-level and 38% at city-level geo-localization tasks, and surpasses StreetCLIP performance while requiring fewer training resources. The data and code are available at https://github.com/lingli1996/GeoReasoner.

</details>

### Cascade-CLIP: Cascaded Vision-Language Embeddings Alignment for Zero-Shot Semantic Segmentation.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24aq.html)
- **作者**: Yunheng Li, Zhong-Yu Li, Quan-Sheng Zeng, Qibin Hou, Ming-Ming Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Beyond Sole Strength: Customized Ensembles for Generalized Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/lu24a.html)
- **作者**: Zhihe Lu, Jiawang Bai, Xin Li, Zeyu Xiao, Xinchao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Understanding Retrieval-Augmented Task Adaptation for Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/ming24a.html)
- **作者**: Yifei Ming, Yixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### An Empirical Study Into What Matters for Calibrating Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/tu24a.html)
- **作者**: Weijie Tu, Weijian Deng, Dylan Campbell, Stephen Gould, Tom Gedeon
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Diagnosing the Compositional Knowledge of Vision Language Models from a Game-Theoretic View.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wang24n.html)
- **作者**: Jin Wang, Shichao Dong, Yapeng Zhu, Kelu Yao, Weidong Zhao, Chao Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Connecting the Dots: Collaborative Fine-tuning for Black-Box Vision-Language Models.
- **链接**: [arXiv:2402.04050](https://arxiv.org/abs/2402.04050) · [代码](https://github.com/mrflogs/CraFT)
- **作者**: Zhengbo Wang, Jian Liang, Ran He, Zilei Wang, Tieniu Tan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the emergence of pretrained vision-language models (VLMs), considerable efforts have been devoted to fine-tuning them for downstream tasks. Despite the progress made in designing efficient fine-tuning methods, such methods require access to the model's parameters, which can be challenging as model owners often opt to provide their models as a black box to safeguard model ownership. This paper proposes a \textbf{C}ollabo\textbf{ra}tive \textbf{F}ine-\textbf{T}uning (\textbf{CraFT}) approach for fine-tuning black-box VLMs to downstream tasks, where one only has access to the input prompts and the output predictions of the model. CraFT comprises two modules, a prompt generation module for learning text prompts and a prediction refinement module for enhancing output predictions in residual style. Additionally, we introduce an auxiliary prediction-consistent loss to promote consistent optimization across these modules. These modules are optimized by a novel collaborative training algorithm. Extensive experiments on few-shot classification over 15 datasets demonstrate the superiority of CraFT. The results show that CraFT achieves a decent gain of about 12\% with 16-shot datasets and only 8,000 queries. Moreover, CraFT trains faster and uses only about 1/80 of the memory footprint for deployment, while sacrificing only 1.62\% compared to the white-box method. Our code is publicly available at https://github.com/mrflogs/CraFT .

</details>

### RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback.
- **链接**: [arXiv:2402.03681](https://arxiv.org/abs/2402.03681)
- **作者**: Yufei Wang, Zhanyi Sun, Jesse Zhang, Zhou Xian, Erdem Biyik, David Held et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reward engineering has long been a challenge in Reinforcement Learning (RL) research, as it often requires extensive human effort and iterative processes of trial-and-error to design effective reward functions. In this paper, we propose RL-VLM-F, a method that automatically generates reward functions for agents to learn new tasks, using only a text description of the task goal and the agent's visual observations, by leveraging feedbacks from vision language foundation models (VLMs). The key to our approach is to query these models to give preferences over pairs of the agent's image observations based on the text description of the task goal, and then learn a reward function from the preference labels, rather than directly prompting these models to output a raw reward score, which can be noisy and inconsistent. We demonstrate that RL-VLM-F successfully produces effective rewards and policies across various domains - including classic control, as well as manipulation of rigid, articulated, and deformable objects - without the need for human supervision, outperforming prior methods that use large pretrained models for reward generation under the same assumptions. Videos can be found on our project website: https://rlvlmf2024.github.io/

</details>

### Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v235/wu24l.html) · 📚 被引 0
- **作者**: Mingrui Wu, Jiayi Ji, Oucheng Huang, Jiale Li, Yuhang Wu, Xiaoshuai Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Candidate Pseudolabel Learning: Enhancing Vision-Language Models by Prompt Tuning with Unlabeled Data.
- **链接**: [arXiv:2406.10502](https://arxiv.org/abs/2406.10502) · [代码](https://github.com/vanillaer/CPL-ICML2024)
- **作者**: Jiahan Zhang, Qi Wei, Feng Liu, Lei Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-tuning vision-language models (VLMs) with abundant unlabeled data recently has attracted increasing attention. Existing methods that resort to the pseudolabeling strategy would suffer from heavily incorrect hard pseudolabels when VLMs exhibit low zero-shot performance in downstream tasks. To alleviate this issue, we propose a Candidate Pseudolabel Learning method, termed CPL, to fine-tune VLMs with suitable candidate pseudolabels of unlabeled data in downstream tasks. The core of our method lies in the generation strategy of candidate pseudolabels, which progressively generates refined candidate pseudolabels by both intra- and inter-instance label selection, based on a confidence score matrix for all unlabeled data. This strategy can result in better performance in true label inclusion and class-balanced instance selection. In this way, we can directly apply existing loss functions to learn with generated candidate psueudolabels. Extensive experiments on nine benchmark datasets with three learning paradigms demonstrate the effectiveness of our method. Our code can be found at https://github.com/vanillaer/CPL-ICML2024.

</details>

### Image Fusion via Vision-Language Model.
- **链接**: [arXiv:2402.02235](https://arxiv.org/abs/2402.02235) · [代码](https://github.com/Zhaozixiang1228/IF-FILM)
- **作者**: Zixiang Zhao, Lilun Deng, Haowen Bai, Yukun Cui, Zhipeng Zhang, Yulun Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image fusion integrates essential information from multiple images into a single composite, enhancing structures, textures, and refining imperfections. Existing methods predominantly focus on pixel-level and semantic visual features for recognition, but often overlook the deeper text-level semantic information beyond vision. Therefore, we introduce a novel fusion paradigm named image Fusion via vIsion-Language Model (FILM), for the first time, utilizing explicit textual information from source images to guide the fusion process. Specifically, FILM generates semantic prompts from images and inputs them into ChatGPT for comprehensive textual descriptions. These descriptions are fused within the textual domain and guide the visual information fusion, enhancing feature extraction and contextual understanding, directed by textual semantic information via cross-attention. FILM has shown promising results in four image fusion tasks: infrared-visible, medical, multi-exposure, and multi-focus image fusion. We also propose a vision-language dataset containing ChatGPT-generated paragraph descriptions for the eight image fusion datasets across four fusion tasks, facilitating future research in vision-language model-based image fusion. Code and dataset are available at https://github.com/Zhaozixiang1228/IF-FILM.

</details>

## 跨领域论文（完整笔记在其他领域）

- MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark. → [multimodal](../multimodal/Guideline%202024.md)
- MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI. → [multimodal](../multimodal/Guideline%202024.md)
- Open-Vocabulary Calibration for Fine-tuned CLIP. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Machine Vision Therapy: Multimodal Large Language Models Can Enhance Visual Robustness via Denoising In-Context Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Exploring Intrinsic Dimension for Vision-Language Model Pruning. → [network-pruning](../network-pruning/Guideline%202024.md)
- Improving Context Understanding in Multimodal Large Language Models via Multimodal Composition Learning. → [multimodal](../multimodal/Guideline%202024.md)
- RoboMP2: A Robotic Multimodal Perception-Planning Framework with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast. → [multimodal](../multimodal/Guideline%202024.md)
- Auto-Encoding Morph-Tokens for Multimodal LLM. → [multimodal](../multimodal/Guideline%202024.md)
- NExT-GPT: Any-to-Any Multimodal LLM. → [multimodal](../multimodal/Guideline%202024.md)
