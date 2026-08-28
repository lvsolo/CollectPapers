# 3D Detection — 2025 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OpenAD: Open-World Autonomous Driving Benchmark for 3D Object Detection.
- **链接**: [arXiv:2411.17761](https://arxiv.org/abs/2411.17761) · [代码](https://github.com/VDIGPKU/OpenAD)
- **作者**: Zhongyu Xia, Jishuo Li, Zhiwei Lin, Xinhao Wang, Yongtao Wang, Ming-Hsuan Yang
- **🏷️ 机构**: UC Merced
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-world perception aims to develop a model adaptable to novel domains and various sensor configurations and can understand uncommon objects and corner cases. However, current research lacks sufficiently comprehensive open-world 3D perception benchmarks and robust generalizable methodologies. This paper introduces OpenAD, the first real open-world autonomous driving benchmark for 3D object detection. OpenAD is built upon a corner case discovery and annotation pipeline that integrates with a multimodal large language model (MLLM). The proposed pipeline annotates corner case objects in a unified format for five autonomous driving perception datasets with 2000 scenarios. In addition, we devise evaluation methodologies and evaluate various open-world and specialized 2D and 3D models. Moreover, we propose a vision-centric 3D open-world object detection baseline and further introduce an ensemble method by fusing general and specialized models to address the issue of lower precision in existing open-world methods for the OpenAD benchmark. We host an online challenge on EvalAI. Data, toolkit codes, and evaluation codes are available at https://github.com/VDIGPKU/OpenAD.

</details>

### Rooms from Motion: Un-posed Indoor 3D Object Detection as Localization and Mapping.
- **链接**: [arXiv:2505.23756](https://arxiv.org/abs/2505.23756) · 📚 被引 0
- **作者**: Justin Lazarow, Kai Kang, Afshin Dehghan
- **🏷️ 机构**: Apple, Apple Inc.
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We revisit scene-level 3D object detection as the output of an object-centric framework capable of both localization and mapping using 3D oriented boxes as the underlying geometric primitive. While existing 3D object detection approaches operate globally and implicitly rely on the a priori existence of metric camera poses, our method, Rooms from Motion (RfM) operates on a collection of un-posed images. By replacing the standard 2D keypoint-based matcher of structure-from-motion with an object-centric matcher based on image-derived 3D boxes, we estimate metric camera poses, object tracks, and finally produce a global, semantic 3D object map. When a priori pose is available, we can significantly improve map quality through optimization of global 3D boxes against individual observations. RfM shows strong localization performance and subsequently produces maps of higher quality than leading point-based and multi-view 3D object detection methods on CA-1M and ScanNet++, despite these global methods relying on overparameterization through point clouds or dense volumes. Rooms from Motion achieves a general, object-centric representation which not only extends the work of Cubify Anything to full scenes but also allows for inherently sparse localization and parametric mapping proportional to the number of objects in a scene.

</details>

### Point4Bit: Post Training 4-bit Quantization for Point Cloud 3D Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f1922bd718528ac3eab114eabbbfa7a0-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jianyu Wang, Yu Wang, Shengjie Zhao, Sifan Zhou
- **🏷️ 机构**: Tongji University, Tsinghua University, Southeast University &amp; Carnegie Mellon University
- **会议**: NeurIPS 2025

### TrackingWorld: World-centric Monocular 3D Tracking of Almost All Pixels.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/cede701f00079e43d053ac57b1e75c3e-Abstract-Conference.html)
- **作者**: Jiahao Lu, Weitao Xiong, Jiacheng Deng, Peng Li, Tianyu Huang, Zhiyang Dou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025
