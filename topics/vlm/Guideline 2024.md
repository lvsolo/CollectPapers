# VLM — 2024 Guideline

> 领域: 视觉语言模型（多模态大模型、CLIP 系、grounding）
> 论文数: 109 · 按重要性排序（引用数/标题信号启发式）

> 同领域其他年份: [2022](Guideline%202022.md)

### THRONE: An Object-Based Hallucination Benchmark for the Free-Form Generations of Large Vision-Language Models. **⭐⭐⭐⭐** (相关度: 75%)
- **链接**: [arXiv:2405.05256](https://arxiv.org/abs/2405.05256) · 📚 被引 19
- **作者**: Prannay Kaul, Zhizhong Li, Hao Yang, Yonatan Dukler, Ashwin Swaminathan, C. J. Taylor et al.
- **🏷️ 机构**: University of Oxford,VGG, AWS AI Labs
- **会议**: CVPR 2024
- **摘要（中）**: ①针对大型视觉语言模型（LVLM）在自由形式生成中的幻觉问题，现有基准主要评估特定问题格式（如多项选择）的幻觉（Type II），而忽略了开放式回答中的幻觉（Type I），且两者往往负相关。②提出了THRONE，一个基于对象的自动评估框架，利用公开语言模型识别LVLM自由输出中的幻觉，并计算信息量丰富的指标。③改进点在于无需外部API调用，且专门针对Type I幻觉进行量化评估。④通过在多个最新LVLM上的评估，表明现有指标的改进并不减少Type I幻觉，揭示了现有基准的局限性。
- **摘要（英）**: This paper addresses the hallucination issue in large vision-language models (LVLMs) during free-form generation, which is often overlooked by existing benchmarks focusing on specific question formats. It proposes THRONE, an object-based automatic framework that uses public language models to detect hallucinations and compute informative metrics. The evaluation shows that improvements in existing metrics do not reduce Type I hallucinations, highlighting the limitations of current benchmarks.
- **核心贡献**: 提出了首个针对LVLM自由形式生成中Type I幻觉的自动评估框架THRONE。
- **创新点**: 利用公开语言模型自动识别幻觉，无需外部API，并区分Type I和Type II幻觉。
- **结果**: 实验表明现有指标改进与Type I幻觉减少不相关，揭示了基准的不足。

### DeIL: Direct-and-Inverse CLIP for Open-World Few-Shot Learning.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02693) · 📚 被引 15
- **作者**: Shuai Shao, Yu Bai, Yan Wang, Baodi Liu, Yicong Zhou
- **🏷️ 机构**: Zhejiang Lab, China University of Petroleum (East China), Beihang University
- **会议**: CVPR 2024

### Towards Better Vision-Inspired Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01285) · 📚 被引 6
- **作者**: Yun-Hao Cao, Kaixiang Ji, Ziyuan Huang, Chuanyang Zheng, Jiajia Liu, Jian Wang et al.
- **🏷️ 机构**: Nanjing University,National Key Laboratory for Novel Software Technology, Ant Group
- **会议**: CVPR 2024

### DRESS : Instructing Large Vision-Language Models to Align and Interact with Humans via Natural Language Feedback.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01350) · 📚 被引 21
- **作者**: Yangyi Chen, Karan Sikka, Michael Cogswell, Heng Ji, Ajay Divakaran
- **🏷️ 机构**: SRI International, University of Illinois Urbana-Champaign
- **会议**: CVPR 2024

### Hallusionbench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01363) · 📚 被引 144
- **作者**: Tianrui Guan, Fuxiao Liu, Xiyang Wu, Ruiqi Xian, Zongxia Li, Xiaoyu Liu et al.
- **🏷️ 机构**: University of Maryland,College Park
- **会议**: CVPR 2024

### Language Models as Black-Box Optimizers for Vision-Language Models.
- **链接**: [arXiv:2309.05950](https://arxiv.org/abs/2309.05950) · 📚 被引 22
- **作者**: Shihong Liu, Samuel Yu, Zhiqiu Lin, Deepak Pathak, Deva Ramanan
- **🏷️ 机构**: Carnegie Mellon University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-language models (VLMs) pre-trained on web-scale datasets have demonstrated remarkable capabilities on downstream tasks when fine-tuned with minimal data. However, many VLMs rely on proprietary data and are not open-source, which restricts the use of white-box approaches for fine-tuning. As such, we aim to develop a black-box approach to optimize VLMs through natural language prompts, thereby avoiding the need to access model parameters, feature embeddings, or even output logits. We propose employing chat-based LLMs to search for the best text prompt for VLMs. Specifically, we adopt an automatic hill-climbing procedure that converges to an effective prompt by evaluating the performance of current prompts and asking LLMs to refine them based on textual feedback, all within a conversational process without human-in-the-loop. In a challenging 1-shot image classification setup, our simple approach surpasses the white-box continuous prompting method (CoOp) by an average of 1.5% across 11 datasets including ImageNet. Our approach also outperforms both human-engineered and LLM-generated prompts. We highlight the advantage of conversational feedback that incorporates both positive and negative prompts, suggesting that LLMs can utilize the implicit gradient direction in textual feedback for a more efficient search. In addition, we find that the text prompts generated through our strategy are not only more interpretable but also transfer well across different VLM architectures in a black-box manner. Lastly, we apply our framework to optimize the state-of-the-art black-box VLM (DALL-E 3) for text-to-image generation, prompt inversion, and personalization.

### Sonic VisionLM: Playing Sound with Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02537) · 📚 被引 16
- **作者**: Zhifeng Xie, Shengye Yu, Qile He, Mengtian Li
- **🏷️ 机构**: Shanghai University
- **会议**: CVPR 2024

### PeVL: Pose-Enhanced Vision-Language Model for Fine-Grained Human Action Recognition.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01784) · 📚 被引 12
- **作者**: Haosong Zhang, Mei Chee Leong, Liyuan Li, Weisi Lin
- **🏷️ 机构**: Institute for Infocomm Research (I2R), A *STAR,Singapore, Nanyang Technological University,Singapore
- **会议**: CVPR 2024

### Dual Memory Networks: A Versatile Adaptation Approach for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02713) · 📚 被引 43
- **作者**: Yabin Zhang, Wenjie Zhu, Hui Tang, Zhiyuan Ma, Kaiyang Zhou, Lei Zhang
- **🏷️ 机构**: HKPolyU, HKUST, HKBU
- **会议**: CVPR 2024

### SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01370) · 📚 被引 225
- **作者**: Boyuan Chen, Zhuo Xu, Sean Kirmani, Brian Ichter, Dorsa Sadigh, Leonidas J. Guibas et al.
- **🏷️ 机构**: Google DeepMind, Google Research
- **会议**: CVPR 2024

### Leveraging Vision-Language Models for Improving Domain Generalization in Image Classification.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02258) · 📚 被引 32
- **作者**: Sravanti Addepalli, Ashish Ramayee Asokan, Lakshay Sharma, R. Venkatesh Babu
- **🏷️ 机构**: Indian Institute of Science,Vision and AI Lab,Bangalore
- **会议**: CVPR 2024

### Active Prompt Learning in Vision Language Models.
- **链接**: [arXiv:2311.11178](https://arxiv.org/abs/2311.11178) · 📚 被引 9
- **作者**: Jihwan Bang, Sumyeong Ahn, Jae-Gil Lee
- **🏷️ 机构**: KAIST Michigan, State University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Pre-trained Vision Language Models (VLMs) have demonstrated notable progress in various zero-shot tasks, such as classification and retrieval. Despite their performance, because improving performance on new tasks requires task-specific knowledge, their adaptation is essential. While labels are needed for the adaptation, acquiring them is typically expensive. To overcome this challenge, active learning, a method of achieving a high performance by obtaining labels for a small number of samples from experts, has been studied. Active learning primarily focuses on selecting unlabeled samples for labeling and leveraging them to train models. In this study, we pose the question, "how can the pre-trained VLMs be adapted under the active learning framework?" In response to this inquiry, we observe that (1) simply applying a conventional active learning framework to pre-trained VLMs even may degrade performance compared to random selection because of the class imbalance in labeling candidates, and (2) the knowledge of VLMs can provide hints for achieving the balance before labeling. Based on these observations, we devise a novel active learning framework for VLMs, denoted as PCB. To assess the effectiveness of our approach, we conduct experiments on seven different real-world datasets, and the results demonstrate that PCB surpasses conventional active learning and random sampling methods. Code will be available in https://github.com/kaist-dmlab/pcb .

### FFF: Fixing Flawed Foundations in contrastive pre-training results in very strong Vision-Language models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01344) · 📚 被引 8
- **作者**: Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
- **🏷️ 机构**: Samsung AI Center Cambridge,UK
- **会议**: CVPR 2024

### PracticalDG: Perturbation Distillation on Vision-Language Models for Hybrid Domain Generalization.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02218) · 📚 被引 19
- **作者**: Zining Chen, Weiqiu Wang, Zhicheng Zhao, Fei Su, Aidong Men, Hongying Meng
- **🏷️ 机构**: Beijing University of Posts and Telecommunications,The school of Artificial Intelligence, Brunel University Uxbridge
- **会议**: CVPR 2024

### EgoThink: Evaluating First-Person Perspective Thinking Capability of Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01355) · 📚 被引 26
- **作者**: Sijie Cheng, Zhicheng Guo, Jingwen Wu, Kechen Fang, Peng Li, Huaping Liu et al.
- **🏷️ 机构**: Tsinghua University,Department of Computer Science and Technology, University of Toronto,Department of Electrical and Computer Engineering, Tsinghua University,Zhili College
- **会议**: CVPR 2024

### JoAPR: Cleaning the Lens of Prompt Learning for Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02711) · 📚 被引 6
- **作者**: Yuncheng Guo, Xiaodong Gu
- **🏷️ 机构**: Fudan University,Department of Electronic Engineering,Shanghai,China,200438
- **会议**: CVPR 2024

### RegionGPT: Towards Region Understanding Vision Language Model.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01309) · 📚 被引 54
- **作者**: Qiushan Guo, Shalini De Mello, Hongxu Yin, Wonmin Byeon, Ka Chun Cheung, Yizhou Yu et al.
- **🏷️ 机构**: The University of Hong Kong, NVIDIA
- **会议**: CVPR 2024

### Anchor-based Robust Finetuning of Vision-Language Models.
- **链接**: [arXiv:2404.06244](https://arxiv.org/abs/2404.06244) · 📚 被引 6
- **作者**: Jinwei Han, Zhiwen Lin, Zhongyisun Sun, Yingguo Gao, Ke Yan, Shouhong Ding et al.
- **🏷️ 机构**: School of Computer Science, Wuhan University, YouTu Lab, Tencent, Electronic Information School, Wuhan University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > We aim at finetuning a vision-language model without hurting its out-of-distribution (OOD) generalization. We address two types of OOD generalization, i.e., i) domain shift such as natural to sketch images, and ii) zero-shot capability to recognize the category that was not contained in the finetune data. Arguably, the diminished OOD generalization after finetuning stems from the excessively simplified finetuning target, which only provides the class information, such as ``a photo of a [CLASS]''. This is distinct from the process in that CLIP was pretrained, where there is abundant text supervision with rich semantic information. Therefore, we propose to compensate for the finetune process using auxiliary supervision with rich semantic information, which acts as anchors to preserve the OOD generalization. Specifically, two types of anchors are elaborated in our method, including i) text-compensated anchor which uses the images from the finetune set but enriches the text supervision from a pretrained captioner, ii) image-text-pair anchor which is retrieved from the dataset similar to pretraining data of CLIP according to the downstream task, associating with the original CLIP text with rich semantics. Those anchors are utilized as auxiliary semantic information to maintain the original feature space of CLIP, thereby preserving the OOD generalization capabilities. Comprehensive experiments demonstrate that our method achieves in-distribution performance akin to conventional finetuning while attaining new state-of-the-art results on domain shift and zero-shot learning benchmarks.

### SocialCounterfactuals: Probing and Mitigating Intersectional Social Biases in Vision-Language Models with Counterfactual Examples.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01138) · 📚 被引 15
- **作者**: Phillip Howard, Avinash Madasu, Tiep Le, Gustavo A. Lujan-Moreno, Anahita Bhiwandiwalla, Vasudev Lal
- **🏷️ 机构**: Intel Labs
- **会议**: CVPR 2024

### Visual Program Distillation: Distilling Tools and Programmatic Reasoning into Vision-Language Models.
- **链接**: [arXiv:2312.03052](https://arxiv.org/abs/2312.03052) · 📚 被引 38
- **作者**: Yushi Hu, Otilia Stretcu, Chun-Ta Lu, Krishnamurthy Viswanathan, Kenji Hata, Enming Luo et al.
- **🏷️ 机构**: Google Research, University of Washington
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Solving complex visual tasks such as "Who invented the musical instrument on the right?" involves a composition of skills: understanding space, recognizing instruments, and also retrieving prior knowledge. Recent work shows promise by decomposing such tasks using a large language model (LLM) into an executable program that invokes specialized vision models. However, generated programs are error-prone: they omit necessary steps, include spurious ones, and are unable to recover when the specialized models give incorrect outputs. Moreover, they require loading multiple models, incurring high latency and computation costs. We propose Visual Program Distillation (VPD), an instruction tuning framework that produces a vision-language model (VLM) capable of solving complex visual tasks with a single forward pass. VPD distills the reasoning ability of LLMs by using them to sample multiple candidate programs, which are then executed and verified to identify a correct one. It translates each correct program into a language description of the reasoning steps, which are then distilled into a VLM. Extensive experiments show that VPD improves the VLM's ability to count, understand spatial relations, and reason compositionally. Our VPD-trained PaLI-X outperforms all prior VLMs, achieving state-of-the-art performance across complex vision tasks, including MMBench, OK-VQA, A-OKVQA, TallyQA, POPE, and Hateful Memes. An evaluation with human annotators also confirms that VPD improves model response factuality and consistency. Finally, experiments on content moderation demonstrate that VPD is also helpful for adaptation to real-world applications with limited data.

### Semantic Shield: Defending Vision-Language Models Against Backdooring and Poisoning via Fine-Grained Knowledge Alignment.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.02344) · 📚 被引 3
- **作者**: Alvi Md. Ishmam, Christopher Thomas
- **🏷️ 机构**: Virginia Tech
- **会议**: CVPR 2024

### Efficient Test-Time Adaptation of Vision-Language Models.
- **链接**: [arXiv:2403.18293](https://arxiv.org/abs/2403.18293)
- **作者**: Adilbek Karmanov, Dayan Guan, Shijian Lu, Abdulmotaleb El Saddik, Eric P. Xing
- **🏷️ 机构**: （机构待查）
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Test-time adaptation with pre-trained vision-language models has attracted increasing attention for tackling distribution shifts during the test time. Though prior studies have achieved very promising performance, they involve intensive computation which is severely unaligned with test-time adaptation. We design TDA, a training-free dynamic adapter that enables effective and efficient test-time adaptation with vision-language models. TDA works with a lightweight key-value cache that maintains a dynamic queue with few-shot pseudo labels as values and the corresponding test-sample features as keys. Leveraging the key-value cache, TDA allows adapting to test data gradually via progressive pseudo label refinement which is super-efficient without incurring any backpropagation. In addition, we introduce negative pseudo labeling that alleviates the adverse impact of pseudo label noises by assigning pseudo labels to certain negative classes when the model is uncertain about its pseudo label predictions. Extensive experiments over two benchmarks demonstrate TDA's superior effectiveness and efficiency as compared with the state-of-the-art. The code has been released in \url{https://kdiaaa.github.io/tda/}.

### Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding.
- **链接**: [arXiv:2311.16922](https://arxiv.org/abs/2311.16922) · 📚 被引 184
- **作者**: Sicong Leng, Hang Zhang, Guanzheng Chen, Xin Li, Shijian Lu, Chunyan Miao et al.
- **🏷️ 机构**: DAMO Academy, Alibaba Group, Nanyang Technological University
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Large Vision-Language Models (LVLMs) have advanced considerably, intertwining visual recognition and language understanding to generate content that is not only coherent but also contextually attuned. Despite their success, LVLMs still suffer from the issue of object hallucinations, where models generate plausible yet incorrect outputs that include objects that do not exist in the images. To mitigate this issue, we introduce Visual Contrastive Decoding (VCD), a simple and training-free method that contrasts output distributions derived from original and distorted visual inputs. The proposed VCD effectively reduces the over-reliance on statistical bias and unimodal priors, two essential causes of object hallucinations. This adjustment ensures the generated content is closely grounded to visual inputs, resulting in contextually accurate outputs. Our experiments show that VCD, without either additional training or the usage of external tools, significantly mitigates the object hallucination issue across different LVLM families. Beyond mitigating object hallucinations, VCD also excels in general LVLM benchmarks, highlighting its wide-ranging applicability.

### PromptKD: Unsupervised Prompt Distillation for Vision-Language Models.
- **链接**: [arXiv:2403.02781](https://arxiv.org/abs/2403.02781) · 📚 被引 110
- **作者**: Zheng Li, Xiang Li, Xinyi Fu, Xin Zhang, Weiqiang Wang, Shuo Chen et al.
- **🏷️ 机构**: College of Computer Science, Nankai University,PCA Lab, VCIP, NKIARI,Shenzhen Futian, Ant Group,Tiansuan Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Prompt learning has emerged as a valuable technique in enhancing vision-language models (VLMs) such as CLIP for downstream tasks in specific domains. Existing work mainly focuses on designing various learning forms of prompts, neglecting the potential of prompts as effective distillers for learning from larger teacher models. In this paper, we introduce an unsupervised domain prompt distillation framework, which aims to transfer the knowledge of a larger teacher model to a lightweight target model through prompt-driven imitation using unlabeled domain images. Specifically, our framework consists of two distinct stages. In the initial stage, we pre-train a large CLIP teacher model using domain (few-shot) labels. After pre-training, we leverage the unique decoupled-modality characteristics of CLIP by pre-computing and storing the text features as class vectors only once through the teacher text encoder. In the subsequent stage, the stored class vectors are shared across teacher and student image encoders for calculating the predicted logits. Further, we align the logits of both the teacher and student models via KL divergence, encouraging the student image encoder to generate similar probability distributions to the teacher through the learnable prompts. The proposed prompt distillation process eliminates the reliance on labeled data, enabling the algorithm to leverage a vast amount of unlabeled images within the domain. Finally, the well-trained student image encoders and pre-stored text features (class vectors) are utilized for inference. To our best knowledge, we are the first to (1) perform unsupervised domain-specific prompt-driven knowledge distillation for CLIP, and (2) establish a practical pre-storing mechanism of text features as shared class vectors between teacher and student. Extensive experiments on 11 datasets demonstrate the effectiveness of our method.

### FairCLIP: Harnessing Fairness in Vision-Language Learning.
- **链接**: [arXiv:2403.19949](https://arxiv.org/abs/2403.19949) · 📚 被引 53
- **作者**: Yan Luo, Min Shi, Muhammad Osama Khan, Muhammad Muneeb Afzal, Hao Huang, Shuaihang Yuan et al.
- **🏷️ 机构**: Harvard University,Harvard Ophthalmology AI Lab, Tandon School of Engineering, New York University, New York University Abu Dhabi,Multimedia and Visual Computing Lab
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Fairness is a critical concern in deep learning, especially in healthcare, where these models influence diagnoses and treatment decisions. Although fairness has been investigated in the vision-only domain, the fairness of medical vision-language (VL) models remains unexplored due to the scarcity of medical VL datasets for studying fairness. To bridge this research gap, we introduce the first fair vision-language medical dataset Harvard-FairVLMed that provides detailed demographic attributes, ground-truth labels, and clinical notes to facilitate an in-depth examination of fairness within VL foundation models. Using Harvard-FairVLMed, we conduct a comprehensive fairness analysis of two widely-used VL models (CLIP and BLIP2), pre-trained on both natural and medical domains, across four different protected attributes. Our results highlight significant biases in all VL models, with Asian, Male, Non-Hispanic, and Spanish being the preferred subgroups across the protected attributes of race, gender, ethnicity, and language, respectively. In order to alleviate these biases, we propose FairCLIP, an optimal-transport-based approach that achieves a favorable trade-off between performance and fairness by reducing the Sinkhorn distance between the overall sample distribution and the distributions corresponding to each demographic group. As the first VL dataset of its kind, Harvard-FairVLMed holds the potential to catalyze advancements in the development of machine learning models that are both ethically aware and clinically effective. Our dataset and code are available at https://ophai.hms.harvard.edu/datasets/harvard-fairvlmed10k.

### The Neglected Tails in Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01234) · 📚 被引 31
- **作者**: Shubham Parashar, Zhiqiu Lin, Tian Liu, Xiangjue Dong, Yanan Li, Deva Ramanan et al.
- **🏷️ 机构**: Texas A&#x0026;M University, Carnegie Mellon University, Zhejiang Lab
- **会议**: CVPR 2024

### Jack of All Tasks, Master of Many: Designing General-purpose Coarse-to-Fine Vision-Language Model.
- **链接**: [arXiv:2312.12423](https://arxiv.org/abs/2312.12423) · 📚 被引 25
- **作者**: Shraman Pramanick, Guangxing Han, Rui Hou, Sayan Nag, Ser-Nam Lim, Nicolas Ballas et al.
- **🏷️ 机构**: Johns Hopkins University, Meta, University of Toronto
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The ability of large language models (LLMs) to process visual inputs has given rise to general-purpose vision systems, unifying various vision-language (VL) tasks by instruction tuning. However, due to the enormous diversity in input-output formats in the vision domain, existing general-purpose models fail to successfully integrate segmentation and multi-image inputs with coarse-level tasks into a single framework. In this work, we introduce VistaLLM, a powerful visual system that addresses coarse- and fine-grained VL tasks over single and multiple input images using a unified framework. VistaLLM utilizes an instruction-guided image tokenizer that filters global embeddings using task descriptions to extract compressed and refined features from numerous images. Moreover, VistaLLM employs a gradient-aware adaptive sampling technique to represent binary segmentation masks as sequences, significantly improving over previously used uniform sampling. To bolster the desired capability of VistaLLM, we curate CoinIt, a comprehensive coarse-to-fine instruction tuning dataset with 6.8M samples. We also address the lack of multi-image grounding datasets by introducing a novel task, AttCoSeg (Attribute-level Co-Segmentation), which boosts the model's reasoning and grounding capability over multiple input images. Extensive experiments on a wide range of V- and VL tasks demonstrate the effectiveness of VistaLLM by achieving consistent state-of-the-art performance over strong baselines across all downstream tasks. Our project page can be found at https://shramanpramanick.github.io/VistaLLM/.

### Building Vision-Language Models on Solid Foundations with Masked Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01348) · 📚 被引 8
- **作者**: Sepehr Sameni, Kushal Kafle, Hao Tan, Simon Jenni
- **🏷️ 机构**: University of Bern, Adobe Research
- **会议**: CVPR 2024

### Non-autoregressive Sequence-to-Sequence Vision-Language Models.
- **链接**: [arXiv:2403.02249](https://arxiv.org/abs/2403.02249) · 📚 被引 2
- **作者**: Kunyu Shi, Qi Dong, Luis Goncalves, Zhuowen Tu, Stefano Soatto
- **🏷️ 机构**: AWS AI Labs
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Sequence-to-sequence vision-language models are showing promise, but their applicability is limited by their inference latency due to their autoregressive way of generating predictions. We propose a parallel decoding sequence-to-sequence vision-language model, trained with a Query-CTC loss, that marginalizes over multiple inference paths in the decoder. This allows us to model the joint distribution of tokens, rather than restricting to conditional distribution as in an autoregressive model. The resulting model, NARVL, achieves performance on-par with its state-of-the-art autoregressive counterpart, but is faster at inference time, reducing from the linear complexity associated with the sequential generation of tokens to a paradigm of constant time joint inference.

### A Closer Look at the Few-Shot Adaptation of Large Vision-Language Models.
- **链接**: [arXiv:2312.12730](https://arxiv.org/abs/2312.12730) · 📚 被引 50
- **作者**: Julio Silva-Rodríguez, Sina Hajimiri, Ismail Ben Ayed, Jose Dolz
- **🏷️ 机构**: &#x00E9;TS Montreal
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Efficient transfer learning (ETL) is receiving increasing attention to adapt large pre-trained language-vision models on downstream tasks with a few labeled samples. While significant progress has been made, we reveal that state-of-the-art ETL approaches exhibit strong performance only in narrowly-defined experimental setups, and with a careful adjustment of hyperparameters based on a large corpus of labeled samples. In particular, we make two interesting, and surprising empirical observations. First, to outperform a simple Linear Probing baseline, these methods require to optimize their hyper-parameters on each target task. And second, they typically underperform -- sometimes dramatically -- standard zero-shot predictions in the presence of distributional drifts. Motivated by the unrealistic assumptions made in the existing literature, i.e., access to a large validation set and case-specific grid-search for optimal hyperparameters, we propose a novel approach that meets the requirements of real-world scenarios. More concretely, we introduce a CLass-Adaptive linear Probe (CLAP) objective, whose balancing term is optimized via an adaptation of the general Augmented Lagrangian method tailored to this context. We comprehensively evaluate CLAP on a broad span of datasets and scenarios, demonstrating that it consistently outperforms SoTA approaches, while yet being a much more efficient alternative.

### Label Propagation for Zero-shot Classification with Vision-Language Models.
- **链接**: [arXiv:2404.04072](https://arxiv.org/abs/2404.04072) · 📚 被引 15
- **作者**: Vladan Stojnic, Yannis Kalantidis, Giorgos Tolias
- **🏷️ 机构**: Czech Technical University in Prague,VRG, FEE, NAVER LABS Europe
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-Language Models (VLMs) have demonstrated impressive performance on zero-shot classification, i.e. classification when provided merely with a list of class names. In this paper, we tackle the case of zero-shot classification in the presence of unlabeled data. We leverage the graph structure of the unlabeled data and introduce ZLaP, a method based on label propagation (LP) that utilizes geodesic distances for classification. We tailor LP to graphs containing both text and image features and further propose an efficient method for performing inductive inference based on a dual solution and a sparsification step. We perform extensive experiments to evaluate the effectiveness of our method on 14 common datasets and show that ZLaP outperforms the latest related works. Code: https://github.com/vladan-stojnic/ZLaP

### Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation.
- **链接**: [arXiv:2404.01943](https://arxiv.org/abs/2404.01943) · 📚 被引 31
- **作者**: Zihan Wang, Xiangyang Li, Jiahao Yang, Yeqi Liu, Junjie Hu, Ming Jiang et al.
- **🏷️ 机构**: Institute of Computing Technology, Chinese Academy of Sciences,Beijing,China,100190, University of Wisconsin,Department of Computer Science,Madison,WI,USA, Indiana University,Department of Human-centered Computing,Indianapolis,IN,USA
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > Vision-and-language navigation (VLN) enables the agent to navigate to a remote location following the natural language instruction in 3D environments. At each navigation step, the agent selects from possible candidate locations and then makes the move. For better navigation planning, the lookahead exploration strategy aims to effectively evaluate the agent's next action by accurately anticipating the future environment of candidate locations. To this end, some existing works predict RGB images for future environments, while this strategy suffers from image distortion and high computational cost. To address these issues, we propose the pre-trained hierarchical neural radiance representation model (HNR) to produce multi-level semantic features for future environments, which are more robust and efficient than pixel-wise RGB reconstruction. Furthermore, with the predicted future environmental representations, our lookahead VLN model is able to construct the navigable future path tree and select the optimal path via efficient parallel evaluation. Extensive experiments on the VLN-CE datasets confirm the effectiveness of our method.

### SC- Tune: Unleashing Self-Consistent Referential Comprehension in Large Vision Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01242) · 📚 被引 6
- **作者**: Tongtian Yue, Jie Cheng, Longteng Guo, Xingyuan Dai, Zijia Zhao, Xingjian He et al.
- **🏷️ 机构**: Laboratory of Cognition and Decision Intelligence for Complex Systems, CASIA, State Key Laboratory of Multimodal Artificial Intelligence Systems, CASIA
- **会议**: CVPR 2024

### On the Test-Time Zero-Shot Generalization of Vision-Language Models: Do we Really need Prompt Learning?
- **链接**: [arXiv:2405.02266](https://arxiv.org/abs/2405.02266) · 📚 被引 34
- **作者**: Maxime Zanella, Ismail Ben Ayed
- **🏷️ 机构**: UCLouvain UMons, &#x00C9;ts Montr&#x00E9;al
- **会议**: CVPR 2024

- **摘要（英，原文）**:

  > The development of large vision-language models, notably CLIP, has catalyzed research into effective adaptation techniques, with a particular focus on soft prompt tuning. Conjointly, test-time augmentation, which utilizes multiple augmented views of a single image to enhance zero-shot generalization, is emerging as a significant area of interest. This has predominantly directed research efforts toward test-time prompt tuning. In contrast, we introduce a robust MeanShift for Test-time Augmentation (MTA), which surpasses prompt-based methods without requiring this intensive training procedure. This positions MTA as an ideal solution for both standalone and API-based applications. Additionally, our method does not rely on ad hoc rules (e.g., confidence threshold) used in some previous test-time augmentation techniques to filter the augmented views. Instead, MTA incorporates a quality assessment variable for each view directly into its optimization process, termed as the inlierness score. This score is jointly optimized with a density mode seeking process, leading to an efficient training- and hyperparameter-free approach. We extensively benchmark our method on 15 datasets and demonstrate MTA's superiority and computational efficiency. Deployed easily as plug-and-play module on top of zero-shot models and state-of-the-art few-shot methods, MTA shows systematic and consistent improvements.

### Investigating Compositional Challenges in Vision-Language Models for Visual Grounding.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01341) · 📚 被引 12
- **作者**: Yunan Zeng, Yan Huang, Jinjin Zhang, Zequn Jie, Zhenhua Chai, Liang Wang
- **🏷️ 机构**: Center for Research on Intelligent Perception and Computing (CRIPAC), Meituan
- **会议**: CVPR 2024

### Semantics-Aware Motion Retargeting with Vision-Language Models.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.00210) · 📚 被引 11
- **作者**: Haodong Zhang, Zhike Chen, Haocheng Xu, Lei Hao, Xiaofei Wu, Songcen Xu et al.
- **🏷️ 机构**: Zhejiang University, Huawei Noah&#x0027;s Ark Lab
- **会议**: CVPR 2024

### CLIP-KD: An Empirical Study of CLIP Model Distillation.
- **链接**: [出版页](https://doi.org/10.1109/CVPR52733.2024.01510) · 📚 被引 67
- **作者**: Chuanguang Yang, Zhulin An, Libo Huang, Junyu Bi, Xinqiang Yu, Han Yang et al.
- **🏷️ 机构**: Institute of Computing Technology,Chinese Academy of Sciences,Beijing,China
- **会议**: CVPR 2024

## 跨领域论文（完整笔记在其他领域）

- CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow. → [3d-detection](../3d-detection/Guideline%202024.md)
- YOLO-World: Real-Time Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Retrieval-Augmented Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- SHiNe: Semantic Hierarchy Nexus for Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- DetCLIPv3: Towards Versatile Generative Open-Vocabulary Object Detection. → [object-detection](../object-detection/Guideline%202024.md)
- ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- The Devil is in the Fine-Grained Details: Evaluating open-Vocabulary Object Detectors for Fine-Grained Understanding. → [object-detection](../object-detection/Guideline%202024.md)
- Open Vocabulary Semantic Scene Sketch Understanding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- CAT-Seg: Cost Aggregation for Open-Vocabulary Semantic Segmentation. → [multimodal](../multimodal/Guideline%202024.md)
- Open-vocabulary object 6D pose estimation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- OMG: Towards Open-vocabulary Motion Generation via Mixture of Controllers. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Open-Vocabulary Segmentation with Semantic-Assisted Calibration. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Emergent Open-Vocabulary Semantic Segmentation from Off-the-Shelf Vision-Language Models. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- OVMR: Open-Vocabulary Recognition with Multi-Modal References. → [multimodal](../multimodal/Guideline%202024.md)
- Open-Vocabulary Semantic Segmentation with Image Embedding Balancing. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- GOV-NeSF: Generalizable Open-Vocabulary Neural Semantic Fields. → [multi-camera-perception](../multi-camera-perception/Guideline%202024.md)
- OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual Representation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- SED: A Simple Encoder-Decoder for Open-Vocabulary Semantic Segmentation. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Transferable and Principled Efficiency for Open-Vocabulary Segmentation. → [network-pruning](../network-pruning/Guideline%202024.md)
- Visual Programming for Zero-Shot Open-Vocabulary 3D Visual Grounding. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- Abductive Ego-View Accident Video Understanding for Safe Driving Perception. → [multimodal](../multimodal/Guideline%202024.md)
- Consistency and Uncertainty: Identifying Unreliable Responses From Black-Box Vision-Language Models for Selective Visual Question Answering. → [multimodal](../multimodal/Guideline%202024.md)
- Distilling Vision-Language Models on Millions of Videos. → [video-understanding](../video-understanding/Guideline%202024.md)
- MADTP: Multimodal Alignment-Guided Dynamic Token Pruning for Accelerating Vision-Language Transformer. → [multimodal](../multimodal/Guideline%202024.md)
- MULTIFLOW: Shifting Towards Task-Agnostic Vision-Language Pruning. → [multimodal](../multimodal/Guideline%202024.md)
- VCoder: Versatile Vision Encoders for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- GeoChat: Grounded Large Vision-Language Model for Remote Sensing. → [multimodal](../multimodal/Guideline%202024.md)
- One Prompt Word is Enough to Boost Adversarial Robustness for Pre-Trained Vision-Language Models. → [network-pruning](../network-pruning/Guideline%202024.md)
- MoPE-CLIP: Structured Pruning for Efficient Vision-Language Models with Module-Wise Pruning Error Metric. → [network-pruning](../network-pruning/Guideline%202024.md)
- Volumetric Environment Representation for Vision-Language Navigation. → [3d-detection](../3d-detection/Guideline%202024.md)
- SyncMask: Synchronized Attentional Masking for Fashion-centric Vision-Language Pretraining. → [multimodal](../multimodal/Guideline%202024.md)
- ArGue: Attribute-Guided Prompt Tuning for Vision-Language Models. → [open-set-detection](../open-set-detection/Guideline%202024.md)
- PartDistill: 3D Shape Part Segmentation by Vision-Language Model Distillation. → [multimodal](../multimodal/Guideline%202024.md)
- MMA: Multi-Modal Adapter for Vision-Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts Adapters. → [continual-learning](../continual-learning/Guideline%202024.md)
- Iterated Learning Improves Compositionality in Large Vision-Language Models. → [self-supervised-vision](../self-supervised-vision/Guideline%202024.md)
- Source-Free Domain Adaptation with Frozen Multimodal Foundation Model. → [multimodal](../multimodal/Guideline%202024.md)
- Sieve: Multimodal Dataset Pruning Using Image Captioning Models. → [multimodal](../multimodal/Guideline%202024.md)
- MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation. → [multimodal](../multimodal/Guideline%202024.md)
- Multimodal Prompt Perceiver: Empower Adaptiveness, Generalizability and Fidelity for All-in-One Image Restoration. → [multimodal](../multimodal/Guideline%202024.md)
- ViP-LLaVA: Making Large Multimodal Models Understand Arbitrary Visual Prompts. → [multimodal](../multimodal/Guideline%202024.md)
- Honeybee: Locality-Enhanced Projector for Multimodal LLM. → [multimodal](../multimodal/Guideline%202024.md)
- LION : Empowering Multimodal Large Language Model with Dual-Level Visual Knowledge. → [multimodal](../multimodal/Guideline%202024.md)
- SmartEdit: Exploring Complex Instruction-Based Image Editing with Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Hallucination Augmented Contrastive Learning for Multimodal Large Language Model. → [multimodal](../multimodal/Guideline%202024.md)
- SEED-Bench: Benchmarking Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- BadCLIP: Dual-Embedding Guided Backdoor Attack on Multimodal Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Sniffer: Multimodal Large Language Model for Explainable Out-of-Context Misinformation Detection. → [multimodal](../multimodal/Guideline%202024.md)
- GLaMM: Pixel Grounding Large Multimodal Model. → [multimodal](../multimodal/Guideline%202024.md)
- TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- Link-Context Learning for Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- Data-Efficient Multimodal Fusion on a Single GPU. → [multimodal](../multimodal/Guideline%202024.md)
- Cloud-Device Collaborative Learning for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Towards Language-Driven Video Inpainting via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs. → [multimodal](../multimodal/Guideline%202024.md)
- GSVA: Generalized Segmentation via Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- Multimodal Pathway: Improve Transformers with Irrelevant Data from Other Modalities. → [multimodal](../multimodal/Guideline%202024.md)
- Exploring the Transferability of Visual Prompting for Multimodal Large Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MM-Narrator: Narrating Long-form Videos with Multimodal In-Context Learning. → [multimodal](../multimodal/Guideline%202024.md)
- TRINS: Towards Multimodal Language Models that Can Read. → [multimodal](../multimodal/Guideline%202024.md)
- Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language. → [multimodal](../multimodal/Guideline%202024.md)
- Enhancing Visual Document Understanding with Contrastive Learning in Large Visual-Language Models. → [multimodal](../multimodal/Guideline%202024.md)
- MLIP: Enhancing Medical Visual Representation with Divergence Encoder and Knowledge-guided Contrastive Learning. → [multimodal](../multimodal/Guideline%202024.md)
- Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding. → [multimodal](../multimodal/Guideline%202024.md)
- OmniViD: A Generative Framework for Universal Video Understanding. → [video-understanding](../video-understanding/Guideline%202024.md)
