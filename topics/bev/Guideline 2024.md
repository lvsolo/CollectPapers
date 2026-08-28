# BEV — 2024 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Navigation Instruction Generation with BEV Perception and Large Language Models.
- **链接**: [arXiv:2407.15087](https://arxiv.org/abs/2407.15087) · 📚 被引 13
- **作者**: Sheng Fan, Rui Liu, Wenguan Wang, Yi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Navigation instruction generation, which requires embodied agents to describe the navigation routes, has been of great interest in robotics and human-computer interaction. Existing studies directly map the sequence of 2D perspective observations to route descriptions. Though straightforward, they overlook the geometric information and object semantics of the 3D environment. To address these challenges, we propose BEVInstructor, which incorporates Bird's Eye View (BEV) features into Multi-Modal Large Language Models (MLLMs) for instruction generation. Specifically, BEVInstructor constructs a PerspectiveBEVVisual Encoder for the comprehension of 3D environments through fusing BEV and perspective features. To leverage the powerful language capabilities of MLLMs, the fused representations are used as visual prompts for MLLMs, and perspective-BEV prompt tuning is proposed for parameter-efficient updating. Based on the perspective-BEV prompts, BEVInstructor further adopts an instance-guided iterative refinement pipeline, which improves the instructions in a progressive manner. BEVInstructor achieves impressive performance across diverse datasets (i.e., R2R, REVERIE, and UrbanWalk).

</details>

### LetsMap: Unsupervised Representation Learning for Label-Efficient Semantic BEV Mapping.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73636-0_7) · 📚 被引 5
- **作者**: Nikhil Gosala, Kürsat Petek, B. Ravi Kiran, Senthil Kumar Yogamani, Paulo L. J. Drews-Jr, Wolfram Burgard et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Accelerating Online Mapping and Behavior Prediction via Direct BEV Feature Attention.
- **链接**: [arXiv:2407.06683](https://arxiv.org/abs/2407.06683) · 📚 被引 8
- **作者**: Xunjiang Gu, Guanyu Song, Igor Gilitschenski, Marco Pavone, Boris Ivanovic
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding road geometry is a critical component of the autonomous vehicle (AV) stack. While high-definition (HD) maps can readily provide such information, they suffer from high labeling and maintenance costs. Accordingly, many recent works have proposed methods for estimating HD maps online from sensor data. The vast majority of recent approaches encode multi-camera observations into an intermediate representation, e.g., a bird's eye view (BEV) grid, and produce vector map elements via a decoder. While this architecture is performant, it decimates much of the information encoded in the intermediate representation, preventing downstream tasks (e.g., behavior prediction) from leveraging them. In this work, we propose exposing the rich internal features of online map estimation methods and show how they enable more tightly integrating online mapping with trajectory forecasting. In doing so, we find that directly accessing internal BEV features yields up to 73% faster inference speeds and up to 29% more accurate predictions on the real-world nuScenes dataset.

</details>

### DA-BEV: Unsupervised Domain Adaptation for Bird's Eye View Perception.
- **链接**: [arXiv:2401.08687](https://arxiv.org/abs/2401.08687) · 📚 被引 2
- **作者**: Kai Jiang, Jiaxing Huang, Weiying Xie, Jie Lei, Yunsong Li, Ling Shao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-only Bird's Eye View (BEV) has demonstrated great potential in environment perception in a 3D space. However, most existing studies were conducted under a supervised setup which cannot scale well while handling various new data. Unsupervised domain adaptive BEV, which effective learning from various unlabelled target data, is far under-explored. In this work, we design DA-BEV, the first domain adaptive camera-only BEV framework that addresses domain adaptive BEV challenges by exploiting the complementary nature of image-view features and BEV features. DA-BEV introduces the idea of query into the domain adaptation framework to derive useful information from image-view and BEV features. It consists of two query-based designs, namely, query-based adversarial learning (QAL) and query-based self-training (QST), which exploits image-view features or BEV features to regularize the adaptation of the other. Extensive experiments show that DA-BEV achieves superior domain adaptive BEV perception performance consistently across multiple datasets and tasks such as 3D object detection and 3D scene segmentation.

</details>

### Cross-View Image Geo-Localization with Panorama-BEV Co-retrieval Network.
- **链接**: [arXiv:2408.05475](https://arxiv.org/abs/2408.05475) · [代码](https://github.com/yejy53/EP-BEV) · 📚 被引 28
- **作者**: Junyan Ye, Zhutao Lv, Weijia Li, Jinhua Yu, Haote Yang, Huaping Zhong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-view geolocalization identifies the geographic location of street view images by matching them with a georeferenced satellite database. Significant challenges arise due to the drastic appearance and geometry differences between views. In this paper, we propose a new approach for cross-view image geo-localization, i.e., the Panorama-BEV Co-Retrieval Network. Specifically, by utilizing the ground plane assumption and geometric relations, we convert street view panorama images into the BEV view, reducing the gap between street panoramas and satellite imagery. In the existing retrieval of street view panorama images and satellite images, we introduce BEV and satellite image retrieval branches for collaborative retrieval. By retaining the original street view retrieval branch, we overcome the limited perception range issue of BEV representation. Our network enables comprehensive perception of both the global layout and local details around the street view capture locations. Additionally, we introduce CVGlobal, a global cross-view dataset that is closer to real-world scenarios. This dataset adopts a more realistic setup, with street view directions not aligned with satellite images. CVGlobal also includes cross-regional, cross-temporal, and street view to map retrieval tests, enabling a comprehensive evaluation of algorithm performance. Our method excels in multiple tests on common cross-view datasets such as CVUSA, CVACT, VIGOR, and our newly introduced CVGlobal, surpassing the current state-of-the-art approaches. The code and datasets can be found at \url{https://github.com/yejy53/EP-BEV}.

</details>

## 跨领域论文（完整笔记在其他领域）

- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Diffusion Model for Robust Multi-sensor Fusion in 3D Object Detection and BEV Segmentation. → [3d-detection](../3d-detection/Guideline%202024.md)
- GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- H-V2X: A Large Scale Highway Dataset for BEV Perception. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
