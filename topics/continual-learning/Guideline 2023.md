# Continual Learning — 2023 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 57 · 按重要性排序（引用数/标题信号启发式）

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

### Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01752)
- **作者**: Zangwei Zheng, Mingyuan Ma, Kai Wang, Ziheng Qin, Xiangyu Yue, Yang You
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### On the Effectiveness of LayerNorm Tuning for Continual Learning in Vision Transformers.
- **链接**: [arXiv:2308.09610](https://arxiv.org/abs/2308.09610) · 📚 被引 9
- **作者**: Thomas De Min, Massimiliano Mancini, Karteek Alahari, Xavier Alameda-Pineda, Elisa Ricci
- **🏷️ 机构**: University of Trento, Inria, Univ. Grenoble Alpes,CNRS, Grenoble INP, LJK,Grenoble,France,38000
- **会议**: ICCV 2023

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

### CBA: Improving Online Continual Learning via Continual Bias Adaptor.
- **链接**: [arXiv:2308.06925](https://arxiv.org/abs/2308.06925) · 📚 被引 24
- **作者**: Quanziang Wang, Renzhen Wang, Yichen Wu, Xixi Jia, Deyu Meng
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, City University of Hong Kong, Xidian University
- **会议**: ICCV 2023

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
- **链接**: [arXiv:2308.14816](https://arxiv.org/abs/2308.14816) · [代码](https://github.com/IntelLabs/CLNeRF) · 📚 被引 18
- **作者**: Zhipeng Cai, Matthias Müller
- **🏷️ 机构**: Intel Labs
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Novel view synthesis aims to render unseen views given a set of calibrated images. In practical applications, the coverage, appearance or geometry of the scene may change over time, with new images continuously being captured. Efficiently incorporating such continuous change is an open challenge. Standard NeRF benchmarks only involve scene coverage expansion. To study other practical scene changes, we propose a new dataset, World Across Time (WAT), consisting of scenes that change in appearance and geometry over time. We also propose a simple yet effective method, CLNeRF, which introduces continual learning (CL) to Neural Radiance Fields (NeRFs). CLNeRF combines generative replay and the Instant Neural Graphics Primitives (NGP) architecture to effectively prevent catastrophic forgetting and efficiently update the model when new data arrives. We also add trainable appearance and geometry embeddings to NGP, allowing a single compact model to handle complex scene changes. Without the need to store historical images, CLNeRF trained sequentially over multiple scans of a changing scene performs on-par with the upper bound model trained on all scans at once. Compared to other CL baselines CLNeRF performs much better across standard benchmarks and WAT. The source code, and the WAT dataset are available at https://github.com/IntelLabs/CLNeRF. Video presentation is available at: https://youtu.be/nLRt6OoDGq0?si=8yD6k-8MMBJInQPs

</details>

### Towards Realistic Evaluation of Industrial Continual Learning Scenarios with an Emphasis on Energy Consumption and Computational Footprint.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01057) · 📚 被引 9
- **作者**: Vivek Chavan, Paul Koch, Marian Schlüter, Clemens Briese
- **🏷️ 机构**: Fraunhofer IPK,Berlin,Germany
- **会议**: ICCV 2023

### A Unified Continual Learning Framework with General Parameter-Efficient Tuning.
- **链接**: [arXiv:2303.10070](https://arxiv.org/abs/2303.10070) · [代码](https://github.com/gqk/LAE) · 📚 被引 96
- **作者**: Qiankun Gao, Chen Zhao, Yifan Sun, Teng Xi, Gang Zhang, Bernard Ghanem et al.
- **🏷️ 机构**: Peking University Shenzhen Graduate School, King Abdullah University of Science and Technology (KAUST), Baidu Inc.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The "pre-training $\rightarrow$ downstream adaptation" presents both new opportunities and challenges for Continual Learning (CL). Although the recent state-of-the-art in CL is achieved through Parameter-Efficient-Tuning (PET) adaptation paradigm, only prompt has been explored, limiting its application to Transformers only. In this paper, we position prompting as one instantiation of PET, and propose a unified CL framework with general PET, dubbed as Learning-Accumulation-Ensemble (LAE). PET, e.g., using Adapter, LoRA, or Prefix, can adapt a pre-trained model to downstream tasks with fewer parameters and resources. Given a PET method, our LAE framework incorporates it for CL with three novel designs. 1) Learning: the pre-trained model adapts to the new task by tuning an online PET module, along with our adaptation speed calibration to align different PET modules, 2) Accumulation: the task-specific knowledge learned by the online PET module is accumulated into an offline PET module through momentum update, 3) Ensemble: During inference, we respectively construct two experts with online/offline PET modules (which are favored by the novel/historical tasks) for prediction ensemble. We show that LAE is compatible with a battery of PET methods and gains strong CL capability. For example, LAE with Adaptor PET surpasses the prior state-of-the-art by 1.3% and 3.6% in last-incremental accuracy on CIFAR100 and ImageNet-R datasets, respectively. Code is available at \url{https://github.com/gqk/LAE}.

</details>

### CLR: Channel-wise Lightweight Reprogramming for Continual Learning.
- **链接**: [arXiv:2307.11386](https://arxiv.org/abs/2307.11386) · [代码](https://github.com/gyhandy/Channel-wise-Lightweight-Reprogramming) · 📚 被引 8
- **作者**: Yunhao Ge, Yuecheng Li, Shuo Ni, Jiaping Zhao, Ming-Hsuan Yang, Laurent Itti
- **🏷️ 机构**: University of Southern California, Google Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to emulate the human ability to continually accumulate knowledge over sequential tasks. The main challenge is to maintain performance on previously learned tasks after learning new tasks, i.e., to avoid catastrophic forgetting. We propose a Channel-wise Lightweight Reprogramming (CLR) approach that helps convolutional neural networks (CNNs) overcome catastrophic forgetting during continual learning. We show that a CNN model trained on an old task (or self-supervised proxy task) could be ``reprogrammed" to solve a new task by using our proposed lightweight (very cheap) reprogramming parameter. With the help of CLR, we have a better stability-plasticity trade-off to solve continual learning problems: To maintain stability and retain previous task ability, we use a common task-agnostic immutable part as the shared ``anchor" parameter set. We then add task-specific lightweight reprogramming parameters to reinterpret the outputs of the immutable parts, to enable plasticity and integrate new knowledge. To learn sequential tasks, we only train the lightweight reprogramming parameters to learn each new task. Reprogramming parameters are task-specific and exclusive to each task, which makes our method immune to catastrophic forgetting. To minimize the parameter requirement of reprogramming to learn new tasks, we make reprogramming lightweight by only adjusting essential kernels and learning channel-wise linear mappings from anchor parameters to task-specific domain knowledge. We show that, for general CNNs, the CLR parameter increase is less than 0.6\% for any new task. Our method outperforms 13 state-of-the-art continual learning baselines on a new challenging sequence of 53 image classification datasets. Code and data are available at https://github.com/gyhandy/Channel-wise-Lightweight-Reprogramming

</details>

### Rapid Adaptation in Online Continual Learning: Are We Evaluating It Right?
- **链接**: [arXiv:2305.09275](https://arxiv.org/abs/2305.09275) · [代码](https://github.com/drimpossible/EvalOCL) · 📚 被引 6
- **作者**: Hasan Abed Al Kader Hammoud, Ameya Prabhu, Ser-Nam Lim, Philip H. S. Torr, Adel Bibi, Bernard Ghanem
- **🏷️ 机构**: KAUST, University of Oxford, Meta AI
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We revisit the common practice of evaluating adaptation of Online Continual Learning (OCL) algorithms through the metric of online accuracy, which measures the accuracy of the model on the immediate next few samples. However, we show that this metric is unreliable, as even vacuous blind classifiers, which do not use input images for prediction, can achieve unrealistically high online accuracy by exploiting spurious label correlations in the data stream. Our study reveals that existing OCL algorithms can also achieve high online accuracy, but perform poorly in retaining useful information, suggesting that they unintentionally learn spurious label correlations. To address this issue, we propose a novel metric for measuring adaptation based on the accuracy on the near-future samples, where spurious correlations are removed. We benchmark existing OCL approaches using our proposed metric on large-scale datasets under various computational budgets and find that better generalization can be achieved by retaining and reusing past seen information. We believe that our proposed metric can aid in the development of truly adaptive OCL methods. We provide code to reproduce our results at https://github.com/drimpossible/EvalOCL.

</details>

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

### Generating Instance-level Prompts for Rehearsal-free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01088) · 📚 被引 60
- **作者**: Dahuin Jung, Dongyoon Han, Jihwan Bang, Hwanjun Song
- **🏷️ 机构**: Seoul National University,Department of Electrical and Computer Engineering,Seoul,Korea, NAVER AI Lab, NAVER Cloud
- **会议**: ICCV 2023

### Introducing Language Guidance in Prompt-based Continual Learning.
- **链接**: [arXiv:2308.15827](https://arxiv.org/abs/2308.15827) · 📚 被引 35
- **作者**: Muhammad Gul Zain Ali Khan, Muhammad Ferjad Naeem, Luc Van Gool, Didier Stricker, Federico Tombari, Muhammad Zeshan Afzal
- **🏷️ 机构**: RPTU, ETH Z&#x00FC;rich, TUM
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual Learning aims to learn a single model on a sequence of tasks without having access to data from previous tasks. The biggest challenge in the domain still remains catastrophic forgetting: a loss in performance on seen classes of earlier tasks. Some existing methods rely on an expensive replay buffer to store a chunk of data from previous tasks. This, while promising, becomes expensive when the number of tasks becomes large or data can not be stored for privacy reasons. As an alternative, prompt-based methods have been proposed that store the task information in a learnable prompt pool. This prompt pool instructs a frozen image encoder on how to solve each task. While the model faces a disjoint set of classes in each task in this setting, we argue that these classes can be encoded to the same embedding space of a pre-trained language encoder. In this work, we propose Language Guidance for Prompt-based Continual Learning (LGCL) as a plug-in for prompt-based methods. LGCL is model agnostic and introduces language guidance at the task level in the prompt pool and at the class level on the output feature of the vision encoder. We show with extensive experimentation that LGCL consistently improves the performance of prompt-based continual learning methods to set a new state-of-the art. LGCL achieves these performance improvements without needing any additional learnable parameters.

</details>

### Online Continual Learning on Hierarchical Label Expansion.
- **链接**: [arXiv:2308.14374](https://arxiv.org/abs/2308.14374) · 📚 被引 4
- **作者**: Byung Hyun Lee, Okchul Jung, Jonghyun Choi, Se Young Chun
- **🏷️ 机构**: Seoul National University,Dept. of ECE,Republic of Korea, Yonsei University,Republic of Korea
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning (CL) enables models to adapt to new tasks and environments without forgetting previously learned knowledge. While current CL setups have ignored the relationship between labels in the past task and the new task with or without small task overlaps, real-world scenarios often involve hierarchical relationships between old and new tasks, posing another challenge for traditional CL approaches. To address this challenge, we propose a novel multi-level hierarchical class incremental task configuration with an online learning constraint, called hierarchical label expansion (HLE). Our configuration allows a network to first learn coarse-grained classes, with data labels continually expanding to more fine-grained classes in various hierarchy depths. To tackle this new setup, we propose a rehearsal-based method that utilizes hierarchy-aware pseudo-labeling to incorporate hierarchical class information. Additionally, we propose a simple yet effective memory management and sampling strategy that selectively adopts samples of newly encountered classes. Our experiments demonstrate that our proposed method can effectively use hierarchy on our HLE setup to improve classification accuracy across all levels of hierarchies, regardless of depth and class imbalance ratio, outperforming prior state-of-the-art works by significant margins while also outperforming them on the conventional disjoint, blurry and i-Blurry CL setups.

</details>

### Measuring Asymmetric Gradient Discrepancy in Parallel Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01048) · 📚 被引 9
- **作者**: Fan Lyu, Qing Sun, Fanhua Shang, Liang Wan, Wei Feng
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing
- **会议**: ICCV 2023

### NAPA-VQ: Neighborhood Aware Prototype Augmentation with Vector Quantization for Continual Learning.
- **链接**: [arXiv:2308.09297](https://arxiv.org/abs/2308.09297) · [代码](https://github.com/TamashaM/NAPA-VQ.git) · 📚 被引 16
- **作者**: Tamasha Malepathirana, Damith A. Senanayake, Saman K. Halgamuge
- **🏷️ 机构**: The University of Melbourne,Dept. of Mechanical Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Catastrophic forgetting; the loss of old knowledge upon acquiring new knowledge, is a pitfall faced by deep neural networks in real-world applications. Many prevailing solutions to this problem rely on storing exemplars (previously encountered data), which may not be feasible in applications with memory limitations or privacy constraints. Therefore, the recent focus has been on Non-Exemplar based Class Incremental Learning (NECIL) where a model incrementally learns about new classes without using any past exemplars. However, due to the lack of old data, NECIL methods struggle to discriminate between old and new classes causing their feature representations to overlap. We propose NAPA-VQ: Neighborhood Aware Prototype Augmentation with Vector Quantization, a framework that reduces this class overlap in NECIL. We draw inspiration from Neural Gas to learn the topological relationships in the feature space, identifying the neighboring classes that are most likely to get confused with each other. This neighborhood information is utilized to enforce strong separation between the neighboring classes as well as to generate old class representative prototypes that can better aid in obtaining a discriminative decision boundary between old and new classes. Our comprehensive experiments on CIFAR-100, TinyImageNet, and ImageNet-Subset demonstrate that NAPA-VQ outperforms the State-of-the-art NECIL methods by an average improvement of 5%, 2%, and 4% in accuracy and 10%, 3%, and 9% in forgetting respectively. Our code can be found in https://github.com/TamashaM/NAPA-VQ.git.

</details>

### Class-Incremental Grouping Network for Continual Audio-Visual Learning.
- **链接**: [arXiv:2309.05281](https://arxiv.org/abs/2309.05281) · [代码](https://github.com/stoneMo/CIGN) · 📚 被引 20
- **作者**: Shentong Mo, Weiguo Pian, Yapeng Tian
- **🏷️ 机构**: Carnegie Mellon University, University of Texas at Dallas
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is a challenging problem in which models need to be trained on non-stationary data across sequential tasks for class-incremental learning. While previous methods have focused on using either regularization or rehearsal-based frameworks to alleviate catastrophic forgetting in image classification, they are limited to a single modality and cannot learn compact class-aware cross-modal representations for continual audio-visual learning. To address this gap, we propose a novel class-incremental grouping network (CIGN) that can learn category-wise semantic features to achieve continual audio-visual learning. Our CIGN leverages learnable audio-visual class tokens and audio-visual grouping to continually aggregate class-aware features. Additionally, it utilizes class tokens distillation and continual grouping to prevent forgetting parameters learned from previous tasks, thereby improving the model's ability to capture discriminative audio-visual categories. We conduct extensive experiments on VGGSound-Instruments, VGGSound-100, and VGG-Sound Sources benchmarks. Our experimental results demonstrate that the CIGN achieves state-of-the-art audio-visual class-incremental learning performance. Code is available at https://github.com/stoneMo/CIGN.

</details>

### ICICLE: Interpretable Class Incremental Continual Learning.
- **链接**: [arXiv:2303.07811](https://arxiv.org/abs/2303.07811) · 📚 被引 21
- **作者**: Dawid Rymarczyk, Joost van de Weijer, Bartosz Zielinski, Bartlomiej Twardowski
- **🏷️ 机构**: Jagiellonian University,Faculty of Mathematics and Computer Science, Autonomous University of Barcelona
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning enables incremental learning of new tasks without forgetting those previously learned, resulting in positive knowledge transfer that can enhance performance on both new and old tasks. However, continual learning poses new challenges for interpretability, as the rationale behind model predictions may change over time, leading to interpretability concept drift. We address this problem by proposing Interpretable Class-InCremental LEarning (ICICLE), an exemplar-free approach that adopts a prototypical part-based approach. It consists of three crucial novelties: interpretability regularization that distills previously learned concepts while preserving user-friendly positive reasoning; proximity-based prototype initialization strategy dedicated to the fine-grained setting; and task-recency bias compensation devoted to prototypical parts. Our experimental results demonstrate that ICICLE reduces the interpretability concept drift and outperforms the existing exemplar-free methods of common class-incremental learning when applied to concept-based models.

</details>

### Instance and Category Supervision are Alternate Learners for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00515) · 📚 被引 2
- **作者**: Xudong Tian, Zhizhong Zhang, Xin Tan, Jun Liu, Chengjie Wang, Yanyun Qu et al.
- **🏷️ 机构**: East China Normal University, Tencent YouTu Lab, Xiamen University
- **会议**: ICCV 2023

### Data Augmented Flatness-aware Gradient Projection for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00518) · 📚 被引 15
- **作者**: Enneng Yang, Li Shen, Zhenyi Wang, Shiwei Liu, Guibing Guo, Xingwei Wang
- **🏷️ 机构**: Northeastern University,China, JD Explore Academy,China, University of Maryland,USA
- **会议**: ICCV 2023

### TARGET: Federated Class-Continual Learning via Exemplar-Free Distillation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00441) · 📚 被引 71
- **作者**: Jie Zhang, Chen Chen, Weiming Zhuang, Lingjuan Lyu
- **🏷️ 机构**: ETH Zurich, Sony AI
- **会议**: ICCV 2023

### SLCA: Slow Learner with Classifier Alignment for Continual Learning on a Pre-trained Model.
- **链接**: [arXiv:2303.05118](https://arxiv.org/abs/2303.05118) · [代码](https://github.com/GengDavid/SLCA) · 📚 被引 113
- **作者**: Gengwei Zhang, Liyuan Wang, Guoliang Kang, Ling Chen, Yunchao Wei
- **🏷️ 机构**: University of Technology Sydney, Tsinghua University, Beihang University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The goal of continual learning is to improve the performance of recognition models in learning sequentially arrived data. Although most existing works are established on the premise of learning from scratch, growing efforts have been devoted to incorporating the benefits of pre-training. However, how to adaptively exploit the pre-trained knowledge for each incremental task while maintaining its generalizability remains an open question. In this work, we present an extensive analysis for continual learning on a pre-trained model (CLPM), and attribute the key challenge to a progressive overfitting problem. Observing that selectively reducing the learning rate can almost resolve this issue in the representation layer, we propose a simple but extremely effective approach named Slow Learner with Classifier Alignment (SLCA), which further improves the classification layer by modeling the class-wise distributions and aligning the classification layers in a post-hoc fashion. Across a variety of scenarios, our proposal provides substantial improvements for CLPM (e.g., up to 49.76%, 50.05%, 44.69% and 40.16% on Split CIFAR-100, Split ImageNet-R, Split CUB-200 and Split Cars-196, respectively), and thus outperforms state-of-the-art approaches by a large margin. Based on such a strong baseline, critical factors and promising directions are analyzed in-depth to facilitate subsequent research. Code has been made available at: https://github.com/GengDavid/SLCA.

</details>

### Improving Replay Sample Selection and Storage for Less Forgetting in Continual Learning.
- **链接**: [arXiv:2308.01895](https://arxiv.org/abs/2308.01895) · 📚 被引 19
- **作者**: Daniel Brignac, Niels Lobo, Abhijit Mahalanobis
- **🏷️ 机构**: University of Arizona,Tucson,Arizona, University of Central Florida,Orlando,Florida
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning seeks to enable deep learners to train on a series of tasks of unknown length without suffering from the catastrophic forgetting of previous tasks. One effective solution is replay, which involves storing few previous experiences in memory and replaying them when learning the current task. However, there is still room for improvement when it comes to selecting the most informative samples for storage and determining the optimal number of samples to be stored. This study aims to address these issues with a novel comparison of the commonly used reservoir sampling to various alternative population strategies and providing a novel detailed analysis of how to find the optimal number of stored samples.

</details>

### Memory Population in Continual Learning via Outlier Elimination.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00373) · 📚 被引 1
- **作者**: Julio Hurtado, Alain Raymond-Saez, Vladimir Araujo, Vincenzo Lomonaco, Alvaro Soto, Davide Bacciu
- **🏷️ 机构**: University of Pisa, Pontificia Universidad Cat&#x00F3;lica de Chile
- **会议**: ICCV 2023

### Looking through the past: better knowledge retention for generative replay in continual learning.
- **链接**: [arXiv:2309.10012](https://arxiv.org/abs/2309.10012) · [代码](https://github.com/valeriya-khan/looking-through-the-past) · 📚 被引 2
- **作者**: Valeriya Khan, Sebastian Cygert, Bartlomiej Twardowski, Tomasz Trzcinski
- **🏷️ 机构**: IDEAS NCBR, Warsaw, Poland
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we improve the generative replay in a continual learning setting to perform well on challenging scenarios. Current generative rehearsal methods are usually benchmarked on small and simple datasets as they are not powerful enough to generate more complex data with a greater number of classes. We notice that in VAE-based generative replay, this could be attributed to the fact that the generated features are far from the original ones when mapped to the latent space. Therefore, we propose three modifications that allow the model to learn and generate complex data. More specifically, we incorporate the distillation in latent space between the current and previous models to reduce feature drift. Additionally, a latent matching for the reconstruction and original data is proposed to improve generated features alignment. Further, based on the observation that the reconstructions are better for preserving knowledge, we add the cycling of generations through the previously trained model to make them closer to the original data. Our method outperforms other generative replay methods in various scenarios. Code available at https://github.com/valeriya-khan/looking-through-the-past.

</details>

### Continual Learning with Deep Streaming Regularized Discriminant Analysis.
- **链接**: [arXiv:2309.08353](https://arxiv.org/abs/2309.08353) · 📚 被引 2
- **作者**: Joe Khawand, Peter Hanappe, David Colliaux
- **🏷️ 机构**: Ecole Polytechnique, Sony Computer Science Laboratories Paris
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is increasingly sought after in real world machine learning applications, as it enables learning in a more human-like manner. Conventional machine learning approaches fail to achieve this, as incrementally updating the model with non-identically distributed data leads to catastrophic forgetting, where existing representations are overwritten. Although traditional continual learning methods have mostly focused on batch learning, which involves learning from large collections of labeled data sequentially, this approach is not well-suited for real-world applications where we would like new data to be integrated directly. This necessitates a paradigm shift towards streaming learning. In this paper, we propose a streaming version of regularized discriminant analysis as a solution to this challenge. We combine our algorithm with a convolutional neural network and demonstrate that it outperforms both batch learning and existing streaming learning algorithms on the ImageNet ILSVRC-2012 dataset.

</details>

### Flashback for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00368) · 📚 被引 2
- **作者**: Leila Mahmoodi, Mehrtash Harandi, Peyman Moghadam
- **🏷️ 机构**: Monash University, CSIRO,Data61
- **会议**: ICCV 2023

### Instant Continual Learning of Neural Radiance Fields.
- **链接**: [arXiv:2309.01811](https://arxiv.org/abs/2309.01811) · 📚 被引 11
- **作者**: Ryan Po, Zhengyang Dong, Alexander W. Bergman, Gordon Wetzstein
- **🏷️ 机构**: Stanford University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural radiance fields (NeRFs) have emerged as an effective method for novel-view synthesis and 3D scene reconstruction. However, conventional training methods require access to all training views during scene optimization. This assumption may be prohibitive in continual learning scenarios, where new data is acquired in a sequential manner and a continuous update of the NeRF is desired, as in automotive or remote sensing applications. When naively trained in such a continual setting, traditional scene representation frameworks suffer from catastrophic forgetting, where previously learned knowledge is corrupted after training on new data. Prior works in alleviating forgetting with NeRFs suffer from low reconstruction quality and high latency, making them impractical for real-world application. We propose a continual learning framework for training NeRFs that leverages replay-based methods combined with a hybrid explicit--implicit scene representation. Our method outperforms previous methods in reconstruction quality when trained in a continual setting, while having the additional benefit of being an order of magnitude faster.

</details>

### Selective Freezing for Efficient Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00381) · 📚 被引 12
- **作者**: Amelia Sorrenti, Giovanni Bellitto, Federica Proietto Salanitri, Matteo Pennisi, Concetto Spampinato, Simone Palazzo
- **🏷️ 机构**: University of Catania,PeRCeiVe Lab,Catania,Italy
- **会议**: ICCV 2023

### A Comprehensive Empirical Evaluation on Online Continual Learning.
- **链接**: [arXiv:2308.10328](https://arxiv.org/abs/2308.10328) · [代码](https://github.com/AlbinSou/ocl_survey) · 📚 被引 16
- **作者**: Albin Soutif-Cormerais, Antonio Carta, Andrea Cossu, Julio Hurtado, Vincenzo Lomonaco, Joost van de Weijer et al.
- **🏷️ 机构**: Universitat Aut&#x00F2;noma de Barcelona,Computer Vision Center,Barcelona,Spain, University of Pisa,Department of Computer Science,Pisa,Italy, Scuola Normale Superiore,Pisa,Italy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning aims to get closer to a live learning experience by learning directly on a stream of data with temporally shifting distribution and by storing a minimum amount of data from that stream. In this empirical evaluation, we evaluate various methods from the literature that tackle online continual learning. More specifically, we focus on the class-incremental setting in the context of image classification, where the learner must learn new classes incrementally from a stream of data. We compare these methods on the Split-CIFAR100 and Split-TinyImagenet benchmarks, and measure their average accuracy, forgetting, stability, and quality of the representations, to evaluate various aspects of the algorithm at the end but also during the whole training period. We find that most methods suffer from stability and underfitting issues. However, the learned representations are comparable to i.i.d. training under the same computational budget. No clear winner emerges from the results and basic experience replay, when properly tuned and implemented, is a very strong baseline. We release our modular and extensible codebase at https://github.com/AlbinSou/ocl_survey based on the avalanche framework to reproduce our results and encourage future research.

</details>

### Adapt Your Teacher: Improving Knowledge Distillation for Exemplar-free Continual Learning.
- **链接**: [arXiv:2308.09544](https://arxiv.org/abs/2308.09544) · [代码](https://github.com/fszatkowski/cl-teacher-adaptation) · 📚 被引 4
- **作者**: Filip Szatkowski, Mateusz Pyla, Marcin Przewiezlikowski, Sebastian Cygert, Bartlomiej Twardowski, Tomasz Trzcinski
- **🏷️ 机构**: Warsaw University of Technology, IDEAS NCBR
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we investigate exemplar-free class incremental learning (CIL) with knowledge distillation (KD) as a regularization strategy, aiming to prevent forgetting. KD-based methods are successfully used in CIL, but they often struggle to regularize the model without access to exemplars of the training data from previous tasks. Our analysis reveals that this issue originates from substantial representation shifts in the teacher network when dealing with out-of-distribution data. This causes large errors in the KD loss component, leading to performance degradation in CIL models. Inspired by recent test-time adaptation methods, we introduce Teacher Adaptation (TA), a method that concurrently updates the teacher and the main models during incremental training. Our method seamlessly integrates with KD-based CIL approaches and allows for consistent enhancement of their performance across multiple exemplar-free CIL benchmarks. The source code for our method is available at https://github.com/fszatkowski/cl-teacher-adaptation.

</details>

### ScrollNet: Dynamic Weight Importance for Continual Learning.
- **链接**: [arXiv:2308.16567](https://arxiv.org/abs/2308.16567) · [代码](https://github.com/FireFYF/ScrollNet.git) · 📚 被引 6
- **作者**: Fei Yang, Kai Wang, Joost van de Weijer
- **🏷️ 机构**: Universitat Aut&#x00F2;noma de Barcelona,Computer Vision Center,Barcelona,Spain
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The principle underlying most existing continual learning (CL) methods is to prioritize stability by penalizing changes in parameters crucial to old tasks, while allowing for plasticity in other parameters. The importance of weights for each task can be determined either explicitly through learning a task-specific mask during training (e.g., parameter isolation-based approaches) or implicitly by introducing a regularization term (e.g., regularization-based approaches). However, all these methods assume that the importance of weights for each task is unknown prior to data exposure. In this paper, we propose ScrollNet as a scrolling neural network for continual learning. ScrollNet can be seen as a dynamic network that assigns the ranking of weight importance for each task before data exposure, thus achieving a more favorable stability-plasticity tradeoff during sequential task learning by reassigning this ranking for different tasks. Additionally, we demonstrate that ScrollNet can be combined with various CL methods, including regularization-based and replay-based approaches. Experimental results on CIFAR100 and TinyImagenet datasets show the effectiveness of our proposed method. We release our code at https://github.com/FireFYF/ScrollNet.git.

</details>

### Self-Organizing Pathway Expansion for Non-Exemplar Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01759) · 📚 被引 8
- **作者**: Kai Zhu, Kecheng Zheng, Ruili Feng, Deli Zhao, Yang Cao, Zheng-Jun Zha
- **🏷️ 机构**: Alibaba Group, Zhejiang University, University of Science and Technology of China
- **会议**: ICCV 2023

### Dynamic Residual Classifier for Class Incremental Learning.
- **链接**: [arXiv:2308.13305](https://arxiv.org/abs/2308.13305) · 📚 被引 36
- **作者**: Xiuwei Chen, Xiaobin Chang
- **🏷️ 机构**: Sun Yat-sen University,School of Artificial Intelligence,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rehearsal strategy is widely used to alleviate the catastrophic forgetting problem in class incremental learning (CIL) by preserving limited exemplars from previous tasks. With imbalanced sample numbers between old and new classes, the classifier learning can be biased. Existing CIL methods exploit the long-tailed (LT) recognition techniques, e.g., the adjusted losses and the data re-sampling methods, to handle the data imbalance issue within each increment task. In this work, the dynamic nature of data imbalance in CIL is shown and a novel Dynamic Residual Classifier (DRC) is proposed to handle this challenging scenario. Specifically, DRC is built upon a recent advance residual classifier with the branch layer merging to handle the model-growing problem. Moreover, DRC is compatible with different CIL pipelines and substantially improves them. Combining DRC with the model adaptation and fusion (MAF) pipeline, this method achieves state-of-the-art results on both the conventional CIL and the LT-CIL benchmarks. Extensive experiments are also conducted for a detailed analysis. The code is publicly available.

</details>

### Heterogeneous Forgetting Compensation for Class-Incremental Learning.
- **链接**: [arXiv:2308.03374](https://arxiv.org/abs/2308.03374) · [代码](https://github.com/JiahuaDong/HFC) · 📚 被引 22
- **作者**: Jiahua Dong, Wenqi Liang, Yang Cong, Gan Sun
- **🏷️ 机构**: Chinese Academy of Sciences,State Key Laboratory of Robotics, Shenyang Institute of Automation,Shenyang,China,110016, South China University of Technology,Guangzhou,China,510640
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) has achieved remarkable successes in learning new classes consecutively while overcoming catastrophic forgetting on old categories. However, most existing CIL methods unreasonably assume that all old categories have the same forgetting pace, and neglect negative influence of forgetting heterogeneity among different old classes on forgetting compensation. To surmount the above challenges, we develop a novel Heterogeneous Forgetting Compensation (HFC) model, which can resolve heterogeneous forgetting of easy-to-forget and hard-to-forget old categories from both representation and gradient aspects. Specifically, we design a task-semantic aggregation block to alleviate heterogeneous forgetting from representation aspect. It aggregates local category information within each task to learn task-shared global representations. Moreover, we develop two novel plug-and-play losses: a gradient-balanced forgetting compensation loss and a gradient-balanced relation distillation loss to alleviate forgetting from gradient aspect. They consider gradient-balanced compensation to rectify forgetting heterogeneity of old categories and heterogeneous relation consistency. Experiments on several representative datasets illustrate effectiveness of our HFC model. The code is available at https://github.com/JiahuaDong/HFC.

</details>

### Knowledge Restore and Transfer for Multi-Label Class-Incremental Learning.
- **链接**: [arXiv:2302.13334](https://arxiv.org/abs/2302.13334) · 📚 被引 8
- **作者**: Songlin Dong, Haoyu Luo, Yuhang He, Xing Wei, Jie Cheng, Yihong Gong
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,College of Artificial Intelligence, Xi&#x2019;an Jiaotong University,School of Software Engineering, Huawei Technologies,ACS Lab,Shenzhen,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current class-incremental learning research mainly focuses on single-label classification tasks while multi-label class-incremental learning (MLCIL) with more practical application scenarios is rarely studied. Although there have been many anti-forgetting methods to solve the problem of catastrophic forgetting in class-incremental learning, these methods have difficulty in solving the MLCIL problem due to label absence and information dilution. In this paper, we propose a knowledge restore and transfer (KRT) framework for MLCIL, which includes a dynamic pseudo-label (DPL) module to restore the old class knowledge and an incremental cross-attention(ICA) module to save session-specific knowledge and transfer old class knowledge to the new model sufficiently. Besides, we propose a token loss to jointly optimize the incremental cross-attention module. Experimental results on MS-COCO and PASCAL VOC datasets demonstrate the effectiveness of our method for improving recognition performance and mitigating forgetting on multi-label class-incremental learning tasks.

</details>

### Online Class Incremental Learning on Stochastic Blurry Task Boundary via Mask and Visual Prompt Tuning.
- **链接**: [arXiv:2308.09303](https://arxiv.org/abs/2308.09303) · 📚 被引 24
- **作者**: Jun-Yeong Moon, Keon-Hee Park, Jung Uk Kim, Gyeong-Moon Park
- **🏷️ 机构**: Kyung Hee University,Yongin,Republic of Korea
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning aims to learn a model from a continuous stream of data, but it mainly assumes a fixed number of data and tasks with clear task boundaries. However, in real-world scenarios, the number of input data and tasks is constantly changing in a statistical way, not a static way. Although recently introduced incremental learning scenarios having blurry task boundaries somewhat address the above issues, they still do not fully reflect the statistical properties of real-world situations because of the fixed ratio of disjoint and blurry samples. In this paper, we propose a new Stochastic incremental Blurry task boundary scenario, called Si-Blurry, which reflects the stochastic properties of the real-world. We find that there are two major challenges in the Si-Blurry scenario: (1) inter- and intra-task forgettings and (2) class imbalance problem. To alleviate them, we introduce Mask and Visual Prompt tuning (MVP). In MVP, to address the inter- and intra-task forgetting issues, we propose a novel instance-wise logit masking and contrastive visual prompt tuning loss. Both of them help our model discern the classes to be learned in the current batch. It results in consolidating the previous knowledge. In addition, to alleviate the class imbalance problem, we introduce a new gradient similarity-based focal loss and adaptive feature scaling to ease overfitting to the major classes and underfitting to the minor classes. Extensive experiments show that our proposed MVP significantly outperforms the existing state-of-the-art methods in our challenging Si-Blurry scenario.

</details>

### First Session Adaptation: A Strong Replay-Free Baseline for Class-Incremental Learning.
- **链接**: [arXiv:2303.13199](https://arxiv.org/abs/2303.13199) · 📚 被引 24
- **作者**: Aristeidis Panos, Yuriko Kobe, Daniel Olmeda Reino, Rahaf Aljundi, Richard E. Turner
- **🏷️ 机构**: University of Cambridge, Toyota Motor Europe
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In Class-Incremental Learning (CIL) an image classification system is exposed to new classes in each learning session and must be updated incrementally. Methods approaching this problem have updated both the classification head and the feature extractor body at each session of CIL. In this work, we develop a baseline method, First Session Adaptation (FSA), that sheds light on the efficacy of existing CIL approaches and allows us to assess the relative performance contributions from head and body adaption. FSA adapts a pre-trained neural network body only on the first learning session and fixes it thereafter; a head based on linear discriminant analysis (LDA), is then placed on top of the adapted body, allowing exact updates through CIL. FSA is replay-free i.e.~it does not memorize examples from previous sessions of continual learning. To empirically motivate FSA, we first consider a diverse selection of 22 image-classification datasets, evaluating different heads and body adaptation techniques in high/low-shot offline settings. We find that the LDA head performs well and supports CIL out-of-the-box. We also find that Featurewise Layer Modulation (FiLM) adapters are highly effective in the few-shot setting, and full-body adaption in the high-shot setting. Second, we empirically investigate various CIL settings including high-shot CIL and few-shot CIL, including settings that have previously been used in the literature. We show that FSA significantly improves over the state-of-the-art in 15 of the 16 settings considered. FSA with FiLM adapters is especially performant in the few-shot setting. These results indicate that current approaches to continuous body adaptation are not working as expected. Finally, we propose a measure that can be applied to a set of unlabelled inputs which is predictive of the benefits of body adaptation.

</details>

### Space-time Prompting for Video Class-incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01096) · 📚 被引 15
- **作者**: Yixuan Pei, Zhiwu Qing, Shiwei Zhang, Xiang Wang, Yingya Zhang, Deli Zhao et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University, Huazhong University of Science and Technology, Alibaba Group
- **会议**: ICCV 2023

### Audio-Visual Class-Incremental Learning.
- **链接**: [arXiv:2308.11073](https://arxiv.org/abs/2308.11073) · [代码](https://github.com/weiguoPian/AV-CIL_ICCV2023)
- **作者**: Weiguo Pian, Shentong Mo, Yunhui Guo, Yapeng Tian
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce audio-visual class-incremental learning, a class-incremental learning scenario for audio-visual video recognition. We demonstrate that joint audio-visual modeling can improve class-incremental learning, but current methods fail to preserve semantic similarity between audio and visual features as incremental step grows. Furthermore, we observe that audio-visual correlations learned in previous tasks can be forgotten as incremental steps progress, leading to poor performance. To overcome these challenges, we propose AV-CIL, which incorporates Dual-Audio-Visual Similarity Constraint (D-AVSC) to maintain both instance-aware and class-aware semantic similarity between audio-visual modalities and Visual Attention Distillation (VAD) to retain previously learned audio-guided visual attentive ability. We create three audio-visual class-incremental datasets, AVE-Class-Incremental (AVE-CI), Kinetics-Sounds-Class-Incremental (K-S-CI), and VGGSound100-Class-Incremental (VS100-CI) based on the AVE, Kinetics-Sounds, and VGGSound datasets, respectively. Our experiments on AVE-CI, K-S-CI, and VS100-CI demonstrate that AV-CIL significantly outperforms existing class-incremental learning methods in audio-visual class-incremental learning. Code and data are available at: https://github.com/weiguoPian/AV-CIL_ICCV2023.

</details>

### Prototype Reminiscence and Augmented Asymmetric Knowledge Aggregation for Non-Exemplar Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00170) · 📚 被引 48
- **作者**: Wuxuan Shi, Mang Ye
- **🏷️ 机构**: Wuhan University,School of Computer Science,Wuhan,China
- **会议**: ICCV 2023

### When Prompt-based Incremental Learning Does Not Meet Strong Pretraining.
- **链接**: [arXiv:2308.10445](https://arxiv.org/abs/2308.10445) · [代码](https://github.com/TOM-tym/APG) · 📚 被引 39
- **作者**: Yu-Ming Tang, Yi-Xing Peng, Wei-Shi Zheng
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Incremental learning aims to overcome catastrophic forgetting when learning deep networks from sequential tasks. With impressive learning efficiency and performance, prompt-based methods adopt a fixed backbone to sequential tasks by learning task-specific prompts. However, existing prompt-based methods heavily rely on strong pretraining (typically trained on ImageNet-21k), and we find that their models could be trapped if the potential gap between the pretraining task and unknown future tasks is large. In this work, we develop a learnable Adaptive Prompt Generator (APG). The key is to unify the prompt retrieval and prompt learning processes into a learnable prompt generator. Hence, the whole prompting process can be optimized to reduce the negative effects of the gap between tasks effectively. To make our APG avoid learning ineffective knowledge, we maintain a knowledge pool to regularize APG with the feature distribution of each class. Extensive experiments show that our method significantly outperforms advanced methods in exemplar-free incremental learning without (strong) pretraining. Besides, under strong retraining, our method also has comparable performance to existing prompt-based models, showing that our method can still benefit from pretraining. Codes can be found at https://github.com/TOM-tym/APG

</details>

### Multimodal Parameter-Efficient Few-Shot Class Incremental Learning.
- **链接**: [arXiv:2303.04751](https://arxiv.org/abs/2303.04751) · 📚 被引 37
- **作者**: Marco D'Alessandro, Alberto Alonso, Enrique Calabrés, Mikel Galar
- **🏷️ 机构**: Neuraptic AI, Public University of Navarra
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-Shot Class Incremental Learning (FSCIL) is a challenging continual learning task, where limited training examples are available during several learning sessions. To succeed in this task, it is necessary to avoid over-fitting new classes caused by biased distributions in the few-shot training sets. The general approach to address this issue involves enhancing the representational capability of a pre-defined backbone architecture by adding special modules for backward compatibility with older classes. However, this approach has not yet solved the dilemma of ensuring high classification accuracy over time while reducing the gap between the performance obtained on larger training sets and the smaller ones. In this work, we propose an alternative approach called Continual Parameter-Efficient CLIP (CPE-CLIP) to reduce the loss of information between different learning sessions. Instead of adapting additional modules to address information loss, we leverage the vast knowledge acquired by CLIP in large-scale pre-training and its effectiveness in generalizing to new concepts. Our approach is multimodal and parameter-efficient, relying on learnable prompts for both the language and vision encoders to enable transfer learning across sessions. We also introduce prompt regularization to improve performance and prevent forgetting. Our experimental results demonstrate that CPE-CLIP significantly improves FSCIL performance compared to state-of-the-art proposals while also drastically reducing the number of learnable parameters and training costs.

</details>

### Class-Incremental Learning of Plant and Disease Detection: Growing Branches with Knowledge Distillation.
- **链接**: [arXiv:2304.06619](https://arxiv.org/abs/2304.06619) · 📚 被引 9
- **作者**: Mathieu Pagé Fortin
- **🏷️ 机构**: Laval University,Canada
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper investigates the problem of class-incremental object detection for agricultural applications where a model needs to learn new plant species and diseases incrementally without forgetting the previously learned ones. We adapt two public datasets to include new categories over time, simulating a more realistic and dynamic scenario. We then compare three class-incremental learning methods that leverage different forms of knowledge distillation to mitigate catastrophic forgetting. Our experiments show that all three methods suffer from catastrophic forgetting, but the Dynamic Y-KD approach, which additionally uses a dynamic architecture that grows new branches to learn new tasks, outperforms ILOD and Faster-ILOD in most settings both on new and old classes. These results highlight the challenges and opportunities of continual object detection for agricultural applications. In particular, we hypothesize that the large intra-class and small inter-class variability that is typical of plant images exacerbate the difficulty of learning new categories without interfering with previous knowledge. We publicly release our code to encourage future work.

</details>

### Decision Boundary Optimization for Few-shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00376) · 📚 被引 7
- **作者**: Chenxu Guo, Qi Zhao, Shuchang Lyu, Binghao Liu, Chunlei Wang, Lijiang Chen et al.
- **🏷️ 机构**: Beihang University,Department of Electronic Information Engineering, University of Liverpool,Department of Computer Science
- **会议**: ICCV 2023

### Class-Incremental Learning using Diffusion Model for Distillation and Replay.
- **链接**: [arXiv:2306.17560](https://arxiv.org/abs/2306.17560) · 📚 被引 40
- **作者**: Quentin Jodelet, Xin Liu, Yin Jun Phua, Tsuyoshi Murata
- **🏷️ 机构**: Tokyo Institute of Technology,Department of Computer Science,Japan, AIST,Artificial Intelligence Research Center,Japan
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning aims to learn new classes in an incremental fashion without forgetting the previously learned ones. Several research works have shown how additional data can be used by incremental models to help mitigate catastrophic forgetting. In this work, following the recent breakthrough in text-to-image generative models and their wide distribution, we propose the use of a pretrained Stable Diffusion model as a source of additional data for class-incremental learning. Compared to competitive methods that rely on external, often unlabeled, datasets of real images, our approach can generate synthetic samples belonging to the same classes as the previously encountered images. This allows us to use those additional data samples not only in the distillation loss but also for replay in the classification loss. Experiments on the competitive benchmarks CIFAR100, ImageNet-Subset, and ImageNet demonstrate how this new approach can be used to further improve the performance of state-of-the-art methods for class-incremental learning on large scale datasets.

</details>

### SATHUR: Self Augmenting Task Hallucinal Unified Representation for Generalized Class Incremental Learning.
- **链接**: [arXiv:2311.18630](https://arxiv.org/abs/2311.18630) · 📚 被引 0
- **作者**: Sathursan Kanagarajah, Thanuja D. Ambegoda, Ranga Rodrigo
- **🏷️ 机构**: University of Moratuwa,Sri Lanka
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class Incremental Learning (CIL) is inspired by the human ability to learn new classes without forgetting previous ones. CIL becomes more challenging in real-world scenarios when the samples in each incremental step are imbalanced. This creates another branch of problem, called Generalized Class Incremental Learning (GCIL) where each incremental step is structured more realistically. Grow When Required (GWR) network, a type of Self-Organizing Map (SOM), dynamically create and remove nodes and edges for adaptive learning. GWR performs incremental learning from feature vectors extracted by a Convolutional Neural Network (CNN), which acts as a feature extractor. The inherent ability of GWR to form distinct clusters, each corresponding to a class in the feature vector space, regardless of the order of samples or class imbalances, is well suited to achieving GCIL. To enhance GWR's classification performance, a high-quality feature extractor is required. However, when the convolutional layers are adapted at each incremental step, the GWR nodes corresponding to prior knowledge are subject to near-invalidation. This work introduces the Self Augmenting Task Hallucinal Unified Representation (SATHUR), which re-initializes the GWR network at each incremental step, aligning it with the current feature extractor. Comprehensive experimental results demonstrate that our proposed method significantly outperforms other state-of-the-art GCIL methods on CIFAR-100 and CORe50 datasets.

</details>

### Clustering-based Domain-Incremental Learning.
- **链接**: [arXiv:2309.12078](https://arxiv.org/abs/2309.12078)
- **作者**: Christiaan Lamers, René Vidal, Nabil Belbachir, Niki van Stein, Thomas Bäck, Paris Giampouras
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We consider the problem of learning multiple tasks in a continual learning setting in which data from different tasks is presented to the learner in a streaming fashion. A key challenge in this setting is the so-called "catastrophic forgetting problem", in which the performance of the learner in an "old task" decreases when subsequently trained on a "new task". Existing continual learning methods, such as Averaged Gradient Episodic Memory (A-GEM) and Orthogonal Gradient Descent (OGD), address catastrophic forgetting by minimizing the loss for the current task without increasing the loss for previous tasks. However, these methods assume the learner knows when the task changes, which is unrealistic in practice. In this paper, we alleviate the need to provide the algorithm with information about task changes by using an online clustering-based approach on a dynamically updated finite pool of samples or gradients. We thereby successfully counteract catastrophic forgetting in one of the hardest settings, namely: domain-incremental learning, a setting for which the problem was previously unsolved. We showcase the benefits of our approach by applying these ideas to projection-based methods, such as A-GEM and OGD, which lead to task-agnostic versions of them. Experiments on real datasets demonstrate the effectiveness of the proposed strategy and its promising performance compared to state-of-the-art methods.

</details>

### TKIL: Tangent Kernel Optimization for Class Balanced Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00379) · 📚 被引 12
- **作者**: Jinlin Xiang, Eli Shlizerman
- **🏷️ 机构**: University of Washington,Department of Electrical &#x0026; Computer Engineering,Seattle,USA, University of Washington,Department of Electrical &#x0026; Computer Engineering, Department of Applied Mathematics,Seattle,USA
- **会议**: ICCV 2023

### OpenIncrement: A Unified Framework for Open Set Recognition and Deep Class-Incremental Learning.
- **链接**: [arXiv:2310.03848](https://arxiv.org/abs/2310.03848) · 📚 被引 6
- **作者**: Jiawen Xu, Claas Grohnfeldt, Odej Kao
- **🏷️ 机构**: Technical University Berlin, Huawei Munich Research Center
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In most works on deep incremental learning research, it is assumed that novel samples are pre-identified for neural network retraining. However, practical deep classifiers often misidentify these samples, leading to erroneous predictions. Such misclassifications can degrade model performance. Techniques like open set recognition offer a means to detect these novel samples, representing a significant area in the machine learning domain. In this paper, we introduce a deep class-incremental learning framework integrated with open set recognition. Our approach refines class-incrementally learned features to adapt them for distance-based open set recognition. Experimental results validate that our method outperforms state-of-the-art incremental learning techniques and exhibits superior performance in open set recognition compared to baseline methods.

</details>
