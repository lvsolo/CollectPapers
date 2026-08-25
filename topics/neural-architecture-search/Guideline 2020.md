# Neural Architecture Search — 2020 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 24 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Hit-Detector: Hierarchical Trinity Architecture Search for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Guo_Hit-Detector_Hierarchical_Trinity_Architecture_Search_for_Object_Detection_CVPR_2020_paper.html)
- **作者**: Jianyuan Guo, Kai Han, Yunhe Wang, Chao Zhang, Zhaohui Yang, Han Wu et al.
- **🏷️ 机构**: Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University; Noah's Ark Lab, Huawei Technologies, Noah's Ark Lab, Huawei Technologies, Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University
- **会议**: CVPR 2020

### SP-NAS: Serial-to-Parallel Backbone Search for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Jiang_SP-NAS_Serial-to-Parallel_Backbone_Search_for_Object_Detection_CVPR_2020_paper.html) · 📚 被引 55
- **作者**: Chenhan Jiang, Hang Xu, Wei Zhang, Xiaodan Liang, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### NAS-FCOS: Fast Neural Architecture Search for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wang_NAS-FCOS_Fast_Neural_Architecture_Search_for_Object_Detection_CVPR_2020_paper.html) · 📚 被引 201
- **作者**: Ning Wang, Yang Gao, Hao Chen, Peng Wang, Zhi Tian, Chunhua Shen et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020

### Densely Connected Search Space for More Flexible Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_Densely_Connected_Search_Space_for_More_Flexible_Neural_Architecture_Search_CVPR_2020_paper.html) · 📚 被引 98
- **作者**: Jiemin Fang, Yuzhu Sun, Qian Zhang, Yuan Li, Wenyu Liu, Xinggang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Can Weight Sharing Outperform Random Architecture Search? An Investigation With TuNAS.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Bender_Can_Weight_Sharing_Outperform_Random_Architecture_Search_An_Investigation_With_CVPR_2020_paper.html)
- **作者**: Gabriel Bender, Hanxiao Liu, Bo Chen, Grace Chu, Shuyang Cheng, Pieter-Jan Kindermans et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### MTL-NAS: Task-Agnostic Neural Architecture Search Towards General-Purpose Multi-Task Learning.
- **链接**: [arXiv:2003.14058](https://arxiv.org/abs/2003.14058) · [代码](https://github.com/bhpfelix/MTLNAS) · 📚 被引 66
- **作者**: Yuan Gao, Haoping Bai, Zequn Jie, Jiayi Ma, Kui Jia, Wei Liu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > We propose to incorporate neural architecture search (NAS) into general-purpose multi-task learning (GP-MTL). Existing NAS methods typically define different search spaces according to different tasks. In order to adapt to different task combinations (i.e., task sets), we disentangle the GP-MTL networks into single-task backbones (optionally encode the task priors), and a hierarchical and layerwise features sharing/fusing scheme across them. This enables us to design a novel and general task-agnostic search space, which inserts cross-task edges (i.e., feature fusion connections) into fixed single-task network backbones. Moreover, we also propose a novel single-shot gradient-based search algorithm that closes the performance gap between the searched architectures and the final evaluation architecture. This is realized with a minimum entropy regularization on the architecture weights during the search phase, which makes the architecture weights converge to near-discrete values and therefore achieves a single model. As a result, our searched model can be directly used for evaluation without (re-)training from scratch. We perform extensive experiments using different single-task backbones on various task sets, demonstrating the promising performance obtained by exploiting the hierarchical and layerwise features, as well as the desirable generalizability to different i) task sets and ii) single-task backbones. The code of our paper is available at https://github.com/bhpfelix/MTLNAS.

### AdversarialNAS: Adversarial Neural Architecture Search for GANs.
- **链接**: [arXiv:1912.02037](https://arxiv.org/abs/1912.02037) · [代码](https://github.com/chengaopro/AdversarialNAS) · 📚 被引 77
- **作者**: Chen Gao, Yunpeng Chen, Si Liu, Zhenxiong Tan, Shuicheng Yan
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Neural Architecture Search (NAS) that aims to automate the procedure of architecture design has achieved promising results in many computer vision fields. In this paper, we propose an AdversarialNAS method specially tailored for Generative Adversarial Networks (GANs) to search for a superior generative model on the task of unconditional image generation. The AdversarialNAS is the first method that can search the architectures of generator and discriminator simultaneously in a differentiable manner. During searching, the designed adversarial search algorithm does not need to comput any extra metric to evaluate the performance of the searched architecture, and the search paradigm considers the relevance between the two network architectures and improves their mutual balance. Therefore, AdversarialNAS is very efficient and only takes 1 GPU day to search for a superior generative model in the proposed large search space ($10^{38}$). Experiments demonstrate the effectiveness and superiority of our method. The discovered generative model sets a new state-of-the-art FID score of $10.87$ and highly competitive Inception Score of $8.74$ on CIFAR-10. Its transferability is also proven by setting new state-of-the-art FID score of $26.98$ and Inception score of $9.63$ on STL-10. Code is at: \url{https://github.com/chengaopro/AdversarialNAS}.

### Organ at Risk Segmentation for Head and Neck Cancer Using Stratified Learning and Neural Architecture Search.
- **链接**: [arXiv:2004.08426](https://arxiv.org/abs/2004.08426)
- **作者**: Dazhou Guo, Dakai Jin, Zhuotun Zhu, Tsung-Ying Ho, Adam P. Harrison, Chun-Hung Chao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > OAR segmentation is a critical step in radiotherapy of head and neck (H&N) cancer, where inconsistencies across radiation oncologists and prohibitive labor costs motivate automated approaches. However, leading methods using standard fully convolutional network workflows that are challenged when the number of OARs becomes large, e.g. > 40. For such scenarios, insights can be gained from the stratification approaches seen in manual clinical OAR delineation. This is the goal of our work, where we introduce stratified organ at risk segmentation (SOARS), an approach that stratifies OARs into anchor, mid-level, and small & hard (S&H) categories. SOARS stratifies across two dimensions. The first dimension is that distinct processing pipelines are used for each OAR category. In particular, inspired by clinical practices, anchor OARs are used to guide the mid-level and S&H categories. The second dimension is that distinct network architectures are used to manage the significant contrast, size, and anatomy variations between different OARs. We use differentiable neural architecture search (NAS), allowing the network to choose among 2D, 3D or Pseudo-3D convolutions. Extensive 4-fold cross-validation on 142 H&N cancer patients with 42 manually labeled OARs, the most comprehensive OAR dataset to date, demonstrates that both pipeline- and NAS-stratification significantly improves quantitative performance over the state-of-the-art (from 69.52% to 73.68% in absolute Dice scores). Thus, SOARS provides a powerful and principled means to manage the highly complex segmentation space of OARs.

### When NAS Meets Robustness: In Search of Robust Architectures Against Adversarial Attacks.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Guo_When_NAS_Meets_Robustness_In_Search_of_Robust_Architectures_Against_CVPR_2020_paper.html) · 📚 被引 107
- **作者**: Minghao Guo, Yuzhe Yang, Rui Xu, Ziwei Liu, Dahua Lin
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2020

### MiLeNAS: Efficient Neural Architecture Search via Mixed-Level Reformulation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/He_MiLeNAS_Efficient_Neural_Architecture_Search_via_Mixed-Level_Reformulation_CVPR_2020_paper.html)
- **作者**: Chaoyang He, Haishan Ye, Li Shen, Tong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### DSNAS: Direct Neural Architecture Search Without Parameter Retraining.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Hu_DSNAS_Direct_Neural_Architecture_Search_Without_Parameter_Retraining_CVPR_2020_paper.html) · 📚 被引 85
- **作者**: Shoukang Hu, Sirui Xie, Hehui Zheng, Chunxiao Liu, Jianping Shi, Xunying Liu et al.
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2020

### Neural Architecture Search for Lightweight Non-Local Networks.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Neural_Architecture_Search_for_Lightweight_Non-Local_Networks_CVPR_2020_paper.html) · 📚 被引 35
- **作者**: Yingwei Li, Xiaojie Jin, Jieru Mei, Xiaochen Lian, Linjie Yang, Cihang Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Block-Wisely Supervised Neural Architecture Search With Knowledge Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Block-Wisely_Supervised_Neural_Architecture_Search_With_Knowledge_Distillation_CVPR_2020_paper.html) · 📚 被引 119
- **作者**: Changlin Li, Jiefeng Peng, Liuchun Yuan, Guangrun Wang, Xiaodan Liang, Liang Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### SGAS: Sequential Greedy Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_SGAS_Sequential_Greedy_Architecture_Search_CVPR_2020_paper.html)
- **作者**: Guohao Li, Guocheng Qian, Itzel C. Delgadillo, Matthias Müller, Ali K. Thabet, Bernard Ghanem
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### GP-NAS: Gaussian Process Based Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_GP-NAS_Gaussian_Process_Based_Neural_Architecture_Search_CVPR_2020_paper.html)
- **作者**: Zhihang Li, Teng Xi, Jiankang Deng, Gang Zhang, Shengzhao Wen, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### Graph-Guided Architecture Search for Real-Time Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Lin_Graph-Guided_Architecture_Search_for_Real-Time_Semantic_Segmentation_CVPR_2020_paper.html) · 📚 被引 87
- **作者**: Peiwen Lin, Peng Sun, Guangliang Cheng, Sirui Xie, Xi Li, Jianping Shi
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020

### MemNAS: Memory-Efficient Neural Architecture Search With Grow-Trim Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_MemNAS_Memory-Efficient_Neural_Architecture_Search_With_Grow-Trim_Learning_CVPR_2020_paper.html) · 📚 被引 12
- **作者**: Peiye Liu, Bo Wu, Huadong Ma, Mingoo Seok
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### UNAS: Differentiable Architecture Search Meets Reinforcement Learning.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Vahdat_UNAS_Differentiable_Architecture_Search_Meets_Reinforcement_Learning_CVPR_2020_paper.html) · 📚 被引 24
- **作者**: Arash Vahdat, Arun Mallya, Ming-Yu Liu, Jan Kautz
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### FBNetV2: Differentiable Neural Architecture Search for Spatial and Channel Dimensions.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Wan_FBNetV2_Differentiable_Neural_Architecture_Search_for_Spatial_and_Channel_Dimensions_CVPR_2020_paper.html) · 📚 被引 238
- **作者**: Alvin Wan, Xiaoliang Dai, Peizhao Zhang, Zijian He, Yuandong Tian, Saining Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### CARS: Continuous Evolution for Efficient Neural Architecture Search.
- **链接**: [arXiv:1909.04977](https://arxiv.org/abs/1909.04977) · 📚 被引 215
- **作者**: Zhaohui Yang, Yunhe Wang, Xinghao Chen, Boxin Shi, Chao Xu, Chunjing Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > Searching techniques in most of existing neural architecture search (NAS) algorithms are mainly dominated by differentiable methods for the efficiency reason. In contrast, we develop an efficient continuous evolutionary approach for searching neural networks. Architectures in the population that share parameters within one SuperNet in the latest generation will be tuned over the training dataset with a few epochs. The searching in the next evolution generation will directly inherit both the SuperNet and the population, which accelerates the optimal network generation. The non-dominated sorting strategy is further applied to preserve only results on the Pareto front for accurately updating the SuperNet. Several neural networks with different model sizes and performances will be produced after the continuous search with only 0.4 GPU days. As a result, our framework provides a series of networks with the number of parameters ranging from 3.7M to 5.1M under mobile settings. These networks surpass those produced by the state-of-the-art methods on the benchmark ImageNet dataset.

### C2FNAS: Coarse-to-Fine Neural Architecture Search for 3D Medical Image Segmentation.
- **链接**: [arXiv:1912.09628](https://arxiv.org/abs/1912.09628)
- **作者**: Qihang Yu, Dong Yang, Holger Roth, Yutong Bai, Yixiao Zhang, Alan L. Yuille et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

- **摘要（英，原文）**:

  > 3D convolution neural networks (CNN) have been proved very successful in parsing organs or tumours in 3D medical images, but it remains sophisticated and time-consuming to choose or design proper 3D networks given different task contexts. Recently, Neural Architecture Search (NAS) is proposed to solve this problem by searching for the best network architecture automatically. However, the inconsistency between search stage and deployment stage often exists in NAS algorithms due to memory constraints and large search space, which could become more serious when applying NAS to some memory and time consuming tasks, such as 3D medical image segmentation. In this paper, we propose coarse-to-fine neural architecture search (C2FNAS) to automatically search a 3D segmentation network from scratch without inconsistency on network size or input size. Specifically, we divide the search procedure into two stages: 1) the coarse stage, where we search the macro-level topology of the network, i.e. how each convolution module is connected to other modules; 2) the fine stage, where we search at micro-level for operations in each cell based on previous searched macro-level topology. The coarse-to-fine manner divides the search procedure into two consecutive stages and meanwhile resolves the inconsistency. We evaluate our method on 10 public datasets from Medical Segmentation Decalthon (MSD) challenge, and achieve state-of-the-art performance with the network searched using one dataset, which demonstrates the effectiveness and generalization of our searched models.

### Memory-Efficient Hierarchical Neural Architecture Search for Image Denoising.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhang_Memory-Efficient_Hierarchical_Neural_Architecture_Search_for_Image_Denoising_CVPR_2020_paper.html) · 📚 被引 57
- **作者**: Haokui Zhang, Ying Li, Hao Chen, Chunhua Shen
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020

### Rethinking Performance Estimation in Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zheng_Rethinking_Performance_Estimation_in_Neural_Architecture_Search_CVPR_2020_paper.html) · 📚 被引 24
- **作者**: Xiawu Zheng, Rongrong Ji, Qiang Wang, Qixiang Ye, Zhenguo Li, Yonghong Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### EcoNAS: Finding Proxies for Economical Neural Architecture Search.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhou_EcoNAS_Finding_Proxies_for_Economical_Neural_Architecture_Search_CVPR_2020_paper.html) · 📚 被引 93
- **作者**: Dongzhan Zhou, Xinchi Zhou, Wenwei Zhang, Chen Change Loy, Shuai Yi, Xuesen Zhang et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: CVPR 2020
