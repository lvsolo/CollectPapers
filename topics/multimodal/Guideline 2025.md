# Multimodal — 2025 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 120 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Fusion Meets Diverse Conditions: A High-Diversity Benchmark and Baseline for UAV-Based Multimodal Object Detection with Condition Cues.
- **链接**: [arXiv:2510.13620](https://arxiv.org/abs/2510.13620) · 📚 被引 5
- **作者**: Chen Chen, Kangcheng Bin, Ting Hu, Jiahao Qi, Xingyue Liu, Tianpeng Liu et al.
- **🏷️ 机构**: National University of Defense Technology,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unmanned aerial vehicles (UAV)-based object detection with visible (RGB) and infrared (IR) images facilitates robust around-the-clock detection, driven by advancements in deep learning techniques and the availability of high-quality dataset. However, the existing dataset struggles to fully capture real-world complexity for limited imaging conditions. To this end, we introduce a high-diversity dataset ATR-UMOD covering varying scenarios, spanning altitudes from 80m to 300m, angles from 0° to 75°, and all-day, all-year time variations in rich weather and illumination conditions. Moreover, each RGB-IR image pair is annotated with 6 condition attributes, offering valuable high-level contextual information. To meet the challenge raised by such diverse conditions, we propose a novel prompt-guided condition-aware dynamic fusion (PCDF) to adaptively reassign multimodal contributions by leveraging annotated condition cues. By encoding imaging conditions as text prompts, PCDF effectively models the relationship between conditions and multimodal contributions through a task-specific soft-gating transformation. A prompt-guided condition-decoupling module further ensures the availability in practice without condition annotations. Experiments on ATR-UMOD dataset reveal the effectiveness of PCDF.

</details>

### MA-CIR: A Multimodal Arithmetic Benchmark for Composed Image Retrieval.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01982) · 📚 被引 0
- **作者**: Jaeseok Byun, Young Kyun Jang, Seokhyeon Jeong, Donghyun Kim, Taesup Moon
- **🏷️ 机构**: Seoul National University,Department of ECE, Google Deepmind, Korea University,Department of AI
- **会议**: ICCV 2025

### MISSRAG: Addressing the Missing Modality Challenge in Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00308)
- **作者**: Vittorio Pipoli, Alessia Saporita, Federico Bolelli, Marcella Cornia, Lorenzo Baraldi, Costantino Grana et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### GRAB: A Challenging Graph Analysis Benchmark for Large Multimodal Models.
- **链接**: [arXiv:2408.11817](https://arxiv.org/abs/2408.11817) · 📚 被引 0
- **作者**: Jonathan Roberts, Kai Han, Samuel Albanie
- **🏷️ 机构**: University of Cambridge, The University of Hong Kong
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multimodal models (LMMs) have exhibited proficiencies across many visual tasks. Although numerous well-known benchmarks exist to evaluate model performance, they increasingly have insufficient headroom. As such, there is a pressing need for a new generation of benchmarks challenging enough for the next generation of LMMs. One area that LMMs show potential is graph analysis, specifically, the tasks an analyst might typically perform when interpreting figures such as estimating the mean, intercepts or correlations of functions and data series. In this work, we introduce GRAB, a graph analysis benchmark, fit for current and future frontier LMMs. Our benchmark is predominantly synthetic, ensuring high-quality, noise-free questions. GRAB is comprised of 3284 questions, covering five tasks and 23 graph properties. We evaluate 20 LMMs on GRAB, finding it to be a challenging benchmark, with the highest performing model attaining a score of just 21.0%. Finally, we conduct various ablations to investigate where the models succeed and struggle. We release GRAB and a lightweight GRAB-Lite to encourage progress in this important, growing domain.

</details>

### CC-OCR: A Comprehensive and Challenging OCR Benchmark for Evaluating Large Multimodal Models in Literacy.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02019) · 📚 被引 11
- **作者**: Zhibo Yang, Jun Tang, Zhaohai Li, Pengfei Wang, Jianqiang Wan, Humen Zhong et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, Alibaba Group
- **会议**: ICCV 2025

### LMM-Det: Make Large Multimodal Models Excel in Object Detection.
- **链接**: [arXiv:2507.18300](https://arxiv.org/abs/2507.18300) · [代码](https://github.com/360CVGroup/LMM-Det) · 📚 被引 1
- **作者**: Jincheng Li, Chunyu Xie, Ji Ao, Dawei Leng, Yuhui Yin
- **🏷️ 机构**: 360 AI Research, Beihang University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multimodal models (LMMs) have garnered wide-spread attention and interest within the artificial intelligence research and industrial communities, owing to their remarkable capability in multimodal understanding, reasoning, and in-context learning, among others. While LMMs have demonstrated promising results in tackling multimodal tasks like image captioning, visual question answering, and visual grounding, the object detection capabilities of LMMs exhibit a significant gap compared to specialist detectors. To bridge the gap, we depart from the conventional methods of integrating heavy detectors with LMMs and propose LMM-Det, a simple yet effective approach that leverages a Large Multimodal Model for vanilla object Detection without relying on specialized detection modules. Specifically, we conduct a comprehensive exploratory analysis when a large multimodal model meets with object detection, revealing that the recall rate degrades significantly compared with specialist detection models. To mitigate this, we propose to increase the recall rate by introducing data distribution adjustment and inference optimization tailored for object detection. We re-organize the instruction conversations to enhance the object detection capabilities of large multimodal models. We claim that a large multimodal model possesses detection capability without any extra detection modules. Extensive experiments support our claim and show the effectiveness of the versatile LMM-Det. The datasets, models, and codes are available at https://github.com/360CVGroup/LMM-Det.

</details>

### Rethinking Multi-Modal Object Detection From the Perspective of Mono-Modality Feature Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00600) · 📚 被引 9
- **作者**: Tianyi Zhao, Boyang Liu, Yanglei Gao, Yiming Sun, Maoxun Yuan, Xingxing Wei
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,China, Southeast University,China
- **会议**: ICCV 2025

### SMStracker: Tri-Path Score Mask Sigma Fusion for Multi-Modal Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00453) · 📚 被引 2
- **作者**: Sixian Chan, Zedong Li, Wenhao Li, Shijian Lu, Chunhua Shen, Xiaoqin Zhang
- **🏷️ 机构**: Zhejiang University of Technology,China, Nanyang Technological University,Singapore, Zhejiang University,China
- **会议**: ICCV 2025

### What You Have is What You Track: Adaptive and Robust Multimodal Tracking.
- **链接**: [arXiv:2507.05899](https://arxiv.org/abs/2507.05899) · [代码](https://github.com/supertyd/FlexTrack) · 📚 被引 5
- **作者**: Yuedong Tan, Jiawei Shao, Eduard Zamfir, Ruanjun Li, Zhaochong An, Chao Ma et al.
- **🏷️ 机构**: China Telecom,TeleAI, University of Wurzburg,Computer Vision Lab, CAIDAS &#x0026; IFI, ShanghaiTech University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal data is known to be helpful for visual tracking by improving robustness to appearance variations. However, sensor synchronization challenges often compromise data availability, particularly in video settings where shortages can be temporal. Despite its importance, this area remains underexplored. In this paper, we present the first comprehensive study on tracker performance with temporally incomplete multimodal data. Unsurprisingly, under such a circumstance, existing trackers exhibit significant performance degradation, as their rigid architectures lack the adaptability needed to effectively handle missing modalities. To address these limitations, we propose a flexible framework for robust multimodal tracking. We venture that a tracker should dynamically activate computational units based on missing data rates. This is achieved through a novel Heterogeneous Mixture-of-Experts fusion mechanism with adaptive complexity, coupled with a video-level masking strategy that ensures both temporal consistency and spatial completeness which is critical for effective video tracking. Surprisingly, our model not only adapts to varying missing rates but also adjusts to scene complexity. Extensive experiments show that our model achieves SOTA performance across 9 benchmarks, excelling in both conventional complete and missing modality settings. The code and benchmark will be publicly available at https://github.com/supertyd/FlexTrack/tree/main.

</details>

### SAMPLE: Semantic Alignment through Temporal-Adaptive Multimodal Prompt Learning for Event-Based Open-Vocabulary Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01337) · 📚 被引 0
- **作者**: Jing Wang, Rui Zhao, Ruiqin Xiong, Xingtao Wang, Xiaopeng Fan, Tiejun Huang
- **🏷️ 机构**: School of Computer Science, Peking University, School of Computer Science and Technology Harbin Institute of Technology
- **会议**: ICCV 2025

### SimpleVQA: Multimodal Factuality Evaluation for Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00441)
- **作者**: Xianfu Cheng, Wei Zhang, Shiwei Zhang, Jian Yang, Xiangyuan Guan, Xianjie Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Can Knowledge be Transferred from Unimodal to Multimodal? Investigating the Transitivity of Multimodal Knowledge Editing.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00239) · 📚 被引 0
- **作者**: Lingyong Fang, Xinzhong Wang, Depeng Wang, Zongru Wu, Ya Guo, Huijia Zhu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,China, Ant Group,China
- **会议**: ICCV 2025

### Heuristic-Induced Multimodal Risk Distribution Jailbreak Attack for Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00258)
- **作者**: Teng Ma, Xiaojun Jia, Ranjie Duan, Xinfeng Li, Yihao Huang, Xiaoshuang Jia et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### How Do Multimodal Large Language Models Handle Complex Multimodal Reasoning? Placing Them in an Extensible Escape Game.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00457)
- **作者**: Ziyue Wang, Yurui Dong, Fuwen Luo, Minyuan Ruan, Zhili Cheng, Chi Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00839)
- **作者**: Mahmoud Ahmed, Junjie Fei, Jian Ding, Eslam Mohamed Bakr, Mohamed Elhoseiny
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01505)
- **作者**: Lorenzo Baraldi, Davide Bucciarelli, Federico Betti, Marcella Cornia, Lorenzo Baraldi, Nicu Sebe et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### TWIST & SCOUT: Grounding Multimodal LLM-Experts by Forget-Free Tuning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00134)
- **作者**: Aritra Bhowmik, Mohammad Mahdi Derakhshani, Dennis C. Koelma, Yuki M. Asano, Martin R. Oswald, Cees G. M. Snoek
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### LLaVA-KD: A Framework of Distilling Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00030)
- **作者**: Yuxuan Cai, Jiangning Zhang, Haoyang He, Xinwei He, Ao Tong, Zhenye Gan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Exploiting Frequency Dynamics for Enhanced Multimodal Event-Based Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00564) · 📚 被引 0
- **作者**: Meiqi Cao, Xiangbo Shu, Xin Jiang, Rui Yan, Yazhou Yao, Jinhui Tang
- **🏷️ 机构**: Nanjing University of Science and Technology, Nanjing Forestry University
- **会议**: ICCV 2025

### RMultiplex200K: Toward Reliable Multimodal Process Supervision for Visual Language Models on Telecommunications.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00165) · 📚 被引 0
- **作者**: Sijia Chen, Bin Song
- **🏷️ 机构**: Hong Kong University of Science and Technology (Guangzhou),China, Xidian University,China
- **会议**: ICCV 2025

### CompCap: Improving Multimodal Large Language Models with Composite Captions.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02189)
- **作者**: Xiaohui Chen, Satya Narayan Shukla, Mahmoud Azab, Aashu Singh, Qifan Wang, David Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### MCAM: Multimodal Causal Analysis Model for Ego-Vehicle-Level Driving Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00520)
- **作者**: Tongtong Cheng, Rongzhen Li, Yixin Xiong, Tao Zhang, Jing Wang, Kai Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### On Large Multimodal Models as Open-World Image Classifiers.
- **链接**: [arXiv:2503.21851](https://arxiv.org/abs/2503.21851) · 📚 被引 3
- **作者**: Alessandro Conti, Massimiliano Mancini, Enrico Fini, Yiming Wang, Paolo Rota, Elisa Ricci
- **🏷️ 机构**: University of Trento, Fondazione Bruno Kessler
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional image classification requires a predefined list of semantic categories. In contrast, Large Multimodal Models (LMMs) can sidestep this requirement by classifying images directly using natural language (e.g., answering the prompt "What is the main object in the image?"). Despite this remarkable capability, most existing studies on LMM classification performance are surprisingly limited in scope, often assuming a closed-world setting with a predefined set of categories. In this work, we address this gap by thoroughly evaluating LMM classification performance in a truly open-world setting. We first formalize the task and introduce an evaluation protocol, defining various metrics to assess the alignment between predicted and ground truth classes. We then evaluate 13 models across 10 benchmarks, encompassing prototypical, non-prototypical, fine-grained, and very fine-grained classes, demonstrating the challenges LMMs face in this task. Further analyses based on the proposed metrics reveal the types of errors LMMs make, highlighting challenges related to granularity and fine-grained capabilities, showing how tailored prompting and reasoning can alleviate them.

</details>

### Unbiased Missing-Modality Multimodal Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02272) · 📚 被引 6
- **作者**: Ruiting Dai, Chenxi Li, Yandong Yan, Lisi Mo, Ke Qin, Tao He
- **🏷️ 机构**: University of Electronic Science and Technology of China, School of Computer Science, Peking University
- **会议**: ICCV 2025

### MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00694)
- **作者**: Erik A. Daxberger, Nina Wenzel, David Griffiths, Haiming Gang, Justin Lazarow, Gefen Kohavi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Visual Chronicles: Using Multimodal LLMs to Analyze Massive Collections of Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01186)
- **作者**: Boyang Deng, Songyou Peng, Kyle Genova, Gordon Wetzstein, Noah Snavely, Leonidas J. Guibas et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### MM-IFEngine: Towards Multimodal Instruction Following.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00110) · 📚 被引 1
- **作者**: Shengyuan Ding, Shenxi Wu, Xiangyu Zhao, Yuhang Zang, Haodong Duan, Xiaoyi Dong et al.
- **🏷️ 机构**: Fudan University, Shanghai AI Laboratory
- **会议**: ICCV 2025

### MMAT-1M: A Large Reasoning Dataset for Multimodal Agent Tuning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00146) · 📚 被引 0
- **作者**: Tianhong Gao, Yannian Fu, Weiqun Wu, Haixiao Yue, Shanshan Liu, Gang Zhang
- **🏷️ 机构**: Baidu Inc.
- **会议**: ICCV 2025

### ProbMED: A Probabilistic Framework for Medical Multimodal Binding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01875) · 📚 被引 0
- **作者**: Yuan Gao, Sangwook Kim, Jianzhong You, Chris McIntosh
- **🏷️ 机构**: Peter Munk Cardiac Centre
- **会议**: ICCV 2025

### Benchmarking Multimodal CoT Reward Model Stepwise by Visual Program.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00168) · 📚 被引 0
- **作者**: Minghe Gao, Xuqi Liu, Zhongqi Yue, Yang Wu, Shuang Chen, Juncheng Li et al.
- **🏷️ 机构**: Zhejiang University, Chalmers University of Technology, Ant Group
- **会议**: ICCV 2025

### V2PE: Improving Multimodal Long-Context Capability of Vision-Language Models with Variable Visual Position Encoding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01958)
- **作者**: Junqi Ge, Ziyi Chen, Jintao Lin, Jinguo Zhu, Xihui Liu, Jifeng Dai et al.
- **🏷️ 机构**: Tsinghua / Shanghai AI Lab
- **会议**: ICCV 2025

### IMG: Calibrating Diffusion Models via Implicit Multimodal Guidance.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01492) · 📚 被引 0
- **作者**: Jiayi Guo, Chuanhao Yan, Xingqian Xu, Yulin Wang, Kai Wang, Gao Huang et al.
- **🏷️ 机构**: SHI Labs @ Georgia Tech, Tsinghua University
- **会议**: ICCV 2025

### Open-Set Cross Modal Generalization via Multimodal Unified Representation.
- **链接**: [arXiv:2507.14935](https://arxiv.org/abs/2507.14935) · [代码](https://github.com/haihuangcode/CMG) · 📚 被引 0
- **作者**: Hai Huang, Yan Xia, Shulei Wang, Hanting Wang, Minghui Fang, Shengpeng Ji et al.
- **🏷️ 机构**: Zhejiang University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper extends Cross Modal Generalization (CMG) to open-set environments by proposing the more challenging Open-set Cross Modal Generalization (OSCMG) task. This task evaluates multimodal unified representations in open-set conditions, addressing the limitations of prior closed-set cross-modal evaluations. OSCMG requires not only cross-modal knowledge transfer but also robust generalization to unseen classes within new modalities, a scenario frequently encountered in real-world applications. Existing multimodal unified representation work lacks consideration for open-set environments. To tackle this, we propose MICU, comprising two key components: Fine-Coarse Masked multimodal InfoNCE (FCMI) and Cross modal Unified Jigsaw Puzzles (CUJP). FCMI enhances multimodal alignment by applying contrastive learning at both holistic semantic and temporal levels, incorporating masking to enhance generalization. CUJP enhances feature diversity and model uncertainty by integrating modality-agnostic feature selection with self-supervised learning, thereby strengthening the model's ability to handle unknown categories in open-set tasks. Extensive experiments on CMG and the newly proposed OSCMG validate the effectiveness of our approach. The code is available at https://github.com/haihuangcode/CMG.

</details>

### Bridging Domain Generalization to Multimodal Domain Generalization via Unified Representations.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02088) · 📚 被引 2
- **作者**: Hai Huang, Yan Xia, Sashuai Zhou, Hanting Wang, Shulei Wang, Zhou Zhao
- **🏷️ 机构**: Zhejiang University
- **会议**: ICCV 2025

### MMGeo: Multimodal Compositional Geo-Localization for UAVs.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02334) · 📚 被引 4
- **作者**: Yuxiang Ji, Boyong He, Zhuoyue Tan, Liaoni Wu
- **🏷️ 机构**: Institute of Artificial Intelligence, Xiamen University
- **会议**: ICCV 2025

### Multimodal LLM Guided Exploration and Active Mapping Using Fisher Information.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00512)
- **作者**: Wen Jiang, Boshu Lei, Katrina Ashton, Kostas Daniilidis
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Corvid: Improving Multimodal Large Language Models Towards Chain-of-Thought Reasoning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00291)
- **作者**: Jingjing Jiang, Chao Ma, Xurui Song, Hanwang Zhang, Jun Luo
- **🏷️ 机构**: NUS
- **会议**: ICCV 2025

### FullDiT: Video Generative Foundation Models with Multimodal Control via Full Attention.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01460) · 📚 被引 0
- **作者**: Xuan Ju, Weicai Ye, Quande Liu, Qiulin Wang, Xintao Wang, Pengfei Wan et al.
- **🏷️ 机构**: Kling Team, Kuaishou Technology
- **会议**: ICCV 2025

### Analyzing Fine-Tuning Representation Shift for Multimodal LLMs Steering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00213)
- **作者**: Pegah Khayatan, Mustafa Shukor, Jayneel Parekh, Arnaud Dapogny, Matthieu Cord
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### CapeLLM: Support-Free Category-Agnostic Pose Estimation with Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02125)
- **作者**: Junho Kim, Hyungjin Chung, Byung-Hoon Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### EgoM2P: Egocentric Multimodal Multitask Pretraining.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01008) · 📚 被引 1
- **作者**: Gen Li, Yutong Chen, Yiqian Wu, Kaifeng Zhao, Marc Pollefeys, Siyu Tang
- **🏷️ 机构**: ETH Z&#x00FC;rich
- **会议**: ICCV 2025

### InfoBridge: Balanced Multimodal Integration through Conditional Dependency Modeling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00044) · 📚 被引 1
- **作者**: Chenxin Li, Yifan Liu, Panwang Pan, Hengyu Liu, Xinyu Liu, Wuyang Li et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, ByteDance Inc.
- **会议**: ICCV 2025

### OpenVision: A Fully-Open, Cost-Effective Family of Advanced Vision Encoders for Multimodal Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00379) · 📚 被引 0
- **作者**: Xianhang Li, Yanqing Liu, Haoqin Tu, Cihang Xie
- **🏷️ 机构**: University of California,Santa Cruz
- **会议**: ICCV 2025

### MultiModal Action Conditioned Video Simulation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01315) · 📚 被引 0
- **作者**: Yichen Li, Antonio Torralba
- **🏷️ 机构**: MIT CSAIL
- **会议**: ICCV 2025

### Token Activation Map to Visually Explain Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00012)
- **作者**: Yi Li, Hualiang Wang, Xinpeng Ding, Haonan Wang, Xiaomeng Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### WSI-LLaVA: A Multimodal Large Language Model for Whole Slide Image.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02109)
- **作者**: Yuci Liang, Xinheng Lyu, Wenting Chen, Meidan Ding, Jipeng Zhang, Xiangjian He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Multimodal Latent Diffusion Model for Complex Sewing Pattern Generation.
- **链接**: [arXiv:2412.14453](https://arxiv.org/abs/2412.14453) · 📚 被引 2
- **作者**: Shengqi Liu, Yuhao Cheng, Zhuo Chen, Xingyu Ren, Wenhan Zhu, Lincheng Li et al.
- **🏷️ 机构**: AI Institute, Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence,China, Xueshen AI,China, NetEase Fuxi AI Lab,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating sewing patterns in garment design is receiving increasing attention due to its CG-friendly and flexible-editing nature. Previous sewing pattern generation methods have been able to produce exquisite clothing, but struggle to design complex garments with detailed control. To address these issues, we propose SewingLDM, a multi-modal generative model that generates sewing patterns controlled by text prompts, body shapes, and garment sketches. Initially, we extend the original vector of sewing patterns into a more comprehensive representation to cover more intricate details and then compress them into a compact latent space. To learn the sewing pattern distribution in the latent space, we design a two-step training strategy to inject the multi-modal conditions, \ie, body shapes, text prompts, and garment sketches, into a diffusion model, ensuring the generated garments are body-suited and detail-controlled. Comprehensive qualitative and quantitative experiments show the effectiveness of our proposed method, significantly surpassing previous approaches in terms of complex garment design and various body adaptability. Our project page: https://shengqiliu1.github.io/SewingLDM.

</details>

### Aligning Vision to Language: Annotation-Free Multimodal Knowledge Graph Construction for Enhanced LLMs Reasoning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00099) · 📚 被引 5
- **作者**: Junming Liu, Siyuan Meng, Yanting Gao, Song Mao, Pinlong Cai, Guohang Yan et al.
- **🏷️ 机构**: Tongji University, Shanghai Artificial Intelligence Laboratory, New York University
- **会议**: ICCV 2025

### GenieBlue: Integrating Both Linguistic and Multimodal Capabilities for Large Language Models on Mobile Devices.
- **链接**: [arXiv:2503.06019](https://arxiv.org/abs/2503.06019) · 📚 被引 1
- **作者**: Xudong Lu, Yinghao Chen, Renshou Wu, Haohao Gao, Xi Chen, Xue Yang et al.
- **🏷️ 机构**: vivo AI Lab, Shanghai Jiao Tong University, CUHK MMLab
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in Multimodal Large Language Models (MLLMs) have enabled their deployment on mobile devices. However, challenges persist in maintaining strong language capabilities and ensuring hardware compatibility, both of which are crucial for user experience and practical deployment efficiency. In our deployment process, we observe that existing MLLMs often face performance degradation on pure language tasks, and the current NPU platforms on smartphones do not support the MoE architecture, which is commonly used to preserve pure language capabilities during multimodal training. To address these issues, we systematically analyze methods to maintain pure language capabilities during the training of MLLMs, focusing on both training data and model architecture aspects. Based on these analyses, we propose GenieBlue, an efficient MLLM structural design that integrates both linguistic and multimodal capabilities for LLMs on mobile devices. GenieBlue freezes the original LLM parameters during MLLM training to maintain pure language capabilities. It acquires multimodal capabilities by duplicating specific transformer blocks for full fine-tuning and integrating lightweight LoRA modules. This approach preserves language capabilities while achieving comparable multimodal performance through extensive training. Deployed on smartphone NPUs, GenieBlue demonstrates efficiency and practicality for applications on mobile devices.

</details>

### Rethinking Cross-Modal Interaction in Multimodal Diffusion Transformers.
- **链接**: [arXiv:2506.07986](https://arxiv.org/abs/2506.07986) · [代码](https://github.com/Vchitect/TACA) · 📚 被引 2
- **作者**: Zhengyao Lv, Tianlin Pan, Chenyang Si, Zhaoxi Chen, Wangmeng Zuo, Ziwei Liu et al.
- **🏷️ 机构**: The University of Hong Kong, Nanjing University, Nanyang Technological University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Diffusion Transformers (MM-DiTs) have achieved remarkable progress in text-driven visual generation. However, even state-of-the-art MM-DiT models like FLUX struggle with achieving precise alignment between text prompts and generated content. We identify two key issues in the attention mechanism of MM-DiT, namely 1) the suppression of cross-modal attention due to token imbalance between visual and textual modalities and 2) the lack of timestep-aware attention weighting, which hinder the alignment. To address these issues, we propose \textbf{Temperature-Adjusted Cross-modal Attention (TACA)}, a parameter-efficient method that dynamically rebalances multimodal interactions through temperature scaling and timestep-dependent adjustment. When combined with LoRA fine-tuning, TACA significantly enhances text-image alignment on the T2I-CompBench benchmark with minimal computational overhead. We tested TACA on state-of-the-art models like FLUX and SD3.5, demonstrating its ability to improve image-text alignment in terms of object appearance, attribute binding, and spatial relationships. Our findings highlight the importance of balancing cross-modal attention in improving semantic fidelity in text-to-image diffusion models. Our codes are publicly available at \href{https://github.com/Vchitect/TACA}

</details>

### Multimodal Prompt Alignment for Facial Expression Recognition.
- **链接**: [arXiv:2506.21017](https://arxiv.org/abs/2506.21017) · 📚 被引 3
- **作者**: Fuyan Ma, Yiran He, Bin Sun, Shutao Li
- **🏷️ 机构**: Chinese Academy of Military Science, Changchun University of Science and Technology, Hunan University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt learning has been widely adopted to efficiently adapt vision-language models (VLMs) like CLIP for various downstream tasks. Despite their success, current VLM-based facial expression recognition (FER) methods struggle to capture fine-grained textual-visual relationships, which are essential for distinguishing subtle differences between facial expressions. To address this challenge, we propose a multimodal prompt alignment framework for FER, called MPA-FER, that provides fine-grained semantic guidance to the learning process of prompted visual features, resulting in more precise and interpretable representations. Specifically, we introduce a multi-granularity hard prompt generation strategy that utilizes a large language model (LLM) like ChatGPT to generate detailed descriptions for each facial expression. The LLM-based external knowledge is injected into the soft prompts by minimizing the feature discrepancy between the soft prompts and the hard prompts. To preserve the generalization abilities of the pretrained CLIP model, our approach incorporates prototype-guided visual feature alignment, ensuring that the prompted visual features from the frozen image encoder align closely with class-specific prototypes. Additionally, we propose a cross-modal global-local alignment module that focuses on expression-relevant facial features, further improving the alignment between textual and visual features. Extensive experiments demonstrate our framework outperforms state-of-the-art methods on three FER benchmark datasets, while retaining the benefits of the pretrained model and minimizing computational costs.

</details>

### X2i: Seamless Integration of Multimodal Understanding Into Diffusion Transformer Via Attention Distillation.
- **链接**: [arXiv:2503.06134](https://arxiv.org/abs/2503.06134) · [代码](https://github.com/OPPO-Mente-Lab/X2I) · 📚 被引 0
- **作者**: Jian Ma, Qirong Peng, Xu Guo, Chen Chen, Haonan Lu, Zhenyu Yang
- **🏷️ 机构**: OPPO AI Center, Tsinghua University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Text-to-image (T2I) models are well known for their ability to produce highly realistic images, while multimodal large language models (MLLMs) are renowned for their proficiency in understanding and integrating multiple modalities. However, currently there is no straightforward and efficient framework to transfer the multimodal comprehension abilities of MLLMs to T2I models to enable them to understand multimodal inputs. In this paper, we propose the X2I framework, which endows Diffusion Transformer (DiT) models with the capability to comprehend various modalities, including multilingual text, screenshot documents, images, videos, and audio. X2I is trained using merely 100K English corpus with 160 GPU hours. Building on the DiT teacher model, we adopt an innovative distillation method to extract the inference capabilities of the teacher model and design a lightweight AlignNet structure to serve as an intermediate bridge. Compared to the teacher model, X2I shows a decrease in performance degradation of less than 1\% while gaining various multimodal understanding abilities, including multilingual to image, image to image, image-text to image, video to image, audio to image, and utilizing creative fusion to enhance imagery. Furthermore, it is applicable for LoRA training in the context of image-text to image generation, filling a void in the industry in this area. We further design a simple LightControl to enhance the fidelity of instructional image editing. Finally, extensive experiments demonstrate the effectiveness, efficiency, multifunctionality, and transferability of our X2I. The open-source code and checkpoints for X2I can be found at the following link: https://github.com/OPPO-Mente-Lab/X2I.

</details>

### Controlling Multimodal Llms Via Reward-Guided Decoding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00137)
- **作者**: Oscar Mañas, Pierluca D'Oro, Koustuv Sinha, Adriana Romero-Soriano, Michal Drozdzal, Aishwarya Agrawal
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Enhancing Few-Shot Vision-Language Classification With Large Multimodal Model Features.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00265) · 📚 被引 1
- **作者**: Chancharik Mitra, Brandon Huang, Tianning Chai, Zhiqiu Lin, Assaf Arbelle, Rogério Feris et al.
- **🏷️ 机构**: Carnegie Mellon University, University of California,Berkeley, IBM Research
- **会议**: ICCV 2025

### Enhancing Spatial Reasoning in Multimodal Large Language Models Through Reasoning-Based Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00736)
- **作者**: Zhenhua Ning, Zhuotao Tian, Shaoshuai Shi, Guangming Lu, Daojing He, Wenjie Pei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Federated Prompt-Tuning with Heterogeneous and Incomplete Multimodal Client Data.
- **链接**: [arXiv:2602.07081](https://arxiv.org/abs/2602.07081) · 📚 被引 0
- **作者**: Thu Hang Phung, Duong M. Nguyen, Thanh Trung Huynh, Quoc Viet Hung Nguyen, Trong Nghia Hoang, Phi Le Nguyen
- **🏷️ 机构**: Institute of AI Innovation and Societal Impact, Hanoi University of Science and Technology, EPFL, Griffith University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper introduces a generalized federated prompt-tuning framework for practical scenarios where local datasets are multi-modal and exhibit different distributional patterns of missing features at the input level. The proposed framework bridges the gap between federated learning and multi-modal prompt-tuning which have traditionally focused on either uni-modal or centralized data. A key challenge in this setting arises from the lack of semantic alignment between prompt instructions that encode similar distributional patterns of missing data across different clients. To address this, our framework introduces specialized client-tuning and server-aggregation designs that simultaneously optimize, align, and aggregate prompt-tuning instructions across clients and data modalities. This allows prompt instructions to complement one another and be combined effectively. Extensive evaluations on diverse multimodal benchmark datasets demonstrate that our work consistently outperforms state-of-the-art (SOTA) baselines.

</details>

### Enrich and Detect: Video Temporal Grounding With Multimodal Llms.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02252)
- **作者**: Shraman Pramanick, Effrosyni Mavroudi, Yale Song, Rama Chellappa, Lorenzo Torresani, Triantafyllos Afouras
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Benchmarking Multimodal Large Language Models Against Image Corruptions.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00843)
- **作者**: Xinkuan Qiu, Meina Kan, Yongbin Zhou, Shiguang Shan
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Igd: Instructional Graphic Design With Multimodal Layer Generatio.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01693) · 📚 被引 0
- **作者**: Yadong Qu, Hongtao Xie, Yongdong Zhang, Shancheng Fang, Yuxin Wang, Xiaorui Wang et al.
- **🏷️ 机构**: University of Science and Technology of China, YuanShi Technology, Institute of Trustworthy Embodied AI, Fudan University
- **会议**: ICCV 2025

### G2D: Boosting Multimodal Learning with Gradient-Guided Distillation.
- **链接**: [arXiv:2506.21514](https://arxiv.org/abs/2506.21514) · [代码](https://github.com/rAIson-Lab/G2D)
- **作者**: Mohammed Rakib, Arunkumar Bagavathi
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal learning aims to leverage information from diverse data modalities to achieve more comprehensive performance. However, conventional multimodal models often suffer from modality imbalance, where one or a few modalities dominate model optimization, leading to suboptimal feature representation and underutilization of weak modalities. To address this challenge, we introduce Gradient-Guided Distillation (G$^{2}$D), a knowledge distillation framework that optimizes the multimodal model with a custom-built loss function that fuses both unimodal and multimodal objectives. G$^{2}$D further incorporates a dynamic sequential modality prioritization (SMP) technique in the learning process to ensure each modality leads the learning process, avoiding the pitfall of stronger modalities overshadowing weaker ones. We validate G$^{2}$D on multiple real-world datasets and show that G$^{2}$D amplifies the significance of weak modalities while training and outperforms state-of-the-art methods in classification and regression tasks. Our code is available at https://github.com/rAIson-Lab/G2D.

</details>

### PS3: A Multimodal Transformer Integrating Pathology Reports with Histology Images and Biological Pathways for Cancer Survival Prediction.
- **链接**: [arXiv:2509.20022](https://arxiv.org/abs/2509.20022) · [代码](https://github.com/manahilr/PS3) · 📚 被引 2
- **作者**: Manahil Raza, Ayesha Azam, Talha Qaiser, Nasir M. Rajpoot
- **🏷️ 机构**: University of Warwick,UK
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current multimodal fusion approaches in computational oncology primarily focus on integrating multi-gigapixel histology whole slide images (WSIs) with genomic or transcriptomic data, demonstrating improved survival prediction. We hypothesize that incorporating pathology reports can further enhance prognostic performance. Pathology reports, as essential components of clinical workflows, offer readily available complementary information by summarizing histopathological findings and integrating expert interpretations and clinical context. However, fusing these modalities poses challenges due to their heterogeneous nature. WSIs are high-dimensional, each containing several billion pixels, whereas pathology reports consist of concise text summaries of varying lengths, leading to potential modality imbalance. To address this, we propose a prototype-based approach to generate balanced representations, which are then integrated using a Transformer-based fusion model for survival prediction that we term PS3 (Predicting Survival from Three Modalities). Specifically, we present: (1) Diagnostic prototypes from pathology reports, leveraging self-attention to extract diagnostically relevant sections and standardize text representation; (2) Histological prototypes to compactly represent key morphological patterns in WSIs; and (3) Biological pathway prototypes to encode transcriptomic expressions, accurately capturing cellular functions. PS3, the three-modal transformer model, processes the resulting prototype-based multimodal tokens and models intra-modal and cross-modal interactions across pathology reports, WSIs and transcriptomic data. The proposed model outperforms state-of-the-art methods when evaluated against clinical, unimodal and multimodal baselines on six datasets from The Cancer Genome Atlas (TCGA). The code is available at: https://github.com/manahilr/PS3.

</details>

### How Would it Sound? Material-Controlled Multimodal Acoustic Profile Generation for Indoor Scenes.
- **链接**: [arXiv:2508.02905](https://arxiv.org/abs/2508.02905) · 📚 被引 0
- **作者**: Mahnoor Fatima Saad, Ziad Al-Halah
- **🏷️ 机构**: University of Utah
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How would the sound in a studio change with a carpeted floor and acoustic tiles on the walls? We introduce the task of material-controlled acoustic profile generation, where, given an indoor scene with specific audio-visual characteristics, the goal is to generate a target acoustic profile based on a user-defined material configuration at inference time. We address this task with a novel encoder-decoder approach that encodes the scene's key properties from an audio-visual observation and generates the target Room Impulse Response (RIR) conditioned on the material specifications provided by the user. Our model enables the generation of diverse RIRs based on various material configurations defined dynamically at inference time. To support this task, we create a new benchmark, the Acoustic Wonderland Dataset, designed for developing and evaluating material-aware RIR prediction methods under diverse and challenging settings. Our results demonstrate that the proposed model effectively encodes material information and generates high-fidelity RIRs, outperforming several baselines and state-of-the-art methods.

</details>

### LLaVA-Prumerge: Adaptive Token Reduction for Efficient Large Multimodal Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02122)
- **作者**: Yuzhang Shang, Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Autocompose: Automatic Generation of Pose Transition Descriptions for Composed Pose Retrieval Using Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00695)
- **作者**: Yi-Ting Shen, Sungmin Eum, Doheon Lee, Rohit Shete, Chiao-Yi Wang, Heesung Kwon et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Exploring Multimodal Diffusion Transformers for Enhanced Prompt-Based Image Editing.
- **链接**: [arXiv:2508.07519](https://arxiv.org/abs/2508.07519) · 📚 被引 2
- **作者**: Joonghyuk Shin, Alchan Hwang, Yujin Kim, Daneul Kim, Jaesik Park
- **🏷️ 机构**: Seoul National University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transformer-based diffusion models have recently superseded traditional U-Net architectures, with multimodal diffusion transformers (MM-DiT) emerging as the dominant approach in state-of-the-art models like Stable Diffusion 3 and Flux.1. Previous approaches have relied on unidirectional cross-attention mechanisms, with information flowing from text embeddings to image latents. In contrast, MMDiT introduces a unified attention mechanism that concatenates input projections from both modalities and performs a single full attention operation, allowing bidirectional information flow between text and image branches. This architectural shift presents significant challenges for existing editing techniques. In this paper, we systematically analyze MM-DiT's attention mechanism by decomposing attention matrices into four distinct blocks, revealing their inherent characteristics. Through these analyses, we propose a robust, prompt-based image editing method for MM-DiT that supports global to local edits across various MM-DiT variants, including few-step models. We believe our findings bridge the gap between existing U-Net-based methods and emerging architectures, offering deeper insights into MMDiT's behavioral patterns.

</details>

### Scaling Laws for Native Multimodal Models.
- **链接**: [arXiv:2504.07951](https://arxiv.org/abs/2504.07951) · 📚 被引 6
- **作者**: Mustafa Shukor, Enrico Fini, Victor Guilherme Turrisi da Costa, Matthieu Cord, Joshua M. Susskind, Alaaeldin El-Nouby
- **🏷️ 机构**: Sorbonne University, Apple
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Building general-purpose models that can effectively perceive the world through multimodal signals has been a long-standing goal. Current approaches involve integrating separately pre-trained components, such as connecting vision encoders to LLMs and continuing multimodal training. While such approaches exhibit remarkable sample efficiency, it remains an open question whether such late-fusion architectures are inherently superior. In this work, we revisit the architectural design of native multimodal models (NMMs)-those trained from the ground up on all modalities-and conduct an extensive scaling laws study, spanning 457 trained models with different architectures and training mixtures. Our investigation reveals no inherent advantage to late-fusion architectures over early-fusion ones, which do not rely on image encoders or tokenizers. On the contrary, early-fusion exhibits stronger performance at lower parameter counts, is more efficient to train, and is easier to deploy. Motivated by the strong performance of the early-fusion architectures, we show that incorporating Mixture of Experts (MoEs) allows models to learn modality-specific weights, significantly benefiting performance.

</details>

### FedMVP: Federated Multimodal Visual Prompt Tuning for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01660)
- **作者**: Mainak Singha, Subhankar Roy, Sarthak Mehrotra, Ankit Jha, Moloud Abdar, Biplab Banerjee et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Calibrating MLLM-as-a-judge via Multimodal Bayesian Prompt Ensembles.
- **链接**: [arXiv:2509.08777](https://arxiv.org/abs/2509.08777) · 📚 被引 1
- **作者**: Eric Slyman, Md. Mehrab Tanjim, Kushal Kafle, Stefan Lee
- **🏷️ 机构**: Adobe Systems, Oregon State University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) are increasingly used to evaluate text-to-image (TTI) generation systems, providing automated judgments based on visual and textual context. However, these "judge" models often suffer from biases, overconfidence, and inconsistent performance across diverse image domains. While prompt ensembling has shown promise for mitigating these issues in unimodal, text-only settings, our experiments reveal that standard ensembling methods fail to generalize effectively for TTI tasks. To address these limitations, we propose a new multimodal-aware method called Multimodal Mixture-of-Bayesian Prompt Ensembles (MMB). Our method uses a Bayesian prompt ensemble approach augmented by image clustering, allowing the judge to dynamically assign prompt weights based on the visual characteristics of each sample. We show that MMB improves accuracy in pairwise preference judgments and greatly enhances calibration, making it easier to gauge the judge's true uncertainty. In evaluations on two TTI benchmarks, HPSv2 and MJBench, MMB outperforms existing baselines in alignment with human annotations and calibration across varied image content. Our findings highlight the importance of multimodal-specific strategies for judge calibration and suggest a promising path forward for reliable large-scale TTI evaluation.

</details>

### MDP-Omni: Parameter-Free Multimodal Depth Prior-Based Sampling for Omnidirectional Stereo Matching.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02429) · 📚 被引 0
- **作者**: Eunjin Son, HyungGi Jo, Wookyong Kwon, Sang Jun Lee
- **🏷️ 机构**: Jeonbuk National University,Republic of Korea, Electronics and Telecommunications Research Institute (ETRI),Republic of Korea
- **会议**: ICCV 2025

### Multimodal Large Language Model-Guided ISP Hyperparameter Optimization with Dynamic Preference Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00048)
- **作者**: Xinyu Sun, Zhikun Zhao, Congyan Lang, Bing Li, Juan Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### MPBR: Multimodal Progressive Bidirectional Reasoning for Open-Set Fine-Grained Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00127) · 📚 被引 1
- **作者**: Junfu Tan, Peiguang Jing, Yu Zhu, Yu Liu
- **🏷️ 机构**: Tianjin University, Fudan University
- **会议**: ICCV 2025

### XTrack: Multimodal Training Boosts RGB-X Video Object Trackers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00543) · 📚 被引 8
- **作者**: Yuedong Tan, Zongwei Wu, Yuqian Fu, Zhuyun Zhou, Guolei Sun, Eduard Zamfir et al.
- **🏷️ 机构**: University of Wurzburg,Computer Vision Lab, CAIDAS &#x0026; IFI, Sofia University,INSAIT, CVL, ETH Zurich
- **会议**: ICCV 2025

### $\mathcal{F}_{M}$ FinMMR: Make Financial Numerical Reasoning More Multimodal, Comprehensive, and Challenging.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00311) · 📚 被引 1
- **作者**: Zichen Tang, Haihong E, Jiacheng Liu, Zhongjun Yang, Rongjin Li, Zihua Rong et al.
- **🏷️ 机构**: Beijing University of Posts and Telecommunications
- **会议**: ICCV 2025

### BASIC: Boosting Visual Alignment with Intrinsic Refined Embeddings in Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01914)
- **作者**: Jianting Tang, Yubo Wang, Haoyu Cao, Linli Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### G2SF: Geometry-Guided Score Fusion for Multimodal Industrial Anomaly Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01911)
- **作者**: Chengyu Tao, Xuanming Cao, Juan Du
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### MetaMorph: Multimodal Understanding and Generation via Instruction Tuning.
- **链接**: [arXiv:2412.14164](https://arxiv.org/abs/2412.14164) · 📚 被引 1
- **作者**: Shengbang Tong, David Fan, Jiachen Zhu, Yunyang Xiong, Xinlei Chen, Koustuv Sinha et al.
- **🏷️ 机构**: FAIR, Meta, Meta Reality Labs
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we propose Visual-Predictive Instruction Tuning (VPiT) - a simple and effective extension to visual instruction tuning that enables a pretrained LLM to quickly morph into an unified autoregressive model capable of generating both text and visual tokens. VPiT teaches an LLM to predict discrete text tokens and continuous visual tokens from any input sequence of image and text data curated in an instruction-following format. Our empirical investigation reveals several intriguing properties of VPiT: (1) visual generation ability emerges as a natural byproduct of improved visual understanding, and can be unlocked efficiently with a small amount of generation data; (2) while we find understanding and generation to be mutually beneficial, understanding data contributes to both capabilities more effectively than generation data. Building upon these findings, we train our MetaMorph model and achieve competitive performance on both visual understanding and generation. In visual generation, MetaMorph can leverage the world knowledge and reasoning abilities gained from LLM pretraining, and overcome common failure modes exhibited by other generation models. Our results suggest that LLMs may have strong "prior" vision capabilities that can be efficiently adapted to both visual understanding and generation with a relatively simple instruction tuning process.

</details>

### HiMTok: Learning Hierarchical Mask Tokens for Image Segmentation with Large Multimodal Model.
- **链接**: [arXiv:2503.13026](https://arxiv.org/abs/2503.13026) · 📚 被引 3
- **作者**: Tao Wang, Changxu Cheng, Lingfeng Wang, Senda Chen, Wuyue Zhao
- **🏷️ 机构**: Uni-Ubi, Zhejiang University, Tongji University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The remarkable performance of large multimodal models (LMMs) has attracted significant interest from the image segmentation community. To align with the next-token-prediction paradigm, current LMM-driven segmentation methods either use object boundary points to represent masks or introduce special segmentation tokens, whose hidden states are decoded by a segmentation model requiring the original image as input. However, these approaches often suffer from inadequate mask representation and complex architectures, limiting the potential of LMMs. In this work, we propose the Hierarchical Mask Tokenizer (HiMTok), which represents segmentation masks with up to 32 tokens and eliminates the need for the original image during mask de-tokenization. HiMTok allows for compact and coarse-to-fine mask representations, aligning well with the LLM next-token-prediction paradigm and facilitating the direct acquisition of segmentation capabilities. We develop a 3-stage training recipe for progressive learning of segmentation and visual capabilities, featuring a hierarchical mask loss for effective coarse-to-fine learning. Additionally, we enable bidirectional information flow, allowing conversion between bounding boxes and mask tokens to fully leverage multi-task training potential. Extensive experiments demonstrate that our method achieves state-of-the-art performance across various segmentation tasks,while also enhancing visual grounding and maintaining overall visual understanding.

</details>

### LMM4LMM: Benchmarking and Evaluating Large-Multimodal Image Generation With LMMs.
- **链接**: [arXiv:2504.08358](https://arxiv.org/abs/2504.08358) · [代码](https://github.com/IntMeGroup/LMM4LMM) · 📚 被引 11
- **作者**: Jiarui Wang, Huiyu Duan, Yu Zhao, Juntong Wang, Guangtao Zhai, Xiongkuo Min
- **🏷️ 机构**: Shanghai Jiao Tong University,Shanghai,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent breakthroughs in large multimodal models (LMMs) have significantly advanced both text-to-image (T2I) generation and image-to-text (I2T) interpretation. However, many generated images still suffer from issues related to perceptual quality and text-image alignment. Given the high cost and inefficiency of manual evaluation, an automatic metric that aligns with human preferences is desirable. To this end, we present EvalMi-50K, a comprehensive dataset and benchmark for evaluating large-multimodal image generation, which features (i) comprehensive tasks, encompassing 2,100 extensive prompts across 20 fine-grained task dimensions, and (ii) large-scale human-preference annotations, including 100K mean-opinion scores (MOSs) and 50K question-answering (QA) pairs annotated on 50,400 images generated from 24 T2I models. Based on EvalMi-50K, we propose LMM4LMM, an LMM-based metric for evaluating large multimodal T2I generation from multiple dimensions including perception, text-image correspondence, and task-specific accuracy. Extensive experimental results show that LMM4LMM achieves state-of-the-art performance on EvalMi-50K, and exhibits strong generalization ability on other AI-generated image evaluation benchmark datasets, manifesting the generality of both the EvalMi-50K dataset and LMM4LMM metric. Both EvalMi-50K and LMM4LMM will be released at https://github.com/IntMeGroup/LMM4LMM.

</details>

### SHIFT: Smoothing Hallucinations by Information Flow Tuning for Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00347)
- **作者**: Sudong Wang, Yunjian Zhang, Yao Zhu, Enci Liu, Jianing Li, Yanwei Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Improving Multimodal Learning via Imbalanced Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00217) · 📚 被引 7
- **作者**: Shicai Wei, Chunbo Luo, Yang Luo
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: ICCV 2025

### Boosting Multimodal Learning via Disentangled Gradient Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02124) · 📚 被引 6
- **作者**: Shicai Wei, Chunbo Luo, Yang Luo
- **🏷️ 机构**: University of Electronic Science and Technology of China
- **会议**: ICCV 2025

### Perceive, Understand and Restore: Real-World Image Super-Resolution with Autoregressive Multimodal Generative Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01732) · 📚 被引 3
- **作者**: Hongyang Wei, Shuaizheng Liu, Chun Yuan, Lei Zhang
- **🏷️ 机构**: Tsinghua Shenzhen International Graduate School, Tsinghua University, The Hong Kong Polytechnic University
- **会议**: ICCV 2025

### VisNumBench: Evaluating Number Sense of Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00365)
- **作者**: Tengjin Weng, Jingyi Wang, Wenhao Jiang, Zhong Ming
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### CMT: A Cascade MAR with Topology Predictor for Multimodal Conditional CAD Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00659) · 📚 被引 2
- **作者**: Jianyu Wu, Yizhou Wang, Xiangyu Yue, Xinzhu Ma, Jinyang Guo, Dongzhan Zhou et al.
- **🏷️ 机构**: Shanghai Artificial Intelligence Laboratory, The Chinese University of Hong Kong, Beihang University
- **会议**: ICCV 2025

### Harmonizing Visual Representations for Unified Multimodal Understanding and Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01648) · 📚 被引 0
- **作者**: Size Wu, Wenwei Zhang, Lumin Xu, Sheng Jin, Zhonghua Wu, Qingyi Tao et al.
- **🏷️ 机构**: Nanyang Technological University,S-Lab, Shanghai AI Laboratory Research, The Chinese University of Hong Kong
- **会议**: ICCV 2025

### Player-Centric Multimodal Prompt Generation for Large Language Model Based Identity-Aware Basketball Video Captioning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02255) · 📚 被引 3
- **作者**: Zeyu Xi, Haoying Sun, Yaofei Wu, Junchi Yan, Haoran Zhang, Lifang Wu et al.
- **🏷️ 机构**: Beijing University of Technology, Shanghai Jiao Tong University, Chinese Academy of Sciences
- **会议**: ICCV 2025

### Exploring the Visual Feature Space for Multimodal Neural Decoding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00416) · 📚 被引 0
- **作者**: Weihao Xia, A. Cengiz Öztireli
- **🏷️ 机构**: University of Cambridge
- **会议**: ICCV 2025

### Bootstrapping Grounded Chain-of-Thought in Multimodal Llms for Data-Efficient Model Adaptation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00027)
- **作者**: Jiaer Xia, Bingkui Tong, Yuhang Zang, Rui Shao, Kaiyang Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### OURO: A Self-Bootstrapped Framework for Enhancing Multimodal Scene Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01695) · 📚 被引 0
- **作者**: Tianrun Xu, Guanyu Chen, Ye Li, Yuxin Xi, Zeyu Mu, Ruichen Wang et al.
- **🏷️ 机构**: Tsinghua University,Department of Automation,Beijing,China, School of Software, Xinjiang University, School of Artificial Intelligence, Beijing Normal University,Beijing,China
- **会议**: ICCV 2025

### Learning to Inference Adaptively for Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00339)
- **作者**: Zhuoyan Xu, Khoi Duc Nguyen, Preeti Mukherjee, Saurabh Bagchi, Somali Chaterji, Yingyu Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### RoboTron-Mani: All-in-One Multimodal Large Model for Robotic Manipulation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01272) · 📚 被引 1
- **作者**: Feng Yan, Fanfan Liu, Yiyang Huang, Zechao Guan, Liming Zheng, Yufeng Zhong et al.
- **🏷️ 机构**: Meituan
- **会议**: ICCV 2025

### R1-Onevision: Advancing Generalized Multimodal Reasoning Through Cross-Modal Formalization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00229) · 📚 被引 15
- **作者**: Yi Yang, Xiaoxuan He, Hongkun Pan, Xiyan Jiang, Yan Deng, Xingtao Yang et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, Zhejiang University, Renmin University of China
- **会议**: ICCV 2025

### DocThinker: Explainable Multimodal Large Language Models with Rule-Based Reinforcement Learning for Document Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00086)
- **作者**: Wenwen Yu, Zhibo Yang, Yuliang Liu, Xiang Bai
- **🏷️ 机构**: HUAST
- **会议**: ICCV 2025

### ShortV: Efficient Multimodal Large Language Models by Freezing Visual Tokens in Ineffective Layers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00038)
- **作者**: Qianhao Yuan, Qingyu Zhang, Yanjiang Liu, Jiawei Chen, Yaojie Lu, Hongyu Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Visual-Oriented Fine-Grained Knowledge Editing for MultiModal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00240)
- **作者**: Zhen Zeng, Leijiang Gu, Xun Yang, Zhangling Duan, Zenglin Shi, Meng Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### AVAM: A Universal Training-Free Adaptive Visual Anchoring Embedded into Multimodal Large Language Model for Multi-Image Question Answering.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00221)
- **作者**: Kang Zeng, Guojin Zhong, Jintao Cheng, Jin Yuan, Zhiyong Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Text2Outfit: Controllable Outfit Generation With Multimodal Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01500) · 📚 被引 0
- **作者**: Yuanhao Zhai, Yen-Liang Lin, Minxu Peng, Larry S. Davis, Ashwin Chandramouli, Junsong Yuan et al.
- **🏷️ 机构**: State University of New York at Buffalo, Amazon
- **会议**: ICCV 2025

### Griffon v2: Advancing Multimodal Perception with High-Resolution Scaling and Visual-Language Co-Referring.
- **链接**: [arXiv:2403.09333](https://arxiv.org/abs/2403.09333) · [代码](https://github.com/jefferyZhan/Griffon) · 📚 被引 2
- **作者**: Yufei Zhan, Shurong Zheng, Yousong Zhu, Hongyin Zhao, Fan Yang, Ming Tang et al.
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences,Beijing,China, Foundation Model Research Center, Institute of Automation, Chinese Academy of Sciences,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Vision Language Models have achieved fine-grained object perception, but the limitation of image resolution remains a significant obstacle to surpassing the performance of task-specific experts in complex and dense scenarios. Such limitation further restricts the model's potential to achieve nuanced visual and language referring in domains such as GUI Agents, counting, \textit{etc}. To address this issue, we introduce a unified high-resolution generalist model, Griffon v2, enabling flexible object referring with visual and textual prompts. To efficiently scale up image resolution, we design a simple and lightweight down-sampling projector to overcome the input tokens constraint in Large Language Models. This design inherently preserves the complete contexts and fine details and significantly improves multimodal perception ability, especially for small objects. Building upon this, we further equip the model with visual-language co-referring capabilities through a plug-and-play visual tokenizer. It enables user-friendly interaction with flexible target images, free-form texts, and even coordinates. Experiments demonstrate that Griffon v2 can localize objects of interest with visual and textual referring, achieve state-of-the-art performance on REC and phrase grounding, and outperform expert models in object detection, object counting, and REG. Data and codes are released at https://github.com/jefferyZhan/Griffon.

</details>

### Oasis: One Image is All You Need for Multimodal Instruction Data Synthesis.
- **链接**: [arXiv:2503.08741](https://arxiv.org/abs/2503.08741) · [代码](https://github.com/Letian2003/MM_INF) · 📚 被引 1
- **作者**: Letian Zhang, Quan Cui, Bingchen Zhao, Cheng Yang
- **🏷️ 机构**: Tongji University, Bytedance, University of Edinburgh
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of multi-modal large language models (MLLMs) has been largely attributed to the large-scale training data. However, the training data of many MLLMs is unavailable due to privacy concerns. The expensive and labor-intensive process of collecting multi-modal data further exacerbates the problem. Is it possible to synthesize multi-modal training data automatically without compromising diversity and quality? In this paper, we propose a new method, Oasis, to synthesize high-quality multi-modal data with only images. Oasis breaks through traditional methods by prompting only images to the MLLMs, thus extending the data diversity by a large margin. Our method features a delicate quality control method which ensures the data quality. We collected over 500k data and conducted incremental experiments on LLaVA-NeXT. Extensive experiments demonstrate that our method can significantly improve the performance of MLLMs. The image-based synthesis also allows us to focus on the specific-domain ability of MLLMs. Code and dataset are publicly available at https://github.com/Letian2003/MM_INF.

</details>

### Unified Multimodal Understanding via Byte-Pair Visual Encoding.
- **链接**: [arXiv:2506.23639](https://arxiv.org/abs/2506.23639) · 📚 被引 1
- **作者**: Wanpeng Zhang, Yicheng Feng, Hao Luo, Yijiang Li, Zihao Yue, Sipeng Zheng et al.
- **🏷️ 机构**: School of Computer Science, Peking University, University of California,San Diego, School of Information, Renmin University of China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have made significant progress in vision-language understanding, yet effectively aligning different modalities remains a fundamental challenge. We present a framework that unifies multimodal understanding by applying byte-pair encoding to visual tokens. Unlike conventional approaches that rely on modality-specific encoders, our method directly incorporates structural information into visual tokens, mirroring successful tokenization strategies in text-only language models. We introduce a priority-guided encoding scheme that considers both frequency and spatial consistency, coupled with a multi-stage training procedure based on curriculum-driven data composition. These enhancements enable the transformer model to better capture cross-modal relationships and reason with visual information. Comprehensive experiments demonstrate improved performance across diverse vision-language tasks. By bridging the gap between visual and textual representations, our approach contributes to the advancement of more capable and efficient multimodal foundation models.

</details>

### CreatiLayout: Siamese Multimodal Diffusion Transformer for Creative Layout-to-Image Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01718) · 📚 被引 3
- **作者**: Hui Zhang, Dexiang Hong, Yitong Wang, Jie Shao, Xinglong Wu, Zuxuan Wu et al.
- **🏷️ 机构**: Institute of Trustworthy Embodied AI, Fudan University,Shanghai,China, Bytedance Intelligent Creation,China
- **会议**: ICCV 2025

### R1-VL: Learning to Reason with Multimodal Large Language Models via Step-Wise Group Relative Policy Optimization.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00181)
- **作者**: Jingyi Zhang, Jiaxing Huang, Huanjin Yao, Shunyu Liu, Xikun Zhang, Shijian Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Scaling Omni-Modal Pretraining with Multimodal Context: Advancing Universal Representation Learning Across Modalities.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00132) · 📚 被引 0
- **作者**: Yiyuan Zhang, Handong Li, Jing Liu, Xiangyu Yue
- **🏷️ 机构**: MMLab, CUHK, School of Artificial Intelligence, UCAS
- **会议**: ICCV 2025

### Efficient Visual Place Recognition Through Multimodal Semantic Knowledge Integration.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00531) · 📚 被引 2
- **作者**: Sitao Zhang, Hongda Mao, Qingshuang Chen, Yelin Kim
- **🏷️ 机构**: The Pennsylvania State University, Amazon
- **会议**: ICCV 2025

### FALCON: Resolving Visual Redundancy and Fragmentation in High-Resolution Multimodal Large Language Models via Visual Registers.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02184)
- **作者**: Renshan Zhang, Rui Shao, Gongwei Chen, Miao Zhang, Kaiwen Zhou, Weili Guan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### 2.5 Years in Class: A Multimodal Textbook for Vision-Language Pretraining.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00442)
- **作者**: Wenqi Zhang, Hang Zhang, Xin Li, Jiashuo Sun, Yongliang Shen, Weiming Lu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Jailbreaking Multimodal Large Language Models via Shuffle Inconsistency.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00198)
- **作者**: Shiji Zhao, Ranjie Duan, Fengxiang Wang, Chi Chen, Caixin Kang, Shouwei Ruan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Differential-Informed Sample Selection Accelerates Multimodal Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00281)
- **作者**: Zihua Zhao, Feng Hong, Mengxi Chen, Pengyi Chen, Benyuan Liu, Jiangchao Yao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### HIS-GPT: Towards 3D Human-In-Scene Multimodal Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00411) · 📚 被引 0
- **作者**: Jiahe Zhao, Ruibing Hou, Zejie Tian, Hong Chang, Shiguang Shan
- **🏷️ 机构**: Institute of Computing Technology, CAS,State Key Laboratory of AI Safety,China, Communication University of China
- **会议**: ICCV 2025

### Aigi-Holmes: Towards Explainable and Generalizable AI-Generated Image Detection via Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01742)
- **作者**: Ziyin Zhou, Yunpeng Luo, Yuanchen Wu, Ke Sun, Jiayi Ji, Ke Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### LIRA: Reasoning Reconstruction via Multimodal Large Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00172)
- **作者**: Zhen Zhou, Tong Wang, Yunkai Ma, Xiao Tan, Fengshui Jing
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Are They the Same? Exploring Visual Correspondence Shortcomings of Multimodal LLMs.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01641)
- **作者**: Yikang Zhou, Tao Zhang, Shilin Xu, Shihao Chen, Qianyu Zhou, Yunhai Tong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Multimodal LLMs as Customized Reward Models for Text-to-Image Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01826)
- **作者**: Shijie Zhou, Ruiyi Zhang, Huaisheng Zhu, Branislav Kveton, Yufan Zhou, Jiuxiang Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

### Dynamic Multimodal Prototype Learning in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00241)
- **作者**: Xingyu Zhu, Shuo Wang, Beier Zhu, Miaoge Li, Yunfan Li, Junfeng Fang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2025

## 跨领域论文（完整笔记在其他领域）

- SiM3D: Single-Instance Multiview Multimodal and Multisetup 3D Anomaly Detection Benchmark. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion. → [3d-detection](../3d-detection/Guideline%202025.md)
- EVT: Efficient View Transformation for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- Height-Fidelity Dense Global Fusion for Multi-Modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- RoboTron-Drive: All-in-One Large Multimodal Model for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Hints of Prompt: Enhancing Visual Representation for Multimodal LLMs in Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
