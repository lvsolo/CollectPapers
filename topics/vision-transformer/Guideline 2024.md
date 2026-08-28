# Vision Transformer — 2024 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLAMP-ViT: Contrastive Data-Free Learning for Adaptive Post-training Quantization of ViTs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72855-6_18) · 📚 被引 11
- **作者**: Akshat Ramachandran, Souvik Kundu, Tushar Krishna
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Rotary Position Embedding for Vision Transformer.
- **链接**: [arXiv:2403.13298](https://arxiv.org/abs/2403.13298) · [代码](https://github.com/naver-ai/rope-vit) · 📚 被引 58
- **作者**: Byeongho Heo, Song Park, Dongyoon Han, Sangdoo Yun
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Rotary Position Embedding (RoPE) performs remarkably on language models, especially for length extrapolation of Transformers. However, the impacts of RoPE on computer vision domains have been underexplored, even though RoPE appears capable of enhancing Vision Transformer (ViT) performance in a way similar to the language domain. This study provides a comprehensive analysis of RoPE when applied to ViTs, utilizing practical implementations of RoPE for 2D vision data. The analysis reveals that RoPE demonstrates impressive extrapolation performance, i.e., maintaining precision while increasing image resolution at inference. It eventually leads to performance improvement for ImageNet-1k, COCO detection, and ADE-20k segmentation. We believe this study provides thorough guidelines to apply RoPE into ViT, promising improved backbone performance with minimal extra computational overhead. Our code and pre-trained models are available at https://github.com/naver-ai/rope-vit

</details>

### SpecFormer: Guarding Vision Transformer Robustness via Maximum Singular Value Penalization.
- **链接**: [arXiv:2402.03317](https://arxiv.org/abs/2402.03317) · [代码](https://github.com/microsoft/robustlearn) · 📚 被引 1
- **作者**: Xixu Hu, Runkai Zheng, Jindong Wang, Cheuk Hang Leung, Qi Wu, Xing Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) are increasingly used in computer vision due to their high performance, but their vulnerability to adversarial attacks is a concern. Existing methods lack a solid theoretical basis, focusing mainly on empirical training adjustments. This study introduces SpecFormer, tailored to fortify ViTs against adversarial attacks, with theoretical underpinnings. We establish local Lipschitz bounds for the self-attention layer and propose the Maximum Singular Value Penalization (MSVP) to precisely manage these bounds By incorporating MSVP into ViTs' attention layers, we enhance the model's robustness without compromising training efficiency. SpecFormer, the resulting model, outperforms other state-of-the-art models in defending against adversarial attacks, as proven by experiments on CIFAR and ImageNet datasets. Code is released at https://github.com/microsoft/robustlearn.

</details>

### Token Compensator: Altering Inference Cost of Vision Transformer Without Re-tuning.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72640-8_5) · 📚 被引 4
- **作者**: Shibo Jie, Yehui Tang, Jianyuan Guo, Zhi-Hong Deng, Kai Han, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Fairness-Aware Vision Transformer via Debiased Self-Attention.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72913-3_20) · 📚 被引 4
- **作者**: Yao Qiang, Chengyin Li, Prashant Khanduri, Dongxiao Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Removing Rows and Columns of Tokens in Vision Transformer Enables Faster Dense Prediction Without Retraining.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73220-1_19) · 📚 被引 1
- **作者**: Diwei Su, Cheng Fei, Jianxu Luo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### FairViT: Fair Vision Transformer via Adaptive Masking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73650-6_26) · 📚 被引 5
- **作者**: Bowei Tian, Ruijie Du, Yanning Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### GiT: Towards Generalist Vision Transformer Through Universal Language Interface.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73397-0_4) · 📚 被引 6
- **作者**: Haiyang Wang, Hao Tang, Li Jiang, Shaoshuai Shi, Muhammad Ferjad Naeem, Hongsheng Li et al.
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2024

### Parameter-Efficient and Memory-Efficient Tuning for Vision Transformer: A Disentangled Approach.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72995-9_20)
- **作者**: Taolin Zhang, Jiawang Bai, Zhihe Lu, Dongze Lian, Genping Wang, Xinchao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

## 跨领域论文（完整笔记在其他领域）

- Make Your ViT-Based Multi-view 3D Detectors Faster via Token Compression. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Scene-Graph ViT: End-to-End Open-Vocabulary Visual Relationship Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
