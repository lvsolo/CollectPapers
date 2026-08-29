# Video Understanding — 2021 Guideline

> 领域: 视频理解（动作识别、时序动作、视频大模型）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Spatiotemporal Contrastive Video Representation Learning.
- **链接**: [arXiv:2008.03800](https://arxiv.org/abs/2008.03800) · [代码](https://github.com/tensorflow/models)
- **作者**: Rui Qian, Tianjian Meng, Boqing Gong, Ming-Hsuan Yang, Huisheng Wang, Serge J. Belongie et al.
- **🏷️ 机构**: UC Merced
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce a novel self-supervised contrastive learning method to learn representations from unlabelled videos. Existing approaches ignore the specifics of input distortions, e.g., by learning invariance to temporal transformations. Instead, we argue that video representation should preserve video dynamics and reflect temporal manipulations of the input. Therefore, we exploit novel constraints to build representations that are equivariant to temporal transformations and better capture video dynamics. In our method, relative temporal transformations between augmented clips of a video are encoded in a vector and contrasted with other transformation vectors. To support temporal equivariance learning, we additionally propose the self-supervised classification of two clips of a video into 1. overlapping 2. ordered, or 3. unordered. Our experiments show that time-equivariant representations achieve state-of-the-art results in video retrieval and action recognition benchmarks on UCF101, HMDB51, and Diving48.

</details>

### Visual Semantic Role Labeling for Video Understanding.
- **链接**: [arXiv:2104.00990](https://arxiv.org/abs/2104.00990) · 📚 被引 44
- **作者**: Arka Sadhu, Tanmay Gupta, Mark Yatskar, Ram Nevatia, Aniruddha Kembhavi
- **🏷️ 机构**: University of Southern California, PRIOR @ Allen Institute for AI, University of Pennsylvania
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Accurate video understanding involves reasoning about the relationships between actors, objects and their environment, often over long temporal intervals. In this paper, we propose a message passing graph neural network that explicitly models these spatio-temporal relations and can use explicit representations of objects, when supervision is available, and implicit representations otherwise. Our formulation generalises previous structured models for video understanding, and allows us to study how different design choices in graph structure and representation affect the model's performance. We demonstrate our method on two different tasks requiring relational reasoning in videos -- spatio-temporal action detection on AVA and UCF101-24, and video scene graph classification on the recent Action Genome dataset -- and achieve state-of-the-art results on all three datasets. Furthermore, we show quantitatively and qualitatively how our method is able to more effectively model relationships between relevant entities in the scene.

</details>

### Towards Long-Form Video Understanding.
- **链接**: [arXiv:2106.11310](https://arxiv.org/abs/2106.11310) · 📚 被引 120
- **作者**: Chao-Yuan Wu, Philipp Krähenbühl
- **🏷️ 机构**: UT Austin
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human pose is a useful feature for fine-grained sports action understanding. However, pose estimators are often unreliable when run on sports video due to domain shift and factors such as motion blur and occlusions. This leads to poor accuracy when downstream tasks, such as action recognition, depend on pose. End-to-end learning circumvents pose, but requires more labels to generalize. We introduce Video Pose Distillation (VPD), a weakly-supervised technique to learn features for new video domains, such as individual sports that challenge pose estimation. Under VPD, a student network learns to extract robust pose features from RGB frames in the sports video, such that, whenever pose is considered reliable, the features match the output of a pretrained teacher pose detector. Our strategy retains the best of both pose and end-to-end worlds, exploiting the rich visual patterns in raw video frames, while learning features that agree with the athletes' pose and motion in the target video domain to avoid over-fitting to patterns unrelated to athletes' motion. VPD features improve performance on few-shot, fine-grained action recognition, retrieval, and detection tasks in four real-world sports video datasets, without requiring additional ground-truth pose annotations.

</details>

### Temporal Query Networks for Fine-Grained Video Understanding.
- **链接**: [arXiv:2104.09496](https://arxiv.org/abs/2104.09496) · 📚 被引 88
- **作者**: Chuhan Zhang, Ankush Gupta, Andrew Zisserman
- **🏷️ 机构**: University of Oxford, DeepMind,London
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our objective in this work is fine-grained classification of actions in untrimmed videos, where the actions may be temporally extended or may span only a few frames of the video. We cast this into a query-response mechanism, where each query addresses a particular question, and has its own response label set. We make the following four contributions: (I) We propose a new model - a Temporal Query Network - which enables the query-response functionality, and a structural understanding of fine-grained actions. It attends to relevant segments for each query with a temporal attention mechanism, and can be trained using only the labels for each query. (ii) We propose a new way - stochastic feature bank update - to train a network on videos of various lengths with the dense sampling required to respond to fine-grained queries. (iii) We compare the TQN to other architectures and text supervision methods, and analyze their pros and cons. Finally, (iv) we evaluate the method extensively on the FineGym and Diving48 benchmarks for fine-grained action classification and surpass the state-of-the-art using only RGB features.

</details>

### No Frame Left Behind: Full Video Action Recognition.
- **链接**: [arXiv:2103.15395](https://arxiv.org/abs/2103.15395) · 📚 被引 41
- **作者**: Xin Liu, Silvia L. Pintea, Fatemeh Karimi Nejadasl, Olaf Booij, Jan C. van Gemert
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Convolution has been arguably the most important feature transform for modern neural networks, leading to the advance of deep learning. Recent emergence of Transformer networks, which replace convolution layers with self-attention blocks, has revealed the limitation of stationary convolution kernels and opened the door to the era of dynamic feature transforms. The existing dynamic transforms, including self-attention, however, are all limited for video understanding where correspondence relations in space and time, i.e., motion information, are crucial for effective representation. In this work, we introduce a relational feature transform, dubbed the relational self-attention (RSA), that leverages rich structures of spatio-temporal relations in videos by dynamically generating relational kernels and aggregating relational contexts. Our experiments and ablation studies show that the RSA network substantially outperforms convolution and self-attention counterparts, achieving the state of the art on the standard motion-centric benchmarks for video action recognition, such as Something-Something-V1 & V2, Diving48, and FineGym.

</details>

## 跨领域论文（完整笔记在其他领域）

- DeepVideoMVS: Multi-View Stereo on Video With Recurrent Spatio-Temporal Fusion. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-Supervised Video Representation Learning by Context and Motion Decoupling. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Removing the Background by Adding the Background: Towards Background Robust Self-Supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- VideoMoCo: Contrastive Video Representation Learning With Temporally Adversarial Examples. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
