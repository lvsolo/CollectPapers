# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 29 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Alleviating Catastrophic Forgetting of Incremental Object Detection via Within-Class and Between-Class Knowledge Distillation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01732) · 📚 被引 18
- **作者**: Mengxue Kang, Jinpeng Zhang, Jinming Zhang, Xiashuang Wang, Yang Chen, Zhe Ma et al.
- **🏷️ 机构**: Intelligent Science &amp; Technology Academy of CASIC,Beijing,China,100043, Xinjiang University,Xinjiang,China,830046, The Second Academy of China Aerospace Science and Industry Corporation,Beijing,China,100854
- **会议**: ICCV 2023

### Label-Efficient Online Continual Object Detection in Streaming Video.
- **链接**: [arXiv:2206.00309](https://arxiv.org/abs/2206.00309) · [代码](https://github.com/showlab/Efficient-CLS) · 📚 被引 15
- **作者**: Jay Zhangjie Wu, David Junhao Zhang, Wynne Hsu, Mengmi Zhang, Mike Zheng Shou
- **🏷️ 机构**: Show Lab, National University of Singapore, Nanyang Technological University,School of Computer Science and Engineering,Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans can watch a continuous video stream and effortlessly perform continual acquisition and transfer of new knowledge with minimal supervision yet retaining previously learnt experiences. In contrast, existing continual learning (CL) methods require fully annotated labels to effectively learn from individual frames in a video stream. Here, we examine a more realistic and challenging problem$\unicode{x2014}$Label-Efficient Online Continual Object Detection (LEOCOD) in streaming video. We propose a plug-and-play module, Efficient-CLS, that can be easily inserted into and improve existing continual learners for object detection in video streams with reduced data annotation costs and model retraining time. We show that our method has achieved significant improvement with minimal forgetting across all supervision levels on two challenging CL benchmarks for streaming real-world videos. Remarkably, with only 25% annotated video frames, our method still outperforms the base CL learners, which are trained with 100% annotations on all video frames. The data and source code will be publicly available at https://github.com/showlab/Efficient-CLS.

</details>

</details>

### CODA-Prompt: COntinual Decomposed Attention-Based Prompting for Rehearsal-Free Continual Learning.
- **链接**: [arXiv:2211.13218](https://arxiv.org/abs/2211.13218) · [代码](https://github.com/GT-RIPL/CODA-Prompt) · 📚 被引 320
- **作者**: James Seale Smith, Leonid Karlinsky, Vyshnavi Gutta, Paola Cascante-Bonilla, Donghyun Kim, Assaf Arbelle et al.
- **🏷️ 机构**: Georgia Institute of Technology, MIT-IBM Watson AI Lab, IBM Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art rehearsal-free continual learning methods exploit the peculiarities of Vision Transformers to learn task-specific prompts, drastically reducing catastrophic forgetting. However, there is a tradeoff between the number of learned parameters and the performance, making such models computationally expensive. In this work, we aim to reduce this cost while maintaining competitive performance. We achieve this by revisiting and extending a simple transfer learning idea: learning task-specific normalization layers. Specifically, we tune the scale and bias parameters of LayerNorm for each continual learning task, selecting them at inference time based on the similarity between task-specific keys and the output of the pre-trained model. To make the classifier robust to incorrect selection of parameters during inference, we introduce a two-stage training procedure, where we first optimize the task-specific parameters and then train the classifier with the same selection procedure of the inference time. Experiments on ImageNet-R and CIFAR-100 show that our method achieves results that are either superior or on par with {the state of the art} while being computationally cheaper.

</details>

### Margin Contrastive Learning with Learnable-Vector for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00383) · 📚 被引 2
- **作者**: Kotaro Nagata, Kazuhiro Hotta
- **🏷️ 机构**: Meijo University,Electrical and Electronic Engineering,Japan
- **会议**: ICCV 2023

### FedRCIL: Federated Knowledge Distillation for Representation based Contrastive Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00371) · 📚 被引 9
- **作者**: Athanasios Psaltis, Christos Chatzikonstantinou, Charalampos Z. Patrikakis, Petros Daras
- **🏷️ 机构**: Centre for Research and Technology Hellas,Thessaloniki,Greece, University of West Attica,Dept. of Electrical and Electronics Engineering,Athens,Greece
- **会议**: ICCV 2023

### Online Prototype Learning for Online Continual Learning.
- **链接**: [arXiv:2308.00301](https://arxiv.org/abs/2308.00301) · [代码](https://github.com/weilllllls/OnPro) · 📚 被引 64
- **作者**: Yujie Wei, Jiaxin Ye, Zhizhong Huang, Junping Zhang, Hongming Shan
- **🏷️ 机构**: Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, School of Computer Science Fudan University,Shanghai Key Lab of Intelligent Information Processing
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (CL) studies the problem of learning continuously from a single-pass data stream while adapting to new data and mitigating catastrophic forgetting. Recently, by storing a small subset of old data, replay-based methods have shown promising performance. Unlike previous methods that focus on sample storage or knowledge distillation against catastrophic forgetting, this paper aims to understand why the online learning models fail to generalize well from a new perspective of shortcut learning. We identify shortcut learning as the key limiting factor for online CL, where the learned features may be biased, not generalizable to new tasks, and may have an adverse impact on knowledge distillation. To tackle this issue, we present the online prototype learning (OnPro) framework for online CL. First, we propose online prototype equilibrium to learn representative features against shortcut learning and discriminative features to avoid class confusion, ultimately achieving an equilibrium status that separates all seen classes well while learning new classes. Second, with the feedback of online prototypes, we devise a novel adaptive prototypical feedback mechanism to sense the classes that are easily misclassified and then enhance their boundaries. Extensive experimental results on widely-used benchmark datasets demonstrate the superior performance of OnPro over the state-of-the-art baseline methods. Source code is available at https://github.com/weilllllls/OnPro.

</details>

### CoMFormer: Continual Learning in Semantic and Panoptic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00294) · 📚 被引 33
- **作者**: Fabio Cermelli, Matthieu Cord, Arthur Douillard
- **🏷️ 机构**: Politecnico di Torino, Sorbonne Universit&#x00E9;
- **会议**: CVPR 2023

### Exploring Data Geometry for Continual Learning.
- **链接**: [arXiv:2304.03931](https://arxiv.org/abs/2304.03931) · 📚 被引 12
- **作者**: Zhi Gao, Chen Xu, Feng Li, Yunde Jia, Mehrtash Harandi, Yuwei Wu
- **🏷️ 机构**: School of Computer Science &#x0026; Technology, Beijing Institute of Technology,Beijing Key Laboratory of Intelligent Information Technology,China, Shenzhen MSU-BIT University,Guangdong Laboratory of Machine Perception and Intelligent Computing,China, Monash University, and Data61,Department of Electrical and Computer Systems Eng.,Australia
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to efficiently learn from a non-stationary stream of data while avoiding forgetting the knowledge of old data. In many practical applications, data complies with non-Euclidean geometry. As such, the commonly used Euclidean space cannot gracefully capture non-Euclidean geometric structures of data, leading to inferior results. In this paper, we study continual learning from a novel perspective by exploring data geometry for the non-stationary stream of data. Our method dynamically expands the geometry of the underlying space to match growing geometric structures induced by new data, and prevents forgetting by keeping geometric structures of old data into account. In doing so, making use of the mixed curvature space, we propose an incremental search scheme, through which the growing geometric structures are encoded. Then, we introduce an angular-regularization loss and a neighbor-robustness loss to train the model, capable of penalizing the change of global geometric structures and local geometric structures. Experiments show that our method achieves better performance than baseline methods designed in Euclidean space.

</details>

### Real-Time Evaluation in Online Continual Learning: A New Hope.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01144) · 📚 被引 35
- **作者**: Yasir Ghunaim, Adel Bibi, Kumail Alhamoud, Motasem Alfarra, Hasan Abed Al Kader Hammoud, Ameya Prabhu et al.
- **🏷️ 机构**: King Abdullah University of Science and Technology (KAUST), University of Oxford
- **会议**: CVPR 2023

### Preserving Linear Separability in Continual Learning by Backward Feature Projection.
- **链接**: [arXiv:2303.14595](https://arxiv.org/abs/2303.14595) · [代码](https://github.com/rvl-lab-utoronto/BFP) · 📚 被引 12
- **作者**: Qiao Gu, Dongsub Shim, Florian Shkurti
- **🏷️ 机构**: University of Toronto, LG AI Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning (CL) aims to learn new knowledge and consolidate previously learned knowledge from non-stationary data streams. Due to the time-varying training setting, the model learned from a changing distribution easily forgets the previously learned knowledge and biases toward the newly received task. To address this problem, we propose a Continual Bias Adaptor (CBA) module to augment the classifier network to adapt to catastrophic distribution change during training, such that the classifier network is able to learn a stable consolidation of previously learned tasks. In the testing stage, CBA can be removed which introduces no additional computation cost and memory overhead. We theoretically reveal the reason why the proposed method can effectively alleviate catastrophic distribution shifts, and empirically demonstrate its effectiveness through extensive experiments based on four rehearsal-based baselines and three public continual learning benchmarks.

</details>

### Wasserstein Expansible Variational Autoencoder for Discriminative and Generative Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01711) · 📚 被引 2
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: University of York,Department of Computer Science,York,UK,YO10 5GH
- **会议**: ICCV 2023

### Self-Evolved Dynamic Expansion Model for Task-Free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02020) · 📚 被引 16
- **作者**: Fei Ye, Adrian G. Bors
- **🏷️ 机构**: University of York,Department of Computer Science,York,UK,YO10 5GH
- **会议**: ICCV 2023

### Continual Learning for Personalized Co-Speech Gesture Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01910) · 📚 被引 8
- **作者**: Chaitanya Ahuja, Pratik Joshi, Ryo Ishii, Louis-Philippe Morency
- **🏷️ 机构**: CMU,Language Technologies Institute, NTT Human Informatics Laboratories
- **会议**: ICCV 2023

### CLNeRF: Continual Learning Meets NeRF.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.02119) · 📚 被引 18
- **作者**: Zhipeng Cai, Matthias Müller
- **🏷️ 机构**: Intel Labs
- **会议**: ICCV 2023

### Towards Realistic Evaluation of Industrial Continual Learning Scenarios with an Emphasis on Energy Consumption and Computational Footprint.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01057) · 📚 被引 9
- **作者**: Vivek Chavan, Paul Koch, Marian Schlüter, Clemens Briese
- **🏷️ 机构**: Fraunhofer IPK,Berlin,Germany
- **会议**: ICCV 2023

### A Unified Continual Learning Framework with General Parameter-Efficient Tuning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01055) · 📚 被引 96
- **作者**: Qiankun Gao, Chen Zhao, Yifan Sun, Teng Xi, Gang Zhang, Bernard Ghanem et al.
- **🏷️ 机构**: Peking University Shenzhen Graduate School, King Abdullah University of Science and Technology (KAUST), Baidu Inc.
- **会议**: ICCV 2023

### CLR: Channel-wise Lightweight Reprogramming for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01723) · 📚 被引 8
- **作者**: Yunhao Ge, Yuecheng Li, Shuo Ni, Jiaping Zhao, Ming-Hsuan Yang, Laurent Itti
- **🏷️ 机构**: University of Southern California, Google Research
- **会议**: ICCV 2023

### Rapid Adaptation in Online Continual Learning: Are We Evaluating It Right?
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01728) · 📚 被引 6
- **作者**: Hasan Abed Al Kader Hammoud, Ameya Prabhu, Ser-Nam Lim, Philip H. S. Torr, Adel Bibi, Bernard Ghanem
- **🏷️ 机构**: KAUST, University of Oxford, Meta AI
- **会议**: ICCV 2023

### Class-incremental Continual Learning for Instance Segmentation with Image-level Weak Supervision.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00121) · 📚 被引 16
- **作者**: Yu-Hsing Hsieh, Guan-Sheng Chen, Shun-Xian Cai, Ting-Yun Wei, Huei-Fang Yang, Chu-Song Chen
- **🏷️ 机构**: National Taiwan University,Dept. Computer Science and Information Engineering,Taiwan, National Sun Yat-sen University,Dept. Information Management,Taiwan
- **会议**: ICCV 2023

### Growing a Brain with Sparsity-Inducing Generation for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01738)
- **作者**: Hyundong Jin, Gyeong-Hyeon Kim, Chanho Ahn, Eunwoo Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Multimodal Parameter-Efficient Few-Shot Class Incremental Learning.
- **链接**: [arXiv:2303.04751](https://arxiv.org/abs/2303.04751) · 📚 被引 37
- **作者**: Marco D'Alessandro, Alberto Alonso, Enrique Calabrés, Mikel Galar
- **🏷️ 机构**: Neuraptic AI, Public University of Navarra
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-Shot Class Incremental Learning (FSCIL) is a challenging continual learning task, where limited training examples are available during several learning sessions. To succeed in this task, it is necessary to avoid over-fitting new classes caused by biased distributions in the few-shot training sets. The general approach to address this issue involves enhancing the representational capability of a pre-defined backbone architecture by adding special modules for backward compatibility with older classes. However, this approach has not yet solved the dilemma of ensuring high classification accuracy over time while reducing the gap between the performance obtained on larger training sets and the smaller ones. In this work, we propose an alternative approach called Continual Parameter-Efficient CLIP (CPE-CLIP) to reduce the loss of information between different learning sessions. Instead of adapting additional modules to address information loss, we leverage the vast knowledge acquired by CLIP in large-scale pre-training and its effectiveness in generalizing to new concepts. Our approach is multimodal and parameter-efficient, relying on learnable prompts for both the language and vision encoders to enable transfer learning across sessions. We also introduce prompt regularization to improve performance and prevent forgetting. Our experimental results demonstrate that CPE-CLIP significantly improves FSCIL performance compared to state-of-the-art proposals while also drastically reducing the number of learnable parameters and training costs.

</details>

### On the Effectiveness of LayerNorm Tuning for Continual Learning in Vision Transformers.
- **链接**: [arXiv:2308.09610](https://arxiv.org/abs/2308.09610) · 📚 被引 9
- **作者**: Thomas De Min, Massimiliano Mancini, Karteek Alahari, Xavier Alameda-Pineda, Elisa Ricci
- **🏷️ 机构**: University of Trento, Inria, Univ. Grenoble Alpes,CNRS, Grenoble INP, LJK,Grenoble,France,38000
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art rehearsal-free continual learning methods exploit the peculiarities of Vision Transformers to learn task-specific prompts, drastically reducing catastrophic forgetting. However, there is a tradeoff between the number of learned parameters and the performance, making such models computationally expensive. In this work, we aim to reduce this cost while maintaining competitive performance. We achieve this by revisiting and extending a simple transfer learning idea: learning task-specific normalization layers. Specifically, we tune the scale and bias parameters of LayerNorm for each continual learning task, selecting them at inference time based on the similarity between task-specific keys and the output of the pre-trained model. To make the classifier robust to incorrect selection of parameters during inference, we introduce a two-stage training procedure, where we first optimize the task-specific parameters and then train the classifier with the same selection procedure of the inference time. Experiments on ImageNet-R and CIFAR-100 show that our method achieves results that are either superior or on par with {the state of the art} while being computationally cheaper.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning aims to learn a single model on a sequence of tasks without having access to data from previous tasks. The biggest challenge in the domain still remains catastrophic forgetting: a loss in performance on seen classes of earlier tasks. Some existing methods rely on an expensive replay buffer to store a chunk of data from previous tasks. This, while promising, becomes expensive when the number of tasks becomes large or data can not be stored for privacy reasons. As an alternative, prompt-based methods have been proposed that store the task information in a learnable prompt pool. This prompt pool instructs a frozen image encoder on how to solve each task. While the model faces a disjoint set of classes in each task in this setting, we argue that these classes can be encoded to the same embedding space of a pre-trained language encoder. In this work, we propose Language Guidance for Prompt-based Continual Learning (LGCL) as a plug-in for prompt-based methods. LGCL is model agnostic and introduces language guidance at the task level in the prompt pool and at the class level on the output feature of the vision encoder. We show with extensive experimentation that LGCL consistently improves the performance of prompt-based continual learning methods to set a new state-of-the art. LGCL achieves these performance improvements without needing any additional learnable parameters.

</details>

### FedRCIL: Federated Knowledge Distillation for Representation based Contrastive Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00371) · 📚 被引 9
- **作者**: Athanasios Psaltis, Christos Chatzikonstantinou, Charalampos Z. Patrikakis, Petros Daras
- **🏷️ 机构**: Centre for Research and Technology Hellas,Thessaloniki,Greece, University of West Attica,Dept. of Electrical and Electronics Engineering,Athens,Greece
- **会议**: ICCV 2023

### Online Prototype Learning for Online Continual Learning.
- **链接**: [arXiv:2308.00301](https://arxiv.org/abs/2308.00301) · [代码](https://github.com/weilllllls/OnPro) · 📚 被引 64
- **作者**: Yujie Wei, Jiaxin Ye, Zhizhong Huang, Junping Zhang, Hongming Shan
- **🏷️ 机构**: Fudan University,Institute of Science and Technology for Brain-Inspired Intelligence, School of Computer Science Fudan University,Shanghai Key Lab of Intelligent Information Processing
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### Dense Network Expansion for Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01141) · 📚 被引 68
- **作者**: Zhiyuan Hu, Yunsheng Li, Jiancheng Lyu, Dashan Gao, Nuno Vasconcelos
- **🏷️ 机构**: UC San Diego, Microsoft Cloud &#x002B; AI, Qualcomm AI Research
- **会议**: CVPR 2023

</details>

### CBA: Improving Online Continual Learning via Continual Bias Adaptor.
- **链接**: [arXiv:2308.06925](https://arxiv.org/abs/2308.06925) · 📚 被引 23
- **作者**: Quanziang Wang, Renzhen Wang, Yichen Wu, Xixi Jia, Deyu Meng
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, City University of Hong Kong, Xidian University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) enables models to adapt to new tasks and environments without forgetting previously learned knowledge. While current CL setups have ignored the relationship between labels in the past task and the new task with or without small task overlaps, real-world scenarios often involve hierarchical relationships between old and new tasks, posing another challenge for traditional CL approaches. To address this challenge, we propose a novel multi-level hierarchical class incremental task configuration with an online learning constraint, called hierarchical label expansion (HLE). Our configuration allows a network to first learn coarse-grained classes, with data labels continually expanding to more fine-grained classes in various hierarchy depths. To tackle this new setup, we propose a rehearsal-based method that utilizes hierarchy-aware pseudo-labeling to incorporate hierarchical class information. Additionally, we propose a simple yet effective memory management and sampling strategy that selectively adopts samples of newly encountered classes. Our experiments demonstrate that our proposed method can effectively use hierarchy on our HLE setup to improve classification accuracy across all levels of hierarchies, regardless of depth and class imbalance ratio, outperforming prior state-of-the-art works by significant margins while also outperforming them on the conventional disjoint, blurry and i-Blurry CL setups.

</details>

### Few-Shot Class-Incremental Learning via Class-Aware Bilateral Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01139) · 📚 被引 110
- **作者**: Linglan Zhao, Jing Lu, Yunlu Xu, Zhanzhan Cheng, Dashan Guo, Yi Niu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Electronic Engineering, Hikvision Research Institute
- **会议**: CVPR 2023

### Incrementer: Transformer for Class-Incremental Semantic Segmentation with Knowledge Distillation Focusing on Old Class.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00697) · 📚 被引 40
- **作者**: Chao Shang, Hongliang Li, Fanman Meng, Qingbo Wu, Heqian Qiu, Lanxiao Wang
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: CVPR 2023
