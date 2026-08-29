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

### Novel Class Discovery for Point Cloud Segmentation via Joint Learning of Causal Representation and Reasoning.
- **链接**: [arXiv:2510.13307](https://arxiv.org/abs/2510.13307) · 📚 被引 0
- **作者**: Yang Li, Aming Wu, Zihao Zhang, Yahong Han
- **🏷️ 机构**: Tsinghua-Berkeley Shenzhen Institute, Xidian University, Henan University of Technology
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

## 🆕 增量新增

### Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-Time Open-Vocabulary Object Detection. **⭐⭐⭐** (相关度: 75%)
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01938) · 📚 被引 2
- **作者**: Yehao Lu, Minghe Weng, Zekang Xiao, Rui Jiang, Wei Su, Guangcong Zheng et al.
- **🏷️ 机构**: College of Computer Science and Technology, Zhejiang University, Polytechnic Institute, Zhejiang University, ZTE
- **会议**: ICCV 2025
- **摘要（中）**: 针对开放词汇目标检测中实时性与精度平衡的问题，提出了Dynamic-DINO，一种基于细粒度混合专家（MoE）调优的方法。该方法通过动态路由机制在推理时仅激活部分专家，降低计算开销，同时利用MoE的细粒度调整增强模型对开放词汇的适应能力。摘要信息有限，但推测其核心在于优化MoE调优策略以提升实时开放词汇检测性能。
- **摘要（英）**: To balance real-time performance and accuracy in open-vocabulary object detection, Dynamic-DINO proposes fine-grained mixture of experts (MoE) tuning with dynamic routing to activate only relevant experts during inference, reducing computation while enhancing adaptability to open vocabulary. The abstract is limited, but the approach likely optimizes MoE tuning for real-time detection.
- **核心贡献**: 提出基于细粒度MoE调优的实时开放词汇检测方法。
- **创新点**: 利用动态路由机制实现推理时专家稀疏激活。
- **结果**: 预期在保持精度的同时提升推理速度，具体数据待补充。

### Talking to DINO: Bridging Self-Supervised Vision Backbones with Language for Open-Vocabulary Segmentation. **⭐⭐⭐⭐** (相关度: 85%)
- **链接**: [arXiv:2411.19331](https://arxiv.org/abs/2411.19331) · 📚 被引 6
- **作者**: Luca Barsellotti, Lorenzo Bianchi, Nicola Messina, Fabio Carrara, Marcella Cornia, Lorenzo Baraldi et al.
- **🏷️ 机构**: University of Modena and Reggio Emilia,Italy, ISTI-CNR,Italy
- **会议**: ICCV 2025
- **摘要（中）**: 针对开放词汇分割中CLIP空间定位差、DINO缺乏语言理解的问题，提出Talk2DINO混合框架，通过学习映射函数将CLIP文本嵌入对齐到DINOv2的patch级特征，无需微调骨干网络。训练时利用DINOv2注意力图选择性对齐局部视觉patch与文本嵌入，增强分割的自然性和减少噪声，并能有效区分前景。相比现有方法，该方法结合了自监督视觉模型的细粒度编码与语言模型的语义理解，提升了分割精度和鲁棒性。
- **摘要（英）**: This paper addresses the gap between CLIP's global alignment and DINO's lack of language integration in open-vocabulary segmentation. Talk2DINO aligns CLIP text embeddings to DINOv2 patch features via a learned mapping without fine-tuning backbones, using attention maps for selective alignment. It improves segmentation naturalness and foreground distinction over existing methods.
- **核心贡献**: 提出Talk2DINO，一种无需微调骨干的混合框架，结合DINOv2与CLIP实现开放词汇分割。
- **创新点**: 利用DINOv2注意力图进行选择性视觉-文本对齐，避免骨干微调。
- **结果**: 分割更自然、噪声更少，且能有效区分前景。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Segmentation (OVS) aims at segmenting images from free-form textual concepts without predefined training classes. While existing vision-language models such as CLIP can generate segmentation masks by leveraging coarse spatial information from Vision Transformers, they face challenges in spatial localization due to their global alignment of image and text features. Conversely, self-supervised visual models like DINO excel in fine-grained visual encoding but lack integration with language. To bridge this gap, we present Talk2DINO, a novel hybrid approach that combines the spatial accuracy of DINOv2 with the language understanding of CLIP. Our approach aligns the textual embeddings of CLIP to the patch-level features of DINOv2 through a learned mapping function without the need to fine-tune the underlying backbones. At training time, we exploit the attention maps of DINOv2 to selectively align local visual patches with textual embeddings. We show that the powerful semantic and localization abilities of Talk2DINO can enhance the segmentation process, resulting in more natural and less noisy segmentations, and that our approach can also effectively distinguish foreground objects from the background. Experimental results demonstrate that Talk2DINO achieves state-of-the-art performance across several unsupervised OVS benchmarks. Source code and models are publicly available at: https://lorebianchi98.github.io/Talk2DINO/.

</details>

### OpenLex3D: A Tiered Benchmark for Open-Vocabulary 3D Scene Representations. **⭐⭐⭐** (相关度: 70%)
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/05057404e0cab4fe58971dc3a7d6044c-Abstract-Datasets_and_Benchmarks_Track.html)
- **作者**: Christina Kassab, Sacha Morin, Martin Büchner, Matías Mattamala, Kumaraditya Gupta, Abhinav Valada et al.
- **🏷️ 机构**: University of Oxford, Mila, Université de Montréal, Albert-Ludwigs-Universität Freiburg
- **会议**: NeurIPS 2025
- **摘要（中）**: 针对开放词汇3D场景表示缺乏统一基准的问题，提出OpenLex3D分层基准，用于评估3D场景理解中的开放词汇能力。该基准涵盖多个层次的任务，旨在标准化评估流程。方法可能包括数据收集和评估协议设计，但摘要不完整。相比现有基准，它更全面且分层，支持细粒度评估。效果需进一步验证。
- **摘要（英）**: This paper introduces OpenLex3D, a tiered benchmark for open-vocabulary 3D scene representations, addressing the lack of standardized evaluation. It provides hierarchical tasks to assess open-vocabulary capabilities in 3D understanding. The benchmark aims to improve comparability across methods.
- **核心贡献**: 提出OpenLex3D分层基准，标准化开放词汇3D场景表示评估。
- **创新点**: 分层任务设计，覆盖多粒度3D开放词汇理解。
- **结果**: 提供统一评估框架，但具体效果未在摘要中给出。

### Search and Detect: Training-Free Long Tail Object Detection via Web-Image Retrieval. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2409.18733](https://arxiv.org/abs/2409.18733)
- **作者**: Mankeerat Sidhu, Hetarth Chopra, Ansel Blume, Jeonghwan Kim, Revanth Gangi Reddy, Heng Ji
- **🏷️ 机构**: University of Illinois Urbana Champaign,Urbana,USA
- **会议**: CVPR 2025
- **摘要（中）**: 针对长尾目标检测中稀有类性能差的问题，提出SearchDet训练-free框架，通过Web图像检索获取正负样本，嵌入后计算输入图像加权查询以检测目标。该方法无需训练，在ODinW上mAP提升48.7%，LVIS上提升59.1%，优于GroundingDINO等SOTA。相比现有方法，它利用检索示例增强检测，且对示例变化稳定，减少标注和训练成本。
- **摘要（英）**: SearchDet addresses long-tail object detection by retrieving positive and negative web images to compute a weighted query for detection, without training. It achieves 48.7% mAP improvement on ODinW and 59.1% on LVIS over GroundingDINO. The method is stable to exemplar variations, reducing annotation and training costs.
- **核心贡献**: 提出SearchDet，基于Web检索的训练-free长尾目标检测框架。
- **创新点**: 利用检索图像构建加权查询，无需训练即可增强开放词汇检测。
- **结果**: 在ODinW和LVIS上分别提升48.7%和59.1% mAP。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we introduce SearchDet, a training-free long-tail object detection framework that significantly enhances open-vocabulary object detection performance. SearchDet retrieves a set of positive and negative images of an object to ground, embeds these images, and computes an input image-weighted query which is used to detect the desired concept in the image. Our proposed method is simple and training-free, yet achieves over 48.7% mAP improvement on ODinW and 59.1% mAP improvement on LVIS compared to state-of-the-art models such as GroundingDINO. We further show that our approach of basing object detection on a set of Web-retrieved exemplars is stable with respect to variations in the exemplars, suggesting a path towards eliminating costly data annotation and training procedures.

</details>

### Percept, Memory, and Imagine: World Feature Simulating for Open-Domain Unknown Object Detection. **⭐⭐⭐** (相关度: 80%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Percept_Memory_and_Imagine_World_Feature_Simulating_for_Open-Domain_Unknown_CVPR_2025_paper.html) · 📚 被引 3
- **作者**: Aming Wu, Cheng Deng
- **🏷️ 机构**: Xidian University,School of Electronic Engineering,Xi&#x2019;an,China
- **会议**: CVPR 2025
- **摘要（中）**: 针对开放域未知目标检测中感知、记忆和想象能力不足的问题，提出一种世界特征模拟框架。该方法可能通过模拟未知目标的特征来增强检测，但摘要不完整。相比现有方法，它强调对未知类的泛化。效果未在摘要中明确。
- **摘要（英）**: This paper proposes a world feature simulating framework for open-domain unknown object detection, addressing perception, memory, and imagination limitations. It likely simulates features of unknown targets to improve detection. Specific improvements are not detailed in the abstract.
- **核心贡献**: 提出世界特征模拟框架，用于开放域未知目标检测。
- **创新点**: 通过模拟未知类特征增强检测泛化。
- **结果**: 具体效果未在摘要中给出。

### OW-OVD: Unified Open World and Open Vocabulary Object Detection. **⭐⭐⭐** (相关度: 85%)
- **链接**: [出版页](https://openaccess.thecvf.com/content/CVPR2025/html/Xi_OW-OVD_Unified_Open_World_and_Open_Vocabulary_Object_Detection_CVPR_2025_paper.html) · 📚 被引 9
- **作者**: Xing Xi, Yangyang Huang, Ronghua Luo, Yu Qiu
- **🏷️ 机构**: South China University of Technology,School of Computer Science &#x0026; Engineering
- **会议**: CVPR 2025
- **摘要（中）**: 针对开放世界和开放词汇目标检测的分离问题，提出OW-OVD统一框架，旨在同时处理未知类检测和开放词汇识别。该方法可能整合了两种任务的学习策略，但摘要不完整。相比现有方法，它提供统一解决方案。效果未在摘要中明确。
- **摘要（英）**: OW-OVD unifies open world and open vocabulary object detection, addressing the separation between unknown class detection and open-vocabulary recognition. It likely integrates learning strategies for both tasks. Specific results are not provided in the abstract.
- **核心贡献**: 提出OW-OVD，统一开放世界与开放词汇目标检测。
- **创新点**: 整合未知类检测与开放词汇识别任务。
- **结果**: 具体效果未在摘要中给出。

### Cross-Modal and Uncertainty-Aware Agglomeration for Open-Vocabulary 3D Scene Understanding. **⭐⭐⭐⭐** (相关度: 90%)
- **链接**: [arXiv:2503.16707](https://arxiv.org/abs/2503.16707) · 📚 被引 4
- **作者**: Jinlong Li, Cristiano Saltori, Fabio Poiesi, Nicu Sebe
- **🏷️ 机构**: University of Trento, Fondazione Bruno Kessler
- **会议**: CVPR 2025
- **摘要（中）**: 针对3D场景理解中依赖单一VLM的局限，本文提出CUA-O3D，首个集成CLIP、DINOv2和Stable Diffusion等多基础模型的框架，并引入确定性不确定性估计来自适应蒸馏异构2D特征。该方法解决了语义和几何先验的融合问题，实验显示在开放词汇3D分割任务上优于现有方法。
- **摘要（英）**: CUA-O3D integrates multiple foundation models (CLIP, DINOv2, Stable Diffusion) for 3D scene understanding with deterministic uncertainty estimation for adaptive feature distillation. It harmonizes heterogeneous representations and outperforms existing methods on open-vocabulary 3D tasks.
- **核心贡献**: 提出多基础模型集成和不确定性估计的3D开放词汇理解框架。
- **创新点**: 首次结合多种VLM和视觉模型，利用不确定性蒸馏提升鲁棒性。
- **结果**: 在多个3D数据集上取得领先性能。

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The lack of a large-scale 3D-text corpus has led recent works to distill open-vocabulary knowledge from vision-language models (VLMs). However, these methods typically rely on a single VLM to align the feature spaces of 3D models within a common language space, which limits the potential of 3D models to leverage the diverse spatial and semantic capabilities encapsulated in various foundation models. In this paper, we propose Cross-modal and Uncertainty-aware Agglomeration for Open-vocabulary 3D Scene Understanding dubbed CUA-O3D, the first model to integrate multiple foundation models-such as CLIP, DINOv2, and Stable Diffusion-into 3D scene understanding. We further introduce a deterministic uncertainty estimation to adaptively distill and harmonize the heterogeneous 2D feature embeddings from these models. Our method addresses two key challenges: (1) incorporating semantic priors from VLMs alongside the geometric knowledge of spatially-aware vision foundation models, and (2) using a novel deterministic uncertainty estimation to capture model-specific uncertainties across diverse semantic and geometric sensitivities, helping to reconcile heterogeneous representations during training. Extensive experiments on ScanNetV2 and Matterport3D demonstrate that our method not only advances open-vocabulary segmentation but also achieves robust cross-domain alignment and competitive spatial perception capabilities. The code will be available at: https://github.com/TyroneLi/CUA_O3D.

</details>

### ODE: Open-Set Evaluation of Hallucinations in Multimodal Large Language Models.
- **链接**: [arXiv:2409.09318](https://arxiv.org/abs/2409.09318) · 📚 被引 3
- **作者**: Yahan Tu, Rui Hu, Jitao Sang
- **🏷️ 机构**: Beijing Jiaotong University,Beijing,China
- **会议**: CVPR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Hallucination poses a persistent challenge for multimodal large language models (MLLMs). However, existing benchmarks for evaluating hallucinations are generally static, which may overlook the potential risk of data contamination. To address this issue, we propose ODE, an open-set, dynamic protocol designed to evaluate object hallucinations in MLLMs at both the existence and attribute levels. ODE employs a graph-based structure to represent real-world object concepts, their attributes, and the distributional associations between them. This structure facilitates the extraction of concept combinations based on diverse distributional criteria, generating varied samples for structured queries that evaluate hallucinations in both generative and discriminative tasks. Through the generation of new samples, dynamic concept combinations, and varied distribution frequencies, ODE mitigates the risk of data contamination and broadens the scope of evaluation. This protocol is applicable to both general and specialized scenarios, including those with limited data. Experimental results demonstrate the effectiveness of our protocol, revealing that MLLMs exhibit higher hallucination rates when evaluated with ODE-generated samples, which indicates potential data contamination. Furthermore, these generated samples aid in analyzing hallucination patterns and fine-tuning models, offering an effective approach to mitigating hallucinations in MLLMs.

</details>

### OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection.
- **链接**: [arXiv:2503.06435](https://arxiv.org/abs/2503.06435)
- **作者**: Adrian Chow, Evelien Riddell, Yimu Wang, Sean Sedwards, Krzysztof Czarnecki
- **🏷️ 机构**: University of Waterloo
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D object detection for autonomous driving aims to detect novel objects beyond the predefined training label sets in point cloud scenes. Existing approaches achieve this by connecting traditional 3D object detectors with vision-language models (VLMs) to regress 3D bounding boxes for novel objects and perform open-vocabulary classification through cross-modal alignment between 3D and 2D features. However, achieving robust cross-modal alignment remains a challenge due to semantic inconsistencies when generating corresponding 3D and 2D feature pairs. To overcome this challenge, we present OV-SCAN, an Open-Vocabulary 3D framework that enforces Semantically Consistent Alignment for Novel object discovery. OV-SCAN employs two core strategies: discovering precise 3D annotations and filtering out low-quality or corrupted alignment pairs (arising from 3D annotation, occlusion-induced, or resolution-induced noise). Extensive experiments on the nuScenes dataset demonstrate that OV-SCAN achieves state-of-the-art performance.

</details>

### OpenM3D: Open Vocabulary Multi-View Indoor 3D Object Detection without Human Annotations.
- **链接**: [arXiv:2508.20063](https://arxiv.org/abs/2508.20063) · 📚 被引 2
- **作者**: Peng-Hao Hsu, Ke Zhang, Fu-En Wang, Tao Tu, Ming-Feng Li, Yu-Lun Liu et al.
- **🏷️ 机构**: National Tsing Hua University, Amazon, Cornell University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary (OV) 3D object detection is an emerging field, yet its exploration through image-based methods remains limited compared to 3D point cloud-based methods. We introduce OpenM3D, a novel open-vocabulary multi-view indoor 3D object detector trained without human annotations. In particular, OpenM3D is a single-stage detector adapting the 2D-induced voxel features from the ImGeoNet model. To support OV, it is jointly trained with a class-agnostic 3D localization loss requiring high-quality 3D pseudo boxes and a voxel-semantic alignment loss requiring diverse pre-trained CLIP features. We follow the training setting of OV-3DET where posed RGB-D images are given but no human annotations of 3D boxes or classes are available. We propose a 3D Pseudo Box Generation method using a graph embedding technique that combines 2D segments into coherent 3D structures. Our pseudo-boxes achieve higher precision and recall than other methods, including the method proposed in OV-3DET. We further sample diverse CLIP features from 2D segments associated with each coherent 3D structure to align with the corresponding voxel feature. The key to training a highly accurate single-stage detector requires both losses to be learned toward high-quality targets. At inference, OpenM3D, a highly efficient detector, requires only multi-view images for input and demonstrates superior accuracy and speed (0.3 sec. per scene) on ScanNet200 and ARKitScenes indoor benchmarks compared to existing methods. We outperform a strong two-stage method that leverages our class-agnostic detector with a ViT CLIP-based OV classifier and a baseline incorporating multi-view depth estimator on both accuracy and speed.

</details>

### Bilateral Collaboration with Large Vision-Language Models for Open Vocabulary Human-Object Interaction Detection.
- **链接**: [arXiv:2507.06510](https://arxiv.org/abs/2507.06510)
- **作者**: Yupeng Hu, Changxing Ding, Chang Sun, Shaoli Huang, Xiangmin Xu
- **🏷️ 机构**: South China University of Technology, Tencent AI Lab
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open vocabulary Human-Object Interaction (HOI) detection is a challenging task that detects all <human, verb, object> triplets of interest in an image, even those that are not pre-defined in the training set. Existing approaches typically rely on output features generated by large Vision-Language Models (VLMs) to enhance the generalization ability of interaction representations. However, the visual features produced by VLMs are holistic and coarse-grained, which contradicts the nature of detection tasks. To address this issue, we propose a novel Bilateral Collaboration framework for open vocabulary HOI detection (BC-HOI). This framework includes an Attention Bias Guidance (ABG) component, which guides the VLM to produce fine-grained instance-level interaction features according to the attention bias provided by the HOI detector. It also includes a Large Language Model (LLM)-based Supervision Guidance (LSG) component, which provides fine-grained token-level supervision for the HOI detector by the LLM component of the VLM. LSG enhances the ability of ABG to generate high-quality attention bias. We conduct extensive experiments on two popular benchmarks: HICO-DET and V-COCO, consistently achieving superior performance in the open vocabulary and closed settings. The code will be released in Github.

</details>

### Benefit from Seen: Enhancing Open-Vocabulary Object Detection by Bridging Visual and Textual Co-Occurrence Knowledge.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02053)
- **作者**: Yanqi Li, Jianwei Niu, Tao Ren
- **🏷️ 机构**: School of Computer Science and Engineering, Beihang University,State Key Laboratory of Virtual Reality Technology and Systems,Beijing,China, Institute of Software Chinese Academy of Sciences, University of Chinese Academy of Sciences,State Key Laboratory of Intelligent Game,Beijing,China
- **会议**: ICCV 2025

### SFUOD: Source-Free Unknown Object Detection.
- **链接**: [arXiv:2507.17373](https://arxiv.org/abs/2507.17373)
- **作者**: Keon-Hee Park, Seun-An Choe, Gyeong-Moon Park
- **🏷️ 机构**: Kyung Hee University,Yongin,Republic of Korea, Korea University,Seoul,Republic of Korea
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Source-free object detection adapts a detector pre-trained on a source domain to an unlabeled target domain without requiring access to labeled source data. While this setting is practical as it eliminates the need for the source dataset during domain adaptation, it operates under the restrictive assumption that only pre-defined objects from the source domain exist in the target domain. This closed-set setting prevents the detector from detecting undefined objects. To ease this assumption, we propose Source-Free Unknown Object Detection (SFUOD), a novel scenario which enables the detector to not only recognize known objects but also detect undefined objects as unknown objects. To this end, we propose CollaPAUL (Collaborative tuning and Principal Axis-based Unknown Labeling), a novel framework for SFUOD. Collaborative tuning enhances knowledge adaptation by integrating target-dependent knowledge from the auxiliary encoder with source-dependent knowledge from the pre-trained detector through a cross-domain attention mechanism. Additionally, principal axes-based unknown labeling assigns pseudo-labels to unknown objects by estimating objectness via principal axes projection and confidence scores from model predictions. The proposed CollaPAUL achieves state-of-the-art performances on SFUOD benchmarks, and extensive experiments validate its effectiveness.

</details>

### Visual Textualization for Image Prompted Object Detection.
- **链接**: [arXiv:2506.23785](https://arxiv.org/abs/2506.23785)
- **作者**: Yongjian Wu, Yang Zhou, Jiya Saiyin, Bingzheng Wei, Yan Xu
- **🏷️ 机构**: School of Biological Science and Medical Engineering, Beihang University, ByteDance Inc.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We propose VisTex-OVLM, a novel image prompted object detection method that introduces visual textualization -- a process that projects a few visual exemplars into the text feature space to enhance Object-level Vision-Language Models' (OVLMs) capability in detecting rare categories that are difficult to describe textually and nearly absent from their pre-training data, while preserving their pre-trained object-text alignment. Specifically, VisTex-OVLM leverages multi-scale textualizing blocks and a multi-stage fusion strategy to integrate visual information from visual exemplars, generating textualized visual tokens that effectively guide OVLMs alongside text prompts. Unlike previous methods, our method maintains the original architecture of OVLM, maintaining its generalization capabilities while enhancing performance in few-shot settings. VisTex-OVLM demonstrates superior performance across open-set datasets which have minimal overlap with OVLM's pre-training data and achieves state-of-the-art results on few-shot benchmarks PASCAL VOC and MSCOCO. The code will be released at https://github.com/WitGotFlg/VisTex-OVLM.

</details>

### ASGS: Single-Domain Generalizable Open-Set Object Detection via Adaptive Subgraph Searching.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01944) · 📚 被引 1
- **作者**: Yuxuan Yuan, Luyao Tang, Yixin Chen, Chaoqi Chen, Yue Huang, Xinghao Ding
- **🏷️ 机构**: Ministry of Education of China, Xiamen University,Key Laboratory of Multimedia Trusted Perception and Efficient Computing, Shenzhen University
- **会议**: ICCV 2025

### Attention to Trajectory: Trajectory-Aware Open-Vocabulary Tracking.
- **链接**: [arXiv:2503.08145](https://arxiv.org/abs/2503.08145)
- **作者**: Yunhao Li, Yifan Jiao, Dan Meng, Heng Fan, Libo Zhang
- **🏷️ 机构**: Institute of Software Chinese Academy of Sciences, OPPO Research Institute, University of North Texas
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary Multi-Object Tracking (OV-MOT) aims to enable approaches to track objects without being limited to a predefined set of categories. Current OV-MOT methods typically rely primarily on instance-level detection and association, often overlooking trajectory information that is unique and essential for object tracking tasks. Utilizing trajectory information can enhance association stability and classification accuracy, especially in cases of occlusion and category ambiguity, thereby improving adaptability to novel classes. Thus motivated, in this paper we propose \textbf{TRACT}, an open-vocabulary tracker that leverages trajectory information to improve both object association and classification in OV-MOT. Specifically, we introduce a \textit{Trajectory Consistency Reinforcement} (\textbf{TCR}) strategy, that benefits tracking performance by improving target identity and category consistency. In addition, we present \textbf{TraCLIP}, a plug-and-play trajectory classification module. It integrates \textit{Trajectory Feature Aggregation} (\textbf{TFA}) and \textit{Trajectory Semantic Enrichment} (\textbf{TSE}) strategies to fully leverage trajectory information from visual and language perspectives for enhancing the classification results. Extensive experiments on OV-TAO show that our TRACT significantly improves tracking performance, highlighting trajectory information as a valuable asset for OV-MOT. Code will be released.

</details>

### VOVTrack: Exploring the Potentiality in Raw Videos for Open-Vocabulary Multi-Object Tracking.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00701) · 📚 被引 2
- **作者**: Zekun Qian, Ruize Han, Junhui Hou, Linqi Song, Wei Feng
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University, Shenzhen University of Advanced Technology, City University of Hong Kong\\ \{clarkqian
- **会议**: ICCV 2025

### COVTrack: Continuous Open-Vocabulary Tracking via Adaptive Multi-Cue Fusion.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00937)
- **作者**: Zekun Qian, Ruize Han, Zhixiang Wang, Junhui Hou, Wei Feng
- **🏷️ 机构**: College of Intelligence and Computing, Tianjin University, Shenzhen University of Advanced Technology, City University of Hong Kong
- **会议**: ICCV 2025

### FLOSS: Free Lunch in Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2504.10487](https://arxiv.org/abs/2504.10487) · 📚 被引 2
- **作者**: Yasser Benigmim, Mohammad Fahes, Tuan-Hung Vu, Andrei Bursuc, Raoul de Charette
- **🏷️ 机构**: Inria
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we challenge the conventional practice in Open-Vocabulary Semantic Segmentation (OVSS) of using averaged class-wise text embeddings, which are typically obtained by encoding each class name with multiple templates (e.g., a photo of <class>, a sketch of a <class>). We investigate the impact of templates for OVSS, and find that for each class, there exist single-template classifiers--which we refer to as class-experts--that significantly outperform the conventional averaged classifier. First, to identify these class-experts, we introduce a novel approach that estimates them without any labeled data or training. By leveraging the class-wise prediction entropy of single-template classifiers, we select those yielding the lowest entropy as the most reliable class-experts. Second, we combine the outputs of class-experts in a new fusion process. Our plug-and-play method, coined FLOSS, is orthogonal and complementary to existing OVSS methods, offering an improvement without the need for additional labels or training. Extensive experiments show that FLOSS consistently enhances state-of-the-art OVSS models, generalizes well across datasets with different distribution shifts, and delivers substantial improvements in low-data scenarios where only a few unlabeled images are available. Our code is available at https://github.com/yasserben/FLOSS .

</details>

### Training-Free Class Purification for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2508.00557](https://arxiv.org/abs/2508.00557) · 📚 被引 2
- **作者**: Qi Chen, Lingxiao Yang, Yun Chen, Nailong Zhao, Jianhuang Lai, Jie Shao et al.
- **🏷️ 机构**: Sun Yat-sen University, University of Surrey, Alibaba Cloud Computing
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-tuning pre-trained vision-language models has emerged as a powerful approach for enhancing open-vocabulary semantic segmentation (OVSS). However, the substantial computational and resource demands associated with training on large datasets have prompted interest in training-free methods for OVSS. Existing training-free approaches primarily focus on modifying model architectures and generating prototypes to improve segmentation performance. However, they often neglect the challenges posed by class redundancy, where multiple categories are not present in the current test image, and visual-language ambiguity, where semantic similarities among categories create confusion in class activation. These issues can lead to suboptimal class activation maps and affinity-refined activation maps. Motivated by these observations, we propose FreeCP, a novel training-free class purification framework designed to address these challenges. FreeCP focuses on purifying semantic categories and rectifying errors caused by redundancy and ambiguity. The purified class representations are then leveraged to produce final segmentation predictions. We conduct extensive experiments across eight benchmarks to validate FreeCP's effectiveness. Results demonstrate that FreeCP, as a plug-and-play module, significantly boosts segmentation performance when combined with other OVSS methods.

</details>

### Plug-in Feedback Self-Adaptive Attention in CLIP for Training-Free Open-Vocabulary Segmentation.
- **链接**: [arXiv:2508.20265](https://arxiv.org/abs/2508.20265) · 📚 被引 1
- **作者**: Zhixiang Chi, Yanan Wu, Li Gu, Huan Liu, Ziqiang Wang, Yang Zhang et al.
- **🏷️ 机构**: University of Toronto, China Agricultural University, Concordia University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> CLIP exhibits strong visual-textual alignment but struggle with open-vocabulary segmentation due to poor localization. Prior methods enhance spatial coherence by modifying intermediate attention. But, this coherence isn't consistently propagated to the final output due to subsequent operations such as projections. Additionally, intermediate attention lacks direct interaction with text representations, such semantic discrepancy limits the full potential of CLIP. In this work, we propose a training-free, feedback-driven self-adaptive framework that adapts output-based patch-level correspondences back to the intermediate attention. The output predictions, being the culmination of the model's processing, encapsulate the most comprehensive visual and textual semantics about each patch. Our approach enhances semantic consistency between internal representations and final predictions by leveraging the model's outputs as a stronger spatial coherence prior. We design key modules, including attention isolation, confidence-based pruning for sparse adaptation, and adaptation ensemble, to effectively feedback the output coherence cues. Our method functions as a plug-in module, seamlessly integrating into four state-of-the-art approaches with three backbones (ViT-B, ViT-L, ViT-H). We further validate our framework across multiple attention types (Q-K, self-self, and Proxy augmented with MAE, SAM, and DINO). Our approach consistently improves their performance across eight benchmarks.

</details>

### 풟ℐℋ-CLIP: Unleashing the Diversity of Multi-Head Self-Attention for Training-Free Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02116) · 📚 被引 1
- **作者**: Songsong Duan, Xi Yang, Nannan Wang
- **🏷️ 机构**: School of Telecommunications Engineering, Xidian University,State Key Laboratory of Integrated Services Networks,China
- **会议**: ICCV 2025

### CLIP-Adapted Region-to-Text Learning for Generative Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02228) · 📚 被引 1
- **作者**: Jiannan Ge, Lingxi Xie, Hongtao Xie, Pandeng Li, Sun-Ao Liu, Xiaopeng Zhang et al.
- **🏷️ 机构**: Institute of Artificial Intelligence, Hefei Comprehensive National Science Center, Huawei Inc., University of Science and Technology of China
- **会议**: ICCV 2025

### SPADE: Spatial-Aware Denoising Network for Open-Vocabulary Panoptic Scene Graph Generation with Long- and Local-Range Context Reasoning.
- **链接**: [arXiv:2507.05798](https://arxiv.org/abs/2507.05798) · 📚 被引 1
- **作者**: Xin Hu, Ke Qin, Guiduo Duan, Ming Li, Yuan-Fang Li, Tao He
- **🏷️ 机构**: The Laboratory of Intelligent Collaborative Computing of UESTC, Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Monash University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Panoptic Scene Graph Generation (PSG) integrates instance segmentation with relation understanding to capture pixel-level structural relationships in complex scenes. Although recent approaches leveraging pre-trained vision-language models (VLMs) have significantly improved performance in the open-vocabulary setting, they commonly ignore the inherent limitations of VLMs in spatial relation reasoning, such as difficulty in distinguishing object relative positions, which results in suboptimal relation prediction. Motivated by the denoising diffusion model's inversion process in preserving the spatial structure of input images, we propose SPADE (SPatial-Aware Denoising-nEtwork) framework -- a novel approach for open-vocabulary PSG. SPADE consists of two key steps: (1) inversion-guided calibration for the UNet adaptation, and (2) spatial-aware context reasoning. In the first step, we calibrate a general pre-trained teacher diffusion model into a PSG-specific denoising network with cross-attention maps derived during inversion through a lightweight LoRA-based fine-tuning strategy. In the second step, we develop a spatial-aware relation graph transformer that captures both local and long-range contextual information, facilitating the generation of high-quality relation queries. Extensive experiments on benchmark PSG and Visual Genome datasets demonstrate that SPADE outperforms state-of-the-art methods in both closed- and open-set scenarios, particularly for spatial relationship prediction.

</details>

### Identity-Aware Language Gaussian Splatting for Open-Vocabulary 3D Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01903) · 📚 被引 1
- **作者**: SungMin Jang, Wonjun Kim
- **🏷️ 机构**: Konkuk University
- **会议**: ICCV 2025

### Feature Purification Matters: Suppressing Outlier Propagation for Training-Free Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01887)
- **作者**: Shuo Jin, Siyue Yu, Bingfeng Zhang, Mingjie Sun, Yi Dong, Jimin Xiao
- **🏷️ 机构**: Xi&#x0027;an Jiaotong-Liverpool University, China University of Petroleum (East China), Soochow University
- **会议**: ICCV 2025

### Details Matter for Indoor Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2507.23134](https://arxiv.org/abs/2507.23134)
- **作者**: Sanghun Jung, Jingjing Zheng, Ke Zhang, Nan Qiao, Albert Y. C. Chen, Lu Xia et al.
- **🏷️ 机构**: University of Washington, Amazon Lab126
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Unlike closed-vocabulary 3D instance segmentation that is often trained end-to-end, open-vocabulary 3D instance segmentation (OV-3DIS) often leverages vision-language models (VLMs) to generate 3D instance proposals and classify them. While various concepts have been proposed from existing research, we observe that these individual concepts are not mutually exclusive but complementary. In this paper, we propose a new state-of-the-art solution for OV-3DIS by carefully designing a recipe to combine the concepts together and refining them to address key challenges. Our solution follows the two-stage scheme: 3D proposal generation and instance classification. We employ robust 3D tracking-based proposal aggregation to generate 3D proposals and remove overlapped or partial proposals by iterative merging/removal. For the classification stage, we replace the standard CLIP model with Alpha-CLIP, which incorporates object masks as an alpha channel to reduce background noise and obtain object-centric representation. Additionally, we introduce the standardized maximum similarity (SMS) score to normalize text-to-proposal similarity, effectively filtering out false positives and boosting precision. Our framework achieves state-of-the-art performance on ScanNet200 and S3DIS across all AP and AR metrics, even surpassing an end-to-end closed-vocabulary method.

</details>

### Open-Vocabulary Hoi Detection With Interaction-Aware Prompt and Concept Calibration.
- **链接**: [arXiv:2508.03207](https://arxiv.org/abs/2508.03207) · 📚 被引 3
- **作者**: Ting Lei, Shaofeng Yin, Qingchao Chen, Yuxin Peng, Yang Liu
- **🏷️ 机构**: Wangxuan Institute of Computer Technology,Peking University, National Institute of Health Data Science,Peking University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open Vocabulary Human-Object Interaction (HOI) detection aims to detect interactions between humans and objects while generalizing to novel interaction classes beyond the training set. Current methods often rely on Vision and Language Models (VLMs) but face challenges due to suboptimal image encoders, as image-level pre-training does not align well with the fine-grained region-level interaction detection required for HOI. Additionally, effectively encoding textual descriptions of visual appearances remains difficult, limiting the model's ability to capture detailed HOI relationships. To address these issues, we propose INteraction-aware Prompting with Concept Calibration (INP-CC), an end-to-end open-vocabulary HOI detector that integrates interaction-aware prompts and concept calibration. Specifically, we propose an interaction-aware prompt generator that dynamically generates a compact set of prompts based on the input scene, enabling selective sharing among similar interactions. This approach directs the model's attention to key interaction patterns rather than generic image-level semantics, enhancing HOI detection. Furthermore, we refine HOI concept representations through language model-guided calibration, which helps distinguish diverse HOI concepts by investigating visual similarities across categories. A negative sampling strategy is also employed to improve inter-modal similarity modeling, enabling the model to better differentiate visually similar but semantically distinct actions. Extensive experimental results demonstrate that INP-CC significantly outperforms state-of-the-art models on the SWIG-HOI and HICO-DET datasets. Code is available at https://github.com/ltttpku/INP-CC.

</details>

### Unbiased Region-Language Alignment for Open-Vocabulary Dense Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02209) · 📚 被引 2
- **作者**: Yunheng Li, Yuxuan Li, Quan-Sheng Zeng, Wenhai Wang, Qibin Hou, Ming-Ming Cheng
- **🏷️ 机构**: Nankai University,VCIP, CS, Shanghai AI Laboratory,OpenGVLab
- **会议**: ICCV 2025

### Images as Noisy Labels: Unleashing the Potential of the Diffusion Model for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02248)
- **作者**: Fan Li, Xuanbin Wang, Xuan Wang, Zhaoxiang Zhang, Yuelei Xu
- **🏷️ 机构**: Northwestern Polytechnical University
- **会议**: ICCV 2025

### Stepping Out of Similar Semantic Space for Open-Vocabulary Segmentation.
- **链接**: [arXiv:2506.16058](https://arxiv.org/abs/2506.16058) · 📚 被引 1
- **作者**: Yong Liu, Song-Li Wu, Sule Bai, Jiahao Wang, Yitong Wang, Yansong Tang
- **🏷️ 机构**: Tsinghua Shenzhen International Graduate School, The University of Hong Kong, ByteDance Inc.
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary segmentation aims to achieve segmentation of arbitrary categories given unlimited text inputs as guidance. To achieve this, recent works have focused on developing various technical routes to exploit the potential of large-scale pre-trained vision-language models and have made significant progress on existing benchmarks. However, we find that existing test sets are limited in measuring the models' comprehension of ``open-vocabulary" concepts, as their semantic space closely resembles the training space, even with many overlapping categories. To this end, we present a new benchmark named OpenBench that differs significantly from the training semantics. It is designed to better assess the model's ability to understand and segment a wide range of real-world concepts. When testing existing methods on OpenBench, we find that their performance diverges from the conclusions drawn on existing test sets. In addition, we propose a method named OVSNet to improve the segmentation performance for diverse and open scenarios. Through elaborate fusion of heterogeneous features and cost-free expansion of the training space, OVSNet achieves state-of-the-art results on both existing datasets and our proposed OpenBench. Corresponding analysis demonstrate the soundness and effectiveness of our proposed benchmark and method.

</details>

### Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01556) · 📚 被引 1
- **作者**: Yukuan Min, Muli Yang, Jinhao Zhang, Yuxuan Wang, Aming Wu, Cheng Deng
- **🏷️ 机构**: Xidian University,China, A*STAR,Singapore
- **会议**: ICCV 2025

### Understanding Personal Concept in Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01856) · 📚 被引 1
- **作者**: Sunghyun Park, Jungsoo Lee, Shubhankar Borse, Munawar Hayat, Sungha Choi, Kyuwoong Hwang et al.
- **🏷️ 机构**: Qualcomm AI Research
- **会议**: ICCV 2025

### ROVI: A VLM-LLM Re-Captioned Dataset for Open-Vocabulary Instance-Grounded Text-to-Image Generation.
- **链接**: [arXiv:2508.01008](https://arxiv.org/abs/2508.01008)
- **作者**: Cihang Peng, Qiming Hou, Zhong Ren, Kun Zhou
- **🏷️ 机构**: State Key Lab of CAD &#x0026; CG, Zhejiang University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> We present ROVI, a high-quality synthetic dataset for instance-grounded text-to-image generation, created by labeling 1M curated web images. Our key innovation is a strategy called re-captioning, focusing on the pre-detection stage, where a VLM (Vision-Language Model) generates comprehensive visual descriptions that are then processed by an LLM (Large Language Model) to extract a flat list of potential categories for OVDs (Open-Vocabulary Detectors) to detect. This approach yields a global prompt inherently linked to instance annotations while capturing secondary visual elements humans typically overlook. Evaluations show that ROVI exceeds existing detection datasets in image quality and resolution while containing two orders of magnitude more categories with an open-vocabulary nature. For demonstrative purposes, a text-to-image model GLIGEN trained on ROVI significantly outperforms state-of-the-art alternatives in instance grounding accuracy, prompt fidelity, and aesthetic quality. Our dataset and reproducible pipeline are available at https://github.com/CihangPeng/ROVI.

</details>

### DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-Vocabulary Queries in NeRF.
- **链接**: [arXiv:2507.14596](https://arxiv.org/abs/2507.14596)
- **作者**: Doriand Petit, Steve Bourgeois, Vincent Gay-Bellile, Florian Chabot, Loïc Barthe
- **🏷️ 机构**: Universit&#x00E9; Paris-Saclay,CEA, List,Palaiseau,France,F-91120, IRIT Universit&#x00E9; de Toulouse CNRS,France
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D semantic segmentation provides high-level scene understanding for applications in robotics, autonomous systems, \textit{etc}. Traditional methods adapt exclusively to either task-specific goals (open-vocabulary segmentation) or scene content (unsupervised semantic segmentation). We propose DiSCO-3D, the first method addressing the broader problem of 3D Open-Vocabulary Sub-concepts Discovery, which aims to provide a 3D semantic segmentation that adapts to both the scene and user queries. We build DiSCO-3D on Neural Fields representations, combining unsupervised segmentation with weak open-vocabulary guidance. Our evaluations demonstrate that DiSCO-3D achieves effective performance in Open-Vocabulary Sub-concepts Discovery and exhibits state-of-the-art results in the edge cases of both open-vocabulary and unsupervised segmentation.

</details>

### Sliced Wasserstein Bridge for Open-Vocabulary Video Instance Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01159) · 📚 被引 6
- **作者**: Zheyun Qin, Deng Yu, Chuanchen Luo, Zhumin Chen
- **🏷️ 机构**: School of Computer Science and Technology, Shandong University, School of Artificial Intelligence, Shandong University
- **会议**: ICCV 2025

### Seeing the Unseen: A Semantic Alignment and Context-Aware Prompt Framework for Open-Vocabulary Camouflaged Object Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02196) · 📚 被引 2
- **作者**: Peng Ren, Tian Bai, Jing Sun, Fuming Sun
- **🏷️ 机构**: College of Computer Science and Technology, Jilin University, School of Information and Communication Engineering, Dalian Minzu University
- **会议**: ICCV 2025

### Harnessing Vision Foundation Models for High-Performance, Training-Free Open Vocabulary Segmentation.
- **链接**: [arXiv:2411.09219](https://arxiv.org/abs/2411.09219) · 📚 被引 4
- **作者**: Yuheng Shi, Minjing Dong, Chang Xu
- **🏷️ 机构**: University of Sydney, City University of Hong Kong
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> While Contrastive Language-Image Pre-training (CLIP) has advanced open-vocabulary predictions, its performance on semantic segmentation remains suboptimal. This shortfall primarily stems from its spatial-invariant semantic features and constrained resolution. While previous adaptations addressed spatial invariance semantic by modifying the self-attention in CLIP's image encoder, the issue of limited resolution remains unexplored. Different from previous segment-then-splice methods that segment sub-images via a sliding window and splice the results, we introduce a splice-then-segment paradigm that incorporates Segment-Anything Model (SAM) to tackle the resolution issue since SAM excels at extracting fine-grained semantic correlations from high-resolution images. Specifically, we introduce Trident, a training-free framework that first splices features extracted by CLIP and DINO from sub-images, then leverages SAM's encoder to create a correlation matrix for global aggregation, enabling a broadened receptive field for effective segmentation. Besides, we propose a refinement strategy for CLIP's coarse segmentation outputs by transforming them into prompts for SAM, further enhancing the segmentation performance. Trident achieves a significant improvement in the mIoU across eight benchmarks compared with the current SOTA, increasing from 44.4 to 48.6.Code is available at https://github.com/YuHengsss/Trident.

</details>

### OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00602) · 📚 被引 2
- **作者**: Heng Su, Mengying Xie, Nieqing Cao, Yan Ding, Beichen Shao, Xianlei Long et al.
- **🏷️ 机构**: Chongqing University, Xi&#x0027;an Jiaotong-Liverpool University, Shanghai AI Lab
- **会议**: ICCV 2025

### CLIPeR: Hierarchically Improving Spatial Representation of CLIP for Open-Vocabulary Semantic Segmentation.
- **链接**: [arXiv:2411.13836](https://arxiv.org/abs/2411.13836) · 📚 被引 3
- **作者**: Lin Sun, Jiale Cao, Jin Xie, Xiaoheng Jiang, Yanwei Pang
- **🏷️ 机构**: Tianjin University, Chongqing University, Zhengzhou University
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Language-Image Pre-training (CLIP) exhibits strong zero-shot classification ability on various image-level tasks, leading to the research to adapt CLIP for pixel-level open-vocabulary semantic segmentation without additional training. The key is to improve spatial representation of image-level CLIP, such as replacing self-attention map at last layer with self-self attention map or vision foundation model based attention map. In this paper, we present a novel hierarchical framework, named CLIPer, that hierarchically improves spatial representation of CLIP. The proposed CLIPer includes an early-layer fusion module and a fine-grained compensation module. We observe that, the embeddings and attention maps at early layers can preserve spatial structural information. Inspired by this, we design the early-layer fusion module to generate segmentation map with better spatial coherence. Afterwards, we employ a fine-grained compensation module to compensate the local details using the self-attention maps of diffusion model. We conduct the experiments on seven segmentation datasets. Our proposed CLIPer achieves the state-of-the-art performance on these datasets. For instance, using ViT-L, CLIPer has the mIoU of 69.8% and 43.3% on VOC and COCO Object, outperforming ProxyCLIP by 9.2% and 4.1% respectively.

</details>

### Open-Vocabulary Octree-Graph for 3D Scene Understanding.
- **链接**: [arXiv:2411.16253](https://arxiv.org/abs/2411.16253)
- **作者**: Zhigang Wang, Yifei Su, Chenhui Li, Dong Wang, Yan Huang, Xuelong Li et al.
- **🏷️ 机构**: Northwestern Polytechnical University, University of Chinese Academy of Sciences, Shanghai AI Laboratory
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary 3D scene understanding is indispensable for embodied agents. Recent works leverage pretrained vision-language models (VLMs) for object segmentation and project them to point clouds to build 3D maps. Despite progress, a point cloud is a set of unordered coordinates that requires substantial storage space and does not directly convey occupancy information or spatial relation, making existing methods inefficient for downstream tasks, e.g., path planning and text-based object retrieval. To address these issues, we propose \textbf{Octree-Graph}, a novel scene representation for open-vocabulary 3D scene understanding. Specifically, a Chronological Group-wise Segment Merging (CGSM) strategy and an Instance Feature Aggregation (IFA) algorithm are first designed to get 3D instances and corresponding semantic features. Subsequently, an adaptive-octree structure is developed that stores semantics and depicts the occupancy of an object adjustably according to its shape. Finally, the Octree-Graph is constructed where each adaptive-octree acts as a graph node, and edges describe the spatial relations among nodes. Extensive experiments on various tasks are conducted on several widely-used datasets, demonstrating the versatility and effectiveness of our method. Code is available \href{https://github.com/yifeisu/OV-Octree-Graph}{here}.

</details>

### SAMPLE: Semantic Alignment through Temporal-Adaptive Multimodal Prompt Learning for Event-Based Open-Vocabulary Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01337)
- **作者**: Jing Wang, Rui Zhao, Ruiqin Xiong, Xingtao Wang, Xiaopeng Fan, Tiejun Huang
- **🏷️ 机构**: School of Computer Science, Peking University, School of Computer Science and Technology Harbin Institute of Technology
- **会议**: ICCV 2025

### ReME: A Data-Centric Framework for Training-Free Open-Vocabulary Segmentation.
- **链接**: [arXiv:2506.21233](https://arxiv.org/abs/2506.21233) · 📚 被引 2
- **作者**: Xiwei Xuan, Ziquan Deng, Kwan-Liu Ma
- **🏷️ 机构**: University of California, Davis
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training-free open-vocabulary semantic segmentation (OVS) aims to segment images given a set of arbitrary textual categories without costly model fine-tuning. Existing solutions often explore attention mechanisms of pre-trained models, such as CLIP, or generate synthetic data and design complex retrieval processes to perform OVS. However, their performance is limited by the capability of reliant models or the suboptimal quality of reference sets. In this work, we investigate the largely overlooked data quality problem for this challenging dense scene understanding task, and identify that a high-quality reference set can significantly benefit training-free OVS. With this observation, we introduce a data-quality-oriented framework, comprising a data pipeline to construct a reference set with well-paired segment-text embeddings and a simple similarity-based retrieval to unveil the essential effect of data. Remarkably, extensive evaluations on ten benchmark datasets demonstrate that our method outperforms all existing training-free OVS approaches, highlighting the importance of data-centric design for advancing OVS without training. Our code is available at https://github.com/xiweix/ReME .

</details>

### ATAS: Any-to-Any Self-Distillation for Enhanced Open-Vocabulary Dense Prediction.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.01896)
- **作者**: Juan Yeo, Soonwoo Cha, Jiwoo Song, Hyunbin Jin, Taesup Kim
- **🏷️ 机构**: Gradudate School of Data Science, Seoul National University
- **会议**: ICCV 2025

### Learning to Generalize Without Bias for Open-Vocabulary Action Recognition.
- **链接**: [arXiv:2502.20158](https://arxiv.org/abs/2502.20158) · 📚 被引 1
- **作者**: Yating Yu, Congqi Cao, Yifan Zhang, Yanning Zhang
- **🏷️ 机构**: Northwestern Polytechnical University, Institute of Automation, Chinese Academy of Sciences
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Leveraging the effective visual-text alignment and static generalizability from CLIP, recent video learners adopt CLIP initialization with further regularization or recombination for generalization in open-vocabulary action recognition in-context. However, due to the static bias of CLIP, such video learners tend to overfit on shortcut static features, thereby compromising their generalizability, especially to novel out-of-context actions. To address this issue, we introduce Open-MeDe, a novel Meta-optimization framework with static Debiasing for Open-vocabulary action recognition. From a fresh perspective of generalization, Open-MeDe adopts a meta-learning approach to improve known-to-open generalizing and image-to-video debiasing in a cost-effective manner. Specifically, Open-MeDe introduces a cross-batch meta-optimization scheme that explicitly encourages video learners to quickly generalize to arbitrary subsequent data via virtual evaluation, steering a smoother optimization landscape. In effect, the free of CLIP regularization during optimization implicitly mitigates the inherent static bias of the video meta-learner. We further apply self-ensemble over the optimization trajectory to obtain generic optimal parameters that can achieve robust generalization to both in-context and out-of-context novel data. Extensive evaluations show that Open-MeDe not only surpasses state-of-the-art regularization methods tailored for in-context open-vocabulary action recognition but also substantially excels in out-of-context scenarios.Code is released at https://github.com/Mia-YatingYu/Open-MeDe.

</details>

### DanceEditor: Towards Iterative Editable Music-Driven Dance Generation with Open-Vocabulary Descriptions.
- **链接**: [arXiv:2508.17342](https://arxiv.org/abs/2508.17342) · 📚 被引 3
- **作者**: Hengyuan Zhang, Zhe Li, Xingqun Qi, Mengze Li, Muyi Sun, Siye Wang et al.
- **🏷️ 机构**: Peking University, The Hong Kong University of Science and Technology, Beijing University of Posts and Telecommunications
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Generating coherent and diverse human dances from music signals has gained tremendous progress in animating virtual avatars. While existing methods support direct dance synthesis, they fail to recognize that enabling users to edit dance movements is far more practical in real-world choreography scenarios. Moreover, the lack of high-quality dance datasets incorporating iterative editing also limits addressing this challenge. To achieve this goal, we first construct DanceRemix, a large-scale multi-turn editable dance dataset comprising the prompt featuring over 25.3M dance frames and 84.5K pairs. In addition, we propose a novel framework for iterative and editable dance generation coherently aligned with given music signals, namely DanceEditor. Considering the dance motion should be both musical rhythmic and enable iterative editing by user descriptions, our framework is built upon a prediction-then-editing paradigm unifying multi-modal conditions. At the initial prediction stage, our framework improves the authority of generated results by directly modeling dance movements from tailored, aligned music. Moreover, at the subsequent iterative editing stages, we incorporate text descriptions as conditioning information to draw the editable results through a specifically designed Cross-modality Editing Module (CEM). Specifically, CEM adaptively integrates the initial prediction with music and text prompts as temporal motion cues to guide the synthesized sequences. Thereby, the results display music harmonics while preserving fine-grained semantic alignment with text descriptions. Extensive experiments demonstrate that our method outperforms the state-of-the-art models on our newly collected DanceRemix dataset. Code is available at https://lzvsdy.github.io/DanceEditor/.

</details>

### CorrCLIP: Reconstructing Patch Correlations in CLIP for Open-Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.02288) · 📚 被引 4
- **作者**: Dengke Zhang, Fagui Liu, Quan Tang
- **🏷️ 机构**: South China University of Technology, Pengcheng Laboratory
- **会议**: ICCV 2025

### OV3D-CG: Open-Vocabulary 3D Instance Segmentation with Contextual Guidance.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00504)
- **作者**: Mingquan Zhou, Chen He, Ruiping Wang, Xilin Chen
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences,China
- **会议**: ICCV 2025

### Unified Open-World Segmentation with Multi-Modal Prompts.
- **链接**: [arXiv:2510.10524](https://arxiv.org/abs/2510.10524)
- **作者**: Yang Liu, Yufei Yin, Chenchen Jing, Muzhi Zhu, Hao Chen, Yuling Xi et al.
- **🏷️ 机构**: Zhejiang University, Hangzhou Dianzi University, Zhejiang University of Technology
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this work, we present COSINE, a unified open-world segmentation model that consolidates open-vocabulary segmentation and in-context segmentation with multi-modal prompts (e.g., text and image). COSINE exploits foundation models to extract representations for an input image and corresponding multi-modal prompts, and a SegDecoder to align these representations, model their interaction, and obtain masks specified by input prompts across different granularities. In this way, COSINE overcomes architectural discrepancies, divergent learning objectives, and distinct representation learning strategies of previous pipelines for open-vocabulary segmentation and in-context segmentation. Comprehensive experiments demonstrate that COSINE has significant performance improvements in both open-vocabulary and in-context segmentation tasks. Our exploratory analyses highlight that the synergistic collaboration between using visual and textual prompts leads to significantly improved generalization over single-modality approaches.

</details>

### CapeLLM: Support-Free Category-Agnostic Pose Estimation with Multimodal Large Language Models.
- **链接**: [arXiv:2411.06869](https://arxiv.org/abs/2411.06869) · 📚 被引 1
- **作者**: Junho Kim, Hyungjin Chung, Byung-Hoon Kim
- **🏷️ 机构**: EverEx
- **会议**: ICCV 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Category-agnostic pose estimation (CAPE) has traditionally relied on support images with annotated keypoints, a process that is often cumbersome and may fail to fully capture the necessary correspondences across diverse object categories. Recent efforts have explored the use of text queries, leveraging their enhanced stability and generalization capabilities. However, existing approaches often remain constrained by their reliance on support queries, their failure to fully utilize the rich priors embedded in pre-trained large language models, and the limitations imposed by their parametric distribution assumptions. To address these challenges, we introduce CapeLLM, the first multimodal large language model (MLLM) designed for CAPE. Our method only employs query image and detailed text descriptions as an input to estimate category-agnostic keypoints. Our method encompasses effective training strategies and carefully designed instructions for applying the MLLM to CAPE. Moreover, we propose an inference mechanism that further enhances the reasoning process for unseen keypoints. while flexibly modeling their underlying spatial distribution and uncertainty, allowing for adaptive refinement based on contextual cues. We conducted extensive experiments to apply the MLLM to CAPE effectively, focusing not only on the model architecture and prompt design but also on ensuring robustness across input variations. Our approach sets a new state-of-the-art on the MP-100 benchmark in the 1-shot and even 5-shot setting, marking a significant advancement in the field of category-agnostic pose estimation. Code is available at https://github.com/Junhojuno/CapeLLM.

</details>

### MPBR: Multimodal Progressive Bidirectional Reasoning for Open-Set Fine-Grained Recognition.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51701.2025.00127) · 📚 被引 1
- **作者**: Junfu Tan, Peiguang Jing, Yu Zhu, Yu Liu
- **🏷️ 机构**: Tianjin University, Fudan University
- **会议**: ICCV 2025

### Multi-Perspective Data Augmentation for Few-shot Object Detection.
- **链接**: [arXiv:2502.18195](https://arxiv.org/abs/2502.18195)
- **作者**: Anh-Khoa Nguyen Vu, Quoc-Truong Truong, Vinh-Tiep Nguyen, Thanh Duc Ngo, Thanh-Toan Do, Tam V. Nguyen
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent few-shot object detection (FSOD) methods have focused on augmenting synthetic samples for novel classes, show promising results to the rise of diffusion models. However, the diversity of such datasets is often limited in representativeness because they lack awareness of typical and hard samples, especially in the context of foreground and background relationships. To tackle this issue, we propose a Multi-Perspective Data Augmentation (MPAD) framework. In terms of foreground-foreground relationships, we propose in-context learning for object synthesis (ICOS) with bounding box adjustments to enhance the detail and spatial information of synthetic samples. Inspired by the large margin principle, support samples play a vital role in defining class boundaries. Therefore, we design a Harmonic Prompt Aggregation Scheduler (HPAS) to mix prompt embeddings at each time step of the generation process in diffusion models, producing hard novel samples. For foreground-background relationships, we introduce a Background Proposal method (BAP) to sample typical and hard backgrounds. Extensive experiments on multiple FSOD benchmarks demonstrate the effectiveness of our approach. Our framework significantly outperforms traditional methods, achieving an average increase of $17.5\%$ in nAP50 over the baseline on PASCAL VOC. Code is available at https://github.com/nvakhoa/MPAD.

</details>

### Cyclic Contrastive Knowledge Transfer for Open-Vocabulary Object Detection.
- **链接**: [arXiv:2503.11005](https://arxiv.org/abs/2503.11005)
- **作者**: Chuhan Zhang, Chaoyang Zhu, Pingcheng Dong, Long Chen, Dong Zhang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In pursuit of detecting unstinted objects that extend beyond predefined categories, prior arts of open-vocabulary object detection (OVD) typically resort to pretrained vision-language models (VLMs) for base-to-novel category generalization. However, to mitigate the misalignment between upstream image-text pretraining and downstream region-level perception, additional supervisions are indispensable, eg, image-text pairs or pseudo annotations generated via self-training strategies. In this work, we propose CCKT-Det trained without any extra supervision. The proposed framework constructs a cyclic and dynamic knowledge transfer from language queries and visual region features extracted from VLMs, which forces the detector to closely align with the visual-semantic space of VLMs. Specifically, 1) we prefilter and inject semantic priors to guide the learning of queries, and 2) introduce a regional contrastive loss to improve the awareness of queries on novel objects. CCKT-Det can consistently improve performance as the scale of VLMs increases, all while requiring the detector at a moderate level of computation overhead. Comprehensive experimental results demonstrate that our method achieves performance gain of +2.9% and +10.2% AP50 over previous state-of-the-arts on the challenging COCO benchmark, both without and with a stronger teacher model.

</details>

### OVTR: End-to-End Open-Vocabulary Multiple Object Tracking with Transformer.
- **链接**: [arXiv:2503.10616](https://arxiv.org/abs/2503.10616)
- **作者**: Jinyang Li, En Yu, Sijia Chen, Wenbing Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-vocabulary multiple object tracking aims to generalize trackers to unseen categories during training, enabling their application across a variety of real-world scenarios. However, the existing open-vocabulary tracker is constrained by its framework structure, isolated frame-level perception, and insufficient modal interactions, which hinder its performance in open-vocabulary classification and tracking. In this paper, we propose OVTR (End-to-End Open-Vocabulary Multiple Object Tracking with TRansformer), the first end-to-end open-vocabulary tracker that models motion, appearance, and category simultaneously. To achieve stable classification and continuous tracking, we design the CIP (Category Information Propagation) strategy, which establishes multiple high-level category information priors for subsequent frames. Additionally, we introduce a dual-branch structure for generalization capability and deep multimodal interaction, and incorporate protective strategies in the decoder to enhance performance. Experimental results show that our method surpasses previous trackers on the open-vocabulary MOT benchmark while also achieving faster inference speeds and significantly reducing preprocessing requirements. Moreover, the experiment transferring the model to another dataset demonstrates its strong adaptability. Models and code are released at https://github.com/jinyanglii/OVTR.

</details>

### Open-YOLO 3D: Towards Fast and Accurate Open-Vocabulary 3D Instance Segmentation.
- **链接**: [arXiv:2406.02548](https://arxiv.org/abs/2406.02548)
- **作者**: Mohamed El Amine Boudjoghra, Angela Dai, Jean Lahoud, Hisham Cholakkal, Rao Muhammad Anwer, Salman H. Khan et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Recent works on open-vocabulary 3D instance segmentation show strong promise, but at the cost of slow inference speed and high computation requirements. This high computation cost is typically due to their heavy reliance on 3D clip features, which require computationally expensive 2D foundation models like Segment Anything (SAM) and CLIP for multi-view aggregation into 3D. As a consequence, this hampers their applicability in many real-world applications that require both fast and accurate predictions. To this end, we propose a fast yet accurate open-vocabulary 3D instance segmentation approach, named Open-YOLO 3D, that effectively leverages only 2D object detection from multi-view RGB images for open-vocabulary 3D instance segmentation. We address this task by generating class-agnostic 3D masks for objects in the scene and associating them with text prompts. We observe that the projection of class-agnostic 3D point cloud instances already holds instance information; thus, using SAM might only result in redundancy that unnecessarily increases the inference time. We empirically find that a better performance of matching text prompts to 3D masks can be achieved in a faster fashion with a 2D object detector. We validate our Open-YOLO 3D on two benchmarks, ScanNet200 and Replica, under two scenarios: (i) with ground truth masks, where labels are required for given object proposals, and (ii) with class-agnostic 3D proposals generated from a 3D proposal network. Our Open-YOLO 3D achieves state-of-the-art performance on both datasets while obtaining up to $\sim$16$\times$ speedup compared to the best existing method in literature. On ScanNet200 val. set, our Open-YOLO 3D achieves mean average precision (mAP) of 24.7\% while operating at 22 seconds per scene. Code and model are available at github.com/aminebdj/OpenYOLO3D.

</details>

### Revisit the Open Nature of Open Vocabulary Semantic Segmentation.
- **链接**: [出版页](https://openreview.net/forum?id=2vHIHrJAcI)
- **作者**: Qiming Huang, Han Hu, Jianbo Jiao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians.
- **链接**: [arXiv:2504.06003](https://arxiv.org/abs/2504.06003)
- **作者**: Can Zhang, Gim Hee Lee
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> The primary focus of most recent works on open-vocabulary neural fields is extracting precise semantic features from the VLMs and then consolidating them efficiently into a multi-view consistent 3D neural fields representation. However, most existing works over-trusted SAM to regularize image-level CLIP without any further refinement. Moreover, several existing works improved efficiency by dimensionality reduction of semantic features from 2D VLMs before fusing with 3DGS semantic fields, which inevitably leads to multi-view inconsistency. In this work, we propose econSG for open-vocabulary semantic segmentation with 3DGS. Our econSG consists of: 1) A Confidence-region Guided Regularization (CRR) that mutually refines SAM and CLIP to get the best of both worlds for precise semantic features with complete and precise boundaries. 2) A low dimensional contextual space to enforce 3D multi-view consistency while improving computational efficiency by fusing backprojected multi-view 2D features and follow by dimensional reduction directly on the fused 3D features instead of operating on each 2D view separately. Our econSG shows state-of-the-art performance on four benchmark datasets compared to the existing methods. Furthermore, we are also the most efficient training among all the methods.

</details>

### 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds.
- **链接**: [arXiv:2502.20041](https://arxiv.org/abs/2502.20041)
- **作者**: Hengshuo Chu, Xiang Deng, Qi Lv, Xiaoyang Chen, Yinchuan Li, Jianye Hao et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> 3D Affordance detection is a challenging problem with broad applications on various robotic tasks. Existing methods typically formulate the detection paradigm as a label-based semantic segmentation task. This paradigm relies on predefined labels and lacks the ability to comprehend complex natural language, resulting in limited generalization in open-world scene. To address these limitations, we reformulate the traditional affordance detection paradigm into \textit{Instruction Reasoning Affordance Segmentation} (IRAS) task. This task is designed to output a affordance mask region given a query reasoning text, which avoids fixed categories of input labels. We accordingly propose the \textit{3D-AffordanceLLM} (3D-ADLLM), a framework designed for reasoning affordance detection in 3D open-scene. Specifically, 3D-ADLLM introduces large language models (LLMs) to 3D affordance perception with a custom-designed decoder for generating affordance masks, thus achieving open-world reasoning affordance detection. In addition, given the scarcity of 3D affordance datasets for training large models, we seek to extract knowledge from general segmentation data and transfer it to affordance detection. Thus, we propose a multi-stage training strategy that begins with a novel pre-training task, i.e., \textit{Referring Object Part Segmentation}~(ROPS). This stage is designed to equip the model with general recognition and segmentation capabilities at the object-part level. Then followed by fine-tuning with the IRAS task, 3D-ADLLM obtains the reasoning ability for affordance detection. In summary, 3D-ADLLM leverages the rich world knowledge and human-object interaction reasoning ability of LLMs, achieving approximately an 8\% improvement in mIoU on open-vocabulary affordance detection tasks.

</details>

### Class Distribution-induced Attention Map for Open-vocabulary Semantic Segmentations.
- **链接**: [出版页](https://openreview.net/forum?id=CMqOfvD3tO)
- **作者**: Dong Un Kang, Hayeon Kim, Se Young Chun
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### A Simple Framework for Open-Vocabulary Zero-Shot Segmentation.
- **链接**: [arXiv:2406.16085](https://arxiv.org/abs/2406.16085)
- **作者**: Thomas Stegmüller, Tim Lebailly, Nikola Dukic, Behzad Bozorgtabar, Tinne Tuytelaars, Jean-Philippe Thiran
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Zero-shot classification capabilities naturally arise in models trained within a vision-language contrastive framework. Despite their classification prowess, these models struggle in dense tasks like zero-shot open-vocabulary segmentation. This deficiency is often attributed to the absence of localization cues in captions and the intertwined nature of the learning process, which encompasses both image representation learning and cross-modality alignment. To tackle these issues, we propose SimZSS, a Simple framework for open-vocabulary Zero-Shot Segmentation. The method is founded on two key principles: i) leveraging frozen vision-only models that exhibit spatial awareness while exclusively aligning the text encoder and ii) exploiting the discrete nature of text and linguistic knowledge to pinpoint local concepts within captions. By capitalizing on the quality of the visual representations, our method requires only image-caption pairs datasets and adapts to both small curated and large-scale noisy datasets. When trained on COCO Captions across 8 GPUs, SimZSS achieves state-of-the-art results on 7 out of 8 benchmark datasets in less than 15 minutes.

</details>

### Open-Vocabulary Customization from CLIP via Data-Free Knowledge Distillation.
- **链接**: [出版页](https://openreview.net/forum?id=1aF2D2CPHi)
- **作者**: Yongxian Wei, Zixuan Hu, Li Shen, Zhenyi Wang, Chun Yuan, Dacheng Tao
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

### ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination.
- **链接**: [arXiv:2410.09874](https://arxiv.org/abs/2410.09874)
- **作者**: Xinxin Zhao, Wenzhe Cai, Likun Tang, Teng Wang
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Visual navigation is an essential skill for home-assistance robots, providing the object-searching ability to accomplish long-horizon daily tasks. Many recent approaches use Large Language Models (LLMs) for commonsense inference to improve exploration efficiency. However, the planning process of LLMs is limited within texts and it is difficult to represent the spatial occupancy and geometry layout only by texts. Both are important for making rational navigation decisions. In this work, we seek to unleash the spatial perception and planning ability of Vision-Language Models (VLMs), and explore whether the VLM, with only on-board camera captured RGB/RGB-D stream inputs, can efficiently finish the visual navigation tasks in a mapless manner. We achieve this by developing the imagination-powered navigation framework ImagineNav, which imagines the future observation images at valuable robot views and translates the complex navigation planning process into a rather simple best-view image selection problem for VLM. To generate appropriate candidate robot views for imagination, we introduce the Where2Imagine module, which is distilled to align with human navigation habits. Finally, to reach the VLM preferred views, an off-the-shelf point-goal navigation policy is utilized. Empirical experiments on the challenging open-vocabulary object navigation benchmarks demonstrates the superiority of our proposed system.

</details>

### Towards Robust Multimodal Open-set Test-time Adaptation via Adaptive Entropy-aware Optimization.
- **链接**: [arXiv:2501.13924](https://arxiv.org/abs/2501.13924)
- **作者**: Hao Dong, Eleni N. Chatzi, Olga Fink
- **🏷️ 机构**: （机构待查）
- **会议**: ICLR 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Test-time adaptation (TTA) has demonstrated significant potential in addressing distribution shifts between training and testing data. Open-set test-time adaptation (OSTTA) aims to adapt a source pre-trained model online to an unlabeled target domain that contains unknown classes. This task becomes more challenging when multiple modalities are involved. Existing methods have primarily focused on unimodal OSTTA, often filtering out low-confidence samples without addressing the complexities of multimodal data. In this work, we present Adaptive Entropy-aware Optimization (AEO), a novel framework specifically designed to tackle Multimodal Open-set Test-time Adaptation (MM-OSTTA) for the first time. Our analysis shows that the entropy difference between known and unknown samples in the target domain strongly correlates with MM-OSTTA performance. To leverage this, we propose two key components: Unknown-aware Adaptive Entropy Optimization (UAE) and Adaptive Modality Prediction Discrepancy Optimization (AMP). These components enhance the ability of model to distinguish unknown class samples during online adaptation by amplifying the entropy difference between known and unknown samples. To thoroughly evaluate our proposed methods in the MM-OSTTA setting, we establish a new benchmark derived from existing datasets. This benchmark includes two downstream tasks and incorporates five modalities. Extensive experiments across various domain shift situations demonstrate the efficacy and versatility of the AEO framework. Additionally, we highlight the strong performance of AEO in long-term and continual MM-OSTTA settings, both of which are challenging and highly relevant to real-world applications. Our source code is available at https://github.com/donghao51/AEO.

</details>

### OV-MER: Towards Open-Vocabulary Multimodal Emotion Recognition.
- **链接**: [出版页](https://proceedings.mlr.press/v267/lian25b.html)
- **作者**: Zheng Lian, Haiyang Sun, Licai Sun, Haoyu Chen, Lan Chen, Hao Gu et al.
- **🏷️ 机构**: （机构待查）
- **会议**: ICML 2025

### GUIDED: Granular Understanding via Identification, Detection, and Discrimination for Fine-Grained Open-Vocabulary Object Detection.
- **链接**: [arXiv:2603.27014](https://arxiv.org/abs/2603.27014)
- **作者**: Jiaming Li, Zhijia Liang, Weikai Chen, Lin Ma, Guanbin Li
- **🏷️ 机构**: SUN YAT-SEN UNIVERSITY, Zhengzhou University, Tencent AI Lab
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Fine-grained open-vocabulary object detection (FG-OVD) aims to detect novel object categories described by attribute-rich texts. While existing open-vocabulary detectors show promise at the base-category level, they underperform in fine-grained settings due to the semantic entanglement of subjects and attributes in pretrained vision-language model (VLM) embeddings -- leading to over-representation of attributes, mislocalization, and semantic drift in embedding space. We propose GUIDED, a decomposition framework specifically designed to address the semantic entanglement between subjects and attributes in fine-grained prompts. By separating object localization and fine-grained recognition into distinct pathways, HUIDED aligns each subtask with the module best suited for its respective roles. Specifically, given a fine-grained class name, we first use a language model to extract a coarse-grained subject and its descriptive attributes. Then the detector is guided solely by the subject embedding, ensuring stable localization unaffected by irrelevant or overrepresented attributes. To selectively retain helpful attributes, we introduce an attribute embedding fusion module that incorporates attribute information into detection queries in an attention-based manner. This mitigates over-representation while preserving discriminative power. Finally, a region-level attribute discrimination module compares each detected region against full fine-grained class names using a refined vision-language model with a projection head for improved alignment. Extensive experiments on FG-OVD and 3F-OVD benchmarks show that GUIDED achieves new state-of-the-art results, demonstrating the benefits of disentangled modeling and modular optimization. Our code will be released at https://github.com/lijm48/GUIDED.

</details>

### DitHub: A Modular Framework for Incremental Open-Vocabulary Object Detection.
- **链接**: [arXiv:2503.09271](https://arxiv.org/abs/2503.09271)
- **作者**: Chiara Cappellino, Gianluca Mancusi, Matteo Mosconi, Angelo Porrello, Simone Calderara, Rita Cucchiara
- **🏷️ 机构**: University of Modena and Reggio Emilia, Mercuria, University of Modena and Reggio Emilia, Italy
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-Vocabulary object detectors can generalize to an unrestricted set of categories through simple textual prompting. However, adapting these models to rare classes or reinforcing their abilities on multiple specialized domains remains essential. While recent methods rely on monolithic adaptation strategies with a single set of weights, we embrace modular deep learning. We introduce DitHub, a framework designed to build and maintain a library of efficient adaptation modules. Inspired by Version Control Systems, DitHub manages expert modules as branches that can be fetched and merged as needed. This modular approach allows us to conduct an in-depth exploration of the compositional properties of adaptation modules, marking the first such study in Object Detection. Our method achieves state-of-the-art performance on the ODinW-13 benchmark and ODinW-O, a newly introduced benchmark designed to assess class reappearance. For more details, visit our project page: https://aimagelab.github.io/DitHub/

</details>

### VL-SAM-V2: Open-World Object Detection with General and Specific Query Fusion.
- **链接**: [arXiv:2505.18986](https://arxiv.org/abs/2505.18986)
- **作者**: Zhiwei Lin, Yongtao Wang
- **🏷️ 机构**: Peking University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Current perception models have achieved remarkable success by leveraging large-scale labeled datasets, but still face challenges in open-world environments with novel objects. To address this limitation, researchers introduce open-set perception models to detect or segment arbitrary test-time user-input categories. However, open-set models rely on human involvement to provide predefined object categories as input during inference. More recently, researchers have framed a more realistic and challenging task known as open-ended perception that aims to discover unseen objects without requiring any category-level input from humans at inference time. Nevertheless, open-ended models suffer from low performance compared to open-set models. In this paper, we present VL-SAM-V2, an open-world object detection framework that is capable of discovering unseen objects while achieving favorable performance. To achieve this, we combine queries from open-set and open-ended models and propose a general and specific query fusion module to allow different queries to interact. By adjusting queries from open-set models, we enable VL-SAM-V2 to be evaluated in the open-set or open-ended mode. In addition, to learn more diverse queries, we introduce ranked learnable queries to match queries with proposals from open-ended models by sorting. Moreover, we design a denoising point training strategy to facilitate the training process. Experimental results on LVIS show that our method surpasses the previous open-set and open-ended methods, especially on rare objects.

</details>

### Looking Beyond the Known: Towards a Data Discovery Guided Open-World Object Detection.
- **链接**: [arXiv:2510.00303](https://arxiv.org/abs/2510.00303) · 📚 被引 1
- **作者**: Anay Majee, Amitesh Gangrade, Rishabh Iyer
- **🏷️ 机构**: The University of Texas at Dallas, University of Texas at Dallas, University of Texas, Dallas
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Open-World Object Detection (OWOD) enriches traditional object detectors by enabling continual discovery and integration of unknown objects via human guidance. However, existing OWOD approaches frequently suffer from semantic confusion between known and unknown classes, alongside catastrophic forgetting, leading to diminished unknown recall and degraded known-class accuracy. To overcome these challenges, we propose Combinatorial Open-World Detection (CROWD), a unified framework reformulating unknown object discovery and adaptation as an interwoven combinatorial (set-based) data-discovery (CROWD-Discover) and representation learning (CROWD-Learn) task. CROWD-Discover strategically mines unknown instances by maximizing Submodular Conditional Gain (SCG) functions, selecting representative examples distinctly dissimilar from known objects. Subsequently, CROWD-Learn employs novel combinatorial objectives that jointly disentangle known and unknown representations while maintaining discriminative coherence among known classes, thus mitigating confusion and forgetting. Extensive evaluations on OWOD benchmarks illustrate that CROWD achieves improvements of 2.83% and 2.05% in known-class accuracy on M-OWODB and S-OWODB, respectively, and nearly 2.4x unknown recall compared to leading baselines.

</details>

### OVS Meets Continual Learning: Towards Sustainable Open-Vocabulary Segmentation.
- **链接**: [出版页](http://papers.nips.cc/paper_files/paper/2025/hash/184cfed554856b4812b19cd0235a0f6a-Abstract-Conference.html)
- **作者**: Dongjun Hwang, Yejin Kim, Minyoung Lee, Seong Joon Oh, Junsuk Choe
- **🏷️ 机构**: Sogang University, University of Tübingen
- **会议**: NeurIPS 2025

### OpenHOI: Open-World Hand-Object Interaction Synthesis with Multimodal Large Language Model.
- **链接**: [arXiv:2505.18947](https://arxiv.org/abs/2505.18947)
- **作者**: Zhenhao Zhang, Ye Shi, Lingxiao Yang, Suting Ni, Qi Ye, Jingya Wang
- **🏷️ 机构**: ShanghaiTech University, Zhejiang University
- **会议**: NeurIPS 2025

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Understanding and synthesizing realistic 3D hand-object interactions (HOI) is critical for applications ranging from immersive AR/VR to dexterous robotics. Existing methods struggle with generalization, performing well on closed-set objects and predefined tasks but failing to handle unseen objects or open-vocabulary instructions. We introduce OpenHOI, the first framework for open-world HOI synthesis, capable of generating long-horizon manipulation sequences for novel objects guided by free-form language commands. Our approach integrates a 3D Multimodal Large Language Model (MLLM) fine-tuned for joint affordance grounding and semantic task decomposition, enabling precise localization of interaction regions (e.g., handles, buttons) and breakdown of complex instructions (e.g., "Find a water bottle and take a sip") into executable sub-tasks. To synthesize physically plausible interactions, we propose an affordance-driven diffusion model paired with a training-free physics refinement stage that minimizes penetration and optimizes affordance alignment. Evaluations across diverse scenarios demonstrate OpenHOI's superiority over state-of-the-art methods in generalizing to novel object categories, multi-stage tasks, and complex language instructions. Our project page at \href{https://openhoi.github.io}

</details>
<!-- COMPLETE v1 papers=115 -->
