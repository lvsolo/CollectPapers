# Video Understanding — 2025 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### TUMTraf VideoQA: Dataset and Benchmark for Unified Spatio-Temporal Video Understanding in Traffic Scenes.
- **链接**: [出版页](https://proceedings.mlr.press/v267/zhou25g.html)
- **作者**: Xingcheng Zhou, Konstantinos Larintzakis, Hao Guo, Walter Zimmer, Mingyu Liu, Hu Cao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human vision is dynamic and continuous. However, in video understanding with multimodal large language models (LLMs), existing methods primarily rely on static features extracted from images sampled at a fixed low frame rate of frame-per-second (FPS) $\leqslant$2, leading to critical visual information loss. In this paper, we introduce F-16, the first multimodal LLM designed for high-frame-rate video understanding. By increasing the frame rate to 16 FPS and compressing visual tokens within each 1-second clip, F-16 efficiently captures dynamic visual features while preserving key semantic information. Experimental results demonstrate that higher frame rates considerably enhance video understanding across multiple benchmarks, providing a new approach to improving video LLMs beyond scaling model size or training data. F-16 achieves state-of-the-art performance among 7-billion-parameter video LLMs on both general and fine-grained video understanding benchmarks, such as Video-MME and TemporalBench. Furthermore, F-16 excels in complex spatiotemporal tasks, including high-speed sports analysis (\textit{e.g.}, basketball, football, gymnastics, and diving), outperforming SOTA proprietary visual models like GPT-4o and Gemini-1.5-pro. Additionally, we introduce a novel decoding method for F-16 that enables highly efficient low-frame-rate inference without requiring model retraining. We will release the source code, model checkpoints, and data at \href{https://github.com/bytedance/F-16}{https://github.com/bytedance/F-16}.

</details>

### Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation.
- **链接**: [arXiv:2504.02438](https://arxiv.org/abs/2504.02438) · [代码](https://github.com/steven-ccq/ViLAMP)
- **作者**: Chuanqi Cheng, Jian Guan, Wei Wu, Rui Yan
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-form video processing fundamentally challenges vision-language models (VLMs) due to the high computational costs of handling extended temporal sequences. Existing token pruning and feature merging methods often sacrifice critical temporal dependencies or dilute semantic information. We introduce differential distillation, a principled approach that systematically preserves task-relevant information while suppressing redundancy. Based on this principle, we develop ViLAMP, a hierarchical video-language model that processes hour-long videos at "mixed precision" through two key mechanisms: (1) differential keyframe selection that maximizes query relevance while maintaining temporal distinctiveness at the frame level and (2) differential feature merging that preserves query-salient features in non-keyframes at the patch level. Hence, ViLAMP retains full information in keyframes while reducing non-keyframes to their most salient features, resembling mixed-precision training. Extensive experiments demonstrate ViLAMP's superior performance across four video understanding benchmarks, particularly on long-form content. Notably, ViLAMP can process ultra-long videos (up to 10K frames) on a single NVIDIA A100 GPU, achieving substantial computational efficiency while maintaining state-of-the-art performance. Code and model are available at https://github.com/steven-ccq/ViLAMP.

</details>

## 跨领域论文（完整笔记在其他领域）

- LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding. → [network-pruning](../network-pruning/Guideline%202025.md)
