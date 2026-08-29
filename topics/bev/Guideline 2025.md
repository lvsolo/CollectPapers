# BEV — 2025 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### ForestLPR: LiDAR Place Recognition in Forests Attentioning Multiple BEV Density Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shen_ForestLPR_LiDAR_Place_Recognition_in_Forests_Attentioning_Multiple_BEV_Density_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Yanqing Shen, Turcan Tuna, Marco Hutter, César Cadena, Nanning Zheng
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,Institute of Artificial Intelligence and Robotics, ETH Zurich,Robotic Systems Lab
- **会议**: CVPR 2025

### SDGOCC: Semantic and Depth-Guided Bird's-Eye View Transformation for 3D Multimodal Occupancy Prediction.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Duan_SDGOCC_Semantic_and_Depth-Guided_Birds-Eye_View_Transformation_for_3D_Multimodal_CVPR_2025_paper.html)
- **作者**: Zaipeng Duan, Chenxu Dang, Xuzhong Hu, Pei An, Junfeng Ding, Jie Zhan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### BEVDiffuser: Plug-and-Play Diffusion Model for BEV Denoising with Ground-Truth Guidance.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_BEVDiffuser_Plug-and-Play_Diffusion_Model_for_BEV_Denoising_with_Ground-Truth_Guidance_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Xin Ye, Burhaneddin Yaman, Sheng Cheng, Feng Tao, Abhirup Mallik, Liu Ren
- **🏷️ 机构**: Bosch Research North America &amp; Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2025

### Generative Map Priors for Collaborative BEV Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Fu_Generative_Map_Priors_for_Collaborative_BEV_Semantic_Segmentation_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Jiahui Fu, Yue Gong, Luting Wang, Shifeng Zhang, Xu Zhou, Si Liu
- **🏷️ 机构**: Beihang University,Institute of Artificial Intelligence, Sangfor Technologies Inc.
- **会议**: CVPR 2025

### Toward Real-world BEV Perception: Depth Uncertainty Estimation via Gaussian Splatting.
- **链接**: [arXiv:2504.01957](https://arxiv.org/abs/2504.01957) · 📚 被引 8
- **作者**: Shu-Wei Lu, Yi-Hsuan Tsai, Yi-Ting Chen
- **🏷️ 机构**: National Yang Ming Chiao Tung University, Atmanity Inc.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bird's-eye view (BEV) perception has gained significant attention because it provides a unified representation to fuse multiple view images and enables a wide range of down-stream autonomous driving tasks, such as forecasting and planning. Recent state-of-the-art models utilize projection-based methods which formulate BEV perception as query learning to bypass explicit depth estimation. While we observe promising advancements in this paradigm, they still fall short of real-world applications because of the lack of uncertainty modeling and expensive computational requirement. In this work, we introduce GaussianLSS, a novel uncertainty-aware BEV perception framework that revisits unprojection-based methods, specifically the Lift-Splat-Shoot (LSS) paradigm, and enhances them with depth un-certainty modeling. GaussianLSS represents spatial dispersion by learning a soft depth mean and computing the variance of the depth distribution, which implicitly captures object extents. We then transform the depth distribution into 3D Gaussians and rasterize them to construct uncertainty-aware BEV features. We evaluate GaussianLSS on the nuScenes dataset, achieving state-of-the-art performance compared to unprojection-based methods. In particular, it provides significant advantages in speed, running 2.5x faster, and in memory efficiency, using 0.3x less memory compared to projection-based methods, while achieving competitive performance with only a 0.4% IoU difference.

</details>
