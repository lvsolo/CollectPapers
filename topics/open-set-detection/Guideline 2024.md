# Open-set Detection — 2024 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 46 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### VideoGrounding-DINO: Towards Open-Vocabulary Spatio- Temporal Video Grounding. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01789) · 📚 被引 18
- **作者**: Syed Talal Wasim, Muzammal Naseer, Salman H. Khan, Ming-Hsuan Yang, Fahad Shahbaz Khan
- **🏷️ 机构**: Mohamed bin Zayed University of AI, University of California,Merced
- **会议**: CVPR 2024
- **摘要（中）**: ①针对开放词汇的时空视频定位问题，即给定文本查询，在视频中同时定位目标对象的时间和空间位置。②提出了VideoGrounding-DINO框架，结合DINO和视频 grounding 技术，利用时空解码器联合预测时间区间和空间框。③改进点在于将开放词汇能力扩展到视频领域，利用预训练视觉-语言模型对齐文本和视频特征。④摘要未提供具体数据，但预期在视频 grounding 基准上提升性能。
- **摘要（英）**: This paper addresses open-vocabulary spatio-temporal video grounding, proposing VideoGrounding-DINO to jointly localize objects in time and space via a spatio-temporal decoder. It extends open-vocabulary detection to video by leveraging vision-language models. The abstract lacks quantitative results, but the approach aims to improve video grounding benchmarks.
- **核心贡献**: 提出首个开放词汇时空视频定位框架VideoGrounding-DINO。
- **创新点**: 将开放词汇检测扩展到视频时空定位，结合DINO架构。
- **结果**: 未提供具体数据，预期提升视频定位性能。

### Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2402.12259](https://arxiv.org/abs/2402.12259) · 📚 被引 50
- **作者**: Sebastian Koch, Narunas Vaskevicius, Mirco Colosi, Pedro Hermosilla, Timo Ropinski
- **🏷️ 机构**: Bosch Center for Artificial Intelligence, Robert Bosch Corporate Research, TU Vienna
- **会议**: CVPR 2024
- **摘要（中）**: 针对3D场景图预测依赖固定标签集训练的问题，该论文提出Open3DSG，一种无需标注场景图数据的开放世界3D场景图预测方法。方法将3D场景图预测骨干网络的特征与2D视觉语言基础模型的特征空间对齐，实现零样本预测开放词汇对象类别，并利用接地LLM预测开放集关系。相比现有方法，Open3DSG首次支持开放词汇对象和开放集关系预测。实验表明在预测任意对象类别和复杂关系上有效。
- **摘要（英）**: This paper presents Open3DSG, an open-world 3D scene graph prediction method that eliminates the need for labeled scene graph data. It co-embeds 3D backbone features with 2D vision-language foundation models for zero-shot open-vocabulary object querying and uses a grounded LLM for open-set relationship prediction. As the first method to predict both open-vocabulary objects and open-set relationships, it demonstrates effectiveness on arbitrary categories and complex inter-object relations.
- **核心贡献**: 首次实现3D点云中开放词汇对象和开放集关系的零样本场景图预测。
- **创新点**: 利用2D视觉语言模型和接地LLM实现3D场景图的开放世界预测。
- **结果**: 在预测任意对象类别和复杂关系上表现有效。

### Open3DIS: Open-Vocabulary 3D Instance Segmentation with 2D Mask Guidance. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2312.10671](https://arxiv.org/abs/2312.10671) · 📚 被引 72
- **作者**: Phuc D. A. Nguyen, Tuan Duc Ngo, Evangelos Kalogerakis, Chuang Gan, Anh Tuan Tran, Cuong Pham et al.
- **🏷️ 机构**: VinAI Research, UMass Amherst, MIT-IBM Watson AI Lab
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇3D实例分割中小尺度与几何模糊对象难以识别的问题，该论文提出Open3DIS方法。方法通过新模块聚合跨帧2D实例掩码并映射到几何一致的点云区域，生成高质量对象提议，再与3D类无关提议结合。相比现有方法，显著提升了对多样类别对象的分割性能。在ScanNet200、S3DIS和Replica三个数据集上验证了有效性。
- **摘要（英）**: This paper introduces Open3DIS to address the challenge of identifying small-scale and geometrically ambiguous objects in open-vocabulary 3D instance segmentation. It aggregates 2D instance masks across frames and maps them to coherent point cloud regions as high-quality proposals, combined with 3D class-agnostic proposals. Experiments on ScanNet200, S3DIS, and Replica show significant performance gains across diverse categories.
- **核心贡献**: 提出2D掩码引导的3D开放词汇实例分割方法，提升小物体识别能力。
- **创新点**: 跨帧2D掩码聚合与点云映射生成高质量提议。
- **结果**: 在三个数据集上显著提升分割性能。

### Open-Vocabulary 3D Semantic Segmentation with Foundation Models. **⭐⭐⭐** (相关度: 65%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02011) · 📚 被引 28
- **作者**: Li Jiang, Shaoshuai Shi, Bernt Schiele
- **🏷️ 机构**: Max Planck Institute for Informatics, Saarland Informatics Campus
- **会议**: CVPR 2024
- **摘要（中）**: 针对开放词汇3D语义分割依赖标注数据的问题，该论文探索利用基础模型进行开放词汇3D语义分割。方法可能通过将3D特征与视觉语言模型对齐，实现零样本分割。相比传统监督方法，减少了对标注的依赖。但摘要缺失，具体方法和效果不明确。
- **摘要（英）**: This paper explores open-vocabulary 3D semantic segmentation using foundation models, likely by aligning 3D features with vision-language models for zero-shot segmentation. It reduces reliance on labeled data compared to supervised methods, but the abstract is missing, leaving details unclear.
- **核心贡献**: 探索基础模型在开放词汇3D语义分割中的应用。
- **创新点**: 利用视觉语言模型实现3D零样本分割。
- **结果**: 效果未明确。

### Open Vocabulary Semantic Scene Sketch Understanding. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2312.12463](https://arxiv.org/abs/2312.12463) · 📚 被引 7
- **作者**: Ahmed Bourouis, Judith Ellen Fan, Yulia Gryaditskaya
- **🏷️ 机构**: Surrey Institute for People-Centered AI and CVSSP, University of Surrey,UK, Stanford University,Department of Psychology,USA
- **会议**: CVPR 2024
- **摘要（中）**: 本文研究抽象手绘场景草图的机器理解问题，提出了一种基于CLIP预训练视觉Transformer的草图编码器，通过视觉提示调优和引入v-v自注意力块，实现语义感知的特征空间。模型采用两级层次设计，第一级编码整体场景，第二级聚焦单个类别，并引入文本-视觉交叉注意力。在语义草图分割任务上，该方法优于零样本CLIP基线，展示了无需像素级标注的泛化能力。
- **摘要（英）**: This paper tackles semantic understanding of abstract freehand scene sketches by proposing a CLIP-based vision transformer encoder with visual prompt tuning and v-v self-attention blocks. A two-level hierarchy enables holistic and category-specific encoding with cross-attention, achieving superior performance over zero-shot CLIP on semantic sketch segmentation without pixel-level annotations.
- **核心贡献**: 提出了一种无需像素标注的开放词汇草图语义分割方法。
- **创新点**: 在CLIP视觉编码器中引入v-v自注意力块和两级层次结构，实现语义解耦。
- **结果**: 在语义草图分割任务上优于零样本CLIP基线。

### CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning. **⭐⭐** (相关度: 50%)
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02632) · 📚 被引 26
- **作者**: Lianggangxu Chen, Xuejiao Wang, Jiale Lu, Shaohui Lin, Changbo Wang, Gaoqi He
- **🏷️ 机构**: School of Computer Science and Technology, East China Normal University,Shanghai,China
- **会议**: CVPR 2024
- **摘要（中）**: 该论文摘要为空，无法获取具体内容。根据标题推测，其研究开放词汇3D场景图生成，利用跨模态对比学习驱动CLIP，但缺乏详细信息，难以评估其方法和效果。
- **摘要（英）**: The abstract is empty, so no specific details are available. Based on the title, it likely addresses open-vocabulary 3D scene graph generation via cross-modality contrastive learning with CLIP, but the lack of content prevents a thorough assessment.
- **核心贡献**: 未知，因摘要缺失。
- **创新点**: 未知，因摘要缺失。
- **结果**: 未知，因摘要缺失。

### Open-vocabulary object 6D pose estimation. **⭐⭐⭐⭐** (相关度: 70%)
- **链接**: [arXiv:2312.00690](https://arxiv.org/abs/2312.00690) · 📚 被引 20
- **作者**: Jaime Corsetti, Davide Boscaini, Changjae Oh, Andrea Cavallaro, Fabio Poiesi
- **🏷️ 机构**: Fondazione, Queen Mary University, Idiap Research Institute
- **会议**: CVPR 2024
- **摘要（中）**: 本文提出开放词汇物体6D姿态估计的新设置，其中物体仅通过文本提示指定，无需CAD模型或视频序列。方法利用视觉语言模型分割目标物体并估计相对6D姿态，通过融合提示的物体级信息与局部图像特征，实现对新概念的泛化。在REAL275和Toyota-Light数据集上，该方法优于手工方法和深度学习基线，展示了在跨场景中的有效性。
- **摘要（英）**: This paper introduces open-vocabulary object 6D pose estimation, where objects are specified by text prompts without CAD models. A VLM-based approach segments and estimates relative pose by fusing object-level prompt information with local features, outperforming baselines on REAL275 and Toyota-Light datasets.
- **核心贡献**: 首次定义开放词汇6D姿态估计任务，并提出基于VLM的解决方案。
- **创新点**: 利用文本提示融合物体级信息与局部特征，实现无需模型的新类别泛化。
- **结果**: 在34个物体实例上优于手工和深度学习方法。

### AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents. **⭐⭐⭐** (相关度: 40%)
- **链接**: [arXiv:2403.12835](https://arxiv.org/abs/2403.12835) · 📚 被引 21
- **作者**: Jieming Cui, Tengyu Liu, Nian Liu, Yaodong Yang, Yixin Zhu, Siyuan Huang
- **🏷️ 机构**: Institute for Artificial Intelligence, Peking University, BIGAI,National Key Laboratory of General Artificial Intelligence
- **会议**: CVPR 2024
- **摘要（中）**: 针对物理仿真中运动生成难以适应新场景的问题，本文提出AnySkill，一种分层方法，通过低层控制器学习原子动作，高层策略根据开放词汇指令选择并组合动作，以最大化渲染图像与文本的CLIP相似度。该方法使用基于图像的奖励，无需手动设计奖励函数，能够生成响应未见指令的逼真运动序列，是首个实现开放词汇物理技能学习的交互式智能体方法。
- **摘要（英）**: AnySkill addresses adaptability in physics-based motion generation by using a hierarchical method with a low-level controller for atomic actions and a high-level policy that selects actions to maximize CLIP similarity between rendered images and text. It uses image-based rewards, enabling learning without manual reward engineering, and generates realistic motions for unseen instructions.
- **核心贡献**: 提出首个开放词汇物理技能学习方法，支持交互式智能体。
- **创新点**: 利用CLIP图像-文本相似度作为高层策略奖励，免去手动奖励设计。
- **结果**: 在未见指令上生成逼真运动序列，验证了方法的泛化能力。

### Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2311.17938](https://arxiv.org/abs/2311.17938) · 📚 被引 7
- **作者**: Lei Fan, Jianxiong Zhou, Xiaoying Xing, Ying Wu
- **🏷️ 机构**: Northwestern University
- **会议**: CVPR 2024
- **摘要（中）**: ①针对主动开放词汇识别中CLIP模型受视角和遮挡影响导致性能下降，以及序列观测特征融合缺乏有效方法的问题。②提出了一种新的智能体，利用帧间信息进行主动感知和分类，并设计了特征融合策略以保持开放词汇分类的判别力。③相比直接使用CLIP，该方法通过主动移动缓解视角和遮挡问题，并改进了序列特征集成。④实验表明该方法在主动识别任务上显著优于现有基线，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the challenges of active open-vocabulary recognition, where CLIP's performance degrades under viewpoint changes and occlusions, and sequential feature integration is inefficient. It proposes a novel agent that leverages inter-frame information for active perception and classification, with a feature fusion strategy to maintain discriminative power. The method outperforms existing baselines in active recognition tasks, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出了一个主动开放词汇识别框架，通过智能移动和帧间特征融合缓解CLIP的视角和遮挡限制。
- **创新点**: 创新性地利用主动移动策略和跨帧特征集成来增强开放词汇分类的鲁棒性。
- **结果**: 在主动识别任务上取得了优于现有方法的性能。

### From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2404.00906](https://arxiv.org/abs/2404.00906) · 📚 被引 51
- **作者**: Rongjie Li, Songyang Zhang, Dahua Lin, Kai Chen, Xuming He
- **🏷️ 机构**: School of Information Science and Technology, ShanghaiTech University, Shanghai AI Laboratory
- **会议**: CVPR 2024
- **摘要（中）**: ①针对场景图生成（SGG）中现有方法难以处理新颖视觉关系概念的问题。②提出了一个基于序列生成的开放词汇SGG框架，利用视觉-语言预训练模型（VLM）通过图像到文本生成范式，将场景图序列生成后构建图结构。③相比传统方法，该框架直接利用VLM的强能力，并集成显式关系建模以增强视觉-语言任务。④实验表明该方法在开放词汇SGG上取得了优越性能，并提升了下游视觉-语言任务的表现。
- **摘要（英）**: This paper addresses the challenge of generating scene graphs with novel visual relations in open-vocabulary settings. It proposes a sequence-generation-based framework that leverages VLMs for image-to-text generation, then constructs scene graphs from the sequences. The method achieves superior performance in open-vocabulary SGG and enhances downstream vision-language tasks through explicit relation modeling.
- **核心贡献**: 提出了一个基于VLM的开放词汇场景图生成框架，通过图像到文本生成实现图构建。
- **创新点**: 创新性地采用序列生成范式，将SGG任务与VLM结合，并集成关系建模。
- **结果**: 在开放词汇SGG和下游任务上取得了显著性能提升。

### OMG: Towards Open-vocabulary Motion Generation via Mixture of Controllers. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2312.08985](https://arxiv.org/abs/2312.08985) · 📚 被引 29
- **作者**: Han Liang, Jiacheng Bao, Ruichi Zhang, Sihan Ren, Yuecheng Xu, Sibei Yang et al.
- **🏷️ 机构**: ShanghaiTecn University, Tencent PCG
- **会议**: CVPR 2024
- **摘要（中）**: ①针对文本到运动生成中现有方法对未见文本输入失败或产生不合理运动的问题。②提出了OMG框架，采用预训练-微调范式，预训练阶段使用大规模无条件扩散模型（1B参数，20M运动实例）学习运动特征，微调阶段引入运动ControlNet和Mixture-of-Controllers（MoC）块，通过交叉注意力机制和文本特定专家处理子运动。③相比现有方法，OMG通过大规模预训练和MoC设计增强了零样本开放词汇运动生成能力。④实验表明该方法在零样本文本到运动生成上取得了显著效果，具体数据未在摘要中给出。
- **摘要（英）**: This paper addresses the failure of text-to-motion generation on unseen text inputs. It proposes OMG, a framework using a pretrain-finetune paradigm with a 1B-parameter unconditional diffusion model and motion ControlNet with Mixture-of-Controllers blocks. The method improves zero-shot open-vocabulary motion generation, though specific metrics are not detailed in the abstract.
- **核心贡献**: 提出了OMG框架，通过大规模预训练和MoC块实现零样本开放词汇运动生成。
- **创新点**: 创新性地将预训练-微调范式应用于运动生成，并引入MoC块以适配文本特定子运动。
- **结果**: 在零样本文本到运动生成任务上取得了优于现有方法的性能。

### Open-Vocabulary Segmentation with Semantic-Assisted Calibration.
- **链接**: [arXiv:2312.04089](https://arxiv.org/abs/2312.04089)
- **作者**: Yong Liu, Sule Bai, Guanbin Li, Yitong Wang, Yansong Tang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > This paper studies open-vocabulary segmentation (OVS) through calibrating in-vocabulary and domain-biased embedding space with generalized contextual prior of CLIP. As the core of open-vocabulary understanding, alignment of visual content with the semantics of unbounded text has become the bottleneck of this field. To address this challenge, recent works propose to utilize CLIP as an additional classifier and aggregate model predictions with CLIP classification results. Despite their remarkable progress, performance of OVS methods in relevant scenarios is still unsatisfactory compared with supervised counterparts. We attribute this to the in-vocabulary embedding and domain-biased CLIP prediction. To this end, we present a Semantic-assisted CAlibration Network (SCAN). In SCAN, we incorporate generalized semantic prior of CLIP into proposal embedding to avoid collapsing on known categories. Besides, a contextual shift strategy is applied to mitigate the lack of global context and unnatural background noise. With above designs, SCAN achieves state-of-the-art performance on all popular open-vocabulary segmentation benchmarks. Furthermore, we also focus on the problem of existing evaluation system that ignores semantic duplication across categories, and propose a new metric called Semantic-Guided IoU (SG-IoU).

### Emergent Open-Vocabulary Semantic Segmentation from Off-the-Shelf Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00386) · 📚 被引 16
- **作者**: Jiayun Luo, Siddhesh Khandelwal, Leonid Sigal, Boyang Li
- **🏷️ 机构**: Nanyang Technological University,Singapore, University of British Columbia, Vector Institute for AI,Canada
- **会议**: CVPR 2024

### Open-Vocabulary Attention Maps with Token Optimization for Semantic Segmentation in Diffusion Models.
- **链接**: [arXiv:2403.14291](https://arxiv.org/abs/2403.14291) · 📚 被引 16
- **作者**: Pablo Marcos-Manchón, Roberto Alcover-Couso, Juan C. SanMiguel, Jose M. Martínez
- **🏷️ 机构**: VPULab, University of Madrid,Spain
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Diffusion models represent a new paradigm in text-to-image generation. Beyond generating high-quality images from text prompts, models such as Stable Diffusion have been successfully extended to the joint generation of semantic segmentation pseudo-masks. However, current extensions primarily rely on extracting attentions linked to prompt words used for image synthesis. This approach limits the generation of segmentation masks derived from word tokens not contained in the text prompt. In this work, we introduce Open-Vocabulary Attention Maps (OVAM)-a training-free method for text-to-image diffusion models that enables the generation of attention maps for any word. In addition, we propose a lightweight optimization process based on OVAM for finding tokens that generate accurate attention maps for an object class with a single annotation. We evaluate these tokens within existing state-of-the-art Stable Diffusion extensions. The best-performing model improves its mIoU from 52.1 to 86.6 for the synthetic images' pseudo-masks, demonstrating that our optimized tokens are an efficient way to improve the performance of existing methods without architectural changes or retraining.

### Open-Vocabulary Semantic Segmentation with Image Embedding Balancing.
- **链接**: [arXiv:2406.09829](https://arxiv.org/abs/2406.09829) · 📚 被引 26
- **作者**: Xiangheng Shan, Dongyue Wu, Guilin Zhu, Yuanjie Shao, Nong Sang, Changxin Gao
- **🏷️ 机构**: National Key Laboratory of Multispectral Information Intelligent Processing Technology, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation is a challenging task, which requires the model to output semantic masks of an image beyond a close-set vocabulary. Although many efforts have been made to utilize powerful CLIP models to accomplish this task, they are still easily overfitting to training classes due to the natural gaps in semantic information between training and new classes. To overcome this challenge, we propose a novel framework for openvocabulary semantic segmentation called EBSeg, incorporating an Adaptively Balanced Decoder (AdaB Decoder) and a Semantic Structure Consistency loss (SSC Loss). The AdaB Decoder is designed to generate different image embeddings for both training and new classes. Subsequently, these two types of embeddings are adaptively balanced to fully exploit their ability to recognize training classes and generalization ability for new classes. To learn a consistent semantic structure from CLIP, the SSC Loss aligns the inter-classes affinity in the image feature space with that in the text feature space of CLIP, thereby improving the generalization ability of our model. Furthermore, we employ a frozen SAM image encoder to complement the spatial information that CLIP features lack due to the low training image resolution and image-level supervision inherent in CLIP. Extensive experiments conducted across various benchmarks demonstrate that the proposed EBSeg outperforms the state-of-the-art methods. Our code and trained models will be here: https://github.com/slonetime/EBSeg.

### USE: Universal Segment Embeddings for Open-Vocabulary Image Segmentation.
- **链接**: [arXiv:2406.05271](https://arxiv.org/abs/2406.05271) · 📚 被引 20
- **作者**: Xiaoqi Wang, Wenbin He, Xiwei Xuan, Clint Sebastian, Jorge Piazentin Ono, Xin Li et al.
- **🏷️ 机构**: Bosch Research North America, Bosch Center for Artificial Intelligence (BCAI)
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The open-vocabulary image segmentation task involves partitioning images into semantically meaningful segments and classifying them with flexible text-defined categories. The recent vision-based foundation models such as the Segment Anything Model (SAM) have shown superior performance in generating class-agnostic image segments. The main challenge in open-vocabulary image segmentation now lies in accurately classifying these segments into text-defined categories. In this paper, we introduce the Universal Segment Embedding (USE) framework to address this challenge. This framework is comprised of two key components: 1) a data pipeline designed to efficiently curate a large amount of segment-text pairs at various granularities, and 2) a universal segment embedding model that enables precise segment classification into a vast range of text-defined categories. The USE model can not only help open-vocabulary image segmentation but also facilitate other downstream tasks (e.g., querying and ranking). Through comprehensive experimental studies on semantic segmentation and part segmentation benchmarks, we demonstrate that the USE framework outperforms state-of-the-art open-vocabulary segmentation methods.

### OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual Representation.
- **链接**: [arXiv:2404.01409](https://arxiv.org/abs/2404.01409) · 📚 被引 10
- **作者**: Xiongwei Wu, Sicheng Yu, Ee-Peng Lim, Chong-Wah Ngo
- **🏷️ 机构**: Singapore Management University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > In the realm of food computing, segmenting ingredients from images poses substantial challenges due to the large intra-class variance among the same ingredients, the emergence of new ingredients, and the high annotation costs associated with large food segmentation datasets. Existing approaches primarily utilize a closed-vocabulary and static text embeddings setting. These methods often fall short in effectively handling the ingredients, particularly new and diverse ones. In response to these limitations, we introduce OVFoodSeg, a framework that adopts an open-vocabulary setting and enhances text embeddings with visual context. By integrating vision-language models (VLMs), our approach enriches text embedding with image-specific information through two innovative modules, eg, an image-to-text learner FoodLearner and an Image-Informed Text Encoder. The training process of OVFoodSeg is divided into two stages: the pre-training of FoodLearner and the subsequent learning phase for segmentation. The pre-training phase equips FoodLearner with the capability to align visual information with corresponding textual representations that are specifically related to food, while the second phase adapts both the FoodLearner and the Image-Informed Text Encoder for the segmentation task. By addressing the deficiencies of previous models, OVFoodSeg demonstrates a significant improvement, achieving an 4.9\% increase in mean Intersection over Union (mIoU) on the FoodSeg103 dataset, setting a new milestone for food image segmentation.

### Open-Vocabulary Video Anomaly Detection.
- **链接**: [arXiv:2311.07042](https://arxiv.org/abs/2311.07042)
- **作者**: Peng Wu, Xuerong Zhou, Guansong Pang, Yujia Sun, Jing Liu, Peng Wang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Video anomaly detection (VAD) with weak supervision has achieved remarkable performance in utilizing video-level labels to discriminate whether a video frame is normal or abnormal. However, current approaches are inherently limited to a closed-set setting and may struggle in open-world applications where there can be anomaly categories in the test data unseen during training. A few recent studies attempt to tackle a more realistic setting, open-set VAD, which aims to detect unseen anomalies given seen anomalies and normal videos. However, such a setting focuses on predicting frame anomaly scores, having no ability to recognize the specific categories of anomalies, despite the fact that this ability is essential for building more informed video surveillance systems. This paper takes a step further and explores open-vocabulary video anomaly detection (OVVAD), in which we aim to leverage pre-trained large models to detect and categorize seen and unseen anomalies. To this end, we propose a model that decouples OVVAD into two mutually complementary tasks -- class-agnostic detection and class-specific classification -- and jointly optimizes both tasks. Particularly, we devise a semantic knowledge injection module to introduce semantic knowledge from large language models for the detection task, and design a novel anomaly synthesis module to generate pseudo unseen anomaly videos with the help of large vision generation models for the classification task. These semantic knowledge and synthesis anomalies substantially extend our model's capability in detecting and categorizing a variety of seen and unseen anomalies. Extensive experiments on three widely-used benchmarks demonstrate our model achieves state-of-the-art performance on OVVAD task.

### SED: A Simple Encoder-Decoder for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2311.15537](https://arxiv.org/abs/2311.15537) · 📚 被引 90
- **作者**: Bin Xie, Jiale Cao, Jin Xie, Fahad Shahbaz Khan, Yanwei Pang
- **🏷️ 机构**: Tianjin University, Chongqing University, Mohamed bin Zayed University of Artificial Intelligence
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation strives to distinguish pixels into different semantic groups from an open set of categories. Most existing methods explore utilizing pre-trained vision-language models, in which the key is to adopt the image-level model for pixel-level segmentation task. In this paper, we propose a simple encoder-decoder, named SED, for open-vocabulary semantic segmentation, which comprises a hierarchical encoder-based cost map generation and a gradual fusion decoder with category early rejection. The hierarchical encoder-based cost map generation employs hierarchical backbone, instead of plain transformer, to predict pixel-level image-text cost map. Compared to plain transformer, hierarchical backbone better captures local spatial information and has linear computational complexity with respect to input size. Our gradual fusion decoder employs a top-down structure to combine cost map and the feature maps of different backbone levels for segmentation. To accelerate inference speed, we introduce a category early rejection scheme in the decoder that rejects many no-existing categories at the early layer of decoder, resulting in at most 4.7 times acceleration without accuracy degradation. Experiments are performed on multiple open-vocabulary semantic segmentation datasets, which demonstrates the efficacy of our SED method. When using ConvNeXt-B, our SED method achieves mIoU score of 31.6\% on ADE20K with 150 categories at 82 millisecond ($ms$) per image on a single A6000. We will release it at \url{https://github.com/xb534/SED.git}.

### Visual Programming for Zero-Shot Open-Vocabulary 3D Visual Grounding.
- **链接**: [arXiv:2311.15383](https://arxiv.org/abs/2311.15383) · 📚 被引 39
- **作者**: Zhihao Yuan, Jinke Ren, Chun-Mei Feng, Hengshuang Zhao, Shuguang Cui, Zhen Li
- **🏷️ 机构**: FNii, CUHKSZ, IHPC, A*STAR,Singapore, HKU
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > 3D Visual Grounding (3DVG) aims at localizing 3D object based on textual descriptions. Conventional supervised methods for 3DVG often necessitate extensive annotations and a predefined vocabulary, which can be restrictive. To address this issue, we propose a novel visual programming approach for zero-shot open-vocabulary 3DVG, leveraging the capabilities of large language models (LLMs). Our approach begins with a unique dialog-based method, engaging with LLMs to establish a foundational understanding of zero-shot 3DVG. Building on this, we design a visual program that consists of three types of modules, i.e., view-independent, view-dependent, and functional modules. These modules, specifically tailored for 3D scenarios, work collaboratively to perform complex reasoning and inference. Furthermore, we develop an innovative language-object correlation module to extend the scope of existing 3D object detectors into open-vocabulary scenarios. Extensive experiments demonstrate that our zero-shot approach can outperform some supervised baselines, marking a significant stride towards effective 3DVG.

### ArGue: Attribute-Guided Prompt Tuning for Vision-Language Models.
- **链接**: [arXiv:2311.16494](https://arxiv.org/abs/2311.16494) · 📚 被引 47
- **作者**: Xinyu Tian, Shu Zou, Zhaoyuan Yang, Jing Zhang
- **🏷️ 机构**: Australian National University, GE Research
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Although soft prompt tuning is effective in efficiently adapting Vision-Language (V&L) models for downstream tasks, it shows limitations in dealing with distribution shifts. We address this issue with Attribute-Guided Prompt Tuning (ArGue), making three key contributions. 1) In contrast to the conventional approach of directly appending soft prompts preceding class names, we align the model with primitive visual attributes generated by Large Language Models (LLMs). We posit that a model's ability to express high confidence in these attributes signifies its capacity to discern the correct class rationales. 2) We introduce attribute sampling to eliminate disadvantageous attributes, thus only semantically meaningful attributes are preserved. 3) We propose negative prompting, explicitly enumerating class-agnostic attributes to activate spurious correlations and encourage the model to generate highly orthogonal probability distributions in relation to these negative features. In experiments, our method significantly outperforms current state-of-the-art prompt tuning methods on both novel class prediction and out-of-distribution generalization tasks.

## 跨领域论文（完整笔记在其他领域）

- Generative Region-Language Pretraining for Open-Ended Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- YOLO-World: Real-Time Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- InstaGen: Enhancing Object Detection by Training on Synthetic Dataset. → [object-detection](../object-detection/Guideline%202024.md)
- Retrieval-Augmented Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- SHiNe: Semantic Hierarchy Nexus for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Exploring Region-Word Alignment in Built-in Detector for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Scene-adaptive and Region-aware Multi-modal Prompt for Open Vocabulary Object Detection. → [multimodal](../multimodal/Guideline%202024.md)
- Taming Self-Training for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Training-Free Open-Vocabulary Segmentation with Offline Diffusion-Augmented Prototype Generation. → [multimodal](../multimodal/Guideline%202024.md)
- The Devil is in the Fine-Grained Details: Evaluating open-Vocabulary Object Detectors for Fine-Grained Understanding. → [object-detection](../object-detection/Guideline%202024.md)
- CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation. → [multimodal](../multimodal/Guideline%202024.md)
- Exploring the Potential of Large Foundation Models for Open-Vocabulary HOI Detection. → [object-detection](../object-detection/Guideline%202024.md)
- OVMR: Open-Vocabulary Recognition with Multi-Modal References. → [multimodal](../multimodal/Guideline%202024.md)
- Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- Image-to-Image Matching via Foundation Models: A New Perspective for Open-Vocabulary Semantic Segmentation. → [multimodal](../multimodal/Guideline%202024.md)
- Transferable and Principled Efficiency for Open-Vocabulary Segmentation. → [network-pruning](../network-pruning/Guideline%202024.md)
- MaskClustering: View Consensus Based Mask Graph Clustering for Open-Vocabulary 3D Instance Segmentation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and StructurEd Representation. → [multimodal](../multimodal/Guideline%202024.md)
- RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- Self-Supervised Class-Agnostic Motion Prediction with Spatial and Temporal Consistency Regularizations. → [autonomous-driving](../autonomous-driving/Guideline%202024.md)
- OmniSeg3D: Omniversal 3D Segmentation via Hierarchical Contrastive Learning. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- EfficientSAM: Leveraged Masked Image Pretraining for Efficient Segment Anything. → [object-detection](../object-detection/Guideline%202024.md)
