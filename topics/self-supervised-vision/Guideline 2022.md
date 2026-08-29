# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 58 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Supervised Pretraining for Large-Scale Point Clouds.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/f670ef96387d9a5a8a51e2ed80cb148d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zaiwei Zhang, Min Bai, Li Erran Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Green Hierarchical Vision Transformer for Masked Image Modeling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7e487c72fce6e45879a78ee0872d991d-Abstract-Conference.html)
- **作者**: Lang Huang, Shan You, Mingkai Zheng, Fei Wang, Chen Qian, Toshihiko Yamasaki
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Adapting Self-Supervised Vision Transformers by Probing Attention-Conditioned Masking Consistency.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/93b4d708976a1d9b1250c400e7fda811-Abstract-Conference.html) · 📚 被引 0
- **作者**: Viraj Prabhu, Sriram Yenamandra, Aaditya Singh, Judy Hoffman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-supervised Heterogeneous Graph Pre-training Based on Structural Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/6c7297baffe5c85ea1d9e1ccb1222ab8-Abstract-Conference.html) · 📚 被引 4
- **作者**: Yaming Yang, Ziyu Guan, Zhe Wang, Wei Zhao, Cai Xu, Weigang Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### $\alpha$-ReQ : Assessing Representation Quality in Self-Supervised Learning by measuring eigenspectrum decay.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/70596d70542c51c8d9b4e423f4bf2736-Abstract-Conference.html) · 📚 被引 5
- **作者**: Kumar Krishna Agrawal, Arnab Kumar Mondal, Arna Ghosh, Blake A. Richards
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### RSA: Reducing Semantic Shift from Aggressive Augmentations for Self-supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/850e8063d902e0825d3c5504d183bafe-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yingbin Bai, Erkun Yang, Zhaoqing Wang, Yuxuan Du, Bo Han, Cheng Deng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Contrastive and Non-Contrastive Self-Supervised Learning Recover Global and Local Spectral Embedding Methods.
- **链接**: [arXiv:2205.11508](https://arxiv.org/abs/2205.11508) · 📚 被引 5
- **作者**: Randall Balestriero, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-Supervised Learning (SSL) surmises that inputs and pairwise positive relationships are enough to learn meaningful representations. Although SSL has recently reached a milestone: outperforming supervised methods in many modalities\dots the theoretical foundations are limited, method-specific, and fail to provide principled design guidelines to practitioners. In this paper, we propose a unifying framework under the helm of spectral manifold learning to address those limitations. Through the course of this study, we will rigorously demonstrate that VICReg, SimCLR, BarlowTwins et al. correspond to eponymous spectral methods such as Laplacian Eigenmaps, Multidimensional Scaling et al. This unification will then allow us to obtain (i) the closed-form optimal representation for each method, (ii) the closed-form optimal network parameters in the linear regime for each method, (iii) the impact of the pairwise relations used during training on each of those quantities and on downstream task performances, and most importantly, (iv) the first theoretical bridge between contrastive and non-contrastive methods towards global and local spectral embedding methods respectively, hinting at the benefits and limitations of each. For example, (i) if the pairwise relation is aligned with the downstream task, any SSL method can be employed successfully and will recover the supervised method, but in the low data regime, VICReg's invariance hyper-parameter should be high; (ii) if the pairwise relation is misaligned with the downstream task, VICReg with small invariance hyper-parameter should be preferred over SimCLR or BarlowTwins.

</details>

### VICRegL: Self-Supervised Learning of Local Visual Features.
- **链接**: [arXiv:2210.01571](https://arxiv.org/abs/2210.01571) · [代码](https://github.com/facebookresearch/VICRegL) · 📚 被引 23
- **作者**: Adrien Bardes, Jean Ponce, Yann LeCun
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most recent self-supervised methods for learning image representations focus on either producing a global feature with invariance properties, or producing a set of local features. The former works best for classification tasks while the latter is best for detection and segmentation tasks. This paper explores the fundamental trade-off between learning local and global features. A new method called VICRegL is proposed that learns good global and local features simultaneously, yielding excellent performance on detection and segmentation tasks while maintaining good performance on classification tasks. Concretely, two identical branches of a standard convolutional net architecture are fed two differently distorted versions of the same image. The VICReg criterion is applied to pairs of global feature vectors. Simultaneously, the VICReg criterion is applied to pairs of local feature vectors occurring before the last pooling layer. Two local feature vectors are attracted to each other if their l2-distance is below a threshold or if their relative locations are consistent with a known geometric transformation between the two input images. We demonstrate strong performance on linear classification and segmentation transfer tasks. Code and pretrained models are publicly available at: https://github.com/facebookresearch/VICRegL

</details>

### Self-Supervised Fair Representation Learning without Demographics.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/ad991bbc381626a8e44dc5414aa136a8-Abstract-Conference.html) · 📚 被引 2
- **作者**: Junyi Chai, Xiaoqian Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### S3GC: Scalable Self-Supervised Graph Clustering.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/15972a9575e0f03bf82f00aebeb40774-Abstract-Conference.html) · 📚 被引 9
- **作者**: Devvrit, Aditya Sinha, Inderjit S. Dhillon, Prateek Jain
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Improving Self-Supervised Learning by Characterizing Idealized Representations.
- **链接**: [arXiv:2209.06235](https://arxiv.org/abs/2209.06235) · 📚 被引 1
- **作者**: Yann Dubois, Stefano Ermon, Tatsunori B. Hashimoto, Percy Liang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the empirical successes of self-supervised learning (SSL) methods, it is unclear what characteristics of their representations lead to high downstream accuracies. In this work, we characterize properties that SSL representations should ideally satisfy. Specifically, we prove necessary and sufficient conditions such that for any task invariant to given data augmentations, desired probes (e.g., linear or MLP) trained on that representation attain perfect accuracy. These requirements lead to a unifying conceptual framework for improving existing SSL methods and deriving new ones. For contrastive learning, our framework prescribes simple but significant improvements to previous methods such as using asymmetric projection heads. For non-contrastive learning, we use our framework to derive a simple and novel objective. Our resulting SSL algorithms outperform baselines on standard benchmarks, including SwAV+multicrops on linear probing of ImageNet.

</details>

### Dataset Inference for Self-Supervised Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/4ebf0617b32da2cd083c3b17c7285cce-Abstract-Conference.html) · 📚 被引 7
- **作者**: Adam Dziedzic, Haonan Duan, Muhammad Ahmad Kaleem, Nikita Dhawan, Jonas Guan, Yannis Cattan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Losses Can Be Blessings: Routing Self-Supervised Speech Representations Towards Efficient Multilingual and Multitask Speech Processing.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/83d349b6eb8125588b5f091e2d47525c-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yonggan Fu, Yang Zhang, Kaizhi Qian, Zhifan Ye, Zhongzhi Yu, Cheng-I Jeff Lai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Efficient Multi-agent Communication via Self-supervised Information Aggregation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/075b2875e2b671ddd74aeec0ac9f0357-Abstract-Conference.html) · 📚 被引 3
- **作者**: Cong Guan, Feng Chen, Lei Yuan, Chenghe Wang, Hao Yin, Zongzhang Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### AutoLink: Self-supervised Learning of Human Skeletons and Object Outlines by Linking Keypoints.
- **链接**: [arXiv:2205.10636](https://arxiv.org/abs/2205.10636) · 📚 被引 2
- **作者**: Xingzhe He, Bastian Wandt, Helge Rhodin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Graph Self-supervised Learning with Accurate Discrepancy Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5b175f9e93873e3a10a6ce43dbb82e05-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dongki Kim, Jinheon Baek, Sung Ju Hwang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### HierSpeech: Bridging the Gap between Text and Speech by Hierarchical Variational Inference using Self-supervised Representations for Speech Synthesis.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/69c754f571806bf15add18556ff39b4f-Abstract-Conference.html) · 📚 被引 2
- **作者**: Sang-Hoon Lee, Seung-Bin Kim, Ji-Hyun Lee, Eunwoo Song, Min-Jae Hwang, Seong-Whan Lee
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### MetaMask: Revisiting Dimensional Confounder for Self-Supervised Learning.
- **链接**: [arXiv:2209.07902](https://arxiv.org/abs/2209.07902) · 📚 被引 2
- **作者**: Jiangmeng Li, Wenwen Qiang, Yanan Zhang, Wenyi Mo, Changwen Zheng, Bing Su et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Does Self-supervised Learning Really Improve Reinforcement Learning from Pixels?
- **链接**: [arXiv:2206.05266](https://arxiv.org/abs/2206.05266) · 📚 被引 3
- **作者**: Xiang Li, Jinghuan Shang, Srijan Das, Michael S. Ryoo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Bridging the Gap from Asymmetry Tricks to Decorrelation Principles in Non-contrastive Self-supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7d535a224c8ae54ba75bac0457b6b279-Abstract-Conference.html) · 📚 被引 2
- **作者**: Kang-Jun Liu, Masanori Suganuma, Takayuki Okatani
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-Supervised Learning via Maximum Entropy Coding.
- **链接**: [arXiv:2210.11464](https://arxiv.org/abs/2210.11464) · 📚 被引 9
- **作者**: Xin Liu, Zhongdao Wang, Yali Li, Shengjin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Toward a realistic model of speech processing in the brain with self-supervised learning.
- **链接**: [arXiv:2206.01685](https://arxiv.org/abs/2206.01685) · 📚 被引 8
- **作者**: Juliette Millet, Charlotte Caucheteux, Pierre Orhan, Yves Boubenec, Alexandre Gramfort, Ewan Dunbar et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-Supervised Learning with an Information Maximization Criterion.
- **链接**: [arXiv:2209.07999](https://arxiv.org/abs/2209.07999) · 📚 被引 0
- **作者**: Serdar Ozsoy, Shadi Hamdan, Sercan Ö. Arik, Deniz Yuret, Alper T. Erdogan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-Supervised Learning Through Efference Copies.
- **链接**: [arXiv:2210.09224](https://arxiv.org/abs/2210.09224) · 📚 被引 2
- **作者**: Franz Scherr, Qinghai Guo, Timoleon Moraitis
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-Supervised Learning of Brain Dynamics from Broad Neuroimaging Data.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/8600a9df1a087a9a66900cc8c948c3f0-Abstract-Conference.html) · 📚 被引 3
- **作者**: Armin W. Thomas, Christopher Ré, Russell A. Poldrack
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training.
- **链接**: [arXiv:2203.12602](https://arxiv.org/abs/2203.12602) · 📚 被引 264
- **作者**: Zhan Tong, Yibing Song, Jue Wang, Limin Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### CroCo: Self-Supervised Pre-training for 3D Vision Tasks by Cross-View Completion.
- **链接**: [arXiv:2210.10716](https://arxiv.org/abs/2210.10716) · 📚 被引 9
- **作者**: Philippe Weinzaepfel, Vincent Leroy, Thomas Lucas, Romain Brégier, Yohann Cabon, Vaibhav Arora et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### The Mechanism of Prediction Head in Non-contrastive Self-supervised Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9d276b0a087efdd2404f3295b26c24c1-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zixin Wen, Yuanzhi Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-Supervised Visual Representation Learning with Semantic Grouping.
- **链接**: [arXiv:2205.15288](https://arxiv.org/abs/2205.15288) · 📚 被引 4
- **作者**: Xin Wen, Bingchen Zhao, Anlin Zheng, Xiangyu Zhang, Xiaojuan Qi
- **🏷️ 机构**: MEGVII
- **会议**: NeurIPS 2022

### An Investigation into Whitening Loss for Self-supervised Learning.
- **链接**: [arXiv:2210.03586](https://arxiv.org/abs/2210.03586)
- **作者**: Xi Weng, Lei Huang, Lei Zhao, Rao Muhammad Anwer, Salman H. Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### D2NeRF: Self-Supervised Decoupling of Dynamic and Static Objects from a Monocular Video.
- **链接**: [arXiv:2205.15838](https://arxiv.org/abs/2205.15838) · 📚 被引 12
- **作者**: Tianhao Wu, Fangcheng Zhong, Andrea Tagliasacchi, Forrester Cole, Cengiz Öztireli
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Decoupled Self-supervised Learning for Graphs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/040c816286b3844fd78f2124eec75f2e-Abstract-Conference.html) · 📚 被引 1
- **作者**: Teng Xiao, Zhengyu Chen, Zhimeng Guo, Zeyang Zhuang, Suhang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-supervised Amodal Video Object Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/29171e32e652ac40244e96bb8529cb44-Abstract-Conference.html) · 📚 被引 2
- **作者**: Jian Yao, Yuxin Hong, Chiyu Wang, Tianjun Xiao, Tong He, Francesco Locatello et al.
- **🏷️ 机构**: Wuhan University, Fudan / Shanghai AI Lab
- **会议**: NeurIPS 2022

### Self-Supervised Aggregation of Diverse Experts for Test-Agnostic Long-Tailed Recognition.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/dc6319dde4fb182b22fb902da9418566-Abstract-Conference.html) · 📚 被引 16
- **作者**: Yifan Zhang, Bryan Hooi, Lanqing Hong, Jiashi Feng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-Supervised Image Restoration with Blurry and Noisy Pairs.
- **链接**: [arXiv:2211.07317](https://arxiv.org/abs/2211.07317) · 📚 被引 3
- **作者**: Zhilu Zhang, Rongjian Xu, Ming Liu, Zifei Yan, Wangmeng Zuo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Self-Supervised Contrastive Pre-Training For Time Series via Time-Frequency Consistency.
- **链接**: [arXiv:2206.08496](https://arxiv.org/abs/2206.08496) · 📚 被引 74
- **作者**: Xiang Zhang, Ziyuan Zhao, Theodoros Tsiligkaridis, Marinka Zitnik
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Contrastive Learning as Goal-Conditioned Reinforcement Learning.
- **链接**: [arXiv:2206.07568](https://arxiv.org/abs/2206.07568) · 📚 被引 18
- **作者**: Benjamin Eysenbach, Tianjun Zhang, Sergey Levine, Ruslan Salakhutdinov
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Federated Learning from Pre-Trained Models: A Contrastive Learning Approach.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7aa320d2b4b8f6400b18f6f77b6c1535-Abstract-Conference.html) · 📚 被引 31
- **作者**: Yue Tan, Guodong Long, Jie Ma, Lu Liu, Tianyi Zhou, Jing Jiang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### An Empirical Study on Disentanglement of Negative-free Contrastive Learning.
- **链接**: [arXiv:2206.04756](https://arxiv.org/abs/2206.04756) · 📚 被引 1
- **作者**: Jinkun Cao, Ruiqian Nai, Qing Yang, Jialei Huang, Yang Gao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### TreeMoCo: Contrastive Neuron Morphology Representation Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/9f989633ffbd47a83caddacad0f0261f-Abstract-Conference.html) · 📚 被引 4
- **作者**: Hanbo Chen, Jiawei Yang, Daniel Maxim Iascone, Lijuan Liu, Lei He, Hanchuan Peng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Why do We Need Large Batchsizes in Contrastive Learning? A Gradient-Bias Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/db174d373133dcc6bf83bc98e4b681f8-Abstract-Conference.html) · 📚 被引 14
- **作者**: Changyou Chen, Jianyi Zhang, Yi Xu, Liqun Chen, Jiali Duan, Yiran Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Non-Linguistic Supervision for Contrastive Learning of Sentence Embeddings.
- **链接**: [arXiv:2209.09433](https://arxiv.org/abs/2209.09433) · 📚 被引 1
- **作者**: Yiren Jian, Chongyang Gao, Soroush Vosoughi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Expectation-Maximization Contrastive Learning for Compact Video-and-Language Representations.
- **链接**: [arXiv:2211.11427](https://arxiv.org/abs/2211.11427) · 📚 被引 11
- **作者**: Peng Jin, Jinfa Huang, Fenglin Liu, Xian Wu, Shen Ge, Guoli Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Energy-Based Contrastive Learning of Visual Representations.
- **链接**: [arXiv:2202.04933](https://arxiv.org/abs/2202.04933) · 📚 被引 0
- **作者**: Beomsu Kim, Jong Chul Ye
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Optimal Positive Generation via Latent Transformation for Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/74a31a3b862eb7f01defbbed8e5f0c69-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yinqi Li, Hong Chang, Bingpeng Ma, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Revisiting Graph Contrastive Learning from the Perspective of Graph Spectrum.
- **链接**: [arXiv:2210.02330](https://arxiv.org/abs/2210.02330) · 📚 被引 6
- **作者**: Nian Liu, Xiao Wang, Deyu Bo, Chuan Shi, Jian Pei
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Co-Modality Graph Contrastive Learning for Imbalanced Node Classification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/65cbe3e21ac62553111d9ecf7d60c18e-Abstract-Conference.html) · 📚 被引 4
- **作者**: Yiyue Qian, Chunhui Zhang, Yiming Zhang, Qianlong Wen, Yanfang Ye, Chuxu Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Understanding Deep Contrastive Learning via Coordinate-wise Optimization.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/7b5c9cc08960df40615c1d858961eb8b-Abstract-Conference.html) · 📚 被引 2
- **作者**: Yuandong Tian
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Analyzing Data-Centric Properties for Graph Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/5adac7be735715604e8a4b0b2924a7e4-Abstract-Conference.html) · 📚 被引 0
- **作者**: Puja Trivedi, Ekdeep Singh Lubana, Mark Heimann, Danai Koutra, Jayaraman J. Thiagarajan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Uncovering the Structural Fairness in Graph Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/d13565c82d1e44eda2da3bd00b35ca11-Abstract-Conference.html) · 📚 被引 4
- **作者**: Ruijia Wang, Xiao Wang, Chuan Shi, Le Song
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### SCL-WC: Cross-Slide Contrastive Learning for Weakly-Supervised Whole-Slide Image Classification.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/726204cea3ec27790a644e5b379175e3-Abstract-Conference.html) · 📚 被引 7
- **作者**: Xiyue Wang, Jinxi Xiang, Jun Zhang, Sen Yang, Zhongyi Yang, Ming-Hui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Augmentations in Hypergraph Contrastive Learning: Fabricated and Generative.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/0cd1eec0eeaf5ce1bf6d8875a7c1d095-Abstract-Conference.html) · 📚 被引 6
- **作者**: Tianxin Wei, Yuning You, Tianlong Chen, Yang Shen, Jingrui He, Zhangyang Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Divide and Contrast: Source-free Domain Adaptation via Adaptive Contrastive Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html) · 📚 被引 14
- **作者**: Ziyi Zhang, Weikai Chen, Hui Cheng, Zhen Li, Siyuan Li, Liang Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Rethinking and Scaling Up Graph Contrastive Learning: An Extremely Efficient Approach with Group Discrimination.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/46027e3de0db3617a911f1a647def3bf-Abstract-Conference.html) · 📚 被引 3
- **作者**: Yizhen Zheng, Shirui Pan, Vincent C. S. Lee, Yu Zheng, Philip S. Yu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

## 跨领域论文（完整笔记在其他领域）

- ElasticMVS: Learning elastic part representation for self-supervised multi-view stereopsis. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Multimodal Contrastive Learning with LIMoE: the Language-Image Mixture of Experts. → [multimodal](../multimodal/Guideline%202022.md)
- Long-Form Video-Language Pre-Training with Multimodal Temporal Contrastive Learning. → [multimodal](../multimodal/Guideline%202022.md)
- Self-supervised surround-view depth estimation with volumetric feature fusion. → [bev](../bev/Guideline%202022.md)
