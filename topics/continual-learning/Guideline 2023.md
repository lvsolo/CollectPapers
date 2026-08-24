# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Fairness Continual Learning Approach to Semantic Scene Understanding in Open-World Environments.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/ce3cf998b7f59271e80ce03fb74a7115-Abstract-Conference.html) · 📚 23 citations
- **作者**: Thanh-Dat Truong, Hoang-Quan Nguyen, Bhiksha Raj, Khoa Luu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Augmented Memory Replay-based Continual Learning Approaches for Network Intrusion Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/3755a02b1035fbadd5f93a022170e46f-Abstract-Conference.html)
- **作者**: Suresh Kumar Amalapuram, Sumohana S. Channappayya, Bheemarjuna Reddy Tamma
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### FeCAM: Exploiting the Heterogeneity of Class Distributions in Exemplar-Free Continual Learning.
- **链接**: [arXiv:2309.14062](https://arxiv.org/abs/2309.14062) · [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/15294ba2dcfb4521274f7aa1c26f4dd4-Abstract-Conference.html) · [代码](https://github.com/dipamgoswami/FeCAM) · 📚 126 citations
- **作者**: Dipam Goswami, Yuyang Liu, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: Computer Vision Center Barcelona, Universitat Autonoma de Barcelona
- **会议**: NeurIPS 2023

- **摘要（英，原文）**:

  > Exemplar-free class-incremental learning (CIL) poses several challenges since it prohibits the rehearsal of data from previous tasks and thus suffers from catastrophic forgetting. Recent approaches to incrementally learning the classifier by freezing the feature extractor after the first task have gained much attention. In this paper, we explore prototypical networks for CIL, which generate new class prototypes using the frozen feature extractor and classify the features based on the Euclidean distance to the prototypes. In an analysis of the feature distributions of classes, we show that classification based on Euclidean metrics is successful for jointly trained features. However, when learning from non-stationary data, we observe that the Euclidean metric is suboptimal and that feature distributions are heterogeneous. To address this challenge, we revisit the anisotropic Mahalanobis distance for CIL. In addition, we empirically show that modeling the feature covariance relations is better than previous attempts at sampling features from normal distributions and training a linear classifier. Unlike existing methods, our approach generalizes to both many- and few-shot CIL settings, as well as to domain-incremental settings. Interestingly, without updating the backbone network, our method obtains state-of-the-art results on several standard continual learning benchmarks. Code is available at https://github.com/dipamgoswami/FeCAM.

### Bilevel Coreset Selection in Continual Learning: A New Formulation and Algorithm.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a0251e494a7e75d59e06d37e646f46b7-Abstract-Conference.html) · 📚 43 citations
- **作者**: Jie Hao, Kaiyi Ji, Mingrui Liu
- **🏷️ 机构**: George Mason University, University of Electronic Science and Technology of China
- **会议**: NeurIPS 2023

### Selective Amnesia: A Continual Learning Approach to Forgetting in Deep Generative Models.
- **链接**: [arXiv:2305.10120](https://arxiv.org/abs/2305.10120) · [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/376276a95781fa17c177b1ccdd0a03ac-Abstract-Conference.html) · [代码](https://github.com/clear-nus/selective-amnesia) · 📚 210 citations
- **作者**: Alvin Heng, Harold Soh
- **🏷️ 机构**: National University of Singapore
- **会议**: NeurIPS 2023

- **摘要（英，原文）**:

  > The recent proliferation of large-scale text-to-image models has led to growing concerns that such models may be misused to generate harmful, misleading, and inappropriate content. Motivated by this issue, we derive a technique inspired by continual learning to selectively forget concepts in pretrained deep generative models. Our method, dubbed Selective Amnesia, enables controllable forgetting where a user can specify how a concept should be forgotten. Selective Amnesia can be applied to conditional variational likelihood models, which encompass a variety of popular deep generative frameworks, including variational autoencoders and large-scale text-to-image diffusion models. Experiments across different models demonstrate that our approach induces forgetting on a variety of concepts, from entire classes in standard datasets to celebrity and nudity prompts in text-to-image models. Our code is publicly available at https://github.com/clear-nus/selective-amnesia.

### NPCL: Neural Processes for Uncertainty-Aware Continual Learning.
- **链接**: [arXiv:2310.19272](https://arxiv.org/abs/2310.19272) · [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6c4a1a3cbe70ef36d7d6332166bba77d-Abstract-Conference.html) · [代码](https://github.com/srvCodes/NPCL) · 📚 26 citations
- **作者**: Saurav Jha, Dong Gong, He Zhao, Lina Yao
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

- **摘要（英，原文）**:

  > Continual learning (CL) aims to train deep neural networks efficiently on streaming data while limiting the forgetting caused by new tasks. However, learning transferable knowledge with less interference between tasks is difficult, and real-world deployment of CL models is limited by their inability to measure predictive uncertainties. To address these issues, we propose handling CL tasks with neural processes (NPs), a class of meta-learners that encode different tasks into probabilistic distributions over functions all while providing reliable uncertainty estimates. Specifically, we propose an NP-based CL approach (NPCL) with task-specific modules arranged in a hierarchical latent variable model. We tailor regularizers on the learned latent distributions to alleviate forgetting. The uncertainty estimation capabilities of the NPCL can also be used to handle the task head/module inference challenge in CL. Our experiments show that the NPCL outperforms previous CL approaches. We validate the effectiveness of uncertainty estimation in the NPCL for identifying novel data and evaluating instance-level model confidence. Code is available at \url{https://github.com/srvCodes/NPCL}.

### CLeAR: Continual Learning on Algorithmic Reasoning for Human-like Intelligence.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/986e0caad271b59417287737416d8594-Abstract-Conference.html)
- **作者**: Bong Gyun Kang, HyunGi Kim, Dahuin Jung, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Recasting Continual Learning as Sequence Modeling.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/dee254cdacbab59f17dc6a8fbdffa59f-Abstract-Conference.html) · 📚 14 citations
- **作者**: Soochan Lee, Jaehyeon Son, Gunhee Kim
- **🏷️ 机构**: Seoul National University, Georgia Institute of Technology
- **会议**: NeurIPS 2023

### Loss Decoupling for Task-Agnostic Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/249f73e01f0a2bb6c8d971b565f159a7-Abstract-Conference.html) · 📚 59 citations
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Does Continual Learning Meet Compositionality? New Benchmarks and An Evaluation Framework.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6a42b45af2b72e6e5b5e3a6fe695809f-Abstract-Datasets_and_Benchmarks.html) · 📚 7 citations
- **作者**: Weiduo Liao, Ying Wei, Mingchen Jiang, Qingfu Zhang, Hisao Ishibuchi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Overcoming Recency Bias of Normalization Statistics in Continual Learning: Balance and Adaptation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/50ca96a1a9ebe0b5e5688a504feb6107-Abstract-Conference.html)
- **作者**: Yilin Lyu, Liyuan Wang, Xingxing Zhang, Zicheng Sun, Hang Su, Jun Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### RanPAC: Random Projections and Pre-trained Models for Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/2793dc35e14003dd367684d93d236847-Abstract-Conference.html) · 📚 231 citations
- **作者**: Mark D. McDonnell, Dong Gong, Amin Parvaneh, Ehsan Abbasnejad, Anton van den Hengel
- **🏷️ 机构**: University of Adelaide, Commonwealth Bank of Australia
- **会议**: NeurIPS 2023

### Continual Learning for Instruction Following from Realtime Feedback.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/666cccc6376058e251315b4de7e085b9-Abstract-Conference.html)
- **作者**: Alane Suhr, Yoav Artzi
- **🏷️ 机构**: University of California Berkeley, Cornell University
- **会议**: NeurIPS 2023

### Temporal Continual Learning with Prior Compensation for Human Motion Prediction.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/cf7a83a5342befd11d3d65beba1be5b0-Abstract-Conference.html) · 📚 6 citations
- **作者**: Jianwei Tang, Jiangxin Sun, Xiaotong Lin, Lifang Zhang, Wei-Shi Zheng, Jian-Fang Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Hierarchical Decomposition of Prompt-Based Continual Learning: Rethinking Obscured Sub-optimality.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/d9f8b5abc8e0926539ecbb492af7b2f1-Abstract-Conference.html) · 📚 176 citations
- **作者**: Liyuan Wang, Jingyi Xie, Xingxing Zhang, Mingyi Huang, Hang Su, Jun Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CL-NeRF: Continual Learning of Neural Radiance Fields for Evolving Scene Representation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/6c7154e394e24c69409256ccf8bf0804-Abstract-Conference.html)
- **作者**: Xiuzhe Wu, Peng Dai, Weipeng Deng, Handi Chen, Yang Wu, Yan-Pei Cao et al.
- **🏷️ 机构**: Stanford University, The University of Hong Kong, Tongji University, The University of Hong Kong
- **会议**: NeurIPS 2023

### An Efficient Dataset Condensation Plugin and Its Application to Continual Learning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/d5f34e7e70d80f5037ab16a48e2d186e-Abstract-Conference.html) · 📚 47 citations
- **作者**: Enneng Yang, Li Shen, Zhenyi Wang, Tongliang Liu, Guibing Guo
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### A Data-Free Approach to Mitigate Catastrophic Forgetting in Federated Class Incremental Learning for Vision Tasks.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/d160ea01902c33e30660851dfbac5980-Abstract-Conference.html) · 📚 96 citations
- **作者**: Sara Babakniya, Zalan Fabian, Chaoyang He, Mahdi Soltanolkotabi, Salman Avestimehr
- **🏷️ 机构**: University of Southern California
- **会议**: NeurIPS 2023

### Enhancing Knowledge Transfer for Task Incremental Learning with Data-free Subnetwork.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/d7b3cef7c31b94a4a533db83d01a8882-Abstract-Conference.html)
- **作者**: Qiang Gao, Xiaojun Shan, Yuchen Zhang, Fan Zhou
- **🏷️ 机构**: Peking University
- **会议**: NeurIPS 2023

### A Unified Approach to Domain Incremental Learning with Memory: Theory and Algorithm.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/30d046e94d7b8037d6ef27c4357a8dd4-Abstract-Conference.html) · 📚 57 citations
- **作者**: Haizhou Shi, Hao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Few-Shot Class-Incremental Learning via Training-Free Prototype Calibration.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/30dfe47a3ccbee68cffa0c19ccb1bc00-Abstract-Conference.html) · 📚 130 citations
- **作者**: Qi-Wei Wang, Da-Wei Zhou, Yi-Kai Zhang, De-Chuan Zhan, Han-Jia Ye
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
