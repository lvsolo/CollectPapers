# 3D Detection — 2024 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 15 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Towards Flexible 3D Perception: Object-Centric Occupancy Completion Augments 3D Object Detection.
- **链接**: [arXiv:2412.05154](https://arxiv.org/abs/2412.05154) · 📚 被引 1
- **作者**: Chaoda Zheng, Feng Wang, Naiyan Wang, Shuguang Cui, Zhen Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While 3D object bounding box (bbox) representation has been widely used in autonomous driving perception, it lacks the ability to capture the precise details of an object's intrinsic geometry. Recently, occupancy has emerged as a promising alternative for 3D scene perception. However, constructing a high-resolution occupancy map remains infeasible for large scenes due to computational constraints. Recognizing that foreground objects only occupy a small portion of the scene, we introduce object-centric occupancy as a supplement to object bboxes. This representation not only provides intricate details for detected objects but also enables higher voxel resolution in practical applications. We advance the development of object-centric occupancy perception from both data and algorithm perspectives. On the data side, we construct the first object-centric occupancy dataset from scratch using an automated pipeline. From the algorithmic standpoint, we introduce a novel object-centric occupancy completion network equipped with an implicit shape decoder that manages dynamic-size occupancy generation. This network accurately predicts the complete object-centric occupancy volume for inaccurate object proposals by leveraging temporal information from long sequences. Our method demonstrates robust performance in completing object shapes under noisy detection and tracking conditions. Additionally, we show that our occupancy features significantly enhance the detection results of state-of-the-art 3D object detectors, especially for incomplete or distant objects in the Waymo Open Dataset.

</details>

### UNION: Unsupervised 3D Object Detection using Object Appearance-based Pseudo-Classes.
- **链接**: [arXiv:2405.15688](https://arxiv.org/abs/2405.15688) · [代码](https://github.com/TedLentsch/UNION) · 📚 被引 2
- **作者**: Ted de Vries Lentsch, Holger Caesar, Dariu Gavrila
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unsupervised 3D object detection methods have emerged to leverage vast amounts of data without requiring manual labels for training. Recent approaches rely on dynamic objects for learning to detect mobile objects but penalize the detections of static instances during training. Multiple rounds of self-training are used to add detected static instances to the set of training targets; this procedure to improve performance is computationally expensive. To address this, we propose the method UNION. We use spatial clustering and self-supervised scene flow to obtain a set of static and dynamic object proposals from LiDAR. Subsequently, object proposals' visual appearances are encoded to distinguish static objects in the foreground and background by selecting static instances that are visually similar to dynamic objects. As a result, static and dynamic mobile objects are obtained together, and existing detectors can be trained with a single training. In addition, we extend 3D object discovery to detection by using object appearance-based cluster labels as pseudo-class labels for training object classification. We conduct extensive experiments on the nuScenes dataset and increase the state-of-the-art performance for unsupervised 3D object discovery, i.e. UNION more than doubles the average precision to 39.5. The code is available at github.com/TedLentsch/UNION.

</details>

### LION: Linear Group RNN for 3D Object Detection in Point Clouds.
- **链接**: [arXiv:2407.18232](https://arxiv.org/abs/2407.18232) · 📚 被引 29
- **作者**: Zhe Liu, Jinghua Hou, Xinyu Wang, Xiaoqing Ye, Jingdong Wang, Hengshuang Zhao et al.
- **🏷️ 机构**: HUAST
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The benefit of transformers in large-scale 3D point cloud perception tasks, such as 3D object detection, is limited by their quadratic computation cost when modeling long-range relationships. In contrast, linear RNNs have low computational complexity and are suitable for long-range modeling. Toward this goal, we propose a simple and effective window-based framework built on LInear grOup RNN (i.e., perform linear RNN for grouped features) for accurate 3D object detection, called LION. The key property is to allow sufficient feature interaction in a much larger group than transformer-based methods. However, effectively applying linear group RNN to 3D object detection in highly sparse point clouds is not trivial due to its limitation in handling spatial modeling. To tackle this problem, we simply introduce a 3D spatial feature descriptor and integrate it into the linear group RNN operators to enhance their spatial features rather than blindly increasing the number of scanning orders for voxel features. To further address the challenge in highly sparse point clouds, we propose a 3D voxel generation strategy to densify foreground features thanks to linear group RNN as a natural property of auto-regressive models. Extensive experiments verify the effectiveness of the proposed components and the generalization of our LION on different linear group RNN operators including Mamba, RWKV, and RetNet. Furthermore, it is worth mentioning that our LION-Mamba achieves state-of-the-art on Waymo, nuScenes, Argoverse V2, and ONCE dataset. Last but not least, our method supports kinds of advanced linear RNN operators (e.g., RetNet, RWKV, Mamba, xLSTM and TTT) on small but popular KITTI dataset for a quick experience with our linear RNN-based framework.

</details>

### Unified Domain Generalization and Adaptation for Multi-View 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/6b7e1e96243c9edc378f85e7d232e415-Abstract-Conference.html)
- **作者**: Gyusam Chang, Jiwon Lee, Donghyun Kim, Jinkyu Kim, Dongwook Lee, Daehyun Ji et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### DiffuBox: Refining 3D Object Detection with Point Diffusion.
- **链接**: [arXiv:2405.16034](https://arxiv.org/abs/2405.16034) · [代码](https://github.com/cxy1997/DiffuBox)
- **作者**: Xiangyu Chen, Zhenzhen Liu, Katie Luo, Siddhartha Datta, Adhitya Polavaram, Yan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Ensuring robust 3D object detection and localization is crucial for many applications in robotics and autonomous driving. Recent models, however, face difficulties in maintaining high performance when applied to domains with differing sensor setups or geographic locations, often resulting in poor localization accuracy due to domain shift. To overcome this challenge, we introduce a novel diffusion-based box refinement approach. This method employs a domain-agnostic diffusion model, conditioned on the LiDAR points surrounding a coarse bounding box, to simultaneously refine the box's location, size, and orientation. We evaluate this approach under various domain adaptation settings, and our results reveal significant improvements across different datasets, object classes and detectors. Our PyTorch implementation is available at \href{https://github.com/cxy1997/DiffuBox}{https://github.com/cxy1997/DiffuBox}.

</details>

### CRT-Fusion: Camera, Radar, Temporal Fusion Using Motion Information for 3D Object Detection.
- **链接**: [arXiv:2411.03013](https://arxiv.org/abs/2411.03013) · 📚 被引 4
- **作者**: Jisong Kim, Minjae Seong, Jun Won Choi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate and robust 3D object detection is a critical component in autonomous vehicles and robotics. While recent radar-camera fusion methods have made significant progress by fusing information in the bird's-eye view (BEV) representation, they often struggle to effectively capture the motion of dynamic objects, leading to limited performance in real-world scenarios. In this paper, we introduce CRT-Fusion, a novel framework that integrates temporal information into radar-camera fusion to address this challenge. Our approach comprises three key modules: Multi-View Fusion (MVF), Motion Feature Estimator (MFE), and Motion Guided Temporal Fusion (MGTF). The MVF module fuses radar and image features within both the camera view and bird's-eye view, thereby generating a more precise unified BEV representation. The MFE module conducts two simultaneous tasks: estimation of pixel-wise velocity information and BEV segmentation. Based on the velocity and the occupancy score map obtained from the MFE module, the MGTF module aligns and fuses feature maps across multiple timestamps in a recurrent manner. By considering the motion of dynamic objects, CRT-Fusion can produce robust BEV feature maps, thereby improving detection accuracy and robustness. Extensive evaluations on the challenging nuScenes dataset demonstrate that CRT-Fusion achieves state-of-the-art performance for radar-camera-based 3D object detection. Our approach outperforms the previous best method in terms of NDS by +1.7%, while also surpassing the leading approach in mAP by +1.4%. These significant improvements in both metrics showcase the effectiveness of our proposed fusion strategy in enhancing the reliability and accuracy of 3D object detection.

</details>

### Real-time Stereo-based 3D Object Detection for Streaming Perception.
- **链接**: [arXiv:2410.12394](https://arxiv.org/abs/2410.12394) · [代码](https://github.com/weiyangdaren/streamDSGN-pytorch) · 📚 被引 0
- **作者**: Changcai Li, Zonghua Gu, Gang Chen, Libo Huang, Wei Zhang, Huihui Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to promptly respond to environmental changes is crucial for the perception system of autonomous driving. Recently, a new task called streaming perception was proposed. It jointly evaluate the latency and accuracy into a single metric for video online perception. In this work, we introduce StreamDSGN, the first real-time stereo-based 3D object detection framework designed for streaming perception. StreamDSGN is an end-to-end framework that directly predicts the 3D properties of objects in the next moment by leveraging historical information, thereby alleviating the accuracy degradation of streaming perception. Further, StreamDSGN applies three strategies to enhance the perception accuracy: (1) A feature-flow-based fusion method, which generates a pseudo-next feature at the current moment to address the misalignment issue between feature and ground truth. (2) An extra regression loss for explicit supervision of object motion consistency in consecutive frames. (3) A large kernel backbone with a large receptive field for effectively capturing long-range spatial contextual features caused by changes in object positions. Experiments on the KITTI Tracking dataset show that, compared with the strong baseline, StreamDSGN significantly improves the streaming average precision by up to 4.33%. Our code is available at https://github.com/weiyangdaren/streamDSGN-pytorch.

</details>

### 3DET-Mamba: Causal Sequence Modelling for End-to-End 3D Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/547108084f0c2af39b956f8eadb75d1b-Abstract-Conference.html) · 📚 被引 3
- **作者**: Mingsheng Li, Jiakang Yuan, Sijin Chen, Lin Zhang, Anyu Zhu, Xin Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### STONE: A Submodular Optimization Framework for Active 3D Object Detection.
- **链接**: [arXiv:2410.03918](https://arxiv.org/abs/2410.03918) · [代码](https://github.com/RuiyuM/STONE) · 📚 被引 0
- **作者**: Ruiyu Mao, Sarthak Kumar Maharana, Rishabh K. Iyer, Yunhui Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is fundamentally important for various emerging applications, including autonomous driving and robotics. A key requirement for training an accurate 3D object detector is the availability of a large amount of LiDAR-based point cloud data. Unfortunately, labeling point cloud data is extremely challenging, as accurate 3D bounding boxes and semantic labels are required for each potential object. This paper proposes a unified active 3D object detection framework, for greatly reducing the labeling cost of training 3D object detectors. Our framework is based on a novel formulation of submodular optimization, specifically tailored to the problem of active 3D object detection. In particular, we address two fundamental challenges associated with active 3D object detection: data imbalance and the need to cover the distribution of the data, including LiDAR-based point cloud data of varying difficulty levels. Extensive experiments demonstrate that our method achieves state-of-the-art performance with high computational efficiency compared to existing active learning methods. The code is available at https://github.com/RuiyuM/STONE.

</details>

### One for All: Multi-Domain Joint Training for Point Cloud Based 3D Object Detection.
- **链接**: [arXiv:2411.01584](https://arxiv.org/abs/2411.01584) · 📚 被引 3
- **作者**: Zhenyu Wang, Yali Li, Hengshuang Zhao, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The current trend in computer vision is to utilize one universal model to address all various tasks. Achieving such a universal model inevitably requires incorporating multi-domain data for joint training to learn across multiple problem scenarios. In point cloud based 3D object detection, however, such multi-domain joint training is highly challenging, because large domain gaps among point clouds from different datasets lead to the severe domain-interference problem. In this paper, we propose \textbf{OneDet3D}, a universal one-for-all model that addresses 3D detection across different domains, including diverse indoor and outdoor scenes, within the \emph{same} framework and only \emph{one} set of parameters. We propose the domain-aware partitioning in scatter and context, guided by a routing mechanism, to address the data interference issue, and further incorporate the text modality for a language-guided classification to unify the multi-dataset label spaces and mitigate the category interference issue. The fully sparse structure and anchor-free head further accommodate point clouds with significant scale disparities. Extensive experiments demonstrate the strong universal ability of OneDet3D to utilize only one trained model for addressing almost all 3D object detection tasks.

</details>

### MVSDet: Multi-View Indoor 3D Object Detection via Efficient Plane Sweeps.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ef8080f246b4b2c7a2b26daee6e6f22a-Abstract-Conference.html)
- **作者**: Yating Xu, Chen Li, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### ImOV3D: Learning Open Vocabulary Point Clouds 3D Object Detection from Only 2D Images.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/ff9783ec29688387d44779d67d06ef66-Abstract-Conference.html)
- **作者**: Timing Yang, Yuanliang Ju, Li Yi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Voxel Mamba: Group-Free State Space Models for Point Cloud based 3D Object Detection.
- **链接**: [arXiv:2406.10700](https://arxiv.org/abs/2406.10700) · 📚 被引 29
- **作者**: Guowen Zhang, Lue Fan, Chenhang He, Zhen Lei, Zhaoxiang Zhang, Lei Zhang
- **🏷️ 机构**: PolyU / OPPO
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Serialization-based methods, which serialize the 3D voxels and group them into multiple sequences before inputting to Transformers, have demonstrated their effectiveness in 3D object detection. However, serializing 3D voxels into 1D sequences will inevitably sacrifice the voxel spatial proximity. Such an issue is hard to be addressed by enlarging the group size with existing serialization-based methods due to the quadratic complexity of Transformers with feature sizes. Inspired by the recent advances of state space models (SSMs), we present a Voxel SSM, termed as Voxel Mamba, which employs a group-free strategy to serialize the whole space of voxels into a single sequence. The linear complexity of SSMs encourages our group-free design, alleviating the loss of spatial proximity of voxels. To further enhance the spatial proximity, we propose a Dual-scale SSM Block to establish a hierarchical structure, enabling a larger receptive field in the 1D serialization curve, as well as more complete local regions in 3D space. Moreover, we implicitly apply window partition under the group-free framework by positional encoding, which further enhances spatial proximity by encoding voxel positional information. Our experiments on Waymo Open Dataset and nuScenes dataset show that Voxel Mamba not only achieves higher accuracy than state-of-the-art methods, but also demonstrates significant advantages in computational efficiency.

</details>

### MonoMAE: Enhancing Monocular 3D Detection through Depth-Aware Masked Autoencoders.
- **链接**: [arXiv:2405.07696](https://arxiv.org/abs/2405.07696) · 📚 被引 11
- **作者**: Xueying Jiang, Sheng Jin, Xiaoqin Zhang, Ling Shao, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Monocular 3D object detection aims for precise 3D localization and identification of objects from a single-view image. Despite its recent progress, it often struggles while handling pervasive object occlusions that tend to complicate and degrade the prediction of object dimensions, depths, and orientations. We design MonoMAE, a monocular 3D detector inspired by Masked Autoencoders that addresses the object occlusion issue by masking and reconstructing objects in the feature space. MonoMAE consists of two novel designs. The first is depth-aware masking that selectively masks certain parts of non-occluded object queries in the feature space for simulating occluded object queries for network training. It masks non-occluded object queries by balancing the masked and preserved query portions adaptively according to the depth information. The second is lightweight query completion that works with the depth-aware masking to learn to reconstruct and complete the masked object queries. With the proposed object occlusion and completion, MonoMAE learns enriched 3D representations that achieve superior monocular 3D detection performance qualitatively and quantitatively for both occluded and non-occluded objects. Additionally, MonoMAE learns generalizable representations that can work well in new domains.

</details>

### Training an Open-Vocabulary Monocular 3D Detection Model without 3D Data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/8492211e9176b8abdaeb1f7aa4c223ea-Abstract-Conference.html)
- **作者**: Rui Huang, Henry Zheng, Yan Wang, Zhuofan Xia, Marco Pavone, Gao Huang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024
