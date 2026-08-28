# Open-set Detection — 2023 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 9 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Contrastive Feature Masking Open-Vocabulary Vision Transformer.
- **链接**: [arXiv:2309.00775](https://arxiv.org/abs/2309.00775) · 📚 被引 22
- **作者**: Dahun Kim, Anelia Angelova, Weicheng Kuo
- **🏷️ 机构**: Google DeepMind
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present Contrastive Feature Masking Vision Transformer (CFM-ViT) - an image-text pretraining methodology that achieves simultaneous learning of image- and region-level representation for open-vocabulary object detection (OVD). Our approach combines the masked autoencoder (MAE) objective into the contrastive learning objective to improve the representation for localization tasks. Unlike standard MAE, we perform reconstruction in the joint image-text embedding space, rather than the pixel space as is customary with the classical MAE method, which causes the model to better learn region-level semantics. Moreover, we introduce Positional Embedding Dropout (PED) to address scale variation between image-text pretraining and detection finetuning by randomly dropping out the positional embeddings during pretraining. PED improves detection performance and enables the use of a frozen ViT backbone as a region classifier, preventing the forgetting of open-vocabulary knowledge during detection finetuning. On LVIS open-vocabulary detection benchmark, CFM-ViT achieves a state-of-the-art 33.9 AP$r$, surpassing the best approach by 7.6 points and achieves better zero-shot detection transfer. Finally, CFM-ViT acquires strong image-level representation, outperforming the state of the art on 8 out of 12 metrics on zero-shot image-text retrieval benchmarks.

</details>

### SOAR: Scene-debiasing Open-set Action Recognition.
- **链接**: [arXiv:2309.01265](https://arxiv.org/abs/2309.01265) · 📚 被引 12
- **作者**: Yuanhao Zhai, Ziyi Liu, Zhenyu Wu, Yi Wu, Chunluan Zhou, David S. Doermann et al.
- **🏷️ 机构**: University at Buffalo, Wormpex AI Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Deep learning models have a risk of utilizing spurious clues to make predictions, such as recognizing actions based on the background scene. This issue can severely degrade the open-set action recognition performance when the testing samples have different scene distributions from the training samples. To mitigate this problem, we propose a novel method, called Scene-debiasing Open-set Action Recognition (SOAR), which features an adversarial scene reconstruction module and an adaptive adversarial scene classification module. The former prevents the decoder from reconstructing the video background given video features, and thus helps reduce the background information in feature learning. The latter aims to confuse scene type classification given video features, with a specific emphasis on the action foreground, and helps to learn scene-invariant information. In addition, we design an experiment to quantify the scene bias. The results indicate that the current open-set action recognizers are biased toward the scene, and our proposed SOAR method better mitigates such bias. Furthermore, our extensive experiments demonstrate that our method outperforms state-of-the-art methods, and the ablation studies confirm the effectiveness of our proposed modules.

</details>

### Exploring Open-Vocabulary Semantic Segmentation from CLIP Vision Encoder Distillation Only.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00071)
- **作者**: Jun Chen, Deyao Zhu, Guocheng Qian, Bernard Ghanem, Zhicheng Yan, Chenchen Zhu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

### Class-relation Knowledge Distillation for Novel Class Discovery.
- **链接**: [arXiv:2307.09158](https://arxiv.org/abs/2307.09158) · [代码](https://github.com/kleinzcy/Cr-KD-NCD) · 📚 被引 24
- **作者**: Peiyan Gu, Chuyu Zhang, Ruijie Xu, Xuming He
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China
- **会议**: ICCV 2023

### BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects.
- **链接**: [arXiv:2303.14158](https://arxiv.org/abs/2303.14158) · 📚 被引 155
- **作者**: Bowen Wen, Jonathan Tremblay, Valts Blukis, Stephen Tyree, Thomas Müller, Alex Evans et al.
- **🏷️ 机构**: NVIDIA
- **会议**: CVPR 2023

> We tackle the problem of novel class discovery, which aims to learn novel classes without supervision based on labeled data from known classes. A key challenge lies in transferring the knowledge in the known-class data to the learning of novel classes. Previous methods mainly focus on building a shared representation space for knowledge transfer and often ignore modeling class relations. To address this, we introduce a class relation representation for the novel classes based on the predicted class distribution of a model trained on known classes. Empirically, we find that such class relation becomes less informative during typical discovery training. To prevent such information loss, we propose a novel knowledge distillation framework, which utilizes our class-relation representation to regularize the learning of novel classes. In addition, to enable a flexible knowledge distillation scheme for each data point in novel classes, we develop a learnable weighting function for the regularization, which adaptively promotes knowledge transfer based on the semantic similarity between the novel and known classes. To validate the effectiveness and generalization of our method, we conduct extensive experiments on multiple benchmarks, including CIFAR100, Stanford Cars, CUB, and FGVC-Aircraft datasets. Our results demonstrate that the proposed method outperforms the previous state-of-the-art methods by a significant margin on almost all benchmarks. Code is available at \href{https://github.com/kleinzcy/Cr-KD-NCD}{here}.

### Open-vocabulary Attribute Detection.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00680)
- **作者**: María Alejandra Bravo, Sudhanshu Mittal, Simon Ging, Thomas Brox
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### OvarNet: Towards Open-Vocabulary Object Attribute Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02252) · 📚 被引 47
- **作者**: Keyan Chen, Xiaolong Jiang, Yao Hu, Xu Tang, Yan Gao, Jianqi Chen et al.
- **🏷️ 机构**: Beihang University, Xiaohongshu Inc, Shanghai Jiao Tong University,CMIC
- **会议**: CVPR 2023

### PLA: Language-Driven Open-Vocabulary 3D Scene Understanding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00677) · 📚 被引 134
- **作者**: Runyu Ding, Jihan Yang, Chuhui Xue, Wenqing Zhang, Song Bai, Xiaojuan Qi
- **🏷️ 机构**: The University of Hong Kong, ByteDance
- **会议**: CVPR 2023

### Open-Vocabulary Semantic Segmentation with Mask-adapted CLIP.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00682)
- **作者**: Feng Liang, Bichen Wu, Xiaoliang Dai, Kunpeng Li, Yinan Zhao, Hang Zhang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Being Comes from Not-Being: Open-Vocabulary Text-to-Motion Generation with Wordless Training.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02224) · 📚 被引 36
- **作者**: Junfan Lin, Jianlong Chang, Lingbo Liu, Guanbin Li, Liang Lin, Qi Tian et al.
- **🏷️ 机构**: Sun Yat-sen University, Huawei Cloud, The Hong Kong Polytechnic University
- **会议**: CVPR 2023

### Open Vocabulary Semantic Segmentation with Patch Aligned Contrastive Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01860)
- **作者**: Jishnu Mukhoti, Tsung-Yu Lin, Omid Poursaeed, Rui Wang, Ashish Shah, Philip H. S. Torr et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### FreeSeg: Unified, Universal and Open-Vocabulary Image Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01863) · 📚 被引 93
- **作者**: Jie Qin, Jie Wu, Pengxiang Yan, Ming Li, Yuxi Ren, Xuefeng Xiao et al.
- **🏷️ 机构**: Institute of Automation,Chinese Academy of Sciences, ByteDance Inc
- **会议**: CVPR 2023

### Mask-Free OVIS: Open-Vocabulary Instance Segmentation without Manual Mask Annotations.
- **链接**: [arXiv:2303.16891](https://arxiv.org/abs/2303.16891) · 📚 被引 15
- **作者**: Vibashan VS, Ning Yu, Chen Xing, Can Qin, Mingfei Gao, Juan Carlos Niebles et al.
- **🏷️ 机构**: Johns Hopkins University, Salesforce Research, Northeastern University
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Existing instance segmentation models learn task-specific information using manual mask annotations from base (training) categories. These mask annotations require tremendous human effort, limiting the scalability to annotate novel (new) categories. To alleviate this problem, Open-Vocabulary (OV) methods leverage large-scale image-caption pairs and vision-language models to learn novel categories. In summary, an OV method learns task-specific information using strong supervision from base annotations and novel category information using weak supervision from image-captions pairs. This difference between strong and weak supervision leads to overfitting on base categories, resulting in poor generalization towards novel categories. In this work, we overcome this issue by learning both base and novel categories from pseudo-mask annotations generated by the vision-language model in a weakly supervised manner using our proposed Mask-free OVIS pipeline. Our method automatically generates pseudo-mask annotations by leveraging the localization ability of a pre-trained vision-language model for objects present in image-caption pairs. The generated pseudo-mask annotations are then used to supervise an instance segmentation model, freeing the entire pipeline from any labour-expensive instance-level annotations and overfitting. Our extensive experiments show that our method trained with just pseudo-masks significantly improves the mAP scores on the MS-COCO dataset and OpenImages dataset compared to the recent state-of-the-art methods trained with manual masks. Codes and models are provided in https://vibashan.github.io/ovis-web/.

</details>

### CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00679)
- **作者**: Xiaoshi Wu, Feng Zhu, Rui Zhao, Hongsheng Li
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2023

### Learning Open-Vocabulary Semantic Segmentation Models From Natural Language Supervision.
- **链接**: [arXiv:2301.09121](https://arxiv.org/abs/2301.09121) · 📚 被引 100
- **作者**: Jilan Xu, Junlin Hou, Yuejie Zhang, Rui Feng, Yi Wang, Yu Qiao et al.
- **🏷️ 机构**: School of Computer Science, Shanghai Collaborative Innovation Center of Intelligent Visual Computing, Fudan University,Shanghai Key Lab of Intelligent Information Processing, Shanghai AI Laboratory
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we consider the problem of open-vocabulary semantic segmentation (OVS), which aims to segment objects of arbitrary classes instead of pre-defined, closed-set categories. The main contributions are as follows: First, we propose a transformer-based model for OVS, termed as OVSegmentor, which only exploits web-crawled image-text pairs for pre-training without using any mask annotations. OVSegmentor assembles the image pixels into a set of learnable group tokens via a slot-attention based binding module, and aligns the group tokens to the corresponding caption embedding. Second, we propose two proxy tasks for training, namely masked entity completion and cross-image mask consistency. The former aims to infer all masked entities in the caption given the group tokens, that enables the model to learn fine-grained alignment between visual groups and text entities. The latter enforces consistent mask predictions between images that contain shared entities, which encourages the model to learn visual invariance. Third, we construct CC4M dataset for pre-training by filtering CC12M with frequently appeared entities, which significantly improves training efficiency. Fourth, we perform zero-shot transfer on three benchmark datasets, PASCAL VOC 2012, PASCAL Context, and COCO Object. Our model achieves superior segmentation results over the state-of-the-art method by using only 3\% data (4M vs 134M) for pre-training. Code and pre-trained models will be released for future research.

</details>

### Open-Vocabulary Panoptic Segmentation with Text-to-Image Diffusion Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00289) · 📚 被引 383
- **作者**: Jiarui Xu, Sifei Liu, Arash Vahdat, Wonmin Byeon, Xiaolong Wang, Shalini De Mello
- **🏷️ 机构**: UC San Diego, NVIDIA
- **会议**: CVPR 2023

### Side Adapter Network for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00288) · 📚 被引 301
- **作者**: Mengde Xu, Zheng Zhang, Fangyun Wei, Han Hu, Xiang Bai
- **🏷️ 机构**: Huazhong University of Science and Technology, Microsoft Research Asia
- **会议**: CVPR 2023

### Open-Set Fine-Grained Retrieval via Prompting Vision-Language Evaluator.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01857) · 📚 被引 26
- **作者**: Shijie Wang, Jianlong Chang, Haojie Li, Zhihui Wang, Wanli Ouyang, Qi Tian
- **🏷️ 机构**: International School of Information Science &#x0026; Engineering, Dalian University of Technology,China, Huawei Cloud &#x0026; AI,China, The University of Sydney,Sense Time Computer Vision Research Group,Australia
- **会议**: CVPR 2023

### Coreset Sampling from Open-Set for Fine-Grained Self-Supervised Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00728)
- **作者**: Sungnyun Kim, Sangmin Bae, Se-Young Yun
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2023

### Enlarging Instance-specific and Class-specific Information for Open-set Action Recognition.
- **链接**: [arXiv:2303.15467](https://arxiv.org/abs/2303.15467) · [代码](https://github.com/Jun-CEN/PSL) · 📚 被引 10
- **作者**: Jun Cen, Shiwei Zhang, Xiang Wang, Yixuan Pei, Zhiwu Qing, Yingya Zhang et al.
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Alibaba Group, Huazhong University of Science and Technology
- **会议**: CVPR 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-set action recognition is to reject unknown human action cases which are out of the distribution of the training set. Existing methods mainly focus on learning better uncertainty scores but dismiss the importance of feature representations. We find that features with richer semantic diversity can significantly improve the open-set performance under the same uncertainty scores. In this paper, we begin with analyzing the feature representation behavior in the open-set action recognition (OSAR) problem based on the information bottleneck (IB) theory, and propose to enlarge the instance-specific (IS) and class-specific (CS) information contained in the feature for better performance. To this end, a novel Prototypical Similarity Learning (PSL) framework is proposed to keep the instance variance within the same class to retain more IS information. Besides, we notice that unknown samples sharing similar appearances to known samples are easily misclassified as known classes. To alleviate this issue, video shuffling is further introduced in our PSL to learn distinct temporal information between original and shuffled samples, which we find enlarges the CS information. Extensive experiments demonstrate that the proposed PSL can significantly boost both the open-set and closed-set performance and achieves state-of-the-art results on multiple benchmarks. Code is available at https://github.com/Jun-CEN/PSL.

</details>

## 跨领域论文（完整笔记在其他领域）

- Distilling DETR with Visual-Linguistic Knowledge for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Novel Scenes & Classes: Towards Adaptive Open-set Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- EdaDet: Open-Vocabulary Object Detection Using Early Dense Alignment. → [object-detection](../object-detection/Guideline%202023.md)
- Open-Vocabulary Object Detection With an Open Corpus. → [object-detection](../object-detection/Guideline%202023.md)
- Identification of Novel Classes for Improving Few-Shot Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
