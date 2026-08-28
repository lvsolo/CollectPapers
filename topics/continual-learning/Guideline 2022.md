# Continual Learning — 2022 Guideline

> 领域: 持续学习 / 增量学习（含 VLM/多模态场景）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Learning a Condensed Frame for Memory-Efficient Video Class-Incremental Learning.
- **链接**: [arXiv:2211.00833](https://arxiv.org/abs/2211.00833) · 📚 被引 1
- **作者**: Yixuan Pei, Zhiwu Qing, Jun Cen, Xiang Wang, Shiwei Zhang, Yaxiong Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent incremental learning for action recognition usually stores representative videos to mitigate catastrophic forgetting. However, only a few bulky videos can be stored due to the limited memory. To address this problem, we propose FrameMaker, a memory-efficient video class-incremental learning approach that learns to produce a condensed frame for each selected video. Specifically, FrameMaker is mainly composed of two crucial components: Frame Condensing and Instance-Specific Prompt. The former is to reduce the memory cost by preserving only one condensed frame instead of the whole video, while the latter aims to compensate the lost spatio-temporal details in the Frame Condensing stage. By this means, FrameMaker enables a remarkable reduction in memory but keep enough information that can be applied to following incremental tasks. Experimental results on multiple challenging benchmarks, i.e., HMDB51, UCF101 and Something-Something V2, demonstrate that FrameMaker can achieve better performance to recent advanced methods while consuming only 20% memory. Additionally, under the same memory consumption conditions, FrameMaker significantly outperforms existing state-of-the-arts by a convincing margin.

</details>

### S-Prompts Learning with Pre-trained Transformers: An Occam's Razor for Domain Incremental Learning.
- **链接**: [arXiv:2207.12819](https://arxiv.org/abs/2207.12819) · [代码](https://github.com/iamwangyabin/S-Prompts) · 📚 被引 34
- **作者**: Yabin Wang, Zhiwu Huang, Xiaopeng Hong
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> State-of-the-art deep neural networks are still struggling to address the catastrophic forgetting problem in continual learning. In this paper, we propose one simple paradigm (named as S-Prompting) and two concrete approaches to highly reduce the forgetting degree in one of the most typical continual learning scenarios, i.e., domain increment learning (DIL). The key idea of the paradigm is to learn prompts independently across domains with pre-trained transformers, avoiding the use of exemplars that commonly appear in conventional methods. This results in a win-win game where the prompting can achieve the best for each domain. The independent prompting across domains only requests one single cross-entropy loss for training and one simple K-NN operation as a domain identifier for inference. The learning paradigm derives an image prompt learning approach and a novel language-image prompt learning approach. Owning an excellent scalability (0.03% parameter increase per domain), the best of our approaches achieves a remarkable relative improvement (an average of about 30%) over the best of the state-of-the-art exemplar-free methods for three standard DIL tasks, and even surpasses the best of them relatively by about 6% in average when they use exemplars. Source code is available at \url{https://github.com/iamwangyabin/S-Prompts}.

</details>

### ACIL: Analytic Class-Incremental Learning with Absolute Memorization and Privacy Protection.
- **链接**: [arXiv:2205.14922](https://arxiv.org/abs/2205.14922) · 📚 被引 12
- **作者**: Huiping Zhuang, Zhenyu Weng, Hongxin Wei, Renchunzi Xie, Kar-Ann Toh, Zhiping Lin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Class-incremental learning (CIL) learns a classification model with training data of different classes arising progressively. Existing CIL either suffers from serious accuracy loss due to catastrophic forgetting, or invades data privacy by revisiting used exemplars. Inspired by linear learning formulations, we propose an analytic class-incremental learning (ACIL) with absolute memorization of past knowledge while avoiding breaching of data privacy (i.e., without storing historical data). The absolute memorization is demonstrated in the sense that class-incremental learning using ACIL given present data would give identical results to that from its joint-learning counterpart which consumes both present and historical samples. This equality is theoretically validated. Data privacy is ensured since no historical data are involved during the learning process. Empirical validations demonstrate ACIL's competitive accuracy performance with near-identical results for various incremental task settings (e.g., 5-50 phases). This also allows ACIL to outperform the state-of-the-art methods for large-phase scenarios (e.g., 25 and 50 phases).

</details>

### Margin-Based Few-Shot Class-Incremental Learning with Class-Level Overfitting Mitigation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/ae817e85f71ef86d5c9566598e185b89-Abstract-Conference.html) · 📚 被引 4
- **作者**: Yixiong Zou, Shanghang Zhang, Yuhua Li, Ruixuan Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022

### Decomposed Knowledge Distillation for Class-Incremental Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2022/hash/439bf902de1807088d8b731ca20b0777-Abstract-Conference.html) · 📚 被引 10
- **作者**: Donghyeon Baek, Youngmin Oh, Sanghoon Lee, Junghyup Lee, Bumsub Ham
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
