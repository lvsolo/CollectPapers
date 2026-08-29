# FOD Detection — 2025 Guideline

> 领域: 自动驾驶路面异物/异常物体检测（Road Anomaly / 小物体检测 / 可碾压性判断）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2023](Guideline%202023.md), [2021](Guideline%202021.md)

### Spotting the Unexpected (STU): A 3D LiDAR Dataset for Anomaly Segmentation in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2505.02148](https://arxiv.org/abs/2505.02148) · 📚 被引 4
- **作者**: Alexey Nekrasov, Malcolm Burdorf, Stewart Worrall, Bastian Leibe, Julie Stephany Berrio Perez
- **🏷️ 机构**: RWTH Aachen University, The University of Sydney
- **会议**: CVPR 2025
- **摘要（中）**: 针对自动驾驶中3D异常分割研究不足且缺乏高质量多模态数据的问题，本文提出了STU数据集，这是首个公开的、专注于道路异常分割的3D LiDAR数据集，包含密集3D语义标注、LiDAR和相机数据以及序列信息，支持不同范围的异常检测。作者还评估了多个3D分割基线模型，突出了驾驶环境中3D异常检测的挑战。该数据集和评估代码将公开，便于方法比较。
- **摘要（英）**: Addressing the underexplored 3D anomaly segmentation in autonomous driving, this paper presents STU, the first public dataset with dense 3D semantic labels, LiDAR and camera data, and sequential information for road anomaly detection. It evaluates baseline 3D segmentation models, highlighting challenges, and will release data and code for benchmarking.
- **核心贡献**: 发布了首个3D LiDAR道路异常分割数据集STU。
- **创新点**: 提供密集3D标注和多模态序列数据，支持跨范围异常检测。
- **结果**: 提供了基线评估，揭示了3D异常检测的挑战。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To operate safely, autonomous vehicles (AVs) need to detect and handle unexpected objects or anomalies on the road. While significant research exists for anomaly detection and segmentation in 2D, research progress in 3D is underexplored. Existing datasets lack high-quality multimodal data that are typically found in AVs. This paper presents a novel dataset for anomaly segmentation in driving scenarios. To the best of our knowledge, it is the first publicly available dataset focused on road anomaly segmentation with dense 3D semantic labeling, incorporating both LiDAR and camera data, as well as sequential information to enable anomaly detection across various ranges. This capability is critical for the safe navigation of autonomous vehicles. We adapted and evaluated several baseline models for 3D segmentation, highlighting the challenges of 3D anomaly detection in driving environments. Our dataset and evaluation code will be openly available, facilitating the testing and performance comparison of different approaches.

</details>
<!-- COMPLETE v1 papers=1 -->
