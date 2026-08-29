# Open-set Detection — 2025 Guideline

> 领域: 开放类检测总类（开放词表 OVD / 开放世界 OWOD / 开集 OOD / 未知类检测）
> 论文数: 35 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### Any3DIS: Class-Agnostic 3D Instance Segmentation by 2D Mask Tracking.
- **链接**: [arXiv:2411.16183](https://arxiv.org/abs/2411.16183) · 📚 被引 2
- **作者**: Phuc Nguyen, Minh Luu, Anh Tuan Tran, Cuong Pham, Khoi Nguyen
- **🏷️ 机构**: MovianAI, Qualcomm AI Research, Qualcomm Vietnam Company Limited
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Multi-Object Tracking (OV-MOT) aims to enable approaches to track objects without being limited to a predefined set of categories. Current OV-MOT methods typically rely primarily on instance-level detection and association, often overlooking trajectory information that is unique and essential for object tracking tasks. Utilizing trajectory information can enhance association stability and classification accuracy, especially in cases of occlusion and category ambiguity, thereby improving adaptability to novel classes. Thus motivated, in this paper we propose \textbf{TRACT}, an open-vocabulary tracker that leverages trajectory information to improve both object association and classification in OV-MOT. Specifically, we introduce a \textit{Trajectory Consistency Reinforcement} (\textbf{TCR}) strategy, that benefits tracking performance by improving target identity and category consistency. In addition, we present \textbf{TraCLIP}, a plug-and-play trajectory classification module. It integrates \textit{Trajectory Feature Aggregation} (\textbf{TFA}) and \textit{Trajectory Semantic Enrichment} (\textbf{TSE}) strategies to fully leverage trajectory information from visual and language perspectives for enhancing the classification results. Extensive experiments on OV-TAO show that our TRACT significantly improves tracking performance, highlighting trajectory information as a valuable asset for OV-MOT. Code will be released.

</details>

### Distilling Spectral Graph for Object-Context Aware Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2411.17150](https://arxiv.org/abs/2411.17150) · 📚 被引 8
- **作者**: Chanyoung Kim, Dayun Ju, Woojung Han, Ming-Hsuan Yang, Seong Jae Hwang
- **🏷️ 机构**: Yonsei University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Semantic Segmentation (OVSS) has advanced with recent vision-language models (VLMs), enabling segmentation beyond predefined categories through various learning schemes. Notably, training-free methods offer scalable, easily deployable solutions for handling unseen data, a key goal of OVSS. Yet, a critical issue persists: lack of object-level context consideration when segmenting complex objects in the challenging environment of OVSS based on arbitrary query prompts. This oversight limits models' ability to group semantically consistent elements within object and map them precisely to user-defined arbitrary classes. In this work, we introduce a novel approach that overcomes this limitation by incorporating object-level contextual knowledge within images. Specifically, our model enhances intra-object consistency by distilling spectral-driven features from vision foundation models into the attention mechanism of the visual encoder, enabling semantically coherent components to form a single object mask. Additionally, we refine the text embeddings with zero-shot object presence likelihood to ensure accurate alignment with the specific objects represented in the images. By leveraging object-level contextual knowledge, our proposed approach achieves state-of-the-art performance with strong generalizability across diverse datasets.

</details>

### Advancing Generalizable Tumor Segmentation with Anomaly-Aware Open-Vocabulary Attention Maps and Frozen Foundation Diffusion Models.
- **链接**: [arXiv:2505.02753](https://arxiv.org/abs/2505.02753) · [代码](https://github.com/Yankai96/DiffuGTS) · 📚 被引 1
- **作者**: Yankai Jiang, Peng Zhang, Donglin Yang, Yuan Tian, Hai Lin, Xiaosong Wang
- **🏷️ 机构**: Shanghai AI Laboratory, Zhejiang University, The University of British Columbia
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We explore Generalizable Tumor Segmentation, aiming to train a single model for zero-shot tumor segmentation across diverse anatomical regions. Existing methods face limitations related to segmentation quality, scalability, and the range of applicable imaging modalities. In this paper, we uncover the potential of the internal representations within frozen medical foundation diffusion models as highly efficient zero-shot learners for tumor segmentation by introducing a novel framework named DiffuGTS. DiffuGTS creates anomaly-aware open-vocabulary attention maps based on text prompts to enable generalizable anomaly segmentation without being restricted by a predefined training category list. To further improve and refine anomaly segmentation masks, DiffuGTS leverages the diffusion model, transforming pathological regions into high-quality pseudo-healthy counterparts through latent space inpainting, and applies a novel pixel-level and feature-level residual learning approach, resulting in segmentation masks with significantly enhanced quality and generalization. Comprehensive experiments on four datasets and seven tumor categories demonstrate the superior performance of our method, surpassing current state-of-the-art models across multiple zero-shot settings. Codes are available at https://github.com/Yankai96/DiffuGTS.

</details>

### Fine-Grained Image-Text Correspondence with Cost Aggregation for Open-Vocabulary Part Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.html)
- **作者**: Jiho Choi, Seonho Lee, Minhyun Lee, Seungho Lee, Hyunjung Shim
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### GROVE: A Generalized Reward for Learning Open-Vocabulary Physical Skill.
- **链接**: [arXiv:2504.04191](https://arxiv.org/abs/2504.04191) · 📚 被引 5
- **作者**: Jieming Cui, Tengyu Liu, Ziyu Meng, Jiale Yu, Ran Song, Wei Zhang et al.
- **🏷️ 机构**: Peking University,Institute for Artificial Intelligence, BIGAI,State Key Laboratory of General Artificial Intelligence, Tsinghua University,Department of Automation
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Learning open-vocabulary physical skills for simulated agents presents a significant challenge in artificial intelligence. Current reinforcement learning approaches face critical limitations: manually designed rewards lack scalability across diverse tasks, while demonstration-based methods struggle to generalize beyond their training distribution. We introduce GROVE, a generalized reward framework that enables open-vocabulary physical skill learning without manual engineering or task-specific demonstrations. Our key insight is that Large Language Models(LLMs) and Vision Language Models(VLMs) provide complementary guidance -- LLMs generate precise physical constraints capturing task requirements, while VLMs evaluate motion semantics and naturalness. Through an iterative design process, VLM-based feedback continuously refines LLM-generated constraints, creating a self-improving reward system. To bridge the domain gap between simulation and natural images, we develop Pose2CLIP, a lightweight mapper that efficiently projects agent poses directly into semantic feature space without computationally expensive rendering. Extensive experiments across diverse embodiments and learning paradigms demonstrate GROVE's effectiveness, achieving 22.2% higher motion naturalness and 25.7% better task completion scores while training 8.4x faster than previous methods. These results establish a new foundation for scalable physical skill acquisition in simulated environments.

</details>

### LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models.
- **链接**: [arXiv:2501.18954](https://arxiv.org/abs/2501.18954) · [代码](https://github.com/iSEE-Laboratory/LLMDet) · 📚 被引 30
- **作者**: Shenghao Fu, Qize Yang, Qijie Mo, Junkai Yan, Xihan Wei, Jingke Meng et al.
- **🏷️ 机构**: Sun Yat-sen University,School of Computer Science and Engineering,China, Alibaba Group,Tongyi Lab
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent open-vocabulary detectors achieve promising performance with abundant region-level annotated data. In this work, we show that an open-vocabulary detector co-training with a large language model by generating image-level detailed captions for each image can further improve performance. To achieve the goal, we first collect a dataset, GroundingCap-1M, wherein each image is accompanied by associated grounding labels and an image-level detailed caption. With this dataset, we finetune an open-vocabulary detector with training objectives including a standard grounding loss and a caption generation loss. We take advantage of a large language model to generate both region-level short captions for each region of interest and image-level long captions for the whole image. Under the supervision of the large language model, the resulting detector, LLMDet, outperforms the baseline by a clear margin, enjoying superior open-vocabulary ability. Further, we show that the improved LLMDet can in turn build a stronger large multi-modal model, achieving mutual benefits. The code, model, and dataset is available at https://github.com/iSEE-Laboratory/LLMDet.

</details>

### Compositional Caching for Training-free Open-vocabulary Attribute Detection.
- **链接**: [arXiv:2503.19145](https://arxiv.org/abs/2503.19145) · 📚 被引 1
- **作者**: Marco Garosi, Alessandro Conti, Gaowen Liu, Elisa Ricci, Massimiliano Mancini
- **🏷️ 机构**: University of Trento, Cisco Research
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Attribute detection is crucial for many computer vision tasks, as it enables systems to describe properties such as color, texture, and material. Current approaches often rely on labor-intensive annotation processes which are inherently limited: objects can be described at an arbitrary level of detail (e.g., color vs. color shades), leading to ambiguities when the annotators are not instructed carefully. Furthermore, they operate within a predefined set of attributes, reducing scalability and adaptability to unforeseen downstream applications. We present Compositional Caching (ComCa), a training-free method for open-vocabulary attribute detection that overcomes these constraints. ComCa requires only the list of target attributes and objects as input, using them to populate an auxiliary cache of images by leveraging web-scale databases and Large Language Models to determine attribute-object compatibility. To account for the compositional nature of attributes, cache images receive soft attribute labels. Those are aggregated at inference time based on the similarity between the input and cache images, refining the predictions of underlying Vision-Language Models (VLMs). Importantly, our approach is model-agnostic, compatible with various VLMs. Experiments on public datasets demonstrate that ComCa significantly outperforms zero-shot and cache-based baselines, competing with recent training-based methods, proving that a carefully designed training-free approach can successfully address open-vocabulary attribute detection.

</details>

### Exploring Simple Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2401.12217](https://arxiv.org/abs/2401.12217) · 📚 被引 7
- **作者**: Zihang Lai
- **🏷️ 机构**: University of Oxford,Visual Geometry Group (VGG)
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation models aim to accurately assign a semantic label to each pixel in an image from a set of arbitrary open-vocabulary texts. In order to learn such pixel-level alignment, current approaches typically rely on a combination of (i) image-level VL model (e.g. CLIP), (ii) ground truth masks, and (iii) custom grouping encoders. In this paper, we introduce S-Seg, a novel model that can achieve surprisingly strong performance without depending on any of the above elements. S-Seg leverages pseudo-mask and language to train a MaskFormer, and can be easily trained from publicly available image-text datasets. Contrary to prior works, our model directly trains for pixel-level features and language alignment. Once trained, S-Seg generalizes well to multiple testing datasets without requiring fine-tuning. In addition, S-Seg has the extra benefits of scalability with data and consistently improvement when augmented with self-training. We believe that our simple yet effective approach will serve as a solid baseline for future research.

</details>

### Effective SAM Combination for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2411.14723](https://arxiv.org/abs/2411.14723) · 📚 被引 5
- **作者**: Minhyeok Lee, Suhwan Cho, Jungho Lee, Sunghun Yang, Heeseung Choi, Ig-Jae Kim et al.
- **🏷️ 机构**: Yonsei University, Korea Institute of Science and Technology (KIST)
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation aims to assign pixel-level labels to images across an unlimited range of classes. Traditional methods address this by sequentially connecting a powerful mask proposal generator, such as the Segment Anything Model (SAM), with a pre-trained vision-language model like CLIP. But these two-stage approaches often suffer from high computational costs, memory inefficiencies. In this paper, we propose ESC-Net, a novel one-stage open-vocabulary segmentation model that leverages the SAM decoder blocks for class-agnostic segmentation within an efficient inference framework. By embedding pseudo prompts generated from image-text correlations into SAM's promptable segmentation framework, ESC-Net achieves refined spatial aggregation for accurate mask predictions. ESC-Net achieves superior performance on standard benchmarks, including ADE20K, PASCAL-VOC, and PASCAL-Context, outperforming prior methods in both efficiency and accuracy. Comprehensive ablation studies further demonstrate its robustness across challenging conditions.

</details>

### Mosaic3D: Foundation Dataset and Model for Open-Vocabulary 3D Segmentation.
- **链接**: [arXiv:2502.02548](https://arxiv.org/abs/2502.02548) · 📚 被引 3
- **作者**: Junha Lee, Chunghyun Park, Jaesung Choe, Yu-Chiang Frank Wang, Jan Kautz, Minsu Cho et al.
- **🏷️ 机构**: NVIDIA, POSTECH
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We tackle open-vocabulary 3D scene understanding by introducing a novel data generation pipeline and training framework. Our method addresses three critical requirements for effective training: precise 3D region segmentation, comprehensive textual descriptions, and sufficient dataset scale. By leveraging state-of-the-art open-vocabulary image segmentation models and region-aware Vision-Language Models, we develop an automatic pipeline that generates high-quality 3D mask-text pairs. Applying this pipeline to multiple 3D scene datasets, we create Mosaic3D-5.6M, a dataset of over 30K annotated scenes with 5.6M mask-text pairs, significantly larger than existing datasets. Building upon this data, we propose Mosaic3D, a foundation model combining a 3D encoder trained with contrastive learning and a lightweight mask decoder for open-vocabulary 3D semantic and instance segmentation. Our approach achieves state-of-the-art results on open-vocabulary 3D semantic and instance segmentation tasks including ScanNet200, Matterport3D, and ScanNet++, with ablation studies validating the effectiveness of our large-scale training data.

</details>

### Mask-Adapter: The Devil is in the Masks for Open-Vocabulary Segmentation.
- **链接**: [arXiv:2412.04533](https://arxiv.org/abs/2412.04533) · [代码](https://github.com/hustvl/MaskAdapter) · 📚 被引 14
- **作者**: Yongkang Li, Tianheng Cheng, Bin Feng, Wenyu Liu, Xinggang Wang
- **🏷️ 机构**: Huazhong University of Science &amp; Technology,School of EIC
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent open-vocabulary segmentation methods adopt mask generators to predict segmentation masks and leverage pre-trained vision-language models, e.g., CLIP, to classify these masks via mask pooling. Although these approaches show promising results, it is counterintuitive that accurate masks often fail to yield accurate classification results through pooling CLIP image embeddings within the mask regions. In this paper, we reveal the performance limitations of mask pooling and introduce Mask-Adapter, a simple yet effective method to address these challenges in open-vocabulary segmentation. Compared to directly using proposal masks, our proposed Mask-Adapter extracts semantic activation maps from proposal masks, providing richer contextual information and ensuring alignment between masks and CLIP. Additionally, we propose a mask consistency loss that encourages proposal masks with similar IoUs to obtain similar CLIP embeddings to enhance models' robustness to varying predicted masks. Mask-Adapter integrates seamlessly into open-vocabulary segmentation methods based on mask pooling in a plug-and-play manner, delivering more accurate classification results. Extensive experiments across several zero-shot benchmarks demonstrate significant performance gains for the proposed Mask-Adapter on several well-established methods. Notably, Mask-Adapter also extends effectively to SAM and achieves impressive results on several open-vocabulary segmentation datasets. Code and models are available at https://github.com/hustvl/MaskAdapter.

</details>

### SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.html) · 📚 被引 51
- **作者**: Kaiyu Li, Ruixun Liu, Xiangyong Cao, Xueru Bai, Feng Zhou, Deyu Meng et al.
- **🏷️ 机构**: Xi&#x2019;an Jiaotong University,School of Software Engineering,Xi&#x2019;an,China,710049, Xi&#x2019;an Jiaotong University,School of Computer Science and Technology,Xi&#x2019;an,China,710049, Xidian University
- **会议**: CVPR 2025

### Anomize: Better Open Vocabulary Video Anomaly Detection.
- **链接**: [arXiv:2503.18094](https://arxiv.org/abs/2503.18094) · 📚 被引 15
- **作者**: Fei Li, Wenxuan Liu, Jingjing Chen, Ruixu Zhang, Yuran Wang, Xian Zhong et al.
- **🏷️ 机构**: Wuhan University,National Engineering Research Center for Multimedia Software, School of Computer Science, Peking University,State Key Laboratory for Multimedia Information Processing, School of Computer Science, Fudan University,Shanghai Key Lab of Intelligent Information Processing, School of Computer Science
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open Vocabulary Video Anomaly Detection (OVVAD) seeks to detect and classify both base and novel anomalies. However, existing methods face two specific challenges related to novel anomalies. The first challenge is detection ambiguity, where the model struggles to assign accurate anomaly scores to unfamiliar anomalies. The second challenge is categorization confusion, where novel anomalies are often misclassified as visually similar base instances. To address these challenges, we explore supplementary information from multiple sources to mitigate detection ambiguity by leveraging multiple levels of visual data alongside matching textual information. Furthermore, we propose incorporating label relations to guide the encoding of new labels, thereby improving alignment between novel videos and their corresponding labels, which helps reduce categorization confusion. The resulting Anomize framework effectively tackles these issues, achieving superior performance on UCF-Crime and XD-Violence datasets, demonstrating its effectiveness in OVVAD.

</details>

### SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html)
- **作者**: Rong Li, Shijie Li, Lingdong Kong, Xulei Yang, Junwei Liang
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### SGC-Net: Stratified Granular Comparison Network for Open-Vocabulary HOI Detection.
- **链接**: [arXiv:2503.00414](https://arxiv.org/abs/2503.00414) · [代码](https://github.com/Phil0212/SGC-Net) · 📚 被引 1
- **作者**: Xin Lin, Chong Shi, Zuopeng Yang, Haojin Tang, Zhili Zhou
- **🏷️ 机构**: Guangzhou University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent open-vocabulary human-object interaction (OV-HOI) detection methods primarily rely on large language model (LLM) for generating auxiliary descriptions and leverage knowledge distilled from CLIP to detect unseen interaction categories. Despite their effectiveness, these methods face two challenges: (1) feature granularity deficiency, due to reliance on last layer visual features for text alignment, leading to the neglect of crucial object-level details from intermediate layers; (2) semantic similarity confusion, resulting from CLIP's inherent biases toward certain classes, while LLM-generated descriptions based solely on labels fail to adequately capture inter-class similarities. To address these challenges, we propose a stratified granular comparison network. First, we introduce a granularity sensing alignment module that aggregates global semantic features with local details, refining interaction representations and ensuring robust alignment between intermediate visual features and text embeddings. Second, we develop a hierarchical group comparison module that recursively compares and groups classes using LLMs, generating fine-grained and discriminative descriptions for each interaction category. Experimental results on two widely-used benchmark datasets, SWIG-HOI and HICO-DET, demonstrate that our method achieves state-of-the-art results in OV-HOI detection. Codes will be released on https://github.com/Phil0212/SGC-Net.

</details>

### ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html)
- **作者**: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Parameter-efficient Fine-tuning in Hyperspherical Space for Open-vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Zelin Peng, Zhengqin Xu, Zhilin Zeng, Yu Huang, Yaoming Wang, Wei Shen
- **🏷️ 机构**: Shanghai Jiao Tong University,MoE Key Lab of Artificial Intelligence, AI Institute, Meituan
- **会议**: CVPR 2025

### Understanding Fine-tuning CLIP for Open-vocabulary Semantic Segmentation in Hyperbolic Space.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.html)
- **作者**: Zelin Peng, Zhengqin Xu, Zhilin Zeng, Changsong Wen, Yu Huang, Menglin Yang et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

### Semantic Library Adaptation: LoRA Retrieval and Fusion for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2503.21780](https://arxiv.org/abs/2503.21780) · 📚 被引 3
- **作者**: Reza Qorbani, Gianluca Villani, Theodoros Panagiotakopoulos, Marc Botet Colomer, Linus Härenstam-Nielsen, Mattia Segù et al.
- **🏷️ 机构**: KTH, The Good AI Lab, Technical University of Munich
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary semantic segmentation models associate vision and text to label pixels from an undefined set of classes using textual queries, providing versatile performance on novel datasets. However, large shifts between training and test domains degrade their performance, requiring fine-tuning for effective real-world applications. We introduce Semantic Library Adaptation (SemLA), a novel framework for training-free, test-time domain adaptation. SemLA leverages a library of LoRA-based adapters indexed with CLIP embeddings, dynamically merging the most relevant adapters based on proximity to the target domain in the embedding space. This approach constructs an ad-hoc model tailored to each specific input without additional training. Our method scales efficiently, enhances explainability by tracking adapter contributions, and inherently protects data privacy, making it ideal for sensitive applications. Comprehensive experiments on a 20-domain benchmark built over 10 standard datasets demonstrate SemLA's superior adaptability and performance across diverse settings, establishing a new standard in domain adaptation for open-vocabulary semantic segmentation.

</details>

### GREAT: Geometry-Intention Collaborative Inference for Open-Vocabulary 3D Object Affordance Grounding.
- **链接**: [arXiv:2411.19626](https://arxiv.org/abs/2411.19626) · 📚 被引 3
- **作者**: Yawen Shao, Wei Zhai, Yuhang Yang, Hongchen Luo, Yang Cao, Zheng-Jun Zha
- **🏷️ 机构**: University of Science and Technology of China,MoE Key Laboratory of Brain-Inspired Intelligent Perception and Cognition, Northeastern University
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary 3D object affordance grounding aims to anticipate ``action possibilities'' regions on 3D objects with arbitrary instructions, which is crucial for robots to generically perceive real scenarios and respond to operational changes. Existing methods focus on combining images or languages that depict interactions with 3D geometries to introduce external interaction priors. However, they are still vulnerable to a limited semantic space by failing to leverage implied invariant geometries and potential interaction intentions. Normally, humans address complex tasks through multi-step reasoning and respond to diverse situations by leveraging associative and analogical thinking. In light of this, we propose GREAT (GeometRy-intEntion collAboraTive inference) for Open-Vocabulary 3D Object Affordance Grounding, a novel framework that mines the object invariant geometry attributes and performs analogically reason in potential interaction scenarios to form affordance knowledge, fully combining the knowledge with both geometries and visual contents to ground 3D object affordance. Besides, we introduce the Point Image Affordance Dataset v2 (PIADv2), the largest 3D object affordance dataset at present to support the task. Extensive experiments demonstrate the effectiveness and superiority of GREAT. The code and dataset are available at https://yawen-shao.github.io/GREAT/.

</details>

### LPOSS: Label Propagation Over Patches and Pixels for Open-vocabulary Semantic Segmentation.
- **链接**: [arXiv:2503.19777](https://arxiv.org/abs/2503.19777) · [代码](https://github.com/vladan-stojnic/LPOSS) · 📚 被引 2
- **作者**: Vladan Stojnic, Yannis Kalantidis, Jirí Matas, Giorgos Tolias
- **🏷️ 机构**: Czech Technical University in Prague,VRG, FEE, NAVER LABS Europe
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose a training-free method for open-vocabulary semantic segmentation using Vision-and-Language Models (VLMs). Our approach enhances the initial per-patch predictions of VLMs through label propagation, which jointly optimizes predictions by incorporating patch-to-patch relationships. Since VLMs are primarily optimized for cross-modal alignment and not for intra-modal similarity, we use a Vision Model (VM) that is observed to better capture these relationships. We address resolution limitations inherent to patch-based encoders by applying label propagation at the pixel level as a refinement step, significantly improving segmentation accuracy near class boundaries. Our method, called LPOSS+, performs inference over the entire image, avoiding window-based processing and thereby capturing contextual interactions across the full image. LPOSS+ achieves state-of-the-art performance among training-free methods, across a diverse set of datasets. Code: https://github.com/vladan-stojnic/LPOSS

</details>

### Recover and Match: Open-Vocabulary Multi-Label Recognition through Knowledge-Constrained Optimal Transport.
- **链接**: [arXiv:2503.15337](https://arxiv.org/abs/2503.15337) · [代码](https://github.com/EricTan7/RAM) · 📚 被引 4
- **作者**: Hao Tan, Zichang Tan, Jun Li, Ajian Liu, Jun Wan, Zhen Lei
- **🏷️ 机构**: SAIS, UCAS, SIAT,Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences,MAIS
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Identifying multiple novel classes in an image, known as open-vocabulary multi-label recognition, is a challenging task in computer vision. Recent studies explore the transfer of powerful vision-language models such as CLIP. However, these approaches face two critical challenges: (1) The local semantics of CLIP are disrupted due to its global pre-training objectives, resulting in unreliable regional predictions. (2) The matching property between image regions and candidate labels has been neglected, relying instead on naive feature aggregation such as average pooling, which leads to spurious predictions from irrelevant regions. In this paper, we present RAM (Recover And Match), a novel framework that effectively addresses the above issues. To tackle the first problem, we propose Ladder Local Adapter (LLA) to enforce refocusing on local regions, recovering local semantics in a memory-friendly way. For the second issue, we propose Knowledge-Constrained Optimal Transport (KCOT) to suppress meaningless matching to non-GT labels by formulating the task as an optimal transport problem. As a result, RAM achieves state-of-the-art performance on various datasets from three distinct domains, and shows great potential to boost the existing methods. Code: https://github.com/EricTan7/RAM.

</details>

### DeCLIP: Decoupled Learning for Open-Vocabulary Dense Perception.
- **链接**: [arXiv:2505.04410](https://arxiv.org/abs/2505.04410) · [代码](https://github.com/xiaomoguhz/DeCLIP) · 📚 被引 9
- **作者**: Junjie Wang, Bin Chen, Yulin Li, Bin Kang, Yichi Chen, Zhuotao Tian
- **🏷️ 机构**: HIT,School of Computer Science and Technology,Shenzhen, HIT,International Research Institute for Artificial Intelligence,Shenzhen, University of Chinese Academy of Sciences
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Dense visual prediction tasks have been constrained by their reliance on predefined categories, limiting their applicability in real-world scenarios where visual concepts are unbounded. While Vision-Language Models (VLMs) like CLIP have shown promise in open-vocabulary tasks, their direct application to dense prediction often leads to suboptimal performance due to limitations in local feature representation. In this work, we present our observation that CLIP's image tokens struggle to effectively aggregate information from spatially or semantically related regions, resulting in features that lack local discriminability and spatial consistency. To address this issue, we propose DeCLIP, a novel framework that enhances CLIP by decoupling the self-attention module to obtain ``content'' and ``context'' features respectively. The ``content'' features are aligned with image crop representations to improve local discriminability, while ``context'' features learn to retain the spatial correlations under the guidance of vision foundation models, such as DINO. Extensive experiments demonstrate that DeCLIP significantly outperforms existing methods across multiple open-vocabulary dense prediction tasks, including object detection and semantic segmentation. Code is available at \textcolor{magenta}{https://github.com/xiaomoguhz/DeCLIP}.

</details>

### Dual Semantic Guidance for Open Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Dual_Semantic_Guidance_for_Open_Vocabulary_Semantic_Segmentation_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Zhengyang Wang, Tingliang Feng, Fan Lyu, Fanhua Shang, Wei Feng, Liang Wan
- **🏷️ 机构**: Tianjin University,College of Intelligence and Computing, Chinese Academy of Sciences,New Laboratory of Pattern Recognition, Institute of Automation
- **会议**: CVPR 2025

### Masked Point-Entity Contrast for Open-Vocabulary 3D Scene Understanding.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Yan Wang, Baoxiong Jia, Ziyu Zhu, Siyuan Huang
- **🏷️ 机构**: State Key Laboratory of General Artificial Intelligence BIGAI
- **会议**: CVPR 2025

### Reconstructing In-the-Wild Open-Vocabulary Human-Object Interactions.
- **链接**: [arXiv:2503.15898](https://arxiv.org/abs/2503.15898)
- **作者**: Boran Wen, Dingbang Huang, Zichen Zhang, Jiahong Zhou, Jianbin Deng, Jingyu Gong et al.
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Reconstructing human-object interactions (HOI) from single images is fundamental in computer vision. Existing methods are primarily trained and tested on indoor scenes due to the lack of 3D data, particularly constrained by the object variety, making it challenging to generalize to real-world scenes with a wide range of objects. The limitations of previous 3D HOI datasets were primarily due to the difficulty in acquiring 3D object assets. However, with the development of 3D reconstruction from single images, recently it has become possible to reconstruct various objects from 2D HOI images. We therefore propose a pipeline for annotating fine-grained 3D humans, objects, and their interactions from single images. We annotated 2.5k+ 3D HOI assets from existing 2D HOI datasets and built the first open-vocabulary in-the-wild 3D HOI dataset Open3DHOI, to serve as a future test set. Moreover, we design a novel Gaussian-HOI optimizer, which efficiently reconstructs the spatial interactions between humans and objects while learning the contact regions. Besides the 3D HOI reconstruction, we also propose several new tasks for 3D HOI understanding to pave the way for future work. Data and code will be publicly available at https://wenboran2002.github.io/3dhoi.

</details>

### PanoGS: Gaussian-based Panoptic Segmentation for 3D Open Vocabulary Scene Understanding.
- **链接**: [arXiv:2503.18107](https://arxiv.org/abs/2503.18107) · 📚 被引 7
- **作者**: Hongjia Zhai, Hai Li, Zhenzhe Li, Xiaokun Pan, Yijia He, Guofeng Zhang
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD &amp; CG, RayNeo
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recently, 3D Gaussian Splatting (3DGS) has shown encouraging performance for open vocabulary scene understanding tasks. However, previous methods cannot distinguish 3D instance-level information, which usually predicts a heatmap between the scene feature and text query. In this paper, we propose PanoGS, a novel and effective 3D panoptic open vocabulary scene understanding approach. Technically, to learn accurate 3D language features that can scale to large indoor scenarios, we adopt the pyramid tri-plane to model the latent continuous parametric feature space and use a 3D feature decoder to regress the multi-view fused 2D feature cloud. Besides, we propose language-guided graph cuts that synergistically leverage reconstructed geometry and learned language cues to group 3D Gaussian primitives into a set of super-primitives. To obtain 3D consistent instance, we perform graph clustering based segmentation with SAM-guided edge affinity computation between different super-primitives. Extensive experiments on widely used datasets show better or more competitive performance on 3D panoptic open vocabulary scene understanding. Project page: \href{https://zju3dv.github.io/panogs}{https://zju3dv.github.io/panogs}.

</details>

### Open-Vocabulary Functional 3D Scene Graphs for Real-World Indoor Spaces.
- **链接**: [arXiv:2503.19199](https://arxiv.org/abs/2503.19199) · 📚 被引 13
- **作者**: Chenyangguang Zhang, Alexandros Delitzas, Fangjinhua Wang, Ruida Zhang, Xiangyang Ji, Marc Pollefeys et al.
- **🏷️ 机构**: Tsinghua University, ETH Z&#x00FC;rich
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We introduce the task of predicting functional 3D scene graphs for real-world indoor environments from posed RGB-D images. Unlike traditional 3D scene graphs that focus on spatial relationships of objects, functional 3D scene graphs capture objects, interactive elements, and their functional relationships. Due to the lack of training data, we leverage foundation models, including visual language models (VLMs) and large language models (LLMs), to encode functional knowledge. We evaluate our approach on an extended SceneFun3D dataset and a newly collected dataset, FunGraph3D, both annotated with functional 3D scene graphs. Our method significantly outperforms adapted baselines, including Open3DSG and ConceptGraph, demonstrating its effectiveness in modeling complex scene functionalities. We also demonstrate downstream applications such as 3D question answering and robotic manipulation using functional 3D scene graphs. See our project page at https://openfungraph.github.io

</details>

### DPSeg: Dual-Prompt Cost Volume Learning for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_DPSeg_Dual-Prompt_Cost_Volume_Learning_for_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.html) · 📚 被引 4
- **作者**: Ziyu Zhao, Xiaoguang Li, Lingjia Shi, Nasrin Imanpour, Song Wang
- **🏷️ 机构**: University of South Carolina,USA, Shenzhen University of Advanced Technology,China
- **会议**: CVPR 2025

### Forensic Self-Descriptions Are All You Need for Zero-Shot Detection, Open-Set Source Attribution, and Clustering of AI-generated Images.
- **链接**: [arXiv:2503.21003](https://arxiv.org/abs/2503.21003) · 📚 被引 3
- **作者**: Tai D. Nguyen, Aref Azizpour, Matthew C. Stamm
- **🏷️ 机构**: Drexel University,Philadelphia,PA,USA
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The emergence of advanced AI-based tools to generate realistic images poses significant challenges for forensic detection and source attribution, especially as new generative techniques appear rapidly. Traditional methods often fail to generalize to unseen generators due to reliance on features specific to known sources during training. To address this problem, we propose a novel approach that explicitly models forensic microstructures - subtle, pixel-level patterns unique to the image creation process. Using only real images in a self-supervised manner, we learn a set of diverse predictive filters to extract residuals that capture different aspects of these microstructures. By jointly modeling these residuals across multiple scales, we obtain a compact model whose parameters constitute a unique forensic self-description for each image. This self-description enables us to perform zero-shot detection of synthetic images, open-set source attribution of images, and clustering based on source without prior knowledge. Extensive experiments demonstrate that our method achieves superior accuracy and adaptability compared to competing techniques, advancing the state of the art in synthetic media forensics.

</details>

### DOVTrack: Data-Efficient Open-Vocabulary Tracking.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/83538ee6cde54c0a3df02dc629ab8edd-Abstract-Conference.html) · 📚 被引 0
- **作者**: Zekun Qian, Ruize Han, Zhixiang Wang, Junhui Hou, Wei Feng
- **🏷️ 机构**: Tianjin University           City University of Hong Kong, Shenzhen University of Advanced Technology, CyberAgent
- **会议**: NeurIPS 2025

### OpenHype: Hyperbolic Embeddings for Hierarchical Open-Vocabulary Radiance Fields.
- **链接**: [arXiv:2510.21441](https://arxiv.org/abs/2510.21441) · 📚 被引 1
- **作者**: Lisa Weijler, Sebastian Koch, Fabio Poiesi, Timo Ropinski, Pedro Hermosilla
- **🏷️ 机构**: Computer Vision Lab, TU Wien, University Ulm, Fondazione Bruno Kessler
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Modeling the inherent hierarchical structure of 3D objects and 3D scenes is highly desirable, as it enables a more holistic understanding of environments for autonomous agents. Accomplishing this with implicit representations, such as Neural Radiance Fields, remains an unexplored challenge. Existing methods that explicitly model hierarchical structures often face significant limitations: they either require multiple rendering passes to capture embeddings at different levels of granularity, significantly increasing inference time, or rely on predefined, closed-set discrete hierarchies that generalize poorly to the diverse and nuanced structures encountered by agents in the real world. To address these challenges, we propose OpenHype, a novel approach that represents scene hierarchies using a continuous hyperbolic latent space. By leveraging the properties of hyperbolic geometry, OpenHype naturally encodes multi-scale relationships and enables smooth traversal of hierarchies through geodesic paths in latent space. Our method outperforms state-of-the-art approaches on standard benchmarks, demonstrating superior efficiency and adaptability in 3D scene understanding.

</details>

### Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation.
- **链接**: [arXiv:2506.09881](https://arxiv.org/abs/2506.09881) · [代码](https://github.com/anonymouse-9c53tp182bvz/Vireo) · 📚 被引 1
- **作者**: Siyu Chen, Ting Han, Chengzheng Fu, Changshe Zhang, Chaolei Wang, Jinhe Su et al.
- **🏷️ 机构**: Yale University, SUN YAT-SEN UNIVERSITY, Nanjing University of Aeronautics and Astronautics
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary semantic segmentation (OVSS) and domain generalization in semantic segmentation (DGSS) highlight a subtle complementarity that motivates Open-Vocabulary Domain-Generalized Semantic Segmentation (OV-DGSS). OV-DGSS aims to generate pixel-level masks for unseen categories while maintaining robustness across unseen domains, a critical capability for real-world scenarios such as autonomous driving in adverse conditions. We introduce Vireo, a novel single-stage framework for OV-DGSS that unifies the strengths of OVSS and DGSS for the first time. Vireo builds upon the frozen Visual Foundation Models (VFMs) and incorporates scene geometry via Depth VFMs to extract domain-invariant structural features. To bridge the gap between visual and textual modalities under domain shift, we propose three key components: (1) GeoText Prompts, which align geometric features with language cues and progressively refine VFM encoder representations; (2) Coarse Mask Prior Embedding (CMPE) for enhancing gradient flow for faster convergence and stronger textual influence; and (3) the Domain-Open-Vocabulary Vector Embedding Head (DOV-VEH), which fuses refined structural and semantic features for robust prediction. Comprehensive evaluation on these components demonstrates the effectiveness of our designs. Our proposed Vireo achieves the state-of-the-art performance and surpasses existing methods by a large margin in both domain generalization and open-vocabulary recognition, offering a unified and scalable solution for robust visual understanding in diverse and dynamic environments. Code is available at https://github.com/anonymouse-9c53tp182bvz/Vireo.

</details>

### Beyond the Seen: Bounded Distribution Estimation for Open-Vocabulary Learning.
- **链接**: [arXiv:2510.04770](https://arxiv.org/abs/2510.04770) · 📚 被引 0
- **作者**: Xiaomeng Fan, Yuchuan Mao, Zhi Gao, Yuwei Wu, Jin Chen, Yunde Jia
- **🏷️ 机构**: Beijing Institute of Technology, Shenzhen MSU-BIT University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary learning requires modeling the data distribution in open environments, which consists of both seen-class and unseen-class data. Existing methods estimate the distribution in open environments using seen-class data, where the absence of unseen classes makes the estimation error inherently unidentifiable. Intuitively, learning beyond the seen classes is crucial for distribution estimation to bound the estimation error. We theoretically demonstrate that the distribution can be effectively estimated by generating unseen-class data, through which the estimation error is upper-bounded. Building on this theoretical insight, we propose a novel open-vocabulary learning method, which generates unseen-class data for estimating the distribution in open environments. The method consists of a class-domain-wise data generation pipeline and a distribution alignment algorithm. The data generation pipeline generates unseen-class data under the guidance of a hierarchical semantic tree and domain information inferred from the seen-class data, facilitating accurate distribution estimation. With the generated data, the distribution alignment algorithm estimates and maximizes the posterior probability to enhance generalization in open-vocabulary learning. Extensive experiments on $11$ datasets demonstrate that our method outperforms baseline approaches by up to $14\%$, highlighting its effectiveness and superiority.

</details>

### Seg4Diff: Unveiling Open-Vocabulary Semantic Segmentation in Text-to-Image Diffusion Transformers.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/67b87de31003d4f56e3312a2e04b479d-Abstract-Conference.html) · 📚 被引 0
- **作者**: Chaehyun Kim, Heeseong Shin, Eunbeen Hong, Heeji Yoon, Anurag Arnab, Paul Hongsuck Seo et al.
- **🏷️ 机构**: KAIST, Korea Advanced Institute of Science &amp; Technology, Google DeepMind
- **会议**: NeurIPS 2025

### Open-Vocabulary Part Segmentation via Progressive and Boundary-Aware Strategy.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/5c186016d0844767209dc36e9e61441b-Abstract-Conference.html) · 📚 被引 0
- **作者**: Xinlong Li, Di Lin, Shaoyiyi Gao, Jiaxin Li, Ruonan Liu, Qing Guo
- **🏷️ 机构**: Tianjin University, nanjing university, Shanghai Jiao Tong University
- **会议**: NeurIPS 2025

### Interaction-Centric Knowledge Infusion and Transfer for Open Vocabulary Scene Graph Generation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f7b118ed1bfd2a9f366d55021a8bc1e0-Abstract-Conference.html) · 📚 被引 0
- **作者**: Lin Li, Chuhan Zhang, Dong Zhang, Chong Sun, Chen Li, Long Chen
- **🏷️ 机构**: The Hong Kong University of Science and Technology, Hong Kong University of Science and Technology, HKUST
- **会议**: NeurIPS 2025

### Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/f2644105c6680950b0adbfa0a2cfb177-Abstract-Conference.html) · 📚 被引 0
- **作者**: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma et al.
- **🏷️ 机构**: Case Western Reserve University, Huazhong University of Science and Technology, Westlake University
- **会议**: NeurIPS 2025

### LangHOPS: Language Grounded Hierarchical Open-Vocabulary Part Segmentation.
- **链接**: [arXiv:2510.25263](https://arxiv.org/abs/2510.25263) · 📚 被引 0
- **作者**: Yang Miao, Jan-Nico Zaech, Xi Wang, Fabien Despinoy, Danda Pani Paudel, Luc Van Gool
- **🏷️ 机构**: INSAIT, Sofia University, Institute for Computer Science, Artificial Intelligence and Technology, ETHZ - ETH Zurich
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose LangHOPS, the first Multimodal Large Language Model (MLLM) based framework for open-vocabulary object-part instance segmentation. Given an image, LangHOPS can jointly detect and segment hierarchical object and part instances from open-vocabulary candidate categories. Unlike prior approaches that rely on heuristic or learnable visual grouping, our approach grounds object-part hierarchies in language space. It integrates the MLLM into the object-part parsing pipeline to leverage its rich knowledge and reasoning capabilities, and link multi-granularity concepts within the hierarchies. We evaluate LangHOPS across multiple challenging scenarios, including in-domain and cross-dataset object-part instance segmentation, and zero-shot semantic segmentation. LangHOPS achieves state-of-the-art results, surpassing previous methods by 5.5% Average Precision (AP) (in-domain) and 4.8% (cross-dataset) on the PartImageNet dataset and by 2.5% mIOU on unseen object parts in ADE20K (zero-shot). Ablation studies further validate the effectiveness of the language-grounded hierarchy and MLLM driven part query refinement strategy. The code will be released here.

</details>

### Test-Time Adaptation of Vision-Language Models for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/6c5b82193c5d8e6aa5806239676ddc97-Abstract-Conference.html)
- **作者**: Mehrdad Noori, David Osowiechi, Gustavo Adolfo Vargas Hakim, Ali Bahri, Moslem Yazdanpanah, Sahar Dastani et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

### OPMapper: Enhancing Open-Vocabulary Semantic Segmentation with Multi-Guidance Information.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/d3248f63ad76392608963b97c095ca33-Abstract-Conference.html) · 📚 被引 1
- **作者**: Xuehui Wang, Chongjie Si, Xue Yang, Yuzhi Zhao, Wenhai Wang, Xiaokang Yang et al.
- **🏷️ 机构**: Shanghai Jiaotong University, Shanghai Jiao Tong University, Shanghai AI Laboratory
- **会议**: NeurIPS 2025

### COS3D: Collaborative Open-Vocabulary 3D Segmentation.
- **链接**: [arXiv:2510.20238](https://arxiv.org/abs/2510.20238) · [代码](https://github.com/Runsong123/COS3D) · 📚 被引 0
- **作者**: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu et al.
- **🏷️ 机构**: The Chinese University of Hong Kong, Autodesk, Carnegie Mellon University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D segmentation is a fundamental yet challenging task, requiring a mutual understanding of both segmentation and language. However, existing Gaussian-splatting-based methods rely either on a single 3D language field, leading to inferior segmentation, or on pre-computed class-agnostic segmentations, suffering from error accumulation. To address these limitations, we present COS3D, a new collaborative prompt-segmentation framework that contributes to effectively integrating complementary language and segmentation cues throughout its entire pipeline. We first introduce the new concept of collaborative field, comprising an instance field and a language field, as the cornerstone for collaboration. During training, to effectively construct the collaborative field, our key idea is to capture the intrinsic relationship between the instance field and language field, through a novel instance-to-language feature mapping and designing an efficient two-stage training strategy. During inference, to bridge distinct characteristics of the two fields, we further design an adaptive language-to-instance prompt refinement, promoting high-quality prompt-segmentation inference. Extensive experiments not only demonstrate COS3D's leading performance over existing methods on two widely-used benchmarks but also show its high potential to various applications,~\ie, novel image-based 3D segmentation, hierarchical segmentation, and robotics. The code is publicly available at \href{https://github.com/Runsong123/COS3D}{https://github.com/Runsong123/COS3D}.

</details>

### Zero-Shot Detection of LLM-Generated Text via Implicit Reward Model.
- **链接**: [arXiv:2604.21223](https://arxiv.org/abs/2604.21223) · 📚 被引 0
- **作者**: Runheng Liu, Heyan Huang, Xingchen Xiao, Zhijing Wu
- **🏷️ 机构**: Beijing Institute of Technology
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large language models (LLMs) have demonstrated remarkable capabilities across various tasks. However, their ability to generate human-like text has raised concerns about potential misuse. This underscores the need for reliable and effective methods to detect LLM-generated text. In this paper, we propose IRM, a novel zero-shot approach that leverages Implicit Reward Models for LLM-generated text detection. Such implicit reward models can be derived from publicly available instruction-tuned and base models. Previous reward-based method relies on preference construction and task-specific fine-tuning. In comparison, IRM requires neither preference collection nor additional training. We evaluate IRM on the DetectRL benchmark and demonstrate that IRM can achieve superior detection performance, outperforms existing zero-shot and supervised methods in LLM-generated text detection.

</details>

### OOD-Barrier: Build a Middle-Barrier for Open-Set Single-Image Test Time Adaptation via Vision Language Models.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/dd391150be8cec625434323f6b1f9d14-Abstract-Conference.html)
- **作者**: Boyang Peng, Sanqing Qu, Tianpei Zou, Fan Lu, Ya Wu, Kai Chen et al.
- **🏷️ 机构**: （机构待查）
- **会议**: NeurIPS 2025

## 跨领域论文（完整笔记在其他领域）

- Percept, Memory, and Imagine: World Feature Simulating for Open-Domain Unknown Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- OW-OVD: Unified Open World and Open Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202025.md)
- Cross-Modal and Uncertainty-Aware Agglomeration for Open-Vocabulary 3D Scene Understanding. → [multimodal](../multimodal/Guideline%202025.md)
- Towards Open-Vocabulary Audio-Visual Event Localization. → [multimodal](../multimodal/Guideline%202025.md)
- ODE: Open-Set Evaluation of Hallucinations in Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202025.md)
