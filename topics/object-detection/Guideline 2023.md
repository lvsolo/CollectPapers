# Object Detection — 2023 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 26 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Rank-DETR for High Quality Object Detection.
- **链接**: [arXiv:2310.08854](https://arxiv.org/abs/2310.08854) · [代码](https://github.com/LeapLabTHU/Rank-DETR) · 📚 被引 17
- **作者**: Yifan Pu, Weicong Liang, Yiduo Hao, Yuhui Yuan, Yukang Yang, Chao Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modern detection transformers (DETRs) use a set of object queries to predict a list of bounding boxes, sort them by their classification confidence scores, and select the top-ranked predictions as the final detection results for the given input image. A highly performant object detector requires accurate ranking for the bounding box predictions. For DETR-based detectors, the top-ranked bounding boxes suffer from less accurate localization quality due to the misalignment between classification scores and localization accuracy, thus impeding the construction of high-quality detectors. In this work, we introduce a simple and highly performant DETR-based object detector by proposing a series of rank-oriented designs, combinedly called Rank-DETR. Our key contributions include: (i) a rank-oriented architecture design that can prompt positive predictions and suppress the negative ones to ensure lower false positive rates, as well as (ii) a rank-oriented loss function and matching cost design that prioritizes predictions of more accurate localization accuracy during ranking to boost the AP under high IoU thresholds. We apply our method to improve the recent SOTA methods (e.g., H-DETR and DINO-DETR) and report strong COCO object detection results when using different backbones such as ResNet-$50$, Swin-T, and Swin-L, demonstrating the effectiveness of our approach. Code is available at \url{https://github.com/LeapLabTHU/Rank-DETR}.

</details>

### Described Object Detection: Liberating Object Detection with Flexible Expressions.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/f9fd24fd32eccc14cd3ecd3716a1cbf8-Abstract-Conference.html) · 📚 被引 3
- **作者**: Chi Xie, Zhao Zhang, Yixuan Wu, Feng Zhu, Rui Zhao, Shuang Liang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### PrObeD: Proactive Object Detection Wrapper.
- **链接**: [arXiv:2310.18788](https://arxiv.org/abs/2310.18788) · [代码](https://github.com/vishal3477/Proactive-Object-Detection)
- **作者**: Vishal Asnani, Abhinav Kumar, Suya You, Xiaoming Liu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous research in $2D$ object detection focuses on various tasks, including detecting objects in generic and camouflaged images. These works are regarded as passive works for object detection as they take the input image as is. However, convergence to global minima is not guaranteed to be optimal in neural networks; therefore, we argue that the trained weights in the object detector are not optimal. To rectify this problem, we propose a wrapper based on proactive schemes, PrObeD, which enhances the performance of these object detectors by learning a signal. PrObeD consists of an encoder-decoder architecture, where the encoder network generates an image-dependent signal termed templates to encrypt the input images, and the decoder recovers this template from the encrypted images. We propose that learning the optimum template results in an object detector with an improved detection performance. The template acts as a mask to the input images to highlight semantics useful for the object detector. Finetuning the object detector with these encrypted images enhances the detection performance for both generic and camouflaged. Our experiments on MS-COCO, CAMO, COD$10$K, and NC$4$K datasets show improvement over different detectors after applying PrObeD. Our models/codes are available at https://github.com/vishal3477/Proactive-Object-Detection.

</details>

### HASSOD: Hierarchical Adaptive Self-Supervised Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b9ecf4d84999a61783c360c3782e801e-Abstract-Conference.html)
- **作者**: Shengcao Cao, Dhiraj Joshi, Liangyan Gui, Yu-Xiong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Navigating Data Heterogeneity in Federated Learning: A Semi-Supervised Approach for Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/066e4dbfeccb5dc2851acd5eca584937-Abstract-Conference.html) · 📚 被引 7
- **作者**: Taehyeon Kim, Eric Lin, Junu Lee, Christian Lau, Vaikkunth Mugunthan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### DVSOD: RGB-D Video Salient Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/1b88e65f737256d437e56764d39ba06d-Abstract-Datasets_and_Benchmarks.html) · 📚 被引 2
- **作者**: Jingjing Li, Wei Ji, Size Wang, Wenbo Li, Li Cheng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### CoDet: Co-occurrence Guided Region-Word Alignment for Open-Vocabulary Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e10a6a906ef323efaf708f76cf3c1d1e-Abstract-Conference.html)
- **作者**: Chuofan Ma, Yi Jiang, Xin Wen, Zehuan Yuan, Xiaojuan Qi
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Learning from Rich Semantics and Coarse Locations for Long-tailed Object Detection.
- **链接**: [arXiv:2310.12152](https://arxiv.org/abs/2310.12152) · [代码](https://github.com/MengLcool/RichSem) · 📚 被引 0
- **作者**: Lingchen Meng, Xiyang Dai, Jianwei Yang, Dongdong Chen, Yinpeng Chen, Mengchen Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Long-tailed object detection (LTOD) aims to handle the extreme data imbalance in real-world datasets, where many tail classes have scarce instances. One popular strategy is to explore extra data with image-level labels, yet it produces limited results due to (1) semantic ambiguity -- an image-level label only captures a salient part of the image, ignoring the remaining rich semantics within the image; and (2) location sensitivity -- the label highly depends on the locations and crops of the original image, which may change after data transformations like random cropping. To remedy this, we propose RichSem, a simple but effective method, which is robust to learn rich semantics from coarse locations without the need of accurate bounding boxes. RichSem leverages rich semantics from images, which are then served as additional soft supervision for training detectors. Specifically, we add a semantic branch to our detector to learn these soft semantics and enhance feature representations for long-tailed object detection. The semantic branch is only used for training and is removed during inference. RichSem achieves consistent improvements on both overall and rare-category of LVIS under different backbones and detectors. Our method achieves state-of-the-art performance without requiring complex training and testing procedures. Moreover, we show the effectiveness of our method on other long-tailed datasets with additional experiments. Code is available at \url{https://github.com/MengLcool/RichSem}.

</details>

### Scaling Open-Vocabulary Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e6d58fc68c0f3c36ae6e0e64478a69c0-Abstract-Conference.html)
- **作者**: Matthias Minderer, Alexey A. Gritsenko, Neil Houlsby
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Django: Detecting Trojans in Object Detection Models via Gaussian Focus Calibration.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a102d6cb996be3482c059c1e18bbe523-Abstract-Conference.html) · 📚 被引 4
- **作者**: Guangyu Shen, Siyuan Cheng, Guanhong Tao, Kaiyuan Zhang, Yingqi Liu, Shengwei An et al.
- **🏷️ 机构**: MEGVII
- **会议**: NeurIPS 2023

### Prototypical Variational Autoencoder for 3D Few-shot Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/076a93fd42aa85f5ccee921a01d77dd5-Abstract-Conference.html) · 📚 被引 0
- **作者**: Weiliang Tang, Biqi Yang, Xianzhi Li, Yun-Hui Liu, Pheng-Ann Heng, Chi-Wing Fu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### H2RBox-v2: Incorporating Symmetry for Boosting Horizontal Box Supervised Oriented Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/b9603de9e49d0838e53b6c9cf9d06556-Abstract-Conference.html) · 📚 被引 11
- **作者**: Yi Yu, Xue Yang, Qingyun Li, Yue Zhou, Feipeng Da, Junchi Yan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- Multi-modal Queried Object Detection in the Wild. → [multimodal](../multimodal/Guideline%202023.md)
- RangePerception: Taming LiDAR Range View for Efficient and Accurate 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- CoDA: Collaborative Novel Box Discovery and Cross-modal Alignment for Open-vocabulary 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Depth-discriminative Metric Learning for Monocular 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Diffusion-SS3D: Diffusion Model for Semi-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Query-based Temporal Fusion with Explicit Motion for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Leveraging Vision-Centric Multi-Modal Expertise for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- STXD: Structural and Temporal Cross-Modal Distillation for Multi-View 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- M2SODAI: Multi-Modal Maritime Object Detection Dataset With RGB and Hyperspectral Image Sensors. → [multimodal](../multimodal/Guideline%202023.md)
- MonoUNI: A Unified Vehicle and Infrastructure-side Monocular 3D Object Detection Network with Sufficient Depth Clues. → [3d-detection](../3d-detection/Guideline%202023.md)
- CluB: Cluster Meets BEV for LiDAR-Based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Flow-Based Feature Fusion for Vehicle-Infrastructure Cooperative 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- HEDNet: A Hierarchical Encoder-Decoder Network for 3D Object Detection in Point Clouds. → [3d-detection](../3d-detection/Guideline%202023.md)
- Unleash the Potential of Image Branch for Cross-modal 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
