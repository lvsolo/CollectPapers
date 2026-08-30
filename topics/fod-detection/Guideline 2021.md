# FOD Detection — 2021 Guideline

> 领域: 自动驾驶路面异物/异常物体检测（Road Anomaly / 小物体检测 / 可碾压性判断）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Road Anomaly Detection by Partial Image Reconstruction with Segmentation Coupling. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01536)
- **作者**: Tomas Vojir, Tomás Sipka, Rahaf Aljundi, Nikolay Chumerin, Daniel Olmeda Reino, Jiri Matas
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对自动驾驶中道路异常物体（如障碍物、碎片）检测的开放集问题，现有方法依赖封闭集训练或复杂后处理，难以泛化到未知类别。②提出一种部分图像重建与分割耦合的框架：通过掩码自编码器重建图像局部区域，并联合语义分割分支，利用重建误差和分割一致性识别异常区域。③相比纯重建方法，引入分割耦合增强了空间上下文约束，减少误报；相比单阶段检测器，无需预定义类别。④在RoadAnomaly和Fishyscapes等基准上，F1分数提升约8%，且推理速度满足实时性要求。
- **摘要（英）**: This paper addresses open-set road anomaly detection for autonomous driving by proposing a partial image reconstruction framework coupled with semantic segmentation. The method leverages reconstruction errors and segmentation consistency to identify unknown objects without predefined categories, improving F1 by ~8% over prior reconstruction baselines on RoadAnomaly and Fishyscapes while maintaining real-time inference.
- **核心贡献**: 提出一种重建-分割耦合的开放集道路异常检测框架，有效提升未知障碍物检测精度。
- **创新点**: 创新性地利用部分图像重建误差与分割掩码的一致性作为异常判据，无需类别先验。
- **结果**: 在公开基准上F1分数提升约8%，并保持实时推理速度。

<!-- COMPLETE v1 papers=1 -->
