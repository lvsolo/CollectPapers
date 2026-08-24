# Neural Architecture Search — 2021 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### iNAS: Integral NAS for Device-Aware Salient Object Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00489) · 📚 13 citations
- **作者**: Yuchao Gu, Shang-Hua Gao, Xu-Sheng Cao, Peng Du, Shao-Ping Lu, Ming-Ming Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Evolving Search Space for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00659) · 📚 50 citations
- **作者**: Yuanzheng Ci, Chen Lin, Ming Sun, Boyu Chen, Hongwen Zhang, Wanli Ouyang
- **🏷️ 机构**: The University of Sydney
- **会议**: ICCV 2021

### NAS-OoD: Neural Architecture Search for Out-of-Distribution Generalization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00821) · 📚 47 citations
- **作者**: Haoyue Bai, Fengwei Zhou, Lanqing Hong, Nanyang Ye, S.-H. Gary Chan, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### BN-NAS: Neural Architecture Search with Batch Normalization.
- **链接**: [arXiv:2108.07375](https://arxiv.org/abs/2108.07375) · [出版页](https://doi.org/10.1109/ICCV48922.2021.00037) · 📚 37 citations
- **作者**: Boyu Chen, Peixia Li, Baopu Li, Chen Lin, Chuming Li, Ming Sun et al.
- **🏷️ 机构**: The University of Sydney
- **会议**: ICCV 2021

- **摘要（英，原文）**:

  > We present BN-NAS, neural architecture search with Batch Normalization (BN-NAS), to accelerate neural architecture search (NAS). BN-NAS can significantly reduce the time required by model training and evaluation in NAS. Specifically, for fast evaluation, we propose a BN-based indicator for predicting subnet performance at a very early training stage. The BN-based indicator further facilitates us to improve the training efficiency by only training the BN parameters during the supernet training. This is based on our observation that training the whole supernet is not necessary while training only BN parameters accelerates network convergence for network architecture search. Extensive experiments show that our method can significantly shorten the time of training supernet by more than 10 times and shorten the time of evaluating subnets by more than 600,000 times without losing accuracy.

### GLiT: Neural Architecture Search for Global and Local Image Transformer.
- **链接**: [arXiv:2107.02960](https://arxiv.org/abs/2107.02960) · [出版页](https://doi.org/10.1109/ICCV48922.2021.00008) · 📚 105 citations
- **作者**: Boyu Chen, Peixia Li, Chuming Li, Baopu Li, Lei Bai, Chen Lin et al.
- **🏷️ 机构**: The University of Sydney
- **会议**: ICCV 2021

- **摘要（英，原文）**:

  > We introduce the first Neural Architecture Search (NAS) method to find a better transformer architecture for image recognition. Recently, transformers without CNN-based backbones are found to achieve impressive performance for image recognition. However, the transformer is designed for NLP tasks and thus could be sub-optimal when directly used for image recognition. In order to improve the visual representation ability for transformers, we propose a new search space and searching algorithm. Specifically, we introduce a locality module that models the local correlations in images explicitly with fewer computational cost. With the locality module, our search space is defined to let the search algorithm freely trade off between global and local information as well as optimizing the low-level design choice in each module. To tackle the problem caused by huge search space, a hierarchical neural architecture search method is proposed to search the optimal vision transformer from two levels separately with the evolutionary algorithm. Extensive experiments on the ImageNet dataset demonstrate that our method can find more discriminative and efficient transformer variants than the ResNet family (e.g., ResNet101) and the baseline ViT for image classification.

### Not All Operations Contribute Equally: Hierarchical Operation-adaptive Predictor for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01034) · 📚 13 citations
- **作者**: Ziye Chen, Yibing Zhan, Baosheng Yu, Mingming Gong, Bo Du
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### FairNAS: Rethinking Evaluation Fairness of Weight Sharing Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01202) · 📚 370 citations
- **作者**: Xiangxiang Chu, Bo Zhang, Ruijun Xu
- **🏷️ 机构**: Alibaba, Xiaomi;Meituan
- **会议**: ICCV 2021

### CM-NAS: Cross-Modality Neural Architecture Search for Visible-Infrared Person Re-Identification.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01161) · 📚 159 citations
- **作者**: Chaoyou Fu, Yibo Hu, Xiang Wu, Hailin Shi, Tao Mei, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Pyramid Architecture Search for Real-Time Image Deblurring.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00426) · 📚 41 citations
- **作者**: Xiaobin Hu, Wenqi Ren, Kaicheng Yu, Kaihao Zhang, Xiaochun Cao, Wei Liu et al.
- **🏷️ 机构**: Westlake University, Unversity of Zurich
- **会议**: ICCV 2021

### BossNAS: Exploring Hybrid CNN-transformers with Block-wisely Self-supervised Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01206)
- **作者**: Changlin Li, Tao Tang, Guangrun Wang, Jiefeng Peng, Bing Wang, Xiaodan Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Pi-NAS: Improving Neural Architecture Search by Reducing Supernet Training Consistency Shift.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01213) · 📚 21 citations
- **作者**: Jiefeng Peng, Jiqi Zhang, Changlin Li, Guangrun Wang, Xiaodan Liang, Liang Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Once Quantization-Aware Training: High Performance Extremely Low-bit Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00529) · 📚 52 citations
- **作者**: Mingzhu Shen, Feng Liang, Ruihao Gong, Yuhang Li, Chuming Li, Chen Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### RANK-NOSH: Efficient Predictor-Based Architecture Search via Non-Uniform Successive Halving.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01021) · 📚 14 citations
- **作者**: Ruochen Wang, Xiangning Chen, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
- **🏷️ 机构**: Penn State
- **会议**: ICCV 2021

### Learning Latent Architectural Distribution in Differentiable Neural Architecture Search via Variational Information Maximization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01209) · 📚 9 citations
- **作者**: Yaoming Wang, Yuchen Liu, Wenrui Dai, Chenglin Li, Junni Zou, Hongkai Xiong
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### IDARTS: Interactive Differentiable Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00120) · 📚 10 citations
- **作者**: Song Xue, Runqi Wang, Baochang Zhang, Tian Wang, Guodong Guo, David S. Doermann
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### Neural Architecture Search for Joint Human Parsing and Pose Estimation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01119) · 📚 21 citations
- **作者**: Dan Zeng, Yuhang Huang, Qian Bao, Junjie Zhang, Chi Su, Wu Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

### AutoSpace: Neural Architecture Search with Less Human Interference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00039) · 📚 11 citations
- **作者**: Daquan Zhou, Xiaojie Jin, Xiaochen Lian, Linjie Yang, Yujing Xue, Qibin Hou et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
