# 3D Detection — 2025 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 24 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00749)
- **作者**: Adrian Chow, Evelien Riddell, Yimu Wang, Sean Sedwards, Krzysztof Czarnecki
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### OcRFDet: Object-Centric Radiance Fields for Multi-View 3D Object Detection in Autonomous Driving.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02312)
- **作者**: Mingqian Ji, Shanshan Zhang, Jian Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02348)
- **作者**: Geonho Bang, Minjae Seong, Jisong Kim, Geunju Baek, Daye Oh, Junhyung Kim et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Robust 3D Object Detection Using Probabilistic Point Clouds From Single-Photon Lidars.
- **链接**: [arXiv:2508.00169](https://arxiv.org/abs/2508.00169) · 📚 被引 0
- **作者**: Bhavya Goyal, Felipe Gutierrez-Barragan, Wei Lin, Andreas Velten, Yin Li, Mohit Gupta
- **🏷️ 机构**: University of Wisconsin-Madison
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> LiDAR-based 3D sensors provide point clouds, a canonical 3D representation used in various scene understanding tasks. Modern LiDARs face key challenges in several real-world scenarios, such as long-distance or low-albedo objects, producing sparse or erroneous point clouds. These errors, which are rooted in the noisy raw LiDAR measurements, get propagated to downstream perception models, resulting in potentially severe loss of accuracy. This is because conventional 3D processing pipelines do not retain any uncertainty information from the raw measurements when constructing point clouds. We propose Probabilistic Point Clouds (PPC), a novel 3D scene representation where each point is augmented with a probability attribute that encapsulates the measurement uncertainty (or confidence) in the raw data. We further introduce inference approaches that leverage PPC for robust 3D object detection; these methods are versatile and can be used as computationally lightweight drop-in modules in 3D inference pipelines. We demonstrate, via both simulations and real captures, that PPC-based 3D inference methods outperform several baselines using LiDAR as well as camera-LiDAR fusion models, across challenging indoor and outdoor scenarios involving small, distant, and low-albedo objects, as well as strong ambient light. Our project webpage is at https://bhavyagoyal.github.io/ppc .

</details>

### OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00813)
- **作者**: Peng-Hao Hsu, Ke Zhang, Fu-En Wang, Tao Tu, Ming-Feng Li, Yu-Lun Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts.
- **链接**: [arXiv:2508.20488](https://arxiv.org/abs/2508.20488) · 📚 被引 0
- **作者**: Zixuan Hu, Dongxiao Li, Xinzhu Ma, Shixiang Tang, Xiaotong Li, Wenhan Yang et al.
- **🏷️ 机构**: School of Computer Science, Peking University,Beijing,China, The Chinese University of Hong Kong,Hongkong,China, Peng Cheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate monocular 3D object detection (M3OD) is pivotal for safety-critical applications like autonomous driving, yet its reliability deteriorates significantly under real-world domain shifts caused by environmental or sensor variations. To address these shifts, Test-Time Adaptation (TTA) methods have emerged, enabling models to adapt to target distributions during inference. While prior TTA approaches recognize the positive correlation between low uncertainty and high generalization ability, they fail to address the dual uncertainty inherent to M3OD: semantic uncertainty (ambiguous class predictions) and geometric uncertainty (unstable spatial localization). To bridge this gap, we propose Dual Uncertainty Optimization (DUO), the first TTA framework designed to jointly minimize both uncertainties for robust M3OD. Through a convex optimization lens, we introduce an innovative convex structure of the focal loss and further derive a novel unsupervised version, enabling label-agnostic uncertainty weighting and balanced learning for high-uncertainty objects. In parallel, we design a semantic-aware normal field constraint that preserves geometric coherence in regions with clear semantic cues, reducing uncertainty from the unstable 3D representation. This dual-branch mechanism forms a complementary loop: enhanced spatial perception improves semantic classification, and robust semantic predictions further refine spatial understanding. Extensive experiments demonstrate the superiority of DUO over existing methods across various datasets and domain shift types.

</details>

### GeoFormer: Geometry Point Encoder for 3D Object Detection with Graph-Based Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02495) · 📚 被引 1
- **作者**: Xin Jin, Haisheng Su, Cong Ma, Kai Liu, Wei Wu, Fei Hui et al.
- **🏷️ 机构**: Chang&#x0027; an University, Shanghai Jiao Tong University, SenseAuto Research
- **会议**: ICCV 2025

### Unleashing the Temporal Potential of Stereo Event Cameras for Continuous-Time 3D Object Detection.
- **链接**: [arXiv:2508.02288](https://arxiv.org/abs/2508.02288) · [代码](https://github.com/mickeykang16/Ev-Stereo3D) · 📚 被引 2
- **作者**: Jae-Young Kang, Hoonhee Cho, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D object detection is essential for autonomous systems, enabling precise localization and dimension estimation. While LiDAR and RGB cameras are widely used, their fixed frame rates create perception gaps in high-speed scenarios. Event cameras, with their asynchronous nature and high temporal resolution, offer a solution by capturing motion continuously. The recent approach, which integrates event cameras with conventional sensors for continuous-time detection, struggles in fast-motion scenarios due to its dependency on synchronized sensors. We propose a novel stereo 3D object detection framework that relies solely on event cameras, eliminating the need for conventional 3D sensors. To compensate for the lack of semantic and geometric information in event data, we introduce a dual filter mechanism that extracts both. Additionally, we enhance regression by aligning bounding boxes with object-centric information. Experiments show that our method outperforms prior approaches in dynamic environments, demonstrating the potential of event cameras for robust, continuous-time 3D perception. The code is available at https://github.com/mickeykang16/Ev-Stereo3D.

</details>

### MemDistill: Distilling LiDAR Knowledge into Memory for Camera-Only 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00642)
- **作者**: Donghyeon Kwon, Youngseok Yoon, Hyeongseok Son, Suha Kwak
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### EVT: Efficient View Transformation for Multi-Modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02472)
- **作者**: Yongjin Lee, Hyeon Mun Jeong, Yurim Jeon, Sanghyun Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Perspective-Invariant 3D Object Detection.
- **链接**: [arXiv:2507.17665](https://arxiv.org/abs/2507.17665) · 📚 被引 1
- **作者**: Ao Liang, Lingdong Kong, Dongyue Lu, Youquan Liu, Jian Fang, Huaici Zhao et al.
- **🏷️ 机构**: National University of Singapore, Fudan University, Shenyang Institute of Automation, Chinese Academy of Sciences
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rise of robotics, LiDAR-based 3D object detection has garnered significant attention in both academia and industry. However, existing datasets and methods predominantly focus on vehicle-mounted platforms, leaving other autonomous platforms underexplored. To bridge this gap, we introduce Pi3DET, the first benchmark featuring LiDAR data and 3D bounding box annotations collected from multiple platforms: vehicle, quadruped, and drone, thereby facilitating research in 3D object detection for non-vehicle platforms as well as cross-platform 3D detection. Based on Pi3DET, we propose a novel cross-platform adaptation framework that transfers knowledge from the well-studied vehicle platform to other platforms. This framework achieves perspective-invariant 3D detection through robust alignment at both geometric and feature levels. Additionally, we establish a benchmark to evaluate the resilience and robustness of current 3D detectors in cross-platform scenarios, providing valuable insights for developing adaptive 3D perception systems. Extensive experiments validate the effectiveness of our approach on challenging cross-platform tasks, demonstrating substantial gains over existing adaptation methods. We hope this work paves the way for generalizable and unified 3D perception systems across diverse and complex environments. Our Pi3DET dataset, cross-platform benchmark suite, and annotation toolkit have been made publicly available.

</details>

### Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02403)
- **作者**: Linshen Liu, Boyan Su, Junyue Jiang, Guanlin Wu, Cong Guo, Ceyu Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### FreqPDE: Rethinking Positional Depth Embedding for Multi-View 3D Object Detection Transformers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02613)
- **作者**: Haisheng Su, Junjie Zhang, Feixiang Song, Sanping Zhou, Wei Wu, Junchi Yan et al.
- **🏷️ 机构**: XJTU
- **会议**: ICCV 2025

### Height-Fidelity Dense Global Fusion for Multi-Modal 3D Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02475)
- **作者**: Hanshi Wang, Jin Gao, Weiming Hu, Zhipeng Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Motal: Unsupervised 3D Object Detection by Modality and Task-Specific Knowledge Transfer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00593) · 📚 被引 0
- **作者**: Hai Wu, Hongwei Lin, Xusheng Guo, Xin Li, Mingming Wang, Cheng Wang et al.
- **🏷️ 机构**: Xiamen University, Texas A&#x0026;M University, Tsinghua University
- **会议**: ICCV 2025

### Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02143)
- **作者**: Lizhen Xu, Xiuxiu Bai, Xiaojun Jia, Jianwu Fang, Shanmin Pang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Boosting Multi-View Indoor 3D Object Detection Via Adaptive 3D Volume Construction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00565)
- **作者**: Runmin Zhang, Zhu Yu, Si-Yuan Cao, Lingyu Zhu, Guangyi Zhang, Xiaokai Bai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Harnessing Uncertainty-Aware Bounding Boxes for Unsupervised 3D Object Detection.
- **链接**: [arXiv:2408.00619](https://arxiv.org/abs/2408.00619) · 📚 被引 1
- **作者**: Ruiyang Zhang, Hu Zhang, Zhedong Zheng
- **🏷️ 机构**: FST and ICI, University of Macau,China, CSIRO Data61,Australia
- **会议**: ICCV 2025

### CVFusion: Cross-View Fusion of 4D Radar and Camera for 3D Object Detection.
- **链接**: [arXiv:2507.04587](https://arxiv.org/abs/2507.04587) · 📚 被引 4
- **作者**: Hanzhi Zhong, Zhiyu Xiang, Ruoyu Xu, Jingyun Fu, Peng Xu, Shaohong Wang et al.
- **🏷️ 机构**: Zhejiang University,China
- **会议**: ICCV 2025

### Doppler-Aware LiDAR-RADAR Fusion for Weather-Robust 3D Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02525) · 📚 被引 2
- **作者**: Yujeong Chae, Heejun Park, Hyeonseong Kim, Kuk-Jin Yoon
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology
- **会议**: ICCV 2025

### VoxelKP: A Voxel-Based Network Architecture for Human Keypoint Estimation in LiDAR Data.
- **链接**: [arXiv:2312.08871](https://arxiv.org/abs/2312.08871) · 📚 被引 0
- **作者**: Jian Shi, Peter Wonka
- **🏷️ 机构**: KAUST
- **会议**: ICCV 2025

### HVPUNet: Hybrid-Voxel Point-Cloud Upsampling Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02707) · 📚 被引 0
- **作者**: Juhyung Ha, Vibhas K. Vats, Soon-Heung Jung, Md. Alimoor Reza, David J. Crandall
- **🏷️ 机构**: Luddy School of Informatics, Computing, and Engineering, Indiana University,Bloomington,IN,USA, Electronics and Telecommunications Research Institute,Daejeon,Republic of Korea, Drake University,Department of Mathematics and Computer Science,Des Moines,IA,USA
- **会议**: ICCV 2025

### Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images.
- **链接**: [arXiv:2508.02323](https://arxiv.org/abs/2508.02323) · 📚 被引 1
- **作者**: Philipp Wulff, Felix Wimbauer, Dominik Muhle, Daniel Cremers
- **🏷️ 机构**: Technical University of Munich,Munich,Germany
- **会议**: ICCV 2025

### SDFormer: Vision-Based 3D Semantic Scene Completion via SAM-Assisted Dual-Channel Voxel Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02491) · 📚 被引 0
- **作者**: Yujie Xue, Huilong Pi, Jiapeng Zhang, Yunchuan Qin, Zhuo Tang, Kenli Li et al.
- **🏷️ 机构**: College of Computer Science and Electronic Engineering, Hunan University
- **会议**: ICCV 2025
