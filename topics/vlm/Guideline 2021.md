# VLM — 2021 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份:

### Structured Scene Memory for Vision-Language Navigation. **⭐⭐⭐** (相关度: 60%)
- **链接**: [arXiv:2103.03454](https://arxiv.org/abs/2103.03454) · 📚 被引 106
- **作者**: Hanqing Wang, Wenguan Wang, Wei Liang, Caiming Xiong, Jianbing Shen
- **🏷️ 机构**: Beijing Institute of Technology, ETH Zurich, Salesforce Research
- **会议**: CVPR 2021
- **摘要（中）**: ①针对视觉语言导航（VLN）中智能体仅将历史经验存储为循环网络中的隐状态，无法捕捉环境布局和进行长期规划的问题。②提出了结构化场景记忆（SSM）架构，通过分离的模块准确记忆导航过程中的感知信息，并作为结构化场景表示，捕捉和分离环境中的视觉与几何线索；同时引入collect-read控制器，自适应收集信息以支持当前决策，并模拟迭代算法进行长程推理。③相比已有工作，SSM提供了完整的动作空间（地图上所有可导航位置），并基于前沿探索的导航决策策略实现高效全局规划。④在R2R和R4R两个VLN数据集上取得了最先进的性能。
- **摘要（英）**: This paper addresses the limitation of VLN agents that store past experiences as latent states in recurrent networks, failing to capture environment layouts and plan long-term. It proposes Structured Scene Memory (SSM), a compartmentalized architecture that memorizes percepts, captures visual and geometric cues, and uses a collect-read controller for adaptive decision-making and iterative long-range reasoning. SSM enables frontier-exploration-based global planning and achieves state-of-the-art performance on R2R and R4R datasets.
- **核心贡献**: 提出了结构化场景记忆架构，为VLN提供完整的动作空间和全局规划能力。
- **创新点**: 通过collect-read控制器和前沿探索策略，实现了基于结构化场景记忆的长期推理与全局规划。
- **结果**: 在R2R和R4R数据集上达到最先进性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, numerous algorithms have been developed to tackle the problem of vision-language navigation (VLN), i.e., entailing an agent to navigate 3D environments through following linguistic instructions. However, current VLN agents simply store their past experiences/observations as latent states in recurrent networks, failing to capture environment layouts and make long-term planning. To address these limitations, we propose a crucial architecture, called Structured Scene Memory (SSM). It is compartmentalized enough to accurately memorize the percepts during navigation. It also serves as a structured scene representation, which captures and disentangles visual and geometric cues in the environment. SSM has a collect-read controller that adaptively collects information for supporting current decision making and mimics iterative algorithms for long-range reasoning. As SSM provides a complete action space, i.e., all the navigable places on the map, a frontier-exploration based navigation decision making strategy is introduced to enable efficient and global planning. Experiment results on two VLN datasets (i.e., R2R and R4R) show that our method achieves state-of-the-art performance on several metrics.

</details>

### VinVL: Revisiting Visual Representations in Vision-Language Models. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_VinVL_Revisiting_Visual_Representations_in_Vision-Language_Models_CVPR_2021_paper.html) · 📚 被引 747
- **作者**: Pengchuan Zhang, Xiujun Li, Xiaowei Hu, Jianwei Yang, Lei Zhang, Lijuan Wang et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2021
- **摘要（中）**: ①针对视觉语言模型中视觉表示质量不足的问题，特别是目标检测特征在跨模态任务中的局限性。②提出了VinVL，通过重新审视视觉表示，采用改进的目标检测模型（基于更大的骨干网络和更丰富的训练数据）生成更丰富的视觉特征，并用于多种视觉语言任务。③相比已有工作，VinVL在视觉特征提取上进行了系统优化，包括模型架构、预训练数据和训练策略。④在多个视觉语言基准（如VQA、Image Captioning）上取得了显著提升，例如在VQA 2.0上达到最先进水平。
- **摘要（英）**: This paper addresses the insufficient quality of visual representations in vision-language models, particularly the limitations of object detection features. It proposes VinVL, which revisits visual representations by using an improved object detection model with a larger backbone and richer training data to generate more informative visual features. VinVL achieves significant improvements on multiple vision-language benchmarks, including state-of-the-art results on VQA 2.0.
- **核心贡献**: 提出了VinVL，通过优化目标检测模型和训练数据，显著提升了视觉语言任务的视觉表示质量。
- **创新点**: 系统性地重新设计了视觉特征提取流程，包括模型架构、预训练数据和训练策略。
- **结果**: 在VQA 2.0等多个基准上达到最先进性能。

### Improving Weakly Supervised Visual Grounding by Contrastive Knowledge Distillation. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2007.01951](https://arxiv.org/abs/2007.01951) · 📚 被引 63
- **作者**: Liwei Wang, Jing Huang, Yin Li, Kun Xu, Zhengyuan Yang, Dong Yu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021
- **摘要（中）**: 针对弱监督视觉定位中区域-短语对应缺失的问题，提出对比知识蒸馏框架，同时优化区域-短语和图像-句子匹配。核心创新是学习区域-短语评分函数，通过从检测目标名称与候选短语的软匹配分数中蒸馏知识，并利用图像-句子真值监督。该方法在测试时无需目标检测器，显著降低推理成本，在视觉短语定位任务上取得了最先进结果。
- **摘要（英）**: This paper tackles missing region-phrase correspondences in weakly supervised visual grounding by proposing a contrastive knowledge distillation framework that learns a region-phrase score function from soft matching scores and supervises image-sentence matching. It removes the need for object detectors at test time, achieving state-of-the-art results with lower inference cost.
- **核心贡献**: 提出对比知识蒸馏框架，实现无检测器推理的弱监督视觉定位。
- **创新点**: 通过蒸馏软匹配分数学习区域-短语评分函数，避免测试时检测。
- **结果**: 在视觉短语定位任务上超越现有方法，同时降低推理成本。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Weakly supervised phrase grounding aims at learning region-phrase correspondences using only image-sentence pairs. A major challenge thus lies in the missing links between image regions and sentence phrases during training. To address this challenge, we leverage a generic object detector at training time, and propose a contrastive learning framework that accounts for both region-phrase and image-sentence matching. Our core innovation is the learning of a region-phrase score function, based on which an image-sentence score function is further constructed. Importantly, our region-phrase score function is learned by distilling from soft matching scores between the detected object names and candidate phrases within an image-sentence pair, while the image-sentence score function is supervised by ground-truth image-sentence pairs. The design of such score functions removes the need of object detection at test time, thereby significantly reducing the inference cost. Without bells and whistles, our approach achieves state-of-the-art results on visual phrase grounding, surpassing previous methods that require expensive object detectors at test time.

</details>

### Vision-Language Navigation with Random Environmental Mixup.
- **链接**: [arXiv:2106.07876](https://arxiv.org/abs/2106.07876) · [代码](https://github.com/LCFractal/VLNREM) · 📚 被引 65
- **作者**: Chong Liu, Fengda Zhu, Xiaojun Chang, Xiaodan Liang, Zongyuan Ge, Yi-Dong Shen
- **🏷️ 机构**: Chinese Academy of Sciences,State Key Laboratory of Computer Science, Institute of Software,China, Monash University,Melbourne,Australia, RMIT University,Melbourne,Australia
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language Navigation (VLN) tasks require an agent to navigate step-by-step while perceiving the visual observations and comprehending a natural language instruction. Large data bias, which is caused by the disparity ratio between the small data scale and large navigation space, makes the VLN task challenging. Previous works have proposed various data augmentation methods to reduce data bias. However, these works do not explicitly reduce the data bias across different house scenes. Therefore, the agent would overfit to the seen scenes and achieve poor navigation performance in the unseen scenes. To tackle this problem, we propose the Random Environmental Mixup (REM) method, which generates cross-connected house scenes as augmented data via mixuping environment. Specifically, we first select key viewpoints according to the room connection graph for each scene. Then, we cross-connect the key views of different scenes to construct augmented scenes. Finally, we generate augmented instruction-path pairs in the cross-connected scenes. The experimental results on benchmark datasets demonstrate that our augmentation data via REM help the agent reduce its performance gap between the seen and unseen environment and improve the overall performance, making our model the best existing approach on the standard VLN benchmark. The code have released: https://github.com/LCFractal/VLNREM.

</details>

### The Road to Know-Where: An Object-and-Room Informed Sequential BERT for Indoor Vision-Language Navigation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00168) · 📚 被引 67
- **作者**: Yuankai Qi, Zizheng Pan, Yicong Hong, Ming-Hsuan Yang, Anton van den Hengel, Qi Wu
- **🏷️ 机构**: The University of Adelaide,Australian Institute for Machine Learning, Monash University, The Australian National University
- **会议**: ICCV 2021

## 🆕 增量新增

### InstanceRefer: Cooperative Holistic Understanding for Visual Grounding on Point Clouds through Instance Multi-level Contextual Referring. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00181)
- **作者**: Zhihao Yuan, Xu Yan, Yinghong Liao, Ruimao Zhang, Sheng Wang, Zhen Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对点云视觉定位（visual grounding on point clouds）中现有方法仅利用局部或全局特征，缺乏对实例级上下文和跨模态关系的理解。②提出了InstanceRefer，通过实例多级上下文引用，协同理解点云场景，包括实例级特征提取、多级上下文建模和跨模态匹配。③相比已有工作，InstanceRefer更全面地整合了实例间关系和语言描述，提升了定位精度。④在ScanRefer和ReferIt3D等基准上取得了最先进的性能。
- **摘要（英）**: This paper addresses the limitation of point cloud visual grounding methods that rely on local or global features without instance-level context and cross-modal relations. It proposes InstanceRefer, which uses instance multi-level contextual referring for cooperative understanding, including instance feature extraction, multi-level context modeling, and cross-modal matching. The method achieves state-of-the-art performance on ScanRefer and ReferIt3D benchmarks.
- **核心贡献**: 提出了实例多级上下文引用方法，提升点云视觉定位性能。
- **创新点**: 通过实例级特征和跨模态匹配，实现协同场景理解。
- **结果**: 在ScanRefer和ReferIt3D上达到最先进性能。

### 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00292)
- **作者**: Lichen Zhao, Daigang Cai, Lu Sheng, Dong Xu
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2021
- **摘要（中）**: ①针对点云视觉定位中关系建模不足的问题，现有方法难以捕捉对象间的空间和语义关系。②提出了3DVG-Transformer，利用Transformer架构建模点云中对象间的关系，包括空间关系和语义关系，并融合语言特征进行定位。③相比已有工作，3DVG-Transformer通过关系建模增强了场景理解能力。④在ScanRefer和ReferIt3D等基准上取得了竞争性性能。
- **摘要（英）**: This paper addresses the insufficient relation modeling in point cloud visual grounding, where existing methods struggle to capture spatial and semantic relations between objects. It proposes 3DVG-Transformer, which uses Transformer architecture to model object relations in point clouds and fuse language features for grounding. The method achieves competitive performance on ScanRefer and ReferIt3D benchmarks.
- **核心贡献**: 提出了基于Transformer的关系建模方法，提升点云视觉定位精度。
- **创新点**: 利用Transformer捕捉对象间空间和语义关系。
- **结果**: 在ScanRefer和ReferIt3D上取得竞争性性能。

## 跨领域论文（完整笔记在其他领域）

- Parameter Efficient Multimodal Transformers for Video Representation Learning. → [multimodal](../multimodal/Guideline%202021.md)

<!-- COMPLETE v1 papers=7 -->
