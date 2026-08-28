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
