# Network Pruning — 2021 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Supervised Cryo-Electron Tomography Volumetric Image Restoration from Single Noisy Volume with Sparsity Constraint.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00402)
- **作者**: Zhidong Yang, Fa Zhang, Renmin Han
- **🏷️ 机构**: ICT, CAS,High Performance Computer Research Center, Shandong University,Research Center for Mathematics and Interdisciplinary Sciences
- **会议**: ICCV 2021

### Achieving on-Mobile Real-Time Super-Resolution with Neural Architecture and Pruning Search.
- **链接**: [arXiv:2108.08910](https://arxiv.org/abs/2108.08910) · 📚 被引 52
- **作者**: Zheng Zhan, Yifan Gong, Pu Zhao, Geng Yuan, Wei Niu, Yushu Wu et al.
- **🏷️ 机构**: Northeastern University, College of William &#x0026; Mary, Cleveland State University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Though recent years have witnessed remarkable progress in single image super-resolution (SISR) tasks with the prosperous development of deep neural networks (DNNs), the deep learning methods are confronted with the computation and memory consumption issues in practice, especially for resource-limited platforms such as mobile devices. To overcome the challenge and facilitate the real-time deployment of SISR tasks on mobile, we combine neural architecture search with pruning search and propose an automatic search framework that derives sparse super-resolution (SR) models with high image quality while satisfying the real-time inference requirement. To decrease the search cost, we leverage the weight sharing strategy by introducing a supernet and decouple the search problem into three stages, including supernet construction, compiler-aware architecture and pruning search, and compiler-aware pruning ratio search. With the proposed framework, we are the first to achieve real-time SR inference (with only tens of milliseconds per frame) for implementing 720p resolution with competitive image quality (in terms of PSNR and SSIM) on mobile platforms (Samsung Galaxy S20).

</details>

### ResRep: Lossless CNN Pruning via Decoupling Remembering and Forgetting.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00447) · 📚 被引 165
- **作者**: Xiaohan Ding, Tianxiang Hao, Jianchao Tan, Ji Liu, Jungong Han, Yuchen Guo et al.
- **🏷️ 机构**: Beijing National Research Center for Information Science and Technology (BNRist), Kwai Inc,Seattle AI Lab, and FeDA Lab,AI Platform Department, Aberystwyth University,Computer Science Department,SY23 3FL,UK
- **会议**: ICCV 2021

### GDP: Stabilized Neural Network Pruning via Gates with Differentiable Polarization.
- **链接**: [arXiv:2109.02220](https://arxiv.org/abs/2109.02220) · 📚 被引 34
- **作者**: Yi Guo, Huan Yuan, Jianchao Tan, Zhangyang Wang, Sen Yang, Ji Liu
- **🏷️ 机构**: Kuaishou Technology, University of Texas at Austin
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Model compression techniques are recently gaining explosive attention for obtaining efficient AI models for various real-time applications. Channel pruning is one important compression strategy and is widely used in slimming various DNNs. Previous gate-based or importance-based pruning methods aim to remove channels whose importance is smallest. However, it remains unclear what criteria the channel importance should be measured on, leading to various channel selection heuristics. Some other sampling-based pruning methods deploy sampling strategies to train sub-nets, which often causes the training instability and the compressed model's degraded performance. In view of the research gaps, we present a new module named Gates with Differentiable Polarization (GDP), inspired by principled optimization ideas. GDP can be plugged before convolutional layers without bells and whistles, to control the on-and-off of each channel or whole layer block. During the training process, the polarization effect will drive a subset of gates to smoothly decrease to exact zero, while other gates gradually stay away from zero by a large margin. When training terminates, those zero-gated channels can be painlessly removed, while other non-zero gates can be absorbed into the succeeding convolution kernel, causing completely no interruption to training nor damage to the trained model. Experiments conducted over CIFAR-10 and ImageNet datasets show that the proposed GDP algorithm achieves the state-of-the-art performance on various benchmark DNNs at a broad range of pruning ratios. We also apply GDP to DeepLabV3Plus-ResNet50 on the challenging Pascal VOC segmentation task, whose test performance sees no drop (even slightly improved) with over 60% FLOPs saving.

</details>

### Auto Graph Encoder-Decoder for Neural Network Pruning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00630) · 📚 被引 32
- **作者**: Sixing Yu, Arya Mazaheri, Ali Jannesari
- **🏷️ 机构**: Iowa State University, Technical University of Darmstadt
- **会议**: ICCV 2021

### Progressive Correspondence Pruning by Consensus Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00640) · 📚 被引 90
- **作者**: Chen Zhao, Yixiao Ge, Feng Zhu, Rui Zhao, Hongsheng Li, Mathieu Salzmann
- **🏷️ 机构**: &#x00C9;cole Polytechnique F&#x00E9;d&#x00E9;rale de Lausanne (EPFL), The Chinese University of Hong Kong, SenseTime Research
- **会议**: ICCV 2021
