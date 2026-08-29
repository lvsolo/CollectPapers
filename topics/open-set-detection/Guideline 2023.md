# Open-set Detection — 2023 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 21 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-Vocabulary Video Question Answering: A New Benchmark for Evaluating the Generalizability of Video Question Answering Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00288)
- **作者**: Dohwan Ko, Ji Soo Lee, Miso Choi, Jaewon Chu, Jihwan Park, Hyunwoo J. Kim
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Tracking by 3D Model Estimation of Unknown Objects in Videos.
- **链接**: [arXiv:2304.06419](https://arxiv.org/abs/2304.06419) · 📚 被引 2
- **作者**: Denys Rozumnyi, Jirí Matas, Marc Pollefeys, Vittorio Ferrari, Martin R. Oswald
- **🏷️ 机构**: ETH Zurich,Department of Computer Science, Czech Technical University in Prague, Google Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most model-free visual object tracking methods formulate the tracking task as object location estimation given by a 2D segmentation or a bounding box in each video frame. We argue that this representation is limited and instead propose to guide and improve 2D tracking with an explicit object representation, namely the textured 3D shape and 6DoF pose in each video frame. Our representation tackles a complex long-term dense correspondence problem between all 3D points on the object for all video frames, including frames where some points are invisible. To achieve that, the estimation is driven by re-rendering the input video frames as well as possible through differentiable rendering, which has not been used for tracking before. The proposed optimization minimizes a novel loss function to estimate the best 3D shape, texture, and 6DoF pose. We improve the state-of-the-art in 2D segmentation tracking on three different datasets with mostly rigid objects.

</details>

### Open-vocabulary Panoptic Segmentation with Embedding Modulation.
- **链接**: [arXiv:2303.11324](https://arxiv.org/abs/2303.11324) · 📚 被引 26
- **作者**: Xi Chen, Shuang Li, Ser-Nam Lim, Antonio Torralba, Hengshuang Zhao
- **🏷️ 机构**: The University of Hong Kong, Massachusetts Institute of Technology, Meta AI
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary image segmentation is attracting increasing attention due to its critical applications in the real world. Traditional closed-vocabulary segmentation methods are not able to characterize novel objects, whereas several recent open-vocabulary attempts obtain unsatisfactory results, i.e., notable performance reduction on the closed vocabulary and massive demand for extra data. To this end, we propose OPSNet, an omnipotent and data-efficient framework for Open-vocabulary Panoptic Segmentation. Specifically, the exquisitely designed Embedding Modulation module, together with several meticulous components, enables adequate embedding enhancement and information exchange between the segmentation model and the visual-linguistic well-aligned CLIP encoder, resulting in superior segmentation performance under both open- and closed-vocabulary settings with much fewer need of additional data. Extensive experimental evaluations are conducted across multiple datasets (e.g., COCO, ADE20K, Cityscapes, and PascalContext) under various circumstances, where the proposed OPSNet achieves state-of-the-art results, which demonstrates the effectiveness and generality of the proposed approach. The code and trained models will be made publicly available.

</details>

### Exploring Open-Vocabulary Semantic Segmentation from CLIP Vision Encoder Distillation Only.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00071)
- **作者**: Jun Chen, Deyao Zhu, Guocheng Qian, Bernard Ghanem, Zhicheng Yan, Chenchen Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Unsupervised Open-Vocabulary Object Localization in Videos.
- **链接**: [arXiv:2309.09858](https://arxiv.org/abs/2309.09858) · 📚 被引 6
- **作者**: Ke Fan, Zechen Bai, Tianjun Xiao, Dominik Zietlow, Max Horn, Zixu Zhao et al.
- **🏷️ 机构**: Fudan University, Amazon Web Services, National University of Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we show that recent advances in video representation learning and pre-trained vision-language models allow for substantial improvements in self-supervised video object localization. We propose a method that first localizes objects in videos via an object-centric approach with slot attention and then assigns text to the obtained slots. The latter is achieved by an unsupervised way to read localized semantic information from the pre-trained CLIP model. The resulting video object localization is entirely unsupervised apart from the implicit annotation contained in CLIP, and it is effectively the first unsupervised approach that yields good results on regular video benchmarks.

</details>

### Global Knowledge Calibration for Fast Open-Vocabulary Segmentation.
- **链接**: [arXiv:2303.09181](https://arxiv.org/abs/2303.09181) · 📚 被引 42
- **作者**: Kunyang Han, Yong Liu, Jun Hao Liew, Henghui Ding, Jiajun Liu, Yitong Wang et al.
- **🏷️ 机构**: Beijing Jiaotong University,Institute of Information Science, Tsinghua University,Tsinghua Shenzhen International Graduate School, ByteDance
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in pre-trained vision-language models, such as CLIP, have enabled the segmentation of arbitrary concepts solely from textual inputs, a process commonly referred to as open-vocabulary semantic segmentation (OVS). However, existing OVS techniques confront a fundamental challenge: the trained classifier tends to overfit on the base classes observed during training, resulting in suboptimal generalization performance to unseen classes. To mitigate this issue, recent studies have proposed the use of an additional frozen pre-trained CLIP for classification. Nonetheless, this approach incurs heavy computational overheads as the CLIP vision encoder must be repeatedly forward-passed for each mask, rendering it impractical for real-world applications. To address this challenge, our objective is to develop a fast OVS model that can perform comparably or better without the extra computational burden of the CLIP image encoder during inference. To this end, we propose a core idea of preserving the generalizable representation when fine-tuning on known classes. Specifically, we introduce a text diversification strategy that generates a set of synonyms for each training category, which prevents the learned representation from collapsing onto specific known category names. Additionally, we employ a text-guided knowledge distillation method to preserve the generalizable knowledge of CLIP. Extensive experiments demonstrate that our proposed model achieves robust generalization performance across various datasets. Furthermore, we perform a preliminary exploration of open-vocabulary video segmentation and present a benchmark that can facilitate future open-vocabulary research in the video domain.

</details>

### Open-Vocabulary Semantic Segmentation with Decoupled One-Pass Network.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00106) · 📚 被引 45
- **作者**: Cong Han, Yujie Zhong, Dengjie Li, Kai Han, Lin Ma
- **🏷️ 机构**: Meituan Inc, The University of Hong Kong
- **会议**: ICCV 2023

### Contrastive Feature Masking Open-Vocabulary Vision Transformer.
- **链接**: [arXiv:2309.00775](https://arxiv.org/abs/2309.00775) · 📚 被引 22
- **作者**: Dahun Kim, Anelia Angelova, Weicheng Kuo
- **🏷️ 机构**: Google DeepMind
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Contrastive Feature Masking Vision Transformer (CFM-ViT) - an image-text pretraining methodology that achieves simultaneous learning of image- and region-level representation for open-vocabulary object detection (OVD). Our approach combines the masked autoencoder (MAE) objective into the contrastive learning objective to improve the representation for localization tasks. Unlike standard MAE, we perform reconstruction in the joint image-text embedding space, rather than the pixel space as is customary with the classical MAE method, which causes the model to better learn region-level semantics. Moreover, we introduce Positional Embedding Dropout (PED) to address scale variation between image-text pretraining and detection finetuning by randomly dropping out the positional embeddings during pretraining. PED improves detection performance and enables the use of a frozen ViT backbone as a region classifier, preventing the forgetting of open-vocabulary knowledge during detection finetuning. On LVIS open-vocabulary detection benchmark, CFM-ViT achieves a state-of-the-art 33.9 AP$r$, surpassing the best approach by 7.6 points and achieves better zero-shot detection transfer. Finally, CFM-ViT acquires strong image-level representation, outperforming the state of the art on 8 out of 12 metrics on zero-shot image-text retrieval benchmarks.

</details>

### Open-vocabulary Object Segmentation with Diffusion Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00705)
- **作者**: Ziyi Li, Qinye Zhou, Xiaoyun Zhang, Ya Zhang, Yanfeng Wang, Weidi Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Going Denser with Open-Vocabulary Part Segmentation.
- **链接**: [arXiv:2305.11173](https://arxiv.org/abs/2305.11173) · 📚 被引 50
- **作者**: Peize Sun, Shoufa Chen, Chenchen Zhu, Fanyi Xiao, Ping Luo, Saining Xie et al.
- **🏷️ 机构**: The University of Hong Kong, Meta AI, New York University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Object detection has been expanded from a limited number of categories to open vocabulary. Moving forward, a complete intelligent vision system requires understanding more fine-grained object descriptions, object parts. In this paper, we propose a detector with the ability to predict both open-vocabulary objects and their part segmentation. This ability comes from two designs. First, we train the detector on the joint of part-level, object-level and image-level data to build the multi-granularity alignment between language and image. Second, we parse the novel object into its parts by its dense semantic correspondence with the base object. These two designs enable the detector to largely benefit from various data sources and foundation models. In open-vocabulary part segmentation experiments, our method outperforms the baseline by 3.3$\sim$7.3 mAP in cross-dataset generalization on PartImageNet, and improves the baseline by 7.3 novel AP$_{50}$ in cross-category generalization on Pascal Part. Finally, we train a detector that generalizes to a wide range of part segmentation datasets while achieving better performance than dataset-specific training.

</details>

### Towards Open-Vocabulary Video Instance Segmentation.
- **链接**: [arXiv:2304.01715](https://arxiv.org/abs/2304.01715) · [代码](https://github.com/haochenheheda/LVVIS)
- **作者**: Haochen Wang, Xiaolong Jiang, Xu Tang, Yao Hu, Cilin Yan, Weidi Xie et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Video Instance Segmentation (VIS) aims at segmenting and categorizing objects in videos from a closed set of training categories, lacking the generalization ability to handle novel categories in real-world videos. To address this limitation, we make the following three contributions. First, we introduce the novel task of Open-Vocabulary Video Instance Segmentation, which aims to simultaneously segment, track, and classify objects in videos from open-set categories, including novel categories unseen during training. Second, to benchmark Open-Vocabulary VIS, we collect a Large-Vocabulary Video Instance Segmentation dataset (LV-VIS), that contains well-annotated objects from 1,196 diverse categories, significantly surpassing the category size of existing datasets by more than one order of magnitude. Third, we propose an efficient Memory-Induced Transformer architecture, OV2Seg, to first achieve Open-Vocabulary VIS in an end-to-end manner with near real-time inference speed. Extensive experiments on LV-VIS and four existing VIS datasets demonstrate the strong zero-shot generalization ability of OV2Seg on novel categories. The dataset and code are released here https://github.com/haochenheheda/LVVIS.

</details>

### Betrayed by Captions: Joint Caption Grounding and Generation for Open Vocabulary Instance Segmentation.
- **链接**: [arXiv:2301.00805](https://arxiv.org/abs/2301.00805) · 📚 被引 7
- **作者**: Jianzong Wu, Xiangtai Li, Henghui Ding, Xia Li, Guangliang Cheng, Yunhai Tong et al.
- **🏷️ 机构**: Nanyang Technological University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we focus on open vocabulary instance segmentation to expand a segmentation model to classify and segment instance-level novel categories. Previous approaches have relied on massive caption datasets and complex pipelines to establish one-to-one mappings between image regions and words in captions. However, such methods build noisy supervision by matching non-visible words to image regions, such as adjectives and verbs. Meanwhile, context words are also important for inferring the existence of novel objects as they show high inter-correlations with novel categories. To overcome these limitations, we devise a joint \textbf{Caption Grounding and Generation (CGG)} framework, which incorporates a novel grounding loss that only focuses on matching object nouns to improve learning efficiency. We also introduce a caption generation head that enables additional supervision and contextual modeling as a complementation to the grounding loss. Our analysis and results demonstrate that grounding and generation components complement each other, significantly enhancing the segmentation performance for novel classes. Experiments on the COCO dataset with two settings: Open Vocabulary Instance Segmentation (OVIS) and Open Set Panoptic Segmentation (OSPS) demonstrate the superiority of the CGG. Specifically, CGG achieves a substantial improvement of 6.8% mAP for novel classes without extra data on the OVIS task and 15% PQ improvements for novel classes on the OSPS benchmark.

</details>

### MasQCLIP for Open-Vocabulary Universal Image Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00088) · 📚 被引 40
- **作者**: Xin Xu, Tianyi Xiong, Zheng Ding, Zhuowen Tu
- **🏷️ 机构**: Peking University, Tsinghua University, University of California,San Diego
- **会议**: ICCV 2023

### A Simple Framework for Open-Vocabulary Segmentation and Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00100) · 📚 被引 138
- **作者**: Hao Zhang, Feng Li, Xueyan Zou, Shilong Liu, Chunyuan Li, Jianwei Yang et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, University of Wisconsin-Madison, International Digital Economy Academy (IDEA)
- **会议**: ICCV 2023

### SOAR: Scene-debiasing Open-set Action Recognition.
- **链接**: [arXiv:2309.01265](https://arxiv.org/abs/2309.01265) · 📚 被引 12
- **作者**: Yuanhao Zhai, Ziyi Liu, Zhenyu Wu, Yi Wu, Chunluan Zhou, David S. Doermann et al.
- **🏷️ 机构**: University at Buffalo, Wormpex AI Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning models have a risk of utilizing spurious clues to make predictions, such as recognizing actions based on the background scene. This issue can severely degrade the open-set action recognition performance when the testing samples have different scene distributions from the training samples. To mitigate this problem, we propose a novel method, called Scene-debiasing Open-set Action Recognition (SOAR), which features an adversarial scene reconstruction module and an adaptive adversarial scene classification module. The former prevents the decoder from reconstructing the video background given video features, and thus helps reduce the background information in feature learning. The latter aims to confuse scene type classification given video features, with a specific emphasis on the action foreground, and helps to learn scene-invariant information. In addition, we design an experiment to quantify the scene bias. The results indicate that the current open-set action recognizers are biased toward the scene, and our proposed SOAR method better mitigates such bias. Furthermore, our extensive experiments demonstrate that our method outperforms state-of-the-art methods, and the ablation studies confirm the effectiveness of our proposed modules.

</details>

### Class-relation Knowledge Distillation for Novel Class Discovery.
- **链接**: [arXiv:2307.09158](https://arxiv.org/abs/2307.09158) · [代码](https://github.com/kleinzcy/Cr-KD-NCD) · 📚 被引 24
- **作者**: Peiyan Gu, Chuyu Zhang, Ruijie Xu, Xuming He
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle the problem of novel class discovery, which aims to learn novel classes without supervision based on labeled data from known classes. A key challenge lies in transferring the knowledge in the known-class data to the learning of novel classes. Previous methods mainly focus on building a shared representation space for knowledge transfer and often ignore modeling class relations. To address this, we introduce a class relation representation for the novel classes based on the predicted class distribution of a model trained on known classes. Empirically, we find that such class relation becomes less informative during typical discovery training. To prevent such information loss, we propose a novel knowledge distillation framework, which utilizes our class-relation representation to regularize the learning of novel classes. In addition, to enable a flexible knowledge distillation scheme for each data point in novel classes, we develop a learnable weighting function for the regularization, which adaptively promotes knowledge transfer based on the semantic similarity between the novel and known classes. To validate the effectiveness and generalization of our method, we conduct extensive experiments on multiple benchmarks, including CIFAR100, Stanford Cars, CUB, and FGVC-Aircraft datasets. Our results demonstrate that the proposed method outperforms the previous state-of-the-art methods by a significant margin on almost all benchmarks. Code is available at \href{https://github.com/kleinzcy/Cr-KD-NCD}{here}.

</details>

## 跨领域论文（完整笔记在其他领域）

- Distilling DETR with Visual-Linguistic Knowledge for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Novel Scenes & Classes: Towards Adaptive Open-set Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- EdaDet: Open-Vocabulary Object Detection Using Early Dense Alignment. → [object-detection](../object-detection/Guideline%202023.md)
- Open-Vocabulary Object Detection With an Open Corpus. → [object-detection](../object-detection/Guideline%202023.md)
- Identification of Novel Classes for Improving Few-Shot Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
