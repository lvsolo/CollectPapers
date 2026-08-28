# Neural Architecture Search — 2021 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 22 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### iNAS: Integral NAS for Device-Aware Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00489) · 📚 被引 11
- **作者**: Yuchao Gu, Shang-Hua Gao, Xu-Sheng Cao, Peng Du, Shao-Ping Lu, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University,TKLNDST, CS, Huawei Technologies
- **会议**: ICCV 2021

### BossNAS: Exploring Hybrid CNN-transformers with Block-wisely Self-supervised Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01206)
- **作者**: Changlin Li, Tao Tang, Guangrun Wang, Jiefeng Peng, Bing Wang, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Evolving Search Space for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00659)
- **作者**: Yuanzheng Ci, Chen Lin, Ming Sun, Boyu Chen, Hongwen Zhang, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object tracking has achieved significant progress over the past few years. However, state-of-the-art trackers become increasingly heavy and expensive, which limits their deployments in resource-constrained applications. In this work, we present LightTrack, which uses neural architecture search (NAS) to design more lightweight and efficient object trackers. Comprehensive experiments show that our LightTrack is effective. It can find trackers that achieve superior performance compared to handcrafted SOTA trackers, such as SiamRPN++ and Ocean, while using much fewer model Flops and parameters. Moreover, when deployed on resource-constrained mobile chipsets, the discovered trackers run much faster. For example, on Snapdragon 845 Adreno GPU, LightTrack runs $12\times$ faster than Ocean, while using $13\times$ fewer parameters and $38\times$ fewer Flops. Such improvements might narrow the gap between academic models and industrial deployments in object tracking task. LightTrack is released at https://github.com/researchmm/LightTrack.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present BN-NAS, neural architecture search with Batch Normalization (BN-NAS), to accelerate neural architecture search (NAS). BN-NAS can significantly reduce the time required by model training and evaluation in NAS. Specifically, for fast evaluation, we propose a BN-based indicator for predicting subnet performance at a very early training stage. The BN-based indicator further facilitates us to improve the training efficiency by only training the BN parameters during the supernet training. This is based on our observation that training the whole supernet is not necessary while training only BN parameters accelerates network convergence for network architecture search. Extensive experiments show that our method can significantly shorten the time of training supernet by more than 10 times and shorten the time of evaluating subnets by more than 600,000 times without losing accuracy.

</details>

### GLiT: Neural Architecture Search for Global and Local Image Transformer.
- **链接**: [arXiv:2107.02960](https://arxiv.org/abs/2107.02960)
- **作者**: Boyu Chen, Peixia Li, Chuming Li, Baopu Li, Lei Bai, Chen Lin et al.
- **🏷️ 机构**: The University of Sydney, BAIDU USA LLC, University of Oxford
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### TransNAS-Bench-101: Improving Transferability and Generalizability of Cross-Task Neural Architecture Search.
- **链接**: [arXiv:2105.11871](https://arxiv.org/abs/2105.11871) · 📚 被引 50
- **作者**: Yawen Duan, Xin Chen, Hang Xu, Zewei Chen, Xiaodan Liang, Tong Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### DOTS: Decoupling Operation and Topology in Differentiable Architecture Search.
- **链接**: [arXiv:2010.00969](https://arxiv.org/abs/2010.00969) · 📚 被引 41
- **作者**: Yuchao Gu, Lijuan Wang, Yun Liu, Yi Yang, Yu-Huan Wu, Shao-Ping Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Searching by Generating: Flexible and Efficient One-Shot NAS With Architecture Generator.
- **链接**: [arXiv:2103.07289](https://arxiv.org/abs/2103.07289) · 📚 被引 17
- **作者**: Sian-Yao Huang, Wei-Ta Chu
- **🏷️ 机构**: National Cheng Kung University,Tainan,Taiwan
- **会议**: CVPR 2021

### Combined Depth Space Based Architecture Search for Person Re-Identification.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Combined_Depth_Space_Based_Architecture_Search_for_Person_Re-Identification_CVPR_2021_paper.html) · 📚 被引 167
- **作者**: Hanjun Li, Gaojie Wu, Wei-Shi Zheng
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Retinex-Inspired Unrolling With Cooperative Prior Architecture Search for Low-Light Image Enhancement.
- **链接**: [arXiv:2012.05609](https://arxiv.org/abs/2012.05609) · 📚 被引 969
- **作者**: Risheng Liu, Long Ma, Jiaao Zhang, Xin Fan, Zhongxuan Luo
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Low-light image enhancement plays very important roles in low-level vision field. Recent works have built a large variety of deep learning models to address this task. However, these approaches mostly rely on significant architecture engineering and suffer from high computational burden. In this paper, we propose a new method, named Retinex-inspired Unrolling with Architecture Search (RUAS), to construct lightweight yet effective enhancement network for low-light images in real-world scenario. Specifically, building upon Retinex rule, RUAS first establishes models to characterize the intrinsic underexposed structure of low-light images and unroll their optimization processes to construct our holistic propagation structure. Then by designing a cooperative reference-free learning strategy to discover low-light prior architectures from a compact search space, RUAS is able to obtain a top-performing image enhancement network, which is with fast speed and requires few computational resources. Extensive experiments verify the superiority of our RUAS framework against recently proposed state-of-the-art methods.

</details>

### Once Quantization-Aware Training: High Performance Extremely Low-bit Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00529) · 📚 被引 35
- **作者**: Mingzhu Shen, Feng Liang, Ruihao Gong, Yuhang Li, Chuming Li, Chen Lin et al.
- **🏷️ 机构**: Sensetime Research, University of Oxford
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural architecture search (NAS) has shown great promise in designing state-of-the-art (SOTA) models that are both accurate and efficient. Recently, two-stage NAS, e.g. BigNAS, decouples the model training and searching process and achieves remarkable search efficiency and accuracy. Two-stage NAS requires sampling from the search space during training, which directly impacts the accuracy of the final searched models. While uniform sampling has been widely used for its simplicity, it is agnostic of the model performance Pareto front, which is the main focus in the search process, and thus, misses opportunities to further improve the model accuracy. In this work, we propose AttentiveNAS that focuses on improving the sampling strategy to achieve better performance Pareto. We also propose algorithms to efficiently and effectively identify the networks on the Pareto during training. Without extra re-training or post-processing, we can simultaneously obtain a large number of networks across a wide range of FLOPs. Our discovered model family, AttentiveNAS models, achieves top-1 accuracy from 77.3% to 80.7% on ImageNet, and outperforms SOTA models, including BigNAS and Once-for-All networks. We also achieve ImageNet accuracy of 80.1% with only 491 MFLOPs. Our training code and pretrained models are available at https://github.com/facebookresearch/AttentiveNAS.

</details>

### IDARTS: Interactive Differentiable Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00120) · 📚 被引 11
- **作者**: Song Xue, Runqi Wang, Baochang Zhang, Tian Wang, Guodong Guo, David S. Doermann
- **🏷️ 机构**: Beihang University,Beijing,China, Institute of Deep Learning, Baidu Research,National Engineering Laboratory for Deep Learning Technology and Application,Beijing,China, University at Buffalo,USA
- **会议**: ICCV 2021

### Neural Architecture Search for Joint Human Parsing and Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01119) · 📚 被引 30
- **作者**: Dan Zeng, Yuhang Huang, Qian Bao, Junjie Zhang, Chi Su, Wu Liu
- **🏷️ 机构**: Shanghai University, AI Research of JD.com, Kingsoft Cloud
- **会议**: ICCV 2021

### FP-NAS: Fast Probabilistic Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yan_FP-NAS_Fast_Probabilistic_Neural_Architecture_Search_CVPR_2021_paper.html) · 📚 被引 18
- **作者**: Zhicheng Yan, Xiaoliang Dai, Peizhao Zhang, Yuandong Tian, Bichen Wu, Matt Feiszli
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### HourNAS: Extremely Fast Neural Architecture Search Through an Hourglass Lens.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_HourNAS_Extremely_Fast_Neural_Architecture_Search_Through_an_Hourglass_Lens_CVPR_2021_paper.html) · 📚 被引 11
- **作者**: Zhaohui Yang, Yunhe Wang, Xinghao Chen, Jianyuan Guo, Wei Zhang, Chao Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Towards Improving the Consistency, Efficiency, and Flexibility of Differentiable Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_Towards_Improving_the_Consistency_Efficiency_and_Flexibility_of_Differentiable_Neural_CVPR_2021_paper.html) · 📚 被引 37
- **作者**: Yibo Yang, Shan You, Hongyang Li, Fei Wang, Chen Qian, Zhouchen Lin
- **🏷️ 机构**: Shanghai AI Lab, Peking University
- **会议**: CVPR 2021

### Landmark Regularization: Ranking Guided Super-Net Training in Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Yu_Landmark_Regularization_Ranking_Guided_Super-Net_Training_in_Neural_Architecture_Search_CVPR_2021_paper.html) · 📚 被引 13
- **作者**: Kaicheng Yu, René Ranftl, Mathieu Salzmann
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

### Neural Architecture Search With Random Labels.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_Neural_Architecture_Search_With_Random_Labels_CVPR_2021_paper.html) · 📚 被引 46
- **作者**: Xuanyang Zhang, Pengfei Hou, Xiangyu Zhang, Jian Sun
- **🏷️ 机构**: MEGVII
- **会议**: CVPR 2021

### DCNAS: Densely Connected Neural Architecture Search for Semantic Image Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_DCNAS_Densely_Connected_Neural_Architecture_Search_for_Semantic_Image_Segmentation_CVPR_2021_paper.html) · 📚 被引 92
- **作者**: Xiong Zhang, Hongmin Xu, Hong Mo, Jianchao Tan, Cheng Yang, Lei Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

## 跨领域论文（完整笔记在其他领域）

- NPAS: A Compiler-Aware Framework of Unified Network Pruning and Architecture Search for Beyond Real-Time Mobile Acceleration. → [network-pruning](../network-pruning/Guideline%202021.md)
