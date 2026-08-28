# VLM — 2021 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### InstanceRefer: Cooperative Holistic Understanding for Visual Grounding on Point Clouds through Instance Multi-level Contextual Referring.
- **链接**: [arXiv:2103.01128](https://arxiv.org/abs/2103.01128) · 📚 被引 102
- **作者**: Zhihao Yuan, Xu Yan, Yinghong Liao, Ruimao Zhang, Sheng Wang, Zhen Li et al.
- **🏷️ 机构**: The Chinese University of Hong Kong (Shenzhen),Shenzhen Research Institute of Big Data, Southern University of Science and Technology,CryoEM Center
- **会议**: ICCV 2021

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Compared with the visual grounding on 2D images, the natural-language-guided 3D object localization on point clouds is more challenging. In this paper, we propose a new model, named InstanceRefer, to achieve a superior 3D visual grounding through the grounding-by-matching strategy. In practice, our model first predicts the target category from the language descriptions using a simple language classification model. Then, based on the category, our model sifts out a small number of instance candidates (usually less than 20) from the panoptic segmentation of point clouds. Thus, the non-trivial 3D visual grounding task has been effectively re-formulated as a simplified instance-matching problem, considering that instance-level candidates are more rational than the redundant 3D object proposals. Subsequently, for each candidate, we perform the multi-level contextual inference, i.e., referring from instance attribute perception, instance-to-instance relation perception, and instance-to-background global localization perception, respectively. Eventually, the most relevant candidate is selected and localized by ranking confidence scores, which are obtained by the cooperative holistic visual-language feature matching. Experiments confirm that our method outperforms previous state-of-the-arts on ScanRefer online benchmark and Nr3D/Sr3D datasets.

</details>

### 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds.
- **链接**: [出版页](https://doi.org/10.1109/ICCV48922.2021.00292) · 📚 被引 137
- **作者**: Lichen Zhao, Daigang Cai, Lu Sheng, Dong Xu
- **🏷️ 机构**: Beihang University,College of Software,China, The University of Sydney,Australia
- **会议**: ICCV 2021

### Vision-Language Navigation with Random Environmental Mixup.
- **链接**: [arXiv:2106.07876](https://arxiv.org/abs/2106.07876) · [代码](https://github.com/LCFractal/VLNREM)
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
