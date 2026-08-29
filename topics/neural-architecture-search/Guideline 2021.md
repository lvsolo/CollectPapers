# Neural Architecture Search — 2021 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

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
- **链接**: [arXiv:2011.10904](https://arxiv.org/abs/2011.10904)
- **作者**: Yuanzheng Ci, Chen Lin, Ming Sun, Boyu Chen, Hongwen Zhang, Wanli Ouyang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The automation of neural architecture design has been a coveted alternative to human experts. Recent works have small search space, which is easier to optimize but has a limited upper bound of the optimal solution. Extra human design is needed for those methods to propose a more suitable space with respect to the specific task and algorithm capacity. To further enhance the degree of automation for neural architecture search, we present a Neural Search-space Evolution (NSE) scheme that iteratively amplifies the results from the previous effort by maintaining an optimized search space subset. This design minimizes the necessity of a well-designed search space. We further extend the flexibility of obtainable architectures by introducing a learnable multi-branch setting. By employing the proposed method, a consistent performance gain is achieved during a progressive search over upcoming search spaces. We achieve 77.3% top-1 retrain accuracy on ImageNet with 333M FLOPs, which yielded a state-of-the-art performance among previous auto-generated architectures that do not involve knowledge distillation or weight pruning. When the latency constraint is adopted, our result also performs better than the previous best-performing mobile models with a 77.9% Top-1 retrain accuracy.

</details>

### NAS-OoD: Neural Architecture Search for Out-of-Distribution Generalization.
- **链接**: [arXiv:2109.02038](https://arxiv.org/abs/2109.02038) · 📚 被引 27
- **作者**: Haoyue Bai, Fengwei Zhou, Lanqing Hong, Nanyang Ye, S.-H. Gary Chan, Zhenguo Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Huawei Noah&#x2019;s Ark Lab, Shanghai Jiao Tong University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances on Out-of-Distribution (OoD) generalization reveal the robustness of deep learning models against distribution shifts. However, existing works focus on OoD algorithms, such as invariant risk minimization, domain generalization, or stable learning, without considering the influence of deep model architectures on OoD generalization, which may lead to sub-optimal performance. Neural Architecture Search (NAS) methods search for architecture based on its performance on the training data, which may result in poor generalization for OoD tasks. In this work, we propose robust Neural Architecture Search for OoD generalization (NAS-OoD), which optimizes the architecture with respect to its performance on generated OoD data by gradient descent. Specifically, a data generator is learned to synthesize OoD data by maximizing losses computed by different neural architectures, while the goal for architecture search is to find the optimal architecture parameters that minimize the synthetic OoD data losses. The data generator and the neural architecture are jointly optimized in an end-to-end manner, and the minimax training process effectively discovers robust architectures that generalize well for different distribution shifts. Extensive experimental results show that NAS-OoD achieves superior performance on various OoD generalization benchmarks with deep models having a much fewer number of parameters. In addition, on a real industry dataset, the proposed NAS-OoD method reduces the error rate by more than 70% compared with the state-of-the-art method, demonstrating the proposed method's practicality for real applications.

</details>

### BN-NAS: Neural Architecture Search with Batch Normalization.
- **链接**: [arXiv:2108.07375](https://arxiv.org/abs/2108.07375) · 📚 被引 30
- **作者**: Boyu Chen, Peixia Li, Baopu Li, Chen Lin, Chuming Li, Ming Sun et al.
- **🏷️ 机构**: The University of Sydney, Baidu USA LLC, University of Oxford
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present BN-NAS, neural architecture search with Batch Normalization (BN-NAS), to accelerate neural architecture search (NAS). BN-NAS can significantly reduce the time required by model training and evaluation in NAS. Specifically, for fast evaluation, we propose a BN-based indicator for predicting subnet performance at a very early training stage. The BN-based indicator further facilitates us to improve the training efficiency by only training the BN parameters during the supernet training. This is based on our observation that training the whole supernet is not necessary while training only BN parameters accelerates network convergence for network architecture search. Extensive experiments show that our method can significantly shorten the time of training supernet by more than 10 times and shorten the time of evaluating subnets by more than 600,000 times without losing accuracy.

</details>

### GLiT: Neural Architecture Search for Global and Local Image Transformer.
- **链接**: [arXiv:2107.02960](https://arxiv.org/abs/2107.02960) · 📚 被引 85
- **作者**: Boyu Chen, Peixia Li, Chuming Li, Baopu Li, Lei Bai, Chen Lin et al.
- **🏷️ 机构**: The University of Sydney, BAIDU USA LLC, University of Oxford
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the first Neural Architecture Search (NAS) method to find a better transformer architecture for image recognition. Recently, transformers without CNN-based backbones are found to achieve impressive performance for image recognition. However, the transformer is designed for NLP tasks and thus could be sub-optimal when directly used for image recognition. In order to improve the visual representation ability for transformers, we propose a new search space and searching algorithm. Specifically, we introduce a locality module that models the local correlations in images explicitly with fewer computational cost. With the locality module, our search space is defined to let the search algorithm freely trade off between global and local information as well as optimizing the low-level design choice in each module. To tackle the problem caused by huge search space, a hierarchical neural architecture search method is proposed to search the optimal vision transformer from two levels separately with the evolutionary algorithm. Extensive experiments on the ImageNet dataset demonstrate that our method can find more discriminative and efficient transformer variants than the ResNet family (e.g., ResNet101) and the baseline ViT for image classification.

</details>

### Not All Operations Contribute Equally: Hierarchical Operation-adaptive Predictor for Neural Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01034) · 📚 被引 11
- **作者**: Ziye Chen, Yibing Zhan, Baosheng Yu, Mingming Gong, Bo Du
- **🏷️ 机构**: Wuhan University,National Engineering Research Center for Multimedia Software, Institute of Artificial Intelligence, Hubei Key Laboratory of Multimedia and Network Communication Engineering, School of Computer Science,Wuhan,China, JD Explore Academy,China, The University of Sydney,Australia
- **会议**: ICCV 2021

### FairNAS: Rethinking Evaluation Fairness of Weight Sharing Neural Architecture Search.
- **链接**: [arXiv:1907.01845](https://arxiv.org/abs/1907.01845) · [代码](https://github.com/fairnas/FairNAS) · 📚 被引 182
- **作者**: Xiangxiang Chu, Bo Zhang, Ruijun Xu
- **🏷️ 机构**: Xiaomi AI Lab.
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> One of the most critical problems in weight-sharing neural architecture search is the evaluation of candidate models within a predefined search space. In practice, a one-shot supernet is trained to serve as an evaluator. A faithful ranking certainly leads to more accurate searching results. However, current methods are prone to making misjudgments. In this paper, we prove that their biased evaluation is due to inherent unfairness in the supernet training. In view of this, we propose two levels of constraints: expectation fairness and strict fairness. Particularly, strict fairness ensures equal optimization opportunities for all choice blocks throughout the training, which neither overestimates nor underestimates their capacity. We demonstrate that this is crucial for improving the confidence of models' ranking. Incorporating the one-shot supernet trained under the proposed fairness constraints with a multi-objective evolutionary search algorithm, we obtain various state-of-the-art models, e.g., FairNAS-A attains 77.5% top-1 validation accuracy on ImageNet. The models and their evaluation codes are made publicly available online http://github.com/fairnas/FairNAS .

</details>

### CM-NAS: Cross-Modality Neural Architecture Search for Visible-Infrared Person Re-Identification.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01161) · 📚 被引 164
- **作者**: Chaoyou Fu, Yibo Hu, Xiang Wu, Hailin Shi, Tao Mei, Ran He
- **🏷️ 机构**: University of Chinese Academy of Sciences,School of Artificial Intelligence, JD AI Research, CASIA,NLPR &amp; CEBSIT &amp; CRIPAC
- **会议**: ICCV 2021

### Pyramid Architecture Search for Real-Time Image Deblurring.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00426) · 📚 被引 38
- **作者**: Xiaobin Hu, Wenqi Ren, Kaicheng Yu, Kaihao Zhang, Xiaochun Cao, Wei Liu et al.
- **🏷️ 机构**: TU M&#x00FC;nchen,Informatics, CAS,SKLOIS, IIE, EPFL,CVLab
- **会议**: ICCV 2021

### Pi-NAS: Improving Neural Architecture Search by Reducing Supernet Training Consistency Shift.
- **链接**: [arXiv:2108.09671](https://arxiv.org/abs/2108.09671) · [代码](https://github.com/Ernie1/Pi-NAS) · 📚 被引 12
- **作者**: Jiefeng Peng, Jiqi Zhang, Changlin Li, Guangrun Wang, Xiaodan Liang, Liang Lin
- **🏷️ 机构**: Sun Yat-sen University, Monash University,GORSE Lab,Dept. of DSAI, University of Oxford
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently proposed neural architecture search (NAS) methods co-train billions of architectures in a supernet and estimate their potential accuracy using the network weights detached from the supernet. However, the ranking correlation between the architectures' predicted accuracy and their actual capability is incorrect, which causes the existing NAS methods' dilemma. We attribute this ranking correlation problem to the supernet training consistency shift, including feature shift and parameter shift. Feature shift is identified as dynamic input distributions of a hidden layer due to random path sampling. The input distribution dynamic affects the loss descent and finally affects architecture ranking. Parameter shift is identified as contradictory parameter updates for a shared layer lay in different paths in different training steps. The rapidly-changing parameter could not preserve architecture ranking. We address these two shifts simultaneously using a nontrivial supernet-Pi model, called Pi-NAS. Specifically, we employ a supernet-Pi model that contains cross-path learning to reduce the feature consistency shift between different paths. Meanwhile, we adopt a novel nontrivial mean teacher containing negative samples to overcome parameter shift and model collision. Furthermore, our Pi-NAS runs in an unsupervised manner, which can search for more transferable architectures. Extensive experiments on ImageNet and a wide range of downstream tasks (e.g., COCO 2017, ADE20K, and Cityscapes) demonstrate the effectiveness and universality of our Pi-NAS compared to supervised NAS. See Codes: https://github.com/Ernie1/Pi-NAS.

</details>

### Once Quantization-Aware Training: High Performance Extremely Low-bit Architecture Search.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00529) · 📚 被引 35
- **作者**: Mingzhu Shen, Feng Liang, Ruihao Gong, Yuhang Li, Chuming Li, Chen Lin et al.
- **🏷️ 机构**: Sensetime Research, University of Oxford
- **会议**: ICCV 2021

### RANK-NOSH: Efficient Predictor-Based Architecture Search via Non-Uniform Successive Halving.
- **链接**: [arXiv:2108.08019](https://arxiv.org/abs/2108.08019) · 📚 被引 5
- **作者**: Ruochen Wang, Xiangning Chen, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
- **🏷️ 机构**: UCLA,Department of Computer Science, DiDi AI Labs
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Predictor-based algorithms have achieved remarkable performance in the Neural Architecture Search (NAS) tasks. However, these methods suffer from high computation costs, as training the performance predictor usually requires training and evaluating hundreds of architectures from scratch. Previous works along this line mainly focus on reducing the number of architectures required to fit the predictor. In this work, we tackle this challenge from a different perspective - improve search efficiency by cutting down the computation budget of architecture training. We propose NOn-uniform Successive Halving (NOSH), a hierarchical scheduling algorithm that terminates the training of underperforming architectures early to avoid wasting budget. To effectively leverage the non-uniform supervision signals produced by NOSH, we formulate predictor-based architecture search as learning to rank with pairwise comparisons. The resulting method - RANK-NOSH, reduces the search budget by ~5x while achieving competitive or even better performance than previous state-of-the-art predictor-based methods on various spaces and datasets.

</details>

### Learning Latent Architectural Distribution in Differentiable Neural Architecture Search via Variational Information Maximization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01209) · 📚 被引 8
- **作者**: Yaoming Wang, Yuchen Liu, Wenrui Dai, Chenglin Li, Junni Zou, Hongkai Xiong
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering,China, Shanghai Jiao Tong University,Department of Computer Science &#x0026; Engineering,China
- **会议**: ICCV 2021

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

### AutoSpace: Neural Architecture Search with Less Human Interference.
- **链接**: [arXiv:2103.11833](https://arxiv.org/abs/2103.11833) · 📚 被引 6
- **作者**: Daquan Zhou, Xiaojie Jin, Xiaochen Lian, Linjie Yang, Yujing Xue, Qibin Hou et al.
- **🏷️ 机构**: National University of Singapore, ByteDance US AI Lab
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current neural architecture search (NAS) algorithms still require expert knowledge and effort to design a search space for network construction. In this paper, we consider automating the search space design to minimize human interference, which however faces two challenges: the explosive complexity of the exploration space and the expensive computation cost to evaluate the quality of different search spaces. To solve them, we propose a novel differentiable evolutionary framework named AutoSpace, which evolves the search space to an optimal one with following novel techniques: a differentiable fitness scoring function to efficiently evaluate the performance of cells and a reference architecture to speedup the evolution procedure and avoid falling into sub-optimal solutions. The framework is generic and compatible with additional computational constraints, making it feasible to learn specialized search spaces that fit different computational budgets. With the learned search space, the performance of recent NAS algorithms can be improved significantly compared with using previously manually designed spaces. Remarkably, the models generated from the new search space achieve 77.8% top-1 accuracy on ImageNet under the mobile setting (MAdds < 500M), out-performing previous SOTA EfficientNet-B0 by 0.7%. All codes will be made public.

</details>
