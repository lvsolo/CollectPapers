# 3D Detection — 2022 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Sparse2Dense: Learning to Densify 3D Features for 3D Object Detection.
- **链接**: [arXiv:2211.13067](https://arxiv.org/abs/2211.13067)
- **作者**: Tianyu Wang, Xiaowei Hu, Zhengzhe Liu, Chi-Wing Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-produced point clouds are the major source for most state-of-the-art 3D object detectors. Yet, small, distant, and incomplete objects with sparse or few points are often hard to detect. We present Sparse2Dense, a new framework to efficiently boost 3D detection performance by learning to densify point clouds in latent space. Specifically, we first train a dense point 3D detector (DDet) with a dense point cloud as input and design a sparse point 3D detector (SDet) with a regular point cloud as input. Importantly, we formulate the lightweight plug-in S2D module and the point cloud reconstruction module in SDet to densify 3D features and train SDet to produce 3D features, following the dense 3D features in DDet. So, in inference, SDet can simulate dense 3D features from regular (sparse) point cloud inputs without requiring dense inputs. We evaluate our method on the large-scale Waymo Open Dataset and the Waymo Domain Adaptation Dataset, showing its high performance and efficiency over the state of the arts.

</details>

### MsSVT: Mixed-scale Sparse Voxel Transformer for 3D Object Detection on Point Clouds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4bad7c27534efca029ca0d366c47c0e3-Abstract-Conference.html) · 📚 被引 1
- **作者**: Shaocong Dong, Lihe Ding, Haiyang Wang, Tingfa Xu, Xinli Xu, Jie Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Fully Sparse 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/0247fa3c511bbc415c8b768ee7b32f9e-Abstract-Conference.html)
- **作者**: Lue Fan, Feng Wang, Naiyan Wang, Zhaoxiang Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Unifying Voxel-based Representation with Transformer for 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/752df938681b2cf15e5fc9689f0bcf3a-Abstract-Conference.html) · 📚 被引 34
- **作者**: Yanwei Li, Yilun Chen, Xiaojuan Qi, Zeming Li, Jian Sun, Jiaya Jia
- **🏷️ 机构**: MEGVII, CUHK / SmartMore
- **会议**: NeurIPS 2022

### Spatial Pruned Sparse Convolution for Efficient 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/2ce10f144bb93449767f355c01f24cc1-Abstract-Conference.html)
- **作者**: Jianhui Liu, Yukang Chen, Xiaoqing Ye, Zhuotao Tian, Xiao Tan, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Fully Convolutional One-Stage 3D Object Detection on LiDAR Range Images.
- **链接**: [arXiv:2205.13764](https://arxiv.org/abs/2205.13764) · 📚 被引 16
- **作者**: Zhi Tian, Xiangxiang Chu, Xiaoming Wang, Xiaolin Wei, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a simple yet effective fully convolutional one-stage 3D object detector for LiDAR point clouds of autonomous driving scenes, termed FCOS-LiDAR. Unlike the dominant methods that use the bird-eye view (BEV), our proposed detector detects objects from the range view (RV, a.k.a. range image) of the LiDAR points. Due to the range view's compactness and compatibility with the LiDAR sensors' sampling process on self-driving cars, the range view-based object detector can be realized by solely exploiting the vanilla 2D convolutions, departing from the BEV-based methods which often involve complicated voxelization operations and sparse convolutions. For the first time, we show that an RV-based 3D detector with standard 2D convolutions alone can achieve comparable performance to state-of-the-art BEV-based detectors while being significantly faster and simpler. More importantly, almost all previous range view-based detectors only focus on single-frame point clouds, since it is challenging to fuse multi-frame point clouds into a single range view. In this work, we tackle this challenging issue with a novel range view projection mechanism, and for the first time demonstrate the benefits of fusing multi-frame point clouds for a range-view based detector. Extensive experiments on nuScenes show the superiority of our proposed method and we believe that our work can be strong evidence that an RV-based 3D detector can compare favourably with the current mainstream BEV-based detectors.

</details>

### CAGroup3D: Class-Aware Grouping for 3D Object Detection on Point Clouds.
- **链接**: [arXiv:2210.04264](https://arxiv.org/abs/2210.04264) · [代码](https://github.com/Haiyang-W/CAGroup3D)
- **作者**: Haiyang Wang, Lihe Ding, Shaocong Dong, Shaoshuai Shi, Aoxue Li, Jianan Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present a novel two-stage fully sparse convolutional 3D object detection framework, named CAGroup3D. Our proposed method first generates some high-quality 3D proposals by leveraging the class-aware local group strategy on the object surface voxels with the same semantic predictions, which considers semantic consistency and diverse locality abandoned in previous bottom-up approaches. Then, to recover the features of missed voxels due to incorrect voxel-wise segmentation, we build a fully sparse convolutional RoI pooling module to directly aggregate fine-grained spatial information from backbone for further proposal refinement. It is memory-and-computation efficient and can better encode the geometry-specific features of each 3D proposal. Our model achieves state-of-the-art 3D detection performance with remarkable gains of +\textit{3.6\%} on ScanNet V2 and +\textit{2.6}\% on SUN RGB-D in term of mAP@0.25. Code will be available at https://github.com/Haiyang-W/CAGroup3D.

</details>

### DeepInteraction: 3D Object Detection via Modality Interaction.
- **链接**: [arXiv:2208.11112](https://arxiv.org/abs/2208.11112) · 📚 被引 31
- **作者**: Zeyu Yang, Jiaqi Chen, Zhenwei Miao, Wei Li, Xiatian Zhu, Li Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing top-performance 3D object detectors typically rely on the multi-modal fusion strategy. This design is however fundamentally restricted due to overlooking the modality-specific useful information and finally hampering the model performance. To address this limitation, in this work we introduce a novel modality interaction strategy where individual per-modality representations are learned and maintained throughout for enabling their unique characteristics to be exploited during object detection. To realize this proposed strategy, we design a DeepInteraction architecture characterized by a multi-modal representational interaction encoder and a multi-modal predictive interaction decoder. Experiments on the large-scale nuScenes dataset show that our proposed method surpasses all prior arts often by a large margin. Crucially, our method is ranked at the first position at the highly competitive nuScenes object detection leaderboard.

</details>

### Towards Efficient 3D Object Detection with Knowledge Distillation.
- **链接**: [arXiv:2205.15156](https://arxiv.org/abs/2205.15156) · [代码](https://github.com/CVMI-Lab/SparseKD) · 📚 被引 10
- **作者**: Jihan Yang, Shaoshuai Shi, Runyu Ding, Zhe Wang, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite substantial progress in 3D object detection, advanced 3D detectors often suffer from heavy computation overheads. To this end, we explore the potential of knowledge distillation (KD) for developing efficient 3D object detectors, focusing on popular pillar- and voxel-based detectors.In the absence of well-developed teacher-student pairs, we first study how to obtain student models with good trade offs between accuracy and efficiency from the perspectives of model compression and input resolution reduction. Then, we build a benchmark to assess existing KD methods developed in the 2D domain for 3D object detection upon six well-constructed teacher-student pairs. Further, we propose an improved KD pipeline incorporating an enhanced logit KD method that performs KD on only a few pivotal positions determined by teacher classification response, and a teacher-guided student model initialization to facilitate transferring teacher model's feature extraction ability to students through weight inheritance. Finally, we conduct extensive experiments on the Waymo dataset. Our best performing model achieves $65.75\%$ LEVEL 2 mAPH, surpassing its teacher model and requiring only $44\%$ of teacher flops. Our most efficient model runs 51 FPS on an NVIDIA A100, which is $2.2\times$ faster than PointPillar with even higher accuracy. Code is available at \url{https://github.com/CVMI-Lab/SparseKD}.

</details>

### MoGDE: Boosting Mobile Monocular 3D Object Detection with Ground Depth Estimation.
- **链接**: [arXiv:2303.13561](https://arxiv.org/abs/2303.13561) · 📚 被引 3
- **作者**: Yunsong Zhou, Quan Liu, Hongzi Zhu, Yunzhe Li, Shan Chang, Minyi Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection (Mono3D) in mobile settings (e.g., on a vehicle, a drone, or a robot) is an important yet challenging task. Due to the near-far disparity phenomenon of monocular vision and the ever-changing camera pose, it is hard to acquire high detection accuracy, especially for far objects. Inspired by the insight that the depth of an object can be well determined according to the depth of the ground where it stands, in this paper, we propose a novel Mono3D framework, called MoGDE, which constantly estimates the corresponding ground depth of an image and then utilizes the estimated ground depth information to guide Mono3D. To this end, we utilize a pose detection network to estimate the pose of the camera and then construct a feature map portraying pixel-level ground depth according to the 3D-to-2D perspective geometry. Moreover, to improve Mono3D with the estimated ground depth, we design an RGB-D feature fusion network based on the transformer structure, where the long-range self-attention mechanism is utilized to effectively identify ground-contacting points and pin the corresponding ground depth to the image feature map. We conduct extensive experiments on the real-world KITTI dataset. The results demonstrate that MoGDE can effectively improve the Mono3D accuracy and robustness for both near and far objects. MoGDE yields the best performance compared with the state-of-the-art methods by a large margin and is ranked number one on the KITTI 3D benchmark.

</details>
