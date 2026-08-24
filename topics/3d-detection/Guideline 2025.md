# 3D Detection — 2025 Guideline

> 领域: 3D 目标检测（LiDAR / 相机 / 多模态融合）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### UniMamba: Unified Spatial-Channel Representation Learning with Group-Efficient Mamba for LiDAR-based 3D Object Detection.
- **链接**: [arXiv:2503.12009](https://arxiv.org/abs/2503.12009) · [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Jin_UniMamba_Unified_Spatial-Channel_Representation_Learning_with_Group-Efficient_Mamba_for_LiDAR-based_CVPR_2025_paper.html) · 📚 被引 18
- **作者**: Xin Jin, Haisheng Su, Kai Liu, Cong Ma, Wei Wu, Fei Hui et al.
- **🏷️ 机构**: Chang&#x2019;an University, Shanghai Jiao Tong University,School of Computer Science, SenseAuto Research
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Recent advances in LiDAR 3D detection have demonstrated the effectiveness of Transformer-based frameworks in capturing the global dependencies from point cloud spaces, which serialize the 3D voxels into the flattened 1D sequence for iterative self-attention. However, the spatial structure of 3D voxels will be inevitably destroyed during the serialization process. Besides, due to the considerable number of 3D voxels and quadratic complexity of Transformers, multiple sequences are grouped before feeding to Transformers, leading to a limited receptive field. Inspired by the impressive performance of State Space Models (SSM) achieved in the field of 2D vision tasks, in this paper, we propose a novel Unified Mamba (UniMamba), which seamlessly integrates the merits of 3D convolution and SSM in a concise multi-head manner, aiming to perform "local and global" spatial context aggregation efficiently and simultaneously. Specifically, a UniMamba block is designed which mainly consists of spatial locality modeling, complementary Z-order serialization and local-global sequential aggregator. The spatial locality modeling module integrates 3D submanifold convolution to capture the dynamic spatial position embedding before serialization. Then the efficient Z-order curve is adopted for serialization both horizontally and vertically. Furthermore, the local-global sequential aggregator adopts the channel grouping strategy to efficiently encode both "local and global" spatial inter-dependencies using multi-head SSM. Additionally, an encoder-decoder architecture with stacked UniMamba blocks is formed to facilitate multi-scale spatial learning hierarchically. Extensive experiments are conducted on three popular datasets: nuScenes, Waymo and Argoverse 2. Particularly, our UniMamba achieves 70.2 mAP on the nuScenes dataset.

### Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Cho_Ev-3DOD_Pushing_the_Temporal_Boundaries_of_3D_Object_Detection_with_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Hoonhee Cho, Jae-Young Kang, Youngho Kim, Kuk-Jin Yoon
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025

### RaCFormer: Towards High-Quality 3D Object Detection via Query-based Radar-Camera Fusion.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Chu_RaCFormer_Towards_High-Quality_3D_Object_Detection_via_Query-based_Radar-Camera_Fusion_CVPR_2025_paper.html) · 📚 被引 11
- **作者**: Xiaomeng Chu, Jiajun Deng, Guoliang You, Yifan Duan, Houqiang Li, Yanyong Zhang
- **🏷️ 机构**: University of Science and Technology of China, The University of Adelaide
- **会议**: CVPR 2025

### V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html)
- **作者**: Xun Huang, Jinlong Wang, Qiming Xia, Siheng Chen, Bisheng Yang, Xin Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Cubify Anything: Scaling Indoor 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lazarow_Cubify_Anything_Scaling_Indoor_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 8
- **作者**: Justin Lazarow, David Griffiths, Gefen Kohavi, Francisco Crespo, Afshin Dehghan
- **🏷️ 机构**: Apple
- **会议**: CVPR 2025

### FSHNet: Fully Sparse Hybrid Network for 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_FSHNet_Fully_Sparse_Hybrid_Network_for_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Shuai Liu, Mingyue Cui, Boyang Li, Quanmin Liang, Tinghe Hong, Yunxiao Shan et al.
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering, Sun Yat-sen University,School of Artificial Intelligence
- **会议**: CVPR 2025

### MonoTAKD: Teaching Assistant Knowledge Distillation for Monocular 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_MonoTAKD_Teaching_Assistant_Knowledge_Distillation_for_Monocular_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 5
- **作者**: Hou-I Liu, Christine Wu, Jen-Hao Cheng, Wenhao Chai, Shian-Yun Wang, Gaowen Liu et al.
- **🏷️ 机构**: National Yang Ming Chiao Tung University, University of Washington, University of Southern California
- **会议**: CVPR 2025

### RICCARDO: Radar Hit Prediction and Convolution for Camera-Radar 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Long_RICCARDO_Radar_Hit_Prediction_and_Convolution_for_Camera-Radar_3D_Object_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Yunfei Long, Abhinav Kumar, Xiaoming Liu, Daniel D. Morris
- **🏷️ 机构**: Michigan State University
- **会议**: CVPR 2025

### GBlobs: Explicit Local Structure via Gaussian Blobs for Improved Cross-Domain LiDAR-based 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Malic_GBlobs_Explicit_Local_Structure_via_Gaussian_Blobs_for_Improved_Cross-Domain_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Dusan Malic, Christian Fruhwirth-Reisinger, Samuel Schulter, Horst Possegger
- **🏷️ 机构**: Christian Doppler Laboratory for Embedded Machine Learning, Amazon
- **会议**: CVPR 2025

### Leveraging Temporal Cues for Semi-Supervised Multi-View 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Park_Leveraging_Temporal_Cues_for_Semi-Supervised_Multi-View_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 1
- **作者**: Jinhyung Park, Navyata Sanghvi, Hiroki Adachi, Yoshihisa Shibata, Shawn Hunt, Shinya Tanaka et al.
- **🏷️ 机构**: Carnegie Mellon University, DENSO Corporation, DENSO International America, Inc.
- **会议**: CVPR 2025

### MonoDGP: Monocular 3D Object Detection with Decoupled-Query and Geometry-Error Priors.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Pu_MonoDGP_Monocular_3D_Object_Detection_with_Decoupled-Query_and_Geometry-Error_Priors_CVPR_2025_paper.html) · 📚 被引 25
- **作者**: Fanqi Pu, Yifan Wang, Jiru Deng, Wenming Yang
- **🏷️ 机构**: Tsinghua University,Shenzhen International Graduate School
- **会议**: CVPR 2025

### Uncertainty Meets Diversity: A Comprehensive Active Learning Framework for Indoor 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Uncertainty_Meets_Diversity_A_Comprehensive_Active_Learning_Framework_for_Indoor_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Jiangyi Wang, Na Zhao
- **🏷️ 机构**: Singapore University of Technology and Design (SUTD)
- **会议**: CVPR 2025

### CorrBEV: Multi-View 3D Object Detection by Correlation Learning with Multi-modal Prototypes.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xue_CorrBEV_Multi-View_3D_Object_Detection_by_Correlation_Learning_with_Multi-modal_CVPR_2025_paper.html)
- **作者**: Ziteng Xue, Mingzhe Guo, Heng Fan, Shihui Zhang, Zhipeng Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### ViKIENet: Towards Efficient 3D Object Detection with Virtual Key Instance Enhanced Network.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_ViKIENet_Towards_Efficient_3D_Object_Detection_with_Virtual_Key_Instance_CVPR_2025_paper.html) · 📚 被引 9
- **作者**: Zhuochen Yu, Bijie Qiu, Andy W. H. Khong
- **🏷️ 机构**: Nanyang Technological University,School of Electrical and Electronic Engineering,Singapore
- **会议**: CVPR 2025

### SP3D: Boosting Sparsely-Supervised 3D Object Detection via Accurate Cross-Modal Semantic Prompts.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_SP3D_Boosting_Sparsely-Supervised_3D_Object_Detection_via_Accurate_Cross-Modal_Semantic_CVPR_2025_paper.html)
- **作者**: Shijia Zhao, Qiming Xia, Xusheng Guo, Pufan Zou, Maoji Zheng, Hai Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Learning Class Prototypes for Unified Sparse-Supervised 3D Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Learning_Class_Prototypes_for_Unified_Sparse-Supervised_3D_Object_Detection_CVPR_2025_paper.html) · 📚 被引 6
- **作者**: Yun Zhu, Le Hui, Hang Yang, Jianjun Qian, Jin Xie, Jian Yang
- **🏷️ 机构**: Nanjing University of Science and Technology,PCA Lab,Nanjing,China, Northwestern Polytechnical University,School of Electronics and Information,Xi&#x2019;an,China, Nanjing University,State Key Laboratory for Novel Software Technology,Nanjing,China
- **会议**: CVPR 2025

### DriveGEN: Generalized and Robust 3D Detection in Driving via Controllable Text-to-Image Diffusion Generation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_DriveGEN_Generalized_and_Robust_3D_Detection_in_Driving_via_Controllable_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Hongbin Lin, Zilu Guo, Yifan Zhang, Shuaicheng Niu, Yafeng Li, Ruimao Zhang et al.
- **🏷️ 机构**: FNii-Shenzhen, National University of Singapore, Nanyang Technological University
- **会议**: CVPR 2025
