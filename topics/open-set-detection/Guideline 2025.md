# Open-set Detection — 2025 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 34 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Any3DIS: Class-Agnostic 3D Instance Segmentation by 2D Mask Tracking.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Nguyen_Any3DIS_Class-Agnostic_3D_Instance_Segmentation_by_2D_Mask_Tracking_CVPR_2025_paper.html)
- **作者**: Phuc Nguyen, Minh Luu, Anh Tuan Tran, Cuong Pham, Khoi Nguyen
- **🏷️ 机构**: MovianAI, Qualcomm AI Research, Qualcomm Vietnam Company Limited
- **会议**: CVPR 2025

### Distilling Spectral Graph for Object-Context Aware Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2411.17150](https://arxiv.org/abs/2411.17150) · 📚 被引 7
- **作者**: Chanyoung Kim, Dayun Ju, Woojung Han, Ming-Hsuan Yang, Seong Jae Hwang
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Open-Vocabulary Semantic Segmentation (OVSS) has advanced with recent vision-language models (VLMs), enabling segmentation beyond predefined categories through various learning schemes. Notably, training-free methods offer scalable, easily deployable solutions for handling unseen data, a key goal of OVSS. Yet, a critical issue persists: lack of object-level context consideration when segmenting complex objects in the challenging environment of OVSS based on arbitrary query prompts. This oversight limits models' ability to group semantically consistent elements within object and map them precisely to user-defined arbitrary classes. In this work, we introduce a novel approach that overcomes this limitation by incorporating object-level contextual knowledge within images. Specifically, our model enhances intra-object consistency by distilling spectral-driven features from vision foundation models into the attention mechanism of the visual encoder, enabling semantically coherent components to form a single object mask. Additionally, we refine the text embeddings with zero-shot object presence likelihood to ensure accurate alignment with the specific objects represented in the images. By leveraging object-level contextual knowledge, our proposed approach achieves state-of-the-art performance with strong generalizability across diverse datasets.

### Advancing Generalizable Tumor Segmentation with Anomaly-Aware Open-Vocabulary Attention Maps and Frozen Foundation Diffusion Models.
- **链接**: [arXiv:2505.02753](https://arxiv.org/abs/2505.02753) · [代码](https://github.com/Yankai96/DiffuGTS)
- **作者**: Yankai Jiang, Peng Zhang, Donglin Yang, Yuan Tian, Hai Lin, Xiaosong Wang
- **🏷️ 机构**: Shanghai AI Laboratory, Zhejiang University, The University of British Columbia
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > We explore Generalizable Tumor Segmentation, aiming to train a single model for zero-shot tumor segmentation across diverse anatomical regions. Existing methods face limitations related to segmentation quality, scalability, and the range of applicable imaging modalities. In this paper, we uncover the potential of the internal representations within frozen medical foundation diffusion models as highly efficient zero-shot learners for tumor segmentation by introducing a novel framework named DiffuGTS. DiffuGTS creates anomaly-aware open-vocabulary attention maps based on text prompts to enable generalizable anomaly segmentation without being restricted by a predefined training category list. To further improve and refine anomaly segmentation masks, DiffuGTS leverages the diffusion model, transforming pathological regions into high-quality pseudo-healthy counterparts through latent space inpainting, and applies a novel pixel-level and feature-level residual learning approach, resulting in segmentation masks with significantly enhanced quality and generalization. Comprehensive experiments on four datasets and seven tumor categories demonstrate the superior performance of our method, surpassing current state-of-the-art models across multiple zero-shot settings. Codes are available at https://github.com/Yankai96/DiffuGTS.

### Fine-Grained Image-Text Correspondence with Cost Aggregation for Open-Vocabulary Part Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.html)
- **作者**: Jiho Choi, Seonho Lee, Minhyun Lee, Seungho Lee, Hyunjung Shim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### GROVE: A Generalized Reward for Learning Open-Vocabulary Physical Skill.
- **链接**: [arXiv:2504.04191](https://arxiv.org/abs/2504.04191)
- **作者**: Jieming Cui, Tengyu Liu, Ziyu Meng, Jiale Yu, Ran Song, Wei Zhang et al.
- **🏷️ 机构**: Peking University,Institute for Artificial Intelligence, BIGAI,State Key Laboratory of General Artificial Intelligence, Tsinghua University,Department of Automation
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Learning open-vocabulary physical skills for simulated agents presents a significant challenge in artificial intelligence. Current reinforcement learning approaches face critical limitations: manually designed rewards lack scalability across diverse tasks, while demonstration-based methods struggle to generalize beyond their training distribution. We introduce GROVE, a generalized reward framework that enables open-vocabulary physical skill learning without manual engineering or task-specific demonstrations. Our key insight is that Large Language Models(LLMs) and Vision Language Models(VLMs) provide complementary guidance -- LLMs generate precise physical constraints capturing task requirements, while VLMs evaluate motion semantics and naturalness. Through an iterative design process, VLM-based feedback continuously refines LLM-generated constraints, creating a self-improving reward system. To bridge the domain gap between simulation and natural images, we develop Pose2CLIP, a lightweight mapper that efficiently projects agent poses directly into semantic feature space without computationally expensive rendering. Extensive experiments across diverse embodiments and learning paradigms demonstrate GROVE's effectiveness, achieving 22.2% higher motion naturalness and 25.7% better task completion scores while training 8.4x faster than previous methods. These results establish a new foundation for scalable physical skill acquisition in simulated environments.

### LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models.
- **链接**: [arXiv:2501.18954](https://arxiv.org/abs/2501.18954) · [代码](https://github.com/iSEE-Laboratory/LLMDet)
- **作者**: Shenghao Fu, Qize Yang, Qijie Mo, Junkai Yan, Xihan Wei, Jingke Meng et al.
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China, Alibaba Group,Tongyi Lab
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Recent open-vocabulary detectors achieve promising performance with abundant region-level annotated data. In this work, we show that an open-vocabulary detector co-training with a large language model by generating image-level detailed captions for each image can further improve performance. To achieve the goal, we first collect a dataset, GroundingCap-1M, wherein each image is accompanied by associated grounding labels and an image-level detailed caption. With this dataset, we finetune an open-vocabulary detector with training objectives including a standard grounding loss and a caption generation loss. We take advantage of a large language model to generate both region-level short captions for each region of interest and image-level long captions for the whole image. Under the supervision of the large language model, the resulting detector, LLMDet, outperforms the baseline by a clear margin, enjoying superior open-vocabulary ability. Further, we show that the improved LLMDet can in turn build a stronger large multi-modal model, achieving mutual benefits. The code, model, and dataset is available at https://github.com/iSEE-Laboratory/LLMDet.

### Compositional Caching for Training-free Open-vocabulary Attribute Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Garosi_Compositional_Caching_for_Training-free_Open-vocabulary_Attribute_Detection_CVPR_2025_paper.html)
- **作者**: Marco Garosi, Alessandro Conti, Gaowen Liu, Elisa Ricci, Massimiliano Mancini
- **🏷️ 机构**: University of Trento, Cisco Research
- **会议**: CVPR 2025

### Exploring Simple Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2401.12217](https://arxiv.org/abs/2401.12217)
- **作者**: Zihang Lai
- **🏷️ 机构**: University of Oxford,Visual Geometry Group (VGG)
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation models aim to accurately assign a semantic label to each pixel in an image from a set of arbitrary open-vocabulary texts. In order to learn such pixel-level alignment, current approaches typically rely on a combination of (i) image-level VL model (e.g. CLIP), (ii) ground truth masks, and (iii) custom grouping encoders. In this paper, we introduce S-Seg, a novel model that can achieve surprisingly strong performance without depending on any of the above elements. S-Seg leverages pseudo-mask and language to train a MaskFormer, and can be easily trained from publicly available image-text datasets. Contrary to prior works, our model directly trains for pixel-level features and language alignment. Once trained, S-Seg generalizes well to multiple testing datasets without requiring fine-tuning. In addition, S-Seg has the extra benefits of scalability with data and consistently improvement when augmented with self-training. We believe that our simple yet effective approach will serve as a solid baseline for future research.

### Effective SAM Combination for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2411.14723](https://arxiv.org/abs/2411.14723)
- **作者**: Minhyeok Lee, Suhwan Cho, Jungho Lee, Sunghun Yang, Heeseung Choi, Ig-Jae Kim et al.
- **🏷️ 机构**: Yonsei University, Korea Institute of Science and Technology (KIST)
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Open-vocabulary semantic segmentation aims to assign pixel-level labels to images across an unlimited range of classes. Traditional methods address this by sequentially connecting a powerful mask proposal generator, such as the Segment Anything Model (SAM), with a pre-trained vision-language model like CLIP. But these two-stage approaches often suffer from high computational costs, memory inefficiencies. In this paper, we propose ESC-Net, a novel one-stage open-vocabulary segmentation model that leverages the SAM decoder blocks for class-agnostic segmentation within an efficient inference framework. By embedding pseudo prompts generated from image-text correlations into SAM's promptable segmentation framework, ESC-Net achieves refined spatial aggregation for accurate mask predictions. ESC-Net achieves superior performance on standard benchmarks, including ADE20K, PASCAL-VOC, and PASCAL-Context, outperforming prior methods in both efficiency and accuracy. Comprehensive ablation studies further demonstrate its robustness across challenging conditions.

### Mosaic3D: Foundation Dataset and Model for Open-Vocabulary 3D Segmentation.
- **链接**: [arXiv:2502.02548](https://arxiv.org/abs/2502.02548)
- **作者**: Junha Lee, Chunghyun Park, Jaesung Choe, Yu-Chiang Frank Wang, Jan Kautz, Minsu Cho et al.
- **🏷️ 机构**: NVIDIA, POSTECH
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > We tackle open-vocabulary 3D scene understanding by introducing a novel data generation pipeline and training framework. Our method addresses three critical requirements for effective training: precise 3D region segmentation, comprehensive textual descriptions, and sufficient dataset scale. By leveraging state-of-the-art open-vocabulary image segmentation models and region-aware Vision-Language Models, we develop an automatic pipeline that generates high-quality 3D mask-text pairs. Applying this pipeline to multiple 3D scene datasets, we create Mosaic3D-5.6M, a dataset of over 30K annotated scenes with 5.6M mask-text pairs, significantly larger than existing datasets. Building upon this data, we propose Mosaic3D, a foundation model combining a 3D encoder trained with contrastive learning and a lightweight mask decoder for open-vocabulary 3D semantic and instance segmentation. Our approach achieves state-of-the-art results on open-vocabulary 3D semantic and instance segmentation tasks including ScanNet200, Matterport3D, and ScanNet++, with ablation studies validating the effectiveness of our large-scale training data.

### Mask-Adapter: The Devil is in the Masks for Open-Vocabulary Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.html)
- **作者**: Yongkang Li, Tianheng Cheng, Bin Feng, Wenyu Liu, Xinggang Wang
- **🏷️ 机构**: Huazhong University of Science &amp; Technology,School of EIC
- **会议**: CVPR 2025

### SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.html)
- **作者**: Kaiyu Li, Ruixun Liu, Xiangyong Cao, Xueru Bai, Feng Zhou, Deyu Meng et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering,Xi&#x2019;an,China,710049, Xi&#x2019;an Jiaotong University,School of Computer Science and Technology,Xi&#x2019;an,China,710049, Xidian University
- **会议**: CVPR 2025

### Anomize: Better Open Vocabulary Video Anomaly Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Anomize_Better_Open_Vocabulary_Video_Anomaly_Detection_CVPR_2025_paper.html)
- **作者**: Fei Li, Wenxuan Liu, Jingjing Chen, Ruixu Zhang, Yuran Wang, Xian Zhong et al.
- **🏷️ 机构**: Wuhan University,National Engineering Research Center for Multimedia Software, School of Computer Science, Peking University,State Key Laboratory for Multimedia Information Processing, School of Computer Science, Fudan University,Shanghai Key Lab of Intelligent Information Processing, School of Computer Science
- **会议**: CVPR 2025

### SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html)
- **作者**: Rong Li, Shijie Li, Lingdong Kong, Xulei Yang, Junwei Liang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### SGC-Net: Stratified Granular Comparison Network for Open-Vocabulary HOI Detection.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_SGC-Net_Stratified_Granular_Comparison_Network_for_Open-Vocabulary_HOI_Detection_CVPR_2025_paper.html)
- **作者**: Xin Lin, Chong Shi, Zuopeng Yang, Haojin Tang, Zhili Zhou
- **🏷️ 机构**: Guangzhou University
- **会议**: CVPR 2025

### ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html)
- **作者**: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Parameter-efficient Fine-tuning in Hyperspherical Space for Open-vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.html)
- **作者**: Zelin Peng, Zhengqin Xu, Zhilin Zeng, Yu Huang, Yaoming Wang, Wei Shen
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, AI Institute, Meituan
- **会议**: CVPR 2025

### Understanding Fine-tuning CLIP for Open-vocabulary Semantic Segmentation in Hyperbolic Space.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.html)
- **作者**: Zelin Peng, Zhengqin Xu, Zhilin Zeng, Changsong Wen, Yu Huang, Menglin Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Semantic Library Adaptation: LoRA Retrieval and Fusion for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.html)
- **作者**: Reza Qorbani, Gianluca Villani, Theodoros Panagiotakopoulos, Marc Botet Colomer, Linus Härenstam-Nielsen, Mattia Segù et al.
- **🏷️ 机构**: KTH, The Good AI Lab, Technical University of Munich
- **会议**: CVPR 2025

### GREAT: Geometry-Intention Collaborative Inference for Open-Vocabulary 3D Object Affordance Grounding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Shao_GREAT_Geometry-Intention_Collaborative_Inference_for_Open-Vocabulary_3D_Object_Affordance_Grounding_CVPR_2025_paper.html)
- **作者**: Yawen Shao, Wei Zhai, Yuhang Yang, Hongchen Luo, Yang Cao, Zheng-Jun Zha
- **🏷️ 机构**: University of Science and Technology of China,MoE Key Laboratory of Brain-Inspired Intelligent Perception and Cognition, Northeastern University
- **会议**: CVPR 2025

### LPOSS: Label Propagation Over Patches and Pixels for Open-vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.html)
- **作者**: Vladan Stojnic, Yannis Kalantidis, Jirí Matas, Giorgos Tolias
- **🏷️ 机构**: Czech Technical University in Prague,VRG, FEE, NAVER LABS Europe
- **会议**: CVPR 2025

### Recover and Match: Open-Vocabulary Multi-Label Recognition through Knowledge-Constrained Optimal Transport.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Tan_Recover_and_Match_Open-Vocabulary_Multi-Label_Recognition_through_Knowledge-Constrained_Optimal_Transport_CVPR_2025_paper.html)
- **作者**: Hao Tan, Zichang Tan, Jun Li, Ajian Liu, Jun Wan, Zhen Lei
- **🏷️ 机构**: SAIS, UCAS, SIAT,Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences,MAIS
- **会议**: CVPR 2025

### DeCLIP: Decoupled Learning for Open-Vocabulary Dense Perception.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_DeCLIP_Decoupled_Learning_for_Open-Vocabulary_Dense_Perception_CVPR_2025_paper.html)
- **作者**: Junjie Wang, Bin Chen, Yulin Li, Bin Kang, Yichi Chen, Zhuotao Tian
- **🏷️ 机构**: HIT,School of Computer Science and Technology,Shenzhen, HIT,International Research Institute for Artificial Intelligence,Shenzhen, University of Chinese Academy of Sciences
- **会议**: CVPR 2025

### Dual Semantic Guidance for Open Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Dual_Semantic_Guidance_for_Open_Vocabulary_Semantic_Segmentation_CVPR_2025_paper.html)
- **作者**: Zhengyang Wang, Tingliang Feng, Fan Lyu, Fanhua Shang, Wei Feng, Liang Wan
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing, Chinese Academy of Sciences,New Laboratory of Pattern Recognition, Institute of Automation
- **会议**: CVPR 2025

### Masked Point-Entity Contrast for Open-Vocabulary 3D Scene Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.html)
- **作者**: Yan Wang, Baoxiong Jia, Ziyu Zhu, Siyuan Huang
- **🏷️ 机构**: State Key Laboratory of General Artificial Intelligence BIGAI
- **会议**: CVPR 2025

### Reconstructing In-the-Wild Open-Vocabulary Human-Object Interactions.
- **链接**: [arXiv:2503.15898](https://arxiv.org/abs/2503.15898)
- **作者**: Boran Wen, Dingbang Huang, Zichen Zhang, Jiahong Zhou, Jianbin Deng, Jingyu Gong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Reconstructing human-object interactions (HOI) from single images is fundamental in computer vision. Existing methods are primarily trained and tested on indoor scenes due to the lack of 3D data, particularly constrained by the object variety, making it challenging to generalize to real-world scenes with a wide range of objects. The limitations of previous 3D HOI datasets were primarily due to the difficulty in acquiring 3D object assets. However, with the development of 3D reconstruction from single images, recently it has become possible to reconstruct various objects from 2D HOI images. We therefore propose a pipeline for annotating fine-grained 3D humans, objects, and their interactions from single images. We annotated 2.5k+ 3D HOI assets from existing 2D HOI datasets and built the first open-vocabulary in-the-wild 3D HOI dataset Open3DHOI, to serve as a future test set. Moreover, we design a novel Gaussian-HOI optimizer, which efficiently reconstructs the spatial interactions between humans and objects while learning the contact regions. Besides the 3D HOI reconstruction, we also propose several new tasks for 3D HOI understanding to pave the way for future work. Data and code will be publicly available at https://wenboran2002.github.io/3dhoi.

### PanoGS: Gaussian-based Panoptic Segmentation for 3D Open Vocabulary Scene Understanding.
- **链接**: [arXiv:2503.18107](https://arxiv.org/abs/2503.18107)
- **作者**: Hongjia Zhai, Hai Li, Zhenzhe Li, Xiaokun Pan, Yijia He, Guofeng Zhang
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD &amp; CG, RayNeo
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > Recently, 3D Gaussian Splatting (3DGS) has shown encouraging performance for open vocabulary scene understanding tasks. However, previous methods cannot distinguish 3D instance-level information, which usually predicts a heatmap between the scene feature and text query. In this paper, we propose PanoGS, a novel and effective 3D panoptic open vocabulary scene understanding approach. Technically, to learn accurate 3D language features that can scale to large indoor scenarios, we adopt the pyramid tri-plane to model the latent continuous parametric feature space and use a 3D feature decoder to regress the multi-view fused 2D feature cloud. Besides, we propose language-guided graph cuts that synergistically leverage reconstructed geometry and learned language cues to group 3D Gaussian primitives into a set of super-primitives. To obtain 3D consistent instance, we perform graph clustering based segmentation with SAM-guided edge affinity computation between different super-primitives. Extensive experiments on widely used datasets show better or more competitive performance on 3D panoptic open vocabulary scene understanding. Project page: \href{https://zju3dv.github.io/panogs}{https://zju3dv.github.io/panogs}.

### Open-Vocabulary Functional 3D Scene Graphs for Real-World Indoor Spaces.
- **链接**: [arXiv:2503.19199](https://arxiv.org/abs/2503.19199)
- **作者**: Chenyangguang Zhang, Alexandros Delitzas, Fangjinhua Wang, Ruida Zhang, Xiangyang Ji, Marc Pollefeys et al.
- **🏷️ 机构**: Tsinghua University, ETH Z&#x00FC;rich
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > We introduce the task of predicting functional 3D scene graphs for real-world indoor environments from posed RGB-D images. Unlike traditional 3D scene graphs that focus on spatial relationships of objects, functional 3D scene graphs capture objects, interactive elements, and their functional relationships. Due to the lack of training data, we leverage foundation models, including visual language models (VLMs) and large language models (LLMs), to encode functional knowledge. We evaluate our approach on an extended SceneFun3D dataset and a newly collected dataset, FunGraph3D, both annotated with functional 3D scene graphs. Our method significantly outperforms adapted baselines, including Open3DSG and ConceptGraph, demonstrating its effectiveness in modeling complex scene functionalities. We also demonstrate downstream applications such as 3D question answering and robotic manipulation using functional 3D scene graphs. See our project page at https://openfungraph.github.io

### DPSeg: Dual-Prompt Cost Volume Learning for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_DPSeg_Dual-Prompt_Cost_Volume_Learning_for_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.html)
- **作者**: Ziyu Zhao, Xiaoguang Li, Lingjia Shi, Nasrin Imanpour, Song Wang
- **🏷️ 机构**: University of South Carolina,USA, Shenzhen University of Advanced Technology,China
- **会议**: CVPR 2025

### Forensic Self-Descriptions Are All You Need for Zero-Shot Detection, Open-Set Source Attribution, and Clustering of AI-generated Images.
- **链接**: [arXiv:2503.21003](https://arxiv.org/abs/2503.21003)
- **作者**: Tai D. Nguyen, Aref Azizpour, Matthew C. Stamm
- **🏷️ 机构**: Drexel University,Philadelphia,PA,USA
- **会议**: CVPR 2025

- **摘要（英，原文）**:

  > The emergence of advanced AI-based tools to generate realistic images poses significant challenges for forensic detection and source attribution, especially as new generative techniques appear rapidly. Traditional methods often fail to generalize to unseen generators due to reliance on features specific to known sources during training. To address this problem, we propose a novel approach that explicitly models forensic microstructures - subtle, pixel-level patterns unique to the image creation process. Using only real images in a self-supervised manner, we learn a set of diverse predictive filters to extract residuals that capture different aspects of these microstructures. By jointly modeling these residuals across multiple scales, we obtain a compact model whose parameters constitute a unique forensic self-description for each image. This self-description enables us to perform zero-shot detection of synthetic images, open-set source attribution of images, and clustering based on source without prior knowledge. Extensive experiments demonstrate that our method achieves superior accuracy and adaptability compared to competing techniques, advancing the state of the art in synthetic media forensics.

## 跨领域论文（完整笔记在其他领域）

- Percept, Memory, and Imagine: World Feature Simulating for Open-Domain Unknown Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- OW-OVD: Unified Open World and Open Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Cross-Modal and Uncertainty-Aware Agglomeration for Open-Vocabulary 3D Scene Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- Towards Open-Vocabulary Audio-Visual Event Localization. → [multimodal](../multimodal/Guideline%202025.md)
