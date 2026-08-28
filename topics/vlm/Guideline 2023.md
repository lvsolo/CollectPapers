# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 10 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLIP2Point: Transfer CLIP to Point Cloud Classification with Image-Depth Pre-Training.
- **链接**: [arXiv:2210.01055](https://arxiv.org/abs/2210.01055) · 📚 被引 140
- **作者**: Tianyu Huang, Bowen Dong, Yunhan Yang, Xiaoshui Huang, Rynson W. H. Lau, Wanli Ouyang et al.
- **🏷️ 机构**: Harbin Institute of Technology, Shanghai AI Laboratory, City University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-training across 3D vision and language remains under development because of limited training data. Recent works attempt to transfer vision-language pre-training models to 3D vision. PointCLIP converts point cloud data to multi-view depth maps, adopting CLIP for shape classification. However, its performance is restricted by the domain gap between rendered depth maps and images, as well as the diversity of depth distributions. To address this issue, we propose CLIP2Point, an image-depth pre-training method by contrastive learning to transfer CLIP to the 3D domain, and adapt it to point cloud classification. We introduce a new depth rendering setting that forms a better visual effect, and then render 52,460 pairs of images and depth maps from ShapeNet for pre-training. The pre-training scheme of CLIP2Point combines cross-modality learning to enforce the depth features for capturing expressive visual and textual features and intra-modality learning to enhance the invariance of depth aggregation. Additionally, we propose a novel Dual-Path Adapter (DPA) module, i.e., a dual-path structure with simplified adapters for few-shot learning. The dual-path structure allows the joint use of CLIP and CLIP2Point, and the simplified adapter can well fit few-shot tasks without post-search. Experimental results show that CLIP2Point is effective in transferring CLIP knowledge to 3D vision. Our CLIP2Point outperforms PointCLIP and other self-supervised 3D networks, achieving state-of-the-art results on zero-shot and few-shot classification.

</details>

### Bird's-Eye-View Scene Graph for Vision-Language Navigation.
- **链接**: [arXiv:2308.04758](https://arxiv.org/abs/2308.04758)
- **作者**: Rui Liu, Xiaohan Wang, Wenguan Wang, Yi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language navigation (VLN), which entails an agent to navigate 3D environments following human instructions, has shown great advances. However, current agents are built upon panoramic observations, which hinders their ability to perceive 3D scene geometry and easily leads to ambiguous selection of panoramic view. To address these limitations, we present a BEV Scene Graph (BSG), which leverages multi-step BEV representations to encode scene layouts and geometric cues of indoor environment under the supervision of 3D detection. During navigation, BSG builds a local BEV representation at each step and maintains a BEV-based global scene map, which stores and organizes all the online collected local BEV representations according to their topological relations. Based on BSG, the agent predicts a local BEV grid-level decision score and a global graph-level decision score, combined with a sub-view selection score on panoramic views, for more accurate action prediction. Our approach significantly outperforms state-of-the-art methods on REVERIE, R2R, and R4R, showing the potential of BEV perception in VLN.

</details>

### PointCLIP V2: Prompting CLIP and GPT for Powerful 3D Open-world Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00249) · 📚 被引 181
- **作者**: Xiangyang Zhu, Renrui Zhang, Bowei He, Ziyu Guo, Ziyao Zeng, Zipeng Qin et al.
- **🏷️ 机构**: City University of Hong Kong, The Chinese University of Hong Kong, Yale University
- **会议**: ICCV 2023

### CLIP-FO3D: Learning Free Open-world 3D Scene Representations from 2D Dense CLIP.
- **链接**: [arXiv:2303.04748](https://arxiv.org/abs/2303.04748) · 📚 被引 66
- **作者**: Junbo Zhang, Runpei Dong, Kaisheng Ma
- **🏷️ 机构**: Tsinghua University, Xi&#x2019;an Jiaotong University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training a 3D scene understanding model requires complicated human annotations, which are laborious to collect and result in a model only encoding close-set object semantics. In contrast, vision-language pre-training models (e.g., CLIP) have shown remarkable open-world reasoning properties. To this end, we propose directly transferring CLIP's feature space to 3D scene understanding model without any form of supervision. We first modify CLIP's input and forwarding process so that it can be adapted to extract dense pixel features for 3D scene contents. We then project multi-view image features to the point cloud and train a 3D scene understanding model with feature distillation. Without any annotations or additional training, our model achieves promising annotation-free semantic segmentation results on open-vocabulary semantics and long-tailed concepts. Besides, serving as a cross-modal pre-training framework, our method can be used to improve data efficiency during fine-tuning. Our model outperforms previous SOTA methods in various zero-shot and data-efficient learning benchmarks. Most importantly, our model successfully inherits CLIP's rich-structured knowledge, allowing 3D scene understanding models to recognize not only object concepts but also open-world semantics.

</details>

### CLIPN for Zero-Shot OOD Detection: Teaching CLIP to Say No.
- **链接**: [arXiv:2308.12213](https://arxiv.org/abs/2308.12213) · [代码](https://github.com/xmed-lab/CLIPN) · 📚 被引 105
- **作者**: Hualiang Wang, Yi Li, Huifeng Yao, Xiaomeng Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology,Department of Electronic and Computer Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection refers to training the model on an in-distribution (ID) dataset to classify whether the input images come from unknown classes. Considerable effort has been invested in designing various OOD detection methods based on either convolutional neural networks or transformers. However, zero-shot OOD detection methods driven by CLIP, which only require class names for ID, have received less attention. This paper presents a novel method, namely CLIP saying no (CLIPN), which empowers the logic of saying no within CLIP. Our key motivation is to equip CLIP with the capability of distinguishing OOD and ID samples using positive-semantic prompts and negation-semantic prompts. Specifically, we design a novel learnable no prompt and a no text encoder to capture negation semantics within images. Subsequently, we introduce two loss functions: the image-text binary-opposite loss and the text semantic-opposite loss, which we use to teach CLIPN to associate images with no prompts, thereby enabling it to identify unknown samples. Furthermore, we propose two threshold-free inference algorithms to perform OOD detection by utilizing negation semantics from no prompts and the text encoder. Experimental results on 9 benchmark datasets (3 ID datasets and 6 OOD datasets) for the OOD detection task demonstrate that CLIPN, based on ViT-B-16, outperforms 7 well-used algorithms by at least 2.34% and 11.64% in terms of AUROC and FPR95 for zero-shot OOD detection on ImageNet-1K. Our CLIPN can serve as a solid foundation for effectively leveraging CLIP in downstream OOD tasks. The code is available on https://github.com/xmed-lab/CLIPN.

</details>

### TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance.
- **链接**: [arXiv:2309.12314](https://arxiv.org/abs/2309.12314) · 📚 被引 73
- **作者**: Kan Wu, Houwen Peng, Zhenghong Zhou, Bin Xiao, Mengchen Liu, Lu Yuan et al.
- **🏷️ 机构**: Sun Yat-sen University, Microsoft, Huazhong University of Science &amp; Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel cross-modal distillation method, called TinyCLIP, for large-scale language-image pre-trained models. The method introduces two core techniques: affinity mimicking and weight inheritance. Affinity mimicking explores the interaction between modalities during distillation, enabling student models to mimic teachers' behavior of learning cross-modal feature alignment in a visual-linguistic affinity space. Weight inheritance transmits the pre-trained weights from the teacher models to their student counterparts to improve distillation efficiency. Moreover, we extend the method into a multi-stage progressive distillation to mitigate the loss of informative weights during extreme compression. Comprehensive experiments demonstrate the efficacy of TinyCLIP, showing that it can reduce the size of the pre-trained CLIP ViT-B/32 by 50%, while maintaining comparable zero-shot performance. While aiming for comparable performance, distillation with weight inheritance can speed up the training by 1.4 - 7.8 $\times$ compared to training from scratch. Moreover, our TinyCLIP ViT-8M/16, trained on YFCC-15M, achieves an impressive zero-shot top-1 accuracy of 41.1% on ImageNet, surpassing the original CLIP ViT-B/16 by 3.5% while utilizing only 8.9% parameters. Finally, we demonstrate the good transferability of TinyCLIP in various downstream tasks. Code and models will be open-sourced at https://aka.ms/tinyclip.

</details>

## 跨领域论文（完整笔记在其他领域）

- ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
- Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202023.md)
- Exploring Open-Vocabulary Semantic Segmentation from CLIP Vision Encoder Distillation Only. → [open-set-detection](../open-set-detection/Guideline%202023.md)
