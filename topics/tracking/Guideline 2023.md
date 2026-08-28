# Tracking — 2023 Guideline

> 领域: 目标跟踪（MOT / 3D 跟踪 / 多目标多相机跟踪）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MBPTrack: Improving 3D Point Cloud Tracking with Memory networks and Box Priors.
- **链接**: [arXiv:2303.05071](https://arxiv.org/abs/2303.05071) · 📚 被引 25
- **作者**: Tian-Xing Xu, Yuan-Chen Guo, Yu-Kun Lai, Song-Hai Zhang
- **🏷️ 机构**: Tsinghua University,China, Cardiff University,United Kingdom
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00934) · 📚 被引 910
- **作者**: Jinkun Cao, Jiangmiao Pang, Xinshuo Weng, Rawal Khirodkar, Kris Kitani
- **🏷️ 机构**: Carnegie Mellon University, Shanghai AI Laboratory, Nvidia
- **会议**: CVPR 2023

### MotionTrack: Learning Robust Short-Term and Long-Term Motions for Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01720) · 📚 被引 167
- **作者**: Zheng Qin, Sanping Zhou, Le Wang, Jinghai Duan, Gang Hua, Wei Tang
- **🏷️ 机构**: Institute of Artificial Intelligence and Robotics, Xi&#x0027;an Jiaotong University,National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, School of Software Engineering, Xi&#x0027;an Jiaotong University, Wormpex AI Research
- **会议**: CVPR 2023

### Exploring Lightweight Hierarchical Vision Transformers for Efficient Visual Tracking.
- **链接**: [arXiv:2308.06904](https://arxiv.org/abs/2308.06904) · 📚 被引 127
- **作者**: Ben Kang, Xin Chen, Dong Wang, Houwen Peng, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,School of Information and Communication Engineering, Microsoft Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### UTM: A Unified Multiple Object Tracking Model with Identity-Aware Feature Enhancement.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02095) · 📚 被引 87
- **作者**: Sisi You, Hantao Yao, Bing-Kun Bao, Changsheng Xu
- **🏷️ 机构**: Nanjing University of Posts and Telecommunications, Institute of Automation, Chinese Academy of Sciences (CASIA),State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2023

</details>

### Tracking without Label: Unsupervised Multiple Object Tracking via Contrastive Similarity Learning.
- **链接**: [arXiv:2309.00942](https://arxiv.org/abs/2309.00942) · 📚 被引 14
- **作者**: Sha Meng, Dian Shao, Jiacheng Guo, Shan Gao
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x2019;an,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D single object tracking has been a crucial problem for decades with numerous applications such as autonomous driving. Despite its wide-ranging use, this task remains challenging due to the significant appearance variation caused by occlusion and size differences among tracked targets. To address these issues, we present MBPTrack, which adopts a Memory mechanism to utilize past information and formulates localization in a coarse-to-fine scheme using Box Priors given in the first frame. Specifically, past frames with targetness masks serve as an external memory, and a transformer-based module propagates tracked target cues from the memory to the current frame. To precisely localize objects of all sizes, MBPTrack first predicts the target center via Hough voting. By leveraging box priors given in the first frame, we adaptively sample reference points around the target center that roughly cover the target of different sizes. Then, we obtain dense feature maps by aggregating point features into the reference points, where localization can be performed more effectively. Extensive experiments demonstrate that MBPTrack achieves state-of-the-art performance on KITTI, nuScenes and Waymo Open Dataset, while running at 50 FPS on a single RTX3090 GPU.

</details>

### Exploring Lightweight Hierarchical Vision Transformers for Efficient Visual Tracking.
- **链接**: [arXiv:2308.06904](https://arxiv.org/abs/2308.06904) · 📚 被引 127
- **作者**: Ben Kang, Xin Chen, Dong Wang, Houwen Peng, Huchuan Lu
- **🏷️ 机构**: Dalian University of Technology,School of Information and Communication Engineering, Microsoft Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based visual trackers have demonstrated significant progress owing to their superior modeling capabilities. However, existing trackers are hampered by low speed, limiting their applicability on devices with limited computational power. To alleviate this problem, we propose HiT, a new family of efficient tracking models that can run at high speed on different devices while retaining high performance. The central idea of HiT is the Bridge Module, which bridges the gap between modern lightweight transformers and the tracking framework. The Bridge Module incorporates the high-level information of deep features into the shallow large-resolution features. In this way, it produces better features for the tracking head. We also propose a novel dual-image position encoding technique that simultaneously encodes the position information of both the search region and template images. The HiT model achieves promising speed with competitive performance. For instance, it runs at 61 frames per second (fps) on the Nvidia Jetson AGX edge device. Furthermore, HiT attains 64.6% AUC on the LaSOT benchmark, surpassing all previous efficient trackers.

</details>

### Tracking without Label: Unsupervised Multiple Object Tracking via Contrastive Similarity Learning.
- **链接**: [arXiv:2309.00942](https://arxiv.org/abs/2309.00942) · 📚 被引 14
- **作者**: Sha Meng, Dian Shao, Jiacheng Guo, Shan Gao
- **🏷️ 机构**: Northwestern Polytechnical University,Xi&#x2019;an,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised learning is a challenging task due to the lack of labels. Multiple Object Tracking (MOT), which inevitably suffers from mutual object interference, occlusion, etc., is even more difficult without label supervision. In this paper, we explore the latent consistency of sample features across video frames and propose an Unsupervised Contrastive Similarity Learning method, named UCSL, including three contrast modules: self-contrast, cross-contrast, and ambiguity contrast. Specifically, i) self-contrast uses intra-frame direct and inter-frame indirect contrast to obtain discriminative representations by maximizing self-similarity. ii) Cross-contrast aligns cross- and continuous-frame matching results, mitigating the persistent negative effect caused by object occlusion. And iii) ambiguity contrast matches ambiguous objects with each other to further increase the certainty of subsequent object association through an implicit manner. On existing benchmarks, our method outperforms the existing unsupervised methods using only limited help from ReID head, and even provides higher accuracy than lots of fully supervised methods.

</details>
