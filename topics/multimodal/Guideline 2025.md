# Multimodal — 2025 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 73 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Can MLLMs Reason in Multimodality? EMMA: An Enhanced MultiModal ReAsoning Benchmark.
- **链接**: [arXiv:2501.05444](https://arxiv.org/abs/2501.05444)
- **作者**: Yunzhuo Hao, Jiawei Gu, Huichen Will Wang, Linjie Li, Zhengyuan Yang, Lijuan Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ability to organically reason over and with both text and images is a pillar of human intelligence, yet the ability of Multimodal Large Language Models (MLLMs) to perform such multimodal reasoning remains under-explored. Existing benchmarks often emphasize text-dominant reasoning or rely on shallow visual cues, failing to adequately assess integrated visual and textual reasoning. We introduce EMMA (Enhanced MultiModal reAsoning), a benchmark targeting organic multimodal reasoning across mathematics, physics, chemistry, and coding. EMMA tasks demand advanced cross-modal reasoning that cannot be addressed by reasoning independently in each modality, offering an enhanced test suite for MLLMs' reasoning capabilities. Our evaluation of state-of-the-art MLLMs on EMMA reveals significant limitations in handling complex multimodal and multi-step reasoning tasks, even with advanced techniques like Chain-of-Thought prompting and test-time compute scaling underperforming. These findings underscore the need for improved multimodal architectures and training paradigms to close the gap between human and model reasoning in multimodality.

</details>

### AffectGPT: A New Dataset, Model, and Benchmark for Emotion Understanding with Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lian25a.html)
- **作者**: Zheng Lian, Haoyu Chen, Lan Chen, Haiyang Sun, Licai Sun, Yong Ren et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations.
- **链接**: [arXiv:2412.01441](https://arxiv.org/abs/2412.01441)
- **作者**: Anian Ruoss, Fabio Pardo, Harris Chan, Bonnie Li, Volodymyr Mnih, Tim Genewein
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we present a benchmark to pressure-test today's frontier models' multimodal decision-making capabilities in the very long-context regime (up to one million tokens) and investigate whether these models can learn from large numbers of expert demonstrations in their context. We evaluate the performance of Claude 3.5 Sonnet, Gemini 1.5 Flash, Gemini 1.5 Pro, Gemini 2.0 Flash Experimental, GPT-4o, o1-mini, o1-preview, and o1 as policies across a battery of simple interactive decision-making tasks: playing tic-tac-toe, chess, and Atari, navigating grid worlds, solving crosswords, and controlling a simulated cheetah. We study increasing amounts of expert demonstrations in the context $\unicode{x2013}$ from no demonstrations to 512 full episodes. Across our tasks, models rarely manage to fully reach expert performance, and often, presenting more demonstrations has little effect. Some models steadily improve with more demonstrations on a few tasks. We investigate the effect of encoding observations as text or images and the impact of chain-of-thought prompting. To help quantify the impact of other approaches and future innovations, we open source our benchmark that covers the zero-, few-, and many-shot regimes in a unified evaluation.

</details>

### How Do Images Align and Complement LiDAR? Towards a Harmonized Multi-modal 3D Panoptic Segmentation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/pan25c.html)
- **作者**: Yining Pan, Qiongjie Cui, Xulei Yang, Na Zhao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### OV-MER: Towards Open-Vocabulary Multimodal Emotion Recognition.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lian25b.html)
- **作者**: Zheng Lian, Haiyang Sun, Licai Sun, Haoyu Chen, Lan Chen, Hao Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents.
- **链接**: [arXiv:2502.09560](https://arxiv.org/abs/2502.09560)
- **作者**: Rui Yang, Hanyang Chen, Junyu Zhang, Mark Zhao, Cheng Qian, Kangrui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leveraging Multi-modal Large Language Models (MLLMs) to create embodied agents offers a promising avenue for tackling real-world tasks. While language-centric embodied agents have garnered substantial attention, MLLM-based embodied agents remain underexplored due to the lack of comprehensive evaluation frameworks. To bridge this gap, we introduce EmbodiedBench, an extensive benchmark designed to evaluate vision-driven embodied agents. EmbodiedBench features: (1) a diverse set of 1,128 testing tasks across four environments, ranging from high-level semantic tasks (e.g., household) to low-level tasks involving atomic actions (e.g., navigation and manipulation); and (2) six meticulously curated subsets evaluating essential agent capabilities like commonsense reasoning, complex instruction understanding, spatial awareness, visual perception, and long-term planning. Through extensive experiments, we evaluated 24 leading proprietary and open-source MLLMs within EmbodiedBench. Our findings reveal that: MLLMs excel at high-level tasks but struggle with low-level manipulation, with the best model, GPT-4o, scoring only 28.9\% on average. EmbodiedBench provides a multifaceted standardized evaluation platform that not only highlights existing challenges but also offers valuable insights to advance MLLM-based embodied agents. Our code and dataset are available at https://embodiedbench.github.io.

</details>

### Visual Graph Arena: Evaluating Visual Conceptualization of Vision and Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/babaiee25a.html)
- **作者**: Zahra Babaiee, Peyman M. Kiasari, Daniela Rus, Radu Grosu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Vision-Language Models Create Cross-Modal Task Representations.
- **链接**: [出版页](https://proceedings.mlr.press/v267/luo25c.html)
- **作者**: Grace Luo, Trevor Darrell, Amir Bar
- **🏷️ 机构**: UC Berkeley
- **会议**: ICML 2025

### Time-VLM: Exploring Multimodal Vision-Language Models for Augmented Time Series Forecasting.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhong25a.html)
- **作者**: Siru Zhong, Weilin Ruan, Ming Jin, Huan Li, Qingsong Wen, Yuxuan Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhu25v.html)
- **作者**: Kangyu Zhu, Peng Xia, Yun Li, Hongtu Zhu, Sheng Wang, Huaxiu Yao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### On Path to Multimodal Generalist: General-Level and General-Bench.
- **链接**: [出版页](https://proceedings.mlr.press/v267/fei25a.html)
- **作者**: Hao Fei, Yuan Zhou, Juncheng Li, Xiangtai Li, Qingshan Xu, Bobo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Multimodal Medical Code Tokenizer.
- **链接**: [出版页](https://proceedings.mlr.press/v267/su25b.html)
- **作者**: Xiaorui Su, Shvat Messica, Yepeng Huang, Ruth Johnson, Lukas Fesser, Shanghua Gao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zou25e.html)
- **作者**: Xin Zou, Yizhou Wang, Yibo Yan, Yuanhuiyi Lyu, Kening Zheng, Sirui Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Decomposition of Graphic Design with Unified Multimodal Model.
- **链接**: [出版页](https://proceedings.mlr.press/v267/nie25c.html)
- **作者**: Hui Nie, Zhao Zhang, Yutao Cheng, Maoke Yang, Gonglei Shi, Qingsong Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### MTSTRec: Multimodal Time-Aligned Shared Token Recommender.
- **链接**: [出版页](https://proceedings.mlr.press/v267/hong25b.html)
- **作者**: Ming-Yi Hong, Yen-Jung Hsu, Miao-Chen Chiang, Che Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering.
- **链接**: [出版页](https://proceedings.mlr.press/v267/song25g.html)
- **作者**: Zihan Song, Xin Wang, Zi Qian, Hong Chen, Longtao Huang, Hui Xue et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/huang25q.html)
- **作者**: Wenke Huang, Jian Liang, Zekun Shi, Didi Zhu, Guancheng Wan, He Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### LEMoN: Label Error Detection using Multimodal Neighbors.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25b.html)
- **作者**: Haoran Zhang, Aparna Balagopalan, Nassim Oufattole, Hyewon Jeong, Yan Wu, Jiacheng Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/chen25n.html)
- **作者**: Jinpeng Chen, Runmin Cong, Yuzhi Zhao, Hongzheng Yang, Guangneng Hu, Horace H. S. Ip et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### MM-RLHF: The Next Step Forward in Multimodal LLM Alignment.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25cs.html)
- **作者**: Yifan Zhang, Tao Yu, Haochen Tian, Chaoyou Fu, Peiyan Li, Jianshu Zeng et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SK-VQA: Synthetic Knowledge Generation at Scale for Training Context-Augmented Multimodal LLMs.
- **链接**: [出版页](https://proceedings.mlr.press/v267/su25a.html)
- **作者**: Xin Su, Man Luo, Kris W. Pan, Tien Pei Chou, Vasudev Lal, Phillip Howard
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/dai25b.html)
- **作者**: Wei Dai, Peilin Chen, Malinda Lu, Daniel Li, Haowen Wei, Hejie Cui et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Diving into Self-Evolving Training for Multimodal Reasoning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/liu25aj.html)
- **作者**: Wei Liu, Junlong Li, Xiwen Zhang, Fan Zhou, Yu Cheng, Junxian He
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Aligning Multimodal Representations through an Information Bottleneck.
- **链接**: [出版页](https://proceedings.mlr.press/v267/almudevar25a.html)
- **作者**: Antonio Almudévar, José Miguel Hernández-Lobato, Sameer Khurana, Ricard Marxer, Alfonso Ortega
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts.
- **链接**: [出版页](https://proceedings.mlr.press/v267/braun25b.html)
- **作者**: Tobias Braun, Mark Rothermel, Marcus Rohrbach, Anna Rohrbach
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### AGAV-Rater: Adapting Large Multimodal Model for AI-Generated Audio-Visual Quality Assessment.
- **链接**: [出版页](https://proceedings.mlr.press/v267/cao25f.html)
- **作者**: Yuqin Cao, Xiongkuo Min, Yixuan Gao, Wei Sun, Guangtao Zhai
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### CtrlSynth: Controllable Image Text Synthesis for Data-Efficient Multimodal Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/cao25g.html)
- **作者**: Qingqing Cao, Mahyar Najibi, Sachin Mehta
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### LV-XAttn: Distributed Cross-Attention for Long Visual Inputs in Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/chang25c.html)
- **作者**: Tzu-Tao Chang, Shivaram Venkataraman
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### A Closer Look at Multimodal Representation Collapse.
- **链接**: [arXiv:2505.22483](https://arxiv.org/abs/2505.22483)
- **作者**: Abhra Chaudhuri, Anjan Dutta, Tu Bui, Serban Georgescu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We aim to develop a fundamental understanding of modality collapse, a recently observed empirical phenomenon wherein models trained for multimodal fusion tend to rely only on a subset of the modalities, ignoring the rest. We show that modality collapse happens when noisy features from one modality are entangled, via a shared set of neurons in the fusion head, with predictive features from another, effectively masking out positive contributions from the predictive features of the former modality and leading to its collapse. We further prove that cross-modal knowledge distillation implicitly disentangles such representations by freeing up rank bottlenecks in the student encoder, denoising the fusion-head outputs without negatively impacting the predictive features from either modality. Based on the above findings, we propose an algorithm that prevents modality collapse through explicit basis reallocation, with applications in dealing with missing modalities. Extensive experiments on multiple multimodal benchmarks validate our theoretical claims. Project page: https://abhrac.github.io/mmcollapse/.

</details>

### Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development.
- **链接**: [出版页](https://proceedings.mlr.press/v267/chen25bm.html)
- **作者**: Daoyuan Chen, Haibin Wang, Yilun Huang, Ce Ge, Yaliang Li, Bolin Ding et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/fang25h.html)
- **作者**: Yiyang Fang, Jian Liang, Wenke Huang, He Li, Kehua Su, Mang Ye
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning.
- **链接**: [arXiv:2506.11672](https://arxiv.org/abs/2506.11672)
- **作者**: Chendi Ge, Xin Wang, Zeyang Zhang, Hong Chen, Jiapei Fan, Longtao Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Continual multimodal instruction tuning is crucial for adapting Multimodal Large Language Models (MLLMs) to evolving tasks. However, most existing methods adopt a fixed architecture, struggling with adapting to new tasks due to static model capacity. We propose to evolve the architecture under parameter budgets for dynamic task adaptation, which remains unexplored and imposes two challenges: 1) task architecture conflict, where different tasks require varying layer-wise adaptations, and 2) modality imbalance, where different tasks rely unevenly on modalities, leading to unbalanced updates. To address these challenges, we propose a novel Dynamic Mixture of Curriculum LoRA Experts (D-MoLE) method, which automatically evolves MLLM's architecture with controlled parameter budgets to continually adapt to new tasks while retaining previously learned knowledge. Specifically, we propose a dynamic layer-wise expert allocator, which automatically allocates LoRA experts across layers to resolve architecture conflicts, and routes instructions layer-wisely to facilitate knowledge sharing among experts. Then, we propose a gradient-based inter-modal continual curriculum, which adjusts the update ratio of each module in MLLM based on the difficulty of each modality within the task to alleviate the modality imbalance problem. Extensive experiments show that D-MoLE significantly outperforms state-of-the-art baselines, achieving a 15% average improvement over the best baseline. To the best of our knowledge, this is the first study of continual learning for MLLMs from an architectural perspective.

</details>

### Gradient Inversion of Multimodal Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/hemo25a.html)
- **作者**: Omri Ben Hemo, Alon Zolfi, Oryan Yehezkel, Omer Hofman, Roman Vainshtein, Hisashi Kojima et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Compression via Pre-trained Transformers: A Study on Byte-Level Multimodal Data.
- **链接**: [出版页](https://proceedings.mlr.press/v267/heurtel-depeiges25a.html)
- **作者**: David Heurtel-Depeiges, Anian Ruoss, Joel Veness, Tim Genewein
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Elucidating the Design Space of Multimodal Protein Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/hsieh25a.html)
- **作者**: Cheng-Yen Hsieh, Xinyou Wang, Daiheng Zhang, Dongyu Xue, Fei Ye, Shujian Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency.
- **链接**: [出版页](https://proceedings.mlr.press/v267/jiang25n.html)
- **作者**: Dongzhi Jiang, Renrui Zhang, Ziyu Guo, Yanwei Li, Yu Qi, Xinyan Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Visual Attention Never Fades: Selective Progressive Attention ReCalibration for Detailed Image Captioning in Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/jung25c.html)
- **作者**: Mingi Jung, Saehyung Lee, Eunji Kim, Sungroh Yoon
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### M3-JEPA: Multimodal Alignment via Multi-gate MoE based on the Joint-Embedding Predictive Architecture.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lei25b.html)
- **作者**: Hongyang Lei, Xiaolong Cheng, Qi Qin, Dan Wang, Huazhen Huang, Qingqing Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### R2-T2: Re-Routing in Test-Time for Multimodal Mixture-of-Experts.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25bc.html)
- **作者**: Zhongyang Li, Ziyue Li, Tianyi Zhou
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### From Black Boxes to Transparent Minds: Evaluating and Enhancing the Theory of Mind in Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25bj.html)
- **作者**: Xinyang Li, Siqi Liu, Bochao Zou, Jiansheng Chen, Huimin Ma
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25cw.html)
- **作者**: Zichao Li, Xueru Wen, Jie Lou, Yuqiu Ji, Yaojie Lu, Xianpei Han et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Imagine While Reasoning in Space: Multimodal Visualization-of-Thought.
- **链接**: [出版页](https://proceedings.mlr.press/v267/li25cz.html)
- **作者**: Chengzu Li, Wenshan Wu, Huanyu Zhang, Yan Xia, Shaoguang Mao, Li Dong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### SAE-V: Interpreting Multimodal Models for Enhanced Alignment.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lou25b.html)
- **作者**: Hantao Lou, Changye Li, Jiaming Ji, Yaodong Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Agent Reviewers: Domain-specific Multimodal Agents with Shared Memory for Paper Review.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lu25p.html)
- **作者**: Kai Lu, Shixiong Xu, Jinqiu Li, Kun Ding, Gaofeng Meng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Improving Multimodal Learning Balance and Sufficiency through Data Remixing.
- **链接**: [出版页](https://proceedings.mlr.press/v267/ma25c.html)
- **作者**: Xiaoyu Ma, Hao Chen, Yongjian Deng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Reasoning Limitations of Multimodal Large Language Models. A case study of Bongard Problems.
- **链接**: [出版页](https://proceedings.mlr.press/v267/malkinski25a.html)
- **作者**: Mikolaj Malkinski, Szymon Pawlonka, Jacek Mandziuk
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Aggregation of Dependent Expert Distributions in Multimodal Variational Autoencoders.
- **链接**: [出版页](https://proceedings.mlr.press/v267/a-mancisidor25a.html)
- **作者**: Rogelio Andrade Mancisidor, Robert Jenssen, Shujian Yu, Michael Kampffmeyer
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### I Think, Therefore I Diffuse: Enabling Multimodal In-Context Reasoning in Diffusion Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/mi25a.html)
- **作者**: Zhenxing Mi, Kuan-Chieh Wang, Guocheng Qian, Hanrong Ye, Runtao Liu, Sergey Tulyakov et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### RollingQ: Reviving the Cooperation Dynamics in Multimodal Transformer.
- **链接**: [出版页](https://proceedings.mlr.press/v267/ni25a.html)
- **作者**: Haotian Ni, Yake Wei, Hang Liu, Gong Chen, Chong Peng, Hao Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Graph4MM: Weaving Multimodal Learning with Structural Information.
- **链接**: [arXiv:2510.16990](https://arxiv.org/abs/2510.16990)
- **作者**: Xuying Ning, Dongqi Fu, Tianxin Wei, Wujiang Xu, Jingrui He
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Real-world multimodal data usually exhibit complex structural relationships beyond traditional one-to-one mappings like image-caption pairs. Entities across modalities interact in intricate ways, with images and text forming diverse interconnections through contextual dependencies and co-references. Graphs provide powerful structural information for modeling intra-modal and inter-modal relationships. However, previous works fail to distinguish multi-hop neighbors and treat the graph as a standalone modality, which fragments the overall understanding. This limitation presents two key challenges in multimodal learning: (1) integrating structural information from multi-hop neighbors into foundational models, and (2) fusing modality-specific information in a principled manner. To address these challenges, we revisit the role of graphs in multimodal learning within the era of foundation models and propose Graph4MM, a graph-based multimodal learning framework. To be specific, we introduce Hop-Diffused Attention, which integrates multi-hop structural information into self-attention through causal masking and hop diffusion. Furthermore, we design MM-QFormer, a multi-mapping querying transformer for cross-modal fusion. Through theoretical and empirical analysis, we show that leveraging structures to integrate both intra- and inter-modal interactions improves multimodal understanding beyond treating them as a standalone modality. Experiments on both generative and discriminative tasks show that Graph4MM outperforms larger VLMs, LLMs, and multimodal graph baselines, achieving a 6.93% average improvement.

</details>

### Test-Time Multimodal Backdoor Detection by Contrastive Prompting.
- **链接**: [出版页](https://proceedings.mlr.press/v267/niu25b.html)
- **作者**: Yuwei Niu, Shuo He, Qi Wei, Zongyu Wu, Feng Liu, Lei Feng
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach.
- **链接**: [出版页](https://proceedings.mlr.press/v267/oh25a.html)
- **作者**: Changdae Oh, Zhen Fang, Shawn Im, Xuefeng Du, Yixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### GoIRL: Graph-Oriented Inverse Reinforcement Learning for Multimodal Trajectory Prediction.
- **链接**: [出版页](https://proceedings.mlr.press/v267/pei25c.html)
- **作者**: Muleilan Pei, Shaoshuai Shi, Lu Zhang, Peiliang Li, Shaojie Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Diffuse Everything: Multimodal Diffusion Models on Arbitrary State Spaces.
- **链接**: [arXiv:2506.07903](https://arxiv.org/abs/2506.07903)
- **作者**: Kevin Rojas, Yuchen Zhu, Sichen Zhu, Felix X.-F. Ye, Molei Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models have demonstrated remarkable performance in generating unimodal data across various tasks, including image, video, and text generation. On the contrary, the joint generation of multimodal data through diffusion models is still in the early stages of exploration. Existing approaches heavily rely on external preprocessing protocols, such as tokenizers and variational autoencoders, to harmonize varied data representations into a unified, unimodal format. This process heavily demands the high accuracy of encoders and decoders, which can be problematic for applications with limited data. To lift this restriction, we propose a novel framework for building multimodal diffusion models on arbitrary state spaces, enabling native generation of coupled data across different modalities. By introducing an innovative decoupled noise schedule for each modality, we enable both unconditional and modality-conditioned generation within a single model simultaneously. We empirically validate our approach for text-image generation and mixed-type tabular data synthesis, demonstrating that it achieves competitive performance.

</details>

### GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing.
- **链接**: [arXiv:2501.13925](https://arxiv.org/abs/2501.13925)
- **作者**: Akashah Shabbir, Mohammed Zumri, Mohammed Bennamoun, Fahad Shahbaz Khan, Salman Khan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in large multimodal models (LMMs) have recognized fine-grained grounding as an imperative factor of visual understanding and dialogue. However, the benefits of such representation in LMMs are limited to the natural image domain, and these models perform poorly for remote sensing (RS). The distinct overhead viewpoint, scale variation, and presence of small objects in high-resolution RS imagery present a unique challenge in region-level comprehension. Moreover, the development of the grounding conversation capability of LMMs within RS is hindered by the lack of granular, RS domain-specific grounded data. Addressing these limitations, we propose GeoPixel - the first end-to-end high resolution RS-LMM that supports pixel-level grounding. This capability allows fine-grained visual perception by generating interleaved masks in conversation. GeoPixel supports up to 4K HD resolution in any aspect ratio, ideal for high-precision RS image analysis. To support the grounded conversation generation (GCG) in RS imagery, we curate a visually grounded dataset GeoPixelD through a semi-automated pipeline that utilizes set-of-marks prompting and spatial priors tailored for RS data to methodically control the data generation process. GeoPixel demonstrates superior performance in pixel-level comprehension, surpassing existing LMMs in both single-target and multi-target segmentation tasks. Our methodological ablation studies validate the effectiveness of each component in the overall architecture. Our code and data will be publicly released.

</details>

### SAFER: A Calibrated Risk-Aware Multimodal Recommendation Model for Dynamic Treatment Regimes.
- **链接**: [出版页](https://proceedings.mlr.press/v267/shen25l.html)
- **作者**: Yishan Shen, Yuyang Ye, Hui Xiong, Yong Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Efficiently Serving Large Multimodal Models Using EPD Disaggregation.
- **链接**: [出版页](https://proceedings.mlr.press/v267/singh25d.html)
- **作者**: Gursimran Singh, Xinglu Wang, Yifan Hu, Timothy Tin Long Yu, Linzi Xing, Wei Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### WMarkGPT: Watermarked Image Understanding via Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/tan25f.html)
- **作者**: Songbai Tan, Xuerui Qiu, Yao Shu, Gang Xu, Linrui Xu, Xiangyu Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Understanding the Emergence of Multimodal Representation Alignment.
- **链接**: [出版页](https://proceedings.mlr.press/v267/tjandrasuwita25a.html)
- **作者**: Megan Tjandrasuwita, Chanakya Ekbote, Liu Ziyin, Paul Pu Liang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Ranked from Within: Ranking Large Multimodal Models Without Labels.
- **链接**: [出版页](https://proceedings.mlr.press/v267/tu25a.html)
- **作者**: Weijie Tu, Weijian Deng, Dylan Campbell, Yu Yao, Jiyang Zheng, Tom Gedeon et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### PyTDC: A multimodal machine learning training, evaluation, and inference platform for biomedical foundation models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/velez-arce25a.html)
- **作者**: Alejandro Velez-Arce, Marinka Zitnik
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Topological Signatures of Adversaries in Multimodal Alignments.
- **链接**: [出版页](https://proceedings.mlr.press/v267/vu25a.html)
- **作者**: Minh Nhat Vu, Geigh Zollicoffer, Huy Quang Mai, Ben Nebgen, Boian S. Alexandrov, Manish Bhattarai
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Learning Optimal Multimodal Information Bottleneck Representations.
- **链接**: [出版页](https://proceedings.mlr.press/v267/wu25x.html)
- **作者**: Qilong Wu, Yiyang Shao, Jun Wang, Xiaobo Sun
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### When Every Millisecond Counts: Real-Time Anomaly Detection via the Multimodal Asynchronous Hybrid Network.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xiao25a.html)
- **作者**: Dong Xiao, Guangyao Chen, Peixi Peng, Yangru Huang, Yifan Zhao, Yongxing Dai et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### I2MoE: Interpretable Multimodal Interaction-aware Mixture-of-Experts.
- **链接**: [出版页](https://proceedings.mlr.press/v267/xin25c.html)
- **作者**: Jiayi Xin, Sukwon Yun, Jie Peng, Inyoung Choi, Jenna L. Ballard, Tianlong Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Efficient Quantification of Multimodal Interaction at Sample Level.
- **链接**: [出版页](https://proceedings.mlr.press/v267/yang25aj.html)
- **作者**: Zequn Yang, Hongfa Wang, Di Hu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Robust Multimodal Large Language Models Against Modality Conflict.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25dq.html)
- **作者**: Zongmeng Zhang, Wengang Zhou, Jie Zhao, Houqiang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### MP-Nav: Enhancing Data Poisoning Attacks against Multimodal Learning.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25am.html)
- **作者**: Jingfeng Zhang, Prashanth Krishnamurthy, Naman Patel, Anthony Tzes, Farshad Khorrami
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning: A Scalable Bayesian Planner.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25bk.html)
- **作者**: Chunhui Zhang, Zhongyu Ouyang, Kwonjoon Lee, Nakul Agarwal, Sean Dae Houlihan, Soroush Vosoughi et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhang25cg.html)
- **作者**: Zhicheng Zhang, Wuyou Xia, Chenxi Zhao, Zhou Yan, Xiaoqiang Liu, Yongjie Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### CPCF: A Cross-Prompt Contrastive Framework for Referring Multimodal Large Language Models.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhu25h.html)
- **作者**: Lanyun Zhu, Deyi Ji, Tianrun Chen, Haiyang Wu, De Wen Soh, Jun Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### EasyRef: Omni-Generalized Group Image Reference for Diffusion Models via Multimodal LLM.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zong25a.html)
- **作者**: Zhuofan Zong, Dongzhi Jiang, Bingqi Ma, Guanglu Song, Hao Shao, Dazhong Shen et al.
- **🏷️ 机构**: SenseTime, CUHK
- **会议**: ICML 2025

## 跨领域论文（完整笔记在其他领域）

- SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
