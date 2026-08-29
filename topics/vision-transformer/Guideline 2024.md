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

> Rotary Position Embedding (RoPE) performs remarkably on language models, especially for length extrapolation of Transformers. However, the impacts of RoPE on computer vision domains have been underexplored, even though RoPE appears capable of enhancing Vision Transformer (ViT) performance in a way similar to the language domain. This study provides a comprehensive analysis of RoPE when applied to ViTs, utilizing practical implementations of RoPE for 2D vision data. The analysis reveals that RoPE demonstrates impressive extrapolation performance, i.e., maintaining precision while increasing image resolution at inference. It eventually leads to performance improvement for ImageNet-1k, COCO detection, and ADE-20k segmentation. We believe this study provides thorough guidelines to apply RoPE into ViT, promising improved backbone performance with minimal extra computational overhead. Our code and pre-trained models are available at https://github.com/naver-ai/rope-vit

</details>

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) are increasingly used in computer vision due to their high performance, but their vulnerability to adversarial attacks is a concern. Existing methods lack a solid theoretical basis, focusing mainly on empirical training adjustments. This study introduces SpecFormer, tailored to fortify ViTs against adversarial attacks, with theoretical underpinnings. We establish local Lipschitz bounds for the self-attention layer and propose the Maximum Singular Value Penalization (MSVP) to precisely manage these bounds By incorporating MSVP into ViTs' attention layers, we enhance the model's robustness without compromising training efficiency. SpecFormer, the resulting model, outperforms other state-of-the-art models in defending against adversarial attacks, as proven by experiments on CIFAR and ImageNet datasets. Code is released at https://github.com/microsoft/robustlearn.

</details>

### AdanCA: Neural Cellular Automata As Adaptors For More Robust Vision Transformer.
- **链接**: [arXiv:2406.08298](https://arxiv.org/abs/2406.08298) · 📚 被引 1
- **作者**: Yitao Xu, Tong Zhang, Sabine Süsstrunk
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

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

## 🆕 增量新增

### HEAL-SWIN: A Vision Transformer on the Sphere. **⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2307.07313](https://arxiv.org/abs/2307.07313) · 📚 被引 9
- **作者**: Oscar Carlsson, Jan E. Gerken, Hampus Linander, Heiner Spieß, Fredrik Ohlsson, Christoffer Petersson et al.
- **🏷️ 机构**: Chalmers University of Tech-nology, University of Gothenburg,Department of Mathematical Sciences,Gothenburg,Sweden,SE-41296, Neural Information Processing, Science of Intelligence, Technical University Berlin,Berlin,Germany,DE-10623, Ume&#x00E5; Uni-versity,Department of Mathematics and Mathematical Statistics,Ume&#x00E5;,Sweden,SE-90187
- **会议**: CVPR 2024
- **摘要（中）**: 针对高分辨率广角鱼眼图像在平面投影中引入畸变和损失的问题，提出了HEAL-SWIN transformer，结合HEALPix网格和SWIN transformer，实现无畸变的球形数据处理。利用HEALPix的嵌套结构进行SWIN的patch和window操作，最小化计算开销。在合成和真实自动驾驶数据集上，该模型在语义分割、深度回归和分类任务上表现优越。
- **摘要（英）**: To address the distortion and loss issues when projecting high-resolution fisheye images onto planar grids, this paper proposes HEAL-SWIN, combining the HEALPix grid with the SWIN transformer for distortion-free spherical data processing. The nested structure of HEALPix enables efficient patching and windowing, minimizing computational overhead. The model demonstrates superior performance on synthetic and real automotive datasets for segmentation, depth regression, and classification.
- **核心贡献**: 提出了基于HEALPix的球形视觉transformer，适用于高分辨率鱼眼图像。
- **创新点**: 将HEALPix网格与SWIN transformer结合，实现无畸变球形处理。
- **结果**: 在多个任务上取得优于现有方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution wide-angle fisheye images are becoming more and more important for robotics applications such as autonomous driving. However, using ordinary convolutional neural networks or vision transformers on this data is problematic due to projection and distortion losses introduced when projecting to a rectangular grid on the plane. We introduce the HEAL-SWIN transformer, which combines the highly uniform Hierarchical Equal Area iso-Latitude Pixelation (HEALPix) grid used in astrophysics and cosmology with the Hierarchical Shifted-Window (SWIN) transformer to yield an efficient and flexible model capable of training on high-resolution, distortion-free spherical data. In HEAL-SWIN, the nested structure of the HEALPix grid is used to perform the patching and windowing operations of the SWIN transformer, enabling the network to process spherical representations with minimal computational overhead. We demonstrate the superior performance of our model on both synthetic and real automotive datasets, as well as a selection of other image datasets, for semantic segmentation, depth regression and classification tasks. Our code is publicly available at https://github.com/JanEGerken/HEAL-SWIN.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Although Vision Transformer (ViT) has achieved significant success in computer vision, it does not perform well in dense prediction tasks due to the lack of inner-patch information interaction and the limited diversity of feature scale. Most existing studies are devoted to designing vision-specific transformers to solve the above problems, which introduce additional pre-training costs. Therefore, we present a plain, pre-training-free, and feature-enhanced ViT backbone with Convolutional Multi-scale feature interaction, named ViT-CoMer, which facilitates bidirectional interaction between CNN and transformer. Compared to the state-of-the-art, ViT-CoMer has the following advantages: (1) We inject spatial pyramid multi-receptive field convolutional features into the ViT architecture, which effectively alleviates the problems of limited local information interaction and single-feature representation in ViT. (2) We propose a simple and efficient CNN-Transformer bidirectional fusion interaction module that performs multi-scale fusion across hierarchical features, which is beneficial for handling dense prediction tasks. (3) We evaluate the performance of ViT-CoMer across various dense prediction tasks, different frameworks, and multiple advanced pre-training. Notably, our ViT-CoMer-L achieves 64.3% AP on COCO val2017 without extra training data, and 62.1% mIoU on ADE20K val, both of which are comparable to state-of-the-art methods. We hope ViT-CoMer can serve as a new backbone for dense prediction tasks to facilitate future research. The code will be released at https://github.com/Traffic-X/ViT-CoMer.

</details>

### LUM-ViT: Learnable Under-sampling Mask Vision Transformer for Bandwidth Limited Optical Signal Acquisition. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2403.01412](https://arxiv.org/abs/2403.01412)
- **作者**: Lingfeng Liu, Dong Ni, Hangjie Yuan
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024
- **摘要（中）**: ①针对高光谱等信号采集带宽受限导致实时检测困难的问题。②提出了LUM-ViT，一种带有可学习欠采样掩码的ViT变体，通过预采集调制减少采集数据量，并采用核级权重二值化和三阶段微调策略优化光学计算。③相比传统全采样方法，仅采样10%像素即可保持高精度，显著降低带宽需求。④在ImageNet分类任务上，采样10%像素时精度损失仅1.8%，并在真实光学硬件上保持近原始精度。
- **摘要（英）**: This paper tackles bandwidth constraints in signal acquisition, such as hyperspectral imaging, which hinder real-time detection. It introduces LUM-ViT, a ViT variant with a learnable under-sampling mask for pre-acquisition modulation, plus kernel-level weight binarization and three-stage fine-tuning. Sampling only 10% of pixels, it maintains accuracy within 1.8% on ImageNet and near-original accuracy on real optical hardware.
- **核心贡献**: 提出可学习欠采样掩码的ViT用于带宽受限信号采集。
- **创新点**: 预采集调制与核级二值化结合，实现极低采样率下的高精度。
- **结果**: 10%采样下精度损失1.8%，硬件实现有效。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Bandwidth constraints during signal acquisition frequently impede real-time detection applications. Hyperspectral data is a notable example, whose vast volume compromises real-time hyperspectral detection. To tackle this hurdle, we introduce a novel approach leveraging pre-acquisition modulation to reduce the acquisition volume. This modulation process is governed by a deep learning model, utilizing prior information. Central to our approach is LUM-ViT, a Vision Transformer variant. Uniquely, LUM-ViT incorporates a learnable under-sampling mask tailored for pre-acquisition modulation. To further optimize for optical calculations, we propose a kernel-level weight binarization technique and a three-stage fine-tuning strategy. Our evaluations reveal that, by sampling a mere 10% of the original image pixels, LUM-ViT maintains the accuracy loss within 1.8% on the ImageNet classification task. The method sustains near-original accuracy when implemented on real-world optical hardware, demonstrating its practicality. Code will be available at https://github.com/MaxLLF/LUM-ViT.

</details>

### Question Aware Vision Transformer for Multimodal Reasoning. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2402.05472](https://arxiv.org/abs/2402.05472) · 📚 被引 23
- **作者**: Roy Ganz, Yair Kittenplon, Aviad Aberdam, Elad Ben-Avraham, Oren Nuriel, Shai Mazor et al.
- **🏷️ 机构**: Technion,Israel, AWS AI Labs
- **会议**: CVPR 2024
- **摘要（中）**: ①针对视觉-语言模型中视觉编码过程与用户查询解耦，导致视觉特征未能针对问题相关图像区域优化的问题。②提出了QA-ViT，一种问题感知的视觉Transformer，将问题信息直接嵌入视觉编码器，生成动态视觉特征，聚焦于与问题相关的图像方面。③该方法模型无关，可高效集成到任何VL架构中，相比现有方法无需修改LLM或投影模块。④大量实验表明，在多种多模态架构和任务上均取得一致改进，尤其在视觉和场景文本理解方面表现突出。
- **摘要（英）**: QA-ViT addresses the decoupling of vision encoding from user queries in vision-language models by embedding question awareness directly into the vision encoder, producing dynamic features focused on query-relevant image regions. It is model-agnostic and integrates efficiently into any VL architecture. Extensive experiments show consistent improvements across diverse multimodal tasks, particularly in visual and scene-text understanding.
- **核心贡献**: 提出问题感知视觉Transformer，动态调整视觉特征以匹配查询。
- **创新点**: 在视觉编码器内嵌入问题信息，实现查询驱动的特征提取。
- **结果**: 在多种多模态任务上取得一致性能提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language (VL) models have gained significant research focus, enabling remarkable advances in multimodal reasoning. These architectures typically comprise a vision encoder, a Large Language Model (LLM), and a projection module that aligns visual features with the LLM's representation space. Despite their success, a critical limitation persists: the vision encoding process remains decoupled from user queries, often in the form of image-related questions. Consequently, the resulting visual features may not be optimally attuned to the query-specific elements of the image. To address this, we introduce QA-ViT, a Question Aware Vision Transformer approach for multimodal reasoning, which embeds question awareness directly within the vision encoder. This integration results in dynamic visual features focusing on relevant image aspects to the posed question. QA-ViT is model-agnostic and can be incorporated efficiently into any VL architecture. Extensive experiments demonstrate the effectiveness of applying our method to various multimodal architectures, leading to consistent improvement across diverse tasks and showcasing its potential for enhancing visual and scene-text understanding.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Parameter-efficient fine-tuning for pre-trained Vision Transformers aims to adeptly tailor a model to downstream tasks by learning a minimal set of new adaptation parameters while preserving the frozen majority of pre-trained parameters. Striking a balance between retaining the generalizable representation capacity of the pre-trained model and acquiring task-specific features poses a key challenge. Currently, there is a lack of focus on guiding this delicate trade-off. In this study, we approach the problem from the perspective of Singular Value Decomposition (SVD) of pre-trained parameter matrices, providing insights into the tuning dynamics of existing methods. Building upon this understanding, we propose a Residual-based Low-Rank Rescaling (RLRR) fine-tuning strategy. This strategy not only enhances flexibility in parameter tuning but also ensures that new parameters do not deviate excessively from the pre-trained model through a residual design. Extensive experiments demonstrate that our method achieves competitive performance across various downstream image classification tasks, all while maintaining comparable new parameters. We believe this work takes a step forward in offering a unified perspective for interpreting existing methods and serves as motivation for the development of new approaches that move closer to effectively considering the crucial trade-off mentioned above. Our code is available at \href{https://github.com/zstarN70/RLRR.git}{https://github.com/zstarN70/RLRR.git}.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The remarkable success of Vision Transformers in Artificial Neural Networks (ANNs) has led to a growing interest in incorporating the self-attention mechanism and transformer-based architecture into Spiking Neural Networks (SNNs). While existing methods propose spiking self-attention mechanisms that are compatible with SNNs, they lack reasonable scaling methods, and the overall architectures proposed by these methods suffer from a bottleneck in effectively extracting local features. To address these challenges, we propose a novel spiking self-attention mechanism named Dual Spike Self-Attention (DSSA) with a reasonable scaling method. Based on DSSA, we propose a novel spiking Vision Transformer architecture called SpikingResformer, which combines the ResNet-based multi-stage architecture with our proposed DSSA to improve both performance and energy efficiency while reducing parameters. Experimental results show that SpikingResformer achieves higher accuracy with fewer parameters and lower energy consumption than other spiking Vision Transformer counterparts. Notably, our SpikingResformer-L achieves 79.40% top-1 accuracy on ImageNet with 4 time-steps, which is the state-of-the-art result in the SNN field.

</details>

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

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Transformers have rapidly gained popularity in various computer vision applications, post-hoc explanations of their internal mechanisms remain largely unexplored. Vision Transformers extract visual information by representing image regions as transformed tokens and integrating them via attention weights. However, existing post-hoc explanation methods merely consider these attention weights, neglecting crucial information from the transformed tokens, which fails to accurately illustrate the rationales behind the models' predictions. To incorporate the influence of token transformation into interpretation, we propose TokenTM, a novel post-hoc explanation method that utilizes our introduced measurement of token transformation effects. Specifically, we quantify token transformation effects by measuring changes in token lengths and correlations in their directions pre- and post-transformation. Moreover, we develop initialization and aggregation rules to integrate both attention weights and token transformation effects across all layers, capturing holistic token contributions throughout the model. Experimental results on segmentation and perturbation tests demonstrate the superiority of our proposed TokenTM compared to state-of-the-art Vision Transformer explanation methods.

</details>

### SHViT: Single-Head Vision Transformer with Memory Efficient Macro Design. **⭐⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2401.16456](https://arxiv.org/abs/2401.16456) · 📚 被引 174
- **作者**: Seokju Yun, Youngmin Ro
- **🏷️ 机构**: University of Seoul,Machine Intelligence Laboratory,Korea
- **会议**: CVPR 2024
- **摘要（中）**: ①针对高效视觉Transformer在宏微设计层面存在计算冗余的问题。②提出了SHViT架构，采用大步长patchify stem、早期卷积替代注意力、单头注意力模块等设计。③相比现有高效ViT，SHViT减少内存访问成本并消除头部冗余，同时并行结合全局和局部信息提升精度。④在ImageNet-1k上，SHViT-S实现了最先进的精度-速度权衡，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses computational redundancy in efficient Vision Transformers by proposing SHViT, which uses larger-stride patchify, early convolutions, and a single-head attention module. These designs reduce memory costs and head redundancy while improving accuracy. SHViT-S achieves state-of-the-art speed-accuracy tradeoff on ImageNet-1k, though specific numbers are not detailed.
- **核心贡献**: 提出SHViT架构，实现高效内存利用和最优速度-精度权衡。
- **创新点**: 单头注意力模块并行融合全局与局部信息。
- **结果**: 在ImageNet-1k上达到最先进的速度-精度权衡。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, efficient Vision Transformers have shown great performance with low latency on resource-constrained devices. Conventionally, they use 4x4 patch embeddings and a 4-stage structure at the macro level, while utilizing sophisticated attention with multi-head configuration at the micro level. This paper aims to address computational redundancy at all design levels in a memory-efficient manner. We discover that using larger-stride patchify stem not only reduces memory access costs but also achieves competitive performance by leveraging token representations with reduced spatial redundancy from the early stages. Furthermore, our preliminary analyses suggest that attention layers in the early stages can be substituted with convolutions, and several attention heads in the latter stages are computationally redundant. To handle this, we introduce a single-head attention module that inherently prevents head redundancy and simultaneously boosts accuracy by parallelly combining global and local information. Building upon our solutions, we introduce SHViT, a Single-Head Vision Transformer that obtains the state-of-the-art speed-accuracy tradeoff. For example, on ImageNet-1k, our SHViT-S4 is 3.3x, 8.1x, and 2.4x faster than MobileViTv2 x1.0 on GPU, CPU, and iPhone12 mobile device, respectively, while being 1.3% more accurate. For object detection and instance segmentation on MS COCO using Mask-RCNN head, our model achieves performance comparable to FastViT-SA12 while exhibiting 3.8x and 2.0x lower backbone latency on GPU and mobile device, respectively.

</details>

### SpecFormer: Guarding Vision Transformer Robustness via Maximum Singular Value Penalization. **⭐⭐⭐** (相关度: 45%)
- **链接**: [arXiv:2402.03317](https://arxiv.org/abs/2402.03317) · 📚 被引 1
- **作者**: Xixu Hu, Runkai Zheng, Jindong Wang, Cheuk Hang Leung, Qi Wu, Xing Xie
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对视觉Transformer易受对抗攻击且现有防御方法缺乏理论依据的问题。②提出了SpecFormer，通过最大奇异值惩罚（MSVP）精确控制自注意力层的局部Lipschitz界，增强鲁棒性。③相比经验性训练调整，该方法有坚实理论基础，且不牺牲训练效率。④在CIFAR和ImageNet数据集上，SpecFormer在对抗防御上优于现有最先进方法。
- **摘要（英）**: This paper addresses the vulnerability of Vision Transformers to adversarial attacks, where existing defenses lack theoretical basis. It introduces SpecFormer with Maximum Singular Value Penalization (MSVP) to control local Lipschitz bounds of self-attention layers. It outperforms state-of-the-art defenses on CIFAR and ImageNet without compromising efficiency.
- **核心贡献**: 提出基于Lipschitz界约束的ViT对抗防御方法。
- **创新点**: 通过MSVP精确管理自注意力层的鲁棒性边界。
- **结果**: 在多个数据集上优于现有防御方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) are increasingly used in computer vision due to their high performance, but their vulnerability to adversarial attacks is a concern. Existing methods lack a solid theoretical basis, focusing mainly on empirical training adjustments. This study introduces SpecFormer, tailored to fortify ViTs against adversarial attacks, with theoretical underpinnings. We establish local Lipschitz bounds for the self-attention layer and propose the Maximum Singular Value Penalization (MSVP) to precisely manage these bounds By incorporating MSVP into ViTs' attention layers, we enhance the model's robustness without compromising training efficiency. SpecFormer, the resulting model, outperforms other state-of-the-art models in defending against adversarial attacks, as proven by experiments on CIFAR and ImageNet datasets. Code is released at https://github.com/microsoft/robustlearn.

</details>

### Token Compensator: Altering Inference Cost of Vision Transformer Without Re-tuning. **⭐⭐** (相关度: 30%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-72640-8_5) · 📚 被引 4
- **作者**: Shibo Jie, Yehui Tang, Jianyuan Guo, Zhi-Hong Deng, Kai Han, Yunhe Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024
- **摘要（中）**: ①针对视觉Transformer推理成本高且调整需要重新训练的问题。②提出了Token Compensator，一种无需重新训练即可改变推理成本的方法。③相比现有剪枝或蒸馏方法，该方法避免重新训练，但摘要信息有限。④具体效果未在摘要中提供，需进一步查阅全文。
- **摘要（英）**: This paper addresses high inference costs of Vision Transformers and the need for re-tuning. It proposes Token Compensator to alter inference cost without re-training. Details on effectiveness are limited in the abstract.
- **核心贡献**: 提出无需重新训练的ViT推理成本调整方法。
- **创新点**: 通过token补偿机制实现成本调整。
- **结果**: 未提供具体数据。

### Siamese Vision Transformers are Scalable Audio-Visual Learners.
- **链接**: [arXiv:2403.19638](https://arxiv.org/abs/2403.19638) · 📚 被引 4
- **作者**: Yan-Bo Lin, Gedas Bertasius
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Traditional audio-visual methods rely on independent audio and visual backbones, which is costly and not scalable. In this work, we investigate using an audio-visual siamese network (AVSiam) for efficient and scalable audio-visual pretraining. Our framework uses a single shared vision transformer backbone to process audio and visual inputs, improving its parameter efficiency, reducing the GPU memory footprint, and allowing us to scale our method to larger datasets and model sizes. We pretrain our model using a contrastive audio-visual matching objective with a multi-ratio random masking scheme, which enables our model to process larger audio-visual instance batches, helpful for contrastive learning. Unlike prior audio-visual methods, our method can robustly handle audio, visual, and audio-visual inputs with a single shared ViT backbone. Furthermore, despite using the shared backbone for both modalities, AVSiam achieves competitive or even better results than prior methods on AudioSet and VGGSound for audio-visual classification and retrieval. Our code is available at https://github.com/GenjiB/AVSiam

</details>

### CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction.
- **链接**: [arXiv:2310.01403](https://arxiv.org/abs/2310.01403)
- **作者**: Size Wu, Wenwei Zhang, Lumin Xu, Sheng Jin, Xiangtai Li, Wentao Liu et al.
- **🏷️ 机构**: NTU S-Lab
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary dense prediction tasks including object detection and image segmentation have been advanced by the success of Contrastive Language-Image Pre-training (CLIP). CLIP models, particularly those incorporating vision transformers (ViTs), have exhibited remarkable generalization ability in zero-shot image classification. However, when transferring the vision-language alignment of CLIP from global image representation to local region representation for the open-vocabulary dense prediction tasks, CLIP ViTs suffer from the domain shift from full images to local image regions. In this paper, we embark on an in-depth analysis of the region-language alignment in CLIP models, which is essential for downstream open-vocabulary dense prediction tasks. Subsequently, we propose an approach named CLIPSelf, which adapts the image-level recognition ability of CLIP ViT to local image regions without needing any region-text pairs. CLIPSelf empowers ViTs to distill itself by aligning a region representation extracted from its dense feature map with the image-level representation of the corresponding image crop. With the enhanced CLIP ViTs, we achieve new state-of-the-art performance on open-vocabulary object detection, semantic segmentation, and panoptic segmentation across various benchmarks. Models and code are released at https://github.com/wusize/CLIPSelf.

</details>

### A Simple Romance Between Multi-Exit Vision Transformer and Token Reduction.
- **链接**: [出版页](https://openreview.net/forum?id=gJeYtRuguR)
- **作者**: Dongyang Liu, Meina Kan, Shiguang Shan, Xilin Chen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### Learning Adaptive and View-Invariant Vision Transformer for Real-Time UAV Tracking.
- **链接**: [出版页](https://proceedings.mlr.press/v235/li24ax.html) · 📚 被引 15
- **作者**: Yongxin Li, Mengyuan Liu, You Wu, Xucheng Wang, Xiangyang Yang, Shuiwang Li
- **🏷️ 机构**: College of Computer Science and Engineering, Guilin University of Technology, Guilin, China, School of Computer Science, Fudan University, Shanghai, China, School of Artificial Intelligence, Sun Yat-sen University, Zhuhai, China
- **会议**: ICML 2024

### GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer.
- **链接**: [arXiv:2406.01210](https://arxiv.org/abs/2406.01210)
- **作者**: Ding Jia, Jianyuan Guo, Kai Han, Han Wu, Chao Zhang, Chang Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-modal transformers have demonstrated superiority in various vision tasks by effectively integrating different modalities. This paper first critiques prior token exchange methods which replace less informative tokens with inter-modal features, and demonstrate exchange based methods underperform cross-attention mechanisms, while the computational demand of the latter inevitably restricts its use with longer sequences. To surmount the computational challenges, we propose GeminiFusion, a pixel-wise fusion approach that capitalizes on aligned cross-modal representations. GeminiFusion elegantly combines intra-modal and inter-modal attentions, dynamically integrating complementary information across modalities. We employ a layer-adaptive noise to adaptively control their interplay on a per-layer basis, thereby achieving a harmonized fusion process. Notably, GeminiFusion maintains linear complexity with respect to the number of input tokens, ensuring this multimodal framework operates with efficiency comparable to unimodal networks. Comprehensive evaluations across multimodal image-to-image translation, 3D object detection and arbitrary-modal semantic segmentation tasks, including RGB, depth, LiDAR, event data, etc. demonstrate the superior performance of our GeminiFusion against leading-edge techniques. The PyTorch code is available at https://github.com/JiaDingCN/GeminiFusion

</details>

### FiT: Flexible Vision Transformer for Diffusion Model.
- **链接**: [arXiv:2402.12376](https://arxiv.org/abs/2402.12376)
- **作者**: Zeyu Lu, Zidong Wang, Di Huang, Chengyue Wu, Xihui Liu, Wanli Ouyang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Nature is infinitely resolution-free. In the context of this reality, existing diffusion models, such as Diffusion Transformers, often face challenges when processing image resolutions outside of their trained domain. To overcome this limitation, we present the Flexible Vision Transformer (FiT), a transformer architecture specifically designed for generating images with unrestricted resolutions and aspect ratios. Unlike traditional methods that perceive images as static-resolution grids, FiT conceptualizes images as sequences of dynamically-sized tokens. This perspective enables a flexible training strategy that effortlessly adapts to diverse aspect ratios during both training and inference phases, thus promoting resolution generalization and eliminating biases induced by image cropping. Enhanced by a meticulously adjusted network structure and the integration of training-free extrapolation techniques, FiT exhibits remarkable flexibility in resolution extrapolation generation. Comprehensive experiments demonstrate the exceptional performance of FiT across a broad range of resolutions, showcasing its effectiveness both within and beyond its training resolution distribution. Repository available at https://github.com/whlzy/FiT.

</details>

### Outlier-aware Slicing for Post-Training Quantization in Vision Transformer.
- **链接**: [出版页](https://proceedings.mlr.press/v235/ma24f.html)
- **作者**: Yuexiao Ma, Huixia Li, Xiawu Zheng, Feng Ling, Xuefeng Xiao, Rui Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### Enhancing Vision Transformer: Amplifying Non-Linearity in Feedforward Network Module.
- **链接**: [出版页](https://proceedings.mlr.press/v235/xu24n.html)
- **作者**: Yixing Xu, Chao Li, Dong Li, Xiao Sheng, Fan Jiang, Lu Tian et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2024

### InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD.
- **链接**: [arXiv:2404.06512](https://arxiv.org/abs/2404.06512) · 📚 被引 12
- **作者**: Xiaoyi Dong, Pan Zhang, Yuhang Zang, Yuhang Cao, Bin Wang, Linke Ouyang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The Large Vision-Language Model (LVLM) field has seen significant advancements, yet its progression has been hindered by challenges in comprehending fine-grained visual content due to limited resolution. Recent efforts have aimed to enhance the high-resolution understanding capabilities of LVLMs, yet they remain capped at approximately 1500 x 1500 pixels and constrained to a relatively narrow resolution range. This paper represents InternLM-XComposer2-4KHD, a groundbreaking exploration into elevating LVLM resolution capabilities up to 4K HD (3840 x 1600) and beyond. Concurrently, considering the ultra-high resolution may not be necessary in all scenarios, it supports a wide range of diverse resolutions from 336 pixels to 4K standard, significantly broadening its scope of applicability. Specifically, this research advances the patch division paradigm by introducing a novel extension: dynamic resolution with automatic patch configuration. It maintains the training image aspect ratios while automatically varying patch counts and configuring layouts based on a pre-trained Vision Transformer (ViT) (336 x 336), leading to dynamic training resolution from 336 pixels to 4K standard. Our research demonstrates that scaling training resolution up to 4K HD leads to consistent performance enhancements without hitting the ceiling of potential improvements. InternLM-XComposer2-4KHD shows superb capability that matches or even surpasses GPT-4V and Gemini Pro in 10 of the 16 benchmarks. The InternLM-XComposer2-4KHD model series with 7B parameters are publicly available at https://github.com/InternLM/InternLM-XComposer.

</details>

### Visual Anchors Are Strong Information Aggregators For Multimodal Large Language Model.
- **链接**: [arXiv:2405.17815](https://arxiv.org/abs/2405.17815)
- **作者**: Haogeng Liu, Quanzeng You, Xiaotian Han, Yongfei Liu, Huaibo Huang, Ran He et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In the realm of Multimodal Large Language Models (MLLMs), vision-language connector plays a crucial role to link the pre-trained vision encoders with Large Language Models (LLMs). Despite its importance, the vision-language connector has been relatively less explored. In this study, we aim to propose a strong vision-language connector that enables MLLMs to achieve high accuracy while maintain low computation cost. We first reveal the existence of the visual anchors in Vision Transformer and propose a cost-effective search algorithm to extract them. Building on these findings, we introduce the Anchor Former (AcFormer), a novel vision-language connector designed to leverage the rich prior knowledge obtained from these visual anchors during pretraining, guiding the aggregation of information. Through extensive experimentation, we demonstrate that the proposed method significantly reduces computational costs by nearly two-thirds compared with baseline, while simultaneously outperforming baseline methods. This highlights the effectiveness and efficiency of AcFormer. Codes are available at https://github.com/liuhaogeng/Anchor-Former.

</details>

### Efficient Adaptation of Pre-trained Vision Transformer via Householder Transformation.
- **链接**: [arXiv:2410.22952](https://arxiv.org/abs/2410.22952) · 📚 被引 2
- **作者**: Wei Dong, Yuan Sun, Yiting Yang, Xing Zhang, Zhijun Lin, Qingsen Yan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> A common strategy for Parameter-Efficient Fine-Tuning (PEFT) of pre-trained Vision Transformers (ViTs) involves adapting the model to downstream tasks by learning a low-rank adaptation matrix. This matrix is decomposed into a product of down-projection and up-projection matrices, with the bottleneck dimensionality being crucial for reducing the number of learnable parameters, as exemplified by prevalent methods like LoRA and Adapter. However, these low-rank strategies typically employ a fixed bottleneck dimensionality, which limits their flexibility in handling layer-wise variations. To address this limitation, we propose a novel PEFT approach inspired by Singular Value Decomposition (SVD) for representing the adaptation matrix. SVD decomposes a matrix into the product of a left unitary matrix, a diagonal matrix of scaling values, and a right unitary matrix. We utilize Householder transformations to construct orthogonal matrices that efficiently mimic the unitary matrices, requiring only a vector. The diagonal values are learned in a layer-wise manner, allowing them to flexibly capture the unique properties of each layer. This approach enables the generation of adaptation matrices with varying ranks across different layers, providing greater flexibility in adapting pre-trained models. Experiments on standard downstream vision tasks demonstrate that our method achieves promising fine-tuning performance.

</details>

### Boosting the Transferability of Adversarial Attack on Vision Transformer with Adaptive Token Tuning.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/24f8dd1b8f154f1ee0d7a59e368eccf3-Abstract-Conference.html) · 📚 被引 8
- **作者**: Di Ming, Peng Ren, Yunlong Wang, Xin Feng
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

### Slicing Vision Transformer for Flexible Inference.
- **链接**: [arXiv:2412.04786](https://arxiv.org/abs/2412.04786)
- **作者**: Yitian Zhang, Huseyin Coskun, Xu Ma, Huan Wang, Ke Ma, Xi Stephen Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViT) is known for its scalability. In this work, we target to scale down a ViT to fit in an environment with dynamic-changing resource constraints. We observe that smaller ViTs are intrinsically the sub-networks of a larger ViT with different widths. Thus, we propose a general framework, named Scala, to enable a single network to represent multiple smaller ViTs with flexible inference capability, which aligns with the inherent design of ViT to vary from widths. Concretely, Scala activates several subnets during training, introduces Isolated Activation to disentangle the smallest sub-network from other subnets, and leverages Scale Coordination to ensure each sub-network receives simplified, steady, and accurate learning objectives. Comprehensive empirical validations on different tasks demonstrate that with only one-shot training, Scala learns slimmable representation without modifying the original ViT structure and matches the performance of Separate Training. Compared with the prior art, Scala achieves an average improvement of 1.6% on ImageNet-1K with fewer parameters.

</details>

### Transforming Vision Transformer: Towards Efficient Multi-Task Asynchronous Learner.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2024/hash/93fab021315170101c92e8330a56fbdb-Abstract-Conference.html) · 📚 被引 2
- **作者**: Hanwen Zhong, Jiaxin Chen, Yutong Zhang, Di Huang, Yunhong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2024

## 跨领域论文（完整笔记在其他领域）

- Vision Transformer Neural Architecture Search for Out-of-Distribution Generalization: Benchmark and Insights. → [neural-architecture-search](../neural-architecture-search/Guideline%202024.md)
- DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Open Vocabulary Semantic Scene Sketch Understanding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Once for Both: Single Stage of Importance and Sparsity Search for Vision Transformer Compression. → [network-pruning](../network-pruning/Guideline%202024.md)
- Dense Vision Transformer Compression with Few Samples. → [network-pruning](../network-pruning/Guideline%202024.md)
- Zero-TPrune: Zero-Shot Token Pruning Through Leveraging of the Attention Graph in Pre-Trained Transformers. → [network-pruning](../network-pruning/Guideline%202024.md)
- Cross-Domain Few-Shot Object Detection via Enhanced Open-Set Object Detector. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- LPViT: Low-Power Semi-structured Pruning for Vision Transformers. → [network-pruning](../network-pruning/Guideline%202024.md)
- Learning the Unlearned: Mitigating Feature Suppression in Contrastive Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Semantic Residual Prompts for Continual Learning. → [continual-learning](../continual-learning/Guideline%202024.md)
- Isomorphic Pruning for Vision Models. → [network-pruning](../network-pruning/Guideline%202024.md)
- SNP: Structured Neuron-Level Pruning to Preserve Attention Scores. → [network-pruning](../network-pruning/Guideline%202024.md)
- InternVid: A Large-scale Video-Text Dataset for Multimodal Understanding and Generation. → [video-understanding](../video-understanding/Guideline%202024.md)
- Data-independent Module-aware Pruning for Hierarchical Vision Transformers. → [network-pruning](../network-pruning/Guideline%202024.md)
- Synergistic Patch Pruning for Vision Transformer: Unifying Intra- & Inter-Layer Patch Importance. → [network-pruning](../network-pruning/Guideline%202024.md)
- Effective pruning of web-scale datasets based on complexity of concept clusters. → [network-pruning](../network-pruning/Guideline%202024.md)
- Visual Prompt Tuning in Null Space for Continual Learning. → [continual-learning](../continual-learning/Guideline%202024.md)
<!-- COMPLETE v1 papers=39 -->
