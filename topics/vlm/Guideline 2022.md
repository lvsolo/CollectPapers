# VLM — 2022 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 14 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2024](Guideline%202024.md)

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

## 跨领域论文（完整笔记在其他领域）

- MPPNet: Multi-frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202022.md)
- A Simple Baseline for Open-Vocabulary Semantic Segmentation with Pre-trained Vision-Language Model. → [open-set-detection](../open-set-detection/Guideline%202022.md)
- Single-Stream Multi-level Alignment for Vision-Language Pretraining. → [multimodal](../multimodal/Guideline%202022.md)
- Generative Negative Text Replay for Continual Vision-Language Pretraining. → [continual-learning](../continual-learning/Guideline%202022.md)
- Switch-BERT: Learning to Model Multimodal Interactions by Switching Attention and Input. → [multimodal](../multimodal/Guideline%202022.md)
- MUGEN: A Playground for Video-Audio-Text Multimodal Understanding and GENeration. → [multimodal](../multimodal/Guideline%202022.md)
- Hierarchically Self-supervised Transformer for Human Skeleton Representation Learning. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- Motion Sensitive Contrastive Learning for Self-supervised Video Representation. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
- CODER: Coupled Diversity-Sensitive Momentum Contrastive Learning for Image-Text Retrieval. → [multimodal](../multimodal/Guideline%202022.md)
- Learning Visual Representation from Modality-Shared Contrastive Language-Image Pre-training. → [multimodal](../multimodal/Guideline%202022.md)
