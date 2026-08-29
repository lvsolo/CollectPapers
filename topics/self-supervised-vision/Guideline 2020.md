# Self-supervised Vision — 2020 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Semantically-Guided Representation Learning for Self-Supervised Monocular Depth.
- **链接**: [arXiv:2002.12319](https://arxiv.org/abs/2002.12319)
- **作者**: Vitor Guizilini, Rui Hou, Jie Li, Rares Ambrus, Adrien Gaidon
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised learning is showing great promise for monocular depth estimation, using geometry as the only source of supervision. Depth networks are indeed capable of learning representations that relate visual appearance to 3D properties by implicitly leveraging category-level patterns. In this work we investigate how to leverage more directly this semantic structure to guide geometric representation learning, while remaining in the self-supervised regime. Instead of using semantic labels and proxy losses in a multi-task approach, we propose a new architecture leveraging fixed pretrained semantic segmentation networks to guide self-supervised representation learning via pixel-adaptive convolutions. Furthermore, we propose a two-stage training process to overcome a common semantic bias on dynamic objects via resampling. Our method improves upon the state of the art for self-supervised monocular depth prediction over all pixels, fine-grained details, and per semantic categories.

</details>

### Self-Supervised Learning of Appliance Usage.
- **链接**: [出版页](https://openreview.net/forum?id=B1lJzyStvS)
- **作者**: Chen-Yu Hsu, Abbas Zeitoun, Guang-He Lee, Dina Katabi, Tommi S. Jaakkola
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

### vq-wav2vec: Self-Supervised Learning of Discrete Speech Representations.
- **链接**: [arXiv:1910.05453](https://arxiv.org/abs/1910.05453)
- **作者**: Alexei Baevski, Steffen Schneider, Michael Auli
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose vq-wav2vec to learn discrete representations of audio segments through a wav2vec-style self-supervised context prediction task. The algorithm uses either a gumbel softmax or online k-means clustering to quantize the dense representations. Discretization enables the direct application of algorithms from the NLP community which require discrete inputs. Experiments show that BERT pre-training achieves a new state of the art on TIMIT phoneme classification and WSJ speech recognition.

</details>

### From Inference to Generation: End-to-end Fully Self-supervised Generation of Human Face from Speech.
- **链接**: [arXiv:2004.05830](https://arxiv.org/abs/2004.05830)
- **作者**: Hyeong-Seok Choi, Changdae Park, Kyogu Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work seeks the possibility of generating the human face from voice solely based on the audio-visual data without any human-labeled annotations. To this end, we propose a multi-modal learning framework that links the inference stage and generation stage. First, the inference networks are trained to match the speaker identity between the two different modalities. Then the trained inference networks cooperate with the generation network by giving conditional information about the voice. The proposed method exploits the recent development of GANs techniques and generates the human face directly from the speech waveform making our system fully end-to-end. We analyze the extent to which the network can naturally disentangle two latent factors that contribute to the generation of a face image - one that comes directly from a speech signal and the other that is not related to it - and explore whether the network can learn to generate natural human face image distribution by modeling these factors. Experimental results show that the proposed network can not only match the relationship between the human face and speech, but can also generate the high-quality human face sample conditioned on its speech. Finally, the correlation between the generated face and the corresponding speech is quantitatively measured to analyze the relationship between the two modalities.

</details>

### ALBERT: A Lite BERT for Self-supervised Learning of Language Representations.
- **链接**: [arXiv:1909.11942](https://arxiv.org/abs/1909.11942) · [代码](https://github.com/google-research/ALBERT) · 📚 被引 123
- **作者**: Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Increasing model size when pretraining natural language representations often results in improved performance on downstream tasks. However, at some point further model increases become harder due to GPU/TPU memory limitations and longer training times. To address these problems, we present two parameter-reduction techniques to lower memory consumption and increase the training speed of BERT. Comprehensive empirical evidence shows that our proposed methods lead to models that scale much better compared to the original BERT. We also use a self-supervised loss that focuses on modeling inter-sentence coherence, and show it consistently helps downstream tasks with multi-sentence inputs. As a result, our best model establishes new state-of-the-art results on the GLUE, RACE, and \squad benchmarks while having fewer parameters compared to BERT-large. The code and the pretrained models are available at https://github.com/google-research/ALBERT.

</details>

### Hierarchical Foresight: Self-Supervised Learning of Long-Horizon Tasks via Visual Subgoal Generation.
- **链接**: [arXiv:1909.05829](https://arxiv.org/abs/1909.05829)
- **作者**: Suraj Nair, Chelsea Finn
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video prediction models combined with planning algorithms have shown promise in enabling robots to learn to perform many vision-based tasks through only self-supervision, reaching novel goals in cluttered scenes with unseen objects. However, due to the compounding uncertainty in long horizon video prediction and poor scalability of sampling-based planning optimizers, one significant limitation of these approaches is the ability to plan over long horizons to reach distant goals. To that end, we propose a framework for subgoal generation and planning, hierarchical visual foresight (HVF), which generates subgoal images conditioned on a goal image, and uses them for planning. The subgoal images are directly optimized to decompose the task into easy to plan segments, and as a result, we observe that the method naturally identifies semantically meaningful states as subgoals. Across three out of four simulated vision-based manipulation tasks, we find that our method achieves nearly a 200% performance improvement over planning without subgoals and model-free RL approaches. Further, our experiments illustrate that our approach extends to real, cluttered visual scenes. Project page: https://sites.google.com/stanford.edu/hvf

</details>

### Neural Outlier Rejection for Self-Supervised Keypoint Learning.
- **链接**: [arXiv:1912.10615](https://arxiv.org/abs/1912.10615)
- **作者**: Jiexiong Tang, Hanme Kim, Vitor Guizilini, Sudeep Pillai, Rares Ambrus
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Identifying salient points in images is a crucial component for visual odometry, Structure-from-Motion or SLAM algorithms. Recently, several learned keypoint methods have demonstrated compelling performance on challenging benchmarks. However, generating consistent and accurate training data for interest-point detection in natural images still remains challenging, especially for human annotators. We introduce IO-Net (i.e. InlierOutlierNet), a novel proxy task for the self-supervision of keypoint detection, description and matching. By making the sampling of inlier-outlier sets from point-pair correspondences fully differentiable within the keypoint learning framework, we show that are able to simultaneously self-supervise keypoint description and improve keypoint matching. Second, we introduce KeyPointNet, a keypoint-network architecture that is especially amenable to robust keypoint detection and description. We design the network to allow local keypoint aggregation to avoid artifacts due to spatial discretizations commonly used for this task, and we improve fine-grained keypoint descriptor performance by taking advantage of efficient sub-pixel convolutions to upsample the descriptor feature-maps to a higher operating resolution. Through extensive experiments and ablative analysis, we show that the proposed self-supervised keypoint learning method greatly improves the quality of feature matching and homography estimation on challenging benchmarks over the state-of-the-art.

</details>

### Contrastive Learning of Structured World Models.
- **链接**: [arXiv:1911.12247](https://arxiv.org/abs/1911.12247)
- **作者**: Thomas N. Kipf, Elise van der Pol, Max Welling
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A structured understanding of our world in terms of objects, relations, and hierarchies is an important component of human cognition. Learning such a structured world model from raw sensory data remains a challenge. As a step towards this goal, we introduce Contrastively-trained Structured World Models (C-SWMs). C-SWMs utilize a contrastive approach for representation learning in environments with compositional structure. We structure each state embedding as a set of object representations and their relations, modeled by a graph neural network. This allows objects to be discovered from raw pixel observations without direct supervision as part of the learning process. We evaluate C-SWMs on compositional environments involving multiple interacting objects that can be manipulated independently by an agent, simple Atari games, and a multi-object physics simulation. Our experiments demonstrate that C-SWMs can overcome limitations of models based on pixel reconstruction and outperform typical representatives of this model class in highly structured environments, while learning interpretable object-based representations.

</details>
