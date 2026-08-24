# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 23 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Learning to Generate Text-Grounded Mask for Open-World Semantic Segmentation from Only Image-Text Pairs.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01074) · 📚 被引 98
- **作者**: Junbum Cha, Jonghwan Mun, Byungseok Roh
- **🏷️ 机构**: Kakao Brain
- **会议**: CVPR 2023

### Accelerating Vision-Language Pretraining with Free Language Modeling.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.02218) · 📚 被引 8
- **作者**: Teng Wang, Yixiao Ge, Feng Zheng, Ran Cheng, Ying Shan, Xiaohu Qie et al.
- **🏷️ 机构**: Southern University of Science and Technology, ARC Lab, Tencent PCG
- **会议**: CVPR 2023

### Q: How to Specialize Large Vision-Language Models to Data-Scarce VQA Tasks? A: Self-Train on Unlabeled Images!
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01441) · 📚 被引 13
- **作者**: Zaid Khan, B. G. Vijay Kumar, Samuel Schulter, Xiang Yu, Yun Fu, Manmohan Chandraker
- **🏷️ 机构**: Northeastern University, NEC Labs America, Amazon
- **会议**: CVPR 2023

### Task Residual for Tuning Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01049) · 📚 被引 117
- **作者**: Tao Yu, Zhihe Lu, Xin Jin, Zhibo Chen, Xinchao Wang
- **🏷️ 机构**: National University of Singapore, University of Science and Technology of China
- **会议**: CVPR 2023

### Adaptive Zone-aware Hierarchical Planner for Vision-Language Navigation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01432) · 📚 被引 37
- **作者**: Chen Gao, Xingyu Peng, Mi Yan, He Wang, Lirong Yang, Haibing Ren et al.
- **🏷️ 机构**: CUHK
- **会议**: CVPR 2023

### FAME-ViL: Multi-Tasking Vision-Language Model for Heterogeneous Fashion Tasks.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00262) · 📚 被引 50
- **作者**: Xiao Han, Xiatian Zhu, Licheng Yu, Li Zhang, Yi-Zhe Song, Tao Xiang
- **🏷️ 机构**: University of Surrey,CVSSP, Fudan University
- **会议**: CVPR 2023

### VILA: Learning Image Aesthetics from User Comments with Vision-Language Pretraining.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00968) · 📚 被引 83
- **作者**: Junjie Ke, Keren Ye, Jiahui Yu, Yonghui Wu, Peyman Milanfar, Feng Yang
- **🏷️ 机构**: Google Research
- **会议**: CVPR 2023

### CrowdCLIP: Unsupervised Crowd Counting via Vision-Language Model.
- **链接**: [arXiv:2304.04231](https://arxiv.org/abs/2304.04231) · [出版页](https://doi.org/10.1109/CVPR52729.2023.00283) · [代码](https://github.com/dk-liang/CrowdCLIP) · 📚 被引 89
- **作者**: Dingkang Liang, Jiahao Xie, Zhikang Zou, Xiaoqing Ye, Wei Xu, Xiang Bai
- **🏷️ 机构**: HUAST
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Supervised crowd counting relies heavily on costly manual labeling, which is difficult and expensive, especially in dense scenes. To alleviate the problem, we propose a novel unsupervised framework for crowd counting, named CrowdCLIP. The core idea is built on two observations: 1) the recent contrastive pre-trained vision-language model (CLIP) has presented impressive performance on various downstream tasks; 2) there is a natural mapping between crowd patches and count text. To the best of our knowledge, CrowdCLIP is the first to investigate the vision language knowledge to solve the counting problem. Specifically, in the training stage, we exploit the multi-modal ranking loss by constructing ranking text prompts to match the size-sorted crowd patches to guide the image encoder learning. In the testing stage, to deal with the diversity of image patches, we propose a simple yet effective progressive filtering strategy to first select the highly potential crowd patches and then map them into the language space with various counting intervals. Extensive experiments on five challenging datasets demonstrate that the proposed CrowdCLIP achieves superior performance compared to previous unsupervised state-of-the-art counting methods. Notably, CrowdCLIP even surpasses some popular fully-supervised methods under the cross-dataset setting. The source code will be available at https://github.com/dk-liang/CrowdCLIP.

### @ CREPE: Can Vision-Language Foundation Models Reason Compositionally?
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01050) · 📚 被引 73
- **作者**: Zixian Ma, Jerry Hong, Mustafa Omer Gul, Mona Gandhi, Irena Gao, Ranjay Krishna
- **🏷️ 机构**: Stanford University, Cornell University, University of Pennsylvania
- **会议**: CVPR 2023

### HOICLIP: Efficient Knowledge Transfer for HOI Detection with Vision-Language Models.
- **链接**: [arXiv:2303.15786](https://arxiv.org/abs/2303.15786) · [出版页](https://doi.org/10.1109/CVPR52729.2023.02251) · [代码](https://github.com/Artanic30/HOICLIP) · 📚 被引 91
- **作者**: Shan Ning, Longtian Qiu, Yongfei Liu, Xuming He
- **🏷️ 机构**: ShanghaiTech University,Shanghai,China, ByteDance Inc.
- **会议**: CVPR 2023

- **摘要（英，原文）**:

  > Human-Object Interaction (HOI) detection aims to localize human-object pairs and recognize their interactions. Recently, Contrastive Language-Image Pre-training (CLIP) has shown great potential in providing interaction prior for HOI detectors via knowledge distillation. However, such approaches often rely on large-scale training data and suffer from inferior performance under few/zero-shot scenarios. In this paper, we propose a novel HOI detection framework that efficiently extracts prior knowledge from CLIP and achieves better generalization. In detail, we first introduce a novel interaction decoder to extract informative regions in the visual feature map of CLIP via a cross-attention mechanism, which is then fused with the detection backbone by a knowledge integration block for more accurate human-object pair detection. In addition, prior knowledge in CLIP text encoder is leveraged to generate a classifier by embedding HOI descriptions. To distinguish fine-grained interactions, we build a verb classifier from training data via visual semantic arithmetic and a lightweight verb representation adapter. Furthermore, we propose a training-free enhancement to exploit global HOI predictions from CLIP. Extensive experiments demonstrate that our method outperforms the state of the art by a large margin on various settings, e.g. +4.04 mAP on HICO-Det. The source code is available in https://github.com/Artanic30/HOICLIP.

### DeAR: Debiasing Vision-Language Models with Additive Residuals.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00659) · 📚 被引 34
- **作者**: Ashish Seth, Mayur Hemani, Chirag Agarwal
- **🏷️ 机构**: IIT Madras,India, Adobe Inc.
- **会议**: CVPR 2023

### You Need Multiple Exiting: Dynamic Early Exiting for Accelerating Unified Vision Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01038) · 📚 被引 31
- **作者**: Shengkun Tang, Yaqing Wang, Zhenglun Kong, Tianchi Zhang, Yao Li, Caiwen Ding et al.
- **🏷️ 机构**: North Carolina State University,Raleigh,USA, Google Research,New York,USA, Northeastern University,Boston,USA
- **会议**: CVPR 2023

### Improving Commonsense in Vision-Language Models via Knowledge Graph Riddles.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00259) · 📚 被引 7
- **作者**: Shuquan Ye, Yujia Xie, Dongdong Chen, Yichong Xu, Lu Yuan, Chenguang Zhu et al.
- **🏷️ 机构**: City University of Hong Kong, Microsoft
- **会议**: CVPR 2023

### Meta-Personalizing Vision-Language Models to Find Named Instances in Video.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01833) · 📚 被引 13
- **作者**: Chun-Hsiao Yeh, Bryan C. Russell, Josef Sivic, Fabian Caba Heilbron, Simon Jenni
- **🏷️ 机构**: University of California,Berkeley, Adobe Research, Czech Institute of Informatics, Robotics and Cybernetics at the Czech Technical University in Prague (CIIRC CTU)
- **会议**: CVPR 2023

### GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01054) · 📚 被引 13
- **作者**: Da Yin, Feng Gao, Govind Thattai, Michael Johnston, Kai-Wei Chang
- **🏷️ 机构**: University of California,Los Angeles, Amazon Alexa AI
- **会议**: CVPR 2023

### IFSeg: Image-free Semantic Segmentation via Vision-Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.00290) · 📚 被引 17
- **作者**: Sukmin Yun, Seong Hyeon Park, Paul Hongsuck Seo, Jinwoo Shin
- **🏷️ 机构**: Korea Advanced Institute of Science and Technology (KAIST), Google Research
- **会议**: CVPR 2023

### MaskCLIP: Masked Self-Distillation Advances Contrastive Language-Image Pretraining.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01058) · 📚 被引 162
- **作者**: Xiaoyi Dong, Jianmin Bao, Yinglin Zheng, Ting Zhang, Dongdong Chen, Hao Yang et al.
- **🏷️ 机构**: University of Science and Technology of China, Microsoft Research Asia, Xiamen University
- **会议**: CVPR 2023

### Local 3D Editing via 3D Distillation of CLIP Knowledge.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52729.2023.01219) · 📚 被引 20
- **作者**: Junha Hyung, Sungwon Hwang, Daejin Kim, Hyunji Lee, Jaegul Choo
- **🏷️ 机构**: KAIST AI, Scatter Lab
- **会议**: CVPR 2023

## 跨领域论文（完整笔记在其他领域）

- CLIP the Gap: A Single Domain Generalization Approach for Object Detection. → [object-detection](../object-detection/Guideline%202023.md)
- Open-Vocabulary Semantic Segmentation with Mask-adapted CLIP. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models. → [multimodal](../multimodal/Guideline%202023.md)
- Vita-CLIP: Video and text adaptive CLIP via Multimodal Prompting. → [multimodal](../multimodal/Guideline%202023.md)
