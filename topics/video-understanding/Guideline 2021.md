# Video Understanding — 2021 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Env-QA: A Video Question Answering Benchmark for Comprehensive Understanding of Dynamic Environments.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00170) · 📚 被引 21
- **作者**: Difei Gao, Ruiping Wang, Ziyi Bai, Xilin Chen
- **🏷️ 机构**: Institute of Computing Technology, CAS,Key Laboratory of Intelligent Information Processing of Chinese Academy of Sciences (CAS),Beijing,China,100190
- **会议**: ICCV 2021

### Long Short View Feature Decomposition via Contrastive Video Representation Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00911) · 📚 被引 25
- **作者**: Nadine Behrmann, Mohsen Fayyaz, Juergen Gall, Mehdi Noroozi
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, University of Bonn
- **会议**: ICCV 2021

### Time-Equivariant Contrastive Video Representation Learning.
- **链接**: [arXiv:2112.03624](https://arxiv.org/abs/2112.03624) · 📚 被引 43
- **作者**: Simon Jenni, Hailin Jin
- **🏷️ 机构**: Adobe Research
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel self-supervised contrastive learning method to learn representations from unlabelled videos. Existing approaches ignore the specifics of input distortions, e.g., by learning invariance to temporal transformations. Instead, we argue that video representation should preserve video dynamics and reflect temporal manipulations of the input. Therefore, we exploit novel constraints to build representations that are equivariant to temporal transformations and better capture video dynamics. In our method, relative temporal transformations between augmented clips of a video are encoded in a vector and contrasted with other transformation vectors. To support temporal equivariance learning, we additionally propose the self-supervised classification of two clips of a video into 1. overlapping 2. ordered, or 3. unordered. Our experiments show that time-equivariant representations achieve state-of-the-art results in video retrieval and action recognition benchmarks on UCF101, HMDB51, and Diving48.

</details>

### Motion-Focused Contrastive Learning of Video Representations*.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00211) · 📚 被引 30
- **作者**: Rui Li, Yiheng Zhang, Zhaofan Qiu, Ting Yao, Dong Liu, Tao Mei
- **🏷️ 机构**: University of Science and Technology of China,Hefei,China, JD AI Research,Beijing,China
- **会议**: ICCV 2021

### Unified Graph Structured Models for Video Understanding.
- **链接**: [arXiv:2103.15662](https://arxiv.org/abs/2103.15662) · 📚 被引 40
- **作者**: Anurag Arnab, Chen Sun, Cordelia Schmid
- **🏷️ 机构**: Google Research
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate video understanding involves reasoning about the relationships between actors, objects and their environment, often over long temporal intervals. In this paper, we propose a message passing graph neural network that explicitly models these spatio-temporal relations and can use explicit representations of objects, when supervision is available, and implicit representations otherwise. Our formulation generalises previous structured models for video understanding, and allows us to study how different design choices in graph structure and representation affect the model's performance. We demonstrate our method on two different tasks requiring relational reasoning in videos -- spatio-temporal action detection on AVA and UCF101-24, and video scene graph classification on the recent Action Genome dataset -- and achieve state-of-the-art results on all three datasets. Furthermore, we show quantitatively and qualitatively how our method is able to more effectively model relationships between relevant entities in the scene.

</details>

### Video Pose Distillation for Few-Shot, Fine-Grained Sports Action Recognition.
- **链接**: [arXiv:2109.01305](https://arxiv.org/abs/2109.01305) · 📚 被引 48
- **作者**: James Hong, Matthew Fisher, Michaël Gharbi, Kayvon Fatahalian
- **🏷️ 机构**: Stanford University, Adobe Research
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human pose is a useful feature for fine-grained sports action understanding. However, pose estimators are often unreliable when run on sports video due to domain shift and factors such as motion blur and occlusions. This leads to poor accuracy when downstream tasks, such as action recognition, depend on pose. End-to-end learning circumvents pose, but requires more labels to generalize. We introduce Video Pose Distillation (VPD), a weakly-supervised technique to learn features for new video domains, such as individual sports that challenge pose estimation. Under VPD, a student network learns to extract robust pose features from RGB frames in the sports video, such that, whenever pose is considered reliable, the features match the output of a pretrained teacher pose detector. Our strategy retains the best of both pose and end-to-end worlds, exploiting the rich visual patterns in raw video frames, while learning features that agree with the athletes' pose and motion in the target video domain to avoid over-fitting to patterns unrelated to athletes' motion. VPD features improve performance on few-shot, fine-grained action recognition, retrieval, and detection tasks in four real-world sports video datasets, without requiring additional ground-truth pose annotations.

</details>

### Learning Self-Similarity in Space and Time as Generalized Motion for Video Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.01282) · 📚 被引 41
- **作者**: Heeseung Kwon, Manjin Kim, Suha Kwak, Minsu Cho
- **🏷️ 机构**: Pohang University of Science and Technology (POSTECH),South Korea
- **会议**: ICCV 2021

### MGSampler: An Explainable Sampling Strategy for Video Action Recognition.
- **链接**: [arXiv:2104.09952](https://arxiv.org/abs/2104.09952) · 📚 被引 74
- **作者**: Yuan Zhi, Zhan Tong, Limin Wang, Gangshan Wu
- **🏷️ 机构**: Nanjing University,State Key Laboratory for Novel Software Technology,China
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Frame sampling is a fundamental problem in video action recognition due to the essential redundancy in time and limited computation resources. The existing sampling strategy often employs a fixed frame selection and lacks the flexibility to deal with complex variations in videos. In this paper, we present a simple, sparse, and explainable frame sampler, termed as Motion-Guided Sampler (MGSampler). Our basic motivation is that motion is an important and universal signal that can drive us to adaptively select frames from videos. Accordingly, we propose two important properties in our MGSampler design: motion sensitive and motion uniform. First, we present two different motion representations to enable us to efficiently distinguish the motion-salient frames from the background. Then, we devise a motion-uniform sampling strategy based on the cumulative motion distribution to ensure the sampled frames evenly cover all the important segments with high motion salience. Our MGSampler yields a new principled and holistic sampling scheme, that could be incorporated into any existing video architecture. Experiments on five benchmarks demonstrate the effectiveness of our MGSampler over the previous fixed sampling strategies, and its generalization power across different backbones, video models, and datasets.

</details>

### TeachText: CrossModal Generalized Distillation for Text-Video Retrieval.
- **链接**: [arXiv:2104.08271](https://arxiv.org/abs/2104.08271) · 📚 被引 3
- **作者**: Ioana Croitoru, Simion-Vlad Bogolin, Marius Leordeanu, Hailin Jin, Andrew Zisserman, Samuel Albanie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, considerable progress on the task of text-video retrieval has been achieved by leveraging large-scale pretraining on visual and audio datasets to construct powerful video encoders. By contrast, despite the natural symmetry, the design of effective algorithms for exploiting large-scale language pretraining remains under-explored. In this work, we are the first to investigate the design of such algorithms and propose a novel generalized distillation method, TeachText, which leverages complementary cues from multiple text encoders to provide an enhanced supervisory signal to the retrieval model. Moreover, we extend our method to video side modalities and show that we can effectively reduce the number of used modalities at test time without compromising performance. Our approach advances the state of the art on several video retrieval benchmarks by a significant margin and adds no computational overhead at test time. Last but not least, we show an effective application of our method for eliminating noise from retrieval datasets. Code and data can be found at https://www.robots.ox.ac.uk/~vgg/research/teachtext/.

</details>

## 跨领域论文（完整笔记在其他领域）

- ASCNet: Self-supervised Video Representation Learning with Appearance-Speed Consistency. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Self-Supervised Video Representation Learning with Meta-Contrastive Network. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Enhancing Self-supervised Video Representation Learning via Multi-level Feature Optimization. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- CrossCLR: Cross-modal Contrastive Learning For Multi-modal Video Representations. → [multimodal](../multimodal/Guideline%202021.md)
- Multi-Modal Multi-Action Video Recognition. → [multimodal](../multimodal/Guideline%202021.md)
