# Vision Transformer — 2024 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 18 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### H-ViT: A Hierarchical Vision Transformer for Deformable Image Registration. **⭐⭐** (相关度: 20%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01094) · 📚 被引 39
- **作者**: Morteza Ghahremani, Mohammad Khateri, Bailiang Jian, Benedikt Wiestler, Ehsan Adeli, Christian Wachinger
- **🏷️ 机构**: Technical University of Munich, University of Eastern Finland, Stanford University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对医学图像中可变形图像配准任务，现有方法难以有效建模大形变和复杂解剖结构对应关系。②提出了H-ViT，一种层级视觉Transformer架构，通过多尺度特征提取和全局-局部注意力机制来改进配准精度。③相比传统卷积网络和单尺度Transformer，H-ViT利用层级结构增强了对多尺度形变的感知能力。④摘要未提供具体数据，但实验表明在配准精度和鲁棒性上优于基线方法。
- **摘要（英）**: This paper addresses deformable image registration by proposing H-ViT, a hierarchical vision transformer that captures multi-scale features and global-local dependencies. It improves over CNN-based and single-scale transformer methods by better handling large deformations. Experiments show superior registration accuracy and robustness, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出层级视觉Transformer用于可变形图像配准，增强多尺度形变建模。
- **创新点**: 结合层级结构和全局-局部注意力机制处理复杂形变。
- **结果**: 在配准任务上取得优于基线的精度和鲁棒性。

### DeiT-LT: Distillation Strikes Back for Vision Transformer Training on Long-Tailed Datasets. **⭐⭐⭐** (相关度: 40%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02208) · 📚 被引 19
- **作者**: Harsh Rangwani, Pradipto Mondal, Mayank Mishra, Ashish Ramayee Asokan, R. Venkatesh Babu
- **🏷️ 机构**: Indian Institute of Science,Bangalore, Indian Institute of Technology,Kharagpur
- **会议**: CVPR 2024
- **摘要（中）**: ①针对长尾数据集上Vision Transformer训练困难、性能退化的问题，现有方法多依赖复杂重采样或损失调整。②提出了DeiT-LT，利用知识蒸馏策略，通过教师模型引导学生模型在长尾分布下学习，并设计了针对性的蒸馏损失。③相比传统长尾学习方法，该方法无需修改数据分布，仅通过蒸馏即可提升ViT在尾部类别的表现。④实验表明在多个长尾基准上显著优于现有ViT训练方法，具体准确率提升幅度未在摘要中给出。
- **摘要（英）**: This work tackles the challenge of training Vision Transformers on long-tailed datasets, where performance degrades on tail classes. DeiT-LT employs knowledge distillation with a tailored loss to transfer knowledge from a teacher to the student model, avoiding complex data rebalancing. It achieves significant improvements over existing ViT training methods on multiple benchmarks, though exact numbers are not specified.
- **核心贡献**: 提出DeiT-LT，用蒸馏策略提升ViT在长尾数据集上的训练效果。
- **创新点**: 设计针对长尾分布的蒸馏损失，无需修改数据分布。
- **结果**: 在长尾基准上显著优于现有ViT训练方法。

### ViT-CoMer: Vision Transformer with Convolutional Multi-scale Feature Interaction for Dense Predictions. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2403.07392](https://arxiv.org/abs/2403.07392) · 📚 被引 127
- **作者**: Chunlong Xia, Xinliang Wang, Feng Lv, Xin Hao, Yifeng Shi
- **🏷️ 机构**: Baidu Inc.
- **会议**: CVPR 2024
- **摘要（中）**: ①针对ViT在密集预测任务（如检测、分割）中缺乏内部patch信息交互和特征尺度多样性不足的问题。②提出了ViT-CoMer，一种无需预训练的ViT骨干，通过注入空间金字塔多感受野卷积特征，并设计CNN-Transformer双向融合交互模块，实现多尺度特征融合。③相比现有视觉专用Transformer，该方法无需额外预训练成本，且有效缓解了局部信息交互受限和特征表示单一的问题。④在多个密集预测基准上评估，性能优于现有最先进方法，具体数值未在摘要中完整给出。
- **摘要（英）**: ViT-CoMer addresses the limitations of ViT in dense prediction tasks, including insufficient inner-patch interaction and limited feature scale diversity. It injects spatial pyramid multi-receptive-field convolutional features and proposes a CNN-Transformer bidirectional fusion module for multi-scale interaction, all without requiring pre-training. This approach outperforms state-of-the-art methods on various dense prediction benchmarks, though exact metrics are incomplete in the abstract.
- **核心贡献**: 提出无需预训练的ViT骨干，通过卷积多尺度交互增强密集预测性能。
- **创新点**: 设计CNN-Transformer双向融合模块，实现跨层级多尺度特征交互。
- **结果**: 在多个密集预测任务上超越现有最先进方法。

### Progressive Semantic-Guided Vision Transformer for Zero-Shot Learning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02262) · 📚 被引 50
- **作者**: Shiming Chen, Wenjin Hou, Salman H. Khan, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI, Huazhong University of Science and Technology
- **会议**: CVPR 2024
- **摘要（中）**: ①针对零样本学习中视觉特征与语义属性对齐困难的问题。②提出了渐进式语义引导的视觉Transformer，通过逐步引入语义信息来引导特征学习。③相比传统零样本学习方法，该方法利用渐进策略增强语义与视觉的交互。④摘要未提供具体实验数据，但预期在零样本分类任务上有所提升。
- **摘要（英）**: This paper addresses zero-shot learning by proposing a progressive semantic-guided vision transformer that gradually incorporates semantic information to guide feature learning. It enhances semantic-visual interaction compared to traditional methods. Experiments are expected to show improvements in zero-shot classification, though no specific data is provided in the abstract.
- **核心贡献**: 提出渐进式语义引导的ViT用于零样本学习。
- **创新点**: 通过渐进策略融合语义信息到视觉特征。
- **结果**: 预期在零样本分类上提升，但缺乏具体数据。

### Low-Rank Rescaled Vision Transformer Fine-Tuning: A Residual Design Approach. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2403.19067](https://arxiv.org/abs/2403.19067) · 📚 被引 19
- **作者**: Wei Dong, Xing Zhang, Bihui Chen, Dawei Yan, Zhijun Lin, Qingsen Yan et al.
- **🏷️ 机构**: School of Computer Science and Engineering, University of Electronic Science and Technology of China, College of Information and Control Engineering, Xi&#x0027;an University of Architecture and Technology, School of Computer Science, Northwestern Polytechnical University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对预训练ViT微调时，在保留泛化能力与获取任务特定特征之间难以平衡的问题。②提出了基于残差设计的低秩重缩放（RLRR）微调策略，从预训练参数矩阵的SVD角度分析现有方法，并通过残差设计确保新参数不过度偏离预训练模型。③相比现有参数高效微调方法，RLRR增强了参数调整灵活性，同时保持模型稳定性。④在多个下游图像分类任务上，该方法以相当的新参数数量取得了有竞争力的性能。
- **摘要（英）**: This paper addresses the trade-off in fine-tuning pre-trained ViTs between retaining generalization and acquiring task-specific features. It proposes a Residual-based Low-Rank Rescaling (RLRR) strategy, grounded in SVD analysis, which enhances tuning flexibility while preventing deviation from the pre-trained model via residual design. Extensive experiments show competitive performance on various downstream classification tasks with comparable parameter counts.
- **核心贡献**: 提出RLRR微调策略，平衡泛化与任务适配。
- **创新点**: 基于SVD分析设计残差低秩重缩放。
- **结果**: 在多个分类任务上以相当参数取得竞争性能。

### Random Entangled Tokens for Adversarially Robust Vision Transformer. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02318) · 📚 被引 7
- **作者**: Huihui Gong, Minjing Dong, Siqi Ma, Seyit Camtepe, Surya Nepal, Chang Xu
- **🏷️ 机构**: The University of Sydney, City University of Hong Kong, The University of New South Wales
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉Transformer在对抗攻击下的鲁棒性问题。②提出了随机纠缠令牌（Random Entangled Tokens）方法，通过引入随机性来增强模型鲁棒性。③相比现有对抗训练方法，该方法无需额外训练成本，直接应用于预训练模型。④摘要未提供具体数据，效果未知。
- **摘要（英）**: This paper addresses the adversarial robustness of Vision Transformers by proposing Random Entangled Tokens, which introduce randomness to enhance robustness. It offers a training-free alternative to adversarial training. Specific performance metrics are not provided in the abstract.
- **核心贡献**: 提出随机纠缠令牌机制以提升ViT对抗鲁棒性。
- **创新点**: 利用令牌随机纠缠实现无需训练的鲁棒性增强。
- **结果**: 未报告具体效果数据。

### SpikingResformer: Bridging ResNet and Vision Transformer in Spiking Neural Networks. **⭐⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2403.14302](https://arxiv.org/abs/2403.14302) · 📚 被引 78
- **作者**: Xinyu Shi, Zecheng Hao, Zhaofei Yu
- **🏷️ 机构**: Institute for Artificial Intelligence, Peking University, School of Computer Science, Peking University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对脉冲神经网络（SNN）中视觉Transformer架构缺乏合理缩放方法和局部特征提取瓶颈的问题。②提出了双脉冲自注意力（DSSA）机制及其缩放方法，并构建了结合ResNet多阶段架构的SpikingResformer模型。③相比现有SNN Transformer，DSSA提供了合理的缩放，且多阶段架构增强了局部特征提取，同时减少参数和能耗。④SpikingResformer-L在ImageNet上以4个时间步达到79.40% top-1准确率，达到当前最优水平。
- **摘要（英）**: This paper tackles the lack of scaling methods and local feature extraction bottlenecks in spiking Vision Transformers. It proposes Dual Spike Self-Attention (DSSA) with a scaling method and a ResNet-based multi-stage architecture, SpikingResformer. The model achieves 79.40% top-1 accuracy on ImageNet with 4 time-steps, setting a new state-of-the-art with fewer parameters and lower energy consumption.
- **核心贡献**: 提出DSSA机制和SpikingResformer架构，提升SNN Transformer性能与效率。
- **创新点**: 设计双脉冲自注意力及合理缩放方法，结合多阶段架构。
- **结果**: ImageNet top-1准确率79.40%，参数和能耗更低。

### Token Transformation Matters: Towards Faithful Post-Hoc Explanation for Vision Transformer. **⭐⭐⭐** (相关度: 35%)
- **链接**: [arXiv:2403.14552](https://arxiv.org/abs/2403.14552) · 📚 被引 15
- **作者**: Junyi Wu, Bin Duan, Weitai Kang, Hao Tang, Yan Yan
- **🏷️ 机构**: Illinois Institute of Technology,Department of Computer Science,USA, Robotics Institute, Carnegie Mellon University,USA
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉Transformer事后解释方法仅考虑注意力权重而忽略令牌变换信息的问题。②提出了TokenTM方法，通过量化令牌变换效应（长度和方向变化）并结合注意力权重进行逐层聚合。③相比现有方法，TokenTM更全面地捕捉令牌贡献，提高解释的忠实性。④在分割和扰动测试中表现优越，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the limitation of post-hoc explanation methods for Vision Transformers that ignore token transformation information. It proposes TokenTM, which quantifies token transformation effects and integrates them with attention weights across layers. Experiments on segmentation and perturbation tests show superior performance, though specific metrics are not detailed.
- **核心贡献**: 提出TokenTM方法，融合令牌变换效应以提升解释忠实性。
- **创新点**: 量化令牌变换效应并设计聚合规则。
- **结果**: 在分割和扰动测试中表现优越。

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

## 跨领域论文（完整笔记在其他领域）

- HEAL-SWIN: A Vision Transformer on the Sphere. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Open Vocabulary Semantic Scene Sketch Understanding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Question Aware Vision Transformer for Multimodal Reasoning. → [multimodal](../multimodal/Guideline%202024.md)
- Once for Both: Single Stage of Importance and Sparsity Search for Vision Transformer Compression. → [network-pruning](../network-pruning/Guideline%202024.md)
- SHViT: Single-Head Vision Transformer with Memory Efficient Macro Design. → [object-detection](../object-detection/Guideline%202024.md)
- Dense Vision Transformer Compression with Few Samples. → [network-pruning](../network-pruning/Guideline%202024.md)
- Zero-TPrune: Zero-Shot Token Pruning Through Leveraging of the Attention Graph in Pre-Trained Transformers. → [network-pruning](../network-pruning/Guideline%202024.md)
