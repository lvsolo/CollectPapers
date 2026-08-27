# Neural Architecture Search — 2020 Guideline

> 领域: 神经架构搜索（NAS、Zero-Cost、搜索空间）
> 论文数: 4 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Hit-Detector: Hierarchical Trinity Architecture Search for Object Detection.
- **链接**: [arXiv:2003.11818](https://arxiv.org/abs/2003.11818) · [代码](https://github.com/ggjy/HitDet.pytorch) · 📚 被引 81
- **作者**: Jianyuan Guo, Kai Han, Yunhe Wang, Chao Zhang, Zhaohui Yang, Han Wu et al.
- **🏷️ 机构**: Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University; Noah's Ark Lab, Huawei Technologies, Noah's Ark Lab, Huawei Technologies, Key Lab of Machine Perception (MOE), Dept. of Machine Intelligence, Peking University
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Neural Architecture Search (NAS) has achieved great success in image classification task. Some recent works have managed to explore the automatic design of efficient backbone or feature fusion layer for object detection. However, these methods focus on searching only one certain component of object detector while leaving others manually designed. We identify the inconsistency between searched component and manually designed ones would withhold the detector of stronger performance. To this end, we propose a hierarchical trinity search framework to simultaneously discover efficient architectures for all components (i.e. backbone, neck, and head) of object detector in an end-to-end manner. In addition, we empirically reveal that different parts of the detector prefer different operators. Motivated by this, we employ a novel scheme to automatically screen different sub search spaces for different components so as to perform the end-to-end search for each component on the corresponding sub search space efficiently. Without bells and whistles, our searched architecture, namely Hit-Detector, achieves 41.4\% mAP on COCO minival set with 27M parameters. Our implementation is available at https://github.com/ggjy/HitDet.pytorch.

</details>

### SP-NAS: Serial-to-Parallel Backbone Search for Object Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Jiang_SP-NAS_Serial-to-Parallel_Backbone_Search_for_Object_Detection_CVPR_2020_paper.html) · 📚 被引 56
- **作者**: Chenhan Jiang, Hang Xu, Wei Zhang, Xiaodan Liang, Zhenguo Li
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020

### NAS-FCOS: Fast Neural Architecture Search for Object Detection.
- **链接**: [arXiv:1906.04423](https://arxiv.org/abs/1906.04423) · 📚 被引 200
- **作者**: Ning Wang, Yang Gao, Hao Chen, Peng Wang, Zhi Tian, Chunhua Shen et al.
- **🏷️ 机构**: ZJU
- **会议**: CVPR 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The success of deep neural networks relies on significant architecture engineering. Recently neural architecture search (NAS) has emerged as a promise to greatly reduce manual effort in network design by automatically searching for optimal architectures, although typically such algorithms need an excessive amount of computational resources, e.g., a few thousand GPU-days. To date, on challenging vision tasks such as object detection, NAS, especially fast versions of NAS, is less studied. Here we propose to search for the decoder structure of object detectors with search efficiency being taken into consideration. To be more specific, we aim to efficiently search for the feature pyramid network (FPN) as well as the prediction head of a simple anchor-free object detector, namely FCOS, using a tailored reinforcement learning paradigm. With carefully designed search space, search algorithms and strategies for evaluating network quality, we are able to efficiently search a top-performing detection architecture within 4 days using 8 V100 GPUs. The discovered architecture surpasses state-of-the-art object detection models (such as Faster R-CNN, RetinaNet and FCOS) by 1.5 to 3.5 points in AP on the COCO dataset, with comparable computation complexity and memory footprint, demonstrating the efficacy of the proposed NAS for object detection.

</details>

### Block-Wisely Supervised Neural Architecture Search With Knowledge Distillation.
- **链接**: [出版页](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Block-Wisely_Supervised_Neural_Architecture_Search_With_Knowledge_Distillation_CVPR_2020_paper.html) · 📚 被引 119
- **作者**: Changlin Li, Jiefeng Peng, Liuchun Yuan, Guangrun Wang, Xiaodan Liang, Liang Lin et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2020
