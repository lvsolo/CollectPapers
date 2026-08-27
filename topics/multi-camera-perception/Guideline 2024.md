# Multi-camera Perception — 2024 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 69 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### PKU-DyMVHumans: A Multi-View Video Benchmark for High-Fidelity Dynamic Human Modeling. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2403.16080](https://arxiv.org/abs/2403.16080) · 📚 被引 16
- **作者**: Xiaoyun Zheng, Liwei Liao, Xufeng Li, Jianbo Jiao, Rongjie Wang, Feng Gao et al.
- **🏷️ 机构**: Peking University Shenzhen Graduate School, City University of Hong Kong, University of Birmingham
- **会议**: CVPR 2024
- **摘要（中）**: 针对动态场景中高保真人体重建与渲染因松散衣物和复杂姿态而效果不佳的问题，该论文提出了PKU-DyMVHumans数据集，包含由56个以上同步相机捕获的820万帧、32个受试者、45种场景的多视角视频。该数据集提供了高细节外观和真实运动，并搭建了基于NeRF的基准框架，便于评估最新方法。其贡献在于填补了高质量动态人体数据集的空白，为相关研究提供了标准化测试平台。
- **摘要（英）**: This paper addresses the challenge of high-fidelity dynamic human reconstruction and rendering, particularly for loose clothing and complex poses, by introducing PKU-DyMVHumans, a large-scale multi-view video dataset with 8.2 million frames from over 56 synchronized cameras across 45 scenarios. It provides a benchmark framework based on NeRF, enabling standardized evaluation of state-of-the-art methods. The key contribution is filling the gap in high-quality dynamic human datasets for advancing research.
- **核心贡献**: 构建了大规模多视角动态人体数据集及NeRF基准框架。
- **创新点**: 提供高细节动态人体数据，覆盖松散衣物和复杂姿态。
- **结果**: 为动态人体重建提供了标准化测试平台，促进算法评估。

### MTMMC: A Large-Scale Real-World Multi-Modal Camera Tracking Benchmark. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2403.20225](https://arxiv.org/abs/2403.20225) · 📚 被引 6
- **作者**: Sanghyun Woo, Kwanyong Park, Inkyu Shin, Myungchul Kim, In So Kweon
- **🏷️ 机构**: New York University, ETRI, KAIST
- **会议**: CVPR 2024
- **摘要（中）**: 针对现有跨摄像头多目标跟踪数据集多为合成或受控环境、难以模拟真实动态的问题，该论文提出了MTMMC，一个大规模真实世界多模态数据集，包含16个多模态相机在校园和工厂两种环境、不同时间天气季节下捕获的长视频序列。该数据集提供RGB和热成像两种模态，增强了跟踪精度，并作为现有数据集的超集，为研究复杂真实场景下的多摄像头跟踪提供了挑战性测试平台。
- **摘要（英）**: This paper tackles the limitation of existing multi-target multi-camera tracking datasets being synthetic or controlled, by introducing MTMMC, a large-scale real-world dataset with long videos from 16 multi-modal cameras in campus and factory environments across various conditions. It includes RGB and thermal modalities to improve tracking accuracy and serves as a superset of existing datasets, providing a challenging benchmark for real-world complexities.
- **核心贡献**: 构建了大规模真实世界多模态多摄像头跟踪数据集。
- **创新点**: 引入RGB和热成像双模态，覆盖多样环境条件。
- **结果**: 提供了更具挑战性的基准，促进真实场景跟踪研究。

### PointOBB: Learning Oriented Object Detection via Single Point Supervision. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2311.14757](https://arxiv.org/abs/2311.14757) · 📚 被引 52
- **作者**: Junwei Luo, Xue Yang, Yi Yu, Qingyun Li, Junchi Yan, Yansheng Li
- **🏷️ 机构**: Wuhan University, Southeast University, Harbin Institute of Technology
- **会议**: CVPR 2024
- **摘要（中）**: 针对单点监督目标检测仅生成水平框而忽略遥感图像中常用旋转框的问题，该论文提出了PointOBB，首个基于单点生成旋转框的方法。它通过协同利用原始、缩放和旋转/翻转三种视图，设计尺度增强模块和角度获取模块，分别使用尺度敏感一致性损失和自监督学习预测角度，并采用渐进多视图切换策略。实验表明该方法在旋转目标检测上有效，显著降低了标注成本。
- **摘要（英）**: This paper addresses the gap in single point-supervised detection that only generates horizontal boxes, by proposing PointOBB, the first method for oriented object detection from single point supervision. It leverages three views (original, resized, rotated/flipped) with a scale augmentation module and an angle acquisition module, using a scale-sensitive consistency loss and self-supervised learning, achieving effective oriented box generation with reduced annotation cost.
- **核心贡献**: 提出首个单点监督的旋转框生成方法PointOBB。
- **创新点**: 利用多视图协作和自监督学习预测物体角度。
- **结果**: 在旋转目标检测上取得有效结果，降低标注成本。

### CN-RMA: Combined Network with Ray Marching Aggregation for 3D Indoor Object Detection from Multi-View Images. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02015) · 📚 被引 8
- **作者**: Guanlin Shen, Jingwei Huang, Zhihua Hu, Bin Wang
- **🏷️ 机构**: School of Software, Tsinghua University,China, Tencent,China, Nanjing University of Information Science and Technology,China
- **会议**: CVPR 2024
- **摘要（中）**: 针对多视角图像三维室内目标检测中特征聚合不充分的问题，该论文提出了CN-RMA，一种结合网络与光线行进聚合的方法。该方法通过光线行进技术有效聚合多视角特征，提升三维检测精度。实验在室内数据集上验证了其有效性，但摘要信息有限，具体改进和效果未详细说明。
- **摘要（英）**: This paper addresses insufficient feature aggregation in multi-view 3D indoor object detection by proposing CN-RMA, a combined network with ray marching aggregation. It uses ray marching to effectively fuse multi-view features, improving detection accuracy, though specific details and quantitative results are limited in the abstract.
- **核心贡献**: 提出光线行进聚合的多视角三维检测网络。
- **创新点**: 将光线行进技术用于多视角特征融合。
- **结果**: 在室内检测任务上提升了精度。

### Contrastive Pre-Training with Multi-View Fusion for No-Reference Point Cloud Quality Assessment. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2403.10066](https://arxiv.org/abs/2403.10066) · 📚 被引 28
- **作者**: Ziyu Shan, Yujie Zhang, Qi Yang, Haichen Yang, Yiling Xu, Jenq-Neng Hwang et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Tencent, University of Washington
- **会议**: CVPR 2024
- **摘要（中）**: 针对无参考点云质量评估中标注数据稀缺和泛化性差的问题，该论文提出了CoPA，一种针对点云质量评估的对比预训练框架。它通过将不同失真的点云投影为图像并混合局部补丁生成锚点，利用质量感知对比损失进行预训练，并在微调阶段提出语义引导的多视角融合模块。实验表明该方法在多个数据集上提升了性能，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses the scarcity of labeled data and poor generalization in no-reference point cloud quality assessment by proposing CoPA, a contrastive pre-training framework. It generates anchors by projecting distorted point clouds into images and mixing patches, using a quality-aware contrastive loss, and introduces a semantic-guided multi-view fusion module in fine-tuning, improving performance though specific numbers are not provided.
- **核心贡献**: 提出针对点云质量评估的对比预训练框架CoPA。
- **创新点**: 利用多失真混合图像生成锚点进行质量感知预训练。
- **结果**: 提升了无参考点云质量评估的性能和泛化性。

### View-Category Interactive Sharing Transformer for Incomplete Multi-View Multi-Label Learning. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02593) · 📚 被引 17
- **作者**: Shilong Ou, Zhe Xue, Yawen Li, Meiyu Liang, Yuanqiang Cai, Junjiang Wu
- **🏷️ 机构**: Beijing Universitxsy of Posts and Telecommunications,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对不完整多视图多标签学习中的视图交互问题。②提出视图-类别交互共享Transformer，以处理缺失视图和标签相关性。③通过共享交互机制增强跨视图信息融合。④摘要缺失，无法提供具体效果数据。
- **摘要（英）**: This paper tackles incomplete multi-view multi-label learning by proposing a view-category interactive sharing transformer to handle missing views and label correlations. It enhances cross-view information fusion via shared interaction mechanisms. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出视图-类别交互共享Transformer用于不完整多视图学习。
- **创新点**: 共享交互机制整合视图和类别信息。
- **结果**: 未提供具体效果数据。

### Multiview Aerial Visual Recognition (MAVREC): Can Multi-View Improve Aerial Visual Perception? **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2312.04548](https://arxiv.org/abs/2312.04548) · 📚 被引 9
- **作者**: Aritra Dutta, Srijan Das, Jacob Nielsen, Rajatsubhra Chakraborty, Mubarak Shah
- **🏷️ 机构**: AI Initiative, UCF, UNC Charlotte, IMADA, SDU
- **会议**: CVPR 2024
- **摘要（中）**: ①针对现有无人机航拍数据集规模小、分辨率低、缺乏多样性，导致地面视角训练的模型在航拍感知中性能不佳的问题。②提出MAVREC数据集，包含约2.5小时2.7K视频、超50万帧和110万标注框，同步记录地面和无人机视角。③该数据集是最大的地面和航拍视角数据集，在无人机数据集中规模第四。④通过广泛基准测试，识别了多视角对航拍感知的影响。
- **摘要（英）**: This paper addresses the lack of diverse and large-scale aerial datasets by introducing MAVREC, a video dataset with synchronized ground and drone views, containing 2.5 hours of 2.7K video, 0.5 million frames, and 1.1 million bounding boxes. It is the largest ground-aerial dataset and fourth largest drone dataset. Benchmarking reveals insights into multi-view aerial perception.
- **核心贡献**: 构建大规模多视角航拍数据集MAVREC。
- **创新点**: 同步地面和无人机视角，提供丰富场景多样性。
- **结果**: 提供最大规模地面-航拍数据集，支持感知研究。

### Learning to Select Views for Efficient Multi-View Understanding. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01903) · 📚 被引 5
- **作者**: Yunzhong Hou, Stephen Gould, Liang Zheng
- **🏷️ 机构**: Australian National University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视图理解中视图选择效率低的问题。②提出学习选择视图的方法，以优化多视图理解效率。③通过可学习策略减少冗余视图。④摘要缺失，无法提供具体效果数据。
- **摘要（英）**: This paper addresses inefficient view selection in multi-view understanding by learning to select informative views. It aims to reduce redundancy via a learnable strategy. Specific results are unavailable due to missing abstract.
- **核心贡献**: 提出学习式视图选择方法。
- **创新点**: 可学习策略优化视图选择。
- **结果**: 未提供具体效果数据。

### MVD-Fusion: Single-view 3D via Depth-consistent Multi-view Generation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2404.03656](https://arxiv.org/abs/2404.03656) · 📚 被引 24
- **作者**: Hanzhe Hu, Zhizhuo Zhou, Varun Jampani, Shubham Tulsiani
- **🏷️ 机构**: Carnegie Mellon University, Stanford University, Stability AI
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单视图3D推理中多视图生成不一致、需蒸馏的问题。②提出MVD-Fusion方法，通过生成多视图一致的RGB-D图像进行3D推理，利用深度估计实现重投影条件保持一致性。③相比蒸馏方法和现有生成方法，直接生成一致多视图，避免蒸馏步骤。④在Objaverse和CO3D数据集上，合成精度优于最先进方法，并评估了深度预测的几何质量。
- **摘要（英）**: This paper addresses inconsistency in multi-view generation for single-view 3D inference by proposing MVD-Fusion, which generates multi-view consistent RGB-D images using a diffusion model with depth-based reprojection conditioning. It avoids distillation by directly generating consistent views. The method outperforms state-of-the-art on Objaverse and CO3D, with improved synthesis and geometry quality.
- **核心贡献**: 提出深度一致的多视图生成方法，实现高效单视图3D推理。
- **创新点**: 利用深度估计进行重投影条件，确保多视图一致性。
- **结果**: 在多个数据集上超越现有方法。

### Learn from View Correlation: An Anchor Enhancement Strategy for Multi-View Clustering. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02471) · 📚 被引 52
- **作者**: Suyuan Liu, Ke Liang, Zhibin Dong, Siwei Wang, Xihong Yang, Sihang Zhou et al.
- **🏷️ 机构**: National University of Defense Technology,Changsha,China, Intelligent Game and Decision Lab,Beijing,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视图聚类中视图相关性问题，提出锚点增强策略。②通过利用视图间相关性来增强锚点表示，提升聚类性能。③相比传统多视图聚类方法，更有效地捕捉视图间互补信息。④实验表明在多个数据集上聚类准确率有显著提升。
- **摘要（英）**: This paper addresses the view correlation issue in multi-view clustering by proposing an anchor enhancement strategy. It leverages inter-view correlations to improve anchor representations, outperforming traditional methods on benchmark datasets.
- **核心贡献**: 提出基于视图相关性的锚点增强策略，提升多视图聚类性能。
- **创新点**: 利用视图间相关性动态增强锚点表示。
- **结果**: 在多个多视图数据集上聚类准确率显著提升。

### SelfPose3d: Self-Supervised Multi-Person Multi-View 3d Pose Estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2404.02041](https://arxiv.org/abs/2404.02041) · 📚 被引 22
- **作者**: Vinkle Srivastav, Keqi Chen, Nicolas Padoy
- **🏷️ 机构**: University of Strasbourg, CNRS, INSERM, ICube,Strasbourg,France,UMR7357
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视角多人3D姿态估计依赖大量标注数据的问题，提出自监督方法SelfPose3d。②仅需多视角图像和现成的2D姿态估计器生成的伪标签，通过自监督的3D定位和姿态估计目标进行训练。③引入自适应监督注意力机制缓解伪标签不准确性。④在多个基准上达到与全监督方法相当的性能，无需任何2D/3D真值。
- **摘要（英）**: SelfPose3d proposes a self-supervised approach for multi-person multi-view 3D pose estimation without ground-truth poses, using pseudo labels and adaptive attention to achieve performance comparable to fully-supervised methods.
- **核心贡献**: 提出无需真值的自监督多视角多人3D姿态估计框架。
- **创新点**: 自适应监督注意力机制处理伪标签噪声。
- **结果**: 在标准基准上接近全监督性能。

### Investigating and Mitigating the Side Effects of Noisy Views for Self-Supervised Clustering Algorithms in Practical Multi-View Scenarios. **⭐⭐** (相关度: 15%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02166) · 📚 被引 33
- **作者**: Jie Xu, Yazhou Ren, Xiaolong Wang, Lei Feng, Zheng Zhang, Gang Niu et al.
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China, Singapore University of Technology and Design,Singapore, Harbin Institute of Technology,Shenzhen,China
- **会议**: CVPR 2024
- **摘要（中）**: ①针对实际多视图场景中噪声视图对自监督聚类算法的负面影响。②系统研究了噪声视图的影响机制，并提出缓解策略。③相比现有方法，更关注实际场景中的噪声鲁棒性。④实验验证了所提策略在多种噪声条件下的有效性。
- **摘要（英）**: This work investigates the side effects of noisy views in practical multi-view scenarios for self-supervised clustering and proposes mitigation strategies, demonstrating robustness improvements.
- **核心贡献**: 分析并缓解多视图聚类中噪声视图的负面影响。
- **创新点**: 针对实际场景噪声的系统性研究。
- **结果**: 在噪声条件下聚类性能提升。

### ViewFusion: Towards Multi-View Consistency via Interpolated Denoising. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2402.18842](https://arxiv.org/abs/2402.18842) · 📚 被引 9
- **作者**: Xianghui Yang, Yan Zuo, Sameera Ramasinghe, Loris Bazzani, Gil Avraham, Anton van den Hengel
- **🏷️ 机构**: Amazon
- **会议**: CVPR 2024
- **摘要（中）**: ①针对扩散模型生成新视图时缺乏多视图一致性的问题，提出ViewFusion。②采用自回归方式，通过插值去噪融合已知视图信息，无需额外训练即可集成到预训练扩散模型。③相比现有方法，无需微调即可实现多视图条件生成。④实验证明在生成一致且细节丰富的新视图方面效果显著。
- **摘要（英）**: ViewFusion introduces a training-free algorithm for multi-view consistent novel-view synthesis by auto-regressively fusing known views via interpolated denoising, extending single-view models to multi-view settings.
- **核心贡献**: 提出无需训练的扩散模型多视图一致性生成方法。
- **创新点**: 插值去噪融合已知视图信息。
- **结果**: 在多个数据集上生成一致且高质量的新视图。

### MOHO: Learning Single-View Hand-Held Object Reconstruction with Multi-View Occlusion-Aware Supervision. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2310.11696](https://arxiv.org/abs/2310.11696) · 📚 被引 5
- **作者**: Chenyangguang Zhang, Guanlong Jiao, Yan Di, Gu Wang, Ziqin Huang, Ruida Zhang et al.
- **🏷️ 机构**: Tsinghua University, Technical University of Munich, Google
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单视图手持物体重建依赖3D真值难以获取的问题，提出MOHO框架。②利用手-物视频中的多视图遮挡感知监督，通过合成预训练和真实微调两阶段训练。③提出amodal-mask加权几何监督和域一致的遮挡感知特征，处理手部遮挡和物体自遮挡。④实验表明在真实数据上重建精度显著优于现有方法。
- **摘要（英）**: MOHO proposes a synthetic-to-real framework for single-view hand-held object reconstruction using multi-view occlusion-aware supervision from videos, addressing hand-induced and self-occlusion effectively.
- **核心贡献**: 提出利用多视图遮挡感知监督的单视图手持物体重建框架。
- **创新点**: 合成到真实的遮挡感知训练策略。
- **结果**: 在真实场景中重建精度显著提升。

### Unsupervised Gaze Representation Learning from Multi-view Face Images. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00141) · 📚 被引 9
- **作者**: Yiwei Bao, Feng Lu
- **🏷️ 机构**: School of CSE, Beihang University,State Key Laboratory of VR Technology and Systems
- **会议**: CVPR 2024
- **摘要（中）**: ①针对多视角人脸图像的无监督凝视表示学习问题。②利用多视角一致性进行自监督特征学习。③相比有监督方法，无需标注即可学习有效表示。④实验表明在凝视估计任务上性能接近有监督方法。
- **摘要（英）**: This paper explores unsupervised gaze representation learning from multi-view face images, leveraging view consistency to achieve competitive performance without labels.
- **核心贡献**: 提出多视角人脸图像的无监督凝视表示学习方法。
- **创新点**: 利用多视角一致性进行自监督学习。
- **结果**: 在凝视估计任务上接近有监督性能。

### RNb-NeuS: Reflectance and Normal-Based Multi-View 3D Reconstruction.
- **链接**: [arXiv:2312.01215](https://arxiv.org/abs/2312.01215) · 📚 被引 17
- **作者**: Baptiste Brument, Robin Bruneau, Yvain Quéau, Jean Mélou, François Bernard Lauze, Jean-Denis Durou et al.
- **🏷️ 机构**: IRIT, UMR CNRS 5505,Toulouse,France, Normandie Univ, UNICAEN, ENSICAEN, CNRS, GREYC,Caen,France, DIKU,Copenhagen,Denmark
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > This paper introduces a versatile paradigm for integrating multi-view reflectance (optional) and normal maps acquired through photometric stereo. Our approach employs a pixel-wise joint re-parameterization of reflectance and normal, considering them as a vector of radiances rendered under simulated, varying illumination. This re-parameterization enables the seamless integration of reflectance and normal maps as input data in neural volume rendering-based 3D reconstruction while preserving a single optimization objective. In contrast, recent multi-view photometric stereo (MVPS) methods depend on multiple, potentially conflicting objectives. Despite its apparent simplicity, our proposed approach outperforms state-of-the-art approaches in MVPS benchmarks across F-score, Chamfer distance, and mean angular error metrics. Notably, it significantly improves the detailed 3D reconstruction of areas with high curvature or low visibility.

### SuperNormal: Neural Surface Reconstruction via Multi-View Normal Integration.
- **链接**: [arXiv:2312.04803](https://arxiv.org/abs/2312.04803) · 📚 被引 21
- **作者**: Xu Cao, Takafumi Taketomi
- **🏷️ 机构**: CyberAgent
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We present SuperNormal, a fast, high-fidelity approach to multi-view 3D reconstruction using surface normal maps. With a few minutes, SuperNormal produces detailed surfaces on par with 3D scanners. We harness volume rendering to optimize a neural signed distance function (SDF) powered by multi-resolution hash encoding. To accelerate training, we propose directional finite difference and patch-based ray marching to approximate the SDF gradients numerically. While not compromising reconstruction quality, this strategy is nearly twice as efficient as analytical gradients and about three times faster than axis-aligned finite difference. Experiments on the benchmark dataset demonstrate the superiority of SuperNormal in efficiency and accuracy compared to existing multi-view photometric stereo methods. On our captured objects, SuperNormal produces more fine-grained geometry than recent neural 3D reconstruction methods.

### Sculpt3D: Multi-View Consistent Text-to-3D Generation with Sparse 3D Prior.
- **链接**: [arXiv:2403.09140](https://arxiv.org/abs/2403.09140) · 📚 被引 20
- **作者**: Cheng Chen, Xiaofeng Yang, Fan Yang, Chengzeng Feng, Zhoujie Fu, Chuan-Sheng Foo et al.
- **🏷️ 机构**: Nanyang Technological University, Institute for Infocomm Research A*STAR,Singapore
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent works on text-to-3d generation show that using only 2D diffusion supervision for 3D generation tends to produce results with inconsistent appearances (e.g., faces on the back view) and inaccurate shapes (e.g., animals with extra legs). Existing methods mainly address this issue by retraining diffusion models with images rendered from 3D data to ensure multi-view consistency while struggling to balance 2D generation quality with 3D consistency. In this paper, we present a new framework Sculpt3D that equips the current pipeline with explicit injection of 3D priors from retrieved reference objects without re-training the 2D diffusion model. Specifically, we demonstrate that high-quality and diverse 3D geometry can be guaranteed by keypoints supervision through a sparse ray sampling approach. Moreover, to ensure accurate appearances of different views, we further modulate the output of the 2D diffusion model to the correct patterns of the template views without altering the generated object's style. These two decoupled designs effectively harness 3D information from reference objects to generate 3D objects while preserving the generation quality of the 2D diffusion model. Extensive experiments show our method can largely improve the multi-view consistency while retaining fidelity and diversity. Our project page is available at: https://stellarcheng.github.io/Sculpt3D/.

### 2S-UDF: A Novel Two-Stage UDF Learning Method for Robust Non-Watertight Model Reconstruction from Multi-View Images.
- **链接**: [arXiv:2303.15368](https://arxiv.org/abs/2303.15368) · 📚 被引 10
- **作者**: Junkai Deng, Fei Hou, Xuhui Chen, Wencheng Wang, Ying He
- **🏷️ 机构**: Institute of Software,State Key Laboratory of Computer Science, Chinese Academy of Sciences, School of Computer Science and Engineering, Nanyang Technological University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recently, building on the foundation of neural radiance field, various techniques have emerged to learn unsigned distance fields (UDF) to reconstruct 3D non-watertight models from multi-view images. Yet, a central challenge in UDF-based volume rendering is formulating a proper way to convert unsigned distance values into volume density, ensuring that the resulting weight function remains unbiased and sensitive to occlusions. Falling short on these requirements often results in incorrect topology or large reconstruction errors in resulting models. This paper addresses this challenge by presenting a novel two-stage algorithm, 2S-UDF, for learning a high-quality UDF from multi-view images. Initially, the method applies an easily trainable density function that, while slightly biased and transparent, aids in coarse reconstruction. The subsequent stage then refines the geometry and appearance of the object to achieve a high-quality reconstruction by directly adjusting the weight function used in volume rendering to ensure that it is unbiased and occlusion-aware. Decoupling density and weight in two stages makes our training stable and robust, distinguishing our technique from existing UDF learning approaches. Evaluations on the DeepFashion3D, DTU, and BlendedMVS datasets validate the robustness and effectiveness of our proposed approach. In both quantitative metrics and visual quality, the results indicate our superior performance over other UDF learning techniques in reconstructing 3D non-watertight models from multi-view images. Our code is available at https://bitbucket.org/jkdeng/2sudf/.

### VMINer: Versatile Multi-view Inverse Rendering with Near-and Far-field Light Sources.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01121) · 📚 被引 9
- **作者**: Fan Fei, Jiajun Tang, Ping Tan, Boxin Shi
- **🏷️ 机构**: School of Computer Science, Peking University,National Key Laboratory for Multimedia Information Processing, Hong Kong University of Science and Technology
- **会议**: CVPR 2024

### Visual Anagrams: Generating Multi-View Optical Illusions with Diffusion Models.
- **链接**: [arXiv:2311.17919](https://arxiv.org/abs/2311.17919) · 📚 被引 26
- **作者**: Daniel Geng, Inbum Park, Andrew Owens
- **🏷️ 机构**: University of Michigan
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We address the problem of synthesizing multi-view optical illusions: images that change appearance upon a transformation, such as a flip or rotation. We propose a simple, zero-shot method for obtaining these illusions from off-the-shelf text-to-image diffusion models. During the reverse diffusion process, we estimate the noise from different views of a noisy image, and then combine these noise estimates together and denoise the image. A theoretical analysis suggests that this method works precisely for views that can be written as orthogonal transformations, of which permutations are a subset. This leads to the idea of a visual anagram--an image that changes appearance under some rearrangement of pixels. This includes rotations and flips, but also more exotic pixel permutations such as a jigsaw rearrangement. Our approach also naturally extends to illusions with more than two views. We provide both qualitative and quantitative results demonstrating the effectiveness and flexibility of our method. Please see our project webpage for additional visualizations and results: https://dangeng.github.io/visual_anagrams/

### EpiDiff: Enhancing Multi-View Synthesis via Localized Epipolar-Constrained Diffusion.
- **链接**: [arXiv:2312.06725](https://arxiv.org/abs/2312.06725) · 📚 被引 40
- **作者**: Zehuan Huang, Hao Wen, Junting Dong, Yaohui Wang, Yangguang Li, Xinyuan Chen et al.
- **🏷️ 机构**: Beihang University, Shanghai AI Laboratory, VAST
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Generating multiview images from a single view facilitates the rapid generation of a 3D mesh conditioned on a single image. Recent methods that introduce 3D global representation into diffusion models have shown the potential to generate consistent multiviews, but they have reduced generation speed and face challenges in maintaining generalizability and quality. To address this issue, we propose EpiDiff, a localized interactive multiview diffusion model. At the core of the proposed approach is to insert a lightweight epipolar attention block into the frozen diffusion model, leveraging epipolar constraints to enable cross-view interaction among feature maps of neighboring views. The newly initialized 3D modeling module preserves the original feature distribution of the diffusion model, exhibiting compatibility with a variety of base diffusion models. Experiments show that EpiDiff generates 16 multiview images in just 12 seconds, and it surpasses previous methods in quality evaluation metrics, including PSNR, SSIM and LPIPS. Additionally, EpiDiff can generate a more diverse distribution of views, improving the reconstruction quality from generated multiviews. Please see our project page at https://huanngzh.github.io/EpiDiff/.

### ESR-NeRF: Emissive Source Reconstruction Using LDR Multi-View Images.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00440) · 📚 被引 4
- **作者**: Jinseo Jeong, Junseo Koo, Qimeng Zhang, Gunhee Kim
- **🏷️ 机构**: Seoul National University
- **会议**: CVPR 2024

### SPAD: Spatially Aware Multi-View Diffusers.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00956) · 📚 被引 22
- **作者**: Yash Kant, Aliaksandr Siarohin, Ziyi Wu, Michael Vasilkovsky, Guocheng Qian, Jian Ren et al.
- **🏷️ 机构**: University of Toronto, Snap Research, KAUST
- **会议**: CVPR 2024

### MAS: Multi-view Ancestral Sampling for 3D Motion Generation Using 2D Diffusion.
- **链接**: [arXiv:2310.14729](https://arxiv.org/abs/2310.14729) · 📚 被引 14
- **作者**: Roy Kapon, Guy Tevet, Daniel Cohen-Or, Amit H. Bermano
- **🏷️ 机构**: Tel Aviv University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We introduce Multi-view Ancestral Sampling (MAS), a method for 3D motion generation, using 2D diffusion models that were trained on motions obtained from in-the-wild videos. As such, MAS opens opportunities to exciting and diverse fields of motion previously under-explored as 3D data is scarce and hard to collect. MAS works by simultaneously denoising multiple 2D motion sequences representing different views of the same 3D motion. It ensures consistency across all views at each diffusion step by combining the individual generations into a unified 3D sequence, and projecting it back to the original views. We demonstrate MAS on 2D pose data acquired from videos depicting professional basketball maneuvers, rhythmic gymnastic performances featuring a ball apparatus, and horse races. In each of these domains, 3D motion capture is arduous, and yet, MAS generates diverse and realistic 3D sequences. Unlike the Score Distillation approach, which optimizes each sample by repeatedly applying small fixes, our method uses a sampling process that was constructed for the diffusion framework. As we demonstrate, MAS avoids common issues such as out-of-domain sampling and mode-collapse. https://guytevet.github.io/mas-page/

### Rethinking Multi-View Representation Learning via Distilled Disentangling.
- **链接**: [arXiv:2403.10897](https://arxiv.org/abs/2403.10897) · 📚 被引 30
- **作者**: Guanzhou Ke, Bo Wang, Xiaoli Wang, Shengfeng He
- **🏷️ 机构**: Beijing Jiaotong University, Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, Nanjing University of Science and Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multi-view representation learning aims to derive robust representations that are both view-consistent and view-specific from diverse data sources. This paper presents an in-depth analysis of existing approaches in this domain, highlighting a commonly overlooked aspect: the redundancy between view-consistent and view-specific representations. To this end, we propose an innovative framework for multi-view representation learning, which incorporates a technique we term 'distilled disentangling'. Our method introduces the concept of masked cross-view prediction, enabling the extraction of compact, high-quality view-consistent representations from various sources without incurring extra computational overhead. Additionally, we develop a distilled disentangling module that efficiently filters out consistency-related information from multi-view representations, resulting in purer view-specific representations. This approach significantly reduces redundancy between view-consistent and view-specific representations, enhancing the overall efficiency of the learning process. Our empirical evaluations reveal that higher mask ratios substantially improve the quality of view-consistent representations. Moreover, we find that reducing the dimensionality of view-consistent representations relative to that of view-specific representations further refines the quality of the combined representations. Our code is accessible at: https://github.com/Guanzhou-Ke/MRDD.

### UnionFormer: Unified-Learning Transformer with Multi-View Representation for Image Manipulation Detection and Localization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01190) · 📚 被引 22
- **作者**: Shuaibo Li, Wei Ma, Jianwei Guo, Shibiao Xu, Benchong Li, Xiaopeng Zhang
- **🏷️ 机构**: Beijing University of Technology, Institute of Automation, Chinese Academy of Sciences,MAIS, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2024

### One-2-3-45++: Fast Single Image to 3D Objects with Consistent Multi-View Generation and 3D Diffusion.
- **链接**: [arXiv:2311.07885](https://arxiv.org/abs/2311.07885) · 📚 被引 155
- **作者**: Minghua Liu, Ruoxi Shi, Linghao Chen, Zhuoyang Zhang, Chao Xu, Xinyue Wei et al.
- **🏷️ 机构**: UC San Diego, Tsinghua University, UCLA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advancements in open-world 3D object generation have been remarkable, with image-to-3D methods offering superior fine-grained control over their text-to-3D counterparts. However, most existing models fall short in simultaneously providing rapid generation speeds and high fidelity to input images - two features essential for practical applications. In this paper, we present One-2-3-45++, an innovative method that transforms a single image into a detailed 3D textured mesh in approximately one minute. Our approach aims to fully harness the extensive knowledge embedded in 2D diffusion models and priors from valuable yet limited 3D data. This is achieved by initially finetuning a 2D diffusion model for consistent multi-view image generation, followed by elevating these images to 3D with the aid of multi-view conditioned 3D native diffusion models. Extensive experimental evaluations demonstrate that our method can produce high-quality, diverse 3D assets that closely mirror the original input image. Our project webpage: https://sudo-ai-3d.github.io/One2345plus_page.

### S2MVTC: A Simple Yet Efficient Scalable Multi-View Tensor Clustering.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02274) · 📚 被引 23
- **作者**: Zhen Long, Qiyuan Wang, Yazhou Ren, Yipeng Liu, Ce Zhu
- **🏷️ 机构**: University of Electronic Science &#x0026; Technology of China
- **会议**: CVPR 2024

### Direct2.5: Diverse Text-to-3D Generation via Multi-view 2.5D Diffusion.
- **链接**: [arXiv:2311.15980](https://arxiv.org/abs/2311.15980) · 📚 被引 22
- **作者**: Yuanxun Lu, Jingyang Zhang, Shiwei Li, Tian Fang, David McKinnon, Yanghai Tsin et al.
- **🏷️ 机构**: Nanjing University, Apple, The Hong Kong University of Science and Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advances in generative AI have unveiled significant potential for the creation of 3D content. However, current methods either apply a pre-trained 2D diffusion model with the time-consuming score distillation sampling (SDS), or a direct 3D diffusion model trained on limited 3D data losing generation diversity. In this work, we approach the problem by employing a multi-view 2.5D diffusion fine-tuned from a pre-trained 2D diffusion model. The multi-view 2.5D diffusion directly models the structural distribution of 3D data, while still maintaining the strong generalization ability of the original 2D diffusion model, filling the gap between 2D diffusion-based and direct 3D diffusion-based methods for 3D content generation. During inference, multi-view normal maps are generated using the 2.5D diffusion, and a novel differentiable rasterization scheme is introduced to fuse the almost consistent multi-view normal maps into a consistent 3D model. We further design a normal-conditioned multi-view image generation module for fast appearance generation given the 3D geometry. Our method is a one-pass diffusion process and does not require any SDS optimization as post-processing. We demonstrate through extensive experiments that, our direct 2.5D generation with the specially-designed fusion scheme can achieve diverse, mode-seeking-free, and high-fidelity 3D content generation in only 10 seconds. Project page: https://nju-3dv.github.io/projects/direct25.

### Wired Perspectives: Multi-View Wire Art Embraces Generative AI.
- **链接**: [arXiv:2311.15421](https://arxiv.org/abs/2311.15421) · 📚 被引 9
- **作者**: Zhiyu Qu, Lan Yang, Honggang Zhang, Tao Xiang, Kaiyue Pang, Yi-Zhe Song
- **🏷️ 机构**: SketchX, CVSSP, University of Surrey, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Creating multi-view wire art (MVWA), a static 3D sculpture with diverse interpretations from different viewpoints, is a complex task even for skilled artists. In response, we present DreamWire, an AI system enabling everyone to craft MVWA easily. Users express their vision through text prompts or scribbles, freeing them from intricate 3D wire organisation. Our approach synergises 3D Bézier curves, Prim's algorithm, and knowledge distillation from diffusion models or their variants (e.g., ControlNet). This blend enables the system to represent 3D wire art, ensuring spatial continuity and overcoming data scarcity. Extensive evaluation and analysis are conducted to shed insight on the inner workings of the proposed system, including the trade-off between connectivity and visual aesthetics.

### MVCPS-NeuS: Multi-View Constrained Photometric Stereo for Neural Surface Reconstruction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01935) · 📚 被引 7
- **作者**: Hiroaki Santo, Fumio Okura, Yasuyuki Matsushita
- **🏷️ 机构**: Graduate School of Information Science and Technology, Osaka University
- **会议**: CVPR 2024

### Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection.
- **链接**: [arXiv:2403.12580](https://arxiv.org/abs/2403.12580) · 📚 被引 119
- **作者**: Chengjie Wang, Wenbing Zhu, Bin-Bin Gao, Zhenye Gan, Jiangning Zhang, Zhihao Gu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University, Fudan University, Youtu Lab,Tencent
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Industrial anomaly detection (IAD) has garnered significant attention and experienced rapid development. However, the recent development of IAD approach has encountered certain difficulties due to dataset limitations. On the one hand, most of the state-of-the-art methods have achieved saturation (over 99% in AUROC) on mainstream datasets such as MVTec, and the differences of methods cannot be well distinguished, leading to a significant gap between public datasets and actual application scenarios. On the other hand, the research on various new practical anomaly detection settings is limited by the scale of the dataset, posing a risk of overfitting in evaluation results. Therefore, we propose a large-scale, Real-world, and multi-view Industrial Anomaly Detection dataset, named Real-IAD, which contains 150K high-resolution images of 30 different objects, an order of magnitude larger than existing datasets. It has a larger range of defect area and ratio proportions, making it more challenging than previous datasets. To make the dataset closer to real application scenarios, we adopted a multi-view shooting method and proposed sample-level evaluation metrics. In addition, beyond the general unsupervised anomaly detection setting, we propose a new setting for Fully Unsupervised Industrial Anomaly Detection (FUIAD) based on the observation that the yield rate in industrial production is usually greater than 60%, which has more practical application value. Finally, we report the results of popular IAD methods on the Real-IAD dataset, providing a highly challenging benchmark to promote the development of the IAD field.

### GoMVS: Geometrically Consistent Cost Aggregation for Multi-View Stereo.
- **链接**: [arXiv:2404.07992](https://arxiv.org/abs/2404.07992) · 📚 被引 47
- **作者**: Jiang Wu, Rui Li, Haofei Xu, Wenxun Zhao, Yu Zhu, Jinqiu Sun et al.
- **🏷️ 机构**: Northwestern Poly technical University, ETH Zurich
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Matching cost aggregation plays a fundamental role in learning-based multi-view stereo networks. However, directly aggregating adjacent costs can lead to suboptimal results due to local geometric inconsistency. Related methods either seek selective aggregation or improve aggregated depth in the 2D space, both are unable to handle geometric inconsistency in the cost volume effectively. In this paper, we propose GoMVS to aggregate geometrically consistent costs, yielding better utilization of adjacent geometries. More specifically, we correspond and propagate adjacent costs to the reference pixel by leveraging the local geometric smoothness in conjunction with surface normals. We achieve this by the geometric consistent propagation (GCP) module. It computes the correspondence from the adjacent depth hypothesis space to the reference depth space using surface normals, then uses the correspondence to propagate adjacent costs to the reference geometry, followed by a convolution for aggregation. Our method achieves new state-of-the-art performance on DTU, Tanks & Temple, and ETH3D datasets. Notably, our method ranks 1st on the Tanks & Temple Advanced benchmark.

### Carve3D: Improving Multi-view Reconstruction Consistency for Diffusion Models with RL Finetuning.
- **链接**: [arXiv:2312.13980](https://arxiv.org/abs/2312.13980) · 📚 被引 12
- **作者**: Desai Xie, Jiahao Li, Hao Tan, Xin Sun, Zhixin Shu, Yi Zhou et al.
- **🏷️ 机构**: Adobe Research, Kiel University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Multi-view diffusion models, obtained by applying Supervised Finetuning (SFT) to text-to-image diffusion models, have driven recent breakthroughs in text-to-3D research. However, due to the limited size and quality of existing 3D datasets, they still suffer from multi-view inconsistencies and Neural Radiance Field (NeRF) reconstruction artifacts. We argue that multi-view diffusion models can benefit from further Reinforcement Learning Finetuning (RLFT), which allows models to learn from the data generated by themselves and improve beyond their dataset limitations during SFT. To this end, we introduce Carve3D, an improved RLFT algorithm coupled with a novel Multi-view Reconstruction Consistency (MRC) metric, to enhance the consistency of multi-view diffusion models. To measure the MRC metric on a set of multi-view images, we compare them with their corresponding NeRF renderings at the same camera viewpoints. The resulting model, which we denote as Carve3DM, demonstrates superior multi-view consistency and NeRF reconstruction quality than existing models. Our results suggest that pairing SFT with Carve3D's RLFT is essential for developing multi-view-consistent diffusion models, mirroring the standard Large Language Model (LLM) alignment pipeline. Our code, training and testing data, and video results are available at: https://desaixie.github.io/carve-3d.

### MVHumanNet: A Large-Scale Dataset of Multi-View Daily Dressing Human Captures.
- **链接**: [arXiv:2312.02963](https://arxiv.org/abs/2312.02963) · 📚 被引 31
- **作者**: Zhangyang Xiong, Chenghong Li, Kenkun Liu, Hongjie Liao, Jianqiao Hu, Junyi Zhu et al.
- **🏷️ 机构**: FNii, CUHKSZ, SSE, CUHKSZ
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In this era, the success of large language models and text-to-image models can be attributed to the driving force of large-scale datasets. However, in the realm of 3D vision, while remarkable progress has been made with models trained on large-scale synthetic and real-captured object data like Objaverse and MVImgNet, a similar level of progress has not been observed in the domain of human-centric tasks partially due to the lack of a large-scale human dataset. Existing datasets of high-fidelity 3D human capture continue to be mid-sized due to the significant challenges in acquiring large-scale high-quality 3D human data. To bridge this gap, we present MVHumanNet, a dataset that comprises multi-view human action sequences of 4,500 human identities. The primary focus of our work is on collecting human data that features a large number of diverse identities and everyday clothing using a multi-view human capture system, which facilitates easily scalable data collection. Our dataset contains 9,000 daily outfits, 60,000 motion sequences and 645 million frames with extensive annotations, including human masks, camera parameters, 2D and 3D keypoints, SMPL/SMPLX parameters, and corresponding textual descriptions. To explore the potential of MVHumanNet in various 2D and 3D visual tasks, we conducted pilot studies on view-consistent action recognition, human NeRF reconstruction, text-driven view-unconstrained human image generation, as well as 2D view-unconstrained human image and 3D avatar generation. Extensive experiments demonstrate the performance improvements and effective applications enabled by the scale provided by MVHumanNet. As the current largest-scale 3D human dataset, we hope that the release of MVHumanNet data with annotations will foster further innovations in the domain of 3D human-centric tasks at scale.

### Differentiable Information Bottleneck for Deterministic Multi-View Clustering.
- **链接**: [arXiv:2403.15681](https://arxiv.org/abs/2403.15681) · 📚 被引 28
- **作者**: Xiaoqiang Yan, Zhixiang Jin, Fengshou Han, Yangdong Ye
- **🏷️ 机构**: School of Computer and Artificial Intelligence, Zhengzhou University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In recent several years, the information bottleneck (IB) principle provides an information-theoretic framework for deep multi-view clustering (MVC) by compressing multi-view observations while preserving the relevant information of multiple views. Although existing IB-based deep MVC methods have achieved huge success, they rely on variational approximation and distribution assumption to estimate the lower bound of mutual information, which is a notoriously hard and impractical problem in high-dimensional multi-view spaces. In this work, we propose a new differentiable information bottleneck (DIB) method, which provides a deterministic and analytical MVC solution by fitting the mutual information without the necessity of variational approximation. Specifically, we first propose to directly fit the mutual information of high-dimensional spaces by leveraging normalized kernel Gram matrix, which does not require any auxiliary neural estimator to estimate the lower bound of mutual information. Then, based on the new mutual information measurement, a deterministic multi-view neural network with analytical gradients is explicitly trained to parameterize IB principle, which derives a deterministic compression of input variables from different views. Finally, a triplet consistency discovery mechanism is devised, which is capable of mining the feature consistency, cluster consistency and joint consistency based on the deterministic and compact representations. Extensive experimental results show the superiority of our DIB method on 6 benchmarks compared with 13 state-of-the-art baselines.

### ConsistNet: Enforcing 3D Consistency for Multi-View Images Diffusion.
- **链接**: [arXiv:2310.10343](https://arxiv.org/abs/2310.10343) · 📚 被引 34
- **作者**: Jiayu Yang, Ziang Cheng, Yunfei Duan, Pan Ji, Hongdong Li
- **🏷️ 机构**: Tencent, Australian National University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Given a single image of a 3D object, this paper proposes a novel method (named ConsistNet) that is able to generate multiple images of the same object, as if seen they are captured from different viewpoints, while the 3D (multi-view) consistencies among those multiple generated images are effectively exploited. Central to our method is a multi-view consistency block which enables information exchange across multiple single-view diffusion processes based on the underlying multi-view geometry principles. ConsistNet is an extension to the standard latent diffusion model, and consists of two sub-modules: (a) a view aggregation module that unprojects multi-view features into global 3D volumes and infer consistency, and (b) a ray aggregation module that samples and aggregate 3D consistent features back to each view to enforce consistency. Our approach departs from previous methods in multi-view image generation, in that it can be easily dropped-in pre-trained LDMs without requiring explicit pixel correspondences or depth prediction. Experiments show that our method effectively learns 3D consistency over a frozen Zero123 backbone and can generate 16 surrounding views of the object within 40 seconds on a single A100 GPU. Our code will be made available on https://github.com/JiayuYANG/ConsistNet

### DreamComposer: Controllable 3D Object Generation via Multi-View Conditions.
- **链接**: [arXiv:2312.03611](https://arxiv.org/abs/2312.03611) · 📚 被引 10
- **作者**: Yunhan Yang, Yukun Huang, Xiaoyang Wu, Yuan-Chen Guo, Song-Hai Zhang, Hengshuang Zhao et al.
- **🏷️ 机构**: The University of Hong Kong, VAST, Tsinghua University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Utilizing pre-trained 2D large-scale generative models, recent works are capable of generating high-quality novel views from a single in-the-wild image. However, due to the lack of information from multiple views, these works encounter difficulties in generating controllable novel views. In this paper, we present DreamComposer, a flexible and scalable framework that can enhance existing view-aware diffusion models by injecting multi-view conditions. Specifically, DreamComposer first uses a view-aware 3D lifting module to obtain 3D representations of an object from multiple views. Then, it renders the latent features of the target view from 3D representations with the multi-view feature fusion module. Finally the target view features extracted from multi-view inputs are injected into a pre-trained diffusion model. Experiments show that DreamComposer is compatible with state-of-the-art diffusion models for zero-shot novel view synthesis, further enhancing them to generate high-fidelity novel view images with multi-view conditions, ready for controllable 3D object reconstruction and various other applications.

### Multi-View Aggregation Network for Dichotomous Image Segmentation.
- **链接**: [arXiv:2404.07445](https://arxiv.org/abs/2404.07445) · 📚 被引 19
- **作者**: Qian Yu, Xiaoqi Zhao, Youwei Pang, Lihe Zhang, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Dichotomous Image Segmentation (DIS) has recently emerged towards high-precision object segmentation from high-resolution natural images. When designing an effective DIS model, the main challenge is how to balance the semantic dispersion of high-resolution targets in the small receptive field and the loss of high-precision details in the large receptive field. Existing methods rely on tedious multiple encoder-decoder streams and stages to gradually complete the global localization and local refinement. Human visual system captures regions of interest by observing them from multiple views. Inspired by it, we model DIS as a multi-view object perception problem and provide a parsimonious multi-view aggregation network (MVANet), which unifies the feature fusion of the distant view and close-up view into a single stream with one encoder-decoder structure. With the help of the proposed multi-view complementary localization and refinement modules, our approach established long-range, profound visual interactions across multiple views, allowing the features of the detailed close-up view to focus on highly slender structures.Experiments on the popular DIS-5K dataset show that our MVANet significantly outperforms state-of-the-art methods in both accuracy and speed. The source code and datasets will be publicly available at \href{https://github.com/qianyu-dlut/MVANet}{MVANet}.

### TULIP: Multi-Camera 3D Precision Assessment of Parkinson's Disease.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02128) · 📚 被引 9
- **作者**: Kyungdo Kim, Sihan Lyu, Sneha Mantri, Timothy W. Dunn
- **🏷️ 机构**: Duke University,Department of Biomedical Engineering,Durham,NC,USA, Duke University,Department of Neurology,Durham,NC,USA
- **会议**: CVPR 2024

### Mind The Edge: Refining Depth Edges in Sparsely-Supervised Monocular Depth Estimation.
- **链接**: [arXiv:2212.05315](https://arxiv.org/abs/2212.05315) · 📚 被引 11
- **作者**: Lior Talker, Aviad Cohen, Erez Yosef, Alexandra Dana, Michael Dinerstein
- **🏷️ 机构**: Samsung Israel R&#x0026;D Center,Tel Aviv,Israel
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Monocular Depth Estimation (MDE) is a fundamental problem in computer vision with numerous applications. Recently, LIDAR-supervised methods have achieved remarkable per-pixel depth accuracy in outdoor scenes. However, significant errors are typically found in the proximity of depth discontinuities, i.e., depth edges, which often hinder the performance of depth-dependent applications that are sensitive to such inaccuracies, e.g., novel view synthesis and augmented reality. Since direct supervision for the location of depth edges is typically unavailable in sparse LIDAR-based scenes, encouraging the MDE model to produce correct depth edges is not straightforward. To the best of our knowledge this paper is the first attempt to address the depth edges issue for LIDAR-supervised scenes. In this work we propose to learn to detect the location of depth edges from densely-supervised synthetic data, and use it to generate supervision for the depth edges in the MDE training. To quantitatively evaluate our approach, and due to the lack of depth edges GT in LIDAR-based scenes, we manually annotated subsets of the KITTI and the DDAD datasets with depth edges ground truth. We demonstrate significant gains in the accuracy of the depth edges with comparable per-pixel depth accuracy on several challenging datasets. Code and datasets are available at \url{https://github.com/liortalker/MindTheEdge}.

### Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation.
- **链接**: [arXiv:2312.02145](https://arxiv.org/abs/2312.02145) · 📚 被引 470
- **作者**: Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, Konrad Schindler
- **🏷️ 机构**: Photogrammetry and Remote Sensing, ETH Z&#x00FC;rich
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Monocular depth estimation is a fundamental computer vision task. Recovering 3D depth from a single image is geometrically ill-posed and requires scene understanding, so it is not surprising that the rise of deep learning has led to a breakthrough. The impressive progress of monocular depth estimators has mirrored the growth in model capacity, from relatively modest CNNs to large Transformer architectures. Still, monocular depth estimators tend to struggle when presented with images with unfamiliar content and layout, since their knowledge of the visual world is restricted by the data seen during training, and challenged by zero-shot generalization to new domains. This motivates us to explore whether the extensive priors captured in recent generative diffusion models can enable better, more generalizable depth estimation. We introduce Marigold, a method for affine-invariant monocular depth estimation that is derived from Stable Diffusion and retains its rich prior knowledge. The estimator can be fine-tuned in a couple of days on a single GPU using only synthetic training data. It delivers state-of-the-art performance across a wide range of datasets, including over 20% performance gains in specific cases. Project page: https://marigoldmonodepth.github.io.

### From-Ground-To-Objects: Coarse-to-Fine Self-supervised Monocular Depth Estimation of Dynamic Objects with Ground Contact Prior.
- **链接**: [arXiv:2312.10118](https://arxiv.org/abs/2312.10118) · 📚 被引 17
- **作者**: Jaeho Moon, Juan Luis Gonzalez Bello, Byeongjun Kwon, Munchurl Kim
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Self-supervised monocular depth estimation (DE) is an approach to learning depth without costly depth ground truths. However, it often struggles with moving objects that violate the static scene assumption during training. To address this issue, we introduce a coarse-to-fine training strategy leveraging the ground contacting prior based on the observation that most moving objects in outdoor scenes contact the ground. In the coarse training stage, we exclude the objects in dynamic classes from the reprojection loss calculation to avoid inaccurate depth learning. To provide precise supervision on the depth of the objects, we present a novel Ground-contacting-prior Disparity Smoothness Loss (GDS-Loss) that encourages a DE network to align the depth of the objects with their ground-contacting points. Subsequently, in the fine training stage, we refine the DE network to learn the detailed depth of the objects from the reprojection loss, while ensuring accurate DE on the moving object regions by employing our regularization loss with a cost-volume-based weighting factor. Our overall coarse-to-fine training strategy can easily be integrated with existing DE methods without any modifications, significantly enhancing DE performance on challenging Cityscapes and KITTI datasets, especially in the moving object regions.

### Mining Supervision for Dynamic Regions in Self-Supervised Monocular Depth Estimation.
- **链接**: [arXiv:2404.14908](https://arxiv.org/abs/2404.14908) · 📚 被引 8
- **作者**: Hoang Chuong Nguyen, Tianyu Wang, José M. Álvarez, Miaomiao Liu
- **🏷️ 机构**: Australian National University, NVIDIA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > This paper focuses on self-supervised monocular depth estimation in dynamic scenes trained on monocular videos. Existing methods jointly estimate pixel-wise depth and motion, relying mainly on an image reconstruction loss. Dynamic regions1 remain a critical challenge for these methods due to the inherent ambiguity in depth and motion estimation, resulting in inaccurate depth estimation. This paper proposes a self-supervised training framework exploiting pseudo depth labels for dynamic regions from training data. The key contribution of our framework is to decouple depth estimation for static and dynamic regions of images in the training data. We start with an unsupervised depth estimation approach, which provides reliable depth estimates for static regions and motion cues for dynamic regions and allows us to extract moving object information at the instance level. In the next stage, we use an object network to estimate the depth of those moving objects assuming rigid motions. Then, we propose a new scale alignment module to address the scale ambiguity between estimated depths for static and dynamic regions. We can then use the depth labels generated to train an end-to-end depth estimation network and improve its performance. Extensive experiments on the Cityscapes and KITTI datasets show that our self-training strategy consistently outperforms existing self/unsupervised depth estimation methods.

### ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation.
- **链接**: [arXiv:2403.18807](https://arxiv.org/abs/2403.18807) · 📚 被引 56
- **作者**: Suraj Patni, Aradhye Agarwal, Chetan Arora
- **🏷️ 机构**: Indian Institute of Technology Delhi
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the absence of parallax cues, a learning-based single image depth estimation (SIDE) model relies heavily on shading and contextual cues in the image. While this simplicity is attractive, it is necessary to train such models on large and varied datasets, which are difficult to capture. It has been shown that using embeddings from pre-trained foundational models, such as CLIP, improves zero shot transfer in several applications. Taking inspiration from this, in our paper we explore the use of global image priors generated from a pre-trained ViT model to provide more detailed contextual information. We argue that the embedding vector from a ViT model, pre-trained on a large dataset, captures greater relevant information for SIDE than the usual route of generating pseudo image captions, followed by CLIP based text embeddings. Based on this idea, we propose a new SIDE model using a diffusion backbone which is conditioned on ViT embeddings. Our proposed design establishes a new state-of-the-art (SOTA) for SIDE on NYUv2 dataset, achieving Abs Rel error of 0.059 (14% improvement) compared to 0.069 by the current SOTA (VPD). And on KITTI dataset, achieving Sq Rel error of 0.139 (2% improvement) compared to 0.142 by the current SOTA (GEDepth). For zero-shot transfer with a model trained on NYUv2, we report mean relative improvement of (20%, 23%, 81%, 25%) over NeWCRFs on (Sun-RGBD, iBims1, DIODE, HyperSim) datasets, compared to (16%, 18%, 45%, 9%) by ZoeDepth. The project page is available at https://ecodepth-iitd.github.io

### WorDepth: Variational Language Prior for Monocular Depth Estimation.
- **链接**: [arXiv:2404.03635](https://arxiv.org/abs/2404.03635) · 📚 被引 30
- **作者**: Ziyao Zeng, Daniel Wang, Fengyu Yang, Hyoungseob Park, Stefano Soatto, Dong Lao et al.
- **🏷️ 机构**: Yale University, University of California,Los Angeles
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Three-dimensional (3D) reconstruction from a single image is an ill-posed problem with inherent ambiguities, i.e. scale. Predicting a 3D scene from text description(s) is similarly ill-posed, i.e. spatial arrangements of objects described. We investigate the question of whether two inherently ambiguous modalities can be used in conjunction to produce metric-scaled reconstructions. To test this, we focus on monocular depth estimation, the problem of predicting a dense depth map from a single image, but with an additional text caption describing the scene. To this end, we begin by encoding the text caption as a mean and standard deviation; using a variational framework, we learn the distribution of the plausible metric reconstructions of 3D scenes corresponding to the text captions as a prior. To "select" a specific reconstruction or depth map, we encode the given image through a conditional sampler that samples from the latent space of the variational text encoder, which is then decoded to the output depth map. Our approach is trained alternatingly between the text and image branches: in one optimization step, we predict the mean and standard deviation from the text description and sample from a standard Gaussian, and in the other, we sample using a (image) conditional sampler. Once trained, we directly predict depth from the encoded text using the conditional sampler. We demonstrate our approach on indoor (NYUv2) and outdoor (KITTI) scenarios, where we show that language can consistently improve performance in both.

### Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding.
- **链接**: [arXiv:2311.18482](https://arxiv.org/abs/2311.18482)
- **作者**: Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, Shao-Hua Guan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation. Language-embedded scene representations have made progress by incorporating language features into 3D spaces. However, their efficacy heavily depends on neural networks that are resource-intensive in training and rendering. Although recent 3D Gaussians offer efficient and high-quality novel view synthesis, directly embedding language features in them leads to prohibitive memory usage and decreased performance. In this work, we introduce Language Embedded 3D Gaussians, a novel scene representation for open-vocabulary query tasks. Instead of embedding high-dimensional raw semantic features on 3D Gaussians, we propose a dedicated quantization scheme that drastically alleviates the memory requirement, and a novel embedding procedure that achieves smoother yet high accuracy query, countering the multi-view feature inconsistencies and the high-frequency inductive bias in point-based representations. Our comprehensive experiments show that our representation achieves the best visual quality and language querying accuracy across current language-embedded representations, while maintaining real-time rendering frame rates on a single desktop GPU.

### GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields.
- **链接**: [arXiv:2404.00931](https://arxiv.org/abs/2404.00931) · 📚 被引 3
- **作者**: Yunsong Wang, Hanlin Chen, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore,Department of Computer Science
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Recent advancements in vision-language foundation models have significantly enhanced open-vocabulary 3D scene understanding. However, the generalizability of existing methods is constrained due to their framework designs and their reliance on 3D data. We address this limitation by introducing Generalizable Open-Vocabulary Neural Semantic Fields (GOV-NeSF), a novel approach offering a generalizable implicit representation of 3D scenes with open-vocabulary semantics. We aggregate the geometry-aware features using a cost volume, and propose a Multi-view Joint Fusion module to aggregate multi-view features through a cross-view attention mechanism, which effectively predicts view-specific blending weights for both colors and open-vocabulary features. Remarkably, our GOV-NeSF exhibits state-of-the-art performance in both 2D and 3D open-vocabulary semantic segmentation, eliminating the need for ground truth semantic labels or depth priors, and effectively generalize across scenes and datasets without fine-tuning.

### MaskClustering: View Consensus Based Mask Graph Clustering for Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2401.07745](https://arxiv.org/abs/2401.07745) · 📚 被引 41
- **作者**: Mi Yan, Jiazhao Zhang, Yan Zhu, He Wang
- **🏷️ 机构**: CFCS, School of CS, Peking University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary 3D instance segmentation is cutting-edge for its ability to segment 3D instances without predefined categories. However, progress in 3D lags behind its 2D counterpart due to limited annotated 3D data. To address this, recent works first generate 2D open-vocabulary masks through 2D models and then merge them into 3D instances based on metrics calculated between two neighboring frames. In contrast to these local metrics, we propose a novel metric, view consensus rate, to enhance the utilization of multi-view observations. The key insight is that two 2D masks should be deemed part of the same 3D instance if a significant number of other 2D masks from different views contain both these two masks. Using this metric as edge weight, we construct a global mask graph where each mask is a node. Through iterative clustering of masks showing high view consensus, we generate a series of clusters, each representing a distinct 3D instance. Notably, our model is training-free. Through extensive experiments on publicly available datasets, including ScanNet++, ScanNet200 and MatterPort3D, we demonstrate that our method achieves state-of-the-art performance in open-vocabulary 3D instance segmentation. Our project page is at https://pku-epic.github.io/MaskClustering.

### EMOPortraits: Emotion-Enhanced Multimodal One-Shot Head Avatars.
- **链接**: [arXiv:2404.19110](https://arxiv.org/abs/2404.19110) · 📚 被引 41
- **作者**: Nikita Drobyshev, Antoni Bigata Casademunt, Konstantinos Vougioukas, Zoe Landgraf, Stavros Petridis, Maja Pantic
- **🏷️ 机构**: Imperial College London
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Head avatars animated by visual signals have gained popularity, particularly in cross-driving synthesis where the driver differs from the animated character, a challenging but highly practical approach. The recently presented MegaPortraits model has demonstrated state-of-the-art results in this domain. We conduct a deep examination and evaluation of this model, with a particular focus on its latent space for facial expression descriptors, and uncover several limitations with its ability to express intense face motions. To address these limitations, we propose substantial changes in both training pipeline and model architecture, to introduce our EMOPortraits model, where we: Enhance the model's capability to faithfully support intense, asymmetric face expressions, setting a new state-of-the-art result in the emotion transfer task, surpassing previous methods in both metrics and quality. Incorporate speech-driven mode to our model, achieving top-tier performance in audio-driven facial animation, making it possible to drive source identity through diverse modalities, including visual signal, audio, or a blend of both. We propose a novel multi-view video dataset featuring a wide range of intense and asymmetric facial expressions, filling the gap with absence of such data in existing datasets.

### OmniSeg3D: Omniversal 3D Segmentation via Hierarchical Contrastive Learning.
- **链接**: [arXiv:2311.11666](https://arxiv.org/abs/2311.11666) · 📚 被引 52
- **作者**: Haiyang Ying, Yixuan Yin, Jinzhi Zhang, Fan Wang, Tao Yu, Ruqi Huang et al.
- **🏷️ 机构**: Tsinghua University, Alibaba Group
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Towards holistic understanding of 3D scenes, a general 3D segmentation method is needed that can segment diverse objects without restrictions on object quantity or categories, while also reflecting the inherent hierarchical structure. To achieve this, we propose OmniSeg3D, an omniversal segmentation method aims for segmenting anything in 3D all at once. The key insight is to lift multi-view inconsistent 2D segmentations into a consistent 3D feature field through a hierarchical contrastive learning framework, which is accomplished by two steps. Firstly, we design a novel hierarchical representation based on category-agnostic 2D segmentations to model the multi-level relationship among pixels. Secondly, image features rendered from the 3D feature field are clustered at different levels, which can be further drawn closer or pushed apart according to the hierarchical relationship between different levels. In tackling the challenges posed by inconsistent 2D segmentations, this framework yields a global consistent 3D feature field, which further enables hierarchical segmentation, multi-object selection, and global discretization. Extensive experiments demonstrate the effectiveness of our method on high-quality 3D segmentation and accurate hierarchical structure understanding. A graphical user interface further facilitates flexible interaction for omniversal 3D segmentation.

## 跨领域论文（完整笔记在其他领域）

- CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. → [3d-detection](../3d-detection/Guideline%202024.md)
- Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications. → [3d-detection](../3d-detection/Guideline%202024.md)
- Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors. → [3d-detection](../3d-detection/Guideline%202024.md)
- ADA-Track: End-to-End Multi-Camera 3D Multi-Object Tracking with Alternating Detection and Association. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- RCBEVDet: Radar-Camera Fusion in Bird's Eye View for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- VSRD: Instance-Aware Volumetric Silhouette Rendering for Weakly Supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Multi-View Attentive Contextualization for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- From a Bird's Eye View to See: Joint Camera and Subject Registration without the Camera Calibration. → [bev](../bev/Guideline%202024.md)
- SelfOcc: Self-Supervised Vision-Based 3D Occupancy Prediction. → [3d-detection](../3d-detection/Guideline%202024.md)
- Adaptive Fusion of Single-View and Multi-View Depth for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- MVIP-NeRF: Multi-View 3D Inpainting on NeRF Scenes via Diffusion Prior. → [knowledge-distillation](../knowledge-distillation/Guideline%202024.md)
- Physical 3D Adversarial Attacks against Monocular Depth Estimation in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Driving Into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- DriveWorld: 4D Pre-Trained Scene Understanding via World Models for Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202024.md)
- Volumetric Environment Representation for Vision-Language Navigation. → [3d-detection](../3d-detection/Guideline%202024.md)
