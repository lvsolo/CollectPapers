# Open-set Detection — 2020 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Open-Edit: Open-Domain Image Manipulation with Open-Vocabulary Instructions.
- **链接**: [出版页](https://doi.org/10.1007/978-3-030-58621-8_6) · 📚 被引 25
- **作者**: Xihui Liu, Zhe Lin, Jianming Zhang, Handong Zhao, Quan Tran, Xiaogang Wang et al.
- **🏷️ 机构**: CUHK / Shanghai AI Lab, CUHK
- **会议**: ECCV 2020

## 🆕 增量新增

### Exploring Bottom-Up and Top-Down Cues With Attentive Learning for Webly Supervised Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2003.09790](https://arxiv.org/abs/2003.09790) · 📚 被引 10
- **作者**: Zhonghua Wu, Qingyi Tao, Guosheng Lin, Jianfei Cai
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对新类别目标检测依赖大量人工标注框的问题，提出一种仅需网络图像（无需任何标注）的Webly监督目标检测方法。②方法结合自底向上和自顶向下线索：利用预训练Faster RCNN作为区域估计器，通过共享的通用物体性（objectiveness）识别新类候选区域；随后用自顶向下注意力线索指导区域分类，并引入残差特征细化（RFR）模块解决网络域与目标域之间的域偏移。③相比已有WebSOD方法，创新性地融合了自底向上的区域估计与自顶向下的注意力分类，并显式建模域差异。④在PASCAL VOC数据集上，使用三种不同的新类/基类划分进行实验，在无目标域新类图像和标注的情况下取得了有竞争力的检测性能。
- **摘要（英）**: This paper addresses the problem of detecting novel object classes without manual bounding box annotations by leveraging web images. It proposes a webly supervised detection method that combines bottom-up region estimation from a pretrained detector with top-down attention-guided classification, plus a residual feature refinement block to mitigate domain shift. Experiments on PASCAL VOC with multiple novel/base splits demonstrate competitive performance without target-domain annotations.
- **核心贡献**: 提出一种结合自底向上和自顶向下线索的Webly监督目标检测框架，并引入残差特征细化模块处理域偏移。
- **创新点**: 将通用物体性估计与注意力分类线索结合，并显式建模网络域与目标域的差异。
- **结果**: 在PASCAL VOC三个新类/基类划分上，无需目标域标注即取得有竞争力的检测性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fully supervised object detection has achieved great success in recent years. However, abundant bounding boxes annotations are needed for training a detector for novel classes. To reduce the human labeling effort, we propose a novel webly supervised object detection (WebSOD) method for novel classes which only requires the web images without further annotations. Our proposed method combines bottom-up and top-down cues for novel class detection. Within our approach, we introduce a bottom-up mechanism based on the well-trained fully supervised object detector (i.e. Faster RCNN) as an object region estimator for web images by recognizing the common objectiveness shared by base and novel classes. With the estimated regions on the web images, we then utilize the top-down attention cues as the guidance for region classification. Furthermore, we propose a residual feature refinement (RFR) block to tackle the domain mismatch between web domain and the target domain. We demonstrate our proposed method on PASCAL VOC dataset with three different novel/base splits. Without any target-domain novel-class images and annotations, our proposed webly supervised object detection model is able to achieve promising performance for novel classes. Moreover, we also conduct transfer learning experiments on large scale ILSVRC 2013 detection dataset and achieve state-of-the-art performance.

</details>

### Don't Even Look Once: Synthesizing Features for Zero-Shot Detection. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhu_Dont_Even_Look_Once_Synthesizing_Features_for_Zero-Shot_Detection_CVPR_2020_paper.html) · 📚 被引 60
- **作者**: Pengkai Zhu, Hanxiao Wang, Venkatesh Saligrama
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
- **摘要（中）**: ①针对零样本检测（ZSD）中未见类（unseen classes）缺乏训练样本的问题，提出一种无需直接处理视觉特征的方法。②方法名为“Don't Even Look Once”（DELO），核心思想是直接为未见类合成特征，而非从图像中提取特征；通过生成模型在语义空间（如属性或词向量）条件下合成视觉特征，并训练检测器识别这些合成特征。③相比已有ZSD方法（如直接使用视觉特征或对齐视觉-语义空间），DELO避免了未见类视觉特征不可用的问题，且能更灵活地控制特征生成过程。④在标准ZSD基准（如PASCAL VOC、MS COCO）上，该方法在未见类检测和整体检测性能上均达到当时最先进水平，显著提升了零样本检测的召回率和准确率。
- **摘要（英）**: This paper tackles zero-shot detection by synthesizing visual features for unseen classes instead of relying on unavailable visual examples. The proposed DELO method generates features conditioned on semantic embeddings and trains a detector on these synthetic features, avoiding the need to look at images of unseen classes. It achieves state-of-the-art performance on standard ZSD benchmarks, improving both recall and accuracy for unseen classes.
- **核心贡献**: 提出一种通过特征合成实现零样本检测的新框架，无需任何未见类图像。
- **创新点**: 创新性地将检测问题转化为特征生成问题，利用语义条件生成模型合成未见类特征。
- **结果**: 在PASCAL VOC和MS COCO上达到当时最先进的零样本检测性能。

### A Latent Morphology Model for Open-Vocabulary Neural Machine Translation. **⭐⭐** (相关度: 10%)
- **链接**: [出版页](https://openreview.net/forum?id=BJxSI1SKDH)
- **作者**: Duygu Ataman, Wilker Aziz, Alexandra Birch
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2020
- **摘要（中）**: ①针对开放词汇神经机器翻译（NMT）中罕见词或未登录词（OOV）处理困难的问题，提出一种潜在形态学模型。②方法通过引入潜在形态学分解，将词分解为词根和词缀等形态学单元，并在潜在空间中进行建模，以改善翻译中对形态复杂语言的泛化能力。③相比传统子词切分（如BPE）或基于规则的方法，该模型能更灵活地学习形态结构，但摘要信息不完整，具体实验细节和效果未明确给出。④由于摘要被截断，无法提供具体数据或效果描述。
- **摘要（英）**: This paper addresses open-vocabulary issues in neural machine translation by proposing a latent morphology model that decomposes words into morphological units in a latent space. It aims to improve generalization for morphologically rich languages compared to subword segmentation methods. However, the abstract is incomplete, and specific experimental results are not available.
- **核心贡献**: 提出一种潜在形态学模型用于开放词汇NMT，但贡献不明确。
- **创新点**: 在潜在空间中进行形态学分解，但创新性缺乏细节支撑。
- **结果**: 摘要截断，无法评估具体效果。
<!-- COMPLETE v1 papers=4 -->
