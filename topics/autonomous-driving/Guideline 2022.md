# Autonomous Driving — 2022 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### K-Radar: 4D Radar Object Detection for Autonomous Driving in Various Weather Conditions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/185fdf627eaae2abab36205dcd19b817-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 33
- **作者**: Dong-Hee Paek, Seung-Hyun Kong, Kevin Tirta Wijaya
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Effective Adaptation in Multi-Task Co-Training for Unified Autonomous Driving.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7c319b62e2257b34cb0e1040ced2e007-Abstract-Conference.html) · 📚 被引 4
- **作者**: Xiwen Liang, Yangxin Wu, Jianhua Han, Hang Xu, Chunjing Xu, Xiaodan Liang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Trajectory-guided Control Prediction for End-to-end Autonomous Driving: A Simple yet Strong Baseline.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/286a371d8a0a559281f682f8fbf89834-Abstract-Conference.html) · 📚 被引 45
- **作者**: Penghao Wu, Xiaosong Jia, Li Chen, Junchi Yan, Hongyang Li, Yu Qiao
- **🏷️ 机构**: Shanghai AI Lab
- **会议**: NeurIPS 2022

### Unsupervised Adaptation from Repeated Traversals for Autonomous Driving.
- **链接**: [arXiv:2303.15286](https://arxiv.org/abs/2303.15286) · 📚 被引 0
- **作者**: Yurong You, Cheng Perng Phoo, Katie Luo, Travis Zhang, Wei-Lun Chao, Bharath Hariharan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> For a self-driving car to operate reliably, its perceptual system must generalize to the end-user's environment -- ideally without additional annotation efforts. One potential solution is to leverage unlabeled data (e.g., unlabeled LiDAR point clouds) collected from the end-users' environments (i.e. target domain) to adapt the system to the difference between training and testing environments. While extensive research has been done on such an unsupervised domain adaptation problem, one fundamental problem lingers: there is no reliable signal in the target domain to supervise the adaptation process. To overcome this issue we observe that it is easy to collect unsupervised data from multiple traversals of repeated routes. While different from conventional unsupervised domain adaptation, this assumption is extremely realistic since many drivers share the same roads. We show that this simple additional assumption is sufficient to obtain a potent signal that allows us to perform iterative self-training of 3D object detectors on the target domain. Concretely, we generate pseudo-labels with the out-of-domain detector but reduce false positives by removing detections of supposedly mobile objects that are persistent across traversals. Further, we reduce false negatives by encouraging predictions in regions that are not persistent. We experiment with our approach on two large-scale driving datasets and show remarkable improvement in 3D object detection of cars, pedestrians, and cyclists, bringing us a step closer to generalizable autonomous driving.

</details>
