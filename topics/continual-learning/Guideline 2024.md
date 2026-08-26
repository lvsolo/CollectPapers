# Continual Learning — 2024 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 30 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts Adapters.
- **链接**: [arXiv:2403.11549](https://arxiv.org/abs/2403.11549) · [代码](https://github.com/JiazuoYu/MoE-Adapters4CL) · 📚 被引 115
- **作者**: Jiazuo Yu, Yunzhi Zhuge, Lu Zhang, Ping Hu, Dong Wang, Huchuan Lu et al.
- **🏷️ 机构**: Dalian University of Technology,China, University of Electronic Science and Technology of China, Tsinghua University,China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Continual learning can empower vision-language models to continuously acquire new knowledge, without the need for access to the entire historical dataset. However, mitigating the performance degradation in large-scale models is non-trivial due to (i) parameter shifts throughout lifelong learning and (ii) significant computational burdens associated with full-model tuning. In this work, we present a parameter-efficient continual learning framework to alleviate long-term forgetting in incremental learning with vision-language models. Our approach involves the dynamic expansion of a pre-trained CLIP model, through the integration of Mixture-of-Experts (MoE) adapters in response to new tasks. To preserve the zero-shot recognition capability of vision-language models, we further introduce a Distribution Discriminative Auto-Selector (DDAS) that automatically routes in-distribution and out-of-distribution inputs to the MoE Adapter and the original CLIP, respectively. Through extensive experiments across various settings, our proposed method consistently outperforms previous state-of-the-art approaches while concurrently reducing parameter training burdens by 60%. Our code locates at https://github.com/JiazuoYu/MoE-Adapters4CL

### Continual Learning for Motion Prediction Model via Meta-Representation Learning and Optimal Memory Buffer Retention Strategy.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01462) · 📚 被引 9
- **作者**: Daejun Kang, Dongsuk Kum, Sanmin Kim
- **🏷️ 机构**: Korea Automotive Technology Institute, Korea Advanced Institute of Science and Technology
- **会议**: CVPR 2024

### Learning Equi-Angular Representations for Online Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02259) · 📚 被引 15
- **作者**: Minhyuk Seo, Hyunseo Koh, Wonje Jeung, Minjae Lee, San Kim, Hankook Lee et al.
- **🏷️ 机构**: Yonsei Univ., LG AI Research
- **会议**: CVPR 2024

### Improving Plasticity in Online Continual Learning via Collaborative Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02214) · 📚 被引 11
- **作者**: Maorong Wang, Nicolas Michel, Ling Xiao, Toshihiko Yamasaki
- **🏷️ 机构**: The University of Tokyo, Univ Gustave Eiffel, CNRS, LIGM
- **会议**: CVPR 2024

### BrainWash: A Poisoning Attack to Forget in Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02271) · 📚 被引 7
- **作者**: Ali Abbasi, Parsa Nooralinejad, Hamed Pirsiavash, Soheil Kolouri
- **🏷️ 机构**: Vanderbilt University, University of California,Davis
- **会议**: CVPR 2024

### Towards Backward-Compatible Continual Learning of Image Compression.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02415) · 📚 被引 6
- **作者**: Zhihao Duan, Ming Lu, Justin Yang, Jiangpeng He, Zhan Ma, Fengqing Zhu
- **🏷️ 机构**: Purdue University,West Lafayette,Indiana,U.S.A., Nanjing University,Nanjing,Jiangsu,China
- **会议**: CVPR 2024

### Consistent Prompting for Rehearsal-Free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02689) · 📚 被引 42
- **作者**: Zhanxin Gao, Jun Cen, Xiaobin Chang
- **🏷️ 机构**: School of Artificial Intelligence, Sun Yat-sen University,China, Cheng Kar-Shun Robotics Institute, The Hong Kong University of Science and Technology,China
- **会议**: CVPR 2024

### Resurrecting Old Classes with New Data for Exemplar-Free Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02695) · 📚 被引 24
- **作者**: Dipam Goswami, Albin Soutif-Cormerais, Yuyang Liu, Sandesh Kamath, Bartlomiej Twardowski, Joost van de Weijer
- **🏷️ 机构**: Universitat Aut&#x00F2;noma de Barcelona,Department of Computer Science, University of Chinese Academy of Sciences
- **会议**: CVPR 2024

### ECLIPSE: Efficient Continual Learning in Panoptic Segmentation with Visual Prompt Tuning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00322) · 📚 被引 23
- **作者**: Beomyoung Kim, Joonsang Yu, Sung Ju Hwang
- **🏷️ 机构**: NAVER Cloud, ImageVision, KAIST
- **会议**: CVPR 2024

### InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning.
- **链接**: [arXiv:2404.00228](https://arxiv.org/abs/2404.00228) · 📚 被引 73
- **作者**: Yan-Shuo Liang, Wu-Jun Li
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology,Department of Computer Science and Technology,P. R. China
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Continual learning requires the model to learn multiple tasks sequentially. In continual learning, the model should possess the ability to maintain its performance on old tasks (stability) and the ability to adapt to new tasks continuously (plasticity). Recently, parameter-efficient fine-tuning (PEFT), which involves freezing a pre-trained model and injecting a small number of learnable parameters to adapt to downstream tasks, has gained increasing popularity in continual learning. Although existing continual learning methods based on PEFT have demonstrated superior performance compared to those not based on PEFT, most of them do not consider how to eliminate the interference of the new task on the old tasks, which inhibits the model from making a good trade-off between stability and plasticity. In this work, we propose a new PEFT method, called interference-free low-rank adaptation (InfLoRA), for continual learning. InfLoRA injects a small number of parameters to reparameterize the pre-trained weights and shows that fine-tuning these injected parameters is equivalent to fine-tuning the pre-trained weights within a subspace. Furthermore, InfLoRA designs this subspace to eliminate the interference of the new task on the old tasks, making a good trade-off between stability and plasticity. Experimental results show that InfLoRA outperforms existing state-of-the-art continual learning methods on multiple datasets.

### Enhancing Visual Continual Learning with Language-Guided Supervision.
- **链接**: [arXiv:2403.16124](https://arxiv.org/abs/2403.16124) · 📚 被引 15
- **作者**: Bolin Ni, Hongbo Zhao, Chenghao Zhang, Ke Hu, Gaofeng Meng, Zhaoxiang Zhang et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences,State Key Laboratory of Multimodal Artificial Intelligence Systems, University of Chinese Academy of Sciences,School of Artificial Intelligence
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Continual learning (CL) aims to empower models to learn new tasks without forgetting previously acquired knowledge. Most prior works concentrate on the techniques of architectures, replay data, regularization, \etc. However, the category name of each class is largely neglected. Existing methods commonly utilize the one-hot labels and randomly initialize the classifier head. We argue that the scarce semantic information conveyed by the one-hot labels hampers the effective knowledge transfer across tasks. In this paper, we revisit the role of the classifier head within the CL paradigm and replace the classifier with semantic knowledge from pretrained language models (PLMs). Specifically, we use PLMs to generate semantic targets for each class, which are frozen and serve as supervision signals during training. Such targets fully consider the semantic correlation between all classes across tasks. Empirical studies show that our approach mitigates forgetting by alleviating representation drifting and facilitating knowledge transfer across tasks. The proposed method is simple to implement and can seamlessly be plugged into existing methods with negligible adjustments. Extensive experiments based on eleven mainstream baselines demonstrate the effectiveness and generalizability of our approach to various protocols. For example, under the class-incremental learning setting on ImageNet-100, our method significantly improves the Top-1 accuracy by 3.2\% to 6.1\% while reducing the forgetting rate by 2.6\% to 13.1\%.

### Adaptive VIO: Deep Visual-Inertial Odometry with Online Continual Learning.
- **链接**: [arXiv:2405.16754](https://arxiv.org/abs/2405.16754) · 📚 被引 24
- **作者**: Youqi Pan, Wugen Zhou, Yingdian Cao, Hongbin Zha
- **🏷️ 机构**: Institute for AI, School of IST PKU-SenseTime Joint Lab of MV Peking University,National Key Lab of GAI
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Visual-inertial odometry (VIO) has demonstrated remarkable success due to its low-cost and complementary sensors. However, existing VIO methods lack the generalization ability to adjust to different environments and sensor attributes. In this paper, we propose Adaptive VIO, a new monocular visual-inertial odometry that combines online continual learning with traditional nonlinear optimization. Adaptive VIO comprises two networks to predict visual correspondence and IMU bias. Unlike end-to-end approaches that use networks to fuse the features from two modalities (camera and IMU) and predict poses directly, we combine neural networks with visual-inertial bundle adjustment in our VIO system. The optimized estimates will be fed back to the visual and IMU bias networks, refining the networks in a self-supervised manner. Such a learning-optimization-combined framework and feedback mechanism enable the system to perform online continual learning. Experiments demonstrate that our Adaptive VIO manifests adaptive capability on EuRoC and TUM-VI datasets. The overall performance exceeds the currently known learning-based VIO methods and is comparable to the state-of-the-art optimization-based methods.

### Interactive Continual Learning: Fast and Slow Thinking.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01224) · 📚 被引 23
- **作者**: Biqing Qi, Xinquan Chen, Junqi Gao, Dong Li, Jianxing Liu, Ligang Wu et al.
- **🏷️ 机构**: Harbin Institute of Technology,Department of Control Science and Engineering, School of Mathematics, Harbin Institute of Technology
- **会议**: CVPR 2024

### Convolutional Prompting meets Language Models for Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02229) · 📚 被引 24
- **作者**: Anurag Roy, Riddhiman Moulick, Vinay Kumar Verma, Saptarshi Ghosh, Abir Das
- **🏷️ 机构**: IIT Kharagpur, IML Amazon India
- **会议**: CVPR 2024

### Traceable Federated Continual Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01223) · 📚 被引 18
- **作者**: Qiang Wang, Bingyan Liu, Yawen Li
- **🏷️ 机构**: School of Computer Science, Beijing University of Posts and Telecommunications, School of Economics and Management, Beijing University of Posts and Telecommunications
- **会议**: CVPR 2024

### Orchestrate Latent Expertise: Advancing Online Continual Learning with Multi-Level Supervision and Reverse Self-Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02234) · 📚 被引 20
- **作者**: Hongwei Yan, Liyuan Wang, Kaisheng Ma, Yi Zhong
- **🏷️ 机构**: School of Life Sciences, IDG/McGovern Institute for Brain Research, Tsinghua University, Institute for AI, BNRist Center, Tsinghua-Bosch Joint ML Center, Tsinghua University,THBI Lab,Dept. of Comp. Sci. &#x0026; Tech., Institute for Interdisciplinary Information Sciences, Tsinghua University
- **会议**: CVPR 2024

### RCL: Reliable Continual Learning for Unified Failure Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01154) · 📚 被引 5
- **作者**: Fei Zhu, Zhen Cheng, Xu-Yao Zhang, Cheng-Lin Liu, Zhaoxiang Zhang
- **🏷️ 机构**: Centre for Artificial Intelligence and Robotics, HKISI-CAS, CASIA,State Key Laboratory of Multimodal Artificial Intelligence Systems
- **会议**: CVPR 2024

### Expandable Subspace Ensemble for Pre-Trained Model-Based Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02223) · 📚 被引 118
- **作者**: Da-Wei Zhou, Hai-Long Sun, Han-Jia Ye, De-Chuan Zhan
- **🏷️ 机构**: Nanjing University China School of Artificial Intelligence, Nanjing University,National Key Laboratory for Novel Software Technology,China
- **会议**: CVPR 2024

### Towards Efficient Replay in Federated Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01218) · 📚 被引 34
- **作者**: Yichen Li, Qunwei Li, Haozhao Wang, Ruixuan Li, Wenliang Zhong, Guannan Zhang
- **🏷️ 机构**: Huazhong University of Science and Technology,China, Ant Group,China
- **会议**: CVPR 2024

### OrCo: Towards Better Generalization via Orthogonality and Contrast for Few-Shot Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02717) · 📚 被引 52
- **作者**: Noor Ahmed, Anna Kukleva, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2024

### NICE: Neurogenesis Inspired Contextual Encoding for Replay-free Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02233) · 📚 被引 5
- **作者**: Mustafa Burak Gurbuz, Jean Michael Moorman, Constantine Dovrolis
- **🏷️ 机构**: Georgia Institute of Technology,USA, The Cyprus Institute, Cyprus Georgia Institute of Technology,USA
- **会议**: CVPR 2024

### Gradient Reweighting: Towards Imbalanced Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01577) · 📚 被引 65
- **作者**: Jiangpeng He
- **🏷️ 机构**: Elmore Family School of Electrical and Computer Engineering, Purdue University,USA
- **会议**: CVPR 2024

### DYSON: Dynamic Feature Space Self-Organization for Online Task-Free Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02241) · 📚 被引 10
- **作者**: Yuhang He, Yingjie Chen, Yuhan Jin, Songlin Dong, Xing Wei, Yihong Gong
- **🏷️ 机构**: College of Artificial Intelligence, Xi&#x0027;an Jiaotong University, School of Software Engineering, Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2024

### FCS: Feature Calibration and Separation for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02692) · 📚 被引 29
- **作者**: Qiwei Li, Yuxin Peng, Jiahuan Zhou
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China,100871
- **会议**: CVPR 2024

### Task-Adaptive Saliency Guidance for Exemplar-Free Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02261) · 📚 被引 8
- **作者**: Xialei Liu, Jiang-Tian Zhai, Andrew D. Bagdanov, Ke Li, Ming-Ming Cheng
- **🏷️ 机构**: NKIARI, Shenzhen Futian, VCIP, CS, Nankai University, MICC, University of Florence
- **会议**: CVPR 2024

### Dual-Enhanced Coreset Selection with Class-Wise Collaboration for Online Blurry Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02265) · 📚 被引 3
- **作者**: Yutian Luo, Shiqi Zhao, Haoran Wu, Zhiwu Lu
- **🏷️ 机构**: Gaoling School of Artificial Intelligence, Renmin University of China,Beijing,China, China Unicom Research Institute,Beijing,China
- **会议**: CVPR 2024

### Dual-Consistency Model Inversion for Non-Exemplar Class Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02268) · 📚 被引 11
- **作者**: Zihuan Qiu, Yi Xu, Fanman Meng, Hongliang Li, Linfeng Xu, Qingbo Wu
- **🏷️ 机构**: University of Electronic Science and Technology of China, Dalian University of Technology
- **会议**: CVPR 2024

### Text-Enhanced Data-Free Approach for Federated Class-Incremental Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02253) · 📚 被引 15
- **作者**: Minh-Tuan Tran, Trung Le, Xuan-May Le, Mehrtash Harandi, Dinh Phung
- **🏷️ 机构**: Monash University, University of Melbourne
- **会议**: CVPR 2024

### Long-Tail Class Incremental Learning via Independent SUb-Prototype Construction.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02702) · 📚 被引 13
- **作者**: Xi Wang, Xu Yang, Jie Yin, Kun Wei, Cheng Deng
- **🏷️ 机构**: School of Electronic Engineering, Xidian University,Xi&#x0027;an,China,710071
- **会议**: CVPR 2024

### Class Incremental Learning with Multi-Teacher Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02687)
- **作者**: Haitao Wen, Lili Pan, Yu Dai, Heqian Qiu, Lanxiao Wang, Qingbo Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024
