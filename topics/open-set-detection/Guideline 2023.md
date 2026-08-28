# Open-set Detection — 2023 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### OpenMask3D: Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2306.13631](https://arxiv.org/abs/2306.13631) · 📚 被引 27
- **作者**: Ayça Takmaz, Elisabetta Fedele, Robert W. Sumner, Marc Pollefeys, Federico Tombari, Francis Engelmann
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the task of open-vocabulary 3D instance segmentation. Current approaches for 3D instance segmentation can typically only recognize object categories from a pre-defined closed set of classes that are annotated in the training datasets. This results in important limitations for real-world applications where one might need to perform tasks guided by novel, open-vocabulary queries related to a wide variety of objects. Recently, open-vocabulary 3D scene understanding methods have emerged to address this problem by learning queryable features for each point in the scene. While such a representation can be directly employed to perform semantic segmentation, existing methods cannot separate multiple object instances. In this work, we address this limitation, and propose OpenMask3D, which is a zero-shot approach for open-vocabulary 3D instance segmentation. Guided by predicted class-agnostic 3D instance masks, our model aggregates per-mask features via multi-view fusion of CLIP-based image embeddings. Experiments and ablation studies on ScanNet200 and Replica show that OpenMask3D outperforms other open-vocabulary methods, especially on the long-tail distribution. Qualitative experiments further showcase OpenMask3D's ability to segment object properties based on free-form queries describing geometry, affordances, and materials.

</details>

### Hierarchical Open-vocabulary Universal Image Segmentation.
- **链接**: [arXiv:2307.00764](https://arxiv.org/abs/2307.00764) · [代码](https://github.com/berkeley-hipie/HIPIE) · 📚 被引 1
- **作者**: Xudong Wang, Shufan Li, Konstantinos Kallidromitis, Yusuke Kato, Kazuki Kozuka, Trevor Darrell
- **🏷️ 机构**: UC Berkeley
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary image segmentation aims to partition an image into semantic regions according to arbitrary text descriptions. However, complex visual scenes can be naturally decomposed into simpler parts and abstracted at multiple levels of granularity, introducing inherent segmentation ambiguity. Unlike existing methods that typically sidestep this ambiguity and treat it as an external factor, our approach actively incorporates a hierarchical representation encompassing different semantic-levels into the learning process. We propose a decoupled text-image fusion mechanism and representation learning modules for both "things" and "stuff". Additionally, we systematically examine the differences that exist in the textual and visual features between these types of categories. Our resulting model, named HIPIE, tackles HIerarchical, oPen-vocabulary, and unIvErsal segmentation tasks within a unified framework. Benchmarked on over 40 datasets, e.g., ADE20K, COCO, Pascal-VOC Part, RefCOCO/RefCOCOg, ODinW and SeginW, HIPIE achieves the state-of-the-art results at various levels of image comprehension, including semantic-level (e.g., semantic segmentation), instance-level (e.g., panoptic/referring segmentation and object detection), as well as part-level (e.g., part/subpart segmentation) tasks. Our code is released at https://github.com/berkeley-hipie/HIPIE.

</details>

### Weakly Supervised 3D Open-vocabulary Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/a76b693f36916a5ed84d6e5b39a0dc03-Abstract-Conference.html)
- **作者**: Kunhao Liu, Fangneng Zhan, Jiahui Zhang, Muyu Xu, Yingchen Yu, Abdulmotaleb El Saddik et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Open-Vocabulary Semantic Segmentation via Attribute Decomposition-Aggregation.
- **链接**: [arXiv:2309.00096](https://arxiv.org/abs/2309.00096)
- **作者**: Chaofan Ma, Yuhuan Yang, Chen Ju, Fei Zhang, Ya Zhang, Yanfeng Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation is a challenging task that requires segmenting novel object categories at inference time. Recent studies have explored vision-language pre-training to handle this task, but suffer from unrealistic assumptions in practical scenarios, i.e., low-quality textual category names. For example, this paradigm assumes that new textual categories will be accurately and completely provided, and exist in lexicons during pre-training. However, exceptions often happen when encountering ambiguity for brief or incomplete names, new words that are not present in the pre-trained lexicons, and difficult-to-describe categories for users. To address these issues, this work proposes a novel attribute decomposition-aggregation framework, AttrSeg, inspired by human cognition in understanding new concepts. Specifically, in the decomposition stage, we decouple class names into diverse attribute descriptions to complement semantic contexts from multiple perspectives. Two attribute construction strategies are designed: using large language models for common categories, and involving manually labeling for human-invented categories. In the aggregation stage, we group diverse attributes into an integrated global description, to form a discriminative classifier that distinguishes the target object from others. One hierarchical aggregation architecture is further proposed to achieve multi-level aggregations, leveraging the meticulously designed clustering module. The final results are obtained by computing the similarity between aggregated attributes and images embeddings. To evaluate the effectiveness, we annotate three types of datasets with attribute descriptions, and conduct extensive experiments and ablation studies. The results show the superior performance of attribute decomposition-aggregation.

</details>

### Prompt Pre-Training with Twenty-Thousand Classes for Open-Vocabulary Visual Recognition.
- **链接**: [arXiv:2304.04704](https://arxiv.org/abs/2304.04704) · [代码](https://github.com/amazon-science/prompt-pretraining) · 📚 被引 4
- **作者**: Shuhuai Ren, Aston Zhang, Yi Zhu, Shuai Zhang, Shuai Zheng, Mu Li et al.
- **🏷️ 机构**: AWS / CMU
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This work proposes POMP, a prompt pre-training method for vision-language models. Being memory and computation efficient, POMP enables the learned prompt to condense semantic information for a rich set of visual concepts with over twenty-thousand classes. Once pre-trained, the prompt with a strong transferable ability can be directly plugged into a variety of visual recognition tasks including image classification, semantic segmentation, and object detection, to boost recognition performances in a zero-shot manner. Empirical evaluation shows that POMP achieves state-of-the-art performances on 21 datasets, e.g., 67.0% average accuracy on 10 classification datasets (+3.1% compared to CoOp) and 84.4 hIoU on open-vocabulary Pascal VOC segmentation (+6.9 compared to ZSSeg). Our code is available at https://github.com/amazon-science/prompt-pretraining.

</details>

### OV-PARTS: Towards Open-Vocabulary Part Segmentation.
- **链接**: [arXiv:2310.05107](https://arxiv.org/abs/2310.05107) · [代码](https://github.com/OpenRobotLab/OV_PARTS) · 📚 被引 4
- **作者**: Meng Wei, Xiaoyu Yue, Wenwei Zhang, Shu Kong, Xihui Liu, Jiangmiao Pang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Segmenting and recognizing diverse object parts is a crucial ability in applications spanning various computer vision and robotic tasks. While significant progress has been made in object-level Open-Vocabulary Semantic Segmentation (OVSS), i.e., segmenting objects with arbitrary text, the corresponding part-level research poses additional challenges. Firstly, part segmentation inherently involves intricate boundaries, while limited annotated data compounds the challenge. Secondly, part segmentation introduces an open granularity challenge due to the diverse and often ambiguous definitions of parts in the open world. Furthermore, the large-scale vision and language models, which play a key role in the open vocabulary setting, struggle to recognize parts as effectively as objects. To comprehensively investigate and tackle these challenges, we propose an Open-Vocabulary Part Segmentation (OV-PARTS) benchmark. OV-PARTS includes refined versions of two publicly available datasets: Pascal-Part-116 and ADE20K-Part-234. And it covers three specific tasks: Generalized Zero-Shot Part Segmentation, Cross-Dataset Part Segmentation, and Few-Shot Part Segmentation, providing insights into analogical reasoning, open granularity and few-shot adapting abilities of models. Moreover, we analyze and adapt two prevailing paradigms of existing object-level OVSS methods for OV-PARTS. Extensive experimental analysis is conducted to inspire future research in leveraging foundational models for OV-PARTS. The code and dataset are available at https://github.com/OpenRobotLab/OV_PARTS.

</details>

### Convolutions Die Hard: Open-Vocabulary Segmentation with Single Frozen Convolutional CLIP.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/661caac7729aa7d8c6b8ac0d39ccbc6a-Abstract-Conference.html)
- **作者**: Qihang Yu, Ju He, Xueqing Deng, Xiaohui Shen, Liang-Chieh Chen
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Uncovering Prototypical Knowledge for Weakly Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/e95eb5206c867be843fbc14bbfe8c10e-Abstract-Conference.html) · 📚 被引 5
- **作者**: Fei Zhang, Tianfei Zhou, Boyang Li, Hao He, Chaofan Ma, Tianjiao Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

## 跨领域论文（完整笔记在其他领域）

- CoDA: Collaborative Novel Box Discovery and Cross-modal Alignment for Open-vocabulary 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- CoDet: Co-occurrence Guided Region-Word Alignment for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Scaling Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- POP-3D: Open-Vocabulary 3D Occupancy Prediction from Images. → [occupancy](../occupancy/Guideline%202023.md)
