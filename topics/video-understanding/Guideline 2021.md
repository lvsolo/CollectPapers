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

> We present a self-supervised Contrastive Video Representation Learning (CVRL) method to learn spatiotemporal visual representations from unlabeled videos. Our representations are learned using a contrastive loss, where two augmented clips from the same short video are pulled together in the embedding space, while clips from different videos are pushed away. We study what makes for good data augmentations for video self-supervised learning and find that both spatial and temporal information are crucial. We carefully design data augmentations involving spatial and temporal cues. Concretely, we propose a temporally consistent spatial augmentation method to impose strong spatial augmentations on each frame of the video while maintaining the temporal consistency across frames. We also propose a sampling-based temporal augmentation method to avoid overly enforcing invariance on clips that are distant in time. On Kinetics-600, a linear classifier trained on the representations learned by CVRL achieves 70.4% top-1 accuracy with a 3D-ResNet-50 (R3D-50) backbone, outperforming ImageNet supervised pre-training by 15.7% and SimCLR unsupervised pre-training by 18.8% using the same inflated R3D-50. The performance of CVRL can be further improved to 72.9% with a larger R3D-152 (2x filters) backbone, significantly closing the gap between unsupervised and supervised video representation learning. Our code and models will be available at https://github.com/tensorflow/models/tree/master/official/.

</details>

### Visual Semantic Role Labeling for Video Understanding.
- **链接**: [arXiv:2104.00990](https://arxiv.org/abs/2104.00990) · 📚 被引 44
- **作者**: Arka Sadhu, Tanmay Gupta, Mark Yatskar, Ram Nevatia, Aniruddha Kembhavi
- **🏷️ 机构**: University of Southern California, PRIOR @ Allen Institute for AI, University of Pennsylvania
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a new framework for understanding and representing related salient events in a video using visual semantic role labeling. We represent videos as a set of related events, wherein each event consists of a verb and multiple entities that fulfill various roles relevant to that event. To study the challenging task of semantic role labeling in videos or VidSRL, we introduce the VidSitu benchmark, a large-scale video understanding data source with $29K$ $10$-second movie clips richly annotated with a verb and semantic-roles every $2$ seconds. Entities are co-referenced across events within a movie clip and events are connected to each other via event-event relations. Clips in VidSitu are drawn from a large collection of movies (${\sim}3K$) and have been chosen to be both complex (${\sim}4.2$ unique verbs within a video) as well as diverse (${\sim}200$ verbs have more than $100$ annotations each). We provide a comprehensive analysis of the dataset in comparison to other publicly available video understanding benchmarks, several illustrative baselines and evaluate a range of standard video recognition models. Our code and dataset is available at vidsitu.org.

</details>

### Towards Long-Form Video Understanding.
- **链接**: [arXiv:2106.11310](https://arxiv.org/abs/2106.11310) · 📚 被引 120
- **作者**: Chao-Yuan Wu, Philipp Krähenbühl
- **🏷️ 机构**: UT Austin
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Our world offers a never-ending stream of visual stimuli, yet today's vision systems only accurately recognize patterns within a few seconds. These systems understand the present, but fail to contextualize it in past or future events. In this paper, we study long-form video understanding. We introduce a framework for modeling long-form videos and develop evaluation protocols on large-scale datasets. We show that existing state-of-the-art short-term models are limited for long-form tasks. A novel object-centric transformer-based video recognition architecture performs significantly better on 7 diverse tasks. It also outperforms comparable state-of-the-art on the AVA dataset.

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

> Not all video frames are equally informative for recognizing an action. It is computationally infeasible to train deep networks on all video frames when actions develop over hundreds of frames. A common heuristic is uniformly sampling a small number of video frames and using these to recognize the action. Instead, here we propose full video action recognition and consider all video frames. To make this computational tractable, we first cluster all frame activations along the temporal dimension based on their similarity with respect to the classification task, and then temporally aggregate the frames in the clusters into a smaller number of representations. Our method is end-to-end trainable and computationally efficient as it relies on temporally localized clustering in combination with fast Hamming distances in feature space. We evaluate on UCF101, HMDB51, Breakfast, and Something-Something V1 and V2, where we compare favorably to existing heuristic frame sampling methods.

</details>

## 跨领域论文（完整笔记在其他领域）

- DeepVideoMVS: Multi-View Stereo on Video With Recurrent Spatio-Temporal Fusion. → [multi-camera-perception](../multi-camera-perception/Guideline%202021.md)
- Self-Supervised Video Representation Learning by Context and Motion Decoupling. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- Removing the Background by Adding the Background: Towards Background Robust Self-Supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
- VideoMoCo: Contrastive Video Representation Learning With Temporally Adversarial Examples. → [self-supervised-vision](../self-supervised-vision/Guideline%202021.md)
