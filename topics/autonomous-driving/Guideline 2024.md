# Autonomous Driving — 2024 Guideline

> 领域: 自动驾驶感知与系统（端到端驾驶、规划、驾驶场景理解、数据集基准）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### LaMPilot: An Open Benchmark Dataset for Autonomous Driving with Language Model Programs. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2312.04372](https://arxiv.org/abs/2312.04372) · 📚 被引 53
- **作者**: Yunsheng Ma, Can Cui, Xu Cao, Wenqian Ye, Peiran Liu, Juanwu Lu et al.
- **🏷️ 机构**: Purdue University, University of Illinois Urbana-Champaign, University of Virginia
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有自动驾驶框架难以理解和执行自发用户指令（如“超车”）的问题，提出了LaMPilot框架，将大语言模型（LLM）集成到自动驾驶系统中，通过生成代码调用功能原语来遵循用户指令。同时引入了LaMPilot-Bench，首个专门用于定量评估语言模型程序在自动驾驶中效能的基准数据集。实验表明，现成LLM在处理多样驾驶场景和遵循用户指令方面具有潜力。
- **摘要（英）**: To address the challenge of interpreting and executing spontaneous user instructions in autonomous driving, this paper proposes LaMPilot, a framework integrating LLMs into AD systems to generate code that leverages functional primitives. It also introduces LaMPilot-Bench, the first benchmark for quantitatively evaluating language model programs in AD. Experiments demonstrate the potential of off-the-shelf LLMs in handling diverse driving scenarios and following user instructions.
- **核心贡献**: 提出了LaMPilot框架和LaMPilot-Bench基准，实现LLM驱动的自动驾驶指令执行。
- **创新点**: 利用LLM生成代码来桥接用户指令与驾驶功能。
- **结果**: 实验验证了LLM在驾驶场景中的潜力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving (AD) has made significant strides in recent years. However, existing frameworks struggle to interpret and execute spontaneous user instructions, such as "overtake the car ahead." Large Language Models (LLMs) have demonstrated impressive reasoning capabilities showing potential to bridge this gap. In this paper, we present LaMPilot, a novel framework that integrates LLMs into AD systems, enabling them to follow user instructions by generating code that leverages established functional primitives. We also introduce LaMPilot-Bench, the first benchmark dataset specifically designed to quantitatively evaluate the efficacy of language model programs in AD. Adopting the LaMPilot framework, we conduct extensive experiments to assess the performance of off-the-shelf LLMs on LaMPilot-Bench. Our results demonstrate the potential of LLMs in handling diverse driving scenarios and following user instructions in driving. To facilitate further research in this area, we release our code and data at https://github.com/PurdueDigitalTwin/LaMPilot.

</details>

### HEAL-SWIN: A Vision Transformer on the Sphere. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2307.07313](https://arxiv.org/abs/2307.07313) · 📚 被引 9
- **作者**: Oscar Carlsson, Jan E. Gerken, Hampus Linander, Heiner Spieß, Fredrik Ohlsson, Christoffer Petersson et al.
- **🏷️ 机构**: Chalmers University of Tech-nology, University of Gothenburg,Department of Mathematical Sciences,Gothenburg,Sweden,SE-41296, Neural Information Processing, Science of Intelligence, Technical University Berlin,Berlin,Germany,DE-10623, Ume&#x00E5; Uni-versity,Department of Mathematics and Mathematical Statistics,Ume&#x00E5;,Sweden,SE-90187
- **会议**: CVPR 2024
- **摘要（中）**: 针对高分辨率广角鱼眼图像在平面投影中引入畸变和损失的问题，提出了HEAL-SWIN transformer，结合HEALPix网格和SWIN transformer，实现无畸变的球形数据处理。利用HEALPix的嵌套结构进行SWIN的patch和window操作，最小化计算开销。在合成和真实自动驾驶数据集上，该模型在语义分割、深度回归和分类任务上表现优越。
- **摘要（英）**: To address the distortion and loss issues when projecting high-resolution fisheye images onto planar grids, this paper proposes HEAL-SWIN, combining the HEALPix grid with the SWIN transformer for distortion-free spherical data processing. The nested structure of HEALPix enables efficient patching and windowing, minimizing computational overhead. The model demonstrates superior performance on synthetic and real automotive datasets for segmentation, depth regression, and classification.
- **核心贡献**: 提出了基于HEALPix的球形视觉transformer，适用于高分辨率鱼眼图像。
- **创新点**: 将HEALPix网格与SWIN transformer结合，实现无畸变球形处理。
- **结果**: 在多个任务上取得优于现有方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution wide-angle fisheye images are becoming more and more important for robotics applications such as autonomous driving. However, using ordinary convolutional neural networks or vision transformers on this data is problematic due to projection and distortion losses introduced when projecting to a rectangular grid on the plane. We introduce the HEAL-SWIN transformer, which combines the highly uniform Hierarchical Equal Area iso-Latitude Pixelation (HEALPix) grid used in astrophysics and cosmology with the Hierarchical Shifted-Window (SWIN) transformer to yield an efficient and flexible model capable of training on high-resolution, distortion-free spherical data. In HEAL-SWIN, the nested structure of the HEALPix grid is used to perform the patching and windowing operations of the SWIN transformer, enabling the network to process spherical representations with minimal computational overhead. We demonstrate the superior performance of our model on both synthetic and real automotive datasets, as well as a selection of other image datasets, for semantic segmentation, depth regression and classification tasks. Our code is publicly available at https://github.com/JanEGerken/HEAL-SWIN.

</details>

### RadSimReal: Bridging the Gap Between Synthetic and Real Data in Radar Object Detection With Simulation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2404.18150](https://arxiv.org/abs/2404.18150) · 📚 被引 11
- **作者**: Oded Bialer, Yuval Haitman
- **🏷️ 机构**: General Motors, Technical Center Israel
- **会议**: CVPR 2024
- **摘要（中）**: ①该论文针对雷达图像目标检测中真实标注数据难以获取的问题，尤其是在长距离和恶劣天气条件下。②提出了RadSimReal物理雷达仿真工具，能生成带标注的合成雷达图像，适用于多种雷达类型和环境条件，无需真实数据采集。③相比其他物理仿真，RadSimReal无需雷达设计细节，且运行更快。④实验表明，在RadSimReal数据上训练的模型在真实数据上评估时，性能与真实数据训练相当，甚至跨数据集测试时表现更好。
- **摘要（英）**: This paper addresses the challenge of obtaining annotated real radar data for object detection, especially in long-range and adverse weather conditions. It proposes RadSimReal, a physical radar simulation that generates synthetic radar images with annotations for various radar types and conditions without real data collection. Unlike other simulations, it requires no radar design details and has faster runtime. Models trained on RadSimReal achieve comparable performance to real-data training and even better cross-dataset results.
- **核心贡献**: 提出RadSimReal物理雷达仿真工具，生成合成数据以替代真实标注，提升检测模型泛化性。
- **创新点**: 无需雷达设计细节的物理仿真，速度快且适应多种环境。
- **结果**: 合成数据训练模型在真实数据上性能与真实训练相当，跨数据集表现更优。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection in radar imagery with neural networks shows great potential for improving autonomous driving. However, obtaining annotated datasets from real radar images, crucial for training these networks, is challenging, especially in scenarios with long-range detection and adverse weather and lighting conditions where radar performance excels. To address this challenge, we present RadSimReal, an innovative physical radar simulation capable of generating synthetic radar images with accompanying annotations for various radar types and environmental conditions, all without the need for real data collection. Remarkably, our findings demonstrate that training object detection models on RadSimReal data and subsequently evaluating them on real-world data produce performance levels comparable to models trained and tested on real data from the same dataset, and even achieves better performance when testing across different real datasets. RadSimReal offers advantages over other physical radar simulations that it does not necessitate knowledge of the radar design details, which are often not disclosed by radar suppliers, and has faster run-time. This innovative tool has the potential to advance the development of computer vision algorithms for radar-based autonomous driving applications.

</details>

### ADA-Track: End-to-End Multi-Camera 3D Multi-Object Tracking with Alternating Detection and Association. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2405.08909](https://arxiv.org/abs/2405.08909) · 📚 被引 33
- **作者**: Shuxiao Ding, Lukas Schneider, Marius Cordts, Juergen Gall
- **🏷️ 机构**: Mercedes-Benz AG,Sindelfingen, University of Bonn
- **会议**: CVPR 2024
- **摘要（中）**: 针对多相机3D多目标跟踪中检测与关联任务纠缠或分离的问题，提出ADA-Track++端到端框架，结合跟踪-by-attention和跟踪-by-detection优势。引入基于边增强交叉注意力的可学习数据关联模块，利用外观和几何特征，并设计辅助token缓解注意力归一化导致的错误关联。该模块集成到DETR-based检测器解码器中，实现检测与关联协同。
- **摘要（英）**: ADA-Track++ proposes an end-to-end framework for multi-camera 3D MOT, combining tracking-by-attention and tracking-by-detection paradigms. It introduces a learnable association module with edge-augmented cross-attention and an auxiliary token to improve association accuracy, integrated into a DETR-based detector.
- **核心贡献**: 提出ADA-Track++，端到端多相机3D MOT框架。
- **创新点**: 设计边增强交叉注意力和辅助token的关联模块。
- **结果**: 在3D MOT任务上实现检测与关联的协同提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Many query-based approaches for 3D Multi-Object Tracking (MOT) adopt the tracking-by-attention paradigm, utilizing track queries for identity-consistent detection and object queries for identity-agnostic track spawning. Tracking-by-attention, however, entangles detection and tracking queries in one embedding for both the detection and tracking task, which is sub-optimal. Other approaches resemble the tracking-by-detection paradigm and detect objects using decoupled track and detection queries followed by a subsequent association. These methods, however, do not leverage synergies between the detection and association task. Combining the strengths of both paradigms, we introduce ADA-Track++, a novel end-to-end framework for 3D MOT from multi-view cameras. We introduce a learnable data association module based on edge-augmented cross-attention, leveraging appearance and geometric features. We also propose an auxiliary token in this attention-based association module, which helps mitigate disproportionately high attention to incorrect association targets caused by attention normalization. Furthermore, we integrate this association module into the decoder layer of a DETR-based 3D detector, enabling simultaneous DETR-like query-to-image cross-attention for detection and query-to-query cross-attention for data association. By stacking these decoder layers, queries are refined for the detection and association task alternately, effectively harnessing the task dependencies. We evaluate our method on the nuScenes dataset and demonstrate the advantage of our approach compared to the two previous paradigms.

</details>

### AIDE: An Automatic Data Engine for Object Detection in Autonomous Driving. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2403.17373](https://arxiv.org/abs/2403.17373) · 📚 被引 33
- **作者**: Mingfu Liang, Jong-Chyi Su, Samuel Schulter, Sparsh Garg, Shiyu Zhao, Ying Wu et al.
- **🏷️ 机构**: Northwestern University, NEC Laboratories America, Rutgers University
- **会议**: CVPR 2024
- **摘要（中）**: 针对自动驾驶中长尾分布和罕见类别导致的感知模型性能下降问题，提出AIDE自动数据引擎，利用视觉-语言模型和大语言模型自动识别问题、高效筛选数据、自动标注并生成多样化场景验证模型，实现迭代式自我改进。相比传统人工数据标注流程，该方法显著降低了成本并提升了开放世界检测性能。在自动驾驶数据集上的基准测试表明，AIDE在减少成本的同时取得了更优的检测效果。
- **摘要（英）**: To address the long-tailed distribution and rare categories in autonomous driving perception, AIDE leverages vision-language and large language models to automatically identify issues, curate data, auto-label, and verify via scenario generation, enabling iterative self-improvement. It reduces human annotation cost while achieving superior open-world detection performance on AV benchmarks.
- **核心贡献**: 提出首个基于大模型的自动数据引擎，实现开放世界检测的闭环自改进。
- **创新点**: 利用VLM和LLM实现数据筛选、标注和验证的全自动化流程。
- **结果**: 在自动驾驶数据集上以更低成本取得更优的开放世界检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous vehicle (AV) systems rely on robust perception models as a cornerstone of safety assurance. However, objects encountered on the road exhibit a long-tailed distribution, with rare or unseen categories posing challenges to a deployed perception model. This necessitates an expensive process of continuously curating and annotating data with significant human effort. We propose to leverage recent advances in vision-language and large language models to design an Automatic Data Engine (AIDE) that automatically identifies issues, efficiently curates data, improves the model through auto-labeling, and verifies the model through generation of diverse scenarios. This process operates iteratively, allowing for continuous self-improvement of the model. We further establish a benchmark for open-world detection on AV datasets to comprehensively evaluate various learning paradigms, demonstrating our method's superior performance at a reduced cost.

</details>

### AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2402.17483](https://arxiv.org/abs/2402.17483) · 📚 被引 13
- **作者**: Tang Tao, Guangrun Wang, Yixing Lao, Peng Chen, Jie Liu, Liang Lin et al.
- **🏷️ 机构**: Shenzhen Campus of Sun Yat-sen University, University of Oxford, HKU
- **会议**: CVPR 2024
- **摘要（中）**: 针对神经隐式场中多模态融合时传感器行为不对齐、优化相互干扰的问题，提出AlignMiF几何对齐多模态隐式场。通过几何感知对齐模块和共享几何初始化模块，有效对齐不同模态的粗几何，增强LiDAR与相机数据融合。在多个数据集和场景上验证了方法的有效性。
- **摘要（英）**: To address the misalignment issue in multimodal implicit fields where optimizing one modality adversely affects another, this paper proposes AlignMiF, a geometrically aligned multimodal implicit field. It introduces Geometry-Aware Alignment (GAA) and Shared Geometry Initialization (SGI) modules to align coarse geometry across modalities, enhancing LiDAR-camera fusion. Experiments across datasets demonstrate its effectiveness.
- **核心贡献**: 提出AlignMiF，通过几何对齐模块提升LiDAR-相机联合合成性能。
- **创新点**: 设计GAA和SGI模块，实现跨模态几何对齐与共享初始化。
- **结果**: 在多个数据集上验证了融合效果的提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural implicit fields have been a de facto standard in novel view synthesis. Recently, there exist some methods exploring fusing multiple modalities within a single field, aiming to share implicit features from different modalities to enhance reconstruction performance. However, these modalities often exhibit misaligned behaviors: optimizing for one modality, such as LiDAR, can adversely affect another, like camera performance, and vice versa. In this work, we conduct comprehensive analyses on the multimodal implicit field of LiDAR-camera joint synthesis, revealing the underlying issue lies in the misalignment of different sensors. Furthermore, we introduce AlignMiF, a geometrically aligned multimodal implicit field with two proposed modules: Geometry-Aware Alignment (GAA) and Shared Geometry Initialization (SGI). These modules effectively align the coarse geometry across different modalities, significantly enhancing the fusion process between LiDAR and camera data. Through extensive experiments across various datasets and scenes, we demonstrate the effectiveness of our approach in facilitating better interaction between LiDAR and camera modalities within a unified neural field. Specifically, our proposed AlignMiF, achieves remarkable improvement over recent implicit fusion methods (+2.01 and +3.11 image PSNR on the KITTI-360 and Waymo datasets) and consistently surpasses single modality performance (13.8% and 14.2% reduction in LiDAR Chamfer Distance on the respective datasets).

</details>

### Improving Bird's Eye View Semantic Segmentation by Task Decomposition.
- **链接**: [arXiv:2404.01925](https://arxiv.org/abs/2404.01925) · 📚 被引 14
- **作者**: Tianhao Zhao, Yongcan Chen, Yu Wu, Tianyang Liu, Bo Du, Peilun Xiao et al.
- **🏷️ 机构**: Institute of Artificial Intelligence, School of Computer Science, Hubei Luojia Laboratory, Wuhan University,Wuhan,China, Didi Chuxing,China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Semantic segmentation in bird's eye view (BEV) plays a crucial role in autonomous driving. Previous methods usually follow an end-to-end pipeline, directly predicting the BEV segmentation map from monocular RGB inputs. However, the challenge arises when the RGB inputs and BEV targets from distinct perspectives, making the direct point-to-point predicting hard to optimize. In this paper, we decompose the original BEV segmentation task into two stages, namely BEV map reconstruction and RGB-BEV feature alignment. In the first stage, we train a BEV autoencoder to reconstruct the BEV segmentation maps given corrupted noisy latent representation, which urges the decoder to learn fundamental knowledge of typical BEV patterns. The second stage involves mapping RGB input images into the BEV latent space of the first stage, directly optimizing the correlations between the two views at the feature level. Our approach simplifies the complexity of combining perception and generation into distinct steps, equipping the model to handle intricate and challenging scenes effectively. Besides, we propose to transform the BEV segmentation map from the Cartesian to the polar coordinate system to establish the column-wise correspondence between RGB images and BEV maps. Moreover, our method requires neither multi-scale features nor camera intrinsic parameters for depth estimation and saves computational overhead. Extensive experiments on nuScenes and Argoverse show the effectiveness and efficiency of our method. Code is available at https://github.com/happytianhao/TaDe.

</details>

### PointBeV: A Sparse Approach to BeV Predictions.
- **链接**: [arXiv:2312.00703](https://arxiv.org/abs/2312.00703) · 📚 被引 22
- **作者**: Loïck Chambon, Éloi Zablocki, Mickaël Chen, Florent Bartoccioni, Patrick Pérez, Matthieu Cord
- **🏷️ 机构**: Valeo.ai,Paris,France, Kyutai,Paris,France
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bird's-eye View (BeV) representations have emerged as the de-facto shared space in driving applications, offering a unified space for sensor data fusion and supporting various downstream tasks. However, conventional models use grids with fixed resolution and range and face computational inefficiencies due to the uniform allocation of resources across all cells. To address this, we propose PointBeV, a novel sparse BeV segmentation model operating on sparse BeV cells instead of dense grids. This approach offers precise control over memory usage, enabling the use of long temporal contexts and accommodating memory-constrained platforms. PointBeV employs an efficient two-pass strategy for training, enabling focused computation on regions of interest. At inference time, it can be used with various memory/performance trade-offs and flexibly adjusts to new specific use cases. PointBeV achieves state-of-the-art results on the nuScenes dataset for vehicle, pedestrian, and lane segmentation, showcasing superior performance in static and temporal settings despite being trained solely with sparse signals. We will release our code along with two new efficient modules used in the architecture: Sparse Feature Pulling, designed for the effective extraction of features from images to BeV, and Submanifold Attention, which enables efficient temporal modeling. Our code is available at https://github.com/valeoai/PointBeV.

</details>

### COTR: Compact Occupancy TRansformer for Vision-Based 3D Occupancy Prediction.
- **链接**: [arXiv:2312.01919](https://arxiv.org/abs/2312.01919) · 📚 被引 49
- **作者**: Qihang Ma, Xin Tan, Yanyun Qu, Lizhuang Ma, Zhizhong Zhang, Yuan Xie
- **🏷️ 机构**: East China Normal University,Shanghai,China, Xiamen University,Fujian,China
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The autonomous driving community has shown significant interest in 3D occupancy prediction, driven by its exceptional geometric perception and general object recognition capabilities. To achieve this, current works try to construct a Tri-Perspective View (TPV) or Occupancy (OCC) representation extending from the Bird-Eye-View perception. However, compressed views like TPV representation lose 3D geometry information while raw and sparse OCC representation requires heavy but redundant computational costs. To address the above limitations, we propose Compact Occupancy TRansformer (COTR), with a geometry-aware occupancy encoder and a semantic-aware group decoder to reconstruct a compact 3D OCC representation. The occupancy encoder first generates a compact geometrical OCC feature through efficient explicit-implicit view transformation. Then, the occupancy decoder further enhances the semantic discriminability of the compact OCC representation by a coarse-to-fine semantic grouping strategy. Empirical experiments show that there are evident performance gains across multiple baselines, e.g., COTR outperforms baselines with a relative improvement of 8%-15%, demonstrating the superiority of our method.

</details>

### UnO: Unsupervised Occupancy Fields for Perception and Forecasting.
- **链接**: [arXiv:2406.08691](https://arxiv.org/abs/2406.08691) · 📚 被引 19
- **作者**: Ben Agro, Quinlan Sykora, Sergio Casas, Thomas Gilles, Raquel Urtasun
- **🏷️ 机构**: Waabi, University of Toronto
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Perceiving the world and forecasting its future state is a critical task for self-driving. Supervised approaches leverage annotated object labels to learn a model of the world -- traditionally with object detections and trajectory predictions, or temporal bird's-eye-view (BEV) occupancy fields. However, these annotations are expensive and typically limited to a set of predefined categories that do not cover everything we might encounter on the road. Instead, we learn to perceive and forecast a continuous 4D (spatio-temporal) occupancy field with self-supervision from LiDAR data. This unsupervised world model can be easily and effectively transferred to downstream tasks. We tackle point cloud forecasting by adding a lightweight learned renderer and achieve state-of-the-art performance in Argoverse 2, nuScenes, and KITTI. To further showcase its transferability, we fine-tune our model for BEV semantic occupancy forecasting and show that it outperforms the fully supervised state-of-the-art, especially when labeled data is scarce. Finally, when compared to prior state-of-the-art on spatio-temporal geometric occupancy prediction, our 4D world model achieves a much higher recall of objects from classes relevant to self-driving.

</details>

### Adaptive Fusion of Single-View and Multi-View Depth for Autonomous Driving.
- **链接**: [arXiv:2403.07535](https://arxiv.org/abs/2403.07535) · 📚 被引 43
- **作者**: Junda Cheng, Wei Yin, Kaixuan Wang, Xiaozhi Chen, Shijie Wang, Xin Yang
- **🏷️ 机构**: Huazhong University of Science and Technology, DJI Technology
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view depth estimation has achieved impressive performance over various benchmarks. However, almost all current multi-view systems rely on given ideal camera poses, which are unavailable in many real-world scenarios, such as autonomous driving. In this work, we propose a new robustness benchmark to evaluate the depth estimation system under various noisy pose settings. Surprisingly, we find current multi-view depth estimation methods or single-view and multi-view fusion methods will fail when given noisy pose settings. To address this challenge, we propose a single-view and multi-view fused depth estimation system, which adaptively integrates high-confident multi-view and single-view results for both robust and accurate depth estimations. The adaptive fusion module performs fusion by dynamically selecting high-confidence regions between two branches based on a wrapping confidence map. Thus, the system tends to choose the more reliable branch when facing textureless scenes, inaccurate calibration, dynamic objects, and other degradation or challenging conditions. Our method outperforms state-of-the-art multi-view and fusion methods under robustness testing. Furthermore, we achieve state-of-the-art performance on challenging benchmarks (KITTI and DDAD) when given accurate pose estimations. Project website: https://github.com/Junda24/AFNet/.

</details>

### Holistic Autonomous Driving Understanding by Bird'View Injected Multi-Modal Large Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01297) · 📚 被引 41
- **作者**: Xinpeng Ding, Jianhua Han, Hang Xu, Xiaodan Liang, Wei Zhang, Xiaomeng Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Huawei Noah&#x0027;s Ark Lab, Sun Yat-Sen University
- **会议**: CVPR 2024

### Physical 3D Adversarial Attacks against Monocular Depth Estimation in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02308) · 📚 被引 57
- **作者**: Junhao Zheng, Chenhao Lin, Jiahao Sun, Zhengyu Zhao, Qian Li, Chao Shen
- **🏷️ 机构**: Xi&#x0027;an Jiaotong University,Xi&#x0027;an,China,710049
- **会议**: CVPR 2024

### Multi-Object Tracking in the Dark.
- **链接**: [arXiv:2405.06600](https://arxiv.org/abs/2405.06600)
- **作者**: Xinzhe Wang, Kang Ma, Qiankun Liu, Yunhao Zou, Ying Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Low-light scenes are prevalent in real-world applications (e.g. autonomous driving and surveillance at night). Recently, multi-object tracking in various practical use cases have received much attention, but multi-object tracking in dark scenes is rarely considered. In this paper, we focus on multi-object tracking in dark scenes. To address the lack of datasets, we first build a Low-light Multi-Object Tracking (LMOT) dataset. LMOT provides well-aligned low-light video pairs captured by our dual-camera system, and high-quality multi-object tracking annotations for all videos. Then, we propose a low-light multi-object tracking method, termed as LTrack. We introduce the adaptive low-pass downsample module to enhance low-frequency components of images outside the sensor noises. The degradation suppression learning strategy enables the model to learn invariant information under noise disturbance and image quality degradation. These components improve the robustness of multi-object tracking in dark scenes. We conducted a comprehensive analysis of our LMOT dataset and proposed LTrack. Experimental results demonstrate the superiority of the proposed method and its competitiveness in real night low-light scenes. Dataset and Code: https: //github.com/ying-fu/LMOT

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a lightweight and scalable Regional Point-Language Contrastive learning framework, namely \textbf{RegionPLC}, for open-world 3D scene understanding, aiming to identify and recognize open-set objects and categories. Specifically, based on our empirical studies, we introduce a 3D-aware SFusion strategy that fuses 3D vision-language pairs derived from multiple 2D foundation models, yielding high-quality, dense region-level language descriptions without human 3D annotations. Subsequently, we devise a region-aware point-discriminative contrastive learning objective to enable robust and effective 3D learning from dense regional language supervision. We carry out extensive experiments on ScanNet, ScanNet200, and nuScenes datasets, and our model outperforms prior 3D open-world scene understanding approaches by an average of 17.2\% and 9.1\% for semantic and instance segmentation, respectively, while maintaining greater scalability and lower resource demands. Furthermore, our method has the flexibility to be effortlessly integrated with language models to enable open-ended grounded 3D reasoning without extra task-specific training. Code is available at https://github.com/CVMI-Lab/PLA.

</details>

### Driving Into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving.
- **链接**: [arXiv:2311.17918](https://arxiv.org/abs/2311.17918) · 📚 被引 116
- **作者**: Yuqi Wang, Jiawei He, Lue Fan, Hongxin Li, Yuntao Chen, Zhaoxiang Zhang
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences (UCAS), Institute of Automation, Chinese Academy of Sciences (CASIA),CRIPAC, MAIS, Centre for Artificial Intelligence and Robotics (HKISI_CAS)
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

</details>

### DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes.
- **链接**: [arXiv:2312.07920](https://arxiv.org/abs/2312.07920) · 📚 被引 280
- **作者**: Xiaoyu Zhou, Zhiwei Lin, Xiaojun Shan, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University, Google Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present DrivingGaussian, an efficient and effective framework for surrounding dynamic autonomous driving scenes. For complex scenes with moving objects, we first sequentially and progressively model the static background of the entire scene with incremental static 3D Gaussians. We then leverage a composite dynamic Gaussian graph to handle multiple moving objects, individually reconstructing each object and restoring their accurate positions and occlusion relationships within the scene. We further use a LiDAR prior for Gaussian Splatting to reconstruct scenes with greater details and maintain panoramic consistency. DrivingGaussian outperforms existing methods in dynamic driving scene reconstruction and enables photorealistic surround-view synthesis with high-fidelity and multi-camera consistency. Our project page is at: https://github.com/VDIGPKU/DrivingGaussian.

</details>

### On the Road to Portability: Compressing End-to-End Motion Planner for Autonomous Driving.
- **链接**: [arXiv:2403.01238](https://arxiv.org/abs/2403.01238) · 📚 被引 14
- **作者**: Kaituo Feng, Changsheng Li, Dongchun Ren, Ye Yuan, Guoren Wang
- **🏷️ 机构**: Beijing Institute of Technology, ALLRIDE.AI
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end motion planning models equipped with deep neural networks have shown great potential for enabling full autonomous driving. However, the oversized neural networks render them impractical for deployment on resource-constrained systems, which unavoidably requires more computational time and resources during reference.To handle this, knowledge distillation offers a promising approach that compresses models by enabling a smaller student model to learn from a larger teacher model. Nevertheless, how to apply knowledge distillation to compress motion planners has not been explored so far. In this paper, we propose PlanKD, the first knowledge distillation framework tailored for compressing end-to-end motion planners. First, considering that driving scenes are inherently complex, often containing planning-irrelevant or even noisy information, transferring such information is not beneficial for the student planner. Thus, we design an information bottleneck based strategy to only distill planning-relevant information, rather than transfer all information indiscriminately. Second, different waypoints in an output planned trajectory may hold varying degrees of importance for motion planning, where a slight deviation in certain crucial waypoints might lead to a collision. Therefore, we devise a safety-aware waypoint-attentive distillation module that assigns adaptive weights to different waypoints based on the importance, to encourage the student to accurately mimic more crucial waypoints, thereby improving overall safety. Experiments demonstrate that our PlanKD can boost the performance of smaller planners by a large margin, and significantly reduce their reference time.

</details>

### Bootstrapping Autonomous Driving Radars with Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01422) · 📚 被引 17
- **作者**: Yiduo Hao, Sohrab Madani, Junfeng Guan, Mohammed Alloulah, Saurabh Gupta, Haitham Hassanieh
- **🏷️ 机构**: University of Cambridge, UIUC, EPFL
- **会议**: CVPR 2024

### Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving.
- **链接**: [arXiv:2404.04804](https://arxiv.org/abs/2404.04804) · 📚 被引 74
- **作者**: Jinlong Li, Baolu Li, Zhengzhong Tu, Xinyu Liu, Qing Guo, Felix Juefei-Xu et al.
- **🏷️ 机构**: Cleveland State University, University of Texas at Austin, Centre for Frontier AI Research (CFAR), A&#x002A;STAR
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-centric perception systems for autonomous driving have gained considerable attention recently due to their cost-effectiveness and scalability, especially compared to LiDAR-based systems. However, these systems often struggle in low-light conditions, potentially compromising their performance and safety. To address this, our paper introduces LightDiff, a domain-tailored framework designed to enhance the low-light image quality for autonomous driving applications. Specifically, we employ a multi-condition controlled diffusion model. LightDiff works without any human-collected paired data, leveraging a dynamic data degradation process instead. It incorporates a novel multi-condition adapter that adaptively controls the input weights from different modalities, including depth maps, RGB images, and text captions, to effectively illuminate dark scenes while maintaining context consistency. Furthermore, to align the enhanced images with the detection model's knowledge, LightDiff employs perception-specific scores as rewards to guide the diffusion training process through reinforcement learning. Extensive experiments on the nuScenes datasets demonstrate that LightDiff can significantly improve the performance of several state-of-the-art 3D detectors in night-time conditions while achieving high visual quality scores, highlighting its potential to safeguard autonomous driving.

</details>

### Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving?
- **链接**: [arXiv:2312.03031](https://arxiv.org/abs/2312.03031) · 📚 被引 86
- **作者**: Zhiqi Li, Zhiding Yu, Shiyi Lan, Jiahan Li, Jan Kautz, Tong Lu et al.
- **🏷️ 机构**: Nanjing University,National Key Lab for Novel Software Technology, NVIDIA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> End-to-end autonomous driving recently emerged as a promising research direction to target autonomy from a full-stack perspective. Along this line, many of the latest works follow an open-loop evaluation setting on nuScenes to study the planning behavior. In this paper, we delve deeper into the problem by conducting thorough analyses and demystifying more devils in the details. We initially observed that the nuScenes dataset, characterized by relatively simple driving scenarios, leads to an under-utilization of perception information in end-to-end models incorporating ego status, such as the ego vehicle's velocity. These models tend to rely predominantly on the ego vehicle's status for future path planning. Beyond the limitations of the dataset, we also note that current metrics do not comprehensively assess the planning quality, leading to potentially biased conclusions drawn from existing benchmarks. To address this issue, we introduce a new metric to evaluate whether the predicted trajectories adhere to the road. We further propose a simple baseline able to achieve competitive results without relying on perception annotations. Given the current limitations on the benchmark and metrics, we suggest the community reassess relevant prevailing research and be cautious whether the continued pursuit of state-of-the-art would yield convincing and universal conclusions. Code and models are available at \url{https://github.com/NVlabs/BEV-Planner}

</details>

### VLP: Vision Language Planning for Autonomous Driving.
- **链接**: [arXiv:2401.05577](https://arxiv.org/abs/2401.05577) · 📚 被引 85
- **作者**: Chenbin Pan, Burhaneddin Yaman, Tommaso Nesti, Abhirup Mallik, Alessandro Gabriele Allievi, Senem Velipasalar et al.
- **🏷️ 机构**: Syracuse University, Bosch Research North America &#x0026; Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Autonomous driving is a complex and challenging task that aims at safe motion planning through scene understanding and reasoning. While vision-only autonomous driving methods have recently achieved notable performance, through enhanced scene understanding, several key issues, including lack of reasoning, low generalization performance and long-tail scenarios, still need to be addressed. In this paper, we present VLP, a novel Vision-Language-Planning framework that exploits language models to bridge the gap between linguistic understanding and autonomous driving. VLP enhances autonomous driving systems by strengthening both the source memory foundation and the self-driving car's contextual understanding. VLP achieves state-of-the-art end-to-end planning performance on the challenging NuScenes dataset by achieving 35.9\% and 60.5\% reduction in terms of average L2 error and collision rates, respectively, compared to the previous best method. Moreover, VLP shows improved performance in challenging long-tail scenarios and strong generalization capabilities when faced with new urban environments.

</details>

### Adversarial Backdoor Attack by Naturalistic Data Poisoning on Trajectory Prediction in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01410) · 📚 被引 16
- **作者**: Mozhgan Pourkeshavarz, Mohammad Sabokrou, Amir Rasouli
- **🏷️ 机构**: Noah&#x0027;s Ark Lab,Huawei,Canada, Okinawa Institute of Science and Technology (OIST)
- **会议**: CVPR 2024

### CaDeT: A Causal Disentanglement Approach for Robust Trajectory Prediction in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01409) · 📚 被引 25
- **作者**: Mozhgan Pourkeshavarz, Junrui Zhang, Amir Rasouli
- **🏷️ 机构**: Noah&#x0027;s Ark Lab,Huawei,Canada
- **会议**: CVPR 2024

### NeuRAD: Neural Rendering for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01411) · 📚 被引 90
- **作者**: Adam Tonderski, Carl Lindström, Georg Hess, William Ljungbergh, Lennart Svensson, Christoffer Petersson
- **🏷️ 机构**: Zenseact, Chalmers University of Technology
- **会议**: CVPR 2024

### Editable Scene Simulation for Autonomous Driving via Collaborative LLM-Agents.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01428) · 📚 被引 78
- **作者**: Yuxi Wei, Zi Wang, Yifan Lu, Chenxin Xu, Changxing Liu, Hao Zhao et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Carnegie Mellon University, Tsinghua University
- **会议**: CVPR 2024

### Panacea: Panoramic and Controllable Video Generation for Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00659)
- **作者**: Yuqing Wen, Yucheng Zhao, Yingfei Liu, Fan Jia, Yanhui Wang, Chong Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### SeFlow: A Self-supervised Scene Flow Method in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73232-4_20) · 📚 被引 21
- **作者**: Qingwen Zhang, Yi Yang, Peizheng Li, Olov Andersson, Patric Jensfelt
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

### PACER+: On-Demand Pedestrian Animation Controller in Driving Scenarios.
- **链接**: [arXiv:2404.19722](https://arxiv.org/abs/2404.19722) · 📚 被引 12
- **作者**: Jingbo Wang, Zhengyi Luo, Ye Yuan, Yixuan Li, Bo Dai
- **🏷️ 机构**: Shanghai AI Lab, Carnegie Mellon University, NVIDIA
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the challenge of content diversity and controllability in pedestrian simulation for driving scenarios. Recent pedestrian animation frameworks have a significant limitation wherein they primarily focus on either following trajectory [46] or the content of the reference video [57], consequently overlooking the potential diversity of human motion within such scenarios. This limitation restricts the ability to generate pedestrian behaviors that exhibit a wider range of variations and realistic motions and therefore restricts its usage to provide rich motion content for other components in the driving simulation system, e.g., suddenly changed motion to which the autonomous vehicle should respond. In our approach, we strive to surpass the limitation by showcasing diverse human motions obtained from various sources, such as generated human motions, in addition to following the given trajectory. The fundamental contribution of our framework lies in combining the motion tracking task with trajectory following, which enables the tracking of specific motion parts (e.g., upper body) while simultaneously following the given trajectory by a single policy. This way, we significantly enhance both the diversity of simulated human motion within the given scenario and the controllability of the content, including language-based control. Our framework facilitates the generation of a wide range of human motions, contributing to greater realism and adaptability in pedestrian simulations for driving scenarios. More information is on our project page https://wangjingbo1219.github.io/papers/CVPR2024_PACER_PLUS/PACERPLUSPage.html .

</details>

### Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset.
- **链接**: [arXiv:2406.09383](https://arxiv.org/abs/2406.09383) · 📚 被引 16
- **作者**: Yiming Li, Zhiheng Li, Nuo Chen, Moonjun Gong, Zonglin Lyu, Zehong Wang et al.
- **🏷️ 机构**: New York University
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale datasets have fueled recent advancements in AI-based autonomous vehicle research. However, these datasets are usually collected from a single vehicle's one-time pass of a certain location, lacking multiagent interactions or repeated traversals of the same place. Such information could lead to transformative enhancements in autonomous vehicles' perception, prediction, and planning capabilities. To bridge this gap, in collaboration with the self-driving company May Mobility, we present the MARS dataset which unifies scenarios that enable MultiAgent, multitraveRSal, and multimodal autonomous vehicle research. More specifically, MARS is collected with a fleet of autonomous vehicles driving within a certain geographical area. Each vehicle has its own route and different vehicles may appear at nearby locations. Each vehicle is equipped with a LiDAR and surround-view RGB cameras. We curate two subsets in MARS: one facilitates collaborative driving with multiple vehicles simultaneously present at the same location, and the other enables memory retrospection through asynchronous traversals of the same location by multiple vehicles. We conduct experiments in place recognition and neural reconstruction. More importantly, MARS introduces new research opportunities and challenges such as multitraversal 3D reconstruction, multiagent perception, and unsupervised object discovery. Our data and codes can be found at https://ai4ce.github.io/MARS/.

</details>

### Dualad: Disentangling the Dynamic and Static World for End-to-End Driving.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01395) · 📚 被引 7
- **作者**: Simon Doll, Niklas Hanselmann, Lukas Schneider, Richard Schulz, Marius Cordts, Markus Enzweiler et al.
- **🏷️ 机构**: Mercedes-Benz AG, Esslingen University of Applied Sciences, University of T&#x00FC;bingen
- **会议**: CVPR 2024

### LMDrive: Closed-Loop End-to-End Driving with Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01432) · 📚 被引 178
- **作者**: Hao Shao, Yuxuan Hu, Letian Wang, Guanglu Song, Steven L. Waslander, Yu Liu et al.
- **🏷️ 机构**: CUHKMMLab, CPII under InnoHK, University of Toronto
- **会议**: CVPR 2024

### Self-Supervised Class-Agnostic Motion Prediction with Spatial and Temporal Consistency Regularizations.
- **链接**: [arXiv:2403.13261](https://arxiv.org/abs/2403.13261) · 📚 被引 5
- **作者**: Kewei Wang, Yizheng Wu, Jun Cen, Zhiyu Pan, Xingyi Li, Zhe Wang et al.
- **🏷️ 机构**: School of AIA, Huazhong University of Science and Technology, S-Lab, Nanyang Technological University, SenseTime Research
- **会议**: CVPR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The perception of motion behavior in a dynamic environment holds significant importance for autonomous driving systems, wherein class-agnostic motion prediction methods directly predict the motion of the entire point cloud. While most existing methods rely on fully-supervised learning, the manual labeling of point cloud data is laborious and time-consuming. Therefore, several annotation-efficient methods have been proposed to address this challenge. Although effective, these methods rely on weak annotations or additional multi-modal data like images, and the potential benefits inherent in the point cloud sequence are still underexplored. To this end, we explore the feasibility of self-supervised motion prediction with only unlabeled LiDAR point clouds. Initially, we employ an optimal transport solver to establish coarse correspondences between current and future point clouds as the coarse pseudo motion labels. Training models directly using such coarse labels leads to noticeable spatial and temporal prediction inconsistencies. To mitigate these issues, we introduce three simple spatial and temporal regularization losses, which facilitate the self-supervised training process effectively. Experimental results demonstrate the significant superiority of our approach over the state-of-the-art self-supervised methods.

</details>

## 跨领域论文（完整笔记在其他领域）

- CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. → [3d-detection](../3d-detection/Guideline%202024.md)
- Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications. → [3d-detection](../3d-detection/Guideline%202024.md)
- Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors. → [3d-detection](../3d-detection/Guideline%202024.md)
- SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects. → [3d-detection](../3d-detection/Guideline%202024.md)
- RadarDistill: Boosting Radar-Based Object Detection Performance via Knowledge Distillation from LiDAR Features. → [3d-detection](../3d-detection/Guideline%202024.md)
- Weak-to-Strong 3D Object Detection with X-Ray Distillation. → [3d-detection](../3d-detection/Guideline%202024.md)
- PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- GAFusion: Adaptive Fusing LiDAR and Camera with Multiple Guidance for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Multi-View Attentive Contextualization for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Learning Occupancy for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-Based Roadside 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Commonsense Prototype for Outdoor Unsupervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- IS-Fusion: Instance-Scene Collaborative Fusion for Multimodal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Pseudo Label Refinery for Unsupervised Domain Adaptation on Cross-Dataset 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- CRKD: Enhanced Camera-Radar Object Detection with Cross-Modality Knowledge Distillation. → [3d-detection](../3d-detection/Guideline%202024.md)
- Visual Point Cloud Forecasting Enables Scalable Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202024.md)
- SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- SparseOcc: Rethinking Sparse Latent Representation for Vision-Based Semantic Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202024.md)
- UniPAD: A Universal Pre-Training Paradigm for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202024.md)
