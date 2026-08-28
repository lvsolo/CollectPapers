# Object Detection — 2024 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 8 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### LLMs Meet VLMs: Boost Open Vocabulary Object Detection with Fine-grained Descriptors.
- **链接**: [出版页](https://openreview.net/forum?id=usrChqw6yK)
- **作者**: Sheng Jin, Xueying Jiang, Jiaxing Huang, Lewei Lu, Shijian Lu
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### GeoDiffusion: Text-Prompted Geometric Control for Object Detection Data Generation.
- **链接**: [出版页](https://openreview.net/forum?id=xBfQZWeDRH)
- **作者**: Kai Chen, Enze Xie, Zhe Chen, Yibo Wang, Lanqing Hong, Zhenguo Li et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

### InstructDET: Diversifying Referring Object Detection with Generalized Instructions.
- **链接**: [arXiv:2310.05136](https://arxiv.org/abs/2310.05136)
- **作者**: Ronghao Dang, Jiangyan Feng, Haodong Zhang, Chongjian Ge, Lin Song, Lijun Gong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2024

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose InstructDET, a data-centric method for referring object detection (ROD) that localizes target objects based on user instructions. While deriving from referring expressions (REC), the instructions we leverage are greatly diversified to encompass common user intentions related to object detection. For one image, we produce tremendous instructions that refer to every single object and different combinations of multiple objects. Each instruction and its corresponding object bounding boxes (bbxs) constitute one training data pair. In order to encompass common detection expressions, we involve emerging vision-language model (VLM) and large language model (LLM) to generate instructions guided by text prompts and object bbxs, as the generalizations of foundation models are effective to produce human-like expressions (e.g., describing object property, category, and relationship). We name our constructed dataset as InDET. It contains images, bbxs and generalized instructions that are from foundation models. Our InDET is developed from existing REC datasets and object detection datasets, with the expanding potential that any image with object bbxs can be incorporated through using our InstructDET method. By using our InDET dataset, we show that a conventional ROD model surpasses existing methods on standard REC datasets and our InDET test set. Our data-centric method InstructDET, with automatic data expansion by leveraging foundation models, directs a promising field that ROD can be greatly diversified to execute common object detection instructions.

</details>

### Transferring Labels to Solve Annotation Mismatches Across Object Detection Datasets.
- **链接**: [出版页](https://openreview.net/forum?id=ChHx5ORqF0)
- **作者**: Yuan-Hong Liao, David Acuna, Rafid Mahmood, James Lucas, Viraj Prabhu, Sanja Fidler
- **🏷️ 机构**: NVIDIA / University of Toronto
- **会议**: ICLR 2024

## 跨领域论文（完整笔记在其他领域）

- V-DETR: DETR with Vertex Relative Position Encoding for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- Fusion Is Not Enough: Single Modal Attacks on Fusion Models for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- MixSup: Mixed-grained Supervision for Label-efficient LiDAR-based 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
- LiDAR-PTQ: Post-Training Quantization for Point Cloud 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202024.md)
