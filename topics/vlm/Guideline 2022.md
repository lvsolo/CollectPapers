# VLM — 2022 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### PointCLIP: Point Cloud Understanding by CLIP. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2112.02413](https://arxiv.org/abs/2112.02413) · 📚 被引 421
- **作者**: Renrui Zhang, Ziyu Guo, Wei Zhang, Kunchang Li, Xupeng Miao, Bin Cui et al.
- **🏷️ 机构**: Shanghai AI Laboratory, Peking University,School of CS and Key Lab of HCST
- **会议**: CVPR 2022
- **摘要（中）**: 针对CLIP模型能否从2D泛化到3D点云识别的问题，本文提出PointCLIP，通过将点云投影为多视角深度图，无需渲染即可与CLIP编码的文本进行对齐，实现零样本和少样本3D识别。方法设计了视角间适配器（inter-view adapter）以提取全局特征并自适应融合少样本知识，仅微调轻量适配器即可大幅提升性能。实验表明，PointCLIP在零样本3D分类上取得有竞争力结果，且与经典3D监督网络互补，简单集成可提升基线性能。
- **摘要（英）**: This paper proposes PointCLIP to generalize CLIP to 3D point cloud recognition by projecting point clouds into multi-view depth maps and aligning with text embeddings. An inter-view adapter enables few-shot adaptation with lightweight fine-tuning. Experiments show competitive zero-shot performance and complementary gains when ensembled with supervised 3D networks.
- **核心贡献**: 首次将CLIP成功应用于3D点云理解，通过多视角深度投影实现零样本识别。
- **创新点**: 利用深度图投影和视角间适配器实现2D预训练模型到3D的知识迁移。
- **结果**: 在零样本和少样本3D分类上取得显著性能，并与监督网络互补。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, zero-shot and few-shot learning via Contrastive Vision-Language Pre-training (CLIP) have shown inspirational performance on 2D visual recognition, which learns to match images with their corresponding texts in open-vocabulary settings. However, it remains under explored that whether CLIP, pre-trained by large-scale image-text pairs in 2D, can be generalized to 3D recognition. In this paper, we identify such a setting is feasible by proposing PointCLIP, which conducts alignment between CLIP-encoded point cloud and 3D category texts. Specifically, we encode a point cloud by projecting it into multi-view depth maps without rendering, and aggregate the view-wise zero-shot prediction to achieve knowledge transfer from 2D to 3D. On top of that, we design an inter-view adapter to better extract the global feature and adaptively fuse the few-shot knowledge learned from 3D into CLIP pre-trained in 2D. By just fine-tuning the lightweight adapter in the few-shot settings, the performance of PointCLIP could be largely improved. In addition, we observe the complementary property between PointCLIP and classical 3D-supervised networks. By simple ensembling, PointCLIP boosts baseline's performance and even surpasses state-of-the-art models. Therefore, PointCLIP is a promising alternative for effective 3D point cloud understanding via CLIP under low resource cost and data regime. We conduct thorough experiments on widely-adopted ModelNet10, ModelNet40 and the challenging ScanObjectNN to demonstrate the effectiveness of PointCLIP. The code is released at https://github.com/ZrrSkywalker/PointCLIP.

</details>

### 3DJCG: A Unified Framework for Joint Dense Captioning and Visual Grounding on 3D Point Clouds. **⭐⭐⭐** (相关度: 60%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01597) · 📚 被引 94
- **作者**: Daigang Cai, Lichen Zhao, Jing Zhang, Lu Sheng, Dong Xu
- **🏷️ 机构**: College of Software, Beihang University,China, The University of Sydney,Australia
- **会议**: CVPR 2022
- **摘要（中）**: ①针对3D点云场景中密集描述与视觉定位任务分离、缺乏统一框架的问题。②提出了3DJCG，一个联合处理3D密集描述和视觉定位的统一框架，通过共享编码器和任务特定解码器实现多任务学习。③相比分别训练两个任务的现有方法，该框架利用任务间互补信息，提升整体性能。④在ScanRefer和ReferIt3D数据集上，密集描述和视觉定位任务均达到领先水平，具体数值未在摘要中给出。
- **摘要（英）**: This paper addresses the separation of dense captioning and visual grounding in 3D point clouds by proposing 3DJCG, a unified framework with shared encoders and task-specific decoders. It leverages complementary information between tasks, achieving state-of-the-art performance on ScanRefer and ReferIt3D datasets, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出首个联合3D密集描述与视觉定位的统一框架。
- **创新点**: 通过共享编码器实现任务间知识共享。
- **结果**: 在多个3D数据集上达到领先性能。

### Scaling Up Vision-Language Pretraining for Image Captioning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01745) · 📚 被引 167
- **作者**: Xiaowei Hu, Zhe Gan, Jianfeng Wang, Zhengyuan Yang, Zicheng Liu, Yumao Lu et al.
- **🏷️ 机构**: Microsoft
- **会议**: CVPR 2022

### Reinforced Structured State-Evolution for Vision-Language Navigation.
- **链接**: [arXiv:2204.09280](https://arxiv.org/abs/2204.09280) · 📚 被引 43
- **作者**: Jinyu Chen, Chen Gao, Erli Meng, Qiong Zhang, Si Liu
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, Xiaomi Inc,Xiaomi AI Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-and-language Navigation (VLN) task requires an embodied agent to navigate to a remote location following a natural language instruction. Previous methods usually adopt a sequence model (e.g., Transformer and LSTM) as the navigator. In such a paradigm, the sequence model predicts action at each step through a maintained navigation state, which is generally represented as a one-dimensional vector. However, the crucial navigation clues (i.e., object-level environment layout) for embodied navigation task is discarded since the maintained vector is essentially unstructured. In this paper, we propose a novel Structured state-Evolution (SEvol) model to effectively maintain the environment layout clues for VLN. Specifically, we utilise the graph-based feature to represent the navigation state instead of the vector-based state. Accordingly, we devise a Reinforced Layout clues Miner (RLM) to mine and detect the most crucial layout graph for long-term navigation via a customised reinforcement learning strategy. Moreover, the Structured Evolving Module (SEM) is proposed to maintain the structured graph-based state during navigation, where the state is gradually evolved to learn the object-level spatial-temporal relationship. The experiments on the R2R and R4R datasets show that the proposed SEvol model improves VLN models' performance by large margins, e.g., +3% absolute SPL accuracy for NvEM and +8% for EnvDrop on the R2R test set.

</details>

### ADAPT: Vision-Language Navigation with Modality-Aligned Action Prompts.
- **链接**: [arXiv:2205.15509](https://arxiv.org/abs/2205.15509) · 📚 被引 44
- **作者**: Bingqian Lin, Yi Zhu, Zicong Chen, Xiwen Liang, Jianzhuang Liu, Xiaodan Liang
- **🏷️ 机构**: Shcnzhcn Campus of Sun Yat-sen University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language Navigation (VLN) is a challenging task that requires an embodied agent to perform action-level modality alignment, i.e., make instruction-asked actions sequentially in complex visual environments. Most existing VLN agents learn the instruction-path data directly and cannot sufficiently explore action-level alignment knowledge inside the multi-modal inputs. In this paper, we propose modAlity-aligneD Action PrompTs (ADAPT), which provides the VLN agent with action prompts to enable the explicit learning of action-level modality alignment to pursue successful navigation. Specifically, an action prompt is defined as a modality-aligned pair of an image sub-prompt and a text sub-prompt, where the former is a single-view observation and the latter is a phrase like ''walk past the chair''. When starting navigation, the instruction-related action prompt set is retrieved from a pre-built action prompt base and passed through a prompt encoder to obtain the prompt feature. Then the prompt feature is concatenated with the original instruction feature and fed to a multi-layer transformer for action prediction. To collect high-quality action prompts into the prompt base, we use the Contrastive Language-Image Pretraining (CLIP) model which has powerful cross-modality alignment ability. A modality alignment loss and a sequential consistency loss are further introduced to enhance the alignment of the action prompt and enforce the agent to focus on the related prompt sequentially. Experimental results on both R2R and RxR show the superiority of ADAPT over state-of-the-art methods.

</details>

### Counterfactual Cycle-Consistent Learning for Instruction Following and Generation in Vision-Language Navigation.
- **链接**: [arXiv:2203.16586](https://arxiv.org/abs/2203.16586) · 📚 被引 53
- **作者**: Hanqing Wang, Wei Liang, Jianbing Shen, Luc Van Gool, Wenguan Wang
- **🏷️ 机构**: Beijing Institute of Technology, SKL-IOTSC, University of Macau, ETH Zurich
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Since the rise of vision-language navigation (VLN), great progress has been made in instruction following -- building a follower to navigate environments under the guidance of instructions. However, far less attention has been paid to the inverse task: instruction generation -- learning a speaker~to generate grounded descriptions for navigation routes. Existing VLN methods train a speaker independently and often treat it as a data augmentation tool to strengthen the follower while ignoring rich cross-task relations. Here we describe an approach that learns the two tasks simultaneously and exploits their intrinsic correlations to boost the training of each: the follower judges whether the speaker-created instruction explains the original navigation route correctly, and vice versa. Without the need of aligned instruction-path pairs, such cycle-consistent learning scheme is complementary to task-specific training targets defined on labeled data, and can also be applied over unlabeled paths (sampled without paired instructions). Another agent, called~creator is added to generate counterfactual environments. It greatly changes current scenes yet leaves novel items -- which are vital for the execution of original instructions -- unchanged. Thus more informative training scenes are synthesized and the three agents compose a powerful VLN learning system. Extensive experiments on a standard benchmark show that our approach improves the performance of various follower models and produces accurate navigation instructions.

</details>

### Predict, Prevent, and Evaluate: Disentangled Text-Driven Image Manipulation Empowered by Pre-Trained Vision-Language Model.
- **链接**: [arXiv:2111.13333](https://arxiv.org/abs/2111.13333) · 📚 被引 33
- **作者**: Zipeng Xu, Tianwei Lin, Hao Tang, Fu Li, Dongliang He, Nicu Sebe et al.
- **🏷️ 机构**: University of Trento,MHUG, VIS, Baidu Inc., CVL, ETH Z&#x00FC;rich
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To achieve disentangled image manipulation, previous works depend heavily on manual annotation. Meanwhile, the available manipulations are limited to a pre-defined set the models were trained for. We propose a novel framework, i.e., Predict, Prevent, and Evaluate (PPE), for disentangled text-driven image manipulation that requires little manual annotation while being applicable to a wide variety of manipulations. Our method approaches the targets by deeply exploiting the power of the large-scale pre-trained vision-language model CLIP. Concretely, we firstly Predict the possibly entangled attributes for a given text command. Then, based on the predicted attributes, we introduce an entanglement loss to Prevent entanglements during training. Finally, we propose a new evaluation metric to Evaluate the disentangled image manipulation. We verify the effectiveness of our method on the challenging face editing task. Extensive experiments show that the proposed PPE framework achieves much better quantitative and qualitative results than the up-to-date StyleCLIP baseline.

</details>

### Conditional Prompt Learning for Vision-Language Models.
- **链接**: [arXiv:2203.05557](https://arxiv.org/abs/2203.05557) · [代码](https://github.com/KaiyangZhou/CoOp) · 📚 被引 1678
- **作者**: Kaiyang Zhou, Jingkang Yang, Chen Change Loy, Ziwei Liu
- **🏷️ 机构**: Nanyang Technological University,S-Lab,Singapore
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> With the rise of powerful pre-trained vision-language models like CLIP, it becomes essential to investigate ways to adapt these models to downstream datasets. A recently proposed method named Context Optimization (CoOp) introduces the concept of prompt learning -- a recent trend in NLP -- to the vision domain for adapting pre-trained vision-language models. Specifically, CoOp turns context words in a prompt into a set of learnable vectors and, with only a few labeled images for learning, can achieve huge improvements over intensively-tuned manual prompts. In our study we identify a critical problem of CoOp: the learned context is not generalizable to wider unseen classes within the same dataset, suggesting that CoOp overfits base classes observed during training. To address the problem, we propose Conditional Context Optimization (CoCoOp), which extends CoOp by further learning a lightweight neural network to generate for each image an input-conditional token (vector). Compared to CoOp's static prompts, our dynamic prompts adapt to each instance and are thus less sensitive to class shift. Extensive experiments show that CoCoOp generalizes much better than CoOp to unseen classes, even showing promising transferability beyond a single dataset; and yields stronger domain generalization performance as well. Code is available at https://github.com/KaiyangZhou/CoOp.

</details>

> The 3D visual grounding task has been explored with visual and language streams comprehending referential language to identify target objects in 3D scenes. However, most existing methods devote the visual stream to capturing the 3D visual clues using off-the-shelf point clouds encoders. The main question we address in this paper is "can we consolidate the 3D visual stream by 2D clues synthesized from point clouds and efficiently utilize them in training and testing?". The main idea is to assist the 3D encoder by incorporating rich 2D object representations without requiring extra 2D inputs. To this end, we leverage 2D clues, synthetically generated from 3D point clouds, and empirically show their aptitude to boost the quality of the learned visual representations. We validate our approach through comprehensive experiments on Nr3D, Sr3D, and ScanRefer datasets and show consistent performance gains compared to existing methods. Our proposed module, dubbed as Look Around and Refer (LAR), significantly outperforms the state-of-the-art 3D visual grounding techniques on three benchmarks, i.e., Nr3D, Sr3D, and ScanRefer. The code is available at https://eslambakr.github.io/LAR.github.io/.

- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [object-detection](../object-detection/Guideline%202022.md)
- Multi-View Transformer for 3D Visual Grounding. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Expanding Large Pre-trained Unimodal Models with Multimodal Information Injection for Image-Text Multimodal Classification. → [multimodal](../multimodal/Guideline%202022.md)
- EI-CLIP: Entity-aware Interventional Contrastive Learning for E-commerce Cross-modal Retrieval. → [multimodal](../multimodal/Guideline%202022.md)
- Unified Contrastive Learning in Image-Text-Label Space. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)

## 🆕 增量新增

### Single-Stream Multi-level Alignment for Vision-Language Pretraining. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2203.14395](https://arxiv.org/abs/2203.14395)
- **作者**: Zaid Khan, B. G. Vijay Kumar, Xiang Yu, Samuel Schulter, Manmohan Chandraker, Yun Fu
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对现有视觉-语言预训练中，双流对比学习仅全局对齐、忽略细粒度对齐的问题。②提出单流架构，通过对称跨模态重建（XMM）和伪标签关键词预测（PSL）两个新任务，实现全局、patch-token和概念语义三个级别的对齐。③相比双流方法，单流架构支持更细粒度交互；相比监督方法，无需密集标注，利用动量编码器自动生成伪标签。④实验显示该方法在多个下游任务上优于现有对比学习方法，但摘要未给出具体数值。
- **摘要（英）**: This work tackles the lack of fine-grained alignment in contrastive vision-language pretraining by proposing a single-stream architecture with two novel tasks: symmetric cross-modality reconstruction (XMM) and pseudo-labeled keyword prediction (PSL). These tasks enable alignment at global, patch-token, and semantic levels without dense annotations. The method outperforms contrastive baselines on downstream tasks, though specific numbers are omitted.
- **核心贡献**: 提出单流多级对齐的视觉-语言预训练方法。
- **创新点**: 通过XMM和PSL任务实现无需标注的多级对齐。
- **结果**: 在多个下游任务上取得优于对比学习方法的性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Self-supervised vision-language pretraining from pure images and text with a contrastive loss is effective, but ignores fine-grained alignment due to a dual-stream architecture that aligns image and text representations only on a global level. Earlier, supervised, non-contrastive methods were capable of finer-grained alignment, but required dense annotations that were not scalable. We propose a single stream architecture that aligns images and language at multiple levels: global, fine-grained patch-token, and conceptual/semantic, using two novel tasks: symmetric cross-modality reconstruction (XMM) and a pseudo-labeled key word prediction (PSL). In XMM, we mask input tokens from one modality and use cross-modal information to reconstruct the masked token, thus improving fine-grained alignment between the two modalities. In PSL, we use attention to select keywords in a caption, use a momentum encoder to recommend other important keywords that are missing from the caption but represented in the image, and then train the visual encoder to predict the presence of those keywords, helping it learn semantic concepts that are essential for grounding a textual token to an image region. We demonstrate competitive performance and improved data efficiency on image-text retrieval, grounding, visual question answering/reasoning against larger models and models trained on more data. Code and models available at zaidkhan.me/SIMLA.

</details>

### A Dataset for Interactive Vision-Language Navigation with Unknown Command Feasibility. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20074-8_18) · 📚 被引 29
- **作者**: Andrea Burns, Deniz Arsan, Sanjna Agrawal, Ranjitha Kumar, Kate Saenko, Bryan A. Plummer
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对视觉-语言导航（VLN）中指令可能不可执行的问题，即现有数据集假设所有指令均可执行，但实际中命令可能因环境或物理限制而失败。②提出了一个包含未知命令可行性的交互式VLN数据集，并设计了相应的任务设置和评估协议，以模拟真实场景中的不确定性。③相比已有VLN数据集，该工作首次引入命令可行性判断，增强了模型的鲁棒性和实用性。④摘要未提供具体数据，但通过新数据集和任务设计，为后续研究提供了基准。
- **摘要（英）**: This paper addresses the issue of unknown command feasibility in vision-language navigation, where existing datasets assume all instructions are executable. It introduces a new interactive VLN dataset with feasibility annotations and task protocols to handle uncertain commands. The contribution lies in benchmarking realistic navigation scenarios, though no quantitative results are reported in the abstract.
- **核心贡献**: 提出了首个考虑命令可行性的交互式VLN数据集和评估协议。
- **创新点**: 将命令可行性判断融入VLN任务设计。
- **结果**: 提供了新基准，但未报告具体性能数据。

### Learning Disentanglement with Decoupled Labels for Vision-Language Navigation. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_18) · 📚 被引 8
- **作者**: Wenhao Cheng, Xingping Dong, Salman H. Khan, Jianbing Shen
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对视觉-语言导航中解耦表示学习不足的问题，即现有方法难以分离指令中的不同语义成分。②提出了一种利用解耦标签（如动作、目标、空间关系）来引导特征解耦的学习方法，增强导航决策的准确性。③相比已有工作，该方法显式利用标签信息进行解耦，提高了表示的可解释性和泛化能力。④摘要未提供具体数据，但预期在VLN基准上有所提升。
- **摘要（英）**: This paper tackles the insufficient disentanglement in vision-language navigation by introducing decoupled labels to guide feature separation. The method improves interpretability and generalization, though specific experimental results are not detailed in the abstract.
- **核心贡献**: 提出利用解耦标签增强VLN表示学习的方法。
- **创新点**: 将标签解耦引入导航任务。
- **结果**: 未报告具体效果。

### Generative Negative Text Replay for Continual Vision-Language Pretraining. **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2210.17322](https://arxiv.org/abs/2210.17322)
- **作者**: Shipeng Yan, Lanqing Hong, Hang Xu, Jianhua Han, Tinne Tuytelaars, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对视觉-语言预训练（VLP）在流式数据下遭遇灾难性遗忘的问题。②提出生成式负文本回放（GNTR）方法，利用记忆中的图像生成硬负样本文本，增强对比学习的负样本多样性；同时提出多模态知识蒸馏，对齐新旧模型的实例级预测。③相比传统回放，生成式负样本更有效保留旧知识，且蒸馏损失提升跨模态一致性。④在Conceptual Caption数据集上的实例和类增量分割上评估，结果显示优于现有持续学习方法，但摘要未给出具体数值。
- **摘要（英）**: This paper addresses catastrophic forgetting in continual vision-language pretraining by proposing generative negative text replay (GNTR), which synthesizes hard negative texts from memory images, and multi-modal knowledge distillation to align predictions. This improves negative sample diversity and preserves learned knowledge. Experiments on Conceptual Caption splits show superior performance over existing methods, though specific numbers are not provided.
- **核心贡献**: 提出生成式负文本回放和知识蒸馏的持续视觉-语言预训练方法。
- **创新点**: 利用生成硬负样本增强回放效果。
- **结果**: 在持续学习基准上优于现有方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language pre-training (VLP) has attracted increasing attention recently. With a large amount of image-text pairs, VLP models trained with contrastive loss have achieved impressive performance in various tasks, especially the zero-shot generalization on downstream datasets. In practical applications, however, massive data are usually collected in a streaming fashion, requiring VLP models to continuously integrate novel knowledge from incoming data and retain learned knowledge. In this work, we focus on learning a VLP model with sequential chunks of image-text pair data. To tackle the catastrophic forgetting issue in this multi-modal continual learning setting, we first introduce pseudo text replay that generates hard negative texts conditioned on the training images in memory, which not only better preserves learned knowledge but also improves the diversity of negative samples in the contrastive loss. Moreover, we propose multi-modal knowledge distillation between images and texts to align the instance-wise prediction between old and new models. We incrementally pre-train our model on both the instance and class incremental splits of the Conceptual Caption dataset, and evaluate the model on zero-shot image classification and image-text retrieval tasks. Our method consistently outperforms the existing baselines with a large margin, which demonstrates its superiority. Notably, we realize an average performance boost of $4.60\%$ on image-classification downstream datasets for the class incremental split.

</details>

### UniTAB: Unifying Text and Box Outputs for Grounded Vision-Language Modeling. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1007/978-3-031-20059-5_30)
- **作者**: Zhengyuan Yang, Zhe Gan, Jianfeng Wang, Xiaowei Hu, Faisal Ahmed, Zicheng Liu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①该论文针对接地视觉-语言建模中文本和框输出不统一的问题，即现有模型通常分别处理文本生成和物体定位。②提出了UniTAB框架，统一文本和框的输出空间，通过联合训练实现多任务学习。③相比已有工作，该方法简化了模型结构，提高了跨任务泛化能力。④摘要未提供具体数据，但预期在接地任务上达到先进水平。
- **摘要（英）**: This paper addresses the disconnection between text and box outputs in grounded vision-language modeling by proposing UniTAB, a unified framework that jointly generates text and bounding boxes. It simplifies architecture and enhances generalization, though quantitative results are not specified.
- **核心贡献**: 提出UniTAB统一文本和框输出。
- **创新点**: 联合输出空间设计。
- **结果**: 未报告具体数据。

### Learning Visual Representation from Modality-Shared Contrastive Language-Image Pre-training. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2207.12661](https://arxiv.org/abs/2207.12661)
- **作者**: Haoxuan You, Luowei Zhou, Bin Xiao, Noel Codella, Yu Cheng, Ruochen Xu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ECCV 2022
- **摘要（中）**: ①针对多模态对比预训练中通常为每个模态使用独立编码器、限制跨模态知识共享的问题。②提出MS-CLIP框架，系统研究视觉和语言Transformer在对比预训练中可共享参数的比例，并引入轻量级模态特定并行模块。③相比vanilla CLIP，通过共享大部分编码器参数并添加少量模态特定模块，在多种架构变体中取得更优性能。④在零样本ImageNet分类上相对提升高达13%，表明共享参数能增强跨模态对齐和泛化能力。
- **摘要（英）**: This paper addresses the limitation of separate encoders in multimodal contrastive pre-training by proposing MS-CLIP frameworks that systematically explore parameter sharing between vision and language transformers. It finds that a mostly unified encoder with light-weight modality-specific modules outperforms variants with more separated parameters, achieving up to 13% relative improvement over vanilla CLIP in zero-shot ImageNet classification.
- **核心贡献**: 系统探索了对比语言-图像预训练中跨模态参数共享的架构设计空间。
- **创新点**: 提出在共享Transformer编码器中加入轻量级模态特定并行模块的混合架构。
- **结果**: 零样本ImageNet分类相对提升高达13%。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large-scale multi-modal contrastive pre-training has demonstrated great utility to learn transferable features for a range of downstream tasks by mapping multiple modalities into a shared embedding space. Typically, this has employed separate encoders for each modality. However, recent work suggests that transformers can support learning across multiple modalities and allow knowledge sharing. Inspired by this, we investigate a variety of Modality-Shared Contrastive Language-Image Pre-training (MS-CLIP) frameworks. More specifically, we question how many parameters of a transformer model can be shared across modalities during contrastive pre-training, and rigorously examine architectural design choices that position the proportion of parameters shared along a spectrum. In studied conditions, we observe that a mostly unified encoder for vision and language signals outperforms all other variations that separate more parameters. Additionally, we find that light-weight modality-specific parallel modules further improve performance. Experimental results show that the proposed MS-CLIP approach outperforms vanilla CLIP by up to 13\% relative in zero-shot ImageNet classification (pre-trained on YFCC-100M), while simultaneously supporting a reduction of parameters. In addition, our approach outperforms vanilla CLIP by 1.6 points in linear probing on a collection of 24 downstream vision tasks. Furthermore, we discover that sharing parameters leads to semantic concepts from different modalities being encoded more closely in the embedding space, facilitating the transferring of common semantic structure (e.g., attention patterns) from language to vision. Code is available at \href{https://github.com/Hxyou/MSCLIP}{URL}.

</details>

### How Much Can CLIP Benefit Vision-and-Language Tasks? **⭐⭐⭐⭐** (相关度: 80%)
- **链接**: [arXiv:2107.06383](https://arxiv.org/abs/2107.06383)
- **作者**: Sheng Shen, Liunian Harold Li, Hao Tan, Mohit Bansal, Anna Rohrbach, Kai-Wei Chang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2022
- **摘要（中）**: ①针对视觉-语言任务中视觉编码器依赖人工标注数据、泛化能力有限的问题。②提出将CLIP作为视觉编码器集成到现有V&L模型中，包括任务特定微调和V&L预训练两种场景。③相比广泛使用的BottomUp-TopDown编码器，CLIP利用大规模图文对预训练，显著提升视觉表示质量。④在VQA、视觉蕴含和V&L导航任务上取得新的最先进结果，性能大幅提升。
- **摘要（英）**: This paper investigates the benefit of using CLIP as a visual encoder in vision-and-language models, addressing the limitation of manually-annotated visual encoders. It integrates CLIP into both task-specific fine-tuning and V&L pretraining scenarios, showing significant improvements over BottomUp-TopDown. The method achieves new state-of-the-art results on VQA, Visual Entailment, and V&L Navigation tasks.
- **核心贡献**: 系统评估了CLIP在V&L任务中的优势，并建立了新的性能基准。
- **创新点**: 将CLIP作为通用视觉编码器，替代传统基于区域的特征。
- **结果**: 在多个V&L任务上刷新最先进结果。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Most existing Vision-and-Language (V&L) models rely on pre-trained visual encoders, using a relatively small set of manually-annotated data (as compared to web-crawled data), to perceive the visual world. However, it has been observed that large-scale pretraining usually can result in better generalization performance, e.g., CLIP (Contrastive Language-Image Pre-training), trained on a massive amount of image-caption pairs, has shown a strong zero-shot capability on various vision tasks. To further study the advantage brought by CLIP, we propose to use CLIP as the visual encoder in various V&L models in two typical scenarios: 1) plugging CLIP into task-specific fine-tuning; 2) combining CLIP with V&L pre-training and transferring to downstream tasks. We show that CLIP significantly outperforms widely-used visual encoders trained with in-domain annotated data, such as BottomUp-TopDown. We achieve competitive or better results on diverse V&L tasks, while establishing new state-of-the-art results on Visual Question Answering, Visual Entailment, and V&L Navigation tasks. We release our code at https://github.com/clip-vil/CLIP-ViL.

</details>

### Look Around and Refer: 2D Synthetic Semantics Knowledge Distillation for 3D Visual Grounding. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2211.14241](https://arxiv.org/abs/2211.14241)
- **作者**: Eslam Mohamed Bakr, Yasmeen Alsaedy, Mohamed Elhoseiny
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2022
- **摘要（中）**: ①该论文针对3D视觉定位任务中视觉流仅依赖点云编码器、缺乏丰富2D语义线索的问题，提出利用从点云合成的2D线索来增强3D视觉表示。②方法上，提出了Look Around and Refer (LAR)模块，通过知识蒸馏将2D合成语义知识融入3D编码器，无需额外2D输入，在训练和测试阶段均能高效利用。③相比现有方法，LAR在不增加推理负担的前提下，通过2D线索辅助3D编码器，提升了视觉表示质量。④在Nr3D、Sr3D和ScanRefer三个基准上，LAR显著优于现有最先进方法，取得了持续的性能提升。
- **摘要（英）**: This paper addresses the limitation of 3D visual grounding methods that rely solely on point cloud encoders, proposing to synthesize 2D clues from 3D point clouds to enrich visual representations. The proposed Look Around and Refer (LAR) module employs knowledge distillation to integrate 2D semantic knowledge into the 3D encoder without extra 2D inputs, consistently outperforming state-of-the-art methods on Nr3D, Sr3D, and ScanRefer benchmarks.
- **核心贡献**: 提出LAR模块，通过2D合成语义知识蒸馏增强3D视觉定位的视觉表示。
- **创新点**: 利用从点云合成的2D线索进行知识蒸馏，无需额外2D输入即可提升3D编码器性能。
- **结果**: 在Nr3D、Sr3D和ScanRefer上显著超越现有最先进方法。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The 3D visual grounding task has been explored with visual and language streams comprehending referential language to identify target objects in 3D scenes. However, most existing methods devote the visual stream to capturing the 3D visual clues using off-the-shelf point clouds encoders. The main question we address in this paper is "can we consolidate the 3D visual stream by 2D clues synthesized from point clouds and efficiently utilize them in training and testing?". The main idea is to assist the 3D encoder by incorporating rich 2D object representations without requiring extra 2D inputs. To this end, we leverage 2D clues, synthetically generated from 3D point clouds, and empirically show their aptitude to boost the quality of the learned visual representations. We validate our approach through comprehensive experiments on Nr3D, Sr3D, and ScanRefer datasets and show consistent performance gains compared to existing methods. Our proposed module, dubbed as Look Around and Refer (LAR), significantly outperforms the state-of-the-art 3D visual grounding techniques on three benchmarks, i.e., Nr3D, Sr3D, and ScanRefer. The code is available at https://eslambakr.github.io/LAR.github.io/.

</details>

## 跨领域论文（完整笔记在其他领域）

- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Robust Cross-Modal Representation Learning with Progressive Self-Distillation. → [multimodal](../multimodal/Guideline%202022.md)
- MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection. → [object-detection](../object-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- A Simple Baseline for Open-Vocabulary Semantic Segmentation with Pre-trained Vision-Language Model. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Switch-BERT: Learning to Model Multimodal Interactions by Switching Attention and Input. → [multimodal](../multimodal/Guideline%202022.md)
- MUGEN: A Playground for Video-Audio-Text Multimodal Understanding and GENeration. → [multimodal](../multimodal/Guideline%202022.md)
- Hierarchically Self-supervised Transformer for Human Skeleton Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Motion Sensitive Contrastive Learning for Self-supervised Video Representation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- CODER: Coupled Diversity-Sensitive Momentum Contrastive Learning for Image-Text Retrieval. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Learning Multimodal VAEs through Mutual Supervision. → [multimodal](../multimodal/Guideline%202022.md)
- Poisoning and Backdooring Contrastive Learning. → [multimodal](../multimodal/Guideline%202022.md)
- Bridging the Gap between Object and Image-level Representations for Open-Vocabulary Detection. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Patching open-vocabulary models by interpolating weights. → [open-set-detection](../open-set-detection/Guideline%202022.md)

<!-- COMPLETE v1 papers=16 -->
