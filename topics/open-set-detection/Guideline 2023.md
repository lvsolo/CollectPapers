# Open-set Detection — 2023 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Contrastive Feature Masking Open-Vocabulary Vision Transformer.
- **链接**: [arXiv:2309.00775](https://arxiv.org/abs/2309.00775) · 📚 被引 22
- **作者**: Dahun Kim, Anelia Angelova, Weicheng Kuo
- **🏷️ 机构**: Google DeepMind
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Contrastive Feature Masking Vision Transformer (CFM-ViT) - an image-text pretraining methodology that achieves simultaneous learning of image- and region-level representation for open-vocabulary object detection (OVD). Our approach combines the masked autoencoder (MAE) objective into the contrastive learning objective to improve the representation for localization tasks. Unlike standard MAE, we perform reconstruction in the joint image-text embedding space, rather than the pixel space as is customary with the classical MAE method, which causes the model to better learn region-level semantics. Moreover, we introduce Positional Embedding Dropout (PED) to address scale variation between image-text pretraining and detection finetuning by randomly dropping out the positional embeddings during pretraining. PED improves detection performance and enables the use of a frozen ViT backbone as a region classifier, preventing the forgetting of open-vocabulary knowledge during detection finetuning. On LVIS open-vocabulary detection benchmark, CFM-ViT achieves a state-of-the-art 33.9 AP$r$, surpassing the best approach by 7.6 points and achieves better zero-shot detection transfer. Finally, CFM-ViT acquires strong image-level representation, outperforming the state of the art on 8 out of 12 metrics on zero-shot image-text retrieval benchmarks.

</details>

### SOAR: Scene-debiasing Open-set Action Recognition.
- **链接**: [arXiv:2309.01265](https://arxiv.org/abs/2309.01265) · 📚 被引 12
- **作者**: Yuanhao Zhai, Ziyi Liu, Zhenyu Wu, Yi Wu, Chunluan Zhou, David S. Doermann et al.
- **🏷️ 机构**: University at Buffalo, Wormpex AI Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning models have a risk of utilizing spurious clues to make predictions, such as recognizing actions based on the background scene. This issue can severely degrade the open-set action recognition performance when the testing samples have different scene distributions from the training samples. To mitigate this problem, we propose a novel method, called Scene-debiasing Open-set Action Recognition (SOAR), which features an adversarial scene reconstruction module and an adaptive adversarial scene classification module. The former prevents the decoder from reconstructing the video background given video features, and thus helps reduce the background information in feature learning. The latter aims to confuse scene type classification given video features, with a specific emphasis on the action foreground, and helps to learn scene-invariant information. In addition, we design an experiment to quantify the scene bias. The results indicate that the current open-set action recognizers are biased toward the scene, and our proposed SOAR method better mitigates such bias. Furthermore, our extensive experiments demonstrate that our method outperforms state-of-the-art methods, and the ablation studies confirm the effectiveness of our proposed modules.

</details>

### Exploring Open-Vocabulary Semantic Segmentation from CLIP Vision Encoder Distillation Only.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00071)
- **作者**: Jun Chen, Deyao Zhu, Guocheng Qian, Bernard Ghanem, Zhicheng Yan, Chenchen Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

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
