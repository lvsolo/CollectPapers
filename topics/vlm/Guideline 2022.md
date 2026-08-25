# VLM — 2022 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 13 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### PointCLIP: Point Cloud Understanding by CLIP.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00836) · 📚 被引 421
- **作者**: Renrui Zhang, Ziyu Guo, Wei Zhang, Kunchang Li, Xupeng Miao, Bin Cui et al.
- **🏷️ 机构**: Shanghai AI Laboratory, Peking University,School of CS and Key Lab of HCST
- **会议**: CVPR 2022

### 3DJCG: A Unified Framework for Joint Dense Captioning and Visual Grounding on 3D Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01597) · 📚 被引 94
- **作者**: Daigang Cai, Lichen Zhao, Jing Zhang, Lu Sheng, Dong Xu
- **🏷️ 机构**: College of Software, Beihang University,China, The University of Sydney,Australia
- **会议**: CVPR 2022

### Scaling Up Vision-Language Pretraining for Image Captioning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01745) · 📚 被引 167
- **作者**: Xiaowei Hu, Zhe Gan, Jianfeng Wang, Zhengyuan Yang, Zicheng Liu, Yumao Lu et al.
- **🏷️ 机构**: Microsoft
- **会议**: CVPR 2022

### Reinforced Structured State-Evolution for Vision-Language Navigation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01501) · 📚 被引 42
- **作者**: Jinyu Chen, Chen Gao, Erli Meng, Qiong Zhang, Si Liu
- **🏷️ 机构**: Institute of Artificial Intelligence, Beihang University, Xiaomi Inc,Xiaomi AI Lab
- **会议**: CVPR 2022

### ADAPT: Vision-Language Navigation with Modality-Aligned Action Prompts.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01496) · 📚 被引 44
- **作者**: Bingqian Lin, Yi Zhu, Zicong Chen, Xiwen Liang, Jianzhuang Liu, Xiaodan Liang
- **🏷️ 机构**: Shcnzhcn Campus of Sun Yat-sen University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2022

### Counterfactual Cycle-Consistent Learning for Instruction Following and Generation in Vision-Language Navigation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01503) · 📚 被引 53
- **作者**: Hanqing Wang, Wei Liang, Jianbing Shen, Luc Van Gool, Wenguan Wang
- **🏷️ 机构**: Beijing Institute of Technology, SKL-IOTSC, University of Macau, ETH Zurich
- **会议**: CVPR 2022

### Predict, Prevent, and Evaluate: Disentangled Text-Driven Image Manipulation Empowered by Pre-Trained Vision-Language Model.
- **链接**: [arXiv:2111.13333](https://arxiv.org/abs/2111.13333) · 📚 被引 33
- **作者**: Zipeng Xu, Tianwei Lin, Hao Tang, Fu Li, Dongliang He, Nicu Sebe et al.
- **🏷️ 机构**: University of Trento,MHUG, VIS, Baidu Inc., CVL, ETH Z&#x00FC;rich
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > To achieve disentangled image manipulation, previous works depend heavily on manual annotation. Meanwhile, the available manipulations are limited to a pre-defined set the models were trained for. We propose a novel framework, i.e., Predict, Prevent, and Evaluate (PPE), for disentangled text-driven image manipulation that requires little manual annotation while being applicable to a wide variety of manipulations. Our method approaches the targets by deeply exploiting the power of the large-scale pre-trained vision-language model CLIP. Concretely, we firstly Predict the possibly entangled attributes for a given text command. Then, based on the predicted attributes, we introduce an entanglement loss to Prevent entanglements during training. Finally, we propose a new evaluation metric to Evaluate the disentangled image manipulation. We verify the effectiveness of our method on the challenging face editing task. Extensive experiments show that the proposed PPE framework achieves much better quantitative and qualitative results than the up-to-date StyleCLIP baseline.

### Conditional Prompt Learning for Vision-Language Models.
- **链接**: [arXiv:2203.05557](https://arxiv.org/abs/2203.05557) · [代码](https://github.com/KaiyangZhou/CoOp) · 📚 被引 1676
- **作者**: Kaiyang Zhou, Jingkang Yang, Chen Change Loy, Ziwei Liu
- **🏷️ 机构**: Nanyang Technological University,S-Lab,Singapore
- **会议**: CVPR 2022

- **摘要（英，原文）**:

  > With the rise of powerful pre-trained vision-language models like CLIP, it becomes essential to investigate ways to adapt these models to downstream datasets. A recently proposed method named Context Optimization (CoOp) introduces the concept of prompt learning -- a recent trend in NLP -- to the vision domain for adapting pre-trained vision-language models. Specifically, CoOp turns context words in a prompt into a set of learnable vectors and, with only a few labeled images for learning, can achieve huge improvements over intensively-tuned manual prompts. In our study we identify a critical problem of CoOp: the learned context is not generalizable to wider unseen classes within the same dataset, suggesting that CoOp overfits base classes observed during training. To address the problem, we propose Conditional Context Optimization (CoCoOp), which extends CoOp by further learning a lightweight neural network to generate for each image an input-conditional token (vector). Compared to CoOp's static prompts, our dynamic prompts adapt to each instance and are thus less sensitive to class shift. Extensive experiments show that CoCoOp generalizes much better than CoOp to unseen classes, even showing promising transferability beyond a single dataset; and yields stronger domain generalization performance as well. Code is available at https://github.com/KaiyangZhou/CoOp.

## 跨领域论文（完整笔记在其他领域）

- Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model. → [object-detection](../object-detection/Guideline%202022.md)
- Multi-View Transformer for 3D Visual Grounding. → [multi-camera-perception](../multi-camera-perception/Guideline%202022.md)
- Expanding Large Pre-trained Unimodal Models with Multimodal Information Injection for Image-Text Multimodal Classification. → [multimodal](../multimodal/Guideline%202022.md)
- EI-CLIP: Entity-aware Interventional Contrastive Learning for E-commerce Cross-modal Retrieval. → [multimodal](../multimodal/Guideline%202022.md)
- Unified Contrastive Learning in Image-Text-Label Space. → [self-supervised-vision](../self-supervised-vision/Guideline%202022.md)
