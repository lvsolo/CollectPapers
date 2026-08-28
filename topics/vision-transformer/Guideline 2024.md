# Vision Transformer — 2024 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLAMP-ViT: Contrastive Data-Free Learning for Adaptive Post-training Quantization of ViTs.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72855-6_18) · 📚 被引 11
- **作者**: Akshat Ramachandran, Souvik Kundu, Tushar Krishna
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Rotary Position Embedding for Vision Transformer.
- **链接**: [arXiv:2403.13298](https://arxiv.org/abs/2403.13298) · [代码](https://github.com/naver-ai/rope-vit) · 📚 被引 58
- **作者**: Byeongho Heo, Song Park, Dongyoon Han, Sangdoo Yun
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although Vision Transformer (ViT) has achieved significant success in computer vision, it does not perform well in dense prediction tasks due to the lack of inner-patch information interaction and the limited diversity of feature scale. Most existing studies are devoted to designing vision-specific transformers to solve the above problems, which introduce additional pre-training costs. Therefore, we present a plain, pre-training-free, and feature-enhanced ViT backbone with Convolutional Multi-scale feature interaction, named ViT-CoMer, which facilitates bidirectional interaction between CNN and transformer. Compared to the state-of-the-art, ViT-CoMer has the following advantages: (1) We inject spatial pyramid multi-receptive field convolutional features into the ViT architecture, which effectively alleviates the problems of limited local information interaction and single-feature representation in ViT. (2) We propose a simple and efficient CNN-Transformer bidirectional fusion interaction module that performs multi-scale fusion across hierarchical features, which is beneficial for handling dense prediction tasks. (3) We evaluate the performance of ViT-CoMer across various dense prediction tasks, different frameworks, and multiple advanced pre-training. Notably, our ViT-CoMer-L achieves 64.3% AP on COCO val2017 without extra training data, and 62.1% mIoU on ADE20K val, both of which are comparable to state-of-the-art methods. We hope ViT-CoMer can serve as a new backbone for dense prediction tasks to facilitate future research. The code will be released at https://github.com/Traffic-X/ViT-CoMer.

</details>

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Parameter-efficient fine-tuning for pre-trained Vision Transformers aims to adeptly tailor a model to downstream tasks by learning a minimal set of new adaptation parameters while preserving the frozen majority of pre-trained parameters. Striking a balance between retaining the generalizable representation capacity of the pre-trained model and acquiring task-specific features poses a key challenge. Currently, there is a lack of focus on guiding this delicate trade-off. In this study, we approach the problem from the perspective of Singular Value Decomposition (SVD) of pre-trained parameter matrices, providing insights into the tuning dynamics of existing methods. Building upon this understanding, we propose a Residual-based Low-Rank Rescaling (RLRR) fine-tuning strategy. This strategy not only enhances flexibility in parameter tuning but also ensures that new parameters do not deviate excessively from the pre-trained model through a residual design. Extensive experiments demonstrate that our method achieves competitive performance across various downstream image classification tasks, all while maintaining comparable new parameters. We believe this work takes a step forward in offering a unified perspective for interpreting existing methods and serves as motivation for the development of new approaches that move closer to effectively considering the crucial trade-off mentioned above. Our code is available at \href{https://github.com/zstarN70/RLRR.git}{https://github.com/zstarN70/RLRR.git}.

</details>

### AdanCA: Neural Cellular Automata As Adaptors For More Robust Vision Transformer.
- **链接**: [arXiv:2406.08298](https://arxiv.org/abs/2406.08298) · 📚 被引 1
- **作者**: Yitao Xu, Tong Zhang, Sabine Süsstrunk
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The remarkable success of Vision Transformers in Artificial Neural Networks (ANNs) has led to a growing interest in incorporating the self-attention mechanism and transformer-based architecture into Spiking Neural Networks (SNNs). While existing methods propose spiking self-attention mechanisms that are compatible with SNNs, they lack reasonable scaling methods, and the overall architectures proposed by these methods suffer from a bottleneck in effectively extracting local features. To address these challenges, we propose a novel spiking self-attention mechanism named Dual Spike Self-Attention (DSSA) with a reasonable scaling method. Based on DSSA, we propose a novel spiking Vision Transformer architecture called SpikingResformer, which combines the ResNet-based multi-stage architecture with our proposed DSSA to improve both performance and energy efficiency while reducing parameters. Experimental results show that SpikingResformer achieves higher accuracy with fewer parameters and lower energy consumption than other spiking Vision Transformer counterparts. Notably, our SpikingResformer-L achieves 79.40% top-1 accuracy on ImageNet with 4 time-steps, which is the state-of-the-art result in the SNN field.

</details>

> Vision Transformers (ViTs) demonstrate remarkable performance in image classification through visual-token interaction learning, particularly when equipped with local information via region attention or convolutions. Although such architectures improve the feature aggregation from different granularities, they often fail to contribute to the robustness of the networks. Neural Cellular Automata (NCA) enables the modeling of global visual-token representations through local interactions, with its training strategies and architecture design conferring strong generalization ability and robustness against noisy input. In this paper, we propose Adaptor Neural Cellular Automata (AdaNCA) for Vision Transformers that uses NCA as plug-and-play adaptors between ViT layers, thus enhancing ViT's performance and robustness against adversarial samples as well as out-of-distribution inputs. To overcome the large computational overhead of standard NCAs, we propose Dynamic Interaction for more efficient interaction learning. Using our analysis of AdaNCA placement and robustness improvement, we also develop an algorithm for identifying the most effective insertion points for AdaNCA. With less than a 3% increase in parameters, AdaNCA contributes to more than 10% absolute improvement in accuracy under adversarial attacks on the ImageNet1K benchmark. Moreover, we demonstrate with extensive evaluations across eight robustness benchmarks and four ViT architectures that AdaNCA, as a plug-and-play module, consistently improves the robustness of ViTs.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Transformers have rapidly gained popularity in various computer vision applications, post-hoc explanations of their internal mechanisms remain largely unexplored. Vision Transformers extract visual information by representing image regions as transformed tokens and integrating them via attention weights. However, existing post-hoc explanation methods merely consider these attention weights, neglecting crucial information from the transformed tokens, which fails to accurately illustrate the rationales behind the models' predictions. To incorporate the influence of token transformation into interpretation, we propose TokenTM, a novel post-hoc explanation method that utilizes our introduced measurement of token transformation effects. Specifically, we quantify token transformation effects by measuring changes in token lengths and correlations in their directions pre- and post-transformation. Moreover, we develop initialization and aggregation rules to integrate both attention weights and token transformation effects across all layers, capturing holistic token contributions throughout the model. Experimental results on segmentation and perturbation tests demonstrate the superiority of our proposed TokenTM compared to state-of-the-art Vision Transformer explanation methods.

</details>

### On the Faithfulness of Vision Transformer Explanations. **⭐⭐⭐** (相关度: 30%)
- **链接**: [arXiv:2404.01415](https://arxiv.org/abs/2404.01415) · 📚 被引 14
- **作者**: Junyi Wu, Weitai Kang, Hao Tang, Yuan Hong, Yan Yan
- **🏷️ 机构**: Illinois Institute of Technology,Department of Computer Science,USA, Robotics Institute, Carnegie Mellon University,USA, University of Connecticut,Department of Computer Science,USA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉Transformer解释方法忠实性评估不足的问题。②提出了Salience-guided Faithfulness Coefficient (SaCo)指标，通过成对比较像素组并聚合显著性差异来评估解释的忠实性。③相比现有指标，SaCo能有效区分高级解释方法与随机归因，提供更可靠的评估。④实验表明SaCo能可靠测量忠实性，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the underexplored faithfulness of Vision Transformer explanations by introducing SaCo, a metric that compares salience scores across pixel groups. SaCo reliably distinguishes advanced methods from random attribution, offering a robust evaluation. Specific performance numbers are not provided in the abstract.
- **核心贡献**: 提出SaCo指标用于评估ViT解释的忠实性。
- **创新点**: 基于显著性分布的成对比较聚合方法。
- **结果**: 能有效区分高级解释方法与随机归因。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To interpret Vision Transformers, post-hoc explanations assign salience scores to input pixels, providing human-understandable heatmaps. However, whether these interpretations reflect true rationales behind the model's output is still underexplored. To address this gap, we study the faithfulness criterion of explanations: the assigned salience scores should represent the influence of the corresponding input pixels on the model's predictions. To evaluate faithfulness, we introduce Salience-guided Faithfulness Coefficient (SaCo), a novel evaluation metric leveraging essential information of salience distribution. Specifically, we conduct pair-wise comparisons among distinct pixel groups and then aggregate the differences in their salience scores, resulting in a coefficient that indicates the explanation's degree of faithfulness. Our explorations reveal that current metrics struggle to differentiate between advanced explanation methods and Random Attribution, thereby failing to capture the faithfulness property. In contrast, our proposed SaCo offers a reliable faithfulness measurement, establishing a robust metric for interpretations. Furthermore, our SaCo demonstrates that the use of gradient and multi-layer aggregation can markedly enhance the faithfulness of attention-based explanation, shedding light on potential paths for advancing Vision Transformer explainability.

</details>

## 跨领域论文（完整笔记在其他领域）

### Fairness-Aware Vision Transformer via Debiased Self-Attention.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72913-3_20) · 📚 被引 4
- **作者**: Yao Qiang, Chengyin Li, Prashant Khanduri, Dongxiao Zhu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### Removing Rows and Columns of Tokens in Vision Transformer Enables Faster Dense Prediction Without Retraining.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73220-1_19) · 📚 被引 1
- **作者**: Diwei Su, Cheng Fei, Jianxu Luo
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### FairViT: Fair Vision Transformer via Adaptive Masking.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73650-6_26) · 📚 被引 5
- **作者**: Bowei Tian, Ruijie Du, Yanning Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

### GiT: Towards Generalist Vision Transformer Through Universal Language Interface.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-73397-0_4) · 📚 被引 6
- **作者**: Haiyang Wang, Hao Tang, Li Jiang, Shaoshuai Shi, Muhammad Ferjad Naeem, Hongsheng Li et al.
- **🏷️ 机构**: CUHK
- **会议**: ECCV 2024

### Parameter-Efficient and Memory-Efficient Tuning for Vision Transformer: A Disentangled Approach.
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72995-9_20)
- **作者**: Taolin Zhang, Jiawang Bai, Zhihe Lu, Dongze Lian, Genping Wang, Xinchao Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
