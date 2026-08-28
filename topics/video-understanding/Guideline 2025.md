# Video Understanding — 2025 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 31 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### LVBench: An Extreme Long Video Understanding Benchmark.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02131) · 📚 被引 14
- **作者**: Weihan Wang, Zehai He, Wenyi Hong, Yean Cheng, Xiaohan Zhang, Ji Qi et al.
- **🏷️ 机构**: Zhipu AI, Tsinghua University
- **会议**: ICCV 2025

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human vision is dynamic and continuous. However, in video understanding with multimodal large language models (LLMs), existing methods primarily rely on static features extracted from images sampled at a fixed low frame rate of frame-per-second (FPS) $\leqslant$2, leading to critical visual information loss. In this paper, we introduce F-16, the first multimodal LLM designed for high-frame-rate video understanding. By increasing the frame rate to 16 FPS and compressing visual tokens within each 1-second clip, F-16 efficiently captures dynamic visual features while preserving key semantic information. Experimental results demonstrate that higher frame rates considerably enhance video understanding across multiple benchmarks, providing a new approach to improving video LLMs beyond scaling model size or training data. F-16 achieves state-of-the-art performance among 7-billion-parameter video LLMs on both general and fine-grained video understanding benchmarks, such as Video-MME and TemporalBench. Furthermore, F-16 excels in complex spatiotemporal tasks, including high-speed sports analysis (\textit{e.g.}, basketball, football, gymnastics, and diving), outperforming SOTA proprietary visual models like GPT-4o and Gemini-1.5-pro. Additionally, we introduce a novel decoding method for F-16 that enables highly efficient low-frame-rate inference without requiring model retraining. We will release the source code, model checkpoints, and data at \href{https://github.com/bytedance/F-16}{https://github.com/bytedance/F-16}.

</details>

### Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation.
- **链接**: [arXiv:2504.02438](https://arxiv.org/abs/2504.02438) · [代码](https://github.com/steven-ccq/ViLAMP)
- **作者**: Chuanqi Cheng, Jian Guan, Wei Wu, Rui Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### VideoAds for Fast-Paced Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02025) · 📚 被引 2
- **作者**: Zheyuan Zhang, Wanying Dou, Linkai Peng, Hongyi Pan, Ulas Bagci, Boqing Gong
- **🏷️ 机构**: Northwestern University, Boston University
- **会议**: ICCV 2025

### DynImg: Key Frames with Visual Prompts are Good Representation for Multi-Modal Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02198) · 📚 被引 0
- **作者**: Xiaoyi Bao, Chenwei Xie, Hao Tang, Tingyu Weng, Xiaofeng Wang, Yun Zheng et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Alibaba Group
- **会议**: ICCV 2025

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
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02198) · 📚 被引 0
- **作者**: Xiaoyi Bao, Chenwei Xie, Hao Tang, Tingyu Weng, Xiaofeng Wang, Yun Zheng et al.
- **🏷️ 机构**: Institute of Automation, Chinese Academy of Sciences, Alibaba Group
- **会议**: ICCV 2025

### LVAgent: Long Video Understanding by Multi-Round Dynamical Collaboration of MLLM Agents.
- **链接**: [arXiv:2503.10200](https://arxiv.org/abs/2503.10200) · [代码](https://github.com/64327069/LVAgent) · 📚 被引 5
- **作者**: Boyu Chen, Zhengrong Yue, Siran Chen, Zikang Wang, Yang Liu, Peng Li et al.
- **🏷️ 机构**: Shenzhen Key Lab of Computer Vision and Pattern Recognition, Shenzhen Institutes of Advanced Technology,Chinese Academy of Sciences, Shanghai Artificial Intelligence Laboratory, Institute for AI Industry Research (AIR), Tsinghua University,Beijing,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing MLLMs encounter significant challenges in modeling the temporal context within long videos. Currently, mainstream Agent-based methods use external tools to assist a single MLLM in answering long video questions. Despite such tool-based support, a solitary MLLM still offers only a partial understanding of long videos, resulting in limited performance. In order to better address long video tasks, we introduce LVAgent, the first framework enabling multi-round dynamic collaboration of MLLM agents in long video understanding. Our method consists of four key steps: 1) Selection: We pre-select appropriate agents from the model library to form optimal agent teams based on different tasks. 2) Perception: We design an effective retrieval scheme for long videos to improve the coverage of critical temporal segments while maintaining computational efficiency. 3) Action: Agents answer long video questions and exchange reasons. 4) Reflection: We evaluate each agent's performance in each round of discussion and optimize the agent team for dynamic collaboration. The agents iteratively refine their answers by multi-round dynamical collaboration of MLLM agents. LVAgent is the first agent system method that outperforms all closed-source models (like GPT-4o) and open-source models (like InternVL-2.5 and Qwen2-VL) in the long video understanding tasks. Our LVAgent achieves an accuracy of 80\% on four mainstream long video understanding tasks. Notably, LVAgent improves accuracy by 13.3\% on LongVideoBench. Code is available at https://github.com/64327069/LVAgent.

</details>

### VISTA: Enhancing Long-Duration and High-Resolution Video Understanding by Video Spatiotemporal Augmentation.
- **链接**: [arXiv:2412.00927](https://arxiv.org/abs/2412.00927) · 📚 被引 1
- **作者**: Weiming Ren, Huan Yang, Jie Min, Cong Wei, Wenhu Chen
- **🏷️ 机构**: University of Waterloo, 01.AI
- **会议**: CVPR 2025

### Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shu_Video-XL_Extra-Long_Vision_Language_Model_for_Hour-Scale_Video_Understanding_CVPR_2025_paper.html)
- **作者**: Yan Shu, Zheng Liu, Peitian Zhang, Minghao Qin, Junjie Zhou, Zhengyang Liang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding.
- **链接**: [arXiv:2412.00493](https://arxiv.org/abs/2412.00493) · 📚 被引 18
- **作者**: Duo Zheng, Shijia Huang, Liwei Wang
- **🏷️ 机构**: The Chinese University of Hong Kong
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video understanding has made huge strides in recent years, relying largely on the power of transformers. As this architecture is notoriously expensive and video data is highly redundant, research into improving efficiency has become particularly relevant. Some creative solutions include token selection and merging. While most methods succeed in reducing the cost of the model and maintaining accuracy, an interesting pattern arises: most methods do not outperform the baseline of randomly discarding tokens. In this paper we take a closer look at this phenomenon and observe 5 principles of the nature of visual tokens. For example, we observe that the value of tokens follows a clear Pareto-distribution where most tokens have remarkably low value, and just a few carry most of the perceptual information. We build on these and further insights to propose a lightweight video model, LITE, that can select a small number of tokens effectively, outperforming state-of-the-art and existing baselines across datasets (Kinetics-400 and Something-Something-V2) in the challenging trade-off of computation (GFLOPs) vs accuracy. Experiments also show that LITE generalizes across datasets and even other tasks without the need for retraining.

</details>

### Open-Ended Hierarchical Streaming Video Understanding with Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01926) · 📚 被引 1
- **作者**: Hyolim Kang, Yunsu Park, Youngbeom Yoo, Yeeun Choi, Seon Joo Kim
- **🏷️ 机构**: Yonsei University
- **会议**: ICCV 2025

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multi-modal Large language models (MLLMs) show remarkable ability in video understanding. Nevertheless, understanding long videos remains challenging as the models can only process a finite number of frames in a single inference, potentially omitting crucial visual information. To address the challenge, we propose generating multiple predictions through visual context sampling, followed by a scoring mechanism to select the final prediction. Specifically, we devise a bin-wise sampling strategy that enables MLLMs to generate diverse answers based on various combinations of keyframes, thereby enriching the visual context. To determine the final prediction from the sampled answers, we employ a self-reward by linearly combining three scores: (1) a frequency score indicating the prevalence of each option, (2) a marginal confidence score reflecting the inter-intra sample certainty of MLLM predictions, and (3) a reasoning score for different question types, including clue-guided answering for global questions and temporal self-refocusing for local questions. The frequency score ensures robustness through majority correctness, the confidence-aligned score reflects prediction certainty, and the typed-reasoning score addresses cases with sparse key visual information using tailored strategies. Experiments show that this approach covers the correct answer for a high percentage of long video questions, on seven datasets show that our method improves the performance of three MLLMs.

</details>

### Flow4Agent: Long-form Video Understanding via Motion Prior from Optical Flow.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02211) · 📚 被引 0
- **作者**: Ruyang Liu, Shangkun Sun, Haoran Tang, Wei Gao, Ge Li
- **🏷️ 机构**: School of Electronic and Computer Engineering, Shenzhen Graduate School, Peking University
- **会议**: ICCV 2025

### AdsQA: Towards Advertisement Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02172) · 📚 被引 2
- **作者**: Xinwei Long, Kai Tian, Peng Xu, Guoli Jia, Jingxuan Li, Sa Yang et al.
- **🏷️ 机构**: Tsinghua University, Independent Researcher, Peking University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Do we still need to represent objects explicitly in multimodal large language models (MLLMs)? To one extreme, pre-trained encoders convert images into visual tokens, with which objects and spatiotemporal relationships may be implicitly modeled. To the other extreme, image captions by themselves provide strong empirical performances for understanding tasks, despite missing fine-grained spatiotemporal information. To answer this question, we introduce ObjectMLLM, a framework capable of leveraging arbitrary computer vision algorithm to extract and integrate structured visual representation. Through extensive evaluations on six video question answering benchmarks, we confirm that explicit integration of object-centric representation remains necessary. Surprisingly, we observe that the simple approach of quantizing the continuous, structured object information and representing them as plain text performs the best, offering a data-efficient approach to integrate other visual perception modules into MLLM design. Our code and models are released at https://github.com/brown-palm/ObjectMLLM.

</details>

### Bringing RNNs Back to Efficient Open-Ended Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02177) · 📚 被引 0
- **作者**: Weili Xu, Enxin Song, Wenhao Chai, Xuexiang Wen, Tian Ye, Gaoang Wang
- **🏷️ 机构**: Zhejiang University, University of Washington, HKUST (GZ)
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite advancements in multimodal large language models (MLLMs), current approaches struggle in medium-to-long video understanding due to frame and context length limitations. As a result, these models often depend on frame sampling, which risks missing key information over time and lacks task-specific relevance. To address these challenges, we introduce HierarQ, a task-aware hierarchical Q-Former based framework that sequentially processes frames to bypass the need for frame sampling, while avoiding LLM's context length limitations. We introduce a lightweight two-stream language-guided feature modulator to incorporate task awareness in video understanding, with the entity stream capturing frame-level object information within a short context and the scene stream identifying their broader interactions over longer period of time. Each stream is supported by dedicated memory banks which enables our proposed Hierachical Querying transformer (HierarQ) to effectively capture short and long-term context. Extensive evaluations on 10 video benchmarks across video understanding, question answering, and captioning tasks demonstrate HierarQ's state-of-the-art performance across most datasets, proving its robustness and efficiency for comprehensive video analysis.

</details>

### DynFocus: Dynamic Cooperative Network Empowers LLMs with Video Understanding.
- **链接**: [arXiv:2411.12355](https://arxiv.org/abs/2411.12355) · 📚 被引 0
- **作者**: Yudong Han, Qingpei Guo, Liyuan Pan, Liu Liu, Yu Guan, Ming Yang
- **🏷️ 机构**: Beijing Institute of Technology, Ant Group, Huawei,KooMap Dept.
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The challenge in LLM-based video understanding lies in preserving visual and semantic information in long videos while maintaining a memory-affordable token count. However, redundancy and correspondence in videos have hindered the performance potential of existing methods. Through statistical learning on current datasets, we observe that redundancy occurs in both repeated and answer-irrelevant frames, and the corresponding frames vary with different questions. This suggests the possibility of adopting dynamic encoding to balance detailed video information preservation with token budget reduction. To this end, we propose a dynamic cooperative network, DynFocus, for memory-efficient video encoding in this paper. Specifically, i) a Dynamic Event Prototype Estimation (DPE) module to dynamically select meaningful frames for question answering; (ii) a Compact Cooperative Encoding (CCE) module that encodes meaningful frames with detailed visual appearance and the remaining frames with sketchy perception separately. We evaluate our method on five publicly available benchmarks, and experimental results consistently demonstrate that our method achieves competitive performance.

</details>

### STOP: Integrated Spatial-Temporal Dynamic Prompting for Video Understanding.
- **链接**: [arXiv:2503.15973](https://arxiv.org/abs/2503.15973) · [代码](https://github.com/zhoujiahuan1991/CVPR2025-STOP) · 📚 被引 6
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

### Towards Universal Soccer Video Understanding.
- **链接**: [arXiv:2412.01820](https://arxiv.org/abs/2412.01820) · 📚 被引 18
- **作者**: Jiayuan Rao, Haoning Wu, Hao Jiang, Ya Zhang, Yanfeng Wang, Weidi Xie
- **🏷️ 机构**: Shanghai Jiao Tong University,School of Artificial Intelligence,China, Alibaba Group,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> As a globally celebrated sport, soccer has attracted widespread interest from fans all over the world. This paper aims to develop a comprehensive multi-modal framework for soccer video understanding. Specifically, we make the following contributions in this paper: (i) we introduce SoccerReplay-1988, the largest multi-modal soccer dataset to date, featuring videos and detailed annotations from 1,988 complete matches, with an automated annotation pipeline; (ii) we present an advanced soccer-specific visual encoder, MatchVision, which leverages spatiotemporal information across soccer videos and excels in various downstream tasks; (iii) we conduct extensive experiments and ablation studies on event classification, commentary generation, and multi-view foul recognition. MatchVision demonstrates state-of-the-art performance on all of them, substantially outperforming existing models, which highlights the superiority of our proposed data and model. We believe that this work will offer a standard paradigm for sports understanding research.

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

### Temporal Alignment-Free Video Matching for Few-shot Action Recognition.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Temporal_Alignment-Free_Video_Matching_for_Few-shot_Action_Recognition_CVPR_2025_paper.html) · 📚 被引 10
- **作者**: SuBeen Lee, WonJun Moon, Hyun Seok Seong, Jae-Pil Heo
- **🏷️ 机构**: Sungkyunkwan University
- **会议**: CVPR 2025

## 跨领域论文（完整笔记在其他领域）

- Anomize: Better Open Vocabulary Video Anomaly Detection. → [open-set-detection](../open-set-detection/Guideline%202025.md)
- VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- When the Future Becomes the Past: Taming Temporal Correspondence for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
- Self-supervised ControlNet with Spatio-Temporal Mamba for Real-world Video Super-resolution. → [self-supervised-vision](../self-supervised-vision/Guideline%202025.md)
