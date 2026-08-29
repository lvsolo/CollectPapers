# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### PLOT: Prompt Learning with Optimal Transport for Vision-Language Models.
- **链接**: [出版页](https://openreview.net/forum?id=zqwryBoXYnh)
- **作者**: Guangyi Chen, Weiran Yao, Xiangchen Song, Xinyue Li, Yongming Rao, Kun Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Write and Paint: Generative Vision-Language Models are Unified Modal Learners.
- **链接**: [出版页](https://openreview.net/forum?id=HgQR0mXQ1_a)
- **作者**: Shizhe Diao, Wangchunshu Zhou, Xinsong Zhang, Jiawei Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Spotlight: Mobile UI Understanding using Vision-Language Models with a Focus.
- **链接**: [arXiv:2209.14927](https://arxiv.org/abs/2209.14927)
- **作者**: Gang Li, Yang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mobile UI understanding is important for enabling various interaction tasks such as UI automation and accessibility. Previous mobile UI modeling often depends on the view hierarchy information of a screen, which directly provides the structural data of the UI, with the hope to bypass challenging tasks of visual modeling from screen pixels. However, view hierarchies are not always available, and are often corrupted with missing object descriptions or misaligned structure information. As a result, despite the use of view hierarchies could offer short-term gains, it may ultimately hinder the applicability and performance of the model. In this paper, we propose Spotlight, a vision-only approach for mobile UI understanding. Specifically, we enhance a vision-language model that only takes the screenshot of the UI and a region of interest on the screen -- the focus -- as the input. This general architecture of Spotlight is easily scalable and capable of performing a range of UI modeling tasks. Our experiments show that our model establishes SoTA results on several representative UI tasks and outperforms previous methods that use both screenshots and view hierarchies as inputs. Furthermore, we explore multi-task learning and few-shot prompting capacities of the proposed models, demonstrating promising results in the multi-task learning direction.

</details>

### MEDICAL IMAGE UNDERSTANDING WITH PRETRAINED VISION LANGUAGE MODELS: A COMPREHENSIVE STUDY.
- **链接**: [arXiv:2209.15517](https://arxiv.org/abs/2209.15517)
- **作者**: Ziyuan Qin, Huahui Yi, Qicheng Lao, Kang Li
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The large-scale pre-trained vision language models (VLM) have shown remarkable domain transfer capability on natural images. However, it remains unknown whether this capability can also apply to the medical image domain. This paper thoroughly studies the knowledge transferability of pre-trained VLMs to the medical domain, where we show that well-designed medical prompts are the key to elicit knowledge from pre-trained VLMs. We demonstrate that by prompting with expressive attributes that are shared between domains, the VLM can carry the knowledge across domains and improve its generalization. This mechanism empowers VLMs to recognize novel objects with fewer or without image samples. Furthermore, to avoid the laborious manual designing process, we develop three approaches for automatic generation of medical prompts, which can inject expert-level medical knowledge and image-specific information into the prompts for fine-grained grounding. We conduct extensive experiments on thirteen different medical datasets across various modalities, showing that our well-designed prompts greatly improve the zero-shot performance compared to the default prompts, and our fine-tuned models surpass the supervised models by a significant margin.

</details>

### When and Why Vision-Language Models Behave like Bags-Of-Words, and What to Do About It?
- **链接**: [arXiv:2210.01936](https://arxiv.org/abs/2210.01936)
- **作者**: Mert Yüksekgönül, Federico Bianchi, Pratyusha Kalluri, Dan Jurafsky, James Zou
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Despite the success of large vision and language models (VLMs) in many downstream applications, it is unclear how well they encode compositional information. Here, we create the Attribution, Relation, and Order (ARO) benchmark to systematically evaluate the ability of VLMs to understand different types of relationships, attributes, and order. ARO consists of Visual Genome Attribution, to test the understanding of objects' properties; Visual Genome Relation, to test for relational understanding; and COCO & Flickr30k-Order, to test for order sensitivity. ARO is orders of magnitude larger than previous benchmarks of compositionality, with more than 50,000 test cases. We show where state-of-the-art VLMs have poor relational understanding, can blunder when linking objects to their attributes, and demonstrate a severe lack of order sensitivity. VLMs are predominantly trained and evaluated on large datasets with rich compositional structure in the images and captions. Yet, training on these datasets has not been enough to address the lack of compositional understanding, and evaluating on these datasets has failed to surface this deficiency. To understand why these limitations emerge and are not represented in the standard tests, we zoom into the evaluation and training procedures. We demonstrate that it is possible to perform well on retrieval over existing datasets without using the composition and order information. Given that contrastive pretraining optimizes for retrieval on datasets with similar shortcuts, we hypothesize that this can explain why the models do not need to learn to represent compositional information. This finding suggests a natural solution: composition-aware hard negative mining. We show that a simple-to-implement modification of contrastive learning significantly improves the performance on tasks requiring understanding of order and compositionality.

</details>
