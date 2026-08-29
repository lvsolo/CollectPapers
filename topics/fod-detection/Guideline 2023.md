# FOD Detection — 2023 Guideline

> 领域: 自动驾驶路面异物/异常物体检测（Road Anomaly / 小物体检测 / 可碾压性判断）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2025](Guideline%202025.md), [2021](Guideline%202021.md)

### Visual Exemplar Driven Task-Prompting for Unified Perception in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2303.01788](https://arxiv.org/abs/2303.01788) · 📚 被引 22
- **作者**: Xiwen Liang, Minzhe Niu, Jianhua Han, Hang Xu, Chunjing Xu, Xiaodan Liang
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2023
- **摘要（中）**: ①该论文针对自动驾驶中多任务学习（如目标检测、语义分割、可行驶区域分割和车道线检测）性能远低于单任务基线的问题。②提出了VE-Prompt框架，通过引入视觉示例（visual exemplars）和任务特定提示（task-specific prompting）来引导模型学习高质量的任务特定表示，并在大规模驾驶数据集上系统评估了现有主流多任务方法。③相比已有工作，该研究首次在自动驾驶场景下对多任务方法进行全面比较，并利用视觉示例增强任务提示，弥补了通用多任务方法在驾驶任务上的性能差距。④实验表明，现有方法虽有效但仍与单任务基线存在较大差距，而VE-Prompt在多个任务上显著提升了性能，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the performance gap of multi-task learning methods in autonomous driving perception tasks, including object detection, semantic segmentation, drivable area segmentation, and lane detection. It proposes VE-Prompt, a framework that leverages visual exemplars and task-specific prompting to learn high-quality task-specific representations, and provides a comprehensive evaluation of existing multi-task methods on a large-scale driving dataset. The results show that VE-Prompt effectively improves multi-task performance, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出了VE-Prompt框架，利用视觉示例和任务提示提升自动驾驶多任务感知性能，并提供了大规模驾驶数据集上的多任务方法基准评估。
- **创新点**: 创新性地将视觉示例引入任务特定提示机制，以增强多任务模型的任务特定表示学习。
- **结果**: 在自动驾驶多任务感知上显著缩小了与单任务基线的性能差距，具体数据待全文验证。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-task learning has emerged as a powerful paradigm to solve a range of tasks simultaneously with good efficiency in both computation resources and inference time. However, these algorithms are designed for different tasks mostly not within the scope of autonomous driving, thus making it hard to compare multi-task methods in autonomous driving. Aiming to enable the comprehensive evaluation of present multi-task learning methods in autonomous driving, we extensively investigate the performance of popular multi-task methods on the large-scale driving dataset, which covers four common perception tasks, i.e., object detection, semantic segmentation, drivable area segmentation, and lane detection. We provide an in-depth analysis of current multi-task learning methods under different common settings and find out that the existing methods make progress but there is still a large performance gap compared with single-task baselines. To alleviate this dilemma in autonomous driving, we present an effective multi-task framework, VE-Prompt, which introduces visual exemplars via task-specific prompting to guide the model toward learning high-quality task-specific representations. Specifically, we generate visual exemplars based on bounding boxes and color-based markers, which provide accurate visual appearances of target categories and further mitigate the performance gap. Furthermore, we bridge transformer-based encoders and convolutional layers for efficient and accurate unified perception in autonomous driving. Comprehensive experimental results on the diverse self-driving dataset BDD100K show that the VE-Prompt improves the multi-task baseline and further surpasses single-task models.

</details>

## 跨领域论文（完整笔记在其他领域）

- Meta-Tuning Loss Functions and Data Augmentation for Few-Shot Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
<!-- COMPLETE v1 papers=2 -->
