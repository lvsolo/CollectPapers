# Video Understanding — 2023 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### EgoDistill: Egocentric Head Motion Distillation for Efficient Video Understanding.
- **链接**: [arXiv:2301.02217](https://arxiv.org/abs/2301.02217) · 📚 被引 8
- **作者**: Shuhan Tan, Tushar Nagarajan, Kristen Grauman
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advances in egocentric video understanding models are promising, but their heavy computational expense is a barrier for many real-world applications. To address this challenge, we propose EgoDistill, a distillation-based approach that learns to reconstruct heavy egocentric video clip features by combining the semantics from a sparse set of video frames with the head motion from lightweight IMU readings. We further devise a novel self-supervised training strategy for IMU feature learning. Our method leads to significant improvements in efficiency, requiring 200x fewer GFLOPs than equivalent video models. We demonstrate its effectiveness on the Ego4D and EPICKitchens datasets, where our method outperforms state-of-the-art efficient video understanding methods.

</details>

### EPIC Fields: Marrying 3D Geometry and Video Understanding.
- **链接**: [arXiv:2306.08731](https://arxiv.org/abs/2306.08731)
- **作者**: Vadim Tschernezki, Ahmad Darkhalil, Zhifan Zhu, David Fouhey, Iro Laina, Diane Larlus et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural rendering is fuelling a unification of learning, 3D geometry and video understanding that has been waiting for more than two decades. Progress, however, is still hampered by a lack of suitable datasets and benchmarks. To address this gap, we introduce EPIC Fields, an augmentation of EPIC-KITCHENS with 3D camera information. Like other datasets for neural rendering, EPIC Fields removes the complex and expensive step of reconstructing cameras using photogrammetry, and allows researchers to focus on modelling problems. We illustrate the challenge of photogrammetry in egocentric videos of dynamic actions and propose innovations to address them. Compared to other neural rendering datasets, EPIC Fields is better tailored to video understanding because it is paired with labelled action segments and the recent VISOR segment annotations. To further motivate the community, we also evaluate two benchmark tasks in neural rendering and segmenting dynamic objects, with strong baselines that showcase what is not possible today. We also highlight the advantage of geometry in semi-supervised video object segmentations on the VISOR annotations. EPIC Fields reconstructs 96% of videos in EPICKITCHENS, registering 19M frames in 99 hours recorded in 45 kitchens.

</details>

### Revealing the unseen: Benchmarking video action recognition under occlusion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/cef53466b62aebbcf8aa2210a89b33a1-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 4
- **作者**: Shresth Grover, Vibhav Vineet, Yogesh S. Rawat
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CAST: Cross-Attention in Space and Time for Video Action Recognition.
- **链接**: [arXiv:2311.18825](https://arxiv.org/abs/2311.18825) · 📚 被引 6
- **作者**: Dongho Lee, Jongseo Lee, Jinwoo Choi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recognizing human actions in videos requires spatial and temporal understanding. Most existing action recognition models lack a balanced spatio-temporal understanding of videos. In this work, we propose a novel two-stream architecture, called Cross-Attention in Space and Time (CAST), that achieves a balanced spatio-temporal understanding of videos using only RGB input. Our proposed bottleneck cross-attention mechanism enables the spatial and temporal expert models to exchange information and make synergistic predictions, leading to improved performance. We validate the proposed method with extensive experiments on public benchmarks with different characteristics: EPIC-KITCHENS-100, Something-Something-V2, and Kinetics-400. Our method consistently shows favorable performance across these datasets, while the performance of existing methods fluctuates depending on the dataset characteristics.

</details>

### Unsupervised Video Domain Adaptation for Action Recognition: A Disentanglement Perspective.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/39235c56aef13fb05a6adc95eb9d8d66-Abstract-Conference.html) · 📚 被引 3
- **作者**: Pengfei Wei, Lingdong Kong, Xinghua Qu, Yi Ren, Zhiqiang Xu, Jing Jiang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023
