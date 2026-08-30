# Vision Transformer — 2023 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 12 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### PaCa-ViT: Learning Patch-to-Cluster Attention in Vision Transformers. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01781) · 📚 被引 34
- **作者**: Ryan Grainger, Thomas Paniagua, Xi Song, Naresh P. Cuntoor, Mun Wai Lee, Tianfu Wu
- **🏷️ 机构**: NC State,Department of ECE, An Independent Researcher, BlueHalo
- **会议**: CVPR 2023
- **摘要（中）**: 针对视觉Transformer中自注意力计算复杂度高且难以捕捉局部细节的问题，提出PaCa-ViT方法，通过引入patch到簇的注意力机制，将注意力计算从全局patch对patch转变为patch与聚类中心之间的交互，从而降低计算成本并增强局部特征建模。相比标准ViT，该方法在保持全局上下文的同时，更高效地处理高分辨率输入。实验表明，在图像分类等任务上，PaCa-ViT在计算效率和精度之间取得了更好的平衡。
- **摘要（英）**: To address the high computational cost and limited local detail capture in vision transformers, PaCa-ViT introduces patch-to-cluster attention, replacing global patch-pair interactions with patch-cluster center computations. This reduces complexity while enhancing local feature modeling. Experiments show improved efficiency-accuracy trade-offs on image classification benchmarks.
- **核心贡献**: 提出patch-to-cluster注意力机制，降低ViT计算复杂度并提升局部建模能力。
- **创新点**: 创新性地将注意力从patch对patch改为patch对簇中心，实现高效全局-局部融合。
- **结果**: 在图像分类任务上实现更优的效率与精度平衡。

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

> We present an architecture and a training recipe that adapts pre-trained open-world image models to localization in videos. Understanding the open visual world (without being constrained by fixed label spaces) is crucial for many real-world vision tasks. Contrastive pre-training on large image-text datasets has recently led to significant improvements for image-level tasks. For more structured tasks involving object localization applying pre-trained models is more challenging. This is particularly true for video tasks, where task-specific data is limited. We show successful transfer of open-world models by building on the OWL-ViT open-vocabulary detection model and adapting it to video by adding a transformer decoder. The decoder propagates object representations recurrently through time by using the output tokens for one frame as the object queries for the next. Our model is end-to-end trainable on video data and enjoys improved temporal consistency compared to tracking-by-detection baselines, while retaining the open-world capabilities of the backbone detector. We evaluate our model on the challenging TAO-OW benchmark and demonstrate that open-world capabilities, learned from large-scale image-text pre-training, can be transferred successfully to open-world localization across diverse videos.

</details>

### I-ViT: Integer-only Quantization for Efficient Vision Transformer Inference. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2207.01405](https://arxiv.org/abs/2207.01405) · 📚 被引 122
- **作者**: Zhikai Li, Qingyi Gu
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Automation
- **会议**: ICCV 2023
- **摘要（中）**: 针对ViT在边缘设备上部署时浮点运算开销大的问题，提出I-ViT整数-only量化方案，使ViT的整个推理计算图仅使用整数算术和位移操作，避免浮点运算。线性操作采用dyadic算术，非线性操作（如Softmax、GELU、LayerNorm）通过轻量级整数近似方法实现。实验表明，I-ViT在保持精度的同时，显著降低存储和计算开销，适用于资源受限场景。
- **摘要（英）**: To enable efficient ViT inference on edge devices, I-ViT proposes an integer-only quantization scheme where the entire computational graph uses integer arithmetic and bit-shifting, avoiding floating-point operations. Linear layers follow dyadic arithmetic, while non-linear functions are approximated with lightweight integer methods. Experiments show significant reductions in storage and computation with minimal accuracy loss.
- **核心贡献**: 提出首个ViT整数-only推理方案，覆盖所有操作。
- **创新点**: 创新性地设计非线性操作的整数近似方法，突破dyadic算术限制。
- **结果**: 在保持精度下，实现高效整数推理，降低部署成本。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) have achieved state-of-the-art performance on various computer vision applications. However, these models have considerable storage and computational overheads, making their deployment and efficient inference on edge devices challenging. Quantization is a promising approach to reducing model complexity, and the dyadic arithmetic pipeline can allow the quantized models to perform efficient integer-only inference. Unfortunately, dyadic arithmetic is based on the homogeneity condition in convolutional neural networks, which is not applicable to the non-linear components in ViTs, making integer-only inference of ViTs an open issue. In this paper, we propose I-ViT, an integer-only quantization scheme for ViTs, to enable ViTs to perform the entire computational graph of inference with integer arithmetic and bit-shifting, and without any floating-point arithmetic. In I-ViT, linear operations (e.g., MatMul and Dense) follow the integer-only pipeline with dyadic arithmetic, and non-linear operations (e.g., Softmax, GELU, and LayerNorm) are approximated by the proposed light-weight integer-only arithmetic methods. More specifically, I-ViT applies the proposed Shiftmax and ShiftGELU, which are designed to use integer bit-shifting to approximate the corresponding floating-point operations. We evaluate I-ViT on various benchmark models and the results show that integer-only INT8 quantization achieves comparable (or even slightly higher) accuracy to the full-precision (FP) baseline. Furthermore, we utilize TVM for practical hardware deployment on the GPU's integer arithmetic units, achieving 3.72$\sim$4.11$\times$ inference speedup compared to the FP model. Code of both Pytorch and TVM is released at https://github.com/zkkli/I-ViT.

</details>

### RepQ-ViT: Scale Reparameterization for Post-Training Quantization of Vision Transformers. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2212.08254](https://arxiv.org/abs/2212.08254) · 📚 被引 113
- **作者**: Zhikai Li, Junrui Xiao, Lianwei Yang, Qingyi Gu
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Automation
- **会议**: ICCV 2023
- **摘要（中）**: 这篇论文针对视觉Transformer（ViT）在后训练量化（PTQ）中精度下降的问题，尤其是在低比特情况下。作者提出了RepQ-ViT框架，通过量化尺度重参数化来解耦量化和推理过程，前者使用复杂量化器，后者使用简化量化器。该方法特别关注LayerNorm后激活的通道间变化和Softmax后激活的幂律分布，分别采用通道量化和log√2量化，然后重参数化到硬件友好的格式。实验表明，RepQ-ViT在低比特量化下显著提升了ViT的精度，优于现有PTQ方法。
- **摘要（英）**: This paper addresses the accuracy degradation of vision transformers (ViTs) in post-training quantization (PTQ), especially at low bit-widths. The authors propose RepQ-ViT, a framework that decouples quantization and inference via scale reparameterization, using complex quantizers for training and simplified ones for deployment. It targets extreme activation distributions, applying channel-wise and log√2 quantization, then reparameterizes scales for hardware efficiency. Experiments show significant accuracy improvements over existing PTQ methods for ViTs.
- **核心贡献**: 提出RepQ-ViT，一种基于尺度重参数化的ViT后训练量化框架，兼顾精度和硬件效率。
- **创新点**: 通过解耦量化和推理过程，并针对极端激活分布设计专用量化策略。
- **结果**: 在低比特量化下显著提升ViT精度，优于现有PTQ方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Post-training quantization (PTQ), which only requires a tiny dataset for calibration without end-to-end retraining, is a light and practical model compression technique. Recently, several PTQ schemes for vision transformers (ViTs) have been presented; unfortunately, they typically suffer from non-trivial accuracy degradation, especially in low-bit cases. In this paper, we propose RepQ-ViT, a novel PTQ framework for ViTs based on quantization scale reparameterization, to address the above issues. RepQ-ViT decouples the quantization and inference processes, where the former employs complex quantizers and the latter employs scale-reparameterized simplified quantizers. This ensures both accurate quantization and efficient inference, which distinguishes it from existing approaches that sacrifice quantization performance to meet the target hardware. More specifically, we focus on two components with extreme distributions: post-LayerNorm activations with severe inter-channel variation and post-Softmax activations with power-law features, and initially apply channel-wise quantization and log$\sqrt{2}$ quantization, respectively. Then, we reparameterize the scales to hardware-friendly layer-wise quantization and log2 quantization for inference, with only slight accuracy or computational costs. Extensive experiments are conducted on multiple vision tasks with different model variants, proving that RepQ-ViT, without hyperparameters and expensive reconstruction procedures, can outperform existing strong baselines and encouragingly improve the accuracy of 4-bit PTQ of ViTs to a usable level. Code is available at https://github.com/zkkli/RepQ-ViT.

</details>

### DropKey for Vision Transformer. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02174) · 📚 被引 74
- **作者**: Bonan Li, Yinhan Hu, Xuecheng Nie, Congying Han, Xiangjian Jiang, Tiande Guo et al.
- **🏷️ 机构**: University of Chinese Academy of Sciences, MT Lab, Meitu Inc., University of Cambridge
- **会议**: CVPR 2023
- **摘要（中）**: 针对ViT训练中过拟合和注意力退化问题，提出DropKey方法，在训练过程中随机丢弃部分注意力键，增强模型泛化能力。该方法类似Dropout但作用于注意力矩阵，能有效缓解注意力集中问题。实验表明在图像分类等任务上提升性能。
- **摘要（英）**: This paper proposes DropKey, a regularization technique that randomly drops attention keys during ViT training to improve generalization and mitigate attention degeneration. It demonstrates performance gains on image classification tasks.
- **核心贡献**: 提出DropKey正则化方法，提升ViT泛化能力。
- **创新点**: 将Dropout思想应用于注意力键的随机丢弃。
- **结果**: 在图像分类任务上提升性能。

### EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention. **⭐⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2305.07027](https://arxiv.org/abs/2305.07027) · 📚 被引 828
- **作者**: Xinyu Liu, Houwen Peng, Ningxin Zheng, Yuqing Yang, Han Hu, Yixuan Yuan
- **🏷️ 机构**: The Chinese University of Hong Kong, Microsoft Research
- **会议**: CVPR 2023
- **摘要（中）**: 针对ViT在实时应用中计算成本高的问题，提出EfficientViT系列，通过三明治布局（单个内存受限的MHSA夹在高效FFN之间）提升内存效率，并设计级联组注意力模块，将特征分片喂给不同注意力头，减少计算冗余并增强注意力多样性。实验表明EfficientViT在速度和精度上优于现有高效模型，如EfficientViT-M5在ImageNet上达到高精度同时保持低延迟。
- **摘要（英）**: This paper proposes EfficientViT, a family of high-speed vision transformers with a sandwich layout and cascaded group attention to reduce memory-bound operations and attention redundancy. It outperforms existing efficient models in speed-accuracy trade-off, with EfficientViT-M5 achieving high accuracy on ImageNet at low latency.
- **核心贡献**: 提出高效ViT架构，通过三明治布局和级联组注意力实现速度与精度的平衡。
- **创新点**: 级联组注意力机制减少计算冗余，三明治布局提升内存效率。
- **结果**: 在ImageNet等任务上优于现有高效模型，速度更快。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers have shown great success due to their high model capabilities. However, their remarkable performance is accompanied by heavy computation costs, which makes them unsuitable for real-time applications. In this paper, we propose a family of high-speed vision transformers named EfficientViT. We find that the speed of existing transformer models is commonly bounded by memory inefficient operations, especially the tensor reshaping and element-wise functions in MHSA. Therefore, we design a new building block with a sandwich layout, i.e., using a single memory-bound MHSA between efficient FFN layers, which improves memory efficiency while enhancing channel communication. Moreover, we discover that the attention maps share high similarities across heads, leading to computational redundancy. To address this, we present a cascaded group attention module feeding attention heads with different splits of the full feature, which not only saves computation cost but also improves attention diversity. Comprehensive experiments demonstrate EfficientViT outperforms existing efficient models, striking a good trade-off between speed and accuracy. For instance, our EfficientViT-M5 surpasses MobileNetV3-Large by 1.9% in accuracy, while getting 40.4% and 45.2% higher throughput on Nvidia V100 GPU and Intel Xeon CPU, respectively. Compared to the recent efficient model MobileViT-XXS, EfficientViT-M2 achieves 1.8% superior accuracy, while running 5.8x/3.7x faster on the GPU/CPU, and 7.4x faster when converted to ONNX format. Code and models are available at https://github.com/microsoft/Cream/tree/main/EfficientViT.

</details>

### HM-ViT: Hetero-modal Vehicle-to-Vehicle Cooperative Perception with Vision Transformer. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2304.10628](https://arxiv.org/abs/2304.10628) · 📚 被引 100
- **作者**: Hao Xiang, Runsheng Xu, Jiaqi Ma
- **🏷️ 机构**: University of California,Los Angeles
- **会议**: ICCV 2023
- **摘要（中）**: ①该论文针对车车协同感知中异构模态（如相机与LiDAR）协作的问题，现有方法仅支持同质传感器配置。②提出了HM-ViT，首个统一的多智能体异构模态协同感知框架，通过异构3D图Transformer联合推理智能体间和智能体内交互，融合多视角图像与LiDAR点云特征。③相比现有协同感知方法，创新在于支持不同数量和类型的传感器组合，提升协作规模与跨模态交互。④在OPV2V数据集上，HM-ViT优于SOTA协同感知方法，具体数值未在摘要中给出。
- **摘要（英）**: This paper tackles the problem of hetero-modal cooperative perception in V2V scenarios, where agents have different sensor modalities. It proposes HM-ViT, the first unified framework for multi-agent hetero-modal cooperation, using a heterogeneous 3D graph transformer to fuse multi-view images and LiDAR features. The innovation is supporting varying agent types and numbers, enhancing collaboration scale. Experiments on OPV2V show superiority over SOTA methods, though exact metrics are omitted.
- **核心贡献**: 提出首个异构模态V2V协同感知框架HM-ViT。
- **创新点**: 设计异构3D图Transformer以联合建模智能体间和智能体内交互。
- **结果**: 在OPV2V上优于现有SOTA协同感知方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vehicle-to-Vehicle technologies have enabled autonomous vehicles to share information to see through occlusions, greatly enhancing perception performance. Nevertheless, existing works all focused on homogeneous traffic where vehicles are equipped with the same type of sensors, which significantly hampers the scale of collaboration and benefit of cross-modality interactions. In this paper, we investigate the multi-agent hetero-modal cooperative perception problem where agents may have distinct sensor modalities. We present HM-ViT, the first unified multi-agent hetero-modal cooperative perception framework that can collaboratively predict 3D objects for highly dynamic vehicle-to-vehicle (V2V) collaborations with varying numbers and types of agents. To effectively fuse features from multi-view images and LiDAR point clouds, we design a novel heterogeneous 3D graph transformer to jointly reason inter-agent and intra-agent interactions. The extensive experiments on the V2V perception dataset OPV2V demonstrate that the HM-ViT outperforms SOTA cooperative perception methods for V2V hetero-modal cooperative perception. We will release codes to facilitate future research.

</details>

### FLatten Transformer: Vision Transformer using Focused Linear Attention.
- **链接**: [arXiv:2308.00442](https://arxiv.org/abs/2308.00442) · [代码](https://github.com/LeapLabTHU/FLatten-Transformer) · 📚 被引 322
- **作者**: Dongchen Han, Xuran Pan, Yizeng Han, Shiji Song, Gao Huang
- **🏷️ 机构**: Tsinghua University,BNRist,Department of Automation
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The quadratic computation complexity of self-attention has been a persistent challenge when applying Transformer models to vision tasks. Linear attention, on the other hand, offers a much more efficient alternative with its linear complexity by approximating the Softmax operation through carefully designed mapping functions. However, current linear attention approaches either suffer from significant performance degradation or introduce additional computation overhead from the mapping functions. In this paper, we propose a novel Focused Linear Attention module to achieve both high efficiency and expressiveness. Specifically, we first analyze the factors contributing to the performance degradation of linear attention from two perspectives: the focus ability and feature diversity. To overcome these limitations, we introduce a simple yet effective mapping function and an efficient rank restoration module to enhance the expressiveness of self-attention while maintaining low computation complexity. Extensive experiments show that our linear attention module is applicable to a variety of advanced vision Transformers, and achieves consistently improved performances on multiple benchmarks. Code is available at https://github.com/LeapLabTHU/FLatten-Transformer.

</details>

### Vision Transformer Adapters for Generalizable Multitask Learning.
- **链接**: [arXiv:2308.12372](https://arxiv.org/abs/2308.12372) · 📚 被引 15
- **作者**: Deblina Bhattacharjee, Sabine Süsstrunk, Mathieu Salzmann
- **🏷️ 机构**: EPFL,School of Computer and Communication Sciences,Switzerland
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the first multitasking vision transformer adapters that learn generalizable task affinities which can be applied to novel tasks and domains. Integrated into an off-the-shelf vision transformer backbone, our adapters can simultaneously solve multiple dense vision tasks in a parameter-efficient manner, unlike existing multitasking transformers that are parametrically expensive. In contrast to concurrent methods, we do not require retraining or fine-tuning whenever a new task or domain is added. We introduce a task-adapted attention mechanism within our adapter framework that combines gradient-based task similarities with attention-based ones. The learned task affinities generalize to the following settings: zero-shot task transfer, unsupervised domain adaptation, and generalization without fine-tuning to novel domains. We demonstrate that our approach outperforms not only the existing convolutional neural network-based multitasking methods but also the vision transformer-based ones. Our project page is at \url{https://ivrl.github.io/VTAGML}.

</details>

### Revisiting Vision Transformer from the View of Path Ensemble.
- **链接**: [arXiv:2308.06548](https://arxiv.org/abs/2308.06548) · 📚 被引 7
- **作者**: Shuning Chang, Pichao Wang, Hao Luo, Fan Wang, Mike Zheng Shou
- **🏷️ 机构**: National University of Singapore,Show Lab, Alibaba Group
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) are normally regarded as a stack of transformer layers. In this work, we propose a novel view of ViTs showing that they can be seen as ensemble networks containing multiple parallel paths with different lengths. Specifically, we equivalently transform the traditional cascade of multi-head self-attention (MSA) and feed-forward network (FFN) into three parallel paths in each transformer layer. Then, we utilize the identity connection in our new transformer form and further transform the ViT into an explicit multi-path ensemble network. From the new perspective, these paths perform two functions: the first is to provide the feature for the classifier directly, and the second is to provide the lower-level feature representation for subsequent longer paths. We investigate the influence of each path for the final prediction and discover that some paths even pull down the performance. Therefore, we propose the path pruning and EnsembleScale skills for improvement, which cut out the underperforming paths and re-weight the ensemble components, respectively, to optimize the path combination and make the short paths focus on providing high-quality representation for subsequent paths. We also demonstrate that our path combination strategies can help ViTs go deeper and act as high-pass filters to filter out partial low-frequency signals. To further enhance the representation of paths served for subsequent paths, self-distillation is applied to transfer knowledge from the long paths to the short paths. This work calls for more future research to explain and design ViTs from new perspectives.

</details>

### TripLe: Revisiting Pretrained Model Reuse and Progressive Learning for Efficient Vision Transformer Scaling and Searching.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01573) · 📚 被引 2
- **作者**: Cheng Fu, Hanxian Huang, Zixuan Jiang, Yun Ni, Lifeng Nai, Gang Wu et al.
- **🏷️ 机构**: UC San Diego, Google
- **会议**: ICCV 2023

### Adaptive and Background-Aware Vision Transformer for Real-Time UAV Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01286) · 📚 被引 63
- **作者**: Shuiwang Li, Xiangxyang Yang, Dan Zeng, Xucheng Wang
- **🏷️ 机构**: Guilin University of Technology,College of Information Science and Engineering,China, Southern University of Science and Technology,Research Institue of Trustworthy Autonomous Systems,China
- **会议**: ICCV 2023

### FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization.
- **链接**: [arXiv:2303.14189](https://arxiv.org/abs/2303.14189) · [代码](https://github.com/apple/ml-fastvit) · 📚 被引 102
- **作者**: Pavan Kumar Anasosalu Vasu, James Gabriel, Jeff Zhu, Oncel Tuzel, Anurag Ranjan
- **🏷️ 机构**: Apple
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The recent amalgamation of transformer and convolutional designs has led to steady improvements in accuracy and efficiency of the models. In this work, we introduce FastViT, a hybrid vision transformer architecture that obtains the state-of-the-art latency-accuracy trade-off. To this end, we introduce a novel token mixing operator, RepMixer, a building block of FastViT, that uses structural reparameterization to lower the memory access cost by removing skip-connections in the network. We further apply train-time overparametrization and large kernel convolutions to boost accuracy and empirically show that these choices have minimal effect on latency. We show that - our model is 3.5x faster than CMT, a recent state-of-the-art hybrid transformer architecture, 4.9x faster than EfficientNet, and 1.9x faster than ConvNeXt on a mobile device for the same accuracy on the ImageNet dataset. At similar latency, our model obtains 4.2% better Top-1 accuracy on ImageNet than MobileOne. Our model consistently outperforms competing architectures across several tasks -- image classification, detection, segmentation and 3D mesh regression with significant improvement in latency on both a mobile device and a desktop GPU. Furthermore, our model is highly robust to out-of-distribution samples and corruptions, improving over competing robust models. Code and models are available at https://github.com/apple/ml-fastvit.

</details>

### FDViT: Improve the Hierarchical Architecture of Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00547) · 📚 被引 15
- **作者**: Yixing Xu, Chao Li, Dong Li, Xiao Sheng, Fan Jiang, Lu Tian et al.
- **🏷️ 机构**: Advanced Micro Devices, Inc.,Beijing,China
- **会议**: ICCV 2023

### MPCViT: Searching for Accurate and Efficient MPC-Friendly Vision Transformer with Heterogeneous Attention.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00466) · 📚 被引 20
- **作者**: Wenxuan Zeng, Meng Li, Wenjie Xiong, Tong Tong, Wen-Jie Lu, Jin Tan et al.
- **🏷️ 机构**: Peking University, Virginia Tech, Ant Group
- **会议**: ICCV 2023

### Fcaformer: Forward Cross Attention in Hybrid Vision Transformer.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00557) · 📚 被引 8
- **作者**: Haokui Zhang, Wenze Hu, Xiaoyu Wang
- **🏷️ 机构**: Intellifusion, The Hong Kong University of Science and Technology (Guangzhou)
- **会议**: ICCV 2023

### A Re-Parameterized Vision Transformer (ReVT) for Domain-Generalized Semantic Segmentation.
- **链接**: [arXiv:2308.13331](https://arxiv.org/abs/2308.13331) · 📚 被引 14
- **作者**: Jan-Aike Termöhlen, Timo Bartels, Tim Fingscheidt
- **🏷️ 机构**: Technische Universitat Braunschweig,Germany
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The task of semantic segmentation requires a model to assign semantic labels to each pixel of an image. However, the performance of such models degrades when deployed in an unseen domain with different data distributions compared to the training domain. We present a new augmentation-driven approach to domain generalization for semantic segmentation using a re-parameterized vision transformer (ReVT) with weight averaging of multiple models after training. We evaluate our approach on several benchmark datasets and achieve state-of-the-art mIoU performance of 47.3% (prior art: 46.3%) for small models and of 50.1% (prior art: 47.8%) for midsized models on commonly used benchmark datasets. At the same time, our method requires fewer parameters and reaches a higher frame rate than the best prior art. It is also easy to implement and, unlike network ensembles, does not add any computational complexity during inference.

</details>

### Lightweight Vision Transformer with Spatial and Channel Enhanced Self-Attention.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00162) · 📚 被引 15
- **作者**: Jiahao Zheng, Longqi Yang, Yiying Li, Ke Yang, Zhiyuan Wang, Jun Zhou
- **🏷️ 机构**: University of Electronic Science and Technology of China,Chengdu,China, Academy of Military Sciences,Defense Innovation Institute,Beijing,China
- **会议**: ICCV 2023

## 跨领域论文（完整笔记在其他领域）

- SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer. → [network-pruning](../network-pruning/Guideline%202023.md)
- MDL-NAS: A Joint Multi-domain Learning Framework for Vision Transformer. → [neural-architecture-search](../neural-architecture-search/Guideline%202023.md)
- Global Vision Transformer Pruning with Hessian-Aware Saliency. → [network-pruning](../network-pruning/Guideline%202023.md)
- Boost Vision Transformer with GPU-Friendly Sparsity and Quantization. → [network-pruning](../network-pruning/Guideline%202023.md)

## 🆕 增量新增

### Castling-ViT: Compressing Self-Attention via Switching Towards Linear-Angular Attention at Vision Transformer Inference. **⭐⭐⭐** (相关度: 55%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01387) · 📚 被引 57
- **作者**: Haoran You, Yunyang Xiong, Xiaoliang Dai, Bichen Wu, Peizhao Zhang, Haoqi Fan et al.
- **🏷️ 机构**: Georgia Institute of Technology, Meta Research
- **会议**: CVPR 2023
- **摘要（中）**: ①针对ViT推理时自注意力计算开销大的问题。②提出Castling-ViT，在推理阶段动态切换至线性-角度注意力，减少计算量。③相比固定注意力机制，该方法根据输入特征自适应选择注意力类型，提升效率。④在图像分类任务上，Castling-ViT在保持精度的同时显著降低FLOPs。
- **摘要（英）**: This work tackles the high inference cost of self-attention in ViTs. It introduces Castling-ViT, which switches to linear-angular attention during inference to reduce computation. By adaptively selecting attention types, it achieves significant FLOPs reduction with minimal accuracy loss on image classification.
- **核心贡献**: 提出推理时自适应切换注意力机制，降低ViT计算负担。
- **创新点**: 动态选择线性或角度注意力，兼顾精度与效率。
- **结果**: 在图像分类上实现高效推理，FLOPs显著降低。

### T-FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2303.16940](https://arxiv.org/abs/2303.16940) · 📚 被引 31
- **作者**: James Giroux, Martin Bouchard, Robert Laganière
- **🏷️ 机构**: University of Ottawa,Ottawa,Canada
- **会议**: ICCV 2023
- **摘要（中）**: 针对雷达原始ADC信号处理复杂且信息损失大的问题，该论文提出T-FFTRadNet，使用Swin Transformer从原始ADC雷达信号直接进行目标检测。方法通过FFT预处理和Swin Transformer编码器提取特征，避免了传统信号处理的信息丢失。相比基于点云或传统雷达处理方法，该方法在雷达目标检测任务上取得了更优性能。实验验证了Transformer在雷达信号处理中的有效性。
- **摘要（英）**: This paper proposes T-FFTRadNet for object detection from raw ADC radar signals using Swin Transformers. It avoids information loss in traditional processing and achieves superior performance on radar detection tasks, demonstrating the effectiveness of Transformers for radar signals.
- **核心贡献**: 提出基于Swin Transformer的原始ADC雷达信号目标检测方法。
- **创新点**: 直接从原始ADC信号进行检测，避免传统处理的信息损失。
- **结果**: 在雷达检测任务上取得优于传统方法的性能。

### Video OWL-ViT: Temporally-consistent open-world localization in video. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2308.11093](https://arxiv.org/abs/2308.11093) · 📚 被引 11
- **作者**: Georg Heigold, Daniel Keysers, Matthias Minderer, Mario Lucic, Alexey A. Gritsenko, Fisher Yu et al.
- **🏷️ 机构**: Google DeepMind, ETH Zurich
- **会议**: ICCV 2023
- **摘要（中）**: ①针对视频中的开放世界目标定位问题，即识别和定位未在固定标签空间中定义的目标，现有图像级开放词汇模型难以直接应用于视频任务，且视频数据有限。②提出Video OWL-ViT架构，基于预训练的OWL-ViT开放词汇检测模型，添加一个transformer解码器，通过将一帧的输出token作为下一帧的对象查询，循环传播对象表示，实现端到端的视频训练。③相比基于检测跟踪的基线，该方法利用时间一致性，在保留开放世界能力的同时，提升了视频定位的时序稳定性。④在TAO-OW基准上评估，展示了从大规模图像-文本预训练中学习的开放世界能力成功迁移到视频，并优于基线方法。
- **摘要（英）**: This paper addresses open-world object localization in videos, where models must detect objects beyond fixed label spaces, a challenge for image-based open-vocabulary models due to limited video data. It proposes Video OWL-ViT, which adapts the OWL-ViT detector by adding a transformer decoder that recurrently propagates object representations across frames, enabling end-to-end training and improved temporal consistency. Evaluated on TAO-OW, it demonstrates successful transfer of open-world capabilities from large-scale image-text pretraining to video, outperforming tracking-by-detection baselines.
- **核心贡献**: 提出首个将开放世界图像检测模型适配到视频定位的架构和训练策略，实现时序一致的开放词汇检测。
- **创新点**: 利用transformer解码器循环传播对象表示，以输出token作为下一帧查询，实现端到端视频训练。
- **结果**: 在TAO-OW基准上验证了开放世界能力迁移的有效性，并优于跟踪检测基线。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present an architecture and a training recipe that adapts pre-trained open-world image models to localization in videos. Understanding the open visual world (without being constrained by fixed label spaces) is crucial for many real-world vision tasks. Contrastive pre-training on large image-text datasets has recently led to significant improvements for image-level tasks. For more structured tasks involving object localization applying pre-trained models is more challenging. This is particularly true for video tasks, where task-specific data is limited. We show successful transfer of open-world models by building on the OWL-ViT open-vocabulary detection model and adapting it to video by adding a transformer decoder. The decoder propagates object representations recurrently through time by using the output tokens for one frame as the object queries for the next. Our model is end-to-end trainable on video data and enjoys improved temporal consistency compared to tracking-by-detection baselines, while retaining the open-world capabilities of the backbone detector. We evaluate our model on the challenging TAO-OW benchmark and demonstrate that open-world capabilities, learned from large-scale image-text pre-training, can be transferred successfully to open-world localization across diverse videos.

</details>

### ViPLO: Vision Transformer Based Pose-Conditioned Self-Loop Graph for Human-Object Interaction Detection. **⭐⭐⭐** (相关度: 50%)
- **链接**: [arXiv:2304.08114](https://arxiv.org/abs/2304.08114) · 📚 被引 75
- **作者**: Jeeseung Park, Jin-Woo Park, Jong-Seok Lee
- **🏷️ 机构**: mAy-I Inc.,Seoul,Korea, Yonsei University,Korea
- **会议**: CVPR 2023
- **摘要（中）**: ①针对两阶段HOI检测器性能低于单阶段方法的问题，源于旧骨干网络和交互分类器未考虑人类感知过程。②提出ViPLO，基于Vision Transformer的姿势条件自循环图，包含掩码重叠区域模块和姿势条件自循环结构。③相比现有方法，MOA模块解决ViT骨干的量化问题，自循环图利用人体关节局部特征提升交互识别。④在HOI检测基准上，ViPLO显著提升性能，优于现有两阶段方法。
- **摘要（英）**: This paper addresses the performance gap of two-stage HOI detectors by proposing ViPLO, a Vision Transformer-based pose-conditioned self-loop graph. It introduces a masking with overlapped area module and a pose-conditioned self-loop structure to enhance interaction classification. Results show significant performance improvements over existing two-stage methods on HOI benchmarks.
- **核心贡献**: 提出ViT骨干和姿势条件图，提升两阶段HOI检测性能。
- **创新点**: 利用重叠区域掩码和自循环图增强局部特征建模。
- **结果**: 在HOI检测上取得显著精度提升。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Human-Object Interaction (HOI) detection, which localizes and infers relationships between human and objects, plays an important role in scene understanding. Although two-stage HOI detectors have advantages of high efficiency in training and inference, they suffer from lower performance than one-stage methods due to the old backbone networks and the lack of considerations for the HOI perception process of humans in the interaction classifiers. In this paper, we propose Vision Transformer based Pose-Conditioned Self-Loop Graph (ViPLO) to resolve these problems. First, we propose a novel feature extraction method suitable for the Vision Transformer backbone, called masking with overlapped area (MOA) module. The MOA module utilizes the overlapped area between each patch and the given region in the attention function, which addresses the quantization problem when using the Vision Transformer backbone. In addition, we design a graph with a pose-conditioned self-loop structure, which updates the human node encoding with local features of human joints. This allows the classifier to focus on specific human joints to effectively identify the type of interaction, which is motivated by the human perception process for HOI. As a result, ViPLO achieves the state-of-the-art results on two public benchmarks, especially obtaining a +2.07 mAP performance gain on the HICO-DET dataset. The source codes are available at https://github.com/Jeeseung-Park/ViPLO.

</details>

### RangeViT: Towards Vision Transformers for 3D Semantic Segmentation in Autonomous Driving. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2301.10222](https://arxiv.org/abs/2301.10222) · 📚 被引 141
- **作者**: Angelika Ando, Spyros Gidaris, Andrei Bursuc, Gilles Puy, Alexandre Boulch, Renaud Marlet
- **🏷️ 机构**: Valeo.ai,Paris,France
- **会议**: CVPR 2023
- **摘要（中）**: ①针对投影法3D语义分割中，2D CNN性能受限，而ViT难以训练且缺乏归纳偏置的问题。②提出RangeViT，将ViT应用于范围图像分割，通过预训练ViT和定制卷积补偿归纳偏置。③相比传统CNN方法，利用大规模图像预训练提升表示能力，并适配LiDAR数据特性。④在自动驾驶数据集上，RangeViT取得SOTA性能，优于现有投影法。
- **摘要（英）**: This paper addresses the limitations of CNN-based projection methods for 3D semantic segmentation by proposing RangeViT, which applies ViTs to range images. It leverages pre-trained ViTs and tailored convolutions to compensate for inductive bias. Results show state-of-the-art performance on autonomous driving benchmarks.
- **核心贡献**: 提出RangeViT，利用预训练ViT提升3D语义分割性能。
- **创新点**: 结合图像预训练和定制卷积，解决ViT训练难题。
- **结果**: 在自动驾驶数据集上取得SOTA结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Casting semantic segmentation of outdoor LiDAR point clouds as a 2D problem, e.g., via range projection, is an effective and popular approach. These projection-based methods usually benefit from fast computations and, when combined with techniques which use other point cloud representations, achieve state-of-the-art results. Today, projection-based methods leverage 2D CNNs but recent advances in computer vision show that vision transformers (ViTs) have achieved state-of-the-art results in many image-based benchmarks. In this work, we question if projection-based methods for 3D semantic segmentation can benefit from these latest improvements on ViTs. We answer positively but only after combining them with three key ingredients: (a) ViTs are notoriously hard to train and require a lot of training data to learn powerful representations. By preserving the same backbone architecture as for RGB images, we can exploit the knowledge from long training on large image collections that are much cheaper to acquire and annotate than point clouds. We reach our best results with pre-trained ViTs on large image datasets. (b) We compensate ViTs' lack of inductive bias by substituting a tailored convolutional stem for the classical linear embedding layer. (c) We refine pixel-wise predictions with a convolutional decoder and a skip connection from the convolutional stem to combine low-level but fine-grained features of the the convolutional stem with the high-level but coarse predictions of the ViT encoder. With these ingredients, we show that our method, called RangeViT, outperforms existing projection-based methods on nuScenes and SemanticKITTI. The code is available at https://github.com/valeoai/rangevit.

</details>

### Slide-Transformer: Hierarchical Vision Transformer with Local Self-Attention. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2304.04237](https://arxiv.org/abs/2304.04237) · 📚 被引 103
- **作者**: Xuran Pan, Tianzhu Ye, Zhuofan Xia, Shiji Song, Gao Huang
- **🏷️ 机构**: BNRist, Tsinghua University,Department of Automation
- **会议**: CVPR 2023
- **摘要（中）**: 针对现有局部自注意力模块在计算效率、灵活性和通用性上的不足（如Im2Col函数低效或依赖特定CUDA内核），提出Slide Attention模块，利用深度可分离卷积高效替代列式Im2Col，并从行式视角重新解释，同时引入变形移位模块增强特征交互。相比已有局部注意力方法，该方法在保持局部归纳偏置和动态特征选择的同时，显著提升效率且无需CUDA支持。实验表明在图像分类等任务上取得与SOTA相当或更优的性能，同时具有更好的通用性。
- **摘要（英）**: This paper addresses the inefficiency and poor generalizability of existing local self-attention modules, which rely on costly Im2Col or custom CUDA kernels. It proposes Slide Attention, which reinterprets column-based Im2Col from a row-based perspective and substitutes it with depthwise convolution, plus a deformed shifting module. This achieves high efficiency and flexibility without CUDA dependency, matching or exceeding state-of-the-art performance on vision benchmarks.
- **核心贡献**: 提出基于卷积的Slide Attention模块，实现高效、灵活、通用的局部自注意力。
- **创新点**: 用深度可分离卷积替代Im2Col，并引入变形移位模块增强局部特征交互。
- **结果**: 在图像分类等任务上达到与SOTA相当的性能，同时显著提升计算效率和设备通用性。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-attention mechanism has been a key factor in the recent progress of Vision Transformer (ViT), which enables adaptive feature extraction from global contexts. However, existing self-attention methods either adopt sparse global attention or window attention to reduce the computation complexity, which may compromise the local feature learning or subject to some handcrafted designs. In contrast, local attention, which restricts the receptive field of each query to its own neighboring pixels, enjoys the benefits of both convolution and self-attention, namely local inductive bias and dynamic feature selection. Nevertheless, current local attention modules either use inefficient Im2Col function or rely on specific CUDA kernels that are hard to generalize to devices without CUDA support. In this paper, we propose a novel local attention module, Slide Attention, which leverages common convolution operations to achieve high efficiency, flexibility and generalizability. Specifically, we first re-interpret the column-based Im2Col function from a new row-based perspective and use Depthwise Convolution as an efficient substitution. On this basis, we propose a deformed shifting module based on the re-parameterization technique, which further relaxes the fixed key/value positions to deformed features in the local region. In this way, our module realizes the local attention paradigm in both efficient and flexible manner. Extensive experiments show that our slide attention module is applicable to a variety of advanced Vision Transformer models and compatible with various hardware devices, and achieves consistently improved performances on comprehensive benchmarks. Code is available at https://github.com/LeapLabTHU/Slide-Transformer.

</details>

### SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2303.17605](https://arxiv.org/abs/2303.17605) · 📚 被引 63
- **作者**: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, Song Han
- **🏷️ 机构**: Shanghai Qi Zhi Institute, MIT
- **会议**: CVPR 2023
- **摘要（中）**: ①针对高分辨率视觉Transformer计算复杂度高、难以在延迟敏感应用（如自动驾驶）中部署的问题。②提出SparseViT，利用窗口注意力的批处理特性实现激活剪枝，引入稀疏感知适应和进化搜索优化层间稀疏配置。③相比CNN，窗口ViT能实现实际加速，60%稀疏度下延迟降低约50%。④在单目3D检测等任务上，相比密集模型实现1.5倍、1.4倍和1.3倍加速。
- **摘要（英）**: This paper addresses the high computational cost of high-resolution vision transformers in latency-sensitive applications. It proposes SparseViT, which leverages window attention batching for activation pruning and evolutionary search for optimal layerwise sparsity. This achieves ~50% latency reduction at 60% sparsity and 1.3-1.5x speedups in monocular 3D detection.
- **核心贡献**: 提出基于窗口激活剪枝的高效ViT框架，实现实际加速。
- **创新点**: 利用窗口注意力批处理特性实现激活稀疏，结合进化搜索优化配置。
- **结果**: 在单目3D检测中实现1.3-1.5倍加速。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> High-resolution images enable neural networks to learn richer visual representations. However, this improved performance comes at the cost of growing computational complexity, hindering their usage in latency-sensitive applications. As not all pixels are equal, skipping computations for less-important regions offers a simple and effective measure to reduce the computation. This, however, is hard to be translated into actual speedup for CNNs since it breaks the regularity of the dense convolution workload. In this paper, we introduce SparseViT that revisits activation sparsity for recent window-based vision transformers (ViTs). As window attentions are naturally batched over blocks, actual speedup with window activation pruning becomes possible: i.e., ~50% latency reduction with 60% sparsity. Different layers should be assigned with different pruning ratios due to their diverse sensitivities and computational costs. We introduce sparsity-aware adaptation and apply the evolutionary search to efficiently find the optimal layerwise sparsity configuration within the vast search space. SparseViT achieves speedups of 1.5x, 1.4x, and 1.3x compared to its dense counterpart in monocular 3D object detection, 2D instance segmentation, and 2D semantic segmentation, respectively, with negligible to no loss of accuracy.

</details>

### SemiCVT: Semi-Supervised Convolutional Vision Transformer for Semantic Segmentation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01091) · 📚 被引 39
- **作者**: Huimin Huang, Shiao Xie, Lanfen Lin, Ruofeng Tong, Yen-Wei Chen, Yuexiang Li et al.
- **🏷️ 机构**: Zhejiang University, Ritsumeikan University, Tencent Jarvis Lab
- **会议**: CVPR 2023
- **摘要（中）**: 针对语义分割中标注数据稀缺的问题，提出半监督卷积视觉Transformer（SemiCVT），结合卷积和Transformer架构，利用少量标注和大量未标注数据进行训练。方法通过一致性正则化和伪标签策略，在未标注数据上增强模型泛化能力。相比纯监督方法，在PASCAL VOC等数据集上显著提升分割精度，尤其在标注比例较低时优势明显。
- **摘要（英）**: This paper tackles the scarcity of labeled data in semantic segmentation by proposing SemiCVT, a semi-supervised convolutional vision transformer that leverages both labeled and unlabeled data. It employs consistency regularization and pseudo-labeling to improve generalization. Experiments on PASCAL VOC show significant accuracy gains, especially with low annotation ratios.
- **核心贡献**: 提出半监督卷积视觉Transformer框架，有效利用未标注数据提升分割性能。
- **创新点**: 结合卷积和Transformer架构，并设计一致性正则化与伪标签策略。
- **结果**: 在PASCAL VOC上显著提升分割精度，尤其在低标注比例下。

### Distilling Self-Supervised Vision Transformers for Weakly-Supervised Few-Shot Classification & Segmentation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2307.03407](https://arxiv.org/abs/2307.03407) · 📚 被引 42
- **作者**: Dahyun Kang, Piotr Koniusz, Minsu Cho, Naila Murray
- **🏷️ 机构**: Meta AI, Data61 &#x2665; CSIRO, POSTECH
- **会议**: CVPR 2023
- **摘要（中）**: 针对弱监督少样本分类与分割任务中像素级标签缺失的问题，利用自监督预训练的ViT，通过自注意力机制生成注意力图作为像素级伪标签，实现仅用图像级标签训练分类和分割头。同时探索混合监督设置，提出伪标签增强器利用少量真实像素标签改进伪标签质量。在Pascal-5i和COCO-20i上，多种监督设置下均取得显著性能提升，尤其在像素级标签极少时。
- **摘要（英）**: This paper addresses weakly-supervised few-shot classification and segmentation by leveraging a self-supervised ViT, using attention maps as pixel-level pseudo-labels from image-level labels only. It also proposes a pseudo-label enhancer for mixed supervision with a few ground-truth labels. Experiments on Pascal-5i and COCO-20i show significant gains, especially with scarce pixel-level annotations.
- **核心贡献**: 提出基于自监督ViT的弱监督少样本分类与分割方法，并设计伪标签增强器。
- **创新点**: 利用自监督ViT的注意力图作为伪标签，并支持混合监督设置。
- **结果**: 在Pascal-5i和COCO-20i上显著提升性能，尤其在低像素标签场景。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We address the task of weakly-supervised few-shot image classification and segmentation, by leveraging a Vision Transformer (ViT) pretrained with self-supervision. Our proposed method takes token representations from the self-supervised ViT and leverages their correlations, via self-attention, to produce classification and segmentation predictions through separate task heads. Our model is able to effectively learn to perform classification and segmentation in the absence of pixel-level labels during training, using only image-level labels. To do this it uses attention maps, created from tokens generated by the self-supervised ViT backbone, as pixel-level pseudo-labels. We also explore a practical setup with ``mixed" supervision, where a small number of training images contains ground-truth pixel-level labels and the remaining images have only image-level labels. For this mixed setup, we propose to improve the pseudo-labels using a pseudo-label enhancer that was trained using the available ground-truth pixel-level labels. Experiments on Pascal-5i and COCO-20i demonstrate significant performance gains in a variety of supervision settings, and in particular when little-to-no pixel-level labels are available.

</details>

### Vision Transformers are Parameter-Efficient Audio-Visual Learners. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2212.07983](https://arxiv.org/abs/2212.07983) · 📚 被引 90
- **作者**: Yan-Bo Lin, Yi-Lin Sung, Jie Lei, Mohit Bansal, Gedas Bertasius
- **🏷️ 机构**: UNC Chapel Hill,Department of Computer Science
- **会议**: CVPR 2023
- **摘要（中）**: 针对视觉Transformer在多模态任务中微调成本高和跨模态融合效率低的问题，提出LAVISH适配器，在冻结的视觉预训练ViT中注入少量可训练参数，实现音频-视觉任务的高效适应。适配器使用少量潜在token形成注意力瓶颈，避免标准交叉注意力的二次复杂度。相比现有模态特定方法，在多个音频-视觉任务上达到竞争或更优性能，同时减少可调参数，无需音频预训练或外部编码器。
- **摘要（英）**: This paper addresses the high fine-tuning cost and inefficient fusion in ViTs for audio-visual tasks by proposing LAVISH, a latent audio-visual hybrid adapter that injects few trainable parameters into a frozen ViT. It uses latent tokens as an attention bottleneck to reduce complexity. It achieves competitive or better performance on audio-visual benchmarks with fewer parameters and no audio pretraining.
- **核心贡献**: 提出LAVISH适配器，实现冻结ViT对音频-视觉任务的高效参数适应。
- **创新点**: 利用潜在token形成注意力瓶颈，消除交叉注意力二次复杂度。
- **结果**: 在多个音频-视觉任务上达到竞争性能，同时减少参数和训练成本。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision transformers (ViTs) have achieved impressive results on various computer vision tasks in the last several years. In this work, we study the capability of frozen ViTs, pretrained only on visual data, to generalize to audio-visual data without finetuning any of its original parameters. To do so, we propose a latent audio-visual hybrid (LAVISH) adapter that adapts pretrained ViTs to audio-visual tasks by injecting a small number of trainable parameters into every layer of a frozen ViT. To efficiently fuse visual and audio cues, our LAVISH adapter uses a small set of latent tokens, which form an attention bottleneck, thus, eliminating the quadratic cost of standard cross-attention. Compared to the existing modality-specific audio-visual methods, our approach achieves competitive or even better performance on various audio-visual tasks while using fewer tunable parameters and without relying on costly audio pretraining or external audio encoders. Our code is available at https://genjib.github.io/project_page/LAVISH/

</details>

### BiFormer: Vision Transformer with Bi-Level Routing Attention.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00995) · 📚 被引 1070
- **作者**: Lei Zhu, Xinjiang Wang, Zhanghan Ke, Wayne Zhang, Rynson W. H. Lau
- **🏷️ 机构**: City University of Hong Kong, SenseTime Research
- **会议**: CVPR 2023

### PARTICLE: Part Discovery and Contrastive Learning for Fine-grained Recognition.
- **链接**: [arXiv:2309.13822](https://arxiv.org/abs/2309.13822) · 📚 被引 6
- **作者**: Oindrila Saha, Subhransu Maji
- **🏷️ 机构**: University of Massachusetts,Amherst
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We develop techniques for refining representations for fine-grained classification and segmentation tasks in a self-supervised manner. We find that fine-tuning methods based on instance-discriminative contrastive learning are not as effective, and posit that recognizing part-specific variations is crucial for fine-grained categorization. We present an iterative learning approach that incorporates part-centric equivariance and invariance objectives. First, pixel representations are clustered to discover parts. We analyze the representations from convolutional and vision transformer networks that are best suited for this task. Then, a part-centric learning step aggregates and contrasts representations of parts within an image. We show that this improves the performance on image classification and part segmentation tasks across datasets. For example, under a linear-evaluation scheme, the classification accuracy of a ResNet50 trained on ImageNet using DetCon, a self-supervised learning approach, improves from 35.4% to 42.0% on the Caltech-UCSD Birds, from 35.5% to 44.1% on the FGVC Aircraft, and from 29.7% to 37.4% on the Stanford Cars. We also observe significant gains in few-shot part segmentation tasks using the proposed technique, while instance-discriminative learning was not as effective. Smaller, yet consistent, improvements are also observed for stronger networks based on transformers.

</details>

### HiViT: A Simpler and More Efficient Design of Hierarchical Vision Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=3F6I-0-57SC)
- **作者**: Xiaosong Zhang, Yunjie Tian, Lingxi Xie, Wei Huang, Qi Dai, Qixiang Ye et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Vision Transformer Adapter for Dense Predictions.
- **链接**: [出版页](https://openreview.net/forum?id=plKu2GByCNW)
- **作者**: Zhe Chen, Yuchen Duan, Wenhai Wang, Junjun He, Tong Lu, Jifeng Dai et al.
- **🏷️ 机构**: Shanghai AI Lab, Tsinghua / Shanghai AI Lab
- **会议**: ICLR 2023

### Budgeted Training for Vision Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=sVzBN-DlJRi)
- **作者**: Zhuofan Xia, Xuran Pan, Xuan Jin, Yuan He, Hui Xue, Shiji Song et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### GPViT: A High Resolution Non-Hierarchical Vision Transformer with Group Propagation.
- **链接**: [出版页](https://openreview.net/forum?id=IowKt5rYWsK)
- **作者**: Chenhongyi Yang, Jiarui Xu, Shalini De Mello, Elliot J. Crowley, Xiaolong Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### MixPro: Data Augmentation with MaskMix and Progressive Attention Labeling for Vision Transformer.
- **链接**: [出版页](https://openreview.net/forum?id=dRjWsd3gwsm)
- **作者**: Qihao Zhao, Yangyu Huang, Wei Hu, Fan Zhang, Jun Liu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2023

### Understanding and Defending Patched-based Adversarial Attacks for Vision Transformer.
- **链接**: [出版页](https://proceedings.mlr.press/v202/liu23n.html)
- **作者**: Liang Liu, Yanan Guo, Youtao Zhang, Jun Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

### Hiera: A Hierarchical Vision Transformer without the Bells-and-Whistles.
- **链接**: [出版页](https://proceedings.mlr.press/v202/ryali23a.html)
- **作者**: Chaitanya Ryali, Yuan-Ting Hu, Daniel Bolya, Chen Wei, Haoqi Fan, Po-Yao Huang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2023

## 跨领域论文（完整笔记在其他领域）

- Transformer-Based Sensor Fusion for Autonomous Driving: A Survey. → [autonomous-driving](../autonomous-driving/Guideline%202023.md)
- Architecture-Agnostic Masked Image Modeling - From ViT back to CNN. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment. → [vlm](../vlm/Guideline%202023.md)
- MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer. → [3d-detection](../3d-detection/Guideline%202023.md)
- MDL-NAS: A Joint Multi-domain Learning Framework for Vision Transformer. → [neural-architecture-search](../neural-architecture-search/Guideline%202023.md)
- Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers. → [network-pruning](../network-pruning/Guideline%202023.md)
- Global Vision Transformer Pruning with Hessian-Aware Saliency. → [network-pruning](../network-pruning/Guideline%202023.md)
- Boost Vision Transformer with GPU-Friendly Sparsity and Quantization. → [network-pruning](../network-pruning/Guideline%202023.md)
- X-Pruner: eXplainable Pruning for Vision Transformers. → [network-pruning](../network-pruning/Guideline%202023.md)
- CODA-Prompt: COntinual Decomposed Attention-Based Prompting for Rehearsal-Free Continual Learning. → [continual-learning](../continual-learning/Guideline%202023.md)
- DepGraph: Towards Any Structural Pruning. → [network-pruning](../network-pruning/Guideline%202023.md)
- Masked Video Distillation: Rethinking Masked Feature Modeling for Self-supervised Video Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- Unleashing Vanilla Vision Transformer with Masked Image Modeling for Object Detection. → [self-supervised-vision](../self-supervised-vision/Guideline%202023.md)
- A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- CLIPN for Zero-Shot OOD Detection: Teaching CLIP to Say No. → [vlm](../vlm/Guideline%202023.md)
- DiffRate : Differentiable Compression Rate for Efficient Vision Transformers. → [network-pruning](../network-pruning/Guideline%202023.md)
- Contrastive Feature Masking Open-Vocabulary Vision Transformer. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- ElasticViT: Conflict-aware Supernet Training for Deploying Fast Vision Transformer on Diverse Mobile Devices. → [neural-architecture-search](../neural-architecture-search/Guideline%202023.md)
- InstaTune: Instantaneous Neural Architecture Search During Fine-Tuning. → [neural-architecture-search](../neural-architecture-search/Guideline%202023.md)
- Can Unstructured Pruning Reduce the Depth in Deep Neural Networks? → [network-pruning](../network-pruning/Guideline%202023.md)
- TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance. → [vlm](../vlm/Guideline%202023.md)

<!-- COMPLETE v1 papers=38 -->
