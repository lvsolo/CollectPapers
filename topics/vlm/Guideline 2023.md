# VLM — 2023 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 31 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: 

### CLIP2Point: Transfer CLIP to Point Cloud Classification with Image-Depth Pre-Training.
- **链接**: [arXiv:2210.01055](https://arxiv.org/abs/2210.01055) · 📚 被引 140
- **作者**: Tianyu Huang, Bowen Dong, Yunhan Yang, Xiaoshui Huang, Rynson W. H. Lau, Wanli Ouyang et al.
- **🏷️ 机构**: Harbin Institute of Technology, Shanghai AI Laboratory, City University of Hong Kong
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-training across 3D vision and language remains under development because of limited training data. Recent works attempt to transfer vision-language pre-training models to 3D vision. PointCLIP converts point cloud data to multi-view depth maps, adopting CLIP for shape classification. However, its performance is restricted by the domain gap between rendered depth maps and images, as well as the diversity of depth distributions. To address this issue, we propose CLIP2Point, an image-depth pre-training method by contrastive learning to transfer CLIP to the 3D domain, and adapt it to point cloud classification. We introduce a new depth rendering setting that forms a better visual effect, and then render 52,460 pairs of images and depth maps from ShapeNet for pre-training. The pre-training scheme of CLIP2Point combines cross-modality learning to enforce the depth features for capturing expressive visual and textual features and intra-modality learning to enhance the invariance of depth aggregation. Additionally, we propose a novel Dual-Path Adapter (DPA) module, i.e., a dual-path structure with simplified adapters for few-shot learning. The dual-path structure allows the joint use of CLIP and CLIP2Point, and the simplified adapter can well fit few-shot tasks without post-search. Experimental results show that CLIP2Point is effective in transferring CLIP knowledge to 3D vision. Our CLIP2Point outperforms PointCLIP and other self-supervised 3D networks, achieving state-of-the-art results on zero-shot and few-shot classification.

</details>

### Bird's-Eye-View Scene Graph for Vision-Language Navigation.
- **链接**: [arXiv:2308.04758](https://arxiv.org/abs/2308.04758)
- **作者**: Rui Liu, Xiaohan Wang, Wenguan Wang, Yi Yang
- **🏷️ 机构**: （机构待查）
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language navigation (VLN), which entails an agent to navigate 3D environments following human instructions, has shown great advances. However, current agents are built upon panoramic observations, which hinders their ability to perceive 3D scene geometry and easily leads to ambiguous selection of panoramic view. To address these limitations, we present a BEV Scene Graph (BSG), which leverages multi-step BEV representations to encode scene layouts and geometric cues of indoor environment under the supervision of 3D detection. During navigation, BSG builds a local BEV representation at each step and maintains a BEV-based global scene map, which stores and organizes all the online collected local BEV representations according to their topological relations. Based on BSG, the agent predicts a local BEV grid-level decision score and a global graph-level decision score, combined with a sub-view selection score on panoramic views, for more accurate action prediction. Our approach significantly outperforms state-of-the-art methods on REVERIE, R2R, and R4R, showing the potential of BEV perception in VLN.

</details>

### PointCLIP V2: Prompting CLIP and GPT for Powerful 3D Open-world Learning.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00249) · 📚 被引 181
- **作者**: Xiangyang Zhu, Renrui Zhang, Bowei He, Ziyu Guo, Ziyao Zeng, Zipeng Qin et al.
- **🏷️ 机构**: City University of Hong Kong, The Chinese University of Hong Kong, Yale University
- **会议**: ICCV 2023

### CLIP-FO3D: Learning Free Open-world 3D Scene Representations from 2D Dense CLIP.
- **链接**: [arXiv:2303.04748](https://arxiv.org/abs/2303.04748) · 📚 被引 66
- **作者**: Junbo Zhang, Runpei Dong, Kaisheng Ma
- **🏷️ 机构**: Tsinghua University, Xi&#x2019;an Jiaotong University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Training a 3D scene understanding model requires complicated human annotations, which are laborious to collect and result in a model only encoding close-set object semantics. In contrast, vision-language pre-training models (e.g., CLIP) have shown remarkable open-world reasoning properties. To this end, we propose directly transferring CLIP's feature space to 3D scene understanding model without any form of supervision. We first modify CLIP's input and forwarding process so that it can be adapted to extract dense pixel features for 3D scene contents. We then project multi-view image features to the point cloud and train a 3D scene understanding model with feature distillation. Without any annotations or additional training, our model achieves promising annotation-free semantic segmentation results on open-vocabulary semantics and long-tailed concepts. Besides, serving as a cross-modal pre-training framework, our method can be used to improve data efficiency during fine-tuning. Our model outperforms previous SOTA methods in various zero-shot and data-efficient learning benchmarks. Most importantly, our model successfully inherits CLIP's rich-structured knowledge, allowing 3D scene understanding models to recognize not only object concepts but also open-world semantics.

</details>

### CLIPN for Zero-Shot OOD Detection: Teaching CLIP to Say No.
- **链接**: [arXiv:2308.12213](https://arxiv.org/abs/2308.12213) · [代码](https://github.com/xmed-lab/CLIPN) · 📚 被引 105
- **作者**: Hualiang Wang, Yi Li, Huifeng Yao, Xiaomeng Li
- **🏷️ 机构**: The Hong Kong University of Science and Technology,Department of Electronic and Computer Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Out-of-distribution (OOD) detection refers to training the model on an in-distribution (ID) dataset to classify whether the input images come from unknown classes. Considerable effort has been invested in designing various OOD detection methods based on either convolutional neural networks or transformers. However, zero-shot OOD detection methods driven by CLIP, which only require class names for ID, have received less attention. This paper presents a novel method, namely CLIP saying no (CLIPN), which empowers the logic of saying no within CLIP. Our key motivation is to equip CLIP with the capability of distinguishing OOD and ID samples using positive-semantic prompts and negation-semantic prompts. Specifically, we design a novel learnable no prompt and a no text encoder to capture negation semantics within images. Subsequently, we introduce two loss functions: the image-text binary-opposite loss and the text semantic-opposite loss, which we use to teach CLIPN to associate images with no prompts, thereby enabling it to identify unknown samples. Furthermore, we propose two threshold-free inference algorithms to perform OOD detection by utilizing negation semantics from no prompts and the text encoder. Experimental results on 9 benchmark datasets (3 ID datasets and 6 OOD datasets) for the OOD detection task demonstrate that CLIPN, based on ViT-B-16, outperforms 7 well-used algorithms by at least 2.34% and 11.64% in terms of AUROC and FPR95 for zero-shot OOD detection on ImageNet-1K. Our CLIPN can serve as a solid foundation for effectively leveraging CLIP in downstream OOD tasks. The code is available on https://github.com/xmed-lab/CLIPN.

</details>

### VL-Match: Enhancing Vision-Language Pretraining with Token-Level and Instance-Level Matching.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00244) · 📚 被引 4
- **作者**: Junyu Bi, Daixuan Cheng, Ping Yao, Bochen Pang, Yuefeng Zhan, Chuanguang Yang et al.
- **🏷️ 机构**: Institute of Computing Technology,Chinese Academy of Sciences,Beijing,China, Microsoft Corporation
- **会议**: ICCV 2023

### Distribution-Aware Prompt Tuning for Vision-Language Models.
- **链接**: [arXiv:2309.03406](https://arxiv.org/abs/2309.03406) · [代码](https://github.com/mlvlab/DAPT) · 📚 被引 50
- **作者**: Eulrang Cho, Jooyeon Kim, Hyunwoo J. Kim
- **🏷️ 机构**: Korea University,Department of Computer Science and Engineering
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models (VLMs) have shown impressive performance on various downstream tasks by utilizing knowledge learned from large data. In general, the performance of VLMs on target tasks can be further improved by prompt tuning, which adds context to the input image or text. By leveraging data from target tasks, various prompt-tuning methods have been studied in the literature. A key to prompt tuning is the feature space alignment between two modalities via learnable vectors with model parameters fixed. We observed that the alignment becomes more effective when embeddings of each modality are `well-arranged' in the latent space. Inspired by this observation, we proposed distribution-aware prompt tuning (DAPT) for vision-language models, which is simple yet effective. Specifically, the prompts are learned by maximizing inter-dispersion, the distance between classes, as well as minimizing the intra-dispersion measured by the distance between embeddings from the same class. Our extensive experiments on 11 benchmark datasets demonstrate that our method significantly improves generalizability. The code is available at https://github.com/mlvlab/DAPT.

</details>

### Knowledge-Aware Prompt Tuning for Generalizable Vision-Language Models.
- **链接**: [arXiv:2308.11186](https://arxiv.org/abs/2308.11186) · 📚 被引 44
- **作者**: Baoshuo Kan, Teng Wang, Wenpeng Lu, Xiantong Zhen, Weili Guan, Feng Zheng
- **🏷️ 机构**: Qilu University of Technology (Shandong Academy of Sciences), Southern University of Science and Technology, United Imaging Healthcare
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Pre-trained vision-language models, e.g., CLIP, working with manually designed prompts have demonstrated great capacity of transfer learning. Recently, learnable prompts achieve state-of-the-art performance, which however are prone to overfit to seen classes, failing to generalize to unseen classes. In this paper, we propose a Knowledge-Aware Prompt Tuning (KAPT) framework for vision-language models. Our approach takes inspiration from human intelligence in which external knowledge is usually incorporated into recognizing novel categories of objects. Specifically, we design two complementary types of knowledge-aware prompts for the text encoder to leverage the distinctive characteristics of category-related external knowledge. The discrete prompt extracts the key information from descriptions of an object category, and the learned continuous prompt captures overall contexts. We further design an adaptation head for the visual encoder to aggregate salient attentive visual cues, which establishes discriminative and task-aware visual representations. We conduct extensive experiments on 11 widely-used benchmark datasets and the results verify the effectiveness in few-shot image classification, especially in generalizing to unseen categories. Compared with the state-of-the-art CoCoOp method, KAPT exhibits favorable performance and achieves an absolute gain of 3.22% on new classes and 2.57% in terms of harmonic mean.

</details>

### Distilling Large Vision-Language Model with Out-of-Distribution Generalizability.
- **链接**: [arXiv:2307.03135](https://arxiv.org/abs/2307.03135) · [代码](https://github.com/xuanlinli17/large_vlm_distillation_ood) · 📚 被引 28
- **作者**: Xuanlin Li, Yunhao Fang, Minghua Liu, Zhan Ling, Zhuowen Tu, Hao Su
- **🏷️ 机构**: UC San Diego
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Large vision-language models have achieved outstanding performance, but their size and computational requirements make their deployment on resource-constrained devices and time-sensitive tasks impractical. Model distillation, the process of creating smaller, faster models that maintain the performance of larger models, is a promising direction towards the solution. This paper investigates the distillation of visual representations in large teacher vision-language models into lightweight student models using a small- or mid-scale dataset. Notably, this study focuses on open-vocabulary out-of-distribution (OOD) generalization, a challenging problem that has been overlooked in previous model distillation literature. We propose two principles from vision and language modality perspectives to enhance student's OOD generalization: (1) by better imitating teacher's visual representation space, and carefully promoting better coherence in vision-language alignment with the teacher; (2) by enriching the teacher's language representations with informative and finegrained semantic attributes to effectively distinguish between different labels. We propose several metrics and conduct extensive experiments to investigate their techniques. The results demonstrate significant improvements in zero-shot and few-shot student performance on open-vocabulary out-of-distribution classification, highlighting the effectiveness of our proposed approaches. Poster: https://xuanlinli17.github.io/pdfs/iccv23_large_vlm_distillation_poster.pdf Code: https://github.com/xuanlinli17/large_vlm_distillation_ood

</details>

### Gradient-Regulated Meta-Prompt Learning for Generalizable Vision-Language Models.
- **链接**: [arXiv:2303.06571](https://arxiv.org/abs/2303.06571) · 📚 被引 24
- **作者**: Juncheng Li, Minghe Gao, Longhui Wei, Siliang Tang, Wenqiao Zhang, Mengze Li et al.
- **🏷️ 机构**: Zhejiang University, Huawei Cloud, National University of Singapore
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt tuning, a recently emerging paradigm, enables the powerful vision-language pre-training models to adapt to downstream tasks in a parameter -- and data -- efficient way, by learning the ``soft prompts'' to condition frozen pre-training models. Though effective, it is particularly problematic in the few-shot scenario, where prompt tuning performance is sensitive to the initialization and requires a time-consuming process to find a good initialization, thus restricting the fast adaptation ability of the pre-training models. In addition, prompt tuning could undermine the generalizability of the pre-training models, because the learnable prompt tokens are easy to overfit to the limited training samples. To address these issues, we introduce a novel Gradient-RegulAted Meta-prompt learning (GRAM) framework that jointly meta-learns an efficient soft prompt initialization for better adaptation and a lightweight gradient regulating function for strong cross-domain generalizability in a meta-learning paradigm using only the unlabeled image-text pre-training data. Rather than designing a specific prompt tuning method, our GRAM can be easily incorporated into various prompt tuning methods in a model-agnostic way, and comprehensive experiments show that GRAM brings about consistent improvement for them in several settings (i.e., few-shot learning, cross-domain generalization, cross-dataset generalization, etc.) over 11 datasets. Further, experiments show that GRAM enables the orthogonal methods of textual and visual prompt tuning to work in a mutually-enhanced way, offering better generalizability beyond the uni-modal prompt tuning methods.

</details>

### Black Box Few-Shot Adaptation for Vision-Language models.
- **链接**: [arXiv:2304.01752](https://arxiv.org/abs/2304.01752) · 📚 被引 35
- **作者**: Yassine Ouali, Adrian Bulat, Brais Martínez, Georgios Tzimiropoulos
- **🏷️ 机构**: Samsung AI Cambridge
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-Language (V-L) models trained with contrastive learning to align the visual and language modalities have been shown to be strong few-shot learners. Soft prompt learning is the method of choice for few-shot downstream adaptation aiming to bridge the modality gap caused by the distribution shift induced by the new domain. While parameter-efficient, prompt learning still requires access to the model weights and can be computationally infeasible for large models with billions of parameters. To address these shortcomings, in this work, we describe a black-box method for V-L few-shot adaptation that (a) operates on pre-computed image and text features and hence works without access to the model's weights, (b) it is orders of magnitude faster at training time, (c) it is amenable to both supervised and unsupervised training, and (d) it can be even used to align image and text features computed from uni-modal models. To achieve this, we propose Linear Feature Alignment (LFA), a simple linear approach for V-L re-alignment in the target domain. LFA is initialized from a closed-form solution to a least-squares problem and then it is iteratively updated by minimizing a re-ranking loss. Despite its simplicity, our approach can even surpass soft-prompt learning methods as shown by extensive experiments on 11 image and 2 video datasets.

</details>

### Perceptual Grouping in Contrastive Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.00513) · 📚 被引 49
- **作者**: Kanchana Ranasinghe, Brandon McKinzie, Sachin Ravi, Yinfei Yang, Alexander Toshev, Jonathon Shlens
- **🏷️ 机构**: Apple
- **会议**: ICCV 2023

### LoGoPrompt: Synthetic Text Images Can Be Good Visual Prompts for Vision-Language Models.
- **链接**: [arXiv:2309.01155](https://arxiv.org/abs/2309.01155) · 📚 被引 22
- **作者**: Cheng Shi, Sibei Yang
- **🏷️ 机构**: ShanghaiTech University,School of Information Science and Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt engineering is a powerful tool used to enhance the performance of pre-trained models on downstream tasks. For example, providing the prompt "Let's think step by step" improved GPT-3's reasoning accuracy to 63% on MutiArith while prompting "a photo of" filled with a class name enables CLIP to achieve $80$\% zero-shot accuracy on ImageNet. While previous research has explored prompt learning for the visual modality, analyzing what constitutes a good visual prompt specifically for image recognition is limited. In addition, existing visual prompt tuning methods' generalization ability is worse than text-only prompting tuning. This paper explores our key insight: synthetic text images are good visual prompts for vision-language models! To achieve that, we propose our LoGoPrompt, which reformulates the classification objective to the visual prompt selection and addresses the chicken-and-egg challenge of first adding synthetic text images as class-wise visual prompts or predicting the class first. Without any trainable visual prompt parameters, experimental results on 16 datasets demonstrate that our method consistently outperforms state-of-the-art methods in few-shot learning, base-to-new generalization, and domain generalization.

</details>

### Linear Spaces of Meanings: Compositional Structures in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCV51070.2023.01412) · 📚 被引 17
- **作者**: Matthew Trager, Pramuditha Perera, Luca Zancato, Alessandro Achille, Parminder Bhatia, Stefano Soatto
- **🏷️ 机构**: AWS AI Labs
- **会议**: ICCV 2023

### SuS-X: Training-Free Name-Only Transfer of Vision-Language Models.
- **链接**: [arXiv:2211.16198](https://arxiv.org/abs/2211.16198) · [代码](https://github.com/vishaal27/SuS-X) · 📚 被引 80
- **作者**: Vishaal Udandarao, Ankush Gupta, Samuel Albanie
- **🏷️ 机构**: University of Cambridge, DeepMind,London
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Contrastive Language-Image Pre-training (CLIP) has emerged as a simple yet effective way to train large-scale vision-language models. CLIP demonstrates impressive zero-shot classification and retrieval on diverse downstream tasks. However, to leverage its full potential, fine-tuning still appears to be necessary. Fine-tuning the entire CLIP model can be resource-intensive and unstable. Moreover, recent methods that aim to circumvent this need for fine-tuning still require access to images from the target distribution. In this paper, we pursue a different approach and explore the regime of training-free "name-only transfer" in which the only knowledge we possess about the downstream task comprises the names of downstream target categories. We propose a novel method, SuS-X, consisting of two key building blocks -- SuS and TIP-X, that requires neither intensive fine-tuning nor costly labelled data. SuS-X achieves state-of-the-art zero-shot classification results on 19 benchmark datasets. We further show the utility of TIP-X in the training-free few-shot setting, where we again achieve state-of-the-art results over strong training-free baselines. Code is available at https://github.com/vishaal27/SuS-X.

</details>

### Dreamwalker: Mental Planning for Continuous Vision-Language Navigation.
- **链接**: [arXiv:2308.07498](https://arxiv.org/abs/2308.07498) · 📚 被引 43
- **作者**: Hanqing Wang, Wei Liang, Luc Van Gool, Wenguan Wang
- **🏷️ 机构**: Beijing Institute of Technology, ETH Zurich,Computer Vision Lab, Zhejiang University,ReLER, CCAI
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> VLN-CE is a recently released embodied task, where AI agents need to navigate a freely traversable environment to reach a distant target location, given language instructions. It poses great challenges due to the huge space of possible strategies. Driven by the belief that the ability to anticipate the consequences of future actions is crucial for the emergence of intelligent and interpretable planning behavior, we propose DREAMWALKER -- a world model based VLN-CE agent. The world model is built to summarize the visual, topological, and dynamic properties of the complicated continuous environment into a discrete, structured, and compact representation. DREAMWALKER can simulate and evaluate possible plans entirely in such internal abstract world, before executing costly actions. As opposed to existing model-free VLN-CE agents simply making greedy decisions in the real world, which easily results in shortsighted behaviors, DREAMWALKER is able to make strategic planning through large amounts of ``mental experiments.'' Moreover, the imagined future scenarios reflect our agent's intention, making its decision-making process more transparent. Extensive experiments and ablation studies on VLN-CE dataset confirm the effectiveness of the proposed approach and outline fruitful directions for future work.

</details>

### Equivariant Similarity for Vision-Language Foundation Models.
- **链接**: [arXiv:2303.14465](https://arxiv.org/abs/2303.14465) · [代码](https://github.com/Wangt-CN/EqBen) · 📚 被引 20
- **作者**: Tan Wang, Kevin Lin, Linjie Li, Chung-Ching Lin, Zhengyuan Yang, Hanwang Zhang et al.
- **🏷️ 机构**: Nanyang Technological University, Microsoft
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> This study explores the concept of equivariance in vision-language foundation models (VLMs), focusing specifically on the multimodal similarity function that is not only the major training objective but also the core delivery to support downstream tasks. Unlike the existing image-text similarity objective which only categorizes matched pairs as similar and unmatched pairs as dissimilar, equivariance also requires similarity to vary faithfully according to the semantic changes. This allows VLMs to generalize better to nuanced and unseen multimodal compositions. However, modeling equivariance is challenging as the ground truth of semantic change is difficult to collect. For example, given an image-text pair about a dog, it is unclear to what extent the similarity changes when the pixel is changed from dog to cat? To this end, we propose EqSim, a regularization loss that can be efficiently calculated from any two matched training pairs and easily pluggable into existing image-text retrieval fine-tuning. Meanwhile, to further diagnose the equivariance of VLMs, we present a new challenging benchmark EqBen. Compared to the existing evaluation sets, EqBen is the first to focus on "visual-minimal change". Extensive experiments show the lack of equivariance in current VLMs and validate the effectiveness of EqSim. Code is available at https://github.com/Wangt-CN/EqBen.

</details>

### Why Is Prompt Tuning for Vision-Language Models Robust to Noisy Labels?
- **链接**: [arXiv:2307.11978](https://arxiv.org/abs/2307.11978) · [代码](https://github.com/CEWu/PTNL) · 📚 被引 15
- **作者**: Cheng-En Wu, Yu Tian, Haichao Yu, Heng Wang, Pedro Morgado, Yu Hen Hu et al.
- **🏷️ 机构**: University of Wisconsin-Madison, ByteDance Inc.
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Vision-language models such as CLIP learn a generic text-image embedding from large-scale training data. A vision-language model can be adapted to a new classification task through few-shot prompt tuning. We find that such a prompt tuning process is highly robust to label noises. This intrigues us to study the key reasons contributing to the robustness of the prompt tuning paradigm. We conducted extensive experiments to explore this property and find the key factors are: 1) the fixed classname tokens provide a strong regularization to the optimization of the model, reducing gradients induced by the noisy samples; 2) the powerful pre-trained image-text embedding that is learned from diverse and generic web data provides strong prior knowledge for image classification. Further, we demonstrate that noisy zero-shot predictions from CLIP can be used to tune its own prompt, significantly enhancing prediction accuracy in the unsupervised setting. The code is available at https://github.com/CEWu/PTNL.

</details>

### Regularized Mask Tuning: Uncovering Hidden Knowledge in Pre-trained Vision-Language Models.
- **链接**: [arXiv:2307.15049](https://arxiv.org/abs/2307.15049) · 📚 被引 7
- **作者**: Kecheng Zheng, Wei Wu, Ruili Feng, Kai Zhu, Jiawei Liu, Deli Zhao et al.
- **🏷️ 机构**: Zhejiang University,State Key Lab of CAD&#x0026;CG, USTC, Alibaba Group
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Prompt tuning and adapter tuning have shown great potential in transferring pre-trained vision-language models (VLMs) to various downstream tasks. In this work, we design a new type of tuning method, termed as regularized mask tuning, which masks the network parameters through a learnable selection. Inspired by neural pathways, we argue that the knowledge required by a downstream task already exists in the pre-trained weights but just gets concealed in the upstream pre-training stage. To bring the useful knowledge back into light, we first identify a set of parameters that are important to a given downstream task, then attach a binary mask to each parameter, and finally optimize these masks on the downstream data with the parameters frozen. When updating the mask, we introduce a novel gradient dropout strategy to regularize the parameter selection, in order to prevent the model from forgetting old knowledge and overfitting the downstream data. Experimental results on 11 datasets demonstrate the consistent superiority of our method over previous alternatives. It is noteworthy that we manage to deliver 18.73% performance improvement compared to the zero-shot CLIP via masking an average of only 2.56% parameters. Furthermore, our method is synergistic with most existing parameter-efficient tuning methods and can boost the performance on top of them. Project page can be found here (https://wuw2019.github.io/R-AMT/).

</details>

### ECO: Ensembling Context Optimization for Vision-Language Models.
- **链接**: [arXiv:2307.14063](https://arxiv.org/abs/2307.14063) · 📚 被引 7
- **作者**: Lorenzo Agnolucci, Alberto Baldrati, Francesco Todino, Federico Becattini, Marco Bertini, Alberto Del Bimbo
- **🏷️ 机构**: University of Florence,Italy, University of Siena,Italy
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image recognition has recently witnessed a paradigm shift, where vision-language models are now used to perform few-shot classification based on textual prompts. Among these, the CLIP model has shown remarkable capabilities for zero-shot transfer by matching an image and a custom textual prompt in its latent space. This has paved the way for several works that focus on engineering or learning textual contexts for maximizing CLIP's classification capabilities. In this paper, we follow this trend by learning an ensemble of prompts for image classification. We show that learning diverse and possibly shorter contexts improves considerably and consistently the results rather than relying on a single trainable prompt. In particular, we report better few-shot capabilities with no additional cost at inference time. We demonstrate the capabilities of our approach on 11 different benchmarks.

</details>

### Vision-Language Models Performing Zero-Shot Tasks Exhibit Disparities Between Gender Groups.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00294) · 📚 被引 3
- **作者**: Melissa Hall, Laura Gustafson, Aaron Adcock, Ishan Misra, Candace Ross
- **🏷️ 机构**: Meta AI
- **会议**: ICCV 2023

### Towards Vision-Language Mechanistic Interpretability: A Causal Tracing Tool for BLIP.
- **链接**: [arXiv:2308.14179](https://arxiv.org/abs/2308.14179) · [代码](https://github.com/vedantpalit/Towards-Vision-Language-Mechanistic-Interpretability) · 📚 被引 16
- **作者**: Vedant Palit, Rohan Pandey, Aryaman Arora, Paul Pu Liang
- **🏷️ 机构**: IIT Kharagpur, Reworkd.ai, Georgetown University
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Mechanistic interpretability seeks to understand the neural mechanisms that enable specific behaviors in Large Language Models (LLMs) by leveraging causality-based methods. While these approaches have identified neural circuits that copy spans of text, capture factual knowledge, and more, they remain unusable for multimodal models since adapting these tools to the vision-language domain requires considerable architectural changes. In this work, we adapt a unimodal causal tracing tool to BLIP to enable the study of the neural mechanisms underlying image-conditioned text generation. We demonstrate our approach on a visual question answering dataset, highlighting the causal relevance of later layer representations for all tokens. Furthermore, we release our BLIP causal tracing tool as open source to enable further experimentation in vision-language mechanistic interpretability by the community. Our code is available at https://github.com/vedantpalit/Towards-Vision-Language-Mechanistic-Interpretability.

</details>

### Towards an Exhaustive Evaluation of Vision-Language Foundation Models.
- **链接**: [出版页](https://doi.org/10.1109/ICCVW60793.2023.00041) · 📚 被引 3
- **作者**: Emmanuelle Salin, Stéphane Ayache, Benoît Favre
- **🏷️ 机构**: Aix Marseille Univ, Universit&#x00E9; de Toulon,CNRS, LIS,Marseille,France
- **会议**: ICCV 2023

### ClipCrop: Conditioned Cropping Driven by Vision-Language Model.
- **链接**: [arXiv:2211.11492](https://arxiv.org/abs/2211.11492) · 📚 被引 5
- **作者**: Zhihang Zhong, Mingxi Cheng, Zhirong Wu, Yuhui Yuan, Yinqiang Zheng, Ji Li et al.
- **🏷️ 机构**: The University of Tokyo,Japan, Microsoft Research
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> Image cropping has progressed tremendously under the data-driven paradigm. However, current approaches do not account for the intentions of the user, which is an issue especially when the composition of the input image is complex. Moreover, labeling of cropping data is costly and hence the amount of data is limited, leading to poor generalization performance of current algorithms in the wild. In this work, we take advantage of vision-language models as a foundation for creating robust and user-intentional cropping algorithms. By adapting a transformer decoder with a pre-trained CLIP-based detection model, OWL-ViT, we develop a method to perform cropping with a text or image query that reflects the user's intention as guidance. In addition, our pipeline design allows the model to learn text-conditioned aesthetic cropping with a small cropping dataset, while inheriting the open-vocabulary ability acquired from millions of text-image pairs. We validate our model through extensive experiments on existing datasets as well as a new cropping test set we compiled that is characterized by content ambiguity.

</details>

### TinyCLIP: CLIP Distillation via Affinity Mimicking and Weight Inheritance.
- **链接**: [arXiv:2309.12314](https://arxiv.org/abs/2309.12314) · 📚 被引 73
- **作者**: Kan Wu, Houwen Peng, Zhenghong Zhou, Bin Xiao, Mengchen Liu, Lu Yuan et al.
- **🏷️ 机构**: Sun Yat-sen University, Microsoft, Huazhong University of Science &amp; Technology
- **会议**: ICCV 2023

<details><summary>📄 arXiv 原始摘要（点击展开）</summary>

> In this paper, we propose a novel cross-modal distillation method, called TinyCLIP, for large-scale language-image pre-trained models. The method introduces two core techniques: affinity mimicking and weight inheritance. Affinity mimicking explores the interaction between modalities during distillation, enabling student models to mimic teachers' behavior of learning cross-modal feature alignment in a visual-linguistic affinity space. Weight inheritance transmits the pre-trained weights from the teacher models to their student counterparts to improve distillation efficiency. Moreover, we extend the method into a multi-stage progressive distillation to mitigate the loss of informative weights during extreme compression. Comprehensive experiments demonstrate the efficacy of TinyCLIP, showing that it can reduce the size of the pre-trained CLIP ViT-B/32 by 50%, while maintaining comparable zero-shot performance. While aiming for comparable performance, distillation with weight inheritance can speed up the training by 1.4 - 7.8 $\times$ compared to training from scratch. Moreover, our TinyCLIP ViT-8M/16, trained on YFCC-15M, achieves an impressive zero-shot top-1 accuracy of 41.1% on ImageNet, surpassing the original CLIP ViT-B/16 by 3.5% while utilizing only 8.9% parameters. Finally, we demonstrate the good transferability of TinyCLIP in various downstream tasks. Code and models will be open-sourced at https://aka.ms/tinyclip.

</details>

## 跨领域论文（完整笔记在其他领域）

- ViewRefer: Grasp the Multi-view Knowledge for 3D Visual Grounding. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Learning to Prompt CLIP for Monocular Depth Estimation: Exploring the Limits of Human Language. → [multi-camera-perception](../multi-camera-perception/Guideline%202023.md)
- Exploring Open-Vocabulary Semantic Segmentation from CLIP Vision Encoder Distillation Only. → [open-set-detection](../open-set-detection/Guideline%202023.md)
- Task-Oriented Multi-Modal Mutual Learning for Vision-Language Models. → [multimodal](../multimodal/Guideline%202023.md)
- Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models. → [continual-learning](../continual-learning/Guideline%202023.md)
- CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202023.md)
