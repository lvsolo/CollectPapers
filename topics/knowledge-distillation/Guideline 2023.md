# Knowledge Distillation — 2023 Guideline

> 领域: 知识蒸馏（特征/逻辑蒸馏、VLM 蒸馏、自蒸馏）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Periodically Exchange Teacher-Student for Source-Free Object Detection.
- **链接**: [arXiv:2311.13930](https://arxiv.org/abs/2311.13930) · 📚 被引 45
- **作者**: Qipeng Liu, Luojun Lin, Zhifeng Shen, Zhifeng Yang
- **🏷️ 机构**: Fuzhou University,College of Computer and Data Science
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Source-free object detection (SFOD) aims to adapt the source detector to unlabeled target domain data in the absence of source domain data. Most SFOD methods follow the same self-training paradigm using mean-teacher (MT) framework where the student model is guided by only one single teacher model. However, such paradigm can easily fall into a training instability problem that when the teacher model collapses uncontrollably due to the domain shift, the student model also suffers drastic performance degradation. To address this issue, we propose the Periodically Exchange Teacher-Student (PETS) method, a simple yet novel approach that introduces a multiple-teacher framework consisting of a static teacher, a dynamic teacher, and a student model. During the training phase, we periodically exchange the weights between the static teacher and the student model. Then, we update the dynamic teacher using the moving average of the student model that has already been exchanged by the static teacher. In this way, the dynamic teacher can integrate knowledge from past periods, effectively reducing error accumulation and enabling a more stable training process within the MT-based framework. Further, we develop a consensus mechanism to merge the predictions of two teacher models to provide higher-quality pseudo labels for student model. Extensive experiments on multiple SFOD benchmarks show that the proposed method achieves state-of-the-art performance compared with other related methods, demonstrating the effectiveness and superiority of our method on SFOD task.

</details>

### Masked Retraining Teacher-Student Framework for Domain Adaptive Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01745) · 📚 被引 49
- **作者**: Zijing Zhao, Sitong Wei, Qingchao Chen, Dehui Li, Yifan Yang, Yuxin Peng et al.
- **🏷️ 机构**: Peking University,Wangxuan Institute of Computer Technology, Peking University,National Institute of Health Data Science, Tencent Intelligent Mobility
- **会议**: ICCV 2023

### TSOSVNet: Teacher-student collaborative knowledge distillation for Online Signature Verification.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00082) · 📚 被引 2
- **作者**: Chandra Sekhar Vorugunti, Avinash Gautam, Viswanath Pulabaigari, Sreeja SR, Rama Krishna Sai G
- **🏷️ 机构**: IIIT-SriCity,Andhra Pradesh,India, BITS-Pilani,India, IIT-Tirupati,Andhra Pradesh,India
- **会议**: ICCV 2023

## 🆕 增量新增

### Complete-to-Partial 4D Distillation for Self-Supervised Point Cloud Sequence Representation Learning. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2212.05330](https://arxiv.org/abs/2212.05330) · 📚 被引 23
- **作者**: Zhuoyang Zhang, Yuhao Dong, Yunze Liu, Li Yi
- **🏷️ 机构**: IIIS, Tsinghua University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对4D点云序列自监督表示学习未充分利用动态场景时序几何信息的问题。②提出Complete-to-Partial 4D Distillation方法，将4D自监督预训练建模为教师-学生知识蒸馏框架，学生从教师引导中学习有用的4D表示。③相比静态快照方法和图像空间流方法，该方法同时考虑3D几何和时序动态。④在室内外多个4D点云序列理解任务上显著优于现有预训练方法。
- **摘要（英）**: This paper proposes Complete-to-Partial 4D Distillation, a teacher-student knowledge distillation framework for self-supervised 4D point cloud sequence representation learning, which leverages temporal geometric details. It significantly outperforms prior pre-training approaches on various indoor and outdoor 4D understanding tasks.
- **核心贡献**: 提出首个基于知识蒸馏的4D点云序列自监督预训练方法。
- **创新点**: 将完整到部分的重建任务转化为教师-学生蒸馏框架，有效利用时序几何信息。
- **结果**: 在室内外4D点云任务上大幅超越现有预训练方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent work on 4D point cloud sequences has attracted a lot of attention. However, obtaining exhaustively labeled 4D datasets is often very expensive and laborious, so it is especially important to investigate how to utilize raw unlabeled data. However, most existing self-supervised point cloud representation learning methods only consider geometry from a static snapshot omitting the fact that sequential observations of dynamic scenes could reveal more comprehensive geometric details. And the video representation learning frameworks mostly model motion as image space flows, let alone being 3D-geometric-aware. To overcome such issues, this paper proposes a new 4D self-supervised pre-training method called Complete-to-Partial 4D Distillation. Our key idea is to formulate 4D self-supervised representation learning as a teacher-student knowledge distillation framework and let the student learn useful 4D representations with the guidance of the teacher. Experiments show that this approach significantly outperforms previous pre-training approaches on a wide range of 4D point cloud sequence understanding tasks including indoor and outdoor scenarios.

</details>

### MaskCLIP: Masked Self-Distillation Advances Contrastive Language-Image Pretraining. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2208.12262](https://arxiv.org/abs/2208.12262) · 📚 被引 162
- **作者**: Xiaoyi Dong, Jianmin Bao, Yinglin Zheng, Ting Zhang, Dongdong Chen, Hao Yang et al.
- **🏷️ 机构**: University of Science and Technology of China, Microsoft Research Asia, Xiamen University
- **会议**: CVPR 2023
- **摘要（中）**: 针对对比语言-图像预训练（如CLIP）缺乏局部语义表示学习的问题，提出MaskCLIP框架，将掩码自蒸馏融入对比预训练。该方法从完整图像蒸馏表示到掩码图像的预测表示，与视觉-语言对比学习互补，并利用语言间接监督局部语义。实验表明，MaskCLIP在多种下游任务（如线性探测、微调）上取得优越结果，验证了掩码自蒸馏的有效性。
- **摘要（英）**: To address the lack of local semantic representation learning in contrastive language-image pretraining, this paper proposes MaskCLIP, which integrates masked self-distillation into the contrastive framework. It distills representations from full images to masked-image predictions, complementing text-related contrastive learning and leveraging language for indirect local supervision. Extensive experiments show superior performance on downstream tasks like linear probing and fine-tuning.
- **核心贡献**: 提出掩码自蒸馏与对比预训练结合的框架，提升局部表示学习。
- **创新点**: 将掩码图像建模引入CLIP训练，实现全局-局部特征对齐。
- **结果**: 在多个下游任务上取得SOTA结果，验证方法有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents a simple yet effective framework MaskCLIP, which incorporates a newly proposed masked self-distillation into contrastive language-image pretraining. The core idea of masked self-distillation is to distill representation from a full image to the representation predicted from a masked image. Such incorporation enjoys two vital benefits. First, masked self-distillation targets local patch representation learning, which is complementary to vision-language contrastive focusing on text-related representation. Second, masked self-distillation is also consistent with vision-language contrastive from the perspective of training objective as both utilize the visual encoder for feature aligning, and thus is able to learn local semantics getting indirect supervision from the language. We provide specially designed experiments with a comprehensive analysis to validate the two benefits. Symmetrically, we also introduce the local semantic supervision into the text branch, which further improves the pretraining performance. With extensive experiments, we show that MaskCLIP, when applied to various challenging downstream tasks, achieves superior results in linear probing, finetuning, and zero-shot performance with the guidance of the language encoder. Code will be release at \url{https://github.com/LightDXY/MaskCLIP}.

</details>
<!-- COMPLETE v1 papers=5 -->
