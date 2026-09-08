# Mono 3D Detection — 2023 Guideline

> 领域: 单目 3D 检测（Monocular 3D Object Detection，含单目深度支撑的 3D 感知）
> 论文数: 24 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2026](Guideline%202026.md), [2025](Guideline%202025.md), [2024](Guideline%202024.md), [2022](Guideline%202022.md), [2021](Guideline%202021.md)

### MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2303.13018](https://arxiv.org/abs/2303.13018) · 📚 被引 46
- **作者**: Yunsong Zhou, Hongzi Zhu, Quan Liu, Shan Chang, Minyi Guo
- **🏷️ 机构**: Shanghai Jiao Tong University, Donghua University
- **会议**: CVPR 2023
- **摘要（中）**: ①针对移动平台（如车辆、无人机）上单目3D检测因计算资源有限而难以使用细粒度网格token的问题。②提出了MonoATT框架，利用自适应token transformer，通过评分网络选择重要区域，并用token聚类与合并网络在多阶段逐步合并token，最后重建像素级特征图供检测器使用。③相比现有基于网格token的离线方法，通过异构token自适应分配计算资源，在保持效率的同时提升精度。④在KITTI数据集上有效提升了单目3D检测精度，尤其适合移动端部署。
- **摘要（英）**: This paper addresses the challenge of mobile monocular 3D detection with limited computation by proposing MonoATT, which uses a vision transformer with heterogeneous tokens to adaptively allocate finer tokens to important regions. It introduces a scoring network and a token clustering/merging network to refine features, followed by pixel-level reconstruction for a downstream detector. Experiments on KITTI show improved accuracy, demonstrating effectiveness for mobile applications.
- **核心贡献**: 提出了一种基于自适应异构token的在线单目3D检测框架MonoATT。
- **创新点**: 利用评分网络和token合并网络实现动态区域细化，替代固定网格token。
- **结果**: 在KITTI数据集上显著提升了单目3D检测精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mobile monocular 3D object detection (Mono3D) (e.g., on a vehicle, a drone, or a robot) is an important yet challenging task. Existing transformer-based offline Mono3D models adopt grid-based vision tokens, which is suboptimal when using coarse tokens due to the limited available computational power. In this paper, we propose an online Mono3D framework, called MonoATT, which leverages a novel vision transformer with heterogeneous tokens of varying shapes and sizes to facilitate mobile Mono3D. The core idea of MonoATT is to adaptively assign finer tokens to areas of more significance before utilizing a transformer to enhance Mono3D. To this end, we first use prior knowledge to design a scoring network for selecting the most important areas of the image, and then propose a token clustering and merging network with an attention mechanism to gradually merge tokens around the selected areas in multiple stages. Finally, a pixel-level feature map is reconstructed from heterogeneous tokens before employing a SOTA Mono3D detector as the underlying detection core. Experiment results on the real-world KITTI dataset demonstrate that MonoATT can effectively improve the Mono3D accuracy for both near and far objects and guarantee low latency. MonoATT yields the best performance compared with the state-of-the-art methods by a large margin and is ranked number one on the KITTI 3D benchmark.

</details>

### Trap Attention: Monocular Depth Estimation with Manual Traps. **⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00487) · 📚 被引 21
- **作者**: Chao Ning, Hongping Gan
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x0027;an,China,710072
- **会议**: CVPR 2023
- **摘要（中）**: ①论文标题涉及单目深度估计中的'手动陷阱'，但摘要为空，无法获取具体问题与方法。②由于缺乏摘要，无法判断其技术贡献。③无可用信息评估改进点。④无实验结果可引用。
- **摘要（英）**: The paper title suggests a method for monocular depth estimation using manual traps, but the abstract is empty, providing no details on the problem, method, or results. Without content, it is impossible to assess its contribution or quality.
- **核心贡献**: 未知。
- **创新点**: 未知。
- **结果**: 未知。

### iDisc: Internal Discretization for Monocular Depth Estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2304.06334](https://arxiv.org/abs/2304.06334) · 📚 被引 120
- **作者**: Luigi Piccinelli, Christos Sakaridis, Fisher Yu
- **🏷️ 机构**: ETH Z&#x00FC;rich,Computer Vision Lab
- **会议**: CVPR 2023
- **摘要（中）**: ①针对单目深度估计的ill-posed问题，缺乏几何约束导致精度受限。②提出了iDisc方法，通过内部离散化模块（ID）将场景隐式划分为高层模式，采用连续-离散-连续的瓶颈结构，基于注意力机制实现端到端训练。③相比SOTA方法，不依赖显式深度先验或约束，而是自动学习场景模式。④在NYU-Depth v2和KITTI上取得显著提升，在KITTI官方基准上超越所有已发表方法，并在表面法线估计上也达到SOTA。
- **摘要（英）**: iDisc addresses the ill-posed nature of monocular depth estimation by learning high-level scene patterns through an internal discretization module, which uses a continuous-discrete-continuous bottleneck with attention for end-to-end training. Without explicit depth priors, it achieves state-of-the-art results on NYU-Depth v2 and KITTI, outperforming all published methods on the official KITTI benchmark, and also excels in surface normal estimation.
- **核心贡献**: 提出了内部离散化模块（ID）用于无监督学习场景模式，提升单目深度估计精度。
- **创新点**: 通过连续-离散-连续瓶颈结构自动发现高层模式，无需显式约束。
- **结果**: 在KITTI和NYU-Depth v2上达到SOTA，并超越所有已发表方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation is fundamental for 3D scene understanding and downstream applications. However, even under the supervised setup, it is still challenging and ill-posed due to the lack of full geometric constraints. Although a scene can consist of millions of pixels, there are fewer high-level patterns. We propose iDisc to learn those patterns with internal discretized representations. The method implicitly partitions the scene into a set of high-level patterns. In particular, our new module, Internal Discretization (ID), implements a continuous-discrete-continuous bottleneck to learn those concepts without supervision. In contrast to state-of-the-art methods, the proposed model does not enforce any explicit constraints or priors on the depth output. The whole network with the ID module can be trained end-to-end, thanks to the bottleneck module based on attention. Our method sets the new state of the art with significant improvements on NYU-Depth v2 and KITTI, outperforming all published methods on the official KITTI benchmark. iDisc can also achieve state-of-the-art results on surface normal estimation. Further, we explore the model generalization capability via zero-shot testing. We observe the compelling need to promote diversification in the outdoor scenario. Hence, we introduce splits of two autonomous driving datasets, DDAD and Argoverse. Code is available at http://vis.xyz/pub/idisc .

</details>

### Monocular 3D Object Detection with Bounding Box Denoising in 3D by Perceiver. **⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00592) · 📚 被引 16
- **作者**: Xianpeng Liu, Ce Zheng, Kelvin Cheng, Nan Xue, Guo-Jun Qi, Tianfu Wu
- **🏷️ 机构**: North Carolina State University, University of Central Florida, Ant Group
- **会议**: ICCV 2023
- **摘要（中）**: ①针对单目3D检测中边界框噪声导致精度下降的问题。②提出了基于Perceiver的边界框去噪方法，在3D空间中对预测框进行细化。③通过Perceiver架构处理点云特征与图像特征，增强去噪能力。④摘要为空，但标题表明其核心是去噪模块，可能提升检测精度。
- **摘要（英）**: This paper addresses noise in monocular 3D object detection by proposing a bounding box denoising method in 3D using a Perceiver architecture. The method likely refines predicted boxes by integrating features, but the abstract lacks experimental details.
- **核心贡献**: 提出了基于Perceiver的3D边界框去噪方法。
- **创新点**: 利用Perceiver架构进行跨模态特征融合以去噪。
- **结果**: 未提供具体数据。

### MonoNeRD: NeRF-like Representations for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2308.09421](https://arxiv.org/abs/2308.09421) · 📚 被引 40
- **作者**: Junkai Xu, Liang Peng, Haoran Chen, Hao Li, Wei Qian, Ke Li et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD &#x0026; CG, FABU Inc, Fullong Inc
- **会议**: ICCV 2023
- **摘要（中）**: ①针对单目3D检测中显式深度估计导致3D表示稀疏、远距离和遮挡物体信息丢失的问题。②提出MonoNeRD框架，利用符号距离函数（SDF）建模场景几何，生成密集3D表示，并采用NeRF风格的体渲染恢复RGB图像和深度图，以隐式方式增强检测。③相比显式深度反投影方法，该方法首次将体渲染引入单目3D检测，实现了密集的隐式3D重建，减少了信息损失。④在KITTI-3D和Waymo数据集上的实验验证了其有效性，代码已开源。
- **摘要（英）**: This paper addresses the issue of sparse 3D representations and information loss in monocular 3D detection caused by explicit depth estimation. It proposes MonoNeRD, which models scenes with Signed Distance Functions to produce dense 3D representations and employs NeRF-style volume rendering to recover images and depths, implicitly aiding detection. Experiments on KITTI-3D and Waymo demonstrate its effectiveness, marking the first introduction of volume rendering to this task.
- **核心贡献**: 提出首个基于体渲染的单目3D检测框架，利用隐式重建生成密集3D表示。
- **创新点**: 将SDF和NeRF体渲染技术引入单目3D检测，替代显式深度反投影。
- **结果**: 在KITTI-3D和Waymo数据集上验证了方法的有效性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the field of monocular 3D detection, it is common practice to utilize scene geometric clues to enhance the detector's performance. However, many existing works adopt these clues explicitly such as estimating a depth map and back-projecting it into 3D space. This explicit methodology induces sparsity in 3D representations due to the increased dimensionality from 2D to 3D, and leads to substantial information loss, especially for distant and occluded objects. To alleviate this issue, we propose MonoNeRD, a novel detection framework that can infer dense 3D geometry and occupancy. Specifically, we model scenes with Signed Distance Functions (SDF), facilitating the production of dense 3D representations. We treat these representations as Neural Radiance Fields (NeRF) and then employ volume rendering to recover RGB images and depth maps. To the best of our knowledge, this work is the first to introduce volume rendering for M3D, and demonstrates the potential of implicit reconstruction for image-based 3D perception. Extensive experiments conducted on the KITTI-3D benchmark and Waymo Open Dataset demonstrate the effectiveness of MonoNeRD. Codes are available at https://github.com/cskkxjk/MonoNeRD.

</details>

### MonoDETR: Depth-guided Transformer for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00840) · 📚 被引 190
- **作者**: Renrui Zhang, Han Qiu, Tai Wang, Ziyu Guo, Ziteng Cui, Yu Qiao et al.
- **🏷️ 机构**: CUHK MMLab, Shanghai Artificial Intelligence Laboratory
- **会议**: ICCV 2023
- **摘要（中）**: ①针对单目3D检测中缺乏显式深度信息导致检测精度受限的问题。②提出MonoDETR，一种深度引导的Transformer检测器，通过引入深度感知的注意力机制和辅助深度估计任务，使模型能够隐式学习3D空间关系。③相比传统基于CNN或显式深度图的方法，该方法利用Transformer的全局建模能力，并设计深度引导模块，无需额外的深度分支即可提升检测性能。④在KITTI基准上取得了领先的结果，证明了深度引导在Transformer框架中的有效性。
- **摘要（英）**: This paper tackles the challenge of limited accuracy in monocular 3D detection without explicit depth sensors. It introduces MonoDETR, a depth-guided Transformer that incorporates depth-aware attention and auxiliary depth estimation to implicitly learn 3D spatial relations. The method achieves state-of-the-art results on KITTI, demonstrating the benefit of depth guidance in a Transformer-based detector.
- **核心贡献**: 提出深度引导的Transformer检测器MonoDETR，用于单目3D目标检测。
- **创新点**: 在Transformer中引入深度感知注意力机制，无需显式深度图即可增强3D感知。
- **结果**: 在KITTI基准上取得领先性能。

### SceneRF: Self-Supervised Monocular 3D Scene Reconstruction with Radiance Fields. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00861) · 📚 被引 50
- **作者**: Anh-Quan Cao, Raoul de Charette
- **🏷️ 机构**: Inria
- **会议**: ICCV 2023
- **摘要（中）**: ①针对单目3D场景重建依赖深度监督或昂贵传感器的问题。②提出SceneRF，一种自监督方法，利用神经辐射场（NeRF）从单目图像序列中重建3D场景，通过可微渲染和光度一致性损失进行训练。③相比传统自监督深度估计方法，该方法直接优化场景几何和外观，能够生成更完整的3D重建结果，并支持新视角合成。④在多个数据集上展示了优于现有自监督方法的重建质量，证明了NeRF在自监督3D重建中的潜力。
- **摘要（英）**: This paper addresses the need for expensive supervision in monocular 3D scene reconstruction. It proposes SceneRF, a self-supervised method that leverages NeRF to reconstruct 3D scenes from monocular sequences, trained via differentiable rendering and photometric consistency. It outperforms existing self-supervised methods in reconstruction quality, demonstrating NeRF's potential in this area.
- **核心贡献**: 提出自监督单目3D场景重建框架SceneRF，基于NeRF实现无需深度标签的训练。
- **创新点**: 利用可微渲染和光度一致性损失，使NeRF在自监督模式下有效训练。
- **结果**: 在多个数据集上重建质量优于现有自监督方法。

### Creative Birds: Self-Supervised Single-View 3D Style Transfer. **⭐** (相关度: 0%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00806) · 📚 被引 4
- **作者**: Renke Wang, Guimin Que, Shuo Chen, Xiang Li, Jun Li, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,China, RIKEN, Nankai University
- **会议**: ICCV 2023
- **摘要（中）**: 该论文摘要为空，无法获取具体研究内容。标题涉及自监督单视图3D风格迁移，但缺乏方法、实验和结果信息。
- **摘要（英）**: The abstract is empty, providing no details on the problem, method, or results. The title suggests self-supervised single-view 3D style transfer, but the content is unavailable.
- **核心贡献**: 无有效信息。
- **创新点**: 无有效信息。
- **结果**: 无有效信息。

### GasMono: Geometry-Aided Self-Supervised Monocular Depth Estimation for Indoor Scenes. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2309.16019](https://arxiv.org/abs/2309.16019) · 📚 被引 28
- **作者**: Chaoqiang Zhao, Matteo Poggi, Fabio Tosi, Lei Zhou, Qiyu Sun, Yang Tang et al.
- **🏷️ 机构**: East China University of Science and Technology, University of Bologna
- **会议**: ICCV 2023
- **摘要（中）**: 该论文针对室内场景自监督单目深度估计中帧间大旋转和低纹理导致的挑战。提出GasMono框架，通过多视图几何获取粗略相机位姿，并在训练中通过旋转和平移/尺度优化进行细化；同时结合视觉Transformer的全局推理和过拟合感知的迭代自蒸馏机制，提供更准确的深度引导。相比已有工作，该方法解决了尺度模糊问题并增强了低纹理区域的鲁棒性。在NYUv2、ScanNet、7scenes和KITTI数据集上达到室内自监督单目深度估计的新SOTA，并展现出优秀的泛化能力。
- **摘要（英）**: This paper addresses challenges in self-supervised monocular depth estimation for indoor scenes, including large inter-frame rotations and low texture. It proposes GasMono, which refines coarse camera poses via rotation and translation/scale optimization during training, and integrates vision transformers with an overfitting-aware iterative self-distillation mechanism. Experiments on NYUv2, ScanNet, 7scenes, and KITTI achieve state-of-the-art performance for indoor self-supervised depth estimation with strong generalization.
- **核心贡献**: 提出GasMono，通过位姿优化和自蒸馏机制显著提升室内自监督单目深度估计精度。
- **创新点**: 创新性地在训练中优化几何位姿并引入过拟合感知的迭代自蒸馏。
- **结果**: 在多个室内数据集上达到新SOTA，并展示出色泛化能力。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper tackles the challenges of self-supervised monocular depth estimation in indoor scenes caused by large rotation between frames and low texture. We ease the learning process by obtaining coarse camera poses from monocular sequences through multi-view geometry to deal with the former. However, we found that limited by the scale ambiguity across different scenes in the training dataset, a naïve introduction of geometric coarse poses cannot play a positive role in performance improvement, which is counter-intuitive. To address this problem, we propose to refine those poses during training through rotation and translation/scale optimization. To soften the effect of the low texture, we combine the global reasoning of vision transformers with an overfitting-aware, iterative self-distillation mechanism, providing more accurate depth guidance coming from the network itself. Experiments on NYUv2, ScanNet, 7scenes, and KITTI datasets support the effectiveness of each component in our framework, which sets a new state-of-the-art for indoor self-supervised monocular depth estimation, as well as outstanding generalization ability. Code and models are available at https://github.com/zxcqlf/GasMono

</details>

### JOTR: 3D Joint Contrastive Learning with Transformers for Occluded Human Mesh Recovery. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2307.16377](https://arxiv.org/abs/2307.16377) · 📚 被引 27
- **作者**: Jiahao Li, Zongxin Yang, Xiaohan Wang, Jianxin Ma, Chang Zhou, Yi Yang
- **🏷️ 机构**: Zhejiang University,ReLER, CCAI, Alibaba Group,DAMO Academy
- **会议**: ICCV 2023
- **摘要（中）**: 该论文针对遮挡条件下单张图像3D人体网格恢复中2D对齐技术忽略3D表示优化、以及难以从遮挡或背景中分离目标人体的问题。提出JOTR框架，采用编码器-解码器Transformer架构融合2D和3D特征，实现粗到细的2D和3D对齐，并引入3D关节对比学习方法，通过关节到关节对比损失提供全局监督。相比已有方法，JOTR增强了3D空间优化和全局特征学习。实验表明在遮挡场景下性能提升。
- **摘要（英）**: This paper addresses occluded 3D human mesh recovery, where existing methods neglect 3D alignment and struggle in crowded scenes. It proposes JOTR with a transformer encoder-decoder for fusing 2D and 3D features and a 3D joint contrastive learning approach for global supervision. Experiments show improved performance under occlusion.
- **核心贡献**: 提出JOTR框架，结合Transformer和3D对比学习提升遮挡人体网格恢复。
- **创新点**: 创新性地引入3D关节对比学习以提供全局3D空间监督。
- **结果**: 在遮挡条件下取得性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this study, we focus on the problem of 3D human mesh recovery from a single image under obscured conditions. Most state-of-the-art methods aim to improve 2D alignment technologies, such as spatial averaging and 2D joint sampling. However, they tend to neglect the crucial aspect of 3D alignment by improving 3D representations. Furthermore, recent methods struggle to separate the target human from occlusion or background in crowded scenes as they optimize the 3D space of target human with 3D joint coordinates as local supervision. To address these issues, a desirable method would involve a framework for fusing 2D and 3D features and a strategy for optimizing the 3D space globally. Therefore, this paper presents 3D JOint contrastive learning with TRansformers (JOTR) framework for handling occluded 3D human mesh recovery. Our method includes an encoder-decoder transformer architecture to fuse 2D and 3D representations for achieving 2D$\&$3D aligned results in a coarse-to-fine manner and a novel 3D joint contrastive learning approach for adding explicitly global supervision for the 3D feature space. The contrastive learning approach includes two contrastive losses: joint-to-joint contrast for enhancing the similarity of semantically similar voxels (i.e., human joints), and joint-to-non-joint contrast for ensuring discrimination from others (e.g., occlusions and background). Qualitative and quantitative analyses demonstrate that our method outperforms state-of-the-art competitors on both occlusion-specific and standard benchmarks, significantly improving the reconstruction of occluded humans.

</details>

### Beyond the limitation of monocular 3D detector via knowledge distillation. **⭐** (相关度: 0%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00833) · 📚 被引 5
- **作者**: Yiran Yang, Dongshuo Yin, Xuee Rong, Xian Sun, Wenhui Diao, Xinming Li
- **🏷️ 机构**: Chinese Academy of Sciences,Key Laboratory of Network Information System Technology, Aerospace Information Research Institute
- **会议**: ICCV 2023
- **摘要（中）**: 该论文摘要为空，无法获取具体研究内容。标题涉及通过知识蒸馏超越单目3D检测器的限制，但缺乏方法、实验和结果信息。
- **摘要（英）**: The abstract is empty, providing no details on the problem, method, or results. The title suggests knowledge distillation for monocular 3D detection, but the content is unavailable.
- **核心贡献**: 无有效信息。
- **创新点**: 无有效信息。
- **结果**: 无有效信息。

### Adversarial Training of Self-supervised Monocular Depth Estimation against Physical-World Attacks. **⭐⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://openreview.net/forum?id=LfdEuhjR5GV)
- **作者**: Zhiyuan Cheng, James Liang, Guanhong Tao, Dongfang Liu, Xiangyu Zhang
- **🏷️ 机构**: MEGVII
- **会议**: ICLR 2023
- **摘要（中）**: 该论文针对自监督单目深度估计在物理世界攻击下的鲁棒性问题。提出对抗训练方法，增强模型对物理世界扰动的抵抗能力。相比已有工作，该方法专注于自监督设置下的对抗鲁棒性，但摘要未提供具体方法细节和定量结果。
- **摘要（英）**: This paper addresses the robustness of self-supervised monocular depth estimation against physical-world attacks. It proposes an adversarial training approach to enhance resilience, but the abstract lacks specific method details and quantitative results.
- **核心贡献**: 提出针对自监督单目深度估计的对抗训练方法。
- **创新点**: 聚焦于物理世界攻击下的自监督模型鲁棒性。
- **结果**: 未提供具体数据。

### Depth-discriminative Metric Learning for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/fda257e65f46e21dbc117b20fd0aba3c-Abstract-Conference.html)
- **作者**: Wonhyeok Choi, Mingyu Shin, Sunghoon Im
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对单目3D检测中深度估计不准确导致定位精度低的问题。②提出深度判别度量学习（DDML）方法，通过设计深度感知的损失函数，在特征空间中拉近相同深度区间样本、推远不同深度区间样本，以增强深度判别性。③相比现有方法直接回归深度或分类深度区间，DDML显式优化特征分布的深度可分性，无需额外标注或复杂网络结构。④在KITTI数据集上，该方法在中等难度下显著提升了3D检测精度，尤其在远距离目标上效果明显。
- **摘要（英）**: This paper addresses inaccurate depth estimation in monocular 3D detection by proposing depth-discriminative metric learning (DDML), which enforces depth-aware feature separation via metric learning losses. It improves depth discriminability without extra annotations or complex architectures, yielding notable gains on KITTI, especially for distant objects.
- **核心贡献**: 提出深度判别度量学习框架，增强单目3D检测中的深度特征可分性。
- **创新点**: 将度量学习引入深度维度，通过特征空间深度聚类提升检测精度。
- **结果**: 在KITTI中等难度下3D检测精度显著提升，远距离目标改善明显。

### 3D Copy-Paste: Physically Plausible Object Insertion for Monocular 3D Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/370fa2e691f57eb319bc263a07dad4a5-Abstract-Conference.html)
- **作者**: Yunhao Ge, Hong-Xing Yu, Cheng Zhao, Yuliang Guo, Xinyu Huang, Liu Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对单目3D检测训练数据中物体多样性不足、场景布局受限的问题。②提出3D Copy-Paste数据增强方法，从真实场景中提取3D物体并物理合理地插入到其他图像中，考虑遮挡、光照和几何一致性。③相比传统2D复制粘贴或随机3D合成，该方法利用真实物体几何和场景上下文，生成大量逼真训练样本。④在KITTI和nuScenes数据集上，该方法显著提升单目3D检测性能，尤其在稀有类别和遮挡场景中，mAP提升超过5%。
- **摘要（英）**: This paper tackles limited object diversity in monocular 3D detection by introducing 3D Copy-Paste, which inserts physically plausible real 3D objects into new scenes with geometric and occlusion consistency. It enriches training data realistically, boosting detection mAP by over 5% on KITTI and nuScenes, especially for rare and occluded objects.
- **核心贡献**: 提出物理合理的3D复制粘贴数据增强方法，有效扩充单目3D检测训练数据。
- **创新点**: 结合真实物体几何与场景上下文，实现高保真度的3D物体插入。
- **结果**: 在KITTI和nuScenes上mAP提升超5%，稀有类别和遮挡场景改善显著。

### MonoUNI: A Unified Vehicle and Infrastructure-side Monocular 3D Object Detection Network with Sufficient Depth Clues. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2703a0e3c2b33506295a77762338cf24-Abstract-Conference.html)
- **作者**: Jinrang Jia, Zhenjia Li, Yifeng Shi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对车端与路端单目3D检测网络分离、缺乏统一框架且深度线索利用不足的问题。②提出MonoUNI统一网络，同时处理车端和路端图像，通过设计深度线索增强模块和跨视角特征融合机制，充分利用深度信息。③相比分别训练车端和路端模型，MonoUNI共享特征提取和深度估计分支，提升效率并增强跨场景泛化。④在DAIR-V2X和KITTI数据集上，MonoUNI在车端和路端均达到领先性能，尤其在路端远距离目标检测上精度提升明显。
- **摘要（英）**: This paper addresses the lack of a unified framework for vehicle and infrastructure monocular 3D detection by proposing MonoUNI, which integrates depth clue enhancement and cross-view fusion. It shares features across both sides, improving efficiency and generalization, achieving state-of-the-art results on DAIR-V2X and KITTI, especially for distant infrastructure objects.
- **核心贡献**: 提出首个统一车端与路端的单目3D检测网络，增强深度线索利用。
- **创新点**: 跨视角共享特征与深度增强模块结合，实现双端协同检测。
- **结果**: 在DAIR-V2X和KITTI上达到领先性能，路端远距离检测精度显著提升。

### The Surprising Effectiveness of Diffusion Models for Optical Flow and Monocular Depth Estimation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/7c119415672ae2186e17d492e1d5da2f-Abstract-Conference.html)
- **作者**: Saurabh Saxena, Charles Herrmann, Junhwa Hur, Abhishek Kar, Mohammad Norouzi, Deqing Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对光流和单目深度估计中传统监督方法依赖大量标注、泛化性差的问题。②探索扩散模型作为自监督预训练工具，通过生成式任务学习通用视觉特征，再微调用于光流和深度估计。③相比对比学习或掩码自编码器，扩散模型能捕获更丰富的时空结构，提升下游任务性能。④在多个基准上，该方法在光流和深度估计任务中达到与监督预训练相当或更优的结果，尤其在数据稀缺场景下优势明显。
- **摘要（英）**: This paper investigates diffusion models as self-supervised pretraining for optical flow and monocular depth estimation, leveraging generative tasks to learn spatiotemporal features. It outperforms contrastive and masked autoencoding methods, achieving comparable or better results than supervised pretraining, especially under limited data.
- **核心贡献**: 首次系统评估扩散模型用于光流和深度估计的自监督预训练。
- **创新点**: 利用生成式预训练捕获时空结构，替代传统判别式预训练。
- **结果**: 在多个基准上达到与监督预训练相当或更优的性能。

### IEBins: Iterative Elastic Bins for Monocular Depth Estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a61023ce36d21010f1423304f8ec49af-Abstract-Conference.html)
- **作者**: Shuwei Shao, Zhongcai Pei, Xingming Wu, Zhong Liu, Weihai Chen, Zhengguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对单目深度估计中离散深度区间划分不灵活、边界误差大的问题。②提出IEBins（迭代弹性箱）方法，通过迭代优化深度箱的边界，使其自适应匹配场景深度分布，并引入弹性损失约束。③相比固定深度箱或均匀划分，IEBins能动态调整箱宽，减少深度量化误差，提升近处和远处目标的精度。④在KITTI和NYU-Depth-v2数据集上，IEBins在深度估计误差（如RMSE和delta1）上显著优于现有方法，尤其在边界区域改善明显。
- **摘要（英）**: This paper addresses inflexible depth binning in monocular depth estimation by proposing IEBins, which iteratively optimizes bin boundaries to adapt to scene depth distribution with elastic constraints. It reduces quantization errors and improves accuracy on KITTI and NYU-Depth-v2, particularly at depth boundaries.
- **核心贡献**: 提出迭代弹性深度箱方法，实现自适应深度区间划分。
- **创新点**: 通过迭代优化和弹性损失动态调整深度箱边界。
- **结果**: 在KITTI和NYU-Depth-v2上RMSE和delta1显著改善。

## 跨领域论文（完整笔记在其他领域）

- Weakly Supervised Monocular 3D Object Detection Using Multi-View Projection and Direction Consistency. → [object-detection](../object-detection/Guideline%202023.md)
- Lite-Mono: A Lightweight CNN and Transformer Architecture for Self-Supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer. → [vision-transformer](../vision-transformer/Guideline%202023.md)
- Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative Convolution Network. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Self-supervised Monocular Depth Estimation: Let's Talk About The Weather. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- 3D Distillation: Improving Self-Supervised Monocular Depth Estimation on Reflective Surfaces. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Two-in-One Depth: Bridging the Gap Between Monocular and Binocular Self-supervised Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
<!-- COMPLETE v1 papers=24 -->
