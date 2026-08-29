# Object Detection — 2025 Guideline

> 领域: 通用 2D 目标检测（检测器架构、密集预测、小物体/旋转框/NMS 等）
> 论文数: 24 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### DON'T NEED RETRAINING: A Mixture of DETR and Vision Foundation Models for Cross-Domain Few-Shot Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d77402f07113388562f5b51eaee89573-Abstract-Conference.html) · 📚 被引 0
- **作者**: Changhan Liu, Xunzhi Xiang, Zixuan Duan, Wenbin Li, Qi Fan, Yang Gao
- **🏷️ 机构**: Nanjing university, NJU, Nanjing University
- **会议**: NeurIPS 2025

### Roboflow100-VL: A Multi-Domain Object Detection Benchmark for Vision-Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/1013f8ff40a194f3f12a6bcc5221bb34-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Matvei Popov, Peter Robicheaux, Anish Madan, Isaac Robinson, Joseph Nelson, Deva Ramanan et al.
- **🏷️ 机构**: CMU
- **会议**: NeurIPS 2025

### CQ-DINO: Mitigating Gradient Dilution via Category Queries for Vast Vocabulary Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/21168020249eccddcc1736ec79bd096f-Abstract-Conference.html)
- **作者**: Zhichao Sun, Huazhang Hu, Yidong Ma, Gang Liu, Yibo Chen, Xu Tang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### CSPCL: Category Semantic Prior Contrastive Learning for Deformable DETR-Based Prohibited Item Detectors.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/cfbce54e59addd97bf555fc31be7e4ec-Abstract-Conference.html)
- **作者**: Mingyuan Li, Tong Jia, Hao Wang, Bowen Ma, Hui Lu, Shiyi Guo et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### GUIDED: Granular Understanding via Identification, Detection, and Discrimination for Fine-Grained Open-Vocabulary Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/3b00f67a2e03916b26f56b66b38445f7-Abstract-Conference.html)
- **作者**: Jiaming Li, Zhijia Liang, Weikai Chen, Lin Ma, Guanbin Li
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### DitHub: A Modular Framework for Incremental Open-Vocabulary Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/211bc037aefd17aec8e3e48a47cfa007-Abstract-Conference.html)
- **作者**: Chiara Cappellino, Gianluca Mancusi, Matteo Mosconi, Angelo Porrello, Simone Calderara, Rita Cucchiara
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### ELDET: Early-Learning Distillation with Noisy Labels for Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6460e378f24da3a79f20ac2640732a00-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dongmin Choi, Sangbin Lee, EungGu Yun, Jonghyuk Baek, Frank C. Park
- **🏷️ 机构**: SAIGE, Flitto, Seoul National University
- **会议**: NeurIPS 2025

### Test-Time Adaptive Object Detection with Foundation Model.
- **链接**: [arXiv:2510.25175](https://arxiv.org/abs/2510.25175) · [代码](https://github.com/gaoyingjay/ttaod_foundation) · 📚 被引 0
- **作者**: Yingjie Gao, Yanan Zhang, Zhi Cai, Di Huang
- **🏷️ 机构**: Beihang University, Hefei University of Technology, Beijing University of Aeronautics and Astronautics
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In recent years, test-time adaptive object detection has attracted increasing attention due to its unique advantages in online domain adaptation, which aligns more closely with real-world application scenarios. However, existing approaches heavily rely on source-derived statistical characteristics while making the strong assumption that the source and target domains share an identical category space. In this paper, we propose the first foundation model-powered test-time adaptive object detection method that eliminates the need for source data entirely and overcomes traditional closed-set limitations. Specifically, we design a Multi-modal Prompt-based Mean-Teacher framework for vision-language detector-driven test-time adaptation, which incorporates text and visual prompt tuning to adapt both language and vision representation spaces on the test data in a parameter-efficient manner. Correspondingly, we propose a Test-time Warm-start strategy tailored for the visual prompts to effectively preserve the representation capability of the vision branch. Furthermore, to guarantee high-quality pseudo-labels in every test batch, we maintain an Instance Dynamic Memory (IDM) module that stores high-quality pseudo-labels from previous test samples, and propose two novel strategies-Memory Enhancement and Memory Hallucination-to leverage IDM's high-quality instances for enhancing original predictions and hallucinating images without available pseudo-labels, respectively. Extensive experiments on cross-corruption and cross-dataset benchmarks demonstrate that our method consistently outperforms previous state-of-the-art methods, and can adapt to arbitrary cross-domain and cross-category target data. Code is available at https://github.com/gaoyingjay/ttaod_foundation.

</details>

### Neptune-X: Active X-to-Maritime Generation for Universal Maritime Object Detection.
- **链接**: [arXiv:2509.20745](https://arxiv.org/abs/2509.20745) · [代码](https://github.com/gy65896/Neptune-X) · 📚 被引 0
- **作者**: Yu Guo, Shengfeng He, Yuxu Lu, Haonan An, Yihang Tao, Huilin Zhu et al.
- **🏷️ 机构**: City University of Hong Kong, Singapore Management University, Hong Kong Polytechnic University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Maritime object detection is essential for navigation safety, surveillance, and autonomous operations, yet constrained by two key challenges: the scarcity of annotated maritime data and poor generalization across various maritime attributes (e.g., object category, viewpoint, location, and imaging environment). To address these challenges, we propose Neptune-X, a data-centric generative-selection framework that enhances training effectiveness by leveraging synthetic data generation with task-aware sample selection. From the generation perspective, we develop X-to-Maritime, a multi-modality-conditioned generative model that synthesizes diverse and realistic maritime scenes. A key component is the Bidirectional Object-Water Attention module, which captures boundary interactions between objects and their aquatic surroundings to improve visual fidelity. To further improve downstream tasking performance, we propose Attribute-correlated Active Sampling, which dynamically selects synthetic samples based on their task relevance. To support robust benchmarking, we construct the Maritime Generation Dataset, the first dataset tailored for generative maritime learning, encompassing a wide range of semantic conditions. Extensive experiments demonstrate that our approach sets a new benchmark in maritime scene synthesis, significantly improving detection accuracy, particularly in challenging and previously underrepresented settings. The code is available at https://github.com/gy65896/Neptune-X.

</details>

### Real-Time Scene-Adaptive Tone Mapping for High-Dynamic Range Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/8c83381162f247df48f101b3aaa7c440-Abstract-Conference.html) · 📚 被引 0
- **作者**: Gongzhe Li, Linwei Qiu, Peibei Cao, Fengying Xie, Xiangyang Ji, Qilin Sun
- **🏷️ 机构**: The Chinese University of Hong Kong, Shenzhen, Beihang University, Nanjing University of Information Science and Technology
- **会议**: NeurIPS 2025

### Domain-RAG: Retrieval-Guided Compositional Image Generation for Cross-Domain Few-Shot Object Detection.
- **链接**: [arXiv:2506.05872](https://arxiv.org/abs/2506.05872) · 📚 被引 0
- **作者**: Yu Li, Xingyu Qiu, Yuqian Fu, Jie Chen, Tianwen Qian, Xu Zheng et al.
- **🏷️ 机构**: Peking University, Fudan University, Institute of automation, Chinese academy of science, Chinese Academy of Sciences
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Cross-Domain Few-Shot Object Detection (CD-FSOD) aims to detect novel objects with only a handful of labeled samples from previously unseen domains. While data augmentation and generative methods have shown promise in few-shot learning, their effectiveness for CD-FSOD remains unclear due to the need for both visual realism and domain alignment. Existing strategies, such as copy-paste augmentation and text-to-image generation, often fail to preserve the correct object category or produce backgrounds coherent with the target domain, making them non-trivial to apply directly to CD-FSOD. To address these challenges, we propose Domain-RAG, a training-free, retrieval-guided compositional image generation framework tailored for CD-FSOD. Domain-RAG consists of three stages: domain-aware background retrieval, domain-guided background generation, and foreground-background composition. Specifically, the input image is first decomposed into foreground and background regions. We then retrieve semantically and stylistically similar images to guide a generative model in synthesizing a new background, conditioned on both the original and retrieved contexts. Finally, the preserved foreground is composed with the newly generated domain-aligned background to form the generated image. Without requiring any additional supervision or training, Domain-RAG produces high-quality, domain-consistent samples across diverse tasks, including CD-FSOD, remote sensing FSOD, and camouflaged FSOD. Extensive experiments show consistent improvements over strong baselines and establish new state-of-the-art results. Codes will be released upon acceptance.

</details>

### Towards Single-Source Domain Generalized Object Detection via Causal Visual Prompts.
- **链接**: [arXiv:2510.19487](https://arxiv.org/abs/2510.19487) · 📚 被引 0
- **作者**: Chen Li, Huiying Xu, Changxin Gao, Zeyu Wang, Yun Liu, Xinzhong Zhu
- **🏷️ 机构**: Tencent, Zhejiang Normal University, Huazhong University of Science and Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Single-source Domain Generalized Object Detection (SDGOD), as a cutting-edge research topic in computer vision, aims to enhance model generalization capability in unseen target domains through single-source domain training. Current mainstream approaches attempt to mitigate domain discrepancies via data augmentation techniques. However, due to domain shift and limited domain-specific knowledge, models tend to fall into the pitfall of spurious correlations. This manifests as the model's over-reliance on simplistic classification features (e.g., color) rather than essential domain-invariant representations like object contours. To address this critical challenge, we propose the Cauvis (Causal Visual Prompts) method. First, we introduce a Cross-Attention Prompts module that mitigates bias from spurious features by integrating visual prompts with cross-attention. To address the inadequate domain knowledge coverage and spurious feature entanglement in visual prompts for single-domain generalization, we propose a dual-branch adapter that disentangles causal-spurious features while achieving domain adaptation via high-frequency feature extraction. Cauvis achieves state-of-the-art performance with 15.9-31.4% gains over existing domain generalization methods on SDGOD datasets, while exhibiting significant robustness advantages in complex interference environments.

</details>

### VoxDet: Rethinking 3D Semantic Scene Completion as Dense Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/7478016a59b9851ff6685a3fdd0f6b2e-Abstract-Conference.html) · 📚 被引 0
- **作者**: Wuyang Li, Zhu Yu, Alexandre Alahi
- **🏷️ 机构**: EPFL - EPF Lausanne, Zhejiang University, EPFL
- **会议**: NeurIPS 2025

### VL-SAM-V2: Open-World Object Detection with General and Specific Query Fusion.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/c3532dd633e600e9f6db57aa7ae0c858-Abstract-Conference.html)
- **作者**: Zhiwei Lin, Yongtao Wang
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### FlexEvent: Towards Flexible Event-Frame Object Detection at Varying Operational Frequencies.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/8064e4ebbcbe594628887b420956d8c3-Abstract-Conference.html) · 📚 被引 0
- **作者**: Dongyue Lu, Lingdong Kong, Gim Hee Lee, Camille Simon Chane, Wei Tsang Ooi
- **🏷️ 机构**: National University of Singapore, Ecole Nationale Supérieure de l'Electronique et de ses Applications
- **会议**: NeurIPS 2025

### Looking Beyond the Known: Towards a Data Discovery Guided Open-World Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/238597630b574e65fffb533444cf7d00-Abstract-Conference.html)
- **作者**: Anay Majee, Amitesh Gangrade, Rishabh Iyer
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### End-to-End Low-Light Enhancement for Object Detection with Learned Metadata from RAWs.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/417f92ffb65cc4b8e8805b9be2fdbd9f-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xuelin Shen, Haifeng Jiao, Yitong Wang, Yulin He, Wenhan Yang
- **🏷️ 机构**: GUANGMING Laboratory, Shenzhen University, ByteDance Inc
- **会议**: NeurIPS 2025

### Delving into Cascaded Instability: A Lipschitz Continuity View on Image Restoration and Object Detection Synergy.
- **链接**: [arXiv:2510.24232](https://arxiv.org/abs/2510.24232) · 📚 被引 0
- **作者**: Qing Zhao, Weijian Deng, Pengxu Wei, ZiYi Dong, Hannan Lu, Xiangyang Ji et al.
- **🏷️ 机构**: Sun Yat-sen University, Australian National University, SUN YAT-SEN UNIVERSITY
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> To improve detection robustness in adverse conditions (e.g., haze and low light), image restoration is commonly applied as a pre-processing step to enhance image quality for the detector. However, the functional mismatch between restoration and detection networks can introduce instability and hinder effective integration -- an issue that remains underexplored. We revisit this limitation through the lens of Lipschitz continuity, analyzing the functional differences between restoration and detection networks in both the input space and the parameter space. Our analysis shows that restoration networks perform smooth, continuous transformations, while object detectors operate with discontinuous decision boundaries, making them highly sensitive to minor perturbations. This mismatch introduces instability in traditional cascade frameworks, where even imperceptible noise from restoration is amplified during detection, disrupting gradient flow and hindering optimization. To address this, we propose Lipschitz-regularized object detection (LROD), a simple yet effective framework that integrates image restoration directly into the detector's feature learning, harmonizing the Lipschitz continuity of both tasks during training. We implement this framework as Lipschitz-regularized YOLO (LR-YOLO), extending seamlessly to existing YOLO detectors. Extensive experiments on haze and low-light benchmarks demonstrate that LR-YOLO consistently improves detection stability, optimization smoothness, and overall accuracy.

</details>

### Rethinking Scale-Aware Temporal Encoding for Event-based Object Detection.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d450dceeacd6083d1d550247377f2320-Abstract-Conference.html) · 📚 被引 1
- **作者**: Lin Zhu, Tengyu Long, Xiao Wang, Lizhi Wang, Hua Huang
- **🏷️ 机构**: Beijing Normal University, Beijing Institute of Technology, Beihang University
- **会议**: NeurIPS 2025

### ReCon: Region-Controllable Data Augmentation with Rectification and Alignment for Object Detection.
- **链接**: [arXiv:2510.15783](https://arxiv.org/abs/2510.15783) · [代码](https://github.com/haoweiz23/ReCon) · 📚 被引 0
- **作者**: Haowei Zhu, Tianxiang Pan, Rui Qin, Jun-Hai Yong, Bin Wang
- **🏷️ 机构**: Tsinghua University, Tsinghua University, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The scale and quality of datasets are crucial for training robust perception models. However, obtaining large-scale annotated data is both costly and time-consuming. Generative models have emerged as a powerful tool for data augmentation by synthesizing samples that adhere to desired distributions. However, current generative approaches often rely on complex post-processing or extensive fine-tuning on massive datasets to achieve satisfactory results, and they remain prone to content-position mismatches and semantic leakage. To overcome these limitations, we introduce ReCon, a novel augmentation framework that enhances the capacity of structure-controllable generative models for object detection. ReCon integrates region-guided rectification into the diffusion sampling process, using feedback from a pre-trained perception model to rectify misgenerated regions within diffusion sampling process. We further propose region-aligned cross-attention to enforce spatial-semantic alignment between image regions and their textual cues, thereby improving both semantic consistency and overall image fidelity. Extensive experiments demonstrate that ReCon substantially improve the quality and trainability of generated data, achieving consistent performance gains across various datasets, backbone architectures, and data scales. Our code is available at https://github.com/haoweiz23/ReCon .

</details>

## 跨领域论文（完整笔记在其他领域）

- OpenAD: Open-World Autonomous Driving Benchmark for 3D Object Detection. → [3d-detection](../3d-detection/Guideline%202025.md)
- T-norm Selection for Object Detection in Autonomous Driving with Logical Constraints. → [autonomous-driving](../autonomous-driving/Guideline%202025.md)
- Rooms from Motion: Un-posed Indoor 3D Object Detection as Localization and Mapping. → [3d-detection](../3d-detection/Guideline%202025.md)
- Multimodal Causal Reasoning for UAV Object Detection. → [multimodal](../multimodal/Guideline%202025.md)
