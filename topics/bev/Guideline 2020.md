# BEV — 2020 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

## 跨领域论文（完整笔记在其他领域）

- MotionNet: Joint Perception and Motion Prediction for Autonomous Driving Based on Bird's Eye View Maps. → [autonomous-driving](../autonomous-driving/Guideline%202020.md)

## 🆕 增量新增

### MotionNet: Joint Perception and Motion Prediction for Autonomous Driving Based on Bird's Eye View Maps. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2003.06754](https://arxiv.org/abs/2003.06754) · 📚 被引 172
- **作者**: Pengxiang Wu, Siheng Chen, Dimitris N. Metaxas
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: 针对自动驾驶中感知和运动预测分离导致效率低下的问题，提出MotionNet，一种基于BEV地图的联合感知与运动预测深度模型。该方法输入LiDAR扫描序列，输出编码物体类别和运动信息的BEV图，并设计新颖的时空金字塔网络提取层次化特征，同时引入空间和时间一致性损失正则化训练。实验表明，该方法在多个基准上优于基于场景流和3D目标检测的最新方法，可作为边界框系统的补充，为运动规划提供辅助信息。
- **摘要（英）**: MotionNet proposes a joint perception and motion prediction model based on BEV maps, processing LiDAR sweeps to output object categories and motion information. It introduces a spatio-temporal pyramid network and consistency losses, outperforming state-of-the-art scene-flow and 3D detection methods. This provides a complementary approach to bounding-box systems for autonomous driving motion planning.
- **核心贡献**: 提出联合BEV感知和运动预测的深度学习框架，提升效率和准确性。
- **创新点**: 设计时空金字塔网络和一致性损失，实现层次化特征提取和预测平滑。
- **结果**: 在多个基准上超越现有最优方法，验证了联合方法的潜力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to reliably perceive the environmental states, particularly the existence of objects and their motion behavior, is crucial for autonomous driving. In this work, we propose an efficient deep model, called MotionNet, to jointly perform perception and motion prediction from 3D point clouds. MotionNet takes a sequence of LiDAR sweeps as input and outputs a bird's eye view (BEV) map, which encodes the object category and motion information in each grid cell. The backbone of MotionNet is a novel spatio-temporal pyramid network, which extracts deep spatial and temporal features in a hierarchical fashion. To enforce the smoothness of predictions over both space and time, the training of MotionNet is further regularized with novel spatial and temporal consistency losses. Extensive experiments show that the proposed method overall outperforms the state-of-the-arts, including the latest scene-flow- and 3D-object-detection-based methods. This indicates the potential value of the proposed method serving as a backup to the bounding-box-based system, and providing complementary information to the motion planner in autonomous driving. Code is available at https://github.com/pxiangwu/MotionNet.

</details>

## 跨领域论文（完整笔记在其他领域）

- PointPainting: Sequential Fusion for 3D Object Detection. → [object-detection](../object-detection/Guideline%202020.md)
<!-- COMPLETE v1 papers=1 -->
