# Multi-camera Perception — 2021 Guideline

> 领域: 多相机 / 多视角感知（环视、深度估计与 3D 预测）
> 论文数: 6 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Direct Multi-view Multi-person 3D Pose Estimation.
- **链接**: [arXiv:2111.04076](https://arxiv.org/abs/2111.04076) · [代码](https://github.com/sail-sg/mvp)
- **作者**: Tao Wang, Jianfeng Zhang, Yujun Cai, Shuicheng Yan, Jiashi Feng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Multi-view Pose transformer (MvP) for estimating multi-person 3D poses from multi-view images. Instead of estimating 3D joint locations from costly volumetric representation or reconstructing the per-person 3D pose from multiple detected 2D poses as in previous methods, MvP directly regresses the multi-person 3D poses in a clean and efficient way, without relying on intermediate tasks. Specifically, MvP represents skeleton joints as learnable query embeddings and let them progressively attend to and reason over the multi-view information from the input images to directly regress the actual 3D joint locations. To improve the accuracy of such a simple pipeline, MvP presents a hierarchical scheme to concisely represent query embeddings of multi-person skeleton joints and introduces an input-dependent query adaptation approach. Further, MvP designs a novel geometrically guided attention mechanism, called projective attention, to more precisely fuse the cross-view information for each joint. MvP also introduces a RayConv operation to integrate the view-dependent camera geometry into the feature representations for augmenting the projective attention. We show experimentally that our MvP model outperforms the state-of-the-art methods on several benchmarks while being much more efficient. Notably, it achieves 92.3% AP25 on the challenging Panoptic dataset, improving upon the previous best approach [36] by 9.8%. MvP is general and also extendable to recovering human mesh represented by the SMPL model, thus useful for modeling multi-person body shapes. Code and models are available at https://github.com/sail-sg/mvp.

</details>

### Multi-View Representation Learning via Total Correlation Objective.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/65a99bb7a3115fdede20da98b08a370f-Abstract.html)
- **作者**: HyeongJoo Hwang, Geon-Hyeong Kim, Seunghoon Hong, Kee-Eung Kim
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Multi-view Contrastive Graph Clustering.
- **链接**: [出版页](https://proceedings.neurips.cc/paper/2021/hash/10c66082c124f8afe3df4886f5e516e0-Abstract.html)
- **作者**: Erlin Pan, Zhao Kang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

### Residual Relaxation for Multi-view Representation Learning.
- **链接**: [arXiv:2110.15348](https://arxiv.org/abs/2110.15348)
- **作者**: Yifei Wang, Zhengyang Geng, Feng Jiang, Chuming Li, Yisen Wang, Jiansheng Yang et al.
- **🏷️ 机构**: Peking University
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-view methods learn representations by aligning multiple views of the same image and their performance largely depends on the choice of data augmentation. In this paper, we notice that some other useful augmentations, such as image rotation, are harmful for multi-view methods because they cause a semantic shift that is too large to be aligned well. This observation motivates us to relax the exact alignment objective to better cultivate stronger augmentations. Taking image rotation as a case study, we develop a generic approach, Pretext-aware Residual Relaxation (Prelax), that relaxes the exact alignment by allowing an adaptive residual vector between different views and encoding the semantic shift through pretext-aware learning. Extensive experiments on different backbones show that our method can not only improve multi-view methods with existing augmentations, but also benefit from stronger image augmentations like rotation.

</details>

### NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction.
- **链接**: [arXiv:2106.10689](https://arxiv.org/abs/2106.10689)
- **作者**: Peng Wang, Lingjie Liu, Yuan Liu, Christian Theobalt, Taku Komura, Wenping Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel neural surface reconstruction method, called NeuS, for reconstructing objects and scenes with high fidelity from 2D image inputs. Existing neural surface reconstruction approaches, such as DVR and IDR, require foreground mask as supervision, easily get trapped in local minima, and therefore struggle with the reconstruction of objects with severe self-occlusion or thin structures. Meanwhile, recent neural methods for novel view synthesis, such as NeRF and its variants, use volume rendering to produce a neural scene representation with robustness of optimization, even for highly complex objects. However, extracting high-quality surfaces from this learned implicit representation is difficult because there are not sufficient surface constraints in the representation. In NeuS, we propose to represent a surface as the zero-level set of a signed distance function (SDF) and develop a new volume rendering method to train a neural SDF representation. We observe that the conventional volume rendering method causes inherent geometric errors (i.e. bias) for surface reconstruction, and therefore propose a new formulation that is free of bias in the first order of approximation, thus leading to more accurate surface reconstruction even without the mask supervision. Experiments on the DTU dataset and the BlendedMVS dataset show that NeuS outperforms the state-of-the-arts in high-quality surface reconstruction, especially for objects and scenes with complex structures and self-occlusion.

</details>

### Real-Time and Accurate Self-Supervised Monocular Depth Estimation on Mobile Device.
- **链接**: [出版页](https://proceedings.mlr.press/v176/cai22a.html)
- **作者**: Hong Cai, Fei Yin, Tushar Singhal, Sandeep Pendyam, Parham Noorzad, Yinhao Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2021
