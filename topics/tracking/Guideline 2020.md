# Tracking — 2020 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Simultaneous Detection and Tracking with Motion Modelling for Multiple Object Tracking.
- **链接**: [arXiv:2008.08826](https://arxiv.org/abs/2008.08826) · [代码](https://github.com/shijieS/OmniMOTDataset)
- **作者**: ShiJie Sun, Naveed Akhtar, Xiangyu Song, HuanSheng Song, Ajmal Mian, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning-based Multiple Object Tracking (MOT) currently relies on off-the-shelf detectors for tracking-by-detection.This results in deep models that are detector biased and evaluations that are detector influenced. To resolve this issue, we introduce Deep Motion Modeling Network (DMM-Net) that can estimate multiple objects' motion parameters to perform joint detection and association in an end-to-end manner. DMM-Net models object features over multiple frames and simultaneously infers object classes, visibility, and their motion parameters. These outputs are readily used to update the tracklets for efficient MOT. DMM-Net achieves PR-MOTA score of 12.80 @ 120+ fps for the popular UA-DETRAC challenge, which is better performance and orders of magnitude faster. We also contribute a synthetic large-scale public dataset Omni-MOT for vehicle tracking that provides precise ground-truth annotations to eliminate the detector influence in MOT evaluation. This 14M+ frames dataset is extendable with our public script (Code at Dataset <https://github.com/shijieS/OmniMOTDataset>, Dataset Recorder <https://github.com/shijieS/OMOTDRecorder>, Omni-MOT Source <https://github.com/shijieS/DMMN>). We demonstrate the suitability of Omni-MOT for deep learning with DMMNet and also make the source code of our network public.

</details>

### Towards Real-Time Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58621-8_7)
- **作者**: Zhongdao Wang, Liang Zheng, Yixuan Liu, Yali Li, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### Segment as Points for Efficient Online Multi-Object Tracking and Segmentation.
- **链接**: [arXiv:2007.01550](https://arxiv.org/abs/2007.01550) · [代码](https://github.com/detectRecog/PointTrack)
- **作者**: Zhenbo Xu, Wei Zhang, Xiao Tan, Wei Yang, Huan Huang, Shilei Wen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current multi-object tracking and segmentation (MOTS) methods follow the tracking-by-detection paradigm and adopt convolutions for feature extraction. However, as affected by the inherent receptive field, convolution based feature extraction inevitably mixes up the foreground features and the background features, resulting in ambiguities in the subsequent instance association. In this paper, we propose a highly effective method for learning instance embeddings based on segments by converting the compact image representation to un-ordered 2D point cloud representation. Our method generates a new tracking-by-points paradigm where discriminative instance embeddings are learned from randomly selected points rather than images. Furthermore, multiple informative data modalities are converted into point-wise representations to enrich point-wise features. The resulting online MOTS framework, named PointTrack, surpasses all the state-of-the-art methods including 3D tracking methods by large margins (5.4% higher MOTSA and 18 times faster over MOTSFusion) with the near real-time speed (22 FPS). Evaluations across three datasets demonstrate both the effectiveness and efficiency of our method. Moreover, based on the observation that current MOTS datasets lack crowded scenes, we build a more challenging MOTS dataset named APOLLO MOTS with higher instance density. Both APOLLO MOTS and our codes are publicly available at https://github.com/detectRecog/PointTrack.

</details>

### SPARK: Spatial-Aware Online Incremental Attack Against Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58595-2_13) · 📚 被引 62
- **作者**: Qing Guo, Xiaofei Xie, Felix Juefei-Xu, Lei Ma, Zhongguo Li, Wanli Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020

### PG-Net: Pixel to Global Matching Network for Visual Tracking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58542-6_26) · 📚 被引 73
- **作者**: Bingyan Liao, Chenye Wang, Yayun Wang, Yaonong Wang, Jun Yin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2020
