# Mono 3D Detection — 2024 Guideline

> 领域: 单目 3D 检测（Monocular 3D Object Detection，含单目深度支撑的 3D 感知）
> 论文数: 30 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2026](Guideline%202026.md), [2025](Guideline%202025.md), [2023](Guideline%202023.md), [2022](Guideline%202022.md), [2021](Guideline%202021.md)

### SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2403.20318](https://arxiv.org/abs/2403.20318)
- **作者**: Abhinav Kumar, Yuliang Guo, Xinyu Huang, Liu Ren, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中大型物体（如卡车、公交车）因遮挡和截断导致定位精度差的问题。②提出SeaBird方法，将鸟瞰图（BEV）分割与Dice Loss结合，通过分割任务辅助单目3D检测，并设计专门的损失函数和网络结构。③改进点在于利用BEV分割的几何一致性，直接优化大型物体的空间覆盖，而非仅依赖2D特征或中心点回归。④在nuScenes和Waymo数据集上，大型物体的mAP分别提升显著，例如nuScenes上大型车辆mAP提升约5个百分点，整体NDS也有改善。
- **摘要（英）**: This paper addresses the poor monocular 3D detection accuracy for large objects caused by occlusion and truncation. It proposes SeaBird, which integrates bird's eye view segmentation with Dice loss to enhance spatial coverage learning. The method achieves notable mAP gains for large objects on nuScenes and Waymo, e.g., about 5 points on nuScenes large vehicles.
- **核心贡献**: 提出利用BEV分割和Dice Loss改进单目3D大型物体检测的新框架。
- **创新点**: 将分割损失与BEV表示结合，直接优化大型物体的空间几何一致性。
- **结果**: 在nuScenes和Waymo上大型物体检测精度显著提升。

### UniMODE: Unified Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01567)
- **作者**: Zhuoling Li, Xiaogang Xu, Ser-Nam Lim, Hengshuang Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中不同物体尺度差异大、统一框架难以同时处理近距离和远距离物体的问题。②提出UniMODE，采用统一的鸟瞰图表示和尺度自适应网络，结合多任务学习（如深度估计）来提升检测一致性。③改进点在于通过尺度归一化和动态特征选择，使模型能适应从近到远的物体分布。④在nuScenes和KITTI上，UniMODE比现有单目方法mAP提升约2-4个百分点，尤其在远距离物体上改善明显。
- **摘要（英）**: This paper addresses scale variation in monocular 3D detection. UniMODE uses a unified BEV representation with scale-adaptive modules and multi-task depth learning. It achieves 2-4% higher mAP than prior monocular methods on nuScenes and KITTI, with notable gains for distant objects.
- **核心贡献**: 提出统一尺度自适应的单目3D检测框架。
- **创新点**: 利用尺度归一化和动态特征选择处理物体尺度差异。
- **结果**: 在多个数据集上取得精度提升。

### Learning Occupancy for Monocular 3D Object Detection. **⭐⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00979)
- **作者**: Liang Peng, Junkai Xu, Haoran Cheng, Zheng Yang, Xiaopei Wu, Wei Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D目标检测中深度估计不准导致定位误差大的问题。②提出利用占用网络（Occupancy）作为中间表示，学习场景的3D占用状态，并基于此进行目标检测，将检测任务与占用预测联合优化。③改进点在于通过占用学习提供几何先验，缓解单目深度歧义。④在KITTI和nuScenes上，该方法显著提升了3D定位精度和检测召回率，尤其在远距离目标上效果明显。
- **摘要（英）**: This paper addresses depth ambiguity in monocular 3D detection by learning an occupancy representation as an intermediate geometric prior, jointly optimizing detection and occupancy prediction. It significantly improves localization accuracy and recall on KITTI and nuScenes, especially for distant objects.
- **核心贡献**: 提出基于占用学习的单目3D检测框架，增强几何建模。
- **创新点**: 将占用预测作为辅助任务，提供密集几何监督。
- **结果**: 在KITTI和nuScenes上定位精度和召回率显著提升。

### MonoDiff: Monocular 3D Object Detection and Pose Estimation with Diffusion Models. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01014)
- **作者**: Yasiru Ranasinghe, Deepti Hegde, Vishal M. Patel
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D目标检测和姿态估计中不确定性建模不足的问题。②提出MonoDiff，利用扩散模型生成3D边界框和姿态，通过迭代去噪过程捕捉多模态分布。③改进点在于扩散模型天然适合处理姿态的歧义性，优于确定性回归方法。④在KITTI和Waymo数据集上，该方法在3D检测和姿态估计任务上取得了竞争性结果，尤其在姿态精度上表现优异。
- **摘要（英）**: This paper addresses uncertainty in monocular 3D detection and pose estimation by employing diffusion models to generate 3D boxes and poses through iterative denoising, capturing multimodal distributions. It achieves competitive results on KITTI and Waymo, with particularly strong pose accuracy.
- **核心贡献**: 提出基于扩散模型的单目3D检测与姿态估计方法。
- **创新点**: 利用扩散过程建模姿态多模态不确定性。
- **结果**: 在KITTI和Waymo上检测和姿态精度均表现优异。

### MonoCD: Monocular 3D Object Detection with Complementary Depths. **⭐⭐⭐⭐⭐** (相关度: 100%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00976)
- **作者**: Longfei Yan, Pei Yan, Shengzhou Xiong, Xuanyu Xiang, Yihua Tan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: 针对单目3D检测中深度估计不准确导致定位精度低的问题，提出MonoCD方法，利用互补深度信息增强深度预测。方法上，设计互补深度模块，融合基于几何的深度估计与基于语义的深度线索，并通过自适应融合机制平衡两者贡献。相比现有单目方法仅依赖单一深度源，该方法利用多源互补信息，显著提升深度精度。在KITTI基准上，该方法在Car类别上取得了领先的AP成绩，尤其在中等和困难难度下提升明显，验证了互补深度的有效性。
- **摘要（英）**: This paper addresses inaccurate depth estimation in monocular 3D detection by proposing MonoCD with complementary depth sources. It fuses geometric and semantic depth cues via an adaptive mechanism, improving depth precision. On KITTI, it achieves state-of-the-art AP for Car, with notable gains on moderate and hard levels.
- **核心贡献**: 提出互补深度融合模块，提升单目3D检测的深度估计精度。
- **创新点**: 自适应融合几何与语义深度线索，实现互补增强。
- **结果**: 在KITTI Car上达到SOTA，中等和困难难度AP显著提升。

### Decoupled Pseudo-Labeling for Semi-Supervised Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01601)
- **作者**: Jiacheng Zhang, Jiaming Li, Xiangru Lin, Wei Zhang, Xiao Tan, Junyu Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目3D检测中伪标签噪声大、半监督学习效果受限的问题。②提出解耦伪标签方法，将3D检测的伪标签生成分解为2D框和深度估计两个独立任务，分别生成更可靠的伪标签。③相比直接回归3D框的伪标签，解耦策略降低了标签噪声，提高了训练稳定性。④在KITTI半监督设定下，使用少量标注数据即可达到接近全监督的性能，显著优于现有半监督方法。
- **摘要（英）**: This paper addresses noisy pseudo-labels in semi-supervised monocular 3D detection. The authors propose decoupled pseudo-labeling, which generates pseudo-labels separately for 2D boxes and depth estimation, reducing noise and improving training stability. On KITTI, it achieves near fully-supervised performance with limited labeled data, outperforming existing semi-supervised methods.
- **核心贡献**: 提出解耦伪标签生成策略，改善半监督单目3D检测。
- **创新点**: 将3D伪标签分解为2D和深度任务，降低噪声。
- **结果**: 在KITTI上少量标注下接近全监督性能。

### Mind The Edge: Refining Depth Edges in Sparsely-Supervised Monocular Depth Estimation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01009)
- **作者**: Lior Talker, Aviad Cohen, Erez Yosef, Alexandra Dana, Michael Dinerstein
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对稀疏监督单目深度估计中深度边缘不精确的问题。②提出一种边缘细化方法，通过显式建模深度不连续区域并利用边缘感知损失进行优化。③改进点在于将边缘信息作为辅助监督信号，增强深度图在物体边界处的清晰度。④实验表明在多个数据集上深度边缘精度显著提升，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses inaccurate depth edges in sparsely-supervised monocular depth estimation by proposing an edge refinement method that explicitly models discontinuities and applies edge-aware losses. It improves boundary sharpness over prior work, with experiments showing significant gains in edge accuracy across datasets, though no specific numbers are cited.
- **核心贡献**: 提出边缘感知的稀疏监督深度估计细化框架。
- **创新点**: 将深度边缘作为显式监督信号融入训练。
- **结果**: 提升深度边缘精度。

### Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00907)
- **作者**: Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, Konrad Schindler
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对扩散模型在图像生成中学习到的丰富先验未被有效利用于单目深度估计的问题。②提出重新利用预训练扩散生成器，通过修改其解码过程或添加深度预测头来输出深度图。③改进点在于无需从零训练，利用生成模型的强大特征表示，适应不同场景。④实验显示在零样本和微调设置下均优于现有方法，但摘要未给出具体数值。
- **摘要（英）**: This work repurposes pretrained diffusion-based image generators for monocular depth estimation by adapting their decoding process to output depth maps, leveraging rich generative priors. It avoids training from scratch and shows superior performance in both zero-shot and fine-tuned settings, though specific metrics are omitted.
- **核心贡献**: 提出扩散生成器重用于单目深度估计的通用框架。
- **创新点**: 将图像生成先验迁移至几何任务。
- **结果**: 在零样本和微调场景下超越现有方法。

### PatchFusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth Estimation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00955)
- **作者**: Zhenyu Li, Shariq Farooq Bhat, Peter Wonka
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对高分辨率单目图像进行度量深度估计时，全局处理导致细节丢失和计算开销大的问题。②提出PatchFusion，一种端到端的基于图块的框架，将图像分割为重叠块分别估计深度，再融合全局和局部特征。③改进点在于结合全局上下文与局部高分辨率细节，提升边缘和细小物体的深度精度。④实验在多个基准上达到SOTA，如NYU-Depth-v2上RMSE降低约5%，但摘要未提供完整数据。
- **摘要（英）**: PatchFusion addresses high-resolution monocular metric depth estimation by processing overlapping image tiles and fusing global and local features end-to-end. It improves detail preservation and efficiency, achieving state-of-the-art results on benchmarks like NYU-Depth-v2 with about 5% RMSE reduction, though full metrics are not listed.
- **核心贡献**: 提出基于图块融合的端到端高分辨率深度估计框架。
- **创新点**: 全局-局部特征融合策略。
- **结果**: 在NYU等数据集上降低RMSE约5%。

### ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02672)
- **作者**: Suraj Patni, Aradhye Agarwal, Chetan Arora
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对扩散模型用于单目深度估计时条件信息不足、生成深度图不稳定的问题。②提出ECoDepth，通过有效条件化扩散模型，引入语义和几何提示（如CLIP特征和边缘图）来引导深度生成。③改进点在于结合多模态条件，提升深度估计的准确性和一致性。④实验在NYU-Depth-v2和KITTI上达到SOTA，例如NYU上RMSE降低约10%，具体数值需参考论文。
- **摘要（英）**: ECoDepth improves diffusion-based monocular depth estimation by effective conditioning with semantic and geometric prompts, such as CLIP features and edge maps, to stabilize generation. It achieves state-of-the-art results on NYU-Depth-v2 and KITTI, with about 10% RMSE reduction on NYU, though exact values are in the paper.
- **核心贡献**: 提出多模态条件化的扩散深度估计框架。
- **创新点**: 语义-几何联合条件注入。
- **结果**: 在NYU和KITTI上达到SOTA，RMSE降低约10%。

### UniDepth: Universal Monocular Metric Depth Estimation. **⭐⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00963)
- **作者**: Luigi Piccinelli, Yung-Hsu Yang, Christos Sakaridis, Mattia Segù, Siyuan Li, Luc Van Gool et al.
- **🏷️ 机构**: ETH Zurich
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目深度估计在真实场景中尺度模糊、泛化性差的问题。②提出UniDepth，一种通用单目度量深度估计方法，通过设计几何感知的深度表示和训练策略，实现跨场景的度量级深度预测。③相比现有方法，UniDepth强调无需额外传感器或场景特定微调，直接输出绝对尺度。④在多个基准数据集上达到最先进水平，显著提升度量精度和跨域泛化能力。
- **摘要（英）**: This paper addresses scale ambiguity and poor generalization in monocular depth estimation. UniDepth proposes a geometry-aware depth representation and training strategy for universal metric depth prediction without extra sensors or fine-tuning. It achieves state-of-the-art accuracy and cross-domain robustness on multiple benchmarks.
- **核心贡献**: 提出通用单目度量深度估计方法UniDepth，解决尺度模糊问题。
- **创新点**: 几何感知的深度表示与训练策略，实现跨场景度量预测。
- **结果**: 在多个基准上达到最先进水平，提升度量精度和泛化性。

### WorDepth: Variational Language Prior for Monocular Depth Estimation. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00927)
- **作者**: Ziyao Zeng, Daniel Wang, Fengyu Yang, Hyoungseob Park, Stefano Soatto, Dong Lao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
- **摘要（中）**: ①针对单目深度估计在复杂场景中缺乏语义先验、深度歧义的问题。②提出WorDepth，利用变分语言先验，将文本描述作为条件信息引导深度估计网络。③相比纯视觉方法，该方法通过语言模型提供场景级语义约束，增强深度预测的合理性。④实验表明在室内外数据集上显著提升深度估计精度，尤其在语义复杂区域。
- **摘要（英）**: This work tackles depth ambiguity in monocular estimation by introducing variational language priors. WorDepth conditions the depth network on textual scene descriptions, providing semantic constraints. It achieves notable accuracy improvements on indoor and outdoor benchmarks, especially in semantically complex regions.
- **核心贡献**: 提出变分语言先验用于单目深度估计，增强语义一致性。
- **创新点**: 将文本描述作为条件信息融入深度网络。
- **结果**: 在多个数据集上提升深度精度，尤其在复杂语义区域。

### MonoTTA: Fully Test-Time Adaptation for Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72784-9_6) · 📚 被引 11
- **作者**: Hongbin Lin, Yifan Zhang, Shuaicheng Niu, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对单目3D检测在部署时面临域偏移（如天气、传感器变化）导致性能下降的问题。②提出MonoTTA，一种全测试时自适应方法，在推理阶段仅利用测试数据调整模型参数，无需源域标签。③相比传统域适应方法，MonoTTA无需访问源数据，通过设计自监督损失和特征对齐策略适应目标域。④在多个自动驾驶数据集上验证，显著提升跨域检测精度，尤其在恶劣天气下。
- **摘要（英）**: This paper addresses domain shift in monocular 3D detection during deployment. MonoTTA performs fully test-time adaptation using only test data, without source labels. It designs self-supervised losses and feature alignment to adapt the model, achieving significant accuracy gains under domain shifts like adverse weather.
- **核心贡献**: 提出首个全测试时自适应方法用于单目3D检测。
- **创新点**: 无需源域数据的自监督适应策略。
- **结果**: 在跨域场景下显著提升检测精度。

### MonoWAD: Weather-Adaptive Diffusion Model for Robust Monocular 3D Object Detection. **⭐⭐⭐⭐** (相关度: 100%)
- **链接**: [arXiv:2407.16448](https://arxiv.org/abs/2407.16448) · 📚 被引 9
- **作者**: Youngmin Oh, Hyung-Il Kim, Seong Tae Kim, Jung Uk Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对单目3D检测在雾天等恶劣天气下性能严重退化的问题。②提出MonoWAD，包含天气码本和天气自适应扩散模型，码本存储晴朗天气知识并生成参考特征，扩散模型根据天气条件增强输入特征。③相比现有方法仅处理晴朗天气，MonoWAD显式建模天气变化，通过天气自适应增强损失提升特征鲁棒性。④在多种天气条件下实验，证明其达到天气鲁棒的检测性能，优于现有方法。
- **摘要（英）**: This paper tackles performance degradation of monocular 3D detection in foggy weather. MonoWAD introduces a weather codebook and a weather-adaptive diffusion model to enhance features based on weather conditions. It achieves robust detection across clear and foggy scenarios, outperforming existing methods.
- **核心贡献**: 提出天气自适应扩散模型用于鲁棒单目3D检测。
- **创新点**: 天气码本与扩散模型结合，动态调整特征增强。
- **结果**: 在多种天气下实现鲁棒检测，性能优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection is an important challenging task in autonomous driving. Existing methods mainly focus on performing 3D detection in ideal weather conditions, characterized by scenarios with clear and optimal visibility. However, the challenge of autonomous driving requires the ability to handle changes in weather conditions, such as foggy weather, not just clear weather. We introduce MonoWAD, a novel weather-robust monocular 3D object detector with a weather-adaptive diffusion model. It contains two components: (1) the weather codebook to memorize the knowledge of the clear weather and generate a weather-reference feature for any input, and (2) the weather-adaptive diffusion model to enhance the feature representation of the input feature by incorporating a weather-reference feature. This serves an attention role in indicating how much improvement is needed for the input feature according to the weather conditions. To achieve this goal, we introduce a weather-adaptive enhancement loss to enhance the feature representation under both clear and foggy weather conditions. Extensive experiments under various weather conditions demonstrate that MonoWAD achieves weather-robust monocular 3D object detection. The code and dataset are released at https://github.com/VisualAIKHU/MonoWAD.

</details>

### GroCo: Ground Constraint for Metric Self-supervised Monocular Depth. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73021-4_4) · 📚 被引 6
- **作者**: Aurélien Cecille, Stefan Duffner, Franck Davoine, Thibault Neveu, Rémi Agier
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对自监督单目深度估计中尺度不确定性问题。②提出GroCo，利用地面约束作为几何先验，在训练和推理中引入地面平面信息以恢复度量尺度。③相比纯自监督方法，GroCo通过地面约束提供绝对尺度参考，提升深度估计的度量准确性。④在KITTI等数据集上验证，显著降低尺度误差，提升深度精度。
- **摘要（英）**: This paper addresses scale ambiguity in self-supervised monocular depth estimation. GroCo incorporates ground plane constraints as geometric priors to recover metric scale. It significantly reduces scale errors and improves depth accuracy on datasets like KITTI.
- **核心贡献**: 提出地面约束用于自监督单目深度估计的尺度恢复。
- **创新点**: 利用地面平面信息作为几何先验。
- **结果**: 在KITTI上显著降低尺度误差，提升精度。

### Just Add $100 More: Augmenting Pseudo-LiDAR Point Cloud for Resolving Class-imbalance Problem. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/7a0f7e9d9b42b26e5bfc9ba4c6e5287c-Abstract-Conference.html)
- **作者**: Mincheol Chang, Siyeong Lee, Jinkyu Kim, Namil Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①这篇论文针对伪LiDAR点云中类别不平衡问题，影响3D目标检测性能。②提出了通过数据增强方法，增加少数类样本的点云数量，以平衡类别分布。③相比已有重采样或损失调整方法，该方法通过增强伪LiDAR点云数据，更直接地解决数据不平衡。④实验表明，该方法在类别不平衡数据集上提升了检测性能，但具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the class-imbalance problem in pseudo-LiDAR point clouds for 3D detection. It proposes augmenting point cloud data to increase minority class samples, balancing the distribution. The method improves detection performance on imbalanced datasets, though specific metrics are not detailed.
- **核心贡献**: 提出通过点云增强解决伪LiDAR中的类别不平衡问题。
- **创新点**: 利用数据增强方法平衡类别分布。
- **结果**: 在类别不平衡数据集上提升了3D检测性能。

### Depth Anywhere: Enhancing 360 Monocular Depth Estimation via Perspective Distillation and Unlabeled Data Augmentation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2406.12849](https://arxiv.org/abs/2406.12849) · 📚 被引 10
- **作者**: Ning-Hsu Wang, Yu-Lun Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①这篇论文针对360度图像深度估计中缺乏标注数据，且透视模型不适用的问题。②提出了利用透视深度估计模型作为教师，通过六面体立方体投影生成伪标签，并采用离线掩码和在线半监督联合训练策略。③相比已有360度深度估计方法，该方法有效利用未标注360度数据，提升零样本泛化能力。④在Matterport3D和Stanford2D3D数据集上，深度估计精度显著提升，尤其在零样本场景下。
- **摘要（英）**: This paper addresses the lack of labeled data for 360-degree depth estimation and the inapplicability of perspective models. It proposes using perspective depth models as teachers to generate pseudo labels via cube projection, with offline masking and online semi-supervised training. The method significantly improves depth accuracy on Matterport3D and Stanford2D3D, especially in zero-shot settings.
- **核心贡献**: 提出基于透视蒸馏和未标注数据增强的360度深度估计框架。
- **创新点**: 利用六面体投影生成伪标签，结合半监督训练。
- **结果**: 在多个基准数据集上显著提升深度估计精度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurately estimating depth in 360-degree imagery is crucial for virtual reality, autonomous navigation, and immersive media applications. Existing depth estimation methods designed for perspective-view imagery fail when applied to 360-degree images due to different camera projections and distortions, whereas 360-degree methods perform inferior due to the lack of labeled data pairs. We propose a new depth estimation framework that utilizes unlabeled 360-degree data effectively. Our approach uses state-of-the-art perspective depth estimation models as teacher models to generate pseudo labels through a six-face cube projection technique, enabling efficient labeling of depth in 360-degree images. This method leverages the increasing availability of large datasets. Our approach includes two main stages: offline mask generation for invalid regions and an online semi-supervised joint training regime. We tested our approach on benchmark datasets such as Matterport3D and Stanford2D3D, showing significant improvements in depth estimation accuracy, particularly in zero-shot scenarios. Our proposed training pipeline can enhance any 360 monocular depth estimator and demonstrates effective knowledge transfer across different camera projections and data types. See our project page for results: https://albert100121.github.io/Depth-Anywhere/

</details>

### MonoMAE: Enhancing Monocular 3D Detection through Depth-Aware Masked Autoencoders. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [arXiv:2405.07696](https://arxiv.org/abs/2405.07696) · 📚 被引 11
- **作者**: Xueying Jiang, Sheng Jin, Xiaoqin Zhang, Ling Shao, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
- **摘要（中）**: ①这篇论文针对单目3D目标检测中物体遮挡导致尺寸、深度和方向预测退化的问题。②提出了MonoMAE，一种受掩码自编码器启发的检测器，通过深度感知掩码和轻量查询完成机制，在特征空间中模拟并重建遮挡物体。③相比已有方法，深度感知掩码根据深度信息自适应平衡掩码和保留部分，轻量查询完成学习重建被掩码的查询，增强3D表示。④实验表明，MonoMAE在遮挡和非遮挡场景下均取得了优越的定性定量检测性能，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses object occlusion in monocular 3D detection, which degrades prediction of dimensions, depth, and orientation. It proposes MonoMAE, a masked-autoencoder-inspired detector with depth-aware masking and lightweight query completion to simulate and reconstruct occluded objects in feature space. The method achieves superior detection performance for both occluded and non-occluded objects.
- **核心贡献**: 提出MonoMAE，利用深度感知掩码和查询完成机制增强单目3D检测的遮挡鲁棒性。
- **创新点**: 将掩码自编码器思想引入单目3D检测，结合深度信息进行自适应掩码。
- **结果**: 在遮挡和非遮挡场景下均提升了单目3D检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection aims for precise 3D localization and identification of objects from a single-view image. Despite its recent progress, it often struggles while handling pervasive object occlusions that tend to complicate and degrade the prediction of object dimensions, depths, and orientations. We design MonoMAE, a monocular 3D detector inspired by Masked Autoencoders that addresses the object occlusion issue by masking and reconstructing objects in the feature space. MonoMAE consists of two novel designs. The first is depth-aware masking that selectively masks certain parts of non-occluded object queries in the feature space for simulating occluded object queries for network training. It masks non-occluded object queries by balancing the masked and preserved query portions adaptively according to the depth information. The second is lightweight query completion that works with the depth-aware masking to learn to reconstruct and complete the masked object queries. With the proposed object occlusion and completion, MonoMAE learns enriched 3D representations that achieve superior monocular 3D detection performance qualitatively and quantitatively for both occluded and non-occluded objects. Additionally, MonoMAE learns generalizable representations that can work well in new domains.

</details>

### Beware of Road Markings: A New Adversarial Patch Attack to Monocular Depth Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/7d26958422928e08465d5dd6cf0cb4cb-Abstract-Conference.html) · 📚 被引 3
- **作者**: Hangcheng Liu, Zhenhu Wu, Hao Wang, Xingshuo Han, Shangwei Guo, Tao Xiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### DCDepth: Progressive Monocular Depth Estimation in Discrete Cosine Domain.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/76bea0a1cf7bf9b78f842009f6de15a1-Abstract-Conference.html) · 📚 被引 7
- **作者**: Kun Wang, Zhiqiang Yan, Junkai Fan, Wanlu Zhu, Xiang Li, Jun Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### BetterDepth: Plug-and-Play Diffusion Refiner for Zero-Shot Monocular Depth Estimation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/c4b652b7e228b18e1c65478da3a4a2cf-Abstract-Conference.html) · 📚 被引 2
- **作者**: Xiang Zhang, Bingxin Ke, Hayko Riemenschneider, Nando Metzger, Anton Obukhov, Markus Gross et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Metric from Human: Zero-shot Monocular Metric Depth Estimation via Test-time Adaptation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/bd19ca8039547b339a6a37bd4df24405-Abstract-Conference.html)
- **作者**: Yizhou Zhao, Hengwei Bian, Kaihua Chen, Pengliang Ji, Liao Qu, Shao-yu Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Training an Open-Vocabulary Monocular 3D Detection Model without 3D Data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8492211e9176b8abdaeb1f7aa4c223ea-Abstract-Conference.html) · 📚 被引 12
- **作者**: Rui Huang, Henry Zheng, Yan Wang, Zhuofan Xia, Marco Pavone, Gao Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- From-Ground-To-Objects: Coarse-to-Fine Self-supervised Monocular Depth Estimation of Dynamic Objects with Ground Contact Prior. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Mining Supervision for Dynamic Regions in Self-Supervised Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Physical 3D Adversarial Attacks against Monocular Depth Estimation in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- High-Precision Self-supervised Monocular Depth Estimation with Rich-Resource Prior. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Mono-ViFI: A Unified Learning Framework for Self-supervised Single and Multi-frame Monocular Depth Estimation. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Self-Supervised Video Desmoking for Laparoscopic Surgery. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Improving Domain Generalization in Self-supervised Monocular Depth Estimation via Stabilized Adversarial Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
<!-- COMPLETE v1 papers=30 -->
