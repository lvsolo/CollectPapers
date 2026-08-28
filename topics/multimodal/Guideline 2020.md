# Multimodal — 2020 Guideline

> 领域: 多模态学习（图文对齐、融合、多模态融合感知）
> 论文数: 5 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Multimodal Future Localization and Emergence Prediction for Objects in Egocentric View With a Reachability Prior.
- **链接**: [arXiv:2006.04700](https://arxiv.org/abs/2006.04700) · [代码](https://github.com/lmb-freiburg/FLN-EPN-RPN) · 📚 被引 29
- **作者**: Osama Makansi, Özgün Çiçek, Kevin Buchicchio, Thomas Brox
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we investigate the problem of anticipating future dynamics, particularly the future location of other vehicles and pedestrians, in the view of a moving vehicle. We approach two fundamental challenges: (1) the partial visibility due to the egocentric view with a single RGB camera and considerable field-of-view change due to the egomotion of the vehicle; (2) the multimodality of the distribution of future states. In contrast to many previous works, we do not assume structural knowledge from maps. We rather estimate a reachability prior for certain classes of objects from the semantic map of the present image and propagate it into the future using the planned egomotion. Experiments show that the reachability prior combined with multi-hypotheses learning improves multimodal prediction of the future location of tracked objects and, for the first time, the emergence of new objects. We also demonstrate promising zero-shot transfer to unseen datasets. Source code is available at $\href{https://github.com/lmb-freiburg/FLN-EPN-RPN}{\text{this https URL.}}$

</details>

### Multi-Modal Domain Adaptation for Fine-Grained Action Recognition.
- **链接**: [arXiv:2001.09691](https://arxiv.org/abs/2001.09691) · 📚 被引 173
- **作者**: Jonathan Munro, Dima Damen
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-grained action recognition datasets exhibit environmental bias, where multiple video sequences are captured from a limited number of environments. Training a model in one environment and deploying in another results in a drop in performance due to an unavoidable domain shift. Unsupervised Domain Adaptation (UDA) approaches have frequently utilised adversarial training between the source and target domains. However, these approaches have not explored the multi-modal nature of video within each domain. In this work we exploit the correspondence of modalities as a self-supervised alignment approach for UDA in addition to adversarial alignment. We test our approach on three kitchens from our large-scale dataset, EPIC-Kitchens, using two modalities commonly employed for action recognition: RGB and Optical Flow. We show that multi-modal self-supervision alone improves the performance over source-only training by 2.4% on average. We then combine adversarial training with multi-modal self-supervision, showing that our approach outperforms other UDA methods by 3%.

</details>

### Speech2Action: Cross-Modal Supervision for Action Recognition.
- **链接**: [arXiv:2003.13594](https://arxiv.org/abs/2003.13594) · 📚 被引 45
- **作者**: Arsha Nagrani, Chen Sun, David Ross, Rahul Sukthankar, Cordelia Schmid, Andrew Zisserman
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Is it possible to guess human action from dialogue alone? In this work we investigate the link between spoken words and actions in movies. We note that movie screenplays describe actions, as well as contain the speech of characters and hence can be used to learn this correlation with no additional supervision. We train a BERT-based Speech2Action classifier on over a thousand movie screenplays, to predict action labels from transcribed speech segments. We then apply this model to the speech segments of a large unlabelled movie corpus (188M speech segments from 288K movies). Using the predictions of this model, we obtain weak action labels for over 800K video clips. By training on these video clips, we demonstrate superior action recognition performance on standard action recognition benchmarks, without using a single manually labelled action example.

</details>

### Creating Something From Nothing: Unsupervised Knowledge Distillation for Cross-Modal Hashing.
- **链接**: [arXiv:2004.00280](https://arxiv.org/abs/2004.00280) · 📚 被引 115
- **作者**: Hengtong Hu, Lingxi Xie, Richang Hong, Qi Tian
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, cross-modal hashing (CMH) has attracted increasing attentions, mainly because its potential ability of mapping contents from different modalities, especially in vision and language, into the same space, so that it becomes efficient in cross-modal data retrieval. There are two main frameworks for CMH, differing from each other in whether semantic supervision is required. Compared to the unsupervised methods, the supervised methods often enjoy more accurate results, but require much heavier labors in data annotation. In this paper, we propose a novel approach that enables guiding a supervised method using outputs produced by an unsupervised method. Specifically, we make use of teacher-student optimization for propagating knowledge. Experiments are performed on two popular CMH benchmarks, i.e., the MIRFlickr and NUS-WIDE datasets. Our approach outperforms all existing unsupervised methods by a large margin.

</details>

## 跨领域论文（完整笔记在其他领域）

- nuScenes: A Multimodal Dataset for Autonomous Driving. → [autonomous-driving](../autonomous-driving/Guideline%202020.md)
