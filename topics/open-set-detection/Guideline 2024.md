# Open-set Detection — 2024 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### TextField3D: Towards Enhancing Open-Vocabulary 3D Generation with Noisy Text Fields.
- **链接**: [arXiv:2309.17175](https://arxiv.org/abs/2309.17175)
- **作者**: Tianyu Huang, Yihan Zeng, Bowen Dong, Hang Xu, Songcen Xu, Rynson W. H. Lau et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works learn 3D representation explicitly under text-3D guidance. However, limited text-3D data restricts the vocabulary scale and text control of generations. Generators may easily fall into a stereotype concept for certain text prompts, thus losing open-vocabulary generation ability. To tackle this issue, we introduce a conditional 3D generative model, namely TextField3D. Specifically, rather than using the text prompts as input directly, we suggest to inject dynamic noise into the latent space of given text prompts, i.e., Noisy Text Fields (NTFs). In this way, limited 3D data can be mapped to the appropriate range of textual latent space that is expanded by NTFs. To this end, an NTFGen module is proposed to model general text latent code in noisy fields. Meanwhile, an NTFBind module is proposed to align view-invariant image latent code to noisy fields, further supporting image-conditional 3D generation. To guide the conditional generation in both geometry and texture, multi-modal discrimination is constructed with a text-3D discriminator and a text-2.5D discriminator. Compared to previous methods, TextField3D includes three merits: 1) large vocabulary, 2) text consistency, and 3) low latency. Extensive experiments demonstrate that our method achieves a potential open-vocabulary 3D generation capability.

</details>

### FROSTER: Frozen CLIP is A Strong Teacher for Open-Vocabulary Action Recognition.
- **链接**: [出版页](https://openreview.net/forum?id=zYXFMeHRtO)
- **作者**: Xiaohu Huang, Hao Zhou, Kun Yao, Kai Han
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction.
- **链接**: [出版页](https://openreview.net/forum?id=DjzvJCRsVf)
- **作者**: Size Wu, Wenwei Zhang, Lumin Xu, Sheng Jin, Xiangtai Li, Wentao Liu et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: ICLR 2024

### Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.
- **链接**: [arXiv:2310.05130](https://arxiv.org/abs/2310.05130) · [代码](https://github.com/baoguangsheng/fast-detect-gpt)
- **作者**: Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, Yue Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have shown the ability to produce fluent and cogent content, presenting both productivity opportunities and societal risks. To build trustworthy AI systems, it is imperative to distinguish between machine-generated and human-authored content. The leading zero-shot detector, DetectGPT, showcases commendable performance but is marred by its intensive computational costs. In this paper, we introduce the concept of conditional probability curvature to elucidate discrepancies in word choices between LLMs and humans within a given context. Utilizing this curvature as a foundational metric, we present **Fast-DetectGPT**, an optimized zero-shot detector, which substitutes DetectGPT's perturbation step with a more efficient sampling step. Our evaluations on various datasets, source models, and test conditions indicate that Fast-DetectGPT not only surpasses DetectGPT by a relative around 75% in both the white-box and black-box settings but also accelerates the detection process by a factor of 340, as detailed in Table 1. See \url{https://github.com/baoguangsheng/fast-detect-gpt} for code, data, and results.

</details>

## 跨领域论文（完整笔记在其他领域）

- LLMs Meet VLMs: Boost Open Vocabulary Object Detection with Fine-grained Descriptors. → [object-detection](../object-detection/Guideline%202024.md)
