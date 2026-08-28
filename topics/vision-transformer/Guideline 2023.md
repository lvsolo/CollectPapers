# Vision Transformer — 2023 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### MG-ViT: A Multi-Granularity Method for Compact and Efficient Vision Transformers.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/daeef96627a461ec43b7567b2930cfde-Abstract-Conference.html)
- **作者**: Yu Zhang, Yepeng Liu, Duoqian Miao, Qi Zhang, Yiwei Shi, Liang Hu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Patch n' Pack: NaViT, a Vision Transformer for any Aspect Ratio and Resolution.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2023/hash/06ea400b9b7cfce6428ec27a371632eb-Abstract-Conference.html) · 📚 被引 16
- **作者**: Mostafa Dehghani, Basil Mustafa, Josip Djolonga, Jonathan Heek, Matthias Minderer, Mathilde Caron et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

### Time Series as Images: Vision Transformer for Irregularly Sampled Time Series.
- **链接**: [arXiv:2303.12799](https://arxiv.org/abs/2303.12799) · [代码](https://github.com/Leezekun/ViTST) · 📚 被引 28
- **作者**: Zekun Li, Shiyang Li, Xifeng Yan
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Irregularly sampled time series are increasingly prevalent, particularly in medical domains. While various specialized methods have been developed to handle these irregularities, effectively modeling their complex dynamics and pronounced sparsity remains a challenge. This paper introduces a novel perspective by converting irregularly sampled time series into line graph images, then utilizing powerful pre-trained vision transformers for time series classification in the same way as image classification. This method not only largely simplifies specialized algorithm designs but also presents the potential to serve as a universal framework for time series modeling. Remarkably, despite its simplicity, our approach outperforms state-of-the-art specialized algorithms on several popular healthcare and human activity datasets. Especially in the rigorous leave-sensors-out setting where a portion of variables is omitted during testing, our method exhibits strong robustness against varying degrees of missing observations, achieving an impressive improvement of 42.8% in absolute F1 score points over leading specialized baselines even with half the variables masked. Code and data are available at https://github.com/Leezekun/ViTST

</details>

### Efficient Adaptation of Large Vision Transformer via Adapter Re-Composing.
- **链接**: [arXiv:2310.06234](https://arxiv.org/abs/2310.06234) · [代码](https://github.com/DavidYanAnDe/ARC) · 📚 被引 8
- **作者**: Wei Dong, Dawei Yan, Zhijun Lin, Peng Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The advent of high-capacity pre-trained models has revolutionized problem-solving in computer vision, shifting the focus from training task-specific models to adapting pre-trained models. Consequently, effectively adapting large pre-trained models to downstream tasks in an efficient manner has become a prominent research area. Existing solutions primarily concentrate on designing lightweight adapters and their interaction with pre-trained models, with the goal of minimizing the number of parameters requiring updates. In this study, we propose a novel Adapter Re-Composing (ARC) strategy that addresses efficient pre-trained model adaptation from a fresh perspective. Our approach considers the reusability of adaptation parameters and introduces a parameter-sharing scheme. Specifically, we leverage symmetric down-/up-projections to construct bottleneck operations, which are shared across layers. By learning low-dimensional re-scaling coefficients, we can effectively re-compose layer-adaptive adapters. This parameter-sharing strategy in adapter design allows us to significantly reduce the number of new parameters while maintaining satisfactory performance, thereby offering a promising approach to compress the adaptation cost. We conduct experiments on 24 downstream image classification tasks using various Vision Transformer variants to evaluate our method. The results demonstrate that our approach achieves compelling transfer learning performance with a reduced parameter count. Our code is available at \href{https://github.com/DavidYanAnDe/ARC}{https://github.com/DavidYanAnDe/ARC}.

</details>

### Lightweight Vision Transformer with Bidirectional Interaction.
- **链接**: [arXiv:2306.00396](https://arxiv.org/abs/2306.00396) · [代码](https://github.com/qhfan/FAT) · 📚 被引 11
- **作者**: Qihang Fan, Huaibo Huang, Xiaoqiang Zhou, Ran He
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent advancements in vision backbones have significantly improved their performance by simultaneously modeling images' local and global contexts. However, the bidirectional interaction between these two contexts has not been well explored and exploited, which is important in the human visual system. This paper proposes a Fully Adaptive Self-Attention (FASA) mechanism for vision transformer to model the local and global information as well as the bidirectional interaction between them in context-aware ways. Specifically, FASA employs self-modulated convolutions to adaptively extract local representation while utilizing self-attention in down-sampled space to extract global representation. Subsequently, it conducts a bidirectional adaptation process between local and global representation to model their interaction. In addition, we introduce a fine-grained downsampling strategy to enhance the down-sampled self-attention mechanism for finer-grained global perception capability. Based on FASA, we develop a family of lightweight vision backbones, Fully Adaptive Transformer (FAT) family. Extensive experiments on multiple vision tasks demonstrate that FAT achieves impressive performance. Notably, FAT accomplishes a 77.6% accuracy on ImageNet-1K using only 4.5M parameters and 0.7G FLOPs, which surpasses the most advanced ConvNets and Transformers with similar model size and computational costs. Moreover, our model exhibits faster speed on modern GPU compared to other models. Code will be available at https://github.com/qhfan/FAT.

</details>

### Scattering Vision Transformer: Spectral Mixing Matters.
- **链接**: [arXiv:2311.01310](https://arxiv.org/abs/2311.01310) · 📚 被引 4
- **作者**: Badri N. Patro, Vijay Agneeswaran
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have gained significant attention and achieved state-of-the-art performance in various computer vision tasks, including image classification, instance segmentation, and object detection. However, challenges remain in addressing attention complexity and effectively capturing fine-grained information within images. Existing solutions often resort to down-sampling operations, such as pooling, to reduce computational cost. Unfortunately, such operations are non-invertible and can result in information loss. In this paper, we present a novel approach called Scattering Vision Transformer (SVT) to tackle these challenges. SVT incorporates a spectrally scattering network that enables the capture of intricate image details. SVT overcomes the invertibility issue associated with down-sampling operations by separating low-frequency and high-frequency components. Furthermore, SVT introduces a unique spectral gating network utilizing Einstein multiplication for token and channel mixing, effectively reducing complexity. We show that SVT achieves state-of-the-art performance on the ImageNet dataset with a significant reduction in a number of parameters and FLOPS. SVT shows 2\% improvement over LiTv2 and iFormer. SVT-H-S reaches 84.2\% top-1 accuracy, while SVT-H-B reaches 85.2\% (state-of-art for base versions) and SVT-H-L reaches 85.7\% (again state-of-art for large versions). SVT also shows comparable results in other vision tasks such as instance segmentation. SVT also outperforms other transformers in transfer learning on standard datasets such as CIFAR10, CIFAR100, Oxford Flower, and Stanford Car datasets. The project page is available on this webpage.\url{https://badripatro.github.io/svt/}.

</details>

### Efficient Low-rank Backpropagation for Vision Transformer Adaptation.
- **链接**: [arXiv:2309.15275](https://arxiv.org/abs/2309.15275)
- **作者**: Yuedong Yang, Hung-Yueh Chiang, Guihong Li, Diana Marculescu, Radu Marculescu
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The increasing scale of vision transformers (ViT) has made the efficient fine-tuning of these large models for specific needs a significant challenge in various applications. This issue originates from the computationally demanding matrix multiplications required during the backpropagation process through linear layers in ViT. In this paper, we tackle this problem by proposing a new Low-rank BackPropagation via Walsh-Hadamard Transformation (LBP-WHT) method. Intuitively, LBP-WHT projects the gradient into a low-rank space and carries out backpropagation. This approach substantially reduces the computation needed for adapting ViT, as matrix multiplication in the low-rank space is far less resource-intensive. We conduct extensive experiments with different models (ViT, hybrid convolution-ViT model) on multiple datasets to demonstrate the effectiveness of our method. For instance, when adapting an EfficientFormer-L1 model on CIFAR100, our LBP-WHT achieves 10.4% higher accuracy than the state-of-the-art baseline, while requiring 9 MFLOPs less computation. As the first work to accelerate ViT adaptation with low-rank backpropagation, our LBP-WHT method is complementary to many prior efforts and can be combined with them for better performance.

</details>

### ShiftAddViT: Mixture of Multiplication Primitives Towards Efficient Vision Transformer.
- **链接**: [arXiv:2306.06446](https://arxiv.org/abs/2306.06446) · 📚 被引 1
- **作者**: Haoran You, Huihong Shi, Yipin Guo, Yingyan Lin
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) have shown impressive performance and have become a unified backbone for multiple vision tasks. However, both the attention mechanism and multi-layer perceptrons (MLPs) in ViTs are not sufficiently efficient due to dense multiplications, leading to costly training and inference. To this end, we propose to reparameterize pre-trained ViTs with a mixture of multiplication primitives, e.g., bitwise shifts and additions, towards a new type of multiplication-reduced model, dubbed $\textbf{ShiftAddViT}$, which aims to achieve end-to-end inference speedups on GPUs without requiring training from scratch. Specifically, all $\texttt{MatMuls}$ among queries, keys, and values are reparameterized using additive kernels, after mapping queries and keys to binary codes in Hamming space. The remaining MLPs or linear layers are then reparameterized with shift kernels. We utilize TVM to implement and optimize those customized kernels for practical hardware deployment on GPUs. We find that such a reparameterization on attention maintains model accuracy, while inevitably leading to accuracy drops when being applied to MLPs. To marry the best of both worlds, we further propose a new mixture of experts (MoE) framework to reparameterize MLPs by taking multiplication or its primitives as experts, e.g., multiplication and shift, and designing a new latency-aware load-balancing loss. Such a loss helps to train a generic router for assigning a dynamic amount of input tokens to different experts according to their latency. Extensive experiments on various 2D/3D Transformer-based vision tasks consistently validate the effectiveness of our proposed ShiftAddViT, achieving up to $\textbf{5.18$\times$}$ latency reductions on GPUs and $\textbf{42.9}$% energy savings, while maintaining a comparable accuracy as original or efficient ViTs.

</details>
