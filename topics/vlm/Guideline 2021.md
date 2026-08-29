# VLM — 2021 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 3 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Structured Scene Memory for Vision-Language Navigation.
- **链接**: [arXiv:2103.03454](https://arxiv.org/abs/2103.03454) · 📚 被引 106
- **作者**: Hanqing Wang, Wenguan Wang, Wei Liang, Caiming Xiong, Jianbing Shen
- **🏷️ 机构**: Beijing Institute of Technology, ETH Zurich, Salesforce Research
- **会议**: CVPR 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared with the visual grounding on 2D images, the natural-language-guided 3D object localization on point clouds is more challenging. In this paper, we propose a new model, named InstanceRefer, to achieve a superior 3D visual grounding through the grounding-by-matching strategy. In practice, our model first predicts the target category from the language descriptions using a simple language classification model. Then, based on the category, our model sifts out a small number of instance candidates (usually less than 20) from the panoptic segmentation of point clouds. Thus, the non-trivial 3D visual grounding task has been effectively re-formulated as a simplified instance-matching problem, considering that instance-level candidates are more rational than the redundant 3D object proposals. Subsequently, for each candidate, we perform the multi-level contextual inference, i.e., referring from instance attribute perception, instance-to-instance relation perception, and instance-to-background global localization perception, respectively. Eventually, the most relevant candidate is selected and localized by ranking confidence scores, which are obtained by the cooperative holistic visual-language feature matching. Experiments confirm that our method outperforms previous state-of-the-arts on ScanRefer online benchmark and Nr3D/Sr3D datasets.

</details>

### VinVL: Revisiting Visual Representations in Vision-Language Models.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_VinVL_Revisiting_Visual_Representations_in_Vision-Language_Models_CVPR_2021_paper.html) · 📚 被引 747
- **作者**: Pengchuan Zhang, Xiujun Li, Xiaowei Hu, Jianwei Yang, Lei Zhang, Lijuan Wang et al.
- **🏷️ 机构**: PolyU / OPPO
- **会议**: CVPR 2021

### Improving Weakly Supervised Visual Grounding by Contrastive Knowledge Distillation.
- **链接**: [arXiv:2007.01951](https://arxiv.org/abs/2007.01951) · 📚 被引 63
- **作者**: Liwei Wang, Jing Huang, Yin Li, Kun Xu, Zhengyuan Yang, Dong Yu
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2021

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
