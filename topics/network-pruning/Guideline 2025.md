# Network Pruning — 2025 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 25 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### LINR-PCGC: Lossless Implicit Neural Representations for Point Cloud Geometry Compression.
- **链接**: [arXiv:2507.15686](https://arxiv.org/abs/2507.15686) · 📚 被引 1
- **作者**: Wenjie Huang, Qi Yang, Shuting Xia, He Huang, Yiling Xu, Zhu Li
- **🏷️ 机构**: Shanghai Jiao Tong University, University of Missouri-Kansas City
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing AI-based point cloud compression methods struggle with dependence on specific training data distributions, which limits their real-world deployment. Implicit Neural Representation (INR) methods solve the above problem by encoding overfitted network parameters to the bitstream, resulting in more distribution-agnostic results. However, due to the limitation of encoding time and decoder size, current INR based methods only consider lossy geometry compression. In this paper, we propose the first INR based lossless point cloud geometry compression method called Lossless Implicit Neural Representations for Point Cloud Geometry Compression (LINR-PCGC). To accelerate encoding speed, we design a group of point clouds level coding framework with an effective network initialization strategy, which can reduce around 60% encoding time. A lightweight coding network based on multiscale SparseConv, consisting of scale context extraction, child node prediction, and model compression modules, is proposed to realize fast inference and compact decoder size. Experimental results show that our method consistently outperforms traditional and AI-based methods: for example, with the convergence time in the MVUB dataset, our method reduces the bitstream by approximately 21.21% compared to G-PCC TMC13v23 and 21.95% compared to SparsePCGC. Our project can be seen on https://huangwenjie2023.github.io/LINR-PCGC/.

</details>

### General Compression Framework for Efficient Transformer Object Tracking.
- **链接**: [arXiv:2409.17564](https://arxiv.org/abs/2409.17564) · [代码](https://github.com/LingyiHongfd/CompressTracker) · 📚 被引 3
- **作者**: Lingyi Hong, Jinglun Li, Xinyu Zhou, Shilin Yan, Pinxue Guo, Kaixun Jiang et al.
- **🏷️ 机构**: College of Computer Science and Artificial Intelligence, Fudan University,Shanghai Key Lab of Intelligent Information Processing,China, College of Intelligent Robotics and Advanced Manufacturing, Fudan University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous works have attempted to improve tracking efficiency through lightweight architecture design or knowledge distillation from teacher models to compact student trackers. However, these solutions often sacrifice accuracy for speed to a great extent, and also have the problems of complex training process and structural limitations. Thus, we propose a general model compression framework for efficient transformer object tracking, named CompressTracker, to reduce model size while preserving tracking accuracy. Our approach features a novel stage division strategy that segments the transformer layers of the teacher model into distinct stages to break the limitation of model structure. Additionally, we also design a unique replacement training technique that randomly substitutes specific stages in the student model with those from the teacher model, as opposed to training the student model in isolation. Replacement training enhances the student model's ability to replicate the teacher model's behavior and simplifies the training process. To further forcing student model to emulate teacher model, we incorporate prediction guidance and stage-wise feature mimicking to provide additional supervision during the teacher model's compression process. CompressTracker is structurally agnostic, making it compatible with any transformer architecture. We conduct a series of experiment to verify the effectiveness and generalizability of our CompressTracker. Our CompressTracker-SUTrack, compressed from SUTrack, retains about 99 performance on LaSOT (72.2 AUC) while achieves 2.42x speed up. Code is available at https://github.com/LingyiHongfd/CompressTracker.

</details>

### Mixa-Q: Revisiting Activation Sparsity for Vision Transformers From a Mixed-Precision Quantization Perspective.
- **链接**: [arXiv:2507.19131](https://arxiv.org/abs/2507.19131) · 📚 被引 2
- **作者**: Weitian Wang, Shubham Rai, Cecilia De la Parra, Akash Kumar
- **🏷️ 机构**: Robert Bosch GmbH,Renningen,Germany
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose MixA-Q, a mixed-precision activation quantization framework that leverages intra-layer activation sparsity (a concept widely explored in activation pruning methods) for efficient inference of quantized window-based vision transformers. For a given uniform-bit quantization configuration, MixA-Q separates the batched window computations within Swin blocks and assigns a lower bit width to the activations of less important windows, improving the trade-off between model performance and efficiency. We introduce a Two-Branch Swin Block that processes activations separately in high- and low-bit precision, enabling seamless integration of our method with most quantization-aware training (QAT) and post-training quantization (PTQ) methods, or with simple modifications. Our experimental evaluations over the COCO dataset demonstrate that MixA-Q achieves a training-free 1.35x computational speedup without accuracy loss in PTQ configuration. With QAT, MixA-Q achieves a lossless 1.25x speedup and a 1.53x speedup with only a 1% mAP drop by incorporating activation pruning. Notably, by reducing the quantization error in important regions, our sparsity-aware quantization adaptation improves the mAP of the quantized W4A4 model (with both weights and activations in 4-bit precision) by 0.7%, reducing quantization degradation by 24%.

</details>

### Cross-Granularity Online Optimization with Masked Compensated Information for Learned Image Compression.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01533) · 📚 被引 1
- **作者**: Haowei Kuang, Wenhan Yang, Zongming Guo, Jiaying Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China, Pengcheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

### DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer.
- **链接**: [arXiv:2507.04947](https://arxiv.org/abs/2507.04947) · 📚 被引 1
- **作者**: Yecheng Wu, Junyu Chen, Zhuoyang Zhang, Enze Xie, Jincheng Yu, Junsong Chen et al.
- **🏷️ 机构**: MIT NVIDIA
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce DC-AR, a novel masked autoregressive (AR) text-to-image generation framework that delivers superior image generation quality with exceptional computational efficiency. Due to the tokenizers' limitations, prior masked AR models have lagged behind diffusion models in terms of quality or efficiency. We overcome this limitation by introducing DC-HT - a deep compression hybrid tokenizer for AR models that achieves a 32x spatial compression ratio while maintaining high reconstruction fidelity and cross-resolution generalization ability. Building upon DC-HT, we extend MaskGIT and create a new hybrid masked autoregressive image generation framework that first produces the structural elements through discrete tokens and then applies refinements via residual tokens. DC-AR achieves state-of-the-art results with a gFID of 5.49 on MJHQ-30K and an overall score of 0.69 on GenEval, while offering 1.5-7.9x higher throughput and 2.0-3.5x lower latency compared to prior leading diffusion and autoregressive models.

</details>

### Variance-Based Pruning for Accelerating and Compressing Trained Networks.
- **链接**: [arXiv:2507.12988](https://arxiv.org/abs/2507.12988) · [代码](https://github.com/boschresearch/variance-based-pruning) · 📚 被引 2
- **作者**: Uranik Berisha, Jens Mehnert, Alexandru Paul Condurache
- **🏷️ 机构**: GmbH,Automated Driving Research, Robert Bosch,Stuttgart,Germany,70469
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Increasingly expensive training of ever larger models such as Vision Transfomers motivate reusing the vast library of already trained state-of-the-art networks. However, their latency, high computational costs and memory demands pose significant challenges for deployment, especially on resource-constrained hardware. While structured pruning methods can reduce these factors, they often require costly retraining, sometimes for up to hundreds of epochs, or even training from scratch to recover the lost accuracy resulting from the structural modifications. Maintaining the provided performance of trained models after structured pruning and thereby avoiding extensive retraining remains a challenge. To solve this, we introduce Variance-Based Pruning, a simple and structured one-shot pruning technique for efficiently compressing networks, with minimal finetuning. Our approach first gathers activation statistics, which are used to select neurons for pruning. Simultaneously the mean activations are integrated back into the model to preserve a high degree of performance. On ImageNet-1k recognition tasks, we demonstrate that directly after pruning DeiT-Base retains over 70% of its original performance and requires only 10 epochs of fine-tuning to regain 99% of the original accuracy while simultaneously reducing MACs by 35% and model size by 36%, thus speeding up the model by 1.44x. The code is available at: https://github.com/boschresearch/variance-based-pruning

</details>

### Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02119) · 📚 被引 1
- **作者**: Mark Endo, Xiaohan Wang, Serena Yeung-Levy
- **🏷️ 机构**: Stanford University,USA
- **会议**: ICCV 2025

### FastVAR: Linear Visual Autoregressive Modeling Via Cached Token Pruning.
- **链接**: [arXiv:2503.23367](https://arxiv.org/abs/2503.23367) · [代码](https://github.com/csguoh/FastVAR) · 📚 被引 2
- **作者**: Hang Guo, Yawei Li, Taolin Zhang, Jiangshan Wang, Tao Dai, Shu-Tao Xia et al.
- **🏷️ 机构**: Tsinghua University, ETH Zurich, Shenzhen University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual Autoregressive (VAR) modeling has gained popularity for its shift towards next-scale prediction. However, existing VAR paradigms process the entire token map at each scale step, leading to the complexity and runtime scaling dramatically with image resolution. To address this challenge, we propose FastVAR, a post-training acceleration method for efficient resolution scaling with VARs. Our key finding is that the majority of latency arises from the large-scale step where most tokens have already converged. Leveraging this observation, we develop the cached token pruning strategy that only forwards pivotal tokens for scale-specific modeling while using cached tokens from previous scale steps to restore the pruned slots. This significantly reduces the number of forwarded tokens and improves the efficiency at larger resolutions. Experiments show the proposed FastVAR can further speedup FlashAttention-accelerated VAR by 2.7$\times$ with negligible performance drop of <1%. We further extend FastVAR to zero-shot generation of higher resolution images. In particular, FastVAR can generate one 2K image with 15GB memory footprints in 1.5s on a single NVIDIA 3090 GPU. Code is available at https://github.com/csguoh/FastVAR.

</details>

### MosaicDiff: Training-free Structural Pruning for Diffusion Model Acceleration Reflecting Pretraining Dynamics.
- **链接**: [arXiv:2510.11962](https://arxiv.org/abs/2510.11962) · 📚 被引 1
- **作者**: Bowei Guo, Shengkun Tang, Cong Zeng, Zhiqiang Shen
- **🏷️ 机构**: Mohamed bin Zayed University of Artificial Intelligence
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models are renowned for their generative capabilities, yet their pretraining processes exhibit distinct phases of learning speed that have been entirely overlooked in prior post-training acceleration efforts in the community. In this study, we introduce a novel framework called MosaicDiff that aligns diffusion pretraining dynamics with post-training sampling acceleration via trajectory-aware structural pruning. Our approach leverages the observation that the middle, fast-learning stage of diffusion pretraining requires more conservative pruning to preserve critical model features, while the early and later, slow-learning stages benefit from a more aggressive pruning strategy. This adaptive pruning mechanism is the first to explicitly mirror the inherent learning speed variations of diffusion pretraining, thereby harmonizing the model's inner training dynamics with its accelerated sampling process. Extensive experiments on DiT and SDXL demonstrate that our method achieves significant speed-ups in sampling without compromising output quality, outperforming previous state-of-the-art methods by large margins, also providing a new viewpoint for more efficient and robust training-free diffusion acceleration.

</details>

### Keyframe-Oriented Vision Token Pruning: Enhancing Efficiency of Large Vision Language Models on Long-form Video Processing.
- **链接**: [arXiv:2503.10742](https://arxiv.org/abs/2503.10742) · 📚 被引 2
- **作者**: Yudong Liu, Jingwei Sun, Yueqian Lin, Jianyi Zhang, Jingyang Zhang, Ming Yin et al.
- **🏷️ 机构**: Duke University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision language models (VLMs) demonstrate strong capabilities in jointly processing visual and textual data. However, they often incur substantial computational overhead due to redundant visual information, particularly in long-form video scenarios. Existing approaches predominantly focus on either vision token pruning, which may overlook spatio-temporal dependencies, or keyframe selection, which identifies informative frames but discards others, thus disrupting contextual continuity. In this work, we propose KVTP (Keyframe-oriented Vision Token Pruning), a novel framework that overcomes the drawbacks of token pruning and keyframe selection. By adaptively assigning pruning rates based on frame relevance to the query, KVTP effectively retains essential contextual information while significantly reducing redundant computation. To thoroughly evaluate the long-form video understanding capacities of VLMs, we curated and reorganized subsets from VideoMME, EgoSchema, and NextQA into a unified benchmark named SparseKV-QA that highlights real-world scenarios with sparse but crucial events. Our experiments with VLMs of various scales show that KVTP can reduce token usage by 80% without compromising spatiotemporal and contextual consistency, significantly cutting computation while maintaining the performance. These results demonstrate our approach's effectiveness in efficient long-video processing, facilitating more scalable VLM deployment.

</details>

### METEOR: Multi-Encoder Collaborative Token Pruning for Efficient Vision Language Models.
- **链接**: [arXiv:2507.20842](https://arxiv.org/abs/2507.20842) · [代码](https://github.com/YuchenLiu98/METEOR) · 📚 被引 0
- **作者**: Yuchen Liu, Yaoming Wang, Bowen Shi, Xiaopeng Zhang, Wenrui Dai, Chenglin Li et al.
- **🏷️ 机构**: Shanghai Jiao Tong University,China, Meituan Inc.,China, Huawei Inc.,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision encoders serve as the cornerstone of multimodal understanding. Single-encoder architectures like CLIP exhibit inherent constraints in generalizing across diverse multimodal tasks, while recent multi-encoder fusion methods introduce prohibitive computational overhead to achieve superior performance using complementary visual representations from multiple vision encoders. To address this, we propose a progressive pruning framework, namely Multi-Encoder collaboraTivE tOken pRuning (METEOR), that eliminates redundant visual tokens across the encoding, fusion, and decoding stages for multi-encoder MLLMs. For multi-vision encoding, we discard redundant tokens within each encoder via a rank guided collaborative token assignment strategy. Subsequently, for multi-vision fusion, we combine the visual features from different encoders while reducing cross-encoder redundancy with cooperative pruning. Finally, we propose an adaptive token pruning method in the LLM decoding stage to further discard irrelevant tokens based on the text prompts with dynamically adjusting pruning ratios for specific task demands. To our best knowledge, this is the first successful attempt that achieves an efficient multi-encoder based vision language model with multi-stage pruning strategies. Extensive experiments on 11 benchmarks demonstrate the effectiveness of our proposed approach. Compared with EAGLE, a typical multi-encoder MLLMs, METEOR reduces 76% visual tokens with only 0.3% performance drop in average. The code is available at https://github.com/YuchenLiu98/METEOR.

</details>

### When Large Vision-Language Model Meets Large Remote Sensing Imagery: Coarse-to-Fine Text-Guided Token Pruning.
- **链接**: [arXiv:2503.07588](https://arxiv.org/abs/2503.07588) · [代码](https://github.com/VisionXLab/LRS-VQA) · 📚 被引 2
- **作者**: Junwei Luo, Yingying Zhang, Xue Yang, Kang Wu, Qi Zhu, Lei Liang et al.
- **🏷️ 机构**: Wuhan University, Ant Group, SAIS, Shanghai Jiao Tong University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Efficient vision-language understanding of large Remote Sensing Images (RSIs) is meaningful but challenging. Current Large Vision-Language Models (LVLMs) typically employ limited pre-defined grids to process images, leading to information loss when handling gigapixel RSIs. Conversely, using unlimited grids significantly increases computational costs. To preserve image details while reducing computational complexity, we propose a text-guided token pruning method with Dynamic Image Pyramid (DIP) integration. Our method introduces: (i) a Region Focus Module (RFM) that leverages text-aware region localization capability to identify critical vision tokens, and (ii) a coarse-to-fine image tile selection and vision token pruning strategy based on DIP, which is guided by RFM outputs and avoids directly processing the entire large imagery. Additionally, existing benchmarks for evaluating LVLMs' perception ability on large RSI suffer from limited question diversity and constrained image sizes. We construct a new benchmark named LRS-VQA, which contains 7,333 QA pairs across 8 categories, with image length up to 27,328 pixels. Our method outperforms existing high-resolution strategies on four datasets using the same data. Moreover, compared to existing token reduction methods, our approach demonstrates higher efficiency under high-resolution settings. Dataset and code are in https://github.com/VisionXLab/LRS-VQA.

</details>

### WINS: Winograd Structured Pruning for Fast Winograd Convolution.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02087) · 📚 被引 0
- **作者**: Cheonjun Park, Hyun Jae Oh, Mincheol Park, Hyunchan Moon, Minsik Kim, Suhyun Kim et al.
- **🏷️ 机构**: Hankuk University of Foreign Studies, Yonsei University, Samsung Advanced Institute of Technology
- **会议**: ICCV 2025

### MOBIUS: Big-to-Mobile Universal Instance Segmentation via Multi-modal Bottleneck Fusion and Calibrated Decoder Pruning.
- **链接**: [arXiv:2510.15026](https://arxiv.org/abs/2510.15026) · 📚 被引 0
- **作者**: Mattia Segù, Marta Tintore Gazulla, Yongqin Xian, Luc Van Gool, Federico Tombari
- **🏷️ 机构**: Google, Sofia University,INSAIT
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Scaling up model size and training data has advanced foundation models for instance-level perception, achieving state-of-the-art in-domain and zero-shot performance across object detection and segmentation. However, their high computational cost limits adoption on resource-constrained platforms. We first examine the limitations of existing architectures in enabling efficient edge deployment without compromising performance. We then introduce MOBIUS, a family of foundation models for universal instance segmentation, designed for Pareto-optimal downscaling to support deployment across devices ranging from high-end accelerators to mobile hardware. To reduce training and inference demands, we propose: (i) a bottleneck pixel decoder for efficient multi-scale and multi-modal fusion, (ii) a language-guided uncertainty calibration loss for adaptive decoder pruning, and (iii) a streamlined, unified training strategy. Unlike efficient baselines that trade accuracy for reduced complexity, MOBIUS reduces pixel and transformer decoder FLOPs by up to 55% and 75%, respectively, while maintaining state-of-the-art performance in just a third of the training iterations. MOBIUS establishes a new benchmark for efficient segmentation on both high-performance computing platforms and mobile devices.

</details>

### Pruning All-Rounder: Rethinking and Improving Inference Efficiency for Large Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01883) · 📚 被引 0
- **作者**: Wei Suo, Ji Ma, Mengyang Sun, Lin Yuanbo Wu, Peng Wang, Yanning Zhang
- **🏷️ 机构**: Northwestern Polytechnical University,China, Swansea University,United Kingdom
- **会议**: ICCV 2025

### Partial Forward Blocking: A Novel Data Pruning Paradigm for Lossless Training Acceleration.
- **链接**: [arXiv:2506.23674](https://arxiv.org/abs/2506.23674) · 📚 被引 1
- **作者**: Dongyue Wu, Zilin Guo, Jialong Zuo, Nong Sang, Changxin Gao
- **🏷️ 机构**: School of Artifcial Intelligence and Automation, Huazhong University of Science and Technology,National Key Laboratory of Multispectral Information Intelligent Processing Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The ever-growing size of training datasets enhances the generalization capability of modern machine learning models but also incurs exorbitant computational costs. Existing data pruning approaches aim to accelerate training by removing those less important samples. However, they often rely on gradients or proxy models, leading to prohibitive additional costs of gradient back-propagation and proxy model training. In this paper, we propose Partial Forward Blocking (PFB), a novel framework for lossless training acceleration. The efficiency of PFB stems from its unique adaptive pruning pipeline: sample importance is assessed based on features extracted from the shallow layers of the target model. Less important samples are then pruned, allowing only the retained ones to proceed with the subsequent forward pass and loss back-propagation. This mechanism significantly reduces the computational overhead of deep-layer forward passes and back-propagation for pruned samples, while also eliminating the need for auxiliary backward computations and proxy model training. Moreover, PFB introduces probability density as an indicator of sample importance. Combined with an adaptive distribution estimation module, our method dynamically prioritizes relatively rare samples, aligning with the constantly evolving training state. Extensive experiments demonstrate the significant superiority of PFB in performance and speed. On ImageNet, PFB achieves a 0.5% accuracy improvement and 33% training time reduction with 40% data pruned.

</details>

### VFLowOpt: A Token Pruning Framework for LMMs with Visual Information Flow-Guided Optimization.
- **链接**: [arXiv:2508.05211](https://arxiv.org/abs/2508.05211) · 📚 被引 1
- **作者**: Sihan Yang, Runsen Xu, Chenhang Cui, Tai Wang, Dahua Lin, Jiangmiao Pang
- **🏷️ 机构**: Shanghai AI Laboratory, National University of Singapore
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large Multimodal Models (LMMs) excel in visual-language tasks by leveraging numerous visual tokens for fine-grained visual information, but this token redundancy results in significant computational costs. Previous research aimed at reducing visual tokens during inference typically leverages importance maps derived from attention scores among vision-only tokens or vision-language tokens to prune tokens across one or multiple pruning stages. Despite this progress, pruning frameworks and strategies remain simplistic and insufficiently explored, often resulting in substantial performance degradation. In this paper, we propose VFlowOpt, a token pruning framework that introduces an importance map derivation process and a progressive pruning module with a recycling mechanism. The hyperparameters of its pruning strategy are further optimized by a visual information flow-guided method. Specifically, we compute an importance map for image tokens based on their attention-derived context relevance and patch-level information entropy. We then decide which tokens to retain or prune and aggregate the pruned ones as recycled tokens to avoid potential information loss. Finally, we apply a visual information flow-guided method that regards the last token in the LMM as the most representative signal of text-visual interactions. This method minimizes the discrepancy between token representations in LMMs with and without pruning, thereby enabling superior pruning strategies tailored to different LMMs. Experiments demonstrate that VFlowOpt can prune 90% of visual tokens while maintaining comparable performance, leading to an 89% reduction in KV-Cache memory and 3.8 times faster inference.

</details>

### Beyond Text-Visual Attention: Exploiting Visual Cues for Effective Token Pruning in VLMs.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01939) · 📚 被引 6
- **作者**: Qizhe Zhang, Aosong Cheng, Ming Lu, Renrui Zhang, Zhiyong Zhuo, Jiajun Cao et al.
- **🏷️ 机构**: School of Computer Science, Peking University,State Key Laboratory for Multimedia Information Processing, CUHK MMLab, ByteDance
- **会议**: ICCV 2025

### AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning.
- **链接**: [arXiv:2412.03248](https://arxiv.org/abs/2412.03248) · [代码](https://github.com/LaVi-Lab/AIM) · 📚 被引 2
- **作者**: Yiwu Zhong, Zhuoming Liu, Yin Li, Liwei Wang
- **🏷️ 机构**: The Chinese University of Hong Kong, University of Wisconsin-Madison
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have enabled the creation of multi-modal LLMs that exhibit strong comprehension of visual data such as images and videos. However, these models usually rely on extensive visual tokens from visual encoders, leading to high computational demands, which limits their applicability in resource-constrained environments and for long-context tasks. In this work, we propose a training-free adaptive inference method for multi-modal LLMs that can accommodate a broad range of efficiency requirements with a minimum performance drop. Our method consists of a) iterative token merging based on embedding similarity before LLMs, and b) progressive token pruning within LLM layers based on multi-modal importance. With a minimalist design, our method can be applied to both video and image LLMs. Extensive experiments on diverse video and image benchmarks demonstrate that our method substantially reduces computation load (e.g., a $\textbf{7-fold}$ reduction in FLOPs) while preserving the performance of video and image LLMs. Further, at a similar computational cost, our method outperforms the state-of-the-art methods in long video understanding (e.g., $\textbf{+4.6}$ on MLVU). Additionally, our in-depth analysis provides insights into token redundancy and LLM layer behaviors, offering guidance for future research in designing efficient multi-modal LLMs. Our code is available at https://github.com/LaVi-Lab/AIM.

</details>

### ZipVL: Accelerating Vision-Language Models Through Dynamic Token Sparsity.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01904) · 📚 被引 0
- **作者**: Yefei He, Feng Chen, Jing Liu, Wenqi Shao, Hong Zhou, Kaipeng Zhang et al.
- **🏷️ 机构**: Zhejiang University,China, The University of Adelaide,Australia, Monash University,ZIP Lab,Australia
- **会议**: ICCV 2025

### SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02208) · 📚 被引 0
- **作者**: Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis et al.
- **🏷️ 机构**: NVIDIA, MIT, University of Toronto
- **会议**: ICCV 2025

### PLADIS: Pushing the Limits of Attention in Diffusion Models at Inference Time by Leveraging Sparsity.
- **链接**: [arXiv:2503.07677](https://arxiv.org/abs/2503.07677) · 📚 被引 0
- **作者**: Kwanyoung Kim, Byeongsu Sim
- **🏷️ 机构**: Samsung Research
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models have shown impressive results in generating high-quality conditional samples using guidance techniques such as Classifier-Free Guidance (CFG). However, existing methods often require additional training or neural function evaluations (NFEs), making them incompatible with guidance-distilled models. Also, they rely on heuristic approaches that need identifying target layers. In this work, we propose a novel and efficient method, termed PLADIS, which boosts pre-trained models (U-Net/Transformer) by leveraging sparse attention. Specifically, we extrapolate query-key correlations using softmax and its sparse counterpart in the cross-attention layer during inference, without requiring extra training or NFEs. By leveraging the noise robustness of sparse attention, our PLADIS unleashes the latent potential of text-to-image diffusion models, enabling them to excel in areas where they once struggled with newfound effectiveness. It integrates seamlessly with guidance techniques, including guidance-distilled models. Extensive experiments show notable improvements in text alignment and human preference, offering a highly efficient and universally applicable solution. See Our project page : https://cubeyoung.github.io/pladis-proejct/

</details>

### Sparsity Outperforms Low-Rank Projections in Few-Shot Adaptation.
- **链接**: [arXiv:2504.12436](https://arxiv.org/abs/2504.12436) · 📚 被引 0
- **作者**: Nairouz Mrabah, Nicolas Richet, Ismail Ben Ayed, Eric Granger
- **🏷️ 机构**: LIVIA, ETS Montreal,ILLS Department of Systems Engineering,Canada
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Adapting Vision-Language Models (VLMs) to new domains with few labeled samples remains a significant challenge due to severe overfitting and computational constraints. State-of-the-art solutions, such as low-rank reparameterization, mitigate these issues but often struggle with generalization and require extensive hyperparameter tuning. In this paper, a novel Sparse Optimization (SO) framework is proposed. Unlike low-rank approaches that typically constrain updates to a fixed subspace, our SO method leverages high sparsity to dynamically adjust very few parameters. We introduce two key paradigms. First, we advocate for \textit{local sparsity and global density}, which updates a minimal subset of parameters per iteration while maintaining overall model expressiveness. As a second paradigm, we advocate for \textit{local randomness and global importance}, which sparsifies the gradient using random selection while pruning the first moment based on importance. This combination significantly mitigates overfitting and ensures stable adaptation in low-data regimes. Extensive experiments on 11 diverse datasets show that SO achieves state-of-the-art few-shot adaptation performance while reducing memory overhead.

</details>

### SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs.
- **链接**: [arXiv:2506.05344](https://arxiv.org/abs/2506.05344) · [代码](https://github.com/CR400AF-A/SparseMM) · 📚 被引 0
- **作者**: Jiahui Wang, Zuyan Liu, Yongming Rao, Jiwen Lu
- **🏷️ 机构**: Tsinghua University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Multimodal Large Language Models (MLLMs) are commonly derived by extending pre-trained Large Language Models (LLMs) with visual capabilities. In this work, we investigate how MLLMs process visual inputs by analyzing their attention mechanisms. We reveal a surprising sparsity phenomenon: only a small subset (approximately less than 5%) of attention heads in LLMs actively contribute to visual understanding, termed visual heads. To identify these heads efficiently, we design a training-free framework that quantifies head-level visual relevance through targeted response analysis. Building on this discovery, we introduce SparseMM, a KV-Cache optimization strategy that allocates asymmetric computation budgets to heads in LLMs based on their visual scores, leveraging the sparity of visual heads for accelerating the inference of MLLMs. Compared with prior KV-Cache acceleration methods that ignore the particularity of visual, SparseMM prioritizes stress and retaining visual semantics during decoding. Extensive evaluations across mainstream multimodal benchmarks demonstrate that SparseMM achieves superior accuracy-efficiency trade-offs. Notably, SparseMM delivers 1.38x real-time acceleration and 52% memory reduction during generation while maintaining performance parity on efficiency test. Our project is open sourced at https://github.com/CR400AF-A/SparseMM.

</details>

## 跨领域论文（完整笔记在其他领域）

- Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning. → [3d-detection](../3d-detection/Guideline%202025.md)
