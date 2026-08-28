# Tracking — 2024 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### JDT3D: Addressing the Gaps in LiDAR-Based Tracking-by-Attention.
- **链接**: [arXiv:2407.04926](https://arxiv.org/abs/2407.04926) · [代码](https://github.com/TRAILab/JDT3D) · 📚 被引 4
- **作者**: Brian Cheong, Jiachen Zhou, Steven Lake Waslander
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate data association is crucial in reducing confusion, such as ID switches and assignment errors, in multi-object tracking (MOT). However, existing advanced methods often overlook the diversity among trajectories and the ambiguity and conflicts present in motion and appearance cues, leading to confusion among detections, trajectories, and associations when performing simple global data association. To address this issue, we propose a simple, versatile, and highly interpretable data association approach called Decomposed Data Association (DDA). DDA decomposes the traditional association problem into multiple sub-problems using a series of non-learning-based modules and selectively addresses the confusion in each sub-problem by incorporating targeted exploitation of new cues. Additionally, we introduce Occlusion-aware Non-Maximum Suppression (ONMS) to retain more occluded detections, thereby increasing opportunities for association with trajectories and indirectly reducing the confusion caused by missed detections. Finally, based on DDA and ONMS, we design a powerful multi-object tracker named DeconfuseTrack, specifically focused on resolving confusion in MOT. Extensive experiments conducted on the MOT17 and MOT20 datasets demonstrate that our proposed DDA and ONMS significantly enhance the performance of several popular trackers. Moreover, DeconfuseTrack achieves state-of-the-art performance on the MOT17 and MOT20 test sets, significantly outperforms the baseline tracker ByteTrack in metrics such as HOTA, IDF1, AssA. This validates that our tracking design effectively reduces confusion caused by simple global association.

</details>

### Towards Generalizable Multi-Object Tracking. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2406.00429](https://arxiv.org/abs/2406.00429) · 📚 被引 37
- **作者**: Zheng Qin, Le Wang, Sanping Zhou, Panpan Fu, Gang Hua, Wei Tang
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, School of Software Engineering, Xi&#x0027;an Jiaotong University, Wormpex AI Research
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有多目标跟踪器在不同场景下泛化能力差、需针对特定场景定制运动或外观关联的问题，研究了影响泛化的因素并将其具体化为跟踪场景属性，指导设计更通用的跟踪器。提出了点级到实例级的关系框架GeneralTrack，无需平衡运动和外观线索即可跨场景泛化。在多个基准上达到最先进性能，并展示了领域泛化潜力。
- **摘要（英）**: To improve tracker generalization across diverse tracking scenarios, this paper identifies scenario attributes influencing generalization and proposes GeneralTrack, a point-wise to instance-wise relation framework that avoids balancing motion and appearance. It achieves state-of-the-art performance on multiple benchmarks and demonstrates domain generalization potential.
- **核心贡献**: 提出场景属性分析和GeneralTrack框架，实现跨场景通用多目标跟踪。
- **创新点**: 点级到实例级关系建模，消除运动与外观线索的平衡需求。
- **结果**: 在多个基准上取得最先进性能，并验证领域泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-Object Tracking MOT encompasses various tracking scenarios, each characterized by unique traits. Effective trackers should demonstrate a high degree of generalizability across diverse scenarios. However, existing trackers struggle to accommodate all aspects or necessitate hypothesis and experimentation to customize the association information motion and or appearance for a given scenario, leading to narrowly tailored solutions with limited generalizability. In this paper, we investigate the factors that influence trackers generalization to different scenarios and concretize them into a set of tracking scenario attributes to guide the design of more generalizable trackers. Furthermore, we propose a point-wise to instance-wise relation framework for MOT, i.e., GeneralTrack, which can generalize across diverse scenarios while eliminating the need to balance motion and appearance. Thanks to its superior generalizability, our proposed GeneralTrack achieves state-of-the-art performance on multiple benchmarks and demonstrates the potential for domain generalization. https://github.com/qinzheng2000/GeneralTrack.git

</details>

### HIPTrack: Visual Tracking with Historical Prompts. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01822) · 📚 被引 107
- **作者**: Wenrui Cai, Qingjie Liu, Yunhong Wang
- **🏷️ 机构**: State Key Laboratory of Virtual Reality Technology and Systems, Beihang University,Beijing,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体研究问题、方法、改进点和效果信息。标题暗示提出一种利用历史提示的视觉跟踪方法，但缺乏细节支持评估。
- **摘要（英）**: The abstract is empty, providing no details on the problem, method, improvements, or results. The title suggests a visual tracking approach using historical prompts, but insufficient information prevents meaningful evaluation.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

</details>

### Boosting 3D Single Object Tracking with 2D Matching Distillation and 3D Pre-training.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73254-6_16) · 📚 被引 12
- **作者**: Qiangqiang Wu, Yan Xia, Jia Wan, Antoni B. Chan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work proposes a novel learning framework for visual hand dynamics analysis that takes into account the physiological aspects of hand motion. The existing models, which are simplified joint-actuated systems, often produce unnatural motions. To address this, we integrate a musculoskeletal system with a learnable parametric hand model, MANO, to create a new model, MS-MANO. This model emulates the dynamics of muscles and tendons to drive the skeletal system, imposing physiologically realistic constraints on the resulting torque trajectories. We further propose a simulation-in-the-loop pose refinement framework, BioPR, that refines the initial estimated pose through a multi-layer perceptron (MLP) network. Our evaluation of the accuracy of MS-MANO and the efficacy of the BioPR is conducted in two separate parts. The accuracy of MS-MANO is compared with MyoSuite, while the efficacy of BioPR is benchmarked against two large-scale public datasets and two recent state-of-the-art methods. The results demonstrate that our approach consistently improves the baseline methods both quantitatively and qualitatively.

</details>

## 跨领域论文（完整笔记在其他领域）

- Walker: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
