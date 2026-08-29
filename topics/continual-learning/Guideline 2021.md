# Continual Learning — 2021 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Wanderlust: Online Continual Object Detection in the Real World.
- **链接**: [arXiv:2108.11005](https://arxiv.org/abs/2108.11005) · 📚 被引 50
- **作者**: Jianren Wang, Xin Wang, Yue Shang-Guan, Abhinav Gupta
- **🏷️ 机构**: Carnegie Mellon University, Microsoft Research, University of Texas,Austin
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Online continual learning from data streams in dynamic environments is a critical direction in the computer vision field. However, realistic benchmarks and fundamental studies in this line are still missing. To bridge the gap, we present a new online continual object detection benchmark with an egocentric video dataset, Objects Around Krishna (OAK). OAK adopts the KrishnaCAM videos, an ego-centric video stream collected over nine months by a graduate student. OAK provides exhaustive bounding box annotations of 80 video snippets (~17.5 hours) for 105 object categories in outdoor scenes. The emergence of new object categories in our benchmark follows a pattern similar to what a single person might see in their day-to-day life. The dataset also captures the natural distribution shifts as the person travels to different places. These egocentric long-running videos provide a realistic playground for continual learning algorithms, especially in online embodied settings. We also introduce new evaluation metrics to evaluate the model performance and catastrophic forgetting and provide baseline studies for online continual object detection. We believe this benchmark will pose new exciting challenges for learning from non-stationary data in continual learning. The OAK dataset and the associated benchmark are released at https://oakdata.github.io/.

</details>

### Co2L: Contrastive Continual Learning.
- **链接**: [arXiv:2106.14413](https://arxiv.org/abs/2106.14413)
- **作者**: Hyuntak Cha, Jaeho Lee, Jinwoo Shin
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent breakthroughs in self-supervised learning show that such algorithms learn visual representations that can be transferred better to unseen tasks than joint-training methods relying on task-specific supervision. In this paper, we found that the similar holds in the continual learning con-text: contrastively learned representations are more robust against the catastrophic forgetting than jointly trained representations. Based on this novel observation, we propose a rehearsal-based continual learning algorithm that focuses on continually learning and maintaining transferable representations. More specifically, the proposed scheme (1) learns representations using the contrastive learning objective, and (2) preserves learned representations using a self-supervised distillation step. We conduct extensive experimental validations under popular benchmark image classification datasets, where our method sets the new state-of-the-art performance.

</details>

### Class-Incremental Learning for Action Recognition in Videos.
- **链接**: [arXiv:2203.13611](https://arxiv.org/abs/2203.13611) · 📚 被引 52
- **作者**: Jaeyoo Park, Minsoo Kang, Bohyung Han
- **🏷️ 机构**: Seoul National University,ECE &#x0026; ASRI
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle catastrophic forgetting problem in the context of class-incremental learning for video recognition, which has not been explored actively despite the popularity of continual learning. Our framework addresses this challenging task by introducing time-channel importance maps and exploiting the importance maps for learning the representations of incoming examples via knowledge distillation. We also incorporate a regularization scheme in our objective function, which encourages individual features obtained from different time steps in a video to be uncorrelated and eventually improves accuracy by alleviating catastrophic forgetting. We evaluate the proposed approach on brand-new splits of class-incremental action recognition benchmarks constructed upon the UCF101, HMDB51, and Something-Something V2 datasets, and demonstrate the effectiveness of our algorithm in comparison to the existing continual learning methods that are originally designed for image data.

</details>

### Online Continual Learning with Natural Distribution Shifts: An Empirical Study with Visual Data.
- **链接**: [arXiv:2108.09020](https://arxiv.org/abs/2108.09020) · [代码](https://github.com/IntelLabs/continuallearning) · 📚 被引 37
- **作者**: Zhipeng Cai, Ozan Sener, Vladlen Koltun
- **🏷️ 机构**: Intel Labs
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual learning is the problem of learning and retaining knowledge through time over multiple tasks and environments. Research has primarily focused on the incremental classification setting, where new tasks/classes are added at discrete time intervals. Such an "offline" setting does not evaluate the ability of agents to learn effectively and efficiently, since an agent can perform multiple learning epochs without any time limitation when a task is added. We argue that "online" continual learning, where data is a single continuous stream without task boundaries, enables evaluating both information retention and online learning efficacy. In online continual learning, each incoming small batch of data is first used for testing and then added to the training set, making the problem truly online. Trained models are later evaluated on historical data to assess information retention. We introduce a new benchmark for online continual visual learning that exhibits large scale and natural distribution shifts. Through a large-scale analysis, we identify critical and previously unobserved phenomena of gradient-based optimization in continual learning, and propose effective strategies for improving gradient-based online continual learning with real data. The source code and dataset are available in: https://github.com/IntelLabs/continuallearning.

</details>

### Continual Learning on Noisy Data Streams via Self-Purified Replay.
- **链接**: [arXiv:2110.07735](https://arxiv.org/abs/2110.07735) · 📚 被引 35
- **作者**: Chris Dongjoo Kim, Jinseo Jeong, Sangwoo Moon, Gunhee Kim
- **🏷️ 机构**: Seoul National University,Department of Computer Science and Engineering,Seoul,Korea
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continually learning in the real world must overcome many challenges, among which noisy labels are a common and inevitable issue. In this work, we present a repla-ybased continual learning framework that simultaneously addresses both catastrophic forgetting and noisy labels for the first time. Our solution is based on two observations; (i) forgetting can be mitigated even with noisy labels via self-supervised learning, and (ii) the purity of the replay buffer is crucial. Building on this regard, we propose two key components of our method: (i) a self-supervised replay technique named Self-Replay which can circumvent erroneous training signals arising from noisy labeled data, and (ii) the Self-Centered filter that maintains a purified replay buffer via centrality-based stochastic graph ensembles. The empirical results on MNIST, CIFAR-10, CIFAR-100, and WebVision with real-world noise demonstrate that our framework can maintain a highly pure replay buffer amidst noisy streamed data while greatly outperforming the combinations of the state-of-the-art continual learning and noisy label learning methods. The source code is available at http://vision.snu.ac.kr/projects/SPR

</details>

### Few-Shot and Continual Learning with Attentive Independent Mechanisms.
- **链接**: [arXiv:2107.14053](https://arxiv.org/abs/2107.14053) · [代码](https://github.com/huang50213/AIM-Fewshot-Continual) · 📚 被引 27
- **作者**: Eugene Lee, Cheng-Han Huang, Chen-Yi Lee
- **🏷️ 机构**: National Chiao Tung University,Institute of Electronics,Hsinchu,Taiwan
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep neural networks (DNNs) are known to perform well when deployed to test distributions that shares high similarity with the training distribution. Feeding DNNs with new data sequentially that were unseen in the training distribution has two major challenges -- fast adaptation to new tasks and catastrophic forgetting of old tasks. Such difficulties paved way for the on-going research on few-shot learning and continual learning. To tackle these problems, we introduce Attentive Independent Mechanisms (AIM). We incorporate the idea of learning using fast and slow weights in conjunction with the decoupling of the feature extraction and higher-order conceptual learning of a DNN. AIM is designed for higher-order conceptual learning, modeled by a mixture of experts that compete to learn independent concepts to solve a new task. AIM is a modular component that can be inserted into existing deep learning frameworks. We demonstrate its capability for few-shot learning by adding it to SIB and trained on MiniImageNet and CIFAR-FS, showing significant improvement. AIM is also applied to ANML and OML trained on Omniglot, CIFAR-100 and MiniImageNet to demonstrate its capability in continual learning. Code made publicly available at https://github.com/huang50213/AIM-Fewshot-Continual.

</details>

### RECALL: Replay-based Continual Learning in Semantic Segmentation.
- **链接**: [arXiv:2108.03673](https://arxiv.org/abs/2108.03673) · 📚 被引 134
- **作者**: Andrea Maracani, Umberto Michieli, Marco Toldo, Pietro Zanuttigh
- **🏷️ 机构**: University of Padova,Department of Information Engineering
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep networks allow to obtain outstanding results in semantic segmentation, however they need to be trained in a single shot with a large amount of data. Continual learning settings where new classes are learned in incremental steps and previous training data is no longer available are challenging due to the catastrophic forgetting phenomenon. Existing approaches typically fail when several incremental steps are performed or in presence of a distribution shift of the background class. We tackle these issues by recreating no longer available data for the old classes and outlining a content inpainting scheme on the background class. We propose two sources for replay data. The first resorts to a generative adversarial network to sample from the class space of past learning steps. The second relies on web-crawled data to retrieve images containing examples of old classes from online databases. In both scenarios no samples of past steps are stored, thus avoiding privacy concerns. Replay data are then blended with new samples during the incremental steps. Our approach, RECALL, outperforms state-of-the-art methods.

</details>

### Detection and Continual Learning of Novel Face Presentation Attacks.
- **链接**: [arXiv:2108.12081](https://arxiv.org/abs/2108.12081) · 📚 被引 41
- **作者**: Mohammad Rostami, Leonidas Spinoulas, Mohamed E. Hussein, Joe Mathai, Wael Abd-Almageed
- **🏷️ 机构**: USC Information Sciences Institute,Los Angeles,CA,USA,90292
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Advances in deep learning, combined with availability of large datasets, have led to impressive improvements in face presentation attack detection research. However, state-of-the-art face antispoofing systems are still vulnerable to novel types of attacks that are never seen during training. Moreover, even if such attacks are correctly detected, these systems lack the ability to adapt to newly encountered attacks. The post-training ability of continually detecting new types of attacks and self-adaptation to identify these attack types, after the initial detection phase, is highly appealing. In this paper, we enable a deep neural network to detect anomalies in the observed input data points as potential new types of attacks by suppressing the confidence-level of the network outside the training samples' distribution. We then use experience replay to update the model to incorporate knowledge about new types of attacks without forgetting the past learned attack types. Experimental results are provided to demonstrate the effectiveness of the proposed method on two benchmark datasets as well as a newly introduced dataset which exhibits a large variety of attack types.

</details>

### Rehearsal revealed: The limits and merits of revisiting samples in continual learning.
- **链接**: [arXiv:2104.07446](https://arxiv.org/abs/2104.07446) · 📚 被引 61
- **作者**: Eli Verwimp, Matthias De Lange, Tinne Tuytelaars
- **🏷️ 机构**: KU,Leuven
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning from non-stationary data streams and overcoming catastrophic forgetting still poses a serious challenge for machine learning research. Rather than aiming to improve state-of-the-art, in this work we provide insight into the limits and merits of rehearsal, one of continual learning's most established methods. We hypothesize that models trained sequentially with rehearsal tend to stay in the same low-loss region after a task has finished, but are at risk of overfitting on its sample memory, hence harming generalization. We provide both conceptual and strong empirical evidence on three benchmarks for both behaviors, bringing novel insights into the dynamics of rehearsal and continual learning in general. Finally, we interpret important continual learning works in the light of our findings, allowing for a deeper understanding of their successes.

</details>

### Continual Learning for Image-Based Camera Localization.
- **链接**: [arXiv:2108.09112](https://arxiv.org/abs/2108.09112) · 📚 被引 26
- **作者**: Shuzhe Wang, Zakaria Laskar, Iaroslav Melekhov, Xiaotian Li, Juho Kannala
- **🏷️ 机构**: Aalto University
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> For several emerging technologies such as augmented reality, autonomous driving and robotics, visual localization is a critical component. Directly regressing camera pose/3D scene coordinates from the input image using deep neural networks has shown great potential. However, such methods assume a stationary data distribution with all scenes simultaneously available during training. In this paper, we approach the problem of visual localization in a continual learning setup -- whereby the model is trained on scenes in an incremental manner. Our results show that similar to the classification domain, non-stationary data induces catastrophic forgetting in deep networks for visual localization. To address this issue, a strong baseline based on storing and replaying images from a fixed buffer is proposed. Furthermore, we propose a new sampling method based on coverage score (Buff-CS) that adapts the existing sampling strategies in the buffering process to the problem of visual localization. Results demonstrate consistent improvements over standard buffering methods on two challenging datasets -- 7Scenes, 12Scenes, and also 19Scenes by combining the former scenes.

</details>

### SS-IL: Separated Softmax for Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00088) · 📚 被引 167
- **作者**: Hongjoon Ahn, Jihwan Kwak, Subin Lim, Hyeonsu Bang, Hyojun Kim, Taesup Moon
- **🏷️ 机构**: Sungkyunkwan University,Department of Artificial Intelligence,Suwon,Korea, Seoul National University,Department of Electrical and Computer Engineering,Seoul,Korea, Sungkyunkwan University,Department of Computer Engineering,Suwon,Korea
- **会议**: ICCV 2021

### Synthesized Feature based Few-Shot Class-Incremental Learning on a Mixture of Subspaces.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00854) · 📚 被引 64
- **作者**: Ali Cheraghian, Shafin Rahman, Sameera Ramasinghe, Pengfei Fang, Christian Simon, Lars Petersson et al.
- **🏷️ 机构**: Australian National University,Australia, North South University,Dhaka,Bangladesh, Data61-Csiro,Australia
- **会议**: ICCV 2021

### Always Be Dreaming: A New Approach for Data-Free Class-Incremental Learning.
- **链接**: [arXiv:2106.09701](https://arxiv.org/abs/2106.09701) · 📚 被引 137
- **作者**: James Seale Smith, Yen-Chang Hsu, Jonathan C. Balloch, Yilin Shen, Hongxia Jin, Zsolt Kira
- **🏷️ 机构**: Georgia Institute of Technology, Samsung Research America
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern computer vision applications suffer from catastrophic forgetting when incrementally learning new concepts over time. The most successful approaches to alleviate this forgetting require extensive replay of previously seen data, which is problematic when memory constraints or data legality concerns exist. In this work, we consider the high-impact problem of Data-Free Class-Incremental Learning (DFCIL), where an incremental learning agent must learn new concepts over time without storing generators or training data from past tasks. One approach for DFCIL is to replay synthetic images produced by inverting a frozen copy of the learner's classification model, but we show this approach fails for common class-incremental benchmarks when using standard distillation strategies. We diagnose the cause of this failure and propose a novel incremental distillation strategy for DFCIL, contributing a modified cross-entropy training and importance-weighted feature distillation, and show that our method results in up to a 25.1% increase in final task accuracy (absolute difference) compared to SOTA DFCIL methods for common class-incremental benchmarks. Our method even outperforms several standard replay based methods which store a coreset of images.

</details>

### Striking a Balance between Stability and Plasticity for Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00116) · 📚 被引 45
- **作者**: Guile Wu, Shaogang Gong, Pan Li
- **🏷️ 机构**: Mary University of London
- **会议**: ICCV 2021
