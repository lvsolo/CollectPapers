# Self-supervised Vision — 2022 Guideline

> 领域: 视觉自监督学习（对比学习、MAE、DINO 系）
> 论文数: 11 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Self-Supervised Global-Local Structure Modeling for Point Cloud Domain Adaptation with Reliable Voted Pseudo Labels.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.00627) · 📚 被引 60
- **作者**: Hehe Fan, Xiaojun Chang, Wanyue Zhang, Yi Cheng, Ying Sun, Mohan S. Kankanhalli
- **🏷️ 机构**: School of Computing, National University of Singapore, ReLER Lab, AAII, University of Technology,Sydney, Max Planck Institute for Informatics
- **会议**: CVPR 2022

### RigidFlow: Self-Supervised Scene Flow Learning on Point Clouds by Local Rigidity Prior.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01645) · 📚 被引 48
- **作者**: Ruibo Li, Chi Zhang, Guosheng Lin, Zhe Wang, Chunhua Shen
- **🏷️ 机构**: Nanyang Technological University,S-Lab for Advanced Intelligence, School of Computer Science and Engineering, Nanyang Technological University, SenseTime Research
- **会议**: CVPR 2022

### Self-Supervised Arbitrary-Scale Point Clouds Upsampling via Implicit Neural Representation.
- **链接**: [arXiv:2204.08196](https://arxiv.org/abs/2204.08196) · [代码](https://github.com/xnowbzhao/sapcu) · 📚 被引 63
- **作者**: Wenbo Zhao, Xianming Liu, Zhiwei Zhong, Junjun Jiang, Wei Gao, Ge Li et al.
- **🏷️ 机构**: Harbin Institute of Technology, Peking University Shenzhen Graduate School, Tsinghua University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Point clouds upsampling is a challenging issue to generate dense and uniform point clouds from the given sparse input. Most existing methods either take the end-to-end supervised learning based manner, where large amounts of pairs of sparse input and dense ground-truth are exploited as supervision information; or treat up-scaling of different scale factors as independent tasks, and have to build multiple networks to handle upsampling with varying factors. In this paper, we propose a novel approach that achieves self-supervised and magnification-flexible point clouds upsampling simultaneously. We formulate point clouds upsampling as the task of seeking nearest projection points on the implicit surface for seed points. To this end, we define two implicit neural functions to estimate projection direction and distance respectively, which can be trained by two pretext learning tasks. Experimental results demonstrate that our self-supervised learning based scheme achieves competitive or even better performance than supervised learning based state-of-the-art methods. The source code is publicly available at https://github.com/xnowbzhao/sapcu.

</details>

### SimMIM: a Simple Framework for Masked Image Modeling.
- **链接**: [arXiv:2111.09886](https://arxiv.org/abs/2111.09886) · [代码](https://github.com/microsoft/SimMIM) · 📚 被引 1154
- **作者**: Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Jianmin Bao, Zhuliang Yao et al.
- **🏷️ 机构**: Tsinghua University, Microsoft Research Asia, Xi&#x0027;an Jiaotong University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This paper presents SimMIM, a simple framework for masked image modeling. We simplify recently proposed related approaches without special designs such as block-wise masking and tokenization via discrete VAE or clustering. To study what let the masked image modeling task learn good representations, we systematically study the major components in our framework, and find that simple designs of each component have revealed very strong representation learning performance: 1) random masking of the input image with a moderately large masked patch size (e.g., 32) makes a strong pre-text task; 2) predicting raw pixels of RGB values by direct regression performs no worse than the patch classification approaches with complex designs; 3) the prediction head can be as light as a linear layer, with no worse performance than heavier ones. Using ViT-B, our approach achieves 83.8% top-1 fine-tuning accuracy on ImageNet-1K by pre-training also on this dataset, surpassing previous best approach by +0.6%. When applied on a larger model of about 650 million parameters, SwinV2-H, it achieves 87.1% top-1 accuracy on ImageNet-1K using only ImageNet-1K data. We also leverage this approach to facilitate the training of a 3B model (SwinV2-G), that by $40\times$ less data than that in previous practice, we achieve the state-of-the-art on four representative vision benchmarks. The code and models will be publicly available at https://github.com/microsoft/SimMIM.

</details>

### Knowledge-Driven Self-Supervised Representation Learning for Facial Action Unit Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52688.2022.01977) · 📚 被引 41
- **作者**: Yanan Chang, Shangfei Wang
- **🏷️ 机构**: University of Science and Technology of China,Hefei,Anhui,China
- **会议**: CVPR 2022

### SPAct: Self-supervised Privacy Preservation for Action Recognition.
- **链接**: [arXiv:2203.15205](https://arxiv.org/abs/2203.15205) · [代码](https://github.com/DAVEISHAN/SPAct) · 📚 被引 66
- **作者**: Ishan Rajendrakumar Dave, Chen Chen, Mubarak Shah
- **🏷️ 机构**: Center for Research in Computer Vision, University of Central Florida,Orlando,USA
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual private information leakage is an emerging key issue for the fast growing applications of video understanding like activity recognition. Existing approaches for mitigating privacy leakage in action recognition require privacy labels along with the action labels from the video dataset. However, annotating frames of video dataset for privacy labels is not feasible. Recent developments of self-supervised learning (SSL) have unleashed the untapped potential of the unlabeled data. For the first time, we present a novel training framework which removes privacy information from input video in a self-supervised manner without requiring privacy labels. Our training framework consists of three main components: anonymization function, self-supervised privacy removal branch, and action recognition branch. We train our framework using a minimax optimization strategy to minimize the action recognition cost function and maximize the privacy cost function through a contrastive self-supervised loss. Employing existing protocols of known-action and privacy attributes, our framework achieves a competitive action-privacy trade-off to the existing state-of-the-art supervised methods. In addition, we introduce a new protocol to evaluate the generalization of learned the anonymization function to novel-action and privacy attributes and show that our self-supervised framework outperforms existing supervised methods. Code available at: https://github.com/DAVEISHAN/SPAct

</details>

### Incremental Cross-view Mutual Distillation for Self-supervised Medical CT Synthesis.
- **链接**: [arXiv:2112.10325](https://arxiv.org/abs/2112.10325) · 📚 被引 26
- **作者**: Chaowei Fang, Liang Wang, Dingwen Zhang, Jun Xu, Yixuan Yuan, Junwei Han
- **🏷️ 机构**: Xidian University, Northwestern Polytechnical University, Nankai University
- **会议**: CVPR 2022

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Due to the constraints of the imaging device and high cost in operation time, computer tomography (CT) scans are usually acquired with low intra-slice resolution. Improving the intra-slice resolution is beneficial to the disease diagnosis for both human experts and computer-aided systems. To this end, this paper builds a novel medical slice synthesis to increase the between-slice resolution. Considering that the ground-truth intermediate medical slices are always absent in clinical practice, we introduce the incremental cross-view mutual distillation strategy to accomplish this task in the self-supervised learning manner. Specifically, we model this problem from three different views: slice-wise interpolation from axial view and pixel-wise interpolation from coronal and sagittal views. Under this circumstance, the models learned from different views can distill valuable knowledge to guide the learning processes of each other. We can repeat this process to make the models synthesize intermediate slice data with increasing inter-slice resolution. To demonstrate the effectiveness of the proposed approach, we conduct comprehensive experiments on a large-scale CT dataset. Quantitative and qualitative comparison results show that our method outperforms state-of-the-art algorithms by clear margins.

</details>

## 跨领域论文（完整笔记在其他领域）

- Self-supervised object detection from audio-visual correspondence. → [multimodal](../multimodal/Guideline%202022.md)
- Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data. → [autonomous-driving](../autonomous-driving/Guideline%202022.md)
- CrossPoint: Self-Supervised Cross-Modal Contrastive Learning for 3D Point Cloud Understanding. → [multimodal](../multimodal/Guideline%202022.md)
- Fire Together Wire Together: A Dynamic Pruning Approach with Self-Supervised Mask Prediction. → [network-pruning](../network-pruning/Guideline%202022.md)
