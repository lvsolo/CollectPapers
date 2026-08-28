# Tracking — 2022 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Beyond 3D Siamese Tracking: A Motion-Centric Paradigm for 3D Single Object Tracking in Point Clouds.
- **链接**: [arXiv:2203.01730](https://arxiv.org/abs/2203.01730) · 📚 被引 103
- **作者**: Chaoda Zheng, Xu Yan, Haiming Zhang, Baoyuan Wang, Shenghui Cheng, Shuguang Cui et al.
- **🏷️ 机构**: The Chinese University of Hong Kong (Shenzhen), Xiaobing.AI, Westlake University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D single object tracking (3D SOT) in LiDAR point clouds plays a crucial role in autonomous driving. Current approaches all follow the Siamese paradigm based on appearance matching. However, LiDAR point clouds are usually textureless and incomplete, which hinders effective appearance matching. Besides, previous methods greatly overlook the critical motion clues among targets. In this work, beyond 3D Siamese tracking, we introduce a motion-centric paradigm to handle 3D SOT from a new perspective. Following this paradigm, we propose a matching-free two-stage tracker M^2-Track. At the 1^st-stage, M^2-Track localizes the target within successive frames via motion transformation. Then it refines the target box through motion-assisted shape completion at the 2^nd-stage. Extensive experiments confirm that M^2-Track significantly outperforms previous state-of-the-arts on three large-scale datasets while running at 57FPS (~8%, ~17%, and ~22%) precision gains on KITTI, NuScenes, and Waymo Open Dataset respectively). Further analysis verifies each component's effectiveness and shows the motion-centric paradigm's promising potential when combined with appearance matching.

</details>

## 跨领域论文（完整笔记在其他领域）

- Towards Discriminative Representation: Multi-view Trajectory Contrastive Learning for Online Multi-object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- LMGP: Lifted Multicut Meets Geometry Projections for Multi-Camera Multi-Object Tracking. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
