# Network Pruning — 2025 Guideline

> 领域: 网络剪枝 / 模型压缩（结构化剪枝、稀疏化）
> 论文数: 25 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### General Compression Framework for Efficient Transformer Object Tracking.
- **链接**: [arXiv:2409.17564](https://arxiv.org/abs/2409.17564) · [代码](https://github.com/LingyiHongfd/CompressTracker) · 📚 被引 3
- **作者**: Lingyi Hong, Jinglun Li, Xinyu Zhou, Shilin Yan, Pinxue Guo, Kaixun Jiang et al.
- **🏷️ 机构**: College of Computer Science and Artificial Intelligence, Fudan University,Shanghai Key Lab of Intelligent Information Processing,China, College of Intelligent Robotics and Advanced Manufacturing, Fudan University,China
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous works have attempted to improve tracking efficiency through lightweight architecture design or knowledge distillation from teacher models to compact student trackers. However, these solutions often sacrifice accuracy for speed to a great extent, and also have the problems of complex training process and structural limitations. Thus, we propose a general model compression framework for efficient transformer object tracking, named CompressTracker, to reduce model size while preserving tracking accuracy. Our approach features a novel stage division strategy that segments the transformer layers of the teacher model into distinct stages to break the limitation of model structure. Additionally, we also design a unique replacement training technique that randomly substitutes specific stages in the student model with those from the teacher model, as opposed to training the student model in isolation. Replacement training enhances the student model's ability to replicate the teacher model's behavior and simplifies the training process. To further forcing student model to emulate teacher model, we incorporate prediction guidance and stage-wise feature mimicking to provide additional supervision during the teacher model's compression process. CompressTracker is structurally agnostic, making it compatible with any transformer architecture. We conduct a series of experiment to verify the effectiveness and generalizability of our CompressTracker. Our CompressTracker-SUTrack, compressed from SUTrack, retains about 99 performance on LaSOT (72.2 AUC) while achieves 2.42x speed up. Code is available at https://github.com/LingyiHongfd/CompressTracker.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing AI-based point cloud compression methods struggle with dependence on specific training data distributions, which limits their real-world deployment. Implicit Neural Representation (INR) methods solve the above problem by encoding overfitted network parameters to the bitstream, resulting in more distribution-agnostic results. However, due to the limitation of encoding time and decoder size, current INR based methods only consider lossy geometry compression. In this paper, we propose the first INR based lossless point cloud geometry compression method called Lossless Implicit Neural Representations for Point Cloud Geometry Compression (LINR-PCGC). To accelerate encoding speed, we design a group of point clouds level coding framework with an effective network initialization strategy, which can reduce around 60% encoding time. A lightweight coding network based on multiscale SparseConv, consisting of scale context extraction, child node prediction, and model compression modules, is proposed to realize fast inference and compact decoder size. Experimental results show that our method consistently outperforms traditional and AI-based methods: for example, with the convergence time in the MVUB dataset, our method reduces the bitstream by approximately 21.21% compared to G-PCC TMC13v23 and 21.95% compared to SparsePCGC. Our project can be seen on https://huangwenjie2023.github.io/LINR-PCGC/.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Previous works have attempted to improve tracking efficiency through lightweight architecture design or knowledge distillation from teacher models to compact student trackers. However, these solutions often sacrifice accuracy for speed to a great extent, and also have the problems of complex training process and structural limitations. Thus, we propose a general model compression framework for efficient transformer object tracking, named CompressTracker, to reduce model size while preserving tracking accuracy. Our approach features a novel stage division strategy that segments the transformer layers of the teacher model into distinct stages to break the limitation of model structure. Additionally, we also design a unique replacement training technique that randomly substitutes specific stages in the student model with those from the teacher model, as opposed to training the student model in isolation. Replacement training enhances the student model's ability to replicate the teacher model's behavior and simplifies the training process. To further forcing student model to emulate teacher model, we incorporate prediction guidance and stage-wise feature mimicking to provide additional supervision during the teacher model's compression process. CompressTracker is structurally agnostic, making it compatible with any transformer architecture. We conduct a series of experiment to verify the effectiveness and generalizability of our CompressTracker. Our CompressTracker-SUTrack, compressed from SUTrack, retains about 99 performance on LaSOT (72.2 AUC) while achieves 2.42x speed up. Code is available at https://github.com/LingyiHongfd/CompressTracker.

</details>

### Cross-Granularity Online Optimization with Masked Compensated Information for Learned Image Compression.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01533) · 📚 被引 1
- **作者**: Haowei Kuang, Wenhan Yang, Zongming Guo, Jiaying Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology, Peking University,Beijing,China, Pengcheng Laboratory,Shenzhen,China
- **会议**: ICCV 2025

### LLaMaFlex: Many-in-one LLMs via Generalized Pruning and Weight Sharing.
- **链接**: [出版页](https://openreview.net/forum?id=AyC4uxx2HW)
- **作者**: Ruisi Cai, Saurav Muralidharan, Hongxu Yin, Zhangyang Wang, Jan Kautz, Pavlo Molchanov
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose MixA-Q, a mixed-precision activation quantization framework that leverages intra-layer activation sparsity (a concept widely explored in activation pruning methods) for efficient inference of quantized window-based vision transformers. For a given uniform-bit quantization configuration, MixA-Q separates the batched window computations within Swin blocks and assigns a lower bit width to the activations of less important windows, improving the trade-off between model performance and efficiency. We introduce a Two-Branch Swin Block that processes activations separately in high- and low-bit precision, enabling seamless integration of our method with most quantization-aware training (QAT) and post-training quantization (PTQ) methods, or with simple modifications. Our experimental evaluations over the COCO dataset demonstrate that MixA-Q achieves a training-free 1.35x computational speedup without accuracy loss in PTQ configuration. With QAT, MixA-Q achieves a lossless 1.25x speedup and a 1.53x speedup with only a 1% mAP drop by incorporating activation pruning. Notably, by reducing the quantization error in important regions, our sparsity-aware quantization adaptation improves the mAP of the quantized W4A4 model (with both weights and activations in 4-bit precision) by 0.7%, reducing quantization degradation by 24%.

</details>

> While large-scale text-to-image diffusion models have demonstrated impressive image-generation capabilities, there are significant concerns about their potential misuse for generating unsafe content, violating copyright, and perpetuating societal biases. Recently, the text-to-image generation community has begun addressing these concerns by editing or unlearning undesired concepts from pre-trained models. However, these methods often involve data-intensive and inefficient fine-tuning or utilize various forms of token remapping, rendering them susceptible to adversarial jailbreaks. In this paper, we present a simple and effective training-free approach, ConceptPrune, wherein we first identify critical regions within pre-trained models responsible for generating undesirable concepts, thereby facilitating straightforward concept unlearning via weight pruning. Experiments across a range of concepts including artistic styles, nudity, object erasure, and gender debiasing demonstrate that target concepts can be efficiently erased by pruning a tiny fraction, approximately 0.12% of total weights, enabling multi-concept erasure and robustness against various white-box and black-box adversarial attacks.

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce DC-AR, a novel masked autoregressive (AR) text-to-image generation framework that delivers superior image generation quality with exceptional computational efficiency. Due to the tokenizers' limitations, prior masked AR models have lagged behind diffusion models in terms of quality or efficiency. We overcome this limitation by introducing DC-HT - a deep compression hybrid tokenizer for AR models that achieves a 32x spatial compression ratio while maintaining high reconstruction fidelity and cross-resolution generalization ability. Building upon DC-HT, we extend MaskGIT and create a new hybrid masked autoregressive image generation framework that first produces the structural elements through discrete tokens and then applies refinements via residual tokens. DC-AR achieves state-of-the-art results with a gFID of 5.49 on MJHQ-30K and an overall score of 0.69 on GenEval, while offering 1.5-7.9x higher throughput and 2.0-3.5x lower latency compared to prior leading diffusion and autoregressive models.

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Increasingly expensive training of ever larger models such as Vision Transfomers motivate reusing the vast library of already trained state-of-the-art networks. However, their latency, high computational costs and memory demands pose significant challenges for deployment, especially on resource-constrained hardware. While structured pruning methods can reduce these factors, they often require costly retraining, sometimes for up to hundreds of epochs, or even training from scratch to recover the lost accuracy resulting from the structural modifications. Maintaining the provided performance of trained models after structured pruning and thereby avoiding extensive retraining remains a challenge. To solve this, we introduce Variance-Based Pruning, a simple and structured one-shot pruning technique for efficiently compressing networks, with minimal finetuning. Our approach first gathers activation statistics, which are used to select neurons for pruning. Simultaneously the mean activations are integrated back into the model to preserve a high degree of performance. On ImageNet-1k recognition tasks, we demonstrate that directly after pruning DeiT-Base retains over 70% of its original performance and requires only 10 epochs of fine-tuning to regain 99% of the original accuracy while simultaneously reducing MACs by 35% and model size by 36%, thus speeding up the model by 1.44x. The code is available at: https://github.com/boschresearch/variance-based-pruning

</details>

### LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding.
- **链接**: [出版页](https://proceedings.mlr.press/v267/shen25j.html)
- **作者**: Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Lemeng Wu, Jun Chen, Chenchen Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### Training-Free Dataset Pruning for Instance Segmentation.
- **链接**: [arXiv:2503.00828](https://arxiv.org/abs/2503.00828) · [代码](https://github.com/he-y/dataset-pruning-for-instance-segmentation)
- **作者**: Yalun Dai, Lingao Xiao, Ivor W. Tsang, Yang He
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual Autoregressive (VAR) modeling has gained popularity for its shift towards next-scale prediction. However, existing VAR paradigms process the entire token map at each scale step, leading to the complexity and runtime scaling dramatically with image resolution. To address this challenge, we propose FastVAR, a post-training acceleration method for efficient resolution scaling with VARs. Our key finding is that the majority of latency arises from the large-scale step where most tokens have already converged. Leveraging this observation, we develop the cached token pruning strategy that only forwards pivotal tokens for scale-specific modeling while using cached tokens from previous scale steps to restore the pruned slots. This significantly reduces the number of forwarded tokens and improves the efficiency at larger resolutions. Experiments show the proposed FastVAR can further speedup FlashAttention-accelerated VAR by 2.7$\times$ with negligible performance drop of <1%. We further extend FastVAR to zero-shot generation of higher resolution images. In particular, FastVAR can generate one 2K image with 15GB memory footprints in 1.5s on a single NVIDIA 3090 GPU. Code is available at https://github.com/csguoh/FastVAR.

</details>

### DARE the Extreme: Revisiting Delta-Parameter Pruning For Fine-Tuned Models.
- **链接**: [arXiv:2410.09344](https://arxiv.org/abs/2410.09344)
- **作者**: Wenlong Deng, Yize Zhao, Vala Vakilian, Minghui Chen, Xiaoxiao Li, Christos Thrampoulidis
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Diffusion models are renowned for their generative capabilities, yet their pretraining processes exhibit distinct phases of learning speed that have been entirely overlooked in prior post-training acceleration efforts in the community. In this study, we introduce a novel framework called MosaicDiff that aligns diffusion pretraining dynamics with post-training sampling acceleration via trajectory-aware structural pruning. Our approach leverages the observation that the middle, fast-learning stage of diffusion pretraining requires more conservative pruning to preserve critical model features, while the early and later, slow-learning stages benefit from a more aggressive pruning strategy. This adaptive pruning mechanism is the first to explicitly mirror the inherent learning speed variations of diffusion pretraining, thereby harmonizing the model's inner training dynamics with its accelerated sampling process. Extensive experiments on DiT and SDXL demonstrate that our method achieves significant speed-ups in sampling without compromising output quality, outperforming previous state-of-the-art methods by large margins, also providing a new viewpoint for more efficient and robust training-free diffusion acceleration.

</details>

### Libra-Merging: Importance-redundancy and Pruning-merging Trade-off for Acceleration Plug-in in Large Vision-Language Model.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Libra-Merging_Importance-redundancy_and_Pruning-merging_Trade-off_for_Acceleration_Plug-in_in_Large_CVPR_2025_paper.html)
- **作者**: Longrong Yang, Dong Shen, Chaoxiang Cai, Kaibing Chen, Fan Yang, Tingting Gao et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2025

### ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.html)
- **作者**: Xubing Ye, Yukang Gan, Yixiao Ge, Xiao-Ping Zhang, Yansong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

</details>

### Adaptive Pruning of Pretrained Transformer via Differential Inclusions.
- **链接**: [arXiv:2501.03289](https://arxiv.org/abs/2501.03289)
- **作者**: Yizhuo Ding, Ke Fan, Yikai Wang, Xinwei Sun, Yanwei Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision language models (VLMs) demonstrate strong capabilities in jointly processing visual and textual data. However, they often incur substantial computational overhead due to redundant visual information, particularly in long-form video scenarios. Existing approaches predominantly focus on either vision token pruning, which may overlook spatio-temporal dependencies, or keyframe selection, which identifies informative frames but discards others, thus disrupting contextual continuity. In this work, we propose KVTP (Keyframe-oriented Vision Token Pruning), a novel framework that overcomes the drawbacks of token pruning and keyframe selection. By adaptively assigning pruning rates based on frame relevance to the query, KVTP effectively retains essential contextual information while significantly reducing redundant computation. To thoroughly evaluate the long-form video understanding capacities of VLMs, we curated and reorganized subsets from VideoMME, EgoSchema, and NextQA into a unified benchmark named SparseKV-QA that highlights real-world scenarios with sparse but crucial events. Our experiments with VLMs of various scales show that KVTP can reduce token usage by 80% without compromising spatiotemporal and contextual consistency, significantly cutting computation while maintaining the performance. These results demonstrate our approach's effectiveness in efficient long-video processing, facilitating more scalable VLM deployment.

</details>

</details>

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision encoders serve as the cornerstone of multimodal understanding. Single-encoder architectures like CLIP exhibit inherent constraints in generalizing across diverse multimodal tasks, while recent multi-encoder fusion methods introduce prohibitive computational overhead to achieve superior performance using complementary visual representations from multiple vision encoders. To address this, we propose a progressive pruning framework, namely Multi-Encoder collaboraTivE tOken pRuning (METEOR), that eliminates redundant visual tokens across the encoding, fusion, and decoding stages for multi-encoder MLLMs. For multi-vision encoding, we discard redundant tokens within each encoder via a rank guided collaborative token assignment strategy. Subsequently, for multi-vision fusion, we combine the visual features from different encoders while reducing cross-encoder redundancy with cooperative pruning. Finally, we propose an adaptive token pruning method in the LLM decoding stage to further discard irrelevant tokens based on the text prompts with dynamically adjusting pruning ratios for specific task demands. To our best knowledge, this is the first successful attempt that achieves an efficient multi-encoder based vision language model with multi-stage pruning strategies. Extensive experiments on 11 benchmarks demonstrate the effectiveness of our proposed approach. Compared with EAGLE, a typical multi-encoder MLLMs, METEOR reduces 76% visual tokens with only 0.3% performance drop in average. The code is available at https://github.com/YuchenLiu98/METEOR.

</details>

> Text-to-image (T2I) diffusion models have demonstrated impressive image generation capabilities. Still, their computational intensity prohibits resource-constrained organizations from deploying T2I models after fine-tuning them on their internal target data. While pruning techniques offer a potential solution to reduce the computational burden of T2I models, static pruning methods use the same pruned model for all input prompts, overlooking the varying capacity requirements of different prompts. Dynamic pruning addresses this issue by utilizing a separate sub-network for each prompt, but it prevents batch parallelism on GPUs. To overcome these limitations, we introduce Adaptive Prompt-Tailored Pruning (APTP), a novel prompt-based pruning method designed for T2I diffusion models. Central to our approach is a prompt router model, which learns to determine the required capacity for an input text prompt and routes it to an architecture code, given a total desired compute budget for prompts. Each architecture code represents a specialized model tailored to the prompts assigned to it, and the number of codes is a hyperparameter. We train the prompt router and architecture codes using contrastive learning, ensuring that similar prompts are mapped to nearby codes. Further, we employ optimal transport to prevent the codes from collapsing into a single one. We demonstrate APTP's effectiveness by pruning Stable Diffusion (SD) V2.1 using CC3M and COCO as target datasets. APTP outperforms the single-model pruning baselines in terms of FID, CLIP, and CMMD scores. Our analysis of the clusters learned by APTP reveals they are semantically meaningful. We also show that APTP can automatically discover previously empirically found challenging prompts for SD, e.g. prompts for generating text images, assigning them to higher capacity codes.

</details>

- TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model. → [multimodal](../multimodal/Guideline%202025.md)
- DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models. → [multimodal](../multimodal/Guideline%202025.md)
- CASP: Compression of Large Multimodal Models Based on Attention Sparsity. → [multimodal](../multimodal/Guideline%202025.md)
- FlashSloth : Lightning Multimodal Large Language Models via Embedded Visual Compression. → [multimodal](../multimodal/Guideline%202025.md)
- Text-guided Sparse Voxel Pruning for Efficient 3D Visual Grounding. → [3d-detection](../3d-detection/Guideline%202025.md)
