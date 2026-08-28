# Neural Architecture Search — 2023 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MDL-NAS: A Joint Multi-domain Learning Framework for Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01924) · 📚 被引 16
- **作者**: Shiguang Wang, Tao Xie, Jian Cheng, Xingcheng Zhang, Haijun Liu
- **🏷️ 机构**: University of Electronic Science and Technology of China, Harbin Institute of Technology, SenseTime Research
- **会议**: CVPR 2023

### DisWOT: Student Architecture Search for Distillation WithOut Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01145) · 📚 被引 60
- **作者**: Peijie Dong, Lujun Li, Zimian Wei
- **🏷️ 机构**: National University of Defense Technology, Chinese Academy of Sciences
- **会议**: CVPR 2023

### Adversarially Robust Neural Architecture Search for Graph Neural Networks.
- **链接**: [arXiv:2304.04168](https://arxiv.org/abs/2304.04168) · 📚 被引 21
- **作者**: Beini Xie, Heng Chang, Ziwei Zhang, Xin Wang, Daixin Wang, Zhiqiang Zhang et al.
- **🏷️ 机构**: Tsinghua University, Ant Group, Yale University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Graph Neural Networks (GNNs) obtain tremendous success in modeling relational data. Still, they are prone to adversarial attacks, which are massive threats to applying GNNs to risk-sensitive domains. Existing defensive methods neither guarantee performance facing new data/tasks or adversarial attacks nor provide insights to understand GNN robustness from an architectural perspective. Neural Architecture Search (NAS) has the potential to solve this problem by automating GNN architecture designs. Nevertheless, current graph NAS approaches lack robust design and are vulnerable to adversarial attacks. To tackle these challenges, we propose a novel Robust Neural Architecture search framework for GNNs (G-RNA). Specifically, we design a robust search space for the message-passing mechanism by adding graph structure mask operations into the search space, which comprises various defensive operation candidates and allows us to search for defensive GNNs. Furthermore, we define a robustness metric to guide the search procedure, which helps to filter robust architectures. In this way, G-RNA helps understand GNN robustness from an architectural perspective and effectively searches for optimal adversarial robust GNNs. Extensive experimental results on benchmark datasets show that G-RNA significantly outperforms manually designed robust GNNs and vanilla graph NAS baselines by 12.1% to 23.4% under adversarial attacks.

</details>

### HOTNAS: Hierarchical Optimal Transport for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01154) · 📚 被引 15
- **作者**: Jiechao Yang, Yong Liu, Hongteng Xu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China
- **会议**: CVPR 2023

### Differentiable Architecture Search with Random Features.
- **链接**: [arXiv:2208.08835](https://arxiv.org/abs/2208.08835) · 📚 被引 18
- **作者**: Xuanyang Zhang, Yonggang Li, Xiangyu Zhang, Yongtao Wang, Jian Sun
- **🏷️ 机构**: MEGVII Technology, Peking University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Differentiable architecture search (DARTS) has significantly promoted the development of NAS techniques because of its high search efficiency and effectiveness but suffers from performance collapse. In this paper, we make efforts to alleviate the performance collapse problem for DARTS from two aspects. First, we investigate the expressive power of the supernet in DARTS and then derive a new setup of DARTS paradigm with only training BatchNorm. Second, we theoretically find that random features dilute the auxiliary connection role of skip-connection in supernet optimization and enable search algorithm focus on fairer operation selection, thereby solving the performance collapse problem. We instantiate DARTS and PC-DARTS with random features to build an improved version for each named RF-DARTS and RF-PCDARTS respectively. Experimental results show that RF-DARTS obtains \textbf{94.36\%} test accuracy on CIFAR-10 (which is the nearest optimal result in NAS-Bench-201), and achieves the newest state-of-the-art top-1 test error of \textbf{24.0\%} on ImageNet when transferring from CIFAR-10. Moreover, RF-DARTS performs robustly across three datasets (CIFAR-10, CIFAR-100, and SVHN) and four search spaces (S1-S4). Besides, RF-PCDARTS achieves even better results on ImageNet, that is, \textbf{23.9\%} top-1 and \textbf{7.1\%} top-5 test error, surpassing representative methods like single-path, training-free, and partial-channel paradigms directly searched on ImageNet.

</details>
