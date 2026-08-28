# Object Detection — 2020 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 1 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Frustratingly Simple Few-Shot Object Detection.
- **链接**: [arXiv:2003.06957](https://arxiv.org/abs/2003.06957) · [代码](https://github.com/ucbdrive/few-shot-object-detection)
- **作者**: Xin Wang, Thomas E. Huang, Joseph Gonzalez, Trevor Darrell, Fisher Yu
- **🏷️ 机构**: UC Berkeley, ETH Zurich
- **会议**: ICML 2020

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Detecting rare objects from a few examples is an emerging problem. Prior works show meta-learning is a promising approach. But, fine-tuning techniques have drawn scant attention. We find that fine-tuning only the last layer of existing detectors on rare classes is crucial to the few-shot object detection task. Such a simple approach outperforms the meta-learning methods by roughly 2~20 points on current benchmarks and sometimes even doubles the accuracy of the prior methods. However, the high variance in the few samples often leads to the unreliability of existing benchmarks. We revise the evaluation protocols by sampling multiple groups of training examples to obtain stable comparisons and build new benchmarks based on three datasets: PASCAL VOC, COCO and LVIS. Again, our fine-tuning approach establishes a new state of the art on the revised benchmarks. The code as well as the pretrained models are available at https://github.com/ucbdrive/few-shot-object-detection.

</details>
