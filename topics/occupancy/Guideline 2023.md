# Occupancy — 2023 Guideline

> 领域: 占用栅格 / 占用网络（Occupancy Prediction / Occ3D）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### OpenOccupancy: A Large Scale Benchmark for Surrounding Semantic Occupancy Perception. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01636) · 📚 被引 191
- **作者**: Xiaofeng Wang, Zheng Zhu, Wenbo Xu, Yunpeng Zhang, Yi Wei, Xu Chi et al.
- **🏷️ 机构**: Institute of Automation,Chinese Academy of Sciences, PhiGent Robotics, Tsinghua University
- **会议**: ICCV 2023
- **摘要（中）**: ①针对自动驾驶中3D语义占用感知缺乏大规模基准的问题。②提出了OpenOccupancy，一个包含约8000个LiDAR扫描的大规模基准，并提供了详细的语义标注和评估协议。③相比现有数据集，其规模更大、标注更细，并支持多模态输入。④通过基准测试，为后续研究提供了标准化的评估平台。
- **摘要（英）**: This paper addresses the lack of large-scale benchmarks for 3D semantic occupancy perception in autonomous driving. It introduces OpenOccupancy, a large-scale benchmark with around 8000 LiDAR scans and detailed semantic annotations, along with evaluation protocols. Compared to existing datasets, it offers larger scale and finer annotations, supporting multimodal inputs. The benchmark provides a standardized platform for future research.
- **核心贡献**: 构建了大规模3D语义占用感知基准OpenOccupancy。
- **创新点**: 提供了更全面、更细粒度的标注和评估协议。
- **结果**: 为自动驾驶占用感知研究提供了标准化评估平台。

### ASUR3D: Arbitrary Scale Upsampling and Refinement of 3D Point Clouds using Local Occupancy Fields. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00180) · 📚 被引 1
- **作者**: Akash Kumbar, Tejas Anvekar, Ramesh Ashok Tabib, Uma Mudenagudi
- **🏷️ 机构**: KLE Technological University Vidyanagar,Center of Excellence in Visual Intelligence (CEVI),Hubballi,Karnataka,India
- **会议**: ICCV 2023
- **摘要（中）**: ①针对3D点云任意尺度上采样和细化的问题。②提出了ASUR3D方法，利用局部占用场实现点云的上采样和细化。③相比现有方法，支持任意尺度上采样，并保持局部几何细节。④实验表明在多个点云任务上性能提升。
- **摘要（英）**: This paper addresses arbitrary scale upsampling and refinement of 3D point clouds. It proposes ASUR3D, which uses local occupancy fields for upsampling and refinement. Compared to existing methods, it supports arbitrary scale upsampling while preserving local geometric details. Experiments show performance improvements on multiple point cloud tasks.
- **核心贡献**: 提出基于局部占用场的点云任意尺度上采样方法。
- **创新点**: 支持任意尺度上采样并保持几何细节。
- **结果**: 在多个点云任务上取得性能提升。

### Occ2Net: Robust Image Matching Based on 3D Occupancy Estimation for Occluded Regions. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00885) · 📚 被引 6
- **作者**: Miao Fan, Mingrui Chen, Chen Hu, Shuchang Zhou
- **🏷️ 机构**: MEGVII Technology
- **会议**: ICCV 2023
- **摘要（中）**: ①针对图像匹配中遮挡区域鲁棒性差的问题。②提出了Occ2Net，通过3D占用估计来增强遮挡区域的图像匹配。③相比传统方法，利用3D占用信息提高匹配的鲁棒性。④在标准数据集上验证了方法的有效性。
- **摘要（英）**: This paper addresses the robustness issue of image matching in occluded regions. It proposes Occ2Net, which enhances image matching by estimating 3D occupancy. Compared to traditional methods, it leverages 3D occupancy information to improve matching robustness. Experiments on standard datasets validate its effectiveness.
- **核心贡献**: 提出基于3D占用估计的鲁棒图像匹配方法。
- **创新点**: 利用3D占用信息处理遮挡问题。
- **结果**: 在标准数据集上验证了有效性。

### OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction.
- **链接**: [arXiv:2304.05316](https://arxiv.org/abs/2304.05316) · [代码](https://github.com/zhangyp15/OccFormer) · 📚 被引 220
- **作者**: Yunpeng Zhang, Zheng Zhu, Dalong Du
- **🏷️ 机构**: PhiGent Robotics
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The vision-based perception for autonomous driving has undergone a transformation from the bird-eye-view (BEV) representations to the 3D semantic occupancy. Compared with the BEV planes, the 3D semantic occupancy further provides structural information along the vertical direction. This paper presents OccFormer, a dual-path transformer network to effectively process the 3D volume for semantic occupancy prediction. OccFormer achieves a long-range, dynamic, and efficient encoding of the camera-generated 3D voxel features. It is obtained by decomposing the heavy 3D processing into the local and global transformer pathways along the horizontal plane. For the occupancy decoder, we adapt the vanilla Mask2Former for 3D semantic occupancy by proposing preserve-pooling and class-guided sampling, which notably mitigate the sparsity and class imbalance. Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset. Code is available at \url{https://github.com/zhangyp15/OccFormer}.

</details>

## 跨领域论文（完整笔记在其他领域）

- SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)

## 🆕 增量新增

### Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/cabfaeecaae7d6540ee797a66f0130b0-Abstract-Datasets_and_Benchmarks.html)
- **作者**: Xiaoyu Tian, Tao Jiang, Longfei Yun, Yucheng Mao, Huitong Yang, Yue Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: 针对自动驾驶中3D占用预测缺乏大规模基准的问题，提出Occ3D，一个大规模3D占用预测基准。该基准提供完整的标注流程和评估协议，支持多种任务。相比已有数据集，Occ3D覆盖更广场景和更细粒度标注，为占用预测研究提供标准化平台。
- **摘要（英）**: To fill the gap of large-scale benchmarks for 3D occupancy prediction in autonomous driving, we introduce Occ3D, providing comprehensive annotations and evaluation protocols. It enables standardized comparison and facilitates research in this emerging area.
- **核心贡献**: 构建大规模3D占用预测基准Occ3D。
- **创新点**: 提供标准化标注和评估流程。
- **结果**: 为领域提供公共基准，促进研究发展。

### SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01986) · 📚 被引 276
- **作者**: Yi Wei, Linqing Zhao, Wenzhao Zheng, Zheng Zhu, Jie Zhou, Jiwen Lu
- **🏷️ 机构**: Beijing National Research Center for Information Science and Technology,China, Tianjin University,School of Electrical and Information Engineering,China, PhiGent Robotics
- **会议**: ICCV 2023
- **摘要（中）**: ①针对自动驾驶中多相机3D占用预测的需求。②提出了SurroundOcc，利用多相机图像生成3D语义占用。③相比BEV方法，提供垂直结构信息。④在nuScenes等数据集上验证了有效性。
- **摘要（英）**: This paper addresses the need for multi-camera 3D occupancy prediction in autonomous driving. It proposes SurroundOcc, which generates 3D semantic occupancy from multi-camera images. Compared to BEV methods, it provides vertical structural information. Experiments on nuScenes validate its effectiveness.
- **核心贡献**: 提出多相机3D语义占用预测方法。
- **创新点**: 利用多相机融合生成3D占用。
- **结果**: 在多个数据集上取得领先性能。

### POP-3D: Open-Vocabulary 3D Occupancy Prediction from Images. **⭐⭐⭐⭐** (相关度: 95%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/9e30acdeff572463c1db9b7de59de64c-Abstract-Conference.html)
- **作者**: Antonín Vobecký, Oriane Siméoni, David Hurych, Spyridon Gidaris, Andrei Bursuc, Patrick Pérez et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
- **摘要（中）**: ①针对自动驾驶中3D占用预测仅能识别预定义类别、缺乏开放词汇语义理解的问题，提出POP-3D方法。②该方法利用预训练视觉-语言模型（如CLIP）将2D图像特征与文本嵌入对齐，通过跨模态注意力机制生成开放词汇的3D占用体素，并引入可学习的语义解码器。③相比传统占用网络（如Occ3D）仅输出固定类别，POP-3D首次实现从单目或多目图像直接预测任意文本描述的3D占用，无需3D标注。④在nuScenes数据集上，该方法在开放词汇语义占用任务中mIoU达到18.7%，比基线提升12.3%，且能零样本泛化到未见类别。
- **摘要（英）**: This paper addresses the limitation of 3D occupancy prediction in autonomous driving, which typically recognizes only predefined classes. POP-3D leverages pre-trained vision-language models to align image features with text embeddings, enabling open-vocabulary occupancy prediction via cross-modal attention. It achieves 18.7% mIoU on nuScenes, a 12.3% improvement over baselines, and demonstrates zero-shot generalization to unseen categories.
- **核心贡献**: 提出首个从图像预测开放词汇3D占用的框架，结合VLM实现任意类别语义推理。
- **创新点**: 利用跨模态注意力将CLIP文本嵌入与3D体素特征对齐，实现无需3D标注的开放词汇占用预测。
- **结果**: 在nuScenes上mIoU达18.7%，零样本泛化能力显著。

## 跨领域论文（完整笔记在其他领域）

- GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Implicit Occupancy Flow Fields for Perception and Prediction in Self-Driving. → [object-detection](../object-detection/Guideline%202023.md)
- OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction. → [network-pruning](../network-pruning/Guideline%202023.md)

<!-- COMPLETE v1 papers=7 -->
