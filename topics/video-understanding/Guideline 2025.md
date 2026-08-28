# Video Understanding — 2025 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 17 · 按重要性排序（引用数/标题信号启发式）

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

### Principles of Visual Tokens for Efficient Video Understanding.
- **链接**: [arXiv:2411.13626](https://arxiv.org/abs/2411.13626) · 📚 被引 1
- **作者**: Xinyue Hao, Gen Li, Shreyank N. Gowda, Robert B. Fisher, Jonathan Huang, Anurag Arnab et al.
- **🏷️ 机构**: University of Edinburgh, University of Nottingham, Scaled Foundations
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video understanding has made huge strides in recent years, relying largely on the power of transformers. As this architecture is notoriously expensive and video data is highly redundant, research into improving efficiency has become particularly relevant. Some creative solutions include token selection and merging. While most methods succeed in reducing the cost of the model and maintaining accuracy, an interesting pattern arises: most methods do not outperform the baseline of randomly discarding tokens. In this paper we take a closer look at this phenomenon and observe 5 principles of the nature of visual tokens. For example, we observe that the value of tokens follows a clear Pareto-distribution where most tokens have remarkably low value, and just a few carry most of the perceptual information. We build on these and further insights to propose a lightweight video model, LITE, that can select a small number of tokens effectively, outperforming state-of-the-art and existing baselines across datasets (Kinetics-400 and Something-Something-V2) in the challenging trade-off of computation (GFLOPs) vs accuracy. Experiments also show that LITE generalizes across datasets and even other tasks without the need for retraining.

</details>

### Open-Ended Hierarchical Streaming Video Understanding with Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01926) · 📚 被引 1
- **作者**: Hyolim Kang, Yunsu Park, Youngbeom Yoo, Yeeun Choi, Seon Joo Kim
- **🏷️ 机构**: Yonsei University
- **会议**: ICCV 2025

### Breaking the Encoder Barrier for Seamless Video-Language Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02151) · 📚 被引 0
- **作者**: Handong Li, Yiyuan Zhang, Longteng Guo, Xiangyu Yue, Jing Liu
- **🏷️ 机构**: School of Artificial Intelligence, University of Chinese Academy of Sciences, CUHK,MMLab
- **会议**: ICCV 2025

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

### From Trial to Triumph: Advancing Long Video Understanding via Visual Context Sample Scaling and Self-Reward Alignment.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02158) · 📚 被引 1
- **作者**: Yucheng Suo, Fan Ma, Linchao Zhu, Tianyi Wang, Fengyun Rao, Yi Yang
- **🏷️ 机构**: Zhejiang University, Tencent Inc.
- **会议**: ICCV 2025

### How Can Objects Help Video-Language Understanding?
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02042) · 📚 被引 0
- **作者**: Zitian Tang, Shijie Wang, Junho Cho, Jaewook Yoo, Chen Sun
- **🏷️ 机构**: Brown University, Samsung Electronics
- **会议**: ICCV 2025

### Bringing RNNs Back to Efficient Open-Ended Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02177) · 📚 被引 0
- **作者**: Weili Xu, Enxin Song, Wenhao Chai, Xuexiang Wen, Tian Ye, Gaoang Wang
- **🏷️ 机构**: Zhejiang University, University of Washington, HKUST (GZ)
- **会议**: ICCV 2025

### Beyond Training: Dynamic Token Merging for Zero-Shot Video Understanding.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02047) · 📚 被引 2
- **作者**: Yiming Zhang, Zhuokai Zhao, Zhaorun Chen, Zenghui Ding, Xianjun Yang, Yining Sun
- **🏷️ 机构**: HFIPS, Chinese Academy of Sciences, University of Chicago
- **会议**: ICCV 2025

## 跨领域论文（完整笔记在其他领域）

- MCAM: Multimodal Causal Analysis Model for Ego-Vehicle-Level Driving Video Understanding. → [multimodal](../multimodal/Guideline%202025.md)
