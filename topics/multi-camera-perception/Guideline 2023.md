# Multi-camera Perception — 2023 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### A High-Resolution Dataset for Instance Detection with Multi-View Object Capture.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/832ea0ff01bd512aab28bf416db9489c-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 0
- **作者**: Qianqian Shen, Yunhan Zhao, Nahyun Kwon, Jeeeun Kim, Yanan Li, Shu Kong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Masked Two-channel Decoupling Framework for Incomplete Multi-view Weak Multi-label Learning.
- **链接**: [arXiv:2404.17340](https://arxiv.org/abs/2404.17340) · 📚 被引 6
- **作者**: Chengliang Liu, Jie Wen, Yabo Liu, Chao Huang, Zhihao Wu, Xiaoling Luo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view learning has become a popular research topic in recent years, but research on the cross-application of classic multi-label classification and multi-view learning is still in its early stages. In this paper, we focus on the complex yet highly realistic task of incomplete multi-view weak multi-label learning and propose a masked two-channel decoupling framework based on deep neural networks to solve this problem. The core innovation of our method lies in decoupling the single-channel view-level representation, which is common in deep multi-view learning methods, into a shared representation and a view-proprietary representation. We also design a cross-channel contrastive loss to enhance the semantic property of the two channels. Additionally, we exploit supervised information to design a label-guided graph regularization loss, helping the extracted embedding features preserve the geometric structure among samples. Inspired by the success of masking mechanisms in image and text analysis, we develop a random fragment masking strategy for vector features to improve the learning ability of encoders. Finally, it is important to emphasize that our model is fully adaptable to arbitrary view and label absences while also performing well on the ideal full data. We have conducted sufficient and convincing experiments to confirm the effectiveness and advancement of our model.

</details>

### A Novel Approach for Effective Multi-View Clustering with Information-Theoretic Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/8c64bc3f7796d31caa7c3e6b969bf7da-Abstract-Conference.html)
- **作者**: Chenhang Cui, Yazhou Ren, Jingyu Pu, Jiawei Li, Xiaorong Pu, Tianyi Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### MVDoppler: Unleashing the Power of Multi-View Doppler for MicroMotion-based Gait Classification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b5727c1bab903e0ff21cec84a9a7f5a6-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 1
- **作者**: Soheil Hor, Shubo Yang, Jaeho Choi, Amin Arbabian
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Generalized Information-theoretic Multi-view Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b7aa34d2d24f9bab3056993b7bfa0f1b-Abstract-Conference.html) · 📚 被引 2
- **作者**: Weitian Huang, Sirui Yang, Hongmin Cai
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Orthogonal Non-negative Tensor Factorization based Multi-view Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3a5b75ce6cbd3aaaa32d6e935ffc4cff-Abstract-Conference.html) · 📚 被引 12
- **作者**: Jing Li, Quanxue Gao, Qianqian Wang, Ming Yang, Wei Xia
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Factorized Contrastive Learning: Going Beyond Multi-view Redundancy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6818dcc65fdf3cbd4b05770fb957803e-Abstract-Conference.html) · 📚 被引 13
- **作者**: Paul Pu Liang, Zihao Deng, Martin Q. Ma, James Y. Zou, Louis-Philippe Morency, Ruslan Salakhutdinov
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### RayDF: Neural Ray-surface Distance Fields with Multi-view Consistency.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/4f86833d5cc98ec32e470ef1c8cb82e3-Abstract-Conference.html) · 📚 被引 1
- **作者**: Zhuoman Liu, Bo Yang, Yan Luximon, Ajay Kumar, Jinxi Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### GenS: Generalizable Neural Surface Reconstruction from Multi-View Images.
- **链接**: [arXiv:2406.02495](https://arxiv.org/abs/2406.02495) · [代码](https://github.com/prstrive/GenS) · 📚 被引 2
- **作者**: Rui Peng, Xiaodong Gu, Luyang Tang, Shihe Shen, Fanqi Yu, Ronggang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Combining the signed distance function (SDF) and differentiable volume rendering has emerged as a powerful paradigm for surface reconstruction from multi-view images without 3D supervision. However, current methods are impeded by requiring long-time per-scene optimizations and cannot generalize to new scenes. In this paper, we present GenS, an end-to-end generalizable neural surface reconstruction model. Unlike coordinate-based methods that train a separate network for each scene, we construct a generalized multi-scale volume to directly encode all scenes. Compared with existing solutions, our representation is more powerful, which can recover high-frequency details while maintaining global smoothness. Meanwhile, we introduce a multi-scale feature-metric consistency to impose the multi-view consistency in a more discriminative multi-scale feature space, which is robust to the failures of the photometric consistency. And the learnable feature can be self-enhanced to continuously improve the matching accuracy and mitigate aggregation ambiguity. Furthermore, we design a view contrast loss to force the model to be robust to those regions covered by few viewpoints through distilling the geometric prior from dense input to sparse input. Extensive experiments on popular benchmarks show that our model can generalize well to new scenes and outperform existing state-of-the-art methods even those employing ground-truth depth supervision. Code is available at https://github.com/prstrive/GenS.

</details>

### MVDiffusion: Enabling Holistic Multi-view Image Generation with Correspondence-Aware Diffusion.
- **链接**: [arXiv:2307.01097](https://arxiv.org/abs/2307.01097)
- **作者**: Shitao Tang, Fuyang Zhang, Jiacheng Chen, Peng Wang, Yasutaka Furukawa
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces MVDiffusion, a simple yet effective method for generating consistent multi-view images from text prompts given pixel-to-pixel correspondences (e.g., perspective crops from a panorama or multi-view images given depth maps and poses). Unlike prior methods that rely on iterative image warping and inpainting, MVDiffusion simultaneously generates all images with a global awareness, effectively addressing the prevalent error accumulation issue. At its core, MVDiffusion processes perspective images in parallel with a pre-trained text-to-image diffusion model, while integrating novel correspondence-aware attention layers to facilitate cross-view interactions. For panorama generation, while only trained with 10k panoramas, MVDiffusion is able to generate high-resolution photorealistic images for arbitrary texts or extrapolate one perspective image to a 360-degree view. For multi-view depth-to-image generation, MVDiffusion demonstrates state-of-the-art performance for texturing a scene mesh.

</details>

### The Surprising Effectiveness of Diffusion Models for Optical Flow and Monocular Depth Estimation.
- **链接**: [arXiv:2306.01923](https://arxiv.org/abs/2306.01923) · 📚 被引 9
- **作者**: Saurabh Saxena, Charles Herrmann, Junhwa Hur, Abhishek Kar, Mohammad Norouzi, Deqing Sun et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Denoising diffusion probabilistic models have transformed image generation with their impressive fidelity and diversity. We show that they also excel in estimating optical flow and monocular depth, surprisingly, without task-specific architectures and loss functions that are predominant for these tasks. Compared to the point estimates of conventional regression-based methods, diffusion models also enable Monte Carlo inference, e.g., capturing uncertainty and ambiguity in flow and depth. With self-supervised pre-training, the combined use of synthetic and real data for supervised training, and technical innovations (infilling and step-unrolled denoising diffusion training) to handle noisy-incomplete training data, and a simple form of coarse-to-fine refinement, one can train state-of-the-art diffusion models for depth and optical flow estimation. Extensive experiments focus on quantitative performance against benchmarks, ablations, and the model's ability to capture uncertainty and multimodality, and impute missing values. Our model, DDVM (Denoising Diffusion Vision Model), obtains a state-of-the-art relative depth error of 0.074 on the indoor NYU benchmark and an Fl-all outlier rate of 3.26\% on the KITTI optical flow benchmark, about 25\% better than the best published method. For an overview see https://diffusion-vision.github.io.

</details>

### IEBins: Iterative Elastic Bins for Monocular Depth Estimation.
- **链接**: [arXiv:2309.14137](https://arxiv.org/abs/2309.14137) · [代码](https://github.com/ShuweiShao/IEBins) · 📚 被引 13
- **作者**: Shuwei Shao, Zhongcai Pei, Xingming Wu, Zhong Liu, Weihai Chen, Zhengguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular depth estimation (MDE) is a fundamental topic of geometric computer vision and a core technique for many downstream applications. Recently, several methods reframe the MDE as a classification-regression problem where a linear combination of probabilistic distribution and bin centers is used to predict depth. In this paper, we propose a novel concept of iterative elastic bins (IEBins) for the classification-regression-based MDE. The proposed IEBins aims to search for high-quality depth by progressively optimizing the search range, which involves multiple stages and each stage performs a finer-grained depth search in the target bin on top of its previous stage. To alleviate the possible error accumulation during the iterative process, we utilize a novel elastic target bin to replace the original target bin, the width of which is adjusted elastically based on the depth uncertainty. Furthermore, we develop a dedicated framework composed of a feature extractor and an iterative optimizer that has powerful temporal context modeling capabilities benefiting from the GRU-based architecture. Extensive experiments on the KITTI, NYU-Depth-v2 and SUN RGB-D datasets demonstrate that the proposed method surpasses prior state-of-the-art competitors. The source code is publicly available at https://github.com/ShuweiShao/IEBins.

</details>

## 跨领域论文（完整笔记在其他领域）

- Leveraging Vision-Centric Multi-Modal Expertise for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- HotBEV: Hardware-oriented Transformer-based Multi-View 3D Detector for BEV Perception. → [bev](../bev/Guideline%202023.md)
