# VLM — 2022 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Single-Stream Multi-level Alignment for Vision-Language Pretraining.
- **链接**: [arXiv:2203.14395](https://arxiv.org/abs/2203.14395)
- **作者**: Zaid Khan, B. G. Vijay Kumar, Xiang Yu, Samuel Schulter, Manmohan Chandraker, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised vision-language pretraining from pure images and text with a contrastive loss is effective, but ignores fine-grained alignment due to a dual-stream architecture that aligns image and text representations only on a global level. Earlier, supervised, non-contrastive methods were capable of finer-grained alignment, but required dense annotations that were not scalable. We propose a single stream architecture that aligns images and language at multiple levels: global, fine-grained patch-token, and conceptual/semantic, using two novel tasks: symmetric cross-modality reconstruction (XMM) and a pseudo-labeled key word prediction (PSL). In XMM, we mask input tokens from one modality and use cross-modal information to reconstruct the masked token, thus improving fine-grained alignment between the two modalities. In PSL, we use attention to select keywords in a caption, use a momentum encoder to recommend other important keywords that are missing from the caption but represented in the image, and then train the visual encoder to predict the presence of those keywords, helping it learn semantic concepts that are essential for grounding a textual token to an image region. We demonstrate competitive performance and improved data efficiency on image-text retrieval, grounding, visual question answering/reasoning against larger models and models trained on more data. Code and models available at zaidkhan.me/SIMLA.

</details>

### A Dataset for Interactive Vision-Language Navigation with Unknown Command Feasibility.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_18) · 📚 被引 29
- **作者**: Andrea Burns, Deniz Arsan, Sanjna Agrawal, Ranjitha Kumar, Kate Saenko, Bryan A. Plummer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Learning Disentanglement with Decoupled Labels for Vision-Language Navigation.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_18) · 📚 被引 8
- **作者**: Wenhao Cheng, Xingping Dong, Salman H. Khan, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Generative Negative Text Replay for Continual Vision-Language Pretraining.
- **链接**: [arXiv:2210.17322](https://arxiv.org/abs/2210.17322)
- **作者**: Shipeng Yan, Lanqing Hong, Hang Xu, Jianhua Han, Tinne Tuytelaars, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language pre-training (VLP) has attracted increasing attention recently. With a large amount of image-text pairs, VLP models trained with contrastive loss have achieved impressive performance in various tasks, especially the zero-shot generalization on downstream datasets. In practical applications, however, massive data are usually collected in a streaming fashion, requiring VLP models to continuously integrate novel knowledge from incoming data and retain learned knowledge. In this work, we focus on learning a VLP model with sequential chunks of image-text pair data. To tackle the catastrophic forgetting issue in this multi-modal continual learning setting, we first introduce pseudo text replay that generates hard negative texts conditioned on the training images in memory, which not only better preserves learned knowledge but also improves the diversity of negative samples in the contrastive loss. Moreover, we propose multi-modal knowledge distillation between images and texts to align the instance-wise prediction between old and new models. We incrementally pre-train our model on both the instance and class incremental splits of the Conceptual Caption dataset, and evaluate the model on zero-shot image classification and image-text retrieval tasks. Our method consistently outperforms the existing baselines with a large margin, which demonstrates its superiority. Notably, we realize an average performance boost of $4.60\%$ on image-classification downstream datasets for the class incremental split.

</details>

### UniTAB: Unifying Text and Box Outputs for Grounded Vision-Language Modeling.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_30)
- **作者**: Zhengyuan Yang, Zhe Gan, Jianfeng Wang, Xiaowei Hu, Faisal Ahmed, Zicheng Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

### Learning Visual Representation from Modality-Shared Contrastive Language-Image Pre-training.
- **链接**: [arXiv:2207.12661](https://arxiv.org/abs/2207.12661) · [代码](https://github.com/Hxyou/MSCLIP)
- **作者**: Haoxuan You, Luowei Zhou, Bin Xiao, Noel Codella, Yu Cheng, Ruochen Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale multi-modal contrastive pre-training has demonstrated great utility to learn transferable features for a range of downstream tasks by mapping multiple modalities into a shared embedding space. Typically, this has employed separate encoders for each modality. However, recent work suggests that transformers can support learning across multiple modalities and allow knowledge sharing. Inspired by this, we investigate a variety of Modality-Shared Contrastive Language-Image Pre-training (MS-CLIP) frameworks. More specifically, we question how many parameters of a transformer model can be shared across modalities during contrastive pre-training, and rigorously examine architectural design choices that position the proportion of parameters shared along a spectrum. In studied conditions, we observe that a mostly unified encoder for vision and language signals outperforms all other variations that separate more parameters. Additionally, we find that light-weight modality-specific parallel modules further improve performance. Experimental results show that the proposed MS-CLIP approach outperforms vanilla CLIP by up to 13\% relative in zero-shot ImageNet classification (pre-trained on YFCC-100M), while simultaneously supporting a reduction of parameters. In addition, our approach outperforms vanilla CLIP by 1.6 points in linear probing on a collection of 24 downstream vision tasks. Furthermore, we discover that sharing parameters leads to semantic concepts from different modalities being encoded more closely in the embedding space, facilitating the transferring of common semantic structure (e.g., attention patterns) from language to vision. Code is available at \href{https://github.com/Hxyou/MSCLIP}{URL}.

</details>

## 跨领域论文（完整笔记在其他领域）

- A Simple Baseline for Open-Vocabulary Semantic Segmentation with Pre-trained Vision-Language Model. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- CODER: Coupled Diversity-Sensitive Momentum Contrastive Learning for Image-Text Retrieval. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
