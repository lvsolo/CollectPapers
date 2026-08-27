# Neural Architecture Search — 2022 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 2 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### EAutoDet: Efficient Architecture Search for Object Detection.
- **链接**: [arXiv:2203.10747](https://arxiv.org/abs/2203.10747) · 📚 被引 24
- **作者**: Xiaoxing Wang, Jiale Lin, Juanping Zhao, Xiaokang Yang, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022

- **摘要（英，原文）**:

  > Training CNN for detection is time-consuming due to the large dataset and complex network modules, making it hard to search architectures on detection datasets directly, which usually requires vast search costs (usually tens and even hundreds of GPU-days). In contrast, this paper introduces an efficient framework, named EAutoDet, that can discover practical backbone and FPN architectures for object detection in 1.4 GPU-days. Specifically, we construct a supernet for both backbone and FPN modules and adopt the differentiable method. To reduce the GPU memory requirement and computational cost, we propose a kernel reusing technique by sharing the weights of candidate operations on one edge and consolidating them into one convolution. A dynamic channel refinement strategy is also introduced to search channel numbers. Extensive experiments show significant efficacy and efficiency of our method. In particular, the discovered architectures surpass state-of-the-art object detection NAS methods and achieve 40.1 mAP with 120 FPS and 49.2 mAP with 41.3 FPS on COCO test-dev set. We also transfer the discovered architectures to rotation detection task, which achieve 77.05 mAP$_{\text{50}}$ on DOTA-v1.0 test set with 21.1M parameters.

### ViTAS: Vision Transformer Architecture Search.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19803-8_9)
- **作者**: Xiu Su, Shan You, Jiyang Xie, Mingkai Zheng, Fei Wang, Chen Qian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
