# Open-set Detection — 2022 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

### PromptDet: Towards Open-Vocabulary Detection Using Uncurated Images. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20077-9_41) · 📚 被引 140
- **作者**: Chengjian Feng, Yujie Zhong, Zequn Jie, Xiangxiang Chu, Haibing Ren, Xiaolin Wei et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对开放词汇检测依赖人工标注数据的问题，该论文提出PromptDet方法，利用非精选图像（如网络爬取数据）进行训练，通过文本提示和区域级对比学习实现开放词汇检测。方法结合视觉-语言预训练模型，在无需人工标注的情况下学习新类别，并支持任意文本查询的检测。实验表明在多个基准上优于现有方法，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses open-vocabulary detection by proposing PromptDet, which leverages uncurated images and text prompts with region-level contrastive learning to detect novel classes without manual annotations. It builds on vision-language pretraining and supports arbitrary text queries, outperforming prior methods on benchmarks, though no specific numbers are given in the abstract.
- **核心贡献**: 提出PromptDet方法，利用非精选图像实现开放词汇检测。
- **创新点**: 结合文本提示和区域级对比学习，无需人工标注即可学习新类别。
- **结果**: 在多个基准上优于现有方法，但未提供具体数据。

### Scaling Open-Vocabulary Image Segmentation with Image-Level Labels. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_31) · 📚 被引 339
- **作者**: Golnaz Ghiasi, Xiuye Gu, Yin Cui, Tsung-Yi Lin
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对开放词汇图像分割依赖像素级标注的问题，该论文提出利用图像级标签进行训练的方法，通过视觉-语言模型对齐图像和文本嵌入，实现开放词汇分割。方法在无需密集标注的情况下学习任意类别，并扩展到大规模数据集。实验表明在多个分割基准上达到与全监督方法相当的性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses open-vocabulary image segmentation by proposing a method that trains with image-level labels, aligning visual and text embeddings via vision-language models to segment arbitrary categories without dense annotations. It scales to large datasets and achieves performance comparable to fully supervised methods on benchmarks, though no specific numbers are provided in the abstract.
- **核心贡献**: 提出利用图像级标签训练开放词汇分割模型的方法。
- **创新点**: 通过视觉-语言对齐实现无需像素级标注的开放词汇分割。
- **结果**: 在多个基准上达到与全监督方法相当的性能。

### Towards Open-Vocabulary Scene Graph Generation with Prompt-Based Finetuning. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2208.08165](https://arxiv.org/abs/2208.08165) · 📚 被引 46
- **作者**: Tao He, Lianli Gao, Jingkuan Song, Yuan-Fang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对场景图生成中闭集设置限制实际应用的问题，该论文提出开放词汇场景图生成任务，要求模型在基类上训练但推断未见目标类的关系。方法采用两步策略：先在大量粗粒度区域-标题数据上预训练，再利用两种基于提示的技术微调预训练模型而不更新参数，支持完全未见类别的推理。在Visual Genome、GQA和Open-Image三个基准上显著优于现有SGG方法。
- **摘要（英）**: This paper introduces open-vocabulary scene graph generation, where models trained on base classes must infer relations for unseen classes. It proposes a two-step method with pretraining on region-caption data and prompt-based finetuning without parameter updates, enabling inference on completely unseen classes. The method significantly outperforms strong SGG baselines on Visual Genome, GQA, and Open-Image.
- **核心贡献**: 提出开放词汇场景图生成任务及基于提示微调的两步方法。
- **创新点**: 利用提示技术在不更新参数的情况下实现未见类别的关系推理。
- **结果**: 在三个基准上显著优于现有SGG方法。

### Improving Closed and Open-Vocabulary Attribute Prediction Using Transformers. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19806-9_12) · 📚 被引 11
- **作者**: Khoi Pham, Kushal Kafle, Zhe Lin, Zhihong Ding, Scott Cohen, Quan Tran et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: 针对属性预测在闭集和开放词汇设置下的性能提升问题，该论文提出基于Transformer的方法，利用视觉-语言模型增强属性预测能力。方法通过Transformer架构捕捉对象与属性间的交互，并支持开放词汇属性推理。实验表明在多个属性预测基准上取得改进，但摘要未提供具体数值。
- **摘要（英）**: This paper improves attribute prediction in closed and open-vocabulary settings using Transformer-based methods, leveraging vision-language models to capture object-attribute interactions. It supports open-vocabulary attribute inference and achieves improvements on benchmarks, though no specific numbers are given in the abstract.
- **核心贡献**: 提出基于Transformer的属性预测方法，支持开放词汇推理。
- **创新点**: 利用视觉-语言模型增强属性预测的泛化能力。
- **结果**: 在属性预测基准上取得改进，但未提供具体数据。

### A Simple Baseline for Open-Vocabulary Semantic Segmentation with Pre-trained Vision-Language Model. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-19818-2_42) · 📚 被引 211
- **作者**: Mengde Xu, Zheng Zhang, Fangyun Wei, Yutong Lin, Yue Cao, Han Hu et al.
- **🏷️ 机构**: HUAST
- **会议**: ECCV 2022
- **摘要（中）**: ①针对开放词汇语义分割中依赖大量标注数据的问题，提出利用预训练视觉-语言模型（如CLIP）的简单基线方法。②方法通过冻结预训练模型并仅微调少量参数，将图像区域与文本嵌入对齐，实现开放词汇分割。③相比复杂的两阶段方法，该基线简化了流程，降低了计算成本，同时保持了竞争力。④在多个基准数据集上取得了与现有方法相当或更优的性能，但摘要未提供具体数值。
- **摘要（英）**: This paper addresses open-vocabulary semantic segmentation by proposing a simple baseline leveraging pre-trained vision-language models. It aligns image regions with text embeddings via minimal fine-tuning, simplifying complex pipelines while maintaining competitive performance. The method achieves comparable or better results on standard benchmarks, though specific numbers are not detailed in the abstract.
- **核心贡献**: 提出一个简单且有效的开放词汇语义分割基线，验证了预训练VLM的潜力。
- **创新点**: 利用冻结的预训练VLM进行轻量级微调，简化了分割流程。
- **结果**: 在多个基准上达到与复杂方法相当的性能。

### OpenLDN: Learning to Discover Novel Classes for Open-World Semi-Supervised Learning. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2207.02261](https://arxiv.org/abs/2207.02261) · 📚 被引 36
- **作者**: Mamshad Nayeem Rizve, Navid Kardan, Salman Khan, Fahad Shahbaz Khan, Mubarak Shah
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对开放世界半监督学习中，未标注数据可能包含新类别的问题，提出OpenLDN方法。②方法利用成对相似性损失，通过双层优化，在利用标注数据识别已知类的同时，隐式聚类新类别样本。③相比传统SSL假设同分布，该方法放宽了假设，能同时检测和聚类新类。④在多个基准上显著优于现有SSL方法，并有效发现新类，但摘要未给出具体数值。
- **摘要（英）**: This work tackles open-world semi-supervised learning, where unlabeled data may contain novel classes. OpenLDN uses a pairwise similarity loss with bi-level optimization to recognize known classes and cluster novel ones simultaneously. It outperforms existing SSL methods on benchmarks and effectively discovers new classes, though specific metrics are omitted.
- **核心贡献**: 提出OpenLDN，首个在开放世界SSL中同时识别已知类和新类的框架。
- **创新点**: 通过成对相似性损失和双层优化实现隐式新类聚类。
- **结果**: 在多个数据集上优于现有SSL方法，并成功发现新类。

## 跨领域论文（完整笔记在其他领域）

- Open-Vocabulary DETR with Conditional Matching. → [object-detection](../object-detection/Guideline%202022.md)
- Open Vocabulary Object Detection with Pseudo Bounding-Box Labels. → [object-detection](../object-detection/Guideline%202022.md)
- Open-Set Semi-Supervised Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Class-Agnostic Object Detection with Multi-modal Transformer. → [multimodal](../multimodal/Guideline%202022.md)
- Simple Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Few-Shot Object Detection by Knowledge Distillation Using Bag-of-Visual-Words Representations. → [object-detection](../object-detection/Guideline%202022.md)
- UC-OWOD: Unknown-Classified Open World Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Multi-faceted Distillation of Base-Novel Commonality for Few-Shot Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Few-Shot Class-Incremental Learning for 3D Point Cloud Objects. → [continual-learning](../continual-learning/Guideline%202022.md)
- DenseHybrid: Hybrid Anomaly Detection for Dense Open-Set Recognition. → [object-detection](../object-detection/Guideline%202022.md)
- Motion Inspired Unsupervised Perception and Prediction in Autonomous Driving. → [3d-detection](../3d-detection/Guideline%202022.md)
- Few-Shot Class-Incremental Learning from an Open-Set Perspective. → [continual-learning](../continual-learning/Guideline%202022.md)
