# BEV — 2024 Guideline

> 领域: 鸟瞰图感知（BEV 特征、BEV 检测/分割/预测）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks. **⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2407.13517](https://arxiv.org/abs/2407.13517) · 📚 被引 18
- **作者**: Sehwan Choi, Jungho Kim, Hongjae Shin, Jun Won Choi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对在线高精地图构建中BEV分割掩码与地图实例预测之间不一致的问题，提出Mask2Map方法，端到端预测场景中地图实例的类别和有序点集。方法包含实例级掩码预测网络（IMPNet）和掩码驱动地图预测网络（MMPNet），IMPNet生成掩码感知查询和BEV分割掩码以捕获全局语义，MMPNet通过位置查询生成器和几何特征提取器增强局部上下文。为解决网络间不一致，提出网络间去噪训练方法，统一IMPNet和MMPNet的匹配过程。相比已有方法，Mask2Map通过掩码引导的查询和几何特征提升了地图构建的精度和鲁棒性。
- **摘要（英）**: This paper addresses the inconsistency between BEV segmentation masks and map instance prediction in online HD map construction. It proposes Mask2Map, an end-to-end method with an instance-level mask prediction network and a mask-driven map prediction network, enhanced by inter-network denoising training. This improves accuracy and robustness by leveraging mask-aware queries and geometric features.
- **核心贡献**: 提出掩码驱动的高精地图构建框架，并引入网络间去噪训练解决预测不一致问题。
- **创新点**: 利用BEV分割掩码生成点级几何特征，并通过去噪训练统一子网络匹配。
- **结果**: 在公开数据集上验证了地图构建性能的提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce Mask2Map, a novel end-to-end online HD map construction method designed for autonomous driving applications. Our approach focuses on predicting the class and ordered point set of map instances within a scene, represented in the bird's eye view (BEV). Mask2Map consists of two primary components: the Instance-Level Mask Prediction Network (IMPNet) and the Mask-Driven Map Prediction Network (MMPNet). IMPNet generates Mask-Aware Queries and BEV Segmentation Masks to capture comprehensive semantic information globally. Subsequently, MMPNet enhances these query features using local contextual information through two submodules: the Positional Query Generator (PQG) and the Geometric Feature Extractor (GFE). PQG extracts instance-level positional queries by embedding BEV positional information into Mask-Aware Queries, while GFE utilizes BEV Segmentation Masks to generate point-level geometric features. However, we observed limited performance in Mask2Map due to inter-network inconsistency stemming from different predictions to Ground Truth (GT) matching between IMPNet and MMPNet. To tackle this challenge, we propose the Inter-network Denoising Training method, which guides the model to denoise the output affected by both noisy GT queries and perturbed GT Segmentation Masks. Our evaluation conducted on nuScenes and Argoverse2 benchmarks demonstrates that Mask2Map achieves remarkable performance improvements over previous state-of-the-art methods, with gains of 10.1% mAP and 4.1 mAP, respectively. Our code can be found at https://github.com/SehwanChoi0307/Mask2Map.

</details>

### DA-BEV: Unsupervised Domain Adaptation for Bird's Eye View Perception. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2401.08687](https://arxiv.org/abs/2401.08687) · 📚 被引 2
- **作者**: Kai Jiang, Jiaxing Huang, Weiying Xie, Jie Lei, Yunsong Li, Ling Shao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对相机-only BEV感知在无监督域适应中未充分探索的问题，提出DA-BEV，首个域自适应相机-only BEV框架。方法利用图像视图特征和BEV特征的互补性，引入查询机制到域适应框架，包含基于查询的对抗学习（QAL）和基于查询的自训练（QST），分别利用图像视图或BEV特征来正则化另一方的适应。相比现有监督BEV方法，DA-BEV在无标注目标域上实现了有效的域适应。在多个数据集和任务（如3D检测和3D场景分割）上，DA-BEV一致性地取得了优越的域适应性能。
- **摘要（英）**: This paper addresses the under-explored problem of unsupervised domain adaptation for camera-only BEV perception. It proposes DA-BEV, the first domain adaptive BEV framework, using query-based adversarial learning and self-training to exploit complementary image-view and BEV features. This achieves superior adaptation performance across multiple datasets and tasks.
- **核心贡献**: 提出首个相机-only BEV域适应框架，通过查询机制实现图像视图和BEV特征的互补适应。
- **创新点**: 设计基于查询的对抗学习和自训练策略，双向正则化不同视图特征的适应。
- **结果**: 在多个数据集和任务上一致性地取得了优越的域适应性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Camera-only Bird's Eye View (BEV) has demonstrated great potential in environment perception in a 3D space. However, most existing studies were conducted under a supervised setup which cannot scale well while handling various new data. Unsupervised domain adaptive BEV, which effective learning from various unlabelled target data, is far under-explored. In this work, we design DA-BEV, the first domain adaptive camera-only BEV framework that addresses domain adaptive BEV challenges by exploiting the complementary nature of image-view features and BEV features. DA-BEV introduces the idea of query into the domain adaptation framework to derive useful information from image-view and BEV features. It consists of two query-based designs, namely, query-based adversarial learning (QAL) and query-based self-training (QST), which exploits image-view features or BEV features to regularize the adaptation of the other. Extensive experiments show that DA-BEV achieves superior domain adaptive BEV perception performance consistently across multiple datasets and tasks such as 3D object detection and 3D scene segmentation.

</details>

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

## 🆕 增量新增

### SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2403.20318](https://arxiv.org/abs/2403.20318) · 📚 被引 11
- **作者**: Abhinav Kumar, Yuliang Guo, Xinyu Huang, Liu Ren, Xiaoming Liu
- **🏷️ 机构**: Michigan State University, Bosch Research North America, Bosch Center for AI
- **会议**: CVPR 2024
- **摘要（中）**: 针对单目3D检测在大物体上性能下降的问题，指出深度回归损失对大物体噪声敏感是失败原因。通过数学证明，dice损失在大物体上比回归损失具有更好的噪声鲁棒性和收敛性。基于此提出SeaBird方法，将BEV分割与3D检测结合，并使用dice损失训练分割头。实验表明SeaBird在大物体检测上显著提升，同时保持小物体性能。
- **摘要（英）**: To address the performance drop of monocular 3D detection on large objects, this paper identifies the sensitivity of depth regression losses to noise as the cause. It mathematically proves that dice loss offers superior noise robustness and convergence for large objects. The proposed SeaBird integrates BEV segmentation with 3D detection, trained with dice loss, significantly improving large object detection while maintaining performance on smaller ones.
- **核心贡献**: 揭示了回归损失对大物体的敏感性，并提出基于dice损失的SeaBird方法。
- **创新点**: 数学证明dice损失在大物体上的优势，并用于BEV分割辅助检测。
- **结果**: 在大物体检测上显著提升，同时保持小物体性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D detectors achieve remarkable performance on cars and smaller objects. However, their performance drops on larger objects, leading to fatal accidents. Some attribute the failures to training data scarcity or their receptive field requirements of large objects. In this paper, we highlight this understudied problem of generalization to large objects. We find that modern frontal detectors struggle to generalize to large objects even on nearly balanced datasets. We argue that the cause of failure is the sensitivity of depth regression losses to noise of larger objects. To bridge this gap, we comprehensively investigate regression and dice losses, examining their robustness under varying error levels and object sizes. We mathematically prove that the dice loss leads to superior noise-robustness and model convergence for large objects compared to regression losses for a simplified case. Leveraging our theoretical insights, we propose SeaBird (Segmentation in Bird's View) as the first step towards generalizing to large objects. SeaBird effectively integrates BEV segmentation on foreground objects for 3D detection, with the segmentation head trained with the dice loss. SeaBird achieves SoTA results on the KITTI-360 leaderboard and improves existing detectors on the nuScenes leaderboard, particularly for large objects. Code and models at https://github.com/abhi1kumar/SeaBird

</details>

### BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2312.01696](https://arxiv.org/abs/2312.01696) · 📚 被引 55
- **作者**: Zhenxin Li, Shiyi Lan, José M. Álvarez, Zuxuan Wu
- **🏷️ 机构**: School of CS, Fudan University,Shanghai Key Lab of Intell. Info. Processing, NVIDIA
- **会议**: CVPR 2024
- **摘要（中）**: 针对查询式transformer解码器在相机3D检测中超越传统密集BEV方法的现象，指出密集BEV框架在深度估计和物体定位上仍有优势。提出了BEVNeXt，通过CRF调制深度估计、长时时间聚合和两阶段解码器增强密集BEV框架。在nuScenes测试集上达到64.2 NDS，超越BEV和查询式方法，实现最先进性能。
- **摘要（英）**: To address the rise of query-based decoders surpassing dense BEV methods in camera-based 3D detection, this paper argues that dense BEV frameworks retain advantages in depth estimation and localization. It proposes BEVNeXt with CRF-modulated depth estimation, long-term temporal aggregation, and a two-stage decoder. BEVNeXt achieves 64.2 NDS on nuScenes, outperforming both BEV and query-based methods.
- **核心贡献**: 提出了BEVNeXt，通过多项增强组件提升密集BEV检测性能。
- **创新点**: 引入CRF调制深度估计和长时时间聚合。
- **结果**: 在nuScenes上取得最先进NDS。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, the rise of query-based Transformer decoders is reshaping camera-based 3D object detection. These query-based decoders are surpassing the traditional dense BEV (Bird's Eye View)-based methods. However, we argue that dense BEV frameworks remain important due to their outstanding abilities in depth estimation and object localization, depicting 3D scenes accurately and comprehensively. This paper aims to address the drawbacks of the existing dense BEV-based 3D object detectors by introducing our proposed enhanced components, including a CRF-modulated depth estimation module enforcing object-level consistencies, a long-term temporal aggregation module with extended receptive fields, and a two-stage object decoder combining perspective techniques with CRF-modulated depth embedding. These enhancements lead to a "modernized" dense BEV framework dubbed BEVNeXt. On the nuScenes benchmark, BEVNeXt outperforms both BEV-based and query-based frameworks under various settings, achieving a state-of-the-art result of 64.2 NDS on the nuScenes test set. Code will be available at \url{https://github.com/woxihuanjiangguo/BEVNeXt}.

</details>

### BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2406.08785](https://arxiv.org/abs/2406.08785) · 📚 被引 23
- **作者**: Wenjie Wang, Yehao Lu, Guangcong Zheng, Shuigen Zhan, Xiaoqing Ye, Zichang Tan et al.
- **🏷️ 机构**: College of Computer Science and Technology, Zhejiang University, Polytechnic Institute, Zhejiang University, Baidu
- **会议**: CVPR 2024
- **摘要（中）**: 针对视觉路侧3D检测中体素池化的位置近似误差问题，提出BEVSpread，将每个视锥点视为源，将图像特征传播到周围BEV网格并赋予自适应权重。设计了根据距离和深度动态控制衰减速度的权重函数，并通过CUDA并行加速保持推理速度。在两大路侧基准上，BEVSpread作为即插即用模块显著提升了现有基于视锥的BEV方法性能。
- **摘要（英）**: BEVSpread reduces position approximation error in voxel pooling for roadside 3D detection by spreading features from each frustum point to surrounding BEV grids with adaptive weights, controlled by distance and depth. It significantly improves existing frustum-based BEV methods on roadside benchmarks with comparable inference speed.
- **核心贡献**: 提出BEVSpread体素池化策略，减少位置误差并提升检测性能。
- **创新点**: 自适应权重传播和CUDA加速实现高效特征散布。
- **结果**: 在路侧基准上显著提升检测精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-based roadside 3D object detection has attracted rising attention in autonomous driving domain, since it encompasses inherent advantages in reducing blind spots and expanding perception range. While previous work mainly focuses on accurately estimating depth or height for 2D-to-3D mapping, ignoring the position approximation error in the voxel pooling process. Inspired by this insight, we propose a novel voxel pooling strategy to reduce such error, dubbed BEVSpread. Specifically, instead of bringing the image features contained in a frustum point to a single BEV grid, BEVSpread considers each frustum point as a source and spreads the image features to the surrounding BEV grids with adaptive weights. To achieve superior propagation performance, a specific weight function is designed to dynamically control the decay speed of the weights according to distance and depth. Aided by customized CUDA parallel acceleration, BEVSpread achieves comparable inference time as the original voxel pooling. Extensive experiments on two large-scale roadside benchmarks demonstrate that, as a plug-in, BEVSpread can significantly improve the performance of existing frustum-based BEV methods by a large margin of (1.12, 5.26, 3.01) AP in vehicle, pedestrian and cyclist.

</details>

### From a Bird's Eye View to See: Joint Camera and Subject Registration without the Camera Calibration. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2212.09298](https://arxiv.org/abs/2212.09298) · 📚 被引 10
- **作者**: Zekun Qian, Ruize Han, Wei Feng, Song Wang
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University, Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences, University of South Carolina
- **会议**: CVPR 2024
- **摘要（中）**: 针对无相机标定情况下多视角相机和主体在鸟瞰图中的联合注册问题，该论文提出了一种端到端框架。它通过视图变换主体检测模块将第一视角转换为虚拟BEV，利用几何变换估计相机位置和方向，并结合空间和外观信息聚合主体。在合成数据集上验证了方法的有效性，为无标定BEV感知提供了新思路。
- **摘要（英）**: This paper tackles the challenging problem of joint camera and subject registration in BEV without pre-given calibration, by proposing an end-to-end framework with a view-transform detection module, geometric-based camera registration, and spatial-appearance aggregation. Experiments on a synthetic dataset demonstrate remarkable effectiveness, offering a novel approach for uncalibrated BEV perception.
- **核心贡献**: 提出无相机标定的BEV联合注册框架。
- **创新点**: 结合视图变换和几何估计实现相机与主体注册。
- **结果**: 在合成数据集上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle a new problem of multi-view camera and subject registration in the bird's eye view (BEV) without pre-given camera calibration. This is a very challenging problem since its only input is several RGB images from different first-person views (FPVs) for a multi-person scene, without the BEV image and the calibration of the FPVs, while the output is a unified plane with the localization and orientation of both the subjects and cameras in a BEV. We propose an end-to-end framework solving this problem, whose main idea can be divided into following parts: i) creating a view-transform subject detection module to transform the FPV to a virtual BEV including localization and orientation of each pedestrian, ii) deriving a geometric transformation based method to estimate camera localization and view direction, i.e., the camera registration in a unified BEV, iii) making use of spatial and appearance information to aggregate the subjects into the unified BEV. We collect a new large-scale synthetic dataset with rich annotations for evaluation. The experimental results show the remarkable effectiveness of our proposed method.

</details>

### Improving Bird's Eye View Semantic Segmentation by Task Decomposition. **⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2404.01925](https://arxiv.org/abs/2404.01925) · 📚 被引 14
- **作者**: Tianhao Zhao, Yongcan Chen, Yu Wu, Tianyang Liu, Bo Du, Peilun Xiao et al.
- **🏷️ 机构**: Institute of Artificial Intelligence, School of Computer Science, Hubei Luojia Laboratory, Wuhan University,Wuhan,China, Didi Chuxing,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对单目RGB输入到BEV分割的端到端预测因视角差异难以优化的问题，提出将任务分解为BEV地图重建和RGB-BEV特征对齐两个阶段。第一阶段训练BEV自编码器从带噪潜表示重建分割图，学习BEV模式先验；第二阶段将RGB映射到BEV潜空间，在特征层面优化跨视角相关性。该方法简化了感知与生成的耦合，提升了复杂场景的处理能力，并引入极坐标变换进一步优化。
- **摘要（英）**: This paper decomposes BEV semantic segmentation into BEV map reconstruction and RGB-BEV feature alignment stages to address the optimization difficulty from perspective differences. A BEV autoencoder learns prior patterns, and a mapping stage aligns features across views. The approach improves handling of complex scenes and incorporates polar coordinate transformation.
- **核心贡献**: 提出了一种两阶段任务分解方法，将BEV分割拆解为重建和对齐，降低了端到端学习的难度。
- **创新点**: 创新性地利用BEV自编码器学习先验，并在潜空间进行跨视角特征对齐。
- **结果**: 在复杂场景下提升了BEV分割的鲁棒性和性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semantic segmentation in bird's eye view (BEV) plays a crucial role in autonomous driving. Previous methods usually follow an end-to-end pipeline, directly predicting the BEV segmentation map from monocular RGB inputs. However, the challenge arises when the RGB inputs and BEV targets from distinct perspectives, making the direct point-to-point predicting hard to optimize. In this paper, we decompose the original BEV segmentation task into two stages, namely BEV map reconstruction and RGB-BEV feature alignment. In the first stage, we train a BEV autoencoder to reconstruct the BEV segmentation maps given corrupted noisy latent representation, which urges the decoder to learn fundamental knowledge of typical BEV patterns. The second stage involves mapping RGB input images into the BEV latent space of the first stage, directly optimizing the correlations between the two views at the feature level. Our approach simplifies the complexity of combining perception and generation into distinct steps, equipping the model to handle intricate and challenging scenes effectively. Besides, we propose to transform the BEV segmentation map from the Cartesian to the polar coordinate system to establish the column-wise correspondence between RGB images and BEV maps. Moreover, our method requires neither multi-scale features nor camera intrinsic parameters for depth estimation and saves computational overhead. Extensive experiments on nuScenes and Argoverse show the effectiveness and efficiency of our method. Code is available at https://github.com/happytianhao/TaDe.

</details>

### PointBeV: A Sparse Approach to BeV Predictions. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2312.00703](https://arxiv.org/abs/2312.00703) · 📚 被引 22
- **作者**: Loïck Chambon, Éloi Zablocki, Mickaël Chen, Florent Bartoccioni, Patrick Pérez, Matthieu Cord
- **🏷️ 机构**: Valeo.ai,Paris,France, Kyutai,Paris,France
- **会议**: CVPR 2024
- **摘要（中）**: 针对传统BEV模型使用固定分辨率网格导致计算效率低的问题，提出PointBeV，一种基于稀疏BEV单元的稀疏分割模型。该方法通过两遍训练策略聚焦感兴趣区域，推理时可灵活调整内存/性能权衡，并支持长时序上下文。在nuScenes数据集上，车辆、行人和车道分割任务均达到最先进水平，在静态和时序设置下表现优异。
- **摘要（英）**: PointBeV proposes a sparse BEV segmentation model operating on sparse cells instead of dense grids, enabling efficient memory usage and flexible inference trade-offs. It achieves state-of-the-art results on nuScenes for vehicle, pedestrian, and lane segmentation, with superior performance in static and temporal settings.
- **核心贡献**: 提出了稀疏BEV分割模型，实现了内存可控和性能可调的感知方案。
- **创新点**: 创新性地使用稀疏BEV单元和两遍训练策略，替代传统密集网格。
- **结果**: 在nuScenes上达到最先进性能，并支持长时序和低内存场景。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bird's-eye View (BeV) representations have emerged as the de-facto shared space in driving applications, offering a unified space for sensor data fusion and supporting various downstream tasks. However, conventional models use grids with fixed resolution and range and face computational inefficiencies due to the uniform allocation of resources across all cells. To address this, we propose PointBeV, a novel sparse BeV segmentation model operating on sparse BeV cells instead of dense grids. This approach offers precise control over memory usage, enabling the use of long temporal contexts and accommodating memory-constrained platforms. PointBeV employs an efficient two-pass strategy for training, enabling focused computation on regions of interest. At inference time, it can be used with various memory/performance trade-offs and flexibly adjusts to new specific use cases. PointBeV achieves state-of-the-art results on the nuScenes dataset for vehicle, pedestrian, and lane segmentation, showcasing superior performance in static and temporal settings despite being trained solely with sparse signals. We will release our code along with two new efficient modules used in the architecture: Sparse Feature Pulling, designed for the effective extraction of features from images to BeV, and Submanifold Attention, which enables efficient temporal modeling. Our code is available at https://github.com/valeoai/PointBeV.

</details>

### BerfScene: Bev-conditioned Equivariant Radiance Fields for Infinite 3D Scene Generation. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2312.02136](https://arxiv.org/abs/2312.02136) · 📚 被引 1
- **作者**: Qihang Zhang, Yinghao Xu, Yujun Shen, Bo Dai, Bolei Zhou, Ceyuan Yang
- **🏷️ 机构**: CUHK, Stanford, Ant Group
- **会议**: CVPR 2024
- **摘要（中）**: 针对大规模3D场景生成中复杂空间配置和多尺度物体的问题，提出BerfScene，结合BEV地图引导的等变辐射场。通过BEV地图控制物体操作，并利用位置编码和低通滤波器实现等变性，支持生成无限规模的3D场景。实验在多个3D场景数据集上验证了有效性。
- **摘要（英）**: BerfScene introduces a BEV-conditioned equivariant radiance field for large-scale 3D scene generation, enabling object manipulation via BEV maps and infinite scene synthesis through equivariance. Experiments on 3D scene datasets demonstrate effectiveness.
- **核心贡献**: 提出了BEV条件等变辐射场，支持大规模和无限3D场景生成。
- **创新点**: 创新性地利用BEV地图引导辐射场，实现场景的等变生成和拼接。
- **结果**: 在3D场景数据集上验证了生成效果和可控性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating large-scale 3D scenes cannot simply apply existing 3D object synthesis technique since 3D scenes usually hold complex spatial configurations and consist of a number of objects at varying scales. We thus propose a practical and efficient 3D representation that incorporates an equivariant radiance field with the guidance of a bird's-eye view (BEV) map. Concretely, objects of synthesized 3D scenes could be easily manipulated through steering the corresponding BEV maps. Moreover, by adequately incorporating positional encoding and low-pass filters into the generator, the representation becomes equivariant to the given BEV map. Such equivariance allows us to produce large-scale, even infinite-scale, 3D scenes via synthesizing local scenes and then stitching them with smooth consistency. Extensive experiments on 3D scene datasets demonstrate the effectiveness of our approach. Our project website is at https://zqh0253.github.io/BerfScene/.

</details>

### Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving? **⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2312.03031](https://arxiv.org/abs/2312.03031) · 📚 被引 86
- **作者**: Zhiqi Li, Zhiding Yu, Shiyi Lan, Jiahan Li, Jan Kautz, Tong Lu et al.
- **🏷️ 机构**: Nanjing University,National Key Lab for Novel Software Technology, NVIDIA
- **会议**: CVPR 2024
- **摘要（中）**: 这篇论文针对端到端自动驾驶在开放循环评估中过度依赖自我状态而忽视感知信息的问题。作者通过分析nuScenes数据集，发现简单驾驶场景导致模型主要利用自我车辆速度等状态进行路径规划，感知信息未被充分利用。为此，他们引入新指标评估预测轨迹是否遵循道路，并提出一个简单基线，在不依赖感知标注的情况下达到竞争性结果。该工作揭示了现有基准的局限性，并推动更全面的规划质量评估。
- **摘要（英）**: This paper addresses the over-reliance on ego status in open-loop end-to-end autonomous driving, where perception information is underutilized in simple nuScenes scenarios. The authors analyze this issue, introduce a new metric to evaluate road adherence of predicted trajectories, and propose a simple baseline achieving competitive results without perception annotations. The work highlights benchmark limitations and promotes more comprehensive planning evaluation.
- **核心贡献**: 揭示nuScenes基准中自我状态主导规划的问题，并提出道路遵循新指标。
- **创新点**: 新评估指标和无需感知标注的简单基线。
- **结果**: 简单基线达到竞争性结果，新指标提供更全面评估。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving recently emerged as a promising research direction to target autonomy from a full-stack perspective. Along this line, many of the latest works follow an open-loop evaluation setting on nuScenes to study the planning behavior. In this paper, we delve deeper into the problem by conducting thorough analyses and demystifying more devils in the details. We initially observed that the nuScenes dataset, characterized by relatively simple driving scenarios, leads to an under-utilization of perception information in end-to-end models incorporating ego status, such as the ego vehicle's velocity. These models tend to rely predominantly on the ego vehicle's status for future path planning. Beyond the limitations of the dataset, we also note that current metrics do not comprehensively assess the planning quality, leading to potentially biased conclusions drawn from existing benchmarks. To address this issue, we introduce a new metric to evaluate whether the predicted trajectories adhere to the road. We further propose a simple baseline able to achieve competitive results without relying on perception annotations. Given the current limitations on the benchmark and metrics, we suggest the community reassess relevant prevailing research and be cautious whether the continued pursuit of state-of-the-art would yield convincing and universal conclusions. Code and models are available at \url{https://github.com/NVlabs/BEV-Planner}

</details>

### Diffusion Model for Robust Multi-sensor Fusion in 3D Object Detection and BEV Segmentation. **⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73113-6_14) · 📚 被引 20
- **作者**: Duy-Tho Le, Hengcan Shi, Jianfei Cai, Hamid Rezatofighi
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对多传感器融合在3D检测和BEV分割中鲁棒性不足的问题，提出基于扩散模型的融合方法，利用扩散过程增强特征表示的鲁棒性。该方法通过生成式建模处理传感器噪声和不确定性，提升融合质量。相比传统确定性融合，扩散模型能更好地建模数据分布，提高在噪声环境下的性能。实验表明该方法在3D检测和BEV分割任务上均取得改进。
- **摘要（英）**: This paper tackles the robustness issue in multi-sensor fusion for 3D detection and BEV segmentation by introducing a diffusion model-based approach. It leverages generative modeling to handle sensor noise and uncertainty, improving fusion quality. The method outperforms deterministic fusion baselines, demonstrating enhanced performance in noisy conditions.
- **核心贡献**: 提出基于扩散模型的多传感器融合框架，增强3D检测和BEV分割鲁棒性。
- **创新点**: 利用扩散模型的生成能力处理传感器噪声。
- **结果**: 在3D检测和BEV分割任务上取得性能提升。

### GraphBEV: Towards Robust BEV Feature Alignment for Multi-modal 3D Object Detection. **⭐⭐⭐⭐** (相关度: 93%)
- **链接**: [arXiv:2403.11848](https://arxiv.org/abs/2403.11848) · 📚 被引 63
- **作者**: Ziying Song, Lei Yang, Shaoqing Xu, Lin Liu, Dongyang Xu, Caiyan Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对LiDAR和相机标定不准确导致BEV特征错位的问题，提出GraphBEV框架，包含局部对齐模块和全局对齐模块。局部对齐通过图匹配利用邻域感知深度特征，全局对齐修正LiDAR和相机BEV特征的错位。在nuScenes验证集上达到70.1% mAP，超过BEV Fusion 1.6%，且在错位噪声下优于BEV Fusion 8.3%，展示了强大的鲁棒性。
- **摘要（英）**: This paper addresses the misalignment between LiDAR and camera BEV features caused by inaccurate calibration. It proposes GraphBEV with a Local Align module using graph matching for neighbor-aware depth features and a Global Align module for rectifying feature misalignment. The method achieves 70.1% mAP on nuScenes, surpassing BEV Fusion by 1.6%, and by 8.3% under misalignment noise.
- **核心贡献**: 提出图匹配的局部和全局对齐模块，增强多模态BEV融合鲁棒性。
- **创新点**: 利用图匹配处理深度估计误差和特征错位。
- **结果**: 在nuScenes上达到SOTA性能，并在错位噪声下显著优于基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Integrating LiDAR and camera information into Bird's-Eye-View (BEV) representation has emerged as a crucial aspect of 3D object detection in autonomous driving. However, existing methods are susceptible to the inaccurate calibration relationship between LiDAR and the camera sensor. Such inaccuracies result in errors in depth estimation for the camera branch, ultimately causing misalignment between LiDAR and camera BEV features. In this work, we propose a robust fusion framework called Graph BEV. Addressing errors caused by inaccurate point cloud projection, we introduce a Local Align module that employs neighbor-aware depth features via Graph matching. Additionally, we propose a Global Align module to rectify the misalignment between LiDAR and camera BEV features. Our Graph BEV framework achieves state-of-the-art performance, with an mAP of 70.1\%, surpassing BEV Fusion by 1.6\% on the nuscenes validation set. Importantly, our Graph BEV outperforms BEV Fusion by 8.3\% under conditions with misalignment noise.

</details>

### Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2407.08569](https://arxiv.org/abs/2407.08569) · 📚 被引 9
- **作者**: Ruiyang Zhang, Hu Zhang, Hang Yu, Zhedong Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: 针对无监督3D检测中LiDAR点云稀疏导致远距离和小物体检测性能差的问题，提出LiSe方法，是早期尝试将LiDAR与2D图像集成用于无监督3D检测的工作之一。方法上，设计自步学习流程，包含自适应采样和弱模型聚合策略，利用RGB图像提供精确的2D定位线索来补充LiDAR数据。自适应采样动态调整训练中伪标签的分布，防止模型过拟合于易检测样本（如近处和大物体），确保不同尺度和距离的平衡学习。相比仅使用LiDAR的无监督方法，LiSe在远距离和小物体检测上显著提升了性能。
- **摘要（英）**: This paper tackles the challenge of unsupervised 3D detection where sparse LiDAR point clouds degrade performance on distant and small objects. It introduces LiSe, an early attempt integrating LiDAR with 2D images, using a self-paced learning pipeline with adaptive sampling and weak model aggregation to leverage RGB cues for precise 2D localization. This balances learning across object scales and distances, significantly improving detection of hard samples.
- **核心贡献**: 提出首个融合LiDAR和2D图像的无监督3D检测框架，并设计自步学习策略平衡难易样本。
- **创新点**: 引入自适应采样和弱模型聚合机制，动态调整伪标签分布以应对模态差异。
- **结果**: 在远距离和小物体检测上相比仅LiDAR方法有显著性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The unsupervised 3D object detection is to accurately detect objects in unstructured environments with no explicit supervisory signals. This task, given sparse LiDAR point clouds, often results in compromised performance for detecting distant or small objects due to the inherent sparsity and limited spatial resolution. In this paper, we are among the early attempts to integrate LiDAR data with 2D images for unsupervised 3D detection and introduce a new method, dubbed LiDAR-2D Self-paced Learning (LiSe). We argue that RGB images serve as a valuable complement to LiDAR data, offering precise 2D localization cues, particularly when scarce LiDAR points are available for certain objects. Considering the unique characteristics of both modalities, our framework devises a self-paced learning pipeline that incorporates adaptive sampling and weak model aggregation strategies. The adaptive sampling strategy dynamically tunes the distribution of pseudo labels during training, countering the tendency of models to overfit easily detected samples, such as nearby and large-sized objects. By doing so, it ensures a balanced learning trajectory across varying object scales and distances. The weak model aggregation component consolidates the strengths of models trained under different pseudo label distributions, culminating in a robust and powerful final model. Experimental evaluations validate the efficacy of our proposed LiSe method, manifesting significant improvements of +7.1% AP$_{BEV}$ and +3.4% AP$_{3D}$ on nuScenes, and +8.3% AP$_{BEV}$ and +7.4% AP$_{3D}$ on Lyft compared to existing techniques.

</details>

### CALICO: Self-Supervised Camera-LiDAR Contrastive Pre-training for BEV Perception. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2306.00349](https://arxiv.org/abs/2306.00349)
- **作者**: Jiachen Sun, Haizhong Zheng, Qingzhao Zhang, Atul Prakash, Zhuoqing Mao, Chaowei Xiao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: 针对多模态BEV感知缺乏统一自监督预训练框架的问题，提出CALICO，将对比目标应用于LiDAR和相机骨干网络。方法包含两个阶段：点-区域对比（PRC）和区域感知蒸馏（RAD），PRC在LiDAR模态上平衡区域级和场景级表示学习，RAD实现自训练教师模型的对比蒸馏。相比现有单模态预训练方法，CALICO统一了多模态预训练，显著提升了3D检测和BEV地图分割任务性能。实验表明，CALICO在多个任务上大幅超越基线，验证了其有效性。
- **摘要（英）**: This paper addresses the lack of a unified self-supervised pretraining framework for multimodal BEV perception. It proposes CALICO, applying contrastive objectives to both LiDAR and camera backbones via point-region contrast and region-aware distillation. This significantly improves performance on 3D detection and BEV map segmentation, outperforming baselines.
- **核心贡献**: 提出首个统一的多模态BEV自监督预训练框架，结合点-区域对比和区域感知蒸馏。
- **创新点**: 设计两阶段对比学习策略，在LiDAR和相机模态上实现区域级和场景级表示对齐。
- **结果**: 在3D检测和BEV地图分割任务上显著超越基线性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perception is crucial in the realm of autonomous driving systems, where bird's eye view (BEV)-based architectures have recently reached state-of-the-art performance. The desirability of self-supervised representation learning stems from the expensive and laborious process of annotating 2D and 3D data. Although previous research has investigated pretraining methods for both LiDAR and camera-based 3D object detection, a unified pretraining framework for multimodal BEV perception is missing. In this study, we introduce CALICO, a novel framework that applies contrastive objectives to both LiDAR and camera backbones. Specifically, CALICO incorporates two stages: point-region contrast (PRC) and region-aware distillation (RAD). PRC better balances the region- and scene-level representation learning on the LiDAR modality and offers significant performance improvement compared to existing methods. RAD effectively achieves contrastive distillation on our self-trained teacher model. CALICO's efficacy is substantiated by extensive evaluations on 3D object detection and BEV map segmentation tasks, where it delivers significant performance improvements. Notably, CALICO outperforms the baseline method by 10.5% and 8.6% on NDS and mAP. Moreover, CALICO boosts the robustness of multimodal 3D object detection against adversarial attacks and corruption. Additionally, our framework can be tailored to different backbones and heads, positioning it as a promising approach for multimodal BEV perception.

</details>

### DV-3DLane: End-to-end Multi-modal 3D Lane Detection with Dual-view Representation. **⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2406.16072](https://arxiv.org/abs/2406.16072)
- **作者**: Yueru Luo, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: 针对单目3D车道检测中深度损失和光照变化导致精度下降的问题，提出DV-3DLane，一种端到端双视图多模态3D车道检测框架，融合图像和LiDAR点云。方法在透视视图（PV）和鸟瞰视图（BEV）双视图空间中学习多模态特征，包含三个设计：双向特征融合策略、统一查询生成方法、3D双视图可变形注意力机制。相比单目方法，DV-3DLane利用LiDAR几何线索实现精确定位，在公开基准OpenLane上验证了有效性和效率。
- **摘要（英）**: This paper addresses the depth loss and lighting variation issues in monocular 3D lane detection. It proposes DV-3DLane, an end-to-end dual-view multimodal framework fusing images and LiDAR, with bidirectional feature fusion, unified query generation, and 3D dual-view deformable attention. This leverages geometric cues for accurate detection, validated on OpenLane.
- **核心贡献**: 提出双视图多模态3D车道检测框架，通过双向融合和可变形注意力提升精度。
- **创新点**: 设计3D双视图可变形注意力机制，在PV和BEV空间中聚合判别性特征。
- **结果**: 在OpenLane基准上验证了有效性和效率。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate 3D lane estimation is crucial for ensuring safety in autonomous driving. However, prevailing monocular techniques suffer from depth loss and lighting variations, hampering accurate 3D lane detection. In contrast, LiDAR points offer geometric cues and enable precise localization. In this paper, we present DV-3DLane, a novel end-to-end Dual-View multi-modal 3D Lane detection framework that synergizes the strengths of both images and LiDAR points. We propose to learn multi-modal features in dual-view spaces, i.e., perspective view (PV) and bird's-eye-view (BEV), effectively leveraging the modal-specific information. To achieve this, we introduce three designs: 1) A bidirectional feature fusion strategy that integrates multi-modal features into each view space, exploiting their unique strengths. 2) A unified query generation approach that leverages lane-aware knowledge from both PV and BEV spaces to generate queries. 3) A 3D dual-view deformable attention mechanism, which aggregates discriminative features from both PV and BEV spaces into queries for accurate 3D lane detection. Extensive experiments on the public benchmark, OpenLane, demonstrate the efficacy and efficiency of DV-3DLane. It achieves state-of-the-art performance, with a remarkable 11.2 gain in F1 score and a substantial 53.5% reduction in errors. The code is available at \url{https://github.com/JMoonr/dv-3dlane}.

</details>

### Map It Anywhere: Empowering BEV Map Prediction using Large-scale Public Datasets. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/76218e28957e72ffddcd1c3e1e800043-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Cherie Ho, Jiaye Zou, Omar Alama, Sai Mitheran Jagadesh Kumar, Cheng-Yu Chiang, Taneesh Gupta et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①针对BEV地图预测依赖昂贵标注数据、难以扩展至大规模场景的问题。②提出利用大规模公开数据集（如nuScenes、Argoverse等）进行BEV地图预测的通用方法，通过跨数据集迁移和统一标注格式增强泛化能力。③相比仅使用单一数据集训练，该方法能利用更多样化的数据分布提升地图预测的鲁棒性和覆盖范围。④摘要未提供具体数值，但强调在多个公开数据集上验证了有效性。
- **摘要（英）**: This work tackles the high annotation cost in BEV map prediction by leveraging large-scale public datasets. It proposes a method to unify labels across datasets and enable cross-dataset training, improving generalization and robustness. The approach demonstrates competitive performance on multiple benchmarks, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出利用大规模公开数据集增强BEV地图预测泛化能力的框架。
- **创新点**: 通过跨数据集标注统一和联合训练策略提升模型适应性。
- **结果**: 在多个公开数据集上验证了地图预测性能的提升。

## 跨领域论文（完整笔记在其他领域）

- FSD-BEV: Foreground Self-distillation for Multi-view 3D Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- SAMFusion: Sensor-Adaptive Multimodal Fusion for 3D Object Detection in Adverse Weather. → [multimodal](../multimodal/Guideline%202024.md)
- SimPB: A Single Model for 2D and 3D Object Detection from Multiple Cameras. → [3d-detection](../3d-detection/Guideline%202024.md)
- CRT-Fusion: Camera, Radar, Temporal Fusion Using Motion Information for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Autonomous Driving with Spiking Neural Networks. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)

### RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01414)
- **作者**: Zhiwei Lin, Zhe Liu, Zhongyu Xia, Xinhao Wang, Yongtao Wang, Shengxiang Qi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对雷达-相机融合在BEV空间中的对齐和特征融合问题，雷达点稀疏且噪声大，相机图像密集但缺乏深度。②提出RCBEVDet，在BEV视角下设计雷达-相机融合网络，利用雷达的深度信息和相机的语义信息互补。③相比早期融合或后期融合，RCBEVDet在BEV空间进行深度融合，更好地处理了模态差异。④在nuScenes数据集上，RCBEVDet在3D检测精度上优于现有雷达-相机融合方法，尤其在恶劣天气和低光照条件下鲁棒性更强。
- **摘要（英）**: This paper addresses the alignment and feature fusion challenges in radar-camera fusion within BEV space, where radar points are sparse and noisy while camera images are dense but lack depth. It proposes RCBEVDet, a network that fuses radar and camera features in BEV, leveraging radar depth and camera semantics. Compared to early or late fusion, RCBEVDet performs deep fusion in BEV, better handling modality differences. On nuScenes, it outperforms existing radar-camera fusion methods in 3D detection accuracy, with improved robustness in adverse weather and low-light conditions.
- **核心贡献**: 提出BEV空间下的雷达-相机深度融合方法，提升3D检测鲁棒性。
- **创新点**: 在BEV视角下设计多模态融合，有效结合雷达深度与相机语义。
- **结果**: 在nuScenes上精度优于现有融合方法，恶劣条件下鲁棒性更强。

<!-- COMPLETE v1 papers=21 -->
