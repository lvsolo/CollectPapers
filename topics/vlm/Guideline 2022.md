# VLM — 2022 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### VLMo: Unified Vision-Language Pre-Training with Mixture-of-Modality-Experts.
- **链接**: [arXiv:2111.02358](https://arxiv.org/abs/2111.02358) · [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/d46662aa53e78a62afd980a29e0c37ed-Abstract-Conference.html) · 📚 778 citations
- **作者**: Hangbo Bao, Wenhui Wang, Li Dong, Qiang Liu, Owais Khan Mohammed, Kriti Aggarwal et al.
- **🏷️ 机构**: Harbin Institute of Technology, Microsoft Research
- **会议**: NeurIPS 2022

- **摘要（英，原文）**:

  > We present a unified Vision-Language pretrained Model (VLMo) that jointly learns a dual encoder and a fusion encoder with a modular Transformer network. Specifically, we introduce Mixture-of-Modality-Experts (MoME) Transformer, where each block contains a pool of modality-specific experts and a shared self-attention layer. Because of the modeling flexibility of MoME, pretrained VLMo can be fine-tuned as a fusion encoder for vision-language classification tasks, or used as a dual encoder for efficient image-text retrieval. Moreover, we propose a stagewise pre-training strategy, which effectively leverages large-scale image-only and text-only data besides image-text pairs. Experimental results show that VLMo achieves state-of-the-art results on various vision-language tasks, including VQA, NLVR2 and image-text retrieval. The code and pretrained models are available at https://aka.ms/vlmo.

### PyramidCLIP: Hierarchical Feature Alignment for Vision-language Model Pretraining.
- **链接**: [arXiv:2204.14095](https://arxiv.org/abs/2204.14095) · [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/e9882f7f7c44a10acc01132302bac9d8-Abstract-Conference.html) · 📚 163 citations
- **作者**: Yuting Gao, Jinfeng Liu, Zihan Xu, Jun Zhang, Ke Li, Rongrong Ji et al.
- **🏷️ 机构**: ZJU
- **会议**: NeurIPS 2022

- **摘要（英，原文）**:

  > Large-scale vision-language pre-training has achieved promising results on downstream tasks. Existing methods highly rely on the assumption that the image-text pairs crawled from the Internet are in perfect one-to-one correspondence. However, in real scenarios, this assumption can be difficult to hold: the text description, obtained by crawling the affiliated metadata of the image, often suffers from the semantic mismatch and the mutual compatibility. To address these issues, we introduce PyramidCLIP, which constructs an input pyramid with different semantic levels for each modality, and aligns visual elements and linguistic elements in the form of hierarchy via peer-level semantics alignment and cross-level relation alignment. Furthermore, we soften the loss of negative samples (unpaired samples) so as to weaken the strict constraint during the pre-training stage, thus mitigating the risk of forcing the model to distinguish compatible negative pairs. Experiments on five downstream tasks demonstrate the effectiveness of the proposed PyramidCLIP. In particular, with the same amount of 15 million pre-training image-text pairs, PyramidCLIP exceeds CLIP on ImageNet zero-shot classification top-1 accuracy by 10.6%/13.2%/10.0% with ResNet50/ViT-B32/ViT-B16 based image encoder respectively. When scaling to larger datasets, PyramidCLIP achieves the state-of-the-art results on several downstream tasks. In particular, the results of PyramidCLIP-ResNet50 trained on 143M image-text pairs surpass that of CLIP using 400M data on ImageNet zero-shot classification task, significantly improving the data efficiency of CLIP.

### Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models.
- **链接**: [arXiv:2209.07511](https://arxiv.org/abs/2209.07511) · [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5bf2b802e24106064dc547ae9283bb0c-Abstract-Conference.html) · 📚 569 citations
- **作者**: Manli Shu, Weili Nie, De-An Huang, Zhiding Yu, Tom Goldstein, Anima Anandkumar et al.
- **🏷️ 机构**: NVIDIA
- **会议**: NeurIPS 2022

- **摘要（英，原文）**:

  > Pre-trained vision-language models (e.g., CLIP) have shown promising zero-shot generalization in many downstream tasks with properly designed text prompts. Instead of relying on hand-engineered prompts, recent works learn prompts using the training data from downstream tasks. While effective, training on domain-specific data reduces a model's generalization capability to unseen new domains. In this work, we propose test-time prompt tuning (TPT), a method that can learn adaptive prompts on the fly with a single test sample. For image classification, TPT optimizes the prompt by minimizing the entropy with confidence selection so that the model has consistent predictions across different augmented views of each test sample. In evaluating generalization to natural distribution shifts, TPT improves the zero-shot top-1 accuracy of CLIP by 3.6% on average, surpassing previous prompt tuning approaches that require additional task-specific training data. In evaluating cross-dataset generalization with unseen categories, TPT performs on par with the state-of-the-art approaches that use additional training data. Project page: https://azshue.github.io/TPT.

### Look Around and Refer: 2D Synthetic Semantics Knowledge Distillation for 3D Visual Grounding.
- **链接**: [arXiv:2211.14241](https://arxiv.org/abs/2211.14241) · [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/f0b42291ddab77dcb2ef8a3488301b62-Abstract-Conference.html) · 📚 65 citations
- **作者**: Eslam Mohamed Bakr, Yasmeen Alsaedy, Mohamed Elhoseiny
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

- **摘要（英，原文）**:

  > The 3D visual grounding task has been explored with visual and language streams comprehending referential language to identify target objects in 3D scenes. However, most existing methods devote the visual stream to capturing the 3D visual clues using off-the-shelf point clouds encoders. The main question we address in this paper is "can we consolidate the 3D visual stream by 2D clues synthesized from point clouds and efficiently utilize them in training and testing?". The main idea is to assist the 3D encoder by incorporating rich 2D object representations without requiring extra 2D inputs. To this end, we leverage 2D clues, synthetically generated from 3D point clouds, and empirically show their aptitude to boost the quality of the learned visual representations. We validate our approach through comprehensive experiments on Nr3D, Sr3D, and ScanRefer datasets and show consistent performance gains compared to existing methods. Our proposed module, dubbed as Look Around and Refer (LAR), significantly outperforms the state-of-the-art 3D visual grounding techniques on three benchmarks, i.e., Nr3D, Sr3D, and ScanRefer. The code is available at https://eslambakr.github.io/LAR.github.io/.

## 跨领域论文（完整笔记在其他领域）

- MACK: Multimodal Aligned Conceptual Knowledge for Unpaired Image-text Matching. → [multimodal](../multimodal/Guideline%202022.md)
- CAESAR: An Embodied Simulator for Generating Multimodal Referring Expression Datasets. → [multimodal](../multimodal/Guideline%202022.md)
