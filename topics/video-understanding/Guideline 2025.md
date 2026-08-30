# Video Understanding — 2025 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 31 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Track Any Anomalous Object: A Granular Video Anomaly Detection Pipeline. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2506.05175](https://arxiv.org/abs/2506.05175) · 📚 被引 5
- **作者**: Yuzhi Huang, Chenxin Li, Haitao Zhang, Zixu Lin, Yunlong Lin, Hengyu Liu et al.
- **🏷️ 机构**: Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficien Computing, Ministry of Education of China, The Chinese University of Hong Kong
- **会议**: CVPR 2025
- **摘要（中）**: 针对视频异常检测中缺乏细粒度分析（如异常像素）的问题，本文提出Track Any Anomalous Object (TAO)框架，首次将多个细粒度异常对象的检测集成到统一框架中。该方法将异常检测转化为像素级异常对象跟踪，通过将异常分数与分割和跟踪等下游任务关联，消除了阈值调整的需求，并在长视频序列中实现更精确的异常定位。实验表明，TAO在准确性和鲁棒性上设立了新基准。
- **摘要（英）**: Addressing the lack of fine-grained analysis in video anomaly detection, this paper proposes TAO, a framework that integrates detection of multiple fine-grained anomalous objects by transforming the problem into pixel-level tracking. It links anomaly scores to downstream tasks like segmentation and tracking, removing threshold tuning and achieving precise localization, setting new benchmarks in accuracy and robustness.
- **核心贡献**: 提出了TAO框架，将细粒度异常对象检测与跟踪集成，实现无需阈值调整的精确异常定位。
- **创新点**: 将异常检测转化为像素级跟踪问题，并关联下游任务。
- **结果**: TAO在准确性和鲁棒性上设立了新基准。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video anomaly detection (VAD) is crucial in scenarios such as surveillance and autonomous driving, where timely detection of unexpected activities is essential. Although existing methods have primarily focused on detecting anomalous objects in videos -- either by identifying anomalous frames or objects -- they often neglect finer-grained analysis, such as anomalous pixels, which limits their ability to capture a broader range of anomalies. To address this challenge, we propose a new framework called Track Any Anomalous Object (TAO), which introduces a granular video anomaly detection pipeline that, for the first time, integrates the detection of multiple fine-grained anomalous objects into a unified framework. Unlike methods that assign anomaly scores to every pixel, our approach transforms the problem into pixel-level tracking of anomalous objects. By linking anomaly scores to downstream tasks such as segmentation and tracking, our method removes the need for threshold tuning and achieves more precise anomaly localization in long and complex video sequences. Experiments demonstrate that TAO sets new benchmarks in accuracy and robustness. Project page available online.

</details>

### Mamba4D: Efficient 4D Point Cloud Video Understanding with Disentangled Spatial-Temporal State Space Models. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Mamba4D_Efficient_4D_Point_Cloud_Video_Understanding_with_Disentangled_Spatial-Temporal_CVPR_2025_paper.html) · 📚 被引 20
- **作者**: Jiuming Liu, Jinru Han, Lihao Liu, Angelica I. Avilés-Rivero, Chaokang Jiang, Zhe Liu et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,Department of Automation, University of Cambridge, China University of Mining and Technology
- **会议**: CVPR 2025
- **摘要（中）**: ①针对4D点云视频理解中计算效率低和时空建模不足的问题。②提出了Mamba4D，使用解耦的时空状态空间模型进行高效4D点云视频理解。③相比Transformer方法，通过状态空间模型降低计算复杂度并增强长程建模。④摘要未提供具体数据，但方法旨在提升效率和性能。
- **摘要（英）**: This paper addresses the inefficiency and inadequate spatio-temporal modeling in 4D point cloud video understanding. It proposes Mamba4D, using disentangled spatial-temporal state space models for efficient understanding. It improves over Transformer methods by reducing complexity and enhancing long-range modeling, though specific results are not given in the abstract.
- **核心贡献**: 提出解耦时空状态空间模型。
- **创新点**: 状态空间模型用于4D点云。
- **结果**: 未提供具体数据。

### Adapting Pre-trained 3D Models for Point Cloud Video Understanding via Cross-frame Spatio-temporal Perception. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lv_Adapting_Pre-trained_3D_Models_for_Point_Cloud_Video_Understanding_via_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Baixuan Lv, Yaohua Zha, Tao Dai, Xue Yuerong, Ke Chen, Shu-Tao Xia
- **🏷️ 机构**: Tsinghua University, Shenzhen University, Pengcheng Laboratory
- **会议**: CVPR 2025
- **摘要（中）**: ①针对点云视频理解中预训练3D模型适配不足的问题。②提出了跨帧时空感知方法，适配预训练3D模型用于点云视频理解。③相比直接微调，通过跨帧感知增强时空一致性。④摘要未提供具体数据，但方法旨在提升迁移性能。
- **摘要（英）**: This paper addresses the inadequate adaptation of pre-trained 3D models for point cloud video understanding. It proposes a cross-frame spatio-temporal perception method to adapt pre-trained models. It improves over direct fine-tuning by enhancing spatio-temporal consistency, though specific results are not detailed in the abstract.
- **核心贡献**: 提出跨帧时空感知适配方法。
- **创新点**: 跨帧感知增强预训练模型。
- **结果**: 未提供具体数据。

### BOLT: Boost Large Vision-Language Model Without Training for Long-form Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_BOLT_Boost_Large_Vision-Language_Model_Without_Training_for_Long-form_Video_CVPR_2025_paper.html)
- **作者**: Shuming Liu, Chen Zhao, Tianqi Xu, Bernard Ghanem
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2409.14485](https://arxiv.org/abs/2409.14485) · 📚 被引 36
- **作者**: Yan Shu, Zheng Liu, Peitian Zhang, Minghao Qin, Junjie Zhou, Zhengyang Liang et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,School of AI, BAAI
- **会议**: CVPR 2025
- **摘要（中）**: 针对长视频理解中MLLM上下文长度有限和处理成本高的问题，本文提出Video-XL，利用MLLM固有的键值（KV）稀疏化能力压缩视觉输入。方法引入视觉总结标记（VST），为视频每个间隔总结视觉信息，并通过课程学习和复合数据策展进行训练，以克服长视频指令数据稀缺。动态压缩进一步优化压缩质量。实验表明，Video-XL在小时级视频理解上表现优异，有效保留细粒度视觉细节。
- **摘要（英）**: This paper tackles long video understanding in MLLMs, proposing Video-XL with Visual Summarization Tokens to condense visual input via KV sparsification. It uses curriculum learning and composite data curation for training, with dynamic compression. Results show strong performance on hour-scale videos, preserving fine-grained details.
- **核心贡献**: 提出Video-XL和VST机制，实现小时级视频高效理解。
- **创新点**: 利用KV稀疏化能力，通过VST进行视觉总结。
- **结果**: 在长视频理解任务上表现优异，保留细节。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long video understanding poses a significant challenge for current Multi-modal Large Language Models (MLLMs). Notably, the MLLMs are constrained by their limited context lengths and the substantial costs while processing long videos. Although several existing methods attempt to reduce visual tokens, their strategies encounter severe bottleneck, restricting MLLMs' ability to perceive fine-grained visual details. In this work, we propose Video-XL, a novel approach that leverages MLLMs' inherent key-value (KV) sparsification capacity to condense the visual input. Specifically, we introduce a new special token, the Visual Summarization Token (VST), for each interval of the video, which summarizes the visual information within the interval as its associated KV. The VST module is trained by instruction fine-tuning, where two optimizing strategies are offered. 1.Curriculum learning, where VST learns to make small (easy) and large compression (hard) progressively. 2. Composite data curation, which integrates single-image, multi-image, and synthetic data to overcome the scarcity of long-video instruction data. The compression quality is further improved by dynamic compression, which customizes compression granularity based on the information density of different video intervals. Video-XL's effectiveness is verified from three aspects. First, it achieves a superior long-video understanding capability, outperforming state-of-the-art models of comparable sizes across multiple popular benchmarks. Second, it effectively preserves video information, with minimal compression loss even at 16x compression ratio. Third, it realizes outstanding cost-effectiveness, enabling high-quality processing of thousands of frames on a single A100 GPU.

</details>

### VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2412.01095](https://arxiv.org/abs/2412.01095) · 📚 被引 37
- **作者**: Muchao Ye, Weiyang Liu, Pan He
- **🏷️ 机构**: The University of Iowa, Max Planck Institute for Intelligent Systems,T&#x00FC;bingen, Auburn University
- **会议**: CVPR 2025
- **摘要（中）**: 这篇论文针对视频异常检测中现有方法依赖额外推理模块或指令微调导致计算和标注成本高的问题。提出了VERA框架，通过语言化学习使VLM无需修改参数即可进行可解释的视频异常检测。VERA自动将复杂推理分解为针对不同异常模式的引导问题，并作为可学习参数，通过数据驱动的语言交互优化，使用粗粒度标注数据。该方法在检测异常的同时提供可理解的解释，降低了计算和标注开销。
- **摘要（英）**: This paper addresses the high computational and annotation costs in explainable video anomaly detection, where existing methods rely on specialized modules or instruction tuning. It introduces VERA, a verbalized learning framework that enables VLMs to detect anomalies without parameter modification, decomposing reasoning into learnable guiding questions optimized via verbal interactions. VERA provides comprehensible explanations while reducing overhead.
- **核心贡献**: 提出VERA框架，通过语言化学习实现无需参数修改的可解释视频异常检测。
- **创新点**: 将推理分解为可学习的引导问题，利用数据驱动交互优化。
- **结果**: 在降低计算和标注成本的同时，实现异常检测和解释生成。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advancement of vision-language models (VLMs) has established a new paradigm in video anomaly detection (VAD): leveraging VLMs to simultaneously detect anomalies and provide comprehendible explanations for the decisions. Existing work in this direction often assumes the complex reasoning required for VAD exceeds the capabilities of pretrained VLMs. Consequently, these approaches either incorporate specialized reasoning modules during inference or rely on instruction tuning datasets through additional training to adapt VLMs for VAD. However, such strategies often incur substantial computational costs or data annotation overhead. To address these challenges in explainable VAD, we introduce a verbalized learning framework named VERA that enables VLMs to perform VAD without model parameter modifications. Specifically, VERA automatically decomposes the complex reasoning required for VAD into reflections on simpler, more focused guiding questions capturing distinct abnormal patterns. It treats these reflective questions as learnable parameters and optimizes them through data-driven verbal interactions between learner and optimizer VLMs, using coarsely labeled training data. During inference, VERA embeds the learned questions into model prompts to guide VLMs in generating segment-level anomaly scores, which are then refined into frame-level scores via the fusion of scene and temporal contexts. Experimental results on challenging benchmarks demonstrate that the learned questions of VERA are highly adaptable, significantly improving both detection performance and explainability of VLMs for VAD.

</details>

### Apollo: An Exploration of Video Understanding in Large Multimodal Models. **⭐⭐⭐⭐⭐** (相关度: 65%)
- **链接**: [arXiv:2412.10360](https://arxiv.org/abs/2412.10360) · 📚 被引 6
- **作者**: Orr Zohar, Xiaohan Wang, Yann Dubois, Nikhil Mehta, Tong Xiao, Philippe Hansen-Estruch et al.
- **🏷️ 机构**: Meta GenAI, Stanford University
- **会议**: CVPR 2025
- **摘要（中）**: 这篇论文针对视频理解在大规模多模态模型中机制不明、设计决策缺乏依据的问题。进行了全面研究，发现缩放一致性，即小模型和数据集上的设计决策可有效迁移到大模型。基于此，探索了视频采样、架构、数据组成和训练调度等方面，证明fps采样优于均匀帧采样，并确定最佳视觉编码器。该研究为视频-LMMs的设计提供了实证指导，降低训练和评估成本。
- **摘要（英）**: This paper addresses the poor understanding of video understanding mechanisms in large multimodal models, leading to unjustified design decisions. It presents a comprehensive study discovering Scaling Consistency, where decisions on smaller models transfer to larger ones, and explores video sampling, architectures, and data composition. It demonstrates fps sampling is preferable to uniform sampling and identifies best vision encoders, providing empirical guidance.
- **核心贡献**: 揭示缩放一致性并系统探索视频-LMMs设计因素，提供实证指导。
- **创新点**: 发现缩放一致性，使小规模实验有效指导大规模模型设计。
- **结果**: 证明fps采样优于均匀采样，并确定最佳视觉编码器。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the rapid integration of video perception capabilities into Large Multimodal Models (LMMs), the underlying mechanisms driving their video understanding remain poorly understood. Consequently, many design decisions in this domain are made without proper justification or analysis. The high computational cost of training and evaluating such models, coupled with limited open research, hinders the development of video-LMMs. To address this, we present a comprehensive study that helps uncover what effectively drives video understanding in LMMs. We begin by critically examining the primary contributors to the high computational requirements associated with video-LMM research and discover Scaling Consistency, wherein design and training decisions made on smaller models and datasets (up to a critical size) effectively transfer to larger models. Leveraging these insights, we explored many video-specific aspects of video-LMMs, including video sampling, architectures, data composition, training schedules, and more. For example, we demonstrated that fps sampling during training is vastly preferable to uniform frame sampling and which vision encoders are the best for video representation. Guided by these findings, we introduce Apollo, a state-of-the-art family of LMMs that achieve superior performance across different model sizes. Our models can perceive hour-long videos efficiently, with Apollo-3B outperforming most existing $7$B models with an impressive 55.1 on LongVideoBench. Apollo-7B is state-of-the-art compared to 7B LMMs with a 70.9 on MLVU, and 63.3 on Video-MME.

</details>

### M-LLM Based Video Frame Selection for Efficient Video Understanding.
- **链接**: [arXiv:2502.19680](https://arxiv.org/abs/2502.19680) · 📚 被引 17
- **作者**: Kai Hu, Feng Gao, Xiaohan Nie, Peng Zhou, Son Tran, Tal Neiman et al.
- **🏷️ 机构**: Carnegie Mellon University, Amazon, University of Central Florida
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in Multi-Modal Large Language Models (M-LLMs) show promising results in video reasoning. Popular Multi-Modal Large Language Model (M-LLM) frameworks usually apply naive uniform sampling to reduce the number of video frames that are fed into an M-LLM, particularly for long context videos. However, it could lose crucial context in certain periods of a video, so that the downstream M-LLM may not have sufficient visual information to answer a question. To attack this pain point, we propose a light-weight M-LLM -based frame selection method that adaptively select frames that are more relevant to users' queries. In order to train the proposed frame selector, we introduce two supervision signals (i) Spatial signal, where single frame importance score by prompting a M-LLM; (ii) Temporal signal, in which multiple frames selection by prompting Large Language Model (LLM) using the captions of all frame candidates. The selected frames are then digested by a frozen downstream video M-LLM for visual reasoning and question answering. Empirical results show that the proposed M-LLM video frame selector improves the performances various downstream video Large Language Model (video-LLM) across medium (ActivityNet, NExT-QA) and long (EgoSchema, LongVideoBench) context video question answering benchmarks.

</details>

### Online Video Understanding: OVBench and VideoChat-Online.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_Online_Video_Understanding_OVBench_and_VideoChat-Online_CVPR_2025_paper.html) · 📚 被引 2
- **作者**: Zhenpeng Huang, Xinhao Li, Jiaqi Li, Jing Wang, Xiangyu Zeng, Cheng Liang et al.
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology, China Mobile Research Institute
- **会议**: CVPR 2025

### VideoICL: Confidence-based Iterative In-context Learning for Out-of-Distribution Video Understanding.
- **链接**: [arXiv:2412.02186](https://arxiv.org/abs/2412.02186) · [代码](https://github.com/KangsanKim07/VideoICL) · 📚 被引 2
- **作者**: Kangsan Kim, Geon Park, Youngwan Lee, Woongyeong Yeo, Sung Ju Hwang
- **🏷️ 机构**: KAIST
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in multimodal large language models has markedly enhanced the understanding of short videos (typically under one minute), and several evaluation datasets have emerged accordingly. However, these advancements fall short of meeting the demands of real-world applications such as embodied intelligence for long-term decision-making, in-depth movie reviews and discussions, and live sports commentary, all of which require comprehension of long videos spanning several hours. To address this gap, we introduce LVBench, a benchmark specifically designed for long video understanding. Our dataset comprises publicly sourced videos and encompasses a diverse set of tasks aimed at long video comprehension and information extraction. LVBench is designed to challenge multimodal models to demonstrate long-term memory and extended comprehension capabilities. Our extensive evaluations reveal that current multimodal models still underperform on these demanding long video understanding tasks. Through LVBench, we aim to spur the development of more advanced models capable of tackling the complexities of long video comprehension. Our data and code are publicly available at: https://lvbench.github.io.

</details>

### UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00634) · 📚 被引 2
- **作者**: Peiming Li, Ziyi Wang, Yulin Yuan, Hong Liu, Xiangming Meng, Junsong Yuan et al.
- **🏷️ 机构**: Peking University, Shenzhen Graduate School,State Key Laboratory of General Artificial Intelligence, The Zhejiang University-University of Illinois Urbana-Champaign Institute, Zhejiang University, State University of New York at Buffalo
- **会议**: ICCV 2025

### UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00634) · 📚 被引 2
- **作者**: Peiming Li, Ziyi Wang, Yulin Yuan, Hong Liu, Xiangming Meng, Junsong Yuan et al.
- **🏷️ 机构**: Peking University, Shenzhen Graduate School,State Key Laboratory of General Artificial Intelligence, The Zhejiang University-University of Illinois Urbana-Champaign Institute, Zhejiang University, State University of New York at Buffalo
- **会议**: ICCV 2025

### Open-Ended Hierarchical Streaming Video Understanding with Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01926) · 📚 被引 1
- **作者**: Hyolim Kang, Yunsu Park, Youngbeom Yoo, Yeeun Choi, Seon Joo Kim
- **🏷️ 机构**: Yonsei University
- **会议**: ICCV 2025

### ∞-Video: A Training-Free Approach to Long Video Understanding via Continuous-Time Memory Consolidation.
- **链接**: [arXiv:2501.19098](https://arxiv.org/abs/2501.19098)
- **作者**: Saul José Rodrigues dos Santos, António Farinhas, Daniel C. McNamee, André F. T. Martins
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current video-language models struggle with long-video understanding due to limited context lengths and reliance on sparse frame subsampling, often leading to information loss. This paper introduces $\infty$-Video, which can process arbitrarily long videos through a continuous-time long-term memory (LTM) consolidation mechanism. Our framework augments video Q-formers by allowing them to process unbounded video contexts efficiently and without requiring additional training. Through continuous attention, our approach dynamically allocates higher granularity to the most relevant video segments, forming "sticky" memories that evolve over time. Experiments with Video-LLaMA and VideoChat2 demonstrate improved performance in video question-answering tasks, showcasing the potential of continuous-time LTM mechanisms to enable scalable and training-free comprehension of long videos.

</details>

### Improving LLM Video Understanding with 16 Frames Per Second.
- **链接**: [arXiv:2503.13956](https://arxiv.org/abs/2503.13956) · [代码](https://github.com/bytedance/F-16)
- **作者**: Yixuan Li, Changli Tang, Jimin Zhuang, Yudong Yang, Guangzhi Sun, Wei Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### VCA: Video Curious Agent for Long Video Understanding.
- **链接**: [arXiv:2412.10471](https://arxiv.org/abs/2412.10471) · 📚 被引 3
- **作者**: Zeyuan Yang, Delin Chen, Xueyang Yu, Maohao Shen, Chuang Gan
- **🏷️ 机构**: University of Massachusetts,Amherst, Massachusetts Institute of Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long video understanding poses unique challenges due to their temporal complexity and low information density. Recent works address this task by sampling numerous frames or incorporating auxiliary tools using LLMs, both of which result in high computational costs. In this work, we introduce a curiosity-driven video agent with self-exploration capability, dubbed as VCA. Built upon VLMs, VCA autonomously navigates video segments and efficiently builds a comprehensive understanding of complex video sequences. Instead of directly sampling frames, VCA employs a tree-search structure to explore video segments and collect frames. Rather than relying on external feedback or reward, VCA leverages VLM's self-generated intrinsic reward to guide its exploration, enabling it to capture the most crucial information for reasoning. Experimental results on multiple long video benchmarks demonstrate our approach's superior effectiveness and efficiency.

</details>

### VideoAds for Fast-Paced Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02025) · 📚 被引 2
- **作者**: Zheyuan Zhang, Wanying Dou, Linkai Peng, Hongyi Pan, Ulas Bagci, Boqing Gong
- **🏷️ 机构**: Northwestern University, Boston University
- **会议**: ICCV 2025

### DynImg: Key Frames with Visual Prompts are Good Representation for Multi-Modal Video Understanding.
- **链接**: [arXiv:2507.15569](https://arxiv.org/abs/2507.15569) · 📚 被引 0
- **作者**: Xiaoyi Bao, Chenwei Xie, Hao Tang, Tingyu Weng, Xiaofeng Wang, Yun Zheng et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Alibaba Group
- **会议**: ICCV 2025

### LVAgent: Long Video Understanding by Multi-Round Dynamical Collaboration of MLLM Agents.
- **链接**: [arXiv:2503.10200](https://arxiv.org/abs/2503.10200) · [代码](https://github.com/64327069/LVAgent) · 📚 被引 5
- **作者**: Boyu Chen, Zhengrong Yue, Siran Chen, Zikang Wang, Yang Liu, Peng Li et al.
- **🏷️ 机构**: Shenzhen Key Lab of Computer Vision and Pattern Recognition, Shenzhen Institutes of Advanced Technology,Chinese Academy of Sciences, Shanghai Artificial Intelligence Laboratory, Institute for AI Industry Research (AIR), Tsinghua University,Beijing,China
- **会议**: ICCV 2025

### Principles of Visual Tokens for Efficient Video Understanding.
- **链接**: [arXiv:2411.13626](https://arxiv.org/abs/2411.13626) · 📚 被引 1
- **作者**: Xinyue Hao, Gen Li, Shreyank N. Gowda, Robert B. Fisher, Jonathan Huang, Anurag Arnab et al.
- **🏷️ 机构**: University of Edinburgh, University of Nottingham, Scaled Foundations
- **会议**: ICCV 2025

> Existing MLLMs encounter significant challenges in modeling the temporal context within long videos. Currently, mainstream Agent-based methods use external tools to assist a single MLLM in answering long video questions. Despite such tool-based support, a solitary MLLM still offers only a partial understanding of long videos, resulting in limited performance. In order to better address long video tasks, we introduce LVAgent, the first framework enabling multi-round dynamic collaboration of MLLM agents in long video understanding. Our method consists of four key steps: 1) Selection: We pre-select appropriate agents from the model library to form optimal agent teams based on different tasks. 2) Perception: We design an effective retrieval scheme for long videos to improve the coverage of critical temporal segments while maintaining computational efficiency. 3) Action: Agents answer long video questions and exchange reasons. 4) Reflection: We evaluate each agent's performance in each round of discussion and optimize the agent team for dynamic collaboration. The agents iteratively refine their answers by multi-round dynamical collaboration of MLLM agents. LVAgent is the first agent system method that outperforms all closed-source models (like GPT-4o) and open-source models (like InternVL-2.5 and Qwen2-VL) in the long video understanding tasks. Our LVAgent achieves an accuracy of 80\% on four mainstream long video understanding tasks. Notably, LVAgent improves accuracy by 13.3\% on LongVideoBench. Code is available at https://github.com/64327069/LVAgent.

</details>

### VISTA: Enhancing Long-Duration and High-Resolution Video Understanding by Video Spatiotemporal Augmentation.
- **链接**: [arXiv:2412.00927](https://arxiv.org/abs/2412.00927) · 📚 被引 1
- **作者**: Weiming Ren, Huan Yang, Jie Min, Cong Wei, Wenhu Chen
- **🏷️ 机构**: University of Waterloo, 01.AI
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current large multimodal models (LMMs) face significant challenges in processing and comprehending long-duration or high-resolution videos, which is mainly due to the lack of high-quality datasets. To address this issue from a data-centric perspective, we propose VISTA, a simple yet effective Video Spatiotemporal Augmentation framework that synthesizes long-duration and high-resolution video instruction-following pairs from existing video-caption datasets. VISTA spatially and temporally combines videos to create new synthetic videos with extended durations and enhanced resolutions, and subsequently produces question-answer pairs pertaining to these newly synthesized videos. Based on this paradigm, we develop seven video augmentation methods and curate VISTA-400K, a video instruction-following dataset aimed at enhancing long-duration and high-resolution video understanding. Finetuning various video LMMs on our data resulted in an average improvement of 3.3% across four challenging benchmarks for long-video understanding. Furthermore, we introduce the first comprehensive high-resolution video understanding benchmark HRVideoBench, on which our finetuned models achieve a 6.5% performance gain. These results highlight the effectiveness of our framework.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video understanding has made huge strides in recent years, relying largely on the power of transformers. As this architecture is notoriously expensive and video data is highly redundant, research into improving efficiency has become particularly relevant. Some creative solutions include token selection and merging. While most methods succeed in reducing the cost of the model and maintaining accuracy, an interesting pattern arises: most methods do not outperform the baseline of randomly discarding tokens. In this paper we take a closer look at this phenomenon and observe 5 principles of the nature of visual tokens. For example, we observe that the value of tokens follows a clear Pareto-distribution where most tokens have remarkably low value, and just a few carry most of the perceptual information. We build on these and further insights to propose a lightweight video model, LITE, that can select a small number of tokens effectively, outperforming state-of-the-art and existing baselines across datasets (Kinetics-400 and Something-Something-V2) in the challenging trade-off of computation (GFLOPs) vs accuracy. Experiments also show that LITE generalizes across datasets and even other tasks without the need for retraining.

</details>

### Open-Ended Hierarchical Streaming Video Understanding with Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01926) · 📚 被引 1
- **作者**: Hyolim Kang, Yunsu Park, Youngbeom Yoo, Yeeun Choi, Seon Joo Kim
- **🏷️ 机构**: Yonsei University
- **会议**: ICCV 2025

### From Trial to Triumph: Advancing Long Video Understanding via Visual Context Sample Scaling and Self-Reward Alignment.
- **链接**: [arXiv:2503.20472](https://arxiv.org/abs/2503.20472) · 📚 被引 1
- **作者**: Yucheng Suo, Fan Ma, Linchao Zhu, Tianyi Wang, Fengyun Rao, Yi Yang
- **🏷️ 机构**: Zhejiang University, Tencent Inc.
- **会议**: ICCV 2025

> Multi-modal Large language models (MLLMs) show remarkable ability in video understanding. Nevertheless, understanding long videos remains challenging as the models can only process a finite number of frames in a single inference, potentially omitting crucial visual information. To address the challenge, we propose generating multiple predictions through visual context sampling, followed by a scoring mechanism to select the final prediction. Specifically, we devise a bin-wise sampling strategy that enables MLLMs to generate diverse answers based on various combinations of keyframes, thereby enriching the visual context. To determine the final prediction from the sampled answers, we employ a self-reward by linearly combining three scores: (1) a frequency score indicating the prevalence of each option, (2) a marginal confidence score reflecting the inter-intra sample certainty of MLLM predictions, and (3) a reasoning score for different question types, including clue-guided answering for global questions and temporal self-refocusing for local questions. The frequency score ensures robustness through majority correctness, the confidence-aligned score reflects prediction certainty, and the typed-reasoning score addresses cases with sparse key visual information using tailored strategies. Experiments show that this approach covers the correct answer for a high percentage of long video questions, on seven datasets show that our method improves the performance of three MLLMs.

</details>

### MLVU: Benchmarking Multi-task Long Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_MLVU_Benchmarking_Multi-task_Long_Video_Understanding_CVPR_2025_paper.html) · 📚 被引 19
- **作者**: Junjie Zhou, Yan Shu, Bo Zhao, Boya Wu, Zhengyang Liang, Shitao Xiao et al.
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,State Key Laboratory of Networking and Switching Technology, Beijing Academy of Artificial Intelligence, Shanghai Jiao Tong University,School of AI
- **会议**: CVPR 2025

### ViCaS: A Dataset for Combining Holistic and Pixel-level Video Understanding using Captions with Grounded Segmentation.
- **链接**: [arXiv:2412.09754](https://arxiv.org/abs/2412.09754) · 📚 被引 3
- **作者**: Ali Athar, Xueqing Deng, Liang-Chieh Chen
- **🏷️ 机构**: ByteDance Inc.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Do we still need to represent objects explicitly in multimodal large language models (MLLMs)? To one extreme, pre-trained encoders convert images into visual tokens, with which objects and spatiotemporal relationships may be implicitly modeled. To the other extreme, image captions by themselves provide strong empirical performances for understanding tasks, despite missing fine-grained spatiotemporal information. To answer this question, we introduce ObjectMLLM, a framework capable of leveraging arbitrary computer vision algorithm to extract and integrate structured visual representation. Through extensive evaluations on six video question answering benchmarks, we confirm that explicit integration of object-centric representation remains necessary. Surprisingly, we observe that the simple approach of quantizing the continuous, structured object information and representing them as plain text performs the best, offering a data-efficient approach to integrate other visual perception modules into MLLM design. Our code and models are released at https://github.com/brown-palm/ObjectMLLM.

</details>

### HierarQ: Task-Aware Hierarchical Q-Former for Enhanced Video Understanding.
- **链接**: [arXiv:2503.08585](https://arxiv.org/abs/2503.08585) · 📚 被引 7
- **作者**: Shehreen Azad, Vibhav Vineet, Yogesh Singh Rawat
- **🏷️ 机构**: University of Central Florida,Center for Research in Computer Vision, Microsoft Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have shown that agent-based systems leveraging large language models (LLMs) for key information retrieval and integration have emerged as a promising approach for long video understanding. However, these systems face two major challenges. First, they typically perform modeling and reasoning on individual frames, struggling to capture the temporal context of consecutive frames. Second, to reduce the cost of dense frame-level captioning, they adopt sparse frame sampling, which risks discarding crucial information. To overcome these limitations, we propose VideoLucy, a deep memory backtracking framework for long video understanding. Inspired by the human recollection process from coarse to fine, VideoLucy employs a hierarchical memory structure with progressive granularity. This structure explicitly defines the detail level and temporal scope of memory at different hierarchical depths. Through an agent-based iterative backtracking mechanism, VideoLucy systematically mines video-wide, question-relevant deep memories until sufficient information is gathered to provide a confident answer. This design enables effective temporal understanding of consecutive frames while preserving critical details. In addition, we introduce EgoMem, a new benchmark for long video understanding. EgoMem is designed to comprehensively evaluate a model's ability to understand complex events that unfold over time and capture fine-grained details in extremely long videos. Extensive experiments demonstrate the superiority of VideoLucy. Built on open-source models, VideoLucy significantly outperforms state-of-the-art methods on multiple long video understanding benchmarks, achieving performance even surpassing the latest proprietary models such as GPT-4o. Our code and dataset will be made publicly at https://videolucy.github.io

</details>

### Temporal Chain of Thought: Long-Video Understanding by Thinking in Frames.
- **链接**: [arXiv:2507.02001](https://arxiv.org/abs/2507.02001) · 📚 被引 0
- **作者**: Anurag Arnab, Ahmet Iscen, Mathilde Caron, Alireza Fathi, Cordelia Schmid
- **🏷️ 机构**: Google DeepMind, Google, INRIA
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite recent advances in Vision-Language Models (VLMs), long-video understanding remains a challenging problem. Although state-of-the-art long-context VLMs can process around 1000 input frames, they still struggle to effectively leverage this sequence length, and succumb to irrelevant distractors within the context window. We present Temporal Chain of Thought, an inference strategy for video question-answering that curates the model's input context. We use the VLM itself to iteratively identify and extract the most relevant frames from the video, which are then used for answering. We demonstrate how leveraging more computation at inference-time to select the most relevant context leads to improvements in accuracy, in agreement with recent work on inference-time scaling of LLMs. Moreover, we achieve state-of-the-art results on 4 diverse video question-answering datasets, showing consistent improvements with 3 different VLMs. In particular, our method shines on longer videos which would not otherwise fit within the model's context window: On longer videos of more than 1 hour on LVBench, our approach using a context window of 32K outperforms the same VLM using standard inference with a 700K context window by 2.8 points.

</details>

### EPFL-Smart-Kitchen: An Ego-Exo Multi-Modal Dataset for Challenging Action and Motion Understanding in Video-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/80644c59e7ea4bc6267a8b62808e8486-Abstract-Datasets_and_Benchmarks_Track.html) · 📚 被引 0
- **作者**: Andy Bonnetto, Haozhe Qi, Franklin Leong, Matea Tashkovska, Mahdi Rad, Solaiman Shokur et al.
- **🏷️ 机构**: EPFL - EPF Lausanne, EPFL - Switzerland, EPFL
- **会议**: NeurIPS 2025

### Generalizing Single-Frame Supervision to Event-Level Understanding for Video Anomaly Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/092a75a70fb3e822ee9f2efb6eefca7f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Junxi Chen, Liang Li, Yunbin Tu, Li Su, Zhe Xue, Qingming Huang
- **🏷️ 机构**: University of the Chinese Academy of Sciences, Alibaba Group, University of Chinese Academy of Sciences
- **会议**: NeurIPS 2025

### Logic-in-Frames: Dynamic Keyframe Search via Visual Semantic-Logical Verification for Long Video Understanding.
- **链接**: [arXiv:2503.13139](https://arxiv.org/abs/2503.13139) · 📚 被引 2
- **作者**: Weiyu Guo, Ziyang Chen, Shaoguang Wang, JianXiang He, Yijie Xu, Jinhui Ye et al.
- **🏷️ 机构**: Hong Kong University of Science and Technology, Tsinghua University, Tsinghua University, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding long video content is a complex endeavor that often relies on densely sampled frame captions or end-to-end feature selectors, yet these techniques commonly overlook the logical relationships between textual queries and visual elements. In practice, computational constraints necessitate coarse frame subsampling, a challenge analogous to "finding a needle in a haystack." To address this issue, we introduce a semantics-driven search framework that reformulates keyframe selection under the paradigm of Visual Semantic-Logical Search. Specifically, we systematically define four fundamental logical dependencies: 1) spatial co-occurrence, 2) temporal proximity, 3) attribute dependency, and 4) causal order. These relations dynamically update frame sampling distributions through an iterative refinement process, enabling context-aware identification of semantically critical frames tailored to specific query requirements. Our method establishes new SOTA performance on the manually annotated benchmark in key-frame selection metrics. Furthermore, when applied to downstream video question-answering tasks, the proposed approach demonstrates the best performance gains over existing methods on LongVideoBench and Video-MME, validating its effectiveness in bridging the logical gap between textual queries and visual-temporal reasoning. The code will be publicly available.

</details>

### Vid-SME: Membership Inference Attacks against Large Video Understanding Models.
- **链接**: [arXiv:2506.03179](https://arxiv.org/abs/2506.03179) · 📚 被引 0
- **作者**: Qi Li, Runpeng Yu, Xinchao Wang
- **🏷️ 机构**: National University of Singapore
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) demonstrate remarkable capabilities in handling complex multimodal tasks and are increasingly adopted in video understanding applications. However, their rapid advancement raises serious data privacy concerns, particularly given the potential inclusion of sensitive video content, such as personal recordings and surveillance footage, in their training datasets. Determining improperly used videos during training remains a critical and unresolved challenge. Despite considerable progress on membership inference attacks (MIAs) for text and image data in MLLMs, existing methods fail to generalize effectively to the video domain. These methods suffer from poor scalability as more frames are sampled and generally achieve negligible true positive rates at low false positive rates (TPR@Low FPR), mainly due to their failure to capture the inherent temporal variations of video frames and to account for model behavior differences as the number of frames varies. To address these challenges, we introduce Vid-SME, the first membership inference method tailored for video data used in video understanding LLMs (VULLMs). Vid-SME leverages the confidence of model output and integrates adaptive parameterization to compute Sharma-Mittal entropy (SME) for video inputs. By leveraging the SME difference between natural and temporally-reversed video frames, Vid-SME derives robust membership scores to determine whether a given video is part of the model's training set. Experiments on various self-trained and open-sourced VULLMs demonstrate the strong effectiveness of Vid-SME.

</details>

### In the Eye of MLLM: Benchmarking Egocentric Video Intent Understanding with Gaze-Guided Prompting.
- **链接**: [arXiv:2509.07447](https://arxiv.org/abs/2509.07447) · 📚 被引 0
- **作者**: Taiying Peng, Jiacheng Hua, Miao Liu, Feng Lu
- **🏷️ 机构**: Beihang University, Shanghai Artificial Intelligence Laboratory, Tsinghua University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of advanced multimodal large language models (MLLMs) has significantly enhanced AI assistants' ability to process complex information across modalities. Recently, egocentric videos, by directly capturing user focus, actions, and context in an unified coordinate, offer an exciting opportunity to enable proactive and personalized AI user experiences with MLLMs. However, existing benchmarks overlook the crucial role of gaze as an indicator of user intent. To address this gap, we introduce EgoGazeVQA, an egocentric gaze-guided video question answering benchmark that leverages gaze information to improve the understanding of longer daily-life videos. EgoGazeVQA consists of gaze-based QA pairs generated by MLLMs and refined by human annotators. Our experiments reveal that existing MLLMs struggle to accurately interpret user intentions. In contrast, our gaze-guided intent prompting methods significantly enhance performance by integrating spatial, temporal, and intent-related cues. We further conduct experiments on gaze-related fine-tuning and analyze how gaze estimation accuracy impacts prompting effectiveness. These results underscore the value of gaze for more personalized and effective AI assistants in egocentric settings. Project page: https://taiyi98.github.io/projects/EgoGazeVQA

</details>

### Adaptive Keyframe Sampling for Long Video Understanding.
- **链接**: [arXiv:2502.21271](https://arxiv.org/abs/2502.21271) · [代码](https://github.com/ncTimTang/AKS) · 📚 被引 30
- **作者**: Xi Tang, Jihao Qiu, Lingxi Xie, Yunjie Tian, Jianbin Jiao, Qixiang Ye
- **🏷️ 机构**: University of Chinese Academy of Sciences, University at Buffalo, SUNY
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have enabled open-world visual understanding by injecting visual input as extra tokens into large language models (LLMs) as contexts. However, when the visual input changes from a single image to a long video, the above paradigm encounters difficulty because the vast amount of video tokens has significantly exceeded the maximal capacity of MLLMs. Therefore, existing video-based MLLMs are mostly established upon sampling a small portion of tokens from input data, which can cause key information to be lost and thus produce incorrect answers. This paper presents a simple yet effective algorithm named Adaptive Keyframe Sampling (AKS). It inserts a plug-and-play module known as keyframe selection, which aims to maximize the useful information with a fixed number of video tokens. We formulate keyframe selection as an optimization involving (1) the relevance between the keyframes and the prompt, and (2) the coverage of the keyframes over the video, and present an adaptive algorithm to approximate the best solution. Experiments on two long video understanding benchmarks validate that Adaptive Keyframe Sampling improves video QA accuracy (beyond strong baselines) upon selecting informative keyframes. Our study reveals the importance of information pre-filtering in video-based MLLMs. Code is available at https://github.com/ncTimTang/AKS.

</details>

### Re-thinking Temporal Search for Long-Form Video Understanding.
- **链接**: [arXiv:2504.02259](https://arxiv.org/abs/2504.02259) · 📚 被引 7
- **作者**: Jinhui Ye, Zihan Wang, Haosen Sun, Keshigeyan Chandrasegaran, Zane Durante, Cristóbal Eyzaguirre et al.
- **🏷️ 机构**: Stanford University, Northwestern University, Carnegie Mellon University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficiently understanding long-form videos remains a significant challenge in computer vision. In this work, we revisit temporal search paradigms for long-form video understanding and address a fundamental issue pertaining to all state-of-the-art (SOTA) long-context vision-language models (VLMs). Our contributions are twofold: First, we frame temporal search as a Long Video Haystack problem: finding a minimal set of relevant frames (e.g., one to five) from tens of thousands based on specific queries. Upon this formulation, we introduce LV-Haystack, the first dataset with 480 hours of videos, 15,092 human-annotated instances for both training and evaluation aiming to improve temporal search quality and efficiency. Results on LV-Haystack highlight a significant research gap in temporal search capabilities, with current SOTA search methods only achieving 2.1% temporal F1 score on the Longvideobench subset. Next, inspired by visual search in images, we propose a lightweight temporal search framework, T* that reframes costly temporal search as spatial search. T* leverages powerful visual localization techniques commonly used in images and introduces an adaptive zooming-in mechanism that operates across both temporal and spatial dimensions. Extensive experiments show that integrating T* with existing methods significantly improves SOTA long-form video understanding. Under an inference budget of 32 frames, T* improves GPT-4o's performance from 50.5% to 53.1% and LLaVA-OneVision-OV-72B's performance from 56.5% to 62.4% on the Longvideobench XL subset. Our code, benchmark, and models are provided in the Supplementary material.

</details>

### Holmes-VAU: Towards Long-term Video Anomaly Understanding at Any Granularity.
- **链接**: [arXiv:2412.06171](https://arxiv.org/abs/2412.06171) · [代码](https://github.com/pipixin321/HolmesVAU) · 📚 被引 22
- **作者**: Huaxin Zhang, Xiaohao Xu, Xiang Wang, Jialong Zuo, Xiaonan Huang, Changxin Gao et al.
- **🏷️ 机构**: Huazhong University of Science and Technology,Key Laboratory of Image Processing and Intelligent Control, School of Artificial Intelligence and Automation, University of Michigan,Ann Arbor, Kanagawa University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> How can we enable models to comprehend video anomalies occurring over varying temporal scales and contexts? Traditional Video Anomaly Understanding (VAU) methods focus on frame-level anomaly prediction, often missing the interpretability of complex and diverse real-world anomalies. Recent multimodal approaches leverage visual and textual data but lack hierarchical annotations that capture both short-term and long-term anomalies. To address this challenge, we introduce HIVAU-70k, a large-scale benchmark for hierarchical video anomaly understanding across any granularity. We develop a semi-automated annotation engine that efficiently scales high-quality annotations by combining manual video segmentation with recursive free-text annotation using large language models (LLMs). This results in over 70,000 multi-granular annotations organized at clip-level, event-level, and video-level segments. For efficient anomaly detection in long videos, we propose the Anomaly-focused Temporal Sampler (ATS). ATS integrates an anomaly scorer with a density-aware sampler to adaptively select frames based on anomaly scores, ensuring that the multimodal LLM concentrates on anomaly-rich regions, which significantly enhances both efficiency and accuracy. Extensive experiments demonstrate that our hierarchical instruction data markedly improves anomaly comprehension. The integrated ATS and visual-language model outperform traditional methods in processing long videos. Our benchmark and model are publicly available at https://github.com/pipixin321/HolmesVAU.

</details>

### Action Detail Matters: Refining Video Recognition with Local Action Queries.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Action_Detail_Matters_Refining_Video_Recognition_with_Local_Action_Queries_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Mengmeng Wang, Zeyi Huang, Xiangjie Kong, Guojiang Shen, Guang Dai, Jingdong Wang et al.
- **🏷️ 机构**: Zhejiang University of Technology, Huawei, State Grid Corporation of China,SGIT AI Lab
- **会议**: CVPR 2025

### UniViT: Unifying Image and Video Understanding in One Vision Encoder.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/69b6de0de842bfedbc40ed6e162b4233-Abstract-Conference.html) · 📚 被引 0
- **作者**: Feilong Tang, Xiang An, Haolin Yang, Yin Xie, Kaicheng Yang, Ming Hu et al.
- **🏷️ 机构**: Monash University, University of Chicago, DEEP GLINT
- **会议**: NeurIPS 2025

### Universal Visuo-Tactile Video Understanding for Embodied Interaction.
- **链接**: [arXiv:2505.22566](https://arxiv.org/abs/2505.22566) · 📚 被引 0
- **作者**: Yifan Xie, Mingyang Li, Shoujie Li, Xingting Li, Guangyu Chen, Fei Ma et al.
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Tsinghua University, University of Science and Technology Beijing
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Tactile perception is essential for embodied agents to understand physical attributes of objects that cannot be determined through visual inspection alone. While existing approaches have made progress in visual and language modalities for physical understanding, they fail to effectively incorporate tactile information that provides crucial haptic feedback for real-world interaction. In this paper, we present VTV-LLM, the first multi-modal large language model for universal Visuo-Tactile Video (VTV) understanding that bridges the gap between tactile perception and natural language. To address the challenges of cross-sensor and cross-modal integration, we contribute VTV150K, a comprehensive dataset comprising 150,000 video frames from 100 diverse objects captured across three different tactile sensors (GelSight Mini, DIGIT, and Tac3D), annotated with four fundamental tactile attributes (hardness, protrusion, elasticity, and friction). We develop a novel three-stage training paradigm that includes VTV enhancement for robust visuo-tactile representation, VTV-text alignment for cross-modal correspondence, and text prompt finetuning for natural language generation. Our framework enables sophisticated tactile reasoning capabilities including feature assessment, comparative analysis, scenario-based decision making and so on. Experimental evaluations demonstrate that VTV-LLM achieves superior performance in tactile video understanding tasks, establishing a foundation for more intuitive human-machine interaction in tactile domains.

</details>

### AdaVideoRAG: Omni-Contextual Adaptive Retrieval-Augmented Efficient Long Video Understanding.
- **链接**: [arXiv:2506.13589](https://arxiv.org/abs/2506.13589) · 📚 被引 0
- **作者**: Zhucun Xue, Jiangning Zhang, Xurong Xie, Yuxuan Cai, Yong Liu, Xiangtai Li et al.
- **🏷️ 机构**: Zhejiang University (ZJU), Youtu Lab, Tencent, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) perform well in video understanding but degrade on long videos due to fixed-length context and weak long-term dependency modeling. Retrieval-Augmented Generation (RAG) can expand knowledge dynamically, yet existing video RAG schemes adopt fixed retrieval paradigms that ignore query difficulty. This uniform design causes redundant computation and latency for simple queries, while coarse retrieval for complex, multi-hop reasoning can miss key information. Such single-step retrieval severely limits the trade-off between efficiency and cognitive depth. We propose AdaVideoRAG, an adaptive RAG framework for long-video understanding. A lightweight intent classifier dynamically selects suitable retrieval schemes according to query complexity from the simplest to the most sophisticated. We design an Omni-Knowledge Indexing module that extracts and organizes multi-modal information into three databases: (1) a text base built from clip captions, ASR, and OCR; (2) a visual base; and (3) a knowledge graph for deep semantic understanding. This supports hierarchical knowledge access, from naive retrieval to graph-based retrieval, balancing resource cost and reasoning ability. To evaluate deep understanding, we further construct the HiVU benchmark. Experiments show that AdaVideoRAG significantly improves both efficiency and accuracy on long-video QA tasks and can be seamlessly plugged into existing MLLMs through lightweight APIs, establishing a new paradigm for adaptive retrieval-augmented video analysis.

</details>

### LiveStar: Live Streaming Assistant for Real-World Online Video Understanding.
- **链接**: [arXiv:2511.05299](https://arxiv.org/abs/2511.05299) · 📚 被引 0
- **作者**: Zhenyu Yang, Kairui Zhang, Yuhang Hu, Bing Wang, Shengsheng Qian, Bin Wen et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, ShanghaiTech University, Zhengzhou University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite significant progress in Video Large Language Models (Video-LLMs) for offline video understanding, existing online Video-LLMs typically struggle to simultaneously process continuous frame-by-frame inputs and determine optimal response timing, often compromising real-time responsiveness and narrative coherence. To address these limitations, we introduce LiveStar, a pioneering live streaming assistant that achieves always-on proactive responses through adaptive streaming decoding. Specifically, LiveStar incorporates: (1) a training strategy enabling incremental video-language alignment for variable-length video streams, preserving temporal consistency across dynamically evolving frame sequences; (2) a response-silence decoding framework that determines optimal proactive response timing via a single forward pass verification; (3) memory-aware acceleration via peak-end memory compression for online inference on 10+ minute videos, combined with streaming key-value cache to achieve 1.53x faster inference. We also construct an OmniStar dataset, a comprehensive dataset for training and benchmarking that encompasses 15 diverse real-world scenarios and 5 evaluation tasks for online video understanding. Extensive experiments across three benchmarks demonstrate LiveStar's state-of-the-art performance, achieving an average 19.5% improvement in semantic correctness with 18.1% reduced timing difference compared to existing online Video-LLMs, while improving FPS by 12.0% across all five OmniStar tasks. Our model and dataset can be accessed at https://github.com/yzy-bupt/LiveStar.

</details>

### StreamForest: Efficient Online Video Understanding with Persistent Event Memory.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6dd91fec726dbed8915a1fbadd91d1d2-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xiangyu Zeng, Kefan Qiu, Qingyu Zhang, Xinhao Li, Jing Wang, Jiaxin Li et al.
- **🏷️ 机构**: Nanjing University; Shanghai AI Lab, nanjing university, Nanjing University
- **会议**: NeurIPS 2025

### FlexSelect: Flexible Token Selection for Efficient Long Video Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/949c57d30f8791e3ae42646081b3c102-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yunzhu Zhang, Yu Lu, Tianyi Wang, Fengyun Rao, Yi Yang, Linchao Zhu
- **🏷️ 机构**: Zhejiang University, National University of Singapore, WeChat, Tencent Inc.
- **会议**: NeurIPS 2025

### ReAgent-V: A Reward-Driven Multi-Agent Framework for Video Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/de72a54c3d39523b0dd06b64ffa6d50d-Abstract-Conference.html) · 📚 被引 1
- **作者**: Yiyang Zhou, Yangfan He, Yaofeng Su, Siwei Han, Joel Jang, Gedas Bertasius et al.
- **🏷️ 机构**: The University of North Carolina at Chapel Hill, JD.com, Fudan University
- **会议**: NeurIPS 2025

### State Space Prompting via Gathering and Spreading Spatio-Temporal Information for Video Understanding.
- **链接**: [arXiv:2510.12160](https://arxiv.org/abs/2510.12160) · 📚 被引 0
- **作者**: Jiahuan Zhou, Kai Zhu, Zhenyu Cui, Zichen Liu, Xu Zou, Gang Hua
- **🏷️ 机构**: Peking University, Renmin University of China, The Hong Kong University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, pre-trained state space models have shown great potential for video classification, which sequentially compresses visual tokens in videos with linear complexity, thereby improving the processing efficiency of video data while maintaining high performance. To apply powerful pre-trained models to downstream tasks, prompt learning is proposed to achieve efficient downstream task adaptation with only a small number of fine-tuned parameters. However, the sequentially compressed visual prompt tokens fail to capture the spatial and temporal contextual information in the video, thus limiting the effective propagation of spatial information within a video frame and temporal information between frames in the state compression model and the extraction of discriminative information. To tackle the above issue, we proposed a State Space Prompting (SSP) method for video understanding, which combines intra-frame and inter-frame prompts to aggregate and propagate key spatiotemporal information in the video. Specifically, an Intra-Frame Gathering (IFG) module is designed to aggregate spatial key information within each frame. Besides, an Inter-Frame Spreading (IFS) module is designed to spread discriminative spatio-temporal information across different frames. By adaptively balancing and compressing key spatio-temporal information within and between frames, our SSP effectively propagates discriminative information in videos in a complementary manner. Extensive experiments on four video benchmark datasets verify that our SSP significantly outperforms existing SOTA methods by 2.76% on average while reducing the overhead of fine-tuning parameters.

</details>

### Disentangled Concepts Speak Louder Than Words: Explainable Video Action Recognition.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/a5e146ca55a2b18be41942cfa677123d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Jongseo Lee, Wooil Lee, Gyeong-Moon Park, Seong Tae Kim, Jinwoo Choi
- **🏷️ 机构**: Kyung Hee University, Korea University
- **会议**: NeurIPS 2025

### Storyboard-guided Alignment for Fine-grained Video Action Recognition.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/528388f1ad3a481249a97cbb698d2fe6-Abstract-Conference.html) · 📚 被引 0
- **作者**: Enqi Liu, Liyuan Pan, Yan Yang, Yiran Zhong, Zhijing Wu, Xinxiao Wu et al.
- **🏷️ 机构**: Beijing Institute of Technology, Australian National University, Shanghai AI Lab
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Few-Shot Action Recognition (FSAR) aims to train a model with only a few labeled video instances. A key challenge in FSAR is handling divergent narrative trajectories for precise video matching. While the frame- and tuple-level alignment approaches have been promising, their methods heavily rely on pre-defined and length-dependent alignment units (e.g., frames or tuples), which limits flexibility for actions of varying lengths and speeds. In this work, we introduce a novel TEmporal Alignment-free Matching (TEAM) approach, which eliminates the need for temporal units in action representation and brute-force alignment during matching. Specifically, TEAM represents each video with a fixed set of pattern tokens that capture globally discriminative clues within the video instance regardless of action length or speed, ensuring its flexibility. Furthermore, TEAM is inherently efficient, using token-wise comparisons to measure similarity between videos, unlike existing methods that rely on pairwise comparisons for temporal alignment. Additionally, we propose an adaptation process that identifies and removes common information across classes, establishing clear boundaries even between novel categories. Extensive experiments demonstrate the effectiveness of TEAM. Codes are available at github.com/leesb7426/TEAM.

</details>

## 跨领域论文（完整笔记在其他领域）

- Anomize: Better Open Vocabulary Video Anomaly Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- When the Future Becomes the Past: Taming Temporal Correspondence for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Self-supervised ControlNet with Spatio-Temporal Mamba for Real-world Video Super-resolution. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)

## 🆕 增量新增

### LVBench: An Extreme Long Video Understanding Benchmark. **⭐⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2406.08035](https://arxiv.org/abs/2406.08035) · 📚 被引 14
- **作者**: Weihan Wang, Zehai He, Wenyi Hong, Yean Cheng, Xiaohan Zhang, Ji Qi et al.
- **🏷️ 机构**: Zhipu AI, Tsinghua University
- **会议**: ICCV 2025
- **摘要（中）**: ①针对现有大多模态模型在长视频（数小时）理解上的不足，提出了LVBench基准。②LVBench包含公开来源的视频，设计了多种任务以评估长视频理解和信息提取能力。③相比现有短视频基准，LVBench强调长期记忆和扩展理解能力，更贴近实际应用如具身智能和体育评论。④评估显示当前多模态模型在这些任务上表现不佳，表明该基准具有挑战性。
- **摘要（英）**: This paper introduces LVBench, a benchmark for extreme long video understanding, addressing the gap in evaluating models on multi-hour videos. It includes diverse tasks for long-term comprehension and information extraction. Evaluations show current multimodal models underperform, highlighting the need for advanced models.
- **核心贡献**: 提出了首个针对数小时长视频理解的基准LVBench。
- **创新点**: 聚焦于长期记忆和扩展理解能力。
- **结果**: 现有模型在LVBench上表现不佳，验证了任务的难度。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent progress in multimodal large language models has markedly enhanced the understanding of short videos (typically under one minute), and several evaluation datasets have emerged accordingly. However, these advancements fall short of meeting the demands of real-world applications such as embodied intelligence for long-term decision-making, in-depth movie reviews and discussions, and live sports commentary, all of which require comprehension of long videos spanning several hours. To address this gap, we introduce LVBench, a benchmark specifically designed for long video understanding. Our dataset comprises publicly sourced videos and encompasses a diverse set of tasks aimed at long video comprehension and information extraction. LVBench is designed to challenge multimodal models to demonstrate long-term memory and extended comprehension capabilities. Our extensive evaluations reveal that current multimodal models still underperform on these demanding long video understanding tasks. Through LVBench, we aim to spur the development of more advanced models capable of tackling the complexities of long video comprehension. Our data and code are publicly available at: https://lvbench.github.io.

</details>

### CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2412.12075](https://arxiv.org/abs/2412.12075)
- **作者**: Guo Chen, Yicheng Liu, Yifei Huang, Baoqi Pei, Jilan Xu, Yuping He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对长视频理解中现有基准缺乏对线索推理能力评估的问题。②提出了CG-Bench基准，包含基于线索的问题回答任务，要求模型利用视频中的关键线索进行推理。③相比已有基准，更强调线索定位和推理过程，而非简单的事实问答。④具体效果未在摘要中提供，但基准设计旨在推动长视频推理研究。
- **摘要（英）**: This paper addresses the lack of clue-grounded reasoning evaluation in long video understanding. It introduces CG-Bench, a benchmark with clue-based question answering tasks that require models to locate and reason over key video clues. Compared to existing benchmarks, it emphasizes reasoning over simple fact retrieval, aiming to advance long video inference.
- **核心贡献**: 提出了线索导向的长视频问答基准。
- **创新点**: 强调线索推理的基准设计。
- **结果**: 推动长视频推理评估发展。

### SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2502.10810](https://arxiv.org/abs/2502.10810)
- **作者**: Zhenyu Yang, Yuhang Hu, Zemin Du, Dizhan Xue, Shengsheng Qian, Jiahong Wu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025
- **摘要（中）**: ①针对流式视频理解中缺乏时间多轮对话基准的问题。②提出了SVBench基准，包含时间多轮对话任务，评估模型在流式视频中的连续交互能力。③相比静态视频问答，更关注时间动态和对话连贯性。④具体效果未在摘要中提供，但基准旨在促进流式视频理解研究。
- **摘要（英）**: This paper addresses the gap in temporal multi-turn dialogue benchmarks for streaming video understanding. It proposes SVBench, featuring temporal multi-turn dialogues to evaluate continuous interaction in streaming videos. Unlike static QA, it focuses on temporal dynamics and dialogue coherence, aiming to advance streaming video research.
- **核心贡献**: 提出了流式视频时间多轮对话基准。
- **创新点**: 结合时间动态与多轮对话。
- **结果**: 促进流式视频理解评估。

### TUMTraf VideoQA: Dataset and Benchmark for Unified Spatio-Temporal Video Understanding in Traffic Scenes. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhou25g.html)
- **作者**: Xingcheng Zhou, Konstantinos Larintzakis, Hao Guo, Walter Zimmer, Mingyu Liu, Hu Cao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025
- **摘要（中）**: ①针对交通场景中视频理解缺乏统一时空基准的问题。②提出了TUMTraf VideoQA数据集和基准，用于统一时空视频理解，涵盖交通场景中的问答任务。③相比已有交通数据集，更强调时空联合推理和多任务统一。④具体效果未在摘要中提供，但基准旨在推动自动驾驶感知研究。
- **摘要（英）**: This paper addresses the lack of unified spatio-temporal benchmarks for traffic scene video understanding. It introduces TUMTraf VideoQA, a dataset and benchmark for unified spatio-temporal reasoning in traffic scenes. Compared to existing datasets, it emphasizes joint spatial-temporal inference and multi-task unification, aiming to advance autonomous driving perception.
- **核心贡献**: 提出了交通场景统一时空视频理解基准。
- **创新点**: 统一时空推理与多任务设计。
- **结果**: 推动自动驾驶视频理解研究。

### EgoExoBench: A Benchmark for First- and Third-person View Video Understanding in MLLMs. **⭐⭐** (相关度: 25%)
- **链接**: [arXiv:2507.18342](https://arxiv.org/abs/2507.18342)
- **作者**: Yuping He, Yifei Huang, Guo Chen, Baoqi Pei, Jilan Xu, Tong Lu et al.
- **🏷️ 机构**: Nanjing University, The University of Tokyo, Zhejiang University
- **会议**: NeurIPS 2025
- **摘要（中）**: ①针对MLLMs在跨视角（第一人称和第三人称）视频理解与推理能力未探索的问题。②提出了EgoExoBench基准，包含超过7300个问答对，覆盖11个子任务，分为语义对齐、视角关联和时间推理三大挑战。③相比现有基准，该基准首次系统评估MLLMs的自我-外部视角推理。④评估13个MLLMs显示模型在单视角任务上表现优异，但在跨视角语义对齐和关联上存在困难。
- **摘要（英）**: This paper introduces EgoExoBench, the first benchmark for egocentric-exocentric video understanding, with over 7,300 QA pairs across 11 sub-tasks. Evaluation of 13 MLLMs shows they excel on single-view tasks but struggle with cross-view semantic alignment and temporal reasoning.
- **核心贡献**: 提出了首个跨视角视频理解基准。
- **创新点**: 系统评估MLLMs的自我-外部视角推理能力。
- **结果**: MLLMs在跨视角任务上表现不佳。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Transferring and integrating knowledge across first-person (egocentric) and third-person (exocentric) viewpoints is intrinsic to human intelligence, enabling humans to learn from others and convey insights from their own experiences. Despite rapid progress in multimodal large language models (MLLMs), their ability to perform such cross-view reasoning remains unexplored. To address this, we introduce EgoExoBench, the first benchmark for egocentric-exocentric video understanding and reasoning. Built from publicly available datasets, EgoExoBench comprises over 7,300 question-answer pairs spanning eleven sub-tasks organized into three core challenges: semantic alignment, viewpoint association, and temporal reasoning. We evaluate 13 state-of-the-art MLLMs and find that while these models excel on single-view tasks, they struggle to align semantics across perspectives, accurately associate views, and infer temporal dynamics in the ego-exo context. We hope EgoExoBench can serve as a valuable resource for research on embodied agents and intelligent assistants seeking human-like cross-view intelligence.

</details>

### VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding. **⭐⭐⭐⭐** (相关度: 55%)
- **链接**: [arXiv:2412.03735](https://arxiv.org/abs/2412.03735) · 📚 被引 14
- **作者**: Chaoyu Li, Eun Woo Im, Pooyan Fazli
- **🏷️ 机构**: Arizona State University
- **会议**: CVPR 2025
- **摘要（中）**: ①针对多模态大模型在视频理解中的时间幻觉问题，现有研究不足。②构建VidHalluc基准，包含5002个视频，评估动作、时间序列和场景转换三个维度的幻觉。③提出DINO-HEAL方法，利用DINOv2的空间显著性重加权视觉特征，无需训练即可减少幻觉。④实验显示大多数MLLM易受幻觉影响，DINO-HEAL平均提升3.02%的幻觉缓解性能。
- **摘要（英）**: This paper addresses temporal hallucinations in multimodal LLMs for video understanding. It introduces VidHalluc, a large benchmark with 5,002 videos, and proposes DINO-HEAL, a training-free method using DINOv2 saliency to reweight visual features. The method achieves an average 3.02% improvement in hallucination mitigation.
- **核心贡献**: 构建VidHalluc基准并提出DINO-HEAL方法缓解时间幻觉。
- **创新点**: 利用空间显著性重加权视觉特征，无需训练减少幻觉。
- **结果**: 平均提升3.02%的幻觉缓解性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal large language models (MLLMs) have recently shown significant advancements in video understanding, excelling in content reasoning and instruction-following tasks. However, hallucination, where models generate inaccurate or misleading content, remains underexplored in the video domain. Building on the observation that MLLM visual encoders often fail to distinguish visually different yet semantically similar video pairs, we introduce VidHalluc, the largest benchmark designed to examine hallucinations in MLLMs for video understanding. It consists of 5,002 videos, paired to highlight cases prone to hallucinations. VidHalluc assesses hallucinations across three critical dimensions: (1) action, (2) temporal sequence, and (3) scene transition. Comprehensive testing shows that most MLLMs are vulnerable to hallucinations across these dimensions. Furthermore, we propose DINO-HEAL, a training-free method that reduces hallucinations by incorporating spatial saliency from DINOv2 to reweight visual features during inference. Our results show that DINO-HEAL consistently improves performance on VidHalluc, achieving an average improvement of 3.02% in mitigating hallucinations across all tasks. Both the VidHalluc benchmark and DINO-HEAL code are available at https://people-robots.github.io/vidhalluc.

</details>

### VideoAutoArena: An Automated Arena for Evaluating Large Multimodal Models in Video Analysis through User Simulation. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2411.13281](https://arxiv.org/abs/2411.13281) · 📚 被引 2
- **作者**: Ziyang Luo, Haoning Wu, Dongxu Li, Jing Ma, Mohan S. Kankanhalli, Junnan Li
- **🏷️ 机构**: Salesforce AI Research, Nanyang Technological University, The Australian National University
- **会议**: CVPR 2025
- **摘要（中）**: ①针对现有视频理解评估依赖多选题，难以捕捉真实用户复杂需求的问题。②提出VideoAutoArena，基于竞技场框架的自动评估基准，通过用户模拟生成开放式自适应问题。③采用修改的ELO评分系统进行公平比较，并构建黄金标准验证与人类判断的一致性。④实验表明该基准与人类判断高度一致，并引入故障驱动评估增强鲁棒性。
- **摘要（英）**: This paper addresses the limitations of traditional video evaluation methods. It introduces VideoAutoArena, an arena-style benchmark with user simulation for open-ended questions and a modified ELO system. The benchmark aligns strongly with human judgment and includes fault-driven evaluation.
- **核心贡献**: 提出VideoAutoArena，一个自动化的视频理解评估基准。
- **创新点**: 利用用户模拟和ELO评分系统实现可扩展的开放式评估。
- **结果**: 与人类判断高度一致，支持多模型公平比较。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large multimodal models (LMMs) with advanced video analysis capabilities have recently garnered significant attention. However, most evaluations rely on traditional methods like multiple-choice questions in benchmarks such as VideoMME and LongVideoBench, which are prone to lack the depth needed to capture the complex demands of real-world users. To address this limitation-and due to the prohibitive cost and slow pace of human annotation for video tasks-we introduce VideoAutoArena, an arena-style benchmark inspired by LMSYS Chatbot Arena's framework, designed to automatically assess LMMs' video analysis abilities. VideoAutoArena utilizes user simulation to generate open-ended, adaptive questions that rigorously assess model performance in video understanding. The benchmark features an automated, scalable evaluation framework, incorporating a modified ELO Rating System for fair and continuous comparisons across multiple LMMs. To validate our automated judging system, we construct a 'gold standard' using a carefully curated subset of human annotations, demonstrating that our arena strongly aligns with human judgment while maintaining scalability. Additionally, we introduce a fault-driven evolution strategy, progressively increasing question complexity to push models toward handling more challenging video analysis scenarios. Experimental results demonstrate that VideoAutoArena effectively differentiates among state-of-the-art LMMs, providing insights into model strengths and areas for improvement. To further streamline our evaluation, we introduce VideoAutoBench as an auxiliary benchmark, where human annotators label winners in a subset of VideoAutoArena battles. We use GPT-4o as a judge to compare responses against these human-validated answers. Together, VideoAutoArena and VideoAutoBench offer a cost-effective, and scalable framework for evaluating LMMs in user-centric video analysis.

</details>

### DIV-FF: Dynamic Image-Video Feature Fields For Environment Understanding in Egocentric Videos.
- **链接**: [arXiv:2503.08344](https://arxiv.org/abs/2503.08344)
- **作者**: Lorenzo Mur-Labadia, Josechu Guerrero, Ruben Martinez-Cantin
- **🏷️ 机构**: I3A - Universidad de Zaragoza
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Environment understanding in egocentric videos is an important step for applications like robotics, augmented reality and assistive technologies. These videos are characterized by dynamic interactions and a strong dependence on the wearer engagement with the environment. Traditional approaches often focus on isolated clips or fail to integrate rich semantic and geometric information, limiting scene comprehension. We introduce Dynamic Image-Video Feature Fields (DIV FF), a framework that decomposes the egocentric scene into persistent, dynamic, and actor based components while integrating both image and video language features. Our model enables detailed segmentation, captures affordances, understands the surroundings and maintains consistent understanding over time. DIV-FF outperforms state-of-the-art methods, particularly in dynamically evolving scenarios, demonstrating its potential to advance long term, spatio temporal scene understanding.

</details>

### OVO-Bench: How Far is Your Video-LLMs from Real-World Online Video Understanding?
- **链接**: [arXiv:2501.05510](https://arxiv.org/abs/2501.05510) · 📚 被引 5
- **作者**: Junbo Niu, Yifei Li, Ziyang Miao, Chunjiang Ge, Yuanhang Zhou, Qihao He et al.
- **🏷️ 机构**: Shanghai Artificial Intelligence Laboratory, Beihang University, Tsinghua University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Temporal Awareness, the ability to reason dynamically based on the timestamp when a question is raised, is the key distinction between offline and online video LLMs. Unlike offline models, which rely on complete videos for static, post hoc analysis, online models process video streams incrementally and dynamically adapt their responses based on the timestamp at which the question is posed. Despite its significance, temporal awareness has not been adequately evaluated in existing benchmarks. To fill this gap, we present OVO-Bench (Online-VideO-Benchmark), a novel video benchmark that emphasizes the importance of timestamps for advanced online video understanding capability benchmarking. OVO-Bench evaluates the ability of video LLMs to reason and respond to events occurring at specific timestamps under three distinct scenarios: (1) Backward tracing: trace back to past events to answer the question. (2) Real-time understanding: understand and respond to events as they unfold at the current timestamp. (3) Forward active responding: delay the response until sufficient future information becomes available to answer the question accurately. OVO-Bench comprises 12 tasks, featuring 644 unique videos and approximately human-curated 2,800 fine-grained meta-annotations with precise timestamps. We combine automated generation pipelines with human curation. With these high-quality samples, we further developed an evaluation pipeline to systematically query video LLMs along the video timeline. Evaluations of nine Video-LLMs reveal that, despite advancements on traditional benchmarks, current models struggle with online video understanding, showing a significant gap compared to human agents. We hope OVO-Bench will drive progress in video LLMs and inspire future research in online video reasoning. Our benchmark and code can be accessed at https://github.com/JoeLeelyf/OVO-Bench.

</details>

### Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding.
- **链接**: [arXiv:2412.00493](https://arxiv.org/abs/2412.00493) · 📚 被引 18
- **作者**: Duo Zheng, Shijia Huang, Liwei Wang
- **🏷️ 机构**: The Chinese University of Hong Kong
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The rapid advancement of Multimodal Large Language Models (MLLMs) has significantly impacted various multimodal tasks. However, these models face challenges in tasks that require spatial understanding within 3D environments. Efforts to enhance MLLMs, such as incorporating point cloud features, have been made, yet a considerable gap remains between the models' learned representations and the inherent complexity of 3D scenes. This discrepancy largely stems from the training of MLLMs on predominantly 2D data, which restricts their effectiveness in comprehending 3D spaces. To address this issue, in this paper, we propose a novel generalist model, i.e., Video-3D LLM, for 3D scene understanding. By treating 3D scenes as dynamic videos and incorporating 3D position encoding into these representations, our Video-3D LLM aligns video representations with real-world spatial contexts more accurately. In addition, we have implemented a maximum coverage sampling technique to optimize the trade-off between computational cost and performance. Extensive experiments demonstrate that our model achieves state-of-the-art performance on several 3D scene understanding benchmarks, including ScanRefer, Multi3DRefer, Scan2Cap, ScanQA, and SQA3D.

</details>

### MMVU: Measuring Expert-Level Multi-Discipline Video Understanding.
- **链接**: [arXiv:2501.12380](https://arxiv.org/abs/2501.12380) · 📚 被引 8
- **作者**: Yilun Zhao, Haowei Zhang, Lujing Xie, Tongyan Hu, Guo Gan, Yitao Long et al.
- **🏷️ 机构**: Yale NLP MMVU Team
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce MMVU, a comprehensive expert-level, multi-discipline benchmark for evaluating foundation models in video understanding. MMVU includes 3,000 expert-annotated questions spanning 27 subjects across four core disciplines: Science, Healthcare, Humanities & Social Sciences, and Engineering. Compared to prior benchmarks, MMVU features three key advancements. First, it challenges models to apply domain-specific knowledge and perform expert-level reasoning to analyze specialized-domain videos, moving beyond the basic visual perception typically assessed in current video benchmarks. Second, each example is annotated by human experts from scratch. We implement strict data quality controls to ensure the high quality of the dataset. Finally, each example is enriched with expert-annotated reasoning rationals and relevant domain knowledge, facilitating in-depth analysis. We conduct an extensive evaluation of 32 frontier multimodal foundation models on MMVU. The latest System-2-capable models, o1 and Gemini 2.0 Flash Thinking, achieve the highest performance among the tested models. However, they still fall short of matching human expertise. Through in-depth error analyses and case studies, we offer actionable insights for future advancements in expert-level, knowledge-intensive video understanding for specialized domains.

</details>

### DynFocus: Dynamic Cooperative Network Empowers LLMs with Video Understanding.
- **链接**: [arXiv:2411.12355](https://arxiv.org/abs/2411.12355)
- **作者**: Yudong Han, Qingpei Guo, Liyuan Pan, Liu Liu, Yu Guan, Ming Yang
- **🏷️ 机构**: Beijing Institute of Technology, Ant Group, Huawei,KooMap Dept.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The challenge in LLM-based video understanding lies in preserving visual and semantic information in long videos while maintaining a memory-affordable token count. However, redundancy and correspondence in videos have hindered the performance potential of existing methods. Through statistical learning on current datasets, we observe that redundancy occurs in both repeated and answer-irrelevant frames, and the corresponding frames vary with different questions. This suggests the possibility of adopting dynamic encoding to balance detailed video information preservation with token budget reduction. To this end, we propose a dynamic cooperative network, DynFocus, for memory-efficient video encoding in this paper. Specifically, i) a Dynamic Event Prototype Estimation (DPE) module to dynamically select meaningful frames for question answering; (ii) a Compact Cooperative Encoding (CCE) module that encodes meaningful frames with detailed visual appearance and the remaining frames with sketchy perception separately. We evaluate our method on five publicly available benchmarks, and experimental results consistently demonstrate that our method achieves competitive performance.

</details>

### STOP: Integrated Spatial-Temporal Dynamic Prompting for Video Understanding.
- **链接**: [arXiv:2503.15973](https://arxiv.org/abs/2503.15973) · 📚 被引 6
- **作者**: Zichen Liu, Kunlun Xu, Bing Su, Xu Zou, Yuxin Peng, Jiahuan Zhou
- **🏷️ 机构**: Peking University,Wangxuan Institute of Computer Technology,Beijing,China, Renmin University of China,Gaoling School of Artificial Intelligence,Beijing,China, Huazhong University of Science and Technology,School of Artificial Intelligence and Automation,Wuhan,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained on tremendous image-text pairs, vision-language models like CLIP have demonstrated promising zero-shot generalization across numerous image-based tasks. However, extending these capabilities to video tasks remains challenging due to limited labeled video data and high training costs. Recent video prompting methods attempt to adapt CLIP for video tasks by introducing learnable prompts, but they typically rely on a single static prompt for all video sequences, overlooking the diverse temporal dynamics and spatial variations that exist across frames. This limitation significantly hinders the model's ability to capture essential temporal information for effective video understanding. To address this, we propose an integrated Spatial-TempOral dynamic Prompting (STOP) model which consists of two complementary modules, the intra-frame spatial prompting and inter-frame temporal prompting. Our intra-frame spatial prompts are designed to adaptively highlight discriminative regions within each frame by leveraging intra-frame attention and temporal variation, allowing the model to focus on areas with substantial temporal dynamics and capture fine-grained spatial details. Additionally, to highlight the varying importance of frames for video understanding, we further introduce inter-frame temporal prompts, dynamically inserting prompts between frames with high temporal variance as measured by frame similarity. This enables the model to prioritize key frames and enhances its capacity to understand temporal dependencies across sequences. Extensive experiments on various video benchmarks demonstrate that STOP consistently achieves superior performance against state-of-the-art methods. The code is available at https://github.com/zhoujiahuan1991/CVPR2025-STOP.

</details>

### DrVideo: Document Retrieval Based Long Video Understanding.
- **链接**: [arXiv:2406.12846](https://arxiv.org/abs/2406.12846) · 📚 被引 15
- **作者**: Ziyu Ma, Chenhui Gou, Hengcan Shi, Bin Sun, Shutao Li, Hamid Rezatofighi et al.
- **🏷️ 机构**: Hunan University,College of Electrical and Information Engineering, Monash University,Faculty of IT,Data Science &#x0026; AI Department
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most of the existing methods for video understanding primarily focus on videos only lasting tens of seconds, with limited exploration of techniques for handling long videos. The increased number of frames in long videos poses two main challenges: difficulty in locating key information and performing long-range reasoning. Thus, we propose DrVideo, a document-retrieval-based system designed for long video understanding. Our key idea is to convert the long-video understanding problem into a long-document understanding task so as to effectively leverage the power of large language models. Specifically, DrVideo first transforms a long video into a coarse text-based long document to initially retrieve key frames and then updates the documents with the augmented key frame information. It then employs an agent-based iterative loop to continuously search for missing information and augment the document until sufficient question-related information is gathered for making the final predictions in a chain-of-thought manner. Extensive experiments on long video benchmarks confirm the effectiveness of our method. DrVideo significantly outperforms existing LLM-based state-of-the-art methods on EgoSchema benchmark (3 minutes), MovieChat-1K benchmark (10 minutes), and the long split of Video-MME benchmark (average of 44 minutes).

</details>

### Omnia de EgoTempo: Benchmarking Temporal Understanding of Multi-Modal LLMs in Egocentric Videos.
- **链接**: [arXiv:2503.13646](https://arxiv.org/abs/2503.13646) · 📚 被引 6
- **作者**: Chiara Plizzari, Alessio Tonioni, Yongqin Xian, Achin Kulshrestha, Federico Tombari
- **🏷️ 机构**: Google
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding fine-grained temporal dynamics is crucial in egocentric videos, where continuous streams capture frequent, close-up interactions with objects. In this work, we bring to light that current egocentric video question-answering datasets often include questions that can be answered using only few frames or commonsense reasoning, without being necessarily grounded in the actual video. Our analysis shows that state-of-the-art Multi-Modal Large Language Models (MLLMs) on these benchmarks achieve remarkably high performance using just text or a single frame as input. To address these limitations, we introduce EgoTempo, a dataset specifically designed to evaluate temporal understanding in the egocentric domain. EgoTempo emphasizes tasks that require integrating information across the entire video, ensuring that models would need to rely on temporal patterns rather than static cues or pre-existing knowledge. Extensive experiments on EgoTempo show that current MLLMs still fall short in temporal reasoning on egocentric videos, and thus we hope EgoTempo will catalyze new research in the field and inspire models that better capture the complexity of temporal dynamics. Dataset and code are available at https://github.com/google-research-datasets/egotempo.git.

</details>

### Towards Universal Soccer Video Understanding.
- **链接**: [arXiv:2412.01820](https://arxiv.org/abs/2412.01820) · 📚 被引 18
- **作者**: Jiayuan Rao, Haoning Wu, Hao Jiang, Ya Zhang, Yanfeng Wang, Weidi Xie
- **🏷️ 机构**: Shanghai Jiao Tong University,School of Artificial Intelligence,China, Alibaba Group,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a globally celebrated sport, soccer has attracted widespread interest from fans all over the world. This paper aims to develop a comprehensive multi-modal framework for soccer video understanding. Specifically, we make the following contributions in this paper: (i) we introduce SoccerReplay-1988, the largest multi-modal soccer dataset to date, featuring videos and detailed annotations from 1,988 complete matches, with an automated annotation pipeline; (ii) we present an advanced soccer-specific visual encoder, MatchVision, which leverages spatiotemporal information across soccer videos and excels in various downstream tasks; (iii) we conduct extensive experiments and ablation studies on event classification, commentary generation, and multi-view foul recognition. MatchVision demonstrates state-of-the-art performance on all of them, substantially outperforming existing models, which highlights the superiority of our proposed data and model. We believe that this work will offer a standard paradigm for sports understanding research.

</details>

### Temporal Alignment-Free Video Matching for Few-shot Action Recognition.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Temporal_Alignment-Free_Video_Matching_for_Few-shot_Action_Recognition_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: SuBeen Lee, WonJun Moon, Hyun Seok Seong, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: CVPR 2025

### MCAM: Multimodal Causal Analysis Model for Ego-Vehicle-Level Driving Video Understanding.
- **链接**: [arXiv:2507.06072](https://arxiv.org/abs/2507.06072)
- **作者**: Tongtong Cheng, Rongzhen Li, Yixin Xiong, Tao Zhang, Jing Wang, Kai Liu
- **🏷️ 机构**: Chongqing University,Department of Computer Science,China, National Elite Institute of Engineering, Chongqing University,China, College of Computer Science and Technology, National University of Deffense Technology,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate driving behavior recognition and reasoning are critical for autonomous driving video understanding. However, existing methods often tend to dig out the shallow causal, fail to address spurious correlations across modalities, and ignore the ego-vehicle level causality modeling. To overcome these limitations, we propose a novel Multimodal Causal Analysis Model (MCAM) that constructs latent causal structures between visual and language modalities. Firstly, we design a multi-level feature extractor to capture long-range dependencies. Secondly, we design a causal analysis module that dynamically models driving scenarios using a directed acyclic graph (DAG) of driving states. Thirdly, we utilize a vision-language transformer to align critical visual features with their corresponding linguistic expressions. Extensive experiments on the BDD-X, and CoVLA datasets demonstrate that MCAM achieves SOTA performance in visual-language causal relationship learning. Furthermore, the model exhibits superior capability in capturing causal characteristics within video sequences, showcasing its effectiveness for autonomous driving applications. The code is available at https://github.com/SixCorePeach/MCAM.

</details>

### Streaming Videollms for Real-Time Procedural Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02097) · 📚 被引 1
- **作者**: Dibyadip Chatterjee, Edoardo Remelli, Yale Song, Bugra Tekin, Abhay Mittal, Bharat Bhatnagar et al.
- **🏷️ 机构**: Meta Reality Labs, FAIR, Meta
- **会议**: ICCV 2025

### VideoLLaMB: Long Streaming Video Understanding with Recurrent Memory Bridges.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02240) · 📚 被引 4
- **作者**: Yuxuan Wang, Yiqi Song, Cihang Xie, Yang Liu, Zilong Zheng
- **🏷️ 机构**: State Key Laboratory of General Artificial Intelligence, BIGAI,NLCo Lab, University of California,Computer Science and Engineering, Wangxuan Institute of Computer Technology, Peking University
- **会议**: ICCV 2025

### Breaking the Encoder Barrier for Seamless Video-Language Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02151)
- **作者**: Handong Li, Yiyuan Zhang, Longteng Guo, Xiangyu Yue, Jing Liu
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences, CUHK,MMLab
- **会议**: ICCV 2025

### Flow4Agent: Long-form Video Understanding via Motion Prior from Optical Flow.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02211)
- **作者**: Ruyang Liu, Shangkun Sun, Haoran Tang, Wei Gao, Ge Li
- **🏷️ 机构**: School of Electronic and Computer Engineering, Shenzhen Graduate School, Peking University
- **会议**: ICCV 2025

### AdsQA: Towards Advertisement Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02172) · 📚 被引 2
- **作者**: Xinwei Long, Kai Tian, Peng Xu, Guoli Jia, Jingxuan Li, Sa Yang et al.
- **🏷️ 机构**: Tsinghua University, Independent Researcher, Peking University
- **会议**: ICCV 2025

### How Can Objects Help Video-Language Understanding?
- **链接**: [arXiv:2504.07454](https://arxiv.org/abs/2504.07454)
- **作者**: Zitian Tang, Shijie Wang, Junho Cho, Jaewook Yoo, Chen Sun
- **🏷️ 机构**: Brown University, Samsung Electronics
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Do we still need to represent objects explicitly in multimodal large language models (MLLMs)? To one extreme, pre-trained encoders convert images into visual tokens, with which objects and spatiotemporal relationships may be implicitly modeled. To the other extreme, image captions by themselves provide strong empirical performances for understanding tasks, despite missing fine-grained spatiotemporal information. To answer this question, we introduce ObjectMLLM, a framework capable of leveraging arbitrary computer vision algorithm to extract and integrate structured visual representation. Through extensive evaluations on six video question answering benchmarks, we confirm that explicit integration of object-centric representation remains necessary. Surprisingly, we observe that the simple approach of quantizing the continuous, structured object information and representing them as plain text performs the best, offering a data-efficient approach to integrate other visual perception modules into MLLM design. Our code and models are released at https://github.com/brown-palm/ObjectMLLM.

</details>

### Bringing RNNs Back to Efficient Open-Ended Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02177)
- **作者**: Weili Xu, Enxin Song, Wenhao Chai, Xuexiang Wen, Tian Ye, Gaoang Wang
- **🏷️ 机构**: Zhejiang University, University of Washington, HKUST (GZ)
- **会议**: ICCV 2025

### Beyond Training: Dynamic Token Merging for Zero-Shot Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02047) · 📚 被引 2
- **作者**: Yiming Zhang, Zhuokai Zhao, Zhaorun Chen, Zenghui Ding, Xianjun Yang, Yining Sun
- **🏷️ 机构**: HFIPS, Chinese Academy of Sciences, University of Chicago
- **会议**: ICCV 2025

### PvNeXt: Rethinking Network Design and Temporal Motion for Point Cloud Video Recognition.
- **链接**: [arXiv:2504.05075](https://arxiv.org/abs/2504.05075)
- **作者**: Jie Wang, Tingfa Xu, Lihe Ding, Xinjie Zhang, Long Bai, Jianan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks.
- **链接**: [arXiv:2410.19100](https://arxiv.org/abs/2410.19100)
- **作者**: Lawrence Keunho Jang, Yinheng Li, Dan Zhao, Charles Ding, Justin Lin, Paul Pu Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models.
- **链接**: [arXiv:2410.23266](https://arxiv.org/abs/2410.23266)
- **作者**: Ziyao Shangguan, Chuhan Li, Yuxuan Ding, Yanan Zheng, Yilun Zhao, Tesca Fitzgerald et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing benchmarks often highlight the remarkable performance achieved by state-of-the-art Multimodal Foundation Models (MFMs) in leveraging temporal context for video understanding. However, how well do the models truly perform visual temporal reasoning? Our study of existing benchmarks shows that this capability of MFMs is likely overestimated as many questions can be solved by using a single, few, or out-of-order frames. To systematically examine current visual temporal reasoning tasks, we propose three principles with corresponding metrics: (1) Multi-Frame Gain, (2) Frame Order Sensitivity, and (3) Frame Information Disparity. Following these principles, we introduce TOMATO, Temporal Reasoning Multimodal Evaluation, a novel benchmark crafted to rigorously assess MFMs' temporal reasoning capabilities in video understanding. TOMATO comprises 1,484 carefully curated, human-annotated questions spanning six tasks (i.e., action count, direction, rotation, shape & trend, velocity & frequency, and visual cues), applied to 1,417 videos, including 805 self-recorded and -generated videos, that encompass human-centric, real-world, and simulated scenarios. Our comprehensive evaluation reveals a human-model performance gap of 57.3% with the best-performing model. Moreover, our in-depth analysis uncovers more fundamental limitations beyond this gap in current MFMs. While they can accurately recognize events in isolated frames, they fail to interpret these frames as a continuous sequence. We believe TOMATO will serve as a crucial testbed for evaluating the next-generation MFMs and as a call to the community to develop AI systems capable of comprehending human world dynamics through the video modality.

</details>

### CREMA: Generalizable and Efficient Video-Language Reasoning via Multimodal Modular Fusion.
- **链接**: [出版页](https://openreview.net/forum?id=3UaOlzDEt2)
- **作者**: Shoubin Yu, Jaehong Yoon, Mohit Bansal
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning.
- **链接**: [arXiv:2409.20566](https://arxiv.org/abs/2409.20566)
- **作者**: Haotian Zhang, Mingfei Gao, Zhe Gan, Philipp Dufter, Nina Wenzel, Forrest Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present MM1.5, a new family of multimodal large language models (MLLMs) designed to enhance capabilities in text-rich image understanding, visual referring and grounding, and multi-image reasoning. Building upon the MM1 architecture, MM1.5 adopts a data-centric approach to model training, systematically exploring the impact of diverse data mixtures across the entire model training lifecycle. This includes high-quality OCR data and synthetic captions for continual pre-training, as well as an optimized visual instruction-tuning data mixture for supervised fine-tuning. Our models range from 1B to 30B parameters, encompassing both dense and mixture-of-experts (MoE) variants, and demonstrate that careful data curation and training strategies can yield strong performance even at small scales (1B and 3B). Additionally, we introduce two specialized variants: MM1.5-Video, designed for video understanding, and MM1.5-UI, tailored for mobile UI understanding. Through extensive empirical studies and ablations, we provide detailed insights into the training processes and decisions that inform our final designs, offering valuable guidance for future research in MLLM development.

</details>

### Contextual Self-paced Learning for Weakly Supervised Spatio-Temporal Video Grounding.
- **链接**: [arXiv:2501.17053](https://arxiv.org/abs/2501.17053)
- **作者**: Akash Kumar, Zsolt Kira, Yogesh S. Rawat
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Compositional 4D Dynamic Scenes Understanding with Physics Priors for Video Question Answering.
- **链接**: [arXiv:2406.00622](https://arxiv.org/abs/2406.00622)
- **作者**: Xingrui Wang, Wufei Ma, Angtian Wang, Shuo Chen, Adam Kortylewski, Alan L. Yuille
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge.
- **链接**: [arXiv:2501.13468](https://arxiv.org/abs/2501.13468)
- **作者**: Haomiao Xiong, Zongxin Yang, Jiazuo Yu, Yunzhi Zhuge, Lu Zhang, Jiawen Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning.
- **链接**: [arXiv:2410.19702](https://arxiv.org/abs/2410.19702)
- **作者**: Xiangyu Zeng, Kunchang Li, Chenting Wang, Xinhao Li, Tianxiang Jiang, Ziang Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering.
- **链接**: [出版页](https://proceedings.mlr.press/v267/song25g.html)
- **作者**: Zihan Song, Xin Wang, Zi Qian, Hong Chen, Longtao Huang, Hui Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/cheng25b.html)
- **作者**: Chuanqi Cheng, Jian Guan, Wei Wu, Rui Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Genesis: Multimodal Driving Scene Generation with Spatio-Temporal and Cross-Modal Consistency.
- **链接**: [arXiv:2506.07497](https://arxiv.org/abs/2506.07497)
- **作者**: Xiangyu Guo, Zhanqian Wu, Kaixin Xiong, Ziyang Xu, Lijun Zhou, Gangwei Xu et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, University of Pennsylvania, Xiaomi Corporation
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Genesis, a unified framework for joint generation of multi-view driving videos and LiDAR sequences with spatio-temporal and cross-modal consistency. Genesis employs a two-stage architecture that integrates a DiT-based video diffusion model with 3D-VAE encoding, and a BEV-aware LiDAR generator with NeRF-based rendering and adaptive sampling. Both modalities are directly coupled through a shared latent space, enabling coherent evolution across visual and geometric domains. To guide the generation with structured semantics, we introduce DataCrafter, a captioning module built on vision-language models that provides scene-level and instance-level supervision. Extensive experiments on the nuScenes benchmark demonstrate that Genesis achieves state-of-the-art performance across video and LiDAR metrics (FVD 16.95, FID 4.24, Chamfer 0.611), and benefits downstream tasks including segmentation and 3D detection, validating the semantic fidelity and practical utility of the generated data.

</details>

### Eagle 2.5: Boosting Long-Context Post-Training for Frontier Vision-Language Models.
- **链接**: [arXiv:2504.15271](https://arxiv.org/abs/2504.15271) · 📚 被引 1
- **作者**: Guo Chen, Zhiqi Li, Shihao Wang, Jindong Jiang, Yicheng Liu, Lidong Lu et al.
- **🏷️ 机构**: Nanjing University, NVIDIA, Hong Kong Polytechnic University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce Eagle 2.5, a family of frontier vision-language models (VLMs) for long-context multimodal learning. Our work addresses the challenges in long video comprehension and high-resolution image understanding, introducing a generalist framework for both tasks. The proposed training framework incorporates Automatic Degrade Sampling and Image Area Preservation, two techniques that preserve contextual integrity and visual details. The framework also includes numerous efficiency optimizations in the pipeline for long-context data training. Finally, we propose Eagle-Video-110K, a novel dataset that integrates both story-level and clip-level annotations, facilitating long-video understanding. Eagle 2.5 demonstrates substantial improvements on long-context multimodal benchmarks, providing a robust solution to the limitations of existing VLMs. Notably, our best model Eagle 2.5-8B achieves 72.4% on Video-MME with 512 input frames, matching the results of top-tier commercial model such as GPT-4o and large-scale open-source models like Qwen2.5-VL-72B and InternVL2.5-78B.

</details>

### ROVER: Recursive Reasoning Over Videos with Vision-Language Models for Embodied Tasks.
- **链接**: [arXiv:2508.01943](https://arxiv.org/abs/2508.01943)
- **作者**: Philip Schroeder, Ondrej Biza, Thomas Weng, Hongyin Luo, Jim Glass
- **🏷️ 机构**: Massachusetts Institute of Technology, Robotics and AI Institute
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models (VLMs) have exhibited impressive capabilities across diverse image understanding tasks, but still struggle in settings that require reasoning over extended sequences of camera frames from a video. This limits their utility in embodied settings, which require reasoning over long frame sequences from a continuous stream of visual input at each moment of a task attempt. To address this limitation, we propose ROVER (Reasoning Over VidEo Recursively), a framework that enables the model to recursively decompose long-horizon video trajectories into segments corresponding to shorter subtasks within the trajectory. In doing so, ROVER facilitates more focused and accurate reasoning over temporally localized frame sequences without losing global context. We evaluate ROVER, implemented using an in-context learning approach, on diverse OpenX Embodiment videos and on a new dataset derived from RoboCasa that consists of 543 videos showing both expert and perturbed non-expert trajectories across 27 robotic manipulation tasks. ROVER outperforms strong baselines across three video reasoning tasks: task progress estimation, frame-level natural language reasoning, and video question answering. We observe that, by reducing the number of frames the model reasons over at each timestep, ROVER mitigates hallucinations, especially during unexpected or non-optimal moments of a trajectory. In addition, by enabling the implementation of a subtask-specific sliding context window, ROVER's time complexity scales linearly with video length, an asymptotic improvement over baselines. Demos, code, and data available at: https://rover-vlm.github.io

</details>

### Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation.
- **链接**: [arXiv:2505.11383](https://arxiv.org/abs/2505.11383) · 📚 被引 2
- **作者**: Zihan Wang, Seungjun Lee, Gim Hee Lee
- **🏷️ 机构**: National University of Singapore, national university of singaore, National University of Singapore
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-Language Navigation (VLN) is a core task where embodied agents leverage their spatial mobility to navigate in 3D environments toward designated destinations based on natural language instructions. Recently, video-language large models (Video-VLMs) with strong generalization capabilities and rich commonsense knowledge have shown remarkable performance when applied to VLN tasks. However, these models still encounter the following challenges when applied to real-world 3D navigation: 1) Insufficient understanding of 3D geometry and spatial semantics; 2) Limited capacity for large-scale exploration and long-term environmental memory; 3) Poor adaptability to dynamic and changing environments.To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in navigation action prediction. Given posed RGB-D images, our Dynam3D projects 2D CLIP features into 3D space and constructs multi-level 3D patch-instance-zone representations for 3D geometric and semantic understanding with a dynamic and layer-wise update strategy. Our Dynam3D is capable of online encoding and localization of 3D instances, and dynamically updates them in changing environments to provide large-scale exploration and long-term memory capabilities for navigation. By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings. Furthermore, experiments for pre-exploration, lifelong memory, and real-world robot validate the effectiveness of practical deployment.

</details>

### MRSAudio: A Large-Scale Multimodal Recorded Spatial Audio Dataset with Refined Annotations.
- **链接**: [arXiv:2510.10396](https://arxiv.org/abs/2510.10396)
- **作者**: Wenxiang Guo, Changhao Pan, Zhiyuan Zhu, Xintong Hu, Yu Zhang, Li Tang et al.
- **🏷️ 机构**: Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Humans rely on multisensory integration to perceive spatial environments, where auditory cues enable sound source localization in three-dimensional space. Despite the critical role of spatial audio in immersive technologies such as VR/AR, most existing multimodal datasets provide only monaural audio, which limits the development of spatial audio generation and understanding. To address these challenges, we introduce MRSAudio, a large-scale multimodal spatial audio dataset designed to advance research in spatial audio understanding and generation. MRSAudio spans four distinct components: MRSLife, MRSSpeech, MRSMusic, and MRSSing, covering diverse real-world scenarios. The dataset includes synchronized binaural and ambisonic audio, exocentric and egocentric video, motion trajectories, and fine-grained annotations such as transcripts, phoneme boundaries, lyrics, scores, and prompts. To demonstrate the utility and versatility of MRSAudio, we establish five foundational tasks: audio spatialization, and spatial text to speech, spatial singing voice synthesis, spatial music generation and sound event localization and detection. Results show that MRSAudio enables high-quality spatial modeling and supports a broad range of spatial audio research. Demos and dataset access are available at https://mrsaudio.github.io.

</details>

### MVU-Eval: Towards Multi-Video Understanding Evaluation for Multimodal LLMs.
- **链接**: [arXiv:2511.07250](https://arxiv.org/abs/2511.07250)
- **作者**: Tianhao Peng, Haochen Wang, Yuanxing Zhang, Noah Wang, Zili Wang, Ge Zhang et al.
- **🏷️ 机构**: Beijing University of Aeronautics and Astronautics, Institute of automation, Chinese Academy of Sciences; University of Chinese Academy of Sciences, Kuaishou- 快手科技
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of Multimodal Large Language Models (MLLMs) has expanded AI capabilities to visual modalities, yet existing evaluation benchmarks remain limited to single-video understanding, overlooking the critical need for multi-video understanding in real-world scenarios (e.g., sports analytics and autonomous driving). To address this significant gap, we introduce MVU-Eval, the first comprehensive benchmark for evaluating Multi-Video Understanding for MLLMs. Specifically, our MVU-Eval mainly assesses eight core competencies through 1,824 meticulously curated question-answer pairs spanning 4,959 videos from diverse domains, addressing both fundamental perception tasks and high-order reasoning tasks. These capabilities are rigorously aligned with real-world applications such as multi-sensor synthesis in autonomous systems and cross-angle sports analytics. Through extensive evaluation of state-of-the-art open-source and closed-source models, we reveal significant performance discrepancies and limitations in current MLLMs' ability to perform understanding across multiple videos. The benchmark will be made publicly available to foster future research.

</details>

### MME-VideoOCR: Evaluating OCR-Based Capabilities of Multimodal LLMs in Video Scenarios.
- **链接**: [arXiv:2505.21333](https://arxiv.org/abs/2505.21333)
- **作者**: Yang Shi, Huanqian Wang, Wulin Xie, Huanyao Zhang, Lijie Zhao, Yifan Zhang et al.
- **🏷️ 机构**: Peking University, Tsinghua University, Tsinghua University, The Chinese University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) have achieved considerable accuracy in Optical Character Recognition (OCR) from static images. However, their efficacy in video OCR is significantly diminished due to factors such as motion blur, temporal variations, and visual effects inherent in video content. To provide clearer guidance for training practical MLLMs, we introduce the MME-VideoOCR benchmark, which encompasses a comprehensive range of video OCR application scenarios. MME-VideoOCR features 10 task categories comprising 25 individual tasks and spans 44 diverse scenarios. These tasks extend beyond text recognition to incorporate deeper comprehension and reasoning of textual content within videos. The benchmark consists of 1,464 videos with varying resolutions, aspect ratios, and durations, along with 2,000 meticulously curated, manually annotated question-answer pairs. We evaluate 18 state-of-the-art MLLMs on MME-VideoOCR, revealing that even the best-performing model (Gemini-2.5 Pro) achieves an accuracy of only 73.7%. Fine-grained analysis indicates that while existing MLLMs demonstrate strong performance on tasks where relevant texts are contained within a single or few frames, they exhibit limited capability in effectively handling tasks that demand holistic video comprehension. These limitations are especially evident in scenarios that require spatio-temporal reasoning, cross-frame information integration, or resistance to language prior bias. Our findings also highlight the importance of high-resolution visual input and sufficient temporal coverage for reliable OCR in dynamic video scenarios.

</details>

### Seeing the Arrow of Time in Large Multimodal Models.
- **链接**: [arXiv:2506.03340](https://arxiv.org/abs/2506.03340)
- **作者**: Zihui Xue, Romy Luo, Kristen Grauman
- **🏷️ 机构**: University of Texas, Austin, UT Austin, University of Texas at Austin
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Arrow of Time (AoT)-time's irreversible flow shaping physical events-is fundamental to video comprehension, yet remains a significant challenge for modern large multimodal models (LMMs). Current LMMs struggle to perceive and utilize temporal directionality in video when responding to language queries, obstructing deeper temporal understanding. We tackle this deficiency by first providing a critical analysis of existing benchmarks and models. We then introduce ArrowRL, a reinforcement learning (RL)-based training strategy with an innovative reverse reward that instills AoT awareness by encouraging divergent video interpretations between forward and reversed visual frames. For rigorous evaluation, we additionally develop AoTBench, a new multi-faceted benchmark probing temporally challenging questions. Experiments show ArrowRL greatly advances temporal perception: it not only achieves substantial improvements on our challenging AoTBench but also demonstrably boosts performance on standard video question answering (VQA) benchmarks (with peak accuracy gains reaching over 20% and 10% respectively). This validates ArrowRL's effectiveness and highlights the critical need for dedicated AoT understanding in LMMs.

</details>

### VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception.
- **链接**: [arXiv:2509.21100](https://arxiv.org/abs/2509.21100)
- **作者**: Ziang Yan, Yinan He, Xinhao Li, Zhengrong Yue, Xiangyu Zeng, Yali Wang et al.
- **🏷️ 机构**: Zhejiang University, Shanghai AI Lab, Nanjing University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Inducing reasoning in multimodal large language models (MLLMs) is critical for achieving human-level perception and understanding. Existing methods mainly leverage LLM reasoning to analyze parsed visuals, often limited by static perception stages. This paper introduces Visual Test-Time Scaling (VTTS), a novel approach to enhance MLLMs' reasoning via iterative perception during inference. VTTS mimics humans' hierarchical attention by progressively refining focus on high-confidence spatio-temporal regions, guided by updated textual predictions. Specifically, VTTS employs an Iterative Perception (ITP) mechanism, incorporating reinforcement learning with spatio-temporal supervision to optimize reasoning. To support this paradigm, we also present VTTS-80K, a dataset tailored for iterative perception. These designs allows a MLLM to enhance its performance by increasing its perceptual compute. Extensive experiments validate VTTS's effectiveness and generalization across diverse tasks and benchmarks. Our newly introduced Videochat-R1.5 model has achieved remarkable improvements, with an average increase of over 5\%, compared to robust baselines such as Qwen2.5VL-3B and -7B, across more than 15 benchmarks that encompass video conversation, video reasoning, and spatio-temporal perception.

</details>

### Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding.
- **链接**: [arXiv:2509.15178](https://arxiv.org/abs/2509.15178)
- **作者**: Zaiquan Yang, Yuhao Liu, Gerhard P. Hancke, Rynson W. H. Lau
- **🏷️ 机构**: City University of Hong Kong
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Spatio-temporal video grounding (STVG) aims at localizing the spatio-temporal tube of a video, as specified by the input text query. In this paper, we utilize multimodal large language models (MLLMs) to explore a zero-shot solution in STVG. We reveal two key insights about MLLMs: (1) MLLMs tend to dynamically assign special tokens, referred to as \textit{grounding tokens}, for grounding the text query; and (2) MLLMs often suffer from suboptimal grounding due to the inability to fully integrate the cues in the text query (\textit{e.g.}, attributes, actions) for inference. Based on these insights, we propose a MLLM-based zero-shot framework for STVG, which includes novel decomposed spatio-temporal highlighting (DSTH) and temporal-augmented assembling (TAS) strategies to unleash the reasoning ability of MLLMs. The DSTH strategy first decouples the original query into attribute and action sub-queries for inquiring the existence of the target both spatially and temporally. It then uses a novel logit-guided re-attention (LRA) module to learn latent variables as spatial and temporal prompts, by regularizing token predictions for each sub-query. These prompts highlight attribute and action cues, respectively, directing the model's attention to reliable spatial and temporal related visual regions. In addition, as the spatial grounding by the attribute sub-query should be temporally consistent, we introduce the TAS strategy to assemble the predictions using the original video frames and the temporal-augmented frames as inputs to help improve temporal consistency. We evaluate our method on various MLLMs, and show that it outperforms SOTA methods on three common STVG benchmarks. The code will be available at https://github.com/zaiquanyang/LLaVA_Next_STVG.

</details>

### Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation.
- **链接**: [arXiv:2506.11777](https://arxiv.org/abs/2506.11777)
- **作者**: Divyanshu Mishra, Mohammadreza Salehi, Pramit Saha, Olga Patey, Aris T. Papageorghiou, Yuki Asano et al.
- **🏷️ 机构**: University of Oxford, University of Amsterdam, University of Technology Nuremberg
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning (SSL) has achieved major advances in natural images and video understanding, but challenges remain in domains like echocardiography (heart ultrasound) due to subtle anatomical structures, complex temporal dynamics, and the current lack of domain-specific pre-trained models. Existing SSL approaches such as contrastive, masked modeling, and clustering-based methods struggle with high intersample similarity, sensitivity to low PSNR inputs common in ultrasound, or aggressive augmentations that distort clinically relevant features. We present DISCOVR (Distilled Image Supervision for Cross Modal Video Representation), a self-supervised dual branch framework for cardiac ultrasound video representation learning. DISCOVR combines a clustering-based video encoder that models temporal dynamics with an online image encoder that extracts fine-grained spatial semantics. These branches are connected through a semantic cluster distillation loss that transfers anatomical knowledge from the evolving image encoder to the video encoder, enabling temporally coherent representations enriched with fine-grained semantic understanding.Evaluated on six echocardiography datasets spanning fetal, pediatric, and adult populations, DISCOVR outperforms both specialized video anomaly detection methods and state-of-the-art video-SSL baselines in zero-shot and linear probing setups,achieving superior segmentation transfer and strong downstream performance on clinically relevant tasks such as LVEF prediction. Code available at: https://github.com/mdivyanshu97/DISCOVR

</details>

### VideoHallu: Evaluating and Mitigating Multi-modal Hallucinations on Synthetic Video Understanding.
- **链接**: [arXiv:2505.01481](https://arxiv.org/abs/2505.01481)
- **作者**: Zongxia Li, Xiyang Wu, Guangyao Shi, Yubin Qin, Hongyang Du, Tianyi Zhou et al.
- **🏷️ 机构**: University of Maryland, College Park, University of Maryland, University of Southern California
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Models (VLMs) have achieved strong results in video understanding, yet a key question remains: do they truly comprehend visual content or only learn shallow correlations between vision and language? Real visual understanding, especially of physics and common sense, is essential for AI systems that interact with the physical world. Current evaluations mostly use real-world videos similar to training data, so high benchmark scores may not reflect real reasoning ability. To address this, we propose negative-control tests using videos that depict physically impossible or logically inconsistent events. We introduce VideoHallu, a synthetic dataset of physics- and commonsense-violating scenes generated with Veo2, Sora, and Kling. It includes expert-annotated question-answer pairs across four categories of violations. Tests of leading VLMs (Qwen-2.5-VL, Video-R1, VideoChat-R1) show that, despite strong results on benchmarks such as MVBench and MMVU, they often miss these violations, exposing gaps in visual reasoning. Reinforcement learning fine-tuning on VideoHallu improves recognition of such violations without reducing standard benchmark performance. Our data is available at https://github.com/zli12321/VideoHallu.git.

</details>

### Unleashing Hour-Scale Video Training for Long Video-Language Understanding.
- **链接**: [arXiv:2506.05332](https://arxiv.org/abs/2506.05332) · 📚 被引 1
- **作者**: Jingyang Lin, Jialian Wu, Ximeng Sun, Ze Wang, Jiang Liu, Yusheng Su et al.
- **🏷️ 机构**: University of Rochester, AMD, Boston University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent long-form video-language understanding benchmarks have driven progress in video large multimodal models (Video-LMMs). However, the scarcity of well-annotated long videos has left the training of hour-long Video-LMMs underexplored. To close this gap, we present VideoMarathon, a large-scale hour-long video instruction-following dataset. This dataset includes around 9,700 hours of long videos sourced from diverse domains, ranging from 3 to 60 minutes per video. Specifically, it contains 3.3M high-quality QA pairs, spanning six fundamental topics: temporality, spatiality, object, action, scene, and event. Compared to existing video instruction datasets, VideoMarathon significantly extends training video durations up to 1 hour, and supports 22 diverse tasks requiring both short- and long-term video comprehension. Building on VideoMarathon, we propose Hour-LLaVA, a powerful and efficient Video-LMM for hour-scale video-language modeling. It enables hour-long video training and inference at 1-FPS sampling by leveraging a memory augmentation module, which adaptively integrates question-relevant and spatiotemporally informative semantics from the cached full video context. In our experiments, Hour-LLaVA achieves the best performance on multiple representative long video-language benchmarks, demonstrating the high quality of the VideoMarathon dataset and the superiority of the Hour-LLaVA model.

</details>

### MR. Video: MapReduce as an Effective Principle for Long Video Understanding.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/0a02c2bc2e2148b803c4ade1d71e1d25-Abstract-Conference.html)
- **作者**: Ziqi Pang, Yu-Xiong Wang
- **🏷️ 机构**: UIUC, University of Illinois Urbana-Champaign
- **会议**: NeurIPS 2025

### Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding.
- **链接**: [arXiv:2505.18079](https://arxiv.org/abs/2505.18079)
- **作者**: Xiaoyi Zhang, Zhaoyang Jia, Zongyu Guo, Jiahao Li, Bin Li, Houqiang Li et al.
- **🏷️ 机构**: Microsoft, University of Science and Technology of China, Microsoft Research
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-form video understanding presents significant challenges due to extensive temporal-spatial complexity and the difficulty of question answering under such extended contexts. While Large Language Models (LLMs) have demonstrated considerable advancements in video analysis capabilities and long context handling, they continue to exhibit limitations when processing information-dense hour-long videos. To overcome such limitations, we propose the Deep Video Discovery (DVD) agent to leverage an agentic search strategy over segmented video clips. Unlike previous video agents that rely on predefined workflows applied uniformly across different queries, our approach emphasizes the autonomous and adaptive nature of agents. By providing a set of search-centric tools on multi-granular video database, our DVD agent leverages the advanced reasoning capability of LLM to plan on its current observation state, strategically selects tools to orchestrate adaptive workflow for different queries in light of the gathered information. We perform comprehensive evaluation on multiple long video understanding benchmarks that demonstrates our advantage. Our DVD agent achieves state-of-the-art performance on the challenging LVBench dataset, reaching an accuracy of 74.2%, which substantially surpasses all prior works, and further improves to 76.0% with transcripts. The code has been released at https://github.com/microsoft/DeepVideoDiscovery.

</details>

### VideoLucy: Deep Memory Backtracking for Long Video Understanding.
- **链接**: [arXiv:2510.12422](https://arxiv.org/abs/2510.12422)
- **作者**: Jialong Zuo, Yongtai Deng, Lingdong Kong, Jingkang Yang, Rui Jin, Yiwei Zhang et al.
- **🏷️ 机构**: Huazhong University of Science and Technology, National University of Singapore, MMLab@NTU
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent studies have shown that agent-based systems leveraging large language models (LLMs) for key information retrieval and integration have emerged as a promising approach for long video understanding. However, these systems face two major challenges. First, they typically perform modeling and reasoning on individual frames, struggling to capture the temporal context of consecutive frames. Second, to reduce the cost of dense frame-level captioning, they adopt sparse frame sampling, which risks discarding crucial information. To overcome these limitations, we propose VideoLucy, a deep memory backtracking framework for long video understanding. Inspired by the human recollection process from coarse to fine, VideoLucy employs a hierarchical memory structure with progressive granularity. This structure explicitly defines the detail level and temporal scope of memory at different hierarchical depths. Through an agent-based iterative backtracking mechanism, VideoLucy systematically mines video-wide, question-relevant deep memories until sufficient information is gathered to provide a confident answer. This design enables effective temporal understanding of consecutive frames while preserving critical details. In addition, we introduce EgoMem, a new benchmark for long video understanding. EgoMem is designed to comprehensively evaluate a model's ability to understand complex events that unfold over time and capture fine-grained details in extremely long videos. Extensive experiments demonstrate the superiority of VideoLucy. Built on open-source models, VideoLucy significantly outperforms state-of-the-art methods on multiple long video understanding benchmarks, achieving performance even surpassing the latest proprietary models such as GPT-4o. Our code and dataset will be made publicly at https://videolucy.github.io

</details>

### InfiniPot-V: Memory-Constrained KV Cache Compression for Streaming Video Understanding.
- **链接**: [arXiv:2506.15745](https://arxiv.org/abs/2506.15745)
- **作者**: Minsoo Kim, Kyuhong Shim, Jungwook Choi, Simyung Chang
- **🏷️ 机构**: Hanyang University, Sungkyunkwan University, H1R AI
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern multimodal large language models (MLLMs) can reason over hour-long video, yet their key-value (KV) cache grows linearly with time-quickly exceeding the fixed memory of phones, AR glasses, and edge robots. Prior compression schemes either assume the whole video and user query are available offline or must first build the full cache, so memory still scales with stream length. InfiniPot-V is the first training-free, query-agnostic framework that enforces a hard, length-independent memory cap for streaming video understanding. During video encoding it monitors the cache and, once a user-set threshold is reached, runs a lightweight compression pass that (i) removes temporally redundant tokens via Temporal-axis Redundancy (TaR) metric and (ii) keeps semantically significant tokens via Value-Norm (VaN) ranking. Across four open-source MLLMs and four long-video and streaming-video benchmarks, InfiniPot-V cuts peak GPU memory by up to 94%, sustains real-time generation, and matches or surpasses full-cache accuracy-even in multi-turn dialogues. By dissolving the KV cache bottleneck without retraining or query knowledge, InfiniPot-V closes the gap for on-device streaming video assistants.

</details>

### Vgent: Graph-based Retrieval-Reasoning-Augmented Generation For Long Video Understanding.
- **链接**: [arXiv:2510.14032](https://arxiv.org/abs/2510.14032)
- **作者**: Xiaoqian Shen, Wenxuan Zhang, Jun Chen, Mohamed Elhoseiny
- **🏷️ 机构**: KAUST, DAMO Academy, Alibaba Group, Facebook
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding and reasoning over long videos pose significant challenges for large video language models (LVLMs) due to the difficulty in processing intensive video tokens beyond context window and retaining long-term sequential information. Retrieval-Augmented Generation (RAG) has demonstrated effectiveness in processing long context for Large Language Models (LLMs); however, applying RAG to long video faces challenges such as disrupted temporal dependencies and inclusion of irrelevant information that can hinder accurate reasoning. To address these limitations, we propose Vgent, a novel graph-based retrieval-reasoning-augmented generation framework to enhance LVLMs for long video understanding. Our approach introduces two key innovations: (i) It represents videos by structured graphs with semantic relationships across video clips preserved to improve retrieval effectiveness. (ii) It introduces an intermediate reasoning step to mitigate the reasoning limitation of LVLMs, which leverages structured verification to reduce retrieval noise and facilitate the explicit aggregation of relevant information across clips, resulting in more accurate and context-aware responses. We comprehensively evaluate our framework with various open-source LVLMs on three long-video understanding benchmarks. Our approach yielded an overall performance improvement of $3.0\%\sim 5.4\%$ over base models on MLVU, and outperformed state-of-the-art video RAG methods by $8.6\%$. Our code is publicly available at https://xiaoqian-shen.github.io/Vgent.

</details>

### One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding.
- **链接**: [arXiv:2604.14149](https://arxiv.org/abs/2604.14149)
- **作者**: Zheyu Zhang, Ziqi Pang, Shixing Chen, Xiang Hao, Vimal Bhat, Yu-Xiong Wang
- **🏷️ 机构**: University of Illinois at Urbana-Champaign, UIUC, Amazon
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long video understanding is inherently challenging for vision-language models (VLMs) because of the extensive number of frames. With each video frame typically expanding into tens or hundreds of tokens, the limited context length of large language models (LLMs) forces the VLMs to perceive the frames sparsely and lose temporal information. To address this, we explore extreme video token compression towards one token per frame at the final LLM layer. Our key insight is that heuristic-based compression, widely adopted by previous methods, is prone to information loss, and this necessitates supervising LLM layers into learnable and progressive modules for token-level compression (LP-Comp). Such compression enables our VLM to digest 2x-4x more frames with improved performance. To further increase the token efficiency, we investigate frame-level compression, which selects the frames most relevant to the queries via the internal attention scores of the LLM layers, named question-conditioned compression (QC-Comp). As a notable distinction from previous studies, we mitigate the position bias of LLM attention in long contexts, i.e., the over-concentration on the beginning and end of a sequence, by splitting long videos into short segments and employing local attention. Collectively, our combined token-level and frame-level leads to an extreme compression model for long video understanding, named XComp, achieving a significantly larger compression ratio and enabling denser frame sampling. Our XComp is finetuned from VideoChat-Flash with a data-efficient supervised compression tuning stage that only requires 2.5% of the supervised fine-tuning data, yet boosts the accuracy from 42.9% to 46.2% on LVBench and enhances multiple other long video benchmarks.

</details>

### FastVID: Dynamic Density Pruning for Fast Video Large Language Models.
- **链接**: [arXiv:2503.11187](https://arxiv.org/abs/2503.11187)
- **作者**: Leqi Shen, Guoqiang Gong, Tao He, Yifeng Zhang, Pengzhang Liu, Sicheng Zhao et al.
- **🏷️ 机构**: Tsinghua University, JD.com, Sichuan University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video Large Language Models have demonstrated strong video understanding capabilities, yet their practical deployment is hindered by substantial inference costs caused by redundant video tokens. Existing pruning techniques fail to effectively exploit the spatiotemporal redundancy present in video data. To bridge this gap, we perform a systematic analysis of video redundancy from two perspectives: temporal context and visual context. Leveraging these insights, we propose Dynamic Density Pruning for Fast Video LLMs termed FastVID. Specifically, FastVID dynamically partitions videos into temporally ordered segments to preserve temporal structure and applies a density-based token pruning strategy to maintain essential spatial and temporal information. Our method significantly reduces computational overhead while maintaining temporal and visual integrity. Extensive evaluations show that FastVID achieves state-of-the-art performance across various short- and long-video benchmarks on leading Video LLMs, including LLaVA-OneVision, LLaVA-Video, Qwen2-VL, and Qwen2.5-VL. Notably, on LLaVA-OneVision-7B, FastVID effectively prunes $\textbf{90.3%}$ of video tokens, reduces FLOPs to $\textbf{8.3%}$, and accelerates the LLM prefill stage by $\textbf{7.1}\times$, while maintaining $\textbf{98.0%}$ of the original accuracy. The code is available at https://github.com/LunarShen/FastVID.

</details>

## 跨领域论文（完整笔记在其他领域）

- MammAlps: A Multi-view Video Behavior Monitoring Dataset of Wild Mammals in the Swiss Alps. → [multi-camera-perception](../multi-camera-perception/Guideline%202025.md)
- Anomize: Better Open Vocabulary Video Anomaly Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- VisionZip: Longer is Better but Not Necessary in Vision Language Models. → [vlm](../vlm/Guideline%202025.md)
- BOLT: Boost Large Vision-Language Model Without Training for Long-form Video Understanding. → [vlm](../vlm/Guideline%202025.md)
- MotionBench: Benchmarking and Improving Fine-grained Video Motion Understanding for Vision Language Models. → [vlm](../vlm/Guideline%202025.md)
- PVC: Progressive Visual Token Compression for Unified Image and Video Processing in Large Vision-Language Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models. → [network-pruning](../network-pruning/Guideline%202025.md)
- CASP: Compression of Large Multimodal Models Based on Attention Sparsity. → [network-pruning](../network-pruning/Guideline%202025.md)
- SF2T: Self-supervised Fragment Finetuning of Video-LLMs for Fine-Grained Understanding. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- When the Future Becomes the Past: Taming Temporal Correspondence for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- SpatialDreamer: Self-supervised Stereo Video Synthesis from Monocular Input. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Self-supervised ControlNet with Spatio-Temporal Mamba for Real-world Video Super-resolution. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Learning to Generalize Without Bias for Open-Vocabulary Action Recognition. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- Keyframe-Oriented Vision Token Pruning: Enhancing Efficiency of Large Vision Language Models on Long-form Video Processing. → [network-pruning](../network-pruning/Guideline%202025.md)
- AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning. → [network-pruning](../network-pruning/Guideline%202025.md)
- 6D Object Pose Tracking in Internet Videos for Robotic Manipulation. → [tracking](../tracking/Guideline%202025.md)
- LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding. → [network-pruning](../network-pruning/Guideline%202025.md)
- Bisecle: Binding and Separation in Continual Learning for Video Language Understanding. → [continual-learning](../continual-learning/Guideline%202025.md)

<!-- COMPLETE v1 papers=103 -->
