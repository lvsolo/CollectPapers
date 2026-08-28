# Vision Transformer — 2023 Guideline

> 领域: 视觉 Transformer（ViT、混合架构、高效注意力）
> 论文数: 23 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Video OWL-ViT: Temporally-consistent open-world localization in video.
- **链接**: [arXiv:2308.11093](https://arxiv.org/abs/2308.11093) · 📚 被引 11
- **作者**: Georg Heigold, Daniel Keysers, Matthias Minderer, Mario Lucic, Alexey A. Gritsenko, Fisher Yu et al.
- **🏷️ 机构**: Google DeepMind, ETH Zurich
- **会议**: ICCV 2023

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

### I-ViT: Integer-only Quantization for Efficient Vision Transformer Inference.
- **链接**: [arXiv:2207.01405](https://arxiv.org/abs/2207.01405) · [代码](https://github.com/zkkli/I-ViT) · 📚 被引 122
- **作者**: Zhikai Li, Qingyi Gu
- **🏷️ 机构**: Chinese Academy of Sciences,Institute of Automation
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision Transformers (ViTs) have achieved state-of-the-art performance on various computer vision applications. However, these models have considerable storage and computational overheads, making their deployment and efficient inference on edge devices challenging. Quantization is a promising approach to reducing model complexity, and the dyadic arithmetic pipeline can allow the quantized models to perform efficient integer-only inference. Unfortunately, dyadic arithmetic is based on the homogeneity condition in convolutional neural networks, which is not applicable to the non-linear components in ViTs, making integer-only inference of ViTs an open issue. In this paper, we propose I-ViT, an integer-only quantization scheme for ViTs, to enable ViTs to perform the entire computational graph of inference with integer arithmetic and bit-shifting, and without any floating-point arithmetic. In I-ViT, linear operations (e.g., MatMul and Dense) follow the integer-only pipeline with dyadic arithmetic, and non-linear operations (e.g., Softmax, GELU, and LayerNorm) are approximated by the proposed light-weight integer-only arithmetic methods. More specifically, I-ViT applies the proposed Shiftmax and ShiftGELU, which are designed to use integer bit-shifting to approximate the corresponding floating-point operations. We evaluate I-ViT on various benchmark models and the results show that integer-only INT8 quantization achieves comparable (or even slightly higher) accuracy to the full-precision (FP) baseline. Furthermore, we utilize TVM for practical hardware deployment on the GPU's integer arithmetic units, achieving 3.72$\sim$4.11$\times$ inference speedup compared to the FP model. Code of both Pytorch and TVM is released at https://github.com/zkkli/I-ViT.

</details>

### SemiCVT: Semi-Supervised Convolutional Vision Transformer for Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01091) · 📚 被引 39
- **作者**: Huimin Huang, Shiao Xie, Lanfen Lin, Ruofeng Tong, Yen-Wei Chen, Yuexiang Li et al.
- **🏷️ 机构**: Zhejiang University, Ritsumeikan University, Tencent Jarvis Lab
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

### EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention.
- **链接**: [arXiv:2305.07027](https://arxiv.org/abs/2305.07027) · [代码](https://github.com/microsoft/Cream) · 📚 被引 828
- **作者**: Xinyu Liu, Houwen Peng, Ningxin Zheng, Yuqing Yang, Han Hu, Yixuan Yuan
- **🏷️ 机构**: The Chinese University of Hong Kong, Microsoft Research
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Post-training quantization (PTQ), which only requires a tiny dataset for calibration without end-to-end retraining, is a light and practical model compression technique. Recently, several PTQ schemes for vision transformers (ViTs) have been presented; unfortunately, they typically suffer from non-trivial accuracy degradation, especially in low-bit cases. In this paper, we propose RepQ-ViT, a novel PTQ framework for ViTs based on quantization scale reparameterization, to address the above issues. RepQ-ViT decouples the quantization and inference processes, where the former employs complex quantizers and the latter employs scale-reparameterized simplified quantizers. This ensures both accurate quantization and efficient inference, which distinguishes it from existing approaches that sacrifice quantization performance to meet the target hardware. More specifically, we focus on two components with extreme distributions: post-LayerNorm activations with severe inter-channel variation and post-Softmax activations with power-law features, and initially apply channel-wise quantization and log$\sqrt{2}$ quantization, respectively. Then, we reparameterize the scales to hardware-friendly layer-wise quantization and log2 quantization for inference, with only slight accuracy or computational costs. Extensive experiments are conducted on multiple vision tasks with different model variants, proving that RepQ-ViT, without hyperparameters and expensive reconstruction procedures, can outperform existing strong baselines and encouragingly improve the accuracy of 4-bit PTQ of ViTs to a usable level. Code is available at https://github.com/zkkli/RepQ-ViT.

</details>

### HM-ViT: Hetero-modal Vehicle-to-Vehicle Cooperative Perception with Vision Transformer.
- **链接**: [arXiv:2304.10628](https://arxiv.org/abs/2304.10628) · 📚 被引 100
- **作者**: Hao Xiang, Runsheng Xu, Jiaqi Ma
- **🏷️ 机构**: University of California,Los Angeles
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vehicle-to-Vehicle technologies have enabled autonomous vehicles to share information to see through occlusions, greatly enhancing perception performance. Nevertheless, existing works all focused on homogeneous traffic where vehicles are equipped with the same type of sensors, which significantly hampers the scale of collaboration and benefit of cross-modality interactions. In this paper, we investigate the multi-agent hetero-modal cooperative perception problem where agents may have distinct sensor modalities. We present HM-ViT, the first unified multi-agent hetero-modal cooperative perception framework that can collaboratively predict 3D objects for highly dynamic vehicle-to-vehicle (V2V) collaborations with varying numbers and types of agents. To effectively fuse features from multi-view images and LiDAR point clouds, we design a novel heterogeneous 3D graph transformer to jointly reason inter-agent and intra-agent interactions. The extensive experiments on the V2V perception dataset OPV2V demonstrate that the HM-ViT outperforms SOTA cooperative perception methods for V2V hetero-modal cooperative perception. We will release codes to facilitate future research.

</details>

### Order-ViT: Order Learning Vision Transformer for Cancer Classification in Pathology Images.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00263) · 📚 被引 8
- **作者**: Ju Cheon Lee, Jin Tae Kwak
- **🏷️ 机构**: Korea University,School of Electrical Engineering,Seoul,Republic of Korea
- **会议**: ICCV 2023

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

### A Comparative Study of Vision Transformer Encoders and Few-shot Learning for Medical Image Classification.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00265) · 📚 被引 17
- **作者**: Maxat Nurgazin, Nguyen Anh Tu
- **🏷️ 机构**: Nazarbayev University,School of Engineering and Digital Sciences,Department of Computer Science,Astana,Kazakhstan,010000
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

> The advent of high-capacity pre-trained models has revolutionized problem-solving in computer vision, shifting the focus from training task-specific models to adapting pre-trained models. Consequently, effectively adapting large pre-trained models to downstream tasks in an efficient manner has become a prominent research area. Existing solutions primarily concentrate on designing lightweight adapters and their interaction with pre-trained models, with the goal of minimizing the number of parameters requiring updates. In this study, we propose a novel Adapter Re-Composing (ARC) strategy that addresses efficient pre-trained model adaptation from a fresh perspective. Our approach considers the reusability of adaptation parameters and introduces a parameter-sharing scheme. Specifically, we leverage symmetric down-/up-projections to construct bottleneck operations, which are shared across layers. By learning low-dimensional re-scaling coefficients, we can effectively re-compose layer-adaptive adapters. This parameter-sharing strategy in adapter design allows us to significantly reduce the number of new parameters while maintaining satisfactory performance, thereby offering a promising approach to compress the adaptation cost. We conduct experiments on 24 downstream image classification tasks using various Vision Transformer variants to evaluate our method. The results demonstrate that our approach achieves compelling transfer learning performance with a reduced parameter count. Our code is available at \href{https://github.com/DavidYanAnDe/ARC}{https://github.com/DavidYanAnDe/ARC}.

- T-FFTRadNet: Object Detection with Swin Vision Transformers from Raw ADC Radar Signals. → [object-detection](../object-detection/Guideline%202023.md)
- MMST-ViT: Climate Change-aware Crop Yield Prediction via Multi-Modal Spatial-Temporal Vision Transformer. → [multimodal](../multimodal/Guideline%202023.md)
- Unleashing Vanilla Vision Transformer with Masked Image Modeling for Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202023.md)
- Contrastive Feature Masking Open-Vocabulary Vision Transformer. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- ElasticViT: Conflict-aware Supernet Training for Deploying Fast Vision Transformer on Diverse Mobile Devices. → [neural-architecture-search](../neural-architecture-search/Guideline%202023.md)
